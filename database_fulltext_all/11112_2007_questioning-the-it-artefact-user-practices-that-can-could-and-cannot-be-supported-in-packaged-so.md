---
otero_id: 11112
otero_key: "4UDACQVC"
title: "Questioning the IT artefact: user practices that can, could, and cannot be supported in packaged-software designs"
authors: "M W Chiasson; L W Green"
year: "2007"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000701"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Questioning the IT artefact: user practices that can, could, and cannot be supported in packaged-software designs

MW Chiasson<sup>1</sup> and LW Green<sup>2</sup>

<sup>1</sup>Management School, Lancaster University, Lancaster, U.K.; <sup>2</sup>School of Public Health, University of California at Berkeley, CA, U.S.A.

Correspondence: MW Chiasson, Management School, Lancaster University, Lancaster LA1 4YX, U.K. Tel: þ 44 (0)1524 594255; Fax: þ 44 (0)1524 844885; E-mail: m.chiasson@lancaster.ac.uk

## Abstract

The purchase of packaged software has brought new opportunities and challenges to the development of information systems. An important question for packaged software consumers is how a software package will support, change or inhibit practices. To address this question, our paper focuses on the decisions made by a team developing four different software prototypes, with increasingly relaxed constraints on data content and structure. Each prototype significantly enlarged the number of health promotion planners that could be supported by the software. Consistent with the literature, the software designers balanced specificity (constraint) and generality (opening) in the software to incorporate a desire to serve a broad audience, and a need to be relevant to various sub-groups within this audience. Given a detailed knowledge of the software artefact, including the data content and structural choices made by designers, we hope to enable software consumers to question IT artefacts and their spokespeople, so they can make active and informed choices about software generality and specificity. We also suggest that this questioning process is shared across both customised and packaged software, and that the inscription of technology by designers may be either deterministic and detailed, or emergent and general. The implications for packaged software research and practice are considered.

Keywords: packaged software; design; selection; specificity; planning

## Introduction and motivation

IS researchers have examined various assumptions behind IS development practice (Hirschheim & Klein, 1989; Iivari et al., 1998; Avison & Fitzgerald, 2003). One assumption is that the development of organisation-specific information systems from generic programming software is the dominant approach to system design (Sawyer, 2000, 2001). Many of the debates about system analysis and design (Chen, 1976; Yourdon, 1976; Boehm, 1988; Coad & Yourdon, 1991; Booch, 1996) are based on an assumption that software designs emerge from user requirements, independent of available software and technical systems.

In contrast, some suggest that the increase in environmental turbulence surrounding organisations challenges many system development assumptions (Truex et al., 1999), and contribute to software development failure (Standish, 2004). One possibility for increased success is the use of packaged software in order for companies to deal with industrial turbulence, and to shorten implementation timeframes (Keil & Tiwana, 2005).

One area of IS research that has examined packaged software design issues is the enterprise resource planning (ERP) systems literature. In particular, organisations face a different problem with ERP than customised systems development – the need to change their organisational practices in order to fit the software ‘best practices’ (Davenport, 1998; Pollock & Cornford, 2004; Wagner & Newell, 2004; Light, 2005a). As anticipated by Brooks (1987), ‘[t] he key issue, of course, is applicability. Can I use an available off-the-shelf package to do my task?’ (p. 198). In asking these software-driven questions, important assumptions about requirements-driven design need to be reconsidered (Boehm, 1999; Sawyer, 2000).

The basic problem is that organisations will inevitably have specific needs and requirements that must be met by packaged software, either in the existing functionality or through software customisation (Lucas et al., 1988; Light, 2005a). Discrepancies between the software and organisational practices can be a combination of functionality, which is ‘too far’ or ‘too close’. The software can be ‘too far’ from the specific needs of the organisation, thus requiring extensive configuration and development. The software functionality can also be ‘too close’, because of irrelevant or inappropriate functionality that often cannot be modified. This includes irrelevant functionality which can overburden the organisation with unnecessary features that are expensive to purchase, install, maintain, and avoid. As a result, a number of significant costs related to commercial off-the-shelf software (COTS) implementation are often hidden and unrealised at the outset (Keil & Tiwana, 2005). Many of these costs relate to the time, expertise and resources required to address these key discrepancies (Lucas et al., 1988).

One important question in packaged software design and consumption is determining what the software can and will do, in supporting, changing or inhibiting desired organisational practices. Some IS research has examined trade-offs between developers and customers in IS development outsourcing (Sabherwal, 2003), the use of software and business-process components in ERP (Pollock & Cornford, 2004) and the structuring of generic software through socio-technical processes such as genres and technologies-in-practice (Orlikowski & Yates, 1994). But additional work on the early stages of software projects (Cooper & Zmud 1990), including the technical choices and social assumptions made by software developers, and their effect on the range of user practices that can or cannot be supported by the software, is required.

To address these issues, our paper focuses on a team developing software prototypes for health promotion planners. Each prototype represented an attempt to support a wider number of health planners than an initial prototype designed for only breast cancer prevention. Four prototypes were developed, using different database techniques to escape the ‘too near’ problem of specific database content and structure, while providing the ability to modify data content and structure in order to avoid the ‘too far’ problem. Our paper examines the team’s assumptions and decisions, and the constraints and openings realised in the four different software prototypes.

To assist us in understanding the development and proposed influence of these prototypes on practice (Orlikowski & Iacono, 2001), we use two derived concepts from Lucas et al. (1988) and from transaction cost economics (Williamson, 1981; Wang, 2002): software specificity and generality. We refer to software specificity as the tasks that can (or cannot) be supported by the software, and generality as the range of business tasks which could be supported in the software, but require various levels of customisation.

