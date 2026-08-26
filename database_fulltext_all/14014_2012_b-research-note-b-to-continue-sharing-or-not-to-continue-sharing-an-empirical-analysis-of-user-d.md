---
otero_id: 14014
otero_key: "R7BWN49B"
title: "<b>Research Note</b>—To Continue Sharing or Not to Continue Sharing? An Empirical Analysis of User Decision in Peer-to-Peer Sharing Networks"
authors: "Mu Xia; Yun Huang; Wenjing Duan; Andrew B. Whinston"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0344"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/R7BWN49B/fulltext/images/948b2e74faf3b727aa3390d279d9f66f808eee16dcb598abb91eb1f61c7648ae.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Research Note—To Continue Sharing or Not to Continue Sharing? An Empirical Analysis of User Decision in Peer-to-Peer Sharing Networks

Mu Xia, Yun Huang, Wenjing Duan, Andrew B. Whinston,

## To cite this article:

Mu Xia, Yun Huang, Wenjing Duan, Andrew B. Whinston, (2012) Research Note—To Continue Sharing or Not to Continue Sharing? An Empirical Analysis of User Decision in Peer-to-Peer Sharing Networks. Information Systems Research 23(1):247-259. http://dx.doi.org/10.1287/isre.1100.0344

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R7BWN49B/fulltext/images/fe2ff6f4c05f6e1f2ed87ec07521e7f858181a25b9a743b02c1000f26985b62c.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

Research Note

# To Continue Sharing or Not to Continue Sharing? An Empirical Analysis of User Decision in Peer-to-Peer Sharing Networks

Mu Xia

Department of Operations Management and Information Systems, Leavey School of Business, Santa Clara University, Santa Clara, California 95053, mxia@scu.edu

Yun Huang

Science of Networks in Communities (SONIC), Department of Industrial Engineering and Management Sciences, Northwestern University, Evanston, Illinois 60208, yun@northwestern.edu

Wenjing Duan

Department of Information Systems & Technology Management, School of Business, The George Washington University, Washington, DC 20052, wduan@gwu.edu

Andrew B. Whinston

Center for Research in Electronic Commerce, McCombs School of Business, University of Texas at Austin, Austin, Texas 78712, abw@uts.cc.utexas.edu

eer-to-peer sharing networks have seen explosive growth recently. In these networks, sharing files is completely voluntary, and there is no financial reward for users to contribute. However, many users continue to share despite the massive free-riding by others. Using a large-scale data set of individual activities in a peer-topeer music-sharing network, we seek to understand users’ continued-sharing behavior as a private contribution to a public good. We find that the more benefit users “get from” the network, in the form of downloads, browses, and searches, the more likely they are to continue sharing. Also, the more value users “give to” the network, in the form of downloads by other users and recognition by the network, the more likely they are to continue sharing. Moreover, our findings suggest that, overall, “getting from” is a stronger force for the continued-sharing decision than “giving to.”

Key words: peer-to-peer networks; music sharing; IRC, voluntary contribution; sharer; free rider; public good History: Sanjeev Dewan, Senior Editor; Chris Forman, Associate Editor. This paper was received on July 20, 2008, and was with the authors 13 months for 3 revisions. Published online in Articles in Advance April 8, 2011.

## 1. Introduction

The past decade has witnessed the emergence and explosive growth of peer-to-peer (P2P) sharing networks (e.g., Asvanund et al. 2004, Krishnan et al. 2004, Jian and McKie-Mason 2006). In these distributed networks, all content is contributed by users voluntarily, with no financial reward. Accordingly, having a sufficient number of users participate and continually share content in a P2P network is crucial to its sustainability. Interestingly, despite the massive freeriding observed, users do share continuously in many P2P networks (Adar and Huberman 2000, Saroiu et al. 2002). Researchers have been trying to comprehend, mainly through the analytical approach, why they do so (Golle et al. 2001, Ranganathan et al. 2003). Extant empirical investigation on P2P networks is scarce, and what does exist is largely at the aggregate level (Asvanund et al. 2004). In this paper, using a unique individual-level activity data set collected in a P2P network, we empirically investigate drivers of individual users’ sharing decisions.

We distinguish between users’ continued-sharing decision and their start-sharing decision (i.e., when they decide to share files in the network for the first time). Our interest is in the former, which is the users’ decision to stay and continue to share after they join. It is different from the start-sharing decision, which has been the focus of most extant literature studying online communities. Users can make continued-sharing decisions more than once, which is an important variable to examine to understand the dynamics of online sharing networks.

The determinants of the continued-sharing decision are different from those of the start-sharing one. For the start-sharing decision, external factors that either occur outside of a network or can be observed from the outset are the main determinants. For example, for a music-sharing network, the availability of other competing music-sharing services affects a user’s decision about whether to join and start sharing. Once the user decides to start sharing, however, internal factors (i.e., those from within the network that cannot be observed without joining) will carry more weight in changing the user’s decision of whether to continue sharing. For example, a user may be driven to a P2P network for the novelty of its focus, which is observable before she joins; however, she may be put off and decide to leave if she has a negative experience in the network, such as network congestion resulting from excessive downloading.

In a decentralized setting like P2P networks, where users host files on their own servers, an individual user’s decision to continue sharing is an important measure to investigate for several reasons. First, continued sharing is important because it improves the “stickiness” of the network, which leads to better member retention as more active members stay to share in the network (Walczuch et al. 2001). Other often-used measures of contributions in a network, such as the total number of contributors and the total amount of contribution, are functions of the aggregate user decision of continued sharing. Therefore, studying individuals’ decisions gets to the root of the issue and accounts for the significant heterogeneity of participants.

Second, because P2P networks are distributed and rely on participants to serve the content, continued sharing ensures the availability of content for participants, whereas one-time sharing only benefits the participants who happen to log in at the same time as the user. Furthermore, the perception of quality from participants is based on the content availability when they log in, and their willingness to stay depends on such quality, which improves with more continued sharing. Therefore, more continued sharing results in more participants and possibly, in turn, even more sharing.

In this paper, we ask the question, “What drives users’ continued sharing?” We examine how users’ individual sharing decisions are affected by their behaviors and experiences in a P2P network. Building on theories of private provision of public goods, we hypothesize that such continued-sharing decisions are affected by what users “get from” the network and what they “give to” the network. Using a large-scale data set of individual user activities logged in a P2P music-sharing network, we test the two hypotheses using logistic models with individual panel data.

We have two major findings. First, the more benefit a user “gets from” the network, the more likely she is to continue sharing. Second, the more value a user “gives to” the network, the more likely she is to continue sharing. In the case of P2P networks, the significant benefit a user receives is in the form of downloads, searches, and browses she conducts; the value she provides to the network that influences her continued-sharing decision is in the form of downloads by other users and recognition by the network.

## 2. Theoretical Background and Research Hypotheses

## 2.1. Research Context

Music sharing is one of the first large-scale and most popular applications of P2P networks. Our study is conducted in the context of music sharing in Internet relay chat (IRC), which was originally designed for instant communication through a collection of topicoriented chat rooms called IRC channels (Pioch 1997). To participate in a channel, a user must register with a unique username. Users often install scripts (e.g., SDFind and OmenServe) that can turn individual personal computers into file servers, and they share their file collections through special channels called serving channels.<sup>1</sup> Each user can send file search and download requests to the central channel, which then broadcasts them to all sharing users, and the users automatically respond to the requester if there are matching files in their local collections. Because of the large number of users and commands, the channel interface scrolls extremely fast. As a result of the fast scrolling, there is little actual chatting and all activities observed in the channel are commands and requests submitted by users.

