---
otero_id: 4906
otero_key: "FJNCMJCK"
title: "Modeling interferences in information systems design for cyberphysical systems: Insights from a smart grid application"
authors: "Tobias Brandt; Stefan Feuerriegel; Dirk Neumann"
year: "2018"
journal: "European Journal of Information Systems"
doi: "10.1057/s41303-016-0030-1"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ESSAY

# Modeling interferences in information systems design for cyberphysical systems: Insights from a smart grid application

Tobias Brandt<sup>1</sup>, Stefan Feuerriegel<sup>2</sup> and Dirk Neumann<sup>2</sup>

<sup>1</sup>Department of Technology and Operations Management, Rotterdam School of Management, Erasmus University, Burgemeester Oudlaan 50, Mandeville (T) Building, Room 9-58, 3062 PA Rotterdam, The Netherlands; <sup>2</sup>Chair for Information Systems Research, University of Freiburg, Freiburg, Germany

Correspondence: Tobias Brandt, Department of Technology and Operations Management, Rotterdam School of Management, Erasmus University, Burgemeester Oudlaan 50, Mandeville (T) Building, Room 9-58, 3062 PA Rotterdam, The Netherlands. Tel: +31 (0) 10 408 1636; E-mail: brandt@rsm.nl

Accepted by DSR special issue editors Ken Peffers, Tuure Tuunanen and Bjo¨rn Niehaves

## Abstract

In this paper, we analyze possible interferences that occur when developing information systems for cyberphysical systems – hybrids containing legacy technical components and added IT modules. In particular, the enhancement of electricity systems through IT components, resulting in smart grid and smart home solutions, is experiencing increasing adoption rates in advanced and developing countries alike. Due to the substantial interdependence with and reliance on often decades-old legacy infrastructure, these cyberphysical systems present particular opportunities and challenges for the associated information systems. We propose that one channel through which information systems improve cyberphysical systems is by enhancing the components of the legacy system with new features. Introducing the Design–Interference Model, we conceptualize IS design for cyberphysical systems and outline possible obstacles and interferences associated with it. Using a simulation experiment for a smart grid application as a showcase, we derive insights into how to address these challenges. We condense these results into actionable advice that, first, seeks to validate existing guidelines for design-oriented research, second, extends and focuses them on cyberphysical system applications and, third, provides guidance to researchers and practitioners in this increasingly relevant area of information system development.

European Journal of Information Systems (2017).doi:10.1057/s41303-016-0030-1

Keywords: design science; cyberphysical Systems; Design–Interference model; smart grid; sustainability

## Introduction

The process of digitization witnessed during the past decades not only creates new services, products, and markets, but also reshapes existing technical systems and infrastructure. Power systems become smart grids, means of transportation become smart mobility, medical devices become augmented surgical tools – technical components in all aspects of life are merged with information technology into cyberphysical systems. Designing information systems for these cyberphysical systems poses additional challenges to IS scholars compared to completely novel applications, since they contain technical components and traditional action patterns inherent to the legacy systems from which they emerge.

While prototypes and pilot studies of many of these cyberphysical systems have been developed over the past decade, such systems have started to become increasingly adopted in everyday use and are continuously tweaked and improved for novel applications. To provide a theoretical foundation for this particular and increasingly relevant facet of IS design science, this paper pursues the following objectives. First, it extends design theory by analyzing how information systems affect cyberphysical systems. For this purpose, we introduce a theoretical model that relates design features of the information system to features of the legacy system, i.e., the power system in a smart grid. We refer to them as Enhancing Features, since they enhance a legacy component by providing a new use that was previously inaccessible. Second, introducing the concept of interferences into the model, we discuss obstacles and challenges faced when designing information systems for cyberphysical systems. In the process, we validate, emphasize, and extend general design science guidelines, thereby providing insights for IS design not only in the context of cyberphysical systems, but also in a more general sense. Third, as a showcase by which to substantiate our propositions, we link the theoretical development to the design of a smart grid application, whose performance and economic impact are evaluated through a simulation experiment.

The remainder of this paper is structured as follows. In ‘‘Related work’’ section, we discuss research related to our work. We introduce our research model and develop the guiding hypothesis in ‘‘Research model’’ section. ‘‘Designing for green synergies’’ section contains the IT artifact and the simulation experiment. We discuss implications from the showcase relating to the achievement of anticipated outcomes through IS design in ‘‘From objectives to outcomes: preventing interferences’’ section. ‘‘Conclusion’’ section concludes with a summary of our analysis and the derived guidelines.

## Related work

Questions relating to the design, creation, and development of information systems have been central to the IS discipline since its inception (Goes, 2014). However, following Hevner et al’s (2004) landmark article in MIS Quarterly, design science has truly established itself as a major research paradigm within the community (Land et al, 2009). Since then, the theoretical foundation of design science research has been further strengthened by a variety of articles, such as those by Hevner (2007), Gregor & Jones (2007), as well as Kuechler & Vaishnavi (2012). A core objective of these and other articles is the advancement and refinement of design theory. As stated by Gregor & Jones (2007), design theory ‘‘provides a sounder basis for arguing for the rigor and legitimacy of IS as an applied discipline’’ (p. 314).

Nevertheless, the concept of design theory is not uncontroversial. For instance, Baskerville & Pries-Heje (2010) outline different perceptions of what a design theory is and is not, lamenting unnecessary complexity and arguing for a more focused and practical definition. They propose a separation between a theory of the design product and a theory of the design process. For the former, they describe a simplified explanatory theory that relates general requirements for a design product to generalized components. While we agree with the necessity of this logical distinction between product and process, our research in this paper focuses particularly on the interaction between design product and design process. Essentially, we analyze how information systems address a certain objective within cyberphysical systems, thereby producing a desired outcome. From these insights, we derive implications regarding the design process that aid in achieving this outcome. Hence, the premise of this paper is that the design product affects the design process, which in turn affects the product. This cyclical nature is often a core element of design theory as can be seen in, for instance, Hevner (2007) and Peffers et al (2007).

While these papers present a macroscopic perspective on IS design, we investigate one particular step in detail. For comparison, the DSRM process model in Peffers et al (2007) provides an evaluation framework for the entire process, from problem identification through development of objectives, design, development, demonstration, and evaluation of the artifact to communication. In this context, we focus specifically on the links between objectives, development, and implementation. Within cyberphysical systems, these stages are particularly complex since IT components are often added to pre-existing legacy systems.

As a representative showcase of such a cyberphysical system, we consider a smart grid application. Smart grids are described as ‘‘a convergence of information technology and communication technology with power system engineering’’ (Farhangi, 2010, p. 19), exemplifying cyberphysical characteristics. In a world facing the threat of man-made climate change (Anderegg et al, 2010; Cook et al, 2013), uncertain supply and accessibility to fossil fuels (Heinberg & Fridley, 2010; Howarth et al, 2011; Owen et al, 2010), as well as a dependence of the energy markets on politically unstable regions of the world (Doukas et al, 2011; Hamilton, 1983), smart grids are considered to be an essential building block of a cleaner, more sustainable energy paradigm. They facilitate the integration of decentralized, renewable energy sources and improve the overall resilience of the power infrastructure (Moslehi & Kumar, 2010). In recent years, smart grids have emerged as a prominent topic of the energy informatics research stream within the IS community (Goebel et al, 2014; Vom Brocke et al, 2013; Watson et al, 2010). In particular, the links between energy consumption behavior, energy management technologies, and economic implications have been a central research focus. For instance, Loock et al (2013) investigate behavioral aspects of the design of energy management systems. Feuerriegel et al (2012) and Feuerriegel & Neumann (2014) analyze the costs and benefits of integrating demand response mechanisms into electricity markets. Gottwalt et al (2011) study the demand reaction of households under flexible energy prices. While these and similar studies often follow design science methodologies, the design of actual smart grid artifacts – that, for instance, implement a specific demand-side management mechanism – lacks a clear theoretical foundation.

