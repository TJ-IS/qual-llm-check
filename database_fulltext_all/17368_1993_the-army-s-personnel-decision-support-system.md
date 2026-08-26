---
otero_id: 17368
otero_key: "VAQQXCMZ"
title: "The Army's personnel decision support system"
authors: "Henry S. Weigel; Steven P. Wilcox"
year: "1993"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(93)90059-c"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Army's personnel decision support system

Henry S. Weigel and Steven P. Wilcox
General Research Corporation, Vienna VA, USA

The Army's enlisted personnel decision support system combines a variety of modeling techniques, such as goal programming, network models, linear programming, and Markov-type inventory projection, with a management information system to support analysis of personnel planning issues. Using a hierarchy of models, personnel planning decisions are coordinated from the macroscopic, public policy level to the very detailed, unit and military occupational specialty level. This decision support system employs models that combine the full range of modeling methodologies with mechanisms to assure integration between organizational levels.

Keywords: Personnel modeling, Decision support systems, Goal programming, Network flow modeling, Manpower planning, Military manpower models, Markov (transition rate) personnel models.

![](/api/attachments/VAQQXCMZ/fulltext/images/4b8def9f1588ac69c6890b020fc5d7bfc7bad912cf0308f4a9eb97f21e101719.jpg)

Henry S. Weigel received his BS in Mathematics and Physics from the University of Wisconsin in Milwaukee in 1961, and his M.A. in Mathematics from the University of Maryland at College Park in 1969. He has undertaken graduate studies in Operations Research at the George Washington University, Washington, DC. He has been the Technical Director of a 170-member system development group at the General Research Corporation where he directed the modeling efforts of several manpower/personnel management systems that were developed for the U.S. Army. He is presently the Special Assistant for the Director of the Office of Energy Markets and End Use at the Energy Information Administration, U.S. Department of Energy.

## Introduction

Over the past 20 years the General Research Corporation (GRC) has been involved in the design and development of mathematically-based, computerized personnel forecasting systems for the Army. These systems, which are components of the Army's Personnel Decision Support System (PERDSS), provide automated management tools at various levels of detail and in response to a variety of functional needs of the Army managers. The development of the Enlisted Loss Inventory Model (ELIM) and the COnputation of Manpower Programs using LLinear Programming (COMPLIP) model was in response to the need for the automated and accurate projection of trained strength, operating strength, accessions, reenlistments, and losses for the active Army. The Military Occupational Specialty Level System (MOSLS) was developed to provide an improved automated management tool at the MOS and grade levels of detail, accounting for such variables as active Army enlisted strengths, gains, losses, promotions, reclassifications, conversions, and training. The Unit Level System (ULS), currently in the final stages of system acceptance testing, will provide a management tool to deal with the various aspects of active Army enlisted force distribution. A system (CIVFORS) has been designed and developed to provide a decision support tool managing civilians employed by the Army. Finally, two systems have been developed to provide the Army with decision support capability to manage the officers in the active Army. The Officer Projection Aggregate Level System (OPALS) provides the capability to forecast strengths, accessions, promotions, and losses by competitive category, grade, and years of service. The Officer Projection Specialty System (TOPSS) is constrained to the solution provided by OPALS and will support the life-cycle management functions of classification, promotion, training, force alignment, and loss management. OPALS is an operational system and TOPSS is in the final stages of system acceptance testing.

![](/api/attachments/VAQQXCMZ/fulltext/images/d80f636ea2ba611223638d909b6918a5dafb83973bfd6d9f1b6e5bf25454af25.jpg)  
Steven P. Wilcox has received a M.A. Sociology in 1984 and a Ph.D in Operations Research in 1987 from the University of North Carolina at Chapel Hill, with a dissertation in combinatorial optimization. He is currently a Senior Analyst at General Research Corporation, developing enhancements to ELIM and MOSLS, two of the systems described in this article.

To the functional manager the problem may be expressed as the need for automated tools to assist him in performing management, policy analysis, and planning functions. Thus, the range of capabilities of such tools spans the spectrum of functions of personnel and manpower managers employed by the Army. For example, different concerns are represented by functional managers dealing with the enlisted force as opposed to the officer or civilian forces. For the enlisted force further differences in concerns are represented by functional managers dealing with the active Army from those responsible for the Reserve Components (RC). It is not surprising, then, that the PERDSS master plan has identified the major modules associated with the projection of Army strength and personnel management actions. The individual modules actually form a family of Automated Data Processing (ADP) modules being linked by means of a system management module (SMM), the PERDSS data base, and a management information system (MIS).

The discussion in this paper is illustrated with examples from the modeling techniques associated with the automated management tools addressing the needs of the active Army enlisted force. Before any management tool (or computerized mathematical model, or simply model) can be conceptualized, the problem needs to be analyzed from the following perspectives:

\- Functional needs

\- Availability of data

\- Level of detail

• Operations research techniques

• Computer technology

\- Organizational support

A hierarchical approach in modeling is used. It is defined here as the process of representing a large problem in the form of a sequence of linked models. Each echelon of the hierarchy provides certain pre-defined constraints for the next lower echelon. The top echelon is where global optimization may occur. Each subsequent echelon may perform optimization as permitted by the constraints of the higher echelons. The reason for a hierarchical system is that each echelon focuses on a different set of dimensions. When considered together as one model, the combined set of dimensions define a problem that is beyond the scope of present-day operations research and computer technology.

As an example, the PERDSS enlisted system consisting of ELIM-COMPLIP, MOSLS, and ULS form a hierarchical system. The role of ELIM-COMPLIP is to determine the number of accessions, losses, reenlistments and strength by month, for seven years defined as the current year, the budget year, and the program objective memorandum years representing the five year defense plan. The particular focus of ELIM-COMPLIP is on accuracy of projections and flexibility of policy implementation at the aggregate level. Aggregate level here simply means that functional dimensions such as military occupational specialty (MOS), grade, and unit are not considered in the model. The model, however, is quite large because other dimensions that influence loss and reenlistment behavior, and measure the maturity and stability of the force are represented. The projection technique in ELIM-COMPLIP consists of personnel inventory projection coupled with a linear programming formulation. Uniformity of loss behavior in inventory cells is captured by structural dimensions, by demographic characteristics of accessions, and by identifying the cause of loss.

The driving force of ELIM-COMPLIP is the force structure allowance. The monthly force structure allowance values serve as targets for the projection of operating strength. The objective of the LP optimization is to determine the accessions each month such that the sum of the absolute values of the deviations of the projected operating strengths from the strength targets is minimized.

The role of MOSLS is to forecast the enlisted force at the MOS and grade level of detail, subject to the aggregate quantities of gains, losses and immediate reenlistments projected by E-LIM-COMPLIP. MOSLS deals with such personnel actions as gains, losses, reclassifications, conversions, promotions, and training. MOSLS itself is a hierarchical system. The top echelon, known as the T-Model, represents training time groups (i.e., groupings of MOSs that are functionally related and have similar training times) and grades. Each training time group is wholly contained in one career management field. The model is a multi-time-period linear optimization (LP with a large embedded network) model using strength targets at the appropriate level of detail that are consistent with the targets used in ELIM-COMPLIP. The objective is to determine such decision variables as trainee graduates, promotions, and reclassifications so as to project strengths as close to the targets as possible.

The second MOSLS echelon consists of a series of models, each representing the 3-character MOSs and grades of a career management field. The formulation is a multi-time-period pure network representing personnel flows similar to those of the T-Model (but at the MOS and grade level of detail) and constrained by the aggregate flows of the T-Model.

The role of ULS is to forecast the enlisted strength and distribution actions at the MOS, grade, and unit level of detail for the current year, the budget year, and the first year of the five year defense plan. These forecasts are constrained by the MOSLS forecasts. The result is the enlisted distribution plan. The refinement for 12 projection months form the basis for generating requisitions. The forecasting process is a heuristic one with suboptimization each time period.

During the course of the 20 years of design and development of personnel forecasting systems, certain modeling approaches have evolved that have produced results with proven accuracy and functional responsiveness. However, there is no single document that discusses these modeling approaches, with their key methodological and design features, from a cause and effect perspective.

The purpose of this paper is to define clearly the proven modeling methods and to discuss the reason for their effectiveness. This is accomplished by focusing on the problem context as well as modeling techniques. Simple examples are used to explain the various techniques. This paper consists of a brief section on the background of Army personnel modeling, a presentation of the global problem, a discussion of the hierarchical approach to problem definitions, data considerations, and several sections on modeling techniques.

## Overview of manpower modeling methods

A variety of tools from demography and operations research have been adapted to the task of modeling manpower in military organizations. To be useful in a military setting these models have been elaborated and combined in a wide variety of ways. Military manpower modeling systems can be categorized on the basis of the level of detail used, and how features of the basic models are combined.

