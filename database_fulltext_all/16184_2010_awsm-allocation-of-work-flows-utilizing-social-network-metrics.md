---
otero_id: 16184
otero_key: "KTNADTF9"
title: "AWSM: Allocation of work flows utilizing social network metrics"
authors: "Akhilesh Bajaj; Robert Russell"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/i.dss.2010.07.014"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# AWSM: Allocation of work<sup>fl</sup>ows utilizing social network metrics

Akhilesh Bajaj ⁎, Robert Russell

The University of Tulsa, United States

## a r t i c l e i n f o

Article history: Received 20 November 2008 Received in revised form 23 July 2010 Accepted 29 July 2010 Available online 11 August 2010

Keywords: Work<sup>fl</sup>ows Social networks Teams Integer programming Optimization Algorithms

## a b s t r a c t

The primary contribution of this work is a methodology that serves as a decision support tool to create teams of human actors within an organization to perform work<sup>fl</sup>ows, based on optimizing social network (SN) measures of choice, such as group or team cohesiveness. Past literature shows that the constituent activities of the work<sup>fl</sup>ows will be performed with greater ef<sup>fi</sup>ciency and/or effectiveness if the workgroup of actors is optimized along an SN measure such as group cohesiveness. The major contribution here is the creation and implementation of a formal generalized methodology we call AWSM (Allocation of Work<sup>fl</sup>ows with Social Network Metrics) that incorporates ideas from two diverse <sup>fi</sup>elds: social network theory and work<sup>fl</sup>ow modeling, and allows optimization of work groups along any SN metric. In order to implement this model we present newly created algorithms to structure and represent the problem so that standard integer programming solvers can be utilized to solve it. We also present a performance analysis of the AWSM methodology and empirically test its feasibility for solving real world sized problems.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

## 1.1. Motivating example

Jill is the CEO of ACME Bicycles. She supervises the daily work activities of over one hundred employees, where each can perform one or more of several roles such as <sup>fi</sup>nished goods inventory clerk, shipping clerk, lathe specialist, milling machinist, design engineer, engineering supervisor, product development manager, marketing manager, salesperson and so on. Several employees have been crosstrained in their roles, after a new enterprise information system was acquired and installed, that provided a uniform interface and data store for the entire organization. Like almost all organizations, the work load at ACME can be modeled using several work<sup>fl</sup>ow types. Examples of work<sup>fl</sup>ow types include ordering, receiving and stocking raw material, ordering, receiving and stocking outsourced manufactured goods material, building and storing <sup>fi</sup>nished bicycles, brainstorming over the next bicycle design, drawing out the strategic plan for the next 5 years and so on. Like most organizations, each work<sup>fl</sup>ow type at ACME can be decomposed into activity types performed in order to complete a work<sup>fl</sup>ow type. The overall workload at ACME over a time period consists of multiple instances of each work<sup>fl</sup>ow type to be executed within that time period.

Jill has observed that some instances of the same work<sup>fl</sup>ow type are performed more effectively or ef<sup>fi</sup>ciently than other instances. She also understands that some groups of people work better together, and when these groups are allocated an instance of a work<sup>fl</sup>ow type, it tends to get done “better” (faster or more effectively) than another instance of the same work<sup>fl</sup>ow type allocated to another group. She is wondering if there is a way to optimally allocate work amongst her employees, taking into account the knowledge of how well people work with each other.

Business processes usually consist of a number of interrelated activities, performed by people with different skill-sets or roles. Recently, there has been extensive interest in the workflow management systems that provide a means of automating the allocation and scheduling of the interrelated activities that constitute the work<sup>fl</sup>ows. As pointed out in [22], most activities in an organization are executed by a number of agents, possessing different skill-sets. In their description of the dynamic allocation of work<sup>fl</sup>ows to agents, [34] point out several shortcomings with current allocation approaches. These limitations primarily stem from an inability to deal with uncertainty, and to incorporate knowledge about the organization into the allocation process. This lack of the incorporation of organizational knowledge is also recognized in other works such as [9,22,40]. Social networks in an organization constitute an important aspect of organizational knowledge [13], and are used explicitly in our work to help allocate work<sup>fl</sup>ows.

Work<sup>fl</sup>ow allocation has also been studied in the job design literature in human resource management [12,24,26,29,55]. Typical issues in this area include trade-offs between serial and parallel production, employee motivations and incentives management. However, studies in this area also have not typically considered relationships between agents when allocating work<sup>fl</sup>ows, which is the focus of this work.

A rich body of literature dealing with social networks (SN) exists in the social sciences. The sociocentric approach to SN [41,50,56] typically deals with measuring and quantifying the relationships between individuals in a group. The focus is on measuring the structural patterns of interaction and how these patterns can explain outcomes. According to [7], “The social network perspective assumes that actors (whether they be individuals, groups, or organizations; rational or political) are embedded within a web (or network) of interrelationships with other actors. It is this intersection of relationships that de<sup>fi</sup>nes an individual's role, an organization's niche in the market, or simply an actor's position in the social structure.” Graph based analyses in the area utilize measures like centrality and network density to characterize different groups, based on individual links between members (nodes) of that group. Centrality of each member can be characterized by the number of other nodes to which the member is linked [6]. Network density re<sup>fl</sup>ects how reachable a node is, on average, from any other node in the network.

In this work, we take a <sup>fi</sup>rst step towards incorporating ideas from SN to the problem of workflow allocation. The primary contribution of this work is a methodology that creates work<sup>fl</sup>ow teams of human actors within an organization, based on optimizing a social network (SN) measure of choice e.g., group or team cohesiveness. Past literature shows that the constituent activities of the work<sup>fl</sup>ows will be performed with greater ef<sup>fi</sup>ciency and/or effectiveness if the social characteristics of the workgroup of actors are optimized along an SN measure, such as team cohesiveness [30,48,49,51]. Of course, metrics other than team cohesiveness may also drive ef<sup>fi</sup>ciency and/or ef-<sup>fi</sup>cacy. For example, consider an allocation of work<sup>fl</sup>ows dealing with the planning of a major restructuring. These could conceivably require extensive working knowledge of and in<sup>fl</sup>uence within the organization and may be performed more effectively if allocated to a group of actors that is maximized along the SN metric of organizational centrality, i.e. actors who are all central players in the organization.

Our contribution here is the development of a methodology and infrastructure we call AWSM (Allocation of Work<sup>fl</sup>ows utilizing Social Network Metrics), that can be used to allocate a generic set of work-<sup>fl</sup>ows within an organization, to optimize workgroups along any SN metric chosen by the manager. The research paradigm we employ here is design-science based [25]. The artifact developed is the AWSM methodology, which is tested here under industrial strength loads. The theoretical contribution of the artifact developed is to allow the subsequent testing of theories linking social network measures to work<sup>fl</sup>ow performance.

The rest of this paper is organized as follows. In Section 2, we describe earlier work on work<sup>fl</sup>ow allocation amongst agents and the application of social networks to this allocation. Section 3 consists of a detailed description of the AWSM methodology, including the model, algorithms, an illustrative example and performance analysis. We discuss applications of AWSM in Section 4 and conclude with limitations and future research opportunities in Section 5.

## 2. Previous work

## 2.1. Workflow allocation

The allocation of resources to work<sup>fl</sup>ows has long been recognized as an important problem as highlighted in [4] where the middle level of process management is said to deal with this issue. Work<sup>fl</sup>ow allocation has been investigated in several different areas in the literature. In the automated work<sup>fl</sup>ow management systems (WFMS) area, attention has been paid to the dynamic allocation of activities. [22] points out that most WFMSs refer to underlying organizational role lists in order to allocate activities to machines accessible by agents who can perform these roles. [34] provides several shortcomings in the activity allocation methods of WFMSs, many of which can be attributed to a lack of organizational knowledge on the part of the WFMS. One of the pioneering attempts to overcome these limitations is presented in [34], with the use of object constraint language (OCL) to model teams of agents and their relationships in an organization. A limitation of this approach is that OCL does not support concepts that are usually used to characterize organizational relationships. Similarly, [40] uses an object-oriented language to model organizational constraints, with the same limitations. A third approach in [9] uses the event-condition-action framework to model organizational constraints. The AWSM methodology presented here complements these approaches in that it is a static methodology consisting of a series of calculations, which can be implemented alongside a dynamic selection scheme in a WFMS. Further, AWSM explicitly utilizes social network metrics, which traditionally have closer ties to organizational modeling than methods used in some of this earlier work.

In the human resource area, task or function allocation usually deals with the allocation of tasks to people versus machines, and to allocate tasks with a view towards maximizing employee satisfaction. The simplest allocation mechanism consists of a list of tasks that are more appropriate for people versus machines [17]. More recently, static and dynamic allocation schemes have been proposed that trade off criteria such as task criticality, job satisfaction, motivation, ef<sup>fi</sup>ciency and training requirements [11,27]. [44] provides a list of requirements that allocation schemes should ful<sup>fi</sup>ll. Some requirements proposed that are relevant to our study include that the allocation scheme should be usable early in the work design process, should have a structured format and should be able to cover allocations between humans in different roles. In this context, the AWSM methodology described in this work is a static scheme that can be used by managers in the early stage of work periods. Further, the AWSM methodology caters to different roles amongst actors, and may be used to optimize a social network metric that has been shown to correlate positively with work ef<sup>fi</sup>ciency, employee satisfaction, and other variables of interest in the human resource area. Hence, AWSM complements existing work in the human resource area on task allocation.

A third area that examines task allocation methods is in computer science, in distributed information systems, where tasks have to be allocated to multiple computer processors. The criteria in this domain include the minimization of communication costs [43] and the maximization of throughput. Both static and dynamic allocation schemes have been considered in this area, with the static schemes assuming knowledge of the characteristics of the workload [39]. Much of the emerging work in this area involves dynamic schemes that are heuristic based [38] rather than mathematical programming based, because of the real-time requirements of workload allocation for computer processors. A pricing scheme is proposed in [31], to improve the quality of service of Internet traf<sup>fi</sup>c. In the area of web services, a market based mechanism is proposed in [45], using the DiffServ architecture, so that quality of service for premium services is enhanced.

