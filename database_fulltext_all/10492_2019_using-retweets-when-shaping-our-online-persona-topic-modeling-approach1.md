---
otero_id: 10492
otero_key: "HDNYXTXS"
title: "Using Retweets When Shaping Our Online Persona: Topic Modeling Approach1"
authors: "Hilah Geva; Gal Oestreicher-Singer; Maytal Saar-Tsechansky"
year: "2019"
journal: "MIS Quarterly"
doi: "10.25300/misq/2019/14346"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# USING RETWEETS WHEN SHAPING OUR ONLINE PERSONA: TOPIC MODELING APPROACH<sup>1</sup>

Hilah Geva and Gal Oestreicher-Singer The Coller School of Management, Tel-Aviv University, Tel Aviv, ISRAEL {hilahlev@mail.tau.ac.il} {galos@post.tau.ac.il}

Maytal Saar-Tsechansky

McCombs School of Business, University of Texas at Austin,

Austin, TX 79712 U.S.A. {maytal@mail.utexas.edu}

Theories of personal branding are built on the idea that each individual should be aware of the persona they present to the world. Nowadays, as social interactions are increasingly shifting to the online arena, users of social platforms are presented with many new opportunities and technology-enabled tools by which they can construct their online personas. A powerful type of tool that has emerged in this ecosystem is the ability to reiterate a friend’s activity, that is, to redistribute an exact copy of the content that the friend has posted online (e.g., words, videos, or pictures) and to incorporate it into one’s own online image. In this work, we examine how users employ reiteration tools when presenting themselves and shaping their online presence. We focus on retweeting behavior on Twitter and study the spectrum of topics that users choose to reiterate. We hypothesize that users’ retweeting behavior will show patterns that are theorized to characterize effective personal branding strategies: Specifically, when reiterating content produced by others, a user will maintain a persona that is consistent with the persona portrayed in self-produced tweets.

We analyze data taken from Twitter over a period of 6 months in 2016, with regard to 3,388 nonexpert users and 464 expert users and the users whom they followed. We use LDA topic modeling to derive the topics in each user’s self-produced tweets and retweets. We find that users’ retweets tend to focus on the topics they address in their self-produced tweets, instead of adding new topics. Further, we find that a user’s retweets do remarkably little to alter the distribution of topics discussed in self-produced tweets. Finally, we find that this tendency is more prominent among “expert” users (i.e., professional bloggers who are particularly likely to use Twitter as a personal branding tool). A rigorous identification strategy lends support to the proposition that the observed effects are indeed driven by image-related considerations rather than by alternative factors known to influence retweeting behavior, such as exposure bias (a phenomenon associated with the formation of echo chambers), need for uniqueness, and social dynamics on the Twitter platform.

Keywords: Twitter, social networks, personal branding, identity signaling, topic modeling, LDA, retweet, persona, impression management

## Introduction

In 1997, Tom Peters coined the term “personal branding” in his manifesto titled “The Brand Called You.” The idea he put forward was simple: Each person should be aware of the persona that he or she signals to the world. Through his manifesto, Peters popularized the notion of impression management—the process by which individuals attempt to control the impressions that others form of them in social situations. Since the publication of Peters’ article, researchers and contributors to popular media outlets have been attempting to provide insights and guidelines as to the best practices in personal branding (e.g., Montoya and Vandehey 2005; Kayser 2014; Schawbel 2009). An understanding of these principles is becoming increasingly important as social interactions are shifting to the online arena: Online social platforms provide their users with a multitude of opportunities to express themselves and broadcast their experiences, thoughts, and opinions, which effectively become an integral part of their signaled identity. These social platforms are not passive vessels; rather, they actively seek to introduce technology-enabled features (such as the “Like” on Facebook) that give rise to new social behaviors and provide new avenues of self-expression, enabling individuals to manage their impressions in new and exciting ways.

We focus on a specific type of behavior that has emerged as a result of these technology-enabled features: the ability to reiterate a friend’s activity, that is, to redistribute an exact copy of content that the friend has posted online (e.g., words, videos, or pictures). In effect, reiteration tools such as the “Retweet” function on Twitter and the “Share” functions on Facebook and Google+ enable the user to leverage someone else’s self-expression, as is, and make it their own, adding to their online image as reflected by the online platform. This reiteration process is effortless and does not entail loss of the message’s integrity—in contrast to the offline alternative of simply attempting to remember a comment or a joke and repeat it to one’s friends.

]In this work, we examine how users employ reiteration tools when presenting themselves and shaping their online presence. Specifically, we analyze how users implement the retweet function on Twitter—perhaps the most popular reiteration tool—in terms of the spectrum of topics that they choose to reiterate.

We begin with the premise that, in the context of Twitter, the topics discussed in a user’s self-composed tweets (self-tweets) can be considered as a proxy for the spectrum of topics that the user is able to (or chooses to) self-produce (hereafter referred to the self-produced persona). However, the persona reflected in the user’s Twitter profile (referred to herein as the full persona) comprises not only self-tweets but also retweets. The retweet function ostensibly provides Twitter users with an opportunity to shape their public personas in virtually any manner they might choose, by taking the time to curate whatever identity they prefer through the content that they share. Thus, when a user augments her own content by retweeting content produced by others, she is faced with a choice: Should she add new topics and expand the breadth of her online persona, or should she add content relating to the same topics and enrich the depth of her online persona? On the one hand, expanding the breadth of topics may signal a more knowledgeable and diverse persona compared to the persona reflected in self-tweets. On the other hand, using the retweet tool to enrich the depth of the online persona may portray a more focused and authentic persona.

This question is not purely empirical. Building on consumer behavior literature on identity signaling, in addition to research in the fields of Information Systems and Marketing, we propose that user reiteration behavior is strongly influenced by personal branding principles discussed in marketing research. This literature suggests that although the digital age fosters the freedom to add breadth to one’s persona, it is advantageous that one’s “personal branding message be clear and consistent, creating an air of authenticity” (Labrecque et al. 2011, p. 39), as such authenticity enhances message receptivity. In our context, this means that users should be likely to use the reiteration tool to enhance their self-tweets by retweeting additional content about topics on which they produce content themselves. Such behavior may serve to enrich the user’s persona while also keeping it focused and consistent. Accordingly, we hypothesize that users’ retweets will resemble their self-produced personas, both in terms of the topics they discuss, and in terms of the distribution of those topics.

To provide further support to the idea that the behavior of Twitter users is in line with personal branding principles, we examine a specific group of so-called “expert” users— bloggers on prominent blog sites who have Twitter accounts—who, presumably, are more likely than more “casual” users to use Twitter as a personal branding tool. As we elaborate below, according to the personal branding literature, we expect these users to be even more prone to exhibiting personas that seem authentic and consistent. Thus, we hypothesize that expert users will strive to signal a consistent persona to a greater extent than other users.

Research on content contribution and sharing on online platforms has identified additional factors and motivations, beyond image considerations, that may affect users’ sharing decisions and their resultant online personas. Our empirical analysis relies on an elaborate identification strategy that takes these factors into account, allowing us to attribute the remaining persona consistency to users’ image-related and personal branding considerations. The factors we control for include need for uniqueness, social network dynamics, and, importantly, exposure to a nonrandom subset of tweets, which biases the content available for a user to retweet. We further distinguish between the phenomenon we examine and the documented phenomenon of echo chambers in social media, defined broadly as a tendency of participants in online discussions to reinforce similar views. We emphasize that although the two phenomena bear superficial similarities, in that they both encompass situations in which the content that a user is exposed to and broadcasts to others is characterized by certain constraints, they are actually fully distinct from each other, such that research of the latter provides little insight regarding the former.

To test our hypotheses, we analyze data collected from Twitter corresponding to a period of 6 months in 2016, with regard to 3,388 core users (“typical” users with an active Twitter presence; see our “Data Collection” section for details) and the approximately 2 million users whom they followed (their “followings”), as well as 464 expert users and their approximately 700,000 followings. We compiled the self-tweets and retweets of each user in the data set and applied Latent Dirichlet Allocation (LDA) topic modeling to derive the topics that users discussed in their self-tweets and in their retweets (Blei et al. 2003). This enabled us to capture at the individual user level both the variety of topics being discussed and the relative volume of discussion of each topic in each user’s self-tweets and retweets. Our analyses support our hypotheses, showing that, in the course of constructing and presenting their online personas, users—and particularly expert users—tend to adhere to personal branding principles by retweeting content that is consistent, in terms of the topics discussed, with the content they produce themselves.

From a theoretical perspective, our work makes three key contributions. First, it links the growing literature on content contribution in social media with personal branding theories, thereby advancing our understanding of the image-related motivations on such media and their effect on the spectrum of topics discussed. Second, it contributes to the stream of literature that specifically seeks to elucidate the drivers of content sharing (rebroadcasting) behavior on social media such as Twitter. Whereas studies in this vein have considered network and link structures, in addition to social dynamics, our work focuses on the effects of textual characteristics on rebroadcasting decisions, and it proposes a unique identification technique for isolating such effects. Third, we contribute to the IS literature that examines emerging online social behaviors in an environment of new digital tools, by focusing on the use of such a tool (the retweet) in building one’s online persona.

From an empirical perspective, our work is among the first to model individuals’ online personas using the spectrum of topics mentioned in a user’s self-tweets and retweets. Within the IS literature, Lee et al. (2017) use the spectrum of topics to measure similarity between different users for the purpose of examining the main determinant of network formation in location-based social networks. Within the Computer Science literature, Bi and Cho (2016) propose two new Bayesian models that integrate the analysis of tweet text and users retweeting behavior in a single probabilistic framework, with the goal of constructing a model that captures the diversity of users’ interests on Twitter. Ramage et al. (2010) characterize users and tweets using a partially supervised model that maps content into dimensions. We add to this literature by using the spectrum of topics to model different aspects of users’ content contribution, which we conceptualize as reflecting their online personas and signaled identities. This approach provides a quantitative metric for different aspects of a user’s persona and enables us to contribute quantitative evidence to the field of online image and impression management, a field mostly dominated by qualitative research. In addition, we offer a new identification method to control for exposure bias—and specifically, content homophily—in topic modeling analysis of social networking sites. We suggest a way in which individually constructed baselines can be used to identify the extent to which an observed effect goes beyond what is driven by homophily.

## Context: Twitter

Twitter is one of the most popular social media platforms, and the most popular microblogging service (Java et al. 2007; Murthy 2013), and as such has received much attention from IS researchers (Mousavi and Gu 2014; Hill et al. 2013; Oh et al. 2013). Twitter enables users to broadcast “what’s happening” by posting short messages known as tweets. Until recently, tweets were limited to 140 characters; in November 2017, Twitter doubled the limit to 280 characters. Tweets commonly share information, news, opinions, complaints, or details about daily activities (Smith et al. 2012).

To understand how users engage on Twitter, it is important to understand how Twitter is distinct from other social networking platforms. Unlike social networks such as Facebook or LinkedIn, which encourage reciprocity (e.g., the common relationship in Facebook—“friends”—is a two-sided, mutually agreed-upon relationship), Twitter enables users to follow other accounts at the click of a button (although about 10% of accounts are protected, meaning that they can be viewed only by approved followers), and there is no explicit expectation that the latter will return the gesture. Thus, Twitter is a directed social network that comprises interconnected communities of users who mutually follow one another, in addition to relationship structures in which users with large numbers of followers, whom they do not follow in return (e.g., as in the case of a movie star with millions of fans), broadcast their opinions “to the masses.” In other words, Twitter functions both as a social networking platform—a platform whose goal is to foster active relationships among individuals via social sharing—and as a social media platform, defined as “a medium wherein ‘ordinary’ people in ordinary social networks… can publish user-generated ‘news’ or ‘updates,’” and in which the notion of a community of friends is not as salient (Murthy 2013, p. 304). The latter feature enhances Twitter’s status as a microblogging service.

For the reader’s convenience, we summarize some of the Twitter-specific terminology used in this paper. Given a focal user (John, for example), the users following John are referred to as John’s followers, while the users John follows are referred to as followings. The tweets that John posts constitute John’s timeline. This timeline comprises all of John’s tweets (including his retweets), ordered chronologically, and it can be viewed by anyone who follows John. In contrast, John’s home timeline (also referred to as his feed; what he sees on his homepage when entering Twitter) is the aggregation of all tweets posted by John’s followings, ordered chronologically. Note that, unlike some networks (for example, Facebook), Twitter does not hide any content from users; all tweets posted by a user’s followings appear in his or her timeline, sorted approximately in reverse chronological order.<sup>2</sup> There are several types of tweets on Twitter; the two most popular are: (1) self-tweets ( the content the John produces by himself) and (2) retweets (tweets that John did not produce by himself, but that he chooses to rebroadcast).

## Theoretical Development and Hypotheses

This research focuses on how online presentation considerations, and specifically personal branding and impression management, shape users’ sharing decisions and their resultant online personas (in terms of topics shared). Accordingly, in this section, we first discuss research on identity signaling and personal branding considerations, and we derive hypotheses regarding the potential effects of these factors on the spectrum of topics that individuals choose to retweet. We subsequently review additional motivations and factors that might influence users’ retweeting behavior. We discuss how each factor might (or why it might not) be expected to influence the scope of topics that a Twitter user chooses to retweet, and we outline how we control for such influence in our analysis.

## Image-Related Considerations: Identity Signaling and Personal Branding

In sociology and social psychology, impression management is defined as a goal-directed process in which people, either consciously or unconsciously, attempt to influence the perceptions of others about a person, object, or event. In many cases, the term is used to refer to the process by which individuals attempt to control the impressions that others form of them in social situations. This ongoing process is influenced both by the target audience and by the context of the social interaction, and it may involve making choices about what information to share (Leary and Kowalski 1990; Toma et al. 2008). The outcome of this process is, effectively, an individual’s online image, which includes self-perceived reputation and status.

In the consumer behavior literature, identity signaling is considered an integral part of impression management (Berger 2014). Identity signaling is a process by which consumers signal to others specific, desired identities (Berger and Heath 2007), and it manifests in various consumer behaviors, including purchase decisions. For example, publicly visible products such as cars and clothes are often used to signal identity (Berger and Heath 2007). Accordingly, consumers may choose to adopt or abandon products that convey specific identities, to ensure that others perceive them as they wish to be perceived (Berger and Heath 2008).

Knowledge is another resource through which people might signal their identities. In contrast to visible products, which a person merely has to use in public in order to convey a desired identity, knowledge tends to be private and is therefore traditionally considered to be “much more difficult to display” (Berger 2014, p. 590). In recent years, however, computer-mediated communication platforms such as social networks and social media websites have made it straightforward, and even unavoidable, to signal one’s identity through knowledge contribution and sharing. A person’s online profile is effectively the identity he portrays to others, and this profile largely comprises the thoughts, opinions, and other knowledge that he chooses to share. It follows that when making content contribution and sharing decisions, users of social media platforms are likely to strive to share identity-relevant information (Berger 2014).

Indeed, recent research has theorized and provided empirical evidence that content contributions of noncommercial users in social media settings such as Twitter are largely motivated by reputation factors (Shi et al. 2014; Wasko and Faraj 2005) and underlying image-related factors (Peng et al. 2018; Toubia and Stephen 2013). In the specific context of Twitter, Toubia and Stephen (2013) have empirically established that image-related utility plays a larger part in motivating content contribution decisions than intrinsic motivation. Similarly, Shi et al. (2014) have noted that “perceived reputation enhancement has been identified as an important factor in motivating sharing in the literature of information systems and management” (p. 128).

Given that online tools have made it second nature to signal one’s identity by sharing content and knowledge, the question becomes what identity users will choose to portray. On Twitter and other social media platforms, there are no time and space constraints, and it seems that individuals can “take the time to curate whatever identity they prefer through what they share” (Berger 2014, p. 603). In particular, in contrast to offline environments, where it is very difficult to share knowledge that one does not actually possess, online environments make it easy for anyone to talk about practically anything, simply by using designated reiteration tools (such as the retweet function on Twitter). Accordingly, we wish to hypothesize about whether individuals use such tools to display identities that are more diverse than the ones they are able to self-produce, in terms of the span of topics discussed, or whether their identities will be contained to the spectrum of topics presented in their self-produced personas.

To develop our hypotheses, we turn to the marketing literature on personal branding. Personal branding tactics have been used for decades by public figures such as movie, sports, and pop stars (Rein et al. 2006; Shepherd 2005). However, as noted above, the prevalence of online social networks, and the highly public nature of the information disseminated in such networks, have created a situation in which individuals engage in identity signaling and thus brand themselves whether they intend to or not. It has been said that if a person does not serve as her own “marketer,” a void is left unfilled, and others will end up branding her, taking away the control she has over how others perceive her (Kaputa 2005; Shepherd 2005). Thus, personal branding in the online world has become an important task for practically everybody (Labrecque et al. 2011). Scholars have investigated several aspects of personal branding, including the process of personal branding or impression management in social network sites such as Facebook and YouTube, using mostly qualitative methods (Chen 2013; Fox and Rooney 2015; Labrecque et al. 2011; Manago et al. 2008; Marshall et al. 2015; Rosenberg and Egbert 2011; Rui and Stefanone 2013; Zhao et al. 2008). Researchers have also examined the implications of personal branding settings such as job market competition (Chiang and Suen 2015; Khedher 2014; Parmentier et al. 2013), politics (Lilleker 2014; Speed et al. 2015) and online dating (Toma et al. 2008).

