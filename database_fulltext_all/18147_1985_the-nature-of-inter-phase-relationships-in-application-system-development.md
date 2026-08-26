---
otero_id: 18147
otero_key: "VRNFPHKB"
title: "The nature of inter-phase relationships in application system development"
authors: "James D. McKeen"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90024-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Nature of Inter-Phase Relationships in Application System Development

James D. McKeen

School of Business, Queen's University, Kingston, Canada K7L 3N6

This study examines the relationships among the component phases of the development life cycle of computer-based application systems. Results indicate that these relationships not only occur but contribute significantly to the consumption of resources during development. The investigation of these interactions presents a general discussion of the nature of the tradeoffs involved, outlines the form of the interaction models to be tested, and finally, marshals empirical evidence to assess the appropriatenes of the proposed models and the integrity of their structure. Implications drawn from this research for the management and control of application system development are presented.

Keywords: Application system development, development life cycle, inter-phase tradeoffs, project estimation.

![](/api/attachments/VRNFPHKB/fulltext/images/8382e67272be7f33c38a94d20c268cace3615617cf0f0bbde2b3c9316e3f70b8.jpg)

James D. McKeen is an Assistant Professor at the School of Business, Queen's University at Kingston, Canada. He received his Ph.D. in Management Information Systems from the University of Minnesota in 1981. His research interests include the implementation of application systems and strategies for selecting application systems in organizations. He has published articles on related topics in the MIS Quarterly and the Journal of Systems and Software.

North-Holland
Information & Management 9 (1985) 21–31

1. The Structure of Phases in Systems Development

The guiding principle for much of systems development is the life cycle – the realization that application systems go through essentially the same process in their development [7]. Its organizing framework is the identification of development phases. These divide the development task into manageable units of work for which the inputs, outputs, and processes are clearly identified. Although variations do exist among system development methodologies in the identification of phases [4], these are more the result of variations in terminology than content.

Despite broad acceptance of the component phases, the structure or juxtaposition of these phases has undergone many changes. “Traditional” methodologies, for instance, represent the process as a set of phases to be performed in strict sequence. Over time, this representation has given way to different structures. Berrisford and Wetherbe [5], for example, propose “heuristic development”. This constitutes a basic reorientation of the phases by moving the development of the output system forward. The suggestion is that once an output system is tailored to match user requirements, the development of the input system (to deliver the specified outputs) should proceed in a straightforward and efficient traditional manner. With the advent of the “structured” methodologies, a major emphasis has been placed on the interaction and iteration among phases [8,11,25,26]. Yourden [25] distinguishes the classical project life cycle, the semi-structured project life cycle and the structured project life cycle by expanding on the idea of feedback between phases of the project. The application of these methodologies has altered the development process to exploit the high correlation between phases and the functions that must be performed [24]. Gunther [14] uses a phase-function matrix which explicitly shows this overlap and interaction. The explicit recognition of the need for iteration is most prominent in the use of prototyping techniques [18] or “evolutionary” life cycles [26]. With these, successive versions of systems are produced, each involving all phases. As the user views the outputs and suggests changes, more analysis and design is indicated and the system enters a new iteration.

These modifications to the traditional or classical life cycle have focussed on the restructuring of individual phases within the framework. Whether these phases are repositioned or simply repeated, the treatments have seldom included any explicit recognition of the tradeoffs among phases and the ramifications these tradeoffs would have on systems development. With the adoption of more “reactive” methodologies like prototyping, an understanding of interrelationships between phases becomes crucial. Allocation of resources among phases is critical because allocation decisions constitute a major determinant of resource requirements of subsequent phases $[13,23,24]$ and of the eventual outcome of development $[17]$ . Indeed, failure to consider the interrelationships between phases represents a shortfall of current systems development methodologies.

## 2. The Importance of Phases in Systems Development

The elaboration of life cycle phases is important for the management of systems development simply because project estimation, planning, and control are anchored on these component phases. For each separate phase, tasks are identified and estimates for the required resource levels are made. All subsequent progress is then monitored relative to these standards. This approach, however, presupposes that phases of development are independent of one another and makes no explicit recognition of the potential tradeoffs among life cycle phases; e.g., Benbasat and Vessey [3] classify techniques for the estimation of time and cost of system development into four major types: (1) proportion of life cycle method; (2) work factors method; (3) standards method; and (4) manpower life cycle method.

The first three attempt to estimate the time to develop the programming phase of a project and then extrapolate to provide an estimate for the total project (e.g., Donelson [9]). If it is believed that coding and testing together consume fifty percent of the total project effort, then the estimate for the time to develop the programming phase is simply doubled to yield the overall project effort.

