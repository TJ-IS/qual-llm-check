---
otero_id: 11484
otero_key: "J63XPNT5"
title: "<i>Essence</i>: facilitating software innovation"
authors: "Ivan Aaen"
year: "2008"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2008.43"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Essence: facilitating software innovation

Ivan Aaen<sup>1</sup>

<sup>1</sup>Department of Computer Science, Aalborg University, Aalborg East, Denmark

Correspondence: Ivan Aaen, Department of Computer Science, Aalborg University, Selma Lagerlo¨fs Vej 300, 5.2.14, Aalborg East 9220, Denmark.

Tel: þ 45 9940 8911;

E-mails: ivan@cs.aau.dk, aaen@acm.org

## Abstract

This paper suggests ways to facilitate creativity and innovation in software development. The paper applies four perspectives – Product, Project, Process, and People – to identify an outlook for software innovation. The paper then describes a new facility – Software Innovation Research Lab (SIRL) – and a new method concept for software innovation – Essence – based on views, modes, and team roles. Finally, the paper reports from an early experiment using SIRL and Essence and identifies further research. European Journal of Information Systems (2008) 17, 543–553. doi:10.1057/ejis.2008.43

Keywords: software innovation

## Introduction

Current software development technologies open new opportunities for software innovation by allowing for changes and adaptations even late in development projects. This paper explores these opportunities and suggests a broad approach to building a setting for the creative software team. This setting consists of an infrastructure and a method concept for using this infrastructure. The infrastructure is a new facility – Software Innovation Research Lab (SIRL) – and the method concept developed for this is called Essence. Together these two aim to facilitate software innovation.

According to Fichman, research on IT innovation has become increasingly popular for two reasons: (1) the introduction of IT into almost every aspect of organizational life, and (2) the growing importance of innovation for organizational competitiveness (Fichman, 2004). Software innovation thus is important for companies operating in the global economy. Much research addresses IT-based innovation from a business perspective as evidenced, for example, by the fierce debate on whether IT matters or not, started in 2003 by Nicholas Carr in Harvard Business Review (Carr, 2003). On the other hand, research on software innovation from a developer’s perspective and research on the facilitation of innovative software development seems still in its infancy.

A study by Lee and Xia suggests that systems development teams are inefficient and reactive in dealing with business changes and therefore have problems supporting business adaptations to shifting demands (Lee & Xia, 2005). This is a major problem for the software developing organizations as well as for their customers.

Agile development may offer some promise to remedy this problem. Highsmith and Cockburn argue that agile software development may help developers quickly deliver innovative, high-quality solutions to an increasingly demanding market changing at a dramatically increasing pace (Highsmith & Cockburn, 2001). How this potential may be realized is not described in any detail.

The research described here targets software innovation as a class of problems including innovative software products, innovation management, processes for software innovation, and paradigmatic changes among developers and customers in relation to development and use of software-based solutions. Our aim is to contribute to a deeper understanding of how to facilitate software innovation akin to the aspiration of Walls et al. (1992).

Software innovation is a complex topic and to make it more manageable, the paper applies four views from software engineering – Product, Project, Process, and People – to allow for separation of concerns (Bernstein & Yuhas, 2005; Pressman, 2005). These views are used as a way to flesh out important aspects of software innovation while maintaining an overview.

## Research approach

The purpose of SIRL and Essence is to facilitate innovation in software development via a set of prospective solutions to be evaluated in varying combinations. Paraphrasing Simon (1981), we are designing artifacts with properties intended to attain goals. Our design effort therefore is concerned with how things ought to be in order to facilitate innovation in software development. To Simon the artifacts we design are centered on the interface between inner and outer environments and the design is concerned with attaining goals by adapting the former to the latter (Simon, 1981, p. 132). The inner environment represents a set of alternatives of action – here in the form of Command Variables (CVs) – that we may apply as means to attain our goals given the circumstances – the outer environment – we operate under while developing software.

The outer environment contains a set of parameters characterizing, for example, the application area for the customer(s), market conditions, and technological constraints. To Simon, the outer environment may take the form of fixed parameters that the design simply must conform to. For software projects, the outer environment may often be more like a negotiated order – a set of constraints that all stakeholders agree must be honored by a viable project thereby serving almost as ‘natural laws’ for the project. Examples of such parameters could be time to market, development costs, fixed product requirements, process requirements, technological platforms, etc.

The inner environment constrains the development team regarding what must be achieved in terms of, for example, serving needs of the users, development costs, and flexibility during development with respect to requirements, solutions, prioritization, etc.

Our design problem therefore is to find combinations of CVs to optimize the facilitation of software innovation given the constraints for a team working on a development project.

As we are developing an experimental design of two Design Research et al., 2004; Vaishnavi & Kuechler, 2004) will be a suitable research framework. Design research projects proceed through a series of process steps ordered sequentially with feedback loops between the steps. This paper will to a varying degree cover the first four steps in design research. The first is Awareness of Problem. This step results in a proposal for a research effort inspired, for example, by new developments in industry or new findings within a research field. The second step is Suggestion following immediately after the research proposal. This step results in a tentative design and is essentially a creative step building a vision of new functionality or novel configurations of existing or new elements. The third step is Development targeting implementation of the tentative design. This step precedes the fourth step – Evaluation – where the artifact is evaluated.

The remainder of this paper is organized after these four design research steps. First, prospects for a new outlook for software innovation are proposed by contrasting traditional and agile software development. Then the tentative design of SIRL and Essence is suggested and related to other research contributions. The tentative design is then developed into an initial configuration of SIRL and basic principles in Essence. Finally, the paper reports from an early experiment on the use of physical space in SIRL and logical views in Essence exploring and evaluating the utility of two principles in the overall design.

