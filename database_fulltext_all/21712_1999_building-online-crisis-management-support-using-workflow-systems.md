---
otero_id: 21712
otero_key: "9TMHFUYF"
title: "Building online crisis management support using workflow systems"
authors: "Hing-Yin Mak; Andrew P Mallard; Tung Bui; Grace Au"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00007-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Building online crisis management support using workflow systems

Hing-Yin Mak <sup>a,)</sup>, Andrew P. Mallard <sup>b,1</sup>, Tung Bui <sup>c,2</sup>, Grace Au <sup>d,3</sup>

<sup>a</sup> Computer Science Department, Hong Kong Baptist UniÕersity, 224 Waterloo Road, Kowloon, Hong Kong, China

<sup>b</sup> Brunel UniÕersity, Uxbridge, UK

<sup>c</sup> The UniÕersity of Hawaii, Honolulu, USA

d <sup>d</sup> Hong Kong UniÕersity of Science and Technology, Hong Kong, China

## Abstract

While workflow systems have typically been proposed for automating formal business procedures, this paper presents a novel application of workflow technology to coordinate and disseminate tasks and related information for crisis management support systems CMSS . This is because an essential requirement for CMSS is that response times must allow the decisionŽ . maker time to appropriately react to an unfolding situation, and where untimely delays could negate the usefulness of even the most sophisticated system. This paper discusses the potential benefits of using a workflow approach for CMSS, and describes the development of a suitable framework for an existing Swiss government CMSS. Results indicate that the ability of workflow technology to coordinate, monitor, organize and distribute specific tasks and the associated required information in a timely and efficient manner appears to make it an ideal tool for strategic crisis management. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Workflow; Crisis management support systems

## 1. Background

## 1.1. Crisis management support system

In a crisis, crisis management support system Ž . CMSS is expected to help its users prepare, analyze, and resolve conflict. A CMSS can be designed to help decision makers: i access large on-lineŽ . databases to cope with information overload and analyze data reliability, ii consult distributedŽ . knowledge bases using case-based reasoning to learn lessons from past crisis, and iii use group decisionŽ . support system DSS to alleviate problems relatedŽ . to group pathologies, improve decision quality, and enhance an organization’s readiness to deal with catastrophe 4,13,14 .

Bui 7 described a research project for an organi-<sup>w</sup> <sup>x</sup> zational computing system to deal with large-scale crises. The project was sponsored by the Swiss Federal Government, and involved the design of a CMSS to evaluate acceptable countermeasures to reduce accidental ingestion doses of radioactivity. This was necessitated by the economic and political catastrophe created in Switzerland as a result of the

![](/api/attachments/9TMHFUYF/fulltext/images/3e6d25c0b93388f92dee3c6b878bc2971d707455dd637c9889aaff6ec29255ca.jpg)  
Fig. 1. A pictorial representation of the CMSS physical model.

Chernobyl accident. As a result, the federal government decided to adopt a more pro-active role in planning and managing crises 11 .<sup>w</sup> <sup>x</sup>

Bui’s research has contributed to the conceptual design of a nationwide, real-time CMSS in Switzerland. A simplified version of the physical representation of this CMSS model is depicted in Fig. 1, and shows the interactions, connection methods and proximity between different specialty experts, expert teams and computer systems. Every 10 min and at 55 different locations, the system continuously checks radioactivity levels. If the level of radioactivity at one location seems abnormally high, radioactivity experts are informed to assess potential radiation risks, together with other civil risks or diseases. Countermeasures to reduce ingestion dose in veg-Ž etables or animal foodstuff are generated and evalu- . ated using contamination assessment algorithms. The recommendation package is then sent to high-level government officials represented as Politicians inŽ Fig. 1 for evaluation and a final decision, using a. computerized voting technique. A more detailed description of the Swiss CMSS architecture will be discussed in Section 3.

## 1.2. Workflow management

From a strict operational perspective, workflow deals with the automation of business processes. A workflow could be a one-time-only process or ad hoc workflow, a collaborative process that coordinates a team working together to achieve a goal Ž . e.g., designing systems specifications , or a missioncritical, transaction-oriented production workflow. A workflow management application defines all the business processes, from the start to finish, including all exception conditions, tracks process-related information and the status of each instance of the process as it gets executed.

An efficient workflow is one that is 1 capable ofŽ . identifying the best procedural routes either serial, Ž parallel or conditional , and 2 able to document and . Ž . make use of rules to ensure the proper load balancing of work assignments based on established business principles and roles of process participants.

Workflow management technology provides a mechanism for planning and controlling how people work together in business environments. It acts as the connectivity tools to manage, monitor, organize and distribute specific business tasks and the associated required information. A principal concept in workflow management is the coordination of tasks in the business process. The medium through which these are conducted might include verbal information, human gesture, documents, images, graphics, sounds and<sup>r</sup>or any type of ‘information’. Due to this wide scope of workflow management, it is difficult to find any one complete definition for it, even though many different definitions have been put forward 20,21,26,37 .

What is clear about workflow management, however, is that it is a flexible tool. By analyzing and writing down an existing sequence of work steps in a structured manner, organizations are forced to examine or re-examine their business procedures. Also through the distribution of activities and associated information, organizations gain a better understanding of their business processes. In addition, one can define the exceptions or desired changes in the business operation, and then work out how best to express the work sequences and convert them into standard routines.

