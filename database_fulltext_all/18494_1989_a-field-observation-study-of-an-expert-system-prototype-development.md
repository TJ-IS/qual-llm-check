---
otero_id: 18494
otero_key: "APH2MHZJ"
title: "A field observation study of an expert system prototype development"
authors: "J. Hershauer; A. Karim; H. Owens; A. Philippakis"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90012-8"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
North-Holland
Information & Management 17 (1989) 107–116

# A Field Observation Study of an Expert System Prototype Development

J. Hershauer, A. Karim, H. Owens, A. Philippakis
Department of Decision and Information Systems, Arizona State University, Tempe, AZ 85287-4206, USA

The paper reports a cooperative effort between business practitioners and academic researchers involving development of a prototype expert system. The study traces the development process from initiation to completion and presents a number of lessons learned that can guide organizations preparing to experiment with the development of expert systems.

Keywords: Expert systems, Prototype, ES development, Industry practice, Scheduling.

James C. Hershauer is Professor of Decision & Information Systems at Arizona State University. He holds a B.S. in Engineering from Purdue University and an M.B.A. and D.B.A. from Indiana University. He has published articles on DSS, service productivity measurement, and information systems in numerous journals. Much of the service productivity work is presented in the second edition of Productivity and Quality: Measurement as a Basis for Improvement written with Everett Adam, Jr. and William Ruch.

Ahmer Karim is a doctoral student in Computer Information Systems at Arizona State University. He received a B.S. in Management Information Systems and Finance from the University of Arizona and an M.S. in Computer Information Systems from Arizona State University. His current research interests include Model Management Systems with Database and Expert System implications, and conflict resolution among multiple experts.

Heidi Owens is a doctoral student in Computer Information Systems at Arizona State University. She received a B.S. degree from Arizona State University in 1981. From 1982 through 1986, Heidi worked for two computer firms that develop popular Decision Support System packages. Her research interests include the design and development of systems that integrate data, models, and expertise, and the facilitation of knowledge integrity control within integrated systems.

Andrew S. Philippakis is Professor of Information Systems and Director of Computer Resources for the College of Business at Arizona State University. His research and teaching interests include applied AI, information management, and decision support. He received his Ph.D. degree from the University of Wisconsin, has published in both academic and professional journals and has coauthored several textbooks on computer programming.

## 1. Introduction

Expert Systems (ES) represents an emergent applied information technology. In addition to a prolific academic literature, ES is the frequent subject of publications aimed at business practitioners [e.g. 2,3,11,12,14,18]. As a new technology for the vast majority of organizations, ES is a potential component in the mix of information systems applications. Business practitioners are evaluating the feasibility of adopting the new technology and are searching for ways of introducing ES into their portfolio of technological capabilities and practices. Such an environment is very receptive to cooperative efforts between business practitioners and academic researchers.

This study is based on field observations by an academic research team that was invited to monitor the development of a prototype expert system. The paper presents a comprehensive account of all phases in ES prototype development and provides an unusual opportunity for a detailed review of issues of interest to both researchers and practitioners.

## 2. Task Overview

The prototype Expert System presented in this paper involves scheduling the distribution of irrigation water through an intricate canal system to the urban and agriculture sectors of a large desert valley. The canal system, which is supplied with water from nearby reservoirs, consists of main canals, smaller branches called laterals, and gates which are used to regulate flow of water. The system is managed by a major utility company.

The irrigation area consists of three main divisions. Each division is subdivided into a number of areas, with a total of thirty areas. The irrigation division under study is managed by a Superintendent, who has three Water Masters, four assistant Water Masters, 59 Zanjeros (local terminology for schedulers), and 11 clerks working in that division.

Water is distributed to each area by Zanjeros utilizing a manual scheduling process. The manual scheduling process begins by reviewing the prior day's scheduling reports to determine the quantity and location of water, and sorting the water orders by specific laterals. Next, the current orders for each lateral are scheduled using a sequencing and ranking process. The process requires that a Zanjero consider the interaction of numerous factors such as the attributes of the orders, the laterals, and other environmental aspects. As an example, if an order is less than six hours in duration or if the customer order is more than 48 hours old, the scheduler would assign higher priorities to these orders.

