---
otero_id: 16082
otero_key: "M5U6ARPF"
title: "Alignment in an inter-organisational network: the case of\n                    <i>ARC transistance</i>"
authors: "Bernhard R Katzy; Gordon Sung; Kevin Crowston"
year: "2016"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2016.9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
EMPIRICAL RESEARCH

# Alignment in an inter-organisational network: the case of ARC transistance

Bernhard R. Katzy<sup>1,✠</sup>, Gordon Sung<sup>1</sup> and Kevin Crowston<sup>2</sup>

<sup>1</sup>University BW Munich, Center for Technology and Innovation Management, Munich, Germany; <sup>2</sup>Syracuse University, School of Information Studies, Syracuse, U.S.A.

Correspondence: Kevin Crowston, Syracuse University, School of Information Studies, 348 Hinds Hall, Syracuse, NY 13244–4100, U.S.A. Tel: +1 (315) 443–1676; Fax: +1 (866) 265–7407; E-mail: crowston@syr.edu

## Abstract

We consider the processes of achieving alignment in coordinated inter-organizational networks through a case study of a system development project in ARC Transistance, a network of European automobile clubs that cooperate to provide pan-European service. The theoretical contribution of the paper is, first, an extended strategic alignment model for inter-organizational networks that distinguishes between integration of IS with business strategy and infrastructure, and what we label ‘accordance’ between the strategies and infrastructures of the network and the member firms. Second, we propose that for a network organization, network and member strategies might be complementary as well as tightly coupled. We similarly argue that IS architectures for networks should strive for being ‘business strategy-neutral’ to more easily accommodate the diversity of members. Finally, we discuss how the process of developing a network information system can be a driver towards network alignment, but how the lack of effective governance structures makes alignment harder to achieve.

European Journal of Information Systems advance online publication, 24 May 2016; doi:10.1057/ejis.2016.9

Keywords: IS-business alignment; inter-organizational network; strategic accordance

## Introduction

A long-standing concern of information systems (IS) and business managers alike is the alignment between IS and business strategies as a prerequisite for organizational performance (Kappelman et al, 2014). Increasingly, <sup>fi</sup>rms cooperate as members of inter-organizational networks (Gulati, 1998), sometimes called virtual organizations (Mowshowitz, 1997). IS provide an essential infrastructure for such cooperation (Kumar & van Dissel, 1996), raising the question of how IS-business alignment can be achieved when there is more than one business and strategy. Indeed, in this setting, alignment becomes dif<sup>fi</sup>cult to de<sup>fi</sup>ne, much less to achieve. Can alignment be based on some combination of the individual member <sup>fi</sup>rms’ business and IS strategies? Or should the network of <sup>fi</sup>rms be thought of as having an overarching business and IS strategy that can be aligned? How can alignment at the network level be achieved in parallel with alignment within the various member organizations? To answer these questions, the goals of this paper are to develop a theoretical perspective on the question of IS-business alignment and how it might be achieved in network organizations.

To develop this perspective, the paper presents a case study of the ARC Transistance network organization, an inter-organizational network comprising 38 independent European automobile clubs. (A table of acronyms is given at the end of the article.) We analyse data from a transformative period for the network, a period when cross-border travel increased with European integration. At that time these old, tradition-rich national clubs for the <sup>fi</sup>rst time faced an internationalization challenge to their business strategy. This challenge led them to form an inter-organizational alliance, while still wanting to preserve their national identities and strategies.

While the case potentially offers multiple lessons, we turned to the literature on IS-business alignment because many dif<sup>fi</sup>culties experienced during system development and implementation in the case seemed to stem from a perceived lack of alignment of the new information system to the stated business objectives of the network and of its members. Consideration of the evolution of the system over nearly a decade demonstrates the dif<sup>fi</sup>culties of achieving IS-business alignment in the novel setting of a network organization, answering the call for examination of the process of alignment across time (Chan & Reich, 2007) and with new loci of alignment.

In this context we identify a new type of alignment – the <sup>fi</sup>t between corresponding domains of the network and of the member <sup>fi</sup>rms – that we label ‘accordance’. We show how activities in the network to increase alignment in some domains paradoxically reduced accordance in others. The case demonstrates that careful experimentation with the appropriate degree of alignment – rather than simply increasing alignment – has been important for the participants. The case also illustrates how development of an appropriate service-oriented IT infrastructure can provide both integration for interoperability and <sup>fl</sup>exibility to accommodate diverse partner business strategies, if its rationale is not simple ef<sup>fi</sup>ciency gains through standardization or through imposition of a lead <sup>fi</sup>rm’s strategy on subordinate partners. The case thus offers implications for the appropriate IT architecture to <sup>fi</sup>t the circumstances of a network.

## Theory: IS-business alignment in interorganizational collaborations

We start by brie<sup>fl</sup>y reviewing research on IS-business alignment to identify the main concepts and the gap in the literature that we intend to address. Alignment is considered important because organizations with more consistent technology, structure and strategy have been found to have more success in systems implementation (Velcu, 2010), better return on IS investments (Byrd et al, 2006) and overall better business performance (Pollalis, 2003; Yayla & Hu, 2012). Although parallels can be drawn between business strategy-IS alignment and alignment with other aspects of business performance (e.g., manufacturing or marketing, Ansoff, 1979), IS alignment is seen as particularly important because IS has the potential to drive signi<sup>fi</sup>cant innovations in business strategy (e.g., Davenport, 1993).

The construct of IS-business alignment has been conceptualized in several different ways. Many de<sup>fi</sup>nitions start from the business strategy of the <sup>fi</sup>rm. In an early article, alignment was de<sup>fi</sup>ned as ‘the extent to which business strategies were enabled, supported and stimulated by information strategies’. To assess alignment, the authors examined IS applications to see if they enabled stated business strategies (Broadbent & Weill, 1993).

At a more aggregate level, alignment can be conceptualized as the match between a business strategy and an IS strategy. Following a contingency logic, researchers have developed typologies of business strategies and IS strategies and assessed <sup>fi</sup>t as coherence in the positioning of a <sup>fi</sup>rm in these matched typologies (e.g, Chan et al, 1997; Croteau & Raymond, 2004). Another approach has been to develop the typologies of strategies empirically, for example, assessing the <sup>fi</sup>t between the critical success factors (CSFs) of academic institutions and their IS capabilities by <sup>fi</sup>rst grouping institutions based on their CSFs and then comparing each institution’s IS capabilities to the pro<sup>fi</sup>les of the most successful members of their group (Sabherwal & Kirs, 1994). More directly, in a study of small U.K. businesses, Hussin et al (2002) measured alignment as the match between managers’ reports of business and IT strategy in three areas: quality, product and market.

Other authors have provided more detailed models of alignment. In particular, Henderson & Venkatraman (1999) described alignment between business and IS by considering four domains: strategy and infrastructure for business and for IS (a two-by-two matrix, as shown in Figure 1). Each of these domains is further described, in terms of skill, structure and processes for infrastructure, and scope, governance and competencies for strategy. An advantage of this model is that it includes both external and internal perspectives on IS and business. In their model, Henderson & Venkatraman (1999) suggested that the four domain of the business have to be in alignment for overall performance. They therefore hypothesized necessary connections among the domains: external strategy must fit internal infrastructure for both IT and business, and business must be integrated with IT at both strategic and operational levels. The Henderson and Venkatraman model has been widely used in subsequent research. For example, Avison et al (2004, p. 223) applied a version of this model in a <sup>fi</sup>nancial services <sup>fi</sup>rm and found that it had ‘conceptual and practical value’ for managers. Gerow et al (2014) used this model as the basis for developing measures of these six types of alignment.

The studies surveyed above described aspects of the business and IS, and conceptualized how they might be aligned. Other researchers have suggested studying the process of and appropriate managerial approaches for achieving alignment (e.g., Sledgianowski & Luftman, 2005). For example, Henderson & Venkatraman (1999) described four ‘alignment perspectives’ that suggest how alignment might be achieved. For example, a perspective of ‘strategy execution’ has organizational strategy driving decisions about the organizational and IS infrastructure needed to execute the chosen strategy. Broadbent & Weill (1993) suggested that alignment is built through practices that include planning, development of appropriate organizational structures, executive consensus on <sup>fi</sup>rm strategic-orientation and consideration of information strategy, business management responsibility for informationbased developments, and extensive interaction between IS and business. Teo & King (1997) proposed different levels of integration of business and IS planning, with the highest level being joint planning of both as one.

