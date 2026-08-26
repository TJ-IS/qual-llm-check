---
otero_id: 23684
otero_key: "NRNXWN23"
title: "Systems development methodologies: unanswered questions"
authors: "Judy L Wynekoop; Nancy L Russo"
year: "1995"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1995.9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Systems development methodologies: unanswered questions

JUDY L. WYNEKOOP

Division of Accounting and Information Systems, The University of Texas at San Antonio, San Antonio, TX 78249, USA

NANCY L. RUSSO

Operations Management and Information Systems, Northern Illinois University, DeKalb, IL 60115, USA

Despite over a decade of study, little is really known about information systems development and the use of systems development methodologies. There has been little evaluation of methodologies in use or examination of the selection, development, adaptation or use of methodologies in practice. This paper discusses this lack of knowledge and its ramifications for research and practice.

## Introduction

Over a decade ago, IFIP WG 8.1 initiated the Comparative Review of Information Systems Design Methodologies (CRIS) because ‘... it seemed inappropriate for the Working Group to develop further ... approaches [to developing information systems] without first undertaking some kind of systematic study of the existing state of the art’ (Olle, 1982, p. 1). However, more than a decade later, little more is known about the ‘existing state of the art’.

Although many systems development methodologies exist, there is no universal agreement that existing methodologies are useful today (Lyytinen, 1989; Baskerville et al., 1992), nor is there agreement that they have ever been useful (Lyytinen, 1987a). Most research to date has focused on the development of new methodologies and frameworks for the selection and understanding of methodologies, rather than on their evaluation or use in practice.

The narrow focus of the current research paradigm has critical ramifications. By failing to evaluate current methodologies, practices and needs, researchers may develop methodologies that are not only irrelevant, but flawed (Lyytinen, 1987a). In turn, systems produced using these methodologies may be unsuccessful.

This paper surveys existing literature on systems development methodologies and challenges researchers to understand how systems are developed in today's organizations, how well methodologies work and what practitioners need today and in the future, before more guidelines or methodologies are developed. Without assessing where the field is now, the next generation of development technologies, such as methodologies or computer-aided software engineering (CASE) tools, may at best be of little use.

## Background

