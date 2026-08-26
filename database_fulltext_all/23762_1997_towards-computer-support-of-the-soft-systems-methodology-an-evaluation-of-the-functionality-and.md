---
otero_id: 23762
otero_key: "BV5MPDGJ"
title: "Towards computer support of the soft systems methodology: an evaluation of the functionality and usability of an SSM toolkit"
authors: "J Zhang; R Smith; R B Watson"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000262"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards computer support of the soft systems methodology: an evaluation of the functionality and usability of an SSM toolkit

J Zhang, R Smith and RB Watson

School of Computer Science and Software Engineering, Swinburne University of Technology, Hawthorn, Victoria 3122, Australia

In recent years a number of research projects have investigated computer support of the soft systems methodology (SSM). These typically involve the production of prototype computer-based tools supporting some aspects of SSM, although evaluation of these has been unsystematic and anecdotal. There has also been some debate in the literature about whether SSM is amenable to computer support. This paper reports a more systematic investigation of the potential for computer support of SSM and evaluation of the functionality and usability of an SSM support toolkit (SoftCase) developed by one of the authors. Following a brief review of previous research in this area, and the functionality of the SoftCase toolkit, the design of the evaluation and its outcome are described in detail. The paper concludes with a discussion of computer technology to support SSM and some possible directions for evaluating the impact of computer support on the SSM process.

## Introduction

The Lancaster Soft Systems Methodology (SSM) (Checkland, 1981; Checkland & Scholes, 1990) and other forms of ‘soft’ systems thinking have arguably now been accepted by the information systems community as having an important role to play in information systems development (Avison & Fitzgerald, 1988; Stowell, 1993; Winter et al, 1995). Even in the object-oriented systems community, usually thought of as wedded to ‘hard’ systems thinking, it is increasingly being recognised that “we need a step in the development process that occurs before analysis can start, the step that establishes the core purpose, structure, and requirements of the system to be built” (Chonoles et al, 1995). This step can be provided by SSM. The important insight contributed by soft systems thinking in general, and SSM in particular, is that whilst a single set of system goals, agreeable to all stakeholders, may not exist, systems ideas can bring about improvements in the understanding and structure of the organization in which an information system resides.

Conventional (hard) systems methodologies are now supported by a plethora of computer-based support tools. These tools can:

facilitate the drawing process associated with many of the specified techniques;

I validate drawings by enforcing consistency;

link different parts of a methodology so that associated study artifacts can be (partially) created automatically;

speed up development by allowing multiple copies of study documents to be taken for exploration of various options and, in the case of software development, by generating skeleton source code and default screen forms; and

I support project management and ensure that certain documentation standards are met.

In a cogent argument in support of the need for appropriate computer support of SSM, Avison et al (1992) have argued that tools are beginning to simplify methodologies, making the various activities more consistent, speeding up manual processes, making some steps redundant and removing from the analyst the drudgery of making large numbers of manual iterations and crosschecks. Indeed there is emerging evidence that users now consider the availability of support tools as a decision driver in the adoption of a methodology (Yourdon, 1992). Given that SSM has a great deal to offer the information systems developer (who will most probably be attuned to such computer support), the lack of tools supporting SSM can only reduce both its impact and its rate of adoption. One case study in which SSM was used (Ormerod, 1993) concluded that widely available computer support could be the key to wider use of soft methodologies.

The above argument, however, begs the question of whether it is both feasible and desirable to provide computer support to the SSM practitioner. It has been argued (Stowell et al, 1991) that the nature of SSM and computer-based automation are diametrically opposed. It is argued that the consequences of an attempt to automate might be:

the enforcemnt of excessive formality and structure, as required if SSM is to be translated into a ‘computer program’, with the consequence that it will be used as “a template for analysis and action as opposed to a framework for exploration and learning” (Stowell et al, 1991); and/or

the danger of over-complexity, with the possibility of creating rich and complex soft systems models being irresistible to the SSM analyst, with the consequence that the power of soft systems will be lost in a mass of detail.

A further contribution to this debate is the critique by Kreher (1993) and reply by Avison et al (1993). Kreher argues that whilst the proposed benefits of a toolkit supporting, for example, the creation of SSM rich pictures, might appear inviting, there could be some dangerous trade-offs related to their achievement. In particular, a tidy, clear-cut rich picture, as might be created using a support tool, might have the psychological effect of leading users to believe that the problem situation is not quite as messy as originally perceived. Further, the use of ‘default’ rich picture screens might constrain creativity. The use of a tool which imposes such ‘standards’ might be intimidating to the user, and more generally the users might lack ownership of what may appear to be sterile, anonymous images scanned into the diagram. It is also suggested that while decomposing ‘rich pictures’ using the ability to put higher resolution levels behind the top level images on a computer screen, may appear superficially useful, it could divert attention from the whole.

In response, Avison et al (1993) have argued that the toolkit they propose is not attempting to do SSM – merely to support the process. They point out that the only true representation of reality is reality itself, and so in analysing any problem situation we are abstracting to gain an understanding of it. The toolkit, they argue, should be viewed as a delivery medium for the abstraction that occurs as the analyst attempts to understand the situation.

It should be noted that the above debate has surfaced widely elsewhere. For example, Mumford (1994) has pointed out that she has been repeatedly approached by people wanting to turn her ETHICS approach into software. This she has resisted for fear that one would lose the pleasures and results that come from face-toface discussion and eventual agreement on strategies and solutions.

In justification of the present research, it could be argued that the concerns of Stowell et al (1991) and Kreher (1993) take very literally the notion of automation, and that a more appropriate alternative view would be that we seek to investigate the notion of computer-based support of selected aspects of SSM and associated data management only. There is no intent that a tool should or could perform the central functions of an SSM study, such as postulating a root definition or generating options for change based on model/real world comparison. Neither will every SSM analyst be comfortable with a computerised support tool. Some may claim, for example, that it inhibits their creativity. On the other hand, some analysts may be encouraged to explore a larger set of root definitions and conceptual models given the power for rapid change of model documentation which the tool places at their fingertips.

