---
otero_id: 6026
otero_key: "M4H899SQ"
title: "Resolving Difference Score Issues in Information Systems Research1"
authors: "Gary Klein; James J. Jiang; Paul Cheney"
year: "2009"
journal: "MIS Quarterly"
doi: "10.2307/20650328"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Resolving Difference Score Issues in Information Systems Research
Author(s): Gary Klein, James J. Jiang and Paul Cheney
Source: MIS Quarterly, Vol. 33, No. 4 (Dec., 2009), pp. 811-826
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/20650328
Accessed: 19-10-2015 04:49 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# RESOLVING DIFFERENCE SCORE ISSUES IN INFORMATION SYSTEMS RESEARCH $^{1}$

By: Gary Klein  
College of Business and Administration  
University of Colorado, Colorado Springs  
P.O. Box 7150  
Colorado Springs, CO 80933-7150  
U.S.A.  
gklein@uccs.edu

James J. Jiang
Department of Business Administration
College of Management
National Taiwan University
Taipei 10617
TAIWAN (R.O.C.)
jjiang@bus.ucf.edu

Paul Cheney
Department of Management Information Systems
University of Central Florida
Orlando, FL 32816-1400
U.S.A.
pcheney@bus.ucf.edu

## Abstract

A number of models and theories in information systems research include concepts of a match between two variables or states. The development of measures for this concept can present problems, because decisions must be made about the nature of the comparison. Should indirect measures of the match be employed, then methodological issues arise about how to best handle the measure when testing the model. Difference scores are commonly used to measure a match between variables or states in IS research, but these have implicit assumptions about the theory and data characteristics that are often false. Not unexpectedly, false assumptions can lead to erroneous conclusions about the relationships among the variables that are used to determine a match in a research model. The implicit assumptions restrict the form of the relationships and limit the IS researcher's ability to understand the possible interplay among theoretical concepts. We suggest some guidelines for the formation and testing of models that measure the match. In addition, we recommend polynomial regression analysis as one means of analyzing the more complex relationships in IS studies. We then use an IS service quality example to illustrate the issues involved in the use of matching variables and make suggestions with regard to using or avoiding difference scores.

Keywords: Difference scores, indirect measures, polynomial regression analysis, IS SERVQUAL

## Introduction

Models that utilize a match between two variables or states are common in information systems studies. For example, the match of prior expectations to perceived performance of a system determine user satisfaction in a model of IS continuance (Bhattacherjee 2001). A similar match is considered in a model of how web portal perceptions of playfulness and usefulness influence intent to continue use (Lin et al. 2005). Perceptions of IS job performance, career satisfaction, and user satisfaction are a result of a matching process for different stakeholders (Tesch et al. 2003). The demand for skills among webmasters should match the supplies to reach peak performance (Wade and Parent 2002). Matching can target features such as system and information quality (McKinney et al. 2002). Practice may require the match be considered separately for different stakeholders and classes of applications (Nevo and Wade 2007). As illustrated above, IS studies of a match between two variables are common. The application of matching models in reference disciplines and added attention to details in IS modeling increase the viability of employing matching variables in IS research.

Determining appropriate measures and analysis techniques to study a proposed match can be problematic. The choice of the measure requires careful consideration of the theory and the research question (Petter et al. 2007; Straub et al. 2004). One may select a direct measure that is a single value for the difference, or an indirect measure that captures a value for each side of the match under study (Kristof 1996). Commensurate, indirect measures contain the same content dimensions for each component and ensure mutual relevance to the matching concepts under investigation (Edwards 1991). In some cases, the difference between the two commensurate variables is used as a single variable for inclusion in a research model. Difference scores create problems in analysis, some of which are well recognized, but there are others that are hidden in the implicit assumptions of forming a difference score (Edwards 2001). The choice of the analysis method requires consideration of the data characteristics and the conceptual model of the proposed match (Venkatraman 1989). Inappropriate techniques can weaken the link between the development and the testing of the theory, violate the theoretical intentions, or fail to reveal the true nature of a relationship (Brown et al. 2008; Edwards 2001).

This note addresses several questions concerning the measurement of the match including the following:

(1) What implicit assumptions in the design and analysis of two commensurate, indirect measures can alter relationships?

(2) Does the form of the relationship between the two components of an indirect measure and the dependent variable make a significant difference in the results because it misrepresents the match?

(3) Might erroneous conclusions result due to the analysis when selecting a particular approach for handling indirect measures?

We address these questions by considering the three implicit assumptions that are made when employing difference scores: (1) equal and opposite weights for the two variables determining the match; (2) that only the magnitude of the difference is relevant in any relationship (magnitudes of the individual components are irrelevant); and (3) the relationship between the matching variables must be linear. Resulting errors in conclusions and possible methods to avoid these errors are first described, and then later illustrated with a model of information systems service quality.

## A Match Between Variables

A theoretical match between two related variables or states is one of a variety of fit models (Venkatraman 1989). Fit can be between two variables or many, may or may not have a specified relationship to a specific criterion, and can vary in functional form. A model of fit involving a match between two variables is developed independently of any performance anchor and it is commonly examined in light of a subsequent effect. Deviations from one variable to another represent a match when close to zero, or lack thereof when not zero. A number of models that consider a match between two entities, their states of nature, or perceptive measures are proposed in the IS literature. For example, discrepancy theory relates the difference between the same measures across individuals or perceptive states to specific domains of interest (Szajna and Scamell 1993; Tesch et al. 2003). Variations of the person–environment fit model lead to expectations that the two states will interrelate (Chilton et al. 2005; LeRouge et al. 2006). Expectation confirmation theory considers the match between two states of perception (Bhattacherjee 2001; Jiang and Klein 2009).

Many studies collect a variable for each state or perception for subsequent analysis. The process of collecting two variables is an indirect measure of the deviation requiring a comparison to define the match value. The reason for collecting commensurate, indirect measures is to capture two states that allow for computational comparison. The comparative result represents a third state, either through a proposed relationship or as a simple predictor. The deviation can be of many considerations as the same variable at different points in time, differences between expectations and perceived delivery, or simply supply and demand of a skill or desire (Jahng et al. 2007; Jiang et al. 2001; Kettinger and Lee 1994; Tesch et al. 2003). The deviation is often computed as a difference score.

