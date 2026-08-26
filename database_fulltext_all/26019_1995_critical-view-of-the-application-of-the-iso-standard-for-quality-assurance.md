---
otero_id: 26019
otero_key: "UAFYB3VN"
title: "Critical view of the application of the ISO standard for quality assurance"
authors: "K. Braa; L. Øgrim"
year: "1995"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1995.tb00098.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Critical view of the application of the ISO standard for quality assurance

K. Braa & L. ∅grim

Department of Informatics, University of Oslo, PO Box 1080, Blindem, 0316 Oslo, Norway

Abstract. The aim of this paper is to initiate a debate on quality assurance and the application of the ISO 9001 in the system development field. It is claimed that unquestioning application of ISO 9001 can be a backwards step in the practice and research of system development. Five aspects of quality are identified in order to design and evaluate the quality of information systems: technical quality, use quality, aesthetic quality, symbolic quality and organizational quality. We find that the standard solely emphasizes technical quality. The standard promotes the ideal of linear, phase-oriented system development, based on a fixed requirement specification and a document-driven process. This is in contrast to most research findings, which criticize one-sided adaptation of phase orientation in system development.

Keywords: information systems quality, ISO 9000, multiple perspectives on quality, quality assurance

## 1 INTRODUCTION

System development projects often produce computer systems of low quality from both use and technical aspects (Lyytinen, 1987). Evolutionary system development can be seen as an attempt to cure these problems (Boehm, 1988; Floyd et al., 1989; Kautz, 1993). Quality assurance is another such attempt. This paper aims to integrate the application of these two approaches by raising the question of whether quality assurance, as stated in the ISO standard, really is an assurance of quality.

The principal aims of quality assurance are to specify requirements and to work according to documented procedures. In this paper we question whether specified requirements and documented procedures really are the means of achieving quality. Standards can be implemented in many ways: this paper follows the 'worse case', which we fear could be the 'cheapest' way to implement the ISO standard. This is done both to provoke a discussion and to emphasize the main points.

The establishment of standards, tools, methods and norms within a new discipline takes time. The introduction of the ISO 9000 standards on quality assurance aroused great interest in the subject both in practical system development and in IT research (Bang et al., 1991; Gillies,

1992). These standards have been accepted since 1992 by all the national standardizing bodies in both the European Union (EU) and the European standardization organization (CEN). The harmonized rules prohibit any government institution within the EU from trading with any company in the EU and the European Economic Cooperation that does not adhere to the harmonized standards (Rothery, 1992, p. 5).

The origin of ISO 9001 is the manufacturing of goods, not the production of intangible services such as computer systems. In our view, this means that the standard is difficult to apply in the field of system development.

Quality in the system development discipline is not a static concept, but has to be continuously evaluated and refined in interaction with technological evolution, organizational claims and changes in the market. There are numerous views on quality related to different perspectives. This paper concentrates on the quality of information systems, more specifically the quality of software in use in organizational context. Discussion of quality as a concept in system development will be addressed in Section 3.

We define quality assurance as the systematic activities aimed at enhancing the quality of information systems during the development process. A quality system denotes the efforts within an organization to structure the quality assurance activities. Important elements of a quality system are structure of responsibility, guidelines and routines of verification and validation of products and activities. Standards are generally defined in terms of a model of best practice, against which all other practices may be compared. This is true also for the standards available for software quality. A standard of quality assurance is a specification of a minimum level of quality assurance activities, decided by some standardization body.

This paper aims to reveal possible negative effects of introducing ISO 9001 in system development. Issues for further research will be outlined. It is our belief that, if care is not taken, the quality assurance systems based on the ISO standard will lead to more traditional system development practice and thus be a step backwards from the last 10 years of advances in system development research and practice.

## 2 THE ISO 9000 SERIES

The standards of the ISO 9000 series constitute one of a number of sets of quality assurance standards. The series dates from 1979, when BS 5750 was introduced in the UK. In 1987, the corresponding ISO, BS and EN standards were harmonized to produce three identical series of standards. Most of the European countries and the USA acknowledge the standard (Burr, 1990). Different countries name the standard in slightly different ways (US, ANSI/ASQC 090; UK, BS 5750; Germany, DIN ISO 9000; Norway, NS-ISO 9000).

The ISO 9000 series contains five standards, 9000–9004. ISO 9000 contains guidelines for choosing and applying standards for quality management and requirements for quality systems. ISO 9001–9003 are general standards covering all of industry, providing the minimum required level of a quality system. ISO 9004 contains guidelines for quality management and quality system elements.

ISO 9001 contains requirements to production and development. The origin of the standard was quality assurance for the manufacturing of goods, and ISO 9000-3 is an adaptation of 9001 to the software development field. ISO 9000-3 gives 'guidelines for the application of ISO 9001 to the development, supply and maintenance of software'. System development organizations are certified according to ISO 9001.

## 3 MULTIPLE PERSPECTIVES ON QUALITY

Quality is hard to define, difficult to measure, but easy to recognize (Pirsig, 1974; Kitchenham, 1989a). Software quality is often regarded as pertaining only to the technical properties of the computer system. The approach of this paper is to expand the definition and to consider the functional and organizational aspects of quality as well. In what follows, five aspects which should be taken into consideration both when designing and when evaluating the quality of information systems have been identified. The aspects are technical quality, use quality, aesthetic quality, symbolic quality and organizational quality.

