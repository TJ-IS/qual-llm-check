---
otero_id: 8894
otero_key: "KKANXWAC"
title: "Design, Implementation, and Evaluation of Trust-Supporting Components in Virtual Communities for Patients"
authors: "JAN MARCO LEIMEISTER; WINFRIED EBNER; HELMUT KRCMAR"
year: "2005"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2005.11045825"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/KKANXWAC/fulltext/images/47df172329f68263a60cbd4ffe3c33bf8cff885238b503a3f07509dd3bf1cb1c.jpg)

# Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# Design, Implementation, and Evaluation of Trust-Supporting Components in Virtual Communities for Patients

JAN MARCO LEIMEISTER <sup>a</sup> , WINFRIED EBNER <sup>a</sup> & HELMUT KRCMAR a

<sup>a</sup> Technische Universität München, Munich, Germany

Published online: 08 Dec 2014.

To cite this article: JAN MARCO LEIMEISTER , WINFRIED EBNER & HELMUT KRCMAR (2005) Design, Implementation, and Evaluation of Trust-Supporting Components in Virtual Communities for Patients, Journal of Management Information Systems, 21:4, 101-131

To link to this article: http://dx.doi.org/10.1080/07421222.2005.11045825

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http:// www.tandfonline.com/page/terms-and-conditions

# Design, Implementation, and Evaluation of Trust-Supporting Components in Virtual Communities for Patients

JAN MARCO LEIMEISTER, WINFRIED EBNER, AND HELMUT KRCMAR

JAN MARCO LEIMEISTER is a Senior Researcher and Assistant Professor at the Chair for Information System, Technische Universität München, Munich, Germany. He manages the research project COSMOS (Community Online Services and Mobile Solutions), funded by the German Ministry for Research and Education. Dr. Leimeister received a Ph.D. for his work on the systematic development of virtual communities for patients for Hohenheim University, Stuttgart, Germany, where he also graduated in Business Administration (majors in Information Systems). He has worked for companies such as DaimlerChrysler, IBM, and Siemens Business Services. His teaching and research areas include online communities, ubiquitous and mobile computing, CSCW, and information management.

WINFRIED EBNER is a Researcher and Scientific Assistant at the Chair for Information Systems, Technische Universität München, Munich, Germany. He developed the Executive Education Program “Communicate!—Communication and Leadership”— a joint project of the Bertelsmann Stiftung, Heinz Nixdorf Stiftung, DaimlerChrysler-Fonds, and Technische Universität München. He graduated in 2002 in Communications Science (majoring in Information Systems) at the Hohenheim University, Stuttgart, Germany. He worked for companies such as Otto Versand, Kienbaum Consultants International, and EddieBauer Inc. His research interests include information management, individual communication, and mediated leadership.

HELMUT KRCMAR holds the Chair for Information Systems, Technische Universität München, Munich, Germany. Prior to this, he worked as a Post Doctoral Fellow at the IBM Los Angeles Scientific Center, as Assistant Professor of Information Systems at the Leonard Stern School of Business, NYU, and at Baruch College, CUNY. From 1987 to 2002 he was Chair for Information Systems, Hohenheim University, Stuttgart, Germany. In 2002–2 he served as Dean, Faculty of Business, Economics, and Social Sciences. His research interests include information and knowledge management, and computer-supported cooperative work.

ABSTRACT: Trust provides the foundation for the successful implementation and operation of a virtual community (VC). Trust is an especially relevant success factor in online health-care communities. A look at existing communities leads to the conclusion that many VCs fail to meet requirements upon which trust is established. Based on the findings in the literature and the researchers’ experience, this paper describes how trust-enabling functionalities can be systematically designed and implemented in a VC for cancer patients. Consequently, the outcomes of these design measures are evaluated. The evaluation results show that supporting trust can be achieved following a two-step model. The presented components support the perceived competence and perceived goodwill of the operators and the other members. Perceived goodwill and competence then support the process of creating and sustaining trust between members as well as between members and the operators of the VC and contribute to the successful implementation and maintenance of the community. The paper concludes with a discussion on further trust-supporting components yet to be implemented and gives recommendations for further research in this area.

KEY WORDS AND PHRASES: access rights, anonymity, health care, online community, perceived competence, perceived goodwill, quality-assured content, transparency criteria, trust, virtual community.

THE OBJECTIVE OF THE WORK DESCRIBED in this paper was to design, implement, and evaluate different trust-enabling functionalities in a virtual community (VC) for German cancer patients (for a closer look at the community, please visit the Web site www.krebsgemeinschaft.de).

There are two reasons why trust and trust-supporting functionalities are of major importance for building and nurturing a VC for cancer patients, as compared with other VCs. First, the members of the community are more elderly people, as the occurrence of cancer is correlated to age. Even if these persons are interested in the Internet and the community, they treat the “new” media with skepticism. Second, the life-threatening situation of cancer patients and the taboo topic “cancer” itself requires a high level of trust. The theoretical body of knowledge on trust and on supporting trust has not yet been substantiated for VCs, and the theoretically grounded design of trust-supporting components in VCs in general has hardly been addressed. Even less emphasis has been placed on high-involvement communities such as communities for patients. The theoretical rationale of this work was to verify existing models of trust and trust-supporting factors for areas of application previously not researched.

## Trust and Building Trust—Some Fundamental Considerations

Trust is a basic organizing principle of interpersonal exchange relations [43, 44]. It can be described as the problem of acting without knowing the reaction of the exchange partner in advance [28]. Trust has been defined from several scientific perspectives: sociology, philosophy, socio-psychology, and economics [1]. For purposes of this study, we use the following definition by Gambetta: “Trust (or, symmetrically, distrust) is a particular level of the subjective probability, with which an agent will perform a particular action, both before [we] can monitor such an action . . . and in a context in which it affects [our] own action” [16, p. 217].

In accordance with Gambetta’s definition, one perspective of research focuses on how factors such as ability, benevolence, and integrity contribute to trust building [30, 40], whereas another perspective focuses on the trust-building processes. Five processes have been identified [10, 29]: a calculative process (a trustor develops trust based on the calculation of the cost and reward for a trustee to cheat or to cooperate in a relationship); a prediction process (a trustor develops trust by predicting a trustee’s future actions based on his past); a capability process (a trustor develops trust based on an evaluation of the trustee’s ability to fulfill his promises); an intentionality process (a trustor develops trust based on his perception of the intentions of the trustee); and a transference process (a trustor develops trust based on transferring trust from a known entity to an unknown entity).

The various perspectives on trust, unclear definitions, and overlapping categorizations have challenged researchers in the area for many years (for further details on different approaches in the IS-field, see, e.g., [6, 8, 17, 20]).

One common denominator, in accordance with Gambetta’s definition and the previously mentioned perspectives on trust, has been a categorization of trust proposed by Abdul-Rahman et al. [1]. Following this lead, social scientists have identified three types of trust:

1. Interpersonal trust: The type of trust one agent has in another agent on a personal level. This trust is both agent- and context-specific. For example, Jane may trust Peter regarding a consulting service for financial assets, but may not trust him in the context of babysitting her children.

2. System trust: This type of trust is not based on any property or state of the trustee as defined in interpersonal trust. It is, rather, based on the perceived property or reliance on a system or institution within which trust exists—for example, the monetary system.

3. Dispositional trust: This type of trust describes the general attitude of the person seeking trustworthiness toward trust. Therefore, it is also called “basic trust,” which means it is independent of any other party or context.

These three types of trust differ in the way in which they can be established within a VC. According to McKnight et al. [32], dispositional trust is based on two presuppositions: First, one presumes that others are generally trustworthy—and, therefore, one should trust them. Second, one presumes that trusting others leads to better outcomes irrespective of whether these other people are good or not. According to this understanding, no component or factor can have a direct effect on dispositional trust.

In contrast, interpersonal trust and system trust can be attained through trust-supporting factors. Consequently, the following sections focus on the establishment of interpersonal and system trust in VCs.

## Trust and Trust-Supporting Factors in the Context of Online Applications

In order to maintain an online application, we need to find ways to enable trust systematically. Figure 1 demonstrates two major trust-supporting factors and their influence on the development of trust—perceived competence and perceived goodwill.

