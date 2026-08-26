---
otero_id: 3294
otero_key: "EKYYG6VQ"
title: "Capturing the “Social” in Social Networks: The Conceptualization and Empirical Application of Relational Quality"
authors: "Christian Meske; Iris Junglas; Matthias Trier; Johannes Schneider; Roope Jaakonmäki; Jan vom Brocke"
year: "2025"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00926"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
2025

# Capturing the “Social” in Social Networks: The Conceptualization and Empirical Application of Relational Quality

Christian Meske , christian.meske@rub.de

Iris Junglas , junglasia@cofc.edu

Matthias Trier , trier@uni-paderborn.de

Johannes Schneider , johannes.schneider@uni.l

Roope Jaakonmäki , roope.jaakonmaeki@hilti.com

See next page for additional authors

Follow this and additional works at: https://aisel.aisnet.org/jais

## Recommended Citation

Meske, Christian; Junglas, Iris; Trier, Matthias; Schneider, Johannes; Jaakonmäki, Roope; and vom Brocke, Jan (2025) "Capturing the “Social” in Social Networks: The Conceptualization and Empirical Application of Relational Quality," , 26(4), 1009-1041. DOI: 10.17705/1jais.00926 Available at: https://aisel.aisnet.org/jais/vol26/iss4/6

This material is brought to you by the AIS Journals at AIS Electronic Library (AISeL). It has been accepted for inclusion in Journal of the Association for Information Systems by an authorized administrator of AIS Electronic Library (AISeL). For more information, please contact elibrary@aisnet.org.

Capturing the “Social” in Social Networks: The Conceptualization and Empirical Application of Relational Quality

Authors Christian Meske, Iris Junglas, Matthias Trier, Johannes Schneider, Roope Jaakonmäki, and Jan vom Brocke

ISSN 1536-9323

# Capturing the “Social” in Social Networks: The Conceptualization and Empirical Application of Relational Quality

Christian Meske,<sup>1</sup> Iris Junglas,<sup>2</sup> Matthias Trier,<sup>3</sup> Johannes Schneider,<sup>4</sup>Roope Jaakonmäki,<sup>5</sup> Jan vom Brocke<sup>6</sup>

<sup>1</sup>Ruhr University Bochum, Germany, christian.meske@rub.de

<sup>2</sup>College of Charleston, USA, junglasia@cofc.edu

<sup>3</sup>Paderborn University, Germany, trier@uni-paderborn.de

<sup>4</sup>University of Liechtenstein, Liechtenstein, johannes.schneider@uni.li

<sup>5</sup>Hilti Group, Liechtenstein, roope.jaakonmaeki@hilti.com

<sup>6</sup>University of Muenster, Germany / University of Liechtenstein, Liechtenstein, jan.vom.brocke@uni-muenster.de

## Abstract

Social networks are omnipresent in both our private and professional lives. As social beings, we thrive on technology’s ability to allow us to be social. But just because online social networks have been designed for “being social” as their name suggests, it does not mean they are actually supportive and representative of the rich social interchanges that take place when individuals communicate in a physical setting. Grounded in relational social capital and relational sociology, we examine the aspect of relational quality—a concept that has been neglected thus far in the bigger picture of social networks. Relational quality describes the richness of the relationship that develops between individuals through social interactions. Since current approaches to social networks mostly focus on structural and cognitive properties, our aim is to derive four theoretically motivated markers for relational quality, comprising markers for being personal, being curious, being respectful, and sharing with others, that—conceptually as well as methodologically—complement existing social network measures. By analyzing more than 440,000 messages posted by more than 24,000 employees across two enterprise social networks (ESN), we illustrate and validate the existence of relational quality in social networks, using sample measures for each marker. We further uncover important relationships between different forms of structural embeddedness and our dimensions of relational quality in online networks.

Keywords: Enterprise Social Network, ESN, Social Capital, Relational Quality, Social Network Analysis, Linguistic Analysis, Computational Research

Sam Rudha and Dorothy E. Leidner were the accepting senior editors. This research article was submitted on September 28, 2021, and underwent three revisions

## 1 Introduction

Human beings communicate and collaborate in different ways and in various contexts to achieve individual or common goals (Abhari et al., 2022; Schoch et al., 2023). The very basis of such practices is social interactions among humans. The quality of such social interactions is seen as an important basis for how people feel and how they behave in the offline world as well as the virtual realm (Wong et al., 2021; Zhang et al., 2022). In the workplace, where enterprise social networks, or ESNs, have made rapid inroads, social interactions have been deemed an important driver for a wide range of benefits— not least, because they translate into positive outcomes at the organizational level (Oh et al., 2004; Sias, 2005; Gallup, 2015; Moqbel & Nah, 2017). Moreover, social interactions have been viewed as an important stepping stone for accumulating social capital (Nahapiet & Ghoshal, 1998), with social capital constituting an individual’s “aggregation of resources linked to the existence of a durable network of relationships” (Bourdieu, 1983, p. 248). Social capital has also been shown to be a significant antecedent for knowledge exchanges, trust, and innovativeness inside the organization (Bartelt et al., 2020).

However, while the quality of social interactions, and hence social capital, has a tremendous impact on important variables, like behaviors in the private as well as professional realm, the nature of it is not entirely understood. Studies have distinguished between three different perspectives of social capital (Nahapiet & Ghoshal, 1998), yet only two—namely structural and cognitive—have achieved much attention. The third one, relational, which taps into the quality and richness of social interactions, is still underresearched in information systems (IS), which is surprising given that social interactions increasingly take place digitally inside and outside of organizations (e.g., Eurostat, 2019; Schuetz et al., 2021; Schoch et al., 2023).

The structural perspective zooms in on the relative position of an actor in a network structure; it examines how the configuration of linkages, particularly the central positioning of an actor within a network, results in benefits for the individual (e.g., Burt, 1995). The cognitive perspective predominantly looks at the intellectual benefits that individuals derive from being part of a network. Studies in this domain zoom in on topic-related aspects, e.g., how shared terms, language, codes, or narratives lead to increased learning potentials (Cornelissen, 2016) or collaborative innovations (Wang et al., 2015).

The third perspective, relational, based on Granovetter’s (1992) notion of relational embeddedness, zooms in on the quality of interactions and the social nature of relationships between networked actors. Put differently, the relational perspective of social capital theory focuses on the quality of personal relationships, developed between individuals through a history of social interactions, and includes—but is not limited to—facets of trustworthiness, overlapping identities, and feelings of mutual closeness and solidarity (Nahapiet & Ghoshal, 1998). Studies in the organizational realm have looked at the quality and trustworthiness of workplace relationships (Oh et al., 2004), the quality of interactions within groups and their effect on the workforce’s productivity (Cornelissen, 2016), as well as on employee well-being, satisfaction levels (Sias, 2005), and performance (Moran, 2005). In contrast, IS studies that take a relational perspective with respect to digital social interactions in enterprises are scarce. One study, for example, has looked at how relationships develop among a set of employees using instant messaging (Cho et al., 2005).

The paucity of studies scrutinizing the relational quality of social interactions is somewhat explainable by the limitations of the methodological toolset that is typically applied as part of a social network analysis (SNA) in the field of IS research. By default, SNA favors the structural perspective by quantifying aspects, such as the number of online connections (Howison et al., 2011), connection strengths (Onnela et al., 2007), or the centrality of actors (e.g., Khansa et al., 2015; Hong et al., 2018; van Osch & Steinfield, 2018). The relational perspective, in contrast, is the least quantifiable of the three, as it requires delving into the quality and value of a relationship between two individuals. The imbalance between social capital theory, which calls for a harmonized mix between all three perspectives, and the analytical method, which exists to measure them, has caused increasing criticism. For instance, scholars have argued that the simple structural measures adopted in extant research do not appropriately depict the actual phenomenon of digital social networking at all (e.g., Howison et al., 2011; Trier & Richter, 2015). Even studies in sociology have noted that too much attention is paid to quantitative methods at the expense of conceptual considerations (Crossley, 2010).

What is needed, apart from a conceptual understanding, is a more nuanced and operational understanding of the relational perspective, which is easily quantifiable. At the same time, we also need a holistic methodological approach that captures all three interdependent social capital perspectives in a more balanced way. With better integration, the focus on individual behaviors, which is symptomatic of the relational perspective, may help to contextualize and explain structural as well as cognitive patterns of social networking and thus contribute to a strand of research that investigates how, for example, relationship strength interacts with structural properties (e.g., Tortoriello et al., 2012; Moser et al., 2013).

At the conceptual level and viewed from an IS perspective, understanding the core characteristics of social interactions, and hence of social capital, is not only important for improving, for instance, the design of communication and collaboration systems but also for predicting and managing individual behaviors within the organization. In addition, developing instruments to analyze and make sense of data, drawn from systems like social networks, is at the core of the IS discipline (Kane et al., 2014; van Osch & Steinfield, 2016; Bulgurcu et al., 2018; Shangguan et al., 2022). A more precise conceptualization of social interactions and social capital is therefore a prerequisite to extend the analytical toolset in this regard, which in turn helps to better describe and interpret individual behaviors in digital enterprise social networks.

Overall, we pursue the following two research questions:

RQ1: How can we conceptualize, operationalize, and validate relational quality as a new and third dimension that augments social network analysis?

RQ2: How can relational quality help to better identify, differentiate, and understand roles that emerge as part of social online interactions?

By answering these questions, we do not aim to extend the theory of social capital itself. Rather, we first uncover that social capital theory encapsulates three different perspectives, of which only two (structural, cognitive) have been the focus of IS research while the third (relational) is hardly used despite available data and analytical methods. Second, we draw on existing theories to enlarge the conceptualization of relational quality with four theoretically motivated markers (i.e., being personal, being curious, being respectful, and sharing). Based on these markers, researchers are able to systematically capture the relational quality of relationships in digital social networks. Integrating the relational perspective, so we argue, may help IS researchers contextualize and explain both structural as well as cognitive patterns better. Third, with an extension of the analytical toolbox that is grounded in relational social capital as well as relational sociology, we provide a first set of four theoretically motivated measures that offer a point of departure and guidance for quantifying relational quality. While further and more complex analytical methods may be applicable to measure our theorized dimensions, our measurement approach is intentionally simple in nature, easy to capture and execute, suitable for analysis that complies with corporate security requirements, and applicable to a wide range of social networks. We hope that by focusing on the careful theoretical development of the facets of relational quality, we can provide future researchers a platform to develop and apply further, and perhaps more advanced, methods. In that sense, our study provides a practical approach for IS researchers and organizations to use immediately to gain a solid understanding of relationships in enterprise social networks beyond the question of who is connected with whom.

The remainder of this article is organized as follows: We first look at studies of digital social relationships and introduce the social capital perspective as a theoretical background to conceptualize a systematic investigation of the relational dimension. Grounded in social capital theory, the relational sociology of Crossley (2011), and linguistic studies, we then derive four facets of relational quality, which we evolve into a simple measurement approach, thus extending SNA. We then assess the contribution of the new analytical lens using more than 440,000 messages posted by more than 24,000 employees across two enterprise social networks and discuss important insights on the interplay of relational quality and structural positions of employees in digital social networks.

## 2 Conceptual Backdrop: Relational Quality of Interactions

Given the likely prospect of positive organizational outcomes of social interactions (Oh et al., 2004; Sias, 2005; Gallup, 2015; Moqbel & Nah, 2017), it is not surprising that IS scholars—facing more and more digital social interaction—have investigated the various social capital dimensions of digital interaction and confirmed their importance in the workplace (Steinfield et al., 2009). Yet some IS studies suggest only a limited role of social relationship formation in organizational online contexts. For example, one study found that structural and relational aspects are mostly evident in face-to-face settings, whereas online settings are more limited and predominantly support cognitive aspects (van den Hooff et al., 2010). While some studies attribute this emphasis to the importance of instrumental information transfer (Yoo & Kanawattanachai, 2001; Robert et al., 2008; Trier & Richter, 2015), the inconsistent results between social relationship development and strategic information transfer might simply imply that current explanations of digital social interaction are not comprehensive enough.

The few IS studies that exist with an explicit focus on the relational dimension of online social networking highlight some contingencies in this debate. Analyzing the meaning that actors attribute to their digital relationships qualitatively, for example, revealed “two interacting actor roles,” each with different motivations that are dependent on the actors’ direct organizational requirements (Trier & Richter, 2015). Similarly, a mixedmethod study that looked at the development of rich working relationships and their related evolving egonetworks via online media discovered “complex underlying motivations” for engaging in networking (Cho et al., 2005). While taken together, those qualitative explorations revealed different roles and a complex relationship formation process with an unfolding change of meaning as part of the relational dimension; however, these studies do not link the qualitative statements of respondents to the larger network structure and thus lack the scalability to explain complete networks and their structures (Crossley, 2010).

Another research stream that zooms in on the relational dimension examines the role of online sociability (Preece, 2001; Bouman et al., 2007) and social climate (cf. Gao et al., 2010). While sociability captures how actors relate to one another, organize their social practices, and construe their social identities (Bouman et al., 2007), social climate solely constitutes an influencing factor on sociability that reflects a comfortable social atmosphere with open affective communication and small psychological distance (Gao et al., 2010). In this context, the concept of sociability has primarily been captured as the result of interacting with a (sociable) technological platform—and not through assessing the nature of the relationship that emerges between individuals (e.g., Bouman et al., 2007;

Gao et al., 2010; Junglas et al., 2013). Further, sociability has mostly been used as a manipulation variable (e.g., low versus high) or has been captured as a subjective variable (e.g., Kügler et al., 2015; Matook et al., 2015) but not as an objectively measured value.

Driven, perhaps, by methodological constraints, existing IS research has paid little attention to examining the quality of relationships, or the richness that is embedded in social interactions. For example, quantitative studies looking at the antecedents of sociability, such as Gao et al. (2010), may underestimate the heterogeneity of digital social networks. This important challenge for quantitative studies has only recently been criticized (Özbölük & Dursun, 2017; Bhattacharyya et al., 2020).

The increasing dominance of studies with a simplified structural or cognitive focus, along with the need for a richer understanding of social network relationships, is also a long-standing criticism raised by relational sociologists. They argue that such a focus is limited and reflective of a structuralist instrumentalist view where actors aim to maximize their utilization of the network (Emirbayer & Goodwin, 1994; Crossley 2011; Bolíbar, 2016). In fact, an “overabstracted” view (Crossley, 2010) of social interactions fails to account for any (emotional) emphatic bonds, neglects reciprocity (Takahashi, 2000), and overlooks mutual expectations. It also ignores any cultural values that mark the relational dimension in networks, even though an individual’s urge to be social is central to their being (Simmel & Hughes, 1949; Berry, 1995) and expresses itself in the profound processes of forming friendships, achieving personal recognition among our friends and peers, and receiving a feeling of support.

Even though the more recent organizational literature stresses the importance of positive social interactions (e.g., Moqbel & Nah, 2017; Sias, 2005) and relationship qualities for knowledge exchanges (Tortoriello et al., 2012), the interplay of social capital aspects—in particular, the role of rich and harmonious social interactions that we term as “the relational dimension” of social capital—has not yet been conceptualized and sufficiently examined in IS research. What is needed is an integrative perspective that captures digital relational quality and is also generic in its methodological approach to seamlessly integrate with existing measurements (cf. Crossley, 2010, p. 1). Such a perspective can then be used to study the interdependencies between the relational and the structural dimensions of social networking—for example, to explain differences in individual behaviors, such as using long socializing versus short advising interaction (Moser et al., 2013), and the implications for structural embeddedness. Structural embeddedness, in our context, refers to the position of an entity within a network and its connectivity to other entities (cf. Moody & White, 2003)

