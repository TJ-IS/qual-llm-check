---
otero_id: 27420
otero_key: "ZK8JRE8S"
title: "A Principles-Based Enterprise Architecture: Lessons From Texaco and Star Enterprise"
authors: "Gary L. Richardson; Brad M. Jackson; Gary W. Dickson"
year: "1990"
journal: "MIS Quarterly"
doi: "10.2307/249787"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
A Principles-Based Enterprise Architecture: Lessons from Texaco and Star Enterprise Author(s): Gary L. Richardson, Brad M. Jackson and Gary W. Dickson  
Source: MIS Quarterly, Vol. 14, No. 4 (Dec., 1990), pp. 385-403  
Published by: Management Information Systems Research Center, University of Minnesota  
Stable URL: http://www.jstor.org/stable/249787

Accessed: 25/06/2014 00:06

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# A Principles-Based Enterprise Architecture: Lessons From Texaco and Star Enterprise

By: Gary L. Richardson
Information Technology Services
Star Enterprise
12700 Northborough Drive
Houston, Texas 77067

Brad M. Jackson
Information Technology
Department

Texaco Inc.
P.O. Box 37327
Houston, Texas 77237

Gary W. Dickson
Carlson School of Management
University of Minnesota
Minneapolis, Minnesota 55455

## Abstract

Star Enterprise is a joint venture partnership between Texaco Inc. and the Saudi Arabian Oil Company. Created in 1988, it became fully operational on January 1, 1989. This new organization inherited staff, facilities, and information resources existing within Texaco Inc. at the time of formation. A significant opportunity for the new organization was to create a new Enterprise Information Technology Architecture to support business functions and management decision making. While this venture was an opportunity, it was also a challenge because of the existing information technology that was comprised of incompatible hardware and nonintegrated systems. This paper describes the architecture that emerged and reviews its current status. Two major contributions of the paper are to identify the principles upon which the architecture is being created and to review what has been learned to date in the process of implementing the architecture.

Keywords: Information architecture, principles, LAN, networking, enterprise, case study

ACM Categories: C.2.1, C.2.4, H.2.4, J.1

## Introduction

“Almost all MIS managers these days find themselves struggling with the problem of integrating a proliferation of departmental and desktop computers. Stand-alone minis and micros have their place, but managers very often run up against a wall due to a lack of ready access to corporate data; for this, interconnection through telecommunications is required” (Emery, 1989, p. 432).

Although Emery's statement is true, the problem goes beyond linking hardware and data (see Hale, et al., 1989, for an excellent example of a “corporate data transport” system). Determination of software, applications, and what is performed where is the dilemma created by the new and extremely capable information technology (IT). Today’s corporate information environment is crying for a complete architecture. The goal of the architecture is to define and interrelate data; make hardware, software, and communications resources available; and have the staff to efficiently and effectively process transactions, produce information, and support a variety of domains of human activity. This demand transcends the definition of where and how data is stored (data architecture). It builds upon, but is not limited to specification of the linking of hardware (network architecture—see Jackson, et al., 1989). And, it is closely tied to (but goes beyond) an information architecture. The latter has been defined as follows:

The term, “information system architecture” refers to the overall structure of the information system. This structure consists of the applications for the various levels of the organization (operations, management control, and strategic planning) and the applications oriented to various management activities (planning, control, and decision making). The system structure or architecture also includes databases, model bases, and supporting software. An information system architecture for an organization should guide long-range development but also allow response to diverse short-range information system demands (Dickson and Wetherbe, 1985, p. 122).

As these authors go on to state, “selecting an information architecture is difficult” (Dickson and Wetherbe, p. 122). Yet, the architectural requirements of the MIS manager in the 1990s surpass the basic information architecture described above. What is needed is an “Enterprise Architecture” that is a dynamic information technology foundation that provides a direction for the deployment and integration of future technological and managerial developments.

This paper describes one organization's process of establishing a principles-based information technology (IT) architecture. The paper focuses on what we define as an “Enterprise Architecture.” This architecture defines and interrelates data, hardware, software, and communications resources, as well as the supporting organization required to maintain the overall physical structure required by the architecture.

From basic design tenets, the paper outlines the architectural models developed for Star Enterprise, a joint oil refining and marketing venture between Texaco Inc. and the Saudi Arabian Oil Company. Particular emphasis in the paper is on two aspects associated with developing the architecture. The first is a precursor—principles upon which the architecture is being based. The second is an antecedent—lessons learned from the process undertaken thus far and issues considered to be of key importance. It is the thesis of this paper that the lessons learned and the principles underlying the development of the architecture are applicable to a large segment of the information technology arena and to other environments and organizations.

## Background

Texaco Inc. was founded in 1902. It is the third largest oil company in the U.S., having 37,000 employees and \$36 billion in revenues in 1989. Texaco Inc. entered into a joint venture partnership with the Saudi Arabian Oil Company (Saudi Aramco) to form Star Enterprise in 1988. Star Enterprise, which had 1989 revenues of approximately \$6.5 billion and 4,000 employees, refines and markets petroleum products in 26 states in the eastern and Gulf Coast regions of the U.S.

Texaco Inc. is supported by the Information Technology Department (ITD), which provides large-scale data and scientific processing. ITD also maintains a corporate data repository and provides telecommunications services (both voice and data), technology research, and a human resources function for all information technology (IT) professionals throughout the company. An important ITD function is to maintain the global IT architecture for the company. The IT function in Star Enterprise is similar to the central Texaco Inc. ITD function except that it does not operate its own large-scale computing and telecommunications complex.