![](/api/attachments/KKANXWAC/fulltext/images/94b908c83242967b8d15ba66ef48273d8600ae73065986fc5d5ba84556b895e1.jpg)  
Figure 1. The Influence of Perceived Competence and Perceived Goodwill on Trust (adapted from [1, 11])

Perceived competence in the off-line environment is monitored by organizations that investigate and evaluate the reputation of other organizations; for example, rating agencies such as Standard & Poor’s or Moody’s. These organizations collect and analyze information about business partners and provide this information as a commercial service.

Within the context of online applications, many “trust partners” have been established. As independent organizations, these trust partners guarantee compliance with standards (i.e., secure payments and encrypted secured data transmission). In the online world, examples are “trusted shops” at online platforms such as epinions.com, or commercial solutions offered by companies such as Verisign Inc. Through continuous examination of, for example, the handling of privacy regulations, these institutions support the development of trust. They may also force business partners to adhere to standards in order to ensure that customers receive the goods or services they expect [41].

There are several factors that can influence perceived competence and perceived goodwill positively (see Figure 2). Perceived competence can be supported by clear definitions of the various responsibilities of the individuals providing goods or services. The disclosure of all prices, delivery times, taxes, or cancellation fees is meant to be an advantage for the buyer or consumer. Binding terms of use and codes of behavior are applied accordingly.

A further indicator to support perceived competence is the disclosure of patterns of past performance. Examples include airlines’ reports on on-time percentages for arrivals and departures or realtors’ statistics on the number of houses bought and sold. The disclosure of performance reports may attract users, as does information about the organization and its management. Even skeptical consumers may be engaged and assured by the transparency of performance numbers [41].

![](/api/attachments/KKANXWAC/fulltext/images/fcdbe9c86d98ffbb39db19568411a187324331b0b45b85cf3af19e9da44071e9.jpg)  
Figure 2. Trust-Supporting Components and Their Influence on Perceived Competence and Perceived Goodwill (adapted from [1, 11])

Perceived goodwill is more difficult to describe. It can be experienced as the discovery of a cooperating partner’s good intentions and can further lead to the development of interpersonal trust. Examples in the off-line world often refer to aspects such as common courtesy and complimentary behavior of market partners when, for example, a customer’s complaint is handled in favor of the client without legal necessity to do so.

In accordance with the existing literature on trust, the rationale of this work was to develop a set of components that affect both perceived competence and perceived competence in a positive manner. Hypothetically, the two constructs should, consequently, have a positive affect on trust.

## The Health-Care Sector: Characteristics of a Breast Cancer Community

Two key characteristics of a VC need to be considered in addition to the aforementioned general factors necessary for the development of trust. These are the target group and the topics discussed in the VC. In this case, the target group is breast cancer patients and the topic is cancer.

Breast cancer patients demand special requirements for the user interface and the composition of the platform.<sup>1</sup> Due to factors related to disease incidence, the topic (breast cancer) attracts a somewhat older female population. Thus, age and gender characteristics of the target group were taken into consideration in designing the VC.

As “cancer” is a personal experience that is still associated with negative social stigma, participation of the community members takes place on a particularly personal and intimate level. From the patients’ viewpoint, being diagnosed with cancer is the beginning of a period of extreme physical and psychological stress whose end cannot be predicted because of the lack of curative treatment and the possible occurrence of relapse.

In order to deal with this stress, patients and their relatives need comprehensive information at all stages of the disease trajectory. Because the diagnosis of cancer can be life threatening, the trustworthiness of the information given is of critical importance. Thus hospitals, medical professionals, and caregivers remain the most important source of information [21, 22, 33]. However, information and interaction are often ubiquitous desires for the patient and seldom coincide with the physicians’ work schedule. Patients experience other needs in addition to the simple retrieval of medical knowledge. The desire for social, peer-to-peer interaction, emotional support, and mobility are commonly expressed in self-help groups [12, 18, 31, 35, 42]. Interestingly, self-help groups only attract 3 percent of cancer patients according to Hasebrook [18]. Possible explanations for the low participation rate are that interested persons are unable to locate a group in their vicinity, or group meeting times do not fit individual patient’s schedules [26].

The results of focus groups consisting of individual cancer patients and members of cancer self-help groups held during the COSMOS (Community Online Services and Mobile Solutions) project indicated that a large number of potential community members expressed interest in using the Internet, but are skeptical about issues relating to the protection of privacy. In particular, the fear of abuse of personal data for advertising purposes deterred persons from using online services [11].

In the absence of trust, it is unlikely that patients will exchange intimate feelings, personal concerns, or taboo topics. Trust also plays an important role for the development of empathy (in the sense of feeling what another person feels and responding compassionately to it [27]), although the interaction between trust and empathy in the online world has hardly been researched [13].

Health-related VCs, in general, and VCs that deal with life-threatening diseases, in particular, are high-involvement VCs. Usage patterns found in these VCs are different than in other VCs, especially in lower-involvement VCs such as communities of practice in companies or communities centered around hobbies. VCs for patients tend to have higher levels of interaction [36, 37] and empathy [39].

In summary, members of patient communities, in general, cancer communities, in particular (especially in Germany), seem to have a higher demand for trust compared with members of “normal” communities. The following design of functionalities accommodates these requirements for the case of the VC krebsgemeinschaft.de as an example of a high-involvement community in the health-care domain.

## Design of Trust-Supporting Components

THE THEORETICAL BACKGROUND ON TRUST and the influence of perceived goodwill and perceived competence on trust can help in deriving design measures for supporting trust in VCs. The test of these theoretically motivated design components can then be used as an exploratory test for the underlying theoretical constructs applied in the domain of high-involvement VCs. The components discussed in this section represent concrete possibilities to support the process of building trust. According to the different types of trust explained above, this concept differentiates between components required to support system trust and those that support interpersonal trust by affecting positively the perceived competence and perceived goodwill of the actors within a VC of cancer patients.

## Perceived Competence

Essential design components for supporting perceived competence in a VC are transparency, high-quality content, the operator’s model, and access rights. According to the previous outlines of the literature on trust, these components should be designed in a way that maximizes their positive influence on perceived competence. Each of these components will be addressed in light of this objective.

## Criteria of Transparency

The adherence to standards established by external regulatory agencies or influential institutions is necessary in order to increase perceived competence in the VC. One such agency is the Health Information System Action Forum (afgis), established in 1999. The aim of this nonprofit forum is to develop a sustainable quality assurance process for German-language health information on the Internet. To attain this goal, the task force “Quality Assurance” drafted the following ten criteria of transparency [34]:

1. transparency of providers (name and address of the provider is clearly visible at the site);

2. transparency of goal, purpose, and target groups of information (the targeted audience is clearly defined);

3. transparency of authors and data sources (names, functions of authors, and sources of data are identified);

4. transparency of actuality of information (dating of information is indicated);

5. transparency of feedback mechanisms (opportunity of providing feedback, for example, via e-mail, to the providers of information);

6. transparency of quality assurance procedures (statements relating to the quality of information are published);

7. transparency of separation of advertising and editorial contents (product advertisements are clearly separated from factual content);

8. transparency of financing and sponsoring (financial support from companies and organizations is clearly identified);

9. transparency of cooperation and networks (any and all associations with companies or governmental/political organizations are indicated);

10. transparency of use and protection of data (indication of whether and how user information may be collected or used is clearly stated).

The afgis subgroup “Quality Assurance” is presently transforming these criteria into extensive and detailed guidelines. Operators must submit an application and meet minimum standard requirements in order to display the afgis trust seal on their Web site.

## Quality Assured Content

The quality of the content published on a VC is an important factor in establishing perceived competence. In the case of krebsgemeinschaft.de, the content is provided by the reputable German cancer information service (Krebsinformationsdienst [KID]), which is associated with the German Cancer Research Center in Heidelberg. KID plays the role of content manager for the VC. This institution has a long track record in supporting cancer patients via telephone hotlines and e-mail services. Through KID’s association with the German Cancer Research Center, the latest research results are available and integrated into the Web site in a timely fashion. Each text module of the Web site is proofread by a recognized expert in the field of oncology for correctness and relevance.

## The Operators of Krebsgemeinschaft.de