A second, more pragmatic rationale for the present research would be to take the position of Avison and Golder (1991b), that the conjectures above as to the consequences of an attempt to automate SSM would be best reviewed when exploratory development has made a selection of potential tools available.

In the present paper we first examine the process of using SSM with a view to identifying aspects potentially suitable for computer support. The formal model of “a system to use SSM” (Checkland & Scholes, 1990) is used for this purpose. We next review work to date on computer support for SSM, comprising both that reported in the literature and some unpublished Australian work. A brief overview of an SSM support tool, termed SoftCase, developed by one of the authors of this paper, is then presented. The main contribution of the paper, a laboratory-based evaluation of the SoftCase tool, is then addressed. This includes a brief consideration of the types of criteria against which a support tool should be evaluated, followed by a description of the design of the evaluation and results obtained. Finally, some directions for investigating the impact of computer support on the wider SSM process and resultant learning are canvassed.

## Aspects of SSM suitable for support

It may be assumed that before the requirements for computer support of SSM can be specified, detailed consideration must be given to the process of using SSM. This assumption follows from the so-called ‘law of conceptualisation’ (Checkland, 1981, p 237), which states that “conceptualisation of a system which serves another must be preceded by conceptualisation of the system served”. Computer support is provided by a ‘serving system’ which serves a particular human activity system, the ‘served system’ (cf. Winter et al, 1995). The served system may be identified with the ‘system to use SSM’ described by Checkland and Scholes (1990). It should be noted that the ‘system to use SSM’ embraces the modelbuilding of the original seven-stage representation of SSM (Checkland, 1981), and the Analysis 1, 2 and 3 activities of the stream of cultural analysis of Checkland and Scholes (1990). A relatively straightforward grouping of the 16 activities of the ‘system to use SSM’, according to Checkland’s notion that ‘a system to do X’ involves planning to do X, doing X, and monitoring and controlling the doing of X, has been proposed by Zhang (1993). Therein, X was identified as ‘applying SSM to a real-world problem situation, and capturing the methodological learning from this use’. Such a reconsideration of the ‘system to use SSM’ produces five groupings of the 16 activities proposed by Checkland and Scholes (1990) (with the activity numbers used by Checkland and Scholes identified in brackets), as follows:

(1) planning an SSM study (Activity 1);

(2) applying SSM to a real-world problem situation (Activities 2–9);

(3) monitoring and controlling the application of SSM to a real-world problem situation (Activities 10–12);

(4) capturing methodological learning from the use of SSM (Activities 13–16);

(5) monitoring and controlling the refinement of SSM based on learning from its use. (Not explicitly included by Checkland and Scholes, but a direct consequence of applying the notion of a ‘system to do X’).

Each of the above areas could be conceived of as a candidate for computer support. In the present research we consider only the group (2) in detail, but each of the others might be fruitful candidates for future work. An examination of the techniques underpinning each of activities 2 to 9 in the ‘system to use SSM’, and an inventory of the information categories used and/or generated by these activities (Zhang, 1993), suggests the following candidate suite of tools:

(1) Rich Picture Builder (supporting Activities 2– 4);

(2) Relevant System Namer (supporting Activity 5);

(3) Root Definition Builder (supporting Activity 5);

(4) Conceptual Model Builder (supporting Activity 6);

(5) Formal Questioning Work Sheet Builder (supporting Activity 7);

(6) Maltese Cross Builder (supporting Activity 7).

## Previous work on computer support of SSM

As commented by Stowell et al (1993), SSM has not avoided the inclination of researchers to try to produce computer-aided versions of the methods and techniques used in the various methodologies. Three substantial attempts to provide computer support of SSM studies or the teaching of SSM have been reported in the literature, all originating in the UK. Three further unpublished attempts originating in Australia have come to the attention of the authors. We review these briefly in turn.

## A. A tool to support the capture of rich pictures (Avison et al, 1991a, b; 1992)

In a series of three papers, Avison et al (1992) have argued not only that there is a need for tool support for SSM, but also that there are a number of developments which would suggest that this is now plausible. In particular, they suggest the drawing of rich pictures is one such area, and they describe a prototype rich picture drawing tool (‘Get Rich Quick’) constructed at Aston University (UK). The tool described has strong similarity to that described later as a ‘Rich Picture Builder’ in this paper, developed independently at Swinburne. In particular, the tool described by Avison et al (1992) supports retrieval of narratives, graphs, photographs or video pictures, held in the background, by mouse clicking on icons in the rich picture which appears on the screen.

## B. Using expert system technology to teach SSM

(Stowell et al, 1991, 1993; West et al, 1994;

Stansfield, 1995)

SSM is usually taught through a combination of lecture sessions and tutorials. Students sometimes also gain some experience of practice through the use of case studies. One of the difficulties, however, is that if students are to fully understand the rich significance of the methodology, as opposed to using the approach in a limited and functionalist way, personal contact with an experienced practitioner to act as a guide is deemed advisable. Stowell et al (1991) have investigated the application of computer-based expert system technology to provide such practice and guidance without the need for a ‘teacher’ to be present, in a way which enables students to work at their own pace and to gain experience in the different practical stages of the methodology using examples of varying complexity.

The system designed (‘SSM-Aid’) takes the user through each of the seven stages of SSM. At each stage information is given at three levels: (i) an overview of the stage; (ii) specific guidelines about how to carry out the stage; and (iii) a tutorial exercise where the users can try the task set relating to the stage, and compare their answers with those of an expert.

Of a number of outcomes reported (Stowell et al, 1991), one of the most interesting concerned the resilience of the system as an aid for teaching SSM. Whilst there remained problems to be addressed before the package could be developed to a commercial standard, it was believed that the potential benefits could make the investment worthwhile.

