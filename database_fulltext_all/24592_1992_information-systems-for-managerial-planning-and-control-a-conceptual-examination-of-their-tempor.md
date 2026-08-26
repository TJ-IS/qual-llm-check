---
otero_id: 24592
otero_key: "E2W7KPSM"
title: "Information Systems for Managerial Planning and Control: A Conceptual Examination of Their Temporal Structure"
authors: "Gad Ariav"
year: "1992"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1992.11517959"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems for Managerial Planning and Control: A Conceptual Examination of Their Temporal Structure

Gad Ariav

To cite this article: Gad Ariav (1992) Information Systems for Managerial Planning and Control: A Conceptual Examination of Their Temporal Structure, Journal of Management Information Systems, 9:2, 77-98, DOI: 10.1080/07421222.1992.11517959

To link to this article: http://dx.doi.org/10.1080/07421222.1992.11517959

![](/api/attachments/E2W7KPSM/fulltext/images/b1a2c5026122e56da280325b210a5d1b64a8fd488d6d295358a77c410f69b19e.jpg)

Published online: 16 Dec 2015.

![](/api/attachments/E2W7KPSM/fulltext/images/f040a033bc073dcacc7e624d85787a5ec0a70b041020fc7184de101cd847214e.jpg)

Submit your article to this journal ↗

![](/api/attachments/E2W7KPSM/fulltext/images/fcc9c94894243745ad18379ee0324c0c04560c5659c55537a18e2fc62d7e2e11.jpg)

View related articles ↗

# Information Systems for Managerial Planning and Control: A Conceptual Examination of Their Temporal Structure

GAD ARIAV

GAD ARIAV received his Ph.D. in decision sciences in 1984 from The Wharton School of the University of Pennsylvania. His research since then has focused mainly on temporally oriented database management and decision support systems. Before joining Tel Aviv University, he was on the faculty of New York University's Stern School of Business for five years. Dr. Ariav has been dealing professionally with computers and information systems since 1967, including three years in Europe as a leader of a database development project. He has published articles in the Communications of the ACM, ACM Transactions on Database Systems, and Data & Knowledge Engineering, and he serves as an Associate Editor of MIS Quarterly. Together with Michael J. Ginzberg, he is completing a comprehensive book on the design and implementation of Decision Support Systems, to be published by McGraw-Hill in 1993.

ABSTRACT: The managerial functions of planning and control are information-intensive “memory processes,” and are inherently temporal. As such, they are a major application domain for temporally oriented information systems (TOIS), which are distinguished by their explicit handling of time and memory. Although TOIS have been studied vigorously in recent years, there has been no attempt to relate them to the temporal concerns pertinent to these managerial processes. This paper systematically examines the structure of, and access to memory in planning and control activities, in an attempt to identify major related design requirements.

The examination proceeds as follows: First, a conceptual framework of planning and control is developed. This framework facilitates the examination of memory aspects of these processes, specifically the extent and nature of memory implied by the underlying models and the actual control schemes. The three themes that emerge from this examination are: (1) the fundamental necessity of temporally independent access to data in planning and control applications; (2) the inherent multiplicity of time perspectives upon which the notions of planning and control rest; and (3) the need to develop temporally oriented model management. These themes identify basic temporal functionalities that TOIS need to address. Current research on temporally oriented information systems, as assessed against these criteria, has not come up yet with adequate answers.

Acknowledgments: Niv Ahituv, Eric Clemons, Linda-Jo Calloway, Jim Emery, Michael Ginzberg, Howard Morgan, Charlie Tapiero, Ron Weber, and anonymous referees commented on earlier versions of this paper. Their help is gratefully acknowledged.

KEY WORDS AND PHRASES: design requirements for information systems, model management, temporally oriented information systems, planning and control.

## 1. Introduction

THE STUDY OF TEMPORAL ASPECTS OF INFORMATION systems, which has witnessed an extraordinary growth in recent years, has so far centered on technology, primarily temporally sensitive data modeling and related database architectures $[10, 28, 36]$ . The intuitively appealing premise of this growing interest is the recognition that time is a ubiquitous and universal data attribute with its own unique semantics, which users of information systems treat in very special ways. Nevertheless, the question of how information system users actually use temporal information has been rarely raised by the research community that deals with these issues $[5]$ .

Unfortunately, very limited guidance is available elsewhere. There have been only few systematic attempts to identify explicitly the notions of time that are embedded in the various aspects of management $[38, 39]$ . Moreover, even in these attempts, the discussion of information is rather indirect, and information systems are either conceptualized in an abstract fashion (e.g., as statistical inferences or Bayesian estimates), or “assumed away” in the sense that the availability of necessary data is taken for granted. As a result, the development of temporally oriented information systems (TOIS) is proceeding without an explicit notion of what constitutes an effective design for this type of information-processing capability.

As nothing evades our attention so persistently as that which is taken for granted, the purpose of this paper is to deal directly with the temporal nature of the data used in management processes. The focus is specifically on planning and control processes, undoubtedly major managerial tasks $[2]$ . The inquiry proceeds as follows: Section 2 presents a formal framework that consolidates varied references to the topics of planning, control, and time. This unified, basic, but sufficiently expressive model then serves as the background for the study—in the ensuing sections—of key temporal aspects. Section 3 examines the use of information in the different levels of planning models and section 4 takes a closer look at the information constructs that underlie the variety of possible control schemes. The result is an outline of major concepts in the memory structure embedded in managerial planning and control. Memory structure is a term that collectively summarizes the capture of historical processes as formal data and the access to, and use of such preserved data. Section 5 then recapitulates the major design implications, relating them to recent research results.

This paper addresses mainly the concerns that are pertinent to the branch of information systems often labeled decision support systems (DSS). These systems are meant to provide decision makers with computerized, often interactive, tools to support them in their managerial tasks $[6]$ . Planning and control have been traditional arenas for the implementation of DSS, and often serve as the natural setting for the demonstration of their impact and value $[2]$ .

## 2. A Basic Framework of Planning and Control

ONE WAY TO DESCRIBE PLANNING IS AS AN EFFORT to temporally arrange seemingly unrelated data in a way that explicates the perception of causal links between events and actions $[38]$ . The corresponding function of control, that is, the study and analysis of deviations of actual outcomes from the ones planned, is therefore ultimately aimed to improve the planning process $[18]$ . The notational framework presented in this section expresses these common views of planning models and schemes of control in order to facilitate the systematic discussion of possible implications for information systems design. In order to allow concise but broad reference to assumptions about the availability and use of temporal information in processes of planning and control, the view of these processes in this paper is narrow and the framework is intentionally abstract.

In basic schemes of planning and control, observations are made at two points in time. Without loss of generality, let $t_{1}$ denote the time when the plan is put into effect, and let $t_{2}, t_{2} > t_{1}$ , denote the end of the planned period. In a generic formulation of the planning and control problem, the following conceptual elements are identified (after [18]):

