---
otero_id: 1030
otero_key: "GCVKWYEZ"
title: "The Effect of Bots on Human Interaction in Online Communities"
authors: "Hani Safadi; John P. Lalor; Nicholas Berente"
year: "2024"
journal: "MIS Quarterly"
doi: "10.25300/misq/2023/17901"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# THE EFFECT OF BOTS ON HUMAN INTERACTION IN ONLINE COMMUNITIES<sup>1</sup>

Hani Safadi Department of Management Information Systems, Terry College of Business, University of Georgia, Athens, GA, U.S.A. {hanisaf@uga.edu}

John P. Lalor IT, Analytics, and Operations Department, Mendoza College of Business, University of Notre Dame, Notre Dame, IN, U.S.A. {jlalor1@nd.edu}

Nicholas Berente IT, Analytics, and Operations Department, Mendoza College of Business, University of Notre Dame, Notre Dame, IN, U.S.A. {nberente@nd.edu}

We investigate how bots influence human-to-human interaction in online communities. In doing so, we distinguish between reflexive and supervisory bots delegated by community participants and moderators, respectively. We hypothesize that reflexive bot activity will reduce direct reciprocity and increase generalized reciprocity and that supervisory bot activity will reduce preferential attachment among human participants. Through an analysis of almost 70 million posts on the discussion communities on Reddit, a popular platform for online discussions, we found support for the hypotheses.

Keywords: Online communities, bots, agentic artifacts, network exchange, reflexive bots, supervisory bots, direct reciprocity, generalized reciprocity, preferential attachment, panel vector autoregression

## Introduction

There is broad scholarly interest in understanding the factors that affect the health and functioning of online communities (Faraj et al., 2011; e.g., Johnson et al., 2015; Kane et al., 2014; Kraut & Resnick, 2011; Oh et al., 2016). Yet existing research has typically examined online communities where participation was driven by human users. This is not necessarily the case today, as agentic information systems (IS) such as “bots” are becoming ubiquitous and often interact with humans as fellow participants in online communities (Ferrara et al., 2016; Salge et al., 2022).

Bots (software robots) are software programs that autonomously perform tasks on behalf of community participants. Participants in online communities deploy bots for a variety of reasons—from frivolous entertainment bots to bots that help moderate participation in communities (Halfaker & Taraborelli, 2015). Bots post content on social media (Salge et al., 2022; Salge & Karahanna, 2018), organize software development (Hukal et al., 2019), and assist with editorial work (Halfaker and Riedl 2012; Geiger 2014). The proliferation of bots is impacting social interaction in online communities and it is becoming important to understand how. Thus, in this research note, we ask: How do bots influence human social interaction in online communities? Although bots are delegates of human participants, bots’ behavior differs from humans in achieving goals. These behaviors trigger responses from humans interacting with bots and can thus change patterns of human-to-human social interaction (Neff & Nagy, 2016; Traeger et al., 2020).

To answer the research question, we distinguish among types of bots and dimensions of human social interaction. Although there are various agentic IS artifacts (Baird & Maruping, 2021), bots in online communities primarily take two forms<sup>2</sup>—reflexive and supervisory. Reflexive bots are those triggered by certain stimuli to automatically perform an action (e.g., Salge & Karahanna, 2018). Supervisory bots are endowed with decision rights to monitor a domain and influence or control activity in that domain (e.g., Hukal et al., 2019). Further, to conceptualize dimensions of human social interaction, we conceive of online communities in terms of network exchanges comprised of direct reciprocity, generalized reciprocity, and preferential attachment (Faraj & Johnson, 2011). We hypothesize that reflexive bots diffuse human attention broadly, resulting in less direct reciprocity among community participants but more generalized reciprocity across the community overall. Further, supervisory bots substitute for negotiated decision-making with community moderators, resulting in reduced preferential attachment to human members of the community.

We test our hypotheses with panel data from Reddit, an online platform of topical communities (“subreddits”). Reddit’s subreddits are online communities focused on open discussion and the free sharing of ideas (Faraj et al., 2016; Sproull & Arriaga, 2012). Such discussion communities are computer-mediated environments that are minimally structured and social in nature—they are not primarily task focused. Since bots are increasingly prevalent in discussion communities (Ferrara et al., 2016), this context is well suited to explore how bots shape human social interaction.

Using panel vector autoregression, we found support for our hypotheses. These findings contribute to the nascent and growing scholarship on the impact of bots in online communities (Geiger, 2014; Hukal et al., 2019; Neff & Nagy, 2016; Salge et al., 2022; Salge & Karahanna, 2018). The remainder of the research note is organized as follows. First, we distinguish between two forms of bots and elicit how they differ from human participants in online communities. Then, we draw on network exchange theory to construct our hypotheses. We describe our data collection and results, then conclude by discussing the implications of this research.

## Bots in Online Communities

Bots are agentic IS artifacts that act autonomously but in ways that are delegated by others. There are a variety of bots, including conversational agents (chatbots) that help to market products (Thomaz et al., 2020), decision-making bots that manage organizational activity (Kellogg et al., 2020), and online bots that disseminate information (Salge et al., 2022). Bots represent a new domain of study that departs from other information technologies by virtue of their autonomy—their activity is not necessarily “bracketed” by human interaction in the way that previous forms of technology are (Berente et al., 2021). Indeed, bots and other autonomous algorithms act as independent agents in new ways as they manage, supervise, or otherwise influence human activity (Berente et al., 2021; Kellogg et al., 2020; Möhlmann et al., 2021).

Online communities are spaces for social interaction (Faraj et al., 2016). Recent decades have witnessed a proliferation of such communities (Ellison & boyd, 2013; Johnson et al., 2015), which can involve extensive interaction among human participants (Kraut & Resnick, 2011; Sproull & Arriaga, 2012). Participants often develop deep social ties (Preece & Maloney-Krichmar, 2003; Ren et al., 2012), selforganize around common causes (Nan & Lu, 2015; Vaast et al., 2017), and collaborate on innovation (Baldwin & von Hippel, 2011; Benkler, 2006).

Prior studies of online communities have typically focused on humans, but bots are now playing a larger role. Understanding the implications of bots on human activity is thus an important frontier for research. Bots are instances of agentic IS artifacts “that have the ability to perceive and act, such as tak[ing] on specific rights for task execution and responsibilities for preferred outcomes” (Baird & Maruping, 2021, p. 317). Bots satisfy the main properties of agentic IS artifacts: situatedness, autonomy, and flexibility (Jennings et al., 1998). Bots are situated in that they are located in specific digital environments. Bots are autonomous because they act without human supervision. Bots are flexible because their actions vary in response to environmental stimuli. These three properties are continuous rather than categorical. Recent advancements in machine learning make creating more situated, autonomous, and flexible bots possible. The capacity to learn and adapt allows bots to be proactive and act opportunistically. The expanding nature of what bots and, more generally, agentic IS can do calls for a theoretical grounding of these capabilities.

The current generations of bots can help inform a theoretical foundation for studying all sorts of bots in the future. Baird and Maruping (2021) offer a taxonomy of agentic IS based on increasing decision-making latitude. The four categories are reflexive, supervisory, anticipatory, and prescriptive. Within this framework, we isolate more primitive (reflexive and supervisory) bots with an established track record (Table 1), leaving aside more advanced bots (anticipatory and prescriptive) for future work.

<table><tr><td colspan="4">Table 1. Two Types of Bots in Online Communities</td></tr><tr><td>Bot Type</td><td>Delegated By</td><td>Definition</td><td>References</td></tr><tr><td>Reflexive bots</td><td>Participants</td><td>Bots that respond to human activity by posting as community participants</td><td>Baird &amp; Maruping, 2021; Geiger, 2016; Salge et al., 2022; Salge &amp; Karahanna, 2018</td></tr><tr><td>Supervisory bots</td><td>Moderators</td><td>Bots that make decisions to manage and coordinate human activity</td><td>Baird &amp; Maruping, 2021; Geiger, 2014; Halfaker et al., 2013; Hukal et al., 2019</td></tr></table>

![](/api/attachments/GCVKWYEZ/fulltext/images/e2db859ef717bc942abc8eda66c18dce91a76d9372421acf09ff03a0d84056a7.jpg)

Reflexive bots act based on triggering events, performing specific, often repetitive tasks, but do not make decisions for the community. Reflexive bots are typically comprised of conditional statements (i.e., “if x then y”). They monitor an environment and act autonomously in response to triggers. As delegates of community participants (Geiger, 2016), they can act as participants in their own right (Seering et al., 2020) to respond to triggers to execute predefined activities. They can be used to amplify a participant’s influence in the community, such as when social media users employ bots to relay messages (Salge et al., 2022; Salge & Karahanna, 2018). Consider the Reddit bot WikiTextBot in Figure 1 (left) as an example. When a user posts a Wikipedia link in a comment, WikiTextBot automatically pulls the summary of the Wikipedia page and posts it as a reply.

