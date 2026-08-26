---
otero_id: 20871
otero_key: "SVPZ7ZDA"
title: "An object-oriented organizational model to support dynamic role-based access control in electronic commerce"
authors: "Edward C Cheng"
year: "2000"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00083-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An object-oriented organizational model to support dynamic role-based access control in electronic commerce<sup>q</sup>

Edward C. Cheng

OCT Research Laboratory, Birkbeck College, UniÕersity of London, Three Waters Park, MS 215, San Mateo, CA 94403, USA

## Abstract

Role-based access control RBAC provides flexibility to security management over the traditional approach of usingŽ . user and group identifiers. In RBAC, access privileges are given to roles rather than to individual users. Users acquire the corresponding permissions when playing different roles. Roles can be defined simply as a label, but such an approach lacks the support to allow users to automatically change roles under different contexts; using static method also adds administrative overheads in role assignment. In electronic commerce E-Commerce and other cooperative computingŽ . environments, access to shared resources has to be controlled in the context of the entire business process; it is therefore necessary to model dynamic roles as a function of resource attributes and contextual information.

In this paper, an object-oriented organizational model, Organization Modeling and Management OMM , is presented asŽ . an underlying model to support dynamic role definition and role resolution in E-Commerce solution. The paper describes the OMM reference model and shows how it can be applied flexibly to capture the different classes of resources within a corporation, and to maintain the complex and dynamic roles and relationships between the resource objects. Administrative tools use the role model in OMM to define security policies for role definition and role assignment. At runtime, the E-Commerce application and the underlying resource manager queries the OMM system to resolve roles in order to authorize any access attempts. Contrary to traditional approaches, OMM separates the organization model from the applications; thus, it allows independent and flexible role modeling to support realistically the dynamic authorization requirements in a rapidly changing business world. q 2000 Elsevier Science B.V. All rights reserved.

Keywords: Electronic commerce; Role-based access control; Organization modeling; Role resolution; Business process management; Workflow

## 1. Introduction

Electronic Commerce E-Commerce applications Ž . aim to conduct business over the electronic network. Although electronic business transactions evolved from EDI protocols will continue to play a major role in E-Commerce, the rapid growth of the Internet Žin 1998, more than 2 million new users are added to the Internet every quarter 20 has pushed compa- <sup>w</sup> <sup>x</sup>. nies to expand the scope of E-Commerce applications to cover the full range of business activities 3 .<sup>w</sup> <sup>x</sup> These activities may include marketing, negotiation, fulfillment and follow up, all perform over the Internet. This trend creates new business opportunities and posts new technical challenges. It pushes E-

Commerce to go beyond simple short-lived transactions but become a business process that includes outside customers, business partners, and a number of resources within a company. As more people are involved in the transaction circle, security and authorization control become one of the biggest concerns.

Current E-Commerce solutions are primarily developed as applications on top of Resource Managers Ž . Ž . RM or database management system DBMS . Unfortunately, resource manager implementations have historically focused on technologies around access methods, concurrency control, and logging and recovery 7,8,16 . The security model and access con-<sup>w</sup> <sup>x</sup> trol usually assume a simple and static model, which are based on user and group identifiers. As E-Commerce applications are implemented over the DBMS, they simply adopt the user and security model of a relational database management system RDBMS as Ž . their access control model. However, the user model in RDBMS is designed primarily to support access control in processing isolated transactional operations rather than integrated process activities 17 . It<sup>w</sup> <sup>x</sup> is thus not adequate to model the flexible resource relationship that is required to support cooperative works in the E-Commerce context.

The introduction of workflow technology allows E-Commerce applications to cover the full range of business activities over the network. As the workprocess flows across multiple organizations, it is important to identify the different resources involved in the process. However, current workflow deployment practically focuses on departmental level; many of these systems simply ignore the role issue. Others though expand their scope to cover workflow across departmental boundaries, they still assumed a static organization and role model within a single corporation 2,13 .<sup>w</sup> <sup>x</sup>

This paper discusses an organizational and role model to support dynamic access control in E-Commerce. The model is called Organization Modeling and Management OMM . The OMM methodology Ž . supports both the conceptual design and the design implementation phases of the enterprise modeling cycle 1 . It serves as an underlying system for <sup>w</sup> <sup>x</sup> applications and resource managers to control resource accesses and job assignment. The next section covers the related research work in role-based access control RBAC and organization modeling. Section Ž .

3 describes the OMM conceptual and reference model for enterprise modeling. OMM does not assume a particular process or application architecture. With this generic approach, OMM is able to map its object types to other organizational data schemes and to present an integrated multidimensional view of different organizational resources. Section 4 presents the role resolution concept in E-Commerce and discusses a Java-based prototype, OMM, which is used to implement an RBAC system to enable the E-Commerce strategy in a hi-tech company. Section 5 discusses the OMM system architecture. The paper will conclude in Section 6 by a summary and by sharing our practical experience of applying the OMM methodology to a hi-tech firm to support their E-Commerce strategy.

## 2. Related work

Role-based security has been applied in various areas of computer systems security 32 . Osborn 28<sup>w x</sup> <sup>w x</sup> and Kuhn 21 proposed formal models for RBAC.<sup>w</sup> <sup>x</sup> These works provide a basis for separation of duty based on role names. Access privileges are granted to different roles. A user can play multiple roles by binding with a number of role names. Although this approach gives more flexibility to access control than the simple granting to user identifier method, it is still a static approach and ignores entirely the organization model.