## Awareness: a new outlook for software innovation

The last decade has manifested a clash between traditional heavyweight and modern lightweight approaches to software development. This clash is very visible in the debates over software process improvement (SPI) and agile development. Core to these debates are distinctions such as between predictable manufacturing and new product development (Larman, 2004). Such distinctions reflect recent developments in software technologies that appear to affect software innovativeness. This section will point to some of these developments in order to identify ways to improve software innovation.

A brief look at the Software Engineering Body of Knowledge (Abran & Moore, 2004) or the Capability Maturity Model Integration (CMMI Product Team, 2002) shows that the traditional software development paradigm aims for predictable and documented software production. Agile development – according to the values and principles expressed in the manifesto (Beck et al., 2001) – aims for software development. The traditional line of thinking sets one scene for software innovation, while agile thinking sets a quite different one. This section provides a first overview over possible changes in working with innovation in software teams. We discuss these changes for each of the four views and propose a command variable for facilitating innovation for the view together with strategies related to each command variable.

## Product

Improved methods, tools, and techniques for software development allows for greater flexibility in the development of software products. One of the four values in the Agile Manifesto (Beck et al., 2001) – Working software over comprehensive documentation – marks major differences between the two paradigms for software development. These differences are about requirements, design, and testing.

Traditional software development focuses on requirements elicitation, on up-front design in order to get the architecture right from the start, and on verification and validation to ensure, that deliverables are consistent and comply with requirements (Abran & Moore, 2004). Agile development focuses on customer involvement via the whole team (Beck & Andres, 2005), emergent design (Fowler, 2003), test-infected development (Beck & Gamma, 2000) and sees testing as confirming that user and customer needs are met.

Product innovation is about developing new or changed products and services (Tidd et al., 2005). Both traditional and agile development set conditions for product innovation. Traditional development tends to subjugate innovative ideas to the requirements specification (Maiden & Gizikis, 2001; Maiden & Robertson, 2005; Maiden et al., 2006). In practice, this often leads to an early and small window of opportunity for innovative ideas, as path dependencies – costs related to rework – effectively impede later changes (Beck & Andres, 2005). Moreover, these ideas will normally come mainly from the customer. Agile development reduces path dependencies significantly and makes dialogue between customers, users, and developers easier.

Both rely on customers as a main source of innovative ideas. Neither stresses the potential in combining application area expertise with the technological expertise held by developers. Moreover, both approaches are generally reticent on innovation.

An attempt to improve software product innovation might therefore seek to enhance the window of opportunity for innovative ideas aiming for a larger timeframe and for opportunities for combining different points of views.

CV1: A command variable to facilitate software product innovation could extend the window of opportunity for product innovation by combining two strategies: (1) allowing for flexible and emergent design (design strategy), and (2) combining the expertise of the team members for strengthening their combined innovativeness (combination strategy).

## Project

Software project management is more and more about change management and flexible planning. The agile manifesto values responding to change over following a plan and thereby emphasizes the project-view on software development.

Traditional project management focuses on cost and schedule, and includes requirements management, predictive planning, resource allocation, risk planning, quality planning, and plan management (Abran & Moore, 2004). Collecting comprehensive information up-front is key. Agile development focuses on adaptive planning with built-in feedback loops (Cohn, 2006), and is based on incremental development with frequent releases (Larman, 2004).

Project innovation here refers to changes in the context, where products or services are produced – what Tidd et al. labels as position innovation (Tidd et al., 2005) – or to the way a software project is managed to achieve innovative solutions. Project innovation is both about stimulating creativity and innovation throughout the project, and about identifying options in previous projects that may offer breakthroughs to a new project.

Requirements management, detailed predictive planning, and plan oversight are essential to traditional project management (Abran & Moore, 2004). Such principles will likely curb project innovation by limiting efforts to use results and experiences from past projects to the beginning of a new project for the sake of scheduling and requirements management. Agile development encourages a gradual formation of solutions combined with adjustments based on previous experience (Larman, 2004). These principles contribute to build an environment for innovative work via cooperation in the whole team.

There seems to be little advice on how to sustain creative and innovative work throughout a software development project. In agile development, the window of opportunity for introducing new ideas widens to cover a larger part of the entire project. This wider window necessitates that managerial ways be found to balance progress and achievement on the one side and creativity on the other.

Improving software project innovation might therefore be about project management.

CV2: A command variable to facilitate software project innovation could target innovation management via two strategies: (1) assisting in learning from previous project experiences (experience strategy), and (2) help balance progress and achievement with creativity and innovation in software projects (balance strategy).

## Process

The discussions over heavyweight vs lightweight software processes relate to perceptions of competence, management, collaboration, and more. By valuing individuals and interactions over processes and tools, the agile manifesto highlights the gap between a traditional emphasis on standardized software processes and an agile emphasis on practice, competence, motivation, and reflection (Aaen, 2003). Building stable software processes stands at the center of the traditional paradigm. The best-known strategy for this is software process improvement (Abran & Moore, 2004). In agile development, processes are not products – objects – by themselves, but rather practices that evolve dynamically with the team as it adapts to the particular circumstances.

Process innovation is about developing new or improved ways to produce products or provide services (Tidd et al., 2005). To separate product and process innovation, process innovation here only denotes changes in software development. Traditional SPI no doubt is the best-known example of process innovation in software engineering. SPI efforts develop process changes to be rolled-out in the organization via descriptions, best practices, and templates to support the process (McFeeley, 1996). Agile process innovation strategies are very different. Here processes are cultivated in the team while developing software. Examples of central mechanisms for developing and disseminating good agile development practices are sitting together, pair programming, shared code, and continuous integration (Beck & Andres, 2005). See Lyytinen and Rose for an in-depth study of how software organizations assimilate new technologies under varying organizational competencies, shifting managerial focus, and competitive demands (Lyytinen & Rose, 2006).

