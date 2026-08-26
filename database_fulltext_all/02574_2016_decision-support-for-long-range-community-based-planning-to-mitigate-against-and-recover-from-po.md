---
otero_id: 2574
otero_key: "ZMCN2HXM"
title: "Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters"
authors: "Josey Chacko; Loren Paul Rees; Christopher W. Zobel; Terry R. Rakes; Roberta S. Russell; Cliff T. Ragsdale"
year: "2016"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2016.04.005"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters

Josey Chacko <sup>a</sup>, Loren Paul Rees <sup>b,</sup>⁎, Christopher W. Zobel <sup>b</sup>, Terry R. Rakes <sup>b</sup>, Roberta S. Russell <sup>b</sup>, Cliff T. Ragsdale <sup>b</sup>

<sup>a</sup> Richard J. Bolte, Sr., School of Business, Mount St. Mary's University, Emmitsburg, MD 21727, USA

<sup>b</sup> Department of Business Information Technology, Virginia Polytechnic Institute and State University, Blacksburg, VA 24061, USA

## a r t i c l e i n f o

Article history: Received 31 December 2014 Received in revised form 20 February 2016 Accepted 21 April 2016 Available online xxxx

Keywords: Decision support Resilience Sustainability Mathematical programming Disaster planning Multi-hazard

## a b s t r a c t

This paper discusses a new mathematical model for community-driven disaster planning that is intended to help decision makers exploit the synergies resulting from simultaneously considering actions focusing on mitigation and efforts geared toward long-term recovery. The model is keyed on enabling long-term community resilience in the face of potential disasters of varying types, frequencies, and severities, and the approach's highly iterative nature is facilitated by the model's implementation in the context of a decision support system. Three examples from Mombasa, Kenya, East Africa, are discussed and compared in order to demonstrate the advantages of the new mathematical model over the current ad hoc mitigation and long-term recovery planning approaches that are typically used.

© 2016 Elsevier B.V. All rights reserved.

## 1. Introduction

Disasters, whether natural disasters like hurricanes, earthquakes, or tsunamis, or socio-technical disasters such as terrorist attacks, are a significant problem with worldwide impacts, and an increasing number of people are subject to their effects [54]. Furthermore, many areas are actually subject to the impacts of different types of disasters (such as wildfires and landslides in Southern California [19]), or to the same type of disaster striking an area multiple times over the course of many years (such as flooding in Bangladesh [59]). As communities in these areas seek to make strategic investments that can improve their ability to withstand and recover from such disasters, it is therefore important for them to adopt a comprehensive, long-term view that acknowledges the likelihood that multiple disasters will occur.

Because there is a significant amount of complexity associated with determining the most appropriate strategy to follow in such an environment, suitable analytical tools are needed in order to facilitate such efforts. This paper seeks to address this need by introducing a decision support system (DSS) framework for long-range, values-based, community-driven planning in the context of multiple potential disaster events. The focus of our discussion will be on the mathematical model at the core of this DSS, which provides communities with the new opportunity to assess strategies for both disaster mitigation and disaster recovery. As this model is the first of its kind in this genre, we will expend some effort defining the major features that it incorporates and listing caveats that it avoids.

Our discussion begins with a detailed look at disaster planning and community-driven decision making, as well as the use of analytical models to support more effective mitigation and recovery strategies. It then presents and discusses the new mathematical model, and it discusses its implementation in the context of the decision support system. Finally, the model's potential for improving multi-hazard decision making is illustrated by comparing three different real-world scenarios focused on the community of Mombasa, Kenya, in East Africa. The paper concludes with a discussion of the managerial and academic implications of the work, followed by a look at promising future research directions.

## 2. Background

It is well recognized that disaster operations management can be broken into five overlapping phases: mitigation, preparedness, response, short-term recovery, and long-term recovery, each of which occurs in a repeating cycle. Mitigation activities tend to be associated with strengthening capabilities in advance of a future disaster event, whereas preparedness activities tend to be focused on minimizing the actual social, economic, and physical impacts of a disaster before it occurs. Immediately after a disaster strikes, in the response phase, emergency responders initiate activities that are focused on life safety issues. Short-term recovery activities then are used to help transition to long-term recovery and the restoration of the affected community to a properly functioning state (which may be better or worse than its prior state) [22,51].

Much of the current analytical work in disaster operations management tends to focus on the emergency of the disaster—the middle three phases of disaster operations management: preparedness, response, and short-term recovery [22,33,45], and on the specific characteristics of a particular disaster event, or type of disaster, with which these phases are associated [24]. It is important to recognize, however, that there are broader issues of safety that encompass the entire range of hazards that may pose a risk to a city [6,42]. For example, an urban city center such as San Francisco, CA, with a population close to 850,000, is at risk not only from earthquakes but also from wildfires, tsunamis, landslides, flooding, heat waves, and droughts [4]. It is for this reason that institutions such as the U.S. Federal Emergency Management Agency (FEMA) [18] and the United Nations [53] have promoted the use of a “multihazard” approach to risk assessment for more than 10 years.

A multi-hazard perspective acknowledges that multiple different disasters may occur in a given location, possibly simultaneously or with cascading effects, but potentially also independently and in a serial nature. Significant synergistic benefits can be achieved by considering more than one type of hazard in the planning process, including substantial economic and outcome efficiencies [42]. In order to achieve such synergistic benefits, however, we must take a strategic, more sustainable view of disaster operations management, which requires a particular focus on the first and last phases of the disaster management cycle. Such a view allows us to simultaneously consider both actions that mitigate against disasters and actions that enable more effective recovery, and, in particular, to examine opportunities for combining both types of activities over more than just a single-disaster event. No academic work currently exists that explicitly combines both mitigation and recovery in the context of planning for multiple types of disasters. Over the course of our discussion below, we will demonstrate the advantage of taking such an approach over current approaches which involve no long-range mitigative and recovery-based analytical planning. Furthermore, we will also demonstrate the added superiority of considering multiple hazard types rather than planning for just one type—even when both mitigation and recovery are both included in the analysis.

Inherent in taking such a longer-term, multi-hazard view is the need to explicitly consider the input of the community for whom the protective or recovery actions are being taken. The voice of the affected community itself is critical to the sustainability of development-oriented programs [28], and community acceptance of a plan is crucial if investment is to be made in a disaster management solution that will be implemented over the long term. As the literature has indicated for years (e.g., [7,40,50]), disaster officials often fail to determine and include community members' needs in their planning. Whether the community provides direct input into the decision process, or whether their values and interests are instead represented by a spokesperson, actively advocating for their needs is critical.

## 3. Model development

Existing analytical models in disaster operations management typically consider a single type of hazard [24]. Moreover, those that consider a range of hazards (analytical multi-hazard models) typically focus on risk reduction [24], and as a result, post-disaster management is not considered. This can be seen in Table 1, which provides a summary of the main model features represented in a review of the analytical multi-hazard model literature.

According to Kappes et al. [24], appropriate multi-hazard modeling requires the following key elements: (i) accounting for the additional interactions that exist among disaster management elements; (ii) considering both pre- and post-disaster management concomitantly, which is essential for community/asset viability; and (iii) as noted in Cox [16] and in Chacko et al. [14], under budget constraints, there is a need for incorporating mathematical optimization models.

The only work that provides a complete mathematical optimization model, Zhang et al. [60], models only resource allocation during disaster response. Their model does not account for post-disaster management actions and, moreover, does not account for the interactions between different elements. Similarly, although Chacko et al. [14] offer discussion on the objective function and dependency constraints in a multi-hazard context, they do not develop the entire mathematical model or model the post-disaster management phase. In short, there is no extant work in the literature that, for multi-hazard analysis, optimizes over the long-term, including both recovery and mitigation, much less accounts for the unique interactions inherent in multi-hazard models. The research in this paper is intended to fill this gap.

The iterative and interactive nature of the community-based, analytical planning model presented below is particularly suited to a decision support system (DSS) (e.g., [26,47]). When a community utilizes the model and planning approach set forth in this paper, more than just a single model will be built, run, and implemented. Rather, baseline models are run, output is generated and then discussed by the community, which in turn necessitates that additional inputs be considered, and model variants be run. A unified system incorporating both the data and model components made accessible to the user (the community) in a transparent and facilitative manner is therefore preferred. DSS provides just such a framework ([47], p. 29). Fig. 1A provides a general model of a DSS, and Fig. 1B shows this general structure implemented in the context of the specific DSS developed in this paper.

## 3.1. Incorporating community inputs

An important consideration of this modeling framework is that communities may wish to express that either “formal policies” or “ad hoc strictures” be included in the solution generated, such as the community's saying:

• we desire equity across all regions in terms of funds disbursed for recovery per dollar of damage;

• we will not allow rebuilding in the flood plain;

• we will insist that all rebuilding meets new, tougher building codes;

• we wish to take advantage of the opportunity to improve the downtown business district when recovery is necessary, as that will attract new industry/merchants to the city.

We encourage such planning and include it, if desired, as additional constraints in our model.

Although different communities – particularly in different countries – propose and approve mitigation and recovery endeavors using different mechanisms, we assume here that whatever the specific custom may be for approval, certain minimal, basic data must be furnished. Project costs, benefits, equipment demands, personnel needs, time constraints, etc., must all be specified by region as appropriate, and any synergies obtained across projects (e.g., if projects 4 and 7 are both undertaken, a savings of 30% occurs) must also be listed. Regions may be defined in terms of existing political units, as we do in our Mombasa, Kenya, example below, or they may be defined as “areas” that contain assets that must be protected (e.g., that part of Washington, DC, around the White House), or such as “the downtown business district,” “low-income neighborhoods,” or any other “homogeneous” area.

## 3.2. Representing multi-hazard dependencies

The relationships among the common classes in the disaster management process are as follows: hazards (H) impact the community/ critical assets (C), and management strategies (S) requiring available resources (R) are used to intervene to protect and recover the community/ critical assets, by mitigating (in some cases) the effect or magnitude of the hazard itself. The point to be noted here with multi-hazard disaster management is that the complexity of analysis will often be greatly increased, with both positive and negative effects occurring due to the multiplicity of hazards, strategies, critical assets, and available resources; these synergies must be considered—in fact, this is the motivation for multi-hazard analysis. Both the single hazard (“mono-hazard”) and multi-hazard literatures mention complex analyses, discussing dependencies and their synergies. In Table 2, we show this literature and organize it first by within and among dependencies, and then secondly by the specific type of dependency $( \boldsymbol { \mathrm { e . g . , } } \boldsymbol { \mathrm { S = } } \boldsymbol { \mathrm { > C } } )$

Features of analytical multi-hazard models. Table 1

<table><tr><td rowspan="2">Disaster management phases</td><td colspan="5">Methodologies</td><td colspan="9">Multi-hazard synergies (H: hazards; C: critical assets; S: management strategies; R: available resources)</td><td colspan="4">Performance measures</td></tr><tr><td>Game theoretic approaches</td><td>Risk assessment and ranking</td><td>Cost-benefit analysis</td><td>Optimization</td><td>Other</td><td>H-H</td><td>C-C</td><td>S-S</td><td>R-R</td><td>S-C</td><td>S-R</td><td>S-H</td><td>H-C/H-R</td><td>R-S</td><td>Economic cost</td><td>Social cost proxy</td><td>Time</td><td>Other</td></tr><tr><td colspan="19">Primary consideration: Pre-disaster actions</td></tr><tr><td>Abkowitz &amp; Chatterjee [1]</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td></td><td>*</td><td></td><td></td></tr><tr><td>Ayyub et al. [5]</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td><td></td><td>√</td><td>√</td></tr><tr><td>Canto-Perello et al. [12]</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td></tr><tr><td>Chacko et al. [14]</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td></tr><tr><td>Chatterjee &amp; Abkowitz [15]</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td></td><td>*</td><td></td><td></td></tr><tr><td>Dillon et al. [17]</td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td><td></td><td>√</td><td>√</td><td></td><td></td><td>√</td></tr><tr><td>Hausken et al. [21]</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Li et al. [29]</td><td></td><td>√</td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td>√</td><td>√</td><td></td><td></td><td></td></tr><tr><td>Marzocchi et al. [32]</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td></tr><tr><td>Selva [46]</td><td></td><td>√</td><td></td><td></td><td>√</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Stewart &amp; Mueller [49]</td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td>Zhang et al. [60]</td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td></tr><tr><td>Zhuang &amp; Bier [61]</td><td>√</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>√</td><td></td><td></td><td></td><td></td></tr><tr><td colspan="19">Primary considerations: Post-disaster actions</td></tr><tr><td>None</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td colspan="19">Primary considerations: Both pre- and post-disaster actions</td></tr><tr><td>None</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Notice that including dependencies, particularly in optimization models such as mathematical programming models, introduces nonlinearities because constraints are introduced of the form “IF hazard A has already occurred, THEN hazard B's effect will be doubled,” or “IF mitigation project A has already been decided to be implemented, AND IF mitigation project B is implemented simultaneously, THEN combined benefits of the two projects are increased by $3 0 \% \because$ It is well known that such constraints may be linearized using a procedure as exhibited in Williams [58] and Chacko et al. [14]. Note that this linearization does not result in any loss of accuracy; the procedure is a reformulation technique that changes the model structure into a linear form by adding constraints. In this section, we illustrate the process for dependencies between benefits; a similar approach is followed for costs, resources, etc., as in our model examples in Section 5.

Consider a matrix of benefits showing the advantage of undertaking simultaneously projects $\mathrm { x _ { i } }$ and $\mathrm { x _ { i ^ { \ast } } } $

$$
\left( \begin{array}{c c c c} b _ {1 1} & b _ {1 2} & \dots & b _ {1 n} \\ 0 & b _ {2 2} & \dots & b _ {2 n} \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \dots & b _ {n n} \end{array} \right),\tag{1}
$$

where $b _ { i i }$ refers to the benefits purely from project i, and $b _ { i i ^ { \prime } } \left( i \neq i ^ { \prime } \right)$ refers to benefits accruing additionally from the interaction between projects i and i′. If the objective function of the model calculates, for example, the summative benefit of all chosen binary projects, then it is multiplicative (i.e., second order):

$$
\sum_ {i = 1} ^ {n} \sum_ {i ^ {\prime} = 1} ^ {n} b _ {i i ^ {\prime}} x _ {i} x _ {i ^ {\prime}}.
$$

The objective function can be linearized (see, e.g., [14]) by (1) adding a new project k, which is defined as a project that consists of doing projects i and i′ together, and (2) adding the following logical constraints for each project dependency between any two projects i and i′ with i ≠ i′:

$$
2 x _ {k} \leq x _ {i} + x _ {i ^ {\prime}} \leq x _ {k} + 1.\tag{2}
$$

These constraints force the new decision variable $x _ { k }$ to be set to a value of one whenever a dependency occurs (i.e., when both projects i and i’ are undertaken). The net effect on the overall model is simply the inclusion of the additional constraint above (other than the binary constraint) for each combined project. The benefits matrix becomes a (larger) diagonal matrix, and the overall model formulation remains linear.

The method described above can be similarly applied to cost or resource dependencies, so that these constraints will also be extended in the multi-hazard case. Note that, e.g., as in the benefits case, cost dependencies can be in the form of either savings or additional expenses. Also observe that the inclusion of dependencies in the analytical, multihazard planning model necessitates the inclusion of additional input data, namely, the benefit matrix of Eq. (1).

Please cite this article as: J. Chacko, et al., Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.005

A

<table><tr><td>Model Base Management System</td><td>Data Base Management System</td></tr><tr><td colspan="2">Dialog Generation and Management System</td></tr></table>

![](/api/attachments/ZMCN2HXM/fulltext/images/a32003cf8126519c0d6a8114285dcb8464d7d5292017fc306ce14689115ac832.jpg)  
Fig. 1. A. The three parts of a decision support system (Source: [47]). B. The multi-hazard, long-range, community-based DSS of this paper.

Table 2  
Multi-hazard possible synergistic relationships (within and among components).

