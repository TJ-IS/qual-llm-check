---
otero_id: 14288
otero_key: "DGU75TNU"
title: "From Business Process Management to Business Process Ecosystem"
authors: "Richard Vidgen; Xiaofeng Wang"
year: "2006"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000076"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# From business process management to business process ecosystem

Richard Vidgen, Xiaofeng Wang

School of Management, University of Bath, Bath, UK

Correspondence:

Professor R Vidgen, School of Management, University of Bath, Bath BA2 7AY, UK.

Tel: þ 44 1225 383821;

Fax: þ 44 1225 386473;

E-mail: r.t.vidgen@bath.ac.uk

## Abstract

New technologies, notably service-oriented architectures and Web services, are enabling a third wave of business process management (BPM). Supporters claim that BPM is informed by complexity theory and that business processes can evolve and adapt to changing business circumstances. It is suggested by BPM adherents that the business/IT divide will be obliterated through a process-centric approach to systems development. The evolution of BPM and its associated technologies are explored and then coevolutionary theory is used to understand the business/IT relationship. Specifically, Kauffman’s NKC model is applied to a business process ecosystem to bring out the implications of coevolution for the theory and practice of BPM and for the relationship between business and IT. The paper argues that a wider view of the business process ecosystem is needed to take account of the social perspective as well as the human/ non-human dimension.

Journal of Information Technology (2006) 21, 262–271. doi:10.1057/palgrave.jit.2000076 Keywords: business process management; service-oriented architecture; coevolution; complex systems; ecosystem

## Introduction

S <sup>mith</sup> <sup>and</sup> <sup>Fingar</sup> <sup>(2003)</sup> <sup>claim</sup> <sup>that</sup> <sup>organizations</sup> <sup>that</sup>hard-code processes or continue with manual process hard-code processes or continue with manual process steps will lose out to competitors that adopt business process management (BPM) techniques, a view supported by the major IT market intelligence companies – Gartner, Forrester, Ovum and Delphi Group. Organizations carry out BPM to execute, manage, improve and adapt their business operations across the extended enterprise. The implementation of BPM relies in great part on IT (in particular, a service-oriented IT architecture built on Web service technologies) to model business processes and to execute them directly via a business management server. The ability to change a process design and to make it operational quickly makes BPM a key enabler for creating and responding to change, that is, for achieving organizational agility.

Smith and Fingar (2003) call the resurgence of interest in BPM the ‘third wave’. They argue that BPM is both/and (Pettigrew et al., 2003) rather than either/or. For example, BPM is not just about the past and present (process improvement), it is also about the future (process innovation). Smith and Fingar (2003) say that third-wave BPM disrupts the business–IT divide and moves toward a world in which ‘process owners design and deploy their own processes, obliterating, not bridging, the business–IT divide’ (p. 127). But, how is this to be achieved? Smith and Fingar (2003) point explicitly to complex systems theory as an organizing frame for BPM: ‘The study of such distributed multi-participant processes, grid-like systems, emergence, chaos and self-organization are going to set the stage for the theoretical work that will underpin the scientific application of third-wave process management over the coming decade’ (p. 158). However, they provide no further detail concerning how complex systems theory might be applied to BPM and the implications thereof for management.

The best-known centre for complexity research is the Santa Fe Institute, which is a collecting point for distinguished scientists and researchers from different fields who share similar interests in complex phenomena. These researchers believe there are common laws governing complex systems that can cross traditional disciplines. Complexity studies cover a wide range of ideas and theories and it is not possible to do justice to these many and sophisticated ideas in this paper (see Anderson (1999) for an overview of complex systems). Consequently, this paper will focus on a particular aspect of complexity: coevolutionary theory and the development of a business process ecosystem. A coevolutionary perspective is taken to gain insight into the business/IT divide and whether it indeed might be ‘obliterated’ by BPM or whether it will still need to be ‘bridged’ in some fashion. The aim of this paper is, therefore, to analyze the potential contribution of coevolutionary theory to the theory and practice of BPM and to gain further insight into the relationship between business and IT.

The structure of the paper is as follows. In the next section, we trace the history and current state of BPM. In the third section, the research model is described – the business process ecosystem – and Kauffman’s (1993, 1995a) model of coevolution introduced. In the fourth section, coevolutionary theory is applied to business processes and a service-oriented IT architecture, with additional concern for the social context of coevolution. In the fifth section, the implications for practice and research and limitations of the work are discussed. Conclusions are drawn in the final section.

## Business process management (BPM)

## Business process redesign (BPR)

The rationale around which organizations have been built and founded in the last two hundred years is Adam Smith’s idea to break work down into its simplest and most basic tasks, which can be performed by workers with basic skills. A consequence of organizing by function, however, was a loss of flexibility. Many organizations in industrialized countries following the machine metaphor could not cope with changing customer demands and a dynamic and competitive environment. BPR appeared as a remedy and can be dated back to two seminal papers published in the same year: Davenport and Short (1990) and Hammer (1990), which report on the growing wave of process innovation and radical business process change. In this early stage, BPR took on a radical, clean-slate approach, which was typified by the title of Hammer’s 1990 paper: ‘Don’t automate, obliterate’. Hammer and Champy (1993) define business process re-engineering as ‘y the fundamental rethinking and radical redesign of business processes to achieve dramatic improvements in critical, contemporary measures of performance, such as cost, quality, service and speed’ (p. 32). Re-engineering determines what an organization should do, how it should do it and what its concerns should be, as opposed to what they currently are. This radical view is rather different to the incremental changes typical of business process improvement (Harrington, 1991) as represented by TQM (total quality management).

However, the original enthusiasm for BPR has been tempered by reported high failure rates (50–70%) of BPR initiatives (Hammer and Champy, 1993). Although Hammer and Champy argue that this was because companies and managers were not radical enough and failed to comprehend the degree of change required, not only in business processes but also in managerial behaviour and organizational structure, others, including Davenport and Stoddard (1994), began to question the clean-slate basis of BPR and to soften the radical approach to change. In retrospection, Davenport (2002) admits that the very idea of a big, ‘one-time swing’ at process change is less likely to succeed than a continuous process improvement approach. He also considers that information systems (IS) were another aspect of the problem: broad, cross-functional systems were a major departure from the applicationcentric IT architectures most often encountered in organizations. In the early years of BPR, enterprise resource planning (ERP) packages were not mature and so companies either had to develop their own systems or attempt to integrate application packages from different vendors (neither of which are simple tasks).

