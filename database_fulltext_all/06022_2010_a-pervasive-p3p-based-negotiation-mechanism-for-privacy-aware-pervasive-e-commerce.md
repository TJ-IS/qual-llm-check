---
otero_id: 6022
otero_key: "KPUBXA6B"
title: "A pervasive P3P-based negotiation mechanism for privacy-aware pervasive e-commerce"
authors: "Ohbyung Kwon"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2010.08.002"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A pervasive P3P-based negotiation mechanism for privacy-aware pervasive e-commerce

Ohbyung Kwon ⁎

School of Management, Kyung Hee University, Seoul, South Korea

## a r t i c l e i n f o

Article history: Received 12 November 2007 Received in revised form 23 July 2010 Accepted 8 August 2010 Available online 11 August 2010

Keywords: P3P Pervasive computing Pervasive e-commerce Agent technology Privacy-preserving system Context-awareness

## a b s t r a c t

Privacy management is crucial in conducting pervasive computing services. The Platform for Privacy Preferences (P3P) is one of the most signi<sup>fi</sup>cant efforts currently underway for users of Web-based services. Since users are typically nomadic in pervasive computing services, however, their speci<sup>fi</sup>c privacy concerns change dynamically with context. This leads us to develop a dynamically adjusting P3P-based policy for a personalized, privacy-aware service as a core element of secure pervasive computing. The purpose of this paper is to propose dynamically and <sup>fl</sup>exibly a pervasive P3P-based negotiation mechanism for a privacy control of those functions. To do so, we consider and implement a multi-agent negotiation mechanism on top of a pervasive P3P system.

© 2010 Elsevier B.V. All rights reserved.

## 1. Introduction

Along with hardware, network protocols, interaction substrates, applications, and computational methods, privacy control is among the primary issues in pervasive computing. Privacy usually refers to personal information, and the invasion of privacy is usually interpreted as the unauthorized collection, disclosure, or other use of personal information as a direct result of electronic commerce transactions [47]. Privacy concerns are a signi<sup>fi</sup>cant social issue in electronic society including e-commerce stakeholders and virtual communities [14,31]. It has been known that privacy concerns in<sup>fl</sup>uence on the stakeholders' decision process [45]. In pervasive computing systems, which make use of user-related information to interact more naturally with users through a set of devices in a task environment, users' sensitive information could be collected by a variety of service providers, potentially threatening their privacy [39]. Lahloh et al. addressed the fear of <sup>fi</sup>lling out forms found among service users, and hence stressed the importance of enhanced privacy guidance constructed with invisible computers in pervasive computing environments [27,28]. Privacy issues, as well as agent-based automation issues, are more critical in context-aware services that run in pervasive computing environments [4,24,26,43]. The privacy control might not be scalable if the information about privacy control is aggregated centrally. The uni<sup>fi</sup>ed privacy tagging project is an on-going effort to prevent undesirable object aggregations in context-aware systems in a scalable manner [20].

To fully realize the potential of pervasive computing, application designers must incorporate users' personal privacy preferences [9]. To protect users' privacy in ubiquitous or pervasive computing settings, the Privacy Pro<sup>fi</sup>le Negotiation Protocol (PPNP) has been proposed. PPNP, initiated by the Tohda Lab at Keio University in Japan, manages users' privacy pro<sup>fi</sup>les by permitting transfer of pro<sup>fi</sup>les only to trusted services. In a similar effort, ETH Zurich has been developing a privacyaware system that implements P3P.

The Platform for Privacy Preferences (P3P) is an of<sup>fi</sup>cial effort of the World Wide Web Consortium (W3C) to enable Web-based service users to gain control over their private information [12] and is designed in particular to automatically determine with which service providers and users' personal information may be shared. P3P provides a way for a Web site to encode its data-collection and data-use practices in a machine-readable XML format known as a P3P policy [10]. So far, however, efforts to balance privacy protection and service quality have proven ineffective [33].

The setup of a pervasive computing environment with P3P policies for pervasive e-commerce should be quite feasible. In recent years, many research teams have focused on P3P-based privacy-aware ubiquitous or pervasive computing systems and services [15,17,22,29,30,34,42,48,49]. Using the P3P extension framework, Langheinrich has implemented a mechanism for describing dissemination practices based on the location of the data-collection for a privacy-aware system [30].

To extend privacy-aware pervasive e-commerce protocols based on P3P, however, one must consider a large number of sensors, data exchanges, and users with a variety of preferences so that P3P might be applicable; in other words, privacy concerns in pervasive e-commerce are signi<sup>fi</sup>cantly dependent upon the context of the user. A context-free uniform privacy policy would probably work poorly in a pervasive e-commerce model. Despite the availability of P3P, there are still few mechanisms to negotiate differences in systems or to advise users how to achieve their goals [14]. Based on the outstanding research about negotiation strategies between Web sites and user agents done by Cranor and Resnick, context-awareness is essential to practical P3Pbased protocols [11]. No matter what differences there are among their levels of privacy preferences and trust are, users may be treated with the same blanket privacy policy. This approach may disappoint loyal users, hence putting that loyalty directly at risk. To resolve these concerns, providing a personalized privacy policy that takes into account both users' individual characteristics and their point-of-service context in an automatic, dynamic, and <sup>fl</sup>exible way would help realize an unobtrusive and secure pervasive computing service. As Cespedes and Smith have argued, users may fear the widespread availability and use of their personal information [8]. Moreover, the dimensionality of the issues, which include collection, errors, secondary use, and improper access, might not be absolute or <sup>fi</sup>xed as users' perceptions and surrounding conditions continually change [40]. Hence, what and how the personal information including contextual data could be made are explicitly known to the user and then adjusted according to the user's context.

