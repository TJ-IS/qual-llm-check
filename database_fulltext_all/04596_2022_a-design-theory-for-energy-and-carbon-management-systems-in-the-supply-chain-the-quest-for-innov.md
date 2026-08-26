---
otero_id: 4596
otero_key: "T4DC32W6"
title: "A Design Theory for Energy and Carbon Management Systems in the Supply Chain The Quest for Innovation in Information Systems Research: Recognizing, Stimulating, and Promoting Novel and Useful Knowledge"
authors: "Eleni Zampou; Ioannis Mourtos; Katerina Pramatari; Stefan Seidel"
year: "2022"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00725"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2022

# A Design Theory for Energy and Carbon Management Systems in the Supply Chain

Eleni Zampou , zampoueleni@aueb.gr

Ioannis Mourtos , mourtos@aueb.gr

Katerina Pramatar , k.pramatari@aueb.gr

Stefan Seidel , stefan.seidel@wiso.uni-koeln.de

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# A Design Theory for Energy and Carbon Management Systems in the Supply Chain

Eleni Zampou<sup>1</sup>, Ioannis Mourtos<sup>2</sup>, Katerina Pramatari<sup>3</sup>, Stefan Seidel<sup>4</sup>

<sup>1</sup>ELTRUN Research Center, Athens University of Economics and Business, Greece, zampoueleni@aueb.gr <sup>2</sup>ELTRUN Research Center, Athens University of Economics and Business, Greece, mourtos@aueb.gr <sup>3</sup>ELTRUN Research Center, Athens University of Economics and Business, Greece, k.pramatari@aueb.gr <sup>4</sup>University of Liechtenstein, Liechtenstein, stefan.seidel@uni.li

## Abstract

Energy and carbon management systems (ECMS) are a class of green information systems that has the potential to increase environmental sustainability in organizations and across supply chains. Employing a design science research approach, we define the scope of ECMS in the supply chain context, identify requirements, design an expository instantiation, and develop an information systems design theory, including key constructs and design principles. We instantiate this theory in four supply chain contexts to validate and revise the proposed design in two rounds. We identify six system components—data collection, energy monitoring, supply chain coordination, ECMS workflow engine, reporting, and carbon footprint estimator—that integrate and coordinate four types of information flows (transactional, contextual, energy, and product-environmental), and formulate design principles. Our evaluation indicates that the ECMS design theory, if instantiated, supports energy and carbon measurement and environmentally aware decision-making and practice in supply chains. We also highlight how considering energy information flows in combination with material features that afford environmentally aware decision-making and practice are key to qualifying information systems as “green.”

Keywords: Energy and Carbon Management Systems, Green Information Systems, Sustainable Supply Chain Management, Design Science Research, Sustainability

Roger Chiang was the accepting senior editor. This research article was submitted on December 2, 2019 and underwent two revisions. The second, third, and fourth authors contributed equally and are listed in alphabetical order.

## 1 Introduction

Pressures from climate change and pollution, along with stricter regulations, rising energy prices, and changing consumer behaviors, are forcing organizations to develop sustainable supply chains (Ansari & Kant, 2017; Bové & Swartz, 2016; Rajeev, et al., 2017). While recent industry initiatives have suggested that organizations are seeking to develop more energyefficient facilities (e.g., Reuters, 2018; Yang, 2018), less than 20% of the industry participants of a recent survey report a comprehensive awareness of their supply chains’ sustainability performance (Winston & Bonini, 2019), possibly because determining such performance remains challenging (Acquaye et al., 2018; Qorri et al., 2018; Sloan, 2010).

Using the capabilities of information systems (IS) to standardize, monitor, capture, and use data and metadata and to evaluate financial and environmental performance indicators is key to implementing sustainable supply chains (Björklund et al., 2012; Dao et al., 2011; de Camargo & Jabbour, 2017; Lee & Wu, 2014; Melville, 2010). IS facilitate collaboration and information exchange by improving information flows among supply chain partners, which allows for an interorganizational perspective on sustainability (e.g., Banker et al., 2006; Gunasekaran & Ngai, 2004; Thies & Stanoevska-Slabeva, 2013).

Energy and carbon management systems (ECMS) are a class of IS that receive heterogeneous types of environmental data (e.g., electricity and fuel use, emission factors) as inputs, process them to calculate energy-related key performance indicators (KPIs) and derive carbon emissions, and offer functionalities like supply-chain analytics, workflow management, and automated reporting (Melville & Whisnant, 2014). Still, how ECMS can assist the development of sustainable supply chains (de Camargo & Jabbour, 2017) and how one should design and implement these systems remain unclear. While some studies explore the design and implementation of various IS for environmental sustainability (Graeuler et al., 2013; Hilpert et al., 2011; Seidel et al., 2018), they do not attend to designing systems for supply chain management. Therefore, our objective is to inform the design and implementation of ECMS for sustainable supply chain management. This goal deserves our attention, as the supply chain context poses challenges that move beyond those involved in the design and implementation of ECMS within the boundaries of an organization.

We adopt a design science research (DSR) approach (Peffers et al., 2007), combined with elements from action design research (ADR) (Sein et al., 2011), to derive a design theory for ECMS in the supply chain context. Our approach is process oriented, systematic, and iterative (Hevner et al., 2004; Gregor & Hevner, 2013; Peffers et al., 2007). We use the basic components of IS design theory (Gregor & Jones, 2007) as an abstract blueprint to formulate our design theory, and we instantiate and iteratively develop this theory in two DSR rounds in four organizations. These organizations operate in different sectors and have supply chains that range from the supply of raw materials to manufacturing to the point of sales. The four organizations consist of two textile manufacturers—

a textile manufacturer for fashion and luxury markets and an international clothing company seeking to improve their energy-aware production—and two organizations in the fast-moving consumer goods (FMCG) sector, namely a grocery retailer and a major food manufacturer seeking to develop sustainable supply chains.

We proceed as follows. First, we summarize the findings from studies on energy and carbon management (ECM) in supply chains, as well as from work on information systems and environmental sustainability in general and ECMS in particular. Then we introduce our research approach. After formulating a design theory in terms of purpose and scope, design requirements, core constructs, principles of form and function, and expository instantiation, we describe our implementation, including evidence from two rounds of theory instantiation as well as artifact demonstration and evaluation via proof-ofconcept and proof-of-value research (Nunamaker et al., 2015). We conclude by highlighting our findings contributions and practical implications and discuss limitations and suggestions for future research.

## 2 Research Background

## 2.1 Energy and Carbon Management in Sustainable Supply Chains

Organizations’ transition to sustainable supply chains (SSCs) requires the development of performance measurement (Janssen et al., 2015; Qorri et al., 2018), as highlighted in the reviews of Ahi and Searcy (2015), Hassini et al. (2012), and Tajbakhsh and Hassini (2015). Such measurements help organizations to monitor and evaluate their environmental performance, make environmentally aware decisions, predict pitfalls, and be proactive (Gunasekaran et al., 2004; Gunasekaran & Kobu, 2007). Apart from guiding compliance with standards and regulations (Qorri et al., 2018; Seuring & Müller, 2008; Taticchi et al., 2013), such measurements support cost reduction, efficiency (Acquaye et al., 2018), supply chain innovation, and risk management (Schaltegger & Burritt, 2014).

Since incorporating both environmental and nonenvironmental aspects in supply chain management is central to the ability to make the trade-offs among the dimensions of performance (Björklund et al., 2012), a growing number of firms have integrated environmental indicators into the management of their supply chains (Hua et al., 2011; Lee, 2014; Rajeev et al., 2017; Sundarakani, 2010). Specifically, they consider energy and fuel consumption and carbon emission indicators as parameters for solving traditional operational problems, such as production optimization (Du et al., 2016; Nouira et al., 2014; Plitsos et al., 2017), inventory management (Arıkan & Jammernegg, 2014; Hua et al., 2011; Konur et al., 2017), vehicle routing (Ehmke et al., 2018; Xiao et al., 2019; Zhang et al., 2018), inventory routing (Cheng et al., 2016; Kuo et al., 2014), network design (Li et al., 2020; Martí et al., 2015), and even supplier selection (e.g., Genovese et al., 2013; Govindan et al., 2015; Zimmer et al., 2016). Zhou and Wen (2020) offer a comprehensive, updated review of carbon-constrained operations models.

Calculating environmental indicators and ensuring transparency in supply chains is feasible only if the appropriate measurement and management tools are available (Janssen et al., 2015). Janssen et al. (2015) and Qorri et al. (2008) provide overviews of performance measurement and management approaches developed over the last twenty years. These approaches are often linked to standards of environmental management (e.g., ISO 14000 series) or product life cycle assessments (LCA), as well as to reporting initiatives like the Global Reporting Initiative (GRI) (1997) and the Carbon Disclosure Project (CDP) (2000).

Still, considerable debate remains on how firms should measure SSC performance. Hassini et al. (2012) have identified more than one hundred potential indicators and have provided a list of frameworks for SSC management and environmental performance measurement, whereas Ahi and Searcy (2015) have provided evidence indicating that only measures of product quality, greenhouse gas (GHG) and other emissions, and energy consumption are widely used. Tuni et al. (2018) classified these metrics into input and output categories and pointed out that most of the input metrics focus on resource and energy consumption, while the output metrics focus on GHG and carbon emissions. GHG emissions are typically reported as a single CO<sub>2</sub> equivalent, using the global warming potential weighting factors, and are usually aggregated with carbon emissions into a single carbon emissions or CO<sub>2</sub>-equivalent metric. Thus, energy consumption and carbon emissions are the two most prominent environmental performance metrics, and both public authorities and private companies (e.g., European Commission 2018; Techcrunch, 2019; TESCO, 2017) have considered improving energy consumption and carbon emissions as key targets for regulatory emission-control policies and companies’ carbon emission and energy cost reduction policies (Ahi & Searcy, 2013; Varsei et al., 2014).

The energy that is consumed by all supply chain activities—production, storage, transportation, and so on—includes electricity and fuel consumption from both renewable and nonrenewable sources. Carbon emissions are based heavily on energy consumption, as the energy generation process directly affects their input-output relationship. Renewable energy creates vastly fewer carbon emissions than nonrenewable energy extracted from fossil fuels. Considering the continued limited adoption of renewable energy (18.9% of total energy consumed in the European Union and 8.3% of that consumed in transport activities) (Eurostat, 2020), emissions remain strongly correlated with energy consumption.

Measuring environmental performance is challenging because of limited data availability (Bjorklund et al., 2012; Veleva et al., 2003), diverse supply chain players (Ahi & Searcy, 2015; Hervani et al., 2005), incompatibility of classic supply chain measures with an intraorganizational scope rather than an interorganizational scope (Lehtinen & Ahola, 2010), lack of trust and fear about data confidentiality (Hassini et al., 2012), and current enterprise systems’ insufficient capture of nontraditional performance data (Hervani et al., 2005). As a result, organizations require IS to capture and analyze data for every supply chain activity and for each aspect of sustainability (Maestrini et al., 2017; Qorri et al., 2018); that is, the success of the measurement system in the supply chain depends on the ability of the IS of each supply chain member to capture data related to the sustainability dimensions for every supply chain activity (Qorri et al., 2018). Accordingly, we seek to show how IS can address the requirements of energy and carbon management to allow for SSC management and to highlight pertinent implementation issues.

## 2.2 Information Systems and Sustainability Transformations

IS play a pivotal role in sustainability transformations in terms of organizational sensemaking (Seidel et al., 2013), decision-making and knowledge creation (Butler, 2011), belief formation (Melville, 2010), automation (Dao et al., 2011), and innovation (Melville, 2010). IS can facilitate cognitive activities through which individuals across an organization can frame, interpret, and understand the multilayered and complex issues related to environmental sustainability transformation in order to develop sustainabilityrelated actions (Seidel et al., 2013). IS support decision-making related to the environmental sustainability regulations with which firms increasingly must comply (Butler, 2011), assessment of the environmental practices or technologies that a firm should adopt (Bose & Luo, 2011; Dao et al., 2011; Watson et al., 2011; Zhang et al., 2011), and the consequences of such adoption (Bengtsson & Ågerfalk, 2011; DesAutels & Berthon, 2011).

Considering this variety of applications, we can broadly conceive of Green IS as “types of IS that assist individuals and organizations to become more environmentally sustainable” (Recker, 2016, p. 4477)—i.e., they focus on outcomes. Recker (2016) describes these outcomes in terms of environmentally sustainable work practices and decisions, and Seidel et al. (2013) identify sustainable practices and environmental sensemaking as outcomes. The Green IS discourse acknowledges that Green IS help organizations implement sustainable business processes (Watson et al., 2008; Watson et al., 2010).

Based on this discussion, we make two primary observations: Any IS can be a Green IS if it helps organizations accomplish environmental sustainability-related outcomes, and the key challenge from a design perspective is to extend the view from the ends—i.e., the outcome perspective—to the means, i.e., the material features that help organizations produce these outcomes. We argue that IS can accomplish the ends of improving the environmental performance of supply chains by combining several means—measurement and monitoring through capturing and analyzing data across the supply chain, making decisions regarding improvement measures, tracking the progress in environmental performance, identifying potential problems, and providing insight into future actions (Janssen et al., 2015; Lee & Wu, 2014; Qorri et al., 2018).

Since IS, in general, and ECMS, in particular, are rarely mentioned in academic papers on SSCs (Qorri et al., 2018), rigorous scholarly research is needed to explore their design and determine how and to what extent they can improve environmental sustainability in supply chains and logistics (Hoang et al., 2017).

## 2.3 Energy and Carbon Management Systems

ECMS are a type of environmental management information system (EMIS) (El Gayar & Fritz, 2006; Teuteberg & Straßenburg, 2009). EMIS are “organizational-technical systems for systematically obtaining, processing, and making available relevant environmental information in companies” (El Gayar & Fritz, 2006; p. 756). As a subcategory of EMIS, ECMS focus on energy consumption and carbon emissions. In what follows, we discuss the broader category of EMIS, given the limited research on ECMS.

The rich literature on EMIS resides in a fragmented landscape because of the lack of a clear definition and taxonomy. Our literature analysis identified several terms that refer to EMIS and fit the description that El Gayar and Fritz (2006) provide, including “environmental information systems” (Cherradi et al., 2017), “environmental ERP” (Melville, 2012), “environmental enterprise systems” (Hoang et al., 2016), “sustainable enterprise resource planning systems” (Chofreh et al., 2018), “energy information systems” (Effenberger & Hilbert, 2016), “energy management information systems” (Martirano et al., 2018), “energy management control systems” (Schulze et al., 2018), and “carbon management systems” (Corbett, 2013). Because of the interdisciplinary nature of EMIS research, which is based on scholarship from disciplines such as accounting, energy engineering, environmental informatics, IS, logistics, and industrial engineering, obtaining a complete map of the literature is challenging. We found a considerable amount of work on EMIS and the intricacies of energy measurement, as well as their architectural design, microgrids (e.g., Elkazaz et al., 2020; Mazidi et al., 2020; Whittle et al., 2020), and carbon accounting (e.g., Gibassier et al., 2020; Luo & Tang, 2016).

Following Malhotra et al.’s (2013) value space of research classification, we found that most of the studies belong to the design-oriented dimension (e.g., Bensch et al., 2015; Corbett, 2013), while the evaluation of the developed artifacts in actual cases falls into the category of impact-oriented research that uses action research or in vivo real-time approaches (e.g., Stindt, 2014). A few studies fit into the conceptual value space (e.g., Bensch et al., 2014; Effenberger & Hilbert, 2018; Guenther et al., 2016; Setiyoko et al., 2017; Teuteberg & Straßenburg, 2009)

and the analytic space, including case studies, ethnographic analyses, and quantitative empirical analyses (e.g., Hoang et al., 2016; Hoang et al., 2017; Leyh et al., 2014; Melville & Saldanha, 2013; Nishant et al., 2017). Most studies address the application of EMIS in a certain environment or industry, such as logistics (Hilpert et al., 2013b; Iacob et al., 2013), manufacturing (Bruton et al., 2018; Zampou et al., 2014b), higher education (Scholtz et al., 2016), or recycling processes (Schweiger, 2016).

The design science stream has produced several EMIS instantiations, including systems to assess the availability of critical raw materials (Bensch et al., 2014), assist ISO 50001 implementation in manufacturing (Bruton et al., 2018), support energyaware manufacturing (Zampou et al., 2014b), gather real-time data for products’ carbon footprints in transportation processes based on vehicles’ on-board systems and smartphones (Hilpert et al., 2011), report energy consumption and GHG emissions at the product level (Hilpert et al., 2013a), improve reverse logistics (Stindt, 2014), and track the GHG emissions of logistics processes (Hilpert et al., 2013b). Some EMIS instantiations focus on persuading employees to engage in ecologically responsible behaviors (Corbett, 2013; Kotsopoulos et al., 2018), or on enabling urban planning (Culshaw et al., 2006) and mobility tracking (Kugler et al., 2014), fostering sustainable decisionmaking in the energy sector (Nuss, 2015), and supporting vehicles’ end-of-life recycling processes (Schweiger, 2016). These studies suggest various EMIS and ECMS functionalities and system components, including data storage, validation, analytics, and reporting (Melville et al., 2017), or discuss process automation and integration with other systems (Hoang et al., 2017). However, the proposed design knowledge is often highly context specific and not at the level of design theory that one can apply across contexts and time.

