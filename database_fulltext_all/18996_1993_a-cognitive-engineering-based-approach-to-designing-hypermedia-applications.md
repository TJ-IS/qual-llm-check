---
otero_id: 18996
otero_key: "TNSYXRXV"
title: "A cognitive engineering-based approach to designing hypermedia applications"
authors: "Feng-Yang Kuo"
year: "1993"
journal: "Information & Management"
doi: "10.1016/0378-7206(93)90074-4"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Research

# A cognitive engineering-based approach to designing hypermedia applications

Feng-Yang Kuo \*

University of Colorado at Denver, Denver, CO, USA

Hypermedia systems, characterized by their use of graphics, windowing, and networking, are often advocated as effective tools for information representation and management. Their sophistication demands that software engineers be knowledgeable of user cognitive processes in order to develop systems that are functional, learnable, and usable. Recent cognitive research in human-computer interaction has provided a theoretical foundation for understanding user behavior, but the knowledge has not yet been integrated into a practical design procedure. This paper discusses an approach incorporating theoretical work into the process of designing hypermedia systems. Using this approach results in an understanding of user cognitive requirements, a complete design that matches hypermedia presentations to these requirements, and shortened development time.

Keywords: Hypermedia; Cognitive engineering; Human-computer interaction

## 1. Introduction

Hypermedia systems are computer systems built around a network of nodes to allow good information representation and management $[13,10]$ . Each node may contain information in various media formats: text, graphics, sound, and animated picture. A user navigates among nodes connected by predefined network links. The collection of hypermedia nodes and navigation links makes hypermedia systems suitable for supporting a wide range of tasks.

As an example, a hypermedia system called SPRINT was designed to facilitate strategic planning by representing the elements of a plan and their associations as a network [6]. Some hypermedia systems facilitate collaboration among knowledge workers, such as lawyers [9] and auditors [25]; others support city planning [31] and creating maintenance manuals [17].

These hypermedia applications offer users a large shared-database and easy-to-use interfaces for navigating the database by means of direct manipulation. The large database, however, increases the network's complexity which, in turn, causes the user to become “lost in hyperspace” [11].

![](/api/attachments/TNSYXRXV/fulltext/images/58b936efd9db3275b4a66e76d37a147c702b7d9f443daf6b9c1b7ad343dbe3eb.jpg)

To solve this problem, several researchers have focused on providing better browsing paradigms to facilitate users' navigation of the network. For example, Van Dyke Parunak [12] suggests mapping commonly used search strategies, like finding unique identifiers and following directions, to construct the hyperspace topology. Trigg [33] implements Guided Tours and Tabletops that employs annotation, graphic layout, and ordered presentation, to communicate hypermedia notes' meanings to the users. A third technique is by use of controlled access in Scripted Documents system [32], of which users must follow a script consisting of directed paths through one or more hypernodes.

Still, the browsing paradigms offered by most hypertext systems do not meet most needs of users, especially of those who are unfamiliar with the material being presented [30]. Such paradigms provide only general navigational guidance, while the needs of a system's users are determined by the specific preference and knowledge of the user and by the characteristics of the tasks that the user must perform. The paradigms' usefulness can be enhanced if a process of analysis, design, and implementation is applied to make sure that the system meets the needs of the user and their tasks.

This paper presents a process centered around the user's cognitive capability. The concept of user-centered design has been advocated by researchers of human-computer interactions (HCI) like Norman [7] and Marcus and van Dam [2]. The user-centered design emphasizes the user's cognitive abilities as well as his/her cultural, professional, and personal preferences. This is critical to efficient navigation, because the problem of the user being confused can be attributed to the overload of the cognitive processing capability. More importantly, hypermedia capabilities are suited to expressing the user's cognitive processes (e.g., memory, motor, and perception). The media (i.e., pictures, sound, and animation) may complement and reinforce one another to enable more effective communication. But the media can complement the user only when their collective application correspond to the task requirements [16]. Understanding cognitive principles is therefore a prerequisite to the design of a successful hypermedia application.

## 2. The user-centered approach

User-centered design can be as simple as providing guidelines, such as those suggested by Kinzie and Berdel [28]. These involve noting important facts discovered in user interviews, using photographs to expand understanding, and providing hints and feedback during and after user interaction with the system.