To date, studies on privacy in pervasive computing services consider policy matching, which is useful in protecting user data. Researchers assumed in these studies, however, that no negotiation mechanism is needed in interchanging user data and services. The privacy-aware Salsa agent system is outstanding in that the system considers the negotiation phase between users and brokers. In the system, activation of the negotiating state could occur when the broker rejects the request of a user agent when accessing a service agent [44]. Salsa, however, should be extended to allow agents to negotiate with the privacy policy itself. Therefore, this leads us to extend legacy P3P-based privacy management in order to enhance freedom in registering the nomadic user's personal information. To do so, the following unresolved research issues must be addressed: <sup>fi</sup>rst, the service provider's privacy policy should be dynamically designed according to the user's current context, because the nomadic user's privacy concern structure may vary with context. This functionality would decrease the service provider's negotiation efforts. Second, the provider's privacy policy should be personalized to individual users. In particular, a user's reputation value is crucial for privacy policy negotiation. Reputation has been regarded as crucial in electronic marketplace, and hence pivotal in building privacy-aware services that enable users to manage privacy effectively [21,23,50]. Reputation is important in determining the level of risk to which individuals are exposing themselves to and is therefore needed to develop an appropriate privacy policy. Reputation hence provides an operable metric for establishment of trust between unknown entities, and is pivotal in building systems that enable users to manage privacy effectively [36]. Users with a better reputation will be less likely to have service providers require detailed personal information in order to provide better service. The information of reputation is managed by maintaining a history of behavior for users in privacy-aware ubiquitous computing systems [38]. eBay's Feedback Forum is, to our knowledge, one of the most famous systems which have successfully incorporated reputation [40]. Service providers may want the <sup>fl</sup>exibility to apply different privacy policies for different users according to user reputation value.

This paper proposes the concept of P4P (Pervasive Platform for Privacy Preferences), an extension of P3P, and develops a P4P-based negotiation methodology for privacy-aware pervasive computing services. The methodology includes a context-aware policy design and personalization. It also takes into consideration a user's personal pro<sup>fi</sup>le – current location, demographic data, reputation – as context. Moreover, the proposed methodology balances privacy protection and service quality. To do so, <sup>fi</sup>rst, we consider privacy protection by allowing users to negotiate with the services on submitting data elements according to their privacy preferences; in other words, the user can intervene on “required data elements.” Second, giving the users the right to required data elements may decrease the service quality in terms of service utilization since a lack of user-speci<sup>fi</sup>c data may result in fewer provided services from the service provider's viewpoint. To resolve this problem, we consider the reputation mechanism to selectively accept the user's privacy concerns.

The remainder of this paper is organized as follows: Section 2 reviews privacy issues and P3P-aware systems. Section 3 describes a negotiation mechanism with the concept of P4P. In Section 4, performance test is shown, and concluding remarks are made in Section 5.

## 2. Related work: privacy issues and P3P

In recent years, privacy protection has been among the most active and spotlighted issues in electronic business. Accordingly, developing solutions to these privacy concerns that are both technically and socially secure is important. For example, many commercial Web sites provide a privacy policy, because these sites require personal information such as name, e-mail address, certain preferences, and even a social security number (SSN). Specifying a site's privacy policy to inform the users before they register for services has been regarded as a sound way to mollify users' privacy concerns.

The design of P3P is partially derived from the code of ethics for user agents. Based on the CMA code of ethics, it prescribes that a user agent should follow such a code in terms of notice and communication, choice and control, fairness and integrity, and security [46].

To specify a privacy policy in a complete and standardized way, policy speci<sup>fi</sup>cation languages such as EPAL and P3P have emerged. Among these, the P3P speci<sup>fi</sup>cation de<sup>fi</sup>nes the syntax and semantics of P3P-based privacy policies. Since the speci<sup>fi</sup>cations are in a machine-readable format, user agents can understand P3P speci<sup>fi</sup>cations and then automate decision-making on behalf of their users when appropriate, so that users need not read the privacy policy of every site they visit. The user agent is a program which mediates interactions with services on behalf of the user according to her preference. Various privacy-preserving systems based on P3P have been proposed over the last decade. Ackeman proposed a technical mechanism to inform users of data requests and their consequences [2]. A privacy control module could be embedded in the privacyaware systems as middleware [18]. The Personal Context Agent Networking (PeCAN) knowledge architecture consists of both clientand Web-side architectural data components and services, which inform the user of online privacy and trust within e-commerce tasks [22]. Representative commercial examples that use a P3P policy include Microsoft's Explorer Ver6.0 and AT&T's Privacy Bird.

The <sup>fl</sup>ow of personal information in pervasive computing services has been explained with economic models. Acquisti described an economic model as a function of the expected bene<sup>fi</sup>ts of completing the transaction, including the expected bene<sup>fi</sup>ts of maintaining information privacy [3]. Jiang et al. [19] used an economics-based approach to analyze information <sup>fl</sup>ow in ubiquitous computing. Price and Adam [35] described a framework that allows users <sup>fl</sup>exible control of releasing personal data in a ubiquitous computing environment.

However, current research studies seldom address methods for resolving user privacy concerns in a pervasive computing environment. To resolve this problem, discussions are being held to create a better, more complete speci<sup>fi</sup>cation of P3P [5]. A privacy-aware service in a pervasive computing environment for nomadic users requires amended and tailored P3P speci<sup>fi</sup>cations.

## 3. System overview

## 3.1. Overall framework

To realize a P4P-aware pervasive computing service, an overall negotiation framework is proposed as shown in Fig. 1. To determine optimal service usage, the framework should take the following requirements into account:

![](/api/attachments/KPUBXA6B/fulltext/images/b9225b0f531a9d537d5e30de02d65c7da0702ac2bb63f40125928a015d6d688c.jpg)  
Fig. 1. Overall negotiation framework.

• Enable dynamic P3P policy change according to user's privacy preference.

• Enable dynamic P3P policy change according to the user's current context.

Since the policy reference in the P3P 1.0 speci<sup>fi</sup>cation allows the P3P policy to be located in a well-known location, we assume that the privacy preference is stored as an ontology <sup>fi</sup>le, so that user agents may easily access each other for a negotiation to execute a service.

In a pervasive computing service environment, the user interface for nomadic users will not be restricted to a Web browser, but may be extended to any interface that adopts advanced technologies such as multimodal interaction, augmented reality, and motion recognition. For this reason, the framework should consider a pervasive computing service zone for services with P4P-negotiated interactions. In this zone, the user's current context data can be detected by an array of sensors and then delivered to user agents through the sensory network to provide service in advance.

Entering into the service zone, the user agent accesses the service list to select a service on the user's behalf. Pervasive computing services obviously need to be aware of the current regulatory regime so that they can comply with it [35].

Hence, a basic P4P interaction might proceed as follows:

• The user agent identi<sup>fi</sup>es the user's current context and formulates the user's dynamic privacy policy <sup>fi</sup>le.

• The user agent sends the user's dynamic privacy policy to the service agent to request the preference policy URI of the service agent.

• The service agent considers the user's privacy policy, customizes the P3P proposals, and then informs the user agent of the URI.

• The user agent visits the URI, and one or more P3P proposals are retrieved.

• The user agent evaluates the proposal according to the user's privacy preference rule set and determines what actions to take (e.g., deny, accept, prompt, or send a counter-proposal).