IRC provides an ideal environment for this study. All music sharing in IRC is voluntary and free. In addition, compared to other P2P file-sharing applications such as Napster, Gnutella, and Kazaa, three unique characteristics make IRC a good subject to study. First, IRC channels have a very long history that covers the lifespan of other competing filesharing paradigms (Asvanund et al. 2004). Second, the IRC sharing mechanism has not been changed since its release. Therefore, the mechanism itself should have no influence on changes in user behavior in the time period we observed. Third, the status of the network and the activities are easily observable to users. At the network level, the list of sharing and nonsharing users in the network is public information and readily accessible. At the individual level, detailed logs of other users’ downloading activities of one’s own content are continuously recorded, which makes measures of many variables available for researchers to analyze.

In this study, our focus is the “continued-sharing” decision in P2P networks (i.e., we are interested in users’ decisions to stay and continue to contribute after they join). The continued-sharing decision is dynamic in that it can change over time, and for the network to be sustainable it is crucial that as many users as possible always make the choice to continue sharing. Previous literature emphasizes the importance of maintaining the “stickiness” of online communities (e.g., Walczuch et al. 2001) (i.e., retaining members’ active participation). This issue can be more pronounced in a content-based P2P network because a user might not be able to directly observe the dynamics of the network and judge the “quality” beforehand. Therefore, for a P2P network to be sustainable, it must entice more members to keep sharing continuously.

## 2.2. P2P Networks and Online Communities

In this section, we review previous studies on P2P networks and online communities. Existing P2P studies focus on aggregate-level investigation, such as examining overall characteristics (e.g., Adar and Huberman 2000, Saroiu et al. 2002), users’ contribution incentives (e.g., Golle et al. 2001, Ranganathan et al. 2003, Krishnan et al. 2004), and the influence of network externalities (Asvanund et al. 2004). However, to further understand the sustainability of these networks, we need to delve deeper to investigate the individual user’s actions. Related extant literature examining people’s incentives to contribute online mainly comes from the online community setting. While P2P networks are different from online communities, findings from the online community literature provide guidance in studying P2P networks. In particular, just as in P2P networks, continued contribution is the key condition for the sustainability of online communities (Herring 2004, Fayard and DeSanctis 2005).

The online communities that are the foci of the extant literature are mostly conversation based, such as organizational networks, online forums, or mailing lists. Such communities often have a richer and stronger social context than P2P networks. The contributing behavior can then be the result of the offline social setting the users are experiencing. For example, Constant et al. (1996) report that motivations to answer other employees’ questions broadcast in a corporate e-mail system include a number of organizationally oriented factors such as organizational citizenship (“being a good company citizen”) and job obligation (“it’s part of my job”). Even outside organizational boundaries, online reputation may spill over to the offline context. In a study by Wasko and Faraj (2005) of an online message board for a national professional association, professional reputation is found to be a significant predictor of user contribution.

Even for pure online networks, often there is a specific purpose that provides a natural bond for participants, such as learning (Haythornthwaite 2005), contributing to public document repositories (Peddibhotla and Subramani 2007), or providing support (Rodgers and Chen 2005, Ma and Agarwal 2007). In Usenet newsgroups, where most users choose not to disclose their true identity, users value participation for its exchange of ideas, learning, and interaction with the community (Wasko and Faraj 2000).

In the aforementioned studies, conversations are an important precondition of the social setting, especially in pure online networks. Without conversations, the social setting is weak, the exchange of ideas is lacking, and many of the motivations to contribute might not hold. In a P2P network, in which few conversations are conducted between users, the resulting weakened social interactions would seem to limit the drivers of contribution. Nevertheless, one can conjecture that the behavior of users might be more affected by their experience, i.e., their own and observations of others’ activities, in the network. If users can develop personal connections online, despite the absence of face-to-face interactions (Walther 1992, Spears and Lea 1992, Walther et al. 2001), it may be possible that even when words cannot be exchanged and the social aspect of the network is weakened to its extreme, people still exhibit social behavior.

## 2.3. Research Hypotheses

Sharing in a P2P network can be regarded as contributing to a public good. A public good is defined as a good for which consumption is nonexcludable and nonrivalrous (Mas-Collel et al. 1995, p. 359). Although a pure public good is rare (Shmanske 1991), most of the noncommercial online offerings exhibit many attributes of a public good (Kollock 1999). For online goods, because the cost to exclude consumption is very low, the choice of making the good exclusive or nonexclusive is not about cost. In a noncommercial online network, the good (e.g., the contributed content) is often made nonexclusive so as to maximize its reach. Even though some communities require registration to access the content, it is used not as a way to exclude users, but to enhance the network feature (Kollock 1999). Therefore, unlike public goods in the physical world, where the actions as a group are often needed for the provision (e.g., staging a social protest, providing national defense), an individual user’s contribution of information is the provision of a public good in the online setting.

Because our goal is to understand users’ sharing behavior, we need to first identify its associated costs.

Costs are incurred in two stages of public goods development: the production stage and the distribution and maintenance stage (Monge et al. 1998). For online goods, the maintenance cost (i.e., the cost of making the content available over a period of time) can be significant and even higher than the production cost. In P2P networks, both costs are borne by contributors, who have to create the content and make it available on their own servers for others to download. If the content is not created by the contributors, the cost is incurred to obtain the content and possibly to litigate in the case of pirated content. For example, in the IRC network, because a user’s IP address can be retrieved, the cost of getting caught pirating content is significant. In addition, the user has to convert content to the right format and rename the file to include the artist, album, and song information explicitly for searching proposes. The maintenance and distribution cost is mainly that of keeping the server online to provide files across an extended period of time; such cost may be in the form of electricity cost, risk of network attacks, hard disk failure, and bandwidth expenditure. Overall, these costs are significant enough to influence users’ decisions to contribute. In contrast, in conversation-based communities, such as online forums, the cost of distribution and maintenance is borne by the network operator, which can be significant—even astronomical. For example, it is reported that YouTube spends more than \$1 million in bandwidth costs every month (Huang et al. 2007). Because it is not borne by users, the cost is not expected to affect their decision to share.

To understand continued voluntary sharing as a contribution to a public good and, specifically, to develop the following two groups of hypotheses, we draw on online public goods literature. Constant et al. (1996) and Wasko and Faraj (2005) argue that even in an open network, expectations of receiving personal benefits can motivate users to contribute to the online public good in the absence of personal acquaintance. The concept of reciprocity is often used to explain such contributing behavior (Connolly and Thorn 1990). It is based on the fact that when people expect to receive benefit from another, they tend to have the incentive to offer benefit as well. Wellman and Gulia (1999) and Rheingold (1994) have reported that individuals who regularly contribute knowledge indeed receive help more quickly when they ask for something. Going beyond a dyadic exchange, when the other party is a group instead of an individual, generalized reciprocity applies (Emerson 1972, 1976; Ekeh 1974; Yamagishi and Cook 1993), which posits that people contribute to public goods because of the “obligation” to reciprocate with members in a group. Even in a one-to-many setting, instead of a one-to-one relationship, people contribute because they expect to personally benefit from the group. Furthermore, the more benefits they receive from the group, the more they would like to pay back. Based on this stream of work, we expect that if a user receives significant benefits from a network, he or she will have a strong incentive to contribute. In a P2P network, the acts of both downloading and providing content might be considered generalized reciprocity. In other words, when a user consumes resources (a public good) from a group, she has incentives to contribute to the group in return. Therefore, we hypothesize as follows.

<sup>Hypothesis</sup> <sup>1</sup> <sup>(H1).</sup> The more benefit a user receives directly from the network, the more likely she is to continue sharing.