We now derive key facets and a measurement approach for relational quality before we take initial steps to examine the interdependencies between relational and structural network dimensions.

## 3 Deriving the Facets of Relational Quality

In order to develop a theoretically grounded methodological approach for capturing relational quality, we need to delve deeper into relevant aspects of social capital theory and the related principles and concepts of relational sociology.

As already noted, the relational dimension of social capital (Nahapiet & Ghoshal, 1998) is an important yet underrepresented aspect of social interaction that addresses the notion of relationship quality (Moran, 2005). The relevance of this factor was noted by Moran (2005), who found that while structural embeddedness determines the extent and range of resources that are within an individual’s reach, relational quality establishes how much of this potential will be realized. Put differently, although actors may have access to potential resources via their network structure, it is the quality of their relationships that influences whom they approach (Moran, 2005). Relational quality, according to Moran (2005), entails the sense of a contact’s personal closeness, mutual regard, reliability of the resource exchange, and the interpersonal trust that this reliability invokes. This list of properties already indicates that a simple measurement of interaction frequency—also known as “relationship strength” and found in most structural network analyses—is not sufficient to adequately capture relationship quality. A study, outlining further requirements for relationship quality, mentions the need to create opportunities for mutual self-exposure and selection by others in order to build similarity, shared interests, and to receive mutual validation of actors’ identities (Mesch & Talmud, 2006). Another important aspect of relationship quality, as identified by the literature, is that of multiplexity—a relationship should give rise to multiple dimensions of relating (including multiple forms of interacting) and multiple topics to discuss (Mesch & Talmud, 2006).

Beyond these individual aspects, relational sociology offers an even more comprehensive theoretical foundation for our conceptualization of relationship quality in networks. Relational sociology views interpersonal relations as constituents of the social world (Emirbayer, 1997). This view grew out of mounting criticism about the dominance of observing societies and situations as given factors where actors are determined by their psychological states. We draw on the works of Crossley (2010, 2011) as a relevant contributor to the European discourse on relational sociology with a keen interest in extending and improving SNA.

Crossley (2011) understands a network, in line with symbolic interactionism (e.g., Blumer, 1986), as something richer than the mere network structure that conventional SNA uses as a model—namely as a constructed “social world” (p. 5). Specifically, Crossley (2011) argues for adding the relevant symbolic, affective, normative, and resource exchange dimensions of social relationships (discussed in detail in the next section) to extend SNA and enable a richer and more accurate understanding of the richness of interactions (Crossley, 2010). To illustrate the potential corrective impact of such an extension, Crossley provides illustrative case examples where conflicting norms between social groups as well as their strategic interest in creating boundaries in a network around loyal clusters lead to situations in which centrality is no longer considered beneficial—contrary to what structural network theory would suggest. Relationship quality can therefore be defined as the richness and depth of social interactions between actors in a network that are based on personal closeness through mutual positive regard and affect, trustful responsiveness, and norm-respecting interactivity, as well as a diverse sharing of resources.

In order to substantiate the various aspects of relational quality, we relied on studies in linguistics (e.g., Danescu-Niculescu-Mizil et al., 2013; Lin & Qiu, 2013), along with literature on discourse analysis (e.g., Fairclough, 1992; Burr, 2015). These studies suggest that relational quality, as a construct, can be inferred from markers embedded in the language of a conversation (e.g., Golbeck et al., 2011). Specifically, conversations that demonstrate high levels of relational quality are determined by the following linguistic markers: (1) that the conversation between individuals is about something personal that relates to both parties in some sense, (2) that the participating individuals are curious about their respective communication partner, (3) that the conversation is carried out in a respectful manner and exhibits a certain level of decorum, and (4) that individuals are willing to share stories, insights, and experiences with others in conversations.

In the following, we build on our initial definition and link the noted linguistic markers with Crossley’s dimensions of networking in order to systematically develop four key facets of relational quality, which we then use to extend SNA with a systematic and grounded measurement approach.

## 3.1 Being Personal

Being personal captures the notion that an individual is socially aware of another individual or group of individuals and that the individual is able to relate to the other person(s) (Norrick, 1994). Relational sociologists argue that personal interactions are not restricted to economic considerations, as proposed by game theory for example, or to exert power (Crossley, 2011); rather, being personal carries relevant social advantages. In fact, “social conditions can channel strategic interaction in cooperative and pro-social directions” (p. 47) and result in a (strategic) networking advantage that is characterized by repeated interactions among individuals with shared contacts and no apparent conflict of interest—as often is the case in organizational digital interactions.

Crossley’s (2011) relational sociology perspective further emphasizes that building personal relationships “might involve successive increases in personal disclosure” (p. 35). The notion of successive disclosures also ties in with social penetration theory, which suggests that people only reveal superficial and nonintimate information about themselves at the beginning of a relationship and only gradually disclose personal aspects as the relationship progresses (Altman et al., 1981). Disclosures not only grant access to the private feelings of the individual (Rosenfeld, 2000) but are also reciprocal in nature— individuals disclose information about themselves and, in return, receive disclosed information, also referred to as a “dyadic effect” (Jourard, 1971).

Research has also shown that the more intimate a dyadic relationship is, the more likely the relationship is to use a conversational style of communication (Hornstein, 1985). In other words, in an intimate relationship, people use more informal opening statements (Hornstein, 1985), raise more topics in general, are more responsive to one another, and use more complex forms of closing statements. Studies have also shown that individuals in informal social settings predominantly tend to talk about themselves, their personal experiences, and other people within their social group (Dunbar et al., 1997). Being personal is therefore reflected in the extent to which a message is tailored to the relationship (Knobloch, 2003) and balances between stories about oneself and oneself as part of a group.

## 3.2 Being Curious

Being curious captures the notion that individuals are inquisitive and ask questions about other individuals. In organizational settings, being curious is a vital element in the process of establishing sets of shared rules and testing out those rules. Specifically, repeated interactions among individuals slowly institutionalize norms that eventually act as rules (Crossley, 2011, p. 52). These rules are not merely restrictive but also enable behaviors that would otherwise not be possible. Establishing and, more importantly, living those rules requires a certain degree of trust, taking others’ situations and interests into account, and an interest in the continued success of others. This, in turn, gives rise to empathy and the affective responses of feeling joy when others experience positive situations (p. 68)— addressing the affective dimension of social networking in Crossley’s relational sociology. In that sense, trust can be viewed as a long-term reward for reacting strategically in a way that complies with existing norms.

According to Crossley (2011), taking someone else’s perspective requires an awareness of the other person’s situation and a certain degree of identification with that person. “Empathiz(ing) with others by imaginatively enacting their role in a story” (p. 69) is an important element of an evolving relationship. Imaginatively enacting another person’s role entails talking with and about others and asking each other questions. Being able to take the perspective of others, or the community, also creates a perception of duty (judging one’s own behaviors from the community perspective) (p. 62), reinforcing the importance of norms and trust and thus giving rise to the principle of reciprocity.

In written conversations, being curious can often be witnessed in an action-reaction type sequence that keeps a conversation afloat. More information is being exchanged, and the range of questions broadens. Individuals look for opportunities to gather facts, learn, solicit ideas (Litman & Spielberger, 2003), and express actions reflecting care and concern about the other person’s well-being (Fredriksson & Eriksson, 2003).

Researchers have developed different measures that address aspects of curiosity. For example, interpersonal curiosity captures, among other things, the level of curiosity about the emotions of others, which includes verbal as well as nonverbal signs. It also captures the level of prying, which includes asking about the private lives of others and a desire to view others’ lives from the perspective of an invisible spy. Further, it addresses the level of snooping, which includes wondering about others’ interests, what they do, and how they live (Litman & Pezzo, 2007). Social curiosity, in contrast, captures the extent to which an individual is interested in learning more about the thoughts, feelings, and habits of others (also referred to as general social curiosity); it also captures the extent to which an individual likes to listen to other people’s conversations (Renner, 2006). In conversations, both constructs become apparent in two ways: the extent to which an individual asks questions about the other person and the extent to which individuals address other people using pronouns (like “you”).

## 3.3 Being Polite

Being polite captures the notion of individuals being respectful to one another. For example, using the right cues can keep the conversation on a positive track and avoid developing animosity or upsetting the conversational counterpart (Danescu-Niculescu-Mizil et al., 2013). Relational sociologists explain the importance of politeness by emphasizing two interactors’ attempts to establish control over their social relationship in terms of framing a mutual understanding of their identity, situation, and interaction. This, according to White (1992) and Crossley (2011), involves orientation towards norms and symbolic interactions, motivating Crossley’s normative and symbolic dimensions of social networking. Regarding social norms, politeness can be viewed as a positive evaluation of behaviors that are in accordance with an accepted norm. The mutual process of framing a story of cooperation through symbolic interactions relies on using politeness to express and frame a positive and trustful relational experience.

From a conversational perspective, politeness is observed in the “rational” usage of language in order to minimize conflict, disagreement, or antipathy and to promote accord instead. It can also be viewed as the adherence to conversational contracts that are formally defined through institutions, or informally through previous encounters with individuals or groups (Fraser, 1990).

Politeness also always has a social objective. Interestingly, there is a strong inverse relationship between politeness and dominance. Individuals who are expressively polite are considered the least dominant; they are also found to be more transparent in their messaging and lines of arguments (Dillard et al., 1997).

Further, being polite also includes expressions of optimism with the objective of making conversational counterparts feel good about themselves (Brown & Levinson, 1987)—being polite thus also resonates with the affective dimension of social networking (Crossley, 2011). We hence argue that a positive tone, reflected in the words we exchange, is expressive of higher levels of politeness. Being polite might therefore be reflected in the extent to which an individual uses polite word expressions and positive sentiment in their expressions.

## 3.4 Resource Sharing

Sharing is considered a prosocial act (Bucher et al., 2016) that not only instigates bonding experiences between individuals but also fosters existing ones. Sharing can be viewed analogous to the idea of “gift giving,” a processual chain of reciprocities (Sherry, 1983), where an individual is motivated to spend time and effort selecting a gift that is specific to the recipient.

While sharing might be driven by hedonic motives (i.e., sharing happens for the sake of sharing only, and individuals experience inherent pleasure from doing so) or by utilitarian motives (i.e., there is a means to an end or a goal that might be achievable via the venue of reciprocity) (Bucher et al., 2016), relational sociologists have highlighted the importance of exchanges, irrespective of their motives. In fact, they have suggested adding a resource exchange dimension to any network analysis (Crossley, 2011). Social interaction relates to “networks of resource mobilization. Actors pursue and exchange resources and goods in social worlds, sometimes deploying them in pursuit of other, further goods” (Crossley, 2011, p. 138).

In an online conversation, sharing goes beyond the exchange of mere words—it makes use of the digital form of gift-giving, for example, through sharing a link or a document that is relevant to the content of a conversation. By sharing, online individuals build relationality, i.e., life experiences with others (Baker et al., 2005). For sharing to occur, three elements have to be in place: (1) Patterns of interaction have to exist that give rise to gifting partners’ self-identification. (2) There must be a set of norms and obligations that provides the foundation for sharing (normative dimension). (3) Sharing requires an environment where rule-governed activities have symbolism or are part of a ritual (Giesler, 2006) (cf. Crossley’s symbolic dimension). In a work environment, sharing is typically a sign that individuals are going beyond the formal requirements of their jobs. Sharing allows them to help other colleagues in their job while ensuring that the work community, as a whole, is in good shape and able to succeed (Goffee & Jones, 1996). Again, it involves a mutual process of framing a story of cooperation through symbolic interaction.

## 4 Operationalizing Relational Quality by Extending Existing Structural Social Network Measures

In order to operationalize relational quality as a new dimension, we need to be mindful of existing SNA measurement approaches. Traditional SNA mostly measures structural elements, such as how many connections an individual has in a network (often referred to as connectivity or connectedness) or how often an individual interacts with others in the network (often referred to as activity). These measures are more focused on the typology of the network (in a mathematical sense) and pay little attention to the quality of social exchanges that take place in the network (which is the object of our study).

Operationalizing relational quality therefore should not only be considerate of these existing measurements but should also be inclusive. In fact, any operationalization of relational quality and its four facets of being personal, being curious, being respectful, and sharing, should be embedded into the traditional measures that capture structural elements. Only then can we gauge the quality of those measures as part of two enterprise social networks in more detail and uncover aspects that were impossible to unearth with traditional SNA.

It is easy to see that a qualitative approach to generate a proper measurement will “lack the means to identify structure” (Crossley, 2010, p. 2) and will thus fail to scale well to large networks of several thousand individuals. As pointed out above, a quantitative structural SNA, on the other hand, is “too abstract… and insufficiently attentive to inter-agency” (Crossley, 2010, p. 2), i.e., it is insufficient to capture the richness of the interaction taking place. Consequently, network analysis scholars have emphasized the added value of combining qualitative methods with traditional standardized measures (Crossley, 2010; Bellotti, 2016) and, by doing so, avoiding SNA’s current overabstraction and instead gaining the ability to better capture the complexity of interpersonal digital relationships (e.g., Trier & Richter, 2015).

In the following, we propose a measurement approach that can serve as a starting point for future researchers to augment traditional SNA measures with relational quality markers that mirror Crossley’s ideas. Our intention is primarily to validate the existence of relational quality at the conceptual level and to provide a practical and easily implementable way for organizations to extrude patterns about their users’ online behaviors. Therefore, our proposed approach presents an initial foray to stimulate a novel strand of network analytical measures that targets the quality of relationships in digital social networks.<sup>1</sup>

As a deviation from traditional structural measures, which are explained in detail in Appendix A and mostly comprise connectedness and activity levels of users in a network, we will heavily rely on linguistic markers to operationalize relational quality. For that, we take inspiration from past studies that have investigated the qualitative properties of unfolding conversations (e.g., online postings) to categorize user types. For example, one study instructed team players to use short and advising messages, storytellers to use long and socializing-oriented messages, and utility posters to share knowledge but not to socialize (Moser et al., 2013). Another study investigated the antecedents of being seen as a leader in online communities. It was found that, for example, thanking others, sharing technical expertise, and an individual’s structural social capital (e.g., as represented by betweenness centrality measures) were the main drivers for a leadership role in those networks (Faraj et al., 2015).

While such studies analyzing exchanged conversations appear promising, it is surprising “that so few social scientists have relied on word analyses to understand basic social processes.” (Pennebaker & Chung, 2014, p. 2). More recent studies in IS on textual analytics have showcased that this situation is changing (e.g., Zhou et al., 2018). We follow this development and borrow the idea of dictionary-based text analysis approaches for natural language, which have been used by researchers outside of IS, such as social psychology researchers (Tausczik & Pennebaker, 2010). These approaches provide a suitable basis for well-proven tools for augmenting SNA with a comprehensive measurement for each relational quality facet.

## 4.1 Measuring Being Personal

