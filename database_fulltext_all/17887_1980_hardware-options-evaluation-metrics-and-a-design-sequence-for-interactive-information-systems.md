---
otero_id: 17887
otero_key: "DNK35DHM"
title: "Hardware options, evaluation metrics, and a design sequence for interactive information systems"
authors: "Ben Shneiderman"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90026-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Hardware Options, Evaluation Metrics, and a Design Sequence for Interactive Information Systems

Ben Shneiderman \*

Department of Computer Science, University of Maryland, College Park, Maryland 20742, USA

Interactive information systems must satisfy a wide variety of users, serve a broad range of tasks, and be suited to diverse hardware environments. This paper concentrates on three aspects of interactive information systems design: hardware options, evaluation metrics, and a possible design sequence. Rigorous pilot studies are emphasized, and supporting experimental evidence is offered.

Keywords: Interactive information systems, terminal design, evaluation metrics, design sequence, human factor, casual users

![](/api/attachments/DNK35DHM/fulltext/images/38ae97fd8b2d6a6e578c5e73a67f495605e362e0f4f5fedf3257be11a2e68f51.jpg)

Ben Shneiderman is an Associate Professor of Computer Science at the University of Maryland. He has produced five books and more than 50 technical articles on database management, program design and development, human factors research in programming, and computer science education.

## 1. Introduction

Prophets of the new computer age celebrate online interactive computer use as if this technologically sophisticated approach will by itself solve problems. But these prophets are only old timers who remember the batch processing past; the youngsters see terminal access and instant response as normal. The newcomers are more discriminating, they want more than just instantaneous response, they want a “good” system.

A good system not only wins the users' respect, but it generates satisfying feelings of confidence and competence. These good systems can be everything from a well-designed hand calculator to a customer bank terminal or to a complete programming system. The attributes of an effective interactive system include:

\- ease of use

\- ease of learning

\- ease of remembering

– operations suitable for problem domain

– prompt system response

\- reliable software and hardware

\- meaningful error messages

\- adequate user aids (help facilities)

\- maintenance of data integrity and security

\- courtesy to the user

This list is not complete nor are all these attributes measureable, but it provides informal and broad goals for the system designer. A previous paper [1] covers psychological issues such as closure, locus of control, short-term memory, and anxiety, response time considerations, error handling, and system messages. This \* This article is adapted from the book, Software Psychology: Human Factors in Computer and Information Systems (Winthrop Publishers, Cambridge, MA, 1980).

paper examines hardware options and evaluation metrics, and suggests a development sequence.

## 2. Hardware options

The hundreds of terminals commercially available present a dizzying array of options for the system designer. Peripheral devices and custom features compound the problem, but they provide appealing opportunities for the creative designer.

## 2.1 Keyboards

Keyboard selection presents numerous difficult questions. The spacing between keys, number of special keys, availability of a numeric pad for fast keying of numeric data, the angle, shape and surface texture of the keys, pressure and distance required to depress the keys, tactile or auditory feedback on reaching bottom, placement of frequently used keys, and the clarity of the characters on the keys all contribute to the appeal of a keyboard. With the exception of cheap models (with hard to push keys or extremely compact keyboards), mass production has enabled vendors to produce relatively high-quality keyboards. Classic human factors research covers keyboard design [2,3]. Fig. 1 shows interesting results on the workload distribution of each finger using the standard keyboard and the error percentage for each finger.

![](/api/attachments/DNK35DHM/fulltext/images/ac514727ec6208991297137e24205c7cc48e0523f7f4f2561de6b964bad6f6aa.jpg)  
Fig. 1. Percent errors by finger are shown on top, based on 315,996 effective keystrokes [2]. Numbers on fingers are percent of workload [3].

Some studies have investigated the advantage of alternative keyboard layouts such as alphabetically ordered ones for nontypists who make only limited entries. For professional typists, it is possible to redesign key layout to increase typing speed for English language text $[4,6]$ . The 19th century layout was done in order to balance the mechanical loads, but with electric typewriters the layout can be based on·digram frequencies for English. Although such typewriters were built and proved their worth in experimental studies, it is unlikely that they will overcome the widespread acceptance of the traditional typewriter keyboard layout. This is an example of the historical imperative, that is, people's unwillingness to give up familiar and established tools unless the improvement is substantial.

## 2.2. Soft copy versus hard copy

Hard copy displays provide permanent records of the terminal session, while soft copy displays provide an electronic window which eliminates costly, polluting paper consumption. The choice is largely dependent on the application, but the lower cost, higher reliability, quieter operation, and potentially higher speeds of soft displays give them some advantages. At least two experiments [6,7] showed that users made fewer typing errors at hard copy displays – apparently the sound provides reassuring feedback, while soft copy displays require visual attention to verify that the information has been accepted.

Hard copy can be produced by noisy impact devices, such as selectric balls, "daisy" wheels, cylinders, or a matrix of pins; or by quiet nonimpact thermal, electrostatic or ink spray printers. Typical terminal print speeds are 15–80 characters per second. The imprint clarity and typing surface visibility, which may be obscured by the typing device or cover, play important roles in user acceptability.

Soft copy can be produced by the popular cathode ray tube (CRT), light emitting diodes (LED), liquid crystal diodes (LCD), or a flat plasma screen (which permits rear projection of photographic quality images). Display rates can be thousands of characters per second. Glare from the screen, flickering images, lack of contrast and limited number of lines may detract from CRT usage. However, silent operation, unlimited character sets, blinking, multiple intensity levels, black/white reversal, color images, erasing, insertion, cursor action, scrolling and multiple windows are attractive features.

In all display devices the type size, available fonts, sharpness, contrast, platen width, and vertical spacing influence acceptability.

Dramatic improvements are still being made in terminal design, and price continues to fall. As standardization occurs and production volume increases, we may expect continuing increases in quality and decreases in cost.