## 3.1 Technical quality and use quality

Technical quality refers to a system's structure and performance. The technical quality of a computer system is the basis of its functionality — the computer must perform expected operations. However, there is no need for a technically excellent computer system; it is more important that it suits the work tasks it is supposed to support (Bjerkenes et al., 1991).

By use quality we mean quality as experienced by the users when working with the computer-based system. Use quality is difficult to specify in advance. It is often necessary to experiment with design models, such as prototypes, to express needs and claims (Greenbaum & Kyng, 1991). Throughout the specification and design activities, users and developers will then learn about the limitations and the possibilities of the computer system in use. Consequently, learning is an important factor in the specification process, as well as in design.

Quality can be seen as an objective property of the computer software, as in the software engineering tradition (Roetzheim, 1988; Sommerville, 1989) or hard systems thinking, criticized by, for example, Checkland, 1981. From this point of view, also expressed in ISO 9000–3, quality is a measure of how well the design fulfils its specification. The ideal is to make the specification as exact as possible and to make software development a predictable, and thus controllable, process. Technical aspects are easier to specify and measure than use aspects. From an objective viewpoint, technical quality is more important than use quality.

In contrast to the objective view, quality can be seen from a subjective perspective. This is the view taken in the user satisfaction tradition (Kim, 1989), which is oriented towards individuals or groups sharing subjective expectations. Quality is seen as 'fitness for purpose' or as 'fitness for needs' (Kitchenham, 1989b). From this point of view, use quality and subjective assessments are emphasized in order to evaluate quality. Within the user satisfaction tradition, high correspondence between expectations and product signifies good quality, and low correspondence signifies poor quality. This view implies close cooperation between users and developers in order to achieve computer systems of high use quality. (The users can be both at the organizational level and at the end-user level.) A study reported by Baroudi et al. (1986) demonstrates that user involvement in the development of information systems will enhance both system usage and the users' satisfaction with the system.

![](/api/attachments/UAFYB3VN/fulltext/images/e37017ea988efdb3d3a66e444e7f1c36f72448cf691b1652b5de7f0f86d952c8.jpg)  
Figure 1. The relation between technical quality and use quality.

However, the degree of user satisfaction could be high, even if the system is of low technical quality. Low technical quality reduces the ability to maintain and change the system. When user requirements change, these changes may therefore be delayed or never implemented. This means that the experienced use quality decreases after a period of time. The relation between technical quality and use quality is illustrated in Fig. 1.

Objective criteria are needed to answer questions such as: Did the program pass the test?; Does the program implement the specification? This is useful, but insufficient to create information systems with a high use quality.

The challenge is to combine objective measurement with competence and experience and include subjective evaluation in the process of quality assurance (Dahlbom & Mathiassen, 1993). One way is to quantify subjective evaluation in order to make subjective quality more measurable and operational: making the concept of quality comprehensible, specific and concrete (McCall et al, 1977; Sommerville, 1989, p. 101). Explicit expressions are attempts at making subjective qualities more comprehensible. Qualitative properties can be stated as requirements, examples of which are 'easy to use' and 'error minimization'. More operational expressions of these requirements might be 'the time required to learn how to make use of the system' and 'the number of errors expected over a given period of time'. These are examples of making subjective evaluation as measurable as possible.

## 3.2 Aesthetic quality

In many other disciplines, such as the car industry, house building and cooking, aesthetic quality is used to evaluate the quality of artefacts. The idea of aesthetics is usually related to physical objects. However, aesthetics can also be applied to immaterial objects, for example the notion of elegant proofs in mathematics. However, the aesthetic perspective is almost always neglected in software development (Stolterman, 1991; Dahlbom & Mathiassen, 1993). One possible exception is the design of user interfaces.

An aspect of aesthetic quality is ‘elegance’, introduced as a criterion by which to assess quality (Checkland & Scholes, 1990). An attempt to increase aesthetic quality and make it more visible is to raise questions such as: Is the transformation well designed?; Is it aesthetically pleasant?; Is it overcomplicated?; or Is it over-or underengineered?: These assessments allow the users’ subjective experiences as well as the professionals’ experience of similar systems to be included in the judgement of quality.

## 3.3 Symbolic quality

Computer systems are not only artefacts, they are also used as symbols in the organization. This view is supported by Feldman & March's (1981) study of the use of information in organizations. They found that information is often used symbolically, e.g. signalling a well-driven organization, independent of whether the information is used or not.

Symbolic, as well as aesthetic, aspects of computer systems are important factors in tailoring a system to the business philosophy and organizational culture. For example, an organization wishing to have an innovative and modern image should have computer systems with graphical user interfaces and colours.

Symbolic quality may be contradictory to the use quality. This can be illustrated by a hotel owner who wanted to install a computerized reception system (an example experienced by one of the authors). It turned out that the main purpose of the system was to create the impression of a modern, successfully run hotel and to recruit educated personnel. Not much attention was paid to the functionality of the system. If the motivation is of a symbolic character, as in this example, the use quality will probably be ignored.

## 3.4 Organizational quality

