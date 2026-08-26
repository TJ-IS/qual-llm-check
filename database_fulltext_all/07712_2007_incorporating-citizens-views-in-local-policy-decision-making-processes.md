---
otero_id: 7712
otero_key: "M6VHSA9H"
title: "Incorporating citizens' views in local policy decision making processes"
authors: "Rui Pedro Lourenço; João Paulo Costa"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.06.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 43 (2007) 1499– 1511

www.elsevier.com/locate/dss

# Incorporating citizens' views in local policy decision making processes

Rui Pedro Lourenço <sup>⁎</sup>, João Paulo Costa

Faculty of Economics, University of Coimbra, Av. Dias da Silva 165, 3004-512 Coimbra, Portugal INESC Coimbra, R. Antero de Quental 199, 3000-033, Portugal

Available online 27 July 2006

## Abstract

Local policy issues usually exhibit a high degree of complexity and uncertainty and are often characterized as “ill-structured” problems. Problem Structuring Methods (PSMs) rely on stakeholder representation and workshop format procedures to support policy making processes. We consider public participation as a way to reduce uncertainty and to improve the democratic legitimacy of those processes, and we propose a new model for e-participation (information and communication technology supported public participation), employing collaborative writing processes to produce agreed documents. These documents may then be used as formal input into the policy making process, thereby incorporating the citizens' views on those issues. A public participation support system has been developed according to this model. © 2006 Elsevier B.V. All rights reserved.

Keywords: e-Democracy; e-Participation; Public participation support system

## 1. Introduction

Local policy decision making affects our lives, as citizens, in a very crucial way. But how can we influence local policy other than by periodically casting our vote to select our representatives in the decision process?

The purpose of public participation has shifted from the 1960s and 1970s intention to democratise and legitimate policy making [1], to the participation of stakeholders in increasing the quality of policy analysis and support for policy making. These stakeholders may be defined as “organisations and individuals whose interests are affected by the policy under discussion” and it is assumed that they may provide important, high quality information to complement the use of scientific data [2]. Other authors consider that besides expert/ scientific and stakeholder information, a public participation process should include the views of “ordinary” citizens [30], considered here as “… those not holding office or administrative positions in government” [31]. This ordinary citizen participation is crucial for a number of reasons. First, it allows the shortcomings associated with stakeholder representation in deliberative institutions to be overcome [28]. It is not often easy to identify all the interests that should be considered and find a suitable representation for them. Even then, some citizens may consider themselves misrepresented by those who act as stakeholder representatives on behalf of their interests. Also, especially in local policy issues, ordinary citizens may prove to be experts in some field where they have experience and/or knowledge at least as relevant as the “official” expertise [4]. Their potential contribution (such as ideas, comments and proposed solutions) is simply wasted if they are excluded from the policy making process. Ultimately, not only does the success of implementing the outcome of the process depend on its acceptance by the citizens involved, but also it is the very cornerstone of democracy that they should influence that outcome [10].

The question is then how to include the views of ordinary citizens and support local policy decision making processes.

Local policy problems/issues are often characterized as complex societal problems, “because of the dynamic character of the problems, the many phenomena included, the many actors involved and the impact these problems have on society” [5]. They are usually considered to be “wicked” or “ill-structured” problems [10], multi-defined, hard to analyze and to handle [6]. Furthermore, they present a high degree of uncertainty, particularly with respect to the consequences of possible actions and decision making guiding values.

Problem Structuring Methods (PSMs), such as Compram [5] and Strategic Choice Approach (SCA) [7], seem to be the most appropriate to deal with problems with such characteristics. However, as Rosenhead and Mingers state, “…PSMs realize their potential most fully in use with groups in workshop format” [32]. Within the context of local policy decision making processes, this usually implies the prior identification of relevant stakeholders and the inclusion of representatives of their interests in the process. This way PSMs reduce the potentially huge number of participants (ordinary citizens) in the process, which would make it very difficult to proceed with the workshop format. Also, the cognitive effort most PSMs impose on participants prevents their use in a generalized participation context where citizens with different skills are expected to intervene.

Nevertheless, taking into consideration the representative issues mentioned above and the need to satisfy “democratic” constraints, we still consider that it is important to include the views of ordinary citizens in local policy issues. Developments in Information and Communication Technologies (ICTs), and particularly the increasing dissemination of the Internet, suggest that ICTs could be used to widen the spectrum of participants in policy making processes supported by PSMs. Our proposal is to precede the initial PSMs steps with a full public participation engagement process, supported by the World Wide Web (e-participation), which must produce a visible outcome to incorporate into the overall policy making process. We propose to organize the public participation process as a global collaborative writing process, involving ordinary citizens [20].

Participants express their ideas through individual text items supported by official documents. They may also address questions to official entities involved in the process and to other participants. All these different types of contributions are organized properly to facilitate their consultation and retrieval. A statistical model is used to help participants find “related text items” (separate text items suitable for integration into a single one) from other participants. Once two participants agree that their separate text items could be integrated, they start a collaborative writing process. This process involves deciding on a set of actions (adding a new paragraph, replacing a chapter, etc.) to perform on one of the text items so as to include the ideas expressed in the other. Each action may be assigned to one of the co-authors and it can be done synchronously or asynchronously. Once all actions are completed and the results agreed upon and integrated, a new text item emerges. This new joint text item is ready to be integrated again with other individual text items in similar pairwise collaborative writing processes. It is expected that repeating these writing efforts will lead to a smaller set of text items, each one reflecting the views and opinions shared by a particular set of participants. The aim is not to produce a single, consensual document but to support collaboration in the writing of as many documents as necessary to reflect all the different points of view, opinions and proposed actions.