User-centered design can also involve sophisticated use of principles for studying task context and user's needs. For example, the discount usability engineering [18,19] has been shown to be useful for designing advanced graphic interfaces. This approach aims at getting rapid design feedback so that more iterations can be tested. It advocates using principles such as simple natural dialog, speaking the user's language, and minimizing the memory load in designing the interface. A heuristic evaluation is performed to assess the interface in the early part of design. When two or more users are observed having problems with some aspect and when these problems can be explained by some established principles, then the problems should be fixed at once; the test shall continue when the new design is implemented. If the source of the problems cannot be explained, a more in-depth study of the design can be conducted.

Another successful application of user-centered design has been made by Gould et al. [8], who proposed four principles to analyze, design, and test the user interface of a system: early focus on users and tasks, integrated design, empirical measurement, and iterative design. To put these principles in practice, they suggested that designers develop a preliminary specification of the user interface. Equally important is collecting critical information about users and specifying behavioral goals by having a description of intended users, tasks to be performed, and measurements of interest, such as learning time, errors, attitude.

Our approach advocates the use of principles, empirical testing, and iterative design based on research in cognitive engineering and the psychology of HCI. Cognitive engineering has been termed the application of cognitive science to the creation of computer systems. It studies how cognitive processes can be enhanced through display and input devices, such as graphics and the mouse. Cognitive engineering principles are important in hypermedia design because they provide a theoretic foundation for applying each medium and constructing the network of hypermedia nodes that collectively satisfy the user's cognitive needs.

Three techniques that were successfully developed and tested by other researchers are inserted into the approach to ensure a comprehensive application of cognitive principles throughout analysis, design, and testing. The analysis advocated by Wixon et al. is useful for capturing user needs. Work by Carroll and his colleague helps us associating psychological principles with design features. The walkthrough technique of Lewis et al. [4] aids in evaluating the design quality before costly implementation.

The approach also provides a framework for documenting analysis results and design rationales in an integrated manner. The framework is a response to MacLean et al.'s call $[1]$ to include design rationales as a co-product of a design process. The rationale is a record of design alternatives and an explanation of why a specific choice was made. Comparing and contrasting design rationales of various systems allows us to capture the range of constraints affecting the design and to gain insights into why a choice does or does not work.

## 2.1. The approach

Information system experts have long known that the designer must study user goals, decision criteria, and alternative methods to be employed at various stages of task execution. Applying this prescription to hypermedia system, the designer needs to ask more than “what data do you use” and “what do you do with these data.” The inquiry should be more personal, such as “What are your goals of performing this task?” “Why are you doing it in this way?” and “What part of this task do you like best or least.” Asking such questions leads the designer to create an interface that resembles the user’s world.

## 2.1.1. Cognitive processes in HCI

Several studies in HCI development have centered around the cognitive engineering concepts of Card et al. [35]. They propose a three-stage cognitive model: the user perceives the computer presentation, activates long- and short-term memory to search for proper actions, and then acts by sending his/her motor processors in motion. A more elaborate seven-stage model (see Figure 1) expands the memory stage to include other mental activities like specifying action sequences. The work by these and some later researchers [24] shows that the interface must not only satisfy the motor and perceptual requirements but also empower the memory and cognition capacity of its users to let them predict the system's behavior.

![](/api/attachments/TNSYXRXV/fulltext/images/c90b63dd168ba9f826fa623c02f626e61e9c72b4390554cf0b86c3bb2a191e14.jpg)  
Fig. 1. Norman's seven stage model of human-computer interaction [7].

## 2.1.2. Four phases of the approach

In order for hypermedia presentations to help the user to perceive and interpret the display and to infer solutions when encountering new or difficult situations, task analysis should identify user goals and the methods and objects employed to achieve them $[29]$ . Grudin $[14]$ points out that interface objects should be grouped according to the context in which they are used, not simply by their normative descriptions.

A context-based analysis of user tasks is the first phase of our approach (see Figure 2). The contextual analysis is based not only on the data collected through traditional techniques like interviews and questionnaires, but also on interpreting what is observed in the task context and on dialogs with the user regarding these interpretations. In this analysis, the users and the designer are partners; the designer must understand “what the work is, what kind of computer system would support that work, how technology could transform such work, and how to anticipate and support the changes in work that new technology brings” [5]. The user’s own interpretation, language, and work structure must be gathered to study user goals, methods, and objects useful for design.