The fourth approach is based on a formal representation of manpower utilization rates. It has been found that these rates are adequately expressed by a Rayleigh/Norden equation $[19,20,21]$ which predicts manpower utilized in each time period given in knowledge of (1) total cumulative manpower used on the project expressed in many years and (2) the development time of the project. Both of these parameters, however, are estimated using regression methods with independent variables which describe the programming phase (such as number and type of files and reports, number of application subprograms, complexity of functions, degree of coordination required, skill of programmers and analysts, etc.).

A similar approach to the manpower life cycle method is the use of systems dynamics techniques to model software project development. Abdel-Hamid and Madnick [1,2] use this technique to simulate the effects of rework, personnel turnover, and estimating errors on the costs and duration of a hypothetical project. To date however, their work has assumed that a uniform effort is required throughout the project with no explicit allowance for different phases of development nor of potential interactions among these phases.

Obviously the resultant ability of these methods to produce reliable and accurate forecasts for the management of systems development depends directly on an understanding of the component phase structure of the development process. It is incongruous that, despite our limited understanding of resource consumption behavior over the life cycle phases, the dominant methods for the estimation of resource allocation for systems development are based on exactly this knowledge. It seems reasonable that the resources to be devoted to the programming task will be at least partially dictated by the extent of resources committed to previous stages.

## 3. The Rationale for Inter-Phase Relationships

The first study of inter-phase tradeoffs within the system development cycle arose as much by accident as by design. Graver [13], under contract to the U.S. Air Force, tried to develop estimating relationships for the resources (man-hours, computer-hours, elapsed time) consumed in the different phases of the software life cycle separately, using parametric cost estimating techniques. This approach broke with the majority of previous attempts to apply quantitative methods to the estimation and control of development projects by focussing on the individual phases of development rather than concentrating on total costs. As the data was being analyzed, the authors were compelled to make the following observation:

“Results were at first disappointing. Applying the data to the hypothesized man-hour relationships for the individual phases of the life cycle resulted in less precision than estimates made on the total.... It was at this point that the importance of the relations between phases became clear. Much of the variability in the total, which has been seen previously by various researchers, was due to differences in man-hour allocation among phases in the development process...There are trade-offs between the phases. For example, allocating too few man-hours to analysis and design can cause higher error rates, resulting in increased man-hours for integration and test...Trying to estimate man-hours for each individual phase only accentuates the variance, and the trade-offs implicit in the totals are not considered at all. Statistically speaking, the total variance was bound to be larger since the covariance terms (some of which are negative) were not considered.”

The realization of inter-phase tradeoffs within the development process simply implies that a large part of the resource requirements for any one phase results from the manner in which the other phases are completed. Experience indicates that when very little analysis and design work is done, programmers spend a significant part of their time completing the design instead of actually developing the system routines $[13]$ . The resultant effect is an inverse relationship between planning (i.e., analysis and design) and building (i.e., coding)

with respect to resource consumption.

Tradeoffs of an inverse nature between phases carry through the development process. Arguments can be established for coding-testing interactions as well as for testing-implementing interactions. In essence, the interaction phenomenon reduces to a “ripple” effect. The insufficient allocation of resources to any single phase of development creates an extra burden for the subsequent phase(s). This view makes the implicit assumption that the development of a particular application system constitutes a relatively fixed task such that failure to attend to a portion of the task merely postpones that effort until some future time.

The interactions inherent in the development process are not necessarily restricted to adjacent phases. Insufficient design effort may not be realized until the system is undergoing testing or implementation. In fact, inadequacies in the design of a system may escape detection until the system is in full operation, only then to be deluged by problems traceable to failure in the design step. Compelling evidence by Boehm [6] has demonstrated how the cost of correcting an error grows out of all proportion the later in the system development life cycle it is detected.

## 4. A Model of Inter-Phase Relationships

Phases within the system development process are thought to vary inversely. The mathematical form of the hypothesized model of interaction is: $X_{j} = aX_{i}^{-b}$ ,

where $X =$ effort (manhours); $i, j =$ phases; and $a, b =$ real-valued constants.

The effort consumed by phase j (denoted by $X_{j}$ ) is related to the effort consumed by a previous phase i (denoted by $X_{i}$ ) according to the inverse relationship specified. The general form of the model, which was suggested elsewhere [13,23], is depicted in Figure 1. This form of model was chosen because its properties (monotonic decreasing and asymptotic to both axes) represent the hypothesized inter-phase relationships. With this model, b can be interpreted as an elasticity coefficient. That is, a one percent increase in activity i is associated with a b percent decrease in activity j.

