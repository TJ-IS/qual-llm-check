---
otero_id: 23919
otero_key: "DBHHJ4RS"
title: "Towards an enterprise architecture for public administration using a top-down approach"
authors: "V Peristeras; K Tarabanis"
year: "2000"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000378"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Towards an enterprise architecture for public administration using a top-down approach

V Peristeras<sup>1</sup> and K Tarabanis<sup>2</sup>

<sup>1</sup>Greek National Center for Public Administration, Thessaloniki, Greece, pinepthKhol.gr; <sup>2</sup>University of Macedonia, Thessaloniki, Greece, katKuom.gr

The use of Enterprise Architectures is becoming increasingly widespread in the private sector. Borrowing insights from enterprise reference architectures developed during the last decade, IT vendors and companies belonging to specific industries are establishing reference data and process models advancing the standardisation of their businesses and creating a more integrated environment for their activities. Although public administrations share the same problem of non-standardisation, which is being magnified rapidly in a changing and demanding environment, little has been done so far in the direction of integration. This article builds a basis, shows initial directions and attempts to stimulate interest in a PA enterprise framework. Following a top-down approach and employing concepts from the fields of public administration, enterprise integration and generic process and data modeling, the outline of the ArchPad enterprise architec ture for Public Administration is presented. European Journal of Information Systems (2000) 9, 252–260.

## Introduction

During the past few years significant changes are taking place in public administrations (PAs) all over the world. Citizens in all countries are calling for better services at lower cost, responsiveness in an unstable and ever changing political, economic, societal, technological (PEST) environment and administrations closer to their every-day life, acting primarily proactively rather than reactively.

Public Administrations in their quest to satisfy the aforementioned recent societal needs have borrowed management methodologies and practices that have been succcessfully tested in the Private Sector during the last two decades: Total Quality Management, Business Process Re-enginering, Learning Organization, Activity-Based Costing etc. For PAs following these trends and applying them, Information Technology has become a significant leverage factor.

In this context, a series of initiatives promoting and gradually establishing the notion of ‘e-governance’ have taken place in the European Union either as independent activities or as parts of projects enhancing quality and efficiency in PAs. In the latter category, projects such as the British ‘Modernizing Government’ (1999), the Finnish ‘Quality Strategy of Public Services’ (EU Best Practice Administrations, 1999–2000) and the Greek ‘Kleisthenis Program for Modernizing Public Administration’ (The Kleisthenis Project, 1994) could be mentioned.

## Defining the problem

The use of leading-edge information technology to support these major efforts of reorganization, modernisation and reinvention of government is not a simple task. The logic of solely ‘automating’ existing processes, while leaving the organizational structures, the human roles of PAs unchanged has proven to be unsuccessful.

Further, the existence of isolated, overlapping in function and content, highly fragmented and unrelated computerised applications within the same PA organization has resulted in a major interoperability problem and has led to ‘isolated islands of technology’ while Information Systems were viewed as being internal to the PA organization (Tapscott & Caston, 1993). Until recently the ongoing need for inter-organizational exchange of information has become indispensable in the e-governance framework.

A serious need has emerged to analyse and redesign the tasks performed by each agency and ministry, exploring the ways in which various departments fit together, specifying their information processing needs and describing the human roles in each agent.

The need for integration of all systems calls for the formulation of a Reference Architecture for PAs. Of critical importance in this task of PA systems integration is the study of the intersection of their three basic systems (www.ids-scheer.de/english/consulting/fachzentren/ supply/logtag1/sld005.htm) (Figure 1):

I Organizational structures and business processes

I Information systems

I Human roles

The proposed Information Architecture for PA, Arch-

![](/api/attachments/DBHHJ4RS/fulltext/images/338bace603c010d5f0d4f3ab95668809876c563fa8a21304543a7620b7ebe52a.jpg)  
Figure 1 The three systems of PA and their relation.

Pad, is a framework for integrating processes, information systems and human roles. The core of ArchPad is a set of generic enterprise models for PAs at all levels of administrative hierarchy. ArchPad is oriented as much to the administrative experts as to the information systems departments. The goal of ArchPad is to contribute to the task of enhancing value, quality and cost efficiency in PAs.

Being an architecture, ArchPad represents a broad perspective and addresses requirements rather than a specific solution (Stecher, 1993). It aims at providing a basis for reshaping the business processes, the ability to reorganise the technology base, improve data integrity and delivery and allowing for consistent application development and more effective application integration (IBM, 1992).

## Motivation