![](/api/attachments/TNSYXRXV/fulltext/images/86075526a56267f72a429246bffa4ec3a5b0e3e930590b931f948e661e3e8b9f.jpg)  
Fig. 2. The approach.

The contextual analysis is followed by artifact engineering. An artifact is a software and/or hardware system; for example, a hypermedia application may be considered an artifact. Artifact engineering involves specifying the features of the hypermedia system's interface and identifying the design rationales that lead to the selection of each feature. Carroll and Kellogg [22] have used artifacts like HyperCard and Lotus 1-2-3 for examining design rationales that explain why an artifact is successful. The approach here attempts to extend this to the practice of designing new artifacts. The designer must therefore study successful artifacts to learn their design rationales and to determine how they can be applied to the design of other artifacts. The result is an artifact specification that includes network configuration, each node's representation, and interface mechanisms, such as pop-up menus, windows, graphics, and forms. The selected hypermedia features, together with the supporting design rationales, are documented so they can later be evaluated and modified.

The contextual analysis and artifact specification provide a preliminary design of the hypermedia application. By now the designer may be ready to implement a prototype but first a walk-through can be performed. This requires interface experts, preferably those with in-depth understanding of cognitive engineering concepts, to evaluate the design independently. The walk-through allows user goals and actions to achieve these goals to be evaluated explicitly and thoroughly. The walk-through is useful in reducing the cost and time used in implementation.

The last is to create the hypermedia system. After implementation, usability testing will be performed, and iterative design refinements made until the user is satisfied.

## 2.2. Application of the approach

The benefits were shown in a seminar in the spring of 1991. Four separate hypermedia projects were carried out by groups of 3–4 information processing professionals. The result showed that the first three phases, although time consuming, enable the groups to develop a satisfactory product. Group members were required to study cognitive engineering and general HCI principles prior to the project. They were able to relate the design features of the artifact (i.e., the end product) to the applied principles; some commented that the entire design process might be less time consuming for the next project. Group members no longer felt overwhelmed by the various capabilities of hypermedia and were able to apply them intelligently. More importantly, repeated practice in applying the approach could result in more creative interface design. The approach enabled designers to look at system design from the perspective of user needs driving the system design, not vice versa. Overall, the experience demonstrated the practicality of the approach. Its long-term benefits included shortened development time, reduced cost, and higher user satisfaction.

1. Enter a keystroke: 230 msec
2. Mouse operation
2.1 Point with a mouse (average) 1500 msec
2.2 Point a mouse to a menu target 1900 msec
3. Move hands to mouse: 360 msec
4. Perception
4.1 perceive a response: 100 msec
4.2 Scanning 230 msec
4.3 Recognition 340 msec
5. Retrieve from memory
5.1 Retrieve a command name or a delimiter: 1350 msec
5.2 Retrieve a random command abbreviation: 1200 msec
6. Choose among methods: 1250 msec
7. Execute a mental step
7.1 Linking the content of short-term memory with long-term memory 70 msec
7.2 Execute a rule 100 msec
7.3 Decode abbreviations 60 msec

Fig. 3. Contextual analysis steps [5].

## 3. Details and an example

A hypermedia project is used to facilitate discussion. The aim of this project is to develop a system to teach young children the concept of gravity.

## 3.1. Contextual analysis

Figure 3 shows the steps of contextual analysis. This produces a list of user goals, methods, and objects employed to complete the task. Our experience suggests that the following functions are important: identify task metaphors, create task scenarios, and study user descriptive knowledge.

## Identify metaphors with their look and feel

In contextual analysis, the designer must search for metaphors to guide the design. They can be drawn from tools and systems that are used in the task domain and the common-sense real world $[21]$ . For example, observing a user typing with a typewriter may lead to the use of the typewriter metaphor for a word processor. The designer may need to choose a composite set of several metaphors; e.g., the analogy of a typewriter is inadequate for depicting more complex operations such as block insertion and deletion, because they may cause text overflow and page reformatting. For them, the word processor is more like magnetic tape splicer.

The metaphors become a basis of organizing the interface of the hypermedia system. A familiar appearance enables the user to recognize and interpret the representation. The designer should also concentrate on identifying methods and objects to be used later. An example is an interface that uses the desktop metaphor filled with icons representing objects like folders and a trash-can, and methods like moving an object to the trash-can to delete it [15].

