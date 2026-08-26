---
otero_id: 6640
otero_key: "WHY3KPYB"
title: "<b>Research Commentary</b>—Using Income Accounting as the Theoretical Basis for Measuring IT Productivity"
authors: "Dennis O. Kundisch; Neeraj Mittal; Barrie R. Nault"
year: "2014"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0534"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/WHY3KPYB/fulltext/images/da6fca793dd2a7ea98c86beee75fc15a914f76fd3e188a620776a4e2e5e433bb.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Commentary—Using Income Accounting as the Theoretical Basis for Measuring IT Productivity

Dennis O. Kundisch, Neeraj Mittal, Barrie R. Nault

## To cite this article:

Dennis O. Kundisch, Neeraj Mittal, Barrie R. Nault (2014) Research Commentary—Using Income Accounting as the Theoretical Basis for Measuring IT Productivity. Information Systems Research 25(3):449-467. http://dx.doi.org/10.1287/isre.2014.0534

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/WHY3KPYB/fulltext/images/fbaef11d252e8f9a761818b41028b6a272b0d95fd8b56f8e8d76b1d1737b5e12.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Commentary

# Using Income Accounting as the Theoretical Basis for Measuring IT Productivity

Dennis O. Kundisch

Faculty of Business Administration and Economics, University of Paderborn, D-33098 Paderborn, Germany, dennis.kundisch@wiwi.uni-paderborn.de

Neeraj Mittal

Government of India, Ministry of Petroleum and Natural Gas, Shastri Bhawan, New Delhi-110001, India, mittal1967@gmail.com

Barrie R. Nault

Haskayne School of Business, University of Calgary, Calgary, Alberta T2N 1N4, Canada, nault@ucalgary.ca

W e use the under-recognized income accounting identity to provide an important theoretical basis for using the Cobb-Douglas production function in IT productivity analyses. Within the income accounting identity we partition capital into non-IT and IT capital and analytically derive an accounting identity (AI)-based Cobb-Douglas form that both nests the three-input Cobb-Douglas and provides additional terms based on wage rates and rates of return to non-IT and IT capital. To empirically confirm the theoretical derivation, we use a specially constructed data set from a subset of the U.S. manufacturing industry that involve elaborate calculations of rates of return—a data set that is infeasible to obtain for most productivity studies—to estimate the standard Cobb-Douglas and our AI-based form. We find that estimates from our AI-based form correspond with those of the Cobb-Douglas, and our AI-based form has significantly greater explanatory power. In addition, empirical estimation of both forms is relatively robust to the assumption of intertemporally stable input shares required to derive the AI-based form, although there may be limits. Thus, in the context of future research the Cobb-Douglas form and its application in IT productivity work have a theoretically and empirically supported basis in the accounting identity. A poor fit to data or unexpected coefficient estimates suggests problems with data quality or intertemporally unstable input shares. Our work also shows how some returns to IT that do not show up in output elasticities can be found in total factor productivity (TFP)—the novel ways inputs are combined to produce output. The critical insight for future research is that many unobservables that have been considered part of TFP can be manifested in rates of return to IT capital, non-IT capital, and labor—rates of return that are separated from TFP in our AI-based form. Finally, finding that the additional rates of return terms partially explain TFP confirms the need for future IT productivity researchers to incorporate time-varying TFP in their models.

Keywords: information systems; IT policy and management; economics of IS; income accounting identity; IT productivity; production function

History: Chris Forman, Senior Editor; Chris Forman, Associate Editor. This paper was received on February 17, 2013, and was with the authors 10 months for 3 revisions.

## 1. Introduction

The study of returns to IT investment through production theory has been the source of substantial contributions to both knowledge and practice. Although research in this area occurred before, the starting point for the cumulative tradition is usually seen to be Brynjolfsson and Hitt (1996). This and subsequent work used a mathematical function to represent a production function that embodies the relationship between inputs and outputs. However, the level of analysis in which a production function can be used to measure the relationship between inputs and output is less clear. This is embodied in part by the Cambridge Capital Theory Controversies (see, e.g., Robinson 1953–54, Sraffa 1960, Solow 1955–56, and Samuelson 1962 for seminal contributions to the debate, and Cohen and Harcourt 2003 for a recent review article) whereby Cambridge (UK) theorists questioned whether a production function could yield meaningful measures when aggregated to industry or economy levels and whether an aggregate production function exists at all. This is due to two concerns.

One is that different physical inputs have to be aggregated into a single input measure such as aggregating hardware, software, and telecommunications equipment as IT capital. The other is that the mathematical conditions to construct an aggregate production function from a set of different firm-specific production functions are quite restrictive. Indeed, the same aggregation concerns applies to many firm-level studies where Fortune 500 firms often aggregate dissimilar divisions, and divisions have portfolios of products, each with differing inputs and production functions. Meaningful measurement is complicated because production functions contain an element called total factor productivity (TFP) that represents effects on productivity that are not directly attributable to individual inputs. TFP is often interpreted as technological progress and is also known as the Solow residual or as multifactor productivity (MFP). Consequently, returns to IT measured through production functions are sometimes viewed as disconnected from generators of IT value that occur at the process level.

We counter the issue of whether aggregate production functions exist and what this means for measurement by using an important and under-recognized perspective, the income accounting identity, to provide a theoretical basis for the Cobb-Douglas production function—the form used most extensively in the literature empirically investigating returns to IT. The Cobb-Douglas has been commonly used because its parameters are easily interpretable as economic quantities and its good fit with data as a flexible exponential form. The theoretical basis for the Cobb-Douglas that we derive is based on the income accounting identity, which is always true and measures value added as the sum of wages and return on capital. When the latter is partitioned it can be used to identify returns to IT.

Shaikh (1974) showed that with two inputs, labor and capital, the income accounting identity leads to a variant of the Cobb-Douglas. Relative to that work, we show how an income accounting identity that separates IT capital from non-IT capital can lead to an accounting identity-based Cobb-Douglas form that we refer to as the AI-based Cobb-Douglas. This form nests the commonly used Cobb-Douglas, effectively providing a more robust theoretical basis for the historical studies using the Cobb-Douglas to estimate returns to IT, and the additional terms in the AI-based Cobb-Douglas account for part of TFP. Then we empirically test the new form, which has not been done before, using a specially constructed data set that has the additional measures we need to estimate the AI-based Cobb-Douglas—a data set that is impractical to collect in most productivity studies. We run the estimation and compare the results with estimates of the Cobb-Douglas showing a strong empirical correspondence between the forms. Furthermore, we empirically examine the single assumption required to derive the AI-based Cobb-Douglas, constant input shares, and find the forms are robust to large deviations. Consequently, the accounting identity as a key theoretical basis for IT productivity research is compelling and provides important insights into why and how high quality estimates are consistently obtained for the contributions of IT to productivity in the literature.

We believe this work makes a substantial scientific contribution to future research by providing an empirically substantiated theoretical basis for the use of the Cobb-Douglas form in IT productivity analysis, arguably one of the most important developments in the IT field in the last 20 years, and a theory-based explanation for why past results (post-productivity paradox) in the literature have been so significant. In the process, we explain how the Cobb-Douglas is valid for estimation at the firm, industry, sector, and economy levels, indicating that aggregation does not invalidate the use of the Cobb-Douglas form. Thus, there are also beneficial implications of our work for future researchers: essentially that the Cobb-Douglas exponential form has a rigorous theoretical accounting identity basis.

Our work also shows how some returns to IT that do not show up in output elasticities can be found in TFP. The critical insight for future research is that many unobservables that have been considered part of TFP can be manifested in rates of return to IT capital, non-IT capital, and labor—rates of return that are separated from TFP in our AI-based Cobb-Douglas. This supports the current research program of drilling into TFP to uncover otherwise unobservable effects of IT and supports a potential future focus on explanations behind different rates of return due to IT. This includes differences in organization processes, labor quality, IT and overall management, strategy, organization form, transaction costs and outsourcing, and IT implementations. Indeed, IT has been hypothesized, and sometimes shown, to contribute to TFP through organizational capital (Brynjolfsson and Hitt 2003), knowledge spillovers (Hitt and Tambe 2006, Tambe and Hitt 2010), and supply chain spillovers (Cheng and Nault 2007, 2012).

## 1.1. Aggregation in Production

Aggregation in production has been studied for more than a half century in economics, and the goal was to specify conditions under which aggregation was internally consistent—that is, whether mathematical forms of production functions could be aggregated into a parsimonious and interpretable production function such as a Cobb-Douglas at the establishment, firm, industry, or economy level. This so-called

Cambridge Capital Theory Controversy is fundamentally connected to the income accounting identity because the Cobb-Douglas form can be derived from this identity. There has been no resolution to the controversy, with Nobel prize–winning scholars weighing in on each side (e.g., Simon 1979; Samuelson 1979 questioning aggregation; Stiglitz 1974; Solow 1974, 1987 supporting aggregation).

There are three aggregation issues. The first two are mathematical conditions for aggregation related to estimation of the same production function form (e.g., Cobb-Douglas) at different levels of analysis. The first issue is whether different inputs can be aggregated into a single input measure. Aggregations we commonly use are skilled and unskilled work as labor. Other examples include aggregating machines, vehicles, etc., together into non-IT capital and aggregating hardware, software, and telecommunications equipment as IT capital. This aggregation issue affects even product-level productivity analyses. Leontief (1947a, b) dealt with aggregation of variables into homogenous groups and showed that if the marginal rate of substitution of the individual inputs in the aggregated group of inputs is independent of inputs that are not in that group, then that group of inputs can be aggregated. If the production function is a Cobb-Douglas with IT capital, non-IT capital, and labor inputs, then because the Cobb-Douglas satisfies these independence conditions we can aggregate within these input groups. Notice that this aggregation issue does not apply to the output side with multiple products as this is an aggregation of output dollars, and not different subcategories of inputs that have differing productivity characteristics. The second issue is whether a firm-, industry-, or economy-level production function can be aggregated from a set of establishments (assuming single-product establishments with production functions that do not suffer from the first aggregation issue above), each having different production functions. Nataf (1948) proved that such an aggregation is valid if the individual firm production functions are additively separable in inputs. This condition holds for the log-linear Cobb-Douglas form. Nonetheless, some argue this is a restrictive condition. Using sim ulation experiments, Fisher (1971) suggested that the requirements for aggregation to the economy-level are unrealistic. However, Stiglitz (1974, p. 899) concludes, “Under most circumstances and for most problems, the errors introduced as a consequence of aggregation of the kind involved in the standard macro-analysis are not too important …<sup>˙</sup>’’

The third issue concerns whether an aggregate production function can provide useful measures independent of the information contained in the income accounting identity, and as we show, this indirectly obviates measurement aspects of the first two issues. Shaikh (1974), whose analytical approach we adopt, showed with capital and labor that the Cobb-Douglas was an algebraic manipulation of the accounting identity. Following this, many Cambridge (UK) scholars argued that an aggregate production function was not a useful construct. Indeed, after showing that the accounting identity leads to the Cobb-Douglas, Shaikh (1974, p. 117) concludes, “Therefore, precisely because 45’5 8the resulting Cobb-Douglas9 is a mathematical relationship, holding true for large classes of data associated with constant shares, it cannot be interpreted as a production function, or any production relation at all.”

In contrast, the Cambridge (U.S.) scholars (e.g., Solow 1974) argued that an aggregate production function such as the Cobb-Douglas was a useful empirical construct relating inputs to outputs without the need for input share data (the basis of the income accounting identity) and had been successful at estimating marginal products that correspond with observed input prices. As Solow (1974, p. 121) states, “When someone claims that production functions work, he means (a) that they give a good fit to input-output data without the intervention of data deriving from factor shares; and (b) that the function so fitted has partial derivatives that closely mimic factor prices.”

