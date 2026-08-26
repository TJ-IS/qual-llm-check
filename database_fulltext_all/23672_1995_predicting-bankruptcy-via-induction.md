---
otero_id: 23672
otero_key: "Z3TFX589"
title: "Predicting bankruptcy via induction"
authors: "Thomas E McKee"
year: "1995"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1995.4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Predicting bankruptcy via induction

THOMAS E. McKEE

Department of Accountancy, East Tennessee State University, PO Box 70710, Johnson City, TN 37614, USA

Research has consistently shown that auditors disclose going-concern problems for less than 50% of all business failures. As evidenced by widespread litigation, investors and creditors believe that this performance needs to be improved. This paper reports on research which analysed financial data for 60 public companies via an inductive inferencing algorithm. The end result was a simple and theoretically consistent model that was 97% accurate in predicting bankruptcy. Auditors, investors and creditors may find the model useful in improving their bankruptcy prediction capability.

## Introduction

A basic assumption underlying corporate financial reporting is that the entity will continue in existence for a reasonable time (i.e. is a going-concern). Auditors in the United States are required to modify their reports if the time period for existence is expected to be less than a year.

There have been a significant number of cases where businesses failed shortly after receiving unqualified audit reports. For example, Lincoln Savings and Loan and United American Bank are two highly publicized cases where entities that received unqualified audit reports were taken over by the US Government as failing institutions shortly after receiving their unqualified audit reports. Widely publicized business failures such as the previous two have given the public the perception, rightly or wrongly, that audit failures were also involved. Auditors, investors and creditors could benefit from an improvement in bankruptcy predictive ability.

Prediction of going-concern status can be a difficult problem for auditors. Research by Kida (1980) indicated that audit partners presented with a variety of going-concern data made accurate going-concern judgements only approximately 83% of the time.

Even when auditors can predict potential bankruptcy problems they are frequently reluctant to disclose that information due to the possible consequences of a going-concern report. Therefore, auditor predictive ability is significantly higher than auditor disclosure rates for going-concern problems. Research examining the frequency of auditor disclosures in the period prior to actual bankruptcy revealed that auditor disclosure rates have varied from a low of 15% (Deakin, 1977) to a high of 84% (Levitan and Knoblett, 1985) with a mode around 45% as evidenced by three other studies indicating disclosure rates of 43% (Menon and Schwartz, 1986), 44% (Altman and McGough, 1974) and 48% (Altman, 1982).

Auditors do a poor job of choosing which companies with going-concern problems should receive modified audit reports. Research which examined the actual status of companies for the year after they received a going-concern disclosure by their auditors revealed that, in one case, only approximately 25% (Altman, 1982) and, in another case, approximately 38% (Little and McAlum, 1991) of the companies actually went bankrupt in the year after they received a going-concern disclosure from their auditors.

There has been a significant amount of research oriented towards developing highly accurate models capable of predicting going-concern status. Asare (1990, p. 50) notes, 'Most of the studies indicate model superiority over auditors in assessing a client's going-concern status'. These models, especially when coupled with the related statistical assumptions, are fairly complex. Auditors appear to be reluctant to rely heavily on complex models that they poorly understand. Complex models which are highly accurate but seldom used will not improve auditors' predictive ability.

The objective of this research was to develop a highly accurate, theoretically consistent, but simple, model for bankruptcy prediction. The research employed an inductive inferencing algorithm developed for machine learning to extract knowledge structures from real world cases. Existing theory was then used to evaluate pruning choices among the various knowledge structures developed.

## Prior approaches to predicting going-concern status

Auditors have typically sought decision aids for making going-concern predictions. Considerable research has been devoted to developing empirically derived assistance or models to predict going-concern problems. This assistance may be classified into seven categories based on the underlying techniques employed. Assistance has taken the form of (1) check-lists of factors to consider, (2) univariate ratio models (Beaver, 1966), (3) multiple discriminant analysis (Altman, 1968), (4) multivariate conditional probability models (Ohlson, 1980), (5) expert systems (Messier and Hansen, 1988), (6) inductive inferencing techniques derived from machine learning research (Marais et al., 1984; Frydman et al., 1985) and, most recently, (7) neural networks (Bell et al., 1990; Hansen and Messier, 1991). Each type of assistance has advantages over unaided decisions, although all have potentially significant weaknesses which have been documented in the literature.

## Inductive inferencing algorithms

Inductive inference is the process of taking a series of examples or observations and generating an explanation for the behaviour observed. Dietterich and Michalski (1983, p. 43) note, 'The process of inductive learning can be viewed as a search for plausible general descriptions (inductive assertions) that explain the given input data and are useful for predicting new data'.

This study uses a data-driven method attributable to Quinlan (1979, 1982) which he called interactive dichotomizer 3 (ID3). The object of this method is to identify rules which will permit the correct classification of sample data into two or more categories. ID3 uses the information-theoretic measure of entropy to assess the information value of each variable. It develops a splitting point for each variable that is used to classify the sample data.

Tam and Kiang (1992, p. 943) note that ID3 employs a symbolic approach that, ‘. . . sheds some light on the importance of individual variables’. Thus, it can assist in evaluating the significance of the individual variables. This is not true for many other bankruptcy prediction techniques. For example, linear discriminant functions, neural nets and K nearest neighbour classifiers have been criticized for their failure to assist in identifying variable significance. Another widely used technique, logit analysis, does have rigorous statistical tests on the significance of individual variable coefficients but it does not do well with dimension reduction. On the other hand, ‘. . . the ID3 method has a built-in mechanism to reduce the dimensions of the variable space’ (Tam and Kiang, 1992, p. 943). Therefore, with respect to ability to analyse the significance of individual variables and the ability to reduce dimensions, ID3 offers comparative advantages over the classification techniques, linear discriminant functions, neural nets, K nearest neighbour classifiers and logit analysis.

