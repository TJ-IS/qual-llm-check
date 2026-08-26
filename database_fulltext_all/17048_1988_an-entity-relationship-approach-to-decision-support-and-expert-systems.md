---
otero_id: 17048
otero_key: "42FHQ2XS"
title: "An entity-relationship approach to decision support and expert systems"
authors: "Ye-Sho Chen"
year: "1988"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(88)90131-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An Entity–Relationship Approach to Decision Support and Expert Systems

Ye-Sho CHEN \*

Department of Quantitative Business Analysis, Louisiana State University, Baton Rouge, LA 70803, USA

There has been an increasing interest in integrating decision support systems and expert systems to provide decision makers a more accessible, productive and domain-independent information and computing environment. In this paper, we review a workstation-based expert decision support system (WXDSS) proposed by Chen and Pruett. A database-oriented design process is discussed consisting of four phases: (1) requirements analysis, (2) conceptual framework, (3) logical design, and (4) physical system implementation. An entity–relationship (ER) approach to the design of conceptual framework is studied. A positive characteristic of the ER approach is that it provides the user an enterprise view of the WXDSS that is independent of how the information is stored and processed.

Keywords: Entity-Relationship Diagram, Logical Design, Decision Support Systems, Expert Systems.

![](/api/attachments/42FHQ2XS/fulltext/images/9b06c876debaf8f6934d73d2ffba27eacabbf51cea5d5545ef28dfacdc16cfe5.jpg)

Ye-Sho Chen is an Assistant Professor of Management Information Systems in the Department of Quantitative Business Analysis at Louisiana State University. He received his Ph.D. in Industrial Engineering from Purdue University in 1985. His current research interests include decision support and expert systems, quality control information systems, and information storage and retrieval. He a member of ACM, TIMS, AAAAI, and ASQC.

\* This research was funded by the College of Business Administration at Louisiana State University. The author also thanks one of the referees for his/her valuable comments.

## 1. Introduction

The concepts of conventional decision support systems (DSS) described in the literature can be broadly classified into three categories [2]: where-to-support, what-to-support, and how-to-support. Effective integration of these three approaches is an inherent problem in conventional DSS design [2]. As a result, it suffers from drawbacks such as domain-dependence and lack of user-friendliness [27].

With the promotion of expert systems (ES) technology, several attempts have been made to integrate DSS and ES. As Turban and Watkins [28, p. 123] put it, 'The benefits of the DSS/ES integration can be realized along several dimensions: ES contribution, DSS contribution, and the synergetic resulting from the DSS/ES contribution'. The potential for synergy between DSS and ES was examined recently by Henderson [18].

Possible research strategies for the DSS/ES marriage could be classified as follows [29]: (1) enhancements of existing systems, (2) coupling of independent systems, and (3) synergistic integration resulting in a new class of systems. These types of research focus on the implementation strategies for the physical systems.

Another important type of research is to develop a theory of logical DSS/ES integration that is as independent as possible of the way in which the information is stored and processed [4].

In this paper, we discuss both the physical and logical integration of DSS and ES. The study of physical integration is conducted in Section 2, where a workstation-based expert decision support system (WXDSS) is discussed.

A database-design process for the WXDSS is shown in section 3. There an interesting phenomenon showing the importance of being database-oriented is illustrated. Within the proposed design process, we focus on the design of conceptual framework which is an important part of logical DSS/ES integration. The entity–relationship (ER) approach proposed by Chen [7] is adopted as a practical tool for conceptual framework. A brief overview of the ER approach to data management is discussed in section 4. Applications of the ER approach to model management and expertise management are studied in sections 5 and 6, respectively. An ER approach to data, model, and expertise integration is shown in section 7. Finally, section 8 presents the conclusion.

## 2. A Workstation-Based Expert Decision Support System (WXDSS)

