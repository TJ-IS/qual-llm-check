---
otero_id: 3780
otero_key: "T95TT8VA"
title: "Using peer-to-peer technology for knowledge sharing in communities of practices"
authors: "Chen-Ya Wang; Hsin-Yi Yang; Seng-cho T. Chou"
year: "2008"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.06.012"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using peer-to-peer technology for knowledge sharing in communities of practices

Chen-Ya Wang <sup>a,b</sup>, Hsin-Yi Yang <sup>a</sup>, Seng-cho T. Chou <sup>a,⁎</sup>

<sup>a</sup> Department of Information Management, National Taiwan University, No. 1, Sec. 4, Roosevelt Rd., Taipei, 10617 Taiwan, ROC <sup>b</sup> Department of Information Management, Lunghwa University of Science and Technology, No. 300, Sec.1, Wanshou Rd., Guishan, Taoyuan County 33306, Taiwan, ROC

Available online 23 June 2007

## Abstract

Communities of Practices (CoPs) are informal structures within organizations that bind people together through informal relationships and the sharing of expertise and experience. As such, they are effective tools for the creation and sharing of organizational knowledge, and an increasing number of organizations are adopting them as part of their knowledge management strategies. In this paper, we examine the knowledge sharing characteristics and roles of CoPs and develop a peer-to-peer knowledge sharing architecture tha matches the behavioral characteristics of the members of the CoPs. We also propose a peer-to-peer knowledge sharing tool called KTella that enables a community's members to voluntarily share and retrieve knowledge more effectively. © 2007 Elsevier B.V. All rights reserved.

Keywords: Communities of Practices (CoPs); Knowledge sharing; Peer-to-peer (P2P)

## 1. Introduction

Knowledge assets are a critical strategic resource that can provide organizations with a competitive advantage. Consequently, in recent years, both research and application of knowledge management (KM) techniques have become very important topics in management literature. Generally, knowledge can be categorized as either explicit knowledge or tacit knowledge [16]. Most organizations focus on managing explicit knowledge well, and try to capture tacit knowledge embedded in the experienced and skilled people as much as possible. Many approaches have been developed to help organizations create, capture, store, share, and apply knowledge. Often knowledge sharing is the core intent of a KM initiative, so it has become an important theoretical and practical problem [18]. By emphasizing interaction through social networks (person-to-person relationships), community-based knowledge sharing has become one of the most effective tools among a variety of approaches [6,8,22]. One reason that CoPs play such an important role in knowledge management is that knowledge cannot be separated from its context [17]. Despite their formal structures and policies, more and more organizations are developing CoPs as strategic tools for knowledge creation and sharing within the organization and even across organizational boundaries.

KM research can be divided into two categories: human-oriented and technology-oriented research [14]. It is widely recognized that technology can support knowledge management activities and can often be an enabler of knowledge management. Traditional knowl edge management technological architectures (e.g., the Enterprise Knowledge Portal developed by Lotus Notes) are usually centralized, which makes it easy to control, organize, and store knowledge. In addition, they usually have a unique, simple point of access to incorporate the knowledge of the members belonging to different organizational units [15]. Once an organization's members post their knowledge, they become detached from it, and lose control over who can access and use it. As a result, members are more likely to store their draft notes and working documents in their local repositories, rather than in a central knowledge management system. Many knowledge management systems are shunned by users because they are unwilling to update knowledge in the systems. One reason that people do not contribute to knowledge management systems continuously is that the technological architecture of such systems does not match human social behavior and work processes [9,14,18]. Another reason is that knowledge workers do not want to give up their autonomy and anonymity [15]. The design of KM systems needs to be consistent with the social processes of organization cognition [3]. One difficulty in KM nowadays is how to bridge the gap between the technical architecture and human factors (i.e., behavior). Peer-to-peer technology enables users to actively share knowledge and information in a more flexible way. It fits well with a more loosely coupled information-sharing environment (e.g., virtual teams and B2B knowledge sharing) because it feels “natural” and “personal” to users [19,23]. Peer-to-peer technology can complement a centralized technological architecture to help CoP members share their knowledge and enhance their social interaction. In this paper, we propose a peer-to-peer architecture to support knowledge sharing in CoPs from a socio-technical perspective — the perspectives of human behavior and technological architecture support. We have also developed a tool called KTella to facilitate knowledge sharing between the members of CoPs.

The remainder of this paper is organized as follows. In Section 2, we present a review of CoPs and discuss the characteristics of knowledge sharing. In Section 3, we introduce the KTella architecture that can support knowledge sharing within and among CoPs. Section 4 describes two application scenarios of KTella. Finally, in Section 5, we present our conclusions and indicate the direction of future work.