Messier and Hansen (1988) compared the classification accuracy of ID3 against discriminant analysis for the problems of predicting loan defaults and predicting bankruptcy. The loan default sample included 46 US companies while the bankruptcy prediction sample included 23 Australian land development firms. They found that ID3 outperformed discriminant models in all cases tested.

## Example application of ID3

This section presents an example of how ID3 works. The example should aid in understanding the application of the ID3 algorithm in this study. In the example, the values for two ratios are analysed to develop a bankruptcy prediction rule.

Table 1 lists the values of two attributes, the current ratio and net income/total assets ratio, for six hypothetical companies. The example employs only ratios as attributes (variables), although non-financial attributes could be used as well.

To determine an initial splitting point for classifying the cases, ID3 proceeds by analysing each attribute (ratio) in the example set to determine if it will form an optimal classification rule. The purpose of a classification rule is to split the sample into two classification groups in a manner that minimizes the misclassifications. The measure for misclassification is the entropy (measure of disorder) designated $E(C)$ which is calculated for a sample according to the following formula:

$$
E (C) = - \sum_ {i = 1} ^ {n} p (c _ {i}) \log_ {2} p (c _ {i})\tag{1}
$$

where $i=1,\ldots,n$ is the index of possible classifications (in this case n=2, where i=1, bankrupt; i=2 not bankrupt), c is the classification group and $p(c_{1})$ is the probability of occurrence for class i (Messier and Hansen, 1988, p. 1408).

The probabilities for this formula are estimated from the overall sample. In this example, three of the six cases are in each of the two classification groups, so p = 0.5 (each attribute (ratio) has an equal prior probability of appearing in a classification group). Accordingly, to calculate the initial entropy of our example set before selecting a classification rule, we would calculate

Table 1 An example set of company ratios and bankruptcy outcomes

<table><tr><td>Company number</td><td>Current ratio</td><td>Net income/total assets ratio</td><td>Bankruptcy outcome</td></tr><tr><td>1</td><td>2.2</td><td>0.03</td><td>Non-bankrupt</td></tr><tr><td>2</td><td>1.1</td><td>0.04</td><td>Bankrupt</td></tr><tr><td>3</td><td>1.2</td><td>0.10</td><td>Non-bankrupt</td></tr><tr><td>4</td><td>1.4</td><td>-0.05</td><td>Bankrupt</td></tr><tr><td>5</td><td>1.6</td><td>0.01</td><td>Non-bankrupt</td></tr><tr><td>6</td><td>1.3</td><td>0.02</td><td>Bankrupt</td></tr></table>

$$
E (C) = - \left[ \left[ (0. 5) \log_ {2} (0. 5) \right] + \left[ (0. 5) \log_ {2} (0. 5) \right] \right]\tag{2}
$$

$$
E (C) = - \left[ [ (0. 5) (- 1) ] + [ (0. 5) (- 1) ] \right]\tag{3}
$$

$$
E (C) = 1\tag{4}
$$

This means that the initial entropy for the data set in the example is 1.

In this example, the current ratio is designated as attribute A with values $a_{1}, a_{2}, \ldots, a_{6}$ and the net income/total assets ratio as attribute B with values $b_{1}, b_{2}, \ldots, b_{6}$ . Our example set can be split on one of these two attributes by determining which variable will provide the best classification. Since entropy is used to measure classification success, the goal is to split on the variable that will minimize the entropy. To determine which variable offers the best split, ID3 actually computes the change in entropy occurring from each possible splitting point. This can involve a lot of calculations when there are many attributes with numerous values. Rather than making all these computations for our example data set, a visual selection of the best splitting point will be made and the computations to calculate the entropy improvement will be illustrated for that point.

To facilitate the visual selection of the best splitting point the example set is sorted into ascending order based upon the current ratio as indicated in Table 2. A visual inspection of Table 2 indicates that the best splitting rule for the current ratio is to classify all companies with a current ratio of 1.6 or higher as non-bankrupt. This rule would only misclassify one company. It would classify company 3 in the bankrupt group even though it was a non-bankrupt company.

Table 2 Example set sorted on current ratio in ascending order

<table><tr><td>Company number</td><td>Current ratio</td><td>Net income/total assets ratio</td><td>Bankruptcy outcome</td></tr><tr><td>2</td><td>1.1</td><td>0.04</td><td>Bankrupt</td></tr><tr><td>3</td><td>1.2</td><td>0.10</td><td>Non-bankrupt</td></tr><tr><td>6</td><td>1.3</td><td>0.02</td><td>Bankrupt</td></tr><tr><td>4</td><td>1.4</td><td>-0.05</td><td>Bankrupt</td></tr><tr><td>5</td><td>1.6</td><td>0.01</td><td>Non-bankrupt</td></tr><tr><td>1</td><td>2.2</td><td>0.03</td><td>Non-bankrupt</td></tr></table>

Table 3 Example set classified using 1.6 as splitting point

<table><tr><td rowspan="2">Splitting point</td><td colspan="2">Number of classifications</td></tr><tr><td>Bankrupt</td><td>Non-bankrupt</td></tr><tr><td>&lt;1.6</td><td>3</td><td>1</td></tr><tr><td>≥1.6</td><td>0</td><td>2</td></tr></table>

Table 4 Table 3 displayed as a $2 \times 2$ probability table

<table><tr><td rowspan="2">Splitting point</td><td colspan="2">Frequency of classifications</td></tr><tr><td>Bankrupt</td><td>Non-bankrupt</td></tr><tr><td>&lt;1.6</td><td>0.5</td><td>0.1667</td></tr><tr><td>≥1.6</td><td>0</td><td>0.3333</td></tr></table>

The classification of the six examples using a current ratio of $\geqslant1.6$ as a splitting point is displayed in a $2\times2$ frequency table (Table 3). These frequencies may be displayed as probabilities (Table 4).

When a data set is split around a splitting point, the data on each side of the splitting point forms a subtable. The entropy of each subtable $E(C \mid a_{j})$ is given by

$$
E (C \mid A) = - \sum_ {i = 1} ^ {n} p (c _ {i} \mid a _ {j}) \log_ {2} p (c _ {i} \mid a _ {j})\tag{5}
$$

