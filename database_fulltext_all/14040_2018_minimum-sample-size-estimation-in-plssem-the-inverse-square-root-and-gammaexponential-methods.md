---
otero_id: 14040
otero_key: "XY8PNKH3"
title: "Minimum sample size estimation in PLS‐SEM: The inverse square root and gamma‐exponential methods"
authors: "Ned Kock; Pierre Hadaya"
year: "2018"
journal: "Information Systems Journal"
doi: "10.1111/isj.12131"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Minimum sample size estimation in PLS-SEM: The inverse square root and gamma-exponential methods

Ned Kock\* & Pierre Hadaya<sup>†</sup>

\*Division of International Business and Technology Studies, Texas A&M International University, 5201 University Boulevard, Laredo, TX 78041, USA, email: nedkock@tamiu.com, and <sup>†</sup>Department of Management and Technology, École des Sciences de la Gestion, Université du Québec à Montréal, PO Box 8888, Downtown Station, Montreal, Quebec H3C 3P8, Canada

Abstract. Partial least squares-based structural equation modelling (PLS-SEM) is extensively used in the <sup>fi</sup>eld of information systems, as well as in many other <sup>fi</sup>elds where multivariate statistical methods are used. One of the most fundamental issues in PLS-SEM is that of minimum sample size estimation. The ‘10-times rule’ has been a favourite because of its simplicity of application, even though it tends to yield imprecise estimates. We propose two related methods, based on mathematical equations, as alternatives for minimum sample size estimation in PLS-SEM: the inverse square root method, and the gamma-exponential method. Based on three Monte Carlo experiments, we demonstrate that both methods are fairly accurate. The inverse square root method is particularly attractive in terms of its simplicity of application. © 2016 John Wiley & Sons Ltd

Keywords: information systems, partial least squares, structural equation modelling, statistical power, Monte Carlo simulation

## INTRODUCTION

The <sup>fi</sup>eld of information systems (IS) is closely linked with the development, software implementation and use of the partial least squares (PLS) technique (Chin, 1998; Chin et al., 2003; Kock, 2010; Wold, 1980). This technique has been extensively used in IS (Bradley et al., 2012; Goodhue et al., 2012), a practice that has extended to other <sup>fi</sup>elds over the years, to analyse path models with variables that are measured indirectly through other variables (Chin, 1998; Hair et al., 2011; 2014; Lohmöller, 1989). These indirectly measured variables are generally known as latent variables (Kline, 1998; Kock & Lynn, 2012). The approach to analysing path models with latent variables is broadly known as structural equation modelling (SEM). Thus, the acronym ‘PLS-SEM’ is used here to refer to SEM using PLS.

One of the most fundamental issues in PLS-SEM is that of minimum sample size estimation. A widely used minimum sample size estimation method in PLS-SEM is the ‘10-times rule method (Hair et al., 2011), which builds on the assumption that the sample size should be greater than 10 times the maximum number of inner or outer model links pointing at any latent variable in the model. While this method’s simplicity of application makes it a favourite among PLS-SEM users, it has been shown in the past to lead to inaccurate estimates (Goodhue et al., 2012).

We propose two related methods, based on mathematical equations, for minimum sample size estimation in PLS-SEM. The <sup>fi</sup>rst method is called the inverse square root method, because it uses the inverse square root of a sample’s size for standard error estimation – an important step in minimum sample size estimation. The second method is called the gamma-exponential method, because it relies on gamma and exponential smoothing function corrections applied to the <sup>fi</sup>rst method. Based on Monte Carlo experiments, we show that both methods are fairly accurate, with the <sup>fi</sup>rst method being also particularly attractive in terms of its simplicity of application.

The methods we propose here should be seen as heuristic methods; that is, as practical methods that are not guaranteed to yield optimal estimates. We believe that they are valuable time-saving tools to be used in the early cyclical phases of research design, and that can be signi<sup>fi</sup>cantly more precise than comparable early-stage research heuristics currently used by researchers. More speci<sup>fi</sup>cally, they are <sup>fi</sup>rst-step methods that researchers can use to address issues related to statistical power and minimum sample size requirements (Cohen, 1988; 1992; Goodhue et al., 2012; Kock, 2016).

We use a unique study in the <sup>fi</sup>eld of IS to illustrate our discussion of minimum sample size estimation in PLS-SEM. The study targeted was authored by Majchrzak, Beath, Lim, and Chin (MBLC), and published in the journal MIS Quarterly in 2005 (Majchrzak et al., 2005). MBLC’s study, which investigated a collaborative approach for IS design, apparently has the distinction of being the PLS-SEM study published in an elite IS research journal with the smallest sample size ever. It used a sample size of 17.

## MBLC’S STUDY

MBLC’s study focused on the impact that a cooperative learning strategy called collaborative elaboration, developed by educational psychologists, had on client learning and ultimately on short- and long-term outcomes in the context of IS design projects. Figure 1 shows the model that they used, with the main results of their analyses. The path estimation algorithm they used was PLS Mode A (Lohmöller, 1989), and the P value calculation method was bootstrapping (Diaconis & Efron, 1983; Efron et al., 2004). This algorithm and P value calculation method are by far the most widely used in PLS-SEM.

The latent variables shown as ovals were measured re<sup>fl</sup>ectively through multiple indicators, primarily on Likert-type scales with 5 points. The question-statements associated with each indicator were answered with respect to project meetings. Cooperative interdependence (CI) was measured based on two indicators and assessed the degree to which the tasks planned for the meeting were in fact accomplished. Collaborative elaboration (CE) was measured based on six indicators and assessed the degree to which clients and developers elaborated on their respective views about their projects. Client learning (CL) was measured based on three indicators and assessed the degree to which clients changed their views about the IS project requirements. Developers’ communication quality (CQ) was measured based on seven indicators and assessed the degree to which developers were good communicators. Long-term outcomes (LO) was measured based on four indicators and assessed the degree to which clients expanded their knowledge about IS and their development. Short-term outcomes (SO) was measured based on four indicators and assessed the degree to which the project would lead to a successful IS implementation.

![](/api/attachments/XY8PNKH3/fulltext/images/eae87e61ea79356882552e4f25705cd2098403ebc95cc7dd6d3af032fe44c6a7.jpg)  
Figure 1. The model in MBLC’s study with results.

MBLC collected data from 17 project teams comprising 68 developers and 17 clients. Each team had four developers and one client. The 17 teams met three times during the project, which lasted 12 weeks, and which culminated with the development of a IS prototype. Immediately following each of the three meetings, the clients were surveyed about the degree of CI exhibited during the meeting, the use of CE by the developers and themselves, as well as the extent to which CL occurred. The assessments of CI, CE and CL were then averaged across the three meetings in order to obtain richer and more stable measures. In addition to the meeting assessments, the clients were also surveyed on the outcomes of the IS design phase (LO and SO) and CQ at the conclusion of the 12-week project.

MBLC’s study was based on a solid theoretical development, and, as mentioned before, was published in the journal MIS Quarterly, which has long been considered a very selective elite academic IS journal. We use their study as a basis to contrast our proposed methods for minimum required sample size estimation against existing comparison methods.

## POWER, EFFECT SIZE AND MINIMUM SAMPLE SIZE

Statistical power (Cohen, 1988; 1992; Goodhue et al., 2012; Kock, 2016; Muthén & Muthén, 2002), often referred to simply as ‘power’, is a statistical test’s probability of avoiding type II errors, or false negatives. Power is often estimated for a particular coef<sup>fi</sup>cient of association and sample size, for samples drawn from a population, at a given signi<sup>fi</sup>cance level (usually $P < . 0 5 )$ . For example, let us consider a PLS-SEM test using PLS Mode A and bootstrapping. Let us assume that such a test is able to recognize a path coef<sup>fi</sup>cient as statistically signi<sup>fi</sup>cant, where the path coef<sup>fi</sup>cient is associated with a ‘real’ effect at the population level of magnitude .2; which would be referred to as the ‘true’ path coef<sup>fi</sup>cient. Let us also assume that the test correctly recognizes the path coef<sup>fi</sup>cient as signi<sup>fi</sup>cant 83% of the time when samples of size 150 are randomly taken from the population. Under these circumstances, we would conclude that the power of the test is 83%, or .83.

The effect size (Cohen, 1988; 1992; Kock, 2014b) is a measure of the magnitude of an effect that is independent of the size of the sample analysed. Two main measures of effect size are commonly used in PLS-SEM. The most widely used is Cohen’s $f ^ { 2 }$ coef<sup>fi</sup>cient (Cohen, 1988; 1992), which is calculated as $\Delta { \sf R } ^ { 2 } / ( 1 - R ^ { 2 } )$ , where $\Delta { \sf R } ^ { 2 }$ is the incremental contribution of a predictor latent variable to the $R ^ { 2 }$ of the criterion latent variable to which it points. The other measure of effect size commonly used in PLS-SEM is the absolute contribution of the predictor latent variable (Kock, 2014b; Mandal et al., 2012), namely the numerator $\Delta { \sf R } ^ { 2 }$ of Cohen’s $f ^ { 2 }$ equation, without the denominator correction. This second measure tends to yield lower results, thus being a more conservative effect size estimate. By convention, effect sizes of 0.02, 0.15 and 0.35 are, respectively, termed small, medium and large (Cohen, 1992; Kock, 2014b).

The minimum sample size at which a PLS-SEM test achieves an acceptable level of power (usually .8) depends on the effect size associated with the path coef<sup>fi</sup>cient under consideration (Cohen, 1988; 1992; Goodhue et al., 2012; Kock, 2014b). The higher is the magnitude of a path coef<sup>fi</sup>cient at the population level, the higher is usually its effect size, and the greater is the probability that a true effect will be properly detected with a small sample. Therefore, strong path coef<sup>fi</sup>cients at the population level, whether they are negative or positive, tend to require very small sample sizes for their proper identi<sup>fi</sup>cation. So, if a researcher knows that all of the path coef<sup>fi</sup>cients of a model will be strong prior to collecting empirical data, leading to large effect sizes, the researcher may consider using a small sample size in a PLS-SEM analysis. As we will see later, we can use the notion of effect size for a general minimum sample size recommendation that does not rely on predictions about path strength.

More often than not, PLS-SEM is presented as being a desirable multivariate data analysis method because of its remarkable ability to achieve acceptable power at very small sample sizes (Hair et al., 2011; 2014). While this may be true for models containing only strong path coef<sup>fi</sup>cients and large effect sizes, it is not true for models with path coef<sup>fi</sup>cients of more modest magnitudes, and certainly not true for models with fairly weak path coef<sup>fi</sup>cients. (At points in our discussion we deviate somewhat from strict technical statistical jargon, for simplicity. Fo example, in the previous sentence, we refer to ‘weak’ path coef<sup>fi</sup>cients, meaning positive or negative path coef<sup>fi</sup>cients whose absolute values are low.) It will be demonstrated here tha

PLS-SEM’s power is consistent with what one would expect from ordinary least squares regression, and probably other methods with similar mathematical underpinnings.

## COMPARISON METHODS FOR MINIMUM SAMPLE SIZE ESTIMATION

In this section, we discuss three methods for minimum sample size estimation in PLS-SEM that we use as a basis for comparison when we evaluate our proposed methods. The <sup>fi</sup>rst method presented here relies on Monte Carlo simulations (Paxton et al., 2001; Robert & Casella, 2013). The second method, the 10-times rule method (Goodhue et al., 2012; Hair et al., 2011), is the most widely used in PLS-SEM, in the <sup>fi</sup>eld of IS as well as other <sup>fi</sup>elds. The third method, the minimum R-squared method, has been proposed by Hair et al. (2014, p. 21) as an alternative to the 10-times rule method.

## The Monte Carlo simulation method

Using the Monte Carlo simulation (Kock, 2016; Paxton et al., 2001; Robert & Casella, 2013) method for minimum sample size estimation in PLS-SEM requires the researcher to set a number of sample size points (e.g. 15, 20, 30 and 40), generate a number of samples (e.g. 1000) for each sample size point, calculate the percentages of samples in which signi<sup>fi</sup>cant effects (e.g. for which $P < . 0 5 )$ were found for each sample size point (the power associated with each sample size) and estimate via interpolation the minimum sample size at which power reaches the desired threshold (i.e. .8). Table 1 illustrates this process through a set of results for four sample size points.