More recently, an enhanced package for teaching SSM, which incorporates many additional features which exploit the characteristics of multimedia (enhanced interfaces; intensive use of oral advice and taped ‘conversations’) has been described (Stowell et al, 1993).

## C. Soft Systems Analysis and Modeling Tool (SSAMT) (Davenport & Ayers-Hunt, 1995)

A UK-developed tool named SSAMT to support SSM practitioners has recently been reported. SSAMT is very similar to the SoftCase tool reported later in this paper, which is perhaps not surprising given the current ease of developing PC Windows applications and the explosion in CASE tool support for all kinds of systems development methodologies. SSAMT provides most support to the ’below the line’ activities of SSM, although it does provide a means of summarising problem situations in textual form (no graphical rich picture builder is provided) and of comparing conceptual models with the problem situation. It has some features not included in SoftCase, such as ‘Help’ screens at each stage of the process and a greater reporting capability, although its authors emphasise that it is still only a prototype at the demonstrator stage of development.

D. SSM ‘Trainer Wheels’ (Coombe & Dolling, 1992) In 1992–93 some interesting work in computer support of SSM was carried out at the Department of Computer Science, University College, University of New South Wales, Canberra, Australia. Coombe and Dolling (1992) developed a product which they called SSM ‘Trainer Wheels’. This is conceptualised, much as trainer wheels are viewed by the novice bicycle rider, as a computer support tool for the novice SSM practitioner embarking upon his/her initial SSM project. As the novice gains confidence, the support tool will be discarded.

Implemented using Excel 4 running under Microsoft Windows, the product prompts the user through the processes of textual entry of rich picture notes; entry of the CATWOE elements (renamed PATOLC for Proprietor, Action Taker, Transformation, Object Affected, Limitations and Context); root definition creation; explicit recording of assumptions associated with each relevant system; suggestion of some possible activities appropriate to the conceptual model using some simple heuristics; and provision of forms for the recording of decisions relevant to change decisions taken and information needs investigations.

Outcomes of the study, in terms of user reaction to the product or future plans, are not available at the time of writing.

E. A conceptual model drawing tool (Sutherland,1992) Consultants Harris and Sutherland, as reported by Watson and Smith (1988), have developed a conceptual model production tool which stores details about activities and information flows between activities, hierarchical level structures, and data relevant to the positioning of elements of conceptual models on the printed page. The product includes also some simple placement heuristics, to optimise the positioning of activities in a way which minimises the crossing of arrows in diagrams at the time of printing. The product was developed in 1987, using the Dataflex DOS and character-based database management system, and has been used in the course of a number of consultancies in the area of information systems planning. An associated product, written in C, supports export of the conceptual models so developed to HP GL Plotters and Postscript printers. The major disadvantages/limitations reported by Sutherland (1992) include:

(1) The product produces only straight line arrows between activities drawn within square boxes, at odds with the Lancaster University convention; and

(2) There is no capability to export conceptual models so created to high-end graphic packages for later specialised annotation.

Amongst capabilities deemed important by Sutherland in any further development would be:

(1) An ability to move freely between hierarchical levels in a conceptual model, developing lower levels before top levels models for example; and

(2) An ability to clone models so that the analyst can easily explore alternative ideas in the course of a study.

The product has been little used since 1989, as the demands for consultancy have shifted to areas using different methodological approaches.

## F. A conceptual model drawing tool (Ledington & Ledington, 1996)

Recently Ledington and Ledington (1996) have reported research into the use of a modelling approach, supporting the development of SSM conceptual models, termed ‘Decision-Variable Partitioning’. They mentioned briefly the possibility of automating the process of drawing the structures of models using the prioritised transformations and constraints generated in such an approach. Further detail of such support is not available at the time of writing.

## The SoftCase toolkit

The SoftCase toolkit, comprising the first four support tools listed above, has been implemented using the Asymmetrix ‘Toolbook’ product (Joseph, 1990). The remaining two tools are, in a sense, not central to SSM model building, but are possible means of making real world/model comparisons. As such, they have not been fully implemented in the first instance, but for the purpose of the evaluation described below, they have been simulated using a combination of computer and paperbased means. Following the ‘Toolbook’ style, the Soft-Case opening screen represents each separate SSM project as if it were a single volume of a named book on a bookshelf. After the opening of a new or existing SSM project, the user selects from a menu the tool desired. The details of these tools are given by Zhang (1993) and are summarised below.

## Rich Picture Builder

This supports the creation by the user of cartoon style representations of the problem situation. This can be done by means of drawing tools selected from a palette, pre-stored icons selected from a symbol library (e.g. ‘people’ figures, business icons, ‘think’ bubbles, crossed swords), or explanatory text visible in the foreground. A rich picture may be zoomed and scrolled, and textual notes (which may be hidden in the background) may be associated with an icon. Finally, a rich picture may be associated with one or more of the subsequent relevant systems.

## Relevant System Namer

This allows the user to name a set of relevant systems associated with a rich picture. The tool allows the user to enter comments as to whether the system is expected to match the real world, and whether this would be desirable. It also allows the entry of textual notes and associations between relevant system, parent rich pictures and subsequent root definitions.

## Root Definition Builder

This allows the user to store a root definition for each relevant system in either free textual form, or by embedding the CATWOE elements in a form such as recommended by Checkland (1981). CATWOE elements can also be displayed separately, and associated notes stored, browsed and retrieved. Finally, the tool allows the user to enter associations between the root definition, parent relevant system and subsequent expansion as a conceptual model.

## Conceptual Model Builder

This allows the user to enter labelled activity ellipses and to connect them by arrows representing logical contingency. An activity ellipse can be expanded to a higher level of detail by pointing and clicking with the mouse and entering a new root definition. If models are developed at more than one level, the user can request balancing of the arrows to check that they are consistent between levels. A conceptual model may be zoomed and scrolled, and textual notes associated with the development of the model stored. Finally, the tool allows the user to enter associations between the conceptual model, parent root definition and the subsequent comparison phase (e.g. a work sheet).

