---
otero_id: 26533
otero_key: "GWM86WV6"
title: "MCDM Approach for Generating and Evaluating Alternatives in Requirement Analysis"
authors: "Hemant K. Jain; Mohan R. Tanniru; Bijan Fazlollahi"
year: "1991"
journal: "Information Systems Research"
doi: "10.1287/isre.2.3.223"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/GWM86WV6/fulltext/images/b66264f0b0b91fd57906b8c05e35baf4a3e5a5e895750f9506339257a3315771.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# MCDM Approach for Generating and Evaluating Alternatives in Requirement Analysis

Hemant K. Jain, Mohan R. Tanniru, Bijan Fazlollahi,

## To cite this article:

Hemant K. Jain, Mohan R. Tanniru, Bijan Fazlollahi, (1991) MCDM Approach for Generating and Evaluating Alternatives in Requirement Analysis. Information Systems Research 2(3):223-239. http://dx.doi.org/10.1287/isre.2.3.223

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1991 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GWM86WV6/fulltext/images/b01727e4644a4cea933e1c50600d34d4c4d5830d21820c57a736228bec6925cf.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# MCDM Approach for Generating and Evaluating Alternatives in Requirement Analysis

Hemant K. Jain

School of Business Administration

Unıversity of Wisconsin-Milwaukee

Mohan R. Tanniru

Milwaukee, Wisconsin 53201

School of Management

Syracuse Universuty

Bijan Fazlollahi

Syracuse, New York 13210

School of Business Adminıstration

Georgia State University

Atlanta, Georgıa 30303

Determining user requirements and generating alternative system solutions to meet these requirements are two critical steps in the requirement analysis phase of the system development life cycle. Much of the MIS research in the requirement analysis phase has been devoted to the topic of requirement determination and its verification. Alternative generation and evaluation is left, to a significant degree, to the judgment and expertise of an analyst. This paper proposes a multiple criteria decision making (MCDM) approach for generating and evaluating alternatives when the user requirements are expressed in terms of certain operational criteria such as time, cost, risk, etc. These alternatives form the basis for the user to make the necessary trade-offs.

Requirement analysis—Alternative generation—Goal programming-lnformation system design

## 1. Introduction

he management of information resources requires that information system planning be closely linked to corporate goals and objectives. The need for such planning has been well documented (Anthony 1965, Gibson and Nolan 1974, McLean and Soden 1977, Pyburn 1983). For an IS plan to be effective, the planning methodology should convert corporate goals and objectives into information requirements (strategic planning), translate these requirements into specific information system solutions (requirement analysis), and allocate corporate resources to the competing systems (resource allocation) (Davis and Olson 1985)

Several methodologies have been developed to relate corporate goals, objectives, and attributes to IS plans (objectives and strategies) (Cash et al. 1988, King 1978, Lederer and Mendelow 1986, McLean and Soden 1977). These plans tend to be broad statements describing the information needs of the organization. The requirement analysis phase tries to explicitly translate these needs into specific system requirements and select the most cost effective alternative in a socio-economic sense.

Thus, the requirement analysis phase can be viewed as comprising two steps: requirement determination and requirement evaluation.

The requirement determination step attempts to translate user (organization or application) needs into specific system requirements. To do this, one needs to map these user needs to current or proposed system architectures. Prior research (Dickson and Wetherbe 1985) has shown that methodologies such as BSP (IBM), critical success factors (Rockart 1979), business information analysis and integration techniques (Carlson 1979), and ends/means analysis (Wetherbe and Davis 1982) can be used to facilitate such requirement determination. Davis and Olson (1985) discuss several methodologies for determining system requirements and present a contingency approach for selecting a methodology based on specification uncertainty.

The requirement evaluation step needs to translate the system requirements into a proposed system architecture that will satisfy the information needs of the organization most effectively. A system architecture generally consists of a number of subsystems, and each subsystem may be represented by a collection of related processes. Each subsystem can be designed to function under different modes of operation such as completely manual, partially automated, in batch, on-line, or completely automated, etc. It may also be designed to meet different functional requirements. Each of these alternative modes of operation or sets of functional capabilities will be referred to as alternative “configurations" or “designs" of a subsystem. Thus a proposed system architecture may alter the configuration of one or more of its subsystems from their current design to a new design in order to satisfy some or all of the user requirements specified in the requirement determination step. Thus, the primary objectives of the requirement evaluation step are: generate several “feasible" system architectures and then evaluate them in a socio-economic sense in order to select the most “effective" architecture. Many planning/analysis methodologies, however, do not explicitly address the generation of an “effective" architecture.

Two factors that make this requirement evaluation complex are: frequency in design changes and overlapping use of system resources. Changing the design of a subsystem in a system architecture can affect multiple system requirements, but not necessarily all in the same direction (i.e., a change may affect one requirement positively and another negatively) (Lederer and Mendelow 1986). The system resources such as files, peripheral equipment, and software, required to design competing systems, may be used to satisfy multiple-user requirements. This overlapping use of resources will have an impact on the selection of subsystem designs to meet these user requirements (Fazolallahi 1984). Multi-criteria decision making (MCDM) procedures can be used whenever competing objectives have to be satisfied simultaneously and tested for sensitivity to changes. Such an approach has been used by Chandler (1982) for evaluating information system designs.

The objective of this research is to support the alternative generation and evaluation process in the requirement analysis phase with a methodology that incorporates the use of an MCDM approach. In the proposed methodology, a goal-programming algorithm is used to generate multiple solutions that will satisfy the system requirements to varying degrees. The designer makes trade-offs among alternative solutions and selects one that meets his or her explicitly stated priority structure and implicit preferences. Other MCDM algorithms could also be used to facilitate such a tradeoff, but goal programming was chosen because of its widespread use, its ease of understanding, and the availability of appropriate software.

The next section formulates the requirement analysis problem as a multi-criteria decision making problem. §3 describes the goal programming technique used for solving this problem. §4 describes an application of the methodology and §5 discusses the results. Some extensions to the proposed methodology are discussed in the last section.

## 2. Problem Formulation