These documents could be used as the citizen's input in the PSMs regarding the local policy decision making process. Details about the actual integration procedure are outside the scope of this paper since they depend on the particular PSM method being used. The nature (and decisional power) of the sponsor and the level of commitment to the outcome play an important role in motivating citizens to participate. At the very least these documents, expressing the citizen's views and opinions should be taken into account by the sponsor of a PSM supported policy making process. Even then, citizens may wish to intervene simply to take the opportunity to express their points of view and discuss them with their fellow citizens.

This paper will focus on the organization of a participation process and it is structured as follows. The next section presents several proposals (from different research areas) to support public participation processes using ICTs. In Section 3, we describe the general eparticipation model proposed, its most important concepts and the three sub-models comprising it. Section 4 details the e-participation processes outlined in Section 3. The main characteristics of the public participation support system developed are described in

Section 5. Section 6 presents some final remarks and considerations for future work.

## 2. Supporting public participation

Support for public participation should be analysed within a broader view of support for democracy itself. These digital democracy initiatives (e-democracy) may be defined as “a collection of attempts to practice democracy without the limits of time, space and other physical conditions using ICTs and CMCs (computer mediated communications) instead, as an addition, not a replacement for traditional ‘analogue’ political practices” [13]. Within e-democracy initiatives, it is customary to distinguish between two areas — one addressing e-voting and the other addressing e-engagement or e-participation. Despite the manifest interest in e-voting, we are focusing our attention on e-participation, a term used to refer to the use of ICTs in supporting the information, consultation and participation of citizens. Among ICTs, the Internet has been by far the most promising. However, its potential is still far from being fully realized, as stated by Ake Gronlund: “e-Democracy IT tools are so far mainly quite simple mainstream systems…” and “…more advanced IT tools have to be employed to support the participation” [12]. These mainstream systems include websites, e-mail, FAQ lists, chat rooms and (common) discussion forums. Attempts are being made in different research areas to propose new systems capable of unleashing some of the Internet potential and support public participation.

Current discussion forums do not properly support deliberation and informed debate since the discussion is structured with links to previous messages, providing a miscellaneous collection of vaguely associated comments. Computer Supported Argument Visualization (CSAV) [24] aims at shifting from these current online forums to forums designed constructively to visualise arguments and counter-arguments, thus enhancing the deliberation potential of these very popular systems.

Geographical Information Systems (GIS) research is looking into a participatory approach to local and regional spatial planning and has proposed new types of systems such as Public Participation Geographical Information Systems (PPGIS) [3], Web-based Public Participation Systems (WPPS) [29] and Planning Support Systems (PSS) [9]. Their functionality includes allowing Web browsing of documents and static map images, providing communication channels for discussion and voting, allowing interactive map-based queries, scenario building and on-line commenting. The main rationale behind these proposals is that an important part of local policy decision making has strong geographical references. The main limitations of these systems lie in the cognitive demands that manipulating GIS systems make on the common citizen and also in the fact that not all policy problems are geographically related.