## 2.3. Cursor control devices

Some applications require position definitions by cursor movement in two-dimensional space. Positioning can be accomplished by keystrokes from a standard keyboard, but this can be slow and annoying. Several cursor moving devices have been developed, such as:

\- a lightpen which is used to move a cursor to the proper position on the screen

\- a sonic pen which is moved to a position on a special board equipped with microphones which sense the click emitted when the sonic pen touches the board

\- a mouse, which is a small mouse-sized box with rubber wheels which are rolled on a table to activate potentiometers and sense changes in position

\- a touch-sensitive screen with embedded sensing wires or a grid of light beams

\- a touch-sensitive plate used as a writing surface

\- a joystick which can be rotated about two axes.

Work needs to be done to determine the utility of these relatively cheap devices for differing applications. They all face the "third hand problem" — the user must lift at least one hand from the keyboard to indicate the position. Lightpens and touch-sensitive screens have the advantage that the user works directly with the image, but they have the disadvantage that the screen becomes obscured by the user's hand, and that it is tiring to continuously raise a hand and hold it close to a vertical screen.

## 2.4. Audio output

Computer activated tape recording devices are being replaced by more sophisticated speech generation systems which can be programmed to take stored phrases and generate arbitrarily complex sentences. These impressive and inexpensive speech generation systems, when programmed carefully, produce comprehensible speech. They have been employed by telephone companies for automatic generation of changed number messages and by stock exchanges for current quotes in response to telephoned requests. Sophisticated devices which scan typewritten or printed text and speak the material to blind people are appearing on the market. Talking toys and teaching devices are appealing consumer-oriented applications.

Another form of audio output is to have a terminal ring a bell or sound a chime to indicate special conditions. This seems a simple and effective procedure if not overused. Audio tones to signal error conditions should not be used when the terminal is in a public place, since it may lead to embarrassment.

## 2.5. Speech recognition systems

The image of the computer as a secretary which is competent at taking dictation and producing a type-written letter, has persisted from the earliest days of computing. Early attempts at discrete word recognition showed promising results. Systems constructed in the mid-1960's could recognize words spoken in a laboratory setting, taken from a dictionary of one thousand words with more than 90 percent accuracy. The words had to be spoken for entry into the computer's storage by the same person who later used the system. Hobbyists can now buy a speech recognition device which records up to 64 words and achieves 90 percent accuracy for about \$200. Commercial systems with 100 to 1000 word vocabularies are in the \$10,000 to \$20,000 range. Discrete word recognition might be useful in giving single word directives in controlling manufacturing equipment, wheelchairs, aircraft, operating room equipment, etc., when both hands are required for other tasks.

Continuous speech recognition in typically noisy environment with a variety of speakers presents a much greater challenge. Researchers at Carnegie-Mellon University have developed a series of systems, DRAGON, HEARSAY-I and HARPY, to cope with continuous speech recognition [8.9]. In one of the experiments, the vocabulary was restricted to 3:7 words dealing with programming for a desk calculator, and four different people provided sample sentences. The system accurately recognized more than 90 percent of the words and 80 percent of the sentences. Research continues at other universities and industrial sites such as IBM's Yorktown Heights, New York labs.

These results suggest that continuous speech recognition is still a difficult task, and the probability of their term success in developing a commercial system is low. Nonsy office environments, changes in speech style over time and across individuals, variety of syntactic forms, and the large number of words and names makes this task very difficult. A 90 percent or 95 percent recognition score may not be sufficient for commercial applications. Errors of commission (incorrect recognition) must be made extremely small, but errors of omission (failure to recognize with a request for clarification) may be more acceptable.

## 2.6. Graphics output, input, and interaction

On the premise that a picture is worth a thousand words, system designers have sought to provide graphic input and output. Perceptual psychologists have amply demonstrated the advantage of imagery over words or numbers for certain applications. Error rates and task performance time can be reduced substantially when a proper graphic representation can be found.

Early users of computer systems produced graphs, histograms, scattergrams, and crude drawings using line printer characters. CRI screens, electrostatic printers, ink pen plotters, and other devices allowed continuous line drawings with resolution, on the order of one hundred lines per inch. Contemporary displays allow two to four times the resolution, and color displays further enhance the image.

The difficulty has always been to develop software which makes image production convenient. Most graphics equipment manufacturers provide only basic software. Special-purpose graphics languages such as ARTSPEAK, EXPLOR, graphic ALGOL, BUGSYS, and Computer Animated Movie Language have been developed. Special purpose graphics hardware reduces the central processing unit load and permits rapid operations such as real-time rotation in three-space, contrast enhancement, filtering, color substitution, and size changes (zooming in or out). Graphics systems can provide a window on worlds that never existed or are invisible. Graphics applications have included views of:

\- a universe where gravity does not operate on the inverse square law

\- human heart functioning with injuries or diseases

\- crystal growth

\- wind tunnel flows

– demographic data on a map as it changes over time
– travel at speeds approaching the speed of light.

Graphic input is becoming less of a problem. Point by point digitizers facilitate manual insertion of images and TV camera input is becoming more available. Weather and reconnaissance satellite images are dramatic evidence of the success of computer image processing. Software to transform images and perform pattern recognition is improving and has been commercially applied for detecting deviation from manufacturing standards, as in the development of integrated circuit chips.

Interactive computer graphics applications [10] include electronic circuit design, map making, surveying, architecture, automobile design, numerical control of machine tools, textile pattern layout, newspaper layout, and police or firefighter dispatching. Graphics interaction is particularly effective if a basic pattern is to be entered and modifications can be mace on line. The success of graphics interaction depends on a narrow application domain, a natural representation of the real world phenomenon, and the acceptability of the set of operators. Foley and Wallace [11] support graphics interaction but caution users and developers about five problem areas:

1) Boredom-improper pacing

2) Panic—unexpectedly long delays

3) Frustration-inability to convey intentions or

inflexible and unforgiving system

4) Confusion—excessive detail or lack of structure

5) Discomfort—inappropriate physical environment. Bennett [12] gives a set of guidelines for graphics systems developers:

1) Arrange text and graphic symbols on each presentation to establish an explicit context for user action.

2) When a user process is not known in advance, concentrate on displayable data representations and then design operations to act upon these representations.

3) Design the system to provide an explicit framework for representations. The framework gives a uniformity of structure within which the user can synthesize problem solutions. This framework can be developed even though problems themselves are unstructured.

More experimental research is needed to refine our understanding of the advantages and environments suitable to graphics interaction. In summary, the graphics system should provide a familiar representation and standard operations. If graphics interaction provides 90 percent of what is possible manually, users may still be unhappy about losing 10 percent of their operations. A natural evolution for new technologies is to duplicate old technology performance before opening up new possibilities.

## 3. Evaluation metrics

A number of authors have written about the problems of designing interactive systems and have offered lists of features which they thought would improve quality. W.J. Hansen [13] (Fig. 2) begins his list of a dozen entries with the most important one: Know the User. No qualifier or explanation is necessary. Hansen's sensitivity to human short-term memory limitations leads to his second category: minimize memorization. Under "optimization of operations" Hansen includes "display inertia", suggesting that when operations are applied, as little of the display should be changed as possible. This approach reduces disruptive movement and highlights the impact of the last operation. "Muscle memory" refers to the idea that users develop the feel of frequently used key-presses. Hansen recognizes the importance of engi

First principle: Know the User
Minimize memorization
Selection not entry
Names not numbers
Predictable behavior
Access to system information
Optimized operations
Rapid execution of common operations
Display inertia
Muscle memory
Reorganize command parameters
Engineer for errors
Good error messages
Engineer out the common errors
Reversible actions
Redundancy
Data structure integrity

Fig. 2. User engineering principles for interactive systems [13].

neering for errors by providing good messages, reversible actions, and revisions to eliminate common terrors.

Wasserman's [14] five design principles are reasonable (Fig. 3), but the second and fifth ones may need qualification. Although it is usually a good to minimize the user's need to learn about the computer system, restricting access to those who have acquired a certain knowledge level may sometimes be effective. The qualifying test which works well for driving licenses and college entrance, may be useful for complex and powerful systems. Naive users should be prevented from using a system which is too hard for them and would produce an unplesant experience. Waaserman's fifth principle may not always be good advice. Novices may prefer and do better with a system which has few choices and permits or by limited forms of expression.

Gaines and Facey [15] (Fig. 4) emphasize the importance of the user being in control of the terminal, the pace of the interaction, the tutorial aids, and the execution process. Cheriton [16] (Fig. 5) provides

Fig. 3. The design of idiot-proof interactive programs [14].

![](/api/attachments/DNK35DHM/fulltext/images/57783939193128b96348fd26edf417af93b22e1725a88ec9b81cc450ec06db95.jpg)  
Fig. 4. Guidelines for designing interactive systems [15].

further considerations and suggestions for designing general purpose interactive systems. Gebhardt and Stell macher [17] offer guidelines for document retrieval languages and Turoff, Whitescarver and Hiltz [18] last desirable attributes for teleconferencing systems. Engel and Granda [19] have the most complete and detailed set of design criteria. For a general survey, see James Martin's Design of Man-Computer Dialogues [20].

Unfortunately, these lists are only crude guides to the designer. The entries are not independent and sometimes are in conflict. The lists provided by different authors even contain contradictory recommendations. Finally, these design goals are largely unmeasurable. Can we assign a numerical value to the terms these authors use such as simplicity, stability, responsiveness, variety, etc.? How can we compare the simplicity of two design proposals? How do we know what has been left out of the system design?

![](/api/attachments/DNK35DHM/fulltext/images/e6f2c021e75ffe071fab0a2d578f90eb7657f921a688f7f6f7d67ba62378563b.jpg)

![](/api/attachments/DNK35DHM/fulltext/images/f3b8889ff748360880509e7a6a775e9d6f14cfcae5c3598a79767ca1df6006de.jpg)  
Fig. 5. Interface design for time-sharing systems [16].

Understanding of interactive systems can be enhanced by controlled psychological experimentation. Studies by L.H. Miller [21] (Flg. 6), Goodman

![](/api/attachments/DNK35DHM/fulltext/images/26ae57f6ec74cfadc9ce51d6100b26a8291d0c8f352577a8f7b4d903effef3ad.jpg)  
Fig. 6. Graph of time to complete tasks vs. output variability for low and high volume and graph of poest-test satisfaction level vs. output variability (1,700 and 2400 baud) [21].

![](/api/attachments/DNK35DHM/fulltext/images/e1d75410a0613fe0cc66cd33ced5329d3bc3ee1402a0ee6321ee7926efbbd6c1.jpg)  
Fig. 7. Solution time vs. system response time for 30 subjects [22].

and Spence [22] (Fig. 7), Grossberg, Wiesen and Yntema [23], and others are beginning to provide data on how human performance changes as system response time varies. The work of Card, Moran and Newell [24,25] is improving our knowledge of text editor usage. Studies of programming language usage (see [26] for a review) or database query language usage [27] contain relevant results which need to be interpreted and validated in the interactive systems domain. Experimental research can help to resolve some design issues and refine our capacity to measure system quality. Still, some aspects of designing will remain an art or intuitive science where esthetics and contemporary style determine success.

The next four subsections present four, largely independent, measurable, hopefully thorough, design goals: simplicity, power, user satisfaction, and reasonable cost.

## 3.1. Simplicity