## Formal Questioning Work Sheet Builder

In its full implementation, this tool will automatically generate a work sheet with the activities and links in the associated conceptual model entered. The user can then enter textual notes concerning whether the activities/links exist in the real world, the way they are achieved, measures of performance, information needed/generated by the activities and other comments.

## Maltese Cross Builder

In its full implementation, this tool will automatically generate a Maltese Cross (Wilson, 1990) with the top half completed as in the associated work sheet. The user can then enter Information Processing Procedures and their mapping to information categories in the bottom half of the Maltese Cross.

## Product-wide Functions

The SoftCase toolkit supports the output of textual and graphic material to a selection of printers/plotters, and allows cut and paste to a selection of word processor and graphics packages. It also supports the copying of fragments of conceptual models, for pasting subsequently into other models under development.

## The need for evaluation of prototype SSM support tools

We would argue that previous research into the provision of SSM support tools has been largely descriptive, concentrating on the functionality of the tools and, to a greater or lesser extent, the technology by which they were constructed. Ironically, considering that they purportedly support a methodology in which evaluation (monitoring and control) of human activity systems plays such an important part, little attention has been given to the disciplined evaluation of these tools. As reported by Checkland et al (1990), evaluation of any entity involves defining criteria for efficacy (does it work?), efficiency (are the time and effort used worth the result?) and effectiveness (does it do the right thing?). These authors also provide an SSM conceptual model of ‘a system to evaluate X’, where X is any purposeful activity, and compare each activity in the model with its real world manifestations in a particular study context. In the context of the present work, X might be ‘use an SSM support tool’, and some criteria for efficacy, efficiency and effectiveness might be:

Efficacy: is it easy to use? does it expedite the process of using SSM? does it improve the quality of the results of an SSM study?

Efficiency: is the support provided worth the cost of developing and learning to use the tool?

Effectiveness: is an SSM study something which should be supported?

As is the case for many human activity systems, evaluating the effectiveness of this activity is rather more difficult than evaluating its efficacy and efficiency. Furthermore, the effectiveness of an activity such as this, whose purpose is unequivocally to support another activity, may be hard to distinguish from the effectiveness of the supported activity. As discussed by Checkland and Scholes (1990), the efficacy of SSM itself is related to its success in facilitating learning as a means to improving problem situations. The effectiveness of SSM itself is related to whether a continuous cycle of learning is the best means of bringing about these improvements. In the spectrum of problem situations, SSM has been found to be most effective in pluralistic, systemic contexts (Jackson & Keys, 1984). Presumably an SSM support tool, if efficacious, would also be most effective in these contexts, although one may speculate that it might be more effective in problem situations which, while pluralistic and systemic, are inclined to the harder end of the spectrum. Also, as already mentioned, the present day importance of computer-based tools in information systems development methodologies may mean that the use of such a tool may influence the clients of an SSM information systems study to be more favourably disposed to its conclusions.

Evaluating the efficiency of the activity of using an SSM support tool is also difficult, as it requires a comparison of the costs of developing or acquiring, and learning to use, a tool with the incremental improvement in carrying out an SSM study brought about by its use. There are undoubtedly costs involved in developing a tool, although if a tool such as SoftCase had been developed and marketed commercially (as opposed to an academic research effort) these costs could be amortised over many users and the cost to a customer purchasing the tool would probably be comparable to that of the many other specialised CASE tools on the market. The time required to learn to use a tool effectively could be an important cost factor in its use. This question was partially addressed in the present evaluation, although further work and quantitative measurements would be needed to explore it thoroughly. However, considering the potential benefits of SSM studies, and the high costs of employing SSM consultants, it could be argued that if a tool is efficacious, i.e. has any benefits at all, then its benefits outweigh its costs.

We are then left with the question: is a tool such as SoftCase efficacious? Although at first sight this might seem to be a relatively easy question to answer, it is complicated by the fact that an SSM study may be considered to involve two levels of information processing: a superficial level at which the conventional SSM study artifacts such as rich pictures and root definitions are produced; and a deeper level at which learning occurs on the part of the analysts. The production of study artifacts should reflect the learning process, but the latter is poorly understood and its exact relationship to the study artifacts is by no means clear. This dichotomy, as it relates to rich picture diagramming, has been pointed out by Lewis (1992). It is analogous to the distinction between information as structured data and information as the means by which human beings make sense of their world (Boland, 1987).

Furthermore, it has been pointed out by Checkland and Scholes (1990) that the superficial level, involving study artifacts, is not even necessary in an SSM study: experienced analysts using the so-called mode 2 of SSM can largely dispense with them and carry out a study in their heads. Thus the ‘system to use SSM’ only applies to the mode 1 use of SSM and computerised support involving tools such as SoftCase is only possible for this mode.

The evaluation described in the remainder of this paper is primarily concerned with computerised support of SSM study artifact production using the conventional criteria of information systems assessment, i.e. accuracy, timeliness, completeness and appropriateness of format (Senn, 1985). Whilst the effect of computerised support on the learning process itself is clearly important it lies outside the scope of the present investigation. As a pointer to further possible work addressing this question, we do however include some suggestions for evaluating the impact of computer support on the learning process associated with an SSM study, in the penultimate section of this paper.

## Design of the evaluation

## Overview

In view of the contention by Avison and Golder (1991b) that conjectures as to the consequences of an attempt to automate SSM would be best reviewed when exploratory development has made a selection of potential tools available, we contend that it is important that the means adopted by such tool developers to evaluate their products must be explicitly reported. Unless such a procedure is adopted, comparison of products will be at best anecdotal. In accord with this position, we therefore describe the procedures we have adopted, and the outcomes, in some detail.