As the name implies, a DSS is a computer system used to support decision making. Three elements are crucial during a DSS-based decision-making task: data, analytical or computational models, and experience [19]. The conventional DSS design focuses on the support of data, models and their integration. The framework of the conventional design can be represented as [26]:

$$
\begin{array}{c} S _ {\mathrm{CON}} = (U, I, D, D ^ {*}, \\ M, M ^ {*}, R, G) \end{array}\tag{1}
$$

Here $S_{CON}$ denotes the conventional DSS; U represents the user groups; I represents the interface management system; D represents the required data set stored in a data base; $D^{*}$ represents a data management system; M represents a set of models; $M^{*}$ represents a model management system; R includes various types of report generators; and G provides visual display facilities. The Notation in eq. (1) was first proposed by Sen [26].

The conventional DSS has been implemented primarily within a single, specific problem domain [27] and suffers from drawbacks such as domain-dependence and lack of user-friendliness. As a result, the typical DSS user must possess domain expertise to understand 'what' the system supports and tools expertise to know 'how' to use the system correctly. To relieve the what-and-how problems which typically confront the DSS user, Sen and Biswas [27] proposed a promising expert DSS (XDSS) framework. The XDSS framework can be represented as

$$
\begin{array}{l} X _ {\mathrm{XDSS}} = (U, I _ {\mathrm{XDSS}}, D, D ^ {*}, M, M ^ {*}, R, G), \\ I _ {\mathrm{XDSS}} = (I, K B), \\ K B = (\text { Domain } - K B, \text { Tools } - K B). \end{array}\tag{2}
$$

$S_{XDSS}$ represents the XDSS structure which includes the eight previously mentioned components except $I_{XDSS}$ . $I_{XDSS}$ represents the dialogue management part of the XDSS. It includes two component: the interface system (I) and the knowledge-based system (KB). The latter may be further subdivided into two components: Domain-KB which handles the domain expertise necessary to provide ‘know-what’ questions, and Tools-KB which provides ‘know-how’ guidance to use the tools in the conventional DSS.

The XDSS design has several shortcomings, e.g., the system is inflexible, lacks communication capability, and is not cost-effective. To overcome these problems, a workstation-based, enhanced version of the XDSS (WXDSS) is proposed by Chen and Pruett [10]. Its architecture can be represented as

$$
\begin{array}{l} S _ {\mathrm{WXDSS}} = (U, W, \text {Tools} - K B, D, D ^ {*}, M, M ^ {*}, R, G) \\ W = (W _ {i}, \dots , W _ {i}, \dots , W _ {n}), \\ W _ {i} = (d, d ^ {*}, m, m ^ {*}, r, g) + \\ \text {expert system shells} + \\ \text {networking facilities,} \quad i = 1, 2, \dots , n. \end{array} \tag {3}
$$

Here $(d, d^{*}, m, m^{*}, r, g)$ are similar to those used in eq. (1), except the components referred to are personal productivity tools. For example, $d^{*}$ might consist of R-base system V or dBASE III + as a data base management system and $m^{*}$ might consist of Lotus 1-2-3 as a model management system. The main advantage of the $S_{WXDSS}$ concept is that the general Domain-KB in $S_{XDSS}$ is replaced by a set of domain specific and networked workstations.

## 3. Design Considerations for the WXDSS: A Database-Oriented Approach

In this section, we review a database-oriented approach to the design of the WXDSS as was proposed in [10]. We adopt and generalize a step-by-step procedure for data base design [6,24]. The sequence consists of four phases: (1) requirements analysis, (2) conceptual framework, (3) logical design, and (4) physical system implementation. In creating a data base, several appropriate tools are available during each phase of the development process. Among these tools, structured analysis is probably the most prominent for the requirements analysis. The entity–relationship (ER) approach proposed by Chen [7] is one of the most popular conceptual modeling methods. Corresponding to the logical design phase, the relational data model has been accepted as the preferred one since it provides a simpler user view than the other approaches. In the physical system implementation phase, an effective data base management system is usually chosen to implement the data base.

