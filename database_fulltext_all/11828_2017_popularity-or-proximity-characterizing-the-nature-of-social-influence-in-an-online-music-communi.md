---
otero_id: 11828
otero_key: "XZKDFY72"
title: "Popularity or Proximity: Characterizing the Nature of Social Influence in an Online Music Community"
authors: "Sanjeev Dewan; Yi-Jen (Ian) Ho; Jui Ramaprasad"
year: "2017"
journal: "Information Systems Research"
doi: "10.1287/isre.2016.0654"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/XZKDFY72/fulltext/images/bdfd238c4512242edda92762003dd34af91bbd30cd6f6f80f5d6e5be0015ec1f.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Popularity or Proximity: Characterizing the Nature of Social Influence in an Online Music Community

Sanjeev Dewan, Yi-Jen (Ian) Ho, Jui Ramaprasad

To cite this article:

Sanjeev Dewan, Yi-Jen (Ian) Ho, Jui Ramaprasad (2017) Popularity or Proximity: Characterizing the Nature of Social Influence in an Online Music Community. Information Systems Research

Published online in Articles in Advance 24 Feb 2017

http://dx.doi.org/10.1287/isre.2016.0654

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/XZKDFY72/fulltext/images/05fac83fdb4975398da588855f22e34fe5ce66e0006faeb4915674e5201de6ca.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Popularity or Proximity: Characterizing the Nature of Social Influence in an Online Music Community

Sanjeev Dewan,<sup>a</sup> Yi-Jen (Ian) Ho,<sup>b</sup> Jui Ramaprasad<sup>c</sup>

<sup>a</sup> Paul Merage School of Business, University of California, Irvine, Irvine, California 92697; <sup>b</sup> Smeal College of Business, Pennsylvania State University, University Park, Pennsylvania 16802; <sup>c</sup> Desautels School of Management, McGill University, Montréal, Québec H3A 1G5, Canada

Contact: sdewan@uci.edu (SD); ian.ho@psu.edu (Y-JIH); jui.ramaprasad@mcgill.ca (JR)

Received: November 13, 2013 Revised: January 15, 2015; September 14, 2015; November 24, 2015 Accepted: November 29, 2015 Published Online in Articles in Advance: February 24, 2017

https://doi.org/10.1287/isre.2016.0654

Copyright: © 2017 INFORMS

Abstract. We study social influence in an online music community. In this community, users can listen to and “favorite” (or like) songs and follow the favoriting behavior of their social network friends—and the community as a whole. From an individual user’s perspective, two types of information on peer consumption are salient for each song: total number of favorites by the community as a whole and favoriting by their social network friends. Correspondingly, we study two types of social influence: popularity influence, driven by the total number of favorites from the community as a whole, and proximity influence, due to the favoriting behavior of immediate social network friends. Our quasiexperimental research design applies a variety of empirical methods to highly granular data from an online music community. Our analysis finds robust evidence of both popularity and proximity influence. Furthermore, popularity influence is more important for narrow-appeal music compared to broad-appeal music. Finally, the two types of influence are substitutes for one another, and proximity influence, when available, dominates the efect of popularity influence. We discuss implications for design and marketing strategies for online communities, such as the one studied in this paper.

History: Anindya Ghose, Senior Editor; Ming Fan, Associate Editor.

Keywords: social influence • word of mouth • popularity • proximity • social networks • music industry • online community

## 1. Introduction

Social or peer influence has long been recognized as a driver of adoption and consumption decisions, going back to Katz and Lazarsfeld (1955), Arndt (1967), and Bandura (1971), but its importance has only been heightened recently with the proliferation of online social media and social networks (see, e.g., Godes et al. 2005, Brown et al. 2007, Chen et al. 2011, Aral and Walker 2011). In the music industry, the context we study here, social media have made sharing of consumption choices, tastes, and preferences easier than ever before, and in a recent survey, 54% of subjects indicated that they base their music purchasing decisions on positive recommendations from friends (Nielsen Company 2012a). Per Nielsen’s Global Trust in Advertising Survey (Nielsen Company 2012b), 92% of consumers say that recommendations from people they know are the most trusted sources of information when making consumption decisions, followed by 70% of consumers who say that they trust consumer opinions posted online.

Despite this anecdotal evidence, we do not really know whether it is aggregate popularity information that matters, or information about consumption by friends in close social proximity, or both. We expect information about peer consumption to influence the choice of music by users. In fact, there are two types of influence, one driven by aggregate peer consumption information and the other by music consumption in social network proximity. Our analysis covers both types of influence, where we call the efect of information on total favorites popularity influence and the efect of information on friends’ favoriting behavior proximity influence. Our study is designed to measure each type of influence as well as the interaction between the two. Specifically, our research questions are as follows: How does popularity influence afect music consumption choices? Is it more important for mainstream or niche music? How important is proximity influence in music consumption? What is the nature of interaction between the two types of influence? Are they complements or substitutes?

Recently, the role of social influence on consumer choices has been examined in a variety of contexts, such as movie sales (Moretti 2011), Facebook applications (Aral and Walker 2011), adoption of the iPhone 3G (De Matos et al. 2014), restaurant dining choices (Cai et al. 2009), software downloads (Duan et al. 2009), and music subscription services (Bapna and Umyarov 2015). In this paper, we study the role of peer influence on consumption in an online music community—an MP3 blog aggregator—where users can listen to songs drawn from a large number of MP3 blogs. As a result of features introduced on the website over time, users can listen to songs, favorite them, and use social networking features to follow other users and track their favoriting behavior. The site provides the total number of favorites garnered by each song listed on the site and allows users to quickly look up which songs have been favorited by their “friends,” allowing us to study both popularity and proximity influence. Prior work has looked at popularity influence (e.g., Chevalier and Mayzlin 2006; Dewan and Ramaprasad 2012, 2014; Chen et al. 2011) and proximity influence (e.g., Ma et al. 2010, Egebark and Ekstrom 2011) individually, but has not studied them jointly in the same context, as we do here. Furthermore, we are able to exploit exogenous feature implementations on the website that allow us to identify the two types of influence in a quasi-experimental framework.

The music context is ideal for the study of information technology (IT)-enabled social influence, for a number of reasons. First, music is an experience good, so consumers potentially value the opinions and actions of other consumers as signals of whether or not they would like the music themselves. Second, music is an information good, where discovery and consumption are increasingly becoming online activities, and in our case, these two activities occur on the very same website. Finally, the music industry has been transformed by technology and social networks in profound ways, so that understanding social influence in this context will foreshadow what we can expect for other information and experience goods, such as movies, software, and other digital media.

It is important to discuss the unit of social interaction in our setting, which is “favorite,” akin to the “like” action on Facebook. Users can favorite songs and they can also favorite other users, giving them visibility into their friends’ favoriting behavior. These two types of favoriting actions are illustrated in Figure 1. A directed arrow connecting two user nodes indicates that the first user has favorited the second; e.g., user A is following users B, C, and D.<sup>1</sup> The figure also shows which users have favorited each of the two songs 1 and 2. Thus, users can view two types of information for any song posted on the website, total favorites and friends’ favorites, corresponding to what we call popularity influence and proximity influence, respectively.

Online social influence mediated by popularity or proximity has diferent implications for website design and marketing strategies. If proximity influence is important (as in the studies of De Matos et al. 2014, Aral and Walker 2011), then the website should incentivize the creation of social ties, provide visibility of social connections and actions, and encourage interaction and coconsumption. On the other hand, if popularity influence is important (as in Chen et al. 2011, Duan et al. 2009), then it would be a good idea to emphasize popularity statistics, for the overall population and also for subpopulations, based on demographics, listening preferences, etc. It might also make sense to provide information on multiple dimensions of popularity, such as the number of times a song has been listened to, saved to a playlist, or “liked.” The popularity information could also combine internal and external (e.g., best seller lists or rankings) measures that are relevant to the online community in question. Finally, the interaction between the two types of influence also matters. If the two are substitutes, then it would be important to understand which type of influence is more important for diferent types of users and music, so that the appropriate type of signal is prioritized, depending on the situation. If the two types of influence are complements, then strategies to amplify the efect of one type of influence with the other might be useful. In general, design and marketing strategies need to be linked to the types of social influence that are relevant to the context, as well as their interaction. Also, as users spend increasing amounts of time on their mobile devices, the ability to prioritize and operationalize social influence mechanisms within a limited screen real estate is becoming increasingly important. These are the issues that broadly motivate this study.

Figure 1. Illustrating Popularity and Proximity Social Interactions  
![](/api/attachments/XZKDFY72/fulltext/images/f9c73cfbb607e1a88372671da076220143572090b7ed2f48c78ceaa31300e831.jpg)

To study popularity influence, we exploit a natural experiment enabled by a newly implemented feature in an online music community, The Hype Machine (THM).<sup>2</sup> The popularity feature, illustrated in the screenshot of Figure 2, allowed users to observe all other users’ music favoriting behavior in the aggregate, albeit anonymously. The feature was implemented on

Figure 2. (Color online) Popularity Feature on Hype Machine  
![](/api/attachments/XZKDFY72/fulltext/images/edf564104285afa2d946c962d145aaeebfba0c939fe34710e69195690318adc9.jpg)

# The Dø - Keep Your Lips Sealed Club Cheval Remix

INDIE FEMALE VOCALIST FOLK FRENCH INDIE POP

![](/api/attachments/XZKDFY72/fulltext/images/e4593ea02f513d035aa237e630d519a8cba5645b374de64a8868eb00c6cbd7d0.jpg)  
Popularity Feature

Posted by 5 blogs · Download: Amazon • iTunes

Earbuddy + "When you hear a remix this good, it's hard to keep your lips sealed. The

French-Finnish duo The Dø's single,..." Posted on Dec 28th, 2014 →

October 1, 2008. We deploy a diference-in-diferences (DD) methodology to measure the impact of aggregate favorite data on other users’ consumption decisions. After our analysis of popularity influence, we focus on proximity or social network influence. We deploy a variety of approaches to identify and measure proximity influence, including probit and hazard models, building on the work of Aral et al. (2009). Identifying proximity influence using observational data is challenging due to homophily, which may influence both the formation of social ties and music consumption decisions. To overcome the potential selection bias due to homophily, we use two matching techniques, propensity score matching (PSM) and Euclidean distance matching (EDM), as we explain in more detail in Section 4.2.1. Finally, we develop a combined model to jointly estimate both types of influence using a twodimensional quasi-experimental design including both popularity and proximity treatments.

To summarize our results, we find strong and robust evidence for popularity influence. Our diference-indiferences results confirm that being able to observe aggregate popularity information does have a causal impact on subsequent consumption choices. We further find that popularity influence is significant only for newly posted songs (because of the specific nature of the site), and it is more important for narrow-appeal music compared to broad-appeal music, in line with the findings of Tucker and Zhang (2011). We also find consistent evidence of proximity influence, after accounting for homophily. Finally, our results suggest that popularity and proximity influence are substitutes for one another. Popularity influence is most efective when proximity influence is not available, either because the user is not connected to other social network users or none of a user’s friends have favorited a song. Proximity influence, when available, tends to dominate popularity influence. We discuss the implications of these findings in Section 6.

The rest of this paper is organized as follows. Section 2 provides a brief summary of related literature. Sections 3 and 4 present our data and describe our empirical methodologies. Our results are presented in Section 5, and we discuss our findings and provide some concluding remarks in Section 6.

## 2. Literature Review

