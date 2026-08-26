---
otero_id: 17471
otero_key: "XQWUYUNQ"
title: "Interacting with software system components"
authors: "Zhengxin Chen"
year: "1995"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)00023-l"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Interacting with software system components

Zhengxin Chen

Department of Computer Science, University of Nebraska at Omaha, Omaha, NE 68182-0500 USA

## Abstract

An ideal user interface is a crucial factor to support the functionality of software systems for computerized decision making process. A recent trend has been to develop intelligent and flexible user interface on the top of software systems. However, as noted by Woods, a technology driven approach to the development of intelligent interfaces is likely to provide the illusion of assistance while creating a new layer of burdens and complexities. To avoid creating an ever thickening layer of user interface, we have explored an approach which incorporates user interface into software system components design. In this article we point out that existing approaches in related work can be systematically expanded to form an alternative paradigm for interface design. In particular, we discuss a concept called user interface wrapper for software components. Due to the importance and popularity of expert systems, our discussion is mainly around interface design of expert systems, although the basic idea can be extended to designing other software systems as well. According to this approach, each major component of an expert system (including the knowledge base, the inference engine and the explanation unit) is wrapped by a layer of user interface. A case study is provided, in which the user interface wrappers are implemented as windows of system components. A discussion on pros and cons of this approach is provided.

Keywords: Artificial intelligence; Expert systems; User interface wrapper

## 1. Introduction

An ideal user interface is a crucial factor to assist the success of functionality of software systems in computerized decision making process. A recent trend has been to develop intelligent and flexible user interface on the top of software systems. For instance, there have been a lot of discussions on how to support the design and development of expert system user interface (eg. [11]). However, as warned by Woods [20], although ‘intelligent interfaces’ are sometimes seen as a solution to the growing demands of highly technological and highly automated fields of activity, a technology driven approach to the development of intelligent interfaces is likely to provide the illusion of assistance while creating a new layer of burdens and complexities.

To avoid creating such an ever thickening layer of interface, in this article we explore an alternative approach to support the coupling between user interface and software functionality. We introduce the idea of incorporating user interface design into expert system components design, with the hope that this experimental approach will both enhance the functionality of the software system and the flexibility of user interface. In particular, a concept called software component wrapper is proposed. We also describe an experimental expert system in which wrappers are implemented as component windows.

In this article, we discuss various issues related to this approach, including the motivations behind this approach and some important features of this approach. We compare this approach with some existing approaches, and discuss some problems must be solved.

## 2. General principles of interface design in software development

The need for user involvement in interface design $[2–4]$ can be justified from general principles on interface design in software development. Recently, Blumb $[6]$ has re-stated Shneiderman's 'Eight Golden Rules' $[16]$ for interface design. These rules (which are referred to as GRs) are summarized below.

GR 1. Strive for consistency.

GR 2. Enable frequent users to use shortcuts.

GR 3. Offer informative feedback.

GR 4. Design dialogues to yield closure.

GR 5. Offer simple error handling.

GR 6. Permit easy reversal of actions (namely, undo a previous action).

GR 7. Support internal focus of control (that is, the user should feel that he is in charge, and not the system).

GR 8. Reduce short-term memory load of the user (eg. limit what must be remembered in multiscreen scenarios by displaying context information on each screen; use clear mnemonics and sequences of action).

We believe that these rules should be used as a guideline for interface design, and should be incorporated as much as possible into the design process. As to be discussed in a later section, the approach described in this article addresses some of the above concerns, particularly Golden Rules 7 and 8.

## 3. Human involvement in human-computer symbiosis

In a recent paper, Bobrow pointed out that interaction is the new challenge for AI [7]. In the context of expert systems, as observed by Stelzner and Williams [17] and recently restated by [1], there has been a move from the traditional expert systems to expert advisory systems (ie. systems in which the user the system share the reasoning and the decision-making tasks); the human remains very much in the decision-making loop. In expert advisory systems, the prevailing metaphor for the interface is the domain model which the user and the system can manipulate and act on. Since the user is actively involved in the decision-making process, there is increased necessity for the user interface to support the user's cognitive task. This requirement encourages use of the interface as model world metaphor, a metaphor that is directly supported by a deep model of knowledge [17].