\- Decision variables: A set of controllable variables, such as product prices, dollar investments in equipment, lot sizes, or the number of employees. Let $D[t, (t_1, t_2)]$ denote a vector of decision variables' value for the period of time starting at $t_1$ and ending at $t_2$ , as it is known at time $t$ , that is, "as of $t$ ." For instance, $D[t_1, (t_1, t_2)]$ is the plan of action as it is formulated at time $t_1$ , the beginning of the planned period, while $D[t_2, (t_1, t_2)]$ is the set of actual decisions made during the same period of time, as it is observed at the end of the period.

\- Environmental variables: A set of relevant and uncontrollable aspects, denoted $E[t, (t_1, t_2)]$ . Examples for these variables might be oil prices, the GNP, or permissible levels of pollution. For example, $E[t_0, (t_1, t_2)]$ is the environment predicted at time $t_0 < t_1$ to prevail during the period $(t_1, t_2)$ . While $E[t_0, (t_1, t_2)]$ is made sometime before the planned period commenced, $E[t_2, (t_1, t_2)]$ is the same set of variables for the same period, but as actually observed at the end of that period.

\- Outcome variables: A set of variables denoted $O[t, (t_1, t_2)]$ , that measure the performance of the business unit in a specific period of time. This could be, for instance, the accumulated dollar value of sales or revenue, the number of items sold or produced, or the share of the market captured during the period. $O[t_1, (t_1, t_2)]$ is the predicted performance for the planned period, while $O[t_3, (t_1, t_2)]$ denotes these outcome values as they had actually turned out, as has been observed and recorded at $t_3 > t_2$ , sometime after the specified period actually concluded.

\- Models: A model conceptually links decision, environment, and outcome variables of a given planning scenario. The model represents the essence of the process at hand in a concise functional form and explicates the (quantitative) relationship among the involved variables. Examples may include equation sets, input/output models, production functions, econometric models of economic activity, or a simulation model. Although typically overlooked, models too evolve over time, thus the function $M[t_0, (t_1, t_2)]$ denotes the model as it is perceived at the time $t_0$ , prior to the beginning of the planned period, and $M[t_2, (t_1, t_2)]$ is the ex-post perception of the model that prevailed during the planned period. The difference between these two versions of the model $M$ reflects changes in the process modeled, as well as changes in the understanding of the process, for example, a finer resolution, fewer explaining variables in the equations, different coefficients in the model's equations, or even new functional forms (e.g., S-shaped rather than linear).

For the purpose of brevity we will henceforth, when possible, omit the explicit mention of the planned period, but retain the reference to the temporal perspective, that is, the point in time from which data or models are viewed. Thus, for example, $E[t_{0}]$ and $M[t_{1}]$ will stand for $E[t_{0}, (t_{1}, t_{2})]$ and $M[t_{1}, (t_{1}, t_{2})]$ , respectively.

Now that the basic elements of information for planning have been outlined, the structure of control schemes can be discussed. The key construct in these schemes is the “simulated” or “computed” performance, denoted S, with which actual performance is typically compared. A simulated performance is a composite variable computed through the application of a model to decision and environment variables. Yet models, decisions, and environments can be anchored in different temporal perspectives and therefore give rise to different versions of S. The following is a comprehensive set of eight schematic versions of S, indexed in a way that recaps the temporal perspective of the individual components in the composite expression. Specifically:

$S_{111} = M[t_1]\{D[t_1], E[t_1]\}$ is the projected outcome for the period $(t_1, t_2)$ , computed entirely from $t_1$ 's time perspective. $S_{111}$ is conceptually identical to $O[t_1, (t_1, t_2)]$ . $S_{112} = M[t_1]\{D[t_1], E[t_2]\}$ is an outcome projection modified to reflect posterior environmental knowledge. The assumption throughout is that actual values pertaining to the $(t_1, t_2)$ period are indeed "known" at $t_2$ . If an inherent delay characterizes the process, then an appropriately later point in time should be specified instead.

$S_{121} = M[t_1]\{D[t_2],E[t_1]\}$ is an outcome projection reflecting the actual activities, rather then the ones originally planned.

$S_{122} = M[t_1]\{D[t_2], E[t_2]\}$ is a projection that incorporates posterior knowledge about the environment and the activities, while retaining the original perception ("model") of the process.

$S_{211} = M[t_2]\{D[t_1],E[t_1]\}$ is an outcome projection with posterior formulation of the process, but under the original (a priori) environmental forecasts and planned activities (i.e., the decision variables).

$S_{212} = M[t_2]\{D[t_1],E[t_2]\}$ is as $S_{211}$ , but with posterior environmental knowledge. $S_{221} = M[t_2]\{D[t_2],E[t_1]\}$ reflects posterior perceptions of the modeled process and actual decisions, but retains the original environmental predictions.

$S_{222} = M[t_2]\{D[t_2],E[t_2]\}$ is the posterior explanation of the actual outcomes.

The computed values above are in essence the summary of some fundamental “what if” scenarios that are useful for control purposes. The most elementary control scheme—and the least demanding in terms of information system design—involves the comparison of $S_{222}$ with $O[t_{2}]$ . Comparing this pair of values reveals the extent to which we can explain our performance after the fact: if $M[t_{2}]$ faithfully captures the underlying process, then $S_{222}$ should be close to $O[t_{2}, (t_{1}, t_{2})]$ , up to a random noise. This comparison is essentially a “flat snapshot” assessment, although it may involve some limited historical data. Other common elementary schemes, the differences $S_{222}-S_{111}$ or $O[t_{2}]-O[t_{1}]$ , are sensitive only to the total deviation. The “what if” interpretation of the scheme $S_{222}-S_{111}$ is: how much of a difference it would have made if we had known at the time of planning what we know “today,” namely, the actual environmental conditions, the actual actions, and the true nature of the process. In many control systems $O[t_{1}]$ and $O[t_{2}]$ are typically the only formally available information on which the analysis of deviations in business performance is based.

The basic framework presented in this section assumes the simplest form of models and identifies only the very basic control schemes. As it turns out, deeper understanding of these two topics is crucial in relating to the necessary extent of memory in TOIS for planning and control purposes. In section 3 we examine the dynamic nature of $M[t]$ , the model, and in section 4 advanced control schemes are studied.

## 3. Temporal Aspects of Planning Models

THE ACTUAL STATEMENT OF THE MODEL, $M[t, (t_{1}, t_{2})]$ , concretely operationalizes planners' understanding—at a given time—of how environmental conditions and controllable actions determine levels of performance in a specified time period. Beyond the two direct time references used to index models (i.e., the planning period $(t_{1}, t_{2})$ and the temporal perspective t), there is a deeper temporal aspect, namely the extent of dynamics encapsulated by the model. Dynamics is reflected by the extent to which the set of primitive data identified and tied together by a model pertains to different time periods, and the extent to which the model itself describes the relationship among past, anticipated, and present states [38]. The relationship—within a particular planning and control application—between the dynamic level of the underlying model and the design of the corresponding information systems, has traditionally been overlooked.

