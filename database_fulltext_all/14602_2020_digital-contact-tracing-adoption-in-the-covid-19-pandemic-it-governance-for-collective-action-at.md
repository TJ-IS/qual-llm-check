---
otero_id: 14602
otero_key: "43G8BBTK"
title: "Digital contact-tracing adoption in the COVID-19 pandemic: IT governance for collective action at the societal level"
authors: "Kai Riemer; Raffaele Ciriello; Sandra Peter; Daniel Schlagwein"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1819898"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Digital contact-tracing adoption in the COVID-19 pandemic: IT governance for collective action at the societal level

Kai Riemer , Raffaele Ciriello , Sandra Peter & Daniel Schlagwein

To cite this article: Kai Riemer , Raffaele Ciriello , Sandra Peter & Daniel Schlagwein (2020): Digital contact-tracing adoption in the COVID-19 pandemic: IT governance for collective action at the societal level, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1819898

To link to this article: https://doi.org/10.1080/0960085X.2020.1819898

![](/api/attachments/43G8BBTK/fulltext/images/2219c916ac9467a2f5eede160e6b7edf4a9433a7b92843505834f91b22d427e2.jpg)

Published online: 23 Sep 2020.

![](/api/attachments/43G8BBTK/fulltext/images/e998dfc79eeac46cb0c6d932ff0297bb81b09ce388c245db0e8257ac642bf527.jpg)

Submit your article to this journal

![](/api/attachments/43G8BBTK/fulltext/images/d8be573b4ec90a5d51b2e0fec369397549b09c1051a4965c7b26a7541624ad96.jpg)

View related articles

![](/api/attachments/43G8BBTK/fulltext/images/7688054472c65e9e2f1d6a5d8590fc37bfee18130ac97caab04c501353e9a114.jpg)

View Crossmark data

Check for updates

# Digital contact-tracing adoption in the COVID-19 pandemic: IT governance for collective action at the societal level

Kai Riemer <sup>a</sup>, Rafaele Ciriello <sup>a</sup>, Sandra Peter <sup>b</sup> and Daniel Schlagwein <sup>a</sup>

<sup>a</sup>Business Information Systems, The University of Sydney, Sydney, Australia; <sup>b</sup>Sydney Business Insights, The University of Sydney, Sydney, Australia

## ABSTRACT

The COVID-19 pandemic has created a need for rapid, population-wide digital contact tracing. One solution, Bluetooth-enabled digital proximity tracing using smartphones, promises to preserve individual privacy while helping to contain society-wide viral outbreaks. However, this digital solution works efectively only if adopted by the majority of the population. This poses a collective action problem: everyone would benefit from wide-spread proximity tracing, but the benefits for the individual are indirect and limited. To facilitate such collective action at the societal level, this paper conceptualises the option space of IT governance actions for proximity tracing adoption along two dimensions: decision-making entities (who will govern the roll-out) and accountability enforcement (how strictly will adoption and use be enforced). Examining coherent governance approaches that arise from the framework, we show that there are no globally ideal approaches but only locally contextualised ones that depend on immediate health risk, prior experience with pandemics, societal values and national culture, role of government, trust in government and trust in technology in each society. The paper contributes specific propositions for governing digital contact tracing in the COVID-19 pandemic and general theoretical implications for IT governance for collective action at the societal level.

ARTICLE HISTORY Received 16 May 2020 Accepted 2 September 2020

KEYWORDS IT governance; collective action; digital contact tracing; proximity tracing; COVID-19; pandemics

## 1. Introduction

Digital contact tracing has emerged as an important measure for curbing the pandemic spread of SARS-CoV-2, the virus causing the COVID-19 respiratory disease (Sun & Viboud, 2020). Contact tracing is a public health practice to identify and notify those people who had contact with an infected person during their contagious period. Conventional, manual contact tracing relies on people’s recollection and does not scale well in episodes of rapid viral spread (Ferretti et al., 2020). A range of digital contact-tracing solutions have recently been proposed, varying in eficacy and privacy implications. For instance, surveillance tracing utilises a range of digital data collection approaches and surveillance technologies to retrospectively trace the locations an infected person has visited. By contrast, proximity tracing uses Bluetooth to ascertain proximity between smartphones to determine and build a record of local contacts between people as they occur. In case of an infection those records can then be used to notify those people who an infected person has come in contact with.

While early research indicates the eficacy of the approach (Urbaczewski & Lee, 2020), proximity tracing will only be efective and achieve its intended health, economic and societal benefits if a significant user base adopts and uses the service (Ferretti et al.,

2020). Hence, in addition to design considerations (Trang et al., 2020), appropriate governance approaches are required to ensure rapid, populationwide adoption of digital proximity tracing. We thus ask: How can the rapid, population-wide adoption of proximity tracing using digital devices for curbing pandemic spreads be governed? While we focus on the specific COVID-19 pandemic scenario, answering this question has general implications for IT governance for collective action at the societal level.

From a theoretical viewpoint, the problem at hand, namely achieving wide-spread societal adoption of a digital solution, is one of “collective action” (Allison & Kerr, 1994; Dawes, 1980). Collective action refers to the actions taken by a group of people to achieve a common goal (Olson, 1965). However, collective action is dificult to achieve when there are limited immediate benefits or even drawbacks for individuals from acting, or when individual interests conflict directly with collective interests (Dawes, 1980). Then, a free-rider problem might arise whereby individuals try to benefit from the common good without contributing, thereby putting its production in jeopardy (Olson, 1965).

In the case of digital contact tracing, people may a) actively resist adoption because of privacy concerns, b) procrastinate due to the efort required (e.g., installing the app) or c) consider that they can benefit without adopting themselves (e.g., digital contract tracing will be efective if a majority of citizens adopt). Consequently, collective action, the widespread adoption of digital contact tracing on smartphones for the common good, needs to be actively and appropriately governed. The question then arises, how should such IT governance be organised and who is responsible for it?

To address this issue, we begin with a brief review of the IT governance literature in section 2. It shows that prior research has addressed IT governance arrangements at the intra-, inter- and supraorganisational levels, yet IT governance at the societal level remains under-explored. In section 3, we introduce digital contact tracing and its various incarnations in detail. In particular, we show that success depends on overcoming the collective action problem.

In section 4, we draw on the IT governance literature to develop a framework that conceptualises the option space of governance actions. We reason that there are four distinct types of decision-making entities that may engage in IT governance for collective action at the societal level (i.e., individuals, organisations, platforms and governments). Further, we distinguish four levels of accountability enforcement that determine how collective actions are enforced and monitored (i.e., voluntary, encouraged, nudged and mandated).

In section 5, based on the framework, we suggest concrete approaches for the governance of proximity tracing adoption in the COVID-19 pandemic. We argue from the premise that wide-spread adoption of digital proximity tracing will lead to better health, economic, and societal outcomes. Thus, we first show under what conditions societies can achieve the adoption and use of proximity tracing and what barriers, such as privacy concerns, stand in the way. We then consider factors that impact the selection of governance approaches. These include both pandemicspecific factors, such as the stage of the pandemic and prior pandemic experience in a country/region, as well as macro factors such as societal values, and role of, and trust in, governments and technology in the respective society/country.

The immediate, time-sensitive contribution of the paper is to inform governance decisions for achieving adoption of digital contact tracing in the COVID-19 pandemic. The wider, general contribution of the paper to the IS literature is a theoretical framework for the largely under-researched issue of IT governance for collective action at the societal level. The framework conceptualises possible governance actions and pragmatic governance approaches. This will help governments, platform providers, organisations, and individuals in structuring their governance actions in comparable situations where rapid, wide-spread use of digital technology is needed, including for future pandemics.

## 2. IT governance in the literature

IT governance has been an important topic of IS research. So far, prior research has addressed IT governance arrangements at the intra-, inter- and supraorganisational levels but, as this section shows, the societal level has been largely overlooked. Yet, the COVID-19 pandemic has created an unprecedented need for governing the rapid, population-wide adoption of digital contact tracing at the societal level.

## 2.1. IT governance at diferent organisational levels

Governance, in general, refers to the processes of decision-making among the actors involved in some form of collective efort (Hufty, 2011). IT governance specifically “represents the framework for decision rights and accountabilities to encourage desirable behaviour in the use of IT” (Weill, 2004, 3). As summarised in Table 1, the literature on IT governance is welldeveloped at the intra-, inter-organisational, and supra-organisational levels, but less so at the societal level, the focus of this paper.

