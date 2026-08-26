---
otero_id: 18671
otero_key: "QWV7UYFC"
title: "Artificial intelligence based simulation in the design of a GDSS idea generation tool"
authors: "Milam W. Aiken; Olivia R. Liu Sheng"
year: "1991"
journal: "Information & Management"
doi: "10.1016/0378-7206(91)90004-l"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
Techniques

# Artificial intelligence based simulation in the design of a GDSS idea generation tool

Milam W. Aiken and Olivia R. Liu Sheng

Department of Management Information Systems, University of Arizona, Tucson, AZ 85721, USA

Little research has been conducted on the software engineering design problems of group decision support systems (GDSS). We believe this has been due in part to the lack of powerful system design methodologies, such as Artificial Intelligence Based System Simulation (AISS) techniques and also, in part, due to a lack of research direction. The AISS design methodology described here is split into three stages: the specification of system boundaries using a System Entity Structure (SES), SES pruning and model synthesis using an expert system (ES), and the evaluation of candidate design models using discrete event simulation (DEVS). This paper presents an example of applying AISS to the design of a GDSS Idea Generation tool. Simulation results show that the selected model meets the design criterion of equitable distribution of comments among group participants.

Keywords: Software engineering, Simulation, Expert systems, Artificial intelligence, Group decision support systems.

## 1. Introduction

![](/api/attachments/QWV7UYFC/fulltext/images/3e9de27248144cf62baf0c6009892c0e5a887540e3e3aef0b547374e0d56c174.jpg)  
decision support systems. He is a member of the Academy of Management and the Decision Sciences Institute.

Milam W. Aiken received the B.S. degree in Engineering and the Master of Business Administration degree from the University of Oklahoma and the B.A. degree in Computer Science and the B.S. degree in Business from the State University of New York. He is currently a Ph.D. student in Business Administration with a major in Management Information Systems at the University of Arizona. His research interests include expert systems, office automation, and group

The field of group decision support systems (GDSS) has spawned a great deal of research regarding the nature of electronic group support $[5,6,9,10,15,31]$ , but little effort has been made to study group dynamics and tool development using simulation $[19]$ . One reason for this is the focus on qualitative aspects rather than objective quantitative aspects that can be modeled in this way. Researchers have shown through case studies, field studies, and laboratory experiments that a GDSS can reduce the time necessary to reach agreement, foster consensus, and lead to satisfactory meeting results $[4,14,21,22,25,34]$ . Simulation of a GDSS can show potential bottlenecks of communication, refine tool designs without lengthy subject testing, and reveal a variety of results that are unavailable to researchers, except through repetitive time-consuming sessions $[11]$ . The Artificial Intelligence Based System Simulation (AISS) technique facilitates system simulation through comprehensive representation of system variables and automated model synthesis. This greatly reduces the time necessary to design and evaluate the system.

![](/api/attachments/QWV7UYFC/fulltext/images/ebfeba83ab5d04ee769ecc3008381a204f0d2523b8ffb5393898c0e3a6154e0c.jpg)

Olivia R. Liu Sheng received the B.S. degree from the National Chiao Tung University in Taiwan, R.O.C. and the Master and Ph.D. degrees in Computers and Information Systems from the University of Rochester. She is an Assistant Professor of Management Information Systems at University of Arizona and a consultant to Toshiba Corporation on database design for medical image data. She is a member of ACM, IEEE, ORSA, and TIMS. Her current research interests include analysis and design of distributed database and knowledge systems, pictorial and image data management, automation of systems analysis and design, computer-mediated communication support, distributed group work support, integrating office information systems, and manufacturing information system design.

Many facets of the design process have already been successfully computerized $[23,32,33]$ . For example, various expert systems have been developed to replace the traditional trial-and-error methods in design synthesis including R1/XCON for DEC minicomputer configuration $[12]$ , PRE-DIKT for the design of domestic kitchens $[26]$ , and the Logic Synthesis System (LSS) for the design of logic circuits $[7,27]$ . However, AISS presents a more structured and complete methodology for system specification, design, and evaluation. It has potential for improving the productivity of system developers in numerous areas, though most efforts to date have been concentrated on the development of hardware systems. For example, AISS has been used for the design of Local Area Networks $[18,30]$ . However, it has great potential in the area of software design through modular reusability. Here, we illustrate how it can improve software productivity through hierarchically structuring reusable code, using an expert system to select applicable modules and synthesize candidate designs, and finally testing these designs based upon specified performance criteria. In particular, we focus on the special design considerations of a GDSS tool for idea generation and test the generated candidate designs for their file distribution characteristics.