Originally, the Texaco U.S.A. organization, a division of Texaco Inc., was structured as shown in Figure 1. The U.S. refining and marketing of petroleum products was organized geographically. With the Star Enterprise joint venture, what appears in Figure 1 as the “Eastern Region” is the geographic area that now constitutes Star Enterprise. Initial talks to form the joint venture began in late 1987, and the organization became fully operational on January 1, 1989. In the summer of 1988, Star Enterprise headquarters personnel moved into a new six-story building located in Houston, Texas. Part of this staff consisted of four IT personnel. One of their major activities early on was to develop an Enterprise Information Technology Architecture for Star Enterprise.

Even prior to its formal creation, Star Enterprise identified the need to develop an enterprise architecture that would describe the current information processing environment as well as provide a model for deploying future information technologies. Since Star Enterprise was formed from an existing set of refining, distribution, and marketing units, it did not fit the typical startup effort that would normally evolve to maturity over many years of operation. Figure 2 shows the business functions of Star Enterprise and gives some indication of the information processing systems supporting these functions.

The field components of Star Enterprise were mature at its inception. However, the headquarters function was carved out of an existing Texaco contingent and was moved to the new facility over a five-month period. The Star Enterprise headquarters staff consisted of the typical cross-section functional specialties such as: planning, legal, controllers, finance, information technology, marketing, and other similar staff groups. The problem faced by the IT planners was to effectively support the changed business and to take advantage of new technologies while integrating them with those already in place. Several factors made this process difficult including:

![](/api/attachments/ZK8JRE8S/fulltext/images/f50c5200dd55283e7c74a86af6607f904b05464f5b70cc66a028db59b7a36864.jpg)  
Figure 1. Texaco U.S.A. and Star Enterprise

1. A new organizational structure;

2. The physical move to a new headquarters building;

3. The transition when many information technologies were “exploding,” personal computers and local area networks in particular; and

4. An existing base of technology that was incompatible and non-integrated.

Because the base of technology in place at the end of 1987 is so related to the story we are telling, a brief description is in order. Support for the point made above about incompatibility and non-integration is demonstrated by listing features of the IT environment supporting Star Enterprise at its inception.

1. Systems Running on a Variety of Hardware Platforms

— Financial Date Capture System—Datapoint

— Financial/Marketing System—IBM Mainframe

— Refining—Data General

— Automated Marketing System (service station support)—Tandem

— Marketing Region Database Server—IBM RT (using AIX and Oracle)

2. Terminal Systems Available to End Users — Many “dumb” terminals

— Many PCs (IBM and Compaq)

— Standalone, multiple independent LANs

3. Software Incompatibility

— Many different menu systems

— Standard end-user software (word processing, spreadsheets, graphics), but not well integrated

4. Applications Systems and Data Incompatibility
— Data Acquisition System (Fortran based)
— Sales Terminal Control + Pricing/Invoicing (COBOL)

![](/api/attachments/ZK8JRE8S/fulltext/images/7a9e02f1e63b9bb73b26a685fda9e247b85da2afbc9e366b720accd8294f6497.jpg)  
Figure 2. Star Enterprise Business Functions and Related Supporting Information Systems

— Automated Terminal Operations (Data General)

— Automated Marketing System (Tandem)

Given these conditions, the IT staff at Star Enterprise began to engineer a future information systems architecture. A key step in this process was to look for a framework on which to base the architecture. The framework adopted was based upon thoughts provided by Michael Hammer in a presentation to the Texaco Information Technology Conference in 1989 (see Hammer, 1986 and Hammer and Magurian, 1987). Hammer believes that a physical information architecture is a manifestation of beliefs or principles of the organization's leadership. Based upon these notions, a set of “principles” were set forth as a foundation for the Star Enterprise architecture.

Historically, as we have presented, the beliefs (or principles) were not formally stated, and implementation of technology was haphazard and uncoordinated, resulting in the information architecture that was inherited. As will be seen, the principles underlying Star Enterprises's move to a new information technology architecture are founded on the notion of a business orientation that seeks to apply information technology for competitive advantage. The enterprise architecture that is emerging based upon these principles is much better integrated and flexible than the one in place at the time of formation of Star Enterprise.

## Principles for an Information Technology Architecture

The environment in which Star Enterprise exists is changing at an accelerating pace. Market conditions, crude prices, environmental concerns, and new technology are changing faster than ever before. In addition to these conditions, we have the formation of the new company (Star Enterprise) with decentralization of authority. Under these circumstances, it is no surprise that in the area of information technology, there is much uncertainty and people going in different directions. Vendor and product proliferation, incompatible systems, difficulties in sharing information systems and data, and general uncertainty about how to evaluate choices also add to the state of confusion. The information architecture toward which we are moving attempts to provide a sense of structure and order into our constantly changing environment.

An enterprise information technology architecture at Star Enterprise is a set of long-term, consensus-based criteria for evaluating and managing information technology that will persist in the face of change. It is a mechanism for identifying and resolving conflicts and building consensus on technology directions and strategies. An architecture, however, should not be viewed as a formal constrictive solution to all technology problems. Given the current state of technology, it is necessary to try to achieve a high degree of consistency in the architecture. Failure to achieve this objective will perpetuate the islands of automation that historically plagued the architectural scene. Achievement of this goal is difficult given the diversity of opinion regarding what constitutes a correct architecture. It is our opinion that a homogeneous architecture throughout the enterprise will aid in achieving the following goals: improved information flow among entities, reduced support costs for overall system, and portability of software from one segment to another.

Our proposed architecture can be classified into four general area types: principles, inventory, models, and standards. Principles are an organization's basic philosophies that guide the development of the architecture. Inventory is a catalog of what is in place today. Models are pictures of a desired future state—what goes where and how connection takes place. Standards are specific rules or guidelines for implementing the models. This paper focuses on the area of principles for an information technology architecture at Star Enterprise.

