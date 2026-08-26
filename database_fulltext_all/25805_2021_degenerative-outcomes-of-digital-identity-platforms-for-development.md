---
otero_id: 25805
otero_key: "4C6KGJ22"
title: "Degenerative outcomes of digital identity platforms for development"
authors: "Silvia Masiero; Viktor Arvidsson"
year: "2021"
journal: "Information Systems Journal"
doi: "10.1111/isj.12351"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
S P E C I A L I S S U E P A P E R

WILEY

# Degenerative outcomes of digital identity platforms for development

Silvia Masiero<sup>1</sup> | Viktor Arvidsson<sup>2,3</sup>

<sup>1</sup>Department of Informatics, University of Oslo, Ole-Johan Dahls Hus, Oslo, Norway <sup>2</sup>Business Information Systems, University of Sydney Business School, Sydney, New South Wales, Australia

<sup>3</sup>House of Innovation, Stockholm School of Economics, Stockholm, Sweden

Correspondence Silvia Masiero, Department of Informatics University of Oslo, Ole-Johan Dahls Hus, Gaustadalleèn 23B, Oslo N-0373, Norway. Email: silvima@ifi.uio.no

Funding information Marianne and Marcus Wallenberg Foundation London School of Economics and Political Science

## Abstract

Digital identity platforms are widely regarded as important means to improve social protection systems. Yet these platforms have been implicated in the production of a range of unintended outcomes for development beneficiaries. To clarify how digital identity platforms enable the production of one such outcome that we call degenerative, because it causes target systems to deteriorate, we conduct a case study of the incorporation of Aadhaar, the world's largest digital identity platform, in India's primary food security scheme. Based on the data from two South Indian states, we show how the incorporation produced degenerative effects in the access, monitoring, and policy layers of the social protection system. These effects lead us to theorise how Aadhaar enabled the degenerative outcome via exclusion, distortion, and redirection, making public distribution of subsidised goods displaceable in favour of cash transfers.

## K E Y W O R D S

Aadhaar, degenerative, digital identity platform, digital platforms for development, ICT4D

## 1 | INTRODUCTION

Digital platforms have been studied predominantly from the angles of governance, business intelligence, and profit generation (eg, De Reuver, Sørensen, & Basole, 2018; Gawer, 2009; Ghazawneh & Henfridsson, 2013; Parker, Van

Alstyne, & Choudary, 2016; Tiwana, 2013). However, there is a growing sense that digital platforms can contribute to socio-economic development. This has led digital platforms to become a new object of interest for research on information and communication technologies for development, or ICT4D (Koskinen, Bonina, & Eaton, 2018, 2019; Masiero & Nicholson, 2020; Nicholson, Nielsen, Sæbø, & Sahay, 2019; Nielsen, 2017). Whereas information systems (IS) research on digital platforms is mainly concerned with how these enable innovation or generativit (Eaton, Elaluf-Calderwood, Sørensen, & Yoo, 2015; Eck & Uebernickel, 2016; Tilson, Lyytinen, & Sørensen, 2010; Yoo, Henfridsson, & Lyytinen, 2010), the ICT4D literature explicitly relates digital platforms with socio-economic development processes. Not only are digital platforms thus examined outside a global North context, but these ar also studied in terms of their embeddedness in development outcomes (Bonina, Koskinen, Eaton, & Gawer, 2021; Koskinen et al., 2018, 2019).

Social protection systems (public and private programmes that provide benefit transfers to the poor and protect them against livelihood risks) are one context in which digital platforms can play a positive role. One development to this end is the incorporation of digital identity platforms that encode biometric and demographic details of social pro tection recipients. Operating as innovation platforms that constitute “technological building blocks” for third-part development (Gawer, 2009), digital identity platforms can help developing countries expand the range of public ser vices, while affording secure identification to improve resource allocation. By matching biometric and demographic data with recipients' entitlements, digital identity platforms are especially believed to afford accurate targeting, providing an optimal fix to issues such as leakage and diversion known to plague social protection systems (Gelb & Metz, 2018).

Despite the optimism that motivates the incorporation of digital identity platforms in social protection systems, digital identity platforms may produce unintended outcomes. For example, research has found digital identity plat forms to cause exclusionary outcomes that, by denying recipients key supplies and/or barring migrants and refugees from social protection schemes, harm the most vulnerable (Drèze, Khalid, Khera, & Somanchi, 2017; Drèze & Khera, 2015, 2017; Khera, 2019; Ramakumar, 2011; Ramanathan, 2014; Weitzberg, 2020; Weitzberg, Cheesman, Martin, & Schoemaker, 2021). In extreme cases, such unintended outcomes become so serious to block the incorpo ration of digital identity platforms altogether. For example, Kenya's High Court in 2020 ruled that, although the risk of exclusion was insufficient to rule the country's digital identity platform Huduma Namba unconstitutional, “a clear regulatory framework that addresses the possibility” was needed.

We aim to understand the role digital identity platforms play in socio-economic development processes that produce a specific unintended outcome that we call degenerative. In medicine, degenerative refers to a diseas that is characterised by progressive deterioration and loss of function in the organs or tissue. More generally, degeneration refers to a decline and deterioration of a system that results in a lowering of effective power, vitality, o essential quality. In our case, the notion focuses our attention on how digital identity platforms leave target system in enfeebled or terminal states. Clarifying how digital identity platforms degenerate the context they are incorporated in is particularly important considering that such outcomes are easily overshadowed by digital identity platforms' generative aspects when their incorporation succeeds and their technical design, consequently, enable new socio-economic agendas (cf. Gelb & Clark, 2013; Gelb & Metz, 2018). This leads us to ask the research question: how do digital identity platforms enable degenerative outcomes? In particular, we attend to their design properties

To understand this, we conduct a case study of the incorporation of the world's largest digital identity platform India's Aadhaar (meaning platform , foundation ), in the country's public distribution system (PDS). The PDS is th primary food security scheme in India. It provides basic commodities to below-poverty-line households at subsidised prices. Over the last few years, access to the PDS has become conditional to Aadhaar-based authentication in several Indian states. Specifically, our analysis draws on data from two South Indian states, Kerala and Karnataka, on the increasing digitisation of the PDS (2011–2014) and the incorporation of Aadhaar within it (2014-present). Our study shows that Aadhaar produced degenerative effects in three different layers of the PDS, which we term access (th front-end where social protection recipients access goods), monitoring (the back-end monitoring of the social protection system), and policy (the agenda on which social protection is based). By relating these effects at each layer wit design properties of Aadhaar, our analysis clarifies three aspects of degenerative digital identity platform outcomes exclusion from access, distortion of monitoring, and redirection of policy away from public distribution of subsidised goods. Together, these aspects help explain the role that Aadhaar has played in enabling a new socio-economic agenda, where the PDS, a long-standing social protection scheme, is being made replaceable by cash transfers coun ter to its initial intent.

We develop the notion of degenerative digital identity platform outcomes as follows. We first relate the design properties of digital platforms with socio-economic development to centre our attention on digital identity platforms and their incorporation in social protection systems. We then introduce the problem of degenerative outcomes of digital identity platforms for development, and explain the role that Aadhaar played in PDS' degeneration. Specifi cally, we illustrate the effects of its incorporation in the three layers at which the digital identity platforms operate and relate these to its design properties. Our discussion positions the case study within the literature on digital plat forms for development, clarifying the need to examine both generative and degenerative dynamics to understand socio-economic outcomes of digital identity platforms, and draws policy implications for incorporating digital identit in social protection at a time when a “digital identity revolution” is affecting developing countries (Muralidharan Niehaus, & Sukhtankar, 2020).

## 2 | DIGITAL IDENTITY PLATFORMS AND DEVELOPMENT

## 2.1 | Digital platforms and socio-economic development

Digital platforms are generally defined as “the extensible codebase of a software-based system shared by apps that interoperate with it, and the interfaces through which they interoperate” (Tiwana, 2013, p. 7). This definition accentuates how digital platforms offer third-party developers, or complementors, the possibility to build complements upon them through boundary resources (Eaton et al., 2015; Ghazawneh & Henfridsson, 2013). Along these lines, IS research on digital platforms is generally concerned with what Gawer (2009) termed innovation platforms. By con trast with transaction platforms, which extract rent by improving the matching of supply and demand, innovation platforms direct the large, varied, and uncoordinated audiences (Zittrain, 2006, p. 1980) that multi-sided market join toward development of new products and services. Two concerns have therefore been how the architectur and governance design of digital platforms enable organisations to add sides to the market in order to scale the plat form ecosystem through network effects; and how boundary resources can be configured in order to combin resources generatively (Eaton et al., 2015; Eck & Uebernickel, 2016; Ghazawneh & Henfridsson, 2013)

The emerging literature on digital platforms for development presents many continuities with IS research on dig ital platforms: it maintains the distinction between transaction and innovation platforms (Bonina et al., 2021) and explores the tensions that emerge from various architecture and governance designs (Nicholson et al., 2019). To th existing literature, research on digital platforms for development adds new foci such as the roles of digital platforms in decentralising the delivery of social assistance (Madon, Ranjini, Anantha Krishnan, & Babu, 2019), generating inclu sive development models (Addo & Senyo, 2021) and improving refugee management (Madon & Schoemaker, forthcoming). In a review of digital platforms for development literature, Bonina et al. (2021) identify six key questions for future research: (a) how to release the innovation platforms' development potential; (b) whether digital platforms help create new institutions or destroy them; (c) whether and how transaction platforms may exacerbate inequality and exclusion; (d) what digital platforms alternatives there are in the global South and what alternative forms of value digital platforms create for development; (e) what is the dark side of digital plat forms for development; and (f) how digital platforms for development can be better categorised

Together, these questions point to how research on digital platforms for development departs from the predom inant focus on the private sector in the global North (Addo & Senyo, 2021; Mir, Kar, Dwivedi, Gupta, & Sharma, 2020; Mukhopadhyay, Bouwman, & Jaiswal, 2019) and is driven by an alternative logic that centres human development over profit optimisation (Masiero & Nicholson, 2020). This discontinuity is well reflected in recent ICT4D research on digital platforms that emphasise their implications for socio-economic development (Bonina et al., 2021; Koskinen et al., 2018, 2019; Nicholson et al., 2019). By contrast with conventional digital platform research that focus on business model innovation and profit generation, for example, observing the dialectics of openness and control (Eaton et al., 2015; Ghazawneh & Henfridsson, 2013) and/or the monetisation of platform ecosystems (Parker et al., 2016) from economic and engineering perspectives, such a focus highlights that the out comes of digital platforms cannot be evaluated in isolation. A digital platform may well be successfully implemented yet negatively affect the target system in which it is incorporated.