Others have proposed specific role models and methodologies for concurrent engineering, such as <sup>)</sup> <sup>w</sup> <sup>x</sup> <sup>)</sup> M -OBJECT 12 , SAM 33 , and ObjectFlow<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 18,19 . They all start from the process view and tightly couple the organization model with the role model, and some even with the process model.

Other researchers have proposed visual and programming languages for organizational and office systems, such as Officeaid-VPE 11 , HI-VISUAL<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> <sup>)</sup> 15 , M -OBJECT 12 and Regatta VPL 34 . Of-<sup>w x</sup> <sup>w x</sup> ficeaid-VPE and HI-VISUAL were limited to the description of single office tasks. They are therefore not adequate for the integration and collaboration across multiple offices, let alone to include external customers and business partners as required in E-Commerce. M<sup>)</sup>-OBJECT and Regatta VPL have a comprehensive process model and an abstract view of organizations; however, the coupling of the process model with the organization model limits their flexibility in organization and role design.

Some implementations attempt to isolate an organization component from the workflow engine. For instance, WorkParty, a workflow system by SIEMENS, has an organization component called ORM, which is a standalone client-server database application to support organizational modeling 5,31 .<sup>w</sup> <sup>x</sup> ORM has an application programming interface API Ž . and a graphical user interface GUI to allow users to Ž . define and populate the organizational database. Although ORM separates the organization model from the process model, it does not separate the organization model from the role model; the two are still integrated. Also, the organization definition and the role definition of ORM are still static like other prior arts, and it suffers from lack of a dynamic relationship model.

The OÕal project by Malone et al. 23,24,29 at<sup>w</sup> <sup>x</sup> MIT provides a handy tool for inventing organizations. It has an object model for constructing organization information and structure. Through userspecified rules, it can process message objects, such as notification or customized information flows, according to a user’s need. Oval also supports adding hard links between resource objects but not dynamic links.

Still other former efforts address the organizational resource management issue through directory service. Directory services DS and other namingŽ . services are aimed to support distributed object lookup with a naming convention 6 . Each object on<sup>w</sup> <sup>x</sup> the system is assigned a static and universally unique identifier UUID . This approach yields an efficient Ž . solution for simple point-to-point interaction in collaborative software; it resolves static addresses for electronic mail, video conferencing, group scheduling and the likes. Nevertheless, DS lacks an organization model and support for dynamic relationships between resources. Consequently, it fails to support advanced applications, such as in E-Commerce, where deferred binding till run-time is necessary to find out the entity that should be responsible to handle the transaction.

Overall, the existing approaches for access control, user<sup>r</sup>group-based or role-based, suffer from the following common weaknesses.

<sup>Ø</sup> Assume static and isolated transactions over a connected series of work within the E-Commerce business process. As a result, access control fails to implement certain business policies that require reference to the overall context of the business process.

<sup>Ø</sup> Lack a conceptual organization reference model. We need a generic solution so that we can apply the model to different E-Commerce applications and cooperative computing environments.

<sup>Ø</sup> Role model tightly integrated with the process and application architecture. Consequently, it is only adequate to support the particular E-Commerce applications and the underlying BPM systems that observe the specific models.

<sup>Ø</sup> Support only some predefined resource types. Network DS focuses on machine nodes, users and applications; messaging DS on user addresses; and BPR organization subcomponents on users, groups and roles. To support the collaboration between the different applications and users in E-Commerce, the access control module must be extensible and flexible in order to define the access policies over various resource types, which include customers, employees, departments, applications, robots, business partners, and others.

<sup>Ø</sup> Assume only static and hardwired relationships between resources. In reality, relationships between resources are rapidly changing. Relationship exists not only among resources of the same type, but also among different types of objects. For instance, there is a many-to-many relationship between the company projects and its employees. Similarly, a threeway relationship can be defined between customers, bank accounts, and loan agents.

<sup>Ø</sup> Lack openness to integrate and work with other organizational management systems. There are existing directories and organizational resource information systems that run in a cooperative environment, a comprehensive architecture must take consideration to exchange information with the existing solutions.

## 3. The OMM methodology

With the workflow approach, process routing control is abstracted from the application logic; it thus results in a flexible design and implementation of flow logic without interfering the implementation of the associated applications. The flow logic concerns mainly the routing decisions throughout the life of a process instance. The Petri-net representation in Fig. 1 illustrates a flow description of a E-Commerce application, which is a simplified electronic parts ordering process 5,19,27 . <sup>w</sup> <sup>x</sup>

In this example, an electronic parts manufacturing company is offering its products online to business customers. The company divides its product lines by divisions, and different departments within a division manage the production and sales of individual products. A sales representative works in a department and reports to his or her corresponding manager. To complete an electronic ordering process, a number of human workers are involved. The business process is initiated by a worker flow-initiator in the customerŽ . company, most likely over the Internet. This worker will execute the submit order<sub>–</sub> step. The WFMS will then move the process forward, and the sales representative who is serving the flow-initiator’s company must execute the process order<sub>–</sub> step. If the dollar amount of the order is within the customer’s credit limit, the flow will immediately move to the decision step. However, if the dollar amount of the order exceeds the customer’s credit, the business process will require managerial signature; this corresponds to the approÕal 1<sub>–</sub> step in Fig. 1. In general, only the manager of the sales rep of a process instance can grant such authorization. Unfortunately, since the manager-to-sales-rep ratio is usually high 1:10 andŽ . in some cases can grow to 1:20, this step often creates performance bottleneck. To reduce such bottleneck, a policy is established such that the approval signature can be sought from an alternative source under the following condition. If the sales rep’s department currently has more than N number of managerial approval cases pending whereŽ N can be any positive number set by the administrator , then. managers of any other departments within the same division can authorize the process. This corresponds to the approÕal 2<sub>–</sub> step in Fig. 1. Once a managerial signature is obtained, the process will move forward. If the difference between the customer’s credit and the order’s value is over a certain amount \$ M Žwhere M can be any dollar amount set by the administrator ,. then an additional signature from the division VP is required. This corresponds to the step approÕal 3<sub>–</sub> in Fig. 1. Note that only the vice president of the division to which the sales rep of this process instance belongs can process step approÕal 3<sub>–</sub> . The next three steps in this example, decision, accept, and reject, can be automated steps, which are accomplished by software programs without any human intervention. The shipping step can be accomplished by workers in the shipping department. The final step, notify-and-billing, can again be an automated step.

