---
otero_id: 13842
otero_key: "DEGHJVE6"
title: "Architectural alignment of process innovation and digital infrastructure in a high-tech hospital"
authors: "Bendik Bygstad; Egil Øvrelid"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1728201"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Architectural alignment of process innovation and digital infrastructure in a high-tech hospital

Bendik Bygstad & Egil Øvrelid

To cite this article: Bendik Bygstad & Egil Øvrelid (2020): Architectural alignment of process innovation and digital infrastructure in a high-tech hospital, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1728201

To link to this article: https://doi.org/10.1080/0960085X.2020.1728201

CO © 2020 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/DEGHJVE6/fulltext/images/ba2387b4b6ab269436670ea5bc683670b7a0afe07643600176059194c680167d.jpg)

Published online: 27 Feb 2020.

![](/api/attachments/DEGHJVE6/fulltext/images/3572860bcb84e434e00bc151dd022492f58a78fbfd971264783c2df08cdd502c.jpg)

Submit your article to this journal

![](/api/attachments/DEGHJVE6/fulltext/images/afe41e684a8355f8d7f4d2078465e3a69b88fa8c3b3dc58564c9d8f2968b7f93.jpg)

Article views: 271

![](/api/attachments/DEGHJVE6/fulltext/images/2ed39a43bb138002ad07f826c8e4d9d86cb736cfc8f88aa7ba01ab7a5b743c32.jpg)

View related articles

![](/api/attachments/DEGHJVE6/fulltext/images/41561f07a9266a95ae8872bb360130c50adaecf1dd9bdd8de51a57bca09d0808.jpg)

View Crossmark data

EMPIRICAL RESEARCH

∂ OPEN ACCESS

Check for updates

# Architectural alignment of process innovation and digital infrastructure in a high-tech hospital

Bendik Bygstad and Egil Øvrelid

Department of Informatics, University of Oslo, Oslo, Norway

## ABSTRACT

Two central approaches to IT-enabled organisational change are process innovation and digital infrastructure research. In this study, we investigate the alignment between them, both from a theoretical and a practical perspective. They have quite di<sup>f</sup>erent basic assumptions on evolution; process innovation is a top-down approach, while digital infrastructures evolve bottom-up and are partly outside direct managerial control. Our research question is, how can a process innovation initiative successfully align with an underlying digital infrastructure? Our empirical evidence is an in-depth case study at a new high-tech hospital in Norway. Building on a proposed framework of alignment between process innovation and digital infrastructure, we identify, analyse three architectural alignment mechanisms. We found that (i) the careful deployment of lightweight IT in onsite con<sup>fi</sup>guration, loosely coupled from the infrastructure activities, allows for fast process innovation while leveraging the slow and nonlinear evolution of infrastructure (ii) the interaction between lightweight IT and large clinical systems by a set of boundary resources resolves the tension between innovation and infrastructure. For practitioners, we show that lightweight IT can serve as a mediating technology in the con<sup>fi</sup>guration.

ARTICLE HISTORY Received 28 September 2018 Accepted 29 January 2020

ACCEPTING EDITOR Jan Mendling; Brian T. Pentland; Jan Recker

ASSOCIATE EDITOR Jan Mendling; Brian T. Pentland; Jan Recker

KEYWORDS Process innovation; digital infrastructure; lightweight IT; architecture; alignment; case study

## 1. Introduction

Digitalisation denotes IT-enabled organisational change, where the physical and the digital are entwined and con<sup>fi</sup>gured in new ways (Constantinides, Henfridsson, & Parker, 2018; Yoo, Henfridsson, & Lyytinen, 2010). In this study, we investigate the alignment between two central approaches to IT-enabled organisational change, process innovation, and digital infrastructure. Digitalisation often includes two key elements; the redesign (or automation) of a work process or service, and some innovative use of IT. For instance, Amazon redesigned the way we buy books, and a tra<sup>fi</sup>c app in a smartphone tells us when the next bus arrives. Alignment generally refers to “<sup>fi</sup>t”, or congruence, between business needs and IT capabilities (Chan & Reich, 2007).

Process innovation is at the heart of digitalisation. It can be incremental, such as improving work<sup>fl</sup>ow or communications, or disruptive, such as disintermediating supply chains or creating new business models. However, in both cases, successful process innovation needs to align with the underlying IT infrastructure. A customer app must be designed to be easy to use, but also to retrieve data from enterprise systems. A medical device can help to improve the surgery process by providing real-time clinical data, but must also communicate with patient journal systems. A robotic process automation solution must solve a business need, but also integrate with corporate systems in order to work. However, in many cases the process redesign and the underlying digital infrastructure are misaligned; i.e. they do not support each other. When process innovation teams increasingly use lightweight technologies such as mobile phones or Internet-of-things, misalignment often increases (Gregory, Kaganer, Henfridsson, & Ruch, 2018).

From a practical perspective the process innovation team may experience several problems; for instance that it is di<sup>fi</sup>cult to retrieve data from enterprise systems, because of di<sup>f</sup>erent formats, con<sup>fl</sup>icting business interests, or security and privacy concerns (Bygstad, 2017). Or the process innovation team may experience that the underlying infrastructure is simply not flexible enough to accommodate the requirements of agile change, leading to failed projects (Comella-Dorda, Lohiya, & Speksnijder, 2016). For instance, the case we are presenting in this paper highlights how a process innovation initiative on patient <sup>fl</sup>ow in a hospital, con<sup>fl</sup>icts with a large IT portfolio of systems.

From a theoretical perspective we believe it is fruitful to regard this alignment problem as a meeting between two di<sup>f</sup>erent approaches to IT-enabled organisational change, namely process innovation research and digital infrastructure theory. Process innovation may be seen as a sub-discipline of business process management (BPM) and deals with IT-enabled innovations that particularly change user experience (Schmiedel & Brocke, 2015). Process innovation is business-oriented and is usually conducted topdown, through disruptive change or systematic improvement (Hammer, 2015). In contrast, digital infrastructure theory focuses on the large “installed base” of technology, the socio-technical network of technology, users and systems. Digital infrastructures are not designed top-down but evolve (and drift) organically through adaptation (Hanseth & Lyytinen, 2010).

Seen from the perspective of process innovation, digital infrastructure is a necessary foundation, but should be <sup>fl</sup>exible enough to accommodate planned change. Seen from the perspective of digital infrastructure theory, the installed base has its inherent dynamics, which is driven by more powerful forces than local innovation initiatives (Hanseth & Lyytinen, 2010). The two perspectives, thus, seem basically incompatible – can they be aligned?

Beverungen (2014) investigated the problem from a sociological angle, drawing on Giddens (1984) and Ciborra and Hanseth (2000). His starting point was that “business process management is often considered as a top-down management activity. This view is inconsistent with the observation that information infrastructures are at drift, outside top-down management control”. The implication is that the rational top-down approach of BPM is incongruent with current research of large digital infrastructures, which has shown that infrastructures, because of their size, interconnectedness, and complexity, are partly outside direct management control, making alignment very challenging. We will call this phenomenon Beverungen’s problem.

Beverungen o<sup>f</sup>ered a framework based on ostensive and performative aspects (Pentland & Feldman, 2005), combining rational design and social construction (Beverungen, 2014, p.195). However, our approach to resolving Beverungen’s problem is simpler and more practical; we suggest dividing it into two challenges. First, how can we connect and reconcile the rational design innovation process to a large infrastructure that is characterised by drift and ambiguity? Second, how can we design an IT architecture that connects the IT-supported processes with the infrastructure?

Our research question is:

● How can a process innovation initiative successfully align with an underlying digital infrastructure?

We proceed by a structured comparison between process innovation and digital infrastructure research, followed by a framework for aligning them. In dealing with the research question we chose to focus on IT architecture because alignment requires some architectural mechanisms that connect the redesigned processes with the underlying infrastructure. Our analytical approach is therefore to identify successful architectural mechanisms. We suggest to call them architectural alignment mechanisms. We build on the critical realist understanding of mechanisms, i.e. a mechanism is a causal structure that explains an observed outcome (Bhaskar, 1998).

In this paper we investigate this phenomenon in the context of e-health, focusing on the particularly challenging task of patient <sup>fl</sup>ow in large general hospitals. Improving patient logistics with the help of IT is a key aim for current e-health initiatives, but has proven to be quite challenging in practice (De Vries & Huijsman, 2011; Weggelaar-Jansen & van Wijngaarden, 2018). To develop our argument, we suggest a framework where the process innovation initiative and the digital infrastructure are aligned with architectural alignment mechanisms. We also propose that lightweight IT supports process innovation, in that it allows fast development without extensive engineering (Schmiedel & Brocke, 2015).

Our case analysis revealed three architectural mechanisms; onsite con<sup>fi</sup>guration, vendor boundary resources, and institutional boundary resources. Addressing Beverungen’s problem, we suggest that (i) the careful deployment of lightweight IT in onsite con<sup>fi</sup>guration, loosely coupled from the infrastructure activities, allows for fast process innovation, while leveraging the slow and nonlinear evolution of infrastructure, and (ii) the interaction between lightweight IT and large clinical systems by a set of boundary resources resolves the tension between process innovation and digital infrastructure.