## 2. Knowledge sharing in communities of practices

The concept of communities of practice (CoPs), proposed by Lave and Wenger [11], describes informal groups of people who create, share, and leverage their knowledge and experience. CoPs are self-organizing structures with a collective purpose and are held in place by social relationships [1]. Such communities can strengthen the ties between people in the same professional group and extend the network to a larger group. Unlike conventional functional organizations, the members of CoPs usually come from different units of an organization, or even from different organizations (e.g., professional associations, groups of software developers, or skilled craft guilds), and complement the function of formal units.

Intangible, tacit knowledge embedded in an organization's members is an asset that is not easy to capture. CoPs, however, offer a practical mechanism to help their members share and internalize tacit knowledge. Furthermore, through the communities, people can deepen their expertise by discussing work-related activities with others in their field. As well as enabling members to share existing knowledge, CoPs also provide opportunities for new knowledge creation. Several researchers have noted that CoPs appear to be a more effective tool for dealing with unstructured problems and knowledge sharing/ creation than traditional and formal ways of structuring interaction in organizations [7,12,21]. Indeed, many organizations, such as Motorola, HP, IBM, Xerox, Ford, and Shell, have adopted CoPs as a KM tool. To increase knowledge sharing, the exchange of insights and ideas, and the transfer of expertise and experience, we can view CoPs as engines of knowledge creation and sharing [12]. For successful CoP implementation, it is important to: 1) remove barriers to individual participation, 2) support and enrich the development of each individual's uniqueness within the context of the community, and 3) link that uniqueness with the community's purpose [2,13].

Knowledge cannot be easily separated from its context and its owner. Understanding the processes and mechanisms that enable members to share knowledge with their peers in CoPs is very important for knowledge sharing within and between such communities [17]. There is no doubt that information technology plays an important role in CoP activities. In recent years, collaborative technologies such as e-mail, listservs, electronic bulletin boards, electronic forums, and electronic chat rooms have facilitated the development of CoPs whose members are not collocated. [4,20]. A great deal of KM research has found that CoPs enabled by online interactive technologies can function as strategies for persuading an organization's members to adopt KM [2,13]. The technological supports for CoPs are traditionally centralized architectures that facilitate easy control and management of knowledge; however, they do not fit knowledge workers' behavior well. For example, people have to link to a portal to upload their knowledge objects and login to forums to post articles or discuss practices with other members. One requirement for a successful CoP is that its members feel comfortable when participating in a computer-mediated, Internet-based CoP [2], but members may be disinclined to participate if the group becomes too large, or if the knowledge being exchanged is not relevant. Technical support should help the members select useful information from the mass of postings and knowledge objects.

A KM system's social and technological attributes determine the success of knowledge creation and sharing [5]. Existing knowledge sharing and creation approaches tend to focus too much on either social or technological issues. In contrast, a peer-to-peer architecture such as KTella integrates the socio-technical elements to support the KM activities of CoPs. We introduce the system concept and architecture of KTella in the following section.

## 3. KTella P2P knowledge sharing system architecture

## 3.1. System concept

Our design goal is to form a knowledge sharing community based on decentralized P2P technology. The technological architecture of a P2P system, in which a peer is both a server and a client, is consistent with the role of a knowledge sharing community, in which a member is both a knowledge provider and a knowledge consumer; therefore, our design is built around a P2P file sharing system for knowledge sharing.

The proposed P2P knowledge sharing system, called KTella, is based on the Gnutella P2P network in which a peer is generally referred to as a servent (both a SERVer and a cliENT). Gnutella is representative of the decentralized and unstructured P2P systems used for sharing files over the Internet. It was designed in early 2000 as a replacement for Napster; to date, it has been used mainly for the dissemination of multimedia files. Its simple and robust characteristics have made it popular. To share files on the Gnutella network, a participant (node A for example) starts with a networked computer that runs one of the Gnutella clients. Node A will then connect to another Gnutella-enabled networked computer (node B for example) and announce its existence to B, which announces to all its neighboring nodes (nodes C, D, and E for example) that A is alive. This pattern will continue recursively with each new level of nodes announcing to its neighbors that node A is alive. Once node A's status has been announced throughout the network, the user at node A can access the data being shared across the network.

As a servent, the application provides an interface whereby a user can enter keywords describing the files that he is seeking. The program then sends the request to neighboring participants who pass it on to their neighbors who do the same; thus, the request is propagated throughout the network. At the same time, clients check to see if the request corresponds to local files they are willing to share and, if so, they send back a response. File transfers are done via another route using standard HTTP protocol requests.