Along with the arguments above, there is empirical evidence that the Cobb-Douglas form is robust. Gurbaxani et al. (2000) found that a Cobb-Douglas used to predict IT spending as a function of personnel and hardware was independent of scale and time and found that the homotheticity of IT spending supports the aggregation of hardware and of personnel each into single measures. Van Garderen et al. (2000) found that least squares estimates of some aggregate loglinear models like the Cobb-Douglas can yield consistent estimates of the output elasticities with some restrictions on the distribution of aggregate shocks. This is consistent with other research that suggests that the basic requirements for sensible aggregation may be met for firms in the same industry or for narrow sectors of the economy (Walters 1963).

## 1.2. Total Factor Productivity

The additional terms in our AI-based Cobb-Douglas account for part of TFP. Generally, TFP represents the (unspecified) ways that inputs combine to produce output outside of their direct representation in the production function. The result of aggregation to different levels makes it hard to interpret whether TFP contains product-, firm-, or industry-level effects or some combination. Isolating the role of IT in TFP is even more challenging, although it is clear that IT is an important contributor to TFP at the sector level (Oliner and Sichel 2000), the industry level (Stiroh 2002), and the firm level (Brynjolfsson and Hitt 2003).

Several studies have used variants of the Cobb-Douglas to explain the influence of IT on TFP. Hitt and Tambe (2006) examined within-industry productivity spillovers of IT from an industry knowledge pool using firm-level data from 1987 to 1993, where the spillovers were modeled as an element of TFP. They found significant within-industry IT spillovers, although lower than those previously estimated. In a recent study using employee micro-data, Tambe and Hitt (2010) found that regional differences in IT productivity are in part attributable to knowledge spillovers that come from employees changing employers—knowledge spillovers contained in TFP. Using manufacturing industry-level data from 1987 to 1999, Cheng and Nault (2007) studied between-industry productivity spillovers of IT that occur from a mismeasurement of the value of intermediate inputs. Specifying a Cobb-Douglas that modeled the mismeasurement of intermediate inputs as an element of TFP, they found significant IT spillovers from IT-induced quality improvements in intermediate inputs. Subsequently, using the data set described above and 1998–2005 economywide industry-level data, Cheng and Nault (2012) found that customer-driven IT spillovers depend on relative industry concentration, where both the spillover and the relationship with industry concentration are elements of TFP.

Brynjolffson and Hitt (2003) hypothesized the existence of unmeasured inputs such as organizational capital in making up TFP and related this to growth in computer capital. Using firm-level data from 1987 to 1994 and Cobb-Douglas related forms, they found that the long-run contribution of computerization is significantly higher than short-run (annual) returns to computer capital, and thus computer capital together with unmeasured inputs in the long run contribute to TFP. Bulkley and Van Alstyne (2004) hypothesized that the unmeasured inputs could be captured by focusing on how information and connectivity influence productivity distinct from measures of computer capital. Mittal and Nault (2009) modeled labor and non-IT capital as an exponential function of IT capital to capture indirect effects of IT on the productive efficiency of the other inputs, where the indirect effects were captured as an additional term in the Cobb-Douglas, hence explaining part of TFP. Using industry-level data from 1953 to 2000, they found that indirect effects of IT on the productive efficiency of labor and non-IT capital were significant across manufacturing in the United States, and were more significant in IT-intensive industries.

TFP is usually taken to be the constant in a Cobb-Douglas related form, but other unspecified ways that inputs combine to produce output could be contained in the error term. The stochastic frontier approach used by Lee and Barua (1999) in overall IT productivity and by Menon et al. (2000) examining IT productivity in healthcare partitions the error into technical and allocative inefficiency. Technical inefficiency captures the differences between firms in converting inputs to outputs, and allocative inefficiency captures the degree to which firms are not allocating resources at their optimal levels. Accounting for these inefficiencies, Lee and Barua (1999) found higher contributions from IT inputs using the stochastic frontier approach than from using the standard production function approach and that IT intensity reduced inefficiency. Menon et al. (2000) found that both IT and medical IT capital had a positive influence on output.

## 1.3. Our Results

To begin, we are agnostic about the controversy regarding whether aggregate production functions exist independent of specific mathematical functions that represent input and output relationships. Our view of this controversy, a controversy that is absent from the IT literature, is that it confounds the concept of a production function with measuring productivity using a mathematical form that yields clean economic interpretations. Indeed, this is the essence of Solow’s (1974) response to Shaikh (1974) embedded in the two quotes we provide in §1.1. At least at the industry level, numerous articles have shown that a production function approach has intellectual contributions to offer—for instance, those industry-level studies referenced in the prior subsection. Furthermore, it has been shown elsewhere that different production function forms are derivable from the accounting identity, albeit with more elaborate assumptions (e.g., Felipe 2000 for the Translog or Felipe and McCombie 2001 for the Constant Elasticity of Substitution). Therefore, we take the accounting identity derivation of the Cobb-Douglas as a way to add a more rigorous and complementary theoretical basis to the use of production functions—like the Cobb-Douglas—to measure the returns to IT. Here we take the concept of theory to mean building from a set of axioms (accounting rules) to a statement of truth (the income accounting identity) and then deriving an implication of that truth (the AI-based Cobb-Douglas that nests the Cobb-Douglas).

As we discussed briefly above, we extend the algebraic steps from Shaikh (1974) to include IT capital as a separate input, we show analytically that with the mild condition that input shares are relatively stable—a condition that is likely to hold in the medium term (for example, six to eight years)—the income accounting identity can be expressed as a variant of the Cobb-Douglas, the AI-based Cobb-Douglas, that nests the Cobb-Douglas and has additional terms—terms that relate to input-share weighted rates of return to each of the inputs. This means that input shares and rates of return to the inputs are in part explained by TFP. This, in turn implies that TFP is time varying. In addition, the income accounting identity is an ex post relationship that holds at all levels of aggregation, which provides a basis for the Cobb-Douglas and the AI-based Cobb-Douglas regardless of the level of aggregation. That is, the first two aggregation issues described above—aggregation of different inputs into a single input and the aggregation of production functions from the establishmentlevel to higher levels—do not apply. Thus, the income accounting identity provides a theoretical basis for the Cobb-Douglas form and is a unifying concept for the identification of TFP. In this, we highlight an important and under-recognized phenomenon—the theoretical relationship between the income accounting identity and the Cobb-Douglas form—that underlies a substantial amount of IT productivity research. We also provide a critical and (we hope) insightful critique of the so-called Cambridge controversies by concentrating on what these controversies showed— namely, that the income accounting identity, which must always be true, leads to the Cobb-Douglas (with a mild condition), both validating and explaining the robust estimates and fit of IT productivity data to the Cobb-Douglas form.

Then we detail a specially constructed set of industry-level data gathered for the purposes of testing the correspondence between the AI-based Cobb-Douglas and the Cobb-Douglas. The set of data is specially constructed because of the additional terms requiring rates of return in the AI-based Cobb-Douglas and because U.S. data sources only maintain the data required to compute these returns for some industries. Obtaining such a data set is infeasible for most productivity studies, and our focus is using the data to empirically confirm the theoretical correspondence between the AI-based Cobb-Douglas and the Cobb-Douglas rather than suggesting our AI-based form be used more generally.

We then estimate the Cobb-Douglas and the AIbased Cobb-Douglas on our specially constructed data set. In the estimation we find that for periods when the input share of IT capital is relatively stable—the condition required for mathematically expressing the income accounting identity as a variant of the Cobb-Douglas—the Cobb-Douglas and the AI-based Cobb-Douglas fit the data very well, the latter not surprising because it nests the Cobb-Douglas. More importantly, the estimates from the AI-based Cobb-Douglas are internally consistent and significant beyond the Cobb-Douglas, substantiating the theoretical correspondence between the two forms.

This means that estimation with aggregated data can yield results that accurately measure the relationship between inputs and output so that inferences about productivity can be made.

Moreover, it means that the additional terms relating to rates of return to the inputs that are in the AIbased Cobb-Douglas form explain a significant part of TFP. From this, future research can incorporate the insight that many of the impacts of IT that are hidden in the Cobb-Douglas TFP may be accessible through rates of return on IT and other inputs. This would allow researchers to benefit because otherwiseunobservable effects of IT in a production function context may become observable when identifying the impacts of IT on rates of return. This latter point is particularly important because our results provide evidence that returns to the inputs related to IT, such as organizational capital and various spillovers that have been found to be contained in TFP, may be effects that are alternatively captured by wage rates and rates of return. Indeed, relating specific IT investments to rates of return can be an actionable and compelling way to uncover sources of IT value, and our results allow these sources of IT value to be directly related to IT productivity.

## 1.4. Operational Implications for Researchers

There are several important operational implications for researchers using production functions in their work. First, the critical assumption required to derive the Cobb-Douglas from the accounting identity is the relative stability of input shares. Consequently, when using the Cobb-Douglas as a production function in their work, researchers should examine the intertemporal stability of input shares in their data sets. As we found, the Cobb-Douglas and the AI-based Cobb-Douglas are robust to fairly large deviations in input shares, but there may be limits: as will be detailed in our analysis, our split sample used to define periods over which the input shares were more stable produced results that were more consistent and significant than the results over a longer period. Moreover, intertemporally stable input shares are less likely when studying emerging technology phenomena, making the Cobb-Douglas less well suited. This is perhaps why early returns to IT studies had difficulty finding significant effects of IT.

Second, the income accounting identity as a theoretical basis for the Cobb-Douglas means that a good econometric fit of productivity data to the Cobb-Douglas should be expected so long as the input shares are relatively stable. A poor fit or unexpected coefficient estimates for the output elasticities such as insignificant or negative coefficients suggest there are problems with the quality of the underlying data and/or input shares that change substantially over the period of the data set. As we suggest, it is usually infeasible to obtain the data required to estimate the AI-based Cobb-Douglas, so it is not possible to validate the accounting identity directly with most data sets.

Third, researchers should expect output elasticities to reflect input shares because these are the dual interpretations of the exponents (or coefficients in log form) of the Cobb-Douglas when it is used as a production function. Ultimately, to monetize the contribution of an input such as IT capital, it is necessary to compute the marginal product. It is also useful to model TFP as time varying because it contains rates of return on the inputs, which at the minimum can be done using time fixed effects.

Finally, there are no aggregation issues with using production functions for measurement at the firm, industry, sector, or even economy level, so long as the interpretation of results is applied to that level. In terms of measurement, because the accounting identity is invariant to the objectives of an establishment or a firm, the accounting identity basis for the Cobb-Douglas removes the concerns associated with heterogeneous objectives of establishments or firms such as profit maximization, cost minimization, or even growth maximization.

## 2. The Aggregate Production Function and the Income Accounting Identity

## 2.1. Production Functions

A production function is a technological relationship confronting a firm that describes output as a function of inputs. The firm chooses the combination of inputs that produces a profit-maximizing level of output. At the firm level a production function can be defined as $Y = f ( x )$ where Y is output (measured as value added) and x is a vector of inputs containing labor L, non-IT capital $K ,$ and IT capital Z. We take f 4x5 to have the usual properties that make a unique profit-maximizing level of output possible: single valued, nonnegative, and real for all finite x, monotonic, concave, continuous, and twice continuously differentiable. We use a production function with value added rather than output because the difference is intermediate inputs added to each side and our focus is not on intermediate inputs. Our analytical results remain qualitatively the same if we add intermediate inputs.

Because of the issues of aggregation and that the Cobb-Douglas at the firm level mitigates some of these issues, the Cobb-Douglas has been the most frequently used production function in returns to IT research to estimate output elasticities at industry, sector, and economy levels. We write the Cobb-Douglas with three inputs

