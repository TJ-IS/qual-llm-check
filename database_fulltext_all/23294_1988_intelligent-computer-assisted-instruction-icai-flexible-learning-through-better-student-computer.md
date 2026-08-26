---
otero_id: 23294
otero_key: "BQHP4NYA"
title: "Intelligent Computer-assisted Instruction (ICAI): Flexible Learning Through Better Student-Computer Interaction"
authors: "Philippe Duchastel; Jacques Imbeau"
year: "1988"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1988.18"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Intelligent Computer-assisted Instruction (ICAI): Flexible Learning Through Better Student-Computer Interaction\*

Philippe Duchastel and Jacques Imbeau, Department of Educational Technology, Université Laval, Quebec, Canada

Abstract: Intelligent computer-assisted instruction (ICAI) uses artificial intelligence techniques to imitate in computer form the power of human tutorial processes. Its major technical features are the use of a modularized knowledge base instead of CAI's textual scripts, and the ability to interpret the student's statements and questions expressed in natural English. These features make ICAI systems extremely flexible and allow the student much greater learner control of the interaction than is traditionally possible in CAI. Other major elements of an ICAI system are an extensive model of the student and an explicit model of the tutoring process. Our research on the development of GEO, an ICAI system which interacts with students in the area of geography, is briefly described. Finally, the nature of this new technology is discussed in terms of its potential influence on university teaching and learning, especially in terms of our conception of learning.

## Introduction

Intelligent computer-assisted instruction (ICAI) is a form of computer-based learning which incorporates artificial intelligence (AI) techniques such as knowledge representation and natural language processing in order to adapt better the computer instruction to the needs and interests of the students. An example of such a system is GUIDON, developed at Stanford University (Clancey, 1982) to help medical students learn how to diagnose a certain class of infectious diseases. Another is Anderson's (1985) LISP TUTOR, developed at Carnegie-Mellon University to teach undergraduates the basic programming features of the LISP computer language.

ICAI is important to university teaching in the promise it offers as an important new tool in the gamut of learning resources an instructor can place at the disposal of his or her students to foster learning. Developments in ICAI can also be expected to have a beneficial influence on the way we conceive models of learning, and hence will contribute to shaping the future direction of educational technology proper. Far-reaching consequences for the nature of university teaching may well be involved here in the long run.

## Features of ICAI

Artificial intelligence research, which serves as the foundation for ICAI efforts, is aimed at replicating in computer form some of the cognitive processes exhibitited in human reasoning and human interactions generally. While this aim is necessarily limited (the extent of which is a hotly debated issue), the current attention given to expert systems as potent advisors in complex decisional situations shows the power of this software technology to assist us in ill-defined or otherwise-complex tasks. One such task is promoting learning in a variety of settings and with students of diverse abilities, uncertain prior knowledge, and varied interests. Like their predecessor CAI systems, ICAI prototypes are meant to address these issues, although with added finesse made possible by the power of AI techniques.

The central feature of an ICAI system, as with any AI system, is a knowledge base comprising a large number of distinct knowledge elements. Unlike their counterparts in traditional CAI, these knowledge elements are not part of a sequential flow of control within the program, but instead can be retrieved and combined by a separate control module in response to the requirements of the situation at hand. This very fine modularization of knowledge involves a structure (often known either as a semantic net or as a production rule set, depending on the techniques used) which makes some degree of inferential reasoning possible by the system. What this results in is a system which can respond to reasonable yet unanticipated questions put to it by the student. This result contrasts sharply with the much more rigid interaction (relatively speaking) of traditional CAI systems, in which all potentially meaningful questions and responses from the student must be anticipated by the courseware author and explicitly included in the program. Traditional CAI is frame-oriented, whereas ICAI is knowledge-oriented at a much finer level – that of the knowledge elements themselves.

A second powerful feature of many ICAI systems is the inclusion in the system of a component which can analyse student input expressed in natural English and which can translate this input into an internal form recognizable by the system's knowledge base. This natural language processing ability (itself an active area of research in AI) opens up the human-computer interaction well beyond the short-answer expectations and menu-driven interactions of CAI.

Thus, an independent knowledge base permitting inferential processing and a natural language capability combine to provide a large degree of flexibility in the way in which the learning session unfolds. The following brief extract from a GUIDON interaction with a medical student (whose input follows double asterisks) illustrates the extent to which this flexibility goes beyond that found in CAI.