where n is the number of subsets of $c_{i}$ .

Using the formula for calculating subtable entropy, the entropy for the subset represented by the values <1.6 is calculated as follows:

$$
\begin{array}{r l} E (C \mid <   1. 6) = & - \left[ \left(\frac {0 . 5}{0 . 5 + 0 . 1 6 7} \log_ {2} \frac {0 . 5}{0 . 5 + 0 . 1 6 7}\right) \right. \\ & \left. + \left(\frac {0 . 1 6 7}{0 . 1 6 7 + 0 . 5} \log_ {2} \frac {0 . 1 6 7}{0 . 1 6 7 + 0 . 5}\right) \right] \end{array}\tag{6}
$$

$$
E (C \mid <   1. 6) = - [ (0. 7 5 \log_ {2} 0. 7 5) + (0. 2 5 \log_ {2} 0. 2 5) ]\tag{7}
$$

$$
E (C \mid <   1. 6) = - [ (0. 7 5 (- 0. 4 1 5)) + (0. 2 5 (- 2)) ]\tag{8}
$$

$$
E (C \mid <   1. 6) = 0. 8 1 1\tag{9}
$$

In a similar manner, the entropy for the subset represented by the values $\geqslant1.6$ can be calculated as 0 (there is no disorder since there is no misclassification). The entropy for the entire table after the split around the current ratio of 1.6 is then calculated according to the following formula:

$$
E (C \mid A) = \sum_ {j = 1} ^ {M} p (a _ {j}) E (A \mid a _ {j})\tag{10}
$$

where M is the number of subsets. For the previous example, this becomes

$$
E (C \mid A) = \left(\frac {4}{6} 0. 8 1 1\right) + \left(\frac {2}{6} 0\right)\tag{11}
$$

$$
E (C \mid A) = 0. 5 4 1\tag{12}
$$

Since the initial entropy was 1 before any splitting took place, splitting at this point yields an improvement of 0.459 $[1 - 0.541 = 0.459]$ . Entropy improvement occurs because the disorder in the data is reduced.

In the absence of a visual selection of the best splitting point, it is normally only possible to determine if a single point is the optimum splitting point by calculating the entropy improvement for all other possible splitting points. Table 5 displays the values that would be obtained by calculating the entropy improvement for each possible splitting point for the current ratio. It confirms the conclusion that the visually selected splitting point is the best.

Once the best splitting point for the current ratio is calculated, the next step is to compare that with the best splitting point for the net income/total assets ratio to see which ratio should be used for the initial split. Table 6 shows the entropy improvements achieved for all possible splitting points of the net income/total assets ratio. Table 6 reveals that the maximum entropy improvement possible by splitting on the net income/total assets ratio is 0.191, which is considerably less than the 0.459 improvement possible from splitting on the current ratio. Accordingly, the sample of six cases would first be split into two groups based on the current ratio splitting point of <1.6. As shown by Table 2, the group $\geqslant$ 1.6 contains two cases which are perfectly classified, so no further splits would be considered on this group. The group <1.6 contains four cases and needs further classification since it contains both bankrupt and non-bankrupt cases.

Table 5 Entropy improvement for various current ratio splitting points

<table><tr><td>Splitting point</td><td>Initial entropy</td><td>Post-split entropy</td><td>Improvement</td></tr><tr><td>&lt;1.1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>&lt;1.2</td><td>1</td><td>0.809</td><td>0.191</td></tr><tr><td>&lt;1.3</td><td>1</td><td>1</td><td>0</td></tr><tr><td>&lt;1.4</td><td>1</td><td>0.918</td><td>0.082</td></tr><tr><td>&lt;1.6</td><td>1</td><td>0.541</td><td>0.459</td></tr><tr><td>&lt;2.2</td><td>1</td><td>0.809</td><td>0.191</td></tr><tr><td>&gt;2.2</td><td>1</td><td>1</td><td>0</td></tr></table>

Table 6 Entropy improvement for various net income/total assets ratio splitting points

<table><tr><td>Splitting point</td><td>Initial entropy</td><td>Post-split entropy</td><td>Improvement</td></tr><tr><td>&lt;-0.05</td><td>1</td><td>1</td><td>0</td></tr><tr><td>&lt;0.01</td><td>1</td><td>0.809</td><td>0.191</td></tr><tr><td>&lt;0.02</td><td>1</td><td>1</td><td>0</td></tr><tr><td>&lt;0.03</td><td>1</td><td>0.918</td><td>0.082</td></tr><tr><td>&lt;0.04</td><td>1</td><td>1</td><td>0</td></tr><tr><td>&lt;0.10</td><td>1</td><td>0.809</td><td>0.191</td></tr><tr><td>&gt;0.10</td><td>1</td><td>1</td><td>0</td></tr></table>

At this point, ID3 would consider the four remaining cases in the group <1.6 as a new classification problem and proceed to use all the previously illustrated formulae to determine a splitting point for these cases. This analysis is not shown but would yield a splitting point of $\geqslant0.1$ for the net income/total assets ratio for a non-bankruptcy classification.

The final decision tree obtained by ID3 splitting the example cases is displayed in Figure 1. As you can see in Figure 1, ID3 developed a two-stage rule that classified all six cases perfectly. The rule is:

If the current ratio is greater than or equal to 1.6 and if the net income/total assets ratio is greater than or equal to 0.1, then the company will not go bankrupt, else the company will go bankrupt.

![](/api/attachments/Z3TFX589/fulltext/images/bec1468ff90643d20db5510b7e8e8ffb4eb05836c717b91e1d23708a833e2e95.jpg)  
Figure 1 Decision tree for example cases. Cases to be classified, rectangle; non-terminal nodes (non-terminal subsets), circles; terminal nodes (terminal subsets), squares; bankrupt firms, B; non-bankrupt firms, NB

## The current research