When a computer system is well adapted to the organization, it can be said to be of high organizational quality. When assessing the quality of information systems, questions of economy, power and interests will arise sooner or later: Are the computer systems developed for the interests of individual users, for groups of users or for the organization as a whole? Different user groups may have diverging, perhaps contradictory, ideas of what signifies good quality. A personnel control and wage system might represent good use quality for management and the personnel department, but not for the workers who are being controlled. A medical journal system in a hospital may be of good quality for the doctors, but at the same time decrease the influence of the nurses, and use of their competence. This may, in turn, decrease the quality of their work. The different groups of users make different demands on functionality, in order to support their work. If these different interests are not met, an intersection of several interests is developed and the result could be a computer system which is not suited for anyone (Briefs et al., 1983; Nygaard, 1986; Bjerknes et al., 1987). This, in turn, may decrease the organizational quality of the system.

The development of information systems of high organizational quality requires participation from those with knowledge of the organization — on different organizational levels. In a participatory setting, the designers are responsible for explaining the technical possibilities and consequences of different solutions. Herein lies also the opportunity for the designers to use their technical expertise to manipulate the user's expectation. Each computer system is to be used within an organizational tradition. Computer systems not related to the tradition will probably not be accepted by the users, and thus be of low use quality. On the other hand, computer systems built on the organizational tradition, merely automating existing routines, will freeze the present work habits and prevent organizational development (Ehn, 1988; Stage, 1989; ∅grim, 1993).

We have discussed several aspects of quality: technical, use symbolic, aesthetic and organizational quality. The identified aspects of quality can be seen as perspectives, and used as filters or glasses for selecting and interpreting properties.

The concept ‘perspective’ has several related meanings. Nygaard & Sørgaard (1989) define perspective as a way of structuring a person's thinking by (1) the selection of properties of the phenomenon in question, (2) the interpretation of the selected properties and (3) the figurative standpoint with respect to the phenomenon or situation. Our view is that all the identified aspects of quality should be taken into consideration, and none left out when designing a computer system. Different aspects of the quality should be discussed during the development process and could be used as evaluation criteria. In addition, multiple perspectives can be used to enlighten the complexity of quality.

## 4 CHARACTERISTICS OF THE ISO STANDARD FOR QUALITY ASSURANCE

In this section, possible pitfalls of servile implementation of the ISO 9001 and 9000–3 standards are discussed. Three main characteristics of the ISO-standard are emphasised. These are:

● document-driven development process;

● fixed requirement specifications;

● phase-oriented system development.

In addition, we claim that the ISO standard expresses an unethical view on quality.

## 4.1 Document-driven system development

Documentation is necessary to create a common area of comprehension between parties in system development, to avoid misunderstandings with respect to decisions and contracts and to support transparency in the development process. Documents are necessary in order to trace the development process, and are useful in maintenance, enhancement and redesign.

Documentation and verification of the documents are an essential part of ISO 9000-3. According to the standard, the main document for quality assessment is the requirements specification. However a number of other intermediate documents are also provided.

The required input to each development phase should be defined and documented. Each requirement should be defined so that its achievement can be verified (ISO 9000-3: 5.4.4 Input to the development phases).

Every phase and every activity should be defined according to product documents and documented procedures. A phase is not finished before it is sufficiently documented and verified according to the quality system of the organization (ISO 9000-3: 5.4.6 Verification of each phase).

The idea behind the standard is to specify every procedure and document that these have been adhered to. The standard takes for granted that all work can and should be performed according to documented procedures.

The ISO 9001 standard contains 20 requirements or groups of requirements for quality systems. Almost all of them require the establishment and maintenance of documented procedures of different parts of the design work. As an example of the amount of documentation this can lead to, a Norwegian IT organization certified according to ISO has a quality system involving 105 procedures and 76 formulas.

Suchman (1987) discusses the need to adapt actions and plans according to the actual situation in the design of computer systems. This is not in line with the ISO approach. On the contrary, one interpretation of ISO 9000–3 might be that the same documentation procedures should be applied in all situations. This may result in the production of documents solely to satisfy claims. This can lead to unnecessary bureaucratic overheads for a project leader who is already following structured methods or running small projects. The cost of following the prescribed routines can be high and the closing phases of a project prolonged.

Quality assurance, according to ISO 9000-3, is generally based on documents. In other words, quality assurance, according to ISO 9000-3, supports document-driven system development. Document-driven system development is software engineering's traditional way of organizing system development. The assumption is that the documents reflect the practice of the development process. This is criticized by several authors.

A primary source of difficulty with the waterfall model has been its emphasis on fully elaborated documents as completion criteria for early requirements and design phases. . . . it does not work very well for many classes of software, particularly interactive end-user applications. Document-driven standards have pushed many projects to write elaborate specifications of poorly understood user interfaces and decision-support functions, followed by design and development of large quantities of unusable code (Boehm, 1988, p. 3).

Boehm concludes that alternatives to document-driven system development can, for instance, be evolutionary or risk-driven models. We claim that it is not possible to accomplish a rational design process. Reports are often used to make the process look rational. What is documented is what we want to happen, and how we would like the process to be (Parnas & Clements, 1986). When the goal of a procedure is reached, the results are documented, not all the means used to get there. The weak points are seldom reported. Thus, the discovery of failures through reviews and walkthroughs is difficult. This is supported by the conclusion of Feldman & March's (1981) study: organizations often collect information in order to legitimize decisions for the purpose of signalling a rational decision-making process.

