---
otero_id: 17188
otero_key: "G4FBMUF9"
title: "A knowledge based system for controls-displays selection"
authors: "Mao-Jium J. Wang; Hok P. Teh"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90056-h"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A knowledge based system for controls-displays selection

Mao-Jiun J. Wang

Department of Industrial Engineering, National Tsin Hua University Hsin Chu, Taiwan, R.O.C.

Hok P. Teh

General Motors Corporation, Singapore

Appropriate controls and displays are important in achieving an efficient man-machine system. This paper presents the development of a knowledge based system that can facilitate the process of controls and displays selection. Information from the literature was aggregated and classified into selection criteria. Based on these criteria, decision trees for selection of displays and controls were developed. The decision trees were then programmed using an artificial intelligence language, XLISP. The system can recommend appropriate devices that can meet the process requirements.

Keywords: Controls and displays selection, Knowledge based system, Decision tree.

![](/api/attachments/G4FBMUF9/fulltext/images/135753fe858c7dd193138935b19e605ea316ecf7ea58947dfc962a47a708e05c.jpg)  
Hok P. Teh is an industrial engineer in General Motors, Singapore. He received his B.S. in industrial and system engineering from Ohio State University, 1987, and M.S. in industrial engineering from Alfred University, 1988. His areas of interests include artificial intelligence and system analysis.

![](/api/attachments/G4FBMUF9/fulltext/images/ae9945843a42789f0abcf5fc923113159c5867fc8c74088d3f609191e06a35aa.jpg)

Mao-Jiun J. Wang is an associate professor of industrial engineering at National Tsin Hua University, Taiwan, R.O.C. Prior to that, he was an assistant professor of industrial engineering at Alfred University, New York. He received his Ph.D. from State University of New York at Buffalo in 1986. His research interests include decision support system, industrial inspection and ergonomics.

## 1. Introduction

In any large and complex control system such as the control system in a nuclear power plant, the proper design of the controls and displays is essential. Also significant is the selection of appropriate controls and displays, as well as the proper arrangement of devices to meet human factors criteria in achieving an efficient man-machine system.

Traditionally, nearly all control panel designs are constructed manually through qualitative criteria such as McCormick's [5] "Guiding Principles of Arrangement". This qualitative approach has been found to be quite successful when the system under design is small and simple. However, when the system under consideration is large and complex, the efficiency and effectiveness of manual design decreases substantially. The poorly designed system can easily cause human operators to commit errors, especially under emergency and unexpected situations such as the accident at Three Mile Island. A review of literature shows that much work has been done in the design of controls and displays. However, relatively little attention has been given to the selection and arrangement of appropriate displays and controls (e.g. [9], and [10]). Pulat and Ayoub [8] reported on a computer program for control-display selection. The program (UNISER) is designed for displays and controls for the process industry. The database was based on the average subjective ratings of twenty human factors experts. Only 15 controls' average rating data were reported. Also, the program was written in FORTRAN IV with a multiple criteria decision making algorithm. The same set of criteria was applied to all the devices.

Most information regarding the selection of controls and displays is available in various human factors source books. In order to select appropriate devices that can meet the process requirements, the designer has to refer to different human factors source books and make a decision based on the limited information available. If the system to be considered is large and complex, the process for selecting displays and controls can be tedious and inefficient. It seems that there is a need to develop a systematic approach to facilitate the selection of displays and controls.

The objective of this paper is to introduce the development of a knowledge based expert system for selection of controls and displays. Knowledge and information available regarding control panel design was organized to set up selection criteria. These criteria were then used to form branches of decision trees. The construction of decision trees for displays and controls is discussed in the following section.

## 2. Decision Tree Development

Constructing a decision tree is the first step to represent the knowledge base. It is a heuristic approach and three steps are involved in setting up the decision tree.

1. Select a set of criteria that can categorize the characteristics of the devices. The criteria are the nodes of the tree.

2. Identify the branches of the tree. The paths taken from each node are determined by the possible responses to the criteria. At the very end of each branch is the conclusion (the recommended device) which satisfies the conditions contained in the tree.

3. Convert the branches to IF-THEN rules. The collection of the rules comprise the knowledge base.

In this study, the criteria and alternatives were determined by aggregating relevant information in various human factors source books (e.g., [1], [3], [7], and [10]).

As shown in fig. 1, devices were first categorized as: controls and displays. Controls were then divided into discrete controls and continuous controls [4]. Displays were first categorized into visual displays and auditory displays. Visual displays were further classified into dynamic displays and static displays [3]. The further development of each branch is described in the following.

2.1. Development of decision tree for control selection

As mentioned earlier, two decision trees were developed for controls. One for discrete controls and the other for continuous controls. From the literature, the selection criteria for discrete controls are the limbs involved (e.g., foot controls or hand controls), number of settings [4], force requirement [6], and dimension of movement [10]. All these criteria are task-specific dimensions. A decision tree for discrete control selection was developed based on these criteria (fig. 2). In this tree, one additional criterion, light requirement, is added to distinguish legend switch from toggle switch and rotary selector.