As alluded to earlier, being personal means relating to a person through conversational breadth and depth and finding the right balance between talking about oneself and creating commonalities in speech. Of the many approaches possible, a simple and very executable approach to measuring an individual’s tendency to “be personal” entails capturing the usage of personal pronouns in conversational exchanges. Personal pronouns can be considered to be language markers of social relationships and interactions (Kacewicz et al., 2014). Since they refer to human beings and function as a reference between the speaker and listener, they highlight, for example, whether the focus of attention is on self as a distinct entity (“I,” “me,” “mine”), on others (“he,” “she,” “they”), or emphasizes the belongingness to a specific group (“we,” “us,” “ours”) (Chung & Pennebaker, 2007).

In order to measure “being personal” we relied on measures of individualism and collectivism (e.g., Twenge et al., 2013; Pennebaker & Chung, 2014). Individualism is a “social pattern… [of] individuals who view themselves as independent of collectives; [those individuals] are primarily motivated by their own preferences [and] needs… and emphasize rational analyses of the advantages and disadvantages to associating with others” (Triandis, 1995, p. 2). In contrast, collectivism may be defined as a “social pattern… [of] individuals who see themselves as parts of one or more collectives (family, co-workers, tribe, nation); [those individuals] are primarily motivated by the norms of, and duties imposed by, those collectives… [and] are willing to give priority to the goals of these collectives over their own personal goals” (Triandis, 1995, p. 2). From a semantic perspective, individualism is reflected in the usage of the first-person singular pronouns “I,” “me,” and “my.” The usage of those pronouns suggests attention placed on the self as an independent and unique human being, emphasizing distinctiveness (e.g., Pennebaker & Lay, 2002; Twenge et al., 2013). Collectivism, on the other hand, can be identified by the first-person plural pronouns “we,” “us,” and “ours.” Researchers have shown that the use of the pronoun “we” is indicative of group identity (Sylwester & Purver, 2015) and group solidarity (Arguello et al., 2006) and invokes a sense of “community-creating” (Hong & Ho, 2005). People using “we” have also been found to be more connected in their relationships (Pennebaker & Lay, 2002). It is the shift between the usage of both pronouns that is of interest. For example, a study has shown that the usage of the “we” pronoun increases while the usage of the “I” pronoun decreases over time when groups establish themselves as an entity with its own identity. Even when group members are from different cultural backgrounds and only communicate online due to geographical distances, this shift is recognizable (Cassell & Tversky, 2006). The same effect can also be found when people are exposed to a collective trauma. In their study, (Pennebaker & Stone, 2003b) for example, showed that the pronoun “I” dropped by 12% in an online chat group while the pronoun “we” increased by 135% in the days after the death of Princess Diana.

Since “being personal” is about walking the fine line between sharing narratives about oneself and trying to create bonds with others, the usage of pronouns should also be balanced. Following prior studies that have measured individualism and collectivism using a dictionary-based approach, we applied the word lists suggested by the LIWC2015 personal pronoun categories authored by Pennebaker et al. (2015) and summated them.

## 4.2 Measuring Being Curious

Being curious means being inquisitive about other individuals. Being curious can be captured by the extent to which an individual asks questions—as the act of asking indicates curiosity and furthers the progression of conversation between people. It is also captured by the extent to which an individual refers to others and addresses them directly by using the pronoun “you.” Both often go hand in hand, as asking questions most likely entails addressing another person and making them the object of interest. Using the pronoun “you” in general is an indicator that a speaker is socially engaged as well as socially aware of another person’s state of mind (e.g., Pennebaker et al., 2003a). To an extent, it reflects the level of empathy that a person exhibits towards another person. Studies have shown that both activities “asking” and “informating” (or informing oneself) are considered to be one speech act, as they are inherently intertwined (Wish et al., 1980).

In order to measure “being curious,” we captured the proportion of messages that included at least one question mark (Gifford & Hine, 1994), as well as the extent to which an individual addresses another person directly by using the personal pronouns “you,” “your,” and derivatives thereof (Pennebaker et al., 2003a). In order to arrive at an overarching measure for the construct, both measures were summated.

## 4.3 Measuring Being Polite

Being polite is expressed through utterances of politeness (Grandin et al., 2005; Danescu-Niculescu-Mizil et al., 2013) along with appropriate positive sentiment. Being polite means choosing the right words to avoid animosity, keeping the tone of the conversation balanced, and avoiding deviating into extreme statements. In that sense, being polite also means including optimism in statements. Therefore, a simple approach to measuring “being polite” combines two complementary ways. First, we measured the usage of words that have a polite connotation, such as “please,” “apologize,” “kindly,” “thanks,” or “grateful,” for example. Since no validated lexicon exists, we relied on words collected by Miller and Rye (2012) and sources such as Danescu-Niculescu-Mizil et al. (2013) and counted their frequencies. <sup>2</sup> Second, we captured the tone of the conversation through sentiment analysis.

Sentiment analysis, as an instrument to capture the mood or attitudes hidden in a written text, has achieved widespread prominence (Stieglitz et al., 2018), particularly in the area of marketing, where the analysis of customer reviews has been the subject of numerous studies. For our purposes, we used a sentiment lexicon covering a list of about 6,800 positive and negative English words (Hu & Liu, 2004). Since sentiment can be either positive or negative, two sentiment scores were calculated: one score that only summated the occurrence of positive sentiment words, and one score that only summated the occurrence of negative sentiment words. For example, words such as “amazing” or “great” were classified as positive, whereas words such as “bad” or “terrible” were classified as negative sentiment words. Also, among the set of positive words, terms such as “amazing” had a higher sentiment score than the term “good.”

In order to arrive at an overarching sentiment score, we computed the difference between positive and negative sentiment scores and divided the difference by the total number of words authored by an individual. In a further step, we then added the number of polite words used in order to arrive at an overarching score for “being polite.”

## 4.4 Measuring Sharing

Sharing can be operationalized as an individual’s tendency to share documents and references. While sharing can take many forms, in the context of online communications, the act of giving is mostly captured by the number of external resources that an individual provides to someone else. More specifically, in order to capture sharing, we computed the number of messages that contained URLs and attachments and put them in relation to the overall number of messages that an individual authored. Both were indicative of the amount of effort that an individual placed on augmenting the conversation by including external sources of information.

## 5 A Comprehensive Measurement Approach for Relational Quality

Table 1 provides an overview of all measurements and their relation to our conceptualized four facets of relational quality. It further contains a summary of items used for the overarching measurement model.

Aggregated measures were calculated as the sum of the individual standardized measures. More specifically, in order to calculate the standardized measure for individualism, for example, we took the number of words that contained any of the 22 words (e.g., “I, I’m, I’ve, me, my,” etc.) for an individual. Let’s assume that out of 1,000 words of an individual’s message, 45 words indicate individualism (0.045). Let’s also assume that the mean usage for this set of words for the entire network is 0.04, i.e., a person on average uses 40 out of 1,000 words signifying individualism, and the corresponding standard deviation across the network is 0.25. In this case, the standardized measure for this individual’s individualism would be calculated as (0.045-0.04)/0.25 = 0.02, signaling how far the data point is from the network’s mean. The same method was applied to calculate measures of collectivism. In the last step, both measures were summed up to form the aggregated measure for “being personal.”

In addition to the newly formed measures for relational quality, we also incorporated two traditional structural measures—activity and connectivity—into the adopted measurement instrument. Adding the traditional structural measurement dimension enabled us to assess the interplay of multiple social capital dimensions, i.e., whether relational quality overlapped with structural properties and roles or to what extent it provided complementary value to the analysis or further differentiation of existing roles.

Activity measures are useful for capturing the frequency and amount with which individuals contribute to a group or network. The assumption is that someone who is posting a lot of messages would be considered “active.” Using the absolute number of sent messages, however, might be misleading, as someone might send 10 messages per day, whereas someone else may send 10 messages in three years. Therefore, to capture activity, we measured the frequency of activity (Correa et al., 2010) using the rate of sent messages within a certain time frame. Using a rate, i.e., messages per time, rather than absolute counts, allowed us to compare individuals that did not join the network at the same time.

Table 1. Our Adopted Measurement Approach

<table><tr><td>Dimension</td><td>Facet</td><td>Theoretical mechanism</td><td>Measure</td><td>Definition of measure</td><td>Definition of aggregated measures</td></tr><tr><td>Activity</td><td></td><td></td><td>Sent messages</td><td>Total number of messages sent by an individual over the last 365 days</td><td></td></tr><tr><td>Connectivity</td><td></td><td></td><td>Absolute degree centrality (= indegree + outdegree)</td><td>Total number of users that either sent messages to the individual or received messages from the individual</td><td></td></tr><tr><td rowspan="8">Relational quality</td><td rowspan="2">Being personal</td><td rowspan="2">Individualism &amp; collectivism; talking about oneself AND about commonalities (personal pronouns); expression of feelings</td><td>Individualism</td><td>Fraction of words that are first-person singular pronouns</td><td rowspan="2">The sum of the standardized fraction of messages containing first-person singular pronouns (22 words, e.g., “I, I’m, I’ve, me, my”) and first-person plural pronouns (12 words, e.g., “we, we’ve, let’s, us, ours”)</td></tr><tr><td>Collectivism</td><td>Fraction of words that are first-person plural pronouns</td></tr><tr><td rowspan="2">Being curious</td><td rowspan="2">Asking questions in order to learn about others improves empathy; inquiring about others’ emotions</td><td>Asking questions</td><td>Fraction of messages that contain at least one question mark</td><td rowspan="2">The sum of standardized fraction of messages containing a question mark and standardized fraction of those containing second-person singular or plural pronouns (24 words, e.g., “you, you’d, you’ve, your, yourself”)</td></tr><tr><td>Addressing another person directly</td><td>Fraction of words that are second-person singular and plural pronouns</td></tr><tr><td rowspan="2">Being polite</td><td>Positivity (friendliness)</td><td>Sentiment</td><td>Difference between positive and negative words, divided by the total number of words</td><td rowspan="2">The sum of the standardized sentiment score and the standardized fraction of messages containing polite words (6779 words conveying sentiment, e.g., “great, happy, awesome, issue, problem”; 25 words conveying politeness, e.g., “please, thanks, thx, sorry, appreciate”)</td></tr><tr><td>use of polite words, minimizing conflict and disagreement, promoting accord</td><td>Politeness</td><td>Fraction of words that are polite words</td></tr><tr><td rowspan="2">Resource Sharing</td><td rowspan="2">Sharing as gift giving and reciprocation to build relationships; going beyond the minimal requirements</td><td>Reference sharing</td><td>Fraction of messages that contain at least one URL reference</td><td rowspan="2">The sum of the standardized fraction of messages containing URLs and the standardized fraction of messages including attachment(s)</td></tr><tr><td>Document sharing</td><td>Fraction of messages that contain at least one attachment</td></tr></table>

Connectivity measures capture an individual’s standing within the network. A variety of metrics have been used, including, for example, capturing an individual’s position via measures of eigenvector centrality or closeness centrality (Faust, 1997), computing an individual’s status as a binding element for subgroups via measures of betweenness centrality (Newman, 2005), and calculating an individual’ number of communication partners via degree centrality (Faust, 1997). While all of these measures are conceptually related (Valente et al., 2008), we decided to compute the absolute degree centrality that corresponded to the number of different direct communication partners (Scott, 1988). We considered this measure to be more appropriate than other network measures, as our study aimed to capture an individual’s tendency to communicate with many different partners. According to our conceptual understanding, a person with more connections would be seen as more social and more open to talking with different people—as opposed to someone who seeks the company of a single user only (e.g., their spouse or best friend). It should be noted, however, that there is a natural correlation between absolute degree centrality and an individual’s messaging activity level. An individual sending just one message to one communication partner at a time will always increase his/her degree centrality by 1 if that person is a new person. On the other hand, an individual sending many messages to their established set of communication partners will not increase their degree centrality at all.

## 6 Analyzing Two Enterprise Social Networks

To assess relational quality and its proposed measures in organizational settings, we utilized two enterprise social networks (ESNs) of two large multinational corporations. Organizations implement ESNs to enhance collaboration, innovation, and knowledge management (Kane et al., 2014; Kane, 2015; van Osch & Steinfield, 2016; Wehner et al., 2017) as well as organizational socialization (Leidner et al., 2018). ESNs are used for problem-solving, work discussions and ideation, promoting events, sharing news and updates, managing tasks, and informal chats (Mäntymäki & Riemer, 2016). With their confined reach and conversational focus on discussing issues and helping each other (Richter & Riemer, 2013), ESNs are particularly suitable for studying relational quality. Studies have confirmed that participants develop reciprocal ties with deep social relations in which they exchange important information and depend on the support of others over longer periods of time (Cho et al., 2005). ESN users are aware of their joint organizational context; they establish particular roles that are reflective of their work needs and expect the meaning of those relationships to evolve over time (Trier & Richter, 2015). Also, since the audience is restricted to professionals in organizations, there is an increased likelihood that sentences carry lots of meaning, i.e., sentences tend to be longer, more complete, and better thought-out before posting.

Both of our studied enterprises, A and B, operated in the manufacturing industry and had more than 20,000 employees each. The datasets for both were drawn from Yammer, a private social network platform, often used for communication and collaboration within organizations. The data was collected in situ, capturing more than 440,000 postings by more than 24,000 employees in total. Like other social networking sites, Yammer includes features such as instant messaging; managing private and public groups; sharing files, links, and images; tagging content and other users; and searching for existing content. Individuals can choose to be members of a variety of public and private groups. Within these groups, members can post messages and create so-called message threads, consisting of the initial message and replies to it.

For Company A, the main driver for implementing an ESN was internal collaboration. More specifically, Company A wanted to connect employees irrespective of their physical location, and it wanted to provide an information repository for employees, along with a space to respond to timesensitive inquiries. In Company A’s case, Yammer was most often used to find information or get answers to questions, e.g., with issues concerning IT or technology.

For Company B, the implementation of an ESN was driven bottom-up. Some employees were already using Yammer and suggested its deployment for the entire enterprise in order to advance internal collaboration and solidify corporate culture. In Company B’s case, Yammer was most often used to promote and share news and success stories and congratulate others for their successes. The collected dataset covered a 4-year period for Company A, and a 3-year period for Company B. To mitigate seasonal spikes and nonregular usage, we restricted the dataset to include only messages sent over the last 365 days by users that had been part of the Yammer network for more than 1 year. We also excluded users who had sent less than five messages within this time frame. This decision was based on the observation that a certain set of individuals sent one to five messages in the first few days after joining the network and then stopped being active. By eliminating these users, we removed approximately 20% of the least active users to avoid a skewed distribution. Also, only English messages were considered and, for privacy and confidentiality reasons, we only considered messages posted in public groups. Messages were also anonymized, i.e., names of users were removed. The resulting data set included 71,139 messages from 2,346 Yammer users at Company A, and 28,341 messages from 839 Yammer users at Company B. Some additional dataset characteristics can be found in Table 2.

Table 2. Overview of ESN Datasets

<table><tr><td></td><td>Company A</td><td>Company B</td></tr><tr><td>Data collection time span</td><td>4 years(2013 - 2017)</td><td>3 years(2014 - 2017)</td></tr><tr><td>Number of users</td><td>&gt;15,000</td><td>&gt;9,000</td></tr><tr><td>Number of messages</td><td>&gt;300,000</td><td>&gt;145,000</td></tr><tr><td>Words</td><td>&gt;9,000,000</td><td>&gt;4,000,000</td></tr><tr><td>Number of active users throughout a year</td><td>5,371 (36%)</td><td>1,927 (21%)</td></tr><tr><td>Number of users that sent more than five messages over the last year</td><td>2,941 (20%)</td><td>1,512 (17%)</td></tr><tr><td>Number of users that sent more than five messages over the last year in English</td><td>2,346 (16%)</td><td>839 (9%)</td></tr></table>

