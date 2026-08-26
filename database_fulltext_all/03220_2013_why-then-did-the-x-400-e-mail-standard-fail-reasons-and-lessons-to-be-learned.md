---
otero_id: 3220
otero_key: "4YATMERZ"
title: "Why Then Did the X.400 E-mail Standard Fail? Reasons and Lessons to be Learned"
authors: "Kai Jakobs"
year: "2013"
journal: "Journal of Information Technology"
doi: "10.1057/jit.2012.35"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# Why then did the X.400 e-mail standard fail? Reasons and lessons to be learned

Kai Jakobs

RWTH Aachen University, Aachen, Germany

Correspondence:

K Jakobs, RWTH Aachen University, Computer Science Department, Informatik 4, Ahornstr. 55, D-52074 Aachen, Germany.

Tel: þ 49-241-8021405;

Fax: þ 49-241-8022222;

E-mail: kai.jakobs@cs.rwth-aachen.de

## Abstract

The X.400-series of recommendations specifies the elements, protocols, and services of the e-mail system associated with the Open Systems Interconnection (OSI) protocol stack. The paper looks at the various reasons that led to X.400’s failure to gain the widely expected level of market acceptance. A brief literature review suggests that common explanations for success in a standards battle cannot explain the demise of X.400. The same holds for two popular explanations for the victory of Internet over OSI. Therefore, alternative reasons are proposed and discussed, including poor timing of the standardisation activity, inadequate first implementations, and an ill-advised paradigm shift that occurred in the cause of events. Finally, some lessons to be learned for the future are identified.

Journal of Information Technology (2013) 28, 63–73. doi:10.1057/jit.2012.35;

published online 22 January 2013

Keywords: OSI; Internet; electronic messaging; X.400; standardisation; standards wars

## Introduction and motivation

‘Whoever wishes to foresee the future must consult the past; for human events ever resemble those of preceding times.’ N. Machiavelli.

‘The disadvantage of men not knowing the past is that they do not know the present.’ G. K. Chesterton.

## Learning from history

he mere fact that five centuries lie between the above quotes hints at the wisdom they convey. Nonetheless, most historians are reluctant to try and directly transpose insights from the past to the present or future. Moreover, for a reason – in all likelihood – the two environments are very diverse, and actions or events at one particular point in time may lead to outcomes very different from those they might have yielded in a different age.

Still, I would argue that looking back in history to try and learn for the future should be possible if we do not look back over too long a period of time. In this paper I will have a closer look at developments that took place around 30 years ago. Although times clearly have changed since then, and despite the fact that the 1980s are almost prehistoric for the Internet, I feel that valuable insights can be gained by looking back. This holds particularly as the times back then and today share some similarities when it comes to networking. In the 1980s, the Open Systems Interconnection (OSI) initiative, launched by the International Organization for Standardization (ISO), set out to create a whole new communication environment from scratch. These days, the same may be said for the activities towards the Future Internet. This holds specifically for the widely popular ‘clean slate’ approach. I can only hope that its proponents at least attempted to learn something from the past in general, and from the case of OSI and X.400 in particular. Otherwise, we are bound to see the same (or similar) mistakes being made all over again.

## About standards

There are almost as many definitions of a standard as there are standards. In this paper, I will use the definition provided by ISO, according to which a standard is a document that has been established by consensus and approved by a recognized body, that provides, for common and repeated use, rules, guidelines or characteristics for activities or their results, aimed at the achievement of the optimum degree of order in a given context (ISO, 2011).

In the sector of Information and Communication Technology (ICT), compatibility standards are a sine qua non. They enable interoperability between heterogeneous systems that use, for example, different programming languages, communication protocols, and representations of information. All ICT artefacts and systems embody a considerable number of standards. For example, a recent study found that a ‘standard’ laptop incorporates over 250 of them (Biddle et al., 2010). Thus, to a considerable degree, standards shape the ICT landscape.

## About standardisation

The Commission of the European Union rightly observes that ‘Standards are not only technical questions. They determine the technology that will implement the Information Society, and consequently the way in which industry, users, consumers and administrations will benefit from it.’ (CEU, 1996). Accordingly, standardisation may be seen as an interface between technical and non-technical (e.g., economic, organisational, or social) considerations. Standards – the outcome of the standardisation process – result from a process of social interactions between stakeholders. That is, stakeholders cannot just focus on the technical merits of a particular solution, they also have to think about the economic and perhaps societal consequences of a future standard. For a manufacturer, for instance, pros and cons of joining the standardisation bandwagon vs trying to push a proprietary solution need to be considered. Standardsbased products or services may imply price wars and lower revenues, but may also open new markets and widen the customer base. Offering a proprietary solution may yield (or keep, rather) a loyal customer base, but may also result in a technological lock-in and, eventually, marginalisation. It should also be noted that not always do all stakeholders benefit from a standard. Selfishness in the form of pushing an inferior standard that will only benefit one company may also be observed, as may be the desire to prevent a competitor’s (beneficial) technology from being standardised.

The social shaping of technology (SST) approach towards studying the relation between technology and society ‘explores a range of factors – organisational, political, economic and cultural – which pattern the design and implementation of technology’ (Williams and Edge, 1996). SST observes that ‘The shaping process begins with the earliest stages of research and development’ (Williams, 1992). In the ICT sector, standards frequently represent a very early stage of development. The notion that choices can be made during the development of a technology – or a standard – is a cornerstone of the SST approach. These choices have a significant impact on the design of ICT standards. They may be based on a multitude of aspects that may be purely technical, but may also be of a societal or economic nature. Accordingly, there is a multitude of factors that potentially influence the outcome of a standardisation process, ranging from technological advances to changes in societal norms, corporate business interests, and market needs to the views and attitudes of the individuals that actually design the standard.

If we accept that we can indeed learn from history and that standards are an important shaper of ICT, then knowledge about how earlier standards emerged, why they emerged the way they did, and which factors influenced their development would allow us to predict – to a certain extent – how future technologies will look. If we also accept that standards have not just technical ramifications, but also strong economic and societal implications, then the knowledge of what shapes a standard may offer the chance to steer technological development in a way that the outcome will be beneficial to all.

This paper adopts a historiographic approach to the analysis of a consensus-based standards setting process. This approach leads to certain insights and conclusions, but can only tell part of the whole story. To get a fuller picture, the problem would also need to be analysed from other angles, using other approaches. Specifically, a social sciences approach could lead to complementary insights. Likewise, marketing theories would help shed more light on the analysis of the related problem of a battle for dominant design in the market place.

The remainder of this paper is organised as follows: after a very brief review of the literature about standards wars and related phenomena in ICT (in the section ‘Battles and wars over ICT standards – A literature recap’), some popular beliefs relating to the failure of the OSI initiative in general and X.400 in particular will be discussed in the section ‘Why did OSI fail – two popular beliefs’. The subsequent section ‘Standardising X.400’ will offer some socio-technical arguments why X.400 was bound to fail. Finally, the section ‘Summary and some lessons to be learned’ will identify some lessons that can be drawn for the future.