Scholars also discuss the impact of EMIS on energy efficiency and carbon performance (e.g., Hoang et al., 2017; Schulze et al., 2018) and the factors associated with their adoption (e.g., Hoang et al., 2019; Melville & Saldanha, 2013). The extent of ECMS implementation is positively associated with a firm’s energy efficiency (Schulze et al., 2018), and an exploratory investigation of four case studies shows that these systems can improve the quality of environmental data, generate various reports with ease and at low cost, and reduce risk (Hoang et al., 2017). Beyond processing environmental information, ECMS also facilitate decision-making and knowledge creation related to energy consumption and environmental impacts, such as in reverse logistics (Stindt, 2014) and manufacturing operations (Böttcher & Müller, 2016).

## 3 Research Approach

We use a DSR approach to develop prescriptive knowledge and formulate the key components of a design theory (Gregor & Jones, 2007) for ECMS. We employ a staged process based on Peffers et al.’s (2007) incremental and iterative refinement approach. Moving through the phases of problem identification, identification of purpose and scope, design and development, and demonstration and evaluation, we adjust Peffers et al.’s original formulation in three ways. First, we formulate an initial version of a design theory for ECMS in the design and development phase; that is, we develop an abstract blueprint that includes key constructs and principles of form and function and then a concrete instantiation that is consistent with that blueprint and responds to the identified problem situation.

Then, considering that the artifact emerges from interaction with the organizational context, even when its initial design is guided by the intent of researchers, we use the key activities of ADR (Sein et al., 2011)—i.e., ongoing reflection activities throughout the phases, where a group of stakeholders involved in the design and implementation activities (e.g., practitioners, software engineers, researchers, end-users) give feedback before the final evaluation—and thereby attend to the theoretical, technical, and practical perspectives. This resembles Mullarkey and Hevner’s (2019) approach. Finally, we add a phase of reflection and formalization of learning that supports the generation of design theory (Mandviwalla, 2015; Sein et al., 2011). We formulate the design theory components based on reflection on the outcomes of the DSR process and subsequent formalization of key findings. Thus, we move conceptually from building a solution for a single instance of an ECMS to a solution for a broader class of problems (Sein et al., 2011).

We performed two rounds of a sequence of five phases over a period of 33 months. Figure 1 visualizes the iterations, describes the methods and outcomes, and highlights how we articulated the results in the form of a new IS design theory for ECMS. Figure 2 highlights the progress over time. The research team coordinated all DSR activities, from identifying and elucidating user requirements to ECMS design, demonstration, and evaluation.

We developed the ECMS artifacts in the context of two research projects on energy efficiency and carbon efficiency in manufacturing and in the supply chain.<sup>1</sup> The development team, consisting of people from seven information technology (IT) companies who have expertise in supply chain modeling tools, LCA tools, manufacturing systems, energy sensors, monitoring tools, and IT integration, also supported the DSR activities and especially the design, development, and demonstration of the ECMS artifact. The research team and the development team met regularly with the organizations representatives to present the progress at the various phases and to get early feedback on the developments.

![](/api/attachments/T4DC32W6/fulltext/images/26a568e07e6461bc5bc1904594edac4544e795e41bdf995ad2fe399daab3b617.jpg)  
Figure 1. Design Science Research Approach

e-SAVE: Energy Efficiency in the Supply Chain through Collaboration, Advanced Decision Support and Automatic Sensing (Project Number: 288585)

![](/api/attachments/T4DC32W6/fulltext/images/30f14b51a99fb7fb559478586434570de56d116fe3cc53e3c241f329b7f7a91f.jpg)  
Figure 2. Design Science Research Approach Gantt Chart

Table 1. Organizations

<table><tr><td>A</td><td>Organization A is an Italian medium-sized enterprise with 210 employees and a production of more than 700,000 meters of fabric per year. It is one of the oldest manufacturers in the textile industry and is interested in enhancing energy efficiency in manufacturing and collaboration with its suppliers.</td></tr><tr><td>B</td><td>Organization B is a clothing company with 735 employees in Germany and an annual turnover of 184 million euros. Another 2,000 people are employed in Eastern Europe for the manufacturing of garments. The company has 109 retail stores in 58 countries and more than 1,500 up-market fashion stores.</td></tr><tr><td>C</td><td>Organization C is a major Greek retailer with a supply chain consisting of a central warehouse and 94 stores. The central warehouse accommodates the products received from most of its more than 600 suppliers and distributes them to the stores using its own fleet of vehicles. Its internal mechanisms portray an environmentally aware enterprise. The organization has implemented environmentally friendly facilities, such as motion sensors operating the lighting in its warehouse and collaborative distribution processes to improve the company&#x27;s environmental performance.</td></tr><tr><td>D</td><td>Organization D is a multinational food manufacturer, one of the main suppliers in the FMCG sector, and has an environmentally aware profile. The organization has an extensive and complex supply chain network with a presence in Europe, North and South America, Asia, and Oceania. Its distribution network is vast, with partners in more than 100 countries. It has implemented several environmental practices over the years, including energy saving programs, LCA methods, environmental product declaration, business intelligence, and sustainable packaging in logistics.</td></tr></table>

To apply the DSR approach we adopted, we identified four organizations (Table 1) to:

1. cover end-to-end supply chains and capture the specificities of the manufacturing, warehousing, and distribution stages of the supply chain;

2. investigate the application of ECMS in industries with various environmental sustainability objectives—for example, the textile industry is cost driven, whereas the FMCG sector adopts a collaboration perspective to address consumers’ environmental concerns;

3. cover multiple contexts, each with its own implementation challenges in terms of, for instance, data quality and availability, data capturing and integration, and information sharing.

Next, we describe the key activities we carried out and provide an overview of key outcomes. For brevity, we do not present the intermediate results of the applied DSR process.

We grounded the problem identification in a review of studies on ECM and on practitioners’ environmental sustainability reports. We identified ECM requirements and challenges using a working group of corporate decision-makers responsible for supply chain management, environmental management, and reverse logistics. This group included nine companies’ supply chain/logistics managers or directors who met approximately monthly for seven months. We used these meetings and two semistructured interviews to ensure that we understood the companies’ specificities and sectorial challenges. We also had access to six months of distribution data provided by one grocery retailer and one food manufacturer, which helped us estimate energy consumption and carbon emissions and investigate the potential for difficulties related to data availability, quality, and granularity. This process allowed us to define the purpose and scope of ECMS and to elaborate on design and implementation issues related to data capture and integration, data quality and availability, definitions of energy and carbon performance metrics, collaboration, and information sharing.

To elucidate the purpose and scope and decide on a set of ECMS design requirements, we worked closely with the four organizations (Table 1), two of which also participated in the previous phase. We conducted semistructured interviews with their representatives and discussed the design requirements in several meetings over a period of five months. This data collection was supplemented by on-site observations at their factories, warehouses, distribution centers, etc. For each dimension (manufacturing, warehousing, distribution, and supply chain), we included the respective ECM KPIs and hierarchies, as well as the data necessary for their calculation. We translated the end users’ views into six ECMS design requirements that we aligned with those described in Melville et al. (2017) and validated them using information from existing artifacts (Mandviwalla, 2015), a process that allowed us to develop the “design requirements and justificatory knowledge” theory component.

In the design and development phase, we derived a set of key ECMS constructs in terms of (1) the information flows related to key data types required for ECM, and (2) system components. We then identified initial principles of form and function and incorporated those constructs to guide the artifact’s design and development. With the support of the development team, we then translated these principles into technology features. During this phase, the research and development team met regularly to monitor the development process. By reflecting on the outcomes of this phase, we refined the initial constructs, the principles of form and function, and the expository instantiation.

For the purpose of demonstration and evaluation, we performed an ex post naturalistic evaluation (Venable et al., 2012) by deploying the artifacts in the four organizations to establish proof of concept and proof of value (Nunamaker et al., 2015). We applied an observational design evaluation using a field study approach (Pries-Heje et al., 2008; Venable et al., 2012) in both rounds and descriptive methods in the form of scenarios in the second round. The first round of demonstration and evaluation focused on validating the design theory and investigating its design and implementation challenges and feasibility regarding, for instance, data availability and granularity. We also consolidated our proof of concept and proof of value in the second round by assessing the ECMS utility that the organizations perceived and by collecting evidence on how the ECMS theory instantiation yielded an ECMS implementation that supported ECM and environmentally aware decision-making and practice.

As part of the field study, and with the active support and involvement of the development team, we deployed, demonstrated, and evaluated artifacts based on the suggested ECMS design theory at the four organizations. The development team installed several hardware elements like energy sensors and developed interfaces to capture or retrieve energy and fuel consumption data from legacy systems, such as material requirements planning (MRP), manufacturing execution systems (MES), enterprise resource planning (ERP), and warehouse management systems (WMS). Daily transactional data were obtained from these systems and were uploaded to the ECMS for a period of twelve months in the first round and five months in the second.

The design and implementation challenges were analyzed and identified in the first round by the first and the second author (who have expertise in IS design, Green IS, and supply chain management), the third author (who has expertise in manufacturing operations), end users, and domain experts from the development team. Constructs were revised where necessary before initiating the second round of demonstration and evaluation. Workshops with end users at the four organizations allowed the research team to assess the artifact instantiation’s utility in the second round. The group of fourteen end users consisted of three high-level directors in the areas of supply chain, environmental sustainability, and customer service; six mid-level managers from supply chain and logistics to production; a research director; and four IT directors and integrators. Thus, this group included decision makers and IT facilitators who represented all four elements of the ECMS scope and were sufficiently heterogeneous for our purposes. Tables A1 and A2 in the Appendix depict additional details about this group for the sake of transparency and reproducibility. We revised the design theory—specifically, the ECMS information flows, components, and design principles—only after the demonstration and evaluation phases of the first and second rounds.

## 4 Initial ECMS Design Theory

## 4.1 Purpose and Scope

All managers and directors involved in the working group recognized the ECMS core aims in terms of cost reduction, operational improvement, and response to regulatory and consumer requests for more environmentally sustainable solutions. Eight of the nine companies that participated in the working group did not have energy monitoring systems in place and identified the lack of environmental information as a critical barrier to the development and implementation of SSC practices. These companies recognized the need to collect more detailed environmental information (e.g., per day or per route), integrate this information into supply chain processes (e.g., routing and inventory management), and present it in combination with traditional supply chain performance indicators (e.g., vehicle fill rates, inventory levels) to make their decision processes more environmentally aware. Monitoring environmental performance indicators like energy consumption and carbon emissions in the supply chain context remains costly and time-consuming.

To meet these needs, the scope of an ECMS in the supply chain context should involve various dimensions of monitoring, reporting, and decision support while also addressing all stakeholders (Ahi & Searcy, 2015). We adapted Ahi and Searcy’s (2015) conceptual framework for measuring performance in green supply chains to define the key stakeholders in an SSC: the supplier, the manufacturer, the distributor, the retailer, and the customer (Figure 3). We omitted end-of-life management stakeholders like recyclers, reusers, and disposers since reverse logistics is not in the scope of this study.

This study addresses three main types of activity types: (1) manufacturing activities related to the production of raw materials, semifinished goods, or finished goods; (2) warehousing activities related to the storage and handling of raw and packaging materials at the source or semifinished or finished goods at the destination markets; and (3) inbound and outbound transportation activities across all modes of transportation, including road, rail, sea, inland waterways, and multimodal transportation. Thus, the supply chain context includes manufacturing but moves significantly beyond it (Figure 3).

Single and aggregated measurements can only partially satisfy regulatory and consumer requirements and cannot deliver operational improvements or shed light on the strategic aspects of SSCs. For example, organizations can use annual energy consumption and carbon emission data in annual corporate social responsibility reports, but these data do not support decision-making at the process level for routing or replenishment decisions, for example. To support such decisions, more detailed data, such as fuel consumption per vehicle, would need to be entered into an ECMS.

Effective SSC management requires that sustainability indicators be associated with traditional operational indicators (Bai et al., 2012; Maas et al., 2016). Three types of KPIs must be considered: environmental KPIs, including distinct energy consumption and carbon KPIs like total energy consumption, total $\mathrm { C O } _ { 2 }$ emissions, energy efficiency, and $\mathrm { C O } _ { 2 }$ efficiency; operational KPIs like average number of products stored and service level; and integrated KPIs like inventory and transport $\mathrm { C O } _ { 2 }$ efficiency that combine environmental and operational efficiency (Zampou et al., 2014a). These KPIs must be estimated at multiple levels of granularity, such as total energy consumption at the process or machine level. Therefore, we need a hierarchy to estimate KPIs at an overall level and then to decompose them into finer levels for certain nodes and processes.

Because a hierarchical representation presents supply chains as being comprised of manufacturing, warehousing, and logistics nodes, as well as the links among them (Jain et al., 2013), we employ a hierarchy of physical components, i.e., facilities, stores, warehouses, vehicles, and machines as well as processes, i.e., production, warehousing, and distribution. That is, our hierarchy puts the processes of manufacturing, distribution, warehousing, and supply chains (Table 2) at the top level and decomposes each process into the machine (manufacturing), store section (warehousing and supply chain), and vehicle (distribution and supply chain) components. It then adds the product category and the product level to monitor products’ lifecycles across processes (Figure 4).

In summary, we suggest that the scope of an ECMS in the supply chain context should address the key stakeholders in the supply chain (Figure $_ { 3 ) ; }$ consider the key supply chain activities of manufacturing, warehousing, distribution, and the overall supply chain (Table 2); and include the dimensions and hierarchies of monitoring, reporting, and decision support (Figure 4). The ECMS purpose and scope is to support the key stakeholders in calculating their environmental performance for the type of activity they perform (the ECMS intrafirm scope) and support environmental performance calculation at the interface between two successive stakeholders of a supply chain and their activities (the ECMS supply chain scope). The overall goal is to support tracing the environmental impact “from cradle to grave.” For example, a distributor sells products via a retailer to an end customer, and both the distributor and the retailer track the environmental product performance up to the customer. Each of them implements an ECMS instantiation to calculate the product’s environmental burden in their scope. Then, the retailer collects environmental product data from the distributor and adds the environmental burden of its own activities.

The end users in the four organizations also envisioned that ECMS would support them in integrating energy and carbon indicators into their operational decisions. Specifically, Organizations A and B sought processes to:

• optimize energy-aware scheduling in various stages of textile production, particularly those with a considerable energy burden, such as the finishing mill;

trade energy and carbon permits—i.e., exchange energy contracts and carbon permits among supply chain partners or with an external energy provider.

![](/api/attachments/T4DC32W6/fulltext/images/de599d2be5b138193512f57942149452e6248e0a318277dc03791cafb43626ad.jpg)  
Figure 3. The Scope of ECMS in the Supply Chain (figure designed using resources from Flaticon.com)

![](/api/attachments/T4DC32W6/fulltext/images/2e8fa7e6906963c3aba5f1730aea60bb2742c62e6a024b7a3a6ff406a3a4c1b0.jpg)  
Figure 4. ECMS Supply Chain Hierarchy

Table 2. The Purpose and Scope of ECMS

<table><tr><td>ECMS scope</td><td>ECMS purpose</td></tr><tr><td>Manufacturing</td><td>Track energy consumption to quantify potential savings related to manufacturing processes and to improve the performance of their ECM. Track the energy consumption of production machines, which are responsible for the greatest part of energy consumption. Measure indirect energy consumed by activities that are not directly involved in product manufacturing, such as lighting, cooling/heating, and ventilation.</td></tr><tr><td>Warehousing</td><td>Track energy consumption and quantify potential savings related to specific nodes of the supply chain (e.g., warehouse, store) and energy-greedy infrastructures like refrigerators and lighting. Use power supply meters in combination with sensors.</td></tr><tr><td>Distribution</td><td>Track vehicles&#x27; fuel consumption to control and improve distribution processes&#x27; environmental impacts. Collect fuel consumption data and integrate them with traditional indicators like vehicle fill rate, distance traveled, and weight distributed.</td></tr><tr><td>Supply chain</td><td>Measure the energy consumption and carbon emissions across the supply chain, combining the two previous views of warehousing and distribution, collecting data from various organizations (3PLs, retailers, suppliers), and supporting decisions that impact the sustainability performance and choices of supply chains.</td></tr></table>

For their part, Organizations C and D sought processes to:

redesign their supply chain networks—i.e., generate “what if” scenarios of redesign decisions (e.g., whether to add a new warehouse or store or merge two warehouses) based on environmental performance and evaluation through simulation;

promote and distribute packaging redesign—i.e., collaborate on assessments of the environmental impact of various possibilities for retail-ready packaging, particularly ways that consumer units can be bundled into a single package for suppliers and retailers to deliver to points of sales;

create collaborative ordering and replenishment practices to assess policies such as changing replenishment frequencies and safety stock levels in terms of cost, efficiency, and environmental impact;

• collaborate on distribution practices like backhauling;

inform consumers about a product’s environmental profile and examine the impact of providing this information on consumers’ attitudes and buying behavior.

## 4.2 Design Requirements and Justificatory Knowledge

