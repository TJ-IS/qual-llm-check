---
otero_id: 25588
otero_key: "A3ZH8E4G"
title: "Improving the state-tracking ability of corona dashboards"
authors: "Jan Recker"
year: "2021"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2021.1907235"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Improving the state-tracking ability of corona dashboards

Jan Recker

To cite this article: Jan Recker (2021): Improving the state-tracking ability of corona dashboards, European Journal of Information Systems, DOI: 10.1080/0960085X.2021.1907235

To link to this article: https://doi.org/10.1080/0960085X.2021.1907235

![](/api/attachments/A3ZH8E4G/fulltext/images/18fedc800dfcab1dbc2d3e0537a871eaee28f01182dcec5b641982bcbc6443b7.jpg)

Published online: 20 Apr 2021.

![](/api/attachments/A3ZH8E4G/fulltext/images/5b3c93917f456dac62eb62fc4133f15f6fcb4f91e4dceaf2ed0f48f0355b111b.jpg)

Submit your article to this journal

![](/api/attachments/A3ZH8E4G/fulltext/images/139361ceb0fff661d6c7f0c8d54c107a8fb16d56238e8d1f9d1c76ff4cf98d5e.jpg)

Article views: 124

![](/api/attachments/A3ZH8E4G/fulltext/images/5baeb79831a813ba006fa2be20bc9b1cb423bf285b2fd16b831ce399492cd81b.jpg)

View related articles

![](/api/attachments/A3ZH8E4G/fulltext/images/a389be65d4ea0e076c7f54a6e550f626ebcaf4506c1c135d53e20ed15d880b2a.jpg)

View Crossmark data

ARTICLE

Check for updates

# Improving the state-tracking ability of corona dashboards

Jan Recker

University of Hamburg, Hamburg Business School, Hamburg, Germany

## ABSTRACT

Corona dashboards are interactive geospatial information systems used by billions of users to help them understand the evolution of the COVID-19 pandemic. I use a representational lens to explore how these systems can be made more useful. With this lens, the usefulness of these systems to convey information about the pandemic fundamentally depends on whether these systems are implemented as representation or state-tracking systems. I suggest that corona dashboards presently focus disproportionally on representing socially constructed properties (infection rates, deaths, levels of vaccination) of various things such as people, regions, or countries. They would become more useful if they additionally focused on tracking events (such as policy implementations) and changes in states (such as capacities of lockdown wards, usage of face masks). By applying a methodology for design science research involving design archaeology, I analyse the in situ implementation of Germany’s RKI COVID-19-Dashboard, develop new design principles to extend the state-tracking abilities of corona dashboards, and explore the importance, actability, and efectiveness of these design principles through an empirical case study. The contributions this paper makes are new and validated design principles for new feature implementations that can help making corona dashboards more efective and useful.

ARTICLE HISTORY

Received 24 June 2020

Accepted 16 March 202

KEYWORDS

Geospatial information

systems; dashboard;

representation; state-

tracking; design principles;

design science research

## 1. INTRODUCTION

“We built this dashboard because we think it is important for the public to have an understanding of the outbreak situation as it unfolds with transparent data sources.”

Lauren Gardner (Co-director, Johns Hopkins Center for Systems Science and Engineering)

After the local outbreak of COVID-19 in Wuhan (Hubei, China) in December 2019, the virus spread throughout China and 27 other countries by February 2020. The first European case was reported in France on January 24 2020. On January 30 2020, the World Health Organization declared the COVID-19 outbreak a global public health emergency.