Perhaps because personal branding on social media platforms is a relatively new phenomenon, relatively few studies have empirically explored the strategies that individuals use when selecting content to incorporate into their personal brands on social media. Literature on product-branding sheds some light on the principles that users might be likely to follow: It suggests that a consistent and simple message is instrumental to having a good and successful brand, as consistency is perceived as conveying authenticity, which enhances message receptivity (Holt 2004; Labrecque et al. 2011). Notably, similar logic has been applied to the domain of personal branding: Researchers have proposed that, although the digital age fosters the freedom to explore multiple personas, it is advantageous that one’s “personal branding message be clear and consistent, creating an air of authenticity” (Labrecque et al. 2011, p. 39; see also Kaputa 2005). The tendency to emphasize consistency when engaging in impression management may further be enhanced by practical considerations: While it might be technically easy to create multiple personas in the online world, the public nature of the information in networks such as Twitter and Facebook can make it increasingly difficult and costly to successfully manage multiple online personas (Back et al. 2010; Labrecque et al. 2011).

While prior research has suggested that consistency is beneficial in building one’s personal brand, to the best of our knowledge, our work is the first to investigate whether individuals actually establish such consistency through the selection of topics to discuss on social media, when using reiteration tools.

## Hypothesis Formulation

In what follows, drawing from the rationale outlined above, we present the three hypotheses driving our empirical investigation. Our first hypothesis speaks to the spectrum of topics a user will retweet about, while our second hypothesis focuses on the resulting distribution of topics reflected in the user’s online persona. Our third hypothesis focuses on expert users.

As discussed, the literature on identity signaling and imagerelated motivation suggests that, when choosing which posts to retweet, the user is aware of the identity he is signaling and of how it relates to his personal brand. The literature on personal branding suggests that, in order to enhance his brand or desired identity, the user will aim to maintain a consistent and unified persona. This idea leads us to expect that Twitter users will strive to ensure that the content they retweet—as reflected in the topics at the focus of those retweets—is consistent with the content of their self-tweets. In other words, they will use retweets to add depth, rather than breadth, to their online personas in terms of topics discussed. Putting these ideas together, we hypothesize

H1: When retweeting content on Twitter, users will try to maintain a unified presentation of themselves, and will therefore retweet mostly about topics that are discussed in their self-tweets rather than about topics that they do not typically address.

Enriching one’s self-produced persona may also take the form of changing the distribution of content across a given set of topics (e.g., by making the distribution more even, or by emphasizing certain topics at the expense of others). Yet, as we expect users to maintain a consistent persona, we not only expect the actual topics included in their retweets to be similar to the topics in the self-tweets, we also expect the retweets to preserve the underlying topic distribution of the user’s selftweets. For example, if “sports” is the topic that John discusses most frequently in his self-tweets, we expect it to remain among the most frequently discussed topics in his full Twitter persona (comprising self-tweets and retweets). More formally,

H2: The topic distribution of a user’s full persona will be similar to the topic distribution of the user’s self-tweets.

Retweeting patterns may vary across different subsets of users. In particular, some users may be more likely than others to use Twitter for personal branding purposes, and thus to present a consistent persona. We focus on the behavior of expert bloggers (expert users), who are likely to have a semiprofessional background in writing and therefore may perceive their Twitter account as part of their blogging “job,” making them more attuned to their personal branding on this platform. We hypothesize that, in line with H1 and H2, expert users will tend to maintain consistency across their self-tweets and their retweets in terms of the topics discussed and the underlying topic distributions. More importantly, this tendency will be more prominent than the corresponding tendency among more casual Twitter users. Accordingly, we hypothesize

H3: When retweeting content on Twitter, expert users will demonstrate a more unified presentation of themselves than other users do, both with regard to the choice of topics and with regard to the topic distribution.

## Alternative Drivers of the Retweeting Decision

## Selection Bias: Exposure Bias and Confirmation Bias

When selecting which tweets to reiterate, a user does not select randomly from the entire Twittersphere but rather chooses his tweets from a comparatively small subset of tweets to which he is exposed. This is the subset of tweets tweeted by her followings (users she follows). Clearly, users do not randomly choose whom to follow, and hence the content of the tweets contained in this subset is likely to be biased. This bias results from the well-documented phenomenon of homophily. Moreover, given that a user is exposed to a specific set of tweets, she might pay more attention to some tweets than to others, thereby further biasing the pool of source content from which she is likely to retweet. Specifically, theories of selective exposure and confirmation bias assert that users filter out (i.e., tend not to perceive) information that contradicts their own views, leading to the echo chamber phenomenon. In what follows, we will discuss these two sources of bias and their implications for our work.

Exposure Bias Resulting from Homophily: Extensive research has documented the phenomenon of homophily (Aral et al. 2009, Bapna and Umyarov 2015), that is, the tendency to like or to associate with others who are similar to oneself in their characteristics and opinions. In the context of Twitter, homophily is expected to have a substantial influence on the distribution of topics to which an individual is exposed, in that a person is likely to follow (and view the tweets of, and subsequently retweet) others who discuss topics that she herself discusses.

Confirmation Bias and the Echo Chamber Phenomenon: As noted above, the theory of selective exposure asserts that individuals tend not to perceive information that contradicts their own views. This phenomenon is highly similar to confirmation bias, in which “people seek [and share] information that supports their current convictions” (Quattrociocchi et al. 2016, p. 1). Taken together, selective exposure and confirmation bias imply that a user who is exposed to a given set of tweets may consider those tweets that challenge his opinions to be invalid—and in fact, he may not register them at all— and will therefore be unlikely to retweet them.

Selective exposure and confirmation bias have been documented in online settings and can result in an echo chamber phenomenon (Del Vicario et al. 2017; Mutz and Martin 2001), defined by Chandler and Munday (2016) in A Dictionary of Social Media as

A mainstreaming ideological effect in which a group worldview is reinforced through continual circulation amongst like-minded people …. For example, political blogs tend to link with those which reinforce their values and to be disconnected from dissident voices.

In other words, linked individuals discussing a given topic online (e.g., politics or ideological positions) tend to reinforce similar points of view regarding that topic. Online echo chambers have attracted substantial research attention in recent years, and numerous studies have sought to investigate whether communication on online platforms can indeed be characterized as an echo chamber (examining, for example, the extent to which individuals in friend networks hold similar view-points and the extent to which users are exposed to a variety of opposing views) and to identify cognitive drivers of the phenomenon (see, for example, Bakshy et al. 2015; Barberá et al. 2015; Flaxman et al. 2016; Garrett 2009).

In broad terms, the echo chamber phenomenon might seem to relate to what we are investigating here, as it encompasses individuals’ tendency to limit the scope of content they disseminate. Yet, we suggest that the hypotheses at the focus of this investigation—regarding the scope of topics that a user discusses, and their tendencies to retweet content within or outside that scope—are fully distinct from the concept of echo chambers and are not covered by prior research in this vein. This is because the concept of an echo chamber does not relate to the spectrum of topics that an individual discusses, but rather to his or her positions or view-points within a given topic. For example, the echo chamber literature can inform us regarding the extent to which a user who discusses abortion online and holds pro-life views is likely to encounter or disseminate pro-choice messages. Yet it cannot provide insight regarding whether a user who frequently tweets about football is likely to retweet content about music, a topic he rarely discusses (assuming that music-related content as such does not directly reinforce or challenge his ideological opinions), or whether he will prefer to stick to content on football.

Indeed, there is no reason to assume that selective exposure and confirmation bias—the drivers of the echo chamber phenomenon (Del Vicario et al. 2017; Mutz and Martin 2001)—will prevent a user from expanding the set of topics she discusses, as long as these topics do not inherently embody ideological, political, or other view-points that are opposed to her own. This perspective is supported by the observations of Barberá et al. (2015), who studied user communication patterns on various topics and observed that some topics, such as politics, tend to stimulate the formation of echo chambers (defined in their work as discussions that take place primarily among people who share similar ideological view-points), whereas other topics do not. Specifically, the authors noted that, when discussing current events that were unrelated to politics, individuals propagated content by others who did not share their ideology. Thus, for example, if we observe that a person who primarily tweets content about sports is reluctant to retweet content about music, there is no obvious reason to believe that confirmation bias is underlying this behavior.

To sum up, exposure bias (through homophily) and confirmation bias create a selection bias that can affect the content that users observe and subsequently share. Of these two phenomena, exposure bias is likely to influence the spectrum of topics that users discuss. Specifically, it may lead users to share content that resembles the content they self-produce, not because of reluctance to share new topics but rather because familiar topics are the only topics to which they are exposed. In our analyses, we overcome these concerns, as elaborated in the “Identification” section below.

## Need for Uniqueness

Individuals experience a need for uniqueness, which manifests in negative emotions when they find that they are overly similar to others (Berger and Heath 2007; Snyder and Fromkin 1980). Previous literature has suggested that this need for uniqueness is especially strong in the public sphere and in online interactions (Lovett et al. 2013), and that users of social media platforms take uniqueness considerations into account when posting content (Peng et al. 2018). In particular, existing work suggests that, in online interactions, users can satisfy their need for uniqueness by sharing novel content (Ho and Dempsey 2010; Peng et al. 2018). Recent IS literature supports this perspective (although it does not directly discuss the need for uniqueness), showing that Twitter users feel a need to provide their network with new knowledge (Boyd et al. 2010; Shi et al. 2014).

Notably, while the need to provide one’s network with new information might lead a user to cover new topics in her retweets, it can also be satisfied through retweeting content that holds new information regarding topics that she discusses frequently. Thus, if a user’s retweeting behavior reflects a tendency to enhance the depth rather than the breadth of her persona (or vice versa), this tendency is not likely to be attributable to her need for uniqueness per se. In our analyses we do, however, take into account a user’s need for uniqueness by controlling for the extent to which a user is likely to perceive a given tweet (on any topic) as novel and thus to retweet it. Specifically, we take into account tweet popularity, as users may resist sharing content that has already been shared by many others (Peng et al. 2018), as such content probably does not carry information that is new to their networks. We also consider tie strength among users, as Shi et al. (2014) have shown that content from a user’s weak ties is more likely than content from strong ties to contain knowledge that is new to the user’s followers, and thus is more likely to be retweeted.

## Social Dynamics (Reciprocity, Tie Strength, Source Popularity)

Individuals’ sharing choices are based not only on the content and novelty of the tweets they share but also on in-platform social dynamics. In particular, previous work has documented a need for reciprocity (Boyd et al. 2010), which means that, due to a sense of social obligation, a user’s retweeting choices are likely to favor content by users who have previously retweeted her content. In addition, tie strength between users has been shown to influence the retweeting decision. For example, as noted above, Shi et al. (2014) observed that users are more likely to retweet content from weak ties. Finally, users may be influenced by the popularity of the source of the tweet. That is, they may be more inclined to retweet content posted by users who are dominant in the network (have many followers). In our empirical analysis we control for each of these socially driven motivations for retweeting.

## Data Collection

This work uses publicly available data from Twitter.com, collected using Twitter’s REST API.<sup>3</sup>

To address H1 and H2, we collected data about a set of core users, that is, casual users who are representative of the Twittersphere population (in contrast to celebrities or professional bloggers). For each core user we sought to collect both the tweets he had posted over the course of 6 months in 2016 and the content he had received during that time, that is, the tweets that appeared in his home timeline (the latter content reflects the content available for the user to retweet; see further discussion below). Since Twitter’s REST API provides each user’s timeline but not the home timeline, we constructed the home timeline for each user, that is, we identified the tweets that each core user could select for retweeting. To do so, we collected each core user’s own timeline as well as the timelines of each of the core user’s followings, as these timelines collectively make up the user’s home timeline.

Given the limitations that Twitter imposes on data collection<sup>4</sup> and the fact that, for each core user, we collected both the core user’s tweets and his followings’ tweets, we were limited in the number of core users on whom we could collect data. Thus, we randomly selected a sample of 3,500 core users, and obtained a final sample of 3,388 users, after elimination of unanalyzable accounts (as discussed in detail below). Overall, we collected 6 months’ worth of historical data for those selected users and their approximately 2 million followings.

To address H3, we selected a set of expert users and, as in the case of the core users, collected their complete timelines and the timelines of their followings for a period of 6 months.

Finally, we note that on February 2016 Twitter changed the home timeline layout from a purely chronological view to a more curated view that highlights certain tweets that the user is likely to appreciate. Consequently, during our collection period, it was not guaranteed that the tweets appearing in a user’s timeline would be arranged in a strict chronological order. Because this may have biased our results, we reran our main analysis on another data set we had collected prior to the policy change. That set included tweets of 2,435 core users (and their followings) from September 2015 (going 6 months back). All the results obtained through this analysis are similar in direction, magnitude and significance to those obtained from the 2016 dataset. (For complete details, see Appendix A.) In what follows, we describe the selection and collection processes.

## Selecting the Core Users

We selected the core users according to the following fourstep process, using Twitter’s streaming API.<sup>5</sup>

1. We deployed a listener to collect tweets produced by U.S. users<sup>6</sup> during a 1-week window between October 1 and October 8, 2016. This resulted in approximately 8 million tweets.

2. Of the tweets collected in step (1), we drew uniformly at random a sample of 50,000 tweets, produced by 44,054 unique users. Of these users, we filtered out users with exceptionally high (top 5%) numbers of either followers or followings. Importantly, these users were removed in order to eliminate users who probably use Twitter in a commercial capacity or in some other unusual capacity. Additionally, we filtered out users who were inactive in the 3 months prior to the collection date (users who posted fewer than 10 self-tweets or fewer than 10 retweets per month during those 3 months). The latter step aimed to ensure that the data set would pertain only to users who were engaged in Twitter during the data collection time window. Looking at seasonal or one-time users was of less interest to us; rather, we aimed to study the behavior of users who cultivate a presence on the platform. This process resulted in a set of 25,905 potential core users.

3. From the set of users produced in step (2), we randomly drew a sample of 3,500 as the core users for our study. We subsequently eliminated 112 additional users from the set of core users, due to changes in their privacy settings during the data collection window, or if a user’s collection of tweets resulted in no tweets following our language processing scheme (described below); this process resulted in a final sample of 3,388 core users.

4. Finally, for each of the 3,388 core users, we collected a list of the core user’s followings. This resulted in a set of approximately 2 million Twitter users.

## Collecting Core Users’ Data

After identifying the 3,388 core users and their approximately 2 million followings, we collected data from their Twitter accounts. Our goal was to collect 6 months’ worth of historic data for each user and his followings. The collection process itself was conducted between November 3 and November 29, 2016. For each of our 3,388 core users and their approximately 2 million followings, we used Twitter’s REST API to collect that user’s 3,200 most recent posts (self-tweets and retweets; the limitation of 3,200 tweets is imposed by Twitter), in addition to some descriptive statistics. We limited our collection to English tweets. For each user, we then removed tweets that had been created more than 6 months before the actual collection date, resulting in a data set that, for most users, consisted of 6 months’ worth of tweets<sup>8</sup> (see Table 1, leftmost column, for the time span statistics). For each core user, we then used the followings’ tweets to construct the user’s home timeline—the tweets the user received (see Appendix B for complete details).

Table 1 (left column) presents descriptive statistics of our core users.

## Expert Users: Selection and Data Collection

We define expert users as individual bloggers on prominent blog sites who also have Twitter accounts and large numbers of followers; this definition was motivated by the rationale that such users are likely to have greater expertise in using the platform to promote themselves, such as for personal branding purposes, as compared with casual Twitter users. To identify such expert users, we first identified 12 blogging websites (see Appendix C for the complete list of websites). Second, we manually identified lists from the websites’ Twitter pages that contained the Twitter accounts of the bloggers. For example, Huffington Post’s Twitter account includes many lists, among them a list of “Tech-politics bloggers.” Appendix C includes a description of the lists we collected for each blog.

Using Twitter’s REST API, we then collected the user profiles of the members in each of the lists we identified. Among these users, we selected only those who met the following two conditions: First, the user’s Twitter profile description had to contain at least one of the following words—write, report, blog, journal, editor, column, correspondent or tweets— assuming those words indicate the user is an actual blogger. Second, the user’s number of followers had to be larger than 1,000. The latter condition implied that, based on a random sample of 43,918 Twitter users, the user was in the top 25% percent of users with the largest number of followers. This process resulted in the selection of 530 expert users. As with the core users, some expert users were filtered out in the data collection process due to their privacy settings or in cases where, following our language processing scheme (described below), the user’s collection of tweets was empty. Our final data set of expert users comprised 464 users.

