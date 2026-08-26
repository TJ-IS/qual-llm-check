---
otero_id: 3060
otero_key: "XS6RU38Z"
title: "Social media analytics and value creation in urban smart tourism ecosystems"
authors: "Tobias Brandt; Johannes Bendler; Dirk Neumann"
year: "2017"
journal: "Information & Management"
doi: "10.1016/j.im.2017.01.004"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
## Accepted Manuscript

Title: Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Authors: Tobias Brandt, Johannes Bendler, Dirk Neumann

![](/api/attachments/XS6RU38Z/fulltext/images/10ba487a4f1d77c7e38bdd3f5c4bbbc44f0f27ff3a9cdd2d4f338fc9fcff2756.jpg)

PII: S0378-7206(17)30012-5

DOI: http://dx.doi.org/doi:10.1016/j.im.2017.01.004

Reference: INFMAN 2972

To appear in: INFMAN

Received date: 31-5-2016

Revised date: 22-12-2016

Accepted date: 7-1-2017

Please cite this article as: Tobias Brandt, Johannes Bendler, Dirk Neumann, Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems, Information and Management http://dx.doi.org/10.1016/j.im.2017.01.004

This is a PDF file of an unedited manuscript that has been accepted for publication. As a service to our customers we are providing this early version of the manuscript. The manuscript will undergo copyediting, typesetting, and review of the resulting proof before it is published in its final form. Please note that during the production process errors may be discovered which could affect the content, and all legal disclaimers that apply to the journal pertain.

# Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Tobias Brandt (Corresponding author)

Rotterdam School of Management, Erasmus University Burgemeester Oudlaan 50 Mandeville (T) Building, Room 9-58

3062 PA Rotterdam, The Netherlands

brandt@rsm.nl

Johannes Bendler

Geospin GmbH

Im Gaertle 21

79104 Freiburg, Germany

jbendler@geospin.de

Dirk Neumann

University of Freiburg

Platz der Alten Synagoge

79098 Freiburg, Germany

dirk.neumann@is.uni-freiburg.de

## Highlights

 We model an urban smart tourism ecosystem enabled by social media analytics

 A demonstration case using 600,000 Twitter messages in San Francisco is introduced

 We conduct a combination of spatial and semantic analyses on the data set

 Insights on user presence and environmental and topical engagement are revealed

 We formulate value propositions for various stakeholders in the ecosystem

## Abstract

In this article, we demonstrate the potential value that the spatial and semantic analysis of social media messages can provide to smart tourism ecosystems. Building upon a showcase of 600,000 Twitter messages in San Francisco, we illustrate insights for stakeholders within the tourism sector from various analyses, including kernel density estimation and latent Dirichlet allocation. We show that social media analytics captures spatial patterns within the city that relate to the presence of users and the environmental and topical engagement. Furthermore, we outline how these patterns serve as an input to value creation for smart urban tourism.

## Keywords

Smart Tourism; Social Media Analytics; Value Creation; Location-Based Services; Spatial Analysis; LDA

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

## 1. Introduction

The tourism sector is a major driver of global economic growth, contributing almost 10% of the global GDP in 2014 through direct and indirect effects. Essentially, every 10th dollar spent and more than a quarter billion jobs throughout the world can be linked to the travel and tourism industries (World Travel & Tourism Council 2015). Like most other economic sectors, tourism is heavily affected by digitization and the rise of internet-based services. Recent research has outlined, for instance, the effect of Airbnb (Zervas et al. 2015) and online reviews (Chaves et al. 2012; Yacouel and Fleischer 2012) on the hotel market or the use of social media in a travel and tourism context (Majid et al. 2013; Sigala et al. 2012). Nevertheless, a holistic and integrative perspective on how digitization affects all stakeholders in tourism activities is still in its infancy. Gretzel et al. (2015a) took an initiative by defining smart tourism as “tourism supported by integrated efforts at a destination to collect and aggregate/harness data” and “to transform that data into on-site experiences and business value-propositions with a clear focus on efficiency, sustainability and experience enrichment” (p. 181). This notion is further substantiated by Gretzel et al. (2015b) through the introduction of smart tourism ecosystems (STEs) that link the stakeholders of tourism services with the digital environment.

In this article, we build upon research by Gretzel et al. (2015b) on STEs and by Bendler et al. (2014) on social media analytics (SMA) to demonstrate how the spatial and semantic analysis of geo-tagged social media messages may become a powerful vehicle for value creation in STEs. Our research specifically addresses the following objectives:

1. We position SMA within an STE framework.

2. We demonstrate insights that can be derived through SMA using a showcase of more than 600,000 geo-tagged Twitter messages for the city of San Francisco.

3. We outline the resulting value propositions with respect to the stakeholders within the STE.

In the following sections, we successively address these research objectives. The final section concludes and provides an outlook on future research paths.

## 2. SMA within an STE Framework

Over the past several years, the widespread use of mobile devices has heavily boosted the growth of social web services. Their users’ online activity is a tremendous treasure trove of data—in March 2013, Flickr users uploaded more than 3.5 million new images per day (Jeffries 2013); during December 2014, Facebook had an average of 890 million daily active users, of whom 745 million accessed the service from mobile devices (Facebook, Inc. 2014). On an average day, more than 500 million Twitter messages are sent (Oreskovic 2015) and 80 million photographs are shared on Instagram, collecting 3.5 billion likes (Instagram 2016). Consequently, SMA has become an increasingly relevant topic to researchers and corporate managers (Fan and Yan 2015; Harvard Business Review Analytic Service 2010). For instance, Stieglitz et al. (2014) emphasized the relevance of SMA as a laboratory for natural experimentation in social science and business research, while Fan and Gordon (2014) analyzed a large hotel corporation using SMA to substantially improve customer satisfaction. From a corporate management perspective, Risius and Beck (2015) outlined the importance of social media to customer loyalty, while Chung and Koo (2015) and Chung et al. (2015) analyzed the relationship between social media and travel behavior. This connection between social media activity and insights related to tourism issues has been the focus of several studies, which largely rely on two different types of geo-tagged data sources— image-hosting web services such as Flickr and microblogging services such as Twitter. For instance, Wood et al. (2013) used photographs on Flickr to estimate the number of visitors at various recreational sites. Girardin et al. (2008) used Flickr uploads to trace tourists’ movements in Rome and compared them to spatial patterns from text messages provided by a telecommunication company. Chua et al. (2016) and Hawelka et al. (2014) used Twitter messages

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