![](/api/attachments/M5U6ARPF/fulltext/images/6c5827794541e2036ba5a723a1e4cfe449f47c777d270d98c43e639cafeb0895.jpg)  
Functional integration  
Figure 1 The strategic alignment model. Source : Henderson & Venkatraman, 1999.

In these studies, achieving IS alignment can be observed as an outcome of a well-crafted IS-implementation project that takes the business strategy into account and guides implementation accordingly (or even builds both jointly, e.g., Teo & King, 1997). Following this approach, in this paper, we examine the process of system development and implementation with the goal of understanding how alignment was achieved (or not).

IS-implementation projects face different degrees of challenges, and research has identi<sup>fi</sup>ed numerous factors that enhance or impede achievement of alignment during a development project. Teo & King (1997) pointed to the business knowledge of IS executives. Byrd et al (2006) found that <sup>fi</sup>rms with more integrated planning saw better returns on their IS investments. Kearns & Sabherwal (2006) found that business-IS alignment was improved by business managers’ participation in IT planning and IT managers’ participation in business planning, and these in turn were facilitated by top managers’ knowledge of IT.

## The research gap

The general assumption of the existing research is that one governing business strategy exists, a limitation that we seek to address. There have been a few studies that relax this assumption, for example, studies of IS-business alignment in global <sup>fi</sup>rms in which different subsidiaries might have different strategies to <sup>fi</sup>t their local conditions. Under these circumstances, achieving IS alignment is more complex than alignment to the single business strategy of one <sup>fi</sup>rm. For example, Hanseth & Braa (2000) described problems in systems implementation in a conglomerate, where different units pursued different implementation projects. Similarly, IS strategies in transnational companies have been found to differ among companies with different con<sup>fi</sup>gurations (King & Sethi, 1999; King & Sethi, 2001). Hekkala & Urquhart (2013) described how power issues (control of resources, access to decision-making and legitimation) affected project members’ experiences of an inter-organizational system implementation.

However, even work in this area has mostly examined the single global IS strategy and overall corporate structure. For example, Bartlett & Ghoshal’s (1989) models of the structure of global <sup>fi</sup>rms were found to <sup>fi</sup>t a typology of IS structures (Jarvenpaa & Ives, 1993). Kirsch & Haney (2006) developed a model of the process of requirements analysis for common systems that includes both rational knowledge acquisition and political negotiation processes to determine the one integrated set of global requirements and to achieve acceptance of the system from the local stakeholders. An exception is Peppard (1999), who developed a conceptual framework for analysing information management in a global enterprise to highlight the role of IS in supporting business strategies. He drew a distinction between the IS architecture, which might be common, and the ‘suprastructure’ that would support particular individual strategies.

In this paper, we focus in particular on collaborative networks of <sup>fi</sup>rms. Research on networks has observed that IS are a driver towards more inter-organizational collaboration and virtual organizations (Mowshowitz, 1997) and that IS are a necessary infrastructure for such organizations (Kumar & van Dissel, 1996; Andres & Poler, 2015b). However, despite the importance of IT for networks, the network context has received little attention in alignment research. A review article on IT alignment (Chan & Reich, 2007) calls for research on different ‘loci of alignment’ (p. 311) but alignment in an inter-organizational setting is not mentioned. Volkoff et al (1999) examined system development in a network, identifying the need for a sponsoring executive in each <sup>fi</sup>rm. Mandal et al (2003) discuss IS planning for an alliance, but do not include empirical data. Sanders (2005) studied alignment for suppliers in supply chains, but the particular supply chains studied had dominant <sup>fi</sup>rms that could impose a strategy on the others. Gerlach et al (2013) developed a simulation to estimate how decentralization of planning systems decreases revenue for an airline alliance, an example of the impact of lack of alignment in a network setting. The paucity of research on networks is troubling because the issues for networks seem likely to be different and more complex than in a distributed enterprise. For example, <sup>fi</sup>rms in a network might require IS-enabled integration to achieve high performance in their shared business but suffer at the same time from mismatches between the system’s concomitant standardization and their varying business strategies.

The contribution of this paper is to develop for the context of an inter-organizational network, a de<sup>fi</sup>nition of alignment and a description of the process of achieving alignment – that is, the speci<sup>fi</sup>c actions taken to develop a system that <sup>fi</sup>ts a business strategy and vice versa. We do so by carefully describing a particular system implementation to show how and where alignment was achieved or not achieved. As a basis for this analysis, we draw on and extend Henderson and Venkatraman’s (1999) Strategic Alignment Model.

## Research methods

Given our goal of developing a theoretical description of the process of IS-business aligning in a network setting, we followed the theory-building case study approach outlined by Eisenhardt (1989). In the remainder of this section, we describe the case site and our data elicitation and analysis approach.

## Research setting: ARC transistance

Our case is set in the ARC Transistance organization. This organization was chosen because it is a revelatory setting for our research (Yin, 2003): revelatory of the nature and process of system development to achieve IS-business alignment in a network setting. To begin, we recount the history of the ARC Transistance network organization to explain the challenges it faced.

ARC Transistance (since 2009 named ARC Europe) is a collaborative venture of European automobile clubs, led by the largest clubs in eight countries – AA (the United Kingdom), ACI (Italy), ADAC (Germany), ANWB (The Netherlands), ÖAMTC (Austria), RACE (Spain), TCB (Belgium) and TCS (Switzerland) and involving many others as ‘non-shareholder’ partners. These clubs are comparable to the American Automobile Association (AAA)

clubs in the United States. Services include roadside assistance from the <sup>fl</sup>eet of yellow assistance vans, maps from the club printing house, testing of cars, air-rescue services in the event of an accident, a club magazine and a travel agency. The clubs have a long history: indeed, in the Netherlands, the ANWB club has provided roadside assistance since before the invention of the automobile.

The separate <sup>Strategic motivation for the network</sup>national clubs were motivated to collaborate by changing demand, competition and business. First, European inte gration led to growth of cross-border traf<sup>fi</sup>c and travel, leading to increased demand from members for pan-European services. To meet this demand, many of the large national clubs independently operated foreign services – called ‘key points’ – for their members abroad (e.g., a Dutch key point in France to serve Dutch members travelling there on holiday). Increased demand for these services prompted consideration of better ways to deliver them.

Second, the early 1990s brought a radical change in the industry, when motor vehicle manufacturers started offering life-long roadside assistance as a way to maintain customer relationships. Some manufacturers set up their own assistance operations, thus directly competing with the clubs. Other manufactures emerged as business-tobusiness (B2B) customers for roadside assistance services. However, these manufacturers required a single Europeanwide provider, but no individual club had the business scope to offer a truly pan-European service. As well, the B2B nature of the manufacturers’ business did not <sup>fi</sup>t the historic processes and skills developed by the clubs to serve their individual client/members.

In 1991, in response to the demand for <sup>ARC transistance</sup>a European-wide scope of operations, the eight clubs noted above created a new organization, ARC Transistance, to offer roadside assistance services on a pan-European basis, marketing these services in particular to the car industry as a B2B service. ARC Transistance had the responsibility to negotiate the business-to-business (B2B) roadside assistance contracts with the auto manufacturers, while the individual and national contracts remained with the individual clubs. ARC Transistance did not build its own operations infrastructure but instead utilized the network of its clubs for service delivery. As the Chairman explained:

ARC Transistance is not a club itself, ARC Transistance is a coordination body for the clubs.

In other words, the clubs formed a network (or virtual) organization (Camarinha-Matos et al, 2008) with a strategy to provide pan-European roadside assistance. They remained independent and served individual drivers in their own home markets, but cooperated to provide European-wide coverage.

Network members were not homogenous. In some Eastern European countries, clubs were founded only after the fall of the Berlin Wall and resembled franchises of the Western clubs. Since France was a popular destination but did not have a club, a group of clubs created a shared of<sup>fi</sup>ce (called ACTA) to serve club members travelling there. As a result, the clubs’ individual strategies and operational practices differed depending on local circumstances. As the CEO of ARC Transistance noted:

The major shareholder clubs of ARC are generally long established, and successful organisations, and often built their own operation systems, trained their own staff and developed their own operation methods in the way that suits their own market needs.

