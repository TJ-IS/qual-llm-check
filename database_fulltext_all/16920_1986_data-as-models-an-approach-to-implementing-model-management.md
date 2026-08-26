---
otero_id: 16920
otero_key: "WQD9JZTS"
title: "Data as models: An approach to implementing model management"
authors: "Daniel R Dolk"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90123-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Data as Models: An Approach to Implementing Model Management

Daniel R. DOLK

Dept. of Administrative Sciences, Naval Postgraduate School, Monterey, CA 93943, USA

The concept of model management as a logical extension and parallel of data management has resulted in attempts to extend existing data models to incorporate modeling functionality. This fosters a data-oriented view which artificially restricts the domain of model management. This paper suggests that a model-oriented approach which views 'data as a model' not only expands the scope of model management but also offers a more integrated and balanced conceptual foundation from which to implement model management. On the organizational level, this approach recognizes the transition from informal modeling as exemplified by the use of spreadsheets to formal modeling which manages models as a resource in conjunction with data. The notion of information administration is introduced as an organizational mechanism for controlling this evolution. On the technological level, a generalized model management system (GMMS) is required for support of organizational modeling activities. Geoffrion's structured modeling is suggested as a foundation from which to build a model-oriented GMMS. The incorporation of artificial intelligence capabilities into a GMMS is seen as a second implementation step which require the development of a sufficiently flexible meta-level architecture. Model abstractions are introduced as a vehicle for implementing this architecture.

Keywords: Model Management; Information Administration; Model Management System; Structured Modeling; Meta-Level Architecture; Model Abstraction.

![](/api/attachments/WQD9JZTS/fulltext/images/0a657553fa04da86194e2112de32eca963800b34e4d6cf8d7b2f8564fcf4b847.jpg)

Daniel R. Dolk received the Ph.D. degree in management information systems from the University of Arizona, Tucson AZ in 1982. Since 1982, he has been with the Department of Administrative Sciences, Naval Postgraduate School, Monterey CA, where he is currently an Assistant Professor. His research interests include the application of artificial intelligence to database and model management. He is currently working on the design of dictionary/directory systems and the development of an object-oriented model management system for software engineering support. Dr. Dolk is a member of the Association for Computing Machinery, the IEEE Computer Society, the Institute of Management Sciences, and the American Association for Artificial Intelligence.

## 1. The Scope of Model Management

The concept of model management has been with us for over a decade [1]. During that time, there has been much interesting research performed but relatively little attention paid to implementation issues regarding model management. This has been largely due to a lack of sufficiently general conceptual and theoretical foundations for the discipline. This situation has been corrected recently with the emergence of two theoretical approaches, Blanning's relational theory of model management [2] and Geoffrion's structured modeling [3]. With these two frameworks as bases, the way is now paved to begin serious model management implementations. The critical issues in this process, both organizational and technological, are the subject of this paper. The major underlying assumption is that successful implementations are necessary if model management is to achieve the credibility that its supporters predict.

Before embarking on an investigation of these issues, it is necessary to examine more closely the scope of model management and its relation to data management. Historically, there has always been a duality between data and models. The information systems community has traditionally emphasized the data-oriented nature of information systems whereas the modeling community (primarily operations research and management science) has focused on the algorithmic and procedural requirements for solving models. This has perpetuated unnecessarily the notion that data and models are two distinct entities which must be treated in separate ways within information systems.

Much of the relevant literature has addressed this duality by attempting to characterize model management as a logical extension of data management. This has resulted in attempts to devise extended versions of well-known data models to encompass modeling features as well [2]. While this provides the indisputable benefit of a wide body of theoretical and practical knowledge about database management from which to draw, it is nevertheless primarily a data-oriented approach. This implicitly assumes that data are the key elements in an information system which has the unfortunate effect of subordinating models in the planning, design, and development of information systems.