The table shows the power values calculated for each sample size for the CL → LO link in the model used in MBLC’s study, whose path coef<sup>fi</sup>cient was estimated at .397. The process has to be performed individually for each path coef<sup>fi</sup>cient in a PLS-SEM model. From the table, we can see that the power threshold of .8 is reached for a sample size N where $2 0 < N < 3 0$ . Through simple linear interpolation, we calculate the smallest positive integer greater than

$$
2 0 + (3 0 - 2 0) \frac {(. 8 - . 6 4 6)}{(. 8 4 7 - . 6 4 6)}, \text {   which   is   } 2 8.
$$

Thus, the minimum required sample size is estimated via this method to be 28. Note that this method relies on a well-informed choice of sample size points, which in this example are: 15, 20, 30 and 40. Another set of sample size points may not encompass the sample size for which the power threshold of .8 is reached; for example: 100, 200, 300 and 400.

Table 1. The Monte Carlo simulation method

<table><tr><td>N</td><td>Power</td></tr><tr><td>15</td><td>.477</td></tr><tr><td>20</td><td>.646</td></tr><tr><td>30</td><td>.847</td></tr><tr><td>40</td><td>.919</td></tr></table>

© 2016 John Wiley & Sons Ltd, Information Systems Journa

Therefore, the Monte Carlo simulation method often requires two or more simulations. The initial simulations are experimental, to de<sup>fi</sup>ne an appropriate set of sample size points. These would be followed by a <sup>fi</sup>nal simulation, whereby one would estimate via interpolation the minimum sample size at which power reaches the desired threshold of .8.

The samples (e.g. 1000) generated for each sample size point via the Monte Carlo simulation method are based on a population model de<sup>fi</sup>ned by the researcher. The process of building samples in the Monte Carlo simulation method also relies on common factor model assump tions (Kline, 1998; Kock, 2016). This process is explained in more detail in Appendix A. The Monte Carlo simulation method is a complex way by which minimum sample sizes can be determined, and for which technical methodological expertise is required.

As we can see, minimum sample size estimation via the Monte Carlo simulation method may be a very time-consuming alternative, even for experienced methodological researchers with good computer programming skills. Nevertheless, it is a fairly precise method for minimum sample size estimation, and in fact the preferred method for that purpose. As such, we use it to obtain baseline estimates against which other methods are compared.

## The 10-times rule method

The most widely used minimum sample size estimation method in PLS-SEM, in the <sup>fi</sup>eld of IS as well as other <sup>fi</sup>elds, is the ‘10-times rule’ method (Hair et al., 2011; Peng & Lai, 2012). Among the variations of this method, the most commonly seen is based on the rule that the sample size should be greater than 10 times the maximum number of inner or outer model links pointing at any latent variable in the model (Goodhue et al., 2012).

Unlike in the Monte Carlo simulation method, minimum sample size estimation via the 10-times rule method does not depend on the magnitude of the path coef<sup>fi</sup>cients in the model. For example, in the model used in MBLC’s study, the 10-times rule method leads to the minimum sample size estimation of 20, regardless of the strengths of the path coef<sup>fi</sup>cients. This is because the maximum number of model links pointing at any variable in the model is 2, which multiplied by 10 yields 20. As we will see later, this method can lead to grossly inaccurate estimations of minimum required sample size.

## The minimum R-squared method

In their pioneering book on PLS-SEM, Hair et al. (2014, p. 21) discuss an alternative to the 10-times rule for minimum sample size estimation, We refer to this method as the minimum R-squared method’, because the minimum $R ^ { 2 }$ in the model is prominently used for minimum sample size estimation. This method, which builds on Cohen’s (1988; 1992) power tables for least squares regression, relies on a table listing minimum required sample sizes based on three elements.

The <sup>fi</sup>rst element of the minimum R-squared method is the maximum number of arrows pointing at a latent variable (a.k.a. construct) in a model. The second is the signi<sup>fi</sup>cance level used. The third is the minimum $R ^ { 2 }$ in the model. Table 2 is a reduced version of the table presented by Hair et al. (2014, p. 21). This reduced version focuses on the signi<sup>fi</sup>cance level of .05, which is the most commonly used signi<sup>fi</sup>cance level in the <sup>fi</sup>eld of IS, and assumes tha power is set at .8.

For example, in the model used in MBLC’s study, the maximum number of arrows pointing at a latent variable is 2, and the minimum $R ^ { 2 }$ in the model is .549. There is no cell in the table for the minimum R-squared method for which these two values intersect, but the closest cell shows a minimum sample size of 33, which we use as the estimate. As we can see, this method appears to be an improvement over the 10-times rule method, as it takes as an input at least one additional element beyond the network of links in the model. However, this method (i.e. the minimum R-squared method) can also lead to grossly inaccurate estimations o minimum required sample size, which we will see later.

## OUR PROPOSED METHODS FOR MINIMUM SAMPLE SIZE ESTIMATION

In this section, we discuss two related methods, based on mathematical equations, for minimum sample size estimation in PLS-SEM. Neither method relies on Monte Carlo simulations or on elements that make up the 10 times rule or the minimum R-squared methods. The <sup>fi</sup>rst method, called the inverse square root method, uses the inverse square root of a sample’s size for standard error estimation – hence its name. The second method, called the gamma-exponential method, relies on gamma and exponential smoothing function corrections applied to the standard error estimation used in the <sup>fi</sup>rst method.

## The inverse square root method

Whenever one or more researchers analyse samples taken from a population using PLS-SEM, each analysis generates various path coef<sup>fi</sup>cients. Each path coef<sup>fi</sup>cient (β) will have a standard error (S) associated with it. If we plot the distribution of the ratio $\beta / S ,$ , also indicating the location of a critical T ratio (Kock, 2015; Weakliem, 2016) for a speci<sup>fi</sup>c signi<sup>fi</sup>cance level chosen, we will obtain a graph that will have the general shape shown in Figure 2. For each instance, where the ratio $\beta / S$ surpasses the critical T ratio, the effect associated with the path coef<sup>fi</sup>cient $\beta$ will be correctly deemed as statistically signi<sup>fi</sup>cantly. This assumes that the path coef<sup>fi</sup>cient refers to an effect that exists at the population level – a ‘true’ effect.

Table 2. Table for the minimum R-squared method

<table><tr><td rowspan="2">Maximum number of arrows pointing at a construct</td><td colspan="4">Minimum  $R^{2}$  in the model</td></tr><tr><td>.10</td><td>.25</td><td>.50</td><td>.75</td></tr><tr><td>2</td><td>110</td><td>52</td><td>33</td><td>26</td></tr><tr><td>3</td><td>124</td><td>59</td><td>38</td><td>30</td></tr><tr><td>4</td><td>137</td><td>65</td><td>42</td><td>33</td></tr><tr><td>5</td><td>147</td><td>70</td><td>45</td><td>36</td></tr><tr><td>6</td><td>157</td><td>75</td><td>48</td><td>39</td></tr><tr><td>7</td><td>166</td><td>80</td><td>51</td><td>41</td></tr><tr><td>8</td><td>174</td><td>84</td><td>54</td><td>44</td></tr><tr><td>9</td><td>181</td><td>88</td><td>57</td><td>46</td></tr><tr><td>10</td><td>189</td><td>91</td><td>59</td><td>48</td></tr></table>

© 2016 John Wiley & Sons Ltd, Information Systems Journa

The magnitude of the ratio $\beta / S$ increases with increases in the magnitude of the path coef <sup>fi</sup>cient $\beta$ and decreases in the standard error S. This standard error decreases with increases in sample size, as will be seen shortly bow. Therefore, with increases in the magnitude of the path coef<sup>fi</sup>cient and of the sample size analysed, the probability that the ratio $\beta / S$ will surpass the critical T ratio will increase. As result, the likelihood that an effect that does exist at the population level will be mistakenly rejected will decrease. In other words, the power of the test will increase.

As we can see from the <sup>fi</sup>gure, the power of a test associated with a given path coef<sup>fi</sup>cient for which a sign has been hypothesized can be de<sup>fi</sup>ned as the probability that the ratio $\vert \beta \vert / S$ will be greater than the critical T ratio for a speci<sup>fi</sup>c signi<sup>fi</sup>cance level chosen (Cohen, 1988; Goodhue et al., 2012; Kock, 2015). Here $| \beta |$ is the absolute value of $\beta ,$ as a path coef<sup>fi</sup>cient strength’s in-<sup>fl</sup>uence on power is exerted whether the coef<sup>fi</sup>cient is positive or negative. The signi<sup>fi</sup>cance level normally chosen in the <sup>fi</sup>eld of IS is .05 (i.e. $P { < } . 0 5 )$ , for which the critical T ratio can be denoted as $\mathsf { T } _ { . 0 5 }$ . This can be expressed mathematically as follows.

$$
W = P \left(\frac {| \beta |}{S} > \mathrm{T} _ {. 0 5}\right).\tag{1}
$$

Statistical power is denoted as W in 1, and $P ( \cdot )$ is the probability function. If we set power to be above a given level, most commonly .8 in IS research, the above can be expressed using a cumulative probability function $\Phi ( \cdot )$ for the standard normal distribution. Assuming that path co ef<sup>fi</sup>cients are normally distributed, we can say that power will be greater than .8 when the cumu lative distribution function for the standard normal distribution indicated in 2 is greater than .8.

![](/api/attachments/XY8PNKH3/fulltext/images/210038c5ab8ca03635c2b8d6bc91b6a2f910331c76912abfc60badc2982d982c.jpg)  
Note: T = critical T ratio for a specific significance level chosen.  
Figure 2. Distribution of the ratio $\beta / S .$ . Note: T = critical T ratio for a speci<sup>fi</sup>c signi<sup>fi</sup>cance level chosen.

$$
\Phi \left(\frac {| \beta |}{S} - T _ {. 0 5}\right) >. 8.\tag{2}
$$

The assumption that path coef<sup>fi</sup>cients are normally distributed generally holds for PLS-SEM, because coef<sup>fi</sup>cients calculated based on sample sets taken randomly from a population tend to be distributed in conformity with the central limit theorem (Kipnis & Varadhan, 1986; Miller & Wichern, 1977).

Taking 2 as a basis, we obtain 3 in terms of the standardized score associated with the value .8 of the cumulative distribution function for the normal distribution $( z _ { . 8 } . )$ . To obtain 3 we also take into consideration the property that $\top _ { . 0 5 } = z _ { . 9 5 }$

$$
\begin{array}{l}\frac {| \beta |}{S} - T _ {. 0 5} > z. _ {8} \rightarrow\\\frac {| \beta |}{S} > T _ {. 0 5} + z. _ {8} \rightarrow\\\frac {| \beta |}{S} > z. _ {9 5} + z. _ {8}.\end{array}\tag{3}
$$

Any given z-score $z _ { x }$ can be calculated based on a standard normal distribution, which is a normal distribution with a mean of 0 and a standard deviation of 1. The score is a value associated with the probability x that a random variable takes on a value that is equal to or less than $z _ { x } .$ In MATLAB, it is obtained using the function norminv(x,0,1). In Excel, it is obtained using the function NORM ${ \mathsf { N V } } ( x , 0 , 1 )$ or the function NORMSINV(x).

An estimate $\hat { S }$ of the true standard error (S) can be produced through 4. This estimate lends the name to the method presented here, the inverse square root method, and is known to be biassed (Gurland & Tripathi, 1971; Kock, 2014a), consistently underestimating the corresponding true value at very small samples $( \mathsf { i } . \mathsf { e } . \ 1 < N \leq 1 0 )$ , and consistently overestimating it at greater sample sizes $( \mathsf { i } . \mathsf { e } . \ N > 1 0 )$ . Shortly, we will discuss two approaches to correct this bias, which are combined in our second proposed minimum sample size estimation method, the gamma-exponential method.

$$
\hat {S} = \frac {1}{\sqrt {N}}.\tag{4}
$$

Using the Excel function NORMSINV(x), we obtain the values for $z _ { . 9 5 }$ and $z _ { . 8 } ,$ or NORMSINV(.95) and NORMSINV(.8), which are, respectively, 1.645 and 0.842. The sum $Z _ { . 9 5 } + Z _ { . 8 }$ is thus 2.486. Combining 3 and 4, with $| \beta | _ { m i n }$ replacing |β| and representing the absolute value of the statistically signi<sup>fi</sup>cant path coef<sup>fi</sup>cient with the minimum magnitude in the model, we then have:

© 2016 John Wiley & Sons Ltd, Information Systems Journa

$$
| \beta | _ {m i n} \sqrt {\hat {N}} > z. 9 5 + z. 8 \rightarrow \quad \hat {N} > \left(\frac {z . 9 5 + z . 8}{| \beta | _ {m i n}}\right) ^ {2} \rightarrow \quad \hat {N} > \left(\frac {2 . 4 8 6}{| \beta | _ {m i n}}\right) ^ {2}.\tag{5}
$$

Based on our proposed inverse square root method, the minimum sample size is estimated as the smallest positive integer that satis<sup>fi</sup>es 5. As such, it can be calculated by rounding the result of the calculation of the right side of the equation to the next integer. In MATLAB, it can be obtained using the function ceil((2.486/bmin)^2), where bmin is a variable that stores the value of $| \beta | _ { m i n }$ . In Excel, it can be obtained using the function ROUNDUP((2.486/bmin)^2,0), where bmin is the name of a cell that stores the value of $| \beta | _ { m i n }$

## The gamma-exponential method

As we noted earlier, our estimate Ŝ of the true standard error (S), obtained through the formula $1 / \sqrt { N }$ , is known to be biassed. A classic gamma function correction of the bias for very small sample sizes $( \mathfrak { i } . \Theta . \ 1 < N \le 1 0 )$ was proposed by Gurland & Tripathi (1971):

$$
S = \frac {1}{c \sqrt {N}},
$$

where

$$
c = \sqrt {\frac {N - 1}{2}} \frac {\Gamma \left(\frac {N - 1}{2}\right)}{\Gamma \left(\frac {N}{2}\right)}, \text { and } \Gamma (\cdot) \text { is   the   gamma   function. }
$$

With the gamma function correction proposed by Gurland & Tripathi’s (1971), the resulting equation 6 to obtain the minimum required sample size  becomes more complex. This equa: tion can be solved by means of a computer programme that starts with $\hat { N } = 1$ and progressive increments the value of N<sup>^</sup> to 2, 3 etc. until the smallest positive integer that satis<sup>fi</sup>es the equation is obtained. In MATLAB, the value of $\Gamma ( x )$ is obtained using the function gamma(x). In Excel, it is obtained using the two-function formula EXP(GAMMALN(x + 1)).

$$
\left| \beta \right| _ {\min} \sqrt {\hat {N}} \sqrt {\frac {\hat {N} - 1}{2}} \frac {\Gamma \left(\frac {\hat {N} - 1}{2}\right)}{\Gamma \left(\frac {\hat {N}}{2}\right)} > 2. 4 8 6.\tag{6}
$$

The gamma function correction equation has no effect, in terms of minimum required sample size estimation, for $N > 1 0$ . The reason for this is that the correction coef<sup>fi</sup>cient c quickly con verges to 1 for $N > 1 0$ . An exponential smoothing function correction of the standard error bias was proposed and validated by Kock (2014a) in the context of PLS-SEM for sample sizes greater than those covered by the gamma function correction (i.e. N > 10):

$$
\tilde {S} = \frac {1}{\sqrt {N}} e ^ {- \left(\frac {e | \beta |}{\sqrt {N}}\right)}.
$$

With this exponential smoothing function correction, the equation 7 to obtain the minimum required sample size N̂ also ends up being more complex. As with the gamma function correc tion equation, this equation can be solved with a computer programme that starts with N̂ 1 and progressive increments its value to 2, 3 etc. until the smallest positive integer that satis<sup>fi</sup>es the equation is obtained. In MATLAB, the value of ${ \boldsymbol { \theta } } ^ { x }$ is obtained using the function exp(x). In Excel, it is obtained using the function $\mathsf { E X P } ( x )$

$$
| \beta | _ {m i n} \sqrt {\hat {N}} e ^ {\left(\frac {e | \beta | _ {m i n}}{\sqrt {N}}\right)} > 2. 4 8 6.\tag{7}
$$

We developed an Excel spreadsheet with Visual Basic code, discussed in Appendix B, to ob tain corrected estimates based on equations 6 and 7. This enabled us to implement the gamma-exponential method, by combining gamma and exponential smoothing function corrections applied to the standard error estimation used in the inverse square root method. Therefore, the gamma-exponential method can be seen as a re<sup>fi</sup>nement of the inverse square root method.

## MONTE CARLO EXPERIMENTS

In this section, we discuss three Monte Carlo experiments, which we have implemented with MATLAB. Both use the Monte Carlo simulation approach discussed in Appendix A. In these Monte Carlo experiments, 1000 samples were created and analysed for each sample size. Each Monte Carlo experiment was conducted at least twice; i.e. at least two instances of each Monte Carlo experiment were conducted, with all of the corresponding results compiled and summarized. The results obtained across different instances of the same Monte Carlo experiment were virtually identical. This consistency in the results was primarily because of the large number of samples (i.e. 1000) created and analysed for each sample size.

The <sup>fi</sup>rst Monte Carlo experiment builds on the results from MBLC’s study to develop its population model. As such, the true path coef<sup>fi</sup>cients are rather strong, which, as will be seen, lead to small minimum sample size estimates. To illustrate the in<sup>fl</sup>uence of the path coef<sup>fi</sup>cients magnitudes on minimum sample size estimation, the second Monte Carlo experiment uses the paths of the model in MBLC’s study, but with all path coef<sup>fi</sup>cients reduced by .25. The third Monte Carlo experiment has path coef<sup>fi</sup>cients varying from .1 to .35, thus further illustrating the performance of the various minimum sample size estimation methods under more extreme conditions (e.g. a very small path coef<sup>fi</sup>cient) than the two previous experiments. In these Monte Carlo experiments, the PLS-SEM analyses use the PLS Mode A algorithm and the bootstrapping method for P value estimation; these are discussed in appendices C and D.

## First Monte Carlo experiment

Figures 3 to 5 show graphs relating power to sample size for each of the paths of the model in MBLC’s study. The sample size points shown (i.e. 15, 20 … 50) were chosen to allow us to es timate the minimum required sample size, as well as to illustrate how the power values vary based on sample size and path coef<sup>fi</sup>cient magnitude.

![](/api/attachments/XY8PNKH3/fulltext/images/574e1293730d27c6934d27f7b0c84dadc848fed83369afe889bb0241a76055ca.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/76ad535b28728340175e70e3ddd9af39aaf5c80df5f7cb31e2d791cc083b3040.jpg)  
Figure 3. Paths CI → CL (left, $\beta _ { p } = . 5 0 6 )$ and CE → CL (right, $\beta _ { p } = . 5 3 6 )$ ).

![](/api/attachments/XY8PNKH3/fulltext/images/f759604e9b5ad26047253c5f413ef29e35477ea2795d2e9aa01ba56c519e022c.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/b6bc9a5ad38879bc7f9484459f2221985be3147f9705106a58184de6c3ae3c0b.jpg)  
Figure 4. Paths CL → LO (left, $\beta _ { p } = . 3 9 7 )$ and $\mathsf { C Q } \to \mathsf { L O }$ (right, $\beta _ { p } = . 5 2 5 )$ ).

![](/api/attachments/XY8PNKH3/fulltext/images/c1601b81d430c1135c4fdcd6a253845e1bb06f5e37e25ec4a761a509a1296f69.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/c89d6d1baa94195205f60a4b382e19b3876f319cad9e87feb34f6d7c07f434bc.jpg)  
Figure 5. Paths $\mathsf { C L } \to \mathsf { S O }$ (left, $\beta _ { p } = . 4 3 5 )$ and $\mathsf { C Q } \to \mathsf { S O }$ (right, $\beta _ { p } = . 4 9 8 )$ ).

The population model had the same coef<sup>fi</sup>cients as those in MBLC’s study’s results. The power values shown are the percentages of path coef<sup>fi</sup>cients for which a signi<sup>fi</sup>cant effec was found, based on the signi<sup>fi</sup>cance level of .05 (i.e. P <.05) normally chosen in the <sup>fi</sup>eld of IS. The P value calculation method used was bootstrapping with 500 resamples.

As we can see, power values varied based on sample size and path coef<sup>fi</sup>cient magnitude. Power values increased as both sample sizes and path coef<sup>fi</sup>cient strengths increased. Therefore, the minimum required sample size for the entire PLS-SEM analysis was the one at which the power of .8 was achieved for the path with the smallest magnitude, namely CL → LO $( \beta _ { p } = . 3 9 7 )$ , indicated in the respective graph. Based on the graphs above, the minimum required sample size for the entire PLS-SEM analysis was estimated based on the Monte Carlo simulation to be 28.

Table 3 shows the estimates of the minimum required sample size based on the Monte Carlo simulation, the 10-times rule, as well as the R-squared, inverse square root and gammaexponential methods. The Monte Carlo simulation estimate of 28 stands in for the true minimum required sample size. As we can see, the closest estimate to this true minimum required sample size is the gamma-exponential method estimate of 26.

Arguably, all of the methods, except for the 10-times rule, led to minimum sample size estimates that would not lead to power levels drastically below the acceptable threshold. If used in an empirical study, the 10-times rule would lead to a sample size whose power would be ap proximately .65, which is well below the threshold of .8 for the .05 signi<sup>fi</sup>cance level. The gamma-exponential method would lead to a small underestimation: a sample size whose power would be just under .8 for the .05 signi<sup>fi</sup>cance level.

If used in an empirical study, the minimum R-squared and inverse square root methods would lead to relatively small and ‘harmless’ overestimations of the true minimum required sample size needed. Arguably, these overestimations would be harmless because they would lead to power values greater than the threshold of .8 for the .05 signi<sup>fi</sup>cance level – that is, more statistical power – without placing a signi<sup>fi</sup>cant demand on researchers for sample sizes much larger than necessary.

## Second Monte Carlo experiment

Figures 6 to 8 show graphs relating power to sample size for each of the paths of the model in MBLC’s study, but with all path coef<sup>fi</sup>cients reduced by .25. As with the <sup>fi</sup>rst Monte Carlo experiment, the sample size points shown (i.e. 100, 200 … 400) were chosen to allow us to estimate

Table 3. Performance of different estimation methods

<table><tr><td>Method</td><td>Minimum required sample size</td></tr><tr><td>Monte Carlo simulation</td><td>28</td></tr><tr><td>10-times rule</td><td>20</td></tr><tr><td>Minimum R-squared</td><td>33</td></tr><tr><td>Inverse square root</td><td>40</td></tr><tr><td>Gamma-exponential</td><td>26</td></tr></table>

![](/api/attachments/XY8PNKH3/fulltext/images/71c73e8089d39eb44f10d6ba8d8636f442d78ce618c05ced6fd723b445f0ac53.jpg)  
Figure 6. Paths CI → CL (left, $\beta _ { p } = . 2 5 6 )$ and ${ \mathsf { C E } } \to { \mathsf { C L } }$ (right, $\beta _ { p } = . 2 8 6 )$

![](/api/attachments/XY8PNKH3/fulltext/images/5d210857ca91dcabde86427c956c0f6d97426fbd9faee5926aaabbb51116abc6.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/e376c2d1b7454af0322d2c6c368bfdf27be400dbfac185b7c7f2a22267e72024.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/33496d2cc3187c6519becaa89c822673695005819db395f4c9e03b7f67e5c278.jpg)  
Figure 7. Paths CL → LO (left, $\beta _ { p } = . 1 4 7 )$ and CQ → LO (right, $\beta _ { p } = . 2 7 5 )$ .

![](/api/attachments/XY8PNKH3/fulltext/images/1e834abecb46ae4c3f5567960f3928fc70ef8cd06f790b0c04985dbf38b483d5.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/5c7e271165ea12d193c7a7b888a8d58df37f5bf35699988a99a621b91d7ded24.jpg)  
Figure 8. Paths CL → SO (left, $\beta _ { p } = . 1 8 5 )$ and $\mathsf { C Q } \to \mathsf { S O }$ (right, $\beta _ { p } = . 2 4 8 )$ ).

the minimum required sample size, as well as to illustrate how the power values vary based on sample size and path coef<sup>fi</sup>cient magnitude.