We identified four key aspects of ECM that guided the formulation of the design requirements:

1. Data capture and integration: Collecting the required types of data from heterogeneous sources and various systems is challenging because the traditional IS used in supply chain management, such as ERP, WMS, MES, and routing systems, do not typically capture environmental data like energy or fuel consumption. The current state is characterized by a lack of automated reporting of key energy data since energy consumption data could be collected either by energy sensors or from building management systems (BMS) and fuel consumption monitoring systems. In the current state, ECMS also must be integrated into existing systems to retrieve supply chain data.

2. Data quality and availability: ECM is a dataintensive process, and companies cannot easily meet the data requirements by means of their existing infrastructures. Even when data are available, they may not cover the level of detail required to enable ECM. For example, we may miss data regarding energy consumption at the machine level. Poor data quality, such as incorrect inventory levels, is another obstacle.

3. Energy and carbon performance metrics: Selecting the appropriate energy and carbon performance metrics is a challenge because of the lack of established measurement frameworks and the lack of a holistic approach to measuring energy consumption and carbon emissions. Defining metrics ensures the comparability of the results. For example, if the manufacturer of a product relies on industry averages to calculate its carbon emissions and the manufacturer of another product in the same product category relies on actual measurements of carbon emissions, their respective metrics may not be comparable.

4. Collaboration and information sharing: Expanding ECM beyond a firm’s boundaries poses additional challenges related to collaboration, information sharing, and coordination. Standardizing the rules for data collection and collaboration facilitates data exchange throughout the supply chain and the implementation of energy consumption and carbon measurement.

Existing studies support these four key elements, as highlighted in reviews that address fifteen years of work on SSC management and its measurement (Ansari & Kant, 2017; Janssen et al., 2015; Tuni et al., 2018). An ECMS should be able to address these aspects of ECM by supporting firms in their efforts to standardize, monitor, capture, use, and interpret data and diffuse information. In alignment with what has already been suggested, data storage, validation, analytics, and reporting are key components of ECMS (Melville et al., 2017). We propose a set of essential rather than exhaustive design requirements, as shown in Table 3.

The “integration of data flows” requirement (DR2) constitutes the core of an ECMS design. ECM is information intensive, and ECMS must present information in forms that address the varying specificities of scope and factors like time, product, and physical unit (e.g., store, warehouse, vehicle, route, production order, machine). The design of ECMS requires combining various data sources and information flows. Objects such as machines and vehicles that can sense and report energy data are sources of energy information that must be clearly defined and combined (Watson et al., 2010; Zampou et al., 2014b).

## 4.3 Constructs and Principles of Form and Function

We build our design theory based on two types of constructs: information flows of the categories of data required for ECM, and system components for collecting, processing, and disseminating such data.

Table 3. ECMS Design Requirements

<table><tr><td>Design requirement</td><td>Description</td></tr><tr><td>DR1: Data collection and storage</td><td>Collecting energy consumption, fuel consumption, operational, and delivery data</td></tr><tr><td>DR2: Integration of data flows</td><td>Integrating energy consumption information from, for example, energy monitoring systems, into supply chain and product information from MRP, ERP, and WMS; integrating emission factors from governmental or institutional sources</td></tr><tr><td>DR3: Data validation</td><td>Validating and cleansing data</td></tr><tr><td>DR4: Supply chain monitoring and interorganizational coordination</td><td>Monitoring and supervising the various supply chain processes, supporting information sharing, and coordinating various supply chain partners</td></tr><tr><td>DR5: Environmental performance/impact estimation</td><td>Calculating energy consumption and carbon emissions and allocating the environmental impacts at various levels of analysis, such as the process and warehouse levels</td></tr><tr><td>DR6: Environmental reporting</td><td>Reporting the required KPIs in various formats and visualizations to comply with environmental standards and reporting initiatives</td></tr></table>

Information sharing and coordination in the supply chain require transactional information to coordinate the physical demand and supply chain, contextual information to ensure that the different organizations interpret data in the same way, and interorganizational product information to facilitate cross-company coordination (Legner & Schemm, 2008). Building on this conceptualization, we suggest four information flows (Table 4). The energy information flow and the product-environmental information flow are new types of flows, derived from the need to collect and analyze data related to energy and fuel consumption in the context of ECM and the need to calculate the total carbon emissions associated with a product during its life cycle.

We propose the energy information flow as a distinct information flow to highlight the difference between ECMS and existing supply chain management information flows, as Legner and Schemm (2008) suggest, and we highlight the need to collect energy and fuel consumption data in addition to traditional supply chain data like inventories and routes. Energy and fuel consumption data are not stored in the traditional supply chain management systems, although in some cases they may be imposed by energy bills or fuel consumption invoices in a company’s ERP. Thus, they should be treated differently, either by collecting them from different sources or by calculating them.

The product environmental information flow addresses consumers’ demand for sustainable products and the need for manufacturers and suppliers to provide the environmental profiles of their products. ECMS support the calculation of these environmental profiles, but hidden carbon emissions may be inherited from, for example, raw material production. Therefore, the product environmental information flow and respective data can be provided by, for instance, suppliers of raw materials life cycle inventories (LCIs). We also categorize the product environmental information flow as a distinct information flow to highlight the need to treat it differently, either by collecting this data from other sources or by calculating the data.

We define the data entities that each of these information flows comprise. The data related to energy information flows may not only relate to environmental objectives but also to improvements in traditional operations or cost reductions and even to trade-offs between environmental and cost-reduction targets. Table 5 lists definitions for each system component, including their primary functional objectives and their association with the design requirements. Our design builds on the idea of combining data sources and elaborating on the effective integration of the information flows.

Figure 5 visualizes the architecture based on the five system components—data collection, energy monitoring, supply chain coordination, ECMS workflow engine, and reporting—and their interrelationships in terms of information flows. The architecture supports data collection, integrates the various information flows, calculates the respective KPIs (energy monitoring, supply chain coordination, and ECMS workflow engine), and visualizes the ECMS outcomes (reporting).

The data collection system component collects the various types of data from existing systems and infrastructures—such as ERP, WMS, BMS, LCI repositories, and energy sensors—and handles all information flows. ECMS should collect data from heterogeneous data sources; firms in the manufacturing industry must often supplement energy data with additional energy consumption data, such as data collected through energy audit processes.

Table 4. Constructs: ECM Information Flows

<table><tr><td>Information flow</td><td>Description</td></tr><tr><td>Transactional information flow</td><td>Transactions that take place in the supply chain, such as ordering, distribution, inventory management, and production</td></tr><tr><td>Contextual information flow</td><td>Products, facilities, processes, and supply chain partnerships that support the interpretability of transactional information</td></tr><tr><td>Energy information flow</td><td>Energy consumption in warehouses that is either measured by energy sensors or retrieved from existing BMSFuel consumption, referring to vehicle fuel refills or to actual fuel consumption monitored through metering devices installed on vehicles, and possibly data from governmental agencies or standardization initiatives (e.g., emission factors)</td></tr><tr><td>Product environmental information flow</td><td>Environmental profile of products, including products’ embodied carbon footprints as recorded by other supply chain partners or LCIs</td></tr></table>

Table 5. Constructs: ECMS System Components

<table><tr><td>System components</td><td>Description</td><td>DRs</td></tr><tr><td>Data collection</td><td>System components for collecting, validating, cleansing, and identifying the relations among all the data received from various sources. The data collection component consists of two separate subcomponents that function independently: the energy data layer and the operational data layer. The first handles the communication and synchronization with energy sensors and BMS. The second imports data from ERP, WMS, and other corporate systems. Thus, this component handles all information flows for monitoring activities.</td><td>DR1, DR3</td></tr><tr><td>Energy monitoring</td><td>The system&#x27;s mechanism for aggregating and reporting energy consumption data at different levels of analysis, such as energy consumption per node/section. It addresses the mandate for such reporting by retrieving energy consumption data from the energy data layer and uses all energy consumption flows that are not recorded by sensors provided by the operational data layer, such as energy bills and energy audits. Overall, this component supports sensor energy monitoring and non-sensor energy monitoring. It handles the energy information flow and the contextual information flow by associating energy power meters or energy consumption to specific machines, processes, and infrastructures.</td><td>DR2, DR5</td></tr><tr><td>Supply chain coordination</td><td>System components for coordinating the supply chain, maintaining the collaborative relationships between supply chain partners, and facilitating data exchanges. They provide all the required information regarding the objects of interest, such as nodes, products, and partner details. Moreover, they support modeling of the supply chain structure to maintain and disseminate semantic information regarding an organization&#x27;s underlying structure (e.g., facilities, departments), the production arrangement (e.g., processes, process steps), warehousing, the composition of a product, and so on. They also coordinate the collection of external data and handle the contextual information flow.</td><td>DR4</td></tr><tr><td>ECMS workflow engine</td><td>System components for monitoring the daily supply chain processes (e.g., warehousing, ordering, distribution, production) and for supporting estimation of the energy consumption and carbon footprint indicators. The workflow engine also handles information from other supply chain partners, thus handling all flows. It is the key component in materializing the ECM daily calculations, so it also includes the application programming interfaces (APIs) of standardization bodies and initiatives regarding emission factors and environmental profiling of processes.</td><td>DR2, DR5</td></tr><tr><td>Reporting</td><td>The system component facilitating the creation of formatted standard reports that cover the various aspects of ECM in the supply chain and compliance with standards like ISO 14000 series and GRI.</td><td>DR6</td></tr></table>

![](/api/attachments/T4DC32W6/fulltext/images/d808003033e6dc71bca86f443a497bf71bfd3ef25ff4715bd01c2bf7de3ec559.jpg)  
Figure 5. ECMS Constructs: System Components and Information Flows

Table 6. ECMS Design Principles<sup>2</sup>

<table><tr><td>Key component</td><td>Design principles</td></tr><tr><td>Data collection</td><td>DP1.1 Provide features for collecting and cleansing energy and operational data so that the system affords the ability to process energy and operational data.</td></tr><tr><td>Energy monitoring</td><td>DP2.1 Provide features for assigning sensors to specific machines and processes; for collecting, processing, and storing energy sensor consumption data, and for calculating energy values per time interval so that the system affords the ability to monitor energy sensors.DP2.2 Provide features for identifying, collecting, and processing energy secondary data so that the system affords the ability to monitor non-sensor energy consumption.</td></tr><tr><td>Supply chain coordination</td><td>DP3.1 Provide features that enable data exchange among supply chain partners by using data privacy and security protocols and applying standards for information sharing so that the system affords the ability to coordinate across the supply chain.DP3.2 Provide features for modeling organizations&#x27; structure, production, and supply chain processes and supporting their decomposition into the required levels of analysis so that the system affords the ability to coordinate across the supply chain.</td></tr><tr><td>ECMS workflow engine</td><td>DP4.1 Provide features for combining data from various sources of the daily operational activities across the supply chain (e.g., shipments, inventories, production), including emission factors and relevant data from governmental databases so that the system affords the ability to monitor the supply chain end to end and coordinate information flows.DP4.2 Provide features for calculating KPIs at various levels of analysis so that the system affords the ability to monitor the supply chain end to end and coordinate information flows.</td></tr><tr><td>Reporting</td><td>DP5.1 Provide features for reporting on the organizational, supply chain, and production process structures so that the system affords the ability to inform users about the scope of ECM.DP5.2 Provide features for reporting on the ECMS purpose and scope, hierarchies, and KPIs and complying with environmental standards and reporting initiatives so that the system affords the ability to inform end users about measurements of ECM</td></tr></table>

The energy monitoring system component processes the energy information flow and assigns energy consumption to low-level supply chain processes (contextual information flow) to derive KPIs like energy consumption per sensor, per machine, and per section. Because secondary energy consumption data collected through energy audit processes is kept in spreadsheet-like applications, this system component also supports non-sensor energy monitoring. Applying ECM across the supply chain and extending its scope outside a single firm’s boundaries requires handling and designing different supply chain networks and managing the relationships with external partners, which demands a system component that models supply chain processes and allows various participants to access shared data and shared functionality. Therefore, the supply chain coordination system component handles contextual information flows, while an ECMS workflow engine system component materializes ECM in the appropriate purpose and scope and calculates the various KPIs by managing all four information flows. The reporting system component presents the KPI calculation results derived by the ECMS workflow engine component.

We use these system components to formulate principles of form and function. Table 6 presents the design principles, i.e., the design theory’s principles of form and function, each of which is related to a key system component, drawing on the “anatomy of a design principle” suggested by Gregor et al. (2020). Structurally similar formulations of the relationship between material features of information technologies and their outcomes can be found in, for instance, Seidel et al. (2018).

## 4.4 ECMS Expository Instantiation

We developed four instantiations of the ECMS, two covering the manufacturing dimension and two covering the warehousing, distribution, and supply chain dimensions. Figure 6 presents a screenshot of the manufacturing instantiation that calculates energy consumption at the level of production processes. Figure 7 displays the energy consumption trend and KPIs like CO<sub>2</sub>, products distributed, and the transport efficiency of various distribution networks as an example of the instantiation developed for the warehousing and distribution companies, Organizations C and D.

The instantiations implement the key constructs of our theory and differ only in terms of details related to the different implementation and deployment contexts. For example, the data collection system component manages various kinds of data for each case, thus yielding different XML schemas and data interfaces. Similarly, the energy measurement and carbon allocation methodologies differ because the allocation unit in textile manufacturing is one square meter of the produced article, while in the two FMCG companies it is a unit of volume or weight of distributed products. Calculating the indirect energy in manufacturing imposes another context-related differentiation. All principles except DP2.2 and DP3.1 were implemented in all instantiations. DP2.2 was implemented only for manufacturing, where secondary energy data from energy audits had to be collected, and DP3.1 was required only in the warehousing and distribution instantiations.

Overall, the structural similarities of the four instantiations suggest that the proposed design is sufficiently generic to cover the requirements of a broad range of ECMS. However, the four organizations also provided challenges related to data quality and availability, data capture and integration, energy and carbon performance metrics, and collaboration and information sharing that we considered in the specific implementations (Table 7). We adapted the generic blueprint to the idiosyncratic requirements of each case while remaining faithful to the general abstract design principles. Thus, we translated the design principles into concrete focal features of the artifact features by focusing on the features we needed to instantiate the design theory (Lukyanenko & Parsons, 2020).

Several interfaces were developed to capture or retrieve energy and fuel data from already installed systems like energy capturing infrastructure, BMS, or legacy systems. Moreover, energy sensors were installed in three of Organization C’s stores to capture actual energy consumption and in Organization A to monitor the energy consumption of selected machines. The transactional and contextual data specified were extracted as a consolidated daily batch from MRP, MES, ERP, and WMS systems.

## 5 Implementation, Demonstration, and Evaluation

This phase focused on validating and refining the initially formulated design theory through two rounds of demonstration and evaluation. The first round of this phase identified design and implementation challenges while the second round had the objective of validating the extent to which our theory helps implement ECMS that support energy consumption and carbon measurements and facilitate environmentally aware decision-making and practice. We highlight how we refined the constructs and design principles between the two rounds mainly by introducing a new construct—the carbon footprint estimator—and a set of new principles, and also provide proof-of-value evidence regarding ECMS.

![](/api/attachments/T4DC32W6/fulltext/images/72ad1823c21fd91ae28fe599c3d5ae0fdf8c88d44769de8e2719869bb93e804b.jpg)  
Figure 6. ECMS Manufacturing Instantiation

![](/api/attachments/T4DC32W6/fulltext/images/4e31cb825e87303e2da329e7271b9864ff234b4506ce7108b8486d8a1ba05d4b.jpg)  
Figure 7. ECMS Warehousing and Distribution Case Instantiation

Table 7. Settings at the Instantiation per Organization

<table><tr><td>Organization</td><td>Energy consumption data availability</td><td>Fuel consumption data availability</td><td>Transactional and contextual data availability</td><td>Data exchange mechanisms</td></tr><tr><td>A</td><td>Limited data from energy audits and a small number of sensors</td><td>Not applicable</td><td>MES keeps daily data about production processes, and ERP stores orders data</td><td>Not applicable</td></tr><tr><td>B</td><td>Data from energy audits and real-time sensor monitoring</td><td>Not applicable</td><td>ERP and MES keeps data on production processes and ordering</td><td>Not applicable</td></tr><tr><td>C</td><td>Real-time energy monitoring via BMS at one store and monthly energy bills for all other stores</td><td>Actual vehicle refills available in ERP</td><td>WMS keeps daily data on warehousing transactions like orders and inventories), and distribution processes data are kept in ERP</td><td>Already installed for other cases</td></tr><tr><td>D</td><td>Energy sensors with no interoperable APIs that could not be integrated into ECMS</td><td>Not available because an external 3PL provider is used</td><td>ERP stores data about warehousing transactions like ordering; no data on distribution because an external 3PL provider is used</td><td>No such mechanisms installed</td></tr></table>

## 5.1 Settings for Artifact Demonstration and Evaluation

We deployed, demonstrated, and evaluated the ECMS theory and artifacts at the four organizations’ sites to cover the key dimensions of ECMS (Figure 4). We obtained daily transactional data from the respective MRP, MES, ERP, and WMS systems and uploaded them to the ECMS for a period of twelve months in the first round and five months in the second. We retrieved contextual information such as product categories and production processes once during the initialization phase and again when updates were required.