to assess users’ mobility patterns on a regional and global scale, respectively. The appeal of Twitter messages lies in the information they contain beyond photo attachments and spatial coordinates, such as textual information contained in the tweet’s body and hashtags, as well as insights on social links expressed through likes and retweets. For instance, Abbasi et al. (2015) used a text mining approach to uncover trip purposes from tweets. However, they also caution that extracting information from messages is challenging, because users may not necessarily conduct specific activities at the times they are tweeting about them.

Nevertheless, both Tilly et al. (2015) and Bendler et al. (2014) provided evidence supporting the reliability of user-generated content as displayed on social media platforms. Tilly et al. (2015) analyzed macrolevel information on tourism that were obtained from online travel reviews, emphasizing the earlier availability and high correlation with the information provided by official sources. Bendler et al. (2014) demonstrated the robust spatial and temporal relationships between the social media activity (Twitter messages) and the environmental features in their surroundings (such as bars or museums). However, their analysis was limited to a geolocation. In this study, we further refine this approach through additional layers of content analysis. On the one hand, we consider photo attachments of tweets as a measure of the degree to which users engage with their environmental surroundings. This relates by Girardin et al. (2008) and Wood et al. (2013), but we provide a more detailed, microlevel analysis of the data. On the other hand, we investigate specific topics in the Twitter messages as well as their spatial distribution. This extends Abbasi et al.'s (2015) approach by identifying specific events and event locations instead of broad categories. We use the resulting insights to position SMA as a source of value creation in STEs.

Gretzel et al. (2015b) described a typical STE as an interaction space supported by a digital ecosystem and populated by various types of players. They broadly distinguished touristic consumers (TC), residential consumers (RC), tourism suppliers (TS), suppliers from other

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

industries (OS), government agencies, destination marketing organizations (DMO), and intermediaries. These types are not necessarily discrete as a single player can fulfill multiple roles. Gretzel et al. (2015b) also found that STEs are not created but rather are evolved if the necessary technological and regulatory conditions are fulfilled. The rather abstract concept of STEs is applied in a more practical context by, for instance, Park et al. (2016) and Buonincontri and Micera (2016). Park et al. (2016) analyzed how local governments in Korea use Facebook to promote tourism, thereby transforming Facebook into an STE platform. Buonincontri and Micera (2016) analyzed the best practices for the creation of smart tourism destinations from a technological perspective. This article integrates these approaches by investigating the role of social media platforms and analytics as a foundation of STEs.

Specifically, we model an STE based on social media and SMA as illustrated in Figure 1. The technological conditions as defined by Gretzel et al. (2015b) are set by the necessary hardware and software infrastructure, both of which are provided by suppliers with their primary business outside the tourism sector. On the one hand, mobile devices enable users to communicate anytime from essentially any place. Internet connectivity is very reliable, particularly in urban settings; however, the reception and transmission speed are continuously improving even in more rural touristic areas. Whereas, social media provides users with platforms through which to communicate and reach their friends, families, and followers. Mobile devices and social media platforms together enable users to reflect on and share their experiences as they occur (or shortly thereafter). As outlined with the black lines in Figure 1, these users can be both residential consumers and touristic consumers. However, this exchange is not unidirectional, because, in turn, the users continuously supply the infrastructure providers with data (indicated by the red and blue lines). From our perspective, two types of data are particularly relevant—spatiotemporal data that provide information on where the users are and at what times and content data that reflect the users’ experiences.

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

The data received by the providers of the mobile devices (and, similarly, by the telecommunications carriers) allow a detailed tracing of the users’ movements. Although it has been analyzed in a touristic context (Girardin et al. 2008; Raun et al. 2016), its use is usually heavily regulated. Therefore, these data are not well suited to serve as a widely applicable basis for touristic services. In contrast, the data submitted to social media platforms are, to a given extent, open by design. Depending on the platform, users want their messages, pictures, videos, and locations to be widely accessible and want to share them with the world. The provision of this valuable information to third parties consequently constitutes a crucial building block of the business models of most social media platforms (Delo 2013). In an STE, social media platforms constitute a source of value, a basis for value creation, to a variety of players—including tourism suppliers, DMOs, and government agencies. However, to handle the sheer volume of observations, analytics methods are required to transform social media data into actionable insights.

In the next section, we substantiate the proposed model using a showcase of geo-referenced social media messages in the city of San Francisco.

## 3. Showcase: Analyzing Twitter Messages in San Francisco

Over the past decade, Twitter has become a global social force (Broersma and Graham 2013; Gerbaudo 2012; Weller et al. 2014). As outlined earlier, each month, hundreds of millions of users send billions of messages expressing their thoughts and experiences. A substantial share of these messages is geographically referenced (geo-tagged) or can be geographically traced (Weidemann and Swift 2013), enabling an association between the message, its content, and the specific place and time. As proposed earlier, analyzing these associations between location, time, and content may provide valuable insights to various stakeholders in an STE as they reflect experiences and activities of the users who send them. We want to make clear at the outset, though, that such an analysis is just one building block in the evolution of an STE whose overall success depends on

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

the successful use and linking of various sources of information and services. Most users of Twitter and most social media services are younger and better educated, with a slightly higher number of male users, which is not representative of the overall population (Duggan et al. 2015). Nevertheless, keeping this limitation in mind, they are still representative of a large share of the population and constitute a very relevant target group for tourism suppliers.

In section 3.1, we describe the data set used for this study. Second, we outline the methodology of and insights drawn from the spatial analysis of messages and message attachments. Results from the semantic analysis of the messages are presented in section 3.3.

## 3.1. Data Set

We have acquired an extensive data set of more than 600,000 geo-tagged tweets from the metropolitan area of San Francisco that were posted between August 1, 2013 and October 31, 2013. The data set was directly obtained from Twitter and was not distorted or biased, representing the complete set of geo-tagged tweets from this area within the given time span. Each data point contains the text of the tweet, the geographical location, the user who posted it, and other additional information, such as URLs and images contained in the tweet. As depicted in Figure 2, the messages exhibit a relatively stable temporal pattern within a day. Not surprisingly, Twitter activity is the lowest during the night with around 50 to 100 messages. The hourly volume of tweets increases during the morning hours and peaks at around 12 p.m., followed by a slight drop until 3 p.m. Afternoon and early evening cover the most active phase of the day, peaking at around 6 p.m. After that peak, the tweet volume steadily drops until it returns to the nightly baseline. The relative consistency of this daily pattern, illustrated by the boxplots, provides a first confirmation that Twitter activity is closely linked to daily habits and activities of the users involved. This agrees with the finding of Bendler et al. (2014) that Twitter activity is related to points of interest in the vicinity of the user, such as restaurants and bars.

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

