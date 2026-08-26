---
otero_id: 11040
otero_key: "XRJ3DR43"
title: "Influentials, Imitables, or Susceptibles? Virality and Word-of-Mouth Conversations in Online Social Networks"
authors: "Anjana Susarla; Jeong-Ha Oh; Yong Tan"
year: "2016"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.2016.1172454"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Influentials, Imitables, or Susceptibles? Virality and Word-of-Mouth Conversations in Online Social Networks

Anjana Susarla, Jeong-Ha Oh & Yong Tan

To cite this article: Anjana Susarla, Jeong-Ha Oh & Yong Tan (2016) Influentials, Imitables, or Susceptibles? Virality and Word-of-Mouth Conversations in Online Social Networks, Journal of Management Information Systems, 33:1, 139-170, DOI: 10.1080/07421222.2016.1172454

To link to this article: http://dx.doi.org/10.1080/07421222.2016.1172454

![](/api/attachments/XRJ3DR43/fulltext/images/66304475697be49bdaf20d7b35958da638ee2c0e53ef51554353c8cb78f68869.jpg)

Published online: 17 Jun 2016.

![](/api/attachments/XRJ3DR43/fulltext/images/a2eb98c8b798675b1927dc4322d4e49a0aa3cba454629e32b0297b6d2af488de.jpg)

Submit your article to this journal

![](/api/attachments/XRJ3DR43/fulltext/images/ac8f149f2bc8b5a5a3c8779385e018e5e53e6f9ac1c39410d7a361f03b23ff1b.jpg)

Article views: 6

![](/api/attachments/XRJ3DR43/fulltext/images/104040c99ca891fcd3e169c122e5fe3d3fe786b5dfeda50e61b517ed3716d8ae.jpg)

View related articles

![](/api/attachments/XRJ3DR43/fulltext/images/91e88a1dbe91e41c5d1edde5b9cd359bf6bf283f88aa37a0ff0c9b55b4986401.jpg)

View Crossmark data

# Influentials, Imitables, or Susceptibles? Virality and Word-of-Mouth Conversations in Online Social Networks

ANJANA SUSARLA, JEONG-HA OH, AND YONG TAN

ANJANA SUSARLA (asusarla@broad.msu.edu) is an associate professor at the Eli Broad College of Business, Michigan State University. Her research has appeared in Information Systems Research, Journal of Management Information Systems, Management Science, and MIS Quarterly. She received her Ph.D. in information systems from the University of Texas at Austin. Her research focuses on big data analytics, contracts and sourcing, cloud computing, social media, and network science.

JEONG-HA OH (jhoh@gsu.edu) is an assistant professor of computer information systems at the Robinson College of Business, Georgia State University. She received her Ph.D. in information systems from the Foster School of Business at the University of Washington in Seattle. Her current research focuses on health-care analytics, online social networks analysis, information cascade, and content diffusion in social media. She has published in Information Systems Research.

YONG TAN (ytan@uw.edu; corresponding author) is the Neal and Jan Dempsey Professor of Information Systems at the Michael G. Foster School of Business, University of Washington, and Chang Jiang Scholar Visiting Chair at the School of Economics and Management, Tsinghua University. His research interests include social media and networks, mobile and electronic commerce, big data analytics, and economics of information systems. He has published in Information Systems Research, Journal of Management Information Systems, Management Science, Management Information Systems Quarterly, and Operations Research, among others. He is a senior editor of Information Systems Research and a member of the Board of Editors of the Journal of Management Information Systems.

ABSTRACT: Motivated by the rise of social media platforms that achieve a fusion of content and community, we consider the role of word-of-mouth communications (WOM) structured through a network. Using a data set from YouTube, we examine how cascades of WOM interactions enhance the popularity of videos. We first estimate the impact of channel influence and other network parameters in initiating WOM communications. The probit estimation considers the selection effect in videos that are likely to be associated with a greater propensity to trigger WOM. We find that factors related to a channel’s ability to be a connector and a translator is most likely to result in the incidence of WOM. We then examine how cascades of WOM conversations have persistent impacts on subsequent video popularity. Empirically, the main issue here is heterogeneity in the epidemic potential of a video. Since the threshold might vary across videos, we use a finite mixture model. We also conduct a simultaneous estimation using latent instrumental variables to address endogeneity from unobservables. Our research has implications for researchers and practitioners by highlighting how WOM travels through networks of influence and susceptibility in disseminating awareness, and holds insights in regard to designing social recommendation systems and identifying trending topics in social media.

KEY WORDS AND PHRASES: electronic word of mouth, eWOM, finite mixture model, latent instrumental variables, opinion cascades, peer effects, social media, social recommendations, user-generated content.

A rich literature examines the digitization of word-of-mouth (WOM) communications enabled by information technology (IT) (e.g. [28]). However, the popularity of social media alters the mechanisms by which WOM is triggered and propagated. In contrast to the prior literature on WOM that has highlighted mechanisms such as referrals [64] and personalized recommendations [3], there are limited recruitment strategies by content creators in social media. Recent work has recognized the relatively ephemeral nature of attention (e.g. [19, 62]) and inequality in the popularity of user-generated content. Goldenberg, Oestreicher-Singer, and Reichman [33] characterize user search on platforms such as that of content exploration without a defined target. Content sharing and product discovery on social networks occurs through WOM interactions. Increasingly there is a fusion of content and community [50] whereby users are interested not just in exploring digital content but also in interacting with other users. In particular we are motivated by the success of YouTube, which offers a test bed to study the role of interlinked content and community interactions.

User interactions on YouTube exhibit a two-sided nature in that users participate both in content creation and formation of WOM. Content sharing and discovery on YouTube occurs through user interactions, whereby the platform combines the role of personalization and content discovery (e.g. [50]) to influence the collective popularity of videos posted. WOM is transmitted through the network of social ties, thereby disseminating awareness about videos to potential users. Further, given the experience good aspect of videos, potential viewers would be more interested in watching a video that has been highly viewed and discussed. Such interactions shape the spreading of content and the trajectory of WOM.

Prior literature offers competing perspectives on the mechanisms underlying social influence whereby a few videos become very popular while others languish in obscurity. Susceptibility refers to the responsiveness or persuadability of recipient ties [8]. Gladwell [31] contends that a small number of “mavens” or influentials play a disproportionate role in spreading new ideas, while others posit that the susceptibility of persuadable individuals drives contagion [67]. It has been suggested that product design, rather than social influence, is critical in triggering contagion [2]. Certain characteristics of digital content such as their catchiness or memorability increase the likelihood of being imitated or spread [38].

The success of the viral video hit, Harlem Shake, illustrates that what matters to popularity is the ability of a cultural product to trigger conversations and engage viewers. The Harlem Shake was an amateur video. After being posted on YouTube, a group of YouTube users engaged in a number of conversations that spread on social media, resulting in a large number of responses and discussions [44], creating one of the most popular videos and online memes. In other words, a video morphs into a hit when a susceptible audience acts as brand ambassadors who engage in WOM. While prior literature would suggest that influential users have a large potential viewer base, it is the willingness with which a cluster of susceptible network ties engages with a video, as well as the imitability of content when users post response videos, that turns potential audiences from passive viewers into active commentators and sharers.

It is posited that cascades are caused by endogenous shocks from within a network [24]. We are interested in particular in the cascade or herding through susceptibility as measured in commenting actions. A video acquires visibility and buzz through discussions, comments as well as opinions, actions as well as tastes of an adjacent node. The visibility through initial comments gets magnified when adjacent nodes notice the video. This local phenomenon acquires larger visibility due to the patterns of interactions between the nodes commenting on the video. Since large-scale social networks are highly dynamic, analyzing the local structure and topology of interactions is important to understanding the network phenomenon (e.g. [23]). Models of cascading behaviors on networks [41, 66] provide us a method by which we can quantify the trajectory and the spreading patterns by which social influence is transmitted. YouTube provides a unique opportunity in that both the activity network of user interactions (through actions such as commenting) and the network of social ties (through observable connections such as friendship and subscriptions) are observable. We build on theories of epidemic spreading on networks [41, 66] to quantify the trajectory and spreading patterns by which susceptibility is transmitted. The two questions we explore are:

● What factors impact the incidence of WOM?

● Does the impact of cascades of early WOM persist in subsequent popularity?

We identify two factors important in triggering WOM early in the life of a video, which we define as the first fifteen days from when a video is posted:<sup>1</sup> the influence of central channels and imitability of content posted by the influential nodes. Individuals (or network nodes) that are most connected are highly visible and influential in spreading behaviors (e.g. [37]). A channel’s influence and the imitability of the content posted by the channel could depend upon its prior history. We conduct a probit model whereby we model the incidence of WOM, that is, the probability that a video has received at least one comment in the first fifteen days. Our central thesis is that comments by susceptible ties drive subsequent patterns of video viewership. We therefore examine how cascades of conversations by susceptible ties impact the magnitude and persistence of subsequent popularity of videos (defined as popularity after sixty days). We conduct a finite mixture model (FMM) estimation to model the heterogeneity in channel characteristics that impacts the volume of popularity. To separate WOM created by susceptible ties from WOM created by external links, we use YouTube Analytics to account for conversation driven by links external to the local network. Identification is possible since our method of data gathering lends itself to a distinct categorization as (1) a set of channel characteristics prior to posting of a video, (2) early WOM from commenting interactions in the first fifteen days, and (3) panel data of channel and video statistics sixty days after a video is posted.

Our study makes several contributions to the literature. While the role of social networks in transmitting influence and contagion has long been a topic of interest for researchers (e.g. [52]), visual social media platforms such as YouTube offer new insights into the paths by which ideas propagate on networks (e.g. [41]). In contrast to prior work that has found that product characteristics are the most important in viral marketing [2], we find that it is social engagement with a product that makes it viral. A substantial amount of prior research examines WOM primarily as a mechanism of referrals, or highlights the importance of opinion leaders and influencers; our study suggests that WOM initiated through influential nodes gathers momentum as it cascades through susceptible ties. We also find that videos for which early commenting is important versus those driven by later momentum have distinctly different and path-dependent diffusion curves, with differing impacts on aggregate popularity. An understanding of WOM engagement is important to developing greater knowledge about what users search for and what impacts user experience in online social networks.