During the nineties, a number of initiatives in the private sector, such as the Retail Application Architecture (RAA) (Stecher, 1993; IBM, 1992), the Supply Chain Operations Reference-model (SCOR) (www.supplychain.org) and the ARTS Retail Store Integrated Business View Data Model (ARTS, 1996), among others, aimed at solving entrepreneurial problems similar to those presented earlier: problems regarding the data and information that the new, distributed enterprises were utilising, the processes they executed and their interrelations.

Specifically, RAA provides a framework for retail application and information systems planning (Stecher, 1993). SCOR is a process reference model that provides a language for communicating among supply-chain partners (www.suppl-chain.org), while on the other hand the ARTS Data Modeling initiative defined an industry standard data model which provides for software integration and interoperability (ARTS, 1996).

Generic modeling is the common theme in these approaches where models (data, processes, etc) which apply to any enterprise or any industrial sector are developed. The generic models developed as part of the ARTS and SCOR efforts involve data and processes respectively, while the RAA framework includes both types of models. Generic modeling for other systems of the enterprise (eg human roles) has received little attention.

Specific industries such as retail realised the pressure to communicate using a standard language, with reusable elements. Redesign projects and IS development also gain from such a language. Minimally the language provides a means of communicating among units; maximally the language provides a means of representing knowledge for use in the enterprise (www.ie.utoronto.ca/ EIL/tove/comsen/intro11.html).

Similar issues led IT vendors such as SAP and IDS to formulate ready-to-configure solutions covering specific industries and creating generic industry process and data models.

During the same period, significant progress has been made in the public sector throughout Europe, both in reorganising and in introducing computer systems and applications. The ‘Kleisthenis Program (1994 –99)’ funded both by the European Union and the Greek Government with a total amount of approximately 150 MECUs, constituted the main program for public sector modernisation in Greece. At the heart of the Program was the belief that better PA and modernisation of the State is possible by investing in IT, human capital and reorganization (Kostakos, 1997).

Although in the right direction, the intersection of the three systems (structures, humans, IT) (see Figure 1) has not received the required attention during the Program. As a result at its conclusion, a widespread feeling of ‘island’ systems exists. In fact, three such cases exist: I IT islands;

training islands not always in correspondence with the specific needs; and

structural islands that emerged from some interesting yet fragmented re-engineering projects that certainly didn’t alter the model of Greek PA.

The drive for integration, through the definition of Generic Process, Data and Human Models, remains basically the same regardless of whether in the private or the public sector. Although many initiatives facilitate the integration of data and processes in many industries in the private sector, PAs are relatively far behind in this path. They will soon face serious problems, as they rapidly change the way they operate, become more open and citizen-oriented. The specification of a Reference Architecture for PAs is needed and timely.

In the first section of this paper we review the stateof-the-art in Generic Information Systems Architectures, we then attempt to pinpoint and list the Major Processes of PA and give an example of our approach using a mapping methodology. Finally we suggest some paths for future work.

## State-of-the-art in Generic Information System Architecture

The basic motivation and the significance of building generic process and data models were presented in the previous section. In this section a review of the state-ofthe-art is presented on the specification of generic information system architecture. This review is structured around Table 1 which groups various initiatives in this area that have taken place during the last decade. The grouping is built along two axes. The horizontal axis classifies the approaches with respect to what they have tried to model. There are three options for this: modeling data, processes or both.

The vertical axis provides the scope of the models. Three options exist here, as well. At the first level there are frameworks, meta-frameworks (frameworks about how to build frameworks) and methodologies that have been proposed in order to create generic models. This first level serves as a repository or a library that can be consulted before building any kind of generic (process or data) model. At the second level exist generic process and data models. While at the third level examples of specific instantiations of generic data and process models for specific industrial sectors are provided.

The aforementioned taxonomy generates nine cells. The list of approaches that occupy each cell is far from exhaustive. The criterion of choice was the insights these approaches provided to our proposal. As a result, this led to a larger in comparison number of frameworks for building integrated generic models and generic process models since this was the main focus.

The cell in the upper left-hand corner is the most generic and closest to the notion of an ‘architecture’. First in the cells appears the IFIP-IFAC Task Force General Enterprise Reference Architecture Methodology (GERAM) (1998). IFIP and IFAC set up the Task Force on Architectures for Integrating Manufacturing Activities and Enterprises in 1990, with the aim of defining and evaluating Enterprise Reference Architectures. That is, GERAM constitutes a meta-framework for building Enterprise Reference Architecture. Its latest version GERAM 1.6.2, was submitted to ISO TC184/SC5/WG1 for inclusion as an annex to ISO WD15704, ‘Requirements for enterprise-reference architectures and methodologies’ (IBM, 1992). GERAM defines a tool-kit of concepts for designing and maintaining enterprises over their entire life-cycle. GERAM is not yet-another-proposal for an enterprise reference architecture, but is aimed at organising existing enterprise integration knowledge. The framework has the potential for application to all types of enterprises.