The AWSM allocation method is different because it uses mathematical programming for optimization, rather than heuristics, and models work<sup>fl</sup>ows linked to roles. This is very different from generic tasks or services performed by a computer processor (a single “role”). Finally, AWSM uses social network measures as the optimizing metric, rather than communication costs.

## 2.2. Social network measures

A social network is a structure whose nodes represent members in a social context and whose edges can represent interaction links,

M: The set of |Ml = m members, each element shown as m

W: The set of |Wl = w workflow instances, each element shown as wj

R: The set of |R| = r roles, each element shown as rk

X: A relation between M and R, depicting if member mi can perform role $r _ { k }$

Y: A relation between W and R, depicting the relative amount of time expended by each role in a workflow.

Fig. 1. Summary of notation used in the formulation.

collaboration or in<sup>fl</sup>uence between the members [35]. SN analysis has attracted considerable interest from social and behavioral scientists over the last few decades [41,56]. Recently, researchers in arti<sup>fi</sup>cial science and data mining have also recognized that an organization can bene<sup>fi</sup>t from the interactions within the informal social network amongst its members that can often supplement the of<sup>fi</sup>cial hierarchy imposed by the organizational chart [32,46]. Social networks can be represented using graphs (with the members as nodes and the interaction links as edges) or socio-matrices, where the sending members are the rows and the receiving members are the columns. In this work, we utilize a sociometric notation, which is the most widely used today [56].

Several measures have been used in the SN literature to characterize a network, from the perspective of either one actor, or a group. Measures from a member standpoint include the centrality and the prestige of the actor in an SN, with <sup>fi</sup>ner de<sup>fi</sup>nitions including degree centrality, closeness centrality and betweenness centrality [18]. Group or team level measures include the centrality of the leader of the team, overall team density (how interconnected are the members?), and a related construct: the overall team cohesiveness, which was initially de<sup>fi</sup>ned as the “forces that act on members to stay in the group” [16].<sup>1</sup>

There is a considerable support in sociological theory that team cohesion or cohesiveness is an important explanatory variable in studying the emergence of consensus amongst members of a group [10,19]. Team cohesiveness is thought to drive an array of variables including group homogeneity and in<sup>fl</sup>uence of group norms.

Team cohesiveness has also been shown in numerous studies to have a positive impact on performance in the workplace. Examples of earlier work include [54] who concluded that increased cohesiveness fosters better task redesign. [2] demonstrated that participative goal setting is more effective in cohesive groups. [15,42] investigated how increased cohesiveness reduces the negative effects of situational constraints on organizational behavior. [42] summarizes several studies that show how group cohesiveness leads to improved productivity in teams where the cohesiveness is based on task focus, as opposed to social integration.

More recent studies further strengthen the positive link between team cohesiveness and workplace performance. [49] report a study of 103 manufacturing workers that found a positive association between job satisfaction, internal work motivation and team cohesiveness. [48] showed how increased cohesiveness results in lower employee absenteeism. In [51] low cohesiveness was found to negatively affect creative group work such as brainstorming, as well as more routine tasks. In [30] multiple tasks were used on 50 army teams to determine the effects of social cohesion, group potency and team-member exchange on team performance. Social cohesion was found to have a positive effect on physical performance, mental performance and the assessment of the team by the commander.

The cohesiveness of subgroups within a larger SN can be measured based on four different factors: a) the degree of mutuality of the links between the members in the subgroup, i.e. to what extent do the members of the subgroup choose each other?, b) the reachability from one member to another in the subgroup, c) the frequency of ties between members which measures the degree to which members have ties to one another within a subgroup against a theoretical maximum of ties to all members in the subgroup, and d) the relative frequency of ties which measures the frequency of ties of the subgroup relative to the ties in the larger SN.

Measures of subgroup cohesiveness re<sup>fl</sup>ect one of these four factors. For example, [5] proposed a ratio of the average strength of ties in a subgroup to the average strength of ties of members in the subgroup to SN members outside the subgroup, i.e. utilizing factor d) in the discussion above. [1] viewed just the average strength of ties in the subgroup as the “centripetal” force holding the subgroup together, while the strength of ties of members in the subgroup to members outside the subgroup was viewed as a “centrifugal” force. Excellent summaries of different subgroup cohesiveness measures can be found in [47] and more recently in [56].

In this work, we leverage the notion of SN metrics such as team density or cohesiveness in forming work<sup>fl</sup>ow groups and take a <sup>fi</sup>rst step in proposing a methodology that allows for optimal formation of work<sup>fl</sup>ow groups. The example optimizing criterion used in this work is a measure of subgroup cohesiveness of the work<sup>fl</sup>ow subgroup, though other measures for cohesiveness and other SN metrics may be used, without loss of generality. Next, we describe the AWSM methodology that can be used to allocate work<sup>fl</sup>ows optimized along a selected SN measure.

## 3. The AWSM methodology

AWSM consists of a generalized work<sup>fl</sup>ow model, along with algorithms for work<sup>fl</sup>ow allocation. These are described next.

## 3.1. The Generalized workflow model in AWSM

We present the work<sup>fl</sup>ow model using the maximization of group cohesiveness as the objective criterion. This is formally represented ahead, in the objective function (2). Note that another objective criterion may be substituted, with no other changes in the methodology.

Fig. 1 summarizes the notation used in our formulation.

In an organization, let there be a set of members:

$$
\mathbf {M} = \{m _ {i}, i = 1,.., \mathrm{m} \}
$$

and a set of work<sup>fl</sup>ow\_instances:

$$
\mathsf {W} = \left\{w _ {j}, j = 1,.., \mathsf {w} \right\}
$$

A work<sup>fl</sup>ow\_instance<sup>2</sup> requires a set of roles that perform various activities within the work<sup>fl</sup>ow.

Let there be the set of roles in the organization: $R = \{ r _ { k } , k = 1 , . . . , \mathrm { r } \}$