The basic tool in manpower modeling is inventory projection, also called the transition rate (Markov) model. This technique is an elaborate version of a very old demographic and actuarial technique called life table projection $[1,13]$ . In a basic life table, the first row starts out with 100,000 births, and applies a death rate to get the number of people projected to start their second year of life. A death rate is applied in turn to these, and the survivors appear in the next row. This table therefore gives the proportion of the original population surviving to any given birthday. A life table projection can be used to project the number of deaths to expect in a population given a certain age distribution. This concept has been greatly enhanced so as to create a wide variety of elaborations, such as multiple decrement life tables (perhaps giving the female population that is alive and single).

In military manpower modeling, the population is often finely divided into cells. It is frequently necessary to model the force by year of service as well as time to the end of service, for example. Rank and military specialty are other prime candidates for appearance as dimensions. Multiple causes of loss, such as end of term, attrition, or retirement are considered separately. The result is a large tracking matrix in which the processing of loss types alternates with an aging mechanism. The challenge posed by this technique is that the number of cells in the tracking matrix, and consequently the processing time, increases exponentially with the number of dimensions. Inventory projections fit in with the “what if?” concept for decision support systems very well, as the projection assumptions are input and the projection is the output.

Manpower models also frequently use some form of linear program (LP). This is an optimization model in which one designates numeric variables with specified ranges for their values, and maximizes or minimizes some linear formula subject to the restriction that a whole list of equations be satisfied. These may be equalities or inequalities. For example, we might write

$$
\begin{array}{l l} \mathrm {z^ {*} = maximize} & \mathrm{x+2y+3z} \\ \text {such that} & \mathrm {x + y + z = 2 ,} \\ & 2 \mathrm{x} \quad + \mathrm {z\leq 3}, \\ & 0 \leq \mathrm{x} \leq 2, \\ & 0 \leq \mathrm{y} \leq 1, \text {and} \\ & 0 \leq \mathrm{z} \leq 1. \end{array}
$$

In ELIM some of the variables represent non-prior service gains, and retention (survival) rates appear as coefficients in the constraints. Thus ELIM takes life table data and incorporates it into the linear programming formulation. Thus the linear program has an inventory projection function. Linear programs are conceptually more complex than inventory projections, and have a tendency to be treated as decision-making systems, as the formulation attempts to find what is best subject to a set of constraints.

The advantage of linear optimization techniques over non-linear is that they are capable of accommodating considerably larger problems. A good indicator of problem size is the number of constraints represented in the model structure. The problems encountered in the FORECAST development work have had as many as 12,000 constraints. Non-linear problems are considered fairly large with 100 constraints. One may think that very few problems in the real world are linear. In the strictest sense that is true. However, with the use of piece-wise linear approximations of nonlinear objective functions and advanced LP solution procedures, LP formulation is practical.

An optimal solution of an LP represents the best course of management actions as defined by the decision variables (e.g., accession variables) toward achieving the stated goal, defined by the objective function. Thus, in military manpower models, the optimal solution is not only a projection of strengths, gains, and losses but a prescription of management actions (e.g., recruiting goals). The solution is determined simultaneously over all dimensions represented, making the strengths, gains, and losses consistent with each other. The terms strengths, gains, and losses may be thought of in terms of each population inventory cell. Thus, an immediate reenlistment action is represented as a loss to some cells and a gain to others.

Most manpower linear programs have a network structure as a substantial portion of the formulation. A network LP is conceived of as a set of nodes connected by arcs. The nodes serve as switching and pumping stations and the arcs serve as pipes. These pipes have bounded capacity. Unless a node has a supply or demand in it, the amount of flow going in is equal to the amount going out. The switching stations direct the flow so as to maximize or minimize the objective function, which is given by per-unit costs on flow in each pipe. In military manpower modeling applications, the network structure represents the flow of people and their status at different times.

The disadvantage of network modeling is that many decision constraints cannot be represented in a network formulation. However, there are significant advantages because of the limited structure. Special solution codes, taking advantage of the network structure, have been developed that are significantly faster and can accommodate much larger problems than the general LP codes.

The flows on the arcs of a pure network are integer valued. They may be controlled by means of upper and/or lower bounds. Incentives or penalties may be placed on the arcs to encourage or impede flow, respectively. These incentives and penalties are referred to as pseudo-costs, or simply costs: negative and positive costs, respectively. When the Objective is to minimize, negative costs on arcs are the driving force of a network flow model.

Another commonly used linear programming feature is goal programming. Goal programming is a feature of the objective function in which a number of variables are targeted towards objectives. For example, endstrength is frequently a subject of goal programming. For example, there might be a target for the number of infantrymen, and small deviations get a small penalty per unit deviation. Outside a certain range, the penalties are much larger. The object is to get as close to the right number of infantrymen, tank crew members, etc. as possible. Goal programming is easily modeled within a network structure, in which inventory flows along several target arcs placed between two nodes. Under the target, the arcs have incentives, but over the target, the arcs have penalties. Frequently there is a multicriteria feature in which one has a prioritized set of objective functions. Applications of goal programming include those by Charnes, Cooper, and Niehaus [4,6] and Charnes, Cooper, and Ferguson [3]. Gass, et al. [7] present a model that combines the goal programming and the Markov inventory projection model. Computational aspects of multicriteria goal programming are presented in Klingman and Phillips [11].

Multicriterion goal programming is used to support decisions in which there is a definite hierarchy of prioritized goals, such as commonly occur in the military. First the optimal objective function with respect to the first priority goal is found. However, there may be alternative optimal solutions, in which case, the procedure finds the one that best satisfies the second objective. Any number of objective functions may be considered. This procedure enables one to assure decision makers that trade-offs are not being made between objective functions, as happens when the objective functions combines goals.

Another common modeling idea is the transportation problem, which is a kind of network. This arises if you are supplied with an assortment of soldiers with various classifications, and have demands created by the need to fill positions. The soldiers are represented as supplies sitting on nodes, and the jobs are demand nodes. If soldiers of a certain classification can fill a particular job, then an arc representing assignment connects the two nodes. The volume of flow is the number of soldiers assigned. If there are intermediary nodes in the network it is called a transshipment problem. Transshipment models frequently appear in the literature on optimal personnel assignment or detailing. Applications of network transportation/transshipment models include those by Thompson [17] and Charnes and Cooper [2].

Military problems frequently have a projection horizon of a number of years. Thus arcs can be used to model the aging of soldiers each year. Since losses occur with time, it is natural to employ a type of arc in which more goes in than goes out. This models losses that are proportional to the strength partition. This is called a generalized arc, and a network with generalized arcs is called a generalized network. Examples of applications of generalized networks include Charnes, Cooper, and Niehaus [5].

## Background (Holz and Wroth [8])

## The need for COMPLIP

During the 1960's, the Office of the Deputy Chief of Staff for Personnel (ODCSPER) was charged with the responsibility of providing each month to the Army Chief of Staff and Secretariat a chart that showed monthly forecasts of Army trained strength (with operating strength a sub-category) and projected accessions, both draftee and volunteer. Also shown were targets for the trained strength, which were derived from assumptions about the force structure, and the projected monthly differences between trained strength and targets.

The Assistant Secretary of the Army (Manpower and Reserve Affairs), William K. Brehm, found the format of this chart useful for addressing a variety of “what if” questions related to manpower policies as different plans for Vietnam came under considerations. Since each alternative considered required manual computations that took as many as 8 to 20 hours (referred to as “one Pentagon day”) to complete, the need to automate these computations was recognized and in December 1969 Research Analysis Corporation (RAC) was asked to perform this service on a “crash” schedule. (In September, 1972, the General Research Corporation acquired the research staff and contractual obligations of the Research Analysis Corporation.)

During the three weeks allotted, two models were developed. One was the requested simulation of the manual procedures, and the other was an optimization model named COMPLIP. The objective function of the COMPLIP linear program minimized the weighted sum of the absolute values of the deviations of projected trained strength from the targets. This is an accurate representation of the objective of Army personnel managers to maintain the Army's strength as close as possible to prescribed levels, and when the operative constraints make it impossible to eliminate deviations, to provide some control over their timing and direction (i.e., overstrength versus understrength).

Fig. 1 illustrates one of the early applications of COMPLIP [12]. The targets associated with this application prescribed a decrease in trained strength over the succeeding two years. The manually computed program was overstrength during most of this period, while the COMPLIP-generated program matched the targets much more closely. Further, COMPLIP could readily incorporate constraints that were difficult even to approximate by manual methods – e.g., a requirement to be exactly on target at the end of the fiscal year, as indicated in the figure (FY73), and limits on manyears (or average strength). COMPLIP not only provided the desired responsiveness for examination of policy alternatives, but pointed the way to increased efficiency in the programming of manpower resources with, for example, the previously cited application leading to a saving of 5000 trained manyears to man a prescribed force structure.

COMPLIP served as a decision support system by modeling enlisted strength in a limited, but structured way. It does not model the complete picture, which includes training, tour rotations, military occupational specialties, and rank, but concerns enlisted accessions by demographic category and strength targets. By replacing the use of manual procedures, it enabled the Assistant Secretary's office to develop several hundred alternatives [9].