Also in this cell appears the Information Systems

Architecture (ISA) introduced by Zachman (1987) and completed five years later (Sowa & Zachman, 1992). Zachman specified the area of Information Systems architectures motivated primarily by the increasing size and complexity of the implementations of information systems. The architecture that was defined included logical constructs to define and control system integration.

In 1991, through the AMICE project of the ESPRIT program, the CIM-based, CIM-Open Standards Architecture (CIMOSA) framework was developed (1993). CIMOSA can be considered as the first GERAM, although the term was coined later. In fact CIMOSA contributed its basis to the IFIP-IFAC GERAM. The 3- D cube framework of CIMOSA provided and continues to provide a lot of insights to modeling undertakings.

A year later a second GERAM was presented from Purdue University: the Purdue Enterprise Reference Architecture (PERA) (www.pera.net/IndFgeram.html) (Williams, 1992) also based on CIM.

The ARIS framework (Scheer, 1992; 1994) was also accompanied by a fully computerised toolset and has become a leading process modeling front-end. The CIMOSA approach is prominent in ARIS both in its lifecycle dimension and in the different enterprise ‘views it supports.

The GRAI Integrated Methodology (GIM) (Doumeingts et al, 1993) was among the first to model decision structures in CIM.

The TOronto Virtual Enterprise (TOVE) is a project of the University of Toronto. The project aimed at four goals (www.ie.utoronto.ca/EIL/tove/comsen/intro11.html). TOVE proposed a set of integrated ontologies for representing enterprises spanning activities, states, time, organization, resources and products (GERAM, 1998). TOVE also implemented the semantics in a set of axioms that will enable TOVE to automatically deduce the answer to many ‘common sense’ questions about the enterprise.

The Enterprise project, budgeted at over 4 MECU by the British Government, was the UK’s major initiative to promote the use of knowledge-based systems in enterprise modeling. It aimed at supporting organizations in the Management of Change. During the project, the Enterprise Toolset was developed. The Toolset employs executable process models to help users perform their tasks (www.aiai.ed.ac.uk/project/enterprise/enterprise/ enterprise.html).

The Convergent Engineering approach (Taylor, 1995) is an implementation of object-oriented logic in enterprise modeling.

Ontoligua is part of the Knowledge Sharing Project at Stanford University (www-ksl.stanford.edu/knowledgesharing/ontologies/README.html). As in TOVE, Ontologies is the main subject of study in the project. Ontologies provide a vocabulary for representing and communicating knowledge about some topic and a set of relationships that hold among the terms in that vocabulary (www-ksl.stanford.edu:5915/doc/frameeditor/what-is-an-ontology.html).

Table 1 Process of Data Modeling Taxonomy

<table><tr><td></td><td>Data and process</td><td>Process</td><td>Data</td></tr><tr><td>Meta-frameworks, frameworks and methodologies, for generic modeling</td><td>- IFIP-IFAC Task Force GERAM (1998)- Information Systems Architecture (ISA) (Sowa &amp; Zachman, 1992; Zachman, 1987)- Computer Integrated Manufacturing Open System Architecture (CIMOSA) (1993)- Purdue Enterprise Reference Architecture (PERA) (www.pera.net/Ind_geram.html) (Williams, 1992)- Architecture for Information Systems (ARIS) (Scheer, 1992; 1994)- GRAI Integrated Methodology (GIM) (Doumeingts et al, 1993)- Toronto Virtual Enterprise (TOVE) (www.ie.utoronto.ca/EIL/tove/comsen/intro11.html) (www.ie.utoronto.ca/EIL/tove/entonto.fm.html)- The Enterprise Project (www.aiai.ed.ac.uk/project/enterprise/enterprise/enterprise.html)- Ontologies-Ontolingua encoding (www-ksl.stanford.edu/knowledge-sharing/ontologies/README.html) (www-ksl.stanford.edu:5915/doc/frame-editor/what-is-anontology.html)- Convergent Engineering (Taylor, 1995)</td><td>- MIT Process Handbook (Methodology) (Malone &amp; Crowston, 1994; Wyner &amp; Lee, 1995; Crowston, a; Crowston &amp; Osborn, 1996; Crowston, 1997; Bernstein et al, 1999)- Grammar of Processes (Pentland, a; b)</td><td></td></tr><tr><td>Generic models</td><td>- Federal Enterprise Architecture (Spewak &amp; Hill, 1992; Federal Enterprise Architecture Framework, 1999)- SAP Reference Models (www.sap.com/products/techno/pdf/50008444.pdf)</td><td>- Government Process Classification Scheme by the Inter-Agency Benchmarking &amp; Best Practices Council (1996)- Phios Repository (1999)- International Benchmarking Clearinghouse Process Classification Framework (American Productivity &amp; Quality Center, 1992)- Lean Enterprise (www.mit.edu/lean)- Business Excellence Model by European Foundation for Quality Management (www.efqm.org/le99/changesps.htm)</td><td>- IDA Architecture (IDA, 1996)- Data Models, Silverstone et al (1997)- Data Model Patterns, Hay (1996)- Structured Systems Analysis and Design Method (SSDAM)</td></tr><tr><td>Specific industry implementations</td><td>- SAP Industry Solution Maps (www.sap.com)- ARIS Industries Reference Models ((www.idsscheer.de/english.htm) in ‘Aris Toolset’)- Retail Application Architecture (Stecher, 1993; IBM, 1992)</td><td>- MIT PH in the Health Industry (Geisler, 1995; Leavitt, 1995)- Supply Chain Operations Reference-model (SCOR) (www.supply-chain.org)- Alternative Carrier Reference Model (ACRM) (www.idsscheer.de/english/news/mitteilungen/archiv99/telecom.htm)</td><td>- ARTS (Arts Retail Store, 1996)- IDA Projects (www.ispo.cc.be/ida/ida.html)</td></tr></table>