We allow each member m the ability to perform multiple roles, shown by the relation ${ \sf X } \colon { \sf X } = \{ x _ { i k }$ such that $i = 1 , \dots$ m and $k = 1 , . . ,$ r and $x _ { i k } = ~ 1$ if member $m _ { i }$ <sup>f</sup>can perform role k; and 0 otherwise . We capture the relative amount of time spent by each role $r _ { k }$ <sup>g</sup>in accomplishing a work<sup>fl</sup>ow w with the following relation:

$$
\mathrm{Y} = \left\{y _ {k j}, k = 1,.., \mathrm{r} \text {   and   } j = 1,.., \mathrm{w} \text {   and   } \sum_ {k = 1} ^ {r} y _ {k j} = 1 \text {   for   all   } j = 1,.., \mathrm{w} \right\}
$$

For each role $r _ { k }$ let there be $c _ { k }$ members who can perform that role. Then

$$
c _ {k} = \sum_ {i = 1} ^ {m} X _ {i k}, k = 1, \dots \mathrm{r}.
$$

## 3.1.1. Size of solution space

For each work<sup>fl</sup>ow\_instance $w _ { j } ,$ the solution space size is:

$$
\begin{array}{l} s _ {j} = \prod_ {k = 1} ^ {r} Z _ {k} \binom {C _ {k}} {1} \text { subgroups. } \\ = \prod_ {k = 1} ^ {r} Z _ {k} C _ {k} \end{array}\tag{1}
$$

$$
\begin{array}{l} \text {   Where   } j = 1, \ldots w \text {   and   } \\ Z _ {k} = 1 / c _ {k} \text {   if   } Y _ {k j} = 0 \text {   and   } \\ Z _ {k} = 1 \text {   if   } Y _ {k j} > 0 \text {   and   } \end{array}
$$

() represents the combination symbol.

The total solution space size $s = \sum _ { j = 1 } ^ { v v }$ s<sub>j</sub> subgroups.

3.1.2. Decision variables

The number of decision variables=s.

We need to select one subgroup g<sub>jq</sub> for each work<sup>fl</sup>ow\_instance w<sub>j</sub>, Where $j = 1 , \hdots W$ and $q = 1 , \ldots , s _ { j } .$ (The total number of subgroups that need to be picked=w subgroups).

The decision variables are:

$$
V _ {j q} = \left\{ \begin{array}{l l} 1 & \text { if   the   subgroup   is   selected   and } \\ 0 & \text { otherwise } \end{array} \right.
$$

$$
\text {   for   } j = 1, \dots \text {   w,   } q = 1, \dots \text {   s } _ {j}
$$

## 3.1.3. Objective function

Let the cohesiveness of a subgroup $g _ { j q }$ be $\mathtt { c o h } _ { j q }$

We de<sup>fi</sup>ne the cohesiveness as the number of links between members of the subgroups, divided by the theoretical maximum number of links possible between the members. We note that our model formulation does not depend on this de<sup>fi</sup>nition, and an alternate de<sup>fi</sup>nition of cohesiveness or even any other SN criterion may be used here.

The objective function we use is to maximize the global cohesiveness given by

$$
\sum_ {j = 1} ^ {w} \sum_ {q = 1} ^ {s _ {j}} V _ {j q} c o h _ {j q}\tag{2}
$$

## 3.1.4. Constraints

1. Each work<sup>fl</sup>ow\_instance, $w _ { j } ,$ can be assigned only one possible subgroup out of the relevant $s _ { j } .$

2. Each member must not over<sup>fl</sup>ow his/her work time for the workload (time capacity).

To model constraint 1

$$
\sum_ {q = 1} ^ {s _ {j}} V _ {j q} = 1 \text { for   all } j = 1, \dots , w\tag{3}
$$

To model constraint 2

For a given subgroup q, each member, $m _ { i } ,$ , has an assigned role. The time required for that role is represented as $t _ { i q . }$ We assume that each member m works for a maximum of $T _ { i }$ time units. If we want to provide for overtime, it is straightforward to add slack to the time for each member by increasing $T _ { i \cdot }$ Then we have:

$$
\sum_ {j = 1} ^ {w} \sum_ {q = 1} ^ {s _ {j}} V _ {j q} t _ {i q} \leq T _ {i} \text {for all} i = 1,.., \mathrm{m}\tag{4}
$$

Expressions (2) and (3) comprise a standard set partitioning model. The objective is to select the optimum combination of entities to “cover” the speci<sup>fi</sup>ed work<sup>fl</sup>ow\_instances. Constraint (4) is an additional requirement to force compliance with member workload capacities. Thus, the work<sup>fl</sup>ow allocation formulation is a type of set partitioning model with additional constraints. Having formulated the 0–1 integer programming optimization model, we next present the representation and solution method.

## 3.2. Representation of the model and workflow allocation

Our model representation requires four input matrices:

$$
\begin{array}{l} \mathrm {WR = \{w r _ {\mathrm{jk}} |j = 1..w\wedge k = 1..r\wedge \forall j,k:0\Leftarrow w r _ {\mathrm{jk}} \Leftarrow 1\}} \\ \mathrm {MR = \{m r _ {\mathrm{ik}} |i = 1..m\wedge k = 1..r\wedge \forall i,k: m r _ {\mathrm{ik}} = 1\lor m r _ {\mathrm{ik}} = 0\}} \\ \mathrm {MM = \{m m _ {\mathrm {ii^{\prime}}} |i = 1..m\wedge i^{\prime} = 1..m\wedge \forall i, i^{\prime}:0\Leftarrow m m _ {\mathrm {ii^{\prime}}} \Leftarrow 1\}} \\ \mathrm {WT = \{w t _ {j} |j = 1..w\wedge \forall j:0\Leftarrow w t _ {j} \Leftarrow\infty\}} \end{array}
$$

WR consists of W rows and R columns, and each element describes the extent of contribution of a role in that work<sup>fl</sup>ow instance. MR is a binary matrix that consists of M rows and R columns, and each element describes if a member is eligible to perform that role or not. MM has M rows and M columns and captures the actual links between the members in the SN. The WT column vector consists of W rows, and each element represents the time units consumed by that work<sup>fl</sup>ow.

The overall representation and solution method is shown in Fig. 2.

For each work<sup>fl</sup>ow $w _ { j } ,$ the solution space matrix $\mathsf { W I _ { j } }$ represents all the possible member allocations for performing the work<sup>fl</sup>ow, based on the input matrices. Each row represents one possible allocation of members that satis<sup>fi</sup>es the input criteria. If a role is not utilized in the work<sup>fl</sup>ow, then all values in that column are set $\mathrm { t o } - 1$ . Each element

$$
\left.\begin{array}{l}W R\\M R\\M M\\W T\end{array}\right\}\rightarrow \quad \text { Solution   Space   Representation   (WI) } \rightarrow \text { Integer   Program   Solver(CPLEX) }
$$

For each workflow $W _ { \mathrm { j } } \quad ( \ j \ = \ 1$ to w)

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Compute $s_j = \prod_{k=1}^{R} Z_k \begin{pmatrix} c_k \\ 1 \end{pmatrix}$ subgroups
Where $j = 1, \ldots, w$ and
$Z_k = 1 / \begin{pmatrix} c_k \\ 1 \end{pmatrix}$ if $Y_{kj} = 0$ and
$Z_k = 1$ if $Y_{kj} &gt; 0$;
Create a matrix $WI_j$ with $s_j$ rows and $r$ columns;
Initialize all elements in $WI_j$ to -1;
For each column $k$ in $WI_j$ ( $k = 1$ to $r$)
If $WR_{jk} &gt; 0$ (role is utilized in $w_j$) then
Sequentially write the id of all members that can provide
that role down the kth column of $WI_j$ (one id per element),
repeating the list down the column until all rows of $WI_j$ have been
filled in the kth column;
Sort the $WI_j$ matrix along the kth column, in ascending order
utilizing a standard sort procedure such as Quick sort;
End if
End For $k$
End For $j$

Fig. 3. Algorithm for generating the WI matrix for workflow w
</div>

in $\mathrm { W I _ { j } } = - 1$ or a member number of a member that can potentially perform that role, based on information in MR. The solution space representation for each work<sup>fl</sup>ow is a generated matrix $\mathsf { W I } _ { \mathrm { j } } = \{ \boldsymbol { w } i _ { q k } \ |$ | $\mathsf { q } = 1 . . 5 _ { j } \wedge \mathsf { k } = 1 . . \mathsf { r } \wedge \forall \mathsf { q } , \mathsf { k } \colon - 1 < = w i _ { \mathrm { k q } } < = \mathsf { m } \jmath .$

Fig. 3 depicts the algorithm used to generate each $\mathsf { W I _ { j } }$ matrix.

Once the WI matrix is generated for all $j = 1 , . . . , | \mathsf { W } |$ , the following information is input to the CPLEX integer program solver:

$\mathrm { T _ { i } } \ \forall \ \mathrm { i } = 1 . . \mathrm { m }$ (the total time each member can work in the time period) along with any slack

\- s (the total number of subgroups in the solution space for all work<sup>fl</sup>ows)

\- |W|

\- |M|

$\mathsf { W I } _ { \mathrm { j } } \forall j = 1 . .$ w

\- The amount of time each member spends in each subgroup in the solution space (this varies from 0.0 if the member is not in the subgroup to a <sup>fi</sup>nite number)

\- The COH measure for each subgroup in the solution space.

With these inputs, the CPLEX solver executes a standard integer programming solution, to identify a solution that maximizes the global cohesiveness of teams that will perform the workload.

## 3.3. Illustrative example utilizing AWSM

The example we present illustrates the usage of AWSM in a simple scenario, and promotes understanding of the methodology. In this

<table><tr><td></td><td>Systems Analyst</td><td>UI Dev</td><td>Serv Prgmr</td><td>DB Sp</td></tr><tr><td>Andrew</td><td>1</td><td>1</td><td>1</td><td>0</td></tr><tr><td>Bob</td><td>0</td><td>0</td><td>0</td><td>1</td></tr><tr><td>Charlene</td><td>1</td><td>0</td><td>0</td><td>0</td></tr><tr><td>Jane</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Mary</td><td>0</td><td>0</td><td>1</td><td>1</td></tr></table>

Fig. 4. MR: MxR role capability matrix.

$$
w _ {j}.
$$

scenario, there are <sup>fi</sup>ve members in a workgroup: Andrew, Bob, Charlene, Jane and Mary, who work as part of a technical consulting team. There are four organizational roles supported by the <sup>fi</sup>ve group members: systems analyst, user interface developer (UI Dev), server programmer (Serv Prgmr) and database specialist (DB Sp).

Each member can perform one or more of these roles, as shown in the MR matrix in Fig. 4. A value of 1 in row $< \mathrm { i } \mathrm { j } >$ indicates that a member m<sub>i</sub> can perform role $r _ { j } .$ There are 20 work<sup>fl</sup>ow\_instances that need to be performed by this group, over a period of time, representing two work<sup>fl</sup>ow\_types: a) making previously developed web system prototypes functional, and b) developing new web system prototypes for end users to evaluate.

Based on the manager's experience, adding functionality to previously created prototypes requires 20% of time from a Systems Analyst, 60% of time from a DB Sp and 20% time from a Serv Prgmr. Each instance of this work<sup>fl</sup>ow\_type takes approximately 3 weeks, and there are 8 instances in the workload under consideration. Creating a new web prototype for a customer requires 20% of time from a Systems Analyst, 60% of time from a UI Dev and 20% time from a Serv Prgmr. Each instance of this work<sup>fl</sup>ow\_type typically takes 4 weeks, and there are 12 instances in the workload under consideration.

Operating under the premise that tasks in both work<sup>fl</sup>ow\_types are closely interrelated, and performance metrics correlate positively with team cohesiveness, the problem the project manager faces is how to form teams to complete the work<sup>fl</sup>ows in this workload, so as to maximize the overall team cohesiveness for the workload.

For the 5 members, $\begin{array} { r l } { \operatorname* { m } _ { 1 } , \dots \operatorname { m } _ { 5 } , } \end{array}$ , we have an exogenous socio-matrix MM of size $5 \times 5 ,$ as shown in Fig. 5.

<table><tr><td></td><td>Andrew</td><td>Bob</td><td>Charlene</td><td>Jane</td><td>Mary</td></tr><tr><td>Andrew</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Bob</td><td>1</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Charlene</td><td>1</td><td>0</td><td>1</td><td></td><td></td></tr><tr><td>Jane</td><td>0</td><td>1</td><td>0</td><td>1</td><td></td></tr><tr><td>Mary</td><td>0</td><td>1</td><td>0</td><td>0</td><td>1</td></tr></table>

Fig. 5. MM: MxM non-directional socio-matrix

<table><tr><td></td><td>Systems Analyst</td><td>UI Dev</td><td>Serv Prgmr</td><td>DB Sp</td></tr><tr><td>W1</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W2</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W3</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W4</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W5</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W6</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W7</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W8</td><td>0.2</td><td>0.0</td><td>0.2</td><td>0.6</td></tr><tr><td>W9</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W10</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W11</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W12</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W13</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W14</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W15</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W16</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W17</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W18</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W19</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr><tr><td>W20</td><td>0.2</td><td>0.6</td><td>0.2</td><td>0.0</td></tr></table>

Fig. 6. WR: WxR work<sup>fl</sup>ow roles matrix.

Each cell in the matrix has a value=1 if the two members cross a pre-determined threshold on a dimension that enhances team cohesiveness, otherwise it has a value=0. Example dimensions include instrumental or expressive ties [37]. Instrumental ties include work related advice and respect, and are thought to be critical to team effectiveness while expressive ties are more informal and based on friendship [28]. A binary, non-directional representation of a social network is well accepted in the social network literature [56]. However, continuous values from 0→1 can also be used in the MM matrix, with no changes in the rest of the AWSM methodology.

