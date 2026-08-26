---
otero_id: 16971
otero_key: "DNBK37SM"
title: "Relations between specific decision support systems"
authors: "A. Bosman"
year: "1987"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(87)90176-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Relations Between Specific Decision Support Systems

A. BOSMAN

University of Groningen, 9700 AV Groningen, The Netherlands

The means for support of decision-makers are defined in the domain of decision support systems generator. We describe the main components of such a generator and give a critical review. There are two main points of critique. The modelling facilities are restricted and there is a lack of facilities to interconnect models. Proposals are discussed to increase the effectiveness of decision support systems generators. One of these proposals is to create a network of specific decision support systems.

![](/api/attachments/DNBK37SM/fulltext/images/6a8e3e8b1792d438e5162788cb97e5a9788c331b59ff1c36bd5bf375fdcdeac6.jpg)

Aart Bosman is a Professor in the department of business administration and management sciences – economic faculty, University of Groningen, The Netherlands. Studied economics and has a doctorate in economics. Primary teaching interest is in management information systems. Research interests are the role of decision support systems, including expert systems, in organization theory and practice. Is the author/co-author of a number of books – in Dutch – on organization theory, marketing and information systems. Author and co-author (with Henk G. Sol) of a number of articles in the publications of IFIP and North-Holland on information and decision support systems.

## 1. Introduction

A continuous discussion is going on about the topic of decision making. This discussion is the result of a number of factors. The most important factor is the cognitive constraints of men. We cannot recognize a problem at once and if we do, we cannot define it in a proper way without the assistance of various instruments. The instruments we use are procedures to transfer data into information. Most of these procedures are simple and are used interconnectedly. Furthermore, to solve a problem we divide it into parts and try to solve these separately. This approach of problem solving and the application of the division of labour are the two main reasons for the existence of organizations.

Although the division of a problem to find solutions is rather common, this approach has its disadvantages.

(1) Generally and often implicitly it introduces the assumption that the parts into which the problem has been divided are independent. In science it is customary to deal with one of the parts and assume that when this part has been solved, this will also be the case for the rest of the problem. We will discuss this point seen from the point of view of decision making and decision support systems (DSS) in section 2.

(2) There is a lack of procedures that interrelates parts of a problem, especially in the domain of organizational problems. In organizations and organization science the combination of interrelations and decision making is described with the term: coordination problem. We discuss this problem in section 3. It is our hypothesis that 'normal procedures' applied in DSS are inclined to aggravate possible solutions of the coordination problem instead of solving it. In section 4 we discuss procedures to improve the possibilities to describe interrelationships between parts of problems and thus find a better solution for the coordination problem. In section 5 we discuss the connection between management information systems (IS) and DSS and we end this chapter with drawing some conclusions.

Various fields of science are concerned with the delivery of procedures that can solve parts of a decision problem, see, e.g., Vazsonyi [1982]. In this chapter we assume that these files can be integrated in the domain of DSS. This assumption is open to discussion, see Bosman [1987]. The discussion does not have a direct effect on the conclusions we draw in this chapter.

## 2. Decision Support Systems

Sprague and Carlson [1982, p. 12] make a distinction between specific DSS applications, resulting in specific DSS (SDSS), a DSS generator and DSS tools. A DSS generator is defined as: 'a 'package' of related hardware and software which provides a set of capabilities to build specific DSS quickly and easily'. A DSS generator is generally described by its components. Sprague and Carlson distinguish three components, viz. a data base system, a model base system and a dialog system. Bonczek et al. [1981] distinguish as components, a language system, a problem-processing system and a knowledge system. Belew [1985, p. 147] adds to the three components mentioned by Sprague and Carlson two others, viz. a textbase and a rule based system.

We agree with Sol [1985] when he points out: 'It is remarkable that the term DSS is much used without a very strict definition of its content. Many writers seem to approach DSS as a philosophy to seek a useful complementarity between technological tools and human judgement and discretion'. The distinction between a DSS generator and SDSS made by Sprague and Carlson is a relevant one, because much of the confusion Sol sketched, is the result of not making a distinction between generators and SDSS. A larger part of DSS literature deals with the components of a DSS generator and not with the problems SDSS create and the possibilities they offer. As the development of DSS generators is mainly determined by technology, a generator can easily become a constraint when developing SDSS. This is not a reproach in the direction of the technology, but more attention should be paid to the relevance of the relations between components of DSS generators and the construction of SDSS.