Started from the perspective of expert systems as decision aides, [13] explored two key variables affecting user/expert system interaction: (1) user mental models and (2) the nature of the expert system inference explanations. The expert system does not have to be a psychological model of the user, imitating a human's reasoning process. Rather, its knowledge representation techniques and control procedures must be able to capture the fullest possible range and power of the human expert's ability in a particular domain and provide explanation. The important lessons here is to incorporate different kinds of users into system design. In fact, it has been argued that users should be involved into expert system design, and even become a partner of the problem solving process [2-4].

Much study has been around the construction of friendly interface channels, such as natural language processing for text interface, or more recently, graphic user interface. However, the most important factor is related to user modelling. It has been noticed that there are two kinds of models involved: the user's conceptual model of the system and the system's conceptual model of the user [18]. A recent article [13] revisited the issue of users' cognitive models. Although this current paper does not directly deal with user models, the basic idea behind our approach is our profound belief that user models should be incorporated into software interface design. In order to achieve this, users should be allowed to access system components more directly for enhanced functionality in supporting the needs of various users. Similar concern has been addressed in a recent talk by Garcia [8] who noticed that the activity of human in the feedback loop of problem solving has often been neglected; but this activity has important practical consequences as the interface makes possible a synergistic guidance and complementarity between the capabilities in the biological and electronic systems.

A notable remark must be mentioned here is the interface design concerning components of expert systems $[13]$ . Hamil $[9]$ listed 10 research questions of human/expert system interactions by focusing on the theme of the control and communication of relevant information. We believe that a more systematical study on this issue is needed.

Although system component-related considerations have been included into user-interface design, existing approaches generally assume that it is the system determines which component(s) should be involved based on the functions requested by the user; that is, the connection between the user and the system's various functioning components is through the system's interface component. In contrast to this, in our approach, as to be discussed in the next section, the users themselves are granted some degree of access to the components in a more direct manner.

## 4. Towards a new design paradigm

The importance of user responsibility and user participation in problem solving has drawn more and more attention. In a system constructed in such a manner, the user does not simply retrieve what the system can provide; he or she also participates the reasoning process itself (in some degree). This will not only reduce the burden of the top-layer system-user interface, but also increase system functionality as well. User involvement in system design and problem solving signifies an important shift from the traditional paradigm which emphasizes transparency in ininterface design, namely, users are shielded from system design and problem solving detail. As to be explained later in the discussion section, each paradigm has its pros and cons.

These considerations, along with the existing experimental work as summarized in the previous section, can help us to identify two kinds of user-interface design paradigms. According to the traditional paradigm, users are provided with global system functions through a centralized interface component; while in the new paradigm users are given more direct access to components; users are thus granted some degree of the control over the system.

In order to explore this paradigm shift, in the remaining part of this article we investigate an approach which employs a notion of component interface wrapper. We also provide the rationale of exploring this approach. In order to make our discussion concrete, in this article our discussion focusses on the development of one particular kind of software, namely, expert systems.

## 5. Designing expert system components with user interface wrappers

## 5.1. Interface component as gateway to access other system components

As researchers in user interface design noted, a high-level ‘conceptual model’ of the interface is of major importance to the user’s ability to learn an interface and to their comfort and efficiency in using it. It is also noted that the interface designer should be involved in the design of the system itself, for explaining the system’s behaviour, as well as for other reason $[10]$ . These observations are extremely important for interface design of expert systems.

One important principle used in expert system design is the separation (or orthogonality) between knowledge and control. In fact, this idea can be pushed a little further: In an expert system, system components, such as knowledge base (rule base or other form of knowledge), inference engine (the driver routine of knowledge base), explanation unit (which provides answers for ‘how’ and ‘why’ type questions from the user), working memory (which consists of case-specific data) and user interface, are all separated from each other (namely, self-contained).