Hence, we see the overall contribution of this paper as threefold. With respect to designing for cyberphysical systems, we trace and explain how a design product implements certain design objectives as an outcome. With respect to design science in general, we use these insights to identify possible obstacles within the design process, as well as to validate and extend guidelines to prevent and overcome them. Finally, with respect to smart grid research, our example illustrates an actual smart grid application and provides an economic evaluation of its impact.

## Research model

The design of information systems is generally goaloriented, which is reflected in the affinity between design science and action research (e.g., Kuechler & Vaishnavi, 2012; Papas et al, 2012; Sein et al, 2011). Design artifacts seek to solve or mitigate specific problems; hence, they are associated with a certain anticipated outcome. It is the work of the researcher to translate a stated goal into a set of design objectives that seek to produce this outcome. However, the actua mechanisms that link objectives and eventual outcome vary according to the application domain (cf. Figure 1). We investigate these mechanisms for IS design in cyberphysical systems. As outlined in the previous section, there is already a body of work on design principles that guide general IS research, most famously the guidelines by Hevner et al (2004). However, designing for cyberphysical systems poses additional challenges. For instance, smart grids – the characteristic cyberphysical systems analyzed in this study – are hybrids of information technology and a mix of modern as well as decades-old legacy power infrastructure. Successful design for smart grids, thus, requires a profound understanding of the interactions between the various components of this cyberphysical system and their relationship with the people who are ultimately dependent on a reliable energy supply.

Hence, our objective is to investigate the black box outlined in Figure 1. We consider that one mechanism through which IS design contributes to smart grids is by enhancing components of the power system with new features that were previously unavailable. We will elaborate on this concept in the remainder of this section while we further develop the theoretical model.

![](/api/attachments/FJNCMJCK/fulltext/images/669eec0ac60e697d239a33cf62a66403de741dc792ff337020bc023598e32dbd.jpg)  
Figure 1 Starting point: IS design for the cyberphysical systems.

## Definitions

As part of our study, we discuss outcomes that are produced by information systems. Naturally, this has been extensively researched within the IS community (e.g., Markus & Silver, 2008; Robey et al, 2013; Volkoff & Strong, 2013). Since labels are not always unambiguous in the literature and we are adapting some of them slightly to fit the specifics of our context, we provide short definitions of the constructs used in our model.

Technical object According to Markus & Silver (2008), technical objects include IT artifacts, their components, and their output. In a cyberphysical system, this definition requires further clarification, since it contains various technical objects that may or may not be ITrelated. Since these two types of technical objects are distinctly different, we label them differently. On the one hand, legacy components refer to technical objects that are part of the traditional pre-digitization system, such as power lines, generators, or batteries in a smart grid. In this context, legacy, therefore, refers not necessarily to the age of the components but rather to their constituting a part of the traditional power system. The IT-related technical objects from Markus & Silver’s (2008) definition are captured by the IT artifact construct. It is the core product of the design process and can take various forms, ranging from ‘‘software, formal logic, and rigorous mathematics to informal natural language descriptions’’ (Hevner et al, 2004).

Feature Essentially, a feature is what a technical object does, as opposed to what it is used for. Zammuto et al (2007) provide the example of real-time tracking sensors that indicate when a product has passed a specific stage in the process. Similarly, a feature of a battery would be that it stores energy.

Affordance Contrary to features, affordances identify ‘‘what the user may be able to do with the object, given the user’s capabilities and goals’’ (Markus & Silver, 2008). This reflects the argument by Zammuto et al (2007) that affordances arise from a combination of technological and organizational features. However, Robey et al (2013) note that they are not limited to those purposes the artifact’s designer intended, but are shaped by human agents that use the system ‘‘with their own purposes in mind.’’

Hence, we assume that the designer conceives the IT artifact with certain features. Which affordances arise from this design and whether they achieve the intended outcome depends upon the interaction with the legacy components of the power system on the one hand and with the socio-organizational environment on the other.

## Modeling IS design for a smart grid

The smart grid concept comprises the reinforcement of the conventional power infrastructure with information and communication technology, as well as novel products and services arising from this hybridization. The crucial notion is that smart grids are not built from scratch, but are developed on top of an existing infrastructure. Consider, for instance, smart meters and the service environment emerging around them (Jagstaidt et al, 2011; Loock et al, 2013). They allow customers and utilities to observe the energy consumption of a particular building or device in real time. While they do impart ‘‘smartness’’ to a smart grid, they are only a tiny part of the overall cyberphysical system – the multitudes of generators, transformers, power lines, and wirings remain essentially unchanged. Overall, the smart grid constitutes a complex system that adheres to strict laws of physics and whose stability is vital to all stakeholders.

When designing information systems for smart grids, this complexity and the hybrid nature of the cyberphysical system must be kept in mind. Furthermore, the example of smart meters shows that such information systems often enhance existing infrastructure in some way. As we will show in detail in our showcase example, components in the power grid remain unchanged as such, but acquire new potential uses. This brings us back to Figure 1 and the black box that contains the links between the initial design objectives and the intended outcome. As ‘‘potential uses’’ follow the definition of affordances by Markus & Silver (2008), we are already in the process of uncovering these links, the causal chain that leads from objective to outcome. The designer of the information system may conceive it with certain affordances in mind that would result in an intended outcome. However, these affordances arise from features of legacy components of the power system, which they acquired as a result of a certain functionality of the IT artifact. It is the IT artifact that enhances the components of the power system with additional features and as a result of this combination certain affordances are enabled. Whether these affordances are actualized, or whether the users employ the features for completely unanticipated uses, depends on the socio-organizational environment.

Figure 2 visualizes our reasoning up to this point in a Design–Interference Model (DIM) for cyberphysical systems, which emphasizes the relationship of enhancement between IT artifact and legacy component to enable novel affordances. On the one hand, the objectives of this model are to gain a better understanding of the relationships between the different components within the design product. On the other hand, it seeks to uncover potential obstacles in the functionality of the product and in the preceding design process, illustrated by the possible interferences symbol. Each step is a necessary prerequisite for the one following it. For instance, the enhancing feature of the legacy component that results from the interaction with the IT artifact needs to align with the socio-organizational environment to enable the intended affordance. Similarly, the logic of the IT artifact must reflect the physical restrictions of the legacy component, and the design objectives have to be correctly translated into features of the IT artifact. For a successful implementation, the designer should be aware of these potential obstacles from the beginning. Hence, during the remainder of this paper we will further analyze these interferences to provide suggestions on how to conduct successful design research for smart grids and cyberphysical systems in general.

For this purpose, we proceed in the next section with a showcase that validates and demonstrates the practical application of our model. Later, we outline possible interferences by means of the showcase and suggest measures to address them.

## Designing for green synergies