This paper draws from two main streams of work: literature examining word-of-mouth (WOM) and observational learning (OL) efects, and a second stream focused on studying influence in social networks. The first stream consists of studies that look at how individuals make decisions based on aggregate information on the preferences and actions of other peer customers—which we collectively call popularity influence. The second stream of literature examines the role that social network ties play on individual consumption decisions, what we call proximity influence. Below, we provide a brief review of the prior work that informs our analysis of each type of influence, starting with popularity influence.

## 2.1. Popularity Influence

It has long been recognized that consumers tend to be influenced by social interactions with other consumers, even without knowing them or their consumption intent. As noted by Chen et al. (2011), there are two distinct types of social interactions mediated by armslength interaction and information exchange between consumers. The first type of social interaction hinges on consumer preferences and opinions and has been labeled word-of-mouth in the marketing literature, going back to Arndt (1967). The second type of social interaction is driven by the actions and decisions of other consumers and is termed observational learning in the psychology and economics literatures (Bandura 1971, Bikhchandani et al. 1998). The importance of these types of social interactions has grown in the online arena and has been the subject of considerable research interest, as we briefly summarize below.

Starting with research on online WOM, studies have examined the impact of both the volume (amount of information) and valence (net positive or negative opinion) of WOM in product review and reputation systems. The general conclusion is that volume and valence of WOM both afect product sales, though in some contexts valence is more important than volume (e.g., Mizerski 1982, Chevalier and Mayzlin 2006), while in others volume matters relatively more (e.g., Liu 2006) because of increased awareness and number of informed consumers in the marketplace. Other research has also examined the impact of product, review, and reviewer characteristics, and a sampling of the interesting findings include that online reviews are more important for niche as opposed to popular books (Chen et al. 2008), negative reviews are more influential than positive reviews (Chevalier and Mayzlin 2006), featured reviews are more influential than nonfeatured reviews (Forman et al. 2008), and consumers not only use summary statistics and star ratings but also pay attention to the actual text of the reviews (Ghose and Ipeirotis 2011).

Observational learning is the process by which consumers make decisions based on aggregate consumption statistics of prior users. Whether or not the knowledge of aggregate consumption decisions has an efect on subsequent individual consumption has been examined in prior work in the context of books (Sorenson 2007), software adoption (Duan et al. 2009), and online music (Salganik et al. 2006). More recently, Chen et al. (2011) looked at the efect of OL in the presence of WOM efects, based on Amazon.com data, and found that not only do OL and WOM individually drive purchase decisions, but the interaction between the two processes is significant as well.

In our setting, the number of favorites for a song indicates how many users have favorited a song, so it is a measure of the volume of WOM. However, it is not known how many users listened to the song but did not favorite it, so we only have partial information on the valence of WOM. Furthermore, in the absence of listening statistics, comparing the number of favorites across songs is an imperfect signal of which songs were listened to more than others,<sup>3</sup> which has the flavor of OL. We can conclude that the number of favorites is a hybrid of WOM and OL, and conveys both volume and valence, though neither perfectly. Despite its limitations, such a metric of social interaction is increasingly prevalent in online social media, most notably on Facebook and Twitter. Prior research has investigated the correlation between this type of social interaction and product sales and product quality. Specifically, Lee and Lee (2011) and Li and Wu (2013) find a positive impact of Facebook likes on the sale of Groupon vouchers. Moreover, Schöndienst et al. (2012) and Wang and Chang (2013) show that total number of likes result in a higher level of perceived product quality. We add to this literature by examining the relationship between this “liking” information and consumption choices in an online music community.

## 2.2. Proximity Influence

Social network influence is due to social proximity (contact and communication) between social network “friends.” Brown and Reingen (1987) was one of the first studies to look at these “microlevel” interactions and how information spreads over ties in a social network in the ofline world. Valente (1995) studies so-called “relational models of difusion” and discusses the role of specific types of people as network neighbors, arguing that an “individual’s direct contacts influence his or her decision to adopt or not adopt an innovation.” Factors such as opinion leadership (Katz and Lazarsfeld 1955) and the strength of ties (Granovetter 1973) are also related to influence and adoption.

When studying how social proximity afects actors’ behaviors, a key challenge is to be able to separate social influence and homophily, where the latter refers to social correlation in actions due to the fact that people tend to befriend others who have similar tastes and preferences (e.g., Manski 1993). It is a challenge to distinguish real social network influence from correlated efects in that as observers, we do not know if two individuals who are socially tied to one another make the same adoption decision because they have the same taste, or because they were exposed to the same external “shock” at the same time (e.g., an advertisement), or because one influenced the other. Without knowing the social network structure, this reflection problem—where we cannot separate out the efect of the individual on the group from the efect of the group on the individual—does hinder the identification of the endogenous efects. Fortunately, we have data on the underlying social network structure and highly granular data on music consumption and favoriting behavior, which helps mitigate the identification issues stemming from the reflection problem. Such data are not often available.

There have been a variety of methods applied to find evidence of social network influence. Ma et al. (2010) construct a hierarchical Bayesian model to study the efects of peer influence and homophily on both the timing and choice of consumer purchases within a social network. Aral and Walker (2011) design a randomized experiment on Facebook for quantifying social network influence. Tucker (2008), De Matos et al. (2014), and Lu et al. (2012) apply the intransitive triads instrumental variable approach to separate social influence from homophily. More recently, Belo and Ferreira (2016) used a randomization approach via the shufle test of Anagnostopoulos et al. (2008). By randomizing the timing of individuals’ actions, they concluded that social network influence has both positive and negative efects on the difusion of telecom-related products.

The method that we find most useful here is the one by Aral et al. (2009), who develop a propensity-score matching estimation framework to separate social influence from homophily. Briefly, they examine adoption of a mobile service application in an instant messaging social network. The key issue that motivates their analysis is that correlated behavior in product adoption, in the form of either assortative mixing (adopters tend to have adopter friends) or temporal clustering (a user adopts soon after a friend adopts), could be driven by both influence and homophily. Recall, peer-to-peer influence refers to the process by which a user causes their network friends to make similar choices, whereas homophily is the process by which similarities across network neighbors results in correlated choices—which could mimic contagion without any causal influence. As Aral et al. (2009) explain, homophily causes a selection bias because treatments are not randomly assigned—adopters are more likely to be treated because of similarity with their network neighbors. They show that propensity score matching helps to overcome this selection bias by linking up observations across the treatment and control groups with the same likelihood of treatment. We adopt a similar matched sample approach to identify proximity influence and use probit and hazard models to estimate the magnitude of the influence.

## 2.3. Social Influence in the Music Industry

For the reasons mentioned in Section 1, there is great emerging interest in the role of IT-enabled social influence in the music industry. New music is arriving to the marketplace at a growing pace, and the growing long tail nature of the music market (i.e., increased consumption of niche music relative to mainstream music) is increasing the importance of social media in the process of music discovery and consumption. Accordingly, a number of studies have recently examined the impact of social media on music consumption. For example, Dewan and Ramaprasad (2012) studied the impact of music blogging on online sampling and found that observational learning efects are stronger in the tail relative to the body of music sales distribution. Dhar and Chang (2009) found that the volume of user-generated content is predictive of music sales. Dewan and Ramaprasad (2014) studied the interaction among social media (blog buzz), traditional media (radio play), and music sales and found that while blog buzz is positively related to album sales, it is negatively related to song sales, possibly due to the sales displacement efect of free online sampling. Using a randomized field experiment, Bapna and Umyarov (2015) found that peer influence exists in the difusion of premium subscriptions in the online music community Last.fm.

In a study with objectives similar to ours, Salganik et al. (2006) looked at the impact of aggregate prior consumption decisions on the ultimate inequality and unpredictability in an artificial music market. They found that social influence due to observation of prior aggregate consumption decisions “contributes both to inequality and unpredictability in cultural markets,” (p. 855) providing evidence that “collective behavior”

plays a part in consumption decisions. The main difference between the study by Salganik et al. (2006) and our study is that while the prior work created an artificial music market where individuals were not explicitly socially tied to one another, ours is based on real observational data from an online community where individuals are socially tied to one another. Furthermore, we examine both popularity influence and proximity influence, whereas the prior study was restricted to just the observational learning component of popularity influence.

## 3. Data

We use a unique data set provided by the online music community, The Hype Machine. The Hype Machine is the leading music blog aggregator, aggregating MP3s that are posted in their entirety on thousands of music blogs.<sup>4</sup> THM allows users to create an account, stream (but not download) songs that are posted (by clicking on the “listen” link), and favorite songs and users. On October 1, 2008, THM implemented a popularity feature by adding a number next to each track indicating how many users of the site had favorited the song. While individuals could favorite songs prior to this, the number of favorites for a song was not viewable by any other visitors to the site until the implementation of this feature. Figure 2 shows a screenshot of this popularity feature indicating that 242 Hype Machine members favorited the song “Keep Your Lips Sealed.” To measure the efect of popularity influence on music listening, we have obtained data on user behavior from before and after THM made this popularity information visible, providing an opportunity for a natural experiment.

THM also allows members to create a social network using a personal dashboard, to which they can add favorite tracks and favorite users. The act of “favoriting” a person is akin to following another user on Twitter in that it creates a unidirectional tie (as shown in Figure 1), which is not necessarily reciprocated. Figure 3 provides a screenshot of this feature, showing that this particular user has two favorite tracks and one favorite user. To construct the social network of users and measure proximity influence, we have obtained time-stamped data on members’ user favoriting behavior.

To estimate popularity and proximity influence, we use a detailed data set that allows us to observe the entire history of users’ listening and favoriting behaviors. THM has provided daily listen logs for September and October of 2008. These listen logs record each time any user listens to a song, along with the user ID and the details of the song, such as the artist, song title, and a posted time stamp. In addition, we have a separate data set that contains the time-stamped log of members’ favoriting of other users, which we use to construct a member’s social network, as well as song favoriting behavior. Finally, we have supplemented the data from THM with data on song characteristics collected from Amazon (sales rank) and the Echo Nest (e.g., genre, artist popularity).

Figure 3. (Color online) Proximity Feature on Hype Machine  
![](/api/attachments/XZKDFY72/fulltext/images/e267c0aea59f129f70c57d878dabec4c1bfb795e37934cf6cd99ff6315c9a10f.jpg)

## 4. Empirical Methodology

In this section, we discuss the models we use to quantify popularity and proximity influence, including one that jointly estimates both influences in the same empirical model. Notation and variable descriptions are summarized in Table 1.

## 4.1. Model of Popularity Influence

For estimating popularity influence, we employ a DD methodology (see, e.g., Card and Krueger 1994), exploiting the feature implementation in HM on October 1, 2008, that provided visibility of the total number of song favorites.<sup>5</sup> Given that the implementation of this feature is exogenous, as we discuss below, the DD model allows us to reliably measure the impact of the visibility of popularity information on music consumption. We compare a set of songs that experienced the implementation (the treatment group) to a set of songs that did not (the control group). Specifically, we define the songs posted on September 29, 2008, as the treatment group and the songs posted one week earlier, on September 22, 2008, as the control group. The latter group of songs, the group posted on September 22, 2008, was not afected by the feature implementation during the time period we examine. Figure 4 illustrates our DD experimental design, where $\mathbf { \tilde { \Gamma } } _ { T _ { 1 } } = \mathbf { \mathrm { O c t o b e r } }$ 1, 2008, is the date of treatment (implementation of the popularity feature on HM) for the treatment group. Even though there was no such intervention for the control group, we create a dummy treatment event for the control group on $T _ { 0 } { = } \mathrm { S e p t e m b e r } 2 4 ,$ one week prior to the feature implementation. Similar to the event study literature in finance, we use a short estimation window (<sup>±</sup>1 day) to isolate the efect of the feature implementation on listening behavior.<sup>6</sup>