For most of the past four decades, research on IT governance has considered the intra-organisational level, the decision-making processes within a single organisation (Dawson et al., 2016; Magnusson et al., 2020). The 1980s and 1990s marked a shift away from siloed IT departments governed by adhocracy (Mintzberg & McHugh, 1985) and towards formalised IT governance by central management (Weill & Ross, 2004) or IT steering committees (R. Huang et al., 2010). This formalisation continued throughout the 2000s along the path of governing the IT department by a strict supply-and-demand logic (Chen et al., 2010), leading to the “internal market” as the dominant arrangement (Guillemette & Paré, 2012). More recently, internal market arrangements have been challenged by the ongoing consumerization of IT (Leclercq-Vandelannoitte & Bertin, 2018), thus giving way to multi-stakeholder approaches (Boonstra et al., 2018).

IT governance has also been studied at the interorganisational level, including in the context of IT marketplaces. This includes the governance of IT buyer-supplier relationships (Xiao et al., 2013) or other forms of external sourcing of IT products and services (Lacity & Hirschheim, 1993). Although still in a nascent stage, the past decade has seen a further increase in research focused on the governance of inter-organisational systems (Fedorowicz et al., 2018; Grant & Tan, 2013), giving rise to networked governance arrangements that emphasise shared accountability over hierarchical control and efectiveness over eficiency (Provan & Kenis, 2008).

Table 1. Overview of stream in the IT governance literature.

<table><tr><td>Scope</td><td>Focus</td><td>References</td></tr><tr><td>Intra-organisational governance</td><td>Formalisation of decision-making processes related to the IT department within a single organisation, typically governed via internal markets or top-down managerial strategy.</td><td>(Chen et al., 2010); (Guillemette &amp; Paré, 2012); (Magnusson et al., 2020); (Mintzberg &amp; McHugh, 1985); (Weill &amp; Ross, 2004)</td></tr><tr><td>Inter-organisational governance</td><td>Efficiency and effectiveness of decision-making processes in inter-organisational systems, typically governed via markets or networked arrangements.</td><td>(Grant &amp; Tan, 2013); (Fedorowicz et al., 2018); (Lacity &amp; Hirschheim, 1993); (Provan &amp; Kenis, 2008)</td></tr><tr><td>Supra-organisational governance</td><td>Coordination of decision-making processes in digital platforms, technology ecosystems or information infrastructures, typically governed via polycentric arrangements.</td><td>(De Reuver et al., 2018); (Ghazawneh &amp; Henfridsson, 2015); (Gregory et al., 2018; Mindel et al., 2018); (Wareham et al., 2014)</td></tr><tr><td>Societal-level governance</td><td>Selection of decision-making entities and their accountability enforcement among actors in a society involved in a collective action problem.</td><td>This paper.</td></tr></table>

Closely related to research on networked governance arrangements is the recently growing literature on IT governance at the supra-organisational level, beyond a focal organisation or dyadic relationships. Polycentric governance arrangements, emphasising coordination of decision-making processes that are distributed among a range of actors (Mindel et al., 2018; Ostrom, 1990), are particularly dominant at this level. So far, research has primarily been concerned with decision-making processes in digital platforms (e.g., Ghazawneh & Henfridsson, 2015; De Reuver et al., 2018), technology ecosystems (e.g., Wareham et al., 2014) or information infrastructures (e.g., Mindel et al., 2018). The ongoing digitisation of society creates an increasing need for more liberal (Leclercq-Vandelannoitte & Bertin, 2018) and individualised IT governance approaches (Gregory et al., 2018).

## 2.2. Need for IT governance at the societal level

We conclude that interest in the IT governance domain has progressively moved outward, away from the single intra-firm IT function towards decentralised and networked governance at the inter- and supraorganisational level. Our study contributes to this progression, but we are here concerned with a case of IT governance at the societal level, an organisational level of IT governance that has so far remained understudied.

The current IT governance literature calls for considering more liberal IT governance approaches that widen governance to include non-traditional stakeholders and a wider range of governing mechanisms that rely on choice rather than coercion (Leclercq-Vandelannoitte & Bertin, 2018, 342). Yet, most of the IT governance literature takes for granted that there is an a priori defined governing entity, such as an organisation that is tasked with governance. In contrast, our case – achieving adoption of digital contact tracing at the societal level – requires decisions about both: appropriate governing mechanisms as well as the entities that are to do the governing, as they are not pregiven.

Table 1 provides an overview of the major streams in the IT governance literature as outlined here, and how this paper is positioned.

## 3. Digital contact tracing

This section provides an overview of contact tracing and its digital implementations (see Table 2 for a summary). We introduce the benefits of digital contact tracing, and discuss various concerns related to its digital nature, such as surveillance and privacy. Finally, we identify as the main challenge the collective action problem of achieving rapid population-wide adoption of the smartphone apps or services facilitating digital proximity tracing, which motivates this study.

Table 2. Comparison of contact tracing approaches.

<table><tr><td>Approach</td><td>Example</td><td>Benefits</td><td>Drawbacks</td></tr><tr><td>Manual Contract Tracing</td><td>Common practice at prior pandemics, such as MERS, SARS1, or HIV.</td><td>Well understood, effective, accepted, and institutionalised.</td><td>Error-prone, time-intensive, labour-intensive, privacy- invasive, does not scale in rapid outbreaks.</td></tr><tr><td>Surveillance Tracing</td><td>South Korea&#x27;s “Virtuous Surveillance”.</td><td>Effective, top-down, comprehensive, no population acceptance needed.</td><td>Not suitable for individualistic societies, highly privacy invasive, risk of surveillance state.</td></tr><tr><td>Proximity Tracing (centralised)</td><td>Singapore&#x27;s “TraceTogether”, Australia&#x27;s “COVIDSafe” Apps.</td><td>Effective (if widely used), public sector controlled, integrates with manual tracing.</td><td>Privacy concerns towards governments, no automatic rollout possible</td></tr><tr><td>Proximity Tracing (decentralised)</td><td>Apple-Google&#x27;s Exposure Notification.</td><td>Effective (if widely used), global, not privacy invasive, infrastructure already in place, direct OS access, automatic rollout possible.</td><td>Private sector controlled, privacy concerns towards corporations, lack of public control and no integration with manual tracing.</td></tr></table>

## 3.1. Manual contact tracing

Contact tracing is a public health measure to control the outbreaks of infectious diseases. The key is to identify and warn people that have been at risk of infection through contact with infected patients or contagious locations. Conventional manual contact tracing is a labour-intensive process that is not unlike detective work. Manual contact tracing follows a series of steps (ASHM, 2016):

(1) Obtain consent to carry out contact tracing from the infected or suspected patient.

(2) Work with the patient to re-trace their whereabouts during the contagion period.

(3) List any contacts the patient interacted with during the contagion period.

(4) Visit places of potential contagion as well as establish ways of contacting identified individuals.

(5) Notify identified individuals personally of exposure (e.g., via visit or call) and advise them what to do (e.g., get tested or selfisolate).

Contact tracing is an important measure to identify and contain clusters of outbreaks. Visiting and approaching people in person is considered to lead to better compliance with health recommendations (e.g., testing or self-isolating) compared to, for example, general warnings via digital messages (Ferretti et al., 2020).

However, manual contact tracing has considerable shortcomings that limit efectiveness for fastspreading pandemics such as COVID-19 (Ferretti et al., 2020). The shortcomings include:

● Error proneness: Health workers need to rely on patients’ recollection of whereabouts and contacts. Recollection is often fallible. Additionally, patients may be unwilling to make full disclosure and they might also have come in contact with people they do not know.

● Time intensity: Valuable time is lost during which new infections might occur.

● Labour intensity: Manual contact tracing can be overwhelmed in case of pathogens with high infection rates and case numbers.

● Privacy invasion: The patient has to give up the names and contact details of those they have been in contact with.

Digital contact tracing can alleviate some or all of the shortcomings of manual contact tracing (Ferretti et al.,

2020). Two main digital approaches have been developed in the context of the COVID-19 pandemic, surveillance tracing and proximity tracing.

## 3.2. Surveillance tracing

Surveillance tracing is carried out by government entities in a top-down way and uses a range of data collection and surveillance technologies to retrospectively retrace the movements and contacts of a newly diagnosed infected patient. Surveillance tracing is generally considered to be highly privacy invasive for both the patient and those potentially exposed. It requires a wide variety of digital data, such as GPS and cell phone location data, data from social media platforms, CCTV camera and facial recognition data, travel booking data, and other surveillance data points. The aim is to reconstruct movement patterns and to contact those who have interacted with or frequented locations at the same time as the case person. During the COVID-19 pandemic, forms of surveillance tracing have been used in China (Law, 2020), Israel (Tidy, 2020), and South Korea (Dave, 2020a). While considered successful in curbing the spread of the virus, the approach has been criticised for privacy invasion and unintended consequences (Zastrow, 2020).

## 3.3. Proximity tracing

## 3.3.1. Overview