A frequent usage of a deviation between matching variables in the IS literature is the use of an IS SERVQUAL measure. IS SERVQUAL consists of questions measuring customer expectations and their perceptions about the performance of the service provider (Kettinger and Lee 1994). The comparison of expectations and perceptions yields a matching deviation that represents service quality. Service quality can be related to customer satisfaction. Often, a difference score is computed to represent the deviation from a match between the expectation and the perception of actual service (Jiang et al. 2002). When expectations are met or exceeded, then the customer is satisfied; when perceived performance does not meet or exceed expectations, then the customer is dissatisfied. This attainment of expectations closely matches other psychological-need-fulfillment models that examine how attitudes are affected by the congruence between desires and available supplies in the environment (Oliver 1981).

In models that incorporate a matching consideration, analyzing the comparison of two scores can be problematic. The problem centers on having two scores that are intended to represent a single concept: the match between two states. Incorporating two variables into a model that requires a single concept adds to the complexity of the model's relationships. Introducing an additional variable into a complex model further increases the complexity, because the researcher must determine the theoretical implications and seek a larger sample (Kristof 1996). Solutions to these problems generally fall into one of two categories: simplification or using differences. Simplification involves using only one measure by dropping one of the variables from the analysis, a technique that is often applied in the IS literature (Carr 2007; Lee and Lin 2005; Lin et al. 2005). Utilizing differences requires subtracting one commensurate measure from the other, or by asking respondents to make the comparison to arrive at a direct measure. In the IS literature, one or the other forms of differencing has been used in a number of studies (Bhattacherjee 2001; Durvasula et al. 2004; Jiang et al. 2002; Kuo et al. 2005; Wade and Parent 2002).

## Issues with Difference Scores

There are several problems that can arise from the use of simplification. First, indirect measures developed from a theoretical relationship between two states require both components. The elimination of a variable may represent a change in the theory (Edwards 2009). Second, by dropping one of the components from the measure, some of the explanatory power is lost (Watson et al. 1998). The last problem involves the loss of some of the predictive power. Using only one of two measures in a predictive model cannot improve the predictive power of that model (Edwards 1994). Studies may find different results if both components are collected and included instead of just one component (Negash et al. 2003). Arguments may be strengthened or a relationship may be found where none would have been indicated if both components were included in the model.

Using difference scores amounts to a simple subtraction to gain a single measure for use in further analysis. A difference score may be acquired by asking the subjects to provide a direct perception of the match or by subtracting one variable from the other. However, computed difference scores are known to have a variety of problems associated with their psychometric properties, as summarized in Table 1. Although these tend to be well recognized in the IS literature, the relationship between the two components is often ignored. This relationship is overlooked in the process due to the presence of restrictive assumptions. These include assumptions concerning the relative weights of components, the magnitude of components, and the linearity of component interactions.

## Assumption of Equal and Opposite Weights

The first assumption that restricts the use of difference scores is the one of equal but opposite weights for the component scores. Using expectation–confirmation models as the basis of the following equations, equation 1 presents the relationship that is implied by strict differencing:

$$
\text { Satisfaction } = \mathbf {b} _ {0} + \mathbf {b} _ {1} (\mathbf {P} - \mathbf {E}) + e\tag{1}
$$

The variable measuring expectations (E) and the perceptions about the performance (P) of the service provider are compared (P–E). When used in an analysis such as to measure satisfaction, this has the effect of setting the weights on the components to be equal but opposite, as illustrated by the following restatement:

$$
\text { Satisfaction } = \mathbf {b} _ {0} + \mathbf {b} _ {1} (\mathbf {P}) - \mathbf {b} _ {1} (\mathbf {E}) + e\tag{2}
$$

“Like any constraint, this cannot increase the variance explained, and in most cases will decrease it” (Edwards 1994, p. 56). The dependent variable (i.e., satisfaction) is restricted to a very narrow set of functional forms. Figure 1 shows the relationship among the three variables under this condition. The line along P = E is horizontal to the dependent variable plane, so that the magnitude of the components is irrelevant. The line along P = -E increases with P and decreases with E, showing increased satisfaction as the gap gets larger. These conditions are also present in a two-dimensional model using a difference score and dependent variable.

The concept of matching two variables does not require such a limitation. Testing a hypothesis that allows for a broader set of functional forms can yield false conclusions when restricted, as will be demonstrated in a later section of this note. However, should difference scores be desirable for modeling or theoretical reasons, it is possible to test the data for adherence to this assumption with a linear regression model using both components as independent variables and seeing if the coefficients have significantly different weights.

<table><tr><td colspan="2">Table 1. Difference Score Criticisms</td></tr><tr><td>Criticism*</td><td>Specifics</td></tr><tr><td>Use of difference scores to operationalize variables</td><td>Since one&#x27;s perception already entails an expected level, subtraction as a simulation of a psychological process is too simplistic to measure the complex cognitive evaluation process</td></tr><tr><td>Ambiguity of expectations</td><td>Multiple interpretations of expectations can result in serious measurement errors</td></tr><tr><td>Unstable dimensionality</td><td>The difference score-factor structure is not stable under varying contexts</td></tr><tr><td>Reliability</td><td>Lower reliability for difference scores</td></tr><tr><td>Discriminant validity</td><td>It is difficult to demonstrate that the difference score is measuring something unique from the perceptions component alone</td></tr></table>

Sources: Spreng and Page 2003; Van Dyke et al. 1997; Van Dyke et al. 1999

![](/api/attachments/M4H899SQ/fulltext/images/a62b18dc38dc9b50127cb9ff3c233064c9cabb33bf88f4466fa0cb28053c96d3.jpg)  
Figure 1. Curve with Equal and Opposite Weights

## Assumption of No Influence Due to Component Magnitude

The magnitude of the components is lost when using difference scores, so any model implicitly states that a variable dependent on a difference score is independent of the magnitude of the component scores. A further examination of equations 1 and 2 reveals that identical difference scores will produce the same magnitude for the dependent variable regardless of the magnitude of the components. The implied relationship is very different from the one in which the dependent variable is reliant on the magnitude of either or both components. The application of a regression model with separate component scores would use the following expression:

![](/api/attachments/M4H899SQ/fulltext/images/f80d5dbb0a36b3f91b99e5557497062c4e44dd6d0b44cf92d51d399e7fd6c700.jpg)  
Figure 2. Curve Where Magnitudes of Components Matter

$$
\text { Satisfaction } = \mathbf {b} _ {0} + \mathbf {b} _ {1} (\mathbf {P}) - \mathbf {b} _ {2} (\mathbf {E}) + e\tag{3}
$$

