---
otero_id: 18199
otero_key: "NVTTSMU8"
title: "Establishing user-centered criteria for information systems: A software ergonomics perspective"
authors: "Diana L. Knittle; Stephen Ruth; Ella Paton Gardner"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90001-7"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Establishing User-Centered Criteria for Information Systems: A Software Ergonomics Perspective

Diana L. Knittle, Stephen Ruth

and Ella Paton Gardner

George Mason University, 4400 University Drive, Fairfax, Virginia 22030, USA

Despite its importance and increasing cost, interactive software is rarely considered a suitable subject for the development of metrics or standards of performance beyond those traditionally used for hardware: speed, response time, etc. This article examines and extends a specific set of criteria first recommended by Louis Fried as a possible basis for evaluating such software rigorously. This approach is based on the concepts of ergonomics, which focus directly on the reaction of the user to the system rather than the system to the user. It is then possible to be much more specific in identifying effects of system messages, prompts, formats and a wide range of other characteristics of the user's milieu. Examples are given, and the authors conclude that such approaches make it possible to be rigorous and exact in specifying the characteristics of the interactive language of the system.

Keywords: Software metrics, interface design, software ergonomics, software engineering, user centered programming, human factors in systems design.

![](/api/attachments/NVTTSMU8/fulltext/images/5dfda1a147adc92f12cafad29204ecedd5d6d3130f803efb24cf58e1f9e81709.jpg)

Diana Knittle is a computer systems analyst for a defense contracting firm where she is responsible for automation requirements analysis and information systems planning and design. She has also done research on human engineering factors in computer systems design and the implications of user centered design on productivity. She holds an M.S. in Information Systems from George Mason University.

## 1. Introduction

In a 1982 article [14], Louis Fried of the Stanford Research Institute suggested that it was possible to describe criteria for desirable software as clearly as those for hardware. He proposed a classification that focuses on the effect of software on its user. Thus, he shifted the locus of evaluation from characteristics, like compiler certification, file volatility, and input-output speed, to the aggregate effect on the ultimate consumer. Elaborations of his work have appeared frequently, and his idea is as valid today as when he proposed it. However, reading the examples of successes and failures in the market place gives

![](/api/attachments/NVTTSMU8/fulltext/images/b0d61f476b5c81168230f98160121615832316a83bad217b62c45a1f75658c68.jpg)

Stephen Ruth is a Professor in the Department of Decision Sciences at George Mason University. He earned a B.S. from the U.S. Naval Academy and Ph.D. from the University of Pennsylvania. His current research focuses on human engineering issues in computer systems design, with emphasis on the development of testable criteria for evaluating effects of software on user productivity.

![](/api/attachments/NVTTSMU8/fulltext/images/2a84156d68414cfe3ba2d78bdf7bf7555e8bf953584ee86419f258fe1a66282b.jpg)

Ella Paton Gardner is an Assistant Professor in the Department of Decision Sciences at George Mason University. Before that, she worked in the aerospace and automobile industries. She earned a B.S. at the Massachusetts Institute of Technology, an M.B.A. at The University of Michigan and a D.B.A. at The George Washington University. Her major research interest is in improving productivity in organizations by the effective use of microcomputers. This includes studying techniques to relieve anxiety and other health effects sometimes encountered with the introduction of microcomputers.

one the impression that there still has been no conscious process of rationalizing or codifying the user-based system requirements as rigorously as those for hardware. This is the role of ergonomic software principles.

Ergonomics in computing is often considered to involve the operator sitting in special furniture, keying in data with equipment optimized for light, glare, low muscle fatigue and other traditional ergonomic factors. However, it is just as important for the messages, interfaces, menus, graphs, prompts, syntax and other features of the user software to be “humanized.” Ergonomic software in Fried’s context refers to all features which make a difference in the user’s output, with particular emphasis on those not related to physical work place aspects.

In this article we extend the ergonomic software principles proposed by Fried by citing recent examples from the literature. We then propose that these principles be codified and used to evaluate software. Doing so could lead to more rational and economical choices of software.

## 2. Principles of Ergonomic Software

## 2.1. Minimize Worker Effort