Proximity tracing is based on collecting proximitybased data while contacts between people take place (instead of tracing retrospectively). The key idea is to use proximity-based data generated and collected by standard smartphones to alert the contagion period contacts of a newly diagnosed patient. The technology of choice for establishing a contact between two smartphones (considered a contact between their users) is Bluetooth Low Energy (BLE), a version of Bluetooth available in modern smartphones. Proximity tracing works as follows (Li & Guo, 2020):

● Instal service: The user instals the service (e.g., via app download or OS update) on their smartphone and activates Bluetooth. The phone is registered with an ID at a central infection tracking server.

● Send/collect contact IDs: The service operates in the background of a user’s phone and acts as a beacon and receiver. The service sends out its own ID and collects the IDs of other users located within a certain radius and time span (e.g., closer than two metres for at least 15 minutes).

● Disclose infection: When a user tests positive, he/ she enters this into the service on their phone.

The service then registers the infection with the contact tracing server.

● Notify exposed users: If a user has been in proximity to an infected patient who also used the service, then the user receives a notification as well as instructions what to do (e.g., to self-isolate or to get tested).

Two main versions of proximity tracing have emerged, namely centralised and decentralised proximity tracing. They difer in the role of a central entity for registering devices, collecting and managing proximity information and notifying at-risk users, and the corresponding privacy implications.

## 3.3.2. Centralised proximity tracing

In centralised proximity tracing, users register their phone number with the centralised authority, which then creates the anonymised IDs that devices exchange. Anonymity is thus preserved between devices and (through encryption) also from third parties (Asghar et al., 2020), but not vis-à-vis the central authority (such as government health agencies). The central server is in charge of decrypting keys and contacting devices of exposed users via their phone numbers (Criddle & Kelion, 2020). As a result, an element of surveillance remains, but proponents stress that health authorities regain better control for coordinating the pandemic response. This approach is favoured by countries such as Singapore, Australia, France, and Norway (Kelion, 2020b; Lomas, 2020). The first proximity solutions in use were all centralised, such as the TraceTogether<sup>1</sup> app, used by the government of Singapore in its successful early response to the outbreak (Y. Huang et al., 2020; Taylor, 2020), and Australia’s COVIDSafe<sup>2</sup> app, which is modelled on Singapore’s architecture.

## 3.3.3. Decentralised proximity tracing

In decentralised proximity tracing, users register with the central server anonymously. Instead of centralised registration of exposed users and push notifications to devices, each device pulls all known IDs of infected users from the server and compares these with the decentral, locally held list on the device, which means the server does not need to know the identity of any device (Kelion, 2020a).

The most prominent decentralised implementation is Apple and Google’s “Privacy-Preserving Contact Tracing” (Apple, 2020b), which has the broadest potential reach in terms of geography due to the worldwide duopoly of the iOS and Android operating systems. The companies announced on April 11 2020 that they would integrate a dedicated API into both iOS and Android (Apple, 2020a). The API launched in May 2020 and is known as “Exposure Notification API”; 23 countries requested and received access immediately after its launch (Howell O’Neill, 2020a), and as of August 1 2020 16 countries have successfully launched proximity tracing apps based on the API (Dave, 2020b). On September 1 2020 Apple further extended the service integrating it into iOS to work without a dedicated app (Google will follow). Health authorities still have to elect to participate, but they only need to provide Apple and Google with relevant health information, without the need for a dedicated app. Users will be notified if the service is available in their area, but then have to actively opt in to use it (Etherington, 2020). A few countries have already reported initial success with tracing cases using the API (Cellan-Jones, 2020; Cellan-Jones & Kelion, 2020). For example, in Germany, as of September 1 2020, more than 2,500 newly diagnosed patients had requested the transaction IDs to initiate the process of notifying their contacts.

The Apple/Google solution has a number of benefits. First, it promises the highest user privacy protection. Second, the solution could cover up to 99% of all smartphone users given the market penetration of iOS and Android (Statista, 2020). Third, because it is a government-independent solution, it works worldwide which will potentially enable international travel as apps might have the ability to perform data handover. Fourth, implementation in the OS allows privileged access to system functions. This resolves technical problems of tracing apps such as with accessing Bluetooth or measuring Bluetooth signal strength for establishing accurate proximity (Howell O’Neill, 2020b). Hence, OS implementation is expected to increase precision and to reduce the number of false positives (Newton, 2020). Finally, OS implementation has the potential to create a “future-proof” digital infrastructure that would allow for fast reactivation in future outbreaks or pandemics. That is, while Apple and Google announced to take the system ofline after the COVID-19 pandemic (Apple, 2020b), the same system could be rapidly rolled out again for future pandemics.

## 3.4. Privacy vs. control

The above makes clear that no solution is ideal in all situations. If a broad range of data sources are available, then surveillance tracing might be the most efective solution. It can be executed top down and does not require user adoption. Yet, surveillance tracing raises privacy concerns, and hence, depending on the society in question, might be culturally unacceptable or legally impossible to implement.

Centralised proximity tracing provides health authorities with more control because it allows them to integrate proximity tracing with manual contact tracing (Gladstone, 2020). Because of centralised data storage, health authorities have access to the list of contacts when a user tests positive, which provides more control in informing other users at risk (Taylor, 2020). However, while less intrusive than surveillance approaches, privacy concerns vis-à-vis health authorities still remain, such as expressed in Australia (Farrell, 2020). In response to such concerns, many European countries, such as Germany, Switzerland, Italy, Ireland, and Latvia have moved during the development of their solutions from a centralised to a decentralised approach (Busvine & Rinke, 2020; Horowitz & Satariano, 2020; Kelion, 2020c). There have also been documented cases of centralised proximity tracing apps collecting additional real-time GPS-based location data, thus providing intrusive means for user surveillance (Garthwaite & Anderson, 2020). Notably, Norway pulled its centralised proximity tracing app over surveillancerelated privacy concerns (Howell O’Neill, 2020d).

The decentralised solution developed by Apple and Google appears to be the most promising in terms of privacy and technology. Yet, increased privacy comes at the cost of less control for health authorities. That is, the decentralised solution in the design described above does not reveal the kind of data that would be helpful for authorities to contact users via other means to centrally coordinate the pandemic response, or to know how many contacts have successfully be informed of a potential exposure (Cellan-Jones & Kelion, 2020). Overall, important aspects of pandemic control shift from health authorities to individual users and corporations.

In summary, governments (or other governing bodies) will need to alleviate privacy concerns (Morley et al., 2020) and find ways to convince a majority of the population to use digital contact tracing. Achieving wide-spread adoption of contact tracing apps however presents as a collective action problem which demands efective IT governance at the societal level.

## 3.5. Proximity tracing adoption as a collective action problem

Estimates suggest that contact tracing apps could efectively stop the pandemic if 50–70% of the population would use them (Ferretti et al., 2020; Scott, 2020). While it provides some positive efects at any rate of adoption (Howell O’Neill, 2020c), it becomes exponentially more efective with higher adoption rates. Yet, at the time of writing, adoption rates are still quite low in many societies, even in societies with high collectivism and relatively less privacy sensitivity such as Singapore (Consultancy.asia, 2020; Dalzell & Probyn, 2020).

The underlying problem is best understood as a collective action problem: a situation in which individual interests (e.g., privacy concerns and efort avoidance) conflict with collective interests (Dawes, 1980). Proximity tracing presents a special case of a collective action problem, namely a public good dilemma. A public good is non-exclusive and noncompetitive, meaning that anyone can benefit from it and one person’s use does not hinder another person’s use. In a public good dilemma, the whole group benefits if some members cooperate but individuals benefit from free-riding if enough others cooperate (Allison & Kerr, 1994). In the case of proximity tracing, all individuals benefit from collective use, regardless of whether or not they are among the 50–70% adopters, which presents the free-riding problem referred to above.

Research on collective action problems has shown that cooperative behaviour is predominantly conditional: most people cooperate out of reciprocity, not altruism (Axelrod & Hamilton, 1981). A systematic review of 17 studies on various collective action problems involving over 7000 individuals showed that in a typical scenario only 3% of a population can be expected to cooperate independently of others, 20% can be expected to act selfishly (i.e., free ride), 60% cooperate if they believe others will, 10% stop cooperating when enough other people cooperate, and 7% behave unpredictably (Thöni & Volk, 2018). While these percentages will vary from situation to situation, it is clear that a collective approach cannot per se be expected in many modern societies, if not suficiently governed. Hence, collective action problems pose a need for appropriate governance (Ostrom, 1990).

Collective adoption in the case of contact tracing apps is further aggravated by the fact that such apps, in contrast to many consumer apps, have very limited immediate individual benefits (cf. Mindel et al., 2018). They only become useful in the case of an infection, which reduces individual incentives for adoption. Achieving wide-spread adoption of these apps for collective action is thus primarily a governance question. The key question is not one of individual usefulness, but one of appropriate governance of collective action at the societal level for the common good.