The proposed design process for DSS/ES integration is based on the fact that a user-oriented approach is crucial for a newly released technology or methodology. A recent phenomenon in the use of LISP and C shows the importance of being user-oriented. In this early artificial intelligence (AI) laboratory experiments, LISP was the typical language used for implementation. However, as AI researchers attempt to introduce practical AI products into commercial applications, several difficulties in using LISP are encountered. Two significant reasons are: (1) expense of PC usage [21] and (2) lack of LISP programmers [25]. As a result, several competitive languages are proposed, e.g., C [25] and Ada [3]. The significant factors in promoting C are: the powerful UNIX supporting environment [25], the great portability [3], and, most importantly, the dominance in the commercial arena of the IBM PC [25]. Besides replacing LISP with other competitive languages, several other significant options are noticed in [16]: the use of microcomputer-based expert system shells, the integration of various inferencing capabilities into a mainframe-based inference engine, and the improvement of LISP to increase its marketability.

The proposed design framework for the WXDSS presents several research opportunities. For the requirements analysis phase, we might modify the minispecifications of a data flow diagram [14] to incorporate the need for data bases, computational or analytical models, and decision rules. For the conceptual framework phase, we show, in the following sections, the possibility of modifying the ER approach for model management and expertise management. In the realm of logical design, the relational data model has been developed successfully for business applications. However, it has often failed to provide appropriate support for engineering applications [23]. A number of enhancements to the relational data model have been proposed and experimentally implemented with the goal of providing a wider class of applications. The WXDSS framework provides an opportunity for two types of physical design: the comprehensive XDSS design and the workstation tool-kit design. The comprehensive XDSS design has been fertile area of DSS research. Although it has been pointed out that the research in this area is still in its infant stages [5,19], a recent system proposed by Jelassi, Jarke and Stohr [20] provides a promising foundation for obtaining practical results. For the workstation tool-kit design approach, Chen and Pruett [10] identifies four options for the physical integration of the personal software tools.

## 4. Data Management: An ER Approach

Since the invention of ER modeling for data management [7], there have been several versions of the ER approach [8]. Whatever version it is, an ER diagramming technique will incorporate at least four elements: entity, relationship, cardinality, and dependency. To illustrate the concepts, consider the following example taken from the project assignment given in Kroenke and Nilson's book on Data Base Processing for Microcomputers [22, p. 96]:

Requirements Analysis of An Academic Enterprise: Design a data base of your academic environment. Your database should allow you to answer questions about the courses you have taken, the grade you received in the course, the rating (from 1 to 10) which you gave the course, the instructors you have had, the textbooks you have used, and the textbooks' publishers and authors.

As a minimum, you should be able to answer questions such as, "In which of the courses I have taken that are rated 8 or more did I receive a grade "Which text was used in course ABC?" "Which textbooks have I used which were written by Z?" and "What courses did I take during the fall semester of 1985?"

Fig. 1(a) shows an ER model of the academic enterprise. Three entities: COURSE, TEXT, and COURTEXT, are identified. The relationship between the COURSE and COURTEXT (or TEXT and COURTEXT) entities is shown by drawing a line between them. We said that the relationship between COURSE and COURTEXT is one-to-many. We have indicated this by putting a crows foot on the 'many' side of the relationship line. This is the cardinality of the relationship. The small straight line across the relationship line near the COURSE entity indicates that there must be an entry in the COURSE table for every entry in the COURTEXT table. The small circle across the relationship line next to the COURTEXT entity indicates that there need not be an entry in the COURTEXT table for every entry in the COURSE table. The small straight line and small circle notations indicate the dependency of the relationship. Note that the relationship sets in fig. 1(a) do not include the diamond symbol as originally used by Chen [7]. This is because Kroenke and Nilson's ER diagram is based on a binary ER model allowing only: (1) attributes for entities, (2) 'one-to-many' and one-to-one' non-directional relationships. For details on this topic, see reference [8] for examples.

