---
otero_id: 15310
otero_key: "U3QC3TJP"
title: "Research Commentary—Information Technology Substitution Revisited"
authors: "Dawei Zhang; Zhuo (June) Cheng; Hasan A. Qurban H. Mohammad; Barrie R. Nault"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2015.0570"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/U3QC3TJP/fulltext/images/1dc4c9b7c609d1c9b6f359332f8fd6340d110fd121fb5d52caf02c697bbb04d6.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Commentary—Information Technology Substitution Revisited

Dawei Zhang, Zhuo (June) Cheng, Hasan A. Qurban H. Mohammad, Barrie R. Nault

## To cite this article:

Dawei Zhang, Zhuo (June) Cheng, Hasan A. Qurban H. Mohammad, Barrie R. Nault (2015) Research Commentary—Information Technology Substitution Revisited. Information Systems Research 26(3):480-495. http://dx.doi.org/10.1287/isre.2015.0570

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2015, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/U3QC3TJP/fulltext/images/fb9ce033cdb9465058f4fa869dd7059e4f43b62522ab7e1198cb63440a2c2186.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

http://dx.doi.org/10.1287/isre.2015.0570 © 2015 INFORMS

# Research Commentary Information Technology Substitution Revisited

Dawei Zhang College of Business and Economics, Lehigh University, Bethlehem, Pennsylvania 18015, daz215@lehigh.edu

Zhuo (June) Cheng

School of Accounting and Finance, Faculty of Business, Hong Kong Polytechnic University, Hung Hom, Kowloon, Hong Kong, afzcheng@polyu.edu.hk

Hasan A. Qurban H. Mohammad

College of Business Administration, Kuwait University, Safat 13055 Kuwait, hqurban@cba.edu.kw

Barrie R. Nault

Haskayne School of Business, University of Calgary, Calgary, Alberta T2N 1N4, Canada, nault@ucalgary.ca

aking advantage of the opportunities created by the price adjusted performance improvement in information technology (IT) depends in part on the ability of IT capital to substitute for other inputs in production. Studies in the information systems literature and most economics training examining the substitution of IT capital for other inputs use the Allen elasticity of substitution (AES). We present a less-well-known measure for the elasticity of substitution, the Morishima elasticity of substitution (MES). In contrast to the AES, which is misleading when there are three or more inputs—such as non-IT capital, labor, and IT capital—the MES provides a substitution measure where the scale is meaningful, and the measure differs depending on which price is changing. This is particularly important for IT capital, because prices have been declining, and there is evidence that IT capital can substitute for non-IT capital or labor in a qualitatively different way than non-IT capital and labor substitute for each other. Methodologically, we also show the impact of imposing local regularity—for example, monotonicity of output from increases in inputs—which we do through Bayesian methods employed to estimate the underlying functions that are used to calculate various measures of substitution. We demonstrate the importance of the MES as an underrecognized measure of substitution and the impact of imposing local regularity using an economy-wide industry-level data set covering 1998–2009 at the three-digit North American Industry Classification System code level. Our MES results show that reductions in the price of IT capital increase the quantity of IT capital in use, but are unlikely to change the input share of IT capital—the value of IT capital as a proportion of the value of all inputs—in contrast to major studies using the AES. In addition, estimates for both elasticities of substitution are more stable after imposing local regularity. Both of these advances—that is, the MES and imposing local regularity—have the potential to impact future work on IT productivity, IT pricing, IT cost estimation, and any type of analysis that posits the substitution of IT capital for non-IT capital or labor.

Keywords: information systems; IT policy and management; economics of IS; IT substitution; production function

History: Anandhi Bharadwaj, Senior Editor and Associate Editor. This paper was received August 19, 2013, and was with the authors 5 months for 3 revisions. Published online in Articles in Advance May 8, 2015.

## 1. Introduction

Critical to our society, economy, and research in information systems (IS) is the impact of information technology (IT) on production, jobs, and other capital. One key set of measures to assess this impact is the economic measures that determine trade-offs between the amounts of labor, non-IT capital, and IT capital used in production as the result of wage or price changes— the elasticity of substitution (ES). The objective of this Research Commentary is to present an important and underrecognized ES, the Morishima elasticity of substitution, or MES, and describe its benefits, especially for IT as an input, over more frequently used measures. In so doing, we will show why it is critical to isolate which price is changing in any ES measure.

The major studies from the IS literature that examine substitution of IT capital for other inputs concentrate on the Allen elasticity of substitution (AES). When there are three or more inputs—such as non-IT capital, labor, and IT capital—the AES has strict limitations: it is not a measure of ease of substitution and can only provide the direction of the change in quantity of one input in response to a price change of the other input (Blackorby and Russell 1981, 1989).

Fortunately, Blackorby and Russell (1981) discovered the Japanese article by Morishima (1967), an article that has yet to be translated into English, that introduces the MES. In contrast to the AES, in the context of three or more inputs, the scale and sign of the MES are sufficient statistics for assessing both quantitative and qualitative effects of changes in price on input quantity ratios and on relative input shares. Moreover, the MES allows for different MESs depending on which input price is changing. This matters because the price of IT capital is the only input price that has been consistently decreasing, and because IT capital can have broader effects than typical non-IT capital and labor. Thus, it is possible to determine the effect of a change in the price of an input on the relative share of an input; that is, even though IT capital may be a substitute for other inputs, the increased use of IT in response to a price reduction in IT may result in a reduced relative input share of IT, where relative share is price times quantity of IT divided by price times quantity of another input.

In addition to introducing the MES, we present an underrecognized and potentially important methodological issue: the importance of imposing local regularity such that the estimated function from which the parameters are used to calculate the ES follow its theoretical properties—for example, the monotonicity of output from increases in inputs. Imposing local regularity increases the stability and accuracy of the estimates, reducing the chance of erroneous and misleading results.

## 1.1. Overview of Our Approach

We begin by briefly reviewing ESs, and then we explain the two different ESs from a production perspective. In this explanation we aggregate much of the relevant economic literature that describes the differences between the AES and MES, the underlying problems with the AES, and how the MES overcomes these problems.

Next we execute an analysis that yields estimates for the AES and MES. In so doing we demonstrate the differences between the two ESs, and, perhaps more importantly, through our MES estimates we provide evidence for a different level of substitution by IT when the price of IT changes. Using an economy-wide industry-level data set for 1998-2009, we estimate both the MES and the AES using nonlinear regression and Bayesian analyses. We employ one flexible functional form (FFF), the constant elasticity of substitution (CES)-translog, to estimate a production function with three inputs—non-IT capital, IT capital, and labor—and use the estimated parameters to calculate the AES and MES. We then examine whether there are violations of regularity conditions, and when there are, we impose regularity conditions using Bayesian methods to reestimate the FFF and use these newly estimated parameters to recalculate the AES and MES.

## 2. Background Literature

Prior studies in the IS literature have examined ESs between IT capital and other inputs. In an excellent article in Management Science, Dewan and Min (1997) used firm-level data from 1988 to 1992 to estimate translog and CES-translog production functions and then calculated AESs. They found that IT capital is a substitute for non-IT capital and labor. In another excellent article in this journal, Chwelos et al. (2010) used firm-level data from 1987 to 1998 to estimate the translog and CES-translog forms, and then calculated AESs. They found that IT capital is a substitute for labor, but in their more recent data they found that IT capital and non-IT capital have become complements. They also found that over time, more units of IT capital are needed to substitute for a unit of labor. In a working paper, Hitt and Snir (1999) matched survey data of organizational practices from 1995 to 1996 with firm-level data on IT spending and output and inputs from 1987 to 1994 and estimated a translog form to calculate AESs. They also found that IT is a substitute for non-IT capital and labor. Outside of the IS literature, Chun and Mun (2006) in the Southern Economic Journal used cost function estimates from a selection of U.S. industries for 1984–1999 to calculate ESs. Their AESs indicate that IT capital is a substitute for labor, non-IT equipment, and structures, whereas IT is a complement to intermediate inputs. Their MESs show that IT capital and intermediate inputs are substitutes when the price of IT capital changes, but complements when the price of intermediate inputs changes.

Unfortunately, in the published studies in IS detailed above, results from the AES were used in a chain of reasoning to support implications regarding the balance of IT capital and the other inputs, non-IT capital and labor, that in fact the AES cannot be used to show. Indeed, Dewan and Min (1997) state that as a consequence of the AES findings whereby IT capital is a substitute for non-IT capital and labor, the input share of IT capital would increase over time. Chwelos et al. (2010) make a similar prediction given their AES findings that IT capital is a substitute for labor, indicating that the input share of IT capital comes at the expense of labor. As we indicated in §1 and will report in detail in §3, with three or more inputs, the AES does not provide any information about input shares, and, using the MES, we find empirically that an increasing input share for IT capital in response to a decline in the price of IT capital, ceteris paribus, is not correct for the time period covered by our data set. Moreover, both Dewan and Min (1997) and

Chwelos et al. (2010) compare the AES between subsets of industries such as manufacturing and services, and draw conclusions from these comparisons. Again, as we indicated earlier and will see in detail in $\ S 3 ,$ with three or more inputs, the relative magnitudes of the AES have no meaning, and comparisons between AESs are not useful. Indeed, this overinterpretation of the AES when there are more than two inputs has likely plagued a wide range of research for more than a generation.

Although the AES has been the standard in IS literature and the dominant ES taught and used in economics, research since the early 1980s has shown it is a misleading and relatively uninformative measure when used in analyses with more than two inputs (e.g., Blackorby and Russell 1981, 1989). This research also explains why the MES is a superior measure. One possible reason why the MES is taking longer to penetrate the literature is that, as mentioned in §1, the original Morishima (1967) article has yet to be translated into English. In contrast, the AES traces its origins to a classic mathematical economics textbook by Allen (1938) and was generalized to more than two inputs by Uzawa (1962) in the well-known Review of Economic Studies.

## 3. Methodology

## 3.1. Elasticities of Substitution

Hicks (1932) introduced the Hicks elasticity of substitution (HES) to examine the substitutability between inputs. His purpose was to provide a measure of the curvature of the isoquant, or ease of substitution, and comparative statics regarding relative input shares. Allen (1938) introduced the AES as a measure of substitution. The information properties of the HES are satisfied by the AES for two inputs. However, for more than two inputs, the AES is not a measure of curvature and provides no information regarding relative input shares (Blackorby and Russell 1981, 1989).