In theory, innovation platforms have the potential to fill disjunctures between the design of complements for and the lived reality of people in developing countries, that is, design-reality gaps (Heeks, 2002). In particular, this is true for innovation platforms that are designed as digital global public goods, or DGPG (Nicholson et al., 2019) because such innovation platforms are characterised by non-rivalry (use by an actor does not hinder the possibilit of use by others), non-excludability (nobody can be excluded from use) and availability on a global scale. These fea tures make it possible for complementors to create locally-relevant products and services that fill design-reality gaps thereby leading DGPG to tentatively answer the question on how innovation platforms contribute to socioeconomic development (Nicholson et al., 2019; Russpatrick, 2020). Yet, further research is needed to put this asser tion to the test.

More at large, as noted by Koskinen et al. (2019), transaction platforms – especially those with a global nature – find several instantiations in research on digital platforms for development. For example, many studies focus on th production of disempowering effects by digital labour platforms, as well as the links of such platforms with develop ment effects (cf. Graham, Hjorth, & Lehdonvirta, 2017; Heeks, 2017; Heeks, Eskelund, Gomez-Morantes, Malik, & Nicholson, 2020; Malik, Heeks, Masiero, & Nicholson, 2021). Conversely, research of innovation platforms that take socio-economic development into account are largely missing. This clashes with the rapid proliferation across devel oping countries of at least one type of innovation platform, commonly referred to as digital identity platforms

## 2.2 | Digital identity platforms and social protection

Developing countries have been largely interested by social protection, meaning “all public and private initiatives that provide income or consumption transfers to the poor, protect the vulnerable against livelihood risks, and enhanc the social status and rights of the marginalised” (Devereux & Sabates-Wheeler, 2004). Social protection systems, through, for example, food security schemes and employment guarantees, provide effective responses to global pov erty and exclusion (Barrientos & Hulme, 2016; Carswell & De Neve, 2014; Devereux & Vincent, 2010), making them a crucial component of anti-poverty policy.

The last two decades have seen an increased digitisation of social protection systems around the globe. Fo example, anti-poverty cash transfer programmes are being converted into mobile money flows, to avoid leakage and corruption from physical delivery of cash (Aker, Boumnijel, McClelland, & Tierney, 2015; Devereux & Vincent, 2010) The administrative stages of social protection systems, such as the management of cards for food aid or the determi nation of poverty levels, have similarly been digitised (Bhatia, Donger, & Bhabha, 2021; Masiero & Prakash, 2015, 2019), sometimes with specific provisions for vulnerable categories such as refugees or displaced people built into the system (Iazzolino, 2021; Martin & Taylor, 2021; Schoemaker, Baslan, Pon, & Dell, 2021)

A recent development along this trajectory is the incorporation of digital identity platforms in social protection schemes. Digital identity platforms afford social protection schemes where identification, authentication and autho risation are all performed digitally (Nyst, Makin, Pannifer, & Whitley, 2016, p. 8), through architectures that connec users to a repository where their biometric and demographic data are digitally encoded. The core-complement architecture of digital identity platforms is illustrated in Figure 1.

![](/api/attachments/4C6KGJ22/fulltext/images/89ca064c230784297998fadc2afd54f31cdc5009a38ec4eb222942a785cb55f2.jpg)  
F I G U R E 1 Digital identity platform architecture (adapted from Nyst et al., 2016, p. 12)

A digital identity platform has a repository of users' biometric and demographic data at its core and boundar resources, such as Application Programming Interfaces (API) and Software Development Kits (SDK), made available to complementors to develop products and services on top of it (Mukhopadhyay et al., 2019, p. 443). It, therefore constitutes a particular type of innovation platform, where functions of identification, authentication and authorisa tion are tied together. Identification indicates the process of establishing information about an individual , authenti cation indicates the assertion of an identity previously established during identification and authorisation is th process of determining what actions may be performed or services accessed on the basis of the asserted and authenticated identity” (Nyst et al., 2016, pp. 8–9). When a product or service is mediated through a digital identity plat form, complementors can make access authorisation conditional to correct identification and authorisation of users through the platform core.

Making access to services conditional to secure identification and authorisation has been put into direct relatio with the goals of social protection. Targeted social protection schemes are subjected, as in Devereux (2016), to two types of errors: first, an exclusion error, where entitled subjects are excluded from the programme. Second, an inclusio error, where targeting of social protection fails as a result of the erroneous inclusion of non-entitled subjects. Matching records with each citizen's entitlement, digital identity platforms are designed to guarantee accurate targeting, includin all those entitled to a certain scheme and excluding all others, such as duplicates and fraudsters. This reflects Koskine et al.'s (2018, 2019) vision of digital platforms as embedded in socio-economic development processes.

From this development stems a positive digital platforms for development orthodoxy. Social protection schemes are commonly targeted to users with determinate characteristics (Devereux, 2016), such as income levels or member ship to particular vulnerable groups (eg, migrants or refugees), which determine their entitlement. To access entitle ments under a determinate scheme, an individual needs to prove to be who they claim to be and to meet th requirements for the programme (Devereux, 2016; Devereux & Sabates-Wheeler, 2004). Incorporating digital identit platforms in social protection schemes thus affords access through recognition of individuals as entitled users.

Beyond access, two additional positive outcomes are expected of digital identity platforms. First, through their identifi cation functionalities, such platforms are believed to afford improved monitoring of social protection schemes, in terms of the back-end phases that precede delivery of social benefits. Back-end phases vary across programmes and range from administration, common to all programmes, to transportation and storage of commodities where in-kind benefits ar involved. Second, social protection programmes are part of development policies, meaning the broader anti-poverty strate gies underpinning specific schemes. Digital identity platforms are an integral part of such policies, believed to optimise th delivery of benefits to the needful and preserve the financial sustainability of schemes (cf. Gelb & Metz, 2018).

At the same time, unintended outcomes have emerged with the incorporation of digital identity platforms into social protection systems and schemes. For example. digital identity platforms have been linked to exclusionary out comes, such as in Kenya where the Huduma Namba platform, developed to improve social protection, has been blocked by the High Court. Some digital identity platforms have been associated with particularly grave outcomes such as hunger deaths out of exclusion from food security provisions (cf. Singh, 2019) or exclusion from social assis tance of vulnerable people without proof of identity (cf. Weitzberg, 2020). Outcomes like these are clearl unintended in light of the goals of social protection.

But while there is an increased awareness globally that the outcomes of digital identity platforms may worsen situations for intended social protection recipients, despite stated goals of improving programme delivery, these unintended outcomes have yet to be theorised in depth. In particular, there is a need to specify unintended out comes of different types, and to relate socio-economic effects at different layers of target systems with the desig properties of digital identity platforms as to clarify how these outcomes are produced. Theorising about degenerativ outcomes is of special importance, as these represent outcomes where digital identity platforms leave target system in an enfeebled or terminal state, which focuses our research question on how the design properties of digital iden tity platforms enable them.

## 3 | METHODS

## 3.1 | Data collection

Our study relies on the first author's 10-year work on the PDS and its digitisation. The first author has conducted long-term research on digitisation of the PDS (2011–2014) and its subsequent transition to Aadhaar in selecte states (2014-). The case drew our attention as our fieldwork revealed a substantial gap between the proclamation of Aadhaar as a success and the issues that many users faced as a result of its incorporation in the food security scheme. These issues, epitomised by exclusion of entitled recipients from the food security scheme, increasingl focused our attention toward how a digital identity platform intended to improve social protection can produc degenerative outcomes.

To collect data, we used interpretive methods (Walsham, 1995). Data collection consisted of three main phases summarised in Table 1. Fieldwork, inspired by the anthropological view that the state is met by citizens in the form of physical embodiments, such as the police or government bureaus (Corbridge, Williams, Srivastava, & Véron, 2005), was based mainly on visits to PDS ration shops, where the first author observed technology-mediated access to the PDS and interviewed the actors involved. Data collected during this longitudinal study were used to identify degenerative effects of Aadhaar's incorporation the PDS and their causes.

T A B L E 1 Summary of interviews

<table><tr><td colspan="2">Computerisation of PDS in Kerala, 2011–2012</td></tr><tr><td>Interviewees</td><td>No.</td></tr><tr><td>Officers at Food and Civil Supplies Department (Government of Kerala)</td><td>7</td></tr><tr><td>District and sub-district Food and Civil Supplies officers</td><td>17</td></tr><tr><td>PDS ration dealers</td><td>15</td></tr><tr><td>National Informatics Centre (NIC) software developers</td><td>9</td></tr><tr><td>Staff at Kerala State Information Technology Mission (KSITM)</td><td>8</td></tr><tr><td>PDS beneficiaries in:</td><td>36</td></tr><tr><td>1. Urban areas (Trivandrum, Malappuram, Kochi, Kozhikode, Kollam)</td><td></td></tr><tr><td>2. Urban slum colonies (Karimadom, Chenkalchoola)</td><td></td></tr><tr><td>3. Rural villages (districts of Trivandrum, Kollam, Malappuram Calicut, Wayanad)</td><td></td></tr><tr><td>4. Tribal areas (Wayanad, northern areas of Malappuram district)</td><td></td></tr><tr><td>Civic and political activists</td><td>10</td></tr><tr><td>Staff at the state&#x27;s telecentre project (management, telecentre staff)</td><td>24</td></tr><tr><td>Total</td><td>126</td></tr><tr><td colspan="2">Biometric PDS in Karnataka, 2014–2015</td></tr><tr><td>Interviewees</td><td>No.</td></tr><tr><td>Staff at Food, Civil Supplies, and Consumer Affairs Department</td><td>5</td></tr><tr><td>Staff at PDS godowns (warehouses where PDS foodgrains are stored)</td><td>9</td></tr><tr><td>PDS ration dealers</td><td>12</td></tr><tr><td>National Informatics Centre (NIC) software developers</td><td>5</td></tr><tr><td>Implementers working on Aadhaar-based applications</td><td>6</td></tr><tr><td>PDS beneficiaries in:</td><td>18</td></tr><tr><td>1. Urban areas (Bangalore: Risaldar Street, Someshwarpura, Bangalore Central)</td><td></td></tr><tr><td>2. Semi-urban areas (Bangalore: Doddathogur, Anekal)</td><td></td></tr><tr><td>3. Rural villages (districts of: Tumkur, Kolar)</td><td></td></tr><tr><td>Civic and political activists</td><td>7</td></tr><tr><td>Total</td><td>62</td></tr><tr><td colspan="2">Aadhaar-Based PDS in Karnataka, 2018</td></tr><tr><td>Interviewees</td><td>No.</td></tr><tr><td>Ration shop owners</td><td>6</td></tr><tr><td>Ration shop employees</td><td>8</td></tr><tr><td>Aadhaar-based PDS beneficiaries in:</td><td>25</td></tr><tr><td>1. Urban areas (Bangalore: BTM Stage 1; Koramangala; Belakadi; ISRO Colony; JP Nagar)</td><td></td></tr><tr><td>2. Semi-urban areas (Bangalore: Bommanahalli; Vittasandra; Velankani; Doddathogur; Ponappa Agrahara; Ayodhya Nagar)</td><td></td></tr><tr><td>3. Rural villages (district of Kolar)</td><td></td></tr><tr><td>Programme officers</td><td>3</td></tr><tr><td>Total</td><td>42</td></tr><tr><td>Total interviews (2011–2018)</td><td>230</td></tr></table>

