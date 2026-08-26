---
otero_id: 24557
otero_key: "YCCJ3QKK"
title: "The Architecture of an Information System for the Support of Alternative Generation"
authors: "Kenneth R. MacCrimmon; Christian Wagner"
year: "1991"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1991.11517929"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Architecture of an Information System for the Support of Alternative Generation

Kenneth R. MacCrimmon & Christian Wagner

To cite this article: Kenneth R. MacCrimmon & Christian Wagner (1991) The Architecture of an Information System for the Support of Alternative Generation, Journal of Management Information Systems, 8:3, 49-67, DOI: 10.1080/07421222.1991.11517929

To link to this article: http://dx.doi.org/10.1080/07421222.1991.11517929

![](/api/attachments/YCCJ3QKK/fulltext/images/d4ce528d17ef575971b15e95307d0dfd8a49b6919d95649a4b421b21f6b405af.jpg)

Published online: 18 Dec 2015.

![](/api/attachments/YCCJ3QKK/fulltext/images/cea1b30b1fe5f216b21f699ad7c982d08420f59c8834aa435e0aab4332cdb94e.jpg)

Submit your article to this journal ↗

![](/api/attachments/YCCJ3QKK/fulltext/images/6b4aab089ee0fe6b2855fbf25cdb200011ef544bef76879019bcc1e92c777bea.jpg)

View related articles ↗

# The Architecture of an Information System for the Support of Alternative Generation

KENNETH R. MACCRIMMON AND CHRISTIAN WAGNER

KENNETH R. MACCRIMMON is the E.D. MacPhee Professor of Management in the Faculty of Commerce and Business Administration at the University of British Columbia. He has also been on the faculty at Carnegie Mellon University and Northwestern University where he was the J.L. Kellogg Distinguished Professor of Strategy and Decision. His research work ranges from formal axiomatic decision theories to laboratory experiments on information processing behavior; he is coauthor of the recent book, Taking Risks: The Management of Uncertainty. For more than twenty years, he has been researching and teaching courses on creativity and problem solving. Currently, he is on the editorial boards of several journals including the Journal of Risk and Uncertainty and the Journal of Behavioral Decision Making and has just completed a three-year term on the National Science Foundation panel for the Decision, Risk, and Management Science Program.

CHRISTIAN WAGNER is Assistant Professor of Information Systems in the School of Business at the University of Southern California. He received a Ph.D. in Business Administration from the University of British Columbia in 1989. He also holds an undergraduate and a graduate degree in industrial engineering from the Technical University Berlin. His research interests include intelligent database design and computer support for problem solving and creativity. He recently gave talks on computer-supported creativity at international conferences in Belgium and Japan.

ABSTRACT: The pre-choice stages of the problem solving process are more difficult to support through information systems than choice itself. Systems that facilitate problem formulation and solution finding are typically either expert system programs with narrow application domains or programs dealing with easily quantifiable problems. In contrast, this paper introduces a decision support system, GENI, that operates independent of domain, aiding the user in general problem solving tasks. The system's purpose is to support the problem solving process, rather than be a substitute for the human problem solver, by providing structure and by using different stimuli to prompt the user for data input. To deal with broad classes of complex qualitative problems, no single processing mode is sufficient. Hence the techniques in GENI differ mainly

An earlier version of this paper was originally published in the Proceedings of the Twenty-Fourth Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1991). This research was supported in part by the Social Sciences and Humanities Research Council of Canada and by the U.S. National Science Foundation (Grant SES–9016305). We thank Nick Keenan for his assistance in developing portions of the software described in the paper.

in the interface, that is, the types of stimuli displayed, and the types of data recorded. GENI's user interface is built around a standard dialog function that can be modified by means of parameter settings. Experimental results show that differences in the interface content can lead to significant differences in problem-solver performance.

KEY WORDS AND PHRASES: decision support system, problem solving, problem formulation, alternative generation, idea generation, idea generation software.

## 1. Background

MOST DECISION SUPPORT SYSTEMS ARE “CHOICE SUPPORT SYSTEMS.” They help in selecting among existing alternatives. Choice, however, is only one aspect of decision making and problem solving. In fact, choice is one of the easier parts of the problem-solving process because the theoretical underpinnings are strong and because many choice techniques use quantitative tools (e.g., probabilities and utilities) whose computerization is straightforward.

The opposite conditions hold for problem formulation and alternative generation, the earlier steps of the problem solving process $[13, 32, 35]$ . Supporting pre-choice aspects of problem solving is difficult because little theory exists to guide problem formulation and alternative generation. Furthermore, computerization is difficult because the objects to be manipulated are problem elements such as goals, facts, processes, objects, or solution alternatives that are not easily quantifiable. For instance, solving the problem of airline no-shows (i.e., travelers who make reservations but then do not show up for the flight) can only be quantified once solution alternatives have been found. In this example, one needs to have generated the alternative of “overbooking” before one considers trading off the cost of having too many passengers show up against the cost of too few showing up. Recently several authors have argued for the development of DSS to support the generation of solution alternatives $[12, 26, 36, 37]$ , but only a few implementations exist. A DSS for problem formulation was suggested by Ata Mohammed et al. $[2]$ but it deals mainly with quantifiable problem elements.

In this paper we describe the GENI program, which is a DSS that supports problem formulation and alternative generation for managerial problems such as the airline no-show problem. The paper focuses on the interface because the user interface, through the stimuli presented on the screen and the facility for user inputs, is the most important element of the software. Thus, most of the paper deals with design aspects such as screen design, module design, and with the structure of the dialog between the user and the program. The last part of the paper briefly describes empirical evaluations of the software with respect to the effectiveness of different interface types, concentrating on idea generation. These results show that some interface designs are better than others in increasing the idea yield in problem-solving sessions. We suggest characteristics to which these differences may be attributed but do not speculate in this paper on theories of ideation that may explain performance differences. Our argument is more pragmatic, focusing on the differences due to the interface between the program and the user.

## 2.1. General Working Principle of Idea Generation Software