Of all four areas, principles have the most far-reaching and significant impact on an organization because they are the most stable element of an architecture. Principles provide guidelines and rationales for the constant examination and re-evaluation of technology plans. The principles outlined in this paper were initially derived from an intensive three-day discussion with senior IT management, then validated in discussions with the IT Steering Committee. These principles are viewed as a starting point for subsequent decisions that affect the architecture. In this mode, principles form the rational basis for coming to an architectural decision.

Each of the architectural principles in place at Star Enterprise is presented below. The principles cover four areas: organization, applications, data, and infrastructure. In addition to presenting the principles, we give a rationale for each and state the practical implications that result from the principle.

## Organization

## Principle 1

All information technology professionals in each business unit will need to report either directly or indirectly to the person responsible for the information technology function at that business unit.

## Rationale

Escalating technological changes and business unit autonomy will increase the need for continuity and consistency across the information technology functions.

## Implications

1. Substantial cooperation and coordination will be required among all information technology professionals in the business unit.

2. Information technology management will be responsible for, but not limited to:

— Communicating, updating, and compliance of the Star Enterprise Architecture

— Human resource issues

\- Salary consistency

• Career path planning

— New technology dissemination

— Coordination between business units

## Principle 2

Star Enterprise information technology areas will need to collaborate to provide the best service in application development and support, and to eliminate artificial internal competition.

## Rationale

The organization working on the application should ideally be the one closest to the business problem. Collaboration eliminates artificial competition and safeguards overall company interest.

## Implication

1. When seeking application development or support, information technology areas should be contracted in the following order:

— Internal to business units

— Business services

— Other information technology groups in the company

— External sources

## Principle 3

The information technology function in the business unit must be organized to make the most effective use of information technology as a strategic tool.

## Rationale

The application of technology to business solutions demands a thorough knowledge of the business and its directions. Information technology professionals should have a business unit-wide perspective to most effectively exploit technology across the entire business unit.

## Implications

1. Information technology professionals must acquire extensive business knowledge. This is viewed as a time-consuming process.

2. Information technology professionals must play an integral part in the decision-making process.

3. Every business unit should have a person responsible for information technology as part of the top management team of that organization.

4. Information technology management will be responsible for, but not limited to:

— Communication, updating, and compliance of the Star Enterprise architecture — Human resource issues

\- Salary consistency

• Career path planning

— New technology dissemination

## Principle 4

Star Enterprise professionals will need to acquire the necessary skills to effectively utilize and exploit information technology as a strategic tool for the business.

## Rationale

The increased proliferation of computers, information systems, and technology will demand heightened computer skills for all Star Enterprise professionals to maximize the entire organization's performance. The rate of technological change will further increase this demand for education.

## Implications

1. Information technology professionals will be responsible for increasing technology awareness among business unit employees.

2. As more training is required for Star Enterprise professionals, more time will be taken away from their jobs. As a result, training should be more efficient and effective.

3. Applications need to be designed to require as little training as possible.

4. Information technology professionals will be responsible for increasing their own business awareness.

## Applications

## Principle 1

Information systems planning needs to be an integral part of the strategic business planning process.

## Rationale

The business environment is characterized by increased competition, fluctuating margins, unstable markets, and compressed windows of opportunity. In order to continue to compete and exploit the small windows of opportunity for competitive advantage, it is vital that the information systems planning function be fully integrated with the business strategic planning process.

## Implications

1. Information technology professionals will be more proactive in the planning process than in the past.

2. An integrated process will ensure the alignment of the information systems plan with the business plan.

3. Information technology professionals will enhance competitiveness by applying technology to new business opportunities and by creating new business opportunities through innovative technology.

4. Information technology will be assimilated into Star Enterprise much more rapidly.

## Principle 2

Information systems will need to be developed using formal planning and software engineering methodologies.

## Rationale

Star Enterprise wishes to implement, in a timely manner, quality information systems that are closely aligned with business objectives. The existence of formal information system planning and engineering methodologies will support this goal by providing an environment that facilitates communication and decision making between information technology and business unit professionals. This structured environment will provide for systematic review of the application's ability to meet business unit functionality and feasibility requirements, as well as its use of appropriate technology to maintain compatibility with other applications. This review will ensure more flexible and resilient systems that will minimize long-term cost of maintaining the application.

## Implications

1. There will be a need to invest in developing or acquiring systems tools to support methodologies.

2. Application and business staff will need to be trained in these methodologies and tools.

3. Application developers will object to being constrained by standard methodologies.

4. Existing systems and externally acquired packages may not conform to these methodologies and will require special treatment.

5. Rationale will need to be developed to determine which systems may deviate from these standards.

6. Prototyping may be used within the methodology but not as a replacement for the methodology.

7. If the breakthrough strategy methodology is used (locating and immediately starting, results-focused projects that provide opportunities for introducing new management methods, new technologies and new tools and systems into companies by deliberately exploiting the forces that are unleashed during performance-improving crisis situations), it must be understood that the timing constraint should not result in unsound business practice.

## Principle 3

Successful projects require proactive user and sponsor involvement to ensure proper functionality and ultimate business success.

## Rationale

The ultimate responsibility and reward for an investment in an information system must rest with the sponsors who invest in the project. The business success and functionality of the application will be reflected by the willingness of customers to pay for the application. The sponsors will be judged by the return measured in benefits to the using organization or revenue streams from other business units or external customer.

## Implications

1. The business unit will provide the sponsor.

2. The appropriate manpower resources and multi-functional skills from different parts of the organization must be brought together as a project team in a timely manner to ensure the success of the development effort.

## Principle 4

Information systems need to be developed to facilitate their portability across various hardware and software systems.

## Rationale