Table 1 summarises the three phases and the interviews conducted in each of them. In the first phase digitisation of the PDS, conducted at the state level, we focused primarily on the back-end. It helped us capture the IS development undertaken to prevent the diversion of subsidised goods. The first author conducted fieldwork over

8 months (2011–2012) in Kerala, one of the first states to digitise the PDS. During this phase, she conducted 126 interviews with government officials, PDS beneficiaries, PDS officers, members of civic associations and othe actors involved in the digitisation of the food security scheme. She assisted in live demonstrations of the digitised PDS in the National Informatics Centre (NIC Kerala) and observed the initial stages of transition toward a biometric system in the ration shops

In a second phase, incorporation of biometric technologies in the PDS was conducted by several states in th form of pilot projects. During this phase, the first author and a colleague conducted 10 weeks of fieldwork (2014– 2015) in Karnataka, one of the states that was piloting a biometric PDS through a local, state-owned database. Sixt two interviews were conducted with government officials, PDS beneficiaries, ration dealers and members of the public, focusing specifically on the impact on recipients. At this point, ration shops in 6 out of 29 districts had been fitted with biometric point-of-sale machines, and fieldwork allowed the researcher to observe the biometric pro cesses of collection of goods from ration shops

In a third phase, Aadhaar was incorporated in the PDS in several Indian states following legal backing (the Targeted Delivery of Financial and other Subsidies, Benefits and Services Act, known as the Aadhaar Act (2016)) During this phase, the first author and a colleague conducted 42 interviews in Karnataka, targeting ration shops in the Bangalore and Kolar districts where Aadhaar had been fully incorporated. We interviewed ration dealers, as wel as beneficiaries met in the ration shops whom we asked to comment on the new Aadhaar-based PDS. During th study we also reviewed the literature on the Aadhaar-based PDS, compiling an extensive list of Web documents and press releases documenting the transition. A summary of our secondary sources is provided in Appendix A.

Increasingly during the study, the first author's field data have been related to Aadhaar's architecture and gover nance design. The Unique Identification Authority of India (UIDAI), which manages Aadhaar on behalf of the Govern ment, provides many sources on its website and through media press releases, which we have used to form an understanding of Aadhaar's design properties. These documents have been integrated with state-level reports on Aadhaar and the PDS, which we have reviewed with a focus on our two states. A further data source have been the PDS websites of Kerala and Karnataka, which publish information on Aadhaar seeding and instructions for users t authenticate with it.

## 3.2 | Data analysis

To clarify how the design properties of the Aadhaar platform enabled degenerative outcomes in a large social protection programme, we proceeded in two phases. First, we needed to form a clear idea of the ways in which the platform was incorporated in the food security scheme. To do so, the first author examined effects in three layers at which Aadhaar operates in the PDS: access (ration shops where users access goods), monitoring (back-end monitoring of the PDS), and policy (determination of policy decisions affecting the PDS). The researcher identified such layers during data collection, then refined the description of each layer through secondary data, in depth interviews and field observation.

In a second phase, we elicited aspects for each layer which explain the role of Aadhaar in the PDS' degenera tion. By aspects we refer to ways in which Aadhaar, through its design properties, participated in the production of the degenerative outcome. To this end, we used both field data and UIDAI resources to understand how Aadhaar, as opposed to other parts of the social protection system, contributed to the outcome. The analysis resulted in three aspects of degeneration: exclusion of entitled users from the PDS, distortion of ration shop moni toring systems, and redirection of development policy from subsidies to cash transfers. To finalise these aspects, we used dialogue among ourselves, consultation of secondary sources at the national and state level, and presen tation of previous findings in Indian and international institutions, including universities and a registered charit working on digital identity.

## 4 | AADHAAR: DIGITAL IDENTITY FOR SOCIAL WELFARE?

Aadhaar is a platform owned by the Government of India and managed through UIDAI, an agency established under the jurisdiction of the Ministry of Electronics and Information Technology. Here we describe the Aadhaar platform and its incorporation into the PDS.

## 4.1 | The Aadhaar platform

Until 2009 India did not have a national system to prove identity. According to UNICEF (2013, cited i Bhatia & Bhabha, 2016, p. 65), only approximately 40% of the Indian population had their birth registered, with the identification burden falling largely on people in need for social protection. Due to inability to prove identity, undocumented people were unable to be recognised as social protection beneficiaries (UIDAI, 2010). In India social protection is based on numerous targeted programmes (Saini, Sharma, Gulati, Hussain, & von Braun, 2017), ranging from food security to pensions, health insurance and rural employment guarantees, which makes it essential to correctly identify recipients and match identities with their status as beneficiaries.

UIDAI was created in January 2009 and originally functioned as an attached office of India's Planning Commission; since 2016 it operates under the jurisdiction of the Ministry of Electronics and Information Technology, Government of India. UIDAI's mandate was to provide a unique 12-digit number to all residents who enrolled in the Aadhaar programme, capture biometric (10 fingerprints and iris scans) and demographic data, and store these in a database – Central Identities Data Repository (CIDR) – that constitutes the platform's core. From 2011, enrolment centres opened all over India, accompanied by a strong enrolment campaign. The enrolment process, referred to as “free and voluntary” (Nilekani & Shah, 2016) by the Government, takes few minutes, promising to help residents receive better public services based on platform-based authentication.

While adopting a minimal approach, where only essential biometric and demographic data are collected (Mukhopadhyay et al., 2019), Aadhaar involves all three functions of identification, authentication and authorisation of a digital identity platform (Nyst et al., 2016), as illustrated in Figure 2. Through CIDR, the Indian government act as identity provider, enrolling third-parties who can build complements on Aadhaar through boundary resources. As illustrated in the Aadhaar developer portal, UIDAI has created a client application to help the community develop applications that use Aadhaar authentication.<sup>2</sup>

Aadhaar has constructed one of the largest service ecosystems worldwide in terms of enrolled users (UIDAI, 2019). Rather than acting as a unique service provider, the Indian government has created a network of public and private services provided by Aadhaar's complementors and enabled by the platform (Mir et al., 2020) As the platform owner, the Government has through UIDAI designed the platform's architecture, actively directing the many participants in its ecosystem toward the provision of services (Mukhopadhyay et al., 2019). Initially al third parties were enabled to use the platform, which resulted in three broad types of complementors: governmen tal agencies, actors in regulated industry, and private actors (Ramnath & Mendonca, 2016, cited in Mukhopadhyay et al., 2019, p. 42).

On 26 September 2018, the Supreme Court of India pronounced a verdict in response to over 30 petitions that, from 2012 onwards, had confronted the constitutionality of Aadhaar (Rao & Nair, 2019, p. 477). The Supreme Court sanctioned that Aadhaar is constitutional, but its constitutionality is grounded precisely on the digital identity platform's ability to strengthen social protection (Rao & Nair, 2019, p. 477). This has as of yet limited the use of the platform for commercial purposes, excluding privat entities from development of Aadhaar-based complements. According to the UIDAI Annual Report 2019–2020:

Third Parties: -Type 1 – governmental agencies -Type 2 – regulated industries -Type 3 – private actor (use of the platform for commercial purposes limited since 2018)

![](/api/attachments/4C6KGJ22/fulltext/images/c867fb7d20736447aef391d61381c539fa73ed9821299967883c878608f85d67.jpg)  
F I G U R E 2 Aadhaar – Platform architecture

The judgement has helped Aadhaar emerge as a first public owned world's largest biometric technology platform which has not only empowered 123.5 crore [1.235 billion] people with biometric based unique identity but has also provided a nationwide infrastructure to establish their identity online from anywhere, anytime and enabled them to receive their entitlements and exercise their rights without any fear of it being taken away.

## 4.2 | Aadhaar: Incorporation into the PDS

Multiple welfare programmes use the identity functionalities that Aadhaar provides. Of them, the PDS is India's largest food security scheme, and an essential source of social protection for the vast majority of India's poor (Drèze & Khera, 2017). The PDS provides below-poverty-line (BPL) households with basic-need goods (primarily rice, wheat sugar and kerosene) at subsidised prices, with the goal of making them affordable to all. Related commodities ar centrally procured by the Food Corporation of India (FCI) and redistributed through a network of ration shops – so named because each household has the right to a monthly ration – throughout the country. The PDS was a universa scheme till the early 1990s, when a fiscal crisis called for restructuring. To limit the fiscal expenditure, the PDS moved from universal access to targeting the poorest households in India (Radhakrishna & Subbarao, 1997)

![](/api/attachments/4C6KGJ22/fulltext/images/04b2af2c3c9e2ea0309e917d4d5e72d3d9a687a6535ab993adf0a802624a4d68.jpg)  
F I G U R E 3 The Aadhaar-enabled PDS (based on Karnataka state-level system)

The PDS is accessed by beneficiaries through a ration card, a document that proves the household's poverty sta tus.<sup>3</sup> Different states operate different subsidy systems and households classified as Antyodaya Anna Yojana (the poorest of the poor) have the right to obtain a larger quantity of goods. Because of the price difference between subsidised goods and the market, the scheme is susceptible to high rates of leakage to non-entitled recipients. Such leakage has long been seen as one of the principal issues in the PDS (Gulati & Saini, 2015; Saini et al., 2017), and motivated Aadhaar's incorporation.