In equation 3, component scores are separate predictors of satisfaction, while in equation 1 the difference between the two components is a single predictor. Equation 3 shows clearly that a difference at a higher level of expectation might not have the same level of satisfaction as an equivalent gap at a lower level as required by equation 1. A difference score will not allow this relationship to be represented, resulting in a model that arbitrarily rejects potentially valuable information, perhaps even the true relationship. The variation that relaxes this difference score assumption while retaining linearity is shown in Figure 2. Here, the curve is no longer horizontal to the dependent variable plane along the P = E line, showing a sharp visual contrast to the restricted relationship of Figure 1. The slope along the P = E line is the direct result of relaxing the assumption of equal and opposite weights. However, this variation still allows the gap to be an important characteristic as seen by an increase to the dependent value for P that is steeper than for E.

## Assumption of a Linear Relationship

The final assumption considered here is the restriction to linearity in the relationship between the component scores. Even moving to equation 3 retains an assumption of linearity, though with greater variety of form than equation 2. Linearity is a valuable assumption for several reasons. First, many of our analysis techniques require the assumption of linearity. Second, the more parsimonious model is one of linearity. Third, underlying theory does not necessarily dictate the shape of the relationship and unless the theory dictates a nonlinear relationship, linear modeling should be employed (Edwards 1994; Kristof 1996). However, theory-backed models in reference disciplines have been reexamined as nonlinear. Many studies have found that nonlinear relationships are often appropriate. Table 2 presents several such models.

<table><tr><td colspan="2">Table 2. Nonlinear Regression Studies of Theory-Based Models</td></tr><tr><td>Study</td><td>Nonlinearity in Findings</td></tr><tr><td>Person-environment fit: Segmentation preferences vs. segmentation supplies (Kreiner 2006)</td><td>Asymmetric effects of “fit” on employees’ stress and work-home conflict is shown by a pronounced curvilinear shape</td></tr><tr><td>Multi-source feedback: Self-performance evaluation vs. other’s performance evaluation (Bono and Colbert 2005)</td><td>When self and other ratings are not in agreement, satisfaction with ratings is a convex relationship, goal-commitment varies in nonlinear shapes by evaluation level</td></tr><tr><td>Self-enhancement: Self-competence ratings vs. colleague-perceived competence scores (Anseel and Lievens 2006)</td><td>Feedback acceptance altered nonlinear forms across variations in expressed decisiveness</td></tr><tr><td>Psychological contract violation: Promised delivery vs. actual delivery (Lambert et al. 2003)</td><td>Nonlinear findings contradict a basic assumption that outcomes remain constant when delivered inducements match promised inducements irrespective of their magnitudes</td></tr><tr><td>Attraction-selection-attrition: Rater personal factors vs. ratee personal factors (Antonioni and Park 2001)</td><td>Similarity in conscientiousness between rater and ratee is associated with ratings in a concave form</td></tr><tr><td>Person-job fit: Polychronicity supply vs. polychronicity values (Hecht and Allen 2005)</td><td>Negative affect is represented by a U-shape on the supply axis, with a reversal of slopes on the value axis</td></tr></table>

Should there be a compelling logical or empirical reason to expect nonlinearity, then the assumption of linearity should be tested. Should a theory be modified to incorporate principles that expect nonlinearity (such as diminishing returns), then the nonlinear model should be the basis from the start (Edwards 2009). Additionally, studies have experimentally found that linear relationships do not adequately describe the complex relationships between two indirect measures (Atwater et al. 1998; Mittal et al. 1998). Difference scores and simplifications do not adequately represent nonlinear relationships. Should nonlinearity be expected, the component scores should be tested using polynomial regression analysis (PRA).

$$
\text { Satisfaction } = \mathrm{b} _ {0} + \mathrm{b} _ {1} \mathrm{P} + \mathrm{b} _ {2} \mathrm{E} + \mathrm{b} _ {3} \mathrm{P} ^ {2} + \mathrm{b} _ {4} \mathrm{PE} + \mathrm{b} _ {5} \mathrm{E} ^ {2} + \mathrm{e}\tag{4}
$$

In essence, PRA replaces a difference score with the component measures in a nonlinear regression. Interactions and higher-order terms are included. This approach provides comprehensive tests of relationships that motivate the use of difference scores and examines complexities that linear modeling cannot represent (Edwards 2001; Edwards and Cooper 1990). In PRA, congruence is not viewed as a single score, but instead as the correspondence between the component measures. Perfect congruence is not a point but a curve along which component measures are equal. Thus, PRA allows relationships that are more complex than simple difference scores, or even linear models of the component scores.

When surfaces are curvilinear, the surface can be one of several types, including a concave or convex U-shape or an asymptotic form where the function approaches a limit. Models in which a gap in either direction is negative might appear as shown in Figure 3. Although this does not retain linearity, it preserves equal weighting of components, since the line along P = E is horizontal to the floor. This restriction is not required, but it presents a clear representation in the graph. What is unique about the relationship shown is that a deviation from the expected levels in either direction detracts from the dependent variable. For example, workers need some activity in their jobs to maintain mental well being, but being overworked also has detrimental effects (Warr 1994).

A wide variety of shapes become possible with equation 4, and polynomial regression analysis allows for even higher order terms to represent a large variety of relationships. When surfaces are flat, the interpretation is relatively straightforward. However, should a nonlinear case be appropriate and the interpretation of a polynomial model follow, one should become familiar with response–surface analysis (Khuri and Cornell 1987).

## Guidelines for Analyzing Indirect Measures

Figure 4 presents guidelines in the form of a decision tree for determining how an information systems researcher would most appropriately incorporate indirect measures into their research models. The primary consideration must be the theory behind any study; specifically, does the theory include sufficient justification for considering nonlinearity? If the study is exploratory, then ask if the data characteristics are nonlinear. Although PRA presents the opportunity to go beyond the linear domain, quadratic polynomial forms employed throughout this note might not represent the best form. For example, prospect theory, which may be applicable to a number of personal preferences, is represented by a cubic equation (Kahneman and Tversky 1979). Unfortunately, the number of curve possibilities is endless, which, along with the principle of parsimony, stresses the need to have sound justification behind any nonlinear shape.

![](/api/attachments/M4H899SQ/fulltext/images/075e3172653a7bf63dd8f9c1da44e34cfd9009e575fb03a846e7398e7fa55d58.jpg)  
Figure 3. Curve Maximized Along Line of Congruence

