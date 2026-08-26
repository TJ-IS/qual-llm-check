---
otero_id: 16927
otero_key: "N6BRABC7"
title: "Future research directions in model management"
authors: "Benn Konsynski; Ralph H Sprague"
year: "1986"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(86)90126-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Future Research Directions in Model Management

Benn KONSYNSKI $^{+}$ and

Ralph H. SPRAGUE, Jr. \*

$^{+}$ Management Information Systems, University of Arizona, Tucson, AZ 85721,

\* Decision Sciences Dept., College of Business Administration, University of Hawaii, Honolulu, HI 96822, USA

Model management is a relatively new area of research and practice in information systems. This paper reviews present problem areas and suggests opportunities for further research.

Keywords: Model management; Data management; Decision support systems

![](/api/attachments/N6BRABC7/fulltext/images/3c72fb3f48d463e5f090a53c7d7d25826ea84a5f149edd17adb871616bcd6324.jpg)

Benn Konsynski is an Associate Professor of Management Information Systems in the College of Business and Public Administration at the University of Arizona. He received his Ph.D. in computer science from Purdue University. His major research focus is computer-aided approaches to information systems design and implementation. Current research interests include model management systems, learning paradigms in decision support systems, business dialogues in distributed office environments, and design support for local area networks.

![](/api/attachments/N6BRABC7/fulltext/images/ea143632b9c19092be466d72043e185a78377d9b3db15fb437e098e8fbe81e51.jpg)

Ralph H. Sprague, Jr. is Professor and Chairman of the Decision Sciences Department at the College of Business Administration, University of Hawaii. He has over 20 years of experience in teaching, research and consulting on information systems for organizations throughout the world. He is recognized as one of the leading international experts on the subject of Decision Support Systems. He has published widely in academic and business journals and is the co-author of two books, Information Systems Management in Practice and Decision Support Systems. He is co-chairman of the annual Hawaii International Conference on Systems Sciences, which has become a forum for recent research on Model Management Systems.

## 1. Introduction

Why is model management important? Why is it being discussed and developed in the context of decision support systems? Where is it likely to go from here? These questions are the focus of this final short paper in the special issue on model management in DSS.

First we offer a historical perspective that shows the data base and model base components of DSS at the intersection of two evolving trends. We then examine how the model management philosophy is distinguished from earlier methodologies. The usual assumed objectives of certainty and consistency are re-considered. Lastly, issues of model management implementation and administration are considered. A summary of research issues is presented in Fig. 1.

## 2. Historical Perspective: Two Evolutionary Trends

DSS can be viewed as computer-based systems that lie at the intersection of two major evolutionary trends – data processing, which has yielded a significant body of knowledge about managing data, and management science, which is generating a significant body of knowledge about modeling. The confluence of these two trends forms the two major resources that decision makers interact with in the process of dealing with ill-structured problems.

Data, models, and interaction support (dialog) have become the three major components of DSS. The dialog-data-models paradigm has become a popular way to categorize the sets of capabilities required in a DSS. They derive directly from the definition that DSS are:

\- computer-based systems

\- that help decision makers

\- confront ill-structured problems

\- by providing direct access and interaction with

\- data and analysis models.

ELICITATION
Surfacing
Articulating
SPECIFICATION
Representation
Treatment of Null Values
Explanation
Templates
OPERATIONS
Generalization
Abstraction
Composition
Decomposition
ADMINISTRATION
Integrity Monitors
Verification
Validation
Analysis of Model Use
Complexity
Completeness and Consistency
MANIPULATION
Selection
Reference
Retrieval
Associative Access
Context Reference
POLICY SPECIFICATION AND ENFORCEMENT
Aesthetics
Impressions
Values Representation
Compliance

Figure 1. Model Management Research Issues.

Specifically, the set of integrated computer-based tools which form an SPSS can be viewed as consisting of:

\- a data base and software to manage it

\- a model base and software to manage it

\- a dialog system which manages the interaction between the user and the other two components.

Let us consider how the two trends have led to the data base and model base capability of DSS.

## A. The data processing evolution

There are, of course, many ways to define the stages in the evolution of data processing. For our purposes here, the following will suffice.

1. Basic data processing - characterized by stand-alone EDP jobs, mostly for transaction processing, with each program having its own files. Data handling was limited to such classic data processing functions as sorting, classifying, summarizing, etc.

2. Filament management – integrated EDP jobs for related functions, sometimes sharing files across several programs, with some attempts to develop common software for handling files (utilities), and prescribed ways to insure data security, integrity, backup, etc.

3. Data base management – a major capability of the MIS era, with particular emphasis on the software system for dealing with data separate from the programs that use it. The major impact of DBMS at this stage was reduced program maintenance, since data files could be modified without recompiling all the programs that used it. At this stage, DBMS software began to use data 'models' to represent the way data were logically related.

