---
otero_id: 20163
otero_key: "DFY6AMQ5"
title: "An exploratory study of object-oriented software component size determinants and the application of regression tree forecasting models"
authors: "Parag C. Pendharkar"
year: "2004"
journal: "Information & Management"
doi: "10.1016/j.im.2003.12.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An exploratory study of object-oriented software component size determinants and the application of regression tree forecasting models

\* Parag C. Pendharkar

Information Systems, School of Business Administration, Pennsylvania State University at Harrisburg, 777 West Harrisburg Pike, Middletown, PA 17057 4898, USA

Accepted 27 December 2003

Available online 15 April 2004

## Abstract

Software component size estimation is an important task in software project management. For a component-based approach, two steps may be used to estimate the overall size of object-oriented (OO) software: a designer uses metrics to predict the size of the software components and then utilizes the sizes to estimate the overall project size. Using OO software metrics literature, we identified factors that may affect the size of an OO software component. Using real-life data from 152 software components, we then determined the effect of the identified factors on the prediction of OO software component size. The results indicated that certain factors and the type of OO software component play a significant role in the estimate. It is shown how a regression tree data mining approach can be used to learn decision rules to guide future estimates. <sup>#</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Software engineering; Software size; Data mining; Forecasting; Classification and regression tree

## 1. Introduction

One approach to contain cost and improve productivity in software production is to develop better soft ware estimating models. However, their value depends heavily on prior activities: accurately estimating the software size [14]. Among popular measures of software size are the source lines of code (SLOC) and function points (FP) methods [1,2]. The selection of one measure over the other, however, is open to question. Proponents of FP have provided empirical evidence in its favor of the method [25,31,47], while those of SLOC criticize FP for being labor intensive and incapable of lending to automation. But many believe that SLOC is the appropriate measure [4,6,39]. The SLOC approach is criticized for not addressing the issue of language difficulty [23]. A few workers, using both approaches, emphasize the utility of SLOC for measuring software size and FP for measuring the complexity of a software project. Laranjeira [27] suggested that SLOC and FP should be related and represented linearly as $\mathrm { K L O C } = ( B \times \mathrm { F P } ) - \mathrm { A }$ , where KLOC is software size in thousands of lines of code, and A and B are constants.

The use of component-based software development (CBSD) has surged recently [40]. Among the reasons for its popularity are its use in distributed software development and the ease that it provides for the decomposition of a software project. Recent advances in programming languages make platform independent components, such as Java Beans and Windows-only Active X control components, available to the user [38].

Estimation of software component size is important when CBSD is used. The correct estimation in terms of SLOC is important because most software effort and cost estimation models use SLOC as an independent variable. Thus, it can be argued that increasing the forecasting accuracy of SLOC could result in more accurate cost estimates. Since CBSD is likely to use an object-oriented (OO) programming environment, forecasting software component size may be challenging. For example, such forecasting models should take into account the complexity of the objects and the number of objects used to obtain the overall software size.

The objectives of this study are to identify the factors that may affect the size of OO software components and to show how advanced non-linear data mining tools can be used to learn heuristic rules that can be used for providing future software component size estimates. We use the Damiani et al. [13] definition of an OO software component: it is either a class, a class cluster, or an application framework that has certain behavioral properties and user interaction style.

## 2. Literature review

Software size estimation techniques fall into two categories: subjective and objective. Subjective techniques use a project evaluation and review technique (PERT) method and expert judgment to estimate the size of a software project [35]. A few researchers have shown that such models are prone to errors because expert judgment varies due to psychological and personal factors [12]. Also, some of the assumptions in PERT are violated in practice. Delphi approaches, in which a project is decomposed into individual work activities and a team of experts generates an estimate for each activity, are also used [7,50]. One study [22] reported that a combination of developer-generated subjective estimates and analytical model-based estimates provided more accurate software size forecasts. Subjective estimates using paired comparisons have also been shown to be beneficial [33].

Objective techniques use either software metrics or regression models to forecast size. Software metrics such as FP attempt to measure software size in terms of system functionality; it focuses on certain identifiable system features [44]:

1. The number of external input types.

2. The number of external output types.

3. The number of master files.

4. The number of inquiries.

5. The number of interfaces.

A weighted sum of these features can be adjusted using a technical complexity factor (TCF), which depends on 14 variables. The result of the weighted average is the adjusted function points, which is used in software sizing and effort determination.

Several linear, logarithmic, and exponential regression models have been used for estimating software size. A few researchers have used machine-learning techniques, such as neural networks, induction trees, Bayesian analysis, genetic programming, and genetic algorithms for estimating software size, effort, and cost [11,15,26,36]. Results of their studies indicate that regression is a promising approach.

Traditionally, software metrics have been used for procedural languages [32,34]. OO systems differ in two ways. First, they allow for polymorphism and inheritance, which is not available in procedural languages. They reduce the size of the system (the lines of code) and the number of logical constructs (sequences, decisions, or loops) that reduce the procedural complexity of a program [9]. Second, OO systems allow encapsulation. However, Sheetz et al. [43] argue that this is not limited only to OO systems. The software complexity of OO systems occurs at the variable, method, object, and application levels. Several researchers have proposed software metrics to measure the complexity of OO systems [10,17–20,29,30,48]. A few used field data validate some of these proposed metrics.

Some researchers have used a component-based method (CBM) to estimate system size [49]. In it, the size of individual components or modules is obtained and system size is estimated by adding the individual component sizes. The components identified in the Verner–Tate study include menus, input, and reports/inquiries. Using linear regression on 27 actual cases, they validated their CBM using SLOC as a dependent variable and different components as independent variables. Approaches similar to CBM were used by Hakuta et al. [16] and Humphrey [21]. Among the advantages of CBM is that it can be adapted to the environment and thus maintain diversity in the independent variables.