Further complicating the coordination and management of the ARC Transistance network, no single club in the network was dominant. ARC Transistance was actively involved in the de<sup>fi</sup>nition and monitoring of service-level standards for the auto manufacturers’ contracts, but served as a coordinator rather than head of<sup>fi</sup>ce able to impose on the clubs. As well, managers of ARC and of the clubs in the network had varying visions of the future of ARC. Most managers viewed the network as focused strictly on B2B marketing of European-wide assistance network. However, a few individuals considered ARC as an emerging future holding company for a more integrated business, modelled after AAA in the United States (itself a network of local clubs).

Our examination of the process of developing alignment is based on a case study of one cooperative effort, the creation of a common information system. This system implementation project was led by four clubs (AA, ADAC, ANWB and RACE) along with the ARC and ACTA of<sup>fi</sup>ces, and the interactions among these actors are the object of our study. We focus on this system development project in particular because it recurrently forced the crystallization of the meaning and the process of achieving IS-business alignment in this setting, that is, we view the execution of this project as a concrete embodiment of the process of achieving alignment.

## Data elicitation approaches

Data for the case come from both archival documents and interviews with key players in the case. First, data about the organization were gathered from analysis of business strategy and systems development project reports, including technical speci<sup>fi</sup>cations and assessment reports covering successive IS-implementation project phases. A summary of the documents analysed is given in Table 1.

Second, interviews were carried out between 2001 and 2003 by the two European authors with informants at the clubs involved in the systems development project. The protocol included questions about the history of the collaboration and system development project (as identi<sup>fi</sup>ed from the document review). Questions were left open-ended to allow new concepts and ideas to emerge, rather than attempting to <sup>fi</sup>t the data to a preexisting theory. Given our focus on the dynamics of the systems development process, interviews were carried out only with representatives of the organizations directly involved in the effort. A total of 19 semi-structured interviews were undertaken with employees at the ARC Transistance coordination of<sup>fi</sup>ce and ACTA France, as well as with one board member, one or more operational managers (a total of six) and one or more IS managers (a total of six) from each of the clubs in Great Britain (AA), Germany (ADAC) and the Netherlands (ANWB), as well as one interview with a representative of RACE in Spain (the remaining interviews were with project managers). Interviews were undertaken in English, lasted approximately 60–70 min and were transcribed for analysis.

Table 1 Documentary evidence for the case study

<table><tr><td>Organizational documents</td></tr><tr><td>6 club advertising fliers</td></tr><tr><td>Project documents</td></tr><tr><td>4 strategy documents</td></tr><tr><td>3 project plans</td></tr><tr><td>6 project management/structure reports</td></tr><tr><td>4 business process analysis/specification reports</td></tr><tr><td>2 risk assessment and measurement reports</td></tr><tr><td>5 evaluation reports</td></tr><tr><td>2 min from review meetings</td></tr><tr><td>9 progress reports from the project to funding agencies</td></tr></table>

## Data analysis techniques

To analyse documents, interview transcripts and notes, we applied hermeneutic analysis techniques, supported by the software package Atlas-ti. One author began by examining all interview transcripts and notes to establish the history of the organization and of the systems development process, as recounted in the case below. The interview transcripts and notes were next coded to identify text referring to the management of the relationship between the partner clubs. These segments were then assigned to theoretically meaningful categories derived initially from the literature, for example, previously identi<sup>fi</sup>ed factors that enhance or impede alignment. However, the categories evolved through the course of the data analysis. As we coded each segment, we discussed whether the segment <sup>fi</sup>t an existing code, or required a new code or existing codes to be revised.

As one means to validate our <sup>fi</sup>ndings, intermediate versions of the case description were reviewed by club IS and operational employees, and discussed at an ARC board meeting. These interactions con<sup>fi</sup>rmed the basic validity of our case description and <sup>fi</sup>ndings, and provided additional insights to sharpen our <sup>fi</sup>ndings. Board members found the analysis helpful in understanding the underlying source of the problems that had been encountered in the implementation project, again providing a source of validation for our interpretations.

## Case study: creating a European incident management platform – The ARC IP project

In this section, we present a description of a system development effort undertaken within the ARC network called the ARC IP project. We focus on the development of this particular system as a way to reveal the process of and issues and complications in achieving alignment in an inter-organizational network, in line with our focus on the processes of achieving alignment. The key events in the case are listed in Table 2.

As noted above, the clubs had begun their cooperation in response to a need for globalization. Experiences with ARC B2B contracts and with ACTA created awareness among the chief executive of<sup>fi</sup>cers (CEOs) of the ARC clubs (as stated in a Periodic Project Progress Report) that:

Table 2 Timeline of key events in the development project

<table><tr><td>Date</td><td>Event</td></tr><tr><td>01/12/96</td><td>ARC IP Project launched</td></tr><tr><td>19/02/97</td><td>Software development delayed; project board approves a high risk ‘prototyping approach’</td></tr><tr><td>24/03/97</td><td>Project board reviews final version of prototype with users and agrees on implementation plan with developers</td></tr><tr><td>03/06/97</td><td>Project board endorses decision to suspend implementation and notify ARC Board of Directors of the impact</td></tr><tr><td>25/09/97</td><td>ARC Board of Directors decides to delay work on Phase 2 until after Phase 1 implementation</td></tr><tr><td>18/12/97</td><td>Approval given to start Phase 2 scoping exercise in Q1 98</td></tr><tr><td>24/02/98</td><td>Senior technical representative of the clubs met and identified a strategy for Phase II with three stages: (IIa) Separation of Front and Back office implemented for ACTA (F) only (IIb) The further development of the generic solution (IIc) The implementation of the AA/RACE link</td></tr><tr><td>01/99</td><td>Technical Audit by AA and ADAC led to a technical architecture paper; Phase 2 put on hold until Q4/99</td></tr><tr><td>09/99</td><td>Phase 1 pilot at ACTA (F)</td></tr><tr><td>11/99</td><td>Presentation made at annual network meeting in Amsterdam</td></tr><tr><td></td><td>Clubs invited to register their interest in use</td></tr><tr><td></td><td>Project relaunched as ARC-TIME</td></tr><tr><td>08/00</td><td>Business processes agreement</td></tr><tr><td>02/01</td><td>Completion of system architecture</td></tr><tr><td>04/02</td><td>Pilot of Phase 2 at ADAC</td></tr></table>

Incident management is a pan-European affair and incident management services should be provided to a European citizen according to the highest standards.

The CEOs created a strategic vision for the network: that a telephone operator in a club anywhere in Europe should be able to communicate with a member in the member’s native language, verify the services available and successfully manage incidents in cooperation with local service providers, even those in other countries. To support this vision and emerging network strategy, work began on a common operational information system (a piece of network infrastructure), named the ARC IP system.

The various clubs had all invested in their own IS to support member services and many clubs were investing in international networks to support their international key points. However, these independently developed systems and networks operated in parallel and independently, and so did not allow for interoperability. For instance, all cross-border ACTA service requests had to be printed, faxed and re-entered. The new ARC IP system was intended to eliminate such inef<sup>fi</sup>ciencies. As well, cost savings were expected from creating standards supporting ef<sup>fi</sup>cient information exchange.

## Period 1: 1994–1995 – IS alignment driven by the IS departments and interoperation through standard data interfaces

To develop a set of requirements for the planned new system, conferences between operation managers and developers from all clubs were organized starting in 1994 (consistent with the advice of Reich & Benbasat, 2000). Bene<sup>fi</sup>ts as perceived by the managers of the ARC clubs and the ARC Transistance organization are summarized in Table 3; by managers of large clubs in Table 4; and by

## Table 4 Large club management expectations of system bene<sup>fi</sup>ts

● Interface to home club patrol deployment system

● Support for complex, low volume roadside assistance products

● Piloting of new roadside assistance products

● Foreign traveller support for both home and foreign members

Source: club documentation

## Table 3 management expectation of system bene<sup>fi</sup>ts

● Increase speed to market with rapid introduction of new products, because development can be shared

● Support higher service-level standards across Europe for all club members

● Provide standard management information

● Reduce system costs

● Provide potential revenue for future development via licensing fees

● Provide an ARC-wide system and data communication framework with potential for further innovation

● Provide economies of scale with common development and maintenance

● Create a common system at Lyon with an integrated Back Office, potentially improving operational efficiency

Source: Club documentation

managers of smaller clubs in Table 5. The perceptions were only partially overlapping, re<sup>fl</sup>ecting multiple individual club strategies and suggesting potential future problems for the system development and implementation.

Championing the project was a working group of members of the clubs’ IS departments, which established their own set of priorities, shown in Table 6. For IS, this project was a good opportunity to test the concept of interoperability from a technical perspective and to standardize data interfaces, data de<sup>fi</sup>nitions and business processes.