The ultimate goal of DSS is to increase effectiveness and efficiency of decision making in organizations with the help of data processing systems. As the existence of cognitive constraints is one of the main hindrances in decision making we direct our attention to the relations between cognition and the components of DSS generators. To do so, it is necessary to describe the essence of the process of decision making. The lack of such a description and the variety in the descriptions used, are the main reasons for the confusion in the discussion about decision making and the role DSS should play, see Sage et al. [1983] and Bosman [1987]. In accordance with Simon [1960] we divide the decision making process into three phases, see fig. 1. In phase one: Intelligence, a problem is recognized. In phase two: Design, the problem is described and an analysis conducted to be able to generate alternatives for the solution of the problem. In phase three: Choice from the alternatives is made and the outcome of the process is a decision. The division of labour and a divided problem have as a consequence that decision processes can be regarded as separate, although interconnected, elements. The elements are interconnected through formal and informal communication devices. Data processing facilities are the most important component of the formal communication devices and the in- and output devices are delivering decisions or instructions for the execution derived from decisions. Most decision processes are delivering refinements of other decision processes by adding in most cases more details. We do not assume, as, e.g., Sprague and Carlson [1982, p. 27], that execution of a decision is part of a decision process. We regard the execution of decisions as separate processes.

![](/api/attachments/DNBK37SM/fulltext/images/d3732458383241ff55a49b1477a88b4e9b35ba73bd2920e77bd485fef634919e.jpg)  
Fig. 1. Description of a decision process.

Of course, the final goal of decision making is the execution of a decision. As different decision processes can be related with one decision we have to connect these processes to be able to realize the final goal, viz. the execution of a decision. In fig. 2 we give a sketch of relations between decision processes, where each decision process is represented by one box. The relation with the execution can be constructed along two ways. One way described by A in fig. 2, where the decisions of two processes, 1.1 and 1.2, lead to the execution of these decisions. The other way, described by B in fig. 2, is the introduction of a separate decision process, process 3, to start and accompany the execution of a decision. Examples of process 3 are dispatching, control processes or a combination of both. As planning can be regarded as a decision process, control processes are a ‘natural’ extension of decision processes as far as the execution of a decision is concerned. The distinction between planning and control can be regarded as one of the ways we implement the philosophy of dividing problems into parts in organizations. The connections between processes can consist of various forms and directions, as can be seen in the next section.

In fig. 3, taken from Stohr [1983, p. 312], we depict the main components of a DSS generator. The components of a DSS generator offer a decision-maker support through facilities like

\- a query language and a data base management system (DBMS);

![](/api/attachments/DNBK37SM/fulltext/images/d83943242b8d84cb459c7f18c6bda448c8e32b301702a96d8b983b9abc406cbf.jpg)  
Fig. 2. Relations between decision processes.

![](/api/attachments/DNBK37SM/fulltext/images/3725e11ffcc996e4b5b2981b1837f95e59ca2dd175c3ebd867f607199b7e82b9.jpg)  
Fig. 3. The components of a DSS generator.

\- statistical methods to relate variables with data and to detect interrelations between variables;

\- modelling techniques to assist in formulating a problem and finding a solution;

\- user interfaces, query and modelling language to help unexperienced decision-makers use the system and formulate a problem or parts of it;
- cognitive aids to help the decision-maker to formulate his problem and use the other components of the DSS generator. Such a cognitive aid can be a separate component of a DSS generator, as Bonczek et al. [1981] propose by introducing a problem-processing system as part of the DSS generator. A separate component in the form of a cognitive aid does not mean that the other components of the DSS generator are not also in one way or another engaged with cognitive support. In case of a specific cognitive component, emphasis should be on giving assistance in defining the problem.

Cognitive support is not easily defined and can be implemented along different ways. We use the following quotation from Stohr [1983, p. 311] as an illustration. He remarks: 'At a more detailed level some objectives of a cognitive aid might be: (1) To aid the decision-making process by extending human memory and computational capabilities. (2) To 'externalize' the judgement process by making the structural elements – goals and means to achieve them – explicit. (3) To guide decisionmaking by encouraging a systematic approach and providing cues suggestive of new alternatives and goals to be considered by decision-makers. (4) To record the interaction process so that back-tracking and historic records are possible. (5) To process and combine subjective evaluations made by different participants in the decision-making process'.