Butler et al. (2007) identify four benefits that users expect when contributing to an online network: informational, social, visibility related, and altruistic. In a P2P network where no social benefit can be obtained, the other three benefits still apply. Of the three, information benefits are derived directly from the content obtained from the network, which is specifically relevant to this hypothesis. (The other two are used to develop H2.) The information benefit is akin to the benefit a P2P user receives from downloading, browsing content, and searching (i.e., what she “gets from” the network). Similarly, the results of Wasko and Faraj’s (2000) study of technical UseNet groups reveal three benefits to users that drive their participation: tangible returns, intangible returns, and community interest. Although community interest does not apply in the P2P case, the tangible return refers to information gains from the network. That is, the more the user undertakes these activities, such as downloading, browsing, and searching in the network, the more likely she will continue sharing. Therefore, we hypothesize the following.

<sup>Hypothesis</sup> <sup>1A</sup> <sup>(H1A).</sup> The more files a user downloads, the more likely she is to continue sharing.

<sup>Hypothesis</sup> <sup>1B</sup> <sup>(H1B).</sup> The more a user browses other users’ file collections, the more likely she is to continue sharing.

<sup>Hypothesis</sup> <sup>1C</sup> <sup>(H1C).</sup> The more a user searches, the more likely she is to continue sharing.

Moreover, the user’s benefit may depend on the speed with which these tasks are accomplished. The faster the download the user experiences, the more benefit she receives, and the more likely she would be to continue sharing. However, one might also argue for the opposite: The slower the download a user experiences, the more incentive she has to continue sharing. One support for such an argument is the offloading effect (Krishnan et al. 2004, Jian and McKie-Mason 2006), which says that a user shares because by doing so she can add to the content and bandwidth of the whole network and direct some traffic to her own server, thereby reducing congestion to other users and improving her own downloading experience. Nevertheless, in a large P2P network, it is unlikely that a single user’s contribution makes a difference in reducing congestion, given the large number of users and files. Therefore, when the two opposing forces compete in shaping a user’s continued-sharing decision, we believe the offloading effect is less influential. As a result, more positive experiences in speed will make users more likely to share.

<sup>Hypothesis</sup> <sup>1D</sup> <sup>(H1D).</sup> The faster a user’s download speed in using the network, the more likely she is to continue sharing.

To derive our second group of hypotheses, we employ impure altruism theory, or “warm glow,” which argues that people contribute to a public good because of the benefits of giving. It posits that when a good exhibits both public and private good characteristics, some people may be motivated to contribute because the joy of giving more than offsets the cost, as is observed in charity giving. Both Cornes and Sandler (1984, 1994) and Andreoni (1989, 1990) argue, through analytical modeling, that when taking into account the private benefits of giving, such as “warm glow,” (i.e., when people take joy in the act of giving itself), contribution to a public good can be expected in equilibrium. Moreover, the total contribution is more than what a pure altruism theory would predict. These researchers used the term “impure” because the “warm glow” is for the contributor herself and is thus a seemingly selfish motivation. An important precondition for “warm glow” to have any effect on a user is the visibility of the value directly brought by her contribution. In a P2P network, there are statistics a user can observe that might suggest her “value” to the network. Our data allow us to test how different statistics affect users’ decisions to continue sharing. In the work of Butler et al. (2007), both visibility and altruistic benefits refer to the effect achieved as a result of what the user “gives to” the network. Similarly, the “intangible returns” in Wasko and Faraj (2000) as drivers of contribution refer to intrinsic satisfaction and self-actualization, which are based on what the user “gives to” the network. Therefore, we hypothesize as follows.

<sup>Hypothesis</sup> <sup>2</sup> <sup>(H2).</sup> The more value a user provides to the network, the more likely she is to continue sharing.

From a user’s perspective, the value from contribution has two aspects. The user can derive value (i.e., “warm glow”) from the actual consumption of her contributed content by someone else and from an indication of her overall involvement. Consumption of the content can be measured in two ways: the number of times the user’s files have been downloaded by others and the number of times the user’s collection has been browsed by others. Therefore, we have the following hypotheses.

<sup>Hypothesis</sup> <sup>2A</sup> <sup>(H2A).</sup> The more files other users download from a user, the more likely she is to continue sharing.

<sup>Hypothesis</sup> <sup>2B</sup> <sup>(H2B).</sup> The more times other users browse a user’s collection, the more likely she is to continue sharing.

The administrators of the network also display other statistics about a user’s involvement in the network. In the case of the IRC music-sharing network we investigated, the network is managed by a number of operators, and they give some users a “value user” mark, a plus sign (“+”) in front of their usernames, for their logging-in and sharing activities in the channel. We hypothesize the following.

<sup>Hypothesis</sup> <sup>2C</sup> <sup>(H2C).</sup> More involved users are more likely to continue sharing.

## 3. Data Collection and Description

## 3.1. Observed Activities and Types of Users

IRC channels act as automatic P2P networks, like Gnutella and OpenNap. As proposed by Asvanund et al. (2004), P2P network structures can be categorized along two axes: the degree of decentralization of the content and that of the catalog (i.e., list of files available). Both the content and catalog of the IRC file-sharing channels are decentralized because files are indexed and stored by individual computers. The IRC servers provide only centralized message communication that broadcasts requests to all users. The responses to requests are peer to peer. That is, if one user has a matching file, her script server will respond to the sender directly. This hybrid structure makes it easier to monitor all user requests but harder to confirm the actual transactions.

Table 1 shows, as an example, a section of raw data we observed in IRC. Files in the sharing channel are all provided by individual users and hosted on their own servers. Once a logged-in user turns on the sharing function, her file server automatically reports the server status in the channel (e.g., Line 1 in Table 1). Based on this information, we can calculate server parameters, such as the total number of files provided, workload (the length of the download queue), and the bandwidth the user allocated for sharing.<sup>2</sup> We define a user as a sharer if we observe her server status at least once during a certain time period. After a user stays and shares in a channel for a while, the administrator of the IRC channel may recognize that sharer as a “value user” for her contribution.<sup>3</sup> Conversely, we define a user as a “free rider” if she did not turn on the sharing option for the entire period.

Table 1 Commands in An IRC File-Sharing Channel

<table><tr><td>Line</td><td>Raw log (Dec 1st, 2002)</td><td>Explanation</td></tr><tr><td>1</td><td>[00:04]Tons of Rare &amp; Moldy Oldies and A Whole Lotta Everything Else Type: @Fouyia For My List Of: 16,525 Files ± Free Slots: 1/5 ± Files In Queue: 6 ± Total Speed: 21,376 cps</td><td>Bob&#x27;s server status</td></tr><tr><td>2</td><td>[00:47]@find pink Floyd</td><td>Amy searches for Pink Floyd&#x27;s songs.</td></tr><tr><td>3</td><td>[00:50]!Bob Pink Floyd—A Great Day For Freedom.mp3</td><td>Amy downloads one file from Bob.</td></tr><tr><td>4</td><td>[00:51]@Bob</td><td>Amy browses Bob&#x27;s collection.</td></tr><tr><td>5</td><td>[00:52]!Bob Pink Floyd—Burning Bridges.mp3</td><td>Amy gets another file from Bob</td></tr><tr><td>6</td><td>[00:55]@Bob-que</td><td>Amy checks Bob&#x27;s download queue</td></tr></table>

There are four types of user requests: search, download, browse, and delay query. To illustrate, see Line 2 in Table 1, where, to find songs by Pink Floyd, Amy sends a search command “@find” with keywords “pink floyd” to the channel, and IRC servers broadcast it to all other users in the channel. All sharers’ servers, Bob’s being one of them, automatically perform the search and, if matches are found, send back the file name information. Based on these responses, Amy can decide what to download and from whom. In Line 3, Amy issues a download command to get the file “Pink Floyd—A Great Day For Freedom.mp3” from Bob. Depending on the workload, Bob’s file server either sends the file out immediately or puts the download request in its queue, waiting for the next available download slot. If she does not receive the file after a while, Amy can query Bob’s file server to see the position of her request among all download requests in the download queue (Line 6 in Table 1).