One of the benefits provided by COMPLIP during 1970 was in the area of draft policy. The draft was, of course, a highly sensitive political issue. The Army had been issuing draft calls that fluctuated widely from one month to the next, adding fuel to the controversy. COMPLIP could readily impose upper and lower bounds on draft calls to reduce the fluctuations. Subsequently, as operations in Vietnam were phased down, this capability was extended to the imposition of a “no-rise” rule on draft calls.

## COMPLIP as a decision support system

The difference between the initial results obtained from COMPLIP and those from the manual procedures resulted from differences in the solution procedures rather than in the models themselves. The basic relationships among variables initially were essentially the same in both methods. The manual computations attempted by trial and error to adjust an earlier manpower program (projected draft calls and their effects) to changes in specifications, such as new targets for the Army's operating strength.

COMPLIP enables the manpower planner to address the strength management process in a structured way. The linear programming (LP) model formulation gives the problem in terms of an objective function, constraints, and equations that describe the projected strength of the Army as a function of accessions. COMPLIP is a goal programming model that permits the user to specify a sequence of objectives to be applied in priority order. While the formulation imposes a structure on the decision maker, he has the opportunity to experiment with different combinations of user controls. The different alternatives thus produced can be compared using exterior criteria.

![](/api/attachments/VAQQXCMZ/fulltext/images/02f69d58487daa0c7e16a0e6a5113cc912763aaaec0d98a97473eb393d00e734.jpg)  
Fig. 1. Example of an early COMPLIP application.

## The need for ELIM

During the initial period of COMPLIP use, the projection of losses to the force was introduced into the manpower program with the use of methods representing the automation of manual procedures developed several years earlier. Accurate projection of losses is an essential ingredient for the accurate projection of strength.

In FY72, the Army was in the process of phasing down from Vietnam. Strength at the beginning of the year was about 1.3 million, and the Army plan called for this to drop to about 1.1 million by the end of the year. Shortly after the beginning of the fiscal year, the Congress passed an authorization bill which reduced the Army's average strength for the year by 50,000. This cut in average strength meant that the phase-down plan had to be accelerated significantly, to a strength at year end of about 900,000.

At the beginning of FY72, the Army was 4,000 over the strength that had been projected one month earlier. A month later the Army was 8,000 overstrength, and the month after that 16,000 over what had been projected one month earlier.

At this point, the problem had reached crisis proportions. The overstrength condition in the early months of the fiscal year meant that even greater strength cuts were needed to keep the average within the Congressional ceiling. Drastic policies had to be instituted, which not only disrupted personnel management but also caused the strength of units to fall well below what was authorized. Readiness throughout the Army was crippled, and the Army ended the fiscal year more than 50,000 below the desired end strength. (See fig. 2.)

curve (b) is the plan revised to comply with a Congressional cut of 50,000 of average strength, and
curve (c) represents the actual strength.  
![](/api/attachments/VAQQXCMZ/fulltext/images/2ccbbbff26d6f8873b3b3a11c84a461958204c08e9e8066566e9d282439da41e.jpg)  
(Note that the congressional limit was 972,000 AVERAGE strength for the year.)
Curve (a) is the original Army plan,  
Fig. 2. Illustration of a manpower management problem associated with poor strength forecasting.

## The means

In response to this crisis, the Research Analysis Corporation developed as quickly as possible a new method of projecting losses, ELIM. ELIM development started in late 1971.

The first full-scale test of the initial version of ELIM was made in July 1972, using a data base extending only through June 1971. The forecast of losses for each of the months of FY72 could then be compared with the known actual losses for this period, as well as with the projections made by the procedures that ELIM was designed to replace. The ELIM forecast, which extended for 12 months ahead of the data base used for the projection, was compared, month by month, with forecasts made by the existing system, where the latter forecasts were made for just one month ahead of the latest known actuals. Happily, the comparison was very favorable to ELIM, with errors ranging from 0.1 to 0.5 of the corresponding errors of the other system [10].

The development of ELIM-COMPLIP met the immediate needs of Army manpower planners. With its use, other needs were identified and ELIM-COMPLIP underwent a series of modifications to add capabilities to meet increasing needs of Army analysts. It soon became clear that ELIM-COMPLIP was a good personnel and management action forecasting tool for the active Army, at the aggregate level. However, more than ELIM-COMPLIP was needed.

## The problem

To the functional manager, the problem may be expressed as the need for automated tools to assist him in performing management, policy analysis, and planning functions. Thus the range of capabilities of such tools spans the spectrum of functions of personnel and manpower managers employed by the Army. For example, different concerns are represented by functional managers dealing with the enlisted force as opposed to the officer or civilian forces. For the enlisted force further differences in concerns are represented by functional managers dealing with the Active Army from those responsible for the Reserve Components (RC). It is not surprising, then, that the Army has established the FORECAST (PER-DSS) Office to consolidate the personnel system development efforts in order to make use of technology from successful efforts in other areas and to ensure consistency and integration of these systems. The FORECAST master plan has identified the major modules associated with the projection of Army strength and personnel management actions. The individual modules actually form a family of Automated Data Processing (ADP) modules being linked by means of a system management module (SMM), the FORECAST data base, and a management information system (MIS).

## Functional needs

The needs of the functional manager must be identified for incorporation into the model design. For example, accurate projection of strength, gains, and losses at various levels of detail is of paramount importance. Associated with these projections is the need for projections of other personnel actions such as reenlistments, reclassifications, promotions, distributions, and training programs. The offices associated with these different actions need to work from a realistic and consistent set of numbers. Through the publication of model outputs in the MIS, PERDSS plays a major role in achieving this coordination. The needs of these functional users spans the whole range of detail from the global picture of All-Army operating strength to that of tour rotation of soldiers with a particular occupational specialty into individual units.

Producing a single optimization model that encompasses all the desired variables is clearly not possible. Such a model would be enormous, as the number of variables in the model grows very rapidly with the degree of detail. For example, a generalized network LP that optimizes and projects strength and losses on a monthly basis for 70 months and 1,500 MOS and pay grade combinations would have 105,000 nodes, and still fail to model attrition losses as a function of year of service, or to model months to the end of the term of service. The addition of each subdivision exponentially increases the size of the model. At the time that the PERDSS models were designed, the limit on LP size was imposed by IBM's MPSX and Ketron's MPSIII at 16,000 constraints. A set of models that break the overall problem into manageable pieces and yet achieve consistency and credibility from a wide variety of organizational viewpoints is the goal, however. Fundamental to such a system is accurate and consistent data.

In 1985 General Maxwell R. Thurman, the Army's Vice Chief of Staff (VCSA), initiated a special effort to accelerate and facilitate the integrated development of Army Decision Systems – systems used to support the decision process at Headquarters, Department of the Army (HQDA). He directed senior Army leadership to make use of the FORECAST Development Office's success in developing integrated personnel policy and management decision systems by following the template of FORECAST to assist the Army staff agencies in their efforts to build systems to meet their management needs. He gave FORECAST the additional responsibility to integrate existing and developing decision systems and further to develop the “Integration Policy System” (IPS), a system that was to be the central objective setting and resource allocation tool used by the Army leadership.

By 1986, FORECAST had outgrown its personnel roots and, at the suggestion of the Assistant Secretary of the Army (Manpower and Reserve Affairs), (ASA(M & RA)), was reassigned to the Office of the Chief of Staff of the Army (OCSA), under Director of Management (DM). Under the DM, the FORECAST functions were transferred to the Decision Systems Management Office (DSMO). Later this was made the Decision Systems Management Agency (DSMA) with a DSMO established within each HQDA staff agency. The “personnel” part of FORECAST became the DSMO of the Office of the Deputy Chief of Staff for Personnel (ODCSPER) and retained the name FORECAST. The role of the DM as policy maker for information systems within HQDA was formalized and the DSMA was designated as the single integrator of information systems at HQDA. The Army has provided outstanding support for the development of its DSS.

## Hierarchical approach

Sprague and Carlson [16] present the concept of a network of interrelated models as part of the DSS concept. The network of models used in the FORECAST enlisted system consisting of ELIM-COMPLIP, MOSLS, and ULS is hierarchical. Each echelon of the hierarchy provides certain, pre-defined constraints for the next lower echelon. The top echelon is where global optimization may occur. Each subsequent echelon may perform optimization as permitted by the constraints of the higher echelons. The reason for a hierarchical system of models is that each bureaucracy within the Army focuses on a different set of dimensions. The manager in charge of tour rotations in a unit is not, and cannot be concerned with the All-Army accession and strength picture or the number of training seats planned for a particular MOS. The hierarchical set of models supports the need of decision-makers to plan according to consistent sets of numbers.