We wish to compute the optimal allocation for a steady state organizational workload of eight instances of the <sup>fi</sup>rst work<sup>fl</sup>ow type and 12 instances of the second.

The total time unit worked by the total of all members is:

$$
(8 t _ {1} + 1 2 t _ {2}) = (8 * 3 + 1 2 * 4) = 7 2 \text { weeks }.
$$

The WR matrix is shown in Fig. 6 for the 20 work<sup>fl</sup>ow\_instances. The <sup>fi</sup>rst eight represent instances of the <sup>fi</sup>rst work<sup>fl</sup>ow type, and the remaining 12 represent instances of the second type.

The WT matrix (not shown) will simply list the time unit for each work<sup>fl</sup>ow\_instance. In this example, it will consist of 20 rows with values of 3 time units for the <sup>fi</sup>rst eight work<sup>fl</sup>ows, and 4 time units for the remaining 12 instances.

Consider the <sup>fi</sup>rst work<sup>fl</sup>ow\_instance, $\mathsf { W } _ { 1 } .$ As shown in Fig. 6, it requires 20% of the time for a Systems Analyst (which can be satis<sup>fi</sup>ed by Andrew, Charlene or Jane), 20% of time by a Serv Prgmr (which can be performed by Andrew or Mary) and 60% of its time by a DB Sp (which can be ful<sup>fi</sup>lled by Bob or Mary). The candidate subgroups that can be used to accomplish the <sup>fi</sup>rst work<sup>fl</sup>ow instance are shown in Fig. 7 along with their cohesiveness for each subgroup. For example, the second candidate subgroup consists of Charlene, Andrew and Bob, and has a cohesiveness of $2 / 3 = 0 . 6 6 ,$ since there are 3 possible links between 3 people, but only two members of this group have a social link, as shown in the MM socio-matrix in Fig. 5.

The WI matrix for this illustrative example was generated based on the algorithm in Fig. 3, and lists 240 possible member sets (subgroups) as the solution space. There are 96 possible subgroups for the <sup>fi</sup>rst eight work<sup>fl</sup>ow instances (12 subgroups each), and 144 possible subgroups for the second set of 12 work<sup>fl</sup>ow\_instances (also 12 each). The <sup>fi</sup>rst 12 rows in the WI matrix are shown in Fig. 7. It is important to note that only one of these subgroups will be selected in the solution set, and will represent the subgroup allocated to work on w .

As part of this research, we implemented the ideas described in Section 3 in Java™. The program takes as input the MR, MM, WR and WT matrices, and outputs a <sup>fi</sup>le that lists all the possible subgroups for each work<sup>fl</sup>ow instance in the workload. This output <sup>fi</sup>le is then further input to a CPLEX solver that selects the subgroups that will globally optimize the cohesiveness.

Fig. 1 in Appendix 1 is a partial snapshot of the data <sup>fi</sup>le generated by our program for the insurance workload problem. For the workload in this problem, the time “capacity” of each member in the group was computed to be 72/5 with a 20% slack allowed for overtime (the slack can be set to any value in the program), which equals 17.28 weeks. The number of possible subgroups for the workload, the number of members and number of work<sup>fl</sup>ow instances are listed next in the <sup>fi</sup>le. The “quali<sup>fi</sup>ed” section lists the subgroups quali<sup>fi</sup>ed to perform each work<sup>fl</sup>ow instance; for example, subgroups 1–12 are listed as potential subgroups for work<sup>fl</sup>ow\_instance 1.

Below this, a fragment of the “timereq” section is shown, that lists the number of weeks used in each of the 240 possible subgroups. Thus, Andrew would work for 1.20 weeks in subgroup 1, 0.6 weeks in subgroups 2–4, 0.0 weeks in subgroups 5–6 and so on. Similarly, looking at the next open bracket, towards the bottom of the fragment, we <sup>fi</sup>nd that Bob would work 1.8 weeks in the subgroups 1–6. Again, we note that from subgroups 1–12 only one subgroup will be selected to implement the <sup>fi</sup>rst work<sup>fl</sup>ow instance of the <sup>fi</sup>rst work<sup>fl</sup>ow type, which is adding functionality to previously developed web system prototypes. Similarly, from subgroups 13–24, one will be selected to implement the second work<sup>fl</sup>ow instance, and so on. In all 20 subgroups from the 240 potential subgroups will be selected, one for each of the 20 work<sup>fl</sup>ow\_instances that make up the workload in this example.

<table><tr><td></td><td>Systems Analyst</td><td>UI Dev</td><td>Serv Prgmr</td><td>DB Sp</td><td>Cohesiveness</td></tr><tr><td>S1</td><td>Andrew</td><td>Not Needed</td><td>Andrew</td><td>Bob</td><td>1.00</td></tr><tr><td>S2</td><td>Charlene</td><td>Not Needed</td><td>Andrew</td><td>Bob</td><td>0.66</td></tr><tr><td>S3</td><td>Jane</td><td>Not Needed</td><td>Andrew</td><td>Bob</td><td>0.66</td></tr><tr><td>S4</td><td>Andrew</td><td>Not Needed</td><td>Mary</td><td>Bob</td><td>0.66</td></tr><tr><td>S5</td><td>Charlene</td><td>Not Needed</td><td>Mary</td><td>Bob</td><td>0.33</td></tr><tr><td>S6</td><td>Jane</td><td>Not Needed</td><td>Mary</td><td>Bob</td><td>0.66</td></tr><tr><td>S7</td><td>Andrew</td><td>Not Needed</td><td>Andrew</td><td>Mary</td><td>0.33</td></tr><tr><td>S8</td><td>Charlene</td><td>Not Needed</td><td>Andrew</td><td>Mary</td><td>0.33</td></tr><tr><td>S9</td><td>Jane</td><td>Not Needed</td><td>Andrew</td><td>Mary</td><td>0.00</td></tr><tr><td>S10</td><td>Andrew</td><td>Not Needed</td><td>Mary</td><td>Mary</td><td>0.33</td></tr><tr><td>S11</td><td>Charlene</td><td>Not Needed</td><td>Mary</td><td>Mary</td><td>0.33</td></tr><tr><td>S12</td><td>Jane</td><td>Not Needed</td><td>Mary</td><td>Mary</td><td>0.33</td></tr></table>

Fig. 7. W1-1: Possible subgroups for the <sup>fi</sup>rst work<sup>fl</sup>ow instance.

Fig. 2 in Appendix 1 shows another fragment of the data <sup>fi</sup>le for this problem. The top of the fragment indicates the times that would be used by the last member (Mary) for each of the 240 potential subgroups. The lower half of the fragment shows the cohesiveness values for each of the 240 subgroups. For example, the cohesiveness value for subgroup 2 is 0.66. The cohesiveness is a group level measure, dependent on the structure of the composition of each subgroup, and the overall MM socio-matrix.

The task for the CPLEX optimizer is to create a set of subgroups (one subgroup for each work<sup>fl</sup>ow instance) so that global cohesiveness (across all selected subgroups) is maximized. It needs to do this given the time capacity permitted to each member. Consider the 12 candidate subgroups for work<sup>fl</sup>ow instance $\mathsf { w } _ { 1 } ,$ shown in Fig. 7. If each member was allowed to work for unlimited time, the optimizer would obviously select subgroup 1, since it has the highest cohesiveness (1.00) within the <sup>fi</sup>rst 12 candidate subgroups. However, if time capacity is a constraint, then subgroup 1 may actually be suboptimal for the overall global cohesiveness for the workload, since it may prevent the selection of other subgroups in other work<sup>fl</sup>ow instances that contribute more to the global cohesiveness. The second constraint in our model is that one subgroup from each set needs to be selected, so that the entire workload consisting of 20 work<sup>fl</sup>ow instances is satis<sup>fi</sup>ed. Given the <sup>fi</sup>le with the constraints speci<sup>fi</sup>ed, the optimal solution set that was generated by the CPLEX optimizer (b1 sec for the problem) is shown in Fig. 8.

Note that the solution in Fig. 8 maximizes the global cohesiveness for the workload, while still taking into account the capacity constraint that no member can work more than a certain amount of time (we set 17.28 weeks in this case). In our model, the greater the slack in how much “overtime” a member is theoretically allowed, the larger the global cohesiveness that can be achieved, since subgroups with higher cohesiveness can be selected from each group. In many real world situations, overtime may need to be allocated, if some people are critical to several different work<sup>fl</sup>ows and perform roles that others cannot. In some of the empirical test cases we ran (described ahead in Section 3.4), setting the “overtime” to 0% led to no feasible solution, because it became impossible to <sup>fi</sup>nd a candidate subgroup for each work<sup>fl</sup>ow instance and still allow each person to work with no overtime.

Having illustrated the usage of AWSM, we next present a formal time complexity analysis of the methodology and an empirical test using real world size problems.

## 3.4. Performance analysis of AWSM

As shown in Fig. 2, the AWSM methodology consists of generating the feasible subgroups for each work<sup>fl</sup>ow instance (solution space), and then solving using an available solver such as CPLEX. The solution space representation consists of two steps: formulating the possible subgroups for each work<sup>fl</sup>ow instance and arranging them in a matrix WI.

In order to analyze the limits on the solution space size in real world problems, we introduce two parameters: Maximum Roles Per Work<sup>fl</sup>ow (MRW) and Maximum Members Per Role (MMR). MRW is the upper limit of the number of roles that can occur in a workflow\_ instance for the particular organization. Clearly, MRW also represents the upper limit of the number of constituent activities that are used to model a work<sup>fl</sup>ow in that organization, though we note in some cases the same role may perform multiple activities. Nevertheless, in general, MRW is a good representation of the size of each work<sup>fl</sup>ow in terms of its constituent activities, so that if the organization chooses to model several activities in each work<sup>fl</sup>ow, the number of work<sup>fl</sup>ows will be smaller for a particular workload, but the MRW will be a larger number.