In this section we examine more closely a comprehensive set of concrete functional forms that the abstractly stated $M[t, (t_{1}, t_{2})]$ can assume, and analyze their respective assumptions about available information. The set of functional forms to be studied is based on the typology of memory processes in [38], which suggests that models can assume five distinct levels of dynamics, as summarized in Table 1. The premise of this view is that dynamics is a complex property of planning models, and that we can therefore relate to it in terms of degree or level, distinguishing among model types according to the complexity of their implied memory structure.

The implicit structure of the model discussed in section 2 above is of Type I, namely, a myopic formulation. In this level of modeling, the model is essentially static, that is, neither past nor future has an explicit effect on the present state, and the prevailing description of the process is concerned with a single time period. In such a memoryless formulation, $O[t, (t_{1}, t_{2})]$ , for example, the cumulative sales volume, could assume the following functional form:

Table 1 Generic Levels of Memory Processes

<table><tr><td rowspan="2">Type</td><td rowspan="2">Label</td><td colspan="2">Extent of Memory</td></tr><tr><td>Periods</td><td>Temporal Reference</td></tr><tr><td>I</td><td>no memory</td><td>single</td><td>current only</td></tr><tr><td>II</td><td>differential</td><td>two</td><td>current and immediately preceding</td></tr><tr><td>III</td><td>delay</td><td>one or two</td><td>a period or two consecutive periods in the past</td></tr><tr><td>IV</td><td>integro-differential</td><td>multiple</td><td>any string of consecutive periods in the past</td></tr><tr><td>V</td><td>anticipative</td><td>multiple</td><td>past (like Type IV) and extrapolated future data</td></tr></table>

$$
O [ t, (t _ {1}, t _ {2}) ] = k _ {1} (t) + f _ {1} (t) \{E [ t, (t _ {1}, t _ {2}) ], D [ t, (t _ {1}, t _ {2}) ] \}.\tag{1}
$$

The constant $k_{1}(t)$ and the function $f_{1}(t)$ in this equation are economic parameters of compatible cardinality that are believed, at time t, to prevail throughout $(t_{1}, t_{2})$ .

The assumption of this very basic view is that performance for the period is completely determined by contemporary structural parameters and variables, and that the modeled effect is registered instantaneously. These limiting assumptions greatly simplify the task of the corresponding information management—references are made only to current values and data, a service that information systems commonly provide.

The fundamental limitations embedded in this type of models are two, namely, limiting the reference to a single period, and making reference only to the current period. These limitations are gradually relaxed in the subsequent discussion, and further model formulations allow for multiple periods and varying depths of reference to memory. Formulations of Type II, for instance, relax both assumptions. Type II processes (labeled Differential Memory Processes by [38]) are those where history is completely summarized in the state attained in the immediate past (i.e., processes of Markovian nature). Outcomes in these models are functions of change, and change itself is explicitly introduced as a single-step incremental phenomenon. The following equation is an example of a functional form of that type, applied to our previous schematic performance model:

$$
\begin{array}{r l} & O [ t, (t _ {1}, t _ {2}) ] = \\ & k _ {2} (t) + f _ {2} (t) \{E [ t, (t _ {1}, t _ {2}) ], D [ t, (t _ {1}, t _ {2}) ] \} + \\ & f _ {3} (t) \{E [ t, (t _ {1}, t _ {2}) ] - E [ t, (t _ {0}, t _ {2}) ], D [ t, (t _ {1}, t _ {2}) ] - D [ t, (t _ {0}, t _ {2}) ] \}. \end{array}\tag{2}
$$

This formulation holds for all past and future successive periods of time, and setting $f_{3}(t)$ to be a zero function reduces Type II expressions to Type I. The implications of a Type II planning model for information management are two: namely, the extension of the storage capacity to retain data of both the current period as well as the one immediately preceding it, and the extension of data access vocabulary to include expressions for invoking and contrasting sets of data from different periods of time. Although, in principle, the complexity of temporal reference to data has been introduced by this form, limiting it to two consecutive periods suggests some practical ad-hoc solutions. Indeed, this is a fairly common feature of information systems for planning and control applications.

The more general problematic of temporally oriented reference to data is being introduced, though, in Type III models. Delay or “lagged” memory process is one where the current state or behavior is a function of conditions that prevailed (or occurred) n periods earlier. The delay memory characteristic can extend both Type I and Type II memory processes, and form two variants, namely, the lagged myopic and the lagged differential memories. For instance, the lagged version of the model in equation (1) would look as follows:

$$
O [ t, (t _ {1}, t _ {2}) ] = k _ {3} (t) + f _ {4} (t) \left\{E [ t, (t _ {- n + 1}, t _ {- n + 2}) ], D [ t, (t _ {- n + 1}, t _ {- n + 2}) ] \right\}.\tag{3}
$$

$O[t, (t_{1}, t_{2})]$ in this equation is a function of the decisions and conditions that prevailed at period $(t_{-n+1}, t_{-n+2})$ , where n > 0. Setting n = 0—that is, no delay—reduces Type III models to Type I. A lagged Type II model will have components like $E[t, (t_{-n+1}, t_{-n+2})] - E[t, (t_{-n}, t_{-n+1})]$ added to equation (3). These elements isolate the changes in the environment and decisions that prevailed at period $(t_{-n+1}, t_{-n+2})$ relative to the period that immediately preceded it. “Plain” Type II expression is similarly achieved by setting n = 0.

This level of dynamics introduces the core design problem of TOIS: it implies the reference from the present to some arbitrary period in the past, and as a result it dictates the storage and maintenance of information pertaining to all periods in between. A basic tenet of Type III models that could be exploited in the implementations of corresponding information systems is that only two periods are addressed at any time, and mechanisms of information systems for Type II models could be applied. Such simplifications are finally ruled out in memory processes of Type IV.

A dynamic model of Type IV (labeled Integro-Differential by [38]), incorporates the impact of multiple past periods simultaneously. The functional form is such that the current state of the process is determined by past events through a time-dependent weight function. This weight function reflects the relative importance at the present of an event that has occurred at some point of time in the past. The functional form in the following equation is an example for such a complex relationship among performance, decisions/actions, and environmental conditions:

$$
\begin{array}{l} {O [ t, (t _ {1}, t _ {2}) ] =} \\ {k _ {4} (t) +} \\ {\sum_ {j = - n} ^ {- \infty} w [ t, (t _ {j + 1}, t _ {1}) ] \cdot f _ {5} (t) E [ t, (t _ {j + 1}, t _ {j + 2}) ], D [ t, (t _ {j + 1}, t _ {j + 2}) ].} \end{array}\tag{4}
$$

The function $w[t, (t_{j+1}, t_1)], j \leq 0$ , denotes the perception at t of the “relative relevance” of values that prevailed j periods before $t_1$ to performance behavior in period $(t_1, t_2)$ . Note that delay could be introduced either through n, $n \geq 0$ in the lower summation limit or through an appropriate set of null weights, and that therefore the memory processes of Type I and Type III are immediate special cases of Type IV. Similarly, processes of Type II can be formulated as Type IV models with weights of consecutive periods set to isolate differential effects.

