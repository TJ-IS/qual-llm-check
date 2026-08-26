---
otero_id: 6792
otero_key: "K3273MZD"
title: "IT to Support Knowledge Sharing in Communities, towards a Social Capital Analysis"
authors: "Marleen Huysman; Volker Wulf"
year: "2006"
journal: "Journal of Information Technology"
doi: "10.1057/palgrave.jit.2000053"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Research article

# IT to support knowledge sharing in communities, towards a social capital analysis

Marleen Huysman<sup>1</sup>, Volker Wulf<sup>2,3</sup>

<sup>1</sup>Vrije Universiteit Amsterdam, Amsterdam, The Netherlands;

<sup>2</sup>University of Siegen, Siegen, Germany;

<sup>3</sup>Fraunhofer FIT, Siegen, Germany

Correspondence: M Huysman, Vrije Universiteit Amsterdam, De Boelelaan 1105, 1081 HV Amsterdam, The Netherlands. Tel: þ 31205986062; Fax: þ 31205986005;

E-mail: mhuysman@feweb.vu.nl

## Abstract

Ignoring the informal, non-canonical nature of knowledge sharing, including people’s motivation, ability and opportunity to share knowledge, is one of the key causes of resistance to use knowledge-sharing tools. In order to improve knowledge sharing supported by information technology (IT), tools need to be embedded in the social networks of which it is part. This has implications for our knowledge on the design requirements of such socially embedded IT. The paper reviews tools that are designed for the purpose to foster social capital. We will then discuss what is needed for an IS design theory related to knowledge communities and how such a theory could incorporate social capital theory.

Journal of Information Technology (2006) 21, 40–51. doi:10.1057/palgrave.jit.2000053 Published online 4 October 2005

Keywords: knowledge management; communities; requirement analysis; social capital; socio-technical design

## Introduction

A <sup>lthough</sup> <sup>the</sup> <sup>need</sup> <sup>to</sup> <sup>manage</sup> <sup>knowledge</sup> <sup>has</sup> <sup>always</sup>been around, lately the label ‘Knowledge management (KM)’ has attracted both practitioners and scholars in the field of organizations and information technology (IT). This popularity of the concept is not only a result of the growing recognition of the value of knowledge work and the increased IT possibilities, but also because of the increasing complexity of work and speed at which changes take place. Changing organizational boundaries and identities as well as the growth of virtual organizations, teleworkers and geographically dispersed teams, increases the difficulty of monitoring and controlling knowledge. As a result, organizations, especially larger ones, try hard to manage knowledge. This urge to get a grip on knowledge and to leverage it to create competitive advantage constitutes an important topic for discussion among practitioners and theorists alike.

However, the currently accepted or most generally discussed and practiced way of coping with knowledge meets with resistance at various levels. Most tools designed to support knowledge sharing, do not become institutionalized within organizations. Practice has shown the negative consequences of using a managerial, individual and technology oriented perceptive only (e.g. Davenport and Prusak, 1998; Huysman and de Wit, 2002). More and more, KM initiatives are directed towards more informal knowledge-sharing activities within communities of practice. Until so far however, this transition from a first to a second generation of KM (Huysman and de Wit, 2002) only sporadically find acceptance within the field of IT.

Most of the literature related to design requirements for KM systems concentrates mainly on formal modelling and analysis of formal knowledge requirements (e.g. Holsapple, 2003). Furthermore, these tools are mainly designed to support acquisition and retrieval of codified knowledge in order to improve formal individual knowledge bases. Surprisingly less is written about IT to support the so-called ‘second generation of KM’ where the focus is on informal emergent knowledge sharing within communities.

In this paper, we will explore what is needed in terms of requirement analysis to design or evaluate tools intended to support the informal knowledge-sharing needs of collectives, and in particular of communities of practice. While usually requirement analysis is conducted to support workrelated tasks of individuals or formal coordination tasks of teams (typically the field of CSCW, HCI and CMC studies), in case of communities the focus is on emergent knowledge processes (Markus et al., 2002). In this paper, we will take the position that requirement analysis for knowledgesharing communities needs to take into account the social capital of the group.

Although literature on (online) communities is growing, we still do not have a theory about the IS requirements for communities that are geographically dislocated and need technologies to connect. Such a theory is needed since existing theories on IS requirement do not take into account the emergent collective learning processes that typify distributed professional communities (Markus et al., 2002). In other words, what is needed is ‘a kernel theory underlying IS design theory’ (Walls et al., 1992) related to knowledge communities. Markus et al. (2002) have set a first important step in this direction by introducing guidelines for designing and deploying systems that support emergent knowledge processes. They do not, however, focus on social capital as a specific requirement for knowledge sharing in informal organizational settings such as in (online) communities. Social capital resides in the fabric of relationships between individuals and in individual’s connections with their communities (Wasko and Faraj, 2005, citing Putnam, 1995). Theories on social capital help explain what bind and bond (and blind) members of a community. It is our believe that an analysis of such conditions will contribute to better alignment between IT applications and knowledge-sharing needs of (online) communities.

The concept of social capital has lately been adopted within the discipline of KM (Nahapiet and Ghoshal, 1998; Lesser, 2000; Cohen and Prusak, 2001; Adler and Kwon, 2002) and IT (Kumar et al., 1998; Resnick, 2001; Wellman et al., 2001; Preece, 2002; Huysman and Wulf, 2004a, b; Wasko and Faraj, 2005) and is often approached as consisting of three dimensions: a structural opportunity, a cognitive ability and a relational motivation dimension (Huysman, 2004). It has been argued that these dimensions influence the appropriation of IT (Newell et al., 2001). For example, it is expected that distributed communities with a high cognitive ability (e.g. a shared frame of reference) and motivated to share knowledge (e.g. a shared purpose), but with low structural opportunities to do so (e.g. a sparse network) will be in need for communication tools and over time increase the level of density of ties (Brown and Duguid, 2001). Also, it is expected that the variance of these dimensions provide insight into possible IT support. For example, members who are individually motivated to contribute to the community might use reputation systems more than those members whose motivation is more collectively oriented.

The paper starts with a discussion of some of the problems that are related to the so-called ‘first generation of KM’ (Huysman and de Wit, 2002). This critical review of KM initiatives and tools provides the starting point for the argument to include an analysis of existing social capital in order to introduce tools that are more socially embedded within the social system of which it forms part. We will review existing applications that are believed to support social capital. We will argue that these tools mainly support the structural dimension of social capital. We will then discuss the possibilities of a more integrative perspective on social capital in order to align better the technology with (online) communities.

## KM fallacies

Past case study research based on in-depth analysis of various KM initiatives in large organizations have illustrated that the practice of KM is characterized by many fallacies. Several of these fallacies or traps influences directly the (perceived) functionality of IT applications for the support of KM initiatives (Huysman and de Wit, 2002).<sup>1</sup> These fallacies relate to the tendency of organizations to concentrate too much on the role of IT in facilitating knowledge-sharing, resulting in the ‘IT trap’, on imposing managerial needs upon knowledge-sharing, resulting in the ‘management trap’, and on individual learning as the purpose of knowledge sharing, resulting in the individual learning trap’. Below, these KM fallacies will be discussed.

The tendency to perceive IT as independent from its social environment has caused disappointing acceptance rates. It is not the technology itself but the way people use it that determines the role of IT in supporting knowledge sharing. In the words of Zack and McKenny: ‘y the strategic advantage associated with these technologies will not derive from having the technical skills to evaluate and implement communication technologies (or even be first mover), but rather will come from having the appropriate social context, norms, politics, reward systems and leadership to take advantage of electronic communication technology’ (Zack and McKenny, 2000: 212).