This methodology is applicable to managers, in that it presents another technique for enhancing system development productivity. Although we focus on developing a GDSS tool, AISS is applicable to any software or hardware system. The technique serves as a useful adjunct to the system developer as one of many possible development methodologies.

## 2. AISS in GDSS Development

## 2.1. Simulation and GDSS

Many unexplored areas remain in the purview of GDSS; some of these are amenable to quantitative study. Areas yet to be investigated include optimal GDSS architectures and characteristics of group support tools under widely varying loads. For example, much may be revealed by simulating an idea generation tool while varying the amount of time it takes to generate comments, their inter-arrival times, and their distribution (e.g., normal, exponential, uniform, and Poisson).

Simulations allow us to emulate and compare the performance of different combinations of subsystems in a GDSS. They can also identify characteristics of a GDSS that may limit or enhance functionality or performance. To a certain extent, these goals can be accomplished with the actual system hardware, software, and group participants, but simulating components, interfaces, and throughputs can offer more efficient, comprehensive, and inexpensive ways of evaluating complex interactions among widely diversified parameters.

Simulations can be used profitably when group support systems have been specified and designed but not yet released. They can identify both potential performance improvements and difficulties when running with different combinations of subsystems. Simulations can estimate how much advantage could be gained by installing different subsystems without the time-consuming process of actually obtaining and installing them. Because simulations can represent each interchangeable part of a system by a separate and distinct model, components can be rapidly exchanged during the experimentation process.

Probably the most important use of simulation is in testing the performance of systems running under atypical workloads. The goal is to produce an overloaded system and then examine the simulation to determine where the failure occurred. By locating where performance worsens, designers may be able to trace the degradation to a single component (the bottleneck) that cannot handle those work-loads efficiently.

Some previous work has demonstrated how simulation can be used in the area of GDSS. Herniter et al. [13] have described how the AISS methodology can be used to simulate a group session featuring three different types of tools. In addition, they describe a simulation of a local area network to determine configurations for maximum throughput and response time of an interactive GDSS. Aiken and Hayes [3] have described results simulating various group participant characteristics while using the Nominal Group Technique and the Electronic Brainstorming tools. More work, however, needs to be done on how to build these tools in light of the group simulation results as well as results from numerous experimental, case, and field studies.

![](/api/attachments/QWV7UYFC/fulltext/images/c4a28389f2057152be277d3c8c019c558feafbdc08807ae909762179bdd7668e.jpg)  
Fig. 1. System Specification, Analysis, Synthesis, and Simulation (from [28]).

## 2.2. Discrete Event System Simulation

The success of simulation depends in part upon the particular technique and language chosen. A discrete event simulation (DEVS) language such as DEVS-Scheme is an ideal tool for the study of design models. DEVS-Scheme, available at the Artificial Intelligence and Simulation Laboratory at the University of Arizona, is built on top of SCOOPS (Scheme Object-Oriented Programming System), the object-oriented superset of PC-

![](/api/attachments/QWV7UYFC/fulltext/images/5034858761a669b93648aad2f3749264638a0ac0191d488167df3ed6b5ecd4c0.jpg)  
Fig. 2. The System Entity Structure (SES).

Scheme available from Texas Instruments [37]. Models are developed in Scheme syntax, using the DEVS language overlay to create and manipulate Scheme structures and SCOOPS objects to describe the model [36].

DEVS-Scheme has several features that make it valuable for modeling and comparing different hardware and software systems. First, it simplifies the development of modular models. In a more traditional simulation environment, the system would have to be modeled as a single structure. Each component of the GDSS would be a part of that model, interconnected and inseparable. Modifying the simulation to consider other combinations of components would mean essentially rewriting most of the simulation from scratch.

With DEVS-Scheme, components of larger models can be written as stand-alone models, able to run dummy inputs, or inputs from the keyboard, rather than from other components. A second, and related advantage of DEVS is that its structure is hierarchical in nature. This enables a model to approximate a system more closely through successively more refined components.