A sophisticated workflow system supports the definition of this process by allowing an administrator to define this flow-map through some graphical or scripting interface. The workflow data, which impact the routing decision of the flow, are also defined as part of the flow definition. Agent applications, the applications associated with individual steps, are connected to the workflow system through some workflow programming interface. Finally, roles are defined to control task assignment and task authorization <sup>w</sup> <sup>x</sup> 10 . Since the role model of the current business process management BPM systemsŽ . does not support defining dynamic relationships over various resources, it is not adequate to support even a simple E-Commerce application such as the one above.

![](/api/attachments/SVPZ7ZDA/fulltext/images/65439387a3b9bc93a0ff53160d924610a81926c9eeb339b0adc7aa24153dfd82.jpg)  
Fig. 1. Electronic parts ordering process.

![](/api/attachments/SVPZ7ZDA/fulltext/images/c879787ddcce60a80b23a0829475d249356af962de3c06021f91137ab21f8c1a.jpg)  
Fig. 2. OMM separates the role and organization models.

Contrary to existing systems, OMM methodology separates the organization model from the role model of the BPM system 4,5,26,36 . As a result, OMM is<sup>w</sup> <sup>x</sup> able to capture the different resources, both internal and external to the company, involved in the E-Commerce application. Furthermore, it allows us to define dynamic relationships on top of these resources. Fig. 2 shows how the different models interface with one another. With the OMM approach, entities, such as customers, employees, products, equipment and others, are modeled as different object classes separately from the business processes and applications. Role definition and resolution are done through the organizational modeling and management interface.

## 4. The OMM organization and role model

The OMM employs a generic reference model, which can be applied flexibly to define different resource types, the roles they play, and their interrelationships. Resource types are user-defined; they may include workers, machines, robots, applications, processes, products, customers, and others. Modeling of an enterprise involves defining these classes of resources and the dynamic relationships between these resource objects. An E-Commerce process application is interested in assigning tasks to a subset of these resources, such as employees, business partners, or customers. Furthermore, it may associate a step with a certain application, or assign a set of machines that the step should be running on.

There are three fundamental entities in the OMM model, namely the organizations, members, and Õirtual links.

An enterprise is composed of a number of OMM organizations. Each organization represents a class of corporate resources. Each member object within an organization maps to an actual entity of the corporation. Members of the same class share a common set of attributes and methods that is extensible. A member can relate or link to other members through Õirtual links. Contrary to static connections, a virtual link only has a relationship definition, which is evaluated and resolved at runtime. Fig. 3 uses an E-R diagram to show the OMM model. We shall discuss each of the OMM objects in greater detail.

## 4.1. Organizations

An enterprise is composed of a number of OMM organization objects. OMM organizations are created to map to the different dimensions and components of a company. Each organization has a unique identifier across the global enterprise. Using the OMM organizations, a company can be partitioned both vertically and horizontally; vertically into different dimensions or resource types, such as customers, employees, projects and so on. Horizontal partitioning can be applied to break components of the same type into smaller units, such as breaking employees into fulltime workers, contractors and temporary workers.

For instance, during the organization conceptual design phase, an OMM organization may be defined to represent the people of the company, another to represent the different projects, even another to represent the robotic machines, and so on. This creates a view of vertical partitioning of the corporation. Each partition keeps the organization information of a particular dimension. In addition, we can further divide an organization within the same dimension horizontally. For instance, people belonging to the engineering department may be included in one organization, while people in the marketing department are placed in another. In other words, vertical partitioning helps to define the different types of resources within the enterprise, while horizontal partitioning allows users to logically divide resources of the same dimension into smaller subcomponents. Fig. 4 depicts the horizontal and vertical partitioning of the OMM organizations.

![](/api/attachments/SVPZ7ZDA/fulltext/images/5f487c943c3112754ee1a18aa50b23efd0b739419ae7a5af2333103007be929b.jpg)  
Fig. 3. The OMM organization model.

Since different departments or divisions now own their individual organizational definition, a much greater level of autonomy in defining and managing organizational information is granted to them. They can update, delete, or append to their own organizational definition without impacting others. For major restructuring, users may alter the organization schema that corresponds to their units only. In addition, the granularity of partitioning is controlled entirely by management. They have the flexibility to decide how fine they want to divide the organization. When the business conditions change, they may choose to merge together or to further divide their organizations. This is important to support flexible E-Commerce strategy as companies streamline and automate the E-Commerce processes across multiple units within the corporation.

At the organization design-implementation phase, we will consider the database schema of the OMM organizations. The different partitions of OMM organizations correspond naturally to database tables. It is typical to use some tables within a database environment to capture the information of an organizational partition. The OMM methodology does not dictate the underlying data model, although our current prototype implementation uses an RDBMS.