Each architecture proposed during the requirement evaluation phase may suggest changes to subsystems in the current architecture in order to satisfy, completely or partially, one or more of the system requirements. For example, a requirement such as “support the market diversification objective"may be satisfied by adding a new process to one of the subsystems in the current architecture, while a requirement such as “provide better customer service" may be satsfied by influencing the operating parameters (e.g., processing times) of existing subsystems such as “order entry," “credit validation," “order filling," etc. Similarl y, user requirements or objectives that restrict the amount of monetary resource available for system development (cost objective), or the amount of risk an organization is willing to take to develop its information systems (rısk objective) can also be expressed in terms of changes in subsystems proposed by each architecture.

The analyst needs to select a combination of subsystem changes, i.e., a proposed system architecture, that will satisfy various user requirements in the “best" possible way. The conflicting nature of user requirements (e.g., cost minimization vs. processing time reduction) requires that a user make the necessary trade-offs in determining the “best" possible alternative to meet these requirements. Thus, the problem of requirement evaluation becomes one of generating several alternate system architectures to satisfy user requirements and selecting one that “best" meets these requirements from the user's perspective.

As described earlier, a system architecture can be represented by a number of manual and automated subsystems and each subsystem can have associated with it several possible designs. Thus, $X _ { t k }$ represents desıgn k of subsystem i. $X _ { t k }$ takes a value of 1 in a given architecture (alternative) if design k is chosen for subsystem l; otherwise it will be 0. Let there be N such subsystems in the architecture and let $K _ { t }$ represent the number of possible designs for subsystenı i. For clarity of explanation, only three sets of requirement objectives (time, cost, and risk) will be considered here. The formulation can be easıly augmented to include other objectives.

## Time-Related Objectives

This set includes the objectives which express the time needed to process certain information, or the elapsed time between the request and delivery of information. Thus, management may desire to have order processing, customer complaint processing, and vendor invoice processing done under certain cycle time limits. For example, an objective might be to reduce the total tiine to process a customer order by redesigning the manual and computer processes involved. A data flow diagram or other form of system representations can be used to identify the set of subsystems, $A ( \ j ) , j \in J$ affecting a time objective j (§4 illustrates the use of data flow diagrams for this purpose). Here, J will represent the number of time objectives. The time related objectives can be expressed as a function of decision variable $X _ { t k }$

$$
\sum_ {i \in A (j)} \sum_ {k \in K _ {i}} t _ {i k} x _ {i k} \leq G _ {j}, j \in J, \text { where }\tag{1}
$$

$G _ { \jmath }$ represents the target value of time for objective $j ,$ $t _ { x k }$ represents the processing time required in subsystem i under design $k ,$ and $K _ { \iota }$ represents the number of alternative designs for subsystem i.

## Cost-Related Objectives

The cost of automating a subsystem consists of one-time investment costs and recurring operating costs. The investment costs include the cost of hardware, software (packages and development), conversion, installation, training, etc. The operating costs include the cost of data entry, output, storage, maintenance, etc. Since a number of subsystems can share their information processing resources, there can be a significant overlap in these costs. This sharing of resources may be due to the use of the same data file or software module, common devices for data-entry, or similar training requirements, etc.

The estimation of the system cost and the allocation of overhead cost among candidate subsystems is difficult. We recognize that no satisfactory solution exists to this cost allocation problem. The cost-related objectives formulated in the model are designed to be flexible enough to work with the cost allocation procedures used by organizations. The model will provide satisfactory results if the cost allocation scheme used by the organization captures the relative cost of alternative system architectures.

A number of methods have been proposed in the literature for estimating system cost (Albrecht 1979, Benbasat and Vessey 1980, Boehm 1981, Perry 1985). Some of these are: judgment, breadboarding, historical experience, function points, standardized estimates, centralized estimating and risk analysis. For example, breadboarding is based on task categorization and comparison of costs associated with similar tasks, while the function point methodology relates development effort for a system to the specific business functions it supports (Albrecht 1979). Refer to Boehm (1981) and Albrecht (1979) for a detailed review of cost estimation techniques. The problem of estimating project costs and allocating overhead expenses has also been addressed in the project planning and management literature (Brill 1984, Perry 1985, Framel 1990). Although a detailed discussion of this issue is beyond the scope of this paper, a broad framework for subsystem cost estimation is presented in the following paragraphs.

(a) The investment costs incurred to convert each subsystem from its current design to a new design can be broadly categorized under: hardware, software, manpower, installation, conversion and training. Similarly, items included in the operating cost of each subsystem in its new configuration can be grouped into categories such as data entry, output, data storage, maintenance, etc. The above costs can be estimated using any of the estimation techniques described in the literature with the assumption that all other subsystems will remain unchanged.

(b) From the cost categories described above, those categories in which cost saving can be achieved because of the overlapping use of resources by interacting subsystems must be identified. The objective in explicitly identifying the overlapping use of resources is to recognize their impact on the total system cost when a number of interacting subsystems are computerized together. In general, some of the resources used to develop and maintain individual subsystems can be eliminated or reduced by computerizing both subsystems and should be subtracted from the total cost. For example, let us assume that the training cost for subsystems A & B are \$10,000 and \$7,000 respectively. If both these subsystems are automated simultaneously, the total training cost of subsystems A & B may only be \$12,000, thus representing a saving of \$5,000. This saving may be due to the similarity of interfaces in the subsystems and/or due to the existence of common user groups. Thus, savings in the investment and operating cost of subsystems using overlapping resources can be estimated

(c) The total cost expression can then be represented as:

$$
\mathrm{TC} = \sum_ {i \in N} \sum_ {k \in K _ {i}} C _ {i k} x _ {i k} - \sum_ {i \in N} \sum_ {k _ {1} \in K _ {i}} \sum_ {p \sim i} \sum_ {k _ {2} \in K _ {p}} O R _ {i k _ {1} p k _ {2}} x _ {i k _ {1}} x _ {p k _ {1}}\tag{2}
$$

where $C _ { \iota k }$ represents the net present value of the stream of cash outflows (investment and operating costs) associated with implementing the kth design of subsystem i over the planning horizon with the assumption that all other subsystems will remain unchanged, and $O R _ { \iota k _ { 1 } \iota ^ { k _ { 2 } } }$ represents the cost savngs due to the Overlapping use of Resources by design $k _ { 1 }$ of subsystem i and design $k _ { 2 }$ of subsystem p.