Fortuitously, Blackorby and Russell (1981) discovered the Morishima (1967) article that introduces the MES. For an arbitrary number of inputs, the MES is a measure of the curvature of the isoquant and provides comparative statics of relative input shares.

## 3.2. Production and Elasticities of Substitution

We define a production function as $Y = f ( x )$ , where Y is output in units, and x is a vector of inputs containing non-IT capital K, labor L, and IT capital Z. We use capital letters for quantities of $Y , K , L ,$ and Z, and we use lowercase letters to denote natural logs of these quantities later on. Generically, our inputs are over i ∈ 8K1 L1 Z9. We take $f ( x )$ to have the usual properties: single valued, nonnegative, and real for all finite $x ,$ monotonic, concave, continuous, and twice continuously differentiable. Following Chambers (1988), we can define $V ( Y ) = x \colon f ( x ) \geq Y ,$ , which is closed and nonempty, and the lower bound of $V ( Y )$ is defined by the level set $\tilde { V } ( Y ) = \{ x \colon f ( x ) = Y \}$ . Consequently, by the implicit function theorem, we can solve for a given $x _ { i }$ in terms of the remaining x and $Y .$

For constant output we can obtain the marginal rate of technical substitution (MRTS), which is the rate at which one input can be substituted for another while holding the level of output constant

$$
\partial x _ {i} / \partial x _ {j} = - \frac {\partial f (x) / \partial x _ {j}}{\partial f (x) / \partial x _ {i}} = - f _ {j} / f _ {i},
$$

where subscripts of $f$ indicate partial derivatives so that $f _ { i }$ is the partial derivative of $f ( x )$ with respect to x . In a classic work, Hicks (1932) developed an ES between inputs as a percentage change in the input ratio in response to a percentage change in the MRTS

$$
\sigma = \frac {d (x _ {i} / x _ {j}) / [ x _ {i} / x _ {j} ]}{d (f _ {j} / f _ {i}) / [ f _ {j} / f _ {i} ]}.
$$

In the two-factor case, the HES provides two pieces of information. The first is a measure of the curvature of the isoquant, or ease of substitution. The higher the elasticity, the “easier” the substitution of one input for the other—in other words, the lesser the degree of curvature of the isoquant. The second is comparative statics regarding relative input shares (Blackorby and Russell 1989).

The HES was generalized for the n-factor case by Uzawa (1962) to the AES. In the context of production functions, the AES is given by

$$
\sigma_ {i j} ^ {A} = \frac {\sum_ {i} x _ {i} f _ {i}}{x _ {i} x _ {j}} \frac {\mathrm{H} _ {i j}}{\mathrm{H}},\tag{1}
$$

where H is the bordered Hessian determinant of $f ( x )$ and $\mathrm { H } _ { j i }$ is the cofactor associated with $f _ { i j } .$ In the AES, factors i and j are substitutes if $\sigma _ { i j } ^ { A } > 0 ,$ , which means that increasing the price of the jth input increases the optimal quantity demanded of input i. If $\sigma _ { i i } ^ { A } < 0 ,$ , then inputs i and j are complements such that decreasing the price of input j increases the optimal quantity demanded of input i. From the monotonicity of the production function, own price elasticity is negative, $\bar { \boldsymbol { \sigma } } _ { i i } ^ { A } < 0$

The AES embeds some important restrictions. First, the AES is symmetric so that $\sigma _ { i j } ^ { A } = \sigma _ { j i } ^ { A }$ . Consequently, the AES does not depend on which price is changing. Second, from the properties of $f { \bar { ( } } x { \bar { ) } }$ , for a given input $x _ { r } ,$ at least one $\dot { } \sigma _ { r j } ^ { A }$ must be positive so that a given input must be a substitute for at least one other input. In the context of our production function, this latter restriction means that $\hat { \sigma } _ { Z K } ^ { A }$ and $\sigma _ { Z L } ^ { A }$ cannot both be negative (Chambers 1988), so that IT capital must be a substitute for either non-IT capital or labor, or both.

Blackorby and Russell (1989) argue that the AES is not informative beyond the cross-price elasticity of demand. The AES in (1) can be expressed as

$$
\sigma_ {i j} ^ {A} = \epsilon_ {i j} / s _ {j},
$$

where $\epsilon _ { i j } = \partial \ln x _ { i } / \partial \ln p _ { j }$ is the (constant output) cross-price elasticity of demand, and $s _ { j }$ is input $j ^ { \prime } \mathbf { s }$ cost share of the producer’s total expenditure, $s _ { j } =$ $x _ { j } p _ { j } / \sum _ { i } x _ { i } p _ { i }$ . As such, the AES is not a measure of the curvature of the isoquant. They also argue that the AES does not provide information regarding relative input shares, concluding that “absolute income shares is a property of cross-price elasticities and shares; the AES provides no new information about these shares” (Blackorby and Russell 1989, p. 884).

In contrast to the AES, the MES can be defined as

$$
\sigma_ {i j} ^ {M} = \frac {f _ {j}}{x _ {i}} \frac {\mathrm{H} _ {i j}}{\mathrm{H}} - \frac {f _ {j}}{x _ {j}} \frac {\mathrm{H} _ {j j}}{\mathrm{H}}.\tag{2}
$$

We can rearrange to express the MES in terms of the AES as follows:

$$
\sigma_ {i j} ^ {M} = \frac {f _ {j} x _ {j}}{\sum_ {i} f _ {i} x _ {i}} [ \sigma_ {i j} ^ {A} - \sigma_ {j j} ^ {A} ].
$$

The interpretation of substitutes and complements in the MES relates to the relative quantities of inputs, $x _ { i } / x _ { j }$ . In the MES, inputs i and j are substitutes if $\sigma _ { i j } ^ { M } > 0 ,$ , which means that increasing the price of the jth input increases the quantity of input i relative to the quantity of input $j ;$ that is, for normal goods (or inputs) where an increase in the price of the jth input results in a decreased quantity of the jth input, $\dot { x } _ { j } , \sigma _ { i j } ^ { M } > 0$ means the ratio of input quantities, $x _ { i } / x _ { j } ,$ increases, recognizing that this can occur with a decreased $x _ { i } .$ Inputs i and j are complements if $\sigma _ { i j } ^ { M } < 0 :$ an increase in the price of j decreases not only the quantity of input j but also decreases the quantity of input i such that the ratio $x _ { i } / x _ { j }$ decreases.

The MES is not symmetric, which means that, in general, $\sigma _ { i j } ^ { M } \neq \sigma _ { j i } ^ { M }$ . The MES can also classify substitution elasticities differently from the AES. For example, two inputs i and j could be Allen complements, $\sigma _ { i j } ^ { A } < 0 ,$ while being Morishima substitutes, $\bar { \sigma } _ { i j } ^ { M } > 0 .$ , following the description above where $x _ { i }$ may decrease along with $x _ { j } .$ . Hence, “the Allen measure has a bias toward treating inputs as complements (or, the Morishima measure has a bias toward treating inputs as substitutes)” (Mundra and Russell 2004, p. 35), reflecting the fact that the AES measures changes in absolute quantities, and the MES measures changes in relative quantities.

Blackorby and Russell (1989) make the point that the MES is a measure of curvature of the isoquant, or ease of substitution, and that the MES provides comparative static information about relative input shares. Using a cost function formulation (which is dual to our production function constant output formulation), they show that

$$
\frac {\partial \ln [ x _ {j} p _ {j} / x _ {i} p _ {i} ]}{\partial \ln [ p _ {j} / p _ {i} ]} = 1 - \sigma_ {i j} ^ {M}.
$$

The above equation can be rewritten as

$$
\frac {- \partial \ln [ x _ {i} p _ {i} / x _ {j} p _ {j} ]}{\partial \ln [ p _ {j} / p _ {i} ]} = 1 - \sigma_ {i j} ^ {M}.\tag{3}
$$

The equation in (3) relates a change in the relative input share, $x _ { i } p _ { i } / x _ { j } p _ { j }$ , from an underlying change in the price ratio, $p _ { j } / p _ { i } ,$ to the MES. The partial derivative in (3) requires that the percentage change in the price ratio, $p _ { j } / p _ { i } ,$ is induced solely by changing the price of input $j ,$ because allowing both $p _ { j }$ and $p _ { i }$ to vary would entail variation in all other price ratios, $p _ { k } / p _ { i } , k \neq i ,$ contrary to the definition of partial differentiation. Thus, consider input $j$ is IT capital where $p _ { j }$ has been falling over time. For a given decrease in the price ratio $p _ { j } / { p _ { i } }$ induced by a drop in $p _ { j } ,$ the share of another input i, say, non-IT capital or labor, relative to input $j ,$ IT capital, decreases if $\sigma _ { i i } ^ { M } > 1$ and increases if the $\sigma _ { i i } ^ { \mathrm { \prime } M } < 1$

According to Chambers (1988), the MES can be written as

$$
\sigma_ {i j} ^ {M} = \frac {\partial \ln [ x _ {i} / x _ {j} ]}{\partial \ln [ p _ {j} ]}.\tag{4}
$$

Thus, the MES is a two-factor, one-price ES because the MES measures relative input adjustment to singleinput price changes. On the other hand, the AES measures how a single input adjusts to changes in a single-input price, and thus is a one-price, one-factor ES (Chambers 1988). The MES does not measure relative input adjustment to relative price changes because the effect on the relative input shares of changing $p _ { i }$ instead of $p _ { j }$ is generally different.

## 3.3. Empirical Methodology

3.3.1. Estimation Form. Measuring the AES and the MES requires estimating parameters of a functional form that is sufficiently flexible to provide a suitable fit for most data sets. Following earlier research (Dewan and Min 1997, Chwelos et al. 2010), we employ the CES-translog production function. The CES-translog (Pollak et al. 1984) is a FFF, which includes both the CES and the translog production functions as special cases. Using lowercase letters to represent the natural log of our variables, the CES-translog production function for three inputs is

$$
\begin{array}{l} y = \alpha - \frac {1}{\rho} \ln [ \delta_ {z} Z ^ {- \rho} + \delta_ {k} K ^ {- \rho} + (1 - \delta_ {z} - \delta_ {k}) L ^ {- \rho} ] + \beta_ {z k} z k \\ \quad + \beta_ {z l} z l + \beta_ {k l} k l + \beta_ {z z} z ^ {2} + \beta_ {k k} k ^ {2} + \beta_ {l l} l ^ {2} + \epsilon , \end{array} \tag {5}
$$

where $y$ is value added (as a measure of output), z is IT capital, k is non-IT capital, l is labor, and  is an error term.