DEVS-Scheme possesses some desirable characteristics but is generally limited to academic environments. Although DEVS-Scheme was used for the development of models in this simulation, any more commonly-available language may be used instead.

## 2.3. The AISS Methodology

The technique, as developed by Zeigler and Rozenblit [28], is performed in three stages: System Entity Structure (SES) definition, candidate model definition, and candidate model simulation (See Figure 1).

## 1. SES Definition

A System Entity Structure incorporates knowledge about a system through three basic relationships: decomposition (breaking up a system into component parts), taxonomy (listing variants of an object), and coupling (how model components interact). System configuration and performance variables are identified and attached to their respective system components. The resulting tree-like structure represents all possible configurations of the system model. As shown in Figure 2, system or model components (called entities) are linked hierarchically. Aspect relationships show that an entity is composed of several other entities. For example, the entity car has the entities engine, body, and wheels as component parts in a physical composition aspect. Taxonomy or specialization relationships, on the other hand, give variants of an entity. For example, the entities stationwagon and sports coupe are specializations of the entity car. Specialization entities inherit the aspects and attributes of parent entities. In the example, the entity sports coupe inherits the car physical composition aspect parts engine, body, and wheels. Uniformity and inheritance properties of the SES ensure a consistent and concise representation of the problem domain.

## 2. Candidate Model Definition

After the system boundaries and variables are defined, the SES is pruned to obtain substructures of components that exhibit desirable characteristics. In the case of large, complex system entity structures, expert systems may be needed to facilitate the selection of components. Repetitive pruning with differing selection criteria results in several possible components which must be synthesized into candidate design models $[29]$ . These are then tested with simulation techniques. For example, an expert system may identify several possible software modules to meet a system developer's goals and constraints. Individual modules are pruned from the SES if they meet the user's specified criteria. These individual modules are then joined into subsystems based upon synthesizing rules (some modules cannot be linked together, for instance). These subsystems are then tested via simulation to determine which is the best configuration.

It is important to note that no systems are actually built until after the best configuration has been identified via simulation. In the example, no coding is actually done yet. At this stage, only modules and subsystems are identified along with their applicable attributes, such as algorithm complexity, file size, supporting hardware limitations, capacity for input and output, and all other criteria that are important to the system developer. These criteria will be used in the simulation stage.

## 3. Candidate Model Simulation

Experimental frames are next developed for performing simulations on the candidate models. These control the simulation run, provide event generation, and measure and record system data. For example, for testing software subsystems, an experimental frame may be identified to run a simulation for one hour, provide sample input to the subsystem, and record all output from the software system. Finally, simulations using any good DEVS language (such as DEVS-Scheme) are performed on the candidate models. Results from these simulations determine which of the candidate models is the optimum choice.

## 3. Idea Generation Characteristics

One problem that faces designers of GDSS tools is that of efficient and effective idea generation. Idea generation is one possible focus of the GDSS session, and several systems have been developed to support it including COLAB from Xerox PARC, CAM from the University of Minnesota, and GroupSystems from the University of Arizona [20]. The latter provides four tools specifically designed for idea generation including the Electronic Brainstorming tool, the Nominal Group Technique tool, the Automated Delphi Tool, and the Topic Commenter tool [1].

Computer-supported idea generation has several advantages over manual techniques, including automated journaling, rapid generation of ideas, and anonymity. The goals of any idea generation session include: (1) generating as many ideas as possible during a set amount of time, (2) a quick system response time, and (3) an equitable sharing of ideas among the group participants. All three of these goals can be studied using simulation techniques, but the third goal is the focus of this paper. Each group participant should have equal access to the ideas generated by all other participants. Although existing tools have assumed this to be true, very little research has been conducted to validate this assumption [35].

The Arizona GroupSystems Electronic Brainstorming (EBS) software in particular deserves extensive study due to its high frequency of use. EBS has been described as one GDSS tool that can foster group consensus-building, communication, and collaborative work [8]. The EBS tool is founded upon a manual, paper-based brainstorming system in which each group participant writes down an idea on a piece of paper and exchanges it with a paper lying in the center of the table. The electronic approach extends the group size possible and provides automated journaling, record keeping, and other online support. It is traditionally used in a decision room environment with group participants meeting face-to-face.