Supervisory bots, on the other hand, automate the moderation of communities—they are decision-making delegates. Typically, supervisory bots act on behalf of platform moderators and administrators who seek to manage activity— “housekeeping” for the community (Hukal et al., 2019). Like reflexive bots, supervisory bots involve conditional statements and act in response to triggers. However, supervisory bots have broader decision-making authority to evaluate interactions and ensure compliance with norms and rules (Geiger, 2014). Tasks can include scanning contributions, applying quality standards (Halfaker & Taraborelli, 2015), flagging and removing low-quality content, and organizing content (Halfaker & Riedl, 2012). For example, Reddit’s AutoModerator bot in Figure 1 (right) can delete posts that do not conform to editorial standards.

## Bots and Human Social Interaction in Online Communities

Humans exhibit distinct patterns of interaction with each other in online communities (e.g., Faraj & Johnson, 2011), and when bots participate in these environments, they influence these patterns of interaction. It is important to distinguish human-to-bot interaction from human-to-human interaction (i.e., “social” interaction). Existing research has begun to focus on human-to-bot interaction, pointing out that bots can influence humans in a variety of different ways. For example, human-to-bot interaction can elicit both negative and positive human reactions, based on how they are perceived (Clément & Guitton, 2015). Bots are responsible for a significant portion of posts on social media platforms, and as a result, bots can be influential (Ferrara et al., 2016; Salge & Karahanna, 2018), and their actions can increase human engagement with the content (Delkhosh et al., 2023). Bots can spread misinformation, and humans can be deceived as a result of interacting with bots (Lazer et al., 2018). Overall, prior work shows that bots can influence humans in various ways and highlights that further research is needed to fully understand the dynamics of this relationship (Salge et al., 2022). Through their interactions with humans, bots can contribute to entertaining, informing, or managing humans in a community, and their resulting behaviors will undoubtedly impact the communities. But what is the result of bots in an online community on human-to-human interactions? In other words, how does human interaction with bots spill over to social interaction with other humans?

To begin exploring how human interaction with bots can influence patterns of human social interaction, it is important to distinguish how bots behave in communities from how humans behave. Bots are delegates of humans, but they do not behave in communities precisely as their human delegators do. Three capabilities that distinguish between bots and humans are awareness, computational, and interfacing capabilities (Baird & Maruping, 2021; Jennings et al., 1998). Awareness refers to the ability to constantly attend to available stimuli and cues across an environment. Bots can always be awake and pay attention to every post in an online community, humans cannot because their attention is limited and episodic (Simon, 1956). Computational capabilities of bots allow them to quickly and accurately process information across a greater breadth—the attention of bots has a wide reach (Salge & Karahanna, 2018). On the other hand, humans tend to be limited in their scope and speed of processing. The interfacing capabilities of bots rely on routinized processes for automated responses that allow for limited interactivity (Salge et al., 2022).<sup>3</sup> Bots are well suited for routine, superficial activities but lack the human rationality and emotion that integrate diverse stimuli for deep, meaningful interaction. Hence, while bots can manage broader simultaneous interactions, they lack the capacity for deeper engagement. This also affects decision-making; bot decisions are more procedural and automated, whereas human decisions are up for interpretation and negotiation within communities (see Table 2).

In summary, although bots are delegates of human participants, the behavior of the bots in achieving these goals differs from that of human participants. Bot behaviors trigger responses from humans, and the outcomes of these interactions can spill over to alter patterns of human-to-human social interaction (Neff & Nagy, 2016; Traeger et al., 2020).

## Hypotheses: Bot and Human Social Interaction in Online Communities

Research often conceives of online communities in terms of social networks (Safadi et al., 2021; Wasko et al., 2004; Yan et al., 2016) where interactions among participants form network patterns (Faraj & Johnson, 2011; Surma, 2016). Table 3 shows three such patterns: (1) direct reciprocity (A→B→A), (2) generalized reciprocity (A→B→C), and (3) preferential attachment (A→B←C) (Faraj & Johnson, 2011). We draw on how reflexive and supervisory bots differ from human participants and moderators to consider how bots may influence network exchange patterns.

## Reflexive Bots and Direct Reciprocity

Exchange follows a set of norms, foremost among which is reciprocity (Cropanzano & Mitchell, 2005). Expectations of reciprocity, or mutual interchange, are predicated on fairness in interaction, which forms the basis for sociality (Mashima & Takahashi, 2008; Nowak, 2006). Direct reciprocity undergirds social exchange in online communities (Faraj & Johnson, 2011; Surma, 2016) and drives participation and sharing in online communities (Yan et al., 2016). Direct reciprocity is premised on the expectation that a human’s cooperation with another will be returned (Nowak, 2006). Direct reciprocity is dyadic—a participant will act by responding to or providing resources in return for or anticipation of another participant’s actions (Faraj & Johnson, 2011). Many participants contribute to online communities expecting others to reciprocate and return their help, and there is extensive evidence of direct reciprocity in online communities (Kathan et al., 2015; Wang et al., 2015).

<table><tr><td colspan="5">Table 2. Behavioral Differences between Humans and Bots</td></tr><tr><td>Behavior</td><td>Human participant</td><td>Reflexive bot</td><td>Human moderator</td><td>Supervisory bot</td></tr><tr><td>Attention (awareness capabilities)</td><td>Episodic</td><td>Constant</td><td>Episodic</td><td>Constant</td></tr><tr><td>Reach (computational capabilities)</td><td>Local</td><td>Broad</td><td>Local</td><td>Broad</td></tr><tr><td>Interactivity (interfacing capabilities)</td><td>Deeper</td><td>Superficial</td><td>Negotiated</td><td>Procedural</td></tr></table>

<table><tr><td colspan="4">Table 3. Key Network Exchange Patterns</td></tr><tr><td>Construct</td><td>Illustration</td><td>Definition</td><td>References</td></tr><tr><td>Direct reciprocity</td><td><img src="/api/attachments/GCVKWYEZ/fulltext/images/5ad34fb76f768d84c042d0943e2296a8f79d9fb161b49cf64faf4ff0e5c4f952.jpg"/></td><td>An exchange pattern of participants responding directly to others interacting with them</td><td>Faraj &amp; Johnson, 2011; Mashima &amp; Takahashi, 2008; Nowak, 2006; Surma, 2016</td></tr><tr><td>Generalized reciprocity</td><td><img src="/api/attachments/GCVKWYEZ/fulltext/images/c362c78262e7cd39db59efb5eb4a5091d1fa36e6d5fef7261029ebb93a39adb6.jpg"/></td><td>An exchange pattern of indirect communication that supports generalized exchange</td><td>Faraj &amp; Johnson, 2011; Mashima &amp; Takahashi, 2008; Nowak &amp; Sigmund, 2005; Safadi et al., 2021</td></tr><tr><td>Preferential attachment</td><td><img src="/api/attachments/GCVKWYEZ/fulltext/images/ea8a4a55dc886d5f6a62df997033fbb96604dc9e7b3bb3322230f844157c899c.jpg"/></td><td>An exchange pattern that reflects a concentration of interaction</td><td>Barabási &amp; Albert, 1999; Capocci et al., 2006; Faraj &amp; Johnson, 2011; Johnson et al., 2014; Lu et al., 2013</td></tr></table>

Remembering Sawai Jai Singh on his death anniversary today, one of the greatest rulers in history of Rajasthan founder of Jaipur city, built the Jantar Mantar and a scholar

of the plavers, and two other passengers survived

![](/api/attachments/GCVKWYEZ/fulltext/images/e8bdae588d8389ec8a2e72222129b81422fb553cf4e0d0852d922b705a874d00.jpg)

(a) Diffusion: WikiTextBot attracted a response from "cantRYAN.” Although at other times that day, cantRYAN interacted with humans.

(b) Diversion: Deva\_Karma (bot) translates posts into Hindi and reposts them on another dedicated page, diverting participants to the other page.

Figure 2. Reflexive Bots and Direct Reciprocity: Examples of Diffusion (left) and Diversion (right)

Reflexive bots are programmed by humans for a variety of purposes (Long et al., 2017). Due to their constant attention and broad reach, reflexive bots can diffuse the episodic attention of human participants across broader areas and divert human attention away from particular interactions. Figure 2 provides examples of these mechanisms of diffusion and diversion: (1) Diffusion involves presenting stimuli to humans that spread their attention across a greater number of domains. (2) Diversion describes how bots can guide human attention away from particular discussions toward new ones. As bots broadly participate in many different discussions, they introduce contributions that would not have been otherwise included. Humans, therefore, have more information presented to them. Human attention can be diffused as a result, because these bot activities may pull human attention across topics within a discussion, and may divert this attention to different discussions. Because human attention is scarce and episodic, attention to information presented by bots is likely to be at the expense of deep interaction among dyadic sets of human participants. Reflexive bots can be seen as a particular type of super-participant who drives an increasing share of discussions (Johnson et al., 2014), but at the expense of deep, reciprocal dyadic discussions. As a result, human participants will be drawn to more discussions with more participants but there will be less reciprocity in existing discussions. Therefore, we hypothesize:

H1: Reflexive bot activity is associated with less direct reciprocity between humans in an online community.

## Reflexive Bots and Generalized Reciprocity

Reciprocity, when not directed, involves interaction with the community overall. Participants expect that others will act in kind and that their contributions will be rewarded by the community (Levine & Prietula, 2014; Surma, 2016). This indirect reciprocity results in more generalized social exchange across the community as a whole (Mashima & Takahashi, 2008). When someone helps another person, that other person will be inclined to help a third person, or someone else will be inclined to help the first person, in what is often referred to as downstream and upstream indirect reciprocity, respectively (Mashima & Takahashi, 2008; Nowak & Sigmund, 2005). Indirect or generalized reciprocity is a common feature of online communities. When participants find value in the community, they tend to contribute to the community in order to encourage engagement and strengthen the community (Constant et al., 1996; Cross & Sproull, 2004; Wasko et al., 2004). Hobby, leisure, and social support communities are largely comprised of altruistic generalized reciprocity (Goh et al., 2016). Even production communities, which are goaloriented and focused on producing artifacts (e.g., articles, software), inevitably involve generalized reciprocity. In such communities, expert participants often provide help without the expectation of a dyadic reciprocation (Constant et al., 1996; Wasko & Faraj, 2005).

Although reflexive bots will diffuse human attention, resulting in less dyadic interactions with other humans, they will also drive human interaction through their reach across the entire community. Their contributions often provide new information that can elicit reactions from humans that were not previously interacting with each other. As such, although reflexive bots diffuse attention, they also provide occasions for general interaction. Further, diverting attention to new areas can attract attention generally to those areas. Figure 3 provides two illustrations of how reflexive bots can attract interactions through two mechanisms—contributing content to existing discussions and starting new discussions: (1) Within a discussion, bots can introduce new topics that capture the attention of a wider audience. (2) Across discussions, bots’ participation can attract human participants who may not have previously engaged in discussions. Reflexive bots amplify diverse perspectives across the community in ways humans do not. Through their broad reach, reflexive bot activity can inject variety into the discourse of the community, introduce different perspectives more broadly, and generate serendipitous occasions for human interaction. Essentially, this activity provides occasions for broad social exchange among humans. Because reflexive bots operate continuously, they present opportunities for interaction between humans who otherwise would not have connected. These discussions can lead to greater engagement with the community, which can lead to more interaction, thus strengthening the community (Constant et al., 1996; Wasko et al., 2004)—resulting in greater generalized reciprocity. Therefore, we hypothesize:

H2: Reflexive bot activity is associated with more generalized reciprocity among humans in an online community.

## Supervisory Bots and Preferential Attachment

Participants with a central role in the community—typically resulting from a history of both direct and generalized reciprocity with others—enjoy what is referred to as preferential attachment (Capocci et al., 2006; Newman, 2001). Preferential attachment refers to the tendency of a few nodes in the network to generate a large number of interactions (Johnson et al., 2014) since the probability by which a new node attaches to an existing node depends on the existing node’s current connections (Barabási & Albert, 1999). In online communities, there is a subset of humans who drive a large share of the interactions (Krishnamurthy, 2002; Maillart et al., 2008) and typically have a degree of popularity as a result, which means new members of the community will interact with them—thus exhibiting preferential attachment (Capocci et al., 2006; Lu et al., 2013). Preferential attachment is often reflected in a concentration of communication in the community (Faraj & Johnson, 2011, p. 1467). Both informal and formal leaders hold significant influence over the community. This is especially true for moderators, who play a crucial role in resolving conflicts and disputes (Kane et al., 2014), with members often turning to leaders for support and assistance (Johnson et al., 2015). Therefore, we anticipate a preferential attachment toward community leaders.

![](/api/attachments/GCVKWYEZ/fulltext/images/215f343a56557a585d72f06677fb8020b06e57656a701087e357c9633cbddfa2.jpg)

## Figure 3. Reflexive Bots and Generalized Reciprocity: Within (left) and Across (right) Discussions

![](/api/attachments/GCVKWYEZ/fulltext/images/9faa7e730a55b8d8a93021b57480918d2b548856eeae6111222d600e7a2d4bf9.jpg)

(a) Bot moderation: AutoModerator enforcing moderation rules by deleting the post and closing the thread for noncompliance with posting rule.

Figure 4. Supervisory Bots and Preferential Attachment (b) Human moderation: Participants debating with moderators. Human moderators did not close the discussion and engaged with participants.

Many tasks delegated to supervisory bots are traditionally handled by community leaders and moderators who take a central role in the community. However, because supervisory bots typically do not allow for much interactivity—they are executing procedures typically in the form of conditional statements—they do not allow direct dispute. A human would always be subject to inquiry and appeal, but supervisory bots generally are not. Figure 4 illustrates this contrast. In (a), with bot moderation, the AutoModerator bot made a decision to remove and close a discussion for violating the community’s norms. There was no opportunity for further exchange. However, in (b), with a human moderator, participants engaged in a lively debate about norms, exchanging views with human moderators and other participants. Thus, bot supervision is simply procedural, whereas human moderation is often open to questioning and bargaining—i.e., it is negotiated. Supervisory bots encode and enforce moderation (David & Rullani, 2008; Geiger, 2014). Procedural decisions reduce the need for humans to coordinate with each other and negotiate each other’s decisions (Hukal et al., 2019). Humans simply do not interact with supervisory bots as they interact with human leaders. As a result, supervisory bots will reduce human-to-human preferential attachment because there will be less reason to interact with community leaders. This leads to the following hypothesis:

H3: Supervisory bot activity is associated with decreased preferential attachment among humans in an online community.

## Methods

To test our hypotheses, we studied Reddit, an online community platform that allows web users to share and discuss a wide range of topics. Reddit hosts some of the most diverse and active online communities in the Englishspeaking world. Participation is organized in communities devoted to specific topics (e.g., politics, technology, sports) referred to as subreddits. Participants, or “Redditors,” post links, texts, or images to be commented on and discussed by other participants. Redditors provide feedback to each other with upvotes or downvotes.

Data on Reddit activity is collected by the PushShift project<sup>4</sup> and posts and comments from 2005 through 2019 are publicly available on Google BigQuery. However, bot activity on Reddit is relatively low compared to human activity. We designed a sampling strategy to ensure that we identified subreddits with enough bot activity to analyze the effects of bots over time. We designed inclusion criteria at the subreddit level as follows: we selected subreddits with total comment activity (between 2005 and 2019) between 16,000 and 250,000 comments and a total proportion of bot activity among those comments between 3% and 30%. This left us with subreddits that are generally active and have a small to moderate amount of bot activity. With this strategy, 1074 subreddits fit our inclusion criteria. We examined each subreddit every month and organized the data in a panel. The final sample includes 69,336 subreddit months of activity (almost 70 million posts) from April 2007 to December 2019, with a median of 66 months per subreddit.

## Bot Operationalization

Reddit has two types of bots: user and moderator bots, which correspond to the concepts of reflexive and supervisory bots, respectively. User bots are created by participants. User bots post and comment just as human users do, typically in response to specific keywords or phrases, and have privileges associated with human participants. There are many user bots, each coded to perform a different action. For example, WikiTextBot listens for any posted Wikipedia links and replies with a summary of the linked article (Figure 1), and Deva\_Karma waits for any user mentions in a post to translate it into Hindi (Figure 2).<sup>5</sup>

Reddit participants can design user bots to automatically interact with users on Reddit through the Reddit API.<sup>6</sup> Bots have usernames just as human users do on Reddit and can access all Reddit activity. Because user bots do not need to be explicitly identified as such on Reddit, we devised a way to identify them. We relied on a convention among Reddit participants to reply to posts from bots with the phrase “good bot” or “bad bot” if the participant approves or disapproves of the bot’s action, respectively. We used an online ranking of bots using this information to identify the best bots based on the number of times users commented “good bot” or “bad bot” on the bot’s activities.<sup>7</sup> The online ranking score is the lower bound of the Wilson score (Wilson, 1927) confidence interval of the proportion of “good bot” votes.<sup>8</sup> This feature gave us a metric for identifying the most popular bots. We used this list as our list of bots. We focused on the top 2,000 ranked bots according to this metric. Beyond this, we found that entries were either very inactive with very few posts or were false positives (humans that had received a “good/bad bot” reply to one of their posts).

![](/api/attachments/GCVKWYEZ/fulltext/images/79cb62c27a2a75d62049711452b10d9e8efa7677d2b8bddb7c843646cf7e37fc.jpg)

