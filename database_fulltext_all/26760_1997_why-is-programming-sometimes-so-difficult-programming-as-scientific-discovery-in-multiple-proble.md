---
otero_id: 26760
otero_key: "6ZN46ZY7"
title: "Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces"
authors: "Jinwoo Kim; F. Javier Lerch"
year: "1997"
journal: "Information Systems Research"
doi: "10.1287/isre.8.1.25"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR Information Systems Research

![](/api/attachments/6ZN46ZY7/fulltext/images/2b69fbe2949638f158bad1d49ccb8c88b45fa32a276c81afb18406f7680a4b37.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces

Jinwoo Kim, F. Javier Lerch,

To cite this article:

Jinwoo Kim, F. Javier Lerch, (1997) Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces. Information Systems Research 8(1):25-50. http://dx.doi.org/10.1287/isre.8.1.25

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article's accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1997 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/6ZN46ZY7/fulltext/images/eb0b8c4152029233c51425bed42a6bd16f70b7e947f2fd56170f3650c9777486.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Why Is Programming (Sometimes) So Difficult? Programming as Scientific Discovery in Multiple Problem Spaces

Jinwoo Kim • F. Javier Lerch

Department of Business Administration, Yonsei University, Seoul, 120-749, Korea
jinwoo@bubble.yonsei.ac.kr

Graduate School of Industrial Administration, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213 lerch@andrew.cmu.edu

Our theoretical framework views programming as search in three problem spaces: rule, instance, and representation. The main objectives of this study are to find out how programmers change representation while working in multiple problem spaces, and how representation change increases the difficulty of programming tasks. Our theory of programming indicates that programming is similar to the way scientists discover and test theories. That is, programmers generate hypotheses in the rule space and test these hypotheses in the instance space. Moreover, programmers change their representations in the representation space when rule development becomes too difficult or alternative representations are available. We conducted three empirical studies with different programming tasks: writing a new program, understanding an existing program, and reusing an old program. Our results indicate that considerable cognitive difficulties stem from the need to change representations in these tasks. We conclude by discussing the implications of viewing programming as a scientific discovery for the design of programming environments and training methods.

(Empirical Studies of Programmers; Object-Oriented Programming; Scientific Discovery; Multiple Problem Spaces)

## 1. Introduction

Computer programming is a complex and difficult cognitive task (Simon 1973, Jeffries et al. 1981, Mayer 1981, Letovsky 1986, Guindon 1990). This research presents a theoretical view of programming based on well-established research in problem solving (Newell and Simon 1972), and recent work on Scientific Discovery (Simon and Lea 1977, Holland et al. 1986, Langley et al. 1987, Klahr and Dunbar 1988). Our theoretical view characterizes programming at the most basic level of cognitive research in problem solving, that is, as search in problem spaces. We present three studies that investigate different programming tasks under the same view. We expect that this integrated view will help us design better programming environments and training methods.

We regard programming as problem solving in three problem spaces: the rule space, the instance space, and the representation space. In our theoretical framework, programmers generate or refine programs in the rule space, and test these programs in the instance space. In addition, programmers may have to change their representations (i.e., search in the representation space) to lessen the cognitive difficulty of program generation and/or program testing in the other two spaces. This representational change is one of the reasons why programming is (sometimes) so difficult.

Our view of programming is similar to current cognitive theories of Scientific Discovery (Simon and Lea 1977, Langley et al. 1987, Klahr and Dunbar 1988, Klahr et al. 1993, Qin and Simon 1990). Prior studies in Scientific Discovery have investigated how people generate hypotheses (i.e., search in the rule space) and conduct tests (i.e., search in the instance space) to develop rule systems. A rule system is a well-defined set of propositions for predicting or explaining phenomena (Holland et al. 1986). Computer programs can be portrayed as rule systems for solving a set of task instances (Hoc and Nguyen-Xuan 1990), in the same way that rule systems in Scientific Discovery aim to explain a set of related test results (Klahr and Dunbar 1988). We have elaborated current theories of Scientific Discovery by adding the representation space, and by predicting that if search in this space is required, programming becomes more difficult. We used this framework to develop our experimental materials, to analyze verbal protocols, and to make suggestions for enhancing current programming practices.

The main objectives of the research are to find out how programmers change representation while working in multiple problem spaces, and how representation change increases the difficulty of programming tasks. These two objectives are addressed: 1) by presenting a cognitive theory of programming that adds the representation space to current theories of Scientific Discovery, 2) by testing this theory in three empirical studies, and 3) by suggesting improvements in current programming practices based on our proposed theory and the empirical results. The next section presents our theoretical framework of programming as search in three problem spaces. Section 3 outlines the structure of our three empirical studies, and presents the experimental materials and the coding system used for analyzing the verbal protocols. Sections 4, 5 and 6 present the empirical studies and the results. The last section discusses the implications of our empirical results and the implications of viewing programming as Scientific Discovery.

## 2. Programming as Scientific Discovery

This section introduces relevant studies in scientific discovery and explain our theoretical framework of programming as search in three problem spaces.

## 2.1. Scientific Discovery as Dual Space Search

Recent research in cognitive science has made substantial breakthroughs in understanding how humans develop and test rules. This research includes studies on concept attainment (e.g., Medin and Shoben 1988), confirmation bias (e.g., Klayman and Ha 1987), data collection processes (e.g., Faris and Revlin 1989), and data interpretation (e.g., Kuhn and Brannock 1987). In related research, Scientific Discovery studies have investigated the interrelation of two scientific processes: hypothesis generation and hypothesis testing (Simon and Lea 1977, Klahr and Dunbar 1988, Qin and Simon 1990, Klahr et al. 1993, Simon and Kulkarni 1989, Langley et al. 1987). For example, the Dual Space Search model of Scientific Discovery (Klahr and Dunbar 1988) integrates hypothesis generation and hypothesis testing based on an earlier model of rule development proposed by Simon and Lea (1977). According to the Dual Space Search model, scientists search two distinct problem spaces, a “hypothesis space” and an “test (experiment) space.” Search in the hypothesis space includes the generation and refinement of new hypotheses by using prior knowledge or prior test results. Search in the test space includes designing experiments to test hypotheses, running these experiments, and evaluating evidence.