• If the proposal is consistent with the user's preferences, then an agreement is reached. The agent sends the service the ID of the proposal.

• The service provides the user with the customized pervasive service.

## 3.2. Pervasive Platform for Privacy Preferences (P4P)

P4P is an extension of conventional P3P that additionally considers speci<sup>fi</sup>cations relevant to context-sensitive privacy control. A tree structure is used to represent data elements in P3P speci<sup>fi</sup>cations. For example, the data element “vehicle.model” is a child of the data element “vehicle.” However, since the current P3P speci<sup>fi</sup>cation does not consider contextual data, we extend it to include dynamically changing data elements using existing notation. To represent these dynamic elements, we suggest the following method:

## P3P data schema.CONTEXT.context field.context\_value.

Note that default value for context\_value is false. For instance, if a user provides only two declarations for privacy preferences on GPS position data as:

## user.current.GPS\_position.Activity.public.true and

user.current.GPS\_position.Location.moderate.true,

then the user's current GPS position is required when his or her activity is public and the location is in a moderate space, respectively. Other than those two data points, the context value is set to false, which indicates that the data is not required in such context. For example, if we do not declare user.current.GPS\_position.Activity.public, then user.current.GPS\_position.Activity.public is automatically set to false.

To deliver the context data element to the service providers, context information can be acquired from either a personal context ontology or a user agent. Table 1 lists the categories in the P4P context model. The context model partially relies on Dey's context classi<sup>fi</sup>cations: time, identity, location, activity, and computational entity, which are widely adopted in context-aware system development [13,25]. Social context is included in the category because it becomes more important for community-based system [1,47]. Among these context categories, we will focus in this paper on identity, especially reputation, to explain the proposed methodology.

## 3.3. Negotiation mechanism

Privacy concerns arise when there is tension for an individual between the gains earned by providing information and the need to hide the personal information [37]. For user privacy, we adopt an economics-based model on privacy-ef<sup>fi</sup>ciency trade-offs similar to Milne and Gordon's for the negotiation mechanism [32]. Hence, we recognize the P4P-based privacy-aware system as the process of social contracts between client as privacy data supplier, and service provider as demander. The <sup>fi</sup>rst step in the process of addressing the privacyef<sup>fi</sup>ciency trade-off is identifying the attributes that affect the overall process of social contracts. In this paper, we focus on the user's reputation. The contracting dyads then establish privacy proposals which may result in different levels of risk: on the one hand, the client worries about low service quality and high surveillance level, and, on the other hand, the service provider worries about having a too-low surveillance level and its client's potential withdrawal due to poor service quality. Hence, the dyads intend to <sup>fi</sup>nd the optimal level of surveillance that will minimize the risks both of the cost of surveillance and of the cost of low service quality.

Table 1 Proposed context model.

<table><tr><td>Context category</td><td>Context field</td><td>Examples</td></tr><tr><td rowspan="3">Activity</td><td>Public</td><td>Current schedule</td></tr><tr><td>Moderate</td><td></td></tr><tr><td>Private</td><td></td></tr><tr><td rowspan="3">Location</td><td>Public</td><td>Current location</td></tr><tr><td>Moderate</td><td></td></tr><tr><td>Private</td><td></td></tr><tr><td rowspan="2">Computational entity</td><td>Available</td><td>Device, network, TV channel, etc.</td></tr><tr><td>Unavailable</td><td></td></tr><tr><td rowspan="3">Social</td><td>Public</td><td>Nearby person</td></tr><tr><td>Private</td><td></td></tr><tr><td>Alone</td><td></td></tr><tr><td rowspan="3">Physical environment</td><td>Excellent</td><td>Temperature, climate, etc.</td></tr><tr><td>Moderate</td><td></td></tr><tr><td>Poor</td><td></td></tr><tr><td rowspan="3">Identity</td><td>High</td><td>Reputation</td></tr><tr><td>Moderate</td><td></td></tr><tr><td>Low</td><td></td></tr></table>

The economics-based model seeks an optimal privacy policy in terms of cost, which is calculated by trade-offs between the cost of low service quality and the cost of surveillance—delivering one's private information to the other side. The cost incurred by a negotiation break-down resulting from the interest discrepancy between the user and service provider parties is the cost of low service quality. On the other hand, the cost of surveillance indicates the economical and/or psychological concern occurred by delivering private data to service providers to get served. Privacy preferences and actual behavior often exhibit a trade-off relationship, which can sometimes cause complications to users [7].

The functions are suggested by the authors based on two underlying theoretical models: the economic rationality model and the bounded rationality model. In the economic rationality model through rational choice theory, the service provider will invest in a surveillance system in order to maximize the provider's pro<sup>fi</sup>t [6]. The service provider is interested in and motivated by the surveillance factor which can increase the provider's service quality—hence, more bene<sup>fi</sup>t and ultimately less cost. The marginal bene<sup>fi</sup>t of surveillance will be increased and the marginal cost will be decreased. And, the inverse is also true: the cost of low service quality will exponentially increase as surveillance levels decrease, and the cost of surveillance will exponentially increase as the lower priority surveillance factors are considered in the surveillance system.

Secondly, Simon's bounded rationality, the base of decision support system research, is also adopted in the model [41]. According to bounded rationality, the decision makers may act differently with the same information, which are $\left( c _ { i } , p _ { i } , o _ { i } , r _ { i } \right)$ in the manuscript. In a dynamic P3P context, bounded rationality is re<sup>fl</sup>ected to the shapes of cost functions, which can be different from each other. The authors put the decision maker's subjective values by designing the cost functions with two parameters: α and β. Also we invite contextual information into our model to better explain the decision maker's bounded rational behavior.

Hence, as shown in Fig. 2, for a data element i, the costs of surveillance, $y = \alpha _ { 2 , i } e ^ { \beta _ { 2 , i } s } { } _ { i } ,$ and of low service quality, $y = \alpha _ { 1 , i } e ^ { - \beta _ { 1 , i } s } { } _ { i } ,$ depend on the level of surveillance,s .

The negotiating method is represented as follows:

STEP 1: the user agent requests the service provider's P3P policy. The P3P policy Ψ is represented as:

$$
\Psi = \{(c _ {1}, p _ {1}, o _ {1}, r _ {1}), \dots , (c _ {i}, p _ {i}, o _ {i}, r _ {i}), \dots , (c _ {N}, p _ {N}, o _ {N}, r _ {N}) \}\tag{1}
$$