Consistent with the literature, packaged software designers attempt to balance software generality (opening) in order to attract a broad number of possible users, with software specificity (constraint) in order to be relevant to various sub-groups within this audience. One way to handle this balance is to produce very generic software which enrols other intermediaries, such as trainers, consultants and expert users to assist in the diffusion and specification of software, through perhaps an organising vision (Swanson & Ramiller, 1997). The software thus serves as a blueprint for more specific software artefacts and organisational practices (Light, 2005b).

We conclude that our exploration of packaged software systems demonstrates how a detailed knowledge of the data content and structure can support the questioning of IT artefacts and their spokespeople, in order for consumers to make active and informed choices about which software systems will serve their organisations diverse interests. This will allow them to determine how difficult it will be to customise generic functionality, and if and how to generalise specific functionality. We also suggest that this process of software questioning is shared across both customised and packaged software, since both rely upon a software foundation. They differ, however, in terms of handling different ends of the problems: the generality of the software in the case of customised development, and the specificity of software in the case of packaged development.

The paper proceeds as follows. We discuss the relevant health promotion planning literature in order to provide background for our case findings. We then present our case study methodology, followed by our findings. We discuss and conclude with implications for packaged software research and practice.

## Health promotion planning

In order to develop software to support health planning, software designers must ask what health planning entails. One answer is that it is the identification of causes, effects, and resources within clinical, educational, and community settings, which can be used to improve the quality-of-life of individuals and groups by targeting the levers that promote healthy living (Green & Kreuter, 2005). Within this general definition, however, there are two broad approaches to health promotion planning. One is the planned approach, which utilises top-down and scientific evidence to develop plans. It often provides a structured and detailed recipe for health promotion planning, which has the planner collect data, implement parts of programs and evaluate outcomes at the same time, requiring a back-and-forth style of planning to develop immediate and tailored interventions in specific communities. The other is the responsive approach, which emphasises community-specific needs using local evidence (Nutbeam, 1997; Abma, 2005). Its participatory nature is less structured than the planned approach, often calling for more organic, dynamic, and customised approaches to evidence collection and use in planning practice.

Practitioners are aware of the value of the planned approach, but they are often overwhelmed by the extent of scientific data required for it. Consequently, they often focus on limited community-based data due to political and external pressures to act quickly and decisively. The sense of ‘drowning in information, but starved for knowledge’ is pervasive. They are expected, by their peers and sponsors, to deal with volumes of scientific evidence in order to decide what is important and what works in ideal settings, while making their programs more relevant to their local communities’ characteristics and circumstances (Butterfoss et al., 1996). When forced to choose between these demands, they focus on the community data rather than the less tangible assurance of scientific research. As a result, the ‘gap’ between research and practice has grown wider over a long period of time, because of information overload (Goodman et al., 1993).

It is this identified need to collect, integrate and make use of evidence from both research and community sources that motivated a team of developers to create various software prototypes to support health promotion planning.

## Methodology

The question addressed in this paper is: how do software designs support, change or inhibit user practices? To address this question, we participated in a team designing four prototypes for health promotion planning.

The team consisted of academic researchers and software programmers, with an interest in developing software systems to support health promotion planning activities (initially in the planned approach to health promotion planning). Responding to comments about the restricted use and relevance of an initial prototype, the three other prototypes were developed to alleviate constraints on data content and structure (Chiasson & Lovato, 2000, 2001). The authors were also active participants in the project, similar to the participant– observer approach to ethnographic research. This allowed us to study and influence the development team’s actions, as they encountered particular challenges and opportunities. This longitudinal examination also allowed us to determine how individual and group attitudes, critical events and behaviours affected the course of development (Van de Ven & Huber, 1990). It also gave us important insights into timing, learning, adaptation, evolution, technology and social systems interaction, rates of change and responses to contextual factors (Vitalari, 1985).

A case study approach was used, and is appropriate when the issue is best studied in its natural setting, while employing multiple data collection techniques to uncover the complexity and richness of a phenomenon across time, such as the development of information systems (Yin, 1994). Our study also provides a critical case of the issues related to packaged software development, and the various techniques employed by the developers to manage trade-offs between software specificity and generality. It represents a supply-side view of the IT artefact, and its design and shaping (Attewell, 1992; Orlikowski & Iacono, 2001).

Data from the study included documents, e-mails and observational data from development team meetings. This produced numerous meeting minutes, observational notes, interview transcripts and survey results. Particular themes were extracted from critical events and changes in the development team’s directions, which are reported in this paper.

The data were analysed in order to link case data to the theory and empirical work in information systems through ‘analytic generalisation’ (Eisenhardt, 1989; Lee, 1989; Yin 1994; Sabherwal & Robey, 1995). The level of analysis was ‘situated-activity’ (Layder, 1993), where we focused on the interaction between the team and the emerging technological designs. Our findings are reported next.

## Findings

The Empower-Netpower project emerged out of a meshing of academic and commercial interests. The purpose of development was to produce a Canadian and international version of EMPOWER from the U.S. version of the software, and to implement and observe the usage of the software in two Canadian communities planning mammography screening interventions. Further adaptation of the software would be completed from experiences in the field. The project was initially funded by the National Cancer Institute of Canada (NCIC), which was interested only in the implementation and development of a planning methodology across Canadian communities. NCIC provided a 2 year grant for pilot testing of the planning tool in the Canadian settings.