## Analyze work activities and scenarios

User goals, methods, and objects can be discovered by analyzing users acting out work-related scenarios $[20,34]$ . The designer can create them for a hypothetical system and ask the user questions about these scenarios. In this way, the designer understands how various hypermedia features can be applied to solve user problems. A scenario is a record of user actions in response to request that the user performs a definite action, like reordering paragraphs of a document or computing the return on financial investment. A carefully constructed set of requests assures that a comprehensive range of situations is studied and that the results are applicable to real-life work situations. Each is chosen so that the resulting scenario is brief. Scenario analysis produces a record of user actions from which specific user goals, methods, and objects employed to achieve the goals can be identified. In addition, records of several users completing the same scenario enable the designer to compare different approaches to the same situation; this generates a set of methods and objects that satisfy a wider range of users.

## Understand what is in memory

When we ask the question “What do you know about …?” we often expect answers like “This is …, and because …, the result is …”; i.e., we expect the answers to be a narrative description. We assume that the knowledge is “symbolic” and stored accordingly. But there is strong evidence that human memory is more than a collection of concepts represented by symbols [23]. Color, images, sound, and even smell are all part of the storage and, therefore, are all part of a person’s knowledge.

Consequently, when we talk about understanding user needs, we have to think about those nonsymbolic aspects and the metaphors must have such characteristics. This leads to a model world interface that allows direct manipulation, resulting in speedy learning of the system [3].

## Contextual analysis results

The results are a list of user needs and a corresponding list of hypermedia features that should be useful. Table 1 presents partial results of contextual analysis for a system to help children learn concepts about gravity. The example is based on the metaphor of a child playing, like hitting a baseball or taking a boat or plane ride. This includes many objects: a child as the player, a baseball, a ball park, and a coach. It also includes a boat, and the marina, an airplane, and the airport, so that children can learn that gravity occurs in different locations and applies to all objects. For example, the child can drop objects of different sizes and observe that they reach the water at the same time. In playing baseball, the child is encouraged to hit the ball as far as possible. The child must choose the correct angle, i.e., 45 degrees in order to hit the ball out of the park when there is no spin and air drag. In the first column, the child's (user's) need is described in terms of the levels of the tasks and goals. The second column describes the potential hypermedia solution. The metaphor of hitting a baseball includes both color and sound effects, e.g., a solid sound, resembling that of a home-run hit; a green signal, like the traffic light, to show that the child can start hitting, etc.

## 3.2. Artifact engineering

In artifact engineering, the designer uses contextual analysis results to specify the system interface and associates design rationales with the specification. The metaphor chosen guides the design here. For example, the goal of hitting baseballs, riding a boat, and flying an airplane can be achieved by showing a map containing a ball park, a marina, and an airport; the child can elect where to play, e.g., to go to the ballpark to play baseball (see Figure 4).

Table 1  
A partial list of results from the analysis and design

<table><tr><td>User needs</td><td>Potential hypermedia solutions</td><td>Design rationales</td><td>Usability goals</td></tr><tr><td>Learn the concept of gravity</td><td>Provide a hypermedia system that simulates fun places, like hitting baseballs, dropping objects from a ship or a plane</td><td>The metaphor of fun places; easy to learn and fun to use</td><td>An acceptable level of user satisfaction</td></tr><tr><td>Hit baseball</td><td>Provide a ball park where the user can hit the ball. Show the motion of the ball flying</td><td>Interface facilitates planning and evaluation of user goals. Allow the user to associate his/her prior knowledge to the interface</td><td>Training time = time to associate the interface to the metaphor of hitting baseballs + time needed to learn to use the mouse</td></tr><tr><td>Go to a ball park</td><td>A button, represented by a ball player icon to be selected by the user</td><td>an easy-to-recognize icon; preempting user errors by guidance</td><td>Execution time is about 2070 msec (230 msec for scanning, 340 msec for recognition, and 1500 msec for pointing)</td></tr><tr><td>Hit the ball</td><td>A tee icon is selected, followed by a pop-up menu of various hitting angles from which a user can choose</td><td>Learn by doing; easy visual evaluation of user actions, minimal user action in menu operation; preempting user errors by guidance</td><td>Execution time is about 2470 msec (230 msec for scanning, 340 msec of recognition, and 1900 msec for pointing to the selected menu choice)</td></tr><tr><td>Ask the coach</td><td>A coach icon to be selected by the user; explanation is provided to the user about what the user must do to hit the ball out of the park. Linkages (buttons) are provided so the coach can guide the user to experiment with other parts of the system, like dropping an object from a vessel</td><td>Association of known facts (e.g., distance varied in accord with angles chosen) to new knowledge (e.g., the law of gravity)</td><td>Execution time is about 2070 msec (230 msec for scanning 340 msec for recognition, and 1500 msec for pointing)</td></tr></table>