Developing portable information systems will allow Star Enterprise greater flexibility in hardware and vendor selection, encouraging increased vendor competitiveness and resulting in lower costs. It will further facilitate migration to new technologies that are less costly or more effective in supporting evolving business strategies and organizations. This strategy will effectively remove hardware obsolescence or vendor demise as a requirement for costly application re-engineering projects. The approach will allow more flexible use of developmental programming staff and minimize training costs and requirements.

## Implications

1. At this time, there is no computing industry standard or supporting tools for this principle. Interim strategies will have to be established to place Star Enterprise in a position to implement this principle in a timely manner.

2. Information systems development costs may be higher.

3. Vendor and hardware selection will be made later in the project life cycles, enabling less costly investments.

4. In order to provide portability, developers will have to avoid incorporating vendors' proprietary functions into information systems.

## Principle 5

Information systems will need to be periodically reviewed to ensure that they continue to meet the business needs and to avoid technological obsolescence.

## Rationale

The rapidly changing external business and technical environments are forcing significant changes within Star Enterprise. These changes will require an on-going evaluation process to protect the major investment in information systems by keeping them current with the changing environment.

## Implications

1. Reassessment should be led by personnel in the affected business unit with information technology personnel participation.

2. Reassessment may cause additional investment to realign the system to the business needs.

3. Reassessment must also recognize that technology may force changes even if the business requirements are being met by the existing system.

4. Revisions may be more costly than redevelopment.

## Principle 6

Ease of use will be enhanced through information systems that present a consistent appearance to the systems users.

## Rationale

A common user interface is becoming an increasingly important business need. As functionality is increased, cost for training, design, and support can be reduced by presenting a consistent, recognizable interface. This will also enhance the efficiency of the user, while allowing the maximum utilization of information technology resources. Standard interfaces will improve productivity for both the designer and the user.

## Implications

1. Retrofitting of common interfaces into existing or purchased systems may be costly and should be evaluated on a system-by-system basis.

2. Initial training may be costly, but subsequent training should be significantly reduced.

3. Training for occasionally used information systems will be reinforced by consistency of interfaces with more frequently used information systems.

4. Information technology personnel may feel constrained by predetermined design criteria.

5. Standard interfaces will allow more time to be spent on business problems rather than the mechanics of the computer interface.

6. Interface standards will need to be developed and utilized throughout the corporation.

## Principle 7

When determining information systems solutions, the preferred order of selection should be an existing system, a purchased application package, in-house development, then outside services.

## Rationale

When information systems are developed to take advantage of competitive situations, all solutions need to be evaluated with respect to cost, speed, business functionality, synergy, and standardization. No single implementation option can satisfy all the competitive design criteria.

## Implications

1. Management must be prepared to accept less than 100 percent automated solutions.

2. Full compliance with architectural plans may be at additional cost.

3. Compliance with architectural plans will enhance long-term viability.

4. Purchased packages generally will not fit all aspects of the architectural plans.

5. Solution sharing across business units will reduce costs and increase synergy, but may result in compromise.

6. Use of existing information systems for new business opportunities will enhance the value of the information systems to Star Enterprise.

## Principle 8

Information systems need to be managed as an asset. Sponsorship and licensor privileges must be arranged at the time of the development or acquisition of the information system.

## Rationale

Star Enterprise assets are created by investment and management strategies, and the performance of the owner or custodian of the asset is judged by the rate of return generated by the asset. A similar rationale should be operative for sponsors of information systems development projects. Those sponsors of successful applications should be able to receive licensing revenue from other non-sponsors as a reward for undertaking the risk of sponsorship. Business units should not be permitted to avoid risk by receiving “free” software from the initiative of other business units.

## Implications

1. A criterion has to be established concerning the sale of strategic information systems to outsiders.

2. Ownership of multi-user information systems prior to the existence of Star Enterprise must be established.

3. Royalties and commissions must be negotiated and accounting procedures established to facilitate the sale of information systems.

4. It must be determined what deliverables and support will be provided to the licensee.

## Data

## Principle 1

Data needs should be viewed as a corporate asset and be managed as such.

## Rationale

Data is a measurement of a business activity at a point in time. A collection of data can be aggregated and transformed into information and, ultimately, into knowledge about the dynamics of a business situation. This understanding can create competitive advantage, where a business unit will have an opportunity to effectively exploit the situation to achieve maximum profit realization.

## Implications

1. Data management responsibilities must be clearly defined to guarantee effective utilization of information throughout the corporation.

2. Sufficient resources, including manpower, equipment, and software need to be applied to the data management functions in order to ensure the realization of positive benefits from data utilization.

3. A set of data management procedures needs to be developed and should be utilized throughout the corporation.

4. A data training curriculum needs to be developed and should be utilized to educate personnel at all levels and areas of company operations.

5. The Star Enterprise Information Technology Steering Committee (composed of Star Enterprise senior management, including the CEO, COO, CFO, and the director of Information Technology) will periodically review the data management activities and will recommend any strategic adjustments that will improve the overall process.

## Principle 2

Enterprise data plans need to be developed and maintained independently of applications and storage technology.

## Rationale

In order to maximize the effectiveness of information utilization throughout the corporation, a comprehensive process for defining, constructing, installing, and managing data needs to be developed and utilized. As part of this process, a set of data plans needs to be developed independently of information systems. These plans, if they have been constructed and implemented in a consistent manner, will allow for the utilization of data by wider audiences. The process, which will create the potential for greater compatibility between applications and databases, will also facilitate the portability of applications.

## Implications

1. Data planning will be an integral part of business planning, and will therefore require a cooperative effort between business unit managers and information technology managers.

2. Corporate information technology personnel will have the overall responsibility for coordinating the data planning procedures. This activity will undoubtedly require significant resources.

3. A set of data-related conventions and standards will need to be developed and adhered to for the storage and sharing of data.