Empirical results indicate that Scientific Discovery is conducted by interrelated searches in these two problem spaces. In Qin and Simon (1990), subjects were asked to discover the relationship between two sets of data used by Kepler to discover his third law of planetary motion (i.e., the cube of a planet's distance from the sun is proportional to the square of its period of revolution). Discovery processes of the subjects were compared against a computer model (BACON) that attempts to simulate discovery processes (see Langley et al. 1987). Both successful subjects and the BACON program were found to move systematically between the hypothesis space and the test space. These theoretical developments and empirical evidence show that the main difference between Scientific Discovery and many other problem-solving activities lies in the existence of the two problem spaces.

## 2.2. Programming as Search in Multiple Problem Spaces

This section presents in more detail the cognitive operators that programmers and scientists perform in each of the three problem spaces (rule, instance, and representation spaces) to develop rule systems (theories in the case of scientists, and programs in the case of programmers). In the rule (hypothesis) space, both scientists and programmers develop hypotheses for solving related phenomena. The two main operators in the rule space are Derive and Infer.

For the Derive operator, scientists transform existing rules, created for solving related problems, into the solution of their current problem (Holland et al. 1986, Dunbar 1993). For example, Coulomb derived his inverse-square laws of electrical forces by transforming Newton's laws of gravitational forces developed by Newton into his rules for electrical and magnetic forces (Langley et al. 1987). Similarly, many empirical studies in programming have reported that programmers cut and paste existing programs when solving new problems (Maiden and Sutcliffe 1992, Detienne 1991). A large number of studies have also shown how programmers retrieve programming schemas. For example, studies by Adelson and Soloway (1985) and Rist (1986) show that programmers retrieve general programming schemas from their long-term memory and modify these schemas when solving new problems.

For the Infer operator, scientists use solution instances to understand the problem and to generate or evaluate rules (Langley et al. 1987). For example, it is believed that Kepler used the instance of the planetary relation between Mercury and the sun to generate a general rule about the relation between the planets and the sun. Many empirical studies in programming have observed similar behaviors in both highly skilled professional programmers (Kim and Lerch 1992, Guindon et al. 1987) and novices (Jeffries et al. 1981). For example, in a study by Guindon et al. (1987), programmers started the programming process by building and traversing instances as an aid for getting insights about the problem as well as the rules for solving the problem.

Programmers also refine and evaluate the accuracy of existing rules (i.e., programs in progress) from test results in the instance space (i.e., the test space in Scientific Discovery). Kant and Newell (1984) found that programmers extensively use the information from running test cases (in the instance space) to verify and evaluate existing programs during program construction.

The main operator in the instance (test) space is called Mental simulation (Kant and Newell 1984). In Scientific Discovery, scientists design and conduct tests to falsify their current hypotheses. The results are instances (i.e., test results) that may support a hypothesis or cast doubts about the theory. Mental simulations in programming are used in several ways. Guindon et al. (1987) found that programmers use a strategy called “explorative mental simulation” which helps them generate new rules when they have no clue about how to start the programming process. Jeffries et al. (1981) proposed that designers use “problem solving by understanding” when they need to generate an initial rule. Mental simulations are also used to refine the content of existing rules by guiding the programmer during incremental changes. Adelson and Soloway (1985) found that programmers use mental simulation for “systematic expansion”—refining programs by using the results of running partial solutions. Finally, programmers rely heavily upon mental simulation for evaluating the validity of rules (Kant and Newell 1984). Detienne and Soloway (1990) found that their subjects used Mental simulations when they wanted to evaluate the external coherence among several specific programming plans that were derived from general program plans.

In addition to the rule and instance spaces that are already defined in Scientific Discovery, our theory adds one more problem space to the programming task—the representation space. A representation is a mental model that encodes the programmer's current understanding of the target problem (Letovsky 1986). Several prior studies in cognitive psychology and information systems have found that representations have a profound impact upon problem-solving processes (Hayes and Simon 1977a, Vessey 1991; Vessey and Galletta 1992). The representation space is the set of all possible representations for a given problem. In the same way programmers search for appropriate rules and instances in the rule and instance spaces, they can also search for appropriate representations in the representation space. We hypothesize two main operators in the representation space: Construct and Map. For the Construct operator, programmers work on a single representation, while for the Map operator, programmers work with multiple representations. Both Construct and Map manipulate components of the current representation in two different ways—filling-in empty slots or changing existing slots.

Filling-in empty slots is equivalent to the process of building initial representations. The empirical evidence shows that subjects build their representations component by component as they comprehend their problems (e.g., the UNDERSTAND model in Hayes and Simon (1977a). Representations provide the basic elements for building problem spaces: the initial state, the goal state, and the available operators to move from the initial state to the goal state in a given problem (Newell and Simon 1972). Therefore, an initial representation is required before programmers start performing any cognitive operation in the rule or the instance spaces. Although filling-in empty slots is an important process, our study focuses on how programmers change existing slots.

Changing existing slots is equivalent to the process of representation change. Representation change can be performed by either the Construct or the Map operator. We hypothesize that the Construct operator is triggered by impasses in the rule or instance spaces. An impasse occurs when a programmer stops making progress with the current representation. After an impasse has occurred, a programmer may build a new representation by modifying some of the components of the old representation. When changing representations, the Construct operator changes the problem spaces for the rule and instance spaces, allowing the programmer to resume progress in these spaces. We also hypothesize that the Map operator is triggered by the availability of alternative representations. Programmers change their representations with the Map operator by relating components from other available representations to their current representation. Programmers may decide to perform the Map operator when they find an opportunity for using solutions linked to other available representations.

The representation components manipulated by the Construct and Map operators are entities, relations and roles. Our empirical studies focus on how these three components are changed by the two operators (Construct and Map). We have selected Object-Oriented Programming (OOP) for our empirical studies because the three components of cognitive representations are mapped easily to elements of OO programs. This correspondence will help us identify more objectively the representation held by the subjects during the experiments. However, since programming methodologies have been found to influence cognitive representations (Boehm-Davis et al. 1992), the results of our empirical studies may not be applicable to other programming methodologies (e.g., structured programming) directly.

Entities have two basic characteristics—existence and state. An entity exists by itself, distinctly from other entities. The state of an entity encompasses the current values of all of the properties of the entity. Entities are implemented as objects in OOP and properties as attributes. Relations are physical or conceptual connections among entities (Gentner 1983). Relations can be characterized in terms of their cardinality and type. The cardinality of a relation may be one-to-one, one-to-many, or many-to-many (Rumbaugh et al. 1991, Booch 1994). Two important types of relations in OOP are inheritance (isa) and aggregation (is-part-of). These relations form default hierarchies in general rule systems along which the entities in a problem are organized (Holland et al. 1986). Roles are abstract descriptions of the behaviors of entities. A role describes how an entity acts and reacts, in terms of its state and relations to other entities. The characteristics of a role for a given entity are closely related to the other entities connected to this role, their states, and their relations to the given entity (Jacobson 1992). A role is also defined in OOP as “one end of a relation” (Rumbaugh et al. 1991, p. 34), and “a behavioral mask that an object wears” (Booch 1994, p. 90).

In a rule system, rules are clustered around entities, and there are relations between the entities, which form default hierarchies along which the entities are organized (Holland et al. 1986). Likewise, in OO programs, methods are clustered around objects, and there are associations among objects that form inheritance hierarchies around which the design objects are organized (Booch 1994). In this sense, OO programs can be viewed as sets of rules (i.e., methods) linked to entities (i.e., objects) for solving a set of related phenomena (i.e., transforming any valid inputs into desirable outputs).

The study of how representation components are changed has been an important topic in cognitive science, and has generated several empirical studies recently. For example, Kaplan and Simon (1990) showed subjects changing representations in an insight problem. Their performance depended on the availability of alternative representations in the representation space. However, no studies in the psychology of programming have investigated how programmers change representation. This lack of research is intriguing since a common piece of advice for writing complex programs or algorithms is to take a “fresh look” at the problem in order to exploit its characteristics.

## 3. Overview of Experiments

This section outlines the structure of our three empirical studies, and presents the experimental materials and the coding system used for analyzing the verbal protocols.

## 3.1. Focus of Experiments

The three experiments in this research investigate how programmers change representations and the consequences of representation change. In the three experiments, programmers engaged in three different tasks: writing a new program, understanding an existing program, and reusing an old program for solving a new problem. For each experiment, we have two groups of subjects: a Representation group and a Control group. The stimuli given to subjects in the Representation groups were expected to induce programmers to search in the representation space. On the other hand, the stimuli given to subjects in the Control groups were expected to let subjects work only in the rule space and/or the instance space. This design allows us to assess the increased difficulty of working in the representation space during programming tasks.

The first experiment covers the situation where programmers have to develop a new program from scratch. We asked subjects to write an OO program for a problem described on a single sheet of paper. In our analysis of this experiment, we focus on the cognitive process in the rule space because the subjects have to invent their programs. We also investigate how the activities in the rule space triggered representation change, as well as the consequences of representation change. In the second experiment, subjects were given a problem and a computer program that solves it. Subjects were asked to make sure the program was a solution to the problem. This experiment covers the situation where programmers are given a code that they have to understand for future tasks such as maintenance. Our focus in this study is on mental simulation in the instance space because mental simulations have been shown to drive program understanding (Pennington 1987). Program comprehension does not require the generation of rules in the rule space because the rules (i.e., programs) already exist. By working in the instance space, programmers run mental simulation to recognize the rules embedded in the existing program. This experiment investigates how Representation subjects change representations while working primarily in the instance space. Finally, in the third experiment, we gave subjects a new problem, and asked them to solve it by reusing an existing program. In this experiment, subjects were expected to Map between the representation of the new problem and the existing program, while interleaving cognitive operations in both the rule and instance spaces, because software reuse requires the understanding of the existing program (instance space), and the modification of the existing rules to solve the new problem (rule space).

## 3.2. Tower of Hanoi (TOH) Isomorphs

All three experiments in this research used two Tower of Hanoi (TOH) problem isomorphs: the monster change (MC) problem and the monster transfer (MT) problem (Hayes and Simon 1979b). Problem isomorphs are structurally the same problem but disguised by different wording (Hayes and Simon 1979a). The difference in wording induces different internal representations (Simon et al. 1985). The main reason for using the MC and MT problems is that we know the representations induced by them because they have been investigated extensively in problem-solving research (Hayes and Simon 1979a, 1979b). Therefore, we can manipulate the representations for the two experimental groups (Representation and Control groups) while controlling the difficulty of the underlying problem structure.

Both problems have monsters and globes of different sizes. In the MC problem, monsters Change (i.e., expand or shrink) their globe size, while in the MT problem, monsters Transfer globes of different sizes from one monster to another. Both problems have three problem constraints. These constraints have to be taken into account when generating rules for solving the two problems. For the MT problem, the constraints are: 1) only one monster can move its globe at a time, 2) if a monster has more than one globe, it can only move the largest of its globes, and 3) a monster cannot transfer a globe to other monsters that already have a larger globe. The MC problem has three isomorphic constraints: 1) only one globe may be changed at a time, 2) if two globes have the same size, only the globe held by the larger monster may be changed, and 3) a globe cannot be changed to the same size as the globe of a larger monster. The goal state for both isomorphs is that each monster gets a globe proportionate to its own size (e.g., small monster has small globe, etc.) without violating the three problem constraints. In this research we use four problem isomorphs: 3MC, 3MT, 5MC, and 5MT. The difference between the two problems with a 3 and the two problems with a 5 is the number of globes to be changed or transferred (the larger the number of globes, the harder the problem).

Figure 1 presents the initial internal representations induced by the two problems (Hayes and Simon 1979a, 1979b). These representations are built by subjects while reading the description of the problem (MC and MT). Hayes and Simon (1979a, 1979b) have shown that subjects build these representations by in a series of experiments. The representations for the two problems have the same entities (monsters and globes). Both representations share the same HAVE relation, but the cardinalities are different. In the MC problem, the HAVE relation is one-to-one, while this same relation is one-to-many for the MT problem. Both representations also share the NEXTSIZE relation that links monsters with each other in order of size. Finally, prior empirical work (Hayes and Simon 1979a, 1979b) has shown that the main role will be allocated to the monster entities for both representations. In the MC problem we expect monsters to be assigned the role of CHANGing the size of globes while in the MT problem we expect monsters to be assigned the role of TRANSFERring globes. In summary, these two representations have the same entities, but they differ in the nature of their relations and their roles. Therefore, the two representations generate different problem spaces (e.g., different initial states, different operators, etc.) and require different cognitive activities (Hayes and Simon 1979a, 1979b; Kim et al. 1995). We refer to the initial representation, induced by the MC problem shown in Figure 1 as the CHANGE representation, and the representation induced by the MT problem as the TRANSFER representation.

Figure 1 Initial Internal Representations for the MC and MT Problems

<table><tr><td>Problems</td><td>Monster Change (MC)</td><td>Monster Transfer (MT)</td></tr><tr><td>Entities</td><td>monsters, globes</td><td>monsters, globes</td></tr><tr><td>Relations</td><td>HAVE (monster, globe)NEXTSIZE (monster, monster)</td><td>HAVE (monster, globes)NEXTSIZE (monster, monster)</td></tr><tr><td>Main Role</td><td>CHANGING (monsters, globe-size)</td><td>TRANSFERRING (monsters, globe)</td></tr></table>

## 3.3. OO Programs for the TOH Isomorphs

A general OO program for the isomorphs should be able to solve any initial arrangements of monsters and globes. The 3MC and 3MT problems have 27 possible initial arrangements of monsters and globes, and the 5MC and 5MT have 243. A general solution for the Tower of Hanoi (TOH) requires two main programming constructs (Anzai and Simon 1979, VanLehn 1989): recursion and the specification of necessary/sufficient conditions. Appendix 1 presents an OO program that uses these two constructs for solving the 3MC problem. Recursion is used in the changeGlobeSize method (temp → changeGlobeSize (remainingSize)). In order to change the size of the small monster's globe, we need to change the size of the medium monster's globe. In order to change the size of the medium monster's globe, we need to change the size of the large monster's globe recursively, and so on. Necessary/sufficient conditions relate to the destination of the blocking objects. For example, suppose that in the MC problem you want to change the globe size of the small monster to small but you cannot do that because the medium monster has the small globe. In this case, you need to decide the size to which you are going to change the medium monster's globe (which is blocking the desired change of the small monster's globe size). The necessary/sufficient condition is a general concept that means whenever you cannot change the current state of an object to the desired state because of a blocking object, change the state of the blocking object to neither the current state nor the desired state of the current object. The Necessary/Sufficient condition is used in the getRemainingSize method in Appendix 1.

Rules (i.e., programs) with recursion are the most general strategy for the TOH problem. They can solve any instance of the TOH problem and are easily extensible for any number of globes. The Necessary/Sufficient condition is also a very general concept that is applicable to all possible cases. However, these two programming constructs are not often used in everyday problem solving and have been found very difficult to learn and to execute correctly in programming (Pirolli 1986). Therefore, even though the TOH is a small problem, writing a program to solve this problem is not a simple task. It is especially complex if the programmer has the “wrong” representation. For example, it is very difficult to write a program having the initial representation induced by the MT problem (TRANSFER representation) because of the need for additional recursive structures to take care of the one-to-many HAVE relation (see Kim et al. 1995) for more details). In order to write a program for solving the MT problem that is as general as the program for the MC problem in Appendix 1, programmers need to change their initial representation. Figure 2 shows this representation change. Programmers need to change the HAVE relation from monsters having globes to globes having owner-Monsters (i.e., monsters that own the globes). Subjects also need to change the entities for the NEXTSIZE relation from monsters to globes. Finally, subjects should change the role from TRANSFERring globes to CHANGing the size of the ownerMonster (Monster-size in Figure 2). We called this new representation the CHANGE representation for the MT problem. The OO program based on the CHANGE representation for the MT problem is presented in Appendix 2. Since the MC and MT problems are isomorphs, the program in Appendix 2 is equivalent to the program in Appendix 1 except for the labels. For example, every instance of globe in one of the programs is an instance of monster in the other and vice versa.

