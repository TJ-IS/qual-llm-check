---
otero_id: 27457
otero_key: "JQHE3KMY"
title: "A Representational Scheme for Analyzing Information Technology and Organizational Dependency1"
authors: "John Tillquist; John Leslie King; Carson Woo"
year: "2002"
journal: "MIS Quarterly"
doi: "10.2307/4132322"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Representational Scheme for Analyzing Information Technology and Organizational Dependency

Author(s): John Tillquist, John Leslie King and Carson Woo

Source: MIS Quarterly, Vol. 26, No. 2 (Jun., 2002), pp. 91-118

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/4132322

Accessed: 20-06-2016 02:13 UTC

## REFERENCES

Linked references are available on JSTOR for this article:

http://www.jstor.org/stable/4132322?seq=1&cid=pdf-reference#references\_tab\_contents
You may need to log in to JSTOR to access the linked references.

# A REPRESENTATIONAL SCHEME FOR ANALYZING INFORMATION TECHNOLOGY AND ORGANIZATIONAL DEPENDENCY $^{1}$

By: John Tillquist
Anderson Graduate School of Management
University of California, Riverside
Riverside, CA 92521
U.S.A.
john.tillquist@ucr.edu

John Leslie King
University of Michigan
300 West Hall
550 East University Avenue
Ann Arbor, MI 48109-1092
U.S.A.
jlking@umich.edu

Carson Woo
Faculty of Commerce and Business Administration
University of British Columbia
Vancouver, British Columbia V6T 1Z2
CANADA
Carson.Woo@ubc.ca

## Abstract

This paper presents a new representation methodology, dependency network diagrams (DNDs), which enables the essential elements governing organizational relations to be captured, communicated, and evaluated under changing conditions. By depicting important features of organizational relations, information systems can be designed explicitly for control and coordination of organizational activities. The rules and construction algorithm for DNDs are presented and applied to a case study of a Canadian automobile insurance company. Analysis of the case reveals how IT was used to create strategic change within the Canadian vehicle repair market.

Keywords: Management information systems, organizational systems, competitive use of IS, IS planning methodologies, IS strategic planning, organizational change, organizational design

ISRL Categories: AF0701, AF10, AI0102, AK0102, DA08, DD01, DD04, EF01, EF04, FC15

## Introduction

The design of organizational information technologies has relied heavily on data flow diagrams, process models, entity-relationship diagrams, and state transition diagrams. These modeling strategies are adaptations of engineering models of material flow, component design, factory process, and discrete state machines of production. They are organized around the achievement of an optimal state of process efficiency and technological precision. This target state of optimality is theoretically reachable, and we can build systems this way. The question remains, however, whether the systems we build will work the way we want them to in context, where the dynamics of organizational and institutional life conflict with the assumptions of traditional modeling strategies (Orlikowski and Barley 2001). The evidence from studies of system implementation failure suggests that additional strategies are needed.

Models of technological functionality and optimization perform well when the required tasks of system engineering can be executed without regard to confusion or uncertainty arising from organizational context. In such cases, the organization can be “black boxed” and treated as a stable set of conditions that systems can be built to “fit.” In practice, however, organizations cannot be relied upon to conform to the expectations of black boxes. The design of systems that will work effectively in complex organizational contexts requires accommodating for the variance and uncertainty found in actual organizational life.

Unfortunately, there is a price to be paid for relaxing design boundaries arbitrarily. Without carefully circumscribed constraints, system development projects quickly fall into conflicts between users and designers over requirements and specifications, manifested in excessive numbers of change orders as the users discover problems with the emerging design or in poor implementation and use patterns when the project is completed.

The challenge for system builders working in complex organizational application domains is to open the black box enough to accommodate realistic conditions for development, but not so much that the Pandora's box of unbounded expectations and confusion over requirements is unleashed. Several modeling strategies have been suggested for accomplishing this, including socio-technical codevelopment models, such as soft systems methodologies (Checkland 1985), SCOTS (Bijker et al. 1987), and user-centric design (Norman 1990). All of these are constructed around achieving organizational fit, usability, and augmentation.

This paper furthers the effort to develop concrete strategies for system development for complex organizational application domains by using the notion of dependency to isolate a particular facet of organizational dynamics and structure. Dependencies form the basis for interaction through the exchange relation, and as such provide specific structure to the problem of organizational interaction and process coordination. Similar inquiries in management theory provide a starting point for our dependency analysis. Pfeffer and Salancik (1978) introduced resource dependency theory to explain power and influence relations in the organizational context. We use resource dependence theory to construct a conceptual modeling tool called the dependency network diagram for the analysis and design of organizational information systems.

The rationale for the modeling tool and its operation are described first. We then demonstrate the utility of the model in a complex situation involving automobile insurance in a highly institutional environment. We do not suggest that the dependency network diagram approach is a substitute for existing modeling strategies. Rather, we see it as complementary, designed to handle situations such as highly institutionalized production processes in which the existing strategies do not work very well.

## Organizational Information Systems and Resource Dependence Theory

Organizational information systems can have significant implications for organizations. Information technologies change control and coordination activities, shape the form of organizational coupling, and influence strategic coordination (DeSanctis and Poole 1994; Ives and Jarvenpaa 1991). Internal to the organization, structural and procedural arrangements change to make exchange relations between units more efficient. New work practices, new responsibilities, and shifts to the organization's structure are introduced as new IT systems are implemented (Fulk and DeSanctis 1995). Externally, relationships with trade partners are impacted. Organizationally based IT couples work processes and increases access to and availability of shared resources and information, while coincidentally formalizing the exchange contract (Clemons and Row 1992). IT can be (and often, for economic reasons, is) selectively deployed with some trade partners and not others, leading to differentiation in strategy, competition, and cooperation among players within the market.

Organizations need the capability to diagnose changes relevant to IT. Preferably this would include identifying changes to activities, resources, and systems of control and coordination precipitating from organizational IT initiatives.

A common nexus to change is the coordination of activities and dependencies. All activities that involve more than one actor require some way of dividing activities among the different actors and some way of managing the interdependencies among the different activities (Lawrence and Lorsch 1967; March and Simon 1958; Tansey and Hyman 1994). Ideally, organizations are structured by grouping activities to minimize the difficulties of managing these inter-group dependencies. Malone and Crowston (1994) synthesize this ideal in a theory of coordination in which various combinations of the coordination mechanisms, together with different kinds of groupings, give rise to the different organizational structures including functional hierarchies, product hierarchies, and matrix organizations. Coordination is the management of dependencies, and organizational change the adaptation to changing dependencies. Resource dependence theory (Pfeffer and Salancik 1978) provides a theoretical foundation for understanding the dependencies within organizational systems that enable coordination and change.

Resource dependence theory is a theory of rational organizational adaptation to exogenous changes in the environment (Pfeffer and Salancik 1978; Ulrich and Barney 1984). The theory proposes that actors lacking in essential resources will seek to establish relationships with (i.e., be dependent upon) others in order to obtain needed resources. A resource is anything perceived as valuable by an actor, such as information, material, capital, or access to markets, and dependency is a state in which one actor relies on the actions of another to achieve particular outcomes (Emerson 1962; Frooman 1999; Pfeffer 1992). Organizations will seek to formalize agreements that govern the exchange of resources with others to ensure continuing access to needed resources.

Competitive and cooperative dependencies, created as organizations contend for scarce resources, affect internal arrangements and external relations to ensure organizational survivability (DiMaggio and Powell 1991; Hannan and Carroll 1992; Hawley 1950; Parsons 1956a, 1956b). Organizations will differentiate their structures in order to stabilize external dependency relationships and to manage efficiently resource exchanges (Pfeffer and Salancik 1978). Organizations in dependency relations will also seek to establish a stable consensus about the terms and conditions that govern the relationship (Van de Ven and Walker 1984). Patterns of exchange relations among organizations follow paths of dependency (Provan et al. 1980). The particular patterning of interdependent exchange relations creates markets among organizations (Van de Ven and Walker 1984).

Dependency also creates asymmetrical relations of influence, thus establishing power relationships among the participants (Ball-Rokeach and DeFleur 1982; Barrow 1998; Dastmalchian 1986; Frooman 1999; Pfeffer 1992; Pfeffer and Salancik 1978; Provan et al. 1980; Tansey and Hyman 1994). Dependency can be used to instill needs, interests, and motives in the dependent actor that can be used to obtain favored payoffs or to create more favorable conditions in relations (Dastmalchian 1986; Frooman 1999; Pfeffer 1992; Provan et al. 1980; Willer et al 1997).