## Battles and wars over ICT standards – A literature recap

Standards wars have long been a popular subject in the literature, from very different perspectives. Although the topic has primarily been discussed by economists (see, e.g., Shapiro and Varian, 1999; Stango, 2004; Augereau et al., 2006), historians, social scientists, and others have also contributed.

‘Internet vs OSI’ has frequently been considered an example of a standards war (e.g., in Russell, 2006). It would thus seem to be obvious to consider X.400 vs the Internet’s Simple Mail Transfer Protocol (SMTP) as one battle that was fought in this war. Accordingly, a brief look at the analyses of some of such better known battles should yield some helpful lessons for the case at hand.

BetaMax vs Video Home System (VHS) video cassette formats, Ethernet vs Token Ring protocols for Local Area Networks (LANs), and WiFi vs various competitors in the field of Wireless LANs (WLANs) are among the best known examples of battles between competing ICT standards. Other well-studied examples here include those between two different 56k modems in the late 1990s (Augereau et al., 2006) and between browsers in the early/mid 2000s (Oshri et al., 2008). A little more recent are the cases of Blu-ray vs HD-DVD in the field of optical disks, and of the standards for document formats, OOXML and ODF (Office Open XML and Open Document Format, respectively; see (Egyedi and Koppenhol, 2010) or (Blind, 2011)).

The following brief case outlines and the subsequent discussion shall highlight some factors that have been associated with a victory in a standards war.

## - BetaMax vs VHS

Despite the ‘maturity’ of the case, scholars are still not in full agreement as to what caused the victory of the VHS format (invented and marketed by JVC), nor are they with respect to other related issues. For instance, the widely held claim (e.g., by (Cusumano et al., 1992)) that BetaMax (produced by Sony) offered superior image quality has more recently been challenged by Liebowitz and Margolis (1995). Analysing the importance of network effects, Ohashi (2003) found that it would have been possible for Beta to capture the market if it had used its first-mover advantage to build an installed base through low pricing.

Yet, many authors (e.g., Grindley (1990) and Cusumano et al. (1992)) agree that the fact that JVC’s strategy was much more open than Sony’s eventually led to the VHS victory. Sony was reluctant to be an Original Equipment Manufacturer (OEM) supplier. In contrast, JVC joined forces with partners that offered manufacturing capacity, provided access to the North American and European markets, and, most importantly, offered content.

## - Blu-ray vs HD-DVD

This case bears some resemblance to the Beta-VHS case. For one, the technologies are descendants of the VHS cassette. Sony was the main actor in both cases, and both eventual losers initially seemed to have a competitive edge – higher image resolution and built-in backward compatibility, respectively. The latter was at least an early perception. In 2007 (when players first hit the market in noticeable numbers), Brookey (2007) reported that Bluray was not backward compatible with DVDs. Indeed, according to the Blu-ray Disc Association, backward compatibility is not a requirement of the Blu-ray Disc format. Today’s Blu-ray players, however, are capable of also playing DVDs. Yet, other factors proved to be decisive. According to Gallagher (2012), this holds particularly for Sony’s superior corporate strategy, which included the provision of complementary products and, particularly, the utilisation of its technology in another Sony product, the Playstation 3. In contrast, Spark (2009) highlights the dynamic developments in the membership of the supporting consortia where some large studios changed the level of support over time or switched sides entirely. He argues that the final blow for HD-DVD came when Warner Brothers announced that it would cease its support for HD-DVD and would instead exclusively support Blu-ray. Moreover, he notes that ythose close to the deal stated that Warner Brothers received marketing support from Sony as part of the agreement. Along similar lines, Compaine and Cunningham (2010) cite lack of exclusive support by large studios as the major reason for the outcome of the battle. Moreover, in the wake of Warner Brother’s announcement, WalMart delivered another blow to HD-DVD when it announced that it would phase out HD-DVD (Cozzarin et al., 2011).

## - Ethernet vs Token Ring

Strangely, this case is hardly covered at all in the literature. This is all the more surprising as it represents one of the exceptionally few cases where one standards body, the Institute of Electrical and Electronics Engineers (IEEE), put efforts into the development of three competing standards (the third one being Token Bus, supposed to work in production environments; it never really got off the ground).

Explaining the victory of Ethernet (developed and supported by Digital Equipment Corporation (DEC), Intel, and Xerox) over its IBM-sponsored rival von Burg (2001) highlights the importance of communities and sponsor strategies for successfully establishing and improving a standard. This community, in turn, was able to innovate, produce, and extend the market at a rapid pace. On the other hand, although IBM did support the development of a standard through IEEE, its desire for market dominance frustrated potential partners. This lack of a Token Ring community meant that Ethernet’s pace of innovation could not be met, leading to an increasing price gap.

Moreover, DEC, one of the Ethernet sponsors, provided a ready market for LAN products, and Intel, another sponsor, provided the chip designing and manufacturing capacity. Together with the fact that Ethernet also became an IEEE standard (802.3) made it a ‘safe’ technology for investors and suppliers (von Burg, 2001).

## - WiFi vs HomeRF and HiperLAN

It would seem that the success factors in this case were more related to technological aspects than in the previous ones. The main reason underlying the development of the HomeRF standard (by the HomeRF Working Group (WG)) was the allegedly inadequate support for isochronous services – i.e., for telephony – by the IEEE 802.11b specification. According to Lemstra and Hayes (2009), the reason for its eventual failure was the fact that systems implementing the standard would have had to be based on a proprietary technology, as only one consortium member was developing the HomeRF physical layer in silicon. This notion is seconded by Dovev et al. (2012), who also note that many consortium members felt the dependence on this one vendor would have made the standard a proprietary system; this they considered undesirable. In contrast, several silicon vendors supported the 802.11b standard, thus quickly bringing down the prices for the chipset. Moreover, it turned out that voice services was not a market need (Jakobs et al., 2010), rendering the main reason for the HomeRF development obsolete. The different bandwidths offered by the two systems was another decisive factor. Here, the rules of the Federal Communications Committee (FCC) played a crucial role. Exploiting a – still debated – FCC ruling 802.11b-based products could offer 10Mbps bandwidth in 1999. Following another FCC ruling – which was delayed by lobbying and protests by those who had a vested interest in 802.11b – this could eventually be matched by HomeRF 2.0, but only by mid-2001. By then, however, 802.11b already dominated the market.