Workflow management can, therefore, be used for the analysis of existing workflow processes within a business in order to spot potential bottlenecks. As a result, workflow management can help businesses re-engineer their workflow patterns in order to eliminate any unnecessary shortcomings. Therefore, a business workflow model can provide an effective medium for experimenting with, and evaluating the consequence of, different organisational changes within the model prior to final implementation.

## 2. Why workflow for CMSS?

A number of workflow management characteristics would appear to be beneficial to CMSS.

## 2.1. Automation and coordination

Research in the field of Computer-Supported Cooperative Work CSCW has often underlined the Ž .

importance of physical proximity among team members 9,39 . However, a characteristic of workflow<sup>w</sup> <sup>x</sup> management is that it consolidates existing office automation and document management technologies under a single environment, as it often represents the critical link between technology and people 24 . <sup>w</sup> <sup>x</sup> Therefore, in light of recent advances in technology, especially in Internet technology, the authors believe that workflow management systems now offer a means of breaking this geographic reliance.

The workflow analysis also helps identify places where technological support can be valuable 27,36 , <sup>w</sup> <sup>x</sup> or even fully automated. By getting more time out of existing human-intensive processes, successful routing and queue management capabilities can provide better efficiencies.

## 2.2. Visualization and simulation

Having constructed the initial workflow model, various simulations can then be run to identify potential bottlenecks or possible breakdowns. In the case of CMSS, a workflow model would be able to simulate a whole range of possible actions, such as the interactions between the various CMSS processes, and the mechanisms for distribution of tasks and associated information. As a result of this simulation process, an organization is able to gain a better understanding of its work<sup>r</sup>business processes, and therefore, restructure them more effectively.

One of the important benefits of constructing a workflow model is, that the modeling process itself gives the opportunity to re-think thoroughly business processes within an organization. This characteristic would appear to be useful in the development of a successful CMSS, where a good understanding of the environment in which decision-making is to take place is required.

## 2.3. Seamless tool integration

It has been shown that concurrent use of decision analysis techniques, multiple criteria methods, expert systems and decision support technologies, negotiation and group decision making approaches has been effective in dealing with large-scale crises 7 . How-<sup>w</sup> <sup>x</sup> ever, the magnitude of decision and communications tasks during a crisis period is the greatest obstacle standing in the way of building effective CMSS. While decision techniques were appropriately chosen and implemented in the Swiss CMSS, the information flow was not as seamless as it could have been <sup>w</sup> <sup>x</sup> 8,10 .

Workflow management systems provide the functions to coordinate user and system participants, together with the appropriate data resources, which may be accessible directly by the system or off-line, to achieve defined objectives by a set deadline 15 .<sup>w</sup> <sup>x</sup> Workflow management also provides the tools to measure and monitor the progress of the work activities, thereby imposing a better level of quality control. This is also important in CMSS, where quick feedback on the results of previous decisions is critical to help decision makers monitor the outcome of their actions 17 .<sup>w</sup> <sup>x</sup>

## 2.4. Efficiency

In workflow modeling, a series of rules is established to drive the workflow processes. These rules describe where the tasks and associated information should go, and what should be done with them 30 .<sup>w</sup> <sup>x</sup> This helps an organization to improve the speed and timeliness of distribution, as well as minimize misrouting. As existing workflow processes are analyzed, loopholes and hidden inefficiencies become visible, which can then be eliminated through the development of automated workflow rules 23 .<sup>w</sup> <sup>x</sup>

A well thought-out workflow process can also achieve time savings. This is an essential requirement for CMSS, where response times must allow the decision maker time to appropriately react to the unfolding situation, and where untimely delays could negate the usefulness of even the most sophisticated system.

Furthermore, because many workflow systems make use of integrated electronic messaging to automate the movement and routing of electronic information, they can provide the added benefit of information filtering—thereby reducing data overload. This information resource management functionality is important to CMSS, where there is a need for clear, timely, reliable, valid and wide-ranging information.

## 3. The Swiss CMSS project

The aim of the ‘Swiss CMSS model’ is to evaluate the most efficient and acceptable countermeasures after an accidental release of radioactivity. In Fig. 2, the overall system architecture of the CMSS is shown to comprise five main processes, and a number of special crisis management tools. This CMSS can be split into two decision making levels: Ž .a the ‘expert’ level comprising the first four processes, and b the ‘political’ level involving the Ž . final process. A complete description of the system architecture can be found in Refs. 7,10,35 .<sup>w</sup> <sup>x</sup>

## 3.1. EnÕironmental scanning and sensoring system

Air-borne radioactivity is measured every 10 min at 55 monitoring sites throughout the entire country Ž . the NADAM system . The ambient radioactivity level is recorded and transmitted by phone-line to a central computer, where the levels are checked seeŽ Fig. 1 . The sensoring system compares the incom-. ing measured levels against the normal background radiation values. Should the difference between these levels rise above a certain pre-determined level, then an alarm is raised automatically. If this alarm is raised, then the corresponding Alarm Team must meet.

## 3.2. Threat assessment component

Following an alarm, the extent of the crisis has to be judged by a team of experts. This is indicated by the size of the discrepancy between the normal and increased radioactivity measurements, and is determined by the perceived value of the possible loss, the perceived probability of loss and the perceived time pressure.