Grover and Kettinger (1995) acknowledge that while the notion of radical change is intuitively appealing, it has not always met with the degree of success originally claimed by its many proponents. They propose the concept ‘business process change’, a broader and more modest notion than BPR. Grover (1999) argues that the notion of continuous change seemed to be becoming more important than the one-time radical change. In recent years, BPR has seen its second wave (Hammer, 2001; Champy, 2002; Davenport, 2002). Much of the excitement about reengineering’s return is around the redesign of interorganizational processes. It is also why this second wave of re-engineering coined the term ‘X-engineering’ in which ‘X’ stands for cross-organizational business processes (Champy, 2002). In the latter days of BPR, ERP software emerged as the key technology that could support new cross-functional processes. Re-engineering initiatives really turned into ERP implementation projects in many companies. However, new technologies have emerged that go beyond BPR as ERP, including tools such as XML, Web services and e-business process languages. We now consider the role of these new technologies in ‘third-wave’ BPM.

## Business process management

A core aspect of BPM is that process designs are executable and implemented on business management servers allowing processes to be controlled, monitored and even changed in real time. This means that the model is the process and the process is self-documenting. Technology is thus an essential aspect of BPM requiring process management technologies together with an appropriate IT infrastructure. Unsurprisingly, BPM comprises multiple and competing standards and technologies. One of the leading standards organizations is the BPM Initiative (BPMI), a nonprofit organization whose mission is ‘to promote and develop open, complete and royalty free XML-based standards that support and enable BPM in industry’. BPMI (www.bpmi.org) works with other standards bodies such as the Object Management Group (which developed the unified modelling language, UML) and OASIS (a body responsible for e-business standards). The BPMI currently promotes several layers of standards that support process design, the translation of process designs into an executable language and the building of systems to automate intra- and interorganizational business processes.

Coupled with BPM is a service-oriented architecture (SOA), which is defined as (xml.com, 2003):

SOA is an architectural style whose goal is to achieve loose coupling among interacting software agents. A service is a unit of work done by a service provider to achieve desired end results for a service consumer. Both provider and consumer are roles played by software agents on behalf of their owners.

In an SOA the interface contract to the service is platformindependent, the service can be dynamically located and invoked, and the service is self-contained, that is, it maintains its own state. Business processes are implemented by discovering and calling services in appropriate sequences, as specified in a business process model. Industry analysts claim that, ultimately, an SOA approach spells the end of traditional application-centric development. The traditional application, for example, sales order processing, is of too coarse granularity and defined by a boundary that is often all but impermeable to other applications. Organizations will not migrate to a full SOA overnight and will need to expose their legacy applications as a collection of services that can be leveraged as part of an SOA through enterprise application integration technologies.

Web services are a key enabling technology for migration to, and implementation of, an SOA. A Web service is a reusable component that can be published, located and invoked over the Internet using standard protocols (Stal, 2002; the451, 2002). According to George Colony, Founder and Chief Executive of Forrester Research, Web services will be at the core of a new ‘technology thunderstorm’ that will spawn the XInternet, an executable architecture supported by organic IT (Silicon.com, 2003). Through inter-operating IS applications, Web services will enable collaborative commerce applications in areas such as supply chain management and customer relationship management. For example, by exposing its manufacturing systems to its suppliers through Web service interfaces Dell claims to have reduced its stock holding from 26–30 to 3–5 h (Hagel, 2002).

## Coevolution and business process ecosystems

BPM can be thought of as comprising two species: business processes and services (the IT components of an SOA). Ehrlich and Raven (1964) introduce the term coevolution and use it to describe the reciprocal evolution that results from the interactions of unrelated species. They illustrate coevolution by looking at the interactions between the feeding habits of butterfly larvae and the defences of plants and argue that the coevolutionary process has contributed to a wide diversification of both plants and herbivores. Adaptive agents tend to alter their structures or behaviours as responses to interactions with other agents and the environment. These different species coexist in an ecosystem in which adaptation by one type of entity alters the fitness landscape of other types of entity, that is, action is reciprocal. Kauffman (1993, 1995a) uses Sewell Wright’s (1932) idea of a fitness landscape in which agents seek to move to higher ‘fitness peaks’, where survival is more likely. Sometimes actions by other agents will cause an agent to sink to a ‘fitness valley’, where there is a risk of becoming extinct. Thus, all the agents in an ecosystem are striving for fitness and seeking to avoid extinction. The actions of each agent changes the fitness landscapes of the other agents and thus the fitness landscapes are constantly changing and deforming.

In an organizational setting, McKelvey (1999) considers coevolution and competitive behaviour of firms, defining coevolution as ‘mutual causal changes between a firm and competitors, or other elements of its niche, that may have adaptive significance’ (p. 299). McKelvey (1999) stresses that coevolution is a multi-level phenomenon and that it is necessary to ‘take a more emergent natural systems perspective and pick parts naturally emerging as evolutionarily significant (those most likely to change which offer selective advantage for the firm as a whole)’ (p. 298). Mitleton-Kelly (2000) uses coevolutionary theory to study the relationship between the business and IS domains to gain insight into the problems of legacy systems. She takes a multi-level analysis approach to look at the interaction between business individuals and individuals in IT, between business and IS domains, and between the organization and its environment. Peppard and Breu (2003) apply coevolutionary theory to the issue of business/IS strategic alignment.

To develop a model of a business process ecosystem, we take inspiration from Leonard-Barton (1988) and posit that there is mutual adaptation between the user environment, the content of which we define to be business users and business processes, and technology, which we define as IT developers and software components. These four species form the coevolutionary core of the business process ecosystem (Figure 1), in which change by one species will likely lead to reciprocal change by the other species. Primacy is not accorded to any one species and cause and effect will be difficult to unravel as each entity’s actions reverberate through the intricate web of relationships that forms the business process ecosystem (Mitleton-Kelly, 2000). The business process core ecosystem does not have a hard boundary with its environment; rather it will have a close relationship with other systems, entities and stakeholders (such as business units, organizations, standards bodies, regulatory bodies and financial institutions) with which it will coevolve. Thus, Figure 1 makes no hard assumption about the system boundary, contains no linking arrows and flattens out the species to avoid presenting a hierarchy of systems. As Capra (1996) comments:

Since living systems at all levels are networks, we must visualize the web of life as living systems (networks) interacting in network fashion with other systems (networks)y . We tend to arrange these systems, all nesting within larger systems, in a hierarchical scheme by placing the larger systems above the smaller ones in pyramid fashion. But this is a human projection. In nature, there is no ‘above’ nor ‘below’, and there are no hierarchies. There are only networks nesting within other networks (p. 35).

Indeed, the choice of species and distinction between the core species and the peripheral species is a human projection and shaped by the focus of the investigation, in this case a study of BPM, and by the perspective and interests of the investigator.

![](/api/attachments/DGU75TNU/fulltext/images/ad32fa7565737780b2bbd1f660965d1496357d1c6a847659a07cfd7412dd17c2.jpg)  
Figure 1 Business process ecosystem.

From Figure 1, a range of coevolutionary relationships between the four species can be identified. For example, business users and IT developers need to build formal and informal relationships, to share knowledge and to gain insight into each other’s domain, that is, build social capital (Burt, 1992). Taylor-Cummings (1998) reviews the user–IS gap and identifies key factors for the improvement of user– IS relationships that include multi-disciplinary teams, success criteria based on delivering business benefits and close physical proximity. These factors can be seen as enabling conditions that may help promote coevolution in the business process ecosystem between human actors. The coevolution of business users and IT suggests a focus on usability (Nielsen, 1993), and IT developers with software points to the software engineering discipline (Sommerville, 2004). Clearly, the business process ecosystem is an intensely sociotechnical one where technical artefacts and humans are inextricably intertwined in a web of heterogeneous relationships.

We now introduce Kauffman’s (1993) NKC model of coevolution and use business processes to illustrate the working of the model.

## Business process coevolution and the NKC mode

Kauffman’s (1993, 1995a, b) NKC model is a model of genetic interactions on a fitness landscape where there are N characteristics and each characteristic can take one of A states. For example, assume that the inventory control process has four characteristics of interest: inventory level (which should be low to minimize working capital requirements), manual labour requirement (which should be low), inventory level visibility (which should be high) and the number of stock outs (requests for inventory that is not in stock, which should be low). Assume that each of the process characteristics has two states – either it has the desired quality or it does not, that is, A ¼ 2. The number of possible inventory control process configurations on the landscape is A<sup>n</sup>, that is, $2 ^ { 4 } = 1 6 .$ . As the values of N and A increase, the number of positions on the landscape will quickly become very large. In the case of the inventory control process, the different configurations can be represented as a string ranging from 0000 to 1111. These different locations comprise the fitness landscape of the inventory control process.

![](/api/attachments/DGU75TNU/fulltext/images/17fe08ad13bb0ce85ae0489d3dd73c0939190ae8fd704d57f1928dd0f8f1fae1.jpg)  
Figure 2 Business processes and the NKC model.

Figure 2a shows a business process, such as inventory control, with N ¼ 4 characteristics and an internal density of K ¼ 0, that is, each of the N characteristics is independent and can be maximized independently of the other process characteristics. In the case of K ¼ 0, the landscape has a single and smooth-sided peak. Each process characteristic contributes to global fitness independently of the other characteristics and can be tuned for optimal behaviour through ‘universal best-practices’ (Levinthal and Warglien, 1999). Thus, only local intelligence is needed as local improvement will lead to global process improvement.

For values of K greater than 0, the fitness of each location depends on the relationship of that location has with the states of K other locations. For small values of K relative to N, the landscape will have foothills and clear basins of attraction, again leading to the location of a global peak with a high degree of certainty. At the maximum value of K ¼ N1, the landscape becomes random and is very rugged with many peaks. In this scenario, a change to one characteristic of a process, for example, the working capital efficiency in the inventory control process, will impact all the other characteristics (Figure 2b).

Evolution results from an adaptive walk through the landscape where an agent (e.g., a process) seeks to improve its fitness by considering all the one-change neighbouring locations and then making a change if a neighbour provides improved fitness. One characteristic is changed at a time and if none of the neighbouring locations provides improvement, then the agent remains unchanged. Thus, an adaptive walk across the landscape will seek to continually move upwards to points of higher fitness, stopping when a move to a neighbouring point does not increase fitness. A walk on a smooth and single-peaked landscape will lead to a global optimum, but on a rugged landscape it is likely that the walk will end being trapped on a suboptimal peak (the assumption is that hill walking can only move in an upward direction). To avoid being trapped on a suboptimal local peal, and the increased possibility of extinction, organizations need to move beyond incremental search and selection and consider adaptive leaps (Beinhocker, 1999). Unfortunately, for managers seeking a silver bullet solution in coevolutionary theory, adaptive leaps do not guarantee survival either.

Levinthal and Warglien (1999) define robust design as one in which there is moderate interdependence among the elements of a system. A robust design is suitable when it is not clear what the best solution is, but it can be found through an adaptive walk (search and selection) over a smooth surface whereby local adaptation leads to global improvement. Whereas smooth landscapes have long correlation lengths, that is, neighbouring locations have similar heights (fitness values) that make local peaks visible, random landscapes have zero correlation length and rugged landscapes have correlation lengths that decrease as ruggedness increases (Hordijk and Kauffman, 2005). At high values of K relative to N, the peaks proliferate but also get lower and the differences between the peaks and the valleys becomes minimal, that is, complexity is high.

But, managers do not have to accept N and K values and hence the shape of the fitness landscape as given. The ruggedness of a landscape can be tuned by changing the value of K (relative to N). Levinthal and Warglien suggest that organizations can design smooth landscapes by decoupling processes, such as in the Japanese kanban practice where each production station is connected to only two neighbouring ones allowing production to be set to the activity of the downstream station. Internal connections are minimized and the need for central planning and control reduced substantially.

