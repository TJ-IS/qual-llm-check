---
otero_id: 17543
otero_key: "Z86X2GSQ"
title: "A hypermedia expert system for advanced cardiac life support management"
authors: "Ming M. Wang; Jen-Gwo Chen; Hong-Sang Yoon; S. Vasudevan; Laurie Webster"
year: "1994"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(94)90001-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A hypermedia expert system for advanced cardiac life support management

Ming M. Wang

Department of Endodontics, University of Texas, Health Science Center at Houston - Dental Branch Houston, TX 77225, USA

Jen-Gwo Chen \*, Hong-Sang Yoon and S. Vasudevan

Department of Industrial Engineering, University of Houston, Houston, TX 77204-4812, USA

Laurie Webster

NASA / Johnson Space Center, Houston, TX 77058, USA

A hypermedia expert system was developed to assist in diagnosing and recommending treatment for cardiac arrhythmia on space station freedom and to serve as a supplemental tool for training and retraining the crew in the practice of advanced cardiac life support (ACLS) protocols. The system includes five modules: ACLS expert system module, database module, reference-materials module, hypermedia instruction module, and friendly user interface module designed for the use of both the expert and the novice. More than 100 test scenarios adapted from ACLS mega code review study cards were used to validate the system and the results were satisfactory. Two experiments were also conducted to demonstrate the effectiveness of the system as a performance aid and supplemental training tool. Results indicated that the subjects' performance improved significantly after consulting the system. The subjects also reached an acceptable level of performance after receiving 40–60 minutes training via the system. In conclusion, this system has been found to be an excellent ACLS supplemental training tool and performance aid and can also serve as a model and building block for developing a more advanced state of the art time-constrained decision support system.

Keywords: Expert system; Interactive videodisc technology; Advanced cardiac life support system; Object oriented programming.

## 1. Introduction

With the National Aeronautics and Space Administrations (NASA) plans to design and de-

![](/api/attachments/Z86X2GSQ/fulltext/images/b908127780e9c589c2565e0e43ca4a1bf0f4c836a4fb2e5a05de2286078ca840.jpg)

Dr. Jacob Jen-Gwo Chen is an associate professor and chairman in the Department of Industrial Engineering, University of Houston, Texas, USA. He received his B.Sc. degree in Biology from the National Taiwan Normal University, his M.Sc. in Industrial Management from the Central Missouri State University, and his Ph.D. in Industrial Engineering from the University of Oklahoma. He is also the director of the ergonomics laboratory and in charge of the gradu-

ate programs in the Department of Industrial Engineering at the University of Houston. His main research interests lie in the areas of expert systems, automation, and ergonomics. During the past few years he has conducted several successful seminars in Taiwan, China and USA covering expert systems, automation, plant layout, total quality management, and computerized project management.

![](/api/attachments/Z86X2GSQ/fulltext/images/70481f1d0e24a565b4e8255d46f7b9714a6bdd65f0d4e1548760a2704cfd40b2.jpg)

Dr. Hong-Sang Yoon is a chief manager in the Samsung Data Systems, Inc. in Korea. He received his B.Sc. in Agriculture Engineering from Seoul National University, his M.Sc. in Mechanical Engineering from State University of New York, and his Ph.D. in Industrial Engineering from the University of Houston. His concentrates his research in the application of artificial intelligence in management, communication, and manufacturing systems.

![](/api/attachments/Z86X2GSQ/fulltext/images/712576a0072d17eaf484081f544209fbf988ab419efe8b67ca2d73f313bd79dd.jpg)

Mr. S. Vasudevan received his B.E. in Production Engineering from Regional Engineering College and his M.Sc. in Industrial Engineering from University of Houston. Currently, he is employed as an expert system engineer in the Bactel, Inc.

velop a permanently manned space station Freedom on Low Earth Orbit, ensuring the safety and health of the crew via the on-board health maintenance facility (HMF) will assume greater importance than ever before. Cardiac arrhythmia, in general, is one of the highest occurring medical problems [8]. Malignant cardiac arrhythmia is a life-threatening situation and requires immediate medical attention. Without immediate management, it is bound to cause the death of the crew member with possible failure or premature end of the mission. Indeed, malignant cardiac arrhythmia was one of the two reasons that forced the Soviet cosmonauts to return to Earth prematurely [7].