In the process column of the first level of the taxonomy, one finds the Process Handbook (PH) from MIT. The PH was developed at MIT by the Center for Coordination Science. It is basically a process repository, based on a representation that exploits two sources: (1) specialisation of processes based on inheritance of objecct-oriented programming; and (2) concepts about managing dependencies from coordination theory (Malone & Crowston, 1994; Wyner & Lee, 1995; Crowston, a; Crowston & Osborn, 1996; Crowston, 1997; Bernstein et al, 1999).

The grammar of processes exists in the same cell. The metaphor of ‘grammar’ is extensively used and it has been developed into a rigorous model applicable in empirical research (Pentland, a). For this approach the Process Handbook is a useful repository, serving as a large lexicon of process steps and constraints on the ways in which they can be combined (Pentland, b).

The second level of the taxonomy contains Generic Process/Data Model approaches. In the Data & Process column, the SAP Reference Model is placed. This model is the basis of the R/3 logic. It joins both processes and data models in a generic representation of the enterprise (www.sap.com/products/techno/pdf/50008444.pdf).

The Federal Enterprise Architecture Framework was developed by the Chief Information Officers Council (CIO Council) in the USA. The Federal Enterprise Architecture sesrves as a governmental strategic information asset base that defines the business information necessary to operate the business, the technologies necessary to support the business operations, and transitional processes for implementing new technologies in response to the changing needs of the business (Federal Achitecture Enterprise, 1999). The proposed framework is based on two methodological pillars: the Zachman Framework and Dr Steven Spewak’s Enterprise Architecture Planning (Spewak & Hill, 1992). The Federal Enterprise Architecture Framework promotes shared development for common Federal processes, interoperability, and sharing of information among Federal Agencies and other Governmental entities. The latest version of the Framework was published in September 1999 and could be considered the most significant pilot initiative towards the creation of an architecture for PAs.

In the Process column, one finds the generic models of the Government Process Classification Scheme (PCS) from Inter-Agency Benchmarking & Best Practices Council (1996), the International Benchmarking Clearinghouse (IBCCF) (American Productivity & Quality Center, 1992), the Lean Enterprise Model (www.mit.edu/lean) and the European Foundation for Quality Management Excellence Model (www.efqm.org/le99/changesps.htm) serving as a basis for re-engineering, benchmarking and best practices efforts in different industries due to their generic character.

PCS is a taxonomy of common government processes to be used for collecting and sharing ‘best practices’. The four major processes of ‘Establish Direction’, ‘Acquire Resources’, ‘Provide Capabilities’ and ‘Execute the [Agency’s] Mission’ are further analysed providing over 150 fourth level processes (Government Process Classification Scheme, 1996). The specific taxonomy could serve as a useful repository of government-executed processes. The framework is obviously process-oriented as the established classification is based on a horizontal view rather than a functional taxonomy and is thus applicable to the whole of the PA’s functions.

The IBCCF model consists of thirteen generic processes that describe the operation of any private sector organization. This first level of processes is further decomposed into a second and third level of increasing detail. A latest version of the EFQM Model, tuned for non-profit organizations, has been extensively applied to Public Sector benchmarking (Samuels, 1998) during the British ‘Benchmarking Project’. Also, the Phios repository is the commercial version of the aforementioned Process Handbook from MIT (Phios Corporation, 1999) with an extensive library of processes.

The Data column of the second level contains references to the work of Silverstone, Inmon and Graziano (1997) and Hay (1996) who proposed generic data models applicable to a wide range of different enterprises.