We propose some modifications to Gnutella to boost the effectiveness of blind searching. The idea is that each peer should be able to link directly to nodes that are similar to itself, since there is a higher probability that similar peers will have the closest matches to the query keywords. By using a weighted similarity of the other users' ratings, collaborative filtering algorithms can be used to predict a user rating for an item. We adopt a rating mechanism to form peer groups and provide social filtering and recommendation functions to make knowledge sharing effective and efficient.

KTella seeks to retain the simple, robust, and fully decentralized nature of Gnutella, while improving its efficiency. Locating content efficiently in a decentralized P2P system is a challenging problem. Efficient knowledge sharing means being able to provide the right information to the right people at the right time. We use a rating method to support recommendations, and peer clustering to make knowledge sharing efficient. KTella provides the functionality to support knowledge sharing activities and promote knowledge sharing through the dissemination of documents, ideas, experience, and the ratings of knowledge objects.

KTella has five main functions: knowledge searching, knowledge publishing and forwarding, peer clustering, knowledge recommendation, and instant messaging. A KTella user is both a knowledge consumer and a knowledge provider. As a consumer, the user searches KTella for knowledge objects of interest. On the other hand, as a provider, he publishes and forwards knowledge objects to others. Peer clustering finds other users with similar knowledge domains, and acts as a social filter to make searching, publishing, and forwarding knowledge objects more efficient. The knowledge recommendation function provides a predicted rating of a sharable knowledge object (SKO) to recommend to users, while the instant message function provides a communication channel between KTella users.

The basic concept of our approach is that each peer maintains information about its own experience of SKOs, and shares that experience with others on request. This approach can also be used for peer clustering. Each servent has to maintain the following repositories:

(1) A colleague group list: a list of servents in its colleague group (defined below).

(2) A companion peer list: a list of servents in its companion group (defined below).