However, evolution is not static; coevolution involves interactions between different species and adaptive moves by the members of one species will deform the fitness landscape of the other species with which it is coevolving (Hordijk and Kauffman, 2005). Thus, processes are not independent and the inventory control process will likely have inter-dependencies with other processes, such as production planning. In Figure 3, process X has values of N ¼ 5 and K ¼ 3 (note that the connections are only shown for a single, focal, business process characterstic in the interests of clarity). There will also be internal connectivity between the characteristics of process Y (not shown). Further, the characteristics of processes X and Y are linked with each characteristic of process X being connected to two characteristics of process Y, that is, C ¼ 2. Now the internal complexity caused by K in a business process is further complicated by external connections, C, to other business processes. Thus, improving the fitness of one process may affect the fitness of another process, which in turn deforms the landscape of the originating process. In this sense, evolution is always coevolution, it is a reciprocating process in which a process not only responds to its environment, but at the same time can be seen to be co-creating its environment. The NKC model depicts tuneable coupled fitness landscapes.

![](/api/attachments/DGU75TNU/fulltext/images/5fb447495aea7d81544670a1b26e1c009dab79fe12701398d3e653d477687e3f.jpg)  
Figure 3 Coevolution of business processes in the NKC model.

Three configurations of coevolution of business processes can be distinguished: competition, exploitation and mutualism (Metcalfe, 1998). Competition is where one configuration seeks to hinder the fitness of other configurations and exploitation is where one configuration stimulates the fitness of another, but is in turn inhibited by that other. Mutualism is where each configuration stimulates the individual and collective fitness. Clearly, mutualism is what is wanted for the processes within an organization, but one can imagine situations in which a process can become cancerous and seek fitness at the expense of the business. Mutualism may also be appropriate for inter-organizational processes between cooperating organizations, although in a supply network there may be exploitation, depending on the balance of power between customers and suppliers. In other configurations, competition would be appropriate, as would likely be the case in the sales and marketing processes of competitor organizations.

Kauffman (1993, 1995a, b) develops two further themes of relevance to the business process ecosystem: the mutation rate and ‘patching’. The behaviour of a population depends on the size of the population, the structure of the landscape and the mutation rate (Kauffman, 1995a: 183). When mutation rates are low, then at long intervals a fitter variant emerges that rapidly colonizes the population; when mutation rates are very high, many fitter and less-fit variants are found quickly and the population may diffuse away from the peak (ibid., p. 184). The second theme is patching, which Kauffman (1995b) argues is a way of taking a complex system (one with many and highly interacting parts) and dividing it up into a quilt of patches in which each patch can be treated as a species that seeks to improve its own fitness while interacting with other patches. Mutation rate has implications for process innovation and patching for selecting the size of processes and services – both of these ideas are explored further in the implications section.

## Business process/IT coevolution

Thus far, we have considered the coevolution of different process species (Figure 3). Now we turn to the coevolution of processes and software components. In Table 1, terms from evolutionary biology are shown in one column with their business process and software equivalents in separate columns.

An organization comprises two populations, S, of processes and software components (services in an SOA). The alleles, A, indicate the different states a process or service can take. For a process, these states could relate to maturity, flexibility, robustness and for a service might relate to software quality attributes such as reliability, scalability, flexibility and testability. Disturbance, W, relates to one-way influence, for example, a regulatory body may be able to affect the way in which a business process such as the selling of financial products is executed. However, the reverse is assumed not to be the case, that is, the business process does not affect the regulatory requirement.

Kauffman (1995a) identifies two main behaviours relating to C-coupled landscapes. The first is the ‘Red Queen Effect’, coined by Lee Van Valen (1973) from the Red Queen saying to Alice ‘it takes all the running you can do, to keep in the same place’. All the species keep changing their genotypes in a never-ending race to sustain their fitness level. The population never settles down to an unchanging mix of genotypes as species chase peaks that recede into the distance. The second image is of coevolving species that reach an evolutionary stable strategy (ESS) and then stop changing genotypes. Species that have attained an ESS have succeeded in climbing to a peak and remaining on it – coevolution ceases and an ordered regime emerges, although it is likely that this peak is not a particularly high one. As in the prisoner’s dilemma, a species has no incentive to change as long as its partnering species do not change (i.e., a Nash equilibrium has been attained). Kauffman (1995a) sees Red Queen behaviour as chaotic with species climbing and plunging, while the ESS is an ordered regime that is too rigid and unable to move away from suboptimal local peaks (p. 221). Kauffman (1995a) argues that ‘the highest average fitness in coevolving systems appeared to arise just at the phase transition between Red Queen chaos and ESS order’ (pp. 257–258). This phase transition is a place favoured by coevolution and is also known as the edge of chaos.

Table 1 The NKC model applied to an organization’s business processes and service-oriented architecture, adapted from McKelvey (1999) and McCarthy (2003)

<table><tr><td>Variable</td><td>Evolutionary biology</td><td>Business processes</td><td>SOA</td></tr><tr><td>S</td><td>A species which is a population that can be treated as a homogeneous entity</td><td>There are two species - process species and software species - that is, S=2</td><td></td></tr><tr><td>N</td><td>The number of genes in the evolving genotype</td><td>The number of processes enacted within an organization</td><td>The number of software components (services) implemented within an organization&#x27;s SOA</td></tr><tr><td>K</td><td>The degree of internal connectedness among the genes</td><td>The degree of connectedness between processes within an organization</td><td>The degree of connectedness between software components (services) in an organization&#x27;s SOA</td></tr><tr><td>A</td><td>The number of alleles (alternative states) that a gene may take</td><td>The number of possible states that a process can take</td><td>The number of possible states that a software component (service) can take</td></tr><tr><td>C</td><td>The coupledness of the genotype with other genotypes</td><td>The coupledness of process types and service types within an organization</td><td></td></tr><tr><td>W</td><td>Coupling to a gene in the external world that causes disturbance in one direction only</td><td>External constraints such as regulatory bodies that can restrict the way that a business process is conducted or a service executed</td><td></td></tr></table>