The tendency to de-contextualize IT also feeds to the assumption that all knowledge can be transformed into data and stored into systems. Echoes from the legacy of the information-management era resound here. When knowledge is saved in a system it becomes explicit, codified knowledge (Zack, 1999). Knowledge usually has a large tacit dimension and appears to be difficult to be stored in a system. In case of implicit knowledge, the human being is both the knowledge carrier and the vehicle through with the knowledge is passed on.

Next to the producer, the potential consumer of knowledge might also create pockets of resistance to using IT tools for knowledge-sharing. Knowledge only has meaning if it can be related to people (Brown and Duguid, 2000). People want to know from whom they learn as this provides important ‘meta-knowledge’. This is one of the reasons why recorded knowledge is often not re-used (Davenport and Prusak, 1998). Aids to knowledge sharing such as Intranets and knowledge bases that are geared towards codifying knowledge are not effective enough. When sharing experiences, people prefer to look for support from personal networks rather than from electronic networks to gain knowledge about the knowledge. Such ‘metaknowledge’ cannot be recorded in technical networks and requires the support of social personal networks. In that case, tacit knowledge does not need to be transformed into explicit knowledge in order to share it with others. What seems more promising is the support of social networks and knowledge connections to enable transfer (Davenport and Prusak, 1998; Leonard and Sensiper, 1998; Huysman and de Wit, 2002).

Another fallacy of many KM initiatives is caused by the dominance of a management bias. Most initiatives are born out of a managerial need to control and monitor knowledge that in some places is perceived by management as too sticky and at other places too leaky (Brown and Duguid, 2000). The growing importance of workers expertise, mobility, professionalism, etc. trigger managers to think of ways to extract and collect knowledge and make it assessable to others. The need to improve the efficiency of knowledge sharing is further stimulated by the growing awareness of the financial-economic importance of knowledge. Many publications illustrate that the firm’s intellectual capital is usually worth much more than its intrinsic value and that core competences and competitive ability are embedded in the knowledge of organization’s members (Edvinsson and Malone, 1997; Stewart, 1997; Sveiby, 1997; Roos et al., 1998; Bontis, 1999). This managerial bias tends to overshadow the perceived added value of those people who are asked to share their knowledge. Clearly, this tendency is risky as management fully depends on the active involvement of workers to share their knowledge. For successful KM, it is necessary that the initiative is beneficial both to the organization as to the knowledge worker.

A third characteristic of many KM initiatives that limits their chances to succeed is the tendency to focus on the individual ignoring the level of the group. Most initiatives concentrate on the knowledge exchange between individuals, assuming that knowledge is in the head of the individual and needs to be exchanged. In order to enhance this support of knowledge collection and provision, repository systems, such as knowledge base systems, are introduced. However, tools to capture and disseminate knowledge are mainly helpful in supporting exchange of individual knowledge but not so much in the exchange of social or community knowledge (Zack, 1999). The same is true for tools that are introduced to support the flow of knowledge between individuals, such as Intranets. In all these cases, the assumption is that knowledge can be decoupled from the social environment in which it is developed. Obviously, the negative consequences of such a focus on the individual as the main source of knowledge is ignoring the socially situated nature of knowledge (Brown and Duguid, 2000). To support collective learning such as community learning, KM initiatives need to acknowledge that knowledge is socially situated and cannot be uncoupled from the social community of which it is part.

In sum, the history of KM initiatives and technical applications has demonstrated problems of implementation characterized by a management bias, a technology push and an individual learning perspective. Some authors refer to this approach as the first wave, stage or generation of KM (e.g. Ackerman et al., 2003; Huysman and de Wit, 2002). According to these authors, the second wave or generation of KM concentrates more on the collective emergent nature of knowledge sharing. What is typical for this generation is that the role of IT to support knowledge sharing in such an informal situation has been downplayed. This can be seen as problematic since supporting knowledge sharing by technologies remains needed and is essential in case of online communities.

Taking the legacies of this first generation of KM seriously, the design of knowledge-sharing tools needs to take the following into account:

1. Avoiding the IT trap implies that ‘information systems aimed at KM need to maintain the integrity of the social communities in which knowledge is embedded’ (Boland and Tenkasi, 1995). This requires the introduction of socially embedded technologies.

2. Avoiding the management trap suggests the introduction of systems that corresponds to the actual needs and requirements of knowledge workers to share knowledge rather than those of management. This implies in-depth analysis of the social nature of a community in order to understand how and why community members share knowledge.

3. Avoiding the individual learning trap requires tools that support social relationships and communities rather than introducing knowledge repository systems and Intranets that are designed to support knowledge storage and retrieval.

Together, these assumptions create the foundation of socially embedded knowledge-sharing tools. To be clear, such socially embedded tools will not solve all fallacies related to KM. The tendency of organizations and management today to equate development of knowledge or organizational learning with a step forward in the direction towards improving intelligence, also referred to as the improvement bias in the literature on organizational learning (Huysman, 2000), is a fallacy that will not be solved by a socio-technical design. Nor will socio-technical requirement analysis challenge the overall harmonious bias (Huysman, 2000) that characterizes the debates surrounding the topics such as communities of practice, KM and the learning organization. The overall harmonious image that is present in the literature on the knowledge-based view of the firm seem to dominate already for some decades debates related to knowledge and control, power and control (Huysman, 2000). In fact, the dominance of a communitarian view in which unity and collectivism is emphasized at the expense of power and conflict (Etzioni, 1995), also applies to this paper. However, we fully agree with representatives of the conflict perspective on social capital and communities such as Bourdieu (1986) that communities reveal dysfunctional behaviour within tight-knit social networks, evolving into power coalitions. Uzzi (1997) calls such ambivalent effect of communities the ‘paradox of embeddedness’. We therefore think it is important to note at the beginning of the paper, that tools to support communities, might indeed reinforce such dysfunctional behaviour. In the remaining part of this paper, we will refer to these assumptions as basic requirements for tools in the second generation of KM. We will analyse what the implications of such tools are in terms of requirement analysis. To do this, we first review existing socio-technical approaches to system design followed by a discussion of the possibilities of using IT to support social capital by means of a literature review. The paper ends with discussing potentials for requirement analysis based on the theory of social capital as the key ingredient for knowledge sharing in the second generation of KM.

## Socio-technical approaches to IT design

With the development of network technology along with the requirement for second-generation KM, two fields of interest are increasingly in need to converge towards each other: social networks and electronic networks. Practice shows that electronic networks such as intranets cannot strive without a corresponding and co-existing social network (e.g. Blanchard and Horan, 1998; Wellman, 2000). Converging the social with the technical is originally the domain of the socio-technique (Clegg, 2000). Within the field of IT research, socio-technical studies usually focus on the continuous interactions between IT, people, the organizational context and the negotiation taking place during the design, implementation and use of IT. The theory is very broad and covers various research approaches, such as Actor Network Theory (e.g, Walsham, 1997), Soft system methodology (Checkland, 1999), Parti cipative methods (Wulf and Rohde, 1995; Mumford, 2003) Social Constructivism (Bijker et al., 1987; MacKenzie and Wajcman, 1999) Hermeneutics (e.g. Boland, 1991) Structuration theory (e.g. Orlikowski and Robey, 1991), Activity Theory (e.g. Kuutti, 1991), Adaptive Structuration theory (De Sanctis and Poole, 1994). Some researchers reveal the interdependency of social and electronic networks, for example, by concentrating on the sociology of networking (Wellman et al., 2001) using a practice lens when studying the use of networks (Orlikowski, 2000), by introducing a value-added model for design (Choo et al., 2000), by analysing the information ecology of the organization before introducing intranets (Davenport, 1997) or by stressing the process of appropriation and drifting (De Sanctis and Poole, 1994; Ciborra, 1996; Pipek and Wulf, 1999). All these and other researchers argue that the acceptance and use of e-networks highly depend on the degree to which the social aspects are taken into account. Because e-network applications usually have a high degree of interpretive flexibility (Bijker et al., 1987), researchers agree that the design, implementation and use are subject of a continuous socio-technical negotiation in order to appropriate the technology to the personal needs (Choo et al., 2000). Ciborra (1996) refers to ‘drifting’, the tendency of network technology to follow its own path over time as a result of unplanned and context based usage. These ideas of drifting and appropriation already stress the importance of taking the functional requirements of the group seriously in designing networks. Ciborra (1996) pleads for openness, care taking and hospitality when introducing groupware.