EXISTING SOFTWARE FOR IDEA GENERATION, including the few commercially available packages, all share the same weakness, namely limited processing ability. The systems are targeted to support problem solving processes, especially idea generation, for a variety of problem domains. This task represents a considerable challenge since it requires that systems be knowledgeable in many problem contexts or that they be “domain-independent.” Studies in expert systems suggest the difficulty of developing an adequate knowledge base in a single area, so to construct such knowledge bases across a number of different areas becomes an overwhelming task. Consequently, knowledge-based systems have been restricted to narrow and deep problem domains and have lacked broad applicability. Domain-independent systems are ignorant with regard to any specific problem area but can provide general advice, instructions, and support, regardless of the problem domain. The drawback of domain-independent systems is that they do not have the necessary knowledge to reason about any specific problem. Most available idea generation programs fall into this category. For differences in the types of idea generation software see $[24]$ .

Given its lack of problem domain knowledge, idea generation software differs from typical decision support software in that it performs very little or no idea processing, as shown in figure 1. Consequently, idea generation software has to derive its effectiveness from other features: namely, its ability to provide structure to the problemsolving process through useful instructions and stimulating prompts.

## 2.2. GENI Software Overview

The GENI (for GENERating Ideas) software has been developed as a package to support all phases of the problem solving process: problem formulation, alternative generation and evaluation, and choice. The program has been targeted to support the early stages of problem solving, not to solve the problem independently. The program is focused on assisting individual problem solving, not group problem solving. Therefore, all the problem formulation and idea generation techniques have been designed or adapted as individual problem solving techniques. Currently no provisions have been made for group procedures.

In working on a particular problem, the user has to specify the problem and has to develop alternatives. GENI facilitates these tasks by providing structure and stimuli. In this respect, it is similar to other idea generation software packages that are domain-independent and different from systems such as GPS $[25]$ , Bacon $[19]$ , or other knowledge-based systems. Given its lack of domain specificity, GENI is applicable to various managerial problems (such as airline no-shows) but is not very knowledgeable in any specific problem area. The system's “domain” of expertise is problem structuring and idea generation $[24]$ . However, GENI was written in Prolog so that it can be augmented to contain domain-specific knowledge.

Decision Support System  
![](/api/attachments/YCCJ3QKK/fulltext/images/72ddc40e67c7d52f11a11273b88e23786ab3f8a5052f190f6f157a7afd5cbc8c.jpg)

Idea Generation Software  
![](/api/attachments/YCCJ3QKK/fulltext/images/bedcda525b5e48033326bf98be0422cddbf49f3973893eaa79994b69273fadfa.jpg)  
Figure 1. Decision Support versus Idea Generation Software

## 2.3. Problem Solving Support

## 2.3.1. Sources of Techniques

The lack of an accepted theory has not deterred the development of various methods directed at supporting problem formulation and idea generation. Some methods, such as brainstorming, have been widely used and evaluated while others have received little use and no critical evaluation at all. GENI's design is based on a variety of problem formulation and idea generation methods. GENI's techniques make these methods amenable to computerization, yet retain the methods' key elements. Therefore, the following discussion of GENI's techniques will describe both the techniques as well as the problem solving principles or methods upon which they are based.

## 2.3.2. Problem Formulation Techniques

Even though there is no formal theory dealing with problem formulation, there are prescriptions that seem helpful. Some prescriptions are very general, such as the suggestion that effective problem formulation should center on “asking the right questions” [14, 31]. Other prescriptions are somewhat more specific, such as filling in tables based on a distinction between “what is the problem?” and “what is not the problem?” [17]. Other problem solving principles, such as “make implicit assumptions explicit,” can be found in MacCrimmon and Taylor [21] or Rosenhead [30].

While compatible with such general prescriptions, GENI's problem formulation module is based more directly on the key components underlying any problem solving activity. Common to all problems are the following major problem elements: (a) goals, (b) beliefs/assumptions, (c) objects and processes, and (d) solution alternatives. The GENI program has procedures for eliciting all these elements from the user. Let us briefly consider each of these components and their role in problem formulation.

The specification of goals is intended to guide the decision maker in developing a better understanding of what type of solution is needed. In most concepts of problem solving, goals play a major role—such as in the concept of problem solving as eliminating a discrepancy between a current state and a desired state $[28, 29]$ . The specification of the desired state is greatly facilitated by a goal-specification module. Typical goals in the no-show problem are “increase profit,” “maintain customer satisfaction,” and “improve utilization level.”

Belief specifications permit the decision maker to articulate currently held beliefs, such as “If full-fare travelers are charged for a change in their reservations, they will switch airlines.” Once such beliefs are made explicit, they can be questioned and modified, or used as constraints to be met by existing solution alternatives. Belief specification can also be used to record current assumptions regarding a problem’s source, such as, “The passenger didn’t show due to delays in traffic.” Specification and testing of hypotheses is one of the central tasks in any diagnosis problem.

The description of objects and processes helps in specifying the structure and function of the system under scrutiny. Function and structure specifications are used in design $[3, 7]$ as well as in diagnosis $[10, 15]$ . Therefore, an outlet for the specification of these problem elements was considered important. In the airline no-show example, typical objects would be “seat,” “passenger,” and “agent”; typical processes would be “reserving,” “paying,” and “not showing.”

The final part of the problem formulation module asks the user to list already known solution alternatives. Although the main objective of the overall system to is to help the user to develop such alternatives, they are nevertheless requested up front in order to free the decision maker's mind from preconceptions of known, possibly mundane solutions. In this way the user can focus more attention on the search for new, original alternatives [27].

As noted earlier, the user is presented with a standardized screen format for each of the techniques. Thus, as an example of all the problem formulation techniques, figure 2 shows the main screen of the processes description technique.

## 2.3.3. Alternative Generation Techniques

GENI's alternative generation techniques are derived from key concepts (we hesitate to use the term “theories”) that have been advanced to characterize creative problem solving. Among the key processes that have been suggested as underlying the generation of creative alternatives are: free thinking, connecting disparate contexts, variations of a theme, combining problem elements, and deriving means from ends [20]. The GENI techniques based on these processes are: (a) Brainstorming, (b) Metaphoric Connections, (c) Relational Combinations, (d) Juxtaposition, and (e) LOTO Modifications. A brief description of each technique, and its underlying rationale, follows.