The bottom line in practice and research is that despite the development and promotion of a plethora of methodologies and selection frameworks, there remains no generally accepted theory of systems development, nor has there been a systematic investigation of evidence of the deficiency of methodologies in use (Bubenko, 1986; Lyytinen, 1987a). As a starting point for understanding the complexities faced by those attempting to study and use methodologies, this section discusses the role of methodologies in the development process and the difficulties encountered when trying to define what a methodology is (or isn't).

## History and purpose of methodologies

Development methodologies were originated to improve the management and control of the software development process, structure and simplify the process and standardize the development process and product by specifying activities to be done and their relationships. Early methodologies were based on corporate development standards (Meredith, 1986). Today, methodologies may be commercial (sold or recognized outside a single organization), 'homegrown' (developed and used within one organization) or academic (developed and used within a research context).

## What is a methodology?

Divergent opinions of what constitutes a methodology are problematic when applying or discussing research. Although a complete discussion is beyond the scope of this paper, in this section some of the viewpoints are discussed and ‘methodology’ as it is used in this paper is defined.

First there is the method versus methodology debate. Some argue that, since methodology means a ‘science of methods’, the term has no place in information systems (Baskerville et al., 1992; Schach, 1993). There are also those who use ‘method’ and ‘methodology’ interchangeably (Colter, 1984; Connors, 1992), those who consider ‘methods’ to encompass ‘methodologies’ (Davis, 1982; Hackathorn and Karimi, 1988) and those who believe ‘methodologies’ encompass ‘methods’ (Hirschheim, 1985; Lantz, 1985). Some maintain there are no methodologies, only techniques (Keyes, 1992). Because it appears that ‘methodology’ is still the most widely used term, it is used in this paper.

Second, what is a methodology? Definitions run from the broad ‘... a set of guidelines that prescribe a behavior in order to think and act in a situation’ (Nielsen, 1989, p. 82), to the precise ‘... specific, step-by-step strategies for completing one or more phases of the systems development life cycle ... [imposing] tools and standards on the SDLC’ (Whitten et al., 1989, p. 111). Many practitioners consider a methodology to be simply a ‘way of doing things’ (Angell and Straub, 1993, p. 5). Methodology has been used to refer to a single phase in the development process (Schach, 1993) and to ‘all aspects [of development] from initial problem identification ... to the design of alternative solutions’ (Bantleman and Jones, 1984, p. 214). Many publications omit definitions. Given the divergent opinions of what constitutes a methodology, it is essential to define the term in any discussion.

Furthermore, the terms systems development methodology and software development methodology are often used interchangeably. For example, Jackson System Design has been referred to as both (Fitzgerald et al., 1985; Cameron et al., 1991; Song and Osterweil, 1992). Generally, software development methodology refers to the design and production of software and programs only, while systems development methodology includes the analysis, design and implementation of not only the software but at least some part of the system in which it exists (e.g. procedures, people and structure). Thus, software development methodologies are a subset of systems development methodologies. Here, we focus on systems development methodologies, while acknowledging that some may not extend much beyond software development.

Three distinct entities have been called methodologies in the information systems (IS) literature. We offer the following definitions of these three concepts, largely based on IEEE (1987), Lyytinen (1987a) and Schach (1993), to clarify terminology as it is used in this paper.

(1) Methodology: a systematic approach to conducting at least one complete phase (e.g. design or requirements analysis) of software production, consisting of a set of guidelines, activities, techniques and tools, based on a particular philosophy of system development and the target system.

(2) Technique: specific steps for conducting a portion of a phase of software production (e.g. design techniques).

(3) Software process model: a representation of the sequence of stages (e.g. requirements analysis, specification, planning, design, implementation, integration, maintenance and retirement) through which a software product evolves.

Methodology is used by some to mean methodology as defined above, but by others to mean a software process model or a technique. For instance, structured analysis and system specification has been called a methodology (Olle et al., 1988; Nielsen, 1989) and a technique (Mendes, 1980). Prototyping has been referred to as a methodology (Burns and Dennis, 1985; Lantz, 1985; El Louadi et al., 1991; Fazlollahi and Tanniru, 1991; Burch, 1992; Plyler and Kim, 1993), a technique (Jayartna, 1988; Olle et al., 1988) and a process model (Schach, 1993). Is the systems development life cycle (SDLC) a methodology (Palvia and Nosek, 1990; Plyler and Kim, 1993) or a process model (Schach, 1993)? Even computer-aided software engineering (CASE) has been called a methodology (McLaughlin, 1993).

According to the definitions used here, information engineering (Finkelstein, 1989), structured analysis and system specification (DeMarco, 1978), SADT (Ross, 1985), PSL/PSA (Teichroew and Hershey, 1977) and Jackson System Development (Jackson, 1983) are examples of methodologies. Prototyping $^{1}$ , the waterfall model and the spiral model are process models. Joint application design and data flow diagramming are techniques. CASE is a tool.

At best, inconsistent terminology in the literature is confusing. The confusion is not surprising, since methodologies and process models are tightly intertwined (Floyd, 1986). Methodologies are defined within frameworks provided by software process models. For example, information engineering, a methodology, defines techniques, deliverables and activities within the framework provided by the waterfall process model.

However, the problem is more than mere semantics and has implications for methodology research and practice. It is difficult, if not impossible, to evaluate or apply the results of research when the object of study is unclear. For example, surveys that compare the use or effectiveness of prototyping to the SDLC or 'structured

2. How are methodologies selected?

approaches' to prototyping (e.g. Mahmood, 1987; Necco et al., 1987) are problematic, since different methodologies may be used within each development process. That is, company A's SDLC might include very different methodologies and techniques than company B's, thus producing different results.

Although this paper adheres to the definitions above, due to the interrelationship of process models and methodologies and their interchangeability in the literature, both are included in the research discussed here. The term ‘information system development method’ (ISDM) is used to incorporate both methodologies and process models and methodology to refer to methodology only. Research in both areas is vital, but researchers (and readers) must identify the phenomena under study and the validity of comparisons or conclusions.

## The problem

Much IS development research implicitly assumes that (1) methodologies are used and are useful and effective and (2) the frameworks that have been developed to evaluate and select methodologies are useful.

These assumptions have not been validated and should be examined. There are indications in the trade literature that they are unfounded (Yourdon, 1986; Keyes, 1992). We must understand how systems are developed, evaluate currently used and proposed methodologies and find out what is needed before we propose new ways to develop information systems. Although researchers may not need to understand every detail of current practice, we should have at least a general knowledge of what is done, how well it works and what is needed. In the following section, a preliminary list of research issues is discussed.

## Unanswered questions

Because of the inadequate base of empirical evidence, numerous questions about methodologies remain. Four major research issues addressing these questions are presented in Table 1. Each of the issues is discussed below, focusing on what is known from the research that has been done in the area and what is still unknown.

## Are methodologies used? If not, why not?

This appears to be a simple question. However, the answer is not yet known. Most studies to date provide only a general idea of methodologies in use, since they do not distinguish process models from the methodologies (cf. Necco et al., 1987; Dekleva, 1992). In one survey,

Table 1 Methodologies: unanswered questions

3. Do methodologies work?

the confusion of methodologies, tools and techniques by respondents was noted by the authors (Beck and Perkins, 1983). In a 1987 survey, approximately two-thirds of a 97-firm sample used traditional IS development approaches, the SDLC and structured methodologies, while less than half used prototyping and organizations often used more than one ISDM (Necco et al., 1987). In a more recent survey, over three-quarters (76%) of a 133-firm sample reported using an SDLC-based approach to system development (Russo and Klomparens, 1993).

In 1986, Yourdon claimed that only 10% of North American information systems organizations used structured ‘techniques’ in a ‘disciplined fashion’. On the other hand, a year later, survey results were published showing that 69% of the sample used structured ‘approaches’ to developing information systems (Necco et al., 1987). Which is right? Since the extent to which survey respondents used structured methodologies is unclear, it is impossible to know.

Perhaps the question should not be whether or not methodologies are used, but to what extent methodologies are used. It should not be assumed that because an organization has a methodology that all projects follow it (Thayer et al., 1981; Pressman, 1989), nor should it be assumed that survey respondents know how systems are developed in their organizations. For example, in a recent survey, almost one-quarter of the 112 IS managers responding described their methodology as ‘unknown’ (Dekleva, 1992).

The European Community's Euromethod program has made some progress in identifying methodologies in use. For instance, it is known that SSADM, Merise and SDM have the greatest market share in the United Kingdom, France and The Netherlands, respectively (Flynn and Fragoso-Diaz, 1993). However, similar studies of methodology use in other parts of the world have apparently not been published.

An indication of the reasons methodologies may not be used can be found in a field study of the design of large systems (Curtis et al., 1988). Although the study's focus was the design process, rather than methodologies, many software engineering practices were found to fall apart when applied to large systems with deadline pressures. Interviewees indicated that conditions surrounding their projects prevented ideal development practices from being used. Similarly, a study of SSADM use in the United Kingdom found that government organizations' goals of fast development were incompatible with the added development time of SSADM, causing usage to falter (Sauer and Lau, 1994). More studies of this type are needed to help identify why methodologies are not used or how they are used.

Surveys have been the dominant research method used to examine this question. At best, surveys provide a snapshot of methodology use – a general idea of what methodologies are in use. To understand the motivations for using particular methodologies in particular contexts and the historical and contextual influences on the use or non-use of methodologies, longitudinal field research, particularly interpretive research, is necessary.

Corollaries to this question include 'How are systems developed when no methodology is used and what happens when methodologies are not used?' and 'Is a methodological development successful?' Only a database of qualitative and quantitative results from numerous field studies will answer these questions. Without answers to these questions, there is no basis for creating new development technologies, such as methodologies, techniques, process models or CASE tools.

## How are methodologies selected?

Assuming methodologies are used, how do practitioners select them? When organizations decide to develop their own methodologies in-house, how is it done? Most publications on methodology selection have been frameworks or guidelines to help the reader understand (e.g. Fitzgerald et al., 1985; Olle et al., 1988; Song and Osterweil, 1992), classify (e.g. Wood-Harper and Fitzgerald, 1982; Hackathorn and Karimi, 1988) or select (e.g. Wood et al., 1988; Nielsen, 1989; El Louadi et al., 1991; Connors, 1992; Karam and Casselman, 1993) methodologies. Although existing frameworks to compare methodologies have been criticized as inadequate (Cameron et al., 1991), no empirical validation of the frameworks or empirical studies of methodology selection could be found.

## Methodology selection

Practitioners are faced with numerous methodologies. Since one cause of development failure is the use of inappropriate or inadequate methodologies, it is important that practitioners choose the correct methodologies or techniques (Lyytinen, 1987a; Nielsen, 1989). Yet, although taxonomies and selection guidelines have proliferated, they have not been empirically validated, nor do we know how methodologies are successfully selected in practice. Although surveys may provide preliminary answers, qualitative research is needed to understand the motivations of and influences on the selection process.

One limited survey on SSADM selection conducted in the United Kingdom found that most organizations had adopted SSADM because it was the official methodology for government agencies and that only 11% of the respondents had used a formal methodology before adopting SSADM (Edwards et al., 1989a). Practitioners' narratives also offer some insight into how methodologies are selected. For example, Imperial Oil had been using a methodology that addressed only structured analysis and programming and adopted information engineering because it addressed the whole life cycle and emphasized enterprise modelling – two priorities of the organization (Van De Velde, 1992). However, a large database of such anecdotes would be necessary to understand the methodology selection process and dynamics, as well as the issues and priorities considered in selecting a methodology.

## Methodology development and adaptation

Some organizations develop their own methodologies or adapt commercial methodologies for internal use. In a recent survey of over 100 organizations, 65% of the organizations had developed their methodology in-house rather than purchase a commercial one (Russo and Klomparens, 1993). However, little is known about the nature of ‘homegrown’ methodologies or how they are developed.

The little that is known comes primarily from a small base of survey results and practitioners' narratives describing events in a single organization. For instance, it is known that New York Life has used a structured homegrown methodology incorporating data modelling since 1984 and that CASE tools were acquired to support it since developers considered the methodology to be tedious (Zagorsky, 1990). But it is not known why this particular methodology was used, how well it worked, how it was developed or whether it would work in another context.

The adaptation of methodologies to fit a particular situation appears to be common. Most IS managers believe that methodologies should be adapted on a project-by-project basis (Russo and Klomparens, 1993). A UK survey indicates that many SSADM users have adapted the methodology by adding or omitting techniques and steps (Edwards et al., Smith, 1989a, b, c). Additional evidence indicates methodologies may be purchased and adapted because it is cheaper than developing a new methodology in-house and that methodologies must be continually refined to meet changing needs (Van De Velde, 1992). In addition to adapting a single methodology to specific situations, different methodologies may be used on different projects (Edwards et al., 1989a). However, it is not clear how such decisions are made or how such adaptation is done, how frequently it is done, whether there are any controls over the changes and how well the adapted methodologies work. Some believe that today's IS organizations may not have mastered methodologies enough to develop or adapt them safely (Keyes, 1992).

One small study found that methodology adaptation is done by trial and error, often prompted by the purchase of a CASE tool incompatible with existing practices or the use of an inadequate, non-standard methodology that required improvement (Smolander et al., 1987).

Again, although surveys might provide some insight into the development of homegrown methodologies, longitudinal, qualitative studies are needed to provide an understanding of the reasons for, process of and influences on the development of homegrown methodologies. Answers to these questions are important to shape new system development technologies to improve the development process and resulting software products.

## Do methodologies work?

Deficiencies in methodologies have been cited as a cause of IS failure (Lyytinen, 1987a, b). Assuming that methodologies are used, are they effective? What do they accomplish? The answers to these questions lie in research to evaluate methodologies. Unfortunately, we found few published systematic evaluations of methodologies in use under realistic conditions. Exceptions to this include evaluations of methodologies primarily used in Europe, including SSADM (Edwards et al., 1989a, b, c; Westrup, 1993; Middleton, 1994), soft systems methodology (Checkland and Scholes, 1990) and Multiview (Avison and Wood-Harper, 1991). These are useful, but barely start to provide adequate information to provide guidelines for successful methodology use.

The CRIS workshops began to evaluate methodologies. The second workshop (Olle et al., 1983) consisted largely of 'paper' comparisons and evaluations of methodologies. In CRIS I (Olle et al., 1982) and CRIS III (Olle et al., 1986), a limited number of methodologies were evaluated by using them on a standard case problem. Unfortunately, few evaluations in practice were done. Floyd's (1986) evaluation of four methodologies used by college students on case study problems was the closest to evaluation under realistic conditions. CRIS has been an outstanding start, but an academic exercise if not followed by evaluations of methodologies on real problems in real contexts.

There have also been ‘paper’ evaluations of methodologies outside CRIS. These generally discuss the strengths and weaknesses of selected methodologies according to criteria the authors identify as important (e.g. Avison and Fitzgerald, 1988; Nielsen, 1989; Klein and Hirschheim, 1991). One such evaluation concluded that methodology authors leave many parts of their methodology vague and hard to understand (Karam and

Casselman, 1993) - even more reason to evaluate methodologies in use.

Recent field studies and surveys have only begun to evaluate the effectiveness of methodologies. A study of 65 maintenance projects from one firm indicated that the use of structured methodologies for maintenance increased the time spent on analysis and design activities (Banker et al., 1991). A survey of 122 IS organizations found no relationship between the use of ‘modern’ development methods (defined in the study as structured methods, information engineering, prototyping or CASE tools versus the traditional SDLC) in original development and the total amount of time spent maintaining systems, although use did decrease the amount of time spent correcting errors (Dekleva, 1992).

A field study of eight firms found that when methodologies were used, they were considered helpful (Smolander et al., 1987), and a recent survey found that only 45% of a sample of over 100 IS managers were satisfied with their methodology, but failed to note why 55% were not satisfied (Russo and Klomparens, 1993). A field study of SSADM users found that most who had used it for analysis and logical design were satisfied, however less than half who had used it for physical design were satisfied (Edwards et al., 1989a, b, c). Unfortunately, a very large base of such studies addressing multiple methodologies will be necessary before conclusions can be drawn from them.

Published practitioner evaluations of their methodologies are infrequent and their contribution is useful, but limited. For example, although it is known that Exxon used a methodology based on Jackson's Program Design methodology and that productivity did increase as a result of its use (Menard, 1980), it is unclear how this methodology would work in different contexts or how the methodology evolved. A large collection of such practitioner accounts would be necessary to evaluate even a single methodology.

The evaluation of object-oriented methodologies has only started. For example, two object-oriented design methodologies were used by researchers on the same problem and the resulting designs measured for complexity (Sharple and Cohen, 1993). Large-scale studies of real systems will provide more information.

It has been acknowledged that all methodologies are not equally applicable in all situations (Malouin and Landry, 1983; Episkopou and Wood-Harper, 1986; Jayartna, 1988; Nielsen, 1989; Kumar and Welke, 1992). Methodologies have been characterized by their strengths and weaknesses (Avison and Fitzgerald, 1988) and selection frameworks have been proposed (e.g. Wood et al., 1988; Nielsen, 1989; El Louadi et al., 1991). However there is little empirical insight into why some methodologies might be better than others in certain situations.

Laboratory studies comparing prototyping to the SDLC or evaluating parts of ISDMs have been conducted (Boland, 1978; Alavi, 1984; Boehm et al., 1984). One field survey confirming their results was found (Necco et al., 1987), while one found users had no real preference (Mahmood, 1987). Another survey found that the SDLC was used for operational systems and management information systems and prototyping was used for decision support systems and executive information systems (Palvia and Nosek, 1990). Although these results are informative, rather than addressing specific methodologies, they address ISDMs in general. Therefore it is not clear how many methodologies were actually studied, since numerous methodologies may have been represented in the samples.

Researchers have only begun to understand the kinds of methodologies appropriate for certain kinds of systems, contexts or goals. While additional surveys may be informative, the application of specific methodologies to specific problems must be examined in the field to understand the contexts and uses contributing to the success or failure of a methodology.

This question raises a difficult issue: how do we define, much less measure, the ‘success’ of a methodology? Is it developer, MIS Director or user satisfaction with the process and/or product, design complexity or software maintainability? Is it all these things? Although researchers may develop their own measures, metrics used to evaluate methodologies in practice should be identified.

Evidence is emerging that any methodology is beneficial only in the context of an organization with a pre-existing ability to produce quality software (Humphrey, 1989; Loy, 1993). Therefore, methodologies must be evaluated in the context in which they are used. Without a large base of systematic evaluations of various methodologies in different organizations, no concrete conclusions can be drawn. Again, although surveys and laboratory experiments may provide some information, field experiments and qualitative research will be needed to truly understand the issue. Interpretive studies will be needed to relate the use of methodologies and how they are used to their ‘success’ in specific contexts. If we do not know how systems are successfully developed, we have no basis to improve the development process.

## Are methodologies obsolete?

Not only has the nature of information systems changed dramatically within the last decade, but so too have organizations, industries and the role of information systems – and the changes continue. Methodologies for the twenty-first century have been envisioned as addressing not only new technological forms, but also as including rich semantics and support for identifying and exploiting information technology for strategic advantage (Lyytinen, 1989). Some believe methodologies have little or no place in developing today's systems (Keyes, 1992).

Lyytinen (1989) described first-generation methodologies as addressing code quality (e.g. structured programming) and second-generation methodologies as focusing on the analysis and design of well-structured application domains (e.g. structured methodologies, ISAC). Unfortunately it is still unclear how (or how much) first- and second-generation methodologies were used or how well they have worked. Therefore, we cannot know what third-generation methodologies should be or if they are needed at all.

On the one hand, evidence is mounting that the design process is not understood, nor is it rational (Turner, 1987; Curtis et al., 1988). The validity of applying methodologies to structure the design process must therefore be questioned. Some question the validity of teaching methodologies in IS programs (Angell and Straub, 1993). On the other hand, Lyytinen (1988) concluded that systems analysts view the design process as ‘rationalistic’ and want it to be ordered and controlled.

Without a sound empirical base, it cannot be concluded that existing methodologies are appropriate or inappropriate for today's systems or tomorrow's. Since the effectiveness of existing methodologies or how they are used has not been evaluated, it is unclear whether existing methodologies are or are not appropriate for today's systems or for 'post-modern' organizations (Baskerville et al., 1992). The evaluation of existing development practices and methodology usage is clearly necessary to identify any strengths and shortcomings of existing practices, before prescriptions for the future can be made.

## Summary

The dearth of research on methodologies used to develop real systems in real contexts is obvious from the preceding discussion. Methodology knowledge is based on conceptual writings and studies of small systems in unrealistic contexts, augmented by single informer surveys that often compare unspecified methodologies (e.g. the use of prototyping and the SDLC). Although this is a start, research should now focus on the use of methodologies to develop realistic systems in realistic contexts.

It is not yet known if or when there are critical differences among methodologies under real conditions. It is not understood how methodologies are selected or adapted or how they should be selected – or if they should be selected at all. We do not know how methodologies are used or how effective they are. The questions raised in Table 1 must be answered before the software development process or product can be improved.

Although it would be prohibitively expensive in terms of time and money to compare every methodology on every type of system as it is developed in an organization, it is clear that the past research paradigm has been inadequate. Existing software development practices and needs must be evaluated more thoroughly, although this will require a significant resource commitment by both researchers and development organizations.

If the software development process or resulting product is to be improved, not only must the research paradigm be improved, but published research must clearly define what is being studied. Much existing ‘methodology’ research fails to advance knowledge because the object of investigation has not been clearly defined.

Future research may provide a basis for the methodologies of the next century or may show that methodologies – as we know them today – are not beneficial. The basis for the improvement of the systems development process and product will be provided only through the study of real methodologies used in real contexts.

## References

Alavi, M. (1984) An assessment of the prototyping approach to information systems development. Communications of the ACM, 27 (6), 556–63.

Angell, I.O. and Straub, B.H. (1993) Though this be madness, yet there is method in't. Journal of Strategic Information Systems, 2 (1), 5–14.

Avison, D.E. and Fitzgerald, G. (1988) Information systems development: current themes and future directions. Information and Software Technology, 30 (8), 458–66.

Avison, D.E. and Wood-Harper, A.T. (1991) Information systems development research: an exploration of ideas in practice. The Computer Journal, 34 (2), 98–112.

Banker, R.D., Datar, S.M. and Kemerer, C.F. (1991) A model to evaluate variables impacting the productivity of software maintenance projects. Management Science, 37 (1), 1–18.

Bantleman, J.P. and Jones, A.H. (1984) Systems analysis methodologies: a research project, in Beyond Productivity: Information Systems Development for Organizational Effectiveness, Bemelmans, T.M.A. (ed.) (North-Holland, Amsterdam) pp. 213–54.

Baskerville, R., Travis, J. and Truex, D. (1992) Systems without method: the impact of new technologies on information systems development projects, in The Impact of Computer Supported Technologies on Information Systems Development, Kendall, K.E., Lyytinen, K. and DeGross, J.I. (eds) (North-Holland, Amsterdam) pp. 241–69.

Beck, L.L. and Perkins, T.E. (1983) A survey of software engineering practice: tools, methods and results. IEEE Transactions on Software Engineering, SE-9 (5), 541–61.

Boehm, B.W., Gray, T. and Seewaldt, T. (1984) Prototyping versus specifying: a multiproject experiment. IEEE Transactions in Software Engineering, SE-10 (3), 290–302.

Boland, R.J., Jr (1978) The process and product of system design. Management Science, 24 (9), 887–98.

Bubenko, J.A., Jr (1986) Information systems methodologies – a research view, in Information Systems Design Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, Amsterdam), pp. 89–302.