Ideally, the treatment and control groups should contain songs posted on the same date, with identical potential treatment dates. We are unable to construct coincident treatment and control groups, however, because all songs on the website were subject to the feature implementation at the same time—either all songs were treated or none were, depending on whether the date in question is before or after the date of feature implementation, respectively. It is for this reason that the treatment and control groups in our DD design include songs posted one week apart (exactly one week apart to avoid day-of-week diferences). The time separation of the treatment and control groups is a cause for concern, however, because time shocks at diferent points in time could afect treatment and control groups diferently, confounding the measurement of treatment efects. We believe, however, that this is not a serious concern, for the following reasons.

Table 1. Variable Descriptions

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td> $Listens_{jt}$ </td><td>Popularity influenceTotal number of times song j has been listened to at time t</td></tr><tr><td> $PopTreatment_{j}$ </td><td>Dummy variable, equal to 1 if song j is treated (i.e., song j&#x27;s total number of favorites are visible)</td></tr><tr><td> $After_{t}$ </td><td>Dummy variable, equal to 1 if time period t after the popularity treatment (i.e., after 10/1)</td></tr><tr><td> $Listen_{ij}$ </td><td>Proximity influenceDummy variable, equal to 1 if user i has listened to song j</td></tr><tr><td> $ProxTreatment_{ij}$ </td><td>Dummy variable, equal to 1 if user i has a friend who favored song j in the burn-in period</td></tr><tr><td> $Friends_{+}$ </td><td>Total number of users that user i is following</td></tr><tr><td colspan="2"> $Joint model for popularity and proximity influence</td></tr><tr><td>\( Listen_{gjt}$ </td><td>Total number of times song j has been listened to at time t by group g.</td></tr><tr><td> $PopTreatment_{j}$ </td><td>Dummy variable, equal to 1 if song j is treated (i.e., song j&#x27;s total number of favorites are visible)</td></tr><tr><td> $After_{t}$ </td><td>Dummy variable, equal to 1 if time period t is any day after the popularity treatment (i.e., after 10/1)</td></tr><tr><td> $ProxTreatment_{gj}$ </td><td>Dummy variable, equal to 1 if user i (in group g) has a friend who favored song j in the burn-in period</td></tr><tr><td colspan="2">Control variables</td></tr><tr><td> $PreFavorites_{j}$ </td><td>Total number of favorites of song j before the observation window of the study</td></tr><tr><td> $SalesRank_{j}$ </td><td>Sales rank of song j at Amazon.com</td></tr><tr><td> $Genre_{j}$ </td><td>Genre of song j</td></tr></table>

Figure 4. Diference-in-Diferences Experimental Design for Popularity Influence  
![](/api/attachments/XZKDFY72/fulltext/images/69de3895cd6fae6ce1357928c71a1ba72ff4383713519c4bf4baf1742b3ceb72.jpg)

First, even though the samples are one week apart, the listening patterns are virtually identical, as shown in Figure 5. We graph the total number of listens in each hour of the pretreatment period, $T _ { 1 } - 1$ and $T _ { 0 } - 1$ for the treatment and control groups, respectively, and show that they follow almost exactly the same pattern. This consistent pattern of listening behavior across the treatment and control dates provides us some assurance that there were no time-varying shocks that diferentially afected the listening behavior of songs across the treatment and control groups. Second, the time of posting of a song on THM is exogenous, because it is synchronized with the posting of the song on the original MP3 blog, rather than a decision made by THM. Furthermore, the THM website did not publicize the fact that the favoriting feature was imminent, so MP3 blogs could not have anticipated the feature implementation. Third, the songs in the treatment and control groups are similar in terms of genre and popularity. To further increase the similarity of the samples, as we discuss in Section 5, we use coarsened exact matching (CEM) to match individual songs in the treatment and control groups on a one-to-one basis to make sure that the samples are balanced and the songs are similar to each other.<sup>7</sup> As we will see in Section $5 ,$ the results for the matched and unmatched samples are qualitatively similar. Still, we include treatment dummies in all of our DD specifications to absorb any systematic diferences in listen frequency between the treatment and control groups.

Figure 5. Distribution of Listens for Diference-in-Diferences Treatment and Control Subsamples  
![](/api/attachments/XZKDFY72/fulltext/images/f36ef9854757ea8066ff74c51ecdc7f29a2109d5a93fa127e032c2921c34db31.jpg)

Fourth, we find that our treatment and control samples satisfy the key identifying assumption of diference-in-diferences estimation, which is that the treatment and control groups have a common trend in the absence of treatment (Meyer 1995). (See Figure 4 for the importance of a common trend for being able to measure the average treatment efect.) This test is typically operationalized by comparing the trend in the dependent variable over the pretreatment period, across the treatment and control samples (Card and Krueger 1994, Danaher et al. 2014). In our case, the general trend is one of declining listens over time, as songs move of the front page of the site and lose novelty over time. Because the songs are posted at different times on the posting dates (September 22 and September 29 for the control and treatment samples, respectively) we characterize the pretreatment trend by the diference in the average number of listens over the second 12-hour window and the first 12-hour window after posting: we expect this diference to be negative. Figure 6 displays the distribution of this diference measure (labeled “diference of listens”) for the control and treatment subsamples, along with a table of summary statistics and diference tests below the graphs. As shown in the figure, the distributions are virtually identical, with both the diference of means t-test and the Kolmogorov–Smirnov test for equality of distributions being insignificant. This supports the assumption of a common pretreatment trend for the treatment and control samples.

Finally, we conduct a variety of robustness checks (described in Section 5) with alternate treatment and control groups, drawn from diferent points in time, to show that the results are not sensitive to exactly when the songs are posted to THM. Overall, we believe that picking the treatment and control groups one week apart does not compromise the integrity of the diference-in-diferences design. On the contrary, our design assures that treatment is exogenous, overcoming a major challenge in conventional diferencein-diferences models. Indeed, our research design illuminates a practical approach for a quasi-experimental investigation of online feature implementations or policy changes that afect an entire community or website starting at a given point in time.

For us to measure the impact of popularity information, songs in the data set must have had the opportunity to accumulate favorites, so we allow for an initial “burn-in period,” from the time a song is posted on HM to one day prior to the treatment date. This requires us to look at the sample of songs posted two days prior to the treatment date to have a pre-treatment period. Then, the days $T _ { 1 } - 1$ and $T _ { 0 } - 1$ are the pretreatment periods for the treatment and control group, respectively, while $T _ { 1 } + 1$ and $T _ { 0 } + 1$ are the corresponding post-treatment periods. Accordingly, our DD model specification is as follows, for song j on day t:

$$
\begin{array}{c} \log (l i s t e n s _ {j t}) = \beta_ {0} + \beta_ {1}   P o p T r e a t m e n t _ {j} + \beta_ {2}   A f t e r _ {t} \\ \qquad + \beta_ {3} \log (P r e F a v o r i t e s _ {j}) \\ \qquad + \beta_ {4}   P o p T r e a t m e n t _ {j} \times A f t e r _ {t} + \varepsilon_ {j t}, \end{array}\tag{1}
$$

where $L i s t e n s _ { j t }$ denotes the total number of listens of song j on day t. The regression covers the time periods running from one day before the feature implementation to one day after, for the treatment and control groups; i.e., $t \in \{ \dot { T } _ { 0 } - 1 , T _ { 0 } + 1 , T _ { 1 } - 1 , T _ { 1 } + 1 \}$ . The variable PopTreatment is a dummy variable indicating whether song j is in the treatment group $( P o p T r e a t m e n t _ { i } = 1 )$ or control group (PopTreatmen $t _ { j } = 0 ) . A f t e r _ { t }$ is a dummy variable indicating whether the date t is the posttreatment period $\bar { ( } A f t e r _ { t } = 1 )$ or pretreatment period $( A f t e r _ { t } = 0 )$ . The control variable PreFavorites<sub>j</sub> is the number of favorites at the start of the pretreatment period. The $P o p T r e a t m e n t _ { j } \times A f t e r _ { t }$ interaction term characterizes the magnitude of popularity influence. We use ordinary least squares (OLS) to estimate the regression.

Figure 6. Comparison of Pretreatment Trends for Treatment and Control Samples for the Popularity Influence Model  
![](/api/attachments/XZKDFY72/fulltext/images/dd35fdc03a77b63b55afd52c18e5e98abcf9d368360708ce5dcef95f058a3af0.jpg)

![](/api/attachments/XZKDFY72/fulltext/images/e2e7db3691ab6c86cf28536af7a9d63caa4af6e7133694d8f292fc2a6fc70d96.jpg)

<table><tr><td></td><td>Control group</td><td>Treatment group</td></tr><tr><td>Mean</td><td>-30.2202</td><td>-29.2315</td></tr><tr><td>Std. dev.</td><td>28.2601</td><td>26.8050</td></tr><tr><td>T test p-value</td><td colspan="2">0.5294</td></tr><tr><td>KS p-value</td><td colspan="2">0.5664</td></tr></table>

## 4.2. Models for Proximity Influence

Turning to our models to measure proximity influence, we focus on how favoriting a song by a focal user impacts the listening behavior of her social ties. Following prior social network research, distilling social network influence from other drivers of correlation in behavior, such as homophily, is at the heart of our proximity influence analysis. We estimate a probit model and a hazard model, corresponding to how the probability of listening to a song and the time to first listen, respectively, are afected by the favoriting behavior of friends in social network proximity. To conduct this analysis we follow Aral et al. (2009) and use propensity score matching to control for potential homophily. Before specifying our proximity models, we first describe our PSM procedure.

4.2.1. Propensity Score Matching. For a given song, the treatment group consists of those users that have at least one friend who has favorited that song. The goal of PSM in our analyses is to match every user in the treatment group with a user in the control group (none of whose friends has favorited the song) who is homophilous to the user in the treatment group in terms of tastes, calculated based on the users’ observable characteristics, and number of friends. In our case, we do not have data on consumer demographics and other characteristics, but we do observe perhaps the most relevant characteristic of all—actual song listening behavior. Much as a recommender system finds nearest neighbors (e.g., Adomavicius and Tuzhilin 2005), we find matches between the treatment and control group based on the relative song listening profiles of users. From the data on listening history of users, over the three-week period September 1–21, 2008, we construct a profile of each user on HM. These profiles are constructed using data on over 80,000 songs, for which we collected supplemental data on genre and various measures of artist popularity from the Echo Nest (the.echonest.com).<sup>8</sup>

For each user–song pair, we constructed a weight based on the number of times the user listened to that particular song as a fraction of the number of overall listens for that user. We then created a weighted average of each song characteristic in a vector of 28 song characteristics based on all of the songs that the user had listened to. The result of this allowed us to summarize a user’s profile by a series of numbers (the weighted averages of song characteristics), each representing the user’s taste toward a specific music characteristic. We then used these profiles to match each user in the treatment group to a user in the control group, using PSM as follows. Each song in our treatment and control groups was assigned a positive probability of being in the treatment group based on a logit model incorporating the characteristics of the users as characterized by their listening history as well as the number of friends they have. To ensure overlap in the treatment group and control group, we constrained the group of matched observations to be within 0.1 propensity score of each other $( \mathrm { i . e . , C a l i p e r = 0 . 1 ) }$ . After finding a match for each user in the treatment group, we examined the distribution of propensity scores to ensure similarity between the treatment and control groups as advised by Lechner (2002). Looking at Figure $^ { 7 , }$ we see that the distributions of the propensity scores in both the treatment group and control group are almost identical to one another. Specifically, the box plot shows that the two groups are well matched on the minimum, maximum, and median as well as the first and third quartiles shown in the figure. The details of the PSM procedure are provided in the appendix.

As a robustness check, we also implemented a matching procedure at the user–song level, using Euclidean distance matching. For each song, this procedure matches each user in the treatment group (i.e., users that have at least one friend who has favorited the song) with a similar user (based on song listening profiles) in the control group who has a high likelihood of having a friend that might have favorited the song. In this case, matching was based on minimizing the Euclidean distance between the song profile and friends’ song listening profiles. The details of this matching procedure are also described in the appendix. The trade-of between PSM and EDM is that while PSM maximizes the control for homophily (by matching on user characteristics), EDM maximizes the likelihood of treatment (i.e., having a friend that has favorited the song, by matching at the user–song level) for the matching member in the control group. We estimate proximity influence by using both PSM and EDM, and comparing each to random matching, as we discuss in Section 5.2.

Figure 7. Distribution of Propensity Scores After Matching  
![](/api/attachments/XZKDFY72/fulltext/images/38bbc1b5628faa856efdbc6033448a7fa3b902e3c10a98c5d7554861789a28db.jpg)  
Note. The box plots display the minimum, maximum, median, and first and third quartiles of the propensity scores distribution.

4.2.2. Probit Model of Proximity Influence. To examine the impact of proximity influence on the likelihood of listening to a song, while controlling for other song characteristics, we implement a binary probit model. To do this, we look at songs posted on September 22 and allow a 48-hour burn-in period after the time of song posting so that songs can acquire favorites. After this burn-in period, we track the users’ listening choices for the following seven days to estimate the probit model; that is, we use a two-day burnin period followed by a seven-day observation window for all of our proximity influence analyses. Using the matched treatment (ProxTreatment <sup></sup> 1) and control groups (ProxTreatment <sup></sup> 0) under random matching and either PSM or EDM, combined with the song characteristics data, we estimate the following probit model:

$$
\begin{array}{r l} & {\operatorname * {P r} (L i s t e n _ {i j} = 1)} \\ & {\quad = \beta_ {0} + \beta_ {1} P r o x T r e a t m e n t _ {i j}} \\ & {\qquad + \beta_ {2} \log (P r e F a v o r i t e s _ {j}) + G e n r e _ {j} + \varepsilon_ {i j},} \end{array}\tag{2}
$$

where $\boldsymbol { L i s t e n _ { i j } }$ is a binary outcome indicating whether user i listened to song j or not. The variable Prox-Treatmen $t _ { i j }$ is a dummy variable that captures the treatment of proximity influence; i.e., ProxTreatmen $t _ { i j } = 1$ indicates that user i has at least one friend who has favorited song $j ,$ while ProxTreatmen ${ \bf \ell } _ { i j } = 0$ indicates that user i has no friend who has favorited song j. We also include song-level controls PreFavorites (for overall popularity of the song on HM) and Genre . The coefficient $\beta _ { 1 }$ is the coeficient of interest and it captures the impact of proximity influence on a focal user’s listen decision. To isolate proximity influence from homophily, we compare the estimate of $\beta _ { 1 }$ under random matching with both PSM and EDM.

4.2.3. Hazard Model of Proximity Influence. Last, we investigate proximity influence by looking at the time to a user’s first listen to a song. We apply a hazard model to estimate the impact of proximity influence on the duration of time before user i first listens to song j. Similar to the probit model above, the hazard model compares the matched treatment and control groups. Similar to the probit model described in Section 4.2.2, we again use a seven-day observation window after the 48-hour burn-in period after song j was posted. We track user i until she listens to song j. If user i did not listen to song j within the observation window of seven days, we right-censor the observation. Specifically, the hazard rate, $\lambda _ { i j } ,$ follows an exponential distribution<sup>9</sup> and is related to the covariates of interest using the following simple parametric model:

$$
\begin{array}{c} \log (\lambda_ {i j}) = \beta_ {0} + \beta_ {1} P r o x T r e a t m e n t _ {i j} \\ + \beta_ {2} \log (P r e F a v o r i t e s _ {j}) + G e n r e _ {j} + \varepsilon_ {i j}, \end{array}\tag{3}
$$

where $\lambda _ { i j }$ is the hazard rate defined by whether and when user i listened to song j. Similarly, ProxTreatmen $t _ { i j }$ is a dummy variable coding the treatment and control groups, and $\beta _ { 1 }$ is our coeficient of interest. The variables PreFavorites and Genre are song-level controls included in the regression. As before, we estimate the hazard model under random matching, compared with both PSM and EDM.

## 4.3. Combined Model for Popularity and Proximity Influence

To jointly estimate popularity and proximity influence, we need a model that can simultaneously capture the impact of the visibility of popularity information and friends’ favorites on user listen decisions. We extend the DD model of Section 4.1 to a diference-in-diference-in-diferences (DDD) specification by adding a proximity influence treatment; that is, the DDD model is a two-dimensional treatment model, including both popularity treatment (represented by the PopTreatment indicator variable) and proximity influence treatment (represented by the ProxTreatment dummy variable). The third dimension in the DDD model is represented by the dummy variable $A f t e r _ { t } ,$ which indicates whether the time period t in question is the pretreatment period (for popularity influence) or the posttreatment period.

The DDD design has the songs posted on September 29, 2008, as the popularity treatment group (PopTreatment <sup></sup> 1) and the songs posted on September 22, 2008, as the popularity control group (Pop-Treatment <sup></sup> 0). On the other dimension, ProxTreatment divides users into two groups, where ProxTreatment <sup></sup> 1 indicates users in the proximity treatment group that have at least one friend who has favorited song $j ,$ and ProxTreatment <sup></sup> 0 indicates users in the proximity control group that do not have any friends who has favorited song $j .$ Users in the two proximity groups are matched by both random matching and propensity score matching (we do not use EDM here). Accordingly, our DDD model specification is as follows:

$$
\begin{array}{l} \log (L i s t e n _ {g j t}) \\ = \beta_ {0} + \beta_ {1} P o p T r e a t m e n t _ {j} + \beta_ {2} A f t e r _ {t} + \beta_ {3} P r o x T r e a t m e n t _ {g j} \\ \quad + \beta_ {4} P o p T r e a t m e n t _ {j} \times A f t e r _ {t} \\ \quad + \beta_ {5} P o p T r e a t m e n t _ {j} \times P r o x T r e a t m e n t _ {g j} \\ \quad + \beta_ {6} A f t e r _ {t} \times P r o x T r e a t m e n t _ {g j} \\ \quad + \beta_ {7} P o p T r e a t m e n t _ {j} \times A f t e r _ {t} \times P r o x T r e a t m e n t _ {g j} \\ \quad + \beta_ {8} \log (P r e F a v o r i t e s _ {j}) + \beta_ {9} G e n r e _ {j} + \varepsilon_ {i j t}, \end{array} \tag {4}
$$

where $g$ is the index of proximity treatment (0 or 1), and $L i s t e n _ { g j t }$ denotes the total number of listens of proximity treatment type g of song j at time t, where $\bar { t } \in \{ T _ { 0 } - \bar { 1 } , T _ { 0 } + 1 , T _ { 1 } - \bar { 1 , } T _ { 1 } + 1 \}$ . The variables PopTreatment and $P r o x T r e a t m e n t _ { g j }$ are dummy variables for whether an observation is in the treatment or control group for popularity and proximity treatment, respectively. The dummy $A f t e r _ { t }$ identifies whether the date t corresponds to the pretreatment or posttreatment for popularity. The coeficients $\beta _ { 3 }$ represents the magnitude of proximity influence, $\beta _ { 5 }$ captures the magnitude of popularity impact, and the coeficient on the three-way interaction term $\beta _ { 7 }$ characterizes the nature of interaction between popularity and proximity influence $( \beta _ { 7 } > 0$ would indicate that the interaction is complementary, while $\beta _ { 7 } < 0$ would indicate that the interaction is one of substitutes). Equation (4) is estimated using OLS.

## 4.4. Descriptive Statistics

We start by providing descriptive statistics and correlations for the data set used for estimating popularity influence (Tables 2 and 3) followed by those for proximity influence (Tables 4 and 5). The key dependent variable in estimating popularity influence is the total number of times a song is listened to on a given day $( L i s t e n s _ { j t } )$ . Table 2 summarizes songs in the treatment and control group on the pretreatment and posttreatment days. Overall, there are roughly 600 songs in both the treatment and control groups. On average, there were 47.54 listens per song per day on THM, with a standard deviation of 171.56. Some songs posted on THM did not get any listens, but the maximum number of listens in a day for a song was 3,836. While users listen to a variety of songs, they appear to be more selective in their favoriting behavior (PreFavorites ). On average, songs receive 1.33 favorites per day with a standard deviation of 3.46. Again, some songs do not receive any favorites, while the maximum number of favorites for a given song in our data set was 57. The pairwise correlations (Table 3) indicate that listening and favoriting are significantly and strongly correlated with one another $( \breve { 0 } . 7 1 , p < \breve { 0 } . 0 1 )$ and Amazon sales rank of a song is negatively correlated with both the number of listens and number of favorites. This is expected as a higher sales rank corresponds to less popular songs.

Table 2. Descriptive Statistics for Popularity Influence

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td> $Listens_{jt}$ </td><td>2,382</td><td>47.5369</td><td>171.5553</td><td>0</td><td>3,836</td></tr><tr><td> $Prefavorites_j$ </td><td>2,382</td><td>1.3283</td><td>3.4622</td><td>0</td><td>57</td></tr><tr><td> $SalesRank_j$ </td><td>2,382</td><td>2,983,163</td><td>3,643,284</td><td>605</td><td>6,856,013</td></tr></table>

Table 3. Correlations Among Variables for Popularity Influence

<table><tr><td></td><td> $Listens_{jt}$ </td><td> $PreFavorites_{jt}$ </td><td> $SalesRank_j$ </td></tr><tr><td> $Listens_{jt}$ </td><td>1</td><td></td><td></td></tr><tr><td> $PreFavorites_j$ </td><td>0.706***(0.000)</td><td>1</td><td></td></tr><tr><td> $SalesRank_j$ </td><td>-0.129***(0.000)</td><td>-0.165***(0.000)</td><td>1</td></tr></table>

Note. Standard errors are in parentheses.  
<sup>∗∗∗</sup> p < 0.01.

Table 4. Descriptive Statistics for Proximity Influence

<table><tr><td>Variable</td><td>N</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td> $Listen_{ij}$ </td><td>159,583</td><td>0.0057</td><td>0.0754</td><td>0</td><td>1</td></tr><tr><td> $ProxTreatment_{ij}$ </td><td>159,583</td><td>0.0015</td><td>0.0392</td><td>0</td><td>1</td></tr><tr><td> $Prefavorites_j$ </td><td>159,583</td><td>4.7096</td><td>9.2960</td><td>0</td><td>88</td></tr><tr><td> $SalesRank_j$ </td><td>159,583</td><td>3,925,858</td><td>4,297,366</td><td>1,233</td><td>6,508,732</td></tr><tr><td> $OutDegree_i$ </td><td>159,583</td><td>2.7868</td><td>3.6763</td><td>1</td><td>62</td></tr></table>

We now turn to the summary statistics for the relevant variables for the proximity influence analysis (Table 4), which summarize data for a weeklong observation window from September 22, 2008, until September 29, 2008. Overall, we have a pool of over 800 users and roughly 200 songs to create the user–song pairs used in this analysis. From Table 4, we see that the average likelihood of a user listening to an individual song is quite low, 0.0057 (0.57%), with a standard deviation of 0.0754. The likelihood that a user’s friend has favorited a given song is even lower (as expected), 0.0015 (0.15%), with a standard deviation of 0.0392. These summary statistics demonstrate the sparseness of the data, making it challenging to estimate proximity influence. The number of total favorites of the average song is approximately 4.71, with a standard deviation of 9.30, and the Amazon sales rank is 3.9 million, with a standard deviation of 4.3 million.<sup>10</sup> Turning to the pairwise correlations (Table 5), we see the expected correlations—a positive and significant (though low in magnitude) correlation between ProxTreatment and Listen, as well as between PreFavorites and Listen. We also see a negative correlation, as expected, between SalesRank and ProxTreatment, PreFavorites, and Listen. Generally, the correlations are relatively low and again reflect the sparseness of social correlations.

## 5. Results

We present our results in the following order: (i) popularity influence, (ii) proximity influence, and finally (iii) joint estimation of popularity and proximity influence.

Table 5. Correlations Among Variables for Proximity Influence

<table><tr><td></td><td> $Listen_{ij}$ </td><td> $ProxTreatment_{ij}$ </td><td> $PreFavorites_j$ </td><td> $SalesRank_j$ </td><td> $OutDegree_i$ </td></tr><tr><td> $Listen_{ij}$ </td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td> $ProxTreatment_{ij}$ </td><td>0.027***(0.000)</td><td>1</td><td></td><td></td><td></td></tr><tr><td> $PreFavorites_j$ </td><td>0.100***(0.000)</td><td>0.057***(0.000)</td><td>1</td><td></td><td></td></tr><tr><td> $SalesRank_j$ </td><td>-0.021***(0.000)</td><td>-0.002(0.503)</td><td>-0.223***(0.000)</td><td>1</td><td></td></tr><tr><td> $OutDegree_i$ </td><td>-0.008***(0.001)</td><td>0.041***(0.000)</td><td>-0.001(0.618)</td><td>0.001(0.745)</td><td>1</td></tr></table>

Note. Standard errors are in parentheses. <sup>∗∗∗</sup> p < 0.01.

## 5.1. Popularity Influence

Our results for the DD model (Equation (1)) of popularity influence are presented in Table 6, where the dependent variable is log<sup>(</sup>Listens<sup>)</sup>. Recall, the treatment sample is the set of songs posted on September 29, 2008, while the control sample consists of the songs posted one week earlier, on September 22, 2008. In model 1, we consider all of the songs in both samples and do not restrict the control group to match the songs in the treatment group. In model 2, the songs in the control sample are matched with songs in the treatment group, following the matching procedure described in Endnote 7. Model 3 is restricted to “isolates,” that is, users who are not connected to others in the social network. This is an interesting group of users to study because it is subject solely to popularity influence and

Table 6. Diference-in-Diferences Results for Popularity Influence

<table><tr><td>DV:  $\log(Listens_{jt})$ </td><td>1 Unmatched</td><td>2 Matched</td><td>3 Matched, isolates</td><td>4 Matched, unique listens</td></tr><tr><td>Constant</td><td>5.099***(0.143)</td><td>5.338***(0.197)</td><td>2.010***(0.192)</td><td>1.929***(0.182)</td></tr><tr><td> $PopTreatment_j$ </td><td>-0.078(0.054)</td><td>-0.107*(0.065)</td><td>-0.219***(0.067)</td><td>-0.193***(0.062)</td></tr><tr><td> $After_t$ </td><td>-2.199***(0.054)</td><td>-2.339***(0.064)</td><td>-0.729***(0.067)</td><td>-0.771***(0.061)</td></tr><tr><td> $PopTreatment_j \times After_t$ </td><td>0.127*(0.076)</td><td>0.180**(0.090)</td><td>0.301***(0.094)</td><td>0.292***(0.087)</td></tr><tr><td> $\log(PreFavorites_j)$ </td><td>0.943***(0.032)</td><td>0.707***(0.050)</td><td>0.476***(0.045)</td><td>0.421***(0.042)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.648</td><td>0.679</td><td>0.319</td><td>0.326</td></tr><tr><td>N</td><td>2,382</td><td>1,448</td><td>752</td><td>824</td></tr></table>

Notes. The first model does not match the control sample to the treatment sample of songs, while the second model matches the samples, as explained in Section 4. The third model uses the number of unique listens as the dependent variable. All models include genre fixed efects and log of Amazon sales rank as additional control variables. Standard errors are in parentheses.

$$
^ {*} p <   0. 1 0; ^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

no proximity influence. Finally, in model 4, the dependent variable is the number of unique listens. This case is interesting to consider because it is possible that popularity influence is restricted to the first listen of a song, rather than subsequent repeat listens of the same song. All models include genre fixed efects and logarithm of Amazon sales rank as control variables. We discuss the results of all four models together.

The PopTreatment variable has a negative sign, and it is significant in models 2–4, indicating that the songs in the treatment have fewer listens, on average, than the songs in the control sample, all else being equal. Therefore, it is a good idea to include the PopTreatment dummy variable to absorb such systematic differences across the two samples. The After variable is negative and significant, in all models, due to the tendency of the number of listens to naturally decay over time. This may be because the novelty of newly introduced songs wears of over time or because songs get “buried” below newer songs added to the site. The control variable log<sup>(</sup>PreFavorites<sup>)</sup> has the expected positive sign, reflecting the fact that more popular songs (as captured by the favoriting behavior of users on HM) get more listens on average.

The key variable of interest is the interaction term PopTreatment <sup>×</sup> After, which captures the average efect of the treatment on the number of listens, after the availability of song popularity information on the website. This interaction term is estimated to be positive, with varying degrees of significance in the three models. Interestingly, the magnitude and significance of the interaction term are highest in models 3 and 4, consistent with the notion that popularity influence is strongest for isolates (users with no friends) and for the first listen of a song, as opposed to repeat listens. Overall, we find strong evidence of a causal link between the disclosure of song popularity information (in the form of the number of song favorites) and the number of user listens.

We can quantify the economic significance of popularity influence as follows. The estimate of the interaction term PopTreatment <sup>×</sup> After is 0.18 in our main baseline model, which is model 2 in Table 6. Since the dependent variable is the logarithm of Listens, the magnitude of the interaction term implies that the availability of popularity information, after the corresponding feature implementation, increases the total listens of the average song by approximately 19.7% <sup>(</sup>exp<sup>(</sup>0.18<sup>)</sup> <sup></sup> 1.197<sup>)</sup>. Given that the mean number of listens of the average song on the posttreatment date October 2 is 9.511, this implies that the availability of popularity information increases total listens of the average song by almost two. Thus, popularity influence is not only statistically significant; it is an economically significant efect as well.

Table 7. Robustness of Popularity Influence Results to Alternative Treatment/Control Scenarios

<table><tr><td>DV:  $\log(Listens_{jt})$ </td><td>109/29 vs. 09/15</td><td>209/29 vs. 10/06</td><td>310/06 vs. 09/22</td><td>409/22 vs. 09/15</td><td>510/06 vs. 10/13</td></tr><tr><td>Constant</td><td>1.573***(0.041)</td><td>1.830***(0.050)</td><td>1.468***(0.039)</td><td>1.617***(0.051)</td><td>1.749***(0.043)</td></tr><tr><td> $PopTreatment_j$ </td><td>-0.254***(0.053)</td><td>-0.499***(0.058)</td><td>0.354***(0.063)</td><td>-0.155**(0.070)</td><td>0.143**(0.058)</td></tr><tr><td> $After_t$ </td><td>-0.905***(0.055)</td><td>-0.696***(0.068)</td><td>-0.905***(0.053)</td><td>-0.944***(0.074)</td><td>-0.683***(0.056)</td></tr><tr><td> $PopTreatment_j \times After_t$ </td><td>0.245***(0.075)</td><td>-0.041(0.082)</td><td>0.206**(0.089)</td><td>-0.026(0.101)</td><td>0.009(0.082)</td></tr><tr><td> $\log(PreFavorites_j)$ </td><td>1.243***(0.030)</td><td>1.208***(0.029)</td><td>1.225***(0.039)</td><td>1.131***(0.078)</td><td>1.086***(0.026)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.366</td><td>0.446</td><td>0.433</td><td>0.364</td><td>0.487</td></tr><tr><td>No. of observations</td><td>3,438</td><td>2,744</td><td>2,608</td><td>3,302</td><td>1,968</td></tr></table>

Notes. Each date corresponds to when the songs were added to HM. In each column, the sample corresponding to the first date is taken to be the treatment group, while the sample for the second date is the control group. Standard errors are in parentheses.  
<sup>∗∗</sup> p < 0.05; <sup>∗∗∗</sup> p < 0.01.

For additional robustness, Table 7 considers alternative definitions of the treatment versus control samples, to make sure that the results are not driven by the specific dates we picked in our baseline results. In model 1, the control group is taken to be songs posted two weeks prior to the treatment group, i.e., September 15 versus September 29 (in Table 6 the control group corresponds to songs posted one week prior). The PopTreatment <sup>×</sup> After term is positive and significant, consistent with our baseline results of Table 6. In model 2, the treatment and control groups are both after popularity information is available, so as expected, the interaction term is not significant. Model 3 has the same control group as model 1, but the treatment group is moved one week later to October 6, and we can see that the qualitative nature of the results are unchanged. In model 4, both treatment and control are before the popularity feature implementation, so as expected, the interaction term is insignificant. Finally, in model 5, both samples are drawn after the feature implementation, and again the interaction term is not significant, as expected. Overall, we can conclude that the DD results are robust, and there are no “secular”

efects in diferent weeks, validating our DD research design with the treatment and control samples drawn from neighboring weeks.

To get a sense of the economic significance of popularity influence for narrow-appeal music, note that the coeficient estimate for the PopTreatment <sup>×</sup> After interaction term is 0.18 in model 1. That translates to an increase in listens by 19.7% per song per day. Given that the average number of listens per song per day for this subsample on the posttreatment date is 5.695, this means that the availability of popularity information increases average listens per song per day to 6.817. With an average of 800 songs posted per day, this translates into an increase of almost 1,000 listens, on average.

In Table 8 we examine the diferential impact of song popularity information for broad- versus narrowappeal songs, motivated by the work of Tucker and Zhang (2011). We characterize broad versus narrow appeal using two approaches. The first is based on the Amazon sales rank of the song, wherein songs with Amazon sales rank less than 130,000 (the top 20th percentile) are considered broad appeal, while songs with sales rank higher than 130,000 are considered narrow appeal. For robustness, we also consider subsamples using 60,000 (the top 15th percentile) as the cutof. Our second approach for distinguishing between broadand narrow-appeal music is based on genre. Specifically, we include pop, rap, hip-hop, dance, and rhythm and blues (R&B) in the broad-appeal category, while the niche genres include folk, country, classical, and the various types of rock music. Looking at the results in Table 8, we find that the signs and significance of the control variables are consistent with our baseline results of Table 6. As for the key PopTreatment <sup>×</sup> After interaction term, we find that they are positive in sign, but significant only for the narrow-appeal song samples. This is consistent with the theory and findings of Tucker and Zhang (2011), in that popularity influence is more important for narrow-appeal music compared to broad-appeal music.

Table 8. Examining Diferential Popularity Influence for Broad- vs. Narrow-Appeal Music

<table><tr><td rowspan="2">DV:  $\log(Listens_{jt})$ </td><td colspan="2">1Amazon sales rank</td><td colspan="2">2Amazon sales rank</td><td colspan="2">3Genre</td></tr><tr><td>&lt;130,000</td><td>&gt;130,000</td><td>&lt;60,000</td><td>&gt;60,000</td><td>Mainstream</td><td>Niche</td></tr><tr><td>Constant</td><td>4.723***(0.851)</td><td>5.400***(0.280)</td><td>4.338***(1.238)</td><td>5.394***(0.247)</td><td>4.702***(0.313)</td><td>5.801(0.248)</td></tr><tr><td> $PopTreatment_j$ </td><td>0.064(0.227)</td><td>-0.129**(0.066)</td><td>0.116(0.302)</td><td>-0.120*(0.065)</td><td>0.010(0.115)</td><td>-0.152*(0.078)</td></tr><tr><td> $After_t$ </td><td>-1.828(0.219)</td><td>-2.409***(0.065)</td><td>-1.542***(0.288)</td><td>-2.400***(0.065)</td><td>-2.257***(0.118)</td><td>-2.370***(0.076)</td></tr><tr><td> $PopTreatment_j \times After_t$ </td><td>0.197(0.311)</td><td>0.180**(0.092)</td><td>-0.099(0.407)</td><td>0.202**(0.092)</td><td>0.080(0.161)</td><td>0.220**(0.109)</td></tr><tr><td> $\log(PreFavorites_j)$ </td><td>0.621(0.134)</td><td>0.694***(0.055)</td><td>0.771***(0.163)</td><td>0.689***(0.054)</td><td>0.753***(0.079)</td><td>0.667***(0.065)</td></tr><tr><td> $\log(SalesRank_j)$ </td><td>-0.091(0.076)</td><td>-0.156***(0.019)</td><td>-0.083(0.120)</td><td>-0.154***(0.016)</td><td>-0.100***(0.021)</td><td>-0.182***(0.016)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.529</td><td>0.694</td><td>0.485</td><td>0.068</td><td>0.684</td><td>0.676</td></tr><tr><td>N</td><td>174</td><td>1,274</td><td>104</td><td>1,344</td><td>432</td><td>1,016</td></tr></table>

Notes. All regressions are for matched treatment and control samples, as explained in Section 4. The mainstream genres on Hype Machine include pop, rap and hip-hop, dance, and R&B, while the niche genres on Hype Machine include the rock genres, folk, country, and classical. Standard errors are in parentheses. The model estimated here is model 2 from Table 6 (matched treatment and control samples), the main model we will use throughout our remaining analyses. $^ { * } p < 0 . 1 0 ; ^ { * * } p < 0 . 0 5 ; ^ { * * * } p < 0 . 0 1 .$

## 5.2. Proximity Influence

We now turn to our results for proximity influence, where the analyses are conducted at the user–song level. As a preliminary step, we first compare the number of users in the treated group who listen to the song $( n _ { + } )$ and the number of users in the control group who listen to the song (n−), based on the matched sample adoption ratio analysis of Aral et al. (2009). If having a friend who has favorited a song results in more listens, then the ratio $n _ { + } / n _ { - }$ would be greater than one. Furthermore, the magnitude of the $n _ { + } / n _ { - }$ ratio should reduce when going from random matching to propensity score matching, because random matching reflects both homophily and proximity influence, whereas PSM eliminates the efect of homophily (Aral et al. 2009). We use the treatment and control groups as constructed by the PSM method described in Section 5.1 and compare the $n _ { + } / n$ − ratio of the PSMmatched sample to the ratio of the random-matched sample.

Table 9. Estimating Proximity Influence Using Listen Ratios

<table><tr><td></td><td>Random matching</td><td>Propensity score matching</td></tr><tr><td></td><td colspan="2">Panel A: Propensity score matching</td></tr><tr><td> $n_{+}/n_{-}$ </td><td>32/3 = 10.67</td><td>32/7 = 4.57</td></tr><tr><td></td><td colspan="2">Panel B: Euclidean distance matching</td></tr><tr><td> $n_{+}/n_{-}$ </td><td>35/3 = 11.67</td><td>35/6 = 5.83</td></tr></table>

The results of the $( n _ { + } / n _ { - } )$ analysis are presented in Tables 9. We consider random matching of users in the two groups as well as propensity score matching, wherein the control group is restricted to users who have a similar propensity to have a friend who had favorited the song as in the treatment group. We also do the same for Euclidean distance matching, which, as described in Section 4.2.1, matches users on the propensity to be treated. Table 9 shows the results comparing random matching to propensity score matching. We find that $n _ { + } / n _ { + }$ − is equal to 10.67 under random matching, and declines to 4.57 under propensity score matching. The value of the ratio goes down because propensity score matching removes the homophily efect. Yet, the ratio is greater than one, suggesting the presence of proximity influence in this setting. Table 9 presents the results comparing random matching to Euclidean distance matching. Similarly, we find that $n _ { + } / n _ { - }$ is equal to 11.67 under random matching and declines to 5.83 under propensity score matching.

Tables 10 and 11, respectively, present the results for the probit and hazard models, comparing PSM (EDM, respectively) with random matching. In both tables we find that the ProxTreatment variable is positive and significant in both the probit and hazard models. Furthermore, in each case, the magnitude of the coefficient goes down under PSM or EDM compared to

Table 10. Estimating Proximity Influence Using Propensity Score Matching

<table><tr><td rowspan="2"></td><td colspan="2">Probit model</td><td colspan="2">Hazard model</td></tr><tr><td>Random matching</td><td>Propensity score matching</td><td>Random matching</td><td>Propensity score matching</td></tr><tr><td>Constant</td><td>-2.584***(0.284)</td><td>-2.148***(0.212)</td><td>-6.788***(0.632)</td><td>-5.884***(0.446)</td></tr><tr><td> $ProxTreatment_{ij}$ </td><td>1.208***(0.259)</td><td>0.819***(0.199)</td><td>2.464***(0.604)</td><td>1.601***(0.417)</td></tr><tr><td> $log(PreFavorites_j)$ </td><td>0.172**(0.066)</td><td>0.147**(0.061)</td><td>0.285**(0.116)</td><td>0.266**(0.110)</td></tr><tr><td>Genre fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>LR  $chi^2$ </td><td>53.61***</td><td>45.32***</td><td>65.18***</td><td>55.21***</td></tr><tr><td>Pseudo- $R^2$ </td><td>0.221</td><td>0.173</td><td>—</td><td>—</td></tr><tr><td>N</td><td>446</td><td>446</td><td>446</td><td>446</td></tr></table>

Notes. These regressions have a seven-day observation window after a 24-hour burn-in period. Standard errors are in parentheses.

$$
^ {* *} p <   0. 0 5; ^ {* * *} p <   0. 0 1.
$$

random matching. Specifically, in Table 10, the coeficient of ProxTreatment in the probit model goes down from 1.208 under random matching to 0.819 under PSM. In Table 11, the coeficient goes down from 1.061 under random matching to 0.963 under EDM. Since the most important consideration when estimating proximity influence is to be able to isolate it from homophily, we feel that PSM provides a more conservative estimation, since the coeficient on ProxTreatment declines by a larger amount. Accordingly, we use PSM as our primary matching method to account for homophily, and use it in favor of EDM in the joint model below as well.

Under PSM (Table 10), the marginal elasticities (or the percentage increase in probabilities of listen, conditional on treatment) corresponding to the

Table 11. Estimating Proximity Influence Using Euclidean Distance Matching

<table><tr><td rowspan="2"></td><td colspan="2">Probit model</td><td colspan="2">Hazard model</td></tr><tr><td>Random matching</td><td>Euclidean distance matching</td><td>Random matching</td><td>Euclidean distance matching</td></tr><tr><td>Constant</td><td>-2.736***(0.339)</td><td>-2.588***(0.319)</td><td>-7.035***(0.632)</td><td>-6.829***(0.827)</td></tr><tr><td> $ProxTreatment_{ij}$ </td><td>1.061***(0.212)</td><td>0.963***(0.218)</td><td>2.966***(0.340)</td><td>2.767***(0.627)</td></tr><tr><td> $log(PreFavorites_j)$ </td><td>0.175**(0.087)</td><td>0.175**(0.081)</td><td>0.343**(0.173)</td><td>0.298**(0.145)</td></tr><tr><td>Genre fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>LR  $chi^2$ </td><td>51.80***</td><td>47.79***</td><td>73.83***</td><td>67.86***</td></tr><tr><td>Pseudo- $R^2$ </td><td>0.198</td><td>0.179</td><td>—</td><td>—</td></tr><tr><td>N</td><td>476</td><td>476</td><td>476</td><td>476</td></tr></table>

Notes. These regressions have a seven-day observation window after a 24-hour burn-in period. Standard errors are in parentheses. p < 0.05; p < 0.01.

ProxTreatment estimates are 12% and 10.2% for random matching and PSM, respectively. This means that homophily and proximity influence together (under random matching) account for a 12% increase in the probability of listening to a new song, which can be separated into the following components: 10.2% for proximity influence and 1.8% for homophily.

## 5.3. Combined Model of Popularity and Propensity Influence

Finally, we consider the results obtained in a combined model of popularity and proximity influence, as shown in Table 12. We build the model in stages, so that the first model has popularity influence alone, while the second has proximity influence alone. The third model has variables for both popularity and proximity influence. We discuss just the key variables of interest—the control variables generally have the expected sign and significance. Starting with the first model, we find that the interaction term PopTreatment <sup>×</sup> Time is not significant, probably due to the sparseness of total listens at the user–song granularity (recall that our original DD model is at the aggregate song level). We also conduct a subsample analysis comparing the cases ProxTreatment <sup></sup> 0 and ProxTreatment <sup></sup> 1. We find that popularity influence is significant only when the user does not have a friend who has previously favorited the song. In other words, popularity influence is only important in the absence of proximity influence.

Turning to the second model, we find that Prox-Treatment is positive and significant, and its magnitude declines under propensity score matching, consistent with our earlier finding of proximity influence net of homophily. Looking at the subsamples based on PopTreatment (i.e., before and after the popularity information feature implementation), we find that the ProxTreatment variable has greater sign and significance in the absence of PopTreatment, consistent with the idea that the two types of influence are substitutes. The ProxTreatment variable is not significant for the case of PopTreatment <sup></sup> 1, but this regression itself is not significant, so we cannot draw a clear conclusion from it.

Finally, ProxTreatment remains significant in the third model, which combines popularity and proximity treatment variables. Here, the most interesting coeficient is that of the three-way interaction PopTreatment <sup>×</sup> After <sup>×</sup> ProxTreatment, capturing the impact of proximity treatment on popularity influence, and vice versa. We find that this coeficient is negative and significant, consistent with our previous results suggesting that popularity influence and proximity influence are substitutes. Specifically, popularity influence is less important in the presence of proximity influence, echoing our findings from the first model.

<table><tr><td rowspan="3">DV:  $\log(Listens_{gjt})$ </td><td colspan="6">(1) Popularity influence</td><td colspan="6">(2) Proximity influence</td><td colspan="2">(3) Popularity and proximity influence</td></tr><tr><td colspan="2">Full sample</td><td colspan="2">ProxTreatment = 0</td><td colspan="2">ProxTreatment = 1</td><td colspan="2">Full sample</td><td colspan="2">PopTreatment = 0</td><td colspan="2">PopTreatment = 1</td><td colspan="2">Full sample</td></tr><tr><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td><td>Random matching</td><td>PS matching</td></tr><tr><td>Constant</td><td>0.259(0.169)</td><td>0.265(0.171)</td><td>0.051(0.136)</td><td>0.073(0.182)</td><td>0.466(0.343)</td><td>0.498(0.318)</td><td>-0.017(0.153)</td><td>-0.021(0.156)</td><td>-0.198(0.222)</td><td>-0.045(0.167)</td><td>-0.122(0.258)</td><td>0.264(0.287)</td><td>0.116(0.148)</td><td>0.103(0.154)</td></tr><tr><td> $PopTreatment_j$ </td><td>-0.011(0.079)</td><td>-0.075(0.083)</td><td>-0.110*(0.063)</td><td>-0.143**(0.069)</td><td>0.088(0.113)</td><td>-0.008(0.121)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.140(0.089)</td><td>-0.171*(0.096)</td></tr><tr><td> $After_t$ </td><td>-0.228***(0.079)</td><td>-0.258***(0.085)</td><td>-0.187***(0.064)</td><td>-0.212***(0.071)</td><td>-0.268**(0.114)</td><td>-0.304**(0.124)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.187**(0.093)</td><td>-0.212**(0.102)</td></tr><tr><td> $ProxTreatment_{gj}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.323***(0.046)</td><td>0.313***(0.048)</td><td>0.295***(0.079)</td><td>0.277***(0.082)</td><td>0.210**(0.071)</td><td>0.155*(0.082)</td><td>0.285***(0.093)</td><td>0.253***(0.097)</td></tr><tr><td> $PopTreatment_j \times After_t$ </td><td>0.006(0.102)</td><td>0.078(0.108)</td><td>0.131*(0.074)</td><td>0.212**(0.090)</td><td>-0.120(0.147)</td><td>-0.056(0.157)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.131(0.121)</td><td>0.212**(0.102)</td></tr><tr><td> $PopTreatment_j \times ProxTreatment_{gj}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>0.258(0.221)</td><td>0.192(0.129)</td></tr><tr><td> $After_t \times PopTreatment_{ij}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.082(0.132)</td><td>-0.092(0.145)</td></tr><tr><td> $PopTreatment_j \times After_t \times ProxTreatment_{gj}$ </td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-0.251**(0.126)</td><td>-0.268**(0.134)</td></tr><tr><td> $log(PreFavorites_j)$ </td><td>0.041(0.027)</td><td>0.054*(0.027)</td><td>0.061***(0.022)</td><td>0.098***(0.023)</td><td>0.021(0.039)</td><td>0.009(0.040)</td><td>0.041*(0.025)</td><td>0.055**(0.025)</td><td>0.075*(0.043)</td><td>0.115**(0.043)</td><td>0.004(0.043)</td><td>0.001(0.047)</td><td>0.041*(0.022)</td><td>0.054**(0.023)</td></tr><tr><td>Genre fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>F</td><td>2.08**</td><td>2.30**</td><td>2.24**</td><td>3.70***</td><td>2.64***</td><td>2.28**</td><td>5.45***</td><td>5.74***</td><td>1.97*</td><td>3.51***</td><td>1.64</td><td>1.11</td><td>6.70***</td><td>6.42***</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.071</td><td>0.083</td><td>0.152</td><td>0.273</td><td>0.197</td><td>0.152</td><td>0.210</td><td>0.212</td><td>0.092</td><td>0.203</td><td>0.077</td><td>0.016</td><td>0.353</td><td>0.338</td></tr><tr><td>N</td><td>160</td><td>160</td><td>80</td><td>80</td><td>80</td><td>80</td><td>160</td><td>160</td><td>80</td><td>80</td><td>80</td><td>80</td><td>160</td><td>160</td></tr></table>

Table 12. Jointly Estimating Popularity and Proximity Influence

## 6. Conclusions

We have examined the role of “favorites” as a mechanism for social interaction in an online music community, and jointly estimated popularity influence due to the total number of favorites for a song and proximity influence due to the favoriting behavior of social network friends in close social proximity. Applying a quasi-experimental design to highly granular data from a leading music blog aggregator, we find robust evidence that both types of influence are statistically and economically significant. Quantitatively, we find that the availability of popularity information increases the number of listens for the average song by some 12%, and a full 21% for narrow-appeal music. This efect is significant for only newly posted songs, consistent with the nature of our site, where older songs are not immediately visible and do not get much attention. Proximity influence (i.e., having a friend that has favorited a song) increases the likelihood of listening to a song by 10.2%, which appears to be more than five times as important as the efect of homophily in explaining correlated consumption. Finally, popularity and proximity influence are substitutes for one another, in that proximity influence, when available, tends to dominate the efect of aggregate song popularity information.

Our findings of significant popularity and proximity influence resonate with industry reports indicating that 92% of consumers say positive recommendations from people they know are the most trusted sources of information (Nielsen Company 2012b). At the same time, when surveys indicate that 70% of consumers trust consumer opinions posted online (Nielsen Company 2012b), our results suggest that what might be driving the implied social influence might be both direct contact and communication between consumers as well as distant observation of aggregate consumption statistics. Our results indicate that the engagement in online music communities would benefit from both the dissemination of popularity information as well as the mobilization of social ties and coconsumption of music in online social networks.

These results have important managerial implications for the owners of online music communities, such as the one we study in this paper. First, our results suggest that both popularity and proximity influence can be leveraged to increase music consumption and engagement, enabling better monetization of the website, e.g., through better online advertising or more profitable freemium pricing.<sup>11</sup> Marketing strategies should be tied to the type of user and music. To leverage popularity influence, the website should make popularity information more salient, such as through the prominent display of daily, weekly, or monthly most popular lists. This is more important for niche or narrow-appeal music as opposed to mainstream or broad-appeal music. To leverage proximity influence, users should be encouraged and incentivized to increase social ties and coconsumption of music, and rewarded for their own engagement and that of their friends. Indeed, music websites might be able to increase engagement further by proactively pushing relevant popularity and proximity information, rather than waiting for users to discover them on their own.

Users with many social network friends and activities should be continuously fed with updates from their friends to increase their engagement, not unlike the newsfeed feature of Facebook, along with other tactics to increase the virality of music coconsumption (see, e.g., Aral and Walker 2011). Yet popularity information would be important for socially active users as well, given the likely sparseness in the range of songs favorited in even the most active social network cliques. On the other hand, for users that are inactive socially, popularity information is all the more important for music discovery. Here, based on the observational learning literature, we can expect herd behavior and information cascades (Bikhchandani et al. 1998), and that initial conditions matter, leading to inequality in consumption (popular songs will get more popular, while unpopular songs will get more unpopular) and to unpredictability of outcomes (“good” songs may not become popular, while “bad” songs may become viral hits), consistent with the findings of Salganik et al. (2006).

Our results should be generalizable to other experience goods such as online videos, books, software, and other digital content. They would also apply to other online communities where both popularity and proximity influence might be at play. In the music context, such communities include Last.fm, Spotify, and YouTube. Outside the music context, popularity and proximity influence occur together in online gaming communities (such as the online community associated with Xbox and Blizzard Entertainment games), online book clubs (for examples, see Abel 2013), and online health and fitness communities (such as Patients-Likeme.com and nikeplus.com), among others. Both types of influence are also likely on mainstream social networking sites such as Facebook and Twitter, and we are not familiar with prior work that has simultaneously examined popularity and proximity influence and their interactions on such increasingly ubiquitous platforms. More broadly, it is important for online platforms to experiment with diferent features that may facilitate user interaction and engagement with the site.

Turning to limitations, while we have a high level of granularity in music listening and favoriting decisions, we do not have detailed user profiles (because of privacy concerns and/or lack of availability). This means that there are likely sources of unobserved heterogeneity underlying the variation in sampling behavior, which may add noise or bias to our empirical analysis. Seemingly, one shortcoming in our diference-indiferences design is the fact that the treatment and control groups are drawn from diferent (neighboring) weeks. However, as we discussed earlier, this is not a cause for serious concern. On the contrary, our approach guarantees truly exogenous treatment and provides a quasi-experimental approach to study the impact of a global feature implementation that afects an entire website at a given point in time. Another limitation is the fact that at the time of our study, the social networking features on HM were relatively new, so the data for the proximity influence analysis are quite sparse. With richer data, we might be able to analyze the role of social ties and network structure more extensively, better leveraging the greater maturity of the community and its underlying social network. Overall, this work provides useful and robust empirical regularities with respect to macro and micro social influences in online communities and how they afect consumer behavior and profitable engagement strategies by the communities themselves.

## Acknowledgments

The authors would like to acknowledge Anthony Volodkin of The Hype Machine for providing essential data for this research, as well as the review team for providing insightful feedback and guidance.

## Appendix. Details of Matching Procedures for Estimating Proximity Influence Procedure for Propensity Score Matching at the User Level

We implemented a propensity score matching procedure at the user level, with the goal of matching users on their propensity to listen to any given song based on their taste. For each user $T _ { i }$ in the treatment group (who has not listened to song j but has at a friend favoriting it during the burn-in period), we find another user $C _ { i }$ in the control group who (i) has similar tastes as $T _ { i }$ (based on matching the listen profiles), (ii) has not listened to song j, and (iii) does not have any friend who has favorited the song during the burn-in period. The data construction procedure is detailed as follows:

0. Identify a set of active users during the observation window. Profile the listening behavior of users, during the window between September 1 to September 21, by constructing a vector incorporating 28 music characteristics and the number of other users they have followed.

1. Determine the treatment group T:

(a) For each song $j ,$ identify an active user i who has not listened to song $j$ but has at least one friend who has favorited song j during the burn-in period.

(b) Pool all such users into the treatment group T.

2. Determine the potential control group PC: pool active users not in T as the potential control group PC.

3. Determine the control group C: Match the propensity of listening to any given song based on the users’ taste profiles, using a logit model to predict the propensity to be treated. Match each user $T _ { i }$ in T with a user $\bar { \mathrm { P C } _ { i } }$ in $\mathrm { P C }$ with the closest estimated propensity score. Last, we pool these matched users into the control group C.

4. Recover the user–song observations of T and C:

(a) For each song j,

• reconstruct the user–song j pair if user $T _ { i }$ in the treatment group has a friend who has favorited that song j (see step 1(a));

• find the matching control group user $C _ { i }$ who has a friend who has not favorited that song j (see step 3).

(b) Repeat step 4(a) for all songs to construct both treatment and control groups.

## Procedure for Euclidean Distance Matching at the User–Song Level

To supplement our PSM methodology, which accounts for homophily at the user level, we also implemented EDM, which allowed us to match at the user–song level. The goal of conducting the matching at the user–song level is to match users not only on their likelihood to listen to a given song (which we have done with user matching) but also on their likelihood of having a friend favorite the song $( \mathrm { i . e . } ,$ , the likelihood of being treated). Therefore, for each song, for every user $T _ { i }$ who has not listened to the song but has friends favoriting it (our treatment group), we find another user $C _ { i }$ who (1) has similar tastes as $T _ { i }$ and who (2) has not listened to the song either but (3) has a friend who is likely to favorite it (our control group). In this process of matching at the user– song level, we essentially have 238 unique treatment user– song pairs with a relatively large potential control group for each of these pairs. However, we cannot use PSM to match at the user–song level as we did at the user level. Recall that in PSM, we estimated the propensity scores for each user based on 28 song characteristics to match users according to their music tastes. At the user–song level of granularity, the user–song pairs have a small number of observations that are treated, and thus estimating the logistic regression—the first step in propensity score matching—becomes intractable.

To mitigate this, we use Euclidean distance for the matching process, according to the procedure described below. Again, the goal of this procedure is (1) to control for homophily and (2) to match a focal treatment user whose friend has favorited a particular song to a control group user whose friend is likely to favorite that song but has not.

This matching procedure proceeds as follows:

0. Identify a set of active users during the observation window. Profile the listening behavior of users, during the window between September 1 to September 21, by constructing a vector incorporating 28 music characteristics and the number of other users they have followed.

1. For song j:

(a) Determine the treatment group $\mathrm { T } _ { j } \colon$ the active users who have not listened to song j but have at least one friend who has favorited song j during the burn-in period.

(b) Designate a set of potential control group users $\mathrm { P C } _ { j }$ the rest of the active users who have not listened to song j, nor have any friend who has favorited song j.

(c) Calculate the Euclidean distance between each user in the treatment group $( \mathrm { T } _ { j } )$ and each user in the potential control group $( \bar { \mathrm { P C } _ { j } } )$ based on the vector of characteristics as described in step 0; we call this the user or the song’s profile. For each user in the treatment group, select the three users from the potential control group with the shortest Euclidean distance as the “candidates” for the matched control group user.

(d) Determine the control group $\mathrm { C } _ { j } { \mathrm { : } }$ Calculate the Euclidean distance between song j’s profile and each profile of these three candidates’ friends. Pick one of these three candidates whose friend’s profile is the closest to the song’s profile. Last, each user in $\mathrm { T } _ { j }$ has a matched user in the control group (C<sub>j</sub><sup>)</sup>.

(e) For the users in $\mathrm { T } _ { j }$ and $\mathrm { C } _ { j } ,$ recover the set of user– song j pairs, as before.

2. Repeating steps 1(a)–1(e) for every song, and pool T<sub>j</sub> as the treatment group and $\mathrm { C } _ { j }$ as the control group.

## Endnotes

<sup>1</sup> At the time of our study, only 15%–20% of the users were using the social networking features, while the remaining users were “isolates”; i.e., users who were using the site to sample music, but were not following other users.

<sup>2</sup>The Hype Machine, previously studied by Dewan and Ramaprasad (2012), is the largest MP3 blog aggregator. It tracks thousands of MP3 blogs and provides links to blog posts and MP3 tracks, for other users to stream but not download.

<sup>3</sup> The number of favorites for a song is a lower bound on the number of unique listens of the song.

<sup>4</sup>The Hype Machine can be found at http://hypem.com/.

<sup>5</sup> Popularity information was visible to all users of the website, irrespective of whether they were registered to the site or not, and irrespective of whether they had social network friends or not.

<sup>6</sup> We thank an anonymous reviewer for suggesting that we look at the efect of popularity information visibility on songs released earlier to the site. However, we do not find a significant popularity efect for older songs, due to the fact that such songs receive very little attention on THM, and therefore the popularity information is immaterial.

<sup>7</sup> Specifically, we match the two groups of songs on observable characteristics, including genre, the number of favorites prior to the feature implementation, and the Amazon sales rank. We employ one-toone CEM to exactly match genres while not requiring our continuous variables to be exactly matched, but closely matched. A benefit of CEM is that the researcher can ensure balance in matching a priori through implementing bounds on the qualifications of a match for each variable that the groups are matched on. Each song in the treatment group is matched to one song in the control group, using the CEM procedure in Stata (Blackwell et al. 2009). The imbalance statistics produced by the CEM procedure indicate that the imbalance between the treatment and control groups was reduced due to matching.

<sup>8</sup> The Echo Nest has various measures of artist popularity that we collected and used to construct user profiles: artist hotness, artist familiarity, and artist discovery.

<sup>9</sup> Our results are robust to the choice of Weibull and Gompertz distributions for the hazard rate.

<sup>10</sup> Recall that the Amazon.com sales rank information was collected in 2014, and thus represents a measure of quality as observed in the long-term. This explains the large values of sales rank, though there is still variation within our data set.

<sup>11</sup> The freemium business model is common at music websites such as Last.fm, Spotify, etc.

## References

Abel J (2013) Online book clubs: Talk that stays on the page. New York Times (September 20). http://www.nytimes.com/2013/09/22/ fashion/online-book-clubs-talk-that-stays-on-the-paper.html.

Adomavicius G, Tuzhilin A (2005) Toward the next generation of recommender systems: A survey of the state-of-the-art and possible extensions. IEEE Trans. Knowledge Data Engrg. 17(6): 734–749.

Anagnostopoulos A, Kumar R, Mahdian M (2008) Influence and correlation in social networks. Proc. 14th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 7–15.

Aral S, Walker D (2011) Creating social contagion through viral product design: A randomized trial of peer influence in networks. Management Sci. 57(9):1623–1639.

Aral S, Muchnik L, Sundararajan A (2009) Distinguishing influencebased contagion from homophily-driven difusion in dynamic networks. Proc. Natl. Acad. Sci. USA 106(51):21544–21549.

Arndt J (1967) Role of product-related conversations in the difusion of a new product. J. Marketing Res. 4(3):291–295.

Bandura A (1971) Social Learning Theory (Prentice Hall, Englewood Clifs, NJ).

Bapna R, Umyarov A (2015) Do your online friends make you pay? A randomized field experiment in an online music social network. Management Sci. 61(8):1902–1920.

Belo R, Ferreira PA (2016) Peer influence in viral products: Empirical evidence from a large mobile network. Working paper, Heinz School, Carnegie Mellon University, Pittsburgh.

Bikhchandani S, Hirshleifer D, Welch I (1998) Learning from the behavior of others: Conformity, fads, and informational cascades. J. Econom. Perspect. 12(3):151–170.

Blackwell M, Iacus S, King G, Porro G (2009) Coarsened exact matching in Stata. Stata J. 9(4):524–546.

Brown J, Broderick AJ, Lee N (2007) Word of mouth communication within online communities: Conceptualizing the online social network. J. Interactive Marketing 21(3):2–20.

Brown JJ, Reingen P (1987) Social ties and word-of-mouth referral behavior. J. Consumer Res. 14(3):350–362.

Cai H, Chen Y, Fang H (2009) Observational learning: Evidence from a randomized natural field experiment. Amer. Econom. Rev. 99(3):864–882.

Card D, Krueger AB (1994) Minimum wages and employment: A case study of the fast-food industry in New Jersey and Pennsylvania. Amer. Econom. Rev. 84(4):772–793.

Chen P-Y, Shanasobhon S, Smith MD (2008) All reviews are not created equal: The disaggregate impact of reviews and reviewers at Amazon.com. Working paper, Arizona State University, Tempe. https://ssrn.com/abstract<sup></sup>918083.

Chen Y, Wang Q, Xie J (2011) Online social interactions: A natural experiment on word of mouth versus observational learning. J. Marketing Res. 48(2):238–254.

Chevalier J, Mayzlin D (2006) The efect of word of mouth on sales: Online book reviews. J. Marketing Res. 43(3):345–354.

Danaher B, Smith MD, Telang R, Chen S (2014) The efect of graduated response anti-piracy laws on music sales: Evidence from an event study in France. J. Indust. Econom. 62(3):541–553.

De Matos MG, Ferreira PA, Krackhardt D (2014) Peer influence in the difusion of the iPhone 3G over a large social network. MIS Quart. 38(4):1103–1134.

Dewan S, Ramaprasad J (2012) Music blogging, online sampling, and the long tail. Inform. Systems Res. 23(3):1056–1067.

Dewan S, Ramaprasad J (2014) Social media, traditional media, and music sales. MIS Quart. 38(1):101–121.

Dhar V, Chang EA (2009) Does chatter matter? The impact of user-generated content on music sales. J. Interactive Marketing 23(4):300–307.

Duan W, Gu B, Whinston AB (2009) Informational cascades and software adoption on the Internet: An empirical investigation. MIS Quart. 33(1):23–48.

Egebark J, Ekstrom M (2011) Like what you like or like what others like? Conformity and peer efects on Facebook. Working paper, Research Institute of Industrial Economics, Stockholm.

Forman C, Ghose A, Wiesenfeld B (2008) Examining the relationship between reviews and sales: The role of reviewer identity disclosure in electronic markets. Inform. Systems Res. 19(3): 291–313.

Ghose A, Ipeirotis PG (2011) Estimating the helpfulness and economic impact of product reviews: Mining text and reviewer characteristics. IEEE Trans. Knowledge Data Engrg. 23(10):1498–1512.

Godes D, Mayzlin D, Chen Y, Das S, Dellarocas C, Pfeifer B, Libai B, Sen S, Shi M, Verlegh P (2005) The firm’s management of social interactions. Marketing Lett. 16(3):415–428.

Granovetter M (1973) The strength of weak ties. Amer. J. Sociol. 78(6): 1360–1380.

Katz E, Lazarsfeld PF (1955) Personal Influence (Free Press, New York).

Lechner M (2002) Some practical issues in the evaluation of heterogeneous labor market programmes by matching methods. J. Royal Statist. Soc. 165(1):59–82.

Lee K, Lee B (2011) An empirical study on quality uncertainty of products and social commerce. Proc. 13th Internat. Conf. Electronic Commerce (ACM, New York).

Li X, Wu L (2013) Measuring efects of observational learning and social-network word-of-mouth (WOM) on the sales of daily-deal vouchers. Proc. 46th Hawaii Internat. Conf. System Sci., 2908–2917.

Liu Y (2006) Word of mouth for movies: Its dynamics and impact on box ofice revenue. J. Marketing 70(3):74–89.

Lu Y, Gu B, Ye Q, Sheng Z (2012) Social influence and defaults in peer-to-peer lending networks. Huang M-J, Piccoli G, Sambamurthy V, eds. Proc. 33th Internat. Conf. Inform. Systems.

Ma L, Krishnan R, Montgomery A (2010) Homophily or influence? An empirical analysis of purchase within a social network. Working paper, Heinz School, Carnegie Mellon University, Pittsburgh.

Manski CF (1993) Identification of endogenous social efects: The reflection problem. Rev. Econom. Stud. 60(3):531–542.

Meyer BD (1995) Natural and quasi-experiments in economics. J. Bus. Econom. Statist. 13(2):151–161.

Mizerski RW (1982) An attribution explanation of the disproportionate influence of unfavorable information. J. Consumer Res. 9(3):301–310.

Moretti E (2011) Social learning and peer efects in consumption: Evidence from movie sales. Rev. Econom. Stud. 78(1):356–393.

Nielsen Company (2012a) Nielsen music 360 . Report, Nielsen Company, New York.

Nielsen Company (2012b) Global consumers’ trust in “earned” advertising grows in importance. http://www.nielsen.com/us/ en/press-room/2012/nielsen-global-consumers-trust-in-earned -advertising-grows.html.

Salganik MJ, Dodds PS, Watts DJ (2006) Experimental study of inequality and unpredictability in an artificial cultural market. Science 311(5762):854–856.

Schöndienst V, Kulzer F, Günther O (2012) Like versus dislike: How Facebook’s like-button influences people’s perception of product and service quality. Huang M-J, Piccoli G, Sambamurthy V, eds. Proc. 33th Internat. Conf. Inform. Systems.

Sorenson AT (2007) Bestseller lists and product variety. J. Indust. Econom. 55(4):715–738.

Tucker C (2008) Identifying formal and informal influence in technology adoption with network externalities. Management Sci. 54(12):2024–2038.

Tucker C, Zhang J (2011) How does popularity information afect choices? A field experiment. Management Sci. 57(5):828–842.

Valente TW (1995) Network Models of the Difusion of Innovations (Hampton Press, Cresskill, NJ).

Wang J, Chang C (2013) The impacts of online lightweight interactions as signals. Baskerville R, Chan M, eds. Proc. 34th Internat. Conf. Inform. Systems.