Possession, allocation, and use of resources within these exchanges are regulated by governance controls—sets of formal and informal decision rules covering the activities of the actors engaging in the exchange relation (Pfeffer 1992; Pfeffer and Leong 1977). These controls specify the nature of the constraints and penalties and draw boundaries around the discretion, autonomy, and limits of expression and behavior between dependent roles (Pfeffer and Salancik 1978). These exist as direct supervision, standardization, and administrative controls (Durkheim, 1949; Weber 1947), as well as the examination of outcomes (Ouchi and Maguire 1974), mutual adjustment, and contractual regulation (Fromm 1981; Galbraith 1973; March and Simon 1958; Mintzberg 1979). They appear as administrative regulations, prioritization standards, legal obligations, product or service standards, explicit sequencing and tracking processes, and market control structures (Malone and Crowston 1994).

Resource dependency theory does not provide adequate explanations for all social circumstances. Some organizations have transient dependencies operating as market forces and are less subject to negotiated relations. When patterns of dependency arise from specific supply and demand conditions with no residual compliance obligations, transaction cost theory might be a more powerful explanator (Donaldson 1995). However, many organizations embody more than the optimization of transactions, and resource dependency theory is valuable in discerning and describing managerial strategies for organizational change and survival (Scott 1998). Resource dependency theory thus is consonant with ecological and institutional theories of organizations where organizations are seen as persistent structures of order under constant reinterpretation and negotiation, interacting with an indeterminate environment of turbulence and a multitude of competing interests.

Resource dependency theory explicitly acknowledges an active role for managers in evaluating, negotiating, and sustaining organizational relations (Aldrich 1999). Managers can manipulate dependency relationships and thus have an active hand in controlling and changing the organizational network. This gives rise to a final and important feature of resource dependency theory: a lack of presumption about causality. Existing dependencies can shape organizational behaviors and goals, and alteration of dependencies can cause changes in behaviors and goals. However, the opposite is also true: organizations can change their behaviors and goals and thereby change their dependencies. Thus, organizational transformation can be the result of changing dependencies, and it can also be the cause of changing dependencies.

There are several forms of organizational dependency. Organizational units may operate independently, but be ultimately dependent upon the pooled efforts of all. Units may be sequentially dependent, where the output of one directly supports another as an input resource. And units may present a reciprocal dependency, in which case both mutually depend upon the other for needed resources. These differing forms of dependency suggest differing forms of coordination. Standardization works well for pooled dependencies, coordination by plan fits instances of sequential dependencies, while reciprocal dependencies are best managed through a process of mutual adjustment (Thompson 1967). These differing needs equate to different IT designs, depending upon the nature of the dependencies among the constituent units.

Information technologies cluster around exchange relations, providing process support, coordination, and control mechanisms (Pfeffer and Salancik 1978). IT coordinates strategic and process exchange in support of maintaining and making efficient the acquisition of resources critical to the viability of the organization. At the exchange relation, IT provides stakeholders with information about the exposures to risk facing the organization, such as material supply problems, conformance with externally imposed regulation, and access to markets. This makes the exchange relation a critical component in organizational IT design.

Resource dependency theory can serve to inform the design and refinement of organizational systems through an understanding of organizational relationships. Information systems can be designed explicitly for control and coordination of organizational activities by capturing and conveying features of dependency relations. IT designs can then be crafted to efficiently manage the resource exchange interface by improving process coupling, information exchange, and strategic coordination. Analyzing dependency relations also enables organizations to diagnose the impact of IT implementations. In this paper, we use the dependency network diagram as a diagnostic tool to assess the structural and market changes introduced by a new IT implementation.

## The Dependency Network Diagram

The dependency network diagram (DND) is a model of management action and IT design. DNDs incorporate both economic (resource exchange) and political (influence) explication to describe arrangements within exchange relations. Using resource dependency theory, DND modeling emphasizes depictions of the context in which organizations operate, the activities needed to acquire critical resources, and the roles involved in the exchange relation. We operationalize the essential constructs of resource dependency theory by constructing the following definitions:

\- An activity is the means or procedure for the provisioning of material or informational resources necessary to achieve a goal.

\- A resource is anything perceived as valuable by a role, such as information, material, capital, or access to markets.

\- A role is the encapsulation of a set of activities and goals. Roles represent individuals, work groups, organizations, or industrial segments sharing common activities and goals.

• A goal is a desirable or suitable objective.

\- A dependency is the need of one role to achieve a goal through the action of another role.

\- A governance control is a prescription for acceptable actions to fulfill a dependency.

The dependency network diagram arranges these constructs diagrammatically to depict the constituent elements and structure of exchange coordination. We demonstrate the application of the DND model by use of a case in the Canadian insured vehicle repair industry.

## Applying the Data Dependency Diagram to Organizational Systems: The Canadian Insured Vehicle Repair Industry

Government-appointed corporations manage motor vehicle insurance in most Canadian provinces. We followed one such corporation, pseudonymously referred to here as InsCo, through their development of an automated collision repair estimation system. InsCo is a provincial corporation established by the government to provide universal auto insurance to motorists. All motorists are required to buy a basic package of InsCo vehicle insurance that includes accident benefits, third-party legal liability protection, and underinsured motorist protection. InsCo administers insurance claims, reimburses vehicle repair shops, regulates insurance benefits, and polices for fraud.

A longitudinal study of InsCo's automated collision repair estimation system began in 1997, during the initial conceptualization stages of the IT project, and continued through the winter of 2000, after the deployment of the automated estimating system in two provincial regions. The Automated Estimating project replaces manual insurance vehicle damage estimates with standardized computer-based estimates of time, parts, and labor. The project consists of the development and deployment of computers to vehicle repair shops, an upgrade to the InsCo internal fraud detection systems, and minor upgrades to the telecommunication infrastructure.

Initial interviews with InsCo executives identified the key problem areas of interest to InsCo. These data and data from subsequent interviews and on-site observation were used to define the activities, goals, roles, and controls that constituted the vehicle damage estimation and repair process. DND diagrams constructed from these data defined the boundaries of interest around the project. As the project proceeded, interviews were used to track the design and development of the Automated Estimating project. Comparisons of the pre- and post-implementation DND diagrams revealed changes brought about by the new system.

## The Target Process: Estimating Repairs ■

The insurance damage estimation process was the target for InsCo's computerization effort. InsCo's objectives in automating the vehicle damage estimating process related to processes and controls shared with vehicle repair shops, the government, and claimants. The new automated damage estimation system was designed around these dependency relations.

In the existing vehicle damage estimating process, automobile accident claimants visited an InsCo insurance claims center for an estimate. Service clerks attended to customer questions and led them through the estimation process. InsCo damage estimators manually inspected the damaged vehicle and produced a written work order using the industry-standard Mitchell Parts and Labor Estimating Guide (generally known as the Mitchell Manual; Mitchell 2001). The work order communicated the damages and prescribed repairs and authorized the vehicle repair shop to conduct the repairs.

Claimants then sought out a vehicle repair shop of their choice for the repair work. Repair shops were responsible for the completion of the repair work. The repair shop completed the described repairs and submitted proof of completion, along with the work order, to InsCo. Vehicle repair shops abided by InsCo stipulations for the submission and authentication of the completed repair work related to the work order to receive payment.

Relations among the participants in insured vehicle repair involved under this manual system were antagonistic. Damage claim payments often took several weeks, frustrating the repair shops with large accounts receivables. Depending upon the severity of the damages, disputes over the responsibility for damages by claimants and delays in administrative handling, the payment for services would sometimes be received months after repair work was completed. The three-way process with InsCo and the vehicle repair shop inconvenienced claimants, who in effect had to coordinate with both InsCo and the repair shops. Hidden damages or underestimated repairs frequently forced claimants to return to InsCo for a new estimation, increasing the inconvenience of getting repairs completed.

InsCo was frustrated with the process as well. InsCo spent significant effort administering and supporting insurance reimbursements with vehicle repair shops in the years prior to implementing the automated damage estimation system. A “universal access” government regulation, mandating claimants be free to choose any vehicle repair shop, forced InsCo to work with numerous smaller vehicle repair shops. With little business sophistication and minimal computerized operations, these smaller operations limited InsCo administration to a cumbersome and costly set of manual processes.

InsCo's role in the insured damage repair process also made InsCo a visible target for claimant complaints. InsCo preferred claimants' interactions be as transparent as possible: "Our strategic objective is to make InsCo invisible to our customer" (InsCo Executive Vice-President, personal communication 1997). When things did go wrong, however, InsCo was a favored target for blame by claimants, the media, and lawyers. Claimant complaints escalated from the InsCo in-house service to the provincial government's Ombudsman's Office. These complaints were taken seriously, at times resulting in penalties, fines, and sanctions on InsCo operations.

It was in this context that the initial design for the automated vehicle damage estimation system began to take shape. Interviews with the I/S Vice-President identified specific questions raised for the design of the automated estimating system:

\- Could IT be used to make labor-intensive claims processing more efficient? What controls would be necessary to manage the new processes, and, if outsourced, how would compliance be assured?