Brainstorming is an implementation of the free-thinking principle, originally proposed by Osborn [27]. Even though our implementation is for a single person rather than a group, the same basic brainstorming principles are emphasized. The technique's instruction screen urges the user to defer judgment, think wildly, and produce a large quantity of ideas. A short description of the problem and a “headline” serve as a focus. The ideas generated by the user are shown in a separate window so that the user can build upon ideas previously developed—another feature of the brainstorming approach.

![](/api/attachments/YCCJ3QKK/fulltext/images/48482e17438594d301d49eaa92cc813ebe308997c47641ad73e707bbbd08375f.jpg)  
Figure 2. Process Description Technique

Metaphoric Connections are related to a technique used by de Bono [11] that encourages the user to develop ideas by connecting remote stimuli, such as dictionary words, to the focal problem. The underlying rationale is similar to the bisociation concept of Koestler [18]. The remote stimuli provided in the GENI program are several lines of modern poems that have been specially chosen for their imagery. About fifty short poems are stored in GENI and are retrieved randomly whenever the user presses a particular function key. By seeing the poem fragment and the problem statement together, the user is encouraged to think about connections between the two contexts and to type in ideas that the poem suggests for the focal problem.

Ends-Means Chains focus on the importance of goals in the problem solving process. The user's attention is directed toward deriving means from ends, that is, developing lower-level goals from higher-level goals. A previously generated goal is shown, together with the request to think of a means to achieve that goal. A subsequent screen presents the user, on a random basis, with some of the means that have been input, and asks the user to generate means of means, thus extending the goal chain to lower levels. The lower levels of a goal chain are more “alternative-like.”

Relational Combinations are an extension of Crovitz's [9] "relational algorithm" which provides a structure for combining problem elements. The implementation in GENI uses the list of objects and processes that the user specified during the problem formulation phase, plus entries drawn from a list of relational words that are permanently stored in the program's data files. These elements are put into sentences of the form: "PROCESS by means of OBJECT-1 relational word OBJECT-2" (for example, MONITORING by means of PHONE before DEPARTURE DATE). These structures are displayed for the user who is thereby stimulated to suggest new ideas. At any time the user can independently request a change in the display of: (a) the process, (b) the object words, and (c) the relational word.

Juxtaposition is also based on combining problem elements. Unlike the highly structured Relational Combinations technique, this technique simply presents problem elements (defined in the problem formulation phase) together on a single screen. Up to three different problem elements, such as goals, processes, or beliefs, can be displayed simultaneously. Any single element can be replaced on a random basis by selecting the appropriate window and pressing a function key. As with the other techniques, the user is encouraged to think about the displays so as to form a new idea.

LOTO Modifications are based on the concept of creating new ideas by generating variations on a theme $[16]$ . The user is presented, randomly or by choice, with an alternative that was input by the user earlier in the program session (either during the problem formulation phase or from one of the other alternative generation techniques). A transformation term (such as “simplify” or “counteract”) is presented and the user is asked to modify a focal alternative in a way suggested by that term. About fifty transformation terms are available. The user can choose to see a new term or a new focal alternative, drawn from the existing pool of ideas, at any time. “LOTO” is an abbreviation of for “List Of Transformation Operators.” The list is an extension of Osborn’s $[27]$ and Arnold’s $[1]$ checklists.

The standard screen format for all the techniques is shown in figure 3 using the Metaphoric Connections technique as an example.

## 3. Architecture

## 3.1. Program Structure

GENI'S OVERALL STRUCTURE IS ILLUSTRATED in figure 4. The program is menu-driven and uses pull-down windows similar to many other microcomputer software packages. The main menu contains six groups of functions. Group 1 contains the main problem formulation procedures. Group 2 consists of all the techniques that assist directly in idea generation. Group 3 includes printing and editing functions. Group 4 represents the location of the evaluation methods. Group 5 contains the LOTO idea transformation technique. Finally, in Group 6, we find some housekeeping routines to allow the definition of a new problem, storing and recalling of problems, as well as import and export of problem files from and to spreadsheets.

The order of the groups is not arbitrary. Problem-formulation techniques precede idea generation techniques which precede evaluation techniques. Print and edit techniques were moved before evaluation to allow listing and rephrasing of ideas prior to evaluation. The modification techniques follow evaluation to permit improvements of those ideas that were found to be best. Within the idea generation module, techniques are ordered by complexity, which is determined by the number of inputs and the number of different screens. Although the order of techniques suggests a logical progression of the problem solving process, the program user is free to use the techniques in any order.

If the user tries to activate an idea generation technique that requires some prior data inputs, the program will first activate a problem formulation technique to generate these inputs. For example, if the user wants to use Relational Combinations but has not specified any objects or processes, GENI will first activate the object and process formulation modules before invoking the Relational Combinations technique.

![](/api/attachments/YCCJ3QKK/fulltext/images/6059269e6da4ce0bb9856f19fc00d484e61b61f8185aaf47da7fdd28fcba0c51.jpg)  
F1: Instructions F2: Edit F7: New poem At least 3 ideas needed to exit  
Figure 3. Metaphoric Connections Technique

![](/api/attachments/YCCJ3QKK/fulltext/images/c118c12248a004c7bdaadd223a9c8e9e005cba8e10061e05304582fb2595c2e9.jpg)  
Figure 4. GENI—Program Structure

## 3.2. Data Types: Inputs and Outputs

The GENI software stores two basic types of data: (1) resident text information, such as instructions, which are fixed for all problems, and (2) problem-specific data which includes all the user inputs. In addition to instructions and help text, the resident information also includes stimulus information, namely poems for Metaphoric Connections, modifier concepts for LOTO, and relational words for Relational Combinations.