However, the potential insights that can be gathered from spatial SMA are further underscored when we compare intraday patterns between different neighborhoods in San Francisco. The left panel in Figure 3 illustrates the difference in average hourly Twitter volume (as share of daily volume) in four districts of San Francisco: South of Market, Pacific Heights, Golden Gate Park, and the Sunset District. The right panel shows the offset between each district and the average relative tweet volume of the entire city. The districts showcase different types of areas that are related to different activities. Thus, they reveal different activity patterns throughout the day. South of Market, a busy business district, shows a pattern that is similar to the citywide pattern, having an above-average activity rate during the daytime and a below-average activity rate in the evening hours. Pacific Heights and the Sunset District are residential areas and their patterns are very similar. In these districts, we observe that the Twitter activity is above the citywide average during the morning and evening hours and below the average during the working hours. Golden Gate Park, a recreational area, has an entirely different pattern. It exhibits below-average activity during most of the day but shows an increase from the noon to the early evening. The variation in these patterns provides further confirmation of the link between Twitter activity and the daily habits of the users. In the remainder of this section, we investigate the insights that can be derived from the spatial variation of such social media activity and that are potentially valuable in the tourism context.

## 3.2. Spatial Analysis of Messages and Attachments

From a spatial perspective, Twitter messages are discrete points. However, the tweet itself is often related to the vicinity of this point. For instance, a tweet that is posted after a visit to a museum might be associated with a point that is a certain distance from the museum because the user may be walking while typing the tweet. Similarly, a tweet that contains a picture of the Golden Gate Bridge in San Francisco may be posted from the point where the picture was taken while referring to another point a certain distance away (the bridge). A widely accepted method to reflect these

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

spatial relationships is the kernel density estimation (KDE, e.g. Silverman 1986; Wagner et al. 2015; Xie and Yan 2008). The KDE turns the discrete points into a smooth curve that represents the density of tweets across the city area of San Francisco. For our analysis, we define a set ?? that contains all Twitter messages. $m _ { i } \in M$ is an individual tweet and is represented by the following tuple:

$$
m _ {i} = (\lambda_ {i}, \phi_ {i}, t _ {i}, c _ {i}, a _ {i}).
$$

Here, $\lambda _ { i }$ and $\phi _ { i }$ represent the tweet’s longitude and latitude, respectively. $t _ { i }$ is the time the tweet was posted, $c _ { i }$ is the textual message, and $a _ { i }$ is a binary indicator of whether the message contains an attachment.

We can, subsequently, calculate the tweet density at any location $p _ { j } = \left( \lambda _ { j } , \phi _ { j } \right)$ within the city using the KDE equation as follows:

$$
\delta (p _ {j}) = \sum_ {m _ {i} \in M} \frac {1}{\sqrt {2 \pi}} e ^ {- \frac {1}{2} \left(\frac {d (m _ {i} , p _ {j})}{2 5 0}\right) ^ {2}}.
$$

The expression within the sum is the KDE with a Gaussian kernel and a standard deviation of 250 m. $d ( m _ { i } , p _ { j } )$ is the distance between the location $p _ { j }$ and the tweet $m _ { i }$ . The resulting kernel is illustrated in Figure 4. Generally, the highest density value—approximately 0.4—is obtained if $p _ { j }$ and $m _ { i }$ coincide and decreases as the distance between them increases. At a distance of about three standard deviations, density values are only marginally above zero.

The choice of the standard deviation of the Gaussian kernel is critical as it defines the bandwidth of the KDE, that is, the size of the area the tweet is mapped to. For example, a standard deviation of 250 km would produce density values that are almost equal across the entire city area of San Francisco, whereas a standard deviation of 250 cm would essentially leave each tweet unchanged as a point from a citywide perspective. The choice of 250 m in this showcase is the result of

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

theoretical considerations, such as the average walking speed of people (Levine and Norenzayan 1999), and of comparing the effects of different bandwidths.

Applying the KDE to each tweet, we could visualize the density of Twitter messages during the analyzed time span using a heatmap technique, as illustrated in Figure 5. A few things become immediately obvious. The downtown area (1) clearly exhibits the highest number of tweets. This is not surprising as it has the highest density of people—residents, employees, and tourists—during most of the day. Particularly Market Street, which is shown by a dark straight line crossing through the dark blue area, is a busy shopping area heavily frequented by tourists. However, high Twitter activity—represented by the second-darkest shade of blue—can be observed in the entire greater downtown area, including iconic neighborhoods such as Mission, Castro, Haight-Ashbury, and stretches of Golden Gate Park.

We can also make several other interesting observations. The areas facing the Golden Gate Bridge and Alcatraz island (2) exhibit high Twitter activity—particularly on the eastern side—reflecting their touristic appeal. A similarly high density can be observed for Candlestick Park (3), which was home to the local football franchise until the end of 2013. However, tweet density is not exclusively high in touristic areas. For instance, the campus of the San Francisco State University also shows high activity, reflecting the appeal of Twitter among college students.

Nevertheless, these results suggest that analyzing spatial patterns of activity on social media services such as Twitter can serve as a prospective value source in STEs. They visualize the presence of Twitter users, and the showcase of San Francisco illustrates what appears to be a strong touristic motivation for using Twitter. However, as outlined through the example of college campuses, it is clearly not the only motivation and the analysis of user presence is just a starting point.

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

What differentiates tourists from other social media users is the characteristic practice of taking pictures of their touristic endeavors and posting them on social media (Boley et al. 2013; Lo et al. 2011). Subsequently, the analysis of tweets that are combined with photo or video attachments may provide further insights. Figure 6 visualizes the corresponding heatmap for tweets with attachments in San Francisco during the observation period. First, we can clearly observe that the number of tweets with attachments is substantially lower than the overall number of tweets, reflected in comparatively low densities. Nevertheless, there are similarities but also striking differences compared to the patterns in Figure 5. On the one hand, the downtown area continues to show the highest density values, although even here differences can be observed. For instance, in contrast to Figure 5, the Castro and Mission districts (1) are among the areas with the highest density. On the other hand, certain areas increase in relevance relative to their vicinities. The areas facing the Golden Gate Bridge (2) show high densities, again particularly on the eastern side, where the prison island of Alcatraz provides another touristic attraction. Similar high densities can be observed for Golden Gate Park (3) and the San Francisco Zoo (4).

Attaching a picture reflects that the Twitter users engage with their environment and want to share this experience (Kim and Fesenmaier 2015; Munar and Jacobsen 2013, 2014). Although Figure 6 provides certain insights into this environmental engagement, the sheer number of tweets in certain areas—such as downtown—may distort our impression of this phenomenon. Hence, we visualize the conditional probability that a tweet contains an attachment given that it is posted from a specific location in Figure 7. Effectively, the heatmap divides the density values in Figure 6 by the values in Figure 5, providing a completely new perspective.