Four prototypes were developed for health promotion planning users during the course of the project. Only the first prototype was thoroughly evaluated by students and community-based health planners. The second, third and fourth prototypes were designed in response to perceived constraints on the number of users who could use the first prototype. Each prototype was an attempt to produce software that was relevant to a broader audience of health promotion planners. Given the data content and structure in the initial prototype, it served a relatively narrow range of planners with specific functionality. The later three prototypes were developed to serve a broader range of planners with generic data content and structure which could be shaped by users’ settings and data. To do so, subsequent prototypes successively removed data content and structural constraints using various standard and non-standard database techniques, thus allowing the users to specify their own data content and structures in the software. This resulted in three additional prototypes that could be applied to a broader number of health planning users than the original. However, each new prototype required the user to further customise the system through data (in prototypes 2 and 3), and data structures (in prototype 4). A description of the development of the prototypes provides details of the team’s balancing of software specificity and generality in serving a larger number of planners.

## Prototype 1

The first prototype, EMPOWER, was a system designed for health promotion planners involved in the detection and prevention of breast cancer. It was originally designed by a U.S. company and was to be redesigned by the development team in order to produce a Canadian version. Based on the Precede/Proceed Model (Green & Kreuter, 2005), which is illustrated in Figure 1, the purpose of the software was to increase the diffusion and application of research knowledge in health planning for breast cancer prevention.

EMPOWER mimics a planned approach to the Precede– Procede model of health promotion planning (Nutbeam, 1997; Green & Kreuter, 2005) by leading the user through stages 1–6 in planning educational and policy programs. The software directs the users through specific steps needed to change attitudinal, social and environmental factors to increase mammography screening rates, and to increase the early detection of breast cancer. Stages 1 to 6 focus on the assessment of the planning situation (situation analysis and quality-of-life issues); an analysis of health issues that affect quality of life (epidemiological analysis of health issues); an analysis of behaviours and environmental factors that affect health (behavioural and environmental analysis); attitudes, influences and resources affecting behaviour and environment (educational and organisational analysis) and educational and policy levers that could change these (administrative and policy analysis). The stages of the Precede–Proceed model were encoded as one or more pages in the software. Figure 2 illustrates one of the 96 pages in EMPOWER.

This particular page asks the user to assess the resources currently available in the community. The information captured on each page is stored in a separate project file that was intended to be retrievable and changeable at any time. Figure 3 illustrates the steps and resources included in the software.

Looking at Figure 3, the planner follows the pages like a book, entering her specific project information into the electronic pages, which are stored in a text-based project

![](/api/attachments/4UDACQVC/fulltext/images/38dd6cfe1e93dd3639f7579bc4aabb1cb121ee88f60496113c2bed3758317448.jpg)  
Figure 2 Prototype 1: A sample page from EMPOWER.

![](/api/attachments/4UDACQVC/fulltext/images/878bb60378c60d2ec11ae0dfdabc0329b2350f4948a923804ef5180a3b6a0e53.jpg)  
Figure 1 Precede–Proceed model of health promotion planning – EMPOWER focuses on stages 1 through 6.

![](/api/attachments/4UDACQVC/fulltext/images/09e73cf8c7c043a678f4fb6d44cec13aa09dc910e50d416f51aa0881959ed147.jpg)  
Figure 3 Prototype 1: The program structure of the EMPOWER software.

file. This information is then summarised in reports, and additional information is available from each page, displaying scientific evidence or professional experience to deal with project-specific circumstances. In addition, resources (‘consult-on-tap’) are available for each screen, including Precede–Proceed references, case examples, page help, references, and academic and non-academic resources.

Despite some successes in classroom sessions and in the field (Chiasson & Lovato, 2000, 2001), feedback from the users indicated that EMPOWER was too specific for practical use, despite considerable value in training health promotion planners. Not surprisingly, the data content was, by design, only for breast cancer screening and was thus only useful as a training tool for planners focused on other health issues. More surprising, the booklike structure of the software restricted easy updating of project data, resources files and page resources.

A part of the problem for users was that the original U.S. designers had mixed both data and presentation together on the 96 pages, with the data stored in various flat-files that were difficult to modify. Given this, it was difficult to change the information in order to include more recent evidence on breast cancer and Canadian epidemiological data, which differed from the American data. The data quickly became out of date for even those planners focused on breast cancer and mammography screening.

In addition to these data content issues, users required more flexible tools to deal with practical issues in the field than EMPOWER could provide. They needed more responsive approaches to health promotion planning, and a prototype to support this capability.

The planned approach appeared to be fine during the early stages of planning and training, but the responsive approach was needed to provide flexibility for later planning and implementation tasks (Chiasson & Lovato, 2000, 2001). The specific structure of data entry-access in a step-by-step manner restricted the responsive entry of new information later in the planning process, and it restricted individual-specific approaches to information storage and handling. As a result, for initial training purposes with novice users, EMPOWER was fine. But for experienced health planners wishing to employ it in the field, it was too constraining and specific for their hectic and chaotic work environments.

## Prototype 2

In designing the next prototype, which was called NETPOWER (Network Enabling Technology for Planning and Organising Within Everyone’s Reach), the development team felt it was important to produce a software system that could support any health promotion planner, regardless of planning style and topic area. Navigation to the data and between the evidence would need to be flexible. Users would need to have the capability to enter their own data, and the software structure would need to be invoked by the user ‘on demand’, instead of always ‘on top’.

The overall design objective was to create a computerised work space for the planner – more akin to a computer-aided design tool than a structured book. For those who needed more structure, a set of rules was to be available to guide the planner when desired, but the data, the structure among data elements and the process of navigating through the data would be flexible.