Additionally, inertia to the adoption of digital contact tracing in the form of privacy concerns have to be overcome (as discussed above). US polling data suggests that only 50% of the population would “definitely or probably” use proximity tracing for COVID-19, with privacy concerns topping the list of reasons for why people would not use it (Roper, 2020). While the exact numbers will fluctuate with context, polls such as this show the challenge societies are facing in reaping the collective benefits of proximity tracing.

We thus argue that achieving adoption and use of proximity tracing is fundamentally a matter of collective action which requires efective IT governance at the societal level. We thus ask: How can the rapid, population-wide adoption of proximity tracing apps be governed?

## 4. IT governance for proximity tracing adoption

IT governance refers to “the framework for decision rights and accountabilities to encourage desirable behaviour in the use of IT” (Weill, 2004, p. 3). In our scenario, the desirable behaviour to be governed is the wide-spread adoption of digital contact tracing apps or services (in the absence of immediate individual usefulness). Two key issues arise. Firstly, the question of the location of decision rights (R. Huang et al., 2010): who will govern the roll-out and adoption of proximity tracing apps? Secondly, the question of accountability enforcement: how strictly will the adoption and use be enforced and monitored? We account for these issues by developing a framework for IT governance at the societal level whereby these two aspects combine to create the option space of possible IT governance actions.

## 4.1. IT governance decision-making entities

Decision rights in relation to governance concern the right to make or implement decisions (Fama & Jensen, 1983). Decision rights are held by entities that control actions, make decisions, and provide incentives. For the context of digital contact tracing, given its wide societal reach and the fact that the need for it naturally arises, the governing entities are not pre-given. A multitude of entities could be involved (Ghazawneh & Henfridsson, 2015; Mindel et al., 2018; De Reuver et al., 2018; Wareham et al., 2014). The groups of governance-relevant decision-making entities are as follows:

● Individuals: People may govern their actions individually in their local contexts and social structures, such as cliques or families.

● Organisations: Corporations, associations, universities, government organisations, or churches may govern organisational members through internal rules and procedures.

● Platforms: Digital platforms may create technology or rules that regulate and control platform users.

● Governments: Governments of all levels – such as state and federal governments – may govern the actions of citizens within the applicable legal or physical space.

A concrete, situational IT governance approach thus might involve any combination of the above entities in the decision-making and policy-setting.

## 4.2. IT governance accountability enforcement

Accountability in the context of governance means that entities demonstrate responsibility for their actions (not) taken and the consequences of these (in-)actions (Mulgan, 2000). Enforcement of accountability is crucial to ensure people are rewarded or punished appropriately for actions they are accountable for (Moldoveanu & Martin, 2001). Yet, the level of accountability enforcement can vary, with recent calls advocating for IT governance to broaden its approaches beyond mandated adoption and coercion to choice- and incentive-based governance (Leclercq-Vandelannoitte & Bertin, 2018). The relevant levels of accountability enforcement for the context of digital contact tracing are thus as follows (Grant & Tan, 2013; Provan & Kenis, 2008; Wareham et al., 2014; Weitzner et al., 2008):

● Voluntary: The people governed are fully autonomous to engage in collective action (or not). Actions are not controlled or enforced.

● Encouraged: The people governed are encouraged to engage in collective action. System designs might take the form of “opt-in”.

● Nudged: The people governed are actively guided to engage in collective action through incentives yet retain the freedom to choose otherwise. System designs might take the form of “opt-out” (Thaler & Sunstein, 2009; Weinmann et al., 2016).

● Mandated: The people governed are forced and controlled to engage in collective action through contracts, legal frameworks, technological designs etc.

In sum, a concrete governance approach may rely on accountabilities that are enforced in diferent ways and at diferent levels of strength.

## 4.3. Option space of IT governance actions for proximity tracing adoption

The above two dimensions, decision-making entities and level of accountability enforcement, allow to conceptualise the option space of possible IT governance actions to achieve digital contact tracing adoption. Table 3 outlines the option space of governance actions. While developed here in the context of digital proximity tracing, Table 3 can be seen as a general governance framework for achieving collective action at the societal level in a multitude of IT scenarios.

The first row of Table 3 concerns individual-level governance. At the voluntary level, the individual decision is entirely private, not influenced by others (“laissez-faire”). Individuals may not care or dare interfering with other people’s choices related to the use of proximity tracing. At the encouraged level, individuals may act as role models for others such as through recommending proximity tracing to friends, posting about it on social media, join interest groups, or openly communicating about it at work. At the nudged level, individuals may pressure peers into collective action, such as by avoiding (physical) contact with people who do not use proximity tracing or, more positively, expressing appreciation for people who do. At the mandated level, individuals take action to denounce peers that do not comply with the collective action such as by demanding proof that proximity tracing is activated before allowing someone entry to a facility (e.g., their home, shop or ofice) or, where applicable, reporting non-use to the police.

Table 3. Option space of IT governance actions for proximity tracing adoption.

<table><tr><td rowspan="2">Decision-Making Entity</td><td colspan="4">Accountability Enforcement</td></tr><tr><td>Voluntary</td><td>Encouraged</td><td>Nudged</td><td>Mandated</td></tr><tr><td>Individual</td><td>Laissez-faire</td><td>Role model</td><td>Peer pressure</td><td>Denunciation</td></tr><tr><td>Organisation</td><td>Memo</td><td>Guidelines</td><td>Incentives</td><td>Contract or order</td></tr><tr><td>Digital Platform</td><td>Apps or API</td><td>OS, opt-in</td><td>OS, opt-out</td><td>OS, always on</td></tr><tr><td>Government</td><td>Ads &amp; public information</td><td>Guidelines</td><td>Economic pressure</td><td>Required by law and enforced</td></tr></table>

The second row of Table 3, organisational governance, is concerned with increasing adoption and use by stakeholders of an organisation (e.g., employees, customers, students, partners, etc.). At the voluntary level, the organisation might refrain from acting or merely provide information about proximity tracing, for instance, via memos, newsletters, intranet pages or banners. At the encouraged level, the organisation uses guidelines for proximity tracing. While still voluntary, employees or customers are actively encouraged to activate the service. At the nudged level, the organisation provides incentives for using proximity tracing. This could include rewards (such as free or discounted access to services such as health insurance, sports classes, online courses) or punishments (such as preventing access to social gatherings). At the mandated level, the organisation requires employees or customers to use proximity tracing via contract or order, for instance, via beacons that detect the feature and, if turned of, prevent doors from opening and elevators from running.

The third row of Table 3, platform provider governance, is concerned with the way proximity tracing is embedded directly into smartphone devices. At the voluntary level, the smartphone ofers the ability to instal a standalone app for proximity tracing, either apps or those that built on the Apple-Google API, but activation is up to each user. At the encouraged level, Bluetooth-based proximity tracing is built into the smartphone OSes. While turned of by default, the user is encouraged via notifications to advise to optin and activate the feature. At the nudged level,

Bluetooth-based proximity tracing is built into smartphone OSes and turned on per default, but the user can opt-out. At the mandated level, OS-based proximity tracing is always activated and cannot be turned of by the user. The only ways to resist would then be to not update the OS, switch to a brand without the feature, or stop using the smartphone.

The fourth row of Table 3, state/federal governance, is concerned with the way public institutions make and enforce decisions related to proximity tracing. At the voluntary level, governments, through public broadcasting advertise and inform about proximity tracing via radio, newspapers, TV, and Internet. At the encouraged level, authorities provide explicit guidelines for proximity tracing and communicate them via oficial websites, social media channels, and government agencies. At the nudged level, the government de facto mandates proximity tracing through economic pressures, such as by making welfare benefits contingent upon the use of the feature, requiring employers to opt-in, or requiring pubs, restaurants, event locations, and other licenced premises to check for activation. At the mandated level, governments legally enforce proximity tracing at all times, for instance, via random police checks.

## 5. IT governance for proximity tracing in the COVID-19 Pandemic

The previous section outlines in detail the various possible governance actions for proximity tracing adoption of diferent decision-making entities and at diferent levels of enforcement. This section discusses how societies can decide which concrete governance approaches (i.e., sets of those governance actions) to choose, focusing on the COVID-19 pandemic.

Governance approaches leading to more widespread use of proximity tracing are expected to have better outcomes and should hence be chosen. On the one hand, early empirical findings suggest that mandated enforcement of proximity tracing adoption would yield the best health outcomes (Urbaczewski & Lee, 2020). However, such an approach would be considered intolerable or may even be illegal in many societies, particularly Western ones. On the other hand, the least favourable outcomes would arise from no active governance, if proximity tracing is completely left to everyone as a voluntary choice. We thus argue that societies need to find the best trade-of between what is necessary and what is tolerable in choosing governance approaches within our framework that best suit their specific needs.