Regarding the state of the art in the DSS domain a number of critical remarks can be made, especially when we look at the deliverance of cognitive aids by DSS generators.

(1) As already stated in the introduction, decision-makers use procedures to transform data into information. These procedures can be divided into two classes, viz. the formal and the informal one. The modelling facilities in DSS generators are directed at the formal procedures. Most of these facilities deliver analytical algorithms to make a choice. The set of alternatives is regarded as given. However, most decisions are made by using informal procedures. When we compare these procedures with the sequence of phases within the decision process in fig. 1, we observe that in many cases various phases of the decision process, especially phase one and two, are taken together and that in even more cases phases are separated just through the passing of time. With a little exaggeration one could say that DSS modelling facilities are adjusted to the needs in a certain phase: the third one. As the number of alternatives using informal procedures generated in the second phase is small, there is no great need for a choice mechanism.

To increase the effectiveness of DSS model components as cognitive aids the following steps should be taken.

(a) Get rid of the idea that there is only one model – in literature often called the DSS model – that describes all three phases of the decision process. We should develop models for every part of the decision process and find ways to connect these models, if necessary. In some cases a model of a decision process can consist of just one or two phases of the process as is the case with control processes, see fig. 2. Control processes with emphasis on feedback systems with a closed loop structure cannot be regarded as a model of a whole decision process, because the second phase is lacking.

(b) Stress the importance of informal procedures. To do this we should pay more attention to the possibilities of constructing descriptive models. Decision-makers should be assisted with description of their decision processes. To be able to do this we need another modelling mechanism, see section 3, apart from the ones available in the model base component of many DSS generators. Belew is also referring to this point when he introduces a rule based system. Bosman and Sol [1985] propose to use as a common denominator for these other models the term process model. As they [1985, p. 90] remark: 'Process models make it possible to open the black-box way of describing problems. By opening this black-box we are able to specify the language system, the knowledge system and the problem-processing system of individual decision-makers. As to the construction of a conceptual model of an individual decision-maker, we have to describe how scenario's of entities with their attributes are actualized. We may, e.g., specify various psychological types of decision-makers in a multidisciplinary way by introducing entities with corresponding attributes and scenario's for processing data and making decisions'.

(c) Construct models for the second phase of the decision process. The construction of expert systems as process models, is an example of what can be done. Expert systems, however, are covering only part of the second phase, see fig. 1. This cover from decision processing point of view is not really adequate, because the number of alternatives produced is small with no guarantee that the best alternative available in the system has been delivered.

(2) Data bases consist of data of a quantitative, financial, nature gathered and stored through formal procedures. Data relevant to the search of alternatives, e.g., data on alternatives not chosen in the past, are generally not available in the data base. Along with the construction of descriptive models and in combination with efficient search procedures more of these ‘qualitative’ data should be gathered and stored.

(3) Data processing in organizations can be characterized by summarizing or aggregating data. Summarizing is the result of the way we structure organizations and as a part of that structure the ways in which decision processes are interconnected. As Sage et al. [1983, p. 133] conclude: 'often it will be necessary to summarize information due to the complexity of the information, to enable viewing many bits of information in a restricted time interval or for other reasons'. However, aggregating results in a loss of information and it is not plausible to assume that these losses are in all cases compensated by the gains of the efficiency in data processing, see also point 6.

(4) The components of DSS generators are interconnected by interfaces. Next to the fact that not all components are effective as cognitive aids, there is a constraint through the kind of interconnections that interfaces allow. In many cases it is not possible to access data directly from a model base, nor can different models easily be connected. The possibilities to connect different components of DSS generators can and should be increased, see section 5.

(5) We should teach students and decision-makers how to use process models as a carrier for expressing their thoughts, especially their information procedures on decision making. When DSS applications are taught, nearly all model specifications are in equation form with rule based systems as an exception. As cognitive aids equation models can be dangerous, especially when applied by decision-makers without much knowledge of model construction procedures.