where N is the number of data elements included in the P3P policy, $c _ { i } \in C , \ p _ { i } \in P , o _ { i } \in O = \{ a l w a y s , o p t - i n , o p t - o u t \} , r _ { i } \in R ,$ where $C , P ,$ O, and R indicate sets of categories, purposes, options, and retentions, respectively. Category considered in this paper is already described in Table 1. The purpose element describes as to why the data is being collected relevant to the web site. The retention element indicates how long the site will keep the personal information. These four factors are basically provided in P3P speci<sup>fi</sup>cations.

STEP 2: the user agent produces an optimal solution by minimizing the total cost. The total cost on the user's side is determined by a data element where the optimal cost of surveillance is more than those of any other data elements.

![](/api/attachments/KPUBXA6B/fulltext/images/cc29a9bcadea4e4698ff27231b3837142b8c4c7377b19acd3bb301f377fa4324.jpg)  
Fig. 2. Trade-off relationship for negotiation.

A data element's optimal cost is derived as follows. For all $i , f _ { i } ( s _ { i } | c _ { i } , p _ { i } ,$ $o _ { i } , r _ { i } ) = \alpha _ { 1 , i } e ^ { - \beta _ { 1 , i } s _ { i } } + \alpha _ { 2 , i } e ^ { \beta _ { 2 , i } s _ { i } }$ , since the cost of low service quality is $y = \alpha _ { 1 , i } e ^ { - \beta _ { 1 , i } s _ { i } }$ and the cost of surveillance is $y = \alpha _ { 2 , i } e ^ { \beta _ { 2 , i } s _ { i } }$ . Hence, the optimal level of surveillance of the ith data elemen $; s _ { i } ^ { * } ,$ , with the given $c _ { i } ^ { * } , p _ { i } ^ { * } , 0 _ { i } ^ { * } , r _ { i } ^ { * }$ is derived as Eq. (2):

$$
s _ {i} ^ {*} = \frac {\ln \alpha_ {1 i} \beta_ {1 i} - \ln \alpha_ {2 i} \beta_ {2 i}}{\beta_ {1 i} + \beta_ {2 i}}\tag{2}
$$

Then the total cost of the user's side is represented as in Eq. (3):

$$
\begin{array}{c} T C _ {U} = M a x \Bigl \{f _ {1} (s _ {1} ^ {*} | c _ {1} ^ {*}, p _ {1} ^ {*}, o _ {1} ^ {*}, r _ {1} ^ {*}), f _ {2} (s _ {2} ^ {*} | c _ {2} ^ {*}, p _ {2} ^ {*}, o _ {2} ^ {*}, r _ {2} ^ {*}),..., f _ {N} \\ \times (s _ {N} ^ {*} | c _ {N} ^ {*}, p _ {N} ^ {*}, o _ {N} ^ {*}, r _ {N} ^ {*}) \Bigr \} \end{array}\tag{3}
$$

where $s _ { i } ^ { * }$ denotes the optimal level of surveillance of the ith category.

STEP 3: suppose that $T C _ { U } = f _ { M } \big ( s _ { M } ^ { * } | c _ { M } ^ { * } , p _ { M } ^ { * } , o _ { M } ^ { * } , r _ { M } ^ { * } \big )$ ; 1≤M≤N. Then, the optimal set of user preferences, $\{ s _ { 1 } ^ { * } , s _ { 2 } ^ { * } , . . . s _ { i } ^ { * } , . . . s _ { N } ^ { * } | c _ { 1 } ^ { * } , . . . c _ { N } ^ { * } , p _ { 1 } ^ { * } , . . . ,$ $p _ { N } ^ { * } , o _ { 1 } ^ { * } , . . . , o _ { N } ^ { * } , r _ { 1 } ^ { * } , . . . , r _ { N } ^ { * } \}$ , is passed to the Negotiator, so that the Negotiator can compare the user's preferences to those of the service agent.

STEP 4: for any category i, service agent sets $s _ { i } = s _ { i } ^ { * }$ . Then the total cost of the service provider is as in Eq. (4):

$$
\begin{array}{c} T C _ {S} = M a x \Bigl \{g _ {1} \bigl (p _ {1} ^ {*}, o _ {1} ^ {*}, r _ {1} ^ {*}, c _ {1} ^ {*} | s _ {1} \bigr),..., g _ {j} \Bigl (p _ {j} ^ {*}, o _ {j} ^ {*}, r _ {j} ^ {*}, c _ {j} ^ {*} | s _ {j} \Bigr),..., g _ {N} \\ \times \bigl (p _ {N} ^ {*}, o _ {N} ^ {*}, r _ {N} ^ {*}, c _ {N} ^ {*} | s _ {N} \bigr) \Bigr \} \end{array}\tag{4}
$$

STEP 5: the optimal set of the service provider's optimal preference is as in Eq. (5):

$$
\begin{array}{c} \{p _ {1} ^ {*},..., p _ {j} ^ {*},..., p _ {N} ^ {*}, o _ {1} ^ {*},..., o _ {j} ^ {*},..., o _ {N} ^ {*}, r _ {1} ^ {*},..., r _ {j} ^ {*},..., r _ {N} ^ {*}, c _ {1} ^ {*},..., c _ {j} ^ {*}, \\ ... , c _ {N} ^ {*} | s _ {1},..., s _ {i},..., s _ {N} \} \end{array}\tag{5}
$$

Then, Eq. (5) is passed to the Negotiator.

STEP 6: the Negotiator asks the User agent if the service provider's optimal preference is acceptable. If so, stop. If not, preference relaxation is performed according to the following rules:

## [Rules of preference relaxation for User agent]

Rule 1 (Reputation rule): send any privacy-free pro<sup>fi</sup>le to prove that the user is trustworthy, so that the Service agent may optimize its preference by requiring a higher condition category value for the user. The privacy-free pro<sup>fi</sup>le is deeply related to estimate the user's reputation.

Rule 2: while keeping the value of the total cost of the user's side $\left( T C _ { U } \right)$ unchanged, change the level of surveillance $\left( { { s _ { i } } } \right)$ except the optimal level of the level of surveillances $\left( { { s _ { M } } } \right)$ , because $s _ { M }$ is the determinant of $T C _ { U } .$

Rule 3: if the User agent is prompted to allow more surveillance $\left( { { s _ { i } } } \right)$ , increasing the total cost of the user's side $( T C _ { U } )$ , the User agent should ask the user for permission to do so.

## [Rules of preference relaxation for Service agent]