A primary virtue of design is simplicity: from the medieval rule of Occam's Razor which sates that the best explanation of physical principles is the simplest one to the Bauhaus phrase "less is more" to the contemporary "small is beautiful." With simple designs, the designer, implementer, and user are less likely to make mistakes. Simple systems are easy to learn, easy to remember, and easy to use, by the widest possible audience. Simple systems are easier to modify and fix if things go awry.

An interactive system is simple if it has few commands and if the commands have a consistent structure. Output should be readable and error messages should have a uniform format. Command structures should match the problem domain and the sequence of user thought processes.

Simplicity of the commands can be measured by taking the reciprocal of the number of different command formats. With fewer formats, the simplicity value goes up. A simplicity count of one is ideal but possible only for trivial systems (such as an on-off switch). Reisner [28] demonstrates the use of a grammar in evaluating the usability to two proposals for the ROBART interactive graphics system.

## 3.2. Power

One of the joys of using computers is the power they offer. A good system provides powerful commands which enable users to accomplish their goals easily. The commands should facilitate problem-solving processes and provide all previously available manual functions. If a system carries out 19 of the 20 required functions, the users will complain about the missing twentieth function. The computerized system should be better in every way than the manual system.

Experienced users should have especially powerful commands available. They should be able to create macros, extend the system, or tailor the system command structure and output formats to their needs. System operations should be rapid and convey a sense of power rather than a sense of lethargy. The hardware and software should be reliable, stable over time, and secure, with sufficient processing power and storage space. Data should be protected from inadvertent errors, malicious tampering, and privacy violations by careful control of software, cautious management policies, and maintenance of backup copies.

Constructing a metric for power requires the enumeration of a benchmark set of tasks for the system. The power of a system for a specific task is one over the number of commands necessary to accomplish that . Summing over all tasks gives the power of a system relative to the benchmark set. This power metric is most helpful in comparing two systems designed to accomplish the same tasks. A system requiring multiple commands for each task has a low power metric. Providing one command for each task in the benchmark set will maximize power but reduce simplicity. Designs which increase power and simplicity are highly desirable.

## 3.3. User satisfaction

User satisfaction is separate from system effectiveness. A system may be effective but unpleasant to use or satisfying but ineffective. A bibliographic retrieval system may provide excellent results but be tedious to use or simple and satisfying to use but incapable of doing adequate searches through the literature.

A satisfying systems gives the user a sense of control. The system should respond to user commands rapidly, provide simple to understand messages, and offer adequate power. The computer should appear as a tool under the direction of the user. Gaines and Facey [15] describe a reluctant novice who was finally convinced to try the interactive system. She began to use the system and thus again some confidence; while she was consulting a manual for several minutes, the terminal suddenly produced a nasty message and detached the terminal because of inactivity. This user refused to return.

Errors messages should be constructive and supportive, not condemning and confrontive. Each command should produce feedback with meaningful acknowledgement. The system should never "dead-end" leaving the user confused and without recourse. The system should be reliable and minimize fear of failure. There should be no way that files are inadvertently destroyed, and (as much as possible) it should be possible to undo recent commands (such as an incorrect deletion or change). Users should have some way of finding out what they have done, what their current status is, and what options are open to them. Help commands should always be available. Users should be able to restart portions of a session or the entire session, to exit or abort, and to pause or resume at any point. The computer should appear as a helfpful tool aiding users in the performance of their tasks.

![](/api/attachments/DNK35DHM/fulltext/images/5c6f49e3f3ab4b656d0a62d83b9f45461e75f43f1b2445a4c2802af074abe0a9.jpg)  
Fig. 8. User perceived interactive systems quality factors from a survey [29].

User satisfaction is a more difficult measure, and it probably should include subjective measures (obtained by asking users to rate the system) and objective measures of actual use when alternative systems exist. Dzida, Herda and Itzfeldt [29] (Fig. 8) provide survey data from 233 people on subjective user satisfaction issues.

## 3.4. Reasonable cost

A system which costs too much is a failure. A good designer accurately estimates the cost of designing, implementing, and running the system. Improved designs may cost more time and money to develop, but can lead to enormous savings during implementation and in the productive life of the system. Good design can reduce hardware costs, improve reliability, reduce errors, and give users greater satisfaction. If a banking terminal system has a simpler and more powerful command structure that is easier to use, each transaction may take, say 20 percent, less time. This may mean that 20 percent fewer terminal operators, terminals, and telecommunication lines are necessary; central processor hardware needs are reduced, and operating systems demands are lowered. A 20 percent reduction in the transaction complexity and time might yield a 30 percent or more reduction in the system cost. A simpler and more powerful command structure may produce fewer costly and annoying errors, increase employee job satisfaction, reduce turnaround, facilitate hiring, and improve organizational morale.

Cost is measurable by tradiational accounting procedures. This is not simple, since development costs must be traded off against long-term usage costs, and some system features are not easily convertible to dollar values. In spite of these and other problems, if the same assumptions are made, cost estimates can be effective in comparing two similar systems.

## 4. An eight-stage development sequence

Establishing goals for interactive systems is the easy part. The hard part is doing the design. Designing requires the capacity to integrate multiple, complex, conflicting constraints, and produce the detailed specifications for every message of every display. These diverse requirements may be better met by a team rather than an individual designer. A closely knit team, with a competent leader and an open professional atmosphere, may be able to resolve design problems without the cluttered compromises generated by ad hoc committees.

It is impossible to provide an algorithm for designing, but the remainder of this paper is an attempt to define a design methodology. This development sequence is similar to the system life cycle for application program development but contains issues especially relevant to interactive systems for non-technical users [30]. The neat linear presentation hides the dead-ends, jumps, iterations, and revisions that are part of every design experience. This design sequence is general and must be modified to suit specific project needs: hardware requirements might be set by the current environment, software development might be replaced by using available packages, and the schedule may be externally imposed.