\- Could systems be developed to streamline administrative interfaces with claimants and vehicle repair shops? The manual dispensation needed for smaller, minimally computerized vehicle repair shops precluded many automation opportunities. How could InsCo open avenues for automated cost efficiencies without contradicting the government mandate for universal access?

\- Could IT be used to improve claimant services without increasing costs or compounding the administrative responsibilities of claimants and vehicle repair shops? Could claims management systems be deployed that decreased claimant complaints and reduced the government sanctions that resulted from complaints? Could these technical systems be arranged such that the mutual animosity with repair shops would also be reduced?

## Dependency Network Diagrams

## Representation Syntax

The problem facing InsCo was friction and inefficiencies in the vehicle damage estimation and repair process. The roles of the participants of this process—the insurance trust administrator (InsCo), the provincial government, vehicle repair shops, and customer claimants—therefore constitute the focus of the analysis. Several key dependencies exist between these roles:

\- The claimant depends upon the insurance trust administrator to provide a work order and claim resolution, upon the vehicle repair shop for vehicle repair, and upon the provincial government for resolving complaints

\- The vehicle repair shop depends upon the claimant to get the work order and upon the insurance trust administrator for claim payment

\- The insurance trust administrator depends upon the provincial government to provide strategic direction in insurance claims management and upon the vehicle repair shop to contain costs by adhering to the work order

This network of dependencies is depicted in Figure 1.

## Representation Construction

Dependency network diagrams are constructed according to four rules: the scope rule, the actions rule, the goals rule, and the dependency rule. Taken together, these rules specify the constructs, focus, and level of analysis bounding the coordination problem being modeled.

Rule 1: The Scope Rule. The scope of the model bounds the relevant activities, goals, roles, and dependencies within the model. The scope rule assures that only aspects directly relevant to the purpose of the model are modeled.

![](/api/attachments/JQHE3KMY/fulltext/images/68daba57201ee9fc6a9e6d439596c913b4027928364adf378ffdad519365c0c2.jpg)  
Figure 1. DND Model of the Pre-automated Estimating Environment

Resource dependency theory states that activities are purposeful in achieving some goal. Given the subset of relevant goals for a given role i, $\{G_{i,1}, G_{i,2}, ..., G_{i,m}\} \subseteq G_i$ , the activities of role i to be modeled ( $A_i$ ) are defined in terms of the given subset of goals (see Figure 2.A).

This assures that only the activities directly linked to a relevant goal set are included in the model.

Dependencies arise when the activities a role can perform are insufficient to achieve the goal of interest, and the role must rely on another to provide the needed resource (Froom 1999; Pfeffer and Salancik 1987). In terms of DND depictions, dependency D of role $_{i}$ on role $_{j}$ (D $_{i,j}$ ) can be specified in terms of the activities role $_{i}$ requires from role $_{j}$ {A $_{j,1}$ , A $_{j,2}$ , ..., A $_{j,n}$ } to accomplish the goals of role $_{i}$ (see Figure 2.B).

This formulation assures only dependencies linked to a goal of relevance are included in the model. The combination of relevant goals and activities (equation A) and dependencies (equation B) defines a parsimonious boundary for the model, including only goals, activities, and dependencies of explicit relevance.

Rule 2: The Activities Rule. The activities rule specifies granularity in modeling activities. This is necessary in order to concentrate on the essential units of activities for the purpose of analyzing dependency and governance. The rule specifies when a composite of activities is to be modeled as a single activity and when discrete activities are modeled separately.

<table><tr><td>(A)  $A_{i} = \{A_{i,1}, A_{i,2}, ..., A_{i,n}\}$  in role i where each activity  $A_{i,j}$  is necessary to achieve a goal in the subset of relevant role i goals,  $\{G_{i,1}, G_{i,2}, ..., G_{i,m}\} \subseteq G_{i}$ <img src="/api/attachments/JQHE3KMY/fulltext/images/876684397c92806c340a24d396be7805ea0583b9e4d5de3795d120dfd0682d27.jpg"/></td></tr><tr><td>(B)  $D_{i,j} = \text{activities } \{A_{j,1}, A_{j,2}, ..., A_{j,n}\} \text{ from role j necessary to achieve a subset of goals } \{G_{i,1}, G_{i,2}, ..., G_{i,m}\} \text{ in role i}$ <img src="/api/attachments/JQHE3KMY/fulltext/images/f4058a5e6e70f07fd4f253ebda709797e6a94278d3e87050e4f7713d74d8fdbf.jpg"/></td></tr></table>

Figure 2. The Scope Rule

Activities $A_{i,n}$ and $A_{i,n+1}$ for accomplishing goal $G_{i,m}$ in role i should be combined, unless:

(1) distinct roles depend upon activities $A_{i,n}$ and $A_{i,n+1}$ as separate dependencies, or

(2) the sequence of executing the activities is $\{A_{i,n}, A_{j,m}, A_{i,n+1}\}$ where $A_{i}$ and $A_{i+1}$ are in role R but the intermediary activity $A_{j,m}$ is performed by another role j

Rule 3: The Goals Rule. The goals rule specifies when goals are combined or depicted separately. The relationship between a role's goal and the supportive activities determines whether or not a goal should be uniquely identified or combined with other similar goals. Goals $G_{i,n}$ and $G_{i,n+1}$ in role i should be combined in their representation unless the subsets of activities used to achieve $G_{i,n}$ and $G_{i,n+1}$ are composed of different activities.

Rule 4: The Dependency Rule. The dependency rule defines uniqueness of dependency representation. There should exist only one dependency from one role to another unless the dependencies are unrelated.

Given two dependencies $D_{1}$ and $D_{2}$ between roles i and j, where the accomplishment of $G_{i,m}$ in role i depends on $A_{j,n}$ in role j through $D_{1}$ , and $G_{i,m+1}$ depends on $A_{j,n+1}$ through $D_{2}$ (see Figure 3), then the two dependencies should be modeled separately if $A_{j,n} \neq A_{j,n+1}$ and $G_{i,m} \neq G_{i,m+1}$ ; otherwise, $D_{1}$ and $D_{2}$ should be combined into a single dependency.

![](/api/attachments/JQHE3KMY/fulltext/images/0bd54b9ce6309e9a5315f63990e3c0af0d259378697b62fbd72c916f2d2d8431.jpg)  
Figure 3. The Dependency Rule

## Construction Algorithm for the Dependency Network Diagram

The algorithm for constructing the DND is a recursive formulation that traces the roles, goals, and activities to identify and arrange the relevant dependencies:

1. Identify an initial event that triggers the need to accomplish a goal

2. Identify and depict the role that needs to accomplish the goal arising from this initial event

3. Identify and depict all the activities needed to accomplish the goal using the activities rule

4. For each activity not performed internally by the role, construct a dependency to another role using the dependency rule

5. For the newly identified role:

a. depict the activity required by the dependent role

b. identify the goal(s) that compels the role to perform the dependent activity using the goal rule

c. repeat steps 3 through 5 for each goal identified for the newly created role

6. Repeat steps 1 through 5 for any additional initial events

This process assures completeness and representational validity of the model by limiting the representations to only those of relevance (Rule #1). $^{2}$

## Dependency Tracing

To represent the dependencies among organizational roles in the InsCo case, we trace the cascading dependencies that precipitate from an initial event in a pseudo-English form. The initial event is the trigger upon which the representation exists. For vehicle damage estimation and repair, this trigger event of interest is the vehicle accident, since all the insurance and repair activities are generated as a result of this event. In generic form, an initial event is represented as:

A problem/opportunity creates the role's goal to goal. The initiator must [conditionally] activity {, [conditionally] activity ...} [to fulfill the initiating role's goal] to goal {, goal, ...}.

For the InsCo case, the initial motor vehicle accident invokes the claimant's goal to restore vehicle function.

Initial Event: A vehicle accident creates the claimant's goal to restore vehicle function. The claimant must file a claim and submit the vehicle for inspection, provide a work order, submit the vehicle for repair and conditionally resubmit the vehicle for re-inspection to restore vehicle function.

Several activities are invoked as a result of this event, some accomplished by the claimant, others performed by the insurance trust administrator, the provincial government, and the vehicle repair shop in accordance with their own goals. Dependencies arise when a role is unable to satisfy its own goal and must rely upon other roles to perform activities that provide the needed resources (such as providing information, delivering materials, granting access, or contributing labor). Beginning with the vehicle accident, the process follows these dependencies as they appear. Chains of cascading dependencies stemming from the initial event are represented:

The dependent\_role depends upon the supplier\_role for dependency [to fulfill the dependent\_role's goal] to goal. The supplier\_role must [conditionally] activity {, [conditionally] activity, ...} [to fulfill the supplier\_role's goal] to goal {, goal, ...}. The applicable criterion for dependency is the governance control.