Several authors advocate a more anthropological or ethnographic perspective on the design and use of such network tools (Brown and Duguid, 2000). The aim of ethnographic studies is to carry out detailed observations of work practices and processes in their natural settings. In fact, the most common methodology used in the field of computer supportive cooperative work (CSCW) derives from ethnography, building on the notion that work environments are idiosyncratic group cultures with a distinct practice (e.g. Hughes et al., 1994; Shapiro, 1994; Jordan, 1996). A frequently addressed complain of such ethnographic studies is the gap between the empirical findings and corresponding design constraints and requirements of the application. One reason for this gap is that ethnographers do not develop the applications themselves (Ehrlich and Cash, 1994) while translating the inherently descriptive nature into technical requirements is very complicated. Several techniques have been offered to circumvent these complicated issues, such as the use of video’s and photo’s, use of checklists and the use of multidisciplinary design teams (see Ehrlich, 2000). Although highly valuable, effective means of translating ethnographic studies into design requirements are not enough to match knowledge-sharing tools with social networks. It seems that present socio-technical models used to study the interplay between IT and the social system are not yet appropriately adapted to the special requirements of electronic knowledge-sharing tools.

The need to include social requirement analysis for electronic tools to support knowledge sharing, has been brought in relation to the concept of ‘info-culture analysis’, as first introduced by Bressand and Distler (1995). Some researchers have argued that the disappointed results of knowledge-sharing tools such as intranets are due to the fact that designers traditionally analyze the infra-structure and info-structure, but neglect the underlying info-culture (Ciborra, 1996; Choo et al., 2000). Infra-structure relates to the hardware/software that enables the physical/communicational contact between network members. The infostructure relates to the formal rules governing the exchange between actors in the network. The info-culture relates to the stock of background knowledge actors take for granted and is embedded in the social relationships surrounding work group processes.

Introducing networks, based only on an analysis of the infra-structure, would result in a technology-driven implementation of these networks. The limitation of this technology driven approach has been accepted years ago. Infrastructure analysis has been succeeded by an approach that also analyses the info-structure. In terms of knowledge sharing and knowledge based systems or networks, infostructure analysis implies examining, for example, formal business processes, hierarchies, coordination rules, knowledge-sharing strategies (Choo et al., 2000). Info-structure analysis relates to the canonical knowledge-sharing processes. Without being more specific, various authors stress the need for an additional info-cultural analysis when designing knowledge networks like intranets (Ciborra, 1996; Kumar et al., 1998; Choo et al., 2000).

Including an analysis of the information culture or ‘infoculture’ of a social group corresponds to what Kumar et al. (1998) refer to as ‘the third rationality of IT’. Their research on the merchants of Prato inspired these authors to argue that traditional IT development approaches need to be augmented with additional strategies which, as a precursor to development, examine the existing patterns of culture, relationships, and trust (or distrust) in the development situation, and take them into account for devising a development and implementation strategy. This third rationality introduces social capital as the key concept.

Literature on IT and KM has not yet analysed in more detail what it means to include these various layers of development in the knowledge requirement analysis of KM tools. Below we will explore the potentials of using the ideas taken from the field of social capital to improve the knowledge requirement analysis.

## The concept of social capital in relation to KM

The notion of ‘social capital’ is an additional ingredient to the already well-known economic conditions or elements that make up organizational capital: physical capital, financial capital and human capital. Where human capital refers to individual ability (Becker, 1964), social capital refers to collective abilities derived from social networks (for a detailed review of the concept of social capital see Huysman and Wulf, 2004a, b). The ‘traditional’ types of capital determine only partially the process of economic growth and overlook the way in which the economic actors interact and organize themselves to potentially generate growth and development. Increasingly, it becomes accepted that the missing link is ‘social capital’. As usual with emerging new concepts, every contribution to this growing literature on social capital seems to use its own definition.

Several authors have expressed the importance of acknowledging social capital when investing in KM (e.g. Lesser, 2000) as well as the knowledge benefits derived from high levels of social capital (Nahapiet and Ghoshal, 1998; Cohen and Prusak, 2001).

A focus on social capital in relation to knowledge sharing shifts the attention from individuals sharing knowledge to communities as knowledge-sharing entities. Communities and social networks are seen as the prime source of a sense of membership and commitment, the source of mutuality and trust and the places in organizations where people feel most at home and most responsible for one another (Wenger, 1998). Investing in social capital thus implies a more dominant role for communities (e.g. Snyder and Wenger, 2000). In communities, people not only invest in their own learning but also in the learning of others. Therefore, next to shared practice, the driving forces within communities and the key conditions that help communities stay active are mutual trust, a sense of mutuality and recognition by peers (Lesser, 2000); in other words, a high degree of social capital.

Emphasizing social capital as the key ingredient to knowledge sharing not only relaxes the individual learning bias, but also the managerial and technological bias. By scrutinizing communities’ degree of social capital and by improving the level of social capital, tools for knowledge sharing will likely be more in line with people’s opportunities, motivation and ability to share knowledge. Community members will be more inclined to use IT if they are motivated to share knowledge with others, if they are able to share knowledge and if they have the opportunity to share knowledge (Wasko and Faraj, 2005). These three key aspects of knowledge sharing are considered key ingredients of social capital (Nahapiet and Ghoshal, 1998; Adler and Kwon, 2002). The structural dimension refers to network ties, network configurations and organization, the cognitive dimension to shared codes, narratives and language and the relational dimension to shared trust, norms, obligations, identification.

Adler and Kwon (2002) in their review article, also introduce a three-dimensional framework, in which they use the classification of opportunity, ability and motivation. Given the similarity with Nahapiet and Ghoshal’s classification, it is striking to note that they do not refer to this oftencited article. In Table 1 the two classifications are brought in line with each other.

Both the opportunity and structural dimension refer to analysis of ‘who’ shares knowledge and ‘how’ they do that. It concerns the existing or lacking opportunity to connect with each other. These aspects can be analysed on the level of the infra-structure. In combination, the two dimensions refer to the ‘structural opportunity’ dimension.

Both the cognitive and the ability dimension correspond to analysis of ‘what’ is shared. This ‘cognitive ability’ dimension concerns the ability to cognitively connect with each other in order to understand what the other is referring to when communicating. Analysing the infostructure will provide information about this cognitive ability.

The relational and the motivational dimension both refer to the question ‘why’ and ‘when’ people share knowledge. It concerns the motivation to share knowledge based on socially attributed characteristics of the relationship, such as trust, mutual respect and generalized reciprocity (Putnam, 1995). Analysis of the info-culture of the system will provide more insight into this ‘relation-based motivation’ to share knowledge.

Table 1 Conditions for knowledge sharing and knowledge requirement analysis

