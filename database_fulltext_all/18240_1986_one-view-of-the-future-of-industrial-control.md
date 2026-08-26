---
otero_id: 18240
otero_key: "GJRHB87R"
title: "One view of the future of industrial control"
authors: "Theodore J Williams"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90042-x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# One View of the Future of Industrial Control

Theodore J. Williams

Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana 47907, USA

Computer based, industrial control systems will be the medium for all plant control requirements in the future. This paper further foresees that such control systems will be based upon generic, hierarchical architectural forms which can thus apply to all types of industries. These architectures will be designed to achieve the maximum synergism between the computer system and the coexisting management structure of the plant. This paper outlines the requirements for and the probable form of such computer based control systems.

Keywords: Industrial control systems, Computer control, Hierarchical computer systems, Management structures, Data base requirements, Control system requirements, Control enforcement, Production scheduling, Reliability and availability.

![](/api/attachments/GJRHB87R/fulltext/images/56f4614d93d64fb03a85981a19c108f5e855ce228335fa68caf1d1bcec5e7c27.jpg)

Dr. Theodore J. Williams is Professor of Engineering and Director of the Purdue Laboratory for Applied Industrial Control at Purdue University, West Lafayette, Indiana. He received the B.S., M.S., and Ph.D. degrees in chemical engineering from Pennsylvania State University and the M.S. degree in electrical engineering from Ohio State University.

He has served two terms as President of the American Federation for Information Processing Societies (AFIPS) (1976-78). He is a former president of the American Automatic Control Council (AACC) (1965-67), and a Past President of the Instrument Society of America (ISA) (1969).

In 1975, Professor Williams was recipient of the Sir Harold Hartley Silver Medal awarded by the Institute of Measurement and Control in London, England, the First American and the first non-Englishman to achieve this honor.

Dr. Williams is a Fellow of the American Institute of Chemical Engineers, the Instrument Society of America, the American Association for the Advancement of Science, the American Institute of Chemists and the Institute of Measurement and Control (London). He is an Honorary Life Member of the Society for Computer Simulation. He is also a senior member of the IEEE, and a member of the ACS, the ASEE, etc.

## 1. Introduction

Four factors have combined to make overall, hierarchical distributed computer control systems a present day fact, as well as the most likely future plant management and control system: (1) The development of microcomputer based, digital, primary control elements along with high speed, serial communications systems; (2) The potential of ADA as an overall standard process control language; (3) The rapid reduction in computing costs; and (4) The associated developments in data-base management techniques. In addition, several recent studies and applications have shown that a generalized system can probably be developed and used for most, if not all, industries. This should help to reduce the systems development and installation costs of these very large systems.

The place of man, whether plant operator, supervisor, manager or engineer, in a plant controlled by such a computer system, is central to the design and operation of any such system. This paper presents one view of how the human will best integrate with such a system to achieve the best synergism.

Automatic control of any large modern industrial plant, whether by computer-based or conventional means, involves the extensive monitoring of a large number of process variables under a wide range of plant dynamics. It requires the development of a large number of quite complex and often nonlinear relationships for the translation of these variables into the required control correction commands. Finally, these control corrections must be transmitted to a large set of scattered actuation mechanisms of various types which, because of the nature of the manufacturing processes, may control the direction of the expenditure of very large amounts of material and energy. Meanwhile plant personnel must be kept aware of the current status of the plant and its processes. Today the minicomputer is being widely used for these functions for single industrial processes or small parts of larger units. Microprocessors and microcomputers have also recently been applied in many similar applications, though usually on a smaller scale.

Such an industrial plant is also faced with the continual problem of adjusting its schedule to match customer needs, while maintaining high plant productivity and lowest practical costs. This latter problem is now mainly handled through a manual, computer-aided, production control system with a sufficient but not excessive in-process and finished goods inventory. Nevertheless, there is a decided trend today to automate these functions and eventual full automation is in sight.

Thus automation of an industrial plant becomes the managing of its information systems to assure that the necessary data is collected and used wherever it can enhance the operation.