Most evidently, the downtown area loses its dominance over the rest of the map. Although there are certain areas of higher probabilities, such as the coastal zone facing the Golden Gate Bridge and Alcatraz (1), overall probability values are not especially high. On the other hand, certain areas

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

suddenly move into focus, such as the Lands End park facing the Golden Gate (2). However, large parts of the western coastal line, including Ocean Beach (3) and the Fort Funston area (4), also exhibit high probabilities. High probability values even extend into the ocean, representing ships from which pictures of the city were taken. We can also observe a high probability value for a part of Golden Gate Park (5). Interestingly, there are also a few areas that seemed completely ordinary in the preceding figures, which turn out to be associated with high attachment probabilities. The first is Twin Peaks (6), the famous hills looking down onto the city, and the second is John McLaren Park with the Jerry Garcia Amphitheater (7), a regular performance stage. Furthermore, Pier 80 (8) housed Team Oracle during the America’s Cup in 2013. These areas engage Twitter users with their environment—either through a scenic view of the city or entertainment—increasing the likelihood of sending messages with photo or video attachments.

Overall, analyzing the spatial patterns of tweet attachments across the city provides tourismfocused insights as we can identify areas in which users engage with their environment. For that purpose, both the absolute and relative numbers of tweets with attachments provide unique perspectives. The former helps to identify areas for which a high number of tweets from residents and the working population may overshadow its touristic value—as for the Castro and Mission districts in Figure 5. The latter achieves the opposite and puts areas into focus that may be less frequented, but strongly engage people who are there.

## 3.3. Textual Analysis

With the increasing popularity of Twitter, in recent years, various research groups have begun to analyze the textual information contained in the messages. Steiger et al. (2015) provided a detailed overview of studies that combine spatial and semantic analyses of Twitter messages. Furthermore, recent publications have used topic analyses of tweets to reveal urban dynamics (Kling and Pozdnoukhov 2012) and to predict criminal incidents (Gerber 2014). Both studies applied latent

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Dirichlet allocation (LDA, Blei 2012) to model a prespecified number of hidden topics within the messages. Gerber (2014) found that, although the inclusion of Twitter topics improves crime prediction, it is difficult to argue why a specific topic improves the prediction of a particular crime type. Nevertheless, from a tourism point of view, exploring the spatial dimension of LDA topics may prove valuable in identifying how users engage with particular topics—such as sports or entertainment events—in certain areas. Cheng et al. (2014), however, cautioned that the shortness of Twitter messages may prove challenging to LDA because the method usually assumes that a single message relates to several topics. We address this issue by aggregating tweets at the spatial level. Specifically, we construct a grid that splits the observation area into $6 4 \times 8 9$ small tiles as follows:

$$
G = \left[ \begin{array}{c c c} g _ {1, 1} & \dots & g _ {1, 8 9} \\ \vdots & \ddots & \vdots \\ g _ {6 4, 1} & \dots & g _ {6 4, 8 9} \end{array} \right]
$$

with each $g _ { x , y } \in G$ containing the text of all messages sent from that tile. Each tile has an edge length of 0.002 degrees latitude and longitude. This translates to effective dimensions of approximately 220 m vertically and 175 m horizontally, resulting from the curvature of the earth. This choice of dimensions proved to strike the best balance between a high resolution, such that spatial differences can be clearly identified, and a sufficient aggregation of tweets to produce meaningful LDA results, as shown below.

We applied the LDA to the 5,696 grid tiles using the topicmodels package in R (Hornik and Grün 2011). In a first step, we removed URLs, punctuations, numbers, and stop words<sup>1</sup> from the corpus and stemmed the remaining words. In a second step, we converted the corpus into a document-term matrix and removed sparse terms, as well as empty documents. We applied LDA with $k =$

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

[10,20,30, … ,100] topics to the resulting matrix, eventually determining a total of 30 topics to be the most insightful variants. The topics are summarized in detail in Table 2 in the appendix along with the 10 most prominent words in each topic. Although it is normal for LDA to have a high share of similar-looking topics—for instance, topics 2, 25, and 29—could detect certain topics that relate to specific characteristic attractions or events. For example, topic 1 relates to VMworld, a large conference on virtualization and cloud computing that took place during the observation period. Topic 8 addresses the local baseball franchise, the San Francisco Giants, whereas topic 12 refers to Outside Lands, an annual music festival that takes place in Golden Gate Park. Furthermore, topic 15 contains references to the Castro and Mission districts, providing further validation of the insights from Figure 6.

Since the documents used as input for the LDA were grid tiles, we can project the results on the map of San Francisco to illustrate the spatial distribution of specific topics across the city. As shown in Figure 8, there is a strong relationship between the topics under consideration and their spatial patterns. The top left panel visualizes the distribution of topic 1, which is focused on the downtown area (1). The Moscone Center, where VMworld was held, is situated approximately at the center of the circled area. A similarly strong spatial relationship between an event-focused topic and the place where the event is held can be observed for topics 8 and 12. Tiles that are assigned to topic 8 are clustered around the AT&T Park (2), where the San Francisco Giants play their home games. Topic 12 is associated with several tile clusters in and around Golden Gate Park (3), where the Outside Lands festival takes place. Furthermore, topic 15 is clustered in the iconic Castro neighborhood. The social media activity that is generated in this city quarter is an example of a touristically appealing area where topical engagement and environmental engagement (as illustrated in Figure 6) coincide.

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

## 4. Discussion and Value Propositions

San Francisco serves well as a demonstration case because the areas of touristic appeal in the city are well known. The insights generated by SMA can subsequently be compared to actual attractions and events within the city. The results provide starting points for the cities that are less developed as tourist destinations to analyze tourist behavior and reveal appealing attractions and events.

In the preceding section, we described three types of spatial indicators that can be revealed through SMA and may serve as a basis for value generation in an urban STE: presence, environmental engagement, and topical engagement. Recalling potential beneficiaries from SMA as outlined in Figure 1—governments, tourism suppliers, and destination marketing organizations—we juxtapose both dimensions in Table 1 to identify prospective value sources in an SMA-enabled STE.

The dimension of presence as reflected in the density of tweets across the city provides stakeholders with several opportunities to provide value to tourists. Although we have focused on the spatial dimension in our showcase analysis, a simple analytical addition would be to consider spatial patterns at different times of day. Using this information, city administrators can optimize public services such as public transportation to allow tourists to easily travel between different areas of touristic interest. Tourism suppliers can use the same information to optimize advertisement campaigns—both through location-based digital services as well as traditional posters and billboards—to reach many potential visitors at the right time of the day. Furthermore, both tourism suppliers and DMOs can use information on public presence to identify appealing emerging destinations and optimize touring schedules accordingly.