![](/api/attachments/GCVKWYEZ/fulltext/images/35f476eaaf11319cac51381ac9b511927dc45e208c48f63b6304d232005c3cf7.jpg)  
Between January 2014 (left) and June 2018 (right), bot activity on the Football subreddit increased by a factor of ten. The human user network graphs illustrate a change in how human users interacted in the subreddit associated with increased bot activity.  
Figure 5. An Example of the Evolution of the Subreddit Network over Time

Moderator bots are delegated by community moderators to scan new posts and comments for flagged content, identify and remove spammers, etc. Reddit offers a class of moderator bots under the AutoModerator functionality. In any subreddit, there can be only up to one AutoModerator instance. This instance of AutoModerator is customized and deployed at the subreddit level by human subreddit moderators based on how they would like activity to be monitored on their subreddit.<sup>9</sup> By granting the bot access to subreddit moderator privileges, the bot can enforce predefined subreddit rules automatically (Jhaver et al., 2019). AutoModerator’s status for each subreddit is available publicly, so we were able to identify if AutoModerator was active for each subreddit and, if so, the month it was activated, as well as view all of its comments. In our data, 947 of the 1074 communities had AutoModerator activated during the observation period.

User and moderator bots are delegated by community participants and moderators, respectively. Both types of bots are triggered by human activity, with moderator bots having more decision-making latitude beyond merely posting or commenting like user bots. As such, we consider user and moderator bots to be instances of reflexive and supervisory bots within Reddit.

## Network Exchange Operationalization

Conversations in Reddit are structured as nested threaded discussions. Each thread has a starting post and participants can comment on the post or comment on others’ comments.

For this work, we focused on the effects of bots on human interaction and thus modeled interaction as a directed network where an edge connecting two participants represents a reply from the first participant to the second (see Figure 5 for an example). Since we were interested in the influence of bots on human-to-human interaction, we did not include bots in our networks. We only included edges representing replying comments, where both nodes are human participants.

Network exchange patterns:<sup>10</sup> The reciprocity score is a well-established social network measure for quantifying dyadic reciprocal exchange. It measures the ratio of bidirectional links to the total number of links in a directed network (Wasserman & Faust, 1994, p. 124). A larger value indicates that a given directed edge in the network is more likely to have an associated edge pointing in the opposite direction. In our case, higher reciprocity indicates that if Participant A has replied to one of Participant B’s posts/comments, then it is more likely that Participant B has also replied to one of Participant A’s posts/comments. To operationalize generalized reciprocity, we used the density of the directed network, calculated as the proportion of connected participant pairs over all possible dyads in the network (Wasserman & Faust, 1994, Chapter 5). A higherdensity network is indicative of a more generalized exchange with many interactions among participants.

Preferential attachment increases the incoming and outcoming interactions and thus correlates with node centrality measures.<sup>11</sup> Thus, we measured preferential attachment using

Freeman’s (1979) measure of network centralization as the sum of differences between the in-degree centrality of the most central node and all other nodes, divided by the same sum calculated on a star graph with the same number of nodes. This measurement provides the extent to which the observed network conforms to the ideal type of a centralized network (Borgatti & Everett, 2006) in which few nodes enjoy most ties as expected when preferential attachment is prevalent (Faraj & Johnson, 2011).

Bot activity: We operationalized bot activity by considering the propensity of their activity in the community. Activity is measured as the ratio of bot comments to total comments in the subreddit-month. We calculated this ratio for user bots and moderator bots to operationalize user bot activity and moderator bot activity, respectively.

Controls: Controls include the overall number of comments in the subreddit/month, the total number of human moderators, and the number of human participants to measure community activity, community moderation, and community membership, respectively. Table 4 shows constructs and measures and Table 5 presents descriptive statistics and correlations. All variables are per subreddit-month.

<table><tr><td>Construct</td><td>Operationalization</td></tr><tr><td colspan="2">Outcomes</td></tr><tr><td>(1) Direct reciprocity</td><td>Reciprocity score of the human-human interaction network of the subreddit-month</td></tr><tr><td>(2) Generalized reciprocity</td><td>Density of the human-human interaction network of the subreddit-month</td></tr><tr><td>(3) Preferential attachment</td><td>In-degree centralization of the human-human interaction network of the subreddit-month</td></tr><tr><td colspan="2">Predictors</td></tr><tr><td>(4) User bot activity</td><td>The number of user bot comments divided over the total number of comments of both bots and humans in the subreddit-month</td></tr><tr><td>(5) Moderator bot activity</td><td>The number of moderator bot comments divided over the total number of comments of both bots and humans in the subreddit-month</td></tr><tr><td colspan="2">Controls</td></tr><tr><td>(6) Community activity</td><td>Number of comments in the subreddit-month</td></tr><tr><td>(7) Community moderation</td><td>The number of human moderators in the subreddit-month</td></tr><tr><td>(8) Community membership</td><td>The number of human participants in the subreddit-month</td></tr></table>

<table><tr><td colspan="10">Table 5. Descriptive Statistics (top) and Correlation Matrix (bottom)</td></tr><tr><td colspan="2"></td><td>Mean</td><td>SD</td><td>Minimum</td><td>p25</td><td>Median</td><td>p75</td><td colspan="2">Maximum</td></tr><tr><td colspan="2">(1) Direct reciprocity</td><td>.42</td><td>.16</td><td>0</td><td>.33</td><td>.43</td><td>.52</td><td colspan="2">1</td></tr><tr><td colspan="2">(2) Generalized reciprocity</td><td>.042</td><td>.11</td><td>0</td><td>.0049</td><td>.011</td><td>.028</td><td colspan="2">1.50</td></tr><tr><td colspan="2">(3) Preferential attachment</td><td>.13</td><td>.16</td><td>0</td><td>.053</td><td>.089</td><td>.15</td><td colspan="2">2</td></tr><tr><td colspan="2">(4) User bot activity</td><td>.015</td><td>.041</td><td>0</td><td>0</td><td>.0013</td><td>.0095</td><td colspan="2">.98</td></tr><tr><td colspan="2">(5) Moderator bot activity</td><td>.046</td><td>.088</td><td>0</td><td>0</td><td>0</td><td>.056</td><td colspan="2">.97</td></tr><tr><td colspan="2">(6) Community activity</td><td>1143.9</td><td>2179.5</td><td>1</td><td>191</td><td>533</td><td>1300</td><td colspan="2">100547</td></tr><tr><td colspan="2">(7) Community moderation</td><td>3.07</td><td>8.78</td><td>0</td><td>1</td><td>2</td><td>4</td><td colspan="2">363</td></tr><tr><td colspan="2">(8) Community membership</td><td>227.8</td><td>366.9</td><td>1</td><td>44</td><td>118</td><td>273</td><td colspan="2">16389</td></tr><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td colspan="2">(8)</td></tr><tr><td>(1)</td><td>1</td><td>.14*</td><td>.26*</td><td>-.062*</td><td>-.022*</td><td>.1*</td><td>.042*</td><td colspan="2">.024*</td></tr><tr><td>(2)</td><td>.019*</td><td>1</td><td>.45*</td><td>-.33*</td><td>-.28*</td><td>-.84*</td><td>-.29*</td><td colspan="2">-.95*</td></tr><tr><td>(3)</td><td>-.081*</td><td>.53*</td><td>1</td><td>-.25*</td><td>-.18*</td><td>-.17*</td><td>-.18*</td><td colspan="2">-.32*</td></tr><tr><td>(4)</td><td>-.05*</td><td>-.019*</td><td>-.031*</td><td>1</td><td>.18*</td><td>.35*</td><td>.3*</td><td colspan="2">.33*</td></tr><tr><td>(5)</td><td>-.017*</td><td>-.062*</td><td>-.065*</td><td>-.068*</td><td>1</td><td>.34*</td><td>.3*</td><td colspan="2">.28*</td></tr><tr><td>(6)</td><td>.061*</td><td>-.15*</td><td>-.059*</td><td>.049*</td><td>.081*</td><td>1</td><td>.31*</td><td colspan="2">.93*</td></tr><tr><td>(7)</td><td>.025*</td><td>-.018*</td><td>-.018*</td><td>.096*</td><td>.057*</td><td>.053*</td><td>1</td><td colspan="2">.32*</td></tr><tr><td>(8)</td><td>-.003</td><td>-.2*</td><td>-.16*</td><td>.017*</td><td>.03*</td><td>.79*</td><td>.068*</td><td colspan="2">1</td></tr></table>

Note: 71,173 observations in 1,074 groups, Pearson correlations in bottom triangle, Spearman correlations in top triangle, \* p < 0.05