Burch, J.G. (1992) Systems Analysis, Design, and Implementation (Boyd and Fraser, Boston).

Burns, R.N. and Dennis, A.R. (1985) Selecting the appropriate application development methodology. Data Base, 16 (4), 19–23.

Cameron, J.R., Campbell, A. and Ward, P.T. (1991) Comparing software development methods: example. Information and Software Technology, 23 (6), 386–402.

Checkland, P. and Scholes, J. (1990) Soft Systems Methodology in Action (John Wiley & Sons, Chichester).

Colter, M.A. (1984) A comparative examination of systems analysis techniques. MIS Quarterly, 8 (1), 51–66.

Connors, D.T. (1992) Software development methodology and traditional and modern information systems. Software Engineering Notes, 17 (2), 43–9.

Curtis, B., Krasner, H. and Iscoe, N. (1988) A field study of the software design process for large systems. Communications of the ACM, 31 (11), 1268–87.

Davis, G.B. (1982) Strategies for information requirements determination. IBM Systems Journal, 21 (1), 4–30.

Dekleva, S.M. (1992) The influence of the information systems development approach on maintenance. MIS Quarterly, 16 (3), 355–72.

DeMarco, T. (1978) Structured Analysis and System Specification (Yourdon, New York).

Edwards, H.M., Thompson, J.B. and Smith, P. (1989a) Results of survey of use of SSADM in commercial and government sectors in United Kingdom. Information and Software Technology, 31 (1), 21–8.