In addition to keyword searching, users can use browse commands to get a complete list of all the files another user provides (Line 4) before requesting files from the list (Line 5). On the receiving end, any user can view the download statistics and browse requests received (i.e., Bob has a log of requests sent by other users like Amy). Table 2 describes all key variables developed based on the command activities in the sharing channel.

Table 2 Description of Key Variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td colspan="2">Dependent variable</td></tr><tr><td> $Decision_{it}$ </td><td>Sharer  $i$ &#x27;s choice of action after period  $t$ : 1—sharing or 0—stop sharing</td></tr><tr><td colspan="2">Individual sharer activity variables</td></tr><tr><td> $Download_{it}$ </td><td>The total number of files downloaded by sharer  $i$  during period  $t$  (in thousands)</td></tr><tr><td> $Search_{it}$ </td><td>The total number of search commands used by sharer  $i$  during period  $t$ </td></tr><tr><td> $Delay_{it}$ </td><td>Total number of delay queries sent by sharer  $i$  during period  $t$ </td></tr><tr><td> $Browse_{it}$ </td><td>Total number of times sharer  $i$  browsed during period  $t$ </td></tr><tr><td> $Contribute_{it}$ </td><td>The total number of files downloaded from sharer  $i$  during period  $t$  (in thousands)</td></tr><tr><td> $Value\_user_{it}$ </td><td>A dummy variable indicating whether sharer  $i$  had been marked as a value user during period  $t$ </td></tr><tr><td> $Been\_browsed_{it}$ </td><td>Total number of times sharer  $i$  had been browsed by others during period  $t$ </td></tr><tr><td colspan="2">Individual sharer control variables</td></tr><tr><td> $Sharing\_history_{it}$ </td><td>The number of periods sharer  $i$  has shared before period  $t$ </td></tr><tr><td> $Files_{it}$ </td><td>Average collection size of sharer  $i$  during period  $t$  (in thousands)</td></tr><tr><td> $Queue\_length_{it}$ </td><td>Average length of queue of sharer  $i$  during period  $t$ </td></tr><tr><td> $Bandwidth_{it}$ </td><td>Maximal bandwidth of sharer  $i$  during period  $t$  (Kbps)</td></tr><tr><td colspan="2">Network aggregate variables</td></tr><tr><td> $Sharer\_size_t$ </td><td>The number of users who shared music during period  $t$  (in thousands)</td></tr><tr><td> $Freerider\_size_t$ </td><td>The number of users who did not share music during period  $t$  (in thousands)</td></tr><tr><td> $Total\_download_t$ </td><td>The total number of files downloaded during period  $t$  (in thousands)</td></tr></table>

## 3.2. Data Set and Description

Because commands sent to IRC channels are publicly observable, we logged all activities (more than 300 million) in one of the largest IRC musicsharing channels, #mp3passion, from March 2001 to May 2006. Figure 1 plots the biweekly numbers of downloads during the data collection period. At its peak during the year 2003, more than one million files were exchanged biweekly, which amounts to 0.05% of total global music sharing at the time (Wingfield and Smith 2003).

During the entire data collection period, the user size of the sharing channel was stable, with around 20,000 unique users, whereas the number of sharers grew from 600 to more than 2,000. We observe 55,031 unique sharers in total, along with 834,613 free riders.

## 3.3. Issues in Data Processing

3.3.1. User Identities. Our empirical models are individual based, and users are identified by their IDs $( \mathrm { i . e . , }$ nicknames) in the channel (e.g., Amy and Bob in Table 1). Generally, the user ID is an option users can set and save in the IRC client program, so they only need to do it once. Although it is possible to use multiple IDs, we believe there is little incentive for users to do so for two reasons: first, changing IDs does not offer any additional protection of identity because one can easily retrieve a user’s IP address by issuing a command; second, many heavy users often attach significant value to an ID because of the reputation and “cachet” built over long-term use. Thus, they have a strong incentive not to use a different ID. It is also possible that multiple people share the same user ID. To see if and how often this happens, we retrieved all the users’ IP addresses at a number of time points. We found that, both within a snapshot and across time, for each unique IP address, there existed only one ID.

Figure 1 Plot of Number of Downloads (Biweekly)  
![](/api/attachments/R7BWN49B/fulltext/images/8adb5b92281ff0ee6b5351ef9e8d77f727414b4d04aa9ac29105e59d13d47b76.jpg)

3.3.2. Time Window. Our dependent variable, whether a user chose to share during a certain time period, is a binary choice variable that is defined based on the user’s status in that period. Because the channel operates continuously with a large volume of commands being sent and users logging in and out, we need to determine the length of the time window in which to define a user’s status. As discussed, within a time window a user can be a sharer, a free rider, or absent $( \mathrm { i . e . , }$ no observable activities) during that period. In determining the length of the time window, we have to balance two opposing factors. The window cannot be too short because it would not truly reflect the change of user behavior. It also cannot be too long or it will combine too many unrelated activities together. Based on these considerations, we chose two weeks to be the length of the time windows. We also used different time windows as a robustness check, which is discussed later in §4.

4. Empirical Methodology and Results Our primary objective is to analyze the factors in a P2P network that might affect sharers’ decisions to continue sharing. We define a user as a sharer if she turned on the sharing option at least once during the five-year time period. We use the binary choice model with fixed effects on individual panel data to test the factors that influence individual sharers’ decisions (Wooldridge 2002):

$$
\begin{array}{r} P (y _ {i t + 1} = 1 \mid y _ {i t} = 1, X _ {i t}, c _ {i}, c _ {t}) = G (X _ {i t} \beta , c _ {i}, c _ {t}), \\ i = 1, \ldots , N; t = 1, \ldots , T, \end{array}
$$

where $y _ { i t } = 1$ and $y _ { i t + 1 } = 1$ indicate that sharer i turns on the file server in time periods t and $t + 1 ;$ where $X _ { i t }$ is a vector of independent variables that describe the experience and the influence that sharer i has in period t (we discuss these independent variables in more detail in §4.2); and where $c _ { i }$ is a vector of individual-user dummy variables to capture any unobserved intrinsic individual characteristics and $c _ { t }$ is a vector of time dummy variables that denotes the unobserved effect in period t. G4 · 5 is a logistic specification of the linear combination of the independent variables $( X _ { i t } \beta + c _ { t } + c _ { i } )$ , which formalizes the probability of sharer i’s choice between to share or not to share at t + 1, given that she has shared at t.

As discussed in the previous section, we used the time window of two weeks as our primary panel data composition, which divides our data into 135 continuous periods 4T = 1355. Sharers announce their status in the channel every five minutes. Of the 55,031 sharers in the data set, if we did not observe any status announcement from the sharer, we considered its appearance too brief and deleted it from our data. Of the 48,327 “effective” sharers left, we randomly selected 1,000 sharers and used all the periods after they shared as our data points 4N = 319175.

Of all the sharers, the majority of them (67.4%) shared continuously, whereas only a small percentage (18.1%) temporarily stopped sharing more than once. For the 470 users who shared more than one period, the median length between their first and last sharing periods is nine periods, i.e., 18 weeks. On average, each of these sharers temporarily stopped sharing 2.6 times. The median length of such stoppage is two periods.

Table 3 Data Point Illustration

<table><tr><td></td><td>Period 1</td><td>Period 2</td><td>Period 3</td><td>Period 4</td><td>Period 5</td></tr><tr><td>User 1</td><td>0</td><td>1</td><td>0</td><td>1</td><td>0</td></tr><tr><td>User 2</td><td>1</td><td>0</td><td>1</td><td>1</td><td>0</td></tr><tr><td>User 3</td><td>0</td><td>0</td><td>0</td><td>1</td><td>1</td></tr><tr><td>User 4</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr></table>