The problem-specific data can take any of the following forms: problem description, headline, goals, beliefs, objects, processes, alternatives, and ideas. The problem description is a verbal description of the problem; an example is given in the appendix. The headline is a one-line problem synopsis of the essence of the problem. In experimental work, the problem description and the headline are usually provided by the experimenter, whereas in nonexperimental use of GENI, the users may work on problems of their choice and hence provide their own description and headline.

The other problem-specific data types are strictly based on user inputs and most exist for the purpose of recording the information provided during problem formulation. Each data type is kept in a separate data structure, but data items can be reclassified if desired. If, for example, the user typed in a sentence intended to describe a belief, but later wants to treat it as a goal, this reclassification is easily done. Ideas are recorded with the idea generation functions. All the problem formulation inputs such as goals or objects can be used as stimuli to suggest ideas. Figure 5 shows all problem formulation and idea generation techniques with their corresponding data types for stimuli and user inputs.

Figure 5 depicts screen numbers (e.g., 0, 1, 2), indicating that all techniques incorporate multiple screens. Each technique contains a Screen-0, with instructions for the use of the technique (see figure 6 for an example). Each technique also includes a help screen that the user can call up. Techniques such as “Goals” incorporate one further screen, which contains stimuli and allows the input and display of responses. As figure 5 indicates, the Goals technique will display the problem description, a problem headline, plus previously inserted goals, and will request the input of further goals. A more complicated technique, such as Ends-Means Chains will contain additional screens. Ends-Means for instance will first invoke the Goals screen to facilitate the input of goals, if the user did not specify any goals previously. It will then invoke Screen-1 which shows a single goal, the problem headline, plus any previously inserted means (alternative ways to achieve that goal). Screen-1 also asks the user to type in any other possible ways to achieve the goal. When the user decides to move on, Screen-2 will be invoked, with its prompts and its request for the input of “means of means,” or even lower level goals.

## 4. User Interface

## 4.1. Elements of the User Interface

WE DEFINE THE “INTERFACE” AS THE PROGRAM FACILITY that is responsible for the dialog with the user. Therefore, the interface consists of all instructions, help features, system prompts, and features for data inputs. Interface designs can differ in a variety of characteristics, including medium (i.e., visual, aural), content, spacial location on the screen, or timing. Broad interpretations of “interface” include both form and content. Less broad interpretations of the interface concept may exclude the content and instead focus exclusively on format characteristics (e.g., location, timing) (see, for example, [4]).

In GENI, information is presented to the user in a standard format; that is, each technique uses the same type and location of screen windows. Thus, the key difference between interfaces is the content of instructions and prompts and the type of information requested as user input. This difference in interface content is the main distinguishing feature between techniques, since techniques do not process user inputs and since storage and editing capabilities are identical for all techniques.

<table><tr><td>TECHNIQUE</td><td>SCREEN</td><td>RESIDENT STIMULUS</td><td>PROBLEM- RELATED STIMULUS</td><td>USER INPUT</td></tr><tr><td rowspan="2">All techniques</td><td>0</td><td>Instructions</td><td></td><td></td></tr><tr><td>Help</td><td>Help information</td><td></td><td></td></tr><tr><td>Goals</td><td>1</td><td></td><td>Problem description Headline, (Goals)</td><td>Goal</td></tr><tr><td>Objects</td><td>1</td><td></td><td>Problem description Headline, (Objects)</td><td>Object</td></tr><tr><td>Processes</td><td>1</td><td></td><td>Problem description Headline, (Processes)</td><td>Process</td></tr><tr><td>Beliefs</td><td>1</td><td></td><td>Problem description Headline, (Beliefs)</td><td>Belief</td></tr><tr><td>Alternatives</td><td>1</td><td></td><td>Problem description Headline, (Alternatives)</td><td>Alternative</td></tr><tr><td>Brainstorming</td><td>1</td><td></td><td>Problem description Headline, (Ideas)</td><td>Idea</td></tr><tr><td>Metaphoric Connections</td><td>1</td><td>Poem</td><td>Headline, (Ideas)</td><td>Idea</td></tr><tr><td rowspan="3">Relational Combinations</td><td>Objects</td><td colspan="3">see above Objects technique</td></tr><tr><td>Processes</td><td colspan="3">see above Processes technique</td></tr><tr><td>1</td><td>Relational word</td><td>Object and Processes Headline, (Ideas)</td><td>Idea</td></tr><tr><td rowspan="3">Ends-Means Chains</td><td>Goals</td><td colspan="3">see above Goals technique</td></tr><tr><td>1</td><td></td><td>Goal, Headline, (Means)</td><td>Means (=Idea)</td></tr><tr><td>2</td><td></td><td>Means, Headline (Means of means)</td><td>Means of means (=Idea)</td></tr><tr><td rowspan="2">Loto</td><td>Brainstorming (or other)</td><td colspan="3">see above Brainstorming (or other) technique</td></tr><tr><td>1</td><td>Loto Modifier</td><td>Headline, Idea, (Ideas)</td><td>Idea</td></tr><tr><td rowspan="3">Juxtaposition</td><td>Brainstorming (or other)</td><td colspan="3">see above Brainstorming (or other) technique</td></tr><tr><td>Goals (or other)</td><td colspan="3">see above Goals (or other) technique</td></tr><tr><td>1</td><td></td><td>any 3 stimuli</td><td>Idea</td></tr></table>

Figure 5. Techniques and Corresponding Data Types

![](/api/attachments/YCCJ3QKK/fulltext/images/34d1b0337d5f3aa4378cccebfd71d1c79ed95470b58ab5f60a22affe4f8c557e.jpg)  
Figure 6. Metaphoric Connections Instruction Screen

## 4.2. Module Structure

Much of the design effort for GENI went into the module structure. In the module design we considered effectiveness and efficiency of the user dialog, as well as program-development efficiency. To improve user performance, we designed a “standard” screen, shown in figure 7. The same screen is used in all problem formulation and idea generation/modification functions. The window definitions are as follows:

Window 1. Problem headline;

Window 2. Name of technique and short instructions;

Window 3. Main technique prompt, e.g., short problem description;

Window 4. List of previous user inputs;