![](/api/attachments/SVPZ7ZDA/fulltext/images/a2fec3db235feece753e70016df7892177d4dd0db4899a80862b67fef51242cf.jpg)  
Fig. 4. Horizontal and vertical partitioning of OMM organizations.

![](/api/attachments/SVPZ7ZDA/fulltext/images/f0fc7db1c3ac528049472def726188b58f1b79bb52c779bd3e93d41c75e39915.jpg)  
Fig. 5. Class hierarchy of OMM member.

When a relational database implementation is chosen, users define the attributes of the members as columns in a relational table. In an object-oriented database environment, the member attribute definition maps directly to a class definition. This constitutes a class of members for each OMM organization.

## 4.2. Members and the information model

OMM uses an object-oriented model to capture its member information. An enterprise has a main member class, which is the super-class containing a list of system-defined attributes and methods. All user-defined member classes are subclasses of the main member class and inherit the properties of the super-class. Fig. 5 shows the class hierarchy.

The identifier attribute is unique for each member across the entire enterprise. Each member object has a name that is given by the user and is unique only within an OMM organization. Each member object in OMM goes through a life cycle, which is represented by the state transition diagram shown in Fig. 6.

When a resource is created, it enters the actiÕe state. Thereafter, the state changes are triggered by the user through a member method, setState(). A member object may cycle between the actiÕe and inactiÕe states, simulating in reality some resources being suspended, put off-line, or on-leave. When a resource is remoÕed, its information may still be retained in the repository and be queried until it enters the forgotten state, which corresponds to the situation that the resource information is archived away.

![](/api/attachments/SVPZ7ZDA/fulltext/images/f04e370ee97501a8b1f64c60f484a34e5340c8eac59d394c424166e93e942144.jpg)  
Fig. 6. State transitions of an OMM member.

In OMM, member ownership can be transferred from one organization to another. When a member is moved to another organization, some of the user-defined attributes from the original organization may be mapped to the new one, and all other irrelevant information is dropped. However, the system-defined attributes are always retained. This maintains the unique identity of the member even though it may be moved around the enterprise from place to place.

From the class definition point of view, the OMM model is similar to the Object Class in the directory model of X.500 6 . OMM members are different <sup>w</sup> <sup>x</sup> from the X.500 objects in that they support class inheritance, method extension, and object life cycle. The latter captures the dynamic behavior of a resource within a corporation. It also allows the workflow engine to properly perform worklist management. Based on the state of a resource at runtime, the workflow manager may choose to avoid pushing a task to a worker unless it is in the actiÕe state, thus reduces the possibility of assigning work to personnel that are unavailable. Furthermore, the OMM model is unique in that members may relate dynamically to one another through Õirtual links.

## 4.3. Virtual links and the relationship model

As collaborative effort exists between company resources, it is necessary to model relationships between them 30,37 . OMM uses virtual links to de-<sup>w</sup> <sup>x</sup> fine dynamic relationships between member objects. Virtual links are rules constructed based on the member attributes and contextual variables. The OMM engine evaluates the rules to identify roles and relationships that resources have in the company. In OMM, a relationship is established from one resource to! another, and as such it can be represented as a directed edge. If a bidirectional relationship Ž . such as supervisor–subordinate relationship is desired, it can be modeled as two relationships; one as a reÕerse relationship of the other. In this respect, resource objects are like nodes, while virtual links are the directed edges in a graph. A virtual link is defined by the following BNF syntax 9 :<sup>w</sup> <sup>x</sup>

```xml
<Virtual Link> ::= <Owner>, <Relationship Type>, <Expression>, <Organization Scope>
<Owner> ::= null| <Member ID >
<Relationship Type> ::= <Relationship Name> [REVERSE<Relationship Name>] [TRANSITIVE]
<Relationship Name> ::= <Character String Constant>
<Expression> ::= <Expression> <Rel Op> <Expression> |<Attribute Name> <Op> <Value> | <Contextual Variable> <Op> <Value>
<Attribute Name> ::= <Character String Constant>
<Op> ::= = |!=|>=|>|<|<=|
<Value> ::= <Constant> |<Attribute Name>
<Contextual Variable> ::=$<Character String Constant>
<Rel Op> ::= AND|OR
<Organization Scope> ::= <Organization Name>+
<Organization Name> ::= <Character String Constant>
```

The connection between resources is dynamic and virtual because the relationship is defined with a regular expression over the attributes rather than a pair of static resource IDs. There may be a predefined owner of a relationship, or the owner can be associated at runtime. When a user resolves a virtual link, the relationship expression is evaluated over the member attribute values, and there may have any number of resources satisfying the criteria indicating a relationship with the owner in question. An example of a relationship can be:

Owner: null

Relationship Name: manager of <sub>–</sub>

Organization Scope: employee

To find all the employees that are under the managerial responsibility of an executive with member ID john smith<sub>–</sub> , we can resolve this virtual link upon the employee organization. The owner is set to ‘john smith’, its attribute values are retrieved and<sub>–</sub> used to substitute corresponding fields in the virtual link expression. Each member within the employee organization is evaluated against the expression; the X.attributeName is substituted with the correspond ing attribute values of the member under evaluation.

Despite dynamic characteristics of relationships in OMM, hard-coded relationships between two specific entities can still be modeled with virtual links. To define that Mary Ann is acting for <sub>–</sub> John Smith, we have:

$$
\begin{array}{l l} \text {Owner:} & \text {\text {‘mary\_ann’}} \\ \text {Relationship Name:} & \text {acting\_for} \\ \text {Expression:} & (\text {X.name = = 'john\_smith')}) \\ \text {Organization Scope:} & \text {employee} \end{array}
$$