## 4.1. Collect information

The information collecting or pre-design stage involves getting organized and preparing for the job ahead. The design team should be formed and roles assigned. Participation from management is necessary so that surprises may be avoided. Since the success of many organizations will depend on their computer and information systems, it is vital that managers become involved in the design process. The experience with database systems has shown that if the database administrator does not have a high enough organizational rank, and if high-level managers do not participate, the project is likely to fail. Interactive systems also have a powerful organizational impact, restructuring communication patterns, and reassigning responsibilities. If critical decisions are left to technical personnel alone, those who oppose the new system will ensure its failure.

Users, managers, and customers whose activity will be affected by the new system should be interviewed and their ideas sampled by questionnaires. The first goal is to understand current practice, even if the new system will require different procedures – Know the User! It is useful to find out what procedures need improvement and given the users a chance to vent their displeasure to the design team. If the interviewers listen carefully, they will learn from the users and assure them that they are part of the design process. Users want to improve their working environment and resent being a pawn in a designer's technological chess game. Igersheim [31] (Fig. 9) found, in a survey of 225 middle-level managers, that acceptance of an information system is positively related to involvement in the implementation and negatively related to the perception of the system as threatening

No matter how original the project is, someone has done something like it before. Useful ideas can be found by consulting the professional literature about related projects and products and studying the academic literature for fundamental principles in psychology, information science, and computer science. The best advice can come from someone who has designed a comparable product elsewhere. A few hours with someone who has produced a similar system can be extremely therapeutic (for both parties).

<table><tr><td></td><td>ACCEPTANCE</td><td>JOB SATISFACTION</td><td>JOB SKILL</td><td>JOB OPPORTUNITY</td><td>JOB ORIGINALITY</td><td>JOB STATUS</td><td>JOB SALARY</td></tr><tr><td>JOB SATISFACTION</td><td>.72</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>JOB SKILL</td><td>.73</td><td>.81</td><td></td><td></td><td></td><td>.</td><td></td></tr><tr><td>JOB OPPORTUNITY</td><td>.42</td><td>.68</td><td>.53</td><td></td><td></td><td></td><td></td></tr><tr><td>JOB ORIGINALITY</td><td>.70</td><td>.87</td><td>.84</td><td>.66</td><td></td><td></td><td></td></tr><tr><td>JOB STATUS</td><td>.63</td><td>.70</td><td>.68</td><td>.48</td><td>.70</td><td></td><td></td></tr><tr><td>JOB SALARY</td><td>.35</td><td>.57</td><td>.45</td><td>.67</td><td>.53</td><td>.39</td><td></td></tr><tr><td>INVESTMENT</td><td>.43</td><td>.39</td><td>.41</td><td>.38</td><td>.44</td><td>.31</td><td>.24</td></tr></table>

Fig. 9 Correlation coefficients from survey of 225 managers demonstrating positive relationship among system acceptance, Job System and managerial involvement [31].

Even at this early stage, an attempt should be made to estimate costs and benefits from the new system. The costs of the design, implementation, and returning of personnel should be determined. Tentative schedules should be prepared with observable milestones. Each stage should contain modest, comprehensible, and realizable goals, without massive and potentially disruptive changes. Evolutionary progress is preferable to revolutionary discontinuity.

## 4.2 Design semantic structures

The first design task is to define goals and specify requirements. The design team must decide, for example, what banking operations will be available through the online system. Setting goals requires a close cooperation between management and technical staffs, because managerial decisions effect technical complexity and technical feasibility guides management goals. For example, reliable identification by signature or voiceprint analysis might encourage management to eliminate secret codewords and raise the maximum cash withdrawal amount at banking terminals.

Semantic design, the selection and specifications of system functions and features, should be level structured. The syntactic/semantic model of programmer behavior [32] can be applied to interactive systems usage. High-level problem-domain goals are set first, then refined into lower-level program-domain subgoals and tasks. Concurrent with the definition of tasks, the task sequence presented to the user is chosen. Since an interactive session proceeds linearly over time, the steps must be arranged in a complete ordering. The designer now faces the educator's problem of deciding which topics to cover first and discovering ways of decoupling dependent tasks. Tasks should be grouped into transaction units so used can satisfy their desire for closure.

Designers have developed special flowchart schemes to describe interaction sequences or have adapted graph theoretic schemes such as Petri nets or state transition diagrams. The most appealing approach is the use of augmented transition networks where nodes are numbered states and edges have input/output events on them [33–35]. Figure 10 shows a high level transition diagram for using an interactive programming facility [36] with a subdiagram for the LOGON process. This hierarchical approach can show modular designs and hide low level detail, but the diagrams can be confusing and do not assure completeness or consistency. Another approach is offered by Reisner [28], who presents an “action grammar,” based on Backus–Naur Form productions, to define the sequences of permissible operations in an interactive graphics system.

The application domain data structures often play a central role in shaping the system design. A personal calendar might be arranged "bulletin board style" with each entry having a day and time stamp; or entries may be arranged by topic and sorted by date; or the calendar may include date and day of the week notations, so that all Monday schedules could be displayed. Large files of information could be simply sorted or could be sectioned into pages, pages into chapters, and chapters into volumes. Several alternatives should be generated and justification presented for the one chosen.

![](/api/attachments/DNK35DHM/fulltext/images/6c0a798bbd5490deca9afed8d4cf7d4593ba395eccccb6d17d256f0904473979.jpg)  
Fig. 10. Transition diagram with LOGON subdiagram for interactive programming facility [36].

The application domain operators on these structures are also crucial. Multiple low-level operations that would be easy to learn must be evaluated against complex powerful operations which would please more experienced users but challenge novices. The appropriateness of set theory, boolean algebra, predicate calculus, programming notation, or other mathematical approaches should be considered. Then application specific structures and operators should be studied. Chemical notation, architectural notation, editorial proof reading marks, or music symbols may fit for some applications.