## 2. Process innovation and digital infrastructures

The two approaches both deals with IT-enabled organisational change, but their origins are very di<sup>f</sup>erent; process innovation originated from management research with an industrial and quality focus (Harmon, 2010), while digital infrastructure theory was developed from Internet research and actornetwork theory (Hanseth & Lyytinen, 2010).

We <sup>fi</sup>rst compare the research on process innovation and digital infrastructures. An overview of the discussion is o<sup>f</sup>ered in Table 1. Then we discuss the di<sup>f</sup>erence between heavyweight and lightweight IT.

## 2.1. Key terms and assumptions

A business process is “a set of activities that produce value to a customer” (Hammer & Champy, 1993), and all work is process work. The discipline of BPM focuses on supporting business processes using methods, techniques, and software to design, enact, control and analyse operational processes (Recker, 2014).

Process innovation and digital infrastructure theory.

<table><tr><td>Aspect</td><td>Process innovation</td><td>Digital infrastructure</td></tr><tr><td>Focal object</td><td>Business process</td><td>An emerging socio-technical network</td></tr><tr><td>Key terms</td><td>BPM, process improvement (Recker, 2014)</td><td>Installed base, standards, bootstrapping (Hanseth &amp; Lyytinen, 2010)</td></tr><tr><td>Assumptions on evolution</td><td>Process innovation is conducted top-down through disruptive change or systematic improvement (Hammer, 2015)</td><td>Infrastructures are not designed but evolve bottom-up through adaptation, cultivation, and drift (Ciborra, 2000)</td></tr><tr><td>Assumptions on technology and architecture</td><td>Process innovation focuses on the needs of the user and is best supported by light engineering (Schmiedel &amp; Brocke, 2015)</td><td>Infrastructures are layered and interconnected by standards and gateways. This installed base implies a strong path dependency (Hanseth &amp; Lyytinen, 2010).</td></tr><tr><td>Tensions</td><td>Ostensive vs. performative (Pentland, Liu, Kremser, &amp; Hærem, 2019)</td><td>Stability vs. change (Edwards, Jackson, Bowker, &amp; Knobel, 2007)</td></tr></table>

BPM has evolved from being primarily technologyfocused to being a “holistic and principle-oriented discipline concerned with e<sup>fi</sup>cient and e<sup>f</sup>ective business processes” (Schmiedel & Brocke, 2015, p.3). A basic tension in process management is between ostensive (the process as designed) versus performative (the process as conducted) aspects (Pentland et al., 2019)

Digital infrastructure research o<sup>f</sup>ers a quite di<sup>f</sup>erent perspective; it regards the interconnected networks of organisations, people and technologies as the focal object. Hanseth and Lyytinen de<sup>fi</sup>ned it as “a shared, open (and unbounded), heterogeneous and evolving socio-technical system (which we call installed base) consisting of a set of IT capabilities and their users, operations, and design” (Hanseth & Lyytinen, 2010, p. 1). The heterogeneous mix of people and technologies are built on the installed base. As the installed base grows, its development and growth become self-reinforcing, through adaptation and cultivation.

## 2.2. Evolution and innovation

The two approaches also have quite di<sup>f</sup>erent views on evolution and innovation.

Process innovation is conducted top-down through disruptive change or systematic improvement (Hammer, 2015). Process innovation can be seen as “innovations that focus on the adoption of . . . products (which often requires some form of new behavioural pattern) through individuals or organizations, i.e. innovations as seen from the user perspective” (Schmiedel & Brocke, 2015, p. 6).

In contrast, infrastructures are not designed but evolve bottom-up through adaptation, cultivation, and drift (Ciborra & Hanseth, 2000). Some researchers have identi<sup>fi</sup>ed generative mechanisms for this evolution, such as innovation, adoption, and scaling (Henfridsson & Bygstad, 2013), denoting sociotechnical networks of actions. The growth of digital infrastructures is not smooth but usually characterised by negotiation, tensions, and con<sup>fl</sup>icts. Building on extensive historical and social research Edwards et al.’s (2007) identi<sup>fi</sup>ed three basic tensions in digital infrastructures; time (short-term decisions vs. the long-time growth), scale, (such as between global interoperability vs. local optimisation) and agency (such as processes of planned vs. emergent change).

Regarding technology, the two approaches are also di<sup>f</sup>erent, with BPM focusing on the needs of the user in the business process, while digital infrastructure theory is more focused on standards and scaling. In process innovation, the role of technology is in supporting processes that are more e<sup>f</sup>ective. Such process innovations are both triggered by the need to satisfy internal and external stakeholders, but they are also enabled by particular abilities given by modern technology. Schmiedel and Brocke (2015, p. 10) claims, “new technologies of the digital age represent a key source of numerous a<sup>f</sup>ordances for process innovations today”. These are emergent process innovation technologies that change the way people work and enable more dynamic processes, or more dynamic con<sup>fi</sup>guration of processes (Kemsley, 2015)

Process innovations are seen as particularly appealing since they both directly a<sup>f</sup>ect people’s experiences; often do not need heavy engineering; can take place within a given technology; and be deployed globally (Schmiedel & Brocke, 2015). Based on this di<sup>f</sup>erentiation, BPM can drive innovation in two ways: (i) through managing processes that yield product innovations (running processes) and (ii) through managing the redesign of processes that yields process innovations (changing processes).

While process innovation is business-driven, digital infrastructure focuses on stability and slow change. Infrastructures are layered and interconnected by standards and gateways, and the installed base implies a strong path dependency (Hanseth & Lyytinen, 2010). This means that disruptive innovation is unlikely to happen, and usually unwanted (although there are exceptions, called “path creation”), as it con<sup>fl</sup>icts with the installed base. Taking our case as an example, the digital infrastructure of the health region of Norway (including our case hospital) had been growing for 25 years and included around 4.000 di<sup>f</sup>erent applications, each with a speci<sup>fi</sup>c user group. It had gradually become more integrated (through advanced middleware technology), but was still a conglomerate of systems from various vendors, and quite di<sup>fi</sup>cult to adapt and change. Its strength, the secure and e<sup>f</sup>ective data management of the systems, was also its weakness, i.e. the path dependency and inertia.

## 2.3. Lightweight IT

Process innovation focuses on the needs of the user and is best supported by light engineering (Schmiedel & Brocke, 2015), while digital infrastructures include heavier and more durable technologies. In order to conceptualise the di<sup>f</sup>erence between large IT systems and slow innovation on one hand, and the faster innovation e<sup>f</sup>orts on the other, Bygstad (2017) proposed the terms heavyweight IT and lightweight IT. Heavyweight IT was de<sup>fi</sup>ned as “a knowledge regime, driven by IT professionals, enabled by systematic speci<sup>fi</sup>cation and proven digital technology, and realized through software engineering” (p. 181). Further, “ . . . developing heavyweight technology requires specialised IT competence, focusing on requirements, reliability and security” (p.182). The results of this software engineering strategy are impressive solutions, but also very expensive, with time-consuming development, implementation, and adoption projects. In addition, the modules are often tightly interconnected making change in one part a<sup>f</sup>ecting functionality in another part. In a way, this is an explanation for some of the inertia of the installed base (Monteiro, 1998).

In contrast to heavyweight IT, lightweight IT is de<sup>fi</sup>ned as a socio-technical knowledge regime, driven by competent users’ need for solutions, enabled by the consumerisation of digital technology, and realised through innovation processes (Bygstad, 2017). Lightweight IT uses consumer technology such as smart phones, tablets, apps, and whiteboards, and operates largely outside heavyweight IT resources. It follows that lightweight IT prioritise innovation and usability to rigid requirements speci<sup>fi</sup>cations, security and data consistency.

The main point, thus, is that the two regimes have di<sup>f</sup>erent and complementary strengths. While the regime of lightweight IT is formed by the generative relationship between knowledgeable end-user groups and entrepreneurs, the heavyweight IT regime is dealing with core systems and the activities related to stabilising, securing and scaling them (Bygstad, 2017). Examples of strengths with lightweight IT are mobile apps that enable swift purchase of metro tickets, apps to improve service work or white-collar work as well as improved welfare technology solutions (Bygstad & Iden, 2017). Lightweight IT, then, is a knowledge regime, technology-oriented but occupied with <sup>fl</sup>exibility, usability, and innovation (Torkilsheyggi & Hertzum, 2017). Lightweight IT enables and creates new digital relations between technology and users, and gives increased availability, visibility, and con<sup>fi</sup>gurability in adapting to local work practices (Hertzum & Simonsen, 2019). Lightweight IT is con<sup>fi</sup>gurable and thus easier to adapt to particular processes, but it is also powerful in recon<sup>fi</sup>guring digital infrastructures to revitalise hidden information for the purpose of process innovation. Heavyweight IT, on the other hand, enables secure access to comprehensive information repositories. Consequently, both are needed in order to enable profound business innovation.

