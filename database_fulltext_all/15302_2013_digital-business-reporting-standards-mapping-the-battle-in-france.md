---
otero_id: 15302
otero_key: "7WM2URY5"
title: "Digital business reporting standards: mapping the battle in France"
authors: "Véronique Guilloux; Joanne Locke; Alan Lowe"
year: "2013"
journal: "European Journal of Information Systems"
doi: "10.1057/ejis.2012.5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
RESEARCH ARTICLE

# Digital business reporting standards: mapping the battle in France

Ve´ronique Guilloux<sup>1</sup>, Joanne Locke<sup>2</sup> and Alan Lowe<sup>3</sup>

<sup>1</sup>LEMNA, UPEC, France; <sup>2</sup>Birmingham Business School, University of Birmingham, U.K.; <sup>3</sup>Aston Business School, Aston University, U.K.

Correspondence: Joanne Locke, Department of Accounting and Finance, Birmingham Business School, University House, Edgbaston Park Road, Birmingham, United Kingdom B15 2TT. Tel: þ 44 121 4145647; Fax: þ 44 121 4146678; E-mail: j.locke@bham.ac.uk

## Abstract

Government agencies use information technology extensively to collect business data for regulatory purposes. Data communication standards form part of the infrastructure with which businesses must conform to survive. We examine the development of, and emerging competition between, two open business reporting data standards adopted by government bodies in France; Electronic Data Interchange for Administration, Commerce and Transport (EDIFACT) (incumbent) and eXtensible Business Reporting Language (XBRL) (challenger). The research explores whether an incumbent may be displaced in a setting in which the contest is unresolved. Latour’s translation map is applied to trace the enrollments and detours in the battle. We find that regulators play an important role as allies in the development of the standards. The antecedent networks in which the standards are located embed strong beliefs that become barriers to collaboration and fuel the battle. One of the key differentiating attitudes is whether speed is more important than legitimacy. The failure of collaboration encourages competition. The newness of XBRL’s technology just as regulators need to respond to an economic crisis and its adoption by French regulators not using EDIFACT create an opportunity for the challenger to make significant network gains over the longer term. ANT also highlights the importance of the preservation of key components of EDIFACT in ebXML. European Journal of Information Systems (2013) 22, 257–277. doi:10.1057/ejis.2012.5; published online 24 April 2012

Keywords: Business Data standards; EDIFACT; XBRL; ebXML; Actor Network Theory; France

## Introduction

Data standards for the exchange of business information are an important enabling technology embedded in the digital infrastructure used by governments to regulate companies and capital markets (Borras, 2004; Camp & Vincent, 2004). The 2008 subprime credit crisis and subsequent crash of many western capital markets has created pressure on regulators to respond by improving transparency and tightening regulation (European Parliament, 2009; Financial Stability Board, 2009). Changes to the infrastructure of e-government are costly for companies that must modify their systems to comply with no expected return on their investment (van Oosterhout et al, 2006). For this reason, regulators seek to align the interests of submitting companies by claiming that the implementation of advances in Information Communication Technology (ICT) not only improve their surveillance, but also increase their efficiency in relation to submitters and reduce their cost of compliance (European Parliament, 2009: Roth, 2009).

Our research focuses on two business ICT data standards in France; Electronic Data Interchange for Administration, Commerce and Transport (EDIFACT) and eXtensible Business Reporting Language (XBRL). The EDIFACT data standard is widely used in Europe and up until recently was the uncontested incumbent financial data exchange format in France. Since the development of the EDIFACT standard in the early 1990s, a significant shift in technology for data exchange on the Internet has occurred. Extensible Markup Language (XML) is an offshoot of Standard Generalized Markup Language and has been widely adopted as a basis on which to develop specific formats for data exchange (Scheier, 2003). A number of standards based on XML have been developed in the business sphere. These include XBRL and electronic business XML (ebXML), among others. EbXML is of interest because of its close relationship with EDIFACT. The XML standard of particular interest, however, is the one challenging EDIFACT in France – XBRL. This standard has a completely different genesis to EDIFACT and is now well established in other jurisdictions (Kernan, 2008).

In the context of pressure on regulators to make changes, the battle between these two standards for dominance in France provides a richly textured setting in which to contribute to the standards battle literature. The emphasis in the previous research has been on mechanisms to assist corporate management to act strategically to make gains from internally developed standards (Shapiro & Varian, 1999a; Suarez, 2004; De Vries et al, 2008; Lyytinen et al, 2008). In contrast, EDIFACT and XBRL are international open data standards developed by groups of participants on a voluntary basis. Battles between such standards are expected to be driven by different considerations and have been comparatively under-researched (Lee & Oh, 2006; De Vries et al, 2008).

Actor Network Theory (ANT) (Law, 1992, 2000; Latour, 1999) is used to place a focus on the fabrication of the standards through the formation of networks of actors and objects (Hanseth et al, 2004). In particular, Latour’s translation map (Akrich & Latour, 1992; Latour, 1992) provides a conceptual framing for how the boundary of the incumbent network (EDIFACT) is shaped by adding allies, making compromises or ceding ground to the challenger (Ciborra et al, 2001). Only a very few studies have used ANT in research on standards battles (see, for example, Lee & Oh, 2006), but we identify the translation map as well suited to the analysis of standards battles.

A central concern in a standards battle is whether an incumbent standard may be displaced. Our research traces the networks while the controversy is still active, so we are able to follow the action but there is not a clear victor. Rather, we are concerned with identifying the important allies for business reporting standards and their role in expanding and bracing the standards’ networks. The international setting also provides an opportunity to explore the impact of the ‘location’ of the networks on their potential for collaboration rather than competition, and how it may shape their structures and approaches to developing a data standard. We draw out these themes from a detailed tracing of the antecedent and contemporaneous networks of EDIFACT and XBRL. The study also highlights the theoretical contribution of ANT, in particular, focusing on the potential to draw attention to the core semantics inscribed in data standards.

The next section of the paper locates our research in the context of the literature on standards battles. We then present a theorization, informed by ANT, of the standards battle as constituted within complex socio-technical networks. The next section details the methods and data used as a basis for the analysis. The case study section begins with a description of the broad financial reporting domain followed by the specific characteristics of the French environment. The development of the EDIFACT program is traced using the translation map to direct attention to the expansion of the network and associated substitutions and detours. XBRL as an anti-program in France is described; analyzing the emergence of competition between the standards as some European Commission (EC) and French regulators adopt XBRL. The discussion of the findings and contribution of the paper highlights the issues that emerge from tracing the action on the translation map and finally, conclusions are drawn.

## Standards battles

The literature on standards battles provides important insights building on research into the innovation, development and diffusion of standards. It seeks to address the question of why one standard achieves dominance and not another (Katz & Shapiro, 1985; David & Greenstein, 1990; Schilling, 1998; Shapiro & Varian, 1999a; Suarez, 2004, 2005). Central to the understand ing that has developed are the related concepts of; network externality (Katz & Shapiro, 1985), technological trajectories or path dependence (David, 1985; Stango, 2004) and technological lockout (Schilling, 1998). Expressed simply, standards battles arise because of the benefits that accrue to the sponsor of a standard through ‘locking-out’ competitors (or locking-in consumers) if they achieve an installed base that is self-sustaining and makes it difficult for another standard to build the critical mass necessary to break their dominance (the network effect). This is why the timing of development (the trajectory or path) is critical. If another standard has already achieved dominance, it creates a significant barrier to new entrants.

Crucially, research demonstrates that the standard with the ‘best’ technical characteristics may not be successful for a range of social, institutional and managerial reasons (Rosenbloom & Cusumano, 1987; Schilling, 1998; Hanseth, 2001; Suarez, 2004; Hemetsberger & Reinhardt, 2009). This means that the outcome of a standards battle is not determined by the technology, but is likely to be impacted by the actions of those involved. Consequently, a significant part of the standards battles literature focuses on identifving frameworks for analvzing strategic approaches by the management of firms sponsoring proprietary standards (Schilling, 1998; Shapiro & Varian, 1999b; Suarez, 2004; Windrum, 2004; Potter & Cohen, 2010).

The increasing importance of open standards for the Internet brought into question the emphasis on management strategies to accrue the benefits of ‘lockout’ since the ‘appropriability regime’ (Suarez, 2004, p. 276; Oshri et al, 2010) is much less likely to be a factor when the standard development process and outputs are openly available. Network externality and path dependency are still found to be important factors in open standards battles and diffusion (Arthur, 1989; Bonaccorsi & Rossi, 2003; Zhu et al, 2006; Boh et al, 2007). Therefore, while the issues are different, the standards battles are still energetic and even vitriolic because the incumbent will reap the benefit of a critical mass of users, and becoming part of the infrastructure while a challenger must struggle to gain ground before the lack of momentum causes it to fail (Bonaccorsi & Rossi, 2003).

The need for open standards for the Internet has also lead to the increasing importance and proliferation of international standard setting bodies (Camp & Vincent, 2004). Recent research on the process of developing standards has focused on this setting (Jakobs, 2000; Choi et al, 2004; Lee & Oh, 2006; Nickerson & zur Muehlen, 2006; Boh et al, 2007; De Vries et al, 2008; Egyedi & Koppenhol, 2010). Seeking to achieve greater universality in standard setting increases the socio-technical complexity because of the greater heterogeneity of the actors and the broader scope of the standard (Hanseth et al, 2006; see also, Lee & Oh, 2006; Choi et al, 2009). Our research aims to capture some of that complexity using the setting of a standards battle between two open international standards setting bodies to trace the process and issues affecting the trajectory of the incumbent standard.

The two bodies also provide an interesting contrast between a formalized standard setting process conducted within the institution of a government-backed body and a private consortium, which uses a membership model and a ‘market driven’ approach. Blind & Gauch’s (2008) study analyzes two surveys of standard setting consortia and concludes that intensive contacts between formal standard setting bodies and (informal) consortia is one of the factors that ‘promote[s] complementary rather than substitutive relationships between activities’ (p. 512) in the two types of organizations. Our case study shows the barriers to network formation created through different attitudes to legitimacy (Garud et al, 2002; Blind & Gauch, 2008) and entrenched in the networks of each organization and so casts doubt on the generalizability of this finding.

This research extends the growing literature on open standards battles, particularly in the business reporting domain. Our study is theorized using ANT and in particular Latour’s (1992) conceptualization of the sociology of translation. These ideas are captured in the translation map Latour uses as a research device to demonstrate the process of network building. We discuss this methodological approach and how it contributes to the existing standards battles literature in the next section.

## ANT, programs and anti-programs

ANT (Callon, 1986; Latour, 1987, 1991, 2005b; Law & Callon, 1992; Law, 2002) has been used by a number of writers to research ICTs and data standards (Tuomi, 2001; Hanseth et al, 2004, 2006; Chang & Jarvenpaa, 2005; Backhouse et al, 2006; Lee & Oh, 2006); in the business setting (Graham et al, 1995; Ciborra et al, 2001; Gendron & Barrett, 2004; Dechow & Mouritsen, 2005; Quattrone & Hopper, 2005); and in government (McGrath, 2002; Heeks & Stanforth, 2007).

Of particular interest for this study is the work of Lee & Oh (2006) applying an ANT in a setting involving international standards in which the openness of the standard is an issue. They adopt ANT’s four moments of translation in order to theorize the actions by Chinese authorities, as they tried to impose their wireless LAN authentication and privacy infrastructure (WAPI) standard on manufacturers of mobile communications products and associated technology. A distinctive feature of the case is that the standard is promoted by the government for exclusive adoption in the national setting, China. The standard itself was closed and ultimately WAPI failed to mobilize because of the strength of the opposing network. Lee and Oh identify the great difficulty any one standard setter faces in trying to achieve dominance internationally and the particular resistance to closed standards.