The requirements for diagnoses, therapies, and instruments of the HMF life support system have been described and documented among several NASA reports $[4,5]$ . They are as follows: (1) integrated medical information management; (2) preventive, diagnostic, and therapeutic computer-assisted medical management algorithms; (3) computer-assisted medical checklists, procedures, and indexed medical reference materials. The co-operative effort between medicine and engineering is needed to meet these requirements under an environment that is both unusual and resource constrained as in the space station.

Medical diagnosis and treatment are complex procedures that involve the accumulation of clini-

![](/api/attachments/Z86X2GSQ/fulltext/images/a3fcd2efef353b12929a7e5d0ae6c52203f18fa4992f7f26e4ea8f53a943a6c6.jpg)

Dr. Ming M. Wang is an Associate Professor and the undergraduate program coordinator of the Department of Stomatology, University of Texas Houston, Health Science Center - Dental Branch. Dr. Wang is a diploma of the American Board of Endodontics. His main research interests include the application of computer technology in medical-dental field and cytotoxicity.

![](/api/attachments/Z86X2GSQ/fulltext/images/472f99ed98acbb754185e0add8b6f64486274fd4a34eabb484e9cfce778fbd3e.jpg)

Dr. Laurie Webster is a senior expert systems specialist in the Automation and Robotics Division at NASA/JSC. He received a B.Sc. in Mathematics/Physics from Florida A & M University, a M.Sc. in Systems Engineering from West Coast University, a M.Sc. in Electrical Engineering from University of Southern California, a M.Sc. in Biomedical Engineering from the University of Houston, and a Ph.D. in Industrial Engineering from the University of Houston. He is responsible

for planning, conducting research and participating in the development AI for spaceflight systems.

cal data followed by the application of considerable amount of judgement, intuition, and experience. The diagnostic process is typically heuristic, but requires all the necessary information, and each practitioner applies his or her own heuristics for diagnosis and further treatment. The characteristics of this situation fit all the requirements necessary for the application of an expert system. Indeed, expert systems have been applied in the past for medical diagnosis and treatment. When in space, there is always a chance that there may be a 15–20 minutes interval when the space station is out of contact with the ground station and if a life-threatening emergency happens during this period of time, in the absence of a physician the astronauts crew medical officer (CMO) must be guided through the emergency treatment procedures to maintain the vitality of the patient. Thus it is extremely important to integrate the on-board facilities in the form of dedicated expert systems to reduce the dependence of the space station Freedom on continuous medical service support from the ground base. This study will assume the role of one such expert system.

A hypermedia expert system entitled CMO-EMPH Asis-ACLS (Crew Medical Officer - Emergency Medical Protocol Hypermedia Assistant: Advanced Cardiac Life Support) is developed to serve as a model in assisting the CMO in diagnosing and recommending treatment for immediate life-threatening cardiac arrhythmia on space station Freedom and to serve as a supplemental tool for training and retraining the crew in the practice of ACLS protocols.

## 2. System development

Currently, the system includes five modules: (a) ACLS expert system module, (b) database module, (c) reference-materials module, (d) hypermedia interactive video disc (IVD) instruction module, and (e) friendly user interface designed both for the expert and the non-expert. The reference-materials module and the IVD module are executed from within the rules of the expert system during run time and the database module is in the background as is usual. During runtime, the expert system handles the diagnosis and treatment for cardiac arrhythmia, the database keeps control of the dosages of the various drugs, and the reference-materials and IVD modules are optionally available as additional help to the CMO. A user-friendly interface built on top of the expert system hides the inner workings of the system. NEXPERT OBJECT, a commercial expert system shell using the principles of object-oriented programming, is used for building the expert system. Ease Plus is used for building the database system. The system configuration is shown in Figure 1.

![](/api/attachments/Z86X2GSQ/fulltext/images/bd73ea1052c1c63677b43bba799ab8c440897f4c8d9429d3fbb803a3b5392f65.jpg)  
Fig. 1. CMO-EMPHAsis-ACLS system configuration.

2.1. Development of the ACLS expert system module

## 2.1.1. Domain experts and knowledge acquisition