A worker should be required to perform only that work which is essential and cannot be performed by the system. This statement also implies simplification of information input, such as provision of minimal keystrokes or on-screen pointers to call a command or routine, or voice input rather than keyboard entry. For example, Barr and Rogers [2] suggest that the package should be able to detect the host's communication format (baud rate, data length, parity, number of stop bits) then automatically adjust to match rather than requiring the worker to check the host and adjust the format to match. Branscomb and Thomas [4] recommend a synonym table so that the worker does not have to know exact terminology. The system tracks synonym usage and updates this table.

Work done in the past should not be repeated. Program, query, or command code should be reusable, as should file and data definitions. Schmidt [26] shows that repetition leads to boredom which may negate any production gain made by automating the task. Barr and Rogers [2] suggest that a communications package have an automatic re-dial facility so that the worker need not repeat frequently occurring messages.

Kay [16], discussing spreadsheet packages, notes that “one powerful property is the ability to make a solution generic by ‘painting’ a rule in many dozens of cells at once without requiring users to generalize from their original concrete level of thinking”. Thus, a solution such as a calculation could be identified only once by the worker and then reused in any other cell.

Martin [20] recommends minimal data redundancy but suggests that when duplicate occurrences of a data item are required, a single worker entry should update all occurrences of that item. Also, the operating system should perform as many functions as necessary to free the workers, such as supplying the data and providing file and transaction recovery in the event of system failure. Warren [29] was impressed with Visidex's built-in calendar feature with assists in retrieving an deleting information by date or time, supplied automatically by the internal clock. Opening a file automatically updates the date and time in the file definition.

Brownstein and Lerner [6] recommend consideration of recovery capabilities when conducting an evaluation. They also recommend that other overhead functions, such as audit trails, production and operations statistics, file protection, backup, error diagnostics, and transaction logging be considered.

Workers should not be required to search for system information. Documentation should be available on-line as HELP routines. In order to minimize worker effort, the answers to the worker's questions should be immediately available. The worker should not have to pick up the manual, search the index, and find the pages to solve a problem. Chafin [7] recommends a hierarchical on-line help function called from anywhere in the applications program. The implication is that the help screens, like the program, provide exactly the capability needed.

Neal and Simons [22] refer to on-line help and hardcopy documentation as essential to the software and recommend that they be tested with the application in order to be most effective. They measured characteristics like inability to find needed information in the documentation, frequency of use, and duration of access to each section of the on-line help.

Koved and Schneiderman [19] have proposed the use of imbedded menus to facilitate the support of on line users who encounter problems with the more common explicit menus. This task support reduces computer related syntax and semantic errors.

Riemann and Waren [25] suggest that if on-line help messages are hierarchical and clear, and error messages meaningful, hardcopy documentation may not be necessary to operate the system. They also conclude that the external documentation can be helpful to the beginner or casual user if it has a complete, cross-referenced index.

Information presented by the system to the worker should provide specific instructions for action such as how to correct an error and not require the worker to interpret the response. Worker effort can be minimized by understandable system messages. Dean [9], in discussing system messages, states that a message whose meaning has to be explained fails as a message. Messages must be self-explanatory, relevant, specific, timely, and helpful. Errors should take no more effort to correct than to make. Duplication of work should be eliminated. All work should be capable of being performed on-line.

Morland [21] recommends that the layout and format of the data entry screen presented to the worker be as similar as possible to the written data entry form being used. The worker knows where to find each piece of information on the written form and the effort required to transfer that datum to the system can be minimized by providing a similar screen layout.

## 2.2. Minimize Worker Memorization

Workers should be required to memorize as little as possible. If the system requires a minimum level of memorization by the worker, less training will be required. Schneiderman [27] presents Hansen's five engineering principles for interactive system design, one of which is "minimize memorization". Banning's design approach as to allow the worker to point to an object or operation, thus eliminating the need to memorize the names [1].

Foley, Wallace, and Chan [13] suggest that memorization can be minimized by using techniques consisting of a small number of steps and a small amount of key information, applying regular patterns to all techniques, and prompting the actions. They warn that increased demands on user memory mean higher incidence of poor performance, fatigue and frustration, as well as slow learning and recall.

The system should be designed so that learning the system is an incrementally extensible and hierarchical process. The worker should not be required to learn anything not necessary to the task. Learning a relatively small part of the system should reward the worker with the ability to perform some limited amount of real work. Chafin [7] recommends that the worker be given only that capability required to do a specific task, and not unnecessary capabilities. Branscomb and Thomas [4] recommend that architectural system design include a layered interface. This means there would be several groups of commands. The beginner would start with a small group of useful and fairly intuitive commands. Then, as the user profile is updated by the system to indicate sufficient growth in knowledge or needs, new groups of commands would be introduced.