<table><tr><td colspan="7">Table 6. PVAR Results</td></tr><tr><td> $DV_{s,m}=$ </td><td colspan="2">Direct  $reciprocity_{s,m}$ </td><td colspan="2">Generalized  $reciprocity_{s,m}$ </td><td colspan="2">Preferential  $attachment_{s,m}$ </td></tr><tr><td> $\beta_1 DV_{s,m-1}$ </td><td>.097***</td><td>(.027)</td><td>.643***</td><td>(.032)</td><td>.234***</td><td>(.029)</td></tr><tr><td> $\beta_2 Community activity_{s,m-1}$ </td><td>.000*</td><td>(.000)</td><td>-.000</td><td>(.000)</td><td>.000*</td><td>(.000)</td></tr><tr><td> $\beta_3 Community moderation_{s,m-1}$ </td><td>-.000</td><td>(.001)</td><td>.000*</td><td>(.000)</td><td>.000</td><td>(.000)</td></tr><tr><td> $\beta_4 Community membership_{s,m-1}$ </td><td>-.000</td><td>(.000)</td><td>-.000</td><td>(.000)</td><td>-.000**</td><td>(.000)</td></tr><tr><td> $\beta_5 User bot activity_{s,m-1}$ </td><td>-.679**</td><td>(.258)</td><td>.071*</td><td>(.034)</td><td>-.080</td><td>(.110)</td></tr><tr><td> $\beta_6 Moderator bot activity_{s,m-1}$ </td><td>-.064</td><td>(.035)</td><td>-.003</td><td>(.006)</td><td>-.153***</td><td>(.023)</td></tr><tr><td>Hansen&#x27;s  $J\chi^2 statistic$ </td><td colspan="2">431.0***</td><td colspan="2">446.3***</td><td colspan="2">478.3***</td></tr></table>

Note: Robust standard errors in parentheses, $p < 0 . 0 5 , \^ { \star \star } p < 0 . 0 1 , \^ { \star \star \star } p < 0 . 0 0 1$

## Results

Our main estimation approach is the panel vector autoregression (PVAR) model (Abrigo & Love, 2016; Holtz-Eakin et al., 1988), which allowed us to examine the relationship between bot activity and network exchange. Additionally, the PVAR model can establish Granger causality. We adopted the reduced form of the PVAR model, where the dependent variable is endogenous and hence a linear function of its lagged value, as well as the lagged independent variables of network characteristics and the lagged control variables. We used a lag of 1 based on lag-order selection statistics for Lags 1 to 4. The overall coefficient of determination increases with more lags, but the increases were minimal beyond Lag 1 (0.1% to 0.8%). We also accounted for unobserved heterogeneity of individual communities and temporal trends by introducing the individual-specific effect and time-fixed effects. We employed robust standard errors to mitigate heteroskedasticity. The model is as follows; the results are summarized in Table 6.

$$
\begin{array}{l} D V _ {s, m} = \beta_ {1} D V _ {s, m - 1} + \beta_ {2} C o m m u n i t y a c t i v i t y _ {s, m - 1} + \\ \beta_ {3} C o m m u n i t y m o d e r a t i o n _ {s, m - 1} + \\ \beta_ {4} C o m m u n i t y m e m b e r s h i p _ {s, m - 1} + \\ \beta_ {5} U s e r b o t a c t i v i t y _ {s, m - 1} + \\ \beta_ {6} M o d e r a t o r b o t a c t i v i t y _ {s, m - 1} + \alpha_ {s} + u _ {s m}, (w h e r e s \\ a n d m r e f e r t o s u b r e d d i t a n d m o n t h) \end{array}
$$

We found support for H1 $( \beta _ { 5 } = - 0 . 6 7 9 ^ { \ast \ast \ast } )$ . The reflexive activity of user bots is associated with less human direct reciprocity. Because bot activity is measured with the percentage of posting by bots and network reciprocity varies from 0 to 1, this relationship can be interpreted as a decrease of 0.679% in direct reciprocity associated with a 1% increase in user bots’ activity. H2 is also supported. User bots’ activity led to increased generalized reciprocity $( \beta _ { 5 } = 0 . 0 7 1 ^ { * } )$ . Because density in a directed network ranges from 0 to 2, the relationship can be interpreted as an increase of 3.55% associated with an increase of 1% in user bots’ activity.

Finally, supporting H3, supervisory bots were negatively associated with preferential attachment given decreased network in-degree centralization $( \beta _ { 6 } = - 0 . 1 5 3 ^ { \ast \ast \ast } )$ . Because centralization varies from 0 to 2, this relationship can be interpreted as a decrease of 7.65% in centralization associated with a 1% increase in moderator bot activity.

## Causal Interpretation

The PVAR model can establish a less strict form of causality referred to as Granger causality (Granger, 1988). In this form of causality, the focus is on whether one time-series variable can be used to predict the future outcomes of another timeseries variable. Formally, we say that Time Series X Grangercauses Time Series Y if the past values of X can be used for the prediction of the future values of Y. Following the PVAR estimation, we performed pairwise Granger causality tests (Abrigo & Love, 2016) between the dependent variables (network exchange patterns) and the key independent variables of user bot activity and moderator bot activity. The results of these tests are detailed in Appendix B (available upon request). However, they conform with the findings of PVAR (Table 6). Together, these findings suggest that we can interpret the results in a Granger-causal way. Past bot activity can predict a change in future human-human interaction.

## Robustness Checks

We conducted a series of robustness checks to measure the impact of various operational decisions on our results (Appendix A, available upon request). Our checks covered how we identified bots and how many bots we included, the inclusion criteria for subreddits, and false negatives in our data (i.e., bots that were not identified as bots and mistakenly considered humans). Specifically, we accounted for changing network dynamics (A.1.1) and false negatives in bot identification (A.1.2 and A.1.3), excluded human moderators from the networks (A.1.4), and used a different source for bot identification (A.1.5). We then increased (A.1.6) and decreased (A.1.6) the bot detection thresholds and applied more strict inclusion criteria for bots (A.1.8 and A.1.9). We also excluded outlier communities (A.1.10) and employed alternative measurements for the dependent variables (A.2). The results are summarized in Table 7. A detailed discussion is available in Appendix A, which is available upon request.

After replacing our bot list with a different list (A.1.5), we discovered that our results were not statistically significant. We believe that this particular list is inadequate, particularly because it is no longer accessible on the webpage from which we obtained it. Despite this, we included this check in our results for the sake of comprehensiveness. When we decreased the number of bots examined from 2000 to 1000 (A.1.7), we discovered that H3 was no longer supported while H1 and H2 continued to be supported. This is likely due to the fact that the AutoModerator bot is ranked 1849 in our list of bots. Therefore, when we limited our analysis to 1000 bots, AutoModerator was no longer considered a bot and was instead included in the human-human interaction network. The inclusion of this bot specifically impacted H3, as it is the primary supervisory bot on the Reddit platform (although its behavior can be customized for each subreddit that chooses to use it). By excluding AutoModerator from our bot analysis, we also excluded the main mechanism for influencing preferential attachment (H3). When we limited the number of subreddits considered (A.1.8), we found that H2 was no longer supported. The changes in network density were not evident, and we attributed this to the fact that networks with higher bot activity will also experience a greater change in density. This assumption was validated when we loosened the inclusion criteria to a more moderate restriction in our main analysis (A.1.9).

## Discussion

Reddit was valued at \$10 billion in August 2021.<sup>12</sup> This valuation reflects the value of human participation and contribution to online communities (Baldwin & von Hippel, 2011; Faraj et al., 2016). Maintaining the health of online communities, retaining their members, and sustaining their contribution is therefore an important goal of practical and scholarly interest (Butler, 2001; Faraj et al., 2011; Kraut & Resnick, 2011). Yet the landscape of online communities is changing. While the moderation of online content is extremely important for the functioning of online communities (Skousen et al., 2020), the growth of participation and the quantity of offensive and inappropriate content stresses the capacities of human moderators to function (Cheng et al., 2015). Many online communities deploy some form of bot to assist in their moderation (Halfaker & Taraborelli, 2015; Hukal et al., 2019), and many online communities enable user bots as well (Geiger, 2014, 2016). However, existing work does not address how this abundance of bot activity affects human participation and social interaction. In this research note, we take an initial step in this direction. This is particularly important given the rise of generative artificial intelligence instantiated through chatbots. In order to navigate a future where bots possess greater capabilities, it is essential to have a solid theory of their foundations. There are many different types of bots and their capabilities are a moving target. While advancements in artificial intelligence are drawing more attention to bots, many mainstream bots are still largely rule based.<sup>13</sup> Even in many situations that involve artificially intelligent bots, their participation in online communities is triggered and enacted according to conditions, much like rule-based bots.