One objective of this paper is to turn this emphasis on its head and consider a model-oriented alternative. Thus, we will consider data as models instead of the other way around. Our premise is that this approach not only resolves the duality between models and data but also engenders a balanced consideration of data and models in the design and implementation of information systems.

One of the major consequences of the ‘data as model’ approach is a broader scope of model management than has heretofore prevailed. We often have too limited a notion of what we mean by ‘model’ when speaking of model management. Because of its origin in the decision support community, the most common usage has typically been with regard to management science and operations research type of mathematical models. While there is no doubt that these models play an important role in support of certain decision making, this is not sufficient reason to restrict artificially model management to this domain alone. If model management is to attain significant organizational acceptance, it must accommodate models in the realm of enterprise analysis, data base design, software engineering, and information systems analysis and design.

Model management has both organizational and technological aspects and too often the former is neglected in favor of the latter. Section 2 will discuss organizational factors which seem to support the evolution of models as a resource and show how this provides the impetus for the technological dimension embodied by model management systems (MMS). Section 3 will examine the concept of a generalized MMS (GMMS) as the technological vehicle which facilitates the organizational imperative for model management. In both Sections 2 and 3, emphasis will be placed on implementation issues for incorporating model management as a distinct and identifiable organizational function. Section 4 will summarize the ideas presented and portray model management in the larger context suggested by the 'data as models' approach.

## 2. Organizational Dimension of Model Management

Modeling activity within organizations can be characterized as either informal or formal. Informal modeling is that which occurs on an unplanned, ad hoc basis, usually as the result of individual initiative. No organizational charter exists for defining or controlling this activity. The use of spreadsheets is an example of informal modeling. Formal modeling, on the other hand, is a direct result of organizational policy which defines and sanctions explicitly the modeling processes needed to support organizational planning, control, and operation. An example of formal modeling is enterprise analysis, the formulation of an overall information architecture for an organization. The organizational dimension of model management is a function of the transition from informal to formal modeling.

## 2.1. The Spreadsheet Explosion as an Informal Modeling Phenomenon

The most obvious example of informal modeling in organizations today is the widespread acceptance and use of spreadsheet programs on personal computers. While spreadsheets have been a boon for individuals in a business environment, they have become a headache at the organizational level. Increasingly we read of instances in the trade press where decisions were made or almost made on the basis of spreadsheet models which later turned out to be incorrect. The lack of guidelines for spreadsheet use has led to a quality control problem concerning the models being generated. Organizations now face the quandary of how to control the proliferation of a modeling tool which many of its employees find indispensable but which threatens the quality of decision making. In many instances, organizations are becoming aware for the first time of the role of models in decision making and the need for managing models as a resource.

One can't help being reminded of the situation existing prior to the data management era when the proliferation of file-oriented application programs caused widespread data redundancy and serious data integrity problems. The evolution of data management resulted from the organizational desire to control this situation and subsequently led to the centralization of data for the express purpose of sharing and, more importantly, controlling data. In the same way that the proliferation of application programs forced organizations to embrace data management, the proliferation of spreadsheets may force organizations to embrace model management as a mechanism for controlling the modeling resource.

## 2.2. Model Management: Formalizing Informal Modeling

Nolan's model of data processing evolution [4] hypothesizes the stages of initiation, proliferation, control, and integration. Intuitively, this appears to be an accurate description of what is happening currently with respect to the use of spreadsheets for modeling. The proliferation stage is upon us with many companies desperately looking for control mechanisms. It may very well be that the control stage will illuminate the role of models in organizational decision making and the integration stage will give rise to the formalization and implementation of model management. If this indeed turns out to be the case, this reaffirms the need to adopt a more universal view of models such as we are suggesting in the ‘data as models’ approach.

## 2.3. Enterprise Analysis as a Formal Modeling Phenomenon

