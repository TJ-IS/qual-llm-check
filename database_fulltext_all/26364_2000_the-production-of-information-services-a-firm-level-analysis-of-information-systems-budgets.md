---
otero_id: 26364
otero_key: "3GFCM8GK"
title: "The Production of Information Services: A Firm-Level Analysis of Information Systems Budgets"
authors: "Vijay Gurbaxani; Nigel Melville; Kenneth Kraemer"
year: "2000"
journal: "Information Systems Research"
doi: "10.1287/isre.11.2.159.11779"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/3GFCM8GK/fulltext/images/5f0cc20f1d816665306beb00be8ce995947242a84d78d841c4f877e155658abb.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# The Production of Information Services: A Firm-Level Analysis of Information Systems Budgets

Vijay Gurbaxani, Nigel Melville, Kenneth Kraemer,

To cite this article:

Vijay Gurbaxani, Nigel Melville, Kenneth Kraemer, (2000) The Production of Information Services: A Firm-Level Analysis of Information Systems Budgets. Information Systems Research 11(2):159-176. http://dx.doi.org/10.1287/isre.11.2.159.11779

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 2000 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/3GFCM8GK/fulltext/images/f4719e93705c47c8ef512f15a1c87fd0aa61c39cecbbfa3be28a815732c0456d.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# The Production of Information Services: A Firm-Level Analysis of Information Systems Budgets

Vijay Gurbaxani • Nigel Melville • Kenneth Kraemer

Center for Research on Information Technology and Organizations, Graduate School of Management,

University of California, Irvine, Irvine, California 92697

vgurbaxa@gsm.uci.edu • npmelvil@uci.edu • kkraemer@gsm.uci.edu

revious research has demonstrated that the production of information services can be characterized at the aggregate economy-wide level by the Cobb-Douglas production function. However, the underlying production process at the firm level has not yet been ascertained. The objective of this paper is to determine the form of the production process for information systems services at the firm level by conducting an empirical analysis of IS budget data. The production of information services is modeled using a production function with two inputs, hardware and personnel. We estimate various econometric specifications to determine several characteristics of the provision of information services, including the allocation of the information systems budget to its two largest components—hardware and personnel—and its implications for the form of the production function. After controlling for industry sector, we find that the ratio of personnel to hardware is independent of scale, which indicates a homothetic production function. We also find that the ratio of factor shares is constant with time, consistent with the Cobb-Douglas production function. We conclude that the underlying form of the production function is the same at the level of both the firm and the economy. Our analysis demonstrates how the application of production theory to the production of information services can yield useful insights from both a theoretical and managerial perspective. (Information Systems Management; Information Systems Budgets; Production Function; Economics of Information Systems)

## 1. Introduction

Commensurate with rapid technological change and decreased prices, investment by U.S. firms in information technology (IT) has grown steadily in recent decades. Morgan Stanley & Co. estimates that the annual outlay accounts for between 2% and 3% of the total U.S. GDP (Roach 1994), while the Bureau of Economic Analysis (BEA) estimates that its share of total business equipment spending has risen from roughly 5% in 1970 to almost 50% in 1996 (Margherio 1998). The rapid growth in investment in IT by U.S. firms, along with its ever increasing importance as a factor input, have created serious management challenges. In particular, determining the allocation of corporate resources to information technology and managing these resources efficiently are of critical importance. This paper focuses on the efficient allocation of a corporate information systems (IS) budget into its two major components—hardware (or capital) and personnel (or labor). Because budgets reflect the techniques used to produce these services, the analysis of budget data can provide useful insights into the nature of the underlying production process.

Understanding firm-level production is critical to efficiently managing the information systems function in the face of rapid technological progress. Specifically, as the costs of hardware per unit of performance decrease at approximately 20% per year while unit personnel costs have historically remained flat or perhaps increased slowly, the ability to exploit these price trends by substituting hardware for personnel is central to cost-effective management of the information systems function. Indeed, in today’s information systems environment, in which the compensation of certain specialties of personnel has risen rapidly, it has become even more important to find ways to alleviate the impact of these cost trends by substituting hardware for personnel. Naturally, the ability to substitute hardware for personnel depends on the technical possibility of substitution between them and is measured by the elasticity of substitution of the production function that effectively models the production process. As this measure is roughly the percentage change in the ratio of input quantities per unit percentage change in the ratio of input prices, estimating the form of the production function and the associated elasticity of substitution has significant managerial implications. It will enable managers to determine the optimal laborcapital ratio in the production of information systems services for a given set of input prices, and is particularly useful when the input price ratio changes frequently, as is the case here. For example, if it is found that the elasticity of substitution for the production of information services is 1.5, then we would expect the quantity ratio to change by 30% given a 20% reduction in the price of hardware relative to software. The optimal labor-capital ratio has been used in numerous production settings as a measure of production efficiency.

In this paper, our aim is to determine the form of the production function and magnitude of the elasticity of substitution for information systems services at the firm level via a rigorous empirical analysis of information systems budget data from Fortune 500 firms. Previous research has shown that the production process for information systems services at the level of the economy can be characterized by the Cobb-Douglas production function (Gurbaxani and Mendelson 1987, 1992). Indeed, many aggregate production processes have been successfully modeled by the Cobb-Douglas production function (Hildebrand and Liu 1965). However, Cobb-Douglas production at the aggregate level does not necessarily imply that the firm-level production function is also Cobb-Douglas or, if it is, that it has the same parameter values. In the former case, it has been shown analytically that the aggregate production function may describe aggregate behavior quite well despite having a different functional form than that of the individual firms comprising the aggregate (Houthakker 1955). In the latter case, if the individual firms have Cobb-Douglas production functions with different parameters, under certain conditions a Cobb-Douglas function may still successfully model aggregate-level behavior (Fisher 1971). Further, constant returns to scale at the aggregate level may be consistent with decreasing returns to scale at the firm level. Intuitively (and departing temporarily from the perfect competition assumption), this may arise due to “aggregate” economies of scale, perhaps the result of government regulation. To the best of our knowledge, no research exists that has empirically determined the firm-level production process for information systems services. Thus, this study is a reasonable next step in investigations of the technical constraints faced by firms and their allocations of factors in the provision of information services.

The outline of the paper is as follows. The theory, including background, hypotheses, and estimation techniques, is presented in §2. The data set is described and potential limitations are discussed in §3. Results of the analysis are presented in §4. The managerial implications of the research and our concluding remarks are presented in §5.

## 2. Theory

In this section we draw on microeconomic theory to discuss the theory of production as it applies to information services. Previous research on the allocation of the information systems budget to its component categories is introduced and the main results are summarized. Next, we present models that enable the empirical determination of the production function using budget data. We show that budget data spanning several years provides us with the means to identify and characterize firm-level production without directly estimating the production function. Specifically, the data enable us to distinguish between the Cobb-Douglas production function and the Constant Elasticity of Substitution (CES) production function (with elasticity of substitution different from unity) by testing the constancy of labor to capital budget shares with time. Finally, we discuss estimation and inference methodologies in the context of the above models.

## 2.1. Previous Research

A distinctive feature of the information technology industry is the exponential decline in the unit costs of hardware with time. Early studies of the impact of this phenomenon on IS budgets focused on its allocation to hardware and software costs. The prevailing viewpoint was that this cost trend would result in an increasing share of the information systems budget allocated to software (including both the costs of programming labor and purchased software) according to an S-shaped curve (Boehm 1981). Others, however, cited empirical evidence to the contrary, suggesting that, in fact, the data was consistent with constant budget shares of hardware and software with time (Frank 1983).

This controversy was due in large part to the absence of a theoretical framework within which to rigorously analyze the problem. The question of IS budget share trajectory was first analyzed formally by Gurbaxani and Mendelson (1987) who proposed the production of information services model. This model examines the behavior of a firm that maximizes the net present value of information services over a given planning horizon. Information services is modeled as a production process with two inputs, software and hardware. Every period, the firm uses its available software and hardware to generate information services. In each period, the firm decides how much to invest in information systems and how to allocate this investment between the two inputs. The model allows for obsolescence of the inputs and changing costs. The authors are able to obtain a closed-form solution to the discounted dynamic programming problem for the general case of an unspecified production function. Depending on the form of production function used in the model, both outcomes—constant budget shares or an increasing software share—can obtain. For the case of the fixed-proportion production function, equivalent to no substitutability between hardware and software, the S-shaped software budget share curve obtains. In contrast, for the case of the Cobb-Douglas production function, the authors show that software and hardware budget shares are constant with time. Thus, a rigorous analytic treatment has identified a critical feature of efficient information systems production—the substitutability of hardware for software.