$$
Y = S L ^ {\alpha} K ^ {\beta} Z ^ {\gamma}.\tag{1}
$$

The variables Y , L, K, and Z are as above, and as is common in production functions these variables are measured as quantities. That is, $Y , K ,$ and Z are measured in real dollars, and L is measured in hours or full-time equivalents. The variable Y is a revenuebased measure that may contain more effects than simply productivity, an issue we return to at the end of the conclusion. The parameter $S$ is neutral (or disembodied) technological change otherwise known as TFP. A neutral technology implies that as S increases, output increases without the need to increase inputs. In this way S representing TFP is a “black box” of effects from the inputs that arise in part through ITrelated omitted variables such as organizational capital, knowledge spillovers, supply chain spillovers, and indirect effects. In (1), $\alpha , \beta ,$ and  are the output elasticities with respect to labor, non-IT capital, and IT capital, respectively.

## 2.2. Relationship to the Income Accounting Identity

Our derivation below extends the algebraic steps of Shaikh (1974) and Felipe (2001) by separating IT capital from non-IT capital, focusing on the role of IT capital in the analysis. The income accounting identity states that value added is equal to the wage bill plus the operating surplus—in other words, wages and total return on capital. For gross output the income accounting identity includes payments to intermediate inputs such as materials, energy, and purchased services in addition to the wage bill and operating surplus. The operating surplus is the profit made on capital and in principle can be divided into operating surplus on IT capital and operating surplus on non-IT capital, thereby isolating the profits made from IT capital. Using the income accounting identity we show that if input shares are constant over time, then we can derive the Cobb-Douglas form for value added and inputs in dollars. Thus, there is a correspondence between the Cobb-Douglas form representing an underlying aggregate technological relationship and aggregate level dollar data underlying the ex post income accounting identity (Samuelson 1979, p. 933) when input shares are intertemporally constant.

Adding time subscripts to all variables to indicate time dependence, our form of the income accounting identity for the three inputs is

$$
Y _ {t} \equiv \omega_ {t} L _ {t} + u _ {t} K _ {t} + v _ {t} Z _ {t},\tag{2}
$$

where $\omega _ { t }$ is the wage rate, $u _ { t }$ is the ex post rate of return on non-IT capital, and $v _ { t }$ is the ex post rate of return on IT capital. The variables $Y _ { t } , L _ { t } , K _ { t } ,$ , and $Z _ { t }$ are as in (1). The relation in (2) is true for all periods in that the value added in any period equals the sum of the wage bill and both types of profits in that period. As the income accounting identity does not make any assumptions about profit maximization, market structure, the nature of competition, or technology, it is an identity at any level of aggregation. That is, the income accounting identity holds at the business unit, firm, industry, sector, and economy levels.

We rewrite (2) by dividing on both sides by $Y _ { t }$ to get

$$
1 = \frac {\omega_ {t} L _ {t}}{Y _ {t}} + \frac {u _ {t} K _ {t}}{Y _ {t}} + \frac {v _ {t} Z _ {t}}{Y _ {t}} = a _ {t} + b _ {t} + c _ {t},\tag{3}
$$

where $a _ { t } = \omega _ { t } L _ { t } / Y _ { t } , \ b _ { t } = u _ { t } K _ { t } / Y _ { t } ,$ and $c _ { t } = v _ { t } Z _ { t } / Y _ { t } ,$ respectively. Each of these terms represents the proportion of the value added accruing to that input. We now totally differentiate (2) with respect to time. Denoting the time derivative of an arbitrary variable X by $d { \bar { X _ { / } } } d t = { \dot { X } }$ , we get

$$
\dot {Y} _ {t} = \dot {\omega} _ {t} L _ {t} + \omega_ {t} \dot {L} _ {t} + \dot {u} _ {t} K _ {t} + u _ {t} \dot {K} _ {t} + \dot {v} _ {t} Z _ {t} + v _ {t} \dot {Z} _ {t}.
$$

This equation gives the components of growth in terms of growth in rates of return and in input levels. Dividing this equation throughout by $Y _ { t } ,$ using (3), and denoting the growth rate of a variable X by $\varphi _ { X }$ so that $\varphi _ { X } = \stackrel { \smile } { ( { d X } / { \bar { d t } } ) } ( 1 / X ) = \dot { X } / X ,$ , after a small bit of algebra we have

$$
\varphi_ {y _ {t}} = a _ {t} \varphi_ {\omega_ {t}} + b _ {t} \varphi_ {u _ {t}} + c _ {t} \varphi_ {v t} + a _ {t} \varphi_ {l _ {t}} + b _ {t} \varphi_ {k _ {t}} + c _ {t} \varphi_ {z _ {t}},\tag{4}
$$

where $\varphi _ { y _ { t } } , \ \varphi _ { l _ { t } } , \ \varphi _ { k _ { t } } ,$ and $\varphi _ { z _ { t } }$ are the growth rates of value added, labor hours, non-IT capital, and IT capital, respectively. As well, $\varphi _ { \omega _ { t } } , \varphi _ { u _ { t } } ,$ and $\varphi _ { v _ { t } }$ are growth rates of the wage rate, of the rate of return on non-IT capital, and of the rate of return on IT capital, respectively. Thus, the growth rate of value added is a weighted sum of the growth rates in rates of return and in input levels, where the weights are input shares. We do not need any assumptions related to production technology or profit maximization (the behavioral view of a production function) to derive this equation. Combining the first three terms in (4) as

$$
\varphi_ {t} = a _ {t} \varphi_ {\omega_ {t}} + b _ {t} \varphi_ {u _ {t}} + c _ {t} \varphi_ {v _ {t}},\tag{5}
$$

then $\varphi _ { t }$ represents the weighted average of the growth rates of the wage rate, of the rate of return on non-IT capital, and of the rate of return on IT capital. The weights $a _ { t } , b _ { t } ,$ , and $c _ { t }$ are the proportions of value added accruing to each input as above. We can then write the growth rate of value added as

$$
\varphi_ {y _ {t}} = \varphi_ {t} + a _ {t} \varphi_ {l _ {t}} + b _ {t} \varphi_ {k _ {t}} + c _ {t} \varphi_ {z _ {t}}.\tag{6}
$$

Suppose that the proportion of value added accruing to each input is constant over time. This is most often the case in the short and medium term (for example, six to eight years) for most industries. Then we can drop the time dependence of the input shares: $a _ { t } = a ,$ $b _ { t } = b ,$ and $c _ { t } = c .$ . Multiplying both sides by dt and noting that for an arbitrary variable $X , ~ \varphi _ { x _ { t } } \dot { d t } =$ $( 1 / X _ { t } ) ( d X _ { t } / d t ) d t = d X _ { t } / X _ { t } ,$ we can rewrite (6) that describes the growth rate of value added as

$$
\frac {d Y _ {t}}{Y _ {t}} = a \frac {d \omega_ {t}}{\omega_ {t}} + b \frac {d u _ {t}}{u _ {t}} + c \frac {d v _ {t}}{v _ {t}} + a \frac {d L _ {t}}{L _ {t}} + b \frac {d K _ {t}}{K _ {t}} + c \frac {d Z _ {t}}{Z _ {t}}.
$$

Integrating yields

$$
Y _ {t} = \Lambda \omega_ {t} ^ {a} u _ {t} ^ {b} v _ {t} ^ {c} L _ {t} ^ {a} K _ {t} ^ {b} Z _ {t} ^ {c},\tag{7}
$$

where input proportions sum to unity, that $\mathrm { i } s , a + b +$ $c = 1$ as per the income accounting identity (3). The form in (7) resembles the Cobb-Douglas in (1) as far as the two capital terms and the labor term are concerned. However, (7) is simply a different form of the income accounting identity in (2) under the condition of intertemporally constant input shares; in other words, when this condition holds, then (7) and (2) are equivalent.

The difference between the Cobb-Douglas in (1) and the income accounting identity in (7) is that the latter contains additional multiplicative terms consisting of the wage rate and the two rates of return each raised to their input shares. Under a Cobb-Douglas specification these additional terms would be subsumed in TFP. This can be seen by rewriting (7) as

$$
Y _ {t} = \Lambda_ {t} L _ {t} ^ {a} K _ {t} ^ {b} Z _ {t} ^ {c},\tag{8}
$$

where $\Lambda _ { t }$ is a time dependent function equal to $\Lambda \omega _ { t } ^ { a } u _ { t } ^ { b } v _ { t } ^ { c } ,$ , corresponding to S, or TFP, in (1). Referring back to (6) that represents the growth rate of value added, we can see that growth in TFP is through $\varphi _ { t }$ in (5).

If input proportions of value added are intertemporally constant in our data set and we estimate (8), then we should get a very good fit to the Cobb-Douglas. This is because the income accounting identity directly leads to the Cobb-Douglas form under the condition of constant intertemporal input shares. It also occurs when TFP is time invariant because TFP is a function of time in (8). Consequently, when we estimate the Cobb-Douglas in (1), we are implicitly also estimating (7)—the AI-based Cobb-Douglas with the wage rate and rate of return terms buried in TFP as per (8).

## 3. Estimation of Our AI-Based Cobb-Douglas Form

## 3.1. Data Sources and Calculations

To estimate a form related to the income accounting identity as derived in (7) requires data on input stocks or flows (labor hours, capital stocks, or capital inputs) and more critically on rates of return for the inputs such as the wage rate and rates of return on non-IT capital and on IT capital. The raw data needed for these latter calculations are difficult to obtain, and the calculations are even more difficult to generate (as detailed below). As a basis for our calculations, we use times-series data from 1995 to 2007 for 18 three-digit North American Industry Classification System (NAICS) manufacturing industries (see Table 1), which is the only set of industries for which the data for calculating rates of return were available. The data set spans 21 industries (NAICS 311–316, 321– 327, 331–337, and 339); however, for six industries, the data are provided as aggregates between some pairs of industries, i.e., NAICS 311 and 312 (food and beverage and tobacco products), 313 and 314 (textile mills and textile product mills), and 315 and 316 (apparel and leather and applied products). Even though our data set is limited, it is part of the manufacturing sector, a sector that has better defined and more accurate measures of output than the services sector (Mittal and Nault 2009).

Table 1 NAICS Code 31–33 Manufacturing

<table><tr><td>NAICS code</td><td>Subsector</td><td>Combined subsector</td></tr><tr><td>311</td><td>Food manufacturing</td><td rowspan="2">Food and beverage and tobacco products</td></tr><tr><td>312</td><td>Beverage and tobacco product manufacturing</td></tr><tr><td>313</td><td>Textile mills</td><td rowspan="2">Textile mills and textile product mills $^{1}$ </td></tr><tr><td>314</td><td>Textile product mills</td></tr><tr><td>315</td><td>Apparel manufacturing</td><td rowspan="2">Apparel and leather and applied products $^{1}$ </td></tr><tr><td>316</td><td>Leather and allied product manufacturing</td></tr><tr><td>321</td><td>Wood product manufacturing</td><td></td></tr><tr><td>322</td><td>Paper manufacturing</td><td></td></tr><tr><td>323</td><td>Printing and related support activities</td><td></td></tr><tr><td>324</td><td>Petroleum and coal products manufacturing $^{1}$ </td><td></td></tr><tr><td>325</td><td>Chemical manufacturing</td><td></td></tr><tr><td>326</td><td>Plastics and rubber products manufacturing</td><td></td></tr><tr><td>327</td><td>Nonmetallic mineral product manufacturing</td><td></td></tr><tr><td>331</td><td>Primary metal manufacturing</td><td></td></tr><tr><td>332</td><td>Fabricated metal product manufacturing</td><td></td></tr><tr><td>333</td><td>Machinery manufacturing</td><td></td></tr><tr><td>334</td><td>Computer and electronic product manufacturing $^{1}$ </td><td></td></tr><tr><td>335</td><td>Electrical equipment, appliance, and component manufacturing</td><td></td></tr><tr><td>336</td><td>Transportation equipment manufacturing</td><td></td></tr><tr><td>337</td><td>Furniture and related product manufacturing</td><td></td></tr><tr><td>339</td><td>Miscellaneous manufacturing</td><td></td></tr></table>