In summary, the MC problem does not require a representation change when writing a program. Subjects are expected to develop rules and run mental simulations using the initial representation (CHANGE representation) induced by this problem. On the other hand, the representation induced by the MT problem (TRANSFER representation) is expected to make programming tasks very difficult. Therefore, we expect subjects to change their representations. The Representation groups were assigned the MT problems (3MT for the first and second experiments, 5MT for the third experiment), because the initial representation of these problems (the TRANSFER representation) is expected to force representational change. For the Control groups, we used the MC problems (3MC for the first and second experiments, 5MC for the third experiment), because the initial representation of these problems (the CHANGE representation) is not expected to require representational change.

Figure 2 Initial (TRANSFER) Representation and Alternative (CHANGE) Representation for the MT Problem  
![](/api/attachments/6ZN46ZY7/fulltext/images/572355bd305fb1bb2d08a5da2ba1fdb2ca38b0b9ccd34509e463b726448263c9.jpg)

## 3.4. Development of Coding Schema

We used protocol analysis (Ericsson and Simon 1993) to compare the cognitive activities in the three problem spaces between the two groups. Verbal utterances during problem solving are the major source of data for the three studies. Along with verbal protocols, written program protocols were also collected, since the use of both verbal and program protocols is expected to provide a more complete trace of problem-solving behavior (Rist 1989).

Two important preconditions for using protocol analysis are to identify an appropriate unit of analysis, and to develop an objective coding system for each unit. The coding system should not be skewed to some specific features of a certain group in the experiment. We elected to use episode as our unit of analysis considering the volume of data in our study. Episodes are small self-contained phases of highly organized activity (Newell and Simon 1972). A preliminary study was conducted to develop an objective coding system for subjects' protocols. Five expert Object-Oriented designers participated in the preliminary study. All of them had advanced degrees in computer science (3 Ph.D. and 2 MSc), and had worked as full-time software designers for more than 10 years. We asked these experts to write a computer program for two of the four problem isomorphs used in this study (3MC and 5MC). They spent 3 to 5 hours writing and debugging OO programs for these two problems.

We used an iterative procedure to develop the coding system. Several successive approximations were applied to the whole protocol of the five subjects until the coding system became stable, and we were able to code the majority of verbal utterances without difficulty. The simplified coding system for the important categories is shown in Figure 3 (see Kim (1993) for the complete coding system and the details of its development).

Episodes were classified as Construct if activities in the episode were related to building or changing one of the three components of the representation. For example, assigning a property to an entity (e.g., globe-size for a monster entity) is classified as Construct. Also, if subjects implement associations between objects using pointers, this activity would be coded as Construct. The first slot of the coding schema for the Construct operator, as shown in Figure 3, is the Construct number. The second slot consists of protocols that show the serial number of the transcribed protocol and the elapsed time. Next, the "Representation" slot has three sub-slots: entities, relations and roles. Finally, the "Logs" slot is used to keep track of keywords and their timing. We predefined two sets of keywords that were expected to be used by subjects when they have either the CHANGE or the TRANSFER representation. For example, "move" and "transfer" were identified as TRANSFER keywords, while "change" and "change-owner-monster" were identified as CHANGE keywords.

Episodes were classified as Map if subjects attempt to relate more than one representation. In order to be classified as Map, episodes should include: 1) verbal utterances describing at least two different representations, and 2) an indication that subjects are attempting to relate them in the representation space. For example, subjects may explicitly state that a specific element in one problem was equivalent to another element in the other problem. Figure 3 shows the schema for the Map operator. The first two slots are again for record keeping. The "Representations" slot shows the elements (i.e., entities, relations, and roles) of multiple representations (usually two). These sub-slots were coded using the same predefined sets of keywords that were used for coding the Construct episode.

Figure 3 Simplified Coding Schema for Construct, Map, Rule, and Mental Simulation  
![](/api/attachments/6ZN46ZY7/fulltext/images/73ad71651aed6cdc635c1b827644738466fed76b56fae942201e4bf984496731.jpg)

Episodes were classified as Rule, if subjects create or modify any systematic piece of problem-solving strategies that direct search in the problem space. In order to be regarded as a rule, the strategies should be able to compute the next move or at least direct the search to reach to the goal state (i.e., three monsters get a globe proportionate to their own sizes). The “Cognitive operation” slot may have either Infer or Derive. A cognition operation slot is classified as Infer, if subjects develop a new rule by using information from mental simulations executed in the instance space. Otherwise, it is classified as Derive if subjects did not use any information directly from the instance space, but used only prior rules in the rule space. Since the Infer operation uses knowledge in the instance space that has been obtained through mental simulations, the “Reference” slot has a mental simulation number. Accordingly, the Derive operation has a related rule number in the slot. The Rule schema also has the “Representation” slot with three sub-slots as shown in Figure 3. The “Representation” slot displays the internal representation that subjects have while they are developing the current rule. Rules are not part of the representation space and internal representation should have been detected by Construct or Map. However, we have observed that representation changes were often made without clear indication during the activities in the representation space. Therefore, we decided to show subjects’ representations when they have developed rules and to display the information in the Rule episode as well as in the Construct and Map episodes. Finally, the Rule coding schema has a “Contents” slot that represents the actual rules developed through the Rule operation.

Mental simulations represent the actual traversing of a solution path in the instance space. In order to be regarded as a mental simulation, there should be at least one comment about the solution that is being traced. It does not matter whether the subject actually uses paper and pencil. Subjects can verbally specify the dynamic change of the problem states in a given situation (e.g., I am moving the small globe to the . . .) or write/draw the next state. In that sense, the adjective “mental” is a little misleading. But we will continue using this term to comply with current terminology in programming and design. The coding schema for the mental simulation is similar to the schemas for the Rule operation, except that it does not have the developed rule slot. Instead, it has a “Simulation steps” slot that shows the input, interim process, and final output of the simulation. The “Keyword Logs” slot serves the same function as the “Logs” slot in the Construct schema. Examples for each coding schema will be presented in the results sections.

## 3.5. Process of Protocol Analysis

For each experiment we decided to conduct the data analysis step by step across all the subjects to increase reliability. The steps were: transcription, verification of transcription, initial segmentation, segmentation test, episode coding, test for episode coding, and construction of Problem Behavior Graphs. For the protocols, a certain step was finished before the next step was started for any subject. First, all the verbal protocols were transcribed with time marks and written program comments (Rist 1989). Next, all the transcriptions were verified by the first author before segmentation. Then, all the written transcripts were initially segmented into episodes, while keeping track of the elapsed time. Segmentation is driven by a segmentation rule that is based on the types of episodes described in the coding system. After all the protocols were initially segmented, a sample of the initial segmentation was examined by the second author. In the examination, a few ambiguities in the segmentation rule were identified. We revised our segmentation rule and applied it again to the entire set of protocols. Then, the segmented episodes were coded using the coding system. A few episodes could not be coded with the current coding system, so those were reanalyzed after all the protocols were coded. Since the time spent by the subjects in these episodes was negligible in all the experiments (less than 1 percent of the total time), we decided to omit those episodes from further analysis. Then, the attribute values for the representation slots (entities, relations and roles in each of the four types of episodes) were examined by the second author. The representation attributes were selected because this research focuses on representation and representation change. In the examination, a few ambiguities in the coding rule were identified. We revised our coding rule and applied it again to the entire set of protocols. Finally, three Problem Behavior Graphs (PBGs) were built for each subject based on protocol data. A PBG portrays problem-solving activities as a series of searches in the problem space (Newell and Simon 1972). Three PBGs were built for each subject because each subject has potentially three problem spaces (Rule Behavior Graph in the rule space, Simulation Behavior Graph in the instance space, and Representation Behavior Graph in the representation space).

We coded all subjects' verbal protocols for both the Representation and Control groups using the coding scheme. Although the analysis of the verbal and program protocols most accurately shows the dynamic nature of search in the three problem spaces, it is impossible to present all these data in detail for all the subjects because of the large amount of data. Therefore, for each experiment, we decided to present the analysis of one subject in the Representation group in detail, because our focus is on representation change. This subject in each experiment was selected because his/her cognitive processes were relatively simple and representative of the behavior of the group. After analyzing one subject's behavior in detail, we then compared the aggregate protocol results between the two groups. Finally, we provided a brief description of the final output: written programs and execution time.

## 3.6. Subjects

Students participated in the experiments for course credit. All subjects were senior undergraduate students in the Math/Computer Science program at Carnegie Mellon University, and were enrolled in a software engineering course that utilized an Object-Oriented design methodology (Rumbaugh et al. 1991). The software engineering class required our subjects to do a course project that developed a real world OO program that consisted of 125 classes and more than 27,000 lines of codes. Our experiments were conducted at the end of their semester-long class, by which time our subjects had done several homework assignments in C++, and had almost finished their course project. All the subjects had taken at least four courses in programming and computer science, but none of them were familiar with the Monster isomorphs.

## 4. First Study (Programming from Scratch)

This section presents the first empirical study in which subjects were asked to write a new program from scratch.

## 4.1. Experimental Design and Procedure

Eight subjects were randomly assigned to either the 3MC problem (MC group) or to the 3MT problem (MT group). Subjects were asked to write a C++ program that would convert any initial arrangement of monsters and globes to the final state. No solution programs were provided. Here, the MT group is the Representation group because subjects in this group were expected to change their initial representation to develop general rules (i.e., with recursion and sufficient/necessary conditions) for solving the problem. The MC group is the Control group because we expected them to use their initial representation for developing the program. All eight subjects succeeded, within a 4-hour time limit in developing a correct C++ program that was both executable and solved the problem.

## 4.2. Detailed Analysis for One Subject in the Representation Group