Empirically, information systems spending data at the level of the U.S. economy are strikingly consistent with the prediction of the model using the Cobb-Douglas production function, strengthening the case of constant budget shares of hardware and software over time. In a subsequent statistical analysis of IS spending data, again at the aggregate level, Gurbaxani and Mendelson (1992) utilize several procedures to test the null hypothesis that the ratio of software to hardware budget shares remains constant with time. In these studies, software costs were defined as the sum of the costs of personnel who developed and maintained software, and the costs of purchased software. It is worth pointing out that software personnel costs account for over 80%–90% of software costs. Their results support the constancy argument, independent of the pattern of growth of the overall IS budget. Moreover, from a practical standpoint, the substitutability of hardware and software development effort would seem to preclude the fixed-proportion production function. For example, high-level programming languages reduce software development costs relative to lower level languages but require increased hardware resources.

The budget studies using aggregate data have contributed significantly to the resolution of the budget shares debate. However, the assumption implicit in the production of the information services model—that the specific form of production function used successfully at the aggregate economy-wide level aptly characterizes firm-level production—has yet to be empirically tested. Further, we extend the earlier work to focus not just on software costs, which as we noted were associated mainly with software personnel, but on total personnel costs. As we will discuss later, software development and maintenance and operations are the two major activities conducted by an information systems organization. Just as hardware can be substituted for personnel in the software development activity, similar trade-off patterns exist in the operations activity as well. Accordingly, it is useful to examine the hardware-personnel ratio in the overall provision of information systems services. In addition, valuable insight, from both a positive and a normative standpoint, can be gained by examining budget shares at the firm level, and these insights can be used to assist management in deciding how to efficiently allocate its scarce IT resources.

In an earlier study, we examined the production process of information systems services at the firm level (Gurbaxani et al. 1996). Specifically, we conducted a cross-sectional analysis of IS budgets for the 1990 budget year. Two principal hypotheses were tested. The first concerns the question of whether the production of information services at the firm level is homothetic—namely, whether the optimal hardwarepersonnel ratio is independent of scale. This study examined personnel costs rather than software costs. The null hypothesis of homotheticity is retained. The second hypothesis concerns economies of scale. It examined the relationship between the overall information systems budget and the scale of the corporation; the null hypothesis of constant returns to scale is retained. These results are useful for two reasons. First, they are consistent with a Cobb-Douglas production function. Second, they provide normative guidelines to managers regarding the efficient allocation of IT resources among the hardware and personnel budget components. However, these properties of homotheticity and constant returns to scale are not unique to Cobb-Douglas production. Indeed, the CES production function possesses these properties as well. To gain a definitive answer to the question of whether the Cobb-Douglas function obtains at the firm level, it is necessary to conduct a firm-level analysis of cross-sectional data spanning several years. This analysis is the focus of the present study.

## 2.2. Trade-Offs in the Production of Information Services

To understand the nature of trade-offs in the production of information services, it is useful to assess the activity in a structured manner. We consider this production process to have two major inputs, hardware and personnel. As we shall see later, these two inputs account for around 70% of the budget. We will argue that these two inputs are substitutes in production, that is, they can be combined in different ratios to produce any given level of output. Clearly, hardware and personnel are aggregate inputs with many dimensions and are likely to interact in intricate ways. This analysis can be simplified by focusing the discussion on the two major activities that constitute information services: applications development and operations.

In the case of applications development, there are three principal ways in which hardware can be substituted for personnel. First, programmer productivity can be increased through the provision of increased hardware support in the development environment. For example, faster computers in the development environment that provide improvements in response time have been shown to improve programmer productivity (Thadhani 1984). A second approach is through the provision of software tools, which increase programmer productivity but require significant hardware support. CASE tools are a case in point. Sophisticated graphical user interfaces like Windows 95 are another example. These interfaces require as much as 25% of system hardware resources that become unavailable to applications, but it is argued that these systems increase productivity. Database management systems automate many of the file management tasks that programmers once had to code into their applications and provide nonprocedural languages for data access; however, these systems are very hardware-intensive. The third form of substitution derives from the impact of target hardware capacity. As hardware costs decrease, it is often more efficient to increase the capacity of the hardware systems on which the application will run, rather than attempt to improve the efficiency of software programs by devoting additional effort into fitting software into limited hardware resources such as memory or processor capacity.

The trade-offs between hardware and personnel exist in the operations activity as well. Many sophisticated tools are now in use to manage networks and data center operations. These tools allow dramatic reductions in personnel required to manage these operations. Many data centers are now run as “lights-out”

operations; network administrators can diagnose and solve problems remotely. The consolidation of data centers is another example of how the personnel-hardware ratio can be reduced.

To summarize the above discussion, substitution between hardware and personnel takes several forms. Software tools are one important way in which hardware can be substituted for personnel. Furthermore, hardware can directly substitute for personnel by reducing the performance requirements of software. While the above discussion has drawn on the economic theory of production to provide qualitative insights into the nature of the trade-off, we believe that a formal modeling approach will prove to be of value in assessing the production process for information services.

## 2.3. Modeling Firm-Level Production

This paper builds in part on the theoretical models developed in Gurbaxani and Mendelson (1987). The approach involves modeling the production process for information services using a production function that transforms the two inputs—hardware and personnel—into output, information services. The properties of the production process are captured by the specification of the production function. The primary issue that we are concerned with in this paper is the degree of substitutability between hardware and personnel in the information services production process. The analysis centers on the determination of whether the Cobb-Douglas production function characterizes production at the firm level.

We begin by considering two categories of production functions commonly employed in the literature: those with constant and those with variable elasticity of substitution. We argue that the constant elasticity of substitution category, though less flexible than the former, is likely to obtain in our case, thus narrowing the eligible set of productions functions to two: the Cobb-Douglas and the CES (cf. Arrow et al. 1961).<sup>1</sup> Finally, we show that the difference between the economic implications of the two functions enables us to empirically determine which obtains.

Consider the simple case of two inputs. As the price of one falls, the assumption of profit-maximizing behavior dictates that the firm will try to substitute away from the relatively more expensive input and toward the cheaper input, holding constant the level of output produced. A measure of the extent of this shift is the elasticity of substitution. As discussed above, substitutability between hardware and personnel is achieved in several ways, including the use of software tools. Over time, as the hardware to personnel ratio changes, the elasticity of substitution may also vary. For example, one could argue that as more and more substitution possibilities have been exploited, as might be the case when the information systems environment is highly hardware-intensive, the elasticity of substitution may decrease. Conversely, the development of new software tools may increase the opportunities for substitution. We do not know conclusively whether the production process is consistent with constant elasticity of substitution or with a varying elasticity of substitution. In any event, technical possibilities for substitution change slowly. Correspondingly, while this may be an important effect over long durations, the relatively short time span considered in this study (six years) would suggest that it is reasonable to assume constancy of this parameter.<sup>2</sup> Thus, we focus our attention on the class of constant elasticity of substitution production functions, which includes the CES production function and the Cobb-Douglas production function.

The CES production function is homothetic, homogenous of degree one, has constant elasticity of substitution, and is given by

$$
Y = A [ \delta K ^ {- \rho} + (1 - \delta) L ^ {- \rho} ] ^ {1 / \rho}\tag{1}
$$

where Y is the maximum output for a given flow of capital, K, and labor, L. The larger the efficiency parameter, A, is, ceteris paribus, the greater is the output. When the distribution parameter, d, increases, the ratio of capital’s share of output to the share of labor rises. The substitution parameter, q, is so named as it is the difference of the inverse of the elasticity of substitution and one.

The Cobb-Douglas production function is a special case of the CES production function, with the added property of unitary elasticity of substitution.<sup>3</sup>

$$
Y = A L ^ {a} K ^ {b}.\tag{2}
$$

The Cobb-Douglas production function has the unique property that the ratio of the budget shares of the two inputs is independent of the relative price.

To directly test whether the CES production function obtains, one potential method of inquiry is to estimate the linear approximation of the CES production function (Kmenta 1967):

$$
\begin{array}{r l} & {\log Y = \log A + v \delta \log K} \\ & {\quad + v (1 - \delta) \log L - \frac {1}{2} v \rho \delta (1 - \delta) [ \log K / L ] ^ {2},} \end{array}\tag{3}
$$