## Risk-Related Objectives

The risk in implementing the design of a subsystem is defined in terms of the likelihood that the subsystem will not be developed and implemented successfully. A “system success" can be interpreted in many different ways. One of the common interpretations is the successful development of a system so that it can provide the required services. This should be evaluated at the feasibility analysis stage. Only the feasible alternatives, i.e., those that can be implemented as designed and provide the required services, are considered here.

In spite of this screening, there is still some risk associated with the development and implementation of the alternatives that are considered feasible. Several factors such as hardware and software failure, excessive development cost and time, excessive manpower training requirements, etc. may result in either partial implementation or abandonment of a system. The magnitude of this risk depends on factors such as the nature of the subsystem, its size and complexity, the type of technology proposed to be used in the system, the experience level of the people responsible for implementation, and the previous experience of the organization in developing such systems. The risk objective is formulated as one that minimizes the overall likelihood of failure of the system, which is expressed as folows:

$$
\sum_ {i \in N} \sum_ {k \in K _ {i}} f _ {i k} x _ {i k} \leq 0\tag{3}
$$

where $f _ { \iota k }$ represents the likelihood of failure in an effort to implement design k of subsystem i.

The above expression assumes a weak interaction between subsystems, i.e., given the specification of a subsystem, its successful design and implementation can be looked at independently from other subsystems. This can be justified based on the fact that, in many large systems, subsystems are designed to be fairly independent and may be developed by different groups. However in the eventual implementation of the system, one needs to establish proper interfaces between subsystems in order to ensure the success of the overall system. In the piesent model, the risk in implementing these interfaces has not been considered. The augmented model described in §6 considers such an interface risk

The process of determining the value of $\dot { f } _ { i k }$ is judgmental. A scoring methodology (Plebani and Jain 1981), which has been widely and successfully used in project selection, is recommended here to help quantify this risk. In this methodology, a group of managers experienced in managing similar projects identifies a set of factors which may affect the likelihood of failure in implementing the proposed subsystem design. These factors are then assigned appropriate weights. Each alternative design is scored on a scale of 0 to 100 against every factor identified above. The resulting final score for each subsystem is calculated by multiplying the criteria scores with the weights and adding the results. The final score represents the value of $\scriptstyle { \mathcal { f } } _ { \imath k }$ . This process is illustrated in §4 for the sample case. The objective (3) implies that, given everything else equal, management would prefer a combination of subsystems whose designs yield a likelihood of failure as close to zero as possible. Other methods such as AHP (Saaty 1980) can also be used to estimate the value of $\cdot f _ { \imath k }$

## Resource Constraints

The purpose of generating and evaluating alternative system architectures is to consider various feasible designs of the subsystems and to select a combination of subsystem designs that will meet competing user objectives. In selecting these designs, a limitation on any resource such as system development staff, system hardware, storage capacity and available budget should be considered. These limitations can be expressed as constraints that cannot be violated.

If $r _ { q t k }$ represents the additional resource, q, allocated/apportioned to implement design k of subsystem $i ,$ then this resource constraint can be expressed as

$$
\sum_ {i \in N} \sum_ {k \in K _ {i}} r _ {q i k} x _ {i k} \leq R _ {q} \quad \text { for } q \in Q,\tag{4}
$$

where $R _ { g }$ represents the level of additional resource $q$ available, and $Q$ represents various types of resources.

Since only one design of a subsystem can be selected for implementation, the following constraints must be added.

$$
\sum_ {k \in K _ {i}} x _ {i k} = 1 \quad \text { for   all } i \in N.\tag{5}
$$

It is also possible to express any incompatibility among subsystem design combinations as a constraint. For example, if any subsystem $\cdots _ { i } , \boldsymbol { { \scriptscriptstyle \cdot } } ,$ in design m is incompatible with any subsystem $" \boldsymbol { j } ^ { \flat }$ in design n, then one can express it as follows:

$$
x _ {i m} + x _ {j n} \leq 1, \quad i \neq j.
$$

This can occur, for example, if a given subsystem in design m cannot effectively communicate information to a subsystem in design n.

Additional objectives/constraints that require, for example, a subsystem to maintain a particular design can be expressed by assigning a value of 0 or 1 to the decision variable associated with that subsystem for that design. Thus the alternative generation problem can be stated as:

Find a set of subsystem designs represented by the variables $X _ { s k }$ that will achieve a set of objectives expressed in equations (1), (2) and (3), subject to the constraints expressed in (4) and (5).

## 3. Solution Methodology

The multiple-criteria problem formulated in $\ S 2$ can be solved by using a modified O-1 linear integer goal programming model. Each element of decision vector X represents the decision on whether to alter the design of a subsystem i to design k or not. The objectives have been grouped as:

1. Time-related objectives;

2. Total cost minimization objectives;

3. Total risk minimization objectives.

A given problem may involve one or more of these objectives. Additional objectives can also be specified. The available resources are represented as constraints.

The general goal programming model typically has two types of constraints: structural constraints and goal constraints. The former represents a set of existing restrictions that define the feasible solution space that must be adhered to before a satisfactory solution can be considered. The latter represents a set of goal constraints that include the objectives of the problem. The structural constraints are assigned the highest priority and are treated as absolute goals. The goal constraints can be assigned different preemptive priorities. Goal constraints at the same priority level can be assigned different weights. The model tries to achieve the higher priority goals to the fullest possible extent before lower priority goals are considered. The general goal programming technique is described in a number of sources, e.g., Ignizio (1976), Lee (1972), etc.

Generating the priority associated with various user requests has been the subject of much research in the MIS planning literature. Methodologies such as the strategic grid (Cash et al. 1988), strategic set transformation (King 1978), and links to corporate objectives (Davis and Wetherbe 1983) have been proposed for deriving priorities. Steering committees that include user/development personnel may also be used to rank order the importance of user requests, or to assign relative weights to the user requests. In the present model, all the time-related objectives are assigned the same priority. However, different relative weights are assigned to various time objectives based on their importance. Similarly, all the cost minimization objectives are assigned the same priority and individual cost objectives are assigned different relative weights. The set of risk minimization objectives are also treated in a similar manner.