Brown and Eisenhardt (1998) say that organizations that achieve the edge of chaos will compete more effectively than those that do not; at the edge of chaos ‘organizations never quite settle into a stable equilibrium but never quite fall apart, either’ (p. 12). This view is supported by Kauffman (1993) and Anderson (1999), who claims ‘Systems that are driven to (but not past) the edge of chaos out-compete systems that do not’ (pp. 223–224). Lewin and Volberda (1999) summarize the importance of achieving the edge of chaos for organizations:

At this ‘edge of chaos’, an organization is assumed to optimize the benefits of stability, while retaining capacity to change by combining and recombining both path dependence and path creation processes. Such an organization creates sufficient structure to maintain basic order but minimizes structural interdependencies. It evolves internal processes that unleash emergent processes such as improvisation, self-organizing, emergent strategies and strange attractors (e.g., product champions) (p. 530).

In the context of organizations, it is better to think of a ‘region of emergent complexity’ (McKelvey, forthcoming) rather than an ‘edge of chaos’. This region lies between stasis and chaos and is defined by two critical values. If an organization falls below the first critical value because it exhibits minimal response to addressing the adaptive tensions it faces then order will prevail. If the organization over-responds to its adaptive tensions, for example, by initiating too many change programmes too quickly, then it may exceed the second critical value and chaos ensue. Kauffman finds that the ecosystem settles to an ESS if the internal density of connections, K, within species are high (there are a lot of low peaks to be trapped on) and the coupling between the species is low (landscapes do not deform much as a species makes an adaptive move). The ESS ordered regime also emerges when the number of species is low (moves by one process do not deform the landscape of many other processes). Thus, an ordered regime emerges when K is high and C or S is low. This suggests that an organization with tightly coupled processes with low connectivity to monolithic software applications will tend toward order and stasis. A chaotic regime emerges when K is low and C or S is high: an organization with loosely coupled processes with high connectivity to loosely coupled services (this is, after all, one aim of an SOA) could lead to chaotic behaviour. Kauffman finds that when K and C are kept constant and S is varied, an ESS emerges after

1600 generations when S ¼ 4. For values of S ¼ 8 and S ¼ 16, no ESS emerged after 8000 generations, that is, Red Queen behaviour is exhibited. Kauffman also finds that the transition area between an ESS and chaotic behaviour (the edge of chaos or region of emergent complexity) was highly sensitive to the value of K. If K is not allowed to change, then starting an ecosystem with high values of K means that the species will climb to local peaks and stay there, that is, an ESS results. If the ecosystem is started with low values of K, then the Red Queen effect results. Kauffman (1995a) models an ecosystem in which K is allowed to change and finds that the system converged on an optimal value of K where average fitness of species is highest and the extinction rate lowest: ‘The coevolving system tunes its own parameters, as if by an invisible hand, to an optimal K value for everyone’ (p. 232), that is, the ecosystem self-organizes.

## Coevolution as a multi-level phenomenon

Lewin and Volberda (1999) list multi-levelness/embeddedness as a core requirement for conducting coevolutionary research in organizations. They argue that coevolutionary effects take place at multiple levels, within firms as well as between firms. They also note that most research is either at the population level focusing on macroevolutionary theory of the firm or at the microevolution, intra-firm level investigating capabilities and competencies of the individual organization in its competitive context (p. 526). McKelvey (1999) asserts that coevolution at lower levels occurs in the context of higher levels of coevolution.

The coevolutionary relationships in Table 1 are expressed at a level of recursion where an organization is viewed as comprising two species – business processes and software components. The multi-level aspects of coevolutionary theory identified by Lewin and Volberda (1999) suggest that the model can be extended upwards and downwards. Looking up a level, we can picture organizations coevolving within an industry through NK relationships and connecting to organizations in other industries through NKC relationships. Such an extension to multiple organizations is of particular value in studying business-tobusiness relationships and inter-organizational systems (Riggins and Mukhopadhyay, 1994; Clark and Stoddard, 1996). Looking down a level, a business process can be broken into interconnected activities (or tasks) and similarly a service is a bundle of functions that can be invoked by business process activities and by other services. Infinite regress applies in both directions, and as with any recursive model, it is a question of fixing on a focal level of analysis and then deciding on a number of levels to look up and down.

## Business process coevolution as a social system

Thus far, we have applied the NKC model to business processes and IT, but an examination of Figure 1 makes it clear that a limitation of the foregoing analysis is the absence of human agency and a social perspective. Mitleton-Kelly (2000) argues that in a social ecosystem, each agent is a fully participating member that both influences and is influenced by the ‘social ecosystem made up of all related businesses, consumers, suppliers, as well as economic, cultural, and legal institutions’. In the future, processes and services may well be able to evolve and coevolve themselves, but today human intervention is needed and with humans comes the issue of relationships, social networks and the sharing of ideas and knowledge. Capra (2002) argues that we must adapt complex systems theory for new domains:

Social networks are first and foremost networks of communication involving symbolic language, cultural constraints, relationships of power and so on. To understand the structures of such networks we need to use insights from social theory, philosophy, cognitive science, anthropology and other disciplines. A unified systemic framework for the understanding of biological and social phenomena will only emerge when the concepts of nonlinear dynamics are combined with insights from these fields of study (p. 71).

Capra (2002) considers Habermas’ critical theory and Giddens’ structuration theory as possible social theories that could provide insight into the agency of human agents and the creation of social structures (and the recursive relationship between the two). Habermas (1972) is part of the critical school and identifies different knowledge interests: technical, practical and emancipatory. The technical interest is concerned with control and an engineering metaphor; the practical interest is concerned with understanding and language and the facilitator metaphor; the emancipatory interest is concerned with criticism and power and the emancipator metaphor (Hirschheim and Klein, 1989). Giddens (1984) depicts social structure and human action using the dimensions of signification/communication, domination/power and legitimation/sanction. Each of the dimensions is mediated by three modalities: interpretative scheme – stocks of knowledge drawn upon by human actors to make sense of their own and others’ actions; facility – the ability to allocate resources (human and material); norm – actions are sanctioned by drawing upon standards concerning ‘good’ and ‘bad’. According to Giddens, human action not only reinforces the existing structures of meaning but can also change existing structures and create new structures. Structuration theory also acknowledges unintended consequences of intentional human activity and recognizes practical consciousness, that is, people are more knowledgeable than ‘what they can say’.