The spreadsheet phenomenon is an instance of 'bottom up' modeling in the sense that there is no overall organizational charter or control over the process. If this process percolates to higher and higher levels of the organization, this may result in a 'bottom up' awareness of the importance of modeling. In other areas of endeavor, however, organizations are beginning to adopt a 'top down' approach to modeling. In particular, in the area of enterprising analysis, or information engineering, organizations are beginning to become aware of the need for high level strategic planning and modeling of information needs. This results in companies defining broad corporate goals and functional capabilities, then successively refining these to lower and lower levels of the organization. This process eventually results in an information system architecture which supports the operations and objectives of the organization at all levels.

What is conspicuously lacking in this process, however, is consideration of the kinds of models which support decision making protocols and activities. Enterprise analysis is primarily data-oriented as opposed to process-oriented [5] which results in a potentially serious imbalance.

One of the major benefits the ‘data as models’ approach offers is the potential to balance this data-oriented view. Data and models must both become part of the enterprise analysis fabric. The ability to integrate information and decision making models expands the scope and utility of each and provides a much more coordinated and balanced view of the organization. Model management has the potential not only to encompass, but also enrich, the entire enterprise analysis process.

## 2.4. Information Administration: Control of the Modeling Resource

The introduction of models into the information resource environment changes that landscape dramatically. As Fig. 1 shows, the administration and control of these resources must now take into account models in addition to hardware and data. Furthermore these models span a wide range of applications including, for example, linear programming, forecasting, enterprise analysis, software programs, database designs, and so on. The entire domain of formal modeling which the organization supports becomes part of the information administration function.

The concept of information and model administration is a significant extension of the usual notion of data and database administration and arises from the 'data as models' emphasis. The functional details of model administration are beyond the scope of this paper, however. See Dolk and Konsynski [6] for a more complete treatment of this topic.

![](/api/attachments/WQD9JZTS/fulltext/images/14d69aa0672053a26fbf3a9a3817f6c2c0fd4851b340dd06a11b1a36c0e57f3e.jpg)  
Fig. 1.

## 2.5. Summary

Historically, modeling has been a difficult concept to sell to organizations. The advent of spreadsheet programs has introduced ad hoc modeling into many organizations and forced them to acknowledge the role of the models in formal and informal decision making. This may well lead to the recognition of models as a resource that must be controlled. This provides a natural migration path to the more general concept of model management. In order for successful implementation of this concept to occur, however, a broad view of models must be adopted. In this way model management can encompass enterprise analysis as well as the more traditional decision making support.

## 3. Technological Dimension of Model Management

The realization of models as a resource will cause organizations to control, and most likely, centralize this resource. As with data, this will require management systems, both manual and automated, to support this activity. The information administration function described in Section 2 is an example of the former. In the technical sphere, a generalized model management system (GMMS) is necessary for the full support and control of the modeling function.

A generalized model management system can be thought of as an operating system for models. The primary purpose of a GMMS is to support the general description, manipulation (analysis, solution and presentation) and control (access authorization, integrity, security, and privacy) of models. Much of the MMS literature suggests a knowledge-based capability as well in order to enhance the model-user interaction, for a example [7-9]. Although this may be a desirable feature, it is not necessary requirement and may, in fact, delay implementation efforts.

Currently, no existing system qualifies as a truly general MMS in the sense described above. This section will examine aspects of MMS implementations and suggest a migration path for the development of a GMMS to correct this situation. This is seen as a two-phase process: implementing a system of comparable power to existing DBMSs but without knowledge capabilities and then expanding this to incorporate knowledge-based features as well. In particular, the structured modeling approach will be discussed as a promising foundation from which to carry out the first phase and the concept of meta-level architecture introduced as a framework for incorporating artificial intelligence techniques in the second phase.

## 3.1. Model Representation

The development of a GMMS requires a sufficiently powerful and general theory of model representation in order to proceed. Recall the pivotal role that the relational model of data played in the evolution of data management and DBMSs [10]. Without a comparable, underlying theory in the model management domain, the development of MMSs will most likely proceed in a relatively unproductive, ad hoc fashion.