4.1. Operationalization of the Dependent Variable Our dependent variable is the sharer’s decision about whether to continue sharing in the following period. We view this decision made by a user as an individual one that may change over time. Therefore, a sharer in one period might have a different status for the next period. In other words, although user i provided files in period t $( y _ { i t } = 1 )$ , in the following period, she could be a free rider or she might not log in at all $( y _ { i t + 1 } = 0 )$ Our dependent variable, $D e c i s i o n _ { i t } ,$ , is a user’s sharing status after the period in which she shared (i.e., Decisio $\iota _ { i t } = 1$ if $y _ { i t } = 1$ and $y _ { i t + 1 } = 1$ and $D e c i s i o n _ { i t } = 0$ if $y _ { i t } = 1$ and $y _ { i t + 1 } = 0 )$ . Table 3 illustrates the definition of our data points. Each circle is a data point that corresponds to a period after the one in which the user shared.

## 4.2. Operationalization of Independent Variables

Because most of the statistics for any given user can be compiled readily using the individual activities we observed, we use $D o w n l o a d _ { i t }$ to denote the number of files downloaded by sharer i at period t (in thousands), $B r o w s e _ { i t }$ for the number of browse commands sent by sharer i at period t, and $S e a r c h _ { i t }$ for the number of search commands sent by sharer i at period t. These three variables correspond to H1A, H1B, and H1C, respectively.

To test H1D, we had to measure the individual user’s download speed. Unfortunately, we could not directly observe the delay for each download because the download is done in a P2P fashion. However, our data do capture download status queries, which a user sends to inquire about her position in the download queue while waiting to download a file from a particular sharer. We thus used the number of download status queries as an approximation of download delay $( D e l a y _ { i t } )$

Variables that capture value provided by a sharer i at period t include the total number of files downloaded from this user, denoted as $C o n t r i b u t e _ { i t } .$ Been\_browsed is the number of times other users browsed the sharer’s collection. Value ${ _ { \it u s e r } } _ { i t }$ represents the reputation of the user and is collectively determined and marked by the operators of the network based on a user’s overall sharing activities in the channel. These three variables correspond to H2A, H2B, and H2C, respectively.

Table 4 Descriptive Statistics of Key Variables<sup>a</sup>

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td> $Decision_{it}$ </td><td>3,917</td><td>0.52</td><td>0.50</td><td>0.00</td><td>1.00</td></tr><tr><td> $Download_{it}$ </td><td>3,917</td><td>0.12</td><td>0.33</td><td>0.00</td><td>5.09</td></tr><tr><td> $Browse_{it}$ </td><td>3,917</td><td>96.95</td><td>293.42</td><td>0.00</td><td>4,509.00</td></tr><tr><td> $Search_{it}$ </td><td>3,917</td><td>5.30</td><td>12.40</td><td>0.00</td><td>265.00</td></tr><tr><td> $Delay_{it}$ </td><td>3,917</td><td>17.03</td><td>132.08</td><td>0.00</td><td>5,153.00</td></tr><tr><td> $Contribute_{it}$ </td><td>3,917</td><td>0.26</td><td>0.97</td><td>0.00</td><td>19.28</td></tr><tr><td> $Been_browsed_{it}$ </td><td>3,917</td><td>0.82</td><td>26.79</td><td>0.00</td><td>1,515.00</td></tr><tr><td> $Value_user_{it}$ </td><td>3,917</td><td>0.89</td><td>0.32</td><td>0.00</td><td>1.00</td></tr><tr><td> $Sharing_history_{it}$ </td><td>3,917</td><td>19.53</td><td>24.17</td><td>1.00</td><td>130.00</td></tr><tr><td> $Files_{it}$ </td><td>3,917</td><td>4.41</td><td>8.42</td><td>0.00</td><td>120.58</td></tr><tr><td> $Queue_length_{it}$ </td><td>3,917</td><td>7.13</td><td>26.87</td><td>0.00</td><td>440.33</td></tr><tr><td> $Bandwidth_{it}$ </td><td>3,917</td><td>56.40</td><td>285.28</td><td>0.00</td><td>4,836.87</td></tr><tr><td> $Sharer_size_t$ </td><td>135</td><td>1.50</td><td>0.56</td><td>0.48</td><td>2.52</td></tr><tr><td> $Freerider_size_t$ </td><td>135</td><td>28.58</td><td>6.30</td><td>19.90</td><td>64.35</td></tr><tr><td> $Total_download_t$ </td><td>135</td><td>941.38</td><td>152.57</td><td>582.50</td><td>1,306.50</td></tr></table>

<sup>a</sup>Because of space limit, the correlation matrix of key variables is included in the supplementary Online Appendix A.

4.2.1. Control Variables. We include the following individual sharer control variables that may affect a user’s sharing decision. These variables are the number of periods since the user first shared (Sharing $\begin{array} { r } { h i s t o r y _ { i t } ) . } \end{array}$ , total number of files in a sharer’s collection list $( F i l e s _ { i t } )$ , the average length of the queue for downloading her files $( Q u e u e \_ l e n g t h _ { i t } ) .$ , and the maximal bandwidth the user allocated for other users’ download $( B a n d w i d t h _ { i t } )$ .

In addition to individual measures, a user’s decision may also be affected by the overall activities of the network, but the individual measures reflected in the independent variables may not capture all such influences. We thus incorporate the aggregate measures in the model for each time period, including the total number of sharers (Sharer\_size ), the total number of free riders (Freerider\_size ), and the total number of files downloaded by all users (Total\_download ). We use the combined downloads of sharers and free riders because sharers’ downloads are highly correlated with Sharer\_size . We note in our data that, on average, a sharer downloads five times as many files as a free rider does, and sharers in general also stay much longer in the network. Tables 2 and $4 ^ { 4 }$ present the definitions and descriptive statistics for key variables of the data sample. The correlation matrix of key variables is available in the supplementary Online Appendix A. To ensure there is no multicollinearity, we calculate the variance inflation factors (VIF) for the independent variables. There is no VIF value indicating multicollinearity concerns among the key independent variables.

4.2.2. Time Fixed Effects. Although we control for aggregate network activities, many other external factors might also affect a user’s decision to share in a given time period, such as the emergence or termination of other competing music-downloading services and any major lawsuits originating from the content owners. To further account for these factors, which are time dependent but not reflected in the aggregate network measures, we introduce time fixed effects (time periods dummy variables) for different periods. Time fixed effects control for any time-specific impact that might influence the overall network activities.

4.2.3. Individual-User Fixed Effects. In studying user behavior, we have to recognize the fact that the continued-sharing decision may also be influenced by individual intrinsic characteristics (e.g., gender, age, education, geographical location, and music preferences) that we were not able to observe. We thus include user fixed effects to account for all unobserved individual heterogeneity.

We also acknowledge that users’ preferences may change over time because of their experience in the network, and such time-variant changes cannot be fully controlled by the user fixed effects, which may lead to spurious state dependency, as discussed in Heckman (1991). However, including time fixed effects and more individual sharer control variables, as discussed above, would help with this issue.

In summary, the full regression function is

$$
\begin{array}{c} P (y _ {i t + 1} = 1 \mid y _ {i t} = 1, X _ {i t}, c _ {i}, c _ {t}) = \frac {\exp (X _ {i t} \beta + c _ {i} + c _ {t})}{1 + \exp (X _ {i t} \beta + c _ {i} + c _ {t})}, \\ i = 1, \ldots , N;   t = 1, \ldots , T, \end{array}
$$

where