where t is a returns-to-scale parameter. If the coefficient on the squared term in Equation (3) is significant, then the null hypothesis of unitary and constant returns to scale is rejected, thereby implying the CES production function. However, in this study we do not estimate (3) directly due to the difficulty in constructing a metric for the “output” of information systems services. We therefore turn to alternative econometric specifications to determine which, if either, of the two functional specifications obtain. In particular, we test the implications of the two classes of production functions for budget behavior as a means of identifying the appropriate functional form.

We first investigate homotheticity of the production function to test whether our data are consistent with both forms of production functions. The function $g$ is homothetic if it can be written as a monotone transformation of a linearly homogeneous function. An interesting and unique property of homothetic production functions is that the optimal ratio of the two inputs is independent of scale for a given set of prices (Silberberg 1978).<sup>4</sup> We operationalize the scale of IT operations by the total IT budget, which has face validity and has been done in prior studies (Gurbaxani et al. 1996). One simple way to test for homotheticity is to use the following model:

$$
P / H = C + D \cdot B + \varepsilon ,\tag{4}
$$

where $P , H ,$ and $B ,$ are, respectively, personnel, hardware, and budget (to be specified exactly below) and e is the disturbance term. Retaining the null hypothesis of $D = 0$ corresponds to the presence of homotheticity. In addition, the estimate of the constant term allows us to determine the optimal ratio of personnel to hardware, which is important from a managerial standpoint. The model, however, is unable to discern the differences in individual budget characteristics of personnel and hardware, which may move together in several different ways even if the null hypothesis is retained. For example, under the null hypothesis, hardware and personnel may vary linearly with budget, or may be entirely uncorrelated with budget. However, Equation (4) cannot be used to distinguish between these two cases.

An alternative model specification is to separately regress personnel and hardware on total budget using the following two-equation system:

$$
\begin{array}{l} \log H = C _ {h} + D _ {h} \cdot \log B + \varepsilon_ {h} \\ \log P = C _ {p} + D _ {p} \cdot \log B + \varepsilon_ {p}. \end{array}\tag{5}
$$

For this model, the null hypothesis of homotheticity is $D _ { p } \ = \ D _ { h }$ . This is easily seen by exponentiating both equations in (5) and forming the ratio of personnel to hardware, which is equal to exp $( C _ { p } \ : - \ : C _ { h } ) \ : + \ : ( D _ { p } \ : -$ D )log B] and independent of budget under the null.<sup>5</sup>

Up to this point, we have proposed two econometric models that enable us to test for homotheticity using cross-sectional firm-level data and briefly discussed estimation techniques. We now turn to the question of how the introduction of a time dimension can be used to answer our original question of whether the Cobb-Douglas production function obtains at the firm level.

As mentioned previously, one difference between the two production functions is that the Cobb-Douglas has constant and unitary elasticity of substitution, whereas the CES has constant elasticity of substitution that can take on any value. This difference implies that for the former, the ratio of factor shares is constant, while for the latter, it is a function of the relative price. Thus, from one period to the next, the decreasing price of hardware relative to labor accompanied by substitution of hardware for software will lead to a change in factor shares if the CES production function obtains, and no change if the Cobb-Douglas obtains. It is in this way that the use of data spanning several years is essential to empirically distinguishing between the two forms of production function. It is worth emphasizing that the existence of constant budget shares of hardware and personnel over time is a necessary and sufficient condition of Cobb-Douglas production (Gurbaxani 1990).

To test whether the factor shares are constant with time we use dummy variables to account for changes in both slope and intercept for each year. Our model is specified as:

$$
\begin{array}{r l} \log H & = C _ {h 0} + C _ {h 1} M _ {1} + \dots + C _ {H T} M _ {T} \\ & + D _ {h 0} \log B + D _ {h 1} M _ {1} \cdot \log B \\ & + \dots + D _ {h T} M _ {T} \cdot \log B + \varepsilon_ {h} \end{array}\tag{6}
$$

$$
\log P = C _ {p 0} + C _ {p 1} M _ {1} + \dots + C _ {P T} M _ {T} + D _ {p 0} \log B
$$

$$
+ D _ {p 1} M _ {1} \cdot \log B + \dots + D _ {p T} M _ {T} \cdot \log B + \varepsilon_ {p}.
$$

In this model, $M _ { t } = 1$ for year $t ,$ and 0 otherwise. For example, for 1992 (t  3) Equation (6) becomes:

$$
\begin{array}{l} \log H = (C _ {h 0} + C _ {h 3}) + (D _ {h 0} + D _ {h 3}) \cdot \log B + \varepsilon_ {h} \\ \log P = (C _ {p 0} + C _ {p 3}) + (D _ {p 0} + D _ {p 3}) \cdot \log B + \varepsilon_ {p}. \end{array}\tag{7}
$$

As our objective is to determine whether budget shares of hardware and personnel are constant over time, the null hypothesis is given by:<sup>6</sup>

<sup>6</sup>For 1989, the ratio of factor shares is given by exp $[ ( C _ { p 0 } \mathrm { ~ - ~ } C _ { h 0 } ) \mathrm { ~ + ~ }$ $( D _ { p 0 } - D _ { h 0 } )$ log B], which is independent of budget if and only if $D _ { p 0 }$ $\begin{array} { r l } { \mathrm { ~ \ } } & { { } = \ { D } _ { h 0 } . } \end{array}$ For each subsequent year, the ratio of factor shares is given by exp $\{ ( C _ { p 0 } + C _ { p t } ) - ( C _ { h 0 } + C _ { h t } ) + [ ( D _ { p 0 } + D _ { p t } ) - ( D _ { h 0 } + D _ { h t } ) $ ]log B}. Thus, $D _ { p t } = D _ { h t }$ must hold for years 1990 through 1994 for factor shares to be independent of budget. Imposing the additional constraint that factor shares are constant with time implies that $C _ { p t } =$ $C _ { h t }$ for all t. Taken together, these restrictions impose the constraint that the factor shares are constant with time, with the added condition of homotheticity (for robustness).

$$
\begin{array}{r l} H _ {0} \colon D _ {h 0} & = D _ {p 0}; D _ {h t} = D _ {p t}; \\ C _ {h t} & = C _ {p t}; t = 1, 2, \ldots , T. \end{array}\tag{8}
$$

Rejecting the null hypothesis is consistent with the CES production function.

To summarize the above discussion, retaining the null hypothesis of homothetic production is consistent with both Cobb-Douglas and CES production. On the other hand, rejecting the hypothesis of homothetic production would suggest that neither of the two forms of production function are appropriate. Next, retaining the null hypothesis of constant budget shares is consistent with Cobb-Douglas production. Rejecting this hypothesis would suggest that the data is inconsistent with Cobb-Douglas production. Further analysis on the constancy of the change in budget shares would be required to determine whether the data are consistent with CES production.

Having argued why the production of information services is characterized by constant elasticity of substitution and discussed econometric models to statistically infer which of the two most common production functions obtains, we now turn to a discussion of estimation techniques.

## 2.3. Estimation and Hypothesis Testing

Each of the two equations in (5) and (6) could be estimated independently using ordinary least squares (OLS) and unbiased and consistent parameter estimates would be obtained. Typically, an improvement in efficiency can be obtained by taking into account the correlation between error terms across equations arising both from the link between hardware acquisitions and personnel decisions in firms and from firm-specific and general business conditions affecting both. This can be accomplished using Zellner’s Seemingly Unrelated Regression (SUR) model to estimate the systems (5) and (6) (Zellner 1962). However, in this special case—both equations contain the same set of regressors and an equal number of observations—it is well known that the SUR and OLS estimators are identical (Greene 1993, Judge et al.1982). Therefore, no efficiency increase results from the use of SUR.

In the case of hypothesis testing, due to the presence of correlation between the disturbances of Equations (5) and (6) $( \mathrm { E } [ \mathfrak { E } _ { h } \mathfrak { E } _ { p } ] \neq 0 )$ , we must resort to asymptotic tests of the null hypotheses. Assuming that the disturbances in both equations are normally distributed and in the current context of maximum likelihood estimators, three such test statistics are available and all are distributed asymptotically as chi-squared variates: the Wald Test (W), the likelihood ratio test (LR), and the Lagrange Multiplier test (LM).

The Wald test (W) is based on the difference between the constraint evaluated at the maximum likelihood estimate of the parameter and zero. Only the unrestricted model need be estimated and the general form (assuming errors are independent and identically distributed) is given by