It has been repeatedly shown that a major benefit of computer control systems has been the adoption of the role of the “control systems enforcer.” In this, the control computer has the main task of continually checking that the control system equipment is actually keeping the units of the plant production system operating at some optimal level; i.e., to ensure that the optimal set points are being maintained, etc. Often the tasks carried out by these control systems have replaced those that a skilled and attentive operator could have readily done. However, the human operator cannot maintain the same attentiveness as the computer over the long run and thus the computer is to be preferred.

All of these factors and capabilities must be factored into the design and operation of the control system, including the plant's requirements for maximum productivity and minimum energy usage. As the overall requirements become more complex, more and more sophisticated and capable control systems are necessary. To achieve these requirements, the field must gravitate more and more toward digital computer-based systems. The resulting systems must have the following capabilities:

1. Tight control of each operating unit to assure that it is operating at its maximum efficiency of energy utilization and/or of production capability based upon the required production level.

This control reacts also to any internal emergencies.

2. Supervisory and coordinating systems which determine and set the local production level between inventory locations, optimizing unit operations. This assures that no unit is exceeding the area level and using excess energy or raw materials. It responds to the emergencies or upsets in any unit under its control by shutting it down or reducing its output.

3. Overall production control systems capable of carrying out the scheduling function for the entire plant - from customer order or management decision to producing the required products at the optimum combination of time, energy, and raw materials expressed as cost functions.

4. Methods of assuring the overall reliability and availability of the total control system through fault detection, fault tolerance, redundancy and other applicable techniques built into the system.

Because of the ever-widening scope of authority of each of the first three requirements, they can best be carried out by the successively higher levels of a hierarchic control structure. Also it appears that some sort of distributed computational capability should be the structure for the control system. It appears that mini- and micro-computers will effectively handle Requirements 1 and 2 and will be heavily involved in Requirement 4. However, the complexity of Requirement 3 will require a much larger machine at present.

## 2. The Probable Form of the Overall Plant Control System of the Future - the Computerized Hierarchy

Figures 1 and 2 lay out one possible form of this distributed, hierarchical computer control system for overall plant automation. Figure 1 uses the nomenclature common to the continuous process industries, while Figure 2 presents the computer integrated manufacturing system (CIMS) commonly used in discrete manufacturing industries. The levels here are “functional” levels. It is our thesis that the two diagrams are exactly functionally equivalent.

In the context of large industrial plants, or of a centralized company, the tasks that would be carried out at each level of the hierarchy can be readily described and have been extensively pub-

I. Production Scheduling
II. Control Enforcement
III. Plant Coordination and Operational Data Reporting
IV. System Reliability and Availability Assurance

![](/api/attachments/GJRHB87R/fulltext/images/71046a55b2e7459ec74265e584e11319c94877fa1e07c3534df77f7dc6362324.jpg)  
Fig. 1. Assumed Hierarchical Computer Control Structure for an Industrial Plant (Continuous Process such as Petrochemicals).

lished (14). These tasks are readily subdivided into the short list of duties of control computer systems shown in Table 1.

Such lists can outline the tasks which must be carried out in any industrial plant, particularly at

Table 1
Summary of Duties of Control Computer Systems the upper levels of the hierarchy [22,23]. Details of how these operations are actually carried out may vary drastically, particularly at the lowest levels, because of the nature of the process being controlled.

Thus it is our contention that the major differences in the control systems are in the details of the dynamic control technologies used at Level 1 and the details of the mathematical models used for optimization at Level 2. Sensing and communications techniques are the same in both systems. Thus the overall duties of the hierarchy computer system will be as shown in Figure 3 [11,14,15,18].

![](/api/attachments/GJRHB87R/fulltext/images/b7cbe734ce01652116d0a66fc63656cbbbfc4bbabbb990826b748f7ea7767b2b.jpg)  
Fig. 2. Assumed Physical Hierarchy Computer System Structure for a Large Discrete Manufacturing Complex (Computer Integrated Manufacturing System (CIMS)).

## 3. Personnel in the Plant of the Future