Finally, to confirm that each expert account indeed corresponded to a real-life user and not to a service or product, we ran a survey on Amazon Mechanical Turk (MTurk) in which we asked workers whether each blogger account reflected a company or an actual person. Each blogger account was examined and graded by three unique workers. Roughly 99% of the accounts were identified as belonging to an individual person by at least one MTurk worker, and 94% were identified as such by at least two workers. We say that an account represents an actual person if at least two of the workers marked it as such. This step provided us with additional assurance that our sample comprised actual people and not commercial accounts. Details about the survey and its operationalization can be found in Appendix D.

<table><tr><td colspan="3">Table 1. Descriptive Statistics</td></tr><tr><td></td><td>Core Users</td><td>Expert Users</td></tr><tr><td>Followings count(Mean)(Median)</td><td>653503</td><td>1,4791,190</td></tr><tr><td>Followers count(Mean)(Median)</td><td>838623</td><td>49,7006,411</td></tr><tr><td>Followings of Followings count(Mean)(Median)</td><td>2,221483</td><td>3,165743</td></tr><tr><td>Followers of Followings count(Mean)(Median)</td><td>17,996717</td><td>53,2912,089</td></tr><tr><td>Self-tweet count(Mean)(Median)</td><td>468.49380</td><td>493.33323</td></tr><tr><td>Retweet count(Mean)(Median)</td><td>649.99496</td><td>344.75176</td></tr><tr><td>Over 6 months&#x27; worth of data</td><td>72%</td><td>87%</td></tr><tr><td>Over 5 months&#x27; worth of data</td><td>78.8%</td><td>90.7%</td></tr><tr><td>Over 5 months&#x27; worth of data</td><td>86.1%</td><td>95.7%</td></tr><tr><td>Over 3 months&#x27; worth of data</td><td>93.7%</td><td>98.3%</td></tr><tr><td>Over 2 months&#x27; worth of data</td><td>99.4%</td><td>100%</td></tr></table>

We carried out a data collection process similar to that described for the core users in order to obtain 6 months’ worth of historical data for both the expert users and their approximately 700,000 followings. Table 1 (rightmost column) presents the time span activity for the expert users. Table 1 (rightmost column) presents descriptive statistics of the data for the expert users.

## Identification

In this section, we outline our identification strategy. For the sake of clarity, we reiterate our definitions of the three types of user personas discussed above:

(1) A user’s self-produced persona is the set of his selftweets.

(2) A user’s retweeted persona is the set of tweets the user retweeted.

(3) A user’s full persona is the union of the user’s selftweets and the user’s retweets.

As our focus in this study is on impression management and personal branding, our empirical identification strategy focuses on accounting for other known influences and motivations for retweeting. Specifically, we control for exposure bias, social dynamics (reciprocity, tie strength, and source popularity), and tweet characteristics that influence a tweet’s likelihood of being shared (tweet popularity and inherent “retweetability”); by controlling for tweet popularity, along with tie strength, we also take into account the need for uniqueness.

## General Description of Strategy and the Approach to Control for Exposure Bias

Our purpose is to compare the user’s self-produced persona with his retweeted persona, as well as with his full persona, in terms of the topics discussed. However, simply comparing the retweeting behavior of each user to the user’s selftweeting behavior reveals only limited information. Suppose, for example, that we find that a user adds three new topics via retweets. How should we determine whether or not this addition is substantial, and more than we might expect? To identify whether an addition is indeed significant, it is necessary to identify a reference against which the user’s retweeting behavior can be meaningfully compared. A naïve option might be to randomly draw tweets from the entire Twittersphere and compare the topics in that sample to the topics in each user’s retweeted persona. Yet, this reference sample neglects a critical concern: selection bias (discussed at length in the “Theoretical Development” section), in which the subset of tweets from which a user can select content to retweet diverges, in terms of its content, from a random selection of tweets. As discussed above, exposure bias driven by homophily is the form of selection bias that is relevant to the current investigation. Given that users tend to follow others who are similar to themselves, it is possible that the content to which they are exposed (i.e., the topics in the tweets the users can readily retweet) bears a strong resemblance to the content the user discusses in her self-tweets. Accordingly, a random sample of tweets from the Twittersphere may not reflect the topics to which a user is in fact exposed.

This reasoning suggests that, for each user, we need to build an individual, user-specific reference set of retweets that is derived from the tweets the user has actually received (i.e., tweets that were tweeted or retweeted by Twitter users the focal user follows). It is important to note that, in constructing this baseline, we are not interested in capturing the maximal or minimal number of new topics that a user can possibly retweet about. Rather, we aim to construct a set of tweets that is representative of the tweets the user could have retweeted had he generated the same number of retweets but chosen them randomly from his incoming tweets (i.e., not allowing his preferences to favor any subset of those tweets and their corresponding topics over others). Accordingly, for each core user u, we construct an additional persona, henceforth referred to as the random retweeted persona. This persona comprises the same number of retweets that u actually posted, but drawn uniformly at random from the tweets (retweets and self-tweets) posted by u’s followings (recall that we collected all tweets posted by every user’s followings, thereby recreating each user’s home timeline), and that u is likely to have seen.

In generating the random retweeted persona, we take into account the possibility that a user may not see all tweets in her timeline. A user’s followings might generate hundreds of tweets per day, and a user who accesses the platform after even an hour of inactivity might not scroll through all the tweets that were posted while she was away. Accordingly, we limit our pool of tweets such that we sample only those tweets that the user is likely to have seen: For each action (retweet, self-tweet, or reply) performed by u, we take the latest 15 tweets generated by u’s followings.<sup>9</sup> We then draw uniformly at random from these tweets only. Complete details on how the random retweeted persona is constructed are outlined in Appendix E.

Our main analysis relies on a random retweeted persona that controls for exposure bias in this manner. To elucidate how other factors might influence users’ retweeting behavior, we construct additional random retweeted personas that, beyond controlling for exposure bias, introduce further constraints; these will be detailed in what follows. We rerun our analyses using each of these versions of the random retweeted persona.

## Social Dynamics

We account for the different dimensions of social dynamics through the construction of five different types of random retweeted personas: one that controls for reciprocity; three that control for tie strength; and one that controls for source popularity. Below, we discuss each in turn.

## Random Retweeted Persona Controlling for Reciprocity

To account for reciprocity—a user’s propensity to retweet tweets from others who have retweeted him—we use a stratified sampling technique, in which we sample in a way that maintains the proportion of reciprocal retweets and nonreciprocal retweets. For example, consider a user who retweeted 10 tweets from users who previously retweeted him (reciprocal retweets) and 45 tweets from users who did not previously retweet him (nonreciprocal retweets). When sampling random retweets to construct that user’s random retweeted persons, we sample 10 tweets that were posted by users who previously retweeted the user and 45 tweets that were posted by users who did not previously retweet the user.

## Random Retweeted Persona Controlling for Tie Strength

To control for the possibility that users might prefer to retweet content they receive from close friends (strong ties) or, alternatively, from weak ties (as a means, for example, of promoting new knowledge to their networks; Shi et al. 2014), we construct three types of baseline random retweeted personas to account for tie strength. Each relies on stratified sampling, such that the distribution of tie strength exhibited in the retweets will be maintained in the random retweeted persona. For example, if a user retweeted 10 tweets from strong ties and 20 tweets from weak ties, when sampling the random retweets, we sample 10 random retweets from strong ties and 20 random retweets from weak ties.

The three baselines that control for tie strength differ in how strong and weak ties are defined. The first defines tie strength solely on the basis of link relationships (who follows whom), whereas the other two add a level of interaction to the definition (who mentioned whom; or who replied to whom). We provide complete details of the different definitions in Appendix F.

## Random Retweeted Persona Controlling for Source Popularity

To account for the popularity of a tweet’s source (author), we construct a random retweeted persona using a stratified sampling technique based on each user’s number of followers, such that the distribution of source popularity exhibited in the retweets will be maintained in the random retweeted persona. Specifically, we divide each user’s actual retweets into quartiles according to the number of followers the tweet’s original author has. Then, in constructing the random retweeted persona, we sample tweets from the user’s followings according to these quartiles. For example, if 25% of the user’s actual retweets originated from users with fewer than 600 followers, then 25% of the randomly sampled tweets in the random retweeted persona will originate from users who have fewer than 600 followers.

## Tweet Characteristics

We control for two dimensions of tweet characteristics: tweet popularity and inherent retweetability.

## Tweet Popularity

For this analysis, we define a tweet’s popularity as the number of times it has been retweeted. When creating each user’s random retweeted persona, we employ a stratified sampling technique, such that the distribution of tweet popularity exhibited in the retweets will be maintained in the random retweeted persona. Specifically, we partition each user’s actual retweets into quartiles according to the number of retweets for the original tweet. We then sample tweets from the user’s followings according to these quartiles. For example, if 25% of the users’ actual retweets have fewer than 15 retweets, then 25% of the random retweets sampled will also have fewer than 15 retweets.

## Retweetability

Some tweets may be inherently less likely to be retweeted, such as messages with very specific personal content (e.g., “it’s my birthday!”). To control for this bias, we produce another random retweeted persona, where we draw the random retweets only from the retweets of u’s followings (as opposed to the followings’ retweets and self-tweets). The underlying assumption is that tweets that have been found to be worthy of retweeting by at least one user (the core user’s following) have some degree of general appeal and are therefore more likely to be retweeted than the following’s own self-tweets, which may not be of broader interest.

## Document Construction and Topic Modeling

Our next step was to transform each user’s self-produced, retweeted, and random-retweeted personas into quantitative metrics that could be analyzed. We achieved this using the Latent Dirichlet Allocation (LDA) topic modeling approach. LDA was first introduced by Blei et al. in 2003 and is presently the most common topic-modeling algorithm (Shi et al. 2016).<sup>10</sup> Before running LDA on our collected data, we needed to carry out two additional preliminary steps. First, in accordance with prior work, we grouped tweets into documents; second, we performed analysis to choose the number of topics to be used. We now elaborate on those two steps.

## Operationalizing: Document Construction

Prior work on topic modeling for microblogs (e.g., Hong and Davison 2010; Mehrotra et al. 2013) has established that grouping of tweets (such as by author) prior to applying LDA facilitates topic learning. Because our focus was on the relationship between self-tweeting and retweeting for an individual user, we grouped tweets by author and by type (selftweet versus retweet). Specifically, for each user u in our data set (a core user or an expert), we produced the following text documents:

• SelfTweet containing the texts of all user u’s self-tweets.

• ReTweet containing the texts of all user u’s retweets.

RandomReTweet containing the texts of all user u’s random retweets (that is, the tweets that make up the random-retweeted persona).

This process resulted in 10,164 documents for the 3,388 core users, and 1,392 documents for the 464 expert core users. Prior to grouping the tweets into documents, we applied the Porter stemmer and removed content that did not carry meaning, including stop words, URLs, words containing nonalphanumeric characters, and other content types. We also excluded tweets that contained fewer than three words.

## Operationalizing: Determining the Number of Topics in the Corpus Prior to Running LDA

As mentioned above, the LDA topic modeling approach assumes that the number of topics in the corpus is known and fixed. In order for the analysis of a given corpus to be meaningful, it is necessary to determine the appropriate number of topics for that corpus.

Several data-driven metrics have been proposed to help identify a “good” number of topics for a given corpus of documents. As there is no one dominating method, we used four different methods, all of which produced similar results (based on Arun et al. 2010; Cao et al. 2009; Deveaud et al. 2014; Griffiths and Steyvers 2004). Details about the different methods and analysis of their results are provided in Appendix G. This analysis resulted in a decision to run LDA with 25 topics for the core users’ data set and with 30 topics for a combined data set comprising data for core users and for expert users. Finally, for robustness purposes, we ran the main analyses of the paper (H1 and H2) with 15, 20, 25, 30, and 35 topics. The results were consistent in terms of significance and direction across analyses.

## Running LDA

After constructing the documents, we performed two separate LDA runs: First, in order to address H1 and H2, we applied LDA (with 25 topics) over the 10,164 documents corresponding to the core users. Then, to address H3, we applied LDA (with 30 topics) over the 11,556 documents corresponding to the combined data set of both core and expert users.

The output of each LDA run was a set of 25 topics (or 30 topics), as distributions over words (the main keywords of the topics of our two LDA runs are presented in Appendix H), and a topic distribution vector for each of the documents, where each element in a given vector captures the proportion of the content in the corresponding document attributed to a specific topic. We labeled the vectors produced by the LDA as follows (for an illustration of the document construction and LDA, see Figure 1):

• SelfTweet\_vector<sub>u</sub>: topic distribution of user u’s SelfTweet document.

• ReTweet\_vector<sub>u</sub>: topic distribution of user u’s ReTweet<sub>u</sub> document.

RandomReTweet\_vector : topic distribution of user u’s RandomReTweet document.

Note that, because tweets are of similar length, for each document type (SelfTweet, ReTweet, and RandomRetweet) the corresponding vector can also be interpreted as an estimation of the proportion of tweets that relate to each topic. As an illustration, consider an LDA run with five topics that produced the following SelfTweet\_vector from the user’s SelfTweet document: (0.2, 0.1, 0.01, 0.6, 0.09). We interpret these distributions to mean that 20% of the user’s self-tweets are attributed to topic one, 10% of the user’s self-tweets correspond to topic two, 1% of the user’s self-tweets correspond to topic three, etc.

![](/api/attachments/HDNYXTXS/fulltext/images/d1e7ef75fff3b137e7ebfe253f1660941fab2b11c5a30195f56b27713d0a797c.jpg)  
Figure 1. Illustration of the Steps of the Document Construction and LDA Topic Modeling Process

## Empirical Methodology and Results

## H1: The Extent to which Users’ Retweets Are Consistent with Their Self-Tweets

To evaluate the extent to which users’ retweets are consistent with their self-tweets (a tendency theorized to reflect principles of effective personal branding), we first assess the average number of topics discussed in the user’s retweets (her retweeted persona) that are not included in her self-tweets (her self-produced persona), and as such are added to the user’s full persona via retweeting. We then compare that average to the average number of topics discussed in the user’s random-retweeted persona that are not included in the users’ self-tweets.

For the purposes of this comparison, we need to define what it means for a topic to be meaningfully discussed by a user (i.e., eligible to be included in her persona). We use two complementary approaches to determine whether a topic is meaningfully discussed. The first, counts, method is based on the number of tweets each user posts about a given topic in his self-produced and retweeted personas. This method allows for an absolute comparison between different personas: Two personas differ if they post different numbers of tweets corresponding to particular topics. The second, percentage, method relies on the distribution vectors attained from LDA and on the percentage of tweets attributed to each topic. This method allows for a relative comparison: Two personas differ if they attribute different relative importance to certain topics. As we show below, the two methods produce very similar results.

## The Counts Method

This method assumes that a topic is meaningfully discussed in a given persona if the number of tweets that discuss the topic in that persona exceeds a certain threshold, Th.

For this method we first need to transform the topic distribution vectors produced by LDA into count vectors, which we will use to estimate the number of tweets written about each topic. Recall that the distribution vectors can be interpreted as an estimation of the percentage of tweets in the document that correspond to each topic. Therefore, an estimate of the number of tweets in which a given topic is discussed by a user can be captured by the product of the frequency of the topic within the core user’s tweets and the number of tweets by that user. We therefore take the three topic distribution vectors produced by LDA and compute the following three corresponding count vectors for each core user:

• SelfTweetCount\_vector = SelfTweet\_vector × #selftweets posted by user u

• ReTweetCount\_vector = ReTweet\_vector × #retweets posted by user u

• R a n d o m R e T w e e t C o u n t \_ v e c t o r <sub>u</sub> = RandomReTweet\_vector × #retweets posted by user u

Thus, for example, for an LDA run with five topics, if John’s SelfTweet\_vector is (0.2, 0.1, 0.01, 0.6, 0.09) and he has written 100 self-tweets, we will estimate that there are 20 tweets about topic 1, 10 tweets about topic 2, etc.

Given a threshold Th, we say that a topic is added to the full persona via retweets if it is meaningfully discussed in the user’s retweets (i.e., there are at least Th retweets written about it) and is not meaningfully discussed in the user’s selftweets (i.e., there are fewer than Th self-tweets written about it). Table 2 presents the average number of topics (for different values of the threshold Th: 1, 2, 5, and 10) added by the user’s retweeted persona (Row A), versus the average number of topics added by the user’s random retweeted persona (Row B). Significance was evaluated via a Wilcoxon signed-rank test (Row C). For comparison, Rows D–F specify the average number of topics discussed in the user’s self-produced persona (D), retweeted persona (E), and random-retweeted persona (F).

We find that, on average, users discuss up to 7.58 topics in their self-produced tweets and 5.83 to 8.65 topics in their retweets. While the number of retweets and the number of random retweets are the same, we find that the random retweets include 7.77 to 12.47 topics. Given that the random retweets were only sampled from what the user sees in his home timeline, the latter observation suggests that users limit the range of topics that they retweet about. More importantly, we find that, on average, users only add 1.94 to 2.45 topics using the retweet tool, whereas the random retweets add twice as many: 3.74 to 5.80 topics on average. These results support our first hypothesis (H1), that users limit the span of topics that they choose to retweet, retweeting mostly about topics included in their self-tweets.