## 3. Estimating the size of software components

CBM was used and validated in the Informix-4GL environment. Proponents of CBM have reported several advantages of including accurate bottom-up size estimation and an adaptability to different programming environments. However, it has not been used and validated in an OO environment. Using CBM in an OO environment requires accurate size forecasts for the individual components. The purpose of this study is to identify factors that may determine the size of individual OO software components.

Rothenberger and Hershauer [41] argued that FP can be used to measure software complexity. Laranjeira showed that FP and software size were directly linearly related. The size of an OO system depends its complexity and vice versa. There are three levels of complexity for an OO system: method, class, and system. Chidamber and Kemerer noted that complexity at the method level is determined by the number of methods used in a class. They stated that the number of methods increases the amount of time and effort required to develop and maintain the class. Furthermore, many methods in a class have a large effect on sub-classes, since they inherit all the methods from their parent. Given this, many methods impose restrictions or cause difficulties in the ability to inherit. The number of parameters used increases the cognitive complexity. The effect on component size of the number of parameters in a method is not well established. This leads to our first proposition.

## Proposition 1. More methods per component lead to a higher OO component SLOC.

Class-level complexity depends on the complexity of the class, the complexity of any inherited class, and the number of inherited classes. It may be explained by the complexity of methods. An increasing number of sub-classes that inherit methods of a parent class increases the complexity of the parent. Chidamber and Kemerer identify the following reasons for an increase in complexity: with an increase in the number of sub-classes, the level of reuse increases and more testing is necessary to gain reliability assurance. This leads to our second proposition.

Proposition 2. More sub-classes lead to a higher OO component SLOC.

System-level complexity includes non-OO parts that may be too relevant to be neglected. System-level non-OO parts include a set of global definitions of types, structures, unions, and global declarations of the variables. The complexity at the system level may be measured as: the number of system functions/ procedures, the number of global definitions, the number of global variables, the number of graphical user interface (GUI) elements in a component, and the number of events and state changes handled by a window. Since the effects of the number of GUI elements in a component and of the number of events and state changes have received little attention, we propose our third and fourth propositions.

Proposition 3. More GUI elements in a component leads to a higher OO component SLOC.

## Proposition 4. More events handled by a component leads to a higher OO component SLOC.

Earlier CBM studies categorized components based on their functionality. Verner et al used three categories: menus, input, and reports/inquiries. Dolado’s study illustrated the fact that component type is an important factor affecting software size. Damiani et al., highlighting the importance of a software component classification by type of component, asserted that ‘‘we believe that correct component classification can help to address several other problems, besides reuse, such as code comprehension for reverse engineering, dynamic domain modeling, evaluation of programming language dependencies, and usage patterns.’’ They suggested the following six principles for classifying OO software components:

1. descriptor-based behavioral classification;

2. controlled granularity;

3. language independence;

4. trainable user-adaptive response;

5. support for both query and navigational interfaces;

6. thesaurus-based controlled vocabulary.

Bielak, in his study, categorized an application into seven different OO packages of related behavioral functionality. These, termed component types, are:

1. Application component: A high-level user interface component that allows user data display and editing, object property dialogs, and calculation setup dialogs.

2. Data component: An abstract data object factor that provides GUI components for user data selection.

3. Filter component: A GUI component that can be used for importing and exporting foreign data formats.

4. GUI components: Simple GUI components, such as text fields, radio buttons, etc.

5. Business components: Basic abstract business objects.

6. Concrete business input/output components: Concrete input/output components for abstract business components.

7. Application support components: User display and editing, object property dialogs, and calculation setup dialogs.

The different types of component represent different levels of complexity. For example, Bielak writes, ‘‘At the business object level (Obj), components are relatively compact, with behaviors generally restricted to read, write, and data accessors. Indeed, several ‘set’ and ‘get’ functions consist of nothing more than one or two lines of code. At the other extreme, user interface member functions are on average several SLOC larger, carrying the burden of code required to process widget instantiation and configuration, event handling, and display updating.’’ This leads to our fifth and last proposition.

## Proposition 5. The type of component has a significant effect on the OO component SLOC

Using SLOC as a measure of OO component size may have an advantage over using FP. For example, information on all the independent variables can be easily obtained from unified modeling language (UML) diagrams [42] drawn in the systems analysis phase. Using FP requires rating several subjectively developed weighting and complexity factors; these may add to the software development cost [28].

## 4. Data collection and analysis

Data for 152 components were obtained from a reallife X/Motif-based Cþþ research and data-analysis application. The development time for the application was 24 months; a staff of four to nine full-time developers created the component-based application. The details of our data are available in Bielak’s paper.

Since all of the 152 components come from one project, the results of our analysis are not confounded by the effects of multiple programming languages, tools, team dynamics [45], and project personnel. One project data analysis had been conducted in a previous a study. In fact, Rothenberger and Hershauer implied that, when using SLOC as a dependent variable, the internal validity of a study was strengthened if the code was written within the same subject domain and all components were written in the same programming language. The increase in the strength of internal validity, by using one project data analysis, came at the expense of a lower external validity of the results.

We used multiple-regression to test our first four propositions. The dependent variable was SLOC and the independent variables were the number of methods, sub-classes, GUI elements, and events in a component. Table 1 illustrates the inter-item correlations between the model-independent variables. All of the inter-item correlations were less than 0.6, indicating a lack of multicollinearity between the independent variables. Table 2 illustrates the statistical significance results of the overall regression model. The overall model was significant at the 0.01 level. Furthermore, 86% of the variance in the dependent variable was explained by the variances in the independent variables.