Table 1 Summary Statistics 4N = 7085

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td>Value added (Y) (in millions of 2005 dollars)</td><td>175,787</td><td>232,158.2</td><td>-5,532.266</td><td>1,545,957</td></tr><tr><td>Labor (L) (in millions of hours)</td><td>3,154.267</td><td>4,486.429</td><td>84</td><td>25,810</td></tr><tr><td>Non-IT capital stock (K) (in millions of 2005 dollars)</td><td>233,465.3</td><td>318,652.7</td><td>9,381</td><td>1,924,724</td></tr><tr><td>IT capital stock (Z) (in millions of 2005 dollars)</td><td>29,747.91</td><td>49,982.64</td><td>413</td><td>358,847</td></tr></table>

3.3.2. Data Set. Our data set consists of the multifactor-productivity (MFP) data set for the three-digit 2002 North American Industry Classification System (NAICS) from 1998 to 2009. We acquired data on capital stock, IT capital stock, and labor input for 59 threedigit NAICS code industries directly from the U.S. Bureau of Labor Statistics (BLS) website. There are four categories for IT capital stock: computers, software, communication, and other. The productive capital stock of these four IT categories is aggregated as Z. For the non-IT capital stock (K), we totaled the equipment and structure components of the asset types and subtracted the IT capital stock from it. Both IT capital and non-IT capital are collected in millions of 2005 US dollars. The labor input, L is in millions of hours. We also collect current dollar value added (Y ) at the three-digit NAICS code level from the Bureau of Economic Analysis. Deflating it by the corresponding chain-type quantity indexes for output (2005) yields the real value added Y in millions of 2005 dollars. In the end, we have a balanced panel of 708 observations from 12 years of data on 59 industries. Table 1 contains summary statistics for our data set. All of our data are publicly available.

3.3.3. Industry Groups. Our data set covers a broad range of industry groups. Different industry groups may have different fixed effects when estimating the parameters of the CES-translog production function. Different industry groups may also have very different ESs. Therefore, we classify our data set into 12 industry groups both for including fixed effects in estimation and for reporting ESs: manufacturing (NAICS codes 31–33); transportation, communications, and public utilities (NAICS codes 22, 48, and 49); wholesale trade (NAICS code 42); retail trade (NAICS codes 44 and 45); accommodation, food services, and drinking places (NAICS code 72); finance, insurance, and real estate (NAICS codes 52 and 53); entertainment (NAICS codes 51 and 71); professional services (NAICS codes 54, 56, and 81); educational services, health care, and social assistance (NAICS codes 61 and 62); forestry (NAICS code 11); mining (NAICS code 21); and construction (NAICS code 23).<sup>1</sup>

## 3.4. Estimation

We first use nonlinear least-squares methods to estimate our CES-translog form in (5) for our data set. Then, to impose regularity conditions, we use Bayesian-based methods to obtain the parameters.

## 3.4.1. Nonlinear Least-Squares Approach.

CES-translog. To obtain the converged value for all 10 parameters in the CES-translog form in (5), we adopt the approach of “maximization by $\mathsf { p a r t s } ^ { \prime \prime }$ (Song et al. 2005, Fan et al. 2007, Amado and Terasvirta 2013), where we divide the 10 parameters into two sets, iteratively fix one set, and obtain estimates for the other set until convergence. Specifically, Set 1 includes the three parameters $( \rho , \delta _ { z } ,$ and $\delta _ { k } )$ from the $\prime \prime \mathrm { C E S ^ { \prime \prime } }$ part of the CES-translog form. Set 2 includes the remaining seven parameters $( \alpha , \beta _ { z k } , \beta _ { z l } , \beta _ { k l } , \beta _ { z z } ,$ $\beta _ { k k }$ , and $\beta _ { l l } )$ that are the nonlinear parts of the translog form.

We use 1,000 iterations of our process in Figure 1 to generate our final parameter estimates. To start a given iteration, we randomly generate values for Set 1 from a uniform distribution on 6−101 107. Keeping these randomly generated values for Set 1 as fixed, Set 2 is estimated by the nonlinear least squares (NL) method in Stata SE 10.1 that uses a variation of the Gauss–Newton algorithm for optimization. These newly obtained estimates from Set 2 are then fixed, and Set 1 is estimated by the NL method. The result is a local optima for the current iteration. At the end of each iteration, the global optima are replaced by the local optima from the current iteration when they lead to a lower residual sum of squares (RSS). This follows Chwelos et al. (2010) in that we iteratively randomly generate starting values for the parameters to be estimated, execute the nonlinear optimization process, and then take the results with the minimum RSS. Consequently, among the converged results from all 1,000 iterations, we select the set of results with the minimum RSS as our final estimates for the 10 CES-translog parameters. We use the 1,000 iterations to ensure that our results do not depend on a particular set of starting values and thus are global optima in terms of minimum RSS.<sup>2</sup>

Figure 1 (Color online) Nonlinear Estimation Flowchart  
![](/api/attachments/U3QC3TJP/fulltext/images/065cd43f89070b1ae5a080a938fa3906a29d7d53ed25298d8bb1876408d9b05e.jpg)

## 3.4.2. Bayesian Approach.

The impact of regularity conditions. The CES-translog form in (5) is a FFF. Many researchers argue that the usefulness of a FFF hinges on whether the estimated parameters satisfy regularity conditions such as nonnegativity, monotonicity, and concavity for production functions. Violating any of these conditions causes the second-order conditions for optimizing behavior and duality theory to fail (Barnett 2002). Inferences obtained from an estimated FFF that violates any regularity condition are unreliable (Barnett and Pasupathy 2003). Monotonicity violation leads to incorrectly signed elasticities, and curvature violation leads to production frontiers that are convex to the origin (Caves and Christensen 1981, Diewert and Wales 1987, Morey 1986). We focus on the monotonicity conditions in our study because they directly affect the elasticities, and it is generally agreed that greater amounts of input should not yield less output. To show the impact of violating monotonicity on the sign of an ES, consider our form in (5). Monotonicity is satisfied if $f _ { i } \geq 0 ,$ where i = 8k1 l1 z9. Clearly, both the AES and the MES given by (1) and (2), respectively, are functions of H and $f _ { i } .$ Thus, by definition, the sign of the ES is influenced by the sign of $f _ { i } ,$ which in turn determines whether the estimated parameters satisfy monotonicity.

We do not impose concavity for two reasons. First, theoretically, concavity is essentially a condition of diminishing returns. However, diminishing returns have been challenged in the case of IT capital both conceptually and by previous research that has documented increasing returns to IT capital (Kudyna and Diwan 2002). Second, implementation imposing both concavity and monotonicity leads to zero acceptance in our Monte Carlo simulation, possibly because of IT having increasing returns and also because imposing a second moment restriction across every observation in a data set is a severe constraint.

There are two approaches to impose regularity conditions. The first imposes parametric restrictions on the FFF to ensure that conditions hold at all data points. For example, global curvature restrictions can be achieved by using eigenvalue decomposition techniques and Cholesky factorization methods (Diewert and Wales 1987). Although not the same as imposing regularity, Dewan and Min (1997) used regularity conditions via parametric restrictions as a selection criterion between translog and CES-translog production functions. In their data set, they note that the violation rate for the translog function is 89% and virtually zero for CES-translog. Unfortunately, the methods used to impose parametric restrictions undermine the flexibility of most functional forms (Jorgenson and Fraumeni 1981), and the global imposition of regularity conditions forces many FFFs to exhibit unintended properties. For example, imposing global concavity on the inputs of a translog cost function may lead to an upward bias in the degree of substitutability, and on a generalized Leontief cost function forces all inputs to be substitutes (Diewert and Wales 1987). Barnett and Pasupathy (2003) argue that imposing regularity conditions globally actually increases the frequency of monotonicity violations.

The second approach imposes regularity conditions locally. Several studies demonstrate that the advantages of local regularity imposition outweigh those of global regularity imposition (Lau 1978, Diewert and Wales 1987, Terrell 1996, O’Donnell and Coelli 2005). Local imposition of regularity means that constraints are imposed at a single point, at several points, or over a region for which inferences will be drawn (Gallant and Golub 1984, Salvanes and Tjotta 1998). Local imposition of regularity conditions can be achieved through sampling theoretic procedures (Jorgenson and Fraumeni 1981, Ryan and Wales 1998, Moschini 1999). More recently, a Bayesian approach using Monte Carlo simulation methods was proposed to impose regularity locally on the parameters of the estimated FFF.

We adopt the second approach and examine the compliance of the nonlinear least squares parameter estimates with monotonicity by examining the marginal products of the three input factors. In particular, we check compliance with the monotonicity conditions for each observation in our data set and find that about 30% of observations violate at least one of the monotonicity conditions. This violation may undermine the validity of the inferences that are based on the non-linear least squares parameter estimates of the model. Thus, imposing regularity conditions is likely necessary.

CES-translog. Through Bayesian estimation of our CES-translog model in (5), we have the flexibility and the ability to restrict the sampled parameter estimates (i.e., the generated sample draws, in the context of Monte Carlo simulation) to a sample that satisfies regularity conditions. For our CES-translog form, we define a vector for the parameters to be estimated, $\beta =$ $[ \alpha , \rho , \delta _ { z } , \delta _ { k } , \beta _ { z } , \beta _ { k } , \hat { \beta _ { l } } , \hat { \beta _ { z k } } , \beta _ { z l } , \beta _ { k l } , \beta _ { z z } , \beta _ { k k } , \beta _ { l l } ] ^ { T }$ The objective in the Bayesian estimation method is to properly form the posterior probability distribution function, $g ( \beta \mid D )$ , from the observed data D—our measures of value added and inputs.

Bayes’ Theorem relates the posterior probability to the prior probability,

$$
g (\boldsymbol {\beta} \mid D) \propto L (\boldsymbol {\beta} \mid D) \times p (\boldsymbol {\beta}),
$$

where $L ( \beta | D )$ is the likelihood function of the vector of the model parameters $\beta$ given the observed data $D ,$ and $p ( \beta )$ is the prior density function of $\beta .$

We take the error term in (5), , to be multivariate normal, with mean 0 and variance-covariance $\sigma ^ { 2 } I _ { \ O }$ where $\sigma$ is unknown. If we had no prior knowledge about the parameters, we would have used the noninformative prior. However, in our case, the parameters have to satisfy the regularity conditions, so we use an informative prior to incorporate these conditions. We follow Coelli et al. (2005) and propose a joint informative prior for $( \beta , \sigma )$