The Interchange of Data between Administrations Architecture is an effort in the data column, too. This was developed through the European IDA I Program (1996). The fundamental concept is that of a homogeneous Europe-wide facility, the EuroDomain, which allows the exchange of data between disparate or similar IT-systems of local Administrations, the Local Domains. The EuroDomain is foreseen to be established as a homogeneous set of actual, pan-European value-added network services. The emphasis is on the service provided by the EuroDomain. The delineation of responsibility between Local Domains and the EuroDomain is achieved through the vehicle of an access point, called the EuroGate, which is an identifiable module connecting a Local Domain to the EuroDomain. The Euro-Gate is a key architecture element providing both the flexibility and the managerial and technical independence between the Domains.

The Structured Systems Analysis and Design Method (SSADM) was an interesting early attempt in data modeling by the UK government. It was developed by CCTA (Central Computer and Telecommunications Agency) in the early 1980s.

Finally at the third level of the taxonomy, exist some examples of the numerous implementations in specific industrial sectors (partial scope models as defined by GERAM-CIMOSA).

In the Data & Process column the SAP Industry Solution Maps define the business processes of an industry and map these processes to the actual SAP products in order to enable the easy evaluation and implementation of an information technology business solution (www.sap.com). The ARIS Industries Reference Models illustrate industry-specific processes, data and function structures (www.ids-scheer.de/english.htm).