![](/api/attachments/QWV7UYFC/fulltext/images/de07d257eb5068d557f1f9a060737f3188884692a019caef1d0df28270df68ae.jpg)  
Fig. 3. GDSS Idea Generation Tool SES.

The EBS tool begins the session with a blank file for each of the participants and an extra blank file at the central file server. When the first participant finishes, he swaps his file with this central file and begins writing more comments. The next participant to finish swaps with the file that the first participant began with, and so on. This may not result in an equitable or uniformly random distribution of files among the participants, however. It is generally not desirable or “equitable” if some participants see more comments than other participants. One way to achieve uniform distribution may be to add extra files at the central file server. Our task is therefore to design candidate

![](/api/attachments/QWV7UYFC/fulltext/images/db6567220ce560f97dcee2cc5ef7215d4b12518e43198325b30c6bc258921cf6.jpg)  
Fig. 4. GDSS Hardware SES.

![](/api/attachments/QWV7UYFC/fulltext/images/944127c7410047624e3fac670c4ce04f94578d178dd2dd81616a9f4c8574d7c4.jpg)  
Fig. 5. GDSS Software SES.

EBS models and evaluate them for idea sharing characteristics. AISS presents an ideal method to facilitate our task.

## 4. Developing an Idea Generation Tool

The AISS technique involves system definition via a system entity structure (SES), pruning of the SES and synthesis of candidate designs using an expert system (ES), and finally, simulation of candidate designs to determine the optimum configuration of the design. These steps are now outlined in detail.

## 4.1. SES Definition

First, we develop an SES which expresses components and variations of an idea generation

GDSS tool. One possible SES appears in Figures 3, 4, and 5. This knowledge representation of hardware and software components in a GDSS shows many common components. However, the GroupSystems utility modules are special to the system. Attributes and relationships among components are translated into rules for pruning and synthesis.

## 4.2. SES Pruning and Synthesis

The second step is to prune the SES and synthesize a design model using an expert system. An expert system for pruning and synthesis consisting of 40 rules was run on the EXSYS Professional expert' system shell developed by EXSYS, Inc. Since this expert system applies only to a very limited environment (GroupSystems software engineering), other environments must, of course, have a completely different and possibly larger set of rules. In addition, this expert system is in the prototype stage. Although it performs adequately with only 40 rules, many additional rules may be added in the future as new software modules are added.

Table 1  
Constraints Imposed on SES.

<table><tr><td>Constraint</td><td>Value</td></tr><tr><td>Size of group</td><td>small</td></tr><tr><td>Need to meet</td><td>face-to-face</td></tr><tr><td>Purpose of meeting</td><td>idea sharing</td></tr><tr><td>Screen type</td><td>windows</td></tr><tr><td>Distribution</td><td>random</td></tr><tr><td>Output</td><td>no printer</td></tr><tr><td>Input</td><td>text</td></tr></table>

Idea generation constraints imposed on the system appear in Table 1. This reflects the answers given to the expert system for the design of a particular GDSS tool for idea sharing that will support a small group that needs to meet face-to-face. In addition, the user wants the tool to accept text in a window environment for input but printer output is not necessary. For idea sharing, the user wants comments to be shared randomly. All of these factors help to determine which software modules are necessary to construct the GDSS tool.

The resulting recommendations appear in Table 2. This shows that the expert system recommends various file, graphics, string, and other modules as well as a number of data files. Certainty factors for each recommendation are based on a scale of 0 to 1, where 0 is certain evidence against the recommendation and 1 is certain evidence for the recommendation. A threshold of .7 was used to list only the most promising component selections.

Table 2  
Resulting Expert System Recommendations.

<table><tr><td>Recommendation</td><td>Value</td><td>Certainty Factor</td></tr><tr><td>Module type</td><td>Collaborative</td><td>0.85</td></tr><tr><td>Central Files</td><td>1</td><td>0.88</td></tr><tr><td>User Files</td><td>25</td><td>0.75</td></tr><tr><td>File Module</td><td>CopyFile</td><td>0.76</td></tr><tr><td>File Module</td><td>UserCheckUser</td><td>0.8</td></tr><tr><td>File Module</td><td>UserCheckPub</td><td>0.85</td></tr><tr><td>Misc Module</td><td>Randomize</td><td>0.9</td></tr><tr><td>Graphics Module</td><td>MakeScreen</td><td>0.86</td></tr><tr><td>Graphics Module</td><td>Frame</td><td>0.89</td></tr><tr><td>String Module</td><td>GetString</td><td>0.95</td></tr></table>