In the enlisted system hierarchy, the role of ELIM-COMPLIP is to determine the number of accessions, losses, reenlistments and strength by month, for seven years defined as the current year, the budget year, and the program objective memorandum (POM) years representing the five year defense plan (FYDP). The particular focus of ELIM-COMPLIP is on accuracy of projections and flexibility of policy implementation at the aggregate level. Aggregate level here simply means that functional dimensions such as military occupational specialty (MOS), grade, and unit are not considered in the model. The model, however, is quite large because other dimensions that influence loss and reenlistment behavior, and measure the maturity and stability of the force are represented. The projection technique in ELIM-COMPLIP consists of personnel inventory projection coupled with a linear programming formulation. Uniformity of loss behavior in inventory cells is captured by structural dimensions, by demographic characteristics of accessions, and by identifying the cause of loss. To illustrate, consider the structural dimensions of time in service, and months to ETS; the causes of loss of various types of attrition (including the trainee discharge program (TDP)), separation at ETS, and non-disability retirement (NDR); and the characteristics of accessions of high school diploma graduate (HSDG) and non-HSDG (NHSDG). TDP losses occur during the early months of service, with more from NHSDG accessions than HSDGs. ETS losses occur in the months near the ETS month. Populations with 20 or more years of service are the source of NDR losses.

The driving force of ELIM-COMPLIP is the Force Structure Allowance (FSA). The monthly FSAs serve as targets for the projection of operating strength. The operating strength is equal to the total strength less the trainees and the individual accounts, commonly referred to as TTHS (trainees, transients, holdees, and students). The objective of the COMPLIP optimization is to determine the accessions each month such that the sum of the absolute values of the deviations of the projected operating strengths from the FSA strength targets is minimized.

The role of MOSLS is to forecast the enlisted force at the MOS and grade level of detail, subject to the aggregate quantities of gains, losses and immediate reenlistments projected by E-LIM-COMPLIP. MOSLS deals with such personnel actions as gains, losses, reclassifications, conversions, promotions, and training. In order to fit within the 16,000 row design constraint, MOSLS itself is solved as a hierarchical system employing the modeling technique of aggregation and decomposition. The top echelon, known as the T-Model, represents training time groups (i.e., groupings of MOSs that are functionally related and have similar training times) and grades. Each training time group (TTG) is wholly contained in one career management field (CMF). The model is a multi-time-period linear optimization (LP with a large embedded network) model using strength targets at the appropriate level of detail that are consistent with the FSA targets used in ELIM-COMPLIP.

![](/api/attachments/VAQQXCMZ/fulltext/images/bf11afafc548d15377e95db41b3ae5248ccf9145fda88bc9d4d232125fd6c7b6.jpg)  
Fig. 3. T-model structure.

The network structure of the T-Model is pictured in fig. 3. Note the simultaneous (or integrated) representation of promotions, reclassifications, conversions, training program, strengths, gains and losses. The T-Model represents the whole active Army enlisted force at the training time group and grade (TTGg) level of detail. The network solution is the optimal determination of the personnel “flows” as represented by the network arcs. The objective of the optimization is to achieve strengths in each time period, so that each TTGg comes as close to the corresponding strength target as possible. For each TTGg the strength target is represented as four target arcs. The value of incremental representation of the target will be discussed later.

The T-Model solution provides constraints for the M-Model, the second echelon. The M-Model is also a network formulation. It represents the enlisted force for the MOSs and grades within a career management field (CMF). An M-Model run is made for each CMF, with the inter-CMF personnel flows accounted for as inputs and outputs to the model run, as determined by the T-Model.

Both the T- and M-Models are pure network representations that may be solved more quickly with special network codes than with general LP codes. The T-Model, however, has some non-network linear constraints. These constraints are represented in the objective function of the network formulation with the use of Lagrangian multipliers. The network solution forms a starting point for the full scale T-Model to be solved by a general LP code. Inputs, outputs and upper or lower bounds on selected arcs may be specified partly to guide the solution and partly to reflect solution constraints provided by ELIM-COMPLIP for both the T- and M-Models, and T-Model solution constraints on the M-Model. To properly represent the ELIM-COMPLIP solution for use by the networks, an inventory tracking simulation is performed to precompute such quantities as losses by MOS and grade that are consistent with

ELIM-COMPLIP losses each time period. The base for the loss computations may be the simulated inventory in the early projection periods and gradually phase over to using the strength targets as the base, since it is reasonable to expect the inventory to adjust itself to achieve target strength (or nearly so) in later time periods.

The idea here is to illustrate the hierarchical structure of the FORECAST enlisted system and not to exhaustively discuss all the submodules of ELIM-COMPLIP, MOSLS, and ULS.

The role of ULS is to forecast the enlisted strength and distributions actions at the MOS, grade, and unit level of detail for the current year, the budget year, and the first year of the FYDP. These forecasts are constrained by the MOSLS forecasts. The result is the enlisted distribution plan (EDP) at the unit, 9-character MOS, and grade level of detail. Results can be aggregated to the 3-character MOS, grade, station code, Major Command (MACOM) or other management level of detail. The results for the first 12 projection months form the basis for generating requisitions.

The forecasting process is a heuristic one with suboptimization each time period. The strength targets at the MOS, grade, and unit level may represent such distribution guidance as:

\- User-defined minimum

• Minimum threshold of readiness

• Minimum authorized level of fill (MALOF)

• Maximum authorized level of fill

• Full strength target

\- Space-imbalanced MOS (SIMOS) overstrength or user-defined acceptable overstrength.

The three modules of the enlisted system, ELIM-COMPLIP, MOSLS, and ULS have similarities in modeling approaches, e.g., inventory projection, rate development, and linear optimization. But there are also distinctive features such as the use of retention rates in ELIM-COMPLIP. The point is that transfer of design and development technology from one problem to another is appropriate and can be achieved by letting the problem characteristics determine the selection of the applicable technique.

![](/api/attachments/VAQQXCMZ/fulltext/images/eb9a5ca2316e8a78d38a68ba22404cbd1e142443868bb176a80d4ff8a0837d80.jpg)

## Large scale linear optimization

## Optimization over time

Representation of the various structural dimensions tends to cause the model to become very large. Another dimension that needs to be considered is the time dimension, making the model even larger. Thus tradeoffs among dimensions occur among the models at the different echelons of a hierarchical system. The time dimension is important, especially in the top echelon model such as ELIM-COMPLIP, because it permits the LP model to consider simultaneously the goals in each time period. Such a time dynamic model permits tradeoffs of personnel management actions over time in accordance with user priorities. If the time periods are small enough (e.g., monthly), seasonal patterns can be represented. This can be important, for example, with respect to accessions. The penalties for not meeting the goals can be varied over time, possibly placing greater priority on meeting goals in the near term of projection time than in the out years.

## Goal programming

Goal programming in ELIM-COMPLIP is used to represent several goals in multiple, hierarchical objective functions. One goal may be selected as a primary objective, e.g., minimize the deviations of projected operating strength from FSA targets, followed by the selection of a secondary goal, e.g., minimizing the backlog of reserves awaiting training. Upon attaining the optimal solution of the primary goal, the procedure is to invoke a constraint that limits the primary objective function value to be not more than the optimal value plus a small amount to avoid numerical round off problems. The secondary objective function is selected and optimization proceeds towards the secondary goal.

The primary goal may be illustrated with the following simple example, let $S_{i}$ be the projected operating strength at the end of projection period i, $T_{i}$ be the FSA target for projection period i, $N_{i}$ be the negative deviation, i.e., $S_{i}$ is less than $T_{i}$ , $P_{i}$ be the positive deviation, i.e., $S_{i}$ is greater than $T_{i}$ . User-specified penalties are associated with $N_{i}$ and $P_{i}$ . The penalties are represented as pseudo-costs in the objective function. The following equation is used to compute $N_{i}$ and $P_{i}$ .

$$
\mathbf {S} _ {\mathrm{i}} + \mathbf {N} _ {\mathrm{i}} - \mathbf {P} _ {\mathrm{i}} = \mathbf {T} _ {\mathrm{i}}.
$$

The LP solution procedure ensures that $S_{i}$ , $N_{i}$ , and $P_{i}$ are nonnegative. This being the case and since $N_{i}$ and $P_{i}$ have penalties associated with them, at most one, $N_{i}$ or $P_{i}$ , will ever be non-zero. A non-zero value occurs when it is not possible for the projected strength to hit target. However, in a linear system, if deviations occur they tend to occur in concentrations in some of the time periods. It is quite possible for one time period to have a very large deviation and the next time period to be right on target.

Fig. 4. Optimization criteria.  
![](/api/attachments/VAQQXCMZ/fulltext/images/cd41e03c57dd61e994fce61eff966cdb6b20fc91e49994fd95a873941295aea6.jpg)

Such an erratic behavior does not result in a desirable manpower program. This can be avoided by breaking each of the deviation variables, $N_{i}$ , and $P_{i}$ , into two, representing acceptable deviations and excessive deviations. Suppose, $N_{i}$ is replaced by $NEX_{i}$ and $NAC_{i}$ (excessive and acceptable respectively), and $P_{i}$ is replaced by $PEX_{i}$ and $PAC_{i}$ , and $f_{i}$ is a fraction of $T_{i}$ that defines the acceptable range of the deviations, then,

$$
\mathrm{S} _ {\mathrm{i}} + \mathrm{NEX} _ {\mathrm{i}} + \mathrm{NAC} _ {\mathrm{i}} - \mathrm{PEX} _ {\mathrm{i}} - \mathrm{PAC} _ {\mathrm{i}} = \mathrm{T} _ {\mathrm{i}}
$$