HiperLAN was a European development, led by the European Telecommunications Standards Institute. There were two different developments, HiperLAN/1 and /2. The former was different from the 802 specification in most respects; in fact, There was a fair bit of competitiveness w.r.t. the IEEE 802.11 work – also technology-wise (Kruys,

2007). In contrast, the specifications of the HiperLAN/2 and IEEE 802.11a modulation schemes were almost identical. Still, HiperLAN/2 was a centralised system with a focus on support of isochronous traffic (not unlike HomeRF) and Quality of Service (QoS). It was based on the Asynchronous Transfer Mode technology that was very high on the agenda around the millennium change. ‘HiperLAN/2 was never implemented because of the huge success of the IEEE b/g products after Apple announced their first sub 100\$ product in 1999. yy The fact that there was no demand for QoS from the market at the time made the demise of HiperLAN/ 2 inevitable’ (Kruys, 2007).

There is a noticeable difference between the cases of (W)LANs (and document formats) on one hand, and those of the recording media (and browsers and modems) on the other. The latter were actually battles for dominant design between technologies based on proprietary standards; they were fought in the market (for more details see, e.g., van de Kaa et al., 2011 Suarez, 2004). The former were fought between standards proper that were developed by working groups of different standards setting bodies (of course, the market and the different standards-based products played an important role in these cases as well).

Despite their general difference, the cases above also share one striking characteristic (albeit in different expressions) – the importance of having adequate alliances in place when it comes to pushing a technology or a standard in the market. In the cases of the video recording technologies, this refers primarily to the need of supporting content providers. For the local area networks, the ability to enlist – by means of openly available standards – companies with complementary capabilities and expertise proved decisive. This is indeed a lesson to be learned from history, and it seems like Sony (Blu-ray) and Intel (WiFi) have understood that. Sadly, this is of little help for the case at hand – the struggle between the different e-mail system. After all, being associated with the OSI protocols suite, X.400 enjoyed the support of pretty much all Western governments and of many large suppliers. In contrast, the Internet – including its main messaging programme, the SMTP – was initially a small US-based research network, initiated by the US Department of Defense (DoD) and developed by a smallish number of universities, research institutions, and motivated individuals.

Another aspect worth considering relates to the market relevance of a standard. A focus on services for which the market had no demand (voice, QoS) at least contributed to both HomeRF’s and HiperLAN’s demise. Along similar lines, the WLAN case demonstrates that it is may be extremely difficult for a latecomer to fight an incumbent with a large installed base, all the more so if the new technology does not offer any significant benefits (as happened to HiperLAN). Yet again, these insights do not really help explain the e-mail case. Back in 1984, SMTP did not have an installed base worth mentioning, definitely not in Europe. Neither had X.400, but at least on paper it did offer significantly more sophisticated services than SMTP, and it did meet actual market needs (interconnection of incompatible proprietary systems).

One should have thought that the outcome of this ‘war’ was very clear up-front. So, what went ‘wrong’?

In contrast to many others (e.g., (Maathuis and Smit, 2003), (Russell, 2006)), I would argue that the e-mail case was not at all an example of a standards battle, at least not initially. This is simply because of the fact that in the early stages of development, X.400 was the only combatant to be taken seriously. In fact, as we will see (in the section ‘Standardising X.400’; with the benefit of hindsight), X.400 managed to shoot itself in the foot quite effectively, thus avoiding the need for any ‘battle’.

Therefore, although the brief descriptions above illuminate that the outcome of standards battles frequently depend on the same, reoccurring elements, (initially) these elements did not play a major role in the case of e-mail. That is, accepted wisdom from earlier standards battles cannot readily be applied to the X.400 case. In the following, I will, therefore, first discuss some popular beliefs regarding the reasons behind the ‘victory’ of the Internet over OSI (of which X.400 was an integral part). Subsequently, I will focus on X.400 and will offer some explanations why X.400 never became as popular as could have been expected.

## Why did OSI fail – Two popular beliefs

Common wisdom has it that the increasing popularity of the Internet was the one reason why OSI (and thus, X.400) never made it (see, e.g., Maathuis and Smit, 2003). Another popular explanation is OSI’s alleged ‘installed base hostility’ (made by, e.g., Hanseth, 2002).

In the following, these propositions will be discussed for the OSI suite of services and protocols in general.

The standardisation process – the Internet Engineering Task Force’s (IETF’s) alleged superiority

‘The Internet killed OSI’ is a popular point of view (see, e.g., Malamud, 1992; Lehr, 1995). Moreover, there is a certain level of truth to this claim; eventually, the Internet actually did deliver the final blow to OSI.

Many factors contributed to the Internet’s success. The communication software was part of the then increasingly popular UNIX operating system, it was simple and easy to install and to maintain, and it was free. Yet, it would be too simplistic to assume that these were the only reasons. In fact, the Internet’s standards setting process has frequently been identified as a (the?) main reason behind its success (see, e.g., Rutkowski, 1994; Lehr, 1995). This process’s most important characteristics include an evolutionary design approach, the importance assigned to backward compatibility, interoperable implementations, and a considerable degree of pragmatism.

The step-by-step approach is indeed a cornerstone of the process of the IETF, the body in charge of developing the Internet standards. It aims at standardising comparably small but interoperable components, which can be combined to provide the desired functionality. Most importantly, though, a certain level of pragmatism is essential. This includes the tendency to prefer a quick solution over lengthy discussions on merits and disadvantages of different proposals and the rather relaxed attitude towards the use of external specifications. Both characteristics distinguish the IETF process from those of the ‘official’ standards bodies (e.g., ISO and the International Telecommunication Union (ITU), an international organisation within the United Nations System where governments and the private sector coordinate global telecom networks and services). Certainly in the ICT sector, these bodies exhibit a certain tendency towards ‘all-embracing’ solutions that solve all problems at once. This leads to sometimes extremely complex specifications that even large companies are hesitant to implement (because of their complexity and because they tend to solve problems that nobody ever encountered). In contrast, IETF specifications tended to be simple, and different implementations have been tested for interoperability before release of a standard.

The above is a popular and basically correct view of the IETF process. Yet, it is also overly positive – all that glitters is not gold. Over time, a few more critical accounts of the process have been published, including two documents commissioned by the IETF itself. One of them (Davies, 2004) reveals a considerable number of problems as perceived by individual WG members. The author acknowledges that many of the IETF’s problems are rooted in the unexpected and unforeseeable growth of the Internet in terms of both size and importance. The IETF has largely failed to adapt its processes to this changed environment Many of the problems and symptoms appear to be fundamentally caused by the organization failing to adapt its management and processes to its new larger size, and failing to clearly define its future mission once the initial mission had been completed or outgrown. (Davies, 2004). More specifically, he observes that the IETF process is largely built on one-to-one personal trust relationship, a very powerful model that, however, does not scale well. Furthermore, beyond personal relations, it is safe to say that the IETF’s process as such does not scale well either (Jakobs, 2003). On a related note, Davies observes that The IETF has Difficulty Handling Large and/or Complex Problems.