This multiple period, weighted form of $M[t]$ has an important role in management science, as there are only few managerial interventions with an impact that is inherently and exclusively confined to a single and current period of time. An example of this type of process is the popular forecasting of demand by means of a moving average, or by exponential smoothing. Correspondingly, this model also defines a broader scope of TOIS services, as it necessitates not only the flexible reference to various periods of time, but also assumes the capacity to evaluate multiperiod expressions. Such capabilities are not commonly provided, and are definitely not a standard service of typical information systems [18, 25].

Models of Type IV completely relax both the periodic constraint as well as the limitation on the extent of reference to the past. Nevertheless, $[38]$ identifies a fifth level of dynamic modeling, labeled as Anticipative Memory, which does not imply deeper dynamics, but rather adds functional complexity to model expressions. Specifically, this formulation of memory processes captures the influence of anticipated future states on current activities or behavior. According to this view, the extrapolation of the future (e.g., prediction, speculation) dominates the functional expressions that determine present activity. Past experience thus has an effect on current decisions only to the extent that it shapes expectations with regard to the future.

In the ongoing set of examples, a model of Type V could be:

$$
\begin{array}{l} { \begin{array}{l} {O [ t, (t _ {1}, t _ {2}) ] =} \\ {k _ {5} (t) +} \\ {\sum_ {j = 0} ^ {\infty} w ^ {*} [ t, (t _ {1}, t _ {j + 1}) ] \cdot f _ {6} (t) \{E ^ {*} [ t, (t _ {j + 1}, t _ {j + 2}) ], D ^ {*} [ t, (t _ {j + 1}, t _ {j + 2}) ] \}.} \end{array} } \end{array}\tag{5}
$$

In the above example, $w^{*}[t, (t_{i}, t_{j+1})], j \geq 0$ denotes the relative impact of conditions anticipated to prevail in future periods, on the state of affairs during $(t_{1}, t_{2})$ —as perceived at t. As can be clearly seen, equations (4) and (5) differ only in the summation limits, but share a functional form.

The forecasted actions and environmental conditions, are derived from recorded data. For example, the following recursive moving average function forecasts the environmental conditions in the period $(t_{j}, t_{j+1})$ :

$$
\begin{array}{r l} & E ^ {*} \left[ t _ {p}, (t _ {j}, t _ {j + 1}) \right] = \\ & \sum_ {i = p} ^ {j - 1} w \left[ t _ {p}, (t _ {i}, t _ {j}) \right] \cdot E ^ {*} \left[ t _ {p}, (t _ {i}, t _ {i + 1}) \right] + \\ & \sum_ {i = 1} ^ {\infty} w \left[ t _ {p}, (t _ {j}, t _ {p - i}) \right] \cdot E \left[ t _ {p}, (t _ {p - i}, t _ {p - i + 1}) \right]. \end{array}\tag{6}
$$

The temporal perspective in the expression above, $t_{p}$ , is the “current” time from the point of view of the data involved. As a result, this weighted environmental projection for period $(t_{j}, t_{j+1})$ incorporates two strings of values, namely, a series of forecasts for periods in the future relative to $t_{p}$ , and another string of values that have been already observed (and recorded) at that time. The expression in equation (6) highlights further complexities with respect to the use of temporal perspectives in the context of planning models. Throughout the discussion so far we have implicitly assumed that the models are applied with the temporal perspective being set as $t_{1}$ —the “present” coincided with the beginning of the planned period. Equation (6) demonstrates clearly that the two need not be the same. It also demonstrates the intricate role of the temporal perspective which is a defining component in the computational form and not just an identifier.

Planning and control inherently rely on dynamic models, both in the derivation of environmental forecasts, and as a basis for the selection of desirable plans. The term $X[t_{p}, (t_{b}, t_{e})]$ , namely a statement X made at $t_{p}$ about the period that begins at $t_{b}$ and ends at $t_{e}$ , seems to provide an appropriate form of reference to temporal data in this context. In general, $t_{p}$ is the as of qualifier—it determines the temporal perspective. Thus, if $t_{p}$ is earlier than $t_{b}$ , the expression reflects a forecast, while if it is later than $t_{e}$ , the expression could reflect a recorded value or an ex-post computed value, possibly part of a retrospective analysis. In the next section we further develop these notions.

## 4. Temporal Information in Control Schemes

THE BASIC MODEL IN SECTION 2 IDENTIFIED eight generic control-oriented “what if” expressions, and presented two basic control schemes that call for a comparison of planned conditions with actual conditions. However:

comparing predicted and actual outcomes can reveal that something went wrong with a plan, but it does little to localize the source of, and the responsibility for the deviations. Controlling all steps of the planning process helps to identify the problem as

being one of erroneous planning data, a faulty planning model, or poor execution. This, in turn, aids in improving the planning process—the primary aim of control. [18, p. 456]

Thus, any attempt to discover the source of the deviations observed through the basic schemes of control has to use a broader selection from the eight computed outcomes. These computations incorporate various versions of retrospective values and provide the basis for performing a retrospective analysis $[1]$ or an ex-post analysis in cost-accounting terms $[14]$ . Retrospective analyses aim to identify and study overall performance deviations and “assign” them to one or more “sources” which include errors in environmental prediction, execution and control failures (failures to maintain or obtain specific programs), measurement and modeling errors (errors or approximations in constructing and using the planning models), and the stochastic nature of some underlying variables ( $[14]$ , p. 12). It should be noted, again, that the view of control processes adopted here is highly normative, corresponding to the conceptual nature of the examination throughout this paper.

Ex-post, or retrospective, analyses differ from traditional, more simplistic techniques mainly in that (1) the basis for comparison is wider—for example, actual results are compared with ex-post optimum results instead of with an either ex-post or ex-ante standard, and (2) all the parameters of the planning model can be effectively incorporated into the analysis [14]. Although there is no disagreement that an ex-post system will provide superior insight, the issue of its adequacy as a managerial evaluation approach is an unresolved one. The core of the debate includes behavioral and ethical reflections, as echoed, for instance, in the discussion that followed the presentation of [18]. Demski, for example, argued for a wider application of this kind of analysis as a basis for performance evaluation in general. To him, the only proper way to assess business results is not against ex-ante standards but rather against ex-post optimum results, based on actual conditions. Further discussion of this issue is clearly beyond the scope of this paper.

The analysis itself concentrates on selected differences. For instance, the difference between the simulated outcomes $S_{112}$ and $S_{111}$ is due to errors in forecasting environmental conditions, as the original model and decisions are kept unchanged. The conceptual simplicity of the framework presented above should not mislead—the number of possible differences is substantial. Moreover, the combinatorial variation of planned and actual values can be applied to all the components that make up the vectors D and E, resulting in a prohibitively high number of (simulated) outputs and their differences. The issue therefore turns to be the identification of sets of values and expressions that are useful in the analysis of performance deviations.