In our analysis, we argue that attaching pictures and videos to tweets reflects the engagement of users with their environment. This environmental engagement provides additional starting points for value generation in an SMA-enabled ecosystem. For instance, public administrations and

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

tourism suppliers can identify good vantage points for photography from spatial information depending on the probability of taking a picture at a given location as illustrated in Figure 7. The former can use this information to make these spots more easily accessible for tourists whereas the latter can offer tours to these locations and provide additional services in the vicinity, such as food and drinks. Furthermore, stakeholders in the STE in general can discover new scenic attractions from this information, as well. Particularly in areas that are not as developed for tourism as San Francisco, information on environmental engagement can help administrations and businesses to become more aware of the potential attractions their cities might offer to tourists.

The LDA conducted in the last part of our showcase analysis demonstrated a certain topical engagement of Twitter users. Governments can use this information to assess how specific events affect urban dynamics. For instance, festivals and sports game may lead to crowding in specific areas. Although these can usually be anticipated, it is often unclear how these crowds disperse after the event has ended. Administrations can use the spatial social media information to learn from these events how to provide a safe and efficient tourism environment. Businesses, on the other hand, can use the spatial and temporal variation in topical engagement to assess how specific events create anticipation—buzz—in the city during the preceding days or weeks and act accordingly. Overall, the showcase demonstrates that social media can serve as a platform to develop an STE within a city. SMA—here, a combination of spatial and semantic analyses—can provide stakeholders within this ecosystem with valuable information. Thus, they are empowered to provide a better, safer, and more efficient tourism experience in the city.

## 5. Conclusion

In this article, we integrated research streams on smart tourism, spatial analysis, and text mining to investigate how social media can provide a platform to develop smart services for urban tourism. Building upon the STE perspective of Gretzel et al. (2015b), we summarized the role of social

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

media within such an ecosystem and position SMA as a value source in its context. Through an extensive showcase study for the city of San Francisco that includes a data set containing more than 600,000 geo-referenced Twitter messages, we demonstrated the potential value of spatial and semantic analytics to the tourism sector. More specifically, by combining methods that analyze position, textual content, and photo attachments of tweets, we showed that the information contained in social media data provides insights into the presence, environmental engagement, and topical engagement of users across the city. From these results, we derive prospective value propositions for various stakeholders within the ecosystem, such as public administrations and tourism suppliers.

Our work provides immediate implications for both academia and practice. From an academic perspective, we contribute to the theoretical modeling of emerging digital urban ecosystems. Our focal showcase analyzes an STE, and we provide a detailed perspective on how various stakeholders interact within such a system. Recalling Figure 1, we particularly emphasize the respective roles of hardware and platform providers in the emergence of an STE. The former allows consumers to access the internet across the city with mobile devices, whereas the latter enables them to freely share impressions, insights, and opinions. This open, user-generated content is subsequently systematically analyzed to provide value to tourism suppliers, government agencies, and—ultimately—the consumers themselves. Furthermore, we outlined the value of considering all contextual facets of a data point—specifically location, time, textual content, and attachments— and how they combine to express different kinds of user engagement. This contribution in particular is not limited to the tourism sector, but extends to the broader discussions surrounding location-based services (Junglas and Watson 2008) and smart cities (Brandt et al. 2016). As a city is an ecosystem with very distinct spatial and temporal patterns, understanding these dynamics is crucial toward designing successful interventions and applications to improve urban life.

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Our insights translate directly into managerial implications. We outline that city administrators and businesses can begin to foster the emergence of an STE through third-party platforms—social media. Thus, cities do not necessarily need to invest into infrastructure initially, instead relying on the ubiquity of mobile devices and social media. This potentially offers smart solutions also to the cities and regions without the financial resources to realize ambitious smart tourism plans. While our paper presents a proof-of-concept, we provide a detailed discussion of possible value streams enabled by our methodological approach. For instance, the emergence of particular events as spatially attributed topics on social media allows organizers to better direct promotion campaigns and city officials to anticipate mobility flows. In addition, the degree of environmental engagement exhibited by tourists aids the city administration and tourism suppliers in noticing and better understanding the touristic appeal of certain locations.

As we consider our work a starting point for research at the intersection of SMA, spatial analysis, and smart tourism, there are certain limitations. Although San Francisco provides a powerful showcase, future studies will have to validate our results for other cities and derive conditions for the generalizability of the implications. Particularly the transferability to areas that are less developed for tourism, while appealing, remains unclear. Even though we could rely on an extensive data set containing more than 600,000 geo-tagged tweets, this set only captures the months of August, September, and October. Seasonal effects might reduce the explanatory power of the methods presented. Furthermore, we focused on English-language tweets for this showcase, which limits the implications that can be derived for international tourism.

However, these limitations point to a range of promising areas for future research. The methodology used—both for the spatial analysis and text mining—should be compared to other approaches for further validation and improvement. In addition, the implications for value creation in STEs outlined in this article require further investigation, for instance from a business model

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

perspective. Finally, the insights presented in this paper summarize the potential benefits of spatial SMA in a tourism context for governments, businesses, and ultimately the tourists themselves. However, they result from one showcase featuring the analysis of one microblogging service in one city over the course of 3 months. In future studies, they need to be replicated and verified for other geographical settings, social media services (e.g. Instagram, Swarm), and languages.

## References

Abbasi, A., Rashidi, T. H., Maghrebi, M., and Waller, S. T. 2015. “Utilising Location Based Social Media in Travel Survey Methods: bringing Twitter data into the play,” in Proceedings of the 8th ACM SIGSPATIAL International Workshop on Location-Based Social Networks, Article 1.

Bendler, J., Wagner, S., Brandt, T., and Neumann, D. 2014. “Taming Uncertainty in Big Data: Evidence from Social Media in Urban Areas,” Business & Information Systems Engineering (6:5), pp. 279–288.

Blei, D. M. 2012. “Probabilistic topic models,” Communications of the ACM (55:4), pp. 77–84.

Boley, B. B., Magnini, V. P., and Tuten, T. L. 2013. “Social media picture posting and souvenir purchasing behavior: Some initial findings,” Tourism Management (37), pp. 27–30.

Brandt, T., Cudden, J., Ketter, W., Prendergast, D., Sakurai, M., and Watson, R. 2016. “Smart Cities and the Role of IS Research in Improving Urban Life,” in ICIS 2016 Proceedings, Paper 4.

Broersma, M., and Graham, T. 2013. “Twitter as a News Source,” Journalism Practice (7:4), pp. 446–464.

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Buonincontri, P., and Micera, R. 2016. “The experience co-creation in smart tourism destinations: a multiple case analysis of European destinations,” Information Technology & Tourism (16:3), pp. 285–315.