4. Query, report generation – the later stages of the data base approach saw the addition of flexible report generators and English-like query languages to facilitate ad hoc requests and special reports. Emphasis here was on the direct access to data bases by non-technical people such as end users. Throughout the EDP evolution, emphasis has been on manipulating data, initially in predefined ways to accomplish structured tasks, and later in flexible ways to accommodate ad hoc requests and preferences by individual users. Sophisticated ways of manipulating data (models) were embedded in the data processing system for some well-structured problems, for example inventory, but modeling was generally considered a separate type of application. Users dealt with less well-structured problems by querying the data base, getting special reports, and then using their judgment.

In general, the data base approach evolving from the EDP tradition seemed to be characterized by the following objectives.

1. To effectively manage a large amount of data.

2. To establish an independence between the data and the programs that used it.

3. To separate the physical and logical structures of data and deal with them separately.

4. To provide flexible, easy access to data by non-programmers.

The problems and limitations of this approach were related to its dominantly accounting-oriented historical data, and its focus on information flows and summaries. However, for an important set of problems and decisions, getting “the right information to the right person” was necessary but not sufficient. That data often needed to be analyzed, interpreted, and extended with the use of some decision models being developed from management science/operations research efforts.

## B. The modeling evolution

While data processing professionals were strengthening their ability to store and handle data, management scientists and operations researchers were increasing their ability to create models of a problem or situation and manipulate them to shed light on how to handle that problem. A similar sequence of evolutionary steps in the development of modeling might include the following:

1. Symbolic models - the early stages of modeling were characterized by heavy use of linear and nonlinear equations, sometimes in large sets of simultaneous equations.

2. Computers as a computational engine - the computer first became important to modeling as number crunchers to reduce large amounts of data to coefficient estimates for the equations, or as computational engines for solving sets of equations.

3. Computer models - eventually, the computer took on a subtly different role. Rather than a device to compute a mathematical model, the computer program became the model. Computer variables became the symbols which were manipulated by program operators instead of mathematical operators. This approach led to a popular class of models that were not 'solved' but rather 'run' over time to observe the behavior of the model and thus shed light on the model situation.

4. Modeling systems - the computer became so important to modeling efforts that software systems were developed to handle classes of models. The software generally provided common data input formats, similar report formats, and integrated documentation. Modeling systems for statistical programs (e.g. SPSS) and mathematical programming (e.g. MPX) are good examples

5. Interactive modeling - as computers became more available in time-sharing mode, interactive modeling became more feasible. Minicomputers and mainframes dedicated to online usage generally had libraries of models which could be called to do a variety of analyses. Unfortunately, it was common for the models to be stand-alone programs with different data requirements and formats and little if any linkage between the models.

In summary, modeling evolution led to an increasingly close relationship between the models and computers, but continued to be separate from the data which they used. This seemed to reflect model builders' preoccupation with the model as the focus of attention and their hesitance to get intimately involved with data sources and structures. In general, the modeling efforts needed major contributions from the data base efforts of systems professionals.

## C. Evolutions converge

Each of the two development tracks – in data management and in modeling – were useful in their own right. They were each significantly lacking, however, in helping decision-makers deal with ill-structured problems. Developments in decision support systems allowed each set of capabilities to begin realizing their potential. DSS extended and combined both the data base technology and the modeling technology, and gave non-technical users access to them. The data and models were intimately linked, and both were linked with the user.

Conversely, DSS makes demands on the data base and the modeling capability that were not necessary before. Specifically, DSS makes model management capabilities necessary. Without the integration requirements of DSS, modeling systems or libraries of interactive models would probably suffice. So, as the need for model management capabilities became apparent, it was the DSS builders and researchers who began working on its development.

## D. Phases of development

Early model management efforts were attempts to exploit some of the developments in data base technology and apply them to model management. Thus, early attempts were improvements to the procedural handling of models and the development of model definition languages which made it easier to build and modify models. Subsequent work sought to treat models as abstract data types so that more of the data management principles would be directly applicable.

The next phase involved development of ways to represent models (“model models” in the sense of data models) in computer form. The entity relationship approach by Blanning, and the papers by Lee and Miller and by Kimbrough, earlier in this issue, are good examples. Some of the production rule based expert system evolving from artificial intelligence work can also be viewed as a type of model representation in computer form.

The current and near future phase consists of drawing more heavily on concepts and techniques from artificial intelligence to improve the representation of models so they can be better managed. In particular, joint representation schemes that blend the data base and the model base could result from this work. As AI techniques become more embedded in DSS, enhanced data bases in the form of a knowledge base, and better ways of representing model structuring knowledge, may lead to additional convergence of the data base and model base.

