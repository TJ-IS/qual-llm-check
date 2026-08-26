---
otero_id: 21229
otero_key: "VQZEB4DE"
title: "Unifying business objects and system dynamics as a paradigm for developing decision support systems"
authors: "Andreas Gregoriades; Bill Karakostas"
year: "2004"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(03)00004-6"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Short communication

# Unifying business objects and system dynamics as a paradigm for developing decision support systems

Andreas Gregoriades<sup>a,</sup>\*, Bill Karakostas<sup>b</sup>

<sup>a</sup>Department of Computation, UMIST, Manchester, M60 1QD, UK <sup>b</sup> Centre for HCI Design, City University, London, EC1V 0HB, UK

Received 1 October 2002; accepted 1 December 2002

Available online 21 January 2003

## Abstract

Due to the market-driven nature of modern organisations, it is important that they can easily adapt to changing business needs. In order to be able to do so, organisations need to employ information systems that exhibit the important characteristic of adaptability. Change, however, is risky because it encompasses unpredictable behaviours. Organisations, in order to minimise this risk, employ decision support systems (DSS) techniques that enable predictions to be made. This paper describes a simulation methodology, based on the combination of business objects and system dynamics that assists organisations in predicting future behaviours. The methodology eliminates the need for duplicate models of enterprise operation and simulation, and introduces a framework that enables the unification of the two in a single model. <sup>D</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: System dynamics; Business objects; Simulation

## 1. Introduction

Decision support systems (DSS) are software products that help users apply analytical and scientific methods to decision making. They work by using models and algorithms from disciplines such as decision analysis, mathematical programming and optimisation, stochastic modelling, simulation, and logic modelling. DSS products can execute, interpret, visualise, and interactively analyse these models over multiple scenarios. DSS through systems simulation evolved from a traditional trial and error technique into a forecasting methodology that assists organisations coping with business change more intelligently. DSS could assist decision-makers in problems involving risk management and the need to balance conflicting objectives. When well implemented and used wisely, DSS can significantly improve the quality of an organisation’s decision making. In this paper, we explain how our proposed framework (integration of business objects and system dynamics) could be employed in developing DSS.

## 2. Problem identification

Organisations evolve continuously and, as a result, their business processes need to be engineered in a way that would enable enterprises to cope with the changing business requirements. Information systems are the backbone of organisations, therefore changing the business strategy results in changes in the information systems themselves. Since simulation models represent organisational behaviour, modifications to the business processes need to be reflected in the simulation model. In order to cope with the everchanging nature of organisations, information systems engineers concentrate on the adaptability characteristics of systems. In order to accomplish this, a movement was made towards adopting object orientation in designing information systems [6].

Because of the characteristics of business objects, applications employing them are easily modifiable, adaptable, and scalable [1,2,9]. Simulation models, however, are not as modifiable. However, modifications in the organisation’s behaviour need to be reflected into the simulation model in order to have any benefits from simulation. Since the operational and simulation models of the organisation are not identical, continuous alterations of the simulation model are necessary in order to map the changes in the operational model. This task is considerably complex and time consuming [9].

In addition to the above, the simulation process necessitates the execution of the model on a variety of ‘‘What if’’ scenarios that correspond to realistic conditions that need to be examined. In order to achieve this, it is necessary to translate the high level scenarios into low level simulation notation. During this process, a considerable number of simulation variables must be populated, a task that is tedious, redundant, and time consuming [8].

Additionally, traditional simulation methodologies require the simulation model to be constantly supplied with statistical information that describes the current state of the organisation. This information is obtained from the operational model. Analysing, extracting, and finally supplying information to the simulation model can be costly.

Finally, simulation models need to be communicated to the management for accuracy and correctness. However, most of the simulation methodologies employ mathematical modelling, which can easily become very complex and messy for non mathematically oriented people such as the business managers.

To overcome the deficiencies of separate operational and simulation models, it is necessary to adapt a new methodology, which combines the two models into a single framework.

## 3. The proposed solution