ECM for manufacturing: For Organization A, we focused on the processes of weaving, dyeing, and finishing, which use the most energy-consuming machines. Energy audits were used as a systematic procedure to clarify the processes’ energy consumption profiles, and energy sensors were installed to monitor the machines’ energy consumption. We also examined machines like the steam boiler, air filtering, and lighting machines to measure the indirect energy consumption. We measured each department’s consumption of indirect energy over a period and multiplied it by the working time of that department. Then we could accumulate the direct and indirect energy per product into a single value. For Organization B, extensive data on energy consumption were available from both energy audits and real-time sensor monitoring, but these were used only to analyze the energy consumption that accrued over months or years, so it was not feasible to map them to individual products.

ECM for warehousing: This configuration captured the energy consumption and carbon emissions of individual nodes in a supply chain. For Organization C, we selected the retailer’s central warehouse and three stores as representing different environmental profiles—a store with old infrastructure, one with conventional infrastructure, and one with new, environmentally friendly infrastructure. Energy sensors were installed in various nodes and processes.

ECM for distribution activities: We selected two distribution networks—the retailer’s distribution network, which connects the central warehouse to all of the stores served by the retailer’s own fleet (Organization C), and the supplier’s distribution network, which connects the central warehouse to every delivery point served by a third-party logistics company (Organization D). In Organization C, the retailer could provide all required transactional and contextual data. Even though actual fuel consumption was not available, the vehicle fuel refills were available, allowing the average fuel consumption per vehicle and route to be estimated. In Organization D, since actual fuel consumption data were not available, we used the industrial average of fuel consumption.

ECM across the supply chain: We also captured energy information and carbon information across the supply chain, from suppliers’ warehouses to retail stores (Organizations C and D). Synchronizing contextual information like the volume and weight of products and boxes was critical to our ability to calculate carbon emissions per product.

## 5.2 Round 1: Reflection and Refinements on the Components of Design Theory

Here we discuss the four key categories of the findings that surfaced during this round, which led to a revised set of constructs and design principles. We also elaborate on the key findings per category and provide examples.

First, in the category of data quality and availability, we identified limited environmental data availability, poor data quality, and data inconsistencies at all four sites. For example, Organizations A and D kept mainly aggregated information about energy consumption per month based on their electricity bills, while Organization B manually recorded it via physical audits. The fuel consumption data availability in Organizations C and D was even more limited. Transactional information related to inventories and deliveries was of poor quality. For example, we identified negative inventory values in Organization C and inaccurate packaging details in terms of product weight, along with a lack of delivery routes in Organizations C and D. The manufacturing organizations, Organizations A and B, could not meet the requirement for detailed time-dependent information regarding production processes. Moreover, we found inconsistencies and difficulties in transforming data into comparable terms, as Organizations A and B used varying measurement units, such as meters for fabrics and items for garments. Organizations C and D usually expressed vehicle capacity in terms of the number of pallets and stores’ transportation requests in terms of product items and quantities.

Regarding the category of data capture and integration, we identified integration issues with existing systems, limited automation of data retrieval mechanisms, varying data granularity levels, and complexity in integrating information flows at all four sites. In Organizations C and D, we also found dependencies and coordination problems related to aligning the inputs from supply chain partners, and in Organizations A and B, we discovered issues with tracking the workflow because of time-dependent data and the presence of semifinished products in manufacturing. Integration with existing WMS (Organizations A and B), BMS (Organization C), and energy sensors (Organizations B and D) was a demanding process that required the development of interfaces and mechanisms to retrieve energy and operational data continuously and to receive the energy and fuel consumption data that were previously recorded at intervals other than daily by spreadsheetlike solutions in Organizations A and D. The organizations kept these data at various granularity levels. For example, in Organizations A and B, energy sensors were sometimes linked with a group of machines instead of individual machines, meaning that they did not support the direct allocation of energy consumption to process steps and articles.

In the category of energy and carbon performance metrics, we found a lack of standardized and comparable energy, carbon, traditional, and integrated performance indicators. An extended list that included energy performance indicators covering both direct and indirect energy, carbon-related performance indicators, integrated indicators that incorporated both environmental and operational aspects, and indicators that referred to both processes and products were required in all cases. Comparability of the various carbon performance indicators across the supply chain in Organizations C and D was another major challenge because of diversity in the calculation methods that the various partners used.

Finally, concerns related to collaboration and information sharing included partners’ reluctance to share the extended set of required data because of their concern that suppliers could use their environmental information as part of their selection process. Therefore, establishing clear collaboration rules related to information sharing was an important implementation issue. Previous collaboration, mutual trust, and established information sharing processes were important facilitators of ECMS implementation in Organizations C and D.

These challenges and insights allowed us to reflect on the emergent design theory and derive refinements. The demonstration’s findings related mainly to data and technical issues; therefore, we did not revise our design theory’s purpose or scope or the design requirements.

## 5.2.1 Revised Constructs

Because our demonstration highlighted the complexity of estimating carbon emissions, we introduced a new construct called the carbon footprint estimator to represent the system components that encapsulate the logic behind the respective calculations and that decouple them from the ECMS workflow engine. This construct incorporates the business logic for aggregating and disaggregating energy consumption at various levels of analysis, transforms this data into carbon emissions, and then estimates the total carbon footprint. It nests methodologies like the LCA and standards like the GHG Protocol (2011) and translates the energy consumption estimations and carbon emission calculations specified in the KPIs.

The carbon footprint estimator system component computes the carbon emissions of the activities involved in manufacturing, warehousing, and distribution across a supply chain at different levels; allocates these activities’ carbon emissions to products; and provides carbon emissions, emission factors, and environmental parameters to other components when needed. Selecting the appropriate emission factors from LCI databases like the ecoinvent database (ecoinvent, 2019) or from the International Reference Life Cycle Data System (European Commission, 2018) is a prerequisite for calculating carbon footprints. One can add “custom” emission factors that LCA specialists have derived as configuration parameters or calculate them using actual data like emission coefficients based on a particular vehicle’s fuel consumption over a particular period, rather than coefficients of average emissions.

In summary, the carbon footprint estimator system component implements an LCA methodology and reports the carbon emissions according to the GHG Protocol Scope 3 standard (GHGProtocol, 2011) as follows:

1. Scope 1 emissions: direct emissions from owned or controlled sources, such as emissions that occur physically at the warehouse or store

2. Scope 2 emissions: indirect emissions from the generation of purchased energy that the company consumes, or emissions associated with the warehouse’s infrastructure and equipment and the packaging materials used

3. Scope 3 emissions: all other indirect emissions that occur in a company’s value chain, including both upstream and downstream activities, such as the emissions of a vehicle owned by a thirdparty logistics company when transportation is outsourced

The carbon footprint estimator can compute the carbon emissions daily or on request from the ECMS workflow engine by using energy and fuel consumption data and details about manufacturing, warehousing, and transportation activities. For example, it computes distribution activities’ carbon emissions per route using the type of vehicle, the fuel consumption and/or load weight per route, and the length of the route. In the case of warehousing, it estimates carbon emissions from the list of dates/section IDs, electricity consumption per section per day, the type of section, the section area, and the section volume.

Once the computation of carbon emissions from activities has been completed, the carbon footprint estimator can allocate these emissions to certain products, which requires allocation parameters like volume and mass and is time dependent. For example, if a product has been in a certain location (e.g., in a refrigerator) during a certain period, the carbon footprint estimator can allocate to the product part of the refrigerator-related emissions during that period because they can be directly related to the product’s conservation. Thus, the total emissions of a refrigerator during a well-defined time period can be uniformly allocated to all the products it contained during the same period.

To conclude, an independent system component must incorporate the carbon estimation and allocation logic to give the user the ability to set its parameters. This component receives all information flows as input from the ECMS workflow engine component that is responsible for coordinating ECM calculations and conducting carbon estimations and allocations. The ECMS workflow engine then aggregates the KPIs at the level of analysis requested. For example, it could calculate the sum of three stores’ carbon emissions for a week and feed their comparisons into the reporting component. Figure 8 presents our revised architecture.

## 5.2.2 Revised Design Principles

Principles related to the data collection component: Because of environmental data’s limited availability, ECMS require mechanisms that derive these data, either by using existing transactional data, such as calculating fuel consumption based on invoices or by using industrial averages related to vehicle fuel consumption. Based on these findings, we derived the new design principle DP1.2 as follows:

DP1.2 (new): Provide features for generating missing environmental data so that the system affords the ability to process energy data given a company’s levels of data availability and quality.

To address poor data quality and data inconsistencies, we employed a data cleansing process and corrected product weights (Organizations C and D) in collaboration with the end users. We estimated missing weights or volumes of product categories using secondary data from other sources. To derive the actual delivery route in cases where only deliveries but not actual routes were available, we created pseudo-routes using the distances between delivery points (Organization D). For Organizations A and B, where we could not retrieve article step sequences and times from the existing systems, we developed time profiles of the different articles, process steps, and processes. To express two metrics in compatible terms, we constructed dedicated approaches to translate, for instance, the required products into the number of fully loaded pallets. Based on these findings, we derived the new design principle DP1.3 as follows:

DP1.3. (new): Provide features for generating missing operational and transactional data and transforming existing data into a compatible format so that the system affords the ability to process operational and transactional data, given a company’s levels of data quality and inconsistency.

Principles related to the energy monitoring component: DP2.2 is related to non-sensor energy monitoring on the requirements elicited from the manufacturing organizations. However, this design principle is also relevant to the warehousing and distribution organizations, where ECMS must use energy consumption bills or the fuel refills kept in invoices to calculate energy consumption.

![](/api/attachments/T4DC32W6/fulltext/images/915c3d54d37153a18bf5ff71fecdcd7e70d109005bad1cee84e0b2a713aac0ff.jpg)  
Figure 8. ECMS Constructs: System Components and Information Flows (Revised)

In general, the component must compensate for the absence of actual sensor measurements and manage secondary energy and fuel consumption data. Therefore, we revised DP2.2 to include secondary fuel consumption data, rather than only the energy-related data:

DP2.2 (revised): Provide features that can identify, collect, and process the secondary energy and fuel consumption data so that the system affords the ability to monitor non-sensor energy and fuel consumption, given a company’s levels of data availability.

Principles related to the supply chain coordination component: Respondents relayed concerns about disclosing environmental information that supply chain partners can use during negotiations, particularly information about bad environmental performance, which we addressed by defining a minimum set of required data and by sharing aggregated high-level KPIs (Organizations C and D). Moreover, the ECMS provides various levels of collaboration that allow supply chain partners to engage gradually with ECM and to differentiate the information shared. To address collaboration issues and information sharing concerns, we revised DP3.1 as follows:

DP3.1 (revised): Provide features that enable data exchange among supply chain partners by using data privacy and security protocols that consider various levels of information exchange and apply standards for information sharing so that the system affords the ability to coordinate across the supply chain.

Suppliers and retailers (Organizations C and D) used their own internal codes to describe the contextual data flow among products, partners, facilities, and vehicles. For example, even when a product had the same barcode across its lifecycle, suppliers and retailers used an internal product code. To align various internal product codes or differences in measurement units, we devised a new design principle:

DP3.3 (new): Provide features for aligning master data like supply chain partners’ various product identification codes so that the system affords the ability to trace and coordinate the data across the supply chain.

Principles related to the ECMS workflow engine component: Even when the required data were available and of good quality, organizations usually kept them at differing levels of granularity. For example, Organizations C and D kept transactional data such as inventories and shipments on a daily basis, while all four companies kept energy consumption data either at a highly aggregated level (e.g., monthly) or at an overly detailed level, as energy sensors could record energy consumption in real time. Therefore, we had to consider granularity levels as a basic parameter in our ECMS design. We concluded that, in Organizations C and D, collecting and aggregating information at a daily level was adequate to ensure both the applicability and meaningfulness of results, whereas Organizations A and

B required the exact time stamp of all transactional data. Collecting and monitoring information at a detailed time level in Organizations A and B increased complexity and made the applicability of an ECMS even more challenging. As a result, we based the required granularity level on the trade-off between complexity and the level of informational detail. To address the issue of varying levels of data granularity levels, we suggest the following DP:

DP4.3 (new): Provide features such as mechanisms for aggregating energy consumption data at a daily granularity level that transform multiple kinds of data into the same granularity level so that the system affords the ability to monitor the supply chain end to end and coordinate information flows.

Principles related to the reporting component: In addition to the ECM results, at least one end user in each of the four organizations expressed the need to know the data availability levels—their type and origin—along with the data quality, data granularity, the business logic for calculating carbon emissions, as well as the standards applied for calculating the various KPIs, in order to be able to interpret these data. Therefore, we formulated DP5.3 as follows:

DP5.3 (new): Provide features for reporting data availability, data quality, data granularity, the ECM calculation and allocation logic, and the standard applied so that the system affords the ability to inform end users in a transparent, accurate, and comparable way.

Principles related to the carbon footprint estimator component (new): Ensuring the comparability of the results necessitates integrating information flows, which requires a shared granularity level, a complete and accurate dataset, and availability of all required data. For example, in Organizations C and D, we could not compare the carbon emissions of two routes when the routes used different allocation parameters, such as weight, volume, and item. To address the complexity of combining different types of information flows, the ECMS deployed an adaptable logic, allocating the carbon emissions at different levels of analysis and ensuring uniform granularity at all four sites. This logic initially examines data availability and informs the definition of its parameters based on a set of availability measures, such as industry standards for fuel consumption per vehicle type if actual fuel consumption is not available.

DP6.1 (new): Provide features for calculating the ECM KPIs at various levels of analysis using the data granularity level, data accuracy, data availability, and emission factors so that the system affords the ability to estimate energy consumption and the carbon footprint.

In specifying and defining the KPIs to be monitored, common standards can be used to ensure the comparability of different energy and carbon indicators and to address diversity in the carbon calculation and allocation methods used. However, common standards were often missing at the four sites, and end users stated that they had to select the standard to be applied in calculating the KPIs. For example, we employed the GhG Protocol (2011) and, for Organizations C and D, we also adopted the Sustainability Measures for Logistical Activities (Consumer Goods Forum, 2012), as they calculate aspects of the environment and the operations daily.

DP6.2 (new): Provide features for implementing various assessment methodologies, carbon management standards, and related KPIs so that the system affords the ability to estimate energy consumption and the carbon footprint—given the lack of standardized indicators of energy consumption and carbon emissions and traditional performance indicators—as well as compliance with reporting standards or initiatives, including governmental guidelines.

## 5.3 Round 2: Reflection on the Utility of ECMS Design Theory

In the second round, our design theory components converged well; thus, we added no constructs or principles. Instead, we focused on evaluating the extent to which the ECMS design theory, if instantiated, would help to integrate information flows, ECM, and environmentally aware decision-making and practice. This round allowed us to evaluate our design theory and the associated artifact through proofof-concept and proof-of-value research (Nunamaker et al., 2015). The final set of system components and principles appears in Table 8.

In this round, we presented the results of specific scenarios in workshops with at least one end user per organization. The group of end users, in collaboration with the research team, specified the scenarios based on the purpose and scope dimensions of the ECMS, which we also used to define the demonstration settings. Rather than an exhaustive list of scenarios, we wanted to evaluate an instantiation of a designed artifact to establish its utility in achieving its stated purpose (Venable et al., 2012), thus offering key proof-ofconcept examples (Nunamaker et al., 2015). The end users assessed the utility of the ECMS in these scenarios, which are described in Appendix A. The second evaluation round also gave us an opportunity to collect evidence about the value of ECMS, thus moving toward a proof-of-value evaluation of the artifact.

Next, we present the outcomes, structured according to overall feedback, energy and carbon measurement, environmentally aware decision-making and practice, aspects of implementation and future enhancements, and further exploitation.

Table 8. Final ECMS System Components and Design Principles