Rule 1: send any privacy-free pro<sup>fi</sup>le to prove that the service provider is trustworthy, so that the User agent can optimize its preference by requiring category values with better conditions to the service provider.

Rule 2: by keeping the value of the total cost of the seller's side $\left( T C _ { S } \right)$ unchanged, change the level of $( c _ { j } , p _ { j } , o _ { j } , r _ { j } )$ except that of $\left( c _ { j } ^ { * } \right.$ $p _ { j } ^ { * } , o _ { j } ^ { * } , r _ { j } ^ { * } )$ , because $\left( c _ { j } ^ { * } , p _ { j } ^ { * } , o _ { j } ^ { * } , r _ { j } ^ { * } \right)$ is the current determinant $\mathsf { o f } T \dot { C } _ { S } .$ Rule 3: if the Service agent requires a value of $( c _ { j } , p _ { j } , o _ { j } , r _ { j } )$ that can increase $T C _ { S } ,$ the Service agent should inform the service provider to acquire permission.

Preference relaxation is useful for increasing the rate of service utilization while preserving the user's privacy concern. If the service provider requires a data element that the user does not want to provide, the transaction would be closed. However, if the user is trustworthy, then the service provider may make a concession to the user's privacy concerns by either withdrawing the original data request or by suggesting a different piece of information about which the user has less of a privacy concern.

## 4. Experimental evaluation

## 4.1. Setting of the experiment

The aim of this experiment is to investigate how the P4P-aware pervasive computing service adopting the negotiation strategy proposed in this paper provides value that varies by user in terms of service utilization. To do so, to illustrate the technical and operational viability of the negotiation mechanism proposed in this paper, an experimental evaluation was carefully conducted before introducing the P4P-based pervasive computing service.

We developed a prototype system, P4P-based recommendation system, running on an IBM Pentium Server with one 1.8G processor, 1Gbyte of RAM, and a 120 Gbyte hard disk. The negotiation mechanism was programmed in Java SDK 1.4.x running on Microsoft Windows XP Professional Edition. The experiments were conducted with PDAs, which can access the prototype system via a wireless Internet connection.

## 4.2. Experimental design

Each experimental design has 19 participants as subjects: nine buyers and ten sellers. Each seller plays a role of one of the actual shops: W. Bank, H. Bank, F. Café,.S. Bucks Café, Post Of<sup>fi</sup>ce, S. Café, S. Of<sup>fi</sup>ce, Kiosk #1, Kiosk #2, and Kiosk #3. In all of the experiments reported here, the subject pool consisted of graduate students in technology management or international management department at Kyung Hee University. Of the 19 participants, only one is a <sup>fi</sup>rstyear graduate student; the others are in their second year or later. The participants were well acquainted with the service, regardless of their demographic characteristics. Moreover, the participants were quite skillful in using the mobile devices, PDAs. Usable data was hence successfully collected from the participants. Each participant received a set of instructions prior to the experiment and proceeded through the instruction at her own pace. Upon completion of the instructions, the PDA is provided to the buyers. To eliminate unanticipated bias involving PDA usage, instructions were given for how to use the PDA. After careful explanation, the users were asked to <sup>fi</sup>ll in their contextual preferences for using personal information in the context customer relationship management, including for one-to-one marketing such as providing promotion or events. A couple of data elements is considered in the negotiation: user id, user pro<sup>fi</sup>le, phone number and home address. The P4P preference rating screen is shown as Fig. 3. At anytime, of course, the user can modify the ratings.

Reputation is categorized as high, moderate and low as context. To determine the optimal level of surveillance for each data element, the values $\alpha _ { 1 } , \beta _ { 1 } , \alpha _ { 2 } ,$ and $\beta _ { 2 }$ are set by the user. Since it is dif<sup>fi</sup>cult for the user to choose numerically appropriate values, we provided them with simple questions and a 5 Likert scale. If the buyer does not explicitly rate her preference, the values are set to the default.

The sellers are asked to <sup>fi</sup>ll in the reputation value for each buyer. To help them rate the reputation value, a sort of anonymous personal pro<sup>fi</sup>le is provided, including age and income.

The buyer then runs the P4P-based service while walking around the shops with the PDA. When the user approaches a shop, she or he may get a recommendation from the corresponding seller. Fig. 4 shows the results of the P4P suggestion about which data elements are requested to make further recommendations. If the suggestion is acceptable, the user is asked to select ‘like’ and proceed. Otherwise, she would select ‘dislike.’ As shown in $\mathrm { F i g . ~ } 4 ( \mathsf { a } )$ and (b), the same buyer may receive different suggestions from different sellers. Woori Bank just requests the user's address to make a P4P-aware recommendation, while F. Café requires all data elements. These differences occur mainly because of varying recognition of the user's reputation value and negotiation strategies. Source credibility theory can similarly support reputation mechanisms that could be applied [16]. For the experiment, three strategies are randomly selected and applied to get the results: suggestion without negotiation (NO\_NEGO), suggestion with negotiation (NEGO), and suggestion with negotiation having reputation value as context (NEGO\_REPUT). During the experiment, to eliminate any bias affecting evaluation of the <sup>fi</sup>nal result, buyers are not informed of which strategy is applied. When buyers select ‘like’ or ‘dislike’, the evaluation results are stored in the database for further performance evaluation.

## 4.3. Result 1: the effect of negotiation mechanism on service utilization

In this paper, two underlying theories that show the market ef<sup>fi</sup>ciency of web-based services are described: transaction cost theory and agency theory. Success rate is one of the most widely acknowledged metrics for evaluating transaction processing performance. Increasing the transaction success rate would decrease the market ef<sup>fi</sup>ciency by reducing overall transaction costs. Traditionally, a service agent in multi-agent system attempts to increase the transaction success rate by decreasing selling price, which does not guarantee the pro<sup>fi</sup>tability of the service provider. However, since our P4P based negotiation increases the rate without also increasing the price level, the proposed mechanism is more pro<sup>fi</sup>table. The success rate in reaching a deal (sr) is described as follows:

![](/api/attachments/KPUBXA6B/fulltext/images/eedfb68f96e15b7b1a6f74dac8c241febabbc3a52f33fea78287fdd318fb1eee.jpg)  
Fig. 3. Screenshot of P4P Rating.

$$
s r = \frac {\sum_ {i = 1} ^ {N} s _ {i}}{N}\tag{6}
$$

where $s _ { i } = 1$ if the ith pair of user agent and service agent has eventually agreed to transact, and 0 vice versa. N indicates total number of pairs.