To accomplish this, the development team turned to other data and database platforms. One well-established data platform which allows flexible data management and information-focused design is the relational database system. Relational database systems map out things of interest to the user, and the relations between these things. Users can then enter content into the system, thus fleshing out the application and its further use. As long as the database structure is correct and universally applicable to all users, the software would be useful to most health promotion planners.

To achieve this, the development team focused on the information considered to be necessary for most health promotion planners. Unlike the first prototype, this one would be empty of specific health promotion and disease information. However, to assist the first-time planner, the prototype would need some initial data to shape it towards a specific health promotion area and to provide guidance.

Guided by the Precede–Proceed model of health planning, tables were initially created for each factor category: quality of life; health; behaviour; environment factors; predisposing, reinforcing and enabling change; health education interventions and policy or regulatory interventions. In addition, tables were added for references and contact information, and prescribed relational links among the tables were created (e.g. health to quality-of-life, behaviour to health, environment to health, etc.). Figure 4 illustrates the interface of the second prototype:

The prototype was to allow users to enter field-specific data for each of the factor types, stored in different tables. These would then be linked to each other, using the linkages specified in the Precede–Proceed model (see Figure 1). For example, health factors are connected to quality-of-life issues (e.g. lung cancer and suffering), and behaviours are connected to health issues (e.g. smoking and lung cancer). Given the many-to-many possibilities among factors, separates tables would need to be developed to manage each possible connection.

Despite some obvious advantages with this design compared to EMPOWER in addressing the needs of various health planners, the team felt that numerous applications of the Precede–Proceed approach rarely followed the tightly prescribed chain of causation in Figure 1. For example, despite specific causal arrows from attitudes to behaviours to health outcomes, on numerous occasions planners would draw reverse connections between factors. For example, health outcomes could produce predisposing attitudes that affected behaviour, or a behaviour could affect an attitude. So in addition to the many join tables required for the standard

![](/api/attachments/4UDACQVC/fulltext/images/8e642aa56f625efe157d3b7b2bc8295f2cbd19e8ee179f4859d159b24f588b89.jpg)  
Figure 4 Prototype 2: Relational Database tables for each factor type in the Precede–Proceed model.

Precede–Proceed model, many other join tables would be needed to join any factor table to any other (in the extreme case, the number of tables would be nine factorial, which would be 45 join tables).

Related to this, the development team realised that reference materials could be relevant to any one of the factors and linkages, requiring another nine join tables for each connection between the reference and factor tables alone. This would also be the case for contact information and any other resource. The combinations and permutations, combined with the software code and interfaces required for each table and connection, would be overwhelming. As a result, the team considered another design strategy in order to build a simpler data structure that could handle this complexity and flexibility.

## Prototype 3

The team decided to pursue a different prototype, using a database design that collapsed the Precede–Proceed model’s complexity. It began by thinking of the factor types (e.g. quality-of-life, health, behaviour, etc.) as a single class of objects, connected by a single type of linkage between the factors.

In doing so, Figure 5 illustrates how the Precede– Proceed model was recast as a means-end chain of cause and effects. Figure 5 shows the Precede–Proceed model as a means-end chain of factor types, moving from left-toright, and right-to-left. As one moves left on a means-end chain, causal factors are identified which answer how the effect is going to be produced. As one moves right a means-end chain, effects factors are identified which address why a causal factor is included in the model.

Once all the factor types (behaviours, health, qualityof-life, etc.) are considered to be the same thing, a single database table can be used to store information about them. In this case, the development team decided to stick with a single table to store factors and linkages between factors, as shown in Figure 6.

Figure 6 illustrates how factor tables for quality of life, health, behaviour, etc. are integrated into a single Factors table to hold information relevant to every factor. It also illustrates how the Linkages between two factors would be stored for a specific project. Particular attributes have also been identified for these two tables that the team believed would be important to all users. For the Factors table, these include the current and desired level of a factor, its name and the importance of this specific factor (on a scale of 1–6). The Linkages table includes attributes such as the factor cause and the factor effect (means-end chain), and the strength of the connection.

The Factor Library and the Linkage Library tables can then be used to store factors and linkages identified in the literature – hence their association with the References table. For example, a connection between smoking and lung cancer can be stored in Factor Lib and the Linkage Lib, with particular strength characteristics. These theoretical factors and linkages can then be copied into the Factors and Linkages tables to be used by a planner on a specific project. In addition, key Contacts in the project can be called upon to assist with particular project Linkages in order to provide information or support proposed changes.

Figure 7 shows how the third prototype software can be used to connect any factor to any other factor, using this prototype designs. In this figure, various factor types could be connected to any other, within the flexible cause–effect chain. Various references and contacts can be connected to the linkages in order to support the project plan.

This design dramatically reduced the complexity of managing linkages between many factors, from separate independent and join tables, to essentially six tables. It also freed the health planner from the built-in constraints of the Precede–Proceed model, by allowing them to create and connect any factor to any other factor.

![](/api/attachments/4UDACQVC/fulltext/images/90770130844cb87325e49141d342677fb8d6ab233bf57437612584b70ec3720c.jpg)  
Figure 5 Prototype 3: Remodelling Precede–Proceed in order to simplify the data design.

![](/api/attachments/4UDACQVC/fulltext/images/bd82797d677cd003897a3028144b741b88bfd0c343198142c43b09af70de5101.jpg)  
Figure 6 Prototype 3: The resulting database structure of Netpower in the intermediate stage.