Neither traditional nor agile development methods explicitly aid innovative work via methods, techniques, or tools. Innovation and creativity are treated as exogenous to software development – as something to be taken care of by external disciplines. Moreover, agile approaches are generally silent on how to make process innovations from past projects available to future projects.

An effort to strengthen software process innovation might offer a range of process support alternatives to the team.

CV3: A command variable to facilitate software process innovation might build on two strategies: (1) offering tools and techniques for supporting creativity in software development (creativity strategy), and (2) providing tools and techniques for team learning (learning strategy).

## People

The people view is about the stakeholders in software projects. Examples of stakeholders are senior managers, project managers, developers, customers, super-users, end users, and marketing people. These stakeholders play an important role in traditional as well as agile approaches but agile approaches tend to involve customers directly into the project via the whole development team, i.e. developers and customer representatives. The main concerns here are personal and collective development, learning, communication, and cooperation.

The agile manifesto values customer collaboration over contract negotiation. Specifically, this value concerns the relationship between developers and customers. Traditional development views people essentially as functions (CMMI Product Team, 2002). Standardization and division of work are ideal for minimizing communications costs (Pfleeger & Atlee, 2006), for getting new staff up to speed quickly and for exchanging staff between projects when needed. Agile development puts more emphasis on self-organization, socialization, and tacit knowledge. Whereas interpersonal communication in the traditional line-staff organization is considered a cost that should be minimized (Pfleeger & Atlee, 2006), agile teams employ communication as the primary way to exchange information and negotiate options.

People innovation is about changing the ‘mental models which frame what an organization does, for example, changes in the perception of self, of the development team, of the users, or of the market, corresponding to what Tidd et al. calls paradigm innovation (Tidd et al., 2005). Changes in mental models may help remove blocks or develop new perspectives opening for novel possibilities and solutions.

Little in traditional software development supports people innovation. SPI involves organizational change but not likely paradigmatic change. Likewise requirements elicitation generally develops a conventional understanding of a user organization. Agile software development is not elaborate on people innovation either, but the manifesto value mentioned above points to one significant attribute of agile development that could lead to changed perspectives: The frequent melding of developer and customer views via customer collaboration and formation of whole teams. Likewise self-organizing teams may add to the readiness for change.

Neither traditional nor agile software development offers much to develop new mental models of the development organization or of application areas and markets.

An attempt to facilitate people innovation might therefore focus on how to support exchanging perspectives among stakeholders.

CV4: A command variable to facilitate people innovation might include two strategies: (1) sharing views, for example, via visualization of use scenarios and prototype demonstrations (sharing strategy); and (2) extensive communication support for off-site stakeholders (communication strategy).

## Research proposal

The new outlook on software innovation points to a major research challenge: How can a software team be supported in innovation via infrastructure and methods? This challenge could involve a number of sub-questions targeting the four CVs identified above:

CV1 – Extending the window of opportunity. Will more flexibility in the design process lead to more innovation or more uncertainty about goals? Can combining the expertise of members of the whole team lead to strengthened innovativeness? (Product view)

CV2 – Innovation management. Are there ways to innovate via learning from previous projects? Can management principles be devised to help balance progress and achievement with creativity and innovation? (Project view)

CV3 – Innovation process support. How can relevant process support for creativity in software development be provided? How can team learning be supported with few overheads for the team? (Process view)

CV4 – Mental model change. Can the contrasting of customer and developer views spark off changed mental models of the developing organization or of application areas and markets? Can extensive communication support help integrate off-site stakeholders in the innovation process? (People view)

Thus, the research proposal here would be to devise suggestions for each of these command variables and investigate how they may combine to increase software innovation. In Simon’s terms, the increase in software innovation is the utility function we seek to optimize via SIRL and Essence.

## Suggestion: tentative design of SIRL and Essence

The following two sections present SIRL and Essence and outline how they support the four views of software innovation identified above. This section will sketch the tentative design behind the two.

SIRL and Essence were conceived simultaneously. The ideas appeared as a whole and were not gradually selected and merged into a complete design based on literature studies and other sources. Obviously, a number of ideas and considerations served as inspirations and were synthesized into this setup. The synthesis is based on a fundamentally egalitarian belief for software teams that creativity is a skill that can be learned by anybody and that creativity is an everyday activity (Bono, 1977).

The main strategy for innovation support in SIRL and Essence together is to combine a physical workspace with logical views for a whole team where the members have distinct roles in the development process. Roles, views, and space thus should serve as a platform for developing challenging ideas and implementing these in software solutions.

Basically there are four leading ideas in the design of SIRL and Essence:

\- Exploiting physical space for creative teams

\- Using logical perspectives to support part-whole views

\- Encouraging the exploitation of distinct roles in the whole team

\- Supporting evolutionary and experimental software development.

The physical space refers to the location where software development takes place and/or to the displays used by the developing team. Among the inspirations for using physical space were body thinking – the idea that thinking occurs through sensations and awareness of the body (Root-Bernstein & Root-Bernstein, 2000). Related to this line of thinking is the idea of haptic modeling offering visual and tactile feedback during design (Cheshire et al., 2001). As software projects are collective undertakings, the idea of multiple display environments (MDEs) (Johanson et al., 2002; Biehl et al., 2008) seemed obvious to support discussions, comparisons, reflections, and share information. Finally, the use of physical space is inspired by the observation that agile teams cooperate in varying constellations during a project, working sometimes individually and at others times in pairs or together in the entire team (Beck & Andres, 2005).