Continuous controls are often classified by the range of adjustment, setting time, force requirement and adjustment precision ([3], [4], and [10]). Based on these task-specific dimensions, a decision tree was developed. It is demonstrated in fig. 3. Occasionally, two or more selections are recommended. When this occurs, the system designer is encouraged to make a choice based on ergonomics and safety considerations.

## 2.2. Development of decision tree for display selection

Displays can be first categorized into auditory displays and visual displays. For auditory displays, Woodson [10] proposed some guidelines for the selection of these devices. These guidelines are:

![](/api/attachments/G4FBMUF9/fulltext/images/09f3643a9b33d48ed5e3cea2302f572c453d7ab87fbb080c755a23bb3f337804.jpg)  
Fig. 1. Main branches of the decision tree.

![](/api/attachments/G4FBMUF9/fulltext/images/ad8cf85526577f23b77ae9cface33d9269b674db7ea200a076db6ba3d48bcf7e.jpg)  
Fig. 2. Decision tree for discrete controls.

![](/api/attachments/G4FBMUF9/fulltext/images/b6318ca0737783abd1ff86cf46f48bf8431701f97ff17d0a78474f5e413fd83e.jpg)  
Fig. 3. Decision tree for continuous controls.

1. Use bell for fire alarm.

2. Use horn for emergency and equipment malfunctions.

3. Use buzzer for individual operator attention.

4. Use siren for operator attention (more than one operator).

A decision tree was developed based on the above mentioned guidelines (see fig. 4). However, in practice, some people might prefer to choose a different device than the one suggested. For example, the user might prefer horn or siren rather than bell for fire alarm. Therefore, the decision tree was constructed by using the auditory display suggested by Woodson [10], but the user may choose other devices which are enclosed in parenthesis shown in fig. 4.

Visual displays can be further divided into two major categories: static displays and dynamic displays. Woodson [10] suggested some guidelines for the selection of static displays in terms of identification, instruction, and warning messages. Some of his suggestions are: (1) use light(s) or a label for identification, and (2) use red printed board for a long warning message and red colored labels for a short warning message. These guidelines, along with color coding requirements and the method in which the display is presented, were used to design

![](/api/attachments/G4FBMUF9/fulltext/images/a693794007ca07de7c66853f79f58d3eae1fba396ccc088ee8517e4e2121ad2c.jpg)  
Fig. 4. Decision tree for auditory displays.

![](/api/attachments/G4FBMUF9/fulltext/images/5a7ea137aa6b82d0ea0d365596d6c95e90501661cefe035795cc45abf3168f1f.jpg)  
Fig. 5. Decision tree for static displays.

![](/api/attachments/G4FBMUF9/fulltext/images/926729171772906aaa18c9cb29542673fd53d802edfa587ca437f326dc3005e8.jpg)  
Fig. 6. Decision tree for dynamic displays.

the decision tree for static displays (fig. 5). In addition, the recommended color coding for each selected display is also included.

For dynamic displays, no direct classification is provided in the literature. However, some principles for selecting dynamic displays were suggested by Huchingson [4], Van Cott and Kinkade [9], and Woodson [10]. These principles are based on display information requirements. For example, if an exact quantity reading is desired, a counter should be used. Or if a large range of information or historical data is needed, a chart recorder should be chosen. A simple classification of these principles yields the criteria which were used in developing the decision tree for dynamic display shown in fig. 6.

## 3. Program Development

After the entire decision tree was developed, it was used to develop a rule set by using the IF-

THEN rule technique. An IF-THEN rule includes two parts. The IF part is comprised of conditions called clauses connected to one another with logical operators such as AND, OR, and NOT. The THEN part is evaluated only if the IF part is true. The inference mechanism of the system is backward chaining. The reason the system is appropriate for backward chaining is that the goal is to select among a set of alternatives, in this case possible control-display devices. The conclusion, in principle, already exists. Through a query process, the system can determine which device is the best. An artificial intelligence language, XLISP, was used to program the expert system. The reason for using XLISP is because of its simplicity and availability for the IBM PC. An example of the rules for the selection of discrete controls is as follows:

IF (number of settings = 2), (limb = hand) and

(force = high) THEN (device = detent lever)

![](/api/attachments/G4FBMUF9/fulltext/images/756a5786b0282d3f009be759523b219cc784faaab59472725882a8690e64aeb5.jpg)  
Fig. 7. Flowchart of the contros-displays selection program.

The ‘number of settings’, ‘limb’, and ‘force’ are clause variables and the ‘device’ is a conclusive variable in the knowledge base. If all the IF clauses are true, then the THEN clause is invoked, which leads to the conclusion of ‘detent lever’.

In XLISP, the rule is written as:

(COND (and (equal number of settings 2))

(equal limb hand) (equal force high))