Moreover, several characteristics considered by many as being unique to the IETF may also be found in other standards bodies. These include, for example, the claim that ‘everyone can speak’ that can safely also be made by, for example, ISO. Moreover, being allowed to speak does not necessarily imply that everyone actually does speak or, perhaps more importantly, is actually listened to. A closely related problem is discussed in (Spring et al., 1995) – those who want to delay and possibly even obstruct the work stand a good chance of being successful; the process does not foresee any mechanisms for how to deal with such individuals: The IETF does not have a strategy for dealing effectively with an individual who is inhibiting progress, y (Davies, 2004). With roughly 10% such individuals on a typical committee (according to Spring et al., 1995), this is a potentially disastrous situation.

The popular claim that IETF’s ‘individual participation’ makes a difference is not a unique selling point either. For one, it also holds for ISO (ISO, 2012). Moreover, research from the mid-1990s shows that even back then, a sizable minority of IETF WG ‘members’ considered themselves as national/company representatives (Jakobs et al., 2001).

Despite the fact that the IETF’s step-by-step approach does indeed have its advantages, the discussion above suggests that the alleged superiority of the IETF’s standardisation process over those of other standards bodies is at least questionable. Accordingly, it may be dismissed as a valid reason for the claim that the Internet was the reason for OSI’s failure appears to be questionable.

‘Time’ is another and probably even more important aspect to be considered here. It may seem hard to believe today, but back in 1986 (when the first version of X.400 had already been 2 years old), the ‘ARPA Internet’ only comprised around 2000 hosts (just about twice the number of the UK’s academic network JANET), most of them located in the United States (Quarterman and Hoskins, 1986). Originally, the Internet was the successor to the Advanced Research Projects Agency Network (ARPANET) that had been developed under the auspices of the Advanced Research Projects Agency, a DoD agency. The ARPANET was designed for flexibility and robustness and was only used to interconnect DoD’s research contractors. Furthermore, the IETF was founded only in 1986.

OSI, on the other hand, was very much rooted in Europe, enjoyed the support of the European Commission, the US administration, and of almost all major manufacturers. The OSI Reference Model was adopted in 1984, and by the mid-1980s first implementations of the OSI protocol stack were available; most OSI standards had either already been adopted or were at least in a very stable state. It seems very unlikely that this comparably small research network in the United States and its standards should have posed any threat at that time.

## Installed base hostility

Another issue that has been raised in the literature refers to the fact that OSI failed to provide for a smooth transition from previously used networks; it had been designed without taking into account the characteristics of older networks. Any such transition requires some form of ‘jumping’. In particular, X.400 was allegedly ‘installed-base hostile’ (see, e.g., Hanseth, 2002). This claim is justified to a certain extent: X.400 was indeed ‘installed-base hostile’ in a way because of the fact that it was an integral part of the OSI initiative, and accordingly, initially required the use of underlying OSI protocols. This requirement was eventually circumvented to enable X.400 to run over Transmission Control Protocol (TCP, the Internet’s most popular transport protocol) as well. Before this, however, this strict requirement regarding the underlying communication protocols implied that a prospective user company had to install a complete OSI-based infrastructure if it wanted to employ X.400. This would have been a very costly exercise in terms of both time and money, not to mention training and related issues.

On the other hand, the originally envisioned X.400 system, as an enabler of interoperability between heterogeneous, proprietary e-mail systems, was anything but ‘installed-base hostile’. Quite the contrary, it was supposed to enable the individual proprietary elements of the said installed base to communicate. One of the individuals behind the early X.400 development, Ian Cunningham (1983) notes that Standard protocols are the glue that will connect all the individual systems into a worldwide network. Moreover, X.400 was designed to take advantage of the widely installed base of X.25 networks, which at that time represented the most widespread packet-switched network in Europe.

In summary, X.400 being part of the OSI stack implied a certain degree of installed-base hostility. This may indeed have contributed to its non-uptake. X.400 per se, however, was an enabler of interoperability between e-mail systems. Thus, installed-base hostility cannot be considered a major reason for its failure.

## Standardising X.400

Before actually attempting to answer the question why X.400 never really made it, let me first provide a bit of background on the early stages of its development.

## The initial development of X.400

In 1978, the International Federation or Information Processing (IFIP) established a WG on ‘International computer-based messaging’. IFIP is a non-governmental, non-profit, umbrella organisation for national societies working in the field of information processing. It was established in 1960 under the auspices of the UNESCO. The task of IFIP’s then newly founded WG 6.5 was to concentrate on standards for data structures, addressing, and higher level protocols to effect international computer mediated message services (Stefferud, 1979). The basic idea was to develop a system that could serve as a backbone to interconnect the increasing number of incompatible and proprietary electronic messaging services without the need for individual system-to-system gateways. IFIP’s work formed the basis for the subsequent formal standardisation work carried out within the International Telegraph and Telephone Consultative Committee (CCITT), the predecessor to the standardisation sector of today’s International Telecommunication Union (ITU-T). Later on, work on electronic messaging also commenced within ISO. Schmidt and Werle (1998) give a highly interesting account of the developments within both standards bodies towards the first X.400 series of recommendations, with some focus on what went on inside CCITT. However, the publication date of their book implies that later events, especially the nonuptake of X.400, could not be covered.

CCITT published the first X.400 series of recommendations in 1984; a much more elaborate version was published in 1988. Most of these recommendations are still in force today; the current versions date from 1999. Socie´te´ Internationale de Te´le´communications Ae´ronautiques (SITA), the air transport industry’s IT and communications arm, still uses X.400 for all operational messaging in the industry.

Pretty much in parallel with these developments work on electronic messaging was also ongoing in the realm of the Internet. A specification of network text messages was published in 1977, the initial specification for the associated transfer protocol followed in 1982. Both specifications saw various updates and extensions throughout the years, the latest versions dating from 2008.

## Early days

As stated above, IFIP’s early work on what was to become X.400 was triggered by the very real need to interconnect an array of incompatible proprietary e-mail systems. Coopersmith (2010) notes that many firms and organizations invested considerable resources developing email systems since the late 1970 s, but encountered major user resistance because of the many incompatible systems. To extend the user base and thus make e-mail service commercially viable, the individual systems had to be interconnected; this held for both corporate and public systems. Initially, dedicated gateways were used to interconnect systems. For example, in 1992, British Petroleum had 11 different systems in use throughout the Group, with some 33,000 users. All systems were interconnected via gateways, primarily on a peer-to-peer basis (Jakobs and Lenssen, 1994). Yet, such gateway-based interconnection proved to be a costly and functionally complex exercise. Accordingly, a (standards-based) backbone network was urgently needed to provide for smooth interconnectivity between the different e-mail systems. Ultimately, this need was behind the development of X.400.