The model as a stand-alone system has tended to hide the true relationship between models and data which is essential in the implementation of a GMMS. A more profitable line of research has been to extend the notion of data to include models as well. This has culminated in a relational theory of models which extends the relational theory of data to encompass (primarily mathematical) modeling functionality as well [2]. This 'models as data' approach represents an important contribution to model management research and provides a solid foundation from which to undertake GMMS implementation efforts. However, it is necessary to recognize the data-oriented nature of this approach and its potential pitfalls. An MMS based on data precepts is more likely to perpetuate the notion of models as subordinate to data than to effect a true synthesis of data and models.

A model-oriented framework which encapsulates the 'data as models' approach has recently been developed in the form of structured modeling [11]. Structured modeling is based on the assumption that the model is the essential conceptual unit and proceeds to build a framework which encompasses full modeling functionality while subsuming data functionality as well. The next subsection provides a very brief overview of structured modeling.

## 3.2. Structured modeling representation

The overall objectives of structured modeling are to provide a unified framework which promotes ‘good’ modeling practice, supports better computer-based modeling environments, and takes full advantage of data management facilities. The scope of this paper does not allow even a brief description of the technical aspects of structured modeling. The reader is best advised to consult Geoffrion’s monograph [3] for these details.

A summary of the major features is particularly relevant, however, with regard to GMMS implementation:

1. Structured modeling provides a uniform way of describing models as acyclic, attributed graphs. This is intrinsically appealing because of the wide range of applicability of such graphs, not only in management science and operations research but in database design, software engineering, and information systems design as well. Further, there is a wide body of knowledge about the properties of acyclic graphs which provides a strong theoretical foundation.

2. Structured modeling formally supports the notion of user views. Different levels of abstraction of a model can be specified easily while still preserving acyclicity. This allows the user to conceptualize and interact with models at a level which is meaningful rather than being restricted to a single, prescribed view imposed by unrelenting software systems.

3. Geoffrion claims that structured modeling is more general than the relational model [1]. If this is true, then a GMMS implementation based on this framework should be able to provide full DBMS functionality.

4. A structured modeling implementation exists which connects model schemas (i.e., acyclic graphs represented in a model description language) with existing linear programming solution algorithms [11]. Thus, traditional OR optimization can be applied to these model descriptions.

The structured modeling framework shows the difference between 'data as models' versus 'models as data' to be more than semantic nitpicking. The latter approach, as embodied in the relational theory of model management, must extend existing data models and show that the resultant extension accommodates modeling functionality. This, in effect, amounts to 'value adding' to a relational, or comparably powerful, system. The former approach, as embodied in structured modeling, provides full modeling functionality but then must show that this encompasses data functionality as well. Preliminary indications are that structured modeling has a much higher semantic expressiveness for describing models than does the extended relational approach. It remains to be seen, however, whether structured modeling can provide a data management environment equivalent in power and flexibility to relational systems.

At this point, it is much too early to be trumpeting the superiority of one approach over the other. The important factor is that the emergence of these two theories provides a strong foundation from which to begin implementation of MMS's which are comparable in generality to current DBMS's. It is this process which will reveal the relative strengths and weaknesses of the two approaches.

## 3.3. Artificial Intelligence and MMS

Concurrent with the increasing interest in model management has been the phenomenal rise in popularity of artificial intelligence technology. In the space of a few short years, expert systems have progressed from experimental curiosities to operational systems in industry. As a result of these trends, it is reasonable to expect a strong demand for merging expert systems with modeling applications to enhance the decision making utility of the latter. This will eventually lead to embedding knowledge-based capabilities within MMSs in order to support this interface.

Many researchers have recognized from the outset that the ultimate payoff of an MMS is in the area of decision support and therefore much of the conceptual work in the MMS area has been involved with deriving knowledge representations suited for modeling applications. Although this has resulted in interesting research, it has probably tended to retard the implementation of a generalized MMS. Successful AI implementations have largely been confined to very domain-specific applications and attempts to generalize knowledge-based processing beyond this scope have floundered because of exceedingly difficult problems with complexity and knowledge representation. Implementing a GMMS with generalized knowledge processing capabilities is significantly more difficult than a GMMS without such capabilities.