The place of the plant operator, the supervisor, and the engineer in a future plant is a vital part of the study of any such system. In discussing the probable place of operational personnel in the industrial plant of the future, there are two major considerations: The first is that of the “quality of working life” of these personnel: they must be relieved of dirty, undesirable, and monotonous tasks; their health and safety must be protected; and their salary high enough to assure a certain standard of living. The second consideration is economic; the relative capital and operating cost of the devices which can be used for carrying out the plant functions in competition with operating personnel. At the plant floor level, ad hoc decisions can be made for each situation as it arises, since the system can operate regardless of which decision is made on its production interface (men or machines) provided the necessary communications is established and maintained.

At the upper levels of the hierarchy there is a natural allocation of tasks among plant and company supervisory personnel as noted in Figure 4. This distribution of tasks corresponds to that in the hierarchical computer system as shown in Figure 5 [3]. Thus a one-to-one synergism can exist between plant production supervisory personnel and the computer control system operating the plant.

![](/api/attachments/GJRHB87R/fulltext/images/b260a67cbd94ee6873ab791cbd0ad4ac68aabfcb5ab3bc9b1faa68a49434034a.jpg)  
Fig. 3. Definition of the Real Tasks of the Hierarchy Computer Control System.

## 4. The Overall Industrial Plant Computer Control System of the Future – a Summary

In outlining the basic control system of the plant of the future, we see a continued utilization of a set of isolated functions at the lower levels of the hierarchy carried out by small and relatively inexpensive computer systems. These will be highly redundant to preserve the integrity of the control system during the possible failure of any control unit. Fault detection and fault tolerant operational techniques will be built in to assure the highest reliability and availability [16]. Their work will be coordinated by a set of successively higher level, and probably larger, computers connected together and to remote computers by a communications system [8,12].

A large industrial plant will thus need a system architecture that incorporates several small computers for control and monitoring functions in each operating area and supervisory computers controlling each overall process unit system and performing the support and maintenance. The supervisory level systems are then controlled by higher level area systems and the overall scheduling system $[1,4,5,6,9,10,13]$ .

![](/api/attachments/GJRHB87R/fulltext/images/e1df3a0fa0a7051a2bf4acc03ab18993dad617d4b04f95cf6facb0ce811899cf.jpg)  
Fig. 4. Personnel Task Hierarchy in a Large Manufacturing Plant.

There are two major reasons for this structure. The first derives from the one-for-one relationship between the organizational structure and the computer system. The second can be expressed as follows: The true overall plant control system must be a hierarchy in which the power resides in the upper levels and is delegated to the lower levels. Also all intermediate levels have access to all information sent to neighboring units, which is also shared with upper level systems. Finally all lower level units will be distributed in relation to the plant production units as noted below.

Any example can be divided into several areas of activity centered about the manufacturing processes and their related raw material and product inventories and their utility suppliers. Because of the physical size of these processes in large plants and the required space for the related inventories, these process areas are often far apart. The architecture of the distributed control system and the physical location of its parts will be fixed by the actual layout of the industrial plant, rather than the control functions carried out on a particular computer or of its capabilities.

![](/api/attachments/GJRHB87R/fulltext/images/1523352d93d6c8c8eaf65a949423714187f52d80a183f518508311cd1885d240.jpg)  
Fig. 5. Plant Operational Management Hierarchical Structure to Match the Computer Hierarchy of Figure 1.

## 5. The Management Interface

Figure 6 outlines the communications aspects of the upper levels of the hierarchy. Level 4A is the production scheduling level. In the case of the steel mill hierarchical system this would consist of two to three very large computers because of the complexity of the scheduling task.

The system is also responsible for maintaining the Current Production Status Files (Figure 7) in a large data base. This data base for the large steel mill is estimated at 20–40 GigaBytes. All management and staff functions interface to the plant production systems through these data. They may only read and cannot write; the production scheduling computer system has the only writing ability.

## 6. Factors that Influence the System of the Future

In addition to the factors already discussed above there are several other ergonomic and technological factors whose rate of development will affect the way that hierarchical computer control systems are designed, installed and used in the future:

![](/api/attachments/GJRHB87R/fulltext/images/5604a07d28502f2d10286c23a971222f5faf8cb2863cbadb9caa8a69b1378bb0.jpg)  
Fig. 6. Overall Plant Production Control System.

1. Technologically, personnel activities should be confined to:

Handling of all plant emergencies and other unexpected occurrences;

Management of the operation of the computer and other plant equipment; and

Removal, replacement and repair of any components which have failed since the last overhaul. Personnel would thus become supervisors and maintainers of the production equipment rather than direct participants in its operation.

However, legal and social pressure may require that a person be “in charge” of the operational system. This can greatly impact the numbers, appearance and use of the control rooms associated with the computer system.

2. We should not expect any general solution for the fields of artificial speech recognition or artificial vision in the next two decades. Thus we should expect no immediate breakthrough in the artificial intelligence field which will have a major impact on the industrial automation field (17,21). Therefore voice communication with automated systems in the near future will be confined to sophisticated “single word/single speaker” vocabularies and will continue to compete directly with today’s man/machine interface techniques.

3. When finally developed expert systems could be used as repositories of current knowledge necessary for a particular function, such as the diagnosis and repair of a particular device or system. However, they will probably not become overall collections of all pertinent facts on a system from which entirely new inferences and relationships will be generated by the computer system, as is often predicted today.

![](/api/attachments/GJRHB87R/fulltext/images/28c616be7372971f8f90f6a7b4229f20679879636233386ed7fc2382c3b78d17.jpg)  
Fig. 7. Non-Operational Contact with Hierarchy Computer Control System (Level 4B).

Expert systems are showing much promise in the areas of project planning and may become very important adjuncts to the production scheduling task.

4. The overall hierarchical computer control system need not be installed by a user company all at one time. Provided a system design is completed at the start of the project specifying the complete plans for the final full system, component units may be installed as personnel availability, funding or appropriate equipment procurement permits. But all such units of the system must fit into the overall system as planned.

## 7. When?

This discussion would not be complete without some prediction of the progress towards the goals. However, new techniques, while desirable and welcomed, are not necessary for the attainment of the goals.

The analysis then turns on a set of social, economic and psychological issues:

1. When will sufficient numbers of management personnel see the need for these systems and require their development, while also developing the mathematical models, the advanced control applications and the computer programs which make them possible?

2. How soon can suitable standards be evolved and promulgated? Can their use be required in order to reduce the need for personnel to keep on redeveloping the models, the control applications and the computer programs which would otherwise be necessary for each new installation if standard reusable technology were not available?

3. How soon can sufficient, well-trained engineering personnel be available to do the necessary design and production control work?

4. How will the nation's economic conditions and the availability of capital at appropriate interest rates affect the rate of installation of these systems?

It normally takes several years to promulgate an international standard, though “de facto” standards established by a dominate company can be faster. Enforcement of their use is somewhat difficult, however, due to the wish of all vendors to exert commercial advantage, however small.

It will also take several years for the planning, development, engineering, production, installation and commissioning of a system such as this. Personnel training, mathematical modelling and advanced control application planning can take place concurrently.

Thus, the author foresees that the rest of the Eighties and perhaps all the Nineties will be needed to attain a large fraction of the proposed plant automation systems in most industries.

## 8. Conclusions

1. The major deterrents to progress in the industrial automation field are not technological. They are:

a. A lack of suitable standards for communications systems, for programming languages, and for data base management;

b. A lack of sufficiently generic and accurate mathematical models for our pertinent physical and chemical production processes; and

c. A very severe shortage of qualified personnel and other resources to carry out the engineering and programming of the systems.

2. Because of the above deterrents we cannot immediately take advantage of our available technology to achieve what is currently possible for the enhancement of our plants' production potentials.

3. Much stronger management support of the potential applications of the industrial automation field as recipients of the available company resources is a necessary condition for the solution of the deterrents to rapid progress.

## References

[1] Annon., Outline of Computerization in Kawasaki Steel Corp, Kawasaki Steel Corporation, Kobi, Japan (August 1, 1974).

[2] The Automation Research Council, A National Research Plan for Automation, Reports 1 and 2A, May 1974 and Report 8, March 1978, American Control Council, Holmdel, New Jersey.

[3] Denzler, D.R., Moodie, C.L., and Williams, T.J., “Some Industrial Administration Factors in the Computer Control of Chemical Plants,” Proceedings CHEMECA-70 Conference, Melbourne, Australia, pp. 7, 1–21 (August 1979).