Phases may be entered into the model individually or in combination with other phases. Analysis and design, for instance, represent different activities but they are both part of the planning function. The model to examine the relationship between design and analysis would be $X_{D} = aX_{A}^{-b}$ . The model to examine the relationship between testing and the combined phases of analysis plus design would be $X_{T} = aX_{AD}^{-b}$ . The constants in the models (i.e., a and b) apply to specific pairs of life cycle phases.

![](/api/attachments/VRNFPHKB/fulltext/images/ce48176d26f9fefcb4d8599ed581915976e4bdf47ff77e7f54909b98d5647dc3.jpg)  
Fig. 1. General Form of the Model.

Whether phases are entered into the model in combination or individually, the general form of the model is not altered. The manner in which phases are combined, however, does differ depending on the assumptions concerning the nature of interaction. These assumptions provide the distinguishing element between two model variations – an additive effects model and a multiplicative effects model. These model variations differ only in their treatment of combined phases and both fall within the general structure of the original $X_{j}=aX_{i}^{-b}$ model.

The additive effects model assumes that phases are counterbalancing. That is, an insufficient effort in one phase can be compensated for by an increased effort in another phase of development. In order to predict the effort necessary for a future phase of development, it is only necessary to know the effort already expended on the previous phases. This model is expressed as

$$
X _ {j} = a \left(X _ {i} + X _ {i + 1} + \dots + X _ {j - 1}\right) ^ {- b}.
$$

While the assumptions of the additive effects model are that phases of development are compensatory, the multiplicative effects model assumes that phases are “non-forgiving”. This means that an inadequate effort devoted to design, for example, cannot be entirely compensated for by increased effort during coding. Rather, its effect will carry through to testing and implementation. A further argument can be made that postponement of certain portions of the overall development task will have deleterious effects on the resultant outcome of development. That is to say, failure to resolve specific developmental issues at the appropriate time may never be completely rectified by their postponed resolution. As an example, Ginzberg [12] has shown that failure to address key developmental issues during the analysis phase fosters unrealistic user expectations which lead to eventual user dissatisfaction with the system. The form of this model is:

$$
X _ {j} = a \left(X _ {i} \cdot X _ {i + 1} \cdot \dots \cdot X _ {j - 1}\right) ^ {\dots b}.
$$

## 5. An Empirical Evaluation of the Model

A study was undertaken to examine the model's descriptive ability and the appropriateness of its general structure as a representation of the interphase relationships within the systems development life cycle. Thirty-two application systems were randomly selected from five different organizations (two manufacturing firms, a merchandising firm, a life insurance firm, and a leasing and rental agency). The selection was made by the researcher with no prior knowledge of the nature of the system, the development personnel or users involved with the system, or the status or quality of the system. The sample systems were selected from a much larger set of “qualified systems.” Systems qualified for inclusion in the study if they were developed

(1) by internal systems personnel,

(2) for users outside the systems department

(3) in support of a particular business function,

(4) completed within the last year, and

(5) passed through multiple phases of development.

This selection mechanism served to exclude systems software, such as operating systems, utilities, or general support programs, as well as “minor maintenance" projects which tend to involve only one or two phases of development. All systems had reached the stage of being installed; some had been successfully incorporated into their organizations while others had never been used. Some of these systems, for example, were of a managerial control nature, such as inventory reporting and sales analysis. Other systems supported planning functions involving data collection and forecasting models. Many of the systems simply automated existing activities, such as record keeping functions. The required manhours to develop these application systems ranged from 100 to 6000 hours approximately.

The actual time spent by systems personnel in the development of each of these systems, as extracted from the project management reporting systems used by each organization, was allocated among five life cycle phases [17]:

Analysis - all initial work through complete functional requirements (i.e., "what the system will do").

Design - the translation of functional requirements into complete system specifications (i.e., "how the system will do it").

Coding - the preparation of programming instructions including unit testing and program documentation.

Testing - activity to ensure the system operates in accordance with the specifications established during analysis and design (i.e., "system testing").

Implement activity which places the system into full operation within the organizational setting including user training and the development of procedure manuals. The term “implement” was chosen because of its wide acceptance by practitioners. This term is not to be confused with “implementation” which typically denotes the overall process of effecting change in organizations.

## 6. The Results

In all cases, the effort consumed by each phase was expressed as a percentage of the total development effort for the system. This approach normalizes the data in order to isolate the relationships of interest. Any simplistic attempt to correlate design effort with coding effort, for instance, without adjusting for system size would almost invariably result in a positive correlation because total resource requirements tend to increase with the size of the system.

Table 1 contains the result of the model when applied to individual interacting phases. The coefficients of determination $(r^{2})$ , the significance level of the relationships, the number of systems $(N)$ , and the F values are reported. The final form of the model is also presented in those cases where the p-value is less than one percent.