Note that a link may or may not be transitiÕe in nature. When a transitive relationship $r _ { 1 }$ is defined, and if member $m _ { 1 }$ relates to member $m _ { 2 }$ in $r _ { 1 } .$ , and $m _ { 2 }$ relates to $m _ { 3 }$ in $r _ { 1 } .$ , it follows that $m _ { 1 }$ also relates to $m _ { 3 }$ in $r _ { 1 } .$ . Obviously, there is a cost associated with resolving transitive relationships; they should therefore be used with care.

When defining a relationship type, a reÕerse relationship can be specified. For example, if relationship types $r _ { 1 }$ and $r _ { 1 } ^ { \prime }$ are defined as reverse relationships to each other, and if member $m _ { 1 }$ relates to $m _ { 2 }$ in $r _ { 1 }$ , then $m _ { 2 }$ relates to $m _ { 1 }$ in $r _ { 1 } ^ { \prime }$

Fig. 7 shows a relationship graph within an organization; note that here the superÕisor of <sub>–</sub> and the subordinate<sub>–</sub> $. o f$ are represented by reverse links to each other:

Although the example only covers relationships within an organization, virtual links can actually be defined across multiple organizations. In this case, the organization scope will list all OMM organizations involved. For instance, a relationship graph may be desirable to represent the connections between a project and its machine resources and the employees who are involved in the project. Here, the owner is a particular project while the organization scope will include both machine and employee.

![](/api/attachments/SVPZ7ZDA/fulltext/images/915cb5449b519c3222b6b1db955927183b581cc4130c48b88de48656a748f2a3.jpg)  
Fig. 7. OMM relationship graph.

A virtual link may also be defined between a member and an organization. When an OMM organization object is part of a relationship, all member objects within that organization are involved in it. For instance, if Tom Moore is a supervisor of an organization, then he supervises all resources within that organization.

Using virtual links, a workflow system assigns and authorizes steps flexibly to resources who play different roles in the company. Referring to the electronic parts ordering process in Section 3, the roles Athe manager of the sales rep of a process instanceB and Avice president of the division to which the sales rep of this process instance belongsB can be expressed easily with the regular expression in virtual link.

## 5. Role definition and role resolution

Integrated and dynamic E-Commerce applications require support of business process integration and automation 8,25 . It provides a framework on which<sup>w</sup> <sup>x</sup> multiple tasks and applications are integrated to form a network of steps to accomplish a business process <sup>w</sup> <sup>x</sup> 35 . When E-Commerce application is implemented as a business process, it can be formulated as a set of nodes, representing the tasks or steps, connected by some directed edges, which are condition arcs governing the route of the process refer to Fig. 1 for a Ž Petri-net representation of a workflow process . To . ensure this model has a consistent flow behavior, conceptually a process always has a BEGIN and an END step. The BEGIN step only has outgoing arcs and the END step only has incoming arcs. The other steps exist between BEGIN and END have one or more incoming arcs and outgoing arcs 19 .<sup>w</sup> <sup>x</sup>

As the process progresses in time, different tasks are created and assigned to various resources in the company. Sometimes a particular resource may be chosen to execute a step theŽ . pushmodel , other times a group of workers are identified as potential candidates to perform a task; the workers will pick up the task on their own choice theŽ . pullmodel . In both cases, authorization checking must be performed when someone attempts to open and work on a workflow step.

The task assignment and task authorization, which have to do with role resolution, are among the biggest challenges of a successful process-oriented solution. Role resolution refers to identifying the right resources that are playing a certain role <sup>w</sup> <sup>x</sup> 14,30,31 . Two types of questions are asked in role resolution. One is definitive in nature, and the other is relational. The following examples illustrate both types of questions, respectively:

1. Is X an engineer? Or who are the engineers? Ž . definitive

2. Is Y the manager of X? Or who is X’s manager? Ž . relational

The OMM methodology provides a strong basis to model dynamic task assignment and authorization in a BPM system 6,22 , even to the extend of<sup>w</sup> <sup>x</sup> supporting E-Commerce applications, which may include resources external to the corporation. Although the syntax of assignment and authorization specifications in workflow is implementation dependent, most systems support the abstraction of roles to allow more flexibility than simply using user IDs 8,14,19 .<sup>w</sup> <sup>x</sup> A control statement is usually included in the step definition for that purpose. The following syntax of control statement illustrates the notion of such specifications:

² :Role

² :Role Label

The following is an example of authorization statement within the workflow script:

With the current state of the art, users are assigned to take different roles identified by labels like ‘Manager’. The use of role labels, although has more flexibility than simply using a user name in the control statement, does not support resource relationships, which are required in most realistic business processes, such as the electronic parts ordering process discussed in Section 3. With OMM, role definition can be expanded to cover relationships:

$$
\begin{array}{l l} \langle \text {Role} \rangle & : := \langle \text {Role Label} \rangle | \langle \text {Relationship} \\ & \text {Name} \rangle \langle \text {Resource} \rangle \\ \langle \text {Relationship} & : := \langle \text {Character String Constant} \rangle \\ \text {Name} \rangle \\ \langle \text {Resource} \rangle & : := \langle \text {Member ID} \rangle \\ & | \text {\$INITIATOR\_OF\_PROCESS} \end{array}
$$

where \$INITIATOR OF PROCESS is a workflow<sub>– –</sub> system-defined data item, which can be retrieved through the workflow interface. Using the example in Section 3, the workflow script reads:

$$
\{\dots \text {step definition} \dots \} \text {EXECUTE BY same\_business\_VP\_of $INITIATOR - OF\_PROCESS}
$$