4. Each business unit will be responsible for developing data plans that reflect their unique characteristics within the unit's business environment.

5. Data plans will be vertically consistent within the corporation.

6. Data plans will be developed independently from applications, but will be utilized as an integral part of the application planning process.

## Principle 3

The user of the application is responsible for the content and consistency of the data.

## Rationale

In order to guarantee that data is available in a timely and accurate form, it should be captured and validated once, at its source. The capturing entity should be responsible for the accuracy of the data and its consistency with data being captured by other entities within the organization. This will allow the data to flow upward within the organization and be utilized as useful information at each level as well as across organizational boundaries.

## Implications

1. Source data capture will minimize data redundancy, which will result in lower data capture costs and reduced data reconciliation requirements.

2. Uniform data definitions will need to be developed and communicated throughout the organization.

3. Multiple review and validation processes to correct data should be eliminated.

4. The costs associated with data capturing will be absorbed by the data capturing entity.

5. The capturing entity may be required to capture data for which it has no immediate need when the data is needed to satisfy other business unit requirements.

## Principle 4

The steward of the application is responsible for the security of the data.

## Rationale

Improper access to or use of data can have many adverse business consequences. Therefore, access to the data needs to be controlled. Because access to data is most easily accomplished from applications, the steward of the application is in the best position to guarantee the integrity of the database.

## Implications

1. The steward needs to ensure that adequate but timely security is provided within the application set in the area of responsibility.

2. The degree of complexity of the security procedures can adversely affect timely access to the data.

3. The need for data security, as well as the benefits of that effort, should be emphasized throughout the corporation.

4. Data security procedures should be periodically reviewed by the Star Enterprise Information Technology Council.

A model-based infrastructure architecture is required to facilitate information system development and data sharing.

## Infrastructure

## Principle 1

An infrastructure modeling approach facilitates a more rigorous analysis of the overall information architecture. In a highly competitive environment, we must find more effective techniques for the evaluation and communication of the information architecture. Infrastructure modeling represents an engineering-based approach for blueprinting and analysis of information system architecture prior to actual construction. Infrastructure model consistency supports increased use of a compatible development tool set and improves portability of personnel, data, and applications across various components of the architecture.

## Rationale

3. Partnerships with strategic suppliers will need to be used to engineer future models (i.e., “technology gaps”).

## Implications

1. Architectural models for the information infrastructure will need to be developed and communicated.

4. It will be necessary to develop customized discrete models for plants, marketing, headquarters, and other functional entities, such that the total organization's infrastructure can efficiently and effectively meet global business requirements.

2. The infrastructure modeling process will require an interactive activity between various interested parties (i.e., users, management, suppliers, etc.).

5. Infrastructure models will be used to facilitate an improved level of communication regarding the complexity and capabilities of the present and future information architecture.

6. Well-conceived infrastructure models will need to be established to accommodate faster development cycles.

## Principle 2

Star Enterprise needs to achieve a high level of connectivity and compatibility among all hardware, software, and communication components.

## Rationale

A formalized, well integrated, and coherent infrastructure is desirable to support the operational needs of the organization. This strategy allows increased focus on business function rather than underlying technologies. Individuals will find it easier to share data, which will facilitate effective operational decision making. This kind of infrastructure will shorten application development cycles and decrease subsequent support costs. A single system image can be provided to the user, which has positive implications on training and total system cost.

## Implications

1. It will be necessary to subsidize selected emerging technology in order to influence the evolutionary directions of the infrastructure.

2. The supplier selection process will become critical in maintaining consistent infrastructure.

3. This strategy will require a high degree of coordination and collaboration among all business units.

4. The cost of computing will probably increase significantly when deviating from a common infrastructure.

## Current Status

Recall that the transition to the joint venture, Star Enterprise, began in late 1987. Because of the information systems opportunity created by the new organization and the nature of the information technology and applications in place at the time of the change, the ITD staff was presented an opportunity but also a number of difficult challenges. Two basic approaches were taken that served as the foundation for the evolution of information systems for Star Enterprise based upon an enterprise architecture.

One basis was the development of the principles that have just been presented. The second basis was to begin to deal with specific immediate hardware and software issues in a way that would be consistent with the architecture that was evolving. Keep in mind that, as of this writing, the evolutionary process has only been underway for about two years. Naturally, progress has been affected by the practical every day concerns associated with setting up a fundamentally changed business entity.

Regarding the development of the principles that underlie the architecture, the reader should note that in many instances, there is wording such as: "will need to be developed," and "should be led by." Such wording indicates that the principles have been articulated, but their full implementation has only just begun. After the first step of developing the principles, much work has been undertaken to gain managerial consensus for them.

The formation of the aforementioned IT Steering Committee was one formal step in this direction. Gaining the approval from this group for the general approach of the architectural principles was one method of consensus in building and in beginning their implementation. The current status of the architectural principles is that they have been approved in general and are being refined to provide a lower level of detail than presented in this paper. In addition, the principles have been used (where applicable and fully enough defined) to support the physical representation of the information systems architecture that is beginning to emerge at Star Enterprise.

Naturally, there are a large number of constraints that must be overcome to achieve full implementation of an information systems architecture. To name just a few: (1) the inherited technological environment that existed at the initiation of the process, (2) new technologies constantly emerging that must be accommodated, (3) immediate concerns such as providing information technology support for a new headquarters building, and (4) the fact that any information systems architecture is always in transition and ever changing and evolving.

Given these constraints, the information technology staff at Star Enterprise have attempted to form an architecture that is as faithful to the principles as possible. The current status of the architecture is summarized in Figure 3. The major components of the enterprise architecture are subarchitectures for: (1) the network, (2) data, (3) languages, (4) office support, and (5) processors. Examination of Figure 3 indicates a few of the details of the current implementation and some of the current thinking regarding future considerations.