We further examine the percentage of retweets and random retweets that correspond to the newly added topics. We find that, on average (for the four different values of Th), 7.39%– 15.83% of actual retweets correspond to newly added topics, whereas 14.99%–22.41% of random retweets correspond to newly added topics. This observation indicates that actual retweets are more likely than random retweets to contribute to topics already being discussed in the self-produced persona (further supporting H1).

To ensure that the average difference in new topics added per user cannot be attributed to a few atypical users, we further evaluate, for each threshold value, the number of core users for whom the number of topics added by random retweets was larger than that added by actual retweets. The results are shown in Figure 2. We observe that, for each threshold value, in more than 72% of instances the random retweeted persona adds at least one more new topic than does the actual retweeted persona, and in more than 50% of cases the random retweeted persona adds at least two more new topics than does the retweeted persona. In other words, most users use the retweet tool in a way that enables them to portray a consistent and cohesive full persona.

## Percentage Method

This method directly utilizes the topic distribution vectors produced by LDA to determine whether a topic is meaningfully discussed by a given persona. For each topic distribution vector for each user u, we implement the following procedure:

1. We order the distribution vector from the most frequently discussed topic to the least.

2. We create a cumulative distribution.

3. Given a threshold Th, we define as meaningfully discussed those topics that account for Th% of the distribution.

For example, assume that Jane has the following topic distribution for her self-tweets—(0.05, 0.20, 0.35, 0.15, 0.25)—and that Th = 80. We thus define topics two, three, and four as being meaningfully discussed because they are the most frequently discussed topics, and together they account for 80% of the topics discussed.

Similarly to the counts method, we say that a user has added a topic to her full persona via retweets (random retweets) if the topic was discussed in the user’s retweets (random retweets) and was not discussed in her self-tweets. In the results reported below (Table 3), we consider different threshold values of 80, 85, 90, and 95.

As shown in Table 3, users add between 1.32 and 1.67 topics using their retweets, whereas their random retweets add between 2.35 and 3.99 new topics. These results are consistent with those obtained using the counts method, and they lend further support to H1.

Table 2. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets—Counts Method

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Threshold</td></tr><tr><td>Th= 1 tweet</td><td>Th = 2 tweets</td><td>Th = 5 tweets</td><td>Th = 10 tweets</td></tr><tr><td>A</td><td>Mean number of topicsaddedvia the retweets</td><td>2.45</td><td>2.30</td><td>2.11</td><td>1.94</td></tr><tr><td>B</td><td>Mean number of topicsaddedvia the random retweets</td><td>5.80</td><td>5.49</td><td>4.62</td><td>3.74</td></tr><tr><td>C</td><td>Wilcoxon signed-rank test on A and B</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td></tr><tr><td>D</td><td>Mean number of topics in self-produced tweets</td><td>7.58</td><td>6.80</td><td>5.66</td><td>4.70</td></tr><tr><td>E</td><td>Mean number of topics in retweets</td><td>8.65</td><td>7.94</td><td>6.84</td><td>5.83</td></tr><tr><td>F</td><td>Mean number of topics in random retweets</td><td>12.47</td><td>11.50</td><td>9.59</td><td>7.77</td></tr></table>

![](/api/attachments/HDNYXTXS/fulltext/images/e713c699c9d62f75bae6e32f8d150722cc53e6010b278d451f01f02732440ea2.jpg)

Figure 2. Difference Between Number of Topics Added by Actual Retweeted Persona Versus Random Retweeted Persona  
Table 3. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets—Percentage Method

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Threshold</td></tr><tr><td>Th = 80%</td><td>Th = 85%</td><td>Th = 90%</td><td>Th = 95%</td></tr><tr><td>A</td><td>Mean number of topics added via the retweets</td><td>1.32</td><td>1.39</td><td>1.51</td><td>1.67</td></tr><tr><td>B</td><td>Mean number of topics added via the random retweets</td><td>2.35</td><td>2.72</td><td>3.22</td><td>3.99</td></tr><tr><td>C</td><td>Wilcoxon signed-rank test on A and B</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr><tr><td>D</td><td>Mean number of topics in self-produced tweets</td><td>3.09</td><td>3.52</td><td>4.12</td><td>5.11</td></tr><tr><td>E</td><td>Mean number of topics in retweets</td><td>3.59</td><td>4.1</td><td>4.77</td><td>5.84</td></tr><tr><td>F</td><td>Mean number of topics in random retweets</td><td>4.92</td><td>5.71</td><td>6.8</td><td>8.48</td></tr></table>

## Accounting for Alternative Motivations for Retweeting

The results presented above suggest that the spectrum of topics discussed in a user’s retweets tends to resemble that of her self-tweets rather than to add diversity. Our identification strategy—comparison of the actual retweeted persona to the benchmark of the random retweeted persona—indicates that this tendency reflects a choice made by users rather than an artifact of exposure bias. Our next step is to confirm that users’ behavior is driven by image-related and personal branding considerations, rather than by additional factors that might influence the spectrum of topics that users retweet about. Accordingly, we rerun our analyses using the random retweeted personas that we constructed as benchmarks to control for such factors. As described in the “Identification” section, these benchmarks include five personas controlling for social dynamics (reciprocity, tie strength, and source popularity) and two personas covering tweet characteristics (tweet popularity and inherent retweetability). The procedures used for data processing, language processing (including an LDA analysis for the newly constructed documents), and statistical analyses are the same as those described above. The results of all of these analyses are similar in significance, direction, and magnitude to the results reported above (for the results see Appendix I).

## Discussion of H1

Taken together, the results support H1: When shaping their online personas, users tend to adhere to principles of personal branding and to retweet content that refers to topics discussed in their self-tweets rather than to retweet about new topics. In other words, they enhance the depth of their personas rather than the breadth as a means of retaining consistency and conveying authenticity. Our identification strategy, which controls for multiple factors that might influence the scope of topics that users retweet about, lends robustness to our theory that the phenomenon observed can indeed be attributed to image-related and personal branding considerations.

Additional robustness analyses provide further support to H1, showing that, beyond the fact that users add few topics, the topics that a user does add are comparatively similar to his or her self-produced topics (see Appendix J).

## H2: Attention Redistribution

In this section, we empirically study H2, which asserts that users use their retweets in a way that preserves the underlying distribution of topics in their self-tweets. Our analysis in this case entails investigating whether the distribution of tweets across different topics differs between a user’s self-tweets and her full persona (the union of a user’s self-tweets and retweets). Consider, for example, an instance where a user’s self-tweets focus exclusively on five topics (i.e., there are five meaningfully discussed topics in the user’s self-tweets): topics a, b, c, d, and e, and where the two most discussed topics are topics a and b. We examine the user’s full persona to determine whether, as hypothesized, the relative proportions of the topics remain roughly the same, or whether the distribution of content across the topics changes significantly.

In this analysis, we no longer compare retweets (random retweets) to self-tweets, but rather, we compare the topic distribution of the self-tweets to that of the full persona (random full persona).

Formally, we compare the following two personas:

Full persona: comprises the user’s self-produced persona (that is, her self-tweets) and her retweeted persona (that is, her retweets).

Random full persona: comprises the user’s self-produced persona as well as her random-retweeted persona (i.e., the tweets previously selected as her random retweets).

To construct a topic distribution vector for the full persona and the random full persona for a given user u, we consider the three topic distribution vectors produced by the LDA: S e l f T w e e t \_ v e c t o r <sub>u</sub> , R e T w e e t \_ v e c t o r <sub>u</sub> a n d RandomReTweet\_vector . We compute the topic distribution of the full persona (random full persona) as the weighted mean of the topic vectors of the self-tweets and the retweets (random retweets). Formally (the difference between the two personas is highlighted in bold):

$$
\begin{array}{l} \text {FullPersona\_vector} _ {u} = \\ \frac {\text {SelfTweet\_vector} _ {u} * \text {NumberOfSelfTweets} _ {u} + \text {ReTweet\_vector} _ {u} * \text {NumberOfRetweets} _ {u}}{\text {NumberOfSelfTweets} _ {u} + \text {NumberOfRetweets} _ {u}} \end{array}
$$

$$
\begin{array}{l} \text {RandomFullPersona} _ {\text {vector} _ {u}} = \\ \frac {\text {SelfTweet\_vector} _ {u} * \text {NumberOfSelfTweets} _ {u} + \text {RandomReTweet\_vector} _ {u} * \text {NumberOfRetweets} _ {u}}{\text {NumberOfSelfTweets} _ {u} + \text {NumberOfRetweets} _ {u}} \end{array}
$$

Next, for each user, we measure the extent to which the topic distribution corresponding to self-tweets is similar to that of the full persona and to that of the random full persona. We compute dissimilarity between the topic distributions using J-S divergence (see in Appendix J),<sup>11</sup> which results in a number between 0 and 1, where 0 reflects identical probabilities, and 1 reflects orthogonal probabilities.

For each user u we measure J-S divergence between the following two pairs of personas:

• SelfTweet\_vector and FullPersona\_vector, henceforth referred to as observed divergence.

• SelfTweet\_vector and RandomFullPersona\_vector, henceforth referred to as baseline divergence.

We find that the average observed divergence is 0.076 (median 0.059), indicating that, in absolute terms, the topic distribution in a user’s self-tweets is highly similar to the topic distributions in the user’s full persona. We further find that the baseline divergence is 0.086 (median 0.073), which is significantly higher (significance was evaluated via a Wilcoxon signed-rank test; p < .001), indicating lower similarity.

To understand the practical significance of this 0.010 difference between the observed and baseline divergences measured above, we conducted a simulation experiment that aims to answer the following question: What proportion of the user’s retweeting should be on a topic drawn uniformly at random to move away from the observed divergence to the baseline divergence, and thereby produce the 0.010 difference above? Through this experiment, we aimed to capture the extent of random retweeting choices (where the user is agnostic with regard to the topics of her retweets) required to transform the user’s observed retweeting behavior to produce the baseline divergence. As we show below, we find that this corresponds to 10% of the user’s retweets, a rather substantial proportion.

Specifically, we ran the following simulation:

1. We calculated the J-S divergence between each user’s self-tweets and her full persona, and the J-S divergence between the user’s self-tweets and her random full persona (the baseline divergence).

2. For different values of X, we took X% of the user’s retweets and redistributed them equally between the different topics. That is, we simulated what would happen if X% of the retweets were drawn randomly from a uniformly distributed set of topics.

3. We identified the value of X such that the resulting J-S divergence between the user’s self-tweets and the simulated full persona created in step 2 above is equal to the baseline J-S divergence.

Recall that the goal of this process was to answer the question: how much random retweeting does it take to move from actual retweeting behavior to the random baseline? Put differently, how far away from random is the actual retweeting of the users in our dataset? Figure 3 presents the results. The x-axis depicts different values of X (the percentage of random, topic-agnostic, retweeting), and the y-axis presents the resulting J-S divergence between the user’s selftweets and the simulated full persona. As shown in Figure 3 (the darkest dot), we find that to achieve our average baseline divergence, 10% of a user’s retweets ought to be redistributed uniformly across topics. Thus, the observed difference between the observed and baseline divergences has practical significance, and it reflects a substantial (10%) difference in the level of random/agnostic retweeting behavior.

Again, to account for alternative motivations for retweeting, the analysis in this section is repeated for each type of random retweeted persona described in the “Identification” section above. The results are similar in significance and direction.

The results of our analyses support H2, suggesting that users preserve the underlying distribution of topics in their selftweets when retweeting, and they strengthen our general premise that this behavior is driven by image-related considerations.

## H3: Comparing the Retweeting Behavior of Expert and Core Users

In this section, we empirically test H3, which asserts that, compared with core users, expert users demonstrate a more unified presentation of themselves. Specifically, we test H3 in two stages. We first repeat the analysis conducted for H1 and H2 using the data set collected for expert users. Then, we compare the results of the analyses with those corresponding to core users.

Note that the results in this section are based on distribution vectors obtained from running LDA on a combined data set of both the core users and the expert users (with 30 rather than 25 topics, as explained above). This means that when we compare the results for the two types of users, there is a possibility that the quantitative results for the core users might differ slightly from those presented in our analysis of H1 (although they are clearly in the same direction and have similar significance), given that they are obtained from a different LDA run that includes additional documents. However, as can be seen below, the results obtained for the core users are very similar to those reported for H1.

![](/api/attachments/HDNYXTXS/fulltext/images/f6bf17ccf6d901b4b03557ed48d1c1a3c72952e00bfabfe35f83505380334522.jpg)  
Figure 3. Meaning of Attention Redistribution Simulation Results

## Behavior Analysis for Expert Users

The results for H1 for expert users are reported in Tables 4 and 5, and are similar in their direction to the results presented for core users: When considering the counts method (Table 4), we find that, on average, expert users introduce 0.53 to 1.56 new topics through their retweeting activity. Experts’ random-retweeted personas add significantly higher numbers of new topics (between 1.27 and 4.13 on average). When considering the percentage method (Table 5), we see the same tendency: Experts’ retweeted personas add between 0.72 and 1.43 new topics, whereas their random-retweeted personas add between 1.45 and 3.46 new topics.

With regard to H2, we find that expert users, like core users, do not use their retweets to change the relative distributions of topics in their self-tweets. Analysis of the dissimilarity between topic distributions yields results in the same direction as the results obtained for the core users: We find that the average J-S divergence value between the topic distributions of the self-produced persona and of the full persona is 0.023, whereas the average J-S divergence value between the selftweets and the random full persona is 0.036. (Significance was evaluated via a Wilcoxon signed-rank test; p < 0.001.)

These results support H3 by showing that, on average, expert users, like core users, maintain full personas that are very similar to their self-produced personas.

## Comparing Experts and Core Users

When comparing expert users and core users in terms of numbers of topics they add via retweets (H1), we observe that, in line with H3, the tendency to add few topics is more pronounced among expert users. Specifically, whereas core users add 2.05 to 2.81 new topics according to the counts method, and 1.37 to 1.82 topics according to the percentage method, experts add only 0.53 to 1.56 new topics (counts) or 0.72 to 1.43 (percentage).

One should note that the comparison based on the counts method should be interpreted with caution. By definition, the counts method relies on the number of self-tweets and retweets posted by the user. Accordingly, users who tweet more frequently have the potential to discuss more topics, and those who retweet more often have the potential to add more topics. This means that we can only compare the results of core users and experts if we believe that the two groups are similar to each other in terms of the numbers of tweets and retweets they post. This, however, does not seem to be the case. The average numbers of self-tweets and retweets of core users are 468.49 and 649.99, respectively, whereas the average numbers of self-tweets and retweets of experts are 493.33 and 344.75, respectively. Unfortunately, we have no way of controlling for this bias in our analyses. However, comparison based on the percentage method, which does not rely on the number of tweets posted, enables us to assert that expert Twitter users indeed add fewer topics compared with core users and as such present more unified personas.

Next, we compare expert users and core users in terms of the distribution of attention across topics discussed (H2). We observe that, on average, the distance between expert users’ self-tweets and their full personas (average J-S divergence is 0.023; median 0.013) is lower than the corresponding distance for core users (average J-S divergence is 0.078; median 0.06). Next, for both experts and core users, we compute the average ratio between (1) the J-S divergence of the self-tweets and the full persona and (2) the J-S divergence of the self-tweets and the random full persona. We find that this ratio is 1.48 for the core users and 2.73 for the experts.

When considering the practical interpretation of these results, using the simulation described above, we find that the J-S divergence difference for the core users is consistent with that obtained in our previous analysis, and corresponds to a redistribution of approximately 10% of retweets. For the experts the J-S divergence difference is more substantial and corresponds to a redistribution of approximately 15% of retweets. These results further strengthen our hypothesis, by showing that the J-S divergence difference for of expert users is more meaningful. Taken together, our results indicate that, on average, compared with core users, experts show greater similarity between their self-tweets and their full personas. These observations, coupled with our observation that expert users use the retweet option less frequently compared with core users (indicating that they rely to a greater extent on their own words when shaping their personal brands), support our hypothesis (H3) that the tendency to present a consistent persona is stronger among expert users.

Table 4. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method

<table><tr><td colspan="6">Random Retweets: Counts Method</td></tr><tr><td rowspan="2" colspan="2"></td><td colspan="4">Threshold</td></tr><tr><td>Th= 1 tweet</td><td>Th = 2 tweets</td><td>Th = 5 tweets</td><td>Th = 10 tweets</td></tr><tr><td>A</td><td>Mean number of topicsaddedvia the retweets</td><td>1.56</td><td>1.21</td><td>0.81</td><td>0.53</td></tr><tr><td>B</td><td>Mean number of topicsaddedvia the random retweets</td><td>4.13</td><td>3.25</td><td>2.14</td><td>1.27</td></tr><tr><td>C</td><td>Wilcoxon signed-rank test on A and B</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td><td>p&lt; 0.001</td></tr><tr><td>D</td><td>Mean number of topics in self-produced tweets</td><td>7.67</td><td>6.69</td><td>5.28</td><td>4.30</td></tr><tr><td>E</td><td>Mean number of topics in retweets</td><td>6.81</td><td>5.76</td><td>4.36</td><td>3.35</td></tr><tr><td>F</td><td>Mean number of topics in random retweets</td><td>9.82</td><td>8.14</td><td>5.84</td><td>4.11</td></tr></table>