## 3. Model Management Philosophy

There is a growing acceptance of the important role of models as stable, sharable entities in our traditional information systems as well as in decision support environments. In many cases, the models serve as the basis for design of the data, the processing and the user dialogues. Models are often the best repository of the domain semantics that are needed in the design and evolution of our information systems.

We design our information systems around what we perceive as the stable entities of the system. Our design methodologies seek these stable structures around which we make design decisions. In the 1960s our systems development in general was what could be characterized as a process-centered activity. We focussed on processes; data was perceived as a necessary component to the extent that it was needed to carry on certain processing activities. Our perception of stable entities in systems were the procedural elements. The focus of our design efforts was to identify and locate procedures. The management of models involved the management of libraries of solution procedures in the form of programs and subroutines. With the advent of data management, we migrated to a data-centered period in the early 1970s. We perceived that the stable entity around which we could determine design decision was data organization. Under this view, the data relations are perceived as stable, and therefore, we needed to focus on data associations for the stable structures upon which we could base our design decisions. Under this view, model management involves the maintenance of data definitions and associations using dictionaries and semantic databases.

This view is in part changing. We can expect a new centering to emerge, based on the recognition that it is not the data relations that were in fact stable, but rather the models that determined these data relations. We recognized that by pursuing a wholly data-centered approach we were neglecting those stable relationships that are associated with processes and procedures in the task environment. We are seeing a migration from the data-centered view and a recognition that the models are the sources of the assertions and assumptions that we recognize as stable. The assertions and assumptions are the stable entities that we need to base design decisions for systems upon, whether they be decision support systems or traditional information systems. We need to seek the assertions, assumptions, and policies that govern the procedures that determine the data values and data relations as well as the process structures.

## 4. Issues of Certainty and Consistency

There are often analogies drawn between the evolution of model management and data management. Although the analogy has some utility, we need to make sure that we do not fall into the various traps that data modeling and data management have fallen into. The extremes associated with mandatory certainty and consistency in data bases are one example.

Most of us were raised in areas of formal decision making and analytical analysis where we assigned major importance to issues of consistency and completeness. We need to reexamine this authority and evaluate the utility and realism offered by the support for inexactness and inconsistency. We need to accept and exploit the natural inconsistency and incompleteness that we encounter in organizations. If our information systems are to be the analogues and support environments for the problem domains of the organization, we need to reduce the fear of managing and accounting for incompleteness and inconsistency at certain levels. This does not mean that we are relaxing the demands of our information filters that preserve completeness and consistency. What we are asking for is the recognition that there are multiple levels of models that exist in our problem domain and that under different value systems, inconsistencies can arise. We need to examine where we can take advantage of the incompleteness and inconsistency that we encounter. Where can we live with it? Where can we exploit it? Where do we need to resolve it?

The author (B.K.) has worked for many years on developing tools for requirements analysis and logical systems design. We recognized long ago that systems analysts and designers fail to reach a singular, complete, and consistent statement of requirements. We recognize that in order to accomplish what is needed, you have to effectively manage incomplete and inconsistent data. It is difficult to understand why we have not recognized that inconsistency is a natural part of human decision-making activities. It will be important in future systems that we question the necessity for consistency filters. Applying consistency and completeness filters too early in the process may affect the quality of the effort through the propagation of unnecessary constraints.

## 5. Model Management Implementation and Administration

## A. Elicitation, specification, operations

In the area of model management implementation, we have suffered from a lack of tools. We need tools that allow us to elicit models, to formally represent and codify models, and to appropriately match models with problems. We need storage representations for those models and need associative access mechanisms to retrieve models. In the few attempts to develop such tools, many have adopted the knowledge representation schemes that are popular in the AI community. Many still perceive that the model base is little more than an inventory of relations and methods. Others consider the model base to be no more than an inventory of solution procedures which carry models.

The identification and elicitation of models is certainly one of the more neglected areas of study in model management. How do we effectively pursue the elicitation of models that are important in any decision-making activity? There are great opportunities for unique approaches to this elicitation and creativity process. One of the mechanisms being examined at the University of Arizona is the role of gaming and games as a means of elicitation. Approaches used for model elicitation in expert systems should also be examined for use in model management systems.

Related to the elicitation of models is the need for measures and metrics of the potency of models. In any decision-making process we might proceed ad nauseum eliciting detail on a model for a problem area. We need to seek and provide some potency metrics that will offer us a stopping criterion so that we may know when a model is good enough to serve its intended purpose.