The motivation and background of operators of a VC play a central role in regard to perceived competence. For example, sites of pharmaceutical companies producing chemotherapeutic agents seldom publish information related to competing treatment options or alternative treatments. Information on alternative treatments would be better answered by an independent operator with no known ties to commercial entities. For this reason, the accurate disclosure of information regarding the site operators is important in the establishment of trust within a VC.

## The Access Rights Concept

Access rights refer to the determination of accessibility to various functions within the VC and are assigned according to the status of the individual member.

As stated above, interaction not only offers patients information but also serves as a source of support. In order to enhance the supportive aspects of the VC, we designed and implemented the “exchange services” Discussion Board, Ask an Expert, Contact Search, and Chat.

The discussion board supports the asynchronous exchange of information between the members of the community. Ask an Expert represents a special form of the discussion board. This service offers members the opportunity to address questions to an expert (physicians with specialized knowledge) during a limited time range. Only the designated expert answers questions. The Contact Search component serves the community members by connecting them with others who are in a similar situation in life, or have similar interests. The exchange service Chat offers community members the opportunity to communicate synchronously with each other, independent of location.

The access right concept assigns permission to use the exchange services to the members of the VC. The concept follows the five social roles that were originally identified by Kim [23] from her studies of the development of VCs. Kim distinguishes between visitors, novices, regulars, leaders, and elders [23]. Following Kim’s social roles, three levels of authorization are assigned at krebsgemeinschaft.de. Visitors who are simply lurking at the site own the authorization level “guest.” On registering with krebsgemeinschaft.de, they are promoted to the level “member.” During the course of membership, a member can receive the authorization level “VIP member.”

Table 1. Authorization Levels of Krebsgemeinschaft.de [11]

<table><tr><td>Level</td><td>Authorization title</td><td>Description of authorization assignment</td></tr><tr><td>1</td><td>Guest</td><td>Unregistered user of the Web site.</td></tr><tr><td>2</td><td>Member</td><td>Registered user.</td></tr><tr><td>3</td><td>VIP member</td><td>Registered user with special authorities—upgraded by the Community manager (permanently); upgraded by another VIP Member within the Chat (temporary).</td></tr><tr><td>4</td><td>Expert</td><td>Professional expert—appointed by Community manager; special authorization for “Topic of the week,” otherwise authority level Member.</td></tr><tr><td>5</td><td>Community manager</td><td>Supervision of the community (e.g., answering members’ inquiries and recruiting experts)—appointed by the project team.</td></tr><tr><td>6</td><td>Content manager</td><td>Responsible for procuring and maintaining content appointed by the project team.</td></tr><tr><td>7</td><td>Administrator</td><td>Technical administration of the platform—appointed by the project team.</td></tr></table>

Moreover, within krebsgemeinschaft.de, the authorization level “expert” and several administrator authorizations have been appointed. These other types of authorizations needed to be established due to specific characteristics of the domain and specificities related to project organization. The authorization level “community manager” is occupied by a physician from the “Onkologischer Schwerpunkt Stuttgart,” a network of several hospitals that provide specialized cancer treatment in Stuttgart (Germany). This community manager is responsible for the medical care within the community. The “Krebsinformationsdienst (KID)” provides cancer-related content and is thus assigned the role of “content manager.”

In total, there are seven authorization levels within krebsgemeinschaft.de (see Table 1). By dint of these levels of authorization, the rights for individual functionality are assigned. The most important states of the concept of authorization are summarized as follows:

• Unregistered users of the platform (guests) may browse the summary pages of both the Discussion Board and Ask an Expert; however, they are denied access to the content of the contributions to these sections and are themselves unable to contribute. Guests do not have access to the services Contact Search and Chat.

• The functionality “Change Contribution/Question” is restricted to the person making the contribution or posing the question. A question may be changed only as long as the expert has not yet answered it. These two restrictions apply to members and VIP members.

• It is possible for experts and administrators (authority level 5–7) to change or delete the contributions of community members in order to adhere to Discussion Board rules.

Further development of the Chat will allow each member to become a temporary VIP member. This occurs when a member opens up a new room with a new topic within the Chat. The member now has the rights of a VIP member, but this applies only to his or her own room and applies only for the duration of his or her stay in the room. Members seeking more privacy can establish a “private” room.

## Perceived Goodwill

Perceived goodwill can refer either to the operators of the VC or to other members of the community. In order to signal to the members of krebsgemeinschaft.de the greatest possible goodwill of the operators, the motivation of the institutional partners is clearly stated on the Web site, and it is noted that no commercial interests guide the community. The perceived goodwill of the users among themselves is supported by the possibility for members to forego anonymity by displaying data contained in the user profile (see Table 2). Through this step, members demonstrate their goodwill by revealing personal data to other members within the community.

## User Profile

The user profile contains compulsory and optional information that a member provides upon registration. If a member of the community publishes a contribution or asks a question, the contributor’s name is shown as a hyperlink. By clicking on this hyperlink, one obtains the user profile of the corresponding member. The extent of information other members see on the user profile depends on the level of anonymity the member has chosen. Furthermore, the information contained in the user profile serves as a data base for the service “Contact Search.” Table 3 describes the optional fields of the user profile.

## Concept of Anonymity

Each member of the community decides which kind and how much personal data is revealed to other members. Guests are unable to obtain any data. Each person deals individually with his or her illness, and it is the right of members to decide on the level of anonymity desired within the VC. Members can choose between four different levels of anonymity. Table 3 provides a description of each of the four possible anonymity levels.

The anonymity level “anonymous—show friends all” offers a unique differentiation to the members of the VC. If a member has established friendship through chatting or participation in the Discussion Board, he or she can add this person to the personal list of friends. Members included on the list of friends are able to view all data entered; members not noted on the list receive the anonymous form of a user’s profile.

Table 2. Anonymity Levels and Their Effects on the Representation of the User Profile [11]

<table><tr><td>Level of anonymity</td><td>Effects on the representation of the user profile</td></tr><tr><td>Display nothing</td><td>Indicated: “User does not want to indicate his personal data!”</td></tr><tr><td>Anonymous</td><td>Indicated: user name, country, status of user, connection with the illness, data of diagnosis, type of cancer, phase of illness, type of therapy, hobbies, interests (other).</td></tr><tr><td>Anonymous—show friends all</td><td>Indicated to members: user name, country, status of user, connection with the illness, data of diagnosis, type of cancer, phase of illness, type of therapy, hobbies, interests (other) → all entered data is indicated to friends.</td></tr><tr><td>Show everything</td><td>Indicated: all entered data.</td></tr></table>

## Implementation Examples of Additional Components of Krebsgemeinschaft.de

THIS SECTION PROVIDES AN OVERVIEW of the components that have been implemented in krebsgemeinschaft.de. First, we describe the components implemented to support perceived competence. Second, the components implemented to secure perceived goodwill are described.

## Implementation: Supporting Perceived Competence

As previously discussed, perceived competence is crucial to the success of a VC. In order to achieve and demonstrate perceived competence, the aforementioned afgis criteria of transparency were implemented in krebsgemeinschaft.de.

Transparency of providers is fulfilled by the imprint placed in the section “ueber uns” (“about us”). Furthermore, the logo of the VC is placed on every site as a visible label. The transparency of goal, purpose, and target groups is already evidenced by the URL www.krebsgemeinschaft.de (translated: “a cancer community”). In addition, a statement on the home page clarifies that the focus of the community is on survivors of breast cancer, relatives, and other interested persons. The link “gefuehrte tour” (guided tour) links to the site map. The content management system guarantees that all published information is up-to-date. With these instruments, the content manager (KID) ensures the “transparency” of authors and data sources as well as actuality of published content.

There are many options for feedback within the community. On one hand, users can comment on or criticize the layout and content of the Web site by clicking on the link “anregungen und kritik” (“comments and suggestions”). On the other hand, visitors can contact the community manager directly via e-mail in the section “kontakt” (“contact”). Finally, the section “über uns” (“about us”) presents additional routes to contact all involved project partners.

Table 3. Optional Data Contained in the User Profile [11]