(6) DSS generators are mainly constructed to support individual decision-makers. However, as depicted in fig. 2, decision processes are interconnected and depending on the way these interconnections are, specified formally or informally, the problem specification of a decision-maker will change and as a result the procedures he used to find a solution. Most of the formal procedures we apply to assist decision-makers were constructed in a period of time when we did not have the possibilities modern computer systems offer. It is, therefore, not correct to regard existing formal and informal procedures for description of interrelations between decision processes as the only feasible instruments to specify relationships. Regarding the strong relationship between the way in which decision processes are coupled and the manner in which decision-makers define their problems, DSS generators should have facilities, e.g., as a part of a cognitive aid component, to provide information about these relationships and the possible consequences for the organization of changing these.

## 3. Coordination

Because of the division of labour every production process in an organization is divided into a great number of tasks. To realize the execution of production processes in a feasible way the execution of tasks in a production process and the decision processes related to this execution should be coordinated. The coordination problem can be roughly described when giving answers to the questions

\- how to specify decision processes and
- how to interconnect these processes?

As shown in section 2 the answers to both questions are related to each other. Therefore, in every attempt to define decision support, we will be confronted, implicitly or explicitly, with the coordination problem. Stohr [1983, p. 313] also stresses this point when he remarks ‘Organizational structures and processes impose a need for coordination of activities and the decisions leading to these activities. Responsibilities are divided and role relationships complex. Each individual will have 'local' knowledge not available to others. The budgeting and planning processes of large organizations require cooperative decision-making by hundreds of individuals and are prime candidates for computer-assistance'.

The coordination problem is solved using various instruments, which are applied simultaneously. The main instruments are

\- the organizational structure, which divides the organization in parts on the basis of functions or decision processes. The result is a hierarchical system, that can be characterized as nearly decomposable or loosely coupled [for an elaborate exposure on the relevance of organizational structure and a solution of the coordination problem, see Mintzberg [1983]];

\- formal procedures, such as the ones of planning and control, procedures for input, output, processing and storage of data; procedures for the allocation of resources, etc.;

\- informal procedures that enable a distinction between individual and group decision making. It is our hypotheses that group decision making procedures can be regarded as one of the main instruments to solve part of the coordination problem.

When discussing the coordination problem it is common to distinguish two more or less separate parts. These parts are: the influence of the organizational structure on the solution of the coordination problem and the role and functions of formal procedures, especially the ones of planning and control, for the solution of the coordination problem. In the organization literature the first part is generally described using the term macro-organizational research and the second with the word micro-organizational research, see Pondy and Mitroff [1979]. If we look at decision support facilities that can be used to assist in finding solutions for the coordination problem emphasis has been on the micro branch, especially on models that can be used for planning and control.

A survey of the planning literature can be given using the distinction made in table 1. Organizations are divided into parts. These parts are constructed by a division in a horizontal and a vertical direction. In the vertical direction subsystems are created by grouping tasks by means of functions. In the horizontal direction the organization is divided into levels. Well-known is the division into a strategic, an administrative and an operational level. On one level one can coordinate the various functions distinguished at that level. The coordination, especially relevant for the organization as a 'whole' system, has to be implemented by the construction of relations between levels.

Table 1  
Various descriptions of the coordination problem.

<table><tr><td></td><td>prescriptive</td><td>descriptive</td></tr><tr><td>one level</td><td>(1)</td><td>(3)</td></tr><tr><td>more levels</td><td>(2)</td><td>(4)</td></tr></table>

Prescriptive models of planning deliver algorithms to make a choice between alternatives. Descriptive models offer facilities to describe and define the planning problem, without giving a guarantee that a solution or a good solution can be found. Descriptive models are the models we use in the first part of the second phase of the decision process, see fig. 1. Prescriptive models deliver a great deal of the facilities of the model base of DSS generators. These are the models of management science and operations research and most of them can be situated in element (1) of table 1. Multilevel models of a prescriptive nature – element (2) in table 1 – are available for specific applications. Examples are the two level procedures like the Dantzig–Wolfe method, the Benders method and Lagrangean decomposition. The main disadvantage of prescriptive models is that they assume that the relevant alternatives are known. Therefore, prescriptive models are used especially for the solution of problems at the lower levels of the organizational structure.

The variety of descriptive models is great, especially because of the construction of SDSS. Most of these models can be situated in element (3) of table 1. Two classes of models in element (3) should be distinguished. One class are the corporate models. We define a corporate model as the most aggregate model an organization uses to describe and define the behavior of the organization. The financial report of an organization, in the form of a balance sheet and a profit and loss statement, is the best known corporate model of the organization. Other corporate models can be and are developed, see Rosenkranz [1979]. We distinguish corporate models as a separate class because they are a necessity for the solution of the coordination problem. The main arguments for this statement are:

(1) The formulation of the relevant aspects of the coordination problem should include the highest level of the organization, because at that level the problem arises and/or should be solved.

(2) Descriptions of a problem are necessary to define the problem and try to find solutions. The generation of alternatives without a description of a problem is, seen from a methodological point of view, sheer nonsense.

(3) A corporate model introduces the possibilities to describe the effect of exogenous variables that determine the behavior of an organization. Since a financial report consists of identities it is not possible to give a description using exogenous variables to explain the behavior of an organization. Econometric models are to be preferred to give such an explanation. Econometric models have the advantage that efficient and effective procedures are available to estimate the influence of exogenous variables. For an application, see Dikkers [1982].

The other class of models in element (3) of table 1 are the one level descriptive models used for the formulation of problems at other than the highest level of the organization. This can be a simulation model of a queuing problem, a scenario-analysis using a spreadsheet program or an econometric model specifying the relevant exogenous variables in a demand equation. Models in element (4) of table 1 are rare and showing that we generally assume that we can describe and solve coordination problems at one level of the organization. To describe problems at higher levels of the organization we use aggregation. However, aggregation results in loss of information, information that can be relevant for the description of problems at higher levels, see Sol [1982,1985].

Summarizing the relevant features of planning models for the solution of the coordination problem, these features are:

(1) Algorithms to produce solutions. Using mathematical programming as an example a planning problem can be described and a solution found, through

$$
A _ {p} y \leqslant x,\tag{3.1}
$$

$$
p y = z \rightarrow \max,
$$

where

$A_{p} =$ is a matrix with coefficients specifying alternatives;

$y =$ is a vector of endogenous variables;

$p =$ is a vector of coefficients in the objective function;

x = is a vector of exogenous variables;

z = the outcome of the objective function.

(2) Descriptive specifications.

$$
\overline {{A}} x = y,\tag{3.2}
$$

where $\bar{A}=$ a matrix of simultaneously estimated coefficients.

$$
A x = y,\tag{3.3}
$$

where A = a matrix of coefficients whose values are assumed, and/or directly calculated and/or estimated separately.

Most models used in the DSS domain are of type (3.3). A simulation model can also be regarded as a specimen of type (3.3) in which case the vectors of exogenous and endogenous variables consist of stochastic variables. In a number of cases (3.2) and/or (3.3) can be integrated in (3.1), but this is certainly not a standard procedure.

The coordination problem is and can be described and defined in various ways. As far as the facilities of decision support are concerned emphasis has been on the support of individual and group decision making with planning models relating to one level of the organization. If we want to improve the support of decision making processes, especially with regard to the coordination problem, certain facilities of DSS generators have to be extended. We will mention two of these facilities in this paper. The two facilities we consider to be relevant are:

(1) Improvement of the methods to describe problems and the relations between problems. In modelling we generally use equation models for the descriptions of problems, see (3.1), (3.2) and (3.3). These descriptions can be useful, but they are difficult to apply in the case of describing processes, because the coefficients of an equation only specify the influence of the exogenous variables. These coefficients do not give a description of the process of determination of the values of the exogenous variables nor do they explain the 'why' of the influence. In many cases we are interested in the functioning of processes. This is obvious in the case of formal procedures that are specified by the organization. In the case of informal procedures we are interested because these procedures can have a great deal of influence on the behavior of an organization, e.g., by means of the knowledge that is available in the organization. Such a knowledge can be incorporated in the heuristic decision rules used in the organization or in informal procedures referring to the expertise in an organization on certain problems. Rule based systems, e.g., expert systems, deliver descriptions of such processes. We must invest in modelling facilities to describe processes in organizations. Process models can be used for this purpose and it is of great important that we find adequate ways to relate equation and process models.

Process models differ on certain points from equation models. The main differences are

(a) The way in which the interconnection between parts (equations) are defined. In equation models variables are exogenous and endogenous, the extent to which they are interdependent is specified by the coefficients. In process models the dependence is sequentially specified. Using graph theory this dependency can be translated into matrix specifications for a number of cases.

(b) Process models generally give a description of the way an exogenous, instrumental, variable is determined. This specification can be important because the value of the exogenous variable is relevant for the estimation of the coefficients in (3.2). It opens a possibility to connect both kinds of models.