## Theory and Hypotheses

## Word of Mouth in Online Social Networks: Theory

YouTube allows three types of connections between users: incoming subscription ties, outgoing subscriptions, and friend ties [60]. Individual channels can friend other channels, subscribe to other channels, or have other channels subscribe to them. A friend relationship is nondirectional and built upon mutual agreement between users whereas subscription relationships are directional and do not rely on mutual agreement. A friend relationship is initiated by an invitation from one channel to another, requiring confirmation from the other. We characterize such networks as undirected networks (e.g. [65]). By contrast, the act of subscription indicates a willingness to visit and watch the videos uploaded by the channel. We therefore distinguish between incoming and outgoing subscriptions of channels. Friend ties are characterized by affinity, incoming subscription ties are instrumental ties characterized by shared interest, and outgoing subscription ties indicate the ability of a channel to draw attention toward itself [60, 70].

We build on several streams of prior literature. First, an extensive literature on social influence posits that individuals are susceptible to contagion from infectious actors (e.g. [67]). This literature broadly considers phenomena where preferences and actions by individuals are dependent on the decisions of others, impacting the aggregate spread of behaviors, such as WOM [67]. Sacerdote [55] examines the impact of social influence on individual choices. Watts and Dodds [67] argue that individuals most susceptible to social contagion play a critical role in the dynamics of contagion. Kempe, Kleinberg, and Tardos [37] identify the information transmission potential of influential nodes. In the information systems (IS) literature, it has been posited that social influence operates through informational as well as normative channels and influences both attitudes and intentions [40]. We also build on a stream of research on the digitization of WOM in IS and marketing (e.g. [21, 28, 32]. Prior research has found a significant impact of interpersonal relationships between consumers in generating WOM (e.g. [33]). Berger and Iyengar [11] suggest that the manner in which products are discussed depends upon the medium used to structure the discussion—that is, online social networks vs. other settings. Prior literature has also suggested that experience-based versus attribute-based product reviews influence the comprehension and assessment behavior of consumers differently [35].

Finally, we build on recent work that has analyzed WOM transmission through online social networks [36, 58, 61]. Qiu, Rui, and Whinston [51] analyze the impact of information exchange through social networks on market outcomes. Trusov, Bucklin, and Pauwels [64] find that WOM referrals have longer carryover effects in online communities. Ma et al. [46] and Muchnik, Aral, and Taylor [49] find that social influence from prior WOM significantly influences subsequent WOM. Our study builds upon this literature in highlighting the networked nature of interactions between susceptible audiences in generating WOM.

## What Triggers Word of Mouth on YouTube?

By definition, word of mouth occurs when there is conversation generated around a phenomenon [32]. Commenting on YouTube has some similarities with WOM in other settings, such as referrals [64] and personalized recommendations [3] explored in prior research. However, there are also some differences between commenting actions on YouTube and WOM primarily from user reviews studied in prior research. In the context of YouTube, there is limited prerelease promotional activity compared to that of other entertainment products (e.g. [22]). Compared to WOM in traditional settings, YouTube changes the nature of interaction from dyadic to multiparty interactions, making it possible to develop networked relationships between groups of users. Tang, Gu, and Whinston [63] suggest that individuals post content on YouTube driven by a desire for exposure and reputation as well as for motives of revenue. Comments on videos are a critical mechanism by which videos acquire such exposure and reputation. Comments are posited to help in framing a narrative about events and memes [43]. Another motive for commenting on videos is identity signaling [10].

While there is a rich literature on why WOM matters (e.g. [28, 32]), the extant literature has not investigated the mechanisms by which early stage WOM influences subsequent popularity. Once the focal channel posts a video, actions such as comments on a video are prominently highlighted in the newsfeed of the channels connected to it. At the same time, the focal channel can interact by responding to posted comments, which can also be observed by others. Comments constitute a publicly observable signal to other users, thus a measurable way of inferring cascades. Since commenting is visible to others, it provides a method to observe social interactions, the path of information flow and influence transmission. While infectiousness has been examined as a part of observational learning or mimetism, the networked structure of YouTube interactions makes it easier to observe how information epidemics are triggered online (e.g. [1]). YouTube also makes it easy to observe the manner in which users broadcast preferences and the paths of information transmission between users. Our analysis is based on the insight that even when the paths of influence are not directly observable, the sequence of comments generating a cascade is observable. By analyzing the cascade created by interactions between networked actors through exploring comments on videos, we can understand how informational cues inherent in WOM lead to durable popularity of a video. Table 1 highlights different mechanisms by which word of mouth transmission has been studied and the novel context studied in this paper.

Table 1. Mechanisms of Word-of-Mouth Transmission

<table><tr><td>Theoretical construct</td><td>Mechanism of transmission</td><td>Aspects of social media highlighted in prior literature</td><td>Novel contributions of our work</td></tr><tr><td>Propensity to engage in WOM</td><td>Emotional triggers</td><td>Identity signaling [10], interpersonal relationships, emotional cues [49]</td><td>Influence in triggering WOM</td></tr><tr><td>Influence</td><td>Prestige and leadership</td><td>Opinion leadership [52]; tie strength between influencer and recipient [15]; idea propagation from two sided interaction [41]</td><td>Impact of connectors and mavens in triggering WOM</td></tr><tr><td>Susceptibility</td><td>Localized contagion</td><td>Normative interpersonal influence vs. informational interpersonal influence [8]</td><td>Cascade of WOM created by susceptible actors</td></tr><tr><td>Imitability</td><td>Mimicry of others&#x27; behavior</td><td>Imitation and divergence in behavior as a means of identity signaling [10, 13]; visible actions in networks increase imitability (e.g. [1])</td><td>Responses as conversations and memetic diffusion</td></tr></table>

## Channel Influence and Initiation of WOM

Berger and Schwartz [12] suggest that WOM in online communities is driven by accessibility in terms of public visibility or cues. A channel in an influential position on YouTube commands more attention. Thus it is likely that when such a channel posts a video, there is an audience that will notice the video and comment on it. In particular, we examine two different ways by which channel influence matters to the initiation of WOM. Connectors are held to be actors with a great number of connections [31], commonly associated with individuals with high degree centrality [16]. The degree centrality of a node (channel) captures the ability and the opportunity of a node to disseminate information about videos in the local network. The more central the network position of the actor, the more the actor is a channel of relational information to others [65], is more involved in the network [14], and occupies a position of social influence [17]. On the other hand, translators are individuals who are critical to the process of diffusion of ideas and information [16]. We conceptualize a channel’s ability to be a translator when that channel has a greater ability to control the flow of information over the network, and is seen as a source of novel information to others. We therefore hypothesize:

Hypothesis 1a: Channel influence as a connector has a significant positive impact on the likelihood of getting comments.

Hypothesis 1b: Channel influence as a translator has a significant positive impact on the likelihood of getting comments in the first fifteen days.

## Susceptibility and Cascading in Conversations

We examine how susceptibility enhances the overall visibility of videos on YouTube. We examine susceptibility through user interactions. Figure 1 illustrates WOM communications among susceptible ties. When a focal channel posts a video, connected nodes commenting on the video increase exposure of other channels in direct contact with the focal channel and other commenting nodes. While a number of YouTube watchers advise on the importance of building a large potential viewer base through building a community of friends and subscribers [68], it is the susceptibility of the commenters, rather than the influence of the channel alone, that turns potential audiences from passive viewers into active commentators and sharers.

Shi and Whinston [58] posit that learning through networks occurs differently from observational learning in other settings. We examine how the structure of cascade from commenting activity has a persistent impact on popularity. This sequence of conversations creates a “friendship ripple” [39], that is, the process whereby each node exerts a network neighborhood effect in inducing neighboring ties to comment on a video. Bikhchandani, Hirshleifer, and Welch [13] suggest that cascades occur in simple binary choice decisions where imperfectly informed agents, acting sequentially, choose the same action as their predecessors, ignoring their private information. Once the focal channel posts a video, the nodes with friend and subscription ties in the local neighborhood are susceptible to the video since they are aware of the new video through notifications and updates. Commenting on a video is a relatively public signal since the commenting action transmits information to others, increasing susceptibility of adjacent ties. When adjacent ties comment on the focal video, the conversation has the potential to spread within the local network. In this case, an adjacent node joins in the conversation, and can draw in nodes connected to it through friendship and subscription ties. Nodes that are unconnected to the focal node decide to join in the conversation, and commenting acts as a sequential communication. The networked structure of interactions creates a neighborhood effect that provides an impetus for others to join the conversation, eventually increasing the visibility of a video. Such conversations ripple beyond the network neighborhood, leading to an aggregate mass of commenting activity on the video. Thus, cascades in commenting activity in the first fifteen days make it more likely that a video is shared and discovered by casual users, making it likely that a video experiences a durable surge in popularity.

<table><tr><td><img src="/api/attachments/XRJ3DR43/fulltext/images/8655c78f65a32989829721c14a7b9b459506d3666c96e27206e83bb3b0bc2be1.jpg"/>(a) A video is posted by the focal channel</td><td><img src="/api/attachments/XRJ3DR43/fulltext/images/6e3db415cfe249eb04f4c96a91e6438c59e2ecbb3f3145f9fa205933700b6d57.jpg"/>(b) A second channel comments on a video posted by the focal channel</td><td><img src="/api/attachments/XRJ3DR43/fulltext/images/bda0e0d0fbadc523d0aaf1a0d913b53e30697c81f1e84b29266ebd0959e7f2ea.jpg"/>(c) A third channel comments on a video posted by the focal channel</td></tr><tr><td><img src="/api/attachments/XRJ3DR43/fulltext/images/3e018785c36cb4634e6d2b5defac198e6d5e25d773a5074547a071c7ba782e3d.jpg"/>(d) The conversation between the focal channel and others is visible to other network ties</td><td><img src="/api/attachments/XRJ3DR43/fulltext/images/71811814254dc93d60b511d561950913cddd05c307a3669aeab0994c5bff7069.jpg"/>(e) The focal channel responds to the second comment</td><td><img src="/api/attachments/XRJ3DR43/fulltext/images/c78160dfa1e5f42c4fe409ade957ec96c24c97f3f3fc27a6bd706d3b6c1226f2.jpg"/>(f) The network neighborhood effect induces a third channel to comment on the video</td></tr></table>

Figure 1. Susceptibility and Commenting Interactions

Berger and Schwartz [12] suggest that public visibility of choices makes it easy for people to signal that they identify with others. Multiple conversations increase the propensity of viewing videos, and if a video generates intense interest, such conversations might induce nodes outside the local network to join in the conversation, leading to a large mass of commenting activity. The greater the amount of enthusiasm and intensity of discussion centered on a video in the first fifteen days, the more the video acquires visibility, which contributes to a durable popularity surge in the aggregate network. Thus, we hypothesize:

Hypothesis 2a: The localized cascade in the commenting network in the first fifteen days has a significant positive impact on subsequent video popularity (total number of views after sixty days).

Hypothesis 2b: The number of conversations centered on a video in the first fifteen days has a significant impact on subsequent popularity (total number of views after sixty days).

## Imitability and Subsequent Popularity

It has been posited that individuals tend to imitate others’ behaviors though mechanisms such as localized conformity and observational learning [13], mimetism [48], and identity signaling [10]. Imitation of behavior, when those choices are visible to others, is a form of seeking conformity and convergence with others they identify with and a way of signaling affinity [10]. In online social networks, ideas or content act as memes (e.g. [52]), defined as a contagious unit of cultural information (e.g. [25]). The spread of an idea or meme depends upon the openness and willingness to be infected by the meme [38]. Prior literature posits “video response feature allows users to converse through video” [9, p. 761], and characterizes such responses as a visual meme, which is defined as a statement of mutual awareness or a subject of mutual interest [69]. When channels post responses to a video, it is a way of seeking acceptance directing attention toward themselves and making themselves part of the conversation. Thus:

Hypothesis 3: The number of response in the first fifteen days has a significant impact on subsequent popularity (total number of views after sixty days).

## Data

## Data Gathering Approach

We collected a data set consisting of video information and user information from YouTube.com over a period of two months. We first identified a network boundary by focusing on a community of interest on YouTube (a total of thirteen categories). Our sample community (or group) is drawn from the “music” and “people & blog” categories. The interest group itself forms the network boundary. We imposed a number of screening conditions (provided in an appendix available from the authors). For each user, we collected the complete list of friends, subscribers, and subscriptions. We then followed each new video posted in the sample and tracked the activity in the first fifteen days. We then collected several snapshots of the network five days apart starting from sixty days after the video was posted. The data collection was performed with a PHP script that reads the source code of the individual channel and video web pages and takes a snapshot of the list of videos posted in the targeted group, information about each video, and the friend and subscribers lists of each member.

## Channel History Prior to Posting a Video

Within the local network structure, the degree centrality [65] of a node (channel) measures the size of the proximate network of the node, and thus captures the ability of and opportunity for a node to disseminate information about videos and the aggregate level of connectedness of a node in the local network. An actor with a high degree centrality denotes where “the action is” in the network [65]. An actor in a central network position is a channel of information to others [65], has greater social influence [17], and is more involved in the network [14]. We examined the degree centrality in the three types of social ties—friend ties, incoming and outgoing subscriptions of each channel. Table 2 describes the measures prior to video posting, which are used to validate H1a and H1b.

## Activity in the First Fifteen Days After a Video Is Posted

Viewing patterns indicate that most videos reach an epidemic threshold at fifteen days. The epidemic threshold in theoretical parlance [20] denotes the threshold below which a viral infection dies out. Practitioners emphasize the importance of half-life, by which time a video could accumulate almost half of its eventual audience. Building on statistics from Tube Mogul, which is an analytics firm that monitors social media engagement, we considered fifteen days as a threshold. TubeMogul reports cite that the first fifteen days of a video are very critical to building visibility and engagement. Therefore, we feel justified in our approach of using the first fifteen days as crucial to the formation and propagation of WOM. We collected the following information in this time period:

Table 2. Measures Collected Prior to Posting of a Video

<table><tr><td>Hypothesis</td><td>Variable</td><td>Measure</td></tr><tr><td rowspan="3">Channel&#x27;s influence as a connector (H1a)</td><td>nrmdeg.insubs</td><td>Normalized degree centrality in the incoming subscription network</td></tr><tr><td>nrmdeg.frn</td><td>Normalized degree centrality in the friend network</td></tr><tr><td>nrmdeg.outsubs</td><td>Normalized degree centrality in the outgoing subscriber network</td></tr><tr><td rowspan="3">Channel&#x27;s influence as a translator (H1b)</td><td>Log(num. insubs_out)</td><td>Total number of incoming subscribers outside the network at time t</td></tr><tr><td>Log(num. outsubs_out)</td><td>Total number of outgoing subscriptions outside the local network</td></tr><tr><td>Log(num.frn_out)</td><td>Total number of friends of a channel outside the network at time t</td></tr></table>

1. Response Videos denotes the number of response videos to a specific video.

2. Video Runtime is the length of a video measured in seconds (vRunT).

3. Video Category is a dummy variable $\nu C a t _ { i j }$ indicating if the video category is music.

4. Links measures the number of user-generated links that lead to a video.

5. Honored is a dummy variable that indicates whether a video is featured as the most viewed or discussed within its own category or in the overall network.

6. Related Videos are showcased by YouTube as related to a specific video, which could be a dynamic categorization. We used a script to obtain a reasonable fraction of such videos.

7. Keywords measures the total number of tags posted by the channel at the date of posting.

Our sample consists of 3,776 videos posted by 913 users, of which 1,190 videos posted by 474 channels have at least one comment posted within the first fifteen days. Table 3 presents a summary of video characteristics. Figure 2 shows a screenshot of comments.

Figure 3 illustrates a sample screenshot. Using Pajek, we mapped the various commenting networks. We used a PHP client library to program a script to retrieve user information and comments feeds for each video. YouTube.com only allows registered users to comment on videos. Comments are archived chronologically. The YouTube Data API, which allows access to YouTube content and user information through the Google Data API, retrieves the archive of comment entries, including comments threads, user ID of commenter, and the date each comment was posted.<sup>3</sup>

Clustering denotes that if two nodes are neighbors of the same third node, there is a greater probability of the two nodes also sharing a tie [30], indicating a high ratio of ties from within groups to ties between groups. Clustering enhances connectivity and reachability wherein commentators are linked by multiple redundant paths [57], increasing the number of paths of transmission both within and beyond the local network. Greater clustering is likely to trigger further commenting activity, leading to a greater amount of conversations centered on the video. The clustering coefficient C of a vertex v is defined by:

$$
C C _ {1} (v) = \frac {2 | E (G _ {1} (v)) |}{\deg (v) \cdot (\deg (v) - 1)},
$$

Table 3. Video Characteristics in the Treatment Period (first fifteen days)

<table><tr><td></td><td>Mean</td><td>St. dev.</td><td>Min.</td><td>Max.</td></tr><tr><td colspan="5">All videos</td></tr><tr><td>Number of times a video is watched (cumulative)</td><td>16,528</td><td>279,768.5</td><td>4</td><td>13,449,210</td></tr><tr><td>Number of comments in first fifteen days</td><td>2.53</td><td>17.14</td><td>0</td><td>633</td></tr><tr><td>Average number of distinct commenters (excluding the video owner) on each video in the first fifteen days</td><td>6.7382</td><td>22.116</td><td>0</td><td>66,648</td></tr><tr><td>Number of responses in the first fifteen days</td><td>0.4118</td><td>17.570</td><td>0</td><td>1078</td></tr><tr><td colspan="5">Videos with comments in the first fifteen days</td></tr><tr><td>Number of times a video is watched (cumulative)</td><td>14,270</td><td>86,858.61</td><td>24</td><td>2,078,000</td></tr><tr><td>Number of comments in first fifteen days</td><td>8.02</td><td>29.82</td><td>1</td><td>633</td></tr></table>

![](/api/attachments/XRJ3DR43/fulltext/images/45055f1f05323c591b8f9fa564e07d531bc3af19a1f6ff60f8ef1896407b5206.jpg)  
Figure 2. Screenshot of YouTube Video Comments

where $E ( G _ { 1 } ( \nu ) )$ denotes the number of edges among vertices in one neighborhood of vertex v and deg(v) denotes the degree of vertex v [5]. Figure 4 illustrates clustering in conversations for two videos.<sup>4</sup> Channels commenting on video 2 are more clustered than channels commenting on video 161.

![](/api/attachments/XRJ3DR43/fulltext/images/624bb1d5843beeebe1ea0851c56f519f07488a8aed2187a4e716be822ed27365.jpg)  
Figure 3. Sample Feeds from Data API

![](/api/attachments/XRJ3DR43/fulltext/images/635be1194058a3dd410f4fa5e86ca96fcafdc2883ad42ca05b97b2e41bd93d9d.jpg)  
Figure 4. Clustering and Susceptibility

The k-core measures the maximum distinct set of conversations (around a video), either due to a few popular nodes in the commenting network or popular topics.<sup>5</sup> Vertices belonging to a k-core have to be linked to at least k other vertices of the core. The k-core of a network is its largest subgraph whose vertices have at least k degree [57]; thus the maximal subgraph where every node is adjacent to k other nodes. Nodes in the k-core have greater connectedness, and thus greater transmission capacity [18]. Defining $G = ( V , L )$ as a graph where Vis the set of vertices and L is the set of edges, a subgraphinduced by the set W is a k-core iff $\forall \nu \in V : \deg _ { H } ( \nu ) \geq k$ and $H _ { k }$ is the maximum subgraph with this property. To operationalize k-core we employ the generalized p-core measure computed by Pajek. For a network $N = ( V , L , w )$ , where $G ( V , L )$ is a graph and w: $L \to \mathcal { R }$ assigns values to edges, if we define a function $p ( \nu , U )$ , with real values. Then subgraph $H { = } ( C , L | C )$ induced by the set is a p-core at level $t \in \mathbb { R } \operatorname { i f f } ( 1 ) \forall \nu \in V : t \leq p ( \nu , C )$ , and (2) C is the maximal such set. Figure 5 illustrates the concept of a k-core from the undirected commenting network.

![](/api/attachments/XRJ3DR43/fulltext/images/f5f752e5b3af894871bbff736d7b06bc5a906747f7d28d99d0674423c4889fe0.jpg)  
Figure 5. Representative 0, 1, and 2 Cores for Friend Network

Each video is in a conversation with at least k other nodes. As shown in Figure 5, nodes 1 and 2 are in a conversation with each other while 2, 3, 4, and 5 have had pairwise interactions while node 6 has not participated in any conversations. Table 4 describes the above-described network variables collected during the first 15 days after a video has been posted.

## Panel Data After Sixty Days

We collected data about each video and channel at sixty days and subsequently for several periods in time, thirty days apart. We also collected data on video and network characteristics for a five-day window prior to sixty days. Table 5 lists the variables collected after 60 days. We collect the complete list of friends, subscribers, and subscriptions, allowing us to get snapshots of the network structure over time.

## Empirical Methods

## Initiation of Word of Mouth

Our data collection tracks (1) channel history prior to posting a video, (2) each video from its date of posting (i.e., we collect characteristics about channels prior to the video being posted) to the first fifteen days, and (3) subsequent popularity after sixty days, which lends itself to a quasi-treatment propensity score-matching approach as illustrated in Figure 6.

![](/api/attachments/XRJ3DR43/fulltext/images/6cac2db8ef18caf840bcbcee8100b712d6a00c640a015b194894817a9db27645.jpg)  
Figure 6. Propensity Score-Matching Approach Illustrated

Table 4. Description of Variables for First Fifteen Days After a Video Is Posted

<table><tr><td>Used to test hypotheses</td><td>Variable name</td><td>Description of variables</td></tr><tr><td rowspan="2">H2a and H2b</td><td>mean.cc1</td><td>Mean of clustering coefficients of commenting network</td></tr><tr><td>pcore</td><td>Maximal complete subgraph of commenting network</td></tr></table>

Table 5. Description of Variables Collected at Sixty Days and Later

<table><tr><td>Measure</td><td>Variable name</td><td>Description of variables</td></tr><tr><td rowspan="5">Video measures—at and after sixty days</td><td> $NumOfViews_t$ </td><td>Number of times a video is watched at and after sixty days</td></tr><tr><td> $Honored_t$ </td><td>Dummy variable indicating whether a video has been honored or not (= 1 if a video was honored at least once) at time t</td></tr><tr><td> $Responses_t$ </td><td>Number of response videos at time t (Hypotheses 3)</td></tr><tr><td> $Related_t$ </td><td>Related videos as highlighted by YouTube at time t</td></tr><tr><td> $Links_t$ </td><td>Number of prominent external links to a video at time t</td></tr><tr><td rowspan="3">Channel&#x27;s connectedness outside the local network—at and after sixty days</td><td>Log(num. insubs_outjt)</td><td>Total number of incoming subscribers outside the network at time t</td></tr><tr><td>Log(num. outsubs_outjt)</td><td>Total number of outgoing subscriptions outside the local network at time t</td></tr><tr><td>Log(num.frn_outjt)</td><td>Total number of friends of a channel outside the network at time t</td></tr><tr><td rowspan="3">Channel influence measures—at and after sixty days</td><td>nrmdeg.outsubsjt</td><td>Normalized degree centrality of the channel&#x27;s incoming subscribers in the outgoing subscription network at time t</td></tr><tr><td>nrmdeg.frnjt</td><td>Normalized degree centrality of the channel&#x27;s incoming subscribers in the friend network at time t</td></tr><tr><td>nrmdeg.insubsjt</td><td>Normalized degree centrality of the channel&#x27;s incoming subscribers in the incoming subscription network at time t</td></tr></table>

The analysis proceeds in two parts. In the first stage, we examine the likelihood of obtaining comments in the first fifteen days of a video’s posting.<sup>6</sup> The impact of early stage WOM on later video popularity could be the result of a fortuitous position of a video. The susceptibility of the audience and the imitability of a video may be determined by the intrinsic quality, attractiveness, and popularity of previously posted videos. Identification is complicated since it is difficult to find an exogenous shock to a video that does not influence subsequent consumption.

In Table 6 we present the pretreatment channel history. We include a control for the type of content posted by the channel (= 1 if the channel posts music). As proxies for a channel’s ability to be a connector we include the channel’s degree centrality in the three types of networks—the incoming and outgoing subscription networks and the friend network. As factors that are proxies for a channel’s position as a translator we consider (1) the Bonacich power, as a proxy for greater power over information flow in the friend network, which is a network characterized by homophily, and (2) closeness centrality, which denotes a channel’s ability to spread information in a network, in the incoming and outgoing subscription network. We also consider the overall imitability of the content posted by a channel on YouTube, proxied by the number of external links to videos posted by the channel, the response videos posted by the YouTube community and the number of views obtained by the channel.

The problem involved in identification is that susceptibility and influence could both result from previous actions of a channel including its position in the network and characteristics of content posted by the channel. All channels in our sample have posted a video in the first fifteen days. The likelihood that a video is commented on in the first fifteen days is considered an endogenous treatment that results from observed channel characteristics. Conditioning on observables, we can ignore treatment into a selection regime [53]. We therefore examine videos with a similar propensity in triggering WOM, and conduct a matched sample analysis. The matching approach addresses the issues of endogeneity whereby both channel influence (a result of a greater number of connections) and susceptibility toward the content posted by the channel (which arises from the enthusiasm of friends and subscribers) could result from a fortuitous channel position.

The post-treatment outcome is the cumulative number of views at sixty days. The probit model considers factors that impact the incidence of WOM, that is, the likelihood that a video generates a comment in the first fifteen days. In the second stage, the dependent variable is the cumulative demand $\nu _ { i j } ,$ for video i, posted by user j—the total number of views from the aggregate YouTube network after sixty days. The average number of times a video is watched is 16,528 with standard deviation 279,769. Since there is a high dispersion of the popularity of video clips, we used a log-transformed number of views in order to control the skewness. We validated that the log-transformed measure obeys a normal distribution by conducting several tests. While viewers may repeatedly watch a video, since we take logs, any bias caused by repeated viewings will only be a slight downward revision of the estimates. Propensity score-matching estimates the impact of a video’s ability to trigger WOM on subsequent video popularity. The probit model is presented in Table 7 and the results from the matching procedure are presented in Table 8.

Table 6. Pretreatment Characteristics of Channels

<table><tr><td colspan="2">Variables</td><td colspan="2">Videos with comments in the first fifteen days</td><td colspan="2">Videos without comments in the first fifteen days</td></tr><tr><td></td><td></td><td>Mean (S.D.)</td><td>Max.</td><td>Mean (S.D)</td><td>Max.</td></tr><tr><td rowspan="7">Channel characteristics of videos posted by channel</td><td>Channel age</td><td>212.04 (165.036)</td><td>720</td><td>164.041 (157.09)</td><td>734</td></tr><tr><td>Number of honors received</td><td>0.393 (0.020)</td><td>11</td><td>0.25 (0.010)</td><td>9</td></tr><tr><td>Number of videos posted</td><td>53.065(86.46)</td><td>494</td><td>51.794 (90.4)</td><td>428</td></tr><tr><td>Number of channel views</td><td>19,702.55(123,435.7)</td><td>1,886,546</td><td>14,035.37(11,161.5)</td><td>1,432,781</td></tr><tr><td>Number of ratings on videos posted by channel</td><td>56.240 (45.563)</td><td>66,648</td><td>36.997 (11.621)</td><td>1,655</td></tr><tr><td>Average rating of video</td><td>3.968 (0.937)</td><td>5</td><td>3.413 (1.713)</td><td>5</td></tr><tr><td>Category of video (music)</td><td>0.640 (0.579)</td><td>1</td><td>0.784 (0.639)</td><td>1</td></tr><tr><td rowspan="3">Channel imitability within YouTube</td><td>Cumulative number of external links</td><td>4.152 (1.61)</td><td>5</td><td>3.7540 (1.86)</td><td>5</td></tr><tr><td>Number of response videos posted by other channels</td><td>0.133 (0.498)</td><td>255</td><td>0.540 (0.228)</td><td>1078</td></tr><tr><td>Number of videos posted by channel favored at least once</td><td>73.238 (103.516)</td><td>400</td><td>50.509 (89.598)</td><td>60</td></tr><tr><td rowspan="3">Channel influence as a connector</td><td>Number of subscribers</td><td>388.173 (214.724)</td><td>28302</td><td>232.16 (156.218)</td><td>27631</td></tr><tr><td>Number of friends</td><td>272.233 (508.87)</td><td>5250</td><td>143.016 (354.079)</td><td>2000</td></tr><tr><td>Number of outgoing subscriptions</td><td>68.713 (21.489)</td><td>282</td><td>117.542 (31.151)</td><td>2000</td></tr><tr><td rowspan="3">Channel&#x27;s influence as a translator</td><td>Closeness centrality in Incoming subscription network</td><td>0.079 (0.006)</td><td>0.124</td><td>0.078 (0.006)</td><td>0.090</td></tr><tr><td>Closeness centrality in outgoing subscription network</td><td>0.055 (0.077)</td><td>0.242</td><td>0.047 (0.072)</td><td>0.242</td></tr><tr><td>Bonacich power in friend network</td><td>-8.87 (17.37)</td><td>38.857</td><td>-6.95 (13.151)</td><td>38.857</td></tr></table>

<table><tr><td></td><td>Variable</td><td>Estimates</td></tr><tr><td rowspan="5">Channel characteristics</td><td>Intercept</td><td>-1.547 (0.289)***</td></tr><tr><td>Channel age</td><td>-0.001 (0.000)</td></tr><tr><td>Number of channel views</td><td>3.27e-07(6.01e-08)**</td></tr><tr><td>Number of honors received by channel</td><td>0.031 (0.093)</td></tr><tr><td>Number of videos posted by channel</td><td>-0.006 (0.000)*</td></tr><tr><td rowspan="3">Video characteristics</td><td>Log(Cumulative number of ratings)</td><td>-0.002 (0.000)***</td></tr><tr><td>Average rating</td><td>0.156 (0.017)***</td></tr><tr><td>Category = Music</td><td>-0.027 (0.014)**</td></tr><tr><td rowspan="3">Channel&#x27;s influence as a connector</td><td>Number of subscribers</td><td>-0.003 (0.000)**</td></tr><tr><td>Number of outgoing subscriptions</td><td>0.002 (0.000)***</td></tr><tr><td>Number of friends</td><td>0.003 (0.000)***</td></tr><tr><td rowspan="3">Imitability of prior content posted by channel</td><td>Number of links</td><td>0.046 (0.013)***</td></tr><tr><td>Number of response videos posted by other channels</td><td>0.153 (0.021)***</td></tr><tr><td>Number of videos posted by channel favored at least once</td><td>0.001 (0.000)***</td></tr><tr><td rowspan="3">Channel&#x27;s connectedness as a translator</td><td>Bonacich power in friend network</td><td>0.001 (0.001)*</td></tr><tr><td>Closeness centrality in incoming subscription network</td><td>0.472 (0.253)**</td></tr><tr><td>Closeness centrality in outgoing subscription network</td><td>0.270 (0.159)*</td></tr></table>

Table 7. Probit Model of Likelihood of Video Receiving Comments

Table 8. Propensity Score-Matching Results (untreated = 2,586; treated = 1,190)

<table><tr><td>Variable</td><td>Sample</td><td>Treated</td><td>Controls</td><td>Difference (S.E.)</td><td>T-statistic</td></tr><tr><td rowspan="2">Log(number of views at sixty days)</td><td>Unmatched</td><td>7.457</td><td>6.777</td><td>0.679 (0.061)</td><td>11.09</td></tr><tr><td>Average treatment effect</td><td>7.461</td><td>7.156</td><td>0.305 (0.063)</td><td>4.71</td></tr></table>

## Second Stage: Estimating the Magnitude and Persistence of WOM

Once cascades are initiated, there could be bandwagon effects depending on aggregate popularity. The pattern of discovery of globally popular videos could be significantly different from that of searching locally for a video. For example, the impact of social influence could be disproportionately greater for the most popular and the least popular videos, as opposed to the ones in the middle. Alternatively, a strong early word-ofmouth effect could result in a burst of initial popularity, which could quickly taper off when more information about the video becomes available. In other words, both the magnitude of popularity and the growth of popularity could be affected by the initial buzz, which is in turn triggered by the social network structure. Therefore, we conduct a finite mixture model to capture heterogeneity in the impact and persistence of cascades of WOM (and not just the incidence of WOM alone).

Denoting $\nu _ { i j t }$ as the log-number of views of video i posted by channel $j ,$ we examine the impact of the cascade sizes of WOM conversations in the first fifteen days, including as an explanatory variable the likelihood that a video received at least one comment in the first fifteen days. For each period, we include detailed controls $Y _ { i j t }$ for the number of external links, response videos, related videos showcased by YouTube, and whether a video received any honors. We include $X _ { i j t } ,$ the lagged values of the channel’s connectedness in the three different networks. As proxies for susceptibility we consider measures of clustering and k-core in the network of comments $( m e a n . c c 1 _ { i j } )$ . Since views for videos could be driven by past views, we model video views as a function of fixed channel characteristics, a channel’s network position with respect to its social ties at the previous period (to avoid simultaneity), the estimated value of comments from the first stage, and other fixed video characteristics. Since time-varying video characteristics could be a result of past or present shocks to views, we adopt a generalized method of moments (GMM) approach to account for dynamic effects. The lagged differences of explanatory variables are used as instruments [4]. Since we consider the difference between the lagged views, we are not including the video views in the treatment period in our explanatory variable.

$$
\begin{array}{l} v _ {i j t} = \alpha_ {i j t} + \rho e _ {i j} + \eta c _ {i j} + \gamma W _ {i j t} + \beta X _ {j t - 1} \\ \quad + \varphi (v _ {i j t - 1} - v _ {i j t - 2}) \\ \quad + \varepsilon_ {i j t}, \text { for } i = 1, \ldots , n; j = 1, \ldots , J \end{array}\tag{4}
$$

$$
W _ {i j t} = \left[ \begin{array}{c c c} L i n k s _ {i j t} & R e s p o n s e s _ {i j t - 1} - R e s p o n s e s _ {i j t - 2} & R e l a t e d _ {i j t} h o n o r s _ {i j t} \end{array} \right]\tag{5}
$$

$$
X _ {j t - 1} = \left[ n r m \deg . f r n _ {j t - 1} \quad n r m \deg . i n s u b s _ {j t - 1} \quad n r m \deg o u t s u b s _ {j t - 1} \right].\tag{6}
$$

In particular, we need to consider whether videos with epidemic-spreading potential are markedly different from those that cannot engage viewers, which implies the existence of two subpopulations of videos. The empirical approach needs to consider whether there are latent classes of videos that differ in the unobserved propagation or epidemic-spreading potential. We addressed this issue by employing an unbalanced panel finite mixture model (FMM) where each observation is assumed to be from a population of a discrete (finite) set of latent classes [34]. Without loss of generality, we drop the subscripts $i , j ,$ and t for each video. Using X as the set of explanatory variables and v as the dependent variable (the number of views at time $t ) , \theta _ { k } ,$ the parameter vector of the kth component, we can write the density of an M component finite mixture model (e.g. [27]) as:

$$
f (v | \mathrm{X}; z; \theta_ {1}, \theta_ {2},.. \theta_ {M}; \pi_ {1}, \pi_ {2}.. \pi_ {M}) = \sum_ {k = 1} ^ {M} \pi_ {k} (\mathrm{X}) f _ {k} (v | \mathrm{X}; \theta_ {k})\tag{7}
$$

where $\pi _ { k }$ is the mixture proportion $( \textstyle \sum _ { k = 1 } ^ { M } \pi _ { k } = 1 ; \pi _ { k } \ge 0 )$ and $f _ { k }$ the density of the kth mixture component. (Note that we omit the subscript i on each observation without loss of generality.) Since the true component membership is unknown, the mixture density function is $f ( \nu | X , \pi , \theta )$ , where observations of component k follow a generalized linear model (GLM). The maximum likelihood function is:

$$
\max _ {\pi , \theta} \ln L = \sum_ {l = 1} ^ {N} \log \left(\sum_ {k = 1} ^ {M} \pi_ {k} f _ {k} (v | \theta_ {k})\right).\tag{8}
$$

The conditional mean can be written as:

$$
E (v | X) = \sum_ {j = 1} ^ {M} \pi_ {j} \lambda_ {j}, \text { where } \lambda_ {j} = E _ {j} (v | X)\tag{9}
$$

Prior probability that an observation $\nu _ { i }$ belongs to component k isπ<sub>k</sub> for k = 1, 2, . . ., M.

Posterior probability that observation $\nu _ { i }$ belongs to component k is:

$$
\frac {\pi_ {k} f _ {k} (v | X , \theta_ {k})}{\sum_ {j = 1} ^ {M} \pi_ {j} f _ {j} (v | X , \theta_ {j})}.\tag{10}
$$

We employ a finite mixture of GLMs, where the individual parameters are assumed to be from a finite mixture of multivariate normal distributions [47]. We use a maximum likelihood estimation approach using Stata [26] to start with a twocomponent specification and then examine three- and four-component specifications. For comparison, we estimated the model with a GLM with the same set of dependent variable and covariates and found that the coefficients of number of early comments and the lagged difference in views are significant.

One issue with estimating finite mixture models using panel data is the problem of pooling across observations. We address this issue using cluster robust standard errors. We assume that the mixture probabilities are the same across the panel (i.e., there is no transition across latent classes over time), since very few videos reach the epidemic threshold required to become viral hits and once they reach it, they still continue to attract visibility. We examined alternate specification using other types of distributions (Poisson, negative binomial, etc.) and found that using a mixture of normal distributions fits the data best. The results from the FMM specification are shown below in Table 9 and the distribution of posterior probabilities is shown in Table 10. The posterior is the probability that an observation belongs to a mixture class, conditional on the prior. Component 1 (and components 1 and 3 in the threecomponent case) is characterized by a higher coefficient of the diffusion rate while component 2 is characterized by a higher coefficient of the number of comments in the first fifteen days. The posterior probability analysis of membership in the latent classes is presented in an appendix available from the authors.

## Simultaneous Estimation with Latent Instrumental Variable

Given that not everyone on YouTube who views a video is likely to comment on a video, we need to address endogeneity in comment generation, that is, in the incidence of WOM. The propensity score-matching model addresses selection conditional on observables. However, there could be unobservable factors impacting endogeneity. The challenge is to find instruments for early WOM that do not influence subsequent cascading effects. We therefore build on latent instrumental variable (IV) models to implement a latent IV model. The two stages—the first-stage probit model of incidence of WOM, and the second-stage model of impact of cascades on subsequent popularity—are simultaneously estimated, with a latent instrumental variable used for the first-stage estimation.

Latent instrumental variable methods have been used in the literature on online social networks when it is difficult to find observables (e.g. [45, 54]). We build on Lewbel [42], who identifies structural parameters in regression models with endogenous or mismeasured regressors in the absence of traditional identifying information, such as external instruments or repeated measurements. Identification hinges upon finding regressors that are uncorrelated with the product of heteroskedastic errors [6, 7]. Baum and Schaffer [6] provide a method to construct instruments that would satisfy the above identification conditions. Their method is similar to the Arellano and Bond [4] approach using dynamic panel data estimators. Baum and Schaffer [6] suggest that their approach is suitable when no external instruments are available, or, to supplement external instruments to improve the efficiency of the IV estimator. For the first stage, that is, a channel’s likelihood of receiving a comment in the first fifteen days, the latent instrumental variable estimation uses the channel’s Page Rank (computed before the video was posted) in the overall

Table 9. Estimates from Panel Finite Mixture Model of Video Views After Sixty Days

<table><tr><td rowspan="2"></td><td colspan="5">Dependent variable: Views after sixty days</td></tr><tr><td colspan="2">Two components</td><td colspan="3">Three components</td></tr><tr><td>(Intercept)</td><td>3.343 (0.091)***</td><td>3.434 (0.570)***</td><td>3.478 (0.128)***</td><td>5.822 (0.548)***</td><td>2.712 (0.222)***</td></tr><tr><td>k-core</td><td>0.011 (0.001)***</td><td>0.057 (0.026)**</td><td>0.013 (0.001)***</td><td>0.136 (0.015)***</td><td>0.007 (0.001)***</td></tr><tr><td>Clustering coefficient in commenting network</td><td>0.161 (0.014) ***</td><td>0.307 (0.09)***</td><td>0.123 (0.019)***</td><td>-0.119 (0.0718)*</td><td>0.264 (0.029)***</td></tr><tr><td>Likelihood of getting comments</td><td>0.067 (0.03)**</td><td>0.267 (0.097)**</td><td>0.011 (0.050)</td><td>-0.123 (0.181)</td><td>0.357 (0.095)***</td></tr><tr><td>V(t - 1) - V(t - 2) (Instrument)</td><td>3.52 (0.117)***</td><td>0.215 (0.107)**</td><td>3.189 (0.167)***</td><td>0.231 (0.036)***</td><td>5.487 (0.296)***</td></tr><tr><td>Number of links t-1</td><td>0.280 (0.035)***</td><td>0.773 (0.115)***</td><td>0.293 (0.013)***</td><td>0.110 (0.043)***</td><td>0.297 (0.032)***</td></tr><tr><td>Number of honors t-1</td><td>0.008 (0.029)</td><td>0.902 (0.333)***</td><td>0.042 (0.022)**</td><td>1.082 (0.133)*</td><td>0.878 (0.436)**</td></tr><tr><td>Responses t-1</td><td>0.007 (0.000)***</td><td>0.082 (0.033)***</td><td>0.007 (0.000)***</td><td>0.668 (0.035)***</td><td>0.091 (0.025)***</td></tr><tr><td>Related videos t-1</td><td>-2.66e-08 (6.20e-08)</td><td>-4.37e-07 (1.01e-07)***</td><td>-5.89e-09 (7.64e-08)</td><td>-0.0000643 (3.90e-06)***</td><td>-2.51e-07 (3.49e-08)***</td></tr><tr><td>nrmdeg.frn j(t -1)</td><td>0.003 (0.006)</td><td>-0.417 (0.421)</td><td>0.021 (0.005)***</td><td>-0.045 (0.008)***</td><td>-0.038 (0.015)***</td></tr><tr><td>nrmdeg.insubs j(t -1)</td><td>0.323 (0.070)***</td><td>1.410 (0.670)**</td><td>0.188 (0.088)**</td><td>3.502 (0.172)***</td><td>0.233 (0.129)*</td></tr><tr><td>nrmdeg.outsubs j(t -1)</td><td>-0.0467 (0.033)</td><td>-0.474 (0.15)***</td><td>0.0372 (0.061)</td><td>-1.896 (0.132)***</td><td>-0.140 (0.162)</td></tr><tr><td>π(Mixture Proportion)</td><td>0.899 (0.025)</td><td>0.101 (0.025)</td><td>0.552 (0.040)</td><td>0.099 (0.026)</td><td>0.347 (0.038)</td></tr><tr><td>Akaike information criterion</td><td>11,312.019</td><td></td><td>10,974.847</td><td></td><td></td></tr><tr><td>Bayesian information criterionIC</td><td>11,480.360</td><td></td><td>11,230.475</td><td></td><td></td></tr><tr><td>Normalized entropy</td><td>0.0010</td><td></td><td>0.0004</td><td></td><td></td></tr></table>

Table 10. Posterior Probability Distribution

<table><tr><td colspan="2">Two-component model</td><td colspan="3">Three-component model</td></tr><tr><td>Component 1</td><td>Component 2</td><td>Component 1</td><td>Component 2</td><td>Component 3</td></tr><tr><td>0.940</td><td>0.060</td><td>0.684</td><td>0.092</td><td>0.224</td></tr><tr><td>0.180</td><td>0.820</td><td>0.237</td><td>0.654</td><td>0.110</td></tr><tr><td>—</td><td>—</td><td>0.180</td><td>0.038</td><td>0.782</td></tr></table>

Table 11. Simultaneous Estimation with Latent Instrumental Variable

<table><tr><td>Variable</td><td>Second-stage estimates Dependent variable: Views after sixty days</td></tr><tr><td>(Intercept)</td><td>3.48 (0.16)***</td></tr><tr><td>Likelihood of video receiving comments</td><td>3.87 (0.63)***</td></tr><tr><td> $\ln(V(t - 1) - V(t - 2))$ </td><td>0.57 (0.02)***</td></tr><tr><td>Number of links  $_{t-1}$ </td><td>0.01 (0.00)**</td></tr><tr><td>Number of honors  $_{t-1}$ </td><td>0.02 (0.15)</td></tr><tr><td>Number of responses  $_{t-1}$ </td><td>0.00 (0.00)***</td></tr><tr><td>Number of related videos  $_{t-1}$ </td><td>-3.51e-07 (1.92e-07)*</td></tr><tr><td>k-core in comments in the first fifteen days</td><td>0.39 (0.16) ***</td></tr><tr><td>Clustering coefficient in commenting network in the first fifteen days</td><td>0.01 (0.00)***</td></tr></table>

\*\*\*, \*\*, and \* indicate significance at the 0.001, 0.05, 0.1 levels, respectively.  
Note: The first-stage estimates have been omitted for brevity.

YouTube network as an instrument, and in addition computes a generated instrument from the mean-centered residuals from the first stage (e.g. [7]). Following Baum and Schaffer [6], we considered several tests to examine whether the generated instruments can achieve identification. We consider the influence from a channel’s position as a connector and translator in the first stage estimation. For the second stage estimation, we consider several controls similar to those in Table 9 in the finite mixture model. The estimation results are presented in Table 11.

## Results and Discussion

## Discussion

The results from the first stage show that influence, imitability, and the susceptibility of network ties significantly impact the aggregate volume of WOM conversations. The channel influence (measured in terms of network position as a connector and position as a translator) is significantly and positively associated with a greater volume of commenting in the first fifteen days, confirming H1a and H1b. We find that the channel’s position as a connector in the friend networks matters more to the likelihood of obtaining comments, rather than its position as a connector in the subscriber networks. This could likely be due to the shared affiliation and homophily characterizing friend networks on YouTube, which makes the channel’s audience more likely to engage in WOM. We find that WOM is triggered by channel influence. However, what matters to the spread of WOM is engagement with a video or susceptibility to a video rather than connectedness of a node. A channel that is connected to several other channels is in a position to transmit greater amounts of information. However, it is the susceptibility of network ties leading to their willingness to share experiences that raises the visibility of video. The sequence of early WOM conversations is propagated beyond the local network and impacts the aggregate network depending on the existence of a susceptible cluster of nodes that engages in conversations. The willingness of susceptible ties creates a network neighborhood effect that spurs other channels with direct ties to the focal channel to engage with a video and stimulate further discussion. Figure 7 shows the impact of clustering of WOM conversations on the number of comments in the first fifteen days.

![](/api/attachments/XRJ3DR43/fulltext/images/811f8b21ec7c0750856828b9e6ed3247a2ce950f242ac4e2dd6387fdd8d5dd89.jpg)  
Figure 7. Commenting Activity and Clustering Coefficient of Commenting

In examining the patterns of interaction, the k-core as well as clustering coefficient in comment networks have a significant positive impact on popularity on a video, confirming H2a and H2b. We notice that the k-core has a greater impact on subsequent popularity. This is probably since a connected subgraph of a cohesive subset is likely to have greater redundancy [57] leading to degeneracy in the structure of interaction. If networks of users who subscribe to each other are characterized by similarity in tastes, the intensity of conversations between connected channels does not necessarily spread beyond the local network, thereby limiting the global propagation of WOM. In contrast, the k-core patterns could indicate the influence of a small number of nodes to trigger a greater volume of visibility and buzz, which provides a greater opinion-making role to WOM conversations generated by such ties.

We find that imitability has a significant and positive impact on the number of comments, confirming H3. Social media platforms encourage propagation of memes and user engagement in the form of creation and remixing of popular content. In fact, our work suggests two different paths for popularity of digital content-susceptibility that occurs through conversations and factors triggers imitation, replication or indeed, parody that occurs through mimesis [59], suggesting different types of user engagement.

The propensity score estimation indicates that for videos that have reached an epidemic threshold, each comment for a video in the first fifteen days could result in about 1,000 views after sixty days. Initial WOM conversations generated early in the life of a video have a persistent impact on subsequent popularity. Viewers face relatively simple choices of whether to watch a video or not, and whether to comment on a video. This results in a cascading effect whereby subsequent viewers are likely to watch a video depending on whether prior viewers have watched it.

The latent class analysis shows a distinct difference between videos for which early commenting is important versus those driven by momentum from later diffusion. We find that the impact of imitability and the momentum from video views is greater for the latter while the impact of WOM from early stages of the life of a video matters more for the former. This could indicate different ways by which videos acquire visibility on YouTube—that is, a class of videos where views are driven by momentum from prior views, whereas for another class, there is a signaling impact of the early WOM where susceptible actors play an important role in building awareness and buzz about a video. Since we examine the total volume of commenting activity and the clustering coefficients and k-core measures of WOM interactions (and not the underlying sentiment), it should be emphasized that any communication, whether positive or negative, is important to triggering WOM. We found that the three-component mixture model outperforms the two-component model on both the normalized entropy and the Bayesian information criterion. Significantly, we also find that the mixture model outperforms a multilevel model parameterized for individual channel- and video-level heterogeneity (in multilevel models the source of the heterogeneity is assumed to be known). This could be a result of the susceptibility and epidemic threshold needed to trigger WOM. Exogenous changes to a video’s visibility in the form of honored status or response videos posted by other channels have a significant impact once videos reached the epidemic potential. Figure 8, based on the estimated posterior probabilities from the finite mixture model in Tables 8 and 9, shows that aggregate diffusion patterns differ depending on the type of video.

![](/api/attachments/XRJ3DR43/fulltext/images/977943ba5b117510bdef5f717b953649519521222b7e180529ae30838e57909a.jpg)

![](/api/attachments/XRJ3DR43/fulltext/images/056624d5e921748afe3b353ddb0d0d010e8b781996a36de75eef68157fb79dca.jpg)  
Figure 8. Diffusion Curves for Videos Driven by Momentum (Component 1) and Cascading in Comments (Component 2)

![](/api/attachments/XRJ3DR43/fulltext/images/dd7d9e76b95aacc51a7ad003bc2932c044664f9c389e86a41845e966f1af4a76.jpg)  
Figure 9. Impact of Commenting Activity on Persistence of Word of Mouth

The probit model allows us to identify factors that impact the incidence of WOM from the imitability of prior content posted by the channel and influence of a channel. The estimates from Table 7 indicate that the history of a channel in increasing imitability of content, such as posting videos favorited by others and posting videos that have a high number of response videos, significantly increases the likelihood that a video gets comments. The network measures of a channel indicating that the channel functions as a connector, the closeness centrality in the incoming and outgoing subscription network, and the Bonacich power in the friend network are significantly and positively associated with the ability to trigger comments from within the local network. A video that has the ability to generate comments from the local network has a 30 percent greater likelihood of obtaining greater visibility and becoming viral. The predicted number of views of a video that is a global hit is several orders of magnitude larger than videos that do not have epidemic-spreading potential. This is consistent with the literature on informational cascades [29] that has found bandwagon effects in the impact of the online user reviews. Another possibility is that commenting activity above an epidemic threshold could enhance the likelihood of user-generated links to the video, increasing the visibility and virality of the video. Figure 9 shows the impact of commenting activity on persistence of WOM. The simultaneous estimation with latent instrumental variable finds that cascades of conversation, measured through clustering and through the number of conversations, have a highly significant impact on subsequent video popularity.

## Contributions to Literature

Most of the prior work on diffusion and cascades identifies opinion leaders or influentials. However, as Watts and Dodds [67] posit, large cascades of influence are not driven by influentials but by a critical mass of easily influenced individuals. Aral and Walker [3] distinguish between influence and susceptibility in dyadic interactions. Our research adds to this literature both by (1) identifying the incidence of WOM, and (2) quantifying the impact of networked interactions of susceptible actors (through commenting) that leads to propagation of WOM cascades. By analyzing the cascade created by the interactions between networked actors through exploring comments on videos, we can understand how informational cues inherent in WOM lead to durable popularity of a video.

Beyond the context of YouTube, our results have broad implications for the literature on peer effects and the theories of contagion and opinion leadership. Our work contributes by quantifying the impact of network structure and connectedness of nodes on WOM, even when the sequence of peer interactions or the mechanism of influence is not directly observable. Susceptibility could be triggered by providing a setting for shared experience, and the resultant “friendship ripple” effects can propagate beyond the local network depending on the epidemic potential of the product. Whether a new product can be designed to be viral depends on the potential to engage the mass of early adopters, raising their susceptibility, and providing a critical role to the preexisting social ties in triggering WOM conversations. Since influential users are likely to be less susceptible [3], our results suggest that cascading effects are more likely when highly influential users are embedded in a network of susceptible ties that are likely to interact with each other.

Since we distinguish between nodes that are influential in terms of connectedness in friend/subscriber ties and nodes with susceptible social ties, our study also contributes to the modeling of social multiplier effects and other types of social influence (e.g. [2, 36]). Examining the patterns of WOM interactions provides a way to quantify the influence propagation path as well as a means to detect videos that could be potential hits. Our method of measuring patterns of user interaction parallels methods of cascade enumeration in recommendation networks [41]. An understanding of network topology and patterns of social interactions may prove valuable in developing recommendation and collaborative filtering systems. Our approach can be used to monitor potential outbreaks of trending topics in social media as well as a method to monitor the likely adopters or influentials for the emergence of trends and sentiment.

## Implications for Practice

Social commerce has changed the ways that companies do business. The problem, however, is that intertwining marketing promotions with participatory interaction is still a challenge for companies. Our results can provide guidelines for marketing strategy using social media platforms. For content creators on YouTube, building a large base of network ties is important only when the ties are susceptible to content posted by the channel. In practice, it means channels that are active content providers should actively interact with their friend and subscriber base, enhancing the susceptibility of the audience. For channels on YouTube, there appears to be a significant difference in their ability to engage with susceptible audiences early in the life of a video. The analysis of latent classes also points to different methods of manufacturing a viral hit on YouTube, in that there is a trade-off between increasing susceptibility of network ties and increasing overall visibility of the video by pursuing alternate promotional strategies.

Aral and Walker [3] distinguish between active and passive broadcast viral product features, where passive broadcast viral product features are globally more effective while active broadcast features have more marginal effectiveness. In the YouTube context, commenting activity is akin to active referral broadcasting of preferences. Our results suggest that advertisers and marketers seeking to use YouTube for promotional efforts should provide incentives for susceptible audiences to actively broadcast their preferences as well as a platform for network ties to talk about the featured content and interact with each other. Recent attempts by YouTube to adopt a channel-centric user experience and promote customer engagement with channels [56] point to the importance of susceptibility and receptivity of network ties to the success of content creation and monetization on YouTube. Beyond the context of YouTube, our research can provide guidelines for personalization and content discovery strategies by illuminating the manner in which networks of influence and susceptibility disseminate awareness and information.

## Limitations

This study has a few limitations. Some channels could be influential in recommending content without engaging in conversations with other channels. With the convergence of social media and digital-sharing platforms, we cannot quantify the impact of conversations outside YouTube. There could also be decaying impacts from WOM. Finally, we cannot distinguish between whether the relationship between WOM and observed popularity of content is a result of observational learning or other mechanisms whereby influence and susceptibility are transmitted.

## Conclusions and Future Research

While prior research has highlighted the importance of opinion leaders and influencers, our study suggests that initial WOM effects have differing impacts on the process by which a video reaches epidemic thresholds, with differing impacts on aggregate popularity. The act of engaging in conversations itself could contribute to a durable popularity surge of content. It is not so much positive sentiment as susceptibility that seems to be important, suggesting that the success of social media initiatives depend on maintaining a sustained conversation with likely adopters, rather than providing incentives for seeding contagion alone. Future work can incorporate data-mining methods to detect bursts of activity wherein products or ideas suddenly gain relevance. Other work could quantify peer effects arising from engagement in tandem with product recommendations. Randomized experiments and large graph sampling methods may provide greater insights into these issues.

Acknowledgments: The authors thank Sinan Aral, Ravi Bapna, Eyal Carmi, Paul Damien, Chris Dellarocas, David Godes, David Krackhardt, Ramayya Krishnan, Yingda Lu, Gal Oestreicher-Singer, Sarah Rice, Param Vir Singh, Arun Sundararajan, Rahul Telang, and Andrew B. Whinston for their comments. They also thank seminar participants at Heinz College at Carnegie Mellon University and University of Connecticut for helpful comments. They thank participants at the Workshop in Information Systems Economics (WISE), the Winter Conference on Business Intelligence, Informs Conference on Information Systems and Technology (CIST), and the Symposium on Statistical Challenges in eCommerce Research (SCECR) for feedback on earlier versions of this paper.

## NOTES

1. Users are referred to as channels on YouTube. We relied on reports from the YouTube blog and TubeMogul, an analytics firm that tracks YouTube. We examine the action of YouTube users posting response videos.

2. YouTube highlights videos by featuring the most watched videos as well as promoting videos. However, such mechanisms constitute external rather than internal WOM.

3. Data API supports a number of client libraries that abstract the API into a languagespecific object model such as Java, .NET, PHP, and Python (http://code.google.com/apis/ youtube/overview.html).

4. Subsequent to our data collection, YouTube changed its API to restrict access to the top 200 comments so that it is no longer possible to obtain each comment posted on a video, which makes it almost impossible to study WOM interactions.

5. The k-core provides an alternative to using data-mining methods to detect influential commentators or using sentiment analysis to infer positive or negative sentiment.

6. For robustness we considered three different treatment regimes and found that a single treatment regime had the best explanatory power.

## REFERENCES

1. Adar, E.; Zhang, L.; Adamic, L.A.; and Lukose, R. Implicit structure and the dynamics of blogspace. In Workshop on the Weblogging Ecosystem, Thirteenth International World Wide Web Conference, 2004.

2. Aral, S., and Walker, D. Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Science, 57, 9 (2011), 1623– 1639.

3. Aral, S., and Walker, D. Identifying influential and susceptible members of social networks. Science, 337, 6092 (2012), 337–341.

4. Arellano, M., and Bond, S. Some tests of specification for panel data: Monte Carlo evidence and an application to employment equations. Review of Economic Studies, 58 (1991), 277–297.

5. Batagelj, V., and Mrvar, A. Analysis of large networks with Pajek. In Twenty-Sixth Sunbelt Conference, 2006. Vancouver, BC.

6. Baum, C.F., and Schaffer, M. E. IVREG2H: Stata module to perform instrumental variables estimation using heteroskedasticity-based instruments. Statistical Software Components S457555, (2012). Boston College Department of Economics, revised April 2, 2015.

7. Baum, B.F. Implementing new econometric tools in Stata. In Mexican Stata Users’ Group Meetings, 2013–09. Stata Users Group. Mexico City: CIDE.

8. Bearden, W.O.; Netemeyer, R.G.; and Teel, J.E. Measurement of consumer susceptibility to interpersonal influence. Journal of Consumer Research, 15 (1989), 473−481.

9. Benevenuto, F.; Rodrigues, T.; Almeida, V.; Almeida, J.; and Ross, K. Video interactions in online video social networks. ACM Transactions on Multimedia Computing, Communications, and Applications (TOMCCAP), 5, 4 (2009), 1–25.

10. Berger, J., and Heath, C. Where consumers diverge from others: Identity signaling and product domains. Journal of Consumer Research, 34, 2 (2007), 121–134.

11. Berger, J., and R. Iyengar. Communication channels and word of mouth: How the medium shapes the message. Journal of Consumer Research, 40, 3 (2012), 567–579.

12. Berger, J., and Schwartz, E.M. What drives immediate and ongoing word of mouth? Journal of Marketing Research, 48 (October 2011), 869–880.

13. Bikhchandani, S.; Hirshleifer, D.; and Welch, I. A theory of fads, fashion, custom and cultural change as informational cascades. Journal of Political Economy, 100 (1992), 992– 1026.

14. Borgatti, S.P., and Everett, M.G. A graph-theoretic framework for classifying centrality measures. Social Networks, 28, 4 (2006), 466–484.

15. Brown, J.J., and Reingen, P.H. Social ties and word-of-mouth referral behavior. Journal of Consumer Research, 14, 3 (1987), 350–362.

16. Budak, C.; Agarwal, D.; El Abbadi, A. Where the blogs tip: Connectors, mavens, salesmen and translators of the blogosphere. In Proceedings of the First Workshop on Social Media Analytics, Washington, DC: ACM, 2010, pp. 106–114.

17. Burt, R.S. Social contagion and innovation: Cohesion versus structural equivalence. American Journal of Sociology, 92, 6 (1987), 1287–1335.

18. Carmi, S.; Havlin, S.; Kirkpatrick, S.; Shavitt, Y.; and Shir, E. A model of Internet topology using k-shell decomposition. In Proceedings of the National Academy of Sciences, 2007, pp. 1150–1154.

19. Cha, M., Kwak, H., Rodriguez, P., Ahn, Y., and Moon, S. I tube, YouTube, everybody tubes: Analyzing the world’s largest user generated content video system. In Proceedings of the ACM SIGCOMM Internet Measurement Conference, Washington, DC: ACM, 2007, pp. 1– 14.

20. Chakrabarti D.; Wang, Y.; Wang, C.; Leskovec, J.; and Faloutsos, C. Epidemic thresholds in real networks. ACM Transactions on Information Systems Security, 10, 4 (January 2008), 1:1–1:26.

21. Chen, J.; Xu, H.; and Whinston, A.B. Moderated online communities and quality of user-generated content. Journal of Management Information Systems, 28, 2 (2011), 237– 268.

22. Chingtagunta, P.; Gopinath, S.; and Venkatraman, S. The effects of online user reviews on movie box office performance: Accounting for sequential rollout and aggregation across local markets. Marketing Science, 29, 5 (2010), 944–957.

23. Clauset, A. Finding local community structure in networks. Physical Review E, 72, 2 (2007), 026132–026137.

24. Crane, R., and Sornette, D. Robust dynamic classes revealed by measuring the response function of a social system. Proceedings of the National Academy of Sciences, 105, 41, (2008), 15649–15653.

25. Dawkins, R. The Selfish Gene. Oxford: Oxford University Press, 1976.

26. Deb, P. Finite mixture models. Summer North American Stata Users’ Group Meetings, 2008.

27. Deb, P., and Trivedi, P.K. Demand for medical care by the elderly: A finite mixture approach. Journal of Applied Econometrics, 12 (1997), 313–336.

28. Duan, W.; Gu, B.; and Whinston, A.B. Do online reviews matter? An empirical investigation of panel data. Decision Support Systems, 45, 4 (2008), 1007–1016.

29. Duan, W.; Gu, B.; and Whinston, A.B. Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quarterly, 33, 1 (2009), 23–48.

30. Girvan, M., and Newman, M.E.J. Community structure in social and biological networks. Proceedings of the National Academy of Sciences, 99, 12 (June 2002), 7821–7826.

31. Gladwell, M. The Tipping Point: How Little Things Can Make a Big Difference. Boston, MA: Little Brown, 2000.

32. Godes, D., and Mayzlin, D. Using on-line conversations to study word-of-mouth communication. Marketing Science, 23, 4 (2004), 545–560.

33. Goldenberg, J.; Oestreicher-Singer, G.; and Reichman, S. The quest for content: The integration of product networks and social networks in online content exploration. Journal of Marketing Research, 49, 4 (2012), 452–468.

34. Heckman, J.J., and Singer, B. Econometric duration analysis. Journal of Econometrics, 24 (1984), 63–132.

Huang, L.; Tan, C.-H.; Ke W.; and Wei. K.-K. Comprehension and assessment of product reviews: A review-product congruity proposition. Journal of Management Information Systems, 30, 3 (Winter 2013–14), 311–343.

35. Katona, Z.; Zubschek, P.; and Sarvary, M. Network effects and personal influences: The diffusion of an online social network. Journal of Marketing Research, 48 (2011), 425– 443.

36. Kempe, D.; Kleinberg, J.; and Tardos, E. Maximizing the spread of influence through a social network. In Proceedings of Ninth ACM SIGKDD International Conference on Knowledge Discovery and Data Mining, Washington, DC: ACM, 2003.

37. Knobel, M., and Lankshear, C. Online memes, affinities and cultural production. In C. Lankshear, M. Knobel, C. Bigum, and M. Peters (eds.), A New Literacies Sampler. New York: Peter Lang, 2007, pp. 199–227.

38. Krackhardt, D. Structural leverage in marketing. In D. Iacobucci (ed.), Networks in Marketing. Thousand Oaks, CA: Sage, 1996, pp. 50–59.

Kuan, K.K.Y.; Zhong, Y.; and Chau, P.Y.K. Informational and normative social influence in group-buying: Evidence from self-reported and EEG data. Journal of Management Information Systems, 30, 4 (Spring 2014), 151–178.

39. Leskovec, J.; Adamic, L.; and Huberman, B. The dynamics of viral marketing. ACM Transactions on the Web, 1, 1 (2007), article 5.

40. Lewbel, A. Using heteroskedasticity to identify and estimate mismeasured and endogenous regressor models. Journal of Business and Economic Statistics, 30 (2012), 67–80.

41. Lindgren, S. At the nexus of destruction and creation: Pirate and anti-pirate discourse in Swedish online media. In Uğur Dai et al. (eds.), New Media and Interactivity. Proceedings of NMIC2010. Istanbul: Marmara University, pp. 229–236.

42. Lotan, G. The Harlem Shake: Anatomy of a viral meme. Huffingtonpost, 2013. www. huffingtonpost.com/gilad-lotan/the-harlem-shake\_b\_2804799.html.

43. Ma, L.; Krishnan, R.; and Montgomery, A. Latent homophily or social influence? An empirical analysis of purchase within a social network. Management Science, 61, 2 (2015), 454–473.

44. Ma, X.; Khansa, L.; Deng, Y.; and Kim, S.S. Impact of prior reviews on the subsequent review process in reputation systems. Journal of Management Information Systems, 30, 3 (Winter 2013–14), 279–310.

45. McLachlan, D.J., and Peel, D. Finite Mixture Models. Hoboken, NJ: Wiley, 2000.

46. Monge, P.R., and Contractor, N.S. Theories of Communication Networks. New York: Oxford University Press, 2003.

47. Muchnik, L.; Aral, S.; and Taylor, S.J. 2013. Social influence bias: A randomized experiment. Science, 341, 6146 (2013), 647–651.

48. Oestreicher-Singer, G., and Zalmanson. L. Content or community? A digital business strategy for content providers in the social age. MIS Quarterly, 37, 2 (2013), 591–616.

49. Qiu, L.; Rui, H.; and Whinston, A.B. The impact of social network structures on prediction market accuracy in the presence of insider information. Journal of Management Information Systems, 31, 1 (Summer 2014), 145–172.

50. Rogers, E.M. The diffusion of home computers among households in Silicon Valley. Marriage and Family Review, 8 (1985), 89–100.

51. Rosenbaum, P.R., and Rubin, D.B. Reducing bias in observational studies using subclassification on the propensity score. Journal of the American Statistical Association, 79, 387 (1984), 516–524.

52. Rutz, O.J.; Bucklin, R.E.; and Sonnier, G.P. A latent instrumental variables approach to modeling keyword conversion in paid search advertising. Journal of Marketing Research, 49, 3 (2012), 306–319.

53. Sacerdote, B. Peer effects with random assignment: Results for Dartmouth roommates. Quarterly Journal of Economics, 116, 2 (2001), 681–704.

54. Seabrook, J. Streaming dreams. New Yorker, January 16, 2012. www.newyorker.com/ reporting/2012/01/16/120116fa\_fact\_seabrook?currentPage=all/.

55. Seidman, S.B. Network structure and minimum degree. Social Networks, 5 (1983), 269–287.

56. Shi, Z., and Whinston, A.B. Network structure and observational learning: Evidence from a location-based social network. Journal of Management Information Systems, 30, 2 (Fall 2013), 185–212.

57. Shifman, E. An anatomy of a YouTube meme. New Media and Society, 14, 2 (2011), 187–203.

58. Susarla, A.; Oh, J.; and Tan, Y. Social networks and the diffusion of user-generated content: Evidence from YouTube. Information Systems Research, 23, 1 (2012), 23–41.

59. Stephen, A.T., and Toubia, O. Deriving value from social commerce networks. Journal of Marketing Research, 47 (2010), 215–228.

60. Szabo, G., and Huberman, B.A. Predicting the popularity of online content. Communications of the ACM, 53, 8 (2010), 80–88.

61. Tang, Q.; Gu, B.; and Whinston, A.B. Content contribution for revenue sharing and reputation in social media: A dynamic structural model. Journal of Management Information Systems, 29, 2 (2012), 41–76.

62. Trusov, M.; Bucklin, R.E.; and Pauwels, K. Effects of word-of-mouth versus traditional marketing: Findings from an Internet social networking site. Journal of Marketing, 73, 3 (2009), 90–102.

63. Wasserman, S., and Faust, K. Social Network Analysis: Methods and Applications. Cambridge: Cambridge University Press, 1994.

64. Watts, D.J. A simple model of global cascades on random networks. Proceedings of the National Academy of Sciences, 99, 9 (2002), pp. 5766–5771 .

65. Watts, D.J., and Dodds, P. Influentials, networks, and public opinion formation. Journal of Consumer Research, 34 (2007), 441–458.

66. Whyte, J. How to boost your YouTube subscribers: Power of video marketing. Search Engine Journal (December 2007). https://www.searchenginejournal.com/how-to-boost-youryoutube-subscribers-power-of-video-marketing/6105/

67. Xie,L.; Natsev, A.; He, X.; Kender, J.; Hill, M.; and Smith, J.R. Visual memes in social media: tracking real-world news in YouTube videos. In Proceedings of the Nineteenth ACM International Conference on Multimedia. ACM New York: ACM, 2011, pp. 53–62.

68. Yoganarasimhan, H. Impact of social network structure on content propagation: A study using YouTube data. Quantitative Marketing and Economics, 10, 1 (2012), 111–150.