MT4 (a Representation subject) spent 181 minutes to generate his final solution program. The Rule Behavior Graph (RBG) in Figure 4 shows his search process in the rule space. Each square represents a rule episode. The capital letters in the squares represent the cognitive operation used to develop the rule (either Infer or Derive). For example, the subject (MT4) first generated RU1 (RU1 stands for RUle #1) using the Derive operation (D) by reading the problem description and extracting some principles in the problem description and converting them into an abstract rule. Then RU1 was refined into RU2, again by the Derive (D) operation. Since these first two transitions were performed with the Derive operation, no mental simulations were used during the generation or the refinement of the rules. The numbers inside the squares represent the elapsed time for the rule episodes in seconds. For example, MT4 spent 349 seconds in the development of RU10. The RBG proceeds from left to right. Backtracking to an earlier rule is represented by moving left to the earlier rule and down one level. For example, after the subject developed RU9, he nullified all the rules developed between RU4 to RU9, and backtracked to RU3. This segment is an important part of MT4's process, because he strategically modified his representation in this segment of the graph, and also backtracked several steps at once. Figure 5 presents a more detailed analysis of the activities surrounding this switch by showing activities in the representation and rule problem spaces at once.

Figure 4 Rule Behavior Graph (RBG) for MT4  
![](/api/attachments/6ZN46ZY7/fulltext/images/18bdebe60b2bcdba392c8fa2f90efbe6c44e4ecbf920a2578117123b36787e4a.jpg)

Figure 5 Activities in the Rule Problem Spaces Surrounding the Representation Change  
![](/api/attachments/6ZN46ZY7/fulltext/images/0eec67ae3337fdde0cd6a008986cc69b557e0fa991847914bd3cfd265b211fc1.jpg)

Figure 5 shows that after the subject finished building RU9, he ran into an impasse. His protocol explicitly stated that the problem is not solvable ("No, wait, oh, I'm, wait, hold on again, I'm really \*\* not sure there is a solution to this"). After he spent 210 seconds without any progress, he expressed his frustration by rephrasing his prior statement ("But the problem is you can never remove globe, you can never remove Globe One off of Monster Three. This problem is unsolvable."). Afterwards, he was reassured by the experimenter that the problem was solvable. Then he changed the representation from RE1.23 (RE1.23 stands for Representation #1.23) to RE2.0 (from the TRANSFER representation to an unexpected representation). These two representations were encoded in the representation slots of RU9 and RU10. There are no Construct or Map episodes in Figure 5 because there was no explicit search in the representation space during representation change (no verbal protocol), although the subject changed the representation in the rules embedded in the program. RE2.0 is fundamentally different from all prior representations (representations in RU1–RU9) because the subject created an artificial object (superMonster), and assigned all the important roles to this superMonster. With the new representation, he came up with a new rule (RU10) based on the new representation. Figure 6 shows the filled-in Rule schemas for RU9 and RU10 that show the representation change.

The subject spent 114 seconds in rule episode 9, deriving a rule (RU9) that was based on a rule (RU6) developed earlier. The Representation slots show that he had only monsters and globes as entities: A monster has several globes and there is a next-size monster for each monster. Monsters were allocated all the important roles. Each monster decided which globe it was going to move, actually transferred the globe, and told other monsters which globe it had. Therefore, the representation is very similar to what we have expected in Figure 1 (TRANSFER representation). Using this representation, by the end of the RU9, the subject had developed the rule shown in the content slot. This rule was the general rule for the small monster: If the small monster does not have the small globe (line 03), find the monster that has it, and find a temporary monster that has a globe that is smaller than the small monster's globe. The small monster transfers its globe to the temporary monster, and the monster that has the small globe transfers it to the small monster.

The subject spent 352 seconds in building RU10. In this rule episode he created a new entity (super-monster) that was not given in the problem description. He also established two new relations between the super-monster and other existing entities so that the super-monster HAS monsters and globes. More importantly, he moved the role of deciding the next move from the individual monsters to the super-monster. He further decomposed the problem based on several attributes of the super-monster. He first decomposed upon the globe size of the small monster (line 01 and line 06 in the content slot of Figure 6). He further decomposed based upon the globe size of the medium monster (lines 02, 04, 07, and 12). The final program generated by the subject was similar to RU10 with minor refinements made later in other rule episodes.

In summary, the subject started with the representation shown in Figure 1 (the TRANSFER representation). Prior to RU10, the individual monsters were allocated the role of transferring globes to their destination. After experiencing cognitive difficulties in rule development under this representation (an impasse as shown in the protocol), he changed his representation from RE1.23 to RE 2.0. In RE 2.0, the super-monster gained the role of transferring globes, and the problem was decomposed into several cases based upon the value of the attributes

Rule Number: 9
Protocols: p781-789 (114 seconds)
Cognitive Operation: Derive
Reference: (R6)
Representation
Entities: monsters, globes
Relations: HAVE (monster, several globes), NEXTSIZE (monster, monster)
Role: DECIDE (monster, transfer), TRANSFER (monster, globe), INFORM (monster, globe-size)

Figure 6 An Example of the Rule Schema for RU9 and RU10  
```txt
Rule Number: 10
Protocols: p866-877 (349 seconds)
Cognitive Operation: Infer
Reference: (MS10)
Representation
    Entities: Super-monster, monsters, globes
    Relations: HAVE (Super-monster, monsters),
    HAVE (Super-monster, globes),
    HAVE (monsters, globes),
    NEXTSIZE (monster, monster)
    Roles: DECIDE (Super-monster, transfer)
    TRANSFER (monster, globe)
    INFORM (monster, has-globe)
Contents (R10)
01 If (monster1 → globe-getSize () == 3) {
02    If (temp1-hasGlobe(2)) {
03    monster1-transfer (temp1, monster1→globes)
04    }Else{
05    monster1-transfer (temp2, monster1→globes)
06    Else {
07    If (temp1-hasGlobe(3)) {
08    temp1-transfer (temp2, temp1→globes)
09    monster1-transfer(temp1, monster1→globes)
10    temp2-transfer(temp1, temp2-getGlobe(3))
11    temp2-transfer (monster1, temp2→globes)
12    }Else{
13    monster1-transfer (temp1, monster1→globes)
14    temp2-transfer (monster1, temp2→globes)
15    }}
```

Figure 7 Subjects' Impasses in the Representation Group

<table><tr><td>MT1</td><td>“OK, so, if I give the large, the small, for the small to give the Small, its globe to large monster. The small monster, the large monster cannot get rid of it,* the Small globe. (E:Yeah.) But the small monster, the large monster can never get rid of the Small globe. *(E: There is a way. Some people ask me during this process that, this is an unsolvable problem like you think. This is solvable.)</td></tr><tr><td>MT2</td><td>“And then,* medium grabs the Medium, and the small grabs the Small. (E: Can you do that?) Yes. *** Oh, only the largest may be transferred. OK. I didn’t see that. OK. * So then you would take. ** Oh, OK, but it, it would just mean, you just reverse the order of calling it. You would just take the largest globe. (E: And?) Okay, in this case it wouldn’t work because the largest globe is here. ** Sooo. **</td></tr><tr><td>MT4</td><td>“No, wait, oh, I’m, wait, hold on again, I’m really ** not sure there is a solution to this. *(E: There is a solution) Well, ** take a look. **”</td></tr><tr><td>MT6</td><td>“Umm, *** hmm, ***** two and a half hours. ***** Let’s see, ***** I’m sure, I’m doing this wrong. There’s gotta be an algorithm for it. Hmm, ** hmm, *** let’s see, ***** hmm, ***** OK, * umm, ***** hmm, *** let’s see. ***** I’m probably missing something really obvious here. ***** What are we gonna do? OK, *** let’s see, ** hmm, ***** umm, ***** OK, we’re thinking too difficulty I think. ***** Uuumm, ** OK, ** let’s start all over again. *** We have the globes. ****</td></tr></table>

of the super-monster (e.g. the globe size of the small monster, the globe size of the medium monster).

## 4.3. Aggregate Protocol Analysis

We coded 992 episodes for all eight subjects in the four schema categories with an average time of 66.6 seconds per episode, for a total of 18.3 hours of analyzed protocols. Of the 992 episodes, 249 are Rule episodes, 243 are mental simulations, and 248 are Construct episodes. No Map episodes were found in this experiment. Subjects spent 43.3% of their time in the rule space, for an average of 59.6 minutes per subject. (Rule episodes had an average elapsed time of 114 seconds each). Subjects spent 25.2% of their time performing mental simulations, for an average of 34.7 minutes per subject (mental simulation episodes had an average elapsed time of 68 seconds). They also spent 21.7% of their time filling-in the representation components with the Construct operator. The rest of their time was spent in reading the problem description (96 episodes, 2.8%) and in others (156 episodes, 6.9%) which included interactions between the experimenter and the subject, and meta-statements.

All Representation subjects (MT group) followed similar cognitive processes: they first attempted to develop rules using the TRANSFER representation, and then all of them reached an impasse. Figure 7 shows the verbal utterances for the four Representation subjects when they encountered impasses.

All chose the same strategy when facing an impasse in their rule development process: to change their representation. All of them created a new central object. A central object is an artificial object that was not given in the problem description. They established a relation from the central object to monsters and globes so that the central object had monsters and globes. And finally they assigned all the important roles to the central object. Now, the central object knows all the sizes of monsters and globes, and has all the important roles: getting the small globe to the small monster, medium globe to the medium monster, and large globe to the large monster. The monsters and globes objects become just data repositories with simple roles of reporting and updating their own attributes.

Since the Representation subjects assigned all the important roles to the central object, the behaviors of the central object became complex. Accordingly, the prescription for the behaviors (rules) of the central object has become more complex. Actually, to develop a set of rules for the central object is essentially the same as to solve the whole problem. Therefore, the Representation subjects needed further decomposition when they tried to develop a set of rules for the central object. All of them decomposed the rules of the central object on the basis of values of attributes of the central object rather than on the basis of objects. The most frequently used attributes were the initial location of the three globes (38%), followed by the initial location of the small globe (24.8%).

In contrast, the four Control subjects did not change their initial representation. They started with the CHANGE representation and developed rules and ran mental simulations under this representation until the end. They exhibited the behavior observed in Scientific Discovery experiments: they moved systematically from the rule to the instance space to run mental simulations for testing rules or inferring new rules, and then back to the rule space. None of them created a central object.

Since the Representation subjects changed their representation in the middle of rule development, they had to change their activities in the rule space according to their representation change. Figure 8 displays the percentages of rule episodes using either the Infer or the Derive operation. The percentages of time for the two cognitive operations are calculated for both the Representation group and the Control group. The Representation group data are divided into two sections: stage-1 (before representation change to central object), and stage-2 (after representation change).

Figure 8 Percentages of Rule Episodes Using the Infer or the Derive Cognitive Operations

<table><tr><td rowspan="2"></td><td colspan="3">Percentage of Derive</td><td colspan="3">Percentage of Infer</td></tr><tr><td>Entire Episode</td><td>Stage 1</td><td>Stage 2</td><td>Entire Episode</td><td>Stage 1</td><td>Stage 2</td></tr><tr><td>Control GROUP</td><td>74%</td><td>NA</td><td>NA</td><td>26%</td><td>NA</td><td>NA</td></tr><tr><td>Representation GROUP</td><td>67%</td><td>79%</td><td>44%</td><td>33%</td><td>21%</td><td>56%</td></tr></table>

If we compare the Control and Representation groups in total, they do not differ much. The Control group spent 26% of its rule episodes using the Infer operation, while the Representation group spent 33% using the Infer operation. However, when we broke down each episode of the Representation subjects into stage-1 and stage-2, the two groups' behaviors turned out to be very different. The usage of cognitive operations in the rule space for the Control group and stage-1 of the Representation group were again fairly similar to each other. Their rule development was driven mostly by the Derive operation (Control, 74%; stage-1 of Representation, 79%) and a smaller portion of rules were developed by the Infer operation (Control, 26%; stage-1 of Representation, 21%). This is because both groups tried to develop general rules for individual monsters, which required recursion and necessary/sufficient conditions. Since both groups were developing these general rules, they became less dependent on activities in the instance space. On the other hand, the usage of cognitive operations in stage-2 of the Representation group is quite different from patterns in stage-1 of the Representation group and for Control subjects. The Representation subjects in stage-2 were more driven by the Infer (56%) than by the Derive (44%) operation. The Infer operation began to play a more significant role because the rules of the central object were decomposed into specific cases based upon the values of attributes. The designers needed to work in the instance space either to generate or specify case-specific rules. Therefore, the Representation subjects changed their cognitive operations in the rule space according to the changes in the representation space. No such adaptation was observed in the rule space activities of the Control group.

In summary, the Representation group changed their representations from the initial TRANSFER representation to an unexpected representation with a central object. This change resulted in different activities for the two groups in the rule space.

## 4.4. Final Output

The representation of the problem and the nature of rule activities after the change of representation determined the characteristics of the programs written by the two groups. Representation (MT) subjects' final rules (i.e., programs) are only good for solving the 3MT problem because the rules for the central object had to be decomposed for attribute values. Therefore, individual rules can only deal with a very specific set of cases determined by these attribute values. For example, the programs needed to be rewritten from scratch in order to solve the 5MT problem. On the other hand, all Control (MC) subjects developed a general OO program similar to that in Appendix 1. These programs can solve any TOH isomorph because they include recursion and necessary/sufficient condition constructs.

In principle, there are numerous possible changes to the initial representation for the MT problem, but interestingly enough, all the Representation subjects chose to create a central object. Alternatively, the Representation subjects could have chosen the CHANGE representation shown in Figure 2. This alternative representation would allow Representation subjects develop a similar final program as the Control subjects. However, to develop this alternative representation, they needed to modify all the relations and roles of their initial representation. This may be the reason why none of our Representation subjects created the CHANGE representation for the MT problem (with a TRANSFER representation). On the other hand, the representation with the central object preserved most of their initial representation. However, this representation resulted in subjects generating inferior code that is not reusable. In the second experiment, we investigated what happened if we gave the alternative CHANGE representation for the MT problem to the subjects instead of asking them to create it.

## 5. Second Study (Program Understanding)

This section presents the second empirical study in which subjects were asked to understand a given program developed by somebody else.

## 5.1. Subjects

Twenty-four subjects were randomly assigned to either the Representation group or the Control group. The subjects were senior undergraduate students with the same qualifications described in the first study. None of the subjects from the first study participated in this experiment.

## 5.2. Experimental Design and Procedure

Subjects were asked to understand how a computer program solves a problem. They were told that they would be tested on their knowledge of the program. After the subjects stated that they understood the program, they were asked to walk through the program with two test cases. At the end of the experiment, they were asked to answer several comprehension questions. All subjects finished running the two test cases and all subjects answered the questions in a satisfactory way (see Kim (1993) for details).

The Representation subjects were again given the 3MT problem that induces the TRANSFER representation. They were also given the computer program for solving this problem with the CHANGE representation as shown in Appendix 2. Representation subjects were expected to work in the representation space to reconcile the two different representations. The Control subjects were again given the 3MC problem and the program with the CHANGE representation shown in Appendix 1. Consequently, Control subjects were not expected to work in the representation space because both program and problem share the same CHANGE representation.

## 5.3. Detailed Analysis for One Subject in the Representation Group

Subject MT6 spent 70 minutes (4223 seconds) comprehending the program running 10 mental simulations. Figure 9 shows the 10 simulations in a Problem Behavior Graph in the instance space (Simulation Behavior Graph).

Each square in Figure 9 represents a mental simulation episode. The information inside the first parenthesis signifies the inputs to the mental simulation. The notation $(x1, x2, x3)$ refers to the globes in the small monster $(x1)$ , globes in the medium monster $(x2)$ , and globes in the large monster $(x3)$ . For example, $(-, 3, 12)$ in MS4 means that the small monster has no globe $(-)$ , the medium monster has the large globe $(3)$ , and the large monster has the small and the medium globes $(12)$ . The asterisk is a wild card. For example, $(*, *, *)$ in MS1 means that the position of the globes in the monsters is not specified. Similarly, $(*, 1, *)$ in MS2 means that the medium monster has the small globe while the other two globes can be held by any of the three monsters. In each case, the greater the number of asterisks, the more general the simulation is.

Figure 9 Simulation Behavior Graph in the Instance Space for MT6  
![](/api/attachments/6ZN46ZY7/fulltext/images/44fa1b3b2003a1a177bd3aa377a64d9c70dcaa1d6cd05ef0bedb8fb219148fb0.jpg)

For this study we kept a record of the representation keywords uttered by each subject in each mental simulation episode. The number of keywords is a coarse (but objective) indicator of the representation held by the subject during the mental simulation. In the second parenthesis, the letter C stands for CHANGE representation while T stands for TRANSFER representation; the proceeding number equals the number of representation keywords verbalized by the subject. For example, in MS1 this subject mentioned 18 CHANGE keywords.

The subject started with MS1, the most general simulation with all globes as variables. Then he came up with a more specific instance in MS2 where the small globe was in the medium monster. He then went back to the most general case in MS3. Figure 10 shows three examples of filled-in mental simulation schema for MT6.

MT6 spent 183 seconds running MS3. In mental simulation MS3, the subject moved the small globe in the medium monster to the small monster. While he was conducting this step, he spoke nine keywords, all of which were classified as CHANGE keywords. For example, at 41 minutes and 44 seconds (00:41:44), he stated, “... want to change ...”. The keywords show that the subject held only the CHANGE representation during the execution of this mental simulation [C(9)]. However, in the next simulation (MS4), the Keywords Logs shows that the subject mingled keywords for the

Figure 10 Three Examples of Mental Simulation Schema for MS6

Mental Simulation Number: 3
Protocols: p4120-4343 (183 seconds)
Simulation Steps: (\*,1,\*)→(1,\*,\*)
Keywords Logs: C(9)
C(41:44), C(41:57), C(42.00), C(42:22), C(42.44), C(42:46), C(42:48), C(43:00), C(43:16)

Representations:
Entities: monsters, globes
Relations: HAVE (globes, owner monsters),
NEXTSIZE (globe, globe)
Roles: CHANGE (globe, monster size)

C(43.51), T(43:54), T(43.56), T(44.01), C(44:10), T(44·11), T(44:15), C(44·35), C(44:40), C(44·55), T(44:58), T(44:59), T(45:00), C(45.04), C(45:21), T(45:24), C(45·30), C(45·54), C(46:09), C(46:16), C(46:52), T(47:02), C(47·48), C(48:00), T(48:21), T(48·41), T(48:44), T(49:02), C(49:18), T(49:22), C(49:30), C(49.33), C(49:37), T(49:56), C(50.09), C(50.37), C(50:42), C(50:45), T(50:49), C(50·59), T(51·02), T(51:05), C(51:08), T(51:41), T(51.44), C(51:53), C(52:26), C(52.42)
Representations:

![](/api/attachments/6ZN46ZY7/fulltext/images/79e0441c509a25fdb365a6691068eee8b4da037c7016829aaceed4a93830a774.jpg)

T(34:50), T(34:57), T(35:11), T(35:28), T(35:40), T(35:43), T(35:45), T(35:52), T(36:01), T(36:22), T(36:30), T(36:33), T(36:39), T(36:42), T(36:44), T(36:50), T(36:53), T(36:57), T(37:01), T(37:28), T(37:33), T(37:35), T(37:50), T(37:53), T(37:57), T(38:01), T(38:05)

Entities: monsters, globes

CHANGE and TRANSFER representations. For example, at (00:43:51), he said, “... want to change ...”; however, three seconds later he said, “... move ...” which is classified as a TRANSFER keyword. After that he said, “... have to move ...” and “... transfer ...”, then “... like to change ...”. In total, he uttered 27 CHANGE and 21 TRANSFER keywords. Finally, in the second to the last mental simulation (MS9), his utterances were all TRANSFER keywords [T(27)].

It is interesting to note that the subject used only the CHANGE representation in the early mental simulations (MS1, MS2, and MS3). Then he ran several mental simulations with both representations (MS4, MS5, and MS6). Finally, towards the end, he ran mental simulations only with the TRANSFER representation (MS7 to MS10). So, he started with the representation in the solution program (CHANGE representation), and gradually changed his representation to the representation in the problem description. This systematic search in the instance space seemed to help him comprehend the way in which the computer program with the CHANGE representation solved the problem with the TRANSFER representation. Again, the coding does not include Construct or Map episodes in the representation space because the protocol does not have explicit searches in this space (no verbal protocols). But the values of the representation slots in the mental simulation reflect the implicit change.

## 5.4. Aggregate Protocol Results

We coded 174 mental simulation episodes for all twenty-four subjects with an average time of 406.1 seconds per episode, for a total of 19.6 hours of analyzed protocols. For the Representation group we divided each verbal protocol evenly into ten time intervals, and counted the number of keywords for each representation in each protocol interval. Our purpose was to observe the change through time of the frequency of TRANSFER and CHANGE keywords for all subjects, by adjusting for uneven times spent on program comprehension by different subjects. Figure 11 shows the percentage of TRANSFER keywords (the representation of the problem) in each time interval, combined for all Representation subjects. For example, if there are 7 incidents of keywords for the TRANSFER representation, and 3 incidents of keywords for the CHANGE representation in a given time interval, the percentage of TRANSFER keywords for that period becomes 70%.

These results indicate that Representation subjects behaved similarly as a group to subject MT6. They initially used the CHANGE representation from the

Percentage of the TRANSFER keyword occurrences by Representation subjects

Figure 11 Normalized Percentage of TRANSFER Keywords by Representation Subjects  
![](/api/attachments/6ZN46ZY7/fulltext/images/7f5e39ac14fc66c2d50930d0db6286a187245053a94218bf736666765809f17f.jpg)

solution program. Then they gradually migrated to the TRANSFER representation given in the problem description. Subjects usually ran their first mental simulation with only the CHANGE representation, then they held both representations simultaneously as time progressed. The last mental simulation was run mainly with the TRANSFER representation. Therefore, they gradually changed their representation, while they were running mental simulations in the instance space. In contrast, Control subjects did not change their initial representation during the entire experiment. They started with the CHANGE representation, and maintained this representation during every mental simulation.

Representation subjects ran more mental simulations with specific instances (e.g., $(-, 3, 12)$ ) than simulations with a general instance. General simulations are those in which at least one input is a wild card, such as $(*, *, *)$ or $(*, 1, *)$ . Representation subjects spent 18.9 minutes running specific mental simulations (50% of their mental simulation time), while Control subjects spent only 4.2 minutes (25% of their mental simulation time; $t(22) = 2.66, p < 0.01$ ). More interestingly, Representation subjects chose specific instances for 60.0% of their mental simulation time with two representations. In contrast, only 12.9% of the time spent in mental simulations with one representation were coded as specific test-cases. We propose, based on prior research (Kant and Newell 1984), that subjects are able to run more general mental simulations with one representation than with two representations, because holding a single representation frees cognitive resources that can be used to perform more cognitively demanding mental simulations (i.e., mental simulations for general instances).

## 5.5. Final Performance

In the first study, the main difference in performance between the two groups was the quality of their programs in terms of generality. The Representation subjects wrote specific programs with a central object. These programs could not solve other TOH isomorphs. On the other hand, the Control subjects wrote programs with recursion and necessary/sufficient conditions. These programs could be modified easily to solve any other TOH isomorph. The two groups spent roughly the same time developing programs from scratch (Representation: 157 minutes; Control: 118 minutes; $t(6) = 1.53$ , ns).

In contrast, in this study, the two groups had similar comprehension performances as measured by their ability to run the two test cases after they finished the experiment (Representation: 22.4 minutes; Control: 21.8 minutes; $t(22) = 0.14$ , ns), as well as by our written comprehension test (Representation: 81/100 points; Control: 84/100 points; $t(22) = 0.61$ , ns). $^{1}$ But Representation subjects ran more mental simulations and spent more time in understanding the given program. They spent more than twice the time spent by Control subjects (Representation: 37.5 minutes; Control: 16.7 minutes; $t(22) = 2.57$ , $p < 0.01$ ). They also ran more mental simulations (Representation: 6.75 simulations; Control: 3.17 simulations; $t(22) = 1.77$ , $p < 0.05$ after Poisson transformation).

Up to this point, we have observed representation changes during cognitive activities in either the rule space (experiment 1) or the instance space (experiment 2). But we have not observed explicit representation changes in the representation space using either Construct or Map operators. In the third study we observe explicit searches in the representation space during representation change.

## 6. Third Study (Program Reuse)

This section presents the third empirical study in which subjects were asked to reuse a given program for a new problem.

## 6.1. Experimental Design and Procedure

Nine Representation subjects and three Control subjects participated in the third study. We only assigned three subjects to the Control group because we expected that program reuse would be relatively easy when there is no need for representation change. On the other hand, we were especially interested in observing searches in the representation space for Representation subjects, thus the high number of participants.

Both groups were given the 3MC problem and its solution program (the CHANGE solution as shown in Appendix 1) and were asked to reuse the program for solving a new problem. The Control group was given the 5MC problem (CHANGE problem) as its new problem, while the Representation group was given the 5MT problem (TRANSFER representation) as its new problem.

We expected the task for the Representation group to be much more difficult than the task for the Control group. The Control subjects were expected to work only in the rule space because they were given the CHANGE program for the 3MC problem and were asked to reuse it for the 5MC problem (CHANGE representation). In contrast, the Representation subjects were forced to search the representation space because the existing program had the CHANGE representation while the new problem (5MT) was stated in the TRANSFER representation.

## 6.2. Detailed Analysis for a Successful Subject in the Representation Group

Only three of the nine Representation subjects succeeded in reusing the program for solving the new problem, which indicates the difficulty of program reuse requiring a representation change. We analyzed the protocols of the three successful subjects to compare how their cognitive activities were different from the unsuccessful subjects. Figure 12 shows the problem behavior graph in the representation space (Representation Behavior Graph) for MT10 who successfully reused the old program. This is the first time that we observed explicit searches in the representation space during representation change.

Each square in Figure 12 represents a Map episode within the representation space. The second line in the square (e.g., MT $\langle -\rangle$ MC in Map1) represents the two representations in the coding schema of the Map episode (one for REP1 and the other for REP2). The number in the parentheses of the last line represents the duration of the episode in seconds. Therefore, Figure 12 shows that MT10 spent 90 seconds in the representation space (in Map1) mapping the TRANSFER representation of 5MT to the CHANGE representation of 3MC directly. He tried two more Map operations (Map2 and Map3) but was unable to execute this mapping directly. Then he recalled (and/or built) an intermediate representation, the so called inverse Tower of Hanoi (ITOH). This event assumes the subject knew the Tower of Hanoi problem and was able to build an inverse representation of it. In Map4-Map7 he mapped the TRANSFER representation (MT) into this new intermediate representation (ITOH). Then he mapped (Map8-Map10) the inverse TOH (ITOH) and the CHANGE representation (MC). Finally, after he established these two intermediate mappings, one between the CHANGE representation and ITOH, and the other between ITOH and the TRANSFER representation, he was able to map between the TRANSFER (MT) representation and the CHANGE (MC) representation directly (Map11–Map16). Figure 13 provides four schemas for important Map episodes (Map2, Map6, Map8, and Map11) in the RPBG.

Figure 12 Representation Behavior Graph for MT10  
![](/api/attachments/6ZN46ZY7/fulltext/images/7c01d23e7aab15447c2672ec20a7a17842d980eb15698b7e5b254f1e099d8e2d.jpg)  
INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

Figure 12 shows that the subject first performed three Map episodes (Map1–Map3) in the representation space, attempting to map the TRANSFER representation of 5MT to the CHANGE representation of 3MC directly. Figure 13 shows one of these three Map episodes (Map2) in detail. While he was developing a rule (RU3), the subject visited the representation space briefly (80 seconds). During this visit, he tried to map the CHANGE and TRANSFER representations directly, by stating, "So in this case we are not changing the globe size. We are trying to move globes. So, let see. Amm, \*\* so what's similar here, amm." He tried one more Map operation (Map3) but was unable to execute this mapping directly. Then he recalled or partially built an intermediate representation, the so-called inverse Tower of Hanoi (ITOH), mapping the largest globe in the monster transfer problem to the smallest disk in the TOH problem. Evidently, he knew the Tower of Hanoi problem and was able to build an inverse representation of it.

In Map4–Map7 he mapped the TRANSFER representation (MT) into this new intermediate representation (ITOH). Figure 13 shows Map6 in detail. It is clear from the protocols that he established the mapping between the largest globe in the monster transfer problem and the smallest disk in the TOH problem "Only transfer the largest globe. Only transfer the smallest disk". Then he mapped (Map8–Map10) the inverse TOH on the monster change problem (MC). Figure 13 also shows Map8 in detail. He tried to map the ITOH on MC by saying, "Let's umm since we are trying to use tower of hanoi as the basis for this problem, can we fit this one (source program) into the tower of, if we change it slightly." Finally, after he established these two intermediate mappings, one between MC and ITOH and the other between ITOH and MT, he was able to map between the TRANSFER representation and the CHANGE representation directly (Map11–Map16). Figure 13 shows Map11 in which he said, "It gives, ya, it does the same thing. Amm, \*\*, yea, that should work. . . . Okay. So, we are calling, are we reversing monster and globe in every case."

The Representation Behavior Graph in Figure 12 shows how the subject used ITOH as a stepping stone in mapping the two original representations. In order to understand how he did it, we have displayed the activities in all three spaces between Map4 and Map7 in Figure 14.

He started by running a mental simulation (MS8) with a special case (24, 5, 13) in the instance space, and during this mental simulation he briefly visited the representation space (Map4). During Map4, he recognized the TOH problem. He stated, "Wow!! This this almost seems like, hmm, that's very interesting. It's almost like, the tower of hanoi."

Figure 13 Four Filled-in Schema for Important Map Episodes  
![](/api/attachments/6ZN46ZY7/fulltext/images/99736801defc38018ea4240441c81584baef32033f9d2f88546dc117d1190ede.jpg)

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

Figure 14 Three Problem Spaces for MT10 Between Map4 and Map7  
![](/api/attachments/6ZN46ZY7/fulltext/images/f22fa600224225a7164d8ac0afac1d1fc574a58b640a8814ed0563c13f1fb163.jpg)

Then he moved back to the instance space and continued running MS8. Then he started the same mental simulation (MS9) with different steps. In the middle of MS9, he again moved to the representation space very briefly and said, "This looks awfully similar to tower of hanoi. Amm \*\*." After he spent 121 seconds running MS9, he moved to the representation space and did Map6 (shown in Figure 13). He established the mapping between the largest globe in the monster transfer problem and the smallest disk in the TOH problem (this is the reason why it is called the inverse TOH representation). After establishing a couple of more mappings, he concluded that the two problems are the same ("it's exactly the same").

Then he moved into the rule space and derived RU7 based on his knowledge of the solution for TOH problem. However, he could not complete the rule because he was not sure about his recollection of the TOH solution. So he moved into the instance space and ran MS10, which is a specific case of the inverse TOH problem (the small peg has all of the five disks). After he obtained general knowledge of the solution for the TOH problem, he ran another mental simulation, but this time with the MT problem. In this simulation (MS11), he tested whether he could use the knowledge he got from MS10 (Inverse TOH) for the MT problem. Based on these two simulations, he moved back to the rule space and developed RU8. Then, he moved to the Representation space briefly, and stated, "Well, let see, so \* it's like starting the tower of hanoi in mass." Finally, he moved into the instance space, and ran one more mental simulation (MS12). In this simulation, he used the same instance used in MS8, MS9, and MS11 (24, 5, 13), but the instance is represented as Inverse TOH rather than MT.

## 6.3. Aggregate Protocol Results

Only three of the nine Representation subjects reused the program successfully. The other six Representation subjects either ran out of time or started to develop a program from scratch. Of the total time, Representation subjects (both successful and unsuccessful) spent 21% of their time in the Map operation, for an average of 15.7 minutes per subject. Map episodes had an average elapsed time of 96.3 seconds each. Since the third experiment is about program reuse, we focused our attention on the Map episodes.

The analysis of the verbal protocols for the three successful Representation subjects shows a remarkable degree of similarity in their mapping activities within the representation space. All three subjects generated the same intermediate representation (inverse TOH). They used this representation as a stepping stone between 3MC (the source problem) and 5MT (the target problem). Their verbal protocols reveal that the three subjects executed three key activities in the representation space before reusing the rules of the 3MC solution for the 5MT problem: 1) retrieving from memory features of the Tower-of-Hanoi problem (TOH), 2) discovering that the target problem (5MT) has the same structural features as the inverse TOH problem, and 3) mapping the INVERSE TOH problem to the source problem (3MC).