After the orders are scheduled by laterals, the scheduler determines whether there will be sufficient water for tomorrow's orders or whether more water would have to be ordered. Based on the demand, orders may be filed for scheduling on the next day. For each given order to be scheduled, all relevant information is written on the Order Schedule Report. The entire process takes from two to four hours for each of the thirty areas.

The Order Schedule Report is arranged in time sequence. Copies of the reports are given to the Water Master and the Zanjeros. The Water Master primarily uses the reports to maintain water levels in the canal by requesting more water from the reservoirs. The Zanjeros use the report in the field as a guide and timetable for adjusting gate openings at specified times. The schedule is frequently modified in the field due to physical changes in the environment or new information from customers. As an example, some customers may request an earlier shutoff of water than previously requested. Such changes are incorporated into the schedule by the Zanjero as they occur.

## 3. Project Selection

Selection of a target project is an important issue for employing a new technology. A rational selection process would require a clear statement of characteristic attributes for candidate ES projects, an exhaustive list of candidate projects, a complete evaluation of each project's suitability as an ES, and a related cost-benefit analysis. However, such a rational approach is impractical since the selection process itself would consume greater resources than the target project and its expected benefits. As our observed case shows, the selection process in practice relies on limited search and to a great extent on random factors impacting the selection process. Future research will need to provide a balance between the rationality of concepts and the circumstantiality of practices.

The client consulting division of the company's Information Systems department became aware that there had been previous attempts towards implementing a computerized water scheduling system. These attempts had utilized a ‘COBOL-based’ approach, in accordance with the standard implementation policies of the company. Due to the unique nature of the application along with other associated factors, all previous attempts had been unsuccessful. Management perceived expert systems as an alternative to the company's standard methods and recognized the water scheduling application as an opportunity to apply Expert Systems. However, other related applications methods such as decision support systems were not evaluated.

The interest in a computerized water scheduling system by irrigation division executives was the key reason for selecting this project. The application did not involve an urgent need with high expectations and the downside risk of “failure” was not particularly high. The main motivation for an expert systems approach was the fact that the majority of current Zanjeros are long-term employees with no trained and dedicated replacements clearly available. The division has experienced relatively high turnover among younger Zanjeros. Capturing the expertise of current senior Zanjeros through expert systems could preserve their knowledge base which has been developed from many years of experience. If this cannot be done through computer systems during the next five to ten years, then a potentially expensive training program will be needed. The consulting division thus chose this particular problem domain because it was a “safe” environment with available and cooperative experts and with a potential for significant long term benefits. Immediate economic benefits were not explicitly evaluated and customer and managerial complaints about water distribution were infrequent.

## 4. Development Team

Traditional IS projects follow a well established pattern in assigning and defining roles and skills for the project team: project management analysis, systems design, programming. In ES projects, tradition is nonexistent, and the new dimension of knowledge engineering raises some important issues for project team organization. Knowledge engineering has clear parallels to systems analysis, design, and programming. On the other hand, it is not clear what are the specific similarities and differences. Research is needed on defining criteria for effective assignment of roles in ES development teams. Our field observations show a structure that attempts to substitute knowledge engineering for programming.

In order to initiate this project, the information systems department formulated a four member team with the following responsibilities:

\- System analysts (2) – conducting analysis of the current system, performing knowledge acquisition or elicitation, and providing user interface.

\- Knowledge engineer/programmer - designing and coding the system in the LISP language.

\- Supervisor – coordinating the team's activities. The team was to utilize a Water Master and a Zanjero from one of the field offices and a project administrator from the user community to participate with the development team during the design, testing, and evaluation of the prototype.

## 5. Development Process

Evolutionary design methods such as prototyping are generally considered to be the appropriate ones for ES projects $[1,19]$ .