This trajectory was accompanied by the development of a new type of information system (IS), an online interactive dashboard that displays the location and number of confirmed COVID-19 cases, deaths, and recoveries for afected regions on a geospatial map (Dong et al., 2020). One of the first such dashboards was made public by the Center for Systems Science and Engineering at Johns Hopkins University (https:// coronavirus.jhu.edu/map.html) on January 22 2020. Similar dashboards, such as Germany’s RKI COVID-19-Dashboard (https://corona.rki.de), or the WHO Coronavirus Disease Dashboard (https://covid19. who.int/), followed soon after. Since the onset of COVID-19, these dashboards have been used not only by policymakers (Lazzerini & Putoto, 2020) and health professionals (Reeves et al., 2020) but also by billions of citizens worldwide (K Rogers, 2020; Staford, 2020) as they seek information about the outbreak of the virus and attempt to make sense of new regulations and measures taken by governments that afect them.

These “corona dashboards” illustrate an important role that IS play in handling global crisis situations: that of representation. Representation is fundamental to understanding a crisis and managing it (Adam, 2020b). As the outbreak evolved, a manual reporting process quickly became unsustainable. As the virus spread across Chinese regions, then Asian countries, then continents, it became impossible to track cases through direct observation without the help of IS that would collect, aggregate, and report digital data streams from a variety of sources.

Of course, representation is not the only role of IS in global crisis situations. Since the onset of the COVID-19 pandemic, we have come to witness how IS are designed and used to enable contact tracing (Trang et al., 2020), telework (Carillo et al., 2021), virtual collaboration (Waizenegger et al., 2020), crowd monitoring (Adam et al., 2020), contagion control (Urbaczweski & Lee, 2020), or analytics (Pietz et al., 2020). At the same time, IS are also involved in issues surrounding the pandemic, such as cybercrime (Naidoo, 2020), cyberchondria (Laato et al., 2020), or fake news (O’Connor & Murphy, 2020).

While studies such as the above have dealt with these roles, positive and negative, there is little work that has focused on the most basic but perhaps also most fundamental role of how to represent information about the COVID-19 pandemic. This is puzzling because IS research has dealt with fundamental questions of representing and modelling information since the dawn of the discipline (e.g., Batra & Antony, 1994; Kent, 1978; Langefors, 1973; Y Rogers, 1986; Stamper, 1971; Wand & Weber, 1990). Our field possesses an excellent repertoire to reason about representation and how to make information systems more efective (Burton-Jones & Grange, 2013; Burton-Jones et al., 2017).

My proposition is that the presently available corona dashboards are not efective as they could be because they mainly provide functionality for representation<sup>1</sup> but not state-tracking.<sup>2</sup> The key insight here is that a pandemic, the worldwide spread of a virus (World Health Organization, 2010), is neither an object nor an event but instead a process, a progression of events and actions that unfolds over time (Abbott, 2016; Tsoukas & Chia, 2002). To understand the process, we must track changes in states and the events that cause these (e.g., changes in infection rates, implementations of non-pharmaceutical interventions such as lockdowns, or breakthroughs in the development of pharmaceutical interventions such as medications or vaccines), instead of only representing things and their properties (e.g., the number of infected people in diferent countries and their mortality rates), which are the momentary consequences of such events and actions.

To expand on this basic proposition, I follow guidelines for research conduct (Pefers et al., 2007) and artefact analysis (Chandra Kruse et al., 2019) from the design science research tradition (Hevner et al., 2004). I proceed as follows: I first introduce the research context, corona dashboards. I then explain my research approach. Next, I analyse a situated implementation of corona dashboards, Germany’s RKI COVID-19-Dashboard (https://corona.rki.de), and then develop design principles that extend the statetracking ability of corona dashboards by drawing on ideas from representation theory (Weber, 1997). I then report on findings from an empirical case study that has the aims to evaluate the design principles suggested in terms of importance, actability, and efectiveness (Iivari et al., 2020) and to explore why and how design principles are implemented in the in situ dashboard, or not. I conclude with a discussion of findings, implications, and limitations. The main contribution of this article is that it reports the first artefactual and empirical study (Ågerfalk & Karlsson, 2020) of corona dashboards, the most frequently used type of IS during the Covid-19 pandemic (K Rogers, 2020).

## 2. RESEARCH CONTEXT: GEOSPATIAL INTERACTIVE DASHBOARDS TO TRACK THE OUTBREAK OF THE COVID-19 VIRUS

Corona dashboards are geospatial interactive information systems that semi-automatically collect and display information about the existence and spread of the Covid-19 pandemic. These dashboards were developed with the aim to “provide researchers, public health authorities, and the general public with a userfriendly tool to track the outbreak as it unfolds” (Dong et al., 2020, p. 533).

Corona dashboards exist in a variety of formats (Datta, 2020) but most of them, including Germany’s RKI COVID-19-Dashboard, the COVID-19 Global Map in the US, or the WHO Coronavirus Disease (COVID-19) Dashboard, are representationally similar. They use a variety of attributes, such as cumulative cases, recoveries, new infections, or reported deaths, to represent the pandemic. They present these attributes geospatially, for example, by country, region, or city. Many popular corona dashboards rely on the same technology, ArcGIS (Esri, 2020), a cloud-based mapping, analysis, and data storage system, that can be used to create, share, and manage maps, scenes, layers, apps, and other geographic content (Scott & Janikas, 2010).

In what follows, my focus is specifically on one implementation of corona dashboards in Germany, the RKI COVID-19-Dashboard, which displays data provided by the Robert-Koch-Institut (RKI), Germany’s main public health institute and one of the oldest biomedical research institutes in the world. In Germany, the RKI plays a central role in the national strategy for responding to the pandemic outbreak (Staford, 2020). The RKI is responsible for nationwide health monitoring and health reporting of the federal government. Furthermore, it collects and interprets epidemiological data as a result of the Protection against Infection Act (Infektionsschutzgesetz, IfSG).

Figure 1 presents an annotated screenshot of Germany’s RKI COVID-19-Dashboard. The dashboard is divided into five main representation elements from top to bottom and left to right. It reports three key figures, infections, deaths, and recoveries, in total and by day (top element on right-hand side of Figure 1). It also ofers numerical (left-hand side element of Figure 1) and visual (middle element in Figure 1) representations of these figures by state and population density, through drill-down functionality. It also decomposes the figures by demographic attributes such as age group and gender (middle element on the right-hand side of Figure 1). Because of disputes over the timeliness of reported data in various pandemic IS (e.g., Cornish et al., 2020), the dashboard also represents the date of infection separate from the date of record generation (bottom element on the righthand side of Figure 1).

New monthly Covid-19 infections in Germany (right-hand y-axis)  
![](/api/attachments/A3ZH8E4G/fulltext/images/4dfcac6aa9e9a929273ae2160cf7b4a178ec086b5d2ace0d362a639a6125fe1a.jpg)  
Figure 1. Screenshot of Germany’s RKI COVID-19-Dashboard (https://corona.rki.de, from June 16 2020), with annotations

Corona dashboards are likely the most intensively used IS during the global pandemic. For example, the COVID-19 dashboard at Johns Hopkins University reportedly hosts three to five billion interactions every day (K Rogers, 2020). But the use of dashboards is not stable, it varies as the pandemic progresses. Figure 2 shows visits to the German RKI COVID-19-

Dashboard homepage and the number of new monthly infections with COVID-19 between January and October 2020. Around the time the Covid-19 outbreak entered Europe in January 2020 and led to what is now known as the “first wave of the epidemic” in Europe, roughly from February to May 2020 (Flaxman et al., 2020), total visits to Germany’s RKI COVID-19 web page increased from 630,000 (December 2019) and 1,700,000 (January 2020) to 6,200,000 (February 2020) and 66,600,000 visitors in March 2020. As the so-called “second wave” started in Europe around October 2020 (Looi, 2020), visits to the dashboard homepage again started to mirror the rise in infections.

![](/api/attachments/A3ZH8E4G/fulltext/images/4100ae1a96308733b95e905374b61d93752cdc767d0d537b53f2e9f5c03af10d.jpg)  
Figure 2. Visits to the RKI COVID-19 homepage and monthly COVID-19 infections in Germany from January to October 2020, Data from SimilarWeb (2020) and Robert Koch Institut (2020)

The number of reported interactions with corona dashboards might be seen as an indicator that these systems are perceived as useful. However, the verdict about them is not unequivocal, in part because diferent corona dashboards vary in accuracy, timeliness, focus, and scope of information conveyed. In fact, guidelines have been developed to help users evaluate diferent dashboards (Datta, 2020). In the political discourse and public media (e.g., Carthaus, 2020; Minji, 2020), several questions have been posed<sup>3</sup>: How accurate is the information represented? How is the data represented? Why do time lags exist in the representation (e.g., every weekend we see dropping numbers of new infections, mainly because of closed healthcare institutions)? Which representations, graphical or otherwise, appropriately convey the information that users seek? What is not represented accurately (e.g., number of negative tests) and to what extent is technical infrastructure to blame?

The proposition I develop is that corona dashboards do not efectively represent the pandemic. They should not only represent attributes, such as infections and deaths, but also track the evolution of these and other attributes over time in response to events that occur that change the course of the evolution. The ability of a corona dashboard for statetracking becomes ever more important as the pandemic progresses because not only state variables differ by regions but also events that occurred. In Europe, the period March to April 2020 was characterised by a variety of governmental lockdown measures that difered across European states (from stricter measures in Italy, Spain, or Germany, to less strict measures taken, for example, in Sweden). Between May and June 2020, governmental lockdown restrictions in the same regions were partially and stepwise released, but again diferently across nations, states, and even regions or cities (European Centre for Disease Prevention and Control, 2020). As Europe has been dealing with a more severe second wave since fall 2020 (Looi, 2020) and trying to anticipate if additional waves are yet to come (Flaxman et al., 2020), tracking both events and states, and their relationships, will become ever more relevant.

## 3. RESEARCH APPROACH

I apply a staged research process informed by the methodology for design science research by Pefers et al. (2007). It consists of three main steps (Figure 3). My entry point is context-initiated (Pefers et al., 2007, p. 56) in that I start by observing the current practical solution for Covid-19 tracking in the form of the existent implementation of a corona dashboard in Germany, with the view to ascertaining the level of utility currently accomplished by the artefact. This analysis is followed by developing new objectives for a better artefact in the form of four new design principles for state-tracking, and then an evaluation of these design principles with design practitioners. While presented in nominal sequence, the three main steps were executed in an iterative and logically connected fashion. For example, the analysis of Germany’s RKI COVID-19-Dashboard proceeded logically interwoven with the development and formalisation of design principles for state-tracking. Likewise, during the case study evaluation, insights were gained not only about the design principles that specify the solution objectives but also about the decisions that led to the artefact implementation as in-use today. In what follows, I explain each main step briefly.

![](/api/attachments/A3ZH8E4G/fulltext/images/83f45a9fdb5aac4948abb6bf28f434998fcf1fbc4993c3c93a3c8c080003d780.jpg)  
Figure 3. Research process.

## 3.1. Analysis of a situated artefact implementation

I begin by engaging in a type of design archaeology (Chandra Kruse et al., 2019), that is, the analysis of an existing, in situ corona dashboard artefact-in-use. My goal is to understand how and why present corona dashboards that have been made available to the public operate the way to do and to evaluate what they are able to accomplish representationally. I examine a current situated implementation of corona dashboards, Germany’s RKI COVID-19-Dashboard. It is a representative case of corona dashboards as it builds on the same technology (in particular ArcGIS online) as most other dashboards. The basis of my analysis is what is called an interpretation mapping (Wand & Weber, 1993), that is, a mapping of representational elements featuring on the dashboards to a set of theoretical concepts to describe real-world domains in terms of things that are of relevance, their properties, and the events that occur that change the states of these things. A detailed description of these constructs is provided by Weber (1997). Procedural guidelines for such a mapping are described by Rosemann et al. (2009).

## 3.2. Definition of objectives of a solution

The analysis carried out in step one identifies a lack of state-tracking ability in presently available corona dashboards. The dashboards only ofer a partial representation of the pandemic and its impacts, which could result in misinformation, inefective medical interventions, or lack of acceptance of non-pharmaceutical public health interventions. The defined objective in step two therefore is to develop and verify design principles that could extend the state-tracking ability of corona dashboards. I specify these objectives by deriving design principles for state-tracking from representation theory (Weber, 1997). Design principles are a form of prescriptive design knowledge that capture a general solution in a class of artefacts, which can guide designing in a wider range of problems and solutions and are thus valuable outcomes as theoretical contributions for IS scholars (Baskerville et al., 2018) and as guidelines for practitioners to design similar artefacts (Iivari et al., 2020). To make the design principles understandable and useful, I specify them according to a schema provided by Gregor et al. (2020).

## 3.3. Evaluation

To evaluate the extent to which the proposed design principles could assist in developing a new artefact that provides better state-tracking ability, I collected empirical data about the design and operation of Germany’s RKI COVID-19-Dashboard. Details are provided in the Appendix. Key case study informants are stakeholders involved in design activities relevant to the dashboard (i.e., development, implementation, and operation), such as solution architects, GIS developers, user interface designers, or geomatics specialists, rather than end-users of the dashboards (e.g., policymakers, health professionals, or members of the general public) because the diferent designer roles are the main stakeholders that would be concerned with implementing the proposed design principles (Iivari et al., 2020). End users would only be able to report on consequences from these design choices (e.g., in terms of changed perceptions of usefulness). I examine the relevance and applicability of the design principles in terms of importance, actability, and efectiveness, following the suggestions and template by Iivari et al. (2020).

## 4. ANALYSIS OF GERMANY’S RKI COVID-19- DASHBOARD

My starting point was an analysis of the present corona dashboard that is in-use in Germany and maintained by the RKI. To evaluate the abilities of Germany’s RKI COVID-19-Dashboard for representing information about the Covid-19 pandemic, I use a conceptual lexicon that is grounded in representation theory (RT) (Wand & Weber, 1990, 1993, 1995; Weber, 1997). Term definitions and reviews of the RT literature are provided by Burton-Jones et al. (2017) and Recker et al. (2019).

The fundamental idea of RT is that IS are built and used because it can be more eficient to learn about the world from computerised representations than by direct observation (Burton-Jones & Grange, 2013, p. 636; Wand & Weber, 1993, p. 218). In situations like the current global pandemic, one could argue that IS are the only feasible way to learn about the pandemic – we cannot directly observe the spread of the pandemic as it unfolds across the planet.

I use the RT lexicon in my artefact analysis because it distinguishes between representation, that is, the ability of an IS to provide a faithful representation of focal real-world phenomena (Wand & Weber, 1995, p. 207) and state-tracking, that is, the ability of an IS to remain a faithful representation of the focal real-world phenomena as things in the real world undergo change. Following RT, a useful IS for managing a pandemic is one that faithfully represents all information users seek about the pandemic (the focal realworld phenomena) and its efects on other real-world phenomena around us. This means, the IS must feature representations for relevant things afected by the pandemic in the real world (e.g., elderly people, health professionals, or children), systems comprised by them (e.g., families, schools, elderly care facilities), their properties (e.g., existing health conditions), states (e.g., being infected, contagious, vaccinated, or recovered), and so forth.

It is important to note that alternative analysis lexica could just as well be used (Ågerfalk & Eriksson, 2004). For example, Searle (1995) also recognises the existence of an objective world in which citizens could become infected, develop immunity, or die, from a virus. Scholars working with this lexicon would speak of asserting “substantial properties” of “concrete objects” (March & Allen, 2014, p. 1349) rather than representing “intrinsic properties” of “things” (Weber, 1997, pp. 34–35). Yet, both the scholars working with Searle’s lexicon and the scholars working with the RT lexicon recognise that the meaning of data represented in information systems is socially constructed. For example, Wand and Weber (1995, p. 206) note that information systems represent the meaning of some real-world phenomenon as perceived by someone or some group. This is important because corona dashboards display data that is not physically factual but socially constructed. For example, the volume of Covid-19 fatalities they report depends on the definition of Covid-19 associated fatalities agreed upon in that country (Sorci et al., 2020), which implies that the representation of such social facts Searle (1995) could carry communicative meaning (Ågerfalk & Eriksson, 2004). However, a Searleian perspective would additionally recognise that representation (of assertives) is only one of the several functions of a language (Eriksson & Ågerfalk, 2021). Still, for the class of systems that are Corona dashboards, the emphasis is clearly on assertives and thus the fundamental representational question remains the same across the diferent schools of thought: How can we model socially constructed information about the real world within an IS such that the system can be efectively used?

Table 1 summarises my analysis of the main representational elements used in Germany’s RKI COVID-19-Dashboard to convey information about the pandemic (Figure 1) in terms of their usefulness for representation (the ability to observe the state of things, such as a person or object) or state-tracking (the ability to follow a trail of changes over time).

The analysis suggests that the present corona dashboard implementation contains more elements associated with representation than state-tracking. In terms of representation, Germany’s RKI COVID-19- Dashboard allows drilling up and down to states, regions, or municipalities (properties of geographical collectives) or by gender and age (properties of demographic collectives) to examine state variables such as reported versus incurred infections, population volume and density, recovered cases, or deaths. The state representations are updated daily. However, no mechanism is discernible for selecting additional or other epidemiological (e.g., reproduction number) or non-epidemiological (e.g., economic) attributes, such as job losses, GDP, or PMI (Haldane & Chowla, 2021).

In terms of state-tracking, the analysis suggests that the current implementation ofers only partial ability for state-tracking if any. Germany’s RKI COVID-19-Dashboard tracks daily changes in three state attributes (reported infections, reported deaths, estimated recoveries). Other lawful state changes (e.g., possibly recurring infections, actual length of recoveries) are not tracked. Moreover, other possible lawful state transitions (i.e., changes that could occur between attributes such as infections and death that are logically possible) that could result in reported state attributes are not tracked either. For example, the dashboard does not distinguish between deaths caused by COVID-19 versus diferent causes of death with COVID-19 side efects. Moreover, Germany’s RKI COVID-19-Dashboard provides timestamps for the state variables it displays, but no representation is provided for any type of external events that might be relevant to the evolution of the pandemic, such as the timing of nonpharmaceutical interventions (Flaxman et al., 2020) in the form of lockdowns, border closures, or contact restrictions, or – more recently – pharmaceutical interventions such as vaccination rollouts (Limb, 2021).

Table 1. Analysis of the Main Representational Elements in Germany’s RKI COVID-19-Dashboard.

<table><tr><td>Dashboard element</td><td>What is represented?</td><td>What information is conveyed?</td><td>What is the representation useful for?</td></tr><tr><td>Top element on right hand side of Figure 1</td><td>Total infections, deaths, and recoveries (as numbers).</td><td>Numerical attributes convey the values of properties in general of the population of Germany (i.e., a system of things that share non-binding mutual properties).</td><td>For representation: they summarise the state of a collection of people (Germany&#x27;s population) at some point in time (the time of visit).</td></tr><tr><td>Middle element on right hand side of Figure 1</td><td>Total infections (as numbers), by age group and gender (categorised through colour coding).</td><td>Numerical and visual attributes convey the values of properties in general of some subsets of the population of Germany.</td><td>For representation: they summarise the state of a subset of the collection of people (Germany&#x27;s population) that are of particular interest, because of presumed risk of infection, at some point in time (the time of visit).</td></tr><tr><td>Bottom element on right hand side of Figure 1</td><td>Sum of daily infections and daily reported data, by date (as numbers, the two types of data are separated visually through colour cording).</td><td>Numerical and visual attributes convey the values of one property in general (infections) of the population of Germany by event (dates).</td><td>For state-tracking: The inclusion of temporal event data (successive dates) allows following the change in infection or reporting data over time.</td></tr><tr><td>Left hand side element in Figure 1</td><td>Total infections, by state.</td><td>Numerical attributes convey the values of one property in general (infections) in different subsets (states) of the population of Germany.</td><td>For representation: they summarise the state of the collection of people (Germany&#x27;s population) decomposed into sub-sets (by state), at some point in time (the time of visit).</td></tr><tr><td>Middle element in Figure 1</td><td>Total infections relative to population (categorised through colour coding), by state (visual).</td><td>Visual attributes convey the values of one property in general (infections) in two different subsets of the population (state and population density) of Germany.</td><td>For representation: they summarise the state of the collection of people (Germany&#x27;s population) decomposed into sub-sets (by state and population density), at some point in time (the time of visit).</td></tr></table>

## 5. DEFINITION OF SOLUTION OBJECTIVES: DERIVING DESIGN PRINCIPLES FOR STATE-TRACKING

My analysis summarised in Table 1 identifies a lack of state-tracking ability in presently available corona dashboards. To define a potential solution for a better artefact, I again build on RT to develop four design principles that extend corona dashboards’ ability to maintain an up-to-date, faithful representation as events occur that change the relevant real-world phenomena. Table 2 presents four design principles for corona dashboards that I derived deductively from four conditions for state-tracking suggested in RT (Weber, 1997, pp. 133–146). Each design principle is specified in terms of context, aims, mechanism, and rationale, as per the schema suggested by Gregor et al. (2020). Because implementers (providers of corona dashboards in organisations such as hospitals, public health institutions, or governments), and users (policymakers, health professionals, local crisis response teams, and members of the general public) are invariant across all four design principles, they are not featured separately.

## 6. EVALUATION OF THE DESIGN PRINCIPLES IN A CASE STUDY

In the case study, I pursued two broad goals: first, to learn about how the design of Germany’s RKI COVID-19 dashboard was completed (indicated in Figure 3 through an arrow going back from evaluation to analysis), and second, to evaluate whether my design propositions were viewed as important, feasible and relevant (indicated in Figure 3 through an arrow going back from evaluation to definition). Design and procedures are explained in the Appendix.

## 6.1. The design of Germany’s RKI COVID-19- dashboard

In February 2020, when the COVID-19 pandemic had started to impact Europe, the then-available Johns Hopkins COVID-19 Dashboard in the United States created political pressure in Germany to provide a similar technology to inform the German public. The RKI and the German Federal Ministry of Health (BMG) tried to develop a dashboard solution themselves but quickly realised that an industry-strength scalable and loadable infrastructure for usage by 80 million citizens could not be developed within a matter of days. They decided to implement and further develop a prototype created by a German taskforce of Esri, an international supplier of geographic information system software, web GIS and geodatabase management applications. RKI and Esri oficially presented their solution on March 20, 2020, two days after a tweeted picture featured federal minster of health Jens Spahn at a BMG ofice with the Esri dashboard prototype already on the wall.<sup>5</sup>

Three attributes characterise the design of Germany’s RKI COVID-19-Dashboard. First, the dashboard displays only data provided and verified by the RKI in fixed time slices of 24 hours, consistent with other public information released by the RKI. It does not convey estimations or predictions. The data are hosted on an open data hub, NPGeo,<sup>6</sup> a national platform for geodata analysis, combination, and visualisation. This data platform supplies data to Germany’s RKI COVID-19-Dashboard but can also supply specialised dashboards, for example, those used by states, municipalities, or special interest groups such as the German Association for Fire Protection, a non-profit expert network that unites parties involved in civil protection, rescue and security.<sup>7</sup>

Second, RKI data is displayed at agreed-upon geographical levels such as states, counties, districts, and municipalities. This was dificult to implement because Germany’s health data reporting infrastructure is federated and relies on all health department (about 400 in total) to input their data in a comparable, automatable format but on the basis of their own infrastructure and resourcing. One of the executive business development managers from Esri commented:

“Our administrative structure for health care is a matter for the federal states and in this respect it is something that is regulated for the federal states and the federal states then decide together with the state registration ofices for infections, which are located at the health ministries, how they inform the population.”

<table><tr><td>Name</td><td>Original state-tracking condition (Weber, 1997)</td><td>Relevance in the context of the Covid-19 pandemic</td><td>Aim, mechanism, and rationale of the design principle</td></tr><tr><td>1. The mapping principle</td><td>Each state in the focal real-world phenomena must map to at least one state in the IS.It must at all times be possible to tell relevant states of the focal real-world phenomena based on a state of the IS.</td><td>As the interest in the focal phenomena associated with the Covid-19 pandemic changes (e.g., from a purely epidemiological interest to include concerns about economy, public psychic health, or social unrest), relevant states that describe all relevant phenomena must be mapped to an equivalent set of states displayed in a corona dashboard.</td><td rowspan="2">Aim: It must at all times be possible to observe relevant status indicators for particular collectives of people through the corona dashboard.Mechanism: Ensure there is, and always remains, a 1:1 mapping between status indicators that are considered relevant during a pandemic (e.g., total infections, infections relative to population density, excess deaths, the reproduction number R, and so forth) and symbolic representations (e.g., text and graphics) available in the dashboard. Ensure the appropriate and automatic provision of relevant data for each identified status indicator.Rationale: At different times over the course of the pandemic (e.g., before, during, or after the first or second wave), and for different types of decisions, different parameters of the pandemic evolution are relevant: infections relative to population density might be relevant to travelling, reproduction might be relevant to lockdown measures, total infections might be relevant to hospital infrastructure planning.Aim: Corona dashboards must embody relevant transformation laws so that any intermediate and resulting stable states in the focal real-world phenomena can be faithfully represented by the IS. It should also be possible to project relevant future states based on extant transformation laws.Mechanism: Construct an algorithm that periodically, at reasonable and feasible time intervals, evaluates the transformation laws in the IS against data about the state changes in real-world things. For example, compare the algorithm that estimates the number of recovered COVID-19 cases real-world data about the sequences of state changes that reported cases of patients underwent (He et al., 2020). If deviations occur, update the transformation laws in the IS that govern the estimation algorithm.Rationale: Over time during the pandemic, more knowledge has been accrued about contagion periods, length of isolation periods required, or thresholds that indicate levels of relative infection by population density (in Germany: number of infection by 100,000 inhabitants). These laws are socially constructed and can change. Transformation laws in a corona dashboard must thus be made adaptable.</td></tr><tr><td>2. The tracking principle</td><td>State changes adhere to transformation laws (e.g., resurrection is not lawful). States change (e.g., an infected person may recover, or die) because of events (e.g., hospitalisation, care).When things in the focal real-world phenomena change states as a result of events that are internal to the phenomena, the IS must change from a state that faithfully represents the initial state of the thing to a state that faithfully represents the subsequent state of the thing.</td><td>As knowledge about transformation laws that pertain to the Covid-19 pandemic changes through new discoveries (e.g., length of incubation, contagion, or recovery periods), it must be possible to update the transformation laws in corona dashboards so that they correctly update states (such as infections, vaccinations, or recoveries), and also project foreseeable future states (e.g., trends in infections, speed of recoveries, estimated deaths).</td></tr></table>

<table><tr><td>Name</td><td>Original state-tracking condition (Weber, 1997)</td><td>Relevance in the context of the Covid-19 pandemic</td><td>Aim, mechanism, and rationale of the design principle</td></tr><tr><td>3. The external-event principle</td><td>An external event in the focal real-world phenomena is a change of state that arises in some thing in the phenomena by virtue of the action of some thing in the environment of the phenomena. When an external event occurs in the focal real-world phenomena, an external event that is a faithful representation of the real-world external event must occur within the IS.</td><td>For example, over the course of the pandemic, governments implemented and stopped a variety of non-pharmaceutical interventions (European Centre for Disease Prevention and Control, 2020) in response to the trajectory of infections and deaths. Several countries including Russia and China have started vaccination programmes (Cohen, 2020). Mass infections can occur through super-spreading events (Wong &amp; Collins, 2020).</td><td rowspan="2">Aim: It must at all times be possible to use a corona dashboard to track external events (e.g., political interventions such as lockdowns, release of new technologies such as vaccines, or change in season) and map changes in state variables (e.g., infection rate, death rate, etc.) to the occurrence of those events.Mechanism: Ensure that occurrences of relevant external event relevant to the focal real-world phenomena are identified and can be reported to the corona dashboard. Ensure symbolic representations (e.g., text and graphics) are available in the dashboard to convey the meaning of different events.4Rationale: The trajectory of a pandemic is not based on internal states (i.e., molecular and biological features) of the virus only, the distribution and frequency of COVID-19 infections is an epidemiological process influenced by outside factors such as location (middle of Europe versus isolated island), season (spring versus fall), and the behaviours of social collectives and the design of social and technical institutions that govern these behaviours. A corona dashboard must present changes in the COVID-19 pandemic in coupling with those events that influence the epidemic.Aim: It must be possible to track the sequence of relevant events that occur. The sequence of external events in the focal real-world phenomena must match the sequence of external events in the IS.Mechanism: Ensure that relevant event sequences are identified in the real-world and compare these to the sequences of state changes recorded in the IS.8Rationale: Pharmaceutical and non-pharmaceutical response interventions are not singular occurrences but instead interdependent temporal and logical sequences of events. To understand their outcomes, it is important to track not only the events and state changes but also their logical and temporal sequences.</td></tr><tr><td>4. The sequencing principle</td><td>External events do not occur in isolation but in a temporal and logical sequence. Representations of external events in an IS must follow the same sequence as external events that occur in the focal real-world phenomena.</td><td>A temporal sequence in the context of the Covid-19 pandemic might be the stepwise implementation of policy interventions (e.g., Australia&#x27;s three-step plan for removal of lockdown measures). A logical sequence might the occurrence of collective action (e.g., public protests) in response to policy implementations.</td></tr></table>

Table 2. (Continued).

Third, sovereignty for information displayed on the dashboard lies entirely with the RKI. A specialist team at the RKI decides, which data to provide and display. The Esri Germany team consults but final decisions rest with the RKI. In the words of an Esri executive:

“The sovereignty of information lies with the RKI. Because that’s where the specialists are, the ones who are familiar with the phenomenon, who have been researching it for decades. And who, in principle, also have ownership of the data and data infrastructures. So, we must not forget that. And they also have the information sovereignty, whereas here we [Esri] are the technology specialists. And that means that a group discusses optimization at the RKI, and we then come together to discuss whether this can be done and, if so, how it can be done and with what efort. And then, of course, we also contribute our cartographic knowledge and then talk about issues of cartographic design, user ergonomics, user interface design and so on.”

## 6.2. Evaluation of the state-tracking design principles

The primary objective of the case study was to examine the relevance and applicability of the four state-tracking design principles in terms of importance, actability, and efectiveness (Iivari et al., 2020). Figure 4 visually summarises the insights gained through the case study on each of the design principles. Each design principle is positioned in terms of reported level of importance (from low to medium and high), and estimated efectiveness (from low to medium and high). The bubble size summarises the feedback received on actability of each design principle, with a small circle suggesting low actability and the larger circle indicating medium actability (no design principle was rated as highly actable). All design principles were rated as being of medium or higher importance. The visual summary of the qualitative evaluation suggests in particular that the extern design principle 3 (external event representation) was deemed both importance and efective if implemented. One manager remarked:

“From a research point of view, it’s clear that you need to just let one thing correlate with the other and you see how it goes.”

Similarly, design principle 4 (sequencing) was deemed important and of medium efectiveness if implemented. For example, a business development manager at Esri commented:

“I think it is absolutely necessary to go in this direction, that one somehow depicts the complexity with all its interactions. You can do that. [. . .] if several of these events, such as a lockdown and the obligation to wear masks, come together because they are very close in time, and then the infection rates fall, then of course every citizen draws a diferent conclusion and says, yes this measure worked, although you do not really know which of the measures had what efect. Well, that [would be] actually quite nice to see. "

The two design principles that are presently at least partially implemented (DP1 and DP2) were rated of medium-to-high importance and low-to-medium efectiveness. Together, this evaluation suggests that especially those design principles that are presently not considered in corona dashboards were seen as relevant additions.

Reported actability of all design principles was markedly low. None of the design principles was rated high in terms of actability. Three main reasons became salient through the data analysis for why such features were dificult to implement at present:

## 6.2.1. Distribution of information sources

Relevant information in Germany is provided through a federated administration and reporting system in which several hundred local authorities collect, store, and report data in a largely unstandardised manner. With German data regulations in place, a centralised information infrastructure is not yet existent from which relevant data could be sourced for representation through a dashboard even though digital means are already available. An Esri executive stated:

“What does not exist [. . .] is that all these measures are reported to a central location, so that in which county you know what measures have actually been taken for what period. They don’t have that. And you could map that. For example, through the Federal Ofice for Civil Protection and Disaster Relief and the apps KATWARN and NINA [German mobile apps for emergency and disaster control], which are operated from there. But then again, a decree or an injunction must be brought about that the crisis staf decide - and that should be one in every county - then also pass this data to a central location.

## 6.2.2. Possibility of automated extraction

A second challenge is the transmission of data into the NPGeo hub. Relevant data are sourced from local health administration ofices. While all these ofices display local information in some format (e.g., via their homepages), not all of them make the data directly available in a digital let alone open format. Updating information in the corona dashboard therefore regularly involves substantial manual efort or relies on makeshift automation tools such as web scraping. An Esri business development manager explained:

“The disaster control apps, you know NINA and KATWARN for example, they are fed with this information, so that you are then informed. But not everyone has these apps. So, the question is, how do you find out which state registration ofices or regional and local health authorities - we have more than 400 of them in Germany - how do they inform their local population about the measures taken in a timely manner? Once you know that, you have to ask the question: is this source of information digital and can this information be accessed automatically? And at the moment it is not automatable because you don’t get a CSV table or anything else, you have to actively read HTML pages.”

![](/api/attachments/A3ZH8E4G/fulltext/images/ac41541cc9da7703edd9763cbaac39bc492bc3eda7975fe6b76d28d81104794f.jpg)  
Figure 4. Qualitative evaluation of case study feedback on the design principles.

The experienced dificulties with feeding all relevant data to the dashboard led to the initiation of a common data infrastructure project, DEMIS (Diercke, 2017), which, since June 2020, is successively replacing the extant reporting system with an online framework that gradually connects approximately 170 laboratories and 400 health authorities and provides electronic reporting, cooperation between health authorities, and provision of data for evaluation and analysis.

## 6.2.3. Centralised information sovereignty

The third main reason for the lack of actability on certain aspects of the design principles, such as additional state variables (e.g., economic markers of the pandemic) or external events (e.g., political measures taken), resides in RKI being the sole decision authority over the information conveyed through the corona dashboard. As a public health institute, the RKI made the decision to restrict the scope of the dashboard to selected pure epidemiological data, which renders the conveyance of additional, non-epidemiological information (such as the number of requested or granted temporary economic state aids) on Germany’s RKI COVID-19-Dashboard impossible even if deemed implementable and relevant.

## 6.3. Tensions influencing the state-tracking ability of corona dashboards

A second objective of the case study was to develop deeper insights why a particular design principle was not deemed actable, and how a design principle, if implemented, was designed into the in situ artefact. This analysis (Table A3) yielded three tensions:

A first tension concerns the existing federated legislation and administration versus the need for a centralised information infrastructure. This tension played out primarily in the recording and transmission of relevant data to be conveyed on a dashboard; however, it also became evident in matters of IT resourcing. Depending on the size and funding of the relevant local public and health authority, also the technological resourcing varies across the country, in terms of availability of infrastructure, IT capabilities or support availability. One of the regional district geo-managers, for example, explained:

“I know that in [a diferent district], for example, the dashboard is operated by a data processing centre and not by the district administration. And the public health department is included in the district administration. We don’t have a data processing centre, we only have an IT department, and we ourselves are more or less independent, and we are also members of the crisis team. This means that we ourselves can react quickly but do not have to access a data processing centre. [. . .] There is always the question: who maintains the data there?”

Moreover, not only is IT support for data collection and recording diferent across the units of the federated system, also the decision-making about extent and format of disclosure of such data varies by city, district, region, or state. Several districts, for example, chose not to report COVID-19 deaths, others decided to report absolute but not relative numbers, or to report (or not) statistics such as the reproduction number R (Adam, 2020a). In the words of the business relations executive:

“The problem at this point is again our administrative structure. Health care is a matter for the federal states and in this respect it is something that is regulated for the federal states and the federal states then decide together with the state registration ofices for infections, which are located at the health ministries, how they inform the population.”

The main reason for the existence of this tension lies in German regulations that prohibit interdepartmental responsibilities and data interoperability. Health data is collected in federated departments, and no legal basis exists for hosting the data in a central repository. Only in a declared disaster protection case is the Federal Ofice of Civil Protection and Disaster Assistance entitled to combine and provide relevant tasks and information in a single place.

A second tension emerged when discussing the inclusion of mechanisms for external event and sequencing representation (DP3 and DP4) and addresses the balancing between accurate historical data and uncertain forecast data. This tension becomes apparent because through a potential inclusion of external event (and sequencing) representations, it would be possible not only to display the unfolding of the pandemic in relation to those events that occurred in the past but also in relation to predictions about how it could unfold if the event would not occur (or some other event instead). Such prediction models are feasible and also used for strategic planning (Flaxman et al., 2020) but case study participants expressed concerns about how such prediction models, which are necessarily forecasted and with more uncertainty than the presently reported historical and verified data, would be interpreted by endusers of the dashboards. A regional crisis management team coordinator stated:

“Of course, we also have this forecast data, but it has been shown, or was agreed, that such data does not belong in a public dashboard. Only the pure facts should be included, in order not to make oneself vulnerable to attack.”

This concern not only played out in the discussion about whether or not to include forecasted, predicted data together with, or instead of, historical and verified data. It also presented a general tension in terms of the confidence in data processing versus data interpretation. A general tenet in the case study was palpable hesitance about providing more, and more complex data, in fear of misinterpretation or misuse by the general public. This was one noted reason why data about infection numbers was not correlated with intervention events such as political measures. One of the geomatics specialists in a regional public ofice commented:

“If the result now comes out, for example, “despite the use of a mask, the numbers are going up again”, that ultimately leads to people all saying “The mask is nonsense. I’ll leave it out”. Whereby maybe the cause that it goes up was a completely diferent one. [. . .] Maybe there are reasons why the curve and the numbers go up anyway. That would lead to misinterpretations among the citizens. In this respect, you have to weigh more carefully what you are representing.”

A similar view was held by one of the GIS developers:

“In my opinion, two major aspects play a role here: The fear of politicians that the data might show that a certain measure did not afect cases but only restricted daily life. Secondly, the temporal coincidence of a change in state variables and an event might lead to false claims about the impact of events because the efects of certain events might be temporarily shifted.”

In this vain, often a conscious decision was taken not to report more complex statistical information including forecasted data, uncertainty estimates, or in cases even statistics used in the public and political debate (e.g., incidence thresholds or reproduction numbers). One of the Esri executives stated:

“And so that means such uncertainty – we’ve discussed this, can one represent the uncertainty of the numbers? It can be represented, but we know that the public in particular cannot deal with it. [. . .] The most important thing is oficial and really verified data, because there is also enough fake news and whatever else is thrown around.”

## 7. DISCUSSION

Germany’s RKI COVID-19-Dashboard is presently more useful for representation than for statetracking. There are good reasons for this focus. During the early phase of the pandemic outbreak in Europe, a pressing need was to understand the state of the pandemic and the European continent. How many people are afected and where, and how many people are dying from the virus and where, were important questions. Likewise, as a public institute for nationwide health monitoring and reporting, the RKI understandably maintains their decision to represent only epidemiological data but not political, economic, or social data (e.g., incident level thresholds that are the basis of many political measures).

However, as we are witnessing in the public and political debate, the pandemic is not just an epidemiological process, it has wide-reaching consequences on many other facets of everyday life, from health to economic and social issues. Representationally, the “focal phenomenon” that is the COVID-19 pandemic has been expanding gradually since its onset. Providing a dashboard with the aim to help people understand the situation and its consequences must thus inevitably be expanded in reach and coverage.

Even though the Covid-19 virus is a factual object with certain properties, some of which we know and many of which we only begin to learn about, we should not think about the pandemic as a physical thing to represent. The pandemic resembles a socially constructed process – a logical and temporal progression of events and activities that unfold over time. Any IS whose purpose it is to help understanding of the outbreak situation and managing the pandemic must thus be helpful in (re-) constructing the processual narrative that reveals the mechanisms by which the events and actions play out over time.

A continued lack of ability for state-tracking will over time undermine the intended purpose and usefulness of corona dashboards. Early signs are clear. While useful during the early phase of the pandemic’s onset in Europe, the system has become less useful with time as more events and changes occurred in the real-world (e.g., political measures were taken, the epicentres of the pandemic shifted, the number of intensive care units became overloaded in certain regions, and capacities were booted in others) that were neither represented nor tracked, in the dashboard. We all have come to realise that we cannot understand the pandemic, or how to deal with it, by reducing our information to the number of infections, fatalities, and recoveries alone. To anticipate and undertake actions such as restarting the economy, balancing safety and well-being of citizens, rolling out vaccination programmes, or simply making decisions about inter-state travel for holiday purposes, we need to understand how the pandemic evolves in relation to a variety of events and actions that have occurred and continue to occur and interfere with the progression of the pandemic.

One key insight from the analysis of the corona dashboards and the empirical data in the case study is that corona dashboards are only ever as efective as the underlying information system infrastructure including its technological, administrative, and legislative components. Presently, Germany’s main corona dashboard is maintained by the RKI, which is entitled by the Protection against Infection Act to act as a single integrated source of health data. But to make the dashboard a more efective state-tracking system for the general public, information sovereignty must extend beyond the RKI such that non-epidemiological data (e.g., economic state aids, unemployment rates, capacity of hospital beds, etc.) and key events and their sequences can also be covered by the dashboard, especially in terms of non-pharmaceutical interventions (lockdowns, contact restrictions, or school closures) and social events (e.g., demonstrations, or super spreading events). However, relevant interdepartmental connections beyond the health authorities do not legally exist, and data interoperability between diferent ministerial departments is low. Eforts towards a national information infrastructure must continue to develop a legal and technological framework for data interoperability and automated reporting.

Another key insight is that the efectiveness of many regional variants of the RKI Corona Dashboard is presently limited by local authorities hesitance to display complex or uncertain data in fear of user issues such as lack of acceptance, misinterpretation, or abuse. These issues are certainly real; however, they are issues of professional information communication, not provision through dashboards.

Finally, the combination of an open data infrastructure being available through NPGeo, the federated system of legislation and reporting, and diferent preferences for presentation of data have led to the emergence of a multitude of corona dashboards in Germany (some examples are listed in Table A1). With the number of dashboards increasing, the risk of inconsistencies rises, as does the risk of selective (mis-) interpretation because users can basically “choose” a dashboard that provides only those socially constructed information that match subjective preferences. This situation will not help public acceptance of pandemic measures, which is immediately relevant, for example, to the current rollout of vaccination programmes (Limb, 2021). Technologically, it would be possible to develop one central corona dashboard, as was intended originally, and equip it with features such as view filters or role-based access control such that diferent user groups (e.g., members of the general public versus political decision-makers or local crisis response teams) can access only those information most relevant to their tasks, whilst maintaining centralised control over data verification or information display.

## 7.1. Implications for research

The issue of representation versus state-tracking is neither new nor unique to the pandemic. However, the present pandemic vividly demonstrates how important state-tracking is. Thus, while the main contribution of this paper primarily artefactual (Ågerfalk & Karlsson, 2020, p. 111) and hopefully helps improving corona dashboards, it carries important theoretical and empirical implications. Modifying existing corona dashboards such that they implement state-tracking ability allows reflecting, evaluating, and amending theoretical ideas that were initially proposed by Wand and Weber (1995) and have since largely been forgotten. I doubt Wand and Weber (1995) had a pandemic in mind as a process that would change the lives of many when they formulated their ideas. But the question begs whether earlier attention to called statetracking would have led to more IS yielding such abilities. IS scholars have so far missed this opportunity. Burton-Jones et al. (2017, p. 1321) write:

“Our review showed researchers have not been interested in the STM [state-tracking model by Wand and Weber 1995]. We suspect one reason is that its predicted outcome (maintenance of a faithful representation) appears overly academic rather than practically useful.”

The practical relevance of state-tracking is here now. The opportunity is to help institutions to develop more useful IS that can faithfully track relevant sequences of state and event changes that bear relevance to understanding the pandemic and its future trajectory. Making this move will help the world, but it will also inform the future development of our theories of the IS artefacts and their design. By refuting, accepting or modifying the theorised criteria for faithful state-tracking that are at the core of tracing ability we can learn much about the success or failure of state-tracking. Both outcomes will be an advance.

The primary empirical implication of the ideas in this paper is that analyses similar to the inspection of Germany’s RKI COVID-19-Dashboard could now be carried out to compare the wide range of publicly available reports, maps, and other dashboards. Many such IS have been built over recent months and not all of them are equally useful (Datta, 2020). Empirical, comparative research using the design principles or language in this paper as evaluation criteria will help policymakers to utilise the best available IS infrastructure in their decision-making, and it will allow the general public to better understand the advantages and limitations of the wide variety of corona dashboards available.

## 7.2. Limitations and future research

The obvious limitation of the research in this paper is the focus on one representative case of an artefact, Germany’s RKI COVID-19-Dashboard. However, as noted, it builds on the same set of technology infrastructure as most other corona dashboards, so it should be possible to generalise the insights to other dashboard implementations. However, some of the insights about the underlying information infrastructure or federate regulation may be limited to countries with a similar federated democratic system. Analysing other cases of dashboards, their technological, regulatory, and informational infrastructures in comparison to Germany’s RKI COVID-19-Dashboard will certainly deepen and broaden the insights.

Likewise, the empirical insights reported in this paper are also grounded in the specific context of the study. Data collection took place in North Rhine-Westphalia; other states and regions have diferent legislative arrangements. Moreover, end-users did not feature prominently in the case study. Since corona dashboards are ultimately designed to be an efective information system for the general public, future research should examine users perceptions of their usefulness, for example, through a longitudinal survey that captures end-user evaluations over time as the pandemic progresses.

Moreover, the focus in this paper was on representational, not informational issues. Solving these issue may improve the usefulness of corona dashboards, but it will not solve infodemic issues such as misinformation, amateur data analysis, or fake news (Laato et al., 2020). It also will not solve issues of data quality, for example, through wilfully restricted or manipulated reporting of data into the systems (Cornish et al., 2020; Pundir, 2020). While my focus was on representation of “facts”, it is also important to realise that often these facts are socially constructed corona dashboard rely on data provided by some sort of (private, public, national, or governmental) infrastructure.

Finally, the design propositions developed in this paper focus on representational matters, that is, ways to convey information, alone; they do not speak to other purposes or efects a corona dashboard may have. For example, because they display socially constructed information as facts, corona dashboards may carry an action-oriented role (Ågerfalk & Eriksson, 2004; Rittgen, 2006) in that they might instigate certain user responses or behaviours. I have not looked at how action-orientation could be coupled with my chosen focus on representation and state-tracking. I do believe, however, that such an analysis would form a meaningful and desired complement. Such work could, for example, use rule-based approaches to identify how language could be used in specific user contexts to facilitate communication and action (Hirschheim et al., 1995, pp. 198–209).

## 8. CONCLUSION

The fact that both policymakers and regular citizens extensively on corona dashboards in dealing with the Covid-19 pandemic demonstrates that IS play an important role in solving this crisis and preventing the next. We do not save lives directly, nor do we develop vaccines or put more beds in hospital wards. The job of providing the right information to the right people at the right time in the right format is nonetheless critical. Leveraging our cumulative knowledge about the design of efective representation and statetracking systems can be a promising start. It will not stop the pandemic but it might help managing it in the most efective and human way possible.

## Notes

1. Allowing human users to extract meaning about a real-world domain through symbols that convey information about the things in that domain, their states, and properties (Weber, 1997).

2. Maintaining an accurate and complete representation of focal things in a real-world domain as events occur in the real world that change the state of these things (Wand & Weber, 1995).

3. Some points of debate are not representational, they are informational. For example, some countries report only selected data volumes, perhaps with an intent to “look more favourably” in comparison to others (Pundir, 2020). Misinformation is an important issue (Laato et al., 2020) but not the topic of this paper.

4. h t t p s : / / t w i t t e r . c o m / B M G \_ B u n d / s t a t u s 1238447752935325698.

5. https://npgeo-corona-npgeo-de.hub.arcgis.com/.

6. https://www.vfdb.de/home/?L=1.

7. Such an algorithm could be executed manually, for example, by assigning new user roles who are made responsible for identifying and recording external events in the IS, or semi-automatically, by scraping event information from digital chronologies (e.g., European Centre for Disease Prevention and Control, 2020).

8. Such an algorithm could be implemented automatically, for example, through event mining applications that identify event sequences from multimedia streams such as political news (Xie et al., 2008) or from social networking sites such as twitter announcements (Aggarwal & Subbian, 2012).

## Acknowledgments

I am indebted to the senior editor, Pär Ågerfalk, and two anonymous reviewers, for constructive and developmental feedback that helped improve the paper. I am thankful to Esri Germany, in particular Dr. Gerd Buziek, for participating in the study and assisting with case access. All faults remain my own.

## Disclosure statement

No potential conflict of interest was reported by the author.

## ORCID

Jan Recker http://orcid.org/0000-0002-2072-5792

## References

Abbott, A. (2016). Processual Sociology. University of Chicago Press.

Adam, D. (2020a). The limits of R. Nature, 583(7816), 346–348. doi: 10.1038/d41586-020-02009-w.

Adam, D. (2020b). Modelling the pandemic. Nature, 580 (7803), 316–318. doi: 10.1038/d41586-020-01003-6.

Adam, M., Werner, D., Wendt, C., & Benlian, A. (2020). Containing COVID-19 through physical distancing: The impact of real-time crowding information. European Journal of Information Systems, 29(5), 595–607. doi: 10.1080/0960085X.2020.1814681.

Ågerfalk, P. J., & Eriksson, O. (2004). Action-oriented conceptual modelling. European Journal of Information Systems, 13(1), 80–92. doi: 10.1057/palgrave.ejis.3000486.

Ågerfalk, P. J., & Karlsson, F. (2020). Artefactual and empirical contributions in information systems research. European Journal of Information Systems, 29 (2), 109–113. doi: 10.1080/0960085X.2020.1743051.

Aggarwal, C. C., & Subbian, K. (2012). Event detection in social streams. SIAM international conference on data mining, Anaheim, California.

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A. R., & Rossi, M. (2018). Design science research contributions: finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358–376. doi: 10.17705/1jais.00495.

Batra, D., & Antony, S. R. (1994). Novice errors in conceptual database design. European Journal of Information Systems, 3(1), 57–69. doi: 10.1057/ejis.1994.7.

Burton-Jones, A., & Grange, C. (2013). From use to efective use: A representation theory Perspective. Information Systems Research, 24(3), 632–658. doi: 10.1287/ isre.1120.0444.

Burton-Jones, A., Recker, J., Indulska, M., Green, P., & Weber, R. (2017). Assessing representation theory with a framework for pursuing success and failure. MIS Quarterly, 41(4), 1307–1333. doi: 10.25300/MISQ/2017/ 41.4.13.

Carillo, K., Cachat-Rosset, G., Marsan, J., Saba, T., & Klarsfeld, A. (2021). Adjusting to epidemic-induced telework: empirical insights from teleworkers in France. European Journal of Information Systems, 30(1), 69–88. doi: 10.1080/0960085X.2020.1829512.

Carthaus, A. (2020). Corona confusion: How to make sense of the numbers and terminology. Deutsche Welle. Retrieved from April 22. https://p.dw.com/p/3ZeJ7

Chandra Kruse, L., Seidel, S., & Vom Brocke, J. (2019). Design Archaeology: Generating Design Knowledge from Real-World Artifact Design DESRIST 2019: Extending the Boundaries of Design Science Theory and Practice, Springer.

Cohen, J. (2020). With global push for COVID-19 vaccines, China aims to win friends and cut deals. Science magazine. doi: 10.1126/science.abf8838.

Cornish, L., Jerving, S., & Ravelo, J. L. (2020). Data around COVID-19 is a mess and here’s Why that matters. Devex, Retrieved from June 24. https://www.devex.com/news/ data-around-covid-19-is-a-mess-and-here-s-why-thatmatters-97077

Datta, A. (2020). Here are some of the best maps tracking coronavirus updates. Geospatial Media & Communications. Retrieved from May 12. https://www. geospatialworld.net/blogs/here-are-some-of-the-bestmaps-tracking-coronavirus-updates/

Diercke, M. (2017). Deutsches Elektronisches Melde- und Informationssystem für den Infektionsschutz (DEMIS). Epidemiologisches Bulletin, 30, 291–293. doi: 10.17886 EpiBull-2017-039.

Dong, E., Du, H., & Gardner, L. (2020). An interactive web-based dashboard to track COVID-19 in real time. The Lancet, 20(5), 533–534. doi: 10.1016/S1473-3099(20) 30120-1.

Dubé, L., & Paré, G. (2003). Rigor in information systems positivist case research: current practices, trends, and recommendations. MIS Quarterly, 27(4), 597–635. doi: 10.2307/30036550.

Eriksson, O., & Ågerfalk, P. J. (2021). Speaking things into existence: ontological foundations of identity representation and management. Information Systems Journal, 31. doi: 10.1111/isj.12330.

Esri. (2020). ArcGIS online. Esri. Retrieved from November 26. https://www.esri.com/en-us/arcgis/about-arcgis /overview

European Centre for Disease Prevention and Control. (2020). Timeline of ECDC’s response to COVID-19. European Union. 24 September 2020. Retrieved from November 26. https://www.ecdc.europa.eu/en/covid-19 timeline-ecdc-response

Flaxman, S., Mishra, S., Gandy, A., Unwin, H. J. T., Mellan, T. A., Coupland, H., Whittaker, C., Zhu, H., Berah, T., Eaton, J. W., . . .et al. (2020). Estimating the efects of non-pharmaceutical interventions on COVID-19 in Europe. Nature, 584(7820), 257–261. doi: 10.1038/s41586-020-2405-7.

Gioia, D. A., Corley, K. G., & Hamilton, A. L. (2013). Seeking qualitative rigor in inductive research. Organizational Research Methods, 16(1), 15–31. doi: 10.1177/1094428112452151.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). The anatomy of a design principle. Journal of the Association for Information Systems, 21(6), 1622–1652. doi: 10.17705/ 1jais.00649.

Haldane, A., & Chowla, S. (2021). Fast Economic Indicators. Nature Reviews Physics, 3(February), 68–69. https://doi. org/10.1038/s42254-020-0236–y

He, X., Lau, E. H. Y., Wu, P., Deng, X., Wang, J., Hao, X., Lau, Y. C., Wong, J. Y., Guan, Y., Tan, X., . . .et al. (2020). Temporal dynamics in viral shedding and transmissibility of COVID-19. Nature Medicine. doi: 10.1038/s41591- 020-0869-5.

Hevner, A. R., March, S. T., Park, J., & Ram, S. (2004). Design science in information systems research. MIS Quarterly, 28(1), 75–105. doi: 10.2307/25148625.

Hirschheim, R., Klein, H. K., & Lyytinen, K. (1995). Information Systems Development and Data Modeling: Conceptual and Philosophical Foundations. Cambridge University Press.

Iivari, J., Hansen, M. R. P., & Haj-Bolouri, A. (2020). A proposal for minimum reusability evaluation of design principles. European Journal of Information Systems, Forthcoming. doi: 10.1080/0960085X.2020.1793697.

Institut, R. K. (2020). COVID-19 (Coronavirus SARS-CoV-2) [in German]. Robert Koch Institut. November 25, 2020. Retrieved from November 26, 2020. https://www. rki.de/DE/Content/InfAZ/N/Neuartiges\_Coronavirus/ nCoV.html

Kent, W. (1978). Data and Reality. North-Holland.

Laato, S., Najmul Islam, A. K. M., Nazrul Islam, M., & Whelan, E. (2020). What drives unverified information sharing and cyberchondria during the COVID-19

pandemic?. European Journal of Information Systems, 29 (3), 288–305. doi: 10.1080/0960085X.2020.1770632.

Langefors, B. (1973). Theoretical Analysis of Information Systems. Studentlitteratur.

Lazzerini, M., & Putoto, G. (2020). COVID-19 in Italy: momentous decisions and many uncertainties. The Lancet, 8(5), E641–E642. doi: 10.1016/S2214-109X(20) 30110-8.

Lee, A. S. (1991). Integrating positivist and interpretive approaches to organizational research. Organization Science, 2(4), 342–365. doi: 10.1287/orsc.2.4.342.

Limb, M. (2021). Covid-19: data on vaccination rollout and its efects are vital to gauge progress, say scientists. British Medical Journal, 372(76):1. doi: 10.1136/bmj.n76.

Looi, M.-K. (2020). Covid-19: is a second wave hitting Europe?. British Medical Journal, 371, m4113:1. doi: 10.1136/bmj.m4113.

March, S. T., & Allen, G. N. (2014). Toward a social ontology for conceptual modeling. Communications of the Association for Information Systems, 34(70), 1347–1358. doi: 10.17705/1CAIS.03470.

Miles, M. B., & Huberman, M. (1994). Qualitative Data Analysis (2nd ed.). Sage.

Minji, L. (2020). S. Koreans rely on digital maps to track spreading virus. Yonhap News Agency. Retrieved from A p r i l 2 2 . h t t p s : / / e n . y n a . c o . k r / v i e w / AEN20200224003800315

Naidoo, R. (2020). A multi-level influence model of COVID-19 themed cybercrime. European Journal of Information Systems, 29(3), 306–321. doi: 10.1080/ 0960085X.2020.1771222.

O’Connor, C., & Murphy, M. (2020). Going viral: doctors must tackle fake news in the covid-19 pandemic. British Medical Journal, 369, m1587:1. doi: 10.1136/bmj.m1587.

Pefers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45–77. doi: 10.2753/MIS0742-1222240302.

Pietz, J., McCoy, S., & Wilck, J. H. (2020). Chasing John snow: data analytics in the COVID-19 era. European Journal of Information Systems, 29(4), 388–404. doi: 10.1080/0960085X.2020.1793698.

Poole, M. S., & Van De Ven, A. H. (1989). Using paradox to build management and organization theories. Academy of Management Review, 14(4), 562–578. doi: 10.5465/ amr.1989.4308389.

Pundir, P. (2020). ‘Missing’ COVID deaths raise questions about India’s tracking of the outbreak. Vice US. Retrieved from June 16. https://www.vice.com/en\_au/article/ 3azdv3/missing-covid-deaths-raise-questions-aboutindias-tracking-of-the-outbreak

Recker, J., Indulska, M., Green, P., Burton-Jones, A., & Weber, R. (2019). Information systems as representations: A review of the theory and evidence. Journal of the Association for Information Systems, 20(6), 735–786. doi: 10.17705/1jais.00550.

Reeves, J. J., Hollandsworth, H. M., Torriani, F. J., Taplitz, R., Abeles, S., Tai-Seale, M., Millen, M., Clay, B. J., & Longhurst, C. A. (2020). Rapid response to COVID-19: health informatics support for outbreak management in an academic health system. Journal of the American Medical Informatics Association, 27 (6):853–859. doi: 10.1093/jamia/ocaa037.

Rittgen, P. (2006). A language-mapping approach to action-oriented development of information systems.

European Journal of Information Systems, 15(1), 70–81. doi: 10.1057/palgrave.ejis.3000597.

Rogers, K. (2020). Johns Hopkins’ dashboard: the people behind the pandemic’s most visited site. CNN. Retrieved from November 26, 2020. https://edition.cnn.com/2020 07/11/health/johns-hopkins-covid-19-map-teamwellness-trnd/index.html

Rogers, Y. (1986). Pictorial representations of abstract concepts relating to human-computer interaction. ACM SIGCHI Bulletin, 18(2), 43–44. doi: 10.1145/15683.15689.

Rosemann, M., Recker, J., Green, P., & Indulska, M. (2009). Using ontology for the representational analysis of process modeling techniques. International Journal of Business Process Integration and Management, 4(4), 251–265. doi: 10.1504/IJBPIM.2009.032282.

Rubin, H. J., & Rubin, I. S. (2004). Qualitative Interviewing: The Art of Hearing Data (2nd ed.). Sage.

Sarker, S., Xiao, X., Beaulieu, T., & Lee, A. S. (2018). Learning from first-generation qualitative approaches in the IS discipline: an evolutionary view and some implications for authors and evaluators (PART 1/2). Journal of the Association for Information Systems, 19(8), 752–774. doi: 10.17705/1jais.00508.

Scott, L. M., & Janikas, M. V. (2010). Spatial Statistics in ArcGIS. In M. M. Fischer & A. Getis (Eds.), Handbook of Applied Spatial Analysis: Software Tools, Methods and Applications (pp. 27–41). Springer.

Searle, J. R. (1995). The Construction of Social Reality. Free Press.

Silverman, D. (2013). Doing Qualitative Research (4th ed.). Sage.

SimilarWeb. (2020). Estimated total visits to RKI.de. SimilarWeb. Retrieved from November 26, 2020. https://www.similarweb.com/website/rki.de

Sorci, G., Faivre, B., & Morand, S. (2020). Explaining among-Country variation in COVID-19 case fatality rate. Nature Scientific Reports, 10(18909):1–11. doi: 10.1038/s41598-020-75848-2.

Staford, N. (2020). Covid-19: Why Germany’s case fatality rate seems so low. British Medical Journal, 369, m1395:1– 2. doi: 10.1136/bmj.m1395.

Stamper, R. K. (1971). Some ways of measuring information. Computer Bulletin, 15(12), 432–436.

Trang, S., Trenz, M., Weiger, W. H., Tarafdar, M., & Cheung, C. M. K. (2020). One app to trace them all? Examining app specifications for mass acceptance of contact-tracing apps. European Journal of Information Systems, 29(4), 415–428. doi: 10.1080/ 0960085X.2020.1784046.

Tsoukas, H., & Chia, R. (2002). On Organizational Becoming: Rethinking Organizational Change. Organization Science, 13(5), 567–582. https://doi.org/10. 1287/orsc.13.5.567.7810

Urbaczweski, A., & Lee, Y. J. (2020). Information technology and the pandemic: A preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control. European Journal of Information Systems, 29(4), 405–414. doi: 10.1080 0960085X.2020.1802358.

Waizenegger, L., McKenna, B., Cai, W., & Bendz, T. (2020). An afordance perspective of team collaboration and enforced working from home during COVID-19. European Journal of Information Systems, 29(4), 429–442. doi: 10.1080/0960085X.2020.1800417.

Wand, Y., & Weber, R. (1990). An ontological model of an information system. IEEE Transactions on Software Engineering, 16(11), 1282–1292. doi: 10.1109/32.60316.

Wand, Y., & Weber, R. (1993). On the ontological expressiveness of information systems analysis and design grammars. Journal of Information Systems, 3(4), 217–237. doi: 10.1111/j.1365-2575.1993.tb00127.x.

Wand, Y., & Weber, R. (1995). On the deep structure of information systems. Information Systems Journal, 5(3), 203–223. doi: 10.1111/j.1365-2575.1995.tb00108.x.

Weber, R. (1997). Ontological Foundations of Information Systems. Coopers & Lybrand and the Accounting Association of Australia and New Zealand.

Wong, F., & Collins, J. J. (2020). Evidence that coronavirus superspreading is fat-tailed. Proceedings of the National Academy of Sciences, 117(47), 29416–29418. doi: 10.1073/ pnas.2018490117.

World Health Organization. (2010). What is a pandemic?. World Health Organization. Retrieved from November 27, 2020. https://www.who.int/csr/disease/swineflu/fre quently\_asked\_questions/pandemic/en/

Xie, L., Sundaram, H., & Campbell, M. (2008). Event mining in multimedia streams. Proceedings of the IEEE, 96(4), 623–647. doi: 10.1109/JPROC.2008.916362.

Yin, R. K. (2009). Case Study Research: Design and Methods (Vol. 5, 4th ed.). Sage Publications.

## APPENDIX: CASE STUDY PROCEDURES

## Design

I followed an embedded single-case design, following guidelines for positivist case study research (Dubé & Paré, 2003; Miles & Huberman, 1994; Yin, 2009). Through the case study, I tried to learn “facts” (Sarker et al., 2018) about how the design of Germany’s RKI COVID-19 dashboard was completed and about whether my design propositions were viewed as important, actable, and efective (Iivari et al., 2020). The objective of the case study was thus to accurately confront and falsify the design principles with reality.

## Data Collection Procedures

Ethical clearance was granted prior to data collection by the University of Cologne (ref no 200020JR). Table A1 summarises data sources. Primary data were interviews with seventeen stakeholders from six diferent organisations involved with Germany’s RKI COVID-19 dashboard: the main technology provider (Esri), a public health institute, a regional public sector computer support and services provider (RegionalIT) plus three regional public sector institutions from the Cologne region in Germany (a loca crisis management team, an ofice for public real estate cadastre, and a geo-data management team).

Interviewees were purposefully but not randomly recruited through contacts established by Esri on the basis of theoretical sampling criteria (in particular, roles such as technical infrastructure developer, user interface designer, public health expert, cartography expert, regional government, and loca crisis response teams). Interviews were conducted in German and recorded onsite or via videoconferencing between September and November 2020. Average interview length was 58 minutes. Recordings were transcribed, translated, and verified by interviewees. Additional data collected included notes, memos, system screenshots, documentations of additional information systems like SORMAS, an opensource early warning and management system (https://sorma sorg.helmholtz-hzi.de/), diferent corona dashboard variants for regional districts or local crisis management teams (Table A1), and other relevant web pages, such as the NPGeo hub (https://npgeo-corona-npgeo-de.hub.arcgis.com/), or the German Fire Protection Association (https://www.vfdb.de/).

## Data Collection Protocol

Interviews followed a semi-structured interview protocol, which evolved in four iterations over the course of the study. It is registered online at https://doi.org/10.17605/OSF.IO Q3WGV. The protocol was designed with a set of preplanned questions to cover the subject area (Rubin & Rubin, 2004). During the interviews, follow-up inquiries were used in addition to the protocol to gain a deeper understanding of the subject matter or to clarify individual responses. The protocol consisted of four parts: First, clarifying the context and role of the interviewee; second, understanding the design of the corona dashboard, key features, key use cases, and key changes since March 2020; third, evaluating the design principles for state-tracking; and fourth, gathering additional insights and comments.

To evaluate the design principles for state-tracking, I relied on the recommendations and template by Iivari et al. (2020). They suggest five criteria, accessibility, importance, novelty, actability, and efectiveness, to examine whether the prescriptive knowledge for creating instances of IS artefacts contained in the design principles is, in fact, applicable and helpful for practitioners. Of these, accessibility of the design principles (the degree to which practitioners can understand the design principle) was ensured in the interviews by providing clear definitions, explanations, and several examples relevant to corona dashboards (see the interview protocol, part three), rendering the evaluation of accessibility irrelevant. Likewise, novelty (the degree to which a design principles bears potential to surprise practitioners) was deemed irrelevant to the objectives of the case study. In turn, the interview covered evaluations of importance, actability, and efectiveness.

## Data Analysis

A two-pronged strategy was followed. The primary data analysis strategy was hypothetico-deductive (Lee, 1991; Sarker et al., 2018): Data-grounded, inter-subjectively valid, and verifiable claims (Silverman, 2013) were generated to validate or falsify the four design principles for statetracking. Analysis thus involved primarily pattern matching (Yin, 2009), to compare empirically generated evidence (primarily quotes made in the discussion of each criteria for each design principle) with a logical evaluation outcome pattern (a broad categorisation in low, medium, and high) for each design principle. Table A2 provides several illustrative examples.

The secondary data analysis strategy was inductive (Miles & Huberman, 1994), with the aim to develop deeper insights into the rationale of the evaluation of the design principles, that is, why a particular design principles was not deemed actable, and how a design principle was implemented if at all in the in situ artefact-in-use (Chandra Kruse et al., 2019). A thematic analysis was carried out using Gioia et al.’s (2013) methodology to build a data structure that grouped 1<sup>st</sup> order concepts adhering to interviewees’ terms into 2<sup>nd</sup> order conceptual themes, which I captured as tensions (structural paradoxes that require reconciliation, Poole & Van De Ven, 1989) to express the similarities and diferences in the 1<sup>st</sup> order concepts. Table A3 provides illustrative examples.

Table A1. Data sources.

<table><tr><td>Organisation</td><td>Esri</td><td>Public health institute</td><td>RegionalIT</td><td>Local crisis management team</td><td>Office for public real estate cadastre</td><td>District geo-data management team</td><td>Total</td></tr><tr><td>Interviews</td><td>6</td><td>1</td><td>3</td><td>3</td><td>2</td><td>2</td><td>17</td></tr><tr><td>Key Informants</td><td>Executive, business development manager, solution architect, cartographer, user interface designer</td><td>Geo-health specialist</td><td>GIS developer, application consultant</td><td>Department manager, public relations manager, GIS coordination manager</td><td>Department manager, geomatics specialist</td><td>Geo-data manager, crisis management team coordinator</td><td></td></tr><tr><td>Length (minutes)</td><td>316</td><td>70</td><td>51</td><td></td><td>38</td><td>49</td><td>524</td></tr><tr><td>Length (pages)</td><td>93</td><td>20</td><td>17</td><td></td><td>14</td><td>17</td><td>161</td></tr><tr><td>Notes (pages)</td><td>32</td><td>6</td><td>7</td><td></td><td>5</td><td>5</td><td>55</td></tr><tr><td>Additional documents</td><td>4</td><td>1</td><td>1</td><td>1</td><td>3</td><td>1</td><td>11</td></tr><tr><td>Relevant local dashboards and web portals</td><td>https://npgeo-corona-npgeo-de.hub.arcgis.com/); https://npgeo-corona-npgeo-de.hub.arcgis.com/app/ 3a132983ad3c4ab8a28704e9addefaba</td><td>https://health-mapping.de/</td><td>7Tagelnzidenz/</td><td>https://civitec.maps.arcgis.com/apps/opsdashboard/index.html#/0453cba02245458e869241f4070a4393; https://www.giscloud.nrw.de/corona-dashboard.html</td><td>https://experience.arcgis.com/experi ence/</td><td></td><td>0f5d0f9aa11a4bababe775b5c14b</td></tr><tr><td>735f</td><td>https://rhein-erft-kreis.maps.arcgis.com/apps/opsdashboard/index.html#/</td><td>6bd759cc f569448182 e955113418 3300</td><td>https://www.arcgis.com/apps/opsdash board/index.html#/</td><td>252af02201ee4a70bf4190 b339731eee</td><td></td><td></td><td></td></tr></table>

Table A2. Examples for deductive analysis of data.

<table><tr><td>Design principle</td><td>Criteria</td><td>Example quote</td><td>Matched evaluation pattern</td></tr><tr><td rowspan="2">Mapping</td><td>Actability</td><td>Well, the problem is that the state variables that would be most interesting do not exist in the same chronological order as the reported data. There are many different possibilities that could be considered in parallel to the reporting system. But the statistical processing is tedious.</td><td>Low: data processing complicated</td></tr><tr><td>Effectiveness</td><td>We also thought about determining the R-value. I then took a look at the RKI, how is it actually derived. There are so many ways to calculate it inside, so many different results. I would keep my hands off it. We did then too. We&#x27;re careful with that. We don&#x27;t want to give the wrong signal to the outside world.</td><td>Medium: possibly effective but with associated risks</td></tr><tr><td>Tracking</td><td>Actability</td><td>This recovery data is not recorded directly. That is also very difficult. That&#x27;s why the whole process is missing in the health care system, where only the illness is recorded, and estimated values are available. But of course it would also be a great help if you had the data with a better time stamp for a crisis management team.</td><td>Low: lack of data availability</td></tr><tr><td rowspan="3">External event</td><td>Importance</td><td>I think it also makes much more sense to show the correlation between the measures we have taken and the effects. So I think this makes a lot of sense in principle.</td><td>High: logical arguments that support implementation</td></tr><tr><td>Actability</td><td>You would have to find the right place. I think that these graphs on the bottom right are ideal for this purpose. I would first have to investigate a little more closely whether we could display such individual events and what a suitable representation would look like. Superimposed events are, I believe, not technically intended. You need to build something like this from scratch.</td><td>Medium: implementation possible but effort required</td></tr><tr><td>Effectiveness</td><td>If the result now comes out, for example, “despite the use of a mask, the numbers are going up again”, that ultimately leads to people all saying “The mask is nonsense. I&#x27;ll leave it out”. [...] That would lead to misinterpretations among citizens. In this respect, you have to weigh more carefully what you are representing.</td><td>Medium: Risk of misinterpretation possible</td></tr><tr><td>Sequencing</td><td>Actability</td><td>If the data is in a reasonable form that it can be processed, then it is relatively easy to put it on a card. When it starts with getting the data from the individual federal states or the individual districts, then how do you bring it together? What is the data model behind it? Can that be unified? In one rural district the limit is perhaps 50, in the other at 100. That&#x27;s where the problems start, I think, but if you have a clean database, the representation or visualisation on the map is still the nice accessory, but the main work is in data preparation.</td><td>Medium: data preparation required</td></tr><tr><td>Sequencing</td><td>Importance</td><td>I think it is absolutely necessary to go in this direction, that one somehow depicts the complexity with all its interactions. You can do that. It&#x27;s not a big problem mathematically either.</td><td>High: Very relevant solution with limited complexity</td></tr></table>

Table A3. Examples for inductive analysis of data.

<table><tr><td>Example quote</td><td> $1^{st}$  order concept</td><td> $2^{nd}$  order theme</td></tr><tr><td>So this is of course also a huge challenge to collect these data and federalism is not exactly playing into our hands, if you like to put it that way, because every region has its own publication mechanisms and platforms to disclose such things. And in some cases, you can no longer find them at all.</td><td>Federalism in data reporting</td><td>Administrative tension: federated legislation versus centralised information infrastructure</td></tr><tr><td>I know that in [a different district], for example, the dashboard is operated by the data processing centre and not by the district administration. And the public health department is included in the district administration. We don&#x27;t have a data processing centre, we only have an IT department, and we ourselves are more or less independent, and we are also members of the crisis team. This means that we ourselves can react quickly but do not have to access a data processing centre. [...] There is always the question: who maintains the data there?</td><td>Information ownership and solution sovereignty</td><td>Administrative tension: federated legislation versus centralised information infrastructure</td></tr><tr><td>If you compare that with weather forecasts, where you have collected something over the years, you have models, you have that. You can also use a dashboard and visualise it. If you apply it to this case, you simply have to gain a little experience. [...] And then you can perhaps get more valid forecasts. [...] The most important thing is official and really verified data, because there is also enough fake news and whatever else is thrown around.</td><td>Learning about forecasting from other scenarios</td><td>Temporal tension: Accurate historical data versus uncertain forecast data</td></tr><tr><td>Of course, we also have this forecast data, but it has been shown, or was agreed, that such data does not belong in a public dashboard. Only the pure facts should be included, in order not to make oneself vulnerable to attack.</td><td>Availability and vulnerability of forecast data</td><td>Trust tension: Confidence in data processing versus data interpretation</td></tr><tr><td>And so that means such uncertainty – we&#x27;ve discussed this, can one represent the uncertainty of the numbers? It can be represented, but we know that the public in particular cannot deal with it.</td><td>Provision versus interpretation of uncertain data</td><td>Trust tension: Confidence in data processing versus data interpretation</td></tr></table>