Preemptive priorities are then assigned to these three levels of objectives. Assignment of such preemptive priorities limits to some extent the types of trade-off that can be made. However, by using realistic target values for each objective and performing sensitivity analysis (discussed later), one can overcome this limitation. Alternatively, all time-, cost-, and risk-related objectives can be assigned the same level of priority with each objective having different relative weight. In this case, however, the difference in the units of measure for time, cost, and risk makes such an assignment of relative weights and the associated interpretation of the results very difficult.

The objectıves formulated in §2 are represented here as goals by adding deviation variables. A deviation variable reflects either the underachievement (negative deviation) denoted by $d _ { \iota } ^ { - }$ , or overachievement (positive deviation) denoted by $d _ { \iota } ^ { + }$ , of objective i. All deviation variables are assumed to be nonnegative. In a goal programming framework, the following procedure is used to mathematically transform an objective into a goal constraint using the deviation variables.

Consider the objective function expressed in general terms as $f _ { \iota } ( \Vec { x } )$ , representing objective i as a function of decision variables ${ \bar { x } } = ( x _ { 1 } , x _ { 2 } , \ldots , x _ { n } )$ . Let $b _ { \iota }$ represent the value of aspiration level (target value) associated with objective i. The three possible forms of a goal are:

TABLE 1  
Transformation to Goal Programming Format

<table><tr><td>Goal Type</td><td>Goal Programming Form</td><td>Deviation Variables to be Minimized</td></tr><tr><td> $f_{i}(\bar{x}) \leq b_{i}$ </td><td> $f_{i}(\bar{x}) + d_{i}^{-} - d_{i}^{+} = b_{i}$ </td><td> $d_{i}^{+}$ </td></tr><tr><td> $f_{i}(\bar{x}) \geq b_{i}$ </td><td> $f_{i}(\bar{x}) + d_{i}^{-} - d_{i}^{+} = b_{i}$ </td><td> $d_{i}^{-}$ </td></tr><tr><td> $f_{i}(\bar{x}) = b_{i}$ </td><td> $f_{i}(\bar{x}) + d_{i}^{-} - d_{i}^{+} = b_{i}$ </td><td> $d_{i}^{-} - d_{i}^{+}$ </td></tr></table>

$$
1. f _ {i} (\bar {x}) \leq b _ {i},
$$

$$
2. f _ {i} (\bar {x}) \geq b _ {i},
$$

$$
3. f _ {i} (\bar {x}) = b _ {i}.
$$

Regardless of the form, any of these relations can be transformed into the goal programming format by adding negative deviation variable $( d _ { \iota } ^ { - } )$ and subtracting the positive deviation variable $( d _ { \iota } ^ { + } )$ . The transformation process is summarized in Table 1. The deviation variables that are to be minimized to satisfy the goal are also indicated.

In the requirement analysis problem, various time, cost and risk related objectives are considered as goal constraints. The structural constraints are resource limitation constraints, constraints that limit a subsystem to a single design, and other translation constraints. The translation constraints are needed to replace the product terms such as $X _ { \iota k _ { 1 } } X _ { p k _ { 2 } } , \dots$ . in the cost equation (2) by linear variables such as $Y _ { \imath k _ { 1 } p k _ { 2 } } , \ldots$ . This is feasible because $X _ { \iota k _ { 1 } } , X _ { p k _ { x } }$ are zero-one integer variables and their product terms are also zero-one integer variables. For example, $X _ { \iota k _ { 1 } } X _ { p k _ { 2 } }$ can be linearized by replacing it with a new variable $Y _ { \iota k _ { 1 } p k _ { 2 } }$ along with the following two constraints to ensure that $Y _ { _ { I k _ { 1 } p k _ { 2 } } }$ takes a value 1 only when both $X _ { \iota k _ { 1 } }$ and $\mathbf { X } _ { p k _ { 2 } }$ take a value 1:

$$
\begin{array}{l} X _ {i k _ {1}} + X _ {p k _ {2}} - 2 Y _ {i k _ {1} p k _ {2}} \geq 0, \\ X _ {i k _ {1}} + X _ {p k _ {2}} - Y _ {i k _ {1} p k _ {2}} \leq 1, \end{array}
$$

In the above goal programming model, the user is required to estimate or specify, based on judgment, the values of many parameters such as coefficients of the variables, right-hand side values, preemptive priorities and weights. In a practical case, the values of the coefficients are estimates and therefore are uncertain in nature, while the right-hand side values are the target values of the objective and are based on subjective judgments. These values are subject to errors and/or reconsideration during the planning process. Thus, it is important to have some indication as to how sensitive a solution is to changes in input parameter values.

The modified Balas algorithm and post-optimality and sensitivity analysis approach proposed by Wilson and Jain (1988) can be used to solve the above goal programming problem. This approach modifies the implicit enumeration algorithm of Balas so as to provide a set of Z best feasible solutions (as measured by the prioritized goal constraints) rather than a single solution (Mehta and Wilson 1981). The value of Z is selected by the decision maker. Using the solutions in the set, upper and lower bound values for the single parameters (one parameter at a time) are obtained, while ensuring that the optimal solution still remains in the set. The parameters for which the upper and lower bound values can be obtained are: coefficients of the variables in the goal constraints, right-hand side values of the goal constraints, and the relative weights assigned to the goal constraints. Similarly, multiple parameter postoptimality analysis can also be performed if many parameter values change simultaneously (Wilson and Jain 1988). The above postoptimality and sensitivity analysis is performed for a particular set of preemptive priority assignments. The model needs to be run again to try different priority assignments.

