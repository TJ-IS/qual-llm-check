---
otero_id: 6798
otero_key: "J6V2QKA7"
title: "Influence in Social Media: An Investigation of Tweets Spanning the 2011 Egyptian Revolution"
authors: "Srikanth Venkatesan; Rohit Valecha; Niam Yaraghi; Onook Oh; H. Raghav Rao"
year: "2021"
journal: "MIS Quarterly"
doi: "10.25300/misq/2021/15297"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# INFLUENCE IN SOCIAL MEDIA: AN INVESTIGATION OF TWEETS SPANNING THE 2011 EGYPTIAN REVOLUTION <sup>1</sup>

Srikanth Venkatesan Department of Computer Information Systems, College of Business Administration Cal Poly Pomona, Pomona, CA, U.S.A. {svenkatesan@cpp.edu}

Rohit Valecha Department of Information Systems and Cyber Security, College of Business University of Texas at San Antonio, San Antonio, TX, U.S.A {rohit.valecha@utsa.edu}

Niam Yaraghi Miami Herbert Business School, University of Miami, Center for Technology Innovation, The Brookings Institution Coral Gables, FL, U.S.A. {niamyaraghi@miami.edu}

Onook Oh The CU Denver Business School University of Colorado Denver, Denver, CO, U.S.A. {onook.oh@ucdenver.edu}

H. Raghav Rao Department of Information Systems and Cyber Security, College of Business University of Texas at San Antonio, San Antonio, TX, U.S.A {hr.rao@utsa.edu}

Through the lens of social movement theory, this paper investigates the drivers of individual users’ social influence on Twitter during the Egyptian Revolution of 2011. Following this lens, we suggest an extended model of sustained social influence (that considers retweets as the measure of user influence) as a function of the duality of individual Twitter users’ social actions and the underlying facilitating Twitter network structure. Based on an analysis of organic large-scale Twitter data on this social movement, we examine how characteristics of individuals’ social actions, namely activity and tenure on Twitter, and characteristics facilitated by the network (i.e., the number of followers as well as centrality in the community structure of Twitter), impact retweet influence in time windows spanning the movement. Utilizing a mixed methods approach consisting of machine learning and human coding we conceptualize social movement-related engagement activities of Twitter users, which map to generic frames of social movement mobilization. The analysis reveals interesting patterns across different contexts of the Egyptian Revolution. Regarding individual social action, social movement related to “who” and “where” activities, as well as tenure, were found to contribute to individual social influence. In terms of the facilitating structure, the follower network (an observed network structure) and centrality (an unobserved network structure) were both found to contribute significantly to sustained influence.

Keywords: Social media, Twitter, retweets, influence, social movement, computational social science

## Introduction

On February 14, 2018, at Marjory Stoneman Douglas High School in Parkland, Florida, a gunman opened fire with a semi-automatic rifle, killing 17 people and injuring 17 others. Spurred by conversations in social media, the “March for Our Life”<sup>2</sup> social movement was set into motion. On March 24, 2018, student-led protesters came together in Washington, D.C. asking for legislation to prevent gun violence in the U.S. Hundreds of related events took place throughout the U.S. (Wilson 2019). In the wake of these demonstrations, Florida lawmakers passed laws establishing a higher minimum age requirement for buying firearms.

A social movement is a phenomenon of collectivity that acts continuously toward attaining or resisting a change in society or in social groups (Turner and Killian 1957). Generally, this collectivity may have shifting membership and leadership, leading to changing patterns of influence. While social movements have existed for a long time, the use of information and communications technologies (ICTs) in social movements is a relatively new phenomenon. Social media represents a relatively new ICT that provides an opportunity to link diverse and unconnected entities through a human-machine participatory interface.

Social media platforms like Twitter and component IT artifacts such as hashtags have become an integral part of citizen communication during social movements (Oh et al. 2015). The hashtag #MarchForOurLives was shared over three million times, enabling sensemaking within the various phases of social movement operations. Similarly, in India during the Jallikattu social movement on Twitter (Rao and Devi 2017), hashtags like #JusticeforJalikattu were shared over a million times, allowing for faster, 24/7 access to societal reactions. More recently, hashtags such as #BlackLivesMatter have been observed to be more prevalent around critical moments such as George Floyd’s death, resonating through related references such as #ICantBreathe. The Twitter platform has played an instrumental role in the development of frames such as “Black Lives Matter” and contributed to informationally rich conversations and protest movements (Blevins et al. 2019). Improving the understanding of the technohuman processes by which IT design artifacts may be effectively utilized by users in the context of a social movement will be useful for design scientists aiming to bring about change for the greater good of society.

This study draws on sociological theories and discusses the inclusion of technological information systems (IS) artifacts on Twitter. It contributes to the augmentation of IS knowledge by demonstrating the dynamics at the intersection of technological and social impacts. We hope that our interdisciplinary work can generate contributions to the understanding of IS by reformulating problems in sociology and placing primacy on IS (Rai 2017).

The literature on ICTs as a facilitator of collective action has been growing since the early 2000s (Brainard and Siplon 2000; Arquilla and Ronfeldt 2001; Yu et al. 2011). However, we are only aware of a few studies that focus on sustained influence in ICT-enabled social movements. Howard et al. (2011) argue that ICTs have served as effective protest tools in Tunisia and Egypt. Though massive political protests are not attributable solely to a few media platforms, it is evident that social media has played a vital role (Kravets 2011). In this paper, we focus on the 2011 Egyptian Revolution as an appropriate case to study the use of ICTs in social movements. Essentially, we extend the literature on the mobilization of social movements to the human-machine participatory interface of Twitter.

Twitter is a relatively recent ICT that enables front-row observations of organic real-time conversations among citizens; as such, is a powerful media service for capturing history as it unfolds. Twitter includes multiple functionalities such as “following” other users, topical markers (hashtags) that can identify threads, and the “retweeting” of tweets. These technological functions allow people to see a user’s comments in real time, and enable the broadcasting of popular messages in a timely manner, resulting in the rapid spread of critical topical news. Twitter, along with other social media, has played an important role in many social uprisings occurring in Arab nations (Howard et al. 2011). These social uprisings have generally been spontaneous and not centrally planned nor managed. The start dates of the uprisings, online activities, and strategies studied in this paper, were not planned; more importantly, the end dates of these uprisings and associated special events were also unknown. For example, the Egyptian Revolution of 2011 was a surprise, and citizens participated in Twitter conversations about it without a clear understanding of potential outcomes. Such organic social uprisings involve a high degree of uncertainty, and open channels like Twitter act as important bridges to informal mobilization within unorganized structures. In this paper, we study this issue in the context of this social movement to explore the patterns of behaviors (in terms of sustained influence) of the relevant users (tweeters) on the Twitter platform as the movement progressed over time.

Traditional social movement theory views the lens of resource mobilization as a duality of protestors’ social action and the underlying social structure (McAdam 1986; Lin

2002; Bennett and Segerberg 2011). We focus on this duality to analyze the drivers of user influence for mobilization. Following this lens, we identify the facets of “individual social action” and “facilitating structures” as the antecedents of Twitter influence. We adapt the lens to Twitter and investigate two antecedents that may have exerted an influence on retweet influence in the context of the Egyptian Revolution of 2011: (1) characteristics of Twitter users’ actions and tenure on Twitter, and (2) characteristics of connection structure facilitated by the network, i.e., the number of followers, as well as centrality in the community structure of Twitter. We take a computational social science approach to investigate the effect of these antecedents on retweet influence across different contexts of the movement using panel data analysis. Further, we evaluate whether the impact of the antecedents on retweet influence changed depending on the content and context of tweet conversations.