Lee & Oh’s (2006) analysis is limited to documentary evidence and the four moments of translation are applied as ‘stages’ (p. 179) in a framework to 47 relevant articles sourced from ABI/Inform (pp. 178–179). While it is sometimes necessary to rely on historical data, Latour (1987, 2005b) encourages the researcher to ‘follow the actors’ as social structures are fabricated. The networks and objects are best traced before they become ‘black boxed’, while the controversy among the different camps is at its height and the outcome uncertain (Latour, 1987, 1991, 1996, 2005a). In our setting, we are able to observe meetings and interview key individuals involved in the dispute, as well as accessing online communications and documents. We believe that this gives the closer proximity to the actors and the action to be able to assess better their responses and roles in the networks as a basis for interpretation.

Rather than focus on the four moments, which were never intended to be used as stages (Latour, 1999, 2005b), we adopt Latour’s (1992) idea that any technology development can be seen as a program of action and is always opposed by an anti-program. We theorize the battle by concentrating on the fabrication of the network around the program (in our case the incumbent EDIFACT) and an anti-program (XBRL). In particular, we adopt Latour’s translation map as a device to draw attention to the need for the program to add allies to the network, but that in the process something is given up; a detour is made (Latour, 1987, 1992). Latour (1992) describes the delegation of roles or action from human actors to objects or technology to solve problems, reduce effort or encourage specific programs of action.

In the process of designing and creating a technology object, individuals and other objects will be brought together into an assemblage by translating their interests to coincide with that of the desired program of action. The designers inscribe into the object the pattern of use and human behavior that they anticipate is necessary, but they may be mistaken, others may oppose their view or other factors may intervene. The inscriptions may not succeed and the actual use of the object may vary from the designer’s intention or face competition from others with a different view. ‘Rather than following its assigned program of action, a user may use the system in an unanticipated way, she may follow an anti-program’ (Hanseth & Monteiro, 1997, p. 186). In response, the program ‘braces itself’ against the anti-program by making changes or detours (Latour, 1992, p. 247).

The technologies of interest in our setting are standards for the digital exchange of data required for business reporting. The standards require the translation of accounting techniques and information technology (IT) expertise, as well as individual developers, businesses as preparers of accounts, regulators and users of financial information. In the process of adding to the network, for example, a particular approach will be taken to modeling a business process, an alternative that may have its ‘adherents’, must be given up. The loss of the part of the network may give rise to resistance and anti-programs.

We deploy Latour’s (1992) translation diagram to map the broad tensions between a program of action (EDI-FACT) and an anti-program (XBRL). The diagram enables us to represent the standards battle as it develops over time. It provides an organizing structure for the discussion of our research evidence.

Latour (1992) illustrates the translation diagram in an everyday context. He uses the simple example of how to protect his son who refuses to sit properly in the back of the family car. The map is reproduced as Figure 1. Latour uses a simple linguistic metaphor to explain the diagram. Associations in a sentence (made by adding elements using ‘and’) are represented on the horizontal axis. Substitutions (made by replacing elements, so they are optional – one ‘or’ the other) are represented on the vertical axis. A competent researcher, Latour argues, should be able to interpret the actions in the setting to identify the processes of translation that support, or perhaps negate, the program of action.

The relative success or failure of the program of action is shown as a line that demarcates the program that is being studied (on the left of the diagram) from the antiprogram (shown on the right) that it seeks to avoid or replace. It is plotted to show the translation of actors aligned (increasing the network takes the line to the right) but a downward movement is necessarily attendant on an increase in the network. ‘y it is impossible to move in the AND direction (horizontal) without paying the price of the OR dimension (vertical), that is, renegotiating the sociotechnical assemblage’ (Akrich & Latour, 1992; Latour, 1992, p. 251). The take-up of the technology is shown by movements to the right while modifications to the technology and/or the human allies of the program – the socio-technical assemblage – appear on the vertical axis.

Our research focuses on standards battle between two open international digital business reporting standards in France. We explore the translation of the interests of participants in very different networks that create the conditions for a battle rather than collaboration. The adoption of ANT emphasizes the role of the technology object: how it may enable and constrain, enroll actors and reduce options in the battle.

Following the actors: data collection and method The assemblages we describe are still forming and the technologies are not yet settled. We have observed developments over a period of 5 years including interviewing participants in the development of EDIFACT and XBRL. We have also attended international XBRL conferences, working group meetings, observed newsgroup discussions, related Web sites and obtained technical documents for both data standards. The weight of updates, e-mails and news items means that the data used as a basis for our interpretation cannot be fully documented. The Appendix provides a detailed summary and code to identify individual informants and meetings attended. The interviewee code is used to identify all quotes used in the paper.

![](/api/attachments/7WM2URY5/fulltext/images/bea229b4ea98b81dc8141ec77c7443fd1f244178556d61bda2f2604b68d3af3f.jpg)  
Figure 1 Latour’s (1992) translation diagram (Bijker, Wiebe E, and John Law, Eds, Shaping Technology/Building Society: Studies in Sociotechnical Change. Figure 8.7. p. 251. © 1992 Massachusetts Institute of Technology. by permission of The MIT Press).

In constructing the Appendix, a balance is necessary between providing enough information to understand the perspective of the interviewee, while preserving confidentiality. In a relatively small community this is an important issue, particularly in relation to senior people in the development of the data standards. Identifying their positions would mean identifying them as individuals, so we have used a generic description of individuals as ‘senior’ in their area rather than more precise titles. The explanation for the construction of the codes, which are designed to convey an impression of the perspective of the interviewee, is also provided in the Appendix.

In common with other ANT studies, we must make choices about how we focus our research (Law & Callon, 1992; Hanseth & Monteiro, 1997; Miller, 1997; Latour, 2005b). The data standards of interest have developed over time and in multiple locations, so we must necessarily select the elements of the networks and events we report, but we do so in a way that represents the issues and controversies to the best of our ability. Our tracing of the networks that constitute the programs of action are inevitably abbreviated (Law & Callon, 1992; Miller, 1997). In the sections that follow, we first introduce the features of our particular setting of regulated business reporting and the cultural and institutional aspects of France. These form the antecedent networks from within which the two standards developments emerge. As is highlighted later in the paper, the distinctive features of business reporting and the French regulatory environment strongly influence the formation of the networks for each of the standards. Then we trace the early development of EDIFACT and the rise of the challenger, XBRL.

## The origins of business reporting and digital standards

Governments have historically regulated citizens by collecting and (perhaps) redistributing income based on tangible, historically written, records. Centuries old structures for business reporting, based on a written record and often double entry, are still strongly inscribed into digital business standards that use the same organizing concepts from the accounting model and trace their history to an:

Accounting technique [that has] accompanie[d] the business background for more than five centuries when Luca Pacioli, a Venetian monk, invented the modern rules in 1494. (TBG12, 2005, p. 4)

As the technology has developed from written inscription (Latour, 1994; Star, 1996; Bloomfield & Vurdubakis, 1997) to digital, the prescription of the technology, the manner in which it disciplines and directs human action has changed the speed, efficiency and quantity of data that can be collected, stored and exchanged (Hanseth & Monteiro, 1997). The digital business reporting standards that are the focus of our study are a complex combination of bodies of knowledge (Choi et al, 2009) that are drawn into a network by government regulators to increase the speed and efficiency of their surveillance.

Potential participants need to be persuaded that the technology makes it easier and possibly cheaper for them to comply; problematizing the existing approach and enrolling their participation in the ‘solution’ (see, for example, Standard Business Reporting, 2009). Government regulators may also be recruited to argue that the new system will be more accurate and will lead to ‘fairer outcomes or greater reliability. The processes of enrollment are affected by local attitudes to regulation and accountability. We consider the unique characteristics of the French setting that gave rise to it being a very early adopter of digital business regulatory reporting in the next section.

## Preconditions for digital reporting in France: the antecedent network

French accounting regulation historically developed distinctive characteristics that placed French standard setters in a strong position to create the interoperable platform needed for electronic exchange of business data. One of the key factors was the existence of a common chart of accounts used by all companies. The Plan Comptable Ge´ne´ral itself was the outcome of networks of allies (and enemies in the case of the claimed influence of the Goering Plan) and its fortunes have fluctuated over the years (Standish, 1990; Colasse & Standish, 1998). It was promulgated in 1947 and has applied in both public and private enterprises since. Its establishment and use in France since that time provides a very different setting compared with that in Anglo-American countries, where the emphasis is on the report produced providing a ‘true and fair’ representation and there is no common definition of accounts.

The essential difference in approach to accounting perhaps lies in the French attitude of dirigisme – economic and social regulation by the state. The requirement to use a standard chart of accounts in France represents a significant regulation of the process of accounting, as well as its outputs and it generated significant opposition at its introduction (Standish, 1990), but has since become very widely accepted. A senior employee of a French company we interviewed expressed it neatly; ‘France is Descartes’ country and has its proper norms. We consider the Plan Comptable Ge´ne´ral as a beautiful intellectual structure’ (User6).

The weight of influence has changed since interest in a standardized chart of accounts was first stimulated in

1947/8, however. In the latest of three amendments to the Plan, the process of harmonizing it with International Financial Reporting Standards (IFRS) has been significantly advanced (Focus PCG, 2009). These changes occurred in spite of French resistance to the ‘invasion’ of foreign accounting practices (Colasse & Standish, 1998; Ramirez, 2008). The requirements of the Directives of the EC (including the 4th and 7th) and subsequent regulations (European Commission, 2009) to coordinate national laws governing the annual accounts of public limited liability companies are designed to facilitate a single European capital market. These directives, along with other factors, such as the adoption of IFRS, have progressively shifted the French approach to accounting and its regulation closer to the European consensus, which in turn is increasingly shaped by Anglo-American capital market dominance (Chiapello, 2005; Ramirez, 2008).

However, at the time that electronic transmission of data was emerging, the French emphasis on standardized processes of accounting put them ahead of other jurisdictions and provided a standardized way of defining elements of accounting data (meta-data) required for electronic communication. This framework for accounting information was already in existence in those countries adopting the Plan Comptable Ge´ne´ral and an attitude that accepted that data items could be defined by the state was already established; reducing the barriers to enrollment in the program created by a resistance to imposed standardization in Anglo-American countries.

In a setting in which an international standard is being developed, a parochial approach may also be a disadvantage, as described by an interviewee from the XBRL perspective:

For many French what is American is bad. We must prove that French are stronger than foreign countries. There is a lot of pressure to develop something French. y If there is not an international institution which harmonizes, the French will not be able to exchange with other countries. (XDev3)

The broader tension between European and American standards development has also been documented (Zuckerman, 1999). As is shown in the description of the development of EDIFACT that follows, this preference for local approaches facilitated early adoption of electronic exchange in France, enabled dominant participants to inscribe their interests into the standards, and contributed to the complexity and tension in international standard setting.

## Tracing the EDIFACT network

Electronic Data Interchange (EDI) may be ‘defined as a set of message standards to enable the exchange of commercial transaction data between autonomous application systems without human intervention’ (Pfeiffer, 1992 quoted in Graham et al, 1995, p. 4). In common with other standards for the exchange of business data, they are negotiated and defined for specific settings (Damsgaard & Truex, 2000).

The development of EDI reporting to government bodies in France may be linked to the creation of what is now the Directorate General of Administration and Civil Service and a program of reforms beginning with the ‘Modernisation de l’Etat Franc¸ais’ order in 1945. The purpose is to motivate the ‘State to constantly upgrade to adapt to changes in the world and society’. This ‘reform of the state’ must make the administration more ‘efficient and improve services provided to users’ (translated from La Documentation Franc¸aise, 2009). The strong government support and the depth of acceptance of standardized reporting already in existence provided a broad network of allies and existing problematization for the development of EDIFACT and the jedeclare.com portal.

Many different proprietary systems were ‘closed’ and intended to ‘lock in’ users, providing a basis to bind supply chain partners to adopt the same software (Garud & Kumaraswamy, 1993). This is a particular issue for accountants because public accounting firms receive data from many clients and play a pivotal role as an intermediary in further submitting data in required formats to government agencies. The pre-existing structure for the chart of accounts, the French government’s active approach to increased efficiency and the emerging need for open standards provided a conducive environment for a business reporting standard to emerge. This was in contrast to the U.S. environment in the late 1980s and early 1990s. Interviewees from both perspectives saw this as important:

France would be in advance compared with U.S.A. [for the development of a digital accounting standard] as we have already deeply structured our accountability. (XDev3)

In France when a Chartered accountant prepares a chart of accounts, he does it one time and it’s done for all. In America the structure is different for each firm and this is a big source of work [and income for the accountant]. y France is not the same context as U.S.A. (EDev1)

## Mapping the development of EDIFACT

The development of an open system for data exchange can be traced to the early 1990s in the context we are studying. In 1992, a French non-profit body was formed as the result of an initiative of l’Ordre des Experts-Comptables (the French professional accounting association) to promote electronic data interchange for fiscal, informational, countable, analytical and of audit, and social (EDIFICAS France) was formed. The initial members included representatives of a total of eleven accounting and consulting firms and software companies (www.edificas.fr). Its purpose was to promote the use of EDI for the exchange of business information. A key task was to develop an open standard to unlock the possibilities of ICT for data exchange. This is the starting point for the ‘EDIFACT program’ on our translation map in Figure 2 (see Point A on the diagram and Table 1).

AND  
![](/api/attachments/7WM2URY5/fulltext/images/0074d283007c8c1d8e322e67c98479238ceb597a7bfb932b6ebac9aadd222043.jpg)  
Figure 2 Translation map for the development of EDIFACT program.

Table 1 A summary of key events