![](/api/attachments/4UDACQVC/fulltext/images/6257f60d98ccc823574ecf109220bd846fc48834f3b39008bb69754f4711aa4c.jpg)  
Figure 7 Prototype 3: An example using tobacco control.

However, despite the obvious improvements in this design, the team decided that the software still limited the user’s ability to alter field structures of the objects. For example, what if the user wishes to focus on different object attributes than those pre-built in the relational structures? To enhance the generality of the design to support an even broader range of users, the next prototype considered the possibility of removing the constraints on field designs.

## Prototype 4

The fourth prototype generalised health planning one step further, by employing a database technique that allowed users to design and modify the fields for not only factors, linkages, references and contacts, but also for any object they wished to collect information. It did so by using database tables to record meta-data about objects and their field structures, and used a generic engine to create input, update and display screens for these objects.

Figure 8 shows how the previous tobacco factors, linkages, etc. can be recast as objects.

The figure shows the tobacco example as a series of objects and connectors between these various objects.

It also shows how references and contacts can also be recast as objects.

To generalise this capability, a fourth prototype was developed with only two tables – one to allow the user to record objects and attributes of interest to them, and the second to record attributes and their values.

As Figure 9 shows, the Object Types table recorded the various fields and their related factor and connector parent (parent type number). Object types were stored for reuse, modification and the creation of new object types. These structures were then used to produce, using a generic engine, an input and update screen for factors and connectors, which allowed the storage of values in the Object Values table. Given this design, users could specify the various objects of interest to them in planning, and record and update the values of these objects.

![](/api/attachments/4UDACQVC/fulltext/images/9a2e6e95165b6b08ea35a32914ecbd4f8f7beca1c72801cb55981bb3cda8addf.jpg)  
Figure 9 Prototype 4: Database design.

![](/api/attachments/4UDACQVC/fulltext/images/e567a6ee3a797a3c945cd48666b2849380303725db231ab26f77f496b7c0acbd.jpg)  
Figure 8 Prototype 4: Tobacco example as objects with attributes.

In doing so, the fourth prototype was not only applicable to health promotion planning, but also useful to any area of planning. As both the structures and content could be determined by the user, objects could be created for other planning areas, even software development itself, in addition to health promotion planning.

In the next section, we consider the advantages and disadvantages of these new software designs, focusing on the characteristics of software specificity and generality.

## Discussion

Consistent with many of the findings on packaged software, the packaged software team was entrepreneurially motivated by market share (Sawyer, 2000). The software design was also founded on technical designs, as opposed to extensive user involvement. The development process was also less-controlled than the traditional waterfall approach to software design (Sawyer, 2000), drawing upon abstractions of work and technology which could be supported by recursive means-ends chains in the software.

Expanding on this knowledge of packaged software design, the development process was motivated by restrictions in an initial prototype. It was designed for breast cancer screening, and both content and data structures were fixed. It thus limited the potential market of users who would be interested in more generic software that would allow for the customisation to many specific health areas, such as heart disease and other cancers.

To relax these constraints, a second prototype was developed in order to remove restrictions on data content using a relational database system. Despite advantages in allowing data to be entered and changed for many health promotion topics, the design restricted the ability of users to connect factors beyond the fixed set of Precede– Proceed relationships (e.g. predisposing factors to behaviours, vs behaviour to predisposing factors). This prevented health planners from connecting the factors in their own way. To alleviate this restriction, a third prototype was developed that generalised all factor types into one table, and all the connections into another, in order to allow users latitude in connecting factors. However, important in the third design was the identification of a universal and unchanging set of data fields for all factor types – behaviour, health, quality-of-life and others. To overcome these constraints, a fourth prototype was developed to remove restrictions on the object types and field structures, by having these stored in only two relational tables. This final prototype represented the most generic system for health planning, to a point where it could be applied to any planning area because the data structure and content could be shaped towards any planning field.

Despite the advantages of the generic rather than specific software, the final software prototype is now ‘too far’ from any specific user’s planning task and context. It contains only a generic process, without data for any specific health area (e.g. heart disease or breast cancer), without any specific ‘things’ needed to focus the data collection (e.g. health factors, attitudes, health status indicators, etc.), and without any connections between these factors (e.g. smoking to heart disease). Learning the software model and customising it towards health planning will require significant work and discovery (Light, 2005b). The generic strength of the later prototypes is now their greatest weakness – as they are further removed from supporting any particular health planner. It will now take time and effort to develop the data content and structures to make it relevant.

We suggest that to assist with this process, an organising vision will be needed to attract, support and direct a community of practice interested in the diffusion and use of the software – trainers, consultants, system developers and users (Swanson & Ramiller, 1997). These intermediaries must be able and willing to tailor the generic software to support specific customer practices. Without these other participants, the generic prototype may remain an empty and unused shell. It also requires increasing industrial experience with regard to which practices can, could, and cannot be supported in particular software artefacts (Orlikowski & Iacono, 2001).

For example, to address the generality of the software, the latest prototypes now require significant user training and data entry in order for it to be applicable to any specific health planning area, unlike the original prototype. Perhaps additional software designs, such as software ‘wizards’ that mimic the walk-through techniques of the Precede–Proceed model, would allow users to see how the software could work. This could help overcome the disorienting openness of the generic software system. It is also possible that pre-configured data structures and content could be developed by other intermediaries such as consultants, or other users, to support use of the system.