<table><tr><td>Reference</td><td>Field name</td><td>Remarks/format</td></tr><tr><td colspan="3">Personal information</td></tr><tr><td>/D15/</td><td>Title</td><td>Format: text field</td></tr><tr><td>/D130/</td><td>Birthday</td><td>Format: “DD.MM.YYYY”</td></tr><tr><td>/D140/</td><td>Family status</td><td>Values: “no reply,”* “single,”“married,”“divorced,”“separated,”“cohabit,” and “widowed”Format: list to select</td></tr><tr><td>/D190/</td><td>Private telephone</td><td>Format: text field</td></tr><tr><td>/D200/</td><td>Fax</td><td>Format: text field</td></tr><tr><td colspan="3">The illness</td></tr><tr><td>/D210/</td><td>Connection with the illness</td><td>Values: “survivor,”“relative,”“expert,”“other”Format: text field</td></tr><tr><td>/D220/</td><td>Connection (other)</td><td></td></tr><tr><td>/D230/</td><td>Date of diagnosis</td><td>Format: “DD.MM.YYYY”</td></tr><tr><td>/D240/</td><td>Type of cancer</td><td>Values: “breast cancer,” “leukemia,”“other,”“no reply”Format: list to select</td></tr><tr><td>/D250/</td><td>Type of cancer (other)</td><td>Format: text field</td></tr><tr><td>/D260/</td><td>Phase of illness</td><td>Values: “no reply,” “before therapy,”“in therapy,”“remission,” “no metastases,” “metastases”Format: list to select</td></tr><tr><td>/D270/</td><td>Type of therapy</td><td>Values: “radical surgery (removal of the breast),”“X-ray therapy,”“removal of lymph nodes,”“breast saving surgery,”“hormone therapy,”“breast reconstruction,”“chemotherapy,”Format: check box</td></tr><tr><td>/D280/</td><td>Type of therapy (other)</td><td>Format: text field</td></tr><tr><td colspan="3">Personal interests</td></tr><tr><td>/D290/</td><td>Leisure activities</td><td>Values: “music,” “opera/theater/musical,”“dancing,” “walking,” “cinema”Format: check box</td></tr><tr><td>/D300/</td><td>Interests (other)</td><td>Format: text field</td></tr><tr><td colspan="3">Notes: For referencing the long-term stored data, Balzert [4] suggests the format as follows:/D10/, and so on. * The preselected value (standard) is in italics.</td></tr></table>

The transparency of quality assurance procedures is more complex. By the itembased editing of the content, information concerning date, item category, and author can be collected, saved, and presented. Thus, the users know which person is responsible for the content. In addition, the information (which is quality assured as indicated above) is clearly separated from other (user-generated) content by the navigation and further comments. Especially in the discussion board, the user is informed that he or she is responsible for his or her own contributions, and that the operators do not accept liability for any user postings on the board.

The demand of afgis for transparent separation of advertising and editorial content does not apply to this community, as it is not financially supported by advertisement.

Thus, transparency of financing and sponsoring as an issue is eliminated. The home page provides information about the research project operating this VC (COSMOS), the project partners, and the source of funding (the German Ministry of Research and Education). The section “über uns” (about us) clearly lists all cooperation partners with contact information.

During the registration process, all users are required to read the terms of use and the data security declaration; this satisfies the requirement for addressing the issues of transparency of use and protection of data.

## Implementation: Supporting Perceived Goodwill

The user profile and the concept of anonymity have been implemented to only a certain extent. Some of the designed optional fields have not yet been included in the user profile. The current user profile, however, does offer community members the opportunity to get to know each other easily. Through user suggestions, a further functionality was integrated: as a member of krebsgemeinschaft.de, one can send an e-mail to other members by clicking on the link located at the bottom of the user profile (see Figure 2). This is a simple way to start direct and personal communication.

It should be kept in mind that an extensive registration and verification process is mandatory for all potential users of the VC. As part of the registration process, users reveal personal data, but these data are only used for community management purposes. The anonymity concept allows users to decide on the desired degree of privacy; as much or as little information as desired can be displayed without revealing sensitive personal data such as real names, addresses, and so on. Figure 3 illustrates the user profile with the indicated anonymity levels “show everything,” “anonymous,” and “display nothing.”

The anonymity concept provides users with a personally flexible and easy way of sharing private information with the community. In this manner, each member improves and contributes to perceived goodwill (and also to the perceived competence) by displaying sensitive data such as type of disease, type of treatment, interests, and so on. Moreover, members are aware that in the case of bad conduct, the community management has access to full member information and it can take appropriate actions to maintain a healthy community life.

## Evaluation of the Implemented Trust-Supporting Components

EVALUATION, ACCORDING TO BORTZ AND DOERING [7], deals with the verification of the efficacy of an intervention (e.g., a therapy, an action, etc.) by means of empirical research. Summative evaluation focuses on the outcome or the final results of an action, whereas formative evaluation focuses on the continuous development of the intervention. Within a formative evaluation, the interventions are tracked continuously and the results are used as a basis for appropriate further actions (if necessary) in order to achieve the overall objective of the intervention [7]. Thus, the formative evaluation serves to track and improve interventions. In the case of krebsgemeinschaft.de, formative evaluation is applied in order to verify the utility, use, and benefits of the developed trust-supporting components for a VC for cancer patients.

![](/api/attachments/KKANXWAC/fulltext/images/b103ca389fa9f49a1757f441bd8729686e89d6469cce1a20ae4032c248a6518e.jpg)  
Figure 3. User Profile in Different Anonymity Levels [25]

## Methodological Aspects

Deriving statements on the efficiency of the different actions aimed at supporting the development of trust within the community krebsgemeinschaft.de requires defined reference measures for the success of each single action and of all actions combined (in this case, measures for the success of the entire VC). However, in field research, it is difficult to define success measures or respective cause-effect-chains for single actions/interventions, as these affect the user both independently and in combination with other actions, therefore their effect cannot be regarded in isolation. Often, it is only possible to measure and evaluate the sum of several actions and influences as a whole. One can assume that the successful conception and implementation of trustsupporting components will lead to a successful VC (for the evaluation and success measurement of VCs, also see [2, 9, 39]). For the proposed formative evaluation, we used self-reporting data sources (online surveys) and archive analyses, log file analyses, and observations.

Choosing an online survey as a method to collect data poses some important consequences for the process of the investigation and for the design of the questionnaire (for further details, see [5, 14]). Some basic problems occur when conducting an online survey. The sample is self-selective and therefore cannot be regarded as being representative, and statements about “nonparticipants” cannot be made [19]. The questionnaire used in this study was structured, tested, and, consequently, adapted to the needs of the specific targeted audiences. For this purpose, a pretest followed by a discussion with the test persons was conducted. In addition, an online pretest was carried out that tested the content and the functionality of the questionnaire. The instrument intends to measure the effect of the design measures on perceived competence and perceived goodwill, but also addresses the level of trust directly.

## Survey Results

Since trust-related issues can (to some extent) be articulated by the members of the VC, conducting an online survey is potentially fruitful for evaluating the effect of the trust-supporting components. Structure and content of the user survey followed the concept of trust and trust-supporting factors as introduced in the first section (see Figure 1).

To prove the concept and validate the effects of the trust-supporting components, the following research questions guided the online survey:

1. Do the members of krebsgemeinschaft.de assign a positive perceived competence and a positive perceived goodwill to the operators?

2. Do the members of krebsgemeinschaft.de trust the operators of the community and their provided content?

3. Do the members of krebsgemeinschaft.de assign a positive perceived competence and a positive perceived goodwill to the other members?

4. Do the members of krebsgemeinschaft.de trust the other members and the user-generated content?

The survey is provided in the Appendix. In order to measure the degree of trust toward other members and operators, several questions were posed that measured perceived benevolence and the perceived competence of members and operators as well as the respective trust.

Moreover, the users were asked if the members of krebsgemeinschaft.de were disposed to deliver personal information within the community and if they would accept advice provided by other members or the operators. According to the findings of Ridings et al. [40] that a strong relationship exists between “trust” and “desire to give” and “desire to get information,” these behavior patterns were used as indicators for the existence or nonexistence of trust. They show whether the members of krebsgemeinschaft.de are disposed to exchange their own data and information within the VC and whether they are willing to accept the information provided. By integrating Ridings et al.’s [40] measures and findings, the overall existence of trust in the VC was addressed. By comparing the effects on perceived goodwill/competence and on trust in general, the link between trust-supporting components and trust was addressed.

Table 4. Duration of Membership in Krebsgemeinschaft.de (n = 32)