It appears safe to say that X.400 was born into a very favourable environment – it could be assumed to very much simplify the interconnection of different e-mail systems, thus reducing complexity and costs, while at the same time increasing functionality (gateways cannot always map the full functionality between two systems). There were also other aspects very much in favour of a successful adoption and diffusion of X.400. For one, almost all governments and most major vendors supported OSI and thus X.400 (see, e.g., Aschenbrenner, 1986). This held despite the fact that by 1983, the ARPANET had been fully converted to the TCP/IP protocols. Moreover, and again despite the ARPANET, OSI – and thus X.400 – initially did not face any real competition from other networks. More specific to X.400, the fact that the CCITT was responsible for the standardisation activities implied that the (then) monopoly PTTs (Postal Telegraph and Telephone; the respective national entities providing postal and telecommunication services) were in charge; certainly another very favourable aspect.

## Why then did it fail?

Still, there were also a number of less favourable factors. In fact, several reasons may be identified that ‘collaborated’ in a disastrous way and – taken together – led to X.400’s failure.

First and foremost, the close integration into the OSI protocol stack was a double-edged sword. Although it created wide support, it also meant that X.400 was dependent on an extremely complex set of underlying protocols, some of which had not been fully specified at the time of the publication of its 1984 version. The same holds for the Directory Service (DS) (the ITU-T’s X.500 series of recommendations). As the name suggests, the DS was supposed to be the data networking world’s equivalent to White Pages, Yellow Pages, and directory enquiries. The DS’s availability would have contributed considerably to X.400’s user-friendliness.

More generally, the OSI set of protocols were very function-rich, designed to solve all potential communication problems from the outset (see, e.g., Egyedi, 1999; Jakobs, 2002). Such complex standards may easily lead to ambiguities through inadequate wording and/or through the introduction of optional functionalities. The latter was used extensively in the whole OSI suite. Almost inevitably, this led to implementations that fully complied with the standard, yet were not interoperable (this is a fairly common phenomenon; see, e.g., Egyedi, 2007). To at least reduce this problem, so-called profiles had to be developed. A profile specifies which options should be implemented, thus reducing the functionality of an application for the sake of interoperable implementations (Manros, 1989).

X.400’s own complexity was another related issue. The initial version from 1984 comprised seven parts requiring a total of 327 pages of description, its successor from 1988 had 580 pages in eight parts. This increase was due to the limited functionality of the 1984 version, and to improved explanations and documentations in the 1988 version.

In addition to these, more general – although important – aspects a number of other, more specific reasons may be found to explain the failure of X.400. These will be discussed below.

## Unfortunate timing

Timing was one of X.400’s major problems – in two respects. First, in the early eighties, CCITT’s work was organised in 4-year intervals, called ‘study periods’. Accordingly, their ‘Recommendations’ (read ‘standards’) were published only every 4 years, at the end of each study period; this practice was abandoned only when the ITU was restructured in 1993.

Thus, if another 4 year delay was to be avoided, something had to be published by the end of the 1980–1984 study period – regardless of its (technical) maturity. In the case of X.400, this led to the publication of rather premature specifications in 1984. Crucial parts of the specifications were extremely sketchy (e.g., the security features), or missing altogether (e.g., the message store).

Another similar, time-related problem was outside the control of CCITT. The first version of X.400 was supposed to be fully integrated into the seven-layer OSI protocol stack, as part of its top-most ‘Application Layer’. This, in turn, implied that initially the proper functioning of X.400 required a full-blown underlying OSI stack. As X.400 was the first standardised element of the OSI Application Layer, potential early adopters would have had to implement the full OSI stack for just this one, overly function-rich application (Schmidt and Werle, 1998).

To make things worse, not all necessary underlying standards had been adopted in 1984. In particular, the OSI presentation layer standard was not even fully specified by then and therefore, the 1984 version of X.400 was written to sit directly on top of the session layer (this was changed in the subsequent 1988 version, but not without considerable difficulties). This caused a further reduction of functionality in the 1984 version.

Moreover, the standards for the DS were not available in 1984 (its first version was published in 1988). It is easily conceivable that the unavailability of this service further contributed to a reduced usefulness, and user-friendliness, of X.400.

## Inadequate first implementations

Not least because of the complexity of even the incomplete initial X.400 version, early implementations were frequently incompatible. That is, it was next to impossible to exchange messages between systems from different vendors. Such inadequate first expressions of a technology are extremely dangerous.

In cases when decisions to adopt are based only on initial expressions of a technology, poor first implementations may easily deter potential early adopters, prevent any subsequent bandwagon-effect, and thus easily reduce to zero this technology’s chances of being adopted. Cowan (1992) notes that observable early benefits of a technology will outweigh all other aspects; in particular, higher benefits to be gained from a different technology at some later stage will be ignored. These benefits, in turn, cannot be identified at all because of the lack of opportunities for experimentation. It follows that the market can – and frequently will – adopt the ‘wrong’ technology (i.e., ignore the ‘right’ one) when left on its own. That is, possibly superficial, implementation-specific shortcomings that hide the system’s inherent advantages may have a devastating effect.

Furthermore, it may frequently be observed that in the absence of a sound basis for judgement and decisions, the adoption of a particular technology by just one firm may encourage others to follow. If this happens, chances again are that an inferior technology will be adopted, which may be highly useful for the initial adopter (who will have evaluated the alternatives and selected the technology that best suits his needs), but does not necessarily meet other entities’ demands. They, in turn, will then make their choices solely based on the initial adopter’s policy decision. In this case as well, little, if any, experimentation with alternative technologies or systems will occur; they will rapidly be discarded.

## Non-adaptivity

The X.400 specifications also suffered from a side-effect of the enormous speed of technical development in the ICT domain, and from the fact that these technical developments – which occurred in parallel with the X.400 standardisation process – were ignored.

Technical work on the specifications started in the midseventies. At that time, ‘dumb’ terminals, typically connected to a mini computer or a mainframe, were the prevailing end user systems. Consequently, during standardisation work, an environment was assumed that was built around this type of technology. A technical detail may serve to highlight the associated problems: the initial X.400 specifications did not include a ‘Message Store’ (MS). An MS would have allowed to store messages permanently on a local machine (and to retrieve them). Mini or mainframe computers used to run continuously (they were hardly, if ever, switched off under normal circumstances) and thus did not need a dedicated MS. Yet, the diffusion of PCs meant that more ‘intelligent’ end-user systems became available that were typically switched off at the of a working day and would, therefore, have required an MS to receive messages when the PC was switched off. Thanks to its design, adapting X.400 to this new environment was less than trivial and was not really attempted at all for quite a while.

## An ill-advised paradigm shift

Maybe even worse, X.400 suffered from a paradigm shift during its design. Initially, the work done within IFIP had aimed at interconnecting different proprietary e-mail systems through a standards-based ‘backbone’ network. This approach had been in line with the very real need of the most corporate e-mail users who had to interconnect different e-mail systems deployed at various sites or departments.