We begin with a brief discussion of factors that will influence such decisions, before we outline the contextual considerations for employing particular approaches within our framework.

## 5.1. Factors influencing IT governance approaches at the societal level

There are immediate, pandemic-related factors, as well as more general societal, cultural and socio-political factors to consider. The first consideration for choosing a suitable governance approach is the immediate health risk to the population in terms of the stage of the pandemic outbreak (Morley et al., 2020). Specifically, governments will be more inclined to mandate contact tracing, particularly for essential workers who cannot work from home, at the height of an outbreak (at the “top of the curve”) when the spread threatens to overwhelm the health system.

A second consideration that directly relates to the pandemic itself is the prior experience of a society with previous pandemic outbreaks. Societies with pandemic experience, such as Taiwan’s or South Korea’s experience with MERS/SARS1, will find it easier to mandate and enforce contact tracing, as the public will be more understanding of its role in curbing the threat at hand (Yun, 2020).

Besides pandemic-related factors, there are further societal considerations that will impact the choice of governance approaches. A third consideration is that of national culture and societal values (Graham-Harrison, 2020). It has been shown that societal culture has a range of implications for governance (Hofstede, 1980, 2001; House et al., 2004) including in relation to IT (Leidner & Kayworth, 2006). We focus here on the distinction between individualism and collectivism as the most pertinent dimension for questions of collective action (Hofstede, 2001), specifically on the notion of institutional collectivism (Chhokar et al., 2007; House et al., 2004), which refers to the degree to which societal practices encourage and reward collective action. It stands to reason that populations in countries that are high in institutional collectivism, such as Eastern cultures, notably China, South Korea, or India (Chhokar et al., 2007; House et al., 2004), will be more accepting of mandated government action, if perceived as being in line with the common good.

The fourth consideration pertains to the role of government in a society. That is, whether a society has high or low levels of government involvement. At the two extremes, we see authoritarian governments that restrict individual freedoms and libertarian ones that grant individuals and organisations high levels of freedom and autonomy, yet at the expense of strong government institutions (Nolan, 1971). In libertarian societies, the provision of shared services, such as infrastructure or health care, is often done by corporations (instead of the state). Societies with such “small government” ideologies may refrain from mandated government action for proximity tracing either because such force is unwanted or because governments do not have the de facto or de jure necessary powers.

A fifth consideration is the level of trust in the government: the combination of competence, benevolence and integrity attributed to the government (Hamm et al., 2019). When governments are unable to engender trust of their constituents, they will be unable to govern efectively, with problems of policy compliance and resistance to government programmes typical outcomes (Hamm et al., 2019). Because compliance in this case requires ongoing buyin from users, resistance to proximity tracing adoption is likely to be exacerbated if government mistrust is wide-spread within the population. Hence, the less a society trusts their government the less successful will government-led approaches to proximity tracing expected to be.

The final consideration is trust in technology, the belief that technology will provide helpful solutions to problems (Lankton et al., 2015; McKnight et al., 2011). Diferent populations have diferent levels of trust in technology. We argue that societies with higher levels of trust in technology will find it easier to mobilise users to adopt, and other entities to help drive adoption of, contact tracing solutions.

## 5.2. Contextual considerations in configuring IT governance approaches

Which IT governance approach to digital contact tracing, particular proximity tracing, is the most appropriate for which societal context?

## 5.2.1. Mandated, collectivist approaches

Our analysis suggests that mandated approaches will be most successful in achieving a high user rate for digital/proximity tracing solutions because the adoption is not left up to individual choice, thus alleviating the collective action problem. Population-wide adoption allows for efective digital contact tracing, rapid isolation of cases, curbing of the pandemic, and thus better health and economic outcomes.

However, mandated approaches are only acceptable or even possible under a very narrow range of circumstances. For one, societies must generally accept mandated, government-led measures that sacrifice personal freedoms for the collective good. Collectivist societies (typical of many Asian countries) may then embrace even surveillance tracing (and other strong measures such as military-enforced curfews) as “swift and bold actions”, with the very same actions being seen as “heavy-handed” and “unacceptable” in individualistic societies (typical of Europe and the Americas) based on privacy and personal freedom concerns (Wagner & Rogers, 2020). Even in collectivist societies, the required wide-spread compliance will be achieved only if there is an immediate and heavy risk to public health. First-hand experience with previous pandemic outbreaks (e.g., MERS, SARS) will further support early-stage mandated interventions as the impacts of pandemics have been experienced. Also, the government needs to be trusted to avoid wide or hidden resistance (Edelman, 2019a) and have centralised power (e.g., India, which, overnight and nationwide, mandated the use of its tracing app to all workers, Phartiyal (2020)).

The context of South Korea appears suitable for a mandated approach. South Korea reacted to the COVID-19 with a surveillance tracing approach termed “virtuous surveillance” (M. S. Kim, 2020). The approach uses cell phone location data, credit card transaction data, and CCTV surveillance data to retrace peoples’ whereabouts. When a person tests positive, the government releases publicly on the Internet: “the individual’s last name, sex, age, district of residence and credit-card history, with a minute-tominute record of their comings and goings” (Thompson, 2020). Private-sector apps then map and visualise the movements of these confirmed cases and alert users when they are in the vicinity of a respective location (Kim & Denyer, 2020). This heavily privacyinvasive approach enjoys broad buy-in from the Korean public, attributable to its collectivist orientation and recent pandemic experience with MERS and SARS1 outbreaks (Thompson, 2020).

## 5.2.2. Voluntary, individualist approaches

A mandated approach to digital contact tracing will likely trigger resistance in many circumstances. Individualistic societies, which often display libertarian “small government” ideologies, federated/decentralised government structures, or low levels of trust in government, will likely resist a mandated approach. Here, people are concerned with their individual freedom and their privacy, and are reluctant or actively resisting to be forced to take involuntary actions. Such societies face the collective action problem in aggravated form. The result is that government involvement in tracing may be resisted or even illegal in such societies. Hence, the focus of governing digital contract tracing might shift to other entities. In addition to the individual decision maker, this may involve private sector organisations and IT platform providers. They may encourage, nudge or even locally mandate adoption (e.g., as a condition of entry to ofices or shops).

The context of the USA appears to be one where a voluntary, individualistic, non-government approach is the most viable governance option. The (public sector) Centre for Disease Control (CDC) strongly advocates for states to utilise the (private sector) Apple-Google Exposure Notification API. At the time of writing 20 US states had announced development of respective apps (Dave, 2020b). US population polls suggest that there is significantly more trust in the platform provider than the government, particular in regard to IT governance (Loveboy, 2020b). The US population also has very high levels of trust in technology in general (Edelman, 2019b). In addition, US companies are able to require their employees to use proximity tracing apps when on-premise, while governments in the USA are not allowed to mandate the same (Haskins, 2020). For example, PWC has announced that they consider making the on-premise use of proximity tracing mandatory (Leswing, 2020).

## 5.2.3. Balanced approaches

There are many balanced options between the above extreme cases – mandated adoption and heavy surveillance by the government (such as in South Korea or China) vs. moving pandemic response efectively from government and health authorities to private businesses (such as in the USA) – both of which would be unacceptable for many other societies (such as most European ones). In most societies reservations exist both towards the government making proximity tracing mandatory (Loveboy, 2020a) and towards transitioning too much control from democratically-elected governments to private sector platform providers from overseas (Lazar & Sheel, 2020). Here, individual privacy and rights are valued yet the responsibility for public health is seen to rest with governments and health authorities. Nudged and encouraged approaches coordinated between governments and private sector entities promise to be the most appropriate and most successful in these societies.

The context of Australia lends itself to a balanced and varied approach. The Australian government opted for a centralised proximity tracing solution, COVIDSafe, which is based on the architecture of TraceTogether developed in Singapore. Note that COVIDSafe was developed before the launch of the Apple-Google solution. A range of entities are involved in encouraging Australians to adopt the COVIDSafe app. The Australian federal government promotes this app via messaging, television ads, and public health campaigns. Many private organisations have joined initiatives to publicly endorse and drive proximity tracing, such as Endorse COVIDSafe. As a result, they actively promote and encourage the use of contact tracing apps by customers and employees during the recovery phase. For example, museums encourage patrons to download the app when buying tickets, and organisations advise employees in corporate trainings to have the app activated when in the ofice. Individuals publicly encourage their peers on social media, among them public figures such as Atlassian co-founder Mike Cannon-Brookes (Palmer-Derrien, 2020). This combined approach has yielded promising success, with a reported adoption rate of 33.5% in the group of smartphone users aged 14 and over 40 days after launch. There are suggestions that this equates to more than 40% adoption rate in the two key cities Sydney and Melbourne that have seen the highest COVID-19 infection rates (Slonim, 2020). At the time of writing, Australia had the world-wide highest rate of proximity tracing app adoption (Rivero, 2020).