Our modelling facilities are concentrated on one level specifications with a striking lack of adequate corporate models. Process models should offer possibilities to describe the relations between problems at different levels of an organization.

(2) We believe that the use of aggregation in data processing, see section 2, is one of the most important reasons for the customary procedures to define coordination problems at one level of an organization. As already remarked, the assumption that an organization is a system can be accepted only if there is an interrelation between the levels of an organization. However, using aggregation in data processing means that the interrelation between levels is only in one direction, viz. bottom-up. Sol [1982, 1985a] found that aggregation can have as result that certain problems at a lower level of an organization are not discovered at a higher level of the organization. For an adequate description of problems at all levels of the organization and to be able to interconnect problems at different levels it will be necessary to construct relations bottom-up and top-down, meaning that it must be possible to disaggregate data specifications.

## 4. Coordination and (Dis)aggregation

Applications of computers on a large scale for decision support will bring changes in the relations between decision processes, see fig. 2. These changes are necessary because

\- if the process of creating alternatives is elaborated it will be necessary for decision-makers to have some knowledge about alternatives chosen at other levels of the organization;

\- models used to specify alternatives are in general only applied to describe alternatives on one level of the organization. Aggregation is used to create interdependence between levels, but aggregation does not always succeed in doing so in an adequate way;

\- models like (3.1), see section 3, can define alternatives. However, they have the disadvantage that disaggregation is not always possible and if it is, the models are growing large-and difficult to manipulate.

Various relations between decision processes can be constructed when we take the following two measures simultaneously:

(1) Data base facilities create the possibility to disaggregate. When building models we should make more use of this possibility, especially when we are confronted with the fact that the modelling process using equation models does not adequately describe the problem, e.g., if the problem cannot be explained and/or if instrumental variables are lacking. In such a case one can develop a model describing the procedures at a lower level of the organization that determine the values of the exogenous variables in the problem specification. With a sample of data – gathered by means of disaggregation – a specification and simulation of the procedures can be produced that opens the possibility to investigate whether aggregation of data was feasible and if not, to redefine the problem and define the relevant relations between the two levels. (For a more detailed exposure, see Sol [1982], for an application, see Hayes and Clark [1985]).

![](/api/attachments/DNBK37SM/fulltext/images/8f8f83d76fd29627a43be26c827565c5ca2bfe6315b0c5694aeda4efc6efc680.jpg)  
Fig. 4. Relations between decision processes.

(2) Instead of using disaggregation incidentally one could design a systematic way to relate various decision making processes in organizations. This can be realized by offering the possibility to integrate the output of SDSS in models with a specification directed at coordination. Such an approach demands the specification and the construction of relations between SDSS models. A structure defining relations with a possibility to take into account coordination is given in fig. 4. The main attributes of this structure are:

(a) It has as final output the profit and loss accounts and the balance sheet of an organization. We think this is a must because the financial report is the corporate model every organization uses and considering its relevance it must be possible to translate the result of formal planning procedures into financial variables.

(b) We consider the possibility to break the barrier created by the money veil in every organization as a main feature of the structure in fig. 4. The money veil, as a result of the aggregation procedures, makes it impossible to disaggregate to the lowest level of the organization because on account of the aggregation the data applied in decision making procedures at the lowest level are lost. At the lowest level the relevant variables of decision making are not defined in monetary terms but in physical dimensions. They are aggregated using prices as a common denominator. The most obvious example of the money veil are cost data. The cost function used is defined as

$$
c _ {t j} = c _ {v j} \cdot x _ {j} + c _ {f},\tag{4.1}
$$

where

$c_{ij}$ = total cost of the production of a certain quantity of product j;

$c_{vj} = \text{variable cost of the production of product } j;$

$x_{j} =$ production quantity of product $j$ ;

$c_{f} =$ fixed cost.

Both, $c_{vj}$ and $c_{f}$ , are determined by the combination of quantities of the production factors used for the production and their prices. Given (4.1) it is impossible to disaggregate this function and to determine which factors (variables) changed both coefficients. This means that

\- cost figures cannot be used to specify alternative productions functions, they can only be used to compare various production functions. Cost figures derived from functions as (4.1) cannot be applied as parameters in decision processes for the determination of applying certain quantities of production factors;