$$
\mathrm{NAC} _ {\mathrm{i}} + \mathrm{PAC} _ {\mathrm{i}} = \mathrm{f} _ {\mathrm{i}} \cdot \mathrm{T} _ {\mathrm{i}}.
$$

The penalties associated with NEX $_{i}$ and PEX $_{i}$ should be an order of magnitude larger than those for NAC $_{i}$ and PAC $_{i}$ . With such a penalty (or pseudo-cost) structure in the objective function, if a deviation occurs, the acceptable deviation variable (e.g., PAC $_{i}$ ) will take on a positive value up to its limit f $_{i}$ . T $_{i}$ before the excessive deviation variable (e.g., PEX $_{i}$ ) takes on a positive value. As was noted before, the deviation in a projection period occurs in one direction, either positive or negative.

Fig. 4 illustrates the notion of acceptable and excessive deviations. In the picture on the right, the slopes of the lines marked penalties-represent the pseudo-cost for being overstrength. Note the steeper slope when the overstrength is outside the acceptable range. The slopes of the lines marked incentive are negative and represent neg-

![](/api/attachments/VAQQXCMZ/fulltext/images/76e9477281b28d662b947e722eaa7eac120f88672e6279087c1c9b3bd3839608.jpg)

\- End Strength = Beginning Strength-Losses
  - RECLS Out - Conversions Out-Promotions Out
  + Training Gains + RECLS In + Conversions in
  + Promotions In.

\- Optimizer distributes flow of personnel to minimize deviations of end strength from target.

Fig. 5. Projection model trained strength flow (simplified).

ative pseudo-costs (or incentives) for the strength to increase toward the target. When the understrength is viewed as a deviation then the incentive for increasing the strength becomes a penalty (positive pseudo-cost) on the deviation.

## Network flow modeling

In the FORECAST Enlisted System, MOSLS uses a network flow modeling approach with side constraints, and a single, goal-programming objective. A simplified network schematic of the MOSLS M-Model is depicted in fig. 5. MOSLS uses target arcs with six increments as a way of equitably distributing the personnel flow to various target nodes representing the inventory for MOS/grade pairs at the end of a time period or beginning of the next one. The side constraints of greatest import are the grade limits, which limit the total strength at any pay grade, to the grade limit.

MOSLS originally had four increments, but now requires six target arcs because of the interaction between targets, which represent needs, and the grade limits, which can be significantly less than the total of the targets for that grade. Formerly, the targets were normalized to sum to the grade limits, but this salami-slicing procedure did not take into account the different priorities of the various MOSs. Therefore, some MOSs were 'fenced', that is, their targets were not changed, and the remaining MOS' targets were normalized so as to make the total equal to the grade limit. However, the bureaucratic procedure to designate fenced MOSs was arduous, and MOSLS was requested not to normalize the grade limits. However, the grade limits for E-8 were so small relative to the sum of the upper bounds on the first target arcs, resulting in some end-strengths of zero until an additional target arc with a vary high incentive was used as a safety net. This safety net arc is used as an automated arbiter to decide which requirements to fill at close to target, and which to make into bill-payers so as not to exceed the grade limits. (On the overage side, the sixth target arc was required to prevent the LP solution from designating certain MOSs to receive strength greatly in excess of target under circumstances calling for the distribution of excess strength in greater quantities than could be handled by the acceptable positive deviation target arcs.) The story of the development of MOSLS from four increments to six reflects its growing role as a decision support tool.

![](/api/attachments/VAQQXCMZ/fulltext/images/7acd784ef2534435c8f5030ab2be5a3e383e2eff343737a6705c43a689aeec78.jpg)

<table><tr><td colspan="2"></td><td colspan="2">Cumulative Targets for Commands</td><td colspan="2">Incremental Targets for Commands</td><td colspan="2">Relative Costs Negative Incentive Positive Penalty Commands</td></tr><tr><td>Arc No.</td><td>Type of Strength Level</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>1</td><td>User Specified Minimum Fill Level</td><td>80</td><td>120</td><td>80</td><td>120</td><td>-10000</td><td>-11000</td></tr><tr><td>2</td><td>Readiness Level</td><td>90</td><td>140</td><td>10</td><td>20</td><td>-1000</td><td>-1100</td></tr><tr><td>3</td><td>MALOF Strength Level</td><td>95</td><td>180</td><td>5</td><td>40</td><td>-100</td><td>-110</td></tr><tr><td>4</td><td>Full Strength Level</td><td>100</td><td>200</td><td>5</td><td>20</td><td>-10</td><td>-11</td></tr><tr><td>5</td><td>Acceptable Overstrength Level</td><td>105</td><td>220</td><td>5</td><td>20</td><td>+11</td><td>+10</td></tr><tr><td>6</td><td>Unacceptable Overstrength Level</td><td>&gt;105</td><td>&gt;220</td><td>∞</td><td>∞</td><td>+∞</td><td>+∞</td></tr></table>

Fig. 6. Illustration for incremental strength targets.

In the case of ULS, the incremental targets can take on specific meanings as depicted in fig. 6. In this example, command A has a full strength target of 100 and command B of 200 (for a given MOS, grade, and time period). To illustrate the effect of the incremental targets suppose that available personnel (including the stabilized personnel inventory) for both commands A and B numbers only 270, and command B has priority. Then B would receive 200 and A, 70. With incremental targets and command B having priority only at each increment, as reflected by a negative cost of -11,000 as compared to -10,000 for A, the allocation is as follows: Command B gets the first 120; command A gets the next 80; B the next 20; A the next 10; and B the remaining 40. Thus, without incremental targets, A would not even get what is considered to be an absolute minimum. With incremental targets, B hits the MALOF (minimum authorized level of fill) strength level and A makes the readiness level – a much more equitable distribution. A heuristic approach was used to solve the ULS problem rather than a formal network solver. This saved considerable overall time (i.e., model generation and solution) and permitted easy inclusion of non-network constraints.

## Matrix generation and solution codes

The general LP and network models can be generated by means of custom written programs. The ELIM-COMPLIP matrix generator (MG) is written in FORTRAN IV and the MOSLS network MGs are written in PL/1. High level MG languages exist that provide a higher efficiency in development of MGs (after an initial learning curve).

LP solution codes are available from IBM, MPSX/370; from Ketron, MPSIII and WHIZARD. WHIZARD, an in-core optimizer, is faster than the MPSX/370 PRIMAL optimizer. It is currently used in conjunction with MPSX/370. The network solution code ARCNET is from Cleveland Consulting Associates (formerly Analysis, Research and Computation). Ketron has WHIZNET available as a network optimizer within WHIZARD.

Several new LP solution codes have come on the market, among them are AT&Ts KORBX system that is based on the Karmarker algorithm, and IBM's Optimization Subroutine Library (OSL). Test runs have been made using both of these systems with dramatic increases in solution speeds. Whereas, older LP codes have had a limit of 16,000 on the number of constraint rows a problem was permitted to have, the newer codes do not have this limit. Thus, larger problems can be solved with acceptable solution times. For example, the MOSLS problem can be formulated as a single problem of about 33,000 constraint rows rather than a smaller master problem and about 10 smaller subproblems.

## Retention rates

In an application of LP where accession levels are determined, the projected strengths and consequently, the total losses are not only a function of the starting personnel inventory but also of the accessions during the course of the projection horizon. Thus, losses need to be attributed to the accessions during and subsequent to the accession time period. The complement to loss is referred to as retention. The retention rate in a given time period is the fraction of the accession cohort remaining in that time period, where the time period is not earlier than the accession period.

Accurate retention rates can be computed by means of an inventory projection technique. This subject is introduced in the section entitled, Personnel Inventory Projection, and discussed more fully in the section entitled, The Integrated Approach.

## Personnel inventory projection

Personnel inventory projection is a deterministic simulation of the personnel inventory and associated personnel management actions. Preliminary to the basic process of inventory projection is the task of defining an appropriate partition for the inventory. Fundamental to that is the development of rates for each cell of the partition. These rates are specifically defined for the cells of the partition and for the order of use in the simulation. Stand-alone, they may not be properly understood or be applicable for use elsewhere.

The rates that are needed are those that represent the relevant personnel management actions. For ELIM, for example, typical rates are for immediate reenlistments, extensions, and various causes of loss such as separation at expiration of term of service (ETS), nondisability retirement (NDR), and several types of attrition. There are also factors for distribution of reenlistments to their new term of commitment and the distribution of extensions by length of extension. The factors and rates are based on historical data with provision for user overrides to reflect changes in policy from that present in history.

The rate development process will be discussed more fully in a subsequent section. The remainder of this section deals with the techniques in inventory projection that make it an accurate means of loss projection. An example is presented to illustrate the process.

## Population inventory partitioning

The structural characteristics may be used as a basis for partitioning to identify the population by category of personnel such as draftees (when present); first timers (FTI) – i.e., enlistees in their first term that have not extended; exten-dees; and reenlistees. The structure may also reflect such dimensions as time remaining in the