One of the major issues regarding privacy-preserving systems is to increase the service utilization while addressing users' privacy concerns. That the users cannot selectively submit data items to be reported is mainly a product of the current limitations of Web-based systems. Even in cases of P3P-based privacy-aware systems, only the service provider determines P3P content. We hence need to examine whether our negotiation mechanism is signi<sup>fi</sup>cantly effective in increasing market ef<sup>fi</sup>ciency in terms of success rate (Hypothesis 1).

Hypothesis 1. P3P-based privacy-preserving system with the proposed negotiation mechanism (NEGO) will outperform that without a negoti ation mechanism (NO\_NEGO) in terms of the mean success rate.

The cost of surveillance and the cost of low service quality are then determined to derive automatically the total cost and the optimal level of surveillance for each data element. If all of the optimal solutions are implemented, the <sup>fi</sup>nal cost is then determined by selecting the maximum total cost among the data elements. Using a threshold value set by the seller, a <sup>fi</sup>nal decision is made about whether the privacy policy is accepted.

If the user does not accept the policy, then the negotiation system informs the service provider, inquiring whether the service provider is willing to relax the policy. To make this decision, the user's reputation value is considered. For the actual e-commerce system, user reputation data could be estimated partially using the data provided by <sup>fi</sup>nancial agencies, and partially using the user pro<sup>fi</sup>le stored in the personal ontology. However, determining the estimation function is a <sup>fi</sup>nancial engineering or trust issue and is beyond the scope of the current research. Reputation evaluation methods such as the EigenTrust mechanism, Dempster–Shafer theory, and the Behavior

Characteristics-based reputation evaluation method could be accepted for future work [25,36].

In our laboratory experiment, reputation value was computed based on the Behavior Characteristics-based reputation evaluation method: The value of reputation is derived from the user's past behavior history using our prototype system. In this method, user behavior is categorized into several types: basically stable, steadily increasing, steadily decreasing, etc. The acceptable degree of relaxation is determined using the user's reputation value: relaxing the purpose, retention, or even dropping the data element from the list. The temporally updated P4P is then resent to the negotiator for the next round. To simplify our experiment, only two rounds were allowed for relaxation. If more relaxations are allowed, the success rate will be greater than that seen in this experiment.

To test Hypothesis 1, we adopted the paired samples t-test to compare the mean success rate of the two mechanisms: NO\_NEGO and NEGO. Based on the results listed in Table 2, we could conclude that the negotiation mechanism signi<sup>fi</sup>cantly increases the success rate. The statistical test results for Hypothesis 1 indicate that the null hypothesis is strongly statistically rejected at less than 1% signi<sup>fi</sup>cance levels. The negotiation mechanism positively affects the usage of privacy-aware services.

Increasing the success rate in an automated manner, as shown in Table 2, implies that the bene<sup>fi</sup>t of the proposed negotiation mechanism can also be illustrated by agency theory: the higher the success rate between user agent and service agent, the higher the ef<sup>fi</sup>ciency of hiring computational agents. This results in decreasing agency costs via automated transactions.

## 4.4. Result 2: the effect of reputation awareness on service utilization

We conducted another experiment to examine the extent to which considering user reputation in<sup>fl</sup>uences the performance of the negotiation mechanism. A client with a higher socio-economic status and credits in fact has a higher reputation, which in turn affects the usage of web-based services. Research also shows that reputation is a determinant of trust, which signi<sup>fi</sup>cantly affects e-transactions. Reputation is a key for discerning with whom the client or supplier should transact.

(a) Sample result (Woori bank)  
![](/api/attachments/KPUBXA6B/fulltext/images/950aed6fe74812e7538626b0617c724dfca9c458a348caa90fba80f670cf56f9.jpg)

(b) Sample result (F.Café)  
![](/api/attachments/KPUBXA6B/fulltext/images/50bbee0f6e21a58c38dac817115883c42d356c5f8621732fc33a5620a4170736.jpg)  
Fig. 4. Sample recommendation results (Woori bank).

Table 2  
Results of the statistical test—two-samples test for Hypothesis 1.

<table><tr><td rowspan="2">Performance measures</td><td colspan="5">Mean rate of service utilization</td></tr><tr><td colspan="3">Without negotiation mechanism (NO_NEGO)</td><td colspan="2">With negotiation mechanism (NEGO)</td></tr><tr><td rowspan="2">Success rate</td><td>23.33%</td><td></td><td></td><td>65.24%</td><td></td></tr><tr><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>t</td><td>Significance (2-tailed)</td></tr><tr><td>NO_NEGO-NEGO</td><td>-.41905</td><td>.49458</td><td>.03413</td><td>-12.278</td><td>0.000***</td></tr></table>

\*\*\* p b 0.01.

Meanwhile, transactions have two kinds of risks: one, losing trustworthy clients by raising their privacy concerns and making them feel uncomfortable from being asked to reveal too much personal data; two, confronting risk by not requesting suf<sup>fi</sup>cient personal data from a client. One of the best ways to minimize these two risks, and hence increase the transaction success, is to give the client some <sup>fl</sup>exibility and choice—allow him or her freedom to not disclose personal data according to the level of reputation. The transaction decision must take reputation level into consideration: requesting more personal data from clients who have a lower reputation, and allow clients who have a higher reputation to not submit some personal data. The proposed negotiation method includes this task.

Consequently, to examine whether the proposed negotiation method intelligently behaves according to the client's reputation level, the success rate was compared between negotiation protocols both with and without consideration of reputation (Hypothesis 2):

Hypothesis 2. The P4P-based privacy-preserving system with a negotiation mechanism that considers reputation as context (NEGO\_REPUT) will outperform the P3P-based privacy-preserving system that does not consider reputation (NEGO), in terms of the success rate.

We again adopted paired samples t-test to compare the success rates of two mechanisms: NEGO and NEGO\_REPUT. Table 3 shows the results: the rate of service utilization is considerably higher when reputation is not considered. The results indicate that Hypothesis 2 seems to be rejected.

In this case, however, a higher success rate does not necessarily indicate superior performance, simply because users with a lower reputation are less likely to provide value to the service provider. Such users may even abuse the information of the service providers acquired during the use of the service. The service provider thus may want to grant the use of its services and information selectively, and by considering user reputation as a factor. A user with a higher reputation should be more than welcomed by the service provider and a user wither a poorer reputation may be less welcomed. To determine whether simple and reputation-aware negotiations would exhibit better performance, we conducted a regression analysis to examine to what extent reputation level could be a determinant. Fig. 5 shows that a negotiation mechanism that considers the user reputation seems more proportional to the reputation level than other mechanisms do. The F-values of each case are compared in Table 4. We conclude from that table that a negotiation that considers reputation is smarter than one that does not: The mechanism can selectively attract desirable users while avoiding users who have a lower reputation, to decrease service risk.