However, effective use of structured systems design in the development of an ES has also been reported $[4]$ . Organizations steeped in the tradition of structured systems life cycles need guidance from researchers in choosing an appropriate methodology for a given project. Our subject organization demonstrates a case of reluctance in giving up tradition and simultaneous awareness of the need for a changed approach.

The company's IS department employs a standard five-phase system development life cycle. For this project, the team employed an abbreviated form of their standard life cycle consisting of four phases: Initial survey, Analysis, Design, Program and Test phase.

The purpose of the initial survey stage was to conduct a feasibility study of the entire water scheduling project with emphasis on the feasibility of the prototype application. The analysis phase would study the water distribution network and would document the current scheduling system. The logical and physical design phases were to be combined into one design task. Similarly, the program development and system test stages were to be consolidated into one programming task.

## 6. Survey Phase

In the survey stage, the primary focus was the feasibility of the water scheduling system, with emphasis on the ‘prototypical’ nature of the project. The key areas of this phase included the objective, the scope, and the work plan of the project.

The initial analysis of the project by the development team revealed an application which dealt with both quantitative as well as qualitative information and which was seen as being more ‘knowledge-intensive’ as opposed to ‘data-intensive’. Therefore, the decision was made to use an expert systems approach.

The development team chose one of the thirty water distribution areas as the scope of the prototype, and identified four primary objectives of the water scheduling prototype system:

\- To determine the feasibility of the system design.

\- To aid in the determination of the scope of the future production system.

\- To provide assistance in estimating the costs and time for the development and installation of a production scheduling system.

To provide a benchmark for determining the computer resource usage for a production system on a mainframe.

The team viewed the total system as a decision-intensive application comprised of three separate components: the expert system, the scheduler, and the water distribution network. Dividing the system into the three components was seen as facilitating the design process of the system. The scheduling component was viewed by the development team as being different from the ‘intelligent’ subsystem, which was to incorporate the expertise necessary to evaluate the schedule. The third component was regarded as representing the model of the water distribution system and was to encompass the physical and mathematical mapping of the area.

This phase of the project also outlined the operating environment of the prototype and selected LISP as the expert system design language. The primary reason for this selection was the lack of alternative resources supported by the company, and the familiarity with this language by the knowledge engineer. Applying other knowledge engineering languages or expert system shells would have involved acquiring resources not currently available in the department.

The survey stage also outlined the work plan for the analysis phase and presented preliminary cost estimates for the prototype system and the full scale production system. The preliminary cost estimates for the prototype were 730 labor hours at a cost of \$21,900. In terms of the full scale production system, to be implemented based on feasibility of the prototype, the development team's preliminary cost estimate was 4,018 labor hours at a cost of \$162,000.

## 7. Analysis Phase

Knowledge elicitation can be viewed as a counterpart to the information requirements phase of traditional IS projects. However, there are some important differences, as illustrated in our field observations. First of all, by its very nature, expert knowledge is difficult to make explicit. Experts do not tend to follow standardized formal procedures, and even when they do so, they may not be aware of their practices.

Expertise may not reside in a single source. When multiple experts are involved, as is the case with the large number of Zanjeros in our subject case, their specific individual expertise may vary because of variations in the physical and operational characteristics of each irrigation area. In addition, the relevant expertise may be partitioned among multiple experts and across different organizational levels. Personnel at the Water Master level have policy expertise, in contrast to Zanjeros who have practitioner expertise. At the present time, there is no theoretical base for how to conduct the analysis phase of an ES project involving distributed expertise. In particular, capturing expertise distributed across organizational levels presents a promising research area.

The analysis phase of the project involved investigation of the current system, capturing the physical mapping of the water distribution network, and eliciting knowledge from the experts.

Investigation of the current system involved individual interviews with Zanjeros regarding their functions and duties in the field and in the office. In addition, the team attended Zanjero training classes offered for new Zanjero recruits. Information gathered during the investigation phase was used to formulate a logical mapping of the operational system using data flow and context diagrams. Maps and other documentation were used in developing a model of the water distribution network (size and other characteristics of main canals, laterals, and gates).