However, this changed during the course of the standardisation work. According to James White, then a CCITT Special Rapporteur on X.400, CCITT considered the backbone functionality only as a tactical goal, whereas the development of an over-arching architecture for message handling systems was seen as the strategic goal (Manros, 1989). This strategic goal implied that X.400 was to become the ubiquitous e-mail system, providing functionality to the end-user’s desktop.

In fact, in all likelihood, this shift was a crucially important contributor to X.400’s problems in the market. Here again, technical progress overtook standards development. By the mid-eighties, LAN-based e-mail systems had become the systems of choice for internal communication in virtually all organisations. Not unlike PCs, such LAN-based systems did not really fit into the assumed X.400 environment.

Taken together, these two developments – the diffusion of PCs and LANs in the mid to late eighties – rendered the strategic idea of ‘X.400 to the desktop’ virtually obsolete. In more general terms, the time span between the start of the standards setting activity and the completion of the final documents led to a missed window of opportunity. Other systems (i.e., PCs and LANs, with their own proprietary e-mail systems) had occupied the major market segment of corporate internal communication systems. Somewhat ironically, this left X.400 with the backbone market for which it had been intended in the first place, but for which it was now less suited.

## National monopolies and the standardisation process

Finally, a very different, non-technical aspect also needs to be mentioned. Although the initial specifications failed to provide for several important features, X.400 systems have always been extremely complex and hard to manage. Indeed, X.400 aimed at providing the one solution to all e-mail related problems (and then some). All voting members on CCITT committees came from (PTTs) administrations that were the (then) monopoly organisations in charge of the respective national (telephone) networks, or from equivalent organisations. Thus, it does not come as a big surprise that they did not adopt a user-friendly, gradual design, with a first specification evolving along with upcoming new requirements. Rather, they were in a position to follow a ‘take it or leave it’ approach, and design a system that clearly reflected PTTs’ ways of thought, and that met their specific needs, as opposed to those of their users. The distinction between ‘Administrative’ (ADMDs) and ‘Private Management Domains’ , as foreseen in the X.400 recommendation, is a case in point. Basically, this distinction’s major purpose was to make sure that any international traffic would be routed through – and thus charged for – ADMDs, run by the PTTs (Schmidt and Werle, 1998).

## Specific problems and general issues

A closer look at X.400’s standardisation and subsequent adoption reveals that most problems encountered were specific to this particular case. The exceptions include the ‘complexity of the standard’ and its ‘inadequate first implementations’; these are general issues that could hamper the uptake of any ICT standard. The need for an ‘integration into the OSI stack’ is a bit of a hybrid – many ICT standards need to be integrated into an ecosystem of existing standards. However, OSI was a special case in that it formed the environment into which X.400 had to fit, but was not fully available when X.400 was. Indeed, the latter contributed considerably to X.400’s problems.

‘Unfortunate Timing’ was a CCITT-specific problem; their 4-year cycle pretty much enforced the publication of a premature standard. The same holds for ‘Non-Adaptivity’. The rather lengthy standardisation process of at least 4 years should have strongly suggested the need to watch relevant technological developments and to adapt accordingly if need be. Yet, this did not happen. The ‘Ill-advised Paradigm Shift’ was another X.400-specific problem, and was in fact closely related to the problem of the ‘National Monopolies’. In the absence of any competition, the PTTs were in a position to adopt the stance that X.400 was to be the ubiquitous e-mail system.

## And the winner was yyyyy?

Despite the undeniable general need for open, vendor-, and platform-independent communication, the developers of X.400 apparently failed to realise that a system as complex as this, operating on top of an equally complex protocol stack, would be useful only for a handful of large, technically sophisticated organisations. Moreover, they apparently underestimated the growth rate of the Internet. Accordingly, X.400 became a failure in the market place even though it correctly anticipated general initial requirements.

Today, the vast majority of users deploy e-mail systems that interconnect their clients with a central server via a local area network. Most of these systems operate on top of Internet protocols. These include SMTP for message transfer, the Internet Message Access Protocol and the Post Office Protocol to enable the clients to access the mailboxes stored on the server, and Secure/Multipurpose Internet Mail Extensions to encode and encrypt messages that comprise multiple parts (e.g., text, graphics, and a video). In addition, numerous complementary standards exist. Yet, some of the functionalities provided by X.400 (which is now almost 30 years old) are still not available with SMTP. These include, among many others, notifications whether or not a message has reached its destination, or has been read by the recipient. An associated specification exists, which had been on the IETF’s ‘draft standard’ level from 2004 until early 2012, and was then updated by another RFC that is now at the ‘proposed standard’ level (RFCs – Requests for Comments, are a series of documents published by the IETF that contain technical and administrative documents about the Internet). To the best of my knowledge, neither has ever been commercially implemented and deployed.

In short – SMTP and associated protocols ‘won’, but the users did not.

As an aside – a number of stakeholders did not win either. Standardisation is a costly business. Weiss and Toyofuku (1996) estimate the development cost of the Ethernet 10BaseT standard at around \$10,000,000. The US Office of Technology Assessment (OTA) reports that y it has been estimated, for example, that the development of a major international telecommunications standard may require in the range of 1000 person-years of experience, 20 person-years of actual effort, and \$3 million (OTA, 1992). Oksala et al. (1996) report that Some have suggested that the OSI effort y may have cost the governments and corporations that contributed to its development more than half a billion dollars. None of these figures directly relates to X.400 standardisation, but they give a good idea about the costs to be associated with the development of ICT standards. Although such costs are shared by the participating organisations, it is safe to assume that the investments sunk in the standardisation, and the subsequent attempts at commercialisation and/or implementation of X.400 were quite massive.

## Summary and some lessons to be learned

There was a clear need for a standards-based electronic mail system in the late seventies/mid-eighties (and beyond). X.400 was an attempt – initiated by the CCITT – to standardise such a system, with backing from virtually all Western governments. Still, it never really got off the ground.

It has turned out that at least initially, the major reason for this failure had not been the success of the Internet (which was little more than a US research network by that time). Rather, the standards committee’s negligence with respect to technical developments, which took place in parallel with the X.400 specification work, has to be blamed. As a result, only with considerable difficulties could X.400 be integrated into the technical environment that was state-of-the-art in 1984, when its first specifications were published. To make things worse, the original idea underlying X.400, that is, to create a backbone e-mail system to interconnect the numerous proprietary systems that had hit the market, had to take a back seat to the idea of a ubiquitous e-mail system to the desktop. This further complicated integration of X.400 into existing (corporate) IT environments. In contrast, integration of the originally planned backbone would have caused comparably little problems (and might have led to a successful system).

As a consequence, we may note that – Lesson 1 – standards setting in the ICT arena, where technical developments continue to happen at a very high speed, needs an adequate level of flexibility to be able to react to outside developments that are likely to affect the system to be standardised. A second lesson – old news for some – would have to be that all-embracing, over-arching, and therefore very complex standards carry a much greater likelihood of failure than modular, extendable, and thus more flexible ones.