Table 1  
Correlations between the independent variables

<table><tr><td></td><td>Events</td><td>GUI elements</td><td>Methods</td><td>Sub-classes</td></tr><tr><td>Events</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>GUI elements</td><td>0.586*</td><td>1.000</td><td></td><td></td></tr><tr><td>Methods</td><td>0.468*</td><td>0.308*</td><td>1.000</td><td></td></tr><tr><td>Sub-classes</td><td>0.500*</td><td>0.399*</td><td>0.369*</td><td>1.000</td></tr></table>

Significant at a ¼ 0:01.

Table 2  
Multiple regression results for the overall model

<table><tr><td>Source</td><td>d.f.</td><td>Sum of squares</td><td>Mean square</td><td>F value</td></tr><tr><td>Model</td><td>4</td><td>37900000</td><td>9470000</td><td>231*</td></tr><tr><td>Error</td><td>147</td><td>6040000</td><td>41100</td><td></td></tr><tr><td>Corrected total</td><td>151</td><td></td><td></td><td></td></tr></table>

Significant at $\alpha = 0 . 0 1$ ; $R ^ { 2 } = 0 . 8 6 .$

Table 3  
The regression parameters and their significance

<table><tr><td>Parameter(hypothesis no.)</td><td>Estimate</td><td>S.E.</td><td>t value</td><td>Pr &gt; |t|</td></tr><tr><td>Intercept</td><td>-25.1</td><td>25.1</td><td>-1.00</td><td>0.320</td></tr><tr><td>Methods (H1)</td><td>8.05</td><td>1.07</td><td>7.46</td><td>0.0001*</td></tr><tr><td>Sub-classes (H2)</td><td>9.41</td><td>1.79</td><td>5.25</td><td>0.0001*</td></tr><tr><td>GUI elements (H3)</td><td>15.9</td><td>1.19</td><td>13.4</td><td>0.0001*</td></tr><tr><td>Events (H4)</td><td>11.3</td><td>2.05</td><td>5.53</td><td>0.0001*</td></tr></table>

Significant at a ¼ 0:01.

Table 3 illustrates the regression coefficients and statistical significances of each of the individual variables. The results indicated that all the four independent variables were statistically significant at the 0.01 level. Thus, all four propositions were significant. Based on the values of the regression coefficients, the number of GUI elements in a component had the largest effect on SLOC, followed by the number of events, the number of sub-classes, and the number of methods, respectively.

To test the fifth proposition, we used one-way-ANOVA with SLOC as a dependent variable and the type of component as an independent variable. Table 4 illustrates the results of the one-way-ANOVA test and Table 5 illustrates the means and standard deviations of different software components. The results indicate that Proposition 5 is significant at the 0.01 level. The variance in SLOC explained by the type of software component is 23%.

Table 4  
The one-way-ANOVA results for the overall model

<table><tr><td>Source</td><td>d.f.</td><td>Sum of squares</td><td>Mean square</td><td>F value</td></tr><tr><td>Model</td><td>6</td><td>9900000</td><td>1650000</td><td>7.03*</td></tr><tr><td>Error</td><td>145</td><td>34000000</td><td>235000</td><td></td></tr><tr><td>Corrected total</td><td>151</td><td>43900000</td><td></td><td></td></tr></table>

Significant at a ¼ 0:01; $R ^ { 2 } = 0 . 2 3$

Table 5  
Descriptive statistics of different software components

<table><tr><td>Component type</td><td>Number of components</td><td>Mean (SLOC)</td><td>S.D.</td></tr><tr><td>Application</td><td>67</td><td>739</td><td>650</td></tr><tr><td>Data</td><td>6</td><td>288</td><td>424</td></tr><tr><td>Filter</td><td>14</td><td>400</td><td>481</td></tr><tr><td>GUI</td><td>21</td><td>300</td><td>267</td></tr><tr><td>Business</td><td>14</td><td>148</td><td>123</td></tr><tr><td>I/O</td><td>15</td><td>230</td><td>159</td></tr><tr><td>Application support</td><td>15</td><td>118</td><td>130</td></tr></table>

Table 5 indicates that application components are likely to have a greater size than other components. Since the type of software component may play an important role in the overall size of the software, we conducted pair-wise difference-in-means comparisons for different software components. For seven different types of component, we had $^ 7 C _ { 2 } = 2 1$ different pairwise difference-in-means comparisons.

Table 6 illustrates the results for all the 21 different pair-wise difference-in-means comparisons.

The results from Table 6 indicate that the application components had larger sizes than all other components. However, given the unequal component type sample sizes of the OO components, the results of Table 6 may not be robust. Tukey or Scheffe post hoc multiple-comparison tests are recommended for unequal group sample sizes [46]. We performed both; Tables 7 and 8 illustrate the results. The entries in the cells are absolute values of difference-in-means and their significance.

The results in Tables 6–8 indicate that application component type had a larger size when compared to GUI, I/O, and business and application support component types. No other differences-in-means were significant. Thus, software application with a higher number of application components was likely to have a large size, in terms of SLOC, than software application with fewer components.

Pairwise difference-in-means comparisons for different software components