<table><tr><td colspan="4">Table 7. Summary of Robustness Checks</td></tr><tr><td>Analysis</td><td>Hypothesis 1</td><td>Hypothesis 2</td><td>Hypothesis 3</td></tr><tr><td>Main</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td colspan="4">Robustness Tests in Appendix A</td></tr><tr><td>A.1.1</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.2</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.3</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.4</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.5</td><td>Positive, significant</td><td>Negative, not significant</td><td>Negative, not significant</td></tr><tr><td>A.1.6</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.7</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, not significant</td></tr><tr><td>A.1.8</td><td>Negative, significant</td><td>Negative, not significant</td><td>Negative, significant</td></tr><tr><td>A.1.9</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.1.10</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr><tr><td>A.2</td><td>Negative, significant</td><td>Positive, significant</td><td>Negative, significant</td></tr></table>

In our study, rule-based bots had considerable influence on human interaction. Reflexive bot activity decreased direct reciprocity and increased generalized reciprocity, while supervisory bot activity decreased preferential attachment. This shows that the potential impact of including bots in online social environments can be significant even when the bots are relatively simple. Although various studies in IS and human-computer interaction have examined bots, with few exceptions (e.g., Salge et al., 2022), not many studies have theorized about bots. Our work contributes to this nascent domain to unpack how bots can influence human social interaction by drawing on network exchange theory.

First, bots are delegated by other humans to achieve their goals. However, in achieving these goals, bots participate and engage with human participants, and their participation differs from other humans because of their different attention, reach, and interactivity. These differing behaviors (to reach the same goals) can create unintended consequences on other human participants’ behavior. This observation emphasizes the potential for interactive technology, designed with a specific goal in mind, to have unintended consequences due to its interactive nature. This contributes to the ongoing discourse on the unintended impacts of technology (Aanestad et al., 2021; Rahwan et al., 2019). Second, scholarly work in IS has examined the materiality and affordances of online communities (Faraj et al., 2011; Ferguson & Soekijad, 2016; Levina & Arriaga, 2014). This body of work examines how the design of the community platform affords and constrains the actions of its members. Our work contributes to extending this work to show that such affordances extend beyond the static element of community design (e.g., Vaast et al., 2017) to interactive, agentic components such as bots. Third, recent work examining the new wave of technologies such as AI and ML cautions against both the intended and the unintended consequences of the substitution of human activity and human labor (Berente et al., 2021; Brynjolfsson et al., 2021). Our work shows that understanding such substitution extends beyond who is partaking in the activity. While substituting for human moderator activity, supervisory bots can change how other participants perceive such moderation, suggesting that substitution does not necessarily imply equivalence. This conclusion calls for examining the spillover effects of agentic IS beyond their intended activity (e.g., Lebovitz et al., 2021; Traeger et al., 2020).

## Practical Contributions

During Elon Musk’s \$44 billion takeover attempt of Twitter in 2022, bots were one of the contentious issues; this example exemplifies the controversy and confusion around the role of bots.<sup>14</sup> Bots can be good or bad, and it often depends on the perspective. Our work provides practical contributions to stakeholders in online communities. For instance, community managers are interested in understanding the implications of enabling bots. If bots increase human-human interaction, then introducing bots can be of potential benefit, given that human interaction and contribution create value. However, our work cautions against such a simplistic conclusion, given that reflexive bots, while increasing generalized reciprocity, simultaneously decrease direct reciprocity. This suggests a trade-off between promoting the breadth and depth of interaction through bots. Whereas promoting the breadth of interaction can be beneficial, it also risks marginalizing deep reciprocal interactions and, as a result, trivializing the community into a promotional space (Bulgurcu et al., 2018).

Further, given the growth of participation, the value of moderation work, and the scarcity of moderation resources, it is not surprising that many online communities are implementing supervisory bots (Halfaker & Riedl, 2012). Moderation tasks are extremely valuable (Skousen et al., 2020). For instance, it is estimated that in 2020, Reddit moderators worked for at least 466 hours per day. This is the equivalent of an estimated 3.4 million USD per year (Li et al., 2022). Our research points out the impact of supervisory bots in weakening the centrality of human participants and potentially decreasing the depth of interaction in communities without the associated increase in breadth of interaction that we found in other reflexive bots. These results caution practitioners to implement widespread supervisory bots carefully.

## Limitations and Future Work

In this study, we focused on the association between bots and human-to-human interaction. Without a prior theoretical foundation, the “detective work” for underlying mechanisms that can be later confirmed or refuted is valuable (Puranam, 2018, pp. 159-161). The intuition of our detective work in this research is reflected in emerging research that is being conducted on how humans interact with each other around autonomous agents (e.g., Traeger et al., 2020). Characteristics of the autonomous agent influence humanto-human social interaction in ways that are different from other technical elements of platform infrastructures.

In this work, we considered rule-based bots that perform specific roles coded by their developers. Today, many bots in operation are rule based. They execute relatively simple instructions at scale to improve the user experience through efficiency and broad coverage. However, the next phase in automated bots is the “learning bots” phase. Learning bots, powered by machine learning techniques and generative AI, will be data-driven bots and will thus invoke further implications for exhibiting complex behavior and altering human behavior in more unexpected ways—as demonstrated by the example of Microsoft Tay (Salge & Berente, 2017). For example, an “intelligent bot” could lead human participants to focus on topics that need critical thinking, stimulating discussions among human participants and leading to more reciprocity as a result. Future work should test the limit of our findings with rule-based bots and further develop our understanding of how bots alter and shape human interaction in online environments.

Second, beyond the three mainstream exchange patterns of direct reciprocity, generalized reciprocity, and preferential attachment, future research should examine other mechanisms, such as triadic closure and local search (Jackson & Rogers, 2007; Kossinets & Watts, 2006). Third, the scope of this work could be expanded to provide a better understanding of the roles of the participants as they engage with bots. Such an understanding could help community managers save time by using bots without diminishing the overall experience of participants. Finally, bots may have an impact on users’ social interactions outside the focal subreddits where they encounter the bots. This spillover effect would be an interesting extension of this work.

## Summary and Conclusion

In this research note, we took a step toward theoretically unpacking how the proliferation of bots in online communities can influence human-to-human social interaction. Specifically, and notwithstanding advances in machine learning, we focus on two types of bots with relatively limited decision-making latitude (Baird & Maruping, 2021): reflexive and supervisory bots. We theorize how these two types of bots are associated with changes in network exchange patterns of direct reciprocity, generalized reciprocity, and preferential attachment. Future work could draw on this work as a basis for understanding the impact of different forms of AI on human social interaction.

## Acknowledgments

We appreciate the engagement and support of the editors and reviewers during the review process. Hani Safadi acknowledges financial support from the Terry-Sanford Research Award.

## References

Aanestad, M., Kankanhalli, A., Maruping, L., Pang, M.-S., & Ram, S. (2021). Special issue—Call for papers: Digital technologies and social justice. MIS Quarterly. https://misq.umn.edu/skin/ frontend/default/misq/pdf/CurrentCalls/SI\_DigitalTechnologies.p df

Abrigo, M. R. M., & Love, I. (2016). Estimation of panel vector autoregression in Stata. Stata Journal, 16(3), 778-804. https://doi.org/10.1177/1536867x1601600314

Baird, A., & Maruping, L. M. (2021). The next generation of research on IS use: A Theoretical framework of delegation to and from agentic IS artifacts. MIS Quarterly, 45(1), 315-341. https://doi.org/10.25300/MISQ/2021/15882

Baldwin, C. Y., & von Hippel, E. (2011). Modeling a paradigm shift: From producer innovation to user and open collaborative innovation. Organization Science, 22(6), 1399-1417. https://doi.org/10.1287/orsc.1100.0618

Barabási, A.-L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.

Benkler, Y. (2006). The wealth of networks: How social production transforms markets and freedom. Yale University Press.

Berente, N., Gu, B., Recker, J., & Santhanam, R. (2021). Managing artificial intelligence. MIS Quarterly, 45(3), 1433-1450. https://doi.org/10.25300/MISQ/2021/16274

Borgatti, S. P., & Everett, M. G. (2006). A Graph-theoretic perspective on centrality. Social Networks, 28(4), 466-484. https://doi.org/10.1016/j.socnet.2005.11.005

Brynjolfsson, E., Wang, C., & Zhang, X. (2021). The economics of IT and digitization: Eight questions for research. MIS Quarterly, 45(1), 473-477. https://doi.org/10.25300/MISQ/2021/15434.1.4

Bulgurcu, B., Van Osch, W., & Kane, G. C. (2018). The rise of the promoters: User classes and contribution patterns in enterprise social media. Journal of Management Information Systems, 35(2), 610-646. https://doi.org/10.1080/07421222.2018.1451960

Butler, B. S. (2001). Membership size, communication activity, and sustainability: A resource-based model of online social structures. Information Systems Research, 12(4), 346-362. https://doi.org/ 10.1287/isre.12.4.346.9703

Capocci, A., Servedio, V. D. P., Colaiori, F., Buriol, L. S., Donato, D., Leonardi, S., & Caldarelli, G. (2006). Preferential attachment in the growth of social networks: The internet encyclopedia Wikipedia. Physical Review E, 74(3), Article 36116. https://doi.org/ 10.1103/PhysRevE.74.036116