Note. There are no economic subsectors 310, 317–320, 328–330, and 338.  
<sup>1</sup>These industries are not included in the final data set.

Our data are taken from the Bureau of Labor Statistics (BLS) website on Multifactor Productivity Data for Major Sectors and Manufacturing and consist of three files:

Capital in manufacturing: these tables contain figures on real capital input, capital income, productive capital stock, capital composition, price deflators, wealth stock, and depreciation. Capital is divided in equipment, structures, rental residential capital, inventories, and land.

IT capital in manufacturing: these tables contain figures on IT capital input, IT capital rental prices, IT capital income, productive IT capital stock, gross investment in IT capital, price deflators, wealth stock, and depreciation. IT capital is divided into computers, software, communication, and other.

Inputs and output in manufacturing: these tables contain figures on real sector output, input quantities and multifactor productivity, output and input prices, value of production and factor costs, and factor shares. Input factors are divided in labor and capital (primary inputs) and energy, materials, and purchased services (secondary inputs).

We obtained labor hours from an unpublished BLS file sent to us on request. It contains the labor hours for 1995 to 2007 for all NAICS industries listed above. The hours of all persons is divided into hours of all employees and hours of all proprietors. The nominal wage rate is calculated by dividing the cost of labor by labor hours. We use the labor hours for all persons—instead of just labor hours of all employees—because both cost of labor and payments to capital include income that is attributed to proprietors. Thus, just using the hours by all employees would overestimate the wage rate. The real wage rate is calculated by using the deflated cost of labor.

For the calculation of real value added, we use the double deflation technique. Hence, we deflate (per industry) gross output as well as all intermediate or secondary inputs (energy, materials, and purchased services) and subtract the values for deflated secondary inputs from the deflated value of the industry output. The resulting real value added is the value of output in constant year 2000 dollars that is due to the usage of the primary or value-added inputs, together with capital and labor, in the production process. One can also think both of real value added and the real values of primary inputs as quantities because price movements are eliminated through deflation.

We use the figures for productive capital stock and productive IT capital stock as a measure for capital. The BLS determines both figures as direct aggregates in constant year 2000 dollars. Productive capital stock for equipment and structures is estimated using the perpetual inventory method. Productive capital stock for inventories and land is based on Bureau of Economic Analysis estimates for inventories and Economic Research Service/U.S. Department of Agriculture land data, respectively. Productive non-IT capital stock is determined by subtracting productive IT capital stock from productive capital stock.

There is a general problem of additivity in the data: the Tornqvist index constructs time series as chained indices and as such has some nice features compared to the previous (before 1996) fixed weight method. However, it comes at the costs that additivity of the components is lost. That is, the deflated figures for input consumption do not necessarily add up to the overall output. This seems to be especially severe if the relative price changes are substantial as can be observed with respect to IT (Whelan 2000). This problem of additivity becomes apparent when calculating real value added on one hand as the sum of the deflated wage bill and real payments to capital and on the other hand as deflated output less deflated intermediate inputs (energy, material, and purchased services).

To minimize the distortions in the data from the additivity problem, the problem of imprecise deflators, or other data problems we do the following. First, we drop some industries from our sample because of negative real value added in many years (NAICS 334) or because of large deviations from the income accounting identity in real terms in many years (NAICS 313/314, 315/316, and 324). Next, we use two data subsets, 1995–2000 and 2000–2007, on the basis that the Internet became a significant economic factor between 1994 and 1995. Moreover, the farther away from the base year (2000), the higher the distortions, and there may be special Y2K effects in the data. We note that the additivity problem may not only be present in the input and output data but also in the productive capital stock data. However, because we have no way to check the productive capital stock data for consistency as we have when using the double deflation technique, we are forced to take them as they are, recognizing that there may be potential for slight error because we determine productive non-IT capital stock as productive capital stock less productive IT capital stock.

Using industry-level data requires some assumptions about industry production technology. The following assumptions were made by the BLS to derive the data (Strassner et al. 2005). First, an industry frontier production function was used that includes the value-added inputs of capital and labor and the intermediate inputs of energy, materials, and purchased services. Next, the industry production function is taken to be weakly separable in value-added inputs, energy inputs, materials inputs, and purchased services inputs, which implies that the marginal rates of technical substitution for an input group are independent of the quantities of other input groups (see also Nataf 1948 and Leontief 1947a, b). Finally, the industry production function was taken to be linearly homogeneous, which implies constant returns to scale and that industries are cost minimizers as they consume inputs. Consequently, the derivation process at BLS is consistent with our use of the Cobb-Douglas.

3.1.1. Important Calculations. For our estimation of the AI-based Cobb-Douglas in (7), we need the following variables: (i) Real Value Added, $Y _ { t } ,$ which is gross output less costs of materials, energy, and purchased services; (ii) (Average) Real Productive Capital Stock, $C _ { t } ;$ (iii) (Average) Real Productive IT Capital Stock, $Z _ { t } ;$ (iv) (Average) Real Productive Non-IT Capital Stock, $K _ { t } ,$ which is Real Productive Capital Stock less $Z _ { t } ;$ (v) Labor Hours, $L _ { t } ;$ (vi) Real Wage Rate, $\omega _ { t } ,$ which is the labor cost divided by labor hours; (vii) Real Return on Capital, $r _ { t } ;$ (viii) Real Return on IT Capital, $v _ { t } ;$ and (ix) Real Return on Non-IT Capital, $\boldsymbol { u } _ { t } .$

For capital stock data, we use the annual average ((year beginning + year end)/2) because capital income and payments to capital are flows, whereas the capital stocks are year-end figures. A challenge is the determination of the return figures. To determine accurate return figures, we need Real Payments to Capital, Real Payments to IT Capital, and Real Payments to Non-IT Capital. Unfortunately, only Nominal Capital Income and Nominal IT Capital Income are available from the BLS. To make the income accounting identity hold in nominal terms, Nominal Capital Income is adjusted ex post by BLS and then called Nominal Payments to Capital. This adjustment is not made to Nominal IT Capital Income, and therefore we must distribute this adjustment between Nominal IT Capital Income and Nominal Non-IT Capital Income. First we calculate the adjustment

Nominal Adjustment

= Nominal Value Added−Nominal Cost of Labor

−Nominal Capital Income1

Nominal Payments to Capital

= Nominal Capital Income+Nominal Adjustment1

Nominal Relative Adjustment

= 4Nominal Payments to Capital

−Nominal Capital Income5/Nominal Capital Income0

Based on a recommendation by BLS, we distribute this adjustment to Nominal IT Capital Income and Nominal Non-IT Capital Income proportionally applying the above Nominal Relative Adjustment multiplier to both Nominal IT Capital Income and Nominal Non-IT Capital Income

Nominal Non-IT Capital Income

= Nominal Capital Income − Nominal IT Capital Income

Nominal Payments to IT Capital

= 4Nominal Relative Adjustment + 15

∗ Nominal IT Capital Income

Nominal Payments to Non-IT Capital

= 4Nominal Relative Adjustment + 15

∗ Nominal Non-IT Capital Income0

The determination of the return figures in real dollars is more involved. For the income accounting identity to hold, which we term as “balanced,” the following must be true in real dollars:

Balanced Real Return on Capital

= 4Real Value Added − Real Cost of Labor5

/Real Productive Capital Stock0

The BLS provides each of the right-hand side variables in nominal figures and their deflators. The BLS also provides Nominal Payments to Capital and its deflator. Because of the double deflation technique and the additivity problems with chained indices, Real Value Added less the Real Cost of Labor is slightly different from Real Payments to Capital. To calculate balanced real return on IT capital and on non-IT capital, we must distribute the difference (Real Value Added − Real Cost of Labor) − Real Payments to Capital between the two types of capital. To begin, we require an unbalanced Real Return on IT Capital using Nominal Payments to IT Capital provided by the BLS and Real IT Productive Capital Stock, inflated to nominal by the deflator because the BLS does not provide Nominal Productive IT Capital Stock directly

Real Return on IT Capital

= Nominal Payments to IT Capital

/Nominal Productive IT Capital Stock

Next, we use Real Return on IT Capital to compute unbalanced real payments to IT capital and to non-IT capital as follows:

Real Payments to IT Capital

= Real Return on IT Capital

∗ Real Productive IT Capital Stock1

Real Payments to Non-IT Capital

= Real Payments to Capital

− Real Payments to IT Capital0

To make the income accounting identity balance in real dollars, we determine the missing payments to capital in this case; that is

Real Payments to Capital Adjustment

= Real Value Added − Real Cost of Labor

− Real Payments to Capital

This Real Payments to Capital Adjustment now has to be allocated to the two types of capital payments. We use the proportions of the Real Productive Capital Stocks in order to make this allocation; that is

Real Payments to IT Capital Adjustment

= Real Payments to Capital Adjustment

∗ 4Real Productive IT Capital Stock

/Real Productive Capital Stock51

Real Payments to Non-IT Capital Adjustment

= Real Payments to Capital Adjustment

∗ 4Real Productive Non-IT Capital Stock

/Real Productive Capital Stock51

Balanced Real Payments to IT Capital

= Real Payments to IT Capital

\+ Real Payments to IT Capital Adjustment1

Balanced Real Payments to Non-IT Capital

= Real Payments to Non-IT Capital

\+ Real Payments to Non-IT Capital Adjustment0

With these balanced figures, we can now determine the return figures needed for our estimation

Balanced Real Return on IT Capital

= Balanced Real Payments to IT Capital

/Real Productive IT Capital Stock1

Balanced Real Return on Non-IT Capital

= Balanced Real Payments to Non-IT Capital

/Real Productive Non-IT Capital Stock0

These final balanced real returns are what we use for Real Return on IT Capital, $v _ { t } ;$ Real Return on Non-IT Capital, $u _ { t } ;$ and our earlier figure for Real Return on Capital, $r _ { t } .$

3.1.2. Derivation When Using Real Capital Input. Some studies suggest using the real capital input instead of productive capital stock as a measure for capital input since it represents a flow measure of assets that are used but not consumed in the production process and, thus, may be a superior measure to stock data (Jorgenson and Griliches 1967, Chwelos et al. 2010). We run our sets of regressions below using the Real Productive Capital Stock and then again using the Real Capital Input. In the following, we describe the necessary changes to the above calculations when using Real Capital Input.

The BLS determines Real Capital Input and Real IT Capital Input by adapting the Productive Capital Stock and Productive IT Capital Stock data using its standard methodology. The figures are not reported directly in the files provided by BLS, but just the capital composition is (ratio of Capital Input to Productive Stock). Hence, we use the productive capital stock data that are provided as direct aggregates in constant year 2000 dollars and infer the real capital input figures using the provided capital composition figures. We note that the additivity problem described earlier may also be present in real capital input data. However, as with productive capital stock data, because we have no way to check the capital input data for consistency as we can when using the double deflation technique, we are forced to take them as they are, recognizing that there may be potential for slight error because we determine Real Non-IT Capital Input as Real Capital Input less Real IT Capital Input.