<table><tr><td>Duration</td><td>Frequency</td><td>Percentage</td></tr><tr><td>&lt; 1 month</td><td>8</td><td>25.0</td></tr><tr><td>1–3 months</td><td>4</td><td>12.5</td></tr><tr><td>4–6 months</td><td>4</td><td>12.5</td></tr><tr><td>&gt; 6 months</td><td>16</td><td>50.0</td></tr></table>

Table 5. Frequency of Usage of Krebsgemeinschaft.de (n = 32)

<table><tr><td>Frequency of usage</td><td>Frequency</td><td>Percentage</td></tr><tr><td>Daily</td><td>5</td><td>15.6</td></tr><tr><td>Several times per week</td><td>15</td><td>46.9</td></tr><tr><td>Once per week</td><td>5</td><td>16.5</td></tr><tr><td>Less</td><td>7</td><td>21.9</td></tr></table>

## General Information About the Respondents

Duration of membership data on the study sample is indicated in Table 4. Twenty-five percent of the respondents had been registered for less than one month and 50 percent of the respondents had been registered for more than six months at the time of the initiation of the study.

The frequency of usage of members is displayed in Table 5. It is notable that 25 of 32 respondents visit krebsgemeinschaft.de at least once per week.

## Trust in the Operators of the VC Krebsgemeinschaft.de

None of the questions intended to measure the competence or the perceived benevolence of the team was answered negatively (no question was answered with “I do not agree at all” (5) or “I do not agree” (4)). The mean value of all answers was between “I totally agree” (1) and “I agree” (2). This result assigns a high level of trustworthiness to the provider. The question directly linked to the trustworthiness of the provider was also answered positively (average of 1.63). This confirms other results concerning “perceived benevolence” and “perceived competence.” The users acknowledged that both the provider and the team of supervising physicians possessed the necessary experience and knowledge to competently manage krebsgemeinschaft.de. Also, the reverse-coded control question, “From time to time I do have the impression that the team is not capable of answering my cancer-related questions well,” did not change the picture and underscored the competence of the managing team (see Figure 4).

![](/api/attachments/KKANXWAC/fulltext/images/1a8a1dbbfb071bf3f6c19b9b225b5e34690019af71bb0a40ca52440ab01c93e1.jpg)  
Figure 4. Perceived Competence of the Team/the Operator. Note: n = 32.

The interviewed members of krebsgemeinschaft.de expressed the opinion that the team operating the VC is highly motivated to act in the members’ interest and tries to support them. Furthermore, they were in agreement that the team would not misuse the granted trust (in terms of information committed to their care). All in all, the members of krebsgemeinschaft.de were of the opinion that the team is benevolent (see Figure 5).

As a result, one can assume that the members’ trust in the managing team and the provided information was relatively high.

## Trust in the Other Members of the VC Krebsgemeinschaft.de

No question concerning perceived benevolence and competence of the other members of krebsgemeinschaft.de was answered with “disagree strongly.” One member answered three questions with “I do not agree.” The median of all questions was between “I totally agree” and “partly.” This indicated a high trustworthiness of the other members within the community. The direct question concerning other members’ trustworthiness was answered with “I agree” (median of 2.27). This reconfirms the findings above.

![](/api/attachments/KKANXWAC/fulltext/images/651b708b014ba02ac22315bc0e992696bd825381658314ef88bdcf4a41368985.jpg)  
Figure 5. Perceived Goodwill/Benevolence of the Team/the Operator. Note: n = 32.

Perceived Competence of the Other Members. The sharing of experiences by other members was rated as useful (median of 1.96), but already the knowledge and competence of the users is not fully adjudged (median of 2.44 for “The other members of krebsgemeinschaft.de are familiar with the topics they discuss”; median of 2.36 for “The other members always know what I am speaking of”; see Figure 6). Members were more critical in their answers concerning the question relating to following the advice of other members (median of 2.72).

The interviewed persons seemed not to have faith in the competence of other members—at least not enough to follow the advice of fellow members. The reverse-coded question “Not all information provided by the other members is always correct” was averagely answered with “partly” (median of 2.93). This demonstrated that there is at least some doubt concerning the correctness of member-supplied information. Overall, the perceived competence of the other members seems to be relatively good, but limited, leading to a lower amount of confidence in other members. However, the correlation between the relatively negatively perceived competence of other members compared to the perceived competence of experts does not necessarily reflect the failure of trust-supporting components for other members. It may be due to a “real” lack of competence of the other members. Nevertheless, it is conceivable that expert knowledge is not a prerequisite for being a member within a VC for cancer patients.

Expert knowledge can in fact be provided by the operator of the VC, whereas the members contribute to the usefulness of the VC through their relaying of experiences and their personal characteristics such as cooperativeness, openness, and responsiveness. One indicator supporting this idea is the fact that other members were considered as trustworthy despite a lack of confidence in their competence.

![](/api/attachments/KKANXWAC/fulltext/images/5cdb26c20c63993aaa6e755c967a071b17b8bba00c2a9dde5a64c8f894bdb455.jpg)  
Figure 6. Perceived Competence of the Other Members of the VC Krebsgemeinschaft.de. Note: n = 32.

Perceived Goodwill/Benevolence of the Other Members. In contrast to the limited perceived competence, the benevolence of the other users was graded high (Figure 7). The median of the questions, with which this trait was measured, lies between 1.63 (“It is important for the members to support each other”) and 2.24 (“The members of krebsgemeinschaft.de would never consciously give me wrong information”). As a result, the members’ benevolence was graded very high and the dealings between each other can be specified as empathetic. No question related to the perceived benevolence was answered with “I disagree strongly” or “I do not agree.”

This pattern of response is a further hint for the irrelevance of perceived competence for credibility and trustworthiness with respect to other members. The other members are perceived as benevolent, a fact that might be more important for the members than the professional knowledge and expertise of their communication partners. Empathy and trustworthiness do not correlate with perceived competence of the communication partner. Considering the reason for meeting in the community, everyone shares a similar problem, being affected either directly or through a related person by a life-threatening disease. It becomes obvious that the quality-assured and centrally provided content on the platform allows members to focus on empathic support and additional information exchange on issues not covered in the centrally provided content section of the platform. This might explain why the members assigned a high level of benevolence, and at the same time, a lower level of competence to the other members.

## Reported Usage and Online Behavior

In addition to the self-reported statements on perceived benevolence and perceived goodwill of members and the operator, it is important to evaluate whether the users’ actions correspond to their stated levels of trust. According to Ridings et al. [40], there is a strong correlation between trust and the desire to give information (information giving) and to use it (information taking) in VCs. Therefore, one can assume that giving personal information and using personal information from other members are indicators for the presence or absence of trust within the VC.

![](/api/attachments/KKANXWAC/fulltext/images/ab85758dd4ae81a6b321477216a5d59b2f1a5138fec93a71bd391b2499aa77de.jpg)  
Figure 7. Perceived Goodwill/Benevolence of the Other Members. Note: n = 32.

Information Taking. The information collection on the topic breast cancer and on how to cope with the disease (centrally provided by the operators of krebsgemeinschaft.de) as well as the use of experience reports of other members were reported to be important reasons for visiting the community. This indicates that the members have confidence both in the quality-assured information provided by the operators as well as in the member-generated content, as long as it related to empathic issues or experiences of members.

Information Giving. Results of the questions on “exchanging information” indicated members’ confidence in the other members and the provider. They visit krebsgemeinschaft.de with the intention of sharing their knowledge (median of 2.0) and experience (1.93) with others. Since members deal with a life-threatening disease and very intimate and private issues, it seems obvious that a specific amount of confidence in communication partners is necessary for people to share their experiences within this context.

In total, the answers given by the queried members of krebsgemeinschaft.de indicated that the members have confidence in each other and in the operator of the community. They visit the community in order to become active, and to search for thematic and personal information. The members act according to their self-reported trust in operator and peers. They use the centrally provided information and are willing to reveal and exchange personal information and experiences within the VC. All in all, this reveals the members’ trust in krebsgemeinschaft.de in general. Not only do they express confidence in the competence of the operator and the members, but they also act accordingly.

![](/api/attachments/KKANXWAC/fulltext/images/38de688c925b39db793819875fbe352d414499a7819463474923fe6f52a7d66d.jpg)  
Figure 8. Thread in the Discussion Forum [25]

## Document Analysis and Observations