$$
\begin{array}{l} X _ {i t} \beta = \beta_ {1} \cdot D o w n l o a d _ {i t} + \beta_ {2} \cdot B r o w s e _ {i t} + \beta_ {3} \cdot S e a r c h _ {i t} \\ \qquad + \beta_ {4} \cdot D e l a y _ {i t} + \beta_ {5} \cdot C o n t r i b u t e _ {i t} \\ \qquad + \beta_ {6} \cdot B e e n \_ b r o w s e d _ {i t} + \beta_ {7} \cdot V a l u e \_ u s e r _ {i t} \\ \qquad + \beta_ {8} \cdot S h a r i n g \_ h i s t o r y _ {i t} + \beta_ {9} \cdot F i l e s _ {i t} \\ \qquad + \beta_ {1 0} \cdot Q u e u e \_ l e n g t h _ {i t} + \beta_ {1 1} \cdot B a n d w i d t h _ {i t} \\ \qquad + \beta_ {1 2} \cdot S h a r e r \_ s i z e _ {t} + \beta_ {1 3} \cdot F r e e r i d e r \_ s i z e _ {t} \\ \qquad + \beta_ {1 4} \cdot T o t a l \_ d o w n l o a d _ {t} \end{array}
$$

with $c _ { i }$ as the dummy variable for the user and $c _ { t }$ as the dummy variable for the time period.

## 4.3. Biweekly Panel Data Estimation Results

Table 5 demonstrates the results of the binary logistic regression using biweekly panel data. As discussed, the dependent variable is a user’s decision to share in the following period given that she shared in the last period. The first column (Model (a)) shows regression on all individual- and aggregate-level variables without controlling for time fixed effects. Models (b1) and (b2) illustrate the results with progressive inclusion of the two sets of independent variables, with control for time fixed effects. In Model (c), user fixed effects are incorporated in addition to all other variables. Model (d) further extends Model (c) by including the interaction effects between Download and $C o n t r i b u t e _ { i t }$ and between Browse and Been\_browsed . Because the influences of the three network-level variables are captured by the time fixed effects, those variables are not included in Models (b1), (b2), (c), and (d).

The odds ratios of the estimation results for all the models are available in the supplementary Online Appendix B. Also, we calculated the marginal effects of key independent variables in Model (c). Our results show that a one standard deviation increase in variable Download leads to a 27% increase in the odds of continued sharing. Similarly, a one standard deviation increase of variables Browse $_ { i t } , S e a r c h _ { i t } , C o n t r i b u t e _ { i t } ,$ and Been\_Browsed leads to a 23%, 33%, 32%, and 47% increase in the odds of continued sharing, respectively. Becoming a value user leads to a 146% increase

All the models have similar results for the key independent variables. $D o w n l o a d _ { i t } ,$ $B r o w s e _ { i t } ,$ and $\dot { S } e a r c h _ { i t }$ are positive and significant in all models, supporting H1A, H1B, and H1C. H1D is not supported, indicating that either the delay queries are not a good estimate of actual delays, or delays do not really prevent users from continued sharing. For variables reflecting how a sharer’s content is used, Contribute , and Value ${ _ { \it u s e r } } _ { i t }$ are positive and significant in all models, supporting H2A and H2C. H2B is not supported, suggesting that frequency of being browsed does not affect a sharer’s decision. Overall, the results show that both self-use and continuous contribution provide strong incentives for users to continue sharing. The consistency of the results in the series of tests also suggests the robustness of our results.

As to the control variables, Sharing\_history has a significant effect on users’ decisions to share across all models. It is interesting that when the user fixed effects are considered, the sign changes from positive to negative. One explanation is that a specific user’s $^ { \prime \prime } \mathrm { l i f e ^ { \prime \prime } }$ in the channel is almost always finite, so that an average sharer shares fewer than four periods; thus, the longer the user has been in the channel, the more likely she is to leave. In addition, in Model (a), when aggregate network measures are included, the total

Table 5 Panel Data Binary Response Regression Results for Sharer Decision

<table><tr><td>Variable</td><td>Model (a)</td><td>Model (b1)</td><td>Model (b2)</td><td>Model (c)</td><td>Model (d)</td></tr><tr><td colspan="6">Individual activity</td></tr><tr><td> $Download_{it}$ </td><td>0.82***(0.19)</td><td>1.11***(0.19)</td><td>0.78***(0.19)</td><td>0.71***(0.27)</td><td>1.16***(0.32)</td></tr><tr><td> $Browse_{it}$ </td><td>0.0005***(0.0002)</td><td>0.0007***(0.0002)</td><td>0.0005***(0.0002)</td><td>0.0007***(0.0002)</td><td>0.0006***(0.0002)</td></tr><tr><td> $Search_{it}$ </td><td>0.02***(0.004)</td><td>0.03***(0.004)</td><td>0.02***(0.004)</td><td>0.02***(0.007)</td><td>0.02***(0.007)</td></tr><tr><td> $Delay_{it}$ </td><td>-0.0004(0.0005)</td><td>-0.0005(0.0005)</td><td>-0.0002(0.0005)</td><td>-0.0002(0.0006)</td><td>-0.0003(0.0005)</td></tr><tr><td> $Contribute_{it}$ </td><td>0.67***(0.10)</td><td></td><td>0.69***(0.10)</td><td>0.29***(0.10)</td><td>0.44***(0.12)</td></tr><tr><td> $Been_browsed_{it}$ </td><td>0.002(0.004)</td><td></td><td>0.002(0.004)</td><td>0.02(0.01)</td><td>0.02(0.02)</td></tr><tr><td> $Value_user_{it}$ </td><td>0.84***(0.13)</td><td></td><td>1.07***(0.16)</td><td>0.90***(0.23)</td><td>0.87***(0.23)</td></tr><tr><td colspan="6">Interaction terms</td></tr><tr><td> $Download_{it} \times Contribute_{it}$ </td><td></td><td></td><td></td><td></td><td>-0.37***(0.12)</td></tr><tr><td> $Browse_{it} \times Been_browsed_{it}$ </td><td></td><td></td><td></td><td></td><td>-0.00001(0.00001)</td></tr><tr><td colspan="6">Individual control</td></tr><tr><td> $Sharing_history_{it}$ </td><td>0.01***(0.001)</td><td>0.01***(0.002)</td><td>0.01***(0.002)</td><td>-0.16***(0.02)</td><td>-0.16***(0.02)</td></tr><tr><td> $Files_{it}$ </td><td>0.009*(0.005)</td><td>0.02***(0.005)</td><td>0.01**(0.005)</td><td>-0.02(0.02)</td><td>-0.02(0.02)</td></tr><tr><td> $Queue_length_{it}$ </td><td>0.00001(0.001)</td><td>0.0007(0.001)</td><td>-0.00005(0.001)</td><td>0.008**(0.003)</td><td>0.007**(0.003)</td></tr><tr><td> $Bandwidth_{it}$ </td><td>-0.00004(0.0001)</td><td>-0.0001(0.0001)</td><td>-0.00005(0.0001)</td><td>-0.0001(0.0002)</td><td>-0.0002(0.0002)</td></tr><tr><td colspan="6">Network aggregate activity</td></tr><tr><td> $Sharer_size_t$ </td><td>-0.31*** (0.09)</td><td></td><td></td><td></td><td></td></tr><tr><td> $Freerider_size_t$ </td><td>0.01* (0.008)</td><td></td><td></td><td></td><td></td></tr><tr><td> $Total_download_t$ </td><td>-0.0005* (0.0003)</td><td></td><td></td><td></td><td></td></tr><tr><td>Time Fixed Effects</td><td></td><td>Included</td><td>Included</td><td>Included</td><td>Included</td></tr><tr><td>User Fixed Effects</td><td></td><td></td><td></td><td>Included</td><td>Included</td></tr><tr><td>Constant</td><td>-0.67N = 3,917</td><td>-0.33N = 3,917</td><td>-1.28N = 3,917</td><td>-0.21N = 3,123</td><td>-0.36N = 3,123</td></tr><tr><td>Log likelihood =</td><td>-2,485.28</td><td>-2,445.68</td><td>-2,378.90</td><td>-1,596.91</td><td>-1,592.71</td></tr></table>