<table><tr><td>Component relationships</td><td>Description</td><td>Mentioned in multi-hazard disaster mgmt (DM) Lit</td><td>Mentioned in single-hazard DM literature</td></tr><tr><td colspan="4">Dependency (within)</td></tr><tr><td>Hazard-Hazard (H-H)</td><td>Interaction between hazards-these present themselves in multiple forms</td><td>Selva [46]; Marzocchi et al. [32]</td><td>x</td></tr><tr><td>Critical Asset-Critical Asset (C-C)</td><td>Interactions between assets, such as failure dependencies</td><td>Ayyub et al. [5]; Li et al. (2009)</td><td>Maliszewski et al. [31]</td></tr><tr><td>Strategy-Strategy (S-S)</td><td>Interactions between strategies, wherein an intervention strategy improves/degrades performance of another strategy</td><td>Chacko et al. [14]; Stewart &amp; Mueller [49]</td><td>Stewart &amp; Mueller [48]</td></tr><tr><td>Resource-Resource (R-R)</td><td>Interactions between resources, such as failure dependencies</td><td>x</td><td>McLoughlin [34]</td></tr><tr><td colspan="4">Interdependency (among)</td></tr><tr><td>Strategy-Critical asset (S-C)</td><td>Intervention strategy secures multiple assets</td><td>Dillon et al. [17]</td><td>McLoughlin [34]</td></tr><tr><td>Strategy-Available resources (S-R)</td><td>Intervention strategy secures multiple resources</td><td>x</td><td>McLoughlin [34]</td></tr><tr><td>Strategy-Hazard (S-H)</td><td>Intervention strategy secures against multiple vulnerabilities</td><td>Caruson &amp; MacManus [13]; Waugh &amp; Tierney [57]</td><td></td></tr><tr><td>Hazard-Critical asset, Resources (H-C/H-R)</td><td>Hazard affects multiple assets and resources</td><td>Waugh [56]; Ayyub et al. [5]</td><td>McLoughlin [34]</td></tr><tr><td>Resource-Strategy (R-S)</td><td>Application of a resource supports multiple intervention strategies</td><td>Chacko et al. [14]</td><td>x</td></tr></table>

## 3.3. Specifying objective functions

A number of disaster operations related studies are concerned with the terminal value of a measure, or the value of that particular measure at the end of the decision horizon. For example, Jaller [23] employs an objective function that represents benefits that arise based on personpower allocation decisions, and that maximizes the total benefits over all periods. For a community that is under a constant threat of disasters, measures that capture long-term implications such as economic output, infrastructure, quality of life, etc., can be of great value in determining the relative effectiveness of different disaster management policies.

As noted by Perez [41] and Holguin-Veras et al. [22], however, the reality of the social impacts of a disaster implies that both the extent and the duration of a community's suffering should be considered—see their excellent discussion on deprivation costs. One particular type of measure that has been used to represent an entity's capacity for resisting loss and then recovering over time has been resilience [62,64]. Resilience, as a measure, can provide a more complete picture of the community's viability over the long-term by extending the descriptive abilities of short-term emergency related measures such as deprivation costs.

In this research, we allow a community, or its representative, to specify either terminal-valued measures or resilience-based measures, or any combination of the two forms it chooses. As such, we present an objective function formulation for each one as follows.

## 3.3.1. Terminal-value objective function

Consider a measure q(t) of interest to a given community, where this measure is defined over a study horizon [0, T\*]. For example, q(t) might be the value of infrastructure (in €) in the community at time t ∈[0, T\*], or the number of displaced elderly at time t, or the number of jobs lost at time t. The terminal value of q(t) is given by q(T\*).

If we assume that disaster damage is instantaneous and that recovery is linear, or that recovery may be approximated by piecewise linear functions, then a typical plot of a measure q(t) over the study horizon will be of the form shown in Fig. 2. In this figure, we have an initial value for the measure, $I _ { 0 } { = } q ( 0 )$ , which then drops vertically upon the first disaster. It is possible that the full effect of this disaster will not be realized because one or more mitigation projects that were put in place before the disaster occurred are able to reduce the unmitigated effect of the disaster, $D _ { 1 } ,$ , by the combined amount, B<sup>⁎</sup>. If a recovery project is implemented after the disaster, then the level of q(t) builds linearly for the length of that project, resulting in a related recovery of $Y _ { 1 }$ . To then calculate q(T\*), we note that

q(T\*) = Initial Value − ∑ Unmitigated Disaster Damages $+ \ \sum$ Subsequent Recoveries

$$
= I _ {0} - \sum \left(D _ {j} - B _ {j} ^ {*}\right) + \sum \left(Y _ {j}\right)\tag{3}
$$

where the summation is over the disasters and responses to the damages during the study horizon. We note that these values may consist of rough estimates, as they are difficult to measure and obtain.

## 3.3.2. Resilience-based objective function

To measure the resilience of q(t) over the study horizon [0,T\*], we adopt the engineering-based approach of calculating resilience to be the area under q(t) as a percentage of the total area Q\* available if no loss or outside influence on q occurs (see [10,62,63]).

$$
R = \frac {\int_ {0} ^ {T ^ {*}} q (t) d t}{Q ^ {*}}\tag{4}
$$

Note that $\textstyle { \mathrm { Q } } ^ { * } = \int _ { 0 } ^ { T _ { * } } q ( 0 ) d t$ , since q(t) equals q(0) for all t ∈ [0,T\*] if there is no loss.

## 4. Mathematical model

As indicated in Fig. 1B, our decision support system includes spatial and non-spatial data, a mathematical model, and a practical interface to examine and improve possible alternatives. In this section, we first briefly describe the input and output data necessary to support appropriate long-term planning for mitigation and recovery. We then present the details of the mathematical model.

## 4.1. Model inputs and outputs

## 4.1.1. Historical and expert inputs

The following model inputs must be supplied by the community from historical data, or if data are not available, by experts:

• a list of all hazard types that are deemed “relevant” by the community; • the severity (i.e., impact) of each hazard type, by region. The minimum information required by the mathematical model (although more explicit severity definition is encouraged) is the severity's most likely magnitude $( " \mathrm { m } " )$ , its likely smallest (“a”) value, and the severity deemed most pessimistic $( " \mathbf { b } ^ { \prime \prime } )$ in magnitude for each hazard type entry in each region. For example, we might stipulate that a Category 3 hurricane striking the business district region in Portsmouth, VA, would cause infrastructure damage (a, m, b) of (\$3.6 M, \$7.4 M, \$18.2 M).

J. Chacko et al. / Decision Support Systems xxx (2016) xxx–xxx  
![](/api/attachments/ZMCN2HXM/fulltext/images/9994df3d2249bb1e4be9c7518a765acf02064644e8a94630bfe2026efaba09e6.jpg)  
Fig. 2. Disaster–mitigation–recovery sequence.

• The inter-arrival times (IATs) for each hazard type for each region. Again, an (a, m, b) specification is required.

## 4.1.2. Community inputs

The following model inputs must be supplied by the community (or by its representatives):

• A list of possible projects, including all input information required as mentioned in Section 3.1. A benefits matrix must also be included (of the form of Eq. (1)), linking possible projects and dependent benefits/costs/and other synergies.

• Resources available (financial, person-power, equipment; etc.) by time and region.

• Community values (infrastructure, ecology, the elderly, the disadvantaged, jobs, economic development, etc.)

○ Each value must be ranked or positioned in importance relative to the other values specified. Moreover, it is insufficient to say (e.g.) that infrastructure is at top priority, jobs is second, and equity third. Rather, the community must also stipulate whether each measure to be tracked and computed by the model is a terminal value or a resilience measure.

• Additionally, the community may choose to provide extra community constraints as outlined at the start of Section 3.1.

The question to be addressed by the model is, given the possible projects to be undertaken, given the resources available to implement (some of) the projects, and given what the community believes to be its core values in terms of what it wants in terms of infrastructure, equity, elderly, jobs, economic development, etc., what is the best selection and timing of projects, and where will this set of choices leave the community in terms of its desired posture if the hazard types listed strike the community with the severity and frequency specified?

## 4.1.3. Outputs from the Planning model

## The model furnishes the following to the community:

Given the list of projects under consideration, and given the total resources specified, and given the specified list of hazard types and their severities and frequencies, 500 (or more if desired) possible 30-year scenarios of disasters and project implementations are generated. From these, utilizing an expected-value analysis, the median, upperbound, lower-bound, and 95% confidence limit solutions indicate:

• The best mitigation and recovery projects to undertake and skip in terms of meeting the community's specified (and ranked) terminal and resilience values.

• The (likely) severity of damage in each region.

• Vulnerabilities. That is, it is very possible that the community's initial portfolio of projects taken in conjunction with its allocated resources will lead to certain community critical assets being exposed or other vulnerabilities being indicated—in other words, the community's initial plan is not good enough. This, in fact, is one desired outcome of such a planning model—ensuring, through iterative planning, that what the community must have protected is indeed ultimately “covered.”

• Resources expended and resources remaining (if any), for each resource type.

• How the community fared on each of its values and goals. If the community finds out, e.g., through runs of this model, that the business district will do fine in terms of a resilient recovery, but those less well-to-do citizens will be inequitably treated with the resources and projects under consideration, then it may choose to re-evaluate its proposed projects and/or list of goals and ranked objectives.

## 4.2. Model formulation

Methodologically, two well-known solution approaches presented themselves as ready candidates to our problem. The first, dynamic programming, was abandoned after it was realized that (1) there are too many state transitions – actually, an infinite number – in the problem formulation to be included, and (2) that (even if (1) were not a factor) the requisite state transition probabilities would be prohibitively difficult for even experts to specify/stipulate. Consequently, a mathematical programming problem formulation was invoked as the methodology of choice.