The artifacts in the community give a rich and deep understanding of the life in the VC krebsgemeinschaft.de and the level of trust that members have in the community and each other. With the poem “Sign in the Heart . . . ,” an active community member described her feelings for the VC. Inspired by the original text of a popular German poem, she versified a corresponding variation about krebsgemeinschaft.de. Given such an impetus in form of her poem about the importance and meaning of the community, the members started a vital discussion on the specific use of the Internet, in general, and of krebsgemeinschaft.de, in particular, for persons in their situation. This discussion reflects how fast the members reach the private level and reveal details on their individual situation to delineate in which position they are. It can be assumed that VCs such as krebsgemeinschaft.de, which leave it to the users to choose their preferred degree of anonymity, lower the barrier to openly discuss taboo subjects (see Figure 8).

This might be interpreted as evidence for the hypothesis that VCs enable people to talk frankly on topics that are too difficult to be discussed in real life.

Figure 9 shows how two members of krebsgemeinschaft.de try to bolster up a young woman who is suspected to have breast cancer. They offer her being interlocutors in this difficult moment and appeal to her to keep up. Both emphasize that she is not alone and can rely on the support and advice of the community members. It is one of many empathetic discussions within the VC and a good example for the support the members can receive by the community.

![](/api/attachments/KKANXWAC/fulltext/images/19d62f0005b682443d8cadca287a697766e2cf679491784f93fbcf9b1c7f9b54.jpg)  
Figure 9. Thread in the Discussion Forum [25]

The entry in Figure 10 was posted at the end of a discussion about the subject “depression” and shows that enough interpersonal trust has been established to openly discuss taboo subjects.

## Summary and Implications

Krebsgemeinschaft.de is a type of support community, as it provides not only factual information but also emotional support for its members. Observations and archive analyses indicate that members candidly and empathically interact with one another, especially via the Discussion Board and Chat. The log file analyses and the user numbers (by July 2004, krebsgemeinschaft.de had more than 1,000 registered users) underline the success of the project. The results of the surveys intended to measure trust prevailing within the community seem to certify the success of the trust-building components. The design measures seem to have had a positive effect on perceived competence and perceived goodwill of the operators. Similar results were found concerning perceived goodwill of the other members, but slightly lower levels were reported for the perceived competence of other members. Moreover, the data revealed that the respondents declare relatively high levels of trust toward operators and relatively lower levels (but from an absolute perspective, still high levels) of trust toward other members of the VC. These data support the underlying theoretical constructs by showing that the elements of the design measures had an effect on perceived competence and perceived goodwill. Moreover, one can derive from the differences of reported trust and perceived competence (especially of other members) that the cause-and-effect relationship between perceived competence, perceived goodwill, and trust as presented in the literature was supported.

![](/api/attachments/KKANXWAC/fulltext/images/659c005f78f7edc3385795a9e40966e118703822299ae96c411ca69e01fb0182.jpg)  
Figure 10. Thread in the Discussion Board [11]

Artifacts of usage as well as the results of extensive observations comply with this result: Members are willing to use information provided by other members and disclose personal experiences within the community. Therewith, they demonstrate their trust that this information will not be misused and that information and data provided by other members is trustworthy and correct. As verification of this, respondents indicated that they based real-life actions on information gathered in the community.

The archive analyses give a clear impression of the motivation for using krebsgemeinschaft.de, of the personal benefit for the users, and of the role trust plays in the VC.

These results must be seen in light of the study’s limitations. The findings of this indepth case study need further empirical substantiation, especially in respect to other high-involvement VCs or to other domains for VCs outside the health-care realm. The study sample consisted only of members of krebsgemeinschaft.de; those who visited the site but decided not to become members were lost to possible inclusion in the study. The inclusion of nonmembers could have provided valuable data for testing the effect of the design measures and the underlying concepts: Was it an issue of trust that made them decide not to become members? In reality, it would have been difficult to gain access to anyone who visited the site but did not join. Interestingly, the log file analyses of krebgemeinschaft.de show a low rate of onetime visitors, regardless of which criteria proposed for VCs in the literature [9] is applied.

## Future Outlook and Research Recommendations

THE IMPLEMENTED COMPONENTS ARE only a first step toward understanding trust support in the context of online communities. Trust is a multidimensional construct;

a complete in-depth analysis was not possible within the confines of this project. The researchers are of the opinion that the full potential of technical or organizational support of trust has not yet been exploited.

In extension of the model introduced in Figures 1 and 2, future steps should focus on factors influencing perceived goodwill and perceived competence. One possibility for achieving this can be the use of reputation indicators that assist with this process. In the following, three possibilities are presented that promote the communication and visualization of reputation [24]:

1. Mutual appraisal of transaction partners: Many online auction platforms have created the possibility for involved partners to mutually evaluate themselves after a transaction. Often, this appraisal is a combination of a standardized rating (e.g., based on a scale of one to five stars) and a field for open comments. The problem with this type of evaluation is that users may remain anonymous and, thus, the power of expression of the individual evaluation is rather minimal. The persuasiveness of the whole evaluation is dependent on the number of evaluations from different users. Therefore, the greater the number of positive evaluations from transaction partners, the more likely other users will trust the value of this positive feedback [15].

2. Appraisal of opinions: The usual practice of online auction platforms is that no direct appraisals of transaction partners takes place; rather, it is only the recommendations and/or information that are evaluated (e.g., as realized at www.ciao.com with “very helpful,” “helpful,” “little helpful,” and “useless”). The average of the appraisals can be calculated and represented visually.

3. Relationship networks: The idea behind this concept is to find a reputable person who provides information as to the trustworthiness of a potential cooperation partner. To accomplish this, data about the relationship between the cooperating partners must be collected prior to the transaction. The developed relationship networks can then be visualized.

Appraisals of opinions and relationship networks usually use experts to guarantee the correctness of the data provided. Furthermore, the expert has to have access to the data about the relationship between the cooperation partners. Therefore, these solutions are rarely implemented. In contrast, mutual appraisal of transaction partners is used often, because it provides reputation based on transactions at minimal costs.

In order to support the perception of competence and goodwill of transaction partners, reputation indicators are helpful [38]; see also Figure 11. They compensate for a certain lack of primary information and refer to personal experiences as well as experiences of others. Therefore, reputation is defined as “an expectation about an agent’s behavior based on information about or observations of its past behavior” [1, p. 6009].

Future research should focus on possibilities of appropriate reputation mechanisms. Rating mechanisms for user-generated content, users, and operators are promising starting points for supporting perceived competence and perceived goodwill in VCs in general, and in VCs for patients in particular. Rating information in the context of krebsgemeinschaft.de means that single information items can be rated by each registered user. Thus, the centrally provided and quality-assured content could be evaluated by the users in the context of usefulness and comprehensibility. Positive feedback strengthens trust concerning the quality of the content. User-generated content, such as postings in the discussion board or contributions from onetime users, could eventually be rated to support perceived competence and perceived goodwill; these events could further encourage trust among members of the community.

![](/api/attachments/KKANXWAC/fulltext/images/fd30dde4c328956ec2b7add6c596e2f4e4f2afde2140d84a4960bb3e74f9a973.jpg)  
Figure 11. Reputation Factors Influencing Trust-Supporting Factors (adapted from [11, 24])

In addition to technical components geared toward supporting perceived competence and benevolence, the community management plays an important role for the creation and maintenance of trust. Moderation should guide the community according to intersubjectively comprehensible rules to support trust within the VC. The structure and content of these rules for moderation and management, as well as questions such as “What has to be moderated, how and when?” have yet to be researched.

Acknowledgments: This paper presents outcomes of the research project “COSMOS (Community Online Services and Mobile Solutions).” COSMOS is a joint research project of the Technische Universität München and 02 Germany. The project is funded by the German Ministry of Research and Education under contract number FKZ 01 HW 0107–01 HW 0110. For further information, please visit www.cosmos-community.org. The main objective of the project is to examine the design, development, and maintenance of virtual communities.

## NOTE

1. The conception of a development model for health-care communities is done by Arnold et al. [3].

## REFERENCES

1. Abdul-Rahman, A., and Hailes, S. Supporting trust in virtual communities. In R.H. Sprague Jr. (ed.), Proceedings of the Thirty-Third Hawaii International Conference on System Sci-