They also spent approximately two thirds (68%) of their time running mental simulations in the instance space. They used these mental simulations to execute the two intermediate mappings. Representation mappings through mental simulations can be inferred from the fact that subjects run the same test cases with different representations. Finally, as in traditional empirical studies in Scientific Discovery, operations in the rule space were interleaved with mental simulations in the instance space. For example, if the derived rule triggered by the representational mapping was not specific enough, they moved to the instance space and ran a couple of mental simulations, then moved back to the rule space to elaborate on the derived rule.

The six unsuccessful Representation subjects attempted similar processes to those executed by the successful subjects. All six subjects attempted to map the MT problem into the CHANGE solution directly. Four of the them retrieved features of the TOH problem and verbalized the similarities with the current problem. Two of them transformed it into the inverse TOH representation and mapped it to the target problem (5MT). None of them executed the mapping between the inverse TOH problem and the source problem (3MC). Consequently, unsuccessful Representation subjects tried the same type of cognitive activities as the successful Representation subjects, but they were unable to finish the final mapping in the representation space.

The three Control subjects were all successful in reusing the old program within the time limit. Their behavior was very different from that of the Representation subjects. Control subjects derived the new solution program directly from the computer program. They neither created the intermediate representation nor ran any mental simulations. All of their activities were in the rule space deriving the new program.