Cheng, J., Danescu-Niculescu-Mizil, C., & Leskovec, J. (2015). Antisocial behavior in online discussion communities. In Proceedings of the 9th International Conference on Web and Social Media (pp. 61-70). http://www.aaai.org/ocs/index.php/ ICWSM/ICWSM15/paper/view/10469

Clément, M., & Guitton, M. J. (2015). Interacting with bots online: Users’ reactions to actions of automated programs in Wikipedia. Computers in Human Behavior, 50, 66-75. https://doi.org/10.1016/ j.chb.2015.03.078

Constant, D., Sproull, L., & Kiesler, S. (1996). The kindness of strangers: The usefulness of electronic weak ties for technical advice. Organization Science, 7(2), 119-135. https://doi.org/ 10.1287/orsc.7.2.119

Cropanzano, R., & Mitchell, M. S. (2005). Social exchange theory: An interdisciplinary review. Journal of Management, 31(6), 874-900.

Cross, R., & Sproull, L. (2004). More than an answer: Information relationships for actionable knowledge. Organization Science, 15(4), 446-462. http://www.jstor.org/stable/30034748

David, P. A., & Rullani, F. (2008). Dynamics of innovation in an open source collaboration environment: Lurking, laboring, and launching FLOSS projects on SourceForge. Industrial and Corporate Change, 17(4), 647-710. https://doi.org/10.1093/ icc/dtn026

Delkhosh, F., Gopal, R. D., Patterson, R. A., & Yaraghi, N. (2023). Impact of bot involvement in an incentivized blockchain-based online social media platform. Journal of Management Information Systems, 40(3), 778-806. https://doi.org/10.1080/07421222.2023. 2229124

Ellison, N. B., & boyd, D. (2013). Sociality through social network sites. In W. H. Dutton (Ed.), The Oxford handbook of internet studies (pp. 151-172). Oxford University Press. https://doi.org 10.1093/oxfordhb/9780199589074.001.0001

Faraj, S., Jarvenpaa, S. L., & Majchrzak, A. (2011). Knowledge collaboration in online communities. Organization Science, 22(5), 1224-1239. https://doi.org/10.1287/orsc.1100.0614

Faraj, S., & Johnson, S. L. (2011). Network exchange patterns in online communities. Organization Science, 22(6), 1464-1480. https://doi.org/10.1287/orsc.1100.0600

Faraj, S., von Krogh, G., Monteiro, E., & Lakhani, K. R. (2016). Online community as space for knowledge flows. Information Systems Research, 7047, 1-17. https://doi.org/10.1287/isre.2016.0682

Ferguson, J. E., & Soekijad, M. (2016). Multiple interests or unified voice? Online communities as intermediary spaces for development. Journal of Information Technology, 31(4), 358-381. https://doi.org/10.1057/jit.2015.25

Ferrara, E., Varol, O., Davis, C., Menczer, F., & Flammini, A. (2016). The rise of social bots. Communications of the ACM, 59(7), 96- 104. https://doi.org/10.1145/2818717

Freeman, L. C. (1979). Centrality in social networks conceptual clarification. Social Networks, 1(3), 215-239.

Geiger, R. S. (2014). Bots, bespoke, code and the materiality of software platforms. Information Communication and Society, 17(3), 342-356. https://doi.org/10.1080/1369118X.2013.873069

Geiger, R. S. (2016). Bot-based collective blocklists in Twitter: The counterpublic moderation of harassment in a networked public space. Information Communication and Society, 19(6), 787-803. https://doi.org/10.1080/1369118X.2016.1153700

Goh, J. M., Gao, G. (Gordon), & Agarwal, R. (2016). The creation of social value: Can an online health community reduce rural-urban health disparities? MIS Quarterly, 40(1), 247-263. https://doi.org/ 10.25300/MISQ/2016/40.1.11

Granger, C. W. J. (1988). Causality, cointegration, and control. Journal of Economic Dynamics and Control, 12(2), 551-559.

Halfaker, A., Geiger, R. S., Morgan, J. T., & Riedl, J. (2013). The rise and decline of an open collaboration system. American Behavioral Scientist, 57(5), 664-688. https://doi.org/10.1177/0002764212 469365

Halfaker, A., & Riedl, J. (2012). Bots and cyborgs: Wikipedia’s immune system. Computer, 45(3), 79-82. https://doi.org/10.1109 MC.2012.82

Halfaker, A., & Taraborelli, D. (2015, November 30). Artificial intelligence service “ORES” gives Wikipedians X-ray specs to see through bad edits. Wikimedia Blog. https://blog.wikimedia.org/ 2015/11/30/artificial-intelligence-x-ray-specs/

Holtz-Eakin, D., Newey, W., & Rosen, H. S. (1988). Estimating vector autoregressions with panel data. Econometrica, 56(6), 1371-1395. https://doi.org/10.2307/1913103

Hukal, P., Berente, N., Germonprez, M., & Schecter, A. (2019). Bots coordinating work in open source software projects. Computer, 52(9), 52-60. https://doi.org/10.1109/MC.2018.2885970

Jackson, M. O., & Rogers, B. W. (2007). Meeting strangers and friends of friends: How random are social networks? American Economic Review, 97(3), 890-915. https://doi.org/10.1257/aer.97.3.890

Jennings, N. R., Sycara, K., & Wooldridge, M. (1998). A roadmap of agent research and development. Autonomous Agents and Multi-Agent Systems, 1(1), 7-38. https://doi.org/10.1023/A:10100 90405266

Jhaver, S., Birman, I., Gilbert, E., & Bruckman, A. (2019). Humanmachine collaboration for content regulation. ACM Transactions on Computer-Human Interaction, 26(5), 1-35. https://doi.org/ 10.1145/3338243

Johnson, S. L., Faraj, S., & Kudaravalli, S. (2014). Emergence of power laws in online communities: The role of social mechanisms and preferential attachment. MIS Quarterly, 38(3), 795-808.

Johnson, S. L., Safadi, H., & Faraj, S. (2015). The emergence of online community leadership. Information Systems Research, 26(1), 165- 187. https://doi.org/10.1287/isre.2014.0562

Kane, G. C., Johnson, J., & Majchrzak, A. (2014). Emergent life cycle: The tension between knowledge change and knowledge retention in open online coproduction communities. Management Science, 60(12), 3026-3048. https://doi.org/10.1287/mnsc.2013.1855

Kathan, W., Hutter, K., Füller, J., & Hautz, J. (2015). Reciprocity vs. free-riding in innovation contest communities. Creativity and Innovation Management, 24(3), 537-549. https://doi.org/10.1111/ caim.12107

Kellogg, K. C., Valentine, M. A., & Christin, A. (2020). Algorithms at work: The new contested terrain of control. Academy of Management Annals, 14(1), 366-410. https://doi.org/10.5465/ annals.2018.0174

Kossinets, G., & Watts, D. J. (2006). Empirical analysis of an evolving social network. Science, 311(5757), 88-90. https://doi.org/ 10.1126/science.1116869

Kraut, R. E., & Resnick, P. (2011). Building successful online communities: Evidence-based social design. In Building successful online communities: Evidence-based social design. MIT Press.

Krishnamurthy, S. (2002). Cave or community?: An empirical examination of 100 mature open source projects. First Monday, 7(6). https://doi.org/10.5210/fm.v0i0.1477

Lazer, D. M. J., Baum, M. A., Benkler, Y., Berinsky, A. J., Greenhill, K. M., Menczer, F., Metzger, M. J., Nyhan, B., Pennycook, G., Rothschild, D., Schudson, M., Sloman, S. A., Sunstein, C. R., Thorson, E. A., Watts, D. J., & Zittrain, J. L. (2018). The science of fake news. Science, 359(6380), 1094-1096. https://doi.org/ 10.1126/science.aao2998

Lebovitz, S., Levina, N., & Lifshitz-Assa, H. (2021). Is AI ground truth really true? The dangers of training and evaluating AI tools based on experts’ know-what. MIS Quarterly, 45(3), 1501-1526.

https://doi.org/10.25300/MISQ/2021/16564

Levina, N., & Arriaga, M. (2014). Distinction and status production on user-generated content platforms: Using Bourdieu’s theory of cultural production to understand social dynamics in online fields. Information Systems Research, 25(3), 468-488. https://doi.org/ 10.1287/isre.2014.0535

Levine, S. S., & Prietula, M. J. (2014). Performance open collaboration for innovation: Principles and performance. Organization Science, 25(5), 1414-1433. https://doi.org/10.1287/orsc.2013.0872

Li, H., Hecht, B., & Chancellor, S. (2022). Measuring the monetary value of online volunteer work. arXiv. http://arxiv.org/abs/ 2205.14528