![](/api/attachments/XQWUYUNQ/fulltext/images/85b273590020fc75fe5a933385798685a5746192229102d01a06924a6900da14.jpg)  
Fig. 1. Expert system with conventional user interface. Notice that access to the system components, such as editor of knowledge base or inference engine, is carried out through a centralized interface component.

A conventional expert system is depicted in Fig. 1, which includes all major components should be found in a typical expert system. Notice that in this classical configuration, access to the system components, such as editor of knowledge base or inference engine, is carried out through a centralized interface component.

A problem associated with conventional approaches is that in order to make user interface intelligent and flexible, the centralized user-interface component may become quite complex to the system design, and an increased complexity of user interface may become conflict to the design goal of software system functionality.

![](/api/attachments/XQWUYUNQ/fulltext/images/37eb498751e2052b7f010cf88562be34e0d738e3e10531ff7b8c7ea32f9e69b8.jpg)  
Fig. 2. Expert system components with user interface wrappers. Notice that interface component serves as a gateway so that users can directly access system components through this gateway.

The original model of expert system as depicted in Fig. 1 can be revised so that each component in the system is attached by its own user interface wrapper. In particular, we consider the three most fundamental components in expert systems, namely, the knowledge base, the inference engine, and the explanation facility.

Fig. 2 depicts the model of an expert system which has components with user interface wrapper (these components are denoted by double-sided rectangles). Compare Fig. 2 with Fig. 1, we notice that the user interface component is slightly reduced. On the other hand, other components in the system, including knowledge base, inference engine and explanation component are all ‘wrapped’ by user interface components. In other words, the interface component now serves as a gateway so that users can directly access system components through this gateway.

## 5.2. Features of the new model

Unlike the conventional approaches, in this revised model, a portion of user interface can 'penetrate' into system components, namely, to be distributed into the entire expert system. Instead of viewing user interface as an additional layer built on the top of system functionality, under this new design approach, the user will conceptually view the user interface as an extension of the various functioning components. In fact, we may envision that each functioning component is 'wrapped' by a small layer (the 'wrapper') of user interface which is a portion of the user interface specially designed for that system component. The concept of wrapper will benefit both the end user who is consulting the software system for decision making, as well as the software system designer. From the end user's viewpoint, this new approach will make him feel that he is more deeply involved in computerized problem solving or decision making, as well as a kind of control over system execution. This also enhances the user's confidence over the software system he is using. In addition, from the designer's viewpoint, since components functionality and user interface are somewhat integrated, components functionality can be strengthened through improved user interface.

The need for such kind of decentralized interface can also be justified from the varieties of user needs. There may be many different kinds of users; a user may be an experienced AI programmer, or a novice end user. Different kinds of users may have different needs. For example, an inference process tracer allows a user to visualize the inference process step by step, and a full featured rule base editor provides a user to update the rule base as needed, both facilities would be very desirable for an experienced AI programmer but may be of very little interest for a naive user. A designer may also consider allowing the programmer access to different types of inference (namely, backward or forward chaining). On the other hand, a novice user may not be as interested in the wide range of features but rather a system that is easy to use and one that is understandable. The explanation facility might be an important feature in building confidence in the system for the novice and sometimes sceptical user.

The users may also have different concerns over the system functionality. For example, in a rule-based expert system, it is critical how rules are arranged in the rule base and how they related to other rules. If the expert system is not designed to provide for integrity of the rule base, then appropriate security access may need to be assigned to the rule editor on a user by user basis. The designer may allow the AI programmer access to insert and update rules whereas a novice user would have read only access to the rule base. The task of providing different access needs for different types of user can be achieved by attaching a small layer of user interface wrapper outside of individual components.