## 6.4. Final Output

In this study the Representation subjects spent more time and performed worse than the Control group. In the first study, the time spent was equivalent between the two groups, but the quality of the programs written by the Representation group was inferior to the Control group's. In the second study, both groups seemed to have equivalent comprehension of the programs, but the Representation group took up more time. In this study, only three of the nine Representation subjects reused the old program successfully. The time spent in establishing the correct mapping by these three subjects was greater than the time spent by the three Control subjects (Successful Representation subjects: 20.8 minutes; Control subjects: 8.9 minutes; $t(4) = 1.786$ , p < 0.1). The rest of the Representation subjects were unsuccessful even after spending more than six times the time spent by the other six subjects (Unsuccessful Representation subjects: 102.8 minutes). All subjects were assured that the existing program could be reused to solve the new problem.

Successful Representation subjects had to generate a new intermediate representation in the representation space, execute a series of Derive operations in the rule space for mapping between the three representations (TRANSFER, inverse TOH, and CHANGE), and run mental simulations for testing these mappings. Unsuccessful Representation subjects attempted the same activities in the representation space but failed. On the other hand, (successful) Control subjects primarily had to execute a series of Derive operations in the rule space for refining the existing computer program. Therefore, the difference between the Representation and Control groups in the third experiment is greater than the differences between the two groups in the first two experiments.