$$
\begin{array}{r l} {F = (R b - r) ^ {\prime} [ s ^ {2} R (X ^ {\prime} X) ^ {- 1} R ^ {\prime} ] ^ {- 1} (R b - r)} \\ & {\sim F _ {q, 2 N - K},} \end{array}\tag{9}
$$

where b is the least squares estimate of the unknown parameter vector, $R b \mathrm { ~ - ~ } r$ is the matrix of restrictions, s is the standard error of the regression, q is the number of restrictions, N is the number of observations, and K is the number of independent variables. The test statistic presented in (9) multiplied by the number of restrictions converges asymptotically to a chi-squared statistic:

$$
W q (R b - r) ^ {\prime} [ s ^ {2} R (X ^ {\prime} X) ^ {- 1} R ^ {\prime} ] ^ {- 1} (R b - r) \sim \chi_ {q} ^ {2}.\tag{10}
$$

According to Judge et al. (1985), the F-statistic may be better for small or moderate sample sizes. We compute both for completeness.

The likelihood ratio (LR) test is based on the difference between the likelihood function under the null hypothesis and that of the unrestricted model. In contrast to the Wald test, to apply the likelihood ratio test both the unrestricted and restricted model must be estimated. The following statistic is used:

$$
{\cal L} R = - 2 \mathrm{log} \lambda = N [ \mathrm{log} | \hat {\Omega} _ {u} | ] \sim \chi_ {q} ^ {2},\tag{11}
$$

where $\hat { \Omega } _ { r }$ is the estimated residual covariance matrix for the restricted model, and $\hat { \Omega } _ { u }$ is the estimated residual covariance matrix for the unrestricted model.

Finally, the Lagrange Multiplier (LM) test is based on the slope of the likelihood function under the null, which, if close to the unrestricted model, is close to zero at the peak of the likelihood function:

$$
{\cal L} M = N t r [ \hat {\Omega} _ {r} ^ {- 1} (\hat {\Omega} _ {r} - \hat {\hat {\Omega}} _ {u}) ] \sim \chi_ {q} ^ {2},\tag{12}
$$

where tr denotes the trace function and $\hat { \Omega } _ { u }$ is the estimated covariance matrix resulting from the one-step Zellner-efficient estimation of the unconstrained model.

All three tests are asymptotically equivalent (Srivastava 1987). However, their finite sample properties differ, so it is possible that we will reach different conclusions depending on which test statistic is used. It is known that $W > \mathrm { L R } > \mathrm { L M }$ , but neither test is uniformly most powerful as their power functions intersect (Rothenberg 1984).

Finally, note that although Equation (6) does allow for changes in slope and intercept for each year, it assumes that the disturbance terms do not change with time, covarying equivalently each year. This results in a 2 by 2 disturbance covariance matrix as in the crosssection case. Although this assumption may not hold, allowing the variances to change with time would significantly reduce the degrees of freedom and potentially render the system inestimable due to the fact that the number of elements to be estimated in the disturbance covariance matrix varies with the square of the number of equations in the SUR model. Therefore the assumption is maintained for practical reasons; we do not consider it likely that excluding this possibility has significantly degraded our results.

## 3. Data

The data used in this study were collected as part of the I/S Intercorporate Measurement Program (IMP), a joint research program conducted by the Center for Research on Information Technology at the University of California, Irvine, and CSC/Index of Cambridge, Massachusetts. The population is Fortune 500 corporations, the sample frame is 225 CSC/Index companies, and the number of firms in the sample is 138, with observations ranging from the year 1989 through 1994. In this section we describe the three variables used in the present study that originate from the IMP database. We also discuss the strengths and limitations of the data set and their impact on our study.

All variables are initially measured in current dollars and then converted to constant dollars using GDP price deflators. The first is total hardware expenses, H, and includes all hardware purchases (including telecommunication), depreciation and lease expenses, maintenance agreements, and supplies necessary for the operation of the hardware. The second variable is total personnel expenses, P, and the third is total IS expenses, B, which is the sum of total hardware expenses, total purchased software expense, total personnel expenses, total outside services expenses, and all other expenses. GDP deflators used to convert current to constant dollar values are those listed in the FAME Economic Database (formerly CITIBASE), maintained by Fame Data Services.

Summary statistics are listed in Table 1. Note that the hardware to total budget ratio remains roughly constant over the entire series, with a pooled mean of 0.26 and variance of 0.01. Similarly, the ratio of personnel to total budget also remains roughly constant, with a pooled mean of 0.39 and variance of 0.01. Figure 1 shows that the mean values of hardware and personnel components as a percentage of total I/S budget remain constant at around 26% and 40%, respectively. The personnel to hardware ratio remains roughly constant over time at around 1.8 with the exception of the year 1994, when its value rises to 2.79 (Figure 2). This can be explained by looking at the maximum value for 1994, which is 19.76 and roughly three times that of the second highest value. This is obviously an extreme case, but we elect to keep it in the data set.

The IMP survey has been carefully conducted for several years. We believe that it is the best available database on information systems spending. As with any longitudinal data set, however, it has both strengths and limitations. One strength is that, although not a probability sample in the strict sense, the data set has been shown ex post to be representative. The usual limitation of nonprobability samples is that their external validity suffers, i.e., generalizability from the sample results to the population is compromised. However, ex post determination that the sample is representative using a t-test analysis has been done for this data set (Gurbaxani et al. 1996). Thus, the sample is representative and our results are generalizable to the population.

Another strength of the data set is that the usual limitations in accuracy of self-reported surveys are mitigated by the existence of strong incentives for respondents to respond accurately. Specifically, the companies participating in this research program are doing so precisely because they want to benchmark themselves against their peers. They are promised confidentiality of their responses, given feedback showing their own benchmarks in comparison to other firms, and provided with a list of the other firms in the comparison. However, no other firm’s individual benchmarks are identified. The value of the benchmarks and the confidentiality of individual responses combine to induce accurate reporting. Further, as an additional consistency check, we compared the summary statistics of our dataset with those of Computerworld and Information Week. We found that our dataset displays trends similar to those in these external datasets, reinforcing our belief in the accuracy of our dataset.

One limitation of the data set is that the applicability of asymptotic test statistics for finite sample sizes (16 observations for 1991) cannot be taken for granted. As we are testing hypotheses involving the parameters of a 2-equation system whose disturbances are related, the use of asymptotic test statistics is necessary. This would not be the case if we knew a priori the disturbance covariance matrix. But, as is often the case in practice, we do not. Therefore, we are faced with the familiar but often ignored question from asymptotic distribution theory of how large our sample size must be for the asymptotic results to hold. In other words, we must determine how large our sample size should be for the finite test statistic to well approximate its asymptotic limit.

We answer this question by conducting a Monte Carlo simulation. Our model is the 2-equation SUR system in which each equation has the same set of regressors. For various sample sizes, we generate normally distributed disturbances and choose values for the parameters and the explanatory variable that are consistent with our data. We then compute the dependent variable, estimate the system, and perform the Wald test, which yields a test statistic that is asymptotically chi-squared with one degree of freedom under the null hypothesis. This procedure is replicated 100 times. We compute the Kolmogorov-Smirnov (K-S) test statistic to test the null hypothesis that the sample distribution is equal to the chi-square distribution.

Table 1 Summary Statistics (Millions of 1987 Dollars, Except for Ratios)