\- it is generally impossible to connect planning models and SDSS models with cost models, especially when they have an accounting background, because planning models deal with variables with a physical dimension. To be able to connect SDSS it is necessary to interconnect planning models with cost models. A way to realize such a connection is presented in Bosman and Bouma [1976]. Such a connection can be realized if it is possible to disaggregate functions as (4.1) in quantity and price factors. In the case of cost functions this can be done applying a production function as (4.2)

$$
x _ {j} = a _ {1} q _ {1} + a _ {2} q _ {2} + \dots + a _ {n} q _ {n},\tag{4.2}
$$

where

$x_{j} =$ the quantity of product $j$ to produce in a certain period of time;

$a_{i}$ = the technical coefficient, the quantity of production factor i, $i=1,\ldots,n$ , necessary to produce one unit of j;

$q_{i}$ = the quantity of production factor i necessary to produce quantity $x_{j}$ .

(c) We think that coordination in an organization can be improved not by building more complex models but by constructing a network of interdependent models. These models should create the possibility to connect SDSS. It will then be possible to take into account the effects of alternatives chosen by other decision-makers, e.g., by regarding the effects of these decisions as constraints. The integrating models should be updated for that purpose and specifications of various alternatives could be made available, if final decisions have not already been made.

The weakest point in our proposition is the way in which the most important part of the decision process, the second phase of fig. 1, is taken into consideration. However, we assume that our proposal to structure decision processing can be extended on several points. One point is the field of knowledge representation. We suggest that knowledge representations, of which expert systems are an example, should be part of the DSS domain.

## 5. Information Systems and Decision Support-Conclusion

In DSS literature a distinction is often made between IS and DSS. We define IS, following Davis and Olson [1985, p. 6], as 'an integrated, user-machine system for providing information to support operations, management, and decision-making functions in an organization. The system utilizes computer hardware and software; manual procedures; models for analysis, planning, control and decision making; and a data base'. Using this definition of IS we do not consider a distinction between IS and DSS relevant. The distinction often made is probably the result of the facts that IS and management science are regarded as synonyms, which they are definitely not. Of course, the design of IS differs when a case in which DSS generators and SDSS are applied is compared with a case without these applications. There are two reasons for such a difference.

(1) The interrelationships between the subsystems of IS with and without a DSS generator will be different in number and quality. As depicted in fig. 3, a DSS generator opens facilities to construct interrelationships that are not available when a DSS generator is lacking. This especially applies to the data base, but it holds also for other components of DSS generators. Recent research in the DSS domain shows that these differences will grow, because much of this research is directed at a reduction of the influence of the constraints on the interfaces between components of DSS generators, see Holsapple and Whinston [1983], Blanning [1985], Sen and Biswas [1985], Chen and Henschen [1985] and Liang [1985].

(2) Davis and Olson [1985, p. 14] correctly state: 'The fundamental processes of management information systems are more related to organizational processes and organizational effectiveness than computational algorithms'. They suggest that the structure of IS is determined by organizational considerations. Most of these considerations in the discussion of IS structure are the same as the ones we mentioned in section 3, see Davis and Olson [1985], Thierauf [1982]. Given the goal of SDSS, viz. delivering support in decision making, it would be remarkable to assume that no changes in the organizational structure would appear, especially, since we can improve the effectiveness of SDSS by implementing some of the suggestions for improvement we made in section 2. Three ways to realize these improvements can be distinguished.

\- In the formal and informal procedures applied by individual decision makers, see section 3.

\- In the structure of the organization, e.g., emphasis on decentralization.

\- In a combination of both.

In this paper we restrict our attention to the third way with emphasis on the formal procedures. For an example of the second way, see Bosman [1983]. We believe that SDSS can be used to improve decision making if we are willing to define the construction of SDSS as an organizational problem and not as a separate field specified by the abilities of DSS generators. As we have shown in this chapter the organizational problem should be defined by stressing two points, viz. that there is such a big difference between the parts of the decision process that it is not plausible to assume that one model can describe the whole process and secondly that decision processes or its parts cannot be considered independent entities.

DSS are a special kind of IS. The distinction made between IS and DSS is a symptom of the way we solve the coordination problem. We assume that aggregation is the procedure to specify the relations between levels of the organization. However, it is not the only procedure to define relations between levels and probably, as shown, not the most adequate one, because it makes it impossible to define relations in a top-down way and interconnect equation and process models. Coordination is not only a process of translating decisions taken at the top in directives for the execution, as is generally assumed in most organization literature. Problem recognition and problem description suggest and demand a way of describing how decision processes are interconnected in both directions of the organization structure.