The synthesized subsystems of modules that will be simulated are exact duplicates except for the number of central files and user files present. By varying these, we can determine the best configuration for uniformly random comment distribution among group participants.

The use of AISS for module selection does not imply that no additional synthesis or coding is necessary by the model developer. Software components must be linked. In addition, the modules will not cover everything that may be needed by the model. The synthesized model presented by AISS does provide a very helpful foundation upon which to proceed, however. Experience has shown that once the fundamental components are identified, additional work is made clearer and easier.

## 4.3. Model Simulation

Up to this point, software designs have been identified and synthesized. Now, simulation coding must be written to target the performance criteria. Our particular area of concern is the equitable distribution of comment files among group participants. Although many other performance criteria may be specified, this paper concentrates only on file distribution as an example. Our candidate designs feature identical software components with the exception of the number of central and user files. By varying these, we will be able to determine the limits of the software system.

Of course, exhaustive simulation studies varying all possible factors is a waste of time and resources. By placing constraints on the simulations, we can reduce the amount of work needed to generate meaningful results with no loss of generality. For example, we set a simulated session duration time of 45 minutes (the average session duration) without studying session durations of 1 minute or 1000 minutes (although it may be useful to study these limits in other simulations).

Likewise, we will set the number of session participants at eight since some characteristics of large groups become evident when the group reaches this size. As the group size increases, the benefits of automated group support become more and more evident. Smaller groups can often resolve their problem or task without automated support. Alternatively, smaller groups using GDSS often exhibit secondary and tertiary channels of communication among participants – the system no longer becomes the primary means of communication. Members are more prone to talk to each other or communicate with body language in a face-to-face conference when participants are close at hand [39]. If the assumptions stated above hold, there should be no loss of generality to groups of 10, 20, or even larger. The simulated session duration of 45 minutes as well as the eight participants is based upon observation of numerous GDSS sessions [2].

Depending upon the turnaround time that each participant takes to generate a comment on a file, the number of participants, and the number of blank files, the resulting exchange of comments over the duration of an idea generation session may not be uniformly random (i.e., equitable in the distribution of files among participants). Of course, this could be determined by conducting many idea generation sessions, varying the number of participants and the number of blank files, but this is extremely tedious. Alternatively, a queuing theory technique may be available which can adequately model the problem. However, the time that is necessary to identify such a technique and to adjust such a technique to modifications in the model was deemed prohibitive. Therefore, simulation was chosen as the optimal methodology for this problem.

In our simulation, we want to know whether or not we can conclude that a series of items or events is random. One statistical technique used for testing such a hypothesis is the One Sample Runs Test [24]. A run is defined as a sequence of like events that is preceded and followed by an event of a different type, or by none at all. For each user, we apply the One Sample Runs Test since the data are recorded in the order of their occurrence and since they may be dichotomized according to whether the assigned file number is greater or less than the expected file number of 4.5 (9 files/2). We also apply the test to the user numbers seeing each file and the file numbers arriving at the central file server. These three types of runs are not necessarily alike in statistical characteristics. Since all of these data are in order of occurrence and two types of observations can be observed (file numbers above or below the median number and user numbers above or below the median), the One-sample runs test may be applied.

## Hypothesis:

H1: The pattern of two types of observation is determined by a uniformly random process.
Ha: The pattern is not uniformly random.

Normal distributions with different means and variances were used in the simulation to model the turnaround time of comments from the users. The Normal distribution was chosen based upon observation of participants during actual GDSS sessions. After 10 runs of the simulation for each of the three sequences, all sequences were found to be statistically random at the p = 0.025 level of significance. Further, the distributions were random over a long period of the simulated 45 minutes. Therefore, no modification of file distribution characteristics is deemed necessary. When eight participants are using the EBS tool, one central file is adequate for a uniformly random distribution of comments. Additional participants only improve this random distribution. Simulation runs with additional central files also showed uniformly random distributions. Therefore, the simplest candidate design model of one central file was chosen for the final tool.

## 5. Conclusion

This paper has shown how the Artificial Intelligence Based System Simulation (AISS) methodology can improve the construction and evaluation of hardware and software systems. A step-by-step illustration of the use of AISS for the design and simulation of a GDSS idea generation tool showed that the selected model displayed the necessary idea distribution requirement of a uniformly random sharing of comments among group participants.