Naturally, some of the sections of the architecture are more fully developed than are others. Existing conditions, current needs, ease of implementation, and business priorities have had an important effect on the present status. To illustrate the architecture, we used the network architecture model as an example since it is further along than some others.

## Enterprise network architecture

The enterprise network model is the blueprint that describes the planned connectivity of workstations and servers throughout the organization. Figure 4 shows a high-level overview of the building and refinery networks and their associated resources interconnected to the enterprise backbone. All resources, whether located on the enterprise backbone or in the local building or campus, are viewed as peer processing nodes. Current thinking is that some nodes may have special features such as large quantities of memory not found on other nodes because of cost, but are nonetheless treated as peer nodes.

## Headquarters Building Model

A central computer/communication room in the Headquarters facility houses all file and database servers, bridges, and gateways. Print and plot servers are distributed throughout the user community for ease of access. In addition to each office being wired, the conference rooms are wired with multiple connections. This arrangement allows a user to develop a presentation on an office workstation and store it on the file server. Then, when making a presentation in a conference room there is access to the file server where the “slide show” is stored. This type of connectivity facilitates sharing of non-traditional information objects such as: “slide shows,” spreadsheets, and documents. The Headquarters building model is also being applied in other Star Enterprise building sites (e.g., marketing and refining sites).

![](/api/attachments/ZK8JRE8S/fulltext/images/ca165b69035a2f0289ea6629a2b7fb720ca49cfd3036b4708b2fc3b60315b439.jpg)  
Figure 3. Star Enterprise Information System Architecture

In the future, plans are to implement higher-speed networks such as LANs from 16 to 100 Mbps. The enterprise backbone is anticipated to move from 56Kbps to T1 and T3 carrier speeds as applications such as video conferencing emerge. Applications that incorporate more complex objects such as integrated voice, graphics, text, and video will likely require fiber optic technology.

## Refinery Model

The refinery model is comprised of building networks interconnected to a refinery backbone. The administration building model is the same as described in Figure 4 in that there is a high-density population and the users do similar things to users in other office locations, i.e., electronic mail, word processing, spreadsheets, graphics, etc. The process control buildings house the process automation equipment, which has linkages to the physical process units. The process unit buildings typically office a very small number of people, but there are frequently more of these types of buildings than the administrative type.

## Chronology of the Implementation

As of this writing considerable progress has been made toward implementation of the architecture. Activity has been undertaken at the headquarters of Star Enterprise, in the marketing regions, at three refinery locations, and at the retail outlet level. Some of the specifics of the implementation are detailed below. These specifics note, in some cases, activity that is particularly related to the principles we have set forth.

![](/api/attachments/ZK8JRE8S/fulltext/images/82492e2e4441909b707cf373777265cc3b9d1e2815fd3f3defb684c534775089.jpg)  
Figure 4. Enterprise Network Model

LEGEND
IWS = Intelligent
Workstation
DB = Database
Email = Electronic Mail
G = Gateway
X = Unknown

## Headquarters

1989 Building LAN completed
mid-1990 Prototype large database server installation

Marketing Regions

mid-1989 LAN-based environment in four marketing regions

early-1990 Major effort to improve performance of servers and to improve data quality (see principles regarding data capture)

mid-1990 Attachment for lap-top computers to data architecture

late-1990 Install 3rd party retail accounting system and integrate into LAN architecture (see principles on systems acquisition)

late-1990 Install enterprise bridges

1989 Acceptance of architecture based on the use of relational database technology and LANs (away from total reliance on minicomputers)

1990 Pilot efforts to construct LANs connected to local relational data repositories.

late-1990 Install enterprise bridges

## Retail Outlets

late-1989 Install PC-based retail accounting system to assist local management in operation of convenience stores dispensing gasoline

late-1990 Develop conceptual architectural model of future retail outlets

Bulk Plants

mid-1990 Feasibility study for re-systemization

late-1990 Formal requirements analysis (four major business processes)

## Lessons Learned/Issues of Concern

Throughout the process of developing an enterprise information system architecture for Star Enterprise, there has been an increasing awareness of various aspects of important aspects of our effort to apply a coherent architectural strategy. We believe that what has been learned may be of use to others as they consider such an effort and we would like to pass on some of our impressions.

Overall, we have learned several major lessons thus far. These include:

1. An emphasis and focus on any technical area will likely increase the general understanding of that area.

2. Consistency in architectural design has a great potential to improve the overall synergy of technical support and the mobility of software resources throughout the information network.

3. As the process was begun, architectural concerns were often not considered by the user community to be of great importance.

4. Later, however, the real value of architectural design (and the development of principles underlying the design) became recognized across a reasonable subset of the technical and managerial population as an activity that is necessary to achieve strategic company goals.

5. The fundamental importance of developing and gaining consensus for underlying architectural principles has become recognized as paramount in the success of the process.

Six other, more detailed, lessons learned from our activity that may be useful to others include:

(1) Connectivity. During the early phases of the effort, the word architecture was synonymous with connectivity. When pressed, most inindividuals would define connectivity as the ability to move data from one place to another with minimal effort. The early vision in many cases was a file transfer system. As time passed, this vision expanded in many ways. If asked today, most of the technical personnel would define connectivity as an ability to dynamically fetch data by an application running in one node with data residing in another node. Some are now beginning to envision a complete cooperative distribution of the various resources in the system. A cooperative environment is defined here as applications nodes fetching data from one or more nodes in response to a user who may be in yet a third location. These changing views regarding what is involved in connectivity were primarily stimulated from the increased focus on architecture.

Another comment frequently made early in the effort was that connectivity from one business operation to another was not of great value. However, as the level of connectivity improved between the nodes, most of these “island” attitudes seemed to moderate and were recognized as worthwhile reasons for improved information flow between the various units of the organization.