PDS' digitisation date back to the early 2000s, when state governments sought to monitor the scheme to reduce leakage in their local PDS markets. During our fieldwork in Kerala in 2011–2012, state governments delegated loca agencies, for example, the Kerala National Informatics Centre, to create databases of commodities stored in PDS warehouses, located across the country's districts and from which commodities are dispatched to ration shops. Th goal was to trace quantities received monthly by the ration shops, to check whether ration dealers were effectivel selling goods to registered beneficiaries.

Following such early efforts of digitisation, Aadhaar functionalities have been incorporated in the PDS through a process known as Aadhaar seeding.<sup>4</sup> In such a process, Aadhaar credentials are added to the database of PDS beneficiaries that is maintained by the FCI in each state. The result is a database of details of beneficiaries such as name poverty status and ration card number, matched with Aadhaar credentials for each person. Beneficiaries can then access the PDS with their biometric credentials.

The flow of Aadhaar-based disbursal of PDS goods in ration shops is illustrated in Figure 3. Once the beneficiar has authenticated through a biometric fingerprint scanner, the Aadhaar-seeded database matches their credentials with their entitlement, which is then disbursed.<sup>5</sup> If the user's biometric details do not find a match in the FCI database, the individual is not recognised as an entitled beneficiary and is hence unable to receive goods through the PDS. The process aims to clean the FCI database from duplicates and fake beneficiaries, hence minimising fraud and leakage (Saini et al., 2017).

## 5 | FINDINGS

## 5.1 | Effects of the incorporation of Aadhaar in the PDS

Aadhaar makes PDS authentication biometric. As our fieldwork has revealed, effects of this change go beyond th ration shop where authentication takes place. Changes operate at three layers of the PDS: access of users, monitorin of ration shops and the policy that informs the social protection programme. Changes in three layers and th observed consequences for the PDS are summarised in Table 2.

T A B L E 2 Layers of the Aadhaar-based PDS

<table><tr><td>Layer</td><td>Change enabled by Aadhaar</td><td>Consequences for the PDS</td></tr><tr><td>Access</td><td>Reconstruction of access to the PDS through Aadhaar-based user authentication</td><td>1. Transition of ration shops to an Aadhaar-enabled transaction interface2. Users recognised through authentication with CIDR based on fingerprints3. Aimed at eliminating leakage by scrapping fake beneficiaries</td></tr><tr><td>Monitoring</td><td>Reconstruction of back-end monitoring to ensure ration dealers do not divert goods</td><td>1. Design of monitoring tools specific for ration shop transactions2. Every transaction is Aadhaar-monitored through match with users&#x27; CIDR record</td></tr><tr><td>Policy</td><td>Reframing of the development policy underlying the PDS from a subsidy-based scheme to one based on cash transfers</td><td>1. Government advocacy for a shift from subsidies to cash transfers2. Aadhaar as integral part of that shift - enabling direct transfer of benefits3. Aadhaar inscribed in JAM trinity - broad architecture for cash transfer transition</td></tr></table>

## 5.1.1 | Layer 1: Access

Authentication of PDS recipients in ration shops is enabled by Aadhaar-seeded user data. Throughout fieldwork ration dealers argued for Aadhaar as a measure against fraud

Aadhaar makes it impossible to game the system. Those [ration dealers] who used to cheat and sell to the market cannot do so anymore, because the Aadhaar machine controls them. (Ration dealer, Bangalore, April 2018)

In the pre-Aadhaar system, inaccurate or bogus credentials could in principle lead to entitlement. During our fieldwork in Kerala, illegally secured BPL ration cards were reported to abound in the state.<sup>6</sup> Before our fieldwork i Karnataka, “temporary ration cards” were emitted in the state without prior verification of user details (Justic Wadhwa Committee for PDS in Karnataka, 2009), leading to demand for PDS goods exceeding supply. Aadhaar is designed as an antidote to these forms of leakage

## 5.1.2 | Layer 2: Monitoring

At the PDS back-end, goods are disbursed from FCI to district warehouses (known as godowns) and then to ration shops. In the Aadhaar-based PDS, ration shop transactions correspond to beneficiaries' records. The consignment of ration dealers is only disbursed after verification that goods are sold to registered users. As a ration dealer explains,

We [ration dealers] are not allowed to register for fresh ration stocks from the regional godown, unti the consignment for the current month has been completely disbursed. But since the quantity disbursed depends on [the number of] people who accessed the benefit through Aadhaar, the system does not allow ration shop owners to hoard rations illegally. (Ration dealer, Bangalore, April 2018)

Aadhaar hence changes the monitoring of the PDS in two ways. First, it bases the consignment of ration dealer on proof of sales, occurred with beneficiaries whose authenticity is proved by the Aadhaar record. Second, it allow portability across ration shops, as it delinks the user from the shop where they are registered. While at present ration shops still serve their base of registered users, the technology is in principle built to enable access from ever ration shop in the country, to enable users to opt out from ration dealers who are perceived to behave dishonestly

## 5.1.3 | Layer 3: Policy

Aadhaar is interlinked with the development policy of the PDS. The PDS is part of India's strategy of social protec tion based on subsidised goods, supplied through food security schemes that offer in-kind subsidies to the poor. Bu a new policy, based on cash transfers instead of subsidies, has been advocated by the Indian government in the Eco nomic Survey 2015:

[With cash transfers], by reducing the number of government departments involved in the distribution process, opportunities for leakage are curtailed (…) In addition to net fiscal savings, income transfers can compensate consumers and producers for exactly the welfare benefits they derive from price subsidies without distorting their incentives. (Government of India, 2015, p. 64)

The purpose of dismantling the PDS in favour of cash transfers was mostly silent in the interviews we conducted in 2011–2012. Over time however, Aadhaar was purposefully combined with the Pradhan Mantri Jan Dhan Yojan (literally “bank accounts for all people”), a scheme to give bank accounts to the poor, and mobile phones. Jan Dhan Aadhaar and mobiles – called the JAM Trinity – afford a cash transfer programme intended to replace food subsi dies (Government of India, 2015, pp. 64–65).

## 5.2 | Aspects of degeneration in the Aadhaar-based PDS

Our interest in degenerative outcomes stemmed from becoming aware of PDS users that, while able to access rations in the pre-Aadhaar system, reported inability to do so after Aadhaar's incorporation in it. This issue was vocalised in Indian media and over time became a recurring theme in discussion with PDS beneficiaries, leading us to investigate whether platform characteristics were implicated in it. As Aadhaar became the established way to deliver the PDS in our fieldwork states, two further aspects of degenerative outcomes emerged. Regarding moni toring, the shift to a specific actor (the ration dealer) comes with limited monitoring of other actors, which are responsible for substantial amounts of leakage. In terms of policy, the intended shift to cash transfers was met with apprehension across PDS users, who express general preference for the current system of subsidies. We related associated effects with Aadhaar's design properties to clarify its role. A summary of our analysis is presented in Table 3.

## 5.2.1 | Aspect 1: Exclusion

Exclusions of genuinely entitled users from the PDS became visible after Aadhaar's incorporation.<sup>7</sup> In Karnataka, we observed that each user is only allowed three attempts to authenticate with the biometric fingerprint reader, failing which they are invited to come back at another time. Aadhaar-induced exclusions are demonstrated by econometric estimates, which differ in size across states and regions but are consistent on the presence of exclusions (Drèze et al., 2017; Muralidharan et al., 2020).

T A B L E 3 Aspects of degeneration from Aadhaar's incorporation in the PDS

<table><tr><td></td><td>Aspect of degeneration</td><td>Design properties of the Aadhaar platform</td><td>Illustration of the degeneration</td></tr><tr><td>Exclusion (from access)</td><td>Entitled users denied rations due to inability to authenticate with Aadhaar in ration shops</td><td>Platform&#x27;s architecture built to subordinate access authorisation to Aadhaar authentication at the ration shop levelLack of inclusive features in the platform - that is, ways to disburse rations to genuine users for whom authentication fails</td><td>Pre-Aadhaar PDS: a system with wrongful inclusions and exclusionsAadhaar-based PDS: a system built to fight the inclusion error, at the cost of greater exclusions (Drèze et al., 2017; Muralidharan et al., 2020)</td></tr><tr><td>Distortion (of monitoring)</td><td>Ration dealers as the only PDS actor subjected to monitoring</td><td>Platform designed to monitor transactions at the point of sale (using CIDR to authenticate beneficiaries)Lack of features to control other PDS actors (eg, transportation or storage before ration shops)</td><td>Pre-Aadhaar PDS: state-level monitoring of godowns (eg, FIST in Karnataka)Aadhaar-based PDS: monitoring focused on ration dealers, at the cost of control on earlier stages of the system, where substantial leakage occurs (Khera, 2011)</td></tr><tr><td>Redirection (of policy)</td><td>Planned shift from the PDS to a cash transfer system</td><td>Platform designed to link Aadhaar to bank accounts and mobile devicesRegulated industries (including banking) able to build complements on Aadhaar, enabling cash transfer disbursal</td><td>Pre-Aadhaar PDS: a food security system based on in-kind subsidies to beneficiariesAadhaar-based PDS: designed to enable the transition from subsidies to a cash transfer system (Government of India, 2015), which users express concern about (Chanchani, 2017; Khera, 2014)</td></tr></table>

Mismatches in authentication are largely responsible for exclusions. During fieldwork we witnessed severa failed attempts to authentication in ration shops, resulting in inability of ration dealers to disburse goods. In fact Aadhaar-based point-of-sale machines require different technologies (fingerprint reader; connection with CIDR) to function together,<sup>8</sup> an event that even just an electricity failure may impede. In Karnataka, we saw whole families queueing together at ration shops, in the hope that at least one member would be able to authenticate within th three allowed attempts.

Examining Aadhaar's characteristics and specifically the core-complements architecture illustrated in Figure 2, two considerations link the design properties of the platform to the outcome of exclusion. First, the Aadhaar-based PDS is built specifically to subordinate authorisation to authentication:

Aadhaar is being introduced in the PDS as part of the greater fight against poverty (…) by fixing corruption in the main food security system, Aadhaar makes it impossible for people to impersonate rea users, or sell foodgrains to the private market for a profit. (Former PDS official, Bangalore, April 2015)

The Aadhaar-based PDS is not, however, depicted as a route to fight the exclusion error. This informs a second consideration on the lack of provisions for those excluded from Aadhaar:

In India, the language of voluntary enrolment has already given way to mandatory enrolment and seeding the UID number to get food in the public distribution system, to get work, to get cooking gas, to receive scholarships and pensions, to open and operate bank accounts, to register marriages, in renta agreements and sale deeds and wills. The poor have little choice in the matter. (Ramanathan, 2014

Throughout fieldwork, many ration dealers showed us the functioning of authentication in ration shops. In doing so, they emphasised how Aadhaar makes it difficult to game the system, not any affordances of the Aadhaar platform to include unjustly excluded beneficiaries. Many users – especially those for whom disbursement worked well – expressed satisfaction about the system for the same reason: its ability to prevent leakage, not to guarantee inclu sion. When asked about cases of exclusion, a user in Bangalore told us this was “the price to pay” for a non-corrupt system to work.

In sum, Aadhaar's incorporation in the PDS illustrates how a digital identity platform, designed to reduce fraud in social protection, ended up excluding genuine beneficiaries too, furthering its degeneration. In particular, the design property that subordinates authorisation to authentication ends up producing exclusions that constitute a worsened state for many beneficiaries. As a result, the history of leakage in the PDS inspired a core-complements architecture aimed at preventing fraud, but the same architecture results in a social protection system where exclusions are perpetuated.<sup>9</sup>

## 5.2.2 | Aspect 2: Distortion

PDS leakage occurs from godowns and during transportation. In Karnataka a Financial and Stock Accounting System (FIST) tracked goods from godowns to the ration shops. Our 2014–2015 fieldwork, however, revealed limited use of the system, with two of the godowns we visited not using it at all

In contrast, Aadhaar offers a monitoring system that checks transactions at the ration shop level. During field work, beneficiaries described situations in which ration dealers claimed running out of foodgrains, with PDS offi cers echoing the point that fraud by ration dealers needs monitoring

[In a pilot project of Aadhaar-enabled PDS] we are requesting users to authenticate with Aadhaar, so that the ration dealers can only sell goods to them. This is to prevent them from selling to hotels, privates, and whoever wants to trade with them illegally. (PDS Officer, Bangalore, April 2015)

Why the systemic blaming of ration dealers? As noted above, during India's structural adjustment, the pro gramme was criticised for its weight on the nation's fiscal system. For this reason, international institutions rec ommended the shift to a targeted system, restricting subsidies to users classified as BPL (Radhakrishna & Subbarao, 1997; Umali-Deininger & Deininger, 2001).

This transition had severe effects on ration dealers. As a result of the shrink of their customer basis, ratio dealers were severely impoverished; many could not cope with debt and had to close their shops due to unviability During fieldwork in Kerala, the memory of the immediate aftermath of the shift to a targeted PDS was very vivid with memories of debt-induced ration dealer suicides (Suchitra, 2004) and effects on ration shop viability persisting to the day:

Ration shops […] are not viable on their own. Many of us have had a shop licence for a very long time, and have no chance to learn a new profession. Now [after 1997] things have changed: many customers have left the shops […] many shops have had to close down because of debt. (Ration Dealer Union member, Trivandrum, August 2012)

Both states provided financial support to ration shops. In Kerala, poverty levels were re-estimated internall (from 25% to 42%) so to classify more users as BPL (Swaminathan, 2002, p. 51), and the government approved credi concessions to ration dealers. In Karnataka, ration dealers were allowed to sell a wider array of commodities in their shops, beyond those subsidised under the PDS. All these measures were taken to ensure survival of ration shops, in spite of the income shrink caused by the shift to targeting

Aadhaar is, however, delinked from such measures. The platform is functional to controlling the point of sale ensuring that only CIDR-authenticated transactions can take place. This involves two issues: first, the platform affords monitoring of ration dealers, but provides them no alternative for survival. Second, a monitoring mode centred on ration shops transcends the phases of transportation and storage of PDS goods before ration shops, in which substantial levels of leakage occur (Ramakumar, 2011). As a result, the Aadhaar-induced system distorts PD monitoring toward ration dealers, rather than other phases where leakage still occurs.

Distorted monitoring arises as a second aspect of degeneration. The platform had been designed to monitor ration dealers, deemed to be prone to fraud. But in doing so, its design properties are centred on monitoring transac tions at the point of sale, not tackling issues of transportation and storage and not addressing ration dealers' plea for economic survival. This furthers degeneration of the social protection system, as substantial issues that persisted over time remain unaddressed

## 5.2.3 | Aspect 3: Redirection

The JAM trinity is designed to enable transition from subsidies to cash transfers. In India's Economic Survey 2015 the Ministry of Finance motivated this decision:

If the JAM Number Trinity can be seamlessly linked, and all subsidies rolled into one or a few monthly transfers, real progress in terms of direct income support to the poor may finally be possible […] the poor will be protected and provided for; and many prices in India will be liberated to perform their role of efficiently allocating resources in the economy and boosting long run growth. (Government of India, 2015, p. 65)

Replacement of PDS with cash transfers was piloted in the states of Chandigarh, Puducherry and Dadra & Nagar Haveli in 2018–2019.<sup>10</sup> The reason for replacement, stated in the Economic Survey, is in the affordance of cash transfers to remove the regressive effects, room for corruption, and economic distortion that affected the PDS sinc its first decades (Government of India, 2015, pp. 64–65)

Yet, surveys made on PDS recipients raised doubts on these points. Aggarwal (2011), Puri (2012), Khera (2014 and Chanchani (2017) published surveys of PDS users that compared perceptions of the two policies, finding that users, while often not trusting ration dealers, still prefer subsidies to cash transfers. A fundamental reason for this i the relative security of subsidies, perceived as greater than that of cash (Chanchani, 2017, pp. 1852–1853).

These findings prompted us, in the final round of fieldwork, to ask PDS users the question on whether the would ideally prefer in-kind rations or an equal-value sum of cash to be credited to their bank accounts. We encoun tered a situation in which our interviewees declared general preference for in-kind rations, behind which was th comparison between the well-known PDS and the volatility of cash transfers. For their security, food rations are val ued by beneficiaries:

The ration shop is there for us every month (…) maybe it opens at different times, maybe not al (foodgrains) will be available, but it's there. It's food on our table (…) cash may or may not arrive, the bank may or may not disburse it, men in the family may use it for other things than food. (PDS beneficiary, Bangalore, April 2018)

The government's advocacy of cash transfers however continues, with mobile phones identified as the best option for disbursal of cash. In the Economic Survey 2015, the options of mobile banking and post office payment were mentioned as possible routes to enable disbursal, yet the option of post office payments never gained ground over the years (Drèze & Khera, 2020). A shift to mobile phones as a route to disbursal is advocated by Digital India and beyond the PDS, cash transfers have become an established part of the nation's social protection strategy (Raghavan, 2021).

Redirection of policy, from subsidies to cash transfers, constitutes a third aspect of degeneration. The transitio is economically justified with the arguments of regressiveness, distortion and room for leakage put forward by Gov ernment of India (2015). But the transition is still assessed as undesired by many recipients, for whom the passage to cash transfers, which the platform is designed to enable, constitutes a move to a state that they describe as wors than the current one. It is from the eyes of beneficiaries, for whom the PDS is built, that a third aspect of degenera tion of the social protection system is qualified

## 6 | DISCUSSION

Whereas IS research on digital platforms is mainly concerned with how the architecture and governance design enable generativity (Eaton et al., 2015; Eck & Uebernickel, 2016; Tilson et al., 2010; Yoo et al., 2010), digital platforms for development research must also consider the effects digital platforms have on the target systems in which they are incorporated. As our case demonstrated, a digital platform may well be successfully implemented yet hav detrimental effects on socio-economic development. Due to the far-reaching of the digital identity revolution that is unfolding in the Global South, these effects are particularly important to consider in the context of digital identity platforms. A first step to this end is to be specific about the various unintended outcomes these platforms are found to produce (Singh, 2019; Weitzberg, 2020). Our case study clarified how digital identity platforms enable degenera tive outcomes. By examining the effects of Aadhaar's incorporation in the PDS, and relating these with design prop erties at each level in which digital identity platforms can be seen to operate in food security schemes at large, our case study in particular allowed us to theorise about the role Aadhaar played in PDS' degeneration.

Our case study illustrated three aspects of degeneration of the PDS. The first aspect, exclusion, shows how Aadhaar's design properties lead to exclusions of entitled users from access to the PDS. The second aspect, distor tion, shows how the platform is designed to monitor the last mile of the PDS, distorting the focus from earlier phase of transportation and storage. Finally, the aspect of redirection shows how Aadhaar's design properties are functiona to redirection of the subsidy-based system to one based on cash transfers, counter to its initial intent. Together, these aspects help explain how the PDS following the successful incorporation of Aadhaar was found to be in a com parably enfeebled state with lower effective power, ultimately to the detriment of the beneficiaries for whom it is designed.

In particular, we focused our analysis on Aadhaar's design properties. In doing so, our research builds on previ ous studies of the PDS, as it clarifies how the technical design of the digital identity platform, at all three layers, is implicated in a degenerative outcome. Previous studies (cf. Drèze et al., 2017; Muralidharan et al., 2020) have shown exclusions. Here, we have seen how the design property that subordinates authorisation to authentication, made to combat leakage, leads to them. To studies showing the difficult conditions of ration shops (Khera, 2011) and users preference of PDS over cash transfers (Chanchani, 2017; Khera, 2014; Masiero & Das, 2019), we contribute nove understanding into how the digital identity platform is designed to monitor ration shop dealers, and to enable th cash transfer system toward which beneficiaries express suspicion. The perspective proposed here hence adds to the literature, by illuminating the digital platform's role in the target system's degeneration.

In what follows, we discuss degenerative outcomes in the context of platforms for development, as well as th need to investigate such outcomes beyond the access layer.

## 6.1 | Digital platforms and development: Exploring degeneration

Earlier literature on digital platforms for development is centred on the innovation potential of platforms, and on how it can be released (Bonina et al., 2021; Koskinen et al., 2018, 2019). In such a literature, it is the innovation potential of digital platforms that affords development of context-based complements, meeting the needs of user and implementers in developing countries. Critical sides, such as the “dark side” of platforms for development (Bonina et al., 2021, p. 25) or their potential to exacerbate existing inequalities (Bonina et al., 2021; Koskinen et al., 2018, 2019) have been considered, but so far have not been put in relation to the design properties of digita platforms for development.

Against this backdrop, our study further demonstrates that digital platforms with a development purpose can end up having detrimental effects for users. The study links the platform features of Aadhaar to degenerative out comes, detailing how these hurt the users that were supposed to benefit from its incorporation. While unintended outcomes are generally discussed in digital platform literature (cf. De Reuver et al., 2018), the degenerative outcome illustrated here show the decline and deterioration of a platform designed for development and constitute one such unintended outcome that is of particular importance to understand. Specifically, we showed the effects of such decline on social protection, illuminating how even a digital platform reported as successful can produce degenera tive outcomes.

Other studies of digital platforms for development have focused on their positive effects. On Aadhaar Mukhopadhyay et al. (2019) state that the platform's openness affords the scalability needed to serve the poor, whil Mir et al. (2020) identify uniqueness and privacy as properties that enhance secure identification. Such studies, how ever, take the perspective of the digital platform owner (Addo & Senyo, 2021), without openly engaging the disad vantaged users targeted by social protection schemes. Our study completes such a perspective, using long-term fieldwork with disadvantaged users to explore salient aspects of degeneration from digital identity platforms from these with users points of view.

Therefore, a primary implication of our study is that the dark side (Bonina et al., 2021, p. 25) of digital plat forms for development may be linked to their design properties, including the generative capacities that are wel observed to afford third-party innovation. Given the nascent stage of this literature, more studies of digital platform for development are needed to explore degeneration in other contexts. In studying degeneration, we should be reminded that what is considered successful from a digital platform owner's perspective (eg, cash transfers replacing the PDS) may not be equally successful for digital platform users, or can even be negative for them as our respondents suggested. We hence submit that user perspectives, central to ICT4D research since the theorisation of design-reality gaps (Heeks, 2002), should maintain their centrality in research on degenerative outcomes of digita platforms.

More at large, the argument that generativity is the basis of success stems from IS research on digital platforms which maintains that digital platforms are successful in virtue of their potential for innovation (Eaton et al., 2015 Ghazawneh & Henfridsson. 2013). Nevertheless, we illustrated how degeneration can stem exactly from design properties designed for positive purposes, in the Aadhaar case as positive as the uplifting of millions of poor. Degen eration stems, therefore, from an essential feature of innovation platforms more generally, which makes our argu ment relevant beyond the literature on digital platforms for development and digital identity platforms in particular Stemming from digital platforms' innovative potential, the overall outcome of degeneration may accordingly hold in for-profit platforms as well.

The study of degeneration in for-profit platforms is beyond the scope of this paper. The vocabulary used in this work impinges on Aadhaar's context, and more studies are needed to explore degeneration in for-profit contexts With its notion of aspects of degeneration linked to design properties, this paper however provides conceptual tools for such studies to be conducted. Future research in this vein may discover that some of the aspects here found have salience also in these contexts, but it may also be that wholly other aspects will be found. Regardless, such studies will help balance the literature overall

## 6.2 | Digital platforms and social protection: Beyond access

Our research has several implications for countries incorporating digital identity platforms in social protection systems and associated welfare schemes. Such an incorporation is becoming increasingly diffused, as a securely verified identity is considered a general pre-condition for individuals to access essential services (Nyst et al., 2016). Its importance for access has made identity a fundamental right recognised by the United Nations, now stated as Sustainabl Development Goal (SDG) 16:9 as the need to “by 2030, provide legal identity for all, including birth registration”.

Yet, in the interdisciplinary literature on digital identity focus is mostly away from digital platforms' design prop erties (Masiero & Shakthi, 2020). When moving away from the IS field, studies of digital identity generally do not contemplate Tiwana's (2013) notion of digital platforms as extensible codebases for the construction of comple ments. Different foci of the digital identity literature allow exploring important topics, such as the sense of vulnerability due to fear of authentication failure that Chaudhuri (2021) describes in relation to users of the biometric PDS in Jharkhand, or the data privacy and surveillance implications of digital identity for vulnerable users (Hosein & Whitley, 2019; Krishna, 2021; Martin, 2021; Martin & Taylor, 2021). Studies of these topics, which make up a large part of the digital identity literature (Masiero & Shakthi, 2020), have nonetheless left a clear gap in terms of the impli cations that digital identity platforms' design properties for socio-economic development. A gap which our stud encourages others to explore.

Besides addressing this gap, our study makes a further contribution, explicated in the three aspects of degenera tion that we find. As noted above, a rich stream of literature criticises digital identity platforms, questioning th extent to which these can really serve as part of effective development policies. But this literature is largely framed in terms of access to programmes or services, showing the effects of denial of these on non-authenticated users. In terms of access is also a core debate on digital identity for development, questioning the fairness of welfare system where basic-need service provisions are traded for biometric credentials (Iazzolino, 2021; Martin & Taylor, 2021 Schoemaker et al., 2021).

We show that access is only one layer at which degeneration of digital identity platforms unfolds. Studying the Aadhaar-based PDS has uncovered two further layers, illuminating platforms' effects on programme moni toring and on the policy underpinning social protection. Even studies that raise concerns on ration dealer centred monitoring of the PDS and the inadequacy of the cash transfer policy do not centre on Aadhaar as plat form, and do not explore the link of undesired outcomes with platform properties. Notwithstanding the impor tance of the access layer, our study shows the greater depth at which digital identity platforms result into degenerative outcomes.

Our study invites the further search for alternative solutions to biometrics in social welfare. In a study of alternatives to the Aadhaar-based PDS, Allu, Deo, and Devalkar (2019) note that positive effects on leakage reduction are associated with the use of biometrics during user registration, but not to that of biometric authentication in ration shops. Khera (2018) reviews two alternatives to the Aadhaar-based PDS, both based on smart cards that, in Chhattisgarh and Tamil Nadu, have advantages including the ability to enable persons with movement difficulties – such as the elderly – to have others collecting rations for them. Hundal, Janani, and Chaudhuri (2020) compare the biometric PDS in Karnataka with the smart card system in Tamil Nadu, observing that the latter enables a digital record of transactions without incurring in exclusions from biometrics. At the same time, in a study of the smart card system in Tamil Nadu, Carswell and De Neve (2021) note the production of new information gaps occurring as smart cards ar introduced in ration shops. Illustrating degenerations of digital platforms, our study invites research on alternative that can avoid degenerative outcomes.

Overall, our focus on Aadhaar as platform has led us to illuminate how digital identity platforms change socia protection beyond the access layer. Effects in terms of monitoring and policy need study in different country con texts, to understand how digital identity platforms influence these layers.

## 7 | CONCLUSION

This study has shown how digital platforms for development can produce degenerative outcomes. Our analysis of exclusion, distortion and redirection in the Aadhaar-based PDS illuminates blind spots in our understanding of digita identity platforms, questioning in particular the positive orthodoxy behind their incorporation in social protection schemes across the developing world (Muralidharan et al., 2020).

Our study has several limitations. First, while Aadhaar is the world's largest digital identity platform, greater nuance would have been achieved by studying its effects across a larger sample of states, or across a greater number of social protection schemes. Second, further research studying degeneration can complement our study by looking deeper into the process. These efforts could also be combined with the potential of buildin process models of how degeneration unfolds more generally. Third, we focused on digital identity platforms in the light of their relation with socio-economic development. This leaves other problematic aspects of these plat forms, such as their implications for security and data protection, outside the remit of this paper. In advancing the digital platforms for development literature, such implications are yet important to study, especially in th light of the diffusion of social protection programmes that, like Aadhaar, make access conditional to the digita authentication of users.

## ACKNOWLEDGEMENTS

We would like to thank Soumyo Das and Amit Prakash for their precious contribution to data collection. Ear lier versions of this paper were presented at the Sixth Innovation in Information Infrastructures Workshop at University of Surrey, as well as in departmental seminar series at the London School of Economics and Politica Science, Ivey Business School at the University of Western Ontario, and the University of Oslo. We would lik to thank the organisers and participants in these seminars, as well as Reviewers of this paper, for the extremely valuable feedback received. This research is partly funded by the Marianne and Marcus Wallenber Foundation, MMW 2016.0078, and by the London School of Economics and Political Science.

## ENDNOTES

<sup>1</sup> https://www.privacyinternational.org/long-read/3373/kenyan-court-ruling-huduma-namba-identity-system-good-badand-lessons.

<sup>2</sup> https://uidai.gov.in/ecosystem/authentication-devices-documents/developer-section.html.

<sup>3</sup> The state of Tamil Nadu is the only Indian state which has maintained a universal system instead of moving to a targeted one. Some states. including Kerala. have preserved a minimum quantity of subsidy to the above-poverty-line (APL) keeping it so that such prices approach market rates.

<sup>4</sup> https://pdsportal.nic.in/Files/Aadhar%20seeding%20guidelines.pdf.

<sup>5</sup> Provisions under the PDS differ across states, and also between our two field sites. In Kerala, at the time of fieldwork all BPL families were entitled to the same subsidies, while in Karnataka quotas of subsidised goods increased with household size.

<sup>6</sup> https://www.thehindu.com/news/national/kerala/16000-BPL-ration-cards-to-be-cancelled/article13372215.ece.

<sup>7</sup> Reports of this problem appeared in super partes media sources, such as daily newspapers that are widely trusted as accurate sources of information. A summary of our secondary sources is provided in Appendix A

<sup>8</sup> https://thewire.in/rights/right-to-food-how-aadhaar-in-pds-is-denying-rights.

<sup>9</sup> In their study of the Aadhaar-enabled PDS in Jharkhand, Muralidharan et al. (2020) find a 10% reduction in benefits for recipients (23% of the total) who had not linked Aadhaar credentials to benefit rolls, with 3% not receiving any benefits

<sup>10</sup> https://scroll.in/article/851086/cash-transfers-for-subsidised-foodgrain-government-claims-99-success-not-so-say-33.

## DATA AVAILABILITY STATEMENT

The data that support the findings of this study are available from the corresponding author upon reasonable request.

## ORCID

Silvia Masiero https://orcid.org/0000-0002-1427-0779

## REFERENCES

Addo, A., & Senyo, P. K. (2021). Advancing E-governance for development: Digital identity and its link to socioeconomic inclusion. Government Information Quarterly (forthcoming).

Aggarwal, A. (2011). The PDS in Odisha: Against the grain? Economic & Political Weekly, 46, 21–23.

Aker, J. C., Boumnijel, R., McClelland, A., & Tierney, N. (2015). Zap it to me: The short-term impacts of a mobile cash transfe program (Working Paper 268). Washington, DC: Center for Global Development.

Allu, R., Deo, S., & Devalkar, S. K. (2019). Alternatives to Aadhaar based biometrics in the public distribution system. Eco nomic & Political Weekly, 54(12), 30–37.

Barrientos, A., & Hulme, D. (Eds.). (2016). Social protection for the poor and poorest: Concepts, policies and politics. Springer.

Bhatia, A., & Bhabha, J. (2016). India's Aadhaar scheme and the promise of inclusive social protection. Oxford Developmen Studies, 45(1), 64–79

Bhatia, A., Donger, E., & Bhabha, J. (2021). ‘Without an Aadhaar card nothing could be done’: A mixed methods study of biometric identification and birth registration for children in Varanasi, India. Information Technology for Development, 27 (1), 129–149.

Bonina, C., Koskinen, K., Eaton, B., & Gawer, A. (2021). Digital platforms for development: Foundations and research agenda Information Systems Journal.1–34.

Carswell, G., & De Neve, G. (2014). MGNREGA in Tamil Nadu: A story of success and transformation? Journal of Agraria Change, 14(4), 564–585.

Carswell, G., & De Neve, G. (2021). Transparency, exclusion and mediation: How digital and biometric technologies are transforming social protection in Tamil Nadu, India. Oxford Development Studies, 1–16

Chanchani, D. (2017). Would the people of Chhattisgarh prefer cash transfers instead of foodgrain? Economic and Politica Weekly, 52(34), 1851–1855.

Chaudhuri, B. (2021). Distant, opaque and seamful: Seeing the state through the workings of Aadhaar in India. Information Technology for Development, 27(1), 37–49

Corbridge, S., Williams, G., Srivastava, M., & Véron, R. (2005). Seeing the state: Governance and governmentality in India. Cam bridge, UK: Cambridge University Press.

De Reuver, M., Sørensen, C., & Basole, R. C. (2018). The digital platform: A research agenda. Journal of Information Technol ogy, 33(2), 124–135.

Devereux, S. (2016). Is targeting ethical? Global Social Policy, 16(2), 166–181

Devereux, S., & Sabates-Wheeler, R. (2004). Transformative social protection (Working Paper 232). Brighton, England: Insti tute of Development Studies.

Devereux, S., & Vincent, K. (2010). Using technology to deliver social protection: Exploring opportunities and risks. Develop ment in Practice, 20, 367–379.

Drèze, J., Khalid, N., Khera, R., & Somanchi, A. (2017). Aadhaar and food security in Jharkhand. Economic & Political Weekly 52(50), 51.

Drèze, J., & Khera, R. (2015). Understanding leakages in the public distribution system. Economic & Political Weekly, 50(7), 39–42.

Drèze, J., & Khera, R. (2017). Recent social security initiatives in India. World Development, 98, 555–572.

Drèze, J., & Khera, R. (2020, May 13). Getting cash transfers out of a JAM. The Hindu. Retrieved from https://www. thehindu.com/opinion/lead/getting-cash-transfers-out-of-a-jam/article31568674.ece

Eaton, B., Elaluf-Calderwood, S., Sørensen, C., & Yoo, Y. (2015). Distributed tuning of boundary resources: The case of Apple's iOS service system. MIS Quarterly, 39(1), 217–244

Eck, A., & Uebernickel, F. (2016, June). Untangling generativity: Two perspectives on unanticipated change produced by diverse actors. Paper presented at Euronean Conference of Information Systems

Gawer, A. (Ed.). (2009). Platforms, markets and innovation. Edward Elgar Publishing.

Gelb, A., & Clark, J. (2013). Performance lessons from India's universal identification program (CGD Policy Paper, 20).

Gelb, A., & Metz, A. D. (2018). Identification revolution: Can digital ID be harnessed for development?. Brookings Institution Press.

Ghazawneh, A., & Henfridsson, O. (2013). Balancing platform control and external contribution in third-party development: The boundary resources model. Information Systems Journal, 23(2), 173–192.

Government of India. (2015). Wiping every tear from every eye: The JAM Trinity number solution. Economic Survey 2015–2016 Government of India. Retrieved from http://indiabudget.nic.in/es2014-15/echapvol1-03.pd

Graham, M., Hjorth, I., & Lehdonvirta, V. (2017). Digital labour and development: Impacts of global digital labour platform and the gig economy on worker livelihoods. Transfer: European Review of Labour and Research, 23(2), 135–162

Gulati, A., & Saini, S. (2015). Leakages from Public Distribution System (PDS) and the way forward (Working Paper 294). New Delhi, India: Indian Council for Research on International Relations

Heeks, R. (2002). Information systems and developing countries: Failure, success, and local improvisations. The Informatio Society, 18(2), 101–112.

Heeks, R. (2017). Decent work and the digital gig economy: A developing country perspective on employment impacts and standards in online outsourcing, crowdwork, etc. (Development Informatics Working Paper, 71).

Heeks, R., Eskelund, K., Gomez-Morantes, J. E., Malik, F., & Nicholson, B. (2020, June 10–11). Digital labour platforms in the global south: Filling or creating institutional voids? Paper presented at IFIP 9.4 European Conference, Salford, England.

Hosein, G., & Whitley, E. A. (2019). Identity and development: Questioning Aadhaar's digital credentials. In R. Khera (Ed.) Dissent on Aadhaar: Big data meets big brother. Orient Black Swan.

Hundal, H. S., Janani, A. P., & Chaudhuri, B. (2020). A conundrum of efficiency and inclusion: Aadhaar and fair-price shops. Economic & Political Weekly, 55(14), 1–9.

Iazzolino, G. (2021). Infrastructure of compassionate repression: Making sense of biometrics in Kakuma refugee camp. Infor mation Technology for Development, 27(1), 111–128

Justice Wadhwa Committee for PDS in Karnataka. (2009). Justice Wadhwa Committee Report on PDS in Karnataka. Retrieved from https://www.techylib.com/en/view/chocolatehook/justice\_wadhwa\_committee\_on\_public\_distribution\_system pds\_karnat

Khera, R. (2011). Trends in diversion of grain from the Public Distribution System. Economic & Political Weekly, 46, 106–114.

Khera, R. (2014). Cash vs. in-kind transfers: Indian data meets theory. Food Policy, 46, 116–128

Khera, R. (2018, March 14). Smarter than Aadhaar: Govt's insistence on disruptive option is bewildering. Business Standard. Retrieved from https://www.business-standard.com/article/opinion/how-successfully-last-mile-authentication-has recorded-pds-118031301260\_1.htm

Khera, R. (2019). Dissent on Aadhaar: Big data meets big brother. Orient BlackSwan.

Koskinen, K., Bonina, C., & Eaton, B. (2018). Digital platforms in the global south: Foundations and research agenda (Working paper at DIODE network). Retrieved from https://diodeweb.files.wordpress.com/2018/10/digital-platforms-diode paper.pdf

Koskinen, K., Bonina, C., & Eaton, B. (2019). Digital platforms in the Global South: Foundations and research agenda. In International Conference on Social Implications of Computers in Developing Countries (pp. 319–330). Springer

Krishna, S. (2021). Digital identity, datafication and social justice: Understanding Aadhaar use among informal workers in south India. Information Technology for Development, 27(1), 67–90

Madon, S., Ranjini, C. R., Anantha Krishnan, R. K., & Babu, A. (2019). Can digital platforms help decentralise social assistanc programmes? Learning from the Aadhaar-enabled Fertiliser Distribution System (Working Paper Series No. 19-198).

Madon, S., & Schoemaker, E. (forthcoming). Digital identity as a platform for improving refugee management. Information Systems Journal.

Malik, F., Heeks, R., Masiero, S., & Nicholson, B. (2021). Digital labour platforms in Pakistan: Institutional voids and solidarit networks. Information Technology & People.

Martin, A. (2021). Aadhaar in a box? Legitimizing digital identity in times of crisis. Surveillance & Society, 19(1), 104–108

Martin, A., & Taylor, L. (2021). Exclusion and inclusion in identification: Regulation, displacement and data justice. Information Technology for Development, 27(1), 50–66

Masiero, S., & Das, S. (2019). Datafying anti-poverty programmes: Implications for data justice. Information, Communication & Society, 22(7), 916–933

Masiero, S., & Nicholson, B., (2020, June 10–11). Competing logics: Towards a theory of digital platforms for socio-economi development. Paper presented at IFIP 9.4 European Conference, Salford, England.

Masiero, S., & Prakash, A. (2015). The politics of anti-poverty artefacts: Lessons from the computerization of the food secu rity system in Karnataka. In Proceedings of the Seventh International Conference on Information and Communication Tech nologies and Development (pp. 1–10). ACM.

Masiero, S., & Prakash, A. (2019). ICT in social protection schemes: Deinstitutionalising subsidy-based welfare programmes. Information Technology & People, 33(4), 1255–1280.

Masiero, S., & Shakthi, S. (2020). Grappling with Aadhaar: Biometrics, social identity and the Indian state. South Asia Multi disciplinary Academic Journal, 23, 1–8.

Mir, U. B., Kar, A. K., Dwivedi, Y. K., Gupta, M. P., & Sharma, R. S. (2020). Realizing digital identity in government: Prioritizing design and implementation objectives for Aadhaar in India. Government Information Quarterly, 37(2), 101442

Mukhopadhyay, S., Bouwman, H., & Jaiswal, M. P. (2019). An open platform centric approach for scalable government service delivery to the poor: The Aadhaar case. Government Information Quarterly, 36(3), 437–448

Muralidharan, K., Niehaus, P., & Sukhtankar, S. (2020). Balancing corruption and exclusion: Incorporating Aadhaar into PDS. Ideas for India. Retrieved from https://www.ideasforindia.in/topics/poverty-inequality/balancing-corruption-and exclusion-incorporating-aadhaar-into-pds.html.

Nicholson, B., Nielsen, P., Sæbø, J., & Sahay, S. (2019). Exploring tensions of global public good platforms for development The case of DHIS2. In International Conference on Social Implications of Computers in Developing Countries (pp. 207–217) Springer.

Nielsen, P. (2017). Digital innovation: A research agenda for information systems research in developing countries. In Inter national Conference on Social Implications of Computers in Developing Countries (pp. 269–279). Springer.

Nilekani, N., & Shah, V. (2016). Rebooting India: Realizing a billion aspirations. Penguin.

Nyst, C., Makin, P., Pannifer, S., & Whitley, E. (2016). Digital identity: Issue analysis: Executive summary. Consult Hyperion.

Parker, G. G., Van Alstyne, M. W., & Choudary, S. P. (2016). Platform revolution: How networked markets are transforming the economy and how to make them work for you. WW Norton & Company.

Puri, R. (2012). Reforming the public distribution system: Lessons from Chhattisgarh. Economic & Political Weekly, 47, 21–23

Radhakrishna, R., & Subbarao, K. (1997). India's Public Distribution System: A national and international perspective. World Bank.

Raghavan. M. (2021). Transaction failure rates in the Aadhagr-enabled payment system. Dyara Research. Retrieyed from https://www.dvara.com/research/wp-content/uploads/2020/05/Transaction-failure-rates-in-the-Aadhaar-enabled Payment-System-Urgent-issues-for-consideration-and-proposed-solutions.pdf

Ramakumar, R. (2011). The unique ID project in India: A skeptical note. In International Conference on Ethics and Policy of Bio metrics (pp. 154–168). Springer.

Ramanathan, U. (2014). Biometrics use for social protection Programmes in India violating human rights of the poor. United Nations Research Institute for Social Development. Retrieved from http://www.unrisd.org/sp-hr-ramanathan

Rao, U., & Nair, V. (2019). Aadhaar: Governing with biometrics. South Asia: Journal of South Asian Studies, 42(3), 469–481.

Russpatrick, S. (2020). Understanding platform ecosystems for development: Enabling innovation in digital global public goods software platforms. In IFIP Joint Working Conference on the Future of Digital Work: The Challenge of Inequalit (pp. 148–162). Springer.

Saini, S., Sharma, S., Gulati, A., Hussain, S., & von Braun, J. (2017). Indian food and welfare schemes: Scope for digitization towards cash transfers (ZEF-Discussion Papers on Development Policy No. 241). Bonn, Germany

Schoemaker, E., Baslan, D., Pon, B., & Dell, N. (2021). Identity at the margins: Data justice and refugee experience with digital identity systems in Lebanon, Jordan, and Uganda. Information Technology for Development, 27(1), 13–36.

Singh, S. (2019). Death by digital exclusion? On faulty public distribution system in Jharkhand. The Hindu. Retrieved from https://www.thehindu.com/news/national/other-states/death-by-digital-exclusion/article28414768.ece

Suchitra, M. (2004). Undermining a fine public distribution system in Kerala. India Together. Retrieved from http://www. indiatogether.org/2004/jan/pov-keralapds.htm.

Swaminathan, M. (2002). Excluding the needy: The public provisioning of food in India. Social Scientist, 30(3-4), 34–58.

Tilson, D., Lyytinen, K., & Sørensen, C. (2010). Research commentary—Digital infrastructures: The missing IS research agenda. Information Systems Research, 21(4), 748–759.

Tiwana, A. (2013). Platform ecosystems: Aligning architecture, governance, and strategy. Newnes.

UIDAI. (2010). UIDAI strategy overview: Creating a unique identity number for every resident in India. Planning Commission Government of India

UIDAI. (2019). UIDAI Annual Report 2018-2019. Retrieved from https://uidai.gov.in/images/AADHAR\_AR\_2018\_19\_ENG approved.pdf

Umali-Deininger, D. L., & Deininger, K. W. (2001). Towards greater food security for India's poor: Balancing government intervention and private competition. Agricultural Economics, 25(2-3), 321–335

UNICEF. (2013). Every child's birth right: Inequities and trends in birth registration. United Nations Children's Fund (UNICEF).

Walsham, G. (1995). Interpretive case studies in IS research: Nature and method. European Journal of Information Systems, 4 (2), 74–81.

Weitzberg, K. (2020). Biometrics, race making, and white exceptionalism: The controversy over universal fingerprinting in Kenya. The Journal of African History, 61(1), 23–43.

Weitzberg, K., Cheesman, M., Martin, A., & Schoemaker, E. (2021). Between surveillance and recognition: Rethinking digita identity in aid. Big Data & Society, 8(1), 1–7. https://doi.org/10.1177/20539517211006744

Yoo, Y., Henfridsson, O., & Lyytinen, K. (2010). Research commentary—The new organizing logic of digital innovation: An agenda for information systems research. Information Systems Research, 21(4), 724–735

Zittrain, J. (2006). The generative internet. Harvard Law Review, 119, 1974–2040.

## AUTHOR BIOGRAPHIES

Silvia Masiero is Associate Professor of Information Systems at the Department of Informatics, University of Oslo. She has conducted extensive work on the computerisation of India's main food security programme, the Public Distribution System (PDS), and on the adoption of ICTs in core aspects of the Indian public sphere including elections, rural employment guarantees and programmes of social protection. Silvia is Secretary of the International Federation for Information Processing (IFIP) 9.4 Working Group on the Implications of Information and Digital Technologies for Development, a member of the Editorial Board at Information Technology for Development, and a Senior Editor at the Electronic Journal of Information Systems in Developing Countries.

Viktor Arvidsson is a fellow of the Information Systems and Software Engineering unit at the Department of Computer Science, Norwegian University of Science and Technology, NTNU. His research focuses on how emerging digital infrastructures and platforms affect processes of digital innovation, transformation and entrepreneurship in public and private organisations. Viktor is a member of the Editorial Board of the Journal of Strategic Information Systems.

How to cite this article: Masiero, S., & Arvidsson, V. (2021). Degenerative outcomes of digital identity platforms for development. Information Systems Journal, 1–26. https://doi.org/10.1111/isj.12351

## APPENDIX: LISTING OF MAIN SECONDARY SOURCES A.

<table><tr><td colspan="2">Public Distribution System in Kerala</td></tr><tr><td>Aadhaar-Enabled PDS in Kerala</td><td>https://epos.kerala.gov.in/</td></tr><tr><td>Kerala Food and Civil Supplies Department</td><td>https://kerala.gov.in/food-civil-supplies-department</td></tr><tr><td>Kerala Civil Supplies Corporation</td><td>http://www.supplycokerala.com/</td></tr><tr><td>Kerala state IT Mission</td><td>https://www.itmission.kerala.gov.in/</td></tr><tr><td>Akshaya - Kerala E-Governance initiative</td><td>http://www.akshaya.kerala.gov.in/</td></tr><tr><td>Justice Wadhwa Committee Report on PDS in Kerala</td><td>http://pdscvc.nic.in/PDS%20report%20of%20Kerala.doc</td></tr><tr><td colspan="2">Public Distribution System in Karnataka</td></tr><tr><td>Karnataka Food, Civil Supplies and Consumer Affairs Department</td><td>https://ahara.kar.nic.in/</td></tr><tr><td>Karnataka Food and Civil Supplies Corporation</td><td>www.kfcsc.com/</td></tr><tr><td>Justice Wadhwa Committee Report on PDS in Karnataka</td><td>https://www.prsindia.org/sites/default/files/bill_files/Justice_Wadhwa_Committee_Report_on_PDS</td></tr><tr><td>Dr R. Balasubramaniam Report on PDS in Karnataka</td><td>www.graam.org.in/wp-content/uploads/2015/11/PDS-Q-and-A-handout.pdf</td></tr><tr><td>Karnataka e-District</td><td>https://karunadu.karnataka.gov.in/edistrict/Pages/home.aspx</td></tr><tr><td>Karnataka One - Ration Card Services</td><td>https://www.karnatakaone.gov.in/Info/Public/FACSRC</td></tr><tr><td colspan="2">Public Distribution System in India</td></tr><tr><td>PDS Portal of India</td><td>https://pdsportal.nic.in/</td></tr><tr><td>Food Corporation of India</td><td>http://fci.gov.in/</td></tr><tr><td>Government of India - Department of Food and Public Distribution</td><td>https://dfpd.gov.in/index.htm</td></tr><tr><td>Right to Food Campaign</td><td>http://www.righttofoodcampaign.in/</td></tr><tr><td>Food Security Portal - India</td><td>http://www.foodsecurityportal.org/india</td></tr><tr><td>National Food Security Act</td><td>https://nfsa.gov.in/</td></tr><tr><td>India - World Food Programme</td><td>https://www.wfp.org/countries/india</td></tr><tr><td>India - Food and Agriculture Organisation</td><td>http://www.fao.org/india/en/</td></tr><tr><td colspan="2">Aadhaar-based Public Distribution System</td></tr><tr><td>Digital India Portal</td><td>www.digitalindia.gov.in/</td></tr><tr><td>Unique Identification Authority of India</td><td>https://uidai.gov.in/</td></tr><tr><td>World Bank Digital Identity (India case studies):</td><td>https://id4d.worldbank.org/research</td></tr><tr><td>Omidyar Network</td><td>www.omidyar.com</td></tr><tr><td>State of Aadhaar Report</td><td>https://stateofaadhaar.in/</td></tr><tr><td>Union Budget</td><td>www.indiabudget.gov.in/</td></tr><tr><td>e-PDS Portal of India</td><td>https://pdsportal.nic.in/main.aspx</td></tr><tr><td>GSMA Report on Aadhaar</td><td>www.gsma.com/mobilefordevelopment/wp-content/uploads/2017/03/gsmaaadhaar-report-270317.pdf</td></tr><tr><td>India Budget 2016/2017: The JAM Trinity</td><td>www.indiabudget.gov.in/budget2016-2017/es2015-16/echapvol1-03.pdf</td></tr><tr><td>Wiping Every Tear from Every Eye: The JAM Number Trinity Solution</td><td>www.indiabudget.gov.in/budget2015-2016/es2014-15/echapvol1-03.pdf</td></tr><tr><td colspan="2">Main media sources – Covering Aadhaar-based PDS</td></tr><tr><td>Times of India</td><td>http://timesofindia.indiatimes.com/</td></tr><tr><td>Indian Express</td><td>http://indianexpress.com/</td></tr><tr><td>The Hindu</td><td>www.thehindu.com/</td></tr><tr><td>Hindustan Times</td><td>www.hindustantimes.com/</td></tr><tr><td>Deccan Herald</td><td>www.deccanherald.com/</td></tr><tr><td>Business Standard</td><td>www.business-standard.com/</td></tr><tr><td>Economic and Political Weekly</td><td>www.epw.in/</td></tr><tr><td>Live Mint</td><td>www.livemint.com/</td></tr><tr><td>Scroll.in</td><td>https://scroll.in/</td></tr><tr><td>The Wire</td><td>https://thewire.in/</td></tr></table>