According to the postulated “ripple effect”, interactions should be present between adjacent phases. The results indicate a significant relationship between analysis and design, no apparent relationship between design and coding, a strong relationship between coding and testing, and no apparent relationship between testing and implementing. It was postulated that the effects may skip phases. Here there is evidence of a strong relationship between analysis and coding and between coding and implementing. Two definite patterns of interaction emerge: A → C → T and A → C → I. Nineteen percent of the variation in effort consumption during coding is explained by its relationship with analysis; 31 percent of the variation in effort consumption during testing is explained by its association with coding; and 22 percent of the variation in effort consumed by implementing is explained by its relationship with coding.

The results of the analysis of the interaction effects among combined phases are presented in Table 2. The combination of phases yields many significant relationships, but for the most part, these relationships seem to reinforce the dominant patterns found in Table 1.

The effects of the design phase are interesting. The combination of design with analysis adds greatly to the explanatory power of the model. For instance, the relationship between analysis and coding explains 19 percent of the variation in effort consumed by coding (Table 1) while the combination of analysis plus design explains 39 percent of the coding effort (Table 2). In contrast, the combination of the design phase with coding detracts from the explanatory power of the model. Since analysis and design are both part of the planning function (as opposed to coding which is part of the building function), their combination may simply be more appropriate than the combination of design and coding.

Table 1  
Interaction Between Individual Life Cycle Phases

<table><tr><td>Interacting Phases</td><td> $r^{2}$  (significance)</td><td>F Value</td><td>Resulting Model</td></tr><tr><td>A -&gt; D</td><td>.20 (.013)*</td><td>7.169</td><td></td></tr><tr><td>A ----&gt; C</td><td>.19 (.007)**</td><td>8.375</td><td> $X_{C} = 97.25X_{A}^{-.33}$ </td></tr><tr><td>A ----&gt; T</td><td>.00 (.841)</td><td>0.041</td><td></td></tr><tr><td>A ----&gt; I</td><td>.00 (.341)</td><td>0.938</td><td></td></tr><tr><td>D -&gt;C</td><td>.02 (.239)</td><td>1.456</td><td></td></tr><tr><td>D ----&gt;T</td><td>.00 (.588)</td><td>0.301</td><td></td></tr><tr><td>D ----&gt; I</td><td>.00 (.761)</td><td>0.095</td><td></td></tr><tr><td>C -&gt;T</td><td>.31 (.001)**</td><td>13.936</td><td> $X_{T} = 259.70X_{C}^{-.91}$ </td></tr><tr><td>C ----&gt;I</td><td>.22 (.007)**</td><td>8.712</td><td> $X_{I} = 261.33X_{C}^{-.98}$ </td></tr><tr><td>T -&gt;I</td><td>.00 (.438)</td><td>0.623</td><td></td></tr></table>

Notes:

```txt
1. A = analysis, D = design, C = code, T = test, I = implement
```  
2.\* denotes significance at 5 percent level  
\*\* denotes significance at 1 percent level  
3. All $r^{2}$ values have been adjusted for degrees of freedom.

```txt
4. N is not always 32. Any system spending zero effort in one of the interacting phases had to be omitted from that particular analysis.
```

## Table 2

Interaction Between Combined Life Cycle Phases

<table><tr><td> $Interacting Phases^1$ </td><td> $r^2 (significance)$ </td><td>F Value</td><td>Resulting Model</td></tr><tr><td>A -&gt;D + C</td><td>.36 (.000)**</td><td>18.390</td><td> $X_{DC} = 124.08 \times_{A}^{-.29}$ </td></tr><tr><td>A ---&gt; C + T</td><td>.25 (.002)**</td><td>11.198</td><td> $X_{CT} = 95.19 \times_{A}^{-.21}$ </td></tr><tr><td>A ----&gt; T + I</td><td>.00 (.410)</td><td>0.698</td><td></td></tr><tr><td>A + D -&gt;C</td><td>.39 (.000)**</td><td>20.722</td><td> $X_{C} = 428.42 \times_{AD}^{-.69}$ </td></tr><tr><td>A + D ----&gt;T</td><td>.13 (.028)*</td><td>5.355</td><td></td></tr><tr><td>A + D ----&gt; I</td><td>.00 (.965)</td><td>0.002</td><td></td></tr><tr><td>A + D -&gt;C + T</td><td>.45 (.000)**</td><td>26.055</td><td> $X_{CT} = 229.55 \times_{AD}^{-.42}$ </td></tr><tr><td>A + D ----&gt; T + I</td><td>.00 (.403)</td><td>0.718</td><td></td></tr><tr><td>D -&gt;C + T</td><td>.00 (.594)</td><td>0.292</td><td></td></tr><tr><td>D ----&gt; T + I</td><td>.23 (.003)**</td><td>10.174</td><td> $X_{TI} = 179.08 \times_{D}^{-.48}$ </td></tr><tr><td>D + C -&gt;T</td><td>.16 (.016)*</td><td>6.601</td><td></td></tr><tr><td>D + C ----&gt; I</td><td>.15 (.022)*</td><td>5.902</td><td></td></tr><tr><td>D + C -&gt;T + I</td><td>.00 (.301)</td><td>1.107</td><td></td></tr><tr><td>C -&gt;T + I</td><td>.00 (.459)</td><td>0.564</td><td></td></tr><tr><td>C + T -&gt;I</td><td>.25 (.004)**</td><td>10.259</td><td> $X_{I} = 11028.97 \times_{CT}^{-1.85}$ </td></tr></table>