Basically two knowledge sources are generally required for building a knowledge base. They are deep and shallow knowledge [3]. The textbook of ACLS [10] and the IMSS checklist [6] which was developed and used in the Skylab missions are the sources of deep knowledge. The shallow knowledge was obtained from three faculty in the University of Texas, Medical Center at Houston. They are Dr. T. Pate, a certified ACLS instructor, Dr. Sweet, a recipient of ACLS certificate awarded by the American Heart Association (AHA) and Dr. M. Michael Wang who has had extensive training in ACLS management. This knowledge was acquired through a series of interview sessions. A series of meetings with three other aerospace physicians from NASA/JSC also provided valuable information in the shallow knowledge acquisition. During the meetings, the range of the problems was identified. Nine protocols which are used most frequently were selected as the problem domain for the ACLS management. Based on the heart rhythm status, the protocols are enumerated as follows: Asystole, electromechanical dissociation, bradycardia, stable paroxysmal supraventricular tachycardia, unstable paroxysmal supraventricular tachycardia, stable ventricular tachycardia, unstable ventricular tachycardia, ventricular ectopy, and ventricular fibrillation/pulseless ventricular tachycardia.

## 2.1.2. Knowledge representation

The development of the expert system was built via the object-oriented programming approach. The object oriented programming is a data-centered type of approach. Instead of thinking in terms of a function acting on varying types of data, which has been used as the traditional technique in the past, the designer focuses on the data acting on itself by using varying types of functions. For example, there are several potential etiologies of a cardiac arrest (ventricular fibrillation, Asystole, electromechanical dissociation (EMD), Bradycardia, etc.). The investigation of the etiology of a cardiac arrest may be the first decision-making step during the diagnostic procedure. Similar diagnoses may be obtained even if different heuristic rules are applied. Thus an object-oriented programming approach may be the best method since these different rules still deal only with the same object (cardiac arrest).

In any object oriented programming language, the fundamental entity is an object [3]. In turn each object is characterized by its state and its actions. The state of an object is simply the attributes and values of the object. Actions are then the operations that an object is capable of executing. Each object is also a member of a class which in turn may be a member of a super class. An object can also have sub-objects and a class can have sub-classes. Each class is characterized by its field and methods. Further, each class inherits the fields and methods of its super class. A field contains one of the states of the object while a method contains one of the actions of the object.

For example, let ‘administration of Epinephrine’ be an object. It may belong to a class of ‘treatment after 360 Joules defibrillation’ which in turn may be a sub-class of a super class ‘treatment in ventricular fibrillation protocol’. The object, administration of Epinephrine may have sub-objects such as Epinephrine in Asystole,

![](/api/attachments/Z86X2GSQ/fulltext/images/6e1c66aa7be69d9852746b50fb2882df8121ba8631cd876927839f39a922da62.jpg)  
Fig. 2. Hierarchy of relationships between objects, classes etc.

Epinephrine in EMD, etc. The properties of these objects could be dosage, count, time interval, etc. Figure 2 shows the basic structure of an object-oriented programming approach.

The AHA has provided the procedures for the diagnosis and treatment of cardiac arrhythmia under advanced cardiac life support (ACLS). Cardiac arrhythmia is classified broadly into seven protocols namely Asystole (AST), EMD, ventricular fibrillation/pulseless ventricular tachycardia (VFT), bradycardia (BDY), ectopy (VEY), paroxysmal supraventricular tachycardia (PSVT), and ventricular tachycardia (VT). Two of these protocols, PSVT and VT, are further classified into PSVT/stable patient and unstable patient, and VT/stable symptoms and unstable symptoms, making the total number of ACLS protocols to nine. Our system should diagnose the correct type of protocol and recommend treatment accordingly. The diagnosis part of the problem is essentially classification and the treatment part of the problem is construction. It is this construction part that makes the design of the expert system that much more difficult. In order to achieve this requirement, we have adopted a modular approach. A knowledge base (KB) has been built separately for each of the nine ACLS protocols. Thus it is a multiple knowledge base system and as is usual in such systems, a common knowledge base controls the nine individual knowledge bases. This is required as there is a need to share information among the nine individual knowledge bases. The common knowledge base acts as sort of a blackboard and is shared among the individual knowledge bases. The configuration of the knowledge base is shown in Figure 3.