In contrast to the opinions of the IS representatives, operations managers found the project much more problematic because of the diversity of organizational infrastructures among the clubs. As noted above, the clubs determined service levels suitable for their own national members and these differed considerably between countries. These variations were driven by differences in expected service levels, different cultural backgrounds, national or even regional languages and individual operation systems. For example, one assistance centre manager noted:

If there is a customer whose money was stolen during the weekend in Spain, they can call us, and we will send our taxi or towing car to the hotel and give him/ her some money, but this is impossible in Germany, where the customer has to go to a bank.

The different services offered required diverse skills, processes and resources that were not always available or even known by all clubs. The supporting club infrastructures <sup>fi</sup>t each club’s particular business strategy, but did not easily lend themselves to integration with a single IS infrastructure. This is not to say that the operations people disagreed on the need for an encompassing IS infrastructure, but they wanted it only if it followed operational priorities (as in Burn & Szeto, 2000). These differences illustrate the initial differences among clubs in the four domains of Henderson & Venkatraman (1999) strategic alignment model and potential problems achieving alignment.

## Table 5 Smaller club management expectation of ARC IP system bene<sup>fi</sup>ts

● Off-the-shelf package system supporting both domestic and foreign business

● Low level of local IS support required

● Ability to implement Front and Back office independently

Source: Club documentation

Despite these reservations, system development commenced. A core project team was created consisting of the most experienced members of the IS departments from three large clubs, AA, ADAC and ANWB. The approach for the project was adopted from recommended best practices in enterprise integration (e.g., requirements elicitation, data modelling, process modelling). The initial development was a common data standard to allow different clubs’ systems to communicate with each other at the system level. As the project manager described it:

[W]e wanted to actually capture common data, data structures and coding structures in order to facilitate the transfer of data across the virtual network.

However, the data standard de<sup>fi</sup>nition project quickly ran into dif<sup>fi</sup>culties. It was almost impossible to de<sup>fi</sup>ne standard terms for the service packages offered by the different clubs, each tailored to a national market. In attempting to determine the European-wide B2B service offering, club managers were guided by their own business strategies, customers and contexts, leading to signi<sup>fi</sup>cant differences among the visions and perceptions of the various club managers. An assistance centre manager involved in the project noted:

This [diversity] makes the service decision-making process rather dif<sup>fi</sup>cult if it were to be handled by other clubs. We have to work a lot on the different services levels. I think ARC can do a lot in coordinating this.

Alignment to a single system seemed dif<sup>fi</sup>cult at this point and there was no central authority to dictate a common standard. Nevertheless, this phase of the project did have several bene<sup>fi</sup>cial outcomes. A data model was eventually de<sup>fi</sup>ned that could support data interchange among the different clubs, and, more importantly, a practice of regular communication among functional managers of all clubs was started that continued through the years.

## Period 2: 1996 – IS alignment driven by business operations departments: ARC business process reengineering

At the end of 1995, the project team decided on the need to harmonize not only data but also operations by de<sup>fi</sup>ning a common business process model for breakdown assistance services, consistent with the focus on business process re-engineering in the 1990s. In other words, to align IS and business across the network, attempts were

## Table 6 Club IS service management expectations of ARC IP system bene<sup>fi</sup>ts

● Common and easy-to-use system to shorten training

● Real-time entitlement checking to reduce fraudulent usage and service abuse now made to <sup>fi</sup>rst harmonize the businesses of the various member clubs. Again, this was a rather complex process, as the project manager described it:

Within the project team we developed a business process model. We probably have more than twenty versions. It was not anywhere near perfect and we did have a lot of problems with compromising the business process, because there is no such thing as the one and only business process. So, we actually did compromise quite a lot.

Once drafted, the project team sought to promote the business process model to all clubs involved. A regular conference of IS managers from all clubs seemed the appropriate occasion, as described by the project manager:

We promoted this business process model and went through it with some details, and we asked everybody to brainstorm and write down their business processes to see whether it <sup>fi</sup>ts well. The results of it were a few minor changes only.

By the end of the year, the project team had agreed on an ARC-wide business process model for roadside assistance services across Europe, dividing the process into a customer-facing Front Of<sup>fi</sup>ce and a service-providing Back Of<sup>fi</sup>ce. All information exchange between the Front and Back Of<sup>fi</sup>ce of clubs would be realized via automatic electronic transfer, rather than by fax or telephone. The Front Of<sup>fi</sup>ce of any club would eventually be able to automatically dispatch services from the Back Of<sup>fi</sup>ce of any other club in order to provide pan-European services.

While conceptually simple, this model represented a radical change of operations strategy for some clubs. With their current systems, the operators placed orders directly with <sup>fi</sup>eld personnel, for example, communicating directly with garages for towing when needed. Reliance on these direct links made it dif<sup>fi</sup>cult to integrate the different clubs’ operations. Still the achievements made at that point were generally accepted by all ARC clubs and stakeholders, which the project team took as legitimation to move on with implementation.

## Period 3: 1997–2000 – IS alignment driven by system development

In 1997, a project was formed among the clubs and a software development company to implement the new common system, initially to support international incident management among the three large clubs, AA, ADAC and ANWB, and those smaller clubs heavily involved in incident management for holiday traf<sup>fi</sup>c, for example, the Spanish club RACE and ACTA France. As in ARC as a whole, no club had a dominant role in the project – instead, the project structure was a network with reciprocal dependencies among members. Indeed, as the project was co-funded as a collaborative innovation project by the European Union (EU), the software developer was a partner of the clubs rather than a contractor to them. Club executives made it clear that the system could only be costjusti<sup>fi</sup>ed with the additional funding from the EU because the bene<sup>fi</sup>t of the network in general and the system in particular were not clear enough for the clubs to go forward on their own, further indicating the mismatch between the visions of the various clubs and the evolving network structure.

A pilot implementation was planned for validation of requirements and speci<sup>fi</sup>cations; results and experiences from the pilot were intended to guide a European-wide rollout. The joint ACTA of<sup>fi</sup>ce in Lyon, France was chosen as the most suitable pilot site for two reasons. First, key points for four of the major ARC clubs were already present there. Second, support from ACTA France seemed guaranteed because the projected growing market in France demonstrated a clear business need for the system. The intent was that ACTA France would become the pilot model of a pan-European assistance organization with redesigned business processes and supported by a speci<sup>fi</sup>c IS solution.

The system development project followed a waterfall model of software development, as different clubs and the developer took on requirements analysis, coding and acceptance testing, an organization that re<sup>fl</sup>ected the network structure of the project. In February 1997, warnings were received that software development would be delayed as a result of extended negotiations between the developer and ACTA, and the clubs regarding the functionality to be implemented. At a meeting in May 1997, the project board decided to return the software to the contractor for further development, system integration testing and incorporation of change requests arising from user testing at ACTA in Lyon. A new schedule was set to coincide with the move of ACTA to a new building in Lyon during November 1997. However, this target was also missed, as the required functionality was not completed, a situation the contractor blamed on late delivery of stable requirements. We see the problem of achieving a stable set of requirements as a symptomatic of the deeper issues involved in achieving alignment.

Early in 1998, three major priorities were identi<sup>fi</sup>ed for the system development: <sup>fi</sup>rst the separation of Front and Back Of<sup>fi</sup>ce to be implemented for ACTA only; second, focus on serving the clubs AA and ADAC in Lyon but with a more complete solution with additional supported services; and third, the implementation of a link between the systems of AA and RACE. In other words, in order to complete the pilot, implementation was increasingly focused on the prototype and tailored to the needs to the particular implementation site and its interface with individual clubs.

It was not until September 1999 that the Phase I prototype of the ARC IP system, now based on the common data standards, was implemented for ACTA in Lyon. Implementation and rollout were considered a success; the system had been running smoothly in ACTA since the implementation at least until the time of the interviews. However, scepticism remained throughout the ARC network. Typical reproaches were that the system was a B2B system entirely tailored for the use of ACTA, that the requirements for interoperability were not met and that the Front and Back Of<sup>fi</sup>ce were still not separated. In short, the system was apparently only usable by ACTA, as one club manager bluntly put it:

The project and the system development have been hijacked by ACTA Lyon.

In other words, increased IS-business alignment in this context contributed to the success of the system for the speci<sup>fi</sup>c business strategy of ACTA, but at the expense of alignment with other clubs of the network.

