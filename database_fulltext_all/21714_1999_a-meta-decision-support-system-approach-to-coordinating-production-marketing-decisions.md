---
otero_id: 21714
otero_key: "F3DY49YZ"
title: "A meta decision support system approach to coordinating production/marketing decisions"
authors: "Won Jun Lee; Kun Chang Lee"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00009-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A meta decision support system approach to coordinating production<sup>r</sup>marketing decisions

Won Jun Lee <sup>a,)</sup>, Kun Chang Lee <sup>b,1</sup>

<sup>a</sup> Department of Management, College of Business and Economics, UniÕersity of Inchon, Inchon, 402-749, South Korea b Sung Kyun Kwan UniÕersity, Seoul, South Korea

## Abstract

This paper deals with the problem of coordinating production and marketing functions that are traditionally in conflict with each other. Our main concern is to develop a decision support system DSS for coordinating the two functions in aŽ . functionally decentralized firm where each function has information autonomy and makes its own decisions separately with respect to its own local objective function. Previous studies in literature fail to provide practically useful coordination frameworks. Based on coordination theory, this paper proposes a Meta DSS MDSS approach which can effectively solveŽ . the problem of coordinating production and marketing decisions. The MDSS framework we propose is capable of providing guidance for coordinating production and marketing decisions. An example is presented to illustrate the usefulness of the proposed MDSS approach. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Coordination; Production<sup>r</sup>marketing decisions; Meta decision support systems

## 1. Introduction

In most of firms, both production and marketing functions are regarded as two major managerial functions. In general, these two functions are interdependent of each other in many interface areas such as sales forecasting and capacity planning, marketing mix and production planning, inventory management, quality control, and physical distribution <sup>w</sup> <sup>x</sup> 2,20,22 . For example, long term sales forecasts by marketing serves as a basis for planning future capacity expansion. In turn, the capacity of the production facility affects the cost structure and thus the selling price for marketing. A broader product line preferred by marketing is not favored by production because producing more products means too frequent setups that will increase the manufacturing costs.

Despite their close relationship, production and marketing PM decisions are often handled sepa-Ž . rately in functionally decentralized firms, where marketing usually makes decisions without full consideration of production, and vice versa. This separate PM decision-making behavior is reflected in the current literature of production 7 and marketing <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 10 . Consequently, the overall performance is bound to be suboptimal. Many studies in the literature suggest to combine and jointly make the PM decisions to overcome the suboptimal performance of the separate decision-making 3,8,12–15,23,24 . This<sup>w</sup> <sup>x</sup> joint approach however implicitly assumes that a central authority makes all PM decisions. Under functional decentralization, each function has information autonomy and makes its own decisions pertaining to its own decision-making domain. The joint approach is therefore not a viable option for functionally decentralized firms.

Many researchers have stressed the importance of coordinating the two functions in the interface areas to enhance corporate performance 5 . However, the<sup>w</sup> <sup>x</sup> coordination does not appear to be an easy task because production and marketing are usually separate organizational units that possess different action sets, thereby taking different roles in achieving the goal of the entire organization. Furthermore, these two functions make decisions according to their own objectives: marketing seeks profit-maximization while production aiming at cost-minimization. Each function tries to optimize its own goal without full consideration of the other, leading to interfunctional conflicts. These conflicts usually result in degradation of the overall performance at the corporate level. For more on the conflicts and other aspects of the production and marketing interface, refer to Refs. <sup>w</sup> <sup>x</sup> 2,5,20,22 .

This study proposes a new decision support system DSS framework for functionally decentralizedŽ . firms that can help production and marketing coordinate their decisions at the marketing mix and production planning level. Despite the obvious need for coordinating PM decisions at this level, what the term coordination means precisely is not well established in literature. As a result, it has often been erroneously used to mean the joint decision-making as in Refs. 5,23 . We will provide a more detailed <sup>w</sup> <sup>x</sup> discussion of ‘coordination’ in Sections 2–4. Freeland 6 is the first to consider coordinating market-<sup>w</sup> <sup>x</sup> ing mix and production planning decisions in a functionally decentralized firm, and devise a coordination scheme where necessary information is exchanged between production and marketing. Kim and Lee 9 recently discussed coordination strategies<sup>w</sup> <sup>x</sup> for determining optimal price and production lot size. However, these two studies are focused on problem-solving per se and fail to provide decision support guidance useful in reality. Much more research efforts are required to develop decision support systems that will help the two functions coordinate their decision-making processes. This is the underlying motivation for conducting this study.

The main purpose of this study is to develop a new DSS framework called Meta Decision Support System MDSS that can provide proper coordina- Ž . tion of production and marketing of a functionally decentralized firm. To this end, we first review the decision-making strategies for marketing and production from the perspective of ‘coordination theory <sup>w</sup> <sup>x</sup> 16,17,19,25 . Based on Whang’s perspective on coordination 25 , we make a clear distinction between<sup>w</sup> <sup>x</sup> the joint and coordinated strategies and justify the need for MDSS for PM coordination. In developing the MDSS framework, we use the four components of coordination from the coordination theory <sup>w</sup> <sup>x</sup> 16,17,25 : goals, activities, actors, and interdependencies. To illustrate the operational characteristics of the MDSS approach, we use the coordination framework of Kim and Lee 9 along with an illustra- <sup>w</sup> <sup>x</sup> tive example.

This paper is composed of six sections. Section 2 addresses the nature of PM decision-making. Section 3 shows its relation to coordination theory. Section 4 describes the architecture and operational characteristics of the MDSS. Section 5 presents an example to illustrate the decision-making process by the MDSS approach. This paper ends with some concluding remarks.