YOU SHOULD NOW PROCEED TO ASK QUESTIONS THAT WILL ENABLE YOU TO MAKE A HYPOTHESIS ABOUT THE ORGANISMS (OTHER THAN THOSE SEEN ON CULTURES OR SMEARS) WHICH MIGHT BE CAUSING THE INFECTION.

\*\*HOW IS THE FACT THAT THE PATIENT IS BURNED RELEVANT?

THE FACT THAT PATIENT-326 IS SERIOUSLY BURNED WILL BE USED TO CONCLUDE THAT PSEUDOMONAS AERUGINOSA IS ONE OF THE ORGANISMS WHICH MIGHT BE PRESENT (IN ADDITION TO THOSE SEEN ON CULTURES OR SMEARS) (RULE 578).

\*\* HELP

TRY TO DETERMINE THE TYPE OF THE INFECTION: BACTERIAL, FUNGAL, VIRAL, OR TB.

\*\* WHAT IS THE PATIENT'S WBC?

THE WHITE COUNT FROM THE PATIENT'S PERIPHERAL CBC IS 1.9 THOUSAND.

What ICAI makes possible, through its use of AI techniques, is an interactive learning session which gives great control to the learner as to how the session should unfold. Learner control of instruction, long-sought but not often realized in CAI, is a prime capability of ICAI, as has been indicated elsewhere (Duchastel, 1986).

ICAI systems, however, are also meant gently to guide the student's exploration of the task domain being learned. To do this, they need to model explicitly both the student's ongoing status as it develops with respect to the domain as the learning session unfolds, and the very process of tutoring itself.

Given the flexibility involved in ICAI, the student modelling process must induce a representation not only of what error the student may have just committed (as is the case in frame-oriented CAI) but of the student's global knowledge of the domain, including areas where knowledge is fuzzy, as well as outright misconceptions. Such a global and dynamically changing model of the student is then used by the tutorial model proper to guide the interaction.

The tutorial model is meant to imitate the process which a human tutor would engage in similar circumstances. It includes a set of tutorial rules (such as 'if the student is forming an overgeneralization, provide him with an appropriate counter-example') which, working together, bring the student to recognize unfruitful leads and redirect the learning interaction. An examination of the tutorial features of the main current ICAI systems is presented in Duchastel and Imbeau (1986).

In summary, the principal components of a generalized ICAI system are involved in a structure like the following:

![](/api/attachments/BQHP4NYA/fulltext/images/a2a91cd7cec63aef2582f5d3b73cb16ee248792a14c9c79e9b9d3a4e642470e3.jpg)  
Figure 1. Principal components of a generalized ICAI system

It should be noted, however, that not all current ICAI prototypes have all of these features, as research in this field is very diverse and guided by a wide range of both pedagogic and computational concerns.

## ICAI in Quebec

What has been sketched up to this point is a broad outline of an ICAI system and of the concerns of this field of research. Before turning to a consideration of the impact of this new technology on university teaching and learning, a quick view of our current research in Quebec will be provided.

The ICAI system we are developing is an interactive system which will dialogue with students in the domain of geography. Geography (more specifically, South American geography) was the task domain of the very first ICAI system developed (Carbonell, 1970). It is a domain characterized by a relatively stable set of facts and relationships which can be structured in a semantic net (the form of its knowledge base) which can then be queried by the student.

Learning takes place through a mixed-initiative dialogue, ie one in which either the student or the system can ask questions and expect a reasonable response from the other. One aim of our research which goes beyond the earlier system is to provide GEO (the name of our system) with the capability to extend automatically its own knowledge as it interacts with various students. Thus, GEO will respond to questions from the student and ask some for tutorial purposes, but it will also ask questions when appropriate in order to learn from the student. The type of dialogue envisaged (GEO is still in its initial stage of development) is the following simulated conversation (student input follows double asterisks):

\*\* WHAT IS THE CAPITAL OF ONTARIO?

TORONTO.

\*\* WHAT IS ITS POPULATION?

THE POPULATION OF TORONTO IS 2.5 MILLION.

\*\* WHAT IS THE POPULATION OF KINGSTON?

I DON'T KNOW. WHAT IS KINGSTON?

\*\* IT IS A CITY.

O.K. WHERE IS IT?

\*\* IN ONTARIO.

O.K. IS KINGSTON NEAR TORONTO?