## 5. Conclusion

Pervasive P3P-based negotiation mechanisms are developed and evaluated, with the goal of increasing the possibility of a service match by decreasing the gap between the information that service providers require, and the personal information the user is willing to share. Since P4P assumes a nomadic user and a pervasive service running in any space, the speci<sup>fi</sup>cation includes contextual data elements, so that the service may keep track of the user's data which, again, may be dynamically changing. Based on these dynamically changing privacy preferences, negotiation of what information should be passed is a core idea addressed in this paper.

Table 3  
Results of the statistical test—one-way ANOVA for Hypothesis 2.

<table><tr><td rowspan="2">Performance measures</td><td colspan="5">Mean rate of service utilization</td></tr><tr><td colspan="2">Negotiation mechanism without considering reputation</td><td colspan="3">Negotiation mechanism considering reputation</td></tr><tr><td>Success rate</td><td>65.24%</td><td></td><td>60.95%</td><td></td><td></td></tr><tr><td></td><td>Mean</td><td>Std. deviation</td><td>Std. error mean</td><td>t</td><td>Significance (2-tailed)</td></tr><tr><td>NEGO-NEGO_REPUT</td><td>.04286</td><td>.50174</td><td>.03462</td><td>1.238</td><td>0.217</td></tr></table>

\* pb0.01.

![](/api/attachments/KPUBXA6B/fulltext/images/801cd7a90936255470393b55ef866ce9c99bed8cf62ddcf780b348c6d64b15ae.jpg)  
Fig. 5. Comparison of the success rates by changing reputation level

Table 4  
Results of statistical test—regression analysis.

<table><tr><td>Mechanism</td><td>d.o.f</td><td>MSR</td><td>MSE</td><td>F-value</td><td>R-Square</td></tr><tr><td>Without negotiation mechanism</td><td>209</td><td>.333</td><td>.179</td><td>1.859</td><td>0.009</td></tr><tr><td>Negotiation mechanism without considering reputation</td><td>209</td><td>.412</td><td>.227</td><td>1.817</td><td>0.009</td></tr><tr><td>Negotiation mechanism with considering reputation</td><td>209</td><td>10.832</td><td>.188</td><td>57.553*</td><td>0.217</td></tr></table>

\* pb 0.1.

Areas of future research include full-<sup>fl</sup>edged development of P4Pbased privacy-aware pervasive systems, provision of complete P4P categories, purposes and retentions, and evaluation of the negotiation mechanism to optimize performance. Meanwhile, since we adopt a hedonic task, shopping, in this paper, the outcome of the case study could only be generalized to hedonic tasks. An expanded study to overcome the generalization issues should be remained as future research. We currently plan to extend the presented mechanism so that it is available in legacy privacy-preserving systems.

## Acknowledgement

This research is supported by the Ubiquitous Computing and Network(UCN) Project, Knowledge and Economy Frontier R&D Program of the Ministry of Knowledge Economy(MKE) in Korea and a result of subproject UCN UCN 10C2-T2-11T.

## References

[1] G.D. Abowd, Social disclosure of place: from location technology to communication practices, Lecture Notes in Computer Science 3468 (2005) 134–151.

[2] M.S. Ackeman, Privacy in pervasive environments: next generation labeling protocols, Personal and Ubiquitous Computing 8 (6) (2004) 430–439.

[3] A. Acquisti, Protecting privacy with economics: economic incentives for preventive technologies in ubiquitous computing environments, Workshop on Socially-Informed Design of Privacy-enhancing Solutions in Ubiquitous Computing, Proceedings of the UbiComp 2002, Göteborg, Sweden, 2002.

[4] C. Adams, V. Katos, Privacy challenges for location aware technologies, IFIP International Federation for Information Processing 191 (2005) 303–310.

[5] R. Agrawal, J. Kiernan, R. Srikant, Y.R. Xu, XPref: a preference language for P3P, Computer Networks 48 (5) (2005) 809–827.

[6] G.S. Becker, G.N. Becker, The Economics of Life, McGraw-Hill, 1997.

[7] B. Berendt, O. Ganther, S. Spiekermann, Privacy in e-commerce: stated preferences vs. actual behavior, Communications of the ACM 48 (4) (2005) 101–106.

[8] F.V. Cespedes, H.J. Smith, Database marketing—new rules for policy and practice, Sloan Management Review 34 (4) (1993) 7–22.

[9] L.F. Cranor, M. Langheinrich, M. Marchiori, J. Reagle, The Platform for Privacy Preferences 1.0 (P3P1.0) Speci<sup>fi</sup>cation, W3C Recommendation, April 2002, HTML Version at www.w3.org/TR/P3P/.

[10] L.F. Cranor, P. Resnick, Protocols for automated negotiations with buyer anonymity and seller reputations, Netnomics 2 (1) (2000) 1–23.

[11] L.F. Cranor, Web Privacy with P3P, O'Reilly, 2002.

[12] M.J. Culnan, How did they get my name—an exploratory investigation of consumer attitudes toward secondary information use, MIS Quarterly 17 (3) (1993) 341–361.

[13] A.K. Dey, Context-aware computing: the CyberDesk project, AAAI 1998 Spring Symposium on Intelligent Environments, Technical Report SS-98-02, 1998, pp. 51–54.

[14] M. Duckham, L. Kulik, A Formal Model of Obfuscation and Negotiation for Location Privacy, Pervasive 2005, Munich, Germany, 2005, pp. 152–170

[15] J.B. Earp, A.I. Anton, L. Aiman-Smith, W.H. Stuf<sup>fl</sup>ebeam, Examining internet privacy policies within the context of user privacy values, IEEE Transactions on Engineering Management 52 (2) (2005) 227–237.

[16] M.A. Ekstrom, H.C. Bjornsson, C.I. Nass, A reputation mechanism for business-tobusiness electronic commerce that accounts for rater credibility, Journal of Organizational Computing and Electronic Commerce 15 (1) (2005) 1–18

[17] J. Goecks, E. Mynatt, Enabling privacy management in ubiquitous computing environments through trust and reputation systems, Proceedings of CSCW 2002, New Orleans, LA, 2002.