<table><tr><td>Knowledge sharing research questions</td><td>Who shares knowledge and how is knowledge shared?</td><td>What knowledge is shared?</td><td>Why and when is knowledge shared?</td></tr><tr><td>Dimensions (Nahapiet and Ghoshal, 1998)</td><td>Structural dimension</td><td>Cognitive dimension</td><td>Relational dimension</td></tr><tr><td>Social capital sources (Adler and Kwon, 2002)</td><td>Opportunity</td><td>Ability</td><td>Motivation</td></tr><tr><td>Content</td><td>Network ties, configuration, organization</td><td>Shared codes, language, stories</td><td>Trust, norms, obligation, identification, respect, generalized reciprocity</td></tr><tr><td>Layers of requirement analysis</td><td>Infrastructure</td><td>Infrastructure</td><td>Infoculture</td></tr><tr><td>Conditions for knowledge sharing</td><td>Structural opportunity to share knowledge</td><td>Cognitive ability to share knowledge</td><td>Relation-based motivation to share knowledge</td></tr></table>

Before discussing how social capital can be part of IS requirement analysis, we first provide a review of the literature on IT and the support of social capital. The structure of Table 1 is used to organize this review.

## Knowledge-sharing tools to support social capital

Most of the research on social capital is conducted by either social, political, economic or organization scientists. Although the topic has started to be addressed from scholars interested in the design of IT (e.g. Lesser and Cothrel, 2001; Resnick, 2001; Preece, 2002; Huysman and Wulf, 2004a, b), it has not gained comparable attention. The still limited interest in the topic from the side of IT scholars is surprising as the growth in attention in (knowledge intense) networks within and between organizations makes research into the relationship between IT and social capital more important. Referring to the development of IT, one has to ask how to design specific functionality to support social capital.

There are quite some IT applications that have the potential to augment social capital among human actors by providing an infra-structure for establishing, maintaining or intensifying relationships in communities. Of course, the actual impact of these applications on social capital is subject to their appropriation in a specific social context. Cohen and Prusak (2001) hinted already to the importance of the social context when stating that it is not so much the technology that brings people together as it is the existing social capital. Since we believe that the appropriation of IT is grounded in a complex inter-relation between the technological artefacts and their social context, it is however illustrative to give a survey on existing IT systems that may have an impact on social capital.

In the following, we discuss these design approaches with regard to the different aspects of social capital they could support. We focus on functionality and applications developed within the spirit of the second generation of KM to discuss how the structural opportunity, the cognitive ability, and the relational motivation dimensions of social capital can be supported by technical means.

## Structural opportunity dimension

The structural dimension of social capital focuses mainly on the density of networks and on bridging structural holes (Burt, 1992; Wasserman and Faust, 1994). Density of a network refers to the extent to which actors of a network are interconnected. Studying the density of a social network would reveal with whom people share knowledge. Next to who communicates with who, attention is also paid to the question how they do that. Connecting to people in order to share knowledge brings an instrumental perspective to the fore. Different networks tools exist that support peoples opportunity to connect with each other.

A large part of the functionality of IT applications developed so far focus on the structural aspect of social capital. These functionalities provide a technological infra-structure to allow human actors to find, to communicate, or to cooperate with each other. They offer opportunities and infra-structures to share knowledge through network ties.

There are applications that are designed to promote social capital in overcoming spatial or temporal boundaries by making users aware of each other or of artefacts others have created. Among the systems that bridge spatial and temporal boundaries, topic- and member-centered communication spaces are classical examples. Member-centred communication spaces, such as the Bubble or Loops system presented by Ackerman and Halverson (2004), maintain or foster social ties in an already well-defined community. Topic-centered communication spaces, such as news groups, allow people who are in the beginning not necessarily known to each other to exchange ideas or find solutions to problems.

Beyond pure communication, applications may foster the structural dimension of social capital by offering virtual spaces that allow the creation, development and storage of topic-centered materials. These repositories of materials are typically augmented with communication and annotation functionality (cf. Buckingham, 1997; Pipek and Won, 2002; Stahl, 2004).

The systems discussed so far offer places in the virtual space where human actors can direct themselves to, strengthen existing social ties, or build up new ones. In another class of applications, the system takes a more active role in suggesting actors to establish or to refresh relations. Such applications require personal data of the different human actors and domain-specific algorithms to match human actors appropriately. Several expert recommender systems have been designed to support the finding of human actors (cf. Yiman-Seid and Kobsa, 2003). Systems like Who Knows (Streeter and Lochman, 1988), the Referral Web (Kautz et al., 1997a, b), Yenta (Foner, 1997), or MII Expert Finder and XperNet (Maybury et al., 2003) are designed to extract personal data about human interests automatically from documents that were created by the actors. Ogata et al. (2001) have built a system to facilitate finding a person to collaborate with. The system mines and analyses email exchanges among individuals based on a speech act model of communication. Vivacqua and Lieberman (2000) have developed a system which extracts personal data concerning a programmer’s skill from the Java code the programmer has produced. Based on these types of personal data, the recommender systems allow to match actors. However, each system has hitherto dealt with specific matching algorithms for one type of personal data. McDonald (2000) and Becks et al. (2004) have developed frameworks that allows matching human actors based on a variety of different types of personal data.

While recommender systems apply personal data for automatic matchmaking, awareness features capture selected activities of individual actors and make them visible to their cooperation partners. Awareness features are typically built for groups that contain a high level of social capital and cooperate intensely. However, awareness data and the resulting histories of interaction can also be applied to match people who are not yet well known to each other. For instance, the Social Web Cockpit provides awareness data that informs users about the presence of other users at a site of interest. Moreover, it allows for collaborative content rating and recommendation functionalities (Gra¨ther and Prinz, 2001). Won and Pipek (2003) suggest collecting data about those computer-supported activities of users that are indications for their personal expertise. After different steps of aggregation, their Expertise Awareness mechanism supports finding of human actors who possess a required skill profile which is dynamically updated.

Nardi et al. (2002) try to support the contact management of individuals. They have developed a personal communication and contact management application. It mines email applications to gather contact information of individuals (e.g. email addresses, phone number) with whom the user has communicated. It also generates a metrics of the strength of different ties and displays these ties graphically according to their strength. The user can manipulate the visualization by adding color or rearranging the contacts.

While the applications mentioned before are based on ordinary input and output devices, large screen displays and augmented reality applications offer another interesting approach to foster social capital. Churchill et al. (2003) and Divitini and Farshchian (2004) argue that applications based on large screen display can serve an important community building function. Located in public places, these screens advertise services, events and people’s interests, and invite community members to communicate, participate and interact.

Beyond this research work there are many mundane IT applications that can have a strong impact on the structural dimension of social capital. Address book applications and systems of Customer Relationship Management (CRM) are intended to strengthen existing social ties. However, many other types of IT applications, like many other types of material artefact, can have an impact on the development of social capital in a given social aggregate. For instance, Syrja¨nen and Kuutti (2004) present a case study where the introduction of a database with a www interface changed the social relations among the member of a Finish dog breeding community.

## Cognitive ability dimension

The cognitive ability dimension of social capital refers to the ability of the human actors to cognitively connect with each other to understand what the other is referring to when communicating. The higher a social group’s cognitive ability, the more the members are able to share (tacit) knowledge. A group’s cognitive ability depends on its ability to understand each other. Cognitive ability can be analysed by focusing on shared stories, language, communication regimes (Orlikowski and Yates, 1994), etc. The social capital’s cognitive dimension may enable knowledge sharing in the sense that stories, shared language, customs and traditions can bridge the tacit–explicit division as well as division in terms of, for example, old-timers–newcomers (Hinds and Pfeffer, 2003).