Next it is necessary to specify privacy requirements, security needs, and integrity constraints. Integrity constraints improve data quality and protection but can raise costs dramatically and increase response time. Management must make the decisions on these tradeoffs based on sound technical advice.

Once a set of decisions has been made and properly documented, the conclusions should be presented to managers and users for feedback to improve the design (as well as to stimulate participation). Such a presentation is an important milestone, which raises enthusiasm for the project and gains acceptance for the design team.

## 4.3. Design syntactic structures

Once the user population characteristics and the semantic design requirements are clear, the syntax can be designed. If multiple user classes are expected, a range of syntactic styles may be adopted, including the menu selection, fill-in-the-blank, and parametric approaches. Design alternatives should be offered for output formats, split screen strategies (windows), detailed specification of operator syntax, error messages, tutorial aids, and help facilities. Response time requirements for each command type should be listed with means, minimums, and maximums. Competitive designs should be evaluated and justifications presented for the syntactic structures selected. Evaluation should be done first by colleagues, then by managers and users. Getting management and user representatives to sign-off on the semantic and syntactic designs forces more careful review and reduces the opportunity for misunderstanding. Sign-off is a protection mechanism for the design team.

Paper and pencil experimental tests can be conducted on at least portions of the interactive system design. Typewritten sheets can take the place of displays for evaluation of the task flow sequence, output for nats, error messages, etc. These pilot studies are valuable since they can reveal design flaws at an early stage. If aircraft designers feel the need to build full-size plywood mockups, play directors feel the need to conduct dress rehearsals. spacecraft engineers feel the need to run elaborate simulations, then interactive system designers should feel the need to run paper and pencil pilot studies. A more ambitious approach would be to prepare pilot implementations for realistic comparisons.

## 4.4. Specify physical devices

In many cases the interactive system designer may not have a choice over which terminals are used, but even in this case, specific terminal attributes should be kept out of the design process for as long as possible. Device independent requirement specifications, semantic design, and possibly syntactic design will yield easier-to-modify systems, which can accommodate new terminal technologies.

When terminal hardware can be chosen by the designer, the choice can be overwhelming. Hundreds of terminals with dozens of features, an unlimited number of keyboard designs, and a variety of accessories make it a lengthy chore to select a terminal. Ample justification should be given for choosing esoteric features which limit system portability and produce dependence on a limited number of vendors.

Communication line requirements should be stated explicitly. The reliability in terms of error states and mean-time-between-failures (MTBF) should be specified with the baud rate, coding scheme, etc. Backup communications strategies should be described if high reliability is necessary.

Guidelines should be established for the physical work environment of terminal users. Special air conditioning may be required, lighting levels should be considered (too little or too much light, or excessive glare can increase fatigue and error rates), noise levels should be mentioned (high noise levels may interfere with auditory cues from the terminal or terminal noise may disrupt nearby workers), and adequate desk space at the correct height should be specified.

## 4.5. Develop software

Interactive system software, like all software, should be designed in a top-down modular fashion, with the usual concern for modifiability, generality, and portability. Greater attention should be devoted to reliability and maintainability since failures may effect thousands of users whose tolerance of errors may be low and whose capacity to cope with errors may be nonexistent.

The modular software design may follow the hierarchical semantic design. As always, it is valuable to use high-level languages where possible and to adapt available packages if they suit the needs. Frame handling software packages which grew out of the computer-assisted instruction languages have been used successfully to speed implementation. Provide extensive system documentation material for those who must do maintenance. Testing is more challenging for interactive systems, since so many decision paths must be explored and the real-time environment is difficult to establish during development.

After testing single terminals, groups of terminals should be employed to measure response time degradation with increased load. If possible, the system should be tested to overload to find limitations and determine failure patterns.

## 4.6. Devise implementation plan

Even the best system can fail if the implementation plan is inadequate, designing a successful implementation plan requires a sensitivity to human communication problems and has little of the technical content of earlier phases. The designers should allow the system users to actively participate in the implementation planning. They should solicit advice from users about which sites should be first, which features should be taught first, and when training sessions can be scheduled. It is necessary to demonstrate that the designers are anxious to please, interested in improving the work situation, and responsive to suggestions [37].

Neither systems documentation nor design manuals are adequate for training purposes. A carefully designed training manual that has been thoroughly tested and handsomely produced is necessary. The spiral, layered, or phased approach should be used in training. A small subset of the facilities is taught and users receive positive reinforcement for success in learning to use the terminal features. The users gain a feeling of confidence and mastery which builds a positive image for the system. Then additional features can be explained.

![](/api/attachments/DNK35DHM/fulltext/images/5223716da7165e0fe4cd33f4d40f0a30cfca8fe725ccca582748b99def93a581.jpg)  
Fig. 11. Usage of new text editor features with respect to time [39].

Designers should feel they have succeeded if users find the system simple and easy to use. Kennedy [38] presents experimental results in the training of naive users in an interactive medical information system. Sondheimer [39] reports on user resistance to adopting new facilities in an online editor. His results demonstrate how hard it is to get users to change work habits (Fig. 11).

The system should provide a training mode in which novices can try out features without impacting sensitive data in the main file. The training system, possibly on a separate machine, should have a small version of the database and possibly additional tutorial aids. Consultants should be available to answer questions during training and the first days of system use.

## 4.7. Nurture the user community

Once the system is in use, every attempt should be made to create an active user community. Onsite or telephone consultants can offer aid when difficulties arise and an online consultant can service many users at low cost. Both parties can view the same screen images and carry on a discussion using two lines of a display screen.