## 7. General Discussion

This section includes summary of results, implication of the results, and the limitations of the research.

## 7.1. Summary of Results

This research proposes and tests a new theoretical view of programming. It regards programming as problem solving in three problem spaces. The empirical results show that programming becomes more difficult when representation change is required. The analysis of the verbal protocols shows that detecting representational change is difficult. In the first two experiments, we did not find explicit verbal protocols of Construct or Map operators in the representation space for changing representations. In these two experiments, representation changes were detected by inspecting the verbal and program protocols for rule or mental simulation episodes. We assume that representation changes happened suddenly so we can only detect them by comparing the rule and mental simulation episodes that occurred before and after the change, which makes research in this area very difficult to conduct. In the third experiment, we found explicit evidence of search in the representation space because the programmers were forced to map rules from an existing program to a new problem. We also found that mapping among the three available representations (CHANGE, TRANSFER, ITOH) was very difficult (only three out of nine subjects succeeded). The combined results from the three experiments indicate that representation change is important in programming because it has radical consequences on the behavior of programmers.

In summary, programming is problem solving in multiple problem spaces. The task is highly simplified if no representation change is needed. Considerable cognitive difficulties stem from the need to change representations. Improved programming environments and teaching methods should provide more support and guidance on how to search in each problem space, and on how to help programmers change representations when needed.

## 7.2. Implications

Prior studies in Scientific Discovery provide valuable insights on how to assist scientists. Since programming is similar to Scientific discovery, we borrow insights from Scientific Discovery to generate recommendations on how to assist programmers. Therefore, some of our recommendations do not stem from our empirical results directly.

In the rule space, programmers generate and refine rules for the given program by using the Infer and Derive operations. The Infer operation can be facilitated if the programming environment helps in the identification of patterns in multiple instances. The BACON program written by Langley et al. (1987) provides several heuristics for the successful use of the Infer operation. For example, they suggest that scientists pay special attention to unusual patterns of instances instead of focusing on instances that support current rules. Programmers can also use the Derive operation more efficiently if programming environments provide convenient tools to browse and identify existing rules (i.e., programs) that seem promising for solving the problem at hand. Prior studies in analogical problem solving have indicated the way to help the identification and modification of analogs. For example, Gentner and Toupin (1986) found that an explicit demonstration of the structural features (relations and roles) of the analogs facilitates the process of mapping distant analogs significantly, which means that emphasizing methods and relational attributes may help programmers identify candidate objects for reuse.

In the instance space, programmers run mental simulations to develop new rules and/or test existing rules. Good programming environments should help in selecting appropriate instance cases. Klahr and Dunbar (1988) explain the general features of useful tests in Scientific Discovery. For example, they found that the most important step in designing tests is to focus on the aspect of the current situation that the test is intended to illuminate. This finding means that providing external aids for displaying the current situation of the problem may help programmers design more informative mental simulations in the instance space.

In the representation space, programmers construct an initial representation and modify it when they experience difficulties in the rule and instance spaces, or when they have alternative representations available. Prior studies in insight problem solving (Kaplan and Simon 1990) have found that search in the representation space can be promoted by several heuristics. For example, the Notice Invariant heuristic (noticing properties of the situation that remained invariant during solution attempts) has been found to be a particularly powerful means for focusing search. The programming environment can assist programmers in using this heuristic by recording and externally displaying invariant features of representations in prior rules and instances. The programming environment can also help programmers by providing some principles for selecting appropriate representations. For example, the myopic role definition principle (Kim et al. 1995) recommends that programmers develop rules for an entity (class) by only considering the behavior of each specific entity and the messages sent to other entities, while completely ignoring how these messages affect the goals or states of other entities. This strategy is cognitively different from the information hiding or encapsulation principles in OO programming because it reduces the focus of attention to individual entities when developing methods, and postpones the coordination and abstraction of rules. For example, in the MC problem a myopic role definition strategy would recommend the development of rules for the small monster object by: 1) trying to change the size of the small monster's globe to small, 2) if not possible, sending messages to the other monsters telling them to change their globes. In this cognitive strategy, I (the small monster class) do not worry about how the other monsters will perform the messages or whether the execution of the messages will take them further away from their own goals; I just send the messages, wait for them to conduct them, and then change my globe size to small. This strategy may prevent programmers from developing a representation with a central object that looks ahead and makes an optimal decision after considering the behaviors of other objects.

If our new view of the programming task receives more empirical support, it should change the way we teach programming. Traditionally, programming has been taught by introducing students to programming constructs. Programming constructs include data structures (e.g., integer, record, lists, array, class, etc.) and control structures (e.g., iteration, recursion, conditional if-then, macros, and lambda, etc.). Then students are trained to write rules by using the available programming constructs. Almost all training centers on how to search in the rule space while very little focuses on how to search (and use) the instance and representation spaces. Students are not taught how to design informative tests or how to choose and test appropriate representations. A state-of-the-art programming course would emphasize how to conduct complex problem solving (i.e., Scientific Discovery) instead of the learning and application of programming constructs (although this knowledge is obviously necessary). In fact, we believe programming is indeed an excellent domain for teaching general problem-solving skills, as long as the focus is on the similarities between programming and Scientific Discovery.

## 7.3. Limitations of Current Experimental Approach and Future Research

Our experimental methodology limits our results in several ways. The experiments used very small programs only in OOP and utilized college students as programmers. They also used Tower of Hanoi isomorphs that might not be typical of the majority of information system problems. These experimental features prohibit us from investigating several important issues, such as problems of building an abstraction hierarchy (e.g., Booch 1994), impacts of different system development methodologies (e.g., Vessey and Conger 1994), documenting programs (e.g., Davies 1991), negotiating with co-programmers (e.g., Flor and Hutchins 1991), etc.

The programs that the subjects wrote to solve the problems are very small compared with typical programs in the real-world software development field. Nevertheless, the factors we varied between the two experimental conditions produced large effects on the processes of programming and the qualities of final programs. If substantial effects can be produced in this simple environment, we have every reason to suppose that the variables we studied are of considerable importance also in more complex situations where the difficulties in understanding problems and developing rules are even greater than they are under our experimental conditions. However, our experimental studies do not predict the precise scale of these effects in complex situations. This prediction can be tested only in more complex settings, but the experiments demonstrate the value of carefully chosen simple environments for disclosing the powerful effects of key variables upon human performance in programming. Complementing studies that examine software development in naturalistic settings, experiments on smaller programs can give deep insights into the psychological processes employed, and can guide the design of more complex studies.

Our studies used OOP because it is easier to code subjects' internal representations more objectively than in programming in general, since OOP defines explicitly the three representation components. But we believe that the main themes of this paper, programming as scientific discovery and the difficulty of representation change, also apply to other programming paradigms. We are in the process of conducting further empirical studies to test our findings in organizational settings with multiple programming constructs. We expect these findings to help us assess how easy it is to generalize our theoretical and methodological view to programming in more complex settings. $^{2}$

$^{2}$ The research was supported by INI research grant #1-41445 and the Korea Science and Engineering Foundation grant #961-0909-054-1. The authors would like to acknowledge the advice and comments of Herbert A. Simon, Bernd Bruegge, the associate editor, and two reviewers.

Appendix 1 Solution Program for the 3MC Problem
#include<iostream.h>

const int small = 1;

const int medium = 2;

const int large = 3;

class Monster

private:
int monsterSize;
int currentGlobeSize;
Monster \* largerMonster;
public:
Monster (int monsterSize, Monster \* IgrMonster);
\~Monster 0;
void setGlobeSize();
void changeGlobeSize (int desiredGlobeSize);
int getRemaining Size (int currentGlobeSize, int desired-GlobeSize);

## };