System generated instructions or communications should always be in task related natural language. Learning a new language can be very taxing on a worker's memory. Wasserman's [27] list of design principles for "idiotproof" interactive systems includes minimizing the need for the user to learn about the computer system. In Warner's outline for designing user interfaces [28], speaking the user's language" is the first criterion. For example a prompt for a marketing manager should read "Enter The Monthly Sales Target For the Western Region" rather than "Enter Dependent Data Set."

Terminology should be consistent throughout all software with which a worker will interface. This concept could be critical to minimizing worker memory. If the worker is required to memorize one set of terminology in order to update his data file, another set in order to run some analyses, another set in order to format a report, and yet another in order to send that report to his boss's terminal, the memorization required can only be imagend. One of Martin's objectives for data base organization [20] is a single, powerful user language which would "permit untrained users to query, search, and updata data in a data base; to manipulate the data; and to generate reports or documents which use it." This objective was also a finding of the ANSI/SPARC Data Base Management System Study Group in 1975. Warner [28] also agrees with this principle of consistent terminology throughout a system and says it must be in "the user's vocabulary." His examples include command protocol, sequential prompts, menu options, and error messages which must have consistent terminology.

Commands used by the worker should be in natural language syntax form and should be simple rather than complex or compound. Simple, natural language commands would require the least memorization by the worker. Yet Gould and Lewis [15] explain that there can be also an element of confusion in natural syntax. Sometimes the natural language command that system designers think easiest for the worker may confuse the worker.

Benbasat and Wand [3] found that 80 percent of users can comfortably adjust to command truncation. Banning [1] goes beyond simple, natural language syntax to provide icons, visual objects familiar to the worker, to which his system points. Foley, Wallace, and Chan [13] also suggest visual forms as a natural language communication method. However, they warn that use of everyday environment forms can present conflicts similar to the syntax confusion found by Gould and Lewis [15]. The examples given by Foley, Wallace, and Chan [13] include turning a steering wheel left which will move the care to the left but the visual image through the winshield to the right. Another contrast is presented by calculators with 1, 2, 3 in the row above 0 versus phones with 7, 8, 9 in the row above 0. Testing the software should reveal these potential natural syntax and visual confusions.

## 2.3. Minimize Worker Frustation

Systems should spare the worker frustations that may arise from a delay in the accomplishment of a task. Chafin [7] recommends that a program notify the user if an operation will take longer than 15 seconds. He suggests that worker frustration at a long response time can be minimized by a system message indicating expected duration. Thus, the worker may leave the machine and know approximately when to return rather than waiting and not knowing how much longer it will take. He suggests an audible signal to call the worker back when the operation is completed, as well as an abort capability that will not destroy program integrity.

Murch and Snyder [8] confirm that user fatigue and mental lags are brought on by comparatively slow system response times. Doherty and Kelisky [11] found that each second of system response degradation leads to a similar degradation added to user's time for the following command, a phenomenon apparently related to the individual's attention span. Increases in system response time seem to disrupt the thought processes. To continue, users may have to rethink the sequence of actions and become frustrated.

If menus, prompting or other guidance techniques are used, the system should permit the experienced user to bypass them. Guidance techniques are definitely an advantage to the beginner or the casual user, but a stream of system messages and prompts he no longer reads frustates the user. Dean [9] notes that some system messages are useful when learning a program and that as the worker gains experience these messages are ignored. He recommends that the worker should be able to select those system prompts which he no longer wants displayed. However, if the worker is allowed to turn off system messages that warn of critical errors, more frustration may be created than removed.

Morland [21] recommends that the structure of function selection screen presentation in interactive system terminal interfaces be linear rather than hierarchical. The experienced user could enter a function code which would immediately display the function screen desired without sequencing through the levels of a decision tree.

If a worker is interrupted in the performance of a related series of actions, the system should (upon request) provide a summary of the actions performed prior to the interruption. If a worker's thought process is broken by the system or by some external occurrence, even for a short time, he will probably not remember precisely where he was in the task that was interrupted. If the system does not provide such an option, the interrupted worker is forced to retrace his actions manually and, especially if he is involved in a complicated task, he could easily become frustrated.