<table><tr><td></td><td>Year</td><td>N</td><td>Mean</td><td>Median</td><td>Std. Dev.</td><td>Minimum</td><td>Maximum</td></tr><tr><td rowspan="7">IS Budget (B)</td><td>89</td><td>28</td><td>398</td><td>72.6</td><td>979</td><td>4.09</td><td>3960</td></tr><tr><td>90</td><td>42</td><td>239</td><td>72.2</td><td>618</td><td>8.8</td><td>3870</td></tr><tr><td>91</td><td>16</td><td>106</td><td>62.3</td><td>135</td><td>10.89</td><td>535</td></tr><tr><td>92</td><td>31</td><td>215</td><td>66.2</td><td>649</td><td>7.44</td><td>3640</td></tr><tr><td>93</td><td>43</td><td>77</td><td>45.2</td><td>95</td><td>5.5</td><td>471</td></tr><tr><td>94</td><td>31</td><td>150</td><td>43.4</td><td>246</td><td>7.93</td><td>968</td></tr><tr><td>89-94</td><td>191</td><td>196</td><td>57.7</td><td>556</td><td>4.09</td><td>3960</td></tr><tr><td rowspan="7">Hardware (K)</td><td>89</td><td>28</td><td>105</td><td>18.6</td><td>263</td><td>0.42</td><td>1050</td></tr><tr><td>90</td><td>42</td><td>58</td><td>19.4</td><td>146</td><td>1.26</td><td>928</td></tr><tr><td>91</td><td>16</td><td>33</td><td>13.8</td><td>49</td><td>1.83</td><td>194</td></tr><tr><td>92</td><td>31</td><td>56</td><td>20</td><td>157</td><td>1.35</td><td>873</td></tr><tr><td>93</td><td>43</td><td>24</td><td>10.5</td><td>36</td><td>0.97</td><td>183</td></tr><tr><td>94</td><td>31</td><td>38</td><td>10.3</td><td>64</td><td>0.41</td><td>272</td></tr><tr><td>89-94</td><td>191</td><td>51</td><td>14.8</td><td>142</td><td>0.41</td><td>1050</td></tr><tr><td rowspan="7">Personnel (L)</td><td>89</td><td>28</td><td>150</td><td>26</td><td>370</td><td>1.89</td><td>1730</td></tr><tr><td>90</td><td>42</td><td>91</td><td>24.7</td><td>275</td><td>3.46</td><td>1780</td></tr><tr><td>91</td><td>16</td><td>45</td><td>21.6</td><td>56</td><td>3.96</td><td>208</td></tr><tr><td>92</td><td>31</td><td>90</td><td>22.4</td><td>297</td><td>3.6</td><td>1670</td></tr><tr><td>93</td><td>43</td><td>29</td><td>15.9</td><td>40</td><td>2.59</td><td>219</td></tr><tr><td>94</td><td>31</td><td>57</td><td>13.7</td><td>94</td><td>2.38</td><td>377</td></tr><tr><td>89-94</td><td>191</td><td>76</td><td>21.2</td><td>231</td><td>1.89</td><td>1780</td></tr><tr><td rowspan="7">K/B</td><td>89</td><td>28</td><td>0.258</td><td>0.268</td><td>0.092</td><td>0.097</td><td>0.418</td></tr><tr><td>90</td><td>42</td><td>0.282</td><td>0.278</td><td>0.124</td><td>0.061</td><td>0.548</td></tr><tr><td>91</td><td>16</td><td>0.263</td><td>0.274</td><td>0.078</td><td>0.125</td><td>0.377</td></tr><tr><td>92</td><td>31</td><td>0.26</td><td>0.27</td><td>0.087</td><td>0.063</td><td>0.462</td></tr><tr><td>93</td><td>43</td><td>0.274</td><td>0.265</td><td>0.121</td><td>0.035</td><td>0.714</td></tr><tr><td>94</td><td>31</td><td>0.239</td><td>0.235</td><td>0.097</td><td>0.012</td><td>0.398</td></tr><tr><td>89-94</td><td>191</td><td>0.265</td><td>0.26</td><td>0.105</td><td>0.012</td><td>0.714</td></tr><tr><td rowspan="7">L/B</td><td>89</td><td>28</td><td>0.408</td><td>0.425</td><td>0.074</td><td>0.271</td><td>0.543</td></tr><tr><td>90</td><td>42</td><td>0.377</td><td>0.373</td><td>0.106</td><td>0.145</td><td>0.621</td></tr><tr><td>91</td><td>16</td><td>0.41</td><td>0.448</td><td>0.101</td><td>0.183</td><td>0.518</td></tr><tr><td>92</td><td>31</td><td>0.413</td><td>0.43</td><td>0.09</td><td>0.227</td><td>0.578</td></tr><tr><td>93</td><td>43</td><td>0.401</td><td>0.405</td><td>0.118</td><td>0.132</td><td>0.622</td></tr><tr><td>94</td><td>31</td><td>0.373</td><td>0.374</td><td>0.139</td><td>0.063</td><td>0.795</td></tr><tr><td>89-94</td><td>191</td><td>0.395</td><td>0.403</td><td>0.108</td><td>0.063</td><td>0.795</td></tr><tr><td rowspan="7">L/K</td><td>89</td><td>28</td><td>1.822</td><td>1.592</td><td>0.91</td><td>0.931</td><td>4.488</td></tr><tr><td>90</td><td>42</td><td>1.802</td><td>1.369</td><td>1.361</td><td>0.275</td><td>6.638</td></tr><tr><td>91</td><td>16</td><td>1.674</td><td>1.431</td><td>0.694</td><td>1.07</td><td>3.736</td></tr><tr><td>92</td><td>31</td><td>1.857</td><td>1.62</td><td>0.949</td><td>0.491</td><td>4.361</td></tr><tr><td>93</td><td>43</td><td>2.076</td><td>1.592</td><td>1.872</td><td>0.185</td><td>9.68</td></tr><tr><td>94</td><td>31</td><td>2.792</td><td>1.466</td><td>4.317</td><td>0.378</td><td>19.764</td></tr><tr><td>89-94</td><td>191</td><td>2.025</td><td>1.549</td><td>2.131</td><td>0.185</td><td>19.764</td></tr></table>

Figure 1 IS budget component trends (Mean Values)  
![](/api/attachments/3GFCM8GK/fulltext/images/cfd0b2ee06d84da9e9433e75dd2ae03a9816bca03c354524ac7252c6ba70e590.jpg)

We then repeat the procedure in multiple groups of 25, each time computing a mean of the K-S statistic. This results in a sample of means of the K-S statistic, which, after appealing to the central limit theorem, are distributed normally and can be used to conduct hypothesis tests comparing the mean of this sample to the tabled critical value of the test statistic.

We find that for a sample size of 5, all values of the sample of means exceed the K-S critical value, so we reject the null hypothesis that the distribution of the sample data does not differ from the chi-square distribution. However, for a sample size of 15, only 6% of the distribution exceeds the critical value. Using a simple test of means, we reject the null hypothesis that the population mean equals the critical value at the 95% significance level. Thus, we cannot reject the overall null hypothesis that the distribution of the sample data does not differ from the chi-square distribution at any reasonable level of confidence. Therefore, we can proceed with asymptotic test statistics for each year in our data set.

## 4. Analysis of Data

## 4.1. Regression Results

We first test for homotheticity of the production function using the two alternative specifications discussed in §2. Recall that both the CES and the Cobb-Douglas production functions are homothetic. Thus, retaining the null hypothesis of homotheticity places them in the set of possible production functions.

The results for the first specification (Equation 4), in which the ratio of personnel to hardware budget shares is regressed on a constant and total IS budget, are presented in Table 2. The benefit of the single equation model is that the finite t-test can be used. We observe from Table 2 that, for every year, the test statistic corresponding to the total IS budget variable is too small to reject the null hypothesis of homotheticity at any reasonable level of significance. Thus, the coefficient on IS budget is statistically equal to zero and the null hypothesis of homotheticity is retained. The coefficient of determination is less than 0.05 in all cases, which indicates that the model has little explanatory power, as is expected when it is hypothesized that the coefficient of the single independent variable on the right-hand side is statistically equivalent to zero. The constant term is an estimate of the labor-capital ratio and is similar in magnitude to that plotted in Figure 2—it is roughly constant ranging from 1.77 to 1.88 through 1992, then rises modestly in 1993 and again in 1994.

The second specification (Equation 5) is a system of two equations in which the natural logarithm of hardware and personnel are regressed using SUR on a constant and the natural logarithm of total IS budget. A separate equation is estimated for each year. We also include an industry sector dummy to account for potential differences between manufacturing and service sector firms. Recall that this system shares the ability of the first specification to test for homotheticity. However, from an estimation standpoint, in contrast to the first specification, these test statistics are asymptotic, not finite. The results are presented in Table 3.

Figure 2 Summary Statistics: Mean Personnel to Hardware Ratio  
![](/api/attachments/3GFCM8GK/fulltext/images/50cd56ca9e3a05465beae50420f04508507ff48cd920b7568dbeab9937572c76.jpg)

Table 2 Equation 4 Estimation Results: P/H  C  D • B  e