<table><tr><td>Contrast components</td><td>d.f.</td><td>Sum of square</td><td>Mean square</td><td>F value</td></tr><tr><td>Application vs. data</td><td>1</td><td>1120000</td><td>1120000</td><td>4.77**</td></tr><tr><td>Application vs. filter</td><td>1</td><td>1330000</td><td>1330000</td><td>5.66**</td></tr><tr><td>Application vs. GUI</td><td>1</td><td>3080000</td><td>3080000</td><td>13.1*</td></tr><tr><td>Application vs. business</td><td>1</td><td>4040000</td><td>4040000</td><td>17.2*</td></tr><tr><td>Application vs. I/O</td><td>1</td><td>3180000</td><td>3180000</td><td>13.5*</td></tr><tr><td>Application vs. application support</td><td>1</td><td>4730000</td><td>4730000</td><td>20.1*</td></tr><tr><td>Data vs. filter</td><td>1</td><td>53200</td><td>53200</td><td>0.23</td></tr><tr><td>Data vs. GUI</td><td>1</td><td>720</td><td>720</td><td>0.00</td></tr><tr><td>Data vs. business</td><td>1</td><td>82400</td><td>82400</td><td>0.35</td></tr><tr><td>Data vs. I/O</td><td>1</td><td>14600</td><td>14600</td><td>0.06</td></tr><tr><td>Data vs. application support</td><td>1</td><td>124000</td><td>124000</td><td>0.53</td></tr><tr><td>Filter vs. GUI</td><td>1</td><td>84100</td><td>84100</td><td>0.36</td></tr><tr><td>Filter vs. business</td><td>1</td><td>447000</td><td>447000</td><td>1.90</td></tr><tr><td>Filter vs. I/O</td><td>1</td><td>212000</td><td>212000</td><td>0.90</td></tr><tr><td>Filter vs. application support</td><td>1</td><td>579000</td><td>579000</td><td>2.47</td></tr><tr><td>GUI vs. business</td><td>1</td><td>195000</td><td>195000</td><td>0.83</td></tr><tr><td>GUI vs. I/O</td><td>1</td><td>43900</td><td>43900</td><td>0.19</td></tr><tr><td>GUI vs. application support</td><td>1</td><td>291000</td><td>291000</td><td>1.24</td></tr><tr><td>Business vs. I/O</td><td>1</td><td>48200</td><td>48200</td><td>0.21</td></tr><tr><td>Business vs. application support</td><td>1</td><td>6540</td><td>6540</td><td>0.03</td></tr><tr><td>I/O vs. application support</td><td>1</td><td>93500</td><td>93500</td><td>0.40</td></tr></table>

Significant at a ¼ 0:01.  
\*\* Significant at a ¼ 0:05.

The coefficients of the linear regression provided several decision support advantages. From Table 3, the regression-based forecasting model for OO component size can be written as

$$
\begin{array}{r l} S L O C & = 8. 0 5 \times M e t h o d s + S u b - C l a s s e s \\ & + 1 5. 9 G U I E l e m e n t s + 1 1. 3 E v e n t s - 2 5. 1 \end{array}
$$

Pairwise difference-in-means comparisons using Tukey’s post hoc test

<table><tr><td></td><td>Application</td><td>GUI</td><td>Data</td><td>Filter</td><td>I/O</td><td>Business</td></tr><tr><td colspan="7">Application</td></tr><tr><td>GUI</td><td>439*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data</td><td>451</td><td>12.4</td><td></td><td></td><td></td><td></td></tr><tr><td>Filter</td><td>339</td><td>100</td><td>112</td><td></td><td></td><td></td></tr><tr><td>I/O</td><td>509*</td><td>70.9</td><td>58.5</td><td>171</td><td></td><td></td></tr><tr><td>Business</td><td>591*</td><td>152</td><td>140</td><td>252</td><td>81.6</td><td></td></tr><tr><td>Application support</td><td>621*</td><td>182</td><td>170</td><td>283</td><td>112</td><td>30.1</td></tr></table>

Significant at a ¼ 0:01.

Table 8 Pairwise difference-in-means comparisons using Scheffe’s post hoc test

<table><tr><td></td><td>Application</td><td>GUI</td><td>Data</td><td>Filter</td><td>I/O</td><td>Business</td></tr><tr><td colspan="7">Application</td></tr><tr><td>GUI</td><td>439**</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Data</td><td>451</td><td>12.4</td><td></td><td></td><td></td><td></td></tr><tr><td>Filter</td><td>339</td><td>100</td><td>112</td><td></td><td></td><td></td></tr><tr><td>I/O</td><td>509**</td><td>70.9</td><td>58.5</td><td>171</td><td></td><td></td></tr><tr><td>Business</td><td>591**</td><td>152</td><td>140</td><td>252</td><td>81.6</td><td></td></tr><tr><td>Application support</td><td>621*</td><td>182</td><td>170</td><td>282</td><td>112</td><td>30.1</td></tr></table>

Significant at a ¼ 0:01.  
Significant at a ¼ 0:05.

The coefficients of regression are marginal values: a partial derivative of a dependent variable with respect to any one independent variable. For example, the following set represents the set of marginal values for the forecasting model:

$$
\begin{array}{l} \left\{\frac {\partial S L O C}{\partial M e t h o d s}, \frac {\partial S L O C}{\partial S u b - C l a s s e s}, \frac {\partial S L O C}{\partial G U I E l e m e n t s}, \frac {\partial S L O C}{\partial E v e n t s} \right\} \\ = \{8. 0 5, 9. 4 1, 1 5. 9, 1 1. 3 \} \end{array}
$$