Table 3. Correlations Between Measures of Relational Quality (Aggregated Level)

<table><tr><td>Dimension</td><td colspan="2">Activity</td><td colspan="2">Connectivity</td><td colspan="8">Content</td></tr><tr><td>Facet</td><td colspan="2"></td><td colspan="2"></td><td colspan="2">Being personal</td><td colspan="2">Being curious</td><td colspan="2">Being polite</td><td colspan="2">Sharing</td></tr><tr><td>Measure</td><td colspan="2">Number of messages sent over 365 days</td><td colspan="2">Absolute degree centrality</td><td colspan="2">Sum of standardized individual content measures for individualism and collectivism</td><td colspan="2">Sum of standardized individual content measures for asking questions and addressing another person directly</td><td colspan="2">Sum of standardized individual content measures for sentiment and politeness</td><td colspan="2">Sum of standardized individual content measures for reference and document sharing</td></tr><tr><td>Case company</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>Number of messages sent over 365 days</td><td>1</td><td>1</td><td>0.59***</td><td>0.74***</td><td>-0.03</td><td>-0.02</td><td>-0.01</td><td>0.08</td><td>-0.03</td><td>-0.05</td><td>0.11***</td><td>0.07</td></tr><tr><td>Absolute degree centrality</td><td>0.59***</td><td>0.74***</td><td>1</td><td>1</td><td>0.09***</td><td>0.02</td><td>0.07*</td><td>0.11*</td><td>-0.02</td><td>-0.01</td><td>-0.01</td><td>0.01</td></tr><tr><td>Being personal</td><td>-0.03</td><td>-0.02</td><td>0.09***</td><td>0.02</td><td>1</td><td>1</td><td>0.14***</td><td>0.14**</td><td>0.08**</td><td>0.08</td><td>-0.16***</td><td>-0.06</td></tr><tr><td>Being curious</td><td>-0.01</td><td>0.08*</td><td>0.07***</td><td>0.11**</td><td>0.14***</td><td>0.14***</td><td>1</td><td>1</td><td>0.03</td><td>0.06</td><td>0.01</td><td>0.06</td></tr><tr><td>Being polite</td><td>-0.03</td><td>-0.05</td><td>-0.02</td><td>-0.01</td><td>0.08***</td><td>0.08*</td><td>0.03</td><td>0.06</td><td>1</td><td>1</td><td>-0.03</td><td>-0.22***</td></tr><tr><td>Sharing</td><td>0.11***</td><td>0.07*</td><td>-0.01</td><td>0.01</td><td>-0.16***</td><td>-0.06</td><td>0.01</td><td>0.06</td><td>-0.03</td><td>-0.22***</td><td>1</td><td>1</td></tr><tr><td colspan="13">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001. All correlations are based on a minimum N of 839.</td></tr></table>

## 6.1 Matching Concept and Operationalization of Relational Quality

Our research objective was twofold. We aimed to advance SNA with the complementary dimension of relational quality (RQ1) and we wanted to assess how this extension would help study network roles in a more differentiated way (RQ2). Consequently, we now present our analysis of the two organizations in a way that both assesses the validity of method extension and reports novel insights to demonstrate its scientific relevance.

In the theory section, we derived our four facets of relational quality transparently from established existing theories in order to ensure that we were truly representing the relational quality concept that we were trying to augment. As our operationalized measures were gathered from established analytical linguistic approaches such as sentiment analysis, their reliability and internal validity have already been evaluated in prior literature (e.g., Islentyeva et al., 2023; Taboada et al., 2011). However, as they might not have been employed in the context of ESNs, which potentially exhibits specifics not commonly found in other textual interactions, we also performed manual coding of 50 messages for each of our suggested measures, e.g., for sharing, we investigated 50 messages containing URLs and 50 messages containing attachments. We found that all of our measures showed comparable accuracy rates of 70% and above to those of well-established dictionary-based measures—such as those of Taboada et al. (2011) for sentiment analysis, reporting 70% to 80% accuracy depending on the analyzed dataset.

We also needed to make sure that relational quality, along with its four facets, aligned well with existing measures yet augmented them in a nonredundant way. For that, we needed to showcase internal validity, including convergent and discriminant validity, as an important indicator of research quality (Hodson, 2021).

After that, we needed to demonstrate the scientific relevance of our proposed approach, i.e. how it provides insights above and beyond what traditional measures can spot at the methodological level. This enabled us to demonstrate that relational quality is indeed a new dimension at the conceptual level and that it adds value by better differentiating the various user roles and their behaviors in online social networks.

In order to get a better understanding of the convergent as well discriminant validity (Hodson, 2021) of our adopted measures for relational quality, we calculated the correlations between all measures at an aggregated level (Table 3) and at a base level (i.e., individual measures) (Table B1 in the Appendix). Correlation analysis is helpful to identify the extent to which measures overlap and the extent to which they differ. Calculating correlations is a stepping stone to showcase that the measurements are solid and nonredundant—i.e., that they are both anchored in the traditional and can stand on their own. While no standards exist, higher correlations beyond a threshold of 0.7 have been considered indicative of redundancy between measures (Hodson, 2021). Low correlations, in contrast, indicate orthogonality, and little commonality. In practice, a certain degree of overlap should be expected between old and new measures.

Since some of the measures had highly skewed distributions, and some even included zero values (e.g., in cases where a user did not use any of the words in the word lists), we decided to use Kendall’s tau coefficient to measure the strength and direction of association between two variables. As a non-parametric rank correlation method, Kendall’s tau coefficient has been found to have better statistical properties than Spearman’s rank correlation—for example, due to its robustness and insensitivity to errors (Croux & Dehon, 2010). In comparison, Kendall’s tau values are typically smaller in size than Spearman’s rank correlation and are more sensitive to error and discrepancies in the data. Table 3 showcases how the two measures for each facet correlate with the traditional set of activity and connectivity measures. Overall, the table contains 90 correlations, 57 of which (63.3%) were statistically significant at the $p <$ 0.05 level.

Numerous findings can be drawn. First, the strongest correlation was shown among the “old” measures of social networks. More specifically, correlations were highest between activity levels, i.e., the number of messages sent, and connectivity levels, i.e., the number of people a person has been in contact with (0.59 and 0.74, respectively; compare the highlighted dark grey area in Table 3). This indicates that many actors sent large numbers of messages to a range of individuals instead of solely communicating with a confined set of individuals. The high correlation is also an indicator that those measures tapped into closely related aspects. In fact, depending on the network, one could possibly substitute one with the other without losing too much predictive power. This latter observation and the relatedness of “old” measures of social networks were expected and provided impetus to conduct the study in the first place.

Second, and highlighted in the medium grey areas, there was some, but not extensive, overlap between old and new measures. This falls in line with our intention to develop a set of measures that are sufficiently different yet complementary to the existing set of social network measures. The strongest correlations appeared between activity and sharing references (0.16 and 0.17); this is not surprising, as sending a reference always goes along with sending a message.

Third, regarding our newly proposed set of measurements, it is important to look at the correlations within one facet (as highlighted in light gray). Within a facet, correlations should be stronger than outside the facet. For the majority of measures, this was correct. For some, however, it was not, which means that there was overlap. We expected some overlap, as this measure is not a formative entity but a reflective one.

Table 3 showcases how the aggregate measure for each facet correlated with the traditional set of activity and connectivity measures. Overall, the table contains 30 correlations, 14 of which (46.7%) were statistically significant at the $p < 0 . 0 5$ level. The same considerations applied to the aggregate level and the individual level. The newly developed aggregate measures had medium correlations with the existing set of measures (correlations ranges between 0 and 0.11) and medium correlations among themselves (correlations ranged between 0 and 0.22).

Overall, the results show that while there are dependencies between our newly developed relational quality measures and those traditionally used, their strength is moderate at best (most of the correlations are below 0.22). This supports the use of our relational quality facets since they indeed capture other aspects than those captured by traditional SNA. The magnitude of some correlations may seem relatively modest in comparison to the effect sizes reported by other correlation studies. However, the levels are close to the threshold of statistically significant effect sizes presented by other similar studies that apply correlation analyses for word use categories (e.g., Mehl et al., 2006). It has also been found that modest effect sizes are not only more common for bigger sample sizes but are also likely to be more representative of the true population effects (Yarkoni, 2010). Overall, we can conclude that relational quality measures effectively complement structural analysis and are nonredundant.

## 6.2 Relational Quality: Identifying, Differentiating and Understanding Roles in Social Online Interactions

In order to demonstrate that our proposed approach provides insights above and beyond what traditional measures can spot, we juxtaposed and simultaneously embedded relational quality measures with structural measures that are traditionally used in SNA. Specifically, we tried to establish a baseline for both companies with traditional measures of activity and connectivity first and then used this baseline classification as our starting point to evaluate relational quality measures.

To establish a baseline, we captured connectivity (in the form of degree centrality) and activity (in the form of sent messages) levels for users in both companies, A and B, respectively. Both are considered traditional measures and are thus representative of the way traditional SNA represents social networks. We then generated a 2×2 matrix based on the average activity and connectivity levels and the extent to which users were active or connected above and below an ordinary, or median, user. Doing so allowed us to contrast structural measures (i.e., activity and connectivity) with each facet of relational quality to better understand if and how relational quality varied across group segments.

![](/api/attachments/EKYYG6VQ/fulltext/images/9c1de75f5883f2744803965d8e5ec519f7d9afa2e641aca463fea411432c95b5.jpg)

Activity and connectivity of ESN users at Company E  
![](/api/attachments/EKYYG6VQ/fulltext/images/3e40f0edec8b2fd0842fd46037b18e3aa4adb59b469609824cb1cb325a5ef7dd.jpg)  
Figure 1. Segments of Social Network Users Based on Activity and Connectivity Levels for Company A and B

Figure 1 depicts the scatterplots for activity and connectivity levels for both companies (further network visualizations are presented in Appendix C). The red lines represent the median activity levels and median connectivity levels, respectively. For Company A, for example, a typical user sent 13 messages in 365 days and had 8 different direct communication partners; for Company B, a typical user sent 18 messages in 365 days and had 13 different direct communication partners. As indicated by the cluster of darker dots, the majority of users accumulate towards the lower lefthand side (i.e., the darkness of data points corresponds to a high number of users).

Both lines also serve as the basis for a 2×2 matrix that distinguishes between four quadrants. The quadrants are representative of users operating either above or below average levels of activity and connectivity; they are also representative of four different roles:

• Upper-left quadrant (“connectors”): Approximately 10% of users fall into this group. Those individuals have more connections than the median user, but the number of sent messages is below the median user.

• Upper-right quadrant (“engagers”): Over 40% of users fall into this category. Those individuals have more connections than the ordinary user; they also send more messages. Based on structural SNA measurements, this group might be considered the “most social” group of all.

• Lower-left quadrant (“foregoers”): Approximately 40% of users fall into this category. This group of individuals is characterized by below-median levels of activity and a below-median number of connections.

• Lower-right quadrant (“broadcasters”): Approximately 8% of users fall into this category. Those individuals are characterized by sending more messages; however, they are connected to a confined set of peers only.

In Figure 2, we take a closer look by delving into each quadrant’s level of relationship quality. Several similarities and differences stand out.

First, relational quality measures show similar direction and magnitude for all different user groups (represented by the four quadrants) across both companies.

The segment that stands out the most due to its extremes, positive as well as negative, is the lower-right quadrant, a segment that we refer to as “broadcasters.” Those individuals are characterized by sending many messages but are less connected than the median individual. Broadcasters are characterized by a very high level of sharing and low levels of the other three facets of relational quality (being personal, being curious, and being polite). On average, broadcasters are the least individualistic, are the least collectivistic, ask the least questions, and are the least likely to address others directly. They also tend to be less positive and less polite in their choice of words.

The segment that stands out next is the upper-left quadrant, also labeled “connectors.” They are less active but better connected than the median individual. In terms of relational quality, this group is the most personal and shares the least. Looking at this group in more detail, connectors are, on average, the most individualistic and also the most collectivistic. In contrast, they are the least likely to share references and documents with others.

![](/api/attachments/EKYYG6VQ/fulltext/images/8f7ff9caa75520246fd11cb55a92c6acbabb22fbe082026295ff2c4234b4d635.jpg)  
Figure 2. Comparison of Content Facets for Each Company

Note: All values are standardized and displayed using the same scale range

The upper-right and lower-left quadrants are the least outstanding in terms of relational quality. The upper right segment, also referred to as “engagers,” is the most active and most connected group. In contrast, the lower left segment, referred to as “foregoers,” is the least active and has the least connections of all. While engagers and forgoers are antitheses of each other, they behave similarly socially in a networked world.

Engagers are neither personal nor impersonal. They are slightly curious, if at all, and tend to be less polite. Foregoers, in contrast, are slightly personal. They are neither curious nor disinterested but tend to be polite. In fact, they are the politest individuals across all groups. While engagers and foregoers as vastly different regarding their structural embeddedness, their activity per relationship is very similar (i.e., number of messages per contact). Apparently, regardless of the number of contacts, people with a similar share of activity per relationship expose similar relational quality characteristics. This demonstrates how relational quality, as a newly conceptualized and measured dimension, can provide a more detailed and augmented understanding.

To systematically identify relationships, we also compared groups along the two structural dimensions, activity and connectivity (i.e., x and y axes). Keeping connectivity levels constant and looking at low versus high activity levels only (i.e., comparing foregoers vs. broadcasters and connectors vs. engagers), we found that levels of “being personal” (PER), “being curious”

(CUR) and “being polite” (POL) decline, while the level of sharing (SHA) changes increases. For example, when moving from foregoers (F) to broadcasters (B), we note the following differences for Company A (Company B has similar differences): PE $\mathrm { R _ { F } } = 0 . 0 4 9 > \mathrm { P E R _ { B } } = - 0 . 5 7 8 ;$ $\mathrm { C U R _ { F } } = 0 . 0 5 2 > \mathrm { C U R _ { B } } = - 0 . 4 9 5 ; \mathrm { P O L _ { F } } = 0 . 1 1 1 > \mathrm { P O L _ { B } }$ = -0.046; and $\mathrm { S H A _ { F } = - 0 . 0 4 8 < S H A _ { B } = 0 . 6 8 4 }$ , while controlling for connectivity levels. Thus, with increasing activity levels, the first three facets of relational quality—being personal, curious, and polite— decline, while sharing resources increases.

In contrast, when holding activity levels constant and comparing the two groups of low vs. high connectivity (i.e., foregoers vs. connectors and broadcasters vs. engagers), we note that the first two relational quality facets, i.e., being personal and being curious, increase while sharing resources decreases. For example, for Company A, we found that: $\mathrm { P E R _ { F } } = 0 . 0 4 9 < \mathrm { P E R _ { C } } =$ 0.214; CUR<sub>F</sub> = 0.052 < CUR<sub>C</sub> = 0.188; and SHA<sub>F</sub> = -0.048 > SHA<sub>C</sub> -0.455. Interestingly, being polite decreased for both from $\mathrm { P O L _ { F } } = 0 . 1 1 1 > \mathrm { P O L _ { C } } = - 0 . 0 6 6$ and $\mathrm { P O L _ { B } } - 0 . 0 4 6 > \mathrm { P O L _ { E } } = - 0 . 0 7 2$