To further investigate the Design–Interference Model, we consider a smart grid application of IS design. The information system employs an IT artifact that uses synergies between electric mobility and residential renewable energy generation to provide additional financial incentives to households to adopt green technologies. Throughout the course of this section, we will first review the general setting and motivation of the showcase. Afterwards, we will outline the design of the information system, followed by an evaluation of its functionality through a simulation experiment. Throughout the section, we will draw inferences regarding the Design– Interference Model, which are further discussed in the subsequent section.

## Setting and motivation

The application we present seeks to address two sustainability issues society currently faces. These issues concern the increasing need for energy storage due to renewable energy sources on the one hand, and the slow adoption of electric mobility as a more sustainable means of transportation on the other. The information system designed takes advantage of synergies between renewable energy generation and electric mobility to contribute to a solution for both challenges.

Nykamp et al (2012) emphasize that the rising share of intermittent, decentralized, renewable energy sources requires substantial investments into distribution grids if the generation is not matched by simultaneous local demand. As a result, energy storage has become a crucial building block for sustainable power systems, as it detaches consumption from generation. However, storage technologies often exhibit substantial drawbacks, such as high costs (batteries), low efficiency (power-togas), specific geological requirements (compressed air), or a tremendous impact on landscapes and ecosystems (pumped hydro). Hence, the idea of using electric vehicles (EVs) as a swarm of decentralized storage devices has gained significant momentum. Nevertheless, the primary function of the vehicle is mobility and the storage capacity can be considered an additional benefit. Kempton & Tomic´ (2005) have analyzed the technical feasibility of bidirectional energy flows between vehicles and the grid – so-called vehicle-to-grid (V2G) concepts. Various business models building upon these concepts have been proposed, which largely consider fleet operators and aggregators (Brandt et al, 2012; Guille & Gross, 2009; Hill et al, 2012; White & Zhang, 2011). This focus reflects the entry requirements for energy markets, which require a large number of EVs, the reduction in uncertainty caused by this large number of EVs, and possibly scheduled parking times within vehicle fleets. However, the timely realization of these business approaches is questionable, since high prices hamper the public adoption of electric mobility (Al-Alawi & Bradley, 2013). The situation is quite tricky, as using electric vehicles for energy storage could provide owners with revenues that compensate for the high initial costs, yet the realization of these revenues requires a large number of electric vehicles. To solve the immediate problem of low electric mobility adoption rates, households require financial incentives that offset the high initial cost of acquiring an electric vehicle. These incentives must not be dependent on externalities, such as a high adoption rate of electric mobility among the general population.

![](/api/attachments/FJNCMJCK/fulltext/images/1e8902bb0bd7fbfdf7a4120d1c693f2b004b9d5551b79a14ac988d5405212933.jpg)  
Figure 2 Design–Interference model for cyberphysical systems.

We design an IT artifact that seeks to satisfy these requirements by focusing on households that own an electric vehicle as well as a photovoltaic installation. To reflect the impact of renewable energy feed-ins, we add the requirement that the strain on the grid, i.e., the excess feed-ins from photovoltaic generation, needs to be reduced. With respect to the Design–Interference Model, the requirements constitute the anticipated design outcome, which is summarized as follows.

• Financial Incentive. Users receive a financial benefit from using the system that reduces the impact of the high purchase cost of an electric vehicle.

• Reduce Grid Strain. Using the system should decrease the amount of photovoltaic energy fed into the grid, as well as the energy sourced from the grid. Overall, the household should become more energy-autonomous.

• Bottom–Up Solution. The success of the system must not depend on the spread of electric mobility among the overall population. Users must be able to reap the benefits of the information system even if they are the only adopters.

## Information system design

Existing business models that use electric vehicles as storage for intermittent renewable energy generation focus on aggregation schemes, because they assume that these aggregators would enter large-scale energy markets to offer their services. A single EV can offer neither the capacity nor the reliability to compete in the energy market, which is, essentially, the aggregate energy supply. A potentially more useful approach to address intermittent decentralized generation is decentralized storage. We disaggregate the energy supply down to individual generators and consider how more of the energy produced by a specific generator can be used locally. In particular, we focus on residential households that own a rooftop photovoltaic (PV) panel in addition to a pluginhybrid electric vehicle (PHEV). While only a share of potential EV users also own a PV installation, encouraging members of this select group to adopt electric mobility may help to reach the critical threshold of vehicles necessary for business models that provide largescale aggregation.

The underlying intuition behind our approach is that increasing the share of PV energy consumed locally by the household can achieve two of the anticipated design outcomes. The strain on the grid is reduced, since less energy is fed into the grid and the household requires less energy from the grid, as well – it becomes more autonomous overall. Furthermore, residential households generally receive substantially less money for energy they feed into the grid than energy they source from the grid costs them. Hence, an increase in locally consumed PV energy automatically provides a financial benefit if it is matched by a decrease in energy purchased from the utility. The third outcome, the bottom-up aspect, must be included in the system development by design; i.e., at no time during the design process may assumptions on the general adoption of electric mobility be made. The outcomes are to be achieved through an information system that enables smart charging of the electric vehicle while it is plugged in at home. In this context, ‘‘smart charging’’ represents the opposite of ‘‘uncontrolled charging,’’ with the latter implying that the vehicle is plugged in and immediately charged to ful capacity at the maximum power level. Smart charging, on the other hand, refers to the charging (or discharging using V2G-technology) of the vehicle at times and power levels determined by the information system.

Hence, the design objectives to achieve the previously outlined outcomes are, first, the design of an IT artifact that controls the charging of the electric vehicle and, second, the implementation of a charging logic that increases the share of photovoltaic energy consumed by the household. The general functionality of the information system is illustrated in Figure 3 using the constructs from the Design–Interference Model. The DIM outlines what the design product is supposed to do (design objectives), how the product functions (IT artifact, technical object, intended affordance), and what the product eventually delivers (design outcomes). However, by taking a step back from this idealized view of the product’s functionality and considering possible interferences, the DIM allows us to draw inferences regarding the design process, which will be the focus of the penultimate section of this paper.

Figure 3 points out that the design objectives are translated into an IT artifact whose primary feature is the smart charging logic, which is further illustrated in Figure 4. In fixed intervals, the IT artifact receives information on the household demand, PV generation, the status of the PHEV battery, and historical data on the mobility behavior of the users. Based on this information, the artifact decides whether to charge or discharge the vehicle battery (if plugged in), subject to the physical constraints of the system. Due to the high degree of uncertainty associated with the demand and mobility behavior of a single household, the charging logic follows a threshold-based decision strategy instead of an optimization calculus. A detailed description of the implemented decision strategies follows in the next subsection and a complete mathematical formulation can be found in Appendix B.

Figure 3 further outlines that this charging logic enhances the battery of the electric vehicle. In addition to its primary purpose of providing power to the electric motor of the vehicle for traveling, the battery can buffer energy generated by the PV panel and resupply it to the household when needed. This feature – enabled by the IT artifact – allows the user to increase the share of PV energy consumed by the household. This constitutes the intended affordance of the design product and, if realized, results in the accomplishment of all anticipated design outcomes. In the final part of this section, we proceed by outlining the implemented decision strategies and by testing and evaluating the designed system using real-world data.

## Testing and evaluation