1. A = analysis, D = design, C = code, T = test, I = implement  
2. \* denotes significance at 5 percent  
\*\* denotes significance at 1 percent level  
3. all $r^{2}$ values have been adjusted for degrees of freedom.  
4. N is not always 32. Any system spending zero effort in one of the interacting phases had to be omitted from that particular analysis.

The analysis of individual interacting phases (Table 1) found the design phase to be relatively independent of the other phases in the development life cycle. The results of Table 2 clarify the impact of design within the system development life cycle. The relationship between design and the combined phases of testing plus implementing is significant at the 0.003 level. It appears that the design phase exhibits a definite influence which bypasses the coding phase and impacts the testing and implementing phases of development.

As indicated earlier, the manner in which phases are combined depends on the assumptions one is willing to make concerning the nature of the inter-phase tradeoffs. The two hypothesized sets of assumptions result in two different model forms – the additive effects model and the multiplicative effects model. The results of fitting these models to the study sample are presented in Tables 3 and 4. With the last model in each of Tables 3 and 4, the analysis phase is omitted to escape from the constraint of effort consumption summing to 100 percent.

The explanatory power of the additive effects model is greatest when forecasting the effort consumed by the coding and testing phases. Its ability to forecast the effort to implement is reduced. The multiplicative effects model is also at its best when forecasting the coding and testing levels of resource consumption. Forty-six percent of the variation in the effort consumed by the testing phase can be explained by its relationship with the phases of analysis, design, and coding when combined multiplicatively.

The purpose for analyzing the additive versus multiplicative effects models is to determine the specific nature of the interaction effects which have been demonstrated in Tables 1 and 2. Unfortunately, the results of a comparison of the additive model (Table 3) and the multiplicative model (Table 4) are inconclusive. Neither model consistently outperforms the other. Had one model demonstrated a superiority over the other, an argument could be made that the assumptions embedded within the dominant model were a better representation of the true nature of the inter-phase relationships. This not being the case, no such claim can be made. Reasons for the inconclusive results can be postulated. First, neither set of assumptions may capture the underlying characteristics of the interactions. Second, perhaps the multiplicative effects model applies to certain phases of development while the additive effects model applies to other phases of development yielding a “combined effects” model. Further comments are presented later.

## 7. Validation of Results

Two aspects of model validation were explored; a test of the predictive power of the model, and a test of the aptness of the model [10]. The former test was made by an examination of the measures of correlation resulting from the application of the model to the data. These measures were examined from the standpoint of absolute magnitude and of statistical significance. The coefficients of determination, their associated level of significance, and $F$ values were reported for all models of inter-phase relationships (Tables 1-4). All model fitting and testing was performed using SAS [22].

The test concerning the aptness of the models was conducted by means of residual analysis. Distributions of the residuals were analyzed for each of the models presented in Tables 1–4. Four prop-

Table 3  
Inter-Phase Relationships with Additive Effects Model

<table><tr><td>Interacting Phases</td><td colspan="2"> $r^2$  (significance) F Value</td><td>Resulting Model</td></tr><tr><td>A → D</td><td>.20(.013)*</td><td>7.169</td><td> $X_D = 31.95 X_A^{-.22}$ </td></tr><tr><td>A + D → C</td><td>.39(.000)**</td><td>20.722</td><td> $X_C = 428.42 (X_A + X_D)^{-.69}$ </td></tr><tr><td>A + D + C → T</td><td>.39(.000)**</td><td>19.611</td><td> $X_T = 15920107.65 (X_A + X_D + X_C)^{-3.30}$ </td></tr><tr><td>D + C + T → I</td><td>.12(.036)*</td><td>4.866</td><td> $X_I = 13960.73 (X_D + X_C + X_T) - 1.80$ </td></tr></table>

Inter-Phase Relationships with Multiplicative Effects Model