MMR represents the upper limit on the number of human actors that are allowed to perform each role in the organization. A typical value for this may be 3 or 4, but clearly the larger the value of MMR the greater the number of possible teams that can be formed for each work<sup>fl</sup>ow.

Given these two parameters, the upper bound on the value of the total solution space size s in Eq. (1) becomes

$$
s \Leftarrow | W | ^ {*} (M M R) ^ {M R W}.\tag{5}
$$

<table><tr><td></td><td>Systems Analyst</td><td>UI Dev</td><td>Serv Prgmr</td><td>DB Sp</td><td>Subgroup Selected</td><td>Team Cohesiveness</td></tr><tr><td>W1</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>5 (from 1-12)</td><td>0.33</td></tr><tr><td>W2</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>17 (from 13-24)</td><td>0.33</td></tr><tr><td>W3</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>29 (from 25-36)</td><td>0.33</td></tr><tr><td>W4</td><td>Andrew</td><td>Not needed</td><td>Andrew</td><td>Bob</td><td>37 (from 37-48)</td><td>1.00</td></tr><tr><td>W5</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>53 (from 49-60)</td><td>0.33</td></tr><tr><td>W6</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>65 (from 61-72)</td><td>0.33</td></tr><tr><td>W7</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>77 (from 73-84)</td><td>0.33</td></tr><tr><td>W8</td><td>Charlene</td><td>Not needed</td><td>Mary</td><td>Bob</td><td>89 (from 85-96)</td><td>0.33</td></tr><tr><td>W9</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>107 (from 97-108)</td><td>0.00</td></tr><tr><td>W10</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>119 (from 109-120)</td><td>0.00</td></tr><tr><td>W11</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>131 (from 121-132)</td><td>0.00</td></tr><tr><td>W12</td><td>Charlene</td><td>Andrew</td><td>Andrew</td><td>Not needed</td><td>134 (from 133-144)</td><td>1.00</td></tr><tr><td>W13</td><td>Charlene</td><td>Andrew</td><td>Andrew</td><td>Not needed</td><td>146 (from 145-156)</td><td>1.00</td></tr><tr><td>W14</td><td>Charlene</td><td>Andrew</td><td>Andrew</td><td>Not needed</td><td>158 (from 157-168)</td><td>1.00</td></tr><tr><td>W15</td><td>Charlene</td><td>Andrew</td><td>Andrew</td><td>Not needed</td><td>170 (from 169-180)</td><td>1.00</td></tr><tr><td>W16</td><td>Charlene</td><td>Andrew</td><td>Andrew</td><td>Not needed</td><td>182 (from 181-192)</td><td>1.00</td></tr><tr><td>W17</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>203 (from 193-204)</td><td>0.00</td></tr><tr><td>W18</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>215 (from 205-216)</td><td>0.00</td></tr><tr><td>W19</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>227 (from 217-228)</td><td>0.00</td></tr><tr><td>W20</td><td>Charlene</td><td>Jane</td><td>Mary</td><td>Not needed</td><td>239 (from 229-240)</td><td>0.00</td></tr></table>

Fig. 8. AWSM solution for the insurance problem to maximize the overall cohesiveness.

For example, if there were 3 roles per work<sup>fl</sup>ow, and the maximum number of members per role was 4, then a maximum of $4 ^ { 3 } = 6 4$ subgroups are possible for each work<sup>fl</sup>ow in the workload.

The complexity of the algorithm that creates the WI matrix (Fig. 3) is analyzed next. The outer for-loop executes |W| times. The computation of the <sup>fi</sup>rst part of the algorithm that computes the solution space for each work<sup>fl</sup>ow is (MMR)<sup>MRW</sup>. The second part of the algorithm sorts the rows in the solution space a maximum of MRW times. Assuming a sorting algorithm such as quicksort, with a time complexity of nlogn, the complexity of the second part of the algorithm is $\mathsf { M R W } ^ { * } ( ( \bar { \mathsf { M M R } } ) ^ { \mathrm { M R W } } ^ { * } ( \bar { \mathsf { l o g } } \mathrm { ( \bar { M M R } ) ^ { M R W } ) } )$

Hence the overall time complexity for generating the WI matrix is

$$
\begin{array}{l} = | W | ^ {*} (\text {MMR}) ^ {\text {MRW}} + | W | ^ {*} \text {MRW} ^ {*} \Big ((\text {MMR}) ^ {\text {MRW}} * \Big (\log (\text {MMR}) ^ {\text {MRW}} \Big) \Big) \\ = | W | ^ {*} (\text {MMR}) ^ {\text {MRW}} \Big (1 + \text {MRW} ^ {*} \log (\text {MMR}) ^ {\text {MRW}} \Big). \end{array}\tag{6}
$$

As can be seen, the time complexity is exponential in MRW and MMR, and linear in |W|. Eq. (6) indicates that care should be taken when modeling work<sup>fl</sup>ows to reduce the number of roles in the work<sup>fl</sup>ows. A larger work<sup>fl</sup>ow instance can be modeled as multiple smaller work<sup>fl</sup>ows, with the possibility splitting all the way down to 2–3 role work<sup>fl</sup>ows. This will increase the number of work<sup>fl</sup>ows, but should not impact the solution as much as increasing the number of roles per work<sup>fl</sup>ow (taking smaller work<sup>fl</sup>ows and modeling them as a larger work<sup>fl</sup>ow).

## 3.5. Empirical analysis

As mentioned earlier, we implemented the entire infrastructure described in Section 3 in ${ \mathrm { J a V a } } ^ { \mathrm { T M } } ,$ , at a cost of approximately 400 programming hours. For illustration, the outline of the methods used in the code is available at http://nfp.cba.utulsa.edu/bajaja/SocialNetworks/index.html. The software developed as part of this project is also available to the research community as open source via the same website. Once the WI matrix is generated by the software, it is written to the output <sup>fi</sup>le that is further input into the integer program solver. For this empirical analysis, we used CPLEX version 11, on a 3.2 Ghz Intel Pentium 4 processor with 4 Gbytes of main memory. CPLEX invokes a mixed integer programming (MIP) solver to solve the constrained set partitioning problem. Various solution strategies such as depth <sup>fi</sup>rst and best bound are available to the user. In this application, we used the default solution strategies offered by CPLEX which are to balance optimality and feasibility and to use a best bound search.

We tested AWSM for three differently sized hypothetical organizations: 20 members and 10 roles, 40 members and 20 roles, and 60 members and 30 roles. For each organizational size, we set the MRW parameter to 3. The MMR was set to 9 for the <sup>fi</sup>rst organization, 6 for the second organization and 9 for the third organization. After the MR matrix was generated, the WR (work<sup>fl</sup>ow-role), MM (membermember socio-matrix) and WT (work<sup>fl</sup>ow-time) matrices were randomly generated. Each organization was tested for workloads of 1000, 2000 and 3000 work<sup>fl</sup>ow\_instances. One MR matrix was used for each organization; however 5 different WR, MM and WT matrices were generated using random seeds for each workload. A 20% overtime slack capacity was allowed in all cases. Fig. 12 lists the results of the empirical analysis. For example, the <sup>fi</sup>rst <sup>fi</sup>ve rows represent the <sup>fi</sup>rst workload for the organization with 20 members and 10 roles, with 1000 work<sup>fl</sup>ow\_instances, for the <sup>fi</sup>ve randomly generated WR, MM and WT matrices.

The constrained set partitioning model can involve large scale 0–1 integer problems. As can be seen, the <sup>fi</sup>rst feasible solution found is of very high quality and typically well within 1% of optimality; the maximum gap relative to the optimal solution was 1.26%. In 20% of the test problems, the <sup>fi</sup>rst solution found was optimal. The maximum computation time of the <sup>fi</sup>rst solution was 158 s for the largest organization with the maximum workload. A CPLEX solution polishing heuristic, that employs an evolutionary solver, was applied to one of the test problems, but failed to improve the <sup>fi</sup>rst solution in 600 s of CPU time. The speed and accuracy of the <sup>fi</sup>rst solution suggests a practical strategy of terminating the branch and bound MIP solver with the <sup>fi</sup>rst solution since a signi<sup>fi</sup>cant amount of computation time is required to establish optimality and the expected gain in solution quality is nominal. The empirical data in Fig. 9 shows that the AWSM model is capable of optimizing the allocation of work<sup>fl</sup>ows for most practical sized real world problems, including large scale ones involving more than 600,000 binary variables.

## 4. Discussion

Tasks in organizations are increasingly being executed by teams/ workgroups that are created and disbanded <sup>fl</sup>uidly [20]. Social network analysis represents an important framework that can help us better understand how workgroups can function more effectively and/or ef<sup>fi</sup>ciently. In a recent meta-analysis on the effect of SN metrics on team performance, [3] state, “Indeed, unresolved empirical questions and theoretical debates persist about whether or not some social network features yield improved task completion or longer survival in teams.” One reason for this gap in knowledge may be the lack of empirical tools to investigate the correlations between social network metrics and workgroup performance. In this work, we have presented and implemented the AWSM methodology that allows for optimal formation of work<sup>fl</sup>ow groups, with the <sup>fl</sup>exibility of “plugging in” any group level variable as the optimizing variable. For this paper, we use cohesiveness as the example optimizing criterion, but the AWSM methodology is <sup>fl</sup>exible in that any optimizing criterion may be used. Hence, it represents an important infrastructure that can serve as a springboard for future empirical research that investigates the links between social network structure and workgroup performance.

By some estimates, over the next few years as much as 50% of the US workforce will work in small co-located or virtual teams [52]. As research in the area of team performance grows, several variables that measure group characteristics may emerge to in<sup>fl</sup>uence group performance. Example variables similar to cohesiveness that can be used to form optimized work teams using AWSM include the group potency [8,23] and team-member exchange [36,49]. Group potency is the shared belief amongst team members that the team can effectively perform diverse tasks. Team-member exchange is the average measure of members' willingness to perform extra tasks to help other members, and the extent to which these are recognized by other team members.