Edwards, H.M., Thompson, J.B. and Smith, P. (1989b) Experiences in use of SSADM: series of case studies. Part 1: first time users. Information and Software Technology, 31 (8), 411–19.

Edwards, H.M., Thompson, J.B. and Smith, P. (1989c) Experiences in use of SSADM: series of case studies. Part 2: experienced users. Information and Software Technology, 31 (8), 420–8.

El Louadi, M., Pollalis, Y.A. and Teng. J.T.C. (1991) Selecting a systems development methodology: a contingency framework. Information Resources Management Journal, 4 (1), 11–19.

Episkopou, D.M. and Wood-Harper, A.T. (1986) Towards a framework to choose appropriate IS approaches. The Computer Journal, 29 (3), 222–8.

Fazlollahi, B. and Tanniru, M.R. (1991) Selecting a requirement determination methodology – a contingency approach revisited. Information & Management, 21, 291–303.

Finkelstein, C. (1989) An Introduction to Information Engineering (Addison-Wesley, New York).

Fitzgerald, G., Stokes, N. and Wood, J.R.G. (1985) Feature analysis of contemporary information systems methodologies. The Computer Journal, 28 (3), 223–30.

Floyd, C. (1986) A comparative evaluation of system development methods, in Information Systems Design Methodologies: Improving the Practice, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, Amsterdam) pp. 19–54.