<table><tr><td>Key component</td><td>Design principles</td></tr><tr><td>Data collection</td><td>DP1.1 Provide features for collecting and cleansing energy and operational data so that the system affords the ability to process energy and operational data.DP1.2 Provide features for generating missing environmental data so that the system affords the ability to process energy data given a company&#x27;s levels of data availability and quality.DP1.3 Provide features for generating missing operational and transactional data and transforming existing data into a compatible format so that the system affords the ability to process operational and transactional data, given a company&#x27;s levels of data quality and inconsistency.</td></tr><tr><td>Energy monitoring</td><td>DP2.1 Provide features for assigning sensors to specific machines and processes, for collecting, processing and storing energy sensor consumption data, and for calculating energy values per time interval so that the system affords the ability to monitor energy sensors.DP2.2 Provide features for identifying, collecting, and processing the secondary energy and fuel consumption data so that the system affords the ability to monitor non-sensor energy and fuel consumption, given a company&#x27;s levels of data availability.</td></tr><tr><td>Supply chain coordination</td><td>DP3.1 Provide features that enable data exchange among supply chain partners by using data privacy and security protocols that consider various levels of information exchange and apply standards for information sharing so that the system affords the ability to coordinate across the supply chain.DP3.2 Provide features for modeling organizations&#x27; structure, production, and supply chain processes and supporting their decomposition into the required levels of analysis so that the system affords the ability to coordinate across the supply chain.DP3.3 Provide features for aligning master data like supply chain partners&#x27; various product identification codes so that the system affords the ability to trace and coordinate the data across the supply chain.</td></tr><tr><td>ECMS workflow engine</td><td>DP4.1 Provide features for combining data from various sources of the daily operational activities across the supply chain (e.g., shipments, inventories, production), including emission factors and relevant data from governmental databases so that the system affords the ability to monitor the supply chain end to end and coordinate information flows.DP4.2 Provide features for calculating KPIs at various levels of analysis so that the system affords the ability to monitor the supply chain end to end and to coordinate information flows.DP4.3 Provide features such as mechanisms for aggregating energy consumption data at a daily granularity level that transform multiple kinds of data into the same granularity level so that the system affords the ability to monitor the supply chain end to end and coordinate information flows.</td></tr><tr><td>Reporting</td><td>DP5.1 Provide features for reporting on the organizational, supply chain, and production process structures so that the system affords the ability to inform users about the scope of ECM.DP5.2 Provide features for reporting on the ECMS purpose and scope, hierarchies, and KPIs and complying with environmental standards and reporting initiatives so that the system affords the ability to inform end users about measurements of ECM.DP5.3 Provide features for reporting data availability, data quality, data granularity, the ECM calculation and allocation logic, and the standard applied so that the system affords the ability to inform end users in a transparent, accurate, and comparable way.</td></tr><tr><td>Carbon footprint estimator (new)</td><td>DP6.1 Provide features for calculating the ECM KPIs at various levels of analysis using the data granularity level, data accuracy, data availability, and emission factors so that the system affords the ability to estimate energy consumption and the carbon footprint.DP6.2 Provide features for implementing various assessment methodologies, carbon management standards, and related KPIs so that the system affords the ability to estimate energy consumption and the carbon footprint—given the lack of standardized indicators of energy consumption and carbon emissions and traditional performance indicators—as well as compliance with reporting standards or initiatives, including governmental guidelines.</td></tr></table>

## 5.3.1 Overall Feedback

Overall, the end users in Organizations A, B, C, and D agreed that the developed artifact met the initial requirements and addressed first-round challenges such as data heterogeneity, integration quality, and completeness. For example, an end user from Organization D stated that

combining information flows and trusting the ECMS results are key to the system’s success and must be safeguarded with appropriate validation processes. I am happy to see that the new design principles addressed the challenges raised in the first round.

All users perceived the deployed ECMS as userfriendly and reliable, as offering easy access to information, and as supporting efficient monitoring of energy consumption and carbon emissions. The systems provided information that was previously unavailable, which the respondents considered to be timely, accurate, easy to understand, and relevant to key organizational decision makers. The respondents from Organizations C and D expressed that environmentally aware decisions could be positively affected by the higher quality of the information.

Respondents identified the combination of energy- and carbon-related KPIs with KPIs related to production (Organizations A and B), sales or supply chain operations (Organizations C and D) as the key strengths of ECMS in terms of optimizing performance and enhancing decision-making. As a respondent from organization D also highlighted:

by enabling ECMS automatic energy data capture, energy and carbon calculations were based on our actual, daily data rather than yearly estimations, and the opportunities to quantify our impacts could now be materialized. Thus, ECMS provided credible results that are based on my own data and not on generic industry data provided by a third party.

Moreover, they recognized the unified data layer and data collection component as significant contributions of the ECMS since they allowed them to collect their supply chain partners’ data (Organization D).

## 5.3.2 Energy and Carbon Measurement

Energy consumption in Organization A was highly dispersed and understood only through monitoring. The weaving department contained many small machines with linear energy consumption, whereas the finishing mill used few large machines with varying nonlinear and heavy energy consumption, on average. These latter machines were idle 36% of the time, which was reduced to 22% after the company integrated the ECMS results into their production scheduling processes. The ability to observe the energy consumption per machine, per process step, or for an entire textile process revealed both the energy profiles of the machines and the commonalities and differences among the types of products. That is, the organizations perceived different levels of aggregation as critical.

For Organization B, identifying the most energyconsuming machines was valuable because these machines affect peak electricity consumption, which incurs high penalties if it is excessive. Reducing these peaks led to significant cost reductions. Moreover, the energy consumption during standby, cooling, or heating was shown to be substantial, even sometimes during the weekend, when limited production took place, meaning that detailed monitoring may lead to considerable reductions. Energy monitoring also helped improve production schedules, mainly in terms of the reduced use of energy-consuming machines while on standby— up to 16% of energy use could be saved by shutting down such machines at appropriate intervals.

The new analyses also showed that indirect consumption, such as by water depuration systems, warehouses, and administration in Organizations A and B, was significant, and nonproduction departments in Organization B used about half of the electrical energy. Organizations must consider all departments, not only production departments, when the goal is to reduce electricity consumption.

Energy costs are a major cost driver in Organization C’s stores; thus, Organization C invested in energy efficiency infrastructures in their new and renovated stores over the years. After the ECMS presented the energy consumption and carbon footprint of three representative stores, the supply chain manager realized that

the environmental impact of our green store is one third of the environmental impact of our older, less energy-efficient store and around half of a conventional store.

ECMS also provided Organization C with the ability to measure the energy consumption and the carbon footprint of the various sections in its stores by considering temperature requirements for products like cheese and cold cuts, frozen foods, fruits and vegetables, meat, and other refrigerated food. Thus, according to an end user at Organization C:

ECMS enabled us to monitor energy consumption per section and product category, which allowed a more efficient and fair distribution of the carbon footprint on product categories. However, we must be careful when using this information to avoid stigmatizing any product categories.

An end user in organization D observed that

we need to be able to detect monthly where we lose energy, but our current system is not so sophisticated, as it is based mainly on energy consumption bills. ECMS and the smart meters provided us with better information about our energy consumption.

ECMS was also valuable in measuring the impact of alternative modes of distribution and networks, such as direct store delivery versus centralized delivery based on a product’s carbon footprint. By understanding the energy and carbon measurement logic incorporated in ECMS and the estimations related to product categories and product levels, the end users at Organization D could get information for more products, calculate their environmental product declarations, and even experiment by changing product-related attributes like packaging units.

## 5.3.3 Environmentally Aware Decision-Making and Practice

In Organization A, implementing ECMS obliged the operators to engage in a critical discussion about all aspects of energy consumption, from individual machinery analysis to renegotiating the purchasing contracts. All functions were involved, from production and maintenance to scheduling and accounting. This discussion led to potential cost reductions based on reducing machines’ idle time, renegotiating energy contracts, and reducing the time required to produce (i.e., the “makespan”), which reduced indirect consumption and, to a large extent, fixed consumption. All these outcomes reduced the energy consumption directly related to production.

Organization B decided to reduce the number of people who worked during the weekend to the absolute minimum to avoid using nonproductive infrastructures like ventilation. However, energy-aware behavior by employees also proved to be important. For example, reducing the number of employees over the weekend would reach its full potential for energy reduction only if employees were aware that using a ventilation system for only one person would consume excessive energy and jeopardize energy reduction efforts. Moreover, working with ECMS has the potential to have a strong economic impact by eliminating shifts with low utilization of machines, as long as delivery dates are not violated, which would reduce the number of times total consumption exceeds the peak established with the electricity provider, and shutting down energyconsuming machines when they are in standby.

By measuring the energy consumption and carbon footprints of stores with different profiles, managers in Organization C could quantify the impact of investments on energy-efficient infrastructures and plan their future investments, such as replacing refrigerators.

Organization D also highlighted the necessity of having ECMS results:

We need ECMS because CO<sub>2</sub> is also directly connected with costs. If we reduce CO<sub>2</sub>, we can reduce our costs as well. All this information may be used in negotiations with clients—or customers may request it—to show them the improvements in some environmental aspects of our company. We are talking about certifications. It’s absolutely necessary to prove that we are improving ourselves and that we have environmental plans to reduce our $C O _ { 2 } .$

Organizations C and D contended that ECMS could strengthen the collaboration between supply chain partners and that joint environmental decisions could be positively affected by information of higher quality and granularity and by enhanced visibility of the supply chain. For example, the possibility of comparing different distribution networks passing through—or not passing through—the retailer’s central warehouse enabled Organizations C and D to initiate a discussion on jointly addressing environmental challenges.

Customers’ requests for details about carbon footprints at the product level have raised issues related to competition between companies, meaning that the need for accurate and comparable measures to enhance the quality of benchmarking has increased. ECMS addressed the complexity of these calculations in Organizations C and D so they could pass this information to their end consumers.

Overall, the end users in Organizations A, B, C, and D believed that ECMS are aligned with their environmental strategies and could support their sustainability practices overall. For example, Organization A and B wish to develop an energyefficient production process that would alleviate peaks in energy consumption and use their available machines more efficiently, Organization C wants to measure the environmental impact of its activities and develop energy-efficient stores and warehouses, while Organization D seeks to improve the environmental profile of its product and address environmental challenges in collaboration with retailers.

Finally, ECMS can help not only large companies but also small and medium-sized enterprises capture their emissions, identify their origin, and reduce them based on measurements of CO<sub>2</sub>. They can compare their advancements per individual service and at various operational levels. Ideally, such an approach would be compatible with financial accounting, as it would allow users to integrate and compare figures, to see the effects of monitoring, and to make better daily business decisions and trade-offs by using a common approach. Methodologies that are simple, practical, and less complex are the key (Organization D).

## 5.3.4 Aspects of Implementation, Future Enhancements

The transition to ECMS was nontrivial for the organizations in our study, as most employees were used to their legacy systems, making contextual help and customization important. The instantiation was efficient but the shift that was required for all four organizations to understand its use and value was nontrivial, as were the integration and the data interfaces required. After the two rounds of demonstration and evaluation, it was clear that the full potential could be unlocked only by redesigning some processes, such as production planning and scheduling for Organizations A and B.

In the demonstration phase, ECMS were not fully integrated with the organizations’ existing systems, meaning that considerable additional manual effort was required to collect data that were not easily available. This level of integration was acceptable in the context of prototype development, but integration is critical for the further operational use of ECMS. However, one of the respondents stated that “because of its business value, commercial platforms or ERP systems could also adapt the functionalities ECMS support,” thus eliminating any future integration effort.

Addressing data issues remains a prerequisite for enhancing ECMS implementation. For example, validating nonlinear energy consumption models for Organization B needed more detailed data over a longer time horizon to avoid miscalculations. As the combination of information flows requires strict data specifications, the organizations needed more detailed exception handling to return precise information with malformed data, inconsistent requests, or bad configuration parameters. Moreover, the environmentally aware decision-making process could be improved by adding new, more meaningful KPIs to the reports using the carbon footprint estimator component and including cost parameters. ECMS should also include an extended element to consider the cost to an organization, at a minimum, as cost data for supply chain partners are confidential. However, as one of the respondents from Organization D claimed, “It would be good to have the cost next to the CO<sub>2</sub>, but our focus is not on the cost. Reducing CO<sub>2</sub> in transportation usually also reduces the cost.”

User friendliness and system usability were other aspects of the implementation on which the users commented, but developing polished interfaces and providing multilingual context-sensitive help was beyond the scope of the four pilots. Therefore, the respondents considered the artifact instantiation to be acceptable for a system demonstration but also expressed that it should be improved before being released as a permanent deployment (Organizations A, B, C, D).

## 5.3.5 Future Exploitation

A simple comparison of the energy used and saved was not the only KPI that the end users considered in validating the potential impact of the ECMS. The new information provided and the environmentally aware decision-making enabled end users to decide to systematically invest further in the realization of the ECMS (Organizations A and B).

Organization C assessed the energy consumption per warehouse and per storage section, as well as across its distribution network. Electric power bills and fuel consumed in handling internal deliveries from warehouse to stores were among the organization’s highest running expenses. Organizations C and D anticipated acquiring competitive advantages in terms of green collaborative supply chain processes, collaborative distribution processes, and distribution optimization; ECMS could support reporting and negotiation with several of their customers and suppliers.

## As for Organization D, a representative stated:

We want to adopt an ECMS in our company; this is not an academic and research game for us but an endeavor to understand how systems like that can provide us with energy and carbon footprint information, support our sustainability strategies, and enrich our decision-making processes with environmental aspects … I would base my environmental reporting on the ECMS reports, which are much more accurate than the rough estimates I currently do monthly. Both regulations and consumers’ attitudes suggest that. In the future, the information and capabilities provided by ECMS will not be only useful but mandatory.

We can also attribute the positive feedback and outcome of the second evaluation round to the research approach followed in designing and developing the artifact. We engaged end users throughout this process so that they could communicate their needs and requirements during multiple rounds and interactions with the research team and fully understand the design and implementation challenges of ECMS. Against this backdrop, in the second round, they focused on the information value gained and how ECMS can support the measurement of energy consumption and carbon emissions, along with environmentally aware decisionmaking and practice. They recognized this potential and its future exploitation. However, all the organizations also recognized the need to further develop the ECMS artifact, mainly by increasing integration with existing systems and polishing interfaces, in order for it to be exploitable as a product for deployment and productive use.

## 6 Discussion and Implications

## 6.1 Contribution to the Green IS Literature

Our design theory contributes to the ongoing discourse on developing prescriptive knowledge about IS that support environmental sustainability (Malhotra et al., 2013; Seidel et al., 2013) and their impact when implemented in the field. Previous studies have translated explanatory and predictive theory into Green IS design knowledge (e.g., Recker, 2016; Seidel et al., 2018; Watts & Wyner, 2011), but most consider Green IS at an aggregate level (e.g., Chowdhury, 2012; Melville, 2010). Therefore, to explain how they address pertinent environmental problems (Corbett, 2013) we must unpack the black box of Green IS by studying the design and implementation of ECMS as a key type of Green IS.

While our focus is on ECMS, our study also provides some insights into Green IS in general. While Green IS are typically defined by a focus on their ends in terms of enabling environmentally sustainable processes and outcomes (Recker 2016; Watson et al., 2010), we extend this perspective by attending to the means that help to accomplish these ends: environmental information flows coupled with key material features for ECM and environmentally sensitive decisionmaking and practice.

Against this backdrop, we explore the specific types of data and associated information flows that are salient to the development of ECMS because it is these environmental data that are often not available in an appropriate form. Therefore, these data are not used for environmentally sensitive decision-making and practice although it is these data that one must have in order to simultaneously attend to economic, social, and environmental KPIs.

We also explicate this means-end relationship by attending to key material features in the form of two types of constructs in our design theory: energy information flows and system components for monitoring energy and estimating the carbon footprint. We highlight how these environmentally specific components, in conjunction with more generic components for data collection and reporting, constitute a Green IS. This insight highlights how we can reinterpret IS—arguably the greatest drivers of productivity in the past decade (Watson et al., 2010)— in light of sustainability and then combine them with environmentally specific functional building blocks to form IS that facilitate simultaneous economic and environmental outcomes.

We involved industry practitioners in all phases of design and development to obtain the requirements and justificatory knowledge that informed our design and thus the constructs (system components and information flows) and design principles we derived. Deep engagement with industry practitioners provided the foundation for developing prescriptive knowledge (Buhl et al., 2012; Mathiassen & Nielsen, 2008; Seidel et al., 2017). We also actively engaged with scholars and practitioners from other fields, such as management, computer science, engineering, environmental science, supply chain, retailing, and manufacturing—an approach that researchers have found is conducive to Green IS research (vom Brocke et al., 2012).

## 6.2 Contribution to the Literature on ECMS in the Supply Chain

We also contribute to the discourse on the use of IS in the development of ECM in the supply chain (Björklund et al., 2012; Maestrini et al., 2017; Qorri et al., 2018). Our ECMS design addresses the ECM requirements through six system components—data collection, energy monitoring, supply chain coordination, ECMS workflow engine, the carbon footprint estimator, and reporting—that integrate and coordinate four types of information flows: transactional, contextual, energy, and productenvironmental. Our study identified the carbon footprint estimator as a key component of ECMS. Defining the design principles related to this component and integrating them in our architecture were key steps in consolidating the emergent ECMS design theory. By collecting evidence from four organizations in different industries, we broadened our understanding of ECMS in the supply chain. Our components reached their final form and content only after two rounds of building, demonstrating, and evaluating an expository instantiation with these four organizations.

This design theory contributes also to the broader category of EMIS, and ECMS in particular. While a considerable body of knowledge is related to the design of systems from which we can extract design requirements and design principles, these works focus on implementing artifacts that address specific problems rather than on formulating an abstract IS design theory, as our study does.

We also contribute to the currently limited knowledge about the impact and proof of value of ECMS/EMIS, along with their implementation challenges, such as integration with legacy systems, data acquisition and quality, varying levels of data granularity, and integration of energy-related information into process or operational data. The data-related challenges of ECMS arise mainly from data that are heterogeneous, secondary, and time dependent, thus diminishing the information’s reliability and accuracy (Melville & Whisnant, 2012). The data capture and integration capabilities of ECMS impact their data quality (Melville & Whisnant, 2014); we therefore need design principles that address data quality, transparency for stakeholders, and increased accuracy (Melville et al., 2017). Thus, system implementation was not our primary focus but part of our proof-ofconcept and proof-of-value approach. We identified the implementation challenges of ECMS by running four practical demonstrations and attending to how they affected ECMS design.