Undoubtedly, an injection of social theory will be needed to gain insight into the coevolution of human relationships. Inspection of Figure 1 shows that there is also coevolution of humans with technology, which is not fully accounted for by inter-subjective social theories such as Giddens’ structuration theory. Thus, we may also need to consider the agency of technology through ideas such as actor network theory (Latour, 1987) where the term ‘actant’ is used to signify human and non-human actors that are inseparably intertwined in a sociotechnical imbroglio where each shapes the other. The actor network view of human/ technology relationships would appear to resonate with coevolutionary theory. Pickering (1995) takes a less strongly symmetrical view of the agency of people and things, pointing out that human actors have intentionality and proposes the idea of technology having the property of ‘affordance’. Jones (1998) also argues that humans and technology are different because humans have intentions that are organized around plans and goals, although this does not mean that human plans and goals are necessarily explicitly formulated or that human actors are fully aware of their motivations or capable of realizing them. From a coevolutionary perspective, it seems reasonable to take the actor network idea of inseparability, but to also recognize that humans and things may need to be seen as having essential differences, that is, they are separate (but coevolving) species.

## Implications for BPM

In this section, we draw out the implications of coevolutionary theory for BPM. These are landscape tuning and multiple levels of analysis, exploration and exploitation, time-pacing and the greater management challenge of maintaining the business process ecosystem in the region of emergent complexity.

Kauffman’s NKC model can give considerable insight into the design of intra- and inter-organizational processes and IT infrastructures. Through the building of appropriate models and the subsequent tuning of the values of N, K and C, it may be possible to discover laws applicable to business processes and software services. For example, it will be possible to vary the number of processes and services (N), the internal density of interconnections of processes and services (K) and the external coupling of processes and services (C) to gain insight into patterns of behaviour in the business process ecosystem. Further, the NKC model might also be applied to other aspects of the ecosystem, such as stakeholders (Rowley, 1997): the NKC model suggests that a large number of stakeholders (N) with low internal connectivity (K) but high external coupling (C) could create undesirable Red Queen complexity in the business process ecosystem.

It is also possible to investigate difficult questions such as how ‘big’ processes and services should be (i.e., granularity) through picking ‘patches’ of an appropriate size (Kauffman, 1995b):

I wonder if there is some optimal way to break the total production process into local patches, each with a modest number of linked production steps: keep partitioning the system into smaller smaller patches. When overall performance degrades, break up to slightly larger patches. Then one could optimize within each patch, let the patches coevolve, and rapidly attain excellent overall performance (p. 128).

These ideas can be tested by building models and running simulations to see what patterns of behaviour emerge as the variables in the NKC model are varied, as in the work of Rivkin (2001), who investigates complexity and strategy imitation, and Rivkin and Siggelkow (2003), who model the balance between exploration and exploitation (see Maguire et al. (2006) for a review of fitness landscape applications). A further way to research the implications of coevolution and tuning of variables in business process ecosystems is through agent-based modelling, which has been applied extensively to supply chain management (Anthes, 2003). Ideally, these models and agent-based simulations would be created for different levels of analysis. For example, a model of business processes where S is the number of processes in an organization would have C coupling between processes at that level of recursion (Figure 3). This C coupling would be a contributor to the K coupling at the next level of recursion up, where processes coevolve with IT at the level of the organization (Table 1). The different levels clearly need to be intertwined and emergent properties at different levels identified, as indeed they are in Stafford Beer’s viable system model (Beer, 1984), while also recognizing that the ecosystem in Figure 1 is about a network of interacting species.

To maximize their chances of achieving fitness organizations should synchronize concurrent exploration and exploitation, a balance of innovation and knowledge creation with continuous improvements in productivity and process improvement. Overemphasis of exploitation leads to a competence trap, while an emphasis on exploration can have negative consequences such as over-sensitivity to noise and short-term variations, and becoming a victim of fashion and fads. In the NKC model, exploitation is achieved through the adaptive walk, while exploration may involve long jumps across the landscape. Kauffman (1995a) reports that every time a fitter long-jump variant is found, the expected number of tries to find an even fitter long-jump doubles (p. 194). This suggests that organizations should mix long jumps (exploration) with adaptive walks (exploitation) with the implication that radical process redesign and continuous process improvement need to be pursued simultaneously.

Related to the issue of exploration and exploitation is the pace of change. How often should process or technology innovations be introduced? The mutation rate can be influenced in an organizational setting by ‘time-pacing’. Brown and Eisenhardt (1998) define time-pacing as an internal metronome that drives organizations according to the calendar, for example, ‘creating a new product every nine months, generating 20% of annual sales from new services’ (p. 167). Time-pacing requires organizations to change frequently, but can also stop them from changing too often or too quickly. Rhythm is used by organizations to synchronize their clock with the marketplace and with the internals of their business. From a process perspective this could mean, for example, that business process owners must introduce a process innovation every 4 months, while IT managers must evaluate and pilot a new technology every 6 months. Time-pacing is therefore not arbitrary, although Brown and Eisenhardt give no indication as to how an organization might identify and set the pace of the internal metronome. As with patching, perhaps the approach taken needs to be pragmatic and local – require changes of process owners and IT managers on a periodic basis and continue to increase the frequency until the ecosystem begins to be unstable, at which point back off.

The wider challenge for IS management is to consistently strive to shape, design and manage their organizations, so as to remain in the region of emergent complexity, that is, to create the enabling conditions that will enable the business process ecosystem to flourish, avoiding the extremes of stasis and chaos. At first sight, this might seem to suggest that managers abandon command and control strategies in favour of a hands-off approach where autonomous agents are encouraged to interact and selforganize. Rather than consent to one or other of these poles, that is, managers as in control or managers as undifferentiated agents in the ecosystem, managers will need to embrace the paradox of control, that is, they are simultaneously ‘in control’ and ‘not in control’ and will need to learn to live with the anxiety that results (Streatfield, 2001).