Chaves, M. S., Gomes, R., and Pedron, C. 2012. “Analysing reviews in the Web 2.0: Small and medium hotels in Portugal,” Tourism Management (33:5), pp. 1286–1287.

Cheng, X., Yan, X., Lan, Y., and Guo, J. 2014. “BTM: Topic Modeling over Short Texts,” IEEE Transactions on Knowledge and Data Engineering (26:12), pp. 2928–2941.

Chua, A., Servillo, L., Marcheggiani, E., and Moere, A. V. 2016. “Mapping Cilento: Using geotagged social media data to characterize tourist flows in southern Italy,” Tourism Management (57), pp. 295–310.

Chung, N., Han, H., and Koo, C. 2015. “Adoption of travel information in user-generated content on social media: The moderating effect of social presence,” Behaviour & Information Technology (34:9), pp. 902–919.

Chung, N., and Koo, C. 2015. “The use of social media in travel information search,” Telematics and Informatics (32:2), pp. 215–229.

Delo, C. 2013. Meet the Gatekeepers to Twitter and Facebook Data: Gnip, DataSift and Topsy are sanctioned tweet resellers while Facebook keeps its conversations under wraps. http://adage.com/article/digital/meet-gatekeepers-twitter-facebook-data/240365/. Accessed 29 January 2016.

Duggan, M., Ellison, N. B., Lampe, C., Lenhart, A., and Madden, M. 2015. Demographics of Key Social Networking Platforms. PewResearchCenter. http://www.pewinternet.org/2015/01/09/demographics-of-key-social-networking-platforms-2/. Accessed 27 May 2016.

Facebook, Inc. 2014. Annual Report 2014.

Fan, W., and Gordon, M. D. 2014. “The power of social media analytics,” Communications of the ACM (57:6), pp. 74–81.

Fan, W., and Yan, X. 2015. “Novel applications of social media analytics,” Information & Management (52:7), pp. 761–763.

Gerbaudo, P. 2012. Tweets and the streets: Social media and contemporary activism, London: Pluto Press.

Gerber, M. S. 2014. “Predicting crime using Twitter and kernel density estimation,” Decision Support Systems (61), pp. 115–125.

Girardin, F., Calabrese, F., Fiore, F. D., Ratti, C., and Blat, J. 2008. “Digital Footprinting: Uncovering Tourists with User-Generated Content,” IEEE Pervasive Computing (7:4), pp. 36– 43.

Gretzel, U., Sigala, M., Xiang, Z., and Koo, C. 2015a. “Smart tourism: foundations and developments,” Electronic Markets (25:3), pp. 179–188.

Gretzel, U., Werthner, H., Koo, C., and Lamsfus, C. 2015b. “Conceptual foundations for understanding smart tourism ecosystems,” Computers in Human Behavior (50), pp. 558–563. Harvard Business Review Analytic Service 2010. The New Conversation: Taking Social Media from Talk to Action. https://hbr.org/resources/pdfs/tools/16203\_HBR\_SAS%20Report\_webview.pdf. Accessed 5 January 2016.

Hawelka, B., Sitko, I., Beinat, E., Sobolevsky, S., Kazakopoulos, P., and Ratti, C. 2014. “Geolocated Twitter as proxy for global mobility patterns,” Cartography and Geographic Information Science (41:3), pp. 260–271.

Hornik, K., and Grün, B. 2011. “topicmodels: An R Package for Fitting Topic Models,” Journal of Statistical Software (40:13), pp. 1–30.

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Instagram 2016. Instagram Stats. https://www.instagram.com/press/. Accessed 5 January 2016.

Jeffries, A. 2013. The man behind Flickr on making the service 'awesome again': Markus Spiering talks photography, daily habits, and life under Marissa Mayer. http://www.theverge.com/2013/3/20/4121574/flickr-chief-markus-spiering-talks-photos-andmarissa-mayer. Accessed 5 January 2016.

Junglas, I. A., and Watson, R. T. 2008. “Location-based services,” Communications of the ACM (51:3), pp. 65–69.

Kim, J., and Fesenmaier, D. R. 2015. “Sharing Tourism Experiences: The Posttrip Experience,” Journal of Travel Research (advance online publication).

Kling, F., and Pozdnoukhov, A. 2012. “When a city tells a story: urban topic analysis,” in Proceedings of the 20th International Conference on Advances in Geographic Information Systems, pp. 482–485.

Levine, R. V., and Norenzayan, A. 1999. “The Pace of Life in 31 Countries,” Journal of Cross-Cultural Psychology (30:2), pp. 178–205.

Lo, I. S., McKercher, B., Lo, A., Cheung, C., and Law, R. 2011. “Tourism and online photography,” Tourism Management (32:4), pp. 725–731.

Majid, A., Chen, L., Chen, G., Mirza, H. T., Hussain, I., and Woodward, J. 2013. “A context-aware personalized travel recommendation system based on geotagged social media data mining,” International Journal of Geographical Information Science (27:4), pp. 662–684.

Munar, A. M., and Jacobsen, J. K. S. 2013. “Trust and Involvement in Tourism Social Media and Web-Based Travel Information Sources,” Scandinavian Journal of Hospitality and Tourism (13:1), pp. 1–19.

Munar, A. M., and Jacobsen, J. K. S. 2014. “Motivations for sharing tourism experiences through social media,” Tourism Management (43), pp. 46–54.

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Oreskovic, A. 2015. Here's another area where Twitter appears to have stalled: tweets per day. http://www.businessinsider.com/twitter-tweets-per-day-appears-to-have-stalled-2015-6. Accessed 5 January 2016.

Park, J. H., Lee, C., Yoo, C., and Nam, Y. 2016. “An analysis of the utilization of Facebook by local Korean governments for tourism development and the network of smart tourism ecosystem,” International Journal of Information Management (advance online publication).

Raun, J., Ahas, R., and Tiru, M. 2016. “Measuring tourism destinations using mobile tracking data,” Tourism Management (57), pp. 202–212.

Risius, M., and Beck, R. 2015. “Effectiveness of corporate social media activities in increasing relational outcomes: Novel applications of social media analytics,” Information & Management (52:7), pp. 824–839.

Sigala, M., Christou, E., and Gretzel, U. 2012. Social media in travel, tourism and hospitality: Theory, practice and cases, Farnham, Surrey, Burlington, VT: Ashgate Pub.

Silverman, B. W. 1986. Density Estimation for Statistics and Data Analysis, London, New York: Chapman & Hall.

Steiger, E., Albuquerque, J. P., and Zipf, A. 2015. “An Advanced Systematic Literature Review on Spatiotemporal Analyses of Twitter Data,” Transactions in GIS (19:6), pp. 809–834.