<table><tr><td></td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td><td>1994</td></tr><tr><td>N</td><td>28</td><td>42</td><td>16</td><td>31</td><td>43</td><td>31</td></tr><tr><td>Constant</td><td>1.88***(10.0)</td><td>1.77***(7.76)</td><td>1.85***(8.38)</td><td>1.88***(10.3)</td><td>2.36***(6.44)</td><td>3.11***(3.38)</td></tr><tr><td>IS budget</td><td>-1.32E-10†(-0.800)</td><td>1.24E-10†(0.404)</td><td>-1.37E-09†(-1.23)</td><td>-7.17E-11†(-0.320)</td><td>-3.01E-09†(-1.23)</td><td>-1.70E-09†(-0.661)</td></tr><tr><td>Adj. R2</td><td>-0.0138</td><td>-0.0208</td><td>0.0333</td><td>-0.0309</td><td>0.0119</td><td>-0.019</td></tr><tr><td>SEE</td><td>0.916</td><td>1.38</td><td>0.682</td><td>0.963</td><td>1.86</td><td>4.36</td></tr></table>

Note: t-statistics are in parentheses.  
\*\*\*Significant at the 99% level.  
†Null hypothesis cannot be rejected at any reasonable level of significance.

All three test statistics for the null hypothesis of homotheticity show that the deviation between the restricted and the unrestricted model for every year in the study is insufficient in magnitude to cast significant doubt on the null hypothesis. Accordingly, we cannot reject the null at any reasonable level of significance and the null hypothesis of homotheticity is retained, an inference that is consistent with the specification of Equation (4). Moreover, we find that the industry sector coefficients are not significant, indicating that, at least in the context of this model, the two groups of firms do not differ. This may be an indication that a finer grouping of firms is necessary to infer such differences. Another feature of Table 3 to note is that in almost every case the constant term is insignificant. The two exceptions are the constant term for the hardware equation in 1991 and 1992, which are negative and significant at the 99% confidence level. Mathematically, we might expect that pairs of constants for each of the first four years would have a difference of roughly 0.6 to be consistent with the results of the estimation of Equation (4).<sup>7</sup> However, the result of insignificant constant terms makes sense intuitively, as zero budget outlay would yield zero allocation to both hardware and personnel.

Table 3 Equation 5 Estimation Results with H : IS Budget (H)  IS Budget (P)

<table><tr><td></td><td>1989</td><td>1990</td><td>1991</td><td>1992</td><td>1993</td><td>1994</td></tr><tr><td>N</td><td>28</td><td>42</td><td>16</td><td>31</td><td>43</td><td> $27\dagger\dagger$ </td></tr><tr><td>Constant (H)</td><td>-2.04(-2.17)</td><td>-0.629(-0.577)</td><td> $-4.35^{***}$ (-3.46)</td><td> $-3.12^{***}$ (-2.91)</td><td>-3.06(-2.06)</td><td>-1.62(-1.49)</td></tr><tr><td>Constant (P)</td><td>-0.517(-1.16)</td><td>-0.183(.288)</td><td>-1.87(-1.33)</td><td>-0.199(-0.30)</td><td>0.586(0.659)</td><td>-1.61(-1.23)</td></tr><tr><td>IS budget (H)</td><td> $1.04^{***}$ (20.6)</td><td> $0.962^{***}$ (16.3)</td><td> $1.16^{***}$ (16.7)</td><td> $1.09^{***}$ (18.6)</td><td> $1.09^{***}$ (13.1)</td><td> $1.01^{***}$ (17.0)</td></tr><tr><td>IS budget (P)</td><td> $0.976^{***}$ (41.3)</td><td> $0.952^{***}$ (27.6)</td><td> $1.05^{***}$ (13.5)</td><td> $0.960^{***}$ (26.5)</td><td> $0.914^{***}$ (18.3)</td><td> $1.03^{***}$ (14.4)</td></tr><tr><td>Sector dummy (H)</td><td>-0.058(-0.371)</td><td>-0.120(-0.740)</td><td>0.0752(0.521)</td><td>0.197(1.40)</td><td>0.0650(0.374)</td><td>-0.112(-0.707)</td></tr><tr><td>Sector dummy (P)</td><td>0.067(0.914)</td><td>0.070(0.744)</td><td>0.064(0.394)</td><td>0.035(0.406)</td><td>-0.037(-0.350)</td><td>-0.167(-0.875)</td></tr><tr><td>Adjusted  $R^2(H)$ </td><td>0.941</td><td>0.868</td><td>0.949</td><td>0.920</td><td>0.803</td><td>0.917</td></tr><tr><td>Adjusted  $R^2(P)$ </td><td>0.985</td><td>0.949</td><td>0.924</td><td>0.959</td><td>0.888</td><td>0.889</td></tr><tr><td>F</td><td> $0.7025\dagger$ </td><td> $0.0095\dagger$ </td><td> $0.3159\dagger$ </td><td> $1.593\dagger$ </td><td> $1.587\dagger$ </td><td> $0.0187\dagger$ </td></tr><tr><td>Critical value</td><td>8.18</td><td>7.47</td><td>12.25</td><td>7.95</td><td>7.44</td><td>8.29</td></tr><tr><td>W</td><td> $1.58\dagger$ </td><td> $0.0164\dagger$ </td><td> $2.15\dagger$ </td><td> $3.489\dagger$ </td><td> $2.75\dagger$ </td><td> $0.0486\dagger$ </td></tr><tr><td>Probability</td><td>0.208</td><td>0.898</td><td>0.143</td><td>0.0618</td><td>0.0970</td><td>0.826</td></tr><tr><td>LR</td><td> $1.539\dagger$ </td><td> $0.0164\dagger$ </td><td> $2.018\dagger$ </td><td> $3.305\dagger$ </td><td> $2.670\dagger$ </td><td> $0.0461\dagger$ </td></tr><tr><td>Critical value</td><td>6.635</td><td>6.635</td><td>6.635</td><td>6.635</td><td>6.635</td><td>6.635</td></tr></table>

t-statistics are in parentheses.  
\*\*\*Significant at 99% level.  
†Null hypothesis cannot be rejected at any reasonable level of significance.  
††Four cases have been dropped due to 4 not ascertained values of IMPSIC.

By retaining the null hypothesis of homotheticity within each year, we have shown that the CES and the CD production functions both potentially describe the technological constraints facing firms. Next, we turn our attention to the third specification, given by Equation (6), which enables us to determine which of the two obtains. This system is an extension of the previous model, with the addition of dummy variables to account for changes in slope and intercept for each year. In this way, we are able to determine if there are no changes in slope from year to year, i.e., the budget shares are constant with time. As explained in §2, evidence of the constancy of budget shares would imply the Cobb-Douglas production function. Once again, we used SUR to estimate Equation (6). Regression results for the third specification are presented in Table 4.

Results are similar to the previous specification. As before, both constant terms are insignificant. In addition, the three test statistics—F, Wald, and Likelihood

Table 4 Equation 6 Estimation Results with ${ \sf H } _ { 0 } \dot { \bf { \cdot } }$ Constant Budget Shares with Time.

<table><tr><td></td><td>Coefficient</td><td>t-statistic</td></tr><tr><td>Constant (H)</td><td>-2.11</td><td>-1.81</td></tr><tr><td>Constant (P)</td><td>-0.435</td><td>-0.597</td></tr><tr><td colspan="3">Intercept Dummies</td></tr><tr><td>1990</td><td>1.345</td><td>0.856</td></tr><tr><td></td><td>0.323</td><td>0.328</td></tr><tr><td>1991</td><td>-2.23</td><td>-0.880</td></tr><tr><td></td><td>-1.44</td><td>-0.914</td></tr><tr><td>1992</td><td>-0.880</td><td>-0.480</td></tr><tr><td></td><td>0.249</td><td>0.217</td></tr><tr><td>1993</td><td>-0.946</td><td>-0.533</td></tr><tr><td></td><td>1.01</td><td>0.914</td></tr><tr><td>1994</td><td>-1.12</td><td>-0.650</td></tr><tr><td></td><td>-1.23</td><td>-1.144</td></tr><tr><td>IS budget (H)</td><td>1.04***</td><td>16.4</td></tr><tr><td>IS budget (P)</td><td>0.974***</td><td>24.6</td></tr><tr><td colspan="3">Slope Dummies</td></tr><tr><td>1990</td><td>-0.0715</td><td>-0.831</td></tr><tr><td></td><td>-0.0239</td><td>-0.445</td></tr><tr><td>1991</td><td>0.127</td><td>0.910</td></tr><tr><td></td><td>0.0791</td><td>0.905</td></tr><tr><td>1992</td><td>0.0500</td><td>0.497</td></tr><tr><td></td><td>-0.0140</td><td>-0.223</td></tr><tr><td>1993</td><td>0.0559</td><td>0.566</td></tr><tr><td></td><td>-0.0615</td><td>-0.996</td></tr><tr><td>1994</td><td>0.0546</td><td>0.578</td></tr><tr><td></td><td>0.0590</td><td>1.000</td></tr><tr><td>N</td><td>191</td><td></td></tr><tr><td>F</td><td>0.4594†</td><td></td></tr><tr><td>Critical value</td><td>2.36</td><td></td></tr><tr><td>W</td><td>8.94†</td><td></td></tr><tr><td>Probability</td><td>0.6277</td><td></td></tr><tr><td>LR</td><td>8.74†</td><td></td></tr><tr><td>Critical Value of  $\chi^{2}_{(11)}$ </td><td>24.7</td><td></td></tr></table>