The next step of the analysis phase involved elicitation of knowledge from experts. Initially, the team used a single expert who was told that the project involved the design of a computer tool to assist with the scheduling task. No attempt was made to communicate the specific meaning of “expert systems”.

The knowledge elicitation task was conducted through interviews by the two analyst members of the team. The task was viewed to be similar to information requirements definition in traditional IS tasks. The knowledge engineer/programmer was to be involved primarily during the design stage. The knowledge elicitation process involved a series of interviews with the expert. By utilizing examples and walk-throughs of schedules, the analysts tried to capture the various heuristics and intricacies of the scheduling process.

Two problems were encountered that made formulating rules difficult. The first problem was the ambiguity involved in capturing qualitative terms. For example, terms such as “a lot of water”, “enough water” or “bigger/smaller” often came up in the interview and were difficult to interpret. This problem was attributed to the fuzziness of the knowledge. The second problem was the variability of knowledge that results from the uniqueness of canals, laterals, and customer needs. Such problems made the formulation of rules very open to interpretation. The analysts were involved not only in the task of gathering data but also interpreting it. Hence, the analysts acted as intermediaries between the expert and the knowledge engineer. During the translation process (expert → analysts → knowledge engineer), the analysts took on the role of the expert and interpreted the knowledge they received from the expert to the knowledge engineer.

Although initially a single expert was utilized to extract knowledge, the later stages of the process saw the involvement of the managers and policy makers. The involvement of the expert's superiors resulted in some contradictory information. The assistant Water Master, who reviewed the rules extracted from the initial expert, highlighted various rules which were not in accordance with the standard policies prescribed by management. In order to resolve this conflict, the development team decided that any revisions made by management would supersede any inconsistencies. This decision was made because there were certain limitations in having access to the original expert, and the fact that the development team wanted to gain the support of management.

The team also performed validation of rules extracted from the expert. Initially, when the team utilized just a single expert, the analysts presented the expert with the rules for his verification. Later on, when the assistant Water Master revised some of the rules, these rules were not presented back to the original expert. Instead, a management group was assigned the responsibility for verifying rules. Although there were some inconsistencies, they were not seen as significantly affecting the credibility of the knowledge base.

## 8. Design Phase

Traditional IS projects consider the design phase as an opportunity for developing an improved system. Traditional ES projects place the emphasis on capturing the expert's system as "intact" as possible. Our case history demonstrates an interesting mix of both approaches. The development team began with the implicit assumption that expert systems technology would be used to improve more than replicate the scheduling task. Given the environment, it is not clear that this was not an appropriate design objective. Expertise was distributed across multiple experts and across different organizational levels. It is an obvious research need to study appropriate ES design objectives given different organizational settings.

Once the rules were validated by the management group, the analysts represented them in a 'condition-action' format to facilitate the programming task of the knowledge engineer. In this phase of the project, it also became evident that the logical representation of data (data flow diagrams and context charts) could not be utilized by the knowledge engineer in the physical design of the prototype. The rules and procedures captured by the analysts were used as an equivalent substitute for the diagrams. On the other hand, the physical and mathematical mapping of the area were easily utilized by the knowledge engineer in order to represent the water distribution network. In addition, during this phase, it became evident that the main emphasis was being placed on the expert component rather than the scheduler subsystem, contrary to what was anticipated earlier. The knowledge engineer discovered that it was easier to design control into intelligent subsystem, which amounted to a rule-based system, than into the scheduler component. Although, the initial configuration was retained throughout the development of the prototype, the knowledge engineer saw the role of the expert system and the scheduler components as converging together, and noted that the three components are more overlapping than initially anticipated.

Overall, the most difficult problem encountered in the design of the prototype was the interaction of the various rules in the knowledge base. As an example, when a new rule was introduced to the knowledge base, it was not clear just how it would affect the results of the other rules. In addition, many of the rules presented by the Zanjeros were vague, and attempts to formalize them were difficult as they generated various exceptions which were themselves difficult to formalize. As a viable solution to this problem, to knowledge engineer decided to dispense with the exceptions and retain the general rules. These rules applied to a majority of the cases, but did not cover all the possible exceptions. The designers felt that the few exceptions should be left for the Zanjeros.