The marginal value provides information on the change in the value of the dependent variable with a unit increase in the value of the independent variable. Using the marginal value for the variable Methods, it can be concluded that the size of a component increased by approximately eight lines of code if a new method was added. By the same token, the size of a component increased by almost 16 lines of code if a new GUI element was added. Marginal values provide valuable information for software managers. Based on them, it can be seen that reducing the number of GUI elements significantly reduced the OO component size. If a manager had a choice between two UML diagrams for the same OO application, then the one with a smaller number of GUI elements was preferable, resulting in a lower OO component size.

The forecasting accuracy of OO component size can be further improved if a non-linear model is used to learn a forecasting function. Non-linear regression models improve forecasting accuracy, but do not provide information on marginal values. The selection of a non-linear model is important. For example, if a non-linear quadratic regression model is chosen then one is making an assumption of a quadratic relationship between the independent and the dependent variables. Non-linear regression approaches that do not establish a priori functional form fall under three general categories; regression tree, neural network, and genetic programming models. All are non-para metric. Neural network models, while performing well, do not provide any decision-making information. Furthermore, their results are highly dependent on the initial selection of a random set of weights, and multiple runs on the same data may lead to different results.

Genetic programming models are computationally intensive and require longer run times and volatile memory [3]. Regression tree models are more efficient than genetic programming and neural network models [37]. In a study comparing a regression tree model and neural networks for forecasting software effort, Srinivasan and Fisher found that the former performs as well as the latter. We examined different non-linear forecasting models, and selected two that met the following criteria:

1. the non-linear model should not have any a priori structural restriction;

2. the non-linear model should be easy to interpret.

Two sets of non-linear forecasting models met our selection criteria. Both were regression tree models that represent the regression model in the form of a decision tree.

## 4.1. Regression tree analysis

We used classification and regression tree (CART) and chi-squared automatic interaction detection (CHAID) for non-linear regression analysis. The CART algorithm derives a non-parametric, non-linear regression tree for a given set of training data. CHAID is a statistical algorithm that can be used to derive regression trees. The appendix provides a brief introduction to them.

Regression tree models approximate the forecasting function in a staircase function. Fig. 1 illustrates a regression tree with the actual forecasting function shown as a bold curve and the staircase forecasting function, learned by the regression tree, shown as histograms using dotted lines.

![](/api/attachments/DFY6AMQ5/fulltext/images/f46c7f2bbab68c3b2bd7590a3a8694bb3a0ecea63f9b5a994c41f075bf7f9d98.jpg)  
Fig. 1. The function Y ¼ f ðXÞ approximation by a regression tree.

## 4.2. CART

CART provides a regression tree that is sometimes easier to interpret than a simple linear regression model [8]. Fig. 2 illustrates its regression tree. The stopping criterion is the lowest average square of error (the resubstitution error) for training and cross-validation. Fig. 3 shows a plot of the cross-validation and the resubstitution error versus the number of nodes in the regression tree. The resubstitution error decreases as the number of nodes in the regression tree increases and finally stabilizes. The minimum cross-validation error and the resubstitution error were obtained for a regression tree with 27 nodes.

The regression tree developed by CART has several decision support advantages: several heuristic decision rules can be derived from it. A sample of such a decision rule is

IF Number of GUI Elements > 34 AND

Number of Methods 	 53:5

$$
\text { THEN   } S L O C = 2 7 6 0 (S. D. = 1 6 6)
$$

The standard deviation figure can be used to estimate confidence limits. For example, assuming a normal distribution and 3s confidence (99.7%), if m represents the mean value of forecast and s represents the standard deviation then a confidence interval of $[ \mu - 3 \sigma , \mu + 3 \sigma ]$ can be used as a lower and upper bound for the forecast. Thus, if the number of GUI elements is greater than 34 and the number of methods is greater than or equal to 54 then there is a 99.7% chance that SLOC $( \mu = 2 7 6 0 , \sigma = 1 6 6 )$ is within the closed interval [2260, 3260].

![](/api/attachments/DFY6AMQ5/fulltext/images/a7dfcd6724d13a6f4c06d1e1ef389089bbba3732e57f482ceb1b176bd0bdc488.jpg)  
Fig. 2. Regression tree using the CART algorithm.

The CART algorithm also provides information about the contribution of the independent variable in the prediction of the size of the dependent variable.

The variable that provides the highest improvement in the resubstitution estimate for a split corresponds to the highest relative importance. The variable with the highest relative importance, typically occupies the root position in the regression tree as it is the most important predictor of the dependent variable, followed by the other variables. Table 9 illustrates the results of the variables’ relative importance in the prediction of SLOC.

![](/api/attachments/DFY6AMQ5/fulltext/images/bba0c3570e366d6f8d1d9ca83721bf50c6d704cdc781dd9a3c3acc9833a23f59.jpg)  
Fig. 3. Cross-validation and resubstitution errors vs. number of nodes in regression tree.

Table 9  
The relative variable importance

<table><tr><td>Variable</td><td>Relative importance</td></tr><tr><td>GUI element</td><td>100.00</td></tr><tr><td>Events</td><td>70.9</td></tr><tr><td>Sub-classes</td><td>61.6</td></tr><tr><td>Methods</td><td>24.3</td></tr></table>

## 4.3. CHAID

Since CHAID uses statistically significant differences to determine splits, CHAID trees are usually smaller than CART trees. Furthermore, CHAID is noted for its resistance to overfitting the training data; this occurs when the forecasting function, in addition to learning the general patterns, fits the noise present in the training data. Fig. 4 illustrates the regression tree obtained using the enhanced version of CHAID. The level of significance used to determine cut-off value was 0.05.

There were a total of 22 nodes in the CHAID regression tree. All independent variables were found to be statistically significant and used for splits.

CHAID trees, because of their smaller size, have an advantage in eliciting concise decision-making heuristics. But they result in fewer useful decision-making rules. For example, using only the first level split, Fig. 4 can be translated into three rules:

Rule 1: IF (number of sub-classes 3) THEN SLOC ¼ 193.

Rule 2: IF (number of sub-classes > 3) AND (number of sub-classes $\leq 1 4 )$ THEN SLOC ¼ 607. Rule 3: IF (number of sub-classes > 14) AND (number of sub-classes  63) THEN SLOC ¼ 1220.

More specific rules can be obtained using second level and third level splits. The standard deviation information can be used to develop confidence intervals.

We used three different regression models. Two, linear regression and CHAID, are statistical approaches allowing hypothesis testing. There are subtle differences in the models and no one model can serve all the decision-making needs. Linear models may not be very accurate predictors. Additionally, they may need information on all the four independent variables to make a good prediction. The same may not be true for regression tree models. For example, the CHAID tree, for any given set of branches from the initial to the final terminal node, does not use more than three independent variables to predict SLOC. We believe that regression trees may sometimes be useful when it is desirable to predict SLOC with partial data. For example, when a CART tree is available from historical data, it may be possible to get the OO component size estimates when information on the number of GUI elements and the number of methods is available. Using the tree shown in Fig. 2, if the number of GUI elements is greater than 34 and the number of methods is greater than 54 then the expected SLOC is approximately 2760. The estimate does not change when other information about sub-classes and events becomes available. Early in the systems analysis phase, most projects have uncertain and partial information and CART may be a useful forecasting tool then.

![](/api/attachments/DFY6AMQ5/fulltext/images/cf81589b295af50c295c4c1e4908f9dba5ba8d72f402f32a041320a8f0bd9699.jpg)  
Note: The Numbers in the Box represent Mean (Standard Deviation). The variable N is number of training examples that belong to thebranch.  
Fig. 4. Regression tree using the CHAID algorithm.

When choosing between CHAID and CART regression trees, a decision maker may have to consider several factors. First, CART does not provide information on statistical significance, and has a tendency to overfit the training data. Additionally, since all the splits in CART are binary, a CART tree may lead to more specific rules than a CHAID tree. It is likely that CART and CHAID trees will perform differently when the training data contain a large amount of noise.

## 5. Conclusions and summary

Using a few software complexity measures from the literature, we developed and tested linear and nonlinear forecasting models for estimating OO software component size. Our contributions are two-fold. First, we identified different types of software components and show that some may have a larger size than others. Second, using software complexity and metrics literature, we identified some variables that may be used to estimate OO component size.

We believe that it is beneficial for project managers to classify software components into different complexity and component-type categories. For example, application components may require a higher allocation of resources than the other components and a larger development team for application components may be justified.

We have used regression tree-based non-linear models for forecasting. There are several other models that can be used to estimate software size. We believe that regression tree models have an advantage for eliciting decision-making heuristics that can then be represented in IF–THEN rules.

Our study is exploratory and we recognize problems in generalizing the findings. We believe that generalization of our findings to system development with different problem domains, languages, or system size may be limited. Furthermore, there may be other variables, that have an effect. All the components for our study came from one application. Using components from one application may, of course, preserve internal validity of the study at the expense of the external validity.

## Acknowledgements

We thank James Bielak of Greenstone Software Architecture and Consulting for providing the data for the research and for reviewing the first draft of the manuscript. Thanks are also due to the anonymous referees for their valuable comments.

## Appendix A. Introduction to CART and CHAID

## A.1. Classification and regression tree algorithm

Classification and regression trees is a binary decision tree algorithm that is used in data mining problems involving classification and regression. The CART constructs a binary decision tree by splitting data set in a way that the data in the descendant subsets are more pure than the data in the parent set. For example, in a regression problem, let $( x _ { n } , y _ { n } )$ represent nth example, where $x _ { n }$ is the nth example vector on independent variables and $y _ { n }$ is the value of the dependent variable. If there are total of N examples then CART calculates a best split $s ^ { * }$ so that following is maximized over all possible splits S:

$$
\Delta R (s ^ {*}, t) = \underset {s \in S} {\operatorname{argmax}} \Delta R (s, t)
$$

where $\Delta R ( s , t ) = R ( t ) - R ( t _ { \mathrm { L } } ) - R ( t _ { \mathrm { R } } )$ is improvement in resubstitution estimate for split s of t. The resubstitution estimate $R ( t )$ is defined as follows:

$$
R (t) = \frac {1}{N} \sum_ {x _ {n} \in t} (y _ {n} (t)) ^ {2}
$$

The variables $t _ { \mathrm { L } }$ and $t _ { \mathrm { R } }$ are left and right values for split t. The variable $y ( t )$ is defined as follows:

$$
y (t) = \frac {1}{N (t)} \sum_ {x _ {n} \in t} y _ {n}
$$

where $N ( t )$ is the total number of cases in t. The tree continues to grow until a node is reached such that no significant decrease in resubstitution estimate is possible. This node is the terminal node.

## A.1.1. V-fold cross-validation in CART

If O represents the learning set consisting of $( x _ { 1 } , y _ { 1 } )$ $\dots , ( x _ { N } , y _ { N } )$ , and $d ( { \pmb x } )$ denotes a predictor (regression tree) then the resubstitution estimate is given by

$$
R (d) = \frac {1}{N} \sum_ {n} (y _ {n} - d (\boldsymbol {x} _ {n})) ^ {2}
$$