![](/api/attachments/M4H899SQ/fulltext/images/3ab77da90d12dd7ce7f10dcb5b63b5b26f9c40a6ef3f5e4cdbd221a5951f725a.jpg)  
Figure 4. Consideration of Indirect Measures for Model Inclusion

The prior assumption of a linear model does not assure simplicity in the analysis. As shown in Figure 4, a linear model in accordance with equation 3 should be considered to determine if the difference score assumptions are valid. If so, difference scores may appropriately be incorporated into the research model. If not, single equation models can still be readily tested with standard analysis techniques, but more complex path models would require a careful incorporation of the components (Cheung 2009; Edwards 2009).

When nonlinearity is expected due to theory, the anticipated relationship should first be examined with PRA to determine if any coefficient on the higher order terms is significant. If not, then the model should be built using the guidelines for linear expectations. If nonlinearities do exist, then PRA becomes an appropriate method for the study of single equation models or for the development of block variables in more complex models (Marsden 1982).

## Illustration

A common IS research application of indirect measures is in the field of service quality (Kettinger and Lee 2005). The common measure is IS SERVQUAL, which is an adaptation to the IS context and used in many studies (Jiang et al. 2002). In IS SERVQUAL, commensurate measures of expected service levels and perceived service performance are used as an indirect measure of service quality. Its descriptive power makes IS SERVQUAL a potent diagnostic tool for IS managers and a recognizable metric for researchers (Watson et al. 1998). An IS SERVQUAL dataset will serve to illustrate the issues of difference score measurement and the application of the guidelines presented in Figure 4. The appendix describes the collection process and the validation of the data. Validation is done for the independent components of expectation (E) and perceived performance (P), the difference score that represents the match (P - E), and a dependent variable of user satisfaction. The data quality is comparable to other IS studies that utilize IS SERVQUAL (Jiang et al. 2002; Kettinger and Lee 1994).

Researchers avoid difference scores by using a simplified alternative for IS SERVQUAL. They use performance information only (Van Dyke et al. 1997). A number of IS studies have used this approach (Devaraj et al. 2002; Lee and Lin 2005; Negash et al. 2003). None of these studies have found significant relationships between all four service-quality dimensions and user satisfaction. This result is in conflict with several studies of service quality in IS and other contexts that utilize both the expectation and performance dimensions. The performance-only solution represents an entirely different theoretical concept by dismissing the contribution of expectations in determining satisfaction. The omission of expectations can lead to false conclusions (Edwards 2001).

Other studies have employed difference scores of IS SERVQUAL components, with mixed results (Jiang et al. 2003; Kuo et al. 2005; Kuo 2003; Park and Kim 2005). The statistical problems inherent in difference scores are normally fully investigated to consider possible problems including low reliability, unstable dimensionality, and questionable discriminant validity. These problems have been studied extensively with regard to the IS SERVQUAL measure and any negative results concerning these issues were minimal (Carr 2002; Jiang et al. 2002; Pitt et al. 1997). However, none of these studies addressed the potential impact of the implied assumptions of difference scores that radically restrict the form of the relationships and possibly can be in conflict with the intent of the research model or the historical patterns in the data characteristics.

The model in Figure 5 proposes a relationship between the component variables of IS SERVQUAL and user satisfaction. Performance and expectations are maintained as separate items at the collection level, and separate constructs at the variable level. Previous work and theory support the premise that service quality is related to user satisfaction (Jiang et al. 2002). So that we may more clearly show the assumption violations of difference scores, we will begin by assuming that all relationships are linear and follow the guidelines along this path in Figure 4. Should difference-score assumptions hold, one would expect the weights for each component to be of equal magnitude and of opposite sign. A simple linear regression using equation 3 with the results in Table 3 shows that the coefficients do not meet the weight assumptions. More importantly, the regression analysis using difference scores (equation 1) does not indicate a significant relationship between service quality and satisfaction, while the regression component scores from equation 3 seem to indicate that such a relationship may exist. Therefore, we recommend retaining the component scores because it could lead to more significant results. Accordingly, the guidelines in Figure 4 indicate that both components should be used in any further analysis. Should the simple linear regression represent the full research model, then the analysis is complete. If the model is more complex, such as a path model, then the model needs to accommodate both P and E components (Cheung 2009).

![](/api/attachments/M4H899SQ/fulltext/images/b4d4f4d3e01ee4652789f005541faff9d27efd61b39dfc38f5000a68717509ac.jpg)  
Figure 5. The Measurement Model for Service Quality and User Satisfaction

Table 3. Linear Regression Coefficients

<table><tr><td></td><td colspan="3">Separate Components</td><td colspan="2">Difference Score</td></tr><tr><td>User Satisfaction</td><td>Perception</td><td>Expectation</td><td>Adj.  $R^2$ </td><td>P-E</td><td>Adj.  $R^2$ </td></tr><tr><td>Reliability</td><td>0.501*</td><td>0.222 *</td><td>0.331</td><td>-0.16</td><td>0.019</td></tr><tr><td>Responsiveness</td><td>0.471*</td><td>0.222 *</td><td>0.296</td><td>0.113</td><td>0.006</td></tr><tr><td>Assurance</td><td>0.460*</td><td>0.211 *</td><td>0.295</td><td>-0.148</td><td>0.015</td></tr><tr><td>Empathy</td><td>0.471*</td><td>0.054</td><td>0.228</td><td>-0.230*</td><td>0.046</td></tr><tr><td>Overall</td><td>0.537 *</td><td>0.179 *</td><td>0.364</td><td>-0.174</td><td>0.024</td></tr></table>

\*p < .05

Now let's drop the assumption that the model is strictly linear and consider nonlinear possibilities. It is logical to expect nonlinear relationships in the data that possibly need to be incorporated into the model. Past studies in the service-quality literature have found that negative gaps have a greater impact on satisfaction than do positive gaps, and large discrepancies have proportionally more impact than smaller discrepancies (Johnston 1995; Mittal et al. 1998; Nevo and Wade 2007). Their results indicate that the dependent variable increases in a relationship that reflects diminishing returns, perhaps a minor conceptual change to the relationship, but a major one in terms of the analysis. Thus, a pure linear approach may be inadequate to describe the relationship among expectation, performance, and satisfaction in an IS service-quality model. To consider the possible nonlinear aspects in the IS SERVQUAL dataset, we conducted a PRA that included the square and interaction terms of equation 4, sufficient to allow for diminishing returns. Should there be diminishing returns or other nonlinearity in the data, PRA will indicate significant higher-order terms. The results of this polynomial regression analysis are presented in Table 4.

Table 4. Polynomial Regression Coefficients