Moreover, the rules presented by the analysts were, under certain circumstances, modified by the knowledge engineer during the coding process. These modifications resulted due to the interpretation of the rules by the knowledge engineer or due to the underlying limitation of the programming environment.

During the design phase, the analysts were involved in the design of a human interface for the system, using DBase III + . The main purpose of this interface was to provide a front-end component for the LISP environment, which would facilitate communication between the user and the prototype. One of the advantages of this component was the ease of use in generating screens and reports. These features are not easily facilitated in the LISP environment. The user-interface presented no major problems for the developers.

## 9. Testing Phase

In this phase of the project, the prototype was utilized by the assistant Water Master to generate water schedules for customer requests. This system was run with various sets of possible inputs in order to simulate a typical scheduling process. Unfortunately, the results generated by the prototype had various shortcomings and were deemed impractical by the schedulers. One of the problems was that certain rules not captured by the system, and in other cases the generated results did not make practical sense. Primarily, a major problem arose when the development team encountered contradictions in terms of how they had rationalized the scheduling procedure and the way the schedulers were actually performing the operation. An actual simulation of the scheduling process revealed various rules and exceptions which did not arise in trial runs during the analysis phase.

## 10. Findings

The prototype was completed in August 1987, approximately one year from the time of its initiation. The water scheduling system is currently installed on an IBM PC-AT at one of the field offices. The development team has spent several months on the system rectifying problems with the prototype, enhancing the rule base of the expert system, and bringing the prototype to a productive level. In this year and a half into the prototype life cycle, the development team has acquired valuable information concerning the expert system and its associated environment. In order to look at some of the findings of the development team, it would be beneficial to look at the results of the development process as it relates to the original objectives (outlined earlier). Following is an analysis of the original objectives based on the results, as perceived by the development team:

## 10.1. Feasibility of the system design

The finished prototype deviated from the original system design (the expert system and the intelligent scheduler were combined into a single entity). In addition, the team discovered that the 'fine-tuning' of the rules was not as flexible as imagined earlier, and in some cases, resulted in unforeseen side-effects. Difficulties were also encountered due to the lack of expertise in terms of the design tool, the LISP environment.

## 10.2. Implications on the future production system

In terms of a future production system, the development team realized the importance of interaction with the Water Accounting System (to efficiently capture the customer water orders, and to track water usage) and Transmission (in terms of water called for at a predetermined time for subdivision use and ordered water to start within the next 24 hour schedule). Moreover, the development experience also highlighted the importance of environmental factors such as dry-ups, demoss, and other factors, for the implementation of a successful production system.

## 10.3. Impact on cost and time estimates for a future production system

The prototype required 72% more effort to complete than the original estimate. Based on the experience, the original forecasts for a production system was revised from 4,018 labor hours at a cost of \$162,000 to 9,033 labor hours at a cost \$364,200. In order to put these numbers in proper perspective, we point out that there were 20 target areas in the total water scheduling system. A production system could involve twenty distinct expert systems, or one centralized large expert system serving all 20 areas. Viewed in that light, the \$364,200 number may be a conservative estimate.

## 10.4. Implications regarding computer resource usage for a system on a mainframe

After the implementation of the prototype on a microcomputer, the development team concluded the system to be CPU intensive during the scheduling process, and underutilized during nonscheduling tasks. It was recommended that a production system should reside either on several computers (in order to provide the necessary backups) or in one computer with redundant configuration.

## 11. Recommendation of the Development Team

Based on the one and a half year experience, the development team has recommended not to proceed with a production water scheduling system utilizing a development technology similar to the prototype. In order to explore other options, the development team has presented two alternatives.