![](/api/attachments/TNSYXRXV/fulltext/images/181180f92e0f4bb784bf4aba4454ec63946b0a8daa72aa3473fc46b621c6dd4a.jpg)  
Fig. 4. The design of the highest level interface: fun places for a user.

## Hypermedia design

The designer's next responsibility is to assemble a set of hypermedia facilities like nodes (e.g., cards) and links (e.g., buttons) to satisfy user goals. Levels of the networks can be employed, where each level is a collection of nodes satisfying a set of related user goals. The representation is defined by employing graphics, sounds, and emulations that reflect the metaphor. For example, Figure 5 shows an interface that resembles a person hitting baseballs in a stadium, with a coach watching and available for advice. A wooden sound is added at the time of hitting; audience cheers occur when the user hits a home run. Links are used to interconnect nodes. In addition, methods familiar to the user can be simulated. This speeds the learning process. For example, methods like hitting the ball and asking the coach are included in a pop-up menu.

![](/api/attachments/TNSYXRXV/fulltext/images/42daead75915cf88811a37b943b593780bf47f20b1d83d9787d2366aa97f59b5.jpg)  
Fig. 5. The user interface for choosing an angle to hit the baseball.

## Cognitive engineering principles

Documenting design rationales is important for later modification. Associating psychological principles to a design feature is no small task; the designer must first have knowledge of HCI principles. Numerous lists have been published for designing presentations (e.g., graphics) and actions (e.g., keyboards, and mouse) in texts like the Handbook of Human-Computer Interaction [27]. Recently, Blattner et al. [26] and Gaver [37] have recommended principles for using sounds to support human-computer interaction.

Principles may contradict one another. Moran [36] cautions that a collection of guidelines does not add up to a coherent psychological picture. Hence, if a designer tries to follow the principles without guidance, s/he could be easily overwhelmed by their complexity.

In the approach discussed here, the application of principles are guided by Norman's model of HCI as discussed previously. The approach advocates principles that lead to increased efficiency and reduced errors, e.g., the principle of “minimizing motor operations” can be applied to designing keystroke level operations, while the principle of “grouping items into chunks by its functional use” can be applied to organizing menus and the principle of “reducing mental recall by displaying key information” can be applied to designing representations that are easily recognized.

It is therefore necessary for hypermedia designers to learn cognitive engineering principles. In developing their hypermedia project, group members spent two months studying the literature. Applying principles also requires experience, but brainstorming helps to compensate for its lack. Once a designer becomes familiar with the process, s/he can easily sharpen his/her skill and reduces the learning time. Many seminar members commented that examples like those by Carroll and Kellogg were useful in learning principles, because a successful artifact allows extraction of sound principles. Our experience suggests that it is important to compile a list of artifacts and their concomitant design rationales.

![](/api/attachments/TNSYXRXV/fulltext/images/909a2bf706bf4a10dad71c9986c3eba53d0252fa99372099f56838570d963dcf.jpg)  
Fig. 6. Cognitive walkthrough steps [4].

## Artifact engineering result

The result of artifact engineering is a well-defined interface and clear documentation of design rationales. They are added to the result of contextual analysis. The third column of Table 1 shows what design rationales led to the particular solution. Such documentation allows the designer to reevaluate design rationales in later phases if the implementation does not satisfy the user.

## 3.3. Cognitive walkthrough

Cognitive walkthrough is an approach for assessing the learnability of a system. Like structured walkthrough of software engineering, the purpose is to have a group of experts assess the quality of a design prior to its implementation. Figure 6 lists questions that a cognitive walkthrough answers for a particular user action. Note that user actions are derived from the results of artifact engineering; the goal here is to evaluate the interface to ensure its acceptance by the users.