The evaluative process has been structured in two phases. Phase 1 sought to investigate aspects of usability, structured around the design of icons and means provided for users to navigate through the program. Phase 2 on the other hand, sought to probe deeper issues of functionality. Specifically, phases were structured as follows:

## Phase 1

Attribution of Meaning to Icons – Application of a questionnaire to determine the meanings attributed by users to those icons used in the prototype.

Icon Discriminability – Application of a questionnaire to determine, for given actions, those icons which users believe most appropriate to required actions; and

Navigation through the Program – Recording and subsequent analysis of the performance of users undertaking a set of SSM data entry tasks, with the objective of determining the ease of navigation through the sequence of data entry tasks encountered in a typical study.

## Phase 2

Focus Group Meeting – A subsequent, loosely structured meeting of those who have participated in the analysis process, to probe reactions to the functionality and usability of the product, and their insights into the potential of the tool to alter their use of SSM techniques and processes.

The overall structure of the evaluation drew upon Booth (1989), with reference to issues in the evaluation of icons, drawing upon the work of Hakiel and Easterby (1986).

## Attribution of meaning to icons

SoftCase has been developed as a windows application which draws heavily on iconic representations to control system operation. In an initial evaluation, users were presented with a short narrative explaining the nature of the SoftCase product. Subsequently, users were presented with the principal icons which have been incorporated in the software, and were invited to indicate for each, the action they believed would be initiated by selection of that icon in the context of an SSM study. In this way, the extent to which the icons chosen are evocative of the associated actions has been probed (the resultant questionnaire is available upon request as Part I of Appendix E of Zhang, 1993).

## Icon discriminability

In a complementary experiment, users were presented with a list of required actions, and a full set of icons as used in SoftCase. Users were invited to indicate next to each required action, one or more of the icons they believed might invoke the action. In this way, the potential for users to be confused when faced with a selection of icons in Soft Case has been probed (the resultant questionnaire is available upon request as Part II of Appendix E of Zhang, 1993).

## Navigation through the program

This process involved a short demonstration of SoftCase given by the operator, prior to the system being handed over to the user. As noted above, the system supplies only rudimentary context sensitive help. Our interest was in the extent to which, with minimal demonstration, the product was accessible to users. The user was invited to undertake entry of provided SSM study data spanning rich picture, relevant system, root definition and conceptual model entry. Users’ responses were video recorded for subsequent analysis. In this way, user confusions as to control of the sequence of actions required to progress through entry of typical study data has been probed (the data entry scenario to which users responded is available upon request as Part III of Appendix E of Zhang, 1993).

## Focus group meeting

Following the above procedures, a meeting of the SSM practitioners involved in the evaluation was convened. The focus group was invited to reflect on four issues in the light of their experience with the functional prototype. Specifically:

(1) Do you believe the product should be changed to address shortcomings in: (a) functionality? (b) usability?

(2) Do you believe that having the SoftCase tool would change the way in which you apply SSM techniques?

(3) Do you believe that having the SoftCase tool would change the way in which you would follow the broader process of SSM?

(4) What is your opinion of the future for SSM support tools of this kind? and generally?

In this way, participants were encouraged initially to critique the present product, and then to move to questions of the effect they believe such tools might have on both the way in which they apply specific techniques (e.g. conceptual model building), and in broader terms how it might affect the way they would approach SSM study organization and conduct.

## Evaluation of the SoftCase toolkit

## Participants

A user panel was assembled with one member from each of the following categories:

(1) Novice Post-Graduate User trained in SSM;

(2) Inexperienced SSM Practitioner, but with substantial experience using other methodologies;

(3) Experienced SSM Practitioner trained in Australia; and

(4) Experienced SSM Practitioner trained at Lancaster.

## Conduct of Phase 1 of the evaluation

Each user subject initially completed the Phase 1 activities, including video recording of navigation through the program. The questionnaires took approximately 20 min to complete, whilst the navigability experiment took approximately a further 40 min for each subject. The questionnaires and video recordings were analysed using established questionnaire analysis methods and tracing techniques from the human computer interaction literature (Booth, 1989).

## Results for attribution of meaning to icons and icon discriminability

The choice of icons accessible from the Rich Picture Builder was largely confirmed. Of the tool palette icons, minor confusion of the curve drawing tool was recorded, but otherwise no uncertainties in the attribution of meaning were observed. Of the pre-stored icons, only those associated with escape back to the bookshelf and escape from the system registered any degree of confusion. A review of the choice of these icons in subsequent development is planned.

## Results for navigation through the program

Analysis of the videotaped sessions indicated only four operations which provoked user responses which departed from the sequence of actions intended by the system designer. These involved access to the symbol library (during Rich Picture entry), creation of a text window (during entry of data in background to the Rich Picture), transition from the Rich Picture Builder to the Relevant System Namer (during Relevant System entry), and creation of an activity ellipse (during Conceptual Model entry). It is beyond the scope of the present paper to discuss these in detail, beyond noting that means of addressing each problem (e.g., confirmatory messages, on-screen help) have been devised, and that the importance of conducting such navigability evaluation is strongly endorsed.

## Functionality and usability

Phase 2 of the evaluation, a Focus Group Meeting to probe reactions of the four practitioners to the functionality and usability of the product, yielded several hours of audio taped reflections, addressing in particular insights into the potential of the tool to alter practitioners’ use of SSM techniques and processes.

Some of the more significant observations expressed included the following.

(1) Some doubt was expressed as to the potential application of computer technology to support the rich picture development phase. In particular, users observed that it took an unacceptably long time to create meaningful graphic representations of objects required in a rich picture, given the set of drawing primitives supplied. Indeed, some observed that given the time taken to draw a reasonable representation, they would in practice find themselves asking whether it was worth including any objects other than those which could be loaded directly from the symbol library.

With regard to the use of a symbol library, users questioned the time it might take to scan a large library to find a suitable symbol.