Unlike the population model used in the <sup>fi</sup>rst Monte Carlo experiment, here the coef<sup>fi</sup>cients are much smaller than those in MBLC’s study’s results. Except for this key difference, the pro cedures to generate the numbers on the graphs are the same as those in the <sup>fi</sup>rst Monte Carlo experiment. The power values shown are the percentages of path coef<sup>fi</sup>cients for which a signi<sup>fi</sup>cant effect was found, based on the signi<sup>fi</sup>cance level of .05. As before, P values were calculated through bootstrapping with 500 resamples

Consistently with the <sup>fi</sup>rst Monte Carlo experiment, power values varied based on sample size and path coef<sup>fi</sup>cient magnitude, increasing with both sample size and path coef<sup>fi</sup>cient magnitude. As expected, the minimum required sample size for the entire PLS-SEM analysis was the one at which the power of .8 was achieved for the path with the smallest magnitude, namely ${ \mathsf { C L } } \to { \mathsf { L O } } \ ( \beta _ { p } = . 1 4 7 )$ . Based on the graphs above, the minimum required sample size for the entire PLS-SEM analysis was estimated to be 265 based on the Monte Carlo simulation.

Table 4 shows the estimates of the minimum required sample size based on the Monte Carlo simulation, the 10-times rule, as well as the minimum R-squared, inverse square root and gamma-exponential methods. The minimum R-squared obtained in this second experimen was slightly lower than .1, which was used to produce the estimate using the minimum R-squared method. As before, the Monte Carlo simulation estimate of 265 stands in for the true minimum required sample size. Again, as before, the closest estimate to this true minimum required sample size is the gamma-exponential method estimate of 273.

Here we can see that the 10-times rule and the R-squared method estimates were way off mark, signi<sup>fi</sup>cantly underestimating the true minimum required sample size. This was particularly true of the 10-times rule. If used in an empirical study, either of these methods would lead to sample sizes whose power would be well below the threshold of .8 for the .05 signi<sup>fi</sup>cance level.

When used in an empirical study, the gamma-exponential and inverse square root methods would lead to relatively small and harmless overestimations of the true minimum required sample size needed. The overestimations would lead to power values greater than the threshold of .8 for the .05 signi<sup>fi</sup>cance level, arguably without placing a signi<sup>fi</sup>cant demand on researchers for sample sizes much larger than necessary. Even the estimate of 287, obtained via the inverse square root method, would require only 22 additional data points beyond the 265 necessary for the power threshold of .8 to be achieved.

## Third Monte Carlo experiment

Figures 9 to 11 show graphs relating power to sample size for each of the paths of the model in MBLC’s study, but with the path coef<sup>fi</sup>cients starting at the very small value of .1 and incrementally going up to .35. The sample size points shown (30, 50, 100 … 700) were chosen to allow us to estimate power values and the minimum required sample size under somewhat extreme conditions, starting with a very small path coef<sup>fi</sup>cient of .1 and with a very small sample size of

Table 4. Performance of different estimation methods

<table><tr><td>Method</td><td>Minimum required sample size</td></tr><tr><td>Monte Carlo simulation</td><td>265</td></tr><tr><td>10-times rule</td><td>20</td></tr><tr><td>Minimum R-squared</td><td>110</td></tr><tr><td>Inverse square root</td><td>287</td></tr><tr><td>Gamma-exponential</td><td>273</td></tr></table>

![](/api/attachments/XY8PNKH3/fulltext/images/f38afbb2de1b27d159d333878f847a8455e2dc440bd5563ef9a3364f5b0b6c36.jpg)  
Figure 9. Paths CI → CL (left, $\beta _ { p } = . 1 0 0 )$ and ${ \mathsf { C E } } \to { \mathsf { C L } }$ (right, $\beta _ { p } = . 1 5 0 )$ ).

![](/api/attachments/XY8PNKH3/fulltext/images/3966dc414c934f055aeeec7dd601f1c990134e11d7b03f6bbd593e8512267682.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/deaccea46f01d11b5a25add37d930ad0d490e01f087c1893a99ed3c571ca16e7.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/bbf8bbb4b7ab5ea7a0f41331545e451c0ae29ca9026fce0bbb63451aff7af4f7.jpg)  
Figure 10. Paths CL → LO (left, $\beta _ { p } = . 2 0 0 )$ and $\mathsf { C Q } \to \mathsf { L O }$ (right, $\beta _ { p } = . 2 5 0 )$

![](/api/attachments/XY8PNKH3/fulltext/images/3323fcc5c18b281f5357bad7b24f9745b8056fae0e563dbdc29b25c74b1dc2f2.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/9be48e3af36da0d16fb132d34864cb1bd22d64ac77e8d506d2338d9f4a85356c.jpg)  
Figure 11. Paths CL → SO (left, $\beta _ { p } = . 3 0 0 )$ and CQ → SO (right, $\beta _ { p } = . 3 5 0 )$

30. The sample size points were also chosen to illustrate how the power values incrementally grow based on path coef<sup>fi</sup>cient magnitude, as well as based on sample size.

We can see from the graphs above, as expected from our mathematical reasoning presented earlier, that the path with the smallest magnitude ${ \mathsf { C l } } \to { \mathsf { C L } } \left( \beta _ { p } = . 1 \right)$ is the one that drove up the minimum required sample size. We also notice something interesting with this path, and also with the small path ${ \mathsf { C E } } \to { \mathsf { C L } } \ ( \beta _ { p } = . 1 5 )$ : a slightly anomalous behaviour in the area involving the <sup>fi</sup>rst two sample size points (i.e. 30 and 50). It seems that at these small sample sizes the power values for the two weakest paths are a bit higher than they should be. The reason for this is that the PLS Mode A algorithm we used in our PLS-SEM analyses tends to overestimate very weak paths at very small samples, by ‘capitalizing on error’ (see, e.g. Goodhue et al., 2007).

Capitalization on error is illustrated by the average path coef<sup>fi</sup>cient estimated in our Monte Carlo simulation for the path CI → CL $( \beta _ { p } = . 1 )$ at sample size 30, which was .108. This value is a bit higher than the true value of .1. This phenomenon may be at the very source of the mistaken belief that PLS-SEM has a remarkable ability to achieve acceptable power at very small sample sizes (Hair et al., 2011; 2014). Our results show that, even with capitalization on error, the power achieved for the small path CI → CL $( \beta _ { p } = . 1 )$ was too low at the small sample size of 30. It was lower than .2, and thus well below the generally acceptable level of .8 for $P < . 0 5$ (Cohen, 1988; 1992; Goodhue et al., 2012; Kock, 2016).

Table 5 shows the estimates of the minimum required sample size based on the various methods used in the two previous Monte Carlo experiments. The minimum R-squared obtained in this third experiment was much lower than .1, which was used to produce the estimate using the minimum R-squared method. As with the two previous experiments, the Monte Carlo simu lation estimate of 599 stands in for the true minimum required sample size. Again, as before, the closest estimate to this true minimum required sample size is the gamma-exponential method estimate of 605.

As with the second Monte Carlo experiment, we can see that the 10-times rule and the R-squared method estimates were again way off mark, signi<sup>fi</sup>cantly underestimating the true minimum required sample size. If used in an empirical study, either of these methods would lead to sample sizes whose power would be unacceptably low: well below the threshold of .8 for the .05 signi<sup>fi</sup>cance level. Even the sample size of 110 obtained through the minimum R-squared method would lead to a power level below .3, and this sample size is considerably greater than the sample size of 20 suggested by the 10-times rule. We can also see that the inverse square root and gamma-exponential methods yielded minimum sample size estimates that are fairly consistent with the one obtained via the Monte Carlo simulation method.

## Additional Monte Carlo experiments

As part of our ongoing research on minimum required sample sizes in PLS-SEM, we have conducted a number of additional Monte Carlo experiments. These experiments included a variety of models, some simpler and others more complex than the model in MBLC’s study. The result of these Monte Carlo experiments have been largely consistent with those of the three experi ments presented above.

Table 5. Performance of different estimation methods

<table><tr><td>Method</td><td>Minimum required sample size</td></tr><tr><td>Monte Carlo simulation</td><td>599</td></tr><tr><td>10-times rule</td><td>20</td></tr><tr><td>Minimum R-squared</td><td>110</td></tr><tr><td>Inverse square root</td><td>619</td></tr><tr><td>Gamma-exponential</td><td>605</td></tr></table>

Several of the additional experiments that we have conducted included non-normal data. In some cases, the level of non-normality was considerable; e.g. datasets created to have skewness and excess kurtosis values of 2.828 and 12, respectively. Consistently with past claims and related research (Chin, 1998; Hair et al., 2011; 2014; Kock, 2016), we found PLS-SEM to be fairly robust to deviations from normality, to the point that the Monte Carlo experiments yielded results that were virtually the same with both normal and non-normal data. Further analysis suggested that the underlying reasons for this are that least squares regression methods in general are quite robust to deviations from normality, and that so is bootstrapping. This is explained in more detail in Appendix E, with examples.

## DISCUSSION

In this section, we discuss several issues in connection with minimum sample size estimation. We also provide several recommendations, primarily aimed at PLS-SEM users who are not methodological researchers. Among the issues addressed in this section are the method that arguably should be used for minimum sample size estimation, and minimum sample size estimation after and before data collection and analysis.

## Which method should one use for minimum sample size estimation?

It is noteworthy that the gamma-exponential method, which is supposed to improve upon the precision of the inverse square root method, appears to: (a) slightly underestimate the minimum require sample size for small samples (e.g. $1 5 { \geq } N < 5 0 )$ ; and (b) slightly overestimate it for larger samples (e.g. $N \geq 1 0 0 )$ . Does this mean that the gamma-exponential method yields incorrect estimates?

To answer this question, we have also calculated the actual standard errors, as the actual standard deviations of the path coef<sup>fi</sup>cients, in the Monte Carlo experiments. These were calculated in addition to the standard error estimates yielded by bootstrapping and the gammaexponential method corrections. As it turns out, the standard error estimates yielded by the gamma-exponential method corrections were closer to the actual values than those generated by bootstrapping.

For example, for the path CL → LO in the <sup>fi</sup>rst Monte Carlo experiment $( \beta _ { p } = . 3 9 7 )$ at $N = 1 5$ the actual standard error was .181, the bootstrapping estimate was .225 and the gammaexponential method estimate was .2. For the same path CL → LO in the second Monte Carlo experiment $( \beta _ { p } = . 1 4 7 )$ at $N = 1 0 0$ , the actual standard error was .096, the bootstrapping esti mate was .093 and the gamma-exponential method estimate was .096. These are consistent with the patterns of apparent imprecision that we observed, namely the slight underestimations and overestimations at different sample sizes.

In other words, the gamma-exponential method seems to yield the most precise estimates of standard errors, and thus minimum sample size estimates that are closest to the true values than any of the other methods discussed in this paper. This applies even to the Monte Carlo simulation method, because our implementation of this method relied on bootstrapping, which is the standard for PLS-SEM. This implementation decision was not made by mistake, as we attempted to mimic actual analyses conducted by empirical researchers using PLS-SEM. It would be impossible to estimate actual standard errors in empirical PLS-SEM studies, because the true population values are not known.

Nevertheless, the gamma-exponential method is much more complex in its application (relying on a computer programme) than the inverse square root method. The latter, in addition to being simpler (relying on a simple equation), is also fairly precise, leading to smal overestimations that place light demands on researchers in terms of data points over the true minimum sample sizes required. Furthermore, the inverse square root method is ‘safe’ in its slight imprecision, as it seems to always lead to small overestimations of the minimum sample sizes required.

Given the above, our recommendation for PLS-SEM users who are not methodological researchers is that they use the inverse square root method for minimum sample size estimation. They will be generating estimates that are both fairly precise and safe (slight overestimations), with both normal and non-normal data. Their estimates will always be a little larger than the true minimum sample sizes required, but not by much.

## Minimum sample size estimation after data collection and analysis

When minimum sample size estimation is conducted after data collection and analysis, its results can be used as a basis for additional data collection, as well as adjustments in the analysis and in the hypothesis testing assumptions. Minimum sample size estimation after data collection and analysis is known as retrospective estimation, as opposed to prospective estimation, conducted before data collection and analysis. Although there is debate on this topic, the latter (prospective) approach is generally recommended (Gerard et al., 1998; Nakagawa & Foster, 2004).