By providing empirical evidence about the challenges of ECM in the supply chain, we address the call for more empirical studies on the development of performance measurement in SSCs (Ahi & Searcy, 2015; Björklund et al., 2012). More specifically, we offer insights related to the different ECM dimensions of manufacturing, warehousing, distribution, and overall supply chain, along with the KPIs per dimension, the necessary information flows (contextual, transactional, energy, and product environmental), and the factors affecting the development of ECM.

Considering recent trends, the planetary boundary (PB) framework has received considerable attention as an environmental sustainability reference and has been diffused into policy making (Galaz et al., 2012) and into industrial organizations (Bjørn et al., 2017; Steffen et al., 2015). PB provides a framework for managing environmental resources at the global level and a way to move beyond assessing anthropogenic systems in terms of ecoefficiency in order to assess their impacts in relation to the actual state of the environment. However, most of the environmental impacts that human activities cause operate via local effects; thus, many studies investigate how life cycle impact assessment methods can evaluate environmental impacts at the local level to operationalize the framework (Bjørn et al., 2015; Ryberg et al., 2016; Sala et al., 2020).

This view provides a space in which the role and outcomes of ECMS can be positioned in the global context. Sala et al. (2020) match the seventeen LCA impact categories (e.g., climate change, resource use) with the planet’s ten boundaries. The carbon emissions or CO<sub>2</sub> equivalents that ECMS can calculate are the main metrics associated with the LCA impact categories related to climate change. In this view, ECMS can provide outcomes that can link to three key elements of the PB framework—climate change, ocean acidification, and biodiversity integrity—and support addressing these problems. However, future studies should explore how IS could support the calculation of other supply chain KPIs and materialize the PB framework in a more holistic way.

## 6.3 Practical and Managerial Implications

The ECMS design theory suggested here and the artifact we developed can inform software engineers in their efforts to design IS for ECM in the context of supply chains. Our results highlight the core principles of ECMS design, thereby emphasizing a compact set of material features and functionalities that ECMS must offer.

For software vendors, our architecture exhibits a coherent decomposition of the system’s components and their interactions. Modularity can improve systems’ reusability and integration, although the various ECMS components may require context dependent implementation and deployment. Modularity further opens ECMS implementation to the involvement of stakeholders who have expertise in various fields, including energy sensor management, ECM, and supply chain management.

For managers and practitioners across the supply chain, our work captures the essential requirements related to ECM, presents an ECMS that addresses these requirements, and offers a proof of concept, along with main implementation challenges and a proof of value. Such knowledge can assist professionals in assessing the current state of their ECMS implementation and in adopting, implementing, and continuously improving ECMS. This practical value is supported by decomposing the general idea of ECMS into key components and by formulating prescriptive knowledge in terms of design principles related to these components. While some companies have energy reporting systems in place, others may be more competent in estimating carbon emissions. Our suggested ECMS design theory can help these companies develop their expertise, processes, and systems toward full-fledged ECM in the supply chain.

## 7 Conclusion

Our study derives prescriptive knowledge in terms of an IS design theory for ECMS in supply chains. By applying a DSR approach, we formulated an ECMS design theory, developed an expository instantiation based on the design, evaluated and refined the ECMS design theory and the expository instantiation, and provided proof-of-value evidence in two rounds of building, demonstration, and evaluation in four organizations.

Our key limitation lies in the study’s restricted empirical basis and hence the risk of focusing on specific conditions instead of general concepts. We sought to minimize this risk by grounding our conceptual design on previous studies and by validating the outcomes with industrial experts beyond those involved in implementing the system. The iterative process, stage of reflection and formalization of learning, and the overall action research approach we used supported a sound methodological effort to address this limitation.

Further research could investigate whether industryspecific characteristics significantly affect the role and design of ECMS, especially related to the actual and measurable impact of ECM in financial and environmental terms. We consider our consolidated design principles and likely the constructs themselves a starting point for similar work.

## Acknowledgments

We thank the editorial team and the team of anonymous reviewers for their detailed and developmental feedback, which helped us shape our work and enhance our theoretical contribution and implications. The first author and second author were partially supported by the FACTLOG research project, funded from the European Union’s Horizon 2020 program under Grant Agreement No. 869951.

## References

Acquaye, A., Ibn-Mohammed, T., Genovese, A., Afrifa, G. A., Yamoah, F. A., & Oppon, E. (2018). A quantitative model for environmentally sustainable supply chain performance measurement. European Journal of Operational Research, 269(1), 188-205.

Ahi, P., & Searcy, C. (2013). A comparative literature analysis of definitions for green and sustainable supply chain management. Journal of Cleaner Production, 52, 329-341.

Ahi, P., & Searcy, C. (2015). An analysis of metrics used to measure performance in green and sustainable supply chains. Journal of Cleaner Production, 86(C), 360-377.

Ansari, Z. N., & Kant, R. (2017). A state-of-art literature review reflecting 15 years of focus on sustainable supply chain management. Journal of Cleaner Production, 142, 2524-2543.

Arıkan, E., & Jammernegg, W. (2014). The single period inventory model under dual sourcing and product carbon footprint constraint. International Journal of Production Economics, 157, 15-23.

Bai, C., Sarkis, J., Wei, X. & Koh, L. (2012). Evaluating ecological sustainable performance measures for supply chain management. Supply Chain Management 17(1), 78-92.

Barroso, L. A., & Hölzle, U. (2007). The case for energyproportional computing. Computer, 40(12), 33- 37.

Baskerville R. & Pries-Heje J. (2014) Design theory projectability. Proceedings of the IFIP WG 8.2 Working Conference on Information Systems and Organizations.

Bengtsson, F., & Agerfalk, P. J. (2011). Information technology as a change actant in sustainability innovation: Insights from Uppsala. The Journal of Strategic Information Systems, 20(1), 96-112.

Bensch, S., Kolotzek, C., Helbig, C., Thorenz, A., & Tuma, A. (2015). Decision support system for the sustainability assessment of critical raw materials in SMEs. Proceedings of the 48th Hawaii International Conference on System Sciences (pp. 846-855).

Bensch, Stefan, Andris, R., Stindt, D., & Tuma, A. (2014). Conception of a novel open source environmental management information system design to assess the availability of resources: Status quo and directions for future research. In F. Piazolo & M. Felderer (Eds.), Novel methods and technologies for enterprise information systems (pp. 121-135). Springer.

Bjørn, A., Bey, N., Georg, S., Røpke, I., & Hauschild, M. Z. (2017). Is Earth recognized as a finite system in corporate responsibility reporting? Journal of Cleaner Production, 163, 106-117.

Bjørn, A., Diamond, M., Owsianiak, M., Verzat, B., & Hauschild, M. Z. (2015). Strengthening the link between life cycle assessment and indicators for absolute sustainability to support development within planetary boundaries. Environmental Science and Technology, 49(11), 6370-6371.

Björklund, M., Martinsen, U. & Abrahamsson, M. (2012). Performance measurements in the greening of supply chains. Supply Chain Management, 17(1), 29-39.

Bose, R., & Luo, X. (2011). Integrative framework for assessing firms’ potential to undertake Green IT initiatives via virtualization: A theoretical perspective. Journal of Strategic Information Systems, 20(1), 38-54.

Böttcher, C., & Müller, M. (2016). Insights on the impact of energy management systems on carbon and corporate performance. An empirical analysis with data from German automotive suppliers. Journal of Cleaner Production, 137, 1449-1457.

Bové, A.-T., & Swartz, S. (2016). Starting at the source: Sustainability in supply chains. McKinsey. https://www.mckinsey.com/business-functions sustainability-and-resource-productivity/ourinsights/starting-at-the-source-sustainability-insupply-chains

Bruton, K., O’Donovan, P., McGregor, A., & O’Sullivan, D. D. (2018). Design and development of a software tool to assist ISO 50001 implementation in the manufacturing sector. Journal of Engineering Manufacture, 232(10), 1741-1752.

Buhl, H. U., Müller, G., Fridgen, G., & Röglinger, M. (2012). Business and information systems engineering: A complementary approach to information systems—what we can learn from the past and may conclude from present reflection on the future. Journal of the Association for Information Systems, 13(4), 236-253.

Butler, T. (2011). Compliance with institutional imperatives on environmental sustainability: Building theory on the role of Green IS. Journal of Strategic Information Systems, 20(1), 6-26.

Carbon Disclosure Project (CDP) (2000). CDP: Supply chain. https://www.cdp.net/en/supply-chain

Carlson, R., Erixon, M., Forsberg, P., & Pålsson, A.-C. (2001). System for integrated business environmental information management.

Advances in Environmental Research, 5(4), 369- 375.

Cheng, C., Qi, M., Wang, X., & Zhang, Y. (2016). Multiperiod inventory routing problem under carbon emission regulations. International Journal of Production Economics, 182, 263-275.

Cherradi, G., El Bouziri, A., Boulmakoul, A., & Zeitouni, K. (2017). Real-time hazmat environmental information system: A microservice based architecture. Procedia Computer Science, 109, 982-987.

Chofreh, A. G., Goni, F. A., & Klemeš, J. J. (2018). Evaluation of a framework for sustainable enterprise resource planning systems implementation. Journal of Cleaner Production, 190, 778-786.

Chowdhury, G. (2012). Building environmentally sustainable information services: A green is research agenda. Journal of the American Society for Information Science and Technology, 63(4), 633-647.

Corbett, J. (2013). Designing and using carbon management systems to promote ecologically responsible behaviors. Journal of the Association for Information Systems, 14(7), 339-378

Culshaw, M. G., Nathanail, C. P., Leeks, G. J. L., Alker, S., Bridge, D., Duffy, T., Fowler, D., Packman, J. C., Swetnam, R., Wadsworth, R., & Wyatt, B. (2006). The role of web-based environmental information in urban planning: The environmental information system for planners. Science of The Total Environment, 360(1), 233- 245.

Dao, V., Langella, I. & Carbo, J. (2011). From green to sustainability: Information technology and an integrated sustainability framework. Journal of Strategic Information Systems, 20(1), 63-79.

de Camargo Fiorini, P., & Jabbour, C. J. C. (2017). Information systems and sustainable supply chain management towards a more sustainable society: Where we are and where we are going. International Journal of Information Management, 37(4), 241-249.

Des Autels, P., & Berthon, P. (2011). The PC (polluting computer): Forever a tragedy of the commons? Journal of Strategic Information Systems, 20(1), 113-122.

Du, S., Hu, L., & Song, M. (2016). Production optimization considering environmental performance and preference in the cap-and-trade system. Journal of Cleaner Production, 112, 1600-1607.

ecoinvent. (2019). ecoinvent 3.6. https://www. ecoinvent.org/database/ecoinvent-36/ecoinvent-36.html

Effenberger, F., & Hilbert, A. (2016). Towards an energy information system architecture description for industrial manufacturers: Decomposition & allocation view. Energy, 112, 599-605.

Effenberger, F., & Hilbert, A. (2018). A literature review on energy information system software development: Research gaps and questions in industrial manufacturing. Presented at the Multikonferenz Wirtschaftsinformatik.

Ehmke, J. F., Campbell, A. M., & Thomas, B. W. (2018). Optimizing for total costs in vehicle routing in urban areas. Logistics and Transportation Review, 116, 242-265.

El-Gayar, O. F., & Fritz, B. D. (2006). Environmental management information systems (EMIS) for sustainable development: A conceptual overview. Communications of the Association for Information Systems, 17, 2-49.

Elkazaz, M., Sumner, M., Naghiyev, E., Pholboon, S., Davies, R., & Thomas, D. (2020). A hierarchical two-stage energy management for a home microgrid using model predictive and real-time controllers. Applied Energy, 269, Article 115118.

Elliot, S. (2011). Transdisciplinary perspectives on environmental sustainability: A resource base and framework for IT-enabled business transformation. MIS Quarterly, 35(1), 197-236

European Commission (2019). ILCD international life cycle data system. https://eplca.jrc.ec.europa. eu/ilcd.html

European Commission. (2018). 2030 climate & energy framework [Text]. https://ec.europa.eu/clima/ policies/strategies/2030\_en

Eurostat. (2020). Renewable energy statistics: Statistics explained. https://ec.europa.eu/eurostat/statistics xplained/index.php/Renewable\_energy\_statistics

Galaz, V., Biermann, F., Folke, C., Nilsson, M., & Olsson, P. (2012). Global environmental governance and planetary boundaries: An introduction. Ecological Economics, 81, 1-3.

Genovese, A., Lenny Koh, S.C., Bruno, G. & Esposito, E. (2013). Greener supplier selection: State of the art and some empirical evidence, International Journal of Production Research, 51(10), 2868- 2886

GHG Protocol (2011). Corporate value chain (Scope 3) standard. https://ghgprotocol.org/standards/ scope-3-standard

Global Reporting Initiative. (1997). GRI standards. https://www.globalreporting.org/standards

Gibassier, D., Michelon, G., & Cartel, M. (2020). The future of carbon accounting research: We’ve pissed mother nature off, big time. Sustainability Accounting, Management and Policy Journal, 11(3), 477-485.

Goes, P. B. (2014). Design science research in top information systems journals. MIS Quarterly, 38(1), iii-viii.

Govindan, K., Rajendran, S., Sarkis, J., & Murugesan, P. (2015). Multi criteria decision making approaches for green supplier evaluation and selection: A literature review. Journal of Cleaner Production, 98, 66-83.

Graeuler, M., Teuteberg, F., Mahmoud, T., & Gómez, J. M. (2013). Requirements priorization and design considerations for the next generation of corporate environmental management information systems: A foundation for innovation. International Journal of Information Technologies and Systems Approach, 6(1), 98-116.

Gregor S., & Jones D. (2007). The anatomy of a design theory. Journal of The Association For Information Systems 8(5), 312-335.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337-356.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). The anatomy of a design principle. Journal of the Association for Information Systems, 21(6), 1622-1652.

Guenther, E., Endrikat, J., & Guenther, T. W. (2016). Environmental management control systems: A conceptualization and a review of the empirical evidence. Journal of Cleaner Production, 136, 147-171.

Gunasekaran, A., & Kobu, B. (2007). Performance measures and metrics in logistics and supply chain management: A review of recent literature (1995-2004) for research and applications. International Journal of Production Research, 45(12), 2819-2840.

Gunasekaran, A., & Ngai, E. W. T. (2004). Information systems in supply chain integration and management. European Journal of Operational Research, 159(2), 269-295.

Gunasekaran, A., Patel, C., & McGaughey, R. E. (2004). A framework for supply chain performance measurement. International Journal of Production Economics, 87(3), 333-347.

Hassini, E., Surti, C., & Searcy, C. (2012). A literature review and a case study of sustainable supply chains with a focus on metrics. International Journal of Production Economics, 140(1), 69-82.

Hervani, A. A., Helms, M. M., & Sarkis, J. (2005). Performance measurement for green supply chain management. Benchmarking, 12(4), 330- 353.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75-105.

Hilpert, H, Kranz, J., & Schumann, M. (2013b). Leveraging Green IS in Logistics. Business & Information Systems Engineering, 5(5), 315-325.

Hilpert, H., Beckers, C., Kolbe, L. M., & Schumann, M. (2013a). Green IS for GHG emission reporting on product-level? An action design research project in the meat industry. Proceedings of the 8th International Conference on Design Science at the Intersection of Physical and Virtual Design (pp. 324-339).

Hilpert, H., Thoroe, L., & Schumann, M. (2011). Realtime data collection for product carbon footprints in transportation processes based on OBD2 and smartphones. Proceedings of the 44th Hawaii International Conference on System Sciences.

Hoang, G., Molla, A., & Poon, P. L. (2016). How do environmental enterprise systems contribute to sustainability value? A practitioner-oriented framework. Proceedings of the Australasian Conference on Information Systems.

Hoang, G., Molla, A., & Poon, P. L (2017). An exploratory study into the use and value of environmental enterprise systems. Proceedings of the Australasian Conference on Information Systems.

Hoang, G., Molla, A., & Poon, P. L. (2019). Factors influencing the adoption of environmental enterprise systems. Proceedings of the Pacific Asia Conference on Information Systems.

Hua, G., Cheng, T. C. E., & Wang, S. (2011). Managing carbon footprints in inventory management. International Journal of Production Economics, 132(2), 178-185.

Iacob, M. E., van Sinderen, M. J., Steenwijk, M., & Verkroost, P. (2013). Towards a reference architecture for fuel-based carbon management systems in the logistics industry. Information Systems Frontiers, 15(5), 725-745.

Jain, S., Lindskog, E., Andersson, J., & Johansson, B. (2013). A hierarchical approach for evaluating energy trade-offs in supply chains. International

Journal of Production Economics, 146(2), 411- 422.

Janssen, B.P., Johnson, M. P., & Schaltegger, S. (2015). 20 years of performance measurement in sustainable supply chain management: What has been achieved? Supply Chain Management, 20(6), 664-680.

Konur, D., Campbell, J. F., & Monfared, S. A. (2017). Economic and environmental considerations in a stochastic inventory control model with order splitting under different delivery schedules among suppliers. Omega, 71, 46-65.