The design product is evaluated for two decision strategies in addition to the benchmark scenario (B). The latter addresses the case of uncontrolled charging, i.e., the vehicle starts charging when plugged in and stops when the battery is fully charged. Both decision strategies use a threshold for the state-of-charge of the battery up to which the vehicle is charged using excess photovoltaic energy and, if necessary, energy procured from the grid. Above this threshold, only excess PV energy is used to further charge the battery. Conversely, if the PV generation does not suffice to satisfy the energy demand of the household, the vehicle can discharge energy to supply the household down to the threshold. The only difference between the strategies is that the first strategy (S1) uses a fixed threshold, while the second strategy (S2) recalculates the threshold regularly based on the historical mobility needs of the users. It should be noted that the influence of the threshold is not negligible. If a threshold is chosen that is too low, the energy stored in the battery may not suffice to finish a trip. Since we only consider plugin-hybrid EVs, whose combustion engines can provide the missing range, mobility is not impaired. However, the high price of gasoline compared to electrical energy would substantially decrease the financial benefit of the system to the user. If the chosen threshold is too high, the amount of PV energy that can be buffered is limited, which limits the potential financial benefit, as well.

![](/api/attachments/FJNCMJCK/fulltext/images/7ff1d26ebef59f10e5ce67d5f7185b74bfd7e7cc22199bd49e6244d973847cc3.jpg)  
Visualization of the showcase information system functionality according to constructs of the Design–Interference model

![](/api/attachments/FJNCMJCK/fulltext/images/57f34465b11be29598fb354a3588a0edc3af320e8383c6aa6e066d21c5995ed3.jpg)  
Figure 4 Functionality of the IT artifact.

As this is a conceptual study and V2G-capable vehicles are not yet in series production, we cannot evaluate our artifact using a real-world prototype (Lee et al, 2008) or field study (Pries-Heje & Baskerville, 2008). However, V2G technology is well understood and we use real-world data on the physical constraints to construct a realistic simulation in Matlab. Naturally, the form of the IT artifact in a prototype study is different from the version implemented in the simulation. While the latter is a Matlab script to work with the simulation, the code and functionality can be transformed into, for instance, a mobile device app in a relatively straightforward manner.

The parameters used in the evaluation are summarized in Table 1; the complete model can be found in Appendix A. We consider Germany for this simulation experiment whose retail energy prices are based on data from the German Association of Energy and Water Industries (Bdew, 2011). To ensure the general validity of our results, we correct the prices and revenues for the extensive subsidy scheme currently in place in Germany. We derive the specifications of the PHEV battery from the Chevrolet Volt and base the price of energy from gasoline on the average price for Germany in 2011. We use very conservative values for the maximum charging and discharging rates of the EV, as the explicit objective of our research is to provide a system that is beneficial without extensive technological requirements. Hence, the maximum charging rate relates to a standard residential 220 V/240 V outlet and the maximum discharging rate (V2G) is derived from the values provided by

Table 1 Evaluation parameters

<table><tr><td>Parameter</td><td>Value</td></tr><tr><td>Retail price of energy</td><td>0.2142 € per kWh</td></tr><tr><td>Revenue from PV energy fed into grid</td><td>0.0500 € per kWh</td></tr><tr><td>Price of PV energy consumed by household</td><td>0.0000 € per kWh</td></tr><tr><td>Price of energy from gasoline</td><td>0.4408 € per kWh</td></tr><tr><td>Minimum energy stored in battery</td><td>0 kWh</td></tr><tr><td>Maximum energy stored in battery</td><td>16 kWh</td></tr><tr><td>Maximum charging power of battery</td><td>800 W</td></tr><tr><td>Maximum discharging power of battery</td><td>500 W</td></tr><tr><td>Losses from inversion and other causes</td><td>0.93</td></tr></table>

Mitsubishi for its i-MiEV electric car. The parameter concerning loss from inversion is taken from Kempton & Tomic´ (2005) as this value is still valid for most common inverters. As data sources, we use an original trace of PV generation, taken from a PV installation on a single-family home in Eastern Bavaria throughout 2011. This trace describes PV generation in 5-minute intervals for the entire year. This interval size is subsequently used for all calculations. The demand trace is from a specific German 4-person household as recorded in 2011.

Finally, we evaluate the performance of the information system for three distinct types of users, who are distinguished by their mobility needs. The first type (T1) is an employee working fixed shifts, implying a reliable, repetitive mobility profile. The second type (T2) is a family with fixed schedules on weekdays. The profile is quite repetitive as well, but trips are undertaken at different times and are of different lengths than for the shift worker. The third profile (T3) is, again, for a family, but the trips undertaken are randomized based on mobility profiles taken from the study ‘‘Mobility in Germany, 2008’’ (BMBVS, 2010), which provides a very comprehensive dataset on the mobility needs of the German population. This profile is certainly the most realistic one, but overall the results from all three types should provide an indication and validation of the performance of the information system.

Table 2 provides an overview of the evaluation results for the various household types and strategies. We can observe that for any household type the decision strategies substantially outperform the benchmark values. Furthermore, the strategy with flexible thresholds (S2) consistently performs best, although the difference from the fixed threshold ranges from about 22 euros for the shift worker to 100 euros for the family. The most realistic randomized profile results in an additional cost decrease of about 60 euros over S1.

Table 2 Annual energy costs and annual effect on the grid

<table><tr><td>Type</td><td>Strategy</td><td>Energy cost</td><td>PV energy feed-in</td><td>Energy purchase</td></tr><tr><td rowspan="3">T1</td><td>B</td><td>€467.60</td><td>4,881.05 kWh</td><td>3,322.38 kWh</td></tr><tr><td>S1</td><td>€271.87</td><td>3,571.16 kWh</td><td>2,102.84 kWh</td></tr><tr><td>S2</td><td>€249.52</td><td>3,364.84 kWh</td><td>1,950.36 kWh</td></tr><tr><td rowspan="3">T2</td><td>B</td><td>€701.60</td><td>4,254.90 kWh</td><td>4,268.63 kWh</td></tr><tr><td>S1</td><td>€493.19</td><td>2,828.83 kWh</td><td>2,962.78 kWh</td></tr><tr><td>S2</td><td>€394.94</td><td>2,297.04 kWh</td><td>2,360.63 kWh</td></tr><tr><td rowspan="3">T3</td><td>B</td><td>€410.57</td><td>4,957.91 kWh</td><td>3,074.06 kWh</td></tr><tr><td>S1</td><td>€210.86</td><td>3,565.78 kWh</td><td>1,816.75 kWh</td></tr><tr><td>S2</td><td>€152.58</td><td>3,067.94 kWh</td><td>1,428.11 kWh</td></tr></table>

The evaluation is conducted for households featuring three different mobility types over 1 year. T1 and T2 feature a shift worker and a family, respectively, with fixed recurring mobility patterns. T3 features a family with one working parent and the profile is randomized based on real world data, with overall mobility needs being smaller than for T2. The strategies evaluated are benchmark (B), decision strategy with fixed threshold (S1), and decision strategy with flexible threshold (S2)