Arguments that the documents do not mirror the practice do not hold in quality assurance, because of sincere verification. What is verified precisely is the documents, and these are in turn verified against other documents. Output documents from one phase are verified against input documents of the same phase.

Documentation has for a long time been reported as a problematic issue in software development (Weinberg, 1971; Parnas & Clements, 1986; Boehm, 1988). Documentation has often been considered as a burden by developers. It has also been regarded as a task additional to the 'real work' of design and programming. Documentation has low status and is not seen as a useful contribution to developer's work (Parnas & Clements, 1986; Sommerville, 1989).

If documents are not used or do not initiate action, the motivation for producing them will probably decrease and influence the quality of the documents. This is supported by findings of Parnas & Clements, 1986): 'Documentation that is not important to its author will always be poor documentation.'

Another problematic dimension of document production in system development is that it often leads to information overload (Feldman & March, 1981), owing to the emphasis on following strict documentation rules regarding all products and all activities in the process. Furthermore, the overview of the process and product may be cluttered by too much detailed information.

When quality assurance relies solely on documentation, problems which have already been documented will be transmitted to the quality system, and thereby decrease the effect of the quality assurance.

There is a need to stress flexibility in quality management in order to encompass a range of projects with respect to size, application area, complexity and work styles. The standard does not emphasize different levels of competence. The benefits will be least where good practice already exists.

The challenge is to develop suitable documentation techniques in order to relate documents to practice; create routines to handle the use of documents, so as to avoid producing documents which collect dust; and review the documentation procedures with the purpose of initiating action.

## 4.2 Fixed requirement specification

According to the ISO standard, the most important document in the entire development process is the requirement specification. This is clear in the following quotation:

In order to proceed with software development, the supplier should have a complete, unambiguous set of functional requirements. In addition, these requirements should include all aspects necessary to satisfy the purchaser's need (ISO 9000-3: 5.3 Purchaser's requirement specification).

This signals the possibility of specifying all aspects of the design, before the design process has started. Furthermore, the standard presupposes that the specification process should be closed before the system can be designed. This indicates that ISO 9000–3 presupposes separation in time and space between the specification and design activities. This fixed requirement specification presupposes a predictable development process — predictable concerning needs, requirements and properties. The knowledge that user claims and needs change during time (Davis et al., 1988), is not embedded in the quality system suggested by the standard. This is an old-fashioned view of system development (Floyd, 1987).

There are requirements that cannot be specified in advance, either because they are not known or because they cannot be formulated (Davis, 1982; Boehm, 1988). Users do not always know what they want. They are seldom trained to foresee the possibilities and consequences of technical proposals, nor are they experienced in doing so. In many practical situations, the claims can only be judged after the product has been in use for a while. Thus, the recommendations of the ISO 9000–3 are not sufficient for the assurance of use quality.

Since the standard takes requirement specification as its point of departure, important activities at the early stages of the system development process are left out, such as problem definition and the process of requirement specification.

Fixed requirement specification excludes work styles in which the experimentation to uncover user claims is an integrated element of the development process, as in prototyping:

Because of the complexity of software products, it is imperative that these activities be carried out in a disciplined manner, in order to produce a product according to specification rather than depending on the test and validation activities for assurance of quality (ISO 9000–3: 5.6 Design and implementation).

This paragraph explicitly states that the production should be done according to specification rather than depending on the test and validation activities for assurance of quality. Validation activities are related to subjective assessment and use quality, and are, as we can see, not emphasized in ISO 9000-3.

The ISO standard states that, whatever happens, the specification should be the frame of reference, not the usage or intuitive impression of the product. The responsibility for use quality is left to the customers who drew up the specification, assuming that the product actually satisfies the requirement specification.

## 4.3 Linear, phase-oriented system development

Linear, phase-oriented system development can be described by some sort of a waterfall model (Boehm, 1988). According to this perspective, each phase is defined by its input and output documents. The phases are documented and evaluated, and they follow each other logically: a linear, phase-oriented project can be planned and defined in advance,, and there is distance in time and space between specification and realization. A primary source of difficulty with the waterfall model has been its emphasis on fully elaborated documents as completion criteria for early requirement and design phases (Boehm, 1988).

The ISO standard is based on fixed requirement specifications and a document-driven system development process. These are preconditions for linear phase orientation (and linear phase orientation will be a natural consequence).

Whereas fixed requirement specifications involve completing the requirement specification before the design process can begin, this is not the case with evolutionary system development. Evolutionary system development assumes that the goals of the process, as well as the requirements of the product, will change during the project period (Budde et al., 1984; Kautz, 1993). Thus, the development process cannot be planned in detail at the time of project establishment. Only approximate goals can be stated, and the activities must be planned in cycles and sized according to the actual situation (Floyd et al., 1989). This is contradictory to ISO 9000–3, according to which change is deviation.