With the COVID-19 pandemic still in its growth phase at the time of writing, it is too early for any posthoc analysis of approaches to digital contact tracing governance. Yet, our analysis suggests that what is required is a pragmatic, contextualised approach that draws on a set of governance actions from the above IT governance framework and is mindful of the contextual situation of the respective society. A “one size fits all” cross-context approach to (or theory of) IT governance for collective action seems neither possible nor advisable at this point. We suggest that future studies investigate more closely the variety of ways in which countries (and parts of countries) have been combatting COVID-19 with digital contact tracing. We further suggest that our framework will provide the conceptual basis for such research.

## 6. Conclusion

Pandemics such as COVID-19 present large-scale crises that require collective action at the societal level to be contained, including the use of digital technologies. This paper has introduced the topic of digital contact tracing, in particular proximity tracing, as an important, efective and privacy-preserving measure for curbing the spread of pandemic disease outbreaks. The adoption of digital contact tracing, in the form of smartphone apps and services implementing proximity tracing, presents a collective action problem: proximity tracing will only unfold its health, economic and societal benefits when widely adopted and used at the population level, yet in the absence of concrete individual benefits. The paper has identified the governance of this collective action problem as a crucial factor for successful digital contact tracing and proposes a framework for this form of IT governance.

The paper makes four contributions to the IS literature. Firstly, it theoretically frames the populationwide adoption of proximity tracing as a collective action problem. Secondly, it provides a structured conceptualisation of IT governance for collective action at the societal level for subsequent research to build on. This addresses a genuine gap in the IT governance literature, which so far has focused only on the inter-, intra-, and supra-organisational levels, but not on the societal level. Thirdly, it provides a framework outlining the option space of possible IT governance actions for achieving collective action at the societal level. The framework includes as an important governance dimension the decision of which entities are to be involved in IT governance. This presents a novel aspect for the IT governance literature, where the governing entity is generally taken as a priori given (not itself part of the governance design). Finally, we conceptualise the relationship between particular governance approaches and contextual, societal factors in various jurisdictions that will likely impact their selection for concrete responses. While the framework was derived in and for the context of the COVID-19 pandemic, we suggest that it will generalise to other contexts where rapid collective action based on digital technology adoption is required.

The paper also contributes to the immediate problem at hand: how to govern proximity tracing adoption for reaping the desired health, economic, and societal benefits during an unfolding pandemic. For doing so, we suggest governments and health authorities consider following these four steps:

(1) Determine the aim of contact tracing. In the early response to a pandemic, consider mandating adoption for rapid difusion to curb viral spread, “flatten the curve”, and save lives; citizens will likely be open to such an approach. In the later recovery phase, when people will return to workplaces and public spaces, and the aim is to trace and contain outbreaks, the approach must match contextual requirements.

(2) Understand the contextual and cultural factors that shape citizens’ likely reaction to governance actions, and configure governance approaches accordingly (see section 5).

(3) Identify actors that will assist in implementing governance approaches, such as government agencies, private corporations and public institutions, technology platforms and providers, as well as individual citizens more broadly (see section 4.1).

(4) Select, design and roll-out concrete governance actions at all levels (see Table 3) and measure their efectiveness in achieving adoption; adjust where required.

## Notes

1. https://www.tracetogether.gov.sg/

2. https://www.health.gov.au/resources/videos/covid safe-app-how-does-it-work

3. Information via http://www.rki.de/covid-19

4. https://endorsecovidsafe.com/

## Acknowledgments

We would like to thank the Editors of the EJIS Special Communications on IS in the Age of Pandemics for a fast and constructive review process. We also thank the Sydney Business Insights team and members of the Digital Disruption Research Group for their ideas and input to the research, and Alexander Richter, Daniel Reker, and Christoph Müller-Bloch for helpful feedback on earlier drafts of this manuscript.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## ORCID

Kai Riemer http://orcid.org/0000-0002-2348-8315 Rafaele Ciriello http://orcid.org/0000-0002-5073-6310 Sandra Peter http://orcid.org/0000-0002-8431-7368 Daniel Schlagwein http://orcid.org/0000-0002-1591- 4660

## References

Allison, S. T., & Kerr, N. L. (1994). Group correspondence biases and the provision of public goods. Journal of Personality and Social Psychology, 66(4), 688–698. https://doi.org/10.1037/0022-3514.66.4.688

Apple. (2020a). Apple and Google partner on COVID-19 contact tracing technology. Apple Newsroom. https:/ www.apple.com/au/newsroom/2020/04/apple-andgoogle-partner-on-covid-19-contact-tracing-technology/

Apple. (2020b). Privacy-preserving contact tracing. Apple Website. https://www.apple.com/covid19/contacttracing

Asghar, H., Farokhi, F., Kaafar, D., & Rubinstein, B. (2020). On the privacy of tracetogether, the Singaporean CVOID-19 contact tracing mobile app, and recommendations for Australia. The University of Melbourne. https:/ eng.unimelb.edu.au/ingenium/research-stories/worldclass-research/real-world-impact/on-the-privacy-oftracetogether,-the-singaporean-covid-19-contact-tracing -mobile-app,-and-recommendations-for-australia

ASHM. (2016). Australasian contact tracing guidelines. Australasian Society for HIV, Viral Hepatitis and Sexual Health Medicine (ASHM). http://contacttracing.ashm. org.au/contact-tracing-guidance/steps-in-contact-tracing

Axelrod, R., & Hamilton, W. D. (1981). The evolution of cooperation. Science, 211(4489), 1390–1396. https://doi. org/10.1126/science.7466396

Boonstra, A., Eseryel, U. Y., & van Ofenbeek, M. A. G. (2018). Stakeholders’ enactment of competing logics in IT governance: polarization, compromise or synthesis? European Journal of Information Systems, 27(4), 415–433. https://doi.org/10.1057/s41303-017-0055-0

Busvine, D., & Rinke, A. (2020). Germany flips to Apple-Google approach on smartphone contact tracing. Reuters. https://www.reuters.com/article/us-healthcoronavirus-europe-tech/germany-flips-on-smartphonecontact-tracing-backs-apple-and-googleidUSKCN22807J

Cellan-Jones, R. (2020). Contact tracing app ‘working in Ireland’. BBC News. https://www.bbc.com/news/technol ogy-53525712

Cellan-Jones, R., & Kelion, L. (2020). Coronavirus: The great contact-tracing apps mystery. BBC News. https://www. bbc.com/news/technology-53485569

Chen, D. Q., Preston, D. S., & Xia, W. (2010). Antecedents and efects of CIO supply-side and demand-side leadership: A staged maturity model. Journal of Management Information Systems, 27(1), 231–272. https://doi.org/10. 2753/MIS0742-1222270110

Chhokar, J. S., Brodbeck, F. C., & House, R. J. (2007). Culture and leadership across the world: The GLOBE book of in-depth studies of 25 societies. Lawrence Erlbaum.

Consultancy.asia. (2020). Singaporean attitudes to personal COVID data difer to overseas counterparts. https://www.consultancy.asia/news/3126/singaporeanattitudes-to-personal-covid-data-difer-to-overseascounterparts

Criddle, C., & Kelion, L. (2020). Coronavirus contact tracing: World split between two types of app. BBC News. https:// www.bbc.com/news/technology-52355028

Dalzell, S., & Probyn, A. (2020). Convincing Australians to use government-sponsored coronavirus-tracing app a tough ask. ABC. https://www.abc.net.au/news/2020- 04-15/challenge-to-convince-australians-to-use coronavirus-tracing-app/12151130

Dave, P. (2020a). Explainer: How smartphone apps can help ‘contact trace’ the new Coronavirus. Reuters. https://www. reuters.com/article/us-health-coronavirus-tracing-appsexpla/explainer-how-smartphone-apps-can-help-contact -trace-the-new-coronavirus-idUSKCN21W2I8

Dave, P. (2020b). Google says 20 US states, territories ‘exploring’ contact tracing apps. itnews. https://www.itnews.com. au/news/google-says-20-us-states-territories-exploringcontact-tracing-apps-551132

Dawes, R. M. (1980). Social Dilemmas. Annual Review of Psychology, 31, 169–193. https://doi.org/10.1146/ annurev.ps.31.020180.001125

Dawson, G. S., Denford, J. S., Williams, C. K., Preston, D., & Desouza, K. C. (2016). An examination of efective IT governance in the public sector using the legal view of agency theory. Journal of Management Information Systems, 33(4), 1180–1208. https://doi.org/10.1080/ 07421222.2016.1267533