From these concerns we can determine what the new model can do while the old model cannot. The difference is rooted at different ways of envisioning the human-computer symbiosis. In fact, wrappers work like middlemen between the system and the user; an individual user will envision himself or herself as part of the system component for achieving a particular goal (such as inference or explanation). Each wrapper can be expanded independently as needed, without bothering any other components.

## 5.3. Functionality of wrappers

As indicated earlier, wrappers of the components are used to extend the functionality of the components through the user involvement. In the following, we briefly describe what kind of functionality can be provided by wrappers of inference engine and the explanation unit.

## Wrapper of inference engine

The wrapper for inference engine may provide various facilities to users, such as to suspend reasoning (so that the user may examine what is going on in the current reasoning process, for example), or to alter reasoning path (by providing bias in guiding conflict resolution), etc. The wrapper of inference engine serves as a channel so that the user can participate the problem solving process (in some degree). In a traditional interface, users are not granted the right to suspend the inference, or alter the reasoning path.

## Wrapper of explanation unit

The importance of the ability for an software system to tailor an explanation to the specific audience that requested has been recognized since long [19]. Central to the discussion of user models was the idea of achieving task goals. Reference [18] suggested more than one interface for different classes of users. Rather than designing several different kinds of interfaces, however, we can make the same interface more flexible by offering users various choices (or modes) for explanation. For example, the user may ask for an explanation according to the exact reasoning process, or an explanation in terms of some user-provided concepts (or keywords). These choices are provided through the wrapper of the explanation unit, so that a user can select a particular way for explanation.

## 6. Implementing wrappers as windows

Various methods may exist to implement the idea of software component wrapper. In this section, we provide a case study in which wrappers are implemented as component windows. This case study involves a referral expert system in which wrappers are implemented in windowed and event driven environment. The knowledge base of this system consists of 'if..then' type production rules. The system works in the field of managed health care to deal with the following decision problem, namely, a patient is referred by their family physician to a specialist for tests, evaluation, or treatment.

![](/api/attachments/XQWUYUNQ/fulltext/images/af2cd66b8064fa2e86544f44b7080ab7f5e23bc128e2669959f34c16b376724d.jpg)  
Fig. 3. Inference window and tracer window

Although windows have been widely used for the purpose of user interface, they are usually used in terms of functions of the whole system rather than of the components. For example, in the traditional way, the user envisions the interface facility as knowledge base editor, explanation requests, etc., all through a single interface component at the system level. The experimental program is aimed to work as a platform to explore the proposed approach so that a window of a component serves as an entrance for a user to directly access that particular component. The implemented part does not fully demonstrate all the important features of the wrappers as indicated before. However, it does provide a skeleton and can be extended to incorporate all the needed features as described in previous sections.

The system uses three windows which are available to the user at any time when the system is performing a consultation.

Rule base window. The rule base editor is the wrapper for the knowledge base. Through this window, the system allows the user to do all of the editing needed to create the initial rule base and maintain it. The system was designed in such a way so that a new rule base could be created by the user, so long as syntactical requirement is satisfied. When the user selects a file from the directory list it is read into the system as a dynamic linked list, thus facilitating rule updating.

Inference window. The inference window is the wrapper for the inference engine. It is an interactive prompting facility between the user and the inference process. The user may request to suspend or continue the inference process at any time.

Tracer window. The tracer window is the wrapper for explanation unit. It displays which rules are firing; it is able to answer 'why' type questions throughout the entire inference process. The explanation facility is closely tied to inference process. The current version of our system can answer the 'why' type question (namely, tell the user which rule is planned to fire next) and demonstrate it in the explanation window. During the inference process, each time a rule is fired the system will update a window on the screen called the explain/tracer window. This window keeps track of every rule fired and allows the user to suspend the inference process at any time and review the items in this window. As with the editor window, this window can be closed, resized, or moved around on the screen without interrupting the current editing of the rule base or inference in process.

A snapshot of the inference window and the tracer window is depicted in Fig. 3.

## 7. Discussion

7.1. A summary of some advantages of using wrappers in expert system design