If we consider the total cost reduction for T3, the household can decrease the annual energy costs by 258 euros compared to the benchmark. These reductions equal about 2–3 monthly electricity bills for the average German 4-person household every year. For comparison, we consider the federal subsidy for plugin-hybrid EVs in the United States following the American Recovery and Reinvestment Act of 2009. The US government subsidizes a Chevrolet Volt with a tax credit of USD 7,500, which equals about 5,800 euros given current exchange rates. At a marginal tax rate of 30 percent, the actual financial incentive to households is 1,740 euros. This equals about six to seven years of running the information system designed in this study, which is easily within the lifetime of an EV battery. Given current battery prices of 380 euros per kWh (Kihm & Trommer, 2014) – which are projected to decrease – adopting the information system accounts for about a quarter of the initial price difference of 6,000 euros over this time period. Assuming that smart meters measuring household consumption and PV input have already been implemented, investment costs for the information system are negligible since the calculations can be easily made through a smartphone app or the onboard software of the vehicle.

The results in Table 2 also demonstrate that the households become significantly more autonomous. The amount of excess PV energy fed into the grid, as well as the amount of energy procured from the grid, is substantially reduced. Since the PV panel generates energy at levels exceeding the consumption of the household (leading to EV charging) mainly around noon and the early afternoon, i.e., at times when every PV panel is at peak production, this feed-in reduction helps reduce the supply-peak during these times. Similarly, panel c in Figure 5 shows that the vehicle feeds energy back to the household in the morning and evening, reducing the demand peaks at these times. Overall, these dynamics decrease the overall strain on the distribution grid for every household adopting the system.

To conclude this evaluation of the information system presented in this showcase, Figure 5 outlines how the strategies change the composition of the energy supplied to the household for type T3. The benchmark uses only PV and grid supply, but we can observe that PV supply exceeds household demand several times per day (e.g., between 6.30 a.m. and 8.30 a.m.). Particularly during morning hours, this energy is often fed into the grid, since the PHEV is still at full battery. This is already partially compensated when using strategy S1 with a fixed threshold. The PHEV supplies most of the missing energy during the day; only when the battery threshold is reached is the remaining energy sourced from the grid. Panel c in Figure 5 shows the composition of energy supply for strategy S2. The flexible battery threshold eliminates almost any need for energy from the grid during this particular day. For both V2G strategies, the energy supplied by the PHEV battery to the household is then recharged by using excess PV energy or, if necessary, energy from the grid the following day.

Overall, the IT artifact utilizes information on the user’s driving behavior to enhance the battery of the electric vehicle with the feature of buffering photovoltaic energy for later use by the household. Thus, it makes existing synergies between these technologies usable.

## From objectives to outcomes: preventing interferences

In this section, we return to the Design–Interference Model to derive implications pertaining to successful IS research for cyberphysical systems, such as smart grids, from the showcase example we have discussed. As visualized in Figure 2, possible interferences are most likely at the points of contact between the constructs of the model. Consequently, we discuss these points of interference and the lessons learned for future research endeavors.

## Point of interference: From design objectives to the IT artifact

The design process is instantiated by the transformation of the design objectives into a tangible IT artifact. The IS designer defines the eventual design product and considerations of all possible interferences must be incorporated, whether in shaping the artifact, in the relationship with the technical system, or in the behavioral and organizational environment. Interferences at this point are common for all applications of IS design and not limited to a smart grid context. They range from the abstract, such as flaws in the general architecture of the artifact, to the practical, such as coding errors. Guidelines on combating these interferences are outlined in Hevner et al (2004) and the practical example illustrated in this paper corroborates their validity for general designoriented research in IS. With regard to the specific case of designing information systems for cyberphysical systems, we perceive the following three of these guidelines to be of particular relevance due to the nature of those systems.

(a) Benchmark (B)  
![](/api/attachments/FJNCMJCK/fulltext/images/1e28c61a79a5bf68382868e7c98f30dab567cb805377ef478a44c831e670d320.jpg)

(b) Fixed Threshold (S1)  
![](/api/attachments/FJNCMJCK/fulltext/images/73f7d6de82f8d153de73c26e729f8c7b5a49a0188610195e3d85782e0091cdd3.jpg)

(c) Flexible Threshold (S2)  
![](/api/attachments/FJNCMJCK/fulltext/images/3d5b5911fd599c8de7b4a6858b3cf310901d32cf191d7da271c4669466c5705e.jpg)  
Energy supplied by .. ... the grid ... the photovoltaic panel ... the electric vehicle  
Figure 5 Composition of energy supply to household for different strategies.

Design as an Artifact. The importance of this guideline is evident, as we have been discussing IT artifacts throughout this paper. The reasons are twofold. First, cyberphysical systems often affect multiple domains and disciplines, such as electrical engineering (smart grid) or the medical community (smart surgical devices). An IT artifact provides a tangible research result that can reach a large target audience in the scientific community, as well as the general population, without extensive requirements regarding their educational background. The second reason is particularly valid for smart grid research. Energy is ubiquitous, yet invisible; it is crucial to the daily routines of billions of people and the operations of countless companies. Designing as an artifact enables researchers to better communicate how the research results will affect daily personal and corporate ‘‘energy experiences.’’ For instance, in the context of our showcase, we can present the designed artifact as an application that decreases annual energy costs without impeding mobility or daily activities.

Design Evaluation. As we have outlined, cyberphysical systems are in certain ways more complex than many other applications of IS design. This results from the inclusion of technical legacy components that may be unfamiliar to the IS researcher. Even in interdisciplinary research teams, this may lead to unexpected performance deviations by the design product. Rigorous evaluation is indispensable and should be executed at multiple stages of the design process, if practicable. Successful examples range from evaluating the theoretical conception via a mathematical formulation of the expected outcomes, and evaluating pre-implementation through simulation using real-world data as conducted in our showcase, to post-implementation evaluation using field studies.

Design as a Search Process. The complexity of smart grid research prevents many solutions from being immediately, or even after some consideration, evident. For instance, it is frequently assumed that individual electric vehicles cannot effectively provide energy storage without some measure of aggregation. In our showcase, we demonstrate that the former can be achieved by scaling down the target system and by foregoing an optimization calculus for thresholdbased decision strategies. However, finding this kind of solution requires letting go of preconceived notions and searching for what works instead of merely what one wants to work.

## Point of interference: From the IT artifact to the legacy component

The point of interference between the IT artifact and the legacy component is particularly relevant for information systems in cyberphysical systems, such as smart grids. We want to outline two major sources of interferences in this context and guidelines on how to avoid them. First, the physical system might not interact with and react to the IT artifact as expected. For instance, in our simulation experiment we assume that the EV battery is fully dischargeable. However, this kind of deep discharge may result in a much shorter lifespan of the battery. We omitted such lifespan issues in our showcase simply because in the proposed scenarios, the charging strategies never caused additional deep charging incidents and the inclusion of such effects on the battery would unnecessarily complicate the paper. Nonetheless, it is important that we be aware of such potential issues, leading to our first additional guideline.

Comprehend the Legacy System. It is vital that the cyberphysical system is well understood by the researchers. Questions of sustainability and the smart grid as an aspect of this broad field are inherently interdisciplinary and require knowledge from various fields to tackle. While successful IS design for cyberphysical systems does not necessarily require interdisciplinary teams, the researchers involved should have a thorough understanding of the technical and behavioral aspects of the associated domains. Furthermore, for this research to have an impact beyond the IS discipline, this understanding must be communicated in the relevant articles and publication outlets must allow researchers space to communicate it in some form in their papers. Lastly, comprehension of the system is necessary to find synergies between different technologies within the system, to design information systems that enhance existing components and allow them to provide more benefits.