Logical perspectives are meant to make it easier to deal with detail and overview in complex matters. Principles like divide and conquer and separation of concerns are traditional design strategies to help manage the complexity of software systems. The initial inspiration to use logical perspectives in SIRL and Essence came from three directions: (1) the more than 2000-year-old philosophical tradition of portraying all worldly structures as made from four elements thereby offering a generic totality consisting of mutually exclusive elements, (2) the four perspectives on software engineering (Bernstein & Yuhas, 2005; Pressman, 2005), and (3) Tidd et al.’s (2005) distinction between four categories of innovations.

The desktop metaphor in the Xerox Star system of 1981 served as another source of inspiration for both the use of physical space and the use of logical perspectives in SIRL and Essence. The Desktop Metaphor introduced a userinterface using physical localization and logical categorization of office documents as the organizing principle. While the Xerox Star was intended for individual users, these ideas are here elevated to the team level using physical placement and categorization to provide overview and easy access to details.

Employing distinct roles aims to benefit from having different personal perspectives and expertise available in the whole team (Tiwana & McLean, 2005). Agile teams combine at least three types of expertise and responsibilities: development, management, and business or application area knowledge. Every team member including the customer is assigned a continual role according to expertise. Assigning these roles aims to strengthen the diversity between team members and support improvisations and creative sessions via mechanisms similar to those found in Theatresport, improvisational theater (Swartjes & Vromen, 2007; Mahaux & Maiden, 2008), and role play (Yardley-Matwiejczuk, 1997; Maiden et al., 2004) This is expected to increase the likelihood of flow occurring in the team during creative sessions. Flow is the mental state in which team members are fully immersed in what they are doing (Csikszentmihalyi, 1997). Likewise, the use of explicit roles is intended to support movement in the team – lateral thinking moving forward to something new as perspectives and values are contrasted and merged (Bono, 1990).

Supporting evolutionary and experimental development is obviously tightly linked to agile development principles (Beck et al., 2001). Incremental development offers possibilities for reducing uncertainties via experimentation (Boehm, 1988). Using interactive screens is expected to intensify the experiments by making the code itself more tangible and by enabling user interactions and simulations under realistic conditions via haptic feedback as suggested above. This idea thus aims to support the design as a social creative process (Warr & O’Neill, 2005; Adamides & Karacapilidis, 2006).

The next two sections develop this tentative design into an infrastructure (SIRL) and a method concept (Essence).

## Development: SIRL – Software Innovation Research Lab

SIRL (Figure 1) was established in August 2006 at the Department of Computer Science at Aalborg University to facilitate research on software creativity and innovation. The lab is intended for all phases in a development project and enables working as individuals, as pairs, and as a team via flexible arrangements of furniture and equipment.

The lab is an MDE supporting diverse perspectives via four interactive boards. Together these boards represent four generic views: Earth, Water, Fire, and Air. The views were named following Empedocles of Acragas (ca. 495–435 BCE), who in his Tetrasomia, or Doctrine of the Four Elements, argued that all matter is composed of these four elements.

A great many modern systems of perspectives also come in fours. Examples are SWOT (Strengths, Weaknesses, Opportunities, Threats), McCarthy’s 4P within marketing (Product, Pricing, Placement, Promotion), Gupta’s 4P within Six Sigma process management (Prepare, Perform, Perfect, Progress), Liker’s 4P within management (Philosophy, Process, People, Problem solving), Tidd, Bessant & Pavitt’s 4P within innovation (Product, Position, Process, Paradigm), and finally the 4P within software engineering (Product, Project, Process, People) used in Essence. The four generic views of SIRL therefore accommodate many and quite different systems of perspectives of relevance to creative and innovative software development.

When a system of perspectives has been chosen, artifacts and information relevant to a project are categorized and allocated to the interactive screen assigned to a given perspective. The screens are mounted some distance apart to allow for team members to address the screens and thus the information categories and artifacts individually. The interactive screens are also well suited for discussions, demonstrations, and simulations including visualized use scenarios thereby supporting evolutionary and experimental development. Each team member role may be assigned principal responsibility for one screen thereby using physical location to emphasize duties and tasks. This way the floor and particularly the walls are used to actively support creative body thinking.

SIRL is equipped with four interactive screens (Smart Board 660) with projectors, four desktop computers, and one server. Communication software such as Skype and instant messaging clients with cameras and loudspeakers are available for off-site communication. The main software is Visual Studiot IDE for software development and Smart Ideast for idea generation.

![](/api/attachments/J63XPNT5/fulltext/images/b8d2c227e0fda0f258f9d10c196cf9b9a2280e186428c541c2eca13491736bd5.jpg)  
Figure 1 SIRL layout fall 2007.

The laboratory thus provides infrastructural support for the command variables in numerous ways. CV1 (extending the window of opportunity) is supported via the physical space to be allocated to defined perspectives and the equipment for development activities for the team and its members. CV2 (innovation management) is supported by the multiple displays allowing ample screen space for working both with status and plans, and with ideas and alternatives. CV3 (innovation process support) is directly supported via idea generation software and available displays for learning activities without disrupting ongoing development activities. CV4 (mental model change) is supported via the logical perspectives and the displays to be used for visualizations, demonstrations, and communications, for example, with user representatives.

## Development: Essence – innovation in the agile team

Essence is a method concept currently under development in SIRL. The concept is named after Quintessence, the cosmic fifth element added by Aristotle to complement Empedocles’ four earthly elements.