Efforts are also being made to use Multi-Criteria Decision Making (MCDM) methods to support edemocracy initiatives [25]. An e-negotiation system is being proposed [16] under the TED project (Towards Electronic Democracy, http://bayes.escet.urjc.es/ted). The Decisionarium site (http://www.decisionarium.hut. fi — [14]) proposes a set of interactive multi-criteria decision support tools that can be used in public participation processes [26]. Again, the systems proposed so far demand a high cognitive effort from the common citizen and seem to concentrate on providing scientific information (improving communication between experts and the public).

Another research area where public participation support is currently being considered is Group Support Systems (GSS) where Turoff (and others) propose the development of a Social Decision Support System (SDSS) to “support the investigation by large groups of complex topics about which many diverse and opposing views are held” [36]. Contributions to the debate would have to be expressed as an issue, option, comment or relationship between two of them. A continuous dynamic voting system would help to filter and organize the contributions submitted. Despite the obvious improvement with regard to contribution organization, such a system would have to depend on the citizen's ability to post each contribution under the “correct” label. The danger would be of transforming the debate into a meta-debate about the correct label for each contribution (is it an option or simply a comment?).

In our opinion, these systems focus on collecting and organizing citizens' contributions but still do not respond to one of the major challenge for e-participation, scale: “how can technology enable an individual's voice to be heard and not be lost in the mass debate?” [23]. Support must be provided to allow each individual citizen to find others with a similar point of view and to incorporate his/her individual contribution into a common position. The diversity of common positions, resulting from many different convergent processes, will build into a kind of “community memory” [15]. Furthermore, this community memory must be expressed in a suitable form so as to serve as input to the PSM supported policy making process.

Among group collaborative tasks, Collaborative Writing (CW) has been one of the major GSS research areas. The growing use of the Internet and WWW as an underlying environment for collaboration has led to the development of new tools to support distributed, synchronous and asynchronous, CW on the Web — eWriting [18,22]. A recent survey on Web-based Collaborative Writing Applications (WCWAs) [27] identified 16 different systems. Most of these systems, however, were designed and built to support collaborative writing efforts of already established, relatively small, cohesive, groups, and therefore do not take into account group formation and specific coordination support. Others, like the Wiki Wiki Web [19], support on-line editing of Web pages accessible to everyone but offer no real guarantee of a stable and convergent process of producing an agreed document. This illustrates the importance of outlining and programming actions before the actual writing occurs. Also, none of these systems offer a specific communication function to help coordinate the collaborative efforts and to allow for a clear separation between content and coordination information.

As for the e-democracy initiatives, the fact that not all citizens are sufficiently computer literate (the so called “digital divide”) to participate in them is a major concern. However, we must not forget that social and economic conditions already limit the access to “analog” media, thus making it very difficult for some citizens to make their voices heard [11]. ICTs (and particularly the Internet) not only give ordinary citizens the opportunity to express their points of view but may also attract some who are not willing to participate in face-to-face events. Nevertheless, provisions must be made to ensure that alternative channels of participation (“analog” ones) are available.

The major goal of our work is to propose a way to organise a public participation process, using the Internet as communication infrastructure, and to provide the necessary support for the participants (ordinary citizens) to relate their contributions to those of others, and try to express common views, opinions and options. In our model, participants express their ideas individually − divergent phase − and then search for related ideas from other participants. Step by step, related ideas are integrated into a common document through the pairwise collaborative writing efforts of their respective authors. The aim is not to produce a single, consensual document but to collaborate in the writing of as many documents as are needed to reflect all the different points of view, opinions and proposed actions. These documents could then be used as formal input to the global policy making process, not in a legally binding way, but giving political decision makers the chance to analyze the output of the participation process and act according to their political responsibility.

## 3. Proposed e-participation model

Our view of e-participation is based on three types of model: how to properly organize contributions (discussion structure), how to relate contributions (search for related ideas from other participants) and how to integrate contributions (collaborative writing model). These models are built around two key concepts: participants and contributions.

## 3.1. Participants

The different participants involved in a public participation process can be identified as: the sponsor, the facilitator, associated official entities, contributors and observers.

A public participation process begins when someone or some entity decides to promote a citizens' debate on an issue of public interest. Typically, this entity will be an Official Local Authority, a Citizens' Association or NGO, and it will be referred to as the sponsor. It is the sponsor's responsibility to provide the necessary framework for the participation process.

It is the facilitator's responsibility to provide extensive technical and task support including, for instance, blocking “inappropriate” contributions and participants. The credibility of both sponsor and facilitator is very important to ensure that the democratic nature of the participation process is maintained and that there is no censorship.

Access to relevant information is a pre-requisite for engaging in deliberation [17]. Therefore, as many official entities as possible (or their political representatives) should be assembled, not only to answer any questions that may arise but also to provide the documents and data necessary to support the discussion process.

All citizens are potential observers or contributors to the public participation process. However, those that actually want to contribute with their opinions and proposals (contributors) need to register. Nevertheless, to avoid problems such as evaluation apprehension [8], all contributions are presented to others strictly anonymously. Contributors are, in fact, the key participants in the deliberation process and therefore the two terms will be used without distinction.

## 3.2. Contributions

There are several ways a contributor may intervene in the public participation process. The most usual way is to submit a text item with proposals for policies and actions or comments (viewpoints, arguments, rationales or positions) about a certain issue. Within a text item,

Table 1

every reference to a specific document or to specific data should be accompanied by the relevant support documents (such as scientific articles, research reports, plans and maps, statistics or budget figures), which constitute another type of contribution. Alternatively, it is possible to make a request for a document that any participant may afterwards respond to by submitting the relevant document. Finally, any participant may pose questions directly to other participants and answer those questions addressed to him/her.

The text item is the centrepiece of the whole deliberation process. It is composed of a title, one or more chapters (and sub-chapters) and a list of keywords. Each chapter is composed of a title and a number of paragraphs which may include, besides the text itself, a list of references to the support documents. To limit the inclusion of low interest (or even not understandable) text items in the process without compromising its democratic nature, it is required that each text item should be endorsed by a sufficient number of contributors.

Each text item has also an author (contributor of the original text item — see details in Section 3.5), a list of co-authors (who have enhanced the original text item through collaborative writing) and a list of subscribers. A contributor may have different roles with respect to different text items. The author of a text item is responsible for facilitating collaborative writing processes with other contributors and for answering questions regarding his/her text items.

## 3.3. Discussion structure

A very common approach to categorizing contributions within group discussions uses discourse structures, defined as “a template for a discussion structure which allows individuals to classify their contributions to the discussion into meaningful categories that structure their relevance and significance according to the nature of the topic, the objective of the discussion and the characteristics of the group” [35]. Each type of contribution needs to be organised in a way that facilitates its consultation and constitutes a base for the collaborative authoring of joint text items (convergent task).

The importance and type of discussion structure to adopt depends on the number of participants/contributions to be organised and the type of analysis to be performed on the contributions. For instance, a simple question–reply discourse structure like the one usually adopted in forums may be suitable for a very large number of participants/contributions because no one is really very interested in analysing other contributions except those immediately surrounding his/hers. The same structure, used by fewer participants with fewer contributions, may allow for some degree of analysis. Discourse structures where participants have to categorize their contributions according to their content (e.g. opinion, proposed action, pro/con argument, etc.) could deter some citizens from participating, may not be suitable for less prepared contributors and may drive the discussion into a meta-discussion. Instead of focusing on the discussion of policy issues, contributors may embroil themselves in a discussion as to whether each contribution has been classified in the correct category. We therefore propose to treat all text contributions alike, regardless of their content, and define a discussion structure only to establish links between the contributions being integrated and links with other elements of the public participation process, as presented in Table 1.

The “integrate” link is a key part of the collaborative writing model and it will be further explained in the sections that follow. The “support” link between text items and documents reflects the need to support statements made within text items with the relevant documents (statistical data, scientific articles, etc.) and, for each text item, corresponds to its list of references. The remaining links reflect the natural relations between the different types of contribution. On a semantic level, it is possible to define a model to identify related text items and therefore establish a network of implicit links between them, as explained in the next subsection.

## 3.4. Related contributions (text items) and automatic text analysis

It is very useful to be able to find text items related to a particular one, either to initiate a collaborative writing process to integrate them, or simply to find out what other participants have to say about the same subject. For this purpose, an adapted vector-space model [33] is used. Each text item is automatically checked against a list of words (verbs and common nouns in all their forms) and a list of corresponding stems (verb forms and singular/masculine form of nouns — where relevant) is suggested to serve as text item keywords. The final list of keywords (as mentioned in the previous section) with their respective weights (term vector) represents each text item. According to this model, a term that occurs frequently in a particular text item but rarely in the other text items is assigned a greater weight since it is able to make that text item distinct from the others. Typically, a keyword weight of this type (known as term frequency and inverted document frequency) may be defined [34] as

Contributions and links between them

<table><tr><td></td><td>Text item</td><td>Document</td><td>Request for document</td><td>Question</td><td>Answer</td></tr><tr><td>Text item</td><td>Integrate</td><td>Support</td><td>Link</td><td>Link</td><td></td></tr><tr><td>Document</td><td>Support</td><td></td><td>Link</td><td></td><td></td></tr><tr><td>Request for document</td><td>Link</td><td>Link</td><td></td><td></td><td></td></tr><tr><td>Question</td><td>Link</td><td></td><td></td><td></td><td>Link</td></tr><tr><td>Answer</td><td></td><td></td><td></td><td>Link</td><td></td></tr></table>

$$
w _ {i k} = \frac {t f _ {i k} \times \log (N / n _ {k})}{\sqrt {\sum_ {j = 1} ^ {1} \left(t f _ {i j}\right) ^ {2} \times \left(\log (N / n _ {j})\right) ^ {2}}}\tag{1}
$$

where $w _ { i k }$ is the weight of the keyword k relative to text item $i , t f _ { i k }$ is the frequency of occurrence of keyword k in text item i, N is the total number of text items, $n _ { k }$ represents the number of text items with keyword k and l is the number of keywords considered. This weight is normalized to account for differences in the number of assigned keywords.

Given two text item term vectors, $D _ { j }$ and $D _ { i } ,$ it is possible to compute a degree of similarity between those two text items using the vector similarity function of the form

$$
\operatorname{sim} \left(D _ {j}, D _ {i}\right) = \sum_ {k = 1} ^ {l} w _ {j k} w _ {i k}\tag{2}
$$

Using this model, it is possible to identify related text item contributions and their respective degree of similarity in a fully automated procedure. However, to account for semantic aspects and a potentially large number of stems, it is best if the author intervenes manually and chooses from the automatically suggested stems those that best act as keywords. This will provide the starting point for the collaborative writing model.

## 3.5. Collaborative writing

The entire public participation process may be considered as a global collaborative writing process where anonymous citizens try to draw up, not one, but as many documents as necessary to express their different points of view, ideas and proposals for action.

Current CW models (and supporting systems) are adapted to collaborative writing processes involving relatively small and cohesive groups (see Section 2). Public participation processes exhibit two important distinguishing characteristics: there is no pre-formed stable group and the number of potential participants is huge.

In the public participation process, participants start by expressing their ideas on separate text items and then try to integrate them with ideas from other participants. Once two participants agree that their individual text items could be joined together as a single unit, they form an ad-hoc collaborative writing group. The authoring process takes one of the two text items as baseline and changes it to incorporate the ideas of the other text item. The two authors jointly compile a list of operations to be made on the baseline text item (“add chapter”, “delete paragraph”, “change title”, etc.) and assign the operations between them. They also define which operations could be done asynchronously and establish a deadline by which the operations should be completed. Asynchronous operations are executed by the author to whom they are assigned and the result (usually a piece of text) is presented before the agreed deadline. In synchronous mode, all operations made by each author are immediately visible to the other, and there is a separate communication channel that allows them to comment on one another's work. A new version of the “integrated” text item is created when all operations are completed and the results are accepted by both authors. The global participation process may then proceed with the integration of other ideas, expressed in other text items. This way, participants have the opportunity to progressively add their efforts and help to produce a set of documents that may be considered the “end result” of the public participation process.

## 4. Proposed e-participation processes

Having presented a proposal for a global eparticipation model, the processes outlined by the model must now be described in greater detail, with emphasis on the text item contribution, since the procedures for all the other types of contributions are more or less straightforward. Fig. 1 presents a general view of e-participation processes. Initially, all participants must register. Only then can they access any of the other three core processes. They may begin to prepare and submit contributions (particularly text items) to express their ideas and points of view. Alternatively, participants may subscribe to other participants' text items and avoid submitting redundant contributions. This also provides a mechanism to filter “irrelevant” contributions (those that do not gain enough support). Finally, participants may get involved in collaborative writing processes to integrate pairs of text items. This process comprises a set of actions (as presented in Fig.

![](/api/attachments/M6VHSA9H/fulltext/images/f4c62fae0b021a8c900c61efd0a4afbba78212d5486cfb546751f0ef9a0bca79.jpg)  
Fig. 1. e-Participation processes.

1) which may depend on the author's role in the process (see explanation in sections below).