Considering the drawbacks of existing simulation methodologies, the new approach overcomes these by combining the advantages of business and simulation modelling into a single framework. Since business objects directly map to business concepts, they form the most appropriate technique for modelling organisations. Integrating business objects with simulation objects enable the elimination of duplication of business process modelling for simulation and enterprise operation. As a result, information consumed or produced during enterprise operation can be directly communicated to the simulation model. Moreover, since the two technologies are integrated, they can inherit each other’s characteristics. As a result, simulation models inherits the natural business-modelling feature of business objects, characteristic which would enable the communication of the models representation to business-oriented people and scenarios (based on business rules embedded in each business object) could be directly supplied to the simulation model without any human intervention. Finally, the high coupling and low cohesion characteristics of business objects enable the fast and easy application evolution in order to meet changing business requirements [6]. Simulation models also benefit from this characteristic of business objects since they are integrated into a single framework.

In order to reduce complexity, the proposed methodology concentrates on the business model of the organisation as the basis to develop several system dynamics models each one focusing on a specific business aspect. Each business aspect influences and is influenced by other business aspects, with interrelationships between the business aspects formed as interconnections between the system dynamics models. Keeping the complexity of the system dynamics models low (one business aspect per model) enables its comprehensibility by management [7]. Since business objects are the main actors of business models (incorporating information and functionality), encapsulating system dynamics models in business objects enables the cooperation of the two. This approach enables business objects to supply the simulation models with information from the operational model of the organisation. Business objects interact with each other, but they are also independent of each other. The main advantage of this methodology is the one to one mapping between information systems and the reality they represent. Business objects have also complete control of their embedded simulation models, and can communicate ‘‘What if’’ business scenarios to their simulation model dynamically.

## 4. Anatomy of a business object

The building blocks of business objects are listed below and further analysed subsequently.

 Recorder: this is a facility that enables the monitoring of business process operation through recording its performance and transactions.

 Business rules: these are strategies and policies of organisations that concentrate on specific business concepts and realised by business objects.

 System dynamics co-model: system dynamics models correspond to the dynamic aspects of each business concept and are described in a system dynamics notation.

 Methods and attributes: the actions that the business object can perform, the characteristics that distinguish it from the rest of the business objects, and the information that can communicate to the rest of the business objects.

The main purpose of the recorder is to maintain activity logging records of the object’s actions (monitors business objects) and to provide an audit trail for all corporate processes, information that is important for the stochastic aspects of the simulation. The recorder is mainly active during system operation, where the operational aspects of the business objects are utilised. During that time, information concerning the state and actions of the business object is registered in a time-oriented sequence together with information concerning the performance service and execution time.

Business rules represent the constraints that govern both business objects and simulation models. Constraints in business objects enforce the operation of business processes in pre-specified borderlines. In the same manner, simulation is influenced by the same business rules. Business rules may sometimes be realised by simulation models as targets to be reached or conditions to be satisfied.

The third element of a business object is the simulation model. As stated before, this model is realised in system dynamics notation and focuses on the same business concept as its encapsulating business object. Since the model is not operation independent, it is important to feed it with the necessary data that will enable its enactment. Such data are normally supplied from its incorporating object or collaborating business objects. Business rules governing the model are initially transformed into their equivalent numerical format, which influence variables in the model, prior to their execution. Specific parameters of the model are available to other simulation models (retained in separate business objects) in order to preserve the feedback loop paradigm of system dynamics [3 –5].

Finally, methods and attributes of the business objects are used during the operation and simulation of the business process. Some attributes though are public to all objects and represent the state of variables in their simulation model that is important to other business objects. Communicating business objects can also update the state of variables that belong to other business objects simulation models (Fig. 1).

![](/api/attachments/VQZEB4DE/fulltext/images/4d6cf1ee83c663ef5922ef73d21991487749aca08efe133c939d5970d4eb0e79.jpg)  
Fig. 1. Business objects anatomy and communication.

## 5. Advantages of the proposed approach

Integrating two powerful technologies like those used in our approach combines the benefits of both. The advantages of such integration are analysed below.

## 5.1. Interface perceptiveness

Integrating business objects with system dynamics provide an intuitive interface to the simulation engine based on real world concepts. This is due to the ability of business objects to abstract from business concepts ignoring the intricacies inside them.