To conduct cognitive walkthrough, a group of experts familiar with cognitive engineering concepts may be employed as the evaluators. They first address question 1: the user goal. They then evaluate how a user would properly carry out actions to meet this goal (questions 2–7). Finally, the team examines the system's responses.

## Design tradeoffs

In the Artifact Engineering phase, cognitive engineering principles are applied to devise the interface of a hypermedia system. In a cognitive walkthrough, some design fault may still be detected; e.g., the designer applied design rationales incompletely or inconsistently, and the designer should reengineer the interface. Another possibility is that there are competing principles in the situation, and a design tradeoff must be made.

As an example, a designer may attempt to minimize user keystroke actions by using function keys to represent a series of commands. But action efficiency requires memorization and recalling of actions. A user may be confused by the increased mental load associated with function keys. The conflicting design rationales can then be partially resolved by a cognitive walkthrough in which the experts attempt to agree on the best tradeoff. However, the later usability testing provides the final and best solution to this conflict.

## Define usability goals

In order to assess the quality of the resulting implementation, it is necessary for clear definition of usability goals. They can be qualitative/descriptive, such as user enjoyment and satisfaction, or quantitative/prescriptive, such as a range of possible user errors, time for problem solving, and time for keystroke actions. Furthermore, user errors can be classified into motor errors (like incorrect keystrokes) and mental errors (like formulating wrong intention). Target usability goals can be set, such as no keystroke errors.

During the project's implementation the team also experimented with cognitive parameters for predicting the performance of expert users. Research in cognitive engineering has generated a list of metrics for performance prediction. Examples are shown in Figure 7. To apply these metrics, the designer must first analyze a user's actions and assign the theoretic metric to each motor, perceptual, and mental metrics. The sum of the metrics then becomes the performance goal. For example, “going to a ball park” requires the user to scan the display and position the mouse to the icon representing the ball park. The theoretic time for completing this is the sum of “scanning the display” time, “recognition” time, and “pointing the mouse” time. This number becomes the usability goal.

![](/api/attachments/TNSYXRXV/fulltext/images/697cabf5977da2758c9cf81e1c057b14dc7ad50b042e73190322661290876e62.jpg)  
Fig. 7. Summary of cognitive engineering parameters.

## Cognitive walkthrough result

Cognitive walkthrough yields a clear understanding of how and why a system should work. It also generates a list of clearly stated performance goals. Our experience in using the cognitive parameters reveal that the prediction is often inaccurate in comparison with actual user performance: the difficulty stemming from the fact that many motor and perceptual activities are subtle and can be detected only observing the user performing the actual task. A prediction, therefore, serves only as guidance for making design trade-offs.

## 3.4. Implementation, usability testing, and iterative design

The final phase is to implement the design and conduct usability testing. Choosing a proper tool is critical; a review of hypermedia tools can be found in trade magazines and texts like HyperText and HyperMedia. In addition to the technical features of a tool, one should consider the technical skill of the developers and the technological adoption strategy of the company. The developers should be given enough time to learn the tool.

Usability testing should follow the implementation. Rapid heuristic evaluation is applied during the first few iterations to identify major problems: a group of potential users is recruited to test the system. When they are observed to be having difficulty using the system, the designer should reevaluate the usability goals to see whether the performance is acceptable. If poor performance is due to poor design, the designer can evaluate the design document. The designer can then iterate the design phases and modify the design for the next implementation.

Comprehensive usability testing should be conducted at the end of the project. To evaluate whether user performance match the cognitive parameter prediction, users must be trained until they become skilled in using the system. Only then can actual performance be compared to proposed goals. Video taping user actions may also be useful for understanding why there is difference between predicted and actual performances.

Two children of age eight were recruited for heuristic evaluation after the project was completed. Our experience shows it is difficult for the original team of software engineers to perform usability testing. Its methodology is based on psychology and the process is often detailed, cumbersome, and repetitive, as opposed to the creative process of designing the system. Hence, we suggest that usability testing should be conducted by a separate team of experts.

## 4. Conclusion