Stieglitz, S., Dang-Xuan, L., Bruns, A., and Neuberger, C. 2014. “Social Media Analytics: An Interdisciplinary Approach and Its Implications for Information Systems,” Business & Information Systems Engineering (6:2), pp. 89–96.

Tilly, R., Fischbach, K., and Schoder, D. 2015. “Mineable or messy? Assessing the quality of macro-level tourism information derived from social media,” Electronic Markets (25:3), pp. 227–241.

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Wagner, S., Willing, C., Brandt, T., and Neumann, D. 2015. “Data Analytics for Location-Based Services: Enabling User-Based Relocation of Carsharing Vehicles,” in ICIS 2015 Proceedings, Paper 24.

Weidemann, C., and Swift, J. 2013. “Social Media Location Intelligence: The Next Privacy Battle - An ArcGIS add-in and Analysis of Geospatial Data Collected from Twitter.com,” International Journal of Geoinformatics (9:2), pp. 21–27.

Weller, K., Bruns, A., Burgess, J., Mahrt, M., and Puschmann, C. 2014. Twitter and Society, New York: Peter Lang.

Wood, S. A., Guerry, A. D., Silver, J. M., and Lacayo, M. 2013. “Using social media to quantify nature-based tourism and recreation,” Scientific Reports (3), Article 2976.

World Travel & Tourism Council 2015. “Travel & Tourism: Economic Impact 2015 World,” London.

Xie, Z., and Yan, J. 2008. “Kernel Density Estimation of traffic accidents in a network space,” Computers, Environment and Urban Systems (32:5), pp. 396–406.

Yacouel, N., and Fleischer, A. 2012. “The Role of Cybermediaries in Reputation Building and Price Premiums in the Online Hotel Market,” Journal of Travel Research (51:2), pp. 219–226.

Zervas, G., Proserpio, D., and Byers, J. 2015. “The Rise of the Sharing Economy: Estimating the Impact of Airbnb on the Hotel Industry,” SSRN Working Paper .

#

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

## Biographies

Tobias Brandt is an Assistant Professor of Business Information Management in Rotterdam School of Management, Erasmus University. He has received his PhD from the University of Freiburg, Germany, in 2015. His research focuses on the digital transformation of society and economy, with a particular focus on smart cities and urban data analytics. His works have received the Best Paper Awards at the ICIS and the HICSS, and his papers have been published or are forthcoming in the Journal of Management Information Systems, the European Journal of Information Systems, the European Journal of Operational Research, and Omega.

Johannes Bendler is the CTO of Geospin, a start-up company specialized on urban data science. He received his MSc in Computer Science and PhD from the University of Freiburg in 2012 and 2015, respectively. He develops novel data analytics methods for spatial data and is involved in consultation projects from several industries.

Dirk Neumann is a Professor of Information Systems at the University of Freiburg, Germany. He holds degrees in economics from the University of Giessen, Germany and the University of Wisconsin–Milwaukee. He has received his PhD in Economic and Business Sciences from the Karlsruhe Institute of Technology, Germany. His research centers on digitization and novel uses of information systems in industries and the society. His articles have been published in the Journal of Management Information Systems, the ACM Transactions in Internet Technology, the Communications of the ACM, Decision Support Systems, and others.

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

![](/api/attachments/XS6RU38Z/fulltext/images/4eef3073ef9a8ba5b1f3fe9d842d2b722c1ad251941cadeab746d402044f0dd3.jpg)  
Figure 1. SMA-enabled STE

![](/api/attachments/XS6RU38Z/fulltext/images/2409d2825e918a3d3350d5696d14cf53a8e1351f6060c29f11eaec1a59e340ed.jpg)  
Figure 2. Boxplot representation of twitter activity throughout the day (error bars indicate 0.05 and 0.95 quantiles)

![](/api/attachments/XS6RU38Z/fulltext/images/2e23b8fb71adcd41de9e0592608a1d7c97b942e9cfaa96fc54aca2bc01305401.jpg)

![](/api/attachments/XS6RU38Z/fulltext/images/a2b25f3b333683e944587b369ee1c293a2f10e4655a91c48c27b2f8bfecf4984.jpg)  
Figure 3. Twitter patterns showing the average number of shares of tweets per hour within a day

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

![](/api/attachments/XS6RU38Z/fulltext/images/b296ba5110399662a681f65c30df56dd890641a9f716f895c5f04621ade73df0.jpg)  
Figure 4. KDE using a Gaussian kernel with a standard deviation of 250 m

![](/api/attachments/XS6RU38Z/fulltext/images/1d575abf354ce4e744de9fc82349263da0b15509f4682d5c762d5cb9106745fb.jpg)  
Figure 5. Density of tweets in San Francisco during the observation period

![](/api/attachments/XS6RU38Z/fulltext/images/53f2e81bf0b8d749ff8a8ba2daa65fcfa466c4cb1cbf230b5431dd1f66b7526e.jpg)  
Figure 6. Density of tweets with attachments in San Francisco during the observation period

![](/api/attachments/XS6RU38Z/fulltext/images/bef1080e87dd874d713095511da533260509b85a7d7965b3d0eaa2f95ed48470.jpg)  
Figure 7. Conditional probability of photo or video attachment

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

![](/api/attachments/XS6RU38Z/fulltext/images/2db695ea4f729f2217903071eeaa965cfef1c1119d7f54045c7ba7e7fcb11fa2.jpg)  
Figure 8. Spatial distribution of topics (colors represent the different probabilities of a topic being assigned to a tile)

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

Table 1. Potential value sources in SMA-enabled STE

<table><tr><td rowspan="3">Presence</td><td>· Assess spatiotemporal fluctuations to optimize mobility across the city (GOV)</td></tr><tr><td>· Identify target audiences for tailored advertisements for tourist events and attractions (TS)</td></tr><tr><td>· Identify popular times and places for tour and destination scheduling (TS, DMO)</td></tr><tr><td rowspan="2">Environmental engagement</td><td>· Identify good vantage points for photography (GOV, TS)</td></tr><tr><td>· Discover new attractions and scenic areas (GOV, TS, DMO)</td></tr><tr><td rowspan="2">Topical engagement</td><td>· Assess effect of certain events on urban dynamics (GOV)</td></tr><tr><td>· Estimate impact and anticipation for specific events (TS, DMO)</td></tr></table>

GOV = Government; TS = Tourism supplier; DMO = Destination marketing organization

## Appendix: Summary of LDA Topics

Table 2. Topics identified by LDA with first 10 terms in each topic (characteristic locations and events are given in bold)