FIRST ENLISTMENT  
SUBSEQUENT ENLISTMENT  
![](/api/attachments/VAQQXCMZ/fulltext/images/14f66ae5dac5970a103582f435fda18955383c269b288cf4817dab84a20619b6.jpg)  
Fig. 7. Partitioning of the enlisted inventory reflecting structural characteristics with inherent behavioral characteristics (e.g., separations due to ETS or retirement).

![](/api/attachments/VAQQXCMZ/fulltext/images/b76b12b84ae1cffb2888622cb319318767a3982be99f6eadf0aee8ff2f217833.jpg)  
Fig. 8. Statistical technique for partitioning the inventory.

term of commitment, or time in service. This kind of partitioning is seen in fig. 7, an example taken from an earlier version of ELIM-COMPLIP. Note the months-to-ETS breakout that helps capture the behavior characteristics of ETS losses and the month-of-service breakout defines the population eligible for NDR. Length of service is also significant in the estimation of various types of attrition. From this, it is clear that some structural characteristics are strongly associated with behavioral characteristics.

![](/api/attachments/VAQQXCMZ/fulltext/images/d7a1e2351cf01dbed85bc9cd92aab56d85321fe669476775725f93d831297e36.jpg)

![](/api/attachments/VAQQXCMZ/fulltext/images/233389051f16462842f7ebf66f31cf1ef5022e64f04d1a64608834db226f2597.jpg)  
Fig. 9. Inventory matrix, first timers by C-group and training time category.

The FTI population may be further partitioned by characteristic group (C-group). A C-group is defined in terms of demographic characteristics, e.g., civilian education, race, gender, test score category. The C-groups reflect a partitioning that has been determined to be significantly related to attrition behavior.

A statistical technique developed by the University of Michigan known as Automatic Interaction Detection (AID) was initially used in defining the C-groups in ELIM-COMPLIP [14,15]. This is illustrated in fig. 8. The process makes use of factor analysis and determines population splits by selecting dimensions that provide maximum variation in loss behavior between the split populations. Yet another enhancement to the FTI partition is the inclusion of training time. Explicit representation of training time categories increases the accuracy of the projection of the trainee inventory as well as providing a way to represent the variable enlistment terms (VEL), which has recently become effective for some FTI. This partition is shown in fig. 9.

## The representation of accessions

Inventory projection is not the appropriate tool to determine accessions. This determination should be accomplished with a goal LP, i.e., determine accessions so that the projected strength meets (or comes as close as possible) to a strength target. For each accession variable in the LP, a retention coefficient is required to account for losses over time. The source of the retention coefficient can and should be inventory projection. In an inventory projection the accession, if not known, can be represented as retention rates. Each cohort has its own retention rate for each period of the projection, starting with the period in which the accession occurs. A cohort, in this case, is defined by time period and C-group. For example, the accession variable for C-group 1 and projection period 1 defines a unique cohort.

![](/api/attachments/VAQQXCMZ/fulltext/images/4ae4d22045c04cfb3ec56331b69ad37a469c03fe308a0c7b542a857813530339.jpg)  
Fig. 10. Cumulative loss rates as a function of race, civilian education and mental group.

The retention rate for a cohort is 1.0 at the beginning of the accession period. At the end of the accession period and subsequent projection periods it is decremented by the application of loss rates. Thus, the retention characteristics are determined for each accession variable used in the goal LP. The initial retention rate of 1.0 for a cohort may be distributed across other dimensions such as term of service, or training time group by use of historically derived distribution factors. For example, a distribution across term category might be 0.05, 0.5, 0.3, 0.1, 0.5 for terms of two, three, four, five, and six years, respectively. Note the sum of the fractions is 1.0 for the initial cohort retention rate.

Since the accession level is generally not known during inventory projection at the top echelon projection level, the retention rates of the various cohorts represent fractions of separate unknown quantities and, therefore, cannot be combined, but must be tracked separately.

## Rate development

Rate development is an important process in manpower projection since it provides the rates used in the inventory projection process. Thus, the definition of the rates under development has to be consistent with that of the application. That is, the population groups in the numerator and denominator of a rate need to have the same definition in historical data used for rate development as in the inventory where the rate is applied. For example, in a given projection period, the starting inventory is the inventory at the end of the previous period. If this inventory is adjusted for certain gains and losses (e.g., immediate reenlistments) before the ETS loss rate is applied then the computation of the ETS loss rate should have the historical inventory adjusted for the same gains and losses for each similarly defined historical period before the ETS loss rate is computed. Consistency between rate development and application needs to be established for all levels of detail, e.g., structural dimensions, time period lengths, and demographic characteristics.

![](/api/attachments/VAQQXCMZ/fulltext/images/1b4eb81156e4e5bcad3f0b3a4214038f38aaaf2899a58d683209cadc6ce27d72.jpg)  
Fig. 11. Least squares fit function to capture trends.

The importance of demographic characteristics in capturing homogeneity in loss behavior is illustrated in fig. 10. The curves represent cumulative loss rates over months of service for several demographic-based C-groups. If the graphs were linear, then no variation in loss behavior over length of service would be present. The curvature of the graphs indicates that loss rates are higher during the first 6 to 8 months of service than during the subsequent months.

Several rate development techniques may be considered such as simple averages, weighted averages, moving averages, exponential smoothing, or various enhancements of the latter. Exponential smoothing is a recursive technique for smoothing a time series of historical rates giving greater weight to the more recent historical data, and is the technique used in ELIM-COMPLIP.

Exponential smoothing is especially suited for developing rates for inventory projection processes that have the population partitioned into homogeneous cells because the last exponentially smoothed rate is straight lined over projection time. Note that the historical data display no trend but only apparently random fluctuations. When policy is implemented that affects the future behavior of the population with respect to a certain cause of loss, that rate may be adjusted by means of user controls for the appropriate time frame.

If a trend has been observed in history, but is expected to level off at some future time, then an exponential trend function may be fitted to the data by the method of least squares. This is illustrated in fig. 11. The functional form of the trend line is

$$
\mathrm{r} (\mathrm{t}) = \mathrm{A} - (\mathrm{A} - \mathrm{C}) (\mathrm{t} / \mathrm{T}) \exp ((\mathrm{T} - \mathrm{t}) / \mathrm{T}).
$$

where t is the independent variable, time, $t = 0, 1, \ldots, T$ , $r(t)$ is the computed rate for time t, T is the point on the t axis where $r(t)$ has its minimum (or maximum if C is greater than A), in fact, $r(T) = C$ , and A, C are parameters of the function that are normally determined by least squares.

The usable range of the function is from t = 0 to t = T. Since the minimum (or maximum) value, C, is attained at t = T, the rates r(t) for t greater than T are set to the value C (i.e., “straightlined”). The value T at which the function levels off is normally specified by the user. It may be specified over a range of values with incremental increases over the previous value and the least squares is solved for A and C at each new value of T. Solving T directly with least squares, together with A and C can be troublesome (i.e., a saddle point has been encountered).

The parameters of the function are based on the historical data that reflects a trend. In fig. 13 such historical data are pictured in the range t = 0 and t = T. The historical data prior to the point defined as t = 0 are omitted from the calibration of the trend function since they reflect only random fluctuation of the loss rate, without evidence of trend.

In developing rates for a finely partitioned population, it is possible to have population cells with very small populations. When used as the base for computing rates, unstable rates may result. Statistical analysis can be performed to determine statistically significant cell sizes. A rule of thumb may be used that requires a minimum population cell size of 200 for the computation of stable rates.

The computer programming of these rates may be performed as standard “black box” routines for the actual rate projection. But most of the programming is required for the the manipulation of the input data preceding the rate computation and managing the rates after it. Of this, a good part is customized programming. However, rate development technology and some software can be transferred from one project to another.

## The integrated approach

The term integrated approach is used here to mean the simultaneous computation of quantities that depend on one another. For example, in a projection environment the strengths, gains, and losses are such quantities. For a given projection period, i, the following simple relationship holds

$$
\begin{array}{r l} \text { endstrength   (i) } & = \text { endstrength   (i   -   1) } + \text { gains   (i) } \\ & - \text { losses   (i) }. \end{array}
$$

The equation shows the dependence of end-strength on gains and losses, as well as, the previous period endstrength. Losses are a function of the endstrength level which reflects gains and losses of previous periods. Since in FORECAST projections a strength target is given, the gains cannot be arbitrary but rather are determined to bring the projected endstrengths as close to the targets as possible. The gains, then, are a function of strengths (which reflect previous period gains and losses) and specified targets. In fact, the gains in a given period are also affected by the endstrengths and targets of future periods.

<table><tr><td rowspan="2">MSV</td><td colspan="2">C-Group</td></tr><tr><td>1: HSDG</td><td>2: NHSDG</td></tr><tr><td>1</td><td>.0025</td><td>.0097</td></tr><tr><td>2</td><td>.0252</td><td>.0389</td></tr><tr><td>3</td><td>.0212</td><td>.0317</td></tr><tr><td>4</td><td>.0115</td><td>.0166</td></tr><tr><td>5</td><td>.0087</td><td>.0158</td></tr><tr><td>6</td><td>.0088</td><td>.0123</td></tr></table>