## 5.2. Business-oriented modelling

Business object reduces the complexities that exist in the simulation model by presenting the user only with the information that is needed to utilise the model.

5.3. Combined business process and simulation models

Business objects and system dynamics concentrate on the same business process models of the organisation, therefore the same business aspect is represented by the object and simulation model.

## 5.4. Scalability

The simulation models can be easily extended by attaching additional business objects to the existing structure.

## 5.5. Goal-seeking simulation

Business rules embedded in business objects govern the operational and simulation activities of the business process model.

## 5.6. Comparative simulation

Since the output of simulation is stored in the business objects themselves, various comparisons can be made between the results of ‘‘What if’’ scenarios. This enables the visualisation of the implications that a business change might have on the organisation.

## 5.7. Backtrack simulation

Since business objects are ideal for storing information related to the status of the business aspects they represent, they could use such historical data in combination with the simulation model that they encapsulate to recreate past behaviour of organisations. Simulating the organisation in a backward manner would enable the identification of the diversion point in the business processes.

## 6. Conclusions

The integration of business objects and system dynamics has been proven appropriate for the development of a decision support system such as manpower planning and production planning based on case studies that have been carried out using the methodology. Information that has been traditionally isolated in legacy systems is now an active participant in the simulation process of the system. Business object technology is acting as the link between system dynamics models and task-oriented representation of the system, which result in improved usability.

## References

[1] T.H. Davenport, J.E. Short, The new industrial engineering: information technology and business process redesign, Sloan Management Review 31 (4) (1990) 11 – 27.

[2] P. Eeles, O. Sims, Building Business Objects, Wiley, New York, 1998.

[3] F.E. Emery, Systems Thinking, Penguin Books, Harmondsworth, 1969.

[4] J.W. Forrester, Industrial Dynamics, MIT Press, Cambridge, MA, 1961.

[5] J.W. Forrester, System Dynamics and the Lessons of 35 years, Sloan School of Management, Massachusetts Institute of Technology, Massachusetts, 1991.

[6] I. Jacobson, The Object Advantage: Business Process Re-engineering with Object Technology, Addison-Wesley Publishing, Massachusetts, 1994.

[7] B. Richmond, Systems thinking: critical thinking skills for the 1990s and beyond, System Dynamics Review 9 (2) (1993) 113– 133.

[8] P.M. Senge, A. Kleiner, C. Roberts, R. Ross, B. Smith, The Fifth Discipline Fieldbook, Nicholas Brealey Publishing, London, 1994.

[9] D. Taylor, Business Engineering with Object Technology, Wiley, New York, 1995.

![](/api/attachments/VQZEB4DE/fulltext/images/d821247f16e39b1728cebba44094bc91564ac6389f7a504cf666d08226fe027d.jpg)

Andreas Gregoriades holds a PhD and MPhil in Computer Science. Currently, he is employed as a Research Associate at the Centre of HCI, Department of Computation, University of Manchester Institute of Science and Technology (UMIST). His research interests cover system engineering, human reliability, requirements engineering, systems thinking, enterprise modelling, and business process simulation. He has been involved in a number of

EPSRC and European R&D projects in the areas of business process modelling and simulation, software architectures and human reliability assessment. He has also acted as a reviewer for international conferences.

Bill Karakostas is a senior lecturer in the Centre for HCI Design, which is part of the School of Informatics in City University, London. He was previously with the Department of Computation in UMIST, Manchester. Bill holds a Masters in Computer Engineering and Informatics, from Patras University in Greece and an MSc and PhD in Software Engineering, both from UMIST. He has a 12+-year research track in areas such as business engineering (process simulation, modelling, redesign, and workflow management), business object technologies, and software engineering (software reuse and component-based development).

He has been the technical coordinator of many European R&D projects that investigated in the areas of software evolution and reuse electronic commerce systems safety assessment and software architectures in the banking, retailing, shipping, and automotive industries. He has also been technical editor and evaluator for European Commission Research Programmes ESSI and Framework V. He has acted as a reviewer for academic journals, as EPSRC proposal referee and as a member of many conference and workshop committees. Bill has published over 60 academic papers in journals and conferences.