From the expert system example, we may notice various advantages of wrappers implemented as windows for decentralized user interface. There are benefits for both designers and users. For example, employment of knowledge base wrapper facilitates knowledge base maintenance, because it is easy for the users to see which rules are good, which are bad, and it is also easy to update the rules through the rule base editor. The use of inference window and tracer window also facilitates debugging of inference engine. Other advantages include support of visualization in software development, support of system testing and understanding, support of cognition in software development, and integration of functions of software components and user interface.

Recall that in Shneiderman's Eight Golden Rules [16,6], Golden Rule 7 emphasizes the need for supporting internal locus of control (that is, the user should feel that he is in charge, and not the system). As exemplified by the use of windows, the use of software component wrappers apparently provides the user this kind of feeling. In addition, Golden Rule 8 states the need for reducing short-term memory load of the user (eg. limit what must be remembered in multiscreen scenarios by displaying context information on each screen; use clear mnemonics and sequences of action). This rule is apparently supported by the window implementation: the various windows serve as the multiscreen scenarios by displaying context information; the user's mental load is thus reduced.

## 7.2. The generality of the approach

Although so far our discussion has been mainly around expert systems, the idea illustrated there can apparently be generalized into other software systems as well. In fact, our previous discussion related to expert systems has revealed that components interface design should be and can be closely coupled with the design of component functionality; no particular assumption about knowledge base, inference engine or explanation unit has been used. For instance, the wrapper of inference engine should be designed to enhance the functionality of the inference engine, but no particular assumption about inference engine has been made. However, to verify the claim of the generality, more experiments and tests are needed.

## 7.3. Problems need be solved

Earlier we indicated that both the traditional paradigm and the new paradigm investigated in this article have pros and cons. The use of a component wrapper and the task of integration between component functionality and user interface may raise new design problems. Consequently, we should also investigate what are the limitations of the proposed approach, and under which conditions this approach is appropriate. The following are some problems of the new paradigm we have envisioned at this point. Appropriate methods should be developed (or incorporated) to deal with these problems.

(1) The feasibility problem. In the previous subsection we pointed out the generality of the alternative design paradigm. But this is not to imply that the proposed approach should always be used. In fact, among other things, the traditional user-interface design paradigm is much more matured, and has been widely accepted by system designers as well as the users. Therefore, there is no need to employ the alternative design paradigm when the traditional approach succeeds. When to use the alternative paradigm is a subject to be further explored.

(2) The potential security problem. With the increased degree of user participation of system activities comes the potential security problem. For instance, the function of knowledge base updating should be restricted to authorized personnel only. In addition, just like the case of knowledge discovery in database, the increased chance of system component access may result in deriving highly sensitive data from unclassified data [12]. This kind of inference should be prevented.

(3) The potential inconsistency problem. The update of the knowledge base may cause knowledge stored in the knowledge base inconsistent. Existing techniques in maintaining knowledge base consistency may be incorporated to resolve this issue.

## 8. Concluding remarks

Coupling intelligent interface and powerful functionality is a very important issue in computerized decision making technologies. The traditional approaches employ a centralized user interface which wraps outside of the entire system. In order to satisfy the ever increasing user expectation, the intelligent user interface may become a thick layer, and consequently causes the problem of consistency between functionality and user interface. To overcome this problem, in this article, based on existing approaches of related work, the concept of user interface wrapper for system components is introduced. The size of the centralized user interface can be reduced, and the integration between system functionality and user interface can be enhanced.

In this article, we have emphasized the importance of incorporating users into system design principles. Our discussion in this article has been mainly around expert systems. It has been noted that there are additional requirements for expert systems $[18]$ . However, since the considerations behind component wrappers do not rely on any particular features of expert systems, this approach can be generalized so that it is applicable to other software systems as well.