$$
g (\beta , \sigma) \propto \frac {I (\beta)}{\sigma},
$$

where $I ( \beta )$ is an indicator function that takes the value 1 if $\beta$ satisfies the conditions and takes the value 0 otherwise.

The CES-translog form does not have a clear form for the posterior probability density function (pdf) for the parameters. Following Dewan and Min (1997), we assume the posterior is an asymptotic multivariate normal distribution with the mean being the estimates from the least-squares approach and with the variance-covariance matrix being a diagonal matrix with the variances of the estimators from the leastsquares approach on the diagonals. After imposing regularity conditions, the posterior is actually a truncated asymptotic multivariate normal distribution because the indicator function forces the posterior pdf to be zero if the parameters fail to satisfy the regularity conditions.

Implementation. We use Monte Carlo simulation to implement our Bayesian approach. We randomly draw 10,000 times from a multivariate normal distribution for our CES-translog form. For each draw, we check the regularity conditions for each observation. We accept draws with regularity conditions satisfied for at least 70% of the entire data set. A threshold of 70% is chosen to ensure a reasonable level of acceptance rate. Setting the threshold at 100% results in zero accepted draws. With the threshold set at 70%, the acceptance rate for our data set is 45.22%. We take the mean and standard error of the accepted draws as the corresponding statistics for the parameter estimates. Figure 2 provides a flowchart showing the process by which we impose regularity conditions in our estimation.

## 4. Results

In Table 2 we report our parameter estimates for the CES-translog production functions with both the nonlinear least-squares approach and the Bayesian approach. We also provide our estimates for the Cobb–Douglas production function to validate the quality of our data set. The Cobb–Douglas estimates are consistent with those from the previous literature. For example, our IT capital coefficient is estimated at

Figure 2 (Color online) Bayesian Estimation Flowchart  
![](/api/attachments/U3QC3TJP/fulltext/images/c62f7d1580a67b98040aca9b4d228bc4bc5f2a205b962321334cd28806e49ab0.jpg)

Table 2 Parameter Estimates

<table><tr><td></td><td>Cobb-Douglas</td><td>CES-translog least-squares approach</td><td>Imposing regularity Bayesian approach</td></tr><tr><td> $\rho$ </td><td></td><td>0.699***(0.091)</td><td>0.692***(0.091)</td></tr><tr><td>IT</td><td>0.047***(0.021)</td><td>0.580***(0.052)</td><td>0.582***(0.051)</td></tr><tr><td>K</td><td>0.359***(0.031)</td><td>0.050(0.044)</td><td>0.050(0.043)</td></tr><tr><td>L</td><td>0.586**(0.029)</td><td>0.369***(0.036)</td><td>0.368***(0.036)</td></tr><tr><td> $IT \times IT$ </td><td></td><td>0.023(0.014)</td><td>0.031***(0.011)</td></tr><tr><td> $IT \times K$ </td><td></td><td>0.000(0.017)</td><td>0.008(0.015)</td></tr><tr><td> $IT \times L$ </td><td></td><td>-0.091***(0.018)</td><td>-0.085***(0.017)</td></tr><tr><td> $K \times K$ </td><td></td><td>0.039***(0.007)</td><td>0.040***(0.006)</td></tr><tr><td> $K \times L$ </td><td></td><td>-0.076***(0.016)</td><td>-0.074***(0.015)</td></tr><tr><td> $L \times L$ </td><td></td><td>0.110***(0.011)</td><td>0.111***(0.011)</td></tr><tr><td>N</td><td>708</td><td>708</td><td>708</td></tr><tr><td>Industries</td><td>59</td><td>59</td><td>59</td></tr><tr><td>Controls</td><td>Group, year</td><td>Group, year</td><td>N/A</td></tr></table>

Notes. IT, IT capital; K, non-IT capital; L, labor. Standard errors are in parentheses. Dummy variables are suppressed for brevity.  
<sup>∗∗</sup>Significant at the 5% level; <sup>∗∗∗</sup>significant at the 1% level.

0.047. This is comparable with Chwelos et al. (2010), who estimate the IT coefficient at 0.0636. Our coefficient estimates for non-IT capital and labor are also consistent with the economic conjecture of capital and labor being roughly one-third and two-thirds of the contribution (and total input share), respectively.

Our results of the AES and MES are based on their definitions using our CES-translog estimates as the FFF of the production function (see (1) and (2) for AES and MES definitions, respectively, and the appendix for the calculation of the elements in the equations). We use the estimated parameters to calculate the ESs in the following steps. First, we calculate the ESs for each observation (industry, year) in the data set. Second, we calculate the mean ESs for each industry across different years. Third, the industry-group-level ESs are aggregated as the weighted average of the industry-level ESs measures. The weight is the total value added for each industry.

Then, we develop a bootstrap procedure in Stata to estimate the standard errors of the industry-grouplevel ESs. Specifically, because our goal is to estimate the standard errors at the industry-group level, we bootstrap the observed ESs and resample (with replacement) within each industry-group panel. The bootstrap resampling is repeated 200 times. In each repetition, the industry-group ESs are calculated following the above steps. Our final estimates of the standard errors for the industry-group ESs are based on the 200 bootstrapped industry-group ESs. The AES and MES between IT capital and non-IT capital or labor are reported in Table 3. The AES and MES between non-IT capital and labor are reported in Table 4. In both tables, Panel A contains the AES and MES based on the nonlinear least-squares estimates, and Panel B contains the AES and MES based on the Bayesian estimates.

## 4.1. Comparison of ES Estimates Based on Least-Squares and Bayesian Approaches: The Impact of Imposing Regularity Conditions on ES Estimates

Compared with the ES estimates based on the leastsquares approach (Panel A of Tables 3 and 4), the ES estimates based on the Bayesian approach (Panel B of Tables 3 and 4) are remarkably consistent across different industries. Consider the MES between IT capital and non-IT capital $( \sigma _ { z k } ^ { M } )$ as an example. The MES from the Bayesian approach ranges from 1.12 for the industry group mining to 1.26 for the industry group accommodation, food services, and drinking places, with the average economy-wide estimate being 1.19. This narrow range is in sharp contrast to the same estimate from the nonlinear least-squares approach ranging from 0.24 for the industry group mining to 1.57 for the industry group professional services. The consistency across industries conveniently allows us to draw inferences that apply both economy-wide and across industries.

Table 3 Elasticity of Substitution Estimates Between IT and Non-IT or Labor

<table><tr><td>Industry group</td><td>NAICS(Number of industries)</td><td>AES_IT_K( $\sigma_{zk}^{A}$ )</td><td>MES_IT_K( $\sigma_{zk}^{M}$ )</td><td>MES_K_IT( $\sigma_{kz}^{M}$ )</td><td>AES_IT_L( $\sigma_{zl}^{A}$ )</td><td>MES_IT_L( $\sigma_{zl}^{M}$ )</td><td>MES_L_IT( $\sigma_{lz}^{M}$ )</td></tr><tr><td colspan="8">Panel A: Before imposing regularity (monotonicity) conditions, least-squares approach</td></tr><tr><td>Manufacturing</td><td>31–33 (18)</td><td>0.73</td><td>1.21***</td><td>0.25</td><td>0.09</td><td>0.61</td><td>0.25</td></tr><tr><td>Transp., comm., and public utilities</td><td>22, 48, 49 (9)</td><td>1.31**</td><td>1.56***, +</td><td>1.23***</td><td>2.05</td><td>1.89**</td><td>1.46***</td></tr><tr><td>Wholesale trade</td><td>42 (1)</td><td>0.84</td><td>1.30***</td><td>-0.09</td><td>-0.45</td><td>0.14</td><td>-0.05</td></tr><tr><td>Retail trade</td><td>44, 45 (1)</td><td>0.95***</td><td>1.34***, +++</td><td>0.37***, +++</td><td>0.05</td><td>0.50***, +++</td><td>0.32***, +++</td></tr><tr><td>Accommod., food serv., and drinking places</td><td>72 (2)</td><td>0.96***</td><td>1.41***, +++</td><td>0.74***, +++</td><td>0.52***</td><td>0.88***, +++</td><td>0.65***, +++</td></tr><tr><td>Fire</td><td>52, 53 (6)</td><td>1.09***</td><td>1.33***, +++</td><td>0.57</td><td>0.10</td><td>0.72***</td><td>0.54</td></tr><tr><td>Entertainment</td><td>51, 71 (6)</td><td>1.32***</td><td>1.49***, +++</td><td>0.61***, +++</td><td>0.15**</td><td>0.73***, +++</td><td>0.66***, ++</td></tr><tr><td>Professional services</td><td>54, 56, 81 (7)</td><td>1.38***</td><td>1.57***, +++</td><td>1.04**</td><td>0.91**</td><td>1.07***</td><td>1.02***</td></tr><tr><td>Educational serv., health care, and soc. assist.</td><td>61, 62 (4)</td><td>1.24***</td><td>1.49***, +++</td><td>0.98***</td><td>0.84***</td><td>1.06***</td><td>0.96***</td></tr><tr><td>Forestry</td><td>11 (1)</td><td>0.99***</td><td>1.38***, +++</td><td>0.63***, +++</td><td>0.31***</td><td>0.74***, +++</td><td>0.52***, +++</td></tr><tr><td>Mining</td><td>21 (3)</td><td>-0.77***</td><td>0.24**, +++</td><td>0.42***, +++</td><td>4.00***</td><td>3.08***, +++</td><td>0.51***, +++</td></tr><tr><td>Construction</td><td>23 (1)</td><td>0.89***</td><td>1.44***, +++</td><td>0.29***, +++</td><td>0.06</td><td>0.43***, +++</td><td>0.25***, +++</td></tr><tr><td>Economy-wide</td><td>all above (59)</td><td>1.04***</td><td>1.37***, +++</td><td>0.60***, +</td><td>0.46</td><td>0.84***</td><td>0.60***, ++</td></tr><tr><td colspan="8">Panel B: After imposing regularity (monotonicity) conditions, Bayesian approach</td></tr><tr><td>Manufacturing</td><td>31–33 (18)</td><td>0.90***</td><td>1.19***, +++</td><td>0.85***, +++</td><td>0.81***</td><td>1.05***, +++</td><td>0.83***, +++</td></tr><tr><td>Transp., comm., and public utilities</td><td>22, 48, 49 (9)</td><td>0.84***</td><td>1.15***, +++</td><td>0.91***, +++</td><td>1.15***</td><td>1.33***, +++</td><td>0.97***</td></tr><tr><td>Wholesale trade</td><td>42 (1)</td><td>0.89***</td><td>1.19***, +++</td><td>0.80***, +++</td><td>0.72***</td><td>0.93***, +++</td><td>0.77***, +++</td></tr><tr><td>Retail trade</td><td>44, 45 (1)</td><td>0.95***</td><td>1.21***, +++</td><td>0.81***, +++</td><td>0.66***</td><td>0.88***, +++</td><td>0.74***, +++</td></tr><tr><td>Accommod., food serv., and drinking places</td><td>72 (2)</td><td>0.95***</td><td>1.26***, +++</td><td>0.87***, +++</td><td>0.75***</td><td>1.00***</td><td>0.81***, +++</td></tr><tr><td>Fire</td><td>52, 53 (6)</td><td>0.91***</td><td>1.16***, +++</td><td>0.85***, +++</td><td>0.75***</td><td>1.02***</td><td>0.81***, +++</td></tr><tr><td>Entertainment</td><td>51, 71 (6)</td><td>0.80***</td><td>1.15***, +++</td><td>0.96***, +</td><td>1.18***</td><td>1.30***, +++</td><td>1.02***</td></tr><tr><td>Professional services</td><td>54, 56, 81 (7)</td><td>0.85***</td><td>1.23***, +++</td><td>0.82***, +++</td><td>0.79***</td><td>0.97***, +++</td><td>0.80***, +++</td></tr><tr><td>Educational serv., health care, and soc. assist.</td><td>61, 62 (4)</td><td>0.85***</td><td>1.22***, +++</td><td>0.84***, +++</td><td>0.82***</td><td>1.01***</td><td>0.83***, +++</td></tr><tr><td>Forestry</td><td>11 (1)</td><td>0.97***</td><td>1.25***, +++</td><td>0.82***, +++</td><td>0.63***</td><td>0.92***, +++</td><td>0.73***, +++</td></tr><tr><td>Mining</td><td>21 (3)</td><td>0.80***</td><td>1.12***, +++</td><td>0.94***, +++</td><td>1.42***</td><td>1.74***, +++</td><td>1.08***, +++</td></tr><tr><td>Construction</td><td>23 (1)</td><td>0.92***</td><td>1.25***, +++</td><td>0.79***, +++</td><td>0.68***</td><td>0.88***, +++</td><td>0.74***, +++</td></tr><tr><td>Economy-wide</td><td>all above (59)</td><td>0.88***</td><td>1.19***, +++</td><td>0.85***, +++</td><td>0.82***</td><td>1.04***, +++</td><td>0.83***, +++</td></tr></table>