Since radiation damage cannot be measured directly, several calculations have to be made before being able to assess the different kinds of risk thoroughly. These calculations involve the determination of the activity concentration in the contaminated foodstuffs and the committed dose equivalent, which indicates the existing risk for individuals. For this system, the calculation code, ECOSYS 29 , is used.<sup>w</sup> <sup>x</sup> The radioactive contamination is then assessed by region, with different scales of impact, and a series of priority vectors is then determined.

## 3.3. Generation of the possible countermeasures

In order to provide the decision makers with a comprehensive range of countermeasures to reduce the ingestion dose, both ‘possible’ and ‘feasible’ alternatives must be identified. Although a large number of ‘possible’ countermeasures have already been evaluated in a literature survey 34 , the genera-<sup>w</sup> <sup>x</sup> tion of the range of ‘feasible’ countermeasures is more complex. This is because not only single countermeasures have to be considered, but also combinations of them may be of interest. Due to its complexity, this process is supported through the use of an expert-system 35 .<sup>w</sup> <sup>x</sup>

## 3.4. Expert eÕaluation

In this process, a group of experts has to decide how reasonable the collated countermeasures are, largely based on different technological criteria. These are then ranked for the politicians, according to a series of defined criteria and multi-criteria methods 5,6,31 .<sup>w</sup> <sup>x</sup>

In order to avoid isolation of the different decision making groups, in the four processes that involve crisis management staff, additional experts need to be easily contacted throughout the crisis situation. To facilitate this, a support system has been developed at the University of Fribourg 16 , <sup>w</sup> <sup>x</sup> using the software product, Netcalc, and which contains information such as field of expertise, experience, contact information, etc.

## 3.5. Political eÕaluation

In this final process, the politicians have to decide on the propositions made by the experts. Because the political decision makers have to take-over the political responsibility for the execution of the countermeasures, they are asked to decide about the final ranking of the proposed countermeasures with respect to political and economic criteria. The politicians are free to accept the rankings of the experts without any change, to accept the proposed list but adjust the rankings, or to return the proposed solutions asking for alternate ones.

![](/api/attachments/9TMHFUYF/fulltext/images/0da2df96317eeba8322a6705ac2655e72ef5c8fcd3a736a23adc0e57042cd38a.jpg)  
Fig. 2. A crisis management decision support system for evaluating acceptable countermeasures to reduce ingestion dose after an accidental release of radioactivity.

## 4. The analysis and design workflow model for the CMSS

For this analysis, the authors used the Action-Workflow <sup>w</sup> Enterprise Series 3.0 suite of software, which included the AW Process Builder DeveloperŽ Edition and AW Manager. .

## 4.1. Why ActionWorkflow<sup>w</sup>?

<sup>w</sup> We have adopted the ActionWorkflow AWŽ . approach for process analysis and design as it not only includes the capacity for generating and managing forms, as with traditional workflow approaches, but also makes use of action workflow loops. The latter are grounded in the dimension of business process structure, and allow individuals to deal directly with the consequences of their work for completion and satisfaction 22,27 .

The AW approach was established by Winograd and Flores 38 , and is one of the workflow modeling<sup>w</sup> <sup>x</sup> approaches which focuses on the coordination between people and how people communicate. For every workflow loop, there is both a ‘customer’ and ‘performer’. The loop itself is defined as the coordination between them, and is represented by a conversation pattern comprised of four-phases: proposal, agreement, performance and satisfaction. Tasks are defined by the requests and commitments expressed in the loop. A workflow process is a collection of these loops with links between them. Each workflow loop is independent.

In the first request phase, a customer asks the Ž . performer for an action. The performer then agrees to it in the second commitment phase. In the thirdŽ . Ž . performance phase, the performer then fulfills the work and reports it done. In the final evaluationŽ . phase, the customer accepts the report and declares satisfaction.

Therefore, the ultimate goal of any AW process is that of customer satisfaction. This implies that workflow loops have to be closed, and that the customer must acknowledge that the work has been satisfactorily completed. At any phase, there may be additional actions, such as clarification, further negotiations about the conditions, and changes of commitments by the participants 38 .<sup>w</sup> <sup>x</sup>

One of the main differences between the AW and traditional workflow approaches is, that in the latter, actions of coordination are seen as one kind of task or as a flow of information between tasks. However, in the AW approach, the requests and commitments define tasks expressed in the loops 27 .<sup>w</sup> <sup>x</sup>

The use of the AW approach, based on a fourphase action loop, has been well-used and documented, e.g., managing the review of job candidates for hiring personnel 27 ; professional processes in <sup>w</sup> <sup>x</sup> advertising at Young and Rubicam 25 ; providing <sup>w</sup> <sup>x</sup> and managing financial services in banks 3,33 ;<sup>w</sup> <sup>x</sup> curriculum management at George Mason University <sup>w</sup> <sup>x</sup> 12 ; a remote sensing business process for rapid estimates of agriculture in Europe 40 ; redesign of a <sup>w</sup> <sup>x</sup> hospitals patient evaluation report 19 ; managing the <sup>w</sup> <sup>x</sup> life-cycle of annual training programs 32 .<sup>w</sup> <sup>x</sup>

## 4.2. Basic workflow

Applying the AW approach described earlier in Section 3 to the Swiss CMSS model Fig. 2 , weŽ . obtain the Basic Workflow shown in Fig. 3.