This research used the ID3 inductive inferencing algorithm to extract knowledge structures from data on 60 actual companies. Once the knowledge structures were extracted, a previously published theory with related model was used to select the data utilized and to evaluate pruning choices among the various knowledge structures.

## Guiding theoretical model

McKee (1986) proposed a temporal continuity theory to replace the classical going-concern concept. This theory suggested variables that might be appropriate for predicting going-concern status. It also provided a basis for evaluating the knowledge structures developed.

The temporal continuity theory posits that a firm has a planning or operating horizon related to resource commitments made by the firm. A firm processing continuity must have ‘. . . expectations of both sufficient current resources to fulfil its commitments and sufficient market returns or benefits flowing to it’ (McKee, 1986, p. 27). ‘Current resources’ refers to either the actual liquid assets available or that may be made available (i.e. a line of credit) to an entity. It may be estimated using a variety of current liquidity surrogates. For example, the current ratio is a common current liquidity surrogate. ‘Sufficient market returns’ refers to the prospect of future cash flows to the entity. These cash flows may be generated from earning capacity or borrowing capacity based on future earning potential. Surrogates for estimating future cash flows are projected earnings or projected cash flows.

## Ratios selected

This research utilized the following eight ratios: (1) net income/total assets (NI/TA), (2) current assets/total assets (CA/TA), (3) current assets/current liabilities (CA/CL), (4) cash/total assets (CASH/TA), (5) current assets/sales (CA/SALES), (6) long-term debt/total assets (LTD/TA), (7) inventory/cost of goods sold (INV/COGS) and (8) accounts receivable/sales (AR/SALES).

The first six ratios provide comparability with prior research and were obtained from the Hopwood et al. (1989) study. They derived those ratios from the Beaver (1966), Deakin (1977) and Libby (1975) studies. Many of those ratios were also used by a variety of other researchers exploring the bankruptcy prediction problem. The last two ratios were obtained from McKee (1989). They are turnover ratios that prior research has suggested are significant in analysing the current financial liquidity of a company. The eight ratios were viewed as possible surrogates for the theoretical constructs ‘current resources’ and ‘sufficient market returns’.

## Data and definitions

Sixty companies were selected from Compact Disclosure which reports financial data for all public companies filing with the US Securities and Exchange Commission (Disclosure Incorporated, 1990). The fiscal years utilized spanned the 4 year period 1986–1989. One-half of these companies were defined as going-concerns and one-half were defined as non-going-concerns.

Going-concerns were defined in this study as companies having a positive cash flow from operations for the most recent 5 year period. Non-going-concerns were defined as companies that have either filed for bankruptcy or had a significant subsidiary file for bankruptcy.

A minimum existence period of 5 years was adopted for companies utilized in this study to eliminate start-up companies from consideration in this research.

In order to provide evidence on the issue of whether a general or industry-specific model provides the best predictions, 20 of the 60 companies selected were chosen solely from the electronics industry (standard industrial classification 367). That industry was chosen due to the high number of failed companies during the time period the data was selected from. The remaining 40 companies were randomly selected from the database and included a variety of industries.

Table 7 contains a listing of 60 companies from a variety of industries along with related data about fiscal periods, company size and standard industrial classification number.

As revealed in Table 7 the asset sizes of companies employed in this study varied from approximately \$300 000 to \$33 000 000 000. The possible effects of asset size were mitigated through the use of scaled ratios. Ratios were converted to percentile rankings based on the sample group.

## Results

The data were analysed using EXPERT-EASE, an inductive inferencing software system employing ID3 (Human Edge Software Corporation, 1983).

The data for 60 companies was used to form three different knowledge base sources.

(1) Twenty company single industry sample.

(2) Forty company multiple industry sample.

(3) Sixty company multiple industry sample.

Each knowledge base had an equal number of bankrupt and non-bankrupt companies. Each knowledge base source was analysed using both unscaled ratios and ratios scaled between 0 and 100, based on sample percentiles, thus forming a total of six knowledge base sources.

The remaining cases (either 20 or 40) formed a validation sample for the first two knowledge base sources listed. Since all cases were used to form the knowledge bases in the 60 company samples there was no validation sample available for this knowledge base source.

Table 7 Sample companies