Additional data collection involves not only collecting additional data points, but also re-testing the model with the new dataset to ensure that the path coef<sup>fi</sup>cient with the minimum absolute magnitude has not decreased. Let us assume that a researcher collects 100 data points to test a PLS-SEM model, and <sup>fi</sup>nds that the path coef<sup>fi</sup>cient with the minimum absolute magnitude in the model is .237. Using the inverse square root method, the minimum required sample size is estimated to be 111. The researcher then proceeds to collect 11 additional data points and re-tests the model. If the path coef<sup>fi</sup>cient with the minimum absolute magnitude in the model is still .237 or higher, then the minimum sample size requirement is met.

Instead of collecting additional data points, the researcher may rely on adjustments in the analysis and in the hypothesis testing assumptions. Taking the example above as a basis, instead of collecting 11 additional data points the researcher may simplify the model somewhat by removing one or more competing links (i.e. links from multiple predictors to one criterion latent variable), particularly links competing with the link (or path) whose coef<sup>fi</sup>cient is .237. Clearly, this should be informed by theory and past research; otherwise, the empirical study becomes a data-<sup>fi</sup>tting exercise.

Let us say that the researcher removed one link competing with the link whose path coef<sup>fi</sup> cient is .237. This removal would have a good chance of increasing the path coef<sup>fi</sup>cient with the minimum absolute magnitude, because each additional competing link tends to decrease the path coef<sup>fi</sup>cients for other competing links. Let us say that the path coef<sup>fi</sup>cient with the min imum absolute magnitude is .286 after the removal of one competing link. Using the inverse square root method, the minimum required sample size is estimated to be 76. This minimum required sample size is already met by the 100 data points originally collected. In this case, a simpli<sup>fi</sup>cation of the research model obviates the need for additional data collection.

An alternative to simplifying the model, which does not involve collecting more data either, is to regard a path coef<sup>fi</sup>cient that is too low in the context of a given sample size to be nonsigni<sup>fi</sup>cant regardless of the corresponding P value. For example, let us assume that, with 100 data points, the two path coef<sup>fi</sup>cients with the smallest absolute magnitudes are .237 and .253, both found to be signi<sup>fi</sup>cant at $P < . 0 5$ in an empirical study. Using the inverse square root method, the minimum required sample sizes associated with these two coef<sup>fi</sup>cients would, respectively, be 111 (as noted before) and 97. Here the researcher would regard the analysis to have failed to support the hypothesis associated with the .237 path, and succeeded in its support of the hypothesis associated with the .253 path.

## Minimum sample size estimation before data collection and analysis

Minimum sample size estimation before data collection and analysis, or prospective estimation, is generally recommended over the retrospective approach of estimation after data collection and analysis (Gerard et al., 1998; Nakagawa & Foster, 2004). In prospective estimation, the researcher must decide at the outset the acceptable value of the path coef<sup>fi</sup>cient with the min imum absolute magnitude. This is likely to drive hypothesis testing beyond considerations regarding P values. In this context, an important question is: What is a reasonable acceptable value of the path coef<sup>fi</sup>cient with the minimum absolute magnitude in a model?

Based on Cohen’s (1988; 1992) power assessment guidelines, a reasonable answer to this question would be a value that would satisfy $\beta ^ { 2 } / ( 1 - \beta ^ { 2 } ) > . 0 2$ in a very simple model with only one predictor and one criterion latent variable. In other words, the effect size measured via Cohen’s $f ^ { 2 }$ coef<sup>fi</sup>cient in a model with only two variables X and Y, linked as $X \to Y ,$ would have to be greater than Cohen’s (1988; 1992) minimum acceptable effect size of .02.

More complex models would tend to lead to lower effect sizes, because such models would likely include more competing links. Given this, we could set as our target an effect size that is twice Cohen’s (1988; 1992) minimum acceptable, namely an effect size of .04. Our continuing research on this topic, including a variety of targeted Monte Carlo simulations, suggests tha this rule of thumb covers the vast majority of models, including fairly complex models, as long as they are free of vertical and lateral collinearity (Kock & Lynn, 2012). The corresponding inequality for this proposed rule of thumb would be $\beta ^ { 2 } / ( 1 - \beta ^ { 2 } ) > . 0 4$ , whose solution is $\beta { \geq } . 1 9 7$

Using the inverse square root method, the above would lead to a minimum required sample size of 160. Given this, another general rule of thumb could be proposed, this one as an answer to the following question: What is a reasonable value for minimum sample size, if we do not know in advance the value of the path coef<sup>fi</sup>cient with the minimum absolute magnitude? The answer would be 160, based on the inverse square root method. Based on the gammaexponential method, the answer would be 146.

A different approach for prospective minimum sample size estimation is to set the acceptable value of the path coef<sup>fi</sup>cient with the minimum absolute magnitude based on past empirical research or the results of a pilot study. Either of these could suggest a large path coef<sup>fi</sup>cient of minimum absolute magnitude, which would lead to a relatively small sample size requirement. The danger here is in underestimating the minimum required sample size, which would call for conservative prospective estimations of the path coef<sup>fi</sup>cient of minimum absolute magnitude.

For example, if past empirical research or a pilot study suggests a path coef<sup>fi</sup>cient of minimum absolute magnitude of .35, the inverse square root method would yield a minimum required sample size of 51. Still, after having collected and analysed 51 data points in an empirical study, a researcher would have to make sure that the path coef<sup>fi</sup>cient of minimum absolute magnitude was not lower than the expected .35. (A path coef<sup>fi</sup>cient of minimum absolute magnitude equal to or higher than .35 would have been acceptable.) If the path coef<sup>fi</sup>cient of minimum absolute magnitude turned out to be lower than the expected .35, the researcher would have to rely on approaches similar to those discussed earlier in connection with retrospective estimation (e.g. additional data collection).

## Additional issues

The results of our third Monte Carlo experiment illustrated the phenomenon of capitalization on error, whereby a small path coef<sup>fi</sup>cient of .1 was overestimated by the PLS Mode A algorithm we used in our PLS-SEM analyses. This clearly occurred for the sample size of 30, and seems to be a re<sup>fl</sup>ection of a general pattern that occurs with the PLS Mode A algorithm under certain conditions. Notable among those conditions are: (a) very small path coef<sup>fi</sup>cients (e.g. .1), and (b) very small sample sizes (e.g. 30).

Our results suggest that the methods we propose here for minimum sample size estimation are not affected by capitalization on error. The main reason for this is that our proposed methods tend to generate minimum sample size estimates for small path coef<sup>fi</sup>cients that are far above the sample sizes at which capitalization on error occurs. The fact that our methods focus on high power values (i.e. greater than .8) for minimum sample size estimation is a key element in avoiding bias because of capitalization on error. If we had tried to develop methods to estimate minimum sample sizes for low power values (e.g. .2), capitalization on error might become an issue.

Collecting and analysing data at multiple levels of analysis can have an impact on minimum sample size estimation, e.g. collecting data at the individual and team levels. We see this in MBLC’s study, where data from 17 project teams comprising 68 developers and 17 clients was collected, and where each group had four developers and one client. MBLC collected and analysed data at the team level of analysis, which led to a rather small sample size of 17, and team aggregation of the individual data. If they had considered the individual team member to be the unit of analysis, the sample size would have been 85, but the analysis would have to become more complex in order to control for the effect of team membership on various hypothesized relationships. Another aspect that this type of analysis would arguably have to control for is whether the individual is a developer or a client. The topic of multi-level data collection and analysis is beyond the scope of the discussion presented here. Nevertheless, we provide in Appendix F a basic discussion of this topic in the context of MBLC’s study.

## CONCLUSION

IS researchers have been at the forefront of the development, software implementation, and use of PLS-SEM (Aguirre-Urreta & Marakas, 2013; Chin, 1998; Chin et al., 2003; Kock, 2010). One of the most fundamental issues in PLS-SEM is that of minimum sample size estimation, where the ‘10-times rule’ method has been a favourite (Hair et al., 2011) because of its simplicity of application – it builds on the rule that the sample size should be greater than 10 times the maximum number of inner or outer model links pointing at any latent variable in the model.

In spite of the 10-times rule method’s simplicity of application, it has been shown in the past to lead to inaccurate estimates (Goodhue et al., 2012). We proposed two related methods, based on mathematical equations, as alternatives for minimum sample size estimation in PLS-SEM: the inverse square root method and the gamma-exponential method. Based on three Monte Carlo experiments, we demonstrated that both methods are fairly accurate. We also showed that the <sup>fi</sup>rst method is particularly attractive in terms of its simplicity of application.

As demonstrated through our analyses and related discussion, the gamma-exponential method is much more complex in its application (relying on a computer programme) than the inverse square root method. The latter, in addition to being simpler (relying on a simple equation), is also fairly precise, leading to small overestimations, and ‘safe’ in its slight imprecision, apparently always leading to small overestimations of the minimum sample sizes required.

Consistently with these <sup>fi</sup>ndings, it is our recommendation for PLS-SEM users who are not methodological researchers that they use the inverse square root method for minimum sample size estimation at the early stages of their research design. By doing so, those researchers will generate estimates that are both fairly precise and safe, with both normal and non-normal data. Our analyses suggest that their estimates will always be somewhat larger than the true minimum sample sizes required, but not by much, placing light demands on data collection beyond what would actually be needed.

The <sup>fi</sup>eld of IS brings together researchers with a wide variety of skills and interests, counting among them methodological researchers, software developers and expert users of methodological tools. The multidisciplinary nature of the <sup>fi</sup>eld is perhaps one of its de<sup>fi</sup>ning characteristics, and may be one of the reasons why IS has become a reference for other <sup>fi</sup>elds (Baskerville & Myers, 2002; Grover et al., 2006). Not surprisingly, IS researchers have provided the impetus for the widespread use of PLS-SEM (Chin, 1998; Chin et al., 2003; Kock, 2010), and IS researchers have also been at the forefront of questioning some of the claims in connection with PLS-SEM (Aguirre-Urreta & Marakas, 2013; Goodhue et al., 2012). It is our hope that this paper will contribute to this tradition of scholarly debate.

## REFERENCES

Aguirre-Urreta, M.I. & Marakas, G.M. (2013) Research note—partial least squares and models with formatively speci<sup>fi</sup>ed endogenous constructs: a cautionary note. Information Systems Research, 25(4), 761–778.

Baskerville, R.L. & Myers, M.D. (2002) Information systems as a reference discipline. MIS Quarterly, 26(1), 1–14.

Bradley, R.V., Pratt, R.M.E., Byrd, T.A., Outlay, C.N. & Wynn, D.E. Jr. (2012) Enterprise architecture, IT effectiveness and the mediating role of IT alignment in US hospitals Information Systems Journal, 22(2), 97–127.

Chin, W.W. (1998) Issues and opinion on structural equation modeling. MIS Quarterly, 22(1), vii–xvi

Chin, W.W., Marcolin, B.L. & Newsted, P.R. (2003) A partia least squares latent variable modeling approach for measuring interaction effects: Results from a Monte Carlo simulation study and an electronic-mail emotion/ adoption study. Information Systems Research, 14(2), 189–218.

Chin, W.W., Thatcher, J.B. & Wright, R.T. (2012) Assessing common method bias: problems with the ULMC technique. MIS Quarterly, 36(3), 1003–1019.

Chintagunta, P.K. (2001) Endogeneity and heterogeneity in a probit demand model: estimation using aggregate data. Marketing Science, 20(4), 442–456.

Cohen, J. (1988) Statistical Power Analysis for the Behavioral Sciences. Lawrence Erlbaum, Hillsdale, NJ

Cohen, J. (1992) A power primer. Psychological Bulletin, 112(1), 155–159.

Diaconis, P. & Efron, B. (1983) Computer-intensive methods in statistics. Scienti<sup>fi</sup>c American, 249(1), 116–130.

Dijkstra, T.K. & Henseler, J. (2015) Consistent partial least squares path modeling. MIS Quarterly, 39(2), 297–316.

Efron, B., Rogosa, D. & Tibshirani, R. (2004) Resampling methods of estimation, In: International Encyclopedia of the Social & Behavioral Sciences, Smelser, N.J. & Baltes, P.B. (eds), pp. 13216–13220. Elsevier, New York, NY.