Let $R ^ { * } ( d )$ denote the resubstitution estimate for the best predictor (regression tree) given a learning data set. The value of $R ^ { * } ( d )$ depends on the scale used to measure the responses. To make the resubstitution estimate independent of the scale, a normalized resubstitution estimate is used. If $\mu = E ( y )$ then $R ^ { * } ( \mu ) =$ $E ( y - \mu ) ^ { 2 }$ is the variance of y.

The normalized resubstitution estimate is given by

$$
R E ^ {*} = \frac {R ^ {*} (d)}{R ^ {*} (\mu)}
$$

We use V-fold cross-validation to test the performance of the generated regression tree. In V-fold cross-validation we divide the original data O into V sub-sets $\Omega _ { 1 } , . . . , \Omega _ { 5 } ,$ each containing almost same number of cases. For each sub-set $V \in \{ 1 , 2 , \dots , 5 \}$ , we apply the CART construction procedure and test it on remaining four samples. The cross-validation resubstitution estimate can be written as

$$
R ^ {\mathrm{CV}} (d) = \frac {1}{N} \sum_ {v} \sum_ {(x, y) \in \Omega} \left(y _ {n} - d ^ {(v)} (\boldsymbol {x} _ {n})\right) ^ {2}
$$

The relative cross-validation error can be computed as follows:

$$
R E ^ {\mathrm{CV}} (d) = \frac {R ^ {\mathrm{CV}} (d)}{R (\ddot {y})}
$$

where

$$
\ddot {y} = \frac {1}{N} \sum_ {n} y _ {n}
$$

and

$$
R (\ddot {y}) = \frac {1}{N} \sum_ {n} (y _ {n} - \ddot {y}) ^ {2}
$$

More information on CART is available in Breimann et al. textbook.

## A.2. Chi-squared automatic interaction detection

CHAID is a heuristic statistical method that examines the relationships between many categorical independent variables and a single categorical dependent variable. For data with continuous values, the CHAID divides data into equal fixed (usually 10) categories, and then merges the categories that are judged to be statistically insignificant. When dependent variable is categorical a chi-squared test is used and when dependent variable is continuous, F-test is used for determining statistical significance. More information on the CHAID and an improved version, used in our research, the exhaustive CHAID is available in Kass [24] and Bigg et al. [5] respectively.

## References

[1] A.J. Albrecht, Measuring application development productivity, in: Proceedings of the IBM Applications Development Symposium, Monterey, CA, 1979, pp. 83–92.

[2] R.D. Banker, S.M. Datar, C.F. Kemerer, A model to evaluate variables impacting the productivity of software maintenance projects, Management Science 37 (1), 1991, pp. 1–18.

[3] S. Bhattacharyya, P.C. Pendharkar, Inductive, evolutionary and neural techniques for discrimination: a comparative study, Decision Sciences 29 (4), 1998, pp. 871–900.

[4] J. Bielak, Improving Size Estimates Using Historical Data, IEEE Software, November–December 2000, pp. 27– 35.

[5] D. Biggs, B. De Ville, E. Suen, A method of choosing multiway partitions for classification and decision trees, Journal of Applied Statistics 18, 1991, pp. 49–62.

[6] B.W. Boehm, Software Engineering Economics, Englewoods Cliffs, Prentice Hall, NJ, 1981.

[7] G.J. Bozoki, Performance simulation of SSM (Software Sizing Model), in: Proceedings of the 13th Conference of International Society of Parametric Analyst, New Orleans, 1991, CM-14.

[8] L. Breiman, J.H. Friedman, R.A. Olshen, C.J. Stone, Classification and Regression Trees, Belmont, Wadsworth International Group, CA, 1984.

[9] D.N. Card, R.L. Glass, Measuring Software Design Quality, Englewood Cliffs, Prentice Hall, NJ, 1990.

[10] S.R. Chidamber, C.F. Kemerer, A metrics suite for object oriented design, IEEE Transactions on Software Engineering 20 (6), 1994, pp. 476–493.

[11] S. Chulani, B. Boehm, B. Steece, Bayesian analysis of empirical software engineering cost models, IEEE Transactions on Software Engineering 25 (4), 1999, pp. 573–583.

[12] S.D. Conte, H.E. Dunsmore, V.Y. Shen, Software Engineering Metrics and Models, Benjamin/Cummings, New York, 1986.

[13] E. Damiani, M.G. Fugini, C. Bellettini, A hierarchy-aware approach to faceted classification of object-oriented components, ACM Transactions on Software Engineering and Methodology 8 (4), 1999, pp. 425–472.

[14] J.J. Dolado, A validation of the component-based method for software size estimation, IEEE Transactions on Software Engineering 26 (10), 2000, pp. 1006–1021.

[15] G.R. Finnie, G.E. Wittig, J.M. Desharnais, A comparison of software effort estimation techniques: using function points with neural networks, case-based reasoning and regression models, Journal of Systems and Software 39 (3), 1997, pp. 281–289.

[16] M. Hakuta, F. Tone, M.A. Ohminami, A software size estimation model and its evaluation, Journal of Systems and Software 37, 1997, pp. 253–263.

[17] B. Henderson-Sellers, Identifying internal and external characteristics of classes likely to be useful as structural complexity metrics, in: Proceedings of the International Conference on Object Oriented Information Systems, 1994, pp. 227–230.

[18] B. Henderson-Sellers, D. Tegarden, D. Monarchi, Metrics and project management support for an object-oriented software development, in: Tutorial Notes of International Conference on Technology of Object-Oriented Languages and Systems, 1994.

[19] B. Henderson-Sellers, Some metrics for object-oriented software engineering, in: Proceedings of the International Conference on Technology of Object-Oriented Languages and Systems, 1991, pp. 131–139.