## 2. Coordinated production<sup>r</sup>marketing decision making

Many firms are decentralized for such reasons as limited ability of managers to process information, need for speedy decision-making, and motivating employees to take part in decision-making processes Ž<sup>w</sup> <sup>x</sup> 21 , pp. 110–112 . The main assumption of the. present study is that each function of a decentralized firm has information autonomy and local decisionmaking authority in its own domain, delegated from the top management. By the information autonomy, we mean that production and marketing do not share information with each other. Consequently, each function has only limited information. They are, however, willing to exchange information if this is deemed necessary for enhancing the overall performance. By the local decision-making authority, we mean that each function makes decisions belonging to its own domain, and that it is responsible for the decisions that are made according to its own respective local objective.

Three decision-making strategies are possible in managing the PM interface—separate, joint, and coordinated. First, production and marketing decisions can be made separately according to their own local objectiÕes. This separate strategy reflects the decision-making pattern in most of the functionally decentralized firms. Marketing and production decisions made separately may be optimal for each function at the local level but are highly likely to be suboptimal for the entire firm at the global level.

Second, the joint strategy has been suggested as the most effective way of improving the decisionmaking for production and marketing. The joint strategy assumes that a centralized authority makes all the PM decisions simultaneously or jointly with respect to one single objective called the global objectiÕe representing the goal of the entire firm. This is referred to as ‘simultaneous or joint optimization’. A majority of the previous research, especially studies with Operations Research orientation, assumed this approach and their main focus was on analyzing the benefits of the joint optimization in comparison with the separate decision-making <sup>w</sup> <sup>x</sup> 2,8,12–15,23,24 .

The joint strategy in fact assumes away various coordination issues that the functionally decentralized firm may encounter in the course of decisionmaking. It may be a realistic approach only for functionally centralized firms where one person or a group of people makes both production and marketing decisions. Where functionally decentralized, however, production and marketing are two organizational units with differing objectives and thus have motivation to make their own decisions according to the corresponding local objectives. One fundamental question faced by a functionally decentralized firm is therefore how to coordinate the decision-making process of the two functions.

While making their own decisions in a separate manner according to their own local objectives, production and marketing are also willing to cooperate in order to achieve a higher level of decision quality for the entire firm. Since each of the two functions has only limited information, exchange of necessary information between the two becomes indispensable to achievement of a better global performance. The main idea of the coordinated approach is to allow production and marketing to exchange information required for improving the global performance. Although the iterative process of exchanging information and making decisions may fail to converge to a global optimal decision in many cases 4,5 , this<sup>w</sup> <sup>x</sup> coordinated approach may be the only realistic alternative for the functionally decentralized firms. We in this paper present a DSS framework that will guide the iterative information exchange process in order for the entire firm to achieve a highest possible performance level.

To provide a more concrete view of these three decision-making approaches, we consider the following simple single-period, single-product model:

$$
\begin{array}{l} \text {(OP) maximize} _ {p, m, x} \quad p D (p, m) - m D (p, m) \\ - c (D, x) D (p, m) \end{array}\tag{1}
$$

where demand D is a function of the selling price ${ \bf \Xi } ( { \bf \Lambda } _ { p } )$ Ž . and the unit marketing expense m , and the unit production cost Ž . c is a function of demand quantity Ž . Ž . D and other production factors x . We refer to this problem as the overall problem OP . In the Ž . simultaneous optimization, a centralized decisionmaking authority solves OP . This is possible in Ž . reality only when

1. the central authority has access to all information Ž . demand and cost functions ,

2. he or she knows how to solve it optimal solutionŽ algorithms are available ..

We further define marketing and production subproblems as below.

$$
\text {(MP)} \maximize _ { p , m , D } \quad p   D (   p , m ) - m   D (   p , m )
$$

$$
- c _ {\mathrm{e}} D (p, m)\tag{2}
$$

$$
\text {(PP)} \maximize _ { c , x } \quad c ( D , x ) D ( p , m )\tag{3}
$$

The separate and coordinated decision-making approaches described in literature implicitly assume information autonomy. Marketing owns the market data necessary for deriving the demand function. Similarly, only production has the manufacturing cost data. Under the separate approach, marketing first solves MP forŽ . p, m, and D based on an estimated unit production cost or marginal cost $\left( c _ { \mathrm { e } } \right)$ Production can initially provide $c _ { \mathrm { e } }$ or marketing can directly estimate it. By solving MP , marketingŽ . decides p, m, and D according to its own local objective: maximization of marketing profit Ž<sup>s</sup> revenue minus estimated production cost in our. model. Then marketing sends this demand quantity Ž . D to production which subsequently determines x according to the corresponding local objective— minimization of the total production cost, $c ( D , x ) D ( p , m )$ . The process terminates here. Decision quality depends on $c _ { \mathrm { e } }$ . When functionally decentralized, most of the firms would make PM decisions in this manner. In this sense, we refer to this approach as ‘the baseline approach’.

Information autonomy also implies that each function has only limited information. Therefore, under the coordinated approach, production and marketing have no choice but to iteratively exchange information on demand quantity from marketing to produc-Ž tion and unit production cost from production to. Ž marketing until a certain condition is met. After. marketing determines the profit-maximizing D, production calculates the total production cost C and the unit production cost $c ( = C / D )$ . Marketing then receives from production the actual c and uses it in finding new p, m, and D according to the local objective of marketing. The new D is again sent to production where the cost-minimizing x is found. The process continues until the decisions become stabilized or until no significant improvement in profit is obtained. The coordinated approaches discussed in literature 4,6,11 closely resemble the one<sup>w</sup> <sup>x</sup> we just described.