One such type of sets is the so-called complete. A complete set is defined mathematically as a set of partial deviations that sum to the overall deviation. The two equations (presented vertically) in Table 2 exemplify two control schemes based on complete sets of deviations that are “managerially meaningful” [21], in the sense that the individual components of the expressions suggest possible areas for management action. The final selection of a control scheme is primarily based on managerial philosophy and the notion of the “right” or “adequate” method of evaluation. A second concern, typically overlooked, relates to the capability of the information system in place to support such a scheme.

Table 2 Alternative Complete Sets of Partial Deviation Schemes

<table><tr><td>Source of Differences</td><td>Scheme I</td><td>Scheme II</td></tr><tr><td>total deviation</td><td> $O[t_2] - O[t_1] =$ </td><td> $O[t_2] - O[t_1] =$ </td></tr><tr><td>environmental execution</td><td rowspan="2"> $S_{112} - S_{111} + S_{122} - S_{112} + S_{222} - S_{122} + O[t_2] - S_{222}$ </td><td rowspan="2"> $S_{222} - S_{221} + S_{221} - S_{211} + S_{211} - S_{111} + O[t_2] - S_{222}$ </td></tr><tr><td>modelling model&#x27;s noise</td></tr></table>

The unique demand for information put by retrospective schemes has long been recognized: “Quite clearly such an approach requires that we monitor all inputs to the planning model and not just those cost (or cost and revenue) factors present in the optimum program” ([14], p. 202). The more typical discussion of these control schemes simply assumes the availability of the necessary detailed historical information—an assumption that is clearly not supported by common design practices of information system [18, 25].

There are, moreover, some obvious differences among the schemes with respect to the cost of maintaining the involved information. For example, comparison and analysis of the elements that make up Scheme I and Scheme II in Table 2 show that both schemes use the computed outcome of the original plan $O[t_{1}]$ or $S_{111}$ , the actual performance data $O[t_{2}]$ , and the ex-post computed performance $S_{222}$ . The two schemes differ, though, in their demand for historical data in their retrospective components: $S_{112}$ and $S_{122}$ in Scheme I, compared to $S_{221}$ and $S_{211}$ in Scheme II. Although both schemes make use of $D[t_{1}]$ data, Scheme II uses historical environment data, $E[t_{1}]$ , while Scheme I uses the processing model, $M[t_{1}]$ , as it has been perceived at the planning time. An information system designed to cater to control Scheme I will most likely be more concise, as environmental data are typically less compact than model statements. To determine the specific effect of these differences, further case-by-case analysis has to be done.

It should be noted that the two control schemes in Table 2 are very different with respect to the evaluation philosophy that underlies them. Specifically, Scheme I examines performance through the “model lens” that prevailed at the time of planning, but looks more carefully at the way the environment has hampered planning efforts. The second scheme emphasizes the model: namely, it assesses the impact of change in the perception of the process being planned for.

This section has highlighted the fundamental role that mixed temporal expressions play in exercising meaningful control. The expression $X[t_{p}, (t_{b}, t_{e})]$ captures the necessary functional capability to pick and choose elements that differ in their time perspectives $t_{p}$ and allows them to interact with one another to form control schemes. The immediate implications for the design of corresponding information systems is the topic of the next section.

## 5. Implications for the Design of TOIS

THE SECTIONS ABOVE HAVE IDENTIFIED THE BASIC formats of temporal reference to data in the context of planning and control applications. From the vantagepoint of the still evolving set of concerns that constitute “TOIS research,” the above discussion raises three major issues, namely:

1. The maintenance of multiperiod data and the facilitation of complex access to it;

2. The handling of multiple time dimensions of data and the interaction among these dimensions; and

3. The temporal aspects of modeling.

All three are fundamental IS capabilities for planning and control applications, and address two of the three generic components of a decision support system: namely, data and model management $[37]$ . The need to deal with historical data in supporting planning and control decisions has been recognized (e.g., $[25]$ ), and some preliminary discussion of ways to manage such data in the DSS context is emerging (e.g., $[15]$ ). Model management in DSS has been receiving an intensifying attention over the last six or seven years (e.g., $[22]$ ), but has not yet advanced to the point where temporal concerns are treated explicitly.

In this section we further discuss these three themes, identify the concrete problem they posit, evaluate their significance for TOIS design, and briefly relate them to the respective research to date. Although not a comprehensive TOIS research survey (this can be found in $[10, 28, 36]$ ), the discussion leads us to examine critically the state of the art in TOIS research—which is still struggling to find adequate responses to the first issue, has paid minimal attention to the second, and has not even started to address the complexities of the third.

A concrete “real-life” planning problem will serve as a working example throughout this discussion. Consider the following illustrative case of realignment of sales districts contemplated by a major U.S. manufacturer of consumer goods ([25], p.3):

A company currently has 20 sales districts and management wishes to follow the sales of a major brand using a DSS. Now the Sales Division adds an additional district, making 21 districts. A new district, of course, is just pieces of previous districts . . . . Management wants to analyze shipments for the brand over the past two years as if there had always been 21 sales districts.

## 5.1. Temporally Independent Access to Data

Two design issues fall under this category. First, the reference to time in application of planning and control is not an isolated concern but rather an inseparable attribute of the reference to data through the term $X[t_{p}, (t_{b}, t_{e})]$ . Although practically all the involved expressions are explicitly anchored in time, under the prevailing IS design practices, time aspects of data are usually either neglected, implicitly treated, or explicitly factored out [40]. When time is a significant design issue (as in the cases of stocks trading or medical records), temporal aspects are typically handled on an ad-hoc basis to solve a specific problem, and it very often results in the complete concentration on time aspects while knowingly sacrificing other useful views of the data (e.g., [41]).

Second, the unified access to current, historic, and future data is essential and inherent in the conduct of business planning and control. Except for the static models and the most limited control schemes, data and models from different periods are combined and linked together. Thus, data management for these applications assumes a temporally independent access to data which allows the viewing of, and access to, historical data with the same ease that current data are accessed. The prevailing dichotomy of operational versus historical IS designs is thus incompatible with the functional requirements highlighted here (e.g., [25]). Ideally, we should consolidate operational (i.e., short-term) and historical aspects into a single unit of data storage with unified access mechanisms.

Both issues—the maintenance of the temporal context of data and the removal of the traditional distinction between access to current data and access to historical data—are the core concerns in the study of TOIS and their design. The premise of this growing body of research is that there are some major universal attributes of time in information management, and the stated purpose of this research is to articulate correspondingly generalized mechanisms for handling the temporal aspects of data storage and retrieval, as an integral part of, say, a general-purpose DBMS. The above should not be misinterpreted: while some temporal concerns are shared by almost all applications, there will always be some domain- and application-specific temporal terms and concepts. TOIS basically free IS designers from the need to deal with the common aspects of time and enable them to concentrate on those aspects that call for special attention.

These generalized mechanisms—temporally oriented data manipulation languages and corresponding temporally oriented data structures—are typically examined as extensions to the established data management concepts. As of today, the research on TOIS has concentrated mostly on the theoretical underpinnings of these mechanisms (e.g., data models of varying degrees of abstraction), while more limited effort has focused on the development and evaluation of prototypical systems. In the following paragraphs we outline the major themes of this research.