[4] Eriksson, L., “Integrerade Datorsystem i Vara Fabriker Nulage och Utveckling,” Svensk Papperstidnig, Nr 18, (1977) (In Swedish).

[5] Fujishima, Chico, Straus, R.W., et al., Detailed Description, Nippon Steel Company, Hierarchical Integrated On-Line Computerized Control System, Galaxy, Inc., Washington, D.C., p. 119 (July 1979).

[6] Gochi, Eiji, et al., “Special Issue on the Computer System,” The Sumitomo Search, No. 24, Sumitomo Metal Industries, Ltd., Osaka, Japan (November 1980).

[7] Hiatt, W.H., and Petersen, C.D., Reliability Analysis of the Proposed Hierarchical Computer Control System for Large Steel Manufacturing Complexes, Report Number 93, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (September 1977).

[8] Hindin, H.J., and Manuel, T., “Local Networks Will Multiply Opportunities in the 1980's,” Electronics, 55, No. 2, pp. 88–89 (January 27, 1982).

[9] Inoue, Y., et al., “Cast Study 5, Practical Management and Control in the Steel Industry,” Proceedings, IFAC Congress, Kyoto, Japan, pp. CS-106 to CS-117 (August 1981).

[10] Kramer, S., Automation of Information Systems, Estel Hoogovens BV, Ijmuiden, The Netherlands (July 1981).

[11] Long, L.C., Schunk, J.H., and the Steel Industry Advisory Committee, Description of the Example Flat Rolled, Sheet, Strip Steel Mill Used in the Steel Project, Report Number 105, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (September 1977, Revised October 1979).

[12] McGowan, M.J., "The PROWAY Project: is a Standard Process Control Bus in Sight?", Control Engineering, 26, No. 8, pp 29–34 (August 1979).

[13] Miyake, Jukio, et al., “Ohgishima Special Issue,” Nippon Kokan Technical Report, No. 28, Nippon Kokan K.K., Tokyo, Japan (June 1980).

[14] Project Staff, Tasks and Functional Specifications of the Steel Plant Hierarchy Control System, Report Number 98, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (September 1977, Revised June 1982, June 1984).

[15] Project Staff, Systems Engineering of Hierarchy Computer Control Systems for Large Steel Manufacturing Complexes, Report Number 100, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (September 1977).

[16] Schaffer, E.J., and Williams, T.J., An Analysis of Fault Detection, Correction and Prevention in Industrial Computer Systems, Report Number 106, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (October 1977).

[17] Saridis, G.N., “Toward the Realization of Intelligent Controls,” Proceedings of the IEEE, 67, No. 8, p. 1115 (August 1979).

[18] Uronen, P., and Williams, T.J., Hierarchical Computer Control in the Pulp and Paper Industry, Report Number 111, Purdue Laboratory for Applied Industrial Control, Purdue University, West Lafayette, Indiana (September 1978).

[19] Wachter, W.J., "System Malfunction Detection and Correction," Digest of the 1975 International Symposium on

Fault-Tolerant Computing, Paris, France, June 1975, IEEE Computer Society, New York, New York, pp. 196–201.

[20] Wensley, J.H., Levitt, K.N., and Neumann, P.G., “A Comparative Study of Architectures for Fault-Tolerance,” Digest of the 1974 International Symposium on Fault-Tolerant Computing, Urbana, Illinois, June 1974, IEEE Computer Society, New York, New York, pp. 4–16 to 4–21.

[21] Williams, T.J., “Present Status and Outlook for Adaptive and Learning Control in Industrial Control Systems,”

Dechema Monographien, 67, No. 1222–1263, Part 1, p. 9 (1971).

[22] Williams, T.J., “Computer Control and Its Affect on Industrial Productivity,” A.I. Johnson Memorial Lecture, National Research Council of Canada, Montreal (May 24, 1979).

[23] Williams, T.J., “The New Process Control Hardware and Its Effect on Industrial Control of the Future,” Proceedings PROMECON I, Institute of Measurement and Control, London, England, pp. 173–186 (June 16–18, 1981).