The guidelines in this part of the ISO are intended to describe the suggested controls and methods for producing software which meet a purchaser's controls and methods for producing software which meet a purchaser's requirements. This is done primarily by preventing nonconformity at all stages from development through to maintenance (ISO 9000–3: 1 Scope).

Suggested activities later in the standard follow this way of thinking. The product is what was specified with respect to the requirement specification or input to a phase (whether it is convenient or not).

Different situations demand different development strategies (Davis, 1982; Avison & Fitzgerald, 1988; Boehm, 1988). A phase-oriented development strategy could be appropriate when the problem to be solved is well defined or when the management problem is complex, e.g. large software development projects (Curtis et al., 1988). A cyclic or evolutionary development strategy is suitable when the problem area is more open or it is difficult to specify the computer system in advance. One method can never cover all situations. The choice of method depends on the size of the project, the resources available and the uncertainty of the tasks involved (Curtis et al., 1988; Andersen et al., 1990). Our point is that the standard signals one strategy, linear phase orientation, for all kinds of development processes. There is a need for flexibility in quality management regarding different strategies depending on project size, application area, complexity and work styles.

Dahlbom & Mathiassen (1993) discuss mechanistic and romantic views related to system development. We have found ISO 9001 to be based on a mechanistic view of quality assurance, meaning that the best way to obtain quality improvement is to transfer most of the developers' daily work to controllable routines and preferably to automate their daily work. This appears to stem from the origin of quality management ideas within manufacturing. This encourages the 'software factory' method of system development and discourages creativity and individuality.

System development is qualified work. Qualifications and motivation are not factors in generating a quality system in the ISO 9000–3 standard, although motivation and training are mentioned in ISO 9004: 18 Personnel. The one-sided focus on documented procedures, as assumed in the standard, may be a demotivating factor for the system developers. The best way to obtain quality is if those performing the quality work are motivated.

## 4.4 Ethics

Ethics usually means the theory of the foundation of systematic thinking about morals. Strongly simplified, the concepts can be summarized as follows: ethics in the theory of morals, morals are the set of norms and values which guide us in our daily actions, and norms are standards based in the society's or individuals' foundation of values or choices of values.

The application of the ISO standard raises ethical questions. In one way the emphasis on contracts is a strength for the customer, who is guaranteed the required product. On the other hand, with ISO 9000–3's strong reliance on requirements, if the requirements are of low quality they will still be fulfilled. We have recognized a tendency to applaud ISO's focus on specification, thereby strengthening the supplier's position in relation to the customer: 'Give the customer what they specified, nothing more, nothing less' (Hilding, 1993).

We claim that the ISO standard expresses an unethical approach, with good quality being interpreted as how well the design fulfils its specification: giving the customers/users what they happened to specify. This could set the norms for the conduct of system development. Consequently, the customer must be even more competent than the designer in specifying the functionality of the computer system. This could lead to an unethical tendency within the profession of system development.

## 5 EVALUATION OF THE ISO STANDARD ACCORDING TO THE MULTIPLE PERSPECTIVES ON QUALITY

In this section we discuss the ISO standard in an organizational context and related to the quality evaluation criteria: technical quality, use quality, aesthetic quality, symbolic quality, and organizational quality.

ISO 9001 focuses on technical quality, and leaves use quality up to the users' specifications. ISO gives guidelines for 'doing things right', but has no emphasis on 'doing the right things'. A metaphor could be delivering a Cadillac when the user needs a truck. Lientz & Swanson (1980) and Sørgaard (1989) have reported that giving low priority to use quality is the cause of a great deal of user dissatisfaction with delivered systems. Consequently, use quality should be addressed in order to meet these problems. ISO's quality concept and guidelines do not take care of needs or expectations that are subjective or informal. In addition, we find that user participation in general, and user participation as a contributor to design in particular, is absent from the ISO standard, in spite of the fact that participatory design has gained increasing approval (Nakioka & Schuler, 1992).

ISO 9004, which gives guidelines for the whole 9000 series, mentions aesthetic quality in one sentence, related to product specification and service requirement (ISO 9004: 8.5.2. Elements of design reviews), but this is not embedded in 9000–3.

The focus on technical quality also leaves symbolic quality outside the scope of the ISO standard.

The focus on certification may easily lead to the development of a quality system in the direction of a symbolic process, in which certification is a means of gaining market shares. The ISO 9001 certificate frame behind glass, and visible to all visitors to the certified organization, symbolizes a quality organization providing confidence and security to its customers (Rothery, 1992). This finding is supported by the definition of quality assurance in the standard (ISO 8402. Quality — Vocabulary), which says that the aim of quality assurance is to provide confidence. A certified organization is assumed to be modern and well run and creates confidence. The point is not to assure quality, but to assure the clients of the supplier's potential to produce quality.

ISO 9001, with its focus on documents and phases, represents traditional system development and established knowledge, and may act as an obstacle to innovation of work styles. Used more critically, quality assurance can contribute to transparency of the development process. Furthermore, it can contribute to reflection and discussion of work styles among the system developers and thereby the innovation of work styles in system development.

The relation between tradition and innovation is also important when discussing the development process, in order to achieve organizational quality. Quality assurance according to ISO could mean organizing the system development process is a more bureaucratic way. By a bureaucratic organization we mean a hierarchical organization with strong division of work and clear and documented responsibilities and procedures for every work task.