![](/api/attachments/9TMHFUYF/fulltext/images/293d0440c58a6e06a7b7c183ac41d425b2bd0e581e01f9bf96359cf48cae242d.jpg)  
Fig. 3. The basic workflow.

The customer Alarm Team requests the serverŽ . Ž . CMSS Server to evaluate the acceptable countermeasures to reduce ingestion dose after an accidental release of radioactivity.

Phase 1 corresponds to a request to reduce the level of radioactivity to safe levels.

Phase 2 corresponds to a commitment to reduce the level of radioactivity.

Phase 3 corresponds to suitable actions to reduce the level of radioactivity.

Phase 4 corresponds to the eÕaluation of the effectiveness of the measures to reduce the level of radioactivity to safe levels.

## 4.3. Second and third leÕel workflows

By modeling and expanding the Basic Workflow shown in Fig. 3 using the Swiss CMSS diagram in Figs. 1 and 2, we obtain the seven distinct conceptual second-level workflow loops shown in Fig. 4. These are: Data Collection, Threat Assessment, Generation of Countermeasures, Experts Countermeasures, Politicians Countermeasures, Execution and Evaluation.

These second-level workflow loops are then modeled again according to the four-step loop to create the third-level workflows shown in Fig. 5. The second- and third-level workflows derived from the Basic Workflow are described below.

## 4.3.1. Data collection workflow

The first phase of the Basic Workflow represents the service request. This request, to reduce the level of radioactivity, initiates the Swiss CMSS. The analyzed Environment Scanning and Sensoring System processes are grouped in this phase and have been modeled and represented as third-level workflow loops in Fig. 5.

The EnÕironment Scanning Workflow uses an automated measuring and recording system called NADAM. The performer for this workflow is therefore NADAM. As the customer coordinates with NADAM, we have deliberately represented this workflow with a ‘radiation’ icon to make it more meaningful than the standard workflow icon.

The Sensoring System Workflow processes the data from NADAM, and automatically raises an alarm if detected radiation levels are above pre-determined levels. The performer is Alarm System, and this workflow has been represented with the more meaningful ‘alarm’ icon.

![](/api/attachments/9TMHFUYF/fulltext/images/b31c3fa1248c22014a0641096d61d508a72f205e52ce9338f8b4519f897a95c6.jpg)  
Fig. 4. Second-level workflow.

![](/api/attachments/9TMHFUYF/fulltext/images/25765ed65a4a076de793ddd443625458e5377915b5ea57492b5ce8b00347f846.jpg)

## 4.3.2. Threat assessment workflow

Because the threat assessing process shows the commitment between the customer and the performer, it has been mapped onto phase 2 of the Basic Workflow. For this phase, additional actions are further modeled in order to clarify the sub-processes within the Threat Assessment Workflow. The main purpose of this workflow process is to assess the current situation after the accident, calculate all types of risks for different populations and generate priority vectors for decision makers. The third level workflow loops therefore, include ECOSYS Calculation, Method Base Group Decision, Evaluate Threat Consequences, Risk Assess and Priority Vector. For each of these third-level loops, there are different performers to serve the CMSS Server.

The ECOSYS Calculation Workflow uses ECO-SYS to evaluate the committed dose equivalent for different foodstuffs and different groups of people, and determines the resulting impact of the different radiation sources. This workflow will be served by the calculation code, ECOSYS 29 . However, the input for the ECOSYS code, such as the deposited activity on soil, on crops and the measured activity in the air, can be semi-automated.

Problems of group or collective decision making are relevant if decisions have to be made by a committee or a group. The two group problem solving approaches used in this CMSS are the theory of social choice and expert judgement 18 . The<sup>w</sup> <sup>x</sup> Method Base Group Decision Workflow includes two simple methods for collective decision-making, sum-of-theranks rule and multiplicative ranking 6,18 . These <sup>w</sup> <sup>x</sup> group decision methods will be used throughout all the Swiss CMSS processes. The performer for this workflow is, therefore, the combination of the two methods and the CMSS Team, and has been named as Method Base System. Clearly, this third-level workflow can be further modeled to include additional actions such as clarifications and further negotiations about the conditions.

The main purpose of the EÕaluate Threat Consequences Workflow is to find out the consequences of the accidental release of radioactivity. A number of methods are used to determine this, including the Analytic Hierarchy Process AHP 31 andŽ . <sup>w</sup> <sup>x</sup> PROMETHEE 5 methods, which are collectively<sup>w</sup> <sup>x</sup> grouped into this workflow. The performer is the Specific Methods System. As this workflow again consists of a mixture of computer systems, manual calculation, human–human and human–computer negotiations, further workflow loops can also be added.

The Risk Assess and Priority Vector Workflow models the negotiation and discussion between the additional experts and the threat assessment teams. This will finalize the threat assessment process and complete the negotiation phase of the Basic Workflow. The performer for this workflow is additional experts, and this workflow has been represented with the more meaningful ‘group’ icon. Further refinement and discussion of this workflow loop can be found later in Section 4.4.

The performance phase or third phase of the Ž . Basic Workflow consists of four second-level workflow loops—Alternatives Generation, Experts Evaluation, Politicians Evaluation and Execution. Each of these workflow loops is modeled on its functionality and is described below.