An online “gripe” facility or suggestion box gives users a feeling that they can provide useful input and an opportunity to vent their anger about unsatisfactory system components. The system maintenance staff should respond to user suggestions with appropriate action or an explanation. Keeping the user community active and involved will facilitate acceptance and provide suggestions for improvements.

For large communities of users, a newsletter might be helpful. Occasional group meetings of user representatives might promote interchange of ideas. An independent user's organization, an effective source for product development in other areas, might be considered for widely used interactive systems.

## 4.8. Prepare evolutionary plan

No system is complete until it is obsolete. Large complex systems continuously evolve through improvements to current facilities, repair of errors, and modifications in system requirements. Good designers recognize this pattern and produce designs which are easy to maintain, modify, and improve. A good system contains software monitoring probes which provide statistics about performance and tabulate errors. This data can be used to change procedures, revise syntax, modify error messages, or develop automatic error handling. The monitoring probes can provide data for controlled experiments with the system. Experiments might be arranged to test new tasks flow sequences, improved syntax, altered error handling procedures, changed response time performance, new terminals, or a different class of users.

User satisfaction should be evaluated by interviews or questionnaires. A sample of users may be asked to respond to a set of questions at the end of a terminal session. Subjective questions can be misleading, but they do provide an indication of user satisfaction.

## 5. Practitioner's summary

Interactive system design is a difficult, challenging task which requires the capacity to integrate multiple complex requirements and pursue detailed specifications. Designers must be sensitive to manager and user feedback, technically sophisticated, and humble. Humility is important, because no complex system involving hundreds or thousands of people, can please all of the people all of the time. User complaints should be considered to stem from a desire to participate rather than as an attack.

The goals of system design are to produce a product which is simple, powerful, user-satisfying, and reasonable in cost. These goals can be in conflict, so it is necessary to be prepared to make some hard compromises. Criticism can be reduced if decisions are explicit and justifications are written down. Objective evaluation metrics, subjective user satisfaction studies, and rigorous pilot studies can aid the designer in system quality improvement.

An interactive system design sequence should have observable milestones and numerous evaluation points. Informal reviews, pilot tests, and controlled experimental tests should be conducted. Users must be involved in the implementation plans, an active user community should be created. and plans for evolutionary refinements should be stated. The development sequence can be summarized as:

1. Collect information

\- organize design team

\- obtain management participation

\- submit written questionnaires to users at all levels

\- conduct live interviews where possible

\- read practical and academic literature

\- speak with users and designers of similar systems

\- estimate costs and cost/benefit

\- prepare schedule with observable milestones

2. Design semantic structures

\- define goals and establish a hierarchy of requirements

\- consider task flow sequence alternatives

\- organize operations into transaction units

-- create application domain data structures

\- develop application domain operators

\- specify privacy, security, and integrity constraints

\- obtain agreement on semantic design

3. Design syntactic structures.

\- compare alternative display formats

\- create syntax for operators

\- prepare system response formats

\- develop error diagnostics

\- specify response time requirements

— plan user aids and help facilities

\- evaluate design specifications and revise where necessary

\- carry out paper and pencil experimental test

4. Specify physical devices.

\- choose hard or soft copy device

\- specify keyboard layout

\- select audio, graphics, or peripheral devices

— establish requirements for communication lines

— consider work environment noise, lighting, etc.

5. Develop software.

\- produce top-down modular design
- consider modifiability, generality and portability
- emphasize reliability and maintainability
- provide extensive system documentation
- conduct thorough test

6. Devise implementation plan.
- assure user involvement at every stage
- write and field test training manuals
- implement a training subsystem or simulator
- provide adequate training and consultation
- apply spiral/layered/phased approach to implementation
- aim to please the users

7. Nurture the user community.
- provide onsite telephone or consultants
- offer online consultant
- develop online "gripe" command or suggestion box
- make user news available online
- publish newsletter for users
- organize user group meetings for discussion
- respond to user suggestions for improvements

8. Prepare evolutionary plan.
- design for easy refinement or repair
- measure user performance regularly
- improve error handling
- carry out experiments
- sample feedback from users by questionnaires and interviews

## 6. Researcher's agenda

Interactive system design offers unlimited opportunity for research in a topic which has been poorly explored.

An important step would be the refinement and validation of metrics for simplicity and power. Scales or questionnaires need to be tested, validated, and standardized to evaluate user satisfaction. Standard accounting schemes are necessary to measure costs accurately and provide guidance for cost reduction.

The design sequence should be refined, and tools to facilitate implementation should be developed. Packages or special languages for interactive systems development are an exciting opportunity. Decision tables, graph theoretic ideas, augmented transition networks, petri nets, specialized flowcharts, and other schemes need to be evaluated for their utility in aiding interactive system design. Finally, researchers in organizational behavior and dynamics might study the impact of interactive systems and suggest ways of improving user acceptance.

## References

[1] Shneidernman, B., Human factors experiments in designing interactive systems, IEEE Computer. Vol. 12, No. 12 (December 1979), 9–19.

[2] Rupp, Bruce A. and Richard S. Hirsch, Human factors of workstations with display terminals, IBM Human Factors Center, HFC-ss(G320-69C2-)), San Jose, California, (November 15, 1977).

[3] Hart, D.J., The human aspects of working with visual display terminals, INCA-FIEJ Research Report No. 76/02, Washingtonplatz, Darmstadt, West Germany, (1976), 1–61.

[4] Martin, A., A new keyboard layout, Applied Egronomics, 3, 1, (1972).

[5] Kroemer, K.H. Eberhard, Human engineering the keyboard, Human Factors, 14, 1, (1972).

[6] Walther, G.H. and H.F. O'Neil Jr., On-line user-computer interface – the effects of interface flexibility, terminal type, and experience on performance, Proceedings of the National Computer Conference, 43, AFIPS Press, Montvale, New Jersey, (1974).