## Limitations and further theoretical development

Among the limitations identified by McKelvey (1999) of applying the NKC model to organizations is a recognition that any model, no matter how well designed, is still a model. However, McKelvey (1999) also argues that although Kauffman uses the language of evolutionary biology, his NKC model was derived from physics and computer science and may be more applicable to organizations than it is to genes. There is then the larger question of whether complex systems theory in general should be applied to organizations. Stacey (2003) is critical of Brown and Eisenhardt (1998), arguing that they make loose and simplistic interpretations of complex systems. Stacey (2003) argues that being at the edge of chaos is no guarantee of survival and that Brown and Eisenhardt, through their implicit use of the language of cybernetics and cognitivism, absorb complex systems theory into traditional organizational theory. Following Capra (2002), it seems likely that an injection of social (indeed, sociotechnical) theory is needed to avoid the limitations and pitfalls of a machine metaphor.

Lewin and Volberda (1999) argue that to be effective coevolutionary research must be: conducted over a long period of time, take into account the historical context and path dependencies, consider multi-directional causalities between micro- and macroevolution and be aware of nonlinearities and lagged and nested effects (pp. 526–527). Although such a research approach is likely to be difficult, the potential outcome of a theory for agile enterprise suggests it may be a worthwhile endeavour.

## Conclusions

Smith and Fingar (2003) argue that BPM obliterates the business/IT divide, in part, due to organizing around adaptive business processes rather than around IT applications. However, coevolution suggests that there is a divide and that this may be desirable since each can be viewed as a species with its own fitness landscape that it must traverse. But, coevolution also shows us that business environment and technology are inextricably interwoven and mutually shaping. Thus, we might better replace the IT/business divide and its obliteration by an emphasis on coevolution of distinct species. Nicholas Carr (2003) writes provocatively in the Harvard Business Review that ‘IT Doesn’t Matter’. His argument is that IT is accessible and affordable by all and that the strategic potential of IT as a differentiator is being inexorably reduced, that is, IT is highly replicable and will become increasingly commoditized. A coevolutionary perspective suggests that this view is, in part, true as firms adopt an SOA and standards are agreed and embedded, but having a commodity does not mean that it will be used well and firms that can establish a viable business process ecosystem that promotes coevolution of business processes and IT infrastructure will be more likely to achieve competitive advantage than those that do not. The challenge for management, then, is to establish the conditions for the business process ecosystem – a mix of human and non-human species – to operate and maintain itself in a region of emergent complexity, a region bounded by stasis and chaos. Further, managers must recognize that they are embedded within the ecosystem and that they are themselves shaped by, as well as shaping, the ecosystem.

## Acknowledgements

We thank the anonymous reviewers for the valuable and detailed comments they provided and Eve Mitleton-Kelly for her constructive criticism of an earlier version of the paper. We also particularly thank the special issue editors, Bill McKelvey and Yasmin Merali, for the support, guidance and encouragement they gave us in making revisions to this paper. Any remaining errors are ours.

## References

Anderson, P. (1999). Complexity Theory and Organization Science, Organization Science 10(3): 216–232.

Anthes, G. (2003). Agents of Change: Software agents tame supply chain complexity and optimize performance. Computerworld, January, [www document]http://www.computerworld.com/softwaretopics/erp/ story/0,10801,77855,00.html(accessed 15 June 2005).

Beer, S. (1984). The Viable System Model: Its provenance, development, methodology and pathology, Journal of the Operational Research Society 35: 7–26.

Beinhocker, E. (1999). Robust Adaptive Strategies, Sloan Management Review 40(3): 95–106.

Brown, S. and Eisenhardt, K. (1998). Competing on the Edge: Strategy as Structured Chaos, Boston: Harvard Business School Press.

Burt, R. (1992). Structural Holes: The Social Structure of Competition, Cambridge, MA: Harvard University Press.

Capra, F. (1996). The Web of Life: A New Synthesis of Mind and Matter, London: Harper Collins.

Capra, F. (2002). The Hidden Connections, London: Harper-Collins.

Carr, N. (2003). IT Doesn’t Matter, Harvard Business Review 81(5): 41–49.

Champy, J. (2002). X-Engineering the Corporation: Reinvent your Business in the Digital Age, Hodder and Stoughton, London.

Clark, T. and Stoddard, D. (1996). Interorganizational Business Process Redesign: Merging technological and process innovation, Journal of Management Information Systems 13(2): 9–28.

Davenport, T. (2002). The New Reengineering? Darwin Magazine, September. [www document] http://www.darwinmag.com/read/090102/order.html (accessed 4 November 2004).

Davenport, T. and Short, J. (1990). The New Industrial Engineering: Information technology and business process redesign, Sloan Management Review 31(4): 11–27.

Davenport, T. and Stoddard, D. (1994). Reengineering: Business change of mythic proportions, MIS Quarterly 18(2): 121–127.

Ehrlich, P. and Raven, P. (1964). Butterflies and Plants: A study in coevolution, Evolution 18: 586–608.

Giddens, A. (1984). The Constitution of Society, Cambridge: Polity Press.

Grover, V. (1999). From Business Reengineering to Business Process Change Management: A longitudinal study of trends and practices, IEEE Transactions on Engineering Management 46(1): 36–46.

Grover, V. and Kettinger, K. (1995). Toward a Theory of Business Proces Change, Journal of Management Information Systems 12(1): 1–21.

Habermas, J. (1972). Knowledge and Human Interests, London: Heinemann.

Hagel, J. (2002). Out of the Box: Strategies for Achieving Profits Today and Growth Tomorrow Through Web Services, Harvard Business School Press, Boston, Mass.

Hammer, M. (1990). Reengineering Work: Don’t automate, obliterate, Harvard Business Review 68(4): 104–112.

Hammer, M. (2001). The Agenda: What Every Business Must Do to Dominate the Decade, Random House Business Books, New York, NY.

Harrington, H. (1991). Business Process Improvement, New York: McGaw-Hill. Hirschheim, R. and Klein, H. (1989). Four Paradigms of Hirschheim, R. and Klein, H. (1989). Four Paradigms of