At runtime, when a member M attempts to open this step for execution, the workflow engine will query the OMM system to verify if M is the same<sub>–</sub> business VP of <sub>– –</sub> the initiator of the flow process. Here, same business VP of<sub>– – –</sub> is a virtual link, M becomes the owner, and the initiator of that process instance is the member in question. The authorization checking therefore reduces to the following question:

Is M the same business VP of<sub>– – –</sub> the \$INI-TIATOR OF PROCESS?

where same business VP of<sub>– – –</sub> is defined by an expression such as:

$$
\begin{array}{l} \text {(owner.division = = X.division) AND (owner.title} \\ = = ^ {\prime} \mathrm {VP ^ {\prime}}), \text { or } \end{array}
$$

M is the user accessing the process step, and \$INITIATOR OF PROCESS is known by the<sub>– –</sub> workflow engine, the above expression can be evaluated to return a boolean value of whether M is authorized to execute this step. For instance, if M is Charles and the \$INITIATOR OF PROCESS is Susan, then:

Charles is the VP in Susan’s business unit if:

Ž . Charles. division <sup>ss</sup> Susan. division AND Ž .Charles.title <sup>ss</sup>‘VP’

## 6. The OMM system architecture

At the design-implementation phase, the existing organizational databases, such as the human-resource Ž . HR database, customer profile and the corporate directory, are analyzed and mapped to the OMM organization design. Based on this mapping, the agent programs, which make up a part of the OMM server architecture, can populate the OMM data store by accessing the existing databases. In some cases, due to the continual usage of legacy HR applications over the existing organizational databases, it is necessary to periodically refresh some part of the OMM data store by rerunning the agent programs. The actual mapping of the various database schemes to the object-oriented OMM scheme is outside the scope of this paper.

At runtime, the resource manager accesses the OMM organizational information and performs role resolution by calling the OMM API. The OMM server evaluates the rule representing this role on the current organization database and returns the result to the RM. A graphical administrative tool, also calling the OMM API, is used for users to manage the organizational objects through a GUI.

Fig. 8 shows the OMM runtime system architecture with the RM and existing organizational databases.

## 6.1. Domain UUID and naming conÕention

Each OMM server attends clients within a domain. OMM servers exchange information with one another through the regular OMM APIs. A domain corresponds to a physical implementation of a data store in OMM. Multiple OMM organizations may reside in a domain, but an organization does not span across domains. A domain has a globally unique identifier, while organization names are unique only within a domain. However, the relatively unique name of an organization, combined with the unique domain name, must be a UUID. For instance, domain london and domain seattle may both contain an organization named employee. The corresponding unique organization names will look like this:

![](/api/attachments/SVPZ7ZDA/fulltext/images/ecfb09c2c072ee3f2b6522a568b0a1f3821db5453806afc474ae35433b4d44e2.jpg)  
Fig. 8. OMM runtime system architecture.

employee.london employee.seattle

Similarly, although a member name is only unique within an organization, by concatenating the member name with the UUID of the organization, we can obtain a UUID for the member as well. For instance, the member names:

john smith.employee.london<sub>–</sub> john smith.employee.seattle<sub>–</sub>

are globally unique.

For a user to be able to access the global organizational information, updates to domains and OMM organization definitions ought to be propagated to all OMM servers on a regular basis such as once every Ž hour . It is not necessary to escalate updates of . members, virtual links, or attributes outside of a domain, for the organization UUID will indicate if the underlying information is managed by another server. Based on this UUID, the local server may retrieve data from the remote server.

## 7. Conclusion

In this paper, a dynamic organizational information system, the Organization Modeling and Management OMM methodology and organization model,Ž . along with its system architecture, are presented as a comprehensive tool to model roles to support dynamic role-based authorization in E-Commerce. The application of the OMM methodology in role resolution of an electronic order processing application is discussed. Compared to previous efforts 1,4,6, <sup>w</sup> 9,11,17,19,21,24,28,32 , OMM is similar in having a<sup>x</sup> strong object model and separating the organization model from the process model. However, OMM also abstracts the organization model from the role definition, thus giving flexibility in complex organization modeling. It is novel in having a dynamic interrelationship notion that is expressed by using regular expressions over member attributes, system-defined variables and contextual variables. We show that the relationship model is essential in supporting access control of cooperative software, such as E-Commerce applications, for authentication, authorization and dynamic job assignment. Using virtual links, OMM can model dynamic roles such that policies regarding various operations over the work objects can be defined and maintained. Finally, the explicit life cycle of the OMM members reflects the dynamic state changes of resources in reality. This provides a handle for better support of organization management and makes task rerouting and optimistic exception handling in a E-Commerce system possible in case a resource is absent from its duty.

Although OMM is strong in modeling enterprise resources and their interrelationships, it does not have a process model for defining business processes. Our goal is to make OMM available for the research community and to solicit research partners in workflow.

Several areas of further research stem out directly from our current work. OMM as an analytical and modeling tool is useful. However, if the organization database is only maintained by the modeler, then the information collected during the organization analysis process will remain to be static and will quickly be outdated as the organization is undergoing constant changes. Hence, it is important for the OMM system to continually receive input and to have the capability to adjust itself automatically as the underlying information of the organization change. In order to accomplish that goal, we must provide ways for workers on all levels of the enterprise to continually and handily maintain up-to-date information of those enterprise objects that they manage. The OMM system accomplishes this by providing an open Java API to support the development of Internet and Intranet applications. Users not only can access and review organizational resource information, organization structure and resource connections, but can also update the resource information anywhere, anytime through the World Wide Web. As the underlying information is updated, the specific organization models created through the network of enterprise resources and the corresponding interobject relationships will automatically adjust themselves to represent the most up-to-date picture of the enterprise. However, once we allow multiple users to modify the organizational information concurrently, it is possible for them to run into conflicts that may lead to data inconsistency and deadlocks. Although the underlying DBMS can protect data integrity and resolve transaction conflicts, as we are dealing with an object-based system, more work is required to coordinate access on the object level. We are considering providing object-level locks to improve the usability and performance of the system.