When assessing correlations between relational quality facets and structural measures, we note several significant relations. For example, sharing resources generally correlates with a central and active position in the network (see Table 3). Further insights at the item level emerging from our detailed correlation analysis can be found in Appendix B. For example, a similar link exists between a central position in the network and asking questions $( { \mathrm { e . g . , } } \tau = 0 . 1 3 \ { \mathrm { a t } } p < 0 . 0 0 1 \ { \mathrm { i n } } \mathrm { \ B } )$ . We also note that individualism relates negatively to sentiment $( \tau = - 0 . 1 2 \mathrm { a t } p < 0 . 0 0 1$ for Company A) while collectivism relates positively to sentiment $( \tau = 0 . 1 2$ at $p < 0 . 0 0 1$ for Company A) and positively to politeness $( \tau = 0 . 1 4 \mathrm { a t } p < 0 . 0 0 1$ for Company A). Thus, if people refer to their group, this typically coincides with a friendlier conversational tone. Further, asking questions was negatively related to sentiment $( { \mathrm { e . g . , } } \tau = 0 . 2 2 { \mathrm { a t } } p <$ 0.001 for Company B). Generally, being polite and curious thus increases with higher levels of connectivity and decreases when individuals are very active, sharing resources decreases with increasing numbers of contacts and increases with activity levels, and being polite appears to slightly decrease with higher activity levels and more networking contacts.

## 7 Discussion and Implications

## 7.1 Were We Successful at Conceptualizing and Operationalizing Relational Quality as a New Dimension that Augments SNA?

Our first research question departed from the methodological critique by relational sociologists (Crossley, 2010), scholars of social capital (e.g., Moran, 2005), and several IS researchers (e.g. Howison et al., 2011; Trier & Richter, 2015) that SNA, in its classic form, is too limited on structural aspects and should be extended with other methods or metrics. We further noted that an important shortcoming is the current lack of focus on the relational dimension of online social interaction. Consequently, we developed a systematic extension of relational quality and evaluated its ability to augment structural SNA.

First, we found that relational quality emerges as a relevant factor, as indicated by more than half of the postings containing one or more of the four proposed facets (see Appendix B). Specifically, our findings reveal that the classic measures of activity and connectivity are highly correlated, suggesting that they reflect a single dimension of social relating (Hodson, 2021). The low correlation between our four proposed relational quality facets and the existing structural SNA measures suggests that relational quality presents a distinct dimension, in line with the argumentation of Granovetter (1992) and the multidimensional conceptualization of social capital by Nahapiet and Ghoshal (1998).

We further note that in most cases the correlation within a relational quality facet is larger than across facets. Thus, in line with our expectation that small overlaps exist, we can confirm that the four facets represent useful and nonredundant perspectives on the concept of relational quality.

We also applied our approach to reveal more differentiated roles in two different enterprise networks. Company A’s network was mostly used for utilitarian purposes, such as soliciting information in order to proceed and solve a work task; Company B’s network was mostly used for sharing good news and congratulating one another. While both networks had different objectives, it is interesting to note that a similar relationship quality pattern emerged. This gives reason to believe that our measurement is universal enough to abstract from the actual objectives of a network and can be generalized across many different types of networks.

Overall, we believe that relational quality, modeled via the four proposed measurement facets, provides a relevant methodological augmentation for the existing structural measurements. We further note that our simple approach to measuring the four facets already captures another dimension of networking and thus provides additional insights that can be unearthed from online social interaction. This promises a useful starting point and an interesting avenue for developing more refined analytical methods that target relational quality. It further extends previous research with an approach that better scales up to study larger networks than existing qualitative in-depth analysis of individuals (e.g., Cho et al., 2005; Trier & Richter, 2015).

## 7.2 How Can Relational Quality Better Identify and Differentiate Social Network Roles?

Our inquiry into the interdependencies between relational quality and structural analysis yields a series of relevant insights that contribute to a better understanding of the different roles of employees in digital social networks.

First, the study of the two companies reveals that the different structural actor roles show different degrees and patterns of relational quality: The most personal ones are the connectors, the most curious ones are the engagers, the most polite ones are the foregoers, and the most sharing ones are the broadcasters. The identified relationship between structural and relational aspects supports the underlying premise of social capital theory arguing for the interdependence of the different perspectives (Nahapiet & Ghoshal, 1998). Following Bapna et al. (2017) who found that not all online relationships are equal, our findings imply that some roles that appear equal from a structural perspective are in fact not equal if relational quality aspects are included in the analysis.

Specifically, our findings suggest that irrespective of the number of social contacts, as the activity level increases, the relational quality facets of being personal, curious, and polite tend to decrease. Interestingly, the facetsharing resources behave in the opposite way. Here, a higher activity level is related to higher levels of sharing, independent of the number of contacts.

With these findings, our relational quality perspective adds to previous research looking at the link between activity levels and centrality (Klein et al., 2015). While a relationship between both has been previously confirmed, our study points out possible adverse effects of high levels of activity, such as a reduced level of being personal, that may render high levels of activity and connectivity less positive for trustful organizational networks. The latter finding is in line with Bapna et al. (2017) who suggested that for larger numbers of contacts, structural measures such as connectivity should not be related to trust evaluations.

Our findings further show that, when keeping activity levels constant, the relational quality facets of being personal and curious increase while being polite and sharing resources decrease. Generally speaking, most relational quality aspects increase with growing numbers of network contacts and decrease with the activity level.

Our findings also suggest that the four relational quality facets do not behave as one general construct but exhibit diverse changes, pointing to a more complex role of relational quality in digital networks. For example, the facet of sharing resources behaves opposite to the facets of being personal and being curious. In our theoretical conceptualization, we noted that sharing can have two motivations, hedonic or utilitarian (Bucher et al., 2016). Our results imply that people do not appear to consider sharing to be a “gift-giving” act for hedonic reasons but are instead motivated by utilitarian reasons.

We also note that with higher activity levels, relational quality is lower; however, this decline is smaller if with an increased activity level, the number of contacts is also larger (engager role). This interdependence links in interesting ways to the findings of Morelli et al. (2017), who stated that high levels of empathy correlate with high levels of connectivity in networks characterized by high levels of trust. The broadcaster group shows the lowest level of relational quality, suggesting that relational quality is lowest if much activity is concentrated on a few intense sharing relationships.

Another observation is that being polite decreases with increased activity levels and increased connectivity levels. This suggests that politeness is not a primary catalyst for creating larger networks but rather a mode of interaction adopted by people who have either just started building their network or rarely use it. People who are central in their network or those with whom they have exchanged many messages do not appear to consider being polite to be an important element of conversation. A possible explanation for low politeness by central or active individuals may be their routinization of the interaction in established interpersonal relationships that do not require further relationship development. Further, with added interactivity and messages, being polite is perhaps replaced by more efficiency-oriented information and resource sharing. However, we should also note that our data on this factor does not vastly fluctuate across the four actor groups.

On a more general level, our results extend the literature on role differences within digital social networks. Trier and Richter (2015) noted the role of discourse driver, i.e., actors whose motivation to participate results from their opportunity to grow and spread topical information via their postings to a larger group of followers. Bulgurcu et al. (2018) later found a similar role, which they labeled promotors, among actors who post promotional content without noting other users’ contributions. Our results suggest that the relational quality of these roles—which relate to our broadcaster and engager groups—is lower than average, supporting the view that such employees are using the network in instrumental ways. In addition, the emphasis of such individuals is on sharing—but, as we found, it is driven by utilitarian motives. Beyond these roles, however, we also note roles with above-average relational quality that articulate personalness and curiosity.

If we were to visualize connectors and engagers as nodes in a traditional SNA, they would be located in the center of the network graph, whereas the broadcasters and foregoers would be less connected and would therefore be positioned in the graph’s periphery. Our results shed more light on the differences between these two important partitions. We note that individuals in the center of the network have substantially higher levels of relational quality only if their activity level is low. The more active central individuals have a slightly lower relational quality level than inactive employees in the periphery. This suggests that next to activity level, relational quality emerges as an important explanatory factor to further disentangle role differences of peripheral vs. core network actors. Table 4 provides a contrasting view of the two most opposite groups in terms of individual differences.

Overall, our study is one of the first to systematically conceptualize and assess the role of relational quality in digital social networks. We note that our measures, while basic, augment existing structural analyses with a new, relevant dimension. We find that the four conceptualized facets of relational quality behave in complex ways, suggesting that sharing resources in digital networks is driven by utilitarian motives. Our findings extend the more recent findings on actor roles in organizational digital social networks by emphasizing their different relational quality levels. In more detail, we contribute by identifying an inverse relationship between employees’ online activity levels and their engagement in building relational quality. In our study, employees who engage primarily in networking without a high degree of activity showed substantially higher levels of relational quality. Further, relational quality emerged as an important explanatory factor for differences between core and peripheral members.

Table 4. “Broadcasters” vs. “Connectors”

<table><tr><td>Connectors (connectivity focus)</td><td>Broadcasters (activity focus)</td></tr><tr><td>Relatively more personal</td><td>Relatively impersonal</td></tr><tr><td>Relatively high use of “I” and “we”</td><td>Rare use of “I” and “we”</td></tr><tr><td>Curious / asking questions</td><td>Less curious, asking fewer questions</td></tr><tr><td>Relatively more polite (esp. when only few contacts are managed)</td><td>Relatively less polite</td></tr><tr><td>In Company B, relatively more use of positive sentiment</td><td>In Company B, relatively more use of negative sentiment</td></tr><tr><td>Rare use of sharing, indicating relational focus</td><td>Much sharing, indicating transactional focus</td></tr></table>

## 7.3 What are Avenues for Future Research?

Studying relational quality has broader implications for future research on organizational outcomes. For example, future research could investigate in more detail the impact of broadcasters’ sharing behavior. Such sharing has not only been shown to increase team performance, decision satisfaction, and knowledge integration (Mesmer-Magnus & DeChurch, 2009) but also an individual’s job performance and firm performance (Masa’deh et al., 2016). In this context, sharing, in general, and knowledge sharing, in particular, have a positive influence on trust and collaboration among virtual team members (Alsharo et al., 2017).

Similarly, research on the exchange of knowledge could be extended by studying not only whether knowledge is exchanged but, more importantly, how it is exchanged— for example, in a respectful manner as forgoers predominantly do. This would enable links to factors such as team atmosphere and performance.

Relational quality would also enable a more systematic examination of team effectiveness using SNA. This could extend existing studies that note how contributing to a more positive, personal relationship—as the connector role does—contributes to overall team performance (Hu & Liden, 2015). Future studies could also focus on comparing relational quality across different industries or varying cultural settings.

Further, our groundwork builds an important basis that could be used to search for additional variables allowing for a more nuanced analysis of our proposed dimensions and, hence, improving the understanding of social relations online. For instance, researchers could further distinguish between more, or less, formal interactions. Novel techniques, including machine learning and large language models (LLM), could be used for this purpose. However, while such models are known for remarkable results, they might not be easily transferable to the context of ESN, as their usage requires a careful assessment, as demonstrated in Appendix D.

Furthermore, scholars could survey individuals’ expressed perceptions of relational quality to link them to our proposed network measures. Investigating syntactic aspects of text (e.g., using a dependency tree of text) could help researchers explore new information—for instance, what users are curious about. In addition, researchers could also apply our approach to measure relational quality in public social media in order to compare—for example, environments such as Facebook or Twitter with enterprise social networks. The roles of politeness and curiosity are likely very different in ESN contexts since user roles, as well as relationship meanings, are drastically different (cf. Trier & Richter, 2015). Further, social media users are not part of a shared organizational culture and have no professional joint objectives.

Our findings can also inform design researchers by conceptualizing how to support social relationships through information systems, namely by supporting people in being (1) personal, (2) curious, (3) respectful, and (4) sharing. Future design research can now investigate what design features of social networks would encourage the development of relational quality, e.g., through emphasizing specific symbols in chats, such as context-related expressions like emoticons, or recommendations for more personal wording. Some of these forays that future research can build upon are presented in Appendix E.

## 8 Limitations

As any other research, this study has limitations. The results are corroborated in two companies only, impacting the study’s generalizability. However, by looking at those companies more closely, it was possible to eliminate confounding factors that might otherwise have impacted the statistical results. Taking two companies also provided us with a sense of whether the observed patterns apply beyond one case. Since our focus was on social network interactions that take place within organizations, we did not include public data sources, e.g. from Quora. Including those might be an interesting subject of future research.

Also, we readily admit that our proposed facets of relational quality might be measurable by additional variables. For example, being personal might also involve revealing emotions or sharing personal information. However, we found that the selected measures, chosen for their simplicity, effectively demonstrated the added value of the established dimension, were sufficiently discriminant and convergent at the same time, and were simplistic enough to be applied by other researchers. We believe that future research could easily validate our findings or add more comprehensive measures that utilize evolving technological capabilities and analytical methods.

Moreover, our approach did not include perceptual variables, such as individuals’ perceived quality of their virtual relationships, but solely objective measures. In addition, one might argue that a social network’s evolution over time might play an important role. In our case, we were primarily interested in relational quality at one point in time.

## 9 Conclusion

This study conceptualized and measured how “social” enterprise social networks truly are. We not only conceptualized the relational quality and offered a first complementary measurement approach but we also empirically validated the concept via two enterprise social networks and demonstrated the rich additional insights that can be gained about online networking. Our study emphasizes that it is important to look beyond the conventional SNA measures of being active and having many connections with others to integrate the four dimensions of relational quality, which are indispensable for capturing the richness and depth of social relationships in digital social networks. As an overall contribution, we provide a first measurement approach to capture relational quality in computermediated and networked environments and a first empirical inquiry that reveals the importance of considering this added dimension of network research.

## References

Abhari, K., Davidson, E., & Xiao, B. (2022). Inventing Together: The Role of Actor Goals and Platform Affordances in Open Innovation. Journal of the Association for Information Systems, 23(1), 264- 302.

Alsharo, M., Gregg, D., & Ramirez, R. (2017). Virtual team effectiveness: The role of knowledge sharing and trust. Information & Management, 54(4), 479-490.

Altman, I., Vinsel, A., & Brown, B. B. (1981). Dialectic conceptions in social psychology: An application to social penetration and privacy regulation. Advances in Experimental Social Psychology, 14, 107-160.

Arguello, J., Butler, B. S., Joyce, L., Kraut, R., Ling, K. S., & Wang, X. (2006). Talk to me. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems.

Baker, A. C., Jensen, P. J., & Kolb, D. A. (2005). Conversation as Experiential Learning. Management Learning, 36(4), 411-427.

Bapna, R., Gupta, A., Rice, S., & Sundararajan, A. (2017). Trust and the Strength of Ties in Online Social Networks: An Exploratory Field Experiment. MIS Quarterly, 41(1), 115-130.

Bartelt, V., Urbaczewski, A., Mueller, A., & Sarker, S. (2020). Enabling collaboration and innovation in Denver’s smart city through a living lab: a social capital perspective. European Journal of Information Systems, 29(4), 369-387.