The intention is to extend existing agile methods rather than developing a new method. Essence will therefore meld creative sessions into agile development to employ development speed and flexibility throughout the project. Essence should be lightweight, easy, and fun to use. Lightweight as ceremony and project overheads must be kept at a minimum so as not to have projects drop Essence for lack of time. Easy to use as the time needed before Essence is useful should be short and the activities in Essence should come natural to the participants. Finally, Essence should be fun to use to further motivation and outcome.

The strategy for this is to base activities on principles similar to role – playing games and improvisational theater. Both of these are based on defined characters, settings, and situations, whereas the events and actions are largely left to the participants themselves to develop via disciplined improvisations. To ensure a familiar basis for these improvisations, the characters and settings are based on permanent structures (roles and views, respectively), whereas situations reflect a current status or challenge.

Team members have roles defining their characters. Each role has a set of ideals or values providing a clear raison d’eˆtre (Swartjes & Vromen, 2007) to the role. The Challenger is the customer and has all the responsibilities of an on-site customer, yet should pose project requirements in the more open form of challenges. The Responder is the developer employing technical competence to deliver ambitious responses. These two roles engage in a dialogue where solutions are developed by contrasting application area needs and desires with technical opportunity. The Anchor serves to keep the team absorbed and focused on delivering exciting solutions. The last role is the Child; this role is temporary as anyone on the team can take this role temporarily at any given time. The Child may raise any idea or issue – even when contrary to decisions made earlier by the team. This role is named after the child in Hans Christian Andersen’s The Emperor’s New Clothes who said: But he hasn’t got anything on and thereby revealed the emperor’s folly.

The setting is part of framing the story world – the shared view that forms the basis for expressing each character’s ideals (Swartjes & Vromen, 2007). To define the setting, Essence maps the 4Ps from software engineering onto SIRL’s four generic views.

The situation introduces the dynamic element to complete the story world: the point of departure for the game. The first part of this comes in the form of Essence Games. Essence Games are inspired by Hohmann’s Innovation Games (Hohmann, 2006) and numerous methods described in Huczynski (2001). Essence Games are based on the principle of saying yes – accepting all offers that other characters bring into the situation (Swartjes & Vromen, 2007). Until now two Essence Games have been outlined and tried. The other part is the project state. Projects are in one of three states defining the situation to be addressed – Idea, Plan, or Growth. Idea is the mode for suggesting possible courses of action and for developing concepts. Games in this mode are mainly exploratory. Plan is where proposals for doing or achieving goals are developed and necessary preparations are identified. This mode leads to decisions about what to do, when, and by whom. Games in this mode focus mainly on inventory building to identify tasks. Growth is where ideas find actual form via evolution, experimentation, selection, maturation, expansion, enlargement, and progress. Games in this mode are mainly confirmatory and investigate if the project maintains a focus on innovation.

To ensure continuity from Essence game to project activities and also minimize game preparations, Essence elements – views, roles, and modes – should also be used in the overall project. If not, game sessions may just be parentheses without any real impact on the project. The following will outline how such continuity might be pursued and how the views may address the strategies mentioned for each command variable.

## Product

Interactions between stakeholders from the application and development areas may serve as means for exchanging perspectives and developing challenging ideas possibly leading to innovative results (CV4 – sharing strategy). Methodologically, Essence stimulates dialogue between Challenger and Responder in order to develop ambitious technical responses and answer application area challenges (CV1 – combination strategy). Visually, the Product view lets the responders represent the product being built – the source code and system architecture – to make the product and propositions for changes to it more tangible in team discussions (CV1 – design strategy).

## Project

Project-wise software innovation faces at least two challenges: how to manage innovative projects, and how to get inspiration from past projects when addressing new problems. The challenge grows as the window of opportunity for innovation widens. This requires project status and progress to be balanced against visions.

A comprehensive response to these challenges has yet to be developed for Essence. One main strategy may be to use metaphors (Couger et al., 1993; West & Solano, 2005) as instruments for transferring knowledge and inspiration from one area to another. Methodologically, Essence will therefore propose a repository of metaphors derived from past projects and products (CV2 – experience strategy). Visually, the Project view supports the Challenger in maintaining project status and planning throughout the project by giving an overview of status and backlog for the sprint and for the project (CV2 – balance strategy).

## Process

The Process view supports innovative and creative work by offering an assortment of ways to develop and explore concepts and ideas, to elicit tasks and requirements, and to investigate and confirm if the project upholds an appropriate level of innovation. Methodologically, Essence will therefore contain a repertoire of creative methods, tools, and techniques such as patterns (Gamma, 1995; Rising, 1998; Coplien & Harrison, 2005) and Innovation Games (Hohmann, 2006) adapted to Essence with respect to roles, views, and modes (CV3 – creativity strategy). Patterns and pattern languages may also be used to preserve experiences gained in the team (CV3 – learning strategy). Visually, the Process view provides the Anchor with an overview of. and access to.

this repertoire throughout the project. The Process view also contains tools for brainstorming, innovation, and creativity such as ThoughtOfficet and Smart Ideas<sup>s</sup> and other creativity support tools (Shneiderman, 2007) (CV3 – creativity strategy).

## People

The People view facilitates the development of new mental models of the development organization or of application areas and markets. Methodologically, the Child role in Essence empowers at any time any member of the team to irresponsibly question basic assumptions, values, or the like in the project for a while (CV4 – sharing strategy). Interventions from external consultants might also find place here (CV4 – sharing strategy). Visually, the People view demonstrates uses of the software under development, application examples, and scenario visualizations (CV4 – sharing strategy). Throughout the project this view visualizes use scenarios, for example, via video footage from the user organization, video link to actual users, etc. This view also serves as main access point to off-site stakeholders using video chat, Skype, or similar (CV4 – communication strategy).