We concede, however, that despite the generality of later prototypes, that the software still serves as a blueprint (Light, 2005b). In our case, even the later prototype directs user practices towards more rational and planned approaches to health planning – as a means-ends chain. It thus accentuates structured reflection over organic planning, as opposed to even more generic software tools, such as e-mail and a word processor. As such the later software may be unable to support a more responsive approach to planning.

Based on these results, one important implication of our study is that packaged software design and consumption is about competing and complementary objectives between vendors and consumers. Vendors attempt to develop software with as much generality as possible, to capture a wider market share (Light, 2005b). They hope their software is ‘far’ enough away from specific organisational uses so that it can be shaped by many users, but not too far that it requires substantial resources to shape it to support specific practices. On the other hand, customers are (or should be) motivated to search for specific software systems that support their current or future practices. Where the two interests cross, customers are left with the choice of generic software that is hopefully less expensive to purchase and shape than starting-from-scratch. Developers of generic software may also solve a significant problem for customers by helping them avoid the costs of developing and living with the long-term constraints of customised software. This suggests there are greater risks with customised software that is ‘too near’ than packaged software that is ‘too far’ (Lucas et al., 1988; Light, 2005a). The problem with using customised software increases for organisations that require continuous business process change in order to deal with increasingly turbulent industrial environments (Truex et al., 1999).

Furthermore, we suggest that designers do inscribe interests into software. But packaged software designers intentions are to capture as many users as possible by building generic systems that allow significant reinvention. In this case, many unexpected uses of the software are in fact faithful to designers’ intentions (DeSanctis & Poole, 1994). To both the designers and users, more specific and predictable software designs are less valuable than the generic ones. In more theoretical terms, the designers are involved in producing software-based boundary objects that are ‘plastic’, and not fixed (Star & Griesemer, 1989; Gasson, 2006).

Despite important differences, there are many similar challenges of implementing both customised and packaged design. ERP implementations often fail because users struggle to identify the correct software system for the organisational practices (Davenport, 1998; Pollock & Cornford, 2004; Wagner & Newell, 2004; Light, 2005a). Customised design also rests on a selection of software to support the development of systems for organisational practices. The question in both cases are similar – how far or near is the software system to supporting our desired work practices? In the case of customised development, however, the problem may be more about generic software that is ‘too far’, than specific software that is ‘too near’. In both cases, software generality and specificity require resources to change software functionality that is either ‘too far’ or ‘too near’ (Williamson, 1981; Wang, 2002).

To ensure the best possible outcome in both packaged and customised design, we suggest that users engage in a detailed examination of data content and structure in the software in order to make active and informed choices about software systems. This examination includes both the IT artefact as a ‘non-human actant’, and their spokespeople (Callon, 1986; Gasson, 2006). These software artefacts, if they enrol and are enrolled by customers, influence the lives, work practice technical and outcomes of the organisational participants. As a newcomer, software artefacts need to be questioned and examined.

To ensure a good outcome, appropriate organisational and institutional locations need to be developed, so that the IT artefact can be questioned. Through these mechanisms, perhaps the problems with the unexpected costs of packaged software implementation can be addressed (Lucas et al., 1988; Keil & Tiwana, 2005).

## Conclusion

As researchers, we were motivated by the increasing use of packaged software systems in organisations to achieve low-cost and quick developmental advantages (Keil & Tiwana, 2005). Some suggest that with turbulent industrial and organisational environments, the traditional assumptions in system development are no longer relevant (Truex et al., 1999). As pre-existing packaged software are produced by vendors interested in software for a broad audience, software ‘fit’ may have as much to do with changing organisational practices to fit the software, than changing the software to fit the organisation. As a result, requirements may be determined more by what the software can do, than what the organisation does or wants to do.

Despite the trend to purchase pre-existing software instead of developing it from scratch, packaged software systems have only recently received attention in the literature (Sawyer, 2001; Pollock & Cornford, 2004; Light, 2005a). An important question in packaged software design and consumption is how can various software designs support, change or restrict user practices? To address this question, our paper focuses on a software development team and the constraints and capabilities realised in four different software prototypes for health promotion planners.

From our case study, we conclude that vendors strive to achieve a balance between generality and specificity by designing software engines that can be shaped for specific user practices. In particular, four software prototypes were designed to move from a narrow to a broad number of potential health promotion planners, by generalising the data content and structure in various database designs. In the later prototypes, generic software was to be made specific by having the user enter data content and structures.

We also contend that consumers need to understand the capabilities of the software artefacts, so they can make informed choices about the acceptance or change of the software, and the acceptance or change to their practices. In order to make informed choices about software and practice-related change, customers, and the intermediaries who support the consumption of software, need skills to question the producers of packaged software, in terms of software specificity and generality.

We also suggest that software is a non-human actant that affects organisational practices, and needs to be directly questioned by customers. We also suggest that the differences between packaged software and customised development are one of degree, not kind. Both require the careful consideration and selection of software platforms for development. Finally, we suggest that while developers inscribe their interests into software, this inscription is as general as possible, so that many software consumers are attracted to use the software.

The result is a social and technical ecology of software development, selection and reinvention that requires future research and new approaches to software practice, to allow customers to determine what can and cannot change in the software, and the capacity to tell the difference.

Our study is a preliminary investigation of how developers shape and choose software specificity and generality during design. This case provides specific

## About the authors