The first alternative considers utilizing an expert system as a tool for providing scheduling advice and/or facilitating the training process of a new scheduler. In essence, the system would take on an advisory role with the Zanjero performing the actual scheduling. The system could also aid the new recruits in training classes, by providing guidance through the captured expertise.

The other alternative also requires the Zanjero to perform the actual scheduling (in terms of who will receive water); however, an accompanying system would fill-in other necessary details such as times, optimal path, and the amount of water needed for each delivery. Hence, the system would alleviate some of the cumbersome tasks associated with scheduling.

## 12. Lessons Learned

Based on the field observation study, we propose a number of points that summarize research observations and can also act as a guide to organizations considering the initiation of expert systems projects.

## 12.1. Project Definition

In the observed case the project had dual purposes: familiarization with the new technology via building a prototype system, and ultimate development of a final production system. The new technology casts a certain aura of “forgiveness” and it is easy to receive project approval without the normal level of hard-nosed justification. Ambiguous project definition can lead to project failure time and cost overruns, and inconclusive results. The project definition should be expressed in terms of functional objectives, or it should be considered an educational skill development experience and treated as such.

## 12.2. Project Evaluation: Specification of Success Measures

New technology can be invoked as a reason for evasive measures of success and failure. Like any other computer-based project, it is important to define in advance the measures that will be used to evaluate the project. If the purpose is the construction of a prototype, then there should be explicit measures as to what will constitute a successful prototype.

## 12.3. Human Resources

It is important to make certain that appropriate skills are available in advance. In our case study, the knowledge engineering role was played by a programmer/analyst whose expert systems preparation consisted of one college-level course in LISP programming. Specialized training through suitable seminars or use of outside consultants are recommended paths to developing the required level of basic skills.

The team approach is useful provided that each team member makes a distinct contribution and that the team is representative of both the technical and functional areas. In our case, the team consisted of one inexperienced knowledge engineer and two traditional system analyst/programmers working in virtual isolation from the personnel in the target functional application area.

In fact, the analysts actually served as a filter between the expert and the knowledge engineer and may have hampered the transfer of expertise into the system.

## 12.4. Emulation vs. Design

The classic notion of an expert system involves emulation of the existing expertise of an expert. Knowledge engineering, is a relatively passive role in eliciting and encoding knowledge from an expert. In contrast, conventional information system projects are often undertaken with the explicit purpose of designing them to be improved versions of existing systems. Traditional systems analysts are assumed to be capable of using their skills to design new systems. In our case, the project team was not clear of its role with respect to the above distinction between systems design and knowledge engineering. As a result, they tended to assume the role of traditional systems design and operated under the belief that once they developed a model, the model would work well even if it did not emulate the source expertise. Frequently, however, they reverted to a more passive role. The ambiguity remained throughout the project.

We recommend that the emulation versus design issue should be given advance consideration. If there is a source of expertise that cannot benefit from the project team's skills, then the emphasis should be on emulation. If, on the other hand, there is reason to believe that the expert is not all that expert or multiple sources of expertise exist, then the project team may take it upon itself to design a new system that could be used to build expertise. (Such a system would not be, strictly speaking, an “expert system”, but a “knowledge based” system incorporating artificial intelligence technologies with traditional systems methodologies).

## 12.5. Identification of Knowledge Sources

Our study involved a case where expert knowledge was diffused into several organizational layers and across several peer experts. Policy-level knowledge existed at the Water Master level which was separated from the operational knowledge of the Lead Zanjero by the intermediate level of the Assistant Water Master. In addition, there were a large number of Lead Zanjeros who did not have identical levels of expertise. Issues, such as whether there is indeed a ‘single expert’, whether there are several different approaches to the problem, and whether these approaches are equally valid need to be evaluated [15]. For our example, the development team needed to address questions like the consistency among the different Zanjeros, correlation of a Zanjero’s expertise with a given area, and the impact of involvement of management during the elicitation phase.

The subject case is representative of the frequent distribution of expertise in the organization. Multiple expert and multiple organizational levels add to an already difficult situation. Therefore, it is important to identify in advance the source(s) of expertise and to be cautious about inexperienced project teams taking on projects with compounded difficulty.