Notes. IT, IT capital; K, non-IT capital; L, labor.  
<sup>∗∗</sup>Significant at 5%; <sup>∗∗∗</sup>significant at 1%.  
<sup>+</sup>Significant from 1 at 10%; <sup>++</sup>significant from 1 at 5%; <sup>+++</sup>significant from 1 at 1%.

It is worth noting that imposing monotonicity conditions works by removing observations that do not satisfy monotonicity. To the extent that those observations are outliers (or due to data error), there are likely to be dampening effects on the standard error. It is possible that removing observations that do not satisfy monotonicity change the CES-translog parameters and consequently the ES estimates, but there is no systematic direction of the effect on the ESs. We also examined the standard errors from our bootstrapping process, comparing the standard errors when monotonicity is imposed and when it is not. What we found is that the standard errors are smaller when monotonicity is imposed, but this could be due to the estimation method, Bayesian versus least squares, rather than the observations that are removed.

As mentioned before, it is important to impose regularity conditions, especially monotonicity conditions, when estimating elasticities. Therefore, unless specified otherwise, below we focus on discussing the ES estimates from the Bayesian approach.

As much of the interpretation of ESs involves quantities, we restate that in our study, and most productivity studies, the quantity of IT capital is the stock of IT capital in real dollars. It can be converted into a flow through the rental price methodology, but that does not often yield different results because the stock of IT capital is used to derive the rental price. When IT capital is converted to real dollars from nominal dollars, the prior years’ vintages are deflated by the price deflator. This price is based on market prices that in turn reflect some function of IT performance.

Table 4 Elasticity of Substitution Estimates Between Non-IT and Labor

<table><tr><td>Industry group</td><td>NAICS (Number of industries)</td><td>AES_K_L ( $\sigma_{kl}^{A}$ )</td><td>MES_K_L ( $\sigma_{kl}^{M}$ )</td><td>MES_L_K ( $\sigma_{lk}^{M}$ )</td></tr><tr><td colspan="5">Panel A: Before imposing regularity (monotonicity) conditions, least-squares approach</td></tr><tr><td>Manufacturing</td><td>31–33 (18)</td><td>1.60***</td><td>1.56***,+++</td><td>1.56***,+++</td></tr><tr><td>Transportation, communications, and public utilities</td><td>22, 48, 49 (9)</td><td>2.15***</td><td>2.23***,++</td><td>1.99***,+++</td></tr><tr><td>Wholesale trade</td><td>42 (1)</td><td>1.47***</td><td>1.53***,+++</td><td>1.49***,+++</td></tr><tr><td>Retail trade</td><td>44, 45 (1)</td><td>1.56***</td><td>1.47***,+++</td><td>1.52***,+++</td></tr><tr><td>Accommodation, food services, and drinking places</td><td>72 (2)</td><td>1.83***</td><td>1.56***,+++</td><td>1.64***,+++</td></tr><tr><td>Fire</td><td>52, 53 (6)</td><td>1.52***</td><td>1.48***,+++</td><td>1.50***,+++</td></tr><tr><td>Entertainment</td><td>51, 71 (6)</td><td>1.61***</td><td>1.61***,+++</td><td>1.56***,+++</td></tr><tr><td>Professional services</td><td>54, 56, 81 (7)</td><td>1.69***</td><td>1.60***,+++</td><td>1.62***,+++</td></tr><tr><td>Educational services, health care, and social assistance</td><td>61, 62 (4)</td><td>1.67***</td><td>1.58***,+++</td><td>1.60***,+++</td></tr><tr><td>Forestry</td><td>11 (1)</td><td>1.71***</td><td>1.49***,+++</td><td>1.60***,+++</td></tr><tr><td>Mining</td><td>21 (3)</td><td>2.89***</td><td>2.91***,+++</td><td>2.81***,+++</td></tr><tr><td>Construction</td><td>23 (1)</td><td>1.66***</td><td>1.58***,+++</td><td>1.62***,+++</td></tr><tr><td>Economy-wide</td><td>all above (59)</td><td>1.66***</td><td>1.61***,+++</td><td>1.61***,+++</td></tr><tr><td colspan="5">Panel B: After imposing regularity (monotonicity) conditions, Bayesian approach</td></tr><tr><td>Manufacturing</td><td>31–33 (18)</td><td>1.55***</td><td>1.38***,+++</td><td>1.41***,+++</td></tr><tr><td>Transportation, communications, and public utilities</td><td>22, 48, 49 (9)</td><td>1.70***</td><td>1.57***,+++</td><td>1.51***,+++</td></tr><tr><td>Wholesale trade</td><td>42 (1)</td><td>1.44***</td><td>1.31***,+++</td><td>1.34***,+++</td></tr><tr><td>Retail trade</td><td>44, 45 (1)</td><td>1.50***</td><td>1.29***,+++</td><td>1.36***,+++</td></tr><tr><td>Accommodation, food services, and drinking places</td><td>72 (2)</td><td>1.69***</td><td>1.38***,+++</td><td>1.45***,+++</td></tr><tr><td>Fire</td><td>52, 53 (6)</td><td>1.51***</td><td>1.34***,+++</td><td>1.38***,+++</td></tr><tr><td>Entertainment</td><td>51, 71 (6)</td><td>1.60***</td><td>1.49***,+++</td><td>1.43***,+++</td></tr><tr><td>Professional services</td><td>54, 56, 81 (7)</td><td>1.54***</td><td>1.37***,+++</td><td>1.39***,+++</td></tr><tr><td>Educational services, health care, and social assistance</td><td>61, 62 (4)</td><td>1.55***</td><td>1.38***,+++</td><td>1.40***,+++</td></tr><tr><td>Forestry</td><td>11 (1)</td><td>1.63***</td><td>1.34***,+++</td><td>1.44***,+++</td></tr><tr><td>Mining</td><td>21 (3)</td><td>2.06***</td><td>1.92***,+++</td><td>1.78***,+++</td></tr><tr><td>Construction</td><td>23 (1)</td><td>1.53***</td><td>1.33***,+++</td><td>1.39***,+++</td></tr><tr><td>Economy-wide</td><td>all above (59)</td><td>1.55***</td><td>1.38***,+++</td><td>1.40***,+++</td></tr></table>

Notes. K, Non-IT capital; L, labor.  
<sup>∗∗∗</sup>Significant at 1%.  
<sup>++</sup>Significant from 1 at 5%; <sup>+++</sup>significant from 1 at 1%.

## 4.2. AES Estimates

Panel B of Tables 3 and 4 shows that the AESs are significant and positive for all industry groups and for the economy-wide average. This indicates that each pair of inputs are substitutes in the Allen sense. Thus, if the price of any input increases, there is a corresponding increase in the quantity of each of the other inputs.

In Table 5 we show a comparison of the AES estimates between our findings and those of previous IT substitutability studies, noting that the study by Chun and Mun (2006) is not comparable because they estimate a cost function and use gross product originating rather than value added, and, consequently, intermediate inputs are part of their analysis. Our AES results are consistent with previous findings of Dewan and Min (1997) and Hitt and Snir (1999). Our results are also consistent with the findings of Chwelos et al. (2010) except for the AES between IT capital and non-IT capital, where they found that IT capital and non-IT capital are complements.

Table 5 A Comparison of Our AES Results and Previous IT Substitution Studies

<table><tr><td>Study</td><td>Data year</td><td>AES_IT_K $(\sigma_{zk}^{A})$ </td><td>AES_IT_L $(\sigma_{zl}^{A})$ </td><td>AES_K_L $(\sigma_{kl}^{A})$ </td></tr><tr><td>Dewan and Min (1997)</td><td>1988–1992: Firms CES-translog</td><td>1.006</td><td>1.063</td><td>1.005</td></tr><tr><td>Hitt and Snir (1999)</td><td>1987–1994: Firms Translog</td><td>0.945</td><td>0.688</td><td>NA</td></tr><tr><td>Chwelos et al. (2010)</td><td>1987–1999: Firms CES-translog</td><td>-3.406</td><td>3.012</td><td>2.244</td></tr><tr><td rowspan="2">Our study</td><td>1998–2009: Industries CES-translog; least-squares</td><td>1.04</td><td>0.46</td><td>1.66</td></tr><tr><td>1998–2009: Industries CES-translog; Bayesian</td><td>0.88</td><td>0.82</td><td>1.55</td></tr></table>