de Reuver, M., Sørensen, C., & Basole, R. C. (2018). The digital platform: A research agenda. Journal of Information Technology, 33(2), 124–135. https://doi.org 10.1057%2Fs41265-016-0033-3

Edelman. (2019a). Trust barometer - global report. https:// www.edelman.com/sites/g/files/aatuss191/files/2019-02/ 2019\_Edelman\_Trust\_Barometer\_Global\_Report\_2.pdf

Edelman. (2019b). Trust barometer - trust in technology. https://www.edelman.com/sites/g/files/aatuss191/files/ 2019-06/2019TrustBarometer\_TrustInTechnology.pdf

Etherington, D. (2020). Apple launches COVID-19 ‘exposure notification express’ with iOS 13.7 — Android to follow later this month. TechCrunch. https://techcrunch.com/ 2020/09/01/apple-launches-system-level-covid-19- exposure-notification-express-with-ios-13-7-google-tofollow-later-this-month/

Fama, E. F., & Jensen, M. C. (1983). Separation of ownership and control. The Journal of Law and Economics, 26(2), 301–325. https://doi.org/10.1086/467037

Farrell, P. (2020). Experts raise concerns about security of coronavirus tracing app COVIDSafe. ABC. https://www. abc.net.au/news/2020-05-14/experts-concerned-aboutcoronavirus-tracing-covidsafe-security/12245122

Fedorowicz, J., Sawyer, S., & Tomasino, A. (2018). Governance configurations for inter-organizational coordination: A study of public safety networks. Journal of Information Technology, 33(4), 326–344. https://doi.org 10.1057/s41265-018-0056-z

Ferretti, L., Wymant, C., Kendall, M., Zhao, L., Nurtay, A., Abeler-Dörner, L., Parker, M., Bonsall, D., & Fraser, C. (2020). Quantifying SARS-COV-2 transmission suggests epidemic control with digital contact tracing. Science, 368 (6491). https://doi.org/10.1126/science.abb6936

Garthwaite, R., & Anderson, I. (2020). Coronavirus: Alarm over ‘Invasive’ Kuwait and Bahrain contact-tracing apps. BBC News. https://www.bbc.com/news/world-middleeast-53052395

Ghazawneh, A., & Henfridsson, O. (2015). A paradigmatic analysis of digital application marketplaces. Journal of Information Technology, 30(3), 198–208. https://doi.org 10.1057/jit.2015.16

Gladstone, N. (2020). COVIDSafe app yet to trace useful number of unique cases despite second wave. The Sydney Morning Herald. https://www.smh.com.au/national/cov idsafe-app-yet-to-trace-useful-number-of-unique-casesdespite-second-wave-20200725-p55fd7.htm

Graham-Harrison, E. (2020). Coronavirus: How Asian countries acted while the west dithered. The Guardian. https:/ www.theguardian.com/world/2020/mar/21/coronavirusasia-acted-west-dithered-hong-kong-taiwan-europe

Grant, G., & Tan, F. B. (2013). Governing IT in inter-organizational relationships: Issues and future research. European Journal of Information Systems, 22 (5), 493–497. https://doi.org/10.1057/ejis.2013.21

Gregory, R. W., Kaganer, E., Henfridsson, O., & Ruch, T. J. (2018). IT consumerization and the transformation of IT governance. MIS Quarterly, 42(4), 1225–1253.

Guillemette, M. G., & Paré, G. (2012). Toward a new theory of the contribution of the IT function in organizations. MIS Quarterly, 36(2), 529–551. https://doi.org/10.2307/ 41703466

Hamm, J. A., Smidt, C., & Mayer, R. C. (2019). Understanding the psychological nature and mechanisms of political trust. PLoS ONE, 14(5), e0215835. https://doi. org/10.1371/journal.pone.0215835

Haskins, C. (2020). Workers around the world are already being monitored by digital contact tracing apps. BuzzFeed News. https://www.buzzfeednews.com/article/carolineha skins1/coronavirus-private-contact-tracing

Hofstede, G. (1980). Culture’s consequences: international diferences in work-related values. Sage.

Hofstede, G. (2001). Culture’s consequences: comparing values, behaviors, institutions, and organizations across nations (2e). Sage.

Horowitz, J., & Satariano, A. (2020). Europe rolls out contact tracing apps, with hope and trepidation. The New York Times. https://www.nytimes.com/2020/06/16/world/eur ope/contact-tracing-apps-europe-coronavirus.html

House, R. J., Hanges, P. J., Javidan, M., Dorfman, P., & Gupta, V. (2004). Culture, leadership, and organizations: The GLOBE study of 62 societies. Sage.

Howell O’Neill, P. (2020a). Apple and Google’s COVIDtracing tech has been released to 23 countries. MIT

Technology Review. https://www.technologyreview.com/ 2020/05/20/1002001/apple-and-googles-covid-tracingtech-has-been-released-to-22-countries/

Howell O’Neill, P. (2020b). Bluetooth contact tracing needs bigger, better data. MIT Technology Review. https://www. technologyreview.com/2020/04/22/1000353/bluetoothcontact-tracing-needs-bigger-better-data

Howell O’Neill, P. (2020c). No, Coronavirus apps don’t need 60% adoption to be efective. MIT Technology Review. https://www.technologyreview.com/2020/06/05/ 1002775/covid-apps-efective-at-less-than-60-percentdownload/

Howell O’Neill, P. (2020d). Norway halts coronavirus app over privacy concerns. MIT Technology Review. https:// www.technologyreview.com/2020/06/15/1003562/nor way-halts-coronavirus-app-over-privacy-concerns/

Huang, R., Zmud, R. W., & Price, L. R. (2010). Influencing the efectiveness of IT governance practices through steering committees and communication policies. European Journal of Information Systems, 19(3), 288–302. https://doi.org/10.1057/ejis.2010.16

Huang, Y., Sun, M., & Sui, Y. (2020). How digital contact tracing slowed COVID-19 in East Asia. Harvard Business Review. https://hbr.org/2020/04/how-digital-contacttracing-slowed-covid-19-in-east-asia

Hufty,M. (2011). Investigating policy processes: the governance analytical framework (GAF). In U. Wiesmann & H. Hurni (Eds.), Research for sustainable development: Foundations, experiences,and perspectives (pp.403–424). Geographica Bernensia.

Kelion, L. (2020a). Apple and Google accelerate Coronavirus contact tracing apps plan/. BBC News. https://www.bbc. com/news/technology-52415593

Kelion, L. (2020b). Coronavirus: France’s virus-tracing app ‘of to a good start’. BBC News. https://www.bbc.com/ news/technology-52905448

Kelion, L. (2020c). Coronavirus: ministers consider NHS contact-tracing app rethink. BBC News. https://www. bbc.com/news/technology-52995881

Kim, M. J., & Denyer, S. (2020). A ‘travel log’ of the times in South Korea: Mapping the movements of coronavirus carriers. The Washington Post. https://www. washingtonpost.com/world/asia\_pacific/coronavirussouth-korea-tracking-apps/2020/03/13/2bed568e-5fac-11ea-ac50-18701e14e06d\_story.htm

Kim, M. S. (2020). Seoul’s radical experiment in digital contact tracing. The New Yorker. https://www.newyorker. com/news/news-desk/seouls-radical-experiment-in digital-contact-tracing

Lacity, M., & Hirschheim, R. (1993). The information systems outsourcing bandwagon. MIT Sloan Management Review, 35(1), 73–86. https://sloanreview.mit.edu/article the-information-systems-outsourcing-bandwagon/

Lankton, N. K., McKnight, D. H., & Tripp, J. (2015). Technology, humanness, and trust: rethinking trust in technology. Journal of the Association for Information Systems, 16(10), Article 1. https://doi.org/10.17705/1jais. 00411

Law, E. (2020). Coronavirus: China’s contact tracing app touted as helping to contain outbreak. The Straits Times. https:// www.straitstimes.com/asia/east-asia/coronavirus-chinascontact-tracing-app-touted-as-helping-to-contain-outbreak

Lazar, S., & Sheel, M. (2020). Contact tracing apps are vital tools in the fight against Coronavirus. But who decides how they work?. The Conversation. https://theconversation.com/con tact-tracing-apps-are-vital-tools-in-the-fight-againstcoronavirus-but-who-decides-how-they-work-138206

Leclercq-Vandelannoitte, A., & Bertin, E. (2018). From Sovereign IT governance to liberal IT governmentality? A foucauldian analogy. European Journal of Information Systems, 27(3), 326–346. https://doi.org/10.1080 0960085X.2018.1473932

Leidner, D. E., & Kayworth, T. (2006). A review of culture in information systems research: Toward a theory of information technology culture conflict. MIS Quarterly, 30(2), 357–399. https://doi.org/10.2307/25148735