[20] T.P. Hopkins, Software Quality Management II: Building Quality into Software, Computational Mechanisms Press, 1994.

[21] W.A. Humphrey, Discipline for Software Engineering, Addison-Wesley, 1995.

[22] P.M. Johnson, C.A. Moore, J.A. Dane, R.S. Brewer, Empirically guided software effort guesstimation, IEEE Software, 2000, pp. 51–56.

[23] C. Jones, Programming Productivity, McGraw-Hill, New York, 1986.

[24] G. Kass, An exploratory technique for investigating large quantities of categorical data, Applied Statistics 29 (2), 1980, pp. 119–127.

[25] C.F. Kemerer, Reliability of function points measurement: a field experiment, Communications of the ACM 36 (2), 1993, pp. 85–97.

[26] S. Krishnamoorty, D. Fisher, Machine learning approaches to estimating software development effort, IEEE Transactions on Software Engineering 21 (2), 1995, pp. 126–137.

[27] L.A. Laranjeira, Software size estimation of object-oriented systems, IEEE Transactions on Software Engineering 16 (5), 1990, pp. 510–522.

[28] A. Lee, C.H. Cheng, J. Balakrishnan, Software development cost estimation: integrating neural network with cluster analysis, Information and Management 34, 1998, pp. 1–9.

[29] W. Li, S. Henry, Object-oriented metrics that predict maintainability, Journal of Systems and Software 23, 1993, pp. 111–122.

[30] M. Lorenz, J. Kidd, Object-oriented software metrics: a practical guide, Englewood Cliffs, Prentice Hall, NJ, 1994.

[31] G.C. Low, D.R. Jeffery, Function points in the estimation and evaluation of software process, IEEE Transactions on Software Engineering 16 (1), 1990, pp. 81–84.

[32] T.J. McCabe, A complexity measure, IEEE Transactions on Software Engineering 2 (4), 1976, pp. 308–320.

[33] E. Miranda, Improving subjective estimates using paired comparisons, IEEE Software, 2001, pp. 87–91.

[34] P. Nesi, T. Querci, Effort estimation and prediction of objectoriented systems, Journal of Systems and Software 42 (1), 1998, pp. 89–102.

[35] R. Pressman, Software Engineering: A Practitioner’s Approach, McGraw-Hill, New York, 1982.

[36] P.C. Pendharkar, G.H. Subramanian, Application of Learning Curve Theory for Mining Effort-Experience Curves from CASE Tool Usage Data, Working Paper, 2003 (available from http://www.personal.psu.edu/pxp19/pap.html).

[37] P.C. Pendharkar, S. Nanda, A Misclassification Cost Minimizing Evolutionary Neural Approach, Working paper, 2003 (available from the first author upon request).

[38] S. Purao, H.K. Jain, D.L. Nazareth, ODE: a tool for distributing object-oriented applications, Information and Management 39, 2002, pp. 689–703.

[39] L. Putnam, General empirical solution to the macro software sizing and estimating problem, IEEE Transactions on Software Engineering 4, 1978, pp. 345–361.

[40] A. Repenning, A. Ioannidou, M. Payton, W. Ye, J. Roschelle, Using components for rapid distributed software development, IEEE Software, 2001, pp. 38–45.

[41] M.A. Rothenberger, J.C. Hershauer, A software reuse measure: monitoring an enterprise-level model driven development process, Information and Management 35, 1999, pp. 283–293.

[42] J. Schmuller, Sams Teach Yourself UML in 24 hours, Sams publishing, Indianapolis, IN, 1999.

[43] S.D. Sheetz, D.P. Tegarden, D.E. Monarchi, A software complexity model for object-oriented systems, Decision Support Systems 13, 1995, pp. 241–262.

[44] G.H. Subramanian, G.E. Zarnich, An examination of some software development effort and productivity determinants in ICASE tool projects, Journal of Management Information Systems 12 (4), 1996, pp. 143–160.

[45] S.W. Sussman, P.J. Guinan, Antidotes for high complexity and ambiguity in software development, Information and Management 36, 1999, pp. 23–35.

[46] B.G. Tabachnick, L.S. Fidell, Computer-Assisted Research Design and Analysis, Allyn and Bacon, Boston, 2001.

[47] D.P. Tegarden, S.D. Sheetz, D.E. Monarchi, The Effectiveness of Traditional Metrics for Object-Oriented Systems, in: Proceedings of the 25th Hawaii International Conference on System Sciences, IV, 1992, pp. 359–368.

[48] D. Thomas, I. Jacobson, Managing object-oriented software engineering, in: Tutorial Notes of International Conference on Technology of object-oriented languages and systems, 1989, pp. 52–56.

[49] J. Verner, G. Tate, A software size model, IEEE Transactions on Software Engineering 18 (4), 1992, pp. 265– 278.

[50] K. Wiegers, Stop promising miracles, Software Development 8 (2), 2000, pp. 49–49.

![](/api/attachments/DFY6AMQ5/fulltext/images/d3f8bd8c62ef19e698e5de20a5a762c760220586513adde2fca667f111ea2c3d.jpg)

Parag Pendharkar is an associate professor of information systems at Penn State Harrisburg. His work has appeared, or was accepted, for publication in Annals of Operations Research, Communications of ACM, Computers and Operations Research, Decision Sciences, Decision Support Systems, European Journal of Operational Research, Expert Systems with Applications, Intelligent Systems in

Accounting Finance and Management, IEEE Transactions on Professional Communication, Interfaces, International Journal of Human-Computer Studies, Multiple Valued Logic, Omega, as well as several other journals. He serves on the editorial board of the International Journal of Human-Computer Studies.