## 4.1. Registering as contributor

Participants must first register before they can submit contributions. The main purpose of registration is to allow traceability between contributions and authors, which is fundamental to conducting the collaborative authoring process (providing the right authors with the means to integrate their contributions) and to the endorsement mechanism (preventing repeated endorsements of the same item and allowing subscribers to withdraw their support). In any case, all contributions will be presented publicly, without any reference to their authors.

Registering also makes it possible to create “participant-specific working areas” where each participant receives information that directly concerns him/her such as pending questions, own text items waiting for subscription, own text items waiting to initiate or already undergoing the collaborative authoring process, and coauthored contribution progress. Finally, registering is important for guaranteeing access security and for establishing some kind of accountability that may be used by the facilitator to block “inappropriate” participants.

## 4.2. Subscribing to a contribution from another author

The first objective of the subscription mechanism is to deal with the expected information overload in a public participation process by ensuring the relevance of accepted contributions (text items) and reducing redundant ones. To start with, all text items get an initial “pending” status and become available for subscription for a certain period of time. During that time, participants are expected to endorse those text items that they find relevant, instead of submitting similar ones. Once a text item gets enough support, it gets the “accepted” status and becomes part of the community knowledge base. Since every participant must be registered, it is possible to ensure that he/she endorses each text item once only and may withdraw his/her endorsement at any time.