## Evaluation: early experiments with Essence and SIRL

Both SIRL and Essence introduce concepts, structures, and ways of working that have not been combined before. They are still early in their development, and experiments at this stage therefore form part of a search for CV uses that contribute to improve software innovation. In other words, current experiments serve to provide insights and knowledge about the utility of the CVs and produce ideas for how to apply them. The early experiments help in understanding the leading ideas in SIRL and Essence by generating information that can only be gained from practical use in software development projects.

Our strategy is to develop and test SIRL and Essence incrementally by using both for software development by student teams. This section will report on experiences from a term project with four full-time software engineering thesis students in the fall of 2007. The present analysis of the experiment addresses two of the four leading ideas for SIRL and Essence:

\- Is it useful to physically distribute views in SIRL on separate screens?

\- Is it useful to logically split up views in a priori defined categories?

As a student project we can describe the outer environment of the experiment as given by a fixed duration of 4 months using an agile development process. The students agreed on an inner environment where one of them served as customer, where the agile method used was Scrum (Schwaber & Beedle, 2002), and where product testing was lax giving priority to develop more software.

## Table 1 Role questions

## Sprint number

What was your role in this sprint (Challenger/Responder/Anchor)? Could you use the four views for your role?

Which views were most important for your role? Why? How did you use them?

Was the physical separation of views of importance for overview and coordination seen from your perspective?

Was the physical separation of views of importance for working with details in the project seen from your perspective?

Based on Scrum, the students developed a plug-in for Visual Studio to support pair programming between developers in different locations. In 4 months, the students completed four Scrum sprints. For each sprint two students would be Responders, one would be Challenger, and one Anchor. The Child role was not used during this experiment. The students rotated Essence roles to ensure that everybody served as Challenger, Responder, and Anchor. For every sprint the students responded to a questionnaire with 16 qualitative questions on their experiences using screens and views relative to their particular role in the sprint. Six of these questions are used in the present analysis (Table 1). The responses were coded using a 48-node coding tree with TAMS Analyzer, version 3.41.

The responses reflect variations with respect to student personality, sprint number, and role. The following two subsections will address the two questions. For simplicity, roles in the first two sprints will be referred to as early Challenger, Responder, etc., and roles in the two last sprints will be labeled as late.

## Experiences with physical space

Early Challengers found the physical distribution helpful for planning and oversight by showing the project and sprint backlogs and the running product simultaneously. One early Challenger observed: I think the screens were great for splitting up thoughts and discussing issues. The screens help keep ideas alive. The screens help establish overview. Every discussion was persistent in a way, and because of the physical split they were also more focused. Late Challengers reported briefly on their experiences, as they played a limited role in the last sprints.

Early Responders saw themselves as developers and did not engage much in dialogue with the Challenger, leaving this dialogue to the Anchor. For that reason, early Responders focused mainly on their own Product screen. The physical distribution was useful for overviews and for allocating tasks. Late Responders also focused on detailed development. This reflects the limited size of the software, making it fairly easy to maintain an overview of the entire product. Larger projects with more people and more refactoring would likely make more screens useful for Responders.

The group used the Anchor role like a Scrum Master with a stronger managerial role than expected in regular uses of Essence. Early Anchors found separate screens useful to split up and discuss issues, focus on ideas, and maintain overview. Late Anchors pointed more to specific episodes where multiple screens helped maintain overview while addressing details. Thus, this early experiment suggests that splitting up physically on interactive screens has potential, but also – not surprisingly – that the use of screens changes as the team gains experience.

All three roles point to overview as a benefit from using the screens, and Challengers and Anchors point to idea development as another benefit. These observations indicate positive experiences with CV1 (combination strategy). Responders and Anchors point to the utility of the screens for handling whole-part problems related to detailed design, which may indicate positive experiences with CV2 (design strategy). Finally, Anchors and Responders point to support for task allocation as benefits, which suggest positive experiences with CV2 (balance strategy).

## Experiences with logical views

Early Challenger experiences with logical views are on a par with those of physical space. One Challenger observed: Having the ability to see the two backlogs and the running product at the same time helped to understand how each requirement had been seen by the team and how it had been implemented. The other early Challenger observed that the roles help distribute responsibilities. The People and Project views were deemed most important for communication and discussion. Late Challengers also primarily used the People and Project views to show and prioritize backlog items.

Early Responders used the People and Project views to overview tasks and assignments. The Process and Product views were not sufficiently developed to be fully useful. As one of them observed: There were unused possibilities in Essence – we should have used more views. Another late Responder observed that the roles help distribute responsibilities: This way I have specific responsibilities and can concentrate on them [but] the four views were not easy to use directly.

The first Anchor saw little use of the views specifically for his role. The second Anchor used the People and Project views in meetings to keep track. The third Anchor used all views episodically and two of them (Product and Project) the rest of the time, while the fourth primarily used the Project view for status.

All three roles pointed to planning, task allocation, or distribution of responsibilities as benefits from using the views. This suggests positive experiences with CV2 (balance strategy). Challengers also pointed to communication and discussions as benefits, which may indicate some benefits related to CV4 (communication and sharing strategies).

Consistent for all sprints was that the views were not fully used as intended. The primary use of the views was for project overview and coordination – that is for project management – whereas the expected main benefit of them – for creative dialogue under development – was not obtained. Further benefits from using these logical views may not be obtained without a stronger methodological foundation. In particular, this seems to be true for CV1, CV3, and CV4.

## Discussion and conclusion