Gerard, P.D., Smith, D.R. & Weerakkody, G. (1998) Limits of retrospective power analysis. Journal of Wildlife Management, 62(2), 801–807.

Goodhue, D., Lewis, W. & Thompson, R. (2007) Statistica power in analyzing interaction effects: questioning the advantage of PLS with product indicators. Information Systems Research, 18(2), 211–227.

Goodhue, D.L., Lewis, W. & Thompson, R. (2012) Does PLS have advantages for small sample size or nonnormal data? MIS Quarterly, 36(3), 981–1001.

Grilli, L. & Rampichini, C. (2011) The role of sample cluster means in multilevel models. Methodology, 7(4), 121–133.

© 2016 John Wiley & Sons Ltd, Information Systems Journa

Grover, V., Gokhale, R., Lim, J., Coffey, J. & Ayyagari, R (2006) A citation analysis of the evolution and state of information systems within a constellation of reference disciplines. Journal of the Association for Information Systems, 7(5), 270–325.

Gurland, J. & Tripathi, R.C. (1971) A simple approximation for unbiased estimation of the standard deviation. American Statistician, 25(4), 30–32.

Hair, J.F., Hult, G.T.M., Ringle, C.M. & Sartedt, M. (2014) A Primer on Partial Least Squares Structural Equation Modeling. Sage, Thousand Oaks, CA.

Hair, J.F., Ringle, C.M. & Sarstedt, M. (2011) PLS-SEM: indeed a silver bullet. The Journal of Marketing Theory and Practice, 19(2), 139–152.

Hardin, A.M., Fuller, M.A. & Valacich, J.S. (2006) Measur ing group ef<sup>fi</sup>cacy in virtual teams new questions in an old debate. Small Group Research, 37(1), 65–85.

Jak, S., Oort, F.J. & Dolan, C.V. (2013) A test for cluster bias: detecting violations of measurement invariance across clusters in multilevel data. Structural Equation Modeling, 20(2), 265–282.

Kipnis, C. & Varadhan, S.R.S. (1986) Central limit theorem for additive functionals of reversible Markov processe and applications to simple exclusions. Communications in Mathematical Physics, 104(1), 1–19.

Klein, K.J. & Kozlowski, S.W. (2000) From micro to meso: critical steps in conceptualizing and conducting multilevel research. Organizational Research Methods, 3(3), 211–236.

Kline, R.B. (1998) Principles and Practice of Structura Equation Modeling. The Guilford Press, New York, NY.

Kock, N. (2010) Using WarpPLS in e-collaboration studies: an overview of <sup>fi</sup>ve main analysis steps. Internationa Journal of e-Collaboration, 6(4), 1–11.

Kock, N. (2014a) Stable P Value Calculation Methods in PLS-SEM. ScriptWarp Systems, Laredo, TX.

Kock, N. (2014b) Advanced mediating effects tests, multi group analyses, and measurement model assessments in PLS-based SEM. International Journal of e-Collaboration, 10(3), 1–13.

Kock, N. (2015) One-tailed or two-tailed P values in PLS SEM? International Journalofe-Collaboration,11(2), 1–7.

Kock, N. (2016) Non-normality propagation among latent variables and indicators in PLS-SEM simulations. Journa of Modern Applied Statistical Methods, 15(1), 299–315.

Kock, N. & Lynn, G.S. (2012) Lateral collinearity and mis leading results in variance-based SEM: an illustration and recommendations. Journal of the Association for Information Systems. 13(7). 546–580.

Lohmöller, J.-B. (1989) Latent Variable Path Modeling With Partial Least Squares. Physica-Verlag, Heidelberg, Germany.

Majchrzak, A., Beath, C.M., Lim, R.A. & Chin, W.W. (2005) Managing client dialogues during information systems design to facilitate client learning. MIS Quarterly, 29(4), 653–672.

Mandal, P., Mukhopadhyay, S., Bagchi, K. & Gunasekaran, A. (2012) The impact of organisational strategy, culture, people and technology management on organisationa practice and performance: an empirical analysis. International Journal of Information Systems and Change Management, 6(2), 160–176.

Mattson, S. (1997) How to generate non-normal data fo simulation of structural eguation models. Multivariate Behavioral Research, 32(4), 355–373.

Miller, R.B. & Wichern, D.W. (1977) Intermediate Business Statistics: Analysis of Variance, Regression and Time Series. Holt, Rihehart and Winston, New York, NY.

Muthén, L.K. & Muthén, B.O. (2002) How to use a Monte Carlo study to decide on sample size and determine power. Structural Equation Modeling, 9(4), 599–620.

Nakagawa, S. & Foster. T.M. (2004) The case against retrospective statistical power analyses with an intro duction to power analysis. Acta Ethologica, 7(2), 103–108.

Paxton, P., Curran, P.J., Bollen, K.A., Kirby, J. & Chen, F. (2001) Monte Carlo experiments: design and imple mentation. Structural Equation Modeling, 8(2), 287–312.

Peng, D.X. & Lai, F. (2012) Using partial least squares in operations management research: a practical guideline and summary of past research. Journal of Operations Management, 30(6), 467–480.

Preacher, K.J., Zyphur, M.J. & Zhang, Z. (2010) A genera multilevel SEM framework for assessing multilevel medi ation. Psychological Methods, 15(3), 209–233.

Rasoolimanesh, S.M., Dahalan, N. & Jaafar, M. (2016) Tourists' perceived value and satisfaction in a community-based homestay in the Lenggong Valley World Heritage Site. Journal of Hospitality and Tourism Management, 26(1), 72–81.

Raudenbush, S.W. & Bryk, A.S. (2002) Hierarchical Linea Models: Applications and Data Analysis Methods. Sage, Thousand Oaks, CA.

Robert, C. & Casella, G. (2013) Monte Carlo Statistica Methods. Springer, New York, NY.

Schmiedel, T., vom Brocke, J. & Recker, J. (2014) Develop ment and validation of an instrument to measure organizational cultures’ support of business process management. Information & Management, 51(1), 43–56.

Schnabel, R.B. & Eskow, E. (1990) A new modi<sup>fi</sup>ed Cholesky factorization. SIAM Journal on Scienti<sup>fi</sup>c and Statistical Computing, 11(6), 1136–1158.

Shaver, J.M. (1998) Accounting for endogeneity when assessing strategy performance: does entry mode choice affect FDI survival? Management Science, 44(4), 571–585.

Snijders, T. & Bosker, R. (1999) Multilevel Analysis: An In troduction to Basic and Advanced Multilevel Modeling Sage, London, England.

van Mierlo, H., Vermunt, J.K. & Rutte, C.G. (2009) Com posing group-level constructs from individual-leve survey data. Organizational Research Methods, 12(2), 368–392.

Weakliem, D.L. (2016) Hypothesis Testing and Mode Selection in the Social Sciences. Guilford Publications, New York, NY.

Wold, H. (1980) Model construction and evaluation when theoretical knowledge is scarce, In: Evaluation of Econo metric Models, Kmenta, J. & Ramsey, J.B. (eds), pp. 47–74. Academic Press, Waltham, MA.

## Biographies

Ned Kock is Killam Distinguished Professor and Chair ot the Division of International Business and Technology Studies, in the Sanchez School of Business, at Texas A&M International University. He holds degrees in electron ics engineering (BEE), computer science (MS) and man agement information systems (PhD). Ned has authored and edited several books and is the developer of WarpPLS, a widely used structural equation modelling software. Ned has published his research in a number o high-impact journals including Communications of the ACM, Decision Support Systems, European Journal of In formation, Systems IEEE Transactions Information and Management, Journal of the AIS, MIS Quarterly and Orga nization Science. He is the Founding Editor-in-Chief of the International Journal of e-Collaboration, His research interests include multivariate statistics, biological in<sup>fl</sup>uences on behaviour toward technology, action research, ethical and legal issues in technology research and management, e collaboration and business process improvement.

Pierre Hadaya is a professor in the Department of Man agement and Technology at the School of Business Admin istration of the Université du Québec à Montréal. He holds a PhD in Management of Technology from the École Polytechnique de Montréal. His research interests include IT value, IT alignment, enterprise architecture, IT-enabled business transformation, interorganizational information systems, human computer interaction, system dynamics modelling and methodological issues related to PLS-based structural equation modelling. He has published his research in several journal including Journal of Strategic Information Systems, Information and Management,

Computers in Human Behavior, Electronic Markets: The International Journal on Networked Business, Supply Chain Management: An International Journal and Industrial Management and Data Systems.

## APPENDIX A: MONTE CARLO SIMULATIONS

In a Monte Carlo simulation, the samples generated for each sample size point are based on a population model de<sup>fi</sup>ned by the researcher, and build on common factor model assumptions, whose basic mathematical underpinnings are discussed in this appendix. For simplicity, and without any impact on the generality of the discussion presented here, we assume that variables are standardized—i.e. scaled to have a mean of zero and a standard deviation of 1.

Let $\zeta _ { j }$ be the error variable that accounts for the variance in an endogenous latent variable $F _ { j }$ that is not explained by the predictor latent variables that point at $F _ { j } .$ . Let $F _ { j }$ be one of the $N _ { j }$ predictor latent variables that point at an endogenous latent variable $F _ { j } .$ And let $\theta _ { i j }$ be the standardized error variable that accounts for the variance in the indicator $x _ { i j }$ that is not explained by its latent variable $F _ { j }$

In a Monte Carlo simulation where multiple replications of a model are created (e.g. 1000 replications, or samples), error variables and exogenous variables can be created according to equations (A.1) to (A.3). In these equations, Rndn(N) is a function that returns a differen normal random variable each time it is invoked, as a vector with N elements (where N is the sample size), and Stdz( ) is a function that returns a standardized variable.

$$
\zeta_ {i} \leftarrow S t d z (R n d n (N))\tag{A.1}
$$

$$
F _ {j} \leftarrow S t d z (R n d n (N))\tag{A.2}
$$

$$
\theta_ {i j} \leftarrow S t d z (R n d n (N))\tag{A.3}
$$

This assumes that simulated samples that follow normal distributions are desired. To obtain non-normal samples, transformations based on the normally-distributed variables can be used. For example, equations (A.4) to (A.6) transform the normal variables into corresponding non-normal variables that follow a $\chi ^ { 2 }$ distribution with 1 degree of freedom; a distribution with theoretical skewness and excess kurtosis values of 2.828 and 12, respectively.

$$
\zeta_ {i} \leftarrow S t d z \left(\zeta_ {i} ^ {2}\right)\tag{A.4}
$$

$$
F _ {j} \leftarrow S t d z \left(F _ {j} ^ {2}\right)\tag{A.5}
$$

$$
\theta_ {i j} \leftarrow S t d z \left(\theta_ {i j} ^ {2}\right)\tag{A.6}
$$

After the error variables and exogenous latent variables are created, endogenous latent variables are produced based on the true population path coef<sup>fi</sup>cients de<sup>fi</sup>ned beforehand by the researcher. This is indicated in (A.7), where $R _ { i j }$ are the correlations among the linked latent variables. Finally, indicators are created based on the true population loadings based on (A.8).

$$
F _ {i} = \sum_ {j = 1} ^ {N _ {i}} \beta_ {i j} F _ {j} + \left(\sqrt {\left(1 - \sum_ {j = 1} ^ {N _ {i}} \beta_ {i j} R _ {i j}\right)}\right) \zeta_ {i}\tag{A.7}
$$

$$
x _ {i j} = \lambda_ {i j} F _ {i} + \left(\sqrt {1 - \lambda_ {i j} ^ {2}}\right) \theta_ {i j}, j = 1 \dots n _ {i}\tag{A.8}
$$

Normally, a set of samples (e.g. 1000 samples) is generated through the above steps for each sample size, with sample sizes varying incrementally. Generally speaking, a larger set of samples created in connection with each sample size (e.g. 1000 instead of 100) will lead to more precise and replicable measures of statistical power obtained via a Monte Carlo simulation for that particular sample size.

The above discussion refers to one of two main Monte Carlo simulation approaches, whereby both latent variables and indicators are generated. This approach has been commonly used in methodological PLS-SEM investigations published in IS and statistics outlets (Chin et al., 2012; Goodhue et al., 2012; Kock, 2016).