The cognitive preconditions of communication have so far not been a design focus in the applications mentioned above and it is still an open question whether and how they can be impacted within the appropriation process of IT applications. We see two ways the design of IT applications may support the cognitive dimension of social capital. First, communication spaces can provide a bandwidth to appropriately represent the communicative activities and the human actors’ context of interaction. They should also provide opportunities to ground discussions on shared materials. Second, IT applications can represent the history of interaction and make it perceivable for those who communicate with each other.

The appropriate bandwidth of a communication space depends on many factors, such as the degree to which the human actors know each other, the topic of interaction, their familiarity with the topic of interaction or the extend to which they can anticipate the communication partner’s current context of interaction. To better ground certain communicative activities and encourage mutual understanding, communication spaces should also provide for the integration of external materials related to the topic of interaction. Many current applications in support of social capital are still rather restricted with regard to the bandwidth they provide (e.g. they are often restricted to text-based asynchronous communication) and the opportunities to include additional materials. Better support for switches between different bandwidths and opportunities to refer flexibly to additional materials would be desirable.

Fischer et al. (2004) provide an interesting case of how to augment a collocated communication spaces with complex materials. They present the Envisionment and Discovery Collaboratory (EDC), an environment in which participants collaboratively discuss about issues of mutual interest. The EDC supports face-to-face discussion activities by bringing together individuals who share a common problem. The problem is discussed and explored by providing participants with a shared construction space in which participants interact with physical objects that are used to represent the situation currently being discussed. As users manipulate physical objects, a corresponding computational representation is updated by using technologies that recognize the placement and manipulation of physical objects. Computer-generated information is projected back on to the horizontal physical construction area, creating an augmented reality environment. The authors argue that such an application fosters the cognitive dimension of social capital by encouraging the recognition and awareness among the discussants.

To foster the cognitive dimension of social capital, an appropriate representation of the history of communicative activities may be helpful since it allows the human actors to better understand and refer to past interactions. However, communication spaces that store past interactions are typically overwhelmed with large amounts of historical data. So the historical data should be selected, edited and rearranged to support their perception and appropriate search functionality should be provided. The Answer Garden (cf. Ackerman and Malone, 1990; Ackerman, 1998; Pipek and Wulf, 2003) is one of the most influential approaches in integrating data of former interaction within a communication spaces. It was mainly built to encourage learning within organizations by allowing experts to select and edit their answers and rearrange them in a hypertext structure. Knowledge seekers can browse through existing materials before accessing the experts. The implementation of the functionality for selecting, editing, arranging and searching historical data has to be designed specifically with regard to the topic to be dealt with and the application domain (e.g. Chapman, 2004).

## Relation-based motivation dimension

The relation-based motivation dimension of social capital refers to the question ‘why’ and ‘when’ knowledge is shared. It is based on socially attributed characteristics of the relationship, such as trust, mutual respect and generalized reciprocity. If a network ‘scores’ high on the relation-based motivation of social capital, this implies that members are intrinsically motivated to share knowledge with each other because of their willingness to contribute to the relationship. Shared norms, a sense of mutual trust and respect and reciprocity stimulate people to share knowledge with each other (assuming they have the cognitive ability and structural opportunity to do so).

The effects of certain technological functionalities on the relational dimension of social capital have not yet been researched systematically (for an exception see Fischer et al., 2004). Again, it is still largely an open question how the appropriation process of IT applications interacts with the motivation to engage in common ventures.

With regard to topic-centred communication spaces, the reputation to be gained by active contribution seems to be a major factor for human actors to participate. Fischer et al. (2004) argue that the public code deliverables encourage developers in open source communities to write good code. They assume that public visibility of a human actor’s contributions seems to raise motivation.

Fischer et al. (2004) have also investigated into the motivational effects of technical features that represent the individuals’ contributions in a more formalized manner. The Experts Exchange is a web-based knowledge-sharing environment with an active community of almost 100,000 registered users. Any user can pose or answer a question. A point system motivates active participation. When users join, they are given a number of points. They can offer points to others in exchange for answering questions, and can gain points by answering questions posed by other users. By donating a specific amount of points user can express the quality of answers posed to their questions. Moreover, the system provides a listing of the most active contributors. Fischer et al. (2004) conclude that these formalized recognition mechanisms create communitywide awareness of the existence of experts and the distribution of expertise which facilitates potential information exchange and cooperation.

McDonald (2003) has tried to include a motivational element into the design of expertise recommender systems. He augmented an expert recommendation system with social networks. So the recommender system would suggest first those experts who had the closest social ties with the person asking. That way he assumed that the motivation to help could be encouraged. However, the results of an early evaluation study were mixed. Some of the participants feared that the positive motivational effects could be outperformed by negative structural ones (e.g. would not be hinted to the ‘best’ available expert).

## Social capital to support use of knowledge-sharing tools

The tools discussed so far are designed with the – either implicit or explicit – intention to support social capital. Most of these tools are designed only to support one dimension of social capital and mainly the structural dimension. We have not found reference to IT applications that are based on a more integrative approach. Furthermore, given its focus on using IT to increase social capital, these tools are based on a technological deterministic perspective rather than a socio-technical perspective. In the following, we will discuss the inverse relationship: analysing how social capital can inform the design of IT. This discussion is based on a more social deterministic perspective assuming that IT for knowledge sharing will be used only when its design maintains the integrity of the community in which knowledge is embedded (Boland and Tenkasi, 1995).