All the knowledge bases are composed of IF-THEN pattern matching rules, objects, classes, properties and meta-slots. All the nine individual knowledge bases have a very similar structure while the common control knowledge base being a little different from others. The individual knowledge bases follow a particular sequence as dictated by ACLS and for each step or level of the sequence there is an island or a group of rules. The structure of the rules in each of these groups is similar to one another. An example of the rule in VF/pulseless-VT (VFT) protocol management is given below:

IF Status of pulse in level 1 of VFT is 'ABSENT'

AND Nature of rhythm in level 1 of VFT is 'ASYSTOLE'

AND The starting point of VFT protocol is assigned a value of 'DEF 360'

THEN Shift from VFT protocol to AST protocol.

AND $\langle |VFTSTARTER| \rangle$ . DECISION is set to FALSE

AND $\langle |ASTSTARTER| \rangle$ . DECISION is reset.

In the ‘IF’ part of the rule, the first two conditions are the ones that require responses from the CMO. The third condition in the ‘IF’ part of the rules involves assignment of a value to a slot. This is done to write the information about VFT protocol in the common knowledge base blackboard. This information is required when the inference comes back to the VFT protocol.

![](/api/attachments/Z86X2GSQ/fulltext/images/2897e74c49df70c589e5347358909c13e7fe2a4eeba6669e87d2fefb35f1a3e6.jpg)  
Fig. 3. Knowledge base configuration.

In the ‘THEN’ part, the first action forces the hypotheses of the VFT set of rules in the common KB to become false. It is called pattern matching and all the objects within the class ‘VFTSTARTER’ with a property ‘DECISION’ are made false. These actions are executed in order to make sure that forward chaining effects do not take place due to the assignment in the ‘IF’ part and to reset the starter rules of the AST protocol. The starter rules of Asystole require to be reset for the inference to enter the Asystole protocol at the appropriate point.

## 2.2. Development of the database module

The database module which includes crew medical information management and advanced life support (ALS) pack inventory database has been developed and verified. The crew medical information management database includes the following sections:

(a) demographic data (e.g., name, gender, etc.), vital signs (e.g., blood pressure, pulse, respiration and temperature),

(b) subjective information (e.g., primary complaints),

(c) objective information (e.g., HEENT, chest),

(d) assessment (e.g., diagnosis, procedure) and

(e) treatment plan (medication/dose/frequency).

The ALS pack inventory database includes airway management kit, TV fluid therapy kit, cervical spine stabilization supplies, emergency drug kit, portable oxygen supply, bandaging supplies, suction equipment and supplies, assessment supplies, waste management supplies, hyperbaric kit, and transport container.

The database module is developed under the EASE Plus environment with the concept of a relational database structure, which has been used successfully in several major expert system projects (e.g., MEDAS) in the past. All information is classified as either character type or checklist type of field in the record. Each field has been grouped into one of 44 different segment types based on its relationship with other fields and is indexed via the crew identification number. Figures 4 and 5 demonstrate the example of screen design for crew information management database and ALS pack inventory database, respectively. In the main menu of the crew medical information module, the user has five major options: HELP, ADD, EDIT, DELETE, and HMF PANEL. This pull-down menu and other pop-up menus are supported by EASE Plus and are used to allow the user to choose his/her desired alternatives.

![](/api/attachments/Z86X2GSQ/fulltext/images/45c18382bb5caf48590febcdb4bf93178f6c34372f30e118bf094dad5e8aa967.jpg)  
Fig. 4. An example of screen design for crew medical information management database.

![](/api/attachments/Z86X2GSQ/fulltext/images/f72576c969dbb520d28e4d85d5234c39aa7cfd1ee092e5d52be51e1ae323e6cb.jpg)  
Fig. 5. An example of ALS pack inventory database screen design.

## 2.3. Development of the reference materials module

Currently, reference materials for nine ACLS treatments and nine treatment drugs (e.g., epinephrine, atropine, lidocaine, bretylium, isoproterenol, procainamide, verapamil, sodium bicarbonate, and digoxin) suggested by AHA have been developed and integrated with the system as a portion of the reference materials module. Reference materials for each ACLS treatments include the following sections: (a) description (e.g., when three or more beats of ventricular origin occur in succession at a rate in excess of 100 per minute, VT is present), (b) summary of ECG criteria (e.g., rate: the rate is greater than 100 per minute and usually not faster than 220 per minute), (c) treatment (e.g., VT without a pulse should be treated as VF), and (d) further reference (e.g., AHA, Textbook of ACLS, 2nd Edition 1987, pp. 76–79). Reference materials for each emergency drug kit include the information of usage (e.g., Epinephrine is used for VF, pulseless VT, AST, EMD), dosage (e.g., Epinephrine should be repeated at least every 5 minutes), precautions (e.g., Epinephrine may induce or exacerbate ventricular ectopy, especially in patients who are receiving digitalis), and further reference.