![](/api/attachments/42FHQ2XS/fulltext/images/98bbeff227e00811bd1e1c71f5d3ee6c60eec70d02f9b342b47704b36e607cc1.jpg)

```txt
(b) Relational Tables:
COURSE (Course#, Course-title, Semester, Grade, Rating, Instructor)
TEXT (ISBN#, Text-title, Author, Publisher)
COURTEXT (Course#, ISBN#)
Cardinality: For one-to-many cases, the enforcement of this type of restrictions is unnecessary
Dependency:
1. "Not a valid COURSE number." +
Course# IN COURTEXT EQA Course# IN COURSE
2. "Not a valid TEXT number." +
ISBN# IN COURTEXT EQA ISBN# IN TEXT
```  
Fig. 1. (a) An Entity–Relationship Model of the Academic Enterprise and (b) The Corresponding Relational Tables and the Enforcement of Cardinality and Dependency.

Fig. 1(b) shows the relational tables for the three entities described in fig. 1(a). The relationship between COURSE and COURTEXT (or TEXT and COURTEXT) is represented by the column which the two tables have in common. For one-to-many cases, the cardinality is not necessary to enforce [22]. The dependency is enforced through the RULES syntax of R: base 5000 [22].

## 5. Model Management: An ER Approach

Recently, Blanning [4] used an ER approach to model management. Fig. 2(a) shows his ER approach for a cyclic model bank. The algorithm which the ER approach models is shown in fig. 2(b). Blanning's ER diagram leaves some room for improvement. First, the diagram fails to show the process order of the algorithm. Second, the diagram does not capture the simultaneity problem shown in step 5 of the algorithm in fig. 2(b). In the

FINANCIAL STRUCTURE

(a)  
![](/api/attachments/42FHQ2XS/fulltext/images/8088f194940e6faaae139ccf08a95889e2cbc72ce347ff7c1b9144be0b78c7f5.jpg)  
Fig. 2. (a) Blanning's ER Diagram for a Cyclic Model Bank [4] and (b) An Algorithm for which the ER Diagram Tries to Model [4].

following we propose a new ER approach which includes the four important elements discussed in section 4.

Fig. 3(a) shows a new ER diagram for the algorithm shown in fig. 2(b). Four entities are identified: Pricing-Policy, Market, Factory, and Financial-Structure. The relationship between two entities is an input-output format and is shown by drawing an arrow line from input entity to output entity. For example, the Pricing-Policy and Market relationship is demonstrated by drawing an arrow from Pricing-Policy to Market. The cardinality of the relationship shows the process order, which is not shown in Blanning's ER diagram, of the algorithm and is indicated by putting the corresponding number beside the arrow. For example, the number 'one' shown in fig. 3(a)

indicates the algorithm begins with a Pricing-Policy number and inputs to the Market function as the output. The switch sign next to the number 'four' indicates that the function Financial-Structure will be calculated if a fixed point for the simultaneity problem is resolved. The simultaneity problem can be identified through the reverse direction of relationships one and three. There the value Pricing-Policy, the input of relationship one, equals the function Pricing-Policy, the output of relationship three. The switch sign could be defined as the dependency of the relationship.

Fig. 3(b) shows the relational forms for the four entities described in Fig. 3(a). The input-output relationship is represented by a functional format. For example, the relationship between Pricing-Policy and Market is represented as Market (Pric-(b) Relational Forms and Cardinality:

(a)  
![](/api/attachments/42FHQ2XS/fulltext/images/fb2eee1bdac3d6c9b9b964054eff0fefbe29bcef607b578a0898fdf3b9f22d39.jpg)

```txt
1. Market (Pricing-Policy)
2. Factory (Market)
3. Pricing-Policy (Market, Factory)
4. Financial-Structure (Pricing Policy, Market, Factory)

Dependency: Relational form with cardinal #4 works if Pricing-Policy = Pricing-Policy (Market - (Pricing-Policy), Factory Market (Pricing-Policy)).
```  
Fig. 3. (a) A New ER Diagram for the Algorithm shown in Fig. 3(b) and (b) The Corresponding Relational Forms, Cardinality, and Dependency.

ing-Policy). The process order (or cardinality) is shown beside the corresponding relational form. The dependency is enforced through a simultaneity equation.