## References

Belew, R.K., Evolutionary decision support systems, in: Knowledge representation for decision support systems, L.B. Methlie and R.H. Sprague, eds. (North-Holland, Amsterdam, 1985) 147–160.

Blanning, R.W., A relational framework for join implementation in model management systems, Decision Support Systems 1, nr. 1 (1985) 69–81.

Bonczek, R.H., C.W. Holsapple and A.B. Whinston, Foundations of decision support systems (Academic Press, New York, 1981) 393.

Bosman, A., Decision support systems, problem processing and coordination, in: Processes and tools for decision support, H.G. Sol, ed. (North-Holland, Amsterdam, 1983) 79–92.

Bosman, A., Decision support systems, a discipline or a vision, in: H.G. Sol, C.A.Th. Takkenberg and P.H. de Vries Robbé, eds., Expert systems and artificial intelligence in decision support systems (Reidel, DorJrecht, 1987) 23–40.

Bosman, A. and J.L. Bouma, Cost accounting, planning and budgeting, in: Quantitative methods in budgeting, C.B. Tilanus, ed. (Martinus Nijhoff, Leiden, 1976) 109–134.

Bosman, A. and H.G. Sol, Knowledge representation and information systems design, in: Knowledge representation for decision support systems, L.B. Methlie and R.H. Sprague, eds. (North-Holland, Amsterdam, 1985) 81–91.

Chen, M.C. and L.J. Henschen, On the use and internal structure of logic-based decision support systems, Decision Support Systems 1, nr. 3 (1985) 205–219.

Davis, G.B. and M.H. Olson, Management information systems (McGraw-Hill, New York, 1985) 693.

Dikkers, G.J.O.D., Development and introduction of a decision support system, Doctoral thesis, Groningen (1982) 181.

Hayes, R.H. and K.B. Clark, Explaining observed productivity differentials between plants: implications for operational research, Interfaces 15, nr. 6 (1985) 3–14.

Holsapple, C.W. and A.B. Whinston, Data base management: theory and applications (Reidel, Dordrecht, 1985) 392.

Liang, T.P., Integrating model management with data management in decision support systems, Decision Support Systems 1, nr. 3 (1985) 221–232.

Mintzberg, H., Structure in fives (Prentice-Hall, Englewood Cliffs, 1983) 312.

Pondy, L.R. and I.I. Mitroff, Beyond open system models of organization, in: Research in organizational behavior, B.M. Staw, ed. (JAI Press, Greenwich, 1979) 3–39.

Rosenkranz, F., An introduction to corporate modeling (Duke university press, Durham, 1979) 498.

Sage, A.P., B. Galing and A. Lagomasino, Methodologies for determination of information requirements for decision support, Large Scale Systems 5 (1983) 131–167.

Sen, A. and G. Biswas, Decision support systems: an expert systems approach, Decision Support Systems 1, nr. 3 (1985) 197–204.

Simon, H.A., The new science of management decision (Harper and Row, New York, 1960) 50.

Sol, H.G., Simulation in information systems development, Doctoral dissertation, Groningen (1982) 221.

Sol, H.G., Paradoxes around DSS, in: Proceeding NATO advanced summer institute (Springer, Berlin, 1985).

Sol, H.G., Aggregating data for decision support, Decision Support Systems 1, nr. 2 (1985a) 111–121.

Sprague, R.H. and E.D. Carlson, Building effective decision support systems (Prentice-Hall, Englewood-Cliffs, 1982) 329.

Stohr, E.A., DSS for cooperative decision-making, in: Data base management: theory and applications, C.W. Holsapple and A.B. Whinston, eds. (Reidel, Dordrecht, 1983) 307–324.

Takkenberg, C.A.Th., CAP: a decision support system for the planning of production levels, in: Processes and tools for decision support, H.G. Sol, ed. (North-Holland, Amsterdam, 1983) 249–259.

Thierauf, R.J., Decision support systems for effective planning and control (Prentice-Hall, Englewood Cliffs, 1982) 536.

Vazsonyi, A., Computer-supported gedankenexperiments, Interfaces 12, nr. 4 (1982) 34–41.