With functional decentralization, the coordinated approach is perhaps the only viable option for realization of a profit higher than that generated by the baseline separate approach. The quality of the finalŽ . decisions depends on how well the decision-making process is coordinated. Even with the coordination, the firm may fail to find the optimal decisions in terms of the global objective, mostly due to the mathematical complexity existence of local optimaŽ . of the PM interface problems regardless of the decision-making approaches taken.

Several solution algorithms that take the joint perspective have successfully overcome this mathematical complexity to guarantee global optimality <sup>w</sup> <sup>x</sup> 3,8,12–15,23,24 . As discussed earlier, these joint optimization algorithms are difficult to apply under functional decentralization. More research efforts are required to develop the optimal coordinated approaches so that production and marketing decisions are successfully coordinated in practice.

## 3. Relation to coordination theory

In his taxonomy of coordination in operations based on coordination theory 17 , Whang 25 pro-<sup>w x</sup> <sup>w x</sup> poses three perspectives of organizations: single-person perspective, team perspective, and nexus-of-contract perspective. We provide a summary of these three perspectives of organization in Table 1. In this section, we discuss these perspectives in relation to the joint and coordinated decision-making.

Among the three perspectives, the first two are relevant to our study. As Table 1 indicates, the single-person perspective corresponds to the joint PM decision-making. Under joint decision-making, it is assumed that a single authority has access to all information and that this authority makes all PM decisions and is in a position to force implementation of these decisions. Therefore, existence of production and marketing is simply ignored, let alone the coordination issues. In contrast, the coordinated approach recognizes the fact that the two separate organizational units are independent decision-making units and therefore that the coordination of such units is essential to the achievement of the firm’s goal.

Our main concern is with the team perspective, which is based on team theory of economics 18 . It<sup>w</sup> <sup>x</sup> assumes that coordination takes place in full cooperation among the team members in our context, Ž production and marketing . They share the common. single objective or the global objective, and separately work to collectively achieve the objective like a sport team. Each member of the team, however, has only limited amount of information and limited action sets available. In this regard, Whang 25 <sup>w</sup> <sup>x</sup> argues that an information system is required to facilitate information flow and cooperation.

Like the team perspective, the coordinated approach fully acknowledges the existence of two parties, production and marketing. It also assumes that the two parties would coordinate their own decisions in order to achieve a higher level of overall performance. During the process of coordination, each function with only limited information seeks to obtain other necessary information available from the other function. Whether they would cooperate according to the global objective and whether they would exchange truthful information are some of the concerns that the nexus-of-contracts perspective addresses.

Table 1  
Whang’s 25 taxonomy of organizational perspectives <sup>w</sup> <sup>x</sup>

<table><tr><td>Organizational perspective</td><td>Major characteristics</td><td>Corresponding production/ marketing decision-making</td></tr><tr><td rowspan="3">Single-person Perspective</td><td>a centralized authority with access to all information makes all decisions</td><td rowspan="3">Simultaneous or Joint</td></tr><tr><td>multiparty is collapsed into a single authority</td></tr><tr><td>issues of multiparty coordination are ignored</td></tr><tr><td rowspan="3">Team perspective</td><td>existence of multiple parties is acknowledged</td><td rowspan="3">Coordinated</td></tr><tr><td>each party has limited information and action sets, and thus takes different roles</td></tr><tr><td>multiple parties cooperate to achieve the local objective</td></tr><tr><td rowspan="2">Nexus-of-contracts perspective</td><td>self-interested multiparty or agents</td><td rowspan="2">N/A</td></tr><tr><td>each maximizes his/her return</td></tr></table>

The key difference between the coordinated decision-making and the team perspective is that each of the two functions under the coordinated approach makes decisions according to its own local objectives. Just an information system for collecting and storing information may not be sufficient. It appears that, to implement the coordinated approach, a more intelligent system is required to guide the coordination process so that the overall performance can be significantly improved. As an implementation solution, we suggest the MDSS approach.

## 4. The MDSS

In this section, we design the MDSS based on the coordination theory. Its architecture consists of the four components of coordination: goals, activities, actors, and interdependencies 16 . Table 2 summa-<sup>w</sup> <sup>x</sup> rizes the coordination processes associated with the four components.

Goals are the motivations and purposes of an activity that is performed by a human or machine actor a single agent or a team of agents . EachŽ . activity may be broken into sub-activities. The need for coordination arises because of interdependencies among these sub-activities. Therefore, as Malone and Crowston 16 stated, coordination can be defined as<sup>w</sup> <sup>x</sup> ‘‘the act of managing interdependencies among activities performed by actors to achieve a goal’’. The present study proposes to develop the MDSS that casts this concept of coordination into the DSS framework.

Based on the four components of coordination, we develop the architecture of the MDSS consisting of the following six modules: 1 Goal SpecificationŽ . Module, 2 Activity Controller, 3 Actor SelectionŽ . Ž . Module, 4 Interdependency Manager, 5 DSS Ž . Ž . Generator, and 6 Convergence Checking Module. Ž . The MDSS supervises individual production andŽ

Table 2  
Components of coordination

<table><tr><td>Components of coordination</td><td>Associated coordination processes</td></tr><tr><td>Goals</td><td>Identifying goals</td></tr><tr><td>Activities</td><td>Mapping goals to activities</td></tr><tr><td>Actors</td><td>Selecting actors and assigning activities to actors</td></tr><tr><td>Interdependencies</td><td>Managing interdependencies among actors</td></tr></table>