Guidance techniques should be hierarchically organized so that the worker does not have to perform or explicitly bypass unnecessary steps. Warner [28] suggests that the system provide two user interface shells, one for the beginner and another for the expert. At the beginning of a session, the worker can choose the desired interface. Having the ability to choose a help level could minimize frustration in using the system.

Help should be obtained by touching a specific function key at any time that the help is needed. This function key should always be the same key regardless of what part of the software application or software environment is being used by the end user. Help should be available at any time and at any point in the user's operation of the system. Help should be provided to the user in several layers. Level 1 would give a simple instruction of what the user is expected to do at this point (or providing the user options at this point). Level 2 would give a more detailed explanation of what the user may do and any limitation on user actions at this point. Level 3 would give cross references to commands or activities related to this particular help statement. Level 4 would give references to the user manual or system documentation for extensive off-line investigation.

Chafin [7] recommends that an application contains a help function displaying the hierarchical structure of the program in graphical form and that can be called from anywhere in the program. Warner [28] also feels that on-line help should be available throughout the system and that multiple levels of help screens should be provided.

The worker should be able to interrupt or terminate any activity at any point and select another activity. After completion of the second activity, the system should permit resumption of the interrupted activity at the point of interruption by a simple action such as one keystroke (or the equivalent).

If a worker is updating a file and suddenly gets an urgent call to print a copy of a report submitted earlier and that this must be done quickly, the worker must stop what he is doing and comply. Then what? When the worker goes back to what he was doing, he would be relieved to be able to resume his file updating smoothly. Chafin [7] recommends an abort key function be present in an application to allow the worker to interrupt an operation without destroying the program's integrity. DeSanctis and Courtney [10], as part of their recommendation that the user must be as friendly to the system as the system to the user, make the point that the process of implementation must acclimate the user to these operations early.

Installation of hardware or system software should be supported by self-configuration and self-verification techniques. These techniques should be automatically applied so that the system is completely usable at startup. Many systems require a worker to run through a series of installation instructions in setting up and testing both the hardware and the software. Should be worker make the mistake of installing a monochrome monitor when he has a color monitor, he will be frustrated if he has to go back through the entire installation procedures to respecify the monitor option.

This principle may be approaching the realm of “adaptive restructuring” explained by Rauzino [24] as a right-brain type function for which the computing capability does not yet exist. It would be no small problem to create a software system that could configure any combination of components. In order for the system to automatically self-configure and self-verify, there would have to be a limited set of software and hardware options pre-programmed on the system that could be installed and recognized by the system. However, with this restriction, it would be possible and advantageous to have a system that would automatically start without worker effort.

Feedback should be provided for any action for which the results are not immediately obvious. This feedback must meet Dean's [9] criterion of being self-explanatory. He also suggests a system tolerance for user errors. For example, the system would evaluate inputs that may not be exactly right and use them if the correction is obvious, or make a probable correction and request the worker to confirm. The higher the percentage acceptance of user input, the better the potential to minimize worker frustration.

Warner [28] also cites feedback as a criterion in designing user interfaces. A delay in system response can lead the worker to wonder if something went wrong. He recommends that for every action taken by the worker there should be a reaction from the system within about half a second. As mentioned earlier, Chafin [7] recommends that a system message should be provided if an operation will take longer than 15 seconds.

## 2.4. Maximize Use of Habit Patterns

Systems should respond to the human tendency to form both long- and short-term patterns of action. A system should be designed with the capability to adjust itself for changes in the ways that it is used. If an organization acquires a system with the main objective of tracking internal expenditures and the system gradually is used by company engineers for other types of analyses, the system should track this pattern and self-adjust to remain responsive. Branscomb and Thomas [4] recognize the need to keep track of usage patterns and use the information to adjust the system to these user needs and preferences.

Systems should take advantage of “muscle memory.” As a worker becomes more familiar with a system, he should be able to find a function key needed without difficulty just like a typist using a typewriter. The worker should be able to expect to glance at a spot on the screen and find a given piece of information, like the connect-time or menu prompt. These are examples of “muscle memory,” the reaction of muscles of the user based on habit, formed by constant repetition, rather than specific conscious thought.

