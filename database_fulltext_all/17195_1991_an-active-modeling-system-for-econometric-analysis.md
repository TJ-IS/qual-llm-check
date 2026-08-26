---
otero_id: 17195
otero_key: "F8VT9UB7"
title: "An active modeling system for econometric analysis"
authors: "Daniel R. Dolk; Donald J. Kridel"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90061-f"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An active modeling system for econometric analysis

Daniel R. Dolk

Naval Postgraduate School, Monterey, CA 93943, USA

Donald J. Kridel

Southwestern Bell Corporation, St. Louis, MO 63101, USA

This paper examines the feasibility of developing an “artificially intelligent econometrician” as an active decision support system (ADSS) in the sense articulated by [Manheim, 1988]. We review the system components of an ADSS and then relate them to a modeling system for econometric analysis that we have implemented. We present the query language of the PERM (Progressive EconometRic Modeling) system and offer an extension to the language based on process-oriented constructs for model integration. The query language and its extension correspond to the ADSS’s user-directed and computer-directed process managers, respectively. Schemas representing statistical strategies are stored as processes in the extended language and serve as the econometric knowledge base. We suggest an approach to building an inference processor for this system based on experiments to record user query protocols and relate them to the schemas in the knowledge base. The connection between user processes and schemas is implemented by demon constructs in the extended language. Finally, we examine the extent to which our proposed system constitutes an ADSS.

Keywords: Active DSS, Econometric modeling, Model control language, Schema, Process manager, Inference processor, Demon.

## 1. Introduction

Manheim [1988] introduces the concept of an “active” DSS wherein the computer and user work as partners in the problem-solving process. The active DSS (ADSS) is particularly interesting because it relies more on ideas from cognitive science than organizational behavior [Keen and Scott Morton, 1978] or system design [Sprague and Carlson, 1982]. Manheim presents a number of research issues including the feasibility, design, and utility of an ADSS which we intend to examine as the basis for developing an intelligent modeling system for econometric analysis.

Remus and Kottemann [1986] provide a convincing argument for statistical analysis as a fertile domain for expert systems applications. Their “artificially intelligent statistician” (AIS) augments the cognitive limitations of decision-makers by identifying and executing sound statistical strategies which the user may not otherwise be aware of, and thus unwittingly violate. Our experience with a conventional modeling system we’ve developed for econometric forecasting in the telecommunications industry reinforces the desirability of this kind of support for econometric analysis. In econometrics there is a plethora of continually evolving estimation techniques, only a fraction of which the average user can be expected to know. On the other hand, as the discipline grows, so does the body of knowledge concerning acceptable strategies for employing these techniques.

Our objective in this paper is to lay the groundwork for an “artificially intelligent econometrician” based on Manheim’s concept of an active DSS (ADSS). We start by reviewing the concepts and architectural components of an ADSS in Section 2. In subsequent sections, we develop constructs for each of the various components. These constructs comprise a mixture of the concrete and the abstract, starting in Section 3 with a specific example of a model manipulation language for econometric analysis which we've developed for the PERM (Progressive Econometric Modeling) system. In Section 4, we present an extension to this language which serves as a model integration control language for synchronizing processes [Kottemann and Dolk, 1988]. We discuss the difficulties inherent in econometric modeling and suggest the control language as a vehicle for capturing proper modeling strategies. The model manipulation language and its extension correspond to Manheim's user-directed and computer-directed process managers, respectively. Finally, we suggest an approach for developing an inference processor to associate user protocols with stored strategy schemas.

The primary contribution of this paper is the specification of components of a model manipulation language for econometric analysis which not only extend the features of conventional modeling systems but also provide a possible migration path to more powerful ADSS.

## 2. Active decision support systems

Manheim presents the notion of an active DSS as “a DSS which can usefully do more than what its users explicitly direct it to do”, but which requires a “system design based on an explicit model of human problem-working processes” [Manheim, 1988]. The ADSS concept differs from conventional DSS approaches in that it is learning-based and therefore more in the context of cognitive science rather than system design [Sprague and Carlson, 1982] or organizational behavior [Keen and Scott Morton, 1978].

The system architecture for an ADSS consists of three main components: process managers, history processor, and display interfaces. Since DSS's ostensibly support the process of decision-making (or problem-working), process managers are fundamental components of the architecture. Specifically, there are two kinds of process managers: user-directed (UDPM) and computer-directed (CDPM). The UDPM activates resident processes in response to commands issued directly by the user (e.g., a query processor to do data retrieval, or matrix manipulation routines to perform an ordinary least squares estimation). The CDPM, on the other hand, activates processes in response to commands issued by the history processor as it attempts to provide active support. Thus, the CDPM may invoke a particular, predefined regression estimation decision tree once it determines that the user really wants to perform this kind of analysis.

The history processor consists of two parts: a history recorder which simply journals user inputs and the resultant outputs in a history record, and a history inference processor (HIP) which attempts to identify or build a model of the user's image of the problem from the history record.