Users also questioned the constraints of displaying an extensive rich picture on a small screen in a way which would allow the full context to be appreciated. Users were unconvinced that zoom and scroll (which was available in the prototype) would address this problem, as they believed context would be lost. Some technologies, beyond those used in

SoftCase, which might address these concerns are discussed below.

(2) The user panel questioned the value of storing additional material in the background, hidden behind icons placed in the rich picture. Specifically, it was felt that the precise location of material so stored might be forgotten. Some technologies, beyond those used in SoftCase, which might address these concerns are discussed below.

(3) The user panel expressed the view that the power of tools of this kind might be better realisd if they were to address the more mechanical aspects of an SSM study. Specifically cited were:

• maintenance of root definition/conceptual model hierarchies, including level consistency checking; and

• generation of initial comparison work sheets and Maltese Crosses.

(4) Notwithstanding the possible use of computer technology to enforce consistency of the logical linkages shown on various sub-system expansions, the panel expressed concern at the notion of any type of artificial intelligence support to the SSM practitioner. Amongst possibilities discussed were the notions that the tool might suggest possible activities for a conceptual model, based upon a supplied root definition, or that the tool might automatically suggest potential new information processing procedures based upon a supplied Maltese Cross. The panel felt that provision of such advice would constrain the thought processes of the SSM practitioner.

(5) The panel speculated that the future of an SSM computer-based support tool might not lie in its use as a tool to maintain the diagrammatic and textual products of an SSM study at all, but that it might instead be recast as an instructional support tool to the practitioner. It was suggested that the tool might be structured to provide methodological prompts and hints to the analyst over the lifetime of a project.

An alternative, possibly complementary future, saw the tool as a means of presenting study products (diagrams, tables, etc) to those in the problem situation. In this context, the ability to recall data, notes and diagrams might facilitate the promotion of debate.

## Discussion of the choice of technology to support an SSM analyst

Presentation techniques appropriate to the display of Rich Data (including Multi-Media)

As reported at points (1) and (2) of the previous section, the response of users to the notion of entry of rich pictures on a small screen, with associated material activated by mouse clicking on an icon, was questioned. Specifically, concern was expressed at:

(a) The time taken within SoftCase to create a meaningful graphic representation of a rich picture object given a set of drawing primitives.

(b) The limited size of a symbol library which might be created, and problems of efficiently scanning that library to find a suitable symbol.

(c) The difficulties of displaying an extensive rich picture on a small screen in a way which would allow the full context to be appreciated, rather than losing that context as might happen if one simply scrolled across the picture, or zoomed in on specified sections; and

(d) The ease with which the precise location of material hidden behind icons placed on a rich picture might be forgotten.

In part at least, these observations may be a response to the technology adopted in the SoftCase implementation, rather than the functionality which the product sought to provide. In response, investigation of the following technologies might be considered:

In response to point (a), the use of pen technologies, which would allow the user to draw directly to the screen, might be investigated.

An alternative or complementary response would see the provision of a large and extensible library of symbols, but as indicated at point (b), this would only be successful if technologies for rapid discovery of useful symbols could be provided.

Point (c) demands substantial research into display technologies, in particular technologies such as bifocal displays used in the presentation of map-based data, which maintain contextual information (Leung & Apperley, 1993).

Point (d) would require investigation of supporting technologies to browse the full library of material hidden behind symbols to discover their location. Visual cues as to the position and nature of buttons, and catalogues of hidden materials might be investigated.

## Support of the comparison phases of SSM

Feedback from the user panel at point (3) in the previous section encouraged extension of the tool to include the comparison phases of SSM. Further research is planned to extend the implementation and evaluation reported herein to include automated preparation of skeleton work sheets and/or Maltese Crosses, consistent with the preceding modelling.

## ‘Intelligent’ tool support

The discussion reported at point (4) in the previous section should provide impetus to the intention reported by Avison et al (1992) to investigate development of ‘intelligent’ support. The tool provided herein was deliberately cast as an SSM information repository. The development and evaluation of alternative ‘intelligent’ tools is imperative.

## The target market for computer support

A final area demanding investigation, highlighted at point (5) in the previous section, is a clarification of the audience for such tools. The tool proposed herein was originally conceived as a repository for the data gathered and structured by an SSM practitioner in the course of a study. Feedback from the user panel would suggest that at least some practitioners see the tool’s value more as a provider of prompts to the practitioner during a study, or as a vehicle to support presentations on progress of the study to date to those involved in the problem situation. A potential approach to resolving these questions might be to tailor the prototype developed herein towards such audiences and to evaluate its utility in such environments. Such research is under consideration.

## Support of flexible use of modelling tools

Recent work by Guindon (1989) suggests that the natural inclination of many analyst/designers is not purely top– down, but rather a mixture of top–down and bottom–up, with frequent deviations from prescribed methodologies. Recent work by Khushalani et al (1993) seeks to build a model of such behaviour (termed ‘opportunistic’) in the SSM practitioner, and to investigate the consequences of such behaviour for support tool design. Whilst SoftCase has provided some flexibility in the sequence of use of tools, in at least one significant respect flexibility, as would be demanded by a method which encourages informality, has not been available. Specifically, the development of conceptual models in other than a top–down sequence is not provided. Technologies which would support the development of fragments of conceptual models, at various levels of resolution, to be subsequently pieced together to provide a coherent levelled model, provides a substantial technical challenge, particularly if the consistency of logical linkages between activities modelled at various levels is to be enforced. It should be noted that such a requirement is not unique to SSM. Departures from top–down development of data flow diagrams in structured approaches is not supported by present CASE tools.

## Some possible directions for investigating the impact of computer support on the SSM process