\*\*\*Significant at 99% level.  
†Null hypothesis cannot be rejected at any reasonable level of significance.

Ratio—are too small to enable rejection of the null hypothesis. Thus, we retain the null hypothesis of constant budget shares, supporting the notion of a constant elasticity of substitution of unity, consistent with the Cobb-Douglas production function. Since the CES production function would yield changing budget shares with time, this key result enables us to rule it out in favor of the Cobb-Douglas production function. Qualitatively, this result means that the ratio of the dollars spent on hardware to those spent on personnel does not change over time.

As the research questions examined in this paper are formulated such that failure to reject hypotheses is consistent with our theory, the statistical power of the tests is an important consideration. Baroudi and Orlikowski (1989) argue that “studies with high power that find insignificance provide strong support for the decision not to reject the null hypothesis.” Consequently, we would like to minimize Type II error so that the likelihood of retaining the null when it is indeed true is as high as possible. However, unlike the uniform nature of the level of significance in the case of the Type I error, statistical power is dependent upon the “effect size,” namely the degree to which the test statistic deviates from the null. The larger the effect size, the larger is the power, as it becomes increasingly easier to detect that the null does not hold. For a given statistical test, given a sample size, the size of the test, and the effect size, Cohen (1988) provides tabled values of power. Alternatively, power curves facilitate the determination of the sensitivity of power with respect to each parameter.

For many common statistical tests such as tests of means, regression coefficients or ANOVA, it is not difficult to construct or find power curves in the literature. In these cases the distribution under the alternate has either the same basic distribution with a different parameter or a noncentral distribution with a well-developed infinite series expansion. For the case of Equation (4), we use power curves as reported in Neter et al. (1985) and Cohen (1988) to determine that our power exceeds 0.75 for medium effect sizes in accordance with recommended guidelines of 0.7—0.8 and greater for “good” power (Cohen 1988).

In contrast, for the case of the two-equation systems of Equations (5) and (6) there are no well-developed tests of power in the literature as distributions under the alternate are analytically intractable and approximation methods are required. Therefore, we conducted a straightforward simulation exercise to shed some light on the power of these models. We generated the dependent variable Q using the CES function with inputs of hardware and personnel budget, estimated the models of Equations (5) and (6), and tested whether the null hypothesis, equivalent to Cobb-Douglas production, is retained. We adjusted the parameter that distinguishes Cobb-Douglas from CES and repeated the previous steps. For each value of this parameter, we replicated the experiment 250 times. Results indicate that for a substitution coefficient close to unity we retain in all cases. As we move further away from unity, rejections become more numerous. In summary, the results of our simulation exercise suggest that it is unlikely that power is problematic for the models of Equations (5) and (6) given the size of our data set. Thus, we can be reasonably confident that the null hypothesis is retained correctly for the models estimated herein.

The result of the estimation and hypothesis testing of Equation (6) is significant from both a managerial as well as a theoretical standpoint. First, it provides strong evidence that in the face of decreasing hardware prices per unit of performance, managers are indeed substituting away from labor in such a way as to maintain constant budget shares over time. Given that the prices of hardware per unit of performance are decreasing rapidly, while those of personnel are increasing (slowly or rapidly) over time, the phenomenon of constant budget shares over time implies that the capital-labor ratio measured as the ratio of units of hardware to units of personnel for any level of output is increasing over time. Thus, a 20% reduction in the price of hardware relative to personnel would be accompanied by roughly a 25%<sup>8</sup> increase in the input ratio of hardware to personnel. An increasing quantity ratio of hardware to personnel indicates the occurrence of substitution in production. Theoretically, this result enhances the validity of the use of the Cobb-Douglas production to model the production of information services.

## 4.2. Limitations

In this section we discuss the limitations of our analysis. We assess the impact of potential changes in technology and in the relative prices of key inputs on the applicability of our results. We also reflect on the implications of modeling assumptions and evaluate other potential explanations for the observed phenomenon.

Our main result is that information systems environments can be characterized by the Cobb-Douglas production function, consistent with the phenomenon of constant budget shares of hardware and personnel over time, even as the unit price of hardware relative to personnel decreases rapidly. Our empirical findings are based on six years of information systems budget data, though similar results are found in aggregatelevel studies over longer periods (Gurbaxani and Mendelson, 1987, 1990, 1992). It is possible that longer time series or more recent data may exhibit different trends. It is useful, therefore, to assess the applicability of our results to information systems environments more generally. For example, we consider whether our results can be expected to hold for new technology platforms or in the face of different price trends.

When changes in production technologies occur, it is indeed possible that the nature of production shifts, so current models may no longer be appropriate. This raises two related issues: Whether production will still be characterized by the Cobb-Douglas production function as technologies evolve, and what the trend in the optimal hardware-personnel ratio will be. It is our considered opinion that the essential trade-offs between hardware and personnel in the information systems environment that lead to their substitutability will continue to exist. This is indicated by the appropriateness of the Cobb-Douglas model not just for the period of this study, but in longer studies at the aggregate level that have included substantial changes in technology platforms.

Accordingly, while we cannot predict the exact form of the production function with certainty, we think that, in the near term, it is unlikely that the production function characterizing the production of information services will have an elasticity of substitution that is significantly different from unity. For example, if future production can be characterized by a CES production function with an elasticity of substitution of 0.95 (1.05) rather than unity, we would expect to see a slowly decreasing (increasing) share of the hardware budget in place of the current phenomenon of constant budget shares. It should be pointed out, however, that even if production continues to be consistent with the Cobb-Douglas production function, it is possible that the parameters of the function will change so that the optimal factor shares are different. Similarly, the overall level of investment can increase or decrease. Qualitatively, as long as the unit prices of hardware continue to decrease at a faster rate than the unit prices of personnel, information systems managers are best served by aggressively pursuing opportunities for substitution.

One important aspect of this analysis is whether the phenomenon of constant budget shares will maintain if price trends are substantially different from those observed in this study, with no significant changes in production technologies. Theoretically, Cobb-Douglas production implies that budget shares are independent of relative prices and the phenomenon ought to continue. However, this result assumes that managers can rapidly adjust their production processes to exploit any given price trend. Clearly, in the short run, a manager is constrained by production commitments, existing technology platforms, and technical possibilities for substitution. When price trends are reasonably predictable, as is the case here, managers can take these into account in their long-range plans. On the other hand, if there is a sudden spike in the price of an input, e.g. personnel, it is possible that the factor shares will increase in favor of personnel in the short run until the production process can be adjusted to once again exploit substitution possibilities.

We have modeled the information systems production process as a function of two inputs, hardware and personnel. Clearly, as discussed above, the production process for information services has a third input— software, which includes software tools and applications software. The substitution of hardware for labor is achieved both directly and through the use of software tools. Conceptually, the acquisition of software tools can be viewed as a form of capital expenditure. Correspondingly, software tools could be modeled as a third input, or by combining the category with hardware. Indeed, in our analysis, systems software that is bundled with hardware is already included in our hardware expenditure category. Purchased application software, on the other hand, can be conceptualized as a substitute for software development personnel.

Unfortunately, the purchased software category in our data does not distinguish between software tools and applications software. However, we do know that applications software constitutes a much larger component of the purchased software category.

We considered combining the purchased software category with personnel. However, since the data also included purchases of software tools, we chose to conduct the analysis with hardware and personnel. For robustness, we repeated the analysis combining purchased software and personnel expenditures; the results were similar. Given the relatively small magnitude of purchased software compared to personnel in the period considered in this study, this finding is not surprising.

Finally, we consider whether the observed budget phenomenon is the outcome of a focus on improving efficiency or is reflective of organizational inertia inherent in a budgeting process. It should be emphasized that information systems budgets have increased substantially in the period of analysis: both hardware and personnel budgets have grown during this time. We believe that this increase gives managers considerable flexibility in changing the relative allocation of the budgets. Given that our results are based on theory that is borne out by the data, we feel confident that the process reflects a focus on maximizing the efficiency of the information services production process.