Flynn, D.J. and Fragoso-Diaz, O. (1993) Conceptual Euromodelling: how do SSADM and MERISE compare? European Journal of Information Systems, 2 (3), 169–83.

Hackathorn, R.D. and Karimi, J. (1988) A framework for comparing information engineering methodologies. MIS Quarterly, 12 (2), 203–21.

Hirschheim, R.A. (1985) Office Automation: A Social and Organizational Approach (John Wiley, New York).

Humphrey, W.S. (1989) Managing the Software Process (Addison-Wesley, Reading, MA).

IEEE (1987) Software Engineering Standards (Wiley Inter-science, New York).

Jackson, M.A. (1983) System Development (Prentice-Hall, Englewood Cliffs, NJ).

Jayartna, N. (1988) Guide to methodology understanding in systems practice. International Journal on Information Management, 8 (1), 43–53.

Karam, G.M. and Casselman, R.S. (1993) A cataloging framework for software development methods. Computer, 26 (2), 34–45.

Keyes, J. (1992) How software is developed undergoing basic changes. Software Magazine, 12 (1), 38–40, 43–7, 55–6.

Klein, H.K. and Hirschheim, R. (1991) Rationality concepts in information system development methodologies. Accounting, Management & Information Technology, 1 (2), 157–87.

Kumar, K. and Welke, R.J. (1992) Methodology engineering: a proposal for situation-specific methodology construction, in Challenges and Strategies for Research in Systems Development, Cotterman, W.W. and Senn, J.A. (eds) (John Wiley, New York) pp. 257–69.