<table><tr><td>Company name</td><td>Bankruptcy date</td><td>Financial statement date</td><td>Total assets ($1000)</td><td>SIC number</td></tr><tr><td colspan="5">Bankruptcy companies</td></tr><tr><td>ACA Joe Inc.</td><td>05.27.88</td><td>01.31.87</td><td>20 991</td><td>5136</td></tr><tr><td>ANAC Holding Corp.</td><td>07.28.88</td><td>05.30.87</td><td>2095 838</td><td>5912</td></tr><tr><td>Basix Corp.</td><td>02.29.88</td><td>12.31.87</td><td>172 605</td><td>6159</td></tr><tr><td>Bercor Inc.</td><td>06.23.88</td><td>04.03.87</td><td>72 360</td><td>5064</td></tr><tr><td>Berkey Inc.</td><td>07.20.88</td><td>12.31.87</td><td>80 869</td><td>5043</td></tr><tr><td>Cardis Corp.</td><td>05.25.88</td><td>04.30.87</td><td>188 565</td><td>5013</td></tr><tr><td>Care Enterprises</td><td>03.28.88</td><td>12.31.87</td><td>215 465</td><td>8051</td></tr><tr><td>Detroit Texas Gas</td><td>11.02.87</td><td>02.28.85</td><td>30 723</td><td>1311</td></tr><tr><td>First Republic Bank</td><td>07.30.88</td><td>12.31.87</td><td>33 210 686</td><td>6028</td></tr><tr><td>Gibraltar Financial</td><td>02.08.90</td><td>12.31.88</td><td>15 011 110</td><td>6122</td></tr><tr><td>Hauserman Inc.</td><td>10.05.89</td><td>06.30.88</td><td>79 496</td><td>2541</td></tr><tr><td>Hydrogen Energy</td><td>09.30.89</td><td>12.31.88</td><td>2285</td><td>7392</td></tr><tr><td>Interdyne Co.</td><td>11.22.88</td><td>10.31.86</td><td>4555</td><td>3573</td></tr><tr><td>International Texas</td><td>05.19.89</td><td>04.30.88</td><td>1174</td><td>3842</td></tr><tr><td>Jumping Jack Shoes</td><td>02.06.90</td><td>04.30.89</td><td>24 377</td><td>3149</td></tr><tr><td>Kaypro Corp.</td><td>07.10.87</td><td>01.30.86</td><td>26 672</td><td>3573</td></tr><tr><td>Kenai Corp.</td><td>07.10.87</td><td>01.31.86</td><td>47 048</td><td>3533</td></tr><tr><td>L.F. Rothschild</td><td>06.30.89</td><td>06.30.88</td><td>2 778 222</td><td>6200</td></tr><tr><td>Lankmark American</td><td>01.30.90</td><td>12.31.88</td><td>46 417</td><td>NA</td></tr><tr><td>Lapointe Industries</td><td>02.10.89</td><td>06.30.88</td><td>6361</td><td>3662</td></tr><tr><td>ADI Electronics</td><td>10.30.86</td><td>07.31.85</td><td>13 700</td><td>367</td></tr><tr><td>Dense Pac</td><td>02.10.87</td><td>02.28.86</td><td>4503</td><td>367</td></tr><tr><td>Domain Technology</td><td>06.26.89</td><td>06.30.88</td><td>60 069</td><td>367</td></tr><tr><td>Final Test</td><td>03.10.89</td><td>12.31.87</td><td>2186</td><td>367</td></tr><tr><td>Koss Corp.</td><td>12.21.84</td><td>06.30.83</td><td>25 641</td><td>367</td></tr><tr><td>Labarge</td><td>12.31.86</td><td>06.30.85</td><td>86 705</td><td>367</td></tr><tr><td>Semicon</td><td>10.06.87</td><td>06.30.86</td><td>35 644</td><td>367</td></tr><tr><td>Solitron Devices</td><td>05.11.89</td><td>02.28.88</td><td>58 529</td><td>367</td></tr><tr><td>Spectrascan</td><td>07.21.89</td><td>10.31.88</td><td>303</td><td>367</td></tr><tr><td>Technodyne</td><td>08.01.89</td><td>07.30.88</td><td>45 557</td><td>367</td></tr><tr><td colspan="5">Non-bankruptcy companies</td></tr><tr><td>A.A. Importing Co.</td><td></td><td>02.02.88</td><td>16 042</td><td>5719</td></tr><tr><td>A.T. Cross Co.</td><td></td><td>12.31.89</td><td>196 315</td><td>3951</td></tr><tr><td>Abatix Environmental Corp.</td><td></td><td>12.31.89</td><td>3076</td><td>5080</td></tr><tr><td>Academy Computing Corp.</td><td></td><td>12.31.89</td><td>1273</td><td>7374</td></tr><tr><td>Acuson Corp.</td><td></td><td>12.31.89</td><td>183 879</td><td>3811</td></tr><tr><td>ADC Telecommunications</td><td></td><td>10.31.89</td><td>143 831</td><td>3661</td></tr><tr><td>Advance Ross Corp.</td><td></td><td>12.31.89</td><td>16 387</td><td>3564</td></tr><tr><td>AEP Industries Inc.</td><td></td><td>10.31.89</td><td>65 573</td><td>3079</td></tr><tr><td>Beeba S. Creations Inc.</td><td></td><td>08.31.89</td><td>51 883</td><td>5137</td></tr><tr><td>BEI Electronics Inc.</td><td></td><td>09.30.89</td><td>53 907</td><td>3483</td></tr><tr><td>Berry Petroleum Co. Calif.</td><td></td><td>12.31.89</td><td>115 597</td><td>1311</td></tr><tr><td>Bio Logic Systems Corp.</td><td></td><td>02.28.89</td><td>10 334</td><td>7372</td></tr><tr><td>Central Sprinker Corp.</td><td></td><td>10.31.89</td><td>55 989</td><td>3569</td></tr><tr><td>Devon Group Inc.</td><td></td><td>03.31.89</td><td>134 603</td><td>2791</td></tr><tr><td>E. Systems Inc.</td><td></td><td>12.31.89</td><td>852 145</td><td>3674</td></tr><tr><td>Fastenal Co.</td><td></td><td>12.31.89</td><td>21 534</td><td>5070</td></tr><tr><td>Frank E. Best Inc.</td><td></td><td>12.31.88</td><td>46 488</td><td>3429</td></tr><tr><td>General Ceramics Inc.</td><td></td><td>06.30.88</td><td>27 451</td><td>3264</td></tr><tr><td>IIS Intelligent Information</td><td></td><td>12.31.88</td><td>34 025</td><td>3573</td></tr><tr><td>Kelly Services</td><td></td><td>12.31.89</td><td>394 283</td><td>7362</td></tr><tr><td>Advance Circuits</td><td></td><td>08.29.87</td><td>40 221</td><td>367</td></tr><tr><td>Bel Fuse</td><td></td><td>12.31.86</td><td>24 390</td><td>367</td></tr><tr><td>DEL Electronics</td><td></td><td>08.01.87</td><td>3997</td><td>367</td></tr><tr><td>Espey Mfg</td><td></td><td>06.30.87</td><td>20 414</td><td>367</td></tr><tr><td>Int&#x27;l Power Machines</td><td></td><td>12.31.86</td><td>13 491</td><td>367</td></tr><tr><td>Kevlin Microwave</td><td></td><td>05.31.87</td><td>7298</td><td>367</td></tr><tr><td>Methode Electronics</td><td></td><td>04.30.87</td><td>62 973</td><td>367</td></tr><tr><td>Supertex</td><td></td><td>03.31.87</td><td>11 418</td><td>367</td></tr><tr><td>Technitrol</td><td></td><td>12.31.86</td><td>25 788</td><td>367</td></tr><tr><td>Zitel Corp.</td><td></td><td>09.30.86</td><td>13 141</td><td>367</td></tr></table>