## Period 4: 2000 – Re-aligning network and club operations and IS

With the pilot completed with uncertain results, work was undertaken to identify a workable strategy for a Europeanwide system. The leadership of the project was moved from those representing the B2B business to one of the large member clubs, ADAC. The new lead concluded that the aim of the project should be changed from an integrated monolithic system to a modular system using service-oriented architecture (SOA) that could freely be assembled, an approach similar in retrospect to the layered model proposed by Peppard (1999). In other words, project managers no longer sought to achieve alignment between diverse business needs. They instead focused on identifying basic commonalities so that the system would provide an infrastructure for cooperation while minimizing constraints and norms for any particular way of doing business.

To signal the re-launch of the project, it was of<sup>fi</sup>cially reassigned to the leadership of the ARC Transistance CEO and re-named ARC TIME – Tailored Incident Management Europe. Project leaders increased their efforts to involve users with a set of 3-day workshops between November 1999 and January 2000, with the aim to capture the requirements from as many users as possible and to validate feasibility directly with technical people. However, attendance at the workshops varied from time to time, which slowed down the process of capturing the entire business process. Comments from workshop participants describe the problems:

It is dif<sup>fi</sup>cult to get different people from different clubs in order to try to obtain a generic solution, there was lack of consistency.

The workshops did help for the users, but the problem is still the same, things were starting very well, everyone was attending the workshops, but at the end we were only left with a few clubs which were directly in charge of the system development.

Again, a key theme is the problems posed for achieving alignment by the diversity of business strategies and user needs. A particular discrepancy in strategy was that about this time the British club, AA, was purchased by a for-pro<sup>fi</sup>t company, while the continental clubs remained nonpro<sup>fi</sup>t member organizations.

Since the development of the TIME system, ADAC showed strong interest in using it as its own system and therefore agreed to contribute resources (system developers, project managers and <sup>fi</sup>nancial support). Moreover, ADAC took the lead in the development of the rollout. The ADAC managing director described their role:

For ADAC, the <sup>fi</sup>rst phase is the B2B business, which is to integrate other clubs into our organisation in order to provide the service. So we have to <sup>fi</sup>nd a way to make entitlement checking within our own system and give the order to other clubs. The next step is that other clubs are able to see a service order online in our system, reply to it, then take over the order, and <sup>fi</sup>nally give information back when the breakdownservice car reaches the garage. In that way we try to bring ARC TIME Phase III to the B2B area, and in future maybe to medical assistance and only then to the membership services.

However, at this point in the case, and apart from the pilot implementation between the clubs RACE and AA, only the clubs ADAC and ACTA France con<sup>fi</sup>rmed their participation in the development, with other clubs taking a ‘wait-and-see’ attitude, as the senior users from various clubs reported:

We will push this activity in ADAC, and we will replace our stations abroad with the new system, then the site in Munich.

To get further investment, we need a quite sound business case, so from our perspective unless it shows signi<sup>fi</sup>cant improvement on time for processes and quality there is no clear reason for us to invest, because we are quite happy with our existing systems. … So we need to wait and see what it is going to be delivered, and look if there is any signi<sup>fi</sup>cant improvement to justify a business case.

We have to see who is going to use the system, and where they are going to implement the system, then we will decide whether it is making sense for us to participate.

In other words, the process of network aligning continued between a diverse set of business strategies and the desire for a shared network strategy enabled by a common IS. We fade out from the further evolution of the case at this point, but indeed, in the end, ADAC may also come to be seen as ‘hijacking’ the project.

## Discussion

Our <sup>fi</sup>rst contribution is to clarify the concept of ISbusiness alignment in the context of an inter-organizational network lacking a dominant partner. In the case, the club CEOs articulated a strategic vision for a network of pan-European service, delivered through the collaboration of the clubs using their existing operational infrastructures supported by network shared IS, such as the systems discussed in the case above. This vision is an initial statement of a network strategy (at least a business strategy) and network infrastructure. Recall that Henderson & Venkatraman (1999) de<sup>fi</sup>ned strategic alignment in terms of <sup>fi</sup>t between strategies and infrastructure, and integration between IS and business. Achieving <sup>fi</sup>t and integration among these domains is certainly important for the performance of the network as a whole and presumably for each individual club. However, these connections do not fully capture the alignment needed for the network as described in the case.

![](/api/attachments/M5U6ARPF/fulltext/images/efe38d1821b97eb53d25f388bba9171cca8c037b5ea23ee1a86f75226ccfcdf8.jpg)  
Figure 2 The inter-organizational network strategic alignment model. Lines between the network and the clubs represent ‘accor dance’ between the corresponding domains of the SAM.

To address this gap, we conceptualize a third connection among these domains and de<sup>fi</sup>ne network alignment as the ‘accordance’ of each of the network strategies and infrastructures (the four domain of the SAM) with the corresponding domains of the individual members’ strategies and infrastructures. Figure 2 shows our proposed model, including the forms of alignment (<sup>fi</sup>t and integration) proposed by Henderson & Venkatraman (1999) for the network as a whole and for each member club, and adding accordance between the different network members and the network (the curved vertical connections in the <sup>fi</sup>gure).

As in the original model, which posited six separate aspects of alignment (<sup>fi</sup>t, integration, automation and linkage) that must be measured separately (Gerow et al, 2014), network alignment in this model is multi-dimensional, comprising the accordance between the network and each of its members on the four domains of the model (i.e., four factors). Speci<sup>fi</sup>cally, network alignment depends on an accordance or lack of accordance between the network business and information strategies, and the corresponding strategies of the various members (described in terms of scope, governance and competencies in Henderson & Venkatraman (1999)’s model).

A similar logic applies to accordance of the network and individual infrastructures: Henderson & Venkatraman (1999) describe infrastructure in terms of skill, structure and processes, and again, network alignment implies the need for an accordance between these elements for the network and its members.

Henderson & Venkatraman (1999) argued that ‘the <sup>fi</sup>t between external positioning and internal arrangements has been argued to be critical for maximizing economic performance’ (p. 474). A similar logic can be applied to network alignment and the accordance between the network and members. As an example, in the case, the network was planned to draw on the processes and skills of the individual clubs to deliver services (i.e., accordance in the domain of operational infrastructure and processes). However, differences in processes and skills among the member clubs made accordance hard to achieve in this domain, posing a barrier to network alignment and the performance of the network.

Assessing network alignment between the network and the individual members implies that as the strategies and infrastructures of the members converge, network alignment increases. Were full network alignment to be achieved, the organizational boundaries in this framework would disappear. Indeed, the model could be used to describe transitional periods of alignment, such as in post-merger integration situations (e.g., Wijnhoven et al, 2006). During integration, formerly independent – and unaligned – <sup>fi</sup>rms increase mutual accordance in each of the domains until ultimately full alignment is achieved. In the ARC case though, full integration was the goal of only a few participants. Each club had committed to the overall European network, as seen in the creation of ARC Transistance, but continued to pursue its own individual national strategy as well. These individual strategies were supported by distinct IS for the different levels (member clubs vs network). As a result, clubs differed in their adoption of the shared IS. As one club IT manager stated:

We are interested in adopting the data standard, and the backbone infrastructure, but we don’t know yet whether we are going to use the software package or not, because we have our own software system to support our own operation.

The lower part of Figure 2 therefore shows multiple adjacent <sup>fi</sup>gures, as each club maintains its own strategies and infrastructures.

While such a situation might seem to be problematic, based on the evidence from the case – and in contrast to the case of alignment within a single company – we suggest that participation in a network does not require that members have or should attempt to achieve full alignment or to implement all systems in a standard way. Instead, we argue that performance can be achieved when network and individual strategies and infrastructure are complementary, as well as when they are in tight accordance (cf. Andres & Poler, 2015a). As an example, in the case, the strategic scope of the ARC network and the individual clubs were intended to be complementary (i.e., the network strategy was complementary with the club business strategies). The scope of the network strategy was B2B contracts delivered using the services of the national clubs. The network thus did not compete with the member clubs for the individual assistance business (recall that clubs were created originally to serve individual drivers; B2B business was a new development). In other words, the network strategy does not necessarily subsume or replace the individual member strategies, but may co-exist with them, leading to different degrees of accordance and so network alignment. Network alignment can deliberately remain partial, providing space for diversity and separate governance within the constraints implied by complementarity.