Connecting heavyweight and lightweight solutions are usually done by the use of boundary resources (Ghazawneh & Henfridsson, 2013), i.e. tools and regulations that serve as interfaces between the heavy IT systems and the lightweight user services. Boundary resources include two main processes; resourcing and securing. Resourcing denotes how the platform supports the ecosystem with the necessary technical and social resources while securing denotes the degree of control executed by the platform owner. Boundary resources are usually related to platform structures, something we do not have here. In line with Islind, Lindroth, Snis, and Sørensen (2016) we regard boundary resources as a socio-technical concept.

## 3. A framework to align process innovation and digital infrastructure

Beverungen’s problem (Beverungen, 2014) implies that there are some inherent con<sup>fl</sup>icts between process innovation and digital infrastructures. From a theoretical point of view, these con<sup>fl</sup>icts originate in the complexities of both structures. Process complexity arises from the number and dependencies of processes, but also from the instability; innovation and improvement usually mean frequent change of processes. Digital infrastructure complexity grows with the number of elements over time, where the installed base (Hanseth & Lyytinen, 2010) of interconnected systems and established routines become a force in itself, which is di<sup>fi</sup>cult to change.

From a more practical view, we observe the con-<sup>fl</sup>icting forces in change initiatives that include IT solutions. The knowledge regimes are di<sup>f</sup>erent; the process design community is business (or organisation) oriented, while the digital infrastructure community is mainly technology-oriented. Also, the plasticity is di<sup>f</sup>erent; while processes can relatively easily be redesigned, the inertia and path dependency of the installed base of infrastructures is well documented (Hanseth & Lyytinen, 2010). This means that the restructuring of the digital infrastructure to support new organisational processes may create new con<sup>fl</sup>icts of both organisational and technical nature. The time perspective also di<sup>f</sup>ers; process redesign is usually focused on innovation and time-to-market, while the digital infrastructure people are concerned about the need for a long-term and holistic architectural perspective.

The result of these con<sup>fl</sup>icts is that the two di<sup>f</sup>erent regimes have often operated separately without adequate alignment. How should the two forces align? To understand and mitigate this con<sup>fl</sup>ict we propose a simple framework, illustrated in Figure 1. It builds on two sources; <sup>fi</sup>rst, we draw on the analysis presented in the previous section on the key di<sup>f</sup>erences between process innovation and digital infrastructure. Second, we build on the alignment literature. The alignment research deals with business and IT alignment, and we consider the alignment between process change and digital infrastructure to be a subclass of this. In their strategic alignment model,Henderson & Venkatraman, 1993) described four domains for strategic choice: business strategy, IT strategy, organisation infrastructure and processes, and IT infrastructure and processes. Further, there are two main aspects of alignment; strategic <sup>fi</sup>t (the interrelationships between external and internal domains) and functional integration (integration between business and technology domains). Our focus here is functional integration, i.e. the architectural aspect. However, since it is not enough to interconnect the silo systems, there is a need to establish a structural connection between data sources in the installed base, and user services a<sup>f</sup>orded by modern innovative technology. To do so, some architectural alignment mechanisms are needed.

As Figure 1 shows, we envision two di<sup>f</sup>erent structures; on the upper part of the <sup>fi</sup>gure, we show the redesigned processes, while the lower part shows the underlying digital infrastructure. The process innovation is facilitated by lightweight IT, which is <sup>fl</sup>exible innovative technology and its user base. Between them are architectural mechanisms, which mediate between a broad range of systems in the digital infrastructure and the process innovation initiatives. The architectural mechanisms are powerful resources to establish a connection between systems and user services, and we de<sup>fi</sup>ne them as sociotechnical mechanisms that enable alignment between architectural elements, in establishing a connection between core resources and user services. One key type of mechanism is boundary resources.

These de<sup>fi</sup>nitions are our theoretical foundation, but in practice, there are many unsolved questions. We need to identify the architectural mechanisms at work, and we should investigate under which conditions they will work, and how they actually cause outcomes. A more <sup>fi</sup>ne-grained investigation was needed.

![](/api/attachments/DEGHJVE6/fulltext/images/343d5bafb5d801a5c7b3024a18e6759d27dbaab8582dc9b6d86bbb52dc6fdd38.jpg)  
Analytical framework.

![](/api/attachments/DEGHJVE6/fulltext/images/f4fc76ad21ea621c15ce573b0d929a3e63cbe53db6bb7960971690b72c86c418.jpg)  
Østfold hospital (Photo: Health South-East).

## 4. Research method

## 4.1. Case study design

We chose an in-depth case study because the research question asked for a detailed investigation of a phenomenon in its real context (Yin, 2013). In selecting the case, we followed Gerring’s (2007) typology and selected an extreme case, which is prototypical or paradigmatic of some phenomenon of interest. In order to investigate architectural mechanisms, we build on critical realism (Bhaskar, 1998; Sayer, 2000) in our data analysis. Thus, in our analysis, we are aiming to retroduce causal mechanisms.

Our selected case was a brand-new hospital in Norway, the Østfold Hospital. It opened autumn 2015 and was presented as the most modern hospital in Europe, in its use of information technology and process orientation. Thus, it satis<sup>fi</sup>ed our key criteria; it was quite ambitious in both our areas of interest and o<sup>f</sup>ered a unique opportunity to study the interplay of process design with digital infrastructure.

## 4.2. Data collection

We conducted an intensive study over two years, with interviews, observations, participation in workshops and seminars, and documents as our data sources. The interviews were in-depth, semi-structured and open-ended. Key questions included how they addressed the process innovation e<sup>f</sup>orts strategically, as well as the involved various organisational actors in the process. A central question became how they approached the identi<sup>fi</sup>ed requirements for a new process technology, and how they addressed the challenge of aligning this technology with the existing digital infrastructure. The interviews were transcribed and analysed. We also performed several observations in order to compare espoused strategy from management with actual outcome within the organisation.

In line with our perspective, our data collection strategy consisted of three di<sup>f</sup>erent activities:

● To understand the patient logistics strategy, we interviewed top managers in the health region and at the hospital, the Chief Information O<sup>fi</sup>cer (CIO), line managers and clinicians. We also observed clinicians at whiteboard meetings and the practical work at the emergency unit, as well as how coordinators used whiteboards and mobiles in moving patients throughout the hospital.

● To map the digital infrastructure, we interviewed IT personnel at the Østfold hospital and the South-East Regional Authority and the regional IT Centre. We also interviewed vendors and consultants and collected strategy plans, project plans, requirements speci<sup>fi</sup>cations, and status reports.

● We participated in workshops and seminars both arranged locally by Østfold hospital as well as regional workshops arranged by Health South-East (HSE). These workshops raised several interesting debates also regarding Østfold hospital as a role model for other hospitals.

In order to develop converging lines of inquiry in a complex case (Yin, 2013), we built – iteratively, as trends and topics emerged – on multiple sources. See Table 2.

## 4.3. Data analysis

Our point of departure in this paper was di<sup>fi</sup>culties related to aligning a new management-oriented process innovation initiative with the existing digital infrastructure. As Beverungen (2014) emphasised, the alignment of these e<sup>f</sup>orts is not trivial since business process management is often considered as a topdown management activity, inconsistent with the observation that information infrastructures are at drift, outside direct top-down management control.

Addressing these challenges, and how Østfold approached them, we analysed our case in four steps (see Table 3). First, we established a chronology where key events and key challenges were described as Østfold embarked on the e<sup>f</sup>ort to enable structured interaction between process-oriented technology and the digital infrastructure. Our description was discussed several times in workshops and in meetings with management, in order to verify the accuracy of our <sup>fi</sup>ndings and to assess our interpretation.

Data collection.

<table><tr><td>Data collection</td><td>Activity</td><td>Data</td></tr><tr><td>Interviews</td><td>34 interviews with CEO, CIO, Analytic experts, Process manager, Project managers, clinicians, staff</td><td>Goals and purpose of the project, strategic and organisational development and system/analytics implementation.</td></tr><tr><td>Observation</td><td>Around 60 hrs. of observation.</td><td>Views and results of the implementation, the relation between information and decision.Use of analytics to identify patterns of performance and production and decision-making.</td></tr><tr><td>Workshops</td><td>Workshops and seminars</td><td>Strategies, ambitions, and consequences of digital innovation at ∅stfold, and the role of ∅stfold in the bigger regional initiative.</td></tr><tr><td>Documentation</td><td>Documentation of process design, system design, and technical issues.</td><td>504 pages on system design, process descriptions, work descriptions. In particular, we were studying models and drawings describing architectural issues including physical architectures, subsystems, components, and how they were designed in layers.</td></tr></table>

Data analysis.

<table><tr><td>Step</td><td>Description</td><td>Outcome and output</td></tr><tr><td>1</td><td>Establishing a chronology (2013–18), and identify key events</td><td>5 phases from piloting to upstart, section 4.4</td></tr><tr><td>2</td><td>Analysing key events related to process innovation and interaction between new and existing technology</td><td>Section 5.</td></tr><tr><td>3</td><td>Identifying and analysing architectural mechanisms</td><td>Three architectural mechanisms, section 5.1–5.3</td></tr><tr><td>4</td><td>Theorising alignment in process innovation in digital infrastructures.</td><td>Section 6</td></tr></table>