As previously stated, the evaluation described in this paper has focused primarily on the accuracy, timeliness, completeness and appropriateness of format with which the tool supports the production of SSM study artifacts such as rich pictures and root definitions. However, many questions remain concerning the effects that the tool might have on both the SSM study process itself and the learning about a problem situation which should result if a study is efficacious. Whilst a tool may result in a tidier and more rapidly produced rich picture, for example, this might be counterproductive as far as the generation of creative ideas and learning are concerned. Though the empirical examination of such issues poses conceptual and methodological problems, several options for future study remain.

Firstly, field studies may assist in producing descriptive accounts of tool use in the real world. Although field studies can inform about the use of the ‘tool in context’, they have been criticised on the grounds of a lack of experimental control and generalisability (Vessey & Weber, 1984).

Secondly, comparison of computer and manually supported approaches could shed light on their relative efficacy, efficiency and effectiveness. Data could be collected on aspects of the process, for example its duration, usability and learnability, and the product, e.g. its scope, granularity and quality as defined by some extant criterion. Comparative studies that hold the tool support constant and vary the analyst profile may be useful in establishing the extent and presence of, e.g. expert-novice differences. Comparative studies are best conducted in the laboratory where appropriate experimental control can be maintained. For this reason, it may be appropriate to plan an integrated programme of both comparative and field studies in order to gain a more complete understanding of the benefits of the tool, the tool’s effect on the process and product, and how the tool works in context.

Finally, one might conduct more fundamental, modelling-oriented, research aimed neither at understanding how the tool functions in a given context, nor at describing the relative merits of the tool per se, but rather at creating a ‘theory of tool use for SSM’. A modelling approach, though far more ambitious than either field or comparative approaches, offers the greater promise in the form of a generalised theory capable of supporting further tool and method development.

In summary, empirical attempts to determine the effects of computer support on the SSM study process and the resultant learning will need to balance the requirements of rigorous experimental control against those of ecologically valid enquiries (Vessey & Weber, 1984; Curtis, 1988). It is suggested that both field and comparative approaches to understanding are appropriate, and that both field and comparative approaches can, over time, contribute to an integrated theory of tool use for SSM.

## Conclusion

This work has identified the constructive contribution that computer-based support could make to the application of SSM techniques. The paper not only describes the realisation of one such tool, but also the type of evaluation which might give insight. The questions raised by this evaluation should not be interpreted as criticism of the notion of computer support of SSM, but as a challenge and an impetus to the work of those few researchers working in this area. In particular, although there have been some hints of concern as to the effect of computer-based support on the SSM process, in the responses of users to the present support tool, we would take the position of Avison and Golder (1991b), that drawing strong conclusions based on such conjectures would be best postponed until exploratory development has made a selection of potential tools available, and such tools have been evaluated in a disciplined fashion, such as proposed in this paper.

Acknowledgements – The authors thank Steve Howard (Swinburne University of Technology, Melbourne, Australia) for useful suggestions concerning empirical evaluation strategies, and the referees for their constructive comments on the paper.

## References

<sup>Avison</sup> <sup>DE</sup> and <sup>Fitzgerald</sup> <sup>G</sup> (1988) Information Systems Development: Methodologies, Techniques and Tools. Blackwell, Oxford.

<sup>Avison</sup> <sup>DE</sup> and <sup>Golder</sup> <sup>PA</sup> (1991a) The Need for Tool Support for Soft Systems. In Systems Thinking in Europe (<sup>Jackson</sup> <sup>MC</sup> et al, Eds), pp 327–332, Plenum, New York.

<sup>Avison</sup> <sup>DE</sup> and <sup>Golder</sup> <sup>PA</sup> (1991b) Tools supporting soft systems. In Systems Thinking in Europe (Jackson MC et al, Eds), pp 333– 339, Plenum, New York.

<sup>Avison DE, Shah HU</sup> and <sup>Golder PA</sup> (1992) Towards an SSM toolkit; rich picture diagramming. European Journal of Information Systems 1(6), 397–407.

Avison DE, Shah HU <sub>and</sub> Golder PA <sub>(1993)</sub> <sub>Tools</sub> <sub>for</sub> <sub>SSM:</sub> <sub>a</sub> justification – a reply to ‘critique of two contributions to soft systems methodology). European Journal of Information Systems 2(4), 312–313.

<sup>Boland</sup> <sup>RJ</sup> (1987) The in-formation of information systems. In Critical Issues in Information Systems Research (<sup>Boland RJ</sup> and <sup>Hirschheim</sup> <sup>RA</sup> Eds), pp 363–379, Wiley, New York.

<sup>Booth</sup> <sup>P</sup> (1989) An Introduction to Human–Computer Interaction. Lawrence Erlbaum, East Sussex.

<sup>Checkland</sup> <sup>P</sup> (1981) Systems Thinking, Systems Practice. Wiley, Chichester.

<sup>Checkland</sup> <sup>P</sup> and <sup>Scholes</sup> <sup>J</sup> (1990) Soft Systems Methodology in Action. Wiley, Chichester.

Checkland PB, Forbes P <sub>and</sub> Martin S <sub>(1990)</sub> <sub>Techniques</sub> <sub>in</sub> <sub>soft</sub> systems practice part 3: monitoring and control in conceptual models and in evaluation studies. Journal of Applied Systems Analysis 17, 29–37.

Chonoles MJ, Schardt JA <sub>and</sub> Magrogan P <sub>(1995)</sub> <sub>Objects</sub> <sub>are</sub> <sub>not</sub> enough. Report on Object Analysis and Design 2(1), 52–56.

<sup>Coombe</sup> <sup>I</sup> and <sup>Dolling</sup> <sup>A</sup> (1992) private communication.

<sup>Curtis</sup> <sup>B</sup> (1988) Human Factors in Software Development. IEEE Computer Society Press, Los Alamitos, California.

<sup>Davenport</sup> <sup>MS</sup> and <sup>Ayers-Hunt</sup> <sup>J</sup> (1995) Soft systems analysis and modeling tool (SSAMT). In Critical Issues in Systems Theory and Practice (<sup>Ellis K</sup> et al, Eds), pp 291–295, Plenum, New York.