In modeling dynamic relationships, we are defining the relationships only between OMM member objects. It would be more powerful if we expand virtual links to cover relationships between a member and an organization, or even between two organizations. When an OMM organization is being part of a relationship, all member objects within that organization are involved in it. For instance, if Tom Moore is a supervisor of an organization, then it is assumed that he supervises all resources within that organization.

A Java-based OMM prototype code name OMMŽ S-25 has been developed at OCT Research Labora-. tory 10 . With S-25, users can model the different <sup>w</sup> <sup>x</sup> resource types and create resource objects representing various entities in the enterprise. Relationships between the objects are modeled as virtual links using regular expressions. A web interface is provided for users to browse through the enterprise and discover the detailed information and connections of the resources from different point of view. In our case study, we have applied the OMM methodology to model the organizational infrastructure of Hitachi America and use OMM as a key component in their E-Commerce implementation. Hitachi America has 6000 people and over 200 departments, by defining six virtual links to capture their business policies, over 1500 graphical models are automatically generated and self-maintained to represent the complex relationship and interrelated roles between the resources. Hitachi is committed to an E-Commerce initiative strategy. Mas Ishigaki, the Deputy Manager and Director of Information Technology Division at Hitachi America said, AWe need to ensure that E-Commerce is conducted in a secured and controlled manner. Organizations need to adapt rapidly to the ever-changing business environment to stay competitive. OMM is a key technology that can enhance our organization’s ability to better manage change and strengthen our competitiveness.B

## Acknowledgements

Most of the research on OMM is initiated at the OCT Research Laboratory. The author likes to express thanks to many designers and developers who have contributed to the concept and implementation of the OMM system. Thanks to George Loizou for his insightful input, the numerous discussions with him on the OMM model have been very helpful. Thanks to Dieter Gawlick for his input on workflow and the requirement of publish-and-subscribe, which has greatly impacted my thoughts on the topic. Thanks to my wife for her continuous support and encouragement throughout the entire project.

## References

<sup>w</sup> <sup>x</sup>  1 G. Berio et al., The M -OBJECT methodology for information system design in CIM environments, IEEE Trans. Syst. Man Cybern. 25 1 1995 68–85.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 E. Bertino, E. Ferrari, A. Vijayalakshmi, A flexible model for the specification and enforcement of role-based authorizations in workflow management systems, Proc. 2nd ACM Role-Based Access Control Workshop, 1997, November.

<sup>w</sup> <sup>x</sup> 3 D. Blum, D. Litwack, The E-Mail Frontier: Emerging Markets and Evolving Technologies, Addison-Wesley Publishing, 1994, pp. 295–319.

<sup>w</sup> <sup>x</sup> 4 C. Bussler, Enterprise process modeling and enactment in GERAM, Proc. 3rd Intl. Conf. Automation, Robotics and Computer Vision ICARCV ’94 , Singapore, 1994, Novem- Ž . ber.

<sup>w</sup> <sup>x</sup> 5 C. Bussler, Analysis of the organization modeling capability of workflow management systems, Proc. PRIISM ’96 Conf.,. Maui, Hawaii, 1996, January.

<sup>w</sup> <sup>x</sup> 6 CCITT Recommendation X.500 to X.521: Data Communication Networks, Directory, Blue Book, Also ISO<sup>r</sup>IEC Standards ISO 9594-1 to ISO 9594-7, 1988.

<sup>w</sup> <sup>x</sup> 7 E. Cheng et al., An open and extensible event-based transaction manager, Proc. USENIX Conf., 1991.

<sup>w</sup> <sup>x</sup> 8 E. Cheng, Re-engineering and automating enterprise-wide business processes, Proc. Int. Working Conf. Information Industry, Bangkok, Thailand, 1995, April.

<sup>w</sup> <sup>x</sup> 9 E. Cheng. The OMM Model. Technical Report of the OCT Lab and College of Notre Dame, Belmont, CA, November 1997.

<sup>w</sup> <sup>x</sup> 10 E. Cheng, A rule-based organization modeling system to support dynamic role resolution in workflow. Parallel and distributed computing systems, Proc. ISCA 11th Int. Conf., Chicago, Illinois, 1998, September.

<sup>w</sup> <sup>x</sup> 11 P. Di Felice et al., Officeaid VPE: a visual programming with examples system for specifying routine office tasks, J. Visual Lang. Comput. 2 3 1991 275–296.Ž . Ž .

<sup>w</sup> <sup>x )</sup> 12 A. Di Leva, P. Giolito, F. Vernadat, The M -OBJECT organisation model for enterprise modeling of integrated engineering environments, Concurr. Eng. Res. Appl. 5 2Ž . Ž . 1997 183–194.

<sup>w</sup> <sup>x</sup> 13 D. Ferraiolo, J. Barkley, Specifying and managing role-based access control within a corporate intranet, Proc. 2nd ACM Role-Based Access Control Workshop, 1997, November.