This paper has presented SIRL, a facility for experimenting with software innovation, and Essence, a method concept drafted for use in SIRL. The development of SIRL and Essence is based on expectations that today’s software development technology offers a new outlook for software innovation. To query into this outlook, a tentative design of SIRL and Essence was drafted based on four leading ideas, and SIRL and Essence were outlined to implement these ideas. The research itself is an iterative process of highly interdependent steps, making it hard to separate suggestion, development, and evaluation. The research is based on a pre-theory framework that eventually may contribute to guide future research activities (Adam & Fitzgerald, 2000).

The first experiments gave some insights into CV1 (extending the window of opportunity) and CV2 (innovation management). CV3 (innovation process support) was not developed to a degree to allow for experimentation, and CV4 (mental model change) was only marginally covered.

The experiences from using CV1 and CV2 are promising and both CVs seem ready for further research aiming to develop and test their strategies under realistic conditions and based on an elaborated methodological framework.

CV3 and CV4 have yet to undergo their first exploratory experiments. Providing support for CV3 and CV4 should be relatively straightforward but has yet to be implemented. Experiments aiming at both are under preparation.

Experiments in the future research targets three steps:

1. Validation of the leading ideas of the tentative design in order to consolidate theses ideas with respect to the command variables. This paper reported on an early experiment targeting two out of four leading ideas. These two leading ideas in the design of SIRL and Essence seem to offer promise: there seem to be benefits in physical and logical distribution for project discussion and coordination, but the potential for creative development has yet to be fully demonstrated. Evaluation of the remaining two leading ideas – roles and evolution – may give insights into this creative potential. This constitutes one line of future research.

2. A second line of research targets the development of the static structure of roles and modes defining characters, and settings – in particular the design and utility of roles, modes, and tools. Research in this step will likely take place in combination with the research on the two remaining leading ideas and the evaluation will be based on all four command variables.

3. A third line of research targets the dynamic situations consisting of events and actions developed by the participants themselves via disciplined improvisations. How to build Essence games and how to integrate Essence into software development methods constitutes a major research challenge. A number of games intended for Scrum are currently under development. These games will address one or more command variables and will be tested against them.

## About the author

Ivan Aaen is Associate Professor of Computer Science at Aalborg University, Denmark. His interests include software innovation, agile software engineering and informa-

## Acknowledgements

Thanks go to Peter Axel Nielsen, Jens Henrik Hosbond, and Jeremy Rose from Institute for Computer Science at Aalborg University for inspiring discussions. Richard Baskerville has generously offered numerous comments and suggestions for improving the paper. The usual caveats for the remaining errors apply. My students at SIRL, Morten Andersen, Søren Rode Andreasen, Lasse Bæk, and Philip Bredahl Thomsen (2006–07) and Jeppe V. Boelsmand, Rasmus Jensen, Jan Leckscheidt, and Morten Saxov (2007–08) have been indispensable for building SIRL and for the experiments. Also thanks to Søren Hansen, founder of the Aalborg University Creativity Lab, for illustrating the potential in Theatresport and improvisational theater. The Department of Computer Science at Aalborg University supported the research.

tion systems. He holds a Ph.D. in computer science from Aalborg University and is a member of the ACM and IEEE Computer Society.

## References

AAEN I (2003) Software process improvement: blueprints versus recipes. IEEE Software 20(5), 86–93.

ABRAN A and MOORE JW (Eds) (2004) Guide to the Software Engineering Body of Knowledge: 2004 Version. SWEBOK IEEE Computer Society, Washington.

ADAM F and FITZGERALD B (2000) The status of the IS field: historical perspective and practical orientation. Information Research 5(4).

ADAMIDES ED and KARACAPILIDIS N (2006) Information technology support for the knowledge and social processes of innovation management. Technovation 26(1), 50–59.

BECK K and ANDRES C (2005) Extreme Programming Explained: Embrace Change. Addison-Wesley, Boston, MA.

BECK K and GAMMA E (2000) Test-infected: programmers love writing tests. In More Java gems (DEUGO D, Ed.), pp 357–376, Cambridge University Press, New York, NY, USA.

BECK K et al. (2001) Manifesto for Agile Software Development. www.agilemanifesto.org (visited 14 September 2008).

BERNSTEIN L and YUHAS CM (2005) People, process, product, project – the big four. In Trustworthy Systems Through Quantitative Software Engineering (BERNSTEIN L and YUHAS CM, Eds), pp 39–71, John Wiley & Sons, Inc, New York.

BIEHL J et al. (2008) Impromptu: a new interaction framework for supporting collaboration in multiple display environments and its field evaluation for co-located software development. In CHI ‘08: Proceeding of the Twenty-Sixth Annual SIGCHI Conference on Human Factors in Computing Systems, pp 939–948, ACM, New York, NY.

BOEHM BW (1988) A spiral model of software development and enhancement. Computer 21(5), 61–72.

BONO ED (1977) Lateral Thinking: A Textbook of Creativity. Penguin, Harmondsworth.

BONO ED (1990) Teach Yourself How To Think. Penguin, Harmondsworth. CARR NG (2003) IT doesn’t matter. Harvard Business Review 81(5), 41–49.

CHESHIRE D, EVANS M and DEAN C (2001) Haptic modeling – an alternative industrial design methodology. In Proceedings of EuroHaptics (BABER C, F M, W S and AMW, Eds), University of Birmingham, UK.

CMMI P T (2002) CMMI for Software Engineering, Version 1.1, Continuous Representation (CMMI-SW, V1.1, Continuous). Software Engineering Institute, Pittsburgh, PA.