<table><tr><td></td><td> $b_0$ </td><td> $b_1P$ </td><td> $b_2E$ </td><td> $b_3P^2$ </td><td> $b_4PE$ </td><td> $b_5E^2$ </td><td>Adj.  $R^2$ </td></tr><tr><td>Reliability</td><td>-0.06</td><td>0.51*</td><td>0.29*</td><td>-0.04</td><td>-0.10</td><td>0.11</td><td>0.341</td></tr><tr><td>Responsiveness</td><td>0.11</td><td>0.41*</td><td>0.19*</td><td>-0.10</td><td>-0.03</td><td>0.00</td><td>0.303</td></tr><tr><td>Assurance</td><td>-0.04</td><td>0.49*</td><td>0.15</td><td>0.03</td><td>-0.16*</td><td>0.04</td><td>0.312</td></tr><tr><td>Empathy</td><td>-0.01</td><td>0.48*</td><td>-0.01</td><td>0.03</td><td>-0.18*</td><td>0.03</td><td>0.271</td></tr></table>

\*p < 0.05

![](/api/attachments/M4H899SQ/fulltext/images/0865921b8ba3f2d276da46ed02ab427d65de00cbc5719207e72863a6bc44943c.jpg)  
Figure 6. Assurance Response Surface

The significance of the interaction term in two of the IS SERVQUAL dimensions indicates a diminishing-return effect: as both components increase, the related growth in satisfaction decreases. Figure 6 shows the corresponding response surface for the assurance dimension (the empathy curve is similar). The curve rises steeply from the lowest point (-4, -4), then begins to decline in slope as it approaches the opposite point (4, 4). This represents the case of a declining contribution to satisfaction as both components increase. It also shows the diminishing returns of the magnitude of the components when the deviation is zero (the P = E line). The shape also indicates that performance contributes more to satisfaction than expectation does, and as we would expect, user satisfaction grows more quickly along the P axis. The expectation that the difference-score magnitude might negatively influence the relationship is not supported by the curve. It would show a downward trend on either side of the P = E line or significant negative values on one of the coefficients of the squared components if this were true.

Our illustrative example is limited to the component scores and a single dependent variable. Should this be sufficient for the research model, then PRA has already incorporated the complexity required as described in Figure 4. Incorporating PRA into path models when nonlinearity is known to be present is more problematic. Although indirect measures can be incorporated into path models through linear techniques and still maintain the value in their components (Cheung 2009), nonlinear forms require the implementation of other techniques such as blocking (Marsden 1982). One forms a block variable by first conducting a regression analysis of the dependent variable as a function of the component scores. We then use the derived regression equation to create a single value for the component scores as the predicted value of the dependent variable. Block variables summarize the effects of a set of conceptually related variables in path analysis and depict nonlinear and interactive effects as a single path coefficient (Jagodzinski and Weede 1981; Marsden 1982).

Table 4 indicates that only assurance and empathy need to be blocked. This change would require a model as shown in Figure 7. Here, the dimensions of responsiveness and reliability retain the independent constructs for performance and expectation, while block variables are used in the model for empathy and assurance to again complete the steps shown in the guidelines of Figure 4. Table 5 presents three partial least squares (PLS) results using difference scores, the model with the block variable, and a linear model with only component scores. Comparing Model 1 to Model 2 demonstrates how the statistical fit of the model is improved by utilizing component scores. Model 3, which uses the block variables, reduces the adjusted R² value, but not significantly. There is a possible trade-off in the blocking of variables between statistical fit and form, but if the theory states that the relationship is nonlinear, then blocked variables normally provide a better representation of the theory. Theory and data characteristics should take precedence over statistical fit when conducting tests of theory-driven hypotheses (Venkatraman 1989).

During the analysis process, several of the steps are directly related to using commensurate, indirect measures as components in a model. The illustration shows how to follow the guidelines suggested for each branch of the decision tree in Figure 4. For this data set, the difference score model ignores the relationship between user expectations and satisfaction and leads to erroneous conclusions. In addition, the illustration has shown that the use of a linear model may be inadequate to capture the relationships between expectation, performance, and satisfaction. For the data set in the illustration, this inadequacy impacts only the potential interpretation and understanding of the model. In this illustration, both the linear and nonlinear models confirm the expected relationships.

## Concluding Remarks

When considering models that include a match between two variables, IS researchers must carefully consider the structure of the relationship among the variables, the determination of the match, and the analytical techniques applied. Often, the match is considered as a deviation between the two variables. In such a case, it is common among IS researchers to compute or elicit a difference score. Difference scores, however, have known issues with reliability, validity, dimensionality, and interpretability. To avoid these issues, IS researchers apply direct measures of difference, drop one of the variables and use the remaining one, or rigorously validate the difference score for each data set. Although these techniques may alleviate concerns of data quality, they potentially violate or alter the theoretical underpinnings of the research model since they remove a variable or apply unintended assumptions.

There are three assumptions about the relationship among variables when applying difference scores that can lead to false conclusions: assumptions on weights, assumptions on the magnitude of the components, and the assumption of linearity. One question addressed in this note asks whether these assumptions can impact the relationships among the variables. Each assumption was individually investigated mathematically and illustrated with a numerical example. A potential to alter the relationship significantly was found as each assumption was enforced or relaxed.

The second question addressed concerns regarding the form of the relationship between the indirect measures and the dependent variable. The match between two indirect measures has a variety of potential shapes, with different interpretations for each shape. Linear shapes can represent situations where component scores are weighted according to difference score assumptions or independently as long as the value of the dependent variable increases (or decreases) at a constant rate as each component changes. Forms that deviate from linear are necessary for models that might suffer from diminishing returns, have adverse results for deviations in any direction, form an exact match, or follow common theories of preference structures that are nonlinear in nature. The illustration served to highlight how variations in the curves can present decidedly different interpretations of the results. When developing a model from theory, IS researchers should consider the nature of the relationship required, implied, or even allowed by the chosen theory.

![](/api/attachments/M4H899SQ/fulltext/images/3565038cb45dbc1da3abd4489a28baf4244a7781dc9600ded7322c3fa0eb1d2a.jpg)  
Figure 7. Illustration Model with Component and Block Measures