Following a vehicle crash incident, the claimant must get a work order from InsCo before a vehicle repair shop can perform the repairs. The claimant's need for a work order creates a dependency between the claimant and the insurance trust administrator (the role of InsCo) for claim resolution, as the claimant needs a resource (the work order) from another role (the insurance trust administrator). The insurance trust administrator provides the work order (the dependent activity) in concert with the internal goal of resolving insurance claims. In achieving this goal, the insurance trust administrator must also execute government policies regarding cost containment. Regulating the dependency is the insurance policy, the governance control that stipulates the terms and conditions in providing the work order. This dependency appears:

① Claim resolution (Claimant→Insurance trust administrator)
The claimant depends upon the insurance trust administrator to estimate damages and generate work order to restore vehicle function. The insurance trust administrator must estimate damages, generate a work order, process the claim and manage customer service to resolve claim and to enact government cost containment policy. The applicable criterion for estimate damages and generate work order is the insurance policy.

Note that the numbers associated with the dependency descriptions correlate to the numbered dependency arrows depicted in Figure 1. This numbering does not imply a process sequence; satisfaction of dependencies across DND networks may occur in parallel, in sequence, or in no particular order.

A second dependency is brought into play as the provincial government depends upon the insurance trust administrator to contain insurance costs. Financial justification for operations ensures the insurance trust administrator will comply with the cost policies set by the provincial government. This is a standing dependency that exists before, during, and after any particular vehicle collision claim and is invoked as part of the claim process.

② Cost Containment (Provincial government→Insurance trust administrator) The provincial government depends upon the insurance trust administrator for cost containment to protect public good. The insurance trust administrator must assure compliance to enact government cost containment policy. The applicable criterion for cost containment is the financial justification of operations.

If the claimant has difficulties in restoring vehicle function, the claimant needs the provincial government to adjudicate the complaint. Governing the complaint resolution dependency is the Ombudsman Act, which creates an authority to investigate the decision, acts, and procedures of InsCo and other governmental authorities.

③ Complaint resolution (Claimant→Provincial government)
The claimant depends upon the provincial government for complaint resolution to restore vehicle function. The provincial government must adjudicate complaints to protect public good. The applicable criterion for complaint resolution is the Ombudsman Act.

The claimant also needs the vehicle repair shop to repair the vehicle, while the vehicle repair shop repairs the vehicle (action) to generate revenue (goal).

④ Vehicle repair (Claimant→Vehicle repair shop)
The claimant depends upon the vehicle repair shop for vehicle repair to restore vehicle function. The vehicle repair shop must repair vehicle to generate revenue. The applicable criterion for vehicle repair is the repair shop service agreement.

The vehicle repair shop requires the work order in order to be paid for work performed. This creates a dependency on the claimant, governed by the InsCo's universal access mandate allowing claimants to give the work order to any repair shop of their choice.

⑤ Work order (Vehicle repair shop→Claimant)
The vehicle repair shop depends upon the claimant for the work order to generate revenue. The claimant must provide a work order to restore vehicle function. The applicable criterion for work order is the universal access mandate.

The repair shop depends upon the insurance trust administrator to issue payment.

⑥ Claims payment (Vehicle repair shop → Insurance trust administrator)
The vehicle repair shop depends upon the insurance trust administrator for claims payment to generate revenue. The insurance trust administrator must process payment to resolve claim. The applicable criterion for claims payment is the completed work order.

The work order expressly limits the costs of repairs, imposing a dependency of the insurance trust administrator onto the vehicle repair shop to abide by the work order estimate. Invoking the insurance trust administrator's goal to provide compensation also invokes the twin goal of balancing costs and revenues:

⑦ Cost containment (Insurance trust administrator→Vehicle repair shop)
The insurance trust administrator depends upon the vehicle repair shop for managing repair costs to enact government cost containment policy. The vehicle repair shop must manage repair costs to generate revenue. The applicable criterion for cost containment is the work order.

Table 1 summarizes the links between dependencies, goals, and activities expressed in the pseudo-English form above.

<table><tr><td colspan="5">Table 1. Links between Dependencies, Activities, and Goals in Pre-automated Estimating</td></tr><tr><td>Dependency</td><td>Dependent Activity</td><td>Internal Activity</td><td>Source Goal</td><td>Destination Goal</td></tr><tr><td rowspan="2">1 Claim resolution</td><td>A1. Process claim and manage customer service</td><td>A1. File claim and submit vehicle for inspection</td><td>G1. Restore vehicle function</td><td>G2. Resolve claim</td></tr><tr><td>A2. Estimate damages and generate work order</td><td>A4. Resubmit vehicle for re-inspection</td><td></td><td>G1. Enact government cost containment policy</td></tr><tr><td rowspan="2">2 Cost containment</td><td>A2. Estimate damages and generate work order</td><td>A1. Set public insurance policy</td><td>G1. Protect public good</td><td>G1. Enact government cost containment policy</td></tr><tr><td>A4. Assure compliance</td><td></td><td></td><td></td></tr><tr><td>3 Complaint resolution</td><td>A2. Adjudicate complaints</td><td></td><td>G1. Restore vehicle function</td><td>G1. Protect public good</td></tr><tr><td>4 Vehicle repair</td><td>A1. Repair vehicle</td><td>A2. Submit vehicle for repair</td><td>G1. Restore vehicle function</td><td>G1. Generate revenue</td></tr><tr><td>5 Work order</td><td>A3. Provide work order</td><td></td><td>G1. Generate revenue</td><td>G1. Restore vehicle function</td></tr><tr><td>6 Claims payment</td><td>A3. Process payment</td><td>A2. Submit for payment</td><td>G1. Generate revenue</td><td>G2. Resolve claim</td></tr><tr><td>7 Cost containment</td><td>A3. Manage repair costs</td><td>A4. Assure compliance</td><td>G1. Enact government cost containment policy</td><td>G1. Generate revenue</td></tr></table>

## Evaluating for Internal Consistency in the Dependency Network Diagram