Lantz, K.E. (1985) The Prototyping Methodology (Prentice-Hall, Englewood Cliffs, NJ).

Loy, P. (1993) The method won't save you (but it can help). Software Engineering Notes, 18 (1), 30–4.

Lyytinen, K. (1987a) A taxonomic perspective of information systems development: theoretical constructs and recommendations, in Critical Issues in Information Systems Research, Boland, R.J. and Hirschheim, R.A. (eds) (John Wiley, New York) pp. 3–41.

Lyytinen, K. (1987b) Different perspectives on information systems: problems and solutions. ACM Computing Surveys, 19 (1), 5–46.

Lyytinen, K. (1988) Expectation failure concept and systems analysts' view of information system failures: results of an exploratory study. Information & Management, 14 (1), 45–56.

Lyytinen, K. (1989) New challenges of systems development: a vision of the 90's. Data Base, 20 (1), 1–12.

McLaughlin, R. (1993) Does CASE make the customer happier? Software Engineering Notes, 18 (2), 18.

Mahmood, M. (1987) System development methods: a comparative investigation. MIS Quarterly, 11 (3), 293–311.

Malouin, J.L. and Landry, M. (1983) The mirage of universal methods in systems. Journal of Applied Systems Analysis, 10, 47–62.

Menard, J.B. (1980) Exxon's experience with the Michael Jackson design method. Data Base, 11 (1), 88–92.