There are many dangers in representing and codifying models. Representation and codification bring the decision-making process and associated values out into the open. One of the best security measures we have is confusion and lack of documentation. Thus, many decision makers will be concerned about the impact of the formalization of models. As usual, where there exists a danger, there is also great opportunity in allowing, and often demanding, codification and formalization. The classification and the sharing of models in organizations permit the formal review of policy support and enforcement by the organization.

Several efforts are under way to define mechanisms for the formal specification of models. The Structured Modeling effort at UCLA under A. Geoffrion is a good example of such an approach. Structured Modeling and similar efforts may accomplish for modeling what structured programming did for programming activity. There were three key elements in structured programming that were found beneficial: the concept of modularity, the top-down approach to the definition of local logic, and the acceptance of a limited control structure set. Accepting the notions of modularity in modeling and the top-down specification approach in the elicitation and communication of models, we need only seek the limited control structures that will facilitate the representation of models.

Related to research in model representation is the development of a model definition language. Such a language should accommodate graphic, tabular, as well as narrative forms of specification. User domain semantics need to be expressible in the language.

Another area of research related to model management implementation concerns the operations on models and the potential for synthesis of models, to discover new models that have not surfaced in our own patterns or our own creative processes. We can expect that these endeavors will begin with the studies of generalization, abstraction, composition and decomposition. We have the opportunity to let the systems themselves work toward facilitating some of those creative activities that we perceive to be currently uniquely human. A missing element that we have sought from the beginning of the DSS movement is that of learning and adaptation. Operations, such as those mentioned above, may prove to be the key to the introduction of learning and adaptation in our systems.

## B. Model administration

Many of the issues discussed above highlight the need and opportunity for research in model administration. Model administration differs from data administration in that models are less the representation of passive declarations than the definition of active relations and associations that govern decisions and actions in the organization. As the model administration function evolves, we will see the recognition of the separation of the model and data administration functions. Model administration will become an organizational and managerial task, while the data administration will become an operations control task.

## C. Policy specification and enforcement

Aesthetics should not be lost in our pursuit of utility in modeling activities. Aesthetics exist in the symbiotic relationship between the models that exist in organizations and the design processes that determine the support environment. Models themselves are, by definition, an analogue for the real-world phenomenon that we are examining. Thus, we need to understand the relationship of model forms and value forms. As mentioned above, models themselves are among the best reflectors, communicators, purveyors, repositories and documentors of the assertions, assumptions and the values that we hold about a phenomenon. There may, however, be concern associated with the documentation of those values. If we use models honestly and we document and communicate the values that are reflected in the models, we have both a problem and an opportunity. Models are among the best guarantors of policies. They are the best means of communicating policies within an organization from a strategic level on down through the organization.

In decision making, indeed in all problem solving, we made our biggest mistakes in the first five minutes that we examine a situation. It is after the first five minutes that we find that we have made improper assumptions or assertions about the nature and structure of the problem. Thus one facility we require in the use of models is the extension of the first five minutes. The best means of extending the first five minutes is to facilitate the reexamination of the assertions made by, and the assumptions held about the model and the model process. Tools are required to facilitate the elicitation, specification and analysis of the assertions and assumptions that are surfacing in the initial analysis of a problem situation.

For too long a time we have falsely associated precision with decision. We seek precision in our presentation and often associate precision with the utility of the result. We may find in fact that managers make decisions on the basis of impressions formed by the information and not the information as presented. Thus, model management offers us a significant opportunity to study the nature of the impression-making activity. In this view, data is merely the means of communicating the bias that we wish to make use of in the decision-making activity. Though issues of subjectivity arise, we may find that we better serve the decision process. If we believe that models are the best repositories and guarantors of the policies and values of the organization, then the models serve as filters and alerting tools for the subjective determination of impressions. The subjectivity of the filters may indeed reflect the policy and values that the organization wishes to promote.

## 6. Conclusions

Too often we impose the models that we can solve on the problems we encounter. We seek the semantics of the problem in the semantics of the solution procedures that we are promoting. Model management is an opportunity to assist in decoupling the problem semantics from the solution procedures. It is an opportunity to provide a software environment that facilitates the modeling tasks required of effective decision making.

DSS help managers and decision makers deal with ill-structured problems and situations by providing access to – and interaction with – data and models. DSS builders and researchers have adapted many of the techniques and approaches from data base technology to model base management. But both the data base and the model base have been relatively well-structured. The ability to deal with ill-structuredness has been supplied by the user. As we continue to strengthen DSS, we will be adding components to both the data base and the model base to help deal with less structured situations. The techniques and approaches from artificial intelligence will supply some of these additions, to the extent that we may see a third resource evolve – a knowledge base and a knowledge base management system. In fact, as indicated by the papers in this special issue, the current efforts in model base management seem to be leading in this direction.