Future research entails further evaluation of the methodology as a useful adjunct to the development of additional GDSS tools at the University for Arizona. New tools and modifications of existing tools necessitate extensive testing prior to their inclusion into the suite of GroupSystems software used on a day-to-day basis. Additional AISS simulations on existing GroupSystems software should be done to gain a better understanding of each tool's characteristics for the support of groups.

## Acknowledgments

We would like to thank Dr. J.W. Rozenblit and Dr. B.P. Zeigler for their suggestions and support of this research. We would also like to thank Lee Walker for providing information on GroupSystems software modules and Glenda Hayes for her simulation programming work.

## References

[1] PLEXSYS Manual, Department of Management Information Systems, University of Arizona, Tucson, 1988.

[2] Aiken, M., Chen, H., and Cooper, S., “Experiences with a Group Decision Support System: A Longitudinal Study,” working paper, Department of Management Information Systems, University of Arizona, 1990.

[3] Aiken, M. and Hayes, G., “A DEVS-Scheme Simulation of an Electronic Meeting System,” Simulation Digest, Vol. 20, No. 2, 1989, pp. 31–39.

[4] Bjerknes, G. and Bratteteig, T., “The Memoirs of Two Survivors,” Proceedings of the 1988 Conference on Computer-Supported Collaborative Work, Portland, OR, September 1988, pp. 167–177.

[5] Bui, T. and Jarke, M., "A DSS for Cooperative Multiple Criteria Group Decision Making," Proceedings of the 1984 International Conference on Information Systems, December 1984, pp. 101–113.

[6] Bui, T., Sivasankaran, T., Fijol, Y., and Woodbury, M., "Identifying Organizational Opportunities for GDSS Use: Some Experimental Evidence," Decision Support Systems, Conference Proceedings, 1987, pp. 68–75.

[7] Darringer, J. et al., “LSS: A System for Production Logic Synthesis,” IBM Journal of Research and Development, Vol. 28, No. 5, September 1984, pp. 537–545.

[8] Dennis, A.R., George, J.F., Jessup, L.M., Nunamaker, J.F., and Vogel, D.R., “Information Technology to Support Electronic Meetings,” MIS Quarterly, Vol. 12, No. 4, December 1988, pp. 591–624.

[9] DeSanctis, G. and Gallupe, R.B., “A Foundation for the Study of Group Decision Support Systems,” Management Science, Vol. 33, No. 5, May 1987.

[10] Gallupe, B., DeSanctis, G., and Dickson, G., "Computer-Based Support for Group Problem-Finding: An Experimental Investigation," MIS Quarterly, Vol. 12, No. 2, June 1988, pp. 277–296.

[11] Grudin, J., “Why CSCW Applications Fail: Problems in the Design and Evaluation of Organizational Interfaces,” Proceedings of the 1988 Conference on Computer-Supported Collaborative Work, Portland, OR, September 1988, pp. 85–93.

[12] Harmon, P. and King, D., Artificial Intelligence: Expert Systems in Business, John Wiley and Sons, New York, 1985.

[13] Herniter, B., Liu, K.C., and Pendergast, M., “Using Artificial Intelligence Based System Simulation in Management Information Systems Research: Three Case Studies,” in Advances in AI and Simulation: Proceedings of the SCS Multiconference on AI and Simulation, 28-31 March, 1989, Tampa, FL, R. Uttamsingh and A. Wildberger eds., Vol. 20, No. 4, pp. 147–152.

[14] Hiltz, S., Online Communications: A Case Study of the Office of the Future, Ablex Publishing, Norwood, NJ, 1984.

[15] Hiltz, S., Johnson, K., and Turoff, M., “Experiments in Group Decision Making: Communication Process and Outcome in Face-to-Face Versus Computerized Conferences,” Human Communication Research, Vol. 13, No. 2, Winter 1986, pp. 225–252.

[16] Hiltz, S. and Turoff, M., “The Evolution of User Behavior in a Computerized Conferencing System,” Communications of the ACM, Vol. 24, No. 11, November 1981, pp. 739–751.

[17] Hiltz, S. and Turoff, M., “Structuring Computer-Mediated Communication Systems to Avoid Information Overload,” Communications of the ACM, July 1985, pp. 680–689.