The second source of interferences, but also of opportunities, at the link between the IT artifact and the legacy component is particularly applicable to smart grids and results from the fact that power systems are networks. What works for an individual application might end up destabilizing the system if it is adopted by many users. On the other hand, the full benefit of a certain IT artifact may only be realizable once many users adopt it. This concern is articulated in our second guideline.

Consider Network Effects. Designers must be aware of the impact, as well as the attainability, of network effects within the cyberphysical system. Consider the research undertaken in our showcase. The motivation was network effects – the ability of many electric vehicles to serve as energy storage for intermittent energy generation from renewable sources. However, what further guided our search process was the fact that these network effects are currently unattainable, due to the lacking adoption rates of electric mobility. Green Synergies, i.e., the interaction between various green technologies, such as photovoltaics and electric mobility, are also a kind of network effect, although not in the most classical sense. However, they arise from a holistic perspective on the complete system, which is indispensable for successful IS design in cyberphysical systems.

## Point of interference: From enhancing features to enhancing affordances

The step from feature to affordance is a core subject of Information Systems research and fully discussing it in light of our model and showcase could easily fill another paper. Questions, such as ‘‘How do you get the user to use the artifact for the intended purpose?’’ and ‘‘Which potential uses materialize that the designer did not anticipate, for better or for worse?’’ are of crucial importance to IS research of any kind. Unintended affordances that are frequently discussed in the context of smart grids relate to privacy issues, since smart meters may open the door to potential intruders and abusers. However, privacy issues are also relevant to any information system implementation. Instead, this final guideline captures an obvious feature of the information system in our showcase at the intersection between the technical system and the resulting affordances – the role of the user is marginal. In fact, information on all relevant behavior is collected by sensors, such as smart meters or the IT of the electric vehicle. Essentially, the user has only to acquire the system and thereafter its operations are completely automated. Hence, some might question the fit of this system with the general orientation of IS research. We disagree, since minimizing the reliance on the user was a conscious decision on the part of the designers and the role and influence of the user are questions that must be asked in IS design in general, but in complex cyberphysical systems in particular. Yet who is better equipped to tackle this question than IS researchers?

Without doubt, there is potential for a more explicit user interaction with the system to improve the results and increase the financial benefits as well as the energy autonomy of the household. If users supply information on future trips, the critical threshold of the battery can be tuned to finer levels, maximizing the enhancing feature of the battery to buffer photovoltaic energy. However, this potential improvement must be considered in light of the probable price. First, increasing user interaction requires a user interface, which increases development time and costs, as well as potentially raising the cost of the system to the end-user. Second, we need to ask whether the user can provide information that will substantially improve outcomes. Trips are often undertaken spontaneously and it is unclear whether an optimization based on incorrect predictions results in an actual improvement. Third, we need to ask whether the user is willing to provide the necessary information, whether he will use the system in the way the designer intended. While the overall financial benefit of the system is quite large, the daily revenues are around one euro. It is questionable whether this is a sufficient incentive to urge users to report their future trips to the system. The careful consideration of these facts led us to minimizing the role of the user in our showcase. While this by no means implies that the user must always be marginalized in smart grid information systems, it leads us to our final guideline.

![](/api/attachments/FJNCMJCK/fulltext/images/27ebd7df988497aec43f9ef6b79eeb7fc24dadbe13e2ca4c7e6a5fb019614308.jpg)  
CYBERPHYSICAL SYSTEM (SMART GRID)  
Figure 6 Design–Interference model with guidelines to prevent interferences.

Question the Role of the User. Cyberphysical systems are complex and exposing users to this complexity may be overwhelming. There is no general rule on how much user interaction with the technical system is optimal, but it is important to be open-minded on the one hand and critical on the other.

## Conclusion

In this paper, we have investigated the design of information systems for cyberphysical systems using the showcase of a smart grid application. We have introduced the Design–Interference Model for Cyberphysical Systems, which analyzes the design product including antecedents (the design objectives) and impact (the design outcomes). Furthermore, it provides insights into the sources of possible interferences in the design process and in the functionality of the product.

We propose that one central way in which information systems contribute to cyberphysical systems is by enhancing components of the legacy system. We substantiate this claim using as a showcase an information system that enhances the battery of an electric vehicle. However, the concept of enhancing features can also be observed in other applications of smart metering and smart grids (e.g., Katz et al, 2011).

By analyzing the showcase in light of the Design– Interference Model, we derive a set of guidelines for IS research for cyberphysical systems. These validate rules set forth by Hevner et al (2004) regarding general design science projects, emphasizing three that are considered exceedingly important when designing for cyberphysical systems. As illustrated in Figure 6, this includes designing as an artifact, design evaluation, and design as a search process. Furthermore, to prevent possible interferences associated with the legacy systems, we propose three additional guidelines of comprehending the legacy system, considering network effects, and questioning the role of the user. The technical complexity of cyberphysical systems corroborates the outstanding relevance of the precepts when designing for such systems. Nevertheless, these guidelines are relevant to differing degrees in a broader design science context, as well. For instance, network effects and considerations frequently play a critical role when designing social media applications. Hence, we consider the application of the Design–Interference Model and the extension of the aforementioned guidelines to design science applications outside the focus of cyberphysical systems to be a promising area for future research.

## Acknowledgements

The authors would like to express their gratitude to three anonymous reviewers and to the guest editors for their constructive feedback and valuable suggestions. The authors also thank the Solar-Institut Ju¨lich, University of Applied Sciences Aachen, Germany for contributing data on household demand.

## About the Authors

Tobias Brandt is assistant professor of Business Information Management at Rotterdam School of Management, Erasmus University. His research focuses on the digital economy, energy informatics, and data analytics. He has received best paper awards at ICIS and HICSS and his articles have appeared in the JMIS, BISE, and Omega.

Stefan Feuerriegel is research associate at the University of Freiburg, Germany, with a focus on data mining and business analytics. He holds a Master of Science in Simulation Sciences from the RWTH Aachen University

## References

AL-ALAWI BM and BRADLEY TH (2013) Total cost of ownership, payback, and consumer preference modeling of plug-in hybrid electric vehicles. Applied Energy 103, 488–506. doi: 10.1016/j.apenergy.2012.10.009.

ANDEREGG WRL, PRALL JW, HAROLD J and SCHNEIDER SH (2010) Expert credibility in climate change. Proceedings of the National Academy of Sciences of the United States of America 107(27), 12107–12109. doi: 10.1073/pnas.1003187107.

BASKERVILLE RL and PRIES-HEJE J (2010) Explanatory design theory. Business & Information Systems Engineering 2(5), 271–282.

BDEW (2011) Costs of Renewable Energies Continue to Rise Moderately. Berlin.

BMBVS (2010) Mobility in Germany, 2008, Bonn, Berlin.

BRANDT T, WAGNER S AND NEUMANN D (2012) Road to 2020: IS-Supported Business Models for Electric Mobility and Electrical Energy Markets. ICIS 2012 Proceedings.

COOK J, NUCCITELLI D, GREEN SA, RICHARDSON M, WINKLER B, PAINTING R, WAY R, JACOBS P and SKUCE A (2013) Quantifying the consensus on anthropogenic global warming in the scientific literature. Environmental Research Letters 8(2), 24024. doi: 10.1088/1748-9326/8/2/024024.