3.1.3. Important Calculations Using Real Capital Input. When using Real Capital Inputs, there are redefinitions of the Productive Capital Stock-based measures we described earlier. For our estimation of (7) we need (i) Real Value Added as before, $Y _ { t } ; ( \mathrm { i i } )$ Real Capital Input (instead of Average Productive Capital Stock), $C _ { t } ; ( \mathrm { i i i } )$ Real IT Capital Input (instead of Average Productive IT Capital Stock), $Z _ { t } ; ( \mathrm { i v } )$ Real Non-IT Capital Input (instead of Average Productive Non-IT Capital Stock), $K _ { t } ,$ which is Real Capital Input less $Z _ { t } ; ~ ( \mathrm { v } )$ Labor Hours as before, $L _ { t } ;$ (vi) Real Wage Rate, as before, $\omega _ { t } ;$ (vii) Real Return on Capital Input (instead of Return on Capital), $r _ { t } ;$ (viii) Real Return on IT Capital Input (instead of Return on IT Capital), $v _ { t } ;$ and (ix) Real Return on Non-IT Capital (instead of Return on Non-IT Capital), $u _ { t }$

When using Real Capital Inputs, the calculations are analogous to the ones when using Real Productive Capital Stock. The main difference is that we do not need to calculate an average stock figure using two subsequent year-end figures since capital input is already a flow measure that corresponds to the services provided by the capital stock in one year. To keep our calculations consistent in order to make the income accounting identity hold, we use the proportions of the Real Capital Input, i.e., Real IT Capital Input versus Real Non-IT Capital Input, instead of the proportions of capital stocks to distribute the missing payments to capital. Finally, for inflating the Real $\check { I T }$ Capital Input to nominal, we use the investment deflator—the same one already referred to above—because the BLS does not provide Nominal IT Capital Input directly.

## 3.2. Estimation Forms and Econometric Adjustments

3.2.1. Estimation Forms. In our analysis we estimate both the Cobb-Douglas and AI-based Cobb-Douglas. The Cobb-Douglas estimation form of (1) is

$$
y _ {t} = s + \alpha l _ {t} + \beta k _ {t} + \gamma z _ {t} + \epsilon_ {t} ^ {c d},\tag{9}
$$

where the lowercase variables represent natural logs of the uppercase variables. The log of TFP is denoted by $s ,$ and $\epsilon _ { t } ^ { c d }$ is a random disturbance. The AI-based Cobb-Douglas estimation form of (7) is

$$
\begin{array}{r} y _ {t} = \lambda + a _ {1} \ln (\omega_ {t}) + b _ {1} \ln (u _ {t}) + c _ {1} \ln (v _ {t}) \\ + a _ {2} l _ {t} + b _ {2} k _ {t} + c _ {2} z _ {t} + \epsilon_ {t} ^ {a i}, \end{array}\tag{10}
$$

where the lowercase variables are as above, and $\epsilon _ { t } ^ { a i }$ is a random disturbance. The parameter  is what remains of TFP after removing the effects of rates of return from the income accounting identity.

From (7) we expect that the coefficients of the (logged) inputs—the output elasticities—are equal to the coefficients of their (logged) rates of return: $a _ { 1 } =$ $a _ { 2 } , b _ { 1 } = b _ { 2 } .$ , and $c _ { 1 } = c _ { 2 }$ . These in turn should approximate the input shares. If we cannot reject the null hypotheses on the equivalence of these coefficients, this indicates—complementing the theoretical derivation shown above—empirical support for using the Cobb-Douglas in IT productivity work.

The additional terms for rates of return, $a _ { 1 } , \ b _ { 1 } ,$ and $c _ { 1 } ,$ are somewhat difficult to understand because they play two roles. One is that they provide some explanatory power about the effects that are contained in the Cobb-Douglas TFP. This explanatory power is different from actually measuring an effect like organizational capital or spillovers—we simply claim that the explanatory power is likely to contain effects in TFP found in other studies such as organizational capital and spillovers. The second role comes from the underlying accounting identity, whereby the coefficients are input shares and should be the same as the output elasticities (which can also be interpreted as input shares) from the Cobb-Douglas portion of the AI-based CD. This is what allows us to understand the theoretical and empirical correspondence between the two forms.

3.2.2. Econometric Adjustments. Our 14 threedigit NAICS industries differ in what they produce and in size and are subjected to common economy level shocks. In addition, BLS applies smoothing procedures to the data. Therefore, we expect that autocorrelation is present in the data set and that the degree of autocorrelation differs between industries. Using the Wooldridge test for autocorrelation in panel data, we found that AR1 is present in each of our data sets and that the range of autocorrelation coefficients varied substantially between industries. Consequently, we use panel-specific AR1 in our estimations, which in effect acts as an industry-level control. The presence of AR1 invalidates the use of iterated Generalized Least Squares to get the maximum likelihood estimates, and the standard tests of heteroskedasticity such as the likelihood ratio test are not possible (Greene 2003, §5.2.3). Nonetheless, because we expect heteroskedasticity, we also control for it at the industry level.

In our use of panel-specific AR1 we implicitly assume that industry-level effects that are generated by omitted variables that differ between industries can be captured by industry-specific autocorrelation functions. However, these omitted variables may not follow industry-specific autocorrelation functions over time. Rather, there may be omitted variables that are constant over time and differ between industries and others that are constant over industries but change over time. Therefore, we also generate estimates using industry random effects with common AR1.

Finally, we expect year-to-year differences due to changes in overall economic conditions and monetary and fiscal policy. In all of our estimations we also control for time fixed effects, although this has little impact on the qualitative meaning of our results.

## 4. Results

## 4.1. Results from the Cobb-Douglas

We begin the discussion of our results by comparing our Cobb-Douglas estimates with those from a sample of prior IT productivity studies to confirm that our data set is not unusual. The results from prior IT productivity studies are provided in Table 2. The classic paper by Brynjolfsson and Hitt (1996) bundles intermediate inputs (expenses) with labor, which causes their estimates to be weighted toward labor. In the other studies the output elasticity of IT capital ranges from 0.051 to 0.122, although we recognize that different studies have included different assets in their measures of IT capital. The output elasticity of non-IT capital is less than half that of labor.

Our estimates of output elasticities from the Cobb-Douglas form in (9) are contained in Tables 3 and 4, which correspond to our different econometric adjustments: heteroskedasticity, industry-specific autocorrelation (Table 3) versus industry random effects and common autocorrelation (Table 4). For the results in both tables we also control for time fixed effects. In each table we provide results using a stock measure of capital and a flow measure of capital: average real productive capital stock and real capital input, respectively. In addition, we provide results over our complete period 1995–2007, and for two subperiods centered on 2000, 1995–2000, and 2000–2007, noting that 2000 is the base year. We also have results for 2001–2007 (available from the authors), and they are almost identical to the 2000–2007 subperiod.

Examining the odd-numbered (CD) rows in Table 3, we find roughly a 65-35 split between labor and capital across our measures of capital and across our different time periods. All but one of the elasticities are significant at $p < 0 . 0 1$ . The output elasticity of labor is relatively consistent at between 0.606 and 0.673 across the six Cobb-Douglas regressions. The output elasticity of IT capital is substantially higher than in prior studies and is twice as large in the 2000–2007 period as in the 1995–2000 period. In contrast, the output elasticity of non-IT capital is smaller than in most of the prior studies and is not significantly different from zero in the 2000–2007 period. The results are fairly consistent across our two different measures of capital, suggesting that whether we measure capital as a stock or as a flow is not critical to the results. The sum of the output elasticities in the Cobb-Douglas results are all within about 3% of 1.0, which suggests constant returns to scale.

Examining the odd-numbered (CD) rows in Table 4 across our six regressions, 13 of 18 output elasticities are significant at $p < 0 . 0 1$ and one at $p < 0 . 0 5 .$ Although significant in the overall period, the output elasticity of non-IT capital in both subperiods is insignificant using both our stock and flow measures of capital. The output elasticity estimates for labor and IT capital are significant in all of the regressions; as compared to the results in Table 3, the output elasticities of labor are more variable and of IT capital are less variable. Again, the output elasticities of IT capital are almost twice as large in the latter subperiod and substantially larger than those from prior studies. As with the results in Table 3, whether we measure capital as a stock or as a flow is not critical, and the sum of the output elasticities (0.978 to 1.043) in the Cobb-Douglas results suggest constant returns to scale.

Table 2 Output Elasticity Estimates from Selected Past Studies

<table><tr><td rowspan="2">Description</td><td rowspan="2">Data level</td><td rowspan="2">Production function</td><td colspan="4">Elasticity estimates of</td><td rowspan="2">Sum of O.E.</td></tr><tr><td>Labor</td><td>Non-IT capital</td><td>IT labor</td><td>IT capital</td></tr><tr><td>Lichtenberg (1995) Computerworld</td><td>Firm</td><td>Cobb-Douglas</td><td>0.507</td><td>0.333</td><td>—</td><td>0.10</td><td>0.94</td></tr><tr><td>Lichtenberg (1995) Info-week</td><td>Firm</td><td>Cobb-Douglas</td><td>0.489</td><td>0.390</td><td>—</td><td>0.122</td><td>1.001</td></tr><tr><td>Brynjolfsson and Hitt (1995)</td><td>Firm</td><td>Cobb-Douglas</td><td>0.472</td><td>0.242</td><td>—</td><td>0.0522</td><td>0.77</td></tr><tr><td>Brynjolfsson and Hitt (1996)</td><td>Firm</td><td>Cobb-Douglas</td><td>0.883</td><td>0.0608</td><td>0.0178</td><td>0.0169</td><td>0.98</td></tr><tr><td>Dewan and Min (1997)</td><td>Firm</td><td>CES-Translog</td><td>0.601</td><td>0.281</td><td>—</td><td>0.104</td><td>0.99</td></tr><tr><td>Dewan and Kraemer (2000) developed countries</td><td>Country</td><td>Cobb-Douglas</td><td>0.955</td><td>0.176</td><td>—</td><td>0.051</td><td>1.18</td></tr><tr><td>Mittal and Nault (2009)</td><td>Industry</td><td>Cobb-Douglas</td><td>0.700</td><td>0.250</td><td>—</td><td>0.120</td><td>1.07</td></tr></table>

Table 3 Estimation Results: Controls for Heteroskedastic Errors, Industry-Specific AR1, and Time Fixed Effects