Hansen's engineering principles [27] of interactive systems also include optimizing “muscle memory.” Dean [9] suggests a terminal key to re-display previous input for changes. Chafin [7] recommends a help function key that can be used at any point in an applications program; he also suggests a backup key (in case a worker makes an error and wishes to return to the previous step) and an abort key (to stop long operations without crashing the program). One of the features Warren [30] points out about the Supercalc software package is that it includes single-key input for commands and menu selection, and he points out that Visiterm has single-key macro definition capability. All of these suggest consistent, single-key, “muscle memory” functions which help to maximize use of habit patterns by the worker.

Information returned on a screen to a worker should be positioned at the point where the worker expects the response – usually on the following line. Dean [9] suggests that when an input is in error the easiest way for the system to demonstrate to the worker what specifically needs correction might be to show the input in error along with the error message.

The worker should be able to accomplish tasks using a single consistent approach and terminology for all functions. For system developers, this would imply a single language for development that includes all command language, application language, and data manipulation language in one consistently structured language with a common syntax and terminology. Thus the worker should be able to form a language pattern with the system. Martin [20] describes the several levels of languages needed for a data base management system – including the programming level, data manipulation level, subschema description level, schema description level, and physical data description level. He recognizes the desirability of a single, consistent approach at each level, with compatible syntax among all the languages required at the different levels so that it appear to the programmer as though he is using a single language.

Performance of office functions on a computer-based system should require as little retraining as possible. For example, typing a letter on a text processing system should be as close as possible to performing the same activity on an office typewriter. If a worker is accustomed to checking his schedule book at the beginning of each day, he could do so using the computer and the format displayed by the system be as close as possible to that of the hardcopy schedule book.

The system designed by Banning's [1] company displays images of a file drawer containing documents representing files not in use and a desk top with open files on it representing files accessible to the worker. The concept of using files in performing a task is very familiar to workers and the system use of this approach means that retraining has been minimized.

## 2.5. Maximize Tolerance for Human Differences

Systems should be designed to accommodate the fact that people think differently, just as terminals are being designed to tilt and swivel to adjust to human size differences. Systems should store profiles of the way in which an individual worker prefers to perform tasks. These profiles should condition the system to the worker's use pattern when the worker signs on.

When the worker logs onto the system, it would automatically configure itself to operate in the mode and manner desired by the worker. Morland [21] recommends that the system accommodate differences in skill levels by allowing the more experienced workers to go at a faster pace. This could be accomplished by presenting abbreviated screen cues and input fields, or by merging several “novice” screens into more compact advanced worker screens. The worker could thus engage the novice level screen mode of the advanced level, and the preference could be entered as part of the user profile.

Branscomb and Thomas [4] recommend user profiles in architectural system design. They use the IBM ADS message system as an example. ADS has a profile for each worker based on his experience. This profile can either be changed directly by worker choice or by a system algorithm based on the number of interactions between the worker and the system. They also recognize a difference among workers in regard to type of input and output media preferred and feel that the system architecture must accommodate this difference as well.

The system should provide both visual and audible attention-getting methods, designated by the worker. These may include highlighting or blinking signals on a screen, a light signal separate from the screen, a buzzer or bell, etc. Some persons object to loud noises, while others find blinking lights bothersome. Barr and Rogers [2] recommend an audible signal in a communications package once connection with the host is achieved, but they do not recommend worker selection of that attention-getting signal.

In guidance techniques or in complex use such as query development, the system should support both procedural and non-procedural approaches. A system designer cannot possibly predict all the tasks that his system might be asked to perform by different workers during its lifetime. The system should also be able to accept non-procedural requests, with more than an error message in response. Reimann and Waren [25] state that a critical feature for DSS modeling is the capability to support statements in any order desired and refer to variables not yet defined. They call this capability “nonprocedurality”.

## 2.6. Maximize Tolerance for Environmental Change

In light of the rapid advances in hardware technology and the high probability that the original software system will not be used without changes forever, the system should support, with minimal worker effort, change of the hardware/software environment or changes to applications as a result of new functional requirements. Brownstein and Lerner [6] specify flexibility and expandability as criteria to be evaluated in selecting a software package. Martin [20] states that one of the two essential aspects of data base design is that data be independent of the programs that use them so that they can be modified without restructuring those programs. Gould and Lewis [15] use IBM's ADS system as an example and explain that its design allows changes in the user interface with no reprogramming required; changes are simply a matter of editing the control tables. This concept is related to the previously described feature that the system should automatically self-configure and self-verify at start-up. It would be desirable to have the system automatically re-configure and re-verify for changes that should take place, such as upgrading a printer or adding a graphics plotter.