In this paper a user-centered approach to designing hypermedia systems is discussed. It advocates the use of cognitive engineering principles. Scenario-based contextual analysis helps the designer identify the objects and functions and their relationships, user goals, and methods to accomplish the goals. The designer should emphasize spatiality, color, graphics, and sound as an integral part of the user knowledge. In artifact engineering the designer specifies how and why the hypermedia tools can be utilized to support the user. Cognitive walkthrough enables the designer to assess the learnability in a cost-efficient manner; criteria for measuring it are identified and can be applied later in system testing. In the final phase, a hypermedia system is created and usability testing is conducted. Rigorous investigation of user cognitive needs assures a system closely matching user expectations. Still, iterations of the entire approach are needed if user dissatisfaction is detected.

Our experience in designing hypermedia systems has revealed several interesting points. The project teams believe that it could reduce time and errors, since design is now guided by cognitive theories. An informal design language allows designers to communicate easily with one another, and gain from other project teams' experience. Moreover, defining measurable behavior goals allows the designer to evaluate and refine the design. The approach is particularly useful to hypermedia design, but its usefulness could be limited in designing traditional text-based systems, because substantial time and effort invested in understanding and applying cognitive principles may not pay off.

We also believe there is a need for continuous collection of user feedback. Such collection reveals contextual factors not considered in the approach. These include emotional factors, such as stress, and work related problems, such as pressures from colleagues. Discovering them enables the designer to tailor the system to address many situational, subtle problems that cannot be anticipated in the early stage of the design process.

Finally, application of cognitive research results to designing computer systems remains a hotly debated issue: little laboratory research has been related to real work settings. To further our knowledge in this field, cognitive science and theoretical HCI principles must be emphasized in the curriculum for training system analysts and designers. The design rationales must also be documented clearly so any design decision and its effect can be traced. Such an investment is worthwhile, because today's complicated HCI technology demands that software engineers have knowledge in human psychology in order to develop systems that are functional, learnable, and usable.

## 5. References

[1] A. Maclean, R.M. Young, and T.P. Moran, “Design Rationale: The Argument behind the Artifact,” Proceedings of CHI'89, Human Factor in Computing Systems, 1989, pp. 247–252.

[2] A. Marcus, A. and A. van Dam, “User-Interface Developments for th Nineties,” Computer, September 1991, pp. 49–57.

[3] B. Shneiderman, Designing the User Interface, Addison-Wesley Publishing Company, Reading, Massachusetts, 1987.

[4] C. Lewis, P. Polson, C. Wharton, and J. Rieman, "Testing a Walkthrough Methodology for Theory-Based Design of Walk-Up-and-Use Interfaces," Proceedings of CHI'90, Human Factors in Computing Systems, 1990, pp. 235–241.

[5] D. Wixon, K. Holtzblatt, and S. Knox, “Contextual Design: An Emergent View of System Design,” Proceedings of CHI'90, Human Factors in Computing Systems, 1990, pp. 329–336.

[6] D.A. Carlson and S. Ram, "HyperIntelligence: The Next Frontier," Communications of the ACM, Vol. 33, No. 3, March 1990, pp. 311-321.

[7] D.A. Norman, “Cognitive Engineering,” in User Centered System Design, D.A. Norman and S. Draper, eds., Lawrence Erlbaum Associates, Hillsdale, NJ, 1986, pp. 31–61.

[8] D.G. Gould, S.J. Boies and C. Lewis “Making Usable, Useful, Productivity-Enhancing Computer Applications,” communications of the ACM, Vol. 34, No. 1, January, 1991, pp. 74–85.

[9] E. Yoder and T.C. Wettach, “Using Hypertext in a Law Firm,” Hypertext '89 Proceedings, 1989, pp. 159–167,

[10] F.G. Halasz, “Reflections on Notecards: Seven Issues for the Next Generation of Hypermedia Systems,” Communications of the ACM, Vol. 31, No. 7, July 1988, pp. 836–852.

[11] F.R. Campagnoni and K. Ehrlich, “Information Retrieval Using a Hypertext-Based System,” ACM Transactions on Information Systems, Vol. 7, No. 3, July, 1989, pp. 271–291.

[12] H. Van Dyke Parunak, “Hypermedia Topologies and User Navigation,” Hypertext '89 Proceedings, 1989, pp. 43–50.

[13] J. Conklin, “Hypertext: An Introduction and Survey,” Computer, Vol. 20, no. 9, September, 1987, pp. 17–41.

[14] J. Grudin, “The Case against User Interface Consistency,” Comm. o the ACM, Vol. 32, 1989, pp. 1164–1173.