Thus the above analysis provides decision makers with a range of values over which their estimates of the coefficient values, the values of the right-hand side, and the relative weights may vary without moving the optimal solution outside the set Z. These ranges indirectly provide a confidence interval, i.e., ranges of values within which a decision maker can be confident about the decision. The decision maker can also use this algorithm to perform what-if analysis. For this purpose, the sensitivity analysis can be implemented in such a way that ¿ decision maker can input the new value of a coefficient (e.g., a modified cost of implementing a subsystem or a change in the risk of implementing a subsystem). The algorithm can then check whether this change will cause the optimal solution to be outsicle the set of Z solutions or not. If the optimal solution is in the set, then the algorithm can evaluate the new objective function values for all solutions in that set; otherwise the model needs to be rerun with the new values for the coefficient. Similar analyses can be performed by the decision maker to determine the effect of changes in the target values of the objectives and the relative weights assigned to different goals in the optimal solution. Another advantage of this method is that it provides a number of good feasible solutions which the decision maker can evaluate in terms of other intangible, subjective, and political considerations which cannot be modeled explicitly. Thus the decision maker is not bound by a single solution but has a number of alternatives to choose from. The number of alternatives generated (value of Z) should preferably be less than 10 to allow easier comparison by the decision maker.

## 4. An Example Application

The methodology described above was used by a major midwestern utility company during a feasibility study for the automation of its cash management system. The treasury department of the company is responsible for managing the firm's cash reserves, cash flow, and investments. Payments are made by the utility customers at many geographically dispersed district banks and this deposit information is transmitted to the treasury department the next day. The treasury uses this information to make appropriate deposits and wire transfers among its member banks and the main bank, and to decide on certain short-term investiments. The company, at the time of the study, incurred significant opportunity costs in managing its cash because of the lag between customer payments and investment decisions

The primary objective in developing the new system was to obtain timely data on deposits to accelerate investment opportunities. However, management was also concerned with maximizing the success in undertaking this information systems project and keeping the overall cost of the project below the estimated opportunity costs incurred in one year. One other objective w as to achieve the automation of the district ledger subsystem.

CASH MANAGEMENT SYSTEM  
![](/api/attachments/GWM86WV6/fulltext/images/2dc08ab5d20b4bc8f8c8b1edbcbb3d51d241186e00efd1f4261544a10760556f.jpg)  
FiGURE 1. The System Architecture and Its Subsystems for the Utility Company.

The project team formed to complete this study included: two operations clerks and a cash manager from the utility, and two graduate students and a professor from a university. Initial data about the system were obtained using interview techniques, and data flow diagrams were used to document the system and obtain feedback. The project meetings were held weekly in the early stages of the project and monthly in the later stages. The entire study took about nine months to complete and was presented to the management team which included the treasurer and two district office managers. While no MIS professionals were directly involved in the project team in the preliminary stages of the study (partly to get an unbiased view), a number of MIS application managers were actively consulted in the later stages, especially to help estimate the cost/time parameters.

An analysis of the current system resulted in the identification of the following six subsystems within the treasury department that relate to the task of cash management:

1. SS1-Cash Reporting Subsystem

2. SS2-Transfer Selection Subsystem

3. SS3-Deposit Transfer Subsystem

4. SS4-Wire Transfer Subsystem

5. SS5-Bank Ledger Subsystem

6. SS6-District Ledger Subsystem

The data flow diagram in Figure 1 shows the interaction among these subsystems in terms of the data they share and the files they control. The four objectives of the system were identified as: time, cost, risk and district ledger updating. The alternative designs of the 6 subsystems were identified as: current, i.e. manual; and altered, i.e. automated. Thus, a total of 64 (26) different contigurations were possible. Using the methodology described earlier, several design alternatives were generated for management consideration. The details of the problem formulation and the solutions are described below.

MCDM Approach in Requirement Analysis

<table><tr><td colspan="4">TABLE 2Process Sequence</td></tr><tr><td colspan="4">GOAL 1: G1 ≤ 3.5 HOURS</td></tr><tr><td>SS1</td><td>→ SS2</td><td>→ SS5</td><td>→ SS3</td></tr><tr><td>19.0/0.5</td><td>0.75/0.25</td><td>1.50/0.5</td><td>1.25/0.75</td></tr><tr><td colspan="4">GOAL 2: G2 ≤ 3.5 HOURS</td></tr><tr><td>SS1</td><td>→ SS2</td><td>→ SS5</td><td>→ SS4</td></tr><tr><td>19.0/0.5</td><td>0.75/0.25</td><td>1.50/0.5</td><td>1.25/1.00</td></tr><tr><td colspan="4">LEGEND: PROCESS TIMES UNDER CURRENT/ALTERED STATE</td></tr></table>

## Goal Constraints

Goal 1: Satisfy Timeliness Requirement. The time-related goals called for reducing the processing times associated with deposits and wire transfers to no more than 3.5 hours. The paths that affect these goals and the estimates of the time spent in each subsystem on the path under the current and proposed designs are shown in Table 2. The time estimates under the current system were provided by the treasury department personnel and the estimates under the automated design were obtained from corporate systems personnel. The resulting time goals can be expressed as follows:

$$
1 9 X _ {1 1} + 0. 5 X _ {1 2} + 0. 7 5 X _ {2 1} + 0. 2 5 X _ {2 2} + 1. 2 5 X _ {3 1} + 0. 7 5 X _ {3 2} + 1. 5 X _ {5 1} + 0. 5 0 X _ {5 2} \leq 3. 5,
$$

$$
1 9 X _ {1 1} + 0. 5 X _ {1 2} + 0. 7 5 X _ {2 1} + 0. 2 5 X _ {2 2} + 1. 2 5 X _ {4 1} + 1. 0 0 X _ {4 2} + 1. 5 X _ {5 1} + 0. 5 0 X _ {5 2} \leq 3. 5.\tag{6}
$$

Goal 2: Minimization of Information System Cost. This objective minimizes the cost of altering the current design of subsystems to the new design. This cost consists of the one time investment cost and the recurring operating costs. The operating cost component included only the cost of data entry and output as they both result in direct cash outlay. The costs of running the computer (CPU costs), storage, and maintenance were ignored since these were treated as fixed overhead by the organization and were not allocated to each user application. Under a different cost allocation scheme, some of these costs may be explicitly included in the cost expression. Table 3 represents the cost of changing the design of each subsystem to the new automated design and the cost of its operation. The above costs were estimated under the assumption that the design of all other subsystems will remain unchanged. In addition, the table also shows the possible cost savings $( \mathbf { e } . \mathbf { g } . , O R _ { 1 z } )$ due to the overlapping use of resources by interacting subsystems (e.g., 1 & 2). The target value of development cost was \$50,000. The resulting cost expression is:

TABLE 3  
Estımated Cost Parameters in Dollars

<table><tr><td rowspan="2">Cost Parameter</td><td colspan="4">Development Cost</td><td colspan="5">Operation Cost</td><td rowspan="2">Total</td></tr><tr><td>Hardware</td><td>Software</td><td>Conversion</td><td>Installation</td><td>Training</td><td>Data Entry</td><td>Output</td><td>Sub-total</td><td>Discounted Operation Cost</td></tr><tr><td>C1</td><td>49000</td><td>5000</td><td>0</td><td>7000</td><td>10000</td><td>0</td><td>100</td><td>100</td><td>379.1</td><td>71379</td></tr><tr><td>C2</td><td>700</td><td>1500</td><td>200</td><td>4000</td><td>1050</td><td>600</td><td>200</td><td>800</td><td>3032.8</td><td>10483</td></tr><tr><td>C3</td><td>700</td><td>500</td><td>0</td><td>600</td><td>200</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>2948</td></tr><tr><td>C4</td><td>700</td><td>700</td><td>200</td><td>1000</td><td>200</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>3748</td></tr><tr><td>C5</td><td>700</td><td>1000</td><td>800</td><td>1000</td><td>600</td><td>600</td><td>50</td><td>650</td><td>2464.2</td><td>6564</td></tr><tr><td>C6</td><td>700</td><td>500</td><td>800</td><td>1000</td><td>200</td><td>300</td><td>0</td><td>300</td><td>1137.3</td><td>4337</td></tr><tr><td>OR12</td><td>0</td><td>100</td><td>0</td><td>0</td><td>250</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>1298</td></tr><tr><td>OR16</td><td>0</td><td>100</td><td>0</td><td>0</td><td>250</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>1298</td></tr><tr><td>OR23</td><td>0</td><td>100</td><td>0</td><td>0</td><td>250</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>1298</td></tr><tr><td>OR24</td><td>0</td><td>100</td><td>0</td><td>0</td><td>250</td><td>200</td><td>50</td><td>250</td><td>947.8</td><td>1298</td></tr><tr><td>OR25</td><td>0</td><td>400</td><td>0</td><td>0</td><td>900</td><td>800</td><td>100</td><td>900</td><td>3411.9</td><td>4712</td></tr></table>

$$
\begin{array}{r l} 7 1 3 7 9 X _ {1 2} + 1 0 4 8 3 X _ {2 2} + 2 9 4 8 X _ {3 2} + 3 7 4 8 X _ {4 2} + 6 5 6 4 X _ {5 2} + 4 3 3 7 X _ {6 2} - 1 2 9 8 X _ {1 2} X _ {2 2} \\ & - 1 2 9 8 X _ {1 2} X _ {6 2} - 1 2 9 8 X _ {2 2} X _ {3 2} - 1 2 9 8 X _ {2 2} X _ {4 2} - 4 7 1 2 X _ {2 2} X _ {5 2} \leq 5 0, 0 0 0. \end{array} \tag {7}
$$

Goal 3: Minimize Risk of Failure. The application development managers were consulted to obtain the likelihood of failure of each subsystem under automation. They evaluated the likelihood of failure by assigning scores for each subsystem against a number of criteria (see Table 4).

Using the criteria weights assigned by them, the final likelihood of failure score for each subsystem was calculated. Assuming that the risk of failure to remain under the current design is zero, the risk objective can be expressed as:

TABLE 4  
Risk Assessment

<table><tr><td rowspan="2">Criterion</td><td colspan="7">Score Representing Likelihood of Success</td></tr><tr><td>Weight</td><td>SS1</td><td>SS2</td><td>SS3</td><td>SS4</td><td>SS5</td><td>SS6</td></tr><tr><td>New hardware</td><td>0.20</td><td>30</td><td>05</td><td>05</td><td>05</td><td>05</td><td>05</td></tr><tr><td>New software</td><td>0.25</td><td>35</td><td>10</td><td>0</td><td>0</td><td>10</td><td>0</td></tr><tr><td>Familiarity of the organization with similar systems</td><td>0.20</td><td>50</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td>Experience level of user/designer with similar systems</td><td>0.35</td><td>50</td><td>05</td><td>05</td><td>05</td><td>05</td><td>05</td></tr><tr><td>Total weighted score representing likelihood of failure</td><td></td><td>42.25</td><td>9.25</td><td>6.75</td><td>6.75</td><td>9.25</td><td>6.75</td></tr></table>

$$
4 2. 2 5 X _ {1 2} + 9. 2 5 X _ {2 2} + 6. 7 5 X _ {3 2} + 6. 7 5 X _ {4 2} + 9. 2 5 X _ {5 2} + 6. 7 5 X _ {6 2} \leq 0.\tag{8}
$$

Goal 4: Automate District Ledger Subsystem. Management indicated a desire for automating the district ledger subsystem (SS6). However, this goal is of low priority and is pursued only after all other objectives and goals are achieved to the degree desired. This objective is represented as:

$$
X _ {6 2} = 1.\tag{9}
$$

## Structural Constraints

Since only one design of each subsystem can be implemented, structural constraints, as shown in equation (5), were added. For example, the structural constraint for subsystem 1 would be:

$$
X _ {1 1} + X _ {1 2} = 1
$$

In addition to these constraints, other translation constraints that translate the product terms $X _ { 1 2 } X _ { 2 2 } , X _ { 1 2 } X _ { 6 2 } , X _ { 2 2 } X _ { 3 2 } , X _ { 2 2 } X _ { 4 2 }$ , and $\boldsymbol { \chi } _ { 2 z } \boldsymbol { X } _ { 5 2 }$ of the cost equation to the appropriate linearized variable $Y _ { 1 2 , 2 2 } , \dots , Y _ { 2 2 , 5 } $ , were also added to the model (as discussed in the previous section).

## Management Preference Structure

The above objectives and goals are conflicting in nature. Improving the timeliness of the information tends to increase system costs and may increase the likelihood of failure as more changes are introduced into the organization. To make these tradeoffs, management provided the following preference structure:

<table><tr><td>Priority</td><td>Goal</td></tr><tr><td>1</td><td>Minimize process time deviation</td></tr><tr><td>2.</td><td>Minimize total cost deviation.</td></tr><tr><td>3.</td><td>Minimize the total score representing the likelihood of failure.</td></tr><tr><td>4</td><td>Automate the subsystem that updates the district ledger (SS6).</td></tr></table>

The problem is to determine the vector X that satisfies the prioritized goal constraints (6), (7), (8), and (9) while meeting the structural constraints. The next section presents the solution of the above problem and discusses the results.

## 5. Discussion of Results

The problem formulated in the previous section was solved using the modified interactive goal programming algorithm described in Wilson and Jain (1988). The FORTRAN program implementing the algorithm was executed on a DEC System 1060. The solution was obtained in 0.66 seconds of CPU time. In this case a set of 4-best feasible solutions were generated (shown in Table 5).

The Wilson and Jain (1988) methodology was used to determine the upper and lower bounds on the values of each coefficient, right-hand side values, and relative weights. This gives the range in which the values of these parameters can change without moving the optimal solution outside the set. This allowed management to evaluate the sensitivity of the alternate plans to changes in the estimated values of parameters. Management also used this technique to perform what-if analysis as described in §3.

In this particular case, solution $P _ { 1 }$ dominates $P _ { 2 }$ and $P _ { 3 }$ dominates $P _ { 4 }$ . Solution $P _ { 3 }$ is associated with least risk and cost; however, for additional risk and cost, $P _ { 1 }$ allows for the automation of subsystem 6 as well. Note, however, that both the solutions $P _ { 1 }$ and $P _ { 3 }$ cost 27 to 30 thousand dollars more than what was budgeted. If this additional expenditure is too large, the user may wish to run the problem again with a higher priority assigned to the cost objectives.

TABLE 5

<table><tr><td colspan="3">Alternative Planning Strategies and Their Achievement Levels</td></tr><tr><td>System Portfolio</td><td>Subsystems to be Automated</td><td>Goals/objectives Achieved</td></tr><tr><td rowspan="3">#1</td><td>Cash reporting subsystem (SS1)</td><td>Time Goal—achieved</td></tr><tr><td>Bank ledger subsystem (SS5)</td><td>Cost objective—underachieved by $30,982</td></tr><tr><td>District ledger subsystem (SS6)</td><td>Risk objective—underachieved by 58.25 Computerize SS6—yes</td></tr><tr><td rowspan="3">#2</td><td>Cash reporting subsystem (SS1)</td><td>Time Goal—achieved</td></tr><tr><td>Deposit transfer subsystem (SS3)</td><td>Cost objective—underachieved by $30,980</td></tr><tr><td>Bank ledger subsystem (SS5)</td><td>Risk objective—underachieved by 58.25 Computerize SS6—no</td></tr><tr><td rowspan="2">#3</td><td>Cash reporting subsystem (SS1)</td><td>Time Goal—achieved</td></tr><tr><td>Bank ledger subsystem (SS5)</td><td>Cost objective—underachieved by $27,943 Risk objective—underachieved by 51.50 Computerize SS6—no</td></tr><tr><td rowspan="2">#4</td><td>Cash reporting subsystem (SS1)</td><td>Time Goal—achieved</td></tr><tr><td>Transfer selection subsystem (SS2)</td><td>Cost objective—underachieved by $30,510 Risk objective—underachieved by 51.50 Computerize SS6—no</td></tr></table>

Additional alternative solutions can be generated by specifying a larger value of Z. These alternative solutions allow for trade-offs and rethinking on the part of the user before acceptance of a solution for implementation. Also, many subjective factors that often cannot be formulated mathematically in the model can be considered effectively at this stage in narrowing down the user's choice to one alternative

In this particular case, the company used other subjective information and selected the alternative P2, which called for the automation of subsystems 1, 3, and 5. One of the main reasons for this choice was that the bank ledger system was considered much more critical as it maintains bank balances that are constantly changing due to transfers made among banks. A real-time maintenance of bank ledgers provides quick information on bank balances before and after transfers. If this requirement was known earlier in the investigative step, it could have been expressed as a constraint in the problem (the Bank Ledger system is a necessary prerequisite to the Transfer System). However, it is not often feasible for management to a priori state these prerequisites. A methodology such as this can thus enhance evaluation of alternatives using information that is either subjective or difficult to extract from the user in the investigative stage.

In addition, management requested the generation of cash flow estimates if the subsystems in alternative P2 were implemented in different orders (1, 3, and 5; 3, 1, and 5; 5, 3, and 1; etc.). They finally chose to implement the alternative P2 in the order 5, 3, and 1, as it required low initial investment and afforded them time to learn the system before networking various branch offices.

Overall, the reaction of the management to the MCDM approach was very positive. The methodology required their involvement in setting priorities, defining objectives, estimating certain parameter values, etc. While this type of information exchange between an analyst and a user group occurs informally, the approach proposed here made the user aware of the significance of the information they were providing and its potential impact on any proposed system design. The user involvement made the eventual design decision a product of their own judgment rather than that of an analyst, and this increased their commitment to the successful implementation of the proposed design.

## 6. Augmenting the Model

The decision variables, objectives, and structural constraints together constitute the multicriteria model for generating and evaluating alternative system architectures. It is certainly possible to alter/augment the model using other types of objectives, constraints, and variables. This section gives one example of such an augmentation.

In some applications, the risk associated with integrating two or more subsystems can be significant. To consider these integration risks, the model can be augmented by adding integration risk estimates to the risk objectives.

The overall risk expression (3) in the augmented model becomes

$$
\sum_ {t \in N} \sum_ {k \in K _ {t}} f _ {i k} x _ {i k} + \sum_ {t \in N} \sum_ {k _ {1} \in K _ {t}} \sum_ {l > t} \sum_ {k _ {2} \in K _ {t}} I R _ {i k _ {1} l k _ {2}} x _ {i k _ {1}} x _ {i k _ {2}} \leq 0
$$

where $I R _ { \iota k _ { 1 } l k _ { 2 } }$ represents the risk in integrating kth design of subsystem i with $k _ { 2 } ^ { \cdot }$ th 7 design of subsystem l. The integration risk may depend on a variety of criteria such as the strength of the coupling between subsystems / and k and similarity in the type of technology used to implement subsystems t and k. A scoring methodology similar to the one described in §2 can be used to estimate the integration risk.