Mendes, K.S. (1980) Structured systems analysis: a technique to define business requirements. Sloan Management Review, 21 (4), 51–63.

Meredith, D.C. (1986) Don't gamble when choosing a system development methodology. Data Management, 24 (7), 36–9.

Middleton, P. (1994) Euromethod: the lessons learned from SSADM, in Proceedings of the Second European Conference on Information Systems, Bach, W.R.J. (ed.) (Nijenrode University Press, Breakeleu) pp. 359–66.

Necco, C.R. Gordon, C.L. and Tsai, N.W. (1987) Systems analysis and design: current practices, MIS Quarterly, 11 (4), 461–76.

Nielsen, P.A. (1989) Reflections on development methods for information systems: a set of distinctions between methods. Office: Technology and People, 5 (2), 81–104.

Olle, T.W. (1982) Comparative review of information systems design methodologies, in Informations Systems Design Methodologies: A Comparative Review, Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (eds) (North-Holland, Amsterdam) pp. 1–14.

Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (1982) Information Systems Design Methodologies: A Comparative Review (North-Holland, Amsterdam).

Olle, T.W., Sol, H.G. and Tully, C.J. (1983) Information Systems Design Methodologies: A Feature Analysis (North-Holland, Amsterdam).

Olle, T.W., Sol, H.G. and Verrijn-Stuart, A.A. (1986) Information Systems Design Methodologies: Improving the Practice (North-Holland, Amsterdam).