Long, K., Vines, J., Sutton, S., Brooker, P., Feltwell, T., Kirman, B., Barnett, J., & Lawson, S. (2017). “Could you define that in bot terms”? In Proceedings of the CHI Conference on Human Factors in Computing Systems (pp. 3488-3500). https://doi.org/10.1145/ 3025453.3025830

Lu, Y., Jerath, K., & Singh, P. V. (2013). The emergence of opinion leaders in a networked online community: A dyadic model with time dynamics and a heuristic for fast estimation. Management Science, 59(8), 1783-1799. https://doi.org/10.1287/mnsc.1120.1685

Maillart, T., Sornette, D., Spaeth, S., & Von Krogh, G. (2008). Empirical tests of Zipf’s law mechanism in open source Linux distribution. Physical Review Letters, 101(21), 1-4. https://doi.org/10.1103/PhysRevLett.101.218701

Mashima, R., & Takahashi, N. (2008). The emergence of generalized exchange by indirect reciprocity. In A. Biel, D. Eek, T. Gärling, & M. Gustafsson (Eds.), New issues and paradigms in research on social dilemmas (pp. 159-176). Springer.

Möhlmann, M., Zalmanson, L., Henfridsson, O., & Gregory, R. W. (2021). Algorithmic management of work on online labor platforms: When matching meets control. MIS Quarterly, 45(4). 1999-2022. https://doi.org/10.25300/MISQ/2021/15333

Nan, N., & Lu, Y. (2015). Harnessing the power of self-organization in an online community during organizational crisis. MIS Quarterly, 39(4), 1135-1158.

Neff, G., & Nagy, P. (2016). Talking to bots: Symbiotic agency and the case of Tay. International Journal of Communication, 10, 4915- 4931.

Newman, M. E. J. (2001). Clustering and preferential attachment in growing networks. Physical Review E, 64(2), Article 25102. https://doi.org/10.1103/PhysRevE.64.025102

Nowak, M. A. (2006). Five rules for the evolution of cooperation. Science, 314(5805), 1560-1563. https://doi.org/10.1126/science. 1133755

Nowak, M. A., & Sigmund, K. (2005). Evolution of indirect reciprocity. Nature, 437(7063), 1291-1298. https://doi.org/ 10.1038/nature04131

O’Mahony, S., & Ferraro, F. (2007). The emergence of governance in an open source community. Academy of Management Journal, 50(5), 1079-1106. https://doi.org/10.5465/amj.2007.27169153

Oh, W., Moon, J. Y., Hahn, J., & Kim, T. (2016). Research note— Leader influence on sustained participation in online collaborative work communities: A simulation-based approach. Information Systems Research, 27(2), 383-402. https://doi.org/10.1287/isre. 2016.0632

Preece, J., & Maloney-Krichmar, D. (2003). Online communities:

focusing on sociability and usability. In J. A. Jacko & A. Sears (Eds.), Handbook of human-computer interaction (pp. 596-620). Lawrence Erlbaum Associates.

Puranam, P. (2018). The microstructure of organizations. Oxford University Press.

Rahwan, I., Cebrian, M., Obradovich, N., Bongard, J., Bonnefon, J. F., Breazeal, C., Crandall, J. W., Christakis, N. A., Couzin, I. D., Jackson, M. O., Jennings, N. R., Kamar, E., Kloumann, I. M., Larochelle, H., Lazer, D., McElreath, R., Mislove, A., Parkes, D. C., Pentland, A. “Sandy,” … Wellman, M. (2019). Machine behaviour. Nature, 568(7753), 477-486. https://doi.org/10.1038/ s41586-019-1138-y

Ren, Y., Harper, F. M., Drenner, S., Terveen, L., Kiesler, S., Riedl, J., Kraut, R. E., Ren, Harper, Drenner, Terveen, Kiesler, Riedl, & Kraut. (2012). Building member attachment in online communities: Applying theories of group identity and interpersonal bonds. MIS Quarterly, 36(3), 841-864. https://doi.org/10.2307/41703483

Rheingold, H. (1993). The virtual community: Finding connection in a computerized world. Addison-Wesley Longman.

Safadi, H., Johnson, S. L., & Faraj, S. (2021). Who contributes knowledge? Core-periphery tension in online innovation Communities. Organization Science, 32(3), 752-775. https://doi.org/ 10.1287/orsc.2020.1364

Salge, C. A. D. L., & Berente, N. (2017). Is that social bot behaving unethically? Communications of the ACM, 60(9), 29-31. https://doi.org/10.1145/3126492

Salge, C. A. D. L., & Karahanna, E. (2018). Protesting corruption on Twitter: Is it a bot or is it a person? Academy of Management Discoveries, 4(1), 32-49. https://doi.org/10.5465/amd.2015.0121

Salge, C. A. D. L., Karahanna, E., & Thatcher, J. B. (2022). Algorithmic processes of social alertness and social transmission: How bots disseminate information on Twitter. MIS Quarterly, 46(1), 229- 260. https://doi.org/10.25300/MISQ/2021/15598

Seering, J., Luria, M., Ye, C., Kaufman, G., & Hammer, J. (2020). It takes a village: Integrating an adaptive chatbot into an online gaming community. In Proceedings of the CHI Conference on Human Factors in Computing Systems.

Simon, H. A. (1956). Rational choice and the structure of the environment. Psychological Review, 63(2), 129-138.

Skousen, T., Safadi, H., Young, C., Karahanna, E., Safadi, S., & Chebib, F. (2020). Successful moderation in online patient communities: Inductive case study. Journal of Medical Internet Research, 22(3), Article e15983. https://doi.org/10.2196/15983

Sproull, L., & Arriaga, M. (2012). Online communities. In H. Bidgoli (Ed.), Handbook of computer networks (pp. 898-914). John Wiley & Sons. https://doi.org/10.1002/9781118256107.ch58

Surma, J. (2016). Social exchange in online social networks. The reciprocity phenomenon on Facebook. Computer Communications, 73, 342-346. https://doi.org/10.1016/j.comcom.2015.06.017

Thomaz, F., Salge, C., Karahanna, E., & Hulland, J. (2020). Learning from the dark web: Leveraging conversational agents in the era of hyper-privacy to enhance marketing. Journal of the Academy of Marketing Science, 48(1), 43-63. https://doi.org/10.1007/s11747- 019-00704-3

Traeger, M. L., Sebo, S. S., Jung, M., Scassellati, B., & Christakis, N. A. (2020). Vulnerable robots positively shape human conversational dynamics in a human-robot team. Proceedings of the National Academy of Sciences of the United States of America, 117(12), 6370-6375. https://doi.org/10.1073/pnas.1910402117

Vaast, E., Safadi, H., Lapointe, L., & Negoita, B. (2017). Social media affordances for connective action: An examination of microblogging use during the Gulf of Mexico oil spill. MIS Quarterly, 41(4), 1179-1205. https://doi.org/10.25300/MISQ/ 2017/41.4.08

Wang, G. A., Liu, X., Wang, J., Zhang, M., & Fan, W. (2015). Examining micro-level knowledge sharing discussions in online communities. Information Systems Frontiers, 17(6), 1227-1238. https://doi.org/10.1007/s10796-015-9566-1

Wasko, & Faraj. (2005). Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quarterly, 29(1), 35-57. https://doi.org/10.2307/25148667

Wasko, M., Faraj, S., & Teigland, R. (2004). Collective action and knowledge contribution in electronic networks of practice. Journal of the Association for Information Systems, 5(11), 493-513. https://doi.org/10.17705/1jais.00058

Wasserman, S., & Faust, K. (1994). Social network analysis: Methods and applications (Vol. 8). Cambridge University Press. https://doi.org/10.1017/CBO9780511815478

Wilson, E. B. (1927). Probable inference, the law of succession, and statistical inference. Journal of the American Statistical Association, 22(158), 209-212.

Yan, Z., Wang, T., Chen, Y., & Zhang, H. (2016). Knowledge sharing in online health communities: A social exchange theory perspective. Information & Management, 53(5), 643-653. https://doi.org/10.1016/j.im.2016.02.001

## About the Authors

Hani Safadi is an associate professor at Terry College of Business, University of Georgia. He is interested in online collectives and theory development. His research is published in MIS Quarterly, where he served as associate editor, as well as Information Systems Research, Organization Science, Journal of the Association for Information Systems, and Journal of Medical Internet Research, among other outlets.

John P. Lalor is an assistant professor of IT, analytics, and operations at the University of Notre Dame’s Mendoza College of Business. His research interests include natural language processing and text mining, including topic models and deep learning architectures for text sequence classification. He received his Ph.D. degree from the University of Massachusetts Amherst’s College of Information and Computer Science.

Nicholas Berente is a professor of IT, analytics, and operations at the University of Notre Dame’s Mendoza College of Business. He received his Ph.D. from Case Western Reserve University. His research interests include digital innovation, artificial intelligence, and institutional change in organizations. He is a senior editor at MIS Quarterly and Information and Organization.