Notes. In Models (c) and (d), 794 observations were dropped because of prediction successes and failures. Because of space limitations, odds ratio results are included in the supplementary Online Appendix B.  
<sup>∗∗∗</sup>p < 00011 <sup>∗∗</sup>p < 00051 <sup>∗</sup>p < 0010, standard errors in parentheses.

number of files downloaded (Total\_download ) has a significantly negative effect on the sharers’ decision to continue sharing. This finding confirms the negative network effects observed by Asvanund et al. (2004) when a large amount of downloading activity takes place in a P2P network. Interestingly, Sharer\_size is also negative and significant, which may be due to the large amount of content the sharers themselves download. Freerider\_size is positive and significant, which perhaps can be attributed to the audience effect that free riders provide because the IDs of all loggedin users, as well as the number of sharers and free riders, are visible to all participants in the network. In other words, everything else being equal, the more free riders there are, the larger the audience there is for the sharer’s content, and the more likely she will continue sharing.

We have also tested random data samples of various sizes (500 and 3,000 sharers), and all generate fairly consistent results (with the same sign and significance) as those shown in Table 5. Moreover, with the two-week time window, we implicitly assume that a sharer’s decision in the next period is only affected by her experience in the past two weeks. To test how a different user memory affects the result, we constructed one-week, four-week, and ten-week data samples to estimate our empirical models, and we obtained qualitatively similar results (i.e., all the signs and significance of the major independent variables are the same).<sup>6</sup>

In addition, we tested our models using robust standard errors, and the detailed results are presented in the supplementary Online Appendix E. Almost all results (in terms of standard errors and significance level) for models (a)–(d) remain very similar to the original model, except the reduced significance level of Download (from 1% to 5%) and Search (from 1% to 10%) in models (c) and (d), which further validate the robustness of our results.<sup>7</sup>

We can also evaluate the relative importance of the “getting-from” and “giving-to” forces by comparing the two pairs of variables that capture the same activities from opposite directions: Download (files the sharer downloaded from others) and Contribute (files downloaded by others); Browse (browses of others) and Been\_browsed (browses by others). In Table 5, Model (c), we can see that Browse is significant, but Been\_browsed is insignificant. Note the unit for Browse is 1, whereas for other variables, such as Download and Contribute it is thousands (Table 2). Moreover, we find that Download has a greater effect on the dependent variable than Contribute . (Results are not included because of space constraints, but are available upon request.) Findings show that, overall, “getting-from” is a stronger force for the continuedsharing decision than “giving-to.”

We also tested Model (d) in Table 5 to see whether the effect of Download is dependent on Contribute , or whether the effect of Browse is dependent on Been\_browsed . The result shows that the more a sharer contributes (i.e., is downloaded by others), the less effect downloads have on her continued-sharing decision. On the other hand, the interaction term between Browse and Been\_browsed is not significant. We follow the method developed by Ai and Norton (2003) to compute the marginal effect in the logistic model for the two interaction terms, and arrive at qualitatively similar conclusions, as shown in Table 5.

## 5. Discussion, Limitations, and Future Research

The goal of the study is to investigate why users continuously contribute to P2P networks. Our results provide support for both “getting-from” benefits and “giving-to” benefits as explanations. Our findings suggest that in a P2P network, both the user’s benefits received from the network and the value the user provides to the network are significant predictors of her continued contribution. Moreover, “gettingfrom” benefits dominate “giving-to” benefits in all the aggregate models when we take into account aggregate network variables, time fixed effects, and user fixed effects. This finding provides an extension to existing research on voluntary contribution in conversation-based communities, where much of the incentive to contribute lies in the social context and interaction in the conversations users have (Constant et al. 1996, Wasko and Faraj 2005). What is interesting about our results is that when there is very little social context (i.e., no social interaction and full anonymity), the incentives from how much the focal user gains (reciprocity) and how much others benefit from the focal user’s contribution (impure altruism) still remain strong enough to keep users sharing.

Our findings generate a few important managerial implications for P2P network operators. First, the key finding is that users getting what they want from the network, not what they receive in return for their contribution, sustains contribution to the network. This finding indicates that the key to network growth is the continuous addition of new and fresh content for users. Second, showing more statistics to make a user’s use of the network more visible to him or her will help the user continue sharing. Third, adding more features to show how a user’s contribution is used by others will have a similar positive impact. Recognition and visual representation of users’ contributions to the network, even if they are as simple as displaying how their contribution is used and valued by other members, can be quite effective in motivating a user’s continued contribution.

Our results also have implications for contentsharing communities, such as YouTube and Flickr. Recall that there are two stages in public-goods development: the creation/production stage, and the distribution/maintenance stage. Therefore, there are two categories of costs in providing an online public good, whether media or conversation based—one cost category associated with each stage. For online goods, the maintenance cost (i.e., the costs of making the content available over a period of time) is not trivial and often higher than the production cost. Compared to these content-sharing communities, in P2P there are additional costs of distribution and maintenance borne by users, which may give them more incentive to “gain” from the network to offset their costs. In other words, in other content-sharing communities that entail a lower cost, users do not need to gain as much to continue sharing. Therefore, they are more likely to continue sharing than in P2P. Similarly, even though the cost of creating or producing what is being shared (i.e., music files) is close to zero, the cost of being caught and sued (for piracy) makes users wish to “give” less to such a community compared to users of conversation-based communities. Therefore, users are more likely to continue sharing in other contentsharing communities than in P2P.

A unique aspect of our research is the individual activity data set, which allows us to observe individual experiences and actions and therefore enables us to study users’ individual and dynamic decisions. Because the data set was logged using a continuously running program, it has the advantage of being nonbiased compared to survey-based data, which are often used in research on online communities. Also, because the data set captures all user activities during the data collection period, it is also more complete than probing-based data collection, which is often employed in P2P file-sharing research (e.g., Asvanund et al. 2004). To ensure the validity and robustness of our results, we used several techniques, including varying the length of the time window definition, adding aggregate network variables to control for network status and other individual user variables to control for user heterogeneity, and testing a fixedeffects model to control for the influence of time and other unobserved user heterogeneities.

Note that our research does have several limitations. One limitation is that we cannot observe users’ demographic information or information about their activities in other sharing networks, among other nonobservable external factors. Although we control for the influences of such factors in our model, we do not explicitly identify them individually or test them. In future research, a more behavioral approach can be undertaken to understand their effects. Another limitation is that some statistics we devised may not be the best measures of the intended variables. For example, we used the number of delay queries as the measure of the quality of the user’s experience, assuming the more queries a user sends, the worse her experience. This assumption might not be necessarily true, because some people are less patient than others and would send more such query commands in general.

In addition, even though we incorporate individual-user fixed effects to control for cross-sectional differences in user benefits of file sharing, by doing so we implicitly assume that such benefits remain constant over time. However, one might argue that user net benefits of file sharing can change over time, and they are likely to be correlated with downloads and sharing. In that respect, our results for Contribute and Been\_browsed can be regarded as more compelling than the results for Download and Browse, because the former are exogenous to the user.

For future research, we plan to investigate the content of the music being shared and how the files are propagated in the network. The result will shed light not only on online music sharing, but also on knowledge diffusion in P2P networks. We can also match the music shared in IRC with offline and other legitimate online sales data to see how pirated music demand and supply compare with those in the legal channels. The results may be helpful both to record companies and to copyright holders seeking to design a method to thwart illegal file sharing.