In particular, the base model utilized here is the well-known, project-selection, resource allocation model; see, for example, [8,9,11, 30]. This model consists of various objectives or goals, and these are pursued by prescribing which of the community's proposed projects best advance these objectives within the sets of resources available. However, as described above, this basic model must be enhanced with synergistic matrix benefit and cost considerations due to the explicit inclusion of multiple hazard types.

Because of the possible inclusion of resilience in the objective, and the incorporation of benefit-and-cost synergies in the objection function and in constraints, we expect this mathematical programming problem to be nonlinear in general. We linearized these terms using piecewise linear approximations, given that the objective function is separable (see, e.g., [58], for details), we further specify that the binary weights attributed to each linear approximation component are Special Ordered Sets of type 2 (SOS2). Of course, in general, all nonlinear curves may be approximated by straight-line segments, although in practice, the process may require considerable effort and time.

(As discussed earlier, we also linearized the multi-project dependency constraints.)

## 4.2.1. Variables and parameters

The decision variables in the model are as follows: which disaster mitigation projects are to be implemented, including the desired time of each chosen mitigation project's execution, and which recovery projects are to be implemented, along with when (i.e., in response to which disaster event) and to what extent. The planning model may then be described mathematically as follows:

## Index variables

I $\left\{ 1 , . . . , n \right\}$ is the set of potential mitigation projects (e.g., project i ∈ I corresponds to building a sea wall on the waterfront just south of 5th Street);

J $\left\{ 1 , . . . , m \right\}$ is the set of disaster events to be simulated (e.g., the jth disaster to occur $( j \in J ) ^ { \dag } ,$ ); J

H $\{ 1 , . . . , p \}$ is the set of potential hazards (e.g., hazard h∈ H is a hurricane);

R $\{ 1 , . . . , q \}$ is the set of regions (e.g., the business district is the rth region (where r∈ R));

Decision variables