Member and network IS infrastructures might also be tightly in accordance or only partially. For example, the network might impose a common IS architecture, such as a single system intended for use by all partners (as seems to be implied in the literature on global <sup>fi</sup>rms reviewed above). Certainly, some level of standardization is needed to allow the members to communicate and work with each other. However, in the case, it proved dif<sup>fi</sup>cult to serve multiple business strategies and a network strategy with an integrated monolithic software package. In other words, attempting to achieve accordance on the IS architecture was hampered by a perceived lack of <sup>fi</sup>t at the club level between the proposed architecture and the club business strategies.

The later version of the TIME platform, developed using a SOA, offered improved modularity to address this issue. Basic services such as entitlement checking or dispatching assistance services were wrapped into modules of agreed quality for use network-wide. A distinct middleware layer provides a mechanism through which each Front Of<sup>fi</sup>ce could potentially communicate with each Back Of<sup>fi</sup>ce in a standardised way while maintaining its own unique characteristics, contract conditions, language and so forth. This IS architecture, similar in retrospect to the infrastructure/ superstructure framework developed by Peppard (1999), <sup>fi</sup>t the newly introduced Back/Front of<sup>fi</sup>ce operational architecture and so improved I/S-business alignment at the network level (Leymann et al, 2002).

The evolution of the ARC TIME project can be seen as an experimental search for the most appropriate assignment of functions to the middleware layer vs business services (i.e., determining the respective scopes of the network and member IS architectures), and development of interfaces between these. The result is not a simple lack of standardization, but a careful balance between standardized middleware infrastructure and deliberate service diversity. This approach to inter-organizational infrastructure thus bridges tensions between variety and standard enforcement in the ARC network, thus enabling a suitable level of accordance.

The systems that emerged were largely neutral to the strategies of the clubs involved in the network, that is, they did not interfere with the clubs’ individual business strategies. Developing IS in an individual-strategy-neutral way proved particularly bene<sup>fi</sup>cial in the case for maintaining the agility of the network under the conditions of dynamic change (offering a counterpoint to the <sup>fi</sup>ndings of Chung et al (2003) and Tiwana & Konsynski (2010) regarding the importance of infrastructure <sup>fl</sup>exibility and IT agility for strategic alignment). Recall that failures in the early phase of the ARC IP project were attributed to dif<sup>fi</sup>culties in accommodating constant requirements changes. Purely technical speci<sup>fi</sup>cations of the interfaces in the initial periods of the project were not successful, because their context remained operations- and strategy-speci<sup>fi</sup>c. In later periods, the project bene<sup>fi</sup>ted from <sup>fi</sup>tting the emerging network business strategy to the network IS strategy. The SOA structure especially enabled progress with interoperability of the ARC-TIME system without having to wait for achievements in business accordance across the ARC network. In fact, such decoupling of progress in technical implementation from progress in network alignment helped build the network organization, as it avoided disturbing the day-to-day practices of the member clubs.

In summary, experience in this case suggests that IT architectures for networked organizations can be placed along a continuum of degree of tight integration to the business to loose integration of commodity modules. This continuum may be extended to what might be called ‘strategy-free systems’ designed to support many diverse organizations without change. Simple examples include common of<sup>fi</sup>ce applications that are used unchanged in many organizations quite independent of the adopted business strategy. The case suggests that even complex enterprise-level systems might be designed to be used with little tailoring to the speci<sup>fi</sup>c business strategies and infrastructures. Indeed, the range of such applications seems to be increasing with the rise of cloud computing, in which identical applications, even complex ones, are provided to diverse organizations. The attraction of such cloud systems is such that many organizations now face problems accommodating so-called shadow applications, as employees turn to outside providers such as Google or Facebook for applications such as email or document sharing, without the support and outside the control of their IS departments.

## Achieving network alignment through an IS development project

Our second contribution concerns the process of achieving network alignment. As in Henderson & Venkatraman’s (1999) analysis, progress towards alignment might start from any domain in the model. For example, a top-down imposition of a network business strategy might drive decisions about individual members’ operational and I/S infrastructures (what they labelled strategy execution) leading to convergence, as might happen in the case of a merger, for example. However, Ciborra argued that a top-down approach to infrastructure planning works only when the technology can be planned and controlled in all of its features (Ciborra, 2000, p. 35). When, as in a network, control of resources is diffuse and no single actor has the legitimation to impose a solution, collaboration will require greater levels of negotiation, compromise, sharing of resources – all elements seen in the case. In Ciborra’s case studies, attempts at topdown control mostly failed, resulting in an evolution to ‘management by deals’, very much like the approach in our case.

In the case, alignment (such as it was) developed bottom-up, as alignment issues crystalized in the process of developing network-level systems intended to provide integration across the network members. The apparent lack of attention to IS strategy in the case may be one symptom of this approach. Shared system development projects, such as the ARC IP and ARC-TIME systems, can be seen as a crystallization kernel for network alignment, providing a shared history that is a basis for building shared beliefs over time, thus supporting closer alignment of strategies (accordance or complementarity). Clearly, the external competitive pressure that led to the foundation of the ARC network is such a shared history, but equally so is the shared experience of lengthy discussions and resulting de<sup>fi</sup>nition of an IS. This approach mirrors Reich & Benbasat’s (2000) suggestions about the need for communication between business and IS executives, but extends it to executives across the member organizations, who may lack opportunities for such interaction.

Furthermore, in the course of the project, a new ARC network IS infrastructure was created, as one interviewee noted:

The bene<sup>fi</sup>t of phase 1 was a proof of concept that the complete separation of Front Of<sup>fi</sup>ce and Back Of<sup>fi</sup>ce does work, leading to a new virtual organisation. [Q: Was that achieved?] Yes, for all clubs it is possible to connect through the interfaces to the Back Of<sup>fi</sup>ce at Lyon.

The various system (and network) building efforts undertaken during the ARC IP project can be positioned in the four domains of the model, as shown in Figure 3. Interoperability and network alignment was the aim of the workshops in the ARC IP project. Work on the common data dictionary and interchange standards contributed to ability to connect across the IS infrastructures of the clubs; development of a shared architecture contributed to accordance of the operations strategy; and common business process models addressed accordance of the organizational infrastructure and processes. For example, the ability to link the various clubs’ operations required a previously lacking separation of the business processes into Front and Back Of<sup>fi</sup>ce (customer-facing vs service-provider-facing). This structuring of operations and IS systems into Front and Back Of<sup>fi</sup>ce became generally accepted in the course of system development, and so emerged as a network standard for the clubs’ operational infrastructure. And the network IS strategy evolved, describing which functions are included in the network IS infrastructure and which are left to the national clubs and speci<sup>fi</sup>c businesses, as described above. Instead of working towards unconditional accordance in all domains for all clubs, development focused on limited services (such as entitlement checking) and shared technical functionalities (such as the data dictionary) to be provided throughout the network, providing complementarity of IS infrastructure and processes.

However, it should be noted that the use of a systems development project as a way to achieve network alignment poses risks to both development and alignment. In the case, while the structures were prepared technically, not all clubs adopted them. The model is helpful in understanding why the system was not successful as a driver for improved network alignment among the clubs in the network. We recall that the pilot system was implemented successfully in ACTA France, as reported by one club executive:

I think the interoperability has become a success in Lyon, and that is a good example to show that we have to go in that direction.

However, as noted above, many club managers perceived the delivered pilot system as overly tailored for the strategy of ACTA and therefore less suitable for their own club.

Research on change management (Senge, 1990) argues that successful pilot cases will increase the chance of adoption, but the opposite was the case here, where the successful pilot system was rejected by the other clubs as having been ‘hijacked’. Our model suggests that this outcome can be explained by the fact that as the developers struggled to <sup>fi</sup>nish the pilot system, its scope was narrowed to handle B2B contracts only and then only those at ACTA France. As a result, the pilot system <sup>fi</sup>t the particular business strategy of ACTA, which increased the perceived gap between the system and the strategies of the other clubs, thus reducing network alignment overall. In other words, the independence of the multiple con<sup>fi</sup>gurations of the club IS-business alignment was not suf<sup>fi</sup>ciently honoured by the pilot network infrastructure.

![](/api/attachments/M5U6ARPF/fulltext/images/e72b437e652121cf74c2d610bb8a009ac3330a70723d9804225515f74be72192.jpg)  
Figure 3 Stages of the case positioned in the network strategic alignment model. Arrows represent drivers of changes in the corre sponding domains during the phases of the project. Dashed lines depict a resulting lack of accordance.