Finally there are display interfaces which allow the user to activate the UDPM, and which filter the various outputs of the system.

The system is structured as shown in fig. 1 and works roughly as follows:

(1) The user initiates action via some kind of command medium (a language, menu selection, mouse, etc.).

![](/api/attachments/F8VT9UB7/fulltext/images/e98d5ddbe63867e6eadafa5ec26c8265dae7c43a8a604e7888866a88ecc49c00.jpg)  
(Note: Dotted lines indicate data flow; Solid lines indicate process flow.)  
Fig. 1. ADSS Design Architecture.

(2) The UDPM activates one or more processes (e.g., regression routine) to satisfy the action command.

(3) The history recorder logs the command and resultant output in the history record.

(4) The inference processor scans the history record and attempts to create a model of the user problem-working process either deductively by pattern-matching with a library of existing model templates (schemas), or inductively by some form of dynamic pattern recognition.

(5) Once the inference processor identifies a model, it passes control to the CDPM which invokes the processes associated with the model. If no model can be identified, control is returned to the user along with the user-directed process output.

(6) The CDPM returns the user-directed and computer-directed process output to the user after executing its requisite processes.

The key ingredient in this scenario is the history inference processor which is based on a model of human problem-working processes. Manheim suggests a general processing model which is reminiscent of neural networks. The model consists of a hierarchical network of schemas which form concepts. Schemas can be classified as template schemas which are similar to frames, procedural schemas which provide action sequences similar to plans, and mixed schemas which are combinations of the two. Problem-working consists of activation of schemas, under the direction of some higher level control logic, itself a schema.

The challenging part of an ADSS is building a computer model which emulates the above model. This involves the following steps:

(1) Construction of a schematic network from an evolving library of schemas. This involves the continual modification and addition of schemas as well as changes to the connectivity of the schemas.

(2) Operation of the schematic network to formulate hypotheses about the user, the problem, and the relevant problem-working processes.

(3) Testing of the hypotheses through the equivalent of simulation modeling.

The construction and evolution of a schema library is critical to the successful implementation of an ADSS. This can be built from a number of sources:

(1) Protocol analysis which tries to identify actual thought processes empirically.

(2) Predefined schemas derived from conventional wisdom or heuristics in much the same way expert system knowledge bases are created today.

(3) Pattern recognition, or script recognition, derived from a dynamic analysis of the history record.

The implementation of an ADSS raises many practical questions which are not addressed in Manheim's original proposal (see Manheim [1989] for a treatment of these issues). In many respects, an ADSS has more in common with the neural network approach to cognitive science [Rumelhart and McLelland, 1986] than with standard expert, or decision support, system technology. There are places, however, where current DSS design architecture can be adapted to begin investigating ADSS. In the remaining sections, we attempt to build a bridge to an ADSS for econometric modeling that works from the architecture of an existing conventional modeling system.

## 3. PERM: A modeling system for econometric analysis

Our objective is to build an active modeling system which provides some intelligent support to the modeler. Specifically we are interested in helping modelers use econometric estimation techniques properly. Another way of looking at this is that we are attempting to build an expert system which simulates the knowledge of an expert in econometrics. Our approach is to use the concepts of an ADSS as a way to build this system. As a result, we use the terms “active modeling system”, “expert system”, and “ADSS” interchangeably throughout the remaining discussion. Further, we use the term “conventional” in juxtaposition with “active” to denote systems which don’t provide intelligent support. We begin by describing a conventional modeling system based on the econometric modeling life cycle.

![](/api/attachments/F8VT9UB7/fulltext/images/7fa2ea81ddb777218aa8612168fe023d6d4f8014750ec48173d0e923df5b1ffe.jpg)  
Fig. 2. Life Cycle of Econometric Modeling Process.

## 3.1. Econometric modeling life cycle

A simple econometric modeling life cycle for forecasting models is shown in fig. 2.

For many econometric applications significant economic theorizing may well precede the “empirical” steps outlined in fig. 2. Furthermore, depending on the “type” of econometric analysis to be performed, this life cycle may be further simplified, e.g., if the aim of the econometric exercise is to estimate elasticities of demand, then the life cycle is restricted to the data collection and econometric analysis phases.

Data collection, storage and manipulation is the most basic of tasks and logically precedes any empirical analysis. Collection and storage require little in the way of clarifying comments. Data manipulation, however, can be an important element in the life cycle. Since economic theory provides little guidance with respect to the selection of “functional form”, many alternative specifications will typically be tested, e.g., does SALES depend on INCOME, the square of INCOME, or the log of INCOME. These specification searches require that alternative forms of the data-series be easily calculated and retrieved. Updating and scaling of data-series is necessary as well.