Note: this study classified companies in the bankruptcy group if either the company or a significant subsidiary filed for bankruptcy. Thus, some of the companies listed in the bankruptcy column may not have filed for bankruptcy but rather had a significant subsidiary to do so.

An additional knowledge base was formed from ratio values rounded to the nearest multiple of 10 (i.e. a value of 26.8 on a 0–100 scale would be rounded to 30). This reduced the complexity of the classification problem by only providing 11 possible values to consider for each ratio rather than 101. This reduced the number of splitting points. It was theorized that the reduced complexity might improve the development of a knowledge structure.

The classification accuracy for the seven previously described knowledge base sources is presented in Table 8. As illustrated in Table 8, the inductive inferencing algorithm was able to achieve 100% accuracy on all seven knowledge base sources. This accuracy level on the knowledge bases is not surprising since the algorithm will continue splitting the sample data, if possible, until no misclassifications exist. In fact, one valid criticism of this technique is that it is prone to extreme overfitting. This weakness is mitigated in this study since the cognitive structures were ‘pruned’ to a less complex form using existing theory.

## Developing a single cognitive system

The next step in this research was to try to identify which cognitive structure offered the best general predictive ability. The objectives were to determine to what extent the cognitive structures may have overfitted the data and to what extent the knowledge structures overlap.

The data in Table 8 generally indicate that the cognitive systems developed from the scaled ratios were more accurate than the ones developed from the unscaled ratios, even though the same ratios were used to develop both groups of structures. The process of scaling the ratios apparently adds to their information value. Accordingly, due to their lower accuracy levels, the three knowledge structures developed from the unscaled ratios were eliminated from further consideration.

## Pruning the cognitive structures

Since ID3 performs a stepwise splitting that attempts to optimize at each individual split, rather than on an overall basis, it may oversplit (overfit) the data. Oversplitting occurs when a terminal node has one or a few cases that have been split into that node on an arbitrary rather than a logical basis. Breiman et al. (1984, p. 60) note, 'Too large a tree will have a higher true misclassification rate than the right size tree. On the other hand, too small a tree will not use some of the classification information available . . .' Research has indicated that the best approach is to let trees grow to the maximum size based on the splitting rule and then 'prune' them back to an appropriate size. Pruning is frequently accomplished by a backward dynamic programming algorithm. However, due to the small number of trees in the current research, the following two theory-based, simple, pruning rules were utilized.

Table 8 Classification accuracy for different knowledge bases developed

<table><tr><td>Knowledge base source</td><td>Ratios in order utilized</td><td>Development sample accuracy (%)</td><td>Validation sample accuracy (%)</td></tr><tr><td colspan="4">Unscaled ratios</td></tr><tr><td>Twenty company single industry sample</td><td>CASH/TACA/CLCA/TA</td><td>100</td><td>80</td></tr><tr><td>Forty company multiple industry sample</td><td>CA/CL</td><td>100</td><td>75</td></tr><tr><td>Sixty company multiple industry sample</td><td>CA/CLNI/TACASH/TA</td><td>100</td><td>None</td></tr><tr><td colspan="4">Scaled ratios</td></tr><tr><td>Twenty company single industry sample</td><td>CA/CLCA/TANI/TA</td><td>100</td><td>90</td></tr><tr><td>Forty company multiple industry sample</td><td>CA/CL</td><td>100</td><td>85</td></tr><tr><td>Sixty company multiple industry sample</td><td>CA/CLNI/TA</td><td>100</td><td>None</td></tr><tr><td>Twenty company single industry sample with ratios rounded to nearest tenth</td><td>CA/CLNI/TAAR/SALESCA/TA</td><td>100</td><td>97.5</td></tr></table>

Note: data from 60 companies were utilized in this study. When the knowledge base was developed from a sample of these companies, the remaining companies comprised the validation sample.

(1) Pruning rule 1: eliminate a node if the direction of the split is inconsistent with theory.

(2) Pruning rule 2: eliminate a node if the ratio used to determine the split has been previously used in the tree.

The logic behind the first pruning rule is simply that all splits should be theoretically logical. For example, if the splitting rule classified a company as a going-concern based on a lower current ratio, such a split would not be acceptable. The logic behind the second rule is that since the splitting rule can only split in a linear fashion (i.e. all splits are perpendicular to the coordinate axes), the classification power of a ratio is primarily used on the first split. Accordingly, a second split with the same ratio would be expected to have minimal classification power and would probably result in overfitting.

Figure 2 displays the decision tree that had the highest validation sample accuracy level. Application of the two pruning rules to this tree produced a nine-node decision tree, thus reducing the complexity of the decision tree. Pruning on the other knowledge structures also resulted in less complex decision trees.

## Extracting the final knowledge structure

The next step in the research was to see if the ratios included and their order of inclusion in the four pruned-knowledge structures could provide guidance on how to form an ‘optimal’ knowledge structure.

A review of the four pruned-knowledge structures developed from the scaled ratios indicates that the first ratio selected in every structure was the current ratio. This means that this research strongly indicates that a current liquidity measure, the current ratio, is the best single predictor of bankruptcy. This conclusion is consistent with the results of the Messier and Hansen (1988) study which found the current ratio to be the most significant predictor based on two different samples of data.

If we assume that the current ratio can adequately measure current liquidity then we can exclude all other current liquidity measures from consideration. When all current liquidity measures are excluded from consideration, an analysis of the four knowledge structures indicates that only other ratio to be selected was the NI/TA ratio, a profitability measure. It was selected second in two of the four knowledge structures and selected third in one of the four knowledge structures. This indicates that, after excluding current liquidity measures, the NI/TA ratio is the second best predictor of bankruptcy. This is partially consistent with the Messier and Hansen (1988) study since they found a profitability measure to be the second most significant ratio in one of their two data sets and the third most significant ratio in the other one of their two data sets.