The reference materials module is an option available to the CMO to know more about the emergency drugs before administering them to the patient. If for any reason the CMO is doubtful about a certain drugs side effects or dosage, he/she may choose an option to know more about the drugs specificities. The questions for the reference materials of the emergency drugs are asked during the inference of the expert system and every time during a requirement to administer the drugs. Two choices, 'SHOW' and 'SKIP' are provided in the question form. If the CMO chooses 'SKIP', the inference jumps to the next point. On the other hand, if 'SHOW' is chosen, a text file is shown on the screen explaining about the drug. Thus the reference module is a fully integrated system within the expert system.

## 2.4. Development of the hypermedia interactive videodisc instruction module (IVD)

This is the module that makes this system one of the truly unique systems of its kind. Hypermedia is a concept which connotes a highly integrated electronic environment allowing a user to interactively peruse a very large collection of electronically linked information consisting of real time moving color video images, sound, text and electronically searchable databanks $[1,2]$ . In other words, the hypermedia interactive video disc technology combines the interactivity and high quality graphics of personal computer with full color motion video, stills, and audio.

In this system, the hypermedia IVD module is also an option available to the CMO to view a treatment procedure in action on the screen, before he/she is required to administer that treatment to the patient. For instance, during the treatment for Asystole, the CMO may be required to intubate the patient. Although the CMO would have received basic training in intubating the patient, he/she may tend to think that one more look at the procedure may really help in intubating effectively at that time. Similar to the reference materials module, this option is available in the question form and the CMO may choose one of the choices, 'SHOW' or 'SKIP'. If 'SHOW' is selected, the procedure is shown on the screen with audio instructions. As an extra facility, the CMO may terminate the video picture any time during running, by pressing the key F1. This option is provided so that the CMO need not waste time in viewing the entire clipping if he/she is confident of the treatment after watching only a few frames. Apart from the treatment procedures, location of certain equipments like IV pump, defibrillation etc. and the drugs can be viewed on the video selectively. The hypermedia IVD module is thus a fully integrated module with the expert system.

## 2.5. Development of the user interface

Customized question forms have been built for each of the questions that needs to be asked to the users. An example of protocol question form is shown in Figure 6. Six types of information are displayed in the protocol question form (a) instructions to the users to do an action (e.g., defibrillate with upto 360 Joules), (b) reminders to the users (e.g., continue CPR), (c) questions requiring response from the users (e.g., check pulse), (d) title of the choices for the questions (e.g., suggested rhythm), (e) choice for the questions, and (f) the algorithm of the protocol for quick reference (e.g., intubate the patient). Different colors have been assigned to each type of information based on our color preference experiment results and guidelines from NASA-USE-1000, NASA-STD-3000, and MIL-C-25050A.

![](/api/attachments/Z86X2GSQ/fulltext/images/9c281d3b8b10916d10198a67ab5ac0bdfc4b715e9dc86a26678163bf2d8b1b70.jpg)  
Fig. 6. A sample of question form.

As can be seen from the question form, it is divided into two parts vertically. The right hand side gives a quick overview of the protocol that the inferencing is presently under. If the CMO is a medical doctor or he/she may be very familiar with the protocol, then he/she does have to go through the entire protocol step by step. He/she can just have a quick look to refresh the memory and can start treating the patient without having to wait for the expert system. The left hand side goes through the entire protocol step by step and is ideally suited for the CMO who is not a medical doctor or have had only minimal medical emergency treatment training.

## 3. System verification and validation

Expert systems must be verified and validated before being deployed. Without proper verification and validation, disappointing results can occur. Because of their attempt to mimic human intelligence, expert systems have a greater need for verification and validation than conventional computer programs. Verification involves the determination of whether or not the system is functioning as intended. This may involve program debugging, error analysis, input acceptance, output generation, reasonableness of operation, run time control, and scope of problem. Validation concerns a diagnosis of how closely the expert system's solution matches a human expert's solution. In other words, the system validation deals with the system performance in terms of user's satisfaction and accuracy.