Mike W. Chiasson is an Advanced Institute for Management Research (AIM) Innovation Fellow, focused on service sector innovation in healthcare using information systems, and a senior lecturer at Lancaster University’s Management School, in the Department of Management Science. Before joining Lancaster University, he was an associate professor in the Haskayne School of Business, University of Calgary from 1999 to 2006, and he was a postdoctoral fellow at the Institute for Health Promotion Research at the University of British Columbia from 1996 to 1999. His research examines how social context affects IS development and implementation, using a range of social theories (actor network theory, structuration theory, critical social theory, ethnomethodology, communicative action, power-knowledge, deconstruction and institutional theory). In studying these questions, he has examined various development and implementation issues (privacy, user involvement, diffusion, outsourcing, cyber-crime and system development conflict) within medical, legal, engineering, entrepreneurial and governmental settings. Most of his work has been qualitative in nature, with a strong emphasis on participant observation. His work has appeared in various journals, including: Management Information Systems Quarterly, European Journal of Information Systems, Information & Organization, Data Base for Advances in Information Systems, Information Technology and People, and the International Journal of Medical Informatics.

Lawrence W. Green is an Adjunct Professor of Epidemiology and Biostatistics in the School of Medicine and Director of the developing Social and Behavioral Sciences Program in the Comprehensive Cancer Center at the University of California at San Francisco. He joined CDC empirical data to examine software development in health promotion planning, and the conclusions will need to be generalised in other settings with further empirical testing (Lee & Baskerville, 2003). Further research is needed to extend our understanding of these issues to other IT artefacts and social contexts where packaged software systems are developed and consumed.

## Acknowledgements

This project was partially funded by a National Cancer Institute (U.S.) grant to Robert Gold at Macro International, a National Cancer Institute of Canada grant to L. Green, and a Natural Science and Engineering Research Council Postdoctoral Fellowship. We thank those involved in the project including Dawne Milligan, Chris Lovato, Asim Ranjha, Robert Gold, Marshall Kreuter, Gina Dingwell, Louise Potvin, Amanda Joab, and Sue Mills. We also thank Beth Chiasson and Frances Chiasson for their important advice and editorial skills.

in 1999 as Distinguished Fellow-Visiting Scientist to study what accounted for the success of tobacco control in the last third of the 20th century, and how we might take those lessons to other areas of public health. He served as Director of CDC’s World Health Organization Collaborating Center on Global Tobacco Control and as Acting Director of the Office on Smoking and Health. He then served as the Director of CDC’s Office of Science and Extramural Research and as Associate Director for Prevention Research and Academic Partnerships in the Public Health Practice Program Office. He was also Visiting Professor in the Department of Behavioral Sciences and Health Education at Emory University’s Rollins School of Public Health and then Health and Society Visiting Professor at the University of Maryland. For most of the 1990s, Dr. Green was the Director of the Institute of Health Promotion Research and Professor and Head of the Division of Preventive Medicine and Health Promotion, Department of Health Care and Epidemiology, at the University of British Columbia in Canada. Dr. Green has broad experience in health education, prevention, population health, and community interventions for health promotion and risk reduction. He served as the first Director of the U.S. Office of Health Information and Health Promotion in the Office of the Assistant Secretary for Health under the Carter Administration, and as Vice President of the Kaiser Family Foundation. He has been on the public health faculties at Berkeley, Johns Hopkins, Harvard, Texas and Emory. Dr. Green is a past President and Distinguished Fellow of the Society for Public Health Education and recipient of the American Public Health Association’s highest awards (the Distinguished Career Award, the Award of Excellence, and the Mayhew Derryberry Award), and the

American Academy of Health Behavior first Research Laureate Medal. He currently serves on the Editorial Boards of the American Journal of Preventive Medicine, the American Journal of Health Behavior and 12 other journals in his field. His textbooks have been widely adopted. Community and Population Health with Judith Ottoson is

## References

ABMA T (2005) Responsive evaluation: it’s meaning and special contribution to health promotion. Evaluation and program planning 28(3), 279–289.

ATTEWELL P (1992) Technology diffusion and organizational learning. Organization Science 3(1), 1–19.

AVISON DE and FITZGERALD B (2003) Where now for development methodologies? Communications of the ACM 46(1), 79–82.

BOEHM BW (1988) A spiral model of software development and enhancement. Computer 21(5), 61–72.

BOEHM BW (1999) COTS integration: plug and pray? Computer 32(1), 135–138.

BOOCH G (1996) Object Oriented Analysis & Design: With Applications. Benjamin/Cummings, Redwood City, CA.

BROOKS FP (1987) No silver bullet: essence and accidents of software engineering. Computer 20(4), 10–20.

BUTTERFOSS FD, GOODMAN RM, WANDERSMAN A, VALOIS RF and CHINMAN MJ (1996) The plan quality index: an empowerment evaluation tool for measuring and improving the quality of plans. In Empowerment Evaluation: Knowledge and Tools for Self-Assessment & Accountability (FETTERMAN DM, KAFTARIAN SJ and WANDERSMAN A, Eds), pp 304–331, Sage, Thousand Oaks, California.

CALLON M (1986) Some elements of a sociology of translation: domestication of the scallops and the fishermen of St Brieuc Bay. In Power, Action, and Belief: A New Sociology of Knowledge? (LAW J, Ed), pp 196–233, Routledge and Kegan Paul, London.

COAD E and YOURDON E (1991) Object Oriented Design (2nd edition). Yourdon Press, Englewood Cliffs, NJ.

COOPER RB and ZMUD RW (1990) Information technology implementation research: a technological diffusion approach. Management Science 36(2), 123–139.

CHEN P (1976) The entity-relationship model: toward a unified view of data. ACM Transactions on Database Systems 1(1), 9–36.