However, there is a caveat. Apparently, the success of a simple but working system, like Internet mail, carries the risk of the system remaining more or less at this simple level. Comparing the functionalities of X.400 and the various standards that together describe the functionality of Internet e-mail, you will still find a significant gap. Some functionality, for example, delivery notifications or gateways to other communication services, are available over the Internet, but only as non-standard, proprietary products or services (Deutsche Telekom’s ‘eBrief’ (e-letter) would be a case in point). Thus, Lesson Number 3 (which is related to Number 1) would be that also those standards that form the basis of successfully working systems need to be continuously monitored, updated if necessary, and actually be implemented. The latter should go without saying, but experience indicates that this is not necessarily the case.

Related to the above, lesson Number 4 would be to make sure that at least for communication systems standards, all necessary underlying and complementary standards are available upon publication. Although speed may sometimes be a virtue in standardisation, this is by no means always the case. In fact, this may be considered as lesson Number 5.

On a final note – the case of OSI and the Internet has frequently been portrayed as a ‘US versus Europe’ affair; American research and university communities pushed IP, while both European researchers within the computer communications field and telecom operators pushed OSI (Hanseth, 2001). More to the point, it has been said to be an example of ‘[North-American] technical prowess and business acumen versus the [European] authoritarianism of a sclerotic bureaucracy’ (Rogers and Kingsley, 2004). This may have been the case for OSI and the TCP/IP protocol suite in general. Yet, it certainly does not hold for X.400 where North-American researchers were instrumental in IFIP’s early activities, as well as for the work within CCITT (Schmidt and Werle, 1998). On the other hand, the one individual who tried to bridge the gap between SMTP and X.400 was a European (Steve Kille, then with University College London). He took the problem to the IETF and wrote the specifications necessary to interconnect the two systems. It would seem that interested individuals from the United States were heavily involved in the bureaucratic CCITT activities and Europeans in the market-driven work in the United States.

## Note

1 This is an extended and updated version of a paper entitled ‘Even Desperately Needed Standards May Fail – The Case of E-Mail’. It was published in the Proceedings of the Int. Conf. on the History of Computing and Networks, Grenoble, 2002.

## References

Aschenbrenner, J.R. (1986). Open Systems Interconnection, IBM Systems Journal 25(3-4): 369-379

Augereau, A., Greenstein, S. and Rysman, M. (2006). Coordination Versus Differentiation in a Standards War: 56K modems, The RAND Journal of Economics 37(4): 887–909.

Biddle, B., White, A. and Woods, S. (2010). How Many Standards in a Laptop? (And Other Empirical Questions), In: Beyond the Internet? Innovations for future networks and services ITU-T Kaleidoscope Academic Conference [WWW document] http://www.itu.int/dms\_pub/itu-t/opb/proc/T-PROC KALEI-2010-PDF-E.pdf (accessed 22 January 2012).

Blind, K. (2011). An Economic Analysis of Standards Competition: The example of the ISO ODF and OOXML standards, Telecommunications Policy 35(4): 373–381.

Brookey, R.A. (2007). The Format Wars: Drawing the battle lines for the next DVD, Convergence 13(2): 199–211.

CEU (1996). Communication from the Commission to the Council and the Parliament ‘Standardization and the Global Information Society: The European approach’, COM (96): 359.

Compaine, B. and Cunningham, B. (2010). Standards, Technology Adoption, and Ownership – But not all in one place, Journal of Media Economics 23(4): 187–191.

Coopersmith, J. (2010). Old Technologies Never Die, They Just Don’t Get Updated, International Journal for the History of Engineering & Technology 80(2): 166–182.

Cowan, R. (1992). High Technology and the Economics of Standardization, in M. Dierkes and U. Hoffmann (eds.) New Technologies at the Outset – Social Forces in the Shaping of Technological Innovations, Frankfurt, New York: Campus/Westview, pp. 279–300.

Cozzarin, P.P., Koo, B.W. and Lee, W. (2011). Sony’s Redemption: The Blu-Ray vs HD-DVD standards war, [WWW document] http://ssrn.com/abstract ¼ 1996793 (accessed 4 July 2012).

Cunningham, I. (1983). Message-Handling Systems and Protocols, Proceedings of the IEEE 71(12): 1425–1430.

Cusumano, M.A., Mylonadis, Y. and Rosenbloom, R.S. (1992). Strategic Maneuvering and Mass-Market Dynamics: The triumph of VHS over beta, The Business History Review 66(1): 51–94.

Davies, E. (2004). IETF Problem Statement, Request for Comments 3774 [WWW document] http://tools.ietf.org/html/rfc3774 (accessed 4 July 2012).

Dovev, L., Lechner, C. and Singh, H. (2012). Leveraging Multi-Partner Alliances in Technology-Driven Industries, in T.K. Das (ed.) Strategic Alliances for Value Creation, Charlotte: Information Age Publishing, pp. 1–23.