Notes. IT, IT capital; K, non-IT capital; L, labor.

## 4.3. MES Estimates

In interpreting the results of our MES estimation, it is helpful to review substitutability and complementarity in the Morishima sense. Consider the relationship between IT capital and non-IT capital. The MES in the case of a change in the price of IT capital is $\sigma _ { k z } ^ { M }$ . If $\sigma _ { k z } ^ { M } < 0 .$ , then IT capital and non-IT capital are complements. The result of a decrease in the price of IT capital is to increase not only the quantities of IT and non-IT capital but also to increase the ratio of the quantity of non-IT capital to IT capital, $x _ { k } / x _ { z }$ (see (4)). Moreover, this also increases the ratio of the input share of non-IT capital to IT capital, $p _ { k } x _ { k } / ( p _ { z } x _ { z } )$ .

The more common case, and the case with all of our results, is when the MES is positive and the inputs are substitutes. We show the effects of MES substitutes in Figure $^ { 3 , }$ where we explain it as a two-step sequence. In the first step, the effect of a decrease in the price of IT capital is to increase the quantity of IT capital due to its own price elasticity and to decrease the quantity ratio of non-IT capital to IT capital, $x _ { k } / x _ { z } .$ . Here quantities mean the real dollar value of the IT capital and non-IT capital stock, and in our data in 2005 dollars. Notice this does not necessarily imply that the quantity of non-IT capital falls, but rather that $x _ { z }$ increases by a larger percentage than $x _ { k } .$ . In this way, the MES substitutes—here IT capital and non-IT capital—can both have increases in quantity as a consequence of a decrease in price of one of the inputs. This situation with both quantities increasing is essentially what Chwelos et al. (2010) found with IT capital and non-IT capital as AES complements in their post-Internet period.

In addition to the above interpretation of the quantity ratio, in the second step, the MES also tells us how the ratio of input shares changes in response to a price change by comparing the MES with unity (see (3)). If $\sigma _ { k z } ^ { M } < 1$ , then the result of a decrease in the price of IT capital, $p _ { z } ,$ , is to increase the quantity of IT capital, $x _ { z } ,$ and also to increase the ratio of input share of non-IT capital to IT capital, $p _ { k } x _ { k } / ( p _ { z } x _ { z } )$ . Thus, in post-IT capital price change dollar terms, the IT capital input share is lower relative to that of non-IT capital, and this occurs because the ratio of quantities, $x _ { k } / x _ { z } ,$ falls less than the price of IT capital. However, if $\sigma _ { k z } ^ { M } > 1 .$ then a price decrease in IT capital decreases the ratio of input shares of non-IT capital to IT capital because the ratio of quantities falls more than the price of IT capital—a more common interpretation of substitution and typically the case when IT capital has a high own price elasticity.

Figure 3 Interpreting MES Substitution

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Interpreting MES Substitution:  $\sigma_{kz}^{M} &gt; 0$ 

Price of IT capital:  $p_{z}$  (set to 1 initially)

Price of non-IT capital:  $p_{k} = 1$  (numeraire)

Real dollar value of IT capital (quantity):  $x_{z}$ 

Real dollar value of non-IT capital (quantity):  $x_{k}$ 

Ratio of input share of non-IT capital to IT capital:  $p_{k}x_{k}/(p_{z}x_{z})$ 

Step 1:  $p_{z} \downarrow \Rightarrow x_{z} \uparrow$  (own price elasticity)

 $\Rightarrow x_{k}/x_{z} \downarrow \Rightarrow \% \Delta x_{k} &lt; \% \Delta x_{z}$ 

Step 2: If  $\sigma_{kz}^{M} &lt; 1 \Rightarrow p_{k}x_{k}/(p_{z}x_{z}) \uparrow \Rightarrow x_{k}/x_{z}$  falls less than  $p_{z}$ 

If  $\sigma_{kz}^{M} &gt; 1 \Rightarrow p_{k}x_{k}/(p_{z}x_{z}) \downarrow \Rightarrow x_{k}/x_{z}$  falls more than  $p_{z}$
</div>

From Panel B of Tables 3 and $^ { 4 , }$ we can see that all MES estimates are significant and positive, meaning that each pair of inputs are substitutes in the Morishima sense. That is to say, if the price of any particular input increases, then there is a corresponding increase in the quantity ratio of each of the other inputs to that particular input.

Panel B of Tables 3 and 4 also shows the significance from unity for each of the MES estimates (marked by $^ { \prime \prime } + + \stackrel { \cdot } { + } , ^ { \prime \prime } ^ { \prime \prime } + + , ^ { \prime \prime }$ and $" + "$ for 1%, 5%, and 10% significance levels, respectively). Most of the MES estimates are significantly different from unity, with a few exceptions on those of IT capital and labor. However, the economy-wide averages are all significantly different from unity.<sup>3</sup>

4.3.1. MES Results When the Price of IT is Changing. Begin by examining the MESs in Panel B of Table 3, $\sigma _ { k z } ^ { M }$ and $\sigma _ { l z } ^ { M }$ . Over the time period of our data set, the price of IT capital has been decreasing, which, for normal inputs, implies the quantity of IT capital, $x _ { z } ,$ has been increasing. For all 12 industries and economy-wide, we find that $0 < \sigma _ { k z } ^ { M } < 1$ . Thus, IT capital and non-IT capital are substitutes in the Morishima sense, and the ratio of their quantities, $x _ { k } / x _ { z } ,$ is decreasing. It is not possible to determine whether the quantity of non-IT capital, $x _ { k } ,$ is increasing or decreasing. However, even though IT capital and non-IT capital are substitutes in the Morishima sense, we also find that the ratio of the input share of non-IT capital to the input share of IT capital is increasing—meaning that $p _ { k } x _ { k } / p _ { z } x _ { z }$ is increasing. Consequently, the fall in price of IT capital, noting that the price of non-IT capital is constant for the purposes of interpreting $\sigma _ { k z } ^ { \bar { M } } ,$ outweighs the changes in the relative quantities of IT and non-IT capital. As such, this shows that substitution in the Morishima sense is less elastic when the MES is less than unity.

We also find that for nine of the 12 industries, and economy-wide, $0 < \sigma _ { l z } ^ { M } < 1$ Thus, the relationship between IT capital and labor is similar to that between IT and non-IT capital when the price of IT capital changes (falls)—substitution in the Morishima sense is less elastic. We attribute this to the special characteristics of IT as an input to production that we discussed in §1: IT enables complementary technological and organizational innovations, and enhances the efficiency of labor and non-IT capital through indirect effects and various types of spillovers.

In summary, our MES results show that the real input share of IT capital is stable or slightly shrinking in response to a decline in the price of IT capital, at least over the period covered by our data set. This conclusion regarding input shares of IT capital is consistent with observations from the U.S. Bureau of Labor Statistics (2006, p. 7): “Computers have seemingly accounted for a steady increasing proportion of investment in equipment. In terms of current 4read2 real5 dollar investment, however, computer and computer peripherals have maintained a constant share of current dollar investment in equipment. 0 0 0 The increasing prevalence of computers and its constant share of equipment investment may be due to the fact that computers have also embodied rapidly changing technology and have exhibited unprecedented declines in price.”

4.3.2. MES Results When the Price of Non-IT Capital is Changing. Now consider the MESs between IT capital and non-IT capital in Panel B of Table 3, $\sigma _ { z k } ^ { M } ,$ , and between labor and non-IT capital in Table 4, $\sigma _ { l k } ^ { \mathbf { \tilde { M } } }$ . For the most part, over the time period of our data set the prices of non-IT capital have been increasing, which, for normal inputs and absent any effects from other input prices, implies that the quantity of non-IT capital, $x _ { k } ,$ has been decreasing. For all 12 industries and economy-wide, we find that $1 \prec$ $\sigma _ { z k } ^ { M } , \sigma _ { l k } ^ { M } .$ , so that non-IT capital is a substitute in the Morishima sense for both IT capital and labor. Thus, an increase in the price of non-IT capital increases the quantity of IT capital relative to non-IT capital, $x _ { z } / x _ { k } ,$ and the quantity of labor relative to non-IT capital, $x _ { l } / x _ { k }$ . In addition, because these MESs are greater than unity, the relative input share of IT capital to non-IT capital, $p _ { z } x _ { z } / p _ { k } x _ { k } ,$ and the relative input share of labor to non-IT capital, $p _ { l } x _ { l } / p _ { k } x _ { k } ,$ also increase. These relative input share increases are only possible when the quantities of IT capital and labor relative to non-IT capital increase more than the price of non-IT capital, showing that substitution in the Morishima sense is more elastic when the MES is greater than unity.

4.3.3. MES Results When the Price of Labor is Changing. Now consider the MESs between IT capital and labor in Panel B of Table 3, $\sigma _ { z l } ^ { M }$ , and between non-IT capital and labor in Table $4 , \ \sigma _ { k l } ^ { M } .$ . In general, over the time period of our data set the price of labor has been increasing, which, as described above for normal inputs and absent any effects from other input prices, implies that the quantity of labor, $x _ { l } ,$ has been decreasing. First, examine the MESs for IT capital and labor. Across industries and economy-wide, $0 < \sigma _ { z l } ^ { M } .$ , so that IT capital is a substitute for labor when the price of labor changes and the relative quantity of IT capital to labor, $x _ { z } / x _ { l } ,$ increases. However, some industries have $0 < \sigma _ { z l } ^ { M } < 1$ , and for some (and economy-wide), $1 < \sigma _ { z l } ^ { M }$ . Thus, for the former set of industries, substitution in the Morishima sense is less elastic, whereby the relative input share of IT capital to labor is lower, and in the latter set, substitution in the Morishima sense is more elastic, whereby the relative input share of IT capital to labor is higher.

Second, examine the MESs for non-IT capital and labor. Here we find across industries and economywide that $1 < \sigma _ { k l } ^ { M }$ . Thus, non-IT capital is a substitute for labor when the price of labor changes and the relative quantity of IT capital to labor, $x _ { k } / x _ { l } ,$ increases. In addition, substitution in the Morishima sense is more elastic, whereby the relative input share of non-IT capital to labor is higher.