<table><tr><td rowspan="2" colspan="2"></td><td colspan="7">Elasticity/ coefficient estimates for</td></tr><tr><td>Labor hours /</td><td>Wage rate  $\ln(\omega)$ </td><td>Non-IT capital k</td><td>Return Non-IT capital  $\ln(u)$ </td><td>IT capital z</td><td>Return IT capital  $\ln(v)$ </td><td>Sum of O.E.</td></tr><tr><td colspan="9">Capital as average real productive capital stock</td></tr><tr><td>1995–2007</td><td>1. CD</td><td>0.668**</td><td>—</td><td>0.143**</td><td>—</td><td>0.217**</td><td>—</td><td>1.028</td></tr><tr><td>Obs: 182</td><td>2. AI</td><td>0.724**</td><td>0.734**</td><td>0.283**</td><td>0.220**</td><td>0.025</td><td>0.099**</td><td></td></tr><tr><td>1995–2000</td><td>3. CD</td><td>0.657**</td><td>—</td><td>0.224**</td><td>—</td><td>0.134**</td><td>—</td><td>1.015</td></tr><tr><td>Obs: 84</td><td>4. AI</td><td>0.724**</td><td>0.603**</td><td>0.233**</td><td>0.203**</td><td>0.067**</td><td>0.093**</td><td></td></tr><tr><td>2000–2007</td><td>5. CD</td><td>0.606**</td><td>—</td><td>0.082</td><td>—</td><td>0.282**</td><td>—</td><td>0.970</td></tr><tr><td>Obs: 112</td><td>6. AI</td><td>0.644**</td><td>0.725**</td><td>0.282**</td><td>0.281**</td><td>0.058**</td><td>0.081**</td><td></td></tr><tr><td colspan="9">Capital as real capital input</td></tr><tr><td>1995–2007</td><td>7. CD</td><td>0.666**</td><td>—</td><td>0.152**</td><td>—</td><td>0.209**</td><td>—</td><td>1.027</td></tr><tr><td>Obs: 182</td><td>8. AI</td><td>0.732**</td><td>0.739**</td><td>0.285**</td><td>0.218**</td><td>0.020</td><td>0.101**</td><td></td></tr><tr><td>1995–2000</td><td>9. CD</td><td>0.673**</td><td>—</td><td>0.194**</td><td>—</td><td>0.151**</td><td>—</td><td>1.018</td></tr><tr><td>Obs: 84</td><td>10. AI</td><td>0.733**</td><td>0.633**</td><td>0.239**</td><td>0.199**</td><td>0.057**</td><td>0.101**</td><td></td></tr><tr><td>2000–2007</td><td>11. CD</td><td>0.606**</td><td>—</td><td>0.082</td><td>—</td><td>0.281**</td><td>—</td><td>0.969</td></tr><tr><td>Obs: 112</td><td>12. AI</td><td>0.641**</td><td>0.723**</td><td>0.277**</td><td>0.284**</td><td>0.063**</td><td>0.076**</td><td></td></tr></table>

Note. CD is the Cobb-Douglas, AI is the income accounting identity-based Cobb-Douglas.  
<sup>∗∗</sup>Significant at p < 0001.

## 4.2. Results from Our AI-Based Cobb-Douglas

Our estimates of output elasticities and logged rate of return coefficients from the AI-based Cobb-Douglas form in (10) are in the even-numbered (AI) rows of Tables 3 and 4. As with the Cobb-Douglas we described above, we provide results for two different measures of capital—a stock and a flow, and for three different time periods—1995–2007 and two subperiods.

To begin, because the Cobb-Douglas in (9) is nested in the AI-based Cobb-Douglas in (10), we ran Wald tests with the null hypothesis that $a _ { 1 } , b _ { 1 } , c _ { 1 } = 0$ . This hypothesis tests whether the additional input rate of return terms in the AI-based Cobb-Douglas adds significant explanatory power. In all 12 cases (two sets of econometric controls, two measures of capital, three time periods) the hypothesis is rejected at all significance levels $( p < 0 . { \dot { 0 } } { \dot { 0 } } 0 1 )$ so that in each case the additional terms add significant explanatory power. Because these three terms make up the elements of TFP that are measured in (10) as compared to the Cobb-Douglas in (9), the Wald tests indicate that our AI-based Cobb-Douglas is explaining a significant portion of TFP.

Table 4 Estimation Results: Controls for Industry Random Effects, AR1, and Time Fixed Effects

<table><tr><td rowspan="2" colspan="2"></td><td colspan="7">Elasticity/coefficient estimates for</td></tr><tr><td>Labor hours /</td><td>Wage rate  $\ln(\omega)$ </td><td>Non-IT capital k</td><td>Return Non-IT capital  $\ln(u)$ </td><td>IT capital z</td><td>Return IT capital  $\ln(v)$ </td><td>Sum of O.E.</td></tr><tr><td colspan="9">Capital as average real productive capital stock</td></tr><tr><td>1995–2007</td><td>1. CD</td><td>0.590**</td><td>—</td><td>0.260**</td><td>—</td><td>0.161**</td><td>—</td><td>1.011</td></tr><tr><td>Obs: 182</td><td>2. AI</td><td>0.676**</td><td>0.759**</td><td>0.308**</td><td>0.201**</td><td>0.025</td><td>0.129**</td><td></td></tr><tr><td>1995–2000</td><td>3. CD</td><td>0.678**</td><td>—</td><td>0.137</td><td>—</td><td>0.223**</td><td>—</td><td>1.038</td></tr><tr><td>Obs: 84</td><td>4. AI</td><td>0.681**</td><td>0.512**</td><td>0.223**</td><td>0.182**</td><td>0.105**</td><td>0.105**</td><td></td></tr><tr><td>2000–2007</td><td>5. CD</td><td>0.557**</td><td>—</td><td>0.205</td><td>—</td><td>0.222**</td><td>—</td><td>0.984</td></tr><tr><td>Obs: 112</td><td>6. AI</td><td>0.615**</td><td>0.681**</td><td>0.327**</td><td>0.300**</td><td>0.060*</td><td>0.093**</td><td></td></tr><tr><td colspan="9">Capital as real capital input</td></tr><tr><td>1995–2007</td><td>7. CD</td><td>0.611**</td><td>—</td><td>0.256**</td><td>—</td><td>0.148*</td><td>—</td><td>1.015</td></tr><tr><td>Obs: 182</td><td>8. AI</td><td>0.685**</td><td>0.781**</td><td>0.304**</td><td>0.200**</td><td>0.020</td><td>0.130**</td><td></td></tr><tr><td>1995–2000</td><td>9. CD</td><td>0.694**</td><td>—</td><td>0.126</td><td>—</td><td>0.223**</td><td>—</td><td>1.043</td></tr><tr><td>Obs: 84</td><td>10. AI</td><td>0.687**</td><td>0.534**</td><td>0.232**</td><td>0.181**</td><td>0.098**</td><td>0.110**</td><td></td></tr><tr><td>2000–2007</td><td>11. CD</td><td>0.553**</td><td>—</td><td>0.202</td><td>—</td><td>0.223**</td><td>—</td><td>0.978</td></tr><tr><td>Obs: 112</td><td>12. AI</td><td>0.611**</td><td>0.664**</td><td>0.318**</td><td>0.308**</td><td>0.072**</td><td>0.082**</td><td></td></tr></table>

Note. CD is the Cobb-Douglas, AI is the income accounting identity-based Cobb-Douglas.  
<sup>∗</sup>Significant at p < 0005; <sup>∗∗</sup>significant at p < 0001.

4.2.1. Overall Period Regressions. Next, with the AI-based Cobb-Douglas for the overall period (1995– 2007) in Table 3, we find that the output elasticities of labor and non-IT capital increase at the expense of IT capital as compared to the Cobb-Douglas results and are significant to $p < 0 . 0 1$ . In fact, the output elasticity of IT capital is not significant in either regression— using capital stocks or capital inputs—for the overall period. The coefficients of the logged wage rate and the logged return on non-IT capital are very close to those of the output elasticities of labor and non-IT capital. The coefficient of the logged rate of return to IT capital, 0.099 for IT capital stock regression and 0.101 for IT capital input regression, is close to the output elasticities of IT capital in prior studies. All of the coefficients of the input rate of return terms are significant to $p < 0 . 0 1$ . As we discuss in our robustness section below, one reason that may explain why the IT capital output elasticity is insignificant is that the input shares for IT capital changed more in percentage terms over the 13 years, 1995–2007, than did the shares of the other inputs.

Similarly in the two regressions for the overall period in Table 4 we find significant estimates for the output elasticities of labor and of non-IT capital that are higher than those from the Cobb-Douglas and an insignificant output elasticity for IT capital. The coefficients of the logged wage rate and the logged return on non-IT capital are again close to those of the output elasticities of labor and non-IT capital, although not as close as those in Table 3. The coefficient of the logged rate of return to IT capital, 0.129 for IT capital stock regression and 0.130 for IT capital input regression, is on the upper end of the output elasticities of IT capital in prior studies. All of the coefficients of the input rate of return terms are significant to $p < 0 . 0 1$

4.2.2. Subperiod Regressions. Examining the two subperiods, 1995–2000 and 2000-2007, in Table 3, we find that all of the coefficient estimates are significant to $p < 0 . 0 1$ . More striking is the effect of the inclusion of the rates of return terms on the output elasticities of non-IT and IT capital. Across both measures of capital (capital stock and capital input) and across both subperiods, the output elasticities of non-IT capital and IT capital are much closer to their levels in prior studies. Moreover, their magnitudes are very close to those of their (logged) rate of return coefficients, consistent with the income accounting identity result in (7). In particular, the subperiod regressions show results for IT capital that are consistent with results from prior studies. The output elasticity of IT capital ranges between 0.057 and 0.067 across the four subperiod regressions, and the coefficients of the logged rate of return to IT capital range between 0.076 and 0.101. We believe that these significant and historically consistent results are because the input shares of the inputs are more stable over the shorter subperiods, consistent with the condition required for the derivation of the AI-based Cobb-Douglas form.

We find similar results for the two subperiods in Table 4. All of the six coefficient estimates across the subperiods and the measures of capital are significant to $p < 0 . 0 1$ , and the magnitudes of the output elasticities of the three inputs are close to the magnitudes of the coefficients of their respective logged rates of return. As with the results from the other econometric adjustments, the output elasticities are similar to their levels in prior studies, ranging from 0.060 to 0.105, and the coefficients of the rates of return to IT capital range from 0.082 to 0.110.

In both Tables 3 and 4, the consistency in the estimates of output elasticities and the coefficients of their corresponding logged rates of return demonstrate the empirical regularity of the income accounting identity in its AI-based Cobb-Douglas form.

4.2.3. Tests of Differences in Coefficients. From the income accounting identity form in (7), for each input the coefficient of the logged input (the output elasticity) is equal to the coefficient of the logged rate of return. Examining our AI-based Cobb-Douglas estimation form in (10), there are three null hypotheses: $a _ { 1 } = a _ { 2 }$ for the output elasticity of labor and the logged wage rate, $b _ { 1 } = b _ { 2 }$ for the output elasticity of non-IT capital and its logged rate of return, and $c _ { 1 } = c _ { 2 }$ for the output elasticity of IT capital and its logged rate of return. The results of our Wald tests of differences in coefficients are given in Table 5.

Directly from the table, there is perfect consistency in the significance results across econometric adjustments and across time periods. Overall, 24 of 36 tests show that there is not a significant difference in coefficients, and most of the tests that find significant differences are in the overall period where we would expect input shares to be less stable. More importantly, in the two subperiods, where our AI-based Cobb-Douglas regressions yielded a complete set of significant coefficients, 20 of 24 tests show that there is not a significant difference in coefficients, and if we set $p = 0 . 0 1$ , none of the tests of differences would be significant. In the second subperiod, there is no evidence of difference between output elasticities and coefficients of logged rates of return; in the first subperiod the only significant difference is in the labor-related coefficients. As we discuss later, there may be a skill-level effect over time that has affected the relationship between labor hours and wage rates. Nonetheless, the results in Table 5 provide relatively strong statistical support for the equality of coefficients in (10).

Table 5 P -Values for Test of Difference of Coefficients

<table><tr><td rowspan="3"></td><td colspan="6">Test of difference of coefficients</td></tr><tr><td colspan="3">He + PSAR1</td><td colspan="3">RE + AR1</td></tr><tr><td> $a_1 = a_2$ </td><td> $b_1 = b_2$ </td><td> $c_1 = c_2$ </td><td> $a_1 = a_2$ </td><td> $b_1 = b_2$ </td><td> $c_1 = c_2$ </td></tr><tr><td colspan="7">Capital as average real productive capital stock</td></tr><tr><td>1995–2007</td><td>N.S.</td><td>0.001</td><td>0.002</td><td>N.S.</td><td>0.001</td><td>0.003</td></tr><tr><td>1995–2000</td><td>0.012</td><td>N.S.</td><td>N.S.</td><td>0.019</td><td>N.S.</td><td>N.S.</td></tr><tr><td>2000–2007</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td></tr><tr><td colspan="7">Capital as real capital input</td></tr><tr><td>1995–2007</td><td>N.S.</td><td>0.002</td><td>0.003</td><td>N.S.</td><td>0.002</td><td>0.004</td></tr><tr><td>1995–2000</td><td>0.044</td><td>N.S.</td><td>N.S.</td><td>0.045</td><td>N.S.</td><td>N.S.</td></tr><tr><td>2000–2007</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td><td>N.S.</td></tr></table>