Bellotti, E. (2016). Qualitative methods and visualizations in the study of friendship networks. Sociological Research Online, 21(2), 1-10.

Berry, L. L. (1995). Relationship Marketing of Services--Growing Interest, Emerging Perspectives. Journal of the Academy of Marketing Science, 23(4), 236-245.

Bhattacharyya, S., Banerjee, S., & Bose, I. (2020). One size does not fit all: Rethinking recognition system design for behaviorally heterogeneous online communities. Information & Management, 57(7).

Blumer, H. (1986). Symbolic interactionism: Perspective and method. University of California Press.

Bolíbar, M. (2016). Macro, meso, micro: Broadening the “social” of social network analysis with a mixed methods approach. Quality & Quantity, 50(5), 2217-2236.

Bouman, W., de Bruin, B., Hoogenboom, T., Huizing, A., Jansen, R., & Schoondorp, M. (2007). The realm of sociality: Notes on the design of social software. Proceedings of the International Conference on Information Systems.

Bourdieu, P. (1983). The Forms of Capital. In J. G. Richardson (Ed.), Handbook of theory and research for the sociology of education (pp. 241- 258). Greenwood Press.

Brown, P., & Levinson, S. C. (1987). Politeness: Some universals in language usage. Cambridge University Press.

Bucher, E., Fieseler, C., & Lutz, C. (2016). What’s mine is yours (for a nominal fee)—Exploring the spectrum of utilitarian to altruistic motives for Internet-mediated sharing. Computers in Human Behavior, 62, 316-326.

Bulgurcu, B., van Osch, W., & Kane, G. C. (2018). The rise of the promoters: User classes and contribution patterns in enterprise social media. Journal of Management Information Systems, 35(2), 610-646.

Burr, V. (2015). Social constructionism (3rd ed.) Taylor & Francis.

Burt, R. S. (1995). Structural holes: The social structure of competition. Harvard University Press.

Cassell, J., & Tversky, D. (2006). The language of online intercultural community formation. Journal of Computer-Mediated Communication, 10(2), Article JCMC1027.

Cho, H.-K., Trier, M., & Kim, E. (2005). The use of instant messaging in working relationship development: a case study. Journal of Computer-Mediated Communication, 10(4), Article JCMC1044.

Chung, C., & Pennebaker, J. (2007). The Psychological Functions of Function Words. Social communication.

Cornelissen, T. (2016). Do social interactions in the workplace lead to productivity spillover among co-workers? IZA World of Labor, 314, 1-10

Correa, T., Hinsley, A. W., & de Zúñiga, H. G. (2010). Who interacts on the Web? The intersection of users’ personality and social media use. Computers in Human Behavior, 26(2), 247-253.

Crossley, N. (2010). The social world of the network. Combining qualitative and quantitative elements in social network analysis. Sociologica, 4(1). https://doi.org/10.2383/32049

Crossley, N. (2011). Towards Relational Sociology. Routledge.

Croux, C., & Dehon, C. (2010). Influence functions of the Spearman and Kendall correlation measures. Statistical Methods & Applications, 19(4), 497- 515.

Danescu-Niculescu-Mizil, C., Sudhof, M., Jurafsky, D., Leskovec, J., & Potts, C. (2013). A computational approach to politeness with application to social

factors. Proceedings of the 51st Annual Meeting of the Association for Computational Linguistics.

Dillard, J. P., Wilson, S. R., Tusing, K. J., & Kinney, T. A. (1997). Politeness judgments in personal relationships. Journal of Language and Social Psychology, 16(3), 297-325.

Dunbar, R.I.M., Marriott, A., & Duncan, N.D.C. (1997). Human conversational behavior. Human Nature, 8(3), 231-246.

Eurostat. (2019). Digital economy and society statistics— enterprises. https://ec.europa.eu/eurostat/statisticsexplained/index.php?title=Digital\_economy\_and \_society\_statistics\_-\_enterprises (accessed 02-08- 24)

Emirbayer, M. (1997). Manifesto for a relational sociology. American Journal of Sociology, 103(2), 281-317.

Emirbayer, M. and Goodwin, J. (1994). Network analysis, culture, and the problem of agency. American Journal of Sociology, 99(6), 1141- 1454.

Fairclough, N. (1992). Discourse and text: Linguistic and intertextual analysis within discourse analysis. Discourse & Society, 3(2), 193-217.

Faraj, S., Kudaravalli, S., & Wasko, M. (2015). Leading collaboration in online communities. MIS Quarterly, 39(2), 393-412.

Faust, K. (1997). Centrality in affiliation networks. Social Networks, 19(2), 157-191.

Fraser, B. (1990). Perspectives on politeness. Journal of Pragmatics, 14(2), 219-236.

Fredriksson, L., & Eriksson, K. (2003). The ethics of the caring conversation. Nursing Ethics, 10(2), 138- 148.

Gallup. (2015). State of the global workforce. https://www.gallup.com/workplace/238079/stateglobal-workplace-2017.aspx

Gao, Q., Dai, Y., Fan, Z., & Kang, R. (2010). Understanding factors affecting perceived sociability of social software. Computers in Human Behavior, 26(6), 1846-1861.

Garg, R., Smith, M. D., & Telang, R. (2011). Measuring information diffusion in an online community. Journal of Management Information Systems, 28(2), 11-38.

Giesler, M. (2006). Consumer gift systems. Journal of Consumer Research, 33(2), 283-290.

Gifford, R., & Hine, D. W. (1994). The role of verbal behavior in the encoding and decoding of interpersonal dispositions. Journal of Research in Personality, 28(2), 115-132.

Goel, L., Johnson, N., Junglas, I., & Ives, B. (2013). Predicting users’ return to virtual worlds: A social perspective. Information Systems Journal, 23(1), 35-63.

Goffee, R., & Jones, G. (1996). What holds the modern company together? Havard Business Review, 74(6), 133-148.

Golbeck, J., Robles, C., Edmondson, M., & Turner, K. (2011). Predicting personality from Twitter. Proceedings of the 3rd IEEE International Conference on Privacy, Security, Risk and Trust and the 3rd IEEE International Conference on Social Computing (pp. 149-156).

Grandin, T., Barron, S., & Zysk, V. (2005). The unwritten rules of social relationships. Future Horizons.

Granovetter, M. S. (1992). Problems of explanation in economic sociology. In N. Nohria & R. G. Eccles (Eds.), Networks and organizations: Structure, form and action (pp. 25-56). Harvard Business School Press.

Hackman, J. R. (2002). Leading teams: Setting the stage for great performances. Harvard Business Press.

Hodson, G. (2021). Construct jangle or construct mangle? Thinking straight about (nonredundant) psychological constructs. Journal of Theoretical Social Psychology, 5(4), 576-590.

Hong, S., & Ho, H.-Z. (2005). Direct and indirect longitudinal effects of parental involvement on student achievement: Second-order latent growth modeling across ethnic groups. Journal of Educational Psychology, 97(1), 32-42.

Hong, Y., Hu, Y., & Burtch, G. (2018). Embeddedness, prosociality, and social influence: Evidence from online crowdfunding. MIS Quarterly, 42(4), 1211-1224.

Hornstein, G. A. (1985). Intimacy in conversational style as a function of the degree of closeness between members of a dyad. Journal of Personality and Social Psychology, 49(3), 671-681.

Howison, J., Wiggins, A., & Crowston, K. (2011). Validity issues in the use of social network analysis with digital trace data. Journal of the Association for Information Systems, 12(12), 767- 797.

Hu, J., & Liden, R. C. (2015). Making a difference in the teamwork: Linking team prosocial motivation to team processes and effectiveness. Academy of Management Journal, 58(4), 1102-1127.

Hu, M., & Liu, B. (2004). Mining and summarizing customer reviews. Proceedings of the ACM SIGKDD International Conference on Knowledge Discovery and Data Mining.

Islentyeva, A., Pesendorfer, L., & Tolochin, I. (2023). “Can I have a cup of tea please?”: Politeness

markers in the spoken BNC2014. Journal of Politeness Research, 19(2), 297-322.

Jourard, S. (1971). Self-disclosure, an experimental analysis of the transparent self. Wiley-Interscience.

Junglas, I., Goel, L., Abraham, C., & Ives, B. (2013). The social component of information systems—How sociability contributes to technology acceptance. Journal of the Association for Information Systems, 14(10), 585-616.

Kacewicz, E., Pennebaker, J. W., Davis, M., Jeon, M., & Graesser, A. C. (2014). Pronoun use reflects standings in social hierarchies. Journal of Language and Social Psychology, 33(2), 125-143.

Kane, G. (2015). Enterprise social media: Current capabilities and future possibilities. MIS Quarterly Executive, 14(1), 275-304.

Kane, G. C., Labianca, G. J., & Borgatti, S. P. (2014). What’s different about social media networks? A Framework and research agenda. MIS Quarterly, 38(1), 275-304.

Khansa, L., Ma, X., Liginlal, D., & Kim, S. S. (2015). Understanding members’ active participation in online question-and-answer communities: A theory and empirical analysis. Journal of Management Information Systems, 32(2), 162- 203.

Klein, A., Ahlf, H., & Sharma, V. (2015). Social activity and structural centrality in online social networks. Telematics and Informatics, 32(2), 321-332.

Knobloch, L. K. (2003). Manifestations of relationship conceptualizations in conversation. Human Communication Research, 29(4), 482-515.

Kügler, M., Smolnik, S., & Kane, G. (2015). What’s in IT for employees? Understanding the relationship between use and performance in enterprise social software. The Journal of Strategic Information Systems, 24(2), 90-112.

Luangrath, A. W., Xu, Y., & Wang, T. (2023). Paralanguage classifier (PARA): An algorithm for automatic coding of paralinguistic nonverbal parts of speech in text. Journal of Marketing Research, 60(2), 388-408.

Leidner, D. E., Gonzalez, E., & Koch, H. (2018). An affordance perspective of enterprise social media and organizational socialization. The Journal of Strategic Information Systems, 27(2), 117-138.

Lin, H., & Qiu, L. (2013). Two sites, two voices: Linguistic differences between Facebook status updates and tweets. Proceedings of the International Conference on Cross-Cultural Design. 432-440.

Litman, J. A., & Pezzo, M. V. (2007). Dimensionality of interpersonal curiosity. Personality and Individual Differences, 43(6), 1448-1459.

Litman, J. A., & Spielberger, C. D. (2003). Measuring epistemic curiosity and its diversive and specific components. Journal of Personality Assessment, 80(1), 75-86.

Mäntymäki, M., & Riemer, K. (2016). Enterprise social networking: A knowledge management perspective. International Journal of Information Management, 36(6), 1042-1052.

Masa’deh, R., Obeidat, B. Y., & Tarhini, A. (2016). A Jordanian empirical study of the associations among transformational leadership, transactional leadership, knowledge sharing, job performance, and firm performance. Journal of Management Development, 35(5), 681-705.

Matook, S., Cummings, J., & Bala, H. (2015). Are you feeling lonely? The impact of relationship characteristics and online social network features on loneliness. Journal of Management Information Systems, 31(4), 278-310.

Mehl, M. R., Gosling, S. D., & Pennebaker, J. W. (2006). Personality in its natural habitat: Manifestations and implicit folk theories of personality in daily life. Journal of Personality and Social Psychology, 90(5), 862-877.

Mesch, G., & Talmud, I. (2006). The quality of online and offline relationships: The role of multiplexity and duration of social relationships. The Information Society, 22(3), 137-148.

Mesmer-Magnus, J. R., & DeChurch, L. A. (2009). Information sharing and team performance: A meta-analysis. Journal of Applied Psychology, 94(2), 535-546.

Miller, C. A., & Rye, J. (2012). Power and politeness in interactions: ADMIRE—A tool for deriving the former from the latter. Proceedings of the International Conference on Social Informatics. (pp. 177-184).

Moody J, & White, D. R. (2003). Structural cohesion and embeddedness: a hierarchical concept of social groups. American Sociological Review, 68, 103- 127.

Moqbel, M., & Nah, F. F. (2017). Enterprise social media use and impact on performance: The role of workplace integration and positive emotions. AIS Transactions on Human-Computer Interaction, 9(4), 261-280.

Moran, P. (2005). Structural vs. relational embeddedness: Social capital and managerial performance. Strategic Management Journal, 26(12), 1129- 1151.

Morelli, S. A., Ong, D. C., Makati, R., Jackson, M. O., & Zaki, J. (2017). Empathy and well-being correlate

with centrality in different social networks. PNAS, 114(37), 9843-9847.

Moser, C., Ganley, D., & Groenewegen, P. (2013). Communicative genres as organising structures in online communities of team players and storytellers. Information Systems Journal, 23(6), 551-567.

Nahapiet, J., & Ghoshal, S. (1998). Social capital, intellectual capital, and the organizational advantage. Academy of Management Review, 23(2), 242-266.

Newman, M. E. J. (2005). A measure of betweenness centrality based on random walks. Social Networks, 27(1), 39-54.

Nie, N. H. (2001). Sociability, interpersonal relations, and the internet. American Behavioral Scientist, 45(3), 420-435.

Norrick, N. R. (1994). Involvement and joking in conversations. Journal of Pragmatics, 22(3-4), 409-430.

Oh, H., Chung, M.-H., & Labianca, G. (2004). Group social capital and group effectiveness: The role of informal socializing ties. Academy of Management Journal, 47, 860-75.

Onnela, J. P., Saramäki, J., Hyvönen, J., Szabó, G., Lazer, D., Kaski, K., Kertész, J., & Barabási, A. L. (2007). Structure and tie strengths in mobile communication networks. PNAS, 104(18), 7332- 7336.

Özbölük, T., & Dursun, Y. (2017). Online brand communities as heterogeneous gatherings: a netnographic exploration of Apple users. Journal of Product & Brand Management, 26(4), 375- 385.

Pennebaker, J. W., Booth, R. J., Boyd, R. L., & Francis, M. E. (2015). Linguistic inquiry and word count: LIWC2015. Pennebaker Conglomerates.

Pennebaker, J. W., & Chung, C. K. (2014). Counting little words in big data: The psychology of individuals, communities, culture, and history. In J. P. Forgas, O. Vincze, & J. László (Eds.), Social cognition and communication (pp. 25-42). Psychology Press.

Pennebaker, J. W., & Lay, T. C. (2002). Language use and personality during crises: Analyses of Mayor Rudolph Giuliani’s press conferences. Journal of Research in Personality, 36(3), 271-282.

Pennebaker, J. W., Mehl, M. R., & Niederhoffer, K. G. (2003a). Psychological aspects of natural language use: our words, our selves. Annual Review of Psychology, 54(1), 547-577.

Pennebaker, J. W., & Stone, L. D. (2003b). Words of wisdom: Language use over the life span. Journal

of Personality and Social Psychology, 85(2), 291- 301.

Preece, J. (2001). Sociability and usability in online communities: Determining and measuring success. Behaviour & Information Technology, 20(5), 347-356.

Renner, B. (2006). Curiosity About People: The Development of a Social Curiosity Measure in Adults. Journal of Personality Assessment, 87(3), 305-316.

Richter, A., & Riemer, K. (2013). The contextual nature of enterprise social networking: A multicase study comparison. Proceedings of the 21st European Conference on Information Systems.

Ridings, C., & Wasko, M. (2010). Online discussion group sustainability: Investigating the interplay between structural dynamics and social dynamics over time. Journal of the Association for Information Systems, 11(2), 95-121.