Information Systems Development, Communications of the ACM 32(10): 1199–1216.

Hordijk, W. and Kauffman, S. (2005). Correlation Analysis of Coupled Fitness Landscapes, Complexity 10(6): 41–49.

Jones, M. (1998). Information Systems and the Double Mangle: Steering a course between the Scylla of embedded structure and the Charybdis of strong symmetry, in T. Larsen, L. Levine and J. DeGross (eds.) Information Systems: Current Issues and Future Changes, Proceedings of IFIP WG8.2/8.6 joint Working Conference, Helsinki, Finland, pp. 287–302.

Kauffman, S. (1993). The Origins of Order: Self Organization and Selection in Evolution, New York: Oxford University Press.

Kauffman, S. (1995a). At Home in the Universe, London: Penguin Books.

Kauffman, S. (1995b). Escaping the Red Queen Effect, The McKinsey Quarterly 1: 119–129.

Latour, B. (1987). Science in Action, Cambridge, MA: Harvard University Press. Leonard-Barton, D. (1988). Implementation as Mutual Adaptation of Leonard-Barton, D. (1988). Implementation as Mutual Adaptation of

Technology and Organization, Research Policy 17(5): 251–267.

Levinthal, D. and Warglien, M. (1999). Landscape Design: Designing for local action in complex worlds, Organization Science 10(3): 342–357.

Lewin, A. and Volberda, H. (1999). Prolegomena on Coevolution: A framework of research on strategy and new organizational forms, Organization Science 10(5): 519–534.

Maguire, S., McKelvey, B., Mirabeau, L. and O<sup>¨</sup> ztas, N. (2006). Complexity Science and Organization Studies, in S. Clegg, C. Hardy and T. Lawrence (eds.) The Sage Handbook of Organization Studies, 2nd edn. Thousand Oaks, CA: Sage.

McCarthy, I. (2003). Technology Management – A complex adaptive systems approach, International Journal of Technology Management 25(8): 728–745.

McKelvey, B. (forthcoming). MicroStrategy from MicroLeadership: Improving distributed intelligence via complexity science, in A. Lewin and H. Volberda (eds.) Mobilizing the Self-Renewing Organization, New York: Palgrave Macmillan.

McKelvey, B. (1999). Avoiding Complexity Catastrophe in Coevoutionary Pockets: Strategies for rugged landscapes, Organization Science 10(3): 294–321.

Metcalfe, J. (1998). Evolutionary Economics and Creative Destruction, London: Routledge.

Mitleton-Kelly, E. (2000). Co-Evolution and an Enabling Infrastructure: A solution to legacy? in P. Henderson (ed.) Systems Engineering for Business Process Change, Springer-Verlag, London.

Nielsen, J. (1993). Usability Engineering, San Francisco: Morgan Kaufmann.

Peppard, J. and Breu, K. (2003). Beyond Alignment: A coevolutionary view of the information systems strategy process, in: Proceedings of the Twenty-Fourth International Conference on Information Systems, December, Seattle, WA.

Pettigrew, A., Whittington, R., Melin, L., Sanchez-Runde, C., van den Bosch, F., Ruigrok, W. and Numagami, T. (2003). Innovative Forms of Organizing, London: Sage Publications.

Pickering, A. (1995). The Mangle of Practice: Time, Agency and Science, Chicago: University of Chicago Press.

Riggins, F. and Mukhopadhyay, T. (1994). Interdependent Benefits from Interorganizational Systems: Opportunities for business partner reengineering, Journal of Management Information Systems 11(2): 37–57.

Rivkin, J. (2001). Reproducing Knowledge: Replication without imitation at moderate complexity, Organization Science 12(3): 274–293.

Rivkin, J. and Siggelkow, N. (2003). Balancing Search and Stability: Interdependencies among elements of organizational design, Management Science 49(3): 290–311.

Rowley, T. (1997). Moving Beyond Dyadic Ties: A network theory of stakeholder influences, Academy of Management Review 22(4): 887–910.

Silicon.com (2003). Web services are the next IT storm, Forrester CEO says. 10 March 2003,www.silicon.com.

Smith, H. and Fingar, P. (2003). Business Process Management: The Third Wave, Tampa, FL: Meghan-Kiffer Press.

Sommerville, M. (2004). Software Engineering, 7th edn. Reading, MA: Addison Wesley.

Stacey, R. (2003). Strategic Management and Organisational Dynamics: The Challenge of Complexity, 4th edn. Financial Times Prentice-Hall, Harlow, England.

Stal, M. (2002). Web Services: Beyond component-based computing, Communications of the ACM 45(10): 71–76.

Streatfield, P. (2001). The Paradox of Control in Organizations, London: Routledge.

Taylor-Cummings, A. (1998). Bridging the User–IS Gap: A study of major information systems projects, Journal of Information Technology 13: 29–54.

the451 (2002). The SOAP Bubble: a Web services taxonomy. White Paper.www.the451.com(accessed 12 December 2004).

Van Valen, L. (1973). A New Evolutionary Theory, Evolutionary Theory 1: 1.

Wright, S. (1932). The Roles of Mutation, Inbreeding, Crossbreeding and Selection in Evolution, Proceedings of the Sixth International Congress on Genetics 1: 356–366.

xml.com (2003). Web Services definition, http://webservices.xml.com/pub/a ws/2003/09/30/soa.html.. (accessed 20 November 2004).

## About the authors

Richard Vidgen is Professor of Information Systems in the School of Management at the University of Bath. He worked in information systems development in industry for 15 years, during which time he was employed by a large US software firm and as a consultant. In 1992, he left industry to join the University of Salford, where he completed a Ph.D. in systems thinking and information system quality. His current research interests include complex systems theory, information system development methodologies and e-commerce quality. He has published the books Data Modelling for Information Systems (1996) and Developing Web Information Systems (2002) as well as many book chapters and journal papers.

Xiaofeng Wang worked for several years in a research laboratory in Italy where she investigated enterprise knowledge systems. She is currently completing her doctoral studies in Information Systems at the School of Management, University of Bath. Her research interests include information system development methodologies, software development process and applying complex systems theory to research in these areas.