Leswing, K. (2020). Companies could require employees to install Coronavirus-tracing apps like this one from Pwc before coming back to work. CNBC. https://www.cnbc. com/2020/05/06/pwc-is-building-coronavirus-contacttracing-software-for-companies.html

Li, J., & Guo, X. (2020). COVID-19 contact-tracing apps: A survey on the global deployment and challenges. arXiv. https://arxiv.org/abs/2005.03599

Lomas, N. (2020). How will Europe’s Coronavirus contacttracing apps work across borders? TechCrunch. https:/ techcrunch.com/2020/05/15/how-will-europescoronavirus-contacts-tracing-apps-work-across-borders/

Loveboy, B. (2020a). EU rejects idea of making contact tracing apps mandatory for travel. 9to5Mac. https://9to5mac. com/2020/05/13/contact-tracing-apps-mandatory/

Loveboy, B. (2020b). Poll: Would you agree to Coronavirus contact tracing if it were done by apple?. 9to5Mac. https:// 9to5mac.com/2020/03/30/contact-tracing-app/

Magnusson, J., Koutsikouri, D., & Päivärinta, T. (2020). Eficiency Creep and Shadow Innovation: Enacting Ambidextrous IT Governance in the Public Sector. European Journal of Information Systems. forthcoming .

Magnusson, J., Koutsikouri, D., & Päivärinta, T. (2020). Eficiency creep and shadow innovation: Enacting ambidextrous IT governance in the public sector. European Journal of Information Systems. https://doi.org/10.1080 0960085X.2020.1740617

McKnight, D. H., Carter, M., Thatcher, B. J., & Clay, P. F. (2011). Trust in a specific technology: An investigation of its components and measures. ACM Transactions on Management Information Systems, 2(2), 12–32. https:// doi.org/10.1145/1985347.1985353

Mindel, V., Mathiassen, L., & Rai, A. (2018). The sustainability of polycentric information commons. MIS Quarterly, 42(2), 607–632. https://doi.org/10.25300 MISQ/2018/14015

Mintzberg, H., & McHugh, A. (1985). Strategy formation in an adhocracy. Administrative Science Quarterly, 30(2), 160–197. https://doi.org/10.2307/2393104

Moldoveanu, M., & Martin, R. (2001). Strategy formation in an adhocracy. University of Toronto. (https://rogerlmar tin.com/docs/default-source/Articles/incentivesgovernance/agencytheory

Morley, J., Cowls, J., Taddeo, M., & Floridi, L. (2020). Ethical guidelines for COVID-19 tracing apps. Nature, 582(7810), 29–31. https://doi.org/10.1038/d41586-020- 01578-0

Mulgan, R. (2000). Accountability: An ever-expanding concept? Public Administration, 78(3), 555–573. https:/ doi.org/10.1111/1467-9299.00218

Newton, C. (2020). Why bluetooth apps are bad at discovering new cases of COVID-19. The Verge. https://www.theverge. com/interface/2020/4/10/21215267/covid-19-contacttracing-apps-bluetooth-coronavirus-flaws-public-health

Nolan, D. (1971). Classifying and analysing politico-economic systems. The Individualist, 1, 5–11.

Olson, M. (1965). The logic of collective action: Public goods and the theory of groups. Harvard University Press.

Ostrom, E. (1990). Governing the commons: The evolution of institutions for collective action. Cambridge University Press.

Palmer-Derrien, S. (2020). ‘Turn the angry-mob mode of’: cannon-brookes calls on divided tech industry to back government’s COVIDSafe app. Smart Company. https:// www.smartcompany.com.au/coronavirus/angry-mobcannon-brookes-covidsafe-app/

Phartiyal, S. (2020). India orders Coronavirus tracing app for all workers. Reuters. https://www.reuters.com/article/ushealth-coronavirus-india-app-idUSKBN22E07K

Provan, K. G., & Kenis, P. (2008). Modes of network governance: Structure, management, and efectiveness. Journal of Public Administration Research and Theory, 18(2), 229–252. https://doi.org/10.1093/jopart/mum015

Rivero, N. (2020). Global contact tracing app downloads lag behind efective levels. Quartz. https://qz.com/1880457/ global-contact-tracing-app-downloads-lag-behindefective-levels/

Roper, W. (2020). Americans split on contact tracing app. Statista. https://www.statista.com/chart/21573/contacttracing-app-adoption/

Scott, D. (2020). What good digital contact tracing might look like. Vox. https://www.vox.com/2020/4/22/ 21231443/coronavirus-contact-tracing-app-states

Slonim, R. (2020). In Some places 40% of us may have downloaded COVIDSafe: here’s why the government should share what it knows. The Conversation. https://theconversation. com/in-some-places-40-of-us-may-have-downloadedcovidsafe-heres-why-the-government-should-share-what-it -knows-138323

Statista. (2020). Mobile operating systems’ market share worldwide from January 2012 to December 2019. Statista. https://www.statista.com/statistics/272698/glo bal-market-share-held-by-mobile-operating-systemssince-2009/

Sun, K., & Viboud, C. (2020). Impact of contact tracing on SARS-COV-2 transmission. The Lancet Infectious Diseases, 20(8), 876–877. https://doi.org/10.1016/S1473- 3099(20)30357-1

Taylor, J. (2020). Coronavirus apps: How Australia’s COVIDSafe compares to other countries’ contact tracing technology. The Guardian. https://www.theguardian. com/australia-news/2020/may/03/coronavirus-apps-how -australias-covidsafe-compares-to-other-countriescontact-tracing-technology

Thaler, R. H., & Sunstein, C. R. (2009). Nudge: Improving decisions about health, wealth, and happiness. Penguin.

Thompson, D. (2020). The technology that could free america from quarantine. The Atlantic. https://www.theatlan tic.com/ideas/archive/2020/04/contact-tracing-couldfree-america-from-its-quarantine-nightmare/609577/

Thöni, C., & Volk, S. (2018). Conditional cooperation: Review and refinement. Economics Letters, 171, 37–40. https://doi.org/10.1016/j.econlet.2018.06.022

Tidy, J. (2020). Coronavirus: Israel enables emergency spy powers. BBC News. https://www.bbc.com/news/technol ogy-51930681

Trang, S., Trenz, M., Weiger, W. H., Tarafdar, M., & Cheung, C. M. K. (2020). One app to trace them all? Examining app specifications for mass acceptance of contact-tracing apps. European Journal of Information Systems, 1–14. https://doi.org/10.1080/0960085X.2020. 1784046

Urbaczewski, A., & Lee, Y. J. (2020). Information technology and the pandemic: A preliminary multinational analysis of the impact of mobile tracking technology on the COVID-19 contagion control. European Journal of

Information Systems, 1–10. https://doi.org/10.1080 0960085X.2020.1802358.

Wagner, D., & Rogers, J. (2020). China’s Coronavirus success shows up poor pandemic preparedness in the rest of the world. South China Morning Post. https://www.scmp.com/com ment/opinion/article/3078848/chinas-coronavirus-successshows-poor-pandemic-preparedness-rest

Wareham, J., Fox, P. B., & Cano Giner, J. L. (2014). Technology ecosystem governance. Organization Science, 25(4), 1195–1215. https://doi.org/10.1287/orsc.2014.0895

Weill, P. (2004). Don’t just lead, govern: how topperforming firms govern IT. MIS Quarterly Executive, 3 (1), 1–17. https://aisel.aisnet.org/misqe/vol3/iss1/3

Weill, P., & Ross, J. W. (2004). IT governance: How top performers manage IT decision rights for superior results. Harvard Business Press.

Weinmann, M., Schneider, C., & Vom Brocke, J. (2016). Digital nudging. Business & Information Systems Engineering, 58(6), 433–436. https://doi.org/10.1007/s12599-016-0453-1

Weitzner, D. J., Abelson, H., Berners-Lee, T., Feigenbaum, J., Hendler, J., & Sussman, G. J. (2008). Information accountability. Communications of the ACM, 51(6), 82–87. https://doi.org/10.1145/1349026. 1349043

Xiao, J., Xie, K., & Hu, Q. (2013). Inter-firm IT governance in power-imbalanced buyer–supplier dyads: exploring how it works and why it lasts. European Journal of Information Systems, 22(5), 512–528. https://doi.org/10. 1057/ejis.2012.40

Yun, M. (2020). How Taiwan is containing Coronavirus – despite diplomatic isolation by China. The Guardian. https://www.theguardian.com/world/ 2020/mar/13/how-taiwan-is-containing-coronavirusdespite-diplomatic-isolation-by-china?CMP=Share\_ iOSApp\_Other

Zastrow, M. (2020). South Korea is reporting intimate details of COVID-19 cases: has it helped? Nature. https://www. nature.com/articles/d41586-020-00740-y