In the other main Monte Carlo simulation approach only indicators are generated (see, e.g. Mattson, 1997). This latter approach is based on the Cholesky factorization technique (Schna bel & Eskow, 1990), and has the disadvantage of not giving methodological researchers access to latent variable scores. Such scores may be needed in the estimation of certain model coef <sup>fi</sup>cients such as vertical and lateral collinearity variance in<sup>fl</sup>ation factors (Kock & Lynn, 2012), and are useful in the generation of non-normal data (Goodhue et al., 2012; Kock, 2016).

## APPENDIX B: EXCEL SPREADSHEET WITH VISUAL BASIC CODE

Figure B.1 shows the Excel spreadsheet that we have developed to implement the gammaexponential method, by combining gamma and exponential smoothing function corrections applied to the standard error estimation used in the inverse square root method. This Excel spreadsheet also shows the estimate obtained via the inverse square root method, for completeness.

<table><tr><td colspan="5">Estimating minimum sample size: Change the values in the yellow cells to obtain the values in the green cells</td></tr><tr><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T</td><td>1.645</td><td>(T ratio associated with P value threshold chosen)</td><td>P</td><td>0.050 (P value threshold for significance)</td></tr><tr><td>z</td><td>0.842</td><td>(z score associated with power level chosen)</td><td>W</td><td>0.800 (Power level chosen)</td></tr><tr><td>bmin</td><td>0.397</td><td>(Minimum absolute beta coefficient in model)</td><td></td><td></td></tr><tr><td>N(EXPS+GAMM)</td><td>26</td><td>(Minimum required sample size: Exponential smoothing and gamma function methods)</td><td></td><td></td></tr><tr><td>N(SQRT)</td><td>40</td><td>(Minimum required sample size: Square root method)</td><td></td><td></td></tr></table>

Figure B.1: Excel spreadshee

As noted before, the T ratio for a chosen P value threshold is calculated as the z-score asso ciated with 1 minus the P value threshold $( { \tt e . g . } \top _ { . 0 5 } { = } z _ { . 9 5 } )$ . In Excel, a z-score associated with any value x is obtained using the function NORMINV(x,0,1) or the function NORMSINV(x).

Exhibit B.1 shows the Visual Basic code associated with the spreadsheet. We have developed this code so that, whenever any of the cells in yellow in the Excel spreadsheet changes, new values for the minimum required sample sizes are calculated. The code uses cell labels (e.g. T, z etc.) instead ofz standard cell references (e.g. B3, B4 etc.) in the ‘Range’ object calls. The cell labels used are indicated on the spreadsheet next to their respective values.

## EXHIBIT B.1: VISUAL BASIC CODE

```vba
Private Sub Worksheet_Change(ByVal Target As Range)
    If Not Intersect(Target, Range('bmin, P, W')) Is Nothing Then
    Calc_N_EXPSnGAMM
End If

End Sub

Sub Calc_N_EXPSnGAMM()
    Dim T As Double
    Dim z As Double
    Dim b As Double
    Dim cN As Long

    T = Range('T').Value
    z = Range('z').Value
    b = Range('bmin').Value
    cN = 1

Do While Abs(b) × cN ^ 0.5 × Exp((Exp1 × Abs(b)) / cN ^ 0.5) ≤ T + z

    cN = cN + 1

Loop

If cN ≤ 10 Then

    cN = 1

Do While Abs(b) × cN ^ 0.5 × ((cN - 1)/2) ^ 0.5 × Exp(WorksheetFunction.GammaLn(cN/2)) / Exp(WorksheetFunction.GammaLn((cN + 1)/2)) ≤ T + z

    cN = cN + 1
```

```txt
Loop
End If
Range('N_EXPS_GAMM').Value = cN
End Sub
```

The Visual Basic code is split into two main functions: ‘Worksheet\_Change’ and ‘Calc\_N\_EXPSnGAMM’. The code under ‘Calc\_N\_EXPSnGAMM’ implements only the gamma-exponential method. The inverse square root method is implemented without any Visual Basic code, simply through the formula: ROUNDUP(((T + z)/ABS(bmin))^2,0).

## APPENDIX C: PLS MODE A

Various PLS-SEM algorithms have been developed based on Wold’s (1980) original design, of which an extensive discussion is provided by Lohmöller (1989). By far, the most widely used of these algorithms is PLS Mode A. This is an iterative algorithm where indicator weight estimates $\hat { w } _ { i j }$ are initially set to 1, and latent variable estimates $\hat { F } _ { i }$ are initialized with a standardized vector of the summed indicators. Then, the values of $\hat { F } _ { i }$ are re-estimated as

$$
\hat {F} _ {i} := \operatorname{Std} z \left(\sum_ {j = 1} ^ {A _ {i}} \hat {v} _ {i j} \hat {F} _ {j}\right).\tag{C.1}
$$

The step implemented via (C.1) is known as the ‘inside approximation’, where Stdz( ) is a function that returns a standardized column vector with N rows (where N is the sample size), and $A _ { j }$ is the number of latent variables $\hat { F } _ { j } ( j = 1 \ldots A _ { i } )$ that are ‘neighbours’ of the latent variable $\hat { F } _ { i }$ . Latent variables are referred to as neighbours when they are linked to one another by arrows, either by pointing at or being pointed at by neighbour latent variables.

The weights $\hat { \nu } _ { i j }$ are referred to as the ‘inner weights’ (Lohmöller, 1989), and are estimated via three main schemes: centroid. factorial and path weighting. In the centroid scheme. the inner weights are set according to (C.2), as the signs ( 1 or + 1) of the estimated correlations among neighbour latent variables. In the factorial scheme, the inner weights are set according to (C.3), as the correlations among neighbour latent variables. In the path weighting scheme, the inner weights are set according to A.8, as the path coef<sup>fi</sup>cients or correlations among neighbour latent variables, depending on whether the arrows go in or out, respectively.

$$
\hat {v} _ {i j} := \operatorname{Sign} \left(\Sigma_ {\hat {F} _ {i} \hat {F} _ {j}}\right)\tag{C.2}
$$

$$
\hat {v} _ {i j} := \Sigma_ {\hat {F} _ {i} \hat {F} _ {j}}\tag{C.3}
$$

$$
\int \hat {v} _ {i j} := \hat {\beta} _ {i j}, \quad \text {   if   } \hat {F} _ {j} \text {   points   at   } \hat {F} _ {i},
$$