<sup>w</sup> <sup>x</sup> 14 G. Gottlob, Extending object-oriented systems with roles, ACM Trans. Inf. Syst. 14 3 1996 268–296.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 M. Hirakawa, M. Tanaka, T. Ichikawa, An iconic programming system, HI-VISUAL, IEEE Trans. Software Eng. 16 Ž . Ž . 10 1990 1178–1184, October.

<sup>w</sup> <sup>x</sup> 16 M. Howard, Work flow: the coordination of business processes, Gartner Group Presentation Highlights, 1991, August.

<sup>w</sup> <sup>x</sup> 17 C. Hsu, L. Rattner, Information modeling for computerized manufacturing, IEEE Trans. Syst. Man Cybern. 20 4 1990Ž . Ž . 758–776.

<sup>w</sup> <sup>x</sup> 18 M. Hsu, An Execution Model for an Activity Management System, Digital Technical Report, April 1991.

<sup>w</sup> <sup>x</sup> 19 M. Hsu, C. Kleissner, Objectflow-towards a process management infrastructure, Distrib. Parallel Databases 4 2 1996Ž . Ž . 169–194.

<sup>w</sup> <sup>x</sup> 20 Internet Trak, 2nd Quarter, 1998, Ziff-Davis Publishing, July 1998, http:<sup>rr</sup>www.zd.com<sup>r</sup>marketresearch<sup>r</sup>it2q.htm.

<sup>w</sup> <sup>x</sup>21 D.R. Kuhn, Mutual exclusion of roles as a means of implementing separation of duty in role-based access control systems, Proc. 2nd ACM Workshop on Role-Based Access Control, 1997, ACM, November.

<sup>w</sup> <sup>x</sup> 22 P. Lawrence, WfMC Workflow Handbook, Wiley, 1997, pp. 295–353.

<sup>w</sup> <sup>x</sup> 23 T.W. Malone et al., Tools for inventing organizations: toward a handbook of organizational processes, Proc. 2nd

IEEE Workshop on Enabling Technologies Infrastructure for Collaborative Enterprises, Morgantown, WV,1993, April.

<sup>w</sup> <sup>x</sup> 24 T.W. Malone, K.-Y. Lai, C. Fry, Experiments with oval: a radically tailorable tool for cooperative work, ACM Trans. Inf. Syst. 13 2 1995 177–205, April.Ž . Ž .

<sup>w</sup> <sup>x</sup> 25 Medina-Mora et al., The action workflow approach to workflow management technology, Proc. Commun. ACM CSCW,1992, November.

<sup>w</sup> <sup>x</sup> 26 K. Mertins, P. Heisig, O. Krause, Integrating business-process re-engineering with human-resource development for continuous improvement, Int. J. Technol. Manage. 14 1Ž . Ž . 1997 39–49.

<sup>w</sup> <sup>x</sup> 27 T. Murata, Petri nets: properties, analysis and applications, Proc. IEEE 77 4 1989 541–580.Ž . Ž .

<sup>w</sup> <sup>x</sup>28 S. Osborn, Mandatory access control and role-based access control revisited, Proc. 2nd ACM Workshop on Role-Based Access Control, 1997, ACM, November.

<sup>w</sup> <sup>x</sup> 29 Oval Version 1.1 User’s Guide, Center for Coordination Science, MIT, Cambridge, 1992.

<sup>w</sup> <sup>x</sup> 30 H. Roos, L. Bruss, Human and organization issues, The Workflow Paradigm, Future Strategies Publishing, 1994, pp. 35–49.

<sup>w</sup> <sup>x</sup> 31 W. Rupietta, Organization models for cooperative office applications. Database and expert systems applications, Proc. 5th Int. Conf., DEXA ’94, Athens, Greece, 1994.

<sup>w</sup> <sup>x</sup> 32 R. Sandhu, E.J. Coyne, C.E. Youman Eds. , Proc. 1st ACMŽ . Workshop Role-Based Access Control, 1996, ACM.

<sup>w</sup> <sup>x</sup> <sup>)</sup> 33 S. Su, Modeling integrated manufacturing data with SAM- , Computer 19 1 1986 34–49. Ž . Ž .

<sup>w</sup> <sup>x</sup> 34 K. Swenson et al., A business process environment supporting collaborative planning, J. Collab. Comput. 1 1 1994 Ž . Ž . 15–34, March.

<sup>w</sup> <sup>x</sup> 35 W. Vanderaalst, K. Vanhee, Business process redesign — a Petri-net based approach, Comput. Ind. 29 1–2 1996Ž . Ž . 15–26.

<sup>w</sup> <sup>x</sup> 36 R. Vidgen, J. Rose, T. Woodharper, BPR — the need for a methodology to revision the organization, IFIP Trans. A Comput. Sci. Technol. 54 1994 603–612.Ž .

<sup>w</sup> <sup>x</sup> 37 L. Willcocks, G. Smith, IT-enabled BPR-organizational and human-resource dimensions, J. Strategic Inf. Syst. 4 3Ž . Ž .1995 279–301.

Edward Cheng is the Director of the OCT Research Laboratory, which focuses on research in E-Commerce technologies and solutions. Prior to heading up OCT, Edward was the managing director of the Collaborative Computing Lab at Oracle, and had led the R&D team at Digital Equipment to deliver ObjectFlow, an object-oriented workflow product. In the late eighties, Edward led the engineering team at Hewlett Packard to accomplish a 2000% performance improvement on HP SQL. His research interests include process automation technology, enterprise modeling and management, fuzzy logic, high performance OLTP systems, journaling and recovery, and distributive databases. Edward is a PhD candidate at the University of London.