The validation of the knowledge base and the inference engine takes an important role in assessing the system's performance and reliability. In validating the knowledge base, there are two main phases: a debugging phase and a performance measurement phase. The debugging phase should include checks for grammatical errors, checks for inconsistency, checks for completeness, checks for certainty factors, etc. On the other hand, the system should provide accurate results, consistency, quick response times, and an ease of learning and understanding in order for it to prove successful. The knowledge debugging phase is concentrated on the validation of the logic and integrity of the system knowledge base. The human experts will check the knowledge base for rules inconsistency and completeness with the following criteria: consistency (e.g., redundant rules, conflicting rules, etc.) and completeness (e.g., illegal attribute values).

It is only logical to expect the domain experts to conduct evaluation before subjecting the system to any standard evaluation methods. Given the fact that it is their knowledge that has been cloned in the system, the domain experts were by far the best persons to conduct initial evaluations of the system during its final developmental stages. The experts came up with their own scenarios and tested the system's performance for accuracy and correctness of responses. Although the experts found the diagnosis and recommendation of treatments by the system for several ACLS scenarios to be satisfactory, they had several recommendations to make to improve the performance of the system. After ensuring that these modifications were carried out and the performance of the system was free from any faults, the experts cleared the system for evaluation using other standards.

In addition to those basic verification and validation procedures, two experiments were also conducted to demonstrate whether the system is an effective supplemental training tool and performance aid. In the first experiment, four major protocol scenarios (e.g., Unwitnessed VF, VF-EMD-VF, AST, and VF-Asystole-VF) adapted from ACLS mega code review study cards were used as test questions in the first experiment.

ACLS mega code provides case studies of various scenarios that may develop in the case of a cardiac arrest and the user is expected to recommend treatment for each scenario. Each of these scenarios comes in the form of index cards (review cards) apparently for easy handling. An individual scenario or review card may not be of much help in validating any ACLS system. But when some of them are grouped together, a real life cardiac arrest and treatment that follows such a situation can be evolved and simulated. These are situations/scenarios that are non-theoretical, the ones that have happened or likely to happen in real life and hence prove to be excellent material for our validations. A sample scenario is shown as follows:

Scenario description: You are working in the ED and are called at the bedside of a patient who has suddenly become unresponsive. The patient is middle-aged who weighs about 70 kg. A defibrillator is at the bedside. Quick look paddles reveal the rhythm to be VF.

Test Question One-What do you do?

1. Verify that the patient is pulseless and unresponsive. If so, defibrillate with 300 Joules.

2. Give Epinephrine 1:10000, 1.0 mg IV bolus. Continue CPR for 1 to 2 minutes.

3. Verify that the patient is pulseless and unresponsive. If so, defibrillate with 200 Joules.

4. Give Atropine (1 mg IV) and repeat in 2 to 5 minutes.

5. Give Bretylium 5 mg/kg IV bolus and circulate drug for 1 to 2 minutes with CPR.

For the purpose of evaluation of CMO-EMPHAsis-ACLS, scenarios (review cards) that pertained to VF, AST and EMD were isolated. The scenarios were then classified into the following four groups:

(1) Scenario VF: The rhythm pattern remains in VF protocol and does not change course during a consultation session.

(2) Scenario VF-EMD-VF: The rhythm starts with VF, patient undergoes treatment in VF, rhythm changes into EMD, patient undergoes treatment in EMD, rhythm changes back into VF, and treatment continues in VF.

(3) Scenario AST: The rhythm pattern remains in Asystole protocol and does not change course during a consultation session.

(4) Scenario VF-AST-VF: The rhythm starts with VF, patient undergoes treatment in VF, rhythm changes into AST, patient undergoes treatment in AST, rhythm changes back into VF, and treatment continues in VF.

The subjects in this experiment had no ACLS background. A questionnaire containing the above four scenarios were given to them and they were asked to recommend treatment for the scenarios. The recommendations of the subjects were medically incorrect as was of course anticipated. The subjects were then allowed to use CMO-EMPHAsis-ACLS and were asked to concentrate on the protocols that featured in the questionnaire.