## 4.3. Preparing and submitting a new text item

New text items are expected to be truly innovative in relation to previously submitted ones. During the preparation of a new text item, the author may search for similar contributions and opt to support them instead of submitting a redundant one. The author must also be sure that all data (such as statistics and figures) and documents mentioned in the contribution are already available for discussion. Otherwise, it is better to submit them or issue a “request for a document” before submitting the text item. It is the author's responsibility to define the correct “support” links (list of references) between the new text item and those support documents. To build the list of keywords, the author starts with the list of suggested word stems (and respective weight according to expression (1)) provided by the automatic text analysis of the supporting system. He/she may then remove some of the stems, add new ones or increase/ decrease the importance (weight) of existing ones. The final list will constitute the list of keywords “defining” the new text item (term vector), used to find related text items and to initiate the collaborative writing processes.

Each collaborative writing process involves several sub-processes, as outlined in Fig. 1, which will be detailed in the subsections that follow.

## 4.4. Defining and accepting an “integrate” link between two text items

Each integration process is based on the creation of an ad hoc collaborative writing group composed of two participants who consider that their individual text items may be combined into a single one. One participant identifies a text item from another participant and expresses his/her wish to start a collaborative writing process by creating an “integrate” link (see Section 3.3) between the two text items. Since this is a directional link (meaning one text item will be integrated into the other), we will refer to the two text items as “source” (origin of the link) and “baseline” (destination of the link) to better explain the process. The same designation applies to the respective authors. It is up to the “baseline” author to accept or reject the link (and the corresponding integration process). Both text items must have enough supporting participants (to be considered relevant) and the “baseline” text item may not be currently undergoing another integration process. If accepted, an iterative process begins to integrate one into the other and, from that moment on, a “private communication channel” is established between the two participants involved, and this will support the whole collaborative writing process.

Within the collaborative process both authors propose actions to be performed, execute the actions assigned by the “baseline” author, review the actions' results and, finally, accept (or reject) the “integrated” text item. The “baseline” author is the facilitator of the collaborative process with the responsibility for assigning the actions to be executed by each author, establishing a time schedule for their completion and deciding which will be done synchronously.

## 4.5. Creating and managing a “to do” list of actions

A list of “to do” actions is used to coordinate the integration effort between the two authors. For instance, if the author of the “source” text item believes that his/ her idea could be incorporated into the “baseline” text item just by adding a new paragraph to the end of Chapter 3.1, then he/she may propose the action “Add a new paragraph to the end of Chapter 3.1” to be included in the “to do” list.

Both authors may suggest actions to be included in the “to do” list at any time. In fact, the “source” author may complement the “integrate” link with the actions he/she considers necessary to conclude the integration process. This may be an extra argument to convince the “baseline” author to accept the integration process.

Not all the actions need to be assigned to one of the authors at the same time. The “baseline” author chooses which of the proposed actions will in fact be executed and in what order. Some of the actions do not even need to be assigned. For instance, an action to “delete a certain paragraph” just needs to be approved by both authors. It is the “baseline” author's responsibility to assign each of the “executable” actions to one of the authors, to decide which actions should be done synchronously and to define a deadline by which a set of actions must be completed.

## 4.6. Executing and evaluating the actions

Each author is responsible for executing separately those asynchronous actions assigned to him/her and for submitting the results before the deadline established by the “baseline” author. Those actions which are to be executed synchronously require the authors to agree on a specific time to meet on the Internet (considering, for instance, a time schedule presented with the “integrate” link). When they are both online, the authors have the opportunity to execute actions marked as synchronous and at the same time comment via a separate channel (chat-like) as the work progresses. It is expected that these actions will be better coordinated and the results better accepted by the two authors since they have had the opportunity to influence how they were carried out.

Regardless of the way the actions have been executed, both authors have to accept their results before they are incorporated into a new version of the “integrated” text item. Some results may be rejected (with due justification) and the respective actions may be reassigned or simply eliminated from the “to do” list.