## 4.3.3. Generation of countermeasures workflow

This workflow is the first one to be initiated after all actions of the Threat Assessment Workflow have been completed. It can be further modeled with three additional third-level workflow loops: generate alternatives, generate all possible countermeasures and expert discussion.

The Generate AlternatiÕes Workflow has been designed for receiving information from the previous phase, setting up any necessary computer systems and concluding the objectives of the Generation of Countermeasures Workflow, so that it can initiate the next Experts Countermeasures Workflow. The performer is the Threat Assessment Process Team and is named as the Alternatives Generation Group.

The aim of the Generate All Possible Countermeasures Workflow is to determine all feasible countermeasures to reduce activity concentration in plant or animal material. Other constraints such as the restricted amount of time and limited resources also needs to be considered. For these particular requirements, the use of an expert system has been proposed. This situation has been modeled and represented as a third-level workflow loop shown in Fig. 5. The performer for this workflow is an Expert System. As the customer coordinates with a computerized expert system, this workflow has been represented with the more meaningful ‘system’ icon.

The Expert Discussion Workflow models the negotiation and communication between the Additional Experts and the Alternatives Generation Group. The performer for this workflow is Additional Experts, and this workflow has been represented with the more meaningful ‘group’ icon.

## 4.3.4. Experts countermeasures workflow

This workflow is initiated by Generation of Countermeasures Workflow. All feasible countermeasure information will be passed onto this workflow. In order to complete all actions, five third-level workflow loops are defined to accomplish all tasks. These are Experts Evaluation, Stress Management for Experts, Evaluate Expert’s Countermeasures,

Group<sup>r</sup>Individual Decision and Ranking Propositions.

The function of the Experts EÕaluation Workflow is similar to that of the Generate AlternatiÕes Workflow. It is modeled to receive all information from the previous workflow, coordinate all other workflow loops within the Experts Countermeasures Workflow, and finally prepare any information for the next workflow loop.

The Stress Manager module itself is not an on-line real-time system, but has been modeled in the Stress Management for Experts Workflow. The main purpose of this workflow is to allow for the simulation of the effectiveness of the Stress Manager module to reduce the level of stress that can arise in the crisis situation. The performer in this workflow is, therefore, the Stress Manager.

The basic function of the Group<sup>r</sup>IndiÕidual Decision Workflow loop is similar to the Method Base Group Decision Workflow and has the same performer.

![](/api/attachments/9TMHFUYF/fulltext/images/2e78d0f92d76ede9fb5d42623c8e28b457a3379fcd2f913b7fd87fd9efe9b4b9.jpg)  
Fig. 6. Expert discussion workflow.

The function of the EÕaluate Expert’s Countermeasures Workflow is similar to the EÕaluate Threat Consequences Workflow, but evaluates the consequences of the proposed ranking propositions for the politicians. Hence, it has the same performer, Specific Methods Systems.

The function of the Ranking Propositions Workflow is to produce the final ranked list of suitable countermeasures for the politicians. Within this process, additional experts are called upon when required.

## 4.3.5. Politicians countermeasures workflow

The components in this workflow are similar to those in the Experts Countermeasures Workflow. A number of specific methods and group-decision algorithms mentioned above will also be used here. This workflow will be initiated by the completion of Experts Countermeasures Workflow. The proposed ranking propositions will be examined in the political rather than the expert sense. This workflow can be further modeled into five third-level workflow loops. These are Politicians Evaluation, Stress Management for Politician’s Countermeasures, More Group<sup>r</sup>Individual Decision and Decision-Making.

## 4.3.6. Execution workflow

Although the action of carrying out the countermeasures is not directly under the control of the Crisis Management Team, it is still modeled here as a workflow. This is because when conducting artificial simulation, assumptions can be made and the whole workflow can be examined. The performer for this workflow is the Government Minister. This workflow will not be described in detail.

## 4.3.7. EÕaluation workflow

The Cybernetic Control process shown in Fig. 2 will be mapped onto the satisfaction fourth phaseŽ . of the Basic Workflow. This verifies and declares the Alert Teams satisfaction with the effectiveness of the countermeasures to reduce the level of radioactivity. In the Swiss CMSS model, it can also be recognized as a feedback component.

![](/api/attachments/9TMHFUYF/fulltext/images/9f85520cfab5f2777d4619cec0cdc421b65844189fa97f49972ebc25239e28c6.jpg)  
Fig. 7. Expert database contact form.

## 4.4. Characteristics of specific processes

The Swiss CMSS workflow shown in Fig. 5 consists of 23 interconnected workflow loops. However, this does not fully represent the full complexity of the model.

Most current approaches to workflow management are structured around the domain of information processes 28 , and typically involve the use of<sup>w</sup> <sup>x</sup> business process workflows to create and manage forms, and automatically route information. However, in the case of the Swiss CMSS workflow, the situation is more complicated, as the model must also allow for a large degree of human interaction. To demonstrate this hidden complexity, we will now further refine and improve the Expert Discussion Workflow shown in Fig. 6.