[18] D. Hong, M. Yuan, V.Y. Shen, Dynamic privacy management: a plug-in service for the middleware in pervasive computing, Proceedings of the 7th International Conference on Human Computer Interaction with Mobile Devices & Services, Salzburg, Austria, 2005, pp. 1–8.

[19] X. Jiang, J.I. Hong, J.A. Landay, Approximate information <sup>fl</sup>ows: socially-based modeling of privacy in ubiquitous computing, The Fourth International Confer ence on Ubiquitous Computing, Goteberg, Sweden, 2002.

[20] X. Jiang, J. Landay, Modeling privacy control in context-aware systems, IEEE Pervasive Computing 1 (3) (2002) 59–63.

[21] A. Josang, R. Ismail, C. Boyd, A survey of trust and reputation systems for online service provision, Decision Support Systems 43 (2) (2007) 618–644.

[22] D.N. Jutla, P. Bodorik, Y.J. Zhang, PeCAN: an architecture for users' privacy-aware electronic commerce contexts on the semantic web, Information Systems 31 (4–5) (2006) 295–320.

[23] D.S. Kamvar, M.T. Schlosser, H. Garcia-Molina, The eigen trust algorithm for reputation management in P2P networks, Twelfth International World Wide Web Conference, Budapest, Hungary, 2003.

[24] D.J. Kim, D.L. Ferrin, H.R. Rao, A trust-based consumer decision-making model in electronic commerce: the role of trust, perceived risk, and their antecedents, Decision Support Systems 44 (2) (2008) 544–564.

[25] O. Kwon, N. Sadeh, Applying case-based reasoning and multi-agent intelligent system to context-aware comparative shopping, Decision Support Systems 37 (2) (2004) 199–213.

[26] O. Kwon, The potential roles of context-aware computing technology in optimization-based intelligent decision-making. Expert Systems with Applica: tions 31 (3) (2005) 629–642.

[27] O. Kwon, Multi-agent system approach to context-aware coordinated web services under general market mechanism, Decision Support Systems 41 (2) (2006) 380–399.

[28] S. Lahlou, F. Jegou, European disappearing computer privacy design guidelines V1.0. Ambient Agoras, Report D15.4, Disappearing Computer Initiative, Oct. 2003.

[29] S. Lahlou, M. Langheinrich, C. Rocker, Privacy and trust issues with invisible computers, Communications of the ACM 48 (3) (2005) 59–60.

[30] M. Langheinrich, Privacy by design—principles of privacy-aware ubiquitous systems, Proceedings of the Ubicomp 2001, Atlanta, GA, 2001, pp. 273–291.

[31] M. Langheinrich, A privacy awareness system for ubiquitous computing environments, Proceedings of the Ubicomp2002, 2002, pp. 237–245.

[32] A.P. Meyer, Privacy-aware mobile agent: protecting privacy in open systems by modelling social behaviour of software agents, ESAW 2003, London, UK, 2003, pp. 123–135.

[33] G.R. Milne, M.E. Gordon, Direct mail privacy-ef<sup>fi</sup>ciency trade-offs within an implied social-contract framework, Journal of Public Policy & Marketing 12 (2) (1993) 206–215.

[34] C. Neustaedter, S. Greenberg, The design of a context-aware home media space for balancing privacy and awareness, Lecture Notes in Computer Science 2864 (2003) 297–314.

[35] P. Persiano, I. Visconti, An anonymous credential system and a privacy-aware PKI, Lecture Notes in Computer Science 2727/2003, 2003, pp. 27–38.

[36] B. Price, K. Adam, B. Nuseibeh, Keeping ubiquitous computing to yourself: a practical model for user control of privacy, International Journal of Human Computer Studies 63 (1–2) (2005) 228–253.

[37] X. Qu, X. Yang, Y. Tang, H. Zhou, A behavior characteristics-based reputation evaluation method for grid entities, Lecture Notes in Computer Science 3470 (2005) 567–577.

[38] D. Redell, Information Technology and the privacy of the individual, Daft ACM Whitepaper on Computer and Privacy, September, 1992.

[39] P. Resnick, R. Zeckhauser, E. Friedman, K. Kuwabara, Reputation systems, Communications of the ACM 43 (12) (2000) 45–48

[40] D. Saha, A. Mukherjee, Pervasive computing: a paradigm for the 21st century, IEEE Computer 36 (3) (2003) 25–31.

[41] H. Simon, Bounded rationality and organizational learning, Organization Science 2 (1) (1991) 125–134.

[42] H.J. Smith, S.J. Milburg, S.J. Burke, Information privacy: measuring individuals concerns about organizational practices, MIS Quarterly 20 (2) (1996) 167–196.

[43] L. Sweeney, Privacy-preserving surveillance using databases from daily life, IEEE Intelligent Systems 20 (5) (2000) 83.

[44] K. Tang, Y.L. Chen, H.W. Hu, Context-based market basket analysis in a multiplestore environment, Decision Support Systems 45 (1) (2008) 150–163.

[45] The Feedback Forum, eBay.http://pages.ebay.com/services/forum/feedback.html

[46] K. Valck, G.H. van Bruggen, B. Wierenga, Virtual communities: a marketing perspective, Decision Support Systems 47 (3) (2009) 185–203.

[47] W3C, http://www.w3.org/TandS/QL/QL98/pp/APPEL-QLW.html, 1998.

[48] H. Wang, M.K.O. Lee, C. Wang, Consumer privacy concerns about Internet marketing, Communications of the ACM 41 (3) (1988) 63–70.

[49] M. Weiser, Some computer science issues in ubiquitous computing, Communica tions of the ACM 36 (7) (1993) 75–84

[50] J. Yen, R. Popp, G. Cybenko, K.A. Taipale, L. Sweeny, P. Rosenzweig, Homeland security, IEEE Intelligent Systems 20 (5) (2005) 76–86.

![](/api/attachments/KPUBXA6B/fulltext/images/63796e190296cb18035afd5e2060a448a2e78049b826e1f10f8417bcede293a9.jpg)

Dr. Ohbyung Kwon is presently a professor at the School of Management, Kyung Hee University, South Korea, where he initially joined in 2004. In 2002, he worked at the Institute of Software Research International (ISRI) at Carnegie Mellon University. He received MS and PhD degrees at KAIST in 1990 and 1995, respectively. He is now an adjunct professor at San Diego State University (SDSU). His current research interests include context-aware services, case-based reasoning and DSS. He has presented various papers in leading information system journals including Decision Support Systems, Simulation, International Journal of Computer Integrated Manufacturing, and Behavior and Information Technology.