ences. Los Alamitos: IEEE Computer Society Press, 2000 (available at www.cs.ucl.ac.uk/staff/ F.AbdulRahman/docs/hicss33.pdf).

2. Abras, C. Determining success in online education and health communities. Ph.D. dissertation, University of Maryland, Baltimore, 2003.

3. Arnold, Y.; Leimeister, J.M.; and Krcmar, H. COPEP: A development process model for a community platform for cancer patients. In C. Ciborra, R. Mercurio, M. De Marco, M. Martinez, and A. Carignani (eds.), Proceedings of Eleventh European Conference on Information Systems (ECIS). Atlanta: Association for Information Systems, 2003, pp. 1–11.

4. Balzert, H. Lehrbuch der Software-Technik [Textbook for Software Technology]. Berlin: Spektrum Akademischer Verlag, 2000.

5. Bantinic, B.; Moser, K.; and Puhle, B. Der WWW—Fragebogengenerator [WWW— questionaire generator]. In W. Bandilla, B. Bantinic, and L. Graef (eds.), Online Research— Methoden, Anwendungen und Ergebnisse [Online Research—Methods, Applications and Results]. Göttingen: Verlag für Psychologie Dr. C.J. Hogrefe, 1999, pp. 93–102.

6. Bhattacherjee, A. Individual trust in online firms: Scale development and initial test. Journal of Management Information Systems, 19, 1 (Summer 2002), 211–242.

7. Bortz, J., and Doering, N. Forschungsmethoden und Evaluation für Human- und Sozialwissenschaftler [Research Methods and Evaluation for Human and Social Scientists]. Berlin: Springer-Verlag, 2002.

8. Brown, H.G.; Poole, M.S.; and Rodgers, T.L. Interpersonal traits, complementarity, and trust in virtual collaboration. Journal of Management Information Systems, 20, 4 (Spring 2004), 115–137.

9. Cothrel, J. Measuring the success of an online community. Strategy & Leadership, 28, 2 (2000), 17–21.

10. Doney, P.M.; Cannon, J.P.; and Mullen, M.R. Understanding the influence of national culture on the development of trust. Academy of Management Review, 23, 3 (1998), 601–620.

11. Ebner, W.; Leimeister, J.M.; and Krcmar, H. Trust in virtual healthcare communities: Design and implementation of trust-enabling functionalities. In R.H. Sprague Jr. (eds.), Proceedings of the Thirty-Seventh Hawaii International Conference on System Sciences. Los Alamitos, CA: IEEE Computer Society Press, 2004 (available at csdl.computer.org/comp/proceedings/hicss/2004/2056/07/205670182a.pdf).

12. Engelhardt, H.D.; Simeth, A.; and Stark, W. Was Selbsthilfe leistet. Ökonomische Wirkungen und sozialpolitische Bewertung [The Performance of Self-Help: Economic Effects and Socio-Political Evaluation]. Freiburg i. Br.: Lambertus, 1995.

13. Feng, J.; Lazar, J.; and Preece, J. Interpersonal trust and empathy online: A fragile relationship. In G. Cockton and P. Korhonen (eds.), Proceedings of the 2003 Conference on Human Factors in Computing Systems. New York: ACM Press, 2003, pp. 718–719.

14. Gadeib, A. Ansprüche und Entwicklung eines Systems zur Befragung über das World Wide Web [Requirements for and Development of a System for Questionnaires in the World Wide Web]. In W. Bandilla, B. Bantinic, and L. Graef (eds.), Online Research—Methoden, Anwendungen und Ergebnisse [Online Research—Methods, Applications and Results]. Göttingen: Verlag für Psychologie Dr. C.J. Hogrefe, 1999, pp. 103–111.

15. Galla, M. Social relationship management in Internet-based communication and shared information spaces. Ph.D. dissertation, Technische Universität München, Munich, 2004.

16. Gambetta, D. Can we trust trust? In D. Gambetta (ed.), Trust: Making and Breaking Cooperative Relations. Oxford: Blackwell, 1990, pp. 213–238.

17. Gefen, D. What makes an ERP implementation relationship worthwhile: Linking trust mechanisms and ERP usefulness. Journal of Management Information Systems, 21, 1 (Summer 2004), 263–288.

18. Hasebrook, J. Krebs-Selbsthilfegruppen—Untersuchungen zu Bedarf, Funktionen, und Wirksamkeit [Cancer self-help groups: Investigations on demand, features, and efficiency]. In F.A. Muthny and H. Gunther (eds.), Onkologie im psychosozialen Kontext—Spektrum psychoonkologischer Forschung, zentrale Ergebnisse, und klinische Bedeutung [Oncology in Psychosocial Context: Spectrum of Psycho-Oncological Research, Central Results, and Clinical Relevance]. Heidelberg: Roland Asanger Verlag, 1993, pp. 260–275.

19. Hauptmanns, P. Grenzen und Chancen von quantitativen Befragungen mit Hilfe des Internet [Restrictions and prospects of quantitative inquiries using the Internet]. In W. Bandilla,

B. Bantinic, and L. Graef (eds.), Online Research—Methoden, Anwendungen und Ergebnisse [Online Research—Methods, Applications and Results]. Göttingen: Verlag für Psychologie Dr. C.J. Hogrefe, 1999, pp. 21–38.

20. Jarvenpaa, S.L.; Knoll, K.; and Leidner, D.E. Is anybody out there? Antecedents of trust in global virtual teams. Journal of Management Information Systems, 14, 4 (Spring 1998), 29–64.

21. Jenkins, V.; Fallowfield, L.; and Saul, L. Information needs of patients with cancer: Results from a large study in UK centers. British Journal of Cancer, 84, 1 (2001), 48–51.

22. Kaminski, E.; Thomas, R.J.; Charnley, S.; and Mackay, J. Measuring patients’ response to received information. European Journal of Cancer, 37, 6 (supplement 2001), 387.

23. Kim, A.J. Secret Strategies for Successful Online Communities/Community-Building On the Web. Berkeley: Peachpit Press, 1999.

24. Koch, M.; Möslein, K.; and Wagner, M. Vertrauen und Reputation in Online-Anwendungen und virtuellen Gemeinschaften [Trust and reputation in online applications and virtual communications]. In M. Engelien and D. Neumann (eds.), Virtuelle organisationen und neue medien 2000 [Virtual organizations and new media, 2000]. Cologne: Josef Eul Verlag, 2000, pp. 69–84.

25. Leimeister, J.M. Pilotierung virtueller Communities im Gesundheitsbereich— Bedarfsgerechte Entwicklung, Einfuehrung und Betrieb [Piloting virtual communities in the health care domain—User-centric development, implementation and operation]. Ph.D. dissertation, Universität Hohenheim, Stuttgart, 2004.

26. Leimeister, J.M.; Daum, M.; and Krcmar, H. Mobile virtual healthcare communities: An approach to community engineering for cancer patients. In S. Wrycza (ed.), Proceedings of the Tenth European Conference on Information Systems (ECIS). Gdansk: Wydawnictwo Uniwersytetu Gdan;skiego, 2002, pp. 1626–1637.

27. Levenson, R.W., and Ruef, A.W. Empathy: A psychological substrate. Journal of Personality and Social Psychology, 63, 2 (1992), 234–246.

28. Luhmann, N. Trust and Power. Chichester, UK: Wiley, 1979.

29. Luo, W., and Najdawi, M. Trust-building measures: A review of consumer health portals. Communications of the ACM, 47, 1 (2004), 109–113.

30. Mayer, R.C.; Davis, J.H.; and Schoormann, F.D. An integrative model of trust development and decline. Academy of Management Review, 20, 3 (1995), 709–734.

31. McIllmurray, M.B.; Thomas, C.; Francis, B.; Morris, S.; Soothill, K.; and Al-Hamad, A. The psychosocial needs of cancer patients: Findings from an observational study. European Journal of Cancer Care, 10, 4 (2001), 261–269.

32. McKnight, D.H.; Cummings, L.L.; and Chervany, N.L. Initial trust formation in new organizational relationships. Academy of Management Review, 23, 3 (1998), 513–530.

33. Mills, M.E., and Sullivan, K. The importance of information giving for patients newly diagnosed with cancer: A review of the literature. Journal of Clinical Nursing, 8, 6 (1999), 631–642.