Fig. 12. Loss rates used in sample computations.

For a given period, it may be that a moderate number of gains (rather than all that would be needed to hit the target) should be projected in order to avoid excessive overstrengths in subsequent periods. Thus, the integrated approach simultaneously considers strengths, gains, losses, and time.

In this discussion, reference to strength, gains, and losses is appropriate in the context of the total active Army or in the context of a population cell of the selected population inventory partition. In the former case, gains and losses pertain to gains and losses to the active Army. In the latter case, they pertain to gains and losses to the population of the cell. Such gains and losses may reflect such actions as reenlistments, promotions, and reclassifications.

![](/api/attachments/VAQQXCMZ/fulltext/images/089ed47842b42c0ce629f8288e6a3e8b2c0c30c13d9681014addc1beb4a6f665.jpg)  
Fig. 13. Inventory matrices used in sample computations.

The integrated approach should be taken wherever appropriate and to the extent possible, keeping the model at a manageable size. In the enlisted FORECAST systems it has its greatest impact on the highest echelon of the hierarchical structure, ELIM-COMPLIP.

The role of inventory projection is to accurately project losses and loss characteristics (or conversely, retention characteristics) of the accessions that occur during the projection time horizon, where the accession levels are optimally determined by COMPLIP. The goal optimization process, COMPLIP, determines the accessions (and with it the total strengths and losses) such that the weighted sum of the absolute values of the deviations of the projected strengths from the strength targets is minimized. The COMPLIP optimization is accomplished subject to user-specified constraints.

The inventory projection process feeds COM-PLIP projected strengths and losses of the starting inventory in terms of people counts, and retention characteristics (retention rates) of accessions that COMPLIP is to determine. The set of retention rates is the key link between the inventory projection and goal optimization that facilitates the integrated approach in ELIM-COMPLIP. An example will serve to illustrate the use of the retention rate.

In this example, only part of the first term (FT) inventory is considered. The sample partition consists of two C-groups and a month of service breakout. Fig. 12 shows the loss rates, only one loss type is assumed and loss rates are constant over time. The rates are used in the inventory projection process pictured in fig. 13. They are applied to the inventory at the beginning of the month. The inventory is adjusted for the losses to arrive at the inventory at the end of the month. After the first projection month, the inventory is “aged” as shown by the arrows to arrive at the inventory at the beginning of the second projection month. The row of 1.0 s for month of service one at the beginning of each projection period represents the accessions in those projection periods for each of the C-groups. In each time period the retention rates are decremented for losses.

<table><tr><td></td><td>ENLSSTRP3</td><td>FTGNSPP3</td><td>FTLNGSP3</td><td>FTCG1SP1</td><td>FTCG2</td><td>FTCG3</td><td>FTCG4</td><td>FTCG5</td><td>ENLSTRP2</td><td></td><td>RHS</td></tr><tr><td>FT Gains in Proj. Month 3</td><td colspan="6">1</td><td>-1</td><td>-1</td><td></td><td>=</td><td>0</td></tr><tr><td></td><td colspan="8"></td><td></td><td></td><td></td></tr><tr><td>FT Losses in Proj. Month 3</td><td colspan="8">1 -.0207 -.0302 -.0251 -.0385 -.0025 -.0097</td><td>=</td><td>Other FT Losses</td><td></td></tr><tr><td></td><td colspan="6">.9724-.9517</td><td colspan="2">1.0-.9903</td><td></td><td></td><td></td></tr><tr><td>Strength in Proj. Month 3</td><td colspan="6">1 -1 1</td><td colspan="2">-1</td><td>=</td><td>Net Gains/Losses</td><td></td></tr><tr><td></td><td colspan="8"></td><td></td><td></td><td></td></tr></table>

Fig. 14. Portion of COMPLIP-like matrix.

Each C-group has a unique retention rate for each month of accessions. This defines an accession cohort, the level of which is determined by the LP. The retention rate for each accession cohort is tracked in the inventory projection process from the accession month on to the end of projection time. In fig. 13, the inventory in projection month 3 has 12 accession cohorts represented by retention rates: four C-groups and three accession months (i.e., accessions in each of the three projection months). The accessions in projection months 1, 2, and 3 are represented by the retention rates with month of service 3, 2, and 1, respectively. For example, for C-group 1 and month of service 3, the retention rate of 0.9724 at the beginning and 0.9517 at the end of projection month 3 represents the C-group 1 accessions in projection month one. The difference $0.0207 = 0.9724 - 0.9517$ is the fraction of the accession cohort that are projected as losses for the cohort in projection month 3. This is entered in the LP matrix as $-0.0207$ by the matrix generator.

The combination of inventory projection and goal LP is a very effective forecasting approach. The inventory projection provides accuracy in loss projection and the LP provides optimization of accessions (over C-groups and time) to achieve the strength goals represented by the strength targets, subject to user-provided constraints. As previously mentioned, the link between the inventory projection and the LP that facilitates their coupled use is the retention rate. Fig. 14 illustrates the use of retention rates in the LP formulation. The example shows a small portion of a COMPLIP-like structure. It focuses on projection month 3 and depicts three constraints.

\- Computation of FT gains in projection month 3 (FTGNSP3) as the sum of the C-group accessions in project month 3 (FTCG1P3, ..., FTCG2P3).

\- Computation of FT losses in projection month 3 (FTLOSSP3) as the sum of the losses in projection month 3 from all the C-groups accessions for projection months 1, 2, and 3, and the FT losses computed as people counts by the inventory projection process (RHS value). The negative coefficients are the differences in the retention rates at the beginning of projection month 3 and at the end (see fig. 13) for each cohort for which the LP is to compute the accession level. The circled values in fig. 14 correspond to those in fig. 13.

\- Computation of enlisted strength in projection month 3 (ENLSTR3) as the sum of the enlisted strength in projection month 2 (ENLSTR2) plus FT gains in projection month 3 (FTGNSP3) minus FT losses in projection month 3 (FTLOSSP3) plus the net gains-losses) in terms of people counts from the inventory projection process.

This submatrix was selected to illustrate the use of the retention rate in the LP formulation.

## Summary

The enlisted FORECAST system is an example of hierarchical constrained models consisting of ELIM-COMPLIP, MOSLS, and ULS. ELIM-COMPLIP is the top echelon model whose forecasts are used to constrain the MOSLS projection. These in turn constrain the ULS projections. The focus of ELIM-COMPLIP is on accuracy of the projection of the Active Army Military Manpower Program (AAMMP). The inventory partitions and the decision variables have been defined accordingly. The MOS, grade, and unit level of detail is not represented.

The role of MOSLS is to project the enlisted strengths, gains, losses, promotions, reclassifications, reenlistments, conversions, and the training program by MOS and grade, constrained in the aggregate for each time period to the ELIM-COMPLIP projected accessions, losses, and reenlistments. Since MOSLS projections begin with the same personnel inventory as ELIM-COM-

PLIP, the MOSLS projected strengths are implicitly constrained to those of ELIM-COMPLIP.

MOSLS, itself, consists of three hierarchical models:

\- The T-Model defined at the training time group and grade (TTGg) level. Each TTG is a collection of MOSs, within a CMF, with similar training times.

\- The M-Model defined at the MOS and grade level.

\- The Postprocessor which provides refinement of the M-Model solutions.

The role of ULS is to determine the Enlisted Distribution Plan (EDP) and to generate candidate lists of projected movement at the MOS/grade/unit level of detail known as requisitions for the assignment process.

The direction of model development in the FORECAST environment is to complement the mainframe systems with less detailed PC models to conduct what-if analysis for the purposes of assessing the effect of a variety of input assumptions. After the assumptions have been narrowed to the desired set the mainframe models may then be run to obtain more detailed results. A PC What-If model is currently under development for the Enlisted system. It is a combination of simulation and optimization making use of CPLEX Optimization's CPLEX LP code.

Emphasis has also been placed on developing Executive Information Systems (EIS) making use of high-level software tools such as EASEL Corporation's EASEL and COMSHARE's Commander EIS. One of the favorite applications is automatically updated electronic briefing charts.

## Acknowledgments

The work represented in this paper reflects the efforts of many people at Headquarters, Department of the Army (HQDA) and at the General Research Corporation (GRC) over a period of about 20 years. Special mention must be made of some key individuals whose vision and driving force have made the development and use of these systems a success. COL William A. Curtis, Commander, US Army Decision Systems Management Agency, was an early user of the systems and a visionary in extending the early successes of the Personnel DSS progressively to other functional areas. COL Danny Michael, the Deputy Information Management Officer (IMO) of the Office of the Deputy Chief of Staff for Personnel (ODCSPER) has provided significant guidance to the development staff as well as being instrumental in fighting the budget battles in support of this work. A long line of contracting officer's representatives (CORs) of the Decision System Management Office (under COL Michael) faithfully performed their duties in monitoring the contract activities.