Blanning's ER diagram utilizes a relational approach for model management. There are several other approaches which are useful for model management, e.g., the structured modeling approach of Geoffrion [15], the model abstraction approach of Dolk and Konsynski [11], and the semantic net approach of Elam, Henderson, and Miller [12]. We have seen that the ER approach to data management can be modified for the area of relation model management. Whether the ER approach will be useful in the other approaches of model management is yet to be answered, and this suggests opportunities for further research.

## 6. Expertise Management: An ER Approach

The need for development of the conceptual framework of an expert system has been advocated in recent literature [13,17]. In this section, we discuss an ER approach to rule-based expertise management which also includes the four crucial elements: entity, relationship, cardinality, and dependency.

The idea of the ER approach discussed below comes from the inference net studied by Winston [30, p. 186]. For example, consider the following three rules given in [1, p. 186].

Rule 1: If A and B and C, then X.

Rule 2: If A and B and D, then X.

Rule 3: If A and B and E, then Z.

Fig. 4(a) shows an ER model for the set of rules. Eight entities are identified: A, B, C, D, E, X, Y, and Z. The relationship between entities within a rule is shown by connecting the if parts and the then parts of the rule through an AND gate. For example, entities A, B, and C are connected to entity X through gate #1. The number within a gate shows the corresponding rule number and represents the cardinality. The symbol and AND gate 'D' represents the dependency between the if-part entities and the then-part entities. Fig. 4(b)

shows the relational forms for the three rules and the corresponding cardinality and dependency.

This ER approach has all the benefits an inference net has [30], e.g., explaining the reasoning, simplifying the knowledge transfer, and determining the certainty factors of a rule-based system. Another significant benefit is its ability to express a rule-based knowledge explicitly. As pointed out by Aikins [1], one of the primary problems in a rule-based system is that much of the knowledge in the system is represented implicitly. As an example, consider the three production rules shown above. The set of rules has an implicit AB context representation when any one of the rules is treated individually [1]. Fig. 5(a) shows an explicit AB context ER diagram, where G1 refers to group rule #1. Fig. 5(b) presents the relational forms, cardinality, and dependency in a way similar to fig. 4(b).

(a)  
![](/api/attachments/42FHQ2XS/fulltext/images/b21ddc2da0fc2ed85ba6d8a46ca4c66d052b834398e7d3890bb2b85ae0e1748d.jpg)

(b) Relational Forms, Cardinality, and Dependency
RULE-1(A,B,C;X)
RULE-2(A,B,D;Y)
RULE-3(A,B,E;Z)

Fig. 4. (a) An ER Diagram for a Set of Production Rules and (b) The Corresponding Relational Forms, Cardinality, and Dependency.  
![](/api/attachments/42FHQ2XS/fulltext/images/0e5ceca1abeb4d19f54641911cdf9aca9e023b1be54f721dd7fe493a5963f0f4.jpg)

(b) Relational Forms, Cardinality, and Dependency:

```csv
GROUP-RULE-1(A,B; AB)
AB-RULE-1(C;X)
AB-RULE-2(D;Y)
AB-RULE-3(E;Z)
```  
Fig. 5. (a) An ER Diagram Shown the Implicit AB context within a Set of Rules and (b) The Corresponding Relational Forms Cardinality and Dependency