DOUKAS H, FLAMOS A and PSARRAS J (2011) Risks on the Security of Oil and Gas Supply. Energy Sources, Part B: Economics, Planning, and Policy 6(4), 417–425. doi: 10.1080/15567240903047442.

FARHANGI H (2010) The path of the smart grid. IEEE Power and Energy Magazine 8(1), 18–28. doi: 10.1109/MPE.2009.934876.

FEUERRIEGEL S and NEUMANN D (2014) Measuring the financial impact of demand response for electricity retailers. Energy Policy 65, 359–368, doi: 10.1016/j.enpol.2013.10.012.

FEUERRIEGEL S, STRU¨KER J and NEUMANN D (2012) Reducing price uncertainty through demand side management. ICIS 2012 Proceedings.

GOEBEL C, JACOBSEN H, RAZO V, DOBLANDER C, RIVERA J,ILG J, FLATH C, SCHMECK H, WEINHARDT C, PATHMAPERUMA D, APPELRATH H, SONNENSCHEIN M, LEHNHOFF S, KRAMER O, STAAKE T, FLEISCH E, NEUMANN D, STRU¨KER J,EREK K, ZARNEKOW R, ZIEKOW H and LA<sup>¨</sup>SSIG J (2014) Energy informatics. Business & Information Systems Engineering 6(1), 25–31. doi: 10.1007/s12599- 013-0304-2.

GOES P (2014) Editor’s Comments: Design Science Research in Top Information Systems Journals. Management Information Systems Quar terly 38(1), iii–viii.

GOTTWALT S, KETTER W, BLOCK C, V J and WEINHARDT C (2011) Demand side management—A simulation of household behavior under variable prices. Energy Policy 39(12), 8163–8174. doi: 10.1016/j.enpol.2011. 10.016.

GREGOR S and JONES D (2007) The anatomy of a design theory. Journal of the Association for Information Systems 8(5), 312.

GUILLE C and GROSS G (2009) A conceptual framework for the vehicle-togrid (V2G) implementation. Energy Policy 37(11), 4379–4390. doi: 10. 1016/j.enpol.2009.05.053.

H JD (1983) Oil and the macroeconomy since World War II. Journal of Political Economy 91(2), 228–248. doi: 10.2307/1832055.

and his articles have appeared in EJOR, Energy Policy, and the Journal of Decision Systems.

Dirk Neumann is full professor of Information Systems at the University of Freiburg, Germany. His research centers on digitization and novel uses of information systems in industry and society. His articles have been published in JMIS, ACM Transactions in Internet Technology, Communications of the ACM, EJOR, and others.

HEINBERG R and FRIDLEY D (2010) The end of cheap coal. Nature 468(7322), 367–369. doi: 10.1038/468367a.

HEVNER A (2007) A three cycle view of design science research. Scandinavian Journal of Information Systems 19(2), 4.

HEVNER A, MARCH S, PARK J and RAM S (2004) Design science in information systems research. Management Information Systems Quarterly 28(1), 75–105.

HILL DM, AGARWAL AS and AYELLO F (2012) Fleet operator risks for using fleets for V2G regulation. Energy Policy 41, 221–231. doi: 10.1016/j. enpol.2011.10.040.

HOWARTH RW, INGRAFFEA A and ENGELDER T (2011) Natural gas: should fracking stop? Nature 477(7364), 271–275. doi: 10.1038/ 477271a.

JAGSTAIDT U, KOSSAHL J and KOLBE L (2011) Smart metering information management. Business & Information Systems Engineering 3(5), 323-326.

KATZ RH, CULLER DE, SANDERS S, ALSPAUGH S, CHEN Y, DAWSON-HAGGERTY S, D P, H M, J X, K L, K A,L K, O J, M P, R E, T J, H J and S S (2011) An information-centric energy infrastructure: the berkeley view. Sustainable Computing: Informatics and Systems 1(1), 7–22. doi: 10.1016/j.suscom.2010.10. 001.

KEMPTON W and TOMIC´ J (2005) Vehicle-to-grid power fundamentals: calculating capacity and net revenue. Journal of Power Sources 144(1), 268–279. doi: 10.1016/j.jpowsour.2004.12.025.

Kı A and TromMER S (2014) The new car market for electric vehicles and the potential for fuel substitution. Energy Policy 73, 147–157. doi: 10. 1016/j.enpol.2014.05.021.

KUECHLER W and VAISHNAVI V (2012) A framework for theory development in design science research: multiple perspectives. Journal of the Association for Information Systems 13(6), 395.

L F, L C, A A, C E, H A M G (2009) ICIS 2008 Panel report: design science in information systems: hegemony, bandwagon, or new wave? Communications of the Association for Information Systems 24(1), 29.

L J, W G and P B (2008) Process grammar as a tool for business process design. Management Information Systems Quarterly 32(4), 757–778.

LOOCK C, STAAKE T and THIESSE F (2013) Motivating energy-efficient behavior with green IS: an investigation of goal setting and the role of defaults. Management Information Systems Quarterly 37(4), 1313–1332.

M ML and S M (2008) A foundation for the study of IT effects: a new look at DeSanctis and Poole’s concepts of structural features and spirit. Journal of the Association for Information Systems 9(10), 609.

M K and K R (2010) A reliability perspective of the smart grid. IEEE Transactions on Smart Grid 1(1), 57–64. doi: 10.1109/TSG.2010. 2046346.

$\mathsf { D } _ { \mathsf { t } }$ Household demand in period t $\mathsf { B } _ { \sf t }$ Energy stored in battery at end of period t $\mathsf { M } _ { \mathrm { t } }$ Energy reguired for mobility in period t $\mathsf { H } _ { \mathrm { t } }$ Energy supplied by hybrid motor in period t

NYKAMP S, MOLDERINK A, HURINK JL and SMIT GJ (2012) Statistics for PV, wind and biomass generators and their impact on distribution grid planning. Energy 45(1), 924–932. doi: 10.1016/j.energy.2012.06. 067.

OWEN NA, INDERWILDI OR and KING DA (2010) The status of conventiona world oil reserves—Hype or cause for concern? Energy Policy 38(8), 4743–4749. doi: 10.1016/j.enpol.2010.02.026.

PAPAS N, O’KEEFE RM and SELTSIKAS P (2012) The action research vs design science debate: reflections from an intervention in eGovernment. European Journal of Information Systems 21(2), 147. doi: 10.1057/ejis. 2011.50.

PEFFERS K, TUUNANEN T, ROTHENBERGER MA and CHATTERJEE S (2007) A design science research methodology for information systems research. Journal of Management Information Systems 24(3), 45–77. doi: 10. 2753/MIS0742-1222240302.

PRIES-HEJE J and BASKERVILLE RL (2008) The design theory nexus. Management Information Systems Quarterly 32(4), 731–755.

ROBEY D, ANDERSON C and RAYMOND B (2013) Information technology, materiality, and organizational change: a professional odyssey. Journal of the Association for Information Systems 14(7), 379.

SEIN M, HENFRIDSSON O, PURAO S, ROSSI M and LINDGREN R (2011) Action design research. Management Information Systems Quarterly 35(1), 37–56.

V O and S D (2013) Critical realism and affordances: theorizing IT-associated organizational change processes. Management Information Systems Quarterly 37(3), 819–834.

V B J, W R, D C, E S and M N (2013) Green information systems: directives for the IS discipline. Communications of the Association for Information Systems 33(1).