<table><tr><td rowspan="2">Coefficient</td><td rowspan="2">Model 1Difference Scores</td><td colspan="2">Model 2Linear Model</td><td colspan="2">Model 3Linear Model with Block Variables</td></tr><tr><td>P</td><td>E</td><td>P</td><td>E</td></tr><tr><td>Reliability</td><td>-0.19</td><td>0.316 *</td><td>0.114*</td><td>0.207 *</td><td>0.130*</td></tr><tr><td>Responsiveness</td><td>0.14</td><td>0.141 *</td><td>0.138*</td><td>0.148 *</td><td>0.118*</td></tr><tr><td>Assurance</td><td>0.03</td><td>0.110 *</td><td>0.285*</td><td colspan="2">0.154*</td></tr><tr><td>Empathy</td><td>-0.21*</td><td>0.101 *</td><td>-0.362*</td><td colspan="2">0.215*</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.031</td><td colspan="2">0.433</td><td colspan="2">0.426</td></tr></table>

\*p < 0.05

The third question addresses the techniques more directly and concerns the approach selected in the analysis. The simplification of indirect measures by using only one component, or taking a difference score, can lead to erroneous conclusions and violate the underlying theory of a model. Linear models are still appropriate for many situations, but studies should consider how to incorporate both matching variables into the model. When linearity may not be appropriate, polynomial regression analysis is a common method to allow for a variety of shapes. Block variables can serve to represent nonlinear relationships in path models. To assist in the identification of the recommended analysis steps, IS researchers can use the guidelines presented in Figure 4.

On the whole, indirect measures, along with the appropriate analysis techniques, will allow IS investigators greater flexibility in examining each data set for an expected shape based on the underlying theory, prior empirical patterns, and data characteristics. The benefits of using component scores in research models include the avoidance of restrictive assumptions and an increased variety of potential representations. These nonlinear shapes add complexity to the models but they can also generate richer models due to the broader interpretation of theory, and perhaps they will then yield more significant research results.

## References

Anseel, F., and Lievens, F. 2006. “Certainty as a Moderator of Feedback Reactions? A Test of the Strength of the Self-Verification Motive,” Journal of Occupational and Organizational Psychology (79:4), December, pp. 533-551.

Antonioni, D., and Park, H. 2001. “The Effects of Personality Similarity on Peer Ratings of Contextual Work Behaviors,” Personnel Psychology (54:2), Summer, pp. 331-360.

Atwater, L. E., Ostroff, C., Yammarino, F. J., and Fleenor, J. W. 1998. “Self–Other Agreement: Does it Really Matter?,” Personnel Psychology (51:3), Autumn, pp. 577-598.

Baroudi, J. J., and Orlikowski, W. J. 1988. “A Short Form Measure of User Information Satisfaction: A Psychometric Evaluation and Notes on Use,” Journal of Management Information Systems (4:4), Spring, pp. 44-59.

Bentler, P., and Bonett, D. 1980. “Significance Tests and Goodness of Fit in the Analysis of Covariance Structures,” Psychological Bulletin (88:3), November, pp. 588-606.

Bhattacherjee, A. 2001. “Understanding Information Systems Continuance: An Expectation-Confirmation Model,” MIS Quarterly (25:3), September, pp. 351-370.

Bono, J. E., and Colbert, A. E. 2005. “Understanding Responses to Multi-Source Feedback: The Role of Core Self-Evaluations,” Personnel Psychology (58:1), Spring, pp. 171-203.

Brown, S. A., Venkatesh, V., Kuruzovich, J., and Massey, A. P. 2008. “Expectation Confirmation: An Examination of Three Competing Models,” Organizational Behavior and Human Decision Processes (105:1), January, pp. 52-66.

Carr, C. L. 2002. “A Psychometric Evaluation of the Expectations, Perceptions, and Difference-Scores Generated by the IS-Adapted IS SERVQUAL Instrument,” Decision Sciences (33:2), Spring, pp. 281-296.

Carr, C. L. 2007. “The FAIRSERV Model: Consumer Reactions to Services Based on a Multidimensional Evaluation of Service Fairness,” Decision Sciences (38:1), Winter, pp. 107-130.

Cheung, G. W. 2009. “Introducing the Latent Congruence Model for Assessment of Similarity, Agreement, and Fit in Organizational Research,” Organizational Research Methods, (12:1), January, pp. 6 - 33.

Chilton, M. A., Hardgrave, B. C., and Armstrong, D. J. 2005. "Person-Job Cognitive Style Fit for Software Developers: The Effect on Strain and Performance," Journal of Management Information Systems (22:2), Fall, pp. 193-226.

Chin, W. W. 1994. PLS-Graph Manual Version 2.7, Calgary, AB: University of Calgary Press.

Devaraj, S., Fan, M., and Kohli, R. 2002. “Antecedents of B2C Channel Satisfaction and Preference: Validating E-Commerce Metrics,” Information Systems Research (13:3), Summer, pp. 316-333.

Durvasula, S., Lysonski, S., and Mehta, S. 2004. “Technology and its CRM Implications in the Shipping Industry,” International Journal of Technology Management (28:1), January, pp. 88-102.

Edwards, J. R. 1991. “Person–Job Fit: A Conceptual Integration, Literature Review, and Methodological Critique,” in International Review of Industrial and Organizational Psychology, C. L. Cooper and I. T. Robertson (eds.), New York: Wiley, pp. 283-357.

Edwards, J. R. 1994. “The Study of Congruence in Organizational Behavior Research: Critique and a Proposed Alternative,” Organizational Behavior and Human Decision Processes (58:1), April, pp. 51-100.

Edwards, J. R. 2001. “Ten Differences Score Myths,” Organizational Research Methods (4:3), July, pp. 265-287.

Edwards, J. R. 2009. “Latent Variable Modeling in Congruence Research: Current Problems and Future Directions,” Organizational Research Methods, (12:1), January, pp. 34 - 62.

Edwards, J. R., and Cooper, C. 1990. “The Person–Environment Fit Approach to Stress: Recurring Problems and Some Suggested Solutions,” Journal of Organizational Behavior (11:4), May, pp. 293-307.

Fornell, C., and Larcker, D. F. 1981. “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error,” Journal of Marketing Research (18:1), February, pp. 39-50.

Hecht, T. D., and Allen, N. J. 2005. “Exploring Links between Polychronicity and Well-Being from the Perspective of Person–Job Fit: Does it Matter If You Prefer to Do Only One Thing at a Time?,” Organizational Behavior and Human Decision Processes (98:2), November, pp. 155-178.

Hulland, J. 1999. “Use of Partial Least Squares (PLS) in Strategic Management Research: A Review of Four Recent Studies,” Strategic Management Journal (20:2), February, pp. 195-204.