Econometric analysis is comprised of a wide variety of separately identifiable tasks and techniques. The primary goal of this stage of the life cycle is parameter estimation. The different techniques that facilitate coefficient estimation will be described in more detail in the next section. Prior to estimation some preliminary data analysis should be performed. This data analysis will typically include checking the distributional properties of variables and systematically checking for obvious outliers in the data. Statistical as well as informal testing should also be employed at this stage of the life cycle; for example, verifying that coefficient estimates are statistically significant and that these parameter estimates are broadly consistent with existing experience. Lastly, some form of residual analysis or diagnostics should be performed.

Model building in its simplest form is nothing more than “saving” coefficient estimates in a form that allows simulation for forecasting or what-if sensitivity analysis. For more complicated simultaneous models, there may be model-closing identities, adjustment constants, or other complicating factors.

Model simulation is the process of solving the model for specific purposes, e.g., forecasting. The particular solution process will depend on the desired application. For example, forecasting may require different solution techniques than model testing.

The testing phase of the simulation process is also application dependent. While this will almost certainly include some informal comparison of actual and predicted values, there may also be comparisons with other models, evaluation of forecasts in different economic circumstances (boom vs. bust), and impact multiplier calculations. Which of these are performed and how the results are weighted in the evaluation process will depend on the end-user application.

As more data or experience become available, all previous steps will be repeated in the model maintenance phase. For example, as new data become available, the data-series will require updating, regressions will be re-estimated to include the additional data, the model equations will be changed to reflect the revised coefficient estimates from the new regression equations, and new model simulations and testing will be performed.

## 3.2. A conventional modeling system for econometric analysis

An active system for econometric modeling must support the life cycle phases described above. We describe a conventional modeling system for econometric analysis called the Progressive EconometRic Modeling system (PERM) [PERM, 1983] which supports these activities, and then show in subsequent sections how this system can be extended to provide active support.

PERM is a system developed by one of the authors and currently used by several telecommunications corporations for econometric estimation, simulation, and forecasting. PERM supports the entire econometric modeling life cycle shown in fig. 2 by providing the following functional capabilities:

(1) data management: a full complement of data storage, modification, and retrieval commands;

(2) statistical estimation: an ample suite of econometric techniques including discrete choice, maximum likelihood estimation, and pooling;

(3) simultaneous equation model-building: regres-

```txt
The general structure of PERM commands is given below (Brackets, { }, denote optionality and | means "or"):
COMMAND {VARLIST | #EQUATION-ID} {FOR CONDITIONALS}
COMMAND An 8 character or less verb specifying which operation is to be performed; see description of available commands in Figure 4-2;
VARLIST Variable list specifying names of data-series to be retrieved; series name is 15 characters or less beginning with a letter and may contain any character other than & @ $ ' # " , ; < > or blank;
A lag or lead may be specified with a data-series name by specifying the lag (negative integer) or lead in parentheses after the name, e.g., PINC(-2) refers to the data-series PINC lagged two periods; Polynomial distributed lags may be used in regression commands with the syntax:
<degree, length of lag, constraint>
EQUATION-ID A number specifying an equation's id.
Data-series names and equation-id's are mutually exclusive in the sense that one or the other may appear in a particular command (depending upon the command), but never both.
FOR Specified only if data selection conditionals are to be used;
CONDITIONALS Standard boolean conditions with the following operators available: EQ, NE, LT, LE, GT, GE, and BETWEEN...AND
The words OPTIONS, RANGE, OUTPUT, and INPUT have special significance when used in conditionals and are reserved.
OPTIONS EQ 'option1'{//'option2'/....} allows the user to invoke command-specific options.
RANGE BETWEEN yyyypp1 AND yyyypp2 specifies a data range for retrieval (yyyy=year and pp=period).
OUTPUT | INPUT EQ 'filename' designates I/O files.
Fig. 3 Syntax for PERM Action Language
```

Fig. 3. Syntax for PERM Action Language.

## Command Description

## DATA MANAGEMENT COMMANDS

DEL...... Delete Data
DIR...... Databank Directory
READ...... Read Data
SCALE...... Scale Data
TRANS...... Create Transformed Variable
UP...... Update Data Values
USE...... Access Databank (Read/Write)

## STATISTICAL ESTIMATION COMMANDS

ANAL..... Analyze Data
BOXCOX..... Box-Cox Specification Search
DIAGNOSE... Regression Diagnostics
HECKIT..... Heckit Estimation
LOGIT..... Logit Estimation
MLE..... Maximum Likelihood Estimation
OLS..... Ordinary Least Squares Regression
POOL..... Pooled Cross-section Time-series Regression
PROBIT..... Probit Estimation
RCR..... Random Coefficient Regression
RIDGE..... Ridge Regression
ROBUST..... Robust Regression
SUR..... Seemingly Unrelated Regression
TOBIT..... Tobit Estimation
VCR..... Variance Components Regression
WLS..... Weighted Least Squares Regression
2SLS..... Two Stage Least Squares
3SLS..... Three Stage Least Squares

## MODEL BUILDING COMMANDS