WATSON R, BOUDREAU M and CHEN A (2010) Information systems and environmentally sustainable development: energy informatics and new directions for the IS community. Management Information Systems Ouarterly 34(1). 23–38.

WHITE CD and ZHANG KM (2011) Using vehicle-to-grid technology for frequency regulation and peak-load reduction. Journal of Power Sources 196(8), 3972–3980. doi: 10.1016/j.jpowsour.2010.11.010.

ZAMMUTO RF, GRIFFITH TL, MAJCHRZAK A, DOUGHERTY DJ and FARAJ S (2007) Information technology and the changing fabric of organization. Organization Science 18(5), 749–762. doi: 10.1287/orsc. 1070.0307.

## Appendix A: Physical system

Figure 7 illustrates the components of and the possible energy flows within the physical system controlled by the information system. The IT artifact determines its charging decisions using 5-minute intervals. The household and mobility needs are pure consumers, while the photovoltaic panel and the hybrid motor of the vehicle are pure suppliers of energy. The battery and the distribution grid can consume or supply energy within their physical limits.

Table 3 outlines the resulting constraints on the physical system, which have to be satisfied in each period t. The parameter $\beta$ indicates whether the vehicle is plugged in at home (1) or not (0). The parameter a represents losses from inversion.

Finally, the total cost of energy in period t is calculated as

$$
C _ {\mathrm{t}} = p _ {\mathrm{r}} \left(G B _ {\mathrm{t}} + G D _ {\mathrm{t}}\right) + p _ {\mathrm{f}} P G _ {\mathrm{t}} + p _ {\mathrm{c}} \left(P B _ {\mathrm{t}} + P D _ {\mathrm{t}}\right) + p _ {\mathrm{g}} H B _ {\mathrm{t}}
$$

with ${ p } _ { \mathrm { r } }$ as the retail price of energy, $\textstyle p _ { \mathrm { f } }$ as the price of PV energy fed into the grid (generally negative, as it is a revenue of the household), $ { p _ { \mathrm { c } } }$ as the price of PV energy consumed by the household (equal to zero in the showcase, may be negative in certain subsidy schemes), and $p _ { \mathrm { g } }$ as the price of gasoline.

![](/api/attachments/FJNCMJCK/fulltext/images/7754393693d36c509eef7119cc855027aef461746a383f0efb2358489bab9c9e.jpg)  
$\mathsf { G } _ { \mathtt { t } }$ Grid supply or demand in period t  
$\mathsf { P _ { t } }$ Photovoltaic generation in period t $\mathsf { X Y } _ { \mathfrak { t } }$ Energy flow from X to Y in period t

Figure 7 Schematic representation of physical system.

## Table 3 Constraints on physical system

The household demand must be satisfied, either by PV energy, grid energy, or energy supplied by the PHEV if it is plugged in $D _ { t } = P D _ { t } + G D _ { t } + \beta _ { t } B D _ { t }$

All energy generated by the PV installation must be distributed somewhere, either the household, the grid, or the plugged-in PHEV

$$
P _ {t} = P D _ {t} + P G _ {t} + \beta_ {t} P B _ {t}
$$

The net position of the grid is energy supplied to household and PHEV minus the energy received from the PV panel

$$
G _ {t} = G D _ {t} + \beta_ {t} G B _ {t} - P G _ {t}
$$

The change of the state-of-charge of the battery within period t is either energy supplied by the grid or the PV panel minus the energy supplied to the household (if the vehicle is plugged in) or the energy supplied by the hybrid motor minus the energy required for mobility (if the vehicle is not plugged in)

$$
B _ {t} - B _ {t - 1} = \beta_ {t} \left[ \alpha P B _ {t} + \alpha G B _ {t} - \frac {1}{\alpha} B D _ {t} \right] + (1 - \beta_ {t}) [ H B _ {t} - B M _ {t} ]
$$

Mobility needs must be satisfied

$$
M _ {t} = B M _ {t}
$$

All energy from the hybrid motor goes to the battery $H _ { t } = H B _ { t }$

The variables are limited to the following ranges. In addition, the state-of-charge of the battery must be within the range defined by the minimum and the maximum state-of-charge. Charging and discharging of the battery are limited by the maximum charge and discharge rates, respectively

$$
D _ {t}, P _ {t}, M _ {t}, H _ {t}, P D _ {t}, G D _ {t}, B D _ {t}, P G _ {t}, P B _ {t}, G B _ {t}, H B _ {t}, B M _ {t} \geq 0,
$$

$$
0 <   \alpha \leq 1, \beta_ {t} \in \{0, 1 \}, B _ {\text { MIN }} \leq B _ {t} \leq B _ {\text { MAX }},
$$

$$
\frac {1}{\alpha} B D _ {t} \leq B _ {\text { OUT }}, \alpha (P B _ {t} + G B _ {t}) \leq B _ {\text { IN }}
$$

## Appendix B: Implemented strategies

The additional constraints that must be satisfied for the benchmark are outlined in Table 4, while the constraints for the V2G strategies are listed in Table 5. As previously mentioned, both strategies follow the same logic; their

## Table 4 Constraints for benchmark (B)

There is no energy flow from the vehicle to the household BD ¼ 0

The first priority of PV generation is to satisfy household demand PD<sub>t</sub> ¼ min P<sub>t</sub> ; D<sub>t</sub>½ 

The remaining PV energy is used to charge the PHEV, if plugged in, until the battery is fully charged

$$
P B _ {t} = \beta_ {t} \min [ \max [ P _ {t} - P D _ {t}, 0 ], B _ {\text { MAX }} - B _ {t - 1} ]
$$

If plugged in, the PHEV is charged at maximum power

$$
P B _ {t} + G B _ {t} = \beta_ {t} \min \left[ B _ {\mathrm{IN}}, B _ {\mathrm{MAX}} - B _ {t - 1} \right]
$$

## Table 5 Constraints for decision strategies (S1 and S2)

The first priority of PV generation is to satisfy household demand $P D _ { t } = \mathrm { m i n } [ P _ { t } , D _ { t } ]$

If plugged in and battery level is below critical threshold, the PHEV is charged at maximum power. Otherwise, only excess PV energy is used until the battery is fully charged

$$
P B _ {t} + G B _ {t} = \left\{ \begin{array}{l l} \beta_ {t} B _ {\text { IN }} & \text { if   } B _ {t - 1} \leq B _ {\text { crit }} \\ \beta_ {t} \min [ \max [ P _ {t} - P D _ {t}, 0 ], B _ {\text { MAX }} - B _ {t - 1} ] & \text { otherwise } \end{array} \right..
$$

If plugged in and battery level is above critical threshold, remaining household demand is supplied by EV until either maximum power or critical threshold is reached

$$
B D _ {t} = \left\{ \begin{array}{l l} \beta_ {\mathrm{t}} \min [ D _ {t} - P D _ {t}, B _ {t - 1} - B _ {\text { crit }}, B _ {\text { OUT }} ] & \text { if   } B _ {t - 1} > B _ {\text { crit }} \\ 0 & \text { otherwise } \end{array} \right.
$$

only difference lies in the calculation of the threshold state-of-charge of the battery, $B _ { \mathrm { c r i t } }$ . While this value is fixed for S1, it is permanently recalculated for S2 based on the historical mobility needs of the users.