COHN M (2006) Agile Estimating and Planning. Prentice Hall Professional Technical Reference, Upper Saddle River, NJ.

COPLIEN JO and HARRISON N (2005) Organizational Patterns of Agile Software Development. Pearson Prentice Hall, Upper Saddle River, NJ.

COUGER JD, HIGGINS LF and MCINTYRE SC (1993) (Un)Structured creativity in information systems organizations. MIS Quarterly 17(4), 375–397.

C M (1997) Flow and creativity. NAMTA Journal 22(2), 60–97.

FICHMAN RG (2004) Going beyond the dominant paradigm for information technology innovation research: emerging concepts and methods. Journal of the Association for Information Systems 5(8), 314–355.

FOWLER M (2003) Design – who needs an architect? IEEE Software 20(5), 11–13.

GAMMA E (1995) Design Patterns: Elements of Reusable Object-Oriented Software. Addison-Wesley, Reading, MA.

HEVNER AR et al. (2004) Design science in information systems research. MIS Ouarterly 28. 75–105.

HIGHSMITH J and COCKBURN A (2001) Agile software development: the business of innovation. Computer 34(9), 120–127.

HOHMANN L (2006) Innovation Games: Creating Breakthrough Products Through Collaborative Play. Addison-Wesley Professional, Upper Saddle River, NJ.

HUCZYNSKI A (2001) Encyclopedia of Development Methods. Gower, Aldershot, UK.

JOHANSON B, FOX A and WINOGRAD T (2002) The interactive workspaces project: experiences with ubiquitous computing rooms. IEEE Pervasive Computing 1(2), 67–74.

LARMAN C (2004) Agile and Iterative Development: A Manager’s Guide. Addison-Wesley, Boston, MA.

LEE G and XIA W (2005) The ability of information systems development project teams to respond to business and technology changes: a study of flexibility measures. European Journal of Information Systems 14(1), 75–92.

LYYTINEN K and ROSE GM (2006) Information system development agility as organizational learning. European Journal of Information Systems 15(2), 183–199.

MAHAUX M and MAIDEN N (2008) Theater improvisers know the requirements game. Software, IEEE 25(5), 68–69.

MAIDEN N and GIZIKIS A (2001) Where do requirements come from? IEEE Software 18(5), 10–12.

MAIDEN N and ROBERTSON S (2005) Integrating creativity into requirements processes: experiences with an air traffic management system. In Proceedings of the 2005 13th IEEE International Conference on Requirements Engineering (RE’05) pp 105–114.

MAIDEN N, ROBERTSON S and GIZIKIS A (2004) Provoking creativity: imagine what your requirements could be like. IEEE Software 21(5), 68–75.

MAIDEN N, ROBERTSON S and ROBERTSON J (2006) Creative requirements: invention and its role in requirements engineering. In Proceeding of the 28th International Conference on Software Engineering (ANDERSON K, Ed.), pp 1073–1074, ACM, New York, NY.

MCFEELEY B (1996) IDEAL: A User’s Guide for Software Process Improvement. SEI, Pittsburgh, PA.

PFLEEGER SL and ATLEE J (2006) Software Engineering: Theory and Practice, 3rd edn, Pearson Academic Computing, Upper Saddle River, NJ.

PRESSMAN RS (2005) Software Engineering: A Practitioner’s Approach. McGraw-Hill Higher Education, Boston, MA.

RISING L (1998) The Patterns Handbook: Techniques, Strategies, and Applications. Cambridge University Press SIGS Books, Cambridge, UK.

ROOT-BERNSTEIN RS and ROOT-BERNSTEIN M (2000) Sparks of Genius: The Thirteen Thinking Tools of Creative People. Houghton Mifflin Co., Boston, MA.

SCHWABER K and BEEDLE M (2002) Agile Software Development with Scrum. Prentice Hall, Upper Saddle River, NJ.

SHNEIDERMAN B (2007) Creativity support tools: accelerating discovery and innovation. Communications of the ACM 50(12). 20–32

SIMON HA (1981) The Sciences of the Artificial. MIT Press, Cambridge, MA.

SWARTJES IMT and VROMEN JAF (2007) Emergent story generation: lessons from improvisational theater. In Proceedings of the AAAI Fall Symposium on Intelligent Narrative Technologies (H RC and H A, Eds), FS-07-05, 9–11 November, pp 146–149, AAAI Press, Arlington, VA.

TIDD J, BESSANT JR and PAVITT K (2005) Managing Innovation: Integrating Technological, Market and Organization Change. Wiley, Hoboken.

TIWANA A and MCLEAN ER (2005) Expertise integration and creativity in information systems development. Journal of Management Information Systems 22(1), 13–43.

VAISHNAVI V and KUECHLER W (2004) Design research in information systems. 20 January 2004, last updated 4 August 2007. Available from www.isworld.org/Researchdesign/drisISworld.htm.

WALLS JG, WIDMEYER GR and EL SAWY OA (1992) Building an information system design theory for vigilant EIS. Information Systems Research 3(1), 36–59.

WARR A and O’NEILL E (2005) Understanding design as a social creative process. In C&C’05: Proceedings of the 5th Conference on Creativity & Cognition, (EDMONDS E, CANDY L, BROWN P, HEWETT T and JEFFERIES J, Eds), pp 118–127, ACM, New York, NY.

WEST D and SOLANO M (2005) Metaphors be with you! (Metaphor System). In Proceedings of the Agile Development Conference (MANNS ML and WAKE WC, Eds), pp 3–11, IEEE, Computer Society, LOS Alamitor, CA.

YARDLEY-MATWIEJCZUK KM (1997) Role Play: Theory and Practice. Sage, London.