EDTEQ..... Edit Equation
ENTEQ..... Enter Equation
SVEQ..... Save Regression as Model Equation

## . MODEL SIMULATION COMMANDS

GO...... Perform Simulation
LOAD...... Load Simulation
WHATIF...... Change Exogenous Values in Simulation

## MODEL MAINTENANCE COMMANDS

AUP.... Automatic Update Propagation
REESTEQ.... Reestimate Regression Equations in Model

Fig. 4. Sample of PERM Commands.

sions can be saved as equations in simulation models;

(4) model simulation: models formed in the previous step can be solved and "what-if"s performed to provide econometric forecasts;

(5) model maintenance: data-series which are logically linked will be automatically updated by updating the base data-series, and models can be completely reestimated via a single command.

The PERM Action Language (PAL) provides the interface with the user. PAL is similar to the SQL database language except the user need not be concerned about which tables contain which data. All data-series are stored as vectors and users refer to these data-series directly by name. Fig. 3 provides the basic syntax for PAL. A typical command might be:

## OLS DEMAND PRICE INCOME POPULATION FOR STRIKE EQ 0 AND OPTIONS EQ 'LOG'

which says “Perform an ordinary least squares regression with all data-series in logarithms (OPTIONS EQ ‘LOG’) on the dependent variable DEMAND as a function of PRICE, INCOME, and POPULATION for those observations when there was no strike (STRIKE EQ 0).”

PAL provides other important enhancements to SQL. Whereas SQL is primarily used for data retrieval, PAL has a large set of commands which not only retrieve data but operate upon it as well (fig. 4).

PAL is structured so that every command corresponds to a process, thus when the user specifies 2SLS, PERM invokes a statistical routine which performs two-stage least squares. PAL is therefore equivalent to the user-directed process manager (UDPM) of the ADSS. Further, the commands and resulting output can easily be journaled in a history record as they are issued. This provides a basis for investigating modeling protocol given some knowledge of the problem the modeler is trying to solve. For example, if we saw the following consecutive entries in the history record (parenthetical remarks would not appear in the history):

$$
\text { OLS   varlist } \quad (\text { Linear   form })
$$