Window 5. Current user input;

Window 6. Summary of input commands;

Window 7. Additional system prompts (optional).

The Metaphoric Connections screen of figure 3 may serve as a specific example of this general screen layout. The screen in figure 3 shows on top (Window 1) the headline "airline noshows." Below that, in Window 2, appears the technique name "METAPHORIC CONNECTIONS." Further down on the left side, Window 3 contains a few lines of a poem as a prompt for the user. To its right, Window 4 shows two previous user inputs ("YOUR IDEAS"). Window 5, directly below Windows 3 and 4, is reserved for the current user input ("Idea:"), while Window 6, on the bottom of the screen, contains a few function key definitions. Window 7 is not used in the technique. User inputs always appear in Window 5, when the user is typing them in. Once the <return> key is pressed, the system confirms the input by moving it to Window 4. Because of this standardization, the user always knows where to expect new prompts by the system and where to see his or her own inputs.

A standardized screen definition is not only easier for the user to understand, it also simplifies the interface design. The program contains only one module for all problem formulation and idea generation techniques. When the user requests a particular technique, a standardized dialog-function module is activated with parameter settings that configure the module as requested by the user. The following parameters may be varied: fixed stimuli (including instructions, titles, prompt for input, and help); variable stimuli (e.g., problem description or goals); and the type of user input (e.g., idea). Fixed stimuli are identical for all problems, variable stimuli differ by problem. The following instruction represents part of a screen definition:

fcn(process,[2,3,6],[1,3,4],[headline,object,process],mainmenu).

This function specification (fcn) configures the module for inputs of type “process.” It identifies Windows 2, 3, and 6 as the location for fixed stimuli (instructions and titles) and Windows 1, 3, and 4 as the location for variable stimuli, namely the “headline” (1), previously recorded objects (3), and previously recorded activities (4). The last term in the definition indicates that upon termination of the function, the program returns control to the main menu. Information pertaining to the type of input to be recorded and information on the help text are stored separately.

![](/api/attachments/YCCJ3QKK/fulltext/images/f123882faf79480d78eee3f4ad4f61309f25512f42a70b457e5c40826aadd5f6.jpg)  
Figure 7. GENI Screen Design

An earlier version of the program, INVENTOR, demonstrated at a NATO Advanced Research Workshop [22], did not incorporate this standardized design. Consequently, much more code was expended on largely repetitive interface design (more than two-thirds of the total code was attributed to dialog functions), a result very similar to the findings of Sutton and Sprague [33]. The change to the standard screen design became necessary when the program's size made compilation impossible. The new design not only freed memory and facilitated program modifications, it also shortened the task of adding new techniques.

## 4.2. Control Flow

Another critical aspect of the standardized design is the changeable control flow. The previously illustrated “fcn” returns control finally back to the main menu. In this case, the fcn codifies a “single screen” technique. In contrast, some techniques, for instance Ends–Means Chains, contain at least two screens. Two fcn’s are then required with the first one activating the second one. The first fcn configures the standard input module to accept means. It also specifies that once Ends–Means is completed, the standard input module shall be activated with the means2 setting, to collect means of means. Upon completion of means2, control will go back to the main menu.

fcn(meansends,[2,6,4],[1,3,0],[headline,problem,none],means2).  
fcn(means2,[2,6,3,4],[1,3,0],[headline,problem,none],mainmenu).

The control flow specification through fcn's is very useful in program maintenance. Since the control flow is not determined by the order of program lines, flow changes require only minimal program changes (only in the fcn's). Furthermore, the variable control flow feature permits change in the sequence of execution of functions during a program run. For example, if the user chooses the Ends-Means function, but has not specified any goals, Ends-Means cannot be executed. In that case, the standard input function is called with another fcn, one that enables it to record goals and thereafter passes control back to the Ends-Means function. The ideas for the control flow variation as well as for the input module modifications are based on the work of Carlson and Motz [6].

## 4.3. Input Cycle

The input–event cycle for the use of GENI is depicted in figure 8. The user first sees the main menu from which first a group of techniques and then a specific technique can be selected. The technique displays a screen with instructions and then prompts the user for data input (see, for instance, figure 3). The user can then take various actions. First, he or she may type in a data item, such as a goal. This would lead to a recording of that item and a repeated prompt to put in more data. Second, the user can choose to see a new stimulus, such as a new poem, before inserting any further data. GENI would then show the new stimulus and repeat its prompt for more data. If the user needs help, wants to edit existing information, or wants to record an idea that is not related to the current input task, he or she would activate one of three corresponding auxiliary functions instead. Finally, the user can choose to leave the technique. This action will typically return control to the main menu, but can also result in the activation of another technique, based on the fcn definition. In the earlier example, meansends handed control over to means2. The advantage of this type of input cycle lies in its structure and standardization. The design of the input cycle is based on ideas of Benbasat and Wand regarding the development of structured dialogs [5].

## 5. Empirical Assessment of Effectiveness

## 5.1. Purpose of the Investigation

THE MAIN PURPOSE OF THIS PAPER has been to present the structure of the GENI program, with special attention paid to the interface with the user. Yet any claim of design effectiveness or functionality is irrelevant without validation. Several experiments were carried out to answer the general question, “Can the GENI software improve decision-maker performance in the early phases of the problem solving process?” and the more specific question, “Is a more elaborate interface (in terms of both format and content) more effective than a simpler interface?” While the research interest was directed at both problem formulation and idea generation, idea generation was the central aspect of the investigation. Problem formulation performance was not assessed directly. To address the first question, we investigated whether the GENI software could increase problem solver performance beyond a base level, defined by a control treatment. We hypothesized that GENI would lead to better overall performance and that the best ideas would be generated by use of the GENI program.

![](/api/attachments/YCCJ3QKK/fulltext/images/3d076f83a0194bf666f055c27093c0ef9e534b61b9e81e10ef6bc13dcd64b460.jpg)  
Figure 8. Input-Event Cycle