Table 5. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td rowspan="2" colspan="2"></td><td colspan="4">Threshold</td></tr><tr><td>Th = 80%</td><td>Th = 85%</td><td>Th = 90%</td><td>Th = 95%</td></tr><tr><td>A</td><td>Mean number of topics added via the retweets</td><td>0.72</td><td>0.83</td><td>1.03</td><td>1.43</td></tr><tr><td>B</td><td>Mean number of topics added via the random retweets</td><td>1.45</td><td>1.88</td><td>2.53</td><td>3.46</td></tr><tr><td>C</td><td>Wilcoxon signed-rank test on A and B</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr><tr><td>D</td><td>Mean number of topics in self-produced tweets</td><td>3.04</td><td>3.52</td><td>4.21</td><td>5.4</td></tr><tr><td>E</td><td>Mean number of topics in retweets</td><td>3.05</td><td>3.52</td><td>4.19</td><td>5.42</td></tr><tr><td>F</td><td>Mean number of topics in random retweets</td><td>3.87</td><td>4.65</td><td>5.8</td><td>7.72</td></tr></table>

## Conclusion

Theories of impression management and identity signaling suggest that users have a need to signal certain identities to others and that their choices are influenced by how they wish to be perceived by others. For example, the consumer behavior literature shows that individuals adopt or abandon certain products to signal desired identities. When considering computer-mediated communications, such as social media and social networks, content contribution and knowledge sharing become an integral part of how users signal their desired identities and consequently build their personal brands. As elaborated above, research in this domain suggests that presenting a consistent persona conveys authenticity and is, therefore, an effective personal branding strategy. In our paper, we turn to these principles of personal branding to explain user sharing behavior. We show that these principles are reflected in users’ behavior when they use reiteration tools on social media platforms—platforms that provide users with unprecedented opportunities, and designated technologies, to manage how the world perceives them. To our knowledge, our work is the first to link research on content contribution behavior in social media and, specifically, usage of reiteration tools, with theories on personal branding (Labrecque et al. 2011; Peng et al. 2018; Shi et al. 2014; Toubia and Stephen 2013). We connect the streams in showing that Twitter users, who are likely to be motivated by image and identity signaling considerations, contribute and rebroadcast content in a way that reflects an effort to maintain a consistent persona, as recommended by personal branding theories.

Relying on LDA topic modeling, we analyzed data from 3,388 Twitter core users and their approximately 2 million followings, as well as from 464 expert users and their approximately 700,000 followings. In our analyses, we introduced a novel approach to control for exposure bias (driven by homophily), based on generating user-specific reference personas against which to compare each user’s actual behavior. We further controlled for multiple alternative factors that are known to influence retweeting behavior, including social dynamics and tweet characteristics. Our analyses produced empirical support for our three hypotheses, which converge to the general premise that, when retweeting, users tend to maintain personas that are consistent with their self-produced personas, in terms of the topics they discuss and the distributions of those topics (H1 and H2). We further showed that the tendency to produce a consistent, unified persona is more prominent among expert users than among core users (H3).

## Managerial Implications

Our findings provide insights regarding how users share information on social media platforms such as Twitter; an understanding of such behavior is a prerequisite for managers who seek to devise efficient social media strategies and optimize their engagement with consumers on these platforms. We find, for example, that users tend to retweet content about topics with which they are familiar (in terms of being able to produce content about those topics), meaning that they add few new topics, and the topics they do add are relatively similar to those they discuss in their self-tweets. This observation can inform the design of messages to facilitate the propagation of information and content.<sup>12</sup> This is especially important as personalized messages and targeted marketing are growing in popularity.

From the platform perspective, our work suggests that promoting content that resembles the user’s self-produced content (in terms of topics discussed) may increase sharing and thus contribute to the platform ecosystem. Additionally, our insights regarding users’ tweeting and retweeting behavior, as reflected in topics discussed, can inform the design of platforms’ recommendation tools, such as recommendations regarding whom to follow and selections of tweets to feature more prominently in a user’s feed.

Beyond providing managerial insights, our work can also guide users who strive to use social media platforms to promote themselves. Our analysis indicates that expert users have a particularly strong tendency to rely on their own words and to present a consistent and unified persona on Twitter. Although determining causal relationships between topic reiteration behavior and various metrics of success on Twitter is beyond the capacity of our data (see the discussion of this limitation below), it is possible that expert users’ adherence to a consistent persona reflects their belief in the potential of this strategy to lead to “success” on the platform, suggesting that other users might benefit from emulating it.

## Limitations and Path Forward

We acknowledge that our work is not without limitations. First, our analysis in this paper was done using a snapshot of users’ Twitter activity: 6 months of user timeline data. While this data set was sufficient to provide insight regarding the behaviors at the focus of our investigation, it did not enable us to control for the effects of time on the evolution and construction of an online persona. Likewise, it prevented us from studying the interplay between each user’s self-tweets and retweets over time. Further, a snapshot analysis prevents us from being able to untangle the causality mechanism driving the relationship between the way in which users present themselves on Twitter and various metrics of success. Access to a more complete set of panel data of users’ behavior might allow for exploration of this causality mechanism. We therefore believe that future work should focus on obtaining and analyzing a comprehensive panel data set that includes all, or most, activity of Twitter users, starting the moment they create their accounts. As Twitter’s REST API does not allow for the collection of such data retroactively, this could be done in one of two ways: either by purchasing data, or by targeting new Twitter users and following their activity from their arrival date.

Second, with regard to our identification method, while we are able to account for various alternative influences and motivations affecting retweeting behavior, we cannot directly account for individuals’ inherent interest in certain topics. We suggest, however, that while users are clearly more likely to retweet content in which they are interested, there is no reason to assume that their likes and interests are confined to the set of topics they are able to create content about. Thus, while some of the similarity we observe might be attributable to this alternative explanation, we believe that the more likely interpretation of our findings is that users limit the topics of their retweets because of image-related and personal branding considerations.

Third, our identification strategy cannot fully control for individuals who retweet for the sole purpose of increasing their numbers of followers, which, in turn, can convey information regarding users’ reputation and status (Levina and Arriaga 2014). We note, however, that the motivation to attract new followers is partially addressed in our controls for in-platform social dynamics, and particularly reciprocity. Additionally, it seems likely that retweeting behavior with the sole purpose of attracting new followers would be characterized by dissemination of content created by many different users on a relatively broad range of potentially unrelated topics. Given that our empirical analysis shows that users tend to retweet content about a relatively narrow range of topics, we believe that a desire to attract new followers is not the sole (or strongest) motivator for retweeting.

Finally, our study focuses on one social network: Twitter. It seems reasonable to assume that our results can be generalized to other social media networks whose link structure and broadcasting features are similar to those of Twitter. However, there are other types of social networks that have different purposes, goals, link structures, and features. One example is the professional social network, which is characterized by clear and observable utility goals. We think that future work should focus on studying persona construction in these types of networks.

## Acknowledgments