Notes. He + PSAR1: Controls for heteroskedastic errors, industry-specific AR1, and time fixed effects. ${ \mathsf { R E } } + { \mathsf { A R 1 : } }$ Controls for industry random effects, AR1, and time fixed effects. $\mathsf { N } . \mathsf { S } . = \mathsf { n o t }$ significant at $p \ge 0 . 0 5 .$

## 4.3. Robustness

4.3.1. Intertemporal Consistency of Input Shares. In our derivation of the mathematical form in (7) from the income accounting identity, we supposed that the input shares were intertemporally constant. Indeed, this is the only substantive assumption needed to derive the AI-based Cobb-Douglas form. To examine this we ran fixed effects (to capture industry heterogeneity) regressions of year on the input share for each input and for our overall and subperiods. All nine fixed effects regressions had significant effects of year $( p < 0 . 0 1 )$ on input share. However, the estimates of changes in share were relatively small: for IT capital the annual changes were no greater than 0.5%, for non-IT capital the annual changes were no greater than 2%, and for labor the annual changes were no greater than 2.5%. Nonetheless, taken over several years these annual changes in input shares are considerable.

To determine the cumulative effects of input share changes, we examined the annual growth rates of the inputs and the resulting changes in the input share of each for the overall periods and each of the subperiods, by industry and averaged over the industries in our data set in Table 6. For the overall period, the change in input share of labor was roughly a 35% decrease, for non-IT capital a 100% increase, and for IT capital a 210% increase. The changes were correspondingly lower for the two subperiods: for labor the change was a 10%–30% decrease; for non-IT capital, a 33%–63% increase; and for IT capital, an 85%– 86% increase.

The constancy in our results, in particular the regularity between coefficients on the logged rate of return to an input and that input’s output elasticity, is suggestive that changes in input share of the magnitude found in our data may not be sufficiently substantial to invalidate the process of going from the income accounting identity to the AI-based Cobb-Douglas form. Indeed, given the magnitude of the changes reported above, it may be taken as evidence that the AI-based Cobb-Douglas form is reasonably robust to substantial changes in input share. However, there may be a limit—in the overall period we found that the output elasticity of IT capital was not significant, and this corresponds to a period over which the input share of IT capital more than tripled.

4.3.2. Endogeneity, Errors in Variables, Omitted Variables, and Historical Data. We ran endogeneity tests across each of our overall periods and two subperiods for each of the inputs in our Cobb-Douglas form and for each of the inputs and the two logged rates of return to capital in our AI-based Cobb-Douglas form using a Generalized Method of Moments model with lagged variables as instruments (hence, without AR1 but with industry-level controls) to generate Hansen J statistics and the C (difference in Sargan) statistic. Although using lagged variables as instruments is common in the literature when alternative instruments are unavailable, it is not ideal because unobservables that can affect inputs and outputs are likely to persist over time, which we recognize can weaken the tests.

In the Cobb-Douglas form we found evidence that labor hours was endogenous in both the overall period and the later subperiod across both definitions of capital (capital stock and capital input) and that IT capital stock was mildly endogenous $\left( { p < 0 . 0 3 6 } \right)$ in the later subperiod. Given the Wald tests indicating that the additional terms in the AI-based Cobb-Douglas were significant—terms that are part of TFP, finding some level of endogeneity in the Cobb-Douglas form is not surprising. More importantly, we found no evidence of endogeneity in the AI-based Cobb-Douglas regressions even with a large number of tests: five variables, three time periods, and two definitions of capital provided 30 separate tests and none were significant at $p < 0 . 0 5$ . We were unable to perform the endogeneity test on the logged wage rate because the estimated covariance matrix of moment condition was not of full rank, and GMM estimation failed. We believe this is because the wage rate across time after adjusting for inflation shows a much smaller variance than the remaining variables.

Table 6 Annual Growth Rates in Input Factor Shares

<table><tr><td rowspan="3">Industry</td><td colspan="9">Annual growth rates in input factor share of1</td></tr><tr><td colspan="3">Labor (%)</td><td colspan="3">Non-IT capital (%)</td><td colspan="3">IT capital (%)</td></tr><tr><td>1995–2007</td><td>1995–2000</td><td>2000–2007</td><td>1995–2007</td><td>1995–2000</td><td>2000–2007</td><td>1995–2007</td><td>1995–2000</td><td>2000–2007</td></tr><tr><td>311, 312</td><td>-1.5</td><td>-0.5</td><td>-2.3</td><td>-0.9</td><td>-4.7</td><td>1.9</td><td>5.4</td><td>6.2</td><td>4.8</td></tr><tr><td>321</td><td>-2.4</td><td>-1.1</td><td>-3.4</td><td>5.0</td><td>2.8</td><td>6.6</td><td>8.5</td><td>9.2</td><td>8.0</td></tr><tr><td>322</td><td>-3.0</td><td>-1.6</td><td>-4.0</td><td>4.0</td><td>2.8</td><td>5.0</td><td>4.7</td><td>4.8</td><td>4.6</td></tr><tr><td>323</td><td>-2.9</td><td>-1.6</td><td>-3.8</td><td>8.0</td><td>6.4</td><td>9.1</td><td>11.8</td><td>15.3</td><td>9.4</td></tr><tr><td>325</td><td>-5.4</td><td>-2.9</td><td>-7.1</td><td>3.1</td><td>2.0</td><td>3.9</td><td>7.4</td><td>7.9</td><td>7.0</td></tr><tr><td>326</td><td>-2.7</td><td>-4.5</td><td>-1.4</td><td>5.7</td><td>11.4</td><td>1.9</td><td>8.0</td><td>13.7</td><td>4.1</td></tr><tr><td>327</td><td>-2.3</td><td>-2.2</td><td>-2.3</td><td>2.6</td><td>3.2</td><td>2.2</td><td>9.4</td><td>11.7</td><td>7.8</td></tr><tr><td>331</td><td>-3.9</td><td>-1.6</td><td>-5.4</td><td>7.3</td><td>5.7</td><td>8.6</td><td>9.0</td><td>0.1</td><td>15.8</td></tr><tr><td>332</td><td>-2.1</td><td>-0.9</td><td>-3.0</td><td>3.2</td><td>1.2</td><td>4.6</td><td>9.6</td><td>11.7</td><td>8.1</td></tr><tr><td>333</td><td>-3.4</td><td>-1.6</td><td>-4.7</td><td>6.6</td><td>1.5</td><td>10.3</td><td>12.5</td><td>18.4</td><td>8.4</td></tr><tr><td>335</td><td>-3.1</td><td>0.3</td><td>-5.4</td><td>3.0</td><td>-1.0</td><td>5.9</td><td>5.8</td><td>3.5</td><td>7.6</td></tr><tr><td>336</td><td>-5.1</td><td>-2.6</td><td>-6.9</td><td>11.1</td><td>9.0</td><td>12.7</td><td>11.3</td><td>18.6</td><td>6.4</td></tr><tr><td>337</td><td>-3.1</td><td>-1.7</td><td>-4.0</td><td>8.3</td><td>7.3</td><td>9.1</td><td>14.7</td><td>18.2</td><td>12.2</td></tr><tr><td>339</td><td>-3.7</td><td>-4.0</td><td>-3.5</td><td>12.3</td><td>21.2</td><td>6.4</td><td>10.6</td><td>13.6</td><td>8.4</td></tr><tr><td>Average2</td><td>-3.2</td><td>-1.9</td><td>-4.1</td><td>5.7</td><td>4.9</td><td>6.3</td><td>9.2</td><td>10.9</td><td>8.0</td></tr><tr><td>Overall input share change3</td><td>65.6</td><td>89.1</td><td>71.6</td><td>205.1</td><td>133.4</td><td>163.0</td><td>313.5</td><td>186.4</td><td>185.6</td></tr></table>

<sup>1</sup>The annual growth rates are calculated as compound annual growth (CAGR) rate using the first and the last year in the respective period.  
<sup>2</sup>The average is calculated as the arithmetic mean over all industries (without weighing of the industries).  
<sup>3</sup>The overall input share change is calculated using the following formula: (1+ average)<sup>#years</sup> <sup>in</sup> <sup>period</sup>.

As with all productivity data, and perhaps even more so with industry-level data, there can be errors in variables due to measurement. In our case it is reasonable that such errors are not correlated with any particular variable (the classical errors in variable problem) because they arise from different sampling and estimation procedures used by the government agencies that collect the data we use. Measurement error in the dependent variable, in our case value added, typically increases the variance of the estimates, making them less efficient, but there is no bias (see Levi 1973 and later work). Measurement error in our independent variables—labor, non-IT capital, IT capital, and their corresponding rates of return—are likely to cause attenuation bias whereby estimates are likely to be biased toward zero. Together, these two types of measurement errors make it less likely that we would find significant results, which strengthens our confidence in the significant results we found.

Because our Cobb-Douglas and AI-based Cobb-Douglas form are theoretically based, we do not suffer from a functional form misspecification problem that is a common concern with omitted variables. Indeed, this is the strength of theoretically derived estimation forms. In our setting, the remaining concern is industry-specific effects, and we described the different ways we account for those effects in §3.2.2.

In terms of historical data, there are data sources of the measures we use as far back as 1987. However, we found the older data to be problematic for several reasons and chose to begin our analysis with 1995.

First, with the Internet era beginning in roughly 1995, the input shares of IT capital changed considerably as the economy and methods of production changed. In addition, there is a substantial problem with chain aggregates. First, the use of chain aggregates began in 1996 for most of the measures we employed to generate our data—this is when the U.S. Department of Commerce began using the new method to construct all aggregate “real” series in the National Income and Product Accounts. Second, if relative prices are changing, then those products that decline in relative price have a smaller impact on a chain aggregate growth after the base year and a larger impact prior to the base year. Given the decrease in relative prices for IT in recent decades, chain index aggregates grow more slowly after the base year (2000 in our data sources) and faster before the base year relative to fixed weight index aggregates (see Whelan 2002, p. 223). This means that the further the data is from the base year, especially before the base year, the more distortion is introduced. This has a strong impact on our analysis because it means there are greater distortions in our IT capital measures, and because chain aggregates are the source of the additivity problem converting from the nominal to the real income accounting identity, as described in §3.1. This was a main reason for our choice of centering our subperiods on the base period, yielding six years in the early subperiod and eight years in the later subperiod. It is also possible that the recoding of industries to NAICS around 2000, and then reclassifying earlier years from Standard Industrial Classification coding, introduced additional distortion in the data for years increasingly earlier than 2000.

## 5. Conclusion

Our results can be summarized as follows. First, the Cobb-Douglas form used for estimation in much of the IT productivity research can be recovered directly from the income accounting identity, and the additional terms in the income accounting identity can identify additional information embedded in TFP. Second, using a very specific data set spanning 13 years and 14 industries that has the additional measures we need to estimate our theoretically based estimation form, our estimations and the resulting Wald tests show significant additional explanatory power of the AI-based Cobb-Douglas over the Cobb-Douglas. Third, the consistency in the estimates of output elasticities and the coefficients of logged rates of return for our two subperiods and the tests of the equality of coefficients in our AI-based Cobb-Douglas form demonstrate the empirical regularity of the income accounting identity-derived estimation form. This further provides evidence for the AI-based Cobb-Douglas as an empirically supported theoretical justification for using the Cobb-Douglas form.