In order to complete the process of Expert Discussion Workflow, individuals and<sup>r</sup>or groups of experts must first be contacted, before any dialogue or consultation process can take place. The contact mechanism can take a number of forms, including: by person within the same office , by phone, by fax, Ž . by E-mail, etc. These individuals or groups of experts may in turn contact further individuals or groups of experts. In this way, the simple Expert Discussion workflow icon shown in Fig. 5 could actually represent a complex series of interconnecting workflows. However, for the purposes of demonstration, Fig. 6 shows a simplified set of interconnecting workflows, using meaningful icons. Within this workflow, the required experts and their associated contact methods are known. Therefore, we are also able to develop a series of rules and conditions to coordinate, control and monitor the contact for each workflow.

During a crisis situation, it is often difficult to obtain the right experts at the appropriate moment.

For this reason, an organisational component to keep track of a worldwide network of experts has been developed for the Swiss CMSS 16 . However,<sup>w</sup> <sup>x</sup> as AW Enterprise Series provides an ActionWorkflow Basic programming language, additional process components can also be developed. Furthermore, the programming language also allows for script procedures, automation objects and executable modules to be run 1 . In this way, one or more <sup>w</sup> <sup>x</sup> forms or tools can be incorporated into the overall system. Therefore, for the Swiss CMSS workflow, we have the option to integrate it with the existing expert organisational component, and<sup>r</sup>or develop a new one.

![](/api/attachments/9TMHFUYF/fulltext/images/71ee4b584d560e2eecd7eb2f5dd1259bf20357aa1eb88b05f08f2003a8878a0e.jpg)  
Fig. 8. Telephone connection dialog.

A contact form for our prototype, CMSS Expert Database CED , is shown in Fig. 7.Ž .

This tabular form contains Contact Information, ReleÕant Experience and Additional Information for each expert. This database is searchable by name, specialty, experience and location. The Contact Information tab shown includes the specialty, title and normal location of an expert including location time Ž difference , as well as a list of contact phone and fax. numbers, and E-mail addresses. These phone numbers are ranked according to the likelihood of successful contact at that time of day. Furthermore, once a contact number has been selected, a corresponding activation button becomes available. The Phone button activates a modem to dial the number, while the Fax and E-mail buttons use OLE automation to activate corresponding fax or E-mail software. Fig. 8 shows the telephone connection dialog after activating the Phone button.

## 5. Findings and discussion

In this paper, we have proposed the novel application of workflow management to CMSS. While it is clear from this exploratory research that much work is still necessary, initial findings have identified some clear advantages for this approach. As a result of building the workflow model shown in Fig. 5, we have gained a much better understanding of the Swiss CMSS because we have had to clearly identify all the participants, processes, information flows, dialogue channels, and reliance on external systems. This process has also helped us to gauge the overall complexity of the Swiss CMSS, and identify where technological support may be possible in the future. We have also shown that the model can be used to simulate the overall system, thereby identifying potential bottlenecks and allowing for more effective restructuring.

We believe that the AW approach is particularly well-suited to CMSS for a number of reasons. Firstly, because of its emphasis on the monitoring of satisfaction, process quality is ensured at all levels throughout the system. Also, as the AW Process Builder allows for the use of a meaningful icon map, the overall system is easy to understand and visualize, and allows layers of model complexity to be hidden using a grouping function 2 . Furthermore,<sup>w</sup> <sup>x</sup> the Process Builder is extensible, as it can be integrated with other computer systems, and can be customized through its programming language. In the case of the Swiss CMSS, this not only allows for simulations of contacting experts to be run outside of a crisis, in order to identify potential breakdowns, but also allows for improved monitoring of the workflow progress during a crisis.

However, while workflow management does appear to offer clear benefits to CMSS, we must be aware of its limitations. In the case of the Swiss CMSS, the workflow model must also allow for a large degree of human interaction. Therefore, it is unrealistic to expect to create a ‘fully’ automated workflow system because a whole series of negotiations, dialogue, coordinations and communications between individual experts, groups of experts, and systems manual or computerized are involved.Ž .

Another current limitation is that the AW software used for this research provides only internal organization routing, not external, i.e., it is Intranetbased. This is fine for participants in normal business process workflows, which are typically within one controlled organisational environment. However, in the Swiss CMSS workflow, participants such as ‘theŽ experts’ are not limited to one organization or even. one country. They may be individuals, groups or even whole organizations geographically spread around the world. Therefore, the main emphasis of our future work is to investigate the design and development of a web-based workflow framework, which allows for the support of multiple Intranets and individual users into an Extranet. From our preliminary findings, this would appear to be a very promising approach for not only providing the many benefits of workflow to CMSS, but also for creating a single collaborative CMSS virtual environment— free from the previous constraints of geography, time or hardware platform.

Other future work includes the defining of more sophisticated sets of rules to further enhance the Expert Discussion Workflow, and in particular, our CMSS Expert Database. For instance, we intend to explore the possibility of it making allowance for which experts are best contacted, dependent on the time of day relative to their geographic location and their specialist ranking. Also based upon the success of the system to contact an expert, rules might be used to determine which alternative experts should be contacted, or whether an event is escalated or a warning is given.

## References

<sup>w</sup> <sup>x</sup> <sup>w</sup> 1 Action Technologies, ActionWorkflow Enterprise Series 3.0 ActionWorkflow Basic Language Reference Guide, Alameda, CA, 1996.

<sup>w</sup> <sup>x</sup> <sup>w</sup> 2 Action Technologies, ActionWorkflow Enterprise Series 3.0 Process Builder User’s Guide, Alameda, CA, 1996.