(SETF device detent-lever))

A ‘COND’ is defined as a conditional form in XLISP that can take an arbitrary number of clauses. Each clause is enclosed in parentheses. In this case, three clauses were included. If all the clauses are true, the value of ‘detent-lever’ is set to the conclusive variable ‘device’.

Fig. 7 shows the flowchart of the program. The program first asks the user to input the number of devices and then the type of device (either a control or a display). If the answer is 'control', the user is asked to choose either a discrete control or a continuous control. On the other hand, if the answer is display, the user is asked to choose either an auditory display or a visual display. Similarly, if the answer is visual display, then the user will have to decide whether it is a static display or a dynamic display. The program then calls up the corresponding procedure and asks the task specific requirements for selecting a particular device. Each procedure is written as a user-defined function (DEFUN) in XLISP. The process is repeated until all the devices are selected.

## 4. Program Evaluation

The software developed in this study was tested by a process engineer in GTE. The engineer used this software to evaluate the five type of existing devices on a chemical processing control panel. The result of comparison is summarized in table 1. Four devices that were recommended by this software were the same as on the installation. The software recommended a different fifth device which was a circular dial instead of an indicator round per minute. The engineer concluded that the device recommended by the software was an improvement. This is because the circular dial indicated the direction of movement. This characteristic is important to inform the operator whether the speed of the system (agitator) is increasing or decreasing. No problems were reported while using this software.

Table 1  
Comparison of devices recommended by control-display selection expert system with the existing devices.

<table><tr><td>Variable of equipment to display or control</td><td>Existing display/control</td><td>Device recommended by the system</td></tr><tr><td>Pump</td><td>start/stop</td><td>legend switch</td></tr><tr><td>Agitator</td><td>start/stop</td><td>legend switch</td></tr><tr><td>Valve</td><td>open/close</td><td>legend switch</td></tr><tr><td>Rx temperature</td><td>record temperature</td><td>chart recorder</td></tr><tr><td>Agitator speed</td><td>indicator RPM&#x27;s</td><td>circular dial</td></tr></table>

## 5. Conclusion

This paper highlights the importance of choosing appropriate controls and displays for an efficient man-machine system. Existing literature for the displays and controls focuses on the design, not on the classification and selection of these devices. Also, the conventional manual approach for selection and evaluation of control panel devices tends to be time consuming and ineffective. To compensate for these limitations, a knowledge based expert system was developed to help the designer in selecting the appropriate controls and displays. The knowledge base comprises a set of decision trees which was constructed heuristically, this is a rather simple and effective approach. Artificial intelligence languages such as PROLOG and LISP seem to be the promising languages for this purpose since both languages provide great flexibility and power for symbolic processing. The artificial intelligence heuristic approach enables the user to select a control or display without going through every question. This saves the user a considerable amount of time during the panel design and evaluation process. Also, the knowledge base of the system can be further updated as more devices are introduced. Since the knowledge base is structured by a set of decision rules, it provides great flexibility for future expansion.

Furthermore, user-friendliness and menu driven characteristics were designed to be part of the program. The program will guide the user through the selection process by prompts and questions. Other features such as error prompt and the error recovery process were also included. The program has the ability to check the user responses and allow the user to reenter the data, if an error is detected.

In order to use the software effectively, a detailed task analysis of the system is suggested. This is an important procedure to help the designer to have a better understanding about the characteristics of the process variables to be controlled as well as the functional relationships among them. By knowing the process requirements, the user (designer) can interact with the expert system intelligently.

## References

[1] R.W. Bailey, Human Performance Engineering – A Guide for System Designers (Bell Telephone Lab, 1982).

[2] A. Chapanis, and R.G. Kinkade, Design of controls. In: H. Van Cott and R.G. Kinkade, Eds., Human Engineering Guide to Equipment Design (McGraw-Hill Book Company, New York, 1972).

[3] T.S. Clark, and E.N. Corlett, The Ergonomics of Workplace and Machines - A Design Manual (Taylor and Francis, London, 1984).

[4] R.D. Huchingson, New Horizons for Human Factors in Design (McGraw-Hill Book Company, New York, 1981).

[5] E. McCormick, Human Factors Engineering (McGraw-Hill Book Company, New York, 1970).

[6] E. McCormick, and M. Sanders, Human Factors in Engineering and Design (McGraw-Hill Book Company, New York, 1976).

[7] S.T. Pheasant, Body Space (Taylor and Francis, London and Philadelphia, 1986).

[8] B.M. Pulat, and M.A. Ayoub, Computer aided display-control selection procedure for process control jobs. IIE Transactions (1984), 371–377.

[9] H. Van Cott, and R. Kinkade, Human Engineering Guide to Equipment Design (McGraw-Hill Book Company, New York, 1972).

[10] G. Woodson, Human Factors Design Handbook (Mcgraw-Hill Book Company, New York, 1981).