This study is among the first to explore “sustained influence” on Twitter spanning a social movement in the context of a social crisis through a panel analysis of Twitter data. The contributions of this study are fourfold. First, this study analyzes an underaddressed area of social movement mobilization networks—“informal constellations of mobilizing structures” (van Stekelenberg and Klandermans 2010; the advent of online social media like Twitter has enabled the study of such networks. Second, this study shows that the concept of duality of social action and facilitating structures as drivers of mobilization influence hold in the case of informal virtual networks like Twitter. Third, in contrast to much of the crisis research in the traditional social science domain that uses small-scale selfreported data through surveys, polls, and laboratory experiments, we use a large-scale empirical approach to capture natural, organic and societal field data.<sup>3</sup> To extract social movement context-specific variables from a largescale dataset, we use a hybrid mixed methods approach involving machine learning and human coding. This method enables the identification of features of the text that are difficult to capture using pure machine learning techniques and does not require the manual coding of large datasets. Finally, the content analysis of the organic tweets also affords novel ways of examining how the subcontexts and the sentiments associated with these subcontexts play a role in the unfolding of social action and network structure.

The paper is organized as follows. The next section highlights the background of the Egyptian Revolution of 2011 and presents a literature review. Subsequently, we detail the hypotheses, methodology, data collection procedure, and findings from our data analysis. Finally, in our conclusion, we offer some avenues for future research.

## Background and Prior Research

Social media, and especially Twitter, played an important role in the Arab Spring social uprisings (Duffy et al. 2011). In 2010, during the early part of the Arab Spring movement, Twitter users influenced the social movement by catalyzing angry citizens to gather on the streets, eventually leading to the overthrow of the Tunisian ruler. Leveraging this momentum and the power of interconnection through ICTs, protests erupted on January 25, 2011. These protests provided fuel for democratic and anti-dictatorial demonstrations against President Mubarak in the major cities of Egypt. Tahrir Square became the center of some of the most intense protests in Cairo. Some important events related to the Egyptian Revolution social movement are presented in Table 1.

## Prior Research

Social movements generally arise because of a desire or need for change (Turner and Killian 1957). Movements may be sparked by a significant event (Conell and Cohn 1995), which may cause goals to shift and change the orientation of discussions. This phenomenon was observed in the Arab Spring movements, with Tunisia sparking the “big bang” inspiring subsequent movements (Attia et al. 2011; Los Angeles Times 2011).

Some researchers<sup>4</sup> examining the 2011 Arab Spring social movements have argued that collective social behaviors cannot be understood in separation from a deep understanding of how people use ICTs. Street et al. (2015) used web search history data for the 2012 presidential election to measure citizens’ interest in voter registration. Oh et al. (2015) presented empirical evidence showing that the collective use of Twitter’s hashtag contributed to shaping collective sensemaking processes for collective action during the 2011 Egyptian Revolution.

<table><tr><td colspan="2">Table 1. Important Intervals in the Egyptian Revolution</td></tr><tr><td>Significant event</td><td>Description of the event</td></tr><tr><td>The “Day of Revolt,” January 25, 2011</td><td>Protests took place in major cities across Egypt. The demands of the protest included the resignation of the minister of interior, the need for fair minimum wage, the end of emergency law, and term limits for President Mubarak. Twitter access was blocked by the government, but the block was withdrawn the next day. The protesters numbered in the tens of thousands.</td></tr><tr><td>The “Friday of Anger,” January 28, 2011</td><td>Intense protests in Cairo, specifically in Tahrir Square, which included opposition party leaders. The protesters numbered in the hundreds of thousands.</td></tr><tr><td>“Battle of the Camel,” February 2, 2011</td><td>Mubarak groups attack the protesters of “March of the Millions” which was organized on February 2, 2011. Protesters numbered in the millions.</td></tr><tr><td>The “Friday of Departure,” February 11, 2011</td><td>Intense protests despite President Mubarak’s offer of resignation forced him to resign the same evening.</td></tr></table>

In another direction, computational social science researchers have suggested examining individual and collective behaviors through large-scale data-driven approaches (Lazer et al. 2009). Table A8 in the Appendix summarizes computational social science studies related to social movements. Social science literature has also examined social media during the Arab Spring movement. Eltantawy and Wiest (2011) called for an examination of social media as an important aid for collective action and the organization of contemporary social movements such as those occurring in Egypt in 2011. They urged researchers to rethink the theory of resource mobilization. Khamis and Vaughn (2011) analyzed the Egyptian landscape to better understand the characteristics of the revolution itself. The study concluded that, in the case of Egypt, the point of departure was popular grassroots activism, rather than formal institutions or organized political parties, and thus call for research representing this nature of revolution. Other researchers have explored political communication and framing theory, which, along with resource mobilization, form the trio of major theories of social movements (McAdam et al. 1996; Pichardo 1997—see Table 2). Political communication theory focuses on the broader context of political structure or the circumstances surrounding a political landscape (Tufekci and Wilson 2012) and deals with the human-centric aspects of social movements. Framing theory deals with how actors (of a movement) communicate about reality, emphasizing the content of what is being communicated, thus leaving less scope for the role of technological artifacts. Table 2 summarizes the literature.

## Resource Mobilization Theory

Resource mobilization theory (RMT) was one of the earliest sociological theories to focus on structural processes and movement activity (Jenkins 1983). Prior schools of thought established that a collective need for change, shared grievances, and beliefs are necessary preconditions for a collectivity to emerge as a social movement (Turner and Killian 1972). However, the extent and intensity of grievances usually increase prior to the social movement phenomenon and are related to a great extent to the political scenario (McCarthy and Zald 1977), as in the case of the 2011 Arab Spring movements. The basic premise of RMT is that collective action not only occurs because of discontent or grievances but also due to structural factors. A significant portion of RMT research focuses on the social movement organization (SMO) perspective. Participants can be either affiliated or unaffiliated with an SMO. Studies have shown that almost half of participants are not affiliated with such organizations (Klandermans et al. 2014). Affiliated participants would be more likely to identify with organizers, while unaffiliated participants would be more likely to identify with other participants, thus lending themselves to sparse networks like those observed on Twitter, an open channel. For the purposes of this study, we do not assume that Twitter is a milieu of social movement organizations; rather, we focus on the view of individuals forming smaller constellations of informal mobilization/participation structures. This assumption is more pertinent to the context of the Arab Spring because mainstream media and most forms of communication were supervised by the regime against which protests were made (White et al. 1996; Yang 2003). Many informal social groups have used websites and social media to form and develop their networks (Xue et al. 2016). These ICTs have provided citizens with access to information, exposed them to alternate political agendas, and helped reduce the cost of mobilization.

Advances in the social movement literature have introduced a new perspective on viewing social actions: earlier research focused on formal organizations for mobilizing activities, while recent work also discusses the concept of mobilizing structures (Smith and Fetner 2010). Many studies in the resource mobilization literature have explored social movement organizations (SMO), which are formal organizations that are structured and cohesive (Selander and Jarvenpaa, 2016).

<table><tr><td colspan="5">Table 2. Literature Survey</td></tr><tr><td>Author</td><td>Title</td><td>Data</td><td>Method</td><td>Theory base</td></tr><tr><td>Khamis (2011)</td><td>“The Transformation Egyptian Media Lands: Changes, Challenges and Comparative Perspectives”</td><td>No</td><td>Anecdotes</td><td>None</td></tr><tr><td>Eltantawy and Wiest (2011)</td><td>“Social Media in the Egyptian Revolution: Reconsidering Resource Mobilization Theory”</td><td>No</td><td>Theory review</td><td>Resource mobilization</td></tr><tr><td>Wilson and Dunn (2011)</td><td>“Digital Media in the Egyptian Revolution: Descriptive Analysis from the Tahrir Data Sets”</td><td>Survey</td><td>Descriptive</td><td>None</td></tr><tr><td>Lim (2012)</td><td>“Clicks, Cabs, and Coffee Houses: Social Media and Oppositional Movements in Egypt, 2004-2011”</td><td>Anecdotes</td><td>Secondary anecdotes</td><td>None</td></tr><tr><td>Tufekci and Wilson (2012)</td><td>“Social Media and the Decision to Participate in Political Protest: Observation from Tahrir Square”</td><td>Survey</td><td>Logistic regression</td><td>Political communication</td></tr><tr><td>Papacharissi and Oliveira (2012)</td><td>“Affective News and Networked Publics: The Rhythms of News Storytelling on #Egypt”</td><td>Twitter</td><td>Descriptive discourse analysis</td><td>None</td></tr><tr><td>Hamdy and Gomaa (2012)</td><td>“Framing the Egyptian Uprising in Arabic Language Newspapers and Social Media”</td><td>Secondary news articles</td><td>Content coding and analysis</td><td>Framing theory</td></tr></table>

Other studies, such as Flanagin et al. (2006) have explored the collective action aspect of resource mobilization theory. Resource mobilization theory also deals with how a constellation of key players/groups in an informal network of actors strive to promote social change by aligning their interests and issues (McAdam et al. 1996; McCarthy and Zald 1977). However, this aspect of resource mobilization is understudied partly because of the scarcity of means to observe such phenomena. Since we are interested in the technohuman aspect of social movements on Twitter (i.e., the influential users on Twitter in the context of a social movement), we use mobilization theory as a lens for our study and adapt it to Twitter. We focus on how the constellation of key players who are movement actors (humans) utilize IT artifacts to mobilize people toward accomplishing their goals. The use of specialized hashtags directing messages to specific entities has been made possible by the use of an IT artifact (the Twitter platform) and allows mobilization. A new generation of online opinion leaders and self-organized participants has emerged in contrast to the formal leadership and organizations emphasized in classical collective action theories (Earl 2013; Sheng and Gao 2013; Svensson 2014). Nevertheless, a root cause remains shared grievances.

To summarize, this paper focuses on mobilization and informal activism as opposed to formal institutions. We do not adopt the perspective of individual personality traits; rather, we deal with social action and mobilizing structures as the crux. We also address the aspect of framing in this paper by characterizing collective social action into specific frames. We perform a multimethod content analysis to incorporate the prominent contexts (frames), explained in later sections.

## Social Media Service

ICT’s can be effective tools in many social contexts including extreme events (Vaast and Walsham 2013; Chou et al. 2011; Valecha et al. 2019). Social media platforms have been the focus of recent studies on social movements (Della Porta and Mosca 2005; Langman 2005; Wasserman 2007; Ghannam 2011; Fu et al. 2014). In fact, Lim (2012) argues that social media affords movement leaders a means to report, frame issues, and effectively fuel online activism. Eltantawy and Wiest (2011) explain how the resource mobilization theory can be considered in analyzing social media’s role in the Egyptian Revolution social movement. Maghrabi and Salam (2011) explain the role of social media as a means of establishing and maintaining stable ties, creating a collective identity, and providing a platform for resource mobilization. Mobilization of participants unaffiliated to any SMO’s is likely to be achieved by engaging ideologically rather than instrumentally (Klandermans et al. 2014). As discussed by Schmidt and Cohen (2013), new technological artifacts such as Twitter have changed the way that protestors operate. Mechanisms such as retweets, mentions, and hashtags allow influence to be propagated more effectively, which may not have been possible on large societal scales earlier. Our research broadly follows and extends the prior literature.

Twitter is one of the most popular microblogging social networking web services (Williams et al. 2009) in the world. It is primarily used for the exchange of short messages about daily activities and to share and obtain information (Java et al. 2007; Bachura et al. 2017). This provides a favorable environment for users seeking to form and spread opinions. Users are able to immediately broadcast anything to the world with any computer or cell phone with internet capabilities (Valecha et al. 2016).

Other social media services such as Facebook would also be good platforms to study. However, we focus on Twitter in this study for several reasons. First, Twitter messages are limited to 140 characters.<sup>5</sup> This restricted character count makes Twitter better suited for the dissemination of information through mobile phone users. Also, Twitter is almost always public, unless a user explicitly makes a message private. Facebook, in contrast, enforces reciprocal ties—i.e., “Friends.” Twitter is more of a “push” type of social media, which lets users know about news on trending topics. Handles such as hashtags enable more focused communication. Moreover, “following” mechanisms enable a user further to focus on information that is relevant to them that is broadcast by those who they follow (Tsur and Rappoport 2012). Furthermore, Twitter offers a realtime flow of information and a massive reach. Moreover, a few other studies (Maghrabi and Salam 2011; Maghrabi 2017; Howard et al. 2011) have already explored the roles of Facebook and other social media in the social movement context.

The Twitter platform consists of four important components that help in communication—namely, hashtags, mentions, retweets, and following. The retweet is a technological feature that is analogous to message forwarding (Volety et al. 2018). Twitter users use this feature to forward messages—typically retweets contain the prefix “RT” and credit the original tweeter using the @ symbol. The Twitter hashtag is a set of characters prefixed by the symbol #, which acts as a topical marker. This string of characters identifies a user-provided context that can be used by any other users to express similar ideas in their tweets (Tsur and Rappoport 2012). Following is a nonreciprocal mechanism that a user can use to subscribe to another user’s feed. The Twitter mention is a mechanism users can employ to tag other users in a conversation. The mention mechanism uses a username to direct a message to that individual. It may also be viewed as an invitation to join a conversation.

## Social Influence

Retweets carry many conversational aspects; they signify authorship, attribution, and communication fidelity, which present themselves in different ways (Boyd et al. 2010). Many studies have addressed retweets as a measure of social influence. Social influence on Twitter has been widely studied in the literature (Goyal et al. 2010; Kempe et al. 2003; Dholakia et al. 2004). Motivations to retweet could be multifold, ranging from engaging a specific audience, to commenting on a tweet’s content, agreeing with someone, or even saving the tweet for future reference (Stieglitz and Dang-Xuan 2013). While there is much literature on social influence in collaborative settings, the literature on social influence in the context of social movements is sparse. For instance, Hertel et al. (2003) and Schroer and Hertel (2009) focus on collaborative software development and knowledge creation; Arazy and Gellatly (2013) and Butler et al. (2007) deal with online leadership in the context of listservs and knowledge management systems, while Kraut et al. (2010) touch upon technology-mediated social participation. Gergely and Rao (2014) focus on social influence in the case of software piracy. However, none of these studies investigate social movements. In this study, we develop a comprehensive perspective that examines the roles of user-, message- and network-related factors and examines the social movement as a manmade, unplanned, extreme event.

## Retweets

Twitter messages can be construed as synonymous with message forwarding or, to some extent, as a citation network (Weller et al. 2011). Tweets facilitate a conversation among actors irrespective of supporting or opposing opinions regarding the content. For example, in the research contest, one article (A) may cite another article (B). Article A may either strengthen or draw support from the notions of B or oppose the notions of B. Similarly, when a Twitter user retweets in opposition to another tweet, the retweet is usually accompanied by a quote from the original tweet—i.e., User A tweets some information that User B believes is not true. User B can retweet User A’s original tweet with a quote from User A’s tweet that User B then declares to be “not true.” However, even in such cases, a retweet could indicate a measure of influence. In any case, participants often engage at an ideological level during the process of retweeting, thereby contributing to the process of mobilization. Starbird and Palen (2012) show specifically how retweet behavior can be used as an indicator of new and important messages in a politically sensitive crowd interaction network like Twitter (Papacharissi and Oliveira 2012).

In this paper, in order to measure influence on Twitter in the context of the Egyptian Revolution social movement, we focus on retweets and following. The basic difference between them is that retweets are essentially a forwarding mechanism that can be construed as a means of sharing information that a user thinks is worthy of sharing. In addition, retweets also cite the author of the original tweet using the symbol @. This indicates the influence of the tweet as well as that of the username attributed to it. As far as following is concerned, the decision to follow a user likely stems from the desire to subscribe to the user’s feed, indicating the influence of individual users.

We use (sustained) retweet influence as the dependent variable and measure the influence by the number of retweets a username (tweeter) receives over the span of the social movement. We assume that a retweet essentially signifies the worthiness of the original content. Therefore, we attribute a tweet’s retweet worthiness to either the message itself or to the worthiness of the original author (username), as indicated by the following tweet:

“RT @shabab6april: A RevolutionaryPretty kid’s smile invites u 2 #Jan25 #revolution in #egypt. Join her #Now http://on.fb.me/RevolutionKi ...”

Presumably, the retweeter chose to forward this content because it was deemed important.

In retweet networks, Twitter User A may not be connected to Twitter User B, but User B may retweet User A’s tweet because of its content. Therefore, retweets do not necessarily imply any connection between two individuals. However, in following networks, Twitter users who follow each other are connected, and it may not be possible to directly attribute the following to the context of a social movement. Users who are followers of another user do not necessarily exchange movement-related tweets among themselves and may tweet independently. In contrast, mention networks are entirely constructed by the connections among the users concerned within the relevant context. Therefore, for the purposes of this paper, we chose to focus on the mention network for analysis.

## Model Development

Research on the dynamics of social influences is scant. Mason et al. (2007) review the different models of social influence processes from a number of fields (though not in the context of a social movement). They suggest that “the goal [of this type of research] is to encourage interdisciplinary collaborations to build models that incorporate the detailed, micro-level understanding of influence processes contextualized in ways that recognize how multidirectional, dynamic influences are situated in people’s social networks and relationships” (p. 279). Specifically, Mason et al. suggest that, because real-world connections among individuals are most adequately characterized as networks, the most appropriate models for social influence will typically be dynamic networks, and researchers should think of influence not as a phenomenon that occurs at a single point in time but as one that has an extended time course.

Individual mobilization action can be measured in terms of the participants’ engagement activity (Bennett and Segerberg 2011), which can be linked to movements and can help tie ideas together, disseminate ideas, and lead to shifts in a protest movement (Grundberg and Lindgren 2015). The notion of frames can be useful in interpreting the engagement activity of participants as they engage in constructing the vocabulary of motives in the struggles and structures of a movement. Because they facilitate the analysis of information in a unique context and enable emphasis on certain elements of the context, frames are important for understanding influence (Pan and Kosicki 1993).

Apart from individual activity, mobilizing structures play an important role in facilitating activity (Garrett 2006) and mobilizing structures (King 2008). A favorable network structure provides individuals with a greater capacity to access and mobilize resources within a network (Lin 2008). Factors such as past experience, network structure, and engagement strength translate into influence potential (McAdam 1986; Lin 2002).

To summarize, ICTs can be viewed as instruments that afford the formation of mobilizing structures (Earl and Kimport 2011). In this paper, we analyze the role that one such ICT, Twitter, has played in supporting the online activities of a social movement. The mechanisms of following and centrality are facilitated by network structures, while the activity and tenure of a user can be construed as characteristics of individual social action on Twitter. We are interested in finding out whether these mechanisms also translate into the potential for influence, similar to traditional social movement communication (Mcadam 1986; Lin 2002).

We analyze sustained social influence over the span of the social movement. Social influence is often regarded as a dynamic process (Zhang et al. 2011). According to Cha et al. (2010), influence on Twitter is not gained spontaneously. The social influence of the user is acquired through a concerted effort in a specific context over a period of time. Moreover, the influence of the content of a tweet (message) requires some amount of time to propagate and manifest itself in the form of retweets. Clearly, it is important that the temporal aspects of influence are taken into consideration in a setting like Twitter. We assume that the social influences of the interpersonal interactions in our study that manifest in the form of retweets occurred in a subsequent time period and are not instantaneous. Social action is facilitated by underlying mobilization structures. These structures provide participants with mobilization potential by easing the process of mobilization (Eltantawy and Wiest 2011). When a user tweets, the effort needed to reach a potential audience is reduced if the user is highly central at that point in time. Likewise, if followers have subscribed to the user, the dissemination of messages is made easier. In this way, social influence is facilitated concurrently by the mobilization structure.

In summary, the two important constructs of RMT—social action and mobilization structures—form the basis of our model (refer to Figures 1a and 1b). In line with the above arguments, we posit that the effect of social action on social influence takes place in subsequent time periods (see H1 and H2), resulting in lagged variables, while the effect of mobilization structure on social influence takes place within the time period examined (see H3 and H4), resulting in unlagged variables for our model.

Mobilization structures are well orchestrated in social movement organizations (SMOs) in the form of organizational channels, affiliated members, and their associated networks. However, in the case of grassroots movements, where SMOs are not tenable, a more organic network of protestors can be built through open channels. There are countless recent examples of social media platforms like Twitter affording anonymous formation of such informal structures. Networks have become a prominent means of facilitating structure, which is reflected in our model in the form of two variables—centrality and follower count. Our social action construct is represented by four activity variables, detailed as follows.

## User Activity

Recent years have seen a rise in interest in maximizing participation in social networks as an attempt to increase social influence (Fang et al. 2013; Goyal et al. 2010; Kempe et al. 2003; Dholakia et al. 2004). In the case of the Egyptian Revolution movement examined here, the influential users essentially needed to mobilize Egyptian citizens toward the goals of the movement, one of which was to overthrow President Mubarak. In order for mobilization to occur, protesters must demonstrate sustained participation in activities related to the movement (van Stekelenberg and Klandermans 2010). This also ensures their continued engagement in the social movement and is evidenced by individuals motivated to participate (e.g., through tweeting) in social movements for the purpose of furthering a collective good in conjunction with other participants (Klandermans 1984).

For social action to be successful, it has to be conducted en masse, i.e., as a group action. This implies that a social movement requires individuals to engage in protest activities with other individuals (Lohmann 1994). The RMT literature breaks the process of mobilization action into four main action frames (Klandermans and Oegema 1987), which we expound upon here in the context of the Egyptian Revolution: (1)

sympathizing with the cause (who and what—e.g., dictator and freedom), (2) the protester’s need to know about (location of) the events (where—e.g., Tahrir Square), (3) wanting to participate (how—e.g., protest), and (4) being able to participate, which is enabled by Twitter intrinsically by removing barriers to participation. In the words of Xue et al. (2016, p. 7), “this framework of mobilization can also be applied to online activism, whose mobilization process includes: forming shared grievances among the public, framing an appealing goal, reaching as many participants as possible, and conquering barriers to take action.”

Individuals wanting to protest must coordinate their protest activities with others; such activities also require a common goal that focuses on bringing changes to society (regarding what and who) and must converge in time (when) and space (where) (van Stekelenberg and Klandermans 2010; Bennett and Segerberg 2011). In other words, social protest activities are characterized by the frames of what, how, where, and who. In the Egyptian Revolution, protests (White et al.) were targeted at protecting citizens’ freedom (what) against the dictator Mubarak (who) and the largest protests took place in Tahrir Square (where) (Steinert-Threlkeld et al. 2015). In this context, the what and who map to the frames of sympathizing with the cause and expressing a desire to participate. The how and where map to the protestor’s need for information about the events. We posit that there is a positive association between participation in who, what, how, and where activities and social influence, hypothesizing:

H1: The level of activity of Twitter users regarding (a) “who” (dictator), (b) “what” (freedom), (c) “where” (Tahrir Square), and (d) “how” (protest) positively affects their retweet influence in the subsequent time window.

## Tenure

One important aspect of users in an online community is how long they have been engaged in the community. In the case of online communities, users tend to have different degrees of experience in terms of the time they have spent in a particular context. The advantage of longer online use is that users tend to build social capital (Ellison et al. 2007), which allows users to harness resources such as information and organizing capacity through other network members. Increased social capital may increase commitment in community activities (Musembwa and Paul 2012) and the potential for mobilizing collective actions (Paxton 1999). In fact, individual social action has been shown to be influenced by protesters’ past experiences (McAdam 1986).

Lampe and Johnston (2005) studied the behavior of users in an online community in different phases of their tenure. They found that new users were more likely to receive information by observing other members or through feedback from other members. Relatively new users were inclined to participate passively in the network largely to gain information. More experienced users tended to contribute more to the online community by harnessing their experiences. These findings suggest that the extent of experience of a user (tenure) in an online community has a positive impact on their community behavior. In our study, users’ tenure is measured by their earliest point of participation (tweeting) in the specific context of the Egyptian Revolution on Twitter. Essentially, the users who began their activities related to this movement earlier would be expected to accrue more experience in the community, which would position them to exert more influence on Twitter. Therefore, we hypothesize that in the social movement context,

H2: The tenure of Twitter users positively affects their retweet influence in the subsequent time window.

## Following

We suggest that the following concept is not only a means to establish connections on Twitter, but also a way to subscribe to the feeds of users of interest. The relationship is directional and not necessarily reciprocal. Basically, the number of followers a user has can be a measure of in-degree (the number of head points adjacent to a node or individual) for the individual (Lotan et al. 2011; Ye and Wu 2010). However, a user being followed by thousands of users—e.g., in the case of celebrities or media personnel—may not necessarily make an impact in spreading opinions in the social movement context if their messages are not relevant to the topic. Therefore, the following mechanism is important to the context of the study.

The social capital that a user gains over a period through the following mechanism can be leveraged by that user in real time. From the perspective of the social movement, a user with a high number of followers would be expected to have a broader reach. Bakshy et al. (2011) found that influential users are those who already have more followers. This positive association has been supported in the literature (Suh et al. 2010; Lerman and Ghosh 2010; Krishnamurthy et al. 2008). Therefore, in the social movement context, we hypothesize that the number of followers a user has a positive effect on retweet influence within each time window:

H3: The number of followers a Twitter user has positively affects that user’s retweet influence.

## Centrality

Although we are dealing with mobilizing structures that pertain to informal constellations of actors, social scientists argue that without some effort to organize, no movement can mobilize a sustained flow of energy toward social change efforts (van Stekelenburg and Klandermans (2010). Increasingly, researchers in the field of social movements have used the term “networks” to characterize relationships among movement entities, be it individuals, small groups, or organizations. Therefore, the process of mobilization is not singular but involves some degree of formality and centralization. In the absence of a hierarchical structure, as in the case of informal networks, identifying these centralized entities becomes more important.

Extant studies (though not in the context of social movements) have identified and characterized influential users in different contexts in online social networks (Goyal et al. 2010; Hajian 2011; Hajian and White 2011; Trusov et al. 2010). Network structure has also been found to play an important role at the organizational level, impacting the competitiveness of IT-enabled firms (Chi et al. 2010). Since the early experiments on network structures by Bavelas (1950) and Leavitt (1951), the body of literature on centrality measures and their impacts has expanded. Freeman (1979) explored the mathematics of centrality measures, their conceptual meanings, and their impacts on group problem solving. Measures of centrality have been associated with a specific role of the node (also known as vertices) in a network. Thus, the relative position (centrality) of a node in a network can determine the influence of the node (Freeman 1979).

In our study, we consider the Twitter communication network with users as nodes/vertices and mentions and retweets as the edges. We focus on eigenvector centrality in the mentions+retweets network, a measure of the influence of vertices or nodes in the network (Bonacich 2007). This measure is based on relative scores that are assigned to networks on the basis of connections to high-scoring nodes (or Twitter users in this case) that are believed to contribute more to the score of the node in question than connections to low-scoring nodes. A key distinction between eigenvector centrality and betweenness centrality, which influenced our decision to include eigenvector centrality in the model is illustrated by the following example: If a User A posts four mentions and five retweets of User B, betweenness centrality captures the connection between User A and User B while ignoring the counts. Eigenvector centrality, however, considers the counts. Another measure that accounts for the counts is degree centrality. Eigenvector centrality is more appropriate than degree centrality because the latter only captures the number of connections in the network and does not account for the quality of the node’s connections. In terms of retweet worthiness, tweets related to users with high eigenvector centrality may carry value because of the relative importance of their connections. For example, User A may only have 10 connections, but those 10 connections may have a very high degree in the network, which makes User A very influential. From a social influence point of view, these nodes may or may not have direct control over information flow. However, they may acquire “identification” because of the attractiveness of the central nodes that mention them. The fact that a user may reap the benefits of high centrality in terms of the number of retweets in real time is noteworthy. Therefore, we hypothesize that in the context of the Egyptian Revolution, the eigenvector centrality of users in the Twitter network will have a positive effect within each time window:

H4: The eigenvector centrality of Twitter users in the Twitter network positively affects their retweet influence.

## Previous Influence

Having considered the effect of different factors that affect Twitter influence, we argue that the Twitter influence of the users, measured by the number of retweets received by others in a given time window, affects their influence in the subsequent time window. This is an indication of sustained influence over time. Steinfield et al. (2008) show that the social capital and the positional advantage gained in the online social network structure and their influence have longitudinal relationships in the case of Facebook networks. We know that users tend to gain influence in an online community over a period of time (Ellison et al. 2007). Similarly, the potential for collective action and mobilization increases as the commitment of the users’ increases (Paxton 1999). When protesters gain influence, it potentially increases their embeddedness with the community and their commitment to the community goals (Kelman 1958; 1961). Crandall et al. (2008) demonstrated that a feedback effect of social influence processes in online communities does exist. Kempe et al. (2003) also showed that the social influence process in a social network can progress over time. In a similar vein, we expect that the retweet influence of Twitter users in a given time window also has an impact on their retweet influence in a subsequent time window within the context of this study. We thus hypothesize:

H5: The retweet influence of Twitter users in a given time window positively affects their retweet influence in the subsequent time window.

Several other studies have shown retweet influence is also impacted by a number of other factors on Twitter such as tweeting habits and URL use habits (Stieglitz and Dang-Xuan 2013). Twitter users often choose to follow other notable users with similar tweeting habits in order to gain real-time news updates (Suh et al. 2010). In particular, Twitter users who tweet frequently as captured by the status feature on Twitter (Suh et al. 2010) may get retweeted frequently (retweet count). Furthermore, URLs have been shown to improve the contextualization (or believability) of a tweet. Twitter users provide links to outside content by including URLs in their tweets (Boyd et al. 2010). Therefore, we included tweeting (status) and URL use (presence of URL) in the previous time window as activity control variables. Furthermore, the time period may also have an impact on retweet influence. We found more retweet influence in later time periods. Therefore, we added the time period as a control variable in the model. Figures 1a and 1b presents our conceptual mixed-lag model of user influence on Twitter.

$$
\begin{array}{r l} & L n \left(R e t w e e t I n f l u e n c e _ {i, t}\right) = \beta_ {0} + \\ & \beta_ {1 a} A n t i D i c t a t o r A c t i v i t y _ {i, t - 1} + \\ & \beta_ {1 b} F r e e d o m A c t i v i t y _ {i, t - 1} + \\ & \beta_ {1 c} T a h r i r S q u a r e A c t i v i t y _ {i, t - 1} + \\ & \beta_ {1 d} P r o t e s t A c t i v i t y _ {i, t - 1} + \beta_ {2} T e n u r e _ {i, t - 1} + \\ & \beta_ {3} L n (F o l l o w e r C o u n t _ {i}) + \\ & \beta_ {4} E i g e n v e c t o r C e n t r a l i t y _ {i, t} + \\ & \beta_ {5} R e t w e e t I n f l u e n c e _ {i, t - 1} + \beta_ {6} L n (S t a t u s _ {i, t - 1}) + \\ & \beta_ {7} U R L _ {i, t - 1} + \beta_ {8} t + \varepsilon_ {i, t}, \end{array}\tag{1}
$$

where t represents the time window of the protest.

To summarize, we consider retweet influence at a particular time window (t) to be a function of characteristics of (1) an individual Twitter user’s social action in the previous time window (t-1), (2) their underlying facilitating structures within each time window (t), and (3) their prior influence in the previous time window (t-1). The anti-dictator, freedom, Tahrir Square, and protest activities of Twitter users represent the who-what-how-where components of individuals’ social action, while the tenure of Twitter users represents the participation component of individuals’ social action. The eigenvector centrality and the number of followers represent the characteristics facilitated by the structures of the Twitter network. We also consider the effect of the social activity-related control variables, status, and presence of URLs (in previous time window), and time period on retweet influence.

![](/api/attachments/J6V2QKA7/fulltext/images/dce3bb1c63122ccca085a1b6952555ca3235294e1058581ea913515127adeb10.jpg)

![](/api/attachments/J6V2QKA7/fulltext/images/29502bb7c0212c4acc764e832385c5054e05b0ad41ca9644083e2bf287746d37.jpg)  
Figure 1b. Conceptual Model: Extension of Social Movement to Twitter Verse

## Data Description

The data consist of tweets related to the 2011 Egyptian Revolution. The easiest way to collect these tweets is by means of a keyword search using the Twitter SEARCH API (Application Programming Interface), which allows third parties to download the data. However, we were constrained by the fact that Twitter provides access to indices of posts (at best) up to seven days or up to 1500 tweets at one time (a more recent restriction). Thus, we could not obtain the entire set of indexes through mere keyword search. Thus, we were forced to choose an alternative way of tracking the tweets. We chose the REST API instead of the SEARCH API, which has fewer limitations on data collection. We gathered our data using the following steps: First, we collected the tweets from the REST API. Second, we recorded the user IDs within the tweets. Then, using the user IDs as a lead, we traced the entire set of tweets by the users using the SEARCH API. Through this process, we identified 50,778 users who tweeted or retweeted 1,915,429 messages.

Finally, we removed tweets not relevant to the context of the 2011 Egyptian Revolution, i.e., we cleaned the dataset as follows: First, since not all the messages were related to the Egyptian Revolution, we filtered out messages that did not include “Egypt” in the messages. We also checked the topical relevance of tweets using random and multiple protests and social movement-related keywords (including hashtags), such as Mubarak, Egypt, Jan25, Tahrir, protest, revolution, etc. These keywords were identified after referring to media and Twitter. Second, we removed any tweets in Arabic (due to the lack of Arabic-language processing capability). Finally, we also removed users who did not participate in at least two time periods (details on time periods are provided in the next section). Out of a total of 1.9 million tweets that we collected during the event, the data processing and cleaning resulted in 95,794 retweets in a time period of 23 days from January 20 until February 12, 2011.

To explore the hypotheses, we constructed panel data of Twitter users and their interactions to analyze their Twitter influence. We considered retweets to be links between the users who tweeted the original message and the users who retweeted that message. For example, if a user named “Sarah Richani” retweeted this message: “RT @bencnn: Why all the uproar? Every day is police day in #egypt #jan25 #Tunisia,” we consider the retweet to be a link between the username “Sarah Richani” and username “bencnn.”

## Methodology and Analysis

As discussed earlier, we measured the influence of users as the number of times that their messages were retweeted in a certain time window. Retweets are a widely accepted measure of influence on Twitter (Cha et al. 2010). Retweets per tweet per user could also be used as a measure of influence, but in that case, we could not use a user’s activity as a predictor variable. Retweets can typically be identified by the use of RT @username or via @username in tweets. A tweet that starts with @username is not broadcast to all followers, but only to the replied user. A tweet containing @username within the text is broadcast to all followers.

The user’s tenure at each time window represents the previous number of time periods that the user was actively involved in tweeting about the Egyptian Revolution. Follower count represents the total number of followers that each user had (at the time of analysis). This directly indicates the size of the audience for that user. However, since it is impossible to capture follower count in each time period, we captured it at the end of the fourth time period. The eigenvector centrality in each time window was calculated based on the network of retweets and mentions and normalized to eliminate the effects of differences in size and density of networks in the previous time window

Status count and URL presence denote the respective tweeting and URL use habits of each user in the previous time period (t). Retweet influence is measured by the number of retweets containing the username. This indicates that the user generated content with pass-along value. We calculated the measures based on our dataset, which contained 2423 users that had at least one retweet in at least two of the time periods. We also standardized the measures for comparing them with each other.

## Coding Social Movement Activity

For coding social movement activity, we utilized a mixed methods approach consisting of human coding and machine learning. In order to code anti-dictator (who activity: the dictator) freedom (what activity: the purpose), and protest (how activity: the means) activity, we followed the steps for content coding and analysis suggested by Krippendorf (1980). For the content coding, we hired two students who were personally familiar with the events at the time of the social movement (they had family in Egypt). The authors were not involved in content coding. The propositions were not shared with the student coders, and the coders were not allowed to communicate with any of the other coders while coding. They were asked not to spend more than an hour each day coding the data in order to minimize coding errors due to fatigue.

In the pilot coding round, the students were asked to manually code the anti-dictator, freedom, and protest variables from sample tweet messages. The intercoding reliability for the two students on the anti-dictator, freedom, and protest variables was 0.849, 0.913, and 0.941, respectively. Each coder then proceeded to separately code the anti-dictator, freedom, and protest variables for a random set of 7,535 tweet messages. We ensured that the pilot sample data were excluded from the data sample. The variables were dichotomously coded according to whether the tweet messages conveyed the meaning of the variables or not (0 = not conveyed; 1=conveyed). The following tweet illustrates an anti-dictator activity: “DOWN WITH MUBARAK AND HIS THUGS!!! SOLIDARITY WITH THE PROTESTERS!!!! FREE EGYPT NOW!!!!! #JAN25 #TAHRIR”

For the purposes of coding anti-dictator, freedom, and protest variables for the remaining 88,259 tweets (after removing the 7,535 pilot tweets from the corpus of 95,794 tweets), we employed machine learning in two steps: (1) converting text to vectors, and (2) training, testing and predicting class labels. First, we utilized the tf-idf approach, which used the occurrence of terms (words) to relate tweets to anti-dictator and freedom concepts (Ramos 2003). The tf-idf approach generated a weight (as text features to represent each tweet) that was used to evaluate the importance of a term in a tweet with respect to the entire Egyptian social movement. We used the scikit-learn module<sup>6</sup> in Python to learn vocabulary from the training data (7,535 human coded tweets). Next, we applied a random forest algorithm, which uses decision trees to generate class predictions (Liaw and Wiener 2002). For prediction purposes, we considered voted classes of the individual trees with the majority vote on the prediction dataset (88,259 tweets).

We used the random dataset of 7,535 tweets as the training and testing set. Specifically, we created a random 90-10 split of the 7,535 tweets into 6,856 tweets (90%) for training and 679 tweets (10%) for testing. We used the dataset of 6,856 tweets was used for validation, and the dataset of 88,259 tweets for prediction. For training purposes, five decision trees were constructed using the training dataset (6,856 tweets). For testing decision trees, we used the testing dataset (679 tweets). The accuracy of the three variables (anti-dictator, freedom, and protest) was 0.988, 0.996, and 0.919, respectively. To validate decision trees for each of the three variables (anti-dictator, freedom, and protest), we employed 10-fold cross-validation<sup>7</sup> on the training dataset (6,856 tweets). The mean AUC for the three overall voting models (anti-dictator, freedom, and protest) was 0.73, 0.71, and 0.81 respectively. The AUC mean was much higher than the random prediction score of 0.50 (Heumann 2011), which suggests that the three overall voting models represent a reliable method of classifying social movement activity (anti-dictator, freedom, and protest). For further details on machine learning algorithms including additional performance metrics, see the Appendix.

## Time Periods of the Movement

The Egyptian Revolution was fast moving. The revolution largely took place over a time span of 23 days. Social media was a critical enabler. Therefore, sustained influence can be captured in the same time span. Of course, before January 25, small and large gatherings did take place including the “silent stands” movement (Ghonim 2012). However, the surge in movement activity, particularly on Twitter, was observed around January 25 and the tone of the tweet conversations before and after January 25 was considerably different. We investigated Twitter influence from the time the revolution was in full swing until President Mubarak was forced to resign, thus fulfilling the goals of the movement.

Generally, longitudinal studies have arbitrary time periods, such as hourly, daily, or weekly windows. Some studies use acceptable time periods within the domain of interest. However, since we do not have rich prior literature in the area of social media and social movements, we do not have established time periods to draw upon. Goes (2013) and Goes et al. (2014) point out that there is a dearth of studies that use a theoretical/logical basis for defining time periods in the panel studies, especially concerning studies that focus on social media data. Thus, to identify time windows for the panel analysis for sustained influence, we adopted an inductive reasoning approach, which focused on the data and allowed the data to drive the discovery of structural changes in tweet patterns. This led to the identification of movement periods.

We used the social movement literature (Hiller 1975) to ground our development of the time windows. Much of the prior literature views social movements through the lens of a stage model (Dawson and Getty 1929; King 1956; Smelser 1963; Helmes-Hayes 1994). Stage models typically have three or four stages, which are identified based on the differences over time regarding to social unrest, the existence of a collectivity and excitement, or increased mobilization. Generally, the final stage or climax of the movement is characterized by the achievement of the goals of the movement or the decline of the movement itself. Hiller (1975) focuses on the way that movement members participate in different stages of a movement. The transformation of social movements can be determined by noting the differences in the nature of participation at select intervals of time throughout the existence of the social movement. Hiller (1975) argues that the nature and type of participation in movements vary as the movement progresses and proposes that movements have multiple stages based on participants’ orientation toward the goals of the movement. The behavior of movement mobilizers in different time windows of a social movement can be studied in conjunction with this work.

We suggest that, if the role of the Twitter social media was significant for the Egyptian Revolution, then social movement activities would be reflected in the pattern of tweets. Therefore, we used the changes in the nature and type of participation as indicators for the critical points that delimit the different time windows, as recommended by Hiller (1975). These time windows offer a timeline for further analysis (Oh et al. 2015). Drawing from the broad underpinnings of Hiller (1975), we used a key aspect that defines a change in stage--movements have multiple time windows based on participation and this is marked by a change in the orientation of the movement. We argue that this may be demonstrated by the shift in topics of conversation on Twitter. Therefore, we explored whether the distinct time windows of the social movement would be reflected on Twitter in the form of structural changes.

We scanned news media (such as Al Jazeera, The New York Times, The Guardian, and CNN) to identify specific major incidents that might characterize the movement. Table 3 shows the major events in the time periods. In order to code the frames, we analyzed hashtags related to the Egyptian Revolution and selected hashtags that showed up en masse over the various time windows to determine the time periods of the social movement. Figure 2 shows the frequencies of retweets categorized by some of the popular hashtags over the study time period. However, we do not use these hashtags in the analysis (Equation 1). We observed several peaks in the Twitter patterns. Recalling the notion of identifying structural changes (Hiller 1975), we observed two distinct pattern changes. First, the change in the nature of participation is indicated by the steep rise in the number of retweets between Jan 24 and Jan 25, 2011. Second, this rise in participation can also be observed around the dates January 28, February 2, and February 11. The change in orientation of goals can also be observed in the hashtags that are dominant during the time window.

Essentially, both the nature of participation and orientation changed during these periods of the movement. Therefore, we suggest that January 25, January 28, February 2, and February 11 are key dates for the Egyptian Revolution. We consider (1) the period right before January 25, 2011; (2) the period after January 25 and before January 28; (3) the period between January 28 and February 2, 2011, and (4) the time period from February 11 on as four distinct time windows for our analysis of the social movement. Additionally, the number of retweeted users increases considerably in these four time periods (see Table 3). This evidence suggests that the Egyptian Revolution can also be identified on Twitter by the change in the nature of participation (tweeting) and the orientation of the goals of the movement.

To summarize, we divided the social movement into four time windows that broadly correspond to the time intervals seen in Figure 2. Breaking down the social movement into these meaningful time intervals or windows helped us understand the dynamics of the movement (Turner and Killian 1957; Helmes-Hayes 1994; Hiller 1975). We constructed a panel dataset to analyze the level of users influence in each time window as a function of their influence level and other network and individual characteristics in prior time windows.

Figure 3 shows the mean of social movement activities (antidictator, freedom, Tahrir Square, and protest) in different time periods. This allowed us to identify the important activities within different time periods. In the first two time periods, anti-dictator and protest activities dominated. In the third time period, anti-dictator and Tahrir Square activities were the most important. In the final time period, Tahrir Square activity piqued user interest surrounding the social movement.

## Analysis

The messages we collected were related to the Egyptian Revolution. We checked for correlation among the variables (see Table A1 in the Appendix). There were no serious concerns regarding correlations. In some cases, although the correlation coefficient was above 0.5, the variance inflation factor was below 3—i.e., well below the tolerance level of 10 (Freund et al. 2003). Contrary to findings in previous literature, we found the correlation between eigenvector centrality and log followers to be negative. One reason for this may be that eigenvector centrality is measured in time periods (as opposed to one cross-sectional measure). In other words, there may be cases where eigenvector centrality may be lower in latter periods for some users. So, we also measured the correlation between eigenvector centrality and followers in individual periods. The correlation was positive for time periods 1 (rho = 0.043; p > 0.05) and 2 (rho = 0.044; p < 0.05), and was negative for time periods 3 (rho = -0.007; p > 0.05) and 4 (rho = -0.045; p < 0.00).

This study evaluates the model of sustained influence in dynamic longitudinal research design with n = 2423 users over t = four time periods. Because of the dynamic nature of the research design, a dynamic panel data model with the difference generalized method of moments (GMM) estimator (Arellano and Bond 1991) was necessary (Goes et al. 2014). For the difference GMM estimator, we used the crosssectional time-series dynamic panel data (xtdpd) module in STATA, which is well suited for panel datasets with a small number of time periods and a large sample size. The estimation of the difference GMM consists of two equations. The first equation transforms all regressors by differencing, while the second equation uses the obtained estimates as instruments to estimate the original regression model (Roodman 2008).

<table><tr><td colspan="3">Table 3. Number of Retweets in Important Time Windows in the Egyptian Revolution</td></tr><tr><td>Time interval</td><td>Significant event</td><td>Number of retweeted users</td></tr><tr><td>Before January 25, 2011</td><td>The “Day of Revolt” on January 25, 2011</td><td>177</td></tr><tr><td>January 26 – January 28</td><td>The “Friday of Anger” on January 28, 2011</td><td>9412</td></tr><tr><td>January 29 – February 2</td><td>“Battle of the Camel” on February 2, 2011</td><td>17540</td></tr><tr><td>February 3 – February 11</td><td>The “Friday of Departure” on February 11, 2011</td><td>37650</td></tr></table>

Frequency of Retweets for Each Context  
![](/api/attachments/J6V2QKA7/fulltext/images/2a1ce9daaeb15d22ae2106b52a228030b098881696d6661d1e13a3aab288a5a6.jpg)  
Figure 2. Frequency of Retweets for Each Category of Hashtags during the Egyptian Revolution

![](/api/attachments/J6V2QKA7/fulltext/images/a8b62bfc52e8656468ac400012f45bd14d8ad48e5780708e4e559752869dfaf4.jpg)  
Figure 3. Activity Differences in Time Periods

<table><tr><td>DV: retweet influence t</td><td>Coefficient</td><td>Robust std. error</td><td>Odds ratio</td><td colspan="2">95% confidence interval</td></tr><tr><td>Intercept</td><td>1.706***</td><td>0.288</td><td>NA</td><td>1.142</td><td>2.270</td></tr><tr><td>Anti-dictator activity i, t-1</td><td>0.304*</td><td>0.125</td><td>1.355</td><td>0.059</td><td>0.549</td></tr><tr><td>Freedom activity i, t-1</td><td>0.111</td><td>0.293</td><td>1.117</td><td>-0.463</td><td>0.686</td></tr><tr><td>Tahrir activity i, t-1</td><td>0.325*</td><td>0.164</td><td>1.384</td><td>0.004</td><td>0.646</td></tr><tr><td>Protest activity i, t-1</td><td>0.060</td><td>0.089</td><td>1.062</td><td>-0.114</td><td>0.234</td></tr><tr><td>Tenure i, t-1</td><td>0.416***</td><td>0.043</td><td>1.516</td><td>0.331</td><td>0.502</td></tr><tr><td>Ln(Followers)</td><td>0.403***</td><td>0.044</td><td>1.496</td><td>0.316</td><td>0.489</td></tr><tr><td>Centrality i, t</td><td>0.522***</td><td>0.088</td><td>1.685</td><td>0.350</td><td>0.695</td></tr><tr><td>Influence i, t-1</td><td>0.163***</td><td>0.044</td><td>1.177</td><td>0.076</td><td>0.250</td></tr><tr><td>Ln(Status i, t-1)</td><td>-0.194**</td><td>0.071</td><td>0.824</td><td>-0.332</td><td>-0.055</td></tr><tr><td>URL i, t-1</td><td>-0.457***</td><td>0.123</td><td>0.633</td><td>-0.699</td><td>-0.216</td></tr><tr><td>t</td><td>-0.039</td><td>0.070</td><td>0.962</td><td>-0.177</td><td>0.099</td></tr></table>

Note: p-value < 0.10; \*p-value < 0.05; \*\* p-value < 0.01; \*\*\* p-value < 0.001

The difference GMM estimator can control for idiosyncratic data disturbances such as heteroskedasticity and serial correlation. The estimation of the difference GMM in STATA consists of a VCE(robust) option that provides the robust variance-covariance estimation procedure. It accounts for heteroskedasticity and is consistent with autocorrelation in our data. The difference GMM estimator with the robust variancecovariance procedure thus controls for endogeneity, unobserved heterogeneity, and omitted variables by creating GMM type instruments (Arellano and Bond 1991; Holtz-Eakin et al. 1988).

## Results

Using the GMM estimator in the xtdpd module in STATA, we estimated the effect of (1) activity (anti-dictator, freedom, Tahrir Square and protest) and tenure (in the previous time period); (2) eigenvector centrality and followers count (within each time period); (3) retweet influence (in previous time periods); and (4) tweeting, URL use (in previous time periods), and time period on sustained retweet influence (see Table 4). We followed Peng et al.’s (2002) guidance in reporting the results. We found that the anti-dictator activity of users in previous time windows has a significant positive effect on influence in subsequent time windows (H1a supported). The anti-dictator activity was one of the most reliable predictors of the user’s influence. In other words, for each unit of increase in the user’s anti-dictator activity, the expected log count of retweets increased by 0.304 units. In addition, the Tahrir Square activity of users had a significant positive effect on influence in subsequent time windows (H1c supported). This indicates that for each unit of increase in the user’s Tahrir Square activity, the expected log count of retweets increased by 0.325 units. Contrary to our expectations, we did not find a significant positive effect of freedom (H1b not supported) or protest (H1d not supported) activity on the user’s influence in subsequent time windows. Thus H1 is partially supported—i.e., the anti-dictator and Tahrir Square activity of users affected their influence in subsequent time windows.

Tenure in previous time windows captures the number of time previous time periods since the user started tweeting about the Egyptian Revolution. As shown in Table 4, tenure had a positive and significant effect on the influence of users. The variable of tenure has a co-efficient of 0.416, meaning that for each unit of increase in a user’s tenure, the expected log count of retweets increased by 0.416 units. This supports H2.

The number of followers is a positive and significant determinant of users’ influence. The number of followers is another reliable predictor of users’ influence. We found that every unit increase in the number of followers increased the log number of retweets by 0.403 units. This supports H3, which posits that the number of followers is positively associated with retweet influence.

Our results reveal that eigenvector centrality measured in the network of retweets and mentions is a driver of influence on Twitter. As discussed earlier, the eigenvector centrality in the network of retweets and mentions represents how often a user is retweeted and mentioned by users who are themselves frequently retweeted and mentioned. Every unit increase in centrality increased the log number of retweets by 0.523 units (Table 4), which supports H4’s prediction that users’ centrality increases their influence on Twitter.

We found that influential users continued to increase their influence (by 0.163 units) over time. This phenomenon is also represented by the continual increase in the size of the nodes of the retweet networks, as seen in Figure 4, which shows that the retweet in-degree (the number of retweets a user has garnered) increases over time. As time progressed and the social movement evolved, more users became interested in the subject and started retweeting messages pertaining to the specific subject. The users with higher influence in the preliminary time windows of the social movement had a greater chance of being influential in the subsequent time windows of the movement. This supports H5.

Some prior literature, although not related to social movements, has found minimal effects of the number of followers on influence (Cha et al. 2010). In contrast, our results show that the number of followers is a positive and significant driver of influence on Twitter. Our study also demonstrates the importance of activity (anti-dictator and Tahrir Square), tenure, and eigenvector centrality as drivers of Twitter influence. The effect of tweeting and URL use on the influence of users is significant and negative, while the effect of time periods is insignificant.

The four time periods used in the study provide context regarding users’ offline activities. For example, protest activity appeared to be more prominent in the first time period leading up to January 25 when the Tahrir Square protest took place, compared to the last time period leading up to February 11, shortly before Mubarak’s resignation. We verified this by checking the effect of running the analysis with some arbitrary time windows (instead of contextual peaks) on the fit of the model to the data. In order to test this, we divided the social movement into eight equally spaced time periods. Then we tested the model using the GMM estimator. The results (see Table A7 in the Appendix) show that all the significant variables except tenure became insignificant. In other words, activity (anti-dictator, freedom, Tahrir Square, and protest), followers, centrality, and past influence had an insignificant effect on retweet influence. This confirms that the model incorporating eight equal time periods (that ignores context) underperformed vis-à-vis the model that is contextualized using the peaks in the data over four time periods. Thus, we confirm that the context is important in understanding factors that drive sustained influence.

## Endogeneity Check

To examine the endogeneity issue, it is important to choose an appropriate instrumental variable for each of the model variables. In the following subsections, we first provide theoretical justifications and then discuss our empirical strategy for testing whether the model variables are endogenous.

## Endogeneity Effects

In this section, we delve into contextual factors that may determine endogeneity. We discuss the effect of account age on tenure, liking on activity, following on followers, and topical homophily on eigenvector centrality.

The variable “tenure” (measured as the total number of time periods a user is active in) may be endogenous, considering the effect of account age (measured as the number of days elapsed since the creation of the account). Specifically, longer-term users may have longer tenure in the Egyptian Revolution time period compared to newer users. In many online environments, long-term users contribute more to the online community by harnessing their experiences (Chiu et al. 2006). Pitta and Fowler (Pitta and Fowler 2005a) explain that, compared to less experienced users, more experienced users in online social networks can provide/access information efficiently; in other words, they can better mobilize social action by virtue of their experience. Efficacy is achieved through an incremental process resulting from the repetition of activities (Thorndike 1931). Longer tenure within the system allows the user to develop greater self-efficacy in sustaining their activities in forums such as Twitter through repetitive use of the mechanisms of the platform.

In a similar vein, the variable, social movement “activity” may be affected by general Twitter activity such as liking. Twitter users who are more active in general—i.e., they interact with Twitter content—are likely to be active in social movements. In social network conventions, the act of “liking” indicates a shared belief system between the user posting and the user liking the post (Lipsman et al. 2012; O’Connor 2013; Shoenberger and Tandoc Jr. 2014). On many knowledge-sharing sites, responses with the highest numbers of likes are recommended to users. Therefore, using mechanisms such as “likes” creates a reputation voting system: a high number of likes indicates the user’s strong reputation (Kietzmann et al. 2011). While unlike on Facebook, likes are not a primary means for evaluating contribution on Twitter, users may tend to search for tweets made by other users who have a higher number of likes. This could be a potential source of endogeneity since it may impact the kind of tweets that receive attention.

![](/api/attachments/J6V2QKA7/fulltext/images/ef838a328f914bab49161b2bfb2d303fc865fcfa2e009d6d21a7eb4d8a74353c.jpg)  
Up to Jan 25

![](/api/attachments/J6V2QKA7/fulltext/images/a7c4e29bfb6047027379c569cbd9eaccdfafa6c541530539c50cd914a1fb5d2a.jpg)  
Jan 29 to Feb 2

Further, the variable, follower count may be endogenous because of the effect of following count (a measure of the number of friends a user is following), which may result in an omitted instrumental variable bias. In this context, it is important to note that for the follower mechanism, there is a distinction between directionality and reciprocity. That is, the link established between two nodes may be bidirectional. Such directionality need not exist among all ties, unlike a friendship tie on Facebook. In a friendship network, a general assumption is that when two nodes are connected, the friendship is mutual. In the follower network, when two nodes are connected, the mechanism need not be mutual. This absence of a reciprocity assumption is critical in understanding Twitter users. However, this aspect of reciprocity can be captured using the following mechanism, which allows the user to be followed by other users (McPherson et al. 2001). In other words, a plausible assumption is that users that follow a large number of other users (out-degree) may have high counts of followers themselves (reciprocal in-degree).

Figure 4. Retweet Network Maps over Time  
![](/api/attachments/J6V2QKA7/fulltext/images/93e35dd479683edbaecdc79a7b8d9acb9d648cb7d7e64759d55f5f557a6d0c88.jpg)  
Jan 26 to Jan 28

![](/api/attachments/J6V2QKA7/fulltext/images/eff960071ae086f1647a3188531e52e91192a00640c5d417dbf6b04dea788e00.jpg)  
Feb 3 to Feb 11

Lastly, in order to ascertain that network effects such as centrality are purely a function of network structure, factors related to network formation should be exogenous to the model. The similarity between network members, also known as homophily (Lazarsfeld and Merton 1954), is a principal factor of interest in the sociology and networks literatures, receiving strong support in terms of gender (Ibarra 1992), race (Mollica et al. 2003), and status (McPherson and Smith-Lovin 1987) in traditional offline settings such as relationship formation. However, this study focuses on online interactions in a focused social movement context. Therefore, traditional cues such as race, gender, or status are often either unavailable or become irrelevant with respect to the context of resource mobilization. However, in online communities, although demographic attributes such as gender and age may not be visible, other users may still be able to detect similarity patterns based on their selfcategorizations (Monge and Contractor 2003) and the context of messages (tweets) and related attributes. For example, users who support similar political ideologies may tend to interact with each other more often, essentially differentiating between similar and dissimilar people based on such attributes (Abrams and Hogg 1999; Turner 1987). Users can observe the topical leanings of other users by categorizing similar and dissimilar others. In this study, we consider the degree to which users are aligned with their connections as topical homophily (Cardodo et al. 2019).

Topical homophily may affect eigenvector centrality. The topical homophily of users captures similarity in users sharing and information consumption, which may affect their influence in the social movement. We use topical markers from Twitter and hashtags such as #Cairo, #Mubarak, etc. to identify the latent context that users engaged in while exchanging messages concerning the respective topics. Homophily among users may present itself through the usage of similar hashtags (Xu et al. 2000). Thus, we measure the alignment of topical interests in terms of the incidence of similar hashtags among users. Table 5 summarizes all the instrumental variables used and their underlying assumptions.

## Endogeneity Test

The Hausman test is a good test for cross-sectional datasets to determine whether instrumental variables point to the endogeneity of exogenous variables (Hausman, 1978). It involves running a two-stage least squares estimation model with exogenous variables and instrumental variables as explanatory variables. This regression estimates the residuals, which are then regressed on the exogenous variables (Bjørndal et al., 1994). The Hausman test uses the F-test of the significance of the residuals in which the null hypothesis states that the exogenous variables in the model are free from endogeneity. This F-statistic on the significance of the instruments in a first-stage regression has widely been used for IV estimation (e.g., Staiger and Stock, 1997). According to this test, rejecting the null hypothesis implies that there is endogeneity caused by the instrumental variable.

However, estimating dynamic models is more challenging because the lagged dependent variable in dynamic models is likely to be correlated with the user-specific effect. Arellano and Bond (1991) suggested using the GMM model in firstorder differences. First-order differencing removes the cross-sectional effects and estimates the model by using instrument variables (Khansa et al., 2015). However, if the differenced error term is correlated with the differenced lagged dependent variable, this may introduce bias that makes the least square estimator inconsistent. To test the consistency of the GMM estimators, we conducted the Sargan-Hansen test (Khansa et al. 2015).

For dynamic panel datasets, the standard procedure used to test for instrument exogeneity is the Sargan-Hansen test of overidentifying restrictions (Graham et al. 2010). The Sargan-Hansen statistic estimates the model using instrumental variables from ordinary time series. For dynamic panel data, it extends such statistics for testing exogeneity sets of explanatory variables (Bhargava, 1991). The Sargan-Hansen test provides a test of overidentifying restrictions that utilizes the difference GMM approach to investigate the instruments. This “difference GMM approach deals with the inherent endogeneity” (Baum 2013, p. 25).

The difference GMM approach estimates a J-statistic that is computed from “residuals from instrumental variables regression by constructing a quadratic form based on the cross-product of the residuals and exogenous variables” (Sargan, 1988; p. 132–33). This “test of overidentifying restrictions regresses the residuals from an [instrumental variable] or [two-stage least squares] regression on the instruments” (Baum 2009, p. 25).

## Endogeneity Results

As discussed earlier, the variables used in endogeneity testing were account age, social media activity, topical homophily, and following count. Account age was measured as the number of days the account has been active. Social media activity was measured through a favorites count, which is the number of tweets the user has favorited. The following count was the measure of the number of accounts the user is following. Topical homophily is the degree to which users are topically aligned with other users in the context (Cardoso et al. 2019). In order to measure topical homophily, we first identified all the hashtags that were used in the Egyptian Revolution context. This yielded 356 hashtags in the first time period, 1151 hashtags in the second time period, 4135 hashtags in the third time period, and 7434 in the last time period. In the second step, we identified the hashtags of each user. The proportion of user’s hashtags to the total hashtags was used as topical homophily.

To test endogeneity, we adjusted for the instrumental variable effect of account age on tenure (Model 1), liking on activity (Model 2), topical homophily on eigenvector centrality (Model 3), and following on followers (Model 4). We tested the instrumental variable effect in the four regression models using the instruments(var(s)) option of the xtdpd module in STATA.

The results of the four models indicate that Sargan-Hansen’s Jstatistic is not significant. Model 1: χ<sup>2</sup> (1) = 0.012 at p > 0.05; Model 2: χ<sup>2</sup> (1) = 1.222 at p > 0.05; Model 3: χ<sup>2</sup> (1) = 1.275 at p > 0.05; Model 4: χ<sup>2</sup> (1) = 2.150 at p > 0.05. Thus, the null hypothesis of Sargan-Hansen’s J-test for each of the four models (that states the model is well specified and free from endogeneity bias) is accepted.

<table><tr><td colspan="5">Table 5. Endogeneity Assumptions</td></tr><tr><td>Suspected Endogenous Variable</td><td>Instrumental Variable</td><td>Exogeneity assumption</td><td>Relevance assumption</td><td>Reference</td></tr><tr><td>Tenure</td><td>Account age</td><td>Twitter membership prior to the scope of the social movement does not impact retweets in the context of a social movement. Moreover, holding an account for a longer time without social action does not translate to retweets.</td><td>Account age depends on the date of joining the Twitter platform. Greater experience in tweeting behavior could help sustain social action for a longer time due to the efficacy of using the platform.</td><td>(Chiu et al. 2006; Pitta and Fowler 2005b;)</td></tr><tr><td>Social movement activity</td><td>Twitter general activity (Liking)</td><td>General activity on Twitter does not translate into retweets unless a concerted effort is made in the specific context (social action). Therefore, general tweeting behavior is exogenous to the model.</td><td>Twitter users who are generally active, may also have greater social movement activity if they choose to participate in the movement. Also, users with more likes may be exposed to more resources (information and other users).</td><td>(Lipsman et al. 2012; O&#x27;Connor 2013; Shoenberger and Tandoc Jr 2014) (Kietzmann et al. 2011)</td></tr><tr><td>Follower count</td><td>Following count</td><td>A user may follow many other users but receiving retweets depends on social action. For example, users who follow a celebrity may not be retweeted unless they have retweet-worthy content.</td><td>Following an account (a form out-degree, reaching out to other users) may influence them to reciprocate by following the original user back. This may lead to non-random network effects.</td><td>(McPherson et al. 2001)</td></tr><tr><td>Eigenvector centrality</td><td>Topical homophily</td><td>Users tweeting about similar topics to others may not necessarily be retweeted unless the content is worthy of forwarding. Topical homophily only brings users of similar interests together.</td><td>Users who support similar political ideologies may tend to interact with each other more often, essentially differentiating between similar and dissimilar people based on such attributes.</td><td>(Abrams and Hogg 1999; Turner 1987)</td></tr></table>

<table><tr><td colspan="5">Table 6. Results of Endogeneity Analysis</td></tr><tr><td></td><td>Model 1: Account age on tenure</td><td>Model 2: Liking on activity</td><td>Model 3: Homophily on centrality</td><td>Model 4: Following on followers</td></tr><tr><td>Intercept</td><td>1.707***(0.278)</td><td>1.717***(0.289)</td><td>1.673***(0.283)</td><td>1.715***(0.288)</td></tr><tr><td>Anti-dictator activity i, t-1</td><td>0.304*(0.125)</td><td>0.305*(0.125)</td><td>0.293*(0.125)</td><td>0.304*(0.125)</td></tr><tr><td>Freedom activity i, t-1</td><td>0.112(0.293)</td><td>0.108(0.293)</td><td>0.166(0.299)</td><td>0.102(0.293)</td></tr><tr><td>Tahrir activity i, t-1</td><td>0.325*(0.164)</td><td>0.324*(0.163)</td><td>0.360*(0.165)</td><td>0.319^(0.163)</td></tr><tr><td>Protest activity i, t-1</td><td>0.060(0.089)</td><td>0.059(0.089)</td><td>0.065(0.089)</td><td>0.059(0.089)</td></tr><tr><td>Tenure i, t-1</td><td>0.416***(0.044)</td><td>0.417***(0.043)</td><td>0.420***(0.043)</td><td>0.415***(0.043)</td></tr><tr><td>Ln(followers)</td><td>0.403***(0.044)</td><td>0.401***(0.044)</td><td>0.405***(0.044)</td><td>0.393***(0.044)</td></tr><tr><td>Centrality i, t</td><td>0.523***(0.088)</td><td>0.530***(0.089)</td><td>0.507***(0.083)</td><td>0.527***(0.089)</td></tr><tr><td>Influence i, t-1</td><td>0.163***(0.044)</td><td>0.158***(0.043)</td><td>0.161***(0.044)</td><td>0.166***(0.045)</td></tr><tr><td>Ln(Status i, t-1)</td><td>-0.194**(0.071)</td><td>-0.195**(0.071)</td><td>-0.194**(0.071)</td><td>-0.189**(0.071)</td></tr><tr><td>URL i, t-1</td><td>-0.458***(0.123)</td><td>-0.458***(0.123)</td><td>-0.451***(0.123)</td><td>-0.455***(0.123)</td></tr><tr><td>t</td><td>-0.039(0.070)</td><td>-0.036(0.071)</td><td>-0.045(0.069)</td><td>-0.037(0.071)</td></tr><tr><td>J-statistic</td><td>0.012</td><td>1.222</td><td>1.275</td><td>2.150</td></tr><tr><td>Degrees of freedom</td><td>1</td><td>1</td><td>1</td><td>1</td></tr><tr><td>p-value</td><td>0.912</td><td>0.269</td><td>0.259</td><td>0.143</td></tr></table>

Note: p-value < 0.10; \* p-value < 0.05; \*\* p-value < 0.01; \*\*\* p-value < 0.001

This confirms that there is no omitted variable bias caused by the effect of account age on tenure, liking on activity, topical homophily on eigenvector centrality, and following count on followers count (Table 6).

In other words, our results do not reject the null hypothesis of the Sargan-Hansen test for testing the endogeneity of tenure, social movement activity, eigenvector centrality, and follower count caused by the instrumental variables, account age, social media activity, topical homophily, and following count, respectively. This evidence supports Sargan-Hansen’s hypothesis that tenure, social movement activity, eigenvector centrality, and follower count are not endogenous.

## Post Hoc Analysis

In this section, we investigate how less-followed users garner online influence. Subsequently, we examine the effect of tone on sustained influence.

## Influential Users

Through “observed” network characteristics, Twitter gives users with high follower counts the power to influence opinion-making and agenda-setting processes. In order to gain a deeper insight into the effect of “observed” network characteristics on retweet influence on Twitter, we investigated how retweet influence differs between different types of online users, particularly focusing on more vs. less influential users. Bakshy et al. (2011) state that influential users are users who already have higher numbers of followers. Thus, based on the follower counts in the sample, we focused on roughly the top and bottom one third of users. We identified that approximately the top one third of users have more than 5000 followers (more influential users), while the bottom one third of users have less than 500 followers (less influential users).

Using a GMM estimator for both groups, more and less influential users, we tested the effect of social movement activities (anti-dictator, freedom, Tahrir Square, and protest), tenure, eigenvector centrality, and prior influence on sustained retweet influence. The results of the post hoc analysis are presented in Table 7. Interestingly, a key difference in the results for these two groups is that for the less influential users, the results show a positive and significant effect of activity on sustained influence, while for more influential users, we see an insignificant effect of activity on sustained influence. This means that users that have fewer followers on Twitter must participate in online social activities to obtain online influence, while users that already have more followers on Twitter do not necessarily have to participate in online social activities to garner online influence.

<table><tr><td colspan="5">Table 7. Results of Follower Analysis</td></tr><tr><td></td><td colspan="2">Followers &lt; 500 (N = 14,580; 39%)</td><td colspan="2">Followers &gt; 5000 (N = 11,333; 30%)</td></tr><tr><td>DV: retweet influence t</td><td>Coefficient</td><td>Robust S.E</td><td>coefficient</td><td>Robust S.E.</td></tr><tr><td>Intercept</td><td>-0.153</td><td>0.444</td><td>-2.304***</td><td>0.216</td></tr><tr><td>Anti-dictator activity i, t-1</td><td>0.489^</td><td>0.262</td><td>0.080</td><td>0.090</td></tr><tr><td>Freedom activity i, t-1</td><td>0.978^</td><td>0.581</td><td>0.110</td><td>0.198</td></tr><tr><td>Tahrir activity i, t-1</td><td>0.649*</td><td>0.323</td><td>0.833</td><td>0.567</td></tr><tr><td>Protest activity i, t-1</td><td>0.791^</td><td>0.431</td><td>0.059</td><td>0.062</td></tr><tr><td>Tenure i, t-1</td><td>0.201*</td><td>0.093</td><td>0.579***</td><td>0.041</td></tr><tr><td>Ln(Followers)</td><td>-0.060</td><td>0.081</td><td>0.229***</td><td>0.027</td></tr><tr><td>Centrality i, t</td><td>0.949***</td><td>0.167</td><td>0.690***</td><td>0.113</td></tr><tr><td>Influence i, t-1</td><td>0.025***</td><td>0.006</td><td>0.007***</td><td>0.002</td></tr><tr><td>Ln(Status i, t-1)</td><td>-0.090</td><td>0.095</td><td>-0.061*</td><td>0.031</td></tr><tr><td>URL i, t-1</td><td>-1.704**</td><td>0.613</td><td>-0.195^</td><td>0.115</td></tr><tr><td>t</td><td>0.055</td><td>0.112</td><td>-0.186***</td><td>0.052</td></tr></table>

Note: p-value < 0.10; \* p-value < 0.05; \*\* p-value < 0.01; \*\*\* p-value < 0.001

## Revolution Sentiments

The results of our model confirm that informal interpersonal networks that form social structures play an important role in facilitating mobilization on Twitter (King 2007). Providing an arena for cultivating similar interests is one of the key functions of mobilizing structures (Den Hond and De Bakker 2007). While the model used in this paper accounts for topical similarity, an individual tweeter’s sentiments must be aligned with the expected sentiment of the crowd (King 2007) for there to be collective action. Social movement scholars have identified that sentiments are effectively communicated in the presence of facilitating structure and may moderate the transformation of social action into influence (Alvarez et al. 2015; McAdam et al. 1996; Oberschall 1978; Tilly 1977). In this section, as part of the post hoc analysis, we explore sentiments during the Arab Spring and examine how they affected collective action. Specifically, we examine the moderating effect of the emotional tone of the tweet on the relationship between anti-dictator (who) activity and influence.

In the context of the Egyptian Revolution, the vast majority of the Twitter content was anti-dictator in nature, as the revolution was viewed as a progressive movement that would bring political and social freedom to Egypt and move it forward. According to our analysis, 98.46% of data (and 98.90% of retweets) related to #Mubarak<sup>8</sup> were anti-dictator in nature. The tweets with pro-dictator content were very rare and received an extremely small number of retweets, compared to the bulk of the tweets that were anti-dictator and in favor of the revolution.

However, the anti-dictator content itself can be expressed in a positive or negative light. Anti-dictator tweets showing signs of cheer, hope, etc. (such as “Crowd cheers as a huge Mubarak poster is torn down …”) depict positive emotions, while those showing rage, protest, etc. (e.g., “… Egyptians rage against Mubarak's 30-year rule …” and “… Thousands protest against President Hosni Mubarak …”) express negative emotions.

In order to derive emotional tone from textual data, we employed the tool Linguistic Inquiry and Word Count (LIWC; Pennebaker et al. 2015). LIWC extracts the frequency or percentage of words associated with the feature within the validated dictionaries. LIWC features have been validated in prior literature demonstrating a moderate correlation between human coding and LIWC coding (Alpers et al. 2005). To code the emotional tone using LIWC, we used the standard dictionary of “positive emotion” and “negative emotion” dimensions of LIWC, which provides information about the tone of the text. Since tweet messages are aggregated to the user level, a user can have positive tweets in a given time period and negative tweet in another time period or the user can have both positive and negative tweets in any time period. Keeping this in mind, we chose to run two separate models to test the effect of (Model 1) anti-dictator activity, number of positive tweets, and their interaction, and (Model 2) anti-dictator activity, number of negative tweets, and their interaction on sustained retweet influence in the subsequent time period.

<table><tr><td colspan="5">Table 8. Results of Sentiment Analysis</td></tr><tr><td></td><td colspan="2">Positive sentiment</td><td colspan="2">Negative sentiment</td></tr><tr><td>DV: retweet influence t</td><td>Coefficient</td><td>Robust S.E.</td><td>Coefficient</td><td>Robust S.E.</td></tr><tr><td>Intercept</td><td>1.708***</td><td>0.304</td><td>1.949***</td><td>0.292</td></tr><tr><td>Anti-dictator activity i, t-1</td><td>0.218^</td><td>0.129</td><td>0.259^</td><td>0.134</td></tr><tr><td>Sentiment i, t-1</td><td>0.390</td><td>0.605</td><td>-1.124**</td><td>0.420</td></tr><tr><td>Anti-dictator*sentiment i, t-1</td><td>-0.132</td><td>0.311</td><td>0.623**</td><td>0.216</td></tr><tr><td>Tenure i, t-1</td><td>0.414***</td><td>0.043</td><td>0.413***</td><td>0.043</td></tr><tr><td>Ln(followers)</td><td>0.402***</td><td>0.044</td><td>0.402***</td><td>0.044</td></tr><tr><td>Centrality i, t</td><td>0.522***</td><td>0.088</td><td>0.523***</td><td>0.088</td></tr><tr><td>Influence i, t-1</td><td>0.161***</td><td>0.044</td><td>0.162***</td><td>0.044</td></tr><tr><td>Ln(Status i, t-1)</td><td>-0.193**</td><td>0.071</td><td>-0.195**</td><td>0.071</td></tr><tr><td>URL i, t-1</td><td>-0.433***</td><td>0.122</td><td>-0.315***</td><td>0.114</td></tr><tr><td>t</td><td>-0.045</td><td>0.070</td><td>-0.043</td><td>0.070</td></tr></table>

Note: p-value < 0.10; \* p-value < 0.05; \*\* p-value < 0.01; \*\*\* p-value < 0.001

As shown in Table 8, users posting negative tweets (in general) in previous time windows have a lower chance to be influential in the subsequent time windows of the movement. However, specifically with regard to anti-dictator activity, negative tweets within previous time windows have a significant positive effect on influence in subsequent time windows. In addition, for positive tweets, in general, as well as positive tweets, that are specifically related to anti-dictator activity, we see an insignificant effect on sustained influence. Other effects, such as tenure, centrality, followers, and prior influence are consistent with that of the main analysis.

## Discussion and Conclusion

We examine the organic antecedents of retweet influence in the different contexts of the Egyptian Revolution social movement of 2011. We analyzed the panel dataset of tweets generated within the time span of Jan 22 to Feb 11, 2011, during the Egyptian Revolution using a dynamic longitudinal research design with n = 2423 users over t = 4 time periods. Due to the lack of established models for identifying meaningful time windows, the panel analysis was preceded by an a priori inductive reasoning analysis to establish the time windows in accordance with the social movement literature. We established a link between online and offline activities by analyzing online activities using contextualized time periods, which were created based on offline events.

This paper provides a deeper understanding of the fundamental processes by which a particular IS artifact may be effectively utilized by a user in the wake of an extreme event. In that vein, we incorporate the key mechanisms studied in social movement mobilization literature into the IS literature. We examine whether those key mechanisms translate into the potential for influence on Twitter like they would in a traditional social movement setting. This perspective enables researchers to view IS from the foreground of interdisciplinary research (Rai 2017).

Our study makes several contributions. First, beyond merely analyzing influence, our study uses a panel analysis to take a computational social science approach and extends it to the question: What are the antecedents of sustained influence in social movements? Individual participation in social movements is often a result of a lengthy process of mobilization. Van Stekelenburg and Klandermans (2010) point out that, surprisingly, the social movement literature lacks research about sustained participation, considering that long-term participation keeps movements going. Perhaps, this lack of research in sustained participation and sustained influence is due to the fact that, historically, being a long-term activist was, to a large extent, a question of physical availability (McAdam 1986). The proliferation of Web 2.0- based ICT’s has now brought new life to sustaining participation by transcending physical barriers. Our study uniquely identifies that rather than mere active participation, the confluence of sustained social action and favorable network structure facilitation is what is critical for users to be influential. Thus, our study fills this gap in the literature.

Second, this study analyzes another underaddressed area of social movement networks—“informal constellations of mobilizing structures.” Advances in social movement literature, specifically resource mobilization, have introduced a new perspective to viewing social actions: from constituting a formal organization for mobilizing activities to the concept of mobilizing structures (Smith and Fetner 2010). The mobilizing structures perspective focuses on how a constellation of key players/groups in an informal network of actors strive to promote social change by aligning their interests and issues (McAdam et al. 1996; McCarthy and Zald 1977). However, studies analyzing such structures have been hard to come by because unlike formal organizational structures such as SMOs, it is difficult to capture the behavior of such structures (Smith and Fetner 2010). Recent studies have explored other aspects of resource mobilization such as SMOs and collective action groups in the wake of ICTs (Selander and Jarvenpaa 2016). This study adds to this body of literature by analyzing the perspective of mobilizing structures, considering the informal constellations of mobilizing actors in the Twitter network.

Third, this study also shows that the concept of duality of social action and facilitating structures as drivers of mobilization influence hold in the case of informal virtual networks like those found on Twitter. This study provides a holistic theoretical framework that encompasses the factors related to the users and the message (social action) and the network structure. Traditionally, social movement literature has focused on how duality affects mobilization (van Stekelenberg and Klandermans 2010). Following this literature, in this paper, we investigated the drivers of influence on the Twitter platform in the context of the Egyptian Revolution. We then identified the aspects of “individual social action” and “facilitating network structures” among the antecedents of Twitter influence. The facilitating structures correspond to technology-enabled multiple connections, and the retweet phenomena correspond to a human-machine collaborative information propagation process, which enhances the speed and expands the scale of information propagation for the sustained social movement. We extend the literature on social movement mobilization to the new world of the human-machine participatory interface, instantiated by, for example, Twitter. Twitter users’ social action is therefore entangled with the artifact and the network structure it facilitates.

Moreover, we analyze how Twitter users’ participation is based on various frames—what activities (e.g., freedom), how activities (e.g., protest), who activities ( e.g., anti-dictator), and where activities (e.g., Tahrir Square)—and show how these activities impact users’ retweet influence in terms of mobilizing a social movement. These activities highlight the two key features required for social movement mobilization— i.e., bringing about or resisting a change in society and organizing for the sustained participation of citizens. In the Egyptian Revolution movement, these frames depict the focal motive of offline protests. This is an important contribution of this study from the perspective of how social action frames are adapted to a specific context. In this context, what and who activities map to the frames of sympathizing with the cause and expressing a desire to participate. How and where activities map to the protestor’s need for information about events. These adaptations are fairly generalizable across any context of social movement. We demonstrate how collective action frames of social movements can be identified on Twitter.

To extract variables specific to the social movement context from the large-scale dataset, we used a hybrid mixed methods approach involving machine learning and human coding. This method enables the identification of text features that are otherwise difficult to capture using pure machine learning techniques and also overcomes the hurdle of needing to manually code large datasets. We found support for the effect of the anti-dictator (who) activity on retweet influence, but not for the effect of the freedom (what) activity. One reason for this could be that while freedom of expression, association, and access to information have been long-standing issues before the social movement began (Ghonim 2012), there was a sudden surge in anti-dictator activities because of violent responses from dictatorial authorities, pro-government militias, and counterdemonstrators against demonstrations supporting free expression (Steinert-Threlkeld et al. 2015).

We also found evidence for the effect of the Tahrir Square (where) activity on retweet influence, but not for the effect of protest (how) activity. The spatial context (where) activity is significant, probably because it refers to the physical location of the demonstrations whereas the social movement conversations were virtual in nature, suggesting that physical location may have a significant impact. Recent studies have shown that social media activity correlates with the subsequent large-scale decentralized coordination of protests (Steinert-Threlkeld et al. 2015), which may explain why such events may have a significant effect on retweet influence. Furthermore, this study also examines the role of the sentimentality of tweets in relation to the frames of social action. The prevailing wisdom is that negative sentiment posts on Twitter attract more attention (Tsugawa and Ohsaki 2017). Our post hoc analysis reveals a nuanced phenomenon when applied to the specific context of protests. Upon splitting the data into positive and negative sentiment tweets and testing the model, the effects of most of the variables remained consistent. However, regarding the frames related to anti-dictator activities, negative sentiment tweets had a significantly greater impact on retweet influence, suggesting that the sentiments must also fit the prevailing narrative. This finding is also in accordance with social movement theory, which posits that mobilization activity is most effective when it resonates with the expected sentiment of the crowd (King 2007).

This study also highlights new aspects of virtual networks of movement participation—observed vs. unobserved network structures. We conceptualized centrality based on the interaction network (formed by mentions and retweets) on Twitter, and characterized following as an intentional act of subscribing to an actor on Twitter. This means that the follower population is a clearly observed entity, while centrality in a network is unobservable to Twitter users. We consistently found both followers and centrality was consistently to be significant. An “unobserved” network such as the interaction network appears to play a role that is just as important as “observed” networks such as the follower network. Exploring the varying influence of these two measures may reveal interesting avenues for future design research on human-machine interfaced networks.

In conjunction with these theoretical aspects, we articulate some important findings for practice below. We found that tenure is a significant aspect of social action that contributes to sustained Twitter influence. We also found that centrality is a significant aspect of facilitating structure, which, in addition to the number of Twitter followers, contributes to influence. Like page rank algorithms, eigenvector centrality also works well in the context of social movements. A deeper implication could be that analogous to physical connections of an individual (Lin 2002, McAdam 1986), virtual network capital also plays a similar role in determining influence. However, there is a difference between the two similar measures of network capital—centrality and followers— which is pertinent to this study.

The findings also show that a user who is more active in terms of participation may not be as influential as other users with a stronger underlying network structure. However, a user who less frequently participates may nevertheless have significant influence because of a dense underlying network structure and longer participation tenure. Although our findings on the social movements on Twitter may not necessarily be generalized to other platforms and technologies, given the popularity, prominence, and monopoly of Twitter as the main social media platform used for social movements, especially in countries where other forms of social media are restricted and censored, our findings are still important and should be of interest to a very large audience of sociologists and information systems researchers.

This paper has some limitations. The number of followers is a variable collected at one time after the social movement we examined. However, the number of followers generally increases over time, thus the effects of followers would have perhaps have been even stronger if we had been able to collect the information at each event time period. Moreover, while we investigated the content of Twitter messages and their effects on user influence using a mixed methods approach, a full-fledged framing analysis might provide deeper insights. Such an analysis could be a future extension of this study.

We acknowledge that the similarity between users may reflect their retweet influence. Ugander et al. (2012) controlled for demographic similarity (age, gender, and nationality) in investigating factors that cause friends to join Facebook. However, such data is difficult to gather on Twitter. Golder and Macy (2014) identify issues regarding homophily. Following them, we argue that while it is difficult to “separate selection from influence observationally” (p. 10), in this research, the tweets we collected are based on the common interests and similar opinions of individuals involved in the Egyptian Revolution.

We recognize that our study relies on the analysis of archival data. We used appropriate econometric methods to identify and adjust for possible endogeneity; however, more robust study designs could help to draw stronger causal inferences. Specifically, future research could utilize primary data on users’ offline activities by designing large-scale quasiexperiments and enrolling volunteers in them ahead of time. Such experiments could include tools that volunteers would install on their mobile phone and web browsers that collect data relevant to their online and even possibly offline activities over a long period of time. However, such a data collection approach is very intrusive to privacy and would require careful examination to mitigate potential risks to users. Nevertheless, such an approach would enable researchers to incorporate connections to offline activities that would otherwise be difficult to properly explore.

A further limitation of our study is that we did not examine offline activities. Offline activities of users could affect online influence. A reliable dataset of offline activities would allow researchers to examine reverse causality (Leszczensky and Wolbring 2018) and test theories about the effect of online activities on users’ offline activities (Althoff et al. 2017, Vissers and Stolle 2014). For this paper, collecting data on the offline activities of thousands of users was not feasible for the following reasons: First, as discussed earlier, a proactive collection of Twitter data in real time would have been required as the Egyptian Revolution was developing. Most of these users were in Egypt, whereas our research team was located in the U.S. Such geographical distance is a significant barrier to the collection of offline data, especially when it must be done retrospectively after the event. Second, many of the participants in this social uprising used anonymous Twitter handles to mask their identity because of fears of retaliation from the government.

Another limitation of this study is that our data primarily come from a single social media platform—Twitter. Future research could collect real-time data across multiple social media platforms while a social movement is evolving. Such real-time data collection would enable researchers to construct time-varying measures for some of the variables that we could only measure at one point in time, such as the count of followers. Given that users are now concurrently active on multiple social media platforms, a time-varying measure of these variables would enable researchers could look into the interlinked effects of the platforms on each other (Rowe and Alani 2014). For example, researchers could examine whether a user’s popularity on one social platform increases or decreases their popularity on other platforms, or investigate whether a user’s level of activity on one platform is associated with their level of activity on another platform.

Prior studies in computational social science have investigated social behaviors that can be better explained by acknowledging the inseparability of social behaviors and technology uses (Orlikowski 2007; Orlikowski and Scott 2008). In that regard, this research also contributes to computational social science research in the IS field. Positioned at the intersection of social media research and social network analysis, this study sheds light on the effects of similar network structures and positions (Borgatti and Foster 2003). Social media platforms homogenize some parts of content through user profiles. However, features of social media platforms that relate user behavior to network position are rarely seen (Boyd and Ellison 2013). Therefore, the integration of social network analytic concepts into meaningful metrics that users can use to articulate their connections and make better use of their structural capital is important (Boyd and Ellison 2007). Articulating tie strength may help prioritize information from central relations and efficiently mobilize information (Xu et al 2017). Future studies could try to fill this research gap by examining ways to effectively integrate structural features at the foreground of the human-computer interface (Kane et al 2014). Depending on content access mechanisms and the relative position of the nodes, social network platforms may adopt different computational approaches to present otherwise obscure information to users considering the relevant context.

## Acknowledgments

The authors wish to thank the SE and AE for their guidance and the review team for their critical comments that have greatly improved the paper. This research is based on work supported by the National Science Foundation (NSF) under grant #1134853. Rohit Valecha has been funded by NSF under grant #1651475. Onook Oh has been funded by the NSF under grant #1734632. H. Raghav Rao has been funded by NSF under grants #1651475 and 2020252. Any opinions, findings, and conclusions or recommendations expressed in this material are those of the author(s) and do not necessarily reflect the views of the National Science Foundation

## References

Abbasi, A., Zahedi, F. M., Zeng, D., Chen, Y., Chen, H., and Nunamaker Jr., J. F. 2015. “Enhancing Predictive Analytics for Anti-Phishing by Exploiting Website Genre Information.” Journal of Management Information Systems, 31(4), pp. 109-157.

Abrams, D., and Hogg, M. A. 1999. Social Identity and Social Cognition, Blackwell.

Ackland, R., and O’Neil, M. 2011. “Online Collective Identity: The Case of the Environmental Movement,” Social Networks (33), pp. 177-190.

Alpers, G. W., Winzelberg, A. J., Classen, C., Roberts, H., Dev, P., Koopman, C., and Taylor, C. B. 2005. “Evaluation of Computerized Text Analysis in an Internet Breast Cancer Support Group,” Computers in Human Behavior, 21(2), 361-376.

Althoff T, Jindal P, and Leskovec J 2017. “Online Actions with Offline Impact: How Online Social Networks Influence Online and Offline User Behavior,” Proceedings of the 10th ACM International Conference on Web Search Data Mining, pp. 537- 546.

Al-Hasan, A., Yim, D., and Lucas, H. C. 2018. “A Tale of Two Movements: Egypt during the Arab Spring and Occupy Wall Street,” IEEE Transactions on Engineering Management, 66(1), 84-97.

Alvarez, R., Garcia, D., Moreno, Y., and Schweitzer, F. 2015. “Sentiment Cascades in the 15m Movement,” EPJ Data Science (4), Article 6.

Aral, S., and Walker, D. 2011. “Identifying Social Influence in Networks Using Randomized Experiments,” IEEE Intelligent Systems (26:5), pp. 91-96.

Arazy, O., Yeo, L., and Nov, O. 2013. “Stay on the Wikipedia Task: When Task-Related Disagreements Slip into Personal and Procedural Conflicts,” Journal of the American Society for Information Science and Technology (64:8), pp. 1634-1648.

Arellano, M., and Bond, S. 1991. “Some Tests of Specification for Panel Data: Monte Carlo Evidence and an Application to Employment Equations,” The Review of Economic Studies (58:2), pp. 277-297.

Arlot, S., and Celisse, A. 2010. “A Survey of Cross-Validation Procedures for Model Selection,” Statistics Surveys (4), pp. 40-79.

Arquilla, J., and Ronfeldt, D. 2001. Networks and Netwars: The Future Of Terror, Crime, And Militancy, Rand Corporation.

Attia, A. M., Aziz, N., Friedman, B., and Elhusseiny, M. F. 2011. “Commentary: The Impact of Social Networking Tools on Political Change in Egypt’s “Revolution 2.0,” Electronic Commerce Research and Applications (10:4), pp. 369-374.

Bachura, E., Valecha, R., Chen, R., and Rao, R. H. 2017. “Modeling Public Response to Data Breaches,” Proceedings of the American Conference on Information Systems. Boston, MA.

Bachura, E., Valecha, R., Chen, R., and Rao, R. H. 2017. “Data Breaches and the Individual: An Exploratory Study of the OPM Hack,” Proceedings of the International Conference on Information Systems, Seoul, South Korea.

Bakshy, E., Hofman, J. M., Watts, D. J., and Mason, W. A. 2011. “Everyone’s an Influencer: Quantifying Influence on Twitter Categories and Subject Descriptors,” Proceedings of the 4th ACM International Conference on Web Search and Data Mining, pp. 65- 74

Bampo, M., Ewing, M. T., Mather, D. R., Stewart, D., and Wallace, M. 2008. “The Effects of the Social Structure of Digital Networks on

Viral Marketing Performance,” Information Systems Research (19:3), pp. 273-290.

Baum, C. 2009. “Instrumental Variables and Panel Data Methods In Economics and Finance” (http://fmwww.bc.edu/GStat/ docs/StataIV.pdf)

Baum, C. 2013. “Dynamic Panel Data Estimators” (http://fmwww. bc.edu/EC-C/S2013/823/EC823.S2013.nn05. slides.pdf)

Bavelas, A. 1950. “Communication Patterns in Task‐Oriented Groups,” The Journal of the Acoustical Society of America (22:6), pp. 725-730.

Bennett, W. L., and Segerberg, A. 2011. “Digital Media and the Personalization Of Collective Action: Social Technology And The Organization Of Protests Against The Global Economic Crisis,” Information, Communication and Society (14:6), pp. 770- 799.

Bhargava, A. 1991. “Identification and Panel Data Models with Endogenous Regressors,” The Review of Economic Studies (58:1), pp. 129-140.

Bjørndal, T., Salvanes, K. G., and Gordon, D. V. 1994. “Elasticity Estimates of Farmed Salmon Demand in Spain and Italy,” Empirical Economics (19:3), 419-428.

Blevins, J. L., Lee, J. J., McCabe, E. E., and Edgerton, E. 2019. “Tweeting for Social Justice in# Ferguson: Affective Discourse In Twitter Hashtags,” New Media & Society (21:7), 1636-1653.

Bonacich, P. 2007. “Some Unique Properties of Eigenvector Centrality,” Social Networks (29:4), pp. 555-564.

Borgatti, S. P., and Foster, P. C. 2003. “The Network Paradigm in Organizational Research: A Review And Typology,” Journal of Management (29:6), pp. 991-1013.

Boyd, D. M., and Ellison, N. B. 2007. “Social Network Sites: Definition, History, and Scholarship. Journal of Computer-Mediated Communication,” (13:1), pp. 210-230.

Boyd, D., Golder, S., and Lotan, G. 2010. “Tweet, Tweet, Retweet: Conversational Aspects of Retweeting on Twitter,” Proceedings of the 43rd Hawaii International Conference on System Sciences, Kauai, HI.

Bradley, A. P. 1997. “The Use of the Area under the ROC Curve in the Evaluation of Machine Learning Algorithms,” Pattern Recognition (30:7), pp. 1145-1159.

Brainard, L. A., and Siplon, P. D. 2000. “Cyberspace Challenges to Mainstream Advocacy Groups: The Case of Health Care Activism.” Presented at the Annual Meeting of the American Political Science Association, Washington, D.C.

Butler, B., Sproull, L., Kiesler, S., and Kraut, R. 2007. “Community Effort in Online Groups: Who Does the Work and Why?” Leadership at a Distance (11), pp. 171-194.

Cardoso, F. M., Meloni, S., Santanche, A., and Moreno, Y. 2019. “Topical Alignment in Online Social Systems,” Frontiers in Physics (7), Article 58.

Cha, M., Haddadi, H., Benevenuto, F., and Gummadi, K. P. 2010. “Measuring User Influence in Twitter: The Million Follower Fallacy,”in Proceedings of the 4th International AAAI Conference on Weblogs and Social Media, Washington DC.

Chae, I., Stephen, A. T., Bart, Y., and Yao, D. 2016. “Spillover Effects in Seeded Word-of-Mouth Marketing Campaigns,” Marketing Science (36:1), pp. 89-104.

Chi, L., Ravichandran, T., and Andrevski, G. 2010. “Information Technology, Network Structure, and Competitive Action.” Information Systems Research (21:3), pp. 543-570.

Chiu, C.-M., Hsu, M.-H., and Wang, E. T. 2006. “Understanding Knowledge Sharing in Virtual Communities: An Integration of Social Capital and Social Cognitive Theories,” Decision Support Systems (42:3), pp. 1872-1888.

Chou, C. H., Zahedi, F., and Zhao, H. 2011. “Ontology for developing Web Sites for Natural Disaster Management: Methodology and Implementation,” IEEE Transactions on Systems, Man and Cybernetics, Part A: Systems and Humans (41:1), pp. 50-62.

Choi, H., and Zo, H. (2020). “Network Closure Versus Structural Hole: The Role of Knowledge Spillover Networks in National Innovation Performance,” IEEE Transactions on Engineering Management (67:1), pp. 1-11

Colicev, A., O’Connor, P., and Vinzi, V. E. 2016. “Is Investing in Social Media Really Worth It? How Brand Actions and User Actions Influence Brand Value,” Service Science (8:2), pp. 152- 168.

Conell, C., and Cohn, S. 1995. “Learning from Other People’s Actions: Environmental Variation and Diffusion in French Coal Mining Strikes, 1890-1935,” American Journal of Sociology (101), Article 366.403.

Crandall, D., Cosley, D., Huttenlocher, D., Kleinberg, J., and Suri, S. 2008. “Feedback Effects Between Similarity and Social Influence in Online Communities,” Proceeding of the 14th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, pp. 160-168.

Dawson, C. A., and Gettys, W. E. 1929. An Introduction to Sociology, Ronald Press.

Della Porta, D., and Mosca, L. 2005. “Global-Net for Global Movements? A Network of Networks for a Movement of Movements,” Journal of Public Policy (25:1), pp. 165-190.

Den Hond, F., and De Bakker, F. G. 2007. “Ideologically Motivated Activism: How Activist Groups Influence Corporate Social Change Activities,” Academy of Management Review (32:3), pp. 901-924.

Dholakia, U. M., Bagozzi, R. P., and Pearo, L. K. 2004. “A Social Influence Model of Consumer Participation in Network and Small-Group-Based Virtual Communities,” International Journal of Research in Marketing (21:3), pp. 241-263.

Duffy, M. J., and Dhabi, A. 2011. “Networked Journalism and Al-Jazeera English: How the Middle East Network Engages the Audience to Help Produce News,” Journal of Middle East Media (7:1), pp. 1-23.

Earl, J. 2013. “Spreading the Word or Shaping the Conversation: ‘Prosumption’ in Protest Websites,” in Research in Social Movements, Conflicts and Change, Earl, J. and Patrick G. (eds.), Emerald Group, pp. 3-38.

Earl, J., and Kimport, K. 2011. “Digitally Enabled Social Change: Activism in the Internet Age, MIT Press.

Ellison, N. B., and Boyd, D. 2013. “Sociality through social network sites,” The Oxford Handbook of Internet Studies, W. H. Dutton (ed.) Oxford University Press, pp. 151-172.

Ellison, N. B., Steinfield, C., and Lampe, C. 2007. “The Benefits of Facebook “Friends:” Social Capital and College Students’ Use of Online Social Network Sites,” Journal of Computer‐Mediated Communication (12:4), pp. 1143-1168.

Ellison, N., Steinfield, C., and Lampe, C. 2006. “Spatially Bounded Online Social Networks and Social Capital,” International Communication Association (36), pp. 1-37.

Eltantawy, N., and Wiest, J. 2011. “Social Media in the Egyptian Revolution: Reconsidering Resource Mobilization Theory,” International Journal of Communication (5), pp. 1207-1224.

Fang, X., Hu, P. J. H., Li, Z., and Tsai, W. 2013. “Predicting Adoption Probabilities in Social Networks,” Information Systems Research (24:1), pp. 128-145.

Flanagin, A. J., Stohl, C., and Bimber, B. 2006. “Modeling the Structure of Collective Action,” Communication Monographs (73:1), pp. 29-54

Flynn, M. T., and Flynn, C. A. 2012. “Integrating Intelligence and Information: Ten Points for the Commander,” Military Review (92:1), Article 4.

Freeman, L. C. 1977. “A Set of Measures of Centrality Based on Betweenness,” Sociometry (40:1), pp. 35-41.

Freeman, L. C. 1979. “Centrality in Social Networks Conceptual Clarification,” Social Networks (1:3), pp. 215-239.

Freund, R.J., Littell, R.C., and Creighton, L. 2003, SAS Institute.

Fu, K. W., Chau, M., and Sam, C. 2014. “Use of Microblogs in Grassroots Movements in China: Exploring the Role of Online Networking in Public Agenda-Setting,” Journal of Information Technology and Politics (11:3), pp. 309-328

Garrett, R. K. 2006. “Protest in an Information Society: A Review of Literature on Social Movements and New ICTs,” Information Communication and Society (9:2), pp. 202- 224.

Gergely, M., and Rao, V. 2014. “The Effects of Salience, Deterrence, and Social Influence on Software Piracy: A Proposed Experimental Study,” Proceedings of the Americas Conference on Information Systems, Savannah, GA.

Ghannam, J. 2011. Social Media in the Arab World: Leading up to the Uprisings of 2011, Center for International Media Assistance/National Endowment for Democracy.

Ghonim, W. 2012. Revolution 2.0: The Power of the People Is Greater than the People in Power: A Memoir, Houghton Mifflin Harcourt.

Goes, P. 2013. “Popularity effect in User-Generated Content: Online Reviews,” Presented at University at Buffalo, NY.

Goes, P. B., Lin, M., and Au Yeung, C. M. 2014. “‘Popularity Effect’ in User-Generated Content: Evidence from Online Product Reviews,” Information Systems Research, 25(2), 222-238.

Golder, S. A., and Macy, M. W. 2014. “Digital Footprints: Opportunities and Challenges for Online Social Research,” Annual Review of Sociology (40), pp. 129-152.

Golder, S. A., and Macy, M. W. 2015. “Introduction,” in Twitter: A Digital Socioscope, Cambridge University Press (pp. 1-20).

Goyal, A., Bonchi, F., and Lakshmanan, L. V. S. 2010. “Learning Influence Probabilities in Social Networks,” in Proceedings of the Third ACM International Conference on Web Search and Data Mining, New York, NY.

Graham, D. J., Melo, P. S., Jiwattanakulpaisarn, P., and Noland, R. B. 2010. “Testing for Causality between Productivity and Agglomeration Economies,” Journal of Regional Science (50:5), pp. 935-951.

Grundberg, M. D., and Lindgren, S. 2015. “Translocal Frame Extensions in a Networked Protest: Situating the# IdleNoMore Hashtag.” IC Revista Científica de Información y Comunicación (11), pp. 49-77.

Gupta, A., and Kumaraguru, P. 2011. Twitter Explodes with Activity in Mumbai Blast! A Lifeline or an Unmonitored Daemon in the Lurking? (http://precog.iiitd.edu.in/psosm \_www2012/a2- gupta.pdf).

Hajian, B. 2011. “On Measuring Influence and its Properties in Social Networks,” upublished dissertation, Carleton University, Ottowa, CA.

Hajian, B., and White, T. 2011. “Modeling Influence in a Social Network: Metrics and Evaluation,” Proceedings of the 3rd International Conference on Privacy, Security, Risk and Trust and IEEE 3rd International Conference on Social Computing, pp. 497- 500.

Hamdy, N., and Gomaa, E. H. 2012. “Framing the Egyptian Uprising in Arabic Language Newspapers and Social Media,” Journal of Communication (62:2), pp. 195-211.

Hausman, J. A. 1978. “Specification Tests in Econometrics,” Econometrica (46:6), pp. 1251-1271.

Heimbach, I., and Hinz, O. 2018. “The Impact of Sharing Mechanism Design on Content Sharing in Online Social Networks,” Information Systems Research. (29:3), pp. 592-611

Helmes-Hayes, R. 1994. “Canadian Sociology’s First Textbook: C. A. Dawson and W. E. Gettys’s ‘An Introduction to Sociology (1929),’” Canadian Journal of Sociology/Cahiers canadiens de sociologie (19:4), pp. 461-497

Hertel, G., Niedner, S., and Herrmann, S. 2003. “Motivation of Software Developers in Open Source Projects: An Internet-Based Survey of Contributors to the Linux Kernel,” Research Policy (32:7), pp. 1159-1177.

Heumann, B. W. 2011. “An Object-Based Classification of Mangroves Using a Hybrid Decision Tree—Support Vector Machine Approach,” Remote Sensing, 3(11), pp. 2440-2460.

Hiller, H. H. 1975. “A Reconceptualization of the Dynamics of Social Movement Development,” Pacific Sociological Review, 18(3), pp. 342–360.

Holden RT. 1986. “The Contagiousness of Aircraft Hijacking,” American Journal Sociology (91), pp. 874-904

Hinz, O., Skiera, B., Barrot, C., and Becker, J. U. 2011. “Seeding Strategies for Viral Marketing: An Empirical Comparison,” Journal of Marketing (75:6), pp. 55-71.

Holtz-Eakin, D., Newey, W., and Rosen, H. S. 1988. “Estimating Vector Autoregressions with Panel Data,” Econometrica (56:6), pp. 1371-1395.

Howard, P. N., Duffy, A., Deen, F., Muzammil, H., Will, M., and Marwa, M. 2011. “Opening Closed Regimes; What Was the Role of Social Media During the Arab Spring ?” Working Paper (available at https://papers.ssrn.com/sol3/papers.cfm? abstract\_id=2595096).

Ibarra, H. 1992. “Homophily and Differential Returns: Sex Differences in Network Structure and Access in an Advertising Firm,” Administrative Science Quarterly (37:3), pp. 422-447.

Java, A., Song, X., Finin, T., and Tseng, B. 2007. “Why We Twitter: Understanding Microblogging Usage and Communities,” in Proceedings of the 9th WebKDD and 1st SNA-KDD Workshop on Web Mining and Social Network Analysis, pp. 56-65.

Jenkins, J. 1983. “Resource Mobilization Theory and the Study of Social Movements,” Annual Review of Sociology, 9, 527-53.

Kane, G. C., Alavi, M., Labianca, G., and Borgatti, S. P. 2014. “What’s Different about Social Media Networks? A Framework and Research Agenda,” MIS Quarterly (38:1), pp. 275-304.

Kaplan, A. M., and Haenlein, M. 2011. “Two Hearts in Three-Quarter Time: How to Waltz the Social Media/Viral Marketing Dance,” Business Horizons (54:3), pp. 253-263.

Kelman, H. C. 1958. “Compliance, Identification, and Internalization: Three Processes of Attitude Change,” The Journal of Conflict Resolution (2:1), pp. 51-60.

Kelman, H. C. 1961. “Processes of Opinion Change,” Public Opinion Quarterly (25:1), pp. 57-78.

Kempe, D., Kleinberg, J., and Tardos, É. 2003. “Maximizing the Spread of Influence through a Social Network,” in Proceedings of the 9th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, New York, NY.

Keselman, A., Logan, R., Smith, C. A., Leroy, G., and Zeng-Treitler, Q. 2008. “Developing Informatics Tools and Strategies for Consumer-Centered Health Communication,” Journal of the American Medical Informatics Association (15:4), pp. 473-483.

Khamis, S., and Vaughn, K. 2011. “Cyberactivism in the Egyptian Revolution: How Civic Engagement and Citizen Journalism Tilted the Balance,” Arab Media and Society (14:3), pp. 1-25.

Khansa, L., Ma, X., Liginlal, D., and Kim, S. S. 2015. “Understanding Members’ Active Participation in Online Question-And-Answer Communities: A Theory and Empirical Analysis,” Journal of Management Information Systems (32:2), 162-203.

Kietzmann, J. H., Hermkens, K., McCarthy, I. P., and Silvestre, B. S. 2011. "Social Media? Get Serious! Understanding the Functional Building Blocks of Social Media,” Business Horizons (54:3), pp. 241-251.

King, B. 2008. “A Social Movement Perspective of Stakeholder Collective Action and Influence,” Business & Society, 47(1), pp. 21-49.

King, C. W. 1956, Social Movements in the United States, Random House.

Klandermans, B. 1984. “Mobilization and Participation: Social-Psychological Expansions of Resource Mobilization Theory,” American Sociological Review, 49(5), 583–600.

Klandermans, B., and Oegema, D. 1987. “Potentials, Networks, Motivations, and Barriers: Steps Towards Participation in Social Movements,” American Sociological Review (52:4), pp. 519-531.

Klandermans, B., van Stekelenburg, J., Damen, M.-L., van Troost, D., and van Leeuwen, A. 2014. “Mobilization without Organization: The Case of Unaffiliated Demonstrators,” European Sociological Review (30:6), pp. 702-716.

Kohavi, R. 1995. “A Study of Cross-Validation and Bootstrap for Accuracy Estimation and Model Selection,” In IJCAI (14:2), pp. 1137-1145).

Kraut, R., Maher, M. L., Olson, J., Malone, T. W., Pirolli, P., and Thomas, J. C. 2010. “Scientific Foundations: A Case for Technology-Mediated Social-Participation Theory,” Computer (43:11), pp. 22-28.

Kravets, D. 2011. “What’s Fueling Mideast Protests? It’s More Than Twitter,” Wired (http://www.wired.com/dangerroom/2011/01/ social-media-oppression/)

Krippendorff, K. 1980. “Validity in Content Analysism,” In Computerstrategien für die Kommunikationsanalyse, E. Mochmann (Ed.), Campus, pp. 69-112.

Krishnamurthy, B., Gill, P., and Arlitt, M. 2008. “A Few Chirps about Twitter,” in Proceedings of the First Workshop on Online Socia Networks, pp. 19-24.

Kumar, V., Bhaskaran, V., Mirchandani, R., and Shah, M. 2013. “Practice Prize Winner—Creating a Measurable Social Media Marketing Strategy: Increasing the Value and Roi of Intangibles and Tangibles for Hokey Pokey,” Marketing Science (32:2), pp. 194-212.

Lampe, C., and Johnston, E. 2005. “Follow the (Slash) Dot: Effects of Feedback on New Members in an Online Community,” in Proceedings of the 2005 International ACM SIGGROUP Conference on Supporting Group Work, pp. 11-20.

Langman, L. 2005. “From Virtual Public Spheres to Global Justice: A Critical Theory of Internetworked Social Movements,” Sociological Theory (23:1), pp. 42-74.

Lazarsfeld, P. F., and Merton, R. K. 1954. “Friendship as a Social Process: A Substantive and Methodological Analysis,” in Freedom and Control in Modern Society, M. Berger, T. Abel and C.H. Page (eds.), Van Nostrand, pp. 331-334

Lazer, D., Pentland, A., Adamic, L., Aral, S., Barabási, A., Brewer, D., Christakis, N., Contractor, N., Fowler, J., Gutmann, M., Jebara, T., King, G., Macy, M., Roy, D., and Alstyne, M. 2009. “Life in the Network: the Coming Age of Computational Social Science,” Nature (323:5915), pp. 721-723.

Leavitt, H. J. 1951. “Some Effects of Certain Communication Patterns on Group Performance,” The Journal of Abnormal and Social Psychology (46:1), pp. 38-50.

Lerman, K., and Ghosh, R. 2010. “Information Contagion: An Empirical Study of the Spread of News on Digg and Twitter Social Networks,” in Proceedings of 4th International Conference on Weblogs and Social Media, Menlo Park, CA.

Leszczensky L., and Wolbring T. 2018. “How to Deal with Reverse Causality Using Panel Data? Recommendations for Researchers Based on a Simulation Study,” Social Methods and Research (27:3), pp. 1-29

Li, J., and Rao, H. R. 2010. “Twitter as a Rapid Response News Service: An Exploration in the Context of the 2008 China Earthquake,” Electronic Journal of Information Systems in Developing Countries (42:1), pp. 1-22

Liaw, A., and Wiener, M. 2002. Classification and Regression by Random Forest. Newsletter of the R Project (2:3), pp. 18-22.

Lim, M. 2012. “Clicks, Cabs, and Coffee Houses: Social Media and Oppositional Movements in Egypt, 2004-2011,” Journal of Communication (62:2), 231-248.

Lin, N. 2002. “Social Capital: A Theory of Social Structure and Action,”Structural Analysis in the Social Sciences Cambridge University Press (19), pp. 16-278.

Lin, N. 2008. “A Network Theory of Social Capital,” in The Handbook of Social Capital, D. Castiglione, J. van Deth, and G. Wolleb (eds.), Oxford University Press, pp. 50-69.

Lipsman, A., Mudd, G., Rich, M., and Bruich, S. 2012. “The Power of ‘Like,’” Journal of Advertising Research (52:1), pp. 40-52.

Lohmann, S. 1994. “The Dynamics of Informational Cascades: The Monday Demonstrations in Leipzig, East Germany, 1989–91.” World Politics (47:1), pp. 42-101.

Los Angeles Times. 2011. “Arab World: How Tunisia’s Revolution Transforms Politics of Egypt and Region” (http://latimesblogs.latimes.com/babylonbeyond/2011/01/arabworld-how-tunisia-revolution-changed-politics-of-egypt-andregion-.html).

Lotan, G., Graeff, E., Ananny, M., Gaffney, D., Pearce, I., and Boyd, D. 2011. “The Revolutions Were Tweeted: Information Flows During the 2011 Tunisian and Egyptian Revolutions,” International Journal of Communications (5), pp. 1375-1405.

Maghrabi, R.O. 2017. “Online Social Systems, Social Actions, and Politics: A Narrative Analysis of the Role of Social Media in Revolutionary Political Change,” unpublished doctoral

dissertation, University of North Carolina at Greensboro, Greensboro, NC.

Maghrabi, R.O., and Salam, A.F. 2011. “Social Media, Social Movement, and Political Change: The Case of 2011 Cairo Revolt,” in Proceedings of the 30th International Conference on Information Systems, Shanghai, China.

Mann, A. 2016. “Computational Social Science,” Proceedings of the National Academy of Sciences of the United States of America (113:3), pp. 468-470.

Mason, W. A., Conrey, F. R., and Smith, E. R. 2007. "Situating Social Influence Processes: Dynamic, Multidirectional Flows of Influence within Social Networks," Personality and Social Psychology Review (11:3), pp. 279-300.

McAdam, D. 1986. “Recruitment to High-Risk Activism: The Case of Freedom Summer,” American Journal of Sociology (92:1), pp. 64- 90.

McAdam, D., McCarthy, J. D., and Zald, M. N. 1996. Comparative Perspectives on Social Movements Opportunities, Mobilizing Structures, and Framing, Cambridge University Press.

McCarthy, J., and Zald, M. N. 1977. “Resource Mobilization and Social Movements: A Partial Theory,” American Journal of Sociology (82:6), pp. 1212-1241.

McPherson, M., and Smith-Lovin, L. 1987. “Homophily in Voluntary Organizations: Status Distance and the Composition of Face-to-Face Groups,” American Sociological Review (52:3), pp. 370-379.

Mollica, K. A., Gray, B., and Trevino, L. K. 2003. "Racial Homophily and Its Persistence in Newcomers’ Social Networks,” Organization Science (14:2), pp. 123-136.

Monge, P. R., and Contractor, N. S. 2003. Theories of Communication Networks. Oxford University Press.

Musembwa, S., and Paul, S. 2012. “Social Networks: Cultural Diversity, Trust, Reciprocity and Social Capital,” Proceedings of the Americas Conference on Information Systems, Seattle, WA.

O’Connor, A. J. 2013. “The Power of Popularity an Empirical Study of the Relationship between Social Media Fan Counts and Brand Company Stock Prices,” Social Science Computer Review (31:2), pp. 229-235.

Oberschall, A. 1978. “Theories of Social Conflict,” Annual Review of Sociology (4:1), pp. 291-315.

Oh, O., Agrawal, M., and Rao, H. R. 2011. “Information Control and Terrorism: Tracking the Mumbai Terrorist Attack Through Twitter,” Information Systems Frontiers, 13(1), 33-43.

Oh, O., Agrawal, M., and Rao, H. R. 2013. “Community Intelligence and Social Media Services: A Rumor Theoretic Analysis of Tweets during Social Crises,” MIS Quarterly, 37(2), 407-426.

Oh, O., Eom, C., and Rao, H. R. 2015. “Research Note: Role of Social Media in Social Change: An Analysis of Collective Sense Making During the 2011 Egypt Revolution,” Information Systems Research (26:1), pp. 210-223.

Oh, O., Kwon, K. H., and Rao, H. R. 2010. “An Exploration of Social Media in Extreme Events: Rumor Theory and Twitter during the Haiti Earthquake,” Proceedings of the International Conference on Information Systems, St. Louis, MO.

O’lear, S. 1999. “Networks of Engagement: Electronic Communication and Grassroots Environmental Activism in Kaliningrad,” Geografiska Annaler: Series B, Human Geography (81:3), pp. 165-178.

Orlikowski, W. J. 2007. “Sociomaterial Practices: Exploring Technology at Work,” Organization Science (28:9), pp. 1435– 1448.

Orlikowski, W. J., and Scott, S. 2008. “Sociomateriality: Challenging the Separation of Technology, Work, And Organization, Academy of Management Annals (2:1), pp. 433–474.

Pan, Z., and Kosicki, G. M. 1993. “Framing Analysis: An Approach to News Discourse,” Political Communication (10:1), pp. 55-75.

Papacharissi, Z., and Oliveira, M. F. 2012. “Affective News and Networked Publics: The Rhythms of News Storytelling on #Egypt,” Journal of Communication, 62(2), pp. 266-282.

Paxton, P. 1999. “Is Social Capital Declining in the United States? A Multiple Indicator Assessment,” American Journal of Sociology (105:1), 88-127.

Peng, C.-Y. J., Lee, K. L., and Ingersoll, G. M. 2002. “An Introduction to Logistic Regression Analysis and Reporting,” The Journal of Educational Research (96:1), pp. 3-14.

Pennebaker, J. W., Boyd, R. L., Jordan, K., and Blackburn, K. 2015. The Development and Psychometric Properties of LIWC2015 (https://repositories.lib.utexas.edu/bitstream/handle/2152/31333/ LIWC2015\_LanguageManual.pdf?Sequence=3)

Petrescu, M., and Korgaonkar, P. 2011. “Viral Advertising: Definitional Review and Synthesis,” Journal of Internet Commerce (10:3), pp. 208-226.

Pichardo, N. A. 1997. “New Social Movements: A Critical Review,” Annual Review of Sociology (23:1), pp. 411-430.

Pitta, D. A., and Fowler, D. 2005a. “Internet Community Forums: An Untapped Resource for Consumer Marketers,” Journal of Consumer Marketing (22:5), pp. 265-274.

Pitta, D. A., and Fowler, D. 2005b. “Online Consumer Communities and Their Value to New Product Developers,” Journal of Product & Brand Management (14:5), pp. 283-291.

Powers, D. M. 2011. “Evaluation: From Precision, Recall and F-Measure to ROC, Informedness, Markedness and Correlation.” Journal of Machine Learning Technologies, 2(1), 37-63

Puniskis, D., Laurutis, R., and Dirmeikis, R. 2015. “An Artificial Neural Nets for Spam E-Mail Recognition.” Elektronika ir Elektrotechnika, 69(5), 73-76.

Rai, A. 2017. “Avoiding Type III Errors: Formulating IS Research Problems That Matter,” MIS Quarterly (41:2), pp. iii-vii.

Ramos, J. 2003. “Using tf-idf to determine word relevance in document queries.” In Proceedings of the first instructional conference on machine learning (Vol. 242, pp. 133-142).

Rao, P. R., and Devi, S. L. 2017. “EventXtract-IL: Event Extraction from Social Media Text in Indian Languages@ FIRE 2017-An Overview, in Proceedings of the Forum for Information Retrieval and Evaluation, pp. 130-135.

Rayport, J. 1996. “The Virus of Marketing,” Fast Company, https://www.fastcompany.com/90663652/from-calamity-toopportunity-heres-how-business-leaders-found-opportunity-inthe-pandemic?page=0%2C1

Roodman, D. 2008. “Through the Looking Glass, and What OLS Found There: On Growth, Foreign Aid, and Reverse Causality,” Center for Global Development Working Paper No. 137 (http://dx.doi.org/10.2139/ssrn.1100142).

Rowe, M., and Alani, H. (2014) Mining and Comparing Engagement Dynamics across Multiple Social Media Platforms, in Proceedings of the ACM Conference on Web Science, pp. 229–238.

Sargan, J. D. 1988. “Testing for Misspecification after Estimating Using Instrumental Variables,” Contributions to Econometrics, Cambridge University Press, pp. 213-235.

Schmidt, E. and Cohen, J. 2013. The New Digital Age: Reshaping the Future of People, Nations and Business.

Schroer, J., and Hertel, G. 2009. “Voluntary Engagement in an Open Web-Based Encyclopedia: Wikipedians and Why They Do It,” Media Psychology (12:1), pp. 96-120.

Selander, L., and Jarvenpaa, S. L. 2016. “Digital Action Repertoires and Transforming a Social Movement Organization,” MIS Quarterly (40:2), pp. 331-352

Sheng, Q., and Gao, S. 2013. “Opinion Leaders of Chinese Microblogs: Features, Types and Development Trends,” Journal of Northeastern University (Social Science) (15:4), pp. 381-385.

Shoenberger, H., and Tandoc Jr, E. 2014. “Updated Statuses: Understanding Facebook Use through Explicit and Implicit Measures of Attitudes and Motivations,” Online Journal of Communication and Media Technologies (4:1), pp. 217-244.

Smelser, N. 1963. Theory of Collective Behavior, Free Press.

Smith, J., and Fetner, T. 2010. “Structural Approaches in the Sociology of Social Movements,” in Handbook of Social Movements across Disciplines, Bert Klandermans and Conny Roggeband (eds.), Springer, pp. 13-58.

Staiger, D. O., and Stock, J. H. 1994. “Instrumental Variables Regression with Weak Instruments,” National Bureau of Economic Research, Technical Working Paper no. 151. (https://www.nber.org/papers/t0151)

Starbird, K., and Palen, L. 2012. “(White et al.) Will the Revolution be Retweeted? Information Diffusion and the 2011 Egyptian Uprising,” in Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work, pp. 7-16.

Stehman, S. V. 1997. “Selecting and Interpreting Measures Of Thematic Classification Accuracy,” Remote Sensing of Environment (62-1), pp. 77-89.

Steinert-Threlkeld, Z. C., Mocanu, D., Vespignani, A., and Fowler, J. 2015. “Online Social Networks and Offline Protest,” EPJ Data Science (4:1), pp. 1-9.

Steinfield, C., Ellison, N. B., and Lampe, C. 2008. “Social Capital, Self-Esteem, and Use of Online Social Network Sites: A Longitudinal Analysis,” Journal of Applied Developmental Psychology (29:6), pp. 434-445.

Stieglitz, S., and Dang-Xuan, L. 2013. “Emotions and Information Diffusion in Social Media—Sentiment of Microblogs and Sharing Behavior,” Journal of Management Information Systems (29:4), pp. 217-248.

Street, A., Murray, T.A., Blitzer, J., and Patel, R. 2015. “Estimating Voter Registration Deadline Effects with Web Search Data,” Political Analysis (23:2), pp.225-241.

Suh, B., Hong, L., Pirolli, P., and Chi, E. H. 2010. “Want to be Retweeted? Large Scale Analytics on Factors Impacting Retweet in Twitter Network,” in Proceedings of the IEEE Second International Conference on Social Computing, pp. 177-184.

Susarla, A., Oh, J.-H., and Tan, Y. 2012. “Social Networks and the Diffusion of User-Generated Content: Evidence from Youtube,” Information Systems Research (23:1), pp. 23-41.

Svensson, M. 2014. “Voice, Power and Connectivity in China’s Microblogosphere: Digital Divides on Sinaweibo,” China Information (28:2), pp. 168-188.

Thorndike, E. L. 1931. Human Learning, Century.

Tilly, C. 1977. “From Mobilization to Revolution,”, Center for Research on Social Organization, University of Michigan, Ann Harbor Working Paper (Available at https://www.lib.umich.edu/collections/deep-blue-repositories.

Trusov, M., Bodapati, A., and Bucklin, R. 2010. “Determining Influential Users in Internet Social Networks,” Journal of Marketing Research (47:4), pp. 643–658.

Tsugawa, S., and Ohsaki, H. 2017. “On the Relation between Message Sentiment and Its Virality on Social Media,” Social Network Analysis and Mining (7:1), p. 19-33.

Tsur, O., and Rappoport, A. 2012. “What’s in a Hashtag? Content Based Prediction of the Spread of Ideas in Microblogging Communities,” in Proceedings of the 5th ACM International Conference on Web Search and Data Mining, pp. 643-652.

Tucker, C. E. 2014. “Social Networks, Personalized Advertising, and Privacy Controls,” Journal of Marketing Research (51:5), pp. 546- 562.

Tufekci, Z., and Wilson, C. 2012. “Social Media and the Decision to Participate in Political Protest: Observations from Tahrir Square,” Journal of Communication (62:2), 363-379.

Turner, J. C. 1987. Rediscovering the Social Group: Self-Categorization Theory. Blackwell.

Turner, R. H., and Killian., L. M. 1957. Collective Behavior, Prentice-Hall.

Turner, R. H., and Killian, L. M. 1972. Collective Behavior, Prentice-Hall.

Ugander, J., Backstrom, L., Marlow, C., and Kleinberg, J. 2012. “Structural diversity in social contagion,” in Proceedings of the National Academy of Sciences, Article 201116502.

Vaast, E., and Walsham, G. 2013. “Grounded Theorizing for Electronically Mediated Social Contexts,” European Journal of Information Systems (22:1), pp. 9-25.

Valecha, R., Bachura, E., Chen, R., and Rao, H. R. (2016). “An Exploration of Public Reaction to the OPM Data Breach Notifications,” Proceedings of the Workshop on E-Business, Dublin, Ireland.

Valecha, R., Oh, O., and Rao, H. R. (2013). “An Exploration of Collaboration over Time in Collective Crisis Response during the Haiti 2010 Earthquake,” Proceedings of International Conference on Information Systems, Milan, Italy.

Valecha, R., Rao, H. R., Upadhyaya, S., and Sharman, R. (2019). “An Activity Theory Approach to Modeling Dispatch-Mediated Emergency Response Communications,” Journal of the Association for Information Systems (20:1), pp. 33-57.

Valecha, R., Volety, T., Kwon, H., and Rao, H. R. (2019). “The Effect of Threat and Proximity on Cyber-Rumor Sharing,” Proceedings of International Conference on Secure Knowledge Management, Goa, India.

van der Lans, R., Cote, J. A., Cole, C. A., Leong, S. M., Smidts, A., Henderson, P. W., Bluemelhuber, C., Bottomley, P. A., Doyle, J. R., and Fedorikhin, A. 2009. “Cross-National Logo Evaluation Analysis: An Individual-Level Approach,” Marketing Science (28:5), pp. 968-985.

van Stekelenburg, J., and Klandermans, B. 2010. “Individuals in movements,” in Handbook of Social Movements across Disciplines, B. Klandermans and C. Roggeband (eds.), Springer, pp. 157-204.

Venkatesan, S., Yaraghi, N., Rao, H. R., and Oh, O. 2012. “Investigating the Role of Twitter Services in the Egyptian Social Movement,” in Proceedings of the Workshop on Information in Networks, New York, NY.

Vissers S., and Stolle, D. 2014. “Spill-Over Effects between Facebook and On/Offline Political Participation? Evidence from a Two-

Wave Panel Study,” Journal of Information Technology and Politics (11:3), pp. 259-275.

Volety, T., Valecha, R., Vemprala, N., Kwon, H., and Rao, H. R. 2018. “Cyber-Rumor Sharing: The Case of Zika Virus,” Proceedings of the Americas Conference on Information Systems, New Orleans, LA.

Wang, R., Liu, W., and Gao, S. 2016. “Hashtags and Information Virality in Networked Social Movement: Examining Hashtags Co-Occurrence Patterns,” Online Information Review (40:7), pp. 850- 866.

Wasserman, H. 2007. “Is a New Worldwide Web Possible? An Explorative Comparison of the Use of ICTs by Two South African Social Movements,” African Studies Review (50:1), pp. 109-131.

Weller, K., Dröge, E., and Puschmann, C. 2011. “Citation Analysis in Twitter: Approaches for Defining and Measuring Information Flows within Tweets During Scientific Conferences,” in Proceedings of the ESWC2011 Workshop on 'Making Sense of Microposts': Big Things Come in Small Packages: co-located with the 8th Extended Semantic Web Conference, ESWC2011, Heraklion, Crete, Greece.

White, G., Howell, J. A., and Xiaoyuan, S. 1996. In Search of Civil Society: Market Reform and Social Change in Contemporary China, Oxford University Press.

Williams, M. D., Dwivedi, Y. K., Lal, B., and Schwarz, A. 2009. “Contemporary Trends and Issues in IT Adoption and Diffusion Research,” Journal of Information Technology (24:1), pp. 1-10.

Wilson, H. 2019. “March for Archives: An Examination of Five Different Institutions and Their Collecting Efforts of Material from the March for Our Lives Protests,” unpublished master’s thesis, University of North Carolina Chapel Hill, Chapel Hill, NC.

Wilson, C., and Dunn, A. 2011. “The Arab Spring—Digital media in the Egyptian revolution: Descriptive analysis from the Tahrir data set.” International Journal of Communication (5), pp. 1248-1272.

Wilson, J. 1973. Introduction to Social Movements. Basic Books.

Xu, L., Shen, Y., and Chan, H. C. 2017. “Understanding Content Voting Based on Social Foraging Theory,” IEEE Transactions on Engineering Management (64:4), pp. 574-585

Xu, S., and Zhou, A. 2020. “Hashtag Homophily in Twitter Network: Examining a Controversial Cause-Related Marketing Campaign,” Computers in Human Behavior (pp. 102), pp. 87-96.

Xue, T., Stekelenburg, J. V., and Klandermans, P. 2016. “Online Collective Action in China: A New Integrated Framework,” Sociopedia.isa, DOI: 10.1177/205684601661.

Yang, G. 2003. “The Co-Evolution of the Internet and Civil Society in China,” Asian Survey (43:3), pp. 405-422.

Yang, J., Yao, C., Ma, W., and Chen, G. 2010. “A Study of the Spreading Scheme for Viral Marketing Based on a Complex Network Model,” Physica A: Statistical Mechanics and its Applications (389:4), pp. 859-870.

Ye, S., and Wu, S. 2010. “Measuring Message Propagation and Social Influence on Twitter.com,” inProceedings of the International Conference on Social Informatics, pp. 216-231.

Ye, S., and Wu, S. F. 2010. “Measuring Message Propagation and Social Influence on Twitter.com,” Proceedings of the International Conference on Social Informatics, pp. 216-231.

Yu, J., Jiang, Z., and Chan, H. 2011. “The Influence of Socio-Technological Mechanisms on Individual Motivation towards Knowledge Contribution in Problem- Solving Virtual

Communities,” IEEE Transactions on Professional Communication (54:2), pp. 152-167.

Zald, M. N., and Ash, R. 1966. “Social Movement Organizations: Growth, Decay and Change,” Social Forces (44:3), 327–341.

Zhang, M., Sun, C., and Liu, W. 2011. “Identifying Influential Users of Micro-blogging Services: A Dynamic Action-based Network Approach,” in Proceedings of the Pacific Asia Conference on Information Systems, Brisbane, Australia.

## About the Authors

Srikanth Venkatesan is an assistant professor of computer information systems at Cal Poly Pomona. He received his Ph.D. and M.S. in management information systems from the State University of New York at Buffalo. His research interests include online social networks and graph theory, online health information quality, misinformation, cybersecurity, and cloud computing.

Rohit Valecha is an associate professor of information systems and cyber security at the University of Texas at San Antonio. He has research interests in the use of social media for crisis response. His research on detection, mitigation, and prevention of misinformation has been funded by NSF. His research has been published in Journal of the Association for Information Systems, Information Systems Frontiers, International Journal of Information Management, and several other ACM and IEEE journals. He received his M.S. in computer science and Ph.D. in management science and systems from the State University of New York at Buffalo.

Niam Yaraghi is an assistant professor of business technology at Miami Herbert Business School at the University of Miami and a nonresident senior fellow at the Brookings Institution’s Center for Technology Innovation. His research is focused on the economics of health information technologies. In particular, he studies the business models and policy structures that incentivize the transparency, interoperability, and sharing of health information among patients, providers, payers, and regulators. He has a B.Sc in industrial engineering from the Isfahan University of Technology in Iran, and an M.Sc. from the Royal Institute of Technology in Sweden. He received his Ph.D. in management science and systems from the State University of New York at Buffalo.

Onook Oh is an associate professor of information systems at the University of Colorado at Denver. He is currently working with a next-generation theory for information and organization research that can take into account the climate change issues as well as a new mode of labor that is introduced by platform technologies. His research has been published in MIS Quarterly, Information Systems Research, Information Systems Frontier and other journals.

H. Raghav Rao is AT&T Chair Professor of ISCS, College of Business and a professor of computer science (courtesy appointment) at the University of Texas, San Antonio. He graduated from Purdue University. He was a distinguished visiting faculty at Swansea University in the summer of 2020 and 2021 and will be a Fulbright-Nehru scholar at IIM Bangalore in the summer of 2022 and 2023.

## Appendix

<table><tr><td colspan="13">Table A1. Correlation Matrix (All significant at p &lt; 0.001)</td></tr><tr><td></td><td>VIF</td><td>Retweet</td><td>Anti-dictator</td><td>Freedom</td><td>Protest</td><td>Tahrir</td><td>Centrality</td><td>Tenure</td><td>Follower</td><td>Status</td><td>URL</td><td>t</td></tr><tr><td>Retweet</td><td>NA</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Anti-dictator</td><td>2.20</td><td>-0.447</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Freedom</td><td>1.04</td><td>-0.198</td><td>0.409</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Protest</td><td>1.24</td><td>-0.355</td><td>0.613</td><td>0.341</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tahrir</td><td>1.08</td><td>-0.245</td><td>0.512</td><td>0.418</td><td>0.401</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Centrality</td><td>1.04</td><td>0.032</td><td>0.351</td><td>0.216</td><td>0.356</td><td>0.283</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tenure</td><td>1.24</td><td>0.030</td><td>0.286</td><td>0.159</td><td>0.238</td><td>0.215</td><td>0.244</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>Follower</td><td>1.77</td><td>0.296</td><td>-0.231</td><td>-0.102</td><td>-0.133</td><td>-0.168</td><td>-0.011</td><td>0.103</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Status</td><td>1.72</td><td>0.298</td><td>-0.239</td><td>-0.100</td><td>-0.149</td><td>-0.170</td><td>-0.023</td><td>0.055</td><td>0.661</td><td>1</td><td></td><td></td></tr><tr><td>URL</td><td>2.30</td><td>-0.478</td><td>0.710</td><td>0.345</td><td>0.658</td><td>0.428</td><td>0.336</td><td>0.266</td><td>-0.213</td><td>-0.234</td><td>1</td><td></td></tr><tr><td>t</td><td>1.17</td><td>0.014</td><td>0.078</td><td>0.067</td><td>-0.047</td><td>0.182</td><td>-0.215</td><td>0.260</td><td>-0.078</td><td>-0.068</td><td>-0.021</td><td>1</td></tr></table>

To report the effectiveness of the classifier, we utilized an error matrix, commonly referred to as a confusion matrix (Stehman 1997). The confusion matrix is widely used in the literature to evaluate prediction and classification algorithms (Puniskis et al. 2006). The confusion matrix is a relevant measure to evaluate the performance of the classification model. Within the confusion matrix, the lower the number of misclassifications, the better the performance. The extent of misclassification is assessed by the number of Type I and Type II errors.

We developed a confusion matrix (see Table A2) to evaluate the classification model. The columns in the confusion matrix represented predicted activity, and the rows represented the actual activity. The confusion matrix allowed us to determine the percentage of correctly classified and misclassified activities. The performance metrics employed in this paper included those used in prior research: overall accuracy, precision, recall, and F-measure (Abbasi et al. 2015). With the help of the confusion matrix, we defined the evaluation metrics in Table A3, where A0, A1, B0, B1 refer to the number of activities falling into the actual and predicted activities categories.

Following Powers (2011), we defined accuracy as the proportion of the total number of activities that are correctly classified. Precision was the proportion of the predicted activities that are correctly classified. The recall was the proportion of actual activities that are correctly classified. F-measure was the geometric mean of precision and recall. We also used Area under the ROC Curve (AUC) as the ratio of true positive to false positive over variant thresholds of the classifier’s decision boundary. AUC has often been recommended as a measure of machine learning algorithms, especially in supervised learning when compared to overall accuracy (Bradley 1997). These are defined in Table A4. The results of the prediction are shown in Table A5 and Table A6.

Table A2. Confusion Matrix for Performance Measures

<table><tr><td rowspan="2" colspan="2"></td><td colspan="2">Predicted activity</td></tr><tr><td>No (=0)</td><td>Yes (=1)</td></tr><tr><td rowspan="2">Actual activity</td><td>No (=0)</td><td>A0</td><td>A1</td></tr><tr><td>Yes (=1)</td><td>B0</td><td>B1</td></tr></table>

Table A3. Performance Measures

<table><tr><td colspan="2">Accuracy =  $\frac{A0 + B1}{A0 + A1 + B0 + B1}$  =  $\frac{\text{true positives}}{\text{true positives} + \text{true negatives} + \text{false positives} + \text{false negatives}}$ Precision =  $\frac{B1}{A1 + B1}$  =  $\frac{\text{true positives}}{\text{true positives} + \text{false positives}}$ Recall =  $\frac{B1}{B0 + B1}$  =  $\frac{\text{true positives}}{\text{true positives} + \text{false negatives}}$  $F - \text{measure} = \sqrt{\text{Precision} * \text{Recall}}$ </td></tr><tr><td colspan="2">Table A4. Performance Metrics used for the Machine Learning Models</td></tr><tr><td>Evaluation measure</td><td>Description</td></tr><tr><td>Accuracy</td><td>Calculates the percentage of correctly predicted instances of activities.</td></tr><tr><td>Precision</td><td>Measures whether the prediction is precise or not.</td></tr><tr><td>F-measure</td><td>Calculates the weighted harmonic mean of precision and recall.</td></tr><tr><td>AUC</td><td>The performance of a machine learning algorithm</td></tr></table>

<table><tr><td colspan="6">Table A5. Overall Performance of the Machine Learning Models</td></tr><tr><td></td><td>Accuracy</td><td>Precision</td><td>Recall</td><td>F-Score</td><td>AUC-score</td></tr><tr><td>Anti-dictator</td><td>99.60%</td><td>85.71%</td><td>75.00%</td><td>80.00%</td><td>73.00%</td></tr><tr><td>Freedom</td><td>98.81%</td><td>100%</td><td>43.75%</td><td>60.87%</td><td>71.00%</td></tr><tr><td>Protest</td><td>91.91%</td><td>77.65%</td><td>61.11%</td><td>68.39%</td><td>81.00%</td></tr></table>

Table A6. AUC for the Machine Learning Models  
![](/api/attachments/J6V2QKA7/fulltext/images/5e13e7732e467507195fc04d86d4c7e6ec18280485174a554a8601c1165aadb7.jpg)

rf freedom ROC for 10 folds  
![](/api/attachments/J6V2QKA7/fulltext/images/5a87d4e4b9d0857a4c7f653066377abc3cdde97bf8f048c6059f92a10aabe0ed.jpg)

![](/api/attachments/J6V2QKA7/fulltext/images/a1aaab9f97f0b1c14b550b87c42221079fcc4333fcb7aa73022af738931b6f78.jpg)

Table A7. Results of Equal Time Periods Analysis

<table><tr><td>DV: retweet influence t</td><td>Coefficient</td><td>Robust S.E.</td><td>Odds ratio</td><td colspan="2">95% confidence interval</td></tr><tr><td>Intercept</td><td>-0.106</td><td>2.391</td><td>NA</td><td>-4.794</td><td>4.582</td></tr><tr><td>Anti-dictator activity i, t-1</td><td>-6.838</td><td>18.774</td><td>1.355</td><td>-43.634</td><td>29.958</td></tr><tr><td>Freedom activity i, t-1</td><td>12.888</td><td>37.069</td><td>1.119</td><td>-59.767</td><td>85.543</td></tr><tr><td>Tahrir activity i, t-1</td><td>4.337</td><td>11.730</td><td>1.384</td><td>-18.653</td><td>27.326</td></tr><tr><td>Protest activity i, t-1</td><td>1.170</td><td>3.333</td><td>1.062</td><td>-5.361</td><td>7.702</td></tr><tr><td>Tenure i, t-1</td><td>0.569***</td><td>0.135</td><td>1.516</td><td>0.305</td><td>0.832</td></tr><tr><td>Ln(Followers)</td><td>0.485</td><td>0.350</td><td>1.496</td><td>-0.202</td><td>1.171</td></tr><tr><td>Centrality i, t</td><td>0.157</td><td>0.840</td><td>1.685</td><td>-1.489</td><td>1.802</td></tr><tr><td>Influence i, t-1</td><td>0.177</td><td>0.123</td><td>1.178</td><td>-0.064</td><td>0.419</td></tr><tr><td>Ln(Status i, t-1)</td><td>-0.405</td><td>0.419</td><td>0.824</td><td>-1.227</td><td>0.416</td></tr><tr><td>URL i, t-1</td><td>1.119</td><td>3.700</td><td>0.633</td><td>-6.133</td><td>8.372</td></tr><tr><td>t</td><td>-0.278</td><td>0.153</td><td>0.962</td><td>-0.577</td><td>0.021</td></tr></table>

Note: p-value < 0.10; \* p-value < 0.05; \*\* p-value < 0.01; \*\*\* p-value < 0.001

Lazer et al. (2009) have proposed the idea of computational social science. Since then, traditional social science research topics have coalesced around the use of big data. There is empirical evidence that computational social science methods exceed the prediction power of traditional social science methods that historically relied upon survey or interview data (Mann 2016). This superior predictive power might come from the simple fact that it cares only what people did to the exclusion of what they think, decide, plan, or intend.

In Table A8, we summarize studies that have taken a computational social science approach to examine social movements.

<table><tr><td colspan="5">Table A8. Computational Social Science Studies</td></tr><tr><td>Reference</td><td>Research context</td><td>Methodology</td><td>Data sources</td><td>Major findings</td></tr><tr><td>Oh et al.(2015)</td><td>Role of Twitter in shaping collective sensemaking during the 2011 Egyptian Revolution</td><td>Time-series regression analysis</td><td>Twitter</td><td>Hashtag feature of Twitter contributed to shaping and maintaining situational awareness during the 2011 Egyptian Revolution</td></tr><tr><td>Street et al.(2015)</td><td>Estimating the relationship between web search queries and voting registration for Election Day.</td><td>Regression analysis</td><td>Google web search log collected from Google Trend website.</td><td>If the voter registration deadline has been expanded to Election Day, an additional 3 to 4 million of U.S. citizens might have registered in time to vote.</td></tr><tr><td>Wattal et al.(2010)</td><td>Influence of “Web 2.0” in the process of the 2008 presidential election campaigning and candidate performance.</td><td>Descriptive and regression analysis.</td><td>Multiple sources. (1) website data, (2) YouTube views friends’ data, (3) newspapers, TV, radio, and blogs.</td><td>During the 2008 presidential election campaign, the Internet in general and blogs, in particular, have changed the nature of political competition.</td></tr><tr><td>Ackland and O’Neil (2011)</td><td>Roles of the internet in shaping collective identity to perform the social movement.</td><td>Social network analysis.</td><td>Websites of over 160 environmental activist organizations.</td><td>In shaping collective identity to achieve collective goals of the social movement, social movement organizations’ participation in informal networks and direct control over the means of communication is important.</td></tr><tr><td>Wang et al.(2016)</td><td>Examination of how Twitter’s hashtags drive information during the 2011 Occupy Wall Street social movement</td><td>Social network analysis.</td><td>Twitter</td><td>Social movement participants use strategic hashtags to reach different social circles.</td></tr><tr><td>Current manuscript</td><td>Examination of how individual Twitter user’s activities and Twitter’s network structure affect message dissemination through retweets during the 2011 Egyptian Revolution.</td><td>Social network analysis and regression.</td><td>Twitter</td><td>During the 2011 Egyptian Revolution, message dissemination in Twitter has been influenced by the following factors: (1) “who and where” of a Twitter user, (2) longevity of Twitter activity, (3) follower network, and (4) network centrality.</td></tr></table>