<table><tr><td></td><td>Event/decision</td><td>Addition to the network</td><td>Substitution</td></tr><tr><td>A</td><td>EDIFICAS formed by l’Ordre des Experts-Comptables</td><td>European accounting and consulting firms, professional bodies, Edifrance</td><td>Efficiency of operation in the French language reduced participation by non-French speaking representatives</td></tr><tr><td>B</td><td>Operate as a UN/CEFACT working group TBG 12</td><td>Formal support and structure of UN/CEFACT; links with other working groups; recognition by EC, ISO</td><td>Speed of development</td></tr><tr><td>C</td><td>TELER project &amp; Jedeclaire.com portal</td><td>EC funding; European regulatory bodies; INSEE; DGI; evidence of cost savings; application in portal collecting fiscal information from French businesses through accountants; adoption for the Etafi platform for large businesses in France; adoption elsewhere in Europe</td><td>Perceived close link between regulations and message formats; as part of the infrastructure it is taken for granted (&#x27;no-one is speaking of it&#x27;)</td></tr><tr><td>D</td><td>Emergence of new technology – XML</td><td></td><td>Requires splitting the effort to protect the work already invested in the EDIFACT messages – creation of ebXML</td></tr><tr><td>E</td><td>XBRL adoption European banking regulators and Infogreffe</td><td></td><td>The potential for adoption in this sector is lost to the EDIFACT network and XBRL develops an installed user base of at least 650 banks in France (XBRL France)</td></tr></table>

EDIFICAS is widely identified as a singularly French initiative (see, for example, Coffin, 2000). There is, however, a European EDIFICAS that similarly was motivated by accounting professional bodies and included representation from Belgium, the Netherlands, Denmark, Finland, England, Germany, Italy and Spain (EDev3).

The participation of the wider European countries fell away, however, leaving a core membership of (French speaking) Belgian and French representatives – contributing to the identification of EDIFICAS as a French body. There was significant support for EDIFICAS in France. In addition to the support of l’Ordre des Experts-Comptables, it was accredited as a ‘sectoral’ community by the organization of coordination EDIFRANCE.

The strength of the French commitment was reflected in the dominant use of French in developing projects and meetings (Edev3). The complexity of trying to translate into multiple languages created a barrier to participation and over time it contributed to the loss of the active participation of other country representatives (EDev3).

In the early 1990’s, the technological setting included the growing use of the Internet, but XML and the large storage capacities common today were not yet available. EDIFACT achieved recognition by the EC, the International Organization for Standardization (ISO) and by the United Nations (UN), referring to the standard as UN/ EDIFACT. Progress on the standard was reported to the UN using a ‘Rapporteurs’ structure’. The next step was to migrate the EDIFACT group into the UN/CEFACT structure and to create working groups that would operate in accordance with the goals and procedures of CEFACT. This involved significant resources and effort to document the project in line with UN/CEFACT requirements, which included:

The mandate for empowerment of a Working Group may be prepared by an existing group, the Steering Group, or the Plenary. All mandates must specify:

– the overall objectives of the work (scope and purpose); – the key deliverables;

– the geographical focus, i.e. global, regional or national; – the functional expertise for membership;

– any request for delegated responsibilities. (UN/EDIFACT Steering Group, 1997)

The EDIFACT program achieved membership of UN/ CEFACT in March 1998 (UNCEFACT, 1998). Members of EDIFICAS formed part of the International Trade and Business Processes Group (TBG) 12 in charge of accounting, auditing, registration and financial information services in the project (EDev3; Graham et al, 1995; UN/ CEFACT Forum TBG12, 2001). This group was responsible for business reporting, which is the domain of contention we are studying.

Table 2 EDIFACT standard messages

<table><tr><td>Message</td><td>Purpose</td></tr><tr><td>ENTREC (accounting entries)</td><td>Collection of entries into a journal</td></tr><tr><td>LEDGER</td><td>Provides a series of accounts such as general ledger, cost accounting, budget ledger</td></tr><tr><td>BALANC</td><td>Any kind of trial balance</td></tr><tr><td>CHACCO (chart of accounts)</td><td>To transmit any type of chart of accounts</td></tr><tr><td>INFENT (enterprise information)</td><td>The generic container for any electronic declaration procedure (e.g., fiscal return, VAT declaration, reporting, financial statement, etc.)</td></tr></table>

The decision to align the creation of the standard with the UN and ISO was important for EDIFACT. The addition of these allies is shown as strengthening the network, moving the boundary to the right (see Point B on the Figure 2). The alliances provide the authoritative support, legitimacy, careful procedures, and checks and balances not present in many ‘market’ developments of standards (Garud et al, 2002; Weitzel et al, 2006). This development is compatible with the attitudes of the participants in the existing network with their acceptance of government lead standardization and the need for process and rigor. So not only are allies added, but also the existing attitudes are reinforced.

There is increased complexity in dealing with multilingual participants, which is inherent in UN activities. This may have been reduced by the concentration of French speaking participants in TBG12, but at the cost of reduced participation from elsewhere in Europe. It is also very likely that there was a slower delivery of the standard’s ‘messages’ as a result of the formal consensus required (EDev3; Graham et al, 1995). The standard accounting messages that TBG12 developed are shown in Table 2 (http://www1.unece.org/cefact/platform/display/ TBG/TBG12; see also http://www.unece.org/trade/untdid /d11a/trmd/trmdi1.htm for an up-to-date list of all EDIFACT messages).

Each of the approved messages comes with the imprimatur of the UN (see Figure 3).

EDIFICAS also became involved in a project that was important in promoting the concept of EDI for government reporting. The TELematics for Enterprise Reporting (TELER) project was run by a consortium of regulatory bodies, standard setters and companies with approximately 50% funding from the EC. Participants were from countries including Finland, France, Germany, Italy, the Netherlands, Portugal and Spain and they sought to identify EDI solutions to achieve the ‘reduction of costs for the enterprises in their efforts for answering questions of governmental collectors’ (Fouquie\`res & Stol, 1999). It was a trial to establish the business case for EDI. The reason for conducting the trial in France was the already existing standard chart of accounts (Fouquie\`res &

United Nations Directories for Electronic Data Interchange for Administration, Commerce and Transport  
![](/api/attachments/7WM2URY5/fulltext/images/1d7269f039f3116c47a7e9f806423e92f1746163a41b0148db4eb88a15ee7631.jpg)  
Figure 3 Extract of cover page from EDIFACT ENTREC message (size reduced).

Stol, 1999, p. 14). It successfully enrolled government entities and reporting companies and claimed to demonstrate across all the applications tested (of which EDIFACT was one of three) 80–90% cost savings from the perspective of both the filing and receiving entities (Fouquie\`res & Stol, 1999). It was a significant milestone in the acceptance and diffusion of EDIFACT (EDev1, EDev3) (see Point C on Figure 2).

In 1997, while the TELER project was underway, the DGI chose to work in conjunction with EDIFICAS France to align with the EDIFACT standard to develop specific procedures to permit the digital transmission of data from businesses to regulators (Infotrans and DGI) (EDev1). This was an important step toward building a network for the later inclusion of the EDIFACT standard in regulator data collection and dissemination portals (e.g., jedeclare.com). However, it may also have created a negative impression suggesting a need to update the standard as regulations change:

EDIFACT is based on paper fiscal representation. It follows the specification of the DGI y Fiscal [tax accounting] is omnipresent. y With the amount of the accounting charge, the DGI wants to know if it’s a deductable cost. If yes its goes to this box. If not it goes to another cost. The accountant is only interested in the amount of cost. (XDev3)

In 2001, an important development in the diffusion of EDIFACT was the creation of a portal for the electronic receipt of submissions to the Ministry of Finance. One informant described the genesis of the jedeclare.com portal as follows:

Jedeclare.com portal. Yes. ‘I declare dot com’. So that is a portal where as well as the collector, the declarant has found an interest. This portal was created after Mr. Sarkozy who is now the president of France and was then the Minister of Finance, said ‘I want that the Ministry of Finance collect all the fiscal returns electronically!’. (EDev3)

Because of the early work of EDIFICAS, including the participation in TELER, the INFENT message, created as part of EDIFACT, was available just as the pressing need to relieve the administrative burden on submitting entities (‘declarants’) found a powerful champion in Mr. Sarkozy. The result was a platform that still functions very successfully today to provide ‘eform interfaces to facilitate teletransmission of fiscal, social, accounting and financial data to administrations, chartered management bodies, banks, social protection organisations and all other appropriate recipients’ (Archaeon, 2004, p. 1).

The jedeclare.com portal has been established for so long and is so extensively used in France that it has become part of the infrastructure of data exchange between accounting firms (on behalf of declarants), companies and the government. The program has advanced (Figure 2: Point C shows the boundary moving to the right) with the association of the portal. The network has been extended as additional users are added. It is estimated that 90% of accountants (des experts comptables) in France are registered to use the platform. In 2008, this was over 6300 accounting firms (EDev2). They file returns on behalf of the many small/mediumsized businesses that do not have their own accounting departments. Several of our interviewees confirmed that the jedeclare.com portal works efficiently and effectively, reducing compliance costs (e.g., EDev3; Reg1). So, despite the emergence of XML in the late 1990s there has not been any need to consider replacing it. ‘Nobody is speaking of EDIFACT, but everybody is using it’ (EDev3).

EDIFACT also has been successfully implemented in other government reporting applications. For example, in France it is the basis for large companies to report to the DGI though the privately developed Etafi platform (EDev1, EDev2, see also www.aspone.fr). As an UN standard, it has been adopted in many European countries and applied in high tech, civil aviation, retail and tourism industries (Turowski, 2000; Hawser, 2004). Since the technology is built into the infrastructure, it is ‘black boxed’ and taken for granted (Latour, 1987). The possible risk in this is that when active proponents of an alternative emerge to challenge the incumbent standard potential adopters may be persuaded by the promise of a new technology. This can bring the latent tension between the program and anti-program into open conflict.

## An anti-program: XBRL reporting technology

XBRL is an XML-based standard for business reporting developed by a private consortium of businesses, software vendors and regulators (www.xbrl.org). Among other things, XML provides a structure to allow tags that contain semantic definitions to be attached to individual data items to be exchanged electronically. The tags are defined by reference to a taxonomy (data dictionary) that specifies each tag’s meaning in a hierarchical structure. In this section, we consider the characteristics of XML as a technology ally that have particularly distinguished XBRL from EDIFACT and been important in constraining and facilitating the enrollment of others into XBRL’s network and strengthening its resistance in the battle. The two key characteristics are human readability and extensibility.

## Human readability

Because XBRL is based on XML, it uses taxonomies to provide meta-data for the semantics of the elements. The taxonomy can be referenced to external sources, such as accounting standards and regulations, to allow a user to validate the meaning attributed to tags. A feature of the tags is that they are expressed in human readable text (Keogh & Davidson, 2005). This means that there is not only the possibility for computer-to-computer communication, but also human users may ‘read’ the XML documents.

The readability advantage claimed for XML represents an interesting translation between human and nonhuman actors. The EDIFACT standard is specifically

Extract of CERFA form with EDIFACT code shown below

<table><tr><td colspan="2"></td><td colspan="2">Brut</td><td colspan="2">Amort, provisions</td><td>Net N</td><td>Net N-1</td></tr><tr><td colspan="2"></td><td></td><td>AP/MOA</td><td></td><td>AQ/MOA</td><td>DO/MOA</td><td>FC/MOA</td></tr><tr><td colspan="2">Constructions</td><td>AP</td><td>5 76 682,39</td><td>AQ</td><td>4 616 625,79</td><td>1 140 056,60</td><td>1 032134,45</td></tr><tr><td colspan="8"></td></tr><tr><td></td><td colspan="3">Brut</td><td colspan="2">Amort, Provisions</td><td>Net N</td><td>Net N-1</td></tr><tr><td>Construction</td><td colspan="2">AP</td><td>AP/MOA</td><td colspan="2">AQ</td><td>AO/MOA</td><td>DO/MOA</td></tr><tr><td></td><td colspan="2">Code del&#x27;impriméCerfa</td><td>Code EDI-tdfc</td><td colspan="2">Code del&#x27;impriméCerfa</td><td>Code EDI-tdfc</td><td>Code EDI-tdfc</td></tr></table>

Message EDI : SEQ ++ 15 IND++AP/MOA MOA <sup>5</sup> <sup>76</sup> <sup>682,39</sup> ; SEQ ++ 16 IND++AQ/MOA MOA <sup>4</sup> <sup>616</sup> <sup>625,79</sup> ; SEQ ++ 17 IND++DO/MOA MOA 1 140 056,60 ; SEQ ++ 18 IND++FC/MOA MOA 1032134,45

Extract of balance sheet showing XBRL coding below (in French) from Infogreffe

<table><tr><td></td><td colspan="3">Exercice N</td><td>Exercice N-1</td></tr><tr><td>ACTIF</td><td>Brut</td><td>Amortissement</td><td>Net</td><td>Net</td></tr><tr><td>Constructions</td><td>5 76 682,39</td><td>4 616 625,79</td><td>1 140 056,60</td><td>1 032134,45</td></tr></table>

Message XBRL: <xbrli:xbrl xmlns:tca-g=http://www.infogreffe.fr/fr/fr/tca-g/2008-05-3 <ca:ConstructionsNet contextRef="EY2007" decimals="0" unitRef="EURO">1 140 056</ca:ConstructionsNet> <ca:ConstructionsNet contextRef="EY2006" decimals="0" unitRef="EURO">1 032134 </ca:ConstructionsNet> <ca:ConstructionsAmortissementsEtDepreciations contextRef="EY2007" decimals="0" unitRef="EURO">4843416</ca:ConstructionsAmortissementsEtDepreciations> <ca:ConstructionsBrut contextRef="EY2007" decimals="0" unitRef="EURO">5765482</ca:ConstructionsBrut>

Figure 4 Extracts of two documents showing coding in EDIFACT and XBRL. Source: EXDev1; Guilloux, 2010, p. 258 and p. 260.

designed for computer-to-computer communication and is not designed to invite human intervention through readability (see Figure 4, which shows the same message in EDIFACT and XBRL). It is more efficient in that it results in significantly smaller files (EDev3; Sliwa, 2000). XBRL on the other hand delegates a role back to the human by offering the option of readability.

The number of occasions humans should need to read a document, the purpose of which is data exchange between computers, ought to be very low (EDev3). Yet, it appears to be an important ‘selling point’:

I’m sure that if there were a reader for EDI when XBRL arrived in France, XBRL wouldn’t have retained attention! Yes it is important for a human being to see what computers transport even if there’s no point in seeing it y human beings are like that. We have to work a lot on jedeclare to just have this possibility. (EDev2)

The human readability fulfills another purpose for the technology – enrolling more support from preparers of regulatory filings concerned about not being able to ‘see for themselves’ what is being transmitted. Given the exponentially increasing capacity of hardware to send and store data, the increased file size is perhaps not too much of a concession to make for the potential strengthening of the network.

## Extensibility

The ‘X’ in XML is from ‘extensible’ and in the case of XBRL, for example, the taxonomies themselves may be created from scratch by individual companies or extended to suit their needs. Like human readability, extensibility also offers a role back to the human in the process of instituting regulatory procedures and filing submissions. XBRL accounting taxonomies exist in a number of jurisdictions, but arguably the two most important ones are provided free for use by the Financial Accounting Standards Board (U.S. GAAP taxonomy) and the IFRS Foundation (IFRS taxonomy).

Regulators in countries such as the U.S., the Netherlands, Japan, Singapore and the U.K. require filing entities to use these taxonomies. Because taxonomies may be extended, however, the technology provides an opportunity for individual companies to change the concepts they use by adding new ones to those included in the prescribed taxonomy. Hanseth & Monteiro’s description that ‘some technologies inscribe weak/flexible programs of action while others inscribe strong/inflexible programs’ (1997, p. 186) is apt for the comparison between EDIFACT and XBRL. Since XBRL allows this flexibility to reporting companies, it is up to regulators to decide whether to impose rules about extensions. In line with the Anglo-American emphasis on providing a true and fair view in reports the U.S. SEC allows companies to extend the taxonomy as do most other jurisdictions currently using it for regulatory reporting (SEC, 2009).

While there are important technological differences between the two standards, they occupy a common domain. XBRL initially consisted of two identifiable developments, XBRL FR and XBRL GL. The GL or ‘global ledger’ taxonomy is pitched at the journal level. That is, not for transactions between entities, but for recording transactions in an individual entity’s accounting system. The FR taxonomies are designed for ‘financial reporting’ to users external to the entity. EDIFACT’s focus is on transactions between entities, but it provides a basis for communicating journal level data and so overlaps with XBRL GL. EDIFACT also permits electronic declarations such as financial statements, in common with XBRL FR. The overlap between these domains creates a basis for competition or cooperation (Hamscher, 2002).

## Cooperation or competition between the two programs?

Both standards have significant resources invested in them, as well as the commitment of dedicated individuals. The XBRL consortium is more advanced in the application of XML and UN/EDIFACT has the legitimacy and strength of an accepted (CEFACT) modeling approach to business concepts.

‘The first component (of UN/EDIFACT standard) – data elements and codes – is UN/EDIFACT’s core expertise; no other organisation worldwide can claim the same level of expertise in attributing definitions to business data. (y) It is crucial that investment in UN/CEFACT data definitions is protected.’ (UN/EDIFACT Working Group, 2001, Point 4, p. 2)

A meeting of a representative of EDIFICAS and two people from XBRL on 19 December 2000 identified 10 benefits of collaboration. These included from the point of view of EDIFICAS, extending existing EDIFICAS standards outside of Europe and gaining the experience of XML already present in the XBRL consortium. Benefits for XBRL included access to the French market and links to the UN, as well as the creation of a bridge between UN/EDIFACT and XBRL. The minutes also indicated that:

Failing to achieve an agreement would lead to the existence of two competitive standards in some part of the world y a window of opportunity clearly exist today for the two organisations to collaborate. This window of opportunity will not last for long. (Minutes of meeting, December 19, 2000)

Several efforts at engagement were made; all with limited success (see, for example, reports of the 14th and 15th UN/ CEFACT forums available at www.edificas.eu). In this section, we identify the critical interrelated barriers that laid the foundation for conflict rather than collaboration.

## ‘EDI is dead’

One source of conflict was that the concept of ‘EDI’ that was interpreted as simply a generic reference EDI, which would include XML standards by members of EDIFICAS, but was cast as ‘old technology’ superseded by XML in the XBRL camp.

Visibly, my presentation [to the XBRL representatives] was not appreciated at all for the reason that I was referring to ‘[electronic] data interchange’ and [XBRL participant] stated urbi et orbi ‘EDI is dead!’ (EDev3 email)

EDIFACT is an old language. At the beginning XML wasn’t there. (XDev3)

The misunderstanding reflected in these quotes suggests that participant’s attitudes rather than insurmountable technological differences stymied discussion. Indeed, the network of actors and technologies engaged in developing EDIFACT also embraced XML and is active in developing ebXML in conjunction with OASIS (Choi et al, 2009).

![](/api/attachments/7WM2URY5/fulltext/images/3edc533af7446762b89e1e100c5c828044605b96be3881c2cb2555fbe1a43965.jpg)  
Figure 5 Semantic technology basis and the development of ebXML.

## Preserving the messages: scarce resources

XML does pose a challenge to the EDIFACT network (see Point D on the Figure 2 and Table 1):

y EWG faced some major challenges during the past year y . But, more significant is the emergence of a new syntax, XML. (UN/EDIFACT Working Group, 2001, Point 3, p. 2)

The challenge is not, however, because the new ‘syntax’ is fundamentally different to EDI. The concern is to ensure that the model and concepts at the core of the EDIFACT standard are preserved:

y we have to start the production of a new directory of electronic transactions using the new syntax, XML [i.e. ebXML]. But this new set of e-transactions must be based on the data principles in which ‘collectively, hundreds of person-years of investment effort are encapsulated’ (UN/ CEFACT’S strategy for electronic business). (UN/EDIFACT Working Group, 2001, Point 6, p. 2)

This requires securing the scarce resources needed to maintain the EDIFACT directory and work on ebXML. So another explanation for the lack of interest in working with XBRL was the lack of resources to do both:

We [TBG12] had already indicated during the Roma Forum, that we had neither the time nor the resources to create a bridge between XBRL Ledger and Accounting Ledger of ebXML. (15th UN/CEFACT Forum – Sept–Oct 2009 http:// www.edificas.eu/index.php/eng/Working-group)

The relationship between the three standards is shown in Figure 5. The transfer of the effort invested in developing the model of business messages from the EDI standard into XML in the form of ebXML is highlighted.

## Accounting differences in the antecedent networks

There is an important difference between the Anglo-American accounting approach underlying IFRS and the fiscal emphasis and standardized chart of accounts in France. XBRL’s approach to reporting is based on the flexible, principles-based reporting of financial statements in accord with the IFRS’s ‘true and fair’ view. The French standard chart of accounts focuses on the consistent reporting of fiscal facts based on ledger account balances, and so does EDIFACT. This is a subtle difference to non-accountants, but its importance to the XBRL development is reflected in the separation of the ‘internal’ ledger accounts (GL) from the external reporting (FR). The French approach would see no need for this distinction because the French view reports generated from the standard chart of accounts to be representative or equivalent to ‘true and fair’ (Chiapello, 2005; Nobes & Parker, 2006, p. 302).

[XBRL] needs work because XBRL is not used in a heterogeneous environment. The Anglo-Saxon environment does not cover the whole cycle in French fiscality. The IFRS system is limited for the current French accountancy model. (EDev2)

XBRL is a top down approach. It uses the audit sector logic. EDIFICAS has a bottom up approach, that is, do the book keeping, conception of the balance sheets, etc y (EDev1)

This fundamental accounting difference combined with the American genesis of the XBRL consortium provokes French resistance to XBRL and a preference for local standards.

## Legitimacy in standard setting

The development of EDIFACT relied on building support through EDFICAS, EDIFRANCE and UN/CEFACT. The initiative that lead to the development of XBRL came in 1999 from an accountant, Charlie Hoffman, and the American Institute of Chartered Accountants (the equivalent of France’s l’Ordre des Experts-Comptables) (Kernan, 2009). The proponents of XBRL created a purposefully international framework with national jurisdictions and requiring substantial fees for membership (Locke & Lowe, 2007). However, it did not conform to the requirements of supra-national standard setting bodies such as the UN or ISO, preferring the potential for speed based on a market-oriented approach to product development.

The United Nations are an old bureaucracy which does not correspond any more to the constraints of today. We can not wait many years as for EDIFACT project; we (i.e. XBRL group) aim for effectiveness and quickness. (XAcc1)

This difference contributes to a negative perception of the XBRL effort in France, however:

A standardisation process is not a Euro pudding! If sectors must converge – it means long-term. If there is no norm, each IT services company would seek to ‘sell’ their de facto standard. With EDIFACT all is free! This XBRL standard is not serious. (EAuth1)

While the XML and EDI technologies themselves are different, they do not themselves make cooperation between the standard setters impossible. A central issue in the failure to collaborate is the contrasting priorities and understanding of legitimacy between XBRL’s market-driven consortium and EDIFACT’s institutionalized formalization. In addition, XBRL participants’ attitudes to EDI, EDIFACT’s commitment of resources to ebXML, and the antecedent accounting methodologies combined to derail these tentative efforts.

Encroachment of the anti-program: empty spaces The XBRL consortium and the IASC Foundation XBRL team have been involved in a project to create an XBRL platform to provide the Committee of European Banking Supervisors (CEBS) with a standardized format for collecting data from regulated national jurisdictions (the COREP and FINREP projects, see www.XBRL.org). Figure 2 shows the line tracing the network of the EDIFACT program being pushed to the left because of the adoption of XBRL by regulatory bodies including Infogreffe and European banking regulators (see Point E on Figure 2). But the ceding of this territory is not identified as a threat by one interviewee:

EDIFACT has proved its competence in transport in transactions and commercial operations. EDIFACT has nothing to prove. XBRL should have a position elsewhere. Nature detests empty space! Between the banks and the banking commission, there was nothing. XBRL can take its place in this space. (EDev1)

On the XBRL side – the potential is seen as far greater, however:

Authorities like ‘Banque National de Belgique’ will decide like in Belgium that you have no choice, XBRL must be used, and everybody will follow the trend! It is not a question any more of knowing if it will be used, but when it will be imposed by the French institutions. (XAcc1)

It is estimated by XBRL France that 650 banks in France are involved in reporting to CEBS using XBRL.

The push for pan-European systems of reporting to support a single market has been used to argue that XBRL is congruent with the interim step of a ‘unified reporting approach’ in member states (Le´picier, 2008). It is also claimed that XBRL has the support of the European Parliament (Colgren, 2008; Le´picier, 2008). It should be noted, however, that the European Parliament Opinion on simplified business environment (22 January 2008) promotes the use of new technology and only gives XBRL as an example rather than directly recommending its use. XBRL is moving into the spaces that are made available by the European changes and there are two projects being developed using XBRL tagging as the basis for data exchange with a regulator in France in addition to CEBS’ European banking projects. One is the Infogreffe project for the filing of financial reports with the registrant’s office and the other is Euronext for the submission of prospectuses (Le´picier, 2008).

It may be argued that XBRL adoption in applications not using EDIFACT does not push back the boundary as shown at Point E in Figure 2. Despite a government recommendation to adopt XML in 2002, French regulators have adopted a 'practical' approach and have been reluctant to replace systems that work well. This is the strength of an incumbent standard in a network.

EDI works well with the income tax services. When nothing exists, we are open to XML which is more flexible. We evaluate as well the necessary budget to the implementation of a language. We don’t want for example to finance IS [information system] consultancy firm if they invent a new language. This would lead to a proliferation of all sorts of languages. We are not pro or con XBRL. We know for example the portal jedeclare.com works well with EDIFI-CAS. (Reg1)

However, as XBRL builds its network among regulators it seems likely that resources such as accounting and IT expertise, devoted to establishing the XBRL systems will be denied to EDIFACT. It may take a long time, perhaps even 20 years (EDev2) for EDIFACT to be replaced. There are many open questions in this unfinished battle. One is that whether the beliefs inscribed in the EDIFACT project and transferred to ebXML will move into the reporting domain currently dominated by XBRL outside France. Another is that whether XBRL will become the incumbent standard in regulatory reporting in France. Alternatively, perhaps XBRL and EDIFACT could converge y?

We do not need XBRL to have the capacity to move forward y In the past we can mention examples of projects that were distant from EDIFACT. See the beginning of [project name] in large volume distribution. It ended in an alignment with EDIFACT! It will be the same with XBRL. (EAuth1)

## Findings

We have used Latour’s (1992) translation map to provide a visual representation of the key gains and losses to the competing networks in the battle between EDIFACT and the challenger XBRL (Figure 2). The setting is tense as European governments seek ways to achieve transparency and improved regulatory surveillance while being careful not to overburden already stressed businesses (Schmerken, 2007; Financial Stability Board, 2009).

We identify three interrelated factors that are important to the future of business ICT standards adoption in France and internationally. These are: the impact of regulators as the main adopters of business data standards; the important role of pre-existing networks in the development of the standards; and the choice between speed and legitimacy in the governance of the development project. Finally, we discuss the contribution of the paper to the application of ANT in the standards battle literature.

## Regulators as adopters

Tracing the network of allies for EDIFACT and XBRL in France shows the heavy reliance on regulators for diffusing the standard. This is in part a result of the nature of the underlying program – to obtain information from businesses for taxation and accountability purposes. Some proponents initially believed that companies would voluntarily adopt XBRL to enhance information for investors, but it became apparent that only regulators had a clear business case for adoption and businesses would not volunteer to be accountable (Locke & Lowe, 2007). Similarly, the early years in the development of EDIFACT also owe a great deal to promotion by key political figures, EC funding and alliances with regulators as adopters of the standard.

A feature of regulator adoption is that it creates a form of ‘lock in’ that is not otherwise present in open standards (Oshri et al, 2010). In an open and interoperable environment, entities can more easily adopt new standards as they become available and so the risk to a de facto incumbent standard from competitors is higher. EDIFACT’s position as a de jure standard in the jedeclare.com portal is important because it has been protected from challenge in that application for many years and will be for many into the future, as identified by interviewees from both standards (see ‘Encroachment section).

The credit crisis and recession has created a climate in which regulators are under pressure to demonstrate that they are taking positive steps to resolve both the current problems and address weak financial market structures (Financial Stability Board, 2009; Hutton, 2010; Vina, 2010). Our case analysis suggests that this may provide an opportunity for the ‘new’ XBRL standard to be presented as a better ‘solution’, than the incumbent standard, for improved regulation (Moyer, 2008; Bolgiano, 2009). The rhetoric surrounding XBRL focuses on it being the latest technology – the new solution – sometimes very colorfully:

Sincerely and being objective – if France does not implement XBRL, France will be an underdeveloped country! It’s like condoms and AIDS y Condoms are not always used and chosen but in reality, there is no other possibility. France should not miss this opportunity. (XDev1)

By distinguishing itself from the existing ‘failed’ business reporting infrastructure the proponents of XBRL at least have an argument with which to open up the discussion with regulators about the existing framework of business reporting standards in France and potentially ‘unlock’ the incumbent’s position.

The challenger may also move into spaces not occupied by the incumbent. Our case study shows that XBRL has been adopted by the European banking regulators and others not currently using EDIFACT. These adoptions give the challenger a basis on which to build the networks necessary to be in a stronger position to offer an attractive alternative for applications currently ‘occupied’ by the incumbent.

Researchers have suggested that competition between standards is justified, despite the duplication of resources, because it may encourage innovation and reduce the cost to the final user (Oksala et al, 1996; Egyedi & Koppenhol, 2010). Conclusions are mixed and vary depending whether the standard is de facto or de jure (Egyedi & Koppenhol, 2010). While EDIFACT and XBRL are open standards,

EDIFACT relies on a formal UN-backed system while XBRL is a private consortium. While both could become de facto standards through widespread adoption, we have shown the importance of regulator mandation for their diffusion (see also, Locke & Lowe, 2007). This effectively makes them de jure standards in these settings and suggests in line with Egyedi & Koppenhol’s (2010) analysis, that competition may not provide significant benefits.

## The role of existing networks

A practical concern in conducting ANT research is where to draw the boundaries of the network (Latour, 1987; Miller, 1997). In our study, we commence the translation diagram with the basic program of governments to collect business data for regulatory purposes. We have focused on two data standards, but in doing so, the importance of the broader context of pre-existing networks, systems and standards, government policies and culture are highlighted (see Chae & Poole, 2005 at the organizational level; see also, Gro¨tnes, 2008).

The importance of these pre-existing conditions is that EDIFACT developed in France before XML was available precisely because the conditions in France were amenable to a standardized, electronic approach to reporting to government. The existence of a national standardized chart of accounts (the Plan Comptable Ge´ne´ral) and the social acceptance of economic and social regulation by the state (dirigisme) contrast strongly with the U.S. ‘free market’ context for the later development of XBRL.

Similarly, the attraction of the UN/CEFACT structure for providing legitimacy for EDIFACT, as opposed to XBRL’s emphasis on a fast-paced market model, is traced to the translation of the antecedent networks. The close link between the structure of the EDIFACT messages and the regulatory requirements of key adopters in France lead to an impression of the standard as being ‘rigorous’ but inflexible, while the extensibility of XML was a ‘good fit’ for the ‘western’ accounting model of true and fair representation, but was depicted as lacking ‘rigor’. These are examples of the gains and compromises made by the standards in building on the strength of existing networks that also laid the foundation for irreconcilable differences between them. Even though each group recognized that they could gain from cooperation and that there was a limited time frame in which to commence the work, the fledgling cooperation faltered because of the attitudes deeply entrenched in the networks. Understanding the importance of the bricolage from which the standards emerge, helps to explain the tendency to competition and perhaps even battles between standards at the international level.

## Speed vs legitimacy in network building

The existing networks are argued to have lead to the emergence of the two contrasting attitudes to speed and legitimacy. XBRL’s private consortium emphasized speed, whereas EDIFACT’s developers favored legitimacy and consensus through a formal. institutionalized structure (see, for example, XBRL France, 2005; but compare Cox, 2008).

The tension between speed and legitimacy in standard setting has been discussed in the literature (de Vries, 1999; Rada, 2000; Boh et al, 2007). We highlight how these tensions may be related to the location of the core standard setting effort and how they emerged as an issue in the resistance to cooperation between the two standards setting groups. It is interesting to note that the XBRL consortium is now undertaking a modeling exercise using the Unified Modelling Language to enhance the wider usability of the standard (XBRL International Standards Board, 2010); something which EDIFICAT proponents argue should be the foundation rather than an ‘after-thought’.

Since it may not be the technically ‘best’ standard that achieves dominance in a domain (Hanseth, 2001; Suarez, 2004), and we have observed the importance of early regulator adoptions to achieve ‘lock in’, it may be that speed will be the greater determinant of achieving critical mass and therefore survival of a standard. In our case, EDIFACT emerged earlier than XBRL, which gave it the advantage. A key factor in the future may be whether or not regulators are prepared to take the time to engage with the development of ‘technically better’ standards or if they respond public demands to ‘do something’ in the short term.

Our study of the battle between EDIFACT and XBRL has highlighted the importance of the ‘location’ of the projects in existing networks and how the networks are expanded and compromises made using technologies as allies, as well as recruiting other participants and especially in this case regulators. The choice of governance system impacts on the speed of the development and given the importance of early adoption and ‘lock in’, proponents wishing to take advantage of favorable external conditions for adoption (such as a crisis or other disruption to the incumbent) could find that speed is more advantageous than legitimacy. The lack of clear benefits from competition between standards suggests that regulators and developers would achieve net benefits by encouraging early collaboration.

## ANT’s contribution to business standards research

ANT highlights the way in which technologies continuously emerge from the shifting assemblages of networks of actors and actants. Latour’s (1992) translation map (Figure 2) and the case description that accompanies it emphasize the key events and their effect on the boundary between the program and anti-program. We found it a useful device for sensitizing the researcher to ways to interpret movement in the network of alliances and progress of the programs at the ‘battle front’. It disciplines the researcher to consider not only the additions to the network, but also the detours and substitutions made as the conflict unfolds.

Our analysis suggests that intensive case research provides a valuable alternative perspective to that obtained through extensive quantitative work. For example, Blind & Gauch (2008) categorize standard setters as using either formal or informal structures and conclude that there is a consolidation of activities through a reduction in the number of standard setters and that complementary activities are undertaken by the two types of organizations. In contrast, our research shows that the two structures may reflect entrenched differences that are very difficult to overcome to achieve collaboration.

It is important to adapt ANT into the IT literature carefully, maintaining its most fundamental epistemological and ontological tenets (Truex et al, 2006). We have been careful to ‘follow the object’ (Latour, 2005b) and the active controversy (cf Lee & Oh, 2006). This can lead the researcher in surprising directions. For example, in this study it became clear that the EDIFACT standard is embodied in a data modeling approach that is used to express a particular understanding of message structures for representing business events. This is the essential ‘kernel’ of knowledge inscribed into the EDIFACT standard. So when XML emerged as a new technology, EDIFACT developers sought to preserve that kernel in XML in the form of ebXML (Figure 5). Despite the increased effort required to work in both EDI and XML, it is believed by the participants to be important to preserve their work. This suggests that there may be a deeper contention than that between EDIFACT and XBRL. The core representation of business facts, regardless of the technology in which they are operationalized, may be territory over which a longerterm battle has commenced.

The scope of this paper prevents us from also tracing the development of ebXML. However, our documentation of the early motivations of participants may be useful for future research. We also believe that an ANT approach and the observed importance of the ‘kernel’ suggests that researchers working with ICT standards may find it useful to consider whether or not the ‘data standard’ as defined by constituent groups or an acronym is the most fruitful level for analysis. It may be that it would be useful to trace the more fundamental kernel of structures and beliefs being inscribed in standards in future research.

## Conclusion

The standards battle between EDIFACT and XBRL in France has been analyzed using data from observation and interviews over a period of 5 years. The ANT perspective allows us to focus on how the battle unfolds over time as EDIFACT and XBRL are fabricated. We use Latour’s (1992) translation map to provide a visual

## About the authors

Ve´ronique Guilloux is an Assistant Professor in an international management department at UPEC (France). She is a researcher at Laboratoire d’Economie et Management representation of the standards battle in order to frame our analysis and order our evidence.

An implicit issue in research that focuses on standards battles is whether an incumbent standard may be successfully challenged. Our study finds that regulator adoption is important to diffuse business standards to users and achieve ‘lock in’ for an incumbent. EDIFACT is very stable and part of the infrastructure of fiscal reporting in France. However, the impact of the credit crisis on regulators has created an opportunity to challenge the existing reporting framework. The pressure to ‘do something’ to prevent such a similar crisis is strong and allows challengers to argue that the ‘newness’ of their ‘solution’ is valuable enough to warrant change. Problematizations (Latour & Woolgar, 1986; Latour, 1987, 2005a) of the financial crisis will continue to develop not only among regulators, but also among other groups such as the XBRL consortium who offer potential technology based ‘solutions’.

Battles among business standards also raise the question of whether or not it would be better to encourage collaboration than competition. The standards in our study are developed as open projects, but are reliant on regulator adoption and so become de jure standards. Since research suggests that there is less benefit from competition for de jure standards, we suggest that business standards developers would be best encouraged to collaborate early on to reduce the entrenched differences that develop with extensive networks. Regulators also have a role in engaging with business standards developers to avoid the emphasis on speed over legitimacy.

Future research will be able to look back on the developments of the next few years to trace the networks that emerge out of the economic crisis and the role of ebXML in carrying forward the effort invested in the message structures of EDIFACT. The importance of regulators as adopters of business reporting standards also may be explored in other settings along with the barriers to cooperation between international data standards developers.

## Acknowledgements

We would like to thank all the interview participants who gave their time to contribute to this research. The paper has benefited from the comments of participants at the 2008 ICIS Conference in Paris, the 2009 EGOS Colloquium, Barcelona and several local presentations. We would also especially like to thank Professor Peter Standish and this journal’s three anonymous reviewers.

Nantes-Atlantique (LEMNA). Her research interests are interorganizational systems and EDI. Ve´ronique is currently researching e-government with a special focus on virtualizing process. She has presented her work in international conferences ICIS, WITS and published IS articles in leading French journals including SIM, RAM.

Joanne Locke is a senior Lecturer in the Department of Accounting and Finance at the University of Birmingham (U.K.). Her research interest is in the global standardardization of business reporting. Joanne has completed projects on XBRL and ERP systems and published in journals including Organization, IT & People, Accounting

## References

AKRICH M and LATOUR B (1992) A summary of a convenient vocabulary for the semiotics of human and nonhuman assemblies. In Shaping Technology/Building Society: Studies in Sociotechnical Change (B WE and LAW J, Eds), pp 259–264, MIT Press, Cambridge, MA.

ARCHAEON (2004) European trusteeship forum winners. [WWW document] http://avallone.archaeon.co.uk/?p ¼ news201004.uk (accessed January 2008).

ARTHUR B (1989) Competing technologies, increasing returns, and lock-in by historical events. The Economic Journal 99(394), 116–131.

BACKHOUSE J, HSU CW and SILVA L (2006) Circuits of power in creating de jure standards: shaping an international information systems security standard. MIS Quarterly 30(Supplement), 413–438.

BLIND K and GAUCH S (2008) Trends in ICT standards: the relationship between European standardisation bodies and standards consortia. Telecommunications Policy 32(7), 503–513.

B BP and V T (1997) Visions of organization and organizations of vision: The representational practices of information systems development. Accounting, Organizations and Society 22(7), 639–668.

BOH WF, SOH C and YEOH S (2007) Standards development and diffusion: a case study of RosettaNet. Communications of the ACM 50(12), 57–62.

BOLGIANO M (2009) Using standards for transparency. XBRL US Testimony to the Domestic Policy Subcommittee: Oversight and Government Reform Committee. [WWW document] http://xbrl.us/documents/XBRL\_US\_ Testimony.pdf (accessed April 2009).

BONACCORSI A and ROSSI C (2003) Why open source software can succeed. Research Policy 32(7), 1243–1258.

BORRAS J (2004) International technical standards for e-government. Electronic journal of e-government 2(2), 75–80.

CALLON M (1986) Some elements of a sociology of translation: domestication of the scallops and the fishermen of St Brieuc Bay. In Power, Action and Belief: A New Sociology of Knowledge? (LAW J, Ed.), pp 196–233, Routledge and Kegan Paul, London.

CAMP J and VINCENT C (2004) Setting standards: looking to the internet for models of governance. Ethics and Information Technology 6(3), 161-173.

CHAE B and POOLE MS (2005) The surface of emergence in systems development: agency, institutions, and large-scale information systems. European Journal of Information Systems 14(1), 19–36.

CHANG C and JARVENPAA S (2005) Pace of information systems standards development and implementation: the case of XBRL. Electronic Markets 15(4). 365–377.

CHIAPELLO E (2005) Les normes comptables comme institution du capitalisme. Une analyse du passage aux normes IFRS en Europe a\` partir de 2005. Sociologie du travail 47(3), 362–382.

CHOI B, RAGHU TS and VINCE A (2004) Addressing a standards creation process: a focus on ebXML. International Journal of Human-Computer Studies 61(5).627–648

C B, R TS, V A and D KJ (2009) Process model for e-business standards development: a case of ebXML standards. IEEE Transactions on Engineering Management 56(3), 448–467.

CIBORRA CU, BRAA K, CORDELLA A, DAHLBOM B, FAILLA A, HANSETH O, HEPSø V, L J, M E and S KA (2001) From Control to

Organizations and Society, European Accounting Review and Critical Perspectives on Accounting.

Alan Lowe is a Professor of accounting at Aston Business School (U.K.). His research interests include management accounting systems change, ERP and Casemix systems, financial reporting, transparency and accountability and qualitative research methodologies. He has published in journals including Management Accounting Research, Organization Studies, Organization, and Accounting, Auditing and Accountability Journal.

Drift: The Dynamics of Corporate Information Infrastructures. Oxford University Press, Oxford.

COFFIN Z (2000) XBRL liaison report. [WWW document] http://www .juergendaum.com/news/XBRL-LiaisonReport-International-20001016 .doc (accessed March 2005).

COLASSE B and STANDISH P (1998) State versus market: contending interests in the struggle to control French accounting standardisation. Journal of Management and Governance 2(2), 107–147.

COLGREN TD (2008) XBRL international appoints Gilles Maguet as secretary general of XBRL Europe. Business Wire. [WWW document] http://www.reuters.com/article/pressRelease/idUS130780+27-May-2008+BW20080527 (accessed June 2009).

COX C (2008) Speech by SEC Chairman Christopher Cox: address to the 17th XBRL International Conference. [WWW document] http://www .sec.gov/news/speech/2008/spch050708cc-2.htm (accessed June 2008).

D J and T D (2000) Binary trading relations and the limits of EDI standards: the Procrustean bed of standards. European Journal of Information Systems 9(3), 173–188.

D PA (1985) Clio and the economics of QWERTY. American Economic Review 75(2), 332–337.

DAVID PA and GREENSTEIN S (1990) The economics of compatibility standards: an introduction to recent research. The Economics of Innovations and New Technology 1(1/2), 3–41.

DECHOW N and MOURITSEN J (2005) Enterprise resource planning systems, management control and the quest for integration. Accounting, Organizations and Society 30(7–8), 691–733.

DE VRIES HJ (1999) Standardization: A Business Approach to the Role of National Standardization Organizations. Kluwer, Boston.

DE VRIES H, DE VRIES HJ and OSHRI I (2008) Standards Battles in Open Source Software: The Case of Firefox. Palgrave and Macmillan, NY.

EGYEDI TM and KOPPENHOL A (2010) The standards war between ODF and OOXML: or, does competition between overlapping ISO standards lead to innovation? International Journal of IT Standards and Standardization Research 8(1), 49–62.

EUROPEAN COMMISSION (2009) The EU single market. [WWW document] http://ec.europa.eu/internal\_market/accounting/legal\_framework/index\_ en.htm (accessed August 2010).

EUROPEAN PARLIAMENT (2009) Text adopted: community programme for financial services financial reporting and auditing P6\_TA-PROV (2009)0368. [WWW document] http://www.europarl.europa.eu/ sides/getDoc.do?pubRef¼-//EP//TEXT+TA+P6-TA-2009-0368+0+DOC+ XML+V0//EN&language¼EN#BKMD-37 (accessed May 2010).

FINANCIAL STABILITY BOARD (2009) Financial stability board reports on improving financial regulation. [WWW document] http://www .financialstabilityboard.org (accessed May 2010).

FOCUS PCG (2009) Comprendre le plan comptable Franc¸ais et son e´volution. [WWW document] http://www.focuspcg.com/ (accessed September 2010).

FOUQUIE\`RES DE L-A and STOL H (1999) TELER: lowering the burden entailed by enterprises’ data collection. [WWW document] http://europa .eu.int/en/comm/eurostat/re-search/dosis/teler/ (accessed November 2009).

GARUD R, JAIN S and KUMARASWAMY A (2002) Institutional entrepreneurship in the sponsorship of common technological standards: the

case of Sun Microsystems and Java. Academy of Management Journal 45(1), 196–214.

GARUD R and KUMARASWAMY A (1993) Changing competitive dynamics in network industries: an exploration of Sun Microsystems’ open systems strategy. Strategic Management Journal 14(5), 351–369.

GENDRON Y and BARRETT M (2004) Professionalization in action: accountants’ attempt at building a network of support for the WebTrust seal of assurance. Contemporary Accounting Research 21(3), 563–602.

GRAHAM I, SPINARDI G, WILLIAMS R and WEBSTER J (1995) The dynamics of EDI standards development. Technology Analysis & Strategic Management 7(1), 3–20.

GRo¨TNES E (2008) The work of an international standardization consortia: paths towards its current structure. International Journal of IT Standards and Standardization Research 7(1), 48–65.

GUILLOUX V (2010) Comment le <sup>)</sup>texte<sup>\*</sup> peut mettre en lumie\`re les infrastructures SIO en XML et en EDI? Un exemple dans le secteur financier. Management & Avenir 9(n139), 250–264.

HAMSCHER W (2002) XBRL and its adjacent XML languages: An overview. [WWW document] http://www.standardadvantage.com/ Docs/XBRL-Adjacent-Specs-2002-05-27.pdf (accessed August 2005).

HANSETH O (2001) The economics of standards. In From Control to Drift: The Dynamics of Corporate Information Infrastructures (CIBORRA CU, BRAA K, CORDELLA A, DAHLBOM B, FAILLA A, HANSETH O, HEPSØ V, LJUNGBERG J, M E and S KA, Eds), pp 56–70, Oxford University Press, Oxford.

HANSETH O, AANESTAD M and BERG M (2004) Guest editors’ introduction: actor-network theory and information systems. What’s so special? Information Technology and People 17(2), 116–123.

HANSETH O, JACUCCI E, GRISOT M and AANESTAD M (2006) Reflexive standardization. Side-effects and complexity in standard-making. MIS Quarterly 30(Special Issue), 563–581.

HANSETH O and MONTEIRO E (1997) Inscribing behaviour in information infrastructure standards. Accounting, Management and Information Technologies 7(4), 183–211.

HAWSER A (2004) Turf war rages over electronic payments. Global Finance. [WWW document] http://findarticles.com/p/articles/mi\_qa3715/ is\_200410/ai\_n9417474 (accessed August 2008).

HEEKS R and STANFORTH C (2007) Understanding e-government project trajectories from an actor-network perspective. European Journal of Information Systems 16(2), 165–177.

HEMETSBERGER A and REINHARDT C (2009) Collective development in opensource communities: an activity theoretical perspective on successful online collaboration. Organization Studies 30(9), 987–1008.

HUTTON W (2010) Now we know the truth. The financial meltdown wasn’t a mistake – it was a con. The Observer. Sunday, 18 April, http:// www.guardian.co.uk/business/2010/apr/18/goldman-sachs-regulatorscivil-charges (accessed May 2011).

JAKOBS K (2000) Information Technology Standards and Standardization: A Global Perspective. Idea Group Publishing, London.

KATZ M and SHAPIRO C (1985) Network externalities, competition, and compatibility. American Economic Review 75(3), 424–440.

KEOGH J and DAVIDSON K (2005) XML Demystified. McGraw-Hill, NY.

KERNAN K (2008) XBRL around the world. Journal of Accountancy 206(4), 62–66.

KERNAN K (2009) The story of our new language: personalities, cultures, and politics combine to create a common, global language for business. [WWW document] http://www.aicpa.org/Professional+ Resources/Accounting+and+Auditing/BRAAS/downloads/XBRL\_09\_ web\_final.pdf (accessed June 2010).

LA DOCUMENTATION FRANc¸AISE (2009) La modernisation de l’Etat. [WWW document] http://www.ladocumentationfrancaise.fr/dossiers/ modernisation-etat/index.shtml (accessed May 2010).

LATOUR B (1987) Science in Action: How to Follow Scientists and Engineers Through Society. Harvard University Press, Cambridge, MA.

LATOUR B (1991) Technology is society made durable. In A Sociology of Monsters. Essays on Power, Technology and Domination (LAW J, Ed.), pp 103–131, Routledge, London.

LATOUR B (1992) Where are the missing masses? The sociology of a few mundane artifacts. In Shaping Technology/Building Society: Studies in Sociotechnical Change (BIJKER WE and LAW J, Eds), pp 225–258, MIT Press, Cambridge, MA.

LATOUR B (1994) On technical mediation – philosophy, sociology, genealogy. Common Knowledge 3(2), 29–64.

LATOUR B (1996) Aramis: Or the Love of Technology. Harvester Wheatsheaf, Brighton.

LATOUR B (1999) On recalling ANT. In Actor Network Theory and After (LAW J and HASSARD J, Eds), pp 15–25, Blackwell, Oxford.

LATOUR B (2005a) From Realpolitik to Dingpolitik: how to make things public. An introduction. In Making Things Public. Atmospheres of Democracy (LATOUR B and WEIBEL P, Eds), pp 1–31, MIT Press, Cambridge, MA.

LATOUR B (2005b) Reassembling the Social: An Introduction to Actor-Network-Theory. Oxford University Press, Oxford.

LATOUR B and WOOLGAR S (1986) Laboratory Life: The Construction of Scientific Facts. Princeton University Press, Princeton, NJ.

LAW J (1992) Notes on the theory of the actor-network: ordering, strategy, and heterogeneity. Systems Practice 5(4), 379–393.

LAW J (2000) Objects, spaces, others. Society and Space 18(3), 127–132.

LAW J (2002) Objects and spaces. Theory, Culture and Society 19(5/6), 91–105.

LAW J and CALLON M (1992) The life and death of an aircraft: a network analysis of technological change. In Shaping Technology/Building Society: Studies in Sociotechnical Change (BIJKER WE and LAW J, Eds), pp 21–52, MIT Press, Cambridge, MA.

LEE H and OH S (2006) A standards war waged by a developing country: understanding international standard setting from the actor-network perspective. Journal of Strategic Information Systems 15(3), 177–195.

Le´ S (2008) Transparency and regulated information. 17th XBRL International Conference. Evolution in Financial Reporting – XBRL in Action. Eindhoven, The Netherlands.

LOCKE J and LOWE A (2007) XBRL: an (open) source of enlightenment or disillusion? European Accounting Review 16(3), 585–623.

LYYTINEN K, KEIL T and FOMIN V (2008) A framework to build process theories of anticipatory information and communication standardizing. International lournal of IT Standards and Standardization Research 6(1), 1–38.

MCGRATH K (2002) The golden circle: a way of arguing and acting about technology in the London ambulance service. European Journal of Information Systems 11(4), 251–266.

MILLER P (1997) The multiplying machine. Accounting Organizations and Society 22(3–4), 355–364.

MOYER P (2008) XBRL: a magic pill? California CPA Magazine. [WWW document] http://www.calcpa.org/Content/25346.aspx (accessed December 2008).

NICKERSON JV and ZUR MUEHLEN M (2006) The ecology of standards processes: insights from internet standard making. MIS Quarterly 30(Supplement), 467–488.

NOBES CW and PARKER RH (2006) Comparative International Accounting. Pearson Education, Harlow, UK.

O S, R A, S M and O<sup>0</sup>D J (1996) The structure of IT standardization. StandardView 4(1), 9–22.

O I, D V HJ and D V H (2010) The rise of Firefox in the web browser industry: the role of open source in setting standards. Business History 52(5), 834–856.

PFEIFFER H (1992) The Diffusion of EDI. Physica, Heidelberg.

POTTER JA and COHEN S (2010) Information sharing strategies in a standards contest: the case of 2G wireless communication. Journal of High Technology Management Research 21(2), 108–121.

Q P and H T (2005) A ‘time-space odyssey’: management control systems in two multinational organisations. Accounting, Organizations and Society 30(7–8), 735–764.

RADA R (2000) Consensus versus speed. In Information Technology Standards and Standardization: A Global Perspective (JACOBS K, Ed.), pp 19–34, Idea Group Publishing, London.

RAMIREZ C (2008) Exporting professional models: the expansion of the multinational audit firm and the transformation of the French accountancy profession since 1970. Critical Perspectives on Accounting Conference. New York.

ROSENBLOOM R and CUSUMANO M (1987) Technological pioneering and competitive advantage: the birth of the VCR industry. California Management Review 29(4), 51–76.

ROTH D (2009) Road map for financial recovery: radical transparency now! Wired. [WWW document] http://www.wired.com/techbiz/it/

magazine/17-03/wp\_reboot?currentPage=all (accessed December 2009).

SCHEIER RL (2003) XML gets organized. Computerworld 37(43), 30–31.

SCHILLING MA (1998) Technological lockout: an integrative model of the economic and strategic factors driving technological success and failure. Academy of Management Review 23(2), 267–284.

SCHMERKEN I (2007) Credit crisis in sub-prime mortgages affects hedge funds trading in other asset classes. Advanced Trading. [WWW document] http://www.advancedtrading.com/issues/200710/show Article.jhtml?articleID¼201805585 (accessed June 2009).

SEC (2009) Interactive data to improve financial reporting: final rule. [WWW document] http://www.sec.gov/rules/final/2009/33-9002.pdf (accessed February 2009).

SHAPIRO C and VARIAN HR (1999a) The art of standard wars. California Management Review 41(2), 8–32.

SHAPIRO C and VARIAN HR (1999b) Information Rules: A Strategic Guide to the Network Economy. Harvard Business School Press, Boston, MA.

SLIWA C (2000) Bloated file size an issue for XML. Computerworld, 8 May.

STANDARD BUSINESS REPORTING (2009) An Australian government initiative: standard business reporting. [WWW document] http://www.sbr .gov.au (accessed February 2010).

STANDISH P (1990) Origins of the plan comptable ge´ne´ral: a study in cultural intrusion and reaction. Accounting and Business Research 20(80), 337–351.

STANGO V (2004) The economics of standards wars. Review of Network Economics 3(1), 1–19.

STAR SL (1996) Working together: Symbolic interactionism, activity theory, and information systems. In Cognition and Communication at Work (ENGESTRO¨M Y and MIDDLETON D, Eds) pp 296–318, Cambridge University Press, Cambridge.

SUAREZ FF (2004) Battles for technological dominance: an integrative framework. Research Policy 33(2), 271–286.

SUAREZ FF (2005) Network effects revisited: the role of strong ties in technology selection. Academy of Management Journal 48(4), 710–720.

TBG12 (2005) UN/CEFACT business requirements specification version 1. [WWW document] http://www.google.co.uk/search?q=CEFACT%2 FForum%2F2005%2FTBG%2FBS002+&rls=com.microsoft:en-gb: IE-SearchBox&ie=UTF-8&oe=UTF-8&sourceid=ie7&rlz=1I7GGLD\_en& redir\_esc=&ei=0\_c8T6y9ONTp8QPTlNmnCA (accessed September 2010).

TRUEX D, HOLMSTRo¨M J and KEIL M (2006) Theorizing in information systems research: a reflexive analysis of the adaptation of theory in information systems research. Journal of the Association for Information Systems 7(1), Article 33 [WWW document] http://aisel.aisnet.org/jais/ vol7/iss1/33.

TUOMI I (2001) Internet, innovation, and open source: actors in the network. First Monday 6(1), [WWW document] http://www.firstmonday .org/issuess/issuess6\_1/tuomi/index.html.

TUROWSKI K (2000) Establishing standards for business components. In Information Technology Standards and Standardization: A Global Perspective (JAKOBS K, Ed.), pp 131–151, Idea Group Publishing, Hershey, PA.

UNCEFACT (1998) Centre for the facilitation of procedures and practices for administration. Commerce and Transport Meeting of Experts on Data Elements and Automatic Data Interchange (GE.1) Fifty-seventh session.

UN/CEFACT FORUM TBG12 (2001) Accounting and auditing domains: TBG12 terms of reference. [WWW document] http://www.uncefact forum.org/TBG/TBG12/TBG12%20Documents/TBG12\_Terms\_Of \_Reference\_Rev.7.doc (accessed December 2008).

UN/EDIFACT STEERING GROUP (1997) Report from the UN/EDIFACT Steering Group (ESG) Meeting Concord.

UN/EDIFACT WORKING GROUP (2001) Draft report of the UN/ EDIFACT working group (EWG) to the UN/CEFACT plenary of March 2001. [WWW document] http://www.unece.org/cefact/cf\_plenary/ plenary01/docs/01cf13.pdf (accessed December 2009).

VAN OOSTERHOUT M, WAARTS E and VAN HILLEGERSBERG J (2006) Change factors requiring agility and implications for IT. European Journal of Information Systems 15(2), 132–145.

V G (2010) U.K. scraps FSA, reversing system set up by brown (update2). Businessweek Online, 17 June. [WWW document] http:// www.businessweek.com/news/2010-06-17/u-k-scraps-fsa-reversingsystem-set-up-by-brown-update2-.html (accessed August 2010).

WEITZFL T. BEIMBORN D and KöNIG W (2006) A unified economic model of standard diffusion: the impact of standardization cost, network effects, and network topology. MIS Quarterly 30(Supplement), 489–514.

WINDRUM P (2004) Leveraging technological externalities in complex technologies: microsoft’s exploitation of standards in the browser wars. Research Policy 33(3), 385–394.

XBRL FRANCE (2005) Communique´ de presse: reporting et publication d’informations financie\`res. [WWW document] http://www.xbrl.org/fr/ Presse/Communique\_cr%C3%A9ation\_XBRL\_11\_05\_05.pdf (accessed December 2010).

XBRL INTERNATIONAL STANDARDS BOARD (2010) XBRL: towards a diverse ecosystem. Discussion paper. [WWW document] http:// www.xbrl.org/2010TechDiscussion/2010TechDiscussion.pdf (accessed December 2010).

ZHU K, KRAEMER KL, GURBAXANI V and XIN XUS (2006) Migration to open-standard interorganizational systems: network effects, switching costs, and path dependency. MIS Quarterly 30(Supplement), 515–539.

Z A (1999) Standards battles heat up between United States and European Union. Quality Progress 32(1), 39–42.

## A<sub>pp</sub>endix

A<sub>ppe</sub>nd i<sub>x</sub> – d<sub>a</sub>t<sub>a</sub> <sub>co</sub>l l<sub>ec</sub>ti<sub>o</sub>n

T<sub>a</sub>bl<sub>e</sub> A1 I nterviews

<table><tr><td>Date</td><td>Code</td><td>Organization (s)</td><td>Role</td><td>Perspective</td><td>Type</td><td>Duration (approximately)</td></tr><tr><td>18 November 2005</td><td>XUser1</td><td>Credit insurance company/XBRL France</td><td>Senior manager</td><td>User of company credit information/developer</td><td>F2F</td><td>1 h</td></tr><tr><td>15 December 2005</td><td>XUser2</td><td>Credit agency/XBRL France</td><td>Group director/working group member</td><td>Supplier of company credit information/developer</td><td>e-mail</td><td></td></tr><tr><td>14 January 2006</td><td>User3</td><td>Credit agency</td><td>Senior manager</td><td>Supplier of company credit information</td><td>e-mail</td><td></td></tr><tr><td>03 February 2006</td><td>XAcc1</td><td>Public accountancy firm/XBRL France</td><td>Partner/Senior member</td><td>Preparation of accounts/standard promoter</td><td>F2F</td><td>2 h</td></tr><tr><td>28 February 2006</td><td>EUser1</td><td>Edifrance</td><td>Delegate</td><td>EDI &#x27;think tank&#x27;</td><td>F2F</td><td>1 h</td></tr><tr><td>05 July 2006</td><td>EDev1</td><td>EDIFICAS/Conseil supérieur de l&#x27;Ordre des experts-comptables/TBG12</td><td>Accountant &amp; IT/senior role in standards bodies</td><td>Standards developer</td><td>F2F</td><td>1 h</td></tr><tr><td>05 July 2006</td><td>EDev2</td><td>EDIFICAS/Conseil Supérieur de l&#x27;Ordre des Experts Comptables/IS Department</td><td>Senior IT employee/member standards committee</td><td>Standards developer</td><td>Phone</td><td>2 h</td></tr><tr><td>12 July 2006</td><td>XDev1</td><td>Software consultant financial services sector/XBRL France</td><td>Software &amp; standards development</td><td>Software vendor</td><td>F2F</td><td>2 h</td></tr><tr><td>13 September 2006</td><td>Reg1</td><td>Direction Générale de la Modernisation De L&#x27;Etat – Ministère Des Finances (French Ministry of Finance)</td><td>Project leader</td><td>Regulator</td><td>F2F</td><td>1 h</td></tr><tr><td>10 October 2006</td><td>User4</td><td>Consultant in financial services sector</td><td>Consultant</td><td>User XBRL application</td><td>F2F</td><td>1 h</td></tr><tr><td>08 January 2007</td><td>XReg2</td><td>Banque de France/XBRL member</td><td>Senior management/Senior member</td><td>Regulator/developer</td><td>F2F</td><td>30 min</td></tr><tr><td>10 January 2007</td><td>User5</td><td>Fédération Bancaire Française</td><td>Senior manager</td><td>Professional body representing banks</td><td>F2F</td><td>1 h</td></tr><tr><td>31 May 2007</td><td>EDev3</td><td>EDIFICAS/TGB12/Accountant/IT</td><td>Senior developer</td><td>Developer</td><td>F2F</td><td>4 h</td></tr><tr><td>13 January 2008</td><td>EXDev1</td><td>Software vendor both EDIFACT and XBRL based</td><td>Senior manager</td><td>Software developer</td><td>F2F</td><td>3 h</td></tr><tr><td>21 February 2008</td><td>EDev2</td><td>As above</td><td></td><td></td><td>F2F</td><td>1 h</td></tr><tr><td>20 March 2008</td><td>XReg2</td><td>Infogreffe (greffes supervised by Ministère de la Justice)</td><td>Senior manager</td><td>Regulator/developer</td><td>F2F</td><td>2 h</td></tr></table>

Table A1 Conti n <sub>u</sub>ed

<table><tr><td>Date</td><td>Code</td><td>Organization (s)</td><td>Role</td><td>Perspective</td><td>Type</td><td>Duration (approximately)</td></tr><tr><td>01 April 2008</td><td>User6</td><td>Credit agency (same as for User3)</td><td>Senior Manager</td><td>Supplier of business information</td><td>F2F</td><td>1 h</td></tr><tr><td>01 April 2008</td><td>XDev2</td><td>Software vendor/XBRL France</td><td>Senior Manager</td><td>Vendor/developer</td><td>Phone</td><td>30 min</td></tr><tr><td>07 April 2008</td><td>Reg2</td><td>Institut National de la Propriété Industrielle (INPI – supervised by Ministère de l’Economie, des Finances et de l’Emploi)</td><td>Manager</td><td>Regulator</td><td>Phone</td><td>30 min</td></tr><tr><td>21 August 2008</td><td>Reg3</td><td>Institut National de la Propriété Industrielle (INPI – supervised by Ministère de l’Economie, des Finances et de l’Emploi)</td><td>Manager</td><td>Regulator</td><td>F2F</td><td>2 h</td></tr><tr><td>23 October 2008</td><td>EDev3</td><td>As above</td><td></td><td></td><td>e-mail</td><td></td></tr><tr><td>15 January 2009</td><td>Reg4</td><td>Direction Générale des Impôts (DGI)</td><td>Senior manager télé-procedures fiscales</td><td>Regulator</td><td>Phone</td><td>30 min</td></tr><tr><td>03 February 2009</td><td>XDev2</td><td>As above</td><td></td><td></td><td>F2F</td><td>2 h</td></tr><tr><td>13 March 2009</td><td>User7</td><td>Accountancy firm</td><td>Accountant</td><td>User</td><td>F2F</td><td>2 h</td></tr><tr><td>02 September 2009</td><td>User8</td><td>Bank</td><td>IT manager</td><td>User of company credit information</td><td>F2F</td><td>1 h</td></tr><tr><td>02 September 2009</td><td>User9</td><td>Bank</td><td>Information Manager</td><td>User of company credit information</td><td>F2F</td><td>2 h</td></tr><tr><td>13 November 2009</td><td>User10</td><td>Credit agency (same as for User3)</td><td>Senior manager</td><td>Supplier of company credit information</td><td>F2F</td><td>1 h</td></tr><tr><td>11 June 2010</td><td>XDev3</td><td>Software vendor/Accountant/XBRL France</td><td>Senior manager</td><td>Software developer</td><td>Phone</td><td>1 h</td></tr><tr><td>13 June 2010</td><td>EDev1</td><td>As above</td><td></td><td></td><td>F2F</td><td>45 min</td></tr></table>

Notes: Th e cod es fi rst i n d icate wh eth er th e pa rtici pa nt h ad a ny affi l iatio n to E D I FACT (E) o r X B RL(X) . Th e n ext pa rt of th e cod e i n d icates wh at is j u d g ed th e m ost i m po rta nt as pect of th ei r ro l e i n re l ati o n to th e n etwo rk M a n a rti ci a nts wi l l be use rs of th e sta n d a rds a n d d eve l o e rs fo r exa m l e Wh e re th ei r m aj o r ro l e is see n as d eve l o e r <sup>‘</sup> Dev<sup>’</sup> is i n d i cated a re u l ato r use r <sup>‘</sup> Re <sup>’</sup> o r <sup>‘</sup> Use r<sup>’</sup> Th <sub>e</sub> n <sub>u</sub> m b<sub>e</sub>r<sub>s a</sub> r<sub>e</sub> t<sub>o</sub> d i<sub>s</sub>ti n <sub>u</sub> i<sub>s</sub> h d iff<sub>e</sub>r<sub>e</sub>nt i n d ivid <sub>u a</sub> l<sub>s</sub> i n th <sub>e sa</sub> m <sub>e c</sub>l <sub>ass</sub>ifi<sub>ca</sub>ti<sub>o</sub> n Wh <sub>e</sub>r<sub>e a</sub> r<sub>e ea</sub>t <sub>co</sub> nt<sub>ac</sub>t i<sub>s</sub> m <sub>a</sub>d <sub>e</sub> with <sub>a</sub> n i n d ivid <sub>u a</sub> l th <sub>e co</sub>d <sub>e</sub> i<sub>s</sub> r<sub>e ea</sub>t<sub>e</sub>d with <sub>o u</sub>t th <sub>e</sub> f<sub>u</sub> l l d <sub>esc</sub>ri ti<sub>o</sub> n

Table A2 Conference and meeting observation

<table><tr><td>Date</td><td>Organizer and Location</td><td>Title</td><td>Duration</td></tr><tr><td>9–14 May 2004</td><td>XBRL International – Auckland New Zealand</td><td>9th XBRL International Conference</td><td>5 days</td></tr><tr><td>25–27 April 2005</td><td>XBRL International – Boston USA</td><td>11th XBRL International Conference</td><td>3 days</td></tr><tr><td>16–19 May 2006</td><td>XBRL International – Madrid, Spain</td><td>13th XBRL International Conference</td><td>4 days</td></tr><tr><td>4–7 June 2007</td><td>XBRL International – Munich, Germany</td><td>15th XBRL International Conference</td><td>4 days</td></tr><tr><td>3–6 December 2007</td><td>XBRL International – Vancouver Canada</td><td>16th XBRL International Conference</td><td>4 days</td></tr><tr><td>5–8 May 2008</td><td>XBRL International – Eindhoven, Netherlands</td><td>17th XBRL International Conference</td><td>4 days</td></tr><tr><td>16 December 2008</td><td>XBRL France – Paris</td><td>SC, EP, CESR, OAM and the SEC’s IDEA for the credit crunch (presentation by one of the researchers)</td><td>Breakfast meeting</td></tr><tr><td>20 January 2009</td><td>XBRL France – Paris</td><td>Petit déjeuner XBRL présentation des greffes</td><td>Breakfast meeting</td></tr><tr><td>23–25 June 2009</td><td>XBRL International – Paris, France</td><td>19th XBRL International Conference</td><td>4 days</td></tr><tr><td>20 January 2010</td><td>XBRL France – Paris</td><td>Training session</td><td>1 day</td></tr><tr><td>08 January 2010</td><td>XBRL France – Groupe Convergence XBRL France – EDIFICAS</td><td>EDIFACT convergence meeting</td><td>3 h</td></tr></table>