\*\* DO YOU KNOW VANCOUVER?

YES. VANCOUVER IS THE CAPITAL OF BRITISH-COLUMBIA.

WHAT PROVINCE IS NEXT TO BRITISH-COLUMBIA?

\*\* ALBERTA.

RIGHT.

What is sought in GEO is the ability of a system to augment its knowledge base as it encounters new information while interacting with students. This is a form of knowledge acquisition termed 'learning from being told' and is an active area of investigation within AI.

As seen in the dialogue above, GEO must possess a good natural language processor if it is correctly to interpret input from the student in the flexible manner portrayed. It will also need to keep track of what each student knows about geography and of any misconceptions he or she might have. Knowledge of the student, developed over many interactions, will guide the interaction, leading the student to review hazy facts or explore new areas. The student, however, despite tutorial guidance, can always initiate a new line of discussion leading the system to be responsive to his or her own interests.

GEO is currently under development, and while its domain of discourse is simple in terms of the type of knowledge it involves, it seems to us to be a potent tool for exploring learning and tutoring strategies, and eventually other forms of knowledge representation as well.

## The role of ICAI in teaching and learning

The fact that ICAI is an application area of artificial intelligence research and that its goal is to model human tutoring processes, may lead some people to believe that its long-term influence will be a dehumanizing one through which students will become more and more machine-bound and narrow in outlook. That view is certainly ill-founded, however, when one considers how the introduction of past technologies – from the book to CAI – has only enriched the learning opportunities of students and offered them wider scope for intellectual exploration. Of course, any technology can be abused until such cases eventually wither away from neglect, programmed instruction being a prime example. Any new technology requires some time for experimentation and maturation, its potential unfolding coming through trial and error.

The promising side of ICAI research lies in two areas. On the one hand, ICAI systems continue the quest of CAI in adapting instruction to the needs of the individual learner. Because of its particular features, ICAI can individualize learning to a much finer level than CAI can. This is due in large part, in addition to its extensive student modelling aspect, to its potential for true learner control of instruction through natural language querying. In CAI, all interactions must be explicitly preplanned by the course designer, a formidable and never totally successful task. ICAI, on the other hand, creates a learning environment in which the student can spontaneously explore the task domain according to his or her own interests and perceived understandings.

The very flexibility of learning interactions offered by ICAI also affects our own models of learning, which constitute a second impact of ICAI research on our view of the educational process. Educational technology has generally involved a didactic philosophy of teaching in which instructional design has always played a major role. Prescriptive design is still involved in ICAI systems, but the major aim is one of creating much more open-ended learning environments (responsive environments) in which the student can freely explore a domain of interest with the knowledge that he or she is in control of the learning situation. ICAI thus adds a new dimension to learning without, however, removing the value of other means of instruction where these are appropriate.

Computer technology is innovating at a very fast pace in many fields and it is not possible to predict just how it will eventually impact on university teaching and learning. Contemporary education, however, has the interesting task of integrating this new technology (in its most recent forms) into the educational process in order to profit from its promise of contributing to enhanced student learning.

## References

Anderson, J. R. and Reiser, B. (1985) The LISP tutor. Byte, April 1985, 159-175.

Carbonell, J. (1970) AI in CAI: An artificial intelligence approach to computer-assisted instruction. IEEE Transactions on Man-Machine Systems, MMS-11, 4.

Clancey, W. (1982) Tutoring rules for guiding a case method dialogue. In Intelligent Tutoring Systems (D. Sleeman and J. S. Brown, eds) Academic Press, New York.

Duchastel, P. (1986) Intelligent computer-assisted instruction systems: The nature of learner control. Journal of Educational Computing Research, 2, 379-393.

Duchastel, P. and Imbeau, J. (1986) Tutoring strategies in ICAI. Proceedings of the 5th Canadian Symposium on Educational Technology, Ottawa, 89-94.

## Biographical notes

Dr Philippe Duchastel has been involved in information technology since the 1970s, when he was working in distance teaching at the Open University in Great Britain. He is currently building ICAI prototypes and exploring modes of learning as people interact with information-rich systems in educational and training settings.

Dr Jacques Imbeau has a background in physics. He has been involved in computer-assisted learning for a number of years and is currently exploring ICAI possibilities in physics.

Address for correspondence: Department of Educational Technology, 1466 de Koninck, Université Laval, Quebec G1K 7P4, Canada.