From GRC, Betty Holz (now retired), a previous Director of the Management Sciences Group (MSG), was the designer and developer of the early systems. Her keen insight into the Army personnel management problems set the stage for the progressively successful development of the systems. Subsequent MSG directors, Charles E. Smith and James L. Selsor (the present director) continued to provide direction to the projects. Since the Enlisted System is the focus of this paper, special mention is made of the Enlisted Program Manager, David Smyre, and the three present project managers: Sue Ross, ELIM-COMPLIP; Richard Hedgpeth, MOSLS; and Judy Kerbel, ULS. Thanks to Sue Ross and Dick Forrester for providing representative data used in the computational examples and to Judy Kerbel for reviewing the paper. Finally, appreciation is expressed to Bong Allen for tirelessly and enthusiastically providing word processing and graphics support for the preparation of this paper.

## Cited references

[1] B. Benjamin and J.H. Pollard, The Analysis of Mortality and Other Actuarial Statistics (William Heinemann, London, 1980).

[2] A. Charnes and W.W. Cooper, Management Models and Industrial Applications of Linear Programming, 2 vols. (John Wiley and Sons, New York, 1961).

[3] A. Charnes, W.W. Cooper, and R. Ferguson, Optimal estimation of executive compensation, Management Science 1 (1955) 138–151.

[4] A. Charnes, W.W. Cooper, and R.J. Niehaus, A goal programming model for manpower planning, in: Management Science in Planning and Control (edited by J. Blood, Jr.) Special Technical Publication (1969) 79–93.

[5] A. Charnes, W.W. Cooper, and R.J. Niehaus, A general-

ized network model for training and recruiting decisions in manpower planning, in: Manpower and Management Science (edited by D.J. Bartholomew and A.R. Smith) (Lexington Books, Lexington, MA (1971) 115–130.

[6] A. Charnes, W.W. Cooper, and R.J. Niehaus, Studies in Manpower Planning (U.S. Navy, Office of Civilian Manpower Management, Washington, DC, 1972).

[7] S.I. Gass, R.W. Collins, C.W. Meinhardt, D.M. Lemon, and M.D. Gillette, 1988, The Army manpower long-range planning system, Operations Research 36, No. 1 (1988) 5–17.

[8] B.W. Holz and J.M. Wroth, “Improving Strength Forecasts: Support for Army Manpower Management,” Interfaces 10, No. 6 (Dec., 1980) 37ff.

[9] B.W. Holz et al., "Manpower Planning Models: COM-PLIP and CHAMP," RAC-TP-440 (Research Analysis Corporation, McLean, VA, January, 1972) 23–28.

[10] B.W. Holz et al., "The ELIM-COMPLIP System of Manpower Planning Models, Volume I: General Overview," OAD-CR-18 (General Research Corporation, McLean, VA, Dec., 1973) 27–36.

[11] D. Klingman and N.V. Phillips, Topological and computational aspects of preemptive multicriteria military personnel assignment problems, Management Science 30, No. 11 (Nov., 1984) 1362–1375.

[12] P.D. Phillips et al, "Manpower for Force Structure Planning," D2-CR (Research Analysis Corporation, McLean, VA, Oct., 1970) 6–20.

[13] A.H. Pollard, F. Yusuf, and G.N. Pollard, Demographic Techniques, 2nd ed. (Pergamon Press, Sydney, 1974).

[14] J.A. Sonquist, and J.N. Morgan, The Detection of Interaction Effects, Monograph No. 35 (Institute for Social Research, The University of Michigan, Ann Arbor, MI, 1964).

[15] J.A. Sonquist, E.L. Baker, and J.N. Morgan, “Searching for Structure” (Institute for Social Research, The University of Michigan, Ann Arbor, MI, 1971).

[16] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, NJ, 1982).

[17] G.L. Thompson, 1979, A network transshipment model for manpower planning and design, in: Quantitative Planning and Control (edited by Y. Ijiri and A. Whinston) (Academic Press, New York, 1979) 125–140.

## General references

A. Eiger, J.M. Jacobs, D.B. Chung and J.L. Selsor, The US Army's Occupational Specialty Manpower Decision Support System, Interfaces, 18, No. 1 (Jan.-Feb. 1988) 57–73.

J.J. Emberger and H.S. Weigel, ELIM-COMPLIP System Documentation, Vol. 4: The Inventory Projection Module, Report 1131-03-8 1-CR (General Research Corporation, McLean, VA, 1981).

FORECAST Office, The FORECAST Master Plan, (FORECAST Development Office, Office of the Assistant Secretary of the Army [Manpower and Reserve Affairs], Washington, DC, 1983).

B.W. Holz et al., Unit Level Enlisted Strength and Personnel Management Actions Forecasting System (ULS), System Specifications, Report 1402-02-84-CR (General Research Corporation, McLean, VA, 1984).

MOSLS Project Team, Military Occupational Specialty Enlisted Strength and Personnel Management Data Forecasting System (MOSLS), Executive Summary, Report 1403-01-84-CR (General Research Corporation, McLean, VA, 1983).

H.S. Weigel, ELIM-COMPLIP System Documentation, Vol. 3: COMPLIP – The Matrix Generator and Linear Programming, Report 1131-03-84-CR (General Research Corporation, McLean, VA, 1983).

List of abbreviations and acronyms

AAMMP Active Active Army Military Manpower Program
AID Automatic Interaction Detection
ASA(M & RA) Assistant Secretary of the Army (Manpower and Reserve Affairs)
AT&T American Telephone and Telegraph Corporation
ADP Automated Data Processing
AIT Advanced Individual Training
BCT Basic Combat Training
C-Group Characteristic Group
CIVFORS CIVilian FORecasting System
CG Characteristic Group
CMF Career Management Field
COL Colonel
COMPLIP COmputation of Manpower Programs using Linear Programming
Cont continuation
COR Contracting Officer's Representative
DM Director of Management
DSMA Decision Systems Management Agency
DSMO Decision Systems Management Office
DSS Decision Support System
E-8 Enlisted pay grade grade level eight (master sergeant)
EDP Enlisted Distribution Plan
EIS Executive Information System
ELIM Enlisted Loss Inventory Model
ELIM-Enlisted Loss Inventory Model, COmputation of Manpower Programs using Linear Programming
COMPLIP Programs using LLinear Programming
ETS Expiration of Term of Service
FORTRAN FORmula TRANslator
FSA Force Structure Allowance
FT First Term
FTI First TImers
FY Fiscal Year
FYDP Five-Year Defense Plan
GED General Equivalency Diploma
GRC General Research Corporation
HQDA Headquarters, Department of the Army
HSDG High School Diploma Graduate
HSG High School Graduate
IBM International Business Machine Corporation
IMO Information Management Officer
IPS Integration Policy System
LP Linear Program, Linear Programming
MACOM MAjor COMmand
MALOF Minimum Authorized Level Of Fill
MG Matrix Generator
MIS Management Information System
MOS Military Occupational Specialty
MOSLS Military Occupational Specialty Level System
MPSIII Mathematical Programming System, Three

<table><tr><td rowspan="2">MPSX</td><td rowspan="2">Mathematical Programming System, eX-tended</td><td>SMM</td><td>System Management Module</td></tr><tr><td>STI</td><td>Secont-TIme enlistee</td></tr><tr><td rowspan="2">MSG</td><td rowspan="2">Management Sciences Group of the General Research Corporation</td><td>RECLS</td><td>Reclassifications</td></tr><tr><td>RHS</td><td>Right-Hand Side</td></tr><tr><td>NDR</td><td>Non-Disability Retirement</td><td>TC</td><td>Term Category</td></tr><tr><td>NHDG</td><td>Non-High school Diploma Graduate</td><td>TDP</td><td>Trainee Discharge Program</td></tr><tr><td>OCSA</td><td>Office of the Chief of Staff of the Army</td><td>TOPSS</td><td>The Officer Projection Specialty System</td></tr><tr><td rowspan="2">ODCSPER</td><td rowspan="2">Office of the Deputy Chief of Staff for Per-sonnel</td><td>Trng</td><td>training</td></tr><tr><td>TTG</td><td>Training Time Group</td></tr><tr><td>OPALS</td><td>Officer Projection Aggregate Level System</td><td>TTGg</td><td>Training Time Group and grade</td></tr><tr><td>PC</td><td>Personal Computer</td><td>TTHS</td><td>Trainees, Transients, Holdees, and Students</td></tr><tr><td>PERDSS</td><td>Personnel Decision Support System</td><td>UB</td><td>Upper Bound</td></tr><tr><td>PL/I</td><td>Programming Language One</td><td>ULS</td><td>Unit Level System</td></tr><tr><td>POM</td><td>Program Objective Memorandum</td><td>VCSA</td><td>Vice Chief of Staff</td></tr><tr><td>PS</td><td>Prior Service</td><td>VEL</td><td>Variable Enlistment Length</td></tr><tr><td>RC</td><td>Reserve Components</td><td></td><td></td></tr><tr><td>SIMOS</td><td>Space-Imbalanced Military Occupational Specialty</td><td></td><td></td></tr></table>