main()
{
    Monster largeMonster(large, NULL);
    Monster mediumMonster(medium, &largeMonster);
    Monster smallMonster(small, &mediumMonster);

smallMonster.setGlobeSize();
mediumMonster.setGlobeSize();
largeMonster.setGlobeSize();

smallMonster.changeGlobeSize(small);
mediumMonster.changeGlobeSize(medium);
largeMonster.changeGlobeSize(large);

Monster::Monster(int mSize, Monster\* IgrMonster)
{
    monsterSize = mSize;
    largerMonster = lgrMonster;
}

Monster :: \~Monster()
{
}
void Monster :: setGlobeSize()
{
cout << "What is the globe size of monster" << monsterSize << question";
cin >> currentGlobeSize;
}

void Monster::changeGlobeSize(int desiredGlobeSize)
{
int remainingSize;
Monster \*temp;

if (currentGlobeSize == desiredGlobeSize)
return;
else{
remainingSize=getRemainingSize(currentGlobeSize,desired-
GlobeSize);

```cpp
temp = largerMonster;
while (temp)
{
    temp->changeGlobeSize(remainingSize);
    temp = temp->largerMonster;
}
currentGlobeSize = desiredGlobeSize;
cout << "Change the size of monster" << monsterSize << "to size"
<< desiredGlobeSize << "\n";
}
```

int Monster::getRemainingSize (int currentGlobeSize, int desiredGlobeSize)
{
    if (currentGlobeSize != small && desiredGlobeSize != small)
    return small;
    else if (currentGlobeSize != medium && desiredGlobeSize != medium)
    return medium;
    else
    return large;
}

Appendix 2 Solution Program for the 3MT Problem #include <iostream.h>

class Globe
{
private:
int globeSize;
int currentOwnerMonster;
Globe \* largerGlobe;
public:
Globe (int GlobeSize, Globe \* IgrGlobe);
\~Globe();
voidsetOwnerMonster();
voidchangeOwnerMonster (int desiredOwnerMonster);
int getRemainingMonster (int currentOwnerMonster, int desiredOwnerMonster);

## };

main()
{
    Globe    largeGlobe(large, NULL);
    Globe    mediumGlobe(medium, &largeGlobe);
    Globe    smallGlobe(small, &mediumGlobe);

smallGlobe.setOwnerMonster();
mediumGlobe.setOwnerMonster();

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

largeGlobe.setOwnerMonster();

smallGlobe.changeOwnerMonster(small);
mediumGlobe.changeOwnerMonster(medium);
largeGlobe.changeOwnerMonster(large);
}

Globe::Globe(int gSize, Globe\* IgrGlobe)
{
    globeSize = gSize;
    largerGlobe = lgrGlobe;
}

Globe::\~Globe()
{
    }

void Globe::setOwnerMonster()
{
    cout << "Where is the globe" << globeSize << "located?\n";
    cin >> currentOwnerMonster;
}

void Globe :changeOwnerMonster(int desiredOwnerMonster)
{
    int remainingMonster;
    Globe \*temp;

    if (currentOwnerMonster == desiredOwnerMonster)
    return;
    else {
    remainingMonster = getRemainingMonster(currentOwnerMonster, desiredOwnerMonster);
    temp = largerGlobe;
    while (temp)
    {
    temp->changeOwnerMonster(remainingMonster);
    temp = temp->largerGlobe;
    }
    currentOwnerMonster = desiredOwnerMonster;
    cout << "Change the owner of globe" << globeSize << "to the monster" << desiredOwnerMonster << "\n";
    }
}

int Globe..getRemainingMonster (int currentOwnerMonster, int desiredOwnerMonster)
{
    if (currentOwnerMonster != small && desiredOwnerMonster != small)    return small;
    else if (currentOwnerMonster != medium && desiredOwnerMonster != medium)
    return medium;
    else

INFORMATION SYSTEMS RESEARCH
Vol. 8, No. 1, March 1997

return large;

## References

Adelson, B. and E. Soloway, "The Role of Domain Experience in Software Design," IEEE Trans. on Software Engineering, 11 (1985), 1351–1360.

Anzai, Y. and H. A. Simon, "The Theory of Learning by Doing," Psychological Rev., 86 (1979), 124–140.

Boehm-Davis, D. A., R. W. Holt, and A. C. Schultz, "The Role of Program Structure in Software Maintenance," International J. Man-Machine Studies, 36 (1992), 21–63.

Booch, G., Object Oriented Analysis and Design with Applications (2nd ed.), Benjamin/Cummings, Redwood City, CA, 1994.

Chi, M. T., P. J. Feltovich, and R. Glaser, "Categorization and Representation of Physics Problems by Experts and Novices," Cognitive Sci., 5 (1981), 121–152.

Davies, S. P., "The Role of Notation and Knowledge Representation in the Determination of Programming Strategy: A Framework for Integrating Models of Programming Behavior," Cognitive Sci., 15 (1991), 547–572.

——, "Models and Theories of Programming Strategy," International J. Man-Machine Studies, 39 (1993), 237–267.

Detienne, F., "Reasoning from a Schema and from an Analog in Software Code Reuse," in Moher Koenemann-Belliveau, and S. Robertson (Eds.), Empirical Studies of Programmer: Fourth Workshop, Ablex Publishing, Norwood, NJ, 1991, 5–22.

— and E. Soloway, "An Empirically-derived Control Structure for the Process of Program Understanding," International J. Man-Machine Studies, 33 (1990), 323–342.

Dunbar, K., "How Scientists Really Reason: Scientific Reasoning in Real-World Laboratories," in R. J. Sterberg and J. Davidson (Eds.), Mechanisms of Insight, MIT Press, Cambridge, MA, 1993.

Ericsson, A. and H. A. Simon, Protocol Analysis (2nd ed.), MIT Press, Cambridge, MA, 1993.

Farris, H. and R. Revlin, "Sensible Reasoning in Two Task: Rule Discovery and Hypothesis Evaluation," Memory and Cognition, 17 (1989), 221–232.

Flor, N. and E. Hutchins, "Analyzing Distributed Cognition in Software Teams: A Case Study of Team Programming During Perfective Software Maintenance," in Moher Koenemann-Belliveau and S. Robertson (Eds.), Empirical Studies of Programmers: Fourth Workshop, New Brunswick, NJ, 1991, 36–64.

Gentner, D., "Structure-Mapping: A Theoretical Framework for Analogy," Cognitive Sci., 7 (1983), 153–170.

— and C. Toupin, "Systematicity and Surface Similarity in the Development of Analogy," Cognitive Sci., 10 (1986), 277–300.

Guindon, R., "Designing the Design Process: Exploiting Opportunistic Thoughts," Human-Computer Interaction, 5 (1990), 305–344.

—, B. Curtis, and H. Krasner, A Model of Cognitive Processes in Software Design: An Analysis of Breakdowns in Early Design Activities by Individuals, MCC Tech. Rep. No. STP-283-87, Microelectronics and Computer Technology Corporation, Austin, TX, 1987.

Hayes, J. R. and H. A. Simon, "Understanding Written Problem Instructions," in H. A. Simon (Ed.), Models of Thought, Vol. 1, Yale University Press, New Haven, CT, 1977a, 451–476.

— and —, "The Understanding Process: Problem Isomorphs," in H. A. Simon (Ed.), Models of Thought, Vol. 1, Yale University Press, New Haven, CT, 1977b, 477–497.

Hoc, J. M. and A. Nguyen-Xuan, "Language Semantics, Mental Models and Analogy," in J. M. Hoc, T. R. G. Green, Samurcay and D. J. Gilmore (Eds.), Psychology of Programming, Academic Press, London, 1990, 139–156.

Holland, J. H., K. J. Holyoak, R. E. Nisbett, and P. R. Thagard, Induction; Processes of Inference, Learning, and Discovery, MIT Press, Cambridge, MA, 1986.

Jacobson, I., Object-Oriented Software Engineering: A Use Case Driven Approach, Addisson-Wesley, New York, 1992.

Jeffries, R., A. Turner, P. G. Polson, and M. E. Atwood, "The Processes Involved in Designing Software," in J. R. Anderson (Ed.), Cognitive Skills and Their Acquisition, Lawrence Erlbaum Association, Hillsdale, NJ, 1981, 255–283.

Karmiloff-Smith, A., "Children's Problem Solving," in M. Lamb, A. Brown, and R. Rogoff (Eds.), Advances in Developmental Psychology, Vol. 3, LEA, Hillsdale, New Jersey, 1984, 39–89.

Kant, E. and A. Newell, "Problem Solving Techniques for the Design of Algorithms," Information Processing and Management, 20 (1984), 97–118.

Kaplan, C. and H. A. Simon, "In Search of Insight," Cognitive Psychology, 22 (1990), 374–419.

Kim, J., Problem Representation and Rule Development in Object-Oriented Software Development, Unpublished doctoral dissertation, Carnegie Mellon University, Pittsburgh, PA, 1993.

— and F. J. Lerch, "The Cognitive Processes in Logical Design: Comparing Object-oriented Design and Traditional Functional Decomposition Methodologies," Proc. CHI '92 Human Factors in Computing Systems, ACM Press, New York, 1992, 489–498.

—, —, and H. A. Simon, "Representation Construction and Rule Development in Object-oriented Design," ACM Trans. on Computer-Human Interaction, 2 (1995), 357–390.

Klahr, D. and K. Dunbar, "Dual Space Search During Scientific Reasoning," Cognitive Sci., 12 (1988), 1–48.

—, A. Fay, and K. Dunbar, "Heuristics for Scientific Experimentation: A Developmental Study," Cognitive Psychology, 25 (1993), 111–146.

Klayman, J. and Y. Ha, "Confirmation, Disconfirmation, and Information in Hypothesis Testing," Psychological Rev., 94 (1987), 211–228.

Kuhn and Brannock, "Development of the Isolation of Variables Scheme in Experimental and Natural Experiment Context," Developmental Psychology, 13 (1987), 9–14.

Langley, P., H. Simon, G. Bradshaw, and J. Zytkow, Scientific Discovery: Computational Explorations of the Creative Processes, MIT Press, Cambridge, MA, 1987.

Letovsky, S., "Cognitive Processes in Program Comprehension," in E. Soloway and S. Iyengar (Eds.), Empirical Studies of Programmers, Ablex Publishing, Norwood, NJ, 1986, 58–79.

Maiden, A. M. and A. G. Sutcliffe, "Analogously Based Reusability," Behavior & Information Technology, 11 (1992), 79–98.

Mayer, R. E., "The Psychology of How Novices Learn Computer Programming," Computing Surveys, 13 (1981), 121–141.

Medin, D. E. and E. J. Shoben, "Context and Structure in Conceptual Combination," Cognitive Psychology, 20 (1988), 158–190.

Newell, A. and H. A. Simon, Human Problem Solving, Prentice-Hall, Englewood Cliffs, NJ, 1972.

Pennington, N., "Stimulus Structures and Mental Representations in Expert Comprehension of Computer Program," Cognitive Psychology, 19 (1987), 295–341.

Pirolli, P., "A Cognitive Model and Computer Tutor for Programming Recursion," Human-Computer Interaction, 2 (1986), 319–355.

Qin, Y. and H. A. Simon, "Laboratory Replication of Scientific Discovery Processes," Cognitive Sci., 14 (1990), 281–312.

Rist, R., "Plans in Programming: Definition, Demonstration and Development," in E. Soloway and R. Iyengar (Eds.), Proc. First Workshop on Empirical Studies of Programmers, Ablex, Norwood, NJ, 1986, 28–47.

——, "Schema Creation in Programming," Cognitive Sci., 13 (1989), 389–414.

Ruiz, D., Learning and Problem Solving: What is Learned While Solving the Towers of Hanoi, Unpublished doctoral dissertation, Stanford University, Stanford, CA, 1986.

Rumbaugh, J., M. Blaha, W. Premerlani, F. Eddy, and W. Lorensen, Object-oriented Modeling and Design, Prentice-Hall, Englewood Cliffs, NJ, 1991.

Simon, H. A., "The Structure of Ill Structured Problems," Artificial Intelligence, 4 (1973), 181–201.

— and G. Lea, "Problem Solving and Rule Induction," in H. A. Simon (Ed.), Models of Thought, Vol. 1, Yale University Press, New Haven, CT, 1977, 329–346.

—, K. Kotovsky, and J. R. Hayes, "Why Are Some Problems Hard? Evidence from the Tower of Hanoi," Cognitive Psychology, 17 (1985), 248–294.

— and D. Kulkarni, "The Processes of Scientific Discovery: The Strategy of Experimentation," in H. A. Simon (Ed.), Models of Thought, Vol. 2, Yale University Press, New Haven, CT, 1989, 357–382.

VanLehn, K., "Rule Acquisition Events in the Discovery of Problem-Solving Strategies," Cognitive Sci., 15 (1989), 1–47.

Vessey, I., "Cognitive Fit: A Theory-Based Analysis of the Graphs Versus Table Literature," Decision Sci., 22 (1991), 219–240.

— and D. Galletta, "Cognitive Fit: An Empirical Study of Information Acquisition," Information Systems Research, 2 (1992), 63–84.

— and S. Conger, "Requirements Specification: Learning Objects, Process, and Data Methodologies," Comm. ACM, 37 (1994), 102–113.

Visser, W., "More or Less Following a Plan During Design: Opportunistic Deviation in Specification," International J. Man-Machine Studies, 33 (1990), 247–278.

Iris Vessey, Associate Editor. This paper was received on August 1, 1994 and has been with the authors 10 months for 2 revisions.