<sup>w</sup> <sup>x</sup> 3 A. Agostini, G. De Michelis, M.A. Grasso, S. Patriarca, Reengineering a business process with an innovative workflow management systems: a case study, Proceedings of the Conference on Organizational Computing Systems, ACM, New York, 1993, pp. 154–165.

<sup>w</sup> <sup>x</sup> 4 S. Belardo, R.K. Kirk, An investigation of system design considerations for emergency management decision support, IEEE Transactions on Systems Man, and Cybernetics SMC 14 6 1984 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 5 J.P. Brans, B. Mareschal, P. Vincke, PROMETHEE: a new family of outranking methods in multicriteria analysis, in: J.P. Brans Ed. , Proceedings of the IFORS 84 Conference,Ž . WA, 1984, pp. 408–421.

<sup>w</sup> <sup>x</sup> 6 T. Bui, Co-oP, A Group Decision Support System for Cooperative Multiple Criteria Group Decision Making, Lecture Notes in Computer Science, No. 290, Springer, Berlin, 1987, pp. 58–59.

<sup>w</sup> <sup>x</sup> 7 T. Bui, Decision quality in crisis decisions, Swiss Journal of Management, October 1988.

<sup>w</sup> <sup>x</sup> 8 T. Bui, Decision making quality in crisis situation, Journal of Management, Bern 1989 .Ž .

<sup>w</sup> <sup>x</sup> 9 T. Bui, Towards a theory of shared mental model in CSCS, Proceedings of the 1992 Workshop on CSCW, May 1992.

<sup>w</sup> <sup>x</sup> 10 T. Bui, A. Wicki, An evaluation of CMDSS, Working Paper, University of Fribourg, Switzerland, 1989.

<sup>w</sup> <sup>x</sup> 11 T. Bui, A. Wicki, The conceptual definition of a crisis management DSS for evaluating acceptable countermeasures to reduce ingestion dose after an accidental release of radioactivity, Joint EURO<sup>r</sup>TIMS Meetings, Paris, 1990.

<sup>w</sup> <sup>x</sup> 12 P.J. Denning, R. Medina-Mora, Case study: George Mason University, in: T.E. White, L. Fischer Eds. , New Tools forŽ . New Times: The Workflow Paradigm, Future Strategies, Alameda, CA, 1994, pp. 235–251.

<sup>w</sup> <sup>x</sup> 13 J. Elam, J. Isett, An experiment for decision support for crisis decision-making, Working Paper, Naval Postgraduate School, Monterey, CA, 1987.

<sup>w</sup> <sup>x</sup> 14 P. Gray, The IDSC Crisis Management Center, Final Report, Special Service Agreement 89-00254, Project EGY<sup>r</sup>85<sup>r</sup>006, 1989.

<sup>w</sup> <sup>x</sup> 15 K. Hales, M. Lavery, Workflow Management Software: The Business Opportunity, Ovum, London, 1991.

<sup>w</sup> <sup>x</sup> 16 H. Hauschen, Netcalc, Modellier-, Kalkulations- und¨ Auswertungssystem fur hierarchisch vernetzte Modelle, ¨ Diplomarbeit, Universitat Fribourg, August 1988. ¨

<sup>w</sup> <sup>x</sup> 17 T.J. Hausel, A. Omar, Information system for crisis management: lesson from Southern California, Edison, MIS Quarterly December 1986 .Ž .

<sup>w</sup> <sup>x</sup> 18 C. Hwang, M. Lin, Group Decision Making under Multiple Criteria, Lecture Notes in Economics and Mathematical systems, No. 281, Springer, Heidelberg, 1987.

<sup>w</sup> <sup>x</sup> 19 It’s all in the process, PC World 13 5 , 1995 .Ž . Ž .

<sup>w</sup> <sup>x</sup> 20 S. Jablonski, C. Bussler, Workflow Management: Modeling Concepts, Architecture and Implementation, International Thomson Computer Press, UK, 1996.

<sup>w</sup> <sup>x</sup>21 S. Joosten, G. Aussems, M. Duitshof, R. Huffmeijer, E. Mulder, An Empirical Study About the Practice of Workflow Management, University of Twente Service Centrum, Enschede, 1994.

<sup>w</sup> <sup>x</sup> 22 P.G.W. Keen, Shaping the Future: Business Design Through Information Technology, Harvard Business School Press, Boston, MA, 1991.

<sup>w</sup> <sup>x</sup> 23 T.M. Koulopoulos, Automating the document factory, Inform Ž . July 1993 44–47.

<sup>w</sup> <sup>x</sup> 24 T.M. Koulopoulos, The Workflow Imperative: Building Real World Business Solutions, Van Nostrand-Reinhold, New York, 1995.

<sup>w</sup> <sup>x</sup> 25 R.T. Marshak, Young and Rubicam Improves Productivity With Workflow, Workgroup Computing Report, Patricia Seybold Group, Boston, MA, Vol. 15 6 , 1993, pp. 12–20. Ž .

<sup>w</sup> <sup>x</sup> 26 J.C. McCarthy, W.M. Bluestein, The Computing Strategy Report: Workflow’s Progress, Forrester Research, Cambridge, MA, October 1991.