## 4.7. Creating the integrated text item

Throughout the entire collaborative writing process it is up to the “baseline” author to decide when to create a new version of the “integrated” text item and which accepted results should be incorporated into that version. This dispenses with the need to wait for all actions to be completed before creating a new version of the “integrated” text item. Every new version of the “integrated” text item must be evaluated by both authors to decide whether it is a final version, accepted by both of them, or just an intermediate version, still requiring some actions to be performed.

Once a successful integration process ends, the “source” author must decide whether his/her original contribution should remain as a separate contribution to be used in future collaborative writing processes with other text items.

The “baseline” author remains the author of the “integrated” text item and the “source” author (together with all co-authors of the “source” text item) enters the list of co-authors of the “integrated” text item.

It is the responsibility of the author of the “integrated” text item to choose the new list of keywords. As in any other text item, the author must choose a restricted list of stems to serve as keywords, considering the complete list of stems recognized and presented automatically by the system and their respective weight.

It is expected that repeating these pairwise collaborative writing efforts will lead to a smaller set of documents, each one reflecting the common views and opinions of a particular set of participants. This way, not only does the number of fragmented and redundant contributions diminish, but it is also possible to obtain a written outcome of the global e-participation process and, consequently, a written input to the policy making process.

The next section will describe the main features of the system developed to support public participation using this collaborative writing model.

## 5. Public participation support system

Naturally, the support system was developed considering the Internet as its communication infrastructure, and thus being accessible through normal browsers. Some features are implemented using signed Java applets and therefore require the installation of a Java Virtual Machine.

Participants may access the website either as “guests” or as full registered participants. “Guests” may only view the information but cannot really participate (submit text items, collaboratively write joint contributions, etc.). Once logged in, each participant is notified about events that occurred since his/her last participation (new questions posed to him/her, new answers to his/her questions, “integrate” links proposed or accepted, etc.). All information is presented in a way similar to that shown in Fig. 2.

![](/api/attachments/M6VHSA9H/fulltext/images/ade39aee0cbe139a2158c0c5ee9ab94c06b915e4efb2a44fb23c923f9aa15d0c.jpg)  
Fig. 2. Collaborative writing processes (“integrate” links).

It is possible to filter the information presented using the “new contexts” section on every screen and perform related actions either by using the “actions” section on the left or by using the “action buttons” inside the grid. The Java applet at the bottom of each screen is called the Network Monitor. Its function is to detect any request for synchronous activity (collaborative writing related) from any other author while the participant is online and allow the participant to accept/reject the request (see description below). Registered participants may subscribe to other participants' text items or they may prepare their own. Once a new text item is submitted, the author may try to merge it with other text items by proposing an “integrate” link to the corresponding authors.

Fig. 2 shows the screen where “integrate” links (corresponding to ongoing collaborative writing processes) are managed. Each participant can immediately see in which collaborative writing processes he/she is participating and in what role (“source” or “baseline” author). Also, if such a process has been “accepted” by the “baseline” author (see Fig. 1), then it is possible to start a synchronous session with the other author by pressing one of the two buttons available in the “actions” column. If the other author is currently online when such a button is pressed, then his/her Network Monitor informs him/her that a request is being made to begin a synchronous session.

Depending on the request type (manage and/or execute integrate actions, or produce the “integrated” text item), a particular applet will be launched for both authors. Fig. 3 presents the applet developed to synchronously manage the integrate actions and/or execute them, and Fig. 4 presents the applet for developing the “integrated” text item the end result of the collaborative writing process.

Note that, according to Section 4.6, it is possible to conduct a collaborative writing process asynchronously without needing the Java applets. The applet from Fig. 3 allows both authors to synchronously propose new “integrate” actions to be executed in the process of producing the “integrated” text item. This corresponds to the outlining activity of collaborative writing, involving “the creation of a high-level direction for where the document will be going, including major sections and subsections” [21]. It is up to the “baseline” author to execute (write) one of the non-finished actions

![](/api/attachments/M6VHSA9H/fulltext/images/413bffe4b89c29b12ec6c5a706cbf6f378917c86a3d523c6bf2f914f08cff323.jpg)  
Fig. 3. Managing and executing “integrate” actions.

![](/api/attachments/M6VHSA9H/fulltext/images/64ab082dab29a0e35fdff92b30a514ce33e6be78c8dd38a21b6ae6afe37c7bc6.jpg)  
Fig. 4. Producing the “integrated” text item.

synchronously, using the writing area below. Once an action is selected to be executed (for instance, write a certain paragraph), it is possible for both authors to simultaneously start executing it. The applet allows two writers to simultaneously write the same paragraph although some degree of coordination may be necessary to avoid incoherent (although formally correct) common text (e.g., if both authors start writing on exactly the same position the result will be an incoherent text but both authors will observe exactly the same final piece of text). This coordination is achieved through the use of the chat area displayed on the left side of the screen. Once again, it is the responsibility of the “baseline” author to conclude that an action is finished and save the corresponding result for subsequent integration in the final text item. It is expected that, since these actions are being executed in the presence (and with the direct collaboration) of both authors, the end result will be agreed upon by both authors. This is a major advantage over the asynchronous execution of actions done by each author separately.