<sup>Guindon</sup> <sup>R</sup> (1989) The Process of Knowledge Discovery in System Design. In Proceedings of HCI ’89 International. Elsevier, New York.

<sup>Hakiel S</sup> and <sup>Easterby R</sup> (1986) Methods for the design and evaluation of icons for human-computer interfaces. In Proceedings of the IEEE 2nd International Conference on Command, Control, Communications and Management Information Systems. Bournemouth.

<sup>Jackson M</sup> and <sup>Keys P</sup> (1984) Towards a system of systems methodologies. Journal of the Operational Research Society 35, 473–486. <sup>Joseph R</sup> (1990) Toolbook Companion. Cobb, USA.

Khushalani A, Smith R <sub>and</sub> Howard S <sub>(1993)</sub> <sub>Understanding</sub> opportunism in design: theory building using the soft systems methodology. In Proceedings of the 4th Australian Conference on Information Systems. Brisbane, Australia, September.

<sup>Kreher</sup> <sup>H</sup> (1993) Critique of two contributions to soft systems methodology. European Journal of Information Systems 2(4), 304–308.

<sup>Ledington</sup> <sup>J</sup> and <sup>Ledington</sup> <sup>P</sup> (1996) Beyond functional decomposition in soft systems methodology: the decision-variable partitioning approach. In Proceedings of the 7th Australasian Conference on Information Systems, pp 397–408, Hobart, Australia, December.

<sup>Leung Y</sup> and <sup>Apperley M</sup> (1993) A unified theory of distortionoriented presentation techniques. Technical Report SUT-CS-22/93, Department of Computer Science, Swinburne University of Technology.

<sup>Lewis PJ</sup> (1992) Rich Picture Building in the Soft Systems Methodology. European Journal of Information Systems 1(5), 351–360.

<sup>Mumford</sup> <sup>E</sup> (1994) Technology, communication and freedom: is there a relationship? In Transforming Organisations with IT, (<sup>Baskerville</sup> et al, Eds), p 320, Plenum, New York.

<sup>Ormerod</sup> <sup>R</sup> (1993) Putting soft OR methods to work: a case study. Warwick Business School Research Paper No. 90, April 1993.

<sup>Senn</sup> <sup>JA</sup> (1985) Analysis and Design of Information Systems. McGraw-Hill, New York.

<sup>Stansfield</sup> <sup>MH</sup> (1995) The role of information technology in support-

## About the authors

Junzhen Zhang has a BSc(Hons) from Shanghai University and recently obtained a Masters in Applied Science from Swinburne University of Technology. He is currently working in the computer industry in Melbourne, Australia.

Ross Smith is a Principal Lecturer in the School of Computer Science and Software Engineering at Swinburne University of Technology. He received a PhD in Computational Physics from Melbourne University and became interested in SSM while working as an operations research analyst in the Australian Department of Defence. Since joining Swinburne in 1989 he

ing the use of systems concepts in the process of knowledge elicitation. In Critical Issues in Systems Theory and Practice (<sup>Ellis</sup> <sup>K</sup> et al, Eds), pp 355–359, Plenum, New York.

<sup>Stowell</sup> <sup>F</sup> (1993) Information systems and systems science. In Systems Science: Addressing Global Issues (<sup>Stowell FA</sup> et al, Eds), pp 19–24, Plenum, New York.

<sup>Stowell</sup> <sup>F,</sup> <sup>West</sup> <sup>D</sup> and <sup>Javelaud</sup> <sup>V</sup> (1993) Developments in the automation of SSM tutorials using multimedia technology. In Systems Science: Addressing Global Issues (<sup>Stowell FA</sup> et al, Eds), pp 269–274, Plenum, New York.

Stowell F, West D and Stansfield M (1991) The application of an expert system shell to an unstructured domain of expertise: using Expert System Technology to teach SSM. European Journal of Information Systems 1(4), 281–290.

<sup>Sutherland</sup> <sup>A</sup> (1992) private communication.

<sup>Vessey</sup> <sup>I</sup> and <sup>Weber</sup> <sup>R</sup> (1984) Research on structured programming: an empiricist’s evaluation. IEEE Transactions on Software Engineering 10(4).

<sup>Watson</sup> <sup>R</sup> and <sup>Smith</sup> <sup>R</sup> (1988) Applications of the Lancaster Soft Systems Methodology in Australia. Journal of Applied Systems Analysis 15, 3–26.

West D, Stansfield MH <sub>and</sub> Stowell FA <sub>(1994)</sub> <sub>Using</sub> <sub>computer-</sub> based technology to support a subjective method of inquiry. Systems Practice 7(2), 183–204.

<sup>Wilson</sup> <sup>B</sup> (1990) Systems: Concepts, Methodologies and Applications. Wiley, Chichester.

Winter MC, Brown DH <sub>and</sub> Checkland PB <sub>(1995) A role for soft</sub> systems methodology in information systems development. European Journal of Information Systems 4(3), 130–142.

<sup>Yourdon</sup> <sup>E</sup> (1992) Decline and Fall of the American Programmer. Prentice-Hall, Englewood Cliffs, New Jersey.

<sup>Zhang</sup> <sup>J</sup> (1993) An Investigation of Computer Support of the Soft Systems Methodology. Master of Applied Science Dissertation, Department of Computer Science, Swinburne University of Technology.

has taught and carried out research in systems methodologies, software engineering and related areas.

Richard B Watson is a Senior Research Scientist in the Australian Department of Defence and part-time Lecturer at Swinburne University of Technology. He has a PhD in Nuclear Physics from the Australian National University and worked for many years as an operations research analyst in the former Central Studies Establishment in Canberra. In this position he pioneered the use of SSM and has since carried out research in it at Swinburne.