Egyedi, T.M. (1999). Tension between Standardization and Flexibility Revisited: A critique, in K. Jakobs and R. Williams (eds.) 1st IEEE, Conference on Standardization and Innovation in Information Technology (Aachen, Germany, 1999, Piscataway: IEEE Press, pp. 65–74.

Egyedi, T.M. (2007). Standard-Compliant, But Incompatible?!, Computer Standards & Interfaces 29(6): 605–613.

Egyedi, T.M. and Koppenhol, A. (2010). The Standards War Between ODF and OOXML: Does competition between overlapping ISO standards lead to innovation? International Journal of IT Standards and Standardization Research 8(1): 41–52.

Gallagher, S.R. (2012). The Battle of the Blue Laser DVDs: The significance of corporate strategy in standards battles, Technovation 32(2): 90–98.

Grindley, P. (1990). Winning Standards Contests: Using product standards in business strategy, Business Strategy Review 1(1): 71–84.

Hanseth, O. (2001). Gateways – Just as important as standards: How the internet won the ‘religious war’ over standards in Scandinavia. Knowledge, Technology & Policy 14(1): 71–89.

Hanseth, O. (2002). From Systems and Tools to Networks and Infrastructures – From design to cultivation, Towards a theory of ICT solutions and its design methodology implications [WWW document] http://heim.ifi.uio.no/oleha/ Publications/ib\_ISR\_3rd\_resubm2.html (accessed 23 August 2012).

ISO (2011). ISO/IEC Directives, Part 2 – Rules for the structure and drafting of International Standards, 6th edn, 2011 [WWW document] http://isotc .iso.org/livelink/livelink?func¼ll&objId¼10562502&objAction¼download (accessed 22 August 2012).

ISO (2012). ISO/IEC Directives, Part 1 – Procedures for the technical work, [WWW document] http://isotc.iso.org/livelink/livelink?func ¼ ll&objId ¼ 10563026&objAction ¼ download (accessed 22 August 2012).

Jakobs, K. (2002). A Proposal for an Alternative Standards Setting Process, IEEE Communications Magazine 40(7): 118–123.

Jakobs, K. (2003). A Closer Look at the Internet’s Standards Setting Process, in P. Isaı´as and N. Karmakar (eds.) Proceedings of the IADIS International Conference WWW/Internet, Algarve, Portugal: IADIS, 557–564.

Jakobs, K., Lemstra, W., Hayes, V., Tuch, B. and Links, C. (2010). Creating a Wireless LAN Standard: IEEE 802.11, in W. Lemstra, J. Groenewegen and V. Hayes (eds.) The Innovation Journey of WiFi, Cambridge: Cambridge University Press, pp. 53–109.

Jakobs, K. and Lenssen, K. (1994). Successful Applications of Electronic Messaging in International Organizations – Strategies, results, experiences, Report Prepared for the European Electronic Messaging Association.

Jakobs, K., Procter, R. and Williams, R. (2001). The Making of Standards – Looking inside the work groups, IEEE Communications Magazine 39(4): 102–107.

Kruys, J. (2007). Private Communication; response to a survey on the development of HiperLAN.

Lehr, W. (1995). Compatibility Standards and Interoperability: Lessons from the internet, in B. Kahin and J. Abbate (eds.) Standards Policy for Information Infrastructure, Boston: MIT Press, pp. 121–147.

Lemstra, W. and Hayes, V. (2009). License-Exempt: Wi-Fi complement to 3G, Telematics and Informatics 26(3): 227–239.

Liebowitz, S.J. and Margolis, S.E. (1995). Path Dependence, Lock-In, and History, Journal of Law, Economics and Organization 11(1): 205–226.

Maathuis, I. and Smit, W.A. (2003). The Battle between Standards: TCP/IP vs OSI victory through path dependency or by quality? in T.M. Egyedi, K. Krechmer and K. Jakobs (eds.) Proceedings 3rd International Conference on Standardization and Innovation in Information Technology, Piscataway: IEEE Press, pp. 161–176.

Malamud, C. (1992). Exploring The Internet: A Technical Travelogue, Englewood Cliffs: Prentice Hall.

Manros, C.U. (1989). The X.400 Blue Book Companion, Twickenham: Technology Appraisals.

Ohashi, H. (2003). The Role of Network Effects in the US. VCR Market, 1978-86, Journal of Economics & Management Strategy 12(4): 447–494.

Oksala, S., Rutkowski, T., Spring, M. and O’Donnel, J. (1996). The Structure of IT Standardization, StandardView 4(1): 9–22

Oshri, I., de Vries, H. and de Vries, H. (2008). Standards Battles in Open Source Software: The Case of Firefox, Basingstoke: Palgrave Macmillan.

OTA (1992). Global Standards: Building blocks for the future, OTA-TCT-512, [WWW document] www.strategicstandards.com/files/GlobalStandards.pdf (accessed 22 August 2012).

Quarterman, J.S. and Hoskins, J.C. (1986). Notable Computer Networks, Communications of the ACM 29(10): 932–971.

Rogers, J.D. and Kingsley, G. (2004). Denying Public Value: The role of the public sector in accounts of the development of the internet, Journal of Public Administration Research and Theory 14(3): 371–393.

Russell, A.L. (2006). Rough Consensus and Running Code’ and the Internet-OSI Standards War, IEEE Annals of the History of Computing 28(3): 48–61.

Rutkowski, A. (1994). Today’s Cooperative Competitive Standards Environment for Open Information and Telecommunication Networks and the Internet Standards Making Model, Presented at the Workshop on ‘Standards Development and Information Infrastructure’ [WWW document] http://ftp.sunet.se/pub/Internet-documents/isoc/pub/speeches/standardsworkshop.doc (accessed 3 July 2012).

Schmidt, S. and Werle, R. (1998). Coordinating Technology, Boston: MIT Press.

Shapiro, C. and Varian, H.R. (1999). The Art of Standards Wars, California Management Review 41(2): 9–32.

Spark, K.L. (2009). Format War, Antitrust Casualties: The Sherman act and the Blu-Ray-HD DVD format war, California Law Review 83(1): 173–228.

Spring, M.B., Grisham, C., O’Donnell, J., Skogseid, I., Snow, A., Tarr, G. and Wang, P. (1995). Improving the Standardization Process: Working with bulldogs an turtles, in B. Kahin and J. Abbate (eds.) Standards Policy for Information Infrastructure, Boston: MIT Press, pp. 220–252.

Stango, V. (2004). The Economics of Standards Wars, Review of Network Economics 3(1): 1–19.

Stefferud, E. (1979). March 1979 IFIP Working Group 6.5 Workshop Report, [WWW document] http://gopherproxy.meulie.net/gopher.std.com/00 The%20Online%20Book%20Initiative/Networking/archives/msggroup/ msggroup.1520-z (accessed 26 June 2012).

Suarez, F.F. (2004). Battles for Technological Dominance: An integrative framework, Research Policy 33(2): 271–286.

van de Kaa, G., van den Ende, J., de Vries, H.J. and van Heck, E. (2011). Factors for Winning Interface Format Battles: A review and synthesis of the literature, Technological Forecasting & Social Change 78(8): 1397-1411.

von Burg, U. (2001). The Triumph of Ethernet: Technological Communities and the Battle for the LAN Standard, Stanford: Stanford University Press.

Weiss, M.B.H. and Toyofuku, T.T. (1996). Free-Ridership in the Standards Setting Process: The case of 10baseT, StandardView 4(4): 205–212.

Williams, R. (1992). The Social Shaping of Technology: Research concepts and findings in Great Britain, in M. Dierkes and U. Hoffmann (eds.) New Technologies at the Outset – Social Forces in the Shaping of Technological Innovations, Frankfurt, New York: Campus/Westview.

Williams, R. and Edge, D. (1996). The Social Shaping of Technology, Research Policy 25(6): 865–899.

## About the author

Kai Jakobs joined RWTH Aachen University’s Computer Science Department as a member of technical staff in 1985. Since 1987, he has been Head of Technical Staff at the Chair of Communication & Distributed Systems. He holds a Ph.D. in Computer Science from the University of Edinburgh, and is a Certified Standards Professional.

Kai is also the Vice President of the European Academy for Standardisation. Accordingly, his research interests and activities focus on various aspects of ICT standards and the underlying standardisation process; he has published quite extensively in this field. He has also been on the programme committee and editorial board of numerous international conferences and journals, respectively, and has served as an external expert on evaluation panels of various R&D programmes, on both technical and socio-economic issues.

Copyright of Journal of Information Technology (Palgrave Macmillan) is the property of Palgrave Macmillan Ltd. and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