While using CMO-EMPHAsis-ACLS, the subjects were not allowed to refer to the questionnaire. This was done to discourage the subjects from using CMO-EMPHAsis-ACLS with the sole idea of getting plug-in type answers for the scenarios in the questionnaire. This way, the subjects were forced to get acquainted with ACLS through CMO-EMPHAsis-ACLS in a generalized manner. The subjects were asked to practice with CMO-EMPHAsis-ACLS as long as they needed to feel comfortable enough to answer the questionnaire again. The procedure is shown in Figure 7.

After getting acquainted with ACLS, in particular with the protocols that were relevant with the questionnaire, the subjects took the questionnaire again, and the performance of the subjects improved considerably. The results are shown in Table 1.

Table 1 shows that with assistance of CMO-EMPHAsis-ACLS, the subject performance improved from $43.6\%$ to $86.5\%$ in VF scenario and as can be seen significant improvement was also observed in other scenarios. The two-tailed $t$ test result indicated that there is a significant difference $\left[\left|T(-6.504)\right| > -t_{19,99.5}(2.861)\right.$ for VF, $\left|T(-4.090)\right| > -t_{19,99.5}(2.861)$ for VF-EMD-VFT, $\left|T(-9.114)\right| > -t_{19,99.5}(2.861)$ for AST, $\left|T(-7.067)\right| > -t_{19,99.5}(2.861)$ for VF-AST-VF] in subject performance before and after referring to the system in the above mentioned scenarios. The two-tailed $t$ test was conducted with 19 degrees of freedom with 0.01 level of significance. These results demonstrate the effectiveness of the CMO-EMPHAsis-ACLS as a performance aid in recommending an appropriate ACLS treatment. In each of these scenarios there was at least one subject that could answer all the questions correct. This substantiates the accuracy of treatment recommendations of CMO-EMPHASIS-ACLS besides proving it to be an excellent performance aid. This procedure also ensures the quality of the system to serve as a decision making aid and a decision maker if necessary.

![](/api/attachments/Z86X2GSQ/fulltext/images/7d38bf62cb8063303c3cc0343b5036de5594055b860725348ca8ad30239979b3.jpg)  
Fig. 7. Procedure for evaluation using ACLS Mega Code Review.

Performance comparison of subjects with and without consultation to CMO-EMPHAsis-ACLS.

<table><tr><td rowspan="2">Tests</td><td colspan="4">Protocols</td></tr><tr><td>VF</td><td>VF-EMD-VF</td><td>AST</td><td>VF-AST-VF</td></tr><tr><td>Before</td><td></td><td></td><td></td><td></td></tr><tr><td>CMO-EMPHAsis-ACLS</td><td>43.6</td><td>39.5</td><td>26.8</td><td>32.6</td></tr><tr><td>After</td><td></td><td></td><td></td><td></td></tr><tr><td>CMO-EMPHAsis-ACLS</td><td>86.5</td><td>74.1</td><td>86.2</td><td>79.0</td></tr></table>

In the second experiment, two students medically ignorant and with no ACLS knowledge were involved in a pre-training test by answering questions in three protocols (unwitnessed VF, VT, and EMD). The responses were recorded. Subjects were requested to take an ACLS training session via CMO-EMPHAsis-ACLS for 20–30 minutes and then retake the test. This procedure was repeated until reaching the absolute accuracy level (100%). The total time for them in reaching the accuracy level was defined as the minimum protocol training time. Results show that the minimum training time for VF, VT and EMD is one hour, 40 minutes and 40 minutes, respectively. Another 10 subjects with similar background as the two students involved in pre-training were requested to repeat the experiment by taking 40 or 60 minutes (the minimum training time). ACLS training session time via the CMO-EMPHAsis-ACLS depends on the size of the training protocol. Figure 8 shows that the subjects improved their performance after taking the training session. It is imperative, of course, to compare the CMO-EMPHAsis-ACLS with other ACLS training methods (e.g., standard ACLS instruction) before one can say that the CMO-EMPHAsis-ACLS is an effective training tool. At least, our result demonstrates that the system has a great potential as an adjunct to ACLS training.

![](/api/attachments/Z86X2GSQ/fulltext/images/0f520fc592ab789b374521b1f088e8f8ea66c33e2092f2d5dc42b32a812a1f14.jpg)  
Fig. 8. Performance comparison of before and after training.