The more specific second question was studied by comparing the differential effectiveness of the different techniques within the GENI program—techniques that differ considerably in their interfaces. Our expectation was that the more elaborate techniques (e.g., Relational Combinations) would result in higher problem solver productivity, at least in the later stages of a problem solving session. Therefore, a second baseline for technique effectiveness was a comparison of each technique with the performance of GENI's own Brainstorming technique. Problem solvers were expected to perform better with more elaborate techniques than with Brainstorming.

While our research included a study of technique-related performance differences, it did not include the validation of specific idea generation theories. At this early stage in the development and assessment of this type of software, we were less interested in the evaluation of specific theories of ideation than in the tangible differences between techniques that could explain performance differences. As far as the user is concerned, the tangible differences between techniques are only in the interface. The “naive user” may describe the differences simply as a variation in the stimuli appearing in Window 3 or Window 6. Thus, by comparing the techniques, we are comparing differences in interfaces (in the broad sense).

## 5.2. Results

Several experiments were carried out; two are described here. The first [23] compared GENI to a control treatment to assess its overall usefulness. A word processor was chosen as the control treatment to keep the variable “computer” constant, therefore ruling out the possibility that GENI’s techniques were more effective simply because of computerization.

The first experiment with forty-eight undergraduate business school subjects used GENI on two problems and a word processor control treatment on one problem. The results from this experiment are described in detail elsewhere $[23]$ and will not be repeated here, except to say that there was a significant improvement in problem-solver performance with GENI compared to the control treatment.

In a second experiment, the effect of different techniques on problem solver productivity was the primary focus. Each participant in the experiment had to work on four problems, two diagnosis problems ("What is the cause of this situation?") involving corporate takeovers and airline no-shows, and two design tasks ("How can we improve this situation?") involving an ailing donut franchise and acid rain. The order in which subjects worked on the problems differed, whereas the order of techniques was held constant. Subjects used Brainstorming on the first, Metaphoric Connections on the second, Ends-Means on the third, and Relational Combinations on the last problem.

This experiment, while testing the differences between techniques, essentially compared the different types of user interfaces against each other. The subjects were a group of thirty-two M.B.A. students, eight of them women. They competed for four prizes of about \$25 value each (e.g., gold-plated ballpoint pen), one for each problem. The time limit to complete a problem was 17 minutes (a basic 15 minutes plus 2 minutes to finish off). All participants were instructed that prizes were awarded based on both quantity and quality of results. The average yield of about 17 ideas per person-problem shows that the subjects put substantial effort into the task.

The results were evaluated by quantity of ideas, to measure idea fluency, which served as a surrogate for quality. Quantity measures have been used repeatedly in the field of psychology (e.g., [8, 27, 34]), based on one of the key assumptions of Brainstorming, “quantity breeds quality.”

An initial idea count revealed some differences between the techniques (see Table 1), yet only the idea total for Relational Combinations was significantly lower than that of any other technique (t-test, p < 0.01; see Table 2). An investigation of the idea-generation pattern revealed, however, that subjects using Relational Combinations were not actually less fluent, but had much less time to generate ideas. To formulate Relational Combinations, subjects first have to input relevant objects and processes. It was up to each individual to decide how much time to spend on each of these steps of the process and some individuals spent virtually all their time on object and process definitions. Ends–Means Chains, the technique with the second lowest average, also required preparatory effort for goal definition, but only about half the time of Relational Combinations. Metaphoric Connections and Brainstorming, which had the highest idea yields, were the two techniques that allowed the users to record ideas immediately. To compensate for this difference in preparatory effort in the evaluation, an alternate measure was used, idea generation speed.

For the assessment of idea generation speed, each subject's performance was measured from minute 1 to minute 6 and from minute 7 to minute 12 of every problem solving session, allowing a comparison of early idea generation to late idea generation. If a subject had spent less than 12 minutes on producing ideas, that problem session was not included in the evaluation. The exception to this rule was Relational Combinations, where only 3 out of 33 subjects completed 12 minutes or more of idea generation. For Relational Combinations, we therefore only report the results of the first 6 minutes. Idea generation speeds were calculated separately for design and diagnosis. The results are given in Table 3.

Table 1 Total Number of Ideas Based on Technique

<table><tr><td></td><td>Mean</td><td>Std.Dev.</td><td>No. of Obs.</td></tr><tr><td>Rel. Combinations</td><td>10.5</td><td>7.9</td><td>33</td></tr><tr><td>Brainstorming</td><td>21.6</td><td>12.4</td><td>26</td></tr><tr><td>Ends-Means</td><td>17.0</td><td>11.0</td><td>32</td></tr><tr><td>Metaph. Connections</td><td>20.6</td><td>12.4</td><td>31</td></tr></table>

Table 2 Significance of Number-of-Ideas Results (t-statistics)

<table><tr><td rowspan="2"></td><td colspan="2">Brainstorming</td><td colspan="2">Ends-Means</td><td colspan="2">Metaphoric Conn.</td></tr><tr><td>t</td><td>p</td><td>t</td><td>p</td><td>t</td><td>p</td></tr><tr><td>Rel. chain</td><td>-4.18</td><td>&lt;0.01</td><td>-2.74</td><td>&lt;0.01</td><td>-3.91</td><td>&lt;0.01</td></tr><tr><td>Brainstorming</td><td></td><td></td><td>1.50</td><td>0.15, n.s.</td><td>0.30</td><td>n.s.</td></tr><tr><td>Ends-Means</td><td></td><td></td><td></td><td></td><td>-1.22</td><td>n.s.</td></tr></table>

Table 3 Fluency Results (Ideas/Minutes)