<table><tr><td>Interacting Phases</td><td> $r^2$  (significance)</td><td>F Value</td><td>Resulting Model</td></tr><tr><td>A → D</td><td>.20(.013)*</td><td>7.169</td><td> $X_D = 31.95 X_A^{-.22}$ </td></tr><tr><td>A + D → C</td><td>.26(.004)**</td><td>9.922</td><td> $X_C = 351.57 (X_A.X_D)^{-.41}$ </td></tr><tr><td>A + D + C → T</td><td>.46(.000)**</td><td>12.590</td><td> $X_T = 319.20 (X_A.X_D.X_C)^{-.36}$ </td></tr><tr><td>D + C + T → I</td><td>.00(.323)</td><td>1.025</td><td></td></tr></table>

Notes: 1. A = analysis, D = design, C = code, T = test, I = implement  
2. \* denotes significance at 5 percent level  
\*\* denotes significance at 1 percent level  
3. All $r^{2}$ values have been adjusted for degrees of freedom.  
4. N is not always 32. Any system spending zero effort in one of the interacting phases had to be omitted from that particular analysis.

erties of each model were examined: (1) the linearity of the transformed regression function, (2) the constancy of the error variance, (3) the absence of significant outliers, and (4) the normality of the error terms. The first three of these properties were easily verified by a visual inspection of the distribution of the standardized residuals. The fourth property was examined by comparing a histogram of the residuals with a Normal histogram looking for gross departures. Any structural inadequacies of the models would be revealed by a regular pattern on the residual plots or by the existence of significant outliers. In the case of each model, no severe violations of any of the above-mentioned properties were found. It can therefore be concluded that the general structure of the $X_{j}=aX_{i}^{-b}$ model is an appropriate representation of the tradeoffs between the phases of development.

Correlation Coefficients Among Life Cycle Phases (N = 32)

<table><tr><td></td><td>A</td><td>D</td><td>C</td><td>T</td><td>I</td><td>AD</td><td>DC</td><td>CT</td><td>TI</td></tr><tr><td>A</td><td>1.00000(0.0000)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D</td><td>-0.33562(0.0604)</td><td>1.00000(0.00000)</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>-0.45709(0.0216)</td><td>-0.37368*(0.0351)</td><td>1.00000(0.0000)</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>T</td><td>0.06529(0.7226)</td><td>0.27245(0.1314)</td><td>-0.66119*(0.0001)</td><td>1.00000(0.0000)</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>I</td><td>-0.13441(0.4633)</td><td>0.01986(0.9141)</td><td>-0.41864(0.0171)</td><td>0.10042(0.5845)</td><td>1.00000(0.0000)</td><td></td><td></td><td></td><td></td></tr><tr><td>AD</td><td>0.76397(0.0001)</td><td>0.35143(0.0486)</td><td>-0.58418(0.0009)</td><td>0.25151(0.1649)</td><td>-0.11998(0.5131)</td><td>1.00000(0.0000)</td><td></td><td></td><td></td></tr><tr><td>DC</td><td>-0.70011*(0.0001)</td><td>0.10608(0.5634)</td><td>0.88267(0.0001)</td><td>-0.28260(0.1235)</td><td>-0.41781(0.0193)</td><td>-0.62315(0.0001)</td><td>1.00000(0.0000)</td><td></td><td></td></tr><tr><td>CT</td><td>-0.59559*(0.0003)</td><td>-0.32425(0.0702)</td><td>0.90605(0.0001)</td><td>-0.28160(0.1184)</td><td>-0.47880(0.0056)</td><td>-0.81404*(0.0001)</td><td>0.80701(0.0001)</td><td>1.00000(0.0000)</td><td></td></tr><tr><td>TI</td><td>-0.01533(0.9336)</td><td>-0.22542(0.2148)</td><td>0.02523(0.8910)</td><td>-0.01556(0.9326)</td><td>0.21878(0.2290)</td><td>-0.16964(0.3533)</td><td>-0.08717(0.6352)</td><td>0.02349(0.8984)</td><td>1.00000(0.0000)</td></tr></table>

\* Correlation coefficient for inverse linear model exceeds that for inverse curvilinear model.

An inverse linear model was also fitted to the sample data. This simple model provides an alternate explanation and its comparison with the results of the curvilinear model constitutes an additional degree of validation. A correlation matrix of the results is shown in Table 5. By squaring each correlation coefficient in Table 5, comparisons can be made between the linear models and the curvilinear models (Tables 1 and 2). Of the twenty five models presented in Tables 1 and 2, the curvilinear model demonstrates a stronger relationship in all but five instances. These results support the proposed $X_{i} = aX_{i}^{-b}$ model.