Once the process of tracing the dependencies is completed and the diagram constructed, the model is compared against the four rules to assure completeness and parsimony. For the InsCo case, the scope of the DND model for insurance damage estimation and repair is defined by the relevant activities, goals, roles, and dependencies within the model, following the chain of cascading dependencies arising from the initial vehicle event. The four roles depicted (insurance trust administrator, claimant, vehicle repair shop, and government) are the only roles that are triggered in response to the initial vehicle damage repair claim, and hence are the only roles directly relevant to the purpose of the model (rule #1, the scope rule).

Many other dependencies exist between these roles but are not invoked by the initial vehicle accident event. The provincial government, for example, depends upon vehicle repair shops for taxation revenue; however, no demand is made for a “tax” activity in tracing the cascading dependencies from the initial vehicle accident, and hence this dependency is not relevant to the model. The same process abstracts away the dependencies of the claimant on InsCo in issuing the insurance policy, of the government on claimants to vote officials into office for providing tax revenues, and other dependencies not directly related to vehicle damage estimation and repair. The process of tracing dependencies through the construction algorithm assures parsimonious depictions within the model.

Applying the activities rule (rule #2), we find that file claim, provide work order, and resubmit vehicle for re-inspection are distinct model activities. The file claim and provide work order activities form the basis for different dependencies (on the insurance trust administrator and the vehicle repair shop, respectively) and are hence modeled separately. The file claim and resubmit vehicle for re-inspection both depend on the insurance trust administrator, and would be modeled as a single activity except that the activities are separated by an intermediate activity (submit vehicle for repair) that depends on a different role. All other activities are checked in the same manner.

We also check the model to assure goals are represented at the correct level of aggregation (rule #3, the goals rule). For the insurance trust administrator, we check that each goal is accomplished by a different activity (generate work order is necessary to provide compensation; assure compliance is needed to enact government cost containment policy). Each goal in the model is evaluated using this process.

Finally, the dependency rule (rule #4) defines uniqueness of dependency representation. Since there are no multiple dependencies from one role to another in InsCo's pre-implementation DND model, the rule does not apply to this diagram.

## The Introduction of Automated Estimating

Implementation of InsCo's new automated repair estimating system was launched in the fall of 1999. A relatively small project of CDN\$10 million, the Automated Estimating project proposed to shift collision estimation responsibilities from InsCo to the vehicle repair shop.

To replace the administratively dense InsCo repair estimation process, InsCo deployed a pen-based, clipboard-sized computer to estimate repairs. The system selected was one that several U.S. insurance organizations use internally to automate in-house insurance estimation. Instead of deploying the system internally, however, InsCo designed the automated process to allow vehicle repair shop mechanics to create their own claim estimates.

Contained within the automated estimation system is a repository of work procedures, estimated labor rates, and detailed expenses scripted through a GUI user interface. In using the system, vehicle repair shop technicians describe a claimant's collision damages to the system through a combination of pointing and keyboard entry. The system calculates the labor and reimbursable costs from an internal parts and labor database of industry-based standards. A wireless modem connects the clipboard computer to InsCo's wide area network, uploading estimates and downloading payment authorizations along with collision data updates to the existing claims application repository.

To be eligible to use automated estimating, vehicle repair shops must conform to new InsCo certification requirements. These requirements stipulate the repair facilities that need to be in place, specific requirements for customer service, and a comprehensive set of business practices.

## New Work Process

Under the new system, customer service improves as vehicle repair shops provide one-stop damage estimating and automotive repair services for accident claimants. Customer claimants take their vehicle directly to a certified vehicle repair shop, where shop mechanics assess the damage and enter repair information into the pen-based computer. Claimants do not see or contact InsCo insurance representatives directly, and normally do not deal with out-of-pocket payments or reimbursements. Compensation for the repair work is disbursed directly to the vehicle repair shop.

Throughout the process, InsCo uses several procedures and computerized systems to curtail fraud. A new fraud detection system compares damage and repair information with police reports, hospital and ambulance reports, and historical claims and policy information. Statistical analysis of claim submissions from vehicle repair shops track individual shop and industry performance indicators, identifying unusual trends or suspicious activities in vehicle repair shop practices. InsCo also conducts premise inspections and known-damage inspections to assure operational compliance and to deter falsified claims.

## Dependency Network Diagram for InsCo

The dependency network diagram for the post-automated estimating environment depicted in Figure 4. The links between dependencies, activities, and goals are summarized in Table 2.

We again use the psuedo-English form to describe the constructs and relationships depicted in Figure 4.

Initial Event: A vehicle accident creates the claimant's goal to restore vehicle function. The claimant must submit the vehicle for repair to restore vehicle function.

④ Repair service (Claimant→Vehicle repair shop)
The claimant depends upon the vehicle repair shop for vehicle repair to restore vehicle function. The vehicle repair shop must generate claim, estimate damages, repair vehicle and manage customer service to generate revenue. The applicable criterion for vehicle repair is the InsCo service agreement.

The vehicle repair shop handles customer complaints in the post-implementation setting. There are two forms of complaints. The first are complaints with the service and repairs performed by the repair shop itself; the claimant continues to depend upon the repair shop for resolution of these complaints. The second are complaints about InsCo practices and policies used by the repair shops; in the post-implementation setting, the claimant depends upon the repair shop to work through the InsCo process to resolve claimant complaints. This dependency is modeled:

![](/api/attachments/JQHE3KMY/fulltext/images/e573b9797a9f090de968fa54e7aef5c58abeda7f3b136a14783c9592de87ca89.jpg)  
Figure 4. DND Model of the Pre-automated Estimating Environment

## ③ Complaint resolution (Claimant→Vehicle repair shop)

The claimant depends upon the vehicle repair shop for complaint resolution to restore vehicle function. The vehicle repair shop must manage customer service to retain accreditation. The applicable criterion for complaint resolution is the repair shop service agreement.

As with the pre-implementation setting, vehicle repair shops rely upon the insurance trust administrator for claims payment. Control over cost containment shifts from the manual work order to the embedded standards for labor and parts contained within the automated estimating database. In addition, a new dependency of the insurance trust administrator on the repair shop to provide customer service is balanced with a new dependency of the vehicle repair shop to gain pre-authorized approval for repairs.

⑤ Repair authorization (Vehicle repair shop→Insurance trust administrator) The vehicle repair shop depends upon the insurance trust administrator for repair authorization to generate revenue. The insurance trust administrator must accredit repair shop to enact government cost and service policies. The applicable criterion for repair authorization is InsCo certification.

<table><tr><td colspan="5">Table 2. Links between Dependencies, Activities, and Goals in Post-automated Estimating</td></tr><tr><td>Dependency</td><td>Dependent Activity</td><td>Internal Activity</td><td>Source Goal</td><td>Destination Goal</td></tr><tr><td>2 Public service</td><td>A1. Accredit repair shopA3. Assure compliance</td><td>A1. Set public insurance policy</td><td>G1. Protect public good</td><td>G1. Enact government cost containment policyG3. Enact government service policy</td></tr><tr><td>3 Complaint resolution</td><td>A4. Manage customer service</td><td></td><td>G1. Restore vehicle function</td><td>G1. Retain accreditation</td></tr><tr><td>4 Repair service</td><td>A1. Generate claimA2. Estimate damagesA3. Repair vehicleA4. Manage customer service</td><td>A1. Submit vehicle for repair</td><td>G1. Restore vehicle function</td><td>G1. Generate revenue</td></tr><tr><td>5 Repair authorization</td><td>A1. Accredit repair shop</td><td>A1. Generate claimA2. Estimate damagesA6. Manage repair costs</td><td>G1. Generate revenue</td><td>G1. Enact government cost containment policy</td></tr><tr><td>6 Claims payment</td><td>A2. Process claimA3. Assure compliance</td><td>A5. Submit for payment</td><td>G1. Generate revenue</td><td>G1. Enact government cost containment policyG2. Resolve claim</td></tr><tr><td>7 Service to the public</td><td>A4. Manage customer service</td><td>A1. Accredit repair shop</td><td>G2. Retain InsCo accreditation</td><td>G3. Enact government service policy</td></tr></table>

⑥ Claims payment (Vehicle repair shop→Insurance trust administrator) The vehicle repair shop depends upon the insurance trust administrator for claims payment to generate revenue. The insurance trust administrator must process claim to resolve claim and assure compliance to enact government cost policies. The applicable criterion for claims payment is the standardized parts and labor database.

⑦ Service to the public (Insurance trust administrator→Vehicle repair shop) The insurance trust administrator depends upon the vehicle repair shop for service to the public to enact government service policy. The vehicle repair shop must manage customer service to retain InsCo accreditation. The applicable criteria for service to the public are the InsCo service standards.

The provincial government's dependency on the insurance trust administrator shifts to emphasize public service, not just cost containment. The expanded dependency is modeled:

② Public service (Provincial government→Insurance trust administrator) The provincial government depends upon the insurance trust administrator for public service to protect public good. The insurance trust administrator must accredit repair shops and assure compliance to enact government cost and service policies. The applicable criterion for public service is the insurance trust administrator's justification as a public service entity.

DND analysis of InsCo's design shows changes in process, governance, and strategic alignment, and how inequities in exchange relations prompted dependent players to accept the new automated system. The analysis also reveals how critical boundary-defining decisions were made and how consensus about the new, codified business processes was legitimated.

## Changes to the Dependency Network

Table 3 summarizes the changes to the dependencies in InsCo's post-implementation environment. Changes to the governance controls in the InsCo case are summarized in Table 4. Changes in activities are detailed in Table 5. Changes to goals are presented in Table 6.

Three significant changes in the dependency network appear as the new automated estimating process is introduced. InsCo is disintermediated from the claimant process, the vehicle repair shop substitutes for the Ombudsman's office in complaint resolution, and responsibilities are outsourced to the vehicle repair shop.

## Disintermediation of InsCo

For illustration purposes, we label each role in the automated estimation DNDs as claimant, ITA (insurance trust administrator) and VRS (vehicle repair shop) (Figures 1 and 4). In the pre-automated estimating process (Figure 1), the relationship of the claimant's goal to repair the vehicle depends upon the insurance trust administrator to authorize repair work by performing damage estimation ( $A_{ITA,2}$ ) and customer service, ( $A_{ITA,1}$ ), and the vehicle repair shop for repairing the vehicle ( $A_{VRS,1}$ ). This relationship is expressed as the union of the activity sets necessary to effect repairs ( $G_{Claimant,1}$ ):

$$
G _ {\text { Claimant }, 1} \rightarrow \left\{A _ {I T A, 1}, A _ {I T A, 2} \right\} \cup \left\{A _ {V R S, 1} \right\}
$$

With the advent of automated estimating, the vehicle repair shop assumes responsibility for customer service activities ( $A_{ITA,1}$ in Figure 1) and damage estimation ( $A_{ITA,2}$ ). The goal of the claimant (restore vehicle function) is now satisfied by consolidation of the requisite activities into the vehicle repair shop role. InsCo is disintermediated (Figure 5) from the claimant process. In the post-implementation setting, the claimant uniquely depends upon the vehicle repair shop to repair the vehicle:

![](/api/attachments/JQHE3KMY/fulltext/images/1cfa19ca8035bc800a5b9db028ab507966841d2f6fce2ba275a4d72f92ace50f.jpg)  
Figure 5. Disintermediation

Table 3. Changes to Dependencies in Post-implementation Environment

<table><tr><td>Dependency</td><td>Changes to Dependencies in Post-implementation Environment</td></tr><tr><td>1 Claim resolution</td><td>Dependency eliminated</td></tr><tr><td>2 Cost containment</td><td>Changes to 2 Public service</td></tr><tr><td>3 Complaint resolution</td><td>Shifted dependency onto repair shop</td></tr><tr><td>5 Work order</td><td>Replaced by 5 Repair authorization</td></tr><tr><td>5 Repair authorization</td><td>New dependency; replaces 5 Work order</td></tr><tr><td>7 Cost containment</td><td>Replaced by 7 Service to the public</td></tr><tr><td>7 Service to the public</td><td>New dependency; replaces 7 Cost containment</td></tr></table>

Table 4. Changes to Government Controls in the Post-implementation Environment

<table><tr><td>Dependency</td><td>Changes to Governance Controls in Post-implementation Environment</td></tr><tr><td>2 Public service</td><td>Governance control changed from “financial justification” to “public service justification”</td></tr><tr><td>4 Vehicle repair/Repair service</td><td>Governance control shifted from “repair shop service agreement” to “InsCo service agreement”</td></tr><tr><td>5 Work order/repair authorization</td><td>Governance control shifted from “universal access mandate” to “InsCo Certification”</td></tr><tr><td>6 Claims payment</td><td>Governance control shifted from “completed work order” to “standardized parts and labor database”</td></tr><tr><td>7 Cost containment/Service to the public</td><td>Governance control shifted from “work order” to “InsCo service standards”</td></tr><tr><td colspan="2">Table 5. Changes to the Activities in the Post-implementation Environment</td></tr><tr><td>Role</td><td>Changes to Actionable Setting in Post-implementation Environment</td></tr><tr><td>Claimant</td><td>a. Eliminate “file claim and submit vehicle for inspection” for claimant “file claim” activity assumed by vehicle repair shop“submit vehicle for inspection” eliminatedb. Eliminate “provide work order”</td></tr><tr><td>Vehicle repair shop</td><td>a. Add “generate claim”b. Add “estimate damages”c. Add “manage customer service”</td></tr><tr><td>Insurance Trust Administrator</td><td>a. Eliminate “manage customer service” from “process claim”b. Eliminate “estimate damages and generate work order”c. Add “Accredit repair shop”</td></tr><tr><td>Provincial Government</td><td>a. Eliminate “adjudicate complaints”</td></tr></table>

<table><tr><td colspan="2">Table 6. Changes to Goals in the Post-implementation Environment</td></tr><tr><td>Role</td><td>Changes to Goals in Post-implementation Environment</td></tr><tr><td>Insurance Trust Administrator</td><td>Added goal to “enact government service policy”</td></tr><tr><td>Vehicle Repair Shops</td><td>New goal “Retain accreditation” added</td></tr></table>

$$
\mathrm{G} _ {\text { Claimant }, 1} \rightarrow \{\mathrm{A} _ {\text { VRS }, 3} \}
$$

The change is due to computerized processing replacing the manual creation and couriering of the work order. This removes the direct dependency of the claimant on InsCo, consolidating claimant dependency singularly onto the vehicle repair shop. Eliminating the need for a work order removes InsCo from the intermediary role. The DND shifts from a triangular arrangement of claimant-InsCo-repair shop to a linear arrangement, with InsCo "behind" the vehicle repair shop and out of the direct processing with the claimant (Figure 4).

Removing the claimants' dependency on InsCo (dependency ① in Figure 1) reduces labor and administrative requirements for InsCo. Organizational resources used to manage the claimant relations are freed up as the work order dependency is removed, reducing overall costs by eliminating coordination requirements (Malone and Crowston 1994). Dropping the work order from the collision repair process also removes the requirement of pre-authorization for claimant customers, allowing them to bring their business directly to the participating vehicle repair shop. This adds convenience for the claimant, and makes accredited repair shops more attractive. At the same time, the new dependency coupling with vehicle repair shops opens opportunities for standardization and computerization with the relatively fewer, and more sophisticated, repair shops. In real terms, this means lessened overall process and coordination costs, fewer delays from coordination losses, and fewer occasions for friction among the participants.

![](/api/attachments/JQHE3KMY/fulltext/images/18c9f8c07610db8d015eb42641afd3b1bffba9c2e951813e51013fd59637e33e.jpg)  
Figure 6. Substitution

## Substitution of Repair Shops for Complaint Resolution

Prior to automated estimating, InsCo was responsible for direct customer service and claimants depended upon the Ombudsman's Office for service remedies.

$$
G _ {\text { Claimant }, 1} \rightarrow \{A _ {\text { government }, 2} \}
$$

Vehicle repair shops assume responsibility for customer service under the new automated estimating process. Claimants now interact with vehicle repair shops nearly exclusively for service (dependency ③ in Figure 2).

$$
\mathrm{G} _ {\text { Claimant }, 1} \rightarrow \{\mathrm{A} _ {\text { VRS }, 4} \}
$$

Customer service by the vehicle repair shop substitutes (Figure 6) for the government's Ombudsman's office as InsCo drops from public view. Under the new setting, the claimant depends upon the vehicle repair shop for resolving service problems. InsCo practices and policies are temporally and conceptually distanced from the repair experience, reducing the visibility of InsCo claims processes and limiting access for claimants to information about claims resolution. Claimants must be determined and reasonably informed to pursue complaints about InsCo through the government under the new arrangement; presumably, most would focus complaints directly at the repair shop. As a result, customer complaints about InsCo claims administration are expected to be reduced under the new system.

## Outsourcing of Damage Estimation and Customer Service

With automated estimating, responsibilities for generating the insurance claim, estimating damages, and managing customer service are outsourced by InsCo to the vehicle repair shop as part of the system design.

![](/api/attachments/JQHE3KMY/fulltext/images/6b47729524d30de0c4740af2808f3b98685c1533e5759f894d9def47179db058.jpg)

Figure 7. Outsourcing

$$
\left\{\mathrm{G} _ {\text {ITA,1}}, \mathrm{G} _ {\text {ITA,2}} \right\}\rightarrow \left\{\mathrm{A} _ {\text {ITA,1}}, \mathrm{A} _ {\text {ITA,2}} \right\}
$$

becomes

$$
\left\{\mathsf {G} _ {\text {ITA,1}}, \mathsf {G} _ {\text {ITA,2}} \right\}\rightarrow \left\{\mathsf {A} _ {\text {VRS,2}}, \mathsf {A} _ {\text {VRS,4}} \right\}
$$

The dependency created by InsCo with the vehicle repair shop as internal InsCo activities are outsourced (Figure 7) is balanced with a new dependency of vehicle repair shops on InsCo ( $^{⑤}$ Repair authorization in Figure 4) that replaces the work order in the post-implementation setting. This formalizes damage estimation into a repair planning process using a prescribed, set sequence of steps and controlling parameters. InsCo codified work standards replace manual negotiation in estimate reconciliation. Vehicle repair shops comply with the InsCo-defined rules and constraints of the automated estimation system. Thus while claims costs are reduced for InsCo, control is retained through the new dependency created with the vehicle repair shops.

The automated estimating system is associated with the dependency relationships between InsCo and the vehicle repair shop. The first dependency here, that of InsCo on the vehicle repair shops, is a pooled dependency, where both InsCo and the repair shop operate individually but mutually benefit from improved customer service. The other dependencies, those of the vehicle repair shops on InsCo, are sequential, in that the output of the repair shops serves as an input to InsCo's claims processing. Thompson (1967) suggests standardization coupled with shared planning as the best strategies for these forms of dependency.

Automated estimating was intended to standardize the InsCo/repair shop interface, and the outsourcing of damage estimation was instantiated as a work planning and authorization process. This confirms the design configuration of the automated estimating system as appropriate to the situation.

## Impacts of the Automated Estimating System

## Costs

Evidence suggests the Automated Estimating program is having an effect. Lower claim costs and higher investment income led to a \$96 million surplus for InsCo in 1999 (Canadian Insurance News 2000; InsCo Annual Report 1999). Much of the surplus came from reductions in claims processing. While the total number of policies continued to increase to 2.58 million from 2.55 million in 1998, total claims costs decreased to \$1.8 billion in 1999 from \$1.9 billion the year prior (InsCo Annual Report 1999). Most importantly, costs per claim were down 14% to \$2,021 in 1999 from \$2,352 in 1995 (InsCo Annual Report 1999).

These cost savings, and the role of Automated Estimating, are highlighted in the 1999 InsCo annual report:

The decline in claims costs resulted from a combination of three factors. There was an increase in the number of claims, however, the average cost of each claim was lower....The reduction in average claims cost can be partly attributed to improvements in our claims handling practices. These include improvements in our injury management practices, the Enhanced Claims Handling program, and Automated Estimating. (InsCo 1999 Annual Report)

## Consolidation of the Vehicle Repair Market

Early indicators suggest the vehicle repair market in InsCo's Canadian province is beginning a "significant consolidation" as predicted with the advent of Automated Estimating (InsCo Vice-President, Claims, November, 2000). Of the 1,100 businesses claiming to do InsCo collision repair, approximately 400 are InsCo accredited; these, however, account for roughly $80\%$ of the collision repair dollars paid out by InsCo (ARA 2000).

Labor statistics show a decline in the collision repair sector. The motor vehicle repair services labor sector is losing jobs while overall employment is rising elsewhere in the province. Employment in motor vehicle retail services is down 24% to 6,900 positions in 1999 from a high of 28,500 in 1994, the lowest level of sector employment since 1988 (Ministry of Industry and Corporate Relations 2000). This compares to an overall increase in the total provincial workforce (1,910,000 in November 1999 from 1,820,000 in January 1999) in the same period, during which total unemployment dropped to 8.0% from 9.5% (Ministry of Industry and Corporate Relations 1999b), the lowest unemployment rate since September 1981 (Ministry of Industry and Corporate Relations 1999a).

## Complaints

The number of complaints about InsCo investigated by the government ombudsman's office dropped to 62 in 1999, down from 106 in 1995 and 71 in 1996, while the total number of complaints about all government services increased to 478 in 1999 from 430 (1995) and 431 (1996) (Office of the Ombudsman Annual Reports 1995-1999). In the May 2000 Legislative Assembly, the Minister of Labour overseeing InsCo reported:

When I was first elected in 1986, [InsCo] was not only one of the major problems my constituency had to deal with, it was the worst. It was the top of the list—worse than welfare and [the Worker Compensation Board], and that's a horrible commentary. In the last two or three years it's become about number six or seven in terms of the regular complaints.... All I know is that there has been, from my perspective, a demonstrable shift—okay?—in rates of approval. (Minister of Labour 1999)

## Summary: InsCo

The case for automated estimating was initially justified as a cost containment automation project before the InsCo leaders. Discussion among the Board of Directors did not recognize the significance of the implementation; that is, there was no discussion about the restructuring of the repair shop market, the realignment of complaints away from InsCo, and the new opportunities for standardization and automation between InsCo and the upper-tier vehicle repair shops.

The outcome of the project was, in foresight, difficult to assess. Using DND representations, the nature of the changes being undertaken becomes quite intuitive. DND representations tie the changes and adjustments to the reformation of organizational relationships, adding explanation and reasoning to the impacts of IT implementation.

The DND representation shows how information technologies provided the leverage to implement policies, work processes, and certification requirements without violating the government's universal access mandate. Controls built into the technology allowed InsCo to decentralize damage estimation authority while coincidentally increasing control over the functioning and characteristics of vehicle repair shops. The new automated estimating system provided a simple technological solution to the issues facing InsCo before the project was proposed:

\- Could IT be used to make labor-intensive claims processing more efficient? What controls would be necessary to manage the new processes, and, if outsourced, how would compliance be assured?

The overall process becomes more efficient as fewer dependencies translated to lessened interface coordination costs within the claims estimation and repair network. Changing the regulation of claims benefits from administratively dense intervention to a computationally based fraud detection system increases InsCo efficiency and effectiveness in detecting fraudulent claims, while at the same time increasing the granularity of control InsCo holds over vehicle repair shop operations.

\- Could systems be developed to streamline administrative interfaces with claimants and vehicle repair shops? The manual dispensation needed for smaller, minimally computerized vehicle repair shops precluded many automation opportunities. How could InsCo open avenues for automated cost efficiencies without contradicting the government mandate for universal access?

The new automated estimating system opens new opportunities for administrative coordination with certified vehicle repair shops. In doing so, InsCo does not necessarily violate the universal access mandate. Participating repair shops are certified based on their ability to provide “satisfactory” service to claimants, a reasonable criterion for the socially conscious provincial government. Certified participants gain market differentiation as a matter of their own efforts in becoming certified and providing a minimum acceptable level of service—claimants retain the right to select a repair service provider of their choice.

In effect, however, this arrangement aligns the strategies of InsCo and a pool of certified vehicle repair shops, leaving the low-end vehicle repair shops to receive the least benefit. Low-end operations are effectively displaced from the market by customer-convenient certified repair shops. As smaller repair shops disappear, InsCo sheds expensive administrative overhead associated with smaller manual operations and tightens control over the remaining pool.

\- Could IT be used to improve claimant services without increasing costs or compounding the administrative responsibilities of claimants and vehicle repair shops? Could claims management systems be deployed that decreased claimant complaints and reduced the government sanctions that resulted from complaints? Could these technical systems be arranged such that the mutual animosity with repair shops would also be reduced?

Eliminating InsCo's direct involvement with claimants adds convenience for the claimant by simplifying the claimant role and limits InsCo's visibility for complaints. The new computerized work authorization also facilitates repair shop interactions with InsCo, providing greater autonomy and streamlined administrative coordination for the participating repair shops. The previously uneasy relationship between InsCo and vehicle repair shops changes into a shared interest scheme, displacing mutual distrust with a cooperative strategy against the smaller repair shops.

## Conclusions

Models of technological functionality and optimization such as data flow diagrams, process diagrams, and state transition diagrams presume organizations are instrumentally rational; they describe what resources are to be used, and how and when they are to be used, in such a way as to "get the job done." Organizational technologies designed in this way can be made technically correct but may be organizationally inefficient. This is because organizations must order their actions in situations of interdependence and in the face of uncertainty as to where and how that interdependence exists. Understanding the structure of dependencies enables coordinated action of the interdependent elements. Efficiency then arises from the ability to plan, to establish relevant rules, and to provide communication channels among the constituents (Thompson 1967).

In this paper, we have introduced a representational scheme depicting the nature and dynamics of organizational dependency. The dependency network diagram representation model enables technological and organizational designers to directly address organizational interfaces, uncovering opportunities to solve systemic problems through the realignment of dependencies in networked organizations.

We have constructed an approach that allows analysts to narrow focus on the essential dependencies, influences, and changes that structure organizational relationships. This systematic bounding of the organizational IT problem enables system builders to engage complex organizational application domains, systematically opening the black box of organizational and political requirements within carefully circumscribed constraints. This constrained focus on dependencies isolates a particular aspect of organizational dynamics and structure, a focus that highlights the implications of IT on coordination, coupling, and strategic arrangements.

The construction algorithm we define provides a starting point for analysts and precisely limits the scope of the each analysis. The rules we define insure consistent representations across diagrams, facilitating the comparison of dependencies, influences, and changes. Taken together, the DND model formalizes a tightly bounded view into organizations.

Resource dependency theory suggests that changing the dependencies experienced by the organization impacts its behaviors and goals. We have used DNDs in this way to retrospectively diagnose organizational changes at InsCo. This form of analysis facilitates learning from change, and as such melds well with the literature on organizational learning. Resource dependency theory also proposes a parallel causality, in which changes to organizational activities and goals rearrange the dependencies upon others. This suggests that DNDs may have use helping design IT to facilitate changes in organizations that have dependency causes or ramifications.

DND models facilitate planning possible alternative organizational arrangements that reduce dependency coordination costs, maintain access to critical resources, and alter balances of power and control across resource exchanges. DND analyses allow designers to foresee shifts in power relationships and to make adjustments if necessary. DND models also enable designers to balance losses and gains of critical resources in various network arrangements while shaping economic, political, and competitive changes to some advantage. DNDs may, therefore, be of value to designers in representing and examining shifting relations involved in alternative future scenarios.

DNDs may best be used in both senses, diagnostically and prescriptively, as a kind of ongoing background technique to keep abreast of the correspondence between IT design and the organization's dependency/process relationships. This would be a scanning/surveillance application consonant with the strategic view of keeping organizational options open while moving decisively in key opportunities or threats.

DNDs should be of particular value in circumstances where institutional forces are strong. While no organization is completely self-sufficient, highly institutionalized organizations have greater dependencies on others in coordinating material, economic, and political exchange. For these organizations, governance controls not only pressure for effective performance but also consist of social and political pressures to conform to convention and rule (Scott 1998). These historically based complexes of rationalized rules and beliefs are especially important for maintaining the orderliness, predictability, and formalization of relations. DNDs explicitly model these governance controls, making these representations uniquely fitted in describing institutionalized relations.

Dependency representations can be useful for academic research. DNDs depict how structured tasks, goals, and controls interact in complex systems of technological and organizational actors. Roles can be analyzed in terms of their centrality in the dependency network, revealing patterns of influence between and among roles. DNDs enable researchers to study the impact of IT on process coordination and organizational structuring.

Prior research suggests that dependency modeling may be useful in understanding the coordination processes of decision-making and groups (DeSanctis and Poole 1994; Zigurs and Kozar 1994), of organizations and their constituent units (Fulk and DeSanctis 1995), of complex software systems (Malone and Crowston 1994), and in the economic analysis of organizational coordination (Clemons and Row 1992; Hitt 1999). Significant research opportunities exist in applying the DND techniques described here in studying differing levels of organizational analysis. Similar opportunities exist in studies of coordination among organizational units and in integrating complex technological and organizational systems.

For practitioners, DND representations uncover opportunities to solve systemic problems through the realignment of dependencies in response to changing environments. The explicit representation of dependency networks enables organizational systems to be represented and communicated, compared with alternative arrangements, and evaluated in terms of performance and flexibility to changing conditions. The representations of dependencies offered by dependency network diagrams can lead to improved organizational effectiveness by explicit focus on the definition and control of coordination and cooperative role interdependencies.

In either use, DNDs offer insights into the structuring of organizational relations and a means by which to analyze the impact of computerization in changing settings.

## Acknowledgments

This research was funded in part by a grant from the Canadian Social Sciences and Humanities Research Council (SSRC), a grant from the University of California Academic Senate Omnibus Research Fund, and a grant from the Natural Sciences and Engineering Research Council of Canada (NSERC).

## References

Aldrich, H. Organizations Evolving, Sage Publications, Thousand Oaks, CA, 1999.

ARA. Personal Correspondance, Automotive Retailers Association, 2000.

Ball-Rokeach, S. J., and DeFleur, M. L. "A Dependency Model of Mass-edia Effects," Communications Research (3), 1976, pp. 3-21.

Barrow, C. W. "State Theory and the Dependency Principle: An Institutionalist Critique of the Business Climate Concept," Journal of Economic Issues (32:1), March 1998, pp. 107-144.

Bijker, W., Hughes, T., and Pinch, T. (eds.). The Social Construction of Technological Systems, MIT Press, Cambridge, MA, 1987.

Canadian InsurancE-News. http://www.insurance-canada.ca/newevent\_frame.htm, May 2000.

Checkland, P. “Achieving ‘Desirable and Feasible’ Change: An Application of Soft Systems Methodology,” Journal of the Operational Research Society (36:9), September 1985, pp. 821-831

Clemons, E. K., and Row, M. C. “Information Technology and Industrial Cooperation: The Changing Economics of Coordination and Ownership,” Journal of Management Information Systems (9:2), Fall 1992, pp. 9-28.

Dastmalchian, A. “Organizational Resource Dependencies and Goal Orientation,” Journal of Business Research (14:5), October 1986, pp. 387-402.

DeSanctis, G., and Poole, M. S. “Capturing the Complexity in Advanced Technology Use: Adaptive Structuration Theory,” Organization Science (5:2), 1994, pp. 121-147.

DiMaggio, P., and Powell, W. W. “Introduction,” in The New Institutionalism in Organizational Analysis, W. W. Powell and P. DiMaggio (eds.), University of Chicago Press, Chicago, 1991.

Donaldson, L. American Anti-Management Theories of Organization: A Critique of Paradigm Proliferation, Cambridge University Press, Cambridge, England, 1995.

Durkheim, E. The Division of Labor in Society, Free Press, Glencoe, IL, 1949 (originally published in 1893).

Emerson, R. M. "Power-Dependence Relations," American Sociological Review (27), 1962, pp. 31-41.

Fromm, G. (ed.). Studies in Public Regulation, The MIT Press, Cambridge, MA, 1981.

Frooman, J. "Stakeholder Influence Strategies," Academy of Management Review, (24:2), April 1999, pp. 191-205.

Fulk, J., and DeSanctis, G. "Electronic Communication and Changing Organizational Forms," Organization Science, (6:4), July/August 1995, pp. 337-349.

Galbraith, J. R. Designing Complex Organizations, Addison-Wesley, Reading, MA, 1973.

Hannan, M. T., and Carroll, G. R. Dynamics of Organizational Populations: Density, Legitimation, and Competition, Oxford University Press, New York, 1992.

Hawley, A. Human Ecology, Roland, New York, 1950.

Hitt, L. M. “Information Technology and Firm Boundaries: Evidence from Panel Data,” Information Systems Research (10:2), June 1999, pp. 134-149.

Ives, B., and Jarvenpaa, S. L. “Applications of Global Information Technology: Key Issues for Management,” MIS Quarterly (15:1), March 1991, pp. 33-49.

Lawrence, P., and Lorsch, J. Organization and Environment, Division of Research, Harvard Business School, Boston, MA, 1967.

Malone, T. W., Crowston, K. "The Interdisciplinary Study of Coordination," ACM Computing Surveys (26:1), March 1994, pp. 87-119.

March, J. G., and Simon, H. A. Organizations, John Wiley & Sons, New York, 1958.

Minister of Labour. 1998/99 British Columbia Legislative Session: 3rd Session, 36th Parliament, Official Report of Debates of the Legislative Assembly (15:9), Thursday, May 20, 1999.

Ministry of Industry and Corporate Relations. "Employment by Industry for British Columbia," http://www.bcstats.gov.bc.ca/data/dd/handout/naicsann.pdf, 2000.

Ministry of Industry and Corporate Relations. "Labour Force Statistics," October, http://www.bcstats.gov.bc.ca/data/lss/lfs/lfs9910.pdf, 1999a.

Ministry of Industry and Corporate Relations. "Measuring Changes in BC Labour Market Conditions," http://www.bcstats.gov.bc.ca/data/lss/lfs/lfs9911.pdf, November 1999b.

Mitchell Parts and Labor Estimating Guide. http://www.mitchellrepair.com, 2000.

Mintzberg, H. The Structuring of Organizations, Prentice-Hall, Englewood Cliffs, NJ, 1979.

Norman, D. A. The Design of Everyday Things, Doubleday, New York, 1990.

Orlikowski, W. J., and Barley, S. R. “Technology and institutions: What Can Research on Information Technology and Research on Organizations Learn from Each Other?,” MIS Quarterly (25:2), June 2001, pp. 145-165.

Ouchi, W., and Maguire, M. "Organizational Control: Two Functions," Administrative Science Quarterly (20), 1974, pp. 559-569.

Parsons, T. “Suggestions for a Sociological Approach to the Theory of Organizations, Part I,” Administrative Science Quarterly (1:1), 1956, pp. 63-85.

Parsons, T. “Suggestions for a Sociological Approach to the Theory of Organizations, Part II,” Administrative Science Quarterly (1:2), 1956b, pp. 225-239.

Pfeffer, J. Managing with Power: Politics and Influence in Organizations, Harvard University Press, Boston, 1992.

Pfeffer, J., and Leong, A. "Resource Allocations in United Funds: Examination of Power and Dependence," Social Forces (55), 1977, pp. 775-790.

Pfeffer, J., and Salancik, G. The External Control of Organizations: A Resource Dependence Perspective, Harper and Row, New York, 1978.

Provan, K. G., Beyer, J. M., and Kruytbosch, C. "Environmental Linkages and Power in Resource-Dependence Relations between Organizations," Administrative Science Quarterly (25:2), June 1980, pp. 200-225.

Scott, R. Organizations: Rational, Natural, and Open Systems ( $4^{th}$ edition), Prentice-Hall, Englewood Cliffs, NJ, 1998.

Tansey, R., and Hyman, M. R. “Dependency Theory and the Effects of Advertising by Foreign-Based Multinational Corporations in Latin America,” Journal of Advertising (23:1), March 1994, pp. 27-42.

Thompson, J. Organizations in Action, McGraw-Hill, San Francisco, 1967.

Ulrich, D., and Barney, J. "Perspectives on Organizations: Resource Dependence, Efficiency and Population," Academy of Management Review (9:3), 1984, pp. 471-81.

Van de Ven, A. H., and Walker, G. "The Dynamics of Interorganizational Coordination," Administrative Science Quarterly (29:4), December 1984, pp. 598-621.

Weber, M. The Theory of Social and Economic Organization, Oxford University Press, New York, 1947.

Willer, D., Lovaglia, M. J., and Markovsky, B. "Power and Influence: A Theoretical Bridge," Social Forces (76), 1997, pp. 571-603.

Zigurs, I., and Kozar, K “An Exploratory Study of Roles in Computer-Supported Groups,” MIS Quarterly (18:3), September 1994, pp. 277-297.

## About the Authors

John Tillquist is an assistant professor at the University of California, Riverside, specializing in the areas of IT-enabled organizational change and the organizational impacts of information technologies. John spent 10 years as senior engineer and corporate staff manager for GTE Data Services, Ameritech, and US West prior to earning his Ph.D. from the University of California, Irvine.

John Leslie King is Dean and Professor in the School of Information at the University of Michigan. His research concerns the coevolution of institutional and technological artifacts. He was Professor of Information and Computer Science and Management at the University of California, Irvine from 1980-2000.

Carson Woo is an associate professor of Management Information Systems in the University of British Columbia's Faculty of Commerce and Business Administration (Vancouver, Canada). His research interests include methods and tools to support the evolution of information systems, development of multi-agent systems, and their application in business.