## Electronic Companion

An electronic companion to this paper is available as part of the online version that can be found at http://isr.journal .informs.org/.

## References

Adar, E., B. A. Huberman. 2000. Freeriding on gnutella. First Monday 5. Retrieved on February 17, 2011, http://firstmonday .org/htbin/cgiwrap/bin/ojs/index.php/fm/article/viewArticle/ 792/701.

Ai, C., E. C. Norton. 2003. Interaction terms in logit and probit models. Econom. Lett. 80 123–129.

Andreoni, J. 1989. Giving with impure altruism: Applications to charity and ricardian equivalence. J. Political Econom. 97 1447–1458.

Andreoni, J. 1990. Impure altruism and donations to public goods: A theory of warm-glow giving. Econom. J. 100 464–477.

Asvanund, A., K. Clay, R. Krishnan, M. D. Smith. 2004. An empirical analysis of network externalities in peer-to-peer music sharing networks. Inform. Systems Res. 15(2) 155–174.

Butler, B., L. Sproull, S. Kiesler, R. Kraut. 2007. Community effort in online groups: Who does the work and why? S. Weisband, L. Atwater, eds. Leadership at a Distance. Lawrence Erlbaum, Mahwah, NJ.

Connolly, T., B. K. Thorn. 1990. Discretionary data bases: Theory, data and implications. J. Fulk, C. W. Steinfield, eds. Organizations and Communication Technology. Sage, Newbury Park, CA, 219–234.

Constant, D., L. Sproull, S. Kiesler. 1996. The kindness of strangers: Usefulness of electronic weak ties for technical advice. Organ. Sci. 7(2) 119–135.

Cornes, R., T. Sandler. 1984. Easy riders, joint production, and public goods. Econom. J. 94 580–598.

Cornes, R., T. Sandler. 1994. The comparative static properties of the impure public good model. J. Public Econom. 54 403–421.

Ekeh, P. P. 1974. Social Exchange Theory: The Two Traditions. Harvard University Press, Cambridge, MA.

Emerson, R. M. 1972. Exchange theory, Part I: A psychological basis for social exchange. J. Berger, M. Zelditch, B. Anderson, eds. Sociological Theories in Progress. Vol. 2. Houghton-Mifflin, Boston, 38–57.

Emerson, R. M. 1976. Social exchange theory. Ann. Rev. Sociol. 2 335–362.

Fayard, A.-L., G. DeSanctis. 2005. Evolution of an online forum for knowledge management professionals: A language game analysis. J. Computer-Mediated Comm. 10(4) Article 2. http://onlinelibrary.wiley.com/doi/10.1111/j.1083-6101 .2005.tb00265.x/full.

Golle, P., K. Leyton-Brown, I. Mironov, M. Lillibridge. 2001. Incentives for sharing in peer-to-peer networks. Proc. 3rd ACM Conf. Electronic Commerce, October 14–17, Tampa, FL, 264–267.

Haythornthwaite, C. 2005. Social networks and Internet connectivity effects. Inform. Comm. Soc. 8(2) 125–147.

Heckman. J. J. 1991. Identifying the hand of past: Distinguishing state dependence from heterogeneity. Amer. Econom. Rev. 81(2) 75–79.

Herring, S. C. 2004. Computer-mediated discourse analysis: An approach to researching online behavior. S. A. Barab, R. Kling, J. S. Gray, eds. Designing for Virtual Communities in the Service of Learning. Cambridge University Press, Cambridge, 338–376.

Huang, C., J. Li, K. W. Ross. 2007. Can Internet video-on-demand be profitable? Proc. ACM SIGCOMM’07, Association for Computing Machinery, New York.

Jian, L., J. McKie-Mason. 2006. Why share in peer-to-peer networks? Proc. ACM EC 2006 Workshop Econom. Networked Systems, Association for Computing Machinery, New York.

Kollock, P. 1999. The economies of online cooperation: Gifts and public goods in cyberspace. M. A. Smith, P. Kollock, eds. Communities in Cyberspace. Routledge, London, 220–239.

Krishnan, R., M. D. Smith, Z. Tang, R. Telang. 2004. The virtual commons: Why free-riding can be tolerated in file sharing networks. Working paper, Purdue University, West Lafayette, IN.

Ma, M., R. Agarwal. 2007. Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Inform. Systems Res. 18(1) 42–67.

Mas-Colell, A., M. D. Whinston, J. R. Green. 1995. Microeconomic Theory. Oxford University Press, New York.

Monge, P. R., J. Fulk, M. E. Kalman, A. J. Flanagin, C. Parnassa, S. Rumsey. 1998. Production of collective action in alliancebased interorganizational communication and information systems. Organ. Sci. 9 411–433.

Peddibhotla, N., M. Subramani. 2007. Contributing to public document repositories: A critical mass theory perspective. Organ. Stud. 28(3) 327–346.

Pioch, N. 1997. A short IRC primer. Retrieved on April 21, 2010. http://www.irchelp.org/irchelp/ircprimer.html.

Ranganathan, K., M. Ripeanu, A. Sarin, I. Foster. 2003. To share or not to share: An analysis of incentives to contribute in collaborative file sharing environments. Workshop on Economics of Peer-to-Peer Systems, University of California, Berkeley.

Rheingold, H. 1994. A slice of life in my virtual community. L. M. Harasim, ed. Global Networks: Computers and International Communication. MIT Press, Cambridge, MA, 57–80.

Rodgers, S., Q. Chen. 2005. Internet community group participation: Psychosocial benefits for women with breast cancer. J. Comput. Mediated Comm. 10(4) Article 5. http://onlinelibrary .wiley.com/doi/10.1111/j.1083-6101.2005.tb00268.x/full.

Saroiu, S., P. K. Gummadi, S. D. Gribble. 2002. A measurement study on peer-to-peer file sharing systems. Proc. Multimedia Comput. Networking (MMCN’02), San Jose, CA. Retrieved on February 18, 2011, http://www.merit.unu.edu/ publications/rmpdf/2001/rm2001-022.pdf.

Shmanske, S. 1991. Public Goods, Mixed Goods, and Monopolistic Competition. Texas A&M University Press, College Station, TX.

Spears, R., M. Lea. 1992. Social influence and the influence of the “social” in computer-mediated communication. M. Lea, ed. Contexts Comput.-Mediated Comm. Harvester Wheatsheaf, London, 30–65.

Walczuch, R., M. Verkuijlen, B. Geus, U. Ronnen. 2001. Stickiness of commercial virtual communities. MERIT-Infonomics Res. Memorandum Ser. 8(22).

Walther, J. B. 1992. Interpersonal effects in computer-mediated interaction: A relational perspective. Comm. Res. 19(1) 52–90.

Walther, J. B., C. L. Slovacek, L. C. Tidwell. 2001. Is a picture worth a thousand words? Comm. Res. 28(1) 105–134.

Wasko, M. M., S. Faraj. 2000. “It is what one does”: Why people participate and help others in electronic communities of practice. J. Strategic Inform. Systems 9 155–173.

Wasko, M. M., S. Faraj. 2005. Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quart. 29(1) 35–57.

Wellman, B., M. Gulia. 1999. Net surfers don’t ride alone: Virtual communities as communities. M. Smith, P. Kollock, eds. Communities in Cyberspace. Routledge, London, 167–194.

Wingfield, N., E. Smith. 2003. Crowded house: With the Web shaking up music, a free-for-all in online songs. Wall Street Journal (November 19) A1.

Wooldridge, J. M. 2002. Econometric Analysis of Cross Section and Panel Data. The MIT Press, Cambridge, MA.

Yamagishi, T., K. S. Cook. 1993. Generalized exchange and social dilemmas. Soc. Psych. Quart. 56(4) 235–248.