An important means of validation, quite apart from the statistical sense, involves searching for other potential causes or explanations for the observed results. A separate analysis by McKeen [17] correlated 23 different factors with the levels of resource consumption by phase. These factors, which measured inherent attributes of the systems and characteristics of the environments in which the systems were developed, were found incapable of explaining the variation present in the patterns of resource consumption. This evidence corroborates the assertion that these inter-phase relationships do in fact constitute a valid expression of the tradeoffs between the phases of the development process rather than simply reflecting inherent characteristics of systems or their environments.

## 8. Implications and Limitations of the Results

This research has proceeded from the premise that the inter-phase relationships occurring within the systems development life-cycle constitute determinant factors in the consumption of resources. Consideration of the nature of these relationships places the focus on the process of systems development. The assumption implicit in the majority of previous efforts to obtain reliable estimates of systems development costs has been that life cycle cost is predictable using variables that simply describe the system and the development environment [3]. The presence and extent of these demonstrated tradeoffs among life cycle phases leads one to question this assumption. Although all these factors are relevant, a significant part of the resource requirements for any one phase results from the manner in which other phases are completed; it is the process of development which largely determines the pattern of resource consumption and the eventual outcome. By neglecting to incorporate these relationships within cost estimation models of systems development, researchers and practitioners overlook a dominant source of explanatory power.

In addition, the explication of these inter-phase models enables an economic analysis of the systems development process. The manpower resources consumed by systems development are not uniformly valued over the entire process. Typically, a senior analyst is involved in the initial stages of development (analysis and design) but rarely does this same analyst perform the coding functions. By associating costs with project personnel, it is a straightforward exercise to use the inter-phase models developed by this research to provide “optimal” levels for resource consumption during the various development phases. For example, the relationship between the combined phases of analysis plus design and coding was best represented by the model

$$
X _ {\mathrm{C}} = 4 2 8. 4 2 \left(X _ {\mathrm{A}} + X _ {\mathrm{D}}\right) ^ {- 0. 6 9}.
$$

Since this is an inverse, curvilinear function, a point on the curve will be reached at which the increase in effort devoted to analysis plus design would not be sufficient to justify (economically) the associated decrease in coding effort. By extending this approach, an organization could “optimize” its effort consumption over the development life cycle of its application systems to provide economic guidelines for system developers.

The missing piece in the analysis of inter-phase tradeoffs may be the operations/maintenance phase of the development life cycle. It is possible (and perhaps likely) that deficiencies in the development process may lay dormant until after installation only to plague the system during its productive life time. The impact of an inadequate design effort may not be fully realized until the system becomes truly operative. Unfortunately, accurate information regarding the performance of the sample application systems after their introduction into the business environment was not obtainable by the author. Many factors dictate against its general availability. It is well-known that organizations “develop systems but maintain programs”, making attempts to bridge the gap extremely difficult. The inclusion of resource consumption data pertaining to this maintenance phase would promote a fruitful avenue for future research by explicating the relationships and impacts of various development phases over the full life cycle of application systems [15].

The comparison of the additive effects model with the multiplicative effects model was inconclusive. This research was unable to demonstrate any real difference with respect to the applicability of these model variations. Reasons for the inability to make unequivocal statements regarding the preeminence of either type were postulated. Despite the results, it is believed by the author that the effects of resource levels devoted to phases of the development life cycle should not be additive. Certainly the ability to predict the resources to be consumed during the coding phase should be enhanced by a knowledge of the levels of resource consumption by analysis and by design rather than just a knowledge of the aggregate level of resource consumption by all previous phases. Further, it is not likely that an inadequate design effort can be compensated for by additional effort at a later stage. The multiplicative effects model demonstrated superior explanatory power over the additive effects model only when forecasting the effort consumed by the testing phase (Table 4). It may be that the effects of the design phase which bypass the coding phase to impact subsequent phases of development (including the testing phase) are governed by the assumptions of the multiplicative model.

This research broke with tradition somewhat by excluding a “time” variable in the models. This was not an oversight. In previous research $[16]$ , the inclusion of the time dimension was found to be very misleading in an explanatory sense. By managerial override, people are added to projects and taken away from projects. Analysts often work on more than one project switching their attention back and forth. This activity distracts the development picture when you look at it over time. The best data appears to be development hours which cannot be manipulated. This research focussed on individual phases and their consumption of effort. It did not address the overlapping of phases nor manpower loading over “real” time.

Finally, much of our current “software problem” is one of management and control. The common managerial tasks of resource allocation, development life cycle planning and control, project and personnel administration, and effective personnel staffing and directing all contribute to the overall problem. These explanatory models which promote a better understanding of the inter-phase relationships in systems development should provide a basis for improving the management and control of the development process. Better estimation is at the heart of this management control function.