Almost all the attempts to construct a temporally oriented data model, or implement a system based on one, have resorted to a spatial metaphor or imagery for the representation of data over time. The dimensions of such a data cube are objects, attributes, and time, each of which can be directly manipulated by the user. The data cube in figure 1 is a representation of the temporally oriented data structure of the national marketing data in our ongoing example. The cube basically records the entire temporal path of November sales plan. Specifically, it renders graphically a data structure that contains the raw sales plan figures for the different states, for November 1991. For brevity, only four states are listed in the example. For instance, looking at $X[t_p, (t_b, t_e)]$ , where $X$ is NJ-SALES, the initial plan is NJ-SALES[9-27-91,(11/91)]=1650, and after the plan was updated NJ-SALES[10-07-91,(11/91)]=3650. In this data structure the temporal aspects are not factored out but rather perceived as adding depth to the data.

The study of TOIS, primarily of temporally oriented databases, has attempted to translate the “cubic” imagery into well-defined data models. So far the major thrusts of research in this domain have been the extension of the relational model to include temporal components, and the examination of architectures that add time-processing capabilities to the regular relational capabilities. Most of the research embarked from the relational model and added to it data structures and concepts (e.g., [11, 33]), while others have operationalized the cube directly as a “relational-like” conceptual data model (e.g., [4]). The common denominator of this branch of TOIS research is that a traditional relation is extended into a time-relation that contains the history of the objects, that is, all the values that each tuple has acquired over time.

The cubic data structure is then essentially available for direct user manipulations. The operations in the data models mentioned above are typically the basic relational ones, that is, selection (manipulating the object dimension of the cube), and projection (manipulating the attribute dimension), albeit modified to operate within an explicit temporal framework and produce cubes. An additional type of operations manipulates (e.g., restricts) the temporal dimension of the cube. The various temporally oriented conceptual data models have been used as the basis for the design of corresponding query languages. The two major relational query languages—SQL and Quel—have been extended to incorporate temporal elements, and resulted in TOSQL [4] and TQuel [33]. Both avoid penalizing users who are not interested in access to historical data.

While the above is marked by a conceptual perspective, implementation research has focused on the actual construction of experimental TOIS prototypes, translating the conceptual constructs into concrete elements of software and studying their performance $[12]$ . Although it is difficult to discern common themes among these very few efforts, one common concern has been with respect to whether TOIS should be developed from scratch or should extend established data management resources. As one work examined the “from scratch” approach $[13]$ and another built it on top of the relational DBMS INGRES $[31]$ , conclusions are premature.

The current status of the research of temporally independent access to data is surveyed in $[34]$ . As clearly emerges from the survey, the state of the art in the study of TOIS is pre-paradigmatic, and different views are being pursued by different research groups.

![](/api/attachments/E2W7KPSM/fulltext/images/003e071353f05bc71e47667da1fb920b79ee851ed0e15a3017c19b846e267f8e.jpg)  
Figure 1. A Temporally Oriented View of Sales Planning Data

## 5.2. Multiplicity of Time Perspectives

A temporal attribute that is fundamental to the reference to data and models in applications of planning and control is the temporal perspective, $t_{p}$ in the term $X[t_{p}, (t_{b}, t_{e})]$ , which amounts to the statement that there is more than one temporal dimension along which recorded evidence could be viewed and ordered. This stands in sharp contrast to current IS practices, in which time is typically unidimensional—in reference to a single “date line” imagery or the “arrow of time.” Human awareness of events’ occurrence provides a clarifying analogy. There is a fundamental difference between the irreversible, necessarily linear, physiological awareness time (i.e., the inability to “unremember” recorded fact, or “unsee” an already seen view), and the psychological time, in which the cognitive reconstruction of past events is not confined to their original “recording” order [16].

The as of operator—which expresses $t_{p}$ —is an essential element of data manipulation languages that cater to managerial planning and control queries. It also introduces a distinction between database recording time and the time associated with the recorded events themselves. The data in figure 1 were organized along the Planning Time dimension—namely, in a way that reflects the chronological order of the events in the planning process. If, for example, the formal database recording of the adjustment of the sales projections for NJ were delayed until “all other forecasts are in,” the data cube along the actual Recording Time dimension would look rather different, as depicted in figure 2. It should also be noted that the recording of planning data occurs in this example one day after the data is “established” (cf. dates in figure 1). The significance of the difference is demonstrated in the control scenario where one is trying to understand why the NJ sales force did not react any sooner to the revised projections. The explanation is revealed when the data are examined and reorganized as in figure 2: under the assumption that the sales force uses this central database, their new sales forecasts became known only as of 10–16–91, after the successful recording of all revised data.

Multiplicity of time perspectives brings with it a prohibitive complexity. Correspondingly, very little attention has been paid to it so far, although the basic interaction between the two major time dimensions—actual and recording times of an event—has long been recognized as a research issue $[35]$ , and related query language constructs have been proposed. Ad-hoc implementation efforts (e.g., $[7, 41]$ ) typically provide only a single time dimension, and only the basic as of capability: they are capable of reconstructing a “flat” relational snapshot of the data as they existed at a given point in the database’s time. The Time Relational Model (TRM) $[8]$ is somewhat richer with that respect as it defines a Time-View operator that extracts such a snapshot for a specified point in time, as viewed from any specified—possibly different—point in the database’s time. The as-of keyword in TRM is nevertheless limited to a single viewing dimension, the database recording time, and it extracts only a single state. The broader notion of as of as a keyword and operation is fully integrated into the database language defined in $[3]$ , where temporal dimensions are explicitly assignable, specifying the particular time dimension along which the as of qualification is to be interpreted, and allowing the retrieval of whole cubes rather than only single states.

Specifically, as has been argued above, the need to rearrange sets of data temporally is a fundamental planning activity, and planning data may be retrospectively arranged along a number of different time dimensions, for instance:

\- Time of planning: A temporal order that reconstructs the planning process, and presents planning decisions in their original temporal context—reflecting the embedding state of knowledge.

\- Plan's target time: A temporal order that forms the basis for contrasting and comparing actual outcomes with forecasts—the basic feature of retrospective analyses. In our ongoing example this has been “November 1991.”

\- Recording time: According to this temporal order, planning data are tagged with time stamps that are probably sometimes after the time of planning, after which it can be assumed that the plan is known in the organization, and a corresponding adjustments of behavior could be expected.

![](/api/attachments/E2W7KPSM/fulltext/images/cd3e50ad5b1e24f43898e21c97c1308123b706d62781665ce72cd118f0a46ea1.jpg)  
Figure 2. Sales Planning Data along Their Recording Time

This list of time dimensions is by no means exhaustive, and there may be other informative temporal views as well. Current writings in this area at best recognize the importance of this topic (e.g., [35]), but no detailed study of the issues involved has so far been attempted.

## 5.3. Temporally Oriented Model Management