$X _ { i j } = { \left\{ \begin{array} { l l } { 1 , } \\ { 0 , } \end{array} \right. }$ if mitigation project i is implemented in response to disaster j otherwise

$Y _ { j r } =$ the amount of resources allocated to recovery in region $r ,$ in response to disaster j

Indicator variables

$W _ { i , j } = \left\{ { 1 , \atop 0 } \right.$ if mitigation project i is completed before disaster j occurs otherwise

Parameters

$I _ { 0 r }$ is the initial measure/community value for region r ∈ R;

$B _ { i r }$ is the benefit arising from implementing mitigation project i∈I in region r∈R;

$C _ { i j }$ is the cost of implementing mitigation project i∈I in response to disaster j∈J;

$D _ { j r }$ is the expected damages occuring in region $r \in R ,$ because of disaster j;

$\rho$ is the rate at which reconstruction proceeds (e.g.,\$M/year,or homes/year);

$M _ { j } ^ { h }$ is the budget earmarked for hazard h∈H that is used in response to disaster j;

$M _ { j } ^ { C }$ is the common budget,with no specific earmarks, that is used in response to disaster j;

$M _ { j } ^ { U }$ is the budget that was not used in response to the first j disasters (j∈J).

## 4.2.2. Objective function

As discussed above, there are two general forms of an objective function that we consider: the terminal form and a resilience form. The resilience objective is simply calculated as in Eq. (4).

For the terminal objective, Eq. (3) gives the terminal value of the community measure q, chosen to represent the changing level of an important community value or goal over time. Note that the effect of each disaster illustrated in Fig. 2 is actually a random variable, and recall that the mathematical model that we are building here is an expected-value planning model. Stated differently, at any point in time at which the community decides to run the resource allocation planning model, it does so based on the known current state of affairs AND also based on what disasters are expected to occur in the future, and when they are expected. Therefore, by substituting the appropriate parameters, we may rewrite Eq. (3) as:

$$
q (T ^ {*}) = \sum_ {r} \left(I _ {0 r} + \sum_ {j} \left(- D _ {j r} + \sum_ {i} \left(B _ {i r} W _ {i, j} \sum_ {j} X _ {i, j - 1}\right) + Y _ {j r}\right)\right).\tag{5}
$$

For a specific planning study period in a particular community, the inter-arrival times between hazards will be known so that the number of expected disasters, etc., will be known and can be stated explicitly.

Because communities have multiple values and goals that are important to them, we would ultimately expect to have a vector of such output measures, $\overrightarrow { Z } = ( q _ { 1 } , q _ { 2 } , . . . , q _ { z } )$ . As an illustration of this, the example given in Section 5.3 utilizes three different measures: (1) minimize the terminal value of the loss of human life due to disasters, or stated more positively, maximize the terminal value of not-lost human life; (2) maximize the resilience of what we term “economic output” (this may include infrastructure); and (3) maximize the resilience of jobs. To combine these three measures into one objective, we use a MINIMAX MOLP approach (see, e.g., [43]).

## 4.2.3. Constraints

Finally, we present the constraints for the math programming model:

Resource constraints

$$
\sum_ {i \in I ^ {h}} C _ {i j} X _ {i j} \leq M _ {j} ^ {h}; \forall j \in J, \forall h \in H
$$

$$
\sum_ {r \in R} Y _ {j r} \leq M _ {j} ^ {C} + M _ {j - 1} ^ {U}; \forall j \in J
$$

$$
\sum_ {i \in I} C _ {i j} X _ {i j} + \sum_ {r \in R} Y _ {j r} \leq \left(\sum_ {h \in H} M _ {j} ^ {h}\right) + M _ {j} ^ {C} + M _ {j - 1} ^ {U}; \forall j \in J
$$

Linearization constraints (for dependency projects)

$$
2 \sum_ {j} X _ {i j} \leq \sum_ {i \in P} \sum_ {j} X _ {i j} \leq 1 + \sum_ {j} X _ {i j}; \forall j \in J,
$$

where i∈P⊆I indicates all project sets that result in a unique portfolio dependency.

## Additional (optional) community constraints (see Section 3.1)

Set decision variables of some projects to zero and/or adjust resource allocations to regions, etc.

Operational constraints

$$
\sum_ {j \in J} X _ {i j} \leq 1; \forall i \in I
$$

Flow constraints (conservation of resources)

$$
M _ {j} ^ {h} + M _ {j} ^ {C} + M _ {j - 1} ^ {U} = \sum_ {i \in I} C _ {i j} X _ {i j} + \left(\sum_ {r \in R} Y _ {j r}\right) + M _ {j} ^ {U}; \forall j \in J
$$

Non-negativity constraints

$$
X _ {i j} \geq 0; \forall i \in I, j \in J
$$

$$
Y _ {j r} \geq 0; \forall j \in J, r \in R
$$

## 4.3. Implementation

As discussed above, it is critical for (planners in) the community to run the model above in an iterative, interactive fashion. As a case in point, after an initial analysis of the community's proposed projects,

Please cite this article as: J. Chacko, et al., Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.005

J. Chacko et al. / Decision Support Systems xxx (2016) xxx–xxx

the model in example 5–3 below shows that the business district is the least resilient region in Mombasa. Similarly, results may indicate a particularly poor ecological solution, or one that is unequitable to a particular group of citizens. In such cases, planners may choose to add or modify projects until a satisficing solution is obtained.

## 5. Examples

More than a few regions of the world are cradles of conditions that spawn complex disasters. We examine here Kenya's second largest city, Mombasa, a tourist destination that is critical to the Kenyan national economy. As the largest international seaport in East Africa, many east and central African countries rely on the Mombasa port for access to various goods, raw materials, critical machine parts, humanitarian supplies, etc. Mombasa faces risks from multiple significant hazards; the three that are most cited in the literature are flooding, tsunamis, and terrorism. As Mombasa is a heavily populated urban center, when disasters do occur there, they often cause significant consequences. We have chosen such an example to illustrate the modeling approach because “…there are grounds for believing that the most catastrophic effects of supply chain failures (particularly on human life) have occurred in developing countries.” [52]

Flooding. Projections indicate that 17% of Mombasa would be submerged with a sea-level rise of only 30 cm, leading to displacement of people due to flooding, water-logged soils, and reduced crop production caused by salt stress [3]. Moreover, it is estimated that a 1-in-100-year extreme water event (e.g., storm surge) would affect 190,000 people and US\$470 million in assets [25], a significant sum in the Kenyan context.

Terrorism. Al-Shabaab is a Somali group that was designated as a foreign terrorist organization by the U.S. government in 2008; its purpose is to turn Somalia (a neighbor of Kenya), etc., into a fundamentalist Islamic state. The group is believed to be responsible for attacks in Somalia that have killed international aid workers, journalists, civilian leaders, and African Union peacekeepers, and it claimed responsibility for the July 2010 suicide bombings in Kampala, Uganda, that killed more than 70 people, gathering to watch a World Cup final soccer match. In February 2012, the group's leader and al Qaeda leader Ayman al-Zawahiri released a video announcing the alliance of the two organizations. Since that time, al-Shabaab has become a significant terrorist threat to Kenya, with their most press-worthy events being the Westgate Mall bombing in Nairobi during 2013, and the shooting to death of 147 college students during early morning prayer services at Garissa University College in Kenya in April 2015.

Tsunamis. Amollo [2], Ngunjiri [39], Mulwa et al. [36], and Awour et al. [3] highlight the vulnerability of the Mombasa region to both the near-field tsunami risk source from the Davie ridge and far-field risks (for example, the tsunami that occurred off Indonesia in 2001).

Purpose of examples. Three examples showing effects of these three types of hazards on Mombasa, Kenya, are presented in this paper for two purposes: (1) to illustrate the importance of this academic research extension beyond previous work and (2) to demonstrate pedagogically the methodology developed in this paper. The examples all build upon one another as follows:

1. Single-hazard analysis with NO long-term recovery or mitigation considerations included.

2. Single-hazard analysis with long-term recovery and mitigation considerations included.

3. Multiple-hazard analysis with long-term recovery and mitigation considerations included.

Each example presents as output to the community, across the entire horizon of 30 years, a list of projects and when they should be implemented. But also shown are charts and/or graphs of the values of each objective function measure versus time. For example, the community can see how lives are lost over time, and how the value of infrastructure is being decimated by the disasters and rebuilt through each project, as well as (say) the resilience of jobs in each and every region. With this information, the community can see how it is doing in its projected response to what is most likely to occur to it. It may then decide whether the resulting situation is satisfactory, or whether it needs to re-plan and re-think the whole scenario it finds itself in, perhaps defining new projects and/or community goals. It should be noted that although data from Kenyan government reports, etc., were used in these examples, the Kenyan government in no manner agrees to the projects developed or chosen here, or to the conclusions we draw in this research as to how Mombasa disaster management should be conducted.

5.1. Mombasa, Kenya—Single hazard with NO long-term recovery or mitigation analysis

## 5.1.1. Historical and expert inputs to the model

5.1.1.1. Geopolitical regions. As Awour et al. [3] note, politically the Mombasa district is split into four main regions: Mombasa Island (region 1), Kisauni (region 2), Likoni (region 3), and Changamwe (region 4). We adopt these as four regions in our study.

5.1.1.2. Hazards and planning. Flooding. As this first example considers planning for only a single disaster, we select Mombasa's most frequent disaster threat—flooding. In preparation for flooding, we assume the community ensures there is a solid evacuation plan, all proper emergency equipment is either on hand or is readily available, there are sufficient shelters to store displaced individuals, there is a plan for access to adequate food and water and clothing, etc. In short, we assume the community develops detailed, excellent plans for the preparedness, response, and the short-term recovery phases of a flooding disaster. However, in this example, note that we assume that the community has not planned at all for two of the phases of disaster management, namely, mitigating against or recovering in a long-term sense for any type of disaster.

## 5.1.2. Analysis of 5–1 model

Although only flooding was planned for, all three types of disaster actually occur. Using historic data for each of Mombasa's severity losses (i.e., impacts) from flooding and tsunamis in each region, and the time between flooding events and tsunami occurrences there, and using expert opinion to estimate triangular distributions for severity and timing of possible terror attacks in each of Mombasa's four regions, we conduct a simulation of consequences to Mombasa, Kenya, over expected hazards there during a given (30-year) time horizon. [In general, see Kebede et al. [24] and Government of Kenya [20]. For Mombasa flooding inter-arrival times, we used Awour et al. [3]. For tsunamis, our resources were Ngunjiri [39], Amollo [2], Mutimba et al. [37], and Awour et al. [3]] Five hundred different (i.e., statistically independent) replications are generated. (In general, sufficient replications are produced to achieve desired statistical accuracy in output measures; see [27]). In all three examples considered in this paper, hazards are generated according to historical data when it exists, or from expert opinion. If the data cause multiple hazards to occur simultaneously at any time during the independent replications, they are generated in that fashion, and the mathematical model must respond to that combination of impacts at that point in time.

Given initial estimates of infrastructure value/economic output (we include the economy's productive generation as well as the value of its buildings, etc.; see, e.g., Kebede et al. [24]) for each region, the baseline curve of Fig. 3 shows that for the mean response over the 30-year horizon, disasters in Mombasa, Kenya, will reduce the infrastructure value over the four regions so that the infrastructure/economic output is only one-fourth of its initial value. Although the community did an outstanding job preparing for short-term emergency (“lifeline”) activities and thereby saved lives and reduced suffering, they did not consider any mitigative or long-term recovery projects. Consequently, Mombasa did not receive any benefit (lives/jobs/infrastructure) from projects such as building a seawall.

![](/api/attachments/ZMCN2HXM/fulltext/images/1d6e904e4cc171c78b96f050822c7ce7c90f49c9b628953e2f51aace0c0a95a8.jpg)  
Fig. 3. Mean infrastructure value over the 30-year horizon in Mombasa, Kenya, for the three examples.

5.2. Mombasa, Kenya—Single hazard with long-term recovery and mitigation analysis

## 5.2.1. Long-term projects

In this second example, we build on the previous example by (1) maintaining every detailed, excellent plan for the preparedness, response, and short-term recovery phases of a flooding disaster included in Example 5–1, but also by (2) covering the other two, missing phases of disaster recovery, namely, adding various flooding mitigation and long-term recovery projects—but for disasters of type flooding only. In particular, we assume that the community recommends the following four mitigation projects:

Project 1 Build sea walls at the inlet near Mombasa Island (region 1).

Project 2 Develop an early warning system to warn about potential flooding.

Project 3 Upgrade the flood resilience of Mombasa (all regions, but mostly in regions 2 and 3) through vulnerability mapping, training etc.

Project 4 Institute land-management policies to protect and advance mangrove forests on the Kenyan shore, protect natural beaches, and limit human settlement in natural flood plains.

Two points should be noted with regard to how we model these projects. (1) Mombasa does not have the financial resources to fund all four of these projects, and (2) each of these projects is a governmental, city (standard) project complete with implementation details, costs, and benefits. Included in the mathematical model are the financial, human, equipment, time, etc., resource requirements by region for each project; as well as the expected reduction in infrastructure loss in each region should the project be implemented—i.e., the benefit of doing the project. Community planners must typically generate such estimates as part of the process of gaining approval for or “proving in” new projects. We typically enter the benefit into the model as a fraction of the total loss in a region that will occur should the project not be implemented.

## 5.2.2. Analysis of Example 5–2 model

Similarly to Example 5–1, we again conduct a simulation of consequences to Mombasa, Kenya, due to the three hazards flooding, terrorism, and tsunamis experienced over a 30-year horizon extrapolated from past data. This time, however, we allow inclusion of projects for long-term recovery from and mitigation of flooding (only) disasters. Fig. 3 (middle curve) shows the long-term value of infrastructure over the horizon. Note that in this example, the final infrastructure value falls to only \$217.5M, over 2.5 times the terminal value obtained in Example 5–1.

5.3. Mombasa, Kenya—Multiple hazards with long-term recovery and mitigation analysis

In the final example considered in this paper, we build on the previous two examples by (1) maintaining every detailed, excellent plan for the preparedness, response, and short-term recovery phases of a flooding disaster included in examples 1 and 2, and also by (2) keeping the four flooding mitigation projects from Example 5–2. But now (3), we explicitly plan for two additional hazards, namely, tsunamis and terror, and (4) consider the effects upon the analysis of the incorporation of these two additional factors.

## 5.3.1. Long-term projects to protect against tsunamis and terrorism

In addition to the projects considered in Example 5–2, we now redefine Project 2 to provide an early warning system for both floods and tsunamis, and add consideration of a new project (Project 5) with two phases that is directed at terrorism. With Project 5, we propose an advanced CCTV installation in all regions, but particularly near the airport, refinery, and the power generation system (all in region 4).

Long-term recovery projects are assumed the same as in Example 5–2. Also as in Example 5–2, if only a single-disaster model were used, there would be insufficient funds in the budget to include all projects. But for the model developed in this paper, the (30-year) long-term, multiple instance case may enable the inclusion of additional projects on subsequent disasters.

5.3.1.1. Community values. We now enhance our community values to go beyond just the financial considerations (value of infrastructure and economic output) included in Examples 5–1 and 5–2; we define the three measures chosen for Mombasa to be (see Kebede et al. [24] and the Mombasa district strategic plan for baseline values [38]):

(1) the terminal value of not-lost human life;

(2) infrastructure/economic output resilience; and

(3) the resilience of the number of jobs.

## 5.3.2. Dependencies among projects

Within the five mitigation projects listed above for this example (5– 3), there are two inherent dependencies included. First, if both phases of Project 5 are undertaken concurrently, or phase 2 is started after phase 1 is completed, then additional mitigation benefits occur. Moreover, if projects 1 and 3 are both undertaken – in any order – then when both are completed, additional resource savings are obtained. In the mathematical model, therefore, six “real” mitigation projects must be included plus two additional “dependency” projects for a total of eight mitigation projects; to this is added the long-term recovery project (which covers rebuilding in all four regions), making a total of nine projects.

## 5.3.3. Benefits associated with each project

Table 3 shows the project benefits for Example 5–3 for the four Mombasa regions for the measure infrastructure value and the hazard type flooding. (Due to space limitations, the other benefit values are not displayed.) Note that the benefits tables may be interpreted as follows. Consider the data given (a value of 0.40 as shown in the red rectangle) for the community value “Output (‘000)” for “Project 4” under the Hazard Flooding; this indicates that the infrastructure value loss that will be incurred should a flood occur after Project 4 is completed will be reduced by 40%. This value would be determined by community planners when proposing this project after estimating the mitigative effect of the project and calculating it as a percentage of the loss that would otherwise be incurred.

## 5.3.4. Initial analysis of Example 5–3

Fig. 3, multi-hazard case, shows a plot of the Mombasa core value infrastructure as affected by the string of disasters it is likely to face over the next 30 years. The first thing to note is the improved value (an increase of \$23.5M) in terminal infrastructure (measure 2) due to the inclusion of the additional projects over those of Example 5–2. This is in spite of the fact that this financial consideration has been moved to second priority (behind the terminal value of human lives). Clearly, a multi-hazard analysis saves lives, future dollars, and jobs over the current single-hazard approach. But also note that although Examples 5–2 and 5–3 appear “tied” for the first 7 years of the study, the multihazard scenario required higher investment of resources than did the flooding-only case. Thus, the multi-hazard solution was more costly than the single-hazard. However, overall economic output advantage does show itself for the rest of the study. It is sometimes difficult due to the higher initial cost for communities to justify politically the shorter-term added expense, even though benefits eventually accrue “in perpetuity.” Moreover (not shown), lives lost over the 30 years for the 500 runs ranged from 1 to 11 for the multi-hazard case, versus 3–40 lives lost for the single-hazard planning approach. The community must determine how it wishes to reconcile these data, including the possible loss of up to an additional 29 lives.

Although the multi-hazard analysis developed here is preferred to the previous approaches in many respects, further investigation of DSS output can lead to additional improvements. For example, the

Benefits, by region, for Ex 5–3 for the (resilient) output measure infrastructure value. Mitigative benefits/payoff matrix/floods  
Table 3

<table><tr><td rowspan="2"></td><td colspan="4">Output (‘000)</td></tr><tr><td>Mombasa Island (1)</td><td>Kisauni (2)</td><td>Likoni (3)</td><td>Changamwe (4)</td></tr><tr><td>Project 1</td><td>0.35</td><td>0.00</td><td>0.00</td><td>0.35</td></tr><tr><td>Project 2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Project 3</td><td>0.10</td><td>0.20</td><td>0.20</td><td>0.10</td></tr><tr><td>Project 4</td><td>0.40</td><td>0.50</td><td>0.50</td><td>0.40</td></tr><tr><td>Project 5, phase 1</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Project 5, phase 2</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Project 6</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Project 7</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td></tr></table>

DSS output curves of Fig. 4 show the resilience of infrastructure for each of the four regions of Mombasa. This analysis will most likely be disconcerting to Mombasa planners as region 1, the Tourist Island region, is the least resilient with respect to infrastructure value of the four regions. As this region is critical to the Mombasan (and Kenyan) economy, it is likely that planners may want to either develop another project to protect region 1 from flooding (because that is where the greatest flood loss is occurring) or they may want to divert funds from other regions.

The point to be emphasized is that because the community has undertaken the analysis afforded by this model in the decision support system, it is able a priori to determine not only what projects will help it achieve its goals most economically, but it will also be able to assess whether its projected efforts will be sufficient. If as in this case they are not, then further planning and re-runs of the model may be made to assess the new community posture. Obviously, the iterative process may be continued until a satisficing solution is obtained. For example, it is possible that diverting funds to region 1 as suggested may leave the other regions inequitably funded; this too can then be examined.

5.4. Summary of advantages of multi-hazard proposed model over single hazard solution

The solution to Example 5–3 is superior in the long run to both the solution of Example 5–2, whereby only a single hazard was considered, and to that of Example 5–1, in which case a single hazard was planned for and no long-term mitigation or recovery efforts were taken into account. This conclusion appears obvious, but unfortunately, the current state of affairs is that there is no analytical approach either in practice or academia that suggests how disaster analysis should be conducted by those communities that face more than a single possible disaster. Regrettably, this superiority is not just of academic interest. Human lives and valuable resources are being needlessly wasted, and suffering needlessly incurred.

## 6. Model implications

6.1. Managerial implications of utilizing the proposed long-range planning model

This model encourages planners to involve the community and determine its goals and wishes, not just its resources and potential projects. It does this by explicitly incorporating the community's values (e.g. “protect the environment” or “ensure economic resilience”) within the objective function and the model's constraints. These values may be specified as a result of interactions with community members, or they may be provided by representatives who understand the community's priorities and preferences and who speak on the community's behalf. In both cases, the model provides systematic feedback on the range of probable responses to current planning levels of resources and proposed projects, and it highlights – before the disasters actually occur – likely potential vulnerabilities, losses of life, unnecessary damage, suffering, etc. This enables the communi ty to plan strategically to allocate their resources to deal with significant long-term issues, rather than simply to respond to shorter-term, more immediate concerns.

6.2. Academic implications of utilizing the proposed long-range planning model

No academic work presently exists that supports long-term planning for both mitigation against and recovery from multiple types of disasters. We have shown here how to protect – mitigate – against and recover resiliently from multiple disasters of possibly different types, using an approach designed and embraced by the local

Please cite this article as: J. Chacko, et al., Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.005

J. Chacko et al. / Decision Support Systems xxx (2016) xxx–xxx

![](/api/attachments/ZMCN2HXM/fulltext/images/a830f43e5792e94e3fd4e9e79062b520d068dc48488659a6a9b0205e21043fe4.jpg)  
Fig, 4. Economic development concerns over the 30-vear horizon in Mombasa Kenva, Note that the tourist area (Region 1: Mombasa Island) is least resilient

community. Because of the central role that the community's preferences play in the process, we would expect the resulting plans to be more sustainable over the long term and thus to strengthen the community's ability to manage future disasters on their own [35]. This work thus provides an important context for efforts to build specific decision support systems that can better elicit community input and provide effective feedback, using technologies such as geographic information systems (GIS). For example, detailed GIS models of coastal flooding can be tied to the planning model here to show how to utilize community resources more effectively and to express spatial severity distributions more accurately.

## 7. Conclusions and future work

This research proposed a mathematical model of multi-disaster planning. It addressed a gap in the literature by combining the planning of both mitigation and recovery strategies in a single model. In order to do this, it took, as noted in the literature, a long-term view of planning, and then it followed numerous other suggestions in the literature that community input be incorporated in the model not only in terms of candidate projects addressing mitigation and longterm recovery from disasters, but also with respect to community values. The latter was accomplished through both the model's objective function and its constraints.

The model developed was included within the model base (MBMS) section of a decision support system (recall Fig. 1B), where iterations – as desired – between a community's input choices, its resources, and desired outputs are repetitively examined and refined. The database (DBMS) section of the DSS is also fundamental to the long-term disaster planning component of the task at hand with its stores of hazard severity and frequency data; community data, including core values, potential projects, resources, political units, estimated outputs (goals scoresheets, vulnerabilities, potential damage impacts, black swan analyses (see below)); and previous analyses. The DSS presents its results (in the DGMS) for each community value expressed, both by geographic region, and overall—all across the complete time horizon.

The model developed in this paper in Section 4.2 (Eq. (5) in particular) utilizes expected-value analysis. That is, the random variable demand is modeled through its expectation in Eq. (5). This is the general assumption as a first step in much planning. But there are further questions that a community with its expected-value planning well “in hand” may wish to pursue. For example, a community may wish to pursue either (1) risk analysis and non-expected-value analysis, or so-called (2) “black swan” analysis, or both. As an example of the latter, a city may believe that severe flooding in the downtown region, although not likely to occur, might prevent any future growth in the town. As such, it may want to investigate the black swan possibility of a major flood and decide how to respond, given what is likely to occur, and resources available, in order to obviate this undesired, less likely, devastating consequence. For example, in the 500 independent runs generated in each of this paper's latter two examples, four or five runs in each example resulted in “absolutely devastating” results (e.g., economic output dropping from \~\$350M to \~\$105M) for Mombasa, Kenya. Another very promising avenue of approach is to utilize real options theory in determining planning measures. We believe that the ability for community planners to allow for flexibility in future projects depending on the uncertainty that is actually observed is a powerful and useful addition to multihazard planning—particularly for including the potential effects of black swans and other less likely events.

The research developed in this paper is already being extended in the additional directions mentioned here.

## Acknowledgments

The authors wish to thank three anonymous referees and an associate editor for their most helpful comments in aiding us to more clearly explain the significance and importance of this work. Moreover, the suggestion to explore real options analysis is that of a referee.

## References

[1] M.D. Abkowitz, S. Chatterjee, Regional disaster risk: assessment and mitigation concepts in an all-hazards context, Journal of Homeland Security and Emergency Management 9 (1) (2012).

[2] J.O. Amollo, East Africa rift system, seismic activity, ground deformation and tsunami hazard assessment in Kenya coast, http://www.seis.nagoya-u.ac.jp/kimata/jica actionplan09/Joseph.pdf, 2009.

[3] C.B. Awour, V.A. Orindi, A.O. Adwera, Climate change and coastal cities: the case of Mombasa, Kenya, Environment and Urbanization 20 (1) (2008) 231–242.

[4] B.M. Ayyub, Systems resilience for multihazard environments: definition, metrics, and valuation for decision making, Risk Analysis 34 (2) (2013) 340–355.

[5] B.M. Ayyub, W.L. McGill, M. Kaminskiy, Critical asset and portfolio risk analysis: an all-hazards framework, Risk Analysis 27 (4) (2007) 789–801.

[6] R. Basher, Global early warning systems for natural hazards: systematic and peoplecentred, Philosophical Transactions of the Royal Society A-Mathematical Physical and Engineering Sciences 364 (1845) (2006) 2167–2180.

[7] P.R. Berke, J. Kartez, D. Wenger, Recovery after disaster—achieving sustainable development, mitigation and equity, Disasters 17 (2) (1993) 93–109.

[8] H. Bierman, S. Smidt, The Capital Budgeting Decision, eighth ed. Prentice-Hall, Upper Saddle River, NJ, 1993.

[9] R.A. Brealey, S.C. Meyers, Principles of Corporate Finance, fifth ed. McGraw-Hill, New York, 1996.

[10] M. Bruneau, S.E. Chang, R.T. Eguchi, G.C. Lee, T.D. O'Rourke, A.M. Reinhorn, ... D. Von Winterfeldt, A framework to quantitatively assess and enhance the seismic resilience of communities, Earthquake Spectra 19 (4) (2003) 733–752.

[11] J.R. Canada, W.G. Sullivan, J.A. White, Capital Investment Analysis for Engineering and Management second ed, Prentice-Hall Upper Saddle River NI 1996

[12] J. Canto-Perello, J. Curiel-Esparza, V. Calvo, Criticality and threat analysis on utility tunnels for planning security policies of utilities in urban underground space, Expert Systems with Applications 40 (11) (2013) 4707–4714.

[13] K. Caruson, S.A. MacManus, Gauging disaster vulnerabilities at the local level: divergence and convergence in an “all-hazards” system, Administration & Society 43 (3) (2011) 346–371.

Please cite this article as: J. Chacko, et al., Decision support for long-range, community-based planning to mitigate against and recover from potential multiple disasters, Decision Support Systems (2016), http://dx.doi.org/10.1016/j.dss.2016.04.005

[14] J. Chacko, L.P. Rees, C.W. Zobel, Improving resource allocation for disaster operations management in a multi-hazard context, Proceedings of the 11th International ISCRAM Conference, University Park, PA, 2014 May 2014.

[15] S. Chatterjee, M.D. Abkowitz, A methodology for modeling regional terrorism risk, Risk Analysis 31 (7) (2011) 1133–1140.

[16] L.A. Cox, Improving risk-based decision making for terrorism applications, Risk Analysis 29 (3) (2009) 336–341.

[17] R.L. Dillon, R.M. Liebe, T. Bestafka, Risk-based decision making for terrorism applications Risk Analysis 29 (3) (2009) 321–335

[18] FEMA, National Mitigation Strategy: Partnerships for Building Safer Communities, Federal Emergency Management Agency, Washington DC, 1995.

[19] J.E. Gartner, P.M. Santi, S.H. Cannon, Predicting locations of post-fire debris-flow erosion in the san Gabriel Mountains of southern California, Natural Hazards 77 (2) (2015) 1305–1321.

[20] Government of Kenya Ministry of State for Special Programmes, Office of the President, Draft National Policy for Disaster Management in Kenya, 2009.

[21] K. Hausken, V.M. Bier, J. Zhuang, Defending against terrorism, natural disaster, and all hazards, Game Theoretic Risk Analysis of Security Threats 128 (2009) 65–97.

[22] J. Holguin-Veras, N. Perez, M. Jaller, L.N. Van Wassenhove, F. Aros-Vera, On the appropriate objective function for post-disaster humanitarian logistics models, Journal of Operations Management 31 (5) (2013) 262–280.

[23] M.M.A. Jaller, Resource Allocation Problems during Disasters: Points of Distribution Planning and Material Convergence Control(Doctoral Dissertation) Rensselaer Polytechnic Institute, Troy, NY, 2011.

[24] M.S. Kappes, M. Keiler, K. von Elverfeldt, T. Glade, Challenges of analyzing multihazard risk: a review, Natural Hazards 64 (2) (2012) 1925–1958.

[25] A.S. Kebede, R.J. Nicholls, S. Hanson, M. Mokrech, Impacts of climate change and sealevel rise: a preliminary case study of Mombasa, Kenya, Journal of Coastal Research 28 (1A) (2010) 8–19.

[26] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley Publishing Co., Reading, MA, 1978.

[27] W.D. Kelton, R.P. Sadowski, N.B. Zupick, Simulation with Arena, sixth ed., McGraw Hill Education, New York, NY, 2015.

[28] A. Kretschmer, S. Spinler, V. Wassenhove, N. Luk, A school feeding supply chain framework: critical factors for sustainable program design, Production and Operations Management 23 (6) (2013) 990–1001.

[29] H. Li, G.E. Apostolakis, J. Gifun, W. VanSchalkwyk, S. Leite, D. Barber, Ranking the risks from multiple hazards in a small community, Risk Anal. 29 (3) (2009) 438–456.

[30] D.G. Luenberger, Investment Science, Oxford University Press, New York, 1998

[31] P.J. Maliszewski, M.J. Kuby, M.W. Horner, A comparison of multi-objective spatial dispersion models for managing critical assets in urban areas, Computers, Environment and Urban Systems 36 (4) (2012) 331–341.

[32] W. Marzocchi, A. Garcia-Aristizabal, P. Gasparini, M.L. Mastellone, A. Di Ruocco, Basic principles of multi-risk assessment: a case study in Italy, Natural Hazards 62 (2) (2012) 551–573.

[33] J.H. McCoy, H.L. Lee, Using fairness models to improve equity in health delivery fleet management, Production and Operations Management 23 (6) (2014) 965–977.

[34] D. McLoughlin, A framework for integrated emergency management, Public Administration Review 45 (1985) 165–172.

[35] D.S. Mileti, Disasters by Design: A Reassessment of Natural Hazards in the United States Joseph Henry Press Washington DC 1999

[36] J. Mulwa, F. Kimata, A.D. Nguyen, Seismic Hazard, in: J.F. Shroder, P. Paron, O. Olago, T. Omuto (Eds.). Kenva: a Natural Outlook: Geo-Environmental Resources and Hazards, Elsevier B.V, Oxford, UK 2013, pp. 267–292.

[37] S. Mutimba, S. Mayieko, P. Olum, K. Wanyama, Climate Change Vulnerability and Adaptation Preparedness in Kenya, Heinrich Böll Stiftung, East and Horn of Africa, 2010.

[38] National Coordinating Agency for Population and Development (NCAPD), Mombasa District Strategic Plan 2005-2010 for Implementation of the National Population Policy for Sustainable Development, 2005.

[39] C. Ngunjiri, Tsunami and seismic activities in Kenya, http://www.seis.nagoya-u.ac. jp/kimata/jica/ngunjiri.pdf2007.

[40] L. Pearce, Disaster management and community planning, and public participation: how to achieve sustainable hazard mitigation, Natural Hazards 28 (2-3) (2003) 211–228.

[41] N. Perez, Inventory Allocation Models for Post-Disaster Humanitarian Logistics with Explicit Consideration of Deprivation Costs Rensselaer Polytechnic Institute, 2011

[42] J. Pollet, J. Cummins, All hazards approach for assessing readiness of critical infrastructure, IEEE Conference on Technologies for Homeland Security, IEEE 2009, pp. 366–372.

[43] C. Ragsdale, Spreadsheet Modeling and Decision Analysis: A Practical Introduction to Business Analytics, Cengage Learning, Independence, KY, 2014.

[45] J. Salmerón, A. Apte, Stochastic optimization for natural disaster asset prepositioning, Production and Operations Management 19 (5) (2010) 561–574.

[46] J. Selva, Long-term multi-risk assessment: statistical treatment of interaction among risks, Natural Hazards 67 (2) (2013) 701–722

[47] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall Inc. Englewood Cliffs NI 1982

[48] M.G. Stewart, J. Mueller, Terrorism risks and cost-benefit analysis of aviation security, Risk Analysis 33 (5) (2013) 893–908.

[49] M.G. Stewart, J. Mueller, Terrorism risks for bridges in a multi-hazard environment, International Journal of Protective Structures 5 (3) (2014) 275–290.

[50] J.C. Thomas, Citizen, Customer, Partner: Engaging the Public in Public Management, M.E, Sharpe New York NY 2012

[51] K.J. Tierney, M.K. Lindell, R.W. Perry, Facing the Unexpected: Disaster Preparedness and Response in the United States, Joseph Henry Press, Washington, DC, 2001.

[52] B.R. Tukamuhabwa, M. Stevenson, J. Busby, M. Zorzini, Supply chain resilience: definition, review and theoretical foundations for further study, International Journal of Production Research (2015) 1–32.

[53] UNISDR, Hyogo framework for action 2005–1015: building the resilience of nations and communities to disasters, World Conference on Disaster Reduction, Kobe, Hyogo, Japan, 2005.

[54] UNISDR, Global Assessment Report on Disaster Risk Reduction - Making Development Sustainable: The Future of Disaster Risk Management, United Nations, Geneva, Switzerland, 2015.

[56] W.L. Waugh, Terrorism and the all-hazards model, Journal of Emergency Management 2 (1) (2005) 8–10.

[57] W.L. Waugh, K.J. Tierney, Emergency Management: Principles and Practice for Local Government, ICMA Press, 2007.

[58] H.P. Williams, Model Building in Mathematical Programming, fourth ed. John Wiley & Sons Ltd., West Sussex, England, 1999.

[59] Y.C.E. Yang, P. Ray, C.M. Brown, A.F. Khalil, W.H. Yu, Estimation of flood damage functions for river basin planning: a case study in Bangladesh, Natural Hazards 75 (3) (2015) 2773–2791.

[60] J.H. Zhang, J. Li, Z.P. Liu, Multiple-resource and multiple-depot emergency response problem considering secondary disasters, Expert Systems with Applications 39 (12) (2012) 11066–11071.

[61] J. Zhuang, V.M. Bier, Balancing terrorism and natural disasters-defensive strategy with endogenous attacker effort, Operations Research 55 (5) (2007) 976–991.

[62] C.W. Zobel, Representing perceived tradeoffs in defining disaster resilience, Decision Support Systems 50 (2) (2011) 394–403.

[63] C.W. Zobel, L. Khansa, Quantifying cyberinfrastructure resilience against multi‐event attacks, Decision Sciences 43 (4) (2012) 687–710

[64] C.W. Zobel, L. Khansa, Characterizing multi-event disaster resilience, Computers & Operations Research 42 (2014) 83 94.

Josey Chacko received his PhD in Management Science from the Pamplin College of Business, Virginia Polytechnic Institute and State University, and is now assistant professor at the Richard J. Bolte, Sr., School of Business at Mount St. Mary's University. His current research is in the area of sustainable disaster management, and his work has won awards for best student PhD paper at the Southeastern Regional Decision Sciences Institute annual meeting, and a grant from the Center for Student Engagement and Community Partnerships, Virginia Tech, for promoting civic engagement through research. He is actively involved with the International Association for the Study of Information Systems for Crisis Response and Management (ISCRAM). Prior to his work in the US, he received a B. Tech in Elec. and Comm. Engineering from Moi University in Kenya. Additionally, he has 4 years of work experience as an electrical engineer primarily in an aluminum manufacturing firm, where he served as head of the electrical engineering department.

Cliff T. Ragsdale is a Bank of America Professor of Business Information Technology in the Pamplin College of Business, and the Academic Director of the Pamplin College of Business Center for Business Intelligence and Analytics, both at Virginia Tech. He received his PhD in Management Science and Information Technology from the University of Georgia. He also holds an MBA in Finance and BA in Psychology from the University of Central Florida. Dr. Ragsdale's primary area of research interest centers on the integration of computers mathematics, and artificial intelligence to solve business problems. He is a member of INFORMS, AIS, and DSI. He has published in a variety of journals including Decision Sci ences, Decision Support Systems, Naval Research Logistics, and OMEGA. He also serves on the Advisory Boards of INFORMS Transactions on Education and the International Journal of Information Technology & Decision Making. He is also author of the textbook Spreadsheet Modeling and Decision Analysis, 7ed published by CENGAGE Learning.

Terry R. Rakes is the William and Alix Houchens professor of Business Information Technology at Virginia Tech. He received the PhD in Management Science, MBA, and BSIE from Virginia Tech. His research interests are in analytics and big data analysis, text and data mining, geographic information systems, disaster planning and logistics, information security, and the application of decision support and artificial intelligence methodologies to problems in information systems. He has published in Management Science, Decision Sciences, Decision Support Systems, Annals of Operations Research, OMEGA, European Journal of OR, Operations Research Letters, Information and Management, Journal of Information Science, and others.

Loren Paul Rees is Andersen Professor of Business Information Technology at the Virginia Polytechnic Institute and State University. He received the PhD in Industrial and Systems Engineering and the BEE from the Georgia Institute of Technology, and MSEE from the Polytechnic Institute of Brooklyn. Dr. Rees' current research focuses on disaster management planning and on managerial issues in information technology security. He has published in Decision Support Systems, Naval Research Logistics, IIE Transactions, Decision Sciences, OMEGA, Expert Systems with Applications, Transportation Research, Journal of American Medical Informatics Association, Journal of the Operational Research Society, European Journal of Operational Research, Computers and Operations Research, Communications of the ACM, and others.

Roberta S. Russell is Professor of Business Information Technology at Virginia Polytechnic Institute and State University. She received both her BS and PhD in Management Science at Virginia Tech, and her MBA at Old Dominion University. Her primary areas of research are quality assurance and resource allocation in healthcare operations, humanitarian operations and global supply chains. She is co-author of Operations and Supply Chain Management in its 8th edition with Wiley, and Service Management and Operations in its 2nd edition with Prentice-Hall. Dr. Russell has published in Journal of Operations Management,

Decision Sciences, IIE Transactions, IEEE Transactions, International Journal of Production Research, International Journal of Operations and Production Management, Annals of Operations Research and others. She is an active member of POMS, DSI, ASQ, APICS, and ISCRAM, and i the immediate past president of the APICS Foundation.

Christopher W. Zobel is RB Pamplin Professor of Business Information Technology at the Virginia Polytechnic Institute and State University. He received a PhD in Systems Engineering from the University of Virginia, an MS in Mathematics from the University of North

Carolina at Chapel Hill, and a BA in Mathematics from Colgate University. His primary research interests are in developing analytic techniques to improve disaster operations management and environmental decision making. Dr. Zobel has published articles in Decision Support Systems, Decision Sciences, and the European Journal of Operational Research, among others, and he is an active member of the Decision Sciences Institute (DSI), the Institute for Operations Research and the Management Sciences (INFORMS), and the International Association for the Study of Information Systems for Crisis Response and Management (ISCRAM).