[7] Carlisle, James, H., Comparing behavior at various computer display consoles in time-shared legal information, Rand Corporation, Santa Monica, CA Report No. AD712695, (September 1970).

[8] Reddy, D.R., (Ed.) Speech Recognition, Academic Press, New York, (1975).

[9] Lowerre, B.T., The HARPY speech recognition system, Ph.D. Dissertation, Department of Computer Science, Carnegie-Mellon University, Pittsburgh, Pennsylvania, (1976).

[10] Newman, W.M. and R.F. Sproul, Principles of Interactive Computer Graphics, (Second Edition), McGraw-Hill, New York, (1978).

[11] Foley, J.D. and V.L. Wallace, The art of graphic man-machine conversation, Proceedings of the IEEE, 62, 4, (April 1974).

[12] Bennett, John L., User-oriented graphics systems for decision support in unstructured tasks, IBM Research Report RJ 1940, San Jose, CA (Februari 1977).

[13] Hansen, W.J., User engineering principles for interactive systems, Proceedings of the Fall Joint Computer Conference, 39, AFIPS Press, Montvale, New Jersey, (1971), 523–532.

[14] Wasserman, A.I., The design of idiot-proof interactive systems, Proceedings of the National Computer Conference, 42, AFIPS Press, Montvale, N.J. (1973).

[15] Gaines, Brian R. and Peter, V Facey, Some experience in interactive system development and application, Proceedings of the IEEE, 63, 6, (June 1975), 849–911.

[16] Cheriton, D.R., Man-Machine interface design for time-sharing systems, Proceedings of the ACM National Conference, (1976), 36–380.

[17] Gebhardt, F. and I. Stellmacher, Design criteria for documentation retrieval languages, Journal of the American Society for Information Sciences, 29, 4, (July (1978), 191–199.

[18] Turoff, M., J. Whitescarver and S.R. Hiltz, The human machine interface in a computerized conferencing environment, Proceedings of the IEEE conference on Interactive Systems, Man, and Cybernetics, (1978), 145–157.

[19] Engel, Stephen E. and Richard E. Granda, Guidelines for Man/Display Interfaces, IBM Pughkeepsie Laboratory Technical Report TR 00.2720, (December 19, 1975).

[20] Martin, J., Design of Man-Computer Dialogues, Prentice-Hall, Englewood Cliffs, New Jersey, (1973).

[21] Miller, L.H., A study in man-machine interaction, Proceedings of the National Computer Conference, 46, AFIPS Press, Montvale, New Jersey, (1977), 409–421.

[22] Goodman, T. and R. Spence, The effect of system response time on interactive computer aided problem solving, ACM SIGGRAPH '78 Conference Proceedings, (1978), 100–104.

[23] Grossberg, Mitchell, Raymond A. Wiesen and Douwe B. Yntema, An experiment on problem solving with delayed computer responses, IEFE Transactions on Systems, Man, and Cybernetics, SMC-6, 3 (March 1976) 219–222.

[24] Card, S.K., T.P. Moran and A. Newell, The keystroke-level model of user performance time with interactive systems, to appear in Comm. ACM.

[25] Cardf, S.K., T.P. Moran and A. Newell, Computer text editing: An information-processing analysis of a routoutine cognitive skill, Cognitive Psychology 12, 1 (Jan. 1980) 32–74.

[26] Moher, T. and Schneider, G.M., Methodology for experimental research in software engineering, University of Minnesota Computer Science Technical Report 79-2 January 1979).

[27] Shneiderman, B., Improving the human factors aspect of database interactions, ACM Transactions on Database Systems, 3, 4, (December 1978a), 417–439.

[28] Reisner, Phyllis, Using a formal grammar in human factors design of an interactive graphics system, IBM Research Report RJ2505, San Jose, California. (April 11, 1979).

[29] Dzida, W., S. Herda and W.D. Itzfeldt, User perceived quality of interactive systems, IEEE Transactions on Software Engineering, Vol. SE-4, No. 4, (July 1978), 270–276.

[30] Bally, L., J. Brittan and K.H. Wagner, A prototype approach to information system design and development, Information and Management, 1, 1 (November 1977), 21–26.

[31] Igersheim, Roy, H., Managerial response to an information system, Proceedings of the National Computer Conference, 45, AFIPS press, Montvale, New Jersey, (1976), 877–882.

[32] Shneiderman, B. and R. Mayer, Syntactic/semantic interactions in programmer behavior: A model and experimental results, International Journal of Computer and Information Sciences. 7, (1979), 219–239.

[33] Parnas, D.L., On the use of transition diagrams in the design of a user interface for an interactive computer system, Proceeding of the 24th National ACM Conference, ACM, New York, (1969), 379–385.

[34] Denert, F., Specification and design of dialogue systems with state diagrams, In Morlet, E. and D. Ribbens (Editors), Proceedings International Computering Symposium 1977, North-Holland Publishing Company, Amsterdam (1977).

[35] Wasserman, A.I. and S.K. Stinson, A specification method for interactive information systems, Proceedings of Conference on Specifications of Reliable Software, IEEE Catalog No. 79 CH 1401-9C, IEEE Computer Society, Piscataway, N.J., (1979), 68–79.

[36] Feyock, S., Transition diagram-based CAI/HELP systems, International Journal of Man-Machine Studies, 9, (1977), 399–413.

[37] Bjorn-Andersen, N. (Editor). The Human Side of Information Processing, North-Holland Publishing Company, Amsterdam, (1980).

[38] Kennedy, T.C.S., Some behavioural factors affecting the training of naive users of an interactive computer system, International Journal Man-Machine Studies, 7, (1975), 817–834.

[39] Sondheimer, Norman, On the fate of software enhancements, Proceedings of the National Computer Conference, 48 AFIPS Press, Montvale, New Jersey, (1979).