CHIASSON MW and LOVATO C (2000) The health planning context and its effect on a user’s perceptions of software usefulness. Canadian Journal of Public Health 91(3), 225–228.

C MW and L C (2001) Factors influencing the formation of a user’s perceptions and use of a DSS software innovation. Data Base for Advances In Information Systems 32(3), 16–35.

DAVENPORT TH (1998) Putting the enterprise into the enterprise system. Harvard Business Review 76(4), 121–131.

DESANCTIS G and POOLE MS (1994) Capturing the complexity in advanced technology use: adaptive structuration theory. Organization Science 5(2), 121–147.

EISENHARDT KM (1989) Building theories from case study research. Academy of Management Review 14(4), 532–550.

GASSON S (2006) A genealogical study of boundary-spanning IS design. European Journal of Information Systems 15(1), 26–41.

GREEN LW and KREUTER M (2005) Health Program Planning: An Educational and Ecological Approach, 4th edn. McGraw Hill, New York.

GOODMAN GM, STECKLER A, HOOVER S and SCHWARTZ RA (1993) A critique of contemporary community health promotion approaches: based on a qualitative review of six programs in Maine. American Journal of Health Promotion 7, 208–220.

HIRSCHHEIM R and KLEIN H (1989) Four paradigms of information systems development. Communications of the ACM 32, 9–23.

IIVARI J, HIRSCHHEIM R and KLEIN HK (1998) A paradigmatic analysis contrasting information systems development approaches and methodologies. Information Systems Research 9(2), 164–193.

KEIL M and TIWANA A (2005) Beyond cost: the drivers of COTS application value. IEEE Software 22(3), 64.

LAYDER D (1993) New Strategies in Social Research: An Introduction and Guide. Polity Press, Cambridge, MA.

in its 8th edition; Health Program Planning: An Educational and Ecological Approach with Marshall Kreuter is in its 4th edition. The latter has been the repository for description of his Precede–Proceed model and the more than 950 published applications of this social-environmental model in case studies, research, and other textbooks.

LIGHT B (2005a) Potential pitfalls in packaged software adoption. Communications of the ACM 48(5), 119–121.

LIGHT B (2005b) Going beyond ‘misfit’ as a reason for ERP package customisation. Computers in industry 56, 606–619.

LEE A (1989) A scientific methodology for MIS case studies. Management Information Systems Quarterly 13(1), 33–50.

LEE A and BASKERVILLE R (2003) Generalizing generalizability in information systems research. Information Systems Research 14(3), 221–243.

LUCAS H, WALTON EJ and GINZBERG M (1988) Implementing Packaged Software. MIS Quarterly 12(4), 537–549.

NUTBEAM D (1997) Improving the fit between research and practice in health promotion: overcoming structural barriers. Canadian Journal of Public Health 87(suppl 2), s18–s23.

ORLIKOWSKI WJ and IACONO CS (2001) Research commentary: desperately seeking the ‘‘IT’’ in IT research – a call to theorizing the IT artifact. Information Systems Research 12(2), 121–134.

ORLIKOWSKI WJ and YATES J (1994) Genre repertoire: the structuring of communicative practices in organizations. Administrative Sciences Quarterly 39, 541–574.

POLLOCK N and CORNFORD J (2004) ERP systems and the university as a ‘‘unique’’ organization. Information, Technology & People 17(1), 31–52.

SABHERWAL R (2003) The evolution of coordination in outsourced software development projects: a comparison of client and vendor perspectives. Information and Organization 13(3), 153–202.

SABHERWAL R and ROBEY D (1995) Reconciling variance and process strategies for studying information systems development. Information Systems Research 6(4), 303–327.

SAWYER S (2000) Packaged software: implications of the differences from custom approaches to software development. European Journal of Information Systems 9, 47–58.

SAWYER S (2001) A market-based perspective on information systems development. Communications of the ACM 44(11), 97–102.

STANDISH GROUP (2004) 2004 Third quarter research report. Downloaded from http://www.standishgroup.com February 14, 2006. Full reference: http:// www.standishgroup.com/sample\_research/PDFpages/q3-spotlight.pdf.

STAR SL and GRIESEMER JR (1989) Institutional ecology, ‘translations’ and boundary objects: amateurs and professinals in Berkeley’s museum of Vertebrate Zoology. Social Studies of Science 19(3), 387–420.

SWANSON EB and RAMILLER NC (1997) The organizing vision in information systems innovation. Organization Science 8(5), 458–474.

TRUEX D, BASKERVILLE R and KLEIN H (1999) Growing systems in emergent organizations. Communications of the ACM 42(8), 117–123.

VAN DE VEN AH and HUBER GP (1990) Longitudinal field research methods for studying processes of organizational change. Organization Science 1(3), 213–219.

VITALARI NP (1985) The need for longitudinal designs in the study of computing environments. In Research Methods in Information Systems (MUMFORD E, Ed), pp 243–267, Elsevier Science Publishers, North-Holland.

WAGNER EL and NEWELL S (2004) ‘Best’ for whom? The tension between ‘best practice’ ERP packages and diverse epistemic cultures in a university context. Journal of Strategic Information Systems 13, 305–328.

WANG ETG (2002) Transaction attributes and software outsourcing success: an empirical investigation of transaction cost theory. Information Systems Journal 12, 153–181.

WILLIAMSON O (1981) The economics of organization: the transaction cost approach. American Journal of Sociology 87(3), 548–577.

YIN RK (1994) Case Study Research: Design and Methods. Sage, Newbury Park. YOURDON E (1976) Structured Design. Prentice-Hall, Englewood Cliffs, NJ.