Since the hospital building project also included IT, Østfold Hospital had considerable freedom to acquire process technology to solve process-oriented issues, outside regular regional IT budgets. Process technology that is primarily aimed at logistics and horizontal process improvement are relatively unusual in health care. Østfold Hospital, therefore, made an analysis of existing processes so that the various actors from management, clinical practice and administration could gain ownership of the processes, while also being able to gain insight into how the processes could be improved. The goal was to align new and existing technology in such a way that new processes were supported. Further, the project team focused on monitoring and improvement. For instance, although quite successful in the change from functional to process-oriented focus, Østfold Hospital identi<sup>fi</sup>ed challenges related to patient <sup>fl</sup>ow even after upstart and established a monitoring unit to continually maintain and improve process performance.

In step 2, through our interaction with the data and the structuring into chronological key events, we came to acknowledge the profound challenges related to enabling process innovation. Management and in particular the CIO was in constant negotiations with the regional IT Centre in order to communicate the need for an improved architecture to serve process innovation. This recon<sup>fi</sup>guring of the existing architecture had to be done while not interrupting clinical services. The regional IT Centre was not familiar with this type of process technology, while the CIO at Østfold had earlier worked with similar challenges in the private sector. We saw that there was a collaboration between Østfold management and regional IT over time and that negotiations and compromises were needed to obtain a su<sup>fi</sup>cient result.

In step 3 we conducted a causal analysis of the interaction between process technology and the digital infrastructure, drawing on the technique of retroduction (Sayer, 2000), aiming to identify the architectural mechanisms that enabled this interaction. This implied understanding the interaction of entities, i.e. the involved actors, the architectural layers, and subsystems as components, the <sup>fl</sup>ow of data, and the interaction between various subsystems through speci<sup>fi</sup>c interfaces. This allowed us to identify and describe three architectural mechanisms.

We saw that the process technology had the attributes to qualify as lightweight IT, i.e. con<sup>fi</sup>gurable technology, available on the market, with fast implementation (Bygstad, 2017). We then analysed how the lightweight IT interacted with the heavyweight IT (the existing digital infrastructure). We observed that both lightweight IT and heavyweight IT was central in reaching the goal, and we analysed the three architectural mechanisms that served as an explanation for the relatively successful alignment between the process initiative and the digital infrastructure. This also implies that we understand alignment as a gradual process, but that careful planning is needed to structure the collaboration between the various parties.

In the last step, we assessed the alignment mechanisms in order to resolve Beverungen’s problem; we found that the careful deployment of lightweight IT in onsite con-<sup>fi</sup>guration, loosely coupled from the infrastructure activities, allows for fast process innovation while acknowledging the slow and nonlinear evolution of infrastructure.

Our analysis also revealed some problematic issues; the Østfold project managers were not successful in all their e<sup>f</sup>orts. An example is a multi-booking system that was not implemented. The reason for this is brie<sup>fl</sup>y described in 5.4. The project team also experienced several setbacks through compromises that had to be done and ambitions that had to be reduced.

We continue by describing the case, including the phases Østfold Hospital went through to achieve their goals. We then in 5.1–5.3 describe three architectural alignment mechanisms that serve as an explanation for the overall success of the project. In 5.4 we brie<sup>fl</sup>y describe the terminated multi-booking project.

## 4.4. The case

In 1999 the Norwegian Parliament decided to build a new hospital in Østfold County. Østfold Hospital is part of the South-East Regional Health Authority, which covers around half of the Norwegian population, and has 80.000 employees. The construction at the new site started in 2010, and the hospital opened in November 2015, with both somatic and psychiatric services and 4800 employees (Figure 2).

![](/api/attachments/DEGHJVE6/fulltext/images/020697c5b379628e2741ae039b4e5cbe592b6a2c6a5142c1376c3c414e83bdd4.jpg)  
Architectural alignment mechanisms.

The Chief Executive O<sup>fi</sup>cer (CEO) of the hospital, Just Ebbesen, was a medical doctor and a pioneer in using IT to innovate and support clinical processes. He commented:

“I had been engaged with the relationship of process innovation and IT the past 15 years, both theoretically and practically, and I knew what I wanted to achieve: hospital processes should be well de<sup>fi</sup>ned and supported by information. The overall thinking was inspired by the theory of value configurations (Stabell & Fjeldstad, 1998), so the Moss hospital (30 km. away) was designed as the value chain (dealing with the standardised high volume cases), the Østfold (Kalnes) hospital as the value workshop (dealing with complex diagnoses and treatment) we needed a comprehensive communication solution for the value network (including clinicians, sta<sup>f</sup>, patients and municipalities)”.

## His ambition was expressed in these terms:

“New Østfold Hospital will be the best in Europe for process innovation through <sup>fi</sup>ve points. The work processes must be moved closer to the patient. We will use commercially available technology. The work processes will be simpli<sup>fi</sup>ed and mobile technology will support them.”

In 2011, he hired an energetic CIO with experience from production and retail, and in 2012 a Process Director, and established a top management team aiming to build a hospital built on process thinking and advanced IT solutions. The main approach was to implement a completely new solution to support the horizontal processes, with touchscreens, tablets, and mobile phones.

The chronology of the case is brie<sup>fl</sup>y described below.

Phase 1: Process modelling and IT piloting in old hospital 2013–15. Clinicians and IT personnel modelled a total of 65 processes. A separate group worked with the details of the lightweight solution, <sup>fi</sup>rst working with process steps; later con<sup>fi</sup>guring the di<sup>f</sup>erent views of the whiteboard solutions.

Phase 2: Establishing, configuring and testing new architectural solution 2013–2015

Østfold acquired a lightweight IT solution from Imatis, speci<sup>fi</sup>ed to support logistics and communication. This was organised as a sub-project, with an external consultant as project manager, working with a group of clinicians who had modelled and redesigned many processes. Regarding the existing digital infrastructure, the Østfold project had to deal with a “regional package” of more than 300 applications maintained and run by the regional IT Centre. The key applications were the electronic patient record (EPR) system, lab system, radiology system, and chart and medication system.

## The CIO commented:

“The process modelling was very useful. But the solution was new to the regional IT Centre, and integration with the clinical systems was demanding. I spent my days co-ordinating various vendors, the IT Centre, and the doctors. A number of unresolved issues and questions popped up: who has the responsibility for technical integration (Vendors? The IT Centre? We?) The enormous amounts of clinical information from sensors and medical equipment – should everything be stored? And so on . . . 22

The responsibility for parts of the start-up package was transferred in 2013 from the Digital Renewal programme to the Østfold Hospital Project, because of the tight deadline in 2015. Both the lab system and the chart and medication system were new and had to be integrated into the regional package at tight deadlines. An IT architecture team was established in Østfold, particularly to deal with the complex integration issues.

Phase 3: Start-up at the new hospital, Nov 2015. The start-up was successful, but narrowly so. The integration solution between the major clinical systems was complex, and some improvisation and shortcuts were done.

Phase 4: Stabilising solutions (Jan 2016-January 2017). A number of other issues emerged, but overall the situation in the autumn 2016 was satisfactory; a very innovative hospital had been established, for the bene<sup>fi</sup>t of both patients and clinicians.

Phase 5: Monitoring and improving performance (2016–2018). Patient <sup>fl</sup>ow did not work satisfactorily. To establish a data-driven improvement process improvement, an analytics team and several crossdisciplinary improvement teams were established, reporting to the process director.

Overall, the solution was quite successful and was widely recognised as innovative. In 2018, the Østfold solution was awarded level 6 at the HIMSS scale, where 7 is top. (HIMSS refers to the Healthcare Information and Management Systems Society, a global, cause-based, not-for-pro<sup>fi</sup>t organisation focused on better health through information and technology). However, it was recognised that the solution was not “<sup>fi</sup>nished”; it required continuous improvement and tuning.

## 5. Findings

Our analysis revealed three architectural mechanisms that explained important aspects of the success of the project; on-site configuration; vendor boundary resources and institutional boundary resources. (See Figure 3). The key architectural challenge was how to support the processes with a new layer of lightweight technology, and how to connect the new technologies to the heavyweight systems. The <sup>fi</sup>rst mechanism addresses usability and <sup>fl</sup>exibility aspects related to how an actor can con<sup>fi</sup>gure the system to solve practical challenges at hand. The second and third regard how various interface technologies establish value connections between information resources and user services.

The IT context was challenging. The region was at the time running an e-health mega-programme, “Digital Renewal”, aiming at integrating the most important clinical and administrative (silo) systems. The Digital Renewal programme of the Health South-East Region had established a regional IT architecture with an integration framework built on Microsoft BizTalk, enabling a large number of systems to exchange data within and outside the region. However, the integrated package was not ready yet, and progress was slow.

The “regional package” (a key part of the established infrastructure) consisted of more than 300 applications, maintained and run by the regional IT Centre in Oslo. The key applications were the electronic patient record (EPR) system, lab system, radiology system, and chart and medication system. The 2010 and 2012 IT plans of Østfold Hospital included this package, with some local additions.