<table><tr><td rowspan="2">DESIGN</td><td colspan="2">Rel. Combinations</td><td colspan="2">Brainstorming</td><td colspan="2">Ends-Means</td><td colspan="2">Metaphoric Conn.</td></tr><tr><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td></tr><tr><td>1-12 min</td><td></td><td></td><td>1.067</td><td>0.394</td><td>1.55</td><td>0.597</td><td>1.179</td><td>0.629</td></tr><tr><td>1-6 min</td><td>1.25</td><td>1.058</td><td>1.217</td><td>0.393</td><td>1.389</td><td>0.731</td><td>1.071</td><td>0.672</td></tr><tr><td>7-12 min</td><td></td><td></td><td>0.917</td><td>0.432</td><td>1.711</td><td>0.565</td><td>1.286</td><td>0.65</td></tr><tr><td>No. of Obs.</td><td colspan="2">8</td><td colspan="2">10</td><td colspan="2">15</td><td colspan="2">21</td></tr><tr><td rowspan="2">DIAGNOSIS</td><td colspan="2">Rel. Chains</td><td colspan="2">Brainstorming</td><td colspan="2">Ends-Means</td><td colspan="2">Metaphoric Conn.</td></tr><tr><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td><td>Mean</td><td>S.Dev</td></tr><tr><td>1-12 min</td><td></td><td></td><td>1.955</td><td>0.974</td><td>2.313</td><td>1.449</td><td>1.565</td><td>0.768</td></tr><tr><td>1-6 min</td><td>1.55</td><td>0.79</td><td>2.038</td><td>1.043</td><td>2.083</td><td>1.309</td><td>1.463</td><td>0.622</td></tr><tr><td>7-12 min</td><td></td><td></td><td>1.872</td><td>1.078</td><td>2.542</td><td>1.607</td><td>1.667</td><td>1.118</td></tr><tr><td>No. of Obs.</td><td colspan="2">18</td><td colspan="2">13</td><td colspan="2">4</td><td colspan="2">9</td></tr></table>

For design problems, Metaphoric Connections and Brainstorming are approximately similar during the full 12-minute time period (1.2 versus 1.1 ideas per minute), while Ends–Means emerges as the most efficient technique (1.55 ideas per minute). A t-test (see Table 4) indicates a significant difference between Ends–Means and Brainstorming (p < 0.04), but not between Ends–Means and Metaphoric Connections (p = 0.08, n.s.). The breakdown into six-minute halves is more revealing. While during the first six minutes the differences between techniques are insignificant (speeds varying from 1.1 to 1.4 ideas per minute), the second six minutes show a substantial increase in performance for Ends–Means (to 1.7 ideas/minute) compared to a slight increase for Metaphoric Connections (to 1.3 ideas/minute) and a decrease with Brainstorming (to 0.9 ideas/minute). During the second six minutes, the performance difference between Ends–Means on one hand and Brainstorming or Metaphoric Connections on the other hand becomes significant (p < 0.01 for Brainstorming, p = 0.05 for Metaphoric Connections).

Table 4 Significance of Idea Fluency Results (t-statistics)

<table><tr><td colspan="2"></td><td>Bt</td><td>p</td><td>Mt</td><td>(Ends-M.)p</td><td>Pt</td><td>(Metaph. C.)p</td></tr><tr><td rowspan="2">DESIGN1-12 min</td><td rowspan="2">BM</td><td></td><td></td><td>-2.245</td><td>0.04</td><td>-0.51</td><td>n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>1.781</td><td>0.09, n.s.</td></tr><tr><td rowspan="3">DESIGN1-6 min</td><td rowspan="3">RBM</td><td>0.147</td><td>n.s.</td><td>-0.47</td><td>n.s.</td><td>0.668</td><td>n.s.</td></tr><tr><td></td><td></td><td>-0.678</td><td>n.s.</td><td>0.634</td><td>n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>1.35</td><td>0.19, n.s.</td></tr><tr><td rowspan="2">DESIGN7-12 min</td><td rowspan="2">BM</td><td></td><td></td><td>-3.762</td><td>&lt;0.01</td><td>-1.63</td><td>0.12, n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>2.039</td><td>0.05</td></tr><tr><td rowspan="2">DIAGNOSIS1-12 min</td><td rowspan="2">BM</td><td></td><td></td><td>-0.577</td><td>n.s.</td><td>1.002</td><td>n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>1.244</td><td>n.s.</td></tr><tr><td rowspan="3">DIAGNOSIS1-6 min</td><td rowspan="3">RBM</td><td>-1.48</td><td>0.16, n.s.</td><td>-1.09</td><td>n.s.</td><td>0.288</td><td>n.s.</td></tr><tr><td></td><td></td><td>-0.071</td><td>n.s.</td><td>1.476</td><td>0.16, n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>1.192</td><td>n.s.</td></tr><tr><td rowspan="2">DIAGNOSIS7-12 min</td><td rowspan="2">BM</td><td></td><td></td><td>0.974</td><td>n.s.</td><td>0.432</td><td>n.s.</td></tr><tr><td></td><td></td><td></td><td></td><td>1.146</td><td>n.s.</td></tr></table>

For the diagnosis tasks, performance differences are not statistically significant, due to high variance in the results, although Metaphoric Connection and Relational Combinations showed the lowest performance (1.5 to 1.6 ideas/minute versus about 2 ideas/minute for Ends–Means and Brainstorming; see Table 3). Here again, the idea generation yield for Brainstorming decreased over the second six minutes while it increased for Ends–Means and Metaphoric Connections.

## 6. Summary and Conclusions

WE HAVE DESCRIBED THE ARCHITECTURE OF A COMPUTER PROGRAM to support problem formulation and the generation of alternatives for a wide variety of problems. Because it is not feasible to provide extensive knowledge across many problem domains, such programs need to be domain-independent. The ability of domain-independent programs to improve idea generation performance stems from their capacity to help structure the problem and to provide stimuli for new ideas.

An important feature of our GENI program is a standardized screen configuration

18. Koestler, A. The Act of Creation. New York: Macmillan, 1964.

that not only makes it easier for the users but is very efficient in terms of required programming. The heart of the program, however, is a set of techniques to support the definition of problem elements and the generation of alternatives. On problem formulation, the program elicits from the user a set of key problem components, most notably goals, beliefs, assumptions, objects, and processes. These components are later used as data elements in techniques to help generate ideas. The idea-generation module incorporates a variety of techniques ranging from the very unstructured (e.g., Brainstorming) to the very structured (e.g., Relational Combinations). The more structured techniques make the most use of the inputs from the problem-formulation module. Empirical results suggest that while the free-form techniques provide the highest yield of ideas in short problem solving sessions, as time goes on such techniques seem to dry up and need to be supplemented by techniques that provide more stimulation to the user.