Olle, T.W., Hagelstein, J., Macdonald, I.G., Rolland, C., Sol, H.S., Van Assche, F.J.M. and Verrijn-Stuart, A.A. (1988) Information Systems Methodologies (Addison-Wesley, Wokingham, UK).

Palvia, P. and Nosek, J.T. (1990) An empirical evaluation of system development methodologies. Information Resources Management Journal, 3 (3), 23–32.

Plyler, R.W. and Kim, Y.G. (1993) Methodology myths: four tenets for systems developers. Information Systems Management, 10 (2), 39–44.

Ross, D.T. (1985) Applications and extensions of SADT. IEEE Computer, 18 (4), 24–34.

Russo, N.L. and Klomparens, R. (1993) Formal Applications Development Methodologies in the '90's. Working paper, Northern Illinois University, DeKalb, IL.

Sauer, C. and Lau, C. (1994) The adoption of information systems methodologies – an analytical framework and a case study, in Proceedings of the Fifth Australasian Conference on Information Systems.

Schach, S.R. (1993) Software Engineering, 2nd edition (Irwin, Homewood, IL).

Sharple, R.C. and Cohen, S.S. (1993) The object-oriented brewery. Software Engineering Notes, 18 (2), 60–73.

Smolander, K., Tahvanainen, V. and Lyytinen, K. (1987) How to combine tools and methods in practice – a field

study, in Information Systems Engineering, Steinholtz, B., Solvberg, A. and Bergman, L. (eds) (Springer-Verlag, Berlin) pp. 195–285.

Song, X. and Osterweil, L.J. (1992) Toward objective, systematic design-method comparisons. IEEE Software, 9 (5), 43–53.

Teichroew, D. and Hershey, E.A., III (1977) PSL/PSA: a computer-aided technique for structured documentation and analysis of information processing systems. IEEE Transactions on Software Engineering, SE-3 (1), 42–8.

Thayer, R.H., Pyster, A.B. and Wood, R.C. (1981) Major issues in software engineering project management. IEEE Transactions in Software Project Management, SE-7, 333–42.

Turner, J.A. (1987) Understanding the elements of system design, in Critical Issues in Information Systems Research, Boland, R.J., Jr and Hirschheim, R.A. (eds) (John Wiley and Sons, Chichester) pp. 97–111.

Van De Velde, R. (1992) CASE adoption at Imperial Oil. Journal of Systems Management, 43, 24–38.

Westrup, C. (1993) Information systems methodologies in use. Journal of Information Technology, 8, 267–75.

Whitten, J.L., Bentley, L.D. and Barlow, V.M. (1989) Systems Analysis and Design Methods, 2nd edition (Irwin, Homewood, IL).

Wood, B., Pethia, R., Gold, L. and Firth, R. (1988) A Guide to the Assessment of Software Development Methodologies (Software Engineering Institute, Pittsburgh).

Wood-Harper, A.T. and Fitzgerald, G. (1982) A taxonomy of current approaches to systems analysis. The Computer Journal, 25 (1), 12–16.

Yourdon, E. (1986) Whatever happened to structured analysis? Datamation, 32 (11), 133–8.

Zagorksy, C. (1990) Case study: managing the change to CASE. Journal of Information System Management, 7 (3), 24–32.

## Biographical notes

Nancy L. Russo is an assistant professor of information systems at Northern Illinois University, where she teaches in the areas of systems analysis and design and database management. She received her PhD in MIS from Georgia State University in 1993. Her research focuses on systems development methods, productivity and quality issues in information systems development and the diffusion of information technology.

Judy L. Wynekoop is an assistant professor of information systems at the University of Texas, San Antonio, where she teaches in the areas of systems analysis and design, software engineering and management information systems. She received her PhD in information systems from Georgia State University in 1991. Her research focuses on the use and impact of information technology in medicine, the diffusion, implementation and impact of software development technologies and the software development process.

Address for correspondence: Judy L. Wynekoop, Division of Accounting and Information Systems, The University of Texas at San Antonio, San Antonio, TX 78249-0632, USA.