## 5. Concluding Remarks

This paper determines the nature of production possibilities facing firms in their provision of information services. By using time-series data at the firm level spanning six years, we show that hardware and personnel factor shares are constant with time, implying unitary and constant elasticity of substitution, which is consistent with Cobb-Douglas production. Although previous studies have determined that the Cobb-Douglas production function obtains at the aggregate or economy level, this does not imply that this form of production obtains at the firm level. Thus, the results of this study provide strong justification for the use of the Cobb-Douglas production function in studies of information systems production conducted at the firm level. Moreover, when combined with results of previous studies (Gurbaxani 1996), the additional property of constant returns to scale can justifiably be imposed.

From an information systems research standpoint, the results are important for several reasons. First, production models of the information systems environment provide considerable insight into the nature of the production process. Moreover, these models are often utilized in other studies. Our results provide researchers with a theoretical basis for modeling the production of information services. For example, previous empirical studies of the productivity of information technology at the firm level have assumed Cobb-Douglas production (cf. Hitt and Brynjolfsson 1996). Our results show that their assumption is reasonable and increase our confidence in their results. Had our results indicated that the CES form obtains at the firm level, this would not be the case. Another salient benefit arises due to the ease with which the Cobb-Douglas function is estimated relative to the CES. Thus, the validity of using the Cobb-Douglas function and its relatively simple estimation techniques is substantiated by our results.

From a managerial perspective, these results have several significant implications. Two distinct econometric specifications both show that the production of information services is homothetic over the entire sixyear period analyzed in this study. That is, the optimal hardware-personnel ratio is independent of an organization’s scale. This implies that as IS organizations grow in size, the optimal hardware-personnel budget ratio remains fixed for any given set of input prices. Further, the result of unitary elasticity of substitution implies that a change in the relative price of hardware to personnel is accompanied by a commensurate increase in the quantity of hardware relative to personnel. The optimal labor-capital budget ratio is estimated to be around 1.87, which is consistent with that found in previous studies (Gurbaxani and Mendelson 1987, 1992). This is an extremely useful benchmark for managers who are concerned with the efficient use of information systems resources. In addition, the findings of independence of the factor shares of hardware and personnel from prices and scale are important to managers who must plan the ongoing production of information systems services and allocate their IS budgets to the input factors of production in the face of rapidly changing technologies and prices.

There are several promising avenues for further research. One particularly important line of inquiry would be an examination of the tradeoffs in production processes underlying the core activities that constitute information systems, such as applications development and maintenance, and operations. It would also be extremely interesting and important to ascertain the nature of production for information systems services in a highly distributed environment, as is increasingly the case.

Acknowledgments. We thank Deborah Dunkle for her data collection assistance, Robert Town for his suggestions on the econometrics, and participants in colloquia at UC Irvine and Southern Methodist University for valuable comments. This research has been supported by grants from the U.S. National Science Foundation (IIS-9700316), Computer Science Corporation and IBM Corporation.

## References

Arrow, K. J., H. B. Chenery, B. S. Minhas, R. M. Solow. 1961. Capital—Labor substitution and economic efficiency. Rev. Econom. Statist. 43 225–247.

Banker, R., H. Chang, C. Kemerer. 1994. Evidence on economies of scale in software development. Inform. Software Tech. 36 (5) 275– 282.

Baroudi, J., W. Orlikowski. 1989. The problem of statistical power in MIS research. MIS Quart. 13 (1) 87–106.

Bell, D. 1979. The social framework of the information society. M. L. Dertouzos, J. Moses, eds. The Computer Age: A Twenty-Year Review. MIT Press, Cambridge, MA. 163–211.

Boehm, B. W. 1981. Software Engineering Economics. Prentice Hall, Englewood Cliffs, NJ.

Brynjolfsson, E. 1993. The productivity paradox of information technology: Review and assessment. Comm. ACM 36(12) 66–77.

Cohen, J. 1988. Statistical Power Analysis for the Behavioral Sciences. L. Erlbaum Associates, Hillsdale, NJ.

Danziger, J. N., K. L. Kraemer. 1991. Survey research and multiple operationalism: The URBIS project methodology. K. L. Kraemer, ed. The Information Systems Research Challenge: Survey Research Methods. Harvard Business School Press, Cambridge, MA. 351–372.

FAME Economic Database. Machine-readable magnetic file, 1946– present, FAME, 1978–1994, New York.

Fisher, F. 1971. Aggregate production functions and the explanation of wages. Rev. Econom. Statist. 53(4) 305–311.

Fisher, F. M. 1992. Aggregation: Aggregate production functions and related topics. Harvester Wheatsheaf, New York.

Frank, W. I. 1982. Critical Issues in Software. John Wiley, New York. ——. 1983. The history of myth No. 1. Datamation (May) 252–256.

Green, J. H. A. 1964. Aggregation in Economic Analysis. Princeton University Press, Princeton, NJ.

Greene, W. H. 1993. Econometric Analysis. Macmillan, New York.

Gurbaxani, V. 1990. Managing Information Systems Costs: An Economic Analysis of Hardware-Software Tradeoffs. ICIT Press, Washington, DC.

——, H. Mendelson. 1987. Software and hardware in data processing budgets. IEEE Trans. Software Eng. SE-13 (9) 1010–1017.

—, ——. 1990. An integrative model of information systems spending growth. Inform. Systems Res. 1(1) 23–46.

——, ——. 1992. An empirical analysis of software and hardware spending. Decision Support Systems 8 1–16.

——, K. L. Kraemer, N. Vitalari. 1997. An economic analysis of information systems budgets. Management Sci 43(12) 1745–1755.

Hildebrand, G. H., T. C. Liu. 1965. Manufacturing Production Functions in the United States. New York State School of Industrial Relations, Ithaca, NY.

Hitt, L. M., E. Brynjolfsson. 1996. Productivity, business profitability, and consumer surplus: Three different measures of information technology value. MIS Quart. 121–142

Houthakker, H. S. 1955–56. The Pareto distribution and the Cobb-Douglas production function in activity analysis. Rev. Econom. Stud. XXIII 27–31.

Judge, G. G., R. C. Hill, W. Griffiths, H. Lutkepohl, T. Lee. 1982. Introduction to the Theory and Practice of Econometrics. John Wiley & Sons, New York.

Kmenta, J. 1967. On the estimation of the CES production function. Internat. Econom. Rev. 8 180–189.

Kriebel, C. 1989. Understanding the strategic investment in information technology. K. Laudon, J. Turner, eds. Information Tech-

nology and Management Strategy. Prentice Hall, Englewood Cliffs, NJ.

Lucas, H., J. Sutton. 1977. The stage hypothesis S-curve: Some contradictory evidence. Comm. ACM 20 254–259.

Machlup, F. 1979. Uses, value, and benefits of knowledge. Knowledge: Creation, Diffusion, Utilization 1 (1) 62–81.

Margherio, L. 1998. The Emerging Digital Economy. U.S. Department of Commerce, Washington D.C.

Mendelson, H. 1997. The Economics of Information Systems Management. Draft manuscript, Stanford University Graduate School of Business, Stanford, CA.

Neter J., W. Wasserman, M. Kutner. 1985. Applied Linear Statistical Models: Regression, Analysis of Variance, and Experimental Designs. R. D. Irwin, Homewood, IL.

Nolan, R. L. 1973. Managing the computer resource: A stage hypothesis. Comm. ACM 16 399–405.

Porat, M. U. 1977. The Information Economy. U.S. Government Printing Office, Washington, DC.

Rifkin, G. 1991. Heads that roll if computers fail. New York Times May 14.

Roach, S. 1987. America’s Technology Dilemma: A Profile of the Information Economy. Morgan Stanley, New York.

——. 1994. Best case study of all. Forbes August 29.

Silberberg, E. 1978. The Structure of Economics: A Mathematical Analysis. McGraw-Hill, Hightstown, NJ.

Srivastava, V. K., D. E. Giles. 1987. Seemingly Unrelated Regression Equations Models. Marcel Dekker, Inc. New York, NY.

Thadhani, A. J. 1984. Factors affecting programmer productivity during application development. IBM Systems J. 23 (1) 19–35.

Zellner, A. 1962. An efficient method of estimating seemingly unrelated regressions and tests of aggregation bias. J. Amer. Statist. Assoc. 57 348–368.

Robert Kauffman, Associate Editor. This paper was received on May 1, 1997, and was with the authors 10 months for 1 revision.