Finally, consider the response of IT capital to changes in the price of non-IT capital versus labor. The value of $\sigma _ { z k } ^ { M }$ is always greater than unity, and $\sigma _ { z l } ^ { M }$ is around unity and is less than $\sigma _ { z k } ^ { M }$ in 10 of the 12 industries. What this means is if the prices of non-IT capital and labor change by the same percentage, then the quantity and input share of IT capital relative to non-IT capital changes more than it does relative to labor. In other words, the relative quantity and input share of IT capital is more elastic in response to a change in the price of non-IT capital than it is to the price of labor.

## 5. Contributions, Limitations, and Opportunities for Future Research Opportunities for

We make three main contributions in this commentary. First, we introduce the MES, which does not suffer from the drawbacks of the more heavily used AES. The key advantages are that the MES differs depending on which input price is changing, it represents changes in the relative quantities of inputs, the scale is meaningful in that a larger MES represents a greater degree of elasticity, and, depending on whether the MES is greater than unity, it can determine the changes in relative input shares. These latter two advantages allow for a comparison of price versus quantity effects. These advantages are particularly important for IT research in that, in contrast to other inputs, the price of IT has been falling over a substantial period, and the relationships of IT with other capital and labor are richer than the relationships between other inputs. Consequently, the MES allows us to measure the impact of changes in the price of IT capital on relative quantities and input shares differently than the impact of changes in other input prices on IT capital, while giving meaning to less versus more elastic.

Second, we introduce the idea of imposing regularity conditions locally. In much theory-based empirical research, the estimation model has underlying assumptions that are necessary to interpret the parameter estimates as elements of the focal theory. These underlying assumptions are what we call regularity conditions, and even imposing the most basic of these regularity conditions can improve the stability and validity of the estimates.

Third, we execute a state-of-the-art analysis to estimate MESs—which is substantial. We also demonstrate how to impose regularity conditions and show how imposing regularity improves the stability of the estimates of our different elasticities. Finally, our MES results clearly display how its flexibility allows for insights about the relationship between IT and other inputs. For the most part, our MES results show that substitution between IT and other inputs is less elastic when the price of IT changes, and more elastic when the prices of other inputs change. These results support the reasoning that as IT becomes less expensive and more IT is used, IT displaces less non-IT capital and labor than is the case when the price of another input increases and more IT is used. This latter point is evidenced from our analysis: a drop in the price of IT capital and an increase in the price of non-IT capital has the same increasing effect on the quantity ratio of IT capital to non-IT capital. However, these two opposite price changes on IT capital and non-IT capital have opposing effects on the relative input share of IT capital to non-IT capital.

The first two contributions are important because they highlight the advantages of an underrecognized measure, issues with the more heavily used measure in the literature, and a methodology that can improve stability of empirical estimates. They also provide measures and methods along with more refined interpretations that can provide more insight and can be readily used in future research. Our third contribution serves as part of the Research Commentary as we demonstrate how to implement the measure and methods and interpret the results. This third contribution also serves as a regular research contribution by adding novel results to the literature on the substitution of IT for other inputs, and more broadly to the literature on the relationship of IT to other inputs when determining the value of IT.

There are some limitations to what can be learned from our analyses that are endemic to any ES-type analysis. One is that we do not separate out switching or substitution costs between inputs. When firms make decisions about switching between inputs, for example, IT capital for labor, they weigh the switching costs versus the benefit of taking advantage of price changes. These costs are implicitly embedded in the data we use. Similarly, our analyses do not model how quickly firms can substitute one input for another except that they can do so in the time period covered by our observations; for example, with annual data, this would be a year.

## 5.1. Implications for Future Research

Our analysis has implications for future research in the substitution of IT for other inputs and will benefit future researchers in a range of other work. This is not only because the MES is a better measure than the AES, and that imposing regularity locally improves estimation but also because IT is an input with special characteristics. First, MESs can be compared between different subclasses of firms or industries. Consequently, it is possible to see if, for example, the change in the input share balance between two inputs, such as IT capital and labor, is more elastic in one industry or the other. As we saw above, this is not the case with the AES despite work that has made inferences from AESs of different magnitudes. Indeed, based on industry MESs, we make such comparisons in §4. This makes possible some important opportunities for future research.

Second is understanding the resulting changes in input shares that come from the behavior of IT prices. Roughly following Moore’s law, the price of IT capital has been consistently falling over time. For example, see Nordhaus (2002) and Berndt and Rappaport (2002). The continuous improvements in the price/ performance ratio of IT and the empirical evidence of a significant IT impact on productivity continue to motivate increased investment in IT. What we do not know is whether this increased investment in IT exceeds the decline in value of prior vintages of IT capital such that, as an input, IT capital commands a growing or shrinking input share over time. In contrast to the work using the AES, our results suggest that in response to decreases in the price of IT capital, the IT capital input share is stable or even slightly shrinking, and this is definitely an area for future work. Indeed, our results about IT capital input shares being stable or shrinking because of the price declines in IT over time invites a different response to Robert Solow’s (1987, p. 36) famous comment “You can see the computer age everywhere but in the productivity statistics”: computers are everywhere because of price declines, but these same price declines keep the real input share of IT capital roughly the same.

Finally, unlike most other factors of production, IT implementations have multiple effects on the production process. Brynjolfsson and Hitt (2000) argue that IT is a general-purpose technology that facilitates complementary technological or organizational innovations that eventually cause dramatic productivity improvements. Farrell (2003) argues that IT increases output because it enhances the efficiency of labor and asset utilization. Supporting these arguments about IT capital being an input that has broader effects, IT has been shown to contribute to organizational capital (Brynjolfsson and Hitt 2003), to indirect effects enhancing the efficiency of non-IT capital and labor (Mittal and Nault 2009), to interorganizational spillovers both up and down the supply chain (Cheng and Nault 2007, 2012), and to knowledge spillovers (Tambe and Hitt 2014). To better understand these different effects, MESs can be compared between different inputs. This opens up the potential of comparing different subclasses of IT capital or even IT capital and IT operating expenses, together with non-IT capital and labor. This allows access to a deeper understanding about how IT combines with other inputs to create value.

An important future research opportunity comparing MESs between different inputs is the evolution of IT outsourcing. IT outsourcing was prevalent from 1998 to 2009. This transformation of IT capital to operating expense reduces the amount of IT capital we measure, but also reduces value added—the dependent variable in our production function estimation. Consequently, there is no observation we can make in our analyses that addresses this type of substitution. To do this within the analyses we propose would require separating the IT operating expense from the rest of the intermediate inputs and then examining the substitution between IT capital and IT operating expenses. Furthermore, it is possible to separate the different categories of IT capital, such as computers, software, and telecommunications. An interesting future research opportunity is to examine the substitution between these different categories of IT capital as well as IT operating expenses.

More generally, a wide array of future research in IS has the potential to be informed by our analysis: research in IT productivity, IT substitution, IT cost–benefit analyses, and, more broadly, the impact of IT implementations at all levels. In our view, the MES/regularity advances we are reporting are compelling, because the currently favored AES is misleading; they are insightful, because the alternative MES is more informative; and they are actionable in that whenever the AES can be computed the MES can be computed as well based on the same production or cost function estimates.

## 6. Conclusion

Our analysis and prior research has shown that the MES provides a substitution measure where the scale is meaningful, and the measure differs depending on which price is changing. This is in contrast to the AES, which is misleading when there are three or more inputs. Given that the calculation of the MES follows the same process as that of the AES, we conclude that the MES should be used exclusively in studies that examine ESs with more than two inputs. Our empirical analyses also show that imposing local regularity—at least first-order features such as nondecreasing output from increases in inputs— increases stability in the estimates. Here we conclude that imposing local regularity conditions using approaches such as the Bayesian methods we used should be employed when possible to estimate the underlying functions that are used to calculate measures of substitution.

Both of these advances, the MES and imposing local regularity, have the potential to improve future work on IT productivity, IT pricing, IT cost estimation, and any type of analysis that posits the substitution of IT capital for non-IT capital or labor.

## Acknowledgments

The authors thank the senior editor and anonymous reviewers for their invaluable guidance. The authors also thank Albert S. Dexter, Victoria L. Mitchell, the conference participants at Decision Sciences Institute 2006 and the University of Alberta/University of Calgary MIS Research Workshop 2006, and colloquia participants at the University of Texas at Dallas, Purdue University, Michigan State University, and the City University of Hong Kong for helpful comments. Finally, the authors thank Jeanette Burman for outstanding editing assistance. Support was provided by the Social Science and Humanities Research Council of Canada [grant 864-2007-0028], the Robson Endowment, the Informatics Research Centre at the University of Calgary, and the Faculty Staff Development Scheme of the Faculty of Business at Hong Kong Polytechnic University.

## Appendix. Elements of the MES and AES

In the context of production functions, the AES and the MES are defined as in (1) and (2), respectively. For inputs IT capital (Z), non-IT capital (K), and labor (L), the determinant of the bordered Hessian, H, is defined as

$$
\mathrm{H} = \left| \begin{array}{c c c c} 0 & f _ {z} & f _ {k} & f _ {l} \\ f _ {z} & f _ {z z} & f _ {z k} & f _ {z l} \\ f _ {k} & f _ {k z} & f _ {k k} & f _ {k l} \\ f _ {l} & f _ {l z} & f _ {l k} & f _ {l l} \end{array} \right|,
$$

where the elements are the first and second derivatives of the production function. The first and second derivatives of the CES-translog form in (5) are

$$
f _ {z} = \frac {Y}{Z} \bigg [ \frac {\delta_ {z} Z ^ {- \rho}}{T} + 2 \beta_ {z z} z + \beta_ {z l} l + \beta_ {z k} k \bigg ],
$$

$$
f _ {k} = \frac {Y}{K} \bigg [ \frac {\delta_ {k} K ^ {- \rho}}{T} + 2 \beta_ {k k} k + \beta_ {k l} l + \beta_ {z k} z \bigg ],
$$

$$
f _ {l} = \frac {Y}{L} \bigg [ \frac {\delta_ {l} L ^ {- \rho}}{T} + 2 \beta_ {l l} l + \beta_ {k l} k + \beta_ {z l} z \bigg ],
$$