Much of the success of computer systems is dependent on creativity in design and solutions. System development projects are characterized by frequent new developments. When people work together in such environments, they have to be creative, innovative and mutually supportive. These human properties are necessary to design quality computer systems. The bureaucratic ideas expressed by the ISO standard could oppose creativity and innovation. Bureaucracy in organizing is most suited for repeatable pieces of work, to be carried out as fast as possible over a long period of time (Weber, 1964; Fulmer, 1989). More modern approaches to organization and management emphasize cooperation, social needs and the co-workers' creativity and responsibility (Weinberg; 1986; Humphrey, 1987; Fulmer, 1989). If application of the ISO standard means that we implement a bureaucratic conduct of system development, it will conflict with a modern view on how to design an artefact.

## 6 DEVELOPMENT OF ADDITIONAL TECHNIQUES FOR QUALITY ASSURANCE

The challenge now is to make quality assurance applicable to more evolutionary system development, providing appropriate techniques and guidelines for documentation and validation. Two techniques, one addressing process documentation and one use quality, are suggested. Additional techniques for quality assurance should be topics for further research.

## 6.1 Decision diaries

Quality assurance contributes to the transparency of the system development process. A critical issue is documentation, which make the transparency possible. If the documents do not mirror the actual practice and do not capture faults and mistakes, there will be less possibility of using the documents to learn from previous faults. Producing documents for the bookshelf only leads to the view that documentation procedures are unnecessarily bureaucratic. Prescriptive documentation expresses previous experience and work traditions. Both prescriptive and descriptive documentation are necessary in system development and quality assurance. One problem in quality assurance is poor process documentation. One possible approach is to use decision diaries (Braa, 1994) combined with checklists and plans. Decision diaries are extensions of project diaries (Jepsen et al., 1989), with special emphasis on decisions made during the project. The pros and cons of the decisions are logged. This descriptive documentation technique could be combined with prescriptive documents such as checklists and plans, by embedding them in the diaries. Descriptive documentation is flexible because it is suitable for different work styles.

## 6.2 Priority workshop

Post-implementation activities are often done as a sequence of random solutions to satisfy the continuous flow of requests for change (Lientz & Swanson, 1980; Sørgaard, 1989). Both the technical quality and use quality of the computer system may be influenced by such random solutions, suffering from the lack of reflective planning and organization of the redesign process. As one attempt to address use quality in the context of redesign, we suggest arranging priority workshops (Braa et al., 1992; Braa, 1994). Priority workshops as a redesign technique are an institutionalized series of workshops throughout the life cycle of the computer system. A priority workshop aims to:

● make priorities transparent to those who are affected;

● facilitate an overview of different use practices;

● avoid arbitrary decisions of priorities;

● create an opportunity for designers to reflect over design decisions;

● create an opportunity for users to influence the design decisions; and

● support communication between designers and users.

A priority workshop is a forum for discussion with the goal of bridging the gap between designers and users, and between different user groups. This is done in order to put use quality on the agenda and make possible conflicting interests or claims transparent as early as possible.

Representatives of different user groups should participate in the workshop. Priorities are expressed in illustrations such as prototypes or mock-ups in order to gain insight into the consequences of the different design proposals.

The priority workshop technique has been empirically tested in a developer organization cooperating with users from a number of customer organizations (Braa, 1994). The results indicate that the priority workshop could be a useful means to evaluate use quality in collaboration with both users and designers.

## 7 CONCLUSION

The ISO standard initiates quality assurance activities too late in the system development process. Quality assurance should be initiated at the early stages of system development, i.e. during the requirement specification process.

A way to use the ISO standard without limiting the system development process is to regard the standard as a template, and to integrate the many perspectives of quality into the topics of concern.

We have found that the ISO standard signals old-fashioned ideas of system development. Our findings can be summarized as follows:

\- ISO 9001 expresses a narrow view on quality, solely connected to the product. Computer systems tend to be regarded as finished products, while the continuous development of computer systems in use is not taken into account.

\- The technical perspective on quality leads to an evaluation of a computer artefact based solely on objective claims and not on subjective expectations.

\- The standard ignores the many perspectives of quality: use quality, aesthetic quality, symbolic quality and organizational quality.

\- In spite of the approval of user participation in order to obtain use quality, user participation is not mentioned in the standard.

\- The standard expresses the idea that system development can and should be managed by rules, disregarding creativity, innovation and individual work styles among the designers.

\- ISO 9000–3 presupposes a fixed requirement specification, and system development is treated as a predictable process. The standard presupposes that it is possible to prescribe the customers' needs in measurable requirements, before development starts, disregarding the fact that both users and designers learn about the work and the technological possibilities in a use context, during the development process.

\- ISO 9000–3 is based on document-driven system development, with less emphasis on situated action.

\- ISO 9000–3 signals the idea of a linear phase-oriented system development model, not facilitating experimental and cyclic development models.

\- The ISO standard expresses an unethical approach: giving the customers/users what they happened to specify. This could lead to an unethical tendency within the profession of system developers.

The standard is designed for and by lawyers instead of computer professionals. Thus, the standard is difficult to understand and interpret. This reduces the usability of the standard as a tool to implement quality assurance in an organization.