## 7. Conclusions

In this paper, a methodology for generating and evaluating system alternatives during the requirement analysis phase is presented. The objectives/goals of the organization are related to the system architecture by expressing them as a function of organizational resources and the subsystem's characteristics such as time, cost, risk, etc. These objectives are prioritized and a set of solutions (alternative system architectures) that satisfy these objectives is presented to the user. In addition, the methodology explicitly considers the possibility that the candidate subsystems may share certain common resources and, hence, will have an overlapping influence on the achievement of the user objectives. Each solution generated by the methodology includes a combination of subsystems that will be altered from their current design to a new design. The goal programming algorithm was used to make the necessary trade-offs among these competing solutions.

The methodology was used in the analysis of alternative cash management system architectures at a midwestern utility company and was found to be effective in: (1) getting the user actively involved in the analysis pnase and (2) facilitating the decision making process.

There are several impediments to widespread user involvement in the analysis phase, especially when a new methodology is being proposed. The first is the difficulty of obtaining management understanding of the methodology used, so that they can play an effective role in the analysis phase. The second is convincing management that the time they expend to provide the needed information and make the required subjective judgements will ultimately payoff in the design of a system that will better meet the needs of the organization.

At the midwestern utility, the team first described to management the methodology and its ability to link organizational goals with system architecture. By showing management how the assumptions they made can impact the systems chosen, we were able to educate them on the role they can play in system design. We also found management willing to provide goal priorities—probably because they could see how this information can significantly change the way the systems are chosen for development and implementation. Since the methodology allowed them to alter their priorities easily, they were more than willing to assign initial priorities and alter them as the situation demanded it. In summary, management was willing to commit the time necessary to make the selection process effective, because the methodology made them an integral part of the system selection process.\*

\* Edward Stohr, Associate Editor. This paper was received on January 29, 1988 and has been with the authors 18, months for 5 revisions

## References

Albrecht, A. J., “Measuring Application Development Productivity," in Share-Guide, 1979, 83–92.

Anthony, R. N., Plannıng and Central System: A Framework for Analysis, Harvard Business School Press Boston, 1965.

Benbasat, I. and 1. Vessey, “Programmer and Analyst Time/Cost Estimation," MIS Quarterly, (June 1980), 31–43.

Boehm, B. W., Software Engineering Economics, Prentice-Hall, Englewood Cliffs, NJ, 1981

-, “Software Engineering Economics," IEEE Transactions on Software Engineering, SE-10, 1, (1984), 4–21.

Brill, Alan E. (Ed.), Technıques of EDP Project Management: A Book of Readıngs, Yourdon Press, New York, 1984.

Carlson, W. M., “Business Information Analysis and Integration Technique (BIAIT)—The New Horzon," Data Base, 10, 4, (September 1979), 3–9.

Cash, J. I., F. W. McFarlan and J. L. McKenney, Corporate Information Systems Management: The Issues Facing Senior Executtves. (2nd Ed.), Irvine Publication, Homewood. IL, 1988

Chandler, J. S., “A Multiple Criteria Approach for Evaluating Information Systems," MIS Quarterly, 6, 1 (March 1982), 61–74.

Davis, G. B. and J. C. Wetherbe, “Developing a Long Range Information Architecture," Proceedings of National Computer Conference, Anaheim, CA, May 1983.

and M. Olson, Management Information Systems, McGraw-Hill, Inc., New York, 1985.

Dickson, Gary and James Wetherbe, Management of Information Systems, McGraw Hill, New York, 1985.

Ewusi-Mensah, K., “Identifying Subsystems in Information Systems Analysis," Information Systems, 9, 2 (1984), 181–190.

Fazolallahi, B., “A Framework for MIS Planning." School of Management, Syracuse University, Syracuse, NY, Ph.D. Dissertation, 1984

Framel, John, “Managing Information Cost and Technologies as Assets," Journal of Systems Management, (February 1990), 12–19.

Gibson, D. G. and R. L. Nolan, "Managing the Four Stages of EDP Growth," Harvard Busıness Review, (January-February 1974).

IBM Corporation, Busıness System Planning—Information System Planning Gude, Pub# GE 20-0527.

Ignizio, J. P., Goal Programmıng and Extensions, Lexington Books, Lexington, MA, 1976.

King, W. R., "Strategic Plannıng for MIS," MIS Quarterly, 2, 1 (1978), 27–37.

Lederer, A. L. and A L. Mendelow, “Issues in Information Systems Planning," Information and Management, 10 (1986), 245–254.

Lee, S. M., Goal Programmıng for Decısion Analysıs, Auerbach Publisher, Philadelphia, PA, 1972.

McLean. E. R. and J. V. Soden (Eds.), Strategic Plannıng for MIS. Wiley-Interscjence, New York. 1977.

Mehta, N K. and G. R. Wilson, “Project Proposals Evaluation: Zero-One Integer Goal Programming Approach," Proceedıngs of the Midwest AIDS Annual Meeting, April 1981.

Perry, E.. Data Processing Budgets—How to Develop and Us’ Efficiently, Prentice-Hall, Inc., Englewood Cliffs. NJ. 1985.

Plebanı, L. and H. K Jain, “Fvaluating Research Proposals with Group Techniques," Research Management, 24, 6 (November 1981), 34–38.

Pyburn. P. J., “Linking the MIS Plan with Corporate Strategy: An Exploratory Study," MIS Quarterly (June 1983).

Rockart, J. F., “Critical Success Factor," Harvard Busıness Revrew, (March-April 1979).

Saaty, T. L., The Analytic Hterarchv Process, McGraw-Hill, New York, 1980

Wetherbe, J. and G. Davis, “Strategic Planning Through Ends/Means Analysis," MIS Research Center, University of Minnesota, working paper, 1982

Wilson, G. R. and H K. Jaın, “An Approach to Postoptimality and Sensitivıty Analysıs of Zero-One Goal Programs," Naval Resear h Logısttcs Quarterly, 35, 1 (February 1988).