(3) A rating vector repository: a table of attributes (SKO\_id, utility ratings, and relevancy ratings). For each SKO a user rates, a numeric value (describing whether the SKO is good (10) or bad (0) is given by him/her), as well as a numeric value (describing whether the SKO is highly-relevant (10) or irrelevant (0) to the peer's work) are stored in the servent.

(4) A forwarding log repository: a table of attributes (servent\_id, SKO\_id) to record which SKO has been forwarded to whom in order to avoid duplicate knowledge sharing.

KTella consists of two components: a knowledge sharing component and a P2P network component. The former facilitates knowledge sharing between members in a community. The latter deals with a set of descriptors used for communication between servents and sets rules for inter-servent descriptor exchange. Next, we define some terms used in the KTella system and then describe the two components in details.

Colleague group: Peers in relevant organizational divisions are combined in a colleague group. Relevant divisions may be finance departments in different countries, or departments in the same college. Their relationships are explicit in the organization's architecture. Each peer has a colleague group list to keep a record of his/her colleague peers.

Companion group: Peers with the same interests are included in the companion group. Each peer has a companion group list to keep a record of his/her companion peers. Since a peer's interests may change, the companion peers list will be updated dynamically according to the peer's similarity to other potential companion peers.

Knowledge peer: A knowledge peer can be in either a colleague group or a companion group.

Information peer: An information peer does not belong to a colleague group, or a companion group.

Sharable Knowledge Object (SKO): A knowledge object that a peer chooses to share with others. It could be a document that a knowledge worker wrote to describe his experience, or a document that is useful and related to his work.

Relevancy rating: This represents the extent that the SKO is relevant to the knowledge worker's domain.

Utility rating: This represents the extent that the SKO is useful and/or of interest to the knowledge worker. In addition, KTella makes the following assumptions:

(1) Most knowledge workers are servents. Since KTella is a knowledge sharing system, most knowledge workers need to connect to KTella.

(2) A user give ratings on an SKO after browsing it. These ratings are used to form a peer group in order to find companions and facilitate social filtering and making recommendations.

(3) Each peer stores SKOs with high utility ratings. When a user gives a high rating to a document, it means that it is useful or interesting to him. We assume that it will be stored.

## 3.2. KTella algorithms

## 3.2.1. Definition

First, we present some definitions used in the following sections. Given a set N of nodes in KTella, each node $n \in N$ has:

NodeID (n) A unique id.

P A set of colleague groups.

$q$ A companion group.

$N _ { p }$ A set of nodes in colleague groups, where $N _ { p } =$ $\{ n \in p | p \in P \}$

$N _ { q }$ A set of nodes in companion groups, where $N _ { q } = \{ n { \in } q \}$

$N _ { k }$ A set knowledge peers , where $N _ { k } { = } N _ { p } | N _ { q }$

$N _ { i }$ A set information peers, where $N _ { i } { = } N { - } N _ { k }$

$U _ { \sigma }$ The utility vote n gives to an SKO σ.

$R _ { \sigma }$ The relevancy vote n gives to an SKO σ.

$R _ { n i }$ Relevancy to node i, where i denotes the other nodes in KTella

$$
R _ {n i} = \frac {\sum_ {\sigma} (v _ {n , \sigma} - \overline {{v _ {n}}}) (v _ {i , \sigma} - \overline {{v _ {i}}})}{\sqrt {\sum_ {j} (v _ {n , j} - \overline {{v _ {n}}}) ^ {2} \sum_ {j} (v _ {i , j} - \overline {{v _ {i}}}) ^ {2}}},
$$

where the summations over σ are over the SKOs for which both nodes n and i recorded relevancy ratings.

In KTella, a set of SKOs, O, is shared, and each SKO $\sigma \in O$ has:

ObjectID (σ) A unique id.

$K _ { \sigma } \mathrm { ~  ~ \cal ~ \cal ~ A ~ }$ set of keywords associated with σ.

## 3.2.2. SKO Search Algorithm

$O _ { K } \mathrm { : }$ a set of matching SKOs, where $O _ { K } { = } \{ \sigma \mid \mathrm { K } \mathrm { K } _ { \sigma } ,$ σ $O \}$ ; that is, $O _ { K }$ is the set of SKOs that can be described by K.

Knowledge Peers Searching Phase: search $O _ { K }$ in $N _ { k } .$ Information Peers Searching Phase: search $O _ { K }$ in $N _ { i } .$

Box 3

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
When a user of node nsearches for an SKO with a set of keywords K:
If  $O_{K}$  in the Knowledge Peers Searching Phase  $\neq\Phi$ 
the user decides whether to go to the Information Peers Searching Phase
Else
go to the Information Peers Searching Phase
End if
End of algorithm
</div>

## 3.2.3. SKO forward algorithm

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Box 2
When a node n gives a utility rating for an SKO  $\sigma$ :
If  $U_{\sigma} &gt; threshold$ 
for each group p, where  $p \subseteq P$ :
n decides whether to forward
 $\sigma$  to nodes in p
for each node q in  $N_{q}$ 
If  $R_{\sigma} &gt; threshold$ 
KTella automatically forwards  $\sigma$  to  $N_{q}$ 
End if
End if
End of algorithm
</div>

## 3.2.4. Peer clustering algorithm

The algorithm uses the Pearson correlation coefficient to determine if two peers are relevant.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
For each node n:
    If  $R_{ni}&gt;0$ 
    include i in  $N_{q}$ 
    Else
    exclude i from  $N_{q}$ 
    End if
End of algorithm
</div>

## 3.3. KTella network protocol

The core of the KTella network protocol is comprised of a set of descriptors that are used for communication between servents and to set rules for the inter-servent descriptor exchange. We modify some of the descriptors adopted from Gnutella and define some new ones to meet the requirements of the knowledge sharing system. KTella includes the following descriptors:

Ping: A Ping message is sent by a servent when it needs to find hosts that are currently active in the KTella network. A servent receiving a Ping descriptor is expected to respond with one or more Pong descriptors.

Pong: A Pong message is the response to a Ping message. It includes the address of a connected KTella servent and information regarding the amount of data it is making available to the network.

Query: A Query message is used to search SKOs in the KTella network. A servent receiving a Query descriptor responds with a QueryHit if a match is found against its shared SKOs.

QueryHit: A QueryHit message is the response to a Query message. It is used to return a list of matching SKOs along with information for download.

Poll: A Poll message is used for collaborative filtering and is sent by a servent when it needs to collect rating vectors from other servents. A servent receiving a Poll descriptor is expected to respond with PollReply descriptor.

PollReply: A PollReply message is the response to a Poll message. It is used to return its rating vector along with host information.

Forward: A Forward message is used to forward an SKO to other servents. It includes a short description of the SKO and information for download.

Feedback: A Feedback message is used for tuning the knowledge group. It sends a rating vector to other servents which use the rating vectors to calculate their similarity.

The KTella network protocol design is shown in Fig. 1.

## 3.4. System architecture

Since KTella is a P2P knowledge sharing system, each computer must be set up as a KTella client in order to run as a servent. By following KTella's network protocol, peers can communicate with each other and connect to the KTella network. Each servent is equipped with a local repository of SKOs, which is available to the KTella network for sharing with other servents. Most knowledge workers in an organization run servents to

![](/api/attachments/T95TT8VA/fulltext/images/9c603f0c67da76e64785de66aabdfa7d9a489d73186290d22f082eb39d764a95.jpg)  
Fig. 1. The KTella network protocol.

provide SKOs and ratings on them to increase the number of knowledge objects and the ratings repository available to the KTella network as a whole. The system architecture of KTella is illustrated in Fig. 2. The implementation of KTella includes client and network protocol implementation.

We implement the KTella client to run as a servent in the KTella network. Knowledge workers use KTella's clients to connect to the KTella network. Each client acts as a server to contribute SKOs and a client to receive them. KTella client is composed of a user interface module, a search module, an instant message module, a rating module, an SKO exchange module, a publishing module, a recommendation module, and a peer clustering module. The relationships among the modules are shown in Fig. 3. KTella client operates through a user interface module to interact with other servents in the KTella network.

![](/api/attachments/T95TT8VA/fulltext/images/a691e1fd4164d876069137bf700ad821e9a3cb3d2922310f5691fd3a6db55e80.jpg)  
Fig. 2. KTella's system architecture.

## 3.4.1. User interface module

The user interface module acts as an intermediary between a user and other modules. The user interacts with the module when he searches for SKOs in KTella, publishes and forwards an SKO to KTella, gives ratings on an SKO, sends instant messages to other users, or decides whether to download SKOs from other peers. The user interface module then interacts with the search module, publishing module, rating module, instant message module, and SKO exchange module to accomplish the user's task. Conversely when a servent receives a QueryHit from other servents, the user interface module presents related information to the user.

## 3.4.2. Search module

The search module deals with a user's search request from the user interface module to search target SKOs in KTella. When searching for an SKO, the user specifies keywords of the SKO's name and annotations as search criteria. The user interface module sends the search criteria to the search module, which encapsulates the criteria in a Query description and sends it to the connection and communication module to route into the KTella network.

The search module also deals with Query descriptions transmitted from the connection and communication module. First, it parses the search string in the Query description and then scans its SKO repository for any matching SKOs. If a target SKO is found, the search module sends back a QueryHit description containing the SKO and servent information. The annotations of the SKO are obtained from the SKO information database. If a target SKO is not found, the Query description is dropped.

## 3.4.3. Publishing module

When a user considers that a document is an SKO, he/ she sends it to KTella, and chooses which companion groups to forward it to. To facilitate knowledge sharing, the user also assigns annotations to describe the document. The publishing module moves the document to the SKO repository, which is a shared storage on a local disk, for other peers in KTella to access. The repository stores related SKO information in its database.

![](/api/attachments/T95TT8VA/fulltext/images/a4ae654e0afdc8b5558aebffc5631d5d38e743812c0bccaec74ec094bcb3d6ff.jpg)  
Fig. 3. KTella's module architecture

The publishing module then triggers the forwarding module to send the SKO to the colleague groups chosen by the user, as well as the user's companion group. Other peers in KTella can access the SKO by searching or having it forwarded to them.

## 3.4.4. Forwarding module

The rating and publishing modules trigger the forwarding module. When a user gives a rating on an SKO above the threshold, or sends an SKO to KTella, the forwarding module encapsulates the SKO information in a forwarding description and sends it to the connection and communication module to route it to its knowledge peers.

The forwarding module also deals with forwarding descriptions sent from other peers. When a servent receives a forwarding description, the forwarding module checks the forwarding log to avoid duplication. If a KTella servent receives the description for the first time, it keeps it in the forwarding log and triggers the user interface module to inform the user about the new SKO.

## 3.4.5. Rating module

The rating module deals with ratings on SKOs. When a user gives a rating on an SKO downloaded from another peer, the rating module stores it in the rating database. If the rating of the SKO is above the pre-set threshold, KTella keeps it in the SKO repository and triggers the forwarding module. Otherwise, the SKO is deleted. The rating module then triggers the peer clustering module for group tuning. It also encapsulates its rating vector in a feedback description and sends it to servents who have sent PollReply descriptors.

When the rating module receives a Poll description from the connection and communication module, it looks up the rating database to check if there are ratings

![](/api/attachments/T95TT8VA/fulltext/images/de393b91d038fece1e65ec893b14081023b7af56f93d9d4c0b746d56268e9a54.jpg)  
Connections: 0 - Downloads: 0/3/1 - Uploads: 0/0/2

Fig. 4. A screenshot of SKO publishing.

on the SKO that match the Poll description queries. If so, the rating module encapsulates the rating vector in a PollReply description and sends it to the connection and communication module to route into KTella network.

When a servent receives a QueryHit description, the rating module encapsulates Poll descriptions to poll other peers' ratings on the matching SKO. After receiving PollReply descriptions from other peers, the rating module calculates a predicted utility rating for each matching SKO. The predicted utility ratings are calculated by a modified collaborative filtering algorithm and used to complete the SKO predicted rating element in the result set of the QueryHit description, which is then sent to the user interface module.

## 3.4.6. SKO exchange module

The SKO exchange module deals with users' requests for file exchanges from the user interface module. When a user wants to download an SKO from other servents, the SKO exchange module has to download the SKO from the provider. It also deals with other peers' requests for SKO exchange.

## 3.4.7. Instant message module

The instant message module manages communications among peers. It sends instant messages to other peers and receives messages from them.

## 3.4.8. Peer clustering module

When a user gives a rating on an SKO, the rating module triggers the peer clustering module to calculate its similarity to the ratings of other servents who have sent PollReply descriptors. When a servent receives the Feedback description, the rating module is also triggered to calculate its similarity to the servent who sends the description. The similarities among servents are calculated by Pearson's correlation coefficient. Whether or not a servent is included in a companion group list depends on its similarity to other members in the group.

## 4. Application scenarios

In this section, we first present two scenarios that demonstrate how our system works, and then describe the rationale behind the implementation of

![](/api/attachments/T95TT8VA/fulltext/images/62e1b7c02b53fd5b1ad9b16eed8b67087fb4c1c47c20d91bd8b44bf1a4d67918.jpg)  
Fig. 5. A screenshot of SKO forwarding.

KTella. Each user of the KTella knowledge sharing system plays two roles: knowledge provider and knowledge consumer, for which we provide separate scenarios.

## 4.1. Knowledge provider scenario

As a knowledge provider, the KTella client allows a user to publish any type of electronic resource that he/ she deems a knowledge object. The user selects the Share panel to publish an SKO, provides annotations and ratings for it, and chooses which groups to forward it to. This panel also shows information about SKOs he/ she has published and the upload records of the SKOs, as shown by the screenshot in Fig. 4.

After a user downloads an SKO from another peer, he/she is asked to provide ratings and annotations for it and choose which groups to forward it to, as shown in Fig. 5. Also, as knowledge providers, users share their professional opinions about recently downloaded SKOs.

## 4.2. Knowledge consumer scenario

Knowledge consumer is the other role of a KTella system user. As a knowledge consumer, the KTella client allows a user to search for SKOs from other peers. The user selects the Search tab and fills in the search criteria. Information about matching SKOs then appears on the right-hand side of the panel. It includes file information, sharing hosts, and predicted utility ratings to help the user decide whether to download, and where to download, the SKO. The user can also communicate directly with other peers by instant messaging to share ideas and experiences. In addition, he/she can browse others' SKO repositories to see if there are SKOs he/she needs. The screenshot is shown in Fig. 6.

As a knowledge consumer, the user receives SKOs forwarded from others. They are displayed in the Recommendation tab. The user can send instant messages with, and browse the SKO repository of, the forwarders. If he/she downloads the SKOs, the related

![](/api/attachments/T95TT8VA/fulltext/images/28cfc079472ed5e9d8970526ab2538ab8a7d0400fcd8448d9332206cd8b79915.jpg)  
Connections: 1 - Downloads: 0/1/1 - Uploads: 0/0/0

Fig. 6. A screenshot of SKO searching information will be displayed in the Download tab. Fig. 7 is a screenshot of the Recommendation tab.

From the Download tab (Fig. 5), the user can also obtain information on SKOs downloaded from other peers. The search term column specifies the source of the SKO. It could be the search criteria for SKO matching or “Forwarding download”, which means the SKO has been forwarded from others. For each SKO, the KTella client provides information on its download candidates. If a user wants to remove a download record, he/she has to give a utility rating and a relevancy rating on it. This mechanism enforces the rule of sharing ratings with other users.

## 4.3. System rationale

A knowledge sharing system empowers an individual knowledge worker by providing the tools to support and boost his/her knowledge sharing ability. The basic assumption is that if individuals are willing to share knowledge, an effective knowledge sharing system would motivate users to access it and facilitate knowledge sharing among them.

Kwok and Gao [10] summarized and clarified the most salient motivational factors that influence the willingness, or tendency, of P2P network users to share knowledge [10]. These factors are sub-community organization, individual identity and profile generation, contribution– reward mechanism, and reviews and peer recommendations. They are built in to KTella as explained below.

1. Sub-community organization: KTella allows users to set up their own colleague groups. It also forms a companion group automatically through collaborative filtering for each user. The assumption is that knowledge workers will be prepared to help others if they have a sense of belonging to a sub-community that provides a community identity.

2. Individual identity and profile generation: In KTella, each servent has a unique identity. Individual identity is the foundation of trust among members. The rating repository of each servent acts as a personal profile, presenting the interests and work domain of the user. According to interpersonal psychology theory, it is

![](/api/attachments/T95TT8VA/fulltext/images/f2407980becf6ae5d254c0d3c4c5a3566ebfa35a213ce57bbcb0dd0c6623bacd.jpg)  
Connections: 0 - Downloads: 0/3/1 - Unlnards: 0/0/2

Fig. 7. A screenshot of the recommendation tab.

easy for people to form affiliations when they have similar interests.

3. Contribution–reward mechanism: To incorporate reward features into the P2P knowledge sharing system, it is necessary to incorporate a knowledge-tracking mechanism in the application. KTella provides statistical information to evaluate an individual's contribution to the knowledge sharing community. An administrator can set up reward rules according to the statistical information.

4. Peer recommendation: This helps a user decide which member(s) to interact and share knowledge with on the basis of previous experience. KTella indirectly implements the peer recommendation feature through its peer clustering mechanism. In KTella, knowledge peers have a high priority to interact with each other in the knowledge searching and knowledge forwarding processes.

KTella also provides the following basic knowledge sharing functions and mechanisms to make knowledge sharing effective and efficient.

## 1. Contributing

KTella allows a user to contribute any type of electronic resource as an SKO. Annotations of the SKO act as metadata for retrieval. After a user contributes his/her knowledge, KTella automatically forwards the SKO to others who may need it. This mechanism makes contributing knowledge more effective.

## 2. Searching

KTella allows a user to search for SKOs by using keywords and annotations and by browsing other peers' SKO repositories. KTella's search algorithm first searches the user's knowledge peers, because the probability that they will have matching SKOs is high. This mechanism makes searching for knowledge more efficient. In addition, KTella provides a predicted rating for each matching SKO. It helps the user decide which SKO to download.

## 3. Companion finding

KTella finds companion groups for a user. This allows knowledge and experience to be shared among people who would not know each other otherwise. Organizations can avoid repeating mistakes, duplicating efforts, and wasting resources because members of the organization get to know each other's work through the system.

## 4. Information filtering

In KTella, each user is a member of a sub-community that provides a social filtering mechanism. In the knowledge searching and dissemination process, the sub-community filters in relevant knowledge and filters out irrelevant knowledge so that knowledge sharing is more effective and efficient.

## 5. Conclusion

CoPs are an effective means of creating and sharing organizational knowledge. Unlike centralized knowledge management approaches, a peer-to-peer architecture is a knowledge management option that matches the behavioral characteristics of the members of the CoPs. In this paper, we have proposed a P2P knowledge sharing architecture from a social–technical perspective. We have also presented a system called KTella, based on the Gnutella P2P network. KTella seeks to retain the simple, robust, and fully decentralized nature of Gnutella, while providing a knowledge sharing functionality.

Specifically, KTella forms a knowledge sharing environment with multiple knowledge repositories, and enables knowledge to be produced in different formats by different producers at different functional levels. The roles of knowledge generation and codification are performed by the same knowledge worker and contextual information is naturally embedded. Adopting a P2P network architecture makes the social form of organizations similar to a technological architecture so that the knowledge sharing process is more natural and, therefore, more acceptable to users.

We have incorporated a rating method in the P2P knowledge sharing system. Users are asked to give relevancy and utility ratings for SKOs, which are then used for knowledge recommendation and peer clustering. To predict the utility ratings, we modify a collaborative filtering method for knowledge recommendation. This helps a user decide which SKOs to download. Peer clustering also forms sub-communities and finds companion groups for each user. The sub-community acts as a social filtering mechanism. Companion finding avoids duplicating efforts and wasting an organization's resources.

We believe that KTella can empower knowledge workers by providing them with the tools and environment for knowledge sharing. KTella promotes knowledge sharing in the form of document sharing, ideas and experience sharing, and professional judgment sharing and provides powerful tools to support and boost more knowledge sharing activities.

KTella is designed as a platform for knowledge sharing in CoPs based on P2P technology. The performance of such a platform requires further experimental studies, which is a necessary and logical next step for KTella. Other issues, such as the degree of freedom of knowledge workers and intellectual capital gain for CoPs in the P2P knowledge sharing environment are also worth further exploration. In addition, we are working on tagging mechanisms for individual's SKOs and exploring the construction of a common ontology for CoPs. We will then extend KTella with these capabilities to make it a truly powerful knowledge management tool for individual knowledge workers as well as their respective communities.

## Acknowledgements

This work was supported in part by the National Science Council Grants 94-2217-E-002-004, 92-2416- H-002-001, and 91-2416-H-002-008.

## References

[1] W.W. Agresti, Tailoring IT support to communities of practice, IT Professional 5 (6) (2003) 24–28.

[2] A. Ardichvili, V. Page, T. Wentling, Motivation and barriers to participation in virtual knowledge-sharing communities of practice, Journal of Knowledge Management 7 (1) (2003) 64–77.

[3] M. Bonifacio, R. Cuel, G. Mameli, M. Nori, A peer-to-peer architecture for distributed knowledge management, Proceedings of the 3rd International Symposium on Multi-Agent Systems, Large Complex Systems, and E-Businesses MALCEB, 2002.

[4] J.S. Brown, P. Duguid, Organizational learning and communities-of-practice: toward a united view of working, learning, and innovation, Organization Science 2 (1) (1991) 40–57.

[5] D. Holsthouse, Knowledge research issues, California Management Review 40 (3) (1998) 277–280.

[6] J.O. Iverson, R.D. McPhee, Knowledge management in communities of practice, Management Communication Quarter ly 16 (2) (2002) 259–266.

[7] A. Kankanhalli, F. Tanudidjaja, J. Sutano, B. Tan, The role of IT in successful knowledge management initiatives, Communications of the ACM 46 (9) (2003) 69–73.

[8] J. Koh, Y.G. Kim, Knowledge sharing in virtual communities: an e-business perspective, Expert Systems with Applications 26 (2) (2004) 155–166.

[9] M.M. Kwan, P. Balasubramanian, KnowledgeScope: managing knowledge in context, Decision Support Systems 35 (4) (2003) 467–486.

[10] J.S.H. Kwok, S. Gao, Knowledge sharing community in P2P network: a study of motivational perspective, Journal of Knowledge Management 8 (1) (2004) 94–102.

[11] J. Lave, E. Wenger, Situated Learning, Cambridge University Press, Cambridge, UK, 1991.

[12] E.L. Lesser, J. Storck, Communities of practice and organizational performance, IBM Systems Journal 40 (4) (2001) 831–841.

[13] J. Liedtka, Linking competitive advantage with communities of practice, Journal of Management Inquiry 8 (1) (1999) 5–16.

[14] R. Maier, U. Remus, Implementing process-oriented knowledge management strategies, Journal of Knowledge Management 7 (4) (2003) 62–74.

[15] O. Mangisengi, W. Essmayr, P2P knowledge management: an investigation of the technical architecture and main process, Proceedings 14th International Workshop on Database and Expert Systems Applications, 2003.

[16] I. Nonaka, H. Takeuchi, The Knowledge Creating Company, Oxford University Press, New York, 1995.

[17] S.L. Pan, D.E. Leidner, Bridging communities of practice with information technology in pursuit of global knowledge sharing, Journal of Strategic Information Systems 12 (1) (2003) 71–88.

[18] W. Scholl, C. König, B. Meyer, P. Heisig, The future of knowledge management: an International Delphi Study, Journal of Knowledge Management 8 (2) (2004) 19–35.

[19] E. Tsui, Technologies for personal and peer-to-peer (P2P) knowledge management, Technical Report, CSC Leading Edge Forum (LEF), Australia, 2001.

[20] M.M. Wasko, S. Faraj, It is what one does: why people participate and help others in electronic communities of practice, Journal of Strategic Information Systems 9 (2) (2000) 155–173.

[21] I.V. Wartburg, K. Rost, T. Teichert, The creation of social and intellectual capital in virtual communities of practice, The fifth European conference on Organizational Knowledge, Learning and Capabilities, 2004.

[22] E. Wenger, W. Synder, Communities of practice: the organizational frontier, Harvard Business Review 78 (1) (2000) 139–145.

[23] E. Woods, Knowledge management and peer-to-peer computing: making connections, KM World 10 (9) (2001).

Chen-Ya Wang is Lecturer in Information Management at the Lunghwa University of Science and Technology, Taiwan. She has worked as a systems analyst and product manager, and is now a doctoral student in Information Management at National Taiwan University. Her current research interests are recommendation and personalization systems, web technologies and services, e-commerce, and knowledge management.

Hsin-Yi Yang is an engineer at UMC (United Microelectronics Corporation), Taiwan. She received her B.Sc. from the National Sun Yat-Sen University and M.S. in Information Management from the National Taiwan University. Her research interests are P2P computing, knowledge management, and e-commerce.

Seng-cho T. Chou is Professor in Information Management at National Taiwan University. He received his B.Sc. from the Chinese University of Hong Kong, M.S. from the University of California, and Ph.D. in Computer Science from the University of Illinois at Urbana-Champaign. His current research interests are Web technologies and services, e-business and e-commerce, knowledge management, data mining, and ubiquitous computing.