## 4. Conclusions

This paper presents the development of a hypermedia expert system for ACLS management in space station Freedom. The system has also been successfully shown, via the results of the validation test, to be an effective supplemental training tool and performance aid in the practice of ACLS protocols.

The integration of the various protocols of ACLS through the concept of black boarding makes this system capable of handling any theoretical situation in a patient's condition that may involve switching back and forth between various protocols. The complex procedures of reading and writing information from and to the common knowledge base provides an excellent foundation for extending such a concept to more involved medical emergency treatment problems. Also the novel approach of embedding hypermedia techniques such as video display in the rules of the expert system for various treatment procedures should be further exploited and extended to other emergency treatment procedures.

In this context, there are certain areas that are worth the discussion. Would it be practical at all to take instructions from a computer for ACLS? We are addressing a situation in the space environment during the eventuality of the shuttle losing communication with ground support base, a situation when the best possible effort has to come from on-board. It may also turn out that the CMO may or may not be well versed at that time to administer ACLS. In such a situation a system like ours will be certainly vital at least until communication with ground support base is achieved.

On the surface, this tool may not look any different from any other training tool. In fact, even the ACLS manual can be considered equivalent to this tool. But this is a tool that has visual aids in the form of the hypermedia module and an explanation facility in the form of the reference materials module.

A novice or an absolute beginner in ACLS may not even know the existence of various ACLS procedures like defibrillation, intubation, CPR, IV access, etc. that are demonstrated visually in CMO-EMPHAsis-ACLS. If such a person has to be trained in ACLS, this tool may serve as a comprehensive adjunct to class room training.

Students with no ACLS or medical background that were involved in the verification process, came out with a very good understanding of the various procedures, techniques, drugs, sequences, etc. involved in ACLS. In the opinion of the authors, such an understanding could not have been provided if the subjects were just asked to refer to the ACLS manual.

In conclusion, CMO-EMPHAsis-ACLS can serve as a model and building block for developing a more advanced state of the art time-constrained decision support system. The efficiency of this expert system in recommending treatment for emergency situations should pave way for the use of expert systems for other emergency and non-emergency treatment requirements on space station Freedom and other remote medical facility operations and training units (e.g., Navy, antarctic expedition).

## Acknowledgements

This research was supported by the NASA/JSC, Automation and Robotics Division, under Contract NAG9-425. Mr. Dennis Lawler was the project manager. The authors would like to thank Drs. R. Billica, J. Gosbee, C. Lloyd, T. Pate, J. Sweet and Mr. R. Beuker for their supports and contributions.

## References

[1] S. Brunsman, J. Messerly and S. Lammers, Publishers, Multimedia, and Interactivity, in: Interactive Multimedia, eds. S. Ambron and K. Hooper (Microsoft Press, Bellevue, 1988) pp. 273–281.

[2] P. Cook, Multimedia Technology, in: Interactive Multimedia eds. S. Ambron and K. Hooper (Microsoft Press, Bellevue, 1988) pp. 217–240.

[3] J.P. Ignizio, An Introduction to Expert Systems: the Methodology and its Implementation (McGraw-Hill, New York, 1991).

[4] J.S. Logan, Medical Requirement of an In-flight Medical Crew Health Care System (CheCS) for Space Station, NASA-JSC-31013 Revision B, Life Science Division, 24 July 1989.

[5] J.S. Logan, Medical Requirements of an In-flight Medical System for Space Station, NASA-JSC-31013 Revision A, Life Science Division, 11 November 1987.

[6] NASA/JSC IMSS Checklist, 1973.

[7] B. Nelson, R. Gardner, D. Ostler, J. Schulz and J.S. Logan, Medical Impact Analysis for the Space Station

Aviation, Space Environmental Medicine 61 (1990) 169-175.

[8] D.V. Ostler, R.M. Gardner and J.S. Logan, A Medical Decision Support System for the Space Station Health Maintenance Facility, SCAMC (1988) 43–47.

[9] Space Medical Facility Design Requirement, NASA-STD-3000, Man-System Integration Division, 1987.

[10] Textbook of Advanced Cardiac Life Support (American Heart Association, 1987) pp. 76–79.