Jagodzinski, W., and Weede, E. 1981. “Testing Curvilinear Propositions by Polynomial Regression with Particular Reference to the Interpretation of Standardized Solutions,” Quantity and Quality (15:5), October, pp. 447-463.

Jahng, J., Jain, H., and Ramamurthy, K. 2007. “Effects of Interaction Richness on Consumer Attitudes and Behavioral Intentions in E-Commerce: Some Experimental Results,” European Journal of Information Systems (16:3), July, pp. 254-269.

Jiang, J. J., and Klein, G. 2009. “Expectation Confirmation Theory: Capitalizing on Descriptive Power,” in Handbook of Research on Contemporary Theoretical Models in Information Systems, Y. Dwivedi, B. Lal, M. Williams, S. Schneberger, and M. Wade (eds.), Hershey, PA: Information Science Reference, pp. 384-401.

Jiang, J. J., Klein, G., and Balloun, J. 2001. “The Joint Impact of Internal and External Career Anchors on Entry-Level IS Career Satisfaction,” Information & Management (39:1), November, pp. 31-39.

Jiang, J. J., Klein, G., and Carr, C. L. 2002. “Measuring Information System Service Quality: IS SERVQUAL from the Other Side,” MIS Quarterly (26:2), June, pp. 145-166.

Jiang, J. J., Klein, G., Tesch, D., and Chen, H. G. 2003. “Closing the User and Provider Service Quality Gap,” Communications of the ACM (46:2), February, pp. 72-76.

Johnston, R. 1995. “The Zone of Tolerance: Exploring the Relationship between Service Transactions and Satisfaction with the Overall Service,” International Journal of Service Industry Management (6:2), pp. 46-61.

Kahneman, D., and Tversky, A. 1979. “Prospect Theory: An Analysis of Decision under Risk,” Econometrica (47:2), March, pp. 263-292.

Kettinger, W. J., and Lee, C. C. 1994. “Perceived Service Quality and User Satisfaction with the Information Services Function,” Decision Sciences (25:5-6), September, pp. 737-766.

Kettinger, W. J., and Lee, C. C. 2005. “Zones of Tolerance: Alternative Scales for Measuring Information Systems Service Quality,” MIS Quarterly (29:4), December, pp. 607-618.

Khuri, A. I., and Cornell, J. A. 1987. Response Surfaces: Design and Analysis, New York: Marcel Dekker.

Kreiner, G. E. 2006. “Consequences of Work–Home Segmentation or Integration: A Person–Environment Fit Perspective,” Journal of Organizational Behavior (27:4), June, pp. 485-507.

Kristof, A. L. 1996. “Person–Organization Fit: An Integrative Review of its Conceptualizations, Measurement, and Implications,” Personnel Psychology (49:1), Spring, pp. 1-49.

Kuo, T., Lu, I., Huang, C., and Wu, G. 2005. “Measuring Users’ Perceived Portal Service Quality: An Empirical Study,” Total Quality Management & Business Excellence (16:3), May, pp. 309-320.

Kuo, Y. F. 2003. “A Study on Service Quality of Virtual Community Websites,” Total Quality Management & Business Excellence (14:4), June, pp. 461-473.

Lambert, L. S., Edwards, J. R., and Cable, D. M. 2003. “Breach and Fulfillment of the Psychological Contract: A Comparison of Traditional and Expanded Views,” Personnel Psychology (56:4), Winter, pp. 895-934.

Lee, G. G., and Lin, H. F. 2005. “Customer Perceptions of E-Service Quality in Online Shopping,” International Journal of Retail & Distribution Management (33:2), February, pp. 161-176.

LeRouge, C., Nelson, A., and Blanton, J. E. 2006. “The Impact of Role Stress Fit and Self-Esteem on the Job Attitudes of IT Professionals,” Information & Management (43:8), December, pp. 928-938.

Lin, C. S., Wu, S., and Tsai, R. J. 2005. “Integrating Perceived Playfulness into Expectation-Confirmation Model for Web Portal Context,” Information & Management (42:5), July, pp. 683-693.

Marsden, P. V. 1982. “A Note on Block Variables in Multi-Equation Models,” Social Science Research, (11:2), June, pp. 127-140.

McKinney, V., Yoon, K., and Zahedi, F. M. 2002. “The Measurement of Web-Customer Satisfaction: An Expectation and Disconfirmation Approach,” Information Systems Research (13:3), September, pp. 296-315.

Mittal, V., Ross, W. T., Jr., and Baldasare, P. M. 1998. “The Asymmetric Impact of Negative and Positive Attribute Level Performance on Overall Satisfaction and Repurchase Intentions,” Journal of Marketing (62:1), January, pp. 33-47.

Negash, S., Ryan, T., and Igbaria, M. 2003. “Quality and Effectiveness in Web-Based Customer Support Systems,” Information & Management (40:8), September, pp. 757-768.

Nevo, D., and Wade, M. R. 2007. “How to Avoid Disappointment by Design,” Communications of ACM (50:4), April, pp. 43-48.

Oliver, R. L. 1981. “Measurement and Evaluation of Satisfaction Processes in Retail Settings,” Journal of Retailing (57:3), Fall, pp. 25-49.

Park, J. Y., and Kim, J. S. 2005. “The Impact of IS Sourcing Type on Service Quality and Maintenance Efforts,” Information & Management (42:4), May, pp. 261-274.

Petter, S., Straub, D., and Rai, A. 2007. “Specification and Validation of Formative Constructs in IS Research,” MIS Quarterly (31:4), December, pp. 623-656.

Pitt, L. F., Watson, R. T., and Kavan, C. B. 1997. “Measuring Information Systems Service Quality: Concerns for a Complete Canvas,” MIS Quarterly (21:2), June, pp. 209-221.

Podsakoff, P. M., MacKenzie, S. B., Lee, J., and Podsakoff, N. P. 2003. “Common Method Biases in Behavioral Research: A Critical Review of the Literature and Recommended Remedies,” Journal of Applied Psychology (88:5), October, pp. 879-903.

Spreng, R., and Page, T. Jr. 2003. “A Test of Alternative Measures of Disconfirmation,” Decision Sciences (34:1), Winter, pp. 31-61.

Straub, D., Boudreau, M., and Gefen, D. 2004. “Validation Guidelines for IS Positivist Research,” Communications of the AIS (13:24), pp. 380-427.

Szajna, B., and Scamell, R. 1993. “The Effects of Information System User Expectations on Their Performance and Perceptions,” MIS Quarterly (17:4), December, pp. 493-516.