## 12.6. Modeling Issues

An expert system involves construction of a model of a real world situation. Like any model, there are the conflicting issues of detail and complexity versus abstraction and simplicity. Knowledge based systems entail substantial complexity due to their technology. If, in addition, there is structural complexity in the modeled task, the difficulty is further increased. In our case, modeling the water delivery system proved to be difficult. The physical system could be modeled at a high level of abstraction (main canals, laterals, gates), or it could be described in immense detail (for instance, modeling every linear foot of waterway as a distinct component). Initial projects for inexperienced knowledge engineering teams should avoid projects involving difficult modeling situations.

## 12.7. Knowledge Elicitation / Acquisition

With respect to knowledge elicitation/acquisition techniques, the development team had selected the interviewing process for eliciting knowledge. Research in the field of knowledge elicitation has identified several problems in this most common fact-finding method. Hart [8] views the main problem to be lack of overall structure and asserts that unless a recognized methodology is developed, the captured information is difficult to analyze. She proposes techniques such as protocol analysis, induction, and repertory grid approach as other viable options. The important lesson is to consider alternatives before starting the process.

## 12.8. Tool Selection

Despite the recency of expert systems technology, there is a wide range of conceptual and software tools available. In the conceptual area, knowledge representation schemes include rules, logic, semantic nets, and frames. In the software area, languages such as Lisp, Prolog, and Ops5 are competing with a number of proprietary “shells”. It is obvious that the right fit between the nature of the task and the available tools needs to be considered. This was not done by the project team and thus LISP was chosen for the wrong reasons.

The development team utilized Microsoft LISP because the programmer/knowledge engineer had background in this language and the language was easily accessible to the group. Although this language provides flexibility to the expert system builder, there are certain reservations in using it. As an example, it fails to provide guidance in representing knowledge or mechanisms for accessing the knowledge base $[19]$ . Some of the commercial knowledge engineering languages are complete tools for expert system development combining powerful languages with sophisticated support environments.

## 12.9. Systems Development Process

Although, there is no standard approach for developing an expert system, researchers recommend methodologies which deviate from the traditional life cycle approach $[7,9,19]$ . One of the most commonly cited approaches consists of five interdependent, overlapping phases: identification, conceptualization, formalization, implementation, and testing $[19]$ . It is not clear that a successful expert system can be built using the traditional life cycle.

## 12.10. Validation

Just as with any software development project, validation of expert systems is an important issue. There are inherent difficulties in the process of ascertaining that an expert system conforms to the source expertise. Such difficulties are compounded when the project definition and its objectives are ambiguous, the emulate vs. design distinction is not clear, and the source of expertise is diffused across several persons in the organization. When such conditions prevail, it is likely that the project will be very difficult to validate and its acceptance by the end-users is unlikely.

The validation and evaluation of the prototype was an important phase of the project, which needed to be carefully considered. The development team made attempts at verifying the rules captured from the knowledge expert, but the involvement of management and other limitations restricted this process. Moreover, the methodology did not specify any structured iterative process for incorporating updates and modifications in the normal flow of the development process. In the expert system literature, there is very little work on this issue. Recently, researchers $[5,6,10,13,16,17]$ have acknowledged this problem and have attempted to present some alternatives.

## 13. Conclusions and Future Implications

Presently, in the expert systems field there are various areas where academicians and researchers are concentrating their efforts. As there is no one ‘best’ approach for building an expert system, eliciting knowledge, representing knowledge, selecting a language, or following a development cycle, the information gained from reviewing and analyzing a development team’s activities can be extremely valuable.

The initial experience of the prototype project team is not really surprising from a software development view. In retrospect, the water scheduling prototype system is representative of many ‘expert system’ projects currently floundering in businesses. The important issue is not whether these projects succeed or fail, but rather whether or not there is an emerging realization, from practitioners and researchers, about what an expert system application encompasses, and how it needs to be approached. By merging the experiences of researchers and practitioners, we can attempt to alleviate some of the gaps in this field. Hence, by learning from previous mistakes and experiences, future projects can be approached from a more enlightened perspective.