On the basis of our analysis, we suggest that the poor outcome of the pilot project was not caused simply by poor speci<sup>fi</sup>cation of data models and processes or bad implementation practices (e.g., application of the waterfall development model). Indeed, most technical speci<sup>fi</sup>cations were re-used in later phases of systems development, suggesting their essential soundness. Rather, the system as implemented did not meet the con<sup>fl</sup>icting demands posed by the diverse individual clubs’ business processes and their <sup>fi</sup>t to the diverse business strategies.

Managers who were interviewed offered two con<sup>fl</sup>icting explanations for this problem. Some attributed project failure to technical features of the system, which they perceived as insuf<sup>fi</sup>ciently modularized and so incapable of being tailored as needed. Others suggested that interoperability and good functionality had actually been achieved, but the system was in need of more implementation support in the other clubs. Nevertheless, from both groups there are clear indications of the impact on project implementation of the diffuse governance in the network, as reported by a project manager for ARC-TIME:

We started with very disjoint tasks: ANWB did analysis, ADAC built, and AA did test and implementation. Everything was done very isolated. We introduced quality review, but the success of that was limited. We also introduced change management due to creeping functionalities but we still have these problems […]. We introduced stage managers who are responsible for the stage of the project. The idea was, to pull the whole thing together, but there is still a problem, […] they don’t have real authorities within their club. When you don’t have the lead of the project, there is no ultimate authority over other organizations.

These dif<sup>fi</sup>culties re<sup>fl</sup>ect the dif<sup>fi</sup>cult nature of project governance in a network without a central authority.

In the <sup>fi</sup>nal period of the project, a single club, ADAC, continued the systems development project. ADAC has its own resources (being one of the largest clubs) and has not promised that the system will be of use to others. It therefore negotiated with the other clubs to get access to their resources. In the <sup>fi</sup>nal phase, ADAC centralized project governance, combining three forms of power: formal authority, from their role in the project; control of critical resources; and discursive legitimacy through the various teams in the project (Phillips et al, 2000; Hekkala & Urquhart, 2013). It may be that the ADAC managers were more used to working in this fashion, as ADAC is itself a network of regional German clubs. While this approach increases the chance of <sup>fi</sup>nishing development of the technology development project, it is again at the possible cost of lack of accordance with other members of the network, again potentially positioning this system at the member level rather than network infrastructure.

The process of network alignment thus poses somewhat of a paradox: effective governance structures seem to be needed to keep a distributed project on track even if the intended outcome of the project is to support decentralization and diversity rather than convergence of strategies and infrastructures. The lack of these structures in a network of peers thus seems to pose a challenge to using IS to develop the network. And alternately, centralizing governance in one partner may work counter to achieving network alignment.

Our case thus suggests that the degree to which the information system matches the current state of interorganizational structural relationships determines the chance of success of a network-building IS project. The more the IS project is used as an instrument of change and network aligning (e.g., transporting managerial visions about future network strategies), the more network-building effort the project has to bear and so the greater the risk of misalignment should those efforts not pan out.

## Conclusions

This paper has presented a case study of the process of achieving IS-business alignment during the development of a common information system to support a networked organization comprising members with partially shared and partially diverging business interests. The case provides the basis for both a de<sup>fi</sup>nition of IS-business alignment in this context, as well as a theory of network alignment, a process that not only impacts success of ISimplementation projects in network settings, but in which IS plays a driving role for the evolution of the organization.

We conclude that attention should be paid to the network alignment process, a perspective that complements the mainstream of network organization research that has been largely motivated by the agility and speed with which transactions and projects can be undertaken. One caution for management teams is that network management can be long-term effort. Sustaining network-aligning efforts over the long-term requires measurement methods to make achieved intermediate results visible. Further, the case suggests the importance of regular communications between partners to build trust and to <sup>fi</sup>nd commonalities that can be a basis for network alignment (cf. Reich & Benbasat, 2000), which may be dif<sup>fi</sup>cult to arrange in a distributed setting such as a network.

Second, the conclusion of the study for the domain of ISbusiness alignment is that, for networked organizations, a simple match between one business strategy and one IS infrastructure is not suf<sup>fi</sup>cient. Nor does the general belief – that the more alignment among business strategy and processes, IS strategy and systems, the better – seem to hold completely for network organizations. Rather, more sophisticated theories are required to explain the co-existence of multiple businesses, multiple strategies and multiple operations, linked by an appropriate common network infrastructure. The paper contributes a model that distinguishes these multiple concurrent loci of alignment (adding accordance between network and members to the <sup>fi</sup>t and integration identi<sup>fi</sup>ed by Henderson & Venkatraman (1999)). However, more work is needed to develop more precise measures of accordance and complementarity, similar to the work done by Gerow et al (2014) for the relationships of the original Strategic Alignment Model. Further research might test the proposition that either accordance or complementarity network alignment can be associated with high performance.

As well, the case did not examine the level of strategic alignment achieved within each member club. Future research might examine to what extent intra-organizational alignment is a precondition for network alignment. Because the level of network alignment can be less than complete, it seems possible that a network could achieve a suitable level of alignment even if some of the members do not themselves achieve intra-organizational alignment, but more data is needed on how such situations play out.

Finally, the paper proposes design recommendations for IS architectures for collaborative networks. In the case, a system neutral to business strategy enabled broader adoption and so better performance by concurrently supporting multiple business strategies. The practical contributions of this insight for IS departments facing such diversity is that they should consider embracing open standard IS, changing the department’s role to one of a service orchestrator. Future research in this direction is recommended, as an extrapolation of the IS-architecture characteristics in the case might help understand next-generation IS, such as cloud computing and software as a service, that provide broad availability of strategy-neutral information infrastructures.

A further limitation of the study is that we have considered only one case site that did not fully achieve network alignment, albeit through multiple phases of development over a period of many years. This limitation was driven by the dif<sup>fi</sup>culties of studying networks comprising many partners, which greatly multiplies the dif<sup>fi</sup>culty of data collection and analysis. Replicating and extending our results through comparison with other networks should be a goal for future research, for example, by examining systems shared among airlines in alliances (e.g., Hirnle & Hess, 2007) or emerging

<table><tr><td rowspan="3" colspan="2">health IS that link multiple providers (e.g., Salmivalli, 2008).</td><td>ARC IP</td><td>ARC Interoperability Project</td></tr><tr><td>ARC</td><td>ARC Tailored Incident Management Europe</td></tr><tr><td>TIME</td><td>system</td></tr><tr><td>AA</td><td>The Automobile Association (of Britain)</td><td>B2B</td><td>Business to business</td></tr><tr><td>AAA</td><td>American Automobile Association</td><td>ICT</td><td>Information and communications technology</td></tr><tr><td>ACI</td><td>Automobile Club d&#x27;Italia (Automobile Club of Italy)</td><td>ÖAMTC</td><td>Österreichische Automobil-, Motorrad- und Touring Club (Austrian Automobile, Motorcycle and Touring Club)</td></tr><tr><td>ACTA</td><td>Automobile Club Touring Assistance (French operating arm of ARC)</td><td>RACE</td><td>Real Automóvil Club de España (Royal Automobile Club of Spain)</td></tr><tr><td>ADAC</td><td>Allgemeiner Deutscher Automobil-Club (General German Automobile Club)</td><td>SOA</td><td>Service-oriented architecture</td></tr><tr><td>ANWB</td><td>Algemene Nederlandse Wielrijders Bond (General Dutch Wheel-Riders Club)</td><td>TCB</td><td>Touring Club de Belgique/van België (Touring Club of Belgium)</td></tr><tr><td>ARC</td><td>Auto and Road Clubs</td><td>TCS</td><td>Touring Club Schweiz (Swiss Touring Club)</td></tr></table>

## About the authors

Bernhard R. Katzy started his professional career as a car mechanic and later earned master degrees in electrical engineering and business management. He earned a Ph.D. in industrial management from University of Technology (RWTH) Aachen in Germany and a second Ph.D. (habilitation) in general management and technology management from University of St. Gallen, Switzerland. Until his untimely death in November 2015, he was professor at the University BW Munich (D) and Leiden University (NL), and director of CeTIM – Center for Technology and Innovation Management.

## References

ANDRES B and POLER R (2015a) Dealing with the alignment of strategies within the collaborative networked partners. In 6th IFIP WG 5.5/ SOCOLNET Doctoral Conference on Computing, Electrical and Industrial Systems (DoCEIS 2015): Technological Innovation for Cloud-Based Engineering Systems (CAMARINHA-MATOS LM, BALDISSERA TA, DI ORIO G AND MARQUES F Eds), pp 13–21, Springer International Publishing, Costa de Caparica, Portugal.