Unless the standard is used critically, and unless the many perspectives of quality are taken into account, this could be a step back in the theory and practice of system development. Research and development of new approaches to avoid the weaknesses of traditional phase-oriented system development could be impaired. In this way, the application of the ISO standard could be the source of new problems in system development.

International standardization work takes time. The consequence is that we are stuck with a standard that reflects old-fashioned ideas (where we were 10 years ago) of system development. In the discipline of information systems, this can be a major drawback. Consequently, we need to treat the standard as it is, an old-fashioned standard, and use it in a more evolutionary way.

## ACKNOWLEDGEMENTS

We would like to thank Oddvar Hesjedal for useful comments on earlier versions of this paper. Our colleagues Jens Kaasbøll, Gro Bjerknes and Riitta Hellman have made useful comments. The quality discussion has been inspired by the book by Dahlbom & Mathiassen (1993). Last but not least, we would like to thank Trevor Wood-Harper for encouraging us to complete this paper.

Parts of the paper were presented at the HICSS conference (Braa & ∅grim, 1994.)

## REFERENCES

Andersen, N.E., Kensing, F., Lundin, J., Mathiassen, L., Munk-Madsen, A., Rasbech, M. & Sørgaard, P. (1990) Professional Systems Development, Experience, Ideas and Action. Prentice Hall, Hemel Hempstead.

Avison, D.E. & Fitzgerald, G. (1988) Information Systems Development. Methodologies, Techniques and Tools. Blackwell Scientific Publications, Oxford.

Bang et al. (1991) Kvalitetsstyring i Systemudvikling (Quality Management in System Development). Teknisk Forlage, København.

Baroudi, J., Olson, M.H. & Ives, B. (1986) An empirical study of the impact of user involvement on system usage and information satisfaction. Communications of the ACM, 29 (3), 232–238.

Bjerknes, G., Ehn, P. & Kyng, M. (1987) Computers and Democracy: A Scandinavian Challenge. Avebury Gower Publishing, Aldershot.

Bjerknes, G., Bratteteig, T. & Espeseth, T. (1991) Evolution of finished computer systems: the dilemma of enhancement. Scandinavian Journal of Information Systems, 3, 25–45.

Boehm, B.W. (1988) A spiral model of software development and enhancement. IEEE Computer, 61–72.

Braa, K. (1992) Influencing system quality by using decision diaries in prototyping projects. In: Proceedings of the Participatory Design Conference, Muller et al. (eds), pp. 163–171. Cambridge, MA.

Braa, K. (1994) Priority Workshops as a springboard for user participation in redesign activities. In: Proceedings of the 17th Information Systems Research Seminar in Scandinavia (IRIS 17) Kerola et al. (eds), Syöte, Finland.

Braa, K., Bratteteig, T. & Ogrim, L. (1994) Organising the redesign process in systems development. In: Proceedings of the Fourth International Conference on Information Systems Development — ISD '94 Zupancic & Wrycza (eds), Slovenia.

Braa, K. & ∅grim, L. (1994) Quality assurance — an assurance of quality. Application of the ISO Standard in system development. In: Proceedings of the 27th Annual Hawaii International Conference on System Sciences, Nunamaker & Sprague (eds), 842–851, Vol IV, IEEE Computer Society Press.

Briefs, U., Ciborra, C. & Schneider, I. (1982) Systems Design For, With and By the Users. North-Holland Publishing, Amsterdam.

Budde, R., Kuhlenkamp, K. & Mathiassen, L. (1984) Approaches to Prototyping. Springer, Berlin.

Burr, J.T. (1990) The future necessity. Quality Progress, 23, 19–23.

Checkland, P. (1981) Systems Thinking, Systems Practice.
John Wiley, Chichester.

Checkland, P. & Scholes, J. (1990) Soft Systems Methodology in Action. John Wiley, Chichester.

Curtis, B., Krasner, H. & Iscoe, N. (1988) A field study of the software design process for large systems. Communications of the ACM, 31 (11).

Dahlbom, B. & Mathiassen, L. (1993) Computers in Context. The Philosophy and Practice of Systems Design. NCC Blackwell, Cambridge, MA.

Davis, A.M., Bersoff, E.H. & Comer, E.R. (1988) A strategy for comparing alternative software development life cycle models. IEEE Transactions on Software Engineering, 14, 1453–1461.

Davis, G.B. (1982) Strategies for information requirements determination. IBM System Journal, 21.

Ehn, P. (1988) Work-oriented design of computer artifacts. PhD thesis, Arbetslivscentrum, Stockholm.

Feldman & March (1981) Information in organizations as signal and symbol. Administrative Science Quarterly, 26, 171–186.

Floyd, C. (1987) Outline of a paradigm change in software engineering. In: Computers and Democracy, Bjerknes et al. (eds), 191–210. Gower Publishing, Vermont.

Floyd, C. Reisin, F.-M. & Schmidt, G. (1989) STEPS to software development with users. In: ESEC 1989, 48–64. University of Warwick, Coventry.

Fulmer, R.M. (1989) The New Management. Macmillan Publishing, New York.

Gillies, A.C. (1992) Software Quality. Theory and Management. Chapman & Hall, London.