$$
\text { OLS   varlist   FOR   OPTIONS } = \text { `LOG' (Log   form) }
$$

$$
\begin{array}{c} \text { OLS   varlist   FOR   OPTIONS } = ^ {\prime} \text { LLHS } ^ {\prime} (\text { Log - Lin- } \\ \text { ear   form) } \end{array}
$$

$$
\begin{array}{c} \text { OLS   varlist   FOR   OPTIONS } = \text { 'LRHS' } (\text { Linear- } \\ \text { Log   form) } \end{array}
$$

we would be inclined to suspect the modeler was trying to determine the proper functional form of the regression.

PERM provides powerful features for building and simulating econometric models, but it does not constitute an active modeling system. This requires the addition of intelligent support to facilitate the modeling process.

## 4. A model control language for representing modeling strategies

Most modeling systems provide access to data and analytic techniques, but little, if any, guidance on how to apply those techniques correctly. An “intelligent” modeling system should be able to support model formulation and evaluation in a way that extends the capabilities of beginning and experienced modelers alike [Murphy and Stohr, 1985]. This is especially true for statistics and econometrics where guidance in the proper use of various estimation techniques may avoid common mistakes and subsequently improve the quality of resultant models.

## 4.1. Estimation techniques

The list of estimation techniques available to the applied econometrician is growing rapidly. Least squares techniques have always been the cornerstone of applied econometrics. Ordinary least squares (OLS), with the option of autocorrelation and heteroscedasticity corrections, is the most widely used technique. These as well as other error term violations have tended to shift the emphasis from OLS to generalized least squares (GLS). Having the ability to efficiently perform GLS allows the analyst much greater flexibility; for example, the pooling of time-series and cross-sectional data in either the least squares dummy variable (LSDV) method or Zellner's seemingly unrelated regression (SUR). These generalized abilities have led to other difficult estimation issues, however. The applied econometrician may well be faced with the following kinds of questions: what are the appropriate restrictions when pooling time-series and cross-section data (e.g., LSDV, SUR, or in-between), which error term assumptions are violated, and what is the appropriate functional form.

In addition to the more common least squares methods, the efficiency gains in computing have made maximum likelihood (ML) techniques feasible for applied econometrics. While the discrete choice methods like logit and probit are the most frequently used ML methods, there are several others techniques that commonly utilize ML in their solution, e.g., tobit, heckit, and some random coefficient methods [Judge et al., 1980]. The biggest and most powerful advance, however, is the application of general purpose ML routines developed for unconstrained nonlinear optimization problems. These routines allow the analyst to specify any likelihood function and then maximize it to obtain coefficient estimates. While most of these general purpose ML implementations are still crude in the sense that they require significant user expertise (e.g. derivatives of the likelihood function must be supplied), availability of ML techniques has significantly advanced the state-of-the-art of applied econometrics.

![](/api/attachments/F8VT9UB7/fulltext/images/d0828f0e45b087dfc6e2fd9a29008ee7fe5abf768041ed4d16b8e1d52be7c128.jpg)  
Fig. 5. Decision Tree for Functional Form Selection.

## 4.2. Modeling strategies as decision trees

We begin by assuming that the user has estimated a regression model; this model is assumed to contain the appropriate independent variables and to have coefficient estimates with the theoretically correct signs. For the moment, we further assume that the regression technique is OLS and the standard regression assumptions are met, e.g., the error term has zero mean, constant variance across observations, and is not correlated with itself across observations (time).

In this case (fig. 5), we wish to choose the correct functional form and insure that all coefficient estimates are statistically significant. The Box–Cox specification search is used to find the appropriate functional form. By comparing the signs of the coefficients with the original estimates and performing simple t-tests, we verify that the coefficient estimates have the correct signs and are statistically significant. The results of these “tests” are then reported to the user.

For the next example shown in fig. 6, we choose the simple textbook problem of testing for autocorrelation, e.g., the error term is not independent across time-series observations. Since correcting for autocorrelation typically reduces the size of the t-statistics, we will once again test for statistical significance of the estimated parameter estimates. Using a Durbin–Watson (DW) test to determine if autocorrelation is a problem, we simply re-estimate the equation invoking an autocorrelation correction option if the DW test is failed. If the correction is employed, we test for correct signs and t-statistics and report the results to the user. Notice that it would be straightforward to expand the “model is poor” message to detail the model failings by indicating, e.g., that the model has wrong signs or statistically insignificant coefficient estimates. As before, we have assumed that the user has selected the appropriate design matrix, coefficient signs are correct, and the regression technique is OLS.

![](/api/attachments/F8VT9UB7/fulltext/images/77d168fdf77c3658ab7021849757810f3e301e8197facab814d99a20260100aa.jpg)  
Fig. 6. Decision Tree for Autocorrelation Testing.

In comparison to these textbook or hypothetical examples, real world problems become increasingly complex. For example, simply combining the two examples into one, where the analyst is attempting to determine functional form when autocorrelation may be present, more than triples the number of tests to be performed [see Dolk and Kridel, 1989].

Straightforward generalizations are easily implemented, however. For example, if a lagged dependent variable is included in the regression as an independent variable, the Durbin H test can easily be substituted for the Durbin–Watson test. In addition reasonability checks can also be included. For example, the system could test if the estimated coefficients or implied elasticities were within some reasonability region. This region could be rather crude for general use or have a “finer” testing region for specific problems.

Understanding the impact of relaxing error assumptions is critical in comprehending the complicated nature of applied econometric analysis and the burden this implies for the analyst. An example will help clarify this point. The Box–Cox specification search is very sensitive to the underlying error assumptions. If the error term is not well-behaved, then direct application of the Box–Cox procedure will often lead to the selection of “incorrect” functional forms. As a result, not only does allowing violations of the standard error term assumptions require additional testing facilities, but it requires the ability to select functional form and correct for these violations simultaneously. Unless the analyst is aware of the implications of violations of the standard assumptions on all potential regression techniques, errors in estimation will certainly occur. While multiple violations of the standard assumptions pose no problem theoretically, when multiple violations are allowed, the complexity of the decision trees and testing processes become quite burdensome. Of course, this is exactly the reason why intelligent modeling is useful to the analyst.

Additional decision trees have been developed to assist the user in performing regression diagnostics [Belsley, Kuh and Welsch, 1980] and assessing the quality of forecasting models. The forecasting template checks the performance of the model in different periods (booms, busts) and compares implicit multipliers to reasonability standards as well as more common performance tests (root mean square error).

One of the challenges in building an ADSS is to identify local command patterns, or sequences, and match them with global modeling strategy sequences such as the decision trees identified above. One way of representing modeling strategy sequences explicitly is in the form of processes rendered in an appropriate model control language.

## 4.3. PERM control language (PCL)

Kottemann and Dolk [1988] identify requirements for a model integration control language (MICL) which allows processes to communicate with one another, and subsequently facilitates the specification of solution procedures for integrated models. The MICL supports variable correspondence, sequentiality, and dynamic synchronization among processes by providing structured programming constructs, message passing protocols, and variable monitoring (demons).

An MICL is a necessary component of a model manipulation language for an active modeling system because it serves as the medium in which schemas of statistical analysis strategy are encapsulated and subsequently activated. To demonstrate this point, we sketch a simplified PERM Control Language and show how it can be used to capture the modeling strategies outlined above. We emphasize that PERM does not currently support a PCL, although a prototype is under development.

The PCL must provide three capabilities: structured programming constructs, message passing protocols, and demons. The first two features can be accommodated by providing a simple language shell with sequence, selection, and iteration constructs in which ordinary PAL commands are embedded, plus a set of reserved words that serve effectively as arguments which can be passed among processes. The PAL commands activate various processes, usually statistical estimation techniques, which return a set of parameters such as the R-squared statistic, t-statistics, regression coefficients, and standard errors. These parameters are then used to determine whether acceptable statistical criteria have been met, and in this way, an overall model building strategy can be developed.

PCL supports standard programming language constructs of sequence, IF-THEN-ELSE selection, and REPEAT UNTIL iteration, as well as assignment statements, and input/output statements (fig. 7). Any acceptable PAL command is also acceptable in PCL. Additionally, there is a list of reserved variable names which serve as the output variables from any PAL statistical command. For example, BETA(INCOME) refers to the regression coefficient for the independent variable INCOME. Each of the reserved words can be indexed by a regression identifier so that parameters can be compared between regressions. If no regression identifier is specified, then the default is the current regression (i.e., the last regression executed). The four basic data types in PCL are MATRIX, VECTOR, SCALAR, and STRING with STRING being the default.

In addition to the structured programming constructs and reserved words, it is necessary to provide some facility for demons, or dynamic triggers, to detect the conditions under which the PCL processes are to be activated. The general structure of a demon is:

$$
\begin{array}{l} \text {Demon:   WHEN } \langle \text { Condition(s) are detected } \rangle \\ \text { THEN } \langle \text { Activate PCL Command(s) } \\ \text { and / or   Process(es) } \rangle \end{array}
$$

End-Demon

Demons will normally appear as headers to PCL processes so that it is readily apparent when the processes will be invoked. Implementation issues

## Programming Constructs

<table><tr><td rowspan="2">REPEAT UNTIL statement(s) END REPEAT</td><td>ASSIGNMENT STATEMENTS variable = expression</td></tr><tr><td>ARITHMETIC &amp; BOOLEAN OPERATORS</td></tr><tr><td rowspan="2">IF boolean(s) THEN statement(s) {ELSE statement(s)} ENDIF</td><td>+, -, *, /, **, &gt;, &lt;, &gt;=, &lt;=, &gt;&lt;, EXP, LOG, SUM, PI, SIGN, etc, etc.</td></tr><tr><td>MATRIX OPERATORS</td></tr><tr><td>INPUT/OUTPUT INFORM(string) ACCEPT(string)</td><td>+, -, *, INV, &#x27; (trans- pose)</td></tr></table>

## Data Types

```txt
MATRIX Ordinary matrix, eg: INDEP_VAR[100,7]
SMATRIX Symmetric matrix, eg: VAR_COV[7,7]
VECTOR Ordinary vector, eg: DEP_VAR[100]
SCALAR Ordinary scalar, eg: R**2
STRING String of chars, eg: 'LOG'
```

## Reserved Words

```txt
BETA(var, regr) Coefficient of independent variable "var" and regression "regr".
ELAST(var, regr) Elasticity for independent variable "var" and regression "regr".
T(var, regr) T-statistic for independent variable "var" and regression "regr".
FUNCTFORM(regr) Functional form for regression "regr"
= 'LIN' for linear
= 'LOG' for logarithm
= 'LLHS' for log-linear
= 'LRHS' for linear-log
RSQ(regr) R**2 of regression "regr"
DW(regr) Durbin-Watson of regression "regr"
F(regr) F-statistic of regression "regr"
VARLIST[regr] Variable list for regression "regr"
RHO[regr] Estimated rho(s) for regression "regr"
```

Fig. 7. Partial Specification of PCL Syntax.

```txt
PROCESS SELECT FUNCT_FORM
DEMON
WHEN HIST_REC.PREV_COMMAND EQ "OLS"
AND HIST_REC.CURRENT_COMMAND EQ "OLS FOR OPTIONS EQ 'LOG' "
ACTIVATE
END DEMON
* Save functional form from current regression
FF0=FUNCTFORM
* Invoke PAL command for Box-Cox specification search
BOXCOX varlist
IF FUNCTFORM >> FF0 THEN
INFORM "FUNCTFORM is the better functional form"
ENDIF
* Perform t-tests on estimated coefficients
IF T(varlist) < t_cv THEN
INFORM "Warning: Model is poor; BETA(var(s))
statistically insignificant"
ELSE
INFORM "Model is acceptable"
RETURN
ENDIF
Fig. 8. PCL Process for Functional Form Selection.
```

arise with respect to demons in the PERM system but before addressing these problems, it is useful to see what a PCL process looks like.

4.4. Schemas as PCL processes of modeling strategies

The notion of schema is central to the ADSS. Our view is that schemas for econometric modeling are PCL processes which encapsulate statistical strategy for specific situations. To demonstrate what we mean, we will render the decision trees in Section 4.2 as PCL processes.

As before we assume the user-specified regression is “current”, that the coefficient signs are correct, and that the regression technique is OLS. Fig. 8 displays the PCL process for the example presented in fig. 5. It should be noted that to perform the t-tests in the second IF, a table lookup for the critical value of the t-statistic (t\_cv) is required.

The PCL template for the second decision tree discussed above is presented in fig. 9 (once again we maintain the same assumptions described in fig. 6). The information supplied to the user at each step could also include modeling suggestions. For example, if the model failed the second autocorrelation test, the system could suggest that the autocorrelation problem may be due to misspecification and suggest that the user consider adding additional independent variables to the regression. As noted in the previous example, all statistical and reasonability checks require table lookups.

Second, demons are critical to the ADSS since they are the mechanism whereby user command sequences in the history record are “recognized” as part of a more wide reaching strategy schema. The method of embedding these demons in the PERM system presents a challenge, however, since each demon must effectively be implemented by some kind of suspend-resume mechanism explicitly programmed in the Fortran source code, a task for which Fortran is not well-suited. For example, in order for the ADSS to recognize the two consecutive commands

A number of comments are germane at this point. First, the PCL serves as the Computer-Directed Process Manager (CDPM) of the ADSS. Once the ADSS recognizes that the user input pattern fits into one of the schemas, or modeling strategies, in the schema library, then it will invoke the appropriate PCL process(es). Thus the ADSS is augmenting the user-directed command by overlaying a more comprehensive modeling strategy.

```txt
PROCESS AUTO_TEST
DEMON
WHEN HIST_REC.PREV_COMMAND EQ "OLS"
AND DATA-SERIES >< CRS
ACTIVATE
END DEMON
* Save BETA from current regression
BETA0(varlist) = BETA(varlist)
* Durbin-Watson test for autocorrelation
IF DW > dw_cv THEN
* Invoke PAL command for autocorrelation correction
OLS FOR OPTIONS EQ 'AUTO'
IF DW > dw_cv THEN
INFORM "Warning: Model is poor; ... autocorrelation"
RETURN
ENDIF
IF SIGN(BETA(varlist)) >< SIGN(BETA0(varlist)) THEN
INFORM "Warning: Model is poor; Incorrect signs"
RETURN
ENDIF
ELSE
IF T(varlist)) < t_cv THEN
INFORM "Warning: Model is poor; Insignificant ..." 
RETURN
ENDIF
INFORM "Model is OK; estimated rho is 'RHO(regr)' "
ENDIF
RETURN