The applet from Fig. 4 is used by the “baseline” author to produce the “integrated” text item taking into consideration the results of those actions already executed. The “source” author uses the same applet simultaneously to watch and comment on the final result as it is being produced by the “baseline” author. In the end, it is possible for the “source” author to evaluate the final “integrated” text item thus effectively ending the collaborative writing process. Once again, there is a chat area (on the right) which allows for communication between the two authors during the final integration efforts.

The applets presented here illustrate some of the core characteristics of the public participation support system developed. They are essential to the execution of synchronous actions between pairs of participants engaged in collaborative writing efforts. However, all operations can be executed asynchronously using the website in which these applets are integrated.

## 6. Final remarks and future work

Support for local policy decision making processes must take certain aspects into account:

• Local policy problems (or issues) are usually considered to be “wicked” or “ill-structured” and exhibit a high degree of uncertainty (with respect to the consequences of possible actions and decision making guiding values);

• Besides expert and stakeholder representative information, these processes should include the views of ordinary citizens as a way of reducing uncertainty and improving the democratic legitimacy of those processes;

• The spreading use of Internet has raised expectations that it may be used to promote public participation (edemocracy initiatives) but those expectations have not yet been fully met.

PSMs are often used to support policy making processes but they usually take the form of workshops involving experts, stakeholder representatives and political decision makers, leaving out the possibility of ordinary citizens directly influencing the policies that affect their daily lives.

To incorporate citizens' views in local policy making processes we propose to complement PSMs with a public participation process, organized as a global collaborative writing process between ordinary citizens and using the Internet as its communication infrastructure. In our model, participants express their ideas individually − divergent phase − and then search for related ideas from other participants. Step by step, related ideas are integrated into a common document through the pairwise collaborative writing efforts of their respective authors — convergent phase. The expected output of such a process is a set of documents containing the many different views, proposals and opinions expressed. These documents may simply be used within the PSMs context as working documents or the “reduced set” of citizens (authors of the final set of documents) could itself be considered as representative of the many citizens that endorse and co-author these documents. In this case, these authors would become “real” stakeholder representatives and act as such within the PSMs context.

A system has been developed to support this collaborative writing model of public participation. It allows citizens to ask questions to relevant official entities and to browse through the documents (maps, official statistics, etc.) essential to forming an informed opinion, which may be expressed in separate text items or simply by subscribing to other citizens' points of view. The system also helps each author to find text items from other authors suitable for combining into a single, “integrated” text item. Using the statistical model described on Section 3.4, participants may search for text items according to specified words, find text items similar to a specific one, or with higher degree of similarity to those already submitted by the participant. Different collaborative writing strategies are allowed depending on the discretion of the responsible (“baseline”) author. Activities such as outlining, research and writing are supported. The entire collaborative writing process is transparent to all other citizens, even those not registered. As it is an Internet-based system, it is able to support a participatory process in a medium-sized city and can be scaled up, if necessary, with more computing power and larger bandwidth access.

Further research efforts are needed to evaluate the effectiveness of the participation model, the support system and the way to thoroughly integrate the collaborative writing process with the PSMs, keeping in mind that the ultimate goal is to provide a greater level of influence from common citizens on local policy decision making processes. This influence could come, not from the mandatory nature of the participatory process, but from the pressure applied to administrative power by public opinion expressed in a structured and coherent way.

## Acknowledgements

This paper was supported by POCTI/EGE/58828/ 2004.

## References

[1] S.R. Arnstein, A ladder of citizen participation, Journal of the American Institute of Planners 8 (1969).

[2] F.J. Bongers, Participatory Policy Analysis and Group Support Systems, Tilburg University, 2000.

[3] S. Carver, A. Evans, R. Kingston, I. Turton, Public participation, GIS, and cyberdemocracy: evaluating on-line spatial decision support systems, Environment and Planning. B, Planning and Design 28 (6) (2001).

[4] S. Coleman, J. Gøtze, Bowling Together: Online Public Engagement in Policy Deliberation, Hansard Society and BT, 2001.

[5] D.J. DeTombe, Compram, a method for handling complex societal problems, European Journal of Operational Research 128 (2) (2001).

[6] D.J. DeTombe, Introduction to the field of methodology for handling complex societal problems, European Journal of Operational Research 128 (2) (2001).

[7] J. Friend, The strategic choice approach, in: J. Rosenhead, J. Mingers (Eds.), Rational Analysis for a Problematic World Revisited, John Wiley & Sons, 2001, pp. 115–149.

[8] R.B. Gallupe, A.R. Dennis, W.H. Cooper, J.S. Valacich, J.F. Nunamaker, L. Bastianutti, Electronic brainstorming and group size, Academy of Management Journal 35 (2) (1992).

[9] S. Geertman, Participatory planning and GIS: a PSS to bridge the gap, Environment and Planning. B, Planning and Design 29 (1) (2002).

[10] J.L.A. Geurts, C. Joldersma, Methodology for participatory policy analysis, European Journal of Operational Research 128 (2) (2001).

[11] T.F. Gordon, G. Richter, Discourse support systems for deliberative democracy, in: R. Traunmuller, K. Lenk (Eds.), E-Government: State-of-the-Art and Perspectives (EGOV), Springer-Verlag, Aix-en-Provence, 2002, pp. 248–255.

[12] A. Gronlund, e-Democracy: in search of tools and methods for effective participation, Journal of Multi-Criteria Decision Analysis 12 (2–3) (2003).

[13] K.L. Hacker, J. van Dijk, What is digital democracy? in: K.L. Hacker, J. van Dijk (Eds.), Digital Democracy: Issues of Theory and Practice, SAGE Publications, London, 2000, pp. 1–9.