![](/api/attachments/Z3TFX589/fulltext/images/3efb16cf724e0b319df483fe7bd4b3e3c8effa15388071d594693b00a3331443.jpg)  
Figure 2 Fifteen-node cognitive structure developed from 20 company single industry sample of scaled ratios rounded to the nearest tenth. Non-terminal nodes (non-terminal subsets), circles; terminal nodes (terminal subsets), squares; going-concerns, GC; non-going concerns, NGC

The previous review and related assumptions indicate that an optimal knowledge structure would have the current ratio, a current liquidity surrogate, as the first ratio and the net income/total assets ratio, a profitability surrogate, as the second ratio. The next step was to review the pruned-knowledge structures to see if any actual splits were consistent with the optimal knowledge structure.

The knowledge structure pruned from the nine-node knowledge structure developed from all 60 companies was the only one that incorporated the current ratio and the net income/total assets ratio for the first two splits in a manner consistent with the previous analysis. Accordingly, two splitting points from that structure were used in the optimal knowledge structure. Since the current ratio was used only once in the pruned knowledge structure that splitting point was used in the optimal knowledge structure. The NI/TA ratio was used twice in the pruned knowledge structure, so a decision had to be made as to which splitting should be used. On a judgemental basis, the most restrictive splitting point for the NI/TA ratio in the original structure was adopted as the splitting point for this ratio in the optimal knowledge structure.

Figure 3 contains the final optimal knowledge structure developed. It was 97% accurate (two going-concerns were misclassified) when tested on all 60 cases.

## Integration with a theoretical model

The final optimal knowledge structure developed in this research is consistent with the temporal continuity theory model. The two ratios identified through the current research, the current ratio and the net income/total assets ratio are surrogates for the ‘current resources’ and ‘positive long-run resource flows’ in the temporal continuity theory. Also, the final optimal knowledge structure includes them in an order that is consistent with the temporal continuity theory. Thus, this research indicates that the final optimal cognitive system is an empirically successful implementation of the temporal continuity model in the form:

![](/api/attachments/Z3TFX589/fulltext/images/4d6bb69447c8f92af8189d67c3052014a21d768e11f493e63286621459ae3a59.jpg)  
Figure 3 Five-node cognitive structure developed from pruned cognitive structures (96.7% accurate on 60 company sample). Non-terminal nodes (non-terminal subsets), circles; terminal nodes (terminal subsets), squares; going-concerns, GC; non-going concerns, NGC

If the scaled current ratio is $\geqslant24$ and if the scaled net income/total assets ratio is $\geqslant81$ , then the firm will not go bankrupt, else the firm will go bankrupt.

In summary, the final knowledge structure developed was 97% accurate in classifying all 60 companies and was consistent with the previously posited continuity theory.

## Limitations

Since ID3 determines prior probabilities from the original sample proportions and all samples had an equal number of bankrupt and non-bankrupt firms, the prior probabilities used in this research were equal. This could be considered a limitation since several earlier bankruptcy prediction studies using other techniques have been criticized for assuming equal prior probabilities. However, this assumption was deemed appropriate for this study since prior probabilities can vary substantially depending on the population from which they are selected.

Another limitation concerns misclassification costs. Although it is recognized that the cost of misclassifying a bankrupt firm as non-bankrupt may differ from the cost of misclassifying a non-bankrupt firm as bankrupt, these misclassification costs were assumed to be equal in this study. As noted by Marais et al. (1984) in a research study using a similar technique, 'Proper specification of the loss function may be a research project in itself . . .' (p. 95).

The final limitation is that the pruning rules adopted and the process of determining the optimal model, although supported by theory, were somewhat subjective.

## Discussion and conclusions

Business failure in the form of bankruptcy imposes significant costs on stakeholders such as investors and creditors. These stakeholders have indicated that they believe that auditors are in a unique position to signal them about possible bankruptcy problems so they can minimize such costs. The frequency and amount of settlements in court cases filed against auditors associated with business failures that were not signalled to stakeholders indicates that auditors pay a price for not meeting stakeholder expectations.

Auditors have used a variety of decision aids including complex statistical models to assist them in making going-concern judgments. Research indicates that experienced auditors can only correctly forecast bankruptcy approximately 83% of the time. It also indicates that auditors only disclose possible bankruptcy for approximately 45% of the companies that actually go bankrupt within 1 year after receiving the auditors' report. Furthermore, very recent research indicates that 62% of the companies receiving a going-concern modification in their auditors' report did not go bankrupt in the year after receiving that report. Clearly, auditors have a difficult time forecasting and disclosing bankruptcy.

This research has focused on developing a decision model to assist auditors, investors and creditors in forecasting bankruptcy. It employed a data-driven approach, an inductive inferencing algorithm developed for machine learning, with a model-driven approach and use of an existing bankruptcy theory model. It is hoped that this approach has resulted in a more robust model. The final model developed used only two publicly available ratios and was 97% accurate in classifying the bankruptcy status of 60 public companies. The model employed scaled versions of the current ratio and the net income to total assets ratio in a simple decision rule. To be widely accepted by auditors, the model, of course, would need to be further tested on a much larger sample of companies. Nevertheless, it suggests that perhaps a simple, theoretically consistent model may exceed current auditor predictive capabilities.

The simplicity of the final model and the fact that it uses ratios which are readily available for public companies suggests that many stakeholders could themselves make fairly accurate assessments of bankruptcy possibilities for the types of companies included in this study. This raises the question of whether auditors can or should influence such objective assessments by incorporating their opinions about management's plans and capabilities to deal with the factors that would lead a company into bankruptcy. Perhaps auditor training and the available professional guidance does not provide an adequate basis for expressing such an opinion.

The two-ratio model developed in this study should be useful to auditor, investor, creditors and other stakeholders in making highly accurate bankruptcy predictions.

## Acknowledgement

The author would like to acknowledge support provided by Massey University, New Zealand while conducting part of this research.

## References