Kotsopoulos, D., Bardaki, C., Papaioannou, T. G., Lounis, S., & Pramatari, K. (2018). Agile usercentered design of an IoT-enabled gamified intervention for energy conservation. IADIS, 16(1), 1-25.

KPMG (2015). The KPMG survey of corporate responsibility reporting 2015. https://assets. kpmg/content/dam/kpmg/pdf/2016/02/kpmginternational-survey-of-corporate-responsibilityreporting-2015.pdf

Lee, K.-H. (2011). Integrating carbon footprint into supply chain management: The case of Hyundai Motor Company (HMC) in the automobile industry. Journal of Cleaner Production, 19(11), 1216-1223.

Kugler, M., Osswald, S., Frank, C., & Lienkamp, M. (2014). Mobility tracking system for CO<sub>2</sub> footprint determination. Proceedings of the 6th International Conference on Automotive User Interfaces and Interactive Vehicular Applications.

Kuo, T. C., Chen, G. Y.-H., Wang, M. L., & Ho, M. W. (2014). Carbon footprint inventory route planning and selection of hot spot suppliers. International Journal of Production Economics, 150, 125-139.

Lee, K.-H. (2012). Carbon accounting for supply chain management in the automobile industry. Journal of Cleaner Production, 36, 83-93.

Lee, K.-H., & Wu, Y. (2014). Integrating sustainability performance measurement into logistics and supply networks: A multi-methodological approach. British Accounting Review, 46(4), 361-378.

Legner, C., & Schemm, J. (2008). Toward the Interorganizational product information supply chain: Evidence from the retail and consumer goods industries. Journal of the Association for Information Systems, 9(4).

Lehtinen, J., & Ahola, T. (2010). Is performance measurement suitable for an extended enterprise?

International Journal of Operations and Production Management, 30(2), 181-204.

Leyh, C., Rossetto, M., & Demez, M. (2014). Sustainability management and its software support in selected Italian enterprises. Computers in Industry, 65(3), 386-392.

Li, J., Wang, L., & Tan, X. (2020). Sustainable design and optimization of coal supply chain network under different carbon emission policies. Journal of Cleaner Production, 250, Article 119548.

Lukyanenko, R. & Parsons, J. (forthcoming, 2020). Design theory indeterminacy: What is it, how can it be reduced, and why did the polar bear drown? Journal of the Association for Information Systems, 21(5), 1343-1369.

Luo, L., & Tang, Q. (2016). Determinants of the quality of corporate carbon management systems: An international study. International Journal of Accounting, 51(2), 275-305.

Maas, K., Schaltegger, S., & Crutzen, N. (2016). Integrating corporate sustainability assessment, management accounting, control, and reporting. Journal of Cleaner Production, 136, 237-248.

Maestrini, V., Luzzini, D., Maccarrone, P., & Caniato, F. (2017). Supply chain performance measurement systems: A systematic review and research agenda. International Journal of Production Economics, 183, 299-315.

Malhotra, A., Melville, N. P., & Watson, R. T. (2013). Spurring impactful research on information systems for environmental sustainability. MIS Quarterly, 37(4), 1265-1274.

Mandviwalla, M. (2015). Generating and justifying design theory. Journal of the Association for Information Systems, 16(5), 314-344.

Martí, J. M. C., Tancrez, J.-S., & Seifert, R. W. (2015). Carbon footprint and responsiveness trade-offs in supply chain network design. International Journal of Production Economics, 166, 129-142.

Martirano, L., Borghi, L., Bua, F., Cristaldi, L., Grigis, G., Lavecchia, C., Liziero, M., Mongioví, L., Nastri, E., & Tironi, E. (2018). Energy management information systems for energy efficiency. Proceedings of the IEEE International Conference on Environment and Electrical Engineering and IEEE Industrial and Commercial Power Systems Europe.

Mathiassen, L., & Nielsen, P. A. (2008). Engaged scholarship in IS research. Scandinavian Journal of Information Systems, 20(2), 3-20.

Mazidi, M., Rezaei, N., Ardakani, F. J., Mohiti, M., & Guerrero, J. M. (2020). A hierarchical energy

management system for islanded multi-microgrid clusters considering frequency security constraints. International Journal of Electrical Power & Energy Systems, 121, Article 106134.

Melville, N. P. (2010). Information systems innovation for environmental sustainability. MIS Quarterly, 34(1), 1-21.

Melville, N. P. (2012). Environmental sustainability 2.0: Empirical analysis of environmental ERP implementation. https://deepblue.lib.umich. edu/handle/2027.42/91283

Melville, N. P., & Saldanha, T. (2013). Information systems for managing energy and carbon emission information: Empirical analysis of adoption antecedents. Proceedings of the 46th Hawaii International Conference on System Sciences (pp. 935-944).

Melville, N. P., & Whisnant, R. (2014). Energy and carbon management systems: Organizational implementation and application. Journal of Industrial Ecology, 18(6), 920-930.

Melville, N. P., Saldanha, T. J. V., & Rush, D. E. (2017). Systems enabling low-carbon operations: The salience of accuracy. Journal of Cleaner Production, 166, 1074-1083.

Mullarkey M.T. & Hevner A.R. (2019) An elaborated action design research process model. European Journal of Information Systems, 28(1), 6-20.

Nishant, R., Teo, T., & Lim, V. (2017). Understanding the effectiveness of carbon management system (CMS): An Empirical Study. Proceedings of the Pacific Asia Conference on Information Systems.Nouira, I., Frein, Y., & Hadj-Alouane, A. B. (2014). Optimization of manufacturing systems under environmental considerations for a greenness-dependent demand. International Journal of Production Economics, 150, 188-198.

Nunamaker J.F. Jr., Briggs R.O., Derrick D.C. & Schwabe G. (2015). The last research mile: Achieving both rigor and relevance in information systems research. Journal of Management Information Systems, 32(3), 10-47.

Nuss, C. (2015). Developing an environmental management information system to foster sustainable decision-making in the energy sector. European Conference on Information Systems Completed Research Papers.

Page, B., & Rautenstrauch, C. (2001). Environmental informatics: Methods, tools and applications in environmental information processing. In C. Rautenstrauch & S. Patig (Eds.), Environmental Information Systems in Industry and Public Administration (pp. 2-11). IGI Global.

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Plitsos, S., Repoussis, P. P., Mourtos, I., & Tarantilis, C. D. (2017). Energy-aware decision support for production scheduling. Decision Support Systems, 93, 88-97.

Pries-Heje, J., Baskerville, R., & Venable, J. (2008). Strategies for design science research evaluation. Proceedings of the European Conference on Information Systems .

Qorri, A., Mujkić, Z., & Kraslawski, A. (2018). A conceptual framework for measuring sustainability performance of supply chains. Journal of Cleaner Production, 189, 570-584.

Rajeev, A., Pati, R. K., Padhi, S. S., & Govindan, K. (2017). Evolution of sustainability in supply chain management: A literature review. Journal of Cleaner Production, 162(C), 299-314.

Recker, J. (2016). Toward a design theory for green information systems. Proceedings of the 49th Hawaii International Conference on System Sciences.

Reuters. (2018) UPS partners with LA-based startup to develop electric delivery truck. https://www.reuters.com/article/us-ups-thortrucks-idUSKBN1KL22E

Ryberg, M. W., Owsianiak, M., Richardson, K., & Hauschild, M. Z. (2016). Challenges in implementing a planetary boundaries based lifecycle impact assessment methodology. Journal of Cleaner Production, 139, 450-459. https://doi.org/10.1016/j.jclepro.2016.08.074

Sala, S., Crenna, E., Secchi, M., & Sanyé-Mengual, E. (2020). Environmental sustainability of European production and consumption assessed against planetary boundaries. Journal of Environmental Management, 269, Article 110686.

Schaltegger, S., & Burritt, R. (2014). Measuring and managing sustainability performance of supply chains: Review and sustainability supply chain management framework. Supply Chain Management, 19(3), 232-241.

Scholtz, B., Calitz, A. P., & Jonamu, B. (2016). A framework for environmental management information systems in higher education. In J. Marx Gómez & B. Scholtz (Eds.), Information Technology in Environmental Engineering (pp. 29-40). Springer.

Schulze, M., Heidenreich, S., & Spieth, P. (2018). The impact of energy management control systems on

energy efficiency in the German manufacturing industry. Journal of Industrial Ecology, 22(4), 813-826.

Schweiger, K. (2016). An environmental management information system to support the decisionmaking process in the recycling sector for end-oflife-vehicles Proceedings of the Pacific Asia Conference on Information Systems.

Seidel, S., Bharati, P., Fridgen, G., Watson, R., Albizri, A., Boudreau, M.-C., & Watts, S. (2017). The sustainability imperative in information systems research. Communications of the Association for Information Systems, 40(1) 40-52.

Seidel, S., Kruse, L. C., Székely, N., Gau, M., & Stieger, D. (2018). Design principles for sensemaking support systems in environmental sustainability transformations. European Journal of Information Systems, 27(2), 221-247.

Seidel, S., Recker, J., & vom Brocke, J. (2013). Sensemaking and sustainable practicing: functional affordances of information systems in green transformations. MIS Quarterly, 37(4), 1275-1299

Sein, M., Henfridsson, O., Purao, S., Rossi, M., & Lindgren, R. (2011). Action design research. MIS Quarterly, 35(1), 37-56.

Setiyoko, A., Sensuse, D. I., & Noprisson, H. (2017). A systematic literature review of environmental management information system (EMIS) development: Research trends, datasets, and methods. Proceedings of the International Conference on Information Technology Systems and Innovation.

Seuring, S., & Müller, M. (2008). From a literature review to a conceptual framework for sustainable supply chain management. Journal of Cleaner Production, 16(15), 1699-1710.

Sloan, T. W. (2010). Measuring the sustainability of global supply chains: Current practices and future directions. Journal of Global Business Management, 6(1), 92-107.

Steffen, W., Richardson, K., Rockström, J., Cornell, S. E., Fetzer, I., Bennett, E. M., Biggs, R., Carpenter, S. R., Vries, W. de, Wit, C. A. de, Folke, C., Gerten, D., Heinke, J., Mace, G. M., Persson, L. M., Ramanathan, V., Reyers, B., & Sörlin, S. (2015). Planetary boundaries: Guiding human development on a changing planet. Science, 347(6223).

Stindt, D. (2014). An environmental management information system for improving reverse logistics decision-making. In R. G. González-Ramírez, F. Schulte, S. Voß, and J. A. C. Díaz

(Eds.), Computational logistics (pp. 163-177). Springer.

Sundarakani, B., de Souza, R., Goh, M., Wagner, S. M., & Manikandan, S. (2010). Modeling carbon footprints across the supply chain. International Journal of Production Economics, 128(1), 43-50.

Tajbakhsh, A., & Hassini, E. (2015). Performance measurement of sustainable supply chains: A review and research questions. International Journal of Productivity and Performance Management, 64(6), 744-783.

Taticchi, P., Tonelli, F., & Pasqualino, R. (2013). Performance measurement of sustainable supply chains: A literature review and a research agenda. International Journal of Productivity and Performance Management, 62(8), 782-804.

Techcrunch. (2019). Amazon’s climate pledge commits to net zero carbon emissions by 2040 and 100% renewables by 2030. https://techcrunch.com/ 2019/09/19/amazons-climate-pledge-commitsto-net-zero-carbon-emissions-by-2040-and-100- renewables-by-2030/

TESCO. (2017). Climate change. https://www. tescoplc.com/sustainability/planet/climatechange/climate-change/

Teuteberg, F., & Straßenburg, J. (2009). State of the art and future research in environmental management information systems: A systematic literature review. In D. I. N. Athanasiadis, P. A. E. Rizzoli, P. A. Mitkas, & P. D.-I. J. M. Gómez (Eds.), Information technologies in environmental engineering (pp. 64-77). Springer.

The Consumer Good Forum. (2012). 2016 KPI Team: Sustainability Measures for Logistical Activities—CO<sub>2</sub> (GHG) and Energy Reduction. https://www.theconsumergoodsforum.com/wpcontent/uploads/2017/11/CGF-Sustainability-Measures-for-Logistical-Activities-2016-KPI-Team.pdf

Thies, H., & Stanoevska-Slabeva, K. (2013). Enhancing the quality of information in inter-organizational environmental reporting information systems. Proceedings of the 46th Hawaii International Conference on System Sciences (pp. 3495-3504).

Tuni, A., Rentizelas, A., & Duffy, A. (2018). Environmental performance measurement for green supply chains: A systematic analysis and review of quantitative methods. International Journal of Physical Distribution & Logistics Management, 48(8), 765-793.

Varsei, M., Soosay, C., Fahimnia, B., & Sarkis, J. (2014). Framing sustainability performance of supply

chains with multidimensional indicators. Supply Chain Management, 19(3), 242-257.

Veleva, V., Hart, M., Greiner, T., & Crumbley, C. (2003). Indicators for measuring environmental sustainability: A case study of the pharmaceutical industry. Benchmarking, 10(2), 107-119.

Venable, J., Pries-Heje, J., & Baskerville, R. (2012). A Comprehensive framework for evaluation in design science research. In K. Peffers, M. Rothenberger, & B. Kuechler (Eds.), Design science research in information systems: Advances in theory and practice (pp. 423-438). Springer.

vom Brocke, J., Watson, R., Dwyer, C., Elliot, S., & Melville, N. (2013). Green information systems: Directives for the IS discipline. Communications of the Association for Information Systems, 33(1), 509-520.

Watson, R. T., Boudreau, M. C. & Chen, A. J. (2010). Information systems and environmentally sustainable development: Energy informatics and new directions for the IS community. MIS Quarterly, 34(1), 23.

Watson, R. T., Boudreau, M.-C., Chen, A. J., & Sepúlveda, H. H. (2011). Green projects: An information drives analysis of four cases. Journal of Strategic Information Systems, 20(1), 55-62.

Watson, R. T., Boudreau, M-C., Chen, A. J., Huber, M. (2008). Green IS: Building sustainable business practices. In R. T. Watson (Ed.), Information systems: A global text (pp. 247-261). Global Text Project.

Watts, S., & Wyner, G. (2011). Designing and theorizing the adoption of mobile technology‐mediated ethical consumption tools. Information Technology & People, 24(3), 257-280.

Whittle, C., Jones, C. R., & While, A. (2020). Empowering householders: Identifying predictors of intentions to use a home energy management system in the United Kingdom. Energy Policy, 139, Article 111343.

Winston, A., & Bonini, S. (2019) Greening global supply chains: From blindspots to hotspots to action.

The Sustainability Consortium. https://www. sustainabilityconsortium.org/downloads/ greening-global-supply-chains-from-blindspotsto-hotspots-to-action/

Xiao, Y., Zuo, X., Kaku, I., Zhou, S., & Pan, X. (2019). Development of energy consumption optimization model for the electric vehicle routing problem with time windows. Journal of Cleaner Production, 225, 647-663.

Yang J. (2018). FedEx introduces electric vehicles in China. Shine. https://www.shine.cn/biz/ company/1808019752/

Zampou, E., Karagiannaki, A., & Plitsos, S. (2014a) Sustainability performance measurement in manufacturing: Integrating environmental and operational aspects. Proceedings of the 17th EMAN Conference: From Sustainability Reporting to Sustainability Management Control.

Zampou, E., Plitsos, S., Karagiannaki, A., & Mourtos, I. (2014b). Towards a framework for energy-aware information systems in manufacturing. Computers in Industry, 65(3), 419-433.

Zhang, H., Liu, L., & Li, T. (2011). Designing IT systems according to environmental settings: A strategic analysis framework. Journal of Strategic Information Systems, 20(1), 80-95.

Zhang, S., Gajpal, Y., Appadoo, S. S., & Abdulkader, M. M. S. (2018). Electric vehicle routing problem with recharging stations for minimizing energy consumption. International Journal of Production Economics, 203, 404-413.

Zhou, P., & Wen, W. (2020). Carbon-constrained firm decisions: From business strategies to operations modeling. European Journal of Operational Research, 281(1), 1-15.

Zimmer, K., Fröhling, M., & Schultmann, F. (2016). Sustainable supplier management: A review of models supporting sustainable supplier selection, monitoring and development. International Journal of Production Research, 54(5), 1412-1442.

## Appendix

## DSR Phases and Activities

Table A1 provides an overview of the DSR phases, the DSR data collection methods and activities, their purpose, the participants/respondents, and the derived results in terms of design theory components. Table A2 provides an overview of the DSR phases, the derived results in terms of design theory components, and the sections where these are presented.

Table A1. Design Science Research Approach Activities, Participants and Results