[14] R.P. Hämäläinen, Decisionarium—aiding decisions, negotiating and collecting opinions on the Web, Journal of Multi-Criteria Decision Analysis 12 (2–3) (2003).

[15] S.R. Hiltz, M. Turoff, The Network Nation: Human Communication via Computer, MIT Press, 1993.

[16] D.R. Insua, J. Holgado, R. Moreno, Multicriteria e-negotiation systems for e-democracy, Journal of Multi-Criteria Decision Analysis 12 (2–3) (2003).

[17] N. Jankowski, M. van Selm, The promise and practice of public debate in cyberspace, in: K.L. Hacker, J. van Dijk (Eds.), Digital Democracy: Issues of Theory and Practice, SAGE Publications, London, 2000, pp. 149–165.

[18] H.-C. Kim, From comments to dialogues: a study of asynchronous dialogue processes as part of collaborative reviewing on the Web, Proceedings of the 35th Hawaii International Conference on System Sciences (Hawaii, 2002).

[19] B. Leuf, W. Cunningham, The Wiki Way: Quick Collaboration, Addison-Wesley, 2001.

[20] R. Lourenço, J.P. Costa, Supporting eParticipation through structured discussion and collaborative writing, Proceedings of the 4th European Conference on eGovernment (Dublin, Ireland, 2004).

[21] P.B. Lowry, Improving distributed collaborative writing over the internet using enhanced processes, proximity choices, and a Javabased collaborative writing tools, PhD thesis (Graduate College, University of Arizona, 2002).

[22] P.B. Lowry, C.C. Albrecht, J.D. Lee, J. Nunamaker, Users experiences in collaborative writing using Collaboratus, an Internet-based collaborative work, Proceedings of the 35th Hawaii International Conference on System Sciences (Hawaii, 2002).

[23] A. Macintosh, Using information and communication technologies to enhance citizen engagement in the policy process, Promises and Problems of e-Democracy; Challenges of Citizen On-line Engagement, OECD, Paris, 2003.

[24] A. Macintosh, A. Renton, Argument visualisation to support democratic decision-making, Proceedings of the eChallenges e.2004 Conference (Vienna, Austria, 2004).

[25] J.M. Moreno-Jiménez, W. Polasek, e-Democracy and knowledge. A multicriteria framework for the new democratic era, Journal of Multi-Criteria Decision Analysis 12 (2–3) (2003).

[26] J. Mustajoki, R.P. Hamalainen, M. Marttunen, Participatory multicriteria decision analysis with Web-HIPRE: a case of lake regulation policy, Environmental Modelling & Software 19 (6) (2004).

[27] S. Noel, J.-M. Robert, How the Web is used to support collaborative writing, Behaviour & Information Technology 22 (4) (2003).

[28] J. O'Neill, Representing people, representing nature, representing the world, Environment and Planning. C, Government & Policy 19 (4) (2001).

[29] Z.-R. Peng, Internet GIS for public participation, Environment and Planning. B, Planning and Design 28 (6) (2001).

[30] O. Renn, T. Webler, P. Wiedemann, A need for discourse on citizen participation: objectives and structure of the book, in: O. Renn, T. Webler, P. Wiedemann (Eds.), Fair and Competent Citizen Participation: Evaluating New Models for Environmental Discourse, Kluwer Academic Publishers, 1994, pp. 1–15.

[31] N. Roberts, Public deliberation in an age of direct citizen participation, The American Review of Public Administration 34 (4) (2004).

[32] J. Rosenhead, J. Mingers, A new paradigm of analysis, in: J. Rosenhead, J. Mingers (Eds.), Rational Analysis for a Problematic World Revisited, John Wiley & Sons, 2001, pp. 1–19.

[33] G. Salton, Automatic Text Processing, Addison-Wesley, Reading, MA, 1989.

[34] G. Salton, J. Allan, C. Buckley, Automatic structuring and retrieval of large text files, Communications of the ACM 37 (2) (1994).

[35] M. Turoff, S.R. Hiltz, M. Bieber, J. Fjermestad, A. Rana, Collaborative discourse structures in Computer Mediated Group Communications, Proceedings of the 32nd Hawaii International Conference on System Sciences (Hawaii, 1999).

[36] M. Turoff, S.R. Hiltz, H.-K. Cho, Z. Li, Y. Wang, Social Decision Support Systems (SDSS), Proceedings of the 35th Hawaii International Conference on System Sciences (Hawaii, 2002)

![](/api/attachments/M6VHSA9H/fulltext/images/0a3b370ec1681272317beec20d03a662dda7e9cea623f0b25a46a43416a5ca1d.jpg)  
Rui Pedro Lourenço is a Teaching Assistant (information systems) at the Faculty of Economics, University of Coimbra, Portugal. His research interests include Group Support Systems and their applicability in public participation concerning local policy issues (e-Participation). He holds an MSc in Information Management from the University of Coimbra and he is currently enrolled in a PhD research program at the same University.

![](/api/attachments/M6VHSA9H/fulltext/images/6d49725edfdfdb9f3386a6b54af312cbd5327059c3518b09305cf78f4be1fc65.jpg)

João Paulo Costa is an Associate Professor at the Faculty of Economics, University of Coimbra, Portugal. His research interests include Decision Support Systems, Information Systems and Multicriteria Decision Analysis. He holds a PhD in Business Economics from the University of Coimbra.