[18] Huang, Y.M., “Building an Expert System Shell for Design Model Synthesis in Logic Programming,” Unpublished master's thesis, Department of Electrical and Computer Engineering, University of Arizona, Tucson, 1987.

[19] Jessup, Leonard M., “Group Decision Support Systems: A Need for Behavioral Research,” International Journal of Small Group Research, Vol. 3, No. 2, September 1987, pp. 139–158.

[20] Kraemer, K. and King, L., “Computer-Based Systems for Cooperative Work and Group Decision Making,” ACM Computing Surveys, Vol. 20, No. 2, June 1988, pp. 115–146.

[21] Long, R., New Office Information Technology: Human and Managerial Implications, Croom-Helm, New York, 1987.

[22] McCartt, A. and Rohrbaugh, J., “Evaluating Group Decision Support System Effectiveness: A Performance Study,” Decision Support Systems, June 1989, Vol. 5, No. 2, pp. 243–253.

[23] Mehta, C. and Fan, L., “Knowledge-Based Systems for Process Synthesis,” Proceedings of the World Congress III of Chemical Engineering, Tokyo, Japan, 1986.

[24] Miller, I. and Freund, J., Probability and Statistics for Engineers, 2nd Edition, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1977, p. 272.

[25] Nunamaker, J., Vogel, D., Heminger, A., Martz, B., Grohowski, R., and McGoff, C., “Experiences at IBM with Group Support Systems: A Field Study,” Decision Support Systems, Vol. 5, No. 2, June 1989, pp. 183–196.

[26] Oxman, R. and Gero, J., “Using an Expert System for Design Diagnosis and Design Synthesis,” Expert Systems, Vol. 4, No. 1, February 1987, pp. 4–14.

[27] Rauch-Hindin, W., Artificial Intelligence in Business, Science, and Industry, Prentiss-Hall, Englewood Cliffs, New Jersey, 1985.

[28] Rozenblit, J.W., "A Conceptual Basis for Integrated, Model-Based System Design," technical report, Department of Electrical and Computer Engineering, University of Arizona, Tucson, 1986.

[29] Rozenblit, J. and Huang, Y., “Constraint-Driven Generation of Model Structure,” Proceedings of the 1987 Winter Simulation Conference, Atlanta, December 1987.

[30] Rozenblit, J., Suleyman, S., and Zeigler, B., “Knowledge-Based Design of LAN’s Using System Entity Structure Concepts,” Proceedings of the 1986 Winter Simulation Conference, Washington, D.C., 1986.

[31] Stefik, M., Foster, G., Bobrow, D., Kahn, K., Lanning, S., and Suchman, L., “Beyond the Chalkboard: Computer Support for Collaboration and Problem Solving in Meetings,” Communications of the ACM, Vol. 30, No. 1, January 1987, pp. 32–47.

[32] Teichroew, D. and Hershey, E., "PSL/PSA: A Computer-Aided Technique for Structured Documentation and Analysis of Information Processing Systems," IEEE Transactions on Software Engineering, Vol. SE-3, No. 1, January 1977, pp. 41–48.

[33] Teichroew, D. and Sayani, H., “Automation of System Building,” Datamation, August 1971, Vol. 17, No. 8.

[34] Turoff, M. and Hiltz, S., “Computer Support for Group Versus Individual Decisions,” IEEE Transactions on Communications, January 1982, pp. 306–315.

[35] Vogel, D. and Nunamaker, J., “Group Decision Support System Impact: Multi-Methodological Exploration,” Information and Management, forthcoming.

[36] Zeigler, Bernard P., DEVS-Scheme User's Manual, Department of Electrical and Computer Engineering, University of Arizona, Tucson, 1989.

[37] Zeigler, B.P., “Hierarchical Modular Discrete Event Modeling in an Object-Oriented Environment,” Simulation Journal, Vol. 49, No. 5, 1987, pp. 219–230.

[38] Zeigler, B.P., Multifaceted Modeling and Discrete Event Simulation, Academic, New York, 1984.

[39] Zigurs, l., Poole, M.S., and DeSanctis, G., “A Study of Influence in Computer-Mediated Communication,” MIS Quarterly, Vol. 12, No. 4, December 1988, pp. 625–644.