Robert, L. P. J., Dennis, A. R., & Ahuja, M. K. (2008). Social capital and knowledge integration in digitally enabled teams. Information Systems Research, 19, 314-334.

Rosenfeld, L. B. (2000). Overview of the ways privacy, secrecy, and disclosure are balanced in today’s society. In S. Petrino (Ed.), Balancing the secrets of private disclosures (pp. 3-18). Lawrence Erlbaum Associates.

Scott, J. (1988). Social Network analysis. Sociology, 22(1), 109-127.

Schoch, M., Gimpel, H., Maier, A., & Neumeier, K. (2023). From broken habits to new intentions: how COVID-19 expands our knowledge on postadoptive use behaviour of digital communication and collaboration, European Journal of Information Systems, 32(6), 989-1010.

Schuetz, S., Sykes, T., & Venkatesh, V. (2021). Combating COVID-19 fake news on social media through fact checking: antecedents and consequences. European Journal of Information Systems, 30(4), 376-388.

Shangguan, W., Leung, A., Agarwal, A., Konana, P., & Chen, X. (2022). Developing a composite measure to represent information flows in networks: Evidence from a stock market. Information Systems Research, 33(2), 413-428.

Sherry J. (1983). Gift giving in anthropological perspective. Journal of Consumer Research, 10(2), 157-168.

Shi, Z., Rui, H., & Whinston, A. B. (2014). Content sharing in a social broadcasting environment: Evidence from Twitter. MIS Quarterly, 38(1), 123-142.

Sias, P. (2005). Workplace relationship quality and employee information experiences. Communication Studies, 56, 375-395.

Simmel, G., & Hughes, E. C. (1949). The sociology of sociability. American Journal of Sociology, 55(3), 254-261.

Steinfield, C., DiMicco, J. M., Ellison, N. B., & Lampe, C. (2009). Bowling online: social networking and social capital within the organization. Proceedings of the 4th International Conference on Communities and Technologies (pp. 245-254).

Stieglitz, S., & Dang-Xuan, L. (2013). Emotions and information diffusion in social media—Sentiment of microblogs and sharing behavior. Journal of Management Information Systems, 29(4), 217- 248.

Stieglitz, S., Mirbabaie, M., Ross, B., & Neuberger, C. (2018). Social media analytics—Challenges in topic discovery, data collection, and data preparation. International Journal of Information Management, 39, 156-168.

Sylwester, K., & Purver, M. (2015). Twitter language use reflects psychological differences between Democrats and Republicans. PLOS One, 10(9), Article e0137422.

Taboada, M., Brooke, J., Tofiloski, M., Voll, K., & Stede, M. (2011). Lexicon-based methods for sentiment analysis. Computational Linguistics, 37(2), 267-307.

Takahashi, N. (2000). The emergence of generalized exchange. American Journal of Sociology, 105(4), 1105-1134.

Tausczik, Y. R., & Pennebaker, J. W. (2010). The Psychological Meaning of Words: LIWC and Computerized Text Analysis Methods. Journal of Language and Social Psychology, 29(1), 24-54.

Tortoriello, M., Reagans, R., & McEvily, B. (2012). Bridging the knowledge gap: The influence of strong ties, network cohesion, and network range on the transfer of knowledge between organizational units. Organization Science, 23(4), 1024-1039.

Triandis, H. C. (1995). Individualism & collectivism. Westview Press.

Trier, M., & Richter, A. (2015). The deep structure of organizational online networking—an actororiented case study. Information Systems Journal, 25(5), 465-488.

Twenge, J. M., Campbell, W. K., & Gentile, B. (2013). Changes in Pronoun Use in American Books and the Rise of Individualism, 1960-2008. Journal of Cross-Cultural Psychology, 44(3), 406-415.

Valente, T. W., Coronges, K., Lakon, C., & Costenbader, E. (2008). How Correlated Are Network Centrality Measures? Connections, 28(1), 16-26.

van den Hooff, B., de Leeuw van Weenen, F., Soekijad, M., & Huysman, M. (2010). The value of online networks of practice: the role of embeddedness and media use. Journal of Information Technology, 25(2), 205-215.

van Osch, W., & Steinfield, C. W. (2016). Team boundary spanning: Strategic implications for the implementation and use of enterprise social media. Journal of Information Technology, 31(2), 207-225.

van Osch, W., & Steinfield, C. W. (2018). Strategic visibility in enterprise social media: Implications for network formation and boundary spanning. Journal of Management Information Systems, 35(2), 647-682.

Wang, X.-H. F., Fang, Y., Qureshi, I., & Janssen, O. (2015). Understanding employee innovative behavior: Integrating the social network and leader-member exchange perspectives. Journal of Organizational Behavior, 36, 403-420.

Wehner, B., Ritter, C., & Leist, S. (2017). Enterprise social networks: A literature review and research agenda. Computer Networks, 114, 125-142.

Wish, M., D’Andrade, R. G., & Goodnow, J. E. (1980). Dimensions of interpersonal communication: Correspondences between structures for speech acts and bipolar scales. Journal of Personality and Social Psychology, 39(5), 848-860.

White, H. (1992). Identity and control. Princeton University Press.

Wong, R., Cheung, C., Xiao, B., & Thatcher, J. (2021). Standing up or standing by: Understanding bystanders’ proactive reporting responses to social media harassment. Information Systems Research, 32(2), 561-581.

Yarkoni, T. (2010). Personality in 100,000 Words: A large-scale analysis of personality and word use among bloggers. Journal of Research in Personality, 44(3), 363-373.

Yoo, Y., & Kanawattanachai, P. (2001). Developments of transactive memory systems and collective mind in virtual teams. International Journal of Organizational Analysis, 9, 187-208.

Zhang, X., Leidner, D., Cao, X., & Liu, N. (2022). Workplace cyberbullying: A criminological and routine activity perspective. Journal of the Association for Information Systems, 37(1), 51- 79.

Zhou, S., Qiao, Z., Du, Q., Wang, G. A., Fan, W., & Yan, X. (2018). Measuring Customer Agility from Online Reviews Using Big Data Text Analytics. Journal of Management Information Systems, 35(2), 510-539.

## Appendix A: Traditional Social Network Analysis Measures

Social network analysis (SNA) relies on the mathematical structure of a graph (often captured as a mathematical matrix) that captures actors as nodes and their relationships as edges. In the IS field, SNA has been used extensively as a method. Studies have focused on an online network’s structure to answer questions about how and why individuals contribute to, share, and collaborate in online communities (Shi et al., 2014), how information diffuses in those communities (Stieglitz & Dang-Xuan, 2013), how groups sustain and stay alive (Ridings & Wasko, 2010), and how trust is formed (Bapna et al., 2017). For that, researchers have looked at a broad range of online networks, such as Yahoo!Answers (Khansa et al., 2015), Twitter (Stieglitz & Dang-Xuan, 2013; Shi et al., 2014), Facebook (Bapna et al., 2017), and online music communities (Garg et al., 2011). These studies mainly rely on two quantitative dimensions: the level of user activity (e.g., number of postings) and connectivity, i.e., the degree to which that user is connected to others within the network.

Activity levels are unquestionably an important structural measure. The frequency and amount with which individuals contribute to an online group or network is an important aspect of social networking and is typically considered representative of a social person (e.g., Nie, 2001). Studies exist, for example, that look at the frequency with which individuals post weekly questions and weekly answers; they have used SNA to demonstrate that both were mostly driven by the level of membership and tenure, past behaviors, and incentives, including badges or ratings (Khansa et al., 2015). Connectivity levels are the second most used marker to quantify social networks and typically comprise measures that are reflective of the number of communication partners an individual has. For example, studies show that connectivity in online social settings is strongly related to the depths of relationships between people and also allows for the analysis of structural positions in any given network (Shi et al., 2014).

## Appendix B: Correlation Details

Table B1: Correlations between Measures of Relational Quality at the Individual Content Level

<table><tr><td>Dimension</td><td colspan="2">Activity</td><td colspan="2">Connectivity</td><td colspan="16">Content</td></tr><tr><td>Facet</td><td rowspan="2" colspan="2">Number of messages sent over 365 days</td><td rowspan="2" colspan="2">Absolute degree centrality</td><td colspan="4">Being personal</td><td colspan="4">Being curious</td><td colspan="4">Being polite</td><td colspan="4">Sharing</td></tr><tr><td>Measure</td><td colspan="2">Individualism</td><td colspan="2">Collectivism</td><td colspan="2">Asking questions</td><td colspan="2">Addressing another person directly</td><td colspan="2">Sentiment</td><td colspan="2">Politeness</td><td colspan="2">Reference sharing</td><td colspan="2">Document sharing</td></tr><tr><td>Case company</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td><td>A</td><td>B</td></tr><tr><td>Number of messages sent over 365 days</td><td>1</td><td>1</td><td>0.59***</td><td>0.74***</td><td>-0.01</td><td>0.03</td><td>0.03</td><td>0.04</td><td>0</td><td>0.12*</td><td>0.04</td><td>0.09</td><td>-0.01</td><td>0.02</td><td>0</td><td>-0.08</td><td>0.16***</td><td>0.17***</td><td>0.07*</td><td>0.04</td></tr><tr><td>Absolute degree centrality</td><td>0.59***</td><td>0.74***</td><td>1</td><td>1</td><td>0.12***</td><td>0.07</td><td>0.08**</td><td>0.06</td><td>0.08**</td><td>0.13**</td><td>0.07*</td><td>0.11*</td><td>-0.01</td><td>0.07</td><td>0.02</td><td>-0.06</td><td>0.06*</td><td>0.12*</td><td>-0.02</td><td>-0.01</td></tr><tr><td>Individualism</td><td>-0.01</td><td>0.03</td><td>0.12***</td><td>0.07</td><td>1</td><td>1</td><td>-0.08**</td><td>-0.05</td><td>0.24***</td><td>0.15***</td><td>0.08**</td><td>0.17***</td><td>-0.12***</td><td>-0.03</td><td>0.05</td><td>0.1</td><td>-0.09***</td><td>0.03</td><td>-0.15***</td><td>-0.09</td></tr><tr><td>Collectivism</td><td>0.03</td><td>0.04</td><td>0.08***</td><td>0.06</td><td>-0.08***</td><td>-0.05</td><td>1</td><td>1</td><td>-0.01</td><td>0.03</td><td>0.07**</td><td>0.04</td><td>0.12***</td><td>0.07</td><td>0.14***</td><td>0.06</td><td>-0.03</td><td>0.05</td><td>-0.04</td><td>-0.02</td></tr><tr><td>Asking questions</td><td>0</td><td>0.12***</td><td>0.08***</td><td>0.13***</td><td>0.24***</td><td>0.15***</td><td>-0.01</td><td>0.03</td><td>1</td><td>1</td><td>0.08**</td><td>0.12*</td><td>-0.18***</td><td>-0.22***</td><td>0</td><td>0.02</td><td>0.13***</td><td>0.33***</td><td>-0.05</td><td>0.03</td></tr><tr><td>Addressing another person directly</td><td>0.04*</td><td>0.09*</td><td>0.07***</td><td>0.11**</td><td>0.08***</td><td>0.17***</td><td>0.07***</td><td>0.04</td><td>0.08***</td><td>0.12***</td><td>1</td><td>1</td><td>0.07**</td><td>0.16***</td><td>0.26***</td><td>0.27***</td><td>0.06</td><td>0.09</td><td>0</td><td>-0.09</td></tr><tr><td>Sentiment</td><td>-0.01</td><td>0.02</td><td>-0.01</td><td>0.07*</td><td>-0.12***</td><td>-0.03</td><td>0.12***</td><td>0.07*</td><td>-0.18***</td><td>-0.22***</td><td>0.07***</td><td>0.16***</td><td>1</td><td>1</td><td>0.13***</td><td>0.12*</td><td>0</td><td>-0.17***</td><td>0.07*</td><td>-0.18***</td></tr><tr><td>Politeness</td><td>0</td><td>-0.08*</td><td>0.02</td><td>-0.06</td><td>0.05**</td><td>0.1**</td><td>0.14***</td><td>0.06</td><td>0</td><td>0.02</td><td>0.26***</td><td>0.27***</td><td>0.13***</td><td>0.12***</td><td>1</td><td>1</td><td>-0.06</td><td>-0.02</td><td>-0.1***</td><td>-0.09</td></tr><tr><td>Reference sharing</td><td>0.16***</td><td>0.17***</td><td>0.06**</td><td>0.12***</td><td>-0.09***</td><td>0.03</td><td>-0.03</td><td>0.05</td><td>0.13***</td><td>0.33***</td><td>0.06**</td><td>0.09*</td><td>0</td><td>-0.17***</td><td>-0.06**</td><td>-0.02</td><td>1</td><td>1</td><td>0.39***</td><td>0.26***</td></tr><tr><td>Document sharing</td><td>0.07***</td><td>0.04</td><td>-0.02</td><td>-0.01</td><td>-0.15***</td><td>-0.09**</td><td>-0.04</td><td>-0.02</td><td>-0.05**</td><td>0.03</td><td>0</td><td>-0.09**</td><td>0.07***</td><td>-0.18***</td><td>-0.1***</td><td>-0.09**</td><td>0.39***</td><td>0.26***</td><td>1</td><td>1</td></tr><tr><td colspan="21">Note: *p&lt;0.05; **p&lt;0.01; ***p&lt;0.001. All correlations are based on a minimum N of 839.</td></tr></table>

## Appendix C: Visualizing Relational Quality Measures

In a cross-check analysis, we used social network graphs as a means to visualize the proposed new facets of relational quality. Since activity and connectivity levels are part of their default or baseline model, the decision to use social network graphs was deliberate. In that sense, we will use a network graph to highlight the various facets that would otherwise be hard, if not impossible, to interpret.

Table C1 shows individuals as nodes and the number of messages sent between two nodes as connection strength. Overall, it showcases relational quality at the aggregate level. In order to visualize a three-dimensional network graph in a two-dimensional format, graph embedding was required that provided meaningful distances. For that, we used the Spring layout algorithm provided by the Python NetworkX package. The algorithm places springs between each pair of nodes with their strength proportional to their connection strength.

Table C1 also visually compares and contrasts both networks along the various facets. One data point represents one person. We start off with what we refer to as the “baseline” model that captures connectivity (in the form of degree centrality) and activity (in the form of sent messages) levels displayed in one graph. Both are considered “traditional” measures and thus representative of the way traditional SNA tools would measure social networks.

Each facet is displayed as a standardized measure with a scale ranging from dark blue (negative) to dark red (positive). Thus, dark blue points indicate that a facet is present much below the average presence in the network; lighter colors and white indicate that the facet is present close to the average presence in the network; and dark red indicates that the facet is more strongly present than on average. Visually, we can see that the four content facets capture a different story when compared to the traditional measures. At the very least, we can tell that all four facets complement traditional measures in understanding social networks.

Table C1. Measures of Relational Quality at the Aggregate Content Level Across Both Networks