34. Möller, A. Qualitätskriterien von Gesundheitsinformationen [Criteria for quality health information]. Frankfurt, 2004 (available at www.afgis.de/qualitaetssicherung.php?lang=e, last accessed November 11, 2004).

35. Möller, M.L. Selbsthilfegruppen: Selbstbehandlung und Selbsterkenntnis in eigenverantwortlichen Kleingruppen [Self-Help Groups: Self-Treatment and Self-Awareness in Self-Help Groups]. Reinbeck b. Hamburg: Rowohlt, 1978.

36. Nonnecke, B., and Preece, J. Lurker demographics: Counting the silent. In Proceedings of the CHI 2000 Conference on Human Factors in Computing Systems. The Hague: ACM Press, 2000, pp. 73–80.

37. Nonnecke, B., and Preece, J. Silent participants: Getting to know lurkers better. In C. Lueg and Fisher, D. (eds.), From Usenet to CoWebs: Interacting with Social Information Spaces. London: Springer, 2003, pp. 110–132.

38. Pennington, R.; Wilcox, H.D.; and Grover, V. The role of system trust in business-toconsumer transactions. Journal of Management Information Systems, 20, 3 (Winter 2003–4), 197–226.

39. Preece, J., and Maloney-Krichmar, D. Online communities: Focusing on sociability and usability. In J. Jacko and A. Sears (eds.), Handbook of Human–Computer Interaction. Mahwah, NJ: Lawrence Erlbaum, 2003, pp. 596–620.

40. Ridings, C.; Gefen, D.; and Arinze, B. Some antecedents and effects of trust in virtual communities. Journal of Strategic Information Systems, 11, 3–4 (2002), 271–295.

41. Shneiderman, B. Designing trust into online experiences. Communications of the ACM, 43, 12 (2000), 57–59.

42. Spiegel, D.; Bloom, J.R.; and Yalom, I. Group support for patients with metastatic cancer: A randomized outcome study. Archives of General Psychiatry, 38, 5 (1981), 527–533.

43. Wigand, R.; Picot, A.; and Reichwald, R. Information, Organization and Management: Expanding Corporate Boundaries. Chichester, UK: Wiley, 1998.

44. Williamson, O.E. Markets and Hierarchies: Analysis and Antitrust Implications. A Study in the Economics of Internal Organization. New York: Free Press, 1975.

<table><tr><td>E. Fragen an Experten stellen / Posting questions to the service “Ask the Expert”</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>F. Fragen an Experten lesen / Reading postings of the service “Ask the Expert”</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>G. Kontaktsuche / Service “Buddy finder”/partner matching</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>H. Visitenkarten anderer Mitglieder lesen / Reading the cards/ profiles of other members</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>I. Einträge in Gaestebücher erstellen / Making posting in guest books</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>J. Einträge in anderen Gaestebüchern lesen / Reading postings in others’ guest books</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>K. Einträge im eigenen Gästebuch lesen / Reading postings in my guest book</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td colspan="5"></td><td>(continues)</td></tr></table>

<sub>h</sub> <sub>extent</sub> <sub>do</sub> <sub>you</sub> <sub>agree</sub> <sub>with</sub> <sub>the</sub> f<sup>ollowing</sup> <sup>st</sup> <sub>eit</sub> <sub>stim</sub>m<sup>en</sup> <sup>Sie</sup> <sup>den</sup> <sup>unten</sup> <sup>genannten</sup> <sup>Aus</sup>

<table><tr><td></td><td>Stimme voll und ganz zu Agree strongly</td><td>Stimme zu Agree</td><td>Teils, teils Partly</td><td>Stimme nicht zu Disagree</td><td>Stimme überhaupt nicht zu Disagree strongly</td></tr><tr><td>A. Das Team, das krebsgemeinschaft.de betreut, ist in der Lage, die richtigen Informationen für uns auszuwählen. /The team supervising krebsgemeinschaft.de is capable of selecting the right information for our needs.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>B. Das Team von krebsgemeinschaft.de ist vertrauenswürdig /The team of krebsgemeinschaft.de is trustworthy</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>C. Das Team würde die ihm anvertrauten Daten niemals missbrauchen. / The team would never misuse the entrusted data.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>D. Das Team hat ausreichende Erfahrungen, umkrebsgemeinschaft.de kompetent zu leiten. / The team has enough experience to operate krebsgemeinschaft.de.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></table>

<table><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr></table>

<sub>estions</sub> w<sup>e</sup> <sub>am</sub> <sub>is</sub> <sub>not</sub> <sub>capable</sub> <sub>of</sub> <sub>ans</sub>w<sup>ering</sup> <sup>my</sup> <sup>canc</sup> <sub>orten.</sub> <sub>/</sub> <sub>From</sub> t<sup>ime</sup> <sup>to</sup> <sup>time</sup> <sup>I</sup> <sup>do</sup> <sup>have</sup> <sup>the</sup> <sup>i</sup> <sub>t,</sub> <sub>meine</sub> <sub>Fragen</sub> <sub>zum</sub> <sub>T</sub><sup>hema</sup> <sup>Krebs</sup> <sup>zufried</sup> <sub>malhabeichdasG</sub>e<sup>fühl,dassdasTeamni</sup> <sub>ast</sub> <sub>as</sub> <sub>possible</sub> <sub>to</sub> <sub>the</sub> <sub>needs</sub> <sub>of</sub> <sub>the</sub> m

<sub>achlich</sub> <sub>fühle</sub> <sub>ich</sub> <sub>mich</sub> <sub>in</sub> <sub>der</sub> K<sup>rebsgemein</sup> <sub>inschaft.de.</sub> <sub>/</sub> <sub>The</sub> <sub>tea</sub>m <sup>acts</sup> <sup>on</sup> <sup>behalf</sup> <sup>of</sup> <sup>the</sup>

<sub>a</sub> <sub>Krebs</sub> <sub>bereit</sub> <sub>zu</sub> <sub>s</sub>t<sup>ellen.</sup> <sup>/</sup> <sup>The</sup> <sup>team</sup> <sup>ha</sup> <sub>m</sub> <sub>hat</sub> <sub>das</sub> <sub>nötige</sub> <sup>Fachwissen,</sup> <sup>um</sup> <sup>solide</sup> <sup>Info</sup> <sub>or</sub> <sub>the</sub> <sub>team</sub> <sub>to</sub> <sub>support</sub> <sub>the</sub> <sub>m</sub>e<sup>mbers</sup> <sup>as</sup> <sup>well</sup> <sup>a</sup> <sub>einschaft</sub> <sub>best</sub>m<sup>öglichst</sup> <sup>zu</sup> <sup>unterstütz</sup> <sub>eam</sub> <sub>scheint</sub> <sub>es</sub> <sub>wichtig</sub> <sub>zu</sub> <sub>sein,</sub> <sub>die</sub> M<sup>itg</sup> <sub>ch</sub> <sub>extent</sub> <sub>do</sub> <sub>you</sub> <sub>agree</sub> <sub>with</sub> <sub>the</sub> f<sup>ollowing</sup> <sup>st</sup> <sub>eit</sub> <sub>stim</sub>m<sup>en</sup> <sup>Sie</sup> <sup>den</sup> <sup>unten</sup> <sup>genannten</sup> <sup>Aus</sup>

<table><tr><td></td><td>Stimme voll und ganz zu Agree strongly</td><td>Stimme zu Agree</td><td>Teils, teils Partly</td><td>Stimme nicht zu Disagree</td><td>Stimme überhaupt nicht zu Disagree strongly</td></tr><tr><td>A. Die anderen Mitglieder von krebsgemeinschaft.de kennen sich in den Bereichen gut aus, über die sie diskutieren. / The other members of krebsgemeinschaft.de are familiar with the topics they discuss.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>B. Die anderen Mitglieder sind vertrauenswürdig / The other members are trustworthy</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>C. Die Informationen, die die anderen Mitglieder bereit stellen, sind in meinen Augen nicht immer richtig. / Not all information provided by the other members is always correct.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr><tr><td>D. Den Mitgliedern von krebsgemeinschaft.de liegen die anderen Mitglieder am Herzen. / The members mean a lot to each other.</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td><td>☐</td></tr></table>

<table><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr><tr><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td><td>□</td></tr></table>