marketing DSSs to check whether they are working. according to a pre-specified rule. Goal Specification Module specifies a control rule as well as a global objective function. It also helps Activity Controller formulate a set of subproblems to fulfill the global objective function. Then DSS Generator generates an individual DSS for solving each subproblem. Actor Selection Module controls and<sup>r</sup>or executes the individual DSSs generated by DSS Generator. Interdependency Manager controls the direction of information flow and the information to be exchanged between the individual DSSs according to a pre-specified rule. If Convergence Checking Module detects violation of the pre-specified rule, then Interdependency Manager changes the direction of information flow and the information to be exchanged between them. The solution process of this MDSS approach can be summarized as follows:

Step 1: Specify a global objective function.

Step 2: Formulate a set of subproblems.

Step 3: Generate an individual DSS for each subproblem.

Step 4: Execute the individual DSSs.

Step 5: Check interdependency between the individual DSSs during Step 4.

Step 6: Change the direction of information flow and the information to be exchanged among the individual DSSs.

Fig. 1 depicts the schematic architecture of MDSS specified for the problem of coordinating PM decisions. As shown in Fig. 1, the architecture of MDSS is two-layered. The upper layer includes the components of coordination. The lower layer, controlled by the upper layer, specifies the individual DSSs.

![](/api/attachments/F3DY49YZ/fulltext/images/3f598380706db90aced4b1762ddb9f7aef1e8c6f97f14e0f0a0480388b17fd92.jpg)  
Fig. 1. The schematic architecture of MDSS.

## 5. Illustration

In this section, we illustrate the solution process of a prototype MDSS in coordinating PM decisions. We present a PM coordination problem in a general context and describe how MDSS can work with the iterative decision-making process when the process is found to not converge to the global optimum. The prototype MDSS has been implemented in Visual Basic language on Windows ’95 environment.

5.1. Step 1: Specify the global objectiÕe function ( ) Goal Specification Module

Consider a functionally decentralized firm whose overall objective is to maximize the profit Ž . defined as below:

$$
(\mathrm{OP}) \text {   maximize   } \Pi = \mathrm{TR} (D, m) - \mathrm{TC} (D, x)\tag{4}
$$

where D, m, and x are the demand or production volume, the marketing mix factors, and the other production cost factors, respectively, and where $\mathrm { T R } ( D , m )$ and $\mathrm { T C } ( D , x )$ represent the revenue and cost functions, respectively. Marketing and production have only limited information. TRŽ . D, m is known only to marketing and $\mathrm { T C } ( D , x )$ only to production.

## 5.2. Step 2: Formulate a set of subproblems Acti ( Õity Controller)

The coordinated approach can be described as that of solving the following two subproblems iteratively:

$$
(\mathrm{MP}) \text {   maximize   } \mathrm{TR} (D, m) - \mathrm{MC} _ {t - 1} D\tag{5}
$$

$$
(\mathrm{PP}) \text {   minimize   } \mathrm{TC} (D _ {t}, x).\tag{6}
$$

Note that each subproblem has its own local objective function. By formulating subproblems, Activity Controller defines in generic terms the set of activities to be performed in order to achieve the goal specified by Goal Specification Module.

5.3. Step 3: Generate an indiÕidual DSS for each subproblem DSS Generator( )

DSS Generator generates marketing and production DSSs. Model Module of each individual DSS possesses a set of algorithmic models to solve the subproblems. Data Module of each individual DSS stores fundamental information needed for Model Module to process models.

5.4. Step 4: Execute the indiÕidual DSS Actor Selec( - tion Module)

Actor Selection Module selects an appropriate actor to execute its own individual DSS according to its own local objective shown in Step 2.

5.5. Step 5: Check interdependency between the indiÕidual DSSs during Step 4 Interdependency( Manager; ConÕergence Checking Module)

In Step 5, Interdependency Manager identifies the nature of interdependency between the actors, production and marketing. There are two types of approaches to coordinate the interdependencies: Marketing-Oriented Coordination Approach MOCAŽ . and Production-Oriented Coordination Approach Ž . POCA . MOCA works as follows. At iteration t, given the marginal cost $\mathbf { M C } _ { t - 1 }$ from the previous iteration $( t - 1 )$ , marketing determines the demand quantity D DŽ . which production uses to find a new $x ( x _ { t } )$ . Marginal cost MC is then calculated and communicated to marketing for the next iteration $\left( t + 1 \right)$ . This approach is ‘marketing-oriented’, because under MOCA, it is marketing that provides the key information, sales<sup>r</sup>demand forecasts. Production uses this information to determine how much to produce. It is optimal for production to produce exactly the forecasted amount because of the singleperiod characteristics of the model we consider. Once production is determined how to produce that amount at a minimum cost, production has the marginal cost figure and relays it to marketing for the next iteration of information exchange. This process is essentially identical to the cobweb phenomenon of dynamic equilibrium process 1 , pp. 572–575 , so MOCAŽ<sup>w</sup> <sup>x</sup> .

can fail to converge to an optimum. Based on the DSS results provided by Actor Selection Module, Convergence Checking Module will determine whether the process is converging or not. MDSS can prevent the coordination process from diverging by changing the coordinated approaches. The divergent process can be detected by the rule:

$$
\Delta D _ {t} > \Delta D _ {t - 1},\tag{7}
$$

where $\varDelta D _ { t } = | D _ { t } - D _ { t - 1 } | .$ . In the case of divergence, Activity Controller reformulates subproblems as follows:

$$
(\mathrm{MP}) \text {   maximize   } \mathrm{TR} (D _ {t}, m)\tag{8}
$$

$$
\text {(PP)} \text { maximize } \mathrm{MR} _ {t - 1} D - \mathrm{TC} (D, x)\tag{9}
$$