In the Process column, the need to build a common language in industries (eg health (Geisler, 1995; Leavitt, 1995) and supply-chain (www.suppl-chain.org) has led to the identification of the few major processes that describe the whole action in a specific field. For example, the Alternative Carrier Reference Model (ACRM) for telecommunication companies developed by IDS in collaboration with Nokia telecommunications, provides alternative telecommunication carriers with reference structures that allow individual, fast, and costeffective customisation and optimisation of business processes (www.ids-scheer.de/english/news/mitteilungen/ archiv99/telecom.htm).

Finally, in the Data column, the ARTS Model and the sector projects financed by the IDA I project could be placed (Koontz et al, 1980).

## Major processes in PAs

## Defining the major processes-methodology

All generic modeling frameworks, placed in the first level of the taxonomy of the last section, begin the modeling of an enterprise with a function (or process) definition procedure (Scheer, 1992; CIMOSA, 1993; GERAM, 1998). This provides the basis for further information system (or model) building. A similar start point can be employed in building a reference architecture for PA. The key questions at this point are:

which are the major-generic processes performed by all PAs regardless of the tasks they execute and the services they produce?

in what way can the processes of PA be represented? In order to answer the first question, the three-layer management model describing any organization (also referred to as the staff/line model) (Koontz et al, 1980) was employed, that is:

I the strategic layer;

I the operations layer;

I the support layer.

Their adaptation to a PA environment provides respectively the three generic functions that characterise PA:

I formulate Public Policy;

I provide services;

I support operations.

The above are the first level generic processes that could describe any kind of activity that occurs in PA (see Figure 2).

![](/api/attachments/DBHHJ4RS/fulltext/images/23feeb105e8ac40623ef498ae92ab91157418d2c715ffb83798fb872fa998382.jpg)  
Figure 2 Major processes in PA.

There are important reciprocal interrelations among these three generic processes. More importantly, the link between the ‘Formulate public Policy’ process and the ‘Provide Services’ is quite strong and demonstrates the former process more as a learning and evolutionary procedure rather than a simple predefined executable task (Brown & Wildavsky, 1984).

These three generic processes are then compared to processes in the IBCCF framework as well as to models found in the PA literature. The IBCCF provides thirteen generic (first level) processes appropriate to describe any kind of service-oriented organization. Important changes on the IBCCF model were required in order to tune it to the PA needs. In particular, the ‘Formulate Public Policy’ (FPP) process of the public domain differs fundamentally from its corresponding process, ‘Develop Vision & Strategy’, of IBCCF (American Productivity & Quality Center, 1992) as it is based on a public policy analysis model.

Subsequently, the MIT Process Handbook methodology is employed as a process mapping technique. The three notions of decomposition, specialisation and bundles (Wyner & Lee, 1995; Bernstein et al, 1999) were found to be particularly powerful in providing a useful and meaningful representation of PA processes.

The decomposition notion is used by all process representation techniques and it is based on the assumption that all processes can be broken down (or decomposed) into sub-parts (or sub-activities (Bernstein et al, 1999).

Specialisation is the second notion provided by the Process Handbook (PH). This concept was borrowed from object-oriented programming. The inheritance process allows instances of a specific process to both inherit characteristics from its parent (more generic) process and maintain specific characteristics or components as well. In generic process modeling, this is a particular useful concept which helps instantiate a prototype, defined by a generic process model, for the specific organization being modeled.

While a sub-activity represents a part of a process, a specialisation represents a ‘way of’ doing the process (Bernstein et al, 1999).

The third notion of the PH representation that is used is the ‘bundle’. A bundle is created with the grouping of related alternatives of specialisation. In PH methodology there are usually more than one way to specialise a process. These alternative ways of performing specialisations are called ‘bundles’ in the PH framework.

## The proposed model

## Formulate public policy

The first generic process of ‘Formulate Public Policy can be decomposed using the policy analysis model presented by Hogwood and Gunn (1984). As part of the ArchPad architecture, a PA specific model was built rather than adopting the IBCCF ‘Develop Vision & Strategy’ process for reasons mentioned above.

![](/api/attachments/DBHHJ4RS/fulltext/images/5e51cf795cccb15bbf698bc846c449f427547589b3c6fe9ecae5b0981f508ad0.jpg)  
Figure 3 Decomposition of the ‘Formulate Public Policy’ major process.

![](/api/attachments/DBHHJ4RS/fulltext/images/24ec0ad0b6e51bfd2b78f58bff9586f330dc9ded8100bc39008a447c66d70bd3.jpg)  
Figure 4 Decomposition of the ‘Provide Service’ major process.

At the second level of this process, the upper level process is decomposed into eight sub-processes (see Figure 3).

## Provide services

The second generic process, ‘Provide Services’ can also be decomposed. In this task, IBCCF processes are utilised, but are significantly altered. The ‘Design Products and Services’ and the ‘Produce and Deliver for Service-Oriented Organization’ processes of IBCCF, after being adapted into the PA framework, result in the four second-level processes exhibited in Figure 4.

We proceed by analysing the ‘Provide Service’ process using specialisation. There could be two different bundles of specialisation: one based on the ‘Provide WHAT KIND of Service?’ question and one on the ‘WHO Provides the Service?’ This first level of specialisation is shown by the ‘WHO’ and ‘WHAT’ arrows, which emanate from the ‘Provide Service’ generic process (see Figure 5).

Answering the first question provides a ‘bundle’ of specialisation based on the WHAT question. Using a common taxonomy of PA services in the relevant literature (Leavitt, 1995) the categories ‘Provide Regulations and ‘Provide Public Common Goods & Services’ (Lowi, 1979) can be employed. Each of the ‘Provide Regulations’ and ‘Provide Common Goods & Services’ processes inherits the sub-processes of their common parent process ‘Provide Service’ (Figure 4). This inheritance however does not prohibit altering, adapting or even erasing a part of the parent process according to the specific needs of the newly specialised processes. As an example, the ‘Produce’ sub-process will be passed to both specialised processes but with a different meaning: ‘Produce’ becomes ‘Vote/Decide’ in providing regulations and ‘Make/Buy’ in providing public goods. Similarly the ‘Design Service’ generic sub-process will become ‘Design Regulation’ and ‘Design Common Goods’ respectively. These two would fundamentally differ and their differences should emerge, when the next (third) level of decomposition is built.

![](/api/attachments/DBHHJ4RS/fulltext/images/046ce85642fa68568aae591c37d5aeea2ae05d99f741f5be6cf47b6b978a8c5a.jpg)  
Figure 5 Specialisation of the ‘Provide Service’ major process.

The first level of the ‘WHAT’ bundle is further specialised as Figure 5 illustrates. Asking the question ‘WHO Provides the Regulations’ could formulate an interesting bundle based on WHO. Three sources of regulations provision could be detected based on Montesque’s classical separation of powers in the State:

I ‘Provide Legislative Acts’.

I ‘Provide Judicial Decisions’.

I ‘Provide Administrative Acts’.

Of course at the lower levels of the representation, completely different processes would appear as different chains of processes describe the ways in which the parliament legislates, the courts judge and PA produces Acts. For example, all of these processes have a ‘Communicate & Deliver’ sub-process, but it is likely that it will be executed differently.

In Figure 5 an additional second-level specialisation is shown. The ‘Provide Public Common Goods & Services’ first-level specialisation can be further specialised with the ‘WHAT KIND’ of Public Common Goods & Services?’ question. A second-level specialisation is provided in two versions: ‘Provide distributive Goods & Services’ and ‘Provide redistributive Goods & Services’. This categorisation is common in the PA literature (Musgrave, 1959; Lowi, 1979; Lane, 1995).

The ‘Provide distributive Goods & Services’ process describes the production of services which, for various reasons, the free market fails to produce (at all or in efficient quantities) (eg parks, seaports, roads, defence). On the other hand, the ‘Provide redistributive Goods & Services’ describes the intervention of the State in the Market in order to enhance social justice (Musgrave, 1959) (eg health systems, social security-insurance, public education). The above concepts correspond to Buchanan’s productive and protective state (Buchanan, 1977).

Going back to the generic (first) level, we could specialise the ‘Provide Services’ process using the question ‘Who Provides the Service’. Answering this WHO question could provide a second bundle of specialisation to the first-level parent process. A service could be ‘Provided Centrally’, ‘Provided Regionally’ or ‘Provided Locally’. The criterion for this specialisation is not merely geographical but mainly administrative. The whole framework alters as one moves from central to local provision of services.

![](/api/attachments/DBHHJ4RS/fulltext/images/4d4912e9fbc1e02a87f82235364ca5953c48aa38d847b08b38c02cc030a5876a.jpg)  
Figure 6 Specialisation of the ‘Support Operations’ major process.

The sub-processes of these three types of service provision have been inherited from their parent process.

The ‘Communicate & Deliver’ sub-process in ‘services centrally provided’ is not the same as the ‘Communicate & Deliver’ process in ‘services locally provided’. Their differences will certainly appear when the decomposition is carried further.

## Support operations

The third generic process ‘Support Operations’, is specialised employing the IBCCF model. In Figure 6 three specialisations are shown based on the question ‘WHAT KIND of Support Operations’.

The models that result when analysing this third generic process do not differ significantly from those of the private section (ie support operations whether in private or in public sector are about the same). Both the IBCCF and the Phios Process Repository (PPR), mentioned earlier, could service as a ready-to-use process library solution; the latter accommodating a rather impressive number of processes with helpful descriptions (approximately 6000).

Obviously both decomposition and specialisation tasks could be performed further with the support of PA theories and models. The ArchPad model appears more generic at the highest level and gradually becomes more PA-specific as we proceed to lower levels, analysing it using decomposition and specialisation.

## Implications for future research

This paper has presented the need for building an Information Architecture for Public Administration. It proposed a model based both on PA theory and on Information Systems literature. It aims at providing a stimulus for further research in a field that has been little explored until now.

As part of future work we intend to continue developing ArchPad based on other theories of PA as well as a bottom-up approach which will include empirical research. The latter will provide the model with data, enforcing its validity and applicability to the whole PA framework. Analysing numerous specific examples of process execution accompanied by their data models and the organizations in which they are executed, would create a useful PA-specific process/data/structure use-case library, which could be used in re-engineering, benchmarking and integrated Information Systems development.

If PA is to provide an enhanced level of service and participate in the developments of the ‘Information Society’ then an architecture to base this evolution is needed and timely.

## References

American Productivity & Quality Center (1992). International Benchmarking Clearinghouse Process Classification Framework. At www.apqc.org/free/framework.htm

ARTS Retail Store Integrated Business View Data Model (1996) from the Association for Retail Technology Standards.

Bernstein A, Dellarocas C, Malone TW, Quimby J, Crowston K, Lee J, Pentland B, Wyner G and Osborn C (1999) Tools for inventing organizations: towards a handbook of organizational processes. Management Science 45(3).

Browne A and Wildavsky A (1984) Should evolution become implementation. In Implementation, 3rd edn (Wildavsky A and Pressman J, Eds), University of California Press, Berkeley.

Buchanan JM (1977) Freedom in Constitutional Contract. Texas A&M University Press, College Station.

CIMOSA – Open System Architecture for CIM (1993) ESPRIT Consortium AMICE, Springer-Verlag, Berlin.

Crowston K (a) A Taxonomy of Organizational Dependencies and Coordination Mechanisms, at http://ccs.mit.edu/papers/ CCSWP174.html

Crowston K (1997) A coordination theory approach to organizational process design. Organization Science 8(2), 157–175.

Crowston K and Osborn C (1996) A coordination theory approach to process documentation and redesign. MIT Center for Coordination

Science Working Paper, Massachusetts Institute of Technology, August.

Doumeingts G, Chen D, Vallespir B, Fenie P (1993) GIM (GRAI Integrated Methodology) and its Evolutions. A Methodology to Design and Specify Advanced Manufacturing Systems. Proceedings of the JSPE/IFIP TC5/WG5.3 Workshop on the Design of Information Infrastructure Systems for Manufacturing, ’93, pp 101– 117, Tokyo.

EU Best Practice Administrations (1999–2000) Center for Excellence, Finland.

Federal Architecture Enterprise Framework v.1.1 (Sep. 99) CIO Council.

Geisler MA (1995) The Evolving Health Care Delivery Systems: Applying the Process Handbook Methodology to Gain a Vision of the Future. Unpublished MS thesis, MIT Sloan School of Management, Cambridge, MA.

General Enterprise Reference Architecture Methodology version 1.6.2 (GERAM) (1998) IFIP-IFAC Task Force, June 1998.

Government Process Classification Scheme, v1.01 (Oct 1996) at http://www.va.gov/fedsbest/index.htm

Hay D (1996) Data Models Patterns. Dorste House Publishing, NY.

Hogwood BW and Gunn LA (1984) Policy Analysis for the Real World. Oxford University Press, Oxford.

IBM (1992) Retail Application Architecture (RAA)/General Information Manual.

IDA Architecture Guidelines, v.2.1a (July 1996) European Commission, DGIII.

Koontz H, O’Donnell C and Weihreich H (1980) Management, 7th Edition, McGraw Hill, NY.

Kostakos G (1997) The Kleisthenis Program. Administrative Review 7 (in Greek).

Lane J-E (1995) The Public Sector: Concepts, Models and Approaches. Sage Publications, 2nd edn, London.

Leavitt W (1995) Health Care Delivery Systems: Using the MIT CCS Handbook to Create Organizations for the 21st Century. Unpublished MS thesis, MIT Sloan School of Management, Cambridge, MA.

Lowi TJ (1979) The End of Liberalism: The Second Republic of the United States. WW Norton, New York.

Malone TW and Crowston K (1994) The interdisciplinary study of coordination. ACM Computing Surveys 26(1), 87–119.

Modernizing Government (1999) Presented to Parliament by the Prime Minister and the Minister for the Cabinet Office, Great Britain.

Musgrave RA (1959) The Theory of Public Finance. McGraw-Hill, New York.

Pentland BT (a) Grammatical Models of Organizational Processes, at http://ccs.mit.edu/papers/CCSWP176.html

Pentland BT (b) Process Grammars: A Generative Approach to Pro cess Redesign, at http://ccs.mit.edu/papers/CSWP178/CCSWP178. html

Phios Corporation (1999) New Tools for Managing Business Processes. March 1999, at www.phios.com

Samuels M (1998) Towards Best Practice: An Evaluation of the First

## About the authors

Dr Konstantinos Tarabanis is Associate Professor at the University of Macedonia, Department for Business Administration, and Director of the Business Computing Laboratory of the Centre of Research and Technology, Hellas. He received his PhD in Computer Science from the Columbia University, 1991, his MPhil and MSc in Computer Science from the same University (1989 and 1988). He also holds an MSc in Mechanical Engineering from the same University (1984). He serves as Academic Visitor at the IBM TJ Watson Research Center. His research interests concern business process modeling and distributed IT architectures using mobile agents as enabling technology. His previous positions were: Research Scientist at the

Two Years of the Public Sector Benchmarking Project 1996–1998. Next Steps Team Efficiency & Effectiveness Group, Cabinet Office.

Scheer A-W (1992) Architecture of Integrated Information Sysems. Springer, Berlin.

Scheer A-W (1994) Business Process Renengineering: Reference Models for Industrial Enterprises (2nd edn). Springer-Verlag, New York.

Silverstone L, Inmon WH and Graziano K (1997) The Data Model Resource Book. John Wiley & Sons, NY.

Sowa JF and Zachman JA (1992) Extending and formalizing the framework for information systems architecture. IBM Systems Journal 31(3).

Spewak St H and Hill St C (1992) Enterprise Architecture Planning, Developing a Blueprint for Data, Applications and Technology. John Wiley & Sons.

Stecher P (1993) Building business and application systems with the Retail Application Architecture. IBM Systems Journal 32(2).

Tapscott D and Caston A (1993) Paradigm Shift: The New Promise of Information Technology. McGraw-Hill, NY.

Taylor DA (1995) Business Engineering with Object Technology. John Wiley & Sons.

The Kleisthenis Project (1994) Ministry of Internal Affairs, Greece.

Williams TJ (1992) The Purdue Enterprise Reference Architecture. Purdue Laboratory for Applied Industrial Control, Purdue University, USA.

Wyner G and Lee J (1995) Applying specialization to process models. In Proceedings of the Conference on Organizational Computing Systems. Association for Computing Machinery, Milpitas, California.

Zachman JA (1987) A framework for information systems architecture. IBM Systems Journal 26(3).

IBM TJ Watson Research Center, responsible for the development of sensor planning algorithms for the IBM Machine Vision Planning MVP system (1988–1991) and Associate Engineer at IBM East Fishkill (1984–1985).

Vasilis Peristeras is IT Consultant at the United Nations Thessaloniki Centre for Public Service Professionalism. His previous position was chief of administrative support and researcher at the Greek National Centre of Public Administration, Thessaloniki. He studied Political Science and holds postgraduate degrees on Public Administration and Information Systems.