<sup>w</sup> <sup>x</sup> 27 R. Medina-Mora, T. Winograd, R. Flores, F. Flores, The action workflow approach to workflow management technology, Proceedings of the 4th Conference on Computer-Supported Cooperative Work, ACM, 31 October–4 November, Toronto, Canada, 1992, pp. 281–288.

<sup>w</sup> <sup>x</sup> 28 J. Moad, Viewstar faces many goliaths, Datamation 38 11Ž . Ž . 1992 30–31.

29 H. Muller, G. Prohl, ECOSYS 1986: Ein Rechemodell zur¨ ¨ Abschatzung der Strahlenexposition nach kurzzeitiger Depo-¨ sition von Radionukliden auf landwirtschaftlich genutzten Flachen, Benutzer-Handbuch, Stand Marz 1988, Institut fur¨ ¨ ¨ Strahlenschutz, Gesellschaft fur Strahlen-und Umwelt-¨ forschung, 8042 Neuherberg, BRD, 1988.

<sup>w</sup> <sup>x</sup> 30 B. Reinwald, Workflow-Management, Tutorial 13th IFIP World Congress, Hamburg, Germany, 1994.

<sup>w</sup> <sup>x</sup> 31 T.L. Saaty, The Analytic Hierarchical Process: Planning, Priority, Allocation, Mc-Graw Hill, New York, 1980.

<sup>w</sup> <sup>x</sup> 32 T. Schal, Workflow Management Systems for Process Orga- ¨ nizations, Lecture Notes in Computer Science 1096, Springer, 1996.

<sup>w</sup> <sup>x</sup>33 T. Schal, B. Zeller, Workflow management systems for¨ financial services, Proceedings of the Conference on Organizational Computing Systems, ACM, New York, 1993, pp. 142–153.

<sup>w</sup> <sup>x</sup> 34 A. Schenker-Wicki, Literaturstudie zur Dekontamination und Dekorporation von pflanzlichen und tierischen Nahrungsmit-

teln, Bericht zuhanden des Bundesamtes fur Landwirtschaft, ¨ Bern, 1988.

<sup>w</sup> <sup>x</sup> 35 A. Schenker-Wicki, The Conceptual Definition of A Crisis Management Decision Support System CMDSS for Evaluating Acceptable Countermeasures to Reduce Ingestion Dose After an Accidental Release of Radioactivity, University Press Fribourg Switzerland, 1990.

<sup>w</sup> <sup>x</sup> 36 WfMC, The Workflow Reference Model, Version 0.6, Workflow Management Coalition, 1993.

<sup>w</sup> <sup>x</sup> 37 WfMC, The Workflow Reference Model, WFMC-TC-1003, 29-Nov-94, Version 1.1, Workflow Management Coalition, http:<sup>rr</sup>www.aiai.ed.ac.uk<sup>r</sup>project<sup>r</sup>wfmc<sup>r</sup>, 1994.

<sup>w</sup> <sup>x</sup> 38 T. Winograd, T. Flores, Understanding Computers and Cognition: A New Foundation for Design, Ablex Publishing, NJ, 1986.

<sup>w</sup> <sup>x</sup> 39 F.W. Winter, An application of computerized decision tree models in management–union bargaining, Interfaces 15 Ž . 1985 74–80.

<sup>w</sup> <sup>x</sup> 40 A. Zenie, T. Schal, Analyzing and redesigning a remote\` ¨ sensing business process for rapid estimates of agriculture in Europe, Proceedings of the Conference on Organizationa Computing Systems, ACM, Milpitas, CA, 1995.

![](/api/attachments/9TMHFUYF/fulltext/images/090330f658abe68cb55bd400ef24f6ce41049c972fdadbb57e2e7c24415b09b2.jpg)

Hing-Yin Mak is a lecturer in Information Systems at the Hong kong Baptist University. She received a BSc in Mathematics with Computer Science from King’s College, London, and an MSc in Operational Research and PhD in Information Systems from London School of Economics. Her research interests include web information systems, workflow management, medical informatics, computer-supported collaborative work and virtual organisations.

![](/api/attachments/9TMHFUYF/fulltext/images/a4fa0f83a7bfd610a3fd3944efac4af059ea61640db8d31adc4522da67770279.jpg)

Andrew P. Mallard is co-founder and Director of Computing In Action, a UK-based computer consultancy firm. Over the last 15 years, he has provided consultancy services to a wide range of companies and international corporations, and is currently based in Hong Kong helping to re-assess the use of IT within the health sector. Andrew has conducted collaborative research with a number of Hong Kong universities, and is currently taking an external PhD in

Information Systems at Brunel University, UK. His research interests include information systems management, medical informatics, evolving computer systems and the use of web technology, He has also served as a collaborative member of an IEE Professional Group Committee.

![](/api/attachments/9TMHFUYF/fulltext/images/1c0da419891e24974c3a75fad6bbed0b528883ffa92b5fdb6dacc2b68ded36df.jpg)

Grace Au received an undergraduate degree in management sciences, a masters degree in operational research, and a PhD in information systems from the London School of Economics, University of London, UK. She joined the Hong Kong University of Science and Technology in 1992 as an Assistant Professor in the Department of Information and Systems Management and is currently Associate Director of Public Affairs a the university. She has published in Eu-

ropean Journal of Operational Research, Journal of Organizational Computing, Journal of Electronic Commerce, Computers and Industrial Engineering, and Information Systems and Operations Research.