where production plays an active role of determining the production or demand quantity and where, given the demand quantity determined by production, marketing sets the marketing mix policy that maximizes the revenue or marketing profit. Thus, we call this ‘Production-Oriented Coordination Approach’.

## 5.6. Step 6: Change the direction of information flow and the information to be exchanged between indi-Õidual DSSs Interdependency Manager ( )

When the MDSS detects divergence, it switches the coordination approaches, from MOCA to POCA or from POCA to MOCA. The information to be exchanged and the flow direction of information under MOCA and POCA are as follows. Under MOCA, marketing transmits D to production and production sends MC to marketing. Under POCA, marketing relays MR to production and production communicates D to marketing. The counter-clock wise and clockwise movements in Fig. 2 represent MOCA and POCA, respectively. Fig. 2 graphically illustrates a hypothetical situation where employing MOCA results in a divergent process. In this case, Interdependency Manager would change the coordination approaches from MOCA to POCA.

Steps 4 through 6 can be summarized as follows. If the coordination process is initiated with MOCA, Interdependency Manager will notify Actor Selection Module to solve the marketing subproblem under MOCA. Actor Selection Module then selects marketing as the incumbent actor and instructs it to run the marketing DSS to solve the marketing subproblem. After execution, marketing obtains the current optimal marketing mix decisions and the corresponding demand forecast. The incumbent actor marketing then sends the demand forecast information to Interdependency Manager, which relays this information to production and notifies Actor Selection Module to solve the production subproblem. Actor Selection Module then selects production as the incumbent actor and instructs it to execute the production DSS which generates the minimum-cost production schedule and the corresponding marginal cost, given the demand forecast from marketing. The incumbent actor production communicates the marginal cost information to marketing through Interdependency Manager.

![](/api/attachments/F3DY49YZ/fulltext/images/dbc68350848a32fe9470c72dbce4ba19b821182e49f2aeba711c705751dfeab6.jpg)  
Fig. 2. An illustration of MOCA and POCA for a hypothetical situation.

During this process, Convergence Checking Module receives information necessary for checking convergence of the process and informs Interdependency Manager of whether it is converging or not. Once the process starts to diverge, Convergence Checking Module notifies this to Interdependency Manager so that the activities of the two actors are coordinated according to POCA. Under POCA, the process works in the same way except for the fact that based on the marginal revenue information, the production DSS determines the demand volume and sends it to marketing. Due to the information autonomy assumption under functional decentralization, production and marketing exchange the demand volume, marginal cost and revenue, and do not share other information during the coordination process.

## 5.6.1. Numerical example

For illustration purposes, we consider the simple problem of determining the selling price $( p )$ and demand Ž . D . We note that the approach we use can be applied to a more complicated problem.

5.6.1.1. Step 1: Specify the global objectiÕe function. Suppose that the firm’s goal is to maximize the following profit:

$$
\Pi = p D (p) - C (D)\tag{10}
$$

where D is an inverse function of $p$ and the production cost is a function of D. The demand production cost functions are defined as

$$
D (p) = a - b p (a > 0, b > 0, \text { and } p <   a / b)\tag{11}
$$

and

$$
C (D) = s D + r D ^ {2} (s > 0, r > 0).\tag{12}
$$

5.6.1.2. Step 2: Formulate a set of subproblems. Activity Controller formulates subproblems for MOCA and POCA. Under MOCA, the marketing subproblem is to

$$
\begin{array}{r l} \text {(MP)} & \text {maximize} _ {p, D} p D - c _ {\mathrm{e}} D \\ & = p (a - b p) - c _ {\mathrm{e}} (a - b p) \end{array}\tag{13}
$$

where $c _ { \mathrm { e } }$ is the estimated marginal cost of production. Then, the production subproblem is to simply calculate the production cost according to C DŽ . as defined in Step 1. Let $D _ { \mathrm { o } }$ be the demand volume determined by the marketing subproblem. Given $D _ { \mathrm { o } } ,$ production calculates the production cost and the corresponding MC.

Under POCA, production uses MR from marketing to find the demand volume, say $D _ { \mathrm { o } }$ , that solves the following production subproblem:

$$
\left(\mathrm{PP}\right) \text { maximize } _ {D} \mathrm{MR} D - C (D)\tag{14}
$$

where C DŽ . is as defined in Step 1. Once $D _ { \mathrm { o } }$ is obtained, marketing finds the corresponding price and MR.

5.6.1.3. Step 3: Generate an indiÕidual DSS for each subproblem. Individual DSSs for each production and marketing possess data module, model module, and knowledge module. The contents of each module change according to the formulation of subproblems.

5.6.1.4. Step 4: Execute the indiÕidual DSSs

MOCA. Elementary calculus yields for the marketing subproblem

$$
p = (a + b c _ {\mathrm{e}}) / (2 b)\tag{15}
$$

and

$$
D = \left(a - b c _ {\mathrm{e}}\right) / 2.\tag{16}
$$

Production then calculates the production cost and the marginal cost at this demand level.

$$
\mathrm{MC} = 2 r D + s = r \left(a - b c _ {\mathrm{e}}\right) + s\tag{17}
$$

Production sends this marginal cost figure to marketing. Marketing then sets MC of Eq. 17 equal to Ž . $c _ { \mathrm { e } }$ and finds the profit maximizing D. The process iterates until it converges to the optimal solution or until MDSS detects the divergence.

POCA. Using calculus, we can easily find D and $p$ that satisfy the first order optimality condition, MR<sup>s</sup>MC for the production subproblem:

$$
p = (\mathrm{MR} - s) / (2 r)
$$

$$
D = (2 r a - \mathrm{MR} + s) / (2 r b)\tag{18}
$$

Ž . 19

This demand or production volume is then communicated back to marketing in order for it to compute the marginal revenue.

$$
\mathrm{MR} = (a - 2 D) / b\tag{20}
$$

5.6.1.5. Step 5: Check interdependency between the indiÕidual DSSs during Step 4. Convergence Checking Module calculates $\varDelta D _ { t }$ at each iteration and checks divergence by testing if $\varDelta D _ { t } > \varDelta D _ { t - 1 }$ is true. When divergence is detected, Convergence Checking Module notifies this to Interdependency Manager.

5.6.1.6. Step 6: Change the direction of information flow and the information to be exchanged between indiÕidual DSSs. Interdependency Manager controls information flow. Actions of Interdependency Manager are well illustrated for the numerical example in Table 3.

Table 3 presents the execution results of the MDSS with detailed actions taken by Interdependency Manager, Actor Selection Module, and Convergence Checking Module.

Table 3 shows that starting the decision-making process with MOCA, the MDSS detects divergence after the three iterations. It then instructs production and marketing DSSs to switch to the POCA. By doing so, the PM decision-making will converge to the optimal solution.

T<sub>a</sub>bl<sub>e</sub> 3  
A<sub>n</sub> ill<sub>us</sub>t<sub>ra</sub>ti<sub>on o</sub>f th<sub>e</sub> MDS S <sub>coor</sub>di<sub>na</sub>ti<sub>on process</sub>

<table><tr><td rowspan="2">Iteration no.</td><td rowspan="2">Interdependency manager</td><td colspan="2">Actor selection module</td><td rowspan="2">Convergence checking module</td></tr><tr><td>Actor</td><td>DSS solutions</td></tr><tr><td rowspan="2">1</td><td rowspan="2">-Start with MOCA;-Solve (MP) and then (PP);-D from marketing to production;-MC from production to marketing</td><td>Marketing</td><td> $p = 11.25 \ D = 2500$  at  $c_e = 10$ </td><td></td></tr><tr><td>Production</td><td> $\mathbf{MC} = 9.25$  at  $\underline{D = 2500} \Pi = 12812.5$ </td><td></td></tr><tr><td rowspan="2">2</td><td rowspan="2"></td><td>Marketing</td><td> $p = 10.88 \ D = 3250$  at  $\underline{MC = 9.25}$ </td><td> $\Delta_2 = 750$ </td></tr><tr><td>Production</td><td> $\mathbf{MC} = 11.13$  at  $\underline{D = 3250} \Pi = 12390.63$ </td><td></td></tr><tr><td rowspan="2">3</td><td rowspan="2"></td><td>Marketing</td><td> $p = 11.81 \ D = 1375$  at  $\underline{MC = 11.13}$ </td><td> $\Delta_2 = 1875, \Delta_2 < \Delta_3:$  divergingInform Interdependency Manager</td></tr><tr><td>Production</td><td>No execution occurs.</td><td></td></tr><tr><td rowspan="2">4</td><td rowspan="2">-Switch to POCA;-Solve (PP) and then (MP);-D from production to marketing;-MR from marketing to production</td><td>Production</td><td> $D = 2800$  at  $MR = 10$ </td><td></td></tr><tr><td>Marketing</td><td> $p = 11.10$  and  $\mathbf{MR} = 9.7$  at  $\underline{D = 2800}; \Pi = 12880$ </td><td></td></tr><tr><td rowspan="2">5</td><td rowspan="2"></td><td>Production</td><td> $D = 2680$  at  $\underline{MR = 9.7}$ </td><td> $\Delta_5 = 120$ </td></tr><tr><td>Marketing</td><td> $p = 11.16$  and  $\mathbf{MR} = 9.82$  at  $\underline{D = 2680}; \Pi = 12890.8$ </td><td></td></tr><tr><td rowspan="2">6</td><td rowspan="2"></td><td>Production</td><td> $D = 2728$  at  $\underline{MR = 9.82}$ </td><td> $\Delta_6 = 48 \Delta_5 > \Delta_6:$  converging</td></tr><tr><td>Marketing</td><td> $p = 11.14$  and  $\mathbf{MR} = 9.772$  at  $\underline{D = 2728}; \Pi = 12892.5$ </td><td></td></tr><tr><td rowspan="2">7</td><td rowspan="2"></td><td>Production</td><td> $D = 2708.8$  at  $\underline{MR = 9.772}$ </td><td> $\Delta_7 = 19.2 \Delta_6 > \Delta_7:$  converging</td></tr><tr><td>Marketing</td><td> $p = 11.15$  and  $\mathbf{MR} = 9.791$  at  $\underline{D = 2708.8}; \Pi = 12892.8$ </td><td></td></tr><tr><td rowspan="2">8</td><td rowspan="2"></td><td>Production</td><td> $D = 2716.48$  at  $\underline{MR = 9.791}$ </td><td> $\Delta_8 = 7.68 \Delta_7 > \Delta_8:$  converging</td></tr><tr><td>Marketing</td><td> $p = 11.14$  and  $\mathbf{MR} = 9.783$  at  $\underline{D = 2716.48}; \Pi = 12892.8$ </td><td></td></tr><tr><td rowspan="2">9</td><td rowspan="2"></td><td>Production</td><td> $D = 2713.41$  at  $\underline{MR = 9.783}$ </td><td> $\Delta_9 = 3.07 \Delta_8 > \Delta_9:$  converging</td></tr><tr><td>Marketing</td><td> $p = 11.14$  and  $\mathbf{MR} = 9.787$  at  $\underline{D = 2713.41}; \Pi = 12892.9$ </td><td></td></tr><tr><td rowspan="2">10</td><td rowspan="2"></td><td>Production</td><td> $D = 2714.64$  at  $\underline{MR = 9.787}$ </td><td> $\Delta_{10} = 1.23 \Delta_9 > \Delta_{10}:$  converging</td></tr><tr><td>Marketing</td><td> $p = 11.14$  and  $\mathbf{MR} = 9.785$  at  $\underline{D = 2714.64}; \Pi = 12892.9$ </td><td></td></tr><tr><td rowspan="2">11</td><td rowspan="2"></td><td>Production</td><td> $D = 2714.15$  at  $\underline{MR = 9.785}$ </td><td> $\Delta_{11} = 0.49 \Delta_{10} > \Delta_{11}:$  convergingClose enough, stop.</td></tr><tr><td>Marketing</td><td> $p = 11.14$  and  $\mathbf{MR} = 9.786$  at  $\underline{D = 2714.15}; \Pi = 12892.9$ </td><td></td></tr></table>