[15] J. Johnson, T. Roberts, W. Verplank, D. Smith, C. Irby, M. Beard, and K. Mackey, "The Xerox Star: A Retrospective," Computer, September, 1989, pp. 11–26.

[16] J. Lohse, “A Cognitive Model for the Perception and Understanding of Graphs,” Proceedings of CHI'91, Human Factors in Computing Systems, 1991, pp. 137–144.

[17] J. Nielsen, Hypertext and Hypermedia, Academic Press, Inc., Sandiago, CA., 1990a.

[18] J. Nielsen, “The Art of Navigating through Hypertext,” Communications of the ACM, Vol. 33, No. 3, March, 1990b, pp. 297–310.

[19] J. Nielsen, “Traditional Dialogs Design Applied to Modern User Interfaces,” Communications of the ACM, Vol. 33, No. 10, 1990c, pp. 109–118.

[20] J.M. Carroll and M.B. Rosson “Deliberated Evolution: Stalking the View Matcher in Design Space,” Human-Computer Interaction, Vol. 6, No. 3 & 4, 1991, pp. 281–318.

[21] J.M. Carroll, R.L. Mack and W.A. Kellogg, “Interface Metaphors and User Interface Design,” in Handbook of Human-Computer Interaction, M. Helander ed., Elsevier Science Publishers B.V. (North Holland), 1988, pp. 67–85.

[22] J.M. Carroll and W.A. Kellogg “Artifact as Theory-Nexus: Hermeneutics Meets Theory-based Design,” Pro-

ceedings of CHI'89, Human Factors in Computing Systems, 1989, pp. 7–14.

[23] J.R. Anderson, Cognitive Psychology and its Implications, 3rd edition, W.H. Freeman and Company, New York, N.Y., 1990.

[24] J.R. Olson and G.M. Olson, “The Growth of Cognitive Modeling in Human Computer Interaction since GOMS,” Human Computer Interaction Vol. 5, No. 2 and 3, 1990, pp. 221–266.

[25] L. deYoung, “Hypertext Challenges in the Auditing Domain,” Hypertext '89 Proceedings, 1989, pp. 169–179.

[26] M. Blattner, D.A. Sumikawa, and R.M. Greenberg, "Earcons and Icons: Their Structure and Common Design Principles," Human-Computer Interaction, Vol. 4, No. 1, 1989, pp. 11–44.

[27] M. Helander, Handbook of Human-Computer Interaction, Elsevier Science Publishers B.V. (North Holland), 1988.

[28] M.B. Kinzie and R.L. Berdel, “Design and Use of Hypermedia Systems,” ETR&D, Vol. 38, No. 3, 1990, pp. 61–68.

[29] M.D. Phillips, B.S. Howard, H.L. Ammerman, and C.M. Fligg, Jr., "A Task Analytic Approach to Dialogue Design," in Handbook of Human-Computer Interaction, M. Helander ed., Elsevier Science Publishers B.V. (North Holland), 1988, pp. 835–857.

[30] N. Hammond and L. Allinson, Proceedings of CHI'88. Human Factors in Computing Systems, 1988, pp. 269–273.

[31] P. Christiansson, “Building a City Advisor in a Hypermedia Environment,” Environment and Planning B: Planning and Design, Vol. 18, 1991, pp. 39–50.

[32] P.T. Zellweger “Scripted Documents: A Hypermedia Path mechanism,” Hypertext '89 Proceedings, 1989, pp. 1–14.

[33] R.H. Trigg, “Guided Tours and Tabletops: Tools for Communicating in a Hypertext Environment,” ACM Transactions on Information System Vol. 6, No. 4, October 1988, pp. 398–414.

[34] R.M. Young, and P.J. Barnard, “The use of scenarios in human-computer interaction research: Turbo-charging the tortoise of cumulative science,” Proceedings of CHI + GI 1987, Human Factors i Computing Systems, pp. 291–296.

[35] S. Card, T.P. Moran and A. Newell, The Psychology of Human-Computer Interaction, Lawrence Erlbaum Associates, Hillsdale, NJ, 1983.

[36] T.P. Moran, “An Applied Psychology of the User,” Computing Surveys Vol. 13, No. 1, 1981, pp. 1–12.

[37] W.W. Gaver, “The SonicFinder: An Interface that Uses Auditory Icons,” Human-Computer Interaction, Vol. 4, 1989, pp. 67–94.