As mentioned, various applications exist to analyse and map structural dimension of knowledge sharing (see e.g. Fesenmaier and Contractor (2001). Such an analysis of the structural opportunity of a social network to share knowledge will not only reveal the existing flows of knowledge (who is connected to who) but also the methods and tools used by the group to connect to each other. This ‘who’ and ‘how’ analysis forms an important part in surfacing the design requirement of knowledge-sharing tools. However, analysing the structural opportunity dimension, for example, by existing network tools, only informs us about the structural embeddedness of the system. In order to gain more insight in the value of the social capital of a particular social network, one also needs to understand whether the network ‘nodes’ are willing to engage in sharing knowledge with others (Cross and Borgatti, 2004). This comes to the fore when analysing the relation-based motivation to share knowledge.

Remarkably less applications focus on the support of interpersonal relations.

Analysing the relation-based motivation to share knowledge addresses the question why people share knowledge and when they share knowledge. As mentioned earlier, a lot of KM initiatives do not succeed because of failing to address its value to the individual knowledge worker. Therefore, designing tools to support knowledge sharing should take seriously the potential motivational barriers to share knowledge. Motivational barriers are not only problems due to lack of personal benefits. They can also result from, for example, status differences, lack of trust, lack of perceived reciprocity, lack of respect (e.g. Huysman and de Wit, 2002; Hinds and Pfeffer, 2003).

Trust is an important aspect of social capital. It is generally accepted that mutual trust positively influences the possibility of knowledge transfer (e.g. Dodgson, 1993). Trust is needed to safeguard against opportunism and obstruction of sharing knowledge (Szulanski, 1996). Trust is also needed because a large dimension of the knowledge that is to be shared is of a tacit nature. Groups that ‘score’ high on the relational dimension share a sense of mutuality, meaning that people not only want to learn but also want to help others to learn. These people in turn are more likely to contribute their knowledge to the electronic knowledge network or repository (Cohen and Prusak, 2001).

In contrast to the structural aspects of networks that address the density of ties, the relational aspects refer to the ‘strength of ties’ (Granovetter, 1985). Analysis of the strength of ties offers insight into the strategies people employ to share knowledge (Hansen, 1999). Strong ties are important for the exchange of tacit knowledge while weak ties are important for the sharing of explicit knowledge. Strong ties imply a high degree of trust, which makes the entire process flow more smoothly.

Because of the delicate nature of the topic, interviews and questionnaires would probably only reveal the espoused theories. Therefore, ethnographic studies of the knowledgesharing culture of the social group are best suited to reveal the motivations of people to contribute to the relationship.

There are also remarkably few IT applications that are designed to decrease the cognitive distance between actors within a community, related to the cognitive ability dimension of social capital.

Nevertheless, cognitive barriers to sharing knowledge highly influence the use for electronic networks. A cognitive barrier is for example the difficulty to bridge the distance between expert and novice or the difficulty to express the tacit dimension of knowledge (Hinds and Pfeffer, 2003). The assumption is that the higher the cognitive barrier, the more people rely on social or personal networks instead of electronic networks (Leonard and Sensiper, 1998). For instance, the use of expertise requires validation and validation requires contacting the person. Likewise, the tacit dimension of knowledge requires access to social network to transfer the tacit part of the knowledge (Brown and Duguid, 2000).

Electronic networks are usually designed based on the espoused information needs of formal groups, teams within the canonical hierarchy of the organization. This would for example point at a need to access knowledge about the organization, customers, products, each other’s experiences, and best practices. Frequently used methodologies are questionnaires and interviews. For more in-depth insight, the prevalent theories-in-use and the situated cultural nature of knowledge also need to be taken into account. Methodologies used within cultural studies such as ethnography, narrative methods, and pattern recognition and matching might support such reflectivity of the community of practice (Lanzara, 1983).

Although a close match with the social network will improve the usefulness of community tools, some organizational redesign might still be needed to support a continuous natural flow of knowledge. One strategy is to institutionalize the activities of knowledge brokers in the organization. Case base research (e.g. Hargadon, 1998; Wenger, 1998) illustrated that some organizations introduce knowledge brokers whose main role is to bridge various social communities. Various knowledge broker roles can be identified. Wenger (1998) identifies ‘Boundary spanners’ who take care of one specific boundary of a knowledge community; ‘Roamers’ who go from place to place, creating an informal web of connections, and ‘outposts’ who bridge back news from the front and exploring new territories. These types of knowledge brokers concentrate on connecting various communities but not on connecting the social with the technical system. Research on knowledge sharing in practice (Huysman and de Wit, 2002) revealed different types of such ‘socio-technical brokers’, such as ‘reviewers’ of the content of the knowledge base, ‘boosters’ who’s main role is to get people connected and contribute, ‘commuters’ who run between the users at the front-office and the content providers at the back-office and ‘experts’ who are used to gain knowledge additional to what is in the repository.

It is interesting to note that most of these roles were introduced by the broker him/her self out of a need to fill a gap between the two networks. Future research on social capital and community tools will reveal if a better IT alignment will reduce the need of such socio-technical brokers.

## Conclusion

While the concept of social capital originates from sociology and political sciences, it has lately been adopted within the discipline of KM and IT. The notion of ‘social capital’ is an additional ingredient to the already wellknown economic conditions generating organizational value: physical capital, financial capital and human capital. Where human capital refers to individual ability, social capital refers to collective abilities derived from social networks. Several authors have expressed the importance of acknowledging social capital when investing in KM and argue that the higher the level of social capital, the more (distributed) communities are stimulated to connect and share knowledge. Distributed community members will be more inclined to connect and use electronic networks when they are motivated to share knowledge with others, able to share knowledge and have the opportunity to share knowledge. These three conditions of knowledge sharing within communities are considered key ingredients of social capital. At the same time, they offer interesting opportunities to analyse the social context that influences the use of IT within distributed communities. Nevertheless, until so far there has been no structured attempt to analyse this assumed relationship in more detail. This paper aimed to fill this gap by studying socio-technical requirement analysis for communities.

Clearly more empirical research is needed to test the assumption that social capital analysis results in improving the social embeddedness of community tools. Also, more research is needed to explore and study the effect of organizational design requirements such as the various roles of socio-technical brokers in sustaining a connection between the social and the technical system.

## Notes

1 There are many more fallacies related to the field of KM and OL such as the improvement bias and the harmonious bias (Huysman 2000). Although these traps also influence the design of IT, this influence is rather indirect. Here, we restrict the discussion to fallacies that influences directly the perception of the tools to support KM in communities.

## References

Ackerman, M.S. (1998). Augmenting Organizational Memory: A field study of answer garden, ACM Transactions on Information Systems 16(3): 203–224.

Ackerman, M.S. and Halverson, C.H. (2004). Sharing Expertise: The next step for knowledge management, in M.H. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge: MIT Press, pp. 273–299.

Ackerman, M.S. and Malone, T.W. (1990). Answer Garden: A tool for growing organizational memory, Proceedings of the ACM Conference on Office Information Systems (Cambridge, MA, USA, 1990); New York: ACM Press. 31–39.

Ackerman, M., Pipek, V. and Wulf, V. (2003). Beyond Knowledge Management: Sharing expertise, Cambridge, MA: MIT Press.

Adler, P. and Kwon, S-W. (2002). Social Capital: Prospects for a new concept, Academy of Management Review 27(1): 17–40.

Becker, G. (1964). Human Capital, a Theoretical and Empirical Analysis with Special Reference to Education, New York: Columbia University.

Becks, A., Reichling, T. and Wulf, V. (2004). Expert Finding: Approaches to foster social capital, in M. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT Press, pp. 333–354.

Bijker, W.E., Hughes, T.P. and Pinch, T.J. (1987). The Social Construction of Technological Systems, Cambridge, MA: MIT Press.

Blanchard, A. and Horan, T. (1998). Virtual communities and social capital, Social Science Review 16(3): 293–307.

Boland, R. (1991). Information System Use as a Hermeneutic Process, in H.E. Nissen, H.K. Klein and R. Hirschheim (eds.) Information Systems Research: Contemporary approaches & emergent traditions, New York: North-Holland, pp. 439–458.

Boland, R.J. and Tenkasi, R.V. (1995). Perspective making and perspective taking in communities of knowing, Organization Science 6(4): 350–372.

Bontis, N. (1999). Managing Organizational Knowledge by Diagnosing Intellectual Capital: Framing and advancing the state of the field, International Journal of Technology Management 18(5/6/7/8): 433–462

Bourdieu, P. (1986). The form of capital, in J.G. Richardson (ed.) Handbook of Theory and Research for the Sociology of Education, New York: Greenwood Press, pp. 241–258.

Bressand, A. and Distler, C. (1995). La Planete Relationelle, Paris: Flammarion.

Brown, J.S. and Duguid, P. (2000). The Social Life of Information, Cambridge, MA: Harvard Business School Press.

Brown, J.S. and Duguid, P. (2001). Knowledge and Organization: A socialpractice perspective, Organization Science 12(2): 198–213.

Buckingham, S. (1997). Negotiating the Construction and Reconstruction of Organisational Memories, Journal of Universal Computer Science (Special Issue on IT for Knowledge Management), 3(8): 899–928.

Burt, R.S (1992). Structural Holes: The Social Structure of Competition, Cambridge, MA: Harvard University Press.

Chapman, R. (2004). Pearls of Wisdom: Social capital building in informal learning environments, in M.H. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT Press, pp. 310–333.

Checkland, P.B. (1999). Soft Systems Methodology in Action, Chichester: John Wiley and Sons Ltd.

Choo, C.W., Detlor, B. and Turnbull, D. (2000). WebWork, Information Seeking and Knowledge Work on the World Wide Web, Dordrecht: Kluwer Academic Publishers.

Churchill, E., Nelson, L. and Denoue, L. (2003). Multimedia Fliers: Information sharing with digital community bulletin boards, in M. Huysman, E.Wenger, V. Wulf (eds.) Proceedings of the Communities & Technologies (Amsterdam, Netherlands, 2003); Dordrecht: Kluwer.

Ciborra, C.U (1996). Groupware and Teamwork, Chichester: John Wiley and Sons.

Clegg, C.W. (2000). Sociotechnical Principles for System Design, Applied Ergonomics 31: 463–477.

Cohen, D. and Prusak, L. (2001). In Good Company: How social capital makes organizations work, Boston: Harvard Business School Press.

Cross, R. and Borgatti, S.P. (2004). The Ties that Share: Relational characteristics that facilitate information seeking, in M. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT Press, pp. 137–162.

Davenport, T.H. (1997). Information Ecology, New York: Oxford University Press.

Davenport, T.H. and Prusak, L. (1998). Working Knowledge: How organizations manage what they know, Boston: Harvard Business School Press.

De Sanctis, G. and Poole, M.S. (1994). Capturing the Complexity in Advanced Technology Use: Adaptive structuration theory, Organization Science 5(2): 121–145.

Divitini, M. and Farshchian, B. (2004). Shared Displays for Promoting Informal Cooperation: An exploratory study, in F. Darses, R. Dieng, C Simone and M. Zacklad (eds.) Cooperative Systems Design – Scenario-based Design of Collaborative Systems, Amsterdam: IOS Press, pp. 211–226.

Dodgson, M. (1993). Learning, Trust and Technological Collaboration, Human Relations 46: 77–95.

Edvinsson, L. and Malone, M.S. (1997). Intellectual Capital: Realizing your company’s true value by finding its hidden roots, New York: Harper Business.

Ehrlich, K (2000). Designing Groupware Applications, in D.E. Smit (ed.) Knowledge, Groupware and the Internet, Boston: Butterworth Heinemann.

Ehrlich, K. and Cash (1994). Turning Information into Knowledge: Information finding as a collaborative activity, in Proceedings of Digital Libraries (College Station, USA, 1994).

Etzioni, A. (1995). New Communitarian Thinking: persons, virtues, institutions, and communities,, Charlottesville: University Press of Virginia.

Fesenmaier, J. and Contractor, N. (2001). Inquiring Knowledge Networks on the Web (IKNOW): The evolution of knowledge networks for rural development, The Journal of the Community Development Society 32: 160–175.

Fischer, G., Scharff, E. and Ye, Y. (2004). Fostering Social Creativity by Increasing Social Capital, in M. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT-Press, pp. 355–399.

Foner, L.N. (1997). Yenta: A multi-agent, referral-based matchmaking system, in First International Conference on Autonomous Agents (Agent’97); New York: ACM-Press. 301–307.

Granovetter, M (1985). Economic Action and Social Structure: The problem of embeddedness, American Journal of Sociology 91: 481–510.

Gra¨ther, W. and Prinz, W. (2001). The Social Web Cockpit: Support for virtual communities, in Proceedings of the 2001 International ACM SIGGROUP Conference on Supporting Group Work (Boulder, USA, 2001) New York: ACM Press. 252–259.

Hansen, M.T. (1999). The Search-Transfer Problem: The role of weak ties in sharing knowledge across organization sub-units, Administrative Science Quarterly 44(1): 82–111.

Hargadon, A.B. (1998). Firms as Knowledge Brokers: Lessons in pursuing continuous innovation, California Management Review 40(3): 209–227.

Hinds, P.J. and Pfeffer, J. (2003). Why Organizations Don’t ‘Know What They Know’: Cognitive and motivational factors affecting the transfer of expertise, in M. Ackerman, V. Pipek and V. Wulf (eds.) Beyond Knowledge Management: Sharing expertise, Cambridge, MA: MIT Press, pp. 3–26.

Holsapple, C.W. (2003). Handbook on Knowledge Management, Heidelberg: Springer.

Hughes, J., King, V., Rodden, T. and Andersen, H. (1994). Moving Out from the Control Room: Ethnography in system design, in Proceedings of the 1994 ACM Conference on Computer Supported Cooperative Work (Chapel Hill, USA, 1994); New York: ACM Press. 429–439.

Huysman, M.H. (2000). Rethinking Organizational Learning, Accountancy Management and Information Technology 10: 81–99.

Huysman, M.H. (2004). Traps and Challenges for Knowledge Sharing in Practice, Journal of Knowledge and Process Management 11: 81–92.

Huysman, M.H. and de Wit, D. (2002). Knowledge Sharing in Practice, Dordrecht: Kluwer Academics.

Huysman, M. and Wulf, V. (2004a). Social Capital and Information Technology, Cambridge, MA: MIT Press.

Huysman, M.H. and Wulf, V. (2004b). Social Capital and IT – Current debates and research, in M. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT Press, pp. 1–16.

Jordan, B. (1996). Ethnographic Workplace Studies and CSCW, in D. Shapiro, M. Tauber and R. Traunmuller (eds.) The Design of Computer Supported Cooperative Work and Groupware Systems. Human Factors in Information Technology, Amsterdam: North-Holland, pp. 17–42.

Kautz, H.A., Selman, B. and Shah, M. (1997a). Referral Web: Combining social networks and collaborative filtering, Communication of the ACM 40(3): 63–65.

Kautz, H.A., Selman, B. and Shah, M. (1997b). The Hidden Web, AI Magazine 18(2): 27–36.

Kumar, K., van Dissel, H.G. and Bielli, P. (1998). The Merchant of Prato – Revisited: Toward a third rationality of information systems, Management Information Systems Quarterly 22(2): 199–226.

Kuutti, K. (1991). Activity Theory and its Applications to Information Systems Research and development, in H.-E. Nissen (ed.) The Information Systems Research Arena of the 90s, Challenges, Perceptions and Alternative Approaches, Amsterdam: North-Holland, pp. 529–549.

Lanzara, G.F. (1983). The Design Process. Frames, Metaphors and Games, in U. Briefs, C. Ciborra and L. Schneider (eds.) Systems Design For, With, and By

the Users: Proceedings of the IFIP WG 9.1 Working Conference on Systems Design For, With, and By the Users (Riva De Sole, Italy, 20–24 September, 1982); Amsterdam: North-Holland. 29–40.

Leonard, D. and Sensiper, S. (1998). The Role of Tacit Knowledge in Group Innovation, California Management Review 40(3): 112–132.

Lesser, E. and Cothrel, J. (2001). Fast Friends: Virtuality and social capital, Knowledge Directions 2(1): 66–79.

Lesser, E.L. (2000). Knowledge and Social Capital: Foundations and applications, Boston: Butterworth Heinemann.

MacKenzie, D.A. and Wajcman, J. (1999). The Social Shaping of Technology 2nd ed., Philadelphia: Open University Press.

Markus, M.L., Majchrzak, A. and Gasser, L. (2002). A Design Theory for Systems that Support Emergent Knowledge Processes, MIS Quarterly 26(3): 179–213.

Maybury, M., D’Amore, R. and House, D. (2003). Automated Discovery and Mapping of Expertise, in M. Ackerman, V. Pipek and V. Wulf (eds.) Expertise Sharing: Beyond Knowledge Management, Cambridge, MA: MIT Press, pp. 359–382.

McDonald, D.W. (2000). Supporting Nuance in Groupware Design: Moving from naturalistic expertise location to expertise recommendation, PhD Thesis, University of California, Irvine.

McDonald, D.W. (2003). Recommending Collaboration with Social Networks: A comparative evaluation, in Proceedings of the 2003 ACM Conference on Human Factors in Computing Systems (CHI’03) (Ft. Lauderdale, USA, 2003); New York: ACM Press. 593–600.

Mumford, E. (2003). Redesigning Human Systems, Hershey, PA: IRM Press.

Nahapiet, J. and Ghoshal, S. (1998). Social Capital, Intellectual Capital, and the Organizational Advantage, Academy of Management Review 23(2): 242–266.

Nardi, B., Whittaker, S., Isaacs, E., Creech, M., Johnson, J. and Hainsworth, J. (2002). Integrating Communication and Information through ContactMap, Communications of the ACM 45(4): 89–95.

Newell, S., Scarbrough, H. and Swan, J. (2001). From Global Knowledge Management to Internal Electronic Fences: Contradictory outcomes of intranet development, British Journal of Management 12(2): 97–111.

Ogata, H., Yano, Y., Furugori, N. and Jin, Q. (2001). Computer Supported Social Networking for Augmenting Cooperation, Computer Supported Cooperative Work, The Journal of Collaborative Computing 10: 189–209.

Orlikowski, W. (2000). Using Technology and Constituting Structures, a Practice Lens for Studying Technology in Organizations, Organization Science 4(11): 404–428.

Orlikowski, W.J. and Robey, D. (1991). Information Technology and the Structuring of Organizations, Information Systems Research (2): 143–169.

Orlikowski, W.J. and Yates, J. (1994). Genre Repertoire: The Structuring of Communicative Practices in Organizations, Administrative Science Quarterly 39: 541–574.

Pipek, V. and Won, M. (2002). Communication-oriented Computer Support for Knowledge Management, Informatik/Informatique – Magazine of the Swiss Informatics Societies (1): 39–43.

Pipek, V. and Wulf, V. (1999). A Groupware’s Life, in Proceedings of the Sixth European Conference on Computer Supported Cooperative Work (ECSCW, Copenhagen, Denmark, 1999); Dordrecht: Kluwer. 199–219.

Pipek, V. and Wulf, V. (2003). Pruning the Answer Garden: Knowledge sharing in maintenance engineering, in Proceedings of the Eighth European Conference on Computer Supported Cooperative Work (ECSCW, Helsinki, Finland 2003); Dordrecht: Kluwer. 1–20.

Preece, J. (2002). Supporting Community and Building Social Capital, Special Issue of Communications of the ACM 45(4): 37–39.

Putnam, R. (1995). Bowling Alone: The collapse and revival of American community, New York: Simon & Schuster.

Resnick, P. (2001). Beyond Bowling Together: Sociotechnical capital, in J.M. Carroll (ed.) Human Computer Interaction in the New Millennium, Reading, MA: Addison-Wesley, pp. 647–672.

Roos, J., Roos, G., Dragonetti, N. and Edvinsson, L. (1998). Intellectual Capital: Navigating in the New Business Landscape, New York: New York University Press.

Shapiro, D. (1994). The Limits of Ethnography: combining social sciences for CSCW, in Proceedings of the 1994 ACM Conference on Computer Supported Cooperative Work (Chapel Hill, USA, 1994); New York: ACM Press. 417–428.

Snyder, W. and Wenger, E. (2000). Communities of Practice, the Organizational Frontier, Harvard Business Review 78(January/February): 139–145.

Stahl, G. (2004). Building Collaborative Knowing – Elements of a social theory of learning, in J.W. Strijbos, P. Kirschner and R. Martens (eds.) What We Know About CSCL in Higher Education, Dordrecht: Kluwer, pp. 53–86.

Stewart, T.A. (1997). Intellectual Capital: The new wealth of organizations, New York: Doubleday.

Streeter, L.A. and Lochman, K.A. (1988). An Expert/Expert Location System Based on an Automatic Representation of Semantic Structure, in Proceedings of the Forth Conference on Artificial Intelligence Applications (San Diego, USA, 1988); New York: ACM Press. 345–350.

Sveiby, K.E. (1997). The New Organizational Wealth: Managing and measuring knowledge based assets, London: Berrett-Koehler.

Syrja¨nen, L. and Kuutti, K. (2004). Trust, Acceptance and Alignment: The role of IT in redirecting a community, in M. Huysman and V. Wulf (eds.) Social Capital and Information Technology, Cambridge, MA: MIT Press, pp. 21–52.

Szulanski, G. (1996). Exploring Internal Stickiness: Impediments to the transfer of best practice within the firm, Strategic Management Journal 17: 27–43.

Uzzi, B. (1997). Social Structure and Competition in Interfirm Networks: The paradox of embeddedness, Administrative Science Quarterly 42: 35–67.

Vivacqua, A. and Lieberman, H. (2000). Agents to Assist in Finding Help, Proceedings in the Conference on Computer Human Interaction (CHI, The Hague, The Netherlands, 2000); New York: ACM Press. 65–72.

Walls, J., Widmeyer, G. and El Sawy, O. (1992). Building an Information System Design Theory for Vigilant EIS, Information Systems Research 3(1): 36–59.

Walsham, G. (1997). Actor Network Theory and IS Research: Current status and future prospects, in A.S. Lee, J. Liebenau and J.I. DeGross (eds.) Information Systems and Qualitative Research, London: Chapman & Hall, pp. 466–480.

Wasko, M. and Faraj, S. (2005). Why Should I Share? Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice, MIS Quarterly 29(1): 35–58.

Wasserman, S. and Faust, K. (1994). Social Network Analysis: Methods and applications, Cambridge, UK: Cambridge University Press.

Wellman, B. (2000). Computer Networks as Social Networks, Science 293(14): 2031–2034.

Wellman, B, Haase, A.Q, Witte, J. and Hampton, K. (2001). Does the Internet Increase, Decrease, or Supplement Social Capital? American Behavioral Scientist 45: 436–455.

Wenger, E. (1998). Communities of Practice, New York: Cambridge University Press.

Won, M. and Pipek, V (2003). Sharing Knowledge on Knowledge – The eXact peripheral expertise awareness system, Journal of Universal Computer Science 9(12): 1388–1397.

Wulf, V. and Rohde, M. (1995). Towards an Integrated Organization and Technology Development, in Proceedings of the ACM Symposium on Designing Interactive Systems (Ann Arbor, USA, 1995); New York: ACM Press. 55–64.

Yiman-Seid, D. and Kobsa, A. (2003). Expert Finding Systems for Organizations: Problem and domain analysis and the DEMOIR approach, in M. Ackerman, V. Pipek and V. Wulf (eds.) Expertise Sharing: Beyond Knowledge Management, Cambridge, MA: MIT Press, pp. 327–358.

Zack, M.H (1999). Managing codified knowledge, Sloan Management Review 40(4): 45–58.

Zack, M.H. and McKenny, J.L. (2000). Social Context and Interaction in Ongoing Computer-supported Management Groups, in D.E. Smith (ed.) Knowledge, Groupware and the Internet, Boston: Butterworth-Heinemann.

## About the authors

Marleen Huysman is Professor at the Department of Business Administration at the Vrije Universiteit Amsterdam. She studied sociology at the Erasmus University Rotterdam, got her Ph.D. in the field of economics and business administration She conducts research in the field of knowledge management, organizational learning, social dynamics of information systems, (online) communities.

Volker Wulf is a Professor in Information Systems at the University of Siegen and a Senior Research at Fraunhofer FIT, Sankt Augustin. After studying computer science and business administration at the RWTH Aachen and the University of Paris VI., he got a Ph.D. at the University of Dortmund and a habilitation degree at the University of Hamburg. He worked as a Research

Fellow at the Massachusetts Institute of Technology (MIT), Cambridge, MA. His research interests lie primarily in the areas of computer-supported cooperative work, knowledge management, computer-supported cooperative learning, entertainment computing, human–computer interaction, participatory design and organizational computing.