$$
\left\{ \begin{array}{l} \hat {v} _ {i j} := \Sigma_ {\hat {F} _ {i} \hat {F} _ {j}}, \quad \text { if } \hat {F} _ {i} \text { points   at } \hat {F} _ {j}. \end{array} \right.\tag{C.4}
$$

Next the PLS Mode A algorithm proceeds by estimating what are known as the ‘outer weights’; which is done by solving C.1 for $\hat { w } _ { i j }$ , where: $N _ { F }$ is the total number of latent variables in the model, $n _ { j }$ is the number of indicators associated with latent variable $F _ { j }$ and $\hat { \epsilon } _ { i j }$ is the indicator error for the latent variable’s jth indicator. This step yields estimates of the loadings of the indicators on their respective latent variables.

$$
x _ {i j} = \hat {F} _ {i} \hat {w} _ {i j} + \hat {\epsilon} _ {i j}, i = 1 \dots N _ {F}, j = 1 \dots n _ {i}.\tag{C.5}
$$

The PLS Mode A algorithm subsequently proceeds by estimating the latent variables as indicated in (C.6), through the step known as ‘outside approximation’.

$$
\hat {F} _ {i} := \operatorname{Std} z \left(\sum_ {j = 1} ^ {n _ {i}} \hat {w} _ {i j} x _ {i j}\right)\tag{C.6}
$$

The foregoing steps are conducted iteratively until the outer weights $\hat { w } _ { i j }$ change by less than a small fraction. Then, path coef<sup>fi</sup>cients are estimated by solving C.7 for $\hat { \beta } _ { i j }$ . This essentially entails the solution of multiple ordinary least square regressions in ‘mini-models’ with $\hat { F } _ { j }$ predictor latent variables $( j = 1 \ldots N _ { i } )$ pointing at each $\hat { F } _ { i }$ criterion latent variable.

$$
\hat {F} _ {i} = \sum_ {j = 1} ^ {N _ {i}} \hat {\beta} _ {i j} \hat {F} _ {j} + \hat {\zeta} _ {i}.\tag{C.7}
$$

Here, $\hat { \beta } _ { i j }$ is the estimated standardized partial regression (a.k.a. path) coef<sup>fi</sup>cient for the criterion-predictor relationship between $F _ { j }$ and $\hat { F } _ { j } , N _ { j }$ is the number of predictors pointing at $F _ { j }$ in the model and $\zeta _ { i }$ is the structural residual accounting for the variance in $\hat { F } _ { i }$ that is not explained by the estimates of the latent variables that point at it in the model.

## APPENDIX D: BOOTSTRAPPING

Bootstrapping (Diaconis & Efron, 1983) is the most widely used method for standard error estimation in PLS-SEM. Through the bootstrapping method, a standard error is generated for each path coef<sup>fi</sup>cient in a model, and then typically used to generate a T ratio, by dividing the path coef<sup>fi</sup>cient by the standard error. Next, a $P$ value is obtained for the Tratio using the incomplete beta function or a table relating P values to T ratios.

In PLS-SEM, bootstrapping is typically applied to an empirical dataset, with the goal of creating multiple samples based on that dataset. Let $\mathcal { S }$ be a set of samples created based on an em pirical dataset, where each sample in $\mathcal { S }$ is built by taking rows at random and with replacement (i.e. the same row can be repeated) from the original dataset.

Each sample in S has the same size (i.e. number of rows) as the original dataset. The set of samples denoted by $\mathcal { S }$ is also known in PLS-SEM as the resample set. In practical applications, the size of this resample set, or number of samples in $\mathcal { S } _ { : }$ , often varies from 100 to 500. Let $N _ { S }$ denote the size of this resample set, or the number of samples in S.

The standard error estimate denoted as $S _ { \beta }$ , obtained via bootstrapping for a given path coef<sup>fi</sup>cient $\beta ,$ is calculated according to D.1, where: $\beta _ { i }$ is the path coef<sup>fi</sup>cient estimate for sample i, and $\overline { { \beta } }$ is the mean path coef<sup>fi</sup>cient across all samples. This is essentially the standard deviation of $\beta .$

$$
\mathfrak {S} _ {\beta} = \sqrt {\frac {1}{N _ {S}} \sum_ {i = 1} ^ {N _ {S}} \left(\beta_ {i} - \overline {{\beta}}\right) ^ {2}}.\tag{D.1}
$$

The bootstrapping approach to estimation of standard errors in PLS-SEM can be seen as a type of Monte Carlo simulation approach (Robert & Casella, 2013). Mimicking the sample creation process typically seen in Monte Carlo simulations, in bootstrapping many samples are created for subsequent analysis. But bootstrapping should not be confused with the Monte Carlo simulation method discussed earlier; in fact, bootstrapping is used as part of the simulations used in the Monte Carlo experiments.

The key difference between the two methods is that normally in Monte Carlo simulations the samples are created based on a true population model. In bootstrapping, on the other hand, an empirical dataset is used as a basis, from which multiple samples are created by taking rows at random and with replacement from the empirical dataset.

## APPENDIX E: NON-NORMAL DATA

Figure E.1 shows two histograms. The one on the left is for a standardized normally distributed variable, where skewness (indicated as ‘Skew.’ below the histogram) and excess kurtosis (indi cated as ‘Kurt.’) both approach zero. The histogram on the right shows a variable that follows a non-normal distribution, namely a $\chi ^ { 2 }$ distribution with 1 degree of freedom. The variable on the right was created based on a transformation applied to the variable on the left, by squaring and standardizing it. This variable is in fact severely non-normal, with skewness of 2.80 and excess kurtosis of 10.98.

![](/api/attachments/XY8PNKH3/fulltext/images/a8e665b82e8484cd0f1bdc986b4f8e8f19506d3a36533121201a035362fb0872.jpg)  
Figure E.1: Histograms of normal and non-normal data

![](/api/attachments/XY8PNKH3/fulltext/images/ddcf436a483a82eaad72fffb82bdd67b03cbf4ea67b81a5456baa03df8aa6c4d.jpg)

Figure E.2 shows data points and regression lines for three samples, where a predic tor variable (X) is plotted on the horizontal axis and a criterion variable (Y) on the vertical axis. This <sup>fi</sup>gure is based on a simple model with only two variables, where $\scriptstyle \gamma = \beta _ { \gamma \chi } X + \varepsilon .$ . This model’s simplicity does not detract from its usefulness in our making our point regarding the robustness of least squares regression in the presence of non-normal data.

We also model the structural error (ε), to avoid non-normality propagation losses (Kock, 2016). In the <sup>fi</sup>gure, we have the following: (left) both the predictor latent variable (X) and struc tural error (ε) are normal; (middle) the predictor (X) is non-normal but the structural error (ε) is normal; and (right) both the predictor (X) and structural error (ε) are non-normal. The data was created assuming the population model value of $\beta _ { \mathrm { { Y X } } } = . 3$ . To minimize the bias because of sampling error, we used a sample size of 10 000.

As can be inferred from the three graphs, the estimated least squares regression coef<sup>fi</sup>cient equals .3, which is the value of the corresponding population model coef<sup>fi</sup>cient, for each of the three cases. That is, even though the distribution of points shows a clear progression toward increasing non-normality as we move from left to right, we see no variation in the estimated least squares regression coef<sup>fi</sup>cients. In other words, we see no regression coef<sup>fi</sup>cient bias because of the different data distributions.

![](/api/attachments/XY8PNKH3/fulltext/images/079ed1cfb8a04bfffc522ac89b2c5eac134c01af46e537b0317f2f0f5fbdc958.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/c3d456d82c6c52b4183cada1c7921152be27f0c26a7a2fc7a1dda44169d14737.jpg)  
Notes: scales are standardized; left - predictor latent variable and error are normal; middle - predictor is non-normal but error is normal; right - predictor and error are non-normal.

![](/api/attachments/XY8PNKH3/fulltext/images/302a6af047564a658356cd0153e1e95cd24975665b52d8cc2a35b807d438ea18.jpg)  
Figure E.2: Least squares regression coef<sup>fi</sup>cients with normal and non-normal data

Figure E.3 shows the distributions of least squares regression coefficients obtained via bootstrapping, in the form of histograms. The sample size here was set to 300, and the number of resamples to 500. The order of the graphs is the same as in the previous <sup>fi</sup>gure, with the same respective patterns of non-normality. Note that in all three histograms the values for skewness and excess kurtosis both approach zero, suggesting normality.

![](/api/attachments/XY8PNKH3/fulltext/images/b68ceb7444287bc143e2bef01bbd4322e23d148e9d9eb03f9d2e899b5799c66f.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/755a2801c44379443790c4388bd2fbfd22a055912dd88fd074938550991424b0.jpg)

![](/api/attachments/XY8PNKH3/fulltext/images/de53b0dd107488116d2d911b008049dc134b1ebd628649b3ceccdb81a1c1dc91.jpg)  
Notes: histograms show the distribution of least squares regression coefficients; the order of the graphs is the same as in the previous figure.  
Figure E.3: Distributions of least squares regression coef<sup>fi</sup>cients obtained via bootstrapping

This <sup>fi</sup>gure demonstrates a remarkable property of bootstrapping, which is that it tends to yield normal distributions of estimates of the true least squares regression coef<sup>fi</sup>cient $\beta _ { Y X }$ in variable associations of the type $\scriptstyle \ Y = \beta _ { \ Y X } X + \varepsilon$ regardless of nature of the distributions of the variables Y, X and ε. Our continuing research on this topic, including a number of more complex simulations, leads us to conclude that this is generally true for more complex models as well, including typical PLS-SEM models used in empirical IS studies. This property of bootstrapping together with the robustness of least squares regression coef<sup>fi</sup>cients in the presence of non-normality are, in our view, the main underlying reasons why PLS-SEM in general is quite robust to deviations from normality.

More research is needed to ascertain whether the above properties are retained in a recent development related to PLS-SEM: the consistent PLS technique (Dijkstra & Henseler, 2015). This new technique corrects certain parameters estimated via PLS Mode A using the centroid scheme (Lohmöller, 1989) but does not generate latent variable scores or weights, which may be an obstacle to its widespread adoption without further developments aimed at consistently estimating those values. Those values are critical inputs for a number of tests now widely used in PLS-SEM, such as full collinearity and measurement invariance tests (Kock, 2014b; Kock & Lynn, 2012; Rasoolimanesh et al., 2016; Schmiedel et al., 2014).

Among the parameters corrected by consistent PLS are path coef<sup>fi</sup>cients, which tend to be underestimated by PLS Mode A and are used in our proposed minimum sample size estimatior methods. However, it should be noted that in their practical example of the application of the consistent PLS technique to an empirical study in the <sup>fi</sup>eld of IS, where they used bootstrapping as we have done here, Dijkstra & Henseler (2015, p. 310) concluded that: ‘With regard to the two path coef<sup>fi</sup>cients, the differences between the estimates were rather small.’ This comment refers to path coef<sup>fi</sup>cient estimates generated via PLS Mode A and those corrected with the consistent PLS technique. The reason for the small difference is that psychometrically sound measures were used, leading to high reliabilities. Using psychometrically sound measures leading to high reliabilities is typically expected in well-executed empirical studies.

## APPENDIX F: MULTI-LEVEL DATA

Multi-level data is often found in the <sup>fi</sup>eld of IS (see, e.g. Hardin et al., 2006), and it can have an impact on minimum sample size estimation. MBLC’s study is an example of this. Data from 17 project teams comprising 68 developers and 17 clients was collected, where each group had four developers and one client. If we consider the team to be the unit of analysis, the sample size is 17. If we consider the individual team member to be the unit of analysis, the sample size is 85. Choosing the team as the unit of analysis requires some form of aggregation of team members’ data at the team level (Klein & Kozlowski, 2000).

When multi-level data is available, a researcher may choose a level of analysis where there is no aggregation, such as the team member in MBLC’s study, to obtain a larger sample. However, this leads to potential sources of bias, which must be addressed by the researcher. One alternative is to include additional variables that enable the researcher to control for the effects of group membership on each endogenous latent variable (Grilli & Rampichini, 2011). A frequently used option to implement this, which is not without problems (as discussed below), is to include variables storing the group means associated with existing variables (Grilli & Rampichini, 2011; Jak et al., 2013). This is illustrated in Figure F.1, for MBLC’s study, where: TCI is a variable that stores the average cooperative interdependence (CI) in each team; TCE stores average collaborative elaboration (CE); TCL stores average client learning (CL) and TCQ stores average developers’ communication quality (CQ).

![](/api/attachments/XY8PNKH3/fulltext/images/0dead6a34265f456c4a2bf1f82557a2fdce250b3f5574a1837aa2261a09279ba.jpg)  
Figure F.1: Including variables storing group means  
© 2016 John Wiley & Sons Ltd, Information Systems Journa

This approach is akin to that of including control variables into a model so that the results can be said to hold ‘regardless’ of the effects of those variables; in this case, regardless of the in<sup>fl</sup>uences arising from group membership. The inclusion of variables storing the group means associated with existing variables would tend to decrease the path coef<sup>fi</sup>cients in the model, because they involve the insertion of competing links. An outcome of this would likely be a decrease in the path coef<sup>fi</sup>cient with the minimum absolute magnitude in the model. Nevertheless, such a decrease may not be enough to require a sample size greater than the one originally used.

For example, let us consider a variation of MBLC’s study where data at the team member level was used, yielding a sample size of 85. In this scenario, let us assume that no variables storing the group means were included, and that the path coef<sup>fi</sup>cient with the minimum absolute magnitude in the model was found to be .4. This is conservatively assumed to be only slightly higher than the coef<sup>fi</sup>cient of .397 for CL → LO obtained in the actual study; because there is more variation at the team member than at the team level of analysis, and thus less attenuation of path coef<sup>fi</sup>cients with respect to the true values (Kock, 2015; Lohmöller, 1989; Wold, 1980).

Let us now assume that the variables storing the group means—namely TCI, TCE, TCL and TCQ—are included in the model. The addition of TCL and TCQ alone is likely to bring down the path coef<sup>fi</sup>cient of minimum absolute magnitude in the model; let us assume it does, decreasing it from .4 to .3. This would be because of competing links being added to the model. Using the inverse square root method, the new path coef<sup>fi</sup>cient of minimum absolute magnitude in the model of .3 would lead to a minimum required sample size of 69. This requirement is met with a sample size of 85 at the team member level of analysis. That is, in this case it would have been advantageous, in terms of statistical power, to use a unit of analysis leading to a larger sample size; even though that decision would have made the model more complex because of the inclusion of additional variables storing the group means.

Being akin to controlling for the effect of demographic variables (e.g. controlling for the effect of gender), the approach of including variables storing group means is not without problems. A simple illustration where grouping is conducted demographically can help readers understand the approach more intuitively; and also help readers understand some of the approach’s weaknesses. Let us assume that the 85 participants in MBLC’s study were assigned to one of only two teams, one with only males and the other with females. Let us also assume that TCl TCE, TCL and TCQ would each store two sets of different values for males and females. In this case, all of these four variables would end up being perfectly collinear with one another (i.e. absolute correlations of 1), and thus the model should only include one ‘group control’ variable if collinearity were to be avoided. We could call this single group control variable GR (an acronym for gender); a variable with only two values (e.g. 1 = female and 0 = male). This new variable GR would replace the other four variables (i.e. TCI, TCE, TCL and TCQ) and point to all of the endogenous variables in the model: CL, LO and SO.

The illustration above highlights one of the problems with the approach of including variables storing group means: the fewer the number of groups available, the more likely it is that collinearity will occur. A high enough level of collinearity may signi<sup>fi</sup>cantly distort path coef<sup>fi</sup>cients, even if it is not perfect collinearity. For instance, with the original con<sup>fi</sup>guration in MBLC’s study we might <sup>fi</sup>nd, after a full collinearity test, that TCI and TCE are highly collinear (or redundant), and that so are TCL and TCQ; with full collinearity variance in<sup>fl</sup>ation factors above 5 for these variables (Kock & Lynn, 2012). To avert bias because of collinearity, at least one further step would have to be conducted. In this case, a researcher might use only one variable from each collinear pair; e.g. TCI in place of the pair TCI and TCE, and TCL in place of TCL and TCQ. Alternatively, the researcher might create two second-order variables (let us call them TCIE and TCLQ), and use only these second order latent variables in the model (see, e.g. Rasoolimanesh et al., 2016; Schmiedel et al., 2014). These second-order variables would, respectively, have as indicators: TCI and TCE, and TCL and TCQ.

Controlling for the effect of group membership by including variables storing group means may lead to another problem. Because it makes no assumptions about causal associations at the population level, it ignores the possibility of endogeneity (Chintagunta, 2001; Shaver, 1998) involving the variables storing group means. Let us consider the link TCI → CL for example. It allows us to estimate the path coef<sup>fi</sup>cient associated with the link CI → CL controlling for the effect of TCI, assuming that TCI and CI may be correlated. However, at the population level the correlation between TCI and CI may be because of the existence of a causal association instrumentally expressed by the link TCI → CI. If this is the case, TCI would also affect LO indirectly, through the network of links that connect these two variables. This would call for the inclusion of another direct link into the model: TCI → LO. Without this latter link, the path coef<sup>fi</sup>cient for the link CL → LO might be distorted by endogeneity; i.e. the correlation between TCI and the structural error term for the endogenous latent variable LO would not be accounted for.

Nevertheless, it is reasonable to assume that not including the direct link TCI → LO into the model would have a relatively minor biassing effect because the indirect effect of TCI on LO through the network of links that connect these two variables would likely be small. This is because of the fact that indirect effects in general tend to be small, because their magnitude is proportional to products of fractional coef<sup>fi</sup>cients, with each product signi<sup>fi</sup>cantly reducing the magnitude of the indirect effect.

The topic of multi-level data collection and analysis is complex and multi-faceted. The discussion presented here highlights key issues, and illustrates how multi-level data can in<sup>fl</sup>uence minimum sample size estimation. Including variables storing group means is not without prob lems, as we have seen above. For broader discussions on the topic and alternative approaches, the reader is referred to Klein & Kozlowski (2000), Preacher et al. (2010), Raudenbush & Bryk (2002), Snijders & Bosker (1999) and van Mierlo et al. (2009).