## REFERENCES

1. Arnold, J.E. Useful creative techniques. In A Source Book for Creative Thinking, S. Parnes and H. Harding, eds. New York: Scribners, 1962.

2. Ata Mohammed, N.H.; Courtney, J.F.; and Price, D.B. A prototype DSS for structuring and diagnosing managerial problems. IEEE Transactions on Systems, Man, and Cybernetics, 18, 6 (1988), pp. 899–907.

3. Andreasen, M.M. The use of systematic design in practice. In Design and Synthesis, H. Yoshikawa, ed. Amsterdam: Elsevier/North Holland, 1985.

4. Benbasat, I., and Dexter, A.S. An experimental evaluation of graphical and color-enhanced information presentation. Management Science, 31, 11 (1985), pp. 1348–1364.

5. Benbasat, I., and Wand, Y. A structured approach to designing human-computer dialogs. International Journal of Man-Machine Studies, 21 (1984), 105–126.

6. Carlson, E.D., and Motz, W. Integrating dialog management and database management. IBM Research Report RJ2738, Yorktown Heights, NY: IBM, 1980.

7. Chandler, A.D. Strategy and Structure: Chapters in the History of the Industrial Enterprise. Cambridge, MA: MIT Press, 1962.

8. Christensen, P.R.; Guilford, J.P.; and Wilson, R.C. Relations of creative responses to working time and instructions. Journal of Experimental Psychology, 53, 2 (1957), 82–88.

9. Crovitz, H.F. Galton's Walk. New York: Harper and Row, 1970.

10. Davis, R. Reasoning from first principles in electronic troubleshooting. International Journal of Man–Machine Studies, 19 (1983), 403–423.

11. de Bono, E. Lateral Thinking, Harmondsworth, UK: Penguin, 1970.

12. DeSanctis, G., and Gallupe, B.R. A foundation for the study of group decision support systems. Management Science, 38, 5 (1987), 589–609.

13. Dewey, J. How We Think. New York: D.C. Heath, 1933.

14. Drucker, P. The Effective Executive. New York: Harper and Row, 1966.

15. Govindaraj, T., and Su, Y.D. A model of fault diagnosis performance of expert marine engineers. International Journal of Man–Machine Studies, 28 (1988), 1–20.

16. Hofstadter, D. Godel, Escher, Bach: An Eternal Golden Braid. New York: Basic Books, 1979.

17. Kepner, C.H., and Tregoe, B.B. The Rational Manager. New York: McGraw-Hill, 1965.

19. Langley P.; Bradshaw, H.; and Simon, H.A. Bacon.5: the discovery of conservation laws. Proceedings of the Seventh International Joint Conference on Artificial Intelligence, Vancouver, British Columbia, 1981.

20. MacCrimmon, K.R. Creativity: discovery and design problems. University of British Columbia Working Paper, 1988.

21. MacCrimmon, K.R., and Taylor, R. Decision making and problem solving. In Handbook of Industrial and Organizational Psychology, M.D. Dunnette, ed. Chicago: Rand McNally, 1976.

22. MacCrimmon, K.R., and Wagner, C. Expert systems and creativity. In Expert Judgment and Expert Systems, J.L. Mumpower, et al., eds. Berlin: Springer, 1987.

23. MacCrimmon, K.R., and Wagner, C. Stimulating creativity using computer software. University of British Columbia Working Paper, 1990.

24. MacCrimmmon, K.R., and Wagner, C. Designing a program to develop creative outputs: second generation software. Proceedings of the Twenty-Fifth Hawaii International Conference on System Sciences, 1992, forthcoming.

25. Newell, A.; Shaw, C.; and Simon, H.A. Elements of a theory of human problem solving. Psychological Review, 65 (1958), 151–166.

26. Nunamaker, J.F.; Applegate, L.M.; and Konsynski, B.R. Facilitating group creativity with GDSS. Journal of Management Information Systems, 3, 3 (1987), 5–19.

27. Osborn, A.F. Applied Imagination. New York: Charles Scribner's Sons, 1953.

28. Pounds, W.F. The process of problem finding. Industrial Management Review, 11, 1 (1969), 1–19.

29. Reitman, W.R. Heuristic decision procedures: open constraints and the structure of ill-defined problems. In Human Judgments and Optimality, M.W. Shelly and G.L. Bryan, eds. New York: Wiley, 1964.

30. Rosenhead, J., ed. Rational Analysis for a Problematic World. New York: Wiley, 1989.
31. Schank, R. The Creative Attitude. New York: Macmillan, 1988.

32. Simon, H.A. The New Science of Management Decision, rev. ed. Englewood Cliffs, NJ: Prentice-Hall, 1977.

33. Sutton J.A., and Sprague, R.H. A study of display generation and management in interactive business applications. IBM Research Report RJ2392, Yorktown Heights, NY: IBM, 1978.

34. Taylor, D.W.; Berry, P.D.; and Block, C.H. Does group participation when using brainstorming facilitate or inhibit creative thinking? Administrative Science Quarterly, 3 (1957), 23–47.

35. Wallas, G. The Art of Thought. New York: Harcourt, 1926.

36. Weber, S. Systems to think with. Journal of Management Information Systems, 2, 4 (1986), 85–97.

37. Young, L. Creativity support in systems design. DSS-89 Transactions, Ninth International Conference on Decision Support Systems, 1989, pp. 175-185.

## APPENDIX: Sample Problem Description

Airline no-shows. Airline passengers can freely make seat reservations and then fail to show up for the flight without being penalized. This action can cause difficulty for other airline customers in that people may be turned away from a particular flight that in fact will have empty seats at take-off. No-shows are particularly problematic for the airlines, since an empty seat is essentially the same as a perishable commodity that isn't sold—there is no way to store it for a later sale. The revenue from an unsold seat is lost for good. Identify reasons that would explain WHY customers did not honor their reservations.