The rule-based approach represents one of the knowledge representation techniques for expertise management. There are several other knowledge representation techniques, e.g., frames, semantic nets, and logic. We have seen that the ER approach can be used to provide conceptual modeling for rule-based expertise management. Further research is necessary for examining whether the ER approach will be useful in the other knowledge representation techniques of expertise management.

## 7. An ER Approach to Data, Model, and Expertise Management

We have studied the ER approach to data management, model management, and expertise management. A logical next question might be 'How do we integrate the three types of ER diagrams?' To answer the question, a reasonable approach is to see how the three components are integrated at the physical implementation level. There are a number of different ways in which data, model, and expertise management could be physically implemented. Vassiliou [29] classified three possible strategies: (1) enhancements of existing systems, (2) coupling of independent systems, and (3) technology integration resulting in a new class of systems. Vassiliou [29] further suggested that ‘system enhancements represent a short-term partial solution, coupling presents an easy and practical solution and although integration is elegant and promising, it may never lead to a practically acceptable solution’.

A recent promising system developed by Zobaidie and Grimson [31] is consistent with Vassiliou's view and shows a practical way of physically coupling the three basic components. We adopt Zobaidie and Grimson's coupling approach and modify it for the integration of data, model, and expertise at the conceptual framework level.

Our approach could be better explained in terms of the mathematical programming system discussed in Blanning [4]. Fig. 6 shows an ER approach to integrating data, model, and expertise components in the mathematical programming environment. Five entities are identified: user, data, model, expertise, and dictionary. The user entity represents the user group in a certain workstation environment. Within the data entity is a set of subentities modeled by an ER diagram as described in section 4. Similar explanations apply to model and expertise entities. The dictionary entity provides an interface between the other four entities. The relationship and cardinality notations are the same as the ones discussed in section 5. Thus, the process orders one through eight describe the information flow in the mathematical programming system.

![](/api/attachments/42FHQ2XS/fulltext/images/fb520bc4b88741bf8d1d2d3c4b981f769d5429bdc09f8db07024c9ca47d1e7dc.jpg)  
Fig. 6. An ER Approach to Data, Model, and Expertise Management.

The expertise entity and relationships nine and ten are not included in Blanning's article. We put them here to explain the dependency notation. The switch sign notation on relationship nine indicates that if the report, the output of process order eight, is acceptable, then the user will use the expert system(s) within the expertise entity.

## 8. Conclusion

In this paper, we have reviewed a workstation-based decision support and expert system (WXDSS) and proposed a database-oriented design approach for the system. We then showed how the entity–relationship approach proposed by Chen [7] for data management can be modified and applied to model management and expertise management. A significant contribution of this approach is to provide a unified conceptual framework that is as independent as possible of the way in which the information in a WXDSS is stored and processed [4].

## References

[1] J.S. Aikins, Prototypical knowledge for Expert Systems, Artificial Intelligence 20 (1983) 163–210.

[2] G. Ariav and M.J. Ginzberg, DSS Design: A Systemic View of Decision Support, Communication of the ACM 28 (1985) 1045–1052.

[3] L. Baker, Ada and AI Join Forces, AI Expert 2, No. 4 (1987) 38–45.

[4] W. Blanning, An Entity-Relationship Approach to Model Management, Decision Support Systems 2, No. 2 (1986) 65–72.

[5] R.H. Bonczek, C.W. Holsapple and A.B. Whinston, Developments in Decision Support Systems, Advances in Computers 23 (Academic Press, 1984) 161–175.

[6] J.L. Carswell and S.B. Narathe, SA-ER: A Methodology that Links Structured Analysis and Entity-Relationship Modeling for Database Design, The Fifth International Conference on Entity-Relationship Approach P.P. Chen, ed. (North Holland, New York, Amsterdam, 1986).

[7] P.P. Chen, The Entity-Relationship Model - Toward a Unified View of Data, ACM Transactions of Data Base Systems 1, No. 1 (1976) 9-36.