Tesch, D., Jiang, J., and Klein, G. 2003. “The Impact of Information System Personnel Skill Discrepancies on Stakeholder Satisfaction,” Decision Sciences (34:1), Winter, pp. 107-129.

Van Dyke, T. P., Kappelman, L. A., and Prybutok, V. R. 1997. "Measuring Information Systems Service Quality: Concerns on the Use of the SERVQUAL Questionnaire," MIS Quarterly (21:2), June, pp. 195-208.

Van Dyke, T. P., Prybutok, V. R., and Kappelman, L. A. 1999. "Cautions on the Use of the IS SERVQUAL Measure to Assess the Quality of Information Systems Services," Decision Sciences (30:3), Summer, pp. 877-891.

Venkatraman, N. 1989. “The Concept of Fit in Strategy Research: Toward Verbal and Statistical Correspondence,” Academy of Management Review (14:3), July, pp. 423-444.

Wade, M. R., and Parent, M. 2002. “Relationships between Job Skills and Performance: A Study of Webmasters,” Journal of Management Information Systems (18:3), Winter, pp. 71-96.

Warr, P. 1994. “A Conceptual Framework for the Study of Work and Mental Health,” Work and Stress (8:2), August, pp. 84-97.

Watson, R. T., Pitt, L. F., and Kavan, C. B. 1998. “Measuring Information Systems Service Quality: Lessons from Two Longitudinal Case Studies,” MIS Quarterly (22:1), March, pp. 61-79.

## About the Authors

Gary Klein is the Couger Professor of Information Systems at the University of Colorado in Colorado Springs. He obtained his Ph.D. in Management Science from Purdue University. Before that time, he served with the company now known as Accenture in Kansas City and was director of the Information Systems Department for a regional financial institution. His research interests include project management, technology transfer, and mathematical modeling, with over 150 academic publications in these disciplines. He served as Director of Education for the American Society for the Advancement of Project Management and Vice President of Member Services for the AIS SIG on Information Technology Project Management. He is a Fellow of the Decision Sciences Institute and serves that organization as Vice President at Large. He is a founding and current coeditor-in-chief of Comparative Technology Transfer and Society.

James Jiang is a professor of Management Information Systems at the University of Central Florida and Chaired Management Professor at National Taiwan University. He obtained his Ph.D. in Information Systems at the University of Cincinnati. His research interests include IS project management and IS service quality management. He has published over 140 academic articles in these areas in journals such as Decision Sciences, Journal of Management

Information Systems, Communications of the ACM, IEEE Transactions on Systems Man & Cybernetics, IEEE Transactions on Engineering Management, Journal of the AIS, Decision Support Systems, Information & Management, European Journal of Information Systems, and MIS Quarterly. Currently, he serves as an associate editor for MIS Quarterly.

Paul Cheney is a professor and Department Head of Management Information Systems at the University of Central Florida. He received his Ph.D. in Management Information Systems from the University of Minnesota in 1977. He has taught at Texas Tech University, Iowa State University, the University of Georgia, the University of South Florida, and most recently at the University of Central Florida. His research has been primarily in the areas of managing information technology resources and he has published more than 50 articles and one textbook in the field of MIS. His articles have appeared in, among others, MIS Quarterly, Academy of Management Journal, Journal of Management Information Systems, Information Systems Research, and Decision Sciences. He has supervised 14 Ph.D. dissertations and served on over 50 Ph.D. committees. In addition, he has received numerous grants from private and public organizations. One of these was a \$2 million dollar grant from IBM in 1985 to support graduate MIS education. A similar grant was awarded from Solomon Brothers-Smith Barney in 1993 for \$1.8 million dollars.

## Appendix

## IS SERVQUAL Data Sample

Potential subjects were selected from an economic-analysis database developed at a major university research center. Calls were made by graduate assistants in random order from the list until 200 user volunteers were secured, requiring 280 calls in total. Surveys were mailed to the 200 volunteers. Self-addressed return envelopes for questionnaires were provided. All respondents were assured that their responses would be kept confidential. A total of 150 usable instruments were returned (follow-up calls were made if subjects did not respond within 3 weeks). Of the subjects responding, 47 percent were female, 60 percent were in the service industry as opposed to manufacturing, the average work experience was 12 years, the average age 32 years, and one-third of the respondents held management positions.

Items on the instrument included the demographic items plus questions about the subject's perception of IS service quality and user satisfaction. The instrument for measuring user satisfaction was adopted from Baroudi and Orlikowski (1988). The IS SERVQUAL constructs in this study were from Kettinger and Lee (1994). The tangibles dimension was dropped as in other studies of IS service. Both expectations and delivery perceptions were elicited for each IS SERVQUAL item. The component scores were retained and a difference score was computed. All three were validated according to the following process. Due to the illustrative nature of the example, as opposed to model confirmation, details of the data validation process and results are summarized. Specifics were provided during the review process and are available from the authors upon request.

PLS-Graph version 3.01 was used to verify the measures (Chin 1994). Individual item reliability is indicated by a high factor loading, implying that the shared variance between a construct and its measurement is higher than the error variance (Hulland 1999). All IS SERVQUAL item loadings for expectation, performance, and the difference score were 0.7 or higher, with the exception of one item in the empathy dimension. All but one item in the user satisfaction construct had a loading greater than 0.7. All t tests of the loadings for both measures were significant. All items are retained in further analysis given the significance of the loadings and extensive history of the scales. The cross loadings all indicated that each item loads most highly into the expected dimension.

Convergent validity was examined by the composite reliability of constructs with a minimum of 0.70 (Fornell and Larcker 1981). In the data under scrutiny, composite reliability ranged from a low of .82 to a high of .93. Cronbach's alpha scores ranged from a low of .72 to a high of .91 for the measures. Average variance extracted (AVE) reflects variance captured by the indicators (Fornell and Larcker 1981). Evidence regarding discriminant validity can be demonstrated if the square root of AVE for each construct does not fall below the correlation to any other construct. This condition was met.

Common method variance is a potential problem when both dependent and independent variables are collected from the same respondent at the same time. If a method factor exists, a model with such a factor should explain significantly more variance in the data than a model without a method factor. For our data, the normed fit index showed an insignificant improvement with the additional methods factor (Bentler and Bonett 1980). Thus common method variance does not appear to be an issue (Podsakoff et al. 2003). After all validation, component scores were scale-centered to reduce multicollinearity between component measures and their higher-order terms.