## 3.3.1. Meta-Level Architecture

The building of expert systems has clearly become an active area of research and development in AI, especially within the last five years. Acquiring knowledge and then structuring it in a fashion which facilitates efficient inferences are two problems which, until recently, have been approached on a case-by-case basis. The inefficiency of this approach has become evident and more generalized techniques for building expert systems are being considered. The term most often used to describe these techniques is meta-level architecture [12].

Meta-level architecture in AI environments refers to knowledge about knowledge and how to manipulate that knowledge in a reasonably efficient manner. These meta-levels of knowledge are required to generalize the process of acquiring and structuring knowledge at the lower level so that expert systems can be designed and implemented in a general way rather than by the ad hoc methodology previously used.

In its simplest form, meta-level architecture makes the distinction between 'base-level' and 'meta-level' activities (Fig. 2). Base-level actions are those which are performed in some predeterminated sequence in order to attain some goal. Meta-level actions are those which determine what base-level actions need to be performed, and in which sequence, in order to attain some goal. In a relational database system, for example, storing data and retrieving data are base-level actions. Query optimization to find the most efficient sequence of data retrievals which satisfy a given query is an example of a meta-level action. In general, the meta-level actions dynamically determine the base-level behavior which must be exhibited to solve a given problem. In a meta-level architecture, meta-levels may themselves become base-levels for even higher meta-levels of knowledge. A knowledge base which reasoned about the control structure governing query optimization and changed that structure dynamically would be an example of a meta-meta-level. One of the important features of a meta-level architecture is that regardless of which level is the current meta-level and which is the current base-level, the same inference technique can be applied to perform the requisite reasoning.

![](/api/attachments/WQD9JZTS/fulltext/images/24f990d473415b304b238b89a7d9d8f0fdbd89fce36a88b2c0b2150bf0dfd492.jpg)  
Fig. 2.

The potential advantages of meta-level architecture include:

![](/api/attachments/WQD9JZTS/fulltext/images/38110dc09d7044fc22ed82a7f04c710f88d662395b9ef088ea02df0b94e20657.jpg)  
Fig. 3.

1. The explanation of behavior: if the meta-level component determines the behavior of the base-level components, then clearly it should be able to document that behavior.

2. The facilitation of knowledge acquisition: the meta-level level activity potentially should be able to derive new rules from the existing rules in the knowledge base.

3. The facilitation of conceptual knowledge acquisition: an intelligent meta-level processor should theoretically be able to 'learn' and subsequently apply new conceptual primitives.

4. The implementation of strategies: meta-level processes must have knowledge about how and when to use various base-level activities to solve a particular problem.

The above advantages are still theoretical in many cases but the concept of meta-level architecture supplies a framework for thinking generally about how to structure artificial intelligence applications.

A GMMS must be able to support meta-level architecture to avoid an ad hoc approach to implementing knowledge-based capabilities. Some examples of meta-level activities in an MMS include:

1. Query decomposition: An MMS must decompose a query into the appropriate sequence of data retrievals and model invocations; Bonczek et al. [13] have shown how the resolution process can be applied to perform this decomposition.

2. Model invocation: An MMS must be able to convert data from existing representations into the representation required by a solution or evaluation algorithm.

3. Meta-data: An MMS must maintain or have access to a resource dictionary/encyclopedia which is an inventory of the modeling environment including data, models, users, programs, hardware and the subsequent relationships among them.

4. Model integration: An MMS must know how to link models to build composite models and, conversely, how to decompose models into their constituent parts.

5. Splicing expert systems with MMSs: An MMS requires knowledge about models and modeling domains.

## 3.3.2. Abstractions as Meta-level Structures