[8] P.P. Chen, A Preliminary Framework for Entity–Rela-

tionship Models, in: P.P. Chen, ed., Entity–Relationship Approach to Information Modeling and Analysis (North-Holland, Amsterdam, 1983) 19–28.

[9] Y.S. Chen, and J.M. Pruett, Expert Systems and Operational Integration, in: A.W. Filstup, III, F.L. Chu and R.F. Jones, Jr., eds., Computer-Aided Engineering Application, PVP-Vol. 126 (The American Society of Mechanical Engineers, 1987) 1–6.

[10] Y.S. Chen and J.M. Pruett, Decision Support and Expert Systems: A Workstation Approach, Submitted for Publication.

[11] D. Dolk and B. Konsynski, Knowledge Representation for Model Management Systems, IEEE Trans. Software Engineer. SE-10 (1984) 619–627.

[12] J. Elam, J. Henderson, and L. Miller, Model Management Systems: An Approach to Decision Support in Complex Organizations, Proceedings of the Conference on Information Systems (1980).

[13] P. Feldman and G. Fitzgerald, Representing Rules Through Modeling Entity Behavior in: P.P. Chen, ed., The 4th International Conference on Entity-Relationship Approach, IEEE Computer Society (1985) 189–198.

[14] J. Fitzgerald and A. Fitzgerald, Fundamentals of Systems Analysis (Wiley, 1987).

[15] A.M. Geoffrion, An Introduction to Structured Modeling, Management Science 33 (5) (1987) 547–588.

[16] W.B. Cevarter, The Nature and Evaluation of commercial Expert System Building Tools, IEEE Computer 20 (5) (1987) 24–41.

[17] J.P. Held and J.V. Carlis, Conceptual Data Modeling of an Expert System, in: P.P. Chen, ed., The 4th International Conference on Entity-Relationship Approach, IEEE Computer Society (1985) 182–188.

[18] J.C. Henderson, Finding Synergy Between Decision Support Systems and Expert Systems Research, Decision Sciences 18 (3) (1987) 333–349.

[19] S. Hwang, Automatic Model Building Systems: A Survey (DSS-85 Transactions, San Francisco, CA, 1985) 22–32.

[20] M.T. Jelassi, M. Jarke, and Stohr, Designing a Generalized Multiple Criteria Decision Support System, J. of Management Information Systems 1 (4) (1985) 24–43.

[21] S. Karen, Scientific Application for Expert System in Works, Info World, March 10 (1986) 18.

[22] D.M. Kroenke and D.E. Nilson, Database Processing for Microcomputers (SRA, 1986).

[23] R. Lorie, Issures in Databases for Design Applications, IBM Computer Science Research Report, RJ3176 (1981).

[24] National Bureau of Standards, Database Directions: Information Resource Management Strategies and Tools, NISS Special Publication 500-92, Alan Goldfine, ed. (U.S. Department of Commerce, 1982).

[25] J. Roland, C on the Horion, AI Expert 2, No. 4 (1987) 46–55.

[26] A. Sen, Decision Support Systems: An Activity-oriented Design, J. of Information Science 7 (1983) 23–30.

[27] A. Sen and Biswas, Decision Support Systems: An Expert Systems Approach, Decision Support 1 (1985) 197–204.

[28] E. Turban and P.R. Watkins, Integrating Expert Systems and Decision Support Systems, MIS Quarterly (1986) 121–136.

[29] Y. Vassiliou, Knowledge Based and Database Systems: Enhancements, Coupling or Integration, On Knowledge Base Management Systems, M.L. Brodie and J. Mylopoulos, eds. (Springer-Verlag, 1986) 87–91.

[30] P.H. Winston, Artificial Intelligence, (Addison-Wesley, 1984).

[31] A. Al Zobaidie and J.B. Grimson, Expert Systems and Database Systems: How Can They Serve Each Other?, Expert Systems 4 (1) (1987) 30–37.