The high priority and <sup>fi</sup>xed deadline of the Østfold hospital had led to a situation where the responsibility for systems integration was transferred from the regional level to the local project. This meant that the core clinical systems, such as the EPR, lab, radiology, and chart- and medication systems were con<sup>fi</sup>gured and tested by the project. Both the lab system and the chart and medication system were new and had to be integrated into the regional package at tight deadlines. The hospital was also a world test-case for implementing the chart- and medication system to be used not only at surgery units but also in wards. An IT architecture team was established in Østfold, particularly to deal with the complex integration issues.

## 5.1. Mechanism I: on-site con<sup>fi</sup>guration with lightweight IT

The <sup>fi</sup>rst mechanism is on-site configuration with lightweight IT, explaining how process modelling was supported by the particular attributes of lightweight IT.

The modelling and redesign of processes started in 2013, <sup>fi</sup>rst in the emergency unit; later in the wards. Around 25 clinicians and sta<sup>f</sup> were allocated full-time to the project, plus a number of external consultants. A work group, consisting of clinicians, IT personnel, organisation development specialists and IT architects modelled 65 work processes, each of them in considerable detail, with “swim lanes” (for roles) and the need for IT support in each step. Most of these work processes were sub-processes of 38 di<sup>f</sup>erent clinical pathways.

A key part of the process innovation initiative dealt with logistical issues such as:

● Receiving emergency patients arriving with ambulances or by taxi, registering them, conducting triage and medical diagnoses, and requiring additional services such as lab tests or radiology.

● Allocating newly hospitalised patients to wards and beds, and providing the necessary information to the sta<sup>f</sup>, and to the patient’s family.

● Setting up a clinical pathway for each patient, and allocating various resources and services in calendars

● Ensuring that each patient received exactly the medicines that the doctor(s) had prescribed (“closed-loop medication”).

● Co-ordinating the discharge of patients with municipalities. For instance, the municipal care institutions required that information on an incoming patient should be sent before noon.

● Providing the kitchen with exact information on how many meals, dietary requirements, room numbers, etc.

● Providing the cleaning department with timely information on which rooms to clean, and when.

● Creating a real-time (graphical) logistics overview for management, to ensure an optimal <sup>fl</sup>ow of patient and use of resources

While these needs may sound straightforward, the reality was that each of them required a very careful design of the process and that almost every step of the process was dependent on reliable information from various IT systems.

The most innovative and prestigious solution in Østfold Hospital was the Imatis solution, (see <sup>fi</sup>gure 4–7). The Imatis solution was an example of what has been called lightweight IT (Bygstad, 2017; Lacity & Willcocks, 2015); i.e. commercially available IT components, relatively easy to implement, and loosely coupled to the heavyweight systems. The project manager commented:

“When we started work on process innovation at Østfold in 2013, the EPJ system was not ready, while Imatis had a solution already. We travelled to Denmark to see how Imatis was used in a hospital there”

The lightweight Imatis solution used self-check-in automats, mobile phones, tablets and electronic whiteboards, which were modelled in the processes. The extensive solution had to be detailed to give su<sup>fi</sup>cient support, and workshops were regularly held to connect and con<sup>fi</sup>gure technology and tasks. Then, practical solutions with electronic whiteboards, mobile phones and tablets had to be found, dealing with many vendors.

The Imatis solution included:

● A solution for patient self-check-in and dealing with queues

● A system for visualisation of patient <sup>fl</sup>ow and logistics, with whiteboards

● A message broker for distribution of messages to mobile phones and other units

The chief nurse commented:

“The whiteboards place a lot more focus on logistics, they provide a better overview and make more work processes easier. We are experiencing important improvements in emergency reporting routines and we have also signi<sup>fi</sup>cantly reduced the number of phone calls”

![](/api/attachments/DEGHJVE6/fulltext/images/2f93b4d71eab02b4d76e4acd5ed58af3f1817c0712491eaf6f35662d3cf3123d.jpg)  
Self-check-in automates.

The Imatis solution showed how lightweight IT could mediate e<sup>f</sup>ectively between the processes and the existing digital infrastructure; in fact, most of the redesigned processed were informed by the solution. As illustrated in Figure 7 the solution was extensive and supported the <sup>fl</sup>ow of information between the major clinical systems, medical surveillance instruments, ambulance systems and the mobile terminals of both clinicians and patients. Access and security were role-based, enabling <sup>fl</sup>exible use of equipment. The software was con<sup>fi</sup>gurable, and features were adjusted as personnel experienced daily use.

The lightweight solution was particularly useful for horizontal processes (see Figures 4 and 6). For instance, the interplay between the emergency unit and the wards had been unsatisfactory, where the emergency co-ordinator used to call all wards to <sup>fi</sup>nd an available bed. With the whiteboard solution, she could now enter a visual overview of all the available beds, and the means to reserve a bed. When this was routinised, the whole atmosphere in the wards improved a lot, because the telephones stopped ringing. “It is a completely new work situation for me”, said the co-ordinator, “because the whiteboard enables me to have full overview and control of the process”.

![](/api/attachments/DEGHJVE6/fulltext/images/805fb1786e74b1624d7b47a868ffef1320aa6bc3d1eaba22cc61b50565bebde9.jpg)  
On-site con<sup>fi</sup>guration.