The topic of Model Management has been one of the primary concerns in the research and practice of decision support systems [20]. A model for the purposes of this discussion is a computational construct (i.e., algorithms, equations, or combinations thereof), that is applied to data and generates new data, typically related to as forecasts, summaries, deduced facts, or inferred beliefs. The central theme of model management in the context of supporting managerial decision making is the provision of facilities for the creation, maintenance, and use of a relevant modelbase [37]. Specifically, the technical functions that a model management facility should provide are (1) model abstraction, (2) modelbase storage, (3) model extraction, (4) model integration, and (5) model application [22].

The model management component of DSS is increasingly perceived as serving its users in a way that is analogous to the way in which the data management component serves its users with respect to data. This analogy between the management of computational models and data models has been articulated by a number of researchers (e.g., [9, 19, 26]), and indeed suggests some promising avenues of research. In particular, this conceptual resemblance calls for the examination of the extent to which the lessons from research into temporally oriented management of data apply to the temporally oriented management of models.

Attention to the evolution of models has typically focused on the modeling process itself, namely, the relatively intense periods during which models are developed and shaped, and which end with the release of the model for use. The concern here is broader, and covers primarily the long-term maintenance of models that are being already used and are eventually upgraded, restructured, or otherwise modified. As the expression $M[t_{p}, (t_{b}, t_{e})]$ suggests, model management needs to support temporal aspects, making past versions of models accessible and manipulable in a temporally consistent fashion. Unfortunately, model management itself is one of the least well understood aspects of decision support, which further complicates the study of its temporal aspects. So far it has not been addressed in the TOIS literature.

In the working example throughout this section, an alternative sales districting model is considered. The models in this case are as simple as the lists that define how the various state-by-state figures should be aggregated into sales district summaries. Two such partitioning models are outlined in figure 3, where P[1992] is a modified version of the model P[1983], established some years earlier. Interesting what if scenarios in the process of evaluating the new model could be P[1992]{SALES[1990]} or P[1983]{SALES[1993]}. P[year] could be a part of a more general model, perhaps the final “pass” before the presentation of the computed information.

As amply indicated throughout the paper, managerial planning rests on the capability to apply retrospectively new models and views of historic data: “our ability to plan is strictly a function of our ability to reconstruct the process of temporal change as a function of discretionary acts.” ([39], p. 9). This raises the question of the relationship between a model and its primitive data. The primitive data of a model are the types and instances of data that are either manipulated by the model (e.g., the state-by-state sales figures in our example), or were condensed in formulating its functions (e.g., by the application of averaging or linear regression).

<table><tr><td colspan="2"> $\mathcal{P}[1983]$ </td><td colspan="2"> $\mathcal{P}[1992]$ </td></tr><tr><td>Sales District</td><td>States</td><td>Sales District</td><td>States</td></tr><tr><td>1</td><td>ME, NH, VT, MA</td><td>1</td><td>ME, NH, VT, MA, CT, RI, NY</td></tr><tr><td>2</td><td>CT, RI, NY, NJ PA, OH, VA</td><td>2</td><td>NJ, PA, OH, VA, W.VA.</td></tr><tr><td>3</td><td>...</td><td>3</td><td>...</td></tr><tr><td>⋮</td><td></td><td>⋮</td><td></td></tr><tr><td>20</td><td>OR, CA, NE, AZ</td><td>20</td><td>WA, OR, ID</td></tr><tr><td></td><td></td><td>21</td><td>CA, AZ</td></tr></table>

Figure 3. Alternative Sales Districting Models

It seems that fully supporting planning activities dictates the retention of the most basic level of data recording—only detailed historical data that are “raw” and “primitive” enough will allow the unconstrained application of $P[1992]\{SALES[1990]\}$ as in our ongoing example. In applying the ex-post aggregating model to the ex-ante data, only detailed historical data could be realigned and appropriately re-aggregated upward to a district total. Moreover, as the a priori identification of all possibly useful aggregations is a self defying task, maintaining the data in its raw transaction form seems to be an ideal property of systems that could deal with arbitrary requests for historical information. This largely conforms to the centrality of the notion of event in the research on temporally oriented or historic databases. A survey of related conceptual data models shows a wide agreement that event-based data models should underlie our temporal perception of data, and should be the basic element in TOIS storage [5]. The technical ramifications of such a data management mechanism have not been dealt with so far.

The above simple example highlights the need for establishing a framework for specifying formally what if retrospective analyses. As such analyses become more clearly defined and feasible through temporally oriented data management, attention should be paid to the precise and useful definition of correspondingly advanced modeling (i.e., data manipulation) operators. None of the efforts to study TOIS has dealt with any of the complex data manipulations needed for such temporal what if analyses, let alone formulating them as a single database query. The term $(M[t_{1}]\{D[t_{2}], E[t_{3}]\})$ has put forth a possible approach, through the comprehensive identification of the relevant temporally oriented expressions and data constructs.

In general, the research agenda in this area is very broad. The topic of time seems to pervade many of the areas identified as the major categories of model management research $[23]$ , namely, operations on models, administration of models, model manipulations, as well as policies on model use.

## 6. Conclusion

THE MAINTENANCE OF THE TEMPORAL CONTEXT OF stored, retrieved, and displayed data, evokes design decisions that could not be resolved in conventional ways. Principles of sound information systems design and software engineering suggest that the discussion of the pertinent temporal data management practices should be preceded by an examination of major managerial tasks and the temporal nature of the data they use.

Although the inquiry into the elusive notion of time is extensive (e.g., [30]), the study of temporal issues in management and information systems is still in its formative stages, and our understanding of it is cursory. In narrowing down this undoubtedly broad examination, we have adopted a framework based on team theory—a comprehensive model of organizational decision and control, albeit with an explicit information systems construct [17, 24, 27]. The team theoretic view of information systems exhaustively defines them in terms of four conceptual constructs, namely an observation structure, a communication structure, a memory structure and a delay structure [5]. This partitioning is managerially relevant and at the same time complete with respect to IS design.

This paper has dealt with questions pertaining to the memory structure of information systems. The notion of memory is especially central to the ability to relate to time—the two concepts have no meaning independently. Further focusing the inquiry, we examined some aspects of planning and control, and derived related requirements and functional criteria that designers and students of TOIS should address. Reviewing current TOIS research against these concepts reveals that it is only beginning to respond to the complexity of actual managerial tasks as planning and control applications.

The frameworks that guided this paper further indicate where additional efforts should be made. The dialog–data–model management view of DSS [37] calls for the study of the dialog aspect of TOIS in general, and in applications of planning and control in particular. The topic was only skirted in the section on model management—the development of what if commands is in part a dialog-design issue. The nature of the interface between TOIS and their users has received only minimal attention so far (e.g., [3, 29]). The team theoretic framework seconds the need to study the dialog aspect of TOIS as part of what it refers to as the communication structure. The other structures—namely, observation and delay—also need much more detailed study. The former relates to the fundamental nature of the facts that information systems “notice,” while the latter relates to the inevitable effect of delay in noticing and recording facts in information systems [5]. Time plays a significant role in information systems, but our understanding of the issues involved is only preliminary.