Using the income accounting identity, its analytical equivalence to the AI-based Cobb-Douglas form, and the nesting of the Cobb-Douglas form within the AI-based form as a unifying concept, this research makes two important and previously unrecognized contributions.

The first is to provide a rigorous and more general theoretical model to justify the measurement of returns to IT through the Cobb-Douglas, a theoretical model that we validate empirically. It is more rigorous because it is derived from an identity. It is more general because it does not require the behavioral assumptions that underlie production theory, and only requires a mild assumption that input shares are relatively constant in the measurement period. Moreover, because the identity holds at all levels of analysis from the establishment level up to the economy level, our derivation and test applies to all levels of aggregation. These findings are important because they allow us to better understand why the fit between output and inputs has been so strong in prior returns to IT research while validating the source of the measured output elasticities—effectively, the direct returns to IT measured in that work. In addition, our findings provide support for consistent and compelling insights obtained from past productivity research using the Cobb-Douglas form and more importantly provide a theoretical basis for future work such that the Cobb-Douglas form can be confidently used to estimate returns to IT at varying levels of analysis if input shares are reasonably stable over time.

The second is to our understanding and measurement of TFP. Our analytical derivation AI-based Cobb-Douglas shows that elements of TFP from the Cobb-Douglas can be explained by wages and rates of return on IT and non-IT capital and that the only remaining element is a constant of integration. Although we cannot make a definitive empirical connection due to lack of available data, the rates of return to IT likely capture indirect effects from IT capital such as IT-related organizational capital (Brynjolfsson and Hitt 2003), IT knowledge spillovers (Hitt and Tambe 2006, Tambe and Hitt 2010), and supply chain IT spillovers (Cheng and Nault 2007, 2012). That is, the significance of the coefficients of logged rates of return in the AI-based Cobb-Douglas is solid empirical evidence that our form that contains rates of returns on inputs explains a significant part of TFP. Thus, many unobservables that have been considered part of TFP can be identified in rates of return, and this supports the current research program of decomposing TFP to uncover unobservable effects of IT. Moreover, it supports an actionable and compelling way to uncover sources of IT value by relating specific IT investments to rates of return.

These contributions also serve to provide actionable recommendations for IT productivity researchers. When considering the use of the Cobb-Douglas form, the first is to examine the intertemporal stability of input shares and where possible conduct split sample estimates where input shares are more stable. Next, a poor fit to productivity data or unexpected signs or magnitudes of coefficient estimates suggest problems with data quality or substantial intertemporal instability of input shares. With the additional terms in the AI-based Cobb-Douglas being rates of return that vary over time, TFP should be modeled as time varying. Finally, the use of aggregate data such as industry-level data is not an issue so long as input shares are reasonably stable because in that case the income accounting identity holds at all levels.

Our analyses have highlighted three specific limitations and a broader limitation of much IT productivity research for which there may be fruitful future research. The robustness of the AI-based Cobb-Douglas in estimation to substantial changes in input shares is surprising—even with share changes up to 85% over eight years (e.g., IT capital in our later subperiod) the estimation shows strong empirical regularity. Better understanding the limits of input share changes while still providing robust estimation would broaden the domain of applications to which the use of the Cobb-Douglas in IT productivity work is appropriate. Even though empirically we found the Cobb-Douglas form is robust to substantial changes in input shares, this is not always the case. Indeed, as we suggest above, large changes in input shares is a solid explanation for lack of fit to data or problem estimates.

We also noticed apparent differences between the two subperiods in the magnitudes of the output elasticity of labor and the coefficient of the logged wage rate. In the earlier subperiod the output elasticity is higher and the coefficient of the logged wage rate is correspondingly lower than in the later subperiod.

Third, our results point to elements of IT’s impact on productivity captured in rates of return to IT capital that are not necessarily captured in its output elasticity. We take these elements as part of TFP and make the conceptual connection that these may also summarize the effects through IT-based organizational capital and various IT spillovers. However, we do not have the data to more thoroughly examine the relationship between the rate of return to IT capital and these other effects that have been substantiated in the literature—this would be an important avenue for future work.

Finally, there is a stream of literature in productivity research that recognizes revenue-based measures of output, whereby output (or value added) in real terms is calculated by revenue divided by a price deflator, and may not represent true production quantities (e.g., Foster et al. 2008). This is because idiosyncratic demand shifts or market power variations can affect prices, which in turn affect revenue, and neither these shifts nor variations are related to quality or productive efficiency as captured by a production function. Moreover, they remain through aggregation. If these effects on prices are substantial, then they may be important considerations in the accounting identity and our resulting analyses would be different. This is also a possible direction for future research.

## Acknowledgments

The authors thank Al Dexter, Kunsoo Han, Guido Schryen, J. Richard Dietrich, Eric Spires, John Butler, the participants at the 20th Anniversary WISE 2009, and seminar participants at INFORMS 2004 in Banff, Alberta and at the iRC/MIS Colloquia at the University of Calgary for helpful comments. They also thank Randal Kinoshita at the Bureau of Labor Statistics for providing specialized data, Hans Uli Buhl at the University of Augsburg for collaboration support, and Jeanette Burman for editing support. Support was also provided by the German Academic Exchange Service, the University of Calgary, the Ohio State University, the University of Paderborn, and by the Social Science and Humanities Research Council of Canada.

## References

Brynjolfsson E, Hitt LM (1995) Information technology as a factor of production: The role of differences among firms. Econom. Innovation New Tech. 3(3–4):183–189.

Brynjolfsson E, Hitt LM (1996) Paradox lost? Firm-level evidence on the returns to information systems spending. Management Sci. 42(4):541–558.

Brynjolfsson E, Hitt LM (2003) Computing productivity: Firm-level evidence. Rev. Econom. Statist. 85(4):793–808.

Bulkley N, Van Alstyne M (2004) Why information should influence productivity. Castells M, ed. Network Society: A Cross-Cultural Perspective (Edward Elgar, Cheltenham, UK), 145–173.

Cheng Z, Nault BR (2007) Industry level supplier-driven IT spillovers. Management Sci. 53(8):1199–1216.

Cheng Z, Nault BR (2012) Relative industry concentration and customer-driven IT spillovers. Inform. Systems Res. 23(2): 340–355.

Chwelos P, Ramirez R, Kraemer KL, Melville N (2010) Does technological progress alter the nature of information technology as a production input? New evidence and new results. Inform. Systems Res. 21(2):392–408.

Cohen AJ, Harcourt GC (2003) Whatever happened to the Cambridge capital theory controversies? J. Econom. Perspect. 17(1):199–214.

Dewan S, Kraemer KL (2000) Information technology and productivity: Evidence from country-level data. Management Sci. 46(4):548–562.

Dewan S, Min C (1997) The substitution of information technology for other factors of production: A firm-levelanalysis. Management Sci. 43(12):1660–1675.

Felipe J (2000) On the myth and mystery of Singapore’s “Zero TFP.” Asian Econom. J. 14(2):187–209.

Felipe J (2001) Aggregate production functions and the measurement of infrastructure productivity: A reassessment. Eastern Econom. J. 27(3):323–344.

Felipe J, McCombie JSL (2001) The CES production function, the accounting identity, and Occam’s razor. Appl. Econom. 33(10):1221–1232.

Fisher FM (1971) Aggregate production functions and the explanations of wages: A simulation experiment. Rev. Econom. Statist. 53(4):305–325.

Foster L, Haltiwanger J, Syverson C (2008) Reallocation, firm turnover, and efficiency: Selection on productivity or profitability? Amer. Econom. Rev. 98(1):394–425.

Greene WH (2003) Econometric Analysis, 5th ed. (Prentice-Hall, Upper Saddle River, NJ).

Gurbaxani V, Melville N, Kraemer KL (2000) The production of information services: A firm-level analysis of information systems budgets. Inform. Systems Res. 11(2):159–176.

Hitt LM, Tambe P (2006) Measuring spillovers from information technology investments. Proc. 27th Internat. Conf. Inform. Systems, Milwaukee, 1793–1802.

Jorgenson DW, Griliches Z (1967) The explanation of productivity change. Rev. Econom. Stud. 34(3):249–283.

Lee B, Barua A (1999) An integrated assessment of productivity and efficiency impacts of information technology investments: Old data, new analysis and evidence. J. Productivity Anal. 12(1): 21–43.

Leontief WW (1947a) A note on the interrelationship of subsets of independent variables of a continuous function with continuous first derivatives. Bull. Amer. Math. Soc. 53(4):343–350.

Leontief WW (1947b) Introduction to a theory of the internal structure of functional relationships. Econometrica 15(4):361–373.

Levi MD (1973) Errors in the variables bias in the presence of correctly measured variables. Econometrica 41(5):985–986.

Lichtenberg FR (1995) The output contributions of computer equipment and personnel: A firm-level analysis. Econom. Innovation New Tech. 3(3–4):201–217.

Menon NM, Lee B, Eldenberg L (2000) Productivity of information systems in the healthcare industry. Inform. Systems Res. 11(1):83–92.

Mittal N, Nault BR (2009) Investments in information technology: Indirect effects and information technology intensity. Inform. Systems Res. 20(1):140–154.

Nataf A (1948) Sur la possibilite de construction de certains macromodeles. Econometrica 16(3):205–221.

Oliner SD, Sichel DE (2000) The resurgence of growth in the late 1990’s: Is information technology the story? J. Econom. Perspect. 14(4):3–22.

Robinson J (1953-54) The production function and the theory of capital. Rev. Econom. Stud. 21(1):81–106.

Samuelson PA (1962) Parable and realism in capital theory— The surrogate production function. Rev. Econom. Stud. 29(3): 193–206.

Samuelson PA (1979) Paul Douglas’s measurement of production functions and marginal productivities. J. Political Econom. 87(5):923–939.

Shaikh A (1974) Laws of production and laws of algebra: The humbug production function. Rev. Econom. Statist. 56(1):115–120.

Simon HA (1979) On parsimonious explanations of production relations. Scandinavian J. Econom. 81(4):459–474.

Solow R (1974) Laws of production and laws of algebra: The humbug production function: Comment. Rev. Econom. Statist. 56(1):121.

Solow R (1987) Second thoughts on growth theory. Steinherr A, Weiserbs D, eds. Employment and Growth: Issues for the 1980s (Martinus Nijhoff, Dordrecht, The Netherlands), 13–28.

Solow RM (1955–56) The production function and the theory of capital. Rev. Econom. Stud. 23(2):101–108.

Sraffa P (1960) Production of Commodities by Means of Commodities (Cambridge University Press, Cambridge, UK).

Stiglitz JE (1974) The Cambridge–Cambridge controversy in the theory of capital: A view from New Haven: A Review. J. Political Econom. 82(4):893–903.

Stiroh KJ (2002) Information technology and the U.S. productivity revival: What do the industry data say? Amer. Econom. Rev. 92(5):1559–1576.

Strassner EH, Medeiros GW, Smith GM (2005) Annual industry accounts: Introducing KLEMS input estimates for 1997–2003. Survey of Current Business 85(September):31–39.

Tambe P, Hitt LM (2010) Job hopping, knowledge spillovers, and regional returns to information technology investments. Sabherwal R, Summer M, eds. Proc. 31st Internat. Conf. Inform. Systems, St. Louis.

van Garderen KJ, Lee K, Pesaran MH (2000) Cross-sectional aggregation of non-linear models. J. Econometrics 95(2):285–331.

Walters AA (1963) Production and cost functions: An econometric survey. Econometrica 31(1–2):1–66.

Whelan K (2002) A guide to U.S. chain aggregated NIPA data. Rev. Income Wealth 48(2):217–233.