Greenbaum, J. & Kyng, M. (1991) Design at Work: Cooperative Design of Computer Systems. Lawrence Erlbaum, NJ.

Hilding, F. (1993) Experiences from the application of ISO 9000. In: A Critical View on ISO and Quality Assurance. The Norwegian Computer Association, Oslo.

Humphrey, W.S. (1987) Managing for Innovation. Leading Technical People. Prentice-Hall, Englewood Cliffs, NJ.

ISO 8402 (1986) Quality — Vocabulary.

ISO 9000 (1987) Quality management and quality assurance standards.

ISO 9000-3 (1991) Quality management and quality assurance standards — Part 3: Guidelines for the application of ISO 9001 to the development, supply and

maintenance of software.

ISO 9001 (1987) Quality Systems — Model for quality assurance in design/development, production and servicing.

Jepsen, L.O., Mathiassen, L. & Lielsen, P.A. (1989) Back to thinking mode — diaries as a medium for effective management of information systems development. Behaviour and Information Technology, 8, 207–217.

Kautz, K. (1993) Evolutionary System Development. Supporting the Process, Research Report No. 178. DPhil thesis. Department of Informatics, University of Oslo.

Kim, K.K. (1989) User satisfaction: a synthesis of three different perspectives, Journal of Information Systems.

Kitchenham (1989a) Software metrics. In: Software Reli-
possibility Handbook, Rook, P. (ed.). Elsevier.

Kitchenham (1989b) Software quality assurance. Microprocessors and Microcomputers, 13, 373–381.

Lientz, B.P. & Swanson, E.B. (1980) Software Maintenance Management, A Study of the Maintenance in 487 Data Processing Organizations. Addison-Wesley, Reading, MA.

Lyytinen, K. (1987) Towards a dynamic information failure concept — a stakeholder analysis approach. In: The Report of the 10th IRIS Seminar, Järvinen, P. (ed.), 495–510. University of Tampere, Tampere.

McCall, J., Richards, P. & Walters, G. (1977) Factors in Software Quality, Vols I–III, Technical Report. Rome Air Development Center, USA.

Namioka & Schuler (1992) Perspectives on Systems Design: Participatory Design. Lawrence Erlbaum, NJ.

Nygaard, K. (1986) Program Development as a Social Activity. North-Holland, Amsterdam.

Nygaard, K. & Sørgaard, P. (1987) The perspective concept in informatics. In: Computers and Democracy: A Scandinavian Challenge, Bjerknes et al. (eds). Avebury Gower Publishing, Aldershot.

Øgrim, L. (1993) Ledelse av systemutviklingsprosjekter. En dialektisk tilnærming [Management of system development projects. A dialectical approach (in Norwegian)]. DSci thesis, Department of Informatics, University of Oslo.

Parnas, D.L. & Clements, P.C. (1986) A rational design process: how and why to fake it. IEEE Transactions on Software Engineering, SE-12 (2), 251–257.

Pirsig, R.M. (1974) Zen and the Art of Motorcycle Maintenance. Bodley Head.

Roetzheim, W.H. (1988) Structured Computer Project Management, Prentice Hall, Englewood Cliffs, NJ.

Rothery, B. (1992) ISO-9000. Gower Publishing.

Sommerville, I. (1989) Software Engineering. Addison Wesley, Wokingham.

Sørgaard, P. (1989) An Overview of Research in Maintenance, Rapporter från Åbo akademi, informationsbehandling & matematik, Ser. A, No 94, Åbo akademi, Departments of Computer Science and Mathematics.

Stage, J. (1989) Mellem tradition og nyskabelse: Analyse og design i systemudvikling [Between tradition and innovation: analysis and design in system development (in Danish)]. DSci thesis, Department of Informatics, University of Oslo.

Stolterman, E. (1991) Designarbetets dolda rationalitet PhD thesis, Research Report no. 14.91. Information Processing and Computer Science, Institutionen för Informationsbehandling, Administrativ Databehandling. University of Umeå.

Suchman, L.A. (1987) Plans and Situated actions. The Problem of Human Machine Communication, Cambridge University Press, Cambridge.

Weber, M. (1964) Makt og byråkrati (Power and Bureaucracy). Gyldenhal, Oslo.

Weinberg, G.M. (1971) The Psychology of Computer Programming. Van Nostrand Reinhold, New York.

Weinberg, G.M. (1986) Becoming a Technical Leader. An Organic Problemsolving Approach, Dorset House, New York.

## Biography

Kristan Braa is a researcher at the Department of Informatics, University of Oslo. During the last 3 years, she has been a researcher in the research project Functional Integration through Redesign (FIRE). She is currently writing her PhD thesis on quality assurance in participatory design. Her main area of interest is new participatory techniques in the context of redesign processes. In addition, she is concerned with ethical questions of quality assurance.

Leikny ∅grim is currently working as researcher and district manager in ITOS (Norwegian Network for Information Technology, Organization and Management). In addition, she holds a part-time position as an associate professor at the Department of Informatics, University of Oslo. Until recently, she was a researcher in the research project Functional Integration through Redesign (FIRE). Her PhD thesis in computer science discussed project management from a dialectical point of view. Ethical questions related to quality assurance is also one of her current research themes.