## REFERENCES

1. Ackoff, R.L. Creating The Corporate Future. New York: John Wiley, 1981.

2. Applegate, L.M.; Chen, T.T.; Konsynski, B.R.; and Nunamaker, J.F., Jr. Knowledge management in organizational planning. Journal of Management Information Systems, 3, 4 (Spring 1987), 20–38.

3. Ariav, G. Preserving the Time Dimension in Information Systems. Ph.D. dissertation, Decision Sciences Department, University of Pennsylvania, December 1983. [Available as Tech. Report DS-WP 83-12-06.]

4. Ariav, G. A temporally oriented data model. ACM Transactions on Database Systems, 11, 4 (December 1986), 499–527.

5. Ariav, G. Design requirements for temporally oriented information systems. In C. Rolland, F. Bodart, and M. Leonard (eds.), Temporal Aspects of Information Systems. Amsterdam: North-Holland, 1988, pp. 3–16.

6. Ariav, G., and Ginzberg, M.J. DSS design—a systemic view of decision support. Communications of the ACM, 28, 10 (October 1985), 1045–1052.

7. Ariav, G., and Morgan, H.L. MDM: Handling the Time Dimension in Generalized DBMS. Technical Report DS-WP 81-05-06, Decision Sciences Department, University of Pennsylvania, May 1981.

8. Ben-Zvi, J. The Time Relational Model. Ph.D. dissertation, Department of Computer Science, University of California, Los Angeles, 1982.

9. Blanning, R.W. A relational theory of model management. In C.W. Holsapple and A.B. Whinston (eds.), Decision Support Systems: Theory and Applications. Berlin: Springer Verlag, 1987.

10. Bolour, A.; Anderson, T.L.; Dcketser, L.J.; and Wong, H.K.T. The role of time in information processing: a survey. ACM SIGMOD RECORD, 12, 3 (April 1982), 28–48.

11. Clifford, J. A Logical Framework for the Temporal Semantics and Natural-Language Querying of Historical Databases. Ph.D. dissertation, Department of Computer Science, State University of New York at Stony Brook, December 1982.

12. Clifford, J., and Ariav, G. Temporal data management: models and systems. In G. Ariav and J. Clifford (eds.), New Directions for Database Systems. Norwood, NJ: Ablex Publishing, 1986, pp. 168–185.

13. Dadam, P.; Lum, V.; and Werner, H.D. Integration of time versions in relational database systems. In Proceedings of the Tenth International Conference on Very Large Data Bases, VLDB Endowment, 1984, pp. 509–521.

14. Demski, J.S. Analyzing the effectiveness of the traditional standard cost variance model. Management Accounting, 48 (October 1967), 9–19.

15. Diehr, G.; Saharia, A.; and Chao, D. Maintaining remote decision support databases. Journal of Management Information Systems, 7, 2 (Fall 1990), 111–138.

16. Dobbs, H.A.C. The dimensions of the sensible present. In J. Fraser et al. (eds.), The Study of Time (rpt). Berlin: Springer Verlag, 1972, pp. 274–292.

17. Emery, J.C. Organizational Planning and Control Systems: Theory and Technology. New York: Macmillan, 1969.

18. Emery, J.C., and Ness, D.N. A man-machine budgeting system. In C.H. Kriebel, R.L. Van Horn, and J.T. Heames (eds.), Management Information Systems: Progress and Perspectives. Pittsburgh: Carnegie Press, 1971, pp. 447–480.

19. Geoffrion, A.M. An introduction to structured modeling. Management Science, 33, 5 (May 1987), 547–585.

20. Holsapple, C.W., and Whinston, A.B. Model management issues and directions. In E.A. Stohr (ed.), Proceedings of the Workshop on Information Systems and Decision Processes, University of Arizona, Tucson, October 1989, pp. 1–55.

21. Hurst, E.G. A Generalized Approach to the Analysis of Accounting Deviations. Technical ReportDS-WP 79-06-01, Department of Decision Sciences, University of Pennsylvania, June 1979.

22. Klein, G.; Konsynski, B.R.; and Beck, P.O. A linear representation for model management in a DSS. Journal of Management Information Systems, 2, 2 (Fall 1985), 40–54.

23. Konsynski, B.R., and Sprague, R.H. Future directions in model management. Decision Support Systems, 2, 1 (1986), 103–109.

24. Kriebel, C.H., and Moore, J.H. Economics and management information systems. In E.R. McLean (ed.), Proceedings of the First International Conference on Information Systems, Philadelphia, December 1980, pp. 19–31.

25. Laning, L.J.; Walla, G.O.; and Airaghi, L.S. A DSS oversight—historical databases. In G.W. Dickson (ed.), DSS–82 Transactions, June 1982, pp. 87–95.

26. Lenard, M.L. Representing models as data. Journal of Management Information Systems, 2, 4 (Spring 1986), 36–48.

27. Marschak, J., and Radner, R. Economic Theory of Teams. New Haven, CT: Yale University Press, 1972.

28. McKenzie, E. Bibliography: temporal databases. ACM SIGMOD RECORD, 15, 4 (December 1986), 40–52.

29. Shannon, K. The Display of Temporal Information. Technical Report 86–019. Department of Computer Science, University of North Carolina, Chapel Hill, July 1986.

30. Sherover, C.M., ed. The Human Experience of Time. New York: New York University Press, 1975.

31. Shiftan, J. Assessing the Temporal Differentiation of Attributes as an Implementation Strategy for a Temporally Oriented Relational DBMS. Ph.D. dissertation, Department of Information Systems, New York University, December 1986.

32. Snodgrass, R. A Temporal Query Language. Technical Report 85–013, Department of Computer Science, University of North Carolina, Chapel Hill, May 1984.

33. Snodgrass, R. The temporal query language TQuel. ACM Transactions on Database Systems, 12, 2 (June 1987), 247–298.

34. Snodgrass, R. Temporal databases: status and research directions. ACM SIGMOD RECORD, 19, 4 (December 1990), 83–89.

35. Snodgrass, R., and Ahn, I. Temporal databases. Computer, 19, 9 (September 1986), 35–42.

36. Soo, M.D. Bibliography on temporal databases. ACM SIGMOD RECORD, 20, 1 (March 1991), 14–23.

37. Sprague, R.H., and Carlson, E.D. Building Effective Decision Support Systems. Englewood Cliffs, NJ: Prentice-Hall, 1982.

38. Tapiero, C.S. Managerial Planning: An Optimum and Stochastic Control Approach. New York: Gordon and Breach Science Publishers, 1977.

39. Tapiero, C.S. Time, dynamics, and the process of management modelling. TIMS Studies in Management Science, 9 (1978), 7–31.

40. Tsichritzis, D.C., and Lochovsky, F.H. Data Models. Englewood Cliffs, NJ: Prentice-Hall, 1982.

41. Wiederhold, G.; Fries, J.F.; and Weyl, S. Structured organization of clinical databases. In Proceedings of the NCC. Montvale, NJ: AFIPS Press, 1975, pp. 479–485.