<table><tr><td>Topic 1</td><td>Topic 2</td><td>Topic 3</td><td>Topic 4</td><td>Topic 5</td><td>Topic 6</td></tr><tr><td>san</td><td>just</td><td>san</td><td>beach</td><td>like</td><td>san</td></tr><tr><td>francisco</td><td>like</td><td>francisco</td><td>just</td><td>lol</td><td>francisco</td></tr><tr><td>others</td><td>amp</td><td>candlestick</td><td>francisco</td><td>just</td><td>just</td></tr><tr><td>just</td><td>francisco</td><td>pier</td><td>like</td><td>dont</td><td>mph</td></tr><tr><td>vmworld</td><td>san</td><td>others</td><td>san</td><td>get</td><td>twitter</td></tr><tr><td>like</td><td>good</td><td>wharf</td><td>ocean</td><td>love</td><td>others</td></tr><tr><td>get</td><td>one</td><td>fishermans</td><td>love</td><td>amp</td><td>hall</td></tr><tr><td>amp</td><td>house</td><td>amp</td><td>amp</td><td>got</td><td>like</td></tr><tr><td>good</td><td>love</td><td>just</td><td>good</td><td>know</td><td>civic</td></tr><tr><td>new</td><td>get</td><td>sanfrancisco</td><td>can</td><td>good</td><td>city</td></tr><tr><td>Topic 7</td><td>Topic 8</td><td>Topic 9</td><td>Topic 10</td><td>Topic 11</td><td>Topic 12</td></tr><tr><td>san</td><td>park</td><td>san</td><td>san</td><td>san</td><td>lands</td></tr><tr><td>[Cyrillic]</td><td>atampt</td><td>francisco</td><td>francisco</td><td>francisco</td><td>outside</td></tr><tr><td>cbs</td><td>sfgiants</td><td>others</td><td>just</td><td>others</td><td>outsidelands</td></tr><tr><td>francisco</td><td>san</td><td>just</td><td>like</td><td>square</td><td>stage</td></tr><tr><td>new</td><td>francisco</td><td>amp</td><td>amp</td><td>pic</td><td>music</td></tr><tr><td>just</td><td>giants</td><td>like</td><td>get</td><td>amp</td><td>golden</td></tr><tr><td>bay</td><td>others</td><td>new</td><td>time</td><td>cafe</td><td>gate</td></tr><tr><td>day</td><td>just</td><td>one</td><td>good</td><td>restaurant</td><td>san</td></tr><tr><td>hotel</td><td>game</td><td>get</td><td>love</td><td>starbucks</td><td>park</td></tr><tr><td>like</td><td>like</td><td>now</td><td>now</td><td>hotel</td><td>francisco</td></tr><tr><td>Topic 13</td><td>Topic 14</td><td>Topic 15</td><td>Topic 16</td><td>Topic 17</td><td>Topic 18</td></tr><tr><td>san</td><td>just</td><td>san</td><td>san</td><td>san</td><td>san</td></tr><tr><td>francisco</td><td>like</td><td>francisco</td><td>francisco</td><td>francisco</td><td>francisco</td></tr><tr><td>others</td><td>class</td><td>park</td><td>just</td><td>lombard</td><td>just</td></tr><tr><td>amp</td><td>san</td><td>castro</td><td>union</td><td>just</td><td>chinatown</td></tr><tr><td>just</td><td>francisco</td><td>dolores</td><td>square</td><td>cspanwj</td><td>photo</td></tr></table>

##

Social Media Analytics and Value Creation in Urban Smart Tourism Ecosystems

<table><tr><td>like</td><td>get</td><td>mission</td><td>day</td><td>amp</td><td>others</td></tr><tr><td>bar</td><td>dont</td><td>just</td><td>others</td><td>ghirardelli</td><td>amp</td></tr><tr><td>one</td><td>day</td><td>others</td><td>get</td><td>street</td><td>posted</td></tr><tr><td>love</td><td>love</td><td>like</td><td>twin</td><td>square</td><td>sanfrancisco</td></tr><tr><td>time</td><td>lol</td><td>sanfrancisco</td><td>peaks</td><td>others</td><td>tower</td></tr><tr><td>Topic 19</td><td>Topic 20</td><td>Topic 21</td><td>Topic 22</td><td>Topic 23</td><td>Topic 24</td></tr><tr><td>san</td><td>san</td><td>golden</td><td>san</td><td>san</td><td>just</td></tr><tr><td>francisco</td><td>francisco</td><td>gate</td><td>francisco</td><td>francisco</td><td>san</td></tr><tr><td>ferry</td><td>cup</td><td>bridge</td><td>mason</td><td>now</td><td>like</td></tr><tr><td>others</td><td>americas</td><td>san</td><td>fort</td><td>fillmore</td><td>amp</td></tr><tr><td>building</td><td>pier</td><td>francisco</td><td>marina</td><td>jobs</td><td>[Cyrillic]</td></tr><tr><td>exploratorium</td><td>americascup</td><td>presidio</td><td>cup</td><td>hiring</td><td>get</td></tr><tr><td>just</td><td>pavilion</td><td>beach</td><td>americas</td><td>just</td><td>time</td></tr><tr><td>bay</td><td>just</td><td>via</td><td>just</td><td>amp</td><td>day</td></tr><tr><td>embarcadero</td><td>bay</td><td>shared</td><td>others</td><td>like</td><td>coffee</td></tr><tr><td>sanfrancisco</td><td>others</td><td>palace</td><td>village</td><td>electric</td><td>good</td></tr><tr><td>Topic 25</td><td>Topic 26</td><td>Topic 27</td><td>Topic 28</td><td>Topic 29</td><td>Topic 30</td></tr><tr><td>just</td><td>park</td><td>just</td><td>francisco</td><td>francisco</td><td>que</td></tr><tr><td>san</td><td>end</td><td>like</td><td>san</td><td>san</td><td>lol</td></tr><tr><td>francisco</td><td>san</td><td>get</td><td>mission</td><td>just</td><td>love</td></tr><tr><td>like</td><td>francisco</td><td>good</td><td>just</td><td>amp</td><td>just</td></tr><tr><td>good</td><td>lands</td><td>time</td><td>like</td><td>like</td><td>like</td></tr><tr><td>time</td><td>just</td><td>can</td><td>case</td><td>get</td><td>dont</td></tr><tr><td>can</td><td>sanfrancisco</td><td>now</td><td>closed</td><td>california</td><td>amp</td></tr><tr><td>get</td><td>california</td><td>one</td><td>request</td><td>good</td><td>get</td></tr><tr><td>now</td><td>day</td><td>people</td><td>street</td><td>day</td><td>now</td></tr><tr><td>amp</td><td>photo</td><td>know</td><td>get</td><td>[Cyrillic]</td><td>know</td></tr></table>