N<sub>o</sub>t<sub>e :</sub> B <sub>o</sub>ld-f<sub>ace</sub>d fi<sub>gures</sub> <sub>represen</sub>t th<sub>e</sub> i<sub>n</sub>f<sub>orma</sub>ti<sub>on</sub> t<sub>o</sub> b<sub>e</sub> <sub>sen</sub>t t<sub>o</sub> th<sub>e</sub> <sub>nex</sub>t <sub>ac</sub>t<sub>or,</sub> <sub>an</sub>d <sub>un</sub>d<sub>er</sub>li<sub>ne</sub>d <sub>ones</sub> <sub>are</sub> th<sub>e</sub> i<sub>n</sub>f<sub>orma</sub>ti<sub>on</sub> <sub>sen</sub>t f<sub>rom</sub> th<sub>e</sub> <sub>prev</sub>i<sub>ous</sub> <sub>ac</sub>t<sub>or</sub> <sub>an</sub>d <sub>use</sub>d b<sub>y</sub> th<sub>e</sub> <sub>curren</sub>t <sub>ac</sub>t<sub>or</sub>.

As mentioned earlier, a prototype MDSS has been developed on Windows ’95 with Visual Basic language for the situation where production and marketing are wired through local area network. Microsoft Excel is used to generate individual DSSs and solve the production and marketing subproblems on two separate PCs representing the decision-making nodes of production and marketing. Table 3 summarizes the experimental results by the MDSS prototype for the numerical example.

The main feature of the MDSS approach is that it provides global optimal decisions for production and marketing under functional decentralization while other approaches in literature takes the joint approach and thus may not work under decentralization. Equally important is that the MDSS approach eliminates human intervention during the decisionmaking process, which would cause behavioral problems among the decision-makers involved.

We note that the proposed MDSS approach can be applied to a broader class of problems of coordinating PM decisions such as pricing and lot-sizing problems 8,12–15 . The problems they considered,<sup>w</sup> <sup>x</sup> after processing the original problem, can be transformed into the format of our framework so that while adhering to the restrictions imposed by decentralization, we can coordinate the decisions of the two functions to obtain the global optimal performance.

## 6. Conclusion

We in this paper proposed and implemented the MDSS approach to solving the problem of coordinating production and marketing decisions in functionally decentralized firms. It is assumed that, in a functionally decentralized firm, each managerial function solves its own problem according to local objective function, and then seeks to exchange information between the interdependent units. Under this assumption, we designed the MDSS based on coordination theory to provide a more realistic guidance for coordination of production and marketing decisions. We presented a numerical example to illustrate how the MDSS we propose can deal with coordination of the short-term PM decisions.

One immediate extension of the present study is to refine the MDSS to handle the multiple-actor case. Although the architecture of the MDSS appears to be applicable with minor modification, the MDSS requires a multiple-actor version of MOCA and POCA to successfully deal with the complex nature of the interdependencies among multiple actors. One can also investigate into how to incorporate fuzzy logic concept to deal with uncertainty embedded in data. We are now developing more refined version of the MDSS capable of working on the web-based environment in which decision-makers of geographically dispersed production and marketing can collaborate more effectively through Internet.

## Acknowledgements

The authors wish to acknowledge the financial support of Korea Research Foundation made in the program year of 1997.

## References

<sup>w</sup> <sup>x</sup> 1 A.C. Chiang, Fundamental Methods of Mathematical Economics, 2nd edn., McGraw Hill, New York, 1974.

<sup>w</sup> <sup>x</sup> 2 V.L. Crittenden, Close the marketing production gap, Sloan Management Review 33 1992 41–52.Ž .

<sup>w</sup> <sup>x</sup> 3 W.W. Damon, R.A. Schramm, Simultaneous decision model for marketing, Production, and Finance, Management Science 19 1972 161–172.Ž .

<sup>w</sup> <sup>x</sup> 4 X. de Groote, Flexibility and marketing<sup>r</sup>manufacturing coordination, International Journal of Production Economics 36 Ž .1994 153–167.

<sup>w</sup> <sup>x</sup> 5 J. Eliashberg, R. Steinberg, Marketing-Production Joint Decision Making, in: J. Eliashberg, G. Lilien Eds. , Management Ž . Science in Marketing, Chap. 18, North-Holland, Amsterdam, 1993.

<sup>w</sup> <sup>x</sup> 6 J.R. Freeland, Coordination strategies for production and marketing in a functionally decentralized firm, AIIE Transactions 12 1980 126–132.Ž .