An automated system that must recompile an applications program after minor changes is likely to be avoided by any worker because of the delays in performance and the tie up of processing time. Rauzino [24] defines a program as “a data-independent solution to a problem”. These coincide with Fried’s principle that change in data base content should have no repercussion on the applications program.

Application programs should be compatible and transportable among different models of computers. Upgrading machines and programs without major reinvestments of time and money due a compatibility problem is vital. Korns' [18] objective in his research project, Reason, was to develop a highly intelligent software system as independent of its supporting hardware as possible to be easily transportable to succeeding generations of computers. The result was a software called Lision which was based on the power and flexibility of a new system model called the "software'bus." Based in engineering rather than algebra and system theory, this software-bus is really just a data-transmission protocol which allows updates to be done by replacing one, or more, of the bus-integrated components.

Kernighan and Morgan [17] note that software written in assembly language is not transportable to any other machine. If a high level compiler is available, an operating system such as Unix can be moved to that new environment, but even that it is not a trivial undertaking.

Space allocation for files should be automatic and not require worker intervention or specification. All his attention would be focused on the task. Rieman and Waren [25] suggest that a good DSS software package will automatically manage data file manipulation so that the worker can move between modules without worrying about physical file storage. Martin [20] discusses tunability and data migration as two objectives of data base organization. Adjusting storage organization to improve performance (tuning) and moving frequently accessed data to storage locations where it can be quickly accessed (data migration) should be automatic functions in future data bases.

## 2.7. Notify Users of Problems Promptly

The worker should be notified of a problem as soon as it is detected and be notified of potential problems in advance of their occurrence. Korns' [18] software package, Lision, included an interactive debugging capability which seems to embody Fried's concept of interactive system monitoring of input. One of Cheriton's [27] criteria for interface design for time-sharing systems is that they protect the user from costly mistakes or accidents. Morland [21] feels strongly about the need to provide a warning to experienced workers who enter data very rapidly without looking at the screen. Morland suggests the use of an audio interrupt for this purpose, with the severity of the error reflected in the tone of the signal. Another warning flag might be the use of highlighted areas where the frequency and brightness indicate the urgency of the error.

Before making a permanent change to stored information, the system should show the results of that change and require worker approval. If the system does not do this, the worker could unintentionally destroy a great deal of work without intending to do so. Neumann [23] insists on explicit confirmation if a user request might have serious consequences such as irrevocable deletion.

Any requests by the worker that are not understood by the system at the time they are made should generate a helpful response from the system. This response should be immediate and before the worker has entered a whole series of parameters for the command. This response should explain exactly what the problem is and what is required to correct the error and proceed. Warner [28] calls this “empathizing” with the worker. The system should tell the worker in a succinct, yet friendly way when an error is detected and what type of correction is required. The diagnosis of the problem and the appropriate corrective action should be displayed on the screen in the worker’s vocabulary and should not refer the worker to a manual. Schneiderman [27] states that when an error is detected, the system should generate a message stating the problem encountered and then guide the worker in entering the correct command. The message should not be meaningless or embarrassing to the worker but rather should indicate where the error occurred and what may be done to set it right.

The worker should be notified by the system when file capacity has become filled to within a substantial percentage (such as 80 percent) of total system capacity so that the worker can take appropriate action. This helps the worker to avoid a disastrous message like “File Space Exhausted, Overwriting.”

At the conclusion of the worker's correction of the error condition, the system should return the activity to the point at which it was interrupted. Making a mistake and then correcting it should not prevent the worker from finishing the task. He should not be forced to retrace steps already completed correctly nor should be forced to start from the beginning.

## 2.8. Maximize Worker Control of Tasks

The worker should control the flow and sequence of work to the extent possible where there are no sequence-dependent activities. The worker should be able to modify the priorities of processing to be performed by the computer such as changing the sequence in which letters or reports will be printed. This concept of worker control of the system is encompassed by Cheriton's [27] criteria for interface design for time-sharing systems which include the requirement that all actions be initiated and controlled by the worker.