<table><tr><td>Round</td><td>DSR phase</td><td>Activities / data collection method</td><td>Participants / respondents</td><td>Purpose of activities</td><td>Design theory components</td></tr><tr><td rowspan="7">Round 1</td><td rowspan="3">Phase 1</td><td>Working group met on a monthly basis for a period of seven months</td><td>Nine supply chain / logistics managers or directorsa</td><td>Elaborate the objectives of ECMS and respective challenges</td><td rowspan="3">The purpose and scope of ECMS: The scope of ECMS in the supply chain, key stakeholders involved and dimensions (manufacturing, warehousing, distribution, and supply chain)Key aspects guiding the formulation of the design requirements</td></tr><tr><td>Two semi-structured interviews</td><td>Head of Corporate Supply Chain Strategy &amp; Concepts at Metro Cash &amp; Carry and Senior Vice President Logistics—Alfa Beta Vassilopoulos SA-Delhaize Group.</td><td>Validate and enrich the findings of working group</td></tr><tr><td>Actual distribution data</td><td>Six-month distribution data provided by one grocery retailer and one food manufacturer</td><td>Drill down on the challenges of energy consumption measurement and carbon calculations</td></tr><tr><td rowspan="2">Phase 2</td><td>Semi-structured interviews</td><td>Fourteen end-users contained three high-level directors (supply chain, environmental sustainability, customer service), six mid-level managers from supply chain and logistics to production, plus a research director and four IT directors and integrators of the four organizations</td><td>Enrich the ECMS purpose and scope by identifying the ECMS KPIs, hierarchy and the data necessary for their calculation</td><td>ECMS KPIs, hierarchy and the data necessary for their calculation</td></tr><tr><td>Several meetings over a period of five months</td><td>Research team,bdevelopment team,cend-users' representatives</td><td>Converge on the design requirements</td><td>ECMS design requirements</td></tr><tr><td>Phase 3</td><td>Artifact prototype implementation</td><td>Research and development team</td><td>Design the ECMS and develop four artifact instantiations</td><td>ECMS constructs: Information flows and system componentsECMS design principlesECMS expository instantiation</td></tr><tr><td>Phase 4</td><td>Field study</td><td>Research team, development team, end users' representatives</td><td>Validate the design theory and investigate its design and implementation challenges and feasibility</td><td>Demonstration findings</td></tr><tr><td rowspan="3">Round 2</td><td>Phase 2 &amp; 3</td><td>Meetings</td><td>Research team, development team, end users’ representatives</td><td>Present the demonstration findings and reflect on them in order to revise the design theory components</td><td>Revised design theory constructs and design principles</td></tr><tr><td rowspan="2">Phase 4</td><td>Field study</td><td>Research team, development team, end users’ representatives</td><td>Validate the design theory and investigate its feasibility</td><td>Final design theory constructs and design principles</td></tr><tr><td>Workshop with end-users</td><td>End users’ representatives</td><td>Assess the utility of the artifact instantiation</td><td>ECMS design theory utility</td></tr><tr><td colspan="6">aMETRO - MyMarket, AB Vassilopoulos (Part of Delhaize Group), Barilla, Beiersdorf, Colgate-Palmolive, Nestle, Procter &amp; Gamble, Unilever, Kassoudakis Logistics PartnerbThe research team consisted by three of the authors with expertise in information systems design, green IS, supply chain management, manufacturing operations and optimizationcThe development team consisted by people from seven IT companies with expertise on supply chain modelling tools, LCA tools, manufacturing systems, energy sensors monitoring tools and IT integration.</td></tr></table>

Table A2. Design Science Research Approach Results and Related Sections

<table><tr><td>DSR round</td><td>DSR phase</td><td>Design theory components</td><td>Sections reported</td></tr><tr><td rowspan="8">Round 1</td><td rowspan="2">Phase 1</td><td>The purpose and scope of ECMS : the ECMS scope in the supply chain, key players involved and dimensions (manufacturing, warehousing, distribution, and supply chain)</td><td>Section 4.1, Figure 3 and Table 2</td></tr><tr><td>Key aspects of ECM that guided the formulation of the design requirements</td><td>Section 4.2</td></tr><tr><td rowspan="2">Phase 2</td><td>ECMS KPIs, hierarchy and the data necessary for their calculation</td><td>Section 4.1, Figure 4</td></tr><tr><td>ECMS design requirements</td><td>Section 4.2, Table 3</td></tr><tr><td rowspan="3">Phase 3</td><td>ECMS constructs: Information flows and system components</td><td>Section 4.3, Table 4, Table 5, and Figure 5</td></tr><tr><td>ECMS design principles</td><td>Section 4.3, Table 6</td></tr><tr><td>ECMS expository instantiation</td><td>Section 4.4</td></tr><tr><td>Phase 4</td><td>Demonstration findings</td><td>Section 5.2</td></tr><tr><td rowspan="2">Round 2</td><td>Phase 2 &amp; 3</td><td>Revised design theory constructs and design principles</td><td>Section 5.2</td></tr><tr><td>Phase 4</td><td>Reflection on the utility of ECMS design theory</td><td>Section 5.3</td></tr></table>

## Working Group and End User Requirements Elicitation: Phase 1 and 2 / Round 1

Next, we provide more details about how the working group was organized and the data analysis was performed as part of Round 1, Phase 1, and the end user requirements elicitation process conducted as part of Round 1, Phase 2.

## Working Group

We organized with the support of the ECR organization a working group that focused on “environmental sustainability and energy and carbon footprint monitoring in the supply chain.” ECR is a joint industry body to make the FMCG sector responsive to consumer demand and increase supply chain efficiency towards suppliers and retailers’ collaboration. This group included nine supply chain/logistics managers or directors of several FMCG companies in total that met on a monthly basis for a period of seven months, as presented in Table A1. We used an open call for participation to select the participants in the working group. Thus, they were eager to understand and expand their sustainability efforts within their organization and across the supply chain.

The working group was coordinated by two of the authors and each meeting lasted two hours. The authors guided the discussion, based on a predefined structure, and addressed the objectives agreed on in the first meeting:

• To investigate the current environmental and collaborative practices and future interest in environmental practices and, more specifically, in energy consumption and carbon footprint monitoring

• To examine the approaches followed in measuring and monitoring the environmental footprint and to what extent these approaches are applied

• To examine the collaboration level on addressing environmental issues

• To examine whether firms are ready to support information systems that enable energy consumption and carbon footprint monitoring both inside the organization and across the supply chain

The authors transcribed the key points mentioned during the meeting, reflected on the outcome of each meeting, and prepared a summary of the findings that were then discussed and validated in the successive meeting. Further, we had access to six months of distribution data provided by a grocery retailer and a food manufacturer that participated in the working group. The data covered the following scopes of the supply chain: (1) supplier plant warehouse—supplier warehouse, (2) supplier warehouse—retailer stores, and (3) supplier warehouse—retailer central warehouse. More specifically, we used data about distances traversed, fuel consumption, number of distribution units per route and per product, truck type and capacity, load weight, and volume. We applied energy and carbon measurements to investigate potential difficulties related to data availability, quality, and granularity. Τwo in-depth interviews with industry experts (summarized in Table A1) were held to validate and/or enrich the outcomes of the working group. These experts were selected because of their involvement in environmental sustainability organization projects and international activities.

## End User Requirements Elicitation Process

We conducted semi-structured interviews with the representatives of the four companies under study (presented in Table A1). The questionnaire used for guiding the ECMS user requirements specification included the following sections:

• Current environmental and collaborative practices, including questions such as “specify areas like production, distribution that your efforts focus on”

• Problematic areas, including questions such as “specify the problems that are addressed in collaboration with supply chain partners”

• Data availability, including questions such as “specify the available operational and environmental data” or “specify the data collection process (e.g., automatic or non-automatic)”

• Technological infrastructure capability, including questions such as “specify the systems that the organization uses at production, warehousing, distribution, ordering processes”

• Environmental performance indicators, including questions such as “specify the current way of evaluating environmental performance at the company, process and product levels”

• ECMS requirements, including questions such as “discuss and specify a list of services/functionalities that could be implemented by an ECMS”

![](/api/attachments/T4DC32W6/fulltext/images/07dcb98e8579997dde2585be64f093af5207cf5bee9778665765e8fcf07c926c.jpg)  
Figure A1. Viewpoint Definition Example

The research team transcribed the main points discussed during the interviews. We used the “viewpoint definition” template (Figure A1) to present end-users’ insights regarding ECMS and support the requirements analysis including the use case description, the data requirements specification, and the ECMS main functionalities specification. A high-level use case model described the ECMS requirements and illustrated the intended functions (use cases), the prospective users (actors), the relationships between the use cases and actors (use case diagrams), the primary and alternative use case flows, and the data required. The data collection was supplemented by on-site observations, including at four organizations factories, warehouses, and distribution centers. The research team, end users, and the development team discussed the detailed user insights and user and system requirements in several meetings over a period of five months.

## Workshops with End Users: Phase 4 / Round 2

In this round, we presented the results of specific scenarios in workshops with at least one end user per organization. The group of end users, in collaboration with the research team, specified the scenarios based on the purpose and scope of the ECMS, which were also used to define the demonstration settings. Initially, we presented the detailed list of the scenarios and then presented the ECMS instantiations and the ECMS results. The end users were asked whether the design and artifact instantiation covered the initially expressed energy and carbon management requirements, validated the KPIs and ECMS results and discussed how these results could support decision-making and practicing. The end users also highlighted important aspects of implementation, future ECMS enhancements, and exploitation.

## • Energy and carbon management for manufacturing:

\- Scenario 1: Managing energy consumption and carbon emissions of production machines and comparing them

\- Scenario 2: Managing energy consumption and carbon emissions of production processes and comparing them

\- Scenario 3: Managing energy consumption and carbon emissions of a production order by using estimations

• Energy and carbon management for warehousing:

Scenario 4: Managing energy consumption and carbon emissions of three retail stores with different environmental profiles and comparing them

• Energy and carbon management for distribution activities:

Scenario 5: Managing energy consumption and carbon emissions of different distribution networks and comparing them

• Energy and carbon management across the supply chain:

Scenario 6: Managing energy consumption and carbon emissions from supplier’s warehouse to retailers stores

Scenario 1: Managing Energy Consumption and Carbon Emissions of Production Machines and Comparing Them

End users wanted to know about the energy and carbon efficiency per machine and its differentiation across production processes. Figure A2 shows that different monitoring levels supported by the manufacturing expository instantiation.

![](/api/attachments/T4DC32W6/fulltext/images/b25ea172190b1fc8447ba5cee3a1e217e15904efcaa0516c06ea5e5247a54a29.jpg)  
Figure A2. Managing Energy Consumption and Carbon Emissions of Production Machines and Comparing Them

## Scenario 2: Managing Energy Consumption and Carbon Emissions of Production Processes and Comparing Them

In this scenario, end users wanted to be informed about the energy and carbon efficiency of production processes and the production orders to identify the most (in) efficient ones. They also wanted to know the carbon efficiency of a specific product and how this fluctuates across different processes. Figure A3 shows the energy of production orders and articles per process.

![](/api/attachments/T4DC32W6/fulltext/images/e08288f3387d610ce355c67bec8d6fa540c8f8b3a0c0aab607c2b0e78accd0b3.jpg)  
Figure A3. Managing Energy Consumption and Carbon Emissions of Production Processes and Comparing Them

<table><tr><td>Name</td><td>Description</td><td>Article</td><td>Quantity</td><td>Released on</td><td>Due for</td></tr><tr><td>F0_345978</td><td></td><td>-</td><td>51.200</td><td>05/05/2013 21:00</td><td>13/06/2013 21:00</td></tr><tr><td>F0_345979</td><td></td><td>-</td><td>44.400</td><td>05/05/2013 21:00</td><td>13/06/2013 21:00</td></tr><tr><td>F0_345984</td><td></td><td>-</td><td>48.400</td><td>07/05/2013 21:00</td><td>13/06/2013 21:00</td></tr><tr><td>F0_346028</td><td></td><td>-</td><td>60.400</td><td>08/05/2013 21:00</td><td>13/06/2013 21:00</td></tr><tr><td>F0_346029</td><td></td><td>-</td><td>60.200</td><td>08/05/2013 21:00</td><td>13/06/2013 21:00</td></tr><tr><td>F0_346030</td><td></td><td>-</td><td>47.800</td><td>08/05/2013 21:00</td><td>13/06/2013 21:00</td></tr></table>

## Scenario 3: Managing Energy Consumption and Carbon Emissions of a Production Order by Using Estimations

Scenarios 3 and 2 had similar aims but Scenario 3 gave an emphasis on exploiting secondary energy consumption data when energy sensors and real energy measurements are not available (Figure A4). To evaluate the accuracy of estimations, the end user wanted to see a comparison of the energy and carbon efficiency based on real data and on estimations, when both were available (Figure A5).

![](/api/attachments/T4DC32W6/fulltext/images/50c1d13e7d31d844c5c905c93e8e7a23da575d2b49ed7317d850de1b3cfef067.jpg)  
Figure A4. Managing Energy Consumption and Carbon Emissions of a Production Order by Using Estimations

![](/api/attachments/T4DC32W6/fulltext/images/c35076ed3d5f1f87e002c11e244506ff3f005623357d570afe3fb0fb003ba5a7.jpg)  
Figure A5. Comparison of the Energy Consumption (Real/Actual) with the Estimated Values

For the warehousing, distribution and supply chain dimensions, the following scenarios were formulated.

## Scenario 4: Managing Energy Consumption and Carbon Emissions at Three Retail Stores with Different Environmental Profiles and Comparing Them

End users wished to be informed about the energy and carbon efficiency of different stores to identify the most inefficient ones, and to see the energy and carbon efficiency of a specific product or product category and its differentiations across various stores. Figure A6 is a screenshot of the expository instantiation that shows the energy consumption and carbon emission KPIs at the three stores

![](/api/attachments/T4DC32W6/fulltext/images/e3c8347541c6d1517df1cf5243da9f48122cc840ba7be12098b2af1c5b8d5b0b.jpg)  
Figure A6. Managing Energy Consumptions and Carbon Emissions at Three Retail Stores with Different Environmental Profiles and Comparing Them

## Scenario 5: Managing Energy Consumption and Carbon Emissions at Different Distribution Networks and Comparing Them

End users wanted to be informed about the energy and carbon efficiency of a distribution network extending from a central warehouse to all stores and a network extending from a central warehouse to all their delivery points, where an external partner conducted the distribution (Figure A7). They also needed to monitor the energy and carbon efficiency of a specific product/product category and its differentiations among various distribution networks.

![](/api/attachments/T4DC32W6/fulltext/images/48da760165fd532cb91b5253eabbb671512022bf9ef3751820d1270c675d102f.jpg)  
Figure A7. Managing Energy Consumption and Carbon Emissions at Different Distribution Networks and Comparing Them

Scenario 6: Managing Energy Consumption and Carbon Emissions from Supplier’s Warehouse to Retailers’ Stores End users wished to know the carbon emissions across a product life cycle in a network extended from the supplier’s warehouse to retailers’ stores and identify the most inefficient ones (Figure A8).

![](/api/attachments/T4DC32W6/fulltext/images/04d7c68edec3d5938cec918039f8022106b26ed005e8ce3cd8ea67d4f1cf9c26.jpg)  
Figure A8. Managing Energy Consumption and Carbon Emissions from Supplier’s Warehouse to Retailers’ Stores

## About the Authors

Eleni Zampou is a research associate in the Department of Management Science and Technology of the Athens University of Economics and Business and a member of the ELTRUN research group. She has a multidisciplinary educational background that includes computer engineering and informatics, information systems, supply chain management, and environmental sustainability. Her research focuses on digital innovation and transformation in supply chain management and logistics, and she is mainly interested in designing innovative IT solutions and crafting their value propositions. She has twelve years of research and industry experience and has coordinated international research activities in collaboration with major organizations in the areas of retail, supply chain management and logistics, manufacturing, and environmental sustainability. She has also served as a reviewer for several top-tier scientific publications. Her work has been published in various scientific journals, peer-reviewed academic conferences, and books.

Ioannis Mourtos is an associate professor in the Department of Management Science and Technology of the Athens University of Economics and Business and scientific coordinator of the ELTRUN research group. He conducts both theoretical and applied work with a primary focus on mathematical programming and combinatorial optimization. In terms of polyhedral analysis, he has worked on multi-index assignment, stable matchings, matroid parity, and maxcut. In terms of computing, he is mainly interested in integer programming, constraint programming, and their integration. His interests in more applied fields are interdisciplinary and include applications of optimization in manufacturing and transport, along with decision support and the design of related information systems. He is particularly focused on energy-aware information systems and how these encompass the use of elaborate modeling and computing methods to optimize relevant sustainability metrics. He has a broad and diverse publication record, serving also as an ad hoc reviewer for several well-known journals. He enjoys an extensive network of international collaborations and has served as scientific coordinator of EU-wide research projects.

Katerina Pramatari is an associate professor in the Department of Management Science and Technology of the Athens University of Economics and Business and scientific coordinator of the ELTRUN/SCORE research group. She has received various academic distinctions and scholarships and has published more than 100 papers in scientific journals, peer-reviewed academic conferences, and book chapters in, for example, Journal of Retailing, European Journal of Information Systems, Journal of Strategic Information Systems, Journal of Information Technology, Decision Support Systems, etc. She is also heavily involved in the technology transfer domain as a VC partner and in various activities fostering youth entrepreneurship.

Stefan Seidel is a professor and chair of Information Systems and Innovation at the Institute of Information Systems at the University of Liechtenstein and an honorary professor of business information systems at the National University of Ireland, Galway. His research focuses on digital innovation, digital transformation, and artificial intelligence in organizations and society. Stefan’s work has been published in leading journals, including MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Information Technology, European Journal of Information Systems, Communications of the ACM, IEEE Computer, and several others. He is an associate editor for MIS Quarterly.