We would like to thank the senior editor, the associate editor, and three reviewers for their constructive and insightful comments and suggestions. We also thank participants of 2015 Symposium on Statistical Challenges in Electronic Commerce Research, the 2016 International Conference on Information Systems, and the 2017 Conference on Information Systems and Technology for their valuable comments and feedback. Additionally, we would like to thank Karen Marron for her editorial assistance. This study benefitted from the support of the Israel Science Foundation (ISF grant #0612015762), the Kadar Family Foundation and the Henry Crown Institute of Business Research in Israel.

## References

Aral, S., Muchnik, L., and Sundararajan, A. 2009. “Distinguishing Influence-Based Contagion from Homophily-Driven Diffusion in Dynamic Networks,” Proceedings of the National Academy of Sciences (106:51), pp. 21544-21549

Arun, R., Suresh, V., Veni Madhavan, C. E., and Narasimha Murthy, M. N. 2010. “On Finding the Natural Number of Topics with Latent Dirichlet Allocation: Some Observations,” in Advances in Knowledge Discovery and Data Mining, M. J. Zaki, J. X. Yu, B. Ravindran, and V. Pudi (eds.), Berlin: Springer, pp. 391-402.

Back, M. D., Stopfer, J. M., Vazire, S., Gaddis, S., Schmukle, S. C., Egloff, B., and Gosling, S. D. 2010. “Facebook Profiles Reflect Actual Personality, Not Self-Idealization,” Psychological Science (21), pp. 372-374.

Bakshy, S., Messing, S., and Adamic, L. 2015. “Exposure to Ideologically Diverse News and Opinion on Facebook,” Science (348:6239), pp. 1130-1132.

Bapna, R., and Umyarov, A. 2015. “Do Your Online Friends Make You Pay? A Randomized Field Experiment on Peer Influence in Online Social Networks,” Management Science (61:8), pp. 1902-1920.

Barberá, P., Jost, J. T., Nagler, J., Tucker, J. A., and Bonneau, R. 2015. “Tweeting From Left to Right: Is Online Political Communication More Than an Echo Chamber?,” Psychological Science (26:10), pp.1531-1542

Bi, B., and Cho, J. 2016. “Modeling a Retweet Network via an Adaptive Bayesian,” in Proceedings of the 25<sup>th</sup> International Conference on the World Wide Web, pp. 459-469

Berger, J. 2014. “Word of Mouth and Interpersonal Communication: A Review and Directions for Future Research,” Journal of Consumer Psychology (24:4), pp. 586-607.

Berger, J., and Heath, C. 2007. “Where Consumers Diverge from Others: Identity Signaling and Product Domains,” Journal of Consumer Research (34:2), pp. 121-134.

Berger, J., and Heath, C. 2008. “Who Drives Divergence? Identity-Signaling, Outgroup Dissimilarity, and the Abandonment of Cultural Tastes,” Journals of Personality and Social Psychology (95:3), pp. 593-607

Blei, D. M., Ng, A. Y., and Jordan, M. I. 2003. “Latent Dirichlet Allocation,” Journal of Machine Learning Research (3), pp. 993-1022.

Boyd, D., Golder, S., and Lotan, G. 2010. “Tweet, Tweet, Retweet: Conversational Aspects of Retweeting on Twitter,” in Proceedings of the 43<sup>rd</sup> Hawaii International Conference on System Sciences, Washington, DC: IEEE Computer Society.

Cao, J., Xia, T., Li, J., Zhang, Y., and Tang, S. 2009. “A Density-Based Method for Adaptive LDA Model Selection,” Neurocomputing—16th European Symposium on Artificial Neural Networks 2008, pp. 1775-1781.

Chandler, D. and Munday, R., 2016, A Dictionary of Social Media, Oxford, UK: Oxford University Press.

Chen, C.-P. 2013. “Exploring Personal Branding on YouTube,” Journal of Internet Commerce (12:4), pp. 332-347.

Chiang, J. K. H., and Suen, H. Y. 2015. “Self-Presentation and Hiring Recommendations in Online Communities: Lessons from LinkedIn,” Computers in Human Behavior (48), pp. 516-524.

Del Vicario, M., Scala, A., Caldarelli, G., Stanley H. E., and Quattrociocchi, W. 2017. “Modeling Confirmation Bias and Polarization,” Scientific Reports (7), Article 40391.

Deveaud, R., SanJuan, E., and Bellot, P. 2014. “Accurate and Effective Latent Concept Modeling for Ad Hoc Information Retrieval,” Document numérique (17:1), pp. 61-84.

Fox, J., and Rooney, M. C. 2015. “The Dark Triad and Trait Self-Objectification as Predictors of Men’s Use and Self-Presentation Behaviors on Social Networking Sites,” Personality and Individual Differences (76), pp. 161-165.

Flaxman, S., Goel, S., and Rao, J. M. 2016. “Filter Bubbles, Echo Chambers, and Online News Consumption,” Public Opinion Quarterly (80), pp. 298-320.

Garrett, R. K. 2009. “Echo Chambers Online? Politically Motivated Selective Exposure among Internet News Users, Journal of Computer Mediated Communication (14), pp.265-285

Griffiths, T. L., and Steyvers, M. 2004. “Finding Scientific Topics,” Proceedings of the National Academy of Sciences (101, Supplement 1), pp. 5228-5235.

Hill, S., Benton, A., and van den Bulte, C. 2013. “When Does Social Network-Based Prediction Work? A Large Scale Analysis of Brand and TV Audience Engagement by Twitter Users,” in Proceedings of the 34<sup>th</sup> International Conference on Information Systems, Milan, Italy.

Holt, D. 2004. How Brands Become Icons: The Principles of Cultural Branding, Boston: Harvard Business School Press.

Ho, J. Y., and Dempsey, M. 2010. “Viral Marketing: Motivations to Forward Online Content,”Journal of Business Research (63:9), pp. 1000-1006.

Hong, L., and Davison, B. D. 2010, “Empirical Study of Topic Modeling in Twitter,” in Proceedings of the 1<sup>st</sup> Workshop on Social Media Analytics, New York: ACM.

Java, A., Song, X., Finin, T., and Tseng, B. 2007. “Why We Twitter: Understanding Microblogging Usage and Communities,” in Proceedings of the 9<sup>th</sup> WebKDD and 1<sup>st</sup> SNA-KDD 2007 Workshop on Web Mining and Social Network Analysis, New York: ACM, pp. 56-65.

Kaputa, C. 2005. UR a Brand! How Smart People Brand Themselves for Business Success, Mountain View, CA: Davies-Black Publishing.

Kayser M. L. 2014. Personal Branding Secrets for Beginners: A Short and Simple Guide to Getting Started with Your Personal Brand, New Delhi: Blue Ink Publishing.

Khedher, M. 2014. “Personal Branding Phenomenon,” International Journal of Information, Business and Management (6:2), pp. 29-40.

Labrecque, L. I., Markos, E., and Milne, G. R. 2011. “Online Personal Branding: Processes, Challenges, and Implications,” Journal of Interactive Marketing (25:1), pp. 37-50.

Leary, M. R., and Kowalski, R. M. 1990. “Impression Management: A Literature Review and Two-Component Model,” Psychological Bulletin (107), pp. 34-47.

Lee, G. M., Qiu, L., and Whinston, A. B. 2017. “A Friend Like Me: Modeling Network Formation in a Location-Based Social

Network,” Journal of Management Information Systems (33:4), pp. 1008-1033.

Levina, N., and Arriaga, M. 2014. “Distinction and Status Production on UserGenerated Content Platforms: Using Bourdieu’s Theory of Cultural Production to Understand Social Dynamics in Online Fields,” Information Systems Research (25:3), pp. 25(3), 468-488.

Lilleker, G. D. 2015. “Interactivity and Branding: Public Political Communication as a Marketing Tool,” Journal of Political Marketing (14:1-2), pp. 111-128

Lovett, M. J., Peres, R., and Shachar, R. 2013. “On Brands and Word of Mouth,” Journal of Marketing Research (50:4), pp. 427-444.

Manago, A. M., Graham, M. B., Greenfield, P. M., and Salimkhan, G. 2008. “Self-Presentation and Gender on MySpace,” Journal of Applied Developmental Psychology (29), pp. 446-458.

Marshall, T. C., Lefringhausen, K., and Ferenczi, N. 2015. “The Big Five, Self-Esteem, and Narcissism as Predictors of the Topics People Write about in Facebook Status Updates,” Personality and Individual Differences (85), pp. 35-40.

Mehrotra, R., Sanner, S., Buntine, W., and Xie, L. 2013. “Improving LDA Topic Models for Microblogs via Tweet Pooling and Automatic Labeling,” in Proceedings of the 36<sup>th</sup> International ACM SIGIR Conference on Research and Development in Information Retrieval, New York: ACM, pp. 889-892.

Montoya, P., and Vandehey, T. 2005. The Brand Called You: The Ultimate Personal Branding Handbook to Transform Anyone into an Indispensable Brand, Peter Montoya Inc.

Mousavi, R., and Gu, B. 2015. “The Impact of Twitter on Lawmakers’ Political Orientation,” in Proceedings of the 48<sup>th</sup> Hawaii International Conference on System Sciences, Washington, DC: IEEE Computer Society.

Murthy, D. 2013. Twitter: Social Communication in the Twitter Age, Hoboken, NJ: Wiley.

Mutz, D. C., and Martin, P. S. 2001. “Facilitating Communication across Lines of Political Difference: The Role of Mass Media,” American Political Science Review(95:1), pp. 97-114.

Oh, O., Agrawal, M., and Raghav, R. H. 2013. “Community Intelligence and Social Media Services: A Rumor Theoretic Analysis of Tweets During Social Crises,” MIS Quarterly (37:2), pp. 123-142.

Parmentier, M. A., Fischer, E., and Reuber, A. R. 2013. “Positioning Person Brands in Established Organizational Fields,” Journal of the Academy of Marketing Science (41), pp. 373-387.

Peng, J., Agarwal, A., Hosanagar, K., and Iyengar, R. 2018. “Network Overlap and Content Sharing on Social Media Platforms,” Journal of Marketing Research (55:4), pp. 571-585.

Peters, T. 1997. “The Brand Called You,” Fast Company (available at https://www.fastcompany.com/28905/brand-called-you).

Quattrociocchi, W., Scala, A., and Sunstein, C. R. 2016. “Echo Chambers on Facebook,” unpublished working paper (available at SSRN: https://ssrn.com/abstract=2795110).

Ramage, D., Dumais, S., and Liebling, D. 2010. “Characterizing Microblogs with Topic Models, in Proceedings of International AAAI Conference on Web and Social Media (ICWSM-10), Washington, DC.

Rein, I. J., Kotler, P., and Shields, B. 2006. The Elusive Sports Fan, Reinventing Sports in a Crowded Marketplace, New York: McGraw-Hill.

Rosenberg, J., and Egbert, N. 2011. “Online Impression Management: Personality Traits and Concerns for Secondary Goals as Predictors of Self-Presentation Tactics on Facebook,” Journal of Computer-Mediated Communication (17:1), pp. 1-18.

Rui, J. R., and Stefanone, M. A. 2013. “Strategic Image Management Online: Self-Presentation, Self Esteem and Social Network Perspectives,” Information, Communication & Society (16:8), pp. 1286-1305.

Schawbel D. 2009. Me 2.0: Build a Powerful Brand to Achieve Career Success, New York: Kaplan Publishing.

Shepherd, I. D. H. 2005. “From Cattle and Coke to Charlie: Meeting the Challenge of Self Marketing and Personal Branding,” Journal of Marketing Management (21), pp. 589-606.

Shi, Z., Lee, G. M., and Whinston, A. B. 2016. “Towards a Better Measure of Business Proximity: Topic Modeling for Industry Intelligence,” MIS Quarterly (40:4), pp. 1035-1056.

Shi, Z., Rui, H., and Whinston, A. B. 2014. “Content Sharing in a Social Broadcasting Environment: Evidence from Twitter,” MIS Quarterly (38:1), pp. 407-426.

Smith, A. N., Fischer, E., and Yongjian, C. 2012. “How Does Brand-Related User-Generated Content Differ Across YouTube, Facebook, and Twitter?,” Journal of Interactive Marketing (26:2), pp. 102-113.

Speed, R., Butler P., and Collins, N. 2015. “Human Branding in Political Marketing: Applying Contemporary Branding Thought to Political Parties and Their Leaders,” Journal of Political Marketing (14:1-2), pp. 129-151

Snyder, C. R., and Fromkin, H. L. 1980. Uniqueness: The Human Pursuit of Difference, New York: Plenum Press.

Sun, T., Viswanathan, S., and Zheleva, E. 2014. “Impact of Message Design on Online Interactions: An Empirical Investigation,” in Proceedings of the 16<sup>th</sup> International Conference on Electronic Commerce, New York: ACM, pp. 64-71.

Toma, C. L., Hancock, J. T., and Ellison, N. B. 2008. “Separating Fact from Fiction: An Examination of Deceptive Self-Presentation in Online Dating Profiles,” Personality and Social Psychology Bulletin (34), pp. 1023-1036.

Toubia, O., and Stephen, A. T. 2013. “Intrinsic Vs. Image-Related Utility in Social Media: Why Do People Contribute Content on Twitter?,” Marketing Science (32:3), pp. 368-392.

Wasko, M. M., and Faraj, S. 2005. “Why Should I Share? Examining Social Capital and Knowledge Contribution in Electronic Networks of Practice,” MIS Quarterly (29:1), pp. 35-57.

Zhao, S., Grasmuck, S., and Martin, J. 2008. “Identity Construction on Facebook: Digital Empowerment in Anchored Relationships,” Computers in Human Behavior (24), pp. 1816-1836.

## About the Authors

Hilah Geva is a Ph.D. student in the department of Management of Information and Technology at the Coller School of Management at Tel Aviv University. Hilah holds a B.Sc. (magna cum laude) in Computer Science and Cognitive Science from the Hebrew University of Jerusalem and an M.A. (summa cum laude) in Philosophy from Tel-Aviv University. In her research, Hilah focuses on the effects of branding and signaling in online social and economic platforms.

Gal Oestreicher-Singer is a professor of Management of Information and Technology at the Coller School of Management at Tel Aviv University in Israel. She also heads the school’s Management of Information and Technology group. She received her Ph.D. from the Stern School of Business at New York University. Her research focuses on the effects of social media, consumer engagement, and peer influence on electronic commerce outcomes and on the business models of content websites. Her work has been published in the top journals in the fields of both Information Systems and Marketing. She currently serves as a senior editor at MIS Quarterly. She has also been the recipient of several prestigious grants and awards, most recently the ERC grant.

Maytal Saar-Tsechansky is an associate professor of Information, Risk and Operations Management at the McCombs School of Business, The University of Texas at Austin, and a co-founder of Sweetch, a mobile health startup firm. Her research focuses on developing machine learning (ML) and artificial intelligence (AI) methods to improve decision making and to benefit people, organizations, and society. Most of her work aims to augment ML and AI by bringing to bear the problems that machine learning and AI inform in practice and the context in which learning itself occurs, with the goal of effectively dealing with the constraints and taking advantage of the opportunities presented in these environments. Her research integrates business, machine learning, and artificial intelligence, and she has addressed challenges in different domains, including health care, smart electricity grid, fraud detection, finance, and emerging forms of work, such as online labor markets. Maytal received her Ph.D. from New York University’s Stern School of Business. Her research has been published in numerous journals including Journal of Finance, Management Science, Information Systems Research, Journal of Machine Learning Research, and Machine Learning Journal. Maytal’s research has been supported by both government and industry, including the National Science Foundation, SAP, and the Israeli Science Ministry.

# USING RETWEETS WHEN SHAPING OUR ONLINEPERSONA: TOPIC MODELING APPROACH

Hilah Geva and Gal Oestreicher-Singer

The Coller School of Management, Tel-Aviv University, Tel Aviv, ISRAEL {hilahlev@mail.tau.ac.il} {galos@post.tau.ac.il}

Maytal Saar-Tsechansky

McCombs School of Business, University of Texas at Austin, Austin, TX 79712 U.S.A. {maytal@mail.utexas.edu}

## Appendix A

## Robustness Analysis Using an Additional Data Set

All analyses in this paper were done on a data set that was collected in November 2016 (going back 6 months). When analyzing this data set, we assumed that tweets appear in a chronological order. However, in February 2016, Twitter changed the home timeline layout to highlight certain tweets, in which the user is likely to be interested. This means that during our collection period, users were not necessarily presented with tweets in strict chronological order

We control for this potential source of bias by rerunning our main analysis on a previously collected data set. This data set includes tweets of 2,435 core users (and their followings) from September 2015 (going back 6 six), that is, prior to the policy change. All results obtained fo this data set are indeed similar in direction, magnitude, and significance to those obtained from the 2016 data set.

While the 2015 data set circumvents bias related to Twitter’s policy change, it has a different limitation: The filters used to choose the core users were somewhat stricter than those used in the 2016 collection, as follows:

(1) To be included in our 2015 data set, a user had to have posted at least 200 retweets and self-tweets in the 6-month period. Additionally, we filtered out users with fewer than 15 retweets or fewer than 15 self-tweets in each of the three months prior to the date of collection.

(2) We filtered out users with exceptionally high and low (top or bottom 15%) numbers of followers or followings.

While each dataset suffers from its own limitations, these limitations do not overlap, enabling us to suggest that the consistency of our results between the two complementary data sets offers robustness to our results.

Tables A1 to A6 present the main results for H1, H2, and H3 for the 2015 data set.

Table A1. H1: Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method for Core Users Data Set

<table><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.99</td><td>1.88</td><td>1.71</td><td>1.54</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>4.90</td><td>4.60</td><td>3.71</td><td>2.93</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table A2. H1: Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method Core Users Data Set

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.47</td><td>1.55</td><td>1.64</td><td>1.77</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.77</td><td>3.05</td><td>3.39</td><td>3.94</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table A3. H2: Mean J-S Divergence Between Self Tweets and Full (Random) Personas for Core Users Data Set

<table><tr><td></td><td>Mean J-S Divergence</td></tr><tr><td>Self-tweet and full persona</td><td>0.057</td></tr><tr><td>Self-tweets and random full persona</td><td>0.073</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p&lt;0.001</td></tr></table>

Table A4. H3: Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method for Combined Data Set

<table><tr><td rowspan="2"></td><td colspan="4">Experts</td></tr><tr><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.49</td><td>1.13</td><td>0.68</td><td>0.49</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>4.61</td><td>3.78</td><td>2.41</td><td>1.52</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr><tr><td rowspan="2"></td><td colspan="4">Core Users</td></tr><tr><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th=10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.15</td><td>1.90</td><td>1.59</td><td>1.38</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.7963</td><td>5.08994</td><td>3.60329</td><td>2.49</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table A5. H3: Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method Combined Data Set

<table><tr><td rowspan="2"></td><td colspan="4">Experts</td></tr><tr><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>0.55</td><td>0.69</td><td>0.98</td><td>1.35</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>1.93</td><td>2.44</td><td>3.11</td><td>4.07</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr><tr><td rowspan="2"></td><td colspan="4">Core Users</td></tr><tr><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.29</td><td>1.36</td><td>1.45</td><td>1.63</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.15</td><td>2.46</td><td>2.96</td><td>3.87</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table A.6. H3: Mean J-S Divergence Between Self Tweets and Full (Random) Personas for Combined Data Set

<table><tr><td rowspan="2"></td><td colspan="2">Mean J-S Divergence</td></tr><tr><td>Core Uers</td><td>Bloggers</td></tr><tr><td>Self-tweet and full persona</td><td>0.054</td><td>0.012</td></tr><tr><td>Self-tweets and random full persona</td><td>0.067</td><td>0.032</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p&lt;0.001</td><td>p&lt;0.001</td></tr></table>

## Appendix B

## Recreation of Home Timelines

On Twitter, the home timeline of a user u is a stream of all tweets (self-tweets and retweets) posted by all the users that u follows, sorted approximately in reverse chronological order, including promoted tweets that originate from Twitter. One should note that, as a general rule, retweeting does not cause tweets to reappear in a user’s home timeline or to change their relative position in the timeline. For example, if u follows user a, and a posts a tweet, this tweet will appear only once in user u’s home timeline regardless of whether it was retweeted by other users u follows.

However, when collecting data from the REST API, it is not possible to retrieve a user’s full home timeline as such. Instead, we only observe each user’s user timeline: the tweets and retweets that he or she has posted. Consequently, the recreation of the home timeline of each core user was done in two steps: First, we combined all tweets posted by the core user’s followings into one timeline and sorted them by creation date. Second, since retweets do not cause tweets to reappear in a user’s home timeline, we filtered out duplicate tweets. For example, if u follows both a and b, who both retweet tweet t, in reality this tweet will appear only once in u’s home timeline, attributed to the user who retweeted first (let us assume that it is a). However, when we combine the user timelines of a and b, tweet t appears twice (once from a and once from b), so it is necessary to filter b’s retweet out of the timeline. These two steps produce a timeline that closely approximates the actua home timeline of user u.

Note that some followings had their privacy settings set to private during the data collection period or had their accounts suspended, meaning that we could not collect their data. This means that our recreated timelines missed some incoming tweets. However, we estimate that the number of followings affected should not exceed 10% of the followings in our data set.

## Appendix C

## Data Collection for Expert Users

The selection of expert users was done under the assumption that individuals who blog for prominent blog sites and also have Twitter accounts are particularly likely to use Twitter as a personal branding tool. We therefore manually gathered lists, from the Twitter pages of 12 blogging websites, that contained the Twitter accounts of the bloggers who contribute to those sites. Table C1 presents the URLs of the blogs, their Twitter pages, and the specific list pages from which we composed the set of expert users.

<table><tr><td colspan="4">Table C1. Blog URLs</td></tr><tr><td>Blog Name</td><td>Website</td><td>Twitter Page</td><td>Lists from the Twitter Page</td></tr><tr><td>Huffington Post</td><td>http://www.huffingtonpost.com/</td><td>https://twitter.com/Huffington Post</td><td>https://twitter.com/HuffingtonPost/lists/tech-politics-bloggers/membershttps://twitter.com/HuffingtonPost/lists/huffposters-2/membershttps://twitter.com/HuffingtonPost/lists/bloggers/members</td></tr><tr><td>Business Insider</td><td>http://www.businessinsider.com/</td><td>https://twitter.com/business insider</td><td>https://twitter.com/businessinsider/lists/bi-editors-reporters/members</td></tr><tr><td>Mashable</td><td>http://mashable.com/</td><td>https://twitter.com/mashable/</td><td>https://twitter.com/mashable/lists/mashable-staff-24/members</td></tr><tr><td>Gizmodo</td><td>http://gizmodo.com/</td><td>https://twitter.com/Gizmodo</td><td>https://twitter.com/Gizmodo/lists/writers/membershttps://twitter.com/Gizmodo/lists/gizmodostaff/members</td></tr><tr><td>Lifehacker</td><td>http://lifehacker.com/</td><td>https://twitter.com/lifehacker</td><td>https://twitter.com/lifehacker/lists/lifehacker/members</td></tr><tr><td>Gawker</td><td>http://gawker.com/</td><td>https://twitter.com/Gawker</td><td>https://twitter.com/Gawker/lists/writers/members</td></tr><tr><td>The Daily Beast</td><td>http://www.thedailybeast.com/</td><td>https://twitter.com/thedailybeast</td><td>https://twitter.com/thedailybeast/lists/the-daily-beast-staff/members</td></tr><tr><td>Techcrunch</td><td>http://techcrunch.com/</td><td>https://twitter.com/TechCrunch</td><td>https://twitter.com/TechCrunch/lists/writers/members</td></tr><tr><td>Jezebel</td><td>http://jezebel.com/</td><td>https://twitter.com/Jezebel/</td><td>https://twitter.com/Jezebel/lists/writers/membershttps://twitter.com/Jezebel/lists/jezebel-guide/members</td></tr><tr><td>The next web</td><td>http://thenextweb.com/</td><td>https://twitter.com/TheNextWeb</td><td>https://twitter.com/TheNextWeb/lists/tnw-team/members</td></tr><tr><td>Epicurious</td><td>http://www.epicurious.com/</td><td>https://twitter.com/epicurious</td><td>https://twitter.com/epicurious/lists/epicurious-editors-2/members</td></tr><tr><td>NYT Food</td><td>http://www.nytimes.com/pages/dining/index.html</td><td>https://twitter.com/nytfood</td><td>https://twitter.com/nytfood/lists/foodies/members</td></tr></table>

## Appendix D

## MTurk Survey to Determine Whether Experts’ Accounts Represent Actual People or Services

To make sure our experts’ (bloggers’) accounts corresponded to real-life individuals rather than to services or products, we ran the following survey on Amazon Mechanical Turk (see Figure D1), asking workers to tell us whether each blogger’s account reflected a company or an actual person. Each account was graded by three unique Turkers. We say an account represents an actual person if at least two out of the three Turkers marked it as such.

## Survey Instructions (Click to collapse)

• We need your help assessing a Twitter account.

• Please click the link of a Twitter account, enter the user's account and get familiar with the user and his tweets.

• Answer the question below (you can go back and forth to the account page - this is not a memory test)

• Thank you!

Account address:

![](/api/attachments/HDNYXTXS/fulltext/images/09e29acf70a08f02f18c2fb60028465c4ebb92d4694eb8e4c30a2c5b8d28ebe9.jpg)

https://twitter.com/intent/user?user id=377778216

Do you think the Entity behind this Twitter page is a person or a company/PR masquerading as a person?

Submit

## Figure 1. Population Model (Simple Model)

## Appendix E

## Identification

To clarify our identification strategy, we present a diagram that visually portrays our strategy. Let’s assume Dan’s home timeline (the tweets he sees) consists of the following 15 tweets:

Tweet 1 “it’s like i always say: cleveland is bad”

Tweet 2 “musicianship: what a load of fascist malarkey”

Tweet 3 I just witnessed a DRIVER of a CAR run a Red Light. Time to fire off an Op-Ed to the @chicagotribune calling ALL drivers scofflaws! #bikeCHI

Tweet 4 Carrie just struck a bowl & said: “might be an ugly bowl, but it sounds good”

Tweet 5 “Ever sine you told me you saw that Diners, Drive-ins, and Dives guy in NYC, I just won’t watch his show any more”#DadTime

Tweet 6 Thinking a lot about music that exists in spaces where it’s left unconsidered. How & why it’s made and by whom?

Tweet 7 When the servers try and tell you a joke saying you sound like an owl and you actually start crying bc you thought someone was being mean

Tweet 8 Offensive line: TAKE CARE OF LAMAR

Tweet 9 Plot twist: the white girl isn’t drinking a PSL

Tweet 10 Update: just got reprimanded for getting on tinder. This is why I have a privacy screen. I need my replacement asap

Tweet 11 Tinder in NYC is really depressing because everyone is beautiful and you’re just irrelevant

Tweet 12 Get snaps of the inside of frat life is very entertaining. Dance pledges, dance

Tweet 13 When they said I could do better, they were damn right

Tweet 14 Under U.S. law Hillary literally is disqualified from becoming president... https://t.co/N7h4mV88h5

Tweet 15 New uniforms to honor POW/MIA soldiers & all veterans who served our great nation @ our Military Appreciation Game-… https://t.co/GPs6t8xRVa

Now, let us assume that from these 15 tweets Dan retweeted tweets 4, 7, and 15. In this case his retweeted persona will be

Tweet 4 Carrie just struck a bowl & said: “might be an ugly bowl, but it sounds good”

Tweet 7 When the servers try and tell you a joke saying you sound like an owl and you actually start crying bc you thought someone was being mean

Tweet 15 New uniforms to honor POW/MIA soldiers & all veterans who served our great nation @ our Military Appreciation Game-… https://t.co/GPs6t8xRVa

To build Dan’s random retweeted persona we randomly sample three tweets from Dan’s feed (as we explain, we sample the exact number of retweets that the user actually posted). Let’s say we randomly sampled tweets 3, 7, and 10. This means that Dan’s random retweeted persona will be

Tweet 3 I just witnessed a DRIVER of a CAR run a Red Light. Time to fire off an Op-Ed to the @chicagotribune calling ALL drivers scofflaws! #bikeCHI

Tweet 7 When the servers try and tell you a joke saying you sound like an owl and you actually start crying bc you thought someone was being mean

Tweet 10 Update: just got reprimanded for getting on tinder. This is why I have a privacy screen. I need my replacement asap

## Appendix F

# Accounting for Alternative Motivations for Retweeting: Construction of the Different Types of Random Retweet Persona

We replicate our analysis, while accounting for different drivers and factors that may impact retweeting decisions. We do so by using different types of random retweeted persona vectors. Below we elaborate on the construction of the different types of random retweeted personas, and specifically the three random retweeted personas based on tie strength.

## Tie Strength (1): Taking into Account Only Link Characteristics

When creating each core user u’s RandomReTweet document, instead of randomly sampling tweets from the self-tweets and retweets of the user’s followings, we employ a stratified sampling technique.

We first define four types of possible retweets based on the types of links between the core user and the user who originally wrote the retweeted tweet:

(1) Strong tie: The core user follows the user who wrote the retweeted tweet, and that user follows the core user.

(2) Weak tie: The core user follows the user who wrote the retweeted tweet, but that user does not follow the core user.

(3) Reverse weak tie: The core user does not follow the user who wrote the retweeted tweet, but that user follows the core user.

(4) Complete weak tie: The core user does not follow the user who wrote the retweeted tweet, and that user does not follow the core user.

Note that options (3) and (4) are indeed possible options. A user does not have to directly follow another user to have the latter user’s tweet appear in his home timeline. For example, if user a follows user b and user b follows user c, if user b retweets a tweet of user c, this tweet will appear in user a’s home timeline even if a does not follow c. Optimally, we would want to know that the tweet arrived at user a’s timeline via b. However, the retweeting route of a tweet is not information the REST API provides. Given a tweet retweeted by an core user, the REST API provides us only with the user who wrote the original tweet. For this reason we consider tie strength types (3) and (4).

Then, for each core user we compute the percentage of retweets he posts from each of the four groups. Finally, we construct the random retweeted persona, for each core user by randomly selecting potential retweets from the user’s followings in a manner that maintains the same proportions across the four tie strength groups. For example, if the core user retweeted 10 tweets from strong ties, 20 tweets from weak ties, and so forth, when sampling potential retweets from the user’s followings, we will randomly sample 10 tweets from the group of tweets coming from strong ties and 20 tweets from the group of tweets coming from weak ties.

## Tie Strength (2): Taking into Account Link and Interaction Characteristics

We first define five types of possible retweets based on the types of links and interactions (replies and mentions) between the core user and the user who originally wrote the retweeted tweet. Specifically, this specification divides group (1) above (strong ties) into two groups, thus eventually dividing the users’ retweets into five groups prior to conducting the stratified sampling for the construction of the random retweeted persona:

1. Strong tie with no interaction: The core user follows the user who wrote the retweeted tweet, and that user follows the core user. However, there is no personal interaction between them. That is, neither user mentions the other or replies to his or her tweets using the corresponding Twitter handle.

2. Strong tie with interactions: The core user follows the user who wrote the retweeted tweet, and that user follows the core user, and there is at least one personal interaction between the two users (reply or mention), directed either from the core user to the following or from the following to the core user

Then, for each core user, we compute the percentage of retweets he posts from each of the five groups. Finally, we construct the random retweeted persona, for each core user, by randomly selecting potential retweets from the user’s followings in a manner that maintains the same proportions across the five tie strength groups.

## Tie Strength (3): Taking into Account Link and Interaction Characteristics

We first define seven types of possible retweets based on the types of links and interactions (replies and mentions) between the core user and the user who originally wrote the retweeted tweet. Specifically, this specification divides group (1) above (strong ties) into four groups, thus eventually dividing the users’ retweets into seven groups prior to conducting the stratified sampling for the construction of the random retweeted persona:

1. Strong tie with no interaction: The core user follows the user who wrote the retweeted tweet, and that user follows the core user. However, there is no personal interaction between them. That is, neither user mentions the other or replies to his or her tweets using the corresponding Twitter handle.

2. Strong tie with one sided interaction: The core user follows the user who wrote the retweeted tweet, and that user follows the core user. There is at least one interaction initiated by the core user toward the following but no interaction initiated by the following toward the core user.

3. Strong tie with reverse one-sided interaction: The core user follows the user who wrote the retweeted tweet, and that user follows the core user. There is at least one interaction initiated by the following toward the core user and no interaction initiated by the core user toward the following.

4. Strong tie with two-sided interaction: The core user follows the user who wrote the retweeted tweet, and that user follows the core user. There is at least one interaction initiated by the core user toward the following and at least one interaction initiated by the following toward the core user.

Then, for each core user we compute the percentage of retweets he posts from each of the seven groups. Finally, we construct the random retweeted persona, for each core user, by randomly selecting potential retweets from the user’s followings in a manner that maintains the same proportions across the seven tie strength groups.

## Appendix G

## Determining the Number of Topics in the Corpus Prior to Running LDA

As mentioned, LDA needs to be given, a priori, a parameter that tells it the number of topics in the corpus. Selecting a number that is too small could cause unnecessary generalizations, whereas choosing an overly large number could cause redundancy. As explained above, in this paper we use a data-driven approach to find the optimal number of topics. Since there are several metrics that have been developed to find a “good” number, and no one dominating method, we have used four different methods, all leading to similar results. In what follows, we will briefly outline the methods used and discuss the results of each method. Modeling and computations are executed using R’s ldatuning package.<sup>1</sup>]

Method #1 (based on Griffiths and Steyvers 2004): This method is based on evaluating the model by approximating its log-likelihood (as there are clearly too many alternatives to fully estimate the log-likelihood). The suggestion of this method is to use samples from the Gibbs sampling iterations. The number of topics is then chosen to be that with the maximum log-likelihood approximation.

Method #2 (based on Cao et al. 2009): This method suggests a metric to select the number of topics based on the distances among different topics in the model. The method is based on the assumption that LDA performs best when the average cosine distance of topics reaches the minimum.

Method #3 (based on Arun et al. 2010): This method is based on Symmetric K-L divergence and on the assumption that LDA can be viewed as a matrix factorization mechanism. In the proposed metric, divergence values are higher for nonoptimal numbers of topics. Thus, the optima number of topics would be the one that yields the minimum score.

Method #4 (based on Deveaud et al. 2014): This approach focuses on the goal of deriving topics that differ from one another. To this end, this approach derives the number of topics based on the information divergence (using Jensen-Shannon divergence) between all pairs of topic in a given model. The model with the maximum divergence is said to be the best model.

## Finding the Number of Topics for the Core Users’ Corpus

We ran LDA on our core user corpus using Gibbs sampling with T ranging from 5 to 150, alpha = T/50, beta = 0.1 and 1000 iterations (as suggested by Griffiths and Steyvers 2004). For each LDA, run we calculated each of the four metrics. The results are normalized and presented graphically in Figure G1 which portrays each metric as a function of the number of topics. Note that for method #1 (Griffiths and Steyvers 2004) and method #4 (Deveaud et al. 2014) we looked for a maximum, whereas for method #2 (Cao et al. 2009) and method #3 (Arun et al. 2010) we focused on finding the minimum.

According to the four metrics it seems that the optimal number of topics for our corpus ranges between 15 and 35 topics<sup>2</sup> (getting a range is expected given that the different approaches make different assumptions regarding what a good set of topics corresponds to). As these metrics point to a range and not a single number, in what follows we present another layer of analysis that was aimed at selecting one single optima number of topics to be presented in the main results. For robustness purposes, we rerun the main analysis of the paper (H1 and H2) with 15, 20, 25, 30, and 35 topics, with similar results.

## Finding a Single Optimal Number of Topics by Aggregating the Different Methods

To identify a good number of topics, we aggregated the scores of the four methods for each number of topics. For the two methods in which a higher score corresponded to a better result (Deveaud et al. 2014 and Griffiths and Steyvers 2004 ) we took (1-score). Thus, the optima number of topics was the one yielding the overall minimum score. The results of the aggregated scores are presented in Figure G2. As shown, the number of topics with the overall minimum score was 25. Thus, we chose 25 to be the number of topics used for the analysis of the core users throughout the paper.

![](/api/attachments/HDNYXTXS/fulltext/images/fed8b315ce1f490d71cde1ba530d6ef40191e72a7ebcdc32bd63306bc04c5149.jpg)  
Figure G1. Measure by Number of Topics

![](/api/attachments/HDNYXTXS/fulltext/images/ed9808668c999a3f143aaff8e0f5b53048fc74bb63dae4ee7f837dc727bea3e9.jpg)  
Figure G2. Sensitivity Analysis

## Finding the Number of Topics for the Combined Corpus Comprising Core Users and Experts

To find the number of topics for the combined corpus we reran the analysis described above, this time on the combined data set. Figure G3 and Figure G4 present the optimal number of topics for each method and the aggregated score. As shown, the number of topics with the overall minimum score was 30. Thus, we chose 30 to be the number of topics used for the analysis of the combined data set.

![](/api/attachments/HDNYXTXS/fulltext/images/dc75e6e43491060030476101015950db703b2e321f8d2cdc6ef18e2d00e21dff.jpg)  
Figure G3. Measure by Number of Topics

![](/api/attachments/HDNYXTXS/fulltext/images/2060b14b6a3ba73872ff9307d23cb2d26a9c52b50853878854e74451e9aa82ea.jpg)

Figure G4. Sensitivity Analysis

## Appendix H

## Top Keywords of Topics

Table H1 presents the top 20 keywords corresponding to each of the 25 topics from the LDA run on the core users. Table H2 presents the top 20 keywords corresponding to each of the 30 topics from the LDA run on the combined data set of core users and expert users.

<table><tr><td colspan="3">Table H1. Top 20 Keywords per Topic from the LDA Run with 25 Topics on the Core User Data Set</td></tr><tr><td>Topic 0</td><td>Social: College student life</td><td>free tonight parti night homecom black lit week colleg will atlanta fridai go ticket weekend saturdayi tomorrow ladi uwg empir</td></tr><tr><td>Topic 1</td><td>Politics: Democrat, Bernie Sanders, police violence and social justice</td><td>polic women report nodapl kill berni peopl sander join prison war climat chang health right polici justic berniesand million syria</td></tr><tr><td>Topic 2</td><td>Sports: Wrestling</td><td>wwe raw match love ufc live fight sdlive wrestl tonight yr show titl win survivorseri will team hiac goldberg champion</td></tr><tr><td>Topic 3</td><td>Mustic: live performances and concerts</td><td>vote favorit ticket song love ama plai music artist album tonight countri rt listen show dai nowplai year tour dnce</td></tr><tr><td>Topic 4</td><td>Politics: presidential election</td><td>trump hillari clinton vote will elect donald realdonaldtrump obama peopl debat presid support hillaryclinton america american campaign email win fbi</td></tr><tr><td>Topic 5</td><td>Social: General social interactions</td><td>dai fuck love todai time work lol go good peopl feel gonna make night back watch friend hate happi shit</td></tr><tr><td>Topic 6</td><td>Politics: Race in politics</td><td>black trump peopl white fuck year man vote rt women obama presid girl donald will kill time call woman twitter</td></tr><tr><td>Topic 7</td><td>Sports: College football</td><td>happi birthday dai school colleg great year miss todai game tomorrow senior football hope class week best texa tonight team</td></tr><tr><td>Topic 8</td><td>Social: with use of profanity</td><td>nigga shit fuck bitch lol ain ass back man wanna gotta girl love good peopl time make talk real feel</td></tr><tr><td colspan="3">Table H1. Top 20 Keywords per Topic from the LDA Run with 25 Topics on the Core User Data Set (Continued)</td></tr><tr><td>Topic 9</td><td>Social: media and entertainment</td><td>will time make dai todai live good year thing great work peopl world watch love show help week read start</td></tr><tr><td>Topic 10</td><td>Sports: Basketball, NBA</td><td>game win plai team will season year nba back time player good watch nfl best fan man week warrior lebron</td></tr><tr><td>Topic 11</td><td>Entertainment: TV &amp; movies</td><td>love watch episod season show movi book tonight film star cast comic debat happi charact read hei premier favorit fan</td></tr><tr><td>Topic 12</td><td>Entertainment: Travel and food</td><td>love travel happi quot beauti wine good food morn great sashaeat recip etsi vegan coffe check dai chocol yelp kitm</td></tr><tr><td>Topic 13</td><td>Music, rap</td><td>listen music video drop lil album song drake soundcloud bro np nigga happi kany shit birthday rt lit rapper watch</td></tr><tr><td>Topic 14</td><td>Sports: Football &amp; baseball</td><td>game win cub plai team will lead run fan tonight year football good time baseball todai season hit state seri</td></tr><tr><td>Topic 15</td><td>Social: feel-good messages</td><td>love girl life peopl make will dai thing ur time friend feel happi good person best back talk year care</td></tr><tr><td>Topic 16</td><td>College sport and social</td><td>student drink journalnew nursestakedc learn great beer school nurs earn join photo daytonsport untappd fairwindsbrew badg teacher educ commun rickcassano</td></tr><tr><td>Topic 17</td><td>Youtube shows/channels</td><td>youtu video cspanwj plai eddykenzofici artist stylish ivoteeddykenzo playlist part star movi ad regrannapp watch post makingamurder photo bt impastor</td></tr><tr><td>Topic 18</td><td>Sports: Soccer</td><td>goal game win score team plai player season final leagu soccer cup fan match hockei olymp nhl arsen usa messi</td></tr><tr><td>Topic 19</td><td>Weather</td><td>nascar todai race hurricane offic matthew polic honor florida will counti park car storm rain south fire tonight hurricanematthew back</td></tr><tr><td>Topic 20</td><td>Entertainment: video games</td><td>game plai pokemon video anim stream youtub final super episod draw gui appl art pokmon charact will theori jihad updat</td></tr><tr><td>Topic 21</td><td>Religion/faith</td><td>god peopl todai love check will automat unfollow life virgo person work lord jesu good make thing dai live time</td></tr><tr><td>Topic 22</td><td>The Young Turks (TYT): news and commentary program on YouTube</td><td>counti warn beach va virginia sibab sever lake thunderstorm citi theyoungturk ut mtvstarsbrunomar ride point storm cdt bruno brunomar salt</td></tr><tr><td>Topic 23</td><td>Popular culture</td><td>win rt follow chanc stream enter live giveawai pop dai originalfunko twitch sawyerfrdrx plai exclus will winner retweet check game</td></tr><tr><td>Topic 24</td><td>Beauty/cosmetics</td><td>rt win video follow dm happi gui fan palett makeup tweet song winner live show beauti vote todai birthday amaz</td></tr><tr><td colspan="3">Table H2. Top 20 Keywords per Topic from the LDA Run with 30 Topics on the Combined Data Set of Core Users and Expert Users</td></tr><tr><td>Topic 0</td><td>Religion, faith</td><td>god love will life peopl jesu lord prai bless live thing good heart faith make work give chang time world</td></tr><tr><td>Topic 1</td><td>Astrology</td><td>peopl todai check automat unfollow virgo person pisc sagittariu aquariu gemini tauru leo libra ari scorpio cancer feel work capricorn</td></tr><tr><td>Topic 2</td><td>Technology products &amp; companies</td><td>appl market facebook googl peopl tech twitter app compani new year busi will iphon ceo startup work data report brexit</td></tr><tr><td>Topic 3</td><td>Politics: Race in politics</td><td>black peopl trump white vote women man fuck year rt presid obama woman men america kill donald polic hillari stop</td></tr><tr><td>Topic 4</td><td>Social: media and entertainment</td><td>dai time will todai make watch good live great love thing show year work world back week best night tonight</td></tr><tr><td>Topic 5</td><td>Wrestling</td><td>wwe raw match ufc love wrestl sdlive fight jihad tonight yr titl survivorseri team show win hiac goldberg good champion</td></tr><tr><td>Topic 6</td><td>Entertainment: video games</td><td>plai game stream live youtub twitch video gui team pokemon check overwatch go amaz fayde final song start peopl love</td></tr><tr><td>Topic 7</td><td>Mustic, live performances and concerts</td><td>sawyerfrdrx gai band song album show music plai listen vegan ur tonight art queer nowplai tour record tran sawyer sex</td></tr><tr><td>Topic 8</td><td>Youtube music videos</td><td>youtub video warn counti beach va eddykenzofici virginia nursestakedc artist plai stylish ivoteeddykenzo sever theyoungturk thunderstorm nurs pokemon cdt playlist</td></tr><tr><td>Topic 9</td><td>Middle east and war in Syria</td><td>russia syria war attack kill report israel isi russian brexit turkei world state polic aleppo forc syrian uk govern militari</td></tr><tr><td>Topic 10</td><td>Politics: movement for and against Trump</td><td>mtscore imwithh nevertrump donaldtrump hillaryclinton auditthevot vote amjoi msnbc notmypresid uniteblu realdonaldtrump lead knick gop flipitdem ff berlin rt joyannreid</td></tr><tr><td>Topic 11</td><td>Music: rap</td><td>video man lil drop drake nigga bro music album song fuck rt shit year lmao listen kany kid hit birthday</td></tr><tr><td>Topic 12</td><td>Presidential election debates</td><td>trump clinton vote donald elect will peopl hillari debat presid campaign call women obama time support make voter gop year</td></tr><tr><td>Topic 13</td><td>Weather</td><td>polic todai offic join citi hurrican help school report live honor break matthew state park student counti power shoot commun</td></tr><tr><td>Topic 14</td><td>Social: feel-good messages</td><td>love girl peopl life make ur will thing dai time friend feel happi person best good talk back wanna year</td></tr><tr><td>Topic 15</td><td>Social: General social interactions</td><td>fuck dai love lol peopl work time todai go good gonna feel make shit night back hate watch friend thing</td></tr><tr><td>Topic 16</td><td>Social: with use of profanity</td><td>nigga shit fuck bitch ain lol ass love back man wanna gotta girl good time make feel talk ya real</td></tr><tr><td>Topic 17</td><td>Sports: Football</td><td>game win plai team will season good time football tonight year back week player lead todai nfl fan state start</td></tr><tr><td>Topic 18</td><td>Politics: Clinton email leaks and FBI</td><td>hillari trump clinton vote realdonaldtrump will hillaryclinton email maga fbi obama america elect wikileak american support peopl corrupt media win</td></tr><tr><td>Topic 19</td><td>Music: video and streaming</td><td>vote love favorit ama tonight artist song countri rt perform album video music show year happi live dnce taylor male</td></tr><tr><td>Topic 20</td><td>Popular culture</td><td>rt win follow chanc dm winner retweet palett giveawai enter pop makeup originalfunko exclus give set kit lip card kyli</td></tr><tr><td>Topic 21</td><td>Sports: Baseball</td><td>game cub win fan team baseball dodger plai goal seri indian hit worldseri year pitch season player score lead run</td></tr><tr><td>Topic 22</td><td>Music: live tour and performances</td><td>ticket love video tonight music show song tour fan gui follow fuck night listen happi live mix world amaz set</td></tr><tr><td colspan="3">Table H2. Top 20 Keywords per Topic from the LDA Run with 30 Topics on the Combined Data Set of Core Users and Expert Users (Continued)</td></tr><tr><td>Topic 23</td><td>Teenage: politics, highschool sports, and entertainment</td><td>cspanwj citizenradio ut lake post citi photo salt facebook maryland drive utah il healthcar ricardoreport impastor rahde opengov allmet impastortv</td></tr><tr><td>Topic 24</td><td>Movies</td><td>movi episod season book star love watch show film comic review trailer war charact fan gameofthron sibab cast marvel write</td></tr><tr><td>Topic 25</td><td>Social: College students</td><td>happi birthday dai school love year colleg miss todai tomorrow great game best hope week tonight good class night senior</td></tr><tr><td>Topic 26</td><td>Music: Alternative/Indie</td><td>np listen soundcloud free prod nowplai tonight da parti ft uwg music live mixtap night video feat periscop youtub spinrilla</td></tr><tr><td>Topic 27</td><td>Music: TV and youtube</td><td>raider drink beer raidern check photo live earn mtvstarsbrunomar untappd badg love good periscop jaymohrsport great bruno oakland level brunomar</td></tr><tr><td>Topic 28</td><td>Sports: car race</td><td>nascar race lap car win mesport regrannapp watch driver back thechas lead track bt texansch pit fan seahawk caution cup</td></tr><tr><td>Topic 29</td><td>Social: Student life</td><td>student school journalnew make entrepreneur learn media startup wearephoenix smallbiz teacher daytonsport book educ great start rickcassano lead will hoki</td></tr></table>

## Appendix I

Accounting for Alternative Motivations for Retweeting: Results for the Different Types of Random Retweeted Persona

Below we present the results for H1 when accounting for the different factors influencing retweeting behavior.

Social Dynamics

Results When Accounting for Reciprocity

<table><tr><td colspan="5">Table I1. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method</td></tr><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.53983</td><td>2.37387</td><td>2.14997</td><td>1.99336</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.99578</td><td>5.58962</td><td>4.59113</td><td>3.62764</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

<table><tr><td colspan="5">Table I2. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method</td></tr><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.39</td><td>1.45</td><td>1.58</td><td>1.75</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.39</td><td>2.69</td><td>3.17</td><td>3.91</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Results When Accounting for Tie Strength (Definition 1)

<table><tr><td colspan="5">Table I3. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method</td></tr><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.44</td><td>2.29</td><td>2.07</td><td>1.88</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.90</td><td>5.53</td><td>4.49</td><td>3.50</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I4. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th=0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.31</td><td>1.39</td><td>1.5</td><td>1.67</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.24</td><td>2.56</td><td>3.02</td><td>3.83</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p&lt;0.001</td><td>p&lt;0.001</td><td>p&lt;0.001</td><td>p&lt;0.001</td></tr></table>

Results When Accounting for Tie Strength (Definition 2)

<table><tr><td colspan="5">Table I5. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method</td></tr><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.28</td><td>2.18</td><td>2.04</td><td>1.95</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.48</td><td>5.18</td><td>4.33</td><td>3.50</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I6. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.47</td><td>1.53</td><td>1.59</td><td>1.7</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.36</td><td>2.62</td><td>3.01</td><td>3.65</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Results When Accounting for Tie Strength (Definition 3)

<table><tr><td colspan="5">Table I7. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method</td></tr><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.36</td><td>2.23</td><td>2.08</td><td>1.95</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.44</td><td>5.15</td><td>4.23</td><td>3.39</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I8. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.46</td><td>1.52</td><td>1.6</td><td>1.76</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.27</td><td>2.55</td><td>2.94</td><td>3.61</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Results When Accounting for Source (Author) Popularity

Table I9. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method

<table><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.32829</td><td>2.20403</td><td>2.03885</td><td>1.92942</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.50593</td><td>5.25445</td><td>4.47805</td><td>3.70314</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I10. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.37</td><td>1.44</td><td>1.53</td><td>1.66</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.47</td><td>2.77</td><td>3.21</td><td>3.83</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Tweet Characteristics

## Results When Accounting for Tweet Popularity

<table><tr><td colspan="5">Table I11. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method</td></tr><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.47914</td><td>2.30736</td><td>2.11012</td><td>1.94571</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.34785</td><td>5.14601</td><td>4.46503</td><td>3.64908</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I12. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.38</td><td>1.47</td><td>1.58</td><td>1.77</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.53</td><td>2.83</td><td>3.24</td><td>3.87</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Results When Accounting for Retweetability

Table I13. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Counts Method

<table><tr><td></td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>2.37</td><td>2.23</td><td>1.99</td><td>1.81</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>5.66</td><td>5.46</td><td>4.67</td><td>3.81</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table I14. Mean Number of Topics Added via Retweets Versus Mean Number of Topics Added via Random Retweets: Percentage Method

<table><tr><td></td><td>Th = 0.8</td><td>Th = 0.85</td><td>Th = 0.9</td><td>Th = 0.95</td></tr><tr><td>Mean of number of topics added via retweeted persona</td><td>1.3</td><td>1.36</td><td>1.49</td><td>1.63</td></tr><tr><td>Mean of number of topics added via random retweeted persona</td><td>2.67</td><td>2.98</td><td>3.39</td><td>4.03</td></tr><tr><td>Wilcoxon signed-rank test</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Appendix J

## Robustness Analysis: Distance Between Added Topics and Self-Produced Topics

For robustness purposes we examine another aspect of the similarity between users’ self-produced personas and their retweeted personas. Specifically, we empirically study the similarity between topics added via retweets and those in the users’ self-tweets, hypothesizing that they will be closely related to one another. In this analysis, we use topic similarity measures to show that the topics that users add via their retweet are more similar to the topics in their self-tweets than are those added via random retweets.

Specifically, we do the following: First, we create a distance table comparing all pairs of topics. Recall that the topics produced by LDA are multinomial distributions over the words in the corpus, and as such are suitable for comparison using methods that measure similarity (or dissimilarity) between distributions. For each pair of topics in our data set, we compute the distance between the two topics by calculating the Jensen-Shannon divergence (J-S divergence) between their corresponding distributions (that is, (25 × 24)/2 comparisons). J-S divergence is a popular measure for dissimilarity between two probability distributions (Aletras and Stevenson 2014). We use J-S divergence with the base 2 logarithm, which results in a number between 0 and 1, where 0 reflects identical probabilities, and 1 reflects orthogonal probabilities.

Second, for each user, we use two different measures to compute the distance between the topics that were added via the retweeted persona and the topics in the user’s self-tweets. One of the measures is based on minimal distance and the other is based on average distance.

Third, for each user, we use the same two measures to compute the distance between the topics that were added via the random-retweeted persona and the topics in the user’s self-tweets.

Finally, for each user and for each distance measure, we compare the distance obtained for actual retweets (the outcome of the second step) with the distance obtained for the random retweets (the outcome of the third step) to understand the relative dissimilarity between the topics in the user’s self-tweets and the topics in her retweets.

We present the results of the comparison in Table J2 and Table J2. Complete details on the J-S divergence procedure and the two different distance measures are provided in Appendix K.

As can be seen in Tables J1 and J2, for both distance measures and all thresholds (corresponding to the counts method and the percentage method), we find that the topics added via the user’s actual retweets are closer to the topics of her self-tweets than are those added via the random retweets. These findings provide further support to H1 in showing that, beyond the fact that users add few topics, the topics that a user does add are comparatively similar to his or her self-produced topics.

Table J1. Distance Between Topics in Self-Produced Persona and Topics Added via Retweets or Random Retweets: Counts Method

<table><tr><td rowspan="2"></td><td colspan="4">Measure A</td><td colspan="4">Measure B</td></tr><tr><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td><td>Th = 1</td><td>Th = 2</td><td>Th = 5</td><td>Th = 10</td></tr><tr><td>Mean divergence of topics added by retweets to topics in self-tweets (RT-divergence)</td><td>0.54</td><td>0.5</td><td>0.44</td><td>0.38</td><td>0.36</td><td>0.33</td><td>0.29</td><td>0.26</td></tr><tr><td>Mean divergence of topics added by random retweets to topics in self-tweets (random-RT-divergence)</td><td>0.65</td><td>0.63</td><td>0.56</td><td>0.49</td><td>0.47</td><td>0.45</td><td>0.41</td><td>0.35</td></tr><tr><td>Wilcoxon between RT-divergence and random-RT-divergence</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

Table J2. Similarity Between Topics in Self-Produced Persona and Topics Added via Retweets or Random Retweets: Percentage Method

<table><tr><td rowspan="2"></td><td colspan="4">Measure A</td><td colspan="4">Measure B</td></tr><tr><td>Th = 80%</td><td>Th = 85%</td><td>Th = 90%</td><td>Th = 95%</td><td>Th = 80%</td><td>Th = 85%</td><td>Th = 90%</td><td>Th = 95%</td></tr><tr><td>Mean divergence of topics added by retweets to topics in self-tweets (RT-divergence)</td><td>0.29</td><td>0.31</td><td>0.35</td><td>0.40</td><td>0.19</td><td>0.20</td><td>0.22</td><td>0.25</td></tr><tr><td>Mean divergence of topics added by random retweets to topics in self-tweets (random-RT-divergence)</td><td>0.38</td><td>0.42</td><td>0.48</td><td>0.55</td><td>0.27</td><td>0.30</td><td>0.34</td><td>0.39</td></tr><tr><td>Wilcoxon between RT-divergence and random-RT-divergence</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td><td>p &lt; 0.001</td></tr></table>

## Appendix K

## H1: Robustness: Methods Used to Determine Similarity Between Added Topics and Self-Tweeted Topics

We calculate similarity between the topics in the self-produced persona and the topics added via actual retweets or via random retweets. We find that the new topics added via users’ retweets are indeed more similar to those discussed in their self-tweets than are the new topics added via random retweets

Specifically, we do the following:

(1) We create a distance table comparing all pairs of topics. Recall that the topics produced by LDA are multinomial distributions over the words in the corpus, and as such are suitable for comparison using methods that measure similarity between distributions. We compute similarity using the J-S divergence between each pair of topics in our data set (that is, (25 × 24)/2 comparisons). J-S divergence is appropriate for comparing the LDA output vectors, as they are by definition probability vectors (that is, each vector sums to 1). We use the J-S divergence with the base 2 logarithm, which results in a number between 0 and 1, where 0 reflects identical probabilities, and 1 reflects orthogonal probabilities. We find that the pair with the maximum distance is topic 8 and topic 22, with a J-S score of 0.92. The pair with the minimal distance is topic 5 and topic 15, with a J-S score of 0.27. A histogram of the distances is presented in Figure K1. As can be seen, most topics are quite distinct.

(2) Then, for each user, we compute the distance between the topics that were added via the retweets and the topics in the user’s self-tweets. In fact, this was done using two different measures: The first measure (denoted measure A), simply computes the average of distances between each topic in the self-tweets and each added topic. For example, if Jane tweets about topics A, B, and C and adds topics D and E, we compute the distance for Jane as the average of the distances A-D, A-E, B-D, B-E, C-D, and C-E. In the second measure (denoted measure B), we average the minimal distance between each added topic and the topics discussed in the self-tweets. For example, if Jane tweets about topics A, B, and C and adds topics D and E, we average the min of (D-A, D-B, and D-C) and the min of (E-A, E-B, and E-C).

(3) We compute the distance between the topics added via the random retweets and the topics in the user’s self-tweets. As in (2), we use measures (A) and (B) to compute the distances between the topics added via the random retweets and the self-tweets.

The result are presented in the main text. We find that the topics added via the user’s real retweets are closer to his self-tweets than are those added via the random retweets.

![](/api/attachments/HDNYXTXS/fulltext/images/2a8104415af2dc29583d5043f9462c9405e19e635e90e8310d26bc6f13a039fa.jpg)

Figure K1. Histogram of Distances

## References

Aletras, N., and Stevenson, M. 2014. “Measuring the Similarity between Automatically Generated Topics,” in Proceedings of the ${ \cal I } 4 ^ { t h }$ Conference of the European Chapter of the Association for Computational Linguistics, pp. 22-27.

Arun, R., Suresh, V., Veni Madhavan, C. E., and Narasimha Murthy, M. N. 2010. “On Finding the Natural Number of Topics with Latent Dirichlet Allocation: Some Observations,” in Advances in Knowledge Discovery and Data Mining, M. J. Zaki, J. X. Yu, B. Ravindran, and V. Pudi (eds.), Berlin: Springer, pp. 391-402.

Cao, J., Xia, T., Li, J., Zhang, Y., and Tang, S. 2009. “A Density-Based Method for Adaptive LDA Model Selection,” Neurocomputing— $- I { \boldsymbol { \delta } } ^ { t h }$ European Symposium on Artificial Neural Networks 2008, pp. 1775-1781.

Deveaud, R., SanJuan, E., and Bellot, P. 2014. “Accurate and Effective Latent Concept Modeling for Ad Hoc Information Retrieval,” Document numérique (17:1), pp. 61-84.

Griffiths, T. L., and Steyvers, M. 2004. “Finding Scientific Topics,” Proceedings of the National Academy of Sciences (101, Supplement 1), pp. 5228-5235.