The worker should be able to establish his or her own terminology for functions, commands, or data, and have this idiosyncratic terminology “remembered" by the system for future use. For example, the terms couch, sofa, and chesterfield all refer to the same piece of furniture and each of three workers on the system might prefer to use a different term. This applies not only to datum names but also to function and command names. Branscomb and Thomas [4] propose a synonym table which would be automatically updated to include commonly used terminology. Barr and Rogers [2] discuss the importance of the worker-defined macro facility in a communications package which allows the worker to store a long dial-up and log-on sequence for future use. Both of these are facilities whereby the system-recognized terminology is tailored to the preference of the worker.

The worker should be able to define default options for given tasks and have these default options remembered by the system for future use. The capability of the system to allow the worker to “personalize his environment” is also one of Cheriton’s [27] criteria for interface design for time-sharing systems.

The worker should be able to store and retrieve information in a consistent manner, with the residence of the information being transparent to the worker. This relates to Fried's earlier concept concerning allocation of file space. The worker should not be disturbed by (or even need to know about) the details of system file storage. The system should automatically maintain the files without assistance from the worker.

## 2.9. Maximize Task Support

The system should provide complete support of tasks for the worker so that the worker is not required to use other resources for task performance. This parallels Fried's earlier concept for elimination of duplicate work. Switching modes from tool to tool will affect productivity and morale of the worker.

Durniak [12] suggests that the availability of integrated software packages is the reason that the microcomputer is now becoming an indispensable management tool. They enable the worker to keep track of all work simultaneously, without switching from one package to another and re-entering data, thus providing the support environment contemplated by Fried.

From any level in task performance the worker should be able to view the structure of his data because it would minimize the effort in performing his work. If a hierarchical help function is available on-line, why not have on-line hierarchical task documentation also available? If the worker is creating a total comprehensive budget file which depends on a voluminous set of budget files at the next level down, he should be able to find the names of these files without leaving the top level budget file. In outlining criteria for interface design for time-sharing systems Schneiderman [27] cites “self-documenting” as a system requirement.

Fried proposes as on-line, interactive communications capability that would allow the worker to locate and obtain exactly that information which he wants, whether preplanned or ad hoc. Brown [5] discussed local area networks as a key feature in making office automation “user friendly,” saying that it speeds up services and increases efficiency by tying separate offices together. Reimann and Waren [25] call communications a “vital feature” of an effective DSS and suggest that it include multiple linkages to other packages and languages and permit easy uploading and downloading of data, results and models.

Barr and Rogers [2] outline the functions that they feel should be part of the ideal communications package. Among other items included on their list are efficient uploading and downloading, software filtering, addressing peripherals of worker choice, macro facilities, and creation of special data signals for the host.

## 3. Ergonomic Software: An Agenda for Action

The increasing use of the principles described here in the years after Fried's original work indicates that there are several desirable actions which are necessary in order to take advantage of their practically and specificity. The first, and probably easiest, is the development of a rating scale based on the criteria. The next time an organization is planning to establish a network using an interactive software of any type, the principles can be applied to rank the alternatives. This approach would be a much more systematic way to aid in multi-million dollar decisions for long-lived system selection.

The second action is more challenging and concerns standards for software development. In an era of guidelines for work station design, and for recommended interfaces for compilers and data communications software, even for the use of documentation, it seems that we could be ready for an action where the return on investment would be high even though the investment is low. Are we not ready for software standards based on the ultimate beneficiary? We feel that international guidelines for ergonomic software are needed. If such guidelines were developed along the lines we have suggested, software suppliers might become as conscious of meeting users' needs as those of the computer manufacturers'. Also, there could be an unprecedented opportunity for software's improvement curve to move into the double digit range, like that of hardware components such as memory and ALUs.

We have attempted to demonstrate that ergonomic requirements are practical and definitely in the main stream of software development. But we try also to make a more significant and far reaching point – that current software development processes may be applying criteria which miss the essential characteristic of its milieu. By concentrating on the user more explicitly through the use of these criteria, it may be possible to arrive at systems which are better and less expensive because they are more satisfying.

## References

[1] J. Banning, Beyond the Application Program, Byte, Vol. 9, No. 1, January 1984, pp. 251-252+.

[2] D. Barr and G. deW. Rogers, Looking for the Perfect Program, Byte, Vol. 9, No. 13, December 1984, pp. 199–210.