Another set of variables that may potentially be used as optimizing criteria in AWSM include task-ef<sup>fi</sup>cacy related variables. For example, [21] suggested that group cohesiveness in the widely understood sense of “mutual positive attitudes” may not be suf<sup>fi</sup>cient to explain group performance for many tasks. The commitment of the members to the primary group task was a more important explanatory variable for team performance. Thus, measures of group cohesiveness that deal with social affection should be replaced in part by measures that include, for example, the perceived effectiveness with which group members co-ordinate their activities.

Not only is AWSM independent of the optimizing criterion, but it is also independent of the measures used to operationalize a particular construct that may be used to optimize workgroup formation. This is particularly helpful in an area where the research is constantly

<table><tr><td></td><td></td><td>Variables</td><td>Constraints</td><td>Nonzero Coeffs</td><td>Obj fun</td><td>Time of First Sol</td><td>Gap</td><td>Time of Opt Sol</td></tr><tr><td rowspan="5">20 R 10W 2000</td><td>1</td><td>193,533</td><td>1020</td><td>752,381</td><td>1000</td><td>13 sec.</td><td>0.14%</td><td>8.66 min</td></tr><tr><td>2</td><td>191,631</td><td>1020</td><td>744,635</td><td>1000</td><td>13 sec</td><td>0.10%</td><td>8.48 min</td></tr><tr><td>3</td><td>193,730</td><td>1020</td><td>753,561</td><td>1000</td><td>14 sec</td><td>0.14%</td><td>17.05 min</td></tr><tr><td>4</td><td>189,041</td><td>1020</td><td>738,917</td><td>1000</td><td>10 sec</td><td>0%</td><td>0.25 min</td></tr><tr><td>5</td><td>193,026</td><td>1020</td><td>750,179</td><td>1000</td><td>16 sec</td><td>0.07%</td><td>9.00 min</td></tr><tr><td rowspan="5">20 R 10W 2000</td><td>1</td><td>383,651</td><td>2020</td><td>1,491,752</td><td>2000</td><td>42 sec</td><td>0%</td><td>.758 min</td></tr><tr><td>2</td><td>381,425</td><td>2020</td><td>1,482,555</td><td>2000</td><td>34 sec</td><td>0%</td><td>.635 min</td></tr><tr><td>3</td><td>386,068</td><td>2020</td><td>1,501,242</td><td>2000</td><td>27 sec</td><td>0%</td><td>.507 min</td></tr><tr><td>4</td><td>379,138</td><td>2020</td><td>1,475,250</td><td>2000</td><td>38 sec</td><td>0.14%</td><td>64.08 min</td></tr><tr><td>5</td><td>384,707</td><td>2020</td><td>1,496,000</td><td>2000</td><td>32 sec</td><td>0.08%</td><td>35.31 min</td></tr><tr><td rowspan="5">20 R 10W 3000</td><td>1</td><td>571,276</td><td>3020</td><td>2,221,783</td><td>3000</td><td>58 sec</td><td>0.04%</td><td>72.80 min</td></tr><tr><td>2</td><td>571,067</td><td>3020</td><td>2,223,369</td><td>3000</td><td>58 sec</td><td>0.04%</td><td>73.31 min</td></tr><tr><td>3</td><td>575,782</td><td>3020</td><td>2,239,135</td><td>3000</td><td>49 sec</td><td>0%</td><td>0.81 min</td></tr><tr><td>4</td><td>570,346</td><td>3020</td><td>2,218,539</td><td>3000</td><td>59 sec</td><td>0%</td><td>1.08 min</td></tr><tr><td>5</td><td>573,531</td><td>3020</td><td>2,230,504</td><td>3000</td><td>70 sec</td><td>0%</td><td>1.25 min</td></tr><tr><td rowspan="5">40 R20W 1000</td><td>1</td><td>216,000</td><td>1040</td><td>852,654</td><td>1000</td><td>21 sec</td><td>0.51%</td><td>20.99 min</td></tr><tr><td>2</td><td>216,000</td><td>1040</td><td>851,984</td><td>1000</td><td>21 sec</td><td>0.37%</td><td>10.76 min</td></tr><tr><td>3</td><td>216,000</td><td>1040</td><td>852,734</td><td>1000</td><td>21 sec</td><td>0.07%</td><td>10.79 min</td></tr><tr><td>4</td><td>216,000</td><td>1040</td><td>853,300</td><td>1000</td><td>34 sec</td><td>0.30%</td><td>22.54 min</td></tr><tr><td>5</td><td>216,000</td><td>1040</td><td>852,520</td><td>1000</td><td>27 sec</td><td>0.54%</td><td>21.19 min</td></tr><tr><td rowspan="5">40 R20W 2000</td><td>1</td><td>432,000</td><td>2040</td><td>1,705,520</td><td>2000</td><td>56 sec</td><td>0%</td><td>1.00 min</td></tr><tr><td>2</td><td>432,000</td><td>2040</td><td>1,704,716</td><td>2000</td><td>58 sec</td><td>0.20%</td><td>42.05 min</td></tr><tr><td>3</td><td>432,000</td><td>2040</td><td>1,704,344</td><td>2000</td><td>52 sec</td><td>0.05%</td><td>42.56 min</td></tr><tr><td>4</td><td>432,000</td><td>2040</td><td>1,706,106</td><td>2000</td><td>63 sec</td><td>0.03%</td><td>42.66 min</td></tr><tr><td>5</td><td>432,000</td><td>2040</td><td>1,705,416</td><td>2000</td><td>51 sec</td><td>0.10%</td><td>42.19 min</td></tr><tr><td rowspan="5">40 R20W 3000</td><td>1</td><td>648,000</td><td>3040</td><td>2,557,992</td><td>3000</td><td>87 sec</td><td>0.03%</td><td>94.62 min</td></tr><tr><td>2</td><td>648,000</td><td>3040</td><td>2,557,730</td><td>3000</td><td>81 sec</td><td>0%</td><td>1.46 min</td></tr><tr><td>3</td><td>648,000</td><td>3040</td><td>2,556,852</td><td>3000</td><td>82 sec</td><td>0%</td><td>1.53 min</td></tr><tr><td>4</td><td>648,000</td><td>3040</td><td>2,558,900</td><td>3000</td><td>87 sec</td><td>0%</td><td>1.56 min</td></tr><tr><td>5</td><td>648,000</td><td>3040</td><td>2,558,068</td><td>3000</td><td>87 sec</td><td>0.07%</td><td>96.23 min</td></tr><tr><td rowspan="5">60R30W 1000</td><td>1</td><td>214,969</td><td>1060</td><td>852,203</td><td>1000</td><td>31 sec</td><td>0.24%</td><td>10.91 min</td></tr><tr><td>2</td><td>218,094</td><td>1060</td><td>864,266</td><td>1000</td><td>27 sec</td><td>0.34%</td><td>22.06 min</td></tr><tr><td>3</td><td>216,467</td><td>1060</td><td>858,523</td><td>1000</td><td>28 sec</td><td>1.26%</td><td>32.04 min</td></tr><tr><td>4</td><td>216,467</td><td>1060</td><td>856,853</td><td>1000</td><td>121 sec</td><td>0.03%</td><td>2.05 min</td></tr><tr><td>5</td><td>215,896</td><td>1060</td><td>859,608</td><td>1000</td><td>33 sec</td><td>1.23%</td><td>21.65 min</td></tr><tr><td rowspan="5">60R30W 2000</td><td>1</td><td>428,708</td><td>2060</td><td>1,699,101</td><td>2000</td><td>57 sec</td><td>0.29%</td><td>82.24 min</td></tr><tr><td>2</td><td>432,000</td><td>2060</td><td>1,704,716</td><td>2000</td><td>58 sec</td><td>0.20%</td><td>42.18 min</td></tr><tr><td>3</td><td>430,825</td><td>2060</td><td>1,708,324</td><td>2000</td><td>75 sec</td><td>0.02%</td><td>42.33 min</td></tr><tr><td>4</td><td>430,214</td><td>2060</td><td>1,706,887</td><td>2000</td><td>92 sec</td><td>0.05%</td><td>1.63 min</td></tr><tr><td>5</td><td>429,806</td><td>2060</td><td>1,704,161</td><td>2000</td><td>72 sec</td><td>0.24%</td><td>1.20 min</td></tr><tr><td rowspan="5">60R30W 3000</td><td>1</td><td>645,412</td><td>3060</td><td>2,558,418</td><td>3000</td><td>129 sec</td><td>0.01%</td><td>94.07 min</td></tr><tr><td>2</td><td>646,847</td><td>3060</td><td>2,564,046</td><td>3000</td><td>100 sec</td><td>0.01%</td><td>94.21 min</td></tr><tr><td>3</td><td>650,252</td><td>3060</td><td>2,578,360</td><td>3000</td><td>94 sec</td><td>0.06%</td><td>187.36 min</td></tr><tr><td>4</td><td>644,940</td><td>3060</td><td>2,558,524</td><td>3000</td><td>158 sec</td><td>0.02%</td><td>94.46 min</td></tr><tr><td>5</td><td>644,817</td><td>3060</td><td>2,557,196</td><td>3000</td><td>80 sec</td><td>0.34%</td><td>183.31 min</td></tr></table>

Fig. 9. Empirical analysis of varying workloads of three organizations.

evolving, and where the debate about what constitutes appropriate measures for constructs such as cohesiveness, for example, has raged for several decades [14,42,53]. As Section 3 indicates, the optimizing criterion needs to be selected and operationalized prior to the application of AWSM so that the MM matrix can be generated. In a <sup>fi</sup>eld setting, construction of the MM matrix would require that questionnaires be used to calculate the links between members of the organization. Several operationalizations are available in the SNA literature. For example, in [33], employees were asked to make a list for each of the other members that the other members would consider personal friends. In [6], employees were asked to list coworkers with whom they talked frequently about work related topics, whom they considered close friends, who they depended on for inputs for their work and whom they provided outputs of their work.