ANDRES B and POLER R (2015b) Models, guidelines and tools for the integration of collaborative processes in non-hierarchical manufacturing networks: a review. International Journal of Computer Integrated Manufacturing 29(2), 1–36.

ANSOFF HI (1979) Strategic Management. Wiley, New York, NY.

AVISON D, JONES J, POWELL P and WILSON D (2004) Using and validating the strategic alignment model. Journal of Strategic Information Systems 13(3), 223–246.

BARTLETT CA and GHOSHAL S (1989) Managing Across Borders: The Transnational Solution. Harvard Business School, Boston, MA.

B M and W P (1993) Improving business and information strategy alignment: learning from the banking industry. IBM Systems Journal 32(1), 162–179.

BURN JM and SZETO C (2000) A comparison of the views of business and IT management on success factors for strategic alignment. Information & Management 37(4), 197–216.

BYRD TA, LEWIS BR and BRYAN RW (2006) The leveraging influence of strategic alignment on IT investment: an empirical examination. Information & Management 43(3), 308–321.

C -M LM, A H and O M, Eds (2008) ECOLEAD and CNO base concepts. In Methods and Tools for Collaborative Networked Organizations, pp 3–32, Springer, New York, NY.

C YE, H S, C D and B DW (1997) Business strategic orientation, information systems strategic orientation, and strategic alignment. Information Systems Research 8(2), 125–150.

Gordon Sung was a member of the Center for Technology and Innovation Management’s Virtual Organisation Competence team. He received his Ph.D. on the topic of Coordination & Communication of Virtual Projects.

Kevin Crowston is a Distinguished Professor of Information Science in the School of Information Studies at Syracuse University. He joined the school in 1996. He received his A.B. (1984) in Applied Mathematics (Computer Science) from Harvard University and a Ph.D. (1991) in Information Technologies from the Sloan School of Management, Massachusetts Institute of Technology (MIT).

CHAN YE and REICH BH (2007) IT alignment: what have we learned? Journal of Information Technology 22(4), 297.

CHUNG SH, RAINER Jr. RK and LEWIS BR (2003) The impact of information technology infrastructure flexibility on strategic alignment and application implementations. Communications of the Association for Information Systems 11(1), 191–206.

CIBORRA CU et al Eds (2000) A critical review of the literature on the management of corporate information infrastructure. In From Control to Drift: The Dynamics of Corporate Information Infrastructure, pp 15–40, Oxford University Press, Oxford.

CROTEAU A-M and RAYMOND L (2004) Performance outcomes of strategic and IT competencies alignment. Journal of Information Technology 19(3), 178–190.

DAVENPORT TH (1993) Process Innovation: Reengineering Work Through Information Technology. Harvard Business School, Boston.

EISENHARDT KM (1989) Building theory from case study research. Academy of Management Review 14(4), 532–550.

G M, C C and K N (2013) Airline codeshare alliances. Business & Information Systems Engineering 5(3), 153–163.

GEROW JE, THATCHER JB and GROVER V (2014) Six types of IT-business strategic alignment: an investigation of the constructs and their measurement. European Journal of Information Systems 24(5), 465–491.

GULATI R (1998) Alliances and networks. Strategic Management Journal 19(4), 293–317.

H O and B K (2000) Who’s in control: designers, managers – Or technology? Infrastructures at Norsk Hydro. In From Control to Drift: The Dynamics of Corporate Information Infrastructure (CIBBORA CU, BRAA K, CORDELLA A, DAHLBOM B, FAILLA A, HANSETH O, HEPSØ V, LJUNGBERG J, MONTEIRO E and SIMON KA, Eds), pp 125–147, Oxford University Press, Oxford.

HEKKALA R and URQUHART C (2013) Everyday power struggles: living in an IOIS project. European Journal of Information Systems 22(1), 76–94.

HENDERSON JC and VENKATRAMAN N (1999) Strategic alignment: leveraging information technology for transforming organizations. IBM Systems Journal 38(2-3), 472–484.

HIRNLE C and HESS T (2007) Investing into IT infrastructures for inter-firm networks: star alliance’s move to the common platform. The Electronic Journal for Virtual Organizations and Networks 8(March), 124–143.

HUSSIN H, KING M and CRAGG P (2002) IT alignment in small firms. European Journal of Information Systems 11(2), 108–127.

JARVENPAA SL and IVES B (1993) Organizing for global competition: the fit of information technology. Decision Sciences 24(3), 547–580.

KAPPELMAN L, MCLEAN E, JOHNSON V and GERHART N (2014) The 2014 SIM IT key issues and trends study. MIS Quarterly Executive 13(4), 237–263.

KEARNS GS and SABHERWAL R (2006) Strategic alignment between business and information technology: a knowledge-based view of behaviors, outcome, and consequences. Journal of Management Information Systems 23(3), 129–162.

KING WR and SETHI V (1999) An empirical assessment of the organization of transnational information systems. Journal of Management Information Systems 15(4), 7–28.

KING WR and SETHI V (2001) Patterns in the organization of transnationa information systems. Information & Management 38(4), 201–215.

K LJ and H MH (2006) Requirements determination for common systems: turning a global vision into a local reality. Journal of Strategic Information Systems 15(2), 79–104.

KUMAR K and VAN DISSEL HG (1996) Sustainable collaboration: managing conflict and co-operation in inter-organizational systems. MIS Quarterly 20(3), 279–300.

LEYMANN F, ROLLER D and SCHMIDT M-T (2002) Web services and business process management. IBM Systems Journal 41(2), 198–211.

MANDAL P, LOVE PED and IRANI Z (2003) Pre-alliance planning: development of an information system infrastructure to support strategic alliance activities. Management Decision 41(1/2), 132–140.

MOWSHOWITZ A (1997) Virtual organization. Communications of the ACM 40(9).30-37.

PEPPARD J (1999) Information management in the global enterprise: an organising framework. European Journal of Information Systems 8(2), 77–94.

PHILLIPS N, LAWRENCE TB and HARDY C (2000) Inter-organizational collaboration and the dynamics of institutional fields. Journal of Management Studies 37(1), 23–43.

POLLALIS YA (2003) Patterns of co-alignment in information-intensive organizations: business performance through integration strategies. International Journal of Information Management 23(6), 469–492.

REICH BH and BENBASAT I (2000) Factors that influence the social dimension of alignment between business and information technology objectives. MIS Quarterly 24(1), 81–113.

SABHERWAL R and KIRS P (1994) The alignment between organizational critical success factors and information technology capability in academic institutions. Decision Sciences 25(2), 301–330.

SALMIVALLI L (2008) Governing the implementation of a complex interorganizational information system network: the case of Finnish prescription. PhD Thesis, Turku School of Economics. University of Turku, Tampere, Finland.

SANDERS NR (2005) IT alignment in supply chain relationships: a study of supplier benefits. Journal of Supply Chain Management 41(2), 4–13.

SENGE PM (1990) The Fifth Discipline: The Art and Practice of the Learning Organization. Century Business, London.

SLEDGIANOWSKI D and LUFTMAN J (2005) IT-business strategic alignment maturity: a case study. Journal of Cases on Information Technology 7(2), 102–120.

TEO TS and KING WR (1997) Integration between business planning and information systems planning: an evolutionary-contingency perspective. Journal of Management Information Systems 14(1), 185–214.

TIWANA A and KONSYNSKI B (2010) Complementarities between organizational IT architecture and governance structure. Information Systems Research 21(2), 288–304.

VELCU O (2010) Strategic alignment of ERP implementation stages: an empirical investigation. Information & Management 47(3), 158–166.

VOLKOFF O, CHAN YE and NEWSON EFP (1999) Leading the development and implementation of collaborative interorganizational systems. Information & Management 35(2), 63–75.

WIJNHOVEN F, SPIL T, STEGWEE R and FA RTA (2006) Post-merger IT integration strategies: an IT alignment perspective. Journal of Strategic Information Systems 15(1). 5–28.

YAYLA AA and HU Q (2012) The impact of IT-business strategic alignment on firm performance in a developing country setting: exploring moderating roles of environmental uncertainty and strategic orientation. European Journal of Information Systems 21(4), 373–387.

YIN RK (2003) Case Study Research: Design and Methods. SAGE Publications, Thousand Oaks, CA.