Altman, E.I. (1968) Financial ratios, discriminant analysis and the prediction of corporate bankruptcy. Journal of Finance, XXIII (4), 589–609.

Altman, E.I. (1982) Accounting implications of failure

prediction models. Journal of Accounting, Auditing, and Finance, 6 (1), 4–19.

Altman, E.I. and McGough, T. (1974) Evaluation of a company as a going-concern. Journal of Accountancy, 138 (6), 51–7.

Asare, S.K. (1990) The auditor's going-concern decision: a review and implications for future research. Journal of Accounting Literature, 9, 39–64.

Beaver, W. (1966) Financial ratios as predictors of failure. Journal of Accounting Research, 4 (Suppl.), 71–111.

Bell, T.B., Ribar, G.S. and Verchio, J. (1990) Neural nets versus logistic regression: a comparison of each model's ability to predict commercial bank failures, in Proceedings of the 1990 Deloitte & Touche/University of Kansas Symposium on Auditing Problems, (University of Kansas) pp. 29–54.

Breiman, L., Friedman, J.H., Olshen, R.A. and Stone, C.J. (1984) Classification and Regression Trees (Wadsworth International Group, Belmont, CA).

Deakin, E.B. (1977) Business failure prediction: an empirical analysis, in Financial Crises: Institutions and Markets in a Fragile Environment, Altman, E.I. and Sametz, A.W. (eds) (John Wiley & Sons, New York) pp. 72–88.

Dietterich, T.G. and Michalski, R.S. (1983) A comparative review of selected methods for learning from examples, in Machine Learning: An Artificial Intelligence Approach, Michalski, R.S., Carbonell, J.G. and Mitchell, T.M. (eds) (Tiogo Publishing, Palo Alto, CA) pp. 41–81.

Disclosure Incorporated (1990) Compact Disclosure (Bethesda, Maryland).

Frydman, H., Altman, E.I. and Kao, D. (1985) Introducing recursive partitioning for financial classification: the case of financial distress. Journal of Finance, 40 (1), 269–91.

Hansen, J.V. and Messier, W.F. Jr (1991) Artificial neural networks: foundations and application to a decision problem. Expert Systems with Applications, 3, 135–41.

Hopwood, W., McKeown, J. and Mutchler, J. (1989) A test of the incremental explanatory power of opinions qualified for consistency and uncertainty. The Accounting Review, LXIV (1), 28–48.

Human Edge Software Corporation (1983) EXPERT-EASE (Palo Alto, CA).

Kida, T. (1980) An investigation into auditor's continuity and related qualifications. Journal of Accounting Research, 18(2), 506–23.

Levitan, A.S. and Knoblett, J.A. (1985) Indicators of exceptions to the going-concern assumption. Auditing: A Journal of Practice and Theory, 5 (2), 26–39.

Libby, R. (1975) The use of simulated decision makers in information evaluation. The Accounting Review, L (3), 475–89.

Little, P. and McAlum, H. (1991) Subsequent events for companies receiving going concern audit opinions. Southern Business Review, 17 (2), 22–32.

McKee, T.E. (1986) Why can't accountants deal with uncertainty about enterprise continuity? Management Accounting, LXVIII(1) July, 24–9.

McKee, T.E. (1989) Modern Analytical Auditing (Greenwood Press, Westport, Connecticut).

Marais, M., Patell, J. and Wolfson, M. (1984) The experimental design of classification models: an application of recursive partitioning and bootstrapping to commercial bank loan

classifications. Journal of Accounting Research, 22(Suppl.), 87–114.

Menon, K. and Schwartz, K. (1986) The auditor's report for companies facing bankruptcy. Journal of Commercial Bank Lending, 168 (1), 42–52.

Messier, W.F. Jr and Hansen, J.V. (1988) Inducing rules for expert system development: an example using default and bankruptcy data. Management Science, 34 (12), 1403–15.

Ohlson, J. (1980) Financial ratios and the probabilistic prediction of bankruptcy. Journal of Accounting Research, 18 (1), 109–31.

Quinlan, J.R. (1979) Induction Over Large Databases, Report HPP-79-14 (Stanford University).

Quinlan, J.R. (1982) Semi autonomous acquisition of pattern-based knowledge, in Introductory Readings in Expert Systems, Michie, D. (ed.) (Gordon and Breach, Newark, N.J.).

Tam, K.Y. and Kiang, M.Y. (1992) Managerial applications of neural networks: the case of bank failure predictions. Management Science, 38 (7), 926–47.

## Biographical notes

Thomas E. McKee is currently Chairman and Professor of Accountancy at East Tennessee State University. He also holds a Professor II appointment at the Norwegian School of Economics and Business Administration. He has been a Visiting Professor at Massey University, New Zealand, the Norwegian School of Economics and Business Administration and the University of Tennessee. He has also been a member of the faculties at the University of

Maryland and Georgia State University. Prior to that he was a senior accountant with Price Waterhouse.

Professor McKee has authored or co-authored several books including an auditing textbook titled Auditing (currently the 5th edition) and an auditing professional reference book titled Analytical Auditing (1989). He has written numerous articles which have appeared in publications such as the Journal of Accountancy, Internal Auditor, The CPA Journal, The Practical Accountant, Accounting Education, Advances In Accounting and Intelligent Systems in Accounting, Finance, and Management.

Professor McKee annually makes numerous speeches and technical presentations on different contemporary accounting and auditing topics for a variety of audiences. He consistently receives exceptional ratings for these presentations and was previously selected as Outstanding Discussion Leader of The Year by the Tennessee Society of CPAs.

Professor McKee has also provided consulting services to both businesses and CPA firms. He has recently been involved as an expert witness in a variety of litigation cases.

Professor McKee's teaching and research interests primarily relate to auditing. He is currently researching the development of knowledge bases via neural networks, inductive inferencing algorithms or fuzzy logic that can assist in auditing or business decisions.

Address for correspondence: Department of Accountancy, East Tennessee State University, PO Box 70710, Johnson City, TN 37614, USA.