Operationalizations of group level constructs can be of two types: individual–individual and individual–group. An individual–individual measure represents a member's perception of each of the members in the subgroup, while an individual–group measure represents a member's perception of the group as a whole. In Section 3 we demonstrated AWSM with cohesiveness measured using individual– individual links (the MM matrix). AWSM can be also used with a measure that uses the individual's perceptions of the subgroup. The value for this measure for each subgroup in the solution space will have to be calculated outside of AWSM (by using a survey, for example) and then “plugged in” to obtain the optimal subgroups, just as the values for the MM matrix are used as input to AWSM in Section 3. A third alternative, in the interest of expedience for real world scenarios, is to have the manager input their estimate of the criterion value for each subgroup, and use that to allocate the work<sup>fl</sup>ows.

As the discussion above indicates, AWSM can be used to create optimized work<sup>fl</sup>ow teams along a selected metric that may be operationalized in different ways. While group cohesiveness is the metric used in this paper, other metrics such as team leader centrality [6] can also be used to predict team performance. From a practical standpoint, AWSM is particularly useful for work<sup>fl</sup>ows that consist of activities, each of which can be performed by multiple actors. This is becoming increasingly prevalent as organizations standardize much of their work processes using enterprise resource planning (ERP) systems and cross train employees. Once managers have a choice of employees to allocate to each activity, productivity can be leveraged by utilizing the social network measures to decide who gets cross-trained in which activities.

A second practical application for AWSM is the allocation of processes (screens) to employees when an off-the-shelf large scale IS is implemented. Typically, with a large scale implementation, there is disruption of current employee processes, and there is some choice as to retraining employees in the new processes offered by the system. Social network metrics can serve as a useful criterion for creating subgroups that would perform work<sup>fl</sup>ows on the new system.

## 5. Conclusion

While our work here represents an important step in modeling optimal workgroup formation, the model has three limitations that can be addressed in future research. First, the roles of different actors in the model are exogenous, and are not included as decision variables. An extension to our model would be to allow organizational actors to be linked to roles as part of the decision model, so that training of actors in performing speci<sup>fi</sup>c roles can be optimized. This would involve creating a separate MR matrix where each actor would be linked to all possible roles in which they could be trained. The problem may then be modeled as a multi criteria optimization problem where the optimization goals would be maximizing the global cohesiveness (or other measure) and minimizing training costs.

A second limitation of our model is that it does not take differential dependencies between work<sup>fl</sup>ow activities into consideration. It assumes that all activities constituting the work<sup>fl</sup>ow are equally dependent on each other. A more complex model would take into account differential dependencies between work<sup>fl</sup>ow activities and consider only subgroups cohesiveness for activities that are dependent on each other. Our current model does allow this by breaking up a work<sup>fl</sup>ow with differential dependencies between activities into smaller work<sup>fl</sup>ows, where the activities are equally dependent on each other; however this places somewhat greater burden on the work<sup>fl</sup>ow analyst.

A third limitation is that the MM matrix is regarded as an exogenous variable in our model. However, if the workload period is of suf<sup>fi</sup>cient duration, it is possible that the MM matrix may be altered, as members interact with each other. Incorporating the MM matrix as an endogenous variable is beyond the scope of this work, but would make for an interesting extension to the AWSM model.

In this work, the set partitioning problem was solved using the default strategies offered by CPLEX. Our empirical analysis shows that this is suf<sup>fi</sup>cient for real world size problems. However, a possible avenue for future work is to formulate heuristic strategies or evolutionary meta-heuristics that can allow solutions for much larger problems involving thousands of members and roles. For example, in many situations it may not be necessary to maximize or minimize the social network metric; a heuristic threshold level of the metric may satis<sup>fi</sup>ce. A related limitation is that in the AWSM method, sets of work<sup>fl</sup>ows are optimized at one time. In reality, actors may have differing capacities for each work<sup>fl</sup>ow instance, as workloads vary dynamically over time. An interesting extension of the work presented here would be to incorporate varying capacities of actors for each work<sup>fl</sup>ow and possibly, dynamic work<sup>fl</sup>ows occurring over a rolling time horizon.

The major theoretical contribution of this work is the creation and implementation of a formal model that incorporates ideas from two diverse <sup>fi</sup>elds: social network theory and work<sup>fl</sup>ow modeling, and allows optimization of work groups based on any social network criterion. In order to implement this model we also presented algorithms to structure and represent the problem so that standard integer program solvers can attempt to solve it. We also present a performance analysis of the AWSM methodology that demonstrates its feasibility for real world modeling and indicates that breaking up work<sup>fl</sup>ows into smaller sub-<sup>fl</sup>ows will allow larger problems to be solved.

From a theoretical standpoint, the AWSM methodology opens up a new opportunity to investigate which group level variables actually drive team performance for certain types of tasks. As an example, consider a real organization with prede<sup>fi</sup>ned work<sup>fl</sup>ows. Two different group level variables can be compared by <sup>fi</sup>rst creating two sets of optimal subgroups, based on each variable, and then asking managers and other stakeholders to compare these subgroups. Similar, AWSM can also facilitate the study of which criteria drive team performance in which types of work<sup>fl</sup>ows (for example transactional versus creative types of work<sup>fl</sup>ows).

From a practical perspective, the methodology and tool developed here can be immediately applied in diverse settings, to create workgroup teams based on a selected optimizing criterion, hopefully resulting in an immediate positive impact on organizational effectiveness. Diverse stakeholders such as consultants and line managers can use AWSM as a decision support tool to help create work<sup>fl</sup>ow schedules in an operational time frame. AWSM will be especially useful in applications where there is a choice of several possible teams that can be created in order to perform organizational tasks and where they differ widely along the selected optimizing criterion.

## Acknowledgements

The authors would like to acknowledge the efforts and comments of the editor and three reviewers, which greatly enhanced the quality of the <sup>fi</sup>nal paper.

## Appendix 1

![](/api/attachments/KTNADTF9/fulltext/images/c1329829df12213d83965bb4de1cf40ae745b52fddb1c0e3acadc6326ac4732a.jpg)

<table><tr><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td></tr><tr><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.120</td><td>0.60</td><td>0.60</td></tr><tr><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.23</td><td>0.60</td><td>0.60</td><td>0.00</td></tr><tr><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>1.20</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td></tr><tr><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td></tr><tr><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.88</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td></tr><tr><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.88</td><td>0.80</td><td>3.22</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td></tr><tr><td>3.20</td><td>3.20</td><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.88</td><td>0.88</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.88</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td></tr><tr><td>1.60</td><td>0.80</td><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.88</td><td>0.88</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.88</td><td>0.09</td><td>0.00</td><td>4.00</td><td>3.20</td><td>3.20</td><td>1.60</td><td>0.88</td></tr><tr><td>0.80</td><td>3.20</td><td>2.40</td><td>2.40</td><td>0.80</td><td>0.00</td><td>0.00</td><td>]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