## References

[1] Bobrow, Daniel G., Mittal, Sanjay, and Stefik, Mark. "Expert Systems: Perils and Promise," Communications of the ACM, Vol. 29, No. 9, Sept 1986, pp. 880–894.

[2] Business Week, “Office Automation: Making It Pay Off,” No. 3020, October 12, 1987, pp. 134–144.

[3] Computerworld, “Interview-Watch the Rabbits,” Vol. XXI, No. 47, Nov. 23, 1987, pp. 59–61.

[4] DeSalvo, Daniel A., Glamm, Amy E., and Liebowitz, Jay, "Structured Design of an Expert System Prototype at the National Archives," In Barry G. Silverman, editor, Expert Systems for Business, Reading, MA, Addison-Wesley, 1987, pp. 40–77.

[5] Gaschnig, John, Klahr, Philip, Pople, Harry, Shortliffe, Edward, and Terry, Allan, “Evaluation of Expert Systems: Issues and Case Studied,” in Hayes-Roth, Frederick, Waterman, Donald, and Lenat, Douglas, (editors) Building Expert Systems, Reading, Massachusetts, Addison-Wesley, 1983, pp. 241–280.

[6] Goul, Michael, Moffitt, Kathleen, O'Leary, Timothy, and Radwan, Essam, "The Art of Validating Expert Systems: The Project SCII Experience," Working Paper, Technical Report #87-2, Arizona State University, Tempe, AZ., 1987.

[7] Goul, M.&F. Tonge., “Project IPMA: Applying Decision Support System Design Principles to Building Expert-Based Systems.” Decision Sciences, Vol. 18, No. 3, Summer 1987, pp. 448–467.

[8] Hart. Anna., “Knowledge Elicitation: Issues and Methods,” Computer Aided Design. Vol. 17, No. 9, November 1985.

[9] Hayward, S., “A Structured Development Methodology for Expert Systems,” IJCAI 1986, KBS 86, pp. 195–203.

[10] Lane, N.E., “Global Issues in Evaluation of Expert Systems,” IEEE Int'l Conference on Systems, Man, and Cybernetics, Vol. 1, October 1986, pp. 121–125.

[11] Leonard-Barton, Dorothy, “The Case for Integrative Innovation: An Expert System at Digital,” Sloan Management Review, Vol. 24, No. 2, Fall 1987, pp. 7–13.

[12] Leonard-Barton, Dorothy, and Sviokla, John J. “Putting Expert Systems to Work,” Harvard Business Review, Vol. 66, No. 2, March–April 1988, pp. 91–98.

[13] Liebowitz, J., “Useful Approach for Evaluating Expert Systems,” Expert Systems, April 1986, Vol. 3, No. 2, pp. 86–96.

[14] Luconi, Fred L., Malone, Thomas W., and Scott Morton, Michael S., “Expert Systems: The Next Challenge for Management,” Sloan Management Review, Vol. 27, No. 4, Summer 1986, pp. 3–14.

[15] Mittal, S.&C.L. Dym., “Knowledge Acquisition from Multiple Experts”, The AI Magazine, Summer 1985, pp. 32–36.

[16] O'Leary, D.E., "Validation of Expert Systems--With Applications to Auditing and Accounting Expert Systems," Decision Sciences, Vol. 18, No. 3, Summer 1987, pp. 468–486.

[17] St. Johanser J.T.&Harbidge R.M., "Validating Expert Systems: Problems and Solutions in Practice," IJCAI 1986, KBS 86, pp. 215–219.

[18] Sviokla, John J., “Business Implications of Knowledge-Based Systems. Part I,” Data Base, Vol. 17, No. 4, 1986, pp. 5–19.

[19] Waterman, D.L., A Guide to Expert Systems, Reading, Massachusetts, Addison-Wesley, 1986.