The ability to support meta-level architecture in a GMMS requires knowledge representation in addition to model representation. The model representation used in the extended relational and structured modeling approaches does not provide knowledge capabilities. A more elaborate representation is required. One potential candidate is the model abstraction in $[8]$ which is based on object-oriented programming abstractions but represented in first-order predicate calculus. A model abstraction for the standard transportation model is shown in Fig. 3.

Abstractions have similar properties to frames yet retain the advantages of the first-order predicate calculus formalism. This flexibility may be suitable for accommodating the versatile search strategies required for meta-level architecture. In this context, abstractions must also be able to represent knowledge representation structures (e.g., rule structures) in order to satisfy full meta-level functionality. Investigation of these problems is a separate research issue. One promising approach is combining structured modeling constructs with abstraction representations.

## 3.4. Summary

The GMMS is the technological vehicle for supporting organizational model management. Structured modeling and the extended relational approaches to model representation are two viable theoretical bases from which GMMSs can be built. The first phase of GMMS implementation should be to build a system based on these frameworks which is comparable in generality to existing DBMS products.

Implementing artificial intelligence capabilities in a GMMS is a more demanding task and should be undertaken within the framework of a meta-level architecture. This presumes the existence of a GMMS from phase one which can provide the base-level processes. More research is required on knowledge representations for supporting meta-level architecture. Until a meta-level framework evolves, however, AI applications in a model management environment will most likely proceed in an ad hoc fashion.

## 4. Model Management as a Paradigm

Information processing in today's world is primarily data-driven. Propagation of the decision support approach towards information processing requires a new role for model management, one that includes models as an integral component in addition to data. In particular, the view of this paper has been that data should be considered as models and subsequently model management should supplant data management because it provides a more balanced approach. Organizationally, this requires the recognition of models as a resource and the concomitant need for information administration. Technologically, this requires generalized model management systems which have the functional capabilities of current DBMSs and provide full modeling features as well. Model management is the discipline which must further the domain of decision support and eventually extend our notions of what information processing entails.

## References

[1] Will, H. Model Management Systems, Information Systems and Organization Structure, ed. by E. Grochla, and

N. Syzperski, Eds., pp. 467–82 Walter deGruyter, New York (1975).

[2] Blanning, R., A Relational Theory of Model Management, Working Paper No. 85–106, Owen Graduate School of Management, Vanderbilt University, Nashville TN (1985).

[3] Geoffrion, A., Structured Modeling, UCLA Graduate School of Management (Jan. 1985).

[4] Nolan, R., Managing the computer resource: A stage hypothesis, Commun. ACM 16 (1973) 399–405.

[5] Martin, J. and C. Finkelstein, Information Engineering, Savant Institute (1983).

[6] Dolk, D. and B. Konsynski, Model management in organizations, Information and Management 9 (Aug. 1985) 35–47.

[7] Elam, J., J. Henderson, and L. Miller, Model management systems: An approach to decision support in complex organizations. Proc. 1st Int. Conf. Information Systems, Philadelphia PA, pp. 98–110 (Dec. 1980).

[8] Dolk, D. and B. Konsynski, Knowledge representation for model management systems. IEEE Trans. Software Engineer. SE-10 (1984) 619–627.

[9] Bonczek, R., C. Holsapple, and A. Whinston, Foundations of Decision Support Systems, Academic Press, New York (1983).

[10] Codd, E., A relational model for large shared data banks. Commun. ACM'13 (June 1970) no. 6.

[11] Clemence, Jr., R., A Structured Modeling System for Optimization, Master's Thesis. Naval Postgraduate School, Monterey CA (June 1984).

[12] Davis, R., Meta-rules: Reasoning about control. Artific. Intell. 15 (1980) 179–221.

[13] Bonczek, R., C. Holsapple, and A. Whinston, A generalized decision support system using predicate calculus network data base management, Operations Res. 29 (1981) 263–281.