<sup>w</sup> <sup>x</sup> 7 A.C. Hax, D. Candea, Production and Inventory Management, Prentice-Hall, Englewood Cliffs, NJ, 1984.

<sup>w</sup> <sup>x</sup> 8 D. Kim, W.J. Lee, Optimal joint pricing and lot sizing with fixed and variable capacity, European Journal of Operational Research 109 1 1998 212–227.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 D. Kim, W.J. Lee, Optimal coordination strategies for production and marketing decisions, OR Letters 22 1 1998Ž . Ž . 41–47.

<sup>w</sup> <sup>x</sup> 10 P. Kotler, Marketing Management, 7th edn., Prentice-Hall, Englewood-Cliffs, NJ, 1991.

<sup>w</sup> <sup>x</sup> 11 H. Kunreuther, L. Schrage, Joint pricing and inventory decisions for constant priced items, Management Science 19 Ž . 1973 732–738.

<sup>w</sup> <sup>x</sup> 12 W.J. Lee, Determining selling price and order quantity by geometric programming: optimal solution, bounds, and sensitivity, Decision Sciences 24 1993 76–87.Ž .

<sup>w</sup> <sup>x</sup> 13 W.J. Lee, D. Kim, Optimal and heuristic decision strategies for integrated production and marketing planning, Decision Sciences 24 1993 1203–1213.Ž .

<sup>w</sup> <sup>x</sup> 14 W.J. Lee, D. Kim, Effects of Integrating Order<sup>r</sup>Backorder Quantity and Pricing Decisions, Production and Operations Management 9 1998 312–324.Ž .

<sup>w</sup> <sup>x</sup> 15 W.J. Lee, D. Kim, A.V. Cabot, Optimal demand rate, lot sizing, and process reliability improvement decisions, IIE Transactions 28 1996 941–952.Ž .

<sup>w</sup> <sup>x</sup> 16 T. Malone, K. Crowston, What Is Coordination Theory and How Can It Help Design Cooperative Work Systems? CSCW’90 Proceedings of the Conference on Computer-Supported Cooperative Work, ACM, New York, 1990.

<sup>w</sup> <sup>x</sup> 17 T. Malone, K. Crowston, The interdisciplinary study of coordination, ACM Computing Surveys 26 1994 87–119.Ž .

<sup>w</sup> <sup>x</sup> 18 J. Marschak, R. Radner, Economic Theory of Teams, Yale University Press, New Haven, CT, 1972.

<sup>w</sup> <sup>x</sup> 19 G.N. Mentzas, Team coordination in decision support projects, European Journal of Operational Research 89 1996 Ž . 70–85.

<sup>w</sup> <sup>x</sup> 20 D.B. Montgomery, W.H. Hausman, Managing the marketing<sup>r</sup>manufacturing interface, Gestion 2000: Management and Perspective 5 1986 69–85.Ž .

<sup>w</sup> <sup>x</sup> 21 S.P. Robbins, Organization Theory: Structure, Design, and Applications, 3rd edn., Prentice Hall, Englewood Cliffs, NJ, 1990.

<sup>w</sup> <sup>x</sup> 22 B.P. Shapiro, Can marketing and manufacturing coexist?, Harvard Business Review 50 1977 104–114.Ž .

<sup>w</sup> <sup>x</sup> 23 A.G. Sogomonian, C.A. Tang, Modeling framework for coordinating promotion and production decisions within a firm, Management Science 39 1993 191–203.Ž .

24 U.P. Welam, Synthesizing short run production and marketing decisions, AIIE Transactions 9 1977 53–62.Ž .

<sup>w</sup> <sup>x</sup> 25 S. Whang, Coordination in operations: a taxonomy, Journal of Operations Management 12 1995 413–422.Ž .

![](/api/attachments/F3DY49YZ/fulltext/images/53fe2c73a5651303657ca9ea743545a028f0d190d1a9fd27237c2ef6279ba803.jpg)

Won Jun Lee is Associate Professor of Management at the University of Inchon, Korea. He received a BBA from Sung Kyun Kwan University, an MBA from University of Michigan, and a PhD in Business from Indiana University. He was formerly affiliated with Marquette University. His current research interests include DSS for inter-functional coordination, production<sup>r</sup>marketing interface, manufacturing information systems, and operations management. His articles

have been published in IIE Transactions, Decision Sciences, Intelligent Systems in Accounting, Finance, and Management, Production and Operations Management, OR Letters, European Journal of Operational Research, Computers and OR, among others.

![](/api/attachments/F3DY49YZ/fulltext/images/18dd5d31130cb0ab3f4531713dd91c5d6dc773e0efdf9a28d56c76062579ea18.jpg)

Kun Chang Lee is a Professor of MIS at Sung Kyun Kwan University, Korea. He received a BA degree in 1982 from Sung Kyun Kwan University, and a MS in 1984 and a PhD in MIS from the Korea Advanced Institute of Science and Technology KAIST , 1988. His publi-Ž . cations have appeared in Decision Support Systems, Expert Systems, Intelligent Systems in Accounting Finance and Management, Fuzzy Sets and Systems, etc. He has also presented papers at

several international conferences including Hawaii International Conference on Systems and Science HICSS , International JointŽ . Conference on Neural Networks IJCNN , IEEE Conference onŽ . Systems, Man, and Cybernetics SMC , International Society of Ž . DSS ISDSS . His current research interests include DSS, expertŽ . systems, and synergism of neural network and expert systems, and fuzzy logic-driven decision-making. He is a member of New York Academy of Science, and listed in Who’s Who to be published in 1998 15th edition .Ž .