![](/api/attachments/DEGHJVE6/fulltext/images/709d703e8b00dabb5a64d1f9d2db1aa9838209fbcc63e31b25a53e3b78e6bcf3.jpg)  
Patient visualisation and logistics. Each row represents the status of one patient (name in column #7). Allocating <sup>Figure 6.</sup>resources to a patient, such as room, nurse or x-ray, is done by drag-and-drop in the whiteboard.

![](/api/attachments/DEGHJVE6/fulltext/images/3d3b97eb4471c4efe1ec9d7173aebe22e9778d65fc29e529791d6a60945a8681.jpg)  
The Østfold solution. Imatis resource and process manager (centre of <sup>fi</sup>gure) as an interface between lightweight IT and <sup>Figure 7.</sup>heavyweight IT. The lightweight IT consists of user-friendly technology (mobile technology and electronic whiteboards) while the heavyweight IT layer consists of the clinical systems as well as the electronic patient record system. (Norwegian text).

An example of a session that has bene<sup>fi</sup>ted from the visualised and con<sup>fi</sup>gurable interfaces was the daily “whiteboard meeting” (see Figure 4). It starts at 0850 and lasts for 10 minutes. In this meeting, the ward patients are discussed in order to identify who can be discharged. The head of the unit manages the whiteboard registrations, while the doctors and nurses give feedback. The patients are divided into three categories: 1. immediate help, 2. Patients who can be discharged, 3. Patients who have to stay another day. The con<sup>fi</sup>gurable interfaces are powerful also in that a broad range of objects can be used to visualise with coloured icons, and alerts particular aspects of the condition of each patient (balance problems, di<sup>fi</sup>culty eating, allergies, epilepsy, and so forth). It is also very easy to manage the change of responsible clinician for a particular patient, through drag-and-drop functionality. Updated information is also immediately noti<sup>fi</sup>ed to all important systems through the message exchange functionality (see 5.2)

## 5.2. Mechanism II: vendor boundary resources

The second mechanism was vendor boundary resources, i.e. the means with which the user services are technically orchestrated, and how access to heavyweight data resources is provided. A central functionality for enabling on-site con<sup>fi</sup>guration of important information was the Resource and Process Management System with Message Alerts (RPSM). This system consisted of three modules: self-check-in and queue management; patient visualisation and logistics; and a system for advanced message exchange to mobile devices. These modules were supported by the application and integration system.

## 5.2.1. Self-check-in and queue management

The self-check-in and queue management module have three main functions: patient notifying (through SMS), check-in and queue-management for patients; queue visualisation for clinicians (and other employees) to manage appointments and patient waiting time as well as allocating personnel according to particular patient requirements; and messages to inform patients when important changes are made in the schedule. The main role of this module then is to keep core actors up to date regarding the various schedules. The module is made possible through the architectural framework consisting of several application program interfaces (API) and modular views that enables a loose connection between Imatis and the respective heavyweight systems.

## 5.2.2. Patient visualisation and logistics

The purpose of this module was to make it easier to get a real-time overview of key patient information as well as information on important resources information at the department, in order to improve patient <sup>fl</sup>ow. An important function is that the system allows users to get an overview of the patient’s status without disturbing the work<sup>fl</sup>ow. Often at hospitals, clinicians spend a lot of time <sup>fi</sup>nding patients, looking up information systems or calling other departments to inquire about test results, etc. Research has shown that hospitals that have implemented solutions that visualise patient <sup>fl</sup>ow have experienced a signi<sup>fi</sup>cant improvement in productivity, as well as better control of logistics and patient <sup>fl</sup>ow. A nurse commented:

“An additional strength of Imatis is its visual power. We can use certain icons to emphasize particular aspects of the patient’s conditions that need to carefully be taken into consideration. Examples are bleedings, pain, level of consciousness, or allergies. We can also use it to visualize the status of the patient treatment and attach certain resources to it”.

Figure 6 demonstrates whiteboard functionality both related to <sup>fl</sup>ow and visualisation. The whiteboard is con<sup>fi</sup>gured for a particular ward and the status on each room (occupied, to be discharged or available) is displayed. Further, each room is connected to a patient (Østfold has one patient per room policy), and particular medical issues on the patient are displayed graphically. Each patient is also connected to a clinician in charge. Even if this may sound straightforward and commonsensical, hospitals have struggled to reach this level of management.

## 5.2.3. Message exchange

The message exchange module was a comprehensive structure to manage and secure the distribution of messages to a broad range of di<sup>f</sup>erent receivers (see Figure 7). Examples are users, security systems, <sup>fi</sup>re systems, clinical events, and other alarms. Horizontal co-ordination is very much about communication. The message exchange module dealt with authentication and role management, providing basic message delivery to users, functions and responsible roles. In addition, the message exchange module dealt with various emergency situations, such as the provision of patient signal alerts, dissemination of emergency alerts, and position-based events. It co-ordinated the porter service and other support services. Finally, it surveilled the status of technical systems such as <sup>fi</sup>re and security systems, automatic guided vehicles, and other transport systems.

A crucial issue was to access the heavyweight clinical systems from the vendor boundary mechanism. i.e. the Resource and Production System (shown in the middle of Figure 7). When the CIO in 2013 contacted the owners of the clinical systems to identify how the APIs worked, a typical answer was, “our current version does not provide an API, and – by the way – there is nothing in our contract that allows a $3 ^ { \mathrm { r d } }$ party software vendor to access to our data.” As shown in Figure 7, these problems were gradually resolved. The mechanism to accomplish this was the institutional boundary resources.

## 5.3. Mechanism III: institutional boundary resources

The third mechanism was institutional boundary resources, i.e. the interface to the heavyweight clinical and administrative systems, as well as functionality for enabling message <sup>fl</sup>ow within and between systems. The Østfold project manager commented:

“The regional integration solution was gradually established. It was di<sup>fi</sup>cult to involve the central IT unit (HospitalPartner), and the Østfold project had to do much of the development itself. The EPR interface was too simple and the message broker was not ready. We needed to do major adjustments. Eventually, the integration engine – a BizTalk solution – consisted of 90 interfaces (everything from building systems to radiology, labs and clinical information).”

The regional IT unit Hospital Partner was established in 2003. Before 2003, each hospital had its own IT unit, and many hospitals adopted integration technology based on Microsoft BizTalk. Hospital Partner further built on this solution and established a unit called the

Integration Factory. The Integration Factory is responsible for all integration e<sup>f</sup>orts within Health South-East and all information sharing and integration between IT solutions take place through the Integration Factory. The solution enables routing of messages between the main EPR system and systems from several clinical disciplines. The integration solution (Figure 8) includes several functional aspects.

The <sup>fi</sup>rst aspect is how vendors’ APIs make data from each system available. In the health sector, systems have often operated in isolation and APIs have mainly consisted of less standardised structures meant to provide resources for internal programmers and users. Through the increasing need for interaction between various systems, system vendors are required to create more accessible interfaces from where important information can be harvested. Even though systems are required to improve their API’s, message standards often vary, something that will make interaction challenging. The integration factory thus needs to make sure that messages are interoperable. This is done through a message broker where messages are received, transformed – in order to comply with certain standards – and exchanged to other systems.

A second aspect concerns how the systems and their APIs interact through the integration solution within a local hospital context. Historically clinicians have been required to log into several systems updating each one of them when treatment has been performed. With standardised messages, information is registered in one system and then updated in all the others that are relevant for this particular information.

A third aspect is how information is made available across the entire region. When patients are moved between hospitals, information previously was often sent on paper by hard mail or taxi and had to be digitally registered once again at the receiving hospital.

When information is made digitally available across hospitals – even if it is only a limited part of the patient record – hospitals may relieve resources and work more e<sup>f</sup>ectively.

In short, then, this mechanism of institutional boundary resources enables access to regional information repositories, something that enables digital exchange of information and thus more e<sup>f</sup>ective interaction.

## 5.4. Unresolved process issues

The innovation project at Østfold did not succeed in all their e<sup>f</sup>orts. The interaction between lightweight IT and heavyweight infrastructure was demanding, and the most ambitious process aim failed for this reason. The planned multi-booking solution aimed at solving one of the key process issues, namely to book the necessary resources for a clinical pathway based on a speci<sup>fi</sup>c diagnosis. For instance, if a patient is diagnosed with breast cancer, a multi-booking system would (automatically) generate a detailed schedule for the patient, including oncologist consultations, x-ray, surgery, and other activities. The bene<sup>fi</sup>ts would be considerable, both for the patient and for internal logistics. Unfortunately, the solution failed; although satisfactory software was tested, integration with the EPR systems proved too di<sup>fi</sup>cult, partly because of con<sup>fl</sup>icting vendor interests. In addition, the multi-booking solution required all plans to be laid 6 months ahead. This requires tighter coordination between clinical and technical practices across disciplines, which again reduces the <sup>fl</sup>exibility for each discipline. Østfold hospital did not succeed in getting the necessary agreements in place for such a change.

![](/api/attachments/DEGHJVE6/fulltext/images/e08b10e534132a7df5441bf0600f9348556af049e00ccda546b4177ddf792c8c.jpg)  
Integration framework and institutional boundary resource (Norwegian text). The integration platform (BizTalk) at <sup>Figure 8.</sup>the centre enables interaction between electronic patient journal (DIPS) and clinical specialist systems (“Fagsystem”). The integration platform also transforms messages from system standards to common standards. The Gateway (on top of the <sup>fi</sup>gure) supports data exchange with other hospitals.

## 6. Discussion

In this section, we return to Beverungen’s problem (Beverungen, 2014) as a key challenge for our process innovation approach. Beverungen’s problem is based on the insight that there is an incongruence between rational top-down business process management and the fact that digital infrastructures are large, fragmented and complex system landscapes that operate outside of management control. This incongruence makes alignment very challenging. Addressing this key issue, we raised the research question:

● How can a process innovation initiative successfully align with an underlying digital infrastructure?

We operationalised Beverungen’s problem into two challenges. First, how can we connect and reconcile the rational design innovation process to a large infrastructure that is characterised by drift and ambiguity? Second, how can we design an IT architecture that connects the IT-supported processes with the infrastructure? These issues will be addressed respectively in 6.1 and 6.2

## 6.1 How can we connect and reconcile the rational design innovation process to a large digital infrastructure?

In section 2 we introduced and discussed process innovation and digital infrastructure as two quite different approaches to digitalisation (see Table 1). Our empirical work, described in section 5, revealed that (i) the careful deployment of lightweight IT in onsite con<sup>fi</sup>guration, loosely coupled from the infrastructure activities, allows for fast process innovation while leveraging the slow and nonlinear evolution of infrastructure, and (ii) the interaction between lightweight IT and large clinical systems by two types of boundary resources (vendor and institutional) resolves the tension between innovation and infrastructure.

From a more theoretical perspective, we propose that the two approaches can be aligned, but not integrated. This means that they resolve di<sup>f</sup>erent problems; process innovation deals with top-down incremental or radical improvement, preferably with light engineering, while digital infrastructure theory focuses on the growth of the stable installed base, partly outside of managerial control.

Alignment has both cognitive and social linkages (Reich & Benbasat, 2000). The cognitive linkages (i.e. content and methodologies) work if the involved actors understand and recognise the basic assumptions of the other part. For instance, in the Østfold case, the process innovation team asked for speci<sup>fi</sup>c data to support the processes but did not present an architectural view, connecting to the digital infrastructure. The process models from Østfold were incompatible with the technical documentation of the IT Centre. The IT Centre did not recognise the need for the proposed lightweight solutions and found it hard to understand why the hospital just couldn’t use the existing solutions. Gradually, with the help of the Østfold project manager, the IT Centre people understood the purpose of the process innovation.

The social linkages (i.e. actor interactions, and values) work if the involved actors interact with the intention of solving problems, based on shared values. In the Østfold case, the process innovation team initially grew very impatient with the slow response to their requests. The IT department, on the other hand, did not understand the innovative potential at Østfold, and treated the request bureaucratically, i.e. putting them in the queue. Over time, this improved (but was never quite resolved), as the actors understood and recognised more of the other part’s challenges.

We can regard this division of labour as an example of bimodal IT (Ha<sup>f</sup>ke, Kalgovas, & Benlian, 2017). The concept was developed by practitioners, aiming to address the problem that the IT function often does not e<sup>f</sup>ectively balance exploratory and exploitative tasks. The suggested solution was to divide the IT department into two parts; one to support the business with exploratory digital innovation, while the other maintains traditional IT operational performance. The exploratory (process innovation) part was in the Østfold case supported by lightweight IT.

What is the role of lightweight IT in this division of labour? BPM research has found that organisations with knowledge-intensive and creative processes encounter certain challenges when streamlining their work<sup>fl</sup>ow (Seidel, Müller-Wienbergen, & Becker, 2010). Process innovation should therefore aim to (i) avoid heavy engineering, (ii) use existing technologies in an innovative way (Schmiedel & Brocke, 2015).

In the Østfold case, digital process support was designed and implemented by the process innovation teams in co-operation with the vendor. Much of the con<sup>fi</sup>guration was done by clinicians and super-users, requiring no programming. Lightweight IT is a con<sup>fi</sup>gurable, innovative and user-friendly technology, as well as the surrounding knowledge regime, plastic enough to support many types of processes.

The attributes of lightweight IT were important, in the sense that the processes were not automated, i.e. strongly structured by IT, but rather informated (Zubo<sup>f</sup>, 1988). This meant that clinical personnel was equipped with relatively <sup>fl</sup>exible IT tools, such as mobile phones and electronic whiteboards, to support their tasks, but in a problem-solving way. This is congruent with the insight regarding the user perspective from the BPM literature, as “technology should be accessible according to a pull principle where knowledge workers can access a tool in order to solve the problem at hand” (Vom Brocke & Rosemann, 2015, p 6). The lightweight IT could also be recon<sup>fi</sup>gured by local IT sta<sup>f</sup> if needed. Therefore, lightweight IT is a central part of our suggested con<sup>fi</sup>guration, enabling incremental design and implementation. We see lightweight IT as an emergent process innovation technology that changes the way people work and enable more dynamic processes, or more dynamic con<sup>fi</sup>guration of processes (Kemsley, 2015)

We resolve one part of Beverungen’s problem by using existing technologies in an innovative way, since the digital infrastructure is established as a central foundation, and with improved interfaces towards external units. We do however also add something to Beverungen’s analyses in that we demonstrate how modern innovative technology can leverage core information and make it con<sup>fi</sup>gurable on a user level. We thus see lightweight IT and heavyweight IT as compatible, rather than con<sup>fl</sup>icting technologies (Bygstad & Iden, 2017).

## 6.2. How can we design an IT architecture that connects the IT-supported processes with the infrastructure?

We address this issue by building the concept and technical solution of boundary resources (Ghazawneh & Henfridsson, 2013). i.e. tools and regulations that serve as interfaces between the digital infrastructure and the lightweight user services. The key elements in the envisioned technical architecture (which draws on the Østfold solution, shown in Figure 7) are the lightweight user services, the boundary services, and the digital infrastructure. In practical terms, this means that the (lightweight) vendors are responsible for the integration of the user services, while the IT department of the organisation is responsible for connecting to the various heavyweight systems of the digital infrastructure.

The lightweight user services are supporting the business processes by providing functionality and information for the user, often mediated by mobile technology or visual displays (Øvrelid, Sanner, & Siebenhertz, 2018; Torkilsheyggi & Hertzum, 2017). Lightweight solutions are often provided by innovative $3 ^ { \mathrm { r d } }$ party vendors. Recent BPM philosophy is based on an approach where heavy engineering is avoided, and existing technology is used (Schmiedel & Brocke, 2015; Vom Brocke & Rosemann, 2015). This requires a recon<sup>fi</sup>guration of the existing portfolio to lay the foundation for improved user services.

The digital infrastructure is, from an architectural view, a portfolio of organisational systems, which serves as repositories of information in large databases. In this context we can regard them as platforms, i.e.

large transactional registers of information created and used by various actors in the ecosystem (Islind et al., 2016). The platform function, however, does not imply a classical two-sided platform structure; rather, the digital infrastructure is complex and heterogeneous.

The boundary services are in this context the software that connects the user services with the underlying systems. Boundary resources are structured interfaces between systems and services. They enable digital interaction between systems in order to bring the fragmented system portfolios more in systematic relation and enable extensive access to information. Technically, they also enable modularisation and loose coupling (Parnas, 1972) between system modules. Importantly, boundary resources provide security and control mechanisms, supporting important governance and quality policies.

Bygstad and Hanseth (2018) revealed two types of boundary resources in complex architectures; vendor and institutional. In our case analysis, we showed how vendor boundary resources orchestrated the user services, and how access to heavyweight data resources was provided. We also showed how vendor boundary resources communicate with institutional vendor resources (i.e. the BizTalk solution) in order to get access to the underlying digital infrastructure. The institutional boundary resources are crucial for maintaining security and privacy.

Architectural alignment is, then, the orchestration of the elements described above. Lightweight IT with modular and layered architecture facilitates loose coupling between systems components and makes change easier. The digital infrastructure (heavyweight IT) gives the new integrated systems access to powerful information repositories positioned in various core systems, as well as a securing function that establish trustful relations. This is enabled and secured by the boundary resources. The result is a loose coupling between the layers, enabling fast process innovation, and slow evolution of the digital infrastructure.

## 6.3. Implications for the BPM community

In their comprehensive literature review of BPM research, Recker and Mendling (2016) validated BPM as a mature <sup>fi</sup>eld with several strong contributions to research. However, the researchers also pointed to two areas where BPM researchers have had less focus, i.e. (i) process discovery is given signi<sup>fi</sup>cantly more attention than the subsequent activities, such as process improvement in the BPM cycle, and (ii) that there is a lack of methodologically strong empirical and theoretical research.

We suggest that we contribute to both these points. First, our study demonstrates the challenges of aligning business processes with an existing, layered and complex digital infrastructure. In our study, focusing on the implementation of process redesign, we demonstrate how alignment was made possible by adding a layer of process technology upon the digital infrastructure. We also investigated the necessary architectural mechanisms for achieving this.

Second, our <sup>fi</sup>ndings were derived and theorised on the basis of a comprehensive case study at a general hospital in Norway, and are thus primarily empirical. Our <sup>fi</sup>ndings were built on a rich empirical material, consisting of interviews, observations and document analyses, and our conclusions are based on a consistent chain of evidence. We propose that this enriches and deepens our knowledge in the <sup>fi</sup>eld, for both researchers and practitioners.

## 6.4. Implications for practice

The practical contribution can be summarised in the following. Connecting process innovation and digital infrastructure is necessary for the success of such initiatives, but the case illustrates that large digital infrastructures cannot be “designed” top-down, but evolve through architectural growth. As illustrated in the Østfold case a careful use of architectural mechanisms may enable bene<sup>fi</sup>cial solutions.

Further, the role of lightweight IT shows how an intermediating technology, relatively loosely coupled to the digital infrastructure, o<sup>f</sup>ers the agility and <sup>fl</sup>exibility to support process innovation. It also shows a way forward, to more platformoriented solutions (Bygstad & Hanseth, 2018; Tiwana, 2013) in e-health, in the sense that it decouples lightweight interfaces from the main applications. Also, competence is critical. In the Østfold case there was a fortunate mix of competences; a visionary top manager, a process-oriented director of development, and a hands-on CIO, who worked equally enthusiastically with architectural issues as with mobile phone con<sup>fi</sup>gurations.

Finally, previous research (Chan & Reich, 2007) has shown that alignment is complex and dependent on many factors, and we should therefore expect that e<sup>f</sup>ective alignment mechanisms are highly dependent on the particular context in which the project is conducted. For instance, in the Østfold case, an obvious success factor was that the integrated project (the IT project being part of the building project) supported the technical solutions much better than a regional project would have done. Would the same have been feasible in another context, for instance in an established hospital? It is possible, but evidence from many failed similar initiatives (Bjørn & Kensing, 2013; Ellingsen, Monteiro, & Røed, 2013) suggests that it would have been much more challenging.

## 7. Conclusion

Digitalisation is a convenient term but denotes complex organisational change, where the physical and the digital are entwined and con<sup>fi</sup>gured in new ways. It includes usually both process innovation and changing digital infrastructure. In this paper, we investigated the alignment of these two forces in a high-tech hospital.

We found that (i) the careful deployment of lightweight IT in onsite con<sup>fi</sup>guration, loosely coupled from the infrastructure activities, allows for fast process innovation while leveraging the slow and nonlinear evolution of infrastructure (ii) the interaction between lightweight IT and large clinical systems by a set of boundary resources resolves the tension between innovation and infrastructure.

Our main contribution is a model to describe the interaction between lightweight IT and heavyweight in order for process innovation e<sup>f</sup>orts to successfully interact and align with a large existing digital infrastructure. The key to successful interaction is three architectural alignment mechanisms that enable interaction between core information and user services. This con<sup>fi</sup>guration is not smooth; it requires ongoing negotiation between con<sup>fl</sup>icting forces, and it requires the courage to accept a less streamlined development. This, however, is perhaps the characteristic of digital innovation?

## Disclosure statement

No potential con<sup>fl</sup>ict of interest was reported by the authors.

## ORCID

Bendik Bygstad http://orcid.org/0000-0002-9025-3591

## References

Beverungen, D. (2014). Exploring the interplay of the design and emergence of business processes as organizational routines. Business & Information Systems Engineering, 6, 191–202.

Bhaskar, R. (1998). General introduction. In M. S. Archer, R. Bhaskar, A. Collier, T. Lawson, & A. Norrie (Eds.), Critical realism: Essential readings (pp. ix–xxiv). London: Routledge.

Bjørn, P., & Kensing, F. (2013). Special issue on information infrastructures for healthcare: The global and local relation. International Journal of Medical Informatics, 82 (5), 281–282.

Bygstad, B. (2017). Generative innovation: A comparison of lightweight and heavyweight IT. Journal of Information Technology, 32(2), 180–193.

Bygstad, B., & Hanseth, O. (2018). Transforming digital infrastructures through Platformization. Proceedings of European Conference of Information Systems (ECIS), Portsmouth, UK.

Bygstad, B., & Iden, J. (2017). A governance model for managing lightweight IT. World Conference on Information Systems and Technologies, Recent Advance in Information Systems and Technologies (pp. 384–393). Springer.

Chan, Y., & Reich, B. H. (2007). IT alignment: What have we learned? Journal of Information Technology, 22(4), 297–315.

Ciborra, C. Associates. (2000). From control to drift: The dynamics of corporate information infrastructures. Oxford, UK: Oxford University Press.

Ciborra, C., & Hanseth, O. (2000). Introduction. In Ciborra and associates, From control to drift: The dynamics of corporate information infrastructures (pp. 1–11). Oxford, UK: Oxford University Press.

Comella-Dorda, S., Lohiya, S., & Speksnijder, G. (2016). An operating model for company-wide agile development. McKinsey Digital. Retrieved from https://www.mckin sey.com/business-functions/mckinsey-digital/ourinsights/an-operating-model-for-company-wide-agiledevelopment

Constantinides, P., Henfridsson, O., & Parker, P. (2018). Introduction – Platforms and Infrastructures in the Digital Age. Information Systems Research, 29(2), 381–400.

De Vries, J., & Huijsman, R. (2011). Supply chain management in health services: An overview. Supply Chain Management: An International Journal, 16(3), 159–165.

Edwards, P. N., Jackson, S. J., Bowker, G., & Knobel, C. P. (2007). Understanding infrastructure: Dynamics,tensions, and design. Retrieved from https://deepblue.lib. umich.edu/handle/2027.42/49353

Ellingsen, G., Monteiro, E., & Røed, K. (2013). Integration as interdependent workaround. International Journal of Medical Informatics, 82(82), 161–169.

Gerring, J. (2007). Case study research: Principles and prac tices. New York: Cambridge University Press.

Ghazawneh, A., & Henfridsson, O. (2013). Balancing platform control and external contribution in third-party development: The boundary resources model. Inform Systems Journal, 23(2), 173–192.

Giddens, A. (1984). The constitution of society. Cambridge: Polity press.

Gregory, R. W., Kaganer, E., Henfridsson, O., & Ruch, T. J. (2018). IT Consumerization and the transformation of IT governance. MIS Quarterly, 42(4), 1225–1253.

Ha<sup>f</sup>ke, I., Kalgovas, B., & Benlian, A., (2017). «The transformative role of bimodal IT in an era of digital business”. In Hawaii International Conference on System Sciences (pp. 5460–5469), Waikoloa Beach, HI.

Hammer, M. (2015). What is business process management? In J. V. Brocke & M. Rossemann (Eds.), Handbook on business process management 1: Introduction, methods and information systems (2nd ed., pp. 3–16). New York: Springer.

Hammer, M., & Champy, J. (1993). Reengineering the corporations. NYC: Harper.

Hanseth, O., & Lyytinen, K. (2010). Design theory for dynamic complexity in information infrastructures: The case of building internet. Journal of Information Technology, 25(25), 1–19.

Harmon, P. (2010). The scope and evolution of business process management. In J. Vom Brocke & M. Rosemann (Eds.), Handbook on business process management. Introduction, methods and information systems (pp. 37–81). Berlin: Springer.

Henderson, J. C., & Venkatraman, N. (1993). Strategic Alignment: Leveraging information technology for transforming organizations. IBM Systems Journal, 32(1), 4–16.

Henfridsson, O., & Bygstad, B. (2013). The generative mechanisms of digital infrastructure evolution. MIS Quarterly, 37(3), 907–931.

Hertzum, M., & Simonsen, J. (2019, Feb). Con<sup>fi</sup>guring information systems and work practices for each other: What competences are needed locally? International Journal of Human-computer Studies, 122, 242–255.

Islind, A. S., Lindroth, T., Snis, U. L., & Sørensen, C. (2016). Co-creation and <sup>fi</sup>ne-tuning of boundary resources in small-scale platformization. In U. Lundh Snis (Ed.), Nordic contributions in IS research. SCIS 2016. Lecture notes in business information processing (Vol. 259, pp. 149–162). Cham: Springer.

Kemsley, S. (2015). Emerging technologies in BPM. In J. V. Brocke & T. Schmiedel (Eds.), BPM – Driving innovation in a digital world (pp. 3–15). Switzerland: Springer.

Lacity, M., & Willcocks, L. (2015). Robotic process automation at telefonica O2. MIS Quarterly Executive, 15(1), 21–35.

Monteiro, E. (1998). Scaling information infrastructure: The case of next-generation IP in the internet. The Information Society, 14(3), 229–245.

Øvrelid, E., Sanner, T. A., & Siebenhertz, A. (2018). Creating coordinative paths from admission to discharge: The role of lightweight IT in hospital digital process innovation. Proceedings of the 51st Hawaii International Conference on System Sciences, Big Island, Hawaii, USA.

Parnas, D. L. (1972). On the criteria to be used in decomposing systems into modules. Communications of the ACM, 15(12), 1053–1058.

Pentland, B. T., & Feldman, M. S. (2005). Organizational routines as a unit of analysis. Indust. Corporate Change, 14(5), 793–815.

Pentland, B. T., Liu, P., Kremser, W., & Hærem, T. (2019). The dynamics of drift in digitized processes. MIS Quarterly (forthcoming).

Recker, J. (2014). Suggestions for the next wave of bpm research: Strengthening the theoretical core and exploring the protective belt. Journal of Information Technology Theory and Application, 15(2), 5–20.

Recker, J., & Mendling, J. (2016). The state-of-the-art of business process management research as published in the bpm conference: Recommendations for progressing the <sup>fi</sup>eld. Business & Information Systems Engineering, 58 (1), 55–72.

Reich, B. H., & Benbasat, I. (2000). Factors that in<sup>fl</sup>uence the social dimension of alignment between business and information technology objectives. MIS Quarterly, 24 (1), 81–111.

Sayer, A. (2000). Realism and social science. London: Sage Publications.

Schmiedel, T., & Brocke, J. V. (2015). Business process management: Potentials and challenges of driving innovation. In J. V. Brocke & T. Schmiedel (Eds.), BPM – Driving innovation in a digital world (pp. 3–15). Switzerland: Springer.

Seidel, S., Müller-Wienbergen, F., & Becker, J. (2010). The concept of creativity in the information systems discipline: Past, present, and prospects. Communications of the Association for Information Systems, 27(1), 217–242.

Stabell, C. B., & Fjeldstad, O. D. (1998). Con<sup>fi</sup>guring value for competitive advantage: On chains, shops, and networks. Strategic Management Journal, 19(5), 413–437.

Tiwana, A. (2013). Platform Ecosystems: Aligning Architecture, Governance, and Strategy. Waltham, MA: Morgan Kaufmann.

Torkilsheyggi, A., & Hertzum, M. (2017). Incomplete by design: A study of a design-in-use approach to systems implementation. Scandinavian Journal of Information Systems, 29(2), 2017.

Vom Brocke, J., & Rosemann, M. (2015). Business process management. Wiley Encyclopedia of Management, 7, January, 1–9.

Weggelaar-Jansen, A. M., & van Wijngaarden, J. (2018). Transferring skills in quality collaboratives focused on

improving patient logistics. BMC Health Services Research, 18, 224.

Yin, R. (2013). Case study research. Beverly Hills, CA: Sage Publications.

Yoo, Y., Henfridsson, O., & Lyytinen, K. (2010). The new organizing logic of digital innovation: An agenda for information systems research. Information Systems Research, 21(4), 724–735.

Zubo<sup>f</sup>, S. (1988). In the age of the smart machine. New York: Basic Books.

## Appendix: Case study Østfold Hospital

## Interview Guide

Three groups of employees are interviewed: Clinicians, IT sta<sup>f</sup> and managers. The Interview Guide is not a questionnaire, but a checklist. The sequence of questions may vary, and follow-up questions may be asked.

Part 1: Current work situation 1 Please describe your current responsibility and work situation 2 Which tasks and processes are you involved in? 3 How are the processes documented? 4 Which digital solutions do you use in these processes? 5 Can you also show us how you use the digital solutions? 6 Are there problems and issues? How are they addressed? 6 How do you co-ordinate with other units? 7 Which managerial challenges do you experience? 8 To what degree do you have access to real-time information on the processes?

Part 2: New hospital project” 2013-15

9 What were your responsibilities in the “New hospital project”? Please start at the beginning, and go through the story. 10 If you were involved in the process redesign sub-project, please describe your role and activities 11 Which discussions were you involved in? 12 How were di<sup>f</sup>erent opinions solved? 13 Technical challenges? 14 Challenges related to competence? 15 How do you assess the overall results of the project? 16 If you were involved in the IT sub-project, please describe your role and activities 17 Which discussions were you involved in? 18 How were di<sup>f</sup>erent opinions solved? 19 Technical challenges? 20 Challenges related to competence? 21 How do you assess the overall results of the project?