## References

[1] T.K. Abdel-Hamid, and S.E. Madnick, "A Model of Software Project Management Dynamics", The Sixth International Computer Software and Applications Conference (COMPSAC), November 8–12, 1982.

[2] T.K. Abdel-Hamid, and S.E. Madnick, “The Dynamics of Software Project Scheduling”, CACM, Vol. 26, No. 5, May 1983, pp. 340–346.

[3] I. Benbasat, and I. Vessey, “Programmer and Analyst Time/Cost Estimation”, MIS Quarterly, Volume 4, Number 2, June 1980, pp. 31–43.

[4] R.I. Benjamin, Control of the Information System Development Cycle, Wiley Interscience, a division of John Wiley & Sons, Inc., New York, N.Y., 1971.

[5] T.R. Berrisford, and J.C. Wetherbe, “Heuristic Development: A Redesign of System Design,” MIS Quarterly, Volume 3, Number 1, March 1979, pp. 11–19.

[6] B. Boehm, "Software Engineering," IEEE Transactions on Computers, Volume C-25, December, 1976, pp. 136–145.

[7] G.B. Davis, Management Information Systems: Conceptual Foundations, Structure and Development, McGraw-Hill, Inc., New York, N.Y., 1974.

[8] T. DeMarco, Structured Analysis and System Specification, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1979.

[9] W.S. Donelson, “Project Planning and Control,” Datamation, June 1976, pp. 73–80.

[10] R. Dubin, “Theory and Research,” Chapter 3 in The Organization, Management, and Tactics of Social Research (Richard O'Toole, ed.), Schenkman Publ. Co., Inc., 1971, pp. 57–74.

[11] C. Gane, and T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Inc., New Jersey, 1979.

[12] M.J. Ginzberg, “Early Diagnosis of MIS Implementation Failure,” Management Sciences, Volume 27, Number 4, April 1981, pp. 459–478.

[13] C.A. Graver, E.E. Balkovich, W.M. Carriere, and R. Thibodeau, Cost Reporting Elements and Activity Cost Tradeoffs for Defense System Software, General Research Corporation, Final Report No. CR-1-721, 1977.

[14] R.C. Gunther, Management Methodology for Software Product Engineering, Wiley-Interscience Publications, John Wiley & Sons, New York, 1978.

[15] W.R. King and A. Srinivasan, “Integrating Information Systems into the Organization: The Evolution of the Systems Life Cycle,” Applications of Management Science, Schultz, R., ed., Volume 3, JAI Press, 1983.

[16] J.D. McKeen, “An Empirical Investigation of the Process and Product of Application System Development,” Ph.D. dissertation, Graduate School of Business Administration, University of Minnesota, 1981.

[17] J.D. McKeen, “Successful Development Strategies for Business Application Systems,” MIS Quarterly, Volume 7, Number 3, September 1983, pp. 47–65.

[18] J.D. Naumann, and A.M. Jenkins, “Prototyping: The New Paradigm for Systems Development,” MIS Quarterly, Volume 6, Number 3, September 1982, pp. 29–44.

[19] P.V. Norden, “On the Anatomy of Development Projects”, IRE Trans. PGEM, Vol. EM-7, No. 1, 1960, p. 41.

[20] L.H. Putnam, "A General Empirical Solution to the Macro Software Sizing and Estimating Problem", IEEE Transactions on Software Engineering, Vol. SE-4, No. 4, July 1978, pp. 345–361.

[21] L.H. Putnam, "Software Cost Estimation and Life Cycle Control: Getting the Software Numbers", IEEE Computer Society, IEEE Catalog No. EHO 165-1, 1980.

[22] SAS User's Guide: Statistics, SAS Institute Inc., (Ray. A.A. ed.), Cary, N.C., 1982.

[23] R. Thibodeau, and E.N. Dodson, “The Implications of Life Cycle Phase Interrelationships for Software Cost Estimating,” Software Life Cycle Management Workshop, Atlanta (1978), pp. 70–74.

[24] R. Thibodeau, and E.N. Dodson, "Life Cycle Phase Interrelationships," The Journal of Systems and Software, Volume 1, Number 3, 1980, pp. 203-211.

[25] E. Yourdon, Managing the Structured Life Cycle: A Software Development Methodology Overview, Prentice-Hall, New Jersey, 1982.

[26] E. Yourdon, and L.L. Constantine, Structured Design: Fundamentals of a Discipline of Computer Program and Systems Design, Prentice-Hall, Inc., New Jersey, 1979.

[27] R.W. Zmud, "Management of Large Software Development Efforts," MIS Quarterly, Volume 4, Number 2, June 1980, pp. 45–55.