In a recent work [5] Blum noticed that there is a need for a shift to a new, software-oriented paradigm (rather than the traditional hardwareoriented one) for software design. We believe that the technical driven approach to the development of intelligent interface, as criticized by Woods [20], reflects the traditional hardware-oriented paradigm. On the other hand, since our proposed approach is intended to integrate interface design into software components design, it supports the shift to the software-oriented paradigm for software design.

## Acknowledgements

The author thanks Mr. M. Fitzgerald who implemented the case study and prepared Fig. 3 of this article. The author also thanks two reviewers' critical comments on an earlier version of this manuscript.

## References

[1] N.M. Avouris and S. Finotti, User interface design to expert systems based on hierarchical spatial representations, Expert Systems with Applications, 6 (2) (1993) 109–118.

[2] D. Berry and A. Hart (eds.), Expert Systems: Human Issues, Chapman and Hall, London, 1990.

[3] D.C. Berry and A. Hart, User interface standard for expert systems: are they appropriate? Expert Systems with Applications, 2 (4) (1991), (Special issue on expert systems standards), 245–258.

[4] D.C. Berry, Involving users in expert system development, Expert Systems, 11 (1) (1994) 23–28.

[5] B.I. Blum, Development of hardware and software, Information and Decision Technologies 18 (6) (1993) 375–393.

[6] B.I. Blum, Software Engineering: A Holistic View (Oxford University Press, New York, 1992).

[7] D.G. Bobrow, Dimensions of interaction: A shift of perspective in artificial intelligence, AI Magazine 13 (3) (1991) 64–80.

[8] O.N. Garcia, The human-computer interactive aspects of AI, Invited talk in the 7th IEA/AIE Conference, 1994.

[9] B. Hamil, Psychological issues in the design of expert system, in Proc. Human Factors Soc. 28thn Annul. Meeting (1984).

[10] J. Hendler and C. Lewis, Introduction: Designing interfaces for expert systems, Hendler, J. (ed.), Expert Systems: The User Interface (Ablex, Norwood, NJ, 1988) pp. 1–14.

[11] J. Logren, The Ingatius environment – supporting the design and development of expert system user interface, IEEE Expert 7(4) (1992) 49–55.

[12] D.E. O'Leary, Knowledge discovery as a threat to database security, G. Piatetsky-Shapiro and W.J. Frawley, Knowledge Discovery in Databases (AAAI/MIT Press, Menlo Park, CA, 1991) pp. 508–516.

[13] F.W. Rook, and M.L. Donnell, Human cognition and the expert system integration: Mental models and interface explanation, IEEE Trans. SMC, 23 (6) (1993) 1649.

[14] P. Sakariviya, From user interface design to the support of intelligent and adaptive interface: an overhaul of user interface software infrastructure. Knowledge-based Systems, 6 (4) (1993) 220-229. (Special issue on intelligent user interface).

[15] C.G. Thomas, Design, implementation and evaluation of an adaptive user interface. Knowledge-based Systems, 6(4) (1993) 230-238 (Special issue on intelligent user interface).

[16] B. Shneiderman, Designing the User Interface: Strategies for Effective Human-Computer Interaction (Addison-Wesley, Reading, MA, 1987).

[17] M. Stelzner and M.D. Williams, The evolution of interface requirements for expert systems, In Hendler (ed.) Expert Systems: The User Interface, Norwood, NJ, Ablex.

[18] R.C. Wexelblat, On interface requirements for expert systems, AI Magazine, 10 (3) (1989) 66–78.

[19] M.R. Wick, The 1988 AAAI workshop on explanation, AI Magazine, Fall 1989, pp. 22–26.

[20] D.D. Woods, The price of flexibility, pp. 19–28 in W.D. Gray et al. (eds.) Proc. 1993 International Workshop on Intelligent User Interfaces (ACM Press, New York, 1993).

Zhengxin Chen received Ph. D. degree in Computer Science from Louisiana State University in 1988. Since then he has been affiliated with Department of Computer Science at University of Nebraska at Omaha. He is interested in various issues in building intelligent information systems.