The value of operational synergy between the information architectural nodes is difficult to quantify but is a very real result of the design effort. Assuming that some degree of consistency can be realized between the nodes, the movement of technical personnel between locations is much easier. Also, software products can be more easily shared among distributed locations. In contrast to this state, the “island design” philosophy would almost assuredly mean that a product created in one area would not operate well or at all in a second location (see the applications principle addressing this issue). So, a consistent connectivity and architectural plan has significant impact on the operational strategy for the firm as well.

(2) Sunrise Technology. Computer professionals must be an honest breed at heart. Otherwise, how do we explain their continuing belief that a newly promised item of technology will perform exactly as a vendor's salesperson promises. We refer to this phenomenon as “sunrise technology” because there is the frequent belief that a new capability will roar into the sunlight fully functional. In the instance of implementing the enterprise information systems architecture, there has been a bias toward pushing the technology envelope in the use of LANs and client server functions well beyond anything that has been previously installed within the organization. Certainly, one of the serious issues to be wrestled with in any computer-related activity is the level of technical risk to be taken.

On the one hand, it seems obvious that the best strategy is to move slowly until everything has been extensively tested in a laboratory environment. However, the user community will often push new technologies to the point where the IT organization must either install what the user wants or they (the user) will do it themselves. In concert with this condition, information technology is moving so rapidly that a leisurely implementation rate is seldom feasible. So, two basic factors make grasping for fully mature technology solutions the norm. A key lesson we have learned is that it often takes as long to implement the last two percent of a particular project as it does to implement the first 98 percent. Unfortunately, overall functionality is often constrained until that last technology piece is complete.

As our architecture continues to migrate toward the distributed data, client-server model form of operation, the technology gaps will be very noticeable and disruptive during the implementation cycle. Another important lesson is to be aware that the timing of small key technologies can greatly influence the success of large architectures and their related products. Attention to small details is very important to this process.

(3) Positioning Strategy. Movement from one architectural phase to another is a very complex issue. It is much more complex than simply bringing in a new vendor. As indicated earlier, the current trends in our architectural direction are toward higher levels of connectivity and functionality. True, the current movement in the industry is toward more “open” strategies, but if this ever occurs in reality, the building block approach to implementation will be a viable strategy. Today, this is not the case, and architectural phases tend to be step-level jumps with noticeable discontinuities between the levels.

Certainly, one of the key decision processes involved with architectural planning is the need to have a future target. Shorter term goals can then be defined as stepping stones to the strategic goal. Of course the problem here, again, is that historically, information technologists have not been all that accurate in predicting product directions and timing. For example, who would have predicted in 1980 the impact that PCs would have on the industry? This does suggest that more effort is required to assess the relevant technology and to learn how to make better forecasts on arrival schedules for the selected targets. Errors in major product forecast direction will likely cause a perturbation in the future architectural model. Even with good predictions, the technology itself may not have a smooth migration path. Bridging these discontinuities may require a multi-year transition plan during which time the architecture will be a hybrid of each phase.

(4) Data. Modern architectures are going to require a much more sophisticated view of data than earlier central-site type implementations. One advantage of an “island of automation” is that one can basically ignore everything outside of the island. This is not so with an integrated architecture. A client-server-based architecture has data distributed throughout the network. In this mode of operation, it will be necessary to have more rigorous control over the definition, compatibility, and physical format of the various data repositories. Most modern data repositories are relational-based, but future designs will need to deal with object-oriented concepts as well as the broadening definition of data. By the year 2000, it is likely that data will consist of not only traditional numbers and text, but will also include graphs, images, knowledge bases, voice, and possibly other forms of information. Many organizations today are just beginning to make the move from more traditional storage positions. This means that the data migration process from old techniques to newer ones will be noticeable for much of the nineties.

A second data-related problem is anticipated when production-distributed databases become an operational reality. Currently, very few organizations have begun to consider how one might approach the recovery of two synchronized data repositories when one fails during an update. Data integrity concepts in such an environment will be complex.

The lesson learned here is that the distribution of data does not yield a more simplified operational world. It will be a struggle to keep the levels of integrity, recoverability, and security to acceptable levels when compared to the current central site model of operation. The computer hackers are already beginning to show us how painful this process can become. In the last few years, we have begun to understand what the term “virus” means in the computer domain. Likewise, we will become much more aware of other technical issues related to database technology as the physical repositories become more distributed.

(5) Application Strategy. During much of the eighties, the user community became much more “hands on.” This trend is continuing and the quality of end-user tools is now quite impressive. As information technology is distributed across the organization, we will see significant changes in the application development process. On the one hand, we are observing the emergence of CASE tools that hold the promise of improving the development process. On the other hand, new generations of utilities are being offered that make the coding process amenable to non-computer professionals. Although it is not easy to make a firm prediction on exactly how the application strategy is going to change, it is predictable that it will stay in flux for much of the upcoming decade. The drama that is yet to be played out is to find the degree to which procedural language processes can be simplified and taught to end users. If this can be achieved, then the professional IT staff will be primarily responsible for constructing data repositories, training end users, performing network tasks, planning architectures, maintaining existing older applications, and other work of this type.

The application lesson learned in our case is that it is difficult to keep a consistent development strategy intact at the same time that the network architecture, database management strategy, and tools are being defined. Here again, we observe that our pace of change has been too rapid to be assimilated properly.

(6) Security and Data Integrity. This topic was touched upon under the data topic, but more deserves mention. Security, data integrity, and recovery are words that have been used for some time to imply a degree of quality that a set of application systems and their related network infrastructure should possess. Central site systems have achieved reasonable levels of these attributes by tight physical and organization control. Once the central site was pierced with minicomputers, and later with personal computers, the issue has re-emerged. Unfortunately, these concepts are less well-handled in the case of mini and microcomputers than in the tightly integrated architecture present with central site computing.