$$
f _ {z z} = \frac {f _ {z} ^ {2}}{Y} - \frac {f _ {z}}{Z} + \frac {Y}{Z ^ {2}} \left[ \frac {\rho \delta_ {z} ^ {2} Z ^ {- 2 \rho}}{T ^ {2}} - \frac {\rho \delta_ {z} Z ^ {- \rho}}{T} + 2 \beta_ {z z} \right],
$$

$$
f _ {k k} = \frac {f _ {k} ^ {2}}{Y} - \frac {f _ {k}}{K} + \frac {Y}{K ^ {2}} \bigg [ \frac {\rho \delta_ {k} ^ {2} K ^ {- 2 \rho}}{T ^ {2}} - \frac {\rho \delta_ {k} K ^ {- \rho}}{T} + 2 \beta_ {k k} \bigg ],
$$

$$
f _ {l l} = \frac {f _ {l} ^ {2}}{Y} - \frac {f _ {l}}{L} + \frac {Y}{L ^ {2}} \bigg [ \frac {\rho \delta_ {l} ^ {2} L ^ {- 2 \rho}}{T ^ {2}} - \frac {\rho \delta_ {l} L ^ {- \rho}}{T} + 2 \beta_ {l l} \bigg ],
$$

$$
f _ {z k} = \frac {f _ {z} f _ {k}}{Y} + \frac {Y}{Z K} \left[ \frac {\rho \delta_ {z} \delta_ {k} Z ^ {- \rho} K ^ {- \rho}}{T ^ {2}} + \beta_ {z k} \right],
$$

$$
f _ {z l} = \frac {f _ {z} f _ {l}}{Y} + \frac {Y}{Z L} \bigg [ \frac {\rho \delta_ {z} \delta_ {l} Z ^ {- \rho} L ^ {- \rho}}{T ^ {2}} + \beta_ {z l} \bigg ],
$$

$$
f _ {k l} = \frac {f _ {k} f _ {l}}{Y} + \frac {Y}{K L} \bigg [ \frac {\rho \delta_ {k} \delta_ {l} K ^ {- \rho} L ^ {- \rho}}{T ^ {2}} + \beta_ {k l} \bigg ],
$$

where $T = \delta _ { z } Z ^ { - \rho } + \delta _ { k } K ^ { - \rho } + ( 1 - \delta _ { z } - \delta _ { k } ) L ^ { - \rho } .$

By Youngs’ theorem, $f _ { i j } = f _ { j i } .$ In the expression of the AES and MES, a cofactor $\mathrm { H } _ { i j }$ is defined as $\mathrm { H } _ { i j } ^ { - } = ( - 1 ) ^ { i + j } | { \bf M } _ { i j } | ,$ where $| \mathbf { M } _ { i j } |$ is the determinant of the minor matrix that is obtained from deleting the ith row and the jth column of the bordered Hessian. The required minor matrices that are needed to form the different cofactors are

$$
\mathbf {M} _ {k z} = \left[ \begin{array}{c c c} 0 & f _ {k} & f _ {l} \\ f _ {z} & f _ {z k} & f _ {z l} \\ f _ {l} & f _ {l k} & f _ {l l} \end{array} \right], \quad \mathbf {M} _ {l z} = \left[ \begin{array}{c c c} 0 & f _ {k} & f _ {l} \\ f _ {z} & f _ {z k} & f _ {z l} \\ f _ {k} & f _ {k k} & f _ {k l} \end{array} \right],
$$

$$
\mathbf {M} _ {z k} = \left[ \begin{array}{c c c} 0 & f _ {z} & f _ {l} \\ f _ {k} & f _ {k z} & f _ {k l} \\ f _ {l} & f _ {l z} & f _ {l l} \end{array} \right], \quad \mathbf {M} _ {z l} = \left[ \begin{array}{c c c} 0 & f _ {z} & f _ {k} \\ f _ {k} & f _ {k z} & f _ {k k} \\ f _ {l} & f _ {l z} & f _ {l k} \end{array} \right],
$$

$$
\mathbf {M} _ {k l} = \left[ \begin{array}{c c c} 0 & f _ {z} & f _ {k} \\ f _ {z} & f _ {z z} & f _ {z k} \\ f _ {l} & f _ {l z} & f _ {l k} \end{array} \right], \quad \mathbf {M} _ {l k} = \left[ \begin{array}{c c c} 0 & f _ {z} & f _ {l} \\ f _ {z} & f _ {z z} & f _ {z l} \\ f _ {k} & f _ {k z} & f _ {k l} \end{array} \right].
$$

## References

Allen RGD (1938) Why information should influence productivity. Mathematical Analysis for Economists (St. Martin’s, New York).

Amado C, Terasvirta T (2013) Modelling volatility by variance decomposition. J. Econom. 175(2):142–153.

Barnett W (2002) Tastes and technology: Curvature is not sufficient for regularity. J. Econometrics 108(1):199–202.

Barnett W, Pasupathy M (2003) Regularity of the generalized quadratic production model: A counterexample. Econometric Rev. 22(2):135–154.

Berndt R, Rappaport N (2002) Price and quality of desktop and mobile personal computers: A quarter century historical overview. Amer. Econom. Rev. 91(2):268–273.

Blackorby C, Russell R (1981) The Morishma elasticity of substitution; symmetry, constancy, separability, and its relationship to the Hicks and Allen elasticities. Rev. Econom. Stud. 48(1): 147–158.

Blackorby C, Russell R (1989) Will the real elasticity of substitution please stand up? (A comparison of the Allen/Uzawa and Morishima elasticities). Amer. Econom. Rev. 79(4):882–888.

Brynjolfsson E, Hitt LM (2000) Beyond computation: Information technology, organizational transformation and business practices. J. Econom. Perspect. 14(4):23–48.

Brynjolfsson E, Hitt LM (2003) Computing productivity: Firm-level evidence. Rev. Econom. Statist. 85(4):793–808.

Caves D, Christensen L (1981) Global properties of the FFFs. Amer. Econom. Rev. 70:422–432.

Chambers RG (1988) Applied Production Analysis: A Dual Approach (Cambridge University Press, Cambridge, UK).

Cheng Z, Nault BR (2007) Industry level supplier-driven IT spillovers. Management Sci. 53(8):1199–1216.

Cheng Z, Nault BR (2012) Relative industry concentration and customer-driven IT spillovers. Inform. Systems Res. 23(2): 340–355.

Chun H, Mun S (2006) Substitutability and accumulation of information technology capital in U.S. industries. Southern Econom. J. 72(4):1002–1015.

Chwelos P, Ramirez R, Kraemer KL, Melville N (2010) Does technological progress alter the nature of information technology as a production input? New evidence and new results. Inform. Systems Res. 21(2):392–408.

Coelli TJ, Prasada Rao DS, O’Donnell CJ, Battese GE (2005) An Introduction to Efficiency and Productivity Analysis (Springer, New York).

Dewan S, Min C (1997) The substitution of information technology for other factors of production: A firm level-analysis. Management Sci. 43(12):1660–1675.

Diewert W, Wales T (1987) FFFs and global curvature conditions. Econometrica 55(1):43–68.

Fan Y, Pastorello S, Renault E (2007) Maximization by parts in extremum estimation. Working paper, Vanderbilt University, Nashville, TN.

Farrell D (2003) The real new economy. Harvard Bus. Rev. (October):105–112.

Gallant A, Golub E (1984) Imposing curvature restrictions on FFFs. J. Econometrics 26:295–321.

Hicks J (1932) The Theory of Wages, 2nd ed. (MacMillian, London).

Hitt LM, Snir E (1999) The role of information technology in modern production: Complement or substitute to other inputs? Working paper, University of Pennsylvania, Philadelphia.

Jorgenson D, Fraumeni BM (1981) Relative prices and technical change. Berndt E, Field B, eds. Modeling and Measuring Natural Resource Substitution (MIT Press, Cambridge, MA), 17–47.

Kudyna S, Diwan R (2002) Increasing returns to information technology. Inform. Systems Res. 13(1):104–111.

Lau L (1978) Testing and imposing monotonicity, convexity and quasiconvexity constraints. Fuss M, McFadden D, eds. Production Economics: A Dual Approach to Theory and Applications, Vol. 1 (North-Holland, Amsterdam), 409–453.

Mittal N, Nault BR (2009) Investments in information technology: Indirect effects and information technology intensity. Inform. Systems Res. 20(1):140–154.

Morey E (1986) An introduction to checking, testing, and imposing curvature properties: The true function and the estimated function. Canadian J. Econom. 19(2):207–235.

Morishima M (1967) Danryokusei Rison ni kansuru Ni-san no Teian (A few suggestions on the theory of elasticity). Keizai Hyoron (Economic Review, Tokyo) 16:144–150.

Moschini G (1999) Imposing local curvature conditions in flexible demand system. J. Bus. Econom. Statist. 17:487–490.

Mundra K, Russell RR (2004) Dual elasticity of substitution. Working paper, San Diego State University, San Diego.

Nordhaus D (2002) Productivity growth and the new economy. Brookings Paper Econom. Activity 2:201–217.

O’Donnell C, Coelli T (2005) A Bayesian approach to imposing curvature on distance functions. J. Econometrics 126:493–523.

Pollak R, Sickles R, Wales T (1984) The CES-Translog: Specification and estimation of a new cost function. Rev. Econom. Statist. 66:602–607.

Ryan D, Wales T (1998) A simple method for imposing local curvature in some flexible consumer-demand system. J. Bus. Econom. Statist. 16(3):331–338.

Salvanes K, Tjotta S (1998) A note on the importance of testing for regularities for estimated FFFs. J. Productivity Anal. 9: 133–143.

Solow R (1987) We’d better watch out. New York Times Book Rev. (July 12):36. Accessed April 14, 2015, http://www.standup economist.com/pdf/misc/solow-computer-productivity.pdf.

Song PXK, Fan Y, Kalbfleisch JD (2005) Maximization by parts in likelihood inference. J. Amer. Statist. Assoc. 100:1145–1157.

Tambe P, Hitt LM (2014) Job hopping, information technology spillovers, and productivity growth. Management Sci. 60(2): 338–355.

Terrell D (1996) Incorporating monotonicity and concavity conditions in FFFs. J. Appl. Econometrics 11(2):179–194.

U.S. Bureau of Labor Statistics (2006) Overview of capital inputs for the BLS multifactor productivity measures. Accessed April 14, 2015, http://www.bls.gov/mfp/mprcaptl.pdf.

Uzawa H (1962) Production functions with constant elasticities of substitution. Rev. Econom. Stud. 29:291–299.