[3] I. Benbasat and Y. Wang, Command Abbreviation Behavior in Human-Computer Interaction, Communications of the ACM, Vol. 27, No. 4, April 1984, pp. 376–383.

[4] L.M. Branscomb and J.C. Thomas, Ease of Use: A System Design Challenge, IBM Systems Journal, Vol. 23, No. 3, 1984, pp. 224–235.

[5] J.G. Brown, The Friendly Future in Office Automation, Computer Decisions, Vol. 14, April 1982, pp. 144–154.

[6] I. Brownstein and N.B. Lerner, Guidelines for Evaluating and Selecting Software Packages, Elsevier Science Publishing Co., Inc., New York, 1982.

[7] R.L. Chafin, Human Factors in Applications Programming, Infosystems, Vol. 30, June 1983, pp. 102-104.

[8] D. Davies, More Graphics Firms Stressing Ergonomics, Management Information Systems Week, 18 May 1983, p. 17.

[9] M. Dean, How a Computer Should Talk to People, IBM Systems Journal, Vol. 21, No. 4, 1982, pp. 424–453.

[10] G. DeSanctis and J.F. Courtney, Toward Friendly User M.S. Implementation, Communications of the ACM, Vol. 20, No. 10, October 1983, pp. 732–738.

[11] J. Diebold, How New Technologies are Making the Automated Office More Human, Management Review, Vol. 73, No. 11, November 1984, pp. 9–17.

[12] A. Durniak, Anthony, New Software Takes Drudgery Out, Business Week, 13 December 1982, p. 73+.

[13] J.D. Foley, V.L. Wallace, and P. Chan, The Human Factors of Computer Graphics Interaction Techniques, Computer Graphics, IEEE, Vol. 4, November 1984, pp. 13–48.

[14] L. Fried, Nine Principles for Ergonomic Software, Data-mation, Vol. 28, No. 12, November 1982, pp. 163–166.

[15] J.D. Gould and Clayton Lewis, Designing for Usability: Key Principles and What Designers Think, Communications of the ACM, Vol. 28, No. 3, March 1985, pp. 300–311.

[16] A. Kay, Computer Software, Scientific American, Vol. 251, No. 3, September 1984, pp. 52–59.

[17] B.W. Kernighan and S.P. Morgan, The Unix OS: A Model for Software Design, Science, Vol. 215, 12 February 1984, pp. 779–783.

[18] M.F. Korns, Reason and the Software Bus, Byte, Vol. 9, No. 1, January 1984, pp. 104–106+.

[19] L. Koved and B. Schneiderman, Embedded Menus: Selecting Items in Context, Communications of the ACM, Vol. 29, No. 4, April 1986, pp. 312–318.

[20] J. Martin, Computer Data-Base Organization, Prentice-Hall, Inc., Englewood Cliffs, N.J., 1977.

[21] D.J. Morland, Human Factors Guidelines for Terminal Interface Design, Communications of the ACM, Vol. 26, No. 7, July 1983, pp. 484–494.

[22] A.S. Neal and R.M. Simons, Playback: A Method for Evaluating the Usability of Software and Its Documentation, IBM Systems Journal, Vol. 23, No. 1, 1984, pp. 82–96.

[23] P.G. Neumann, Psychosocial Implications of Computer Software Development and Use: Zen and the Art of Computing, Theory and Practice of Software Technology, Elsevier Science Publishing Company, Inc., New York, N.Y., 1983.

[24] V. Rauzino, Conversations with an Intelligent Chaos, Datamation, Vol. 28, No. 5, May 1982, pp. 122–136.

[25] B.C. Reimann and A.D. Waren, User-Oriented Criteria for the Selection of DSS Software, Communications of the ACM, Vol. 28, No. 2, February 1985, pp. 166–179.

[26] P. Schmidt, What's New in Computer Psychology?, New York Times, Vol. 134, Section F, 20 January 1985, p. 15.

[27] B. Schneiderman, Software Psychology, Little, Brown and Company Limited, Toronto, 1980.

[28] J. Warner, Designing User-Friendly Graphics Software, Hardcopy, July 1984, p. 180.

[29] C. Warren, This is the Year of Software, Popular Electronics, Vol. 19, No. 8, August 1981, pp. 62–63.

[30] C. Warren, Systems and Software, Popular Electronics, Vol. 19, No. 11, November 1981, pp. 32–33.