Personal computers and their associated LANs have a degree of security, integrity, and recovery; but really this is the Achilles heel of a modern architecture. Because smaller machines have less secure operational environments, it is absolutely mandatory that security and recovery become a greater concern to the IT organization. The meaning of data integrity is also appearing to change. In previous times, there were attempts to build certain controls and procedures into systems that were felt to improve the data integrity. Now, with the ability to change data easily and without tight control, it is necessary that the user community rethink the issue.

Implicit in our observation is the increasing recognition that computers are becoming so embedded into the work flow process that one has a difficult time separating them from the process itself. If the computer goes down, so too does the process. So, not only are we struggling for reliable procedures for recovery and faulty hardware and software systems, but we are recognizing that the work will stop if we cannot find a better way to recover from the event. The lesson learned here is a complex one. We suggest that this area will become more of a concern than in the past. Innovative solutions are needed in this area to decrease its significance in our future operational activities.

## Conclusion

Star Enterprise is a relatively new venture that was formed from the assets of Texaco U.S.A. The new organization inherited resources from that organization, including a set of information systems applications and an information systems architecture. The latter was notable for its lack of integration and its plethora of incompatible hardware and software systems.

The ITD staff assigned to Star Enterprise took the creation of the new company and its move to a new headquarters building as an opportunity to develop a new “enterprise” information system architecture. A significant early stage in this effort was the creation of a set of principles upon which the architecture would be based. In this paper, we have articulated the principles and have presented an overview of the current vision of the resulting architecture. In addition, we have provided more depth on one part of the architecture—dealing with the interconnectivity of resources (the network). Finally, we have highlighted a few of what the authors believe are lessons learned from the activity thus far associated with implementing the architecture and issues that are currently felt to be of major importance.

Although formal assessment of the exercise that is the subject of this paper is difficult, we can provide some evidence that there is progress. We submit the following:

1. Star Enterprise user groups have requested more training in order to make full use of the information technology they are being provided.

2. Use of the central software library has increased substantially since implementation of the first stages of the architecture.

3. Support costs have been reduced for two reasons: (1) the creation of a common menu system, and (2) software located on the central server and supported by the information technology group.

4. Users share more data compared to the previous situation in which there was either no LAN or no centralized LAN support.

5. The total cost per workstation (including hardware, software, LAN, storage, and maintenance) in the new environment is \$7,500, which is less than half the cost suggested by a prior study.

The Star Enterprise senior management and IT staff are pleased with the progress to date in providing an enhanced information technology infrastructure. Yet, even with the progress made to date, everyone realizes that much remains to be done and that significant challenges must still be faced. The start made, coupled with principles in place to support future evolution, is encouraging. Experiences from this effort have led us to reach the following three conclusions. First, a principles-derived architecture is a long-term process, not a single event. Second, being consistent throughout the enterprise architecture is more important than individual groups searching for local solutions. This raises unresolved organizational questions regarding how to achieve this type of consistency. Third, time must be spent building consensus among technical staff and communicating derived principles throughout the organization.

It is our aspiration that sharing these experiences and providing a sample of the principles we have developed to support the development of an enterprise information systems architecture will prove of value to others as they embark on a similar adventure.

## Acknowledgement

We would like to acknowledge our appreciation to Jeff Clark for his art work.

## References

Dickson, G.W. and Wetherbe, J.C. The Management of Information Systems, McGraw-Hill, New York, NY, 1985.

Emery, J. Executive Overview to: “Integrating Islands of Automation,” MIS Quarterly (13:4), December 1989, p. 432.

Hale, D.P., Haseman, W.D. and Groom, F. “Integrating Islands of Automation,” MIS Quarterly (13:4), December 1989, pp. 433-436.

Hammer, M. “Dispersion and Interconnection: Approaches to Distributed Systems Architecture,” PRISM (Partnership for Research in Information Systems Management) Final Report, Index Group, Inc. and Hammer and Company, Cambridge, MA, 1986.

Hammer, M. and Mangurian, G.E. “The Changing Value of Communications Technology,” Sloan Management Review (28:4), Winter 1987, pp. 65-71.

Jackson, B., Butler, C.W. and Richardson, G.L. "An Information Systems Network Architecture," Journal of Systems Management, February 1989, pp. 28-34.

## About the Authors

Gary L. Richardson is director of information technology, Star Enterprise in Houston, Texas. Dr. Richardson has served in various senior management positions within the Texaco and Star Enterprise organizations since 1979. He is currently an adjunct professor at Sam Houston State University. Previously, he was a professor at Texas A & M. He has written four computer-related texts, numerous technical articles, and has served as a consultant to the U. S. Air Force, Defense Communications Agency, other government agencies, and industry. Dr. Richardson received a B.S. in mechanical engineering from Louisiana Tech University, AFIT training in meteorology at the University of Texas, an M.S. in engineering management at the University of Alaska, and a PhD. in business administration from North Texas State University.

Brad M. Jackson is a senior consultant in the Information Technology Department, Texaco Inc., Houston, Texas. Since 1983, Mr. Jackson has worked in several areas of the organization including: Texaco U.S.A.- Headquarters; Information Technology Research; Telecommunications; and Marketing. He worked directly with Star Enterprise on the development of their enterprise architecture. Currently he is working on a joint Texaco-University of Minnesota research project in group decision support systems. Mr. Jackson holds an M.S. from the University of Houston and a B.S. from the University of Arkansas, both in computer science.

Gary W. Dickson is a professor of management information systems at the Carlson School of Management at the University of Minnesota in Minneapolis, Minnesota.