<table><tr><td>[ 1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td></tr><tr><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.88</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td></tr><tr><td>1.80</td><td>1.80</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td></tr><tr><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.06</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

Fig. 1. Fragment of output <sup>fi</sup>le for illustrative problem input to CPLEX solver.

<table><tr><td>[0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.60</td><td>0.60</td><td>0.60</td><td>1.80</td><td>1.80</td><td>1.80</td><td>2.40</td><td>2.40</td><td>2.40</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.80</td><td>0.80</td><td>C-1.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.88</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.88</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.00</td><td>0.00</td><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.88</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>0.00</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.80</td><td>0.88</td><td>0.80</td><td>0.80</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>]</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>cohesivity = [1.00 0.66 0.66 0.66 0.33 0.66 0.33 0.33 0.33 0.33 0.33 1.00 0.66 0.66 0.66 0.33 0.66 0.33 0.33 1.00 0.66 0.66 0.66 0.33 0.66 0.33 0.33 0.33 1.00 0.66 0.66 0.33 1.00 0.66 0.66 0.33 1.00 0.66 0.33 1.00 0.33 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.00 1.03 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.11 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.10 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.12 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.13 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.14 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.15 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.16 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.17 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.18 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.28 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.29 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.32 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.33 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.34 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.35 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.36 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.37 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.38 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.39 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.40 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.41 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.42 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.43 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.44 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.45 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.46 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.47 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.48 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.49 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.50 1.51 1.51 1.51 1.51 1.51 1.51 1.51 1.51 1.51 1.51 1.51 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.52 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.53 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.54 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.55 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.56 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.57 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.58 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.59 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.60 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.62 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.63 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.64 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.65 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.66 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.67 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.68 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.69 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.70 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 1.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 2.72 3</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Fig. 2. Second fragment of output <sup>fi</sup>le input to CPLEX solver.

## References

[1] R.D. Alba, A graph-theoretic de<sup>fi</sup>nition of a sociometric clique, Journal of Mathematical Sociology 3 (1973) 113–126.

[2] J.T. Austin, P. Bobko, Goal setting theory: unexplored areas and future research needs, Journal of Occupational Psychology 58 (1985) 289–308.

[3] P. Balkundi, D.A. Harrison, Ties, leaders and time in teams: strong inference about network structure's effects on team viability and performance Academy of Management Journal 48 (1) (2006) 49–68.

[4] A. Basu, R.W. Blanning, Metagraphs in work<sup>fl</sup>ow support systems, Decision Support Systems 25 (3) (1999) 199–208.

[5] R.D. Bock, S.Z. Husain, An adaptation of Holzinger's B-coef<sup>fi</sup>cients for the analysis of sociometric data, Sociometry 13 (1950) 146–153.

[6] D.J. Brass, Being in the right place: a structural analysis of individual in<sup>fl</sup>uence in an organization, Administrative Science Quarterly 29 (4) (1984) 518–539.

[7] D.J. Brass, A social network perspective on human resource management, in: G. Ferris (Ed.), Research in Personnel and Human Resource Management, JAI Press, Greenwicj, CT, 1995, pp. 39–79.

[8] M.A. Campion, E.A. Papper, G.J. Medsker, Relations between team characteristics and effectiveness: a replication and extension, Personnel Psychology 49 (1996) 429-452.

[9] F. Casati, S. Castano, M. Fugin, Management work<sup>fl</sup>ow authorization constraints through active database technology, Information Systems Frontiers 3 (3) (2001) 319–338.

[10] R. Collins, Theoretical Sociology, Harcourt Brace Jovanovich, New York, 1988.

[11] C. Corbridge, L. Martin, C.S. Purdy, Allocating Tasks in Future Naval Systems: A Way Forward, Defence Research Agency, 1994.

[12] K. Corts, Teams vs. Individual Accountability: Solving Multi-Task Problems through Job Design, The RAND Journal of Economics 38 (2) (2007) 467–479.

[13] R. Cross, A. Parker, L. Prusak, S.P. Borgatti, Knowing what we know: supporting knowledge creation and sharing in social networks, Organizational Dynamics 30 (2) (2001) 100–120.

[14] G.H. Dobbins, S.J. Zaccaro, The effects of group cohesion and leader behavior on subordinate satisfaction, Group and Organization Studies 11 (1986) 203–219.

[15] M.G. Evans, Organizational behavior: The central role of motivation, Journal of Management 12 (1986) 203–222.

[16] L. Festinger, Informal social communication,Psychological Review 57 (1950) 271–282. [16] L. Festinger, Informal social communication, Psychological Review 57 (1950) 271–282.

[17] P.M. Fitts, Human Engineering for an Effective Air Navigation and Traf<sup>fi</sup>c Control System, National Research Council, 1951.

[18] L.C. Freeman, Cenrtality in social networks, Social Networks 1 (1979) 215–239.

[19] N.E. Friedkin, Structural cohesion and equivalence explanations of scoial homogeneity, Sociological Methods and Research 12 (1984) 235–261.

[20] R.J. Gerard, Teaming up: making the transition to self-directed, team-based organizations, Academy of Management Executive 9 (1995) 91–93.

[21] P.S. Goodman, E. Ravlin, M. Schminke, Understanding groups in organizations, in: L.L. Cummings, B.M. Staw (Eds.), Research in Organizational Behavior, JAI Press, Greenwich, CT, 1987, pp. 121–173.

[22] G. Governatori, A. Rotolo, S. Sadiq, A model of dynamic resource allocation in work<sup>fl</sup>ow systems, Fifteenth Australasian database conference, 2004, pp. 197–206, Dunedin, New Zealand.

[23] T. Hecht, N. Allen, E. Kelly, Group beliefs, ability, and performance: the potency of group potency, Group Dynamics: Theory, Research, and Practice 6 (2) (2002) 143–152.

[24] T. Hemmer, On the interrelation between production technology, job design, and incentives, Journal of Accounting and Economics 19 (1995) 209–245.

[25] A. Hevner, S. March, J. Park, S. Ram, Design science research in information systems, MIS Quarterly 28 (1) (2004) 75–105.

[26] B.R. Holmstrom, P. Migrom, Multitask principal-agent analyses: incentive contracts, asset ownership, and job design, Journal of Law, Economics, and Organization 7 (1991) 24–52.

[27] P. Hornby, W.C. Clegg, J. Robson, C.R.R. McLaren, S.C.S. Richardson, Human and organizational issues in information systems development, Behavior and Information technology 11 (1992) 160–174.

[28] H. Ibarra, Personal networks of women and minorities in management: a conceptual framework, Academy of Management Journal 36 (1993) 56–87.

[29] H. Itoh, Job design, delegation, and cooperation: a principal-agent analysis, European Economic Review 38 (1994) 691–700.

[30] M.H. Jordan, H.S. Feild, A.A. Armenakis, The relationship of group process variables and team performance, A Team-Level Analysis in a Field Setting Small Group Research 33 (1) (2002) 121–150.

[31] B. Jukic, R. Simon, W.S. Chang, Congestion based resource sharing in multi-service networks, Decision Support Systems 37 (3) (2004) 397–413.

[32] H. Kautz, B. Selman, M. Shah, ReferralWeb: combining social networks and collaborative <sup>fi</sup>ltering, Communications of the ACM 30 (3) (1997)

[33] D. Krackhardt, M. Kidluff, Whether close or far: perceptions of balance in friendship networks in organizations, Journal of Personality and Social Psychology 76 (5) (1999) 770–782.

[34] A. Kumar, W.M.V.D. Aalst, E.M. Verbeek, Dynamic work distribution in work<sup>fl</sup>ow management systems: how to balance quality and performance? Journal of Management Information Systems 18 (3) (2001) 129–157.

[35] D. Liben-Nowell, J. Kleinberg, The link prediction problem for social networks, 12th Annual ACM International Conference on Information & Knowledge Management (CIKM), 2003, pp. 556–559.

[36] R.T. Liden, S.J. Wayne, R.T. Sparrowe, An examination of the mediating role of psychological empowerment on the relations between the job, interpersonal relationships, and work outcomes, The Journal of Applied Psychology 85 (2000) 407–416.

[37] J.R. Lincoln, J. Miller, Work and friendship ties in organizations: a comparative analysis of relationship networks. Administrative Science Ouarterly 24 (1979) 181-199.

[38] M. Maheswaran, H. Siegel, A synamic matching and scheduling algorithm for heterogeneous computing systems, Seventh IEEE Heterogeneous Computing Workshop, 1998, pp. 57–69.

[39] S. Menon, Effective reformulations for task allocation in distributed systems with a large number of communicating tasks, IEEE Transactions on Knowledge and Data Engineering 16 (12) (2004) 1497–1508.

[40] M. Momotko, K. Subieta, Dynamic changes in work<sup>fl</sup>ow participant assignment, East European Conference on Advances in Databases and Information Systems, 2002, Bratislava.

[41] J.l. Moreno, Who shall survive? A new approach to the problems of human interrelations, Nervous and Mental Disease Publishing Co, Washington, DC, 1934.

[42] P.E. Mudrack, Group cohesiveness and productivity: a closer look, Human Relations 42 (9) (1989) 771–785.

[43] S. Narasimhan, S. Ram, Database allocation in a distributed environment: incorporating concurrency control and queuing costs, Management Science 40 (8) (1994) 969–983.

[44] M.T. Older, P.E. Watterson, C.W. Clegg, A critical assessment of task allocation methods and their applicability, Ergonomics 40 (2) (1997) 151–171.

[45] M. Parameswaran, J. Stallaert, A.B. Whinston, A Market-Based Allocation Mechanism for the DiffServ Framework, Decision Support Systems 31 (3) (2001) 351–361.

[46] P. Raghavan, Social networks: from the web to the enterprise, IEEE Internet Computing 6 (1) (2002) 91–94.

[47] L.D. Sailer, S.J.C. Gaulin, Proximity, sociality and observation: the de<sup>fi</sup>nition of social groups, American Anthropologist 86 (1984) 91–98.

[48] K. Sanders, A. Nauta, Social cohesiveness and absenteeism: the relationship between characteristics of employees and short-term absenteeism within an organization, Small Group Research 35 (6) (2004) 724–741.

[49] A. Seers, M.M. Petty, J.F. Cashman, Team-member exchange under team and traditional management, A Naturally Occurring Quasi-Experiment Group & Organization Management 20 (1) (1995) 18–38.

[50] G. Simmel, The web of group af<sup>fi</sup>liations, in: G. Simmel (Ed.), Con<sup>fl</sup>ict and the Web of Group Af<sup>fi</sup>liations, Free Press, Glencoe, IL, 1955.

[51] R. Steinmark, Group cohesiveness and extrinsic motivation in virtual groups: lessons from an action case study of electronic brainstorming, 35th Hawaii International Conference on System Sciences (HICSS), IEEE. Hawaji, 2002, p. 16b.

[52] G.L. Stewart, C.C. Manz, H.P. Sims, Team work and group dynamics, John Wiley and Sons, Inc., New York, New York, 1999

[53] R.M. Stodgill, Group productivity, drive and cohesiveness, Organizational Behavior and Human Performance 8 (1972) 26–53.

[54] J. Thomas, R. Grif<sup>fi</sup>n, The social information processing model of task design: a review of the literature, Academy of Management Review 8 (1983) 672–682.

[55] I. Valsecchi, Policing team production through job design, Journal of Law, Economics, and Organization 12 (2) (1996) 361–375.

[56] S. Wasserman, K. Faust, Social network analysis: methods and applications, Cambridge University Press, Cambridge, 1999.

Akhilesh Bajaj is Professor and Chapman Endowed Chair of MIS, at the University of Tulsa. He received a B. Tech. in Chemical Engineering from the Indian Institute of Technology Bombay in 1989 an MBA from Cornell University in 1991, and a Ph.D. in MIS (minor in Computer Science) from the University of Arizona in 1997. Dr. Bajaj's research deals with the construction and testing of tools and methodologies that facilitate the construction of large organizational systems, as well as studying the decision models of the actual consumers of these information systems. He has published articles in several academic journals such as Management Science, IEEE Transactions on Knowledge and Data Engineering, Information Systems, Journal of the Association of Information Systems and the Journal of Information Systems. He is on the editorial board of several journals in the MIS area. His research has been funded by the department of defense (DOD). He teaches undergraduate and graduate courses on basic and advanced database systems, management of information systems, and enterprise wide systems.

Robert Russell is a Collins Professor of Operations Management at the University of Tulsa, He received a Ph.D, in operations research from The University of Texas at Austin in 1972. Professor Russell's research interests include logistics and supply chain management, vehicle routing, meta-heuristics for combinatorial optimization, and sports scheduling. He has published in academic journals such as Management Science, Operations Research, Decision Sciences, Transportation Science, INFORMS Journal on Computing, European Journal of Operational Research, International Journal of Production Research, Journal of the Operational Research Society, and Networks as well as other journals. He is a member of the editorial board of the International Journal of Services and Operations Management and The International journal of Revenue Management. He teaches graduate courses in operations research, supply chain management, decision modeling and analysis, and computer simulation.