Fig. 9. PCL Process for Autocorrelation Correction.
```

OLS varlist {FOR Conditionals}
OLS varlist FOR OPTIONS EQ 'LOG'

## {AND Conditionals}

as an attempt to establish functional form, it must interrupt the program at some point (probably immediately after each command is issued) to perform the pattern checking. There is now no way for the PERM system to do this automatically from only a PCL demon declaration. The situation is further complicated because a user-directed process may be interrupted in a way that requires complex process synchronization as well. For example if an ordinary least squares regression is interrupted in midstream to check for collinearity, it may be necessary to synchronize various stages of the collinearity process with stages of the OLS process. Thus, in the general case, each demon specified in PERM must be implemented by explicitly inserting traps in the appropriate places in the code. This is unacceptably cumbersome, thus some compromises must be made, such as testing for demons only at a few, prespecified points.

Third, PCL provides a tractable medium in which experts can build predefined model strategy schemas and thus develop a more comprehensive schema library. The PCL processes themselves form a knowledge base of econometric modeling strategy.

## 5. History inference processor

The most difficult problems in an ADSS arise in the history inference processor (HIP). Recall that the HIP is responsible for building a computer model which emulates the user's problem-working process. This requires formulating and testing hypotheses about the user, the problem, and relevant problem-working processes. These processes are represented as a network of schemas which are developed from protocol analysis, expert definition, or dynamic pattern recognition.

In the case of an artificially intelligent econometrician, this requires matching strings of user commands with statistical strategies contained in the schema library. Our initial approach to developing a HIP is as follows:

(1) Build a library of PCL process schemas developed by experts in the area of econometric analysis. These schemas will reflect expert knowledge of various statistical strategies as shown in Sections 4.2 and 4.3.

(2) Conduct a number of experiments with modelers to identify patterns of command sequences which are likely to appear in the particular problem situations represented by the schemas. This can be done currently by examining a PERM history record for a session to see what PAL commands were issued.

(3) Insert a demon in PERM which, after every user-directed command is issued, examines the history record and tries to match the current command sequence with one of those derived from the second step. When a match is found, the relevant PCL process is activated to supersede the current user command.

We see several research issues which are relevant to this effort. One is the determination of what aspects of statistical strategy we can reasonably expect to capture. Oldford and Peters [1986] present an ordering of statistical strategies from low-level (e.g., collinearity diagnosis) to high-level (overall model analysis and design), and suggest that there is a limit to the level at which a DSS can usefully support statistical strategy. In particular, this level is a function of how context-dependent the problem is. This is the familiar domain problem which characterizes all expert system applications. Since we are working from the bottom up with respect to this ordering, one of the things we hope to discover is where that practical limit occurs for econometrics.

Another research issue is deciding how intrusive an ADSS should be. Such a system could potentially dominate the “dialog” with a user, continually activating “helpful” schemas which may become annoying after awhile, not to mention expensive. On the other hand, a system which provides support with little, or no, dialog may take on a mystical quality which could undermine its eventual utility. The question of how much support to provide is also a function of user sophistication; naive econometricians will need more help than the seasoned veterans who write the schemas, for example.

The approach outlined above comprises a simplified version of an inference processor, yet could nevertheless provide powerful support in formulating econometric models. Whether this approach constitutes an ADSS is another issue, however. One feature it currently lacks is the ability to identify patterns and create new schemas dynamically. This would require more powerful pattern recognition heuristics as well as some form of automatic code generation capability to transform new patterns into PCL processes.

A fully active system may very well require a radical departure from conventional expert system technology. Research in neural networks is one promising alternative that supports many of the requirements of an ADSS. With neural networks, knowledge is not encoded as rules but rather as patterns of connectivity between nodes. Further, these patterns evolve from usage and experience rather than having to be hard-wired by a programmer or knowledge engineer. Thus, processes yield the data structures (rules) dynamically as opposed to current expert systems where the data structures are required a priori for reasoning to take place. Another appealing feature of neural nets is that some kinds of learning take place quite naturally, thus under the right conditions, it is possible to “train” a net so that an input pattern will result in a specified output pattern [Rumelhart and McLelland, 1986].

The kind of behavior exhibited by neural networks is directly in line with the precepts of ADSS. However, one problem with using neural networks for applications of the kind we have described is that their focus is at a very microscopic level. Much work needs to be done with respect to combining and layering these networks in order to address more macroscopic problems. Although it is not clear at this time how one would incorporate this research into DSS technology, we plan to investigate whether any of the adaptive pattern recognition mechanisms inherent in neural networks can be adapted for use in the HIP.

## 6. Conclusions

We have marshaled ideas from model management, econometrics, and conventional expert systems to consider the feasibility of a developing an active DSS that would serve as an “artificially intelligent econometrician”. We have presented a model manipulation language for econometric analysis which is a slight modification of SQL and which can serve as the user-directed process manager in an ADSS. We then discussed an extension to this language which allows demon descriptions and provides structured programming constructs. This model control language serves as the basis for representing statistical strategy schemas and as a computer-directed process manager in an ADSS. Finally, we outlined an approach to building an inference processor which attempts to recognize model manipulation command sequences as a subset of a more comprehensive strategy schema. Once pattern recognition occurs, one or more schemas is activated to support sound econometric analysis.

We have not answered conclusively whether an ADSS for econometric analysis is feasible. It seems to us that one can go only so far using conventional rule-based expert systems technology, however. More innovative approaches like neural networks may be required to realize a fully active system. Nevertheless, we believe that the system we have described shows the promise of ADSS concepts for implementing intelligent modeling systems.

## References

Belsley, D., Kuh, E. and Welsch, R., Regression Diagnostics, Wiley, 1980.

Dolk, D.R. and Kridel, D.J., Toward a Symbiotic Expert System for Econometric Modeling, Proceedings of the 22n HICSS, Volume III, IEEE Computer Society, 1989, pp. 3–13.

Judge, G., Griffiths, W., Hill, R., and Lee, T. The Theory and Practice of Econometrics, Wiley, 1980.

Keen, P.G.W. and Scott Morton, M., Decision Support Systems: An Organizational Perspective. Addison-Wesley, 1978.

Kottemann, J.E. and Dolk, D.R., Process-oriented model integration. Proceedings of the 21st HICSS, Vol. III, IEEE Computer Society, 1988, 396–402.

Manheim, M., An architecture for active DSS. Proceedings of the 21st HICSS, Vol. III, IEEE Computer Society, 1988, 356–365.

Manheim, M., Issues in Design of a Symbiotic DSS. Proceedings of the 22nd HICSS, Vol. III, IEEE Computer Society, 1989, 14–23.

Murphy, F.M. and Stohr, E.A., An intelligent system for formulating linear programs. Decision Support Systems, 2, 1985, 39–47.

Oldford, R.R. and Peters, S.C., Implementation and study of statistical strategy. In Artificial Intelligence and Statistics, W.A. Gale, ed., Addison-Wesley, 1986.

Remus, W. and Kottemann, J.E., Toward intelligent decision support systems: An artificially intelligent statistician. Management Information Systems Quarterly, December 1986.

Rumelhart D.E. and McLelland, J.L., Parallel Distributed Processing, Volume 1. MIT Press, 1986.

Sprague, R. and Carlson, E., Building Effective Decision Support Systems. Prentice-Hall, 1982.

User's Manual for PERM, Software Model Management Systems, 15230 Oak Hills Drive, Salinas, CA 93907, C1983.