<table><tr><td>Case company</td><td>A</td><td>B</td><td>Description &amp; Interpretation</td></tr><tr><td>“Baseline model” representing connectivity and activity levels</td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/b4200a5337ee5b9ca75e24b03cfc596ab66492b0e46531e0df821b2cb112483d.jpg"/></td><td></td><td>The graph represents the baseline graph produced by traditional means of SNA. It depicts degree centrality (i.e., connectivity) as well as activity levels (i.e., sent messages).The graphs display very connected and active individuals in dark red versus minimally connected and inactive individuals in dark blue.The most connected and active individuals are placed in the middle of the network graph using the Spring Layout method.</td></tr><tr><td>Facet: Being personal</td><td></td><td></td><td>In this graph, dark reds indicate high levels of “being personal.”Given that the most connected and most active individuals are located in the middle, the graph illustrates that those are not necessarily the most personal individuals.Personal individuals (i.e., those that talk about themselves and about the group) tend to be located near the center as well as in the middle and outer bands of the graph.</td></tr><tr><td>Facet: Being curious</td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/6ce6e5743c9d0a239d73c9cc9955f8518881b695294b17c355fb9273e4d7f23a.jpg"/></td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/2c126ef3a8715a0ce035170c2f66e60cc37aa3828fab16712b1494071ade8d10.jpg"/></td><td>In this graph, dark reds indicate high levels of “being curious.”Given that the most connected and most active individuals are located in the middle, the graph illustrates that those in tendency are also curious individuals.Curious individuals (i.e., those that ask questions and address other people directly) tend to be near the center as well as in the middle band of the graph.</td></tr><tr><td>Facet: Being polite</td><td></td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/0cd40992f7355468d65575306511f5280e1fb3a1bf2bcb326064a00a9fb123e0.jpg"/></td><td>In this graph, dark reds indicate high levels of “being polite.”Given that the most connected and most active individuals are located in the middle, the graph illustrates that those in tendency are less polite individuals.Polite individuals (i.e., those that are positive and polite in their messages) tend to be spread all over the graph and can be found less in the center of the graph.</td></tr><tr><td>Facet: Sharing</td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/b0fd5343875fd3dab3ea058eaf55cd9de3f383e0ea323733d42080117d4028c7.jpg"/></td><td><img src="/api/attachments/EKYYG6VQ/fulltext/images/1568f9beabaa8fe1abaa2e3cd5f427b35b2ba4fbb92bd935ba392e8e50995da7.jpg"/></td><td>In this graph, dark reds indicate high levels of “sharing.”Given that the most connected and most active individuals are located in the middle, the graph illustrates that those in tendency are less sharing individuals.Sharing individuals (i.e., those that share URLs and attachments) tend to be spread all over the graph and can be found less in the center of the graph.</td></tr></table>

## Appendix D: Conducting Supplemental Analysis

The primary contribution of our study is to conceptualize and examine the role of relational quality in organizational conversations using relational social capital theory and relational sociology. In addition, we provide a measurement approach that is not only content valid and discriminant but also replicable and easily executable for organizations and researchers alike.

A secondary outcome is our hope that IS researchers—guided by our theoretical framework—explore novel analytical methods and refine measures to further evolve our understanding of relational quality in digital interactions, triggering a broader methodological strand of innovative research. We use this appendix to report (and reflect on) some promising approaches we explored on our journey but did not apply.

For example, the concept of “being curious” could be further operationalized to distinguish between formal and informal questions. Other variations might examine a broad versus narrow scope, an expert versus a lay audience, open-ended versus closed questions, or asking about the present, past, or future. Measuring those will require more sophisticated natural language processing (NLP) techniques; they might even pose novel NLP challenges. While these analytical forays are certainly valid to explore, they also come with a caveat: Their usage requires a careful theoretical argumentation and justification to align with our conceptually derived dimensions.

That said, our latest foray was into the use of large language models (LLM). LLMs are increasingly used for textual analysis (Schneider et al., 2024); they are versatile in nature and easily accessible. To handle specific tasks, however, LLMs are often adjusted for performance or are incorporated into complex NLP algorithms, e.g., for topic modeling (Grottenhorst, 2022).

For our purposes, we explored OpenAI’s ChatGPT 4o abilities to distinguish the level of formality embedded in a question, i.e., formal versus informal. (Note that formality was not part of our methodological assessment but was proposed by the reviewers.) We ran our analysis with a series of test prompts as well as labeled messages (few-shot prompting). The transcript, shown in Table D1, includes a sample prompt with two messages (two-shot prompt).

Method: We sampled 60 messages in total. The messages had to be manually selected since, due to confidentiality reasons, we were not allowed to upload arbitrary ESN messages to an open platform. (Note: We also disallowed OpenAI to store any of our data, i.e., prompts and responses.) The messages could not contain any identifiers or knowledge that could potentially be of interest to a competitor. This presents a major obstacle and is a possible source of bias for the analytical method.

We used fresh sessions for each submitted prompt. We also did not provide any ground truth to the model aside from up to ten labeled messages (as few-shot prompts).

Table D1. Transcript of LLM Interaction

<table><tr><td>Prompt: Label the messages as informal or formal. Informal messages characterized by chat style messages, often having non-complete sentences, often emotional and possibly also emoticons. Formal messages are mostly complete sentences, typically without showing strong emotions.</td></tr><tr><td>Message: Really? :-)</td></tr><tr><td>Label: Informal</td></tr><tr><td>Message: I was curious to know how seriously we consider the human vulnerabilities which could potentially lead to a security breach?</td></tr><tr><td>Label: Formal</td></tr></table>

Evaluation: Of 60 messages, only 33 were classified correctly. The confusion matrix, highlighting the different types of errors, is shown in Table D2.

Table D2. Confusion Matrix

<table><tr><td></td><td>Predicted informal</td><td>Predicted formal</td><td>Total</td></tr><tr><td>Actual informal</td><td>4</td><td>4</td><td>8</td></tr><tr><td>Actual formal</td><td>23</td><td>29</td><td>52</td></tr><tr><td>Total</td><td>27</td><td>33</td><td>60</td></tr></table>

When examining the results and reflecting on our own labeling, we found considerable challenges.

First, without any explanation or concise definition of “formal” and “informal,” LLMs cannot succeed. (Again, this showed that the concept had to precede the measure.) Providing examples would be of little help as we noted that the difference between formal and informal messages is not very prevalent—and even for humans a nontrivial task to pick up on.

Second, the validation of results was unsatisfactory. Various prompts, including few-shot prompting, did not yield sufficient accuracies, and automating the categorization of questions into formal/informal using LLMs could not be achieved without significant extra effort, including manually labeling data and/or employing fine-tuning.

And last, there is not sufficient ESN data publicly accessible that could be used for LLM training purposes as corporations tend to keep ESN data confidential. Creating a large training pool of labeled data with explanations (to better support chain-of-thought reasoning) and appropriate evaluation measures would require a substantial research effort in and by itself.

In conclusion, LLMs were not effective for the purposes of our study.

## Appendix E: Supplemental Validation Analyses

As part of our foray into operationalizing the various facets of relational quality, we also conducted the following explorations—mostly requested by the review team. Those analyses, which required manual coding, should be viewed as validation checks for our proposed measurement.

## Exploration 1: Measuring “Being Curious”—Use of Question Marks

Objective: We analytically explored whether a question mark was indeed indicative of asking for information and part of “being curious” in a conversation.

(Remember that in our study, “being curious” was measured using a dictionary-based approach, looking for a combination of question marks and the usage of second-person singular and plural pronouns.)

Method: We coded 50 randomly selected statements that ended with a question mark into one of three categories: (1) asking for information (truly expressing curiosity, e.g., “How was the movie?”), (2) possibly expressing curiosity, but mostly unclear (e.g., “Really?” or “I don't understand ???”), and (3) not directly asking for information, including sarcasm (e.g., “Oh, you think that was a good idea?”), asking for favors (e.g., “Lube any one?”) or when sharing was not part of the conversation, such as sharing information from an article).

Evaluation: 29 out of 50 were classified as Category 1; 6 out of 50 as Category 2; and 15 out of 50 as Category 3. Given that 35 either qualified as category 1 or 2, we deem our measure as adequate, particularly, since we did not find any indications that a question mark indicated the opposite such as disinterest or calls for stopping a conversation (“Could you end this debate?”).

## Exploration 2: Measuring “Being Curious”—Use of Second-Person Singular and Plural

Objective: We analytically explored whether second-person singular and plural pronouns (e.g., you/yours) were indeed addressing someone directly as part of a conversation.

(Remember that in our study “being curious” was measured using a dictionary-based approach, looking for a combination of question marks and the usage of second-person singular and plural pronouns.)

Method: We coded 50 randomly selected statements that ended with a question mark into one of two categories: (1) statements that used “you” within a dialogue as a means to address the other personally (e.g., “How are you?”), or (2) statements, such as “The title of the song is: ‘You never walk alone’” where “you” is not indicative of addressing anybody directly.

Evaluation: 50 out of 50 were classified correctly with our measurement approach.

## Exploration 3: Measuring “Being Polite”—Use of Polite Words

Objective: We analytically explored whether the usage of polite words was indicative of “being polite.”

(Remember that in our study “being polite” was measured with a dictionary-based approach, using polite words (e.g., “please,” “thank you”) in combination with positive sentiment scores.)

Method: We selected 50 messages from our data set and explored whether they fit into one of the following two categories: (1) statements truly indicating politeness, or (2) statements, such as “You spilled coffee over my shirt. Thanks!” that are sarcastic or ambiguous.

Evaluation: 36 out of 50 were classified as Category 1; 14 were classified as Category 2 as the statement was simply “Thx,” “Thanks,” or “Thank you,” which is very likely indicating a gesture of politeness, but inconclusive as it requires additional context to verify.

## Exploration 4: Measuring “Resource Sharing”

Objective: We analytically explored whether sharing URLs or attachments is truly indicative of a prosocial act of gift giving.

(Remember that in our study “sharing” was measured as a prosocial act of gift giving, using the occurrence of URLs and attachments.)

Method: We coded 50 randomly selected messages containing a URL and 50 containing an attachment. We coded them manually as sharing or not sharing by reading the associated message.

Evaluation: For attachments, we found that our notion of sharing held true in 40/50 cases; in one case we were unsure, and in 9/50 cases we found that messages were not related to sharing. Likewise, for URLs, we found that our notion of sharing held true in 39/50 cases, and in 11/50 cases those messages were not related to sharing in our sense.

Note that we did not consider posting links or documents of company-wide performance reports (e.g., sales reports) as sharing if those were not explicitly requested; we assume this seems to be more of a business-only update. While this is debatable, including those messages would only improve our measure. Also, standard corporate communications (e.g., about corporate news or achievements) were not considered. Overall, we found that most cases of sharing occurred as a spontaneous act during a conversation, e.g., a person explicitly seeking information, or a person sharing information relevant to others without being overtly asked for it.

## Exploration 5: Measuring “Being Personal”—Collectivism

Objective: We analytically explored whether first-person plural pronouns (e.g., “we, we’ve, let’s, us, ours”) are indeed indicative of collectivism.

(Remember that in our study, collectivism was measured using a dictionary-based approach, looking for first-person singular pronouns. Together with measures for individualism, collectivism constituted a measure of “being personal.”)

Method: We randomly selected 50 statements and coded them into three categories: (1) being personal (e.g., if “we” referred to group members in a personal way rather than a general comment like “we” as a company), (2) maybe (unclear, given the message only), and (3) not indicating being personal (e.g., if “we” referred to the entire organization or was part of a saying like “here we go”).

Evaluation: We found that our assumption held true in most cases. 31 out of 50 cases were classified as Category 1, 10 as Category 2, and 9 cases as Category 3. As such, we deem our measure adequate—in particular, since we did not find any indications where “we” indicated the opposite, such as being extremely impersonal or noninclusive for some group members (e.g., “we, the management of this company, prefer this, while you (the ordinary workers)....”).

## Exploration 6: Nonverbal Cues in Addition to Textual Content

Exploration Objective: Identifying nonverbal cues

Method: We applied an approach, suggested by quantitative marketing and showcased by (Luangrath et al., 2023).

Evaluation: We tested the recommended tool with a few samples and found it to be excellent. However, for our proprietary corporate data, this approach is unsuitable as the tool requires online uploads.

## About the Authors

Christian Meske is a full professor of socio-technical system design and artificial intelligence at the Institute of Work Science at Ruhr University Bochum and a member of the European Research Center for Information Systems (ERCIS). His research centers on the design, use, and impact of digital technologies in organizations, providing insights into the interplay between technology, individuals, and organizational structures. He has contributed to numerous interdisciplinary research projects and published over 80 articles in leading conferences and journals, including Business & Information Systems Engineering, Communications of the Association for Information Systems, Information Systems Frontiers, Information Systems Journal, Information Systems Management, and MIS Quarterly Executive. He also serves as a senior editor for Information Systems Management and holds various other roles.

Iris Junglas is the Noah T. Leask Distinguished Professor of Information Management and Innovation in the Department of Supply Chain and Information Management at the College of Charleston. Iris’s research sits at the intersection of technology innovation, business analytics and AI. She has published more than 60 refereed journal articles in outlets including Decision Support Systems, European Journal of Information Systems, Information & Management, Information and Organization, Information Systems Journal, Journal of the Association of Information Systems, Journal of Strategic Information Systems, and MIS Quarterly. Iris is also a Fulbright Scholar from Maynooth University in Ireland, a senior editor for the European Journal of Information Systems, and serves as the editor-in-chief for MIS Quarterly Executive, AIS’s only practitioner-oriented journal.

Matthias Trier is a professor of business informatics and social computing at Paderborn University as well as a visiting professor at Copenhagen Business School. He researches digital social user behavior in immersive social virtual reality environments, the use of social media in organizations, social interaction with intelligent artificial agents, and eventdriven dynamic social network analysis. This research resulted in software tools used by researchers for academic studies, participation in several large research projects, and more than 100 publications in conferences and high-ranked IS journals.

Johannes Schneider is an associate professor of data science and artificial intelligence at the University of Liechtenstein and a member of the European Research Center for Information Systems (ERCIS). He has held industrial research positions at IBM and ABB. Dr. Schneider earned his master’s and PhD degrees in computer science, as well as a master’s in advanced studies in management, technology, and economics, all from ETH Zurich. His research, recognized with multiple best paper awards, encompasses both theoretical foundations and practical implementations of data science, and AI and has been published widely across various academic fields.

Roope Jaakonmäki holds a PhD from the University of Liechtenstein. His research focuses mainly on practical implementations of data science techniques on unstructured data in enterprise, social media, and learning environments. His interdisciplinary approach bridges the gap between theoretical research and practical application, making his publications in information systems and learning analytics fields valuable to both academia and industry. Currently, he works as an IT product owner at Hilti.

Jan vom Brocke is the director of the European Research Center for Information Systems and is a professor and chair of Information Systems & Business Process Management at the University of Münster in Germany. He has published, among other outlets, in Management Science, MIS Quarterly, Information Systems Research, Journal of Management Information Systems, Journal of Information Technology, Journal of the Association for Information Systems, European Journal of Information Systems, Information Systems Journal, Journal of Strategic Information Systems, MIS Quarterly Executive, and MIT Sloan Management Review. He is a visiting professor at the University of Liechtenstein, and he has been named a Fellow of the Association for Information Systems, an Academic Resarch Fellow at MIT CISR, a Fellow of the ESCP Center for Design Science in Entrepreneurship, a Schoeller Senior Fellow at Friedrich Alexander University in Germany, and an Honorary Distinguished Professor at the National University of Ireland, Maynooth.

Copyright © 2025 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
