---
otero_id: 28622
otero_key: "MTJHA5EA"
title: "Star Wars: An Empirical Study of Star Performer Turnover and Content Supply on Multisided Streaming Platforms"
authors: "Jens Forderer; Dominik Gutt; Brad N. Greenwood"
year: "2026"
journal: "Information Systems Research"
doi: "10.1287/isre.2023.0367"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Star Wars: An Empirical Study of Star Performer Turnover and Content Supply on Multisided Streaming Platforms

Jens Forderer,<sup>a,</sup>\* Dominik Gutt,<sup>b</sup> Brad N. Greenwood<sup>c</sup>

<sup>a</sup> Business School, University of Mannheim, 68161 Mannheim, Germany; <sup>b</sup> Rotterdam School of Management, Erasmus University Rotterdam, 3062 PA Rotterdam, Netherlands; <sup>c</sup> School of Business, George Mason University, Fairfax, Virginia 22030 \*Corresponding author

Contact: jens.foerderer@uni-mannheim.de, https://orcid.org/0000-0002-3090-4559 (JF); gutt@rsm.nl, https://orcid.org/0000-0002-2633-9518 (DG); bgreenwo@gmu.edu, https://orcid.org/0000-0002-0772-7814 (BNG)

Received: June 23, 2023 Revised: April 19, 2024; November 5, 2024; January 31, 2025 Accepted: February 8, 2025 Published Online in Articles in Advance: May 14, 2025

https://doi.org/10.1287/isre.2023.0367

Copyright: © 2025 The Author(s)

Abstract. Competition between user-generated content platforms (e.g., Twitch, Spotify, YouTube) is characterized by fierce talent poaching of highly popular “stars” on the supply side. However, little is known about how the loss of a star affects content production from former cocreating peers on multisided content platforms. Whereas theory suggests that star turnovers might decrease the demand for cocreating peers or trigger them to depart the platform as well, empirical understanding is still lacking. To address this gap, we examine the defection of Fortnite star Richard Tyler “Ninja” Blevins from Twitch.tv to Microsoft Mixer in 2019 using a quasi-experimental research design and novel streamerlevel data. Findings are fourfold. First, the turnover of a star decreases peer creators’ content contribution by �20.4%, suggesting that the departure of a star contracts supply for the platform overall. Second, the negative star turnover effect on content contribution is lesser for creators who have a diversified content portfolio and are relatively more popular. Third, evidence suggests that the overall negative effect operates through a downsizing rather than desertion mechanism, (i.e., remaining creators reduce their contribution rather than abandoning the platform entirely). Finally, creators experiment with shifting their focus to other types of content but eventually abandon these efforts. We conclude that star turnover can cause both primary and spillover losses in content supplied to a platform. Our findings have implications for platform management, the content strategy of creators, and our understanding of stars’ influence on multisided content platforms.

![](/api/attachments/MTJHA5EA/fulltext/images/c84daa1fbf12579d626ce0eaa9fe0822fd94d4bb613706a1fe7e6363bc4d4aaa.jpg)

History: Olivia Liu Sheng, Senior Editor; Xitong Li, Associate Editor.

a Open Access Statement: This work is licensed under a Creative Commons Attribution 4.0 International License. You are free to copy, distribute, transmit and adapt this work, but you must attribute this work as “Information Systems Research. Copyright © 2025 The Author(s). https://doi.org/10.1287/ isre.2023.0367, used under a Creative Commons Attribution License: https://creativecommons.org licenses/by/4.0/.”

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2023.0367.

Keywords: multisided platforms • star turnover • content creators • network effects • difference in differences • twitch • viewers • followers • platform management

## 1. Introduction

Competition between user-generated content platforms has yielded intense poaching battles for highly popular supply side “stars” in recent years. Spotify, for example, spent US\$200 million for exclusive rights to The Joe Rogan Experience, a podcast that had garnered more than 11 million listeners per episode (Rosman 2022), and in the live game–streaming market, platforms have been making multimillion dollar deals to lure streamers such as Ninja, xQc, and shroud (as well as their millions of followers). Yet, insofar as such stars are nonemployees of the platform, the concentration of uncontrolled human capital creates significant managerial challenges for platforms. At the same time, academic understanding offers little insight into how the turnover of a star affects contributions to a platform. Although the production and management of user-generated content has been a mainstay of information systems (IS) scholarship for decades (Tiwana et al. 2010, Parker and Van Alstyne 2018, Bhargava 2022), extant work on stars focuses on understanding the effects of winning them, not losing them (e.g., Binken and Stremersch 2009, Hogendorn and Ka Yat Yuen 2009).

To fill this gap, we depart from the theoretical grounding that supply-side contributions to a multisided platform reflect intricate interdependencies between the supply and demand sides as well as among competing platforms (Rochet and Tirole 2003, Parker and van Alstyne 2005). Instead, the departure of a star constitutes a structural disruption, which we argue causes peer creators’ to reduce their content supply to the platform through two theoretical mechanisms: desertion and downsizing. Inasmuch as a star’s departure might signal weakness in the platform, it may stimulate desertion; meaning star departure might similarly cause others to abandon the platform in favor of rivals. Further, if a star’s departure causes a contraction in demand, indirect network effects might cause creators to downsize their supply in an adjustment reaction.

To test these theoretical possibilities, we examine a quasi-experimental event in the market for live video streaming: the sudden departure of the Fortnite streaming star Richard Tyler “Ninja” Blevins from Twitch to Microsoft’s new streaming platform Mixer in 2019. Aside from providing us with an intriguing setting to investigate star departure, this event is well-suited for methodological reasons. Ninja’s departure was unexpected and occurred immediately (Robidoux 2019, Singh 2023) and offers the opportunity to isolate peer creators and unaffected creators (i.e., treatment and control groups). More specifically, using a difference-indifferences (DiD) approach, we compare outcomes between English- and German-language Fortnite streamers before and after Ninja’s departure. Both English and German channels play the same game, thereby isolating game-specific differences, although they cater to different audiences because of language and time zone differences.

Findings indicate that Ninja’s departure had a negative effect on peer content supply to Twitch, which confirms our prediction. Economically, Ninja’s turnover reduced peer content contributions by �20.4%. This result is robust to a host of econometric approaches, including a relative time estimation, heterogeneous windows around departure, various matching approaches, and changing control group definitions. Second, we find support for the conjecture that streamers that are diversified and those that are popular showed much smaller declines in production. Further, in an empirical extension, we find that the mechanism behind the negative effect is primarily downsizing rather than desertion. This is striking as it suggests stars are crucial not only for their own content production but because of their indirect influence on peers’ content production. Finally, we observe that creators explore shifting their focus to other types of content in the wake of Ninja’s departure but ultimately abandon these attempts. Taken together, this evidence suggests star turnover can cause both primary and spillover losses in content supplied to a platform.

## 2. Theoretical Background and Related Literature

User-generated content platforms rely on contributions from outside the firm, that is, by content creators, in order to create value (e.g., Hukal et al. 2020, Bhargava 2022, Burtch et al. 2022, Gu et al. 2024). Yet, whereas early models of multisided platforms largely ignore heterogeneity between supply-side actors (Rochet and Tirole 2003, Armstrong 2006), more recent scholarship has begun to unpack the differences in such agents. Indeed, scholarship indicates that these differences matter for platform outcomes; including popular versus nonpopular apps (Foerderer et al. 2021, Lee et al. 2023), amateurs versus professionals (Boudreau 2018), indie developers versus incumbents (Qiu et al. 2017), central versus peripheral creators (Li et al. 2022), or—as is the focus of our paper—stars and nonstars (Lueker et al. 2022, Carroni et al. 2024).

There is no consensus definition of what makes a content creator a star. In the context of app platforms, Ershov (2018) considers apps that achieved the top position in the bestseller rankings. Carroni et al. (2024) consider star creators as those with full bargaining power over the platform. In work on stardom outside of platform settings (e.g., science, contests, employees, sports), current definitions strongly depend on the contex (Rosen 1981) and consider measures such as citations (Azoulay et al. 2010), the receipt of prestigious awards (Ammann et al. 2016), or even rankings (Groysberg et al. 2008, Bockstedt et al. 2022). And, whereas these provide no uniform theoretical definition, the common denominator is that there is an uneven distribution of demand, and that demand for stars outstrips their peers by an order of magnitude.

In turn, subsequent research on stars in the multisided platform context has largely centered on understanding their effects for the demand side of the platform (Rochet and Tirole 2003, Binken and Stremersch 2009, Hogendorn and Ka Yat Yuen 2009). The core tenet of this scholarship is that stars have disproportionally large effects for platform adoption (e.g., Binken and Stremersch 2009), which makes them particularly important for solving the chicken-and-egg prob lem during platform launch (Rochet and Tirole 2003, Dou and Wu 2021), and that exclusivity is crucial for leveraging these demand effects (Corts and Lederman 2009, Carroni et al. 2024). Raj (2024), for example, examines how artists’ content (i.e., listeners) was affected by a peer’s release of content (i.e., an album) on the music streaming service Spotify.

In contrast, comparatively fewer studies examine the effect stars have on the supply side of a platform: the core interest of this work. Still, it is generally accepted that that peer creators can benefit from the presence of stars. Carroni et al. (2024) develop a model of superstar decision making in a competitive platform setup, focusing on a star’s decision to provide content exclusively to one platform. Still, their findings inform us about the potential effects of stars on their peers: stars are pivotal for platform-to-platform competition because they can induce the agglomeration of consumers and creators. In turn, stars can be beneficial for creators by attracting demand to the platform from both rival platforms and multihoming creators. This aligns with Ershov’s (2018) empirical findings, which suggest that the introduction of star apps in niche markets can reduce consumer uncertainty about those markets, thereby encouraging the entry of new apps. Similarly, Lee et al. (2023) find that adoption of star apps can increase the use of other apps, and Zhang et al. (2019) study the crowdsourcing platform Topcoder, finding that creators can benefit from star coders by learning from them and improving their skills over time. However, there is also evidence that stars can exert deterring effects on peers’ contributions. Bockstedt et al. (2022), for example, find that visible stars in crowdsourcing contests for innovation can deter contributions from nonstars by foreclosing the market. Lueker et al. (2022) similarly observe that the appearance of bestselling games can dampen innovation in similar games through foreclosure. Our study is related to this stream of research but addresses a different question, namely, how the departure of a star affects peers’ contributions to the platform.

## 3. Hypothesis Development

Supply-side contributions to a multisided platform reflect the intricate interdependencies between the supply and demand sides of platforms as well as among competing platforms (Rochet and Tirole 2003, Parker and van Alstyne 2005). In what follows, we argue that the departure of a star constitutes a structural disruption, which, in turn, causes peer creators to reduce their content supply to the platform. This adjustment can be explained through two distinct theoretical mechanisms: desertion and downsizing. 2

Regarding desertion, to the extent that participants in multisided platforms face uncertainty about the future viability of a platform (Caillaud and Jullien 2003, Hukal et al. 2020), contributions will plausibly decline if the departure of the star signals uncertainty about the longterm health of the platform. Uncertainty over the longterm viability of a platform is an important factor for participants in multisided markets (Caillaud and Jullien 2003, Parker and van Alstyne 2005). As the turnover of a star to a rival platform, a highly visible event, might be construed as a weakness in the platform overall, creators may decide to investigate outside options, reallocate their efforts, and deplatform entirely. Corroborating this line of reasoning is evidence that nonstars learn from stars, imitating their behavior, and often follow them to new platforms (Zhang et al. 2019) and adopt new technologies (Lacetera et al. 2004).

Regarding downsizing, to the degree that established interactions between competing content creators can be viewed as complementary (Venkatraman and Lee 2004,

Boudreau 2012, Boudreau and Jeppesen 2015), it is plausible that the demand spillovers created by the star might concomitantly reduce demand for the star’s competitors when the star departs (Katz and Shapiro 1994, Haviv et al. 2020, Raj 2024). Inasmuch as stars can generate intense amounts of demand, which they can only partially internalize, some of the spillover demand is captured by peers. Such demand spillovers are observed widely in research on platforms (Binken and Stremersch 2009, Landsman and Stremersch 2011, Ershov 2018, Liang et al. 2019, Lee et al. 2023, Raj 2024). For example, Ershov (2018) shows that the entrance of star apps into Google’s Play Store leads others to enter that market and capture the glut of consumer demand the star app generated. In music streaming, Raj (2024) similarly finds that an album released by a star generates more demand not only for that star but also for competing artists. Consequently, if a star departs, the star may leave competitors worse off by eroding spillover demand for content. In light of the known correlation between viewership and content supply (Zhao et al. 2021), we, therefore, posit that creators will reduce their content supply to adjust for the reduced demand.<sup>3</sup>

Hypothesis 1. Star departure (turnover) has a negative effect on peers’ content supply.

We further argue that the effect of Hypothesis 1 differs depending on the extent to which a creator benefited from demand spillovers that a star generates. One such condition is a creator’s diversification in terms of the extent to which the creator produces content across multiple, distinct niches (e.g., genres, content formats). This is in contrast to the creator concentrating output within a single content segment. Arguably, there is a mechanical relationship that ties the magnitude of the demand contraction directly to the extent of the spillover effects. Creators whose content is closer to a star’s content benefit more from the spillover effects caused by the star. More specifically, the stronger spil lovers grow out of the attention created by the star for same-segment content and are intensified by any recommendation algorithms that suggest to viewers similar content (Liang et al. 2019, Wang et al. 2023, Raj 2024). For example, Raj (2024) finds that demand spillover effects from album releases on Spotify are larger the greater the content proximity between the creators. In our case, the departure of the star leaves these proximal creators exposed to audience loss, whereas creators with diversified content remain more insulated from the full effects of the star’s departure because their demand is not tied solely to the star’s presence. This logic parallels the dynamics of a firm encountering a demand shock in one segment (e.g., Ahuja and Novelli 2017, Tan et al. 2017). If the firm operates across multiple segments, the diversification mitigates the impact as the shock affects only a portion of demand. Conversely, if the firm is concentrated in a single segment, the consequences are more severe as the firm has no alternative demand to offset the loss. Based on these arguments, we posit that a creator’s content diversity attenuates the negative demand effect caused by the departure of a star.

Hypothesis 2. The negative direct effect of a star departure (turnover) on content supply is less pronounced for diversified creators.

A final factor that we expect to attenuate the negative effect of Hypothesis 1 is creator popularity. Insofar as popular creators possess their own, independent, stream of demand, it is likely that they are less affected by the departure of the star. In the same way that viewers are loyal to a star and may follow the star to a riva platform, a popular creator also likely has loyal viewers who continue to consume the creator’s content despite broader changes in the platform environment. Prior research documents that, on live-streaming platforms, viewers can be intensely loyal because of the importance of social interaction with other viewers (Sjo¨blom and Hamari 2017), sense of community (Hilvert-Bruce et al. 2018), and social support (Zhao et al. 2021), all of which should act as frictions that prevent popular streamers from losses in demand after star departures. Whereas this logic does not nullify the possibility that popular creators also benefit from the existence of the star, it does suggest that they are less reliant on such spillovers than the marginal creator. Moreover, popular creators possess a stronger market dominance that shields them from demand shocks, and this is commonly subsumed as cumulative advantages or a Matthew effect (e.g., Merton 1968). Thus, regardless of a star’s departure, popular streamers should possess resources that allow them to react to demand shocks (e.g., by venturing into different niches in which consumer demand is still present). They should also continue to be recommended by platform algorithms and appear high in search results because they tend to be derived from creators’ existing popularity (Susarla et al. 2012; Zhao et al. 2021, 2023). Thus, even if the popular creator loses some level of demand in the wake of the star’s departure, we posit that their sampling rate will still outstrip the margina creator.

Hypothesis 3. The negative direct effect of a star departure (turnover) on content supply is less pronounced for popular creators.

## 4. Method and Data

## 4.1. Empirical Setting: Tyler “Ninja” Blevins Turnover from Twitch

We investigate star turnover in the context of the live game–video streaming platform Twitch. In doing so, we center our analysis on the defection of the Fortnite streamer star Tyler “Ninja” Blevins.

Twitch is a live-streaming platform that focuses on the streaming of video games and eSports competitions. Creators (hereafter referred to as channels or streamers) broadcast audio and video to viewers in real time as they play a game (Elberse and Leszczynski 2020, Bru¨ ndl et al. 2023). During a live cast, as shown in Figure 1, a channel is usually focused on a specific type of content, usually a game that is played by the streamer, and displayed on the screen along with a live discussion from viewers. Viewers can also see the gamer through a webcam along with various other data. Streamers can also connect to viewers via the platform to build a customer base based on followership and live interactions. Thei content choice is usually linked to their skill in playing a game as viewers may be disappointed if the streamer consistently loses.

On August 1, 2019, Ninja announced he had signed a deal to stream exclusively on the Mixer platform, effective the next day (Needleman 2019). At that time, he was the most popular Fortnite streamer on Twitch with 14.5 million followers. Previously, the market for livestreaming platforms had witnessed explosive growth. Twitch had the largest market share by hours watched (75.6%), followed by YouTube Gaming (17.6%), and Facebook Gaming (3.7%). Mixer, operated by Microsoft, was the de novo platform rival to Twitch. Online Appendix B provides further background on the choice of this context and the market for live-streaming platforms.

## 4.2. Research Design: Matched Difference-in-Differences

To identify the effect of star departure, we leverage a matched difference-in-differences analysis as illustrated in Figure 2. Ninja’s turnover is well-suited to this method. First, Ninja’s departure was unexpected and swiftly implemented, which reduces concerns over anticipation. The move was considered surprising by various media outlets. The Verge described the announcement as “a tweet that blew up gaming” (Stephen 2019). Others described the departure as “shocking” (Robidoux 2019), and eSports journalists rank the departure as the most unexpected signing of all time (Singh 2023). Further, because the switch was effective the next day, the event provides a clear cutoff date for the pre and post periods. Second, it is unlikely that the move was correlated with the behavior of other channels (e.g., because of competi tive pressure). Although the definitive reasons were not disclosed, Ninja’s manager stated that the primary motive was that Twitch had hindered licensing and brand deals outside the platform (Smith 2019).

For group assignment, we exploit language differences, which are a key determinant of competition between streamers. English-language streamers of

Figure 1. (Color online) Example of a Twitch Live Stream of Ninja  
![](/api/attachments/MTJHA5EA/fulltext/images/d30e3c59455907f7597513d7e36bca66dc6f98f338e12f164352637b4aa3230f.jpg)  
Notes. The figure is a screenshot taken during a live cast on Twitch. The majority of the screen (A) displays the game currently being played (Fortnite); the streamer is displayed in a smaller section to the left of the screen (B); and various further stream characteristics are shown at the bottom, including the number of concurrent viewers (C).

Fortnite are affected by Ninja’s departure, whereas German-language streamers of Fortnite should not be affected because German channels compete for a different audience: German-speaking viewers. For streamers to create high-quality content, they need to proficiently speak the language of their audience. Our logic is, thus, that English content is unlikely to appeal to most German viewers, and German channels are unlikely to have a substantial non-German audience because of language barriers. This language barrier is particularly acute because Ninja’s primary audience is composed of teenagers (Marchese 2021), and Fortnite’s comic style appeals to that audience. Viewers of this age in Germanspeaking countries are unlikely to consume Englishlanguage streams because, despite learning English as a second language, they are likely unable to enjoy an English-only stream.<sup>4</sup> In addition, competition in livegame streaming is a matter of concurrency: Ninja streamed almost every day for about 12 hours per day, which made it almost impossible for English-language streamers to cast during the few hours he was absent. At the same time, German teenagers would find it challenging to watch Ninja’s streams because of time zone differences as his streams took place in the evening and at night in local German time.

## 4.3. Data and Variables

We create a unique data set on English- and Germanlanguage Fortnite channels by merging data from various Twitch stream aggregators as described in Online

Figure 2. Research Design  
![](/api/attachments/MTJHA5EA/fulltext/images/f2351a04a949b40044eb0a9142102fdae98507ad889d4a7632da70dce11d8c4b.jpg)  
Notes. The figure displays the quasi-experimental research design. English-language channels serve as the treatment group with German chan nels as the control group, and they are matched via coarsened exact matching. To infer the effects of the switch, we estimate the difference-indifferences between treated and control channels before and after the switch

Appendix B. The channels included in our data set (1) streamed Fortnite for at least one hour in the first week of 2019, (2) streamed exclusively in English (German), and (3) had a minimum average of five viewers. We observe each channel’s broadcasts (e.g., viewership, followers, games played) daily, making the resulting data set a channel–day level panel.

Our primary dependent variable measures the amount of content a channel produces for the platform (MINS STREAMED). This is channel i’s total number of minutes of video stream contributed to the platform on day t. We log-transform the variable to account for its skewed distribution.

Our empirical framework relies on two main indicators. TREAT is one for treated channels, else zero. AFTER is coded as one if day t is after Ninja’s departure, else zero.

To capture the diversification of a streamer (Hypothesis 2), we assess the channel’s content mix. The dummy DIVERSIFIED is one if 25% or more of streamers’ broadcast time is devoted to non-Fortnite content and zero otherwise. Note that, although our sample includes only Fortnite channels, there is considerable heterogeneity in channels’ content mix. We defined the cutoff at the median of the empirical distribution of the total minutes streaming Fortnite divided by the total minutes streamed (i.e., the share of Fortnite streamed of the overall amount streamed), which equals 25%. Results are consistent using a continuous indicator. We operationalize POPULARITY as the sum of followers, following Zhao et al. (2021), and subsequently divide this variable along the terciles of the distribution (Hypothesis 3). To ensure that our moderators are not affected by the treatment, we compute them based on pretreatment data.

FOLLOWERS records the average number of followers of channel i on day t. VIEWERS captures the average number of viewers of channel i on day t. To capture how long a channel has been active on Twitch, we create the variable AGE, which is the count of the days between when channel i joined Twitch and day t. SHARE VIEWERS LOST is the share of predeparture viewers a channel lost in the 10 days following Ninja’s departure. MIXER is one if channel i was available on Mixer. MIXER is time invariant, reflecting a permanent move rather than a fluctuating state. DISCONTINUED is one if channel i did not contribute a single stream to Twitch for the 60 days following Ninja’s switch and zero otherwise. DISCONTINUED is time invariant because a channel can only be discontinued once.

STREAMED is one if a streamer cast a stream on day t. STREAMED FORTNITE is one if streamer i cast Fortnite on day t and otherwise zero. SHARE\_NON-FORTNITE\_CONTENT is the number of minutes a streamer casts content other than Fortnite on day t (i.e., playing a different game or focusing on direct viewer interaction in terms of the “just chatting” format)

divided by the total number of minutes streamed on day t. This variable captures how streamers alter their content mix in reaction to Ninja’s departure (i.e. diversification). Summary statistics are in Table 1.

## 4.4. Matching and Test for Model Assumptions

To mitigate concerns over preswitch heterogeneity between groups as well as to address the fact that there are more English-language channels than German channels, we employ a coarsened exact match (CEM) (Iacus et al. 2012, King and Nielsen 2019). We use preturnover data to match channels on MINS STREAMED (to obtain channels that are comparable in their supply to the platform), on FOLLOWERS and VIEWERS (to obtain channels of comparable demand), and on AGE (to account for differences in channels’ experience or more general effects associated with the time on the platform) (Susarla et al. 2012, Goes et al. 2016). We rely on the Sturges rule default coarsening algorithm and enforce k2k matching.

To assess the effectiveness of the matching, we compare treated and control streamers in Table 2. Column (1) reports a t-test for means to understand predeparture differences across treated and control streamers and shows no significant differences in the dependent variable before matching. Groups differed in viewers and followers; after matching, these differences are insignifi cant. Moreover, the groups became balanced in size. Online Figure A1 shows the corresponding variable distributions, which are similar even before matching. This mitigates concerns of common support violations to a large extent. Column (2) tests for parallel trends by regressing the dependent variable on the treatment indicator, a linear time trend, and their interaction, using only preswitch data. The differences are close to zero and insignificant, supporting the parallel trends assumption.<sup>5</sup> Note that Figure 3 provides a complementary view on the data by estimating differences conditional on individual predeparture and postdeparture days.

## 4.5. Estimation Model

We rely on a standard multiway fixed effect DiD model estimated with ordinary least squares (OLS) (Angrist and Pischke 2009):

$$
\begin{array}{r l} \text { MINS   STREAMED } _ {i, t} & = \beta_ {0} + \beta_ {1} \text { TREAT } _ {i} + \beta_ {2} \text { AFTER } _ {t} \\ & + \beta_ {3} \text { TREAT } _ {i} \times \text { AFTER } _ {t} + \tau_ {t} + \omega_ {i} \\ & + \epsilon_ {i, t}, \end{array} \tag {1}
$$

where $\beta _ { 3 }$ captures the difference in minutes streamed by peer channels before and after Ninja’s departure as compared with the control group of unaffected channels. To control for time-invariant, channel-specific heterogeneity, we include channel fixed effects, which are denoted by $\omega _ { i } .$ . The vector $\tau _ { t }$ contains dummies for day of the week and month of the year. Note that $\beta _ { 2 } \ ( A \dot { F } T E R )$ is collinear with the time fixed effects, $\beta _ { 1 }$ (TREAT) is collinear with the unit fixed effects, and $\beta _ { 0 }$ (i.e., the constant term) is collinear with the unit fixed effects. Robust standard errors are clustered by channel–weekday (and heteroskedasticity robust) based on the understanding that viewer behaviors and streamer activities can vary significantly across different days of the week (Abadie et al. 2023). For example, Saturday and Sunday viewership differs from weekdays because of differences in audience availability and content consumption habits, supporting a clustering by weekday. Hypotheses tests are consistent with standard clustering at the panel unit. Our primary analysis focuses on a window of 60 days before to 60 days after the switch, balancing precise effect capture with avoiding interference from other postevent factors. We omit the day of the announcement.

Table 1. Summary Statistics

<table><tr><td></td><td>Name</td><td>Description</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Median</td><td>Maximum</td></tr><tr><td>1</td><td rowspan="2">Mins streamed Viewers</td><td>Minutes that channel i streamed on day t</td><td>264.78</td><td>175.56</td><td>5.00</td><td>228.00</td><td>1,440.00</td></tr><tr><td>2</td><td>Average number of viewers of channel i on day t</td><td>55.83</td><td>307.15</td><td>4.00</td><td>19.00</td><td>18,873.00</td></tr><tr><td>3</td><td>Followers</td><td>Average number of followers gained by channel i on day t</td><td>17.21</td><td>124.10</td><td>-1,771.00</td><td>2.00</td><td>6,137.00</td></tr><tr><td>4</td><td>Partnered</td><td>One if channel i has partner status, else zero</td><td>0.13</td><td>0.34</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>5</td><td>Mature</td><td>One if channel i is labeled as mature content, else zero</td><td>0.51</td><td>0.50</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td>6</td><td>Age</td><td>Days between channel i joining Twitch and day t</td><td>1,184.97</td><td>667.73</td><td>154.00</td><td>1,067.00</td><td>3,287.00</td></tr><tr><td>7</td><td>Diversified</td><td>One if a channel i devotes 25% or more of the time streamed to non-Fortnite content, else zero</td><td>0.48</td><td>0.50</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>8</td><td>Mixer</td><td>One if channel i was available on Mixer, else zero</td><td>0.01</td><td>0.10</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>9</td><td>Discontinued</td><td>One if channel i did not contribute a single stream to Twitch for the 60 days following Ninja&#x27;s switch, else zero</td><td>0.07</td><td>0.26</td><td>0.00</td><td>0.00</td><td>1.00</td></tr><tr><td>10</td><td>Streamed Fortnite</td><td>One if channel i casted Fortnite on day t and otherwise zero</td><td>0.59</td><td>0.49</td><td>0.00</td><td>1.00</td><td>1.00</td></tr><tr><td>11</td><td>Share Non-Fortnite Content</td><td>Minutes of streamed content other than Fortnite divided by the total number of minutes streamed by channel i on day t</td><td>0.41</td><td>0.49</td><td>0.00</td><td>0.00</td><td>1.00</td></tr></table>

## 5. Results

## 5.1. Hypotheses Tests

Results are in Table 3. Column (1) reports the test for Hypothesis 1, which is confirmed. In column (1), the coefficient of the DiD term is negative and significant, which indicates that Ninja’s departure reduced peer creators’ content broadcast. We estimate an average decline of 100(e $^ { - 0 . 2 2 8 } - 1 ) = - 2 0 . 4 \%$ (or �13.7 minutes). This is a sizable loss of content and overall amounts to a considerable lost opportunity for Twitch to monetize channels via advertising. Multiplying the average number of streamed days during the 60-day window in the treatment group before the switch (15.2) with the minute decline per streamed day (13.7) and the number of Fortnite streamers in the treatment group (260) results in a total content loss of 54,142.4 minutes (902.37 hours).

Table 2. Matching Effectiveness and Test for Parallel Trends

<table><tr><td rowspan="2">Variable</td><td colspan="2">(1) Balance: difference in means</td><td colspan="2">(2) Parallel trends</td></tr><tr><td>Before matching</td><td>After matching</td><td>Before matching</td><td>After matching</td></tr><tr><td>Log(Mins streamed)</td><td>-0.004 (0.027)</td><td>-0.006 (0.032)</td><td>-0.000 (0.001)</td><td>0.002 (0.002)</td></tr><tr><td>Log(Viewers)</td><td>0.287*** (0.061)</td><td>-0.027 (0.077)</td><td>0.001 (0.001)</td><td>-0.002 (0.001)</td></tr><tr><td>Log(Followers)</td><td>0.579*** (0.094)</td><td>0.014 (0.119)</td><td>-0.000 (0.001)</td><td>-0.001 (0.001)</td></tr><tr><td>Log(Age)</td><td>0.012 (0.039)</td><td>0.000 (0.056)</td><td>0.000 (0.000)</td><td>0.000 (0.000)</td></tr></table>

Notes. Based on N � 4,235 channels before matching and N � 520 channels after matching. Reported figures are based on pretreatment data. Difference in trends gives the coefficient when regressing the comparison variable on the interaction between the treatment indicator and a linear time trend. Standard errors in parentheses. Coefficient smaller than 0.001 are indicated as 0.000.  
\*, \*\*, \*\*\* indicate significance at the 5%, 1%, and 0.1% levels, respectively.

Figure 3. Relative Time Estimates for Hypothesis 1  
![](/api/attachments/MTJHA5EA/fulltext/images/69d0e459293575af369ac3b9fe590bbda2ae026605d3459c3ca74e435ecd58a4.jpg)  
Days Relative to Ninja's Switch to Mixer  
Notes. Dependent variable is Log(MINS STREAMED). The figure plots the day-by-day coefficients together with 95% confidence intervals. Th dashed horizontal line denotes a zero coefficient, the dashed vertical denotes the time of Ninja’s switch.

Expanding this calculation to a full year (i.e., 360 days), this loss amounts to 324,854.4 minutes (5,414.2 hours), which cannot be monetized.

Figure 3 shows the day-by-day coefficients. Results indicate that the predeparture coefficients hop above and below zero and turn negative and statistically significant only after Ninja’s turnover. We observe a marked decrease in the point estimates after Ninja’s departure, noting that some of the individual confidence intervals overlap with zero.<sup>6</sup> This supports that effects are due to the departure of Ninja and not because of a confounding event that took place during the preperiod or postperiod; that is, we see no evidence of pre treatment trends.

The remainder of Table 3 proceeds with the tests for Hypotheses 2 and 3, which are also confirmed. Column (2) indicates support for the notion that contentdiversified streamers reduce their provision of content less than undiversified streamers, thereby supporting Hypothesis 2. Estimates indicate that the decline for diversified streamers is $1 0 0 ( \mathrm { e } ^ { - 0 . 3 3 0 + 0 . 2 5 7 } - 1 ) = - 7 . 0 \% ,$ whereas for undiversified streamers it is $1 0 0 ( \mathrm { e } ^ { - 0 . 3 3 0 } - 1 )$

Table 3. Results of the Hypotheses Tests

<table><tr><td rowspan="2"></td><td colspan="3">DV = Log(Mins streamed)</td></tr><tr><td>(1) Hypothesis 1</td><td>(2) Hypothesis 2</td><td>(3) Hypothesis 3</td></tr><tr><td>Treat × After</td><td>-0.228***(0.037)</td><td>-0.330***(0.043)</td><td>-0.063+(0.034)</td></tr><tr><td>Diversification</td><td></td><td></td><td></td></tr><tr><td>Treat × After × Diversified</td><td></td><td>0.257**(0.078)</td><td></td></tr><tr><td>Popularity</td><td></td><td></td><td></td></tr><tr><td>Treat × After × 2nd Tercile</td><td></td><td></td><td>-0.503***(0.074)</td></tr><tr><td>Treat × After × 3rd Tercile</td><td></td><td></td><td>0.000(0.088)</td></tr><tr><td>Channel fixed effects</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Time fixed effects</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Time trend</td><td>x</td><td>x</td><td>x</td></tr><tr><td>Observations</td><td>62,920</td><td>62,920</td><td>62,920</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.358</td><td>0.359</td><td>0.359</td></tr></table>

Notes. OLS estimates. N are channel–day observations. Adjusted R<sup>2</sup> includes variation explained by the channel fixed effects. In column (3), the term TREAT × AFTER captures the effect on the first tercile. Standard errors in parentheses.  
<sup>+</sup>, \*, \*\*, \*\*\* indicate significance at the 10%, 5%, 1%, and 0.1% levels, respectively.

� �28.1%. Online Table A1 includes controls for non-Fortnite content and indicates that the moderating effect of diversification is not driven by an increase in non-Fortnite supply and demand. Results are also consistent using a continuous measure of DIVERSIFIED as shown in Online Table A2. Column (3) is the test for Hypothesis 3. In it, we see that Ninja’s departure had no negative effects on popular streamers. Instead, the low and middle terciles of popularity are driving the effect, indicating a decline of 100(e<sup>�0.063</sup> � 1) � �6.1% and 100(e<sup>�0.503</sup> � 1) � �39.5%, respectively, and supporting Hypothesis 3. Taken together, diversified and popular streamers are less affected by star turnover because they are less prone to the negative demand externalities that stem from the star’s defection.

## 5.2. Robustness Checks

Whereas our initial results are compelling, we subject our estimations to a host of falsification tests to ensure their robustness. A summary of these tests can be found in Table 4.

In a first set of checks, reported in Online Figure A2, we assessed the sensitivity of the result. To safeguard against channels being on different trajectories, we implement the alternative regression formulation for the DiD proposed by Angrist and Pischke (2009, equation (5.2.7)), which includes unit-specific time trends. Results are consistent with Hypothesis 1. Second, averages can be prone to outliers. Still, results are consistent when winsorizing the dependent variable at the 5th and 95th percentiles. Third, the effect could be driven by popular channels. Refuting this concern is that, when we drop large channels—defined as those in the 95th percentile in terms of predeparture followers—Hypothesis 1 remains confirmed. Fourth, results are consistent when using a longer time window of (�120,120) and (�180,180) days. This safeguards the results against being an artifact of the time window.<sup>7</sup> Fifth, the public record indicates that streamer star Turner “Tfue” Tenney paused streaming from September 13 to September 30, 2019. Results are consistent when restricting to (�30,30) days, so the sample does not include Tfue’s break. Last, given that the live-streaming landscape is highly dynamic and to safeguard against inactive channels influencing the results, we report the results when requiring that channels need to have streamed Fortnite at least once in the month before Ninja’s turnover. Again, Hypothesis 1 is confirmed.<sup>8</sup>

Table 4. Summary of Robustness Tests for Alternative Explanations

<table><tr><td></td><td>Alternative explanation</td><td>Test</td><td>Outcome</td></tr><tr><td>1</td><td>Streamers are on different content supply trajectories.</td><td>Include streamer-specific linear time trends to the analysis (Online Figure A2, row (1)).</td><td>✓</td></tr><tr><td>2</td><td>Decrease in content supply is driven by outliers in the dependent variable.</td><td>Winsorize the dependent variable at the 5th and 95th percentiles (Online Figure A2, row (2)).</td><td>✓</td></tr><tr><td>3</td><td>Extremely large channels bias the estimate.</td><td>Drop streamers in the 95th percentile of predeparture followers (Online Figure A2, row (3)).</td><td>✓</td></tr><tr><td>4</td><td>Decrease in content supply is short-lived.</td><td>Use a longer time window of 120 and 180 days (Online Figure A2, rows (4) and (5)).</td><td>✓</td></tr><tr><td>5</td><td>The break of star streamer Tfue during our observation period biases the results.</td><td>Use a time window that excludes Tfue&#x27;s break (Online Figure A2, row (6)).</td><td>✓</td></tr><tr><td>6</td><td>Some channels become inactive before Ninja&#x27;s turnover, thereby biasing the result.</td><td>Require that channels stream Fortnite at least once in the month before Ninja&#x27;s turnover (Online Figure A2, row (7)).</td><td>✓</td></tr><tr><td>7</td><td>Serial correlation causes inconsistent standard errors that are too low.</td><td>Collapse panel into two periods, following Bertrand et al. (2004) (Online Table A3, column (1)).</td><td>✓</td></tr><tr><td>8</td><td>Unobservable event before Ninja&#x27;s departure confounds the estimation.</td><td>Only use pretreatment data and create artificial events in the preperiod (Online Table A3, columns (2)-(4)).</td><td>✓</td></tr><tr><td>9</td><td>Spurious group effects cause a false positive result.</td><td>Only use the control group data and randomly assign a treatment indicator to 50% of the channels; repeat this procedure 1,000 times (Online Figure A3).</td><td>✓</td></tr><tr><td>10</td><td>Results are an artifact of the coarsened exact matching procedure.</td><td>Repeat the analysis for the unmatched sample, using entropy balancing and generalized synthetic control (Online Table A4).</td><td>✓</td></tr><tr><td>11</td><td>German streamers are not a suitable control group.</td><td>Use a different control group comprised of other European language channels (Online Table A5, column (1))</td><td>✓</td></tr><tr><td>12</td><td>Results are an artifact of different seasonality between English and German channels.</td><td>Use a different control group comprised of Minecraft channels (Online Table A5, column (2)), falsification checks for 2020 and 2021 (Online Table A6), and preyear control variables (Online Table A7).</td><td>✓</td></tr></table>

In a second set of tests, reported in Online Table A3, we attempt to rule out typical biases in DiD designs. First, to safeguard against an underestimation of the standard errors in panel data because of serial correlation, we implement the recommended two-period test. The hypothesis is again confirmed. Second, to rule out a false positive finding, we restrict the sample to the preswitch period and then define three different artificial events, at t � 15, t � 30, and t � 45. The insignificant coefficients suggest that our result is not because of a spurious effect in the pretreatment period. Further, to safeguard against spurious group effects, we follow Kogan et al. (2017) and restrict the sample to the control group, randomly assigning an artificial treatment indicator to channels. We then reestimate Equation (1) 1,000 times and plot the coefficients (Online Figure A3). If this randomly assigned placebo treatment indicator is significant, then our effect might be spurious. By contrast, we observe that the distribution of the estimate is centered around zero. A Kolmogorov–Smirnov test cannot reject the null hypothesis of a normal distribution, and a t-test cannot reject the null hypothesis that the mean of the distribution is zero. Thus, there is no evidence of a false positive result.

Third, we took steps to rule out concerns over the matching procedure. Results are in Online Table A4 and are consistent when we do not use any matching procedure (column (1)). Further, when using entropy balancing instead of the CEM, which permits us to retain the full sample by providing a reweighting algorithm that homogenizes the treatment and control groups, results remain consistent. Finally, results remain consistent if we apply a generalized synthetic control approach.

Fourth, there could be asymmetries between the market for English- and German-language channels in the sense that the latter market is smaller, which makes matching difficult. However, we find Hypothesis 1 confirmed when we replicate our estimations using channels in German, French, Swedish, Norwegian, Finnish, Dutch, Danish, Czech, and Polish language as reported in column (1) of Online Table A5.

Finally, seasonal differences between English and German (or European) channels could be concerning, for instance, because of the summer school break. Summer breaks are relatively similar across Germany and the United States (German American Cultural Foundation 2024), but one could be concerned that the timing of the German summer semester (April to September) overlaps considerably with the summer break in most English-speaking countries (May to August), thereby causing differences in viewing patterns.<sup>9</sup> We conduct three tests to assess this possibility. In a first test, we replace the control group with English Minecraft channels. Seasonality should now be identical across groups, and Minecraft is similar in popularity to Fortnite but was not streamed by Ninja. Results remain consistent as reported in column (2) of Online Table A5. In a second test, we focus on falsification. Assuming that seasonality differences between German and English streamers explain the results, we should observe a difference also in the years after Ninja’s departure. However, when we replicate our analysis using data from 2020 and 2021, as reported in Online Table A6, we do not observe any significant effect, which further safeguards the findings from concerns of seasonality. Finally, we reestimate our regressions including content supply and number of views/followers from the past year as control variables, reported in Online Table A7. By incorporating these historical data points, we aim to account for seasonal variations. Once again, results remain consistent.

## 6. Empirical Extensions

## 6.1. Theoretical Mechanisms

In the theoretical prose, we offer two mechanisms that might explain a decline in content production: desertion and downsizing. We examine desertion by estimating whether the departure caused channels to switch to the rival platform (MIXER) or discontinue streaming on Twitch entirely (DISCONTINUED). As these variables are time invariant, we compare treated and control channels in the postperiod:

$$
Y _ {i} = \beta_ {0} + \beta_ {1} T R E A T _ {i} + \tau_ {t} + \epsilon_ {i, t},\tag{2}
$$

where the notation is identical to Equation (1), but $Y _ { i }$ is binary. As MIXER and DISCONTINUED contain mostly zeros (1% overlap between Mixer and Twitch, 7% classified as discontinued) and given that maximum likelihood estimators can be biased when there is little information in the data (e.g., rare events), we use a Firth logit estimator to account for zero-inflation challenges.

Results are in Table 5. Column (1) regresses MIXER on the treatment indicator and the controls. The coeffi cient is insignificant, indicating no evidence that Ninja’s departure increased streamers’ likelihood to sign up for the Mixer platform. Column (2) repeats the same for

Table 5. Test for Desertion Mechanism

<table><tr><td></td><td>DV = Mixer(1)</td><td>DV = Discontinued(2)</td></tr><tr><td>Treat</td><td>1.314(0.957)</td><td>0.383(0.334)</td></tr><tr><td>Controls</td><td>x</td><td>x</td></tr><tr><td>Observations</td><td>520</td><td>520</td></tr></table>

Notes. Maximum-likelihood estimates (Firth estimator). N are channel observations. Adjusted $R ^ { 2 }$ not available for this estimator Standard errors in parentheses. The control variables are natural log of FOLLOWERS, VIEWERS, MINS STREAMED, AGE, and the binary variable MATURE  
\*, \*\*, \*\*\* indicate significance at the 5%, 1%, and 0.1% levels, respectively.

DISCONTINUED. The coefficient on TREAT is insignificant, lending no evidence to the claim that Ninja’s departure caused channels to drop out of the Twitch platform. Taken together, these estimations do not support a desertion mechanism. Online Table A8 reports the results without controls, which are consistent.

To assess downsizing, following prior IS literature (Huang et al. 2021, Lin and Rai 2024, Forderer and Burtch 2025), we use the indirect effects model of Ima et al. (2011). The intuition is to isolate the portion of the causal effect of the star turnover on channels’ content production that is attributable to decreases in channels viewership. In this model, the variable X (star turnover) is assumed to have an effect on Y (channel’s content production), yet part of the effect is allowed to operate through M (channels’ viewership), that is, via mediation. The indirect effect is given by X influencing M, which influences Y. The indirect effect is the portion of the X–Y effect that can be explained, whereas the direct effect is the unexplained portion. Formally, this requires estimating the two following equations:

$$
\begin{array}{r} M _ {i, t} = \beta_ {0} + \beta_ {1} T R E A T _ {i} + \beta_ {2} A F T E R _ {t} + \beta_ {3} T R E A T _ {i} \\ \times A F T E R _ {t} + \epsilon_ {i, t}, \end{array}\tag{3}
$$

$$
\begin{array}{r l} \text { MINS   STREAMED } _ {i, t} & = \lambda_ {0} + \lambda_ {1} \text { TREAT } _ {i} + \lambda_ {2} \text { AFTER } _ {t} \\ & + \lambda_ {3} \text { TREAT } _ {i} \times \text { AFTER } _ {t} + \lambda_ {4} M _ {i, t} \\ & + \epsilon_ {i, t}, \end{array} \tag {4}
$$

where M denotes the mediator (i.e., VIEWERS, which is the average number of viewers of channel i on day t) and the remainder of the variables and indices follow the same notation as in Equation (1). For downsizing to be present, three conditions must be met. First, in Equation (3), the treatment must have a significant negative effect on M $( \beta _ { 3 } < 0 )$ , such that Ninja’s turnover reduces the viewers of the treated peer channels. Second, in Equation (4), the coefficient of M must be significant and positive $( \lambda _ { 4 } > 0 )$ , when controlling for the direct effect of TREAT × AFTER on MINS STREAMED. Third, the average causal mediation effect (ACME) must be statistically significant and negative. The ACME is the estimate of the effect that TREAT × AFTER (Ninja’s turnover) exerts on MINS STREAMED through M (VIEWERS). The method for calculating the ACME is to use Equation (3) to simulate predictions for M for both treatment and control after Ninja’s turnover and plug the predicted M into Equation (4) for $T R E A T \times A \bar { F T } E \bar { R }$ � 1 and $T R E A T \times A F T E R = 0$ . This simulates predictions of MINS STREAMED, which allows us to compare the average differences for both (Imai et al. 2011). This is implemented via nonparametric estimation. Confidence intervals are obtained via bootstrapping.

Results are in Table 6 and are consistent with downsizing. Column (1) shows that the first condition is met. Ninja’s turnover significantly reduced the viewership of peer channels as inferred from estimating Equation (3) using Log(VIEWERS) as dependent variable by $1 0 0 ( \mathrm { \tilde { e } ^ { - 0 . 1 3 5 } - 1 } ) = - 1 2 . 6 \%$ . Column (2) shows that the second condition is also satisfied, suggesting that a 1% increase (decrease) in viewership increases (decreases) the minutes streamed by 1.537%. Finally, the third con dition is also satisfied such that the ACME is statistically significant as its 95% confidence interval does not include zero. The ACME is substantial in magnitude (�0.204) and accounts for 90.6% of the total effect. Note that the direct effect of Ninja’s turnover on MINS STREAMED turns insignificant because its confidence interval includes zero after accounting for the mediated effect. This suggests a full mediation via VIEWERS. Taken together, a consistent picture emerges: a star turnover represents a negative viewer shock for creators, which triggers a reduction in content provision.<sup>10</sup>

Table 6. Mediation Test for Downsizing Mechanism

<table><tr><td></td><td>DV = Log(Viewers) (1)</td><td>DV = Log(Mins streamed) (2)</td></tr><tr><td rowspan="2">Treat × After</td><td>-0.135***</td><td>-0.021</td></tr><tr><td>(0.022)</td><td>(0.011)</td></tr><tr><td rowspan="2">Log(Viewers)</td><td></td><td>1.537***</td></tr><tr><td></td><td>(0.002)</td></tr><tr><td></td><td>Mean</td><td>Confidence Interval</td></tr><tr><td>ACME</td><td>-0.204</td><td>[-0.283; -0.135]</td></tr><tr><td>Direct effect</td><td>-0.021</td><td>[-0.042; 0.002]</td></tr><tr><td>Total effect</td><td>-0.225</td><td>[-0.304; -0.146]</td></tr><tr><td>Percentage of total effect mediated</td><td>90.6</td><td>[0.671; 1.399]</td></tr></table>

Notes. OLS estimates. $ { N _ { \mathrm { ~ \scriptsize ~ = ~ } } } 6 2 , 9 2 0$ channel–day observations. Standard errors in parentheses.  
\* \*\*, \*\*\* indicate significance at the 5%, 1%, and 0.1% levels, 1 1 respectively.

## 6.2. Heterogeneity Across Stars

Next, we estimate how star popularity moderates our focal estimates. This is done to assess whether the observed effects are generalizable to other star departures and examine the heterogeneity of the effect across stars. To this end, we replicate our estimations using the turnover of two other stars, Jeremy “Disguised Toast” Wang and Michael “Shroud” Grzesiek. Disguised Toast streamed the game Hearthstone and announced a switch from Twitch to Facebook Gaming on November 22, 2019 (Esports Observer 2019). Shroud switched from Twitch to Mixer on October 24, 2019, and mostly streamed the game Apex Legends. We proceed identically to our analysis of Ninja but use Hearthstone channels for Disguised Toast and Apex Legends channels for Shroud. Specifically, we exploit the fact that Ninja, Shroud, and Disguised Toast possess different degrees of popularity. In terms of followers, Ninja is by far the largest (14.5 million), followed by Shroud (6.3 million), and then Disguised Toast (1.3 million). Online Table A12 reports the balance checks.<sup>11</sup>

Table 7. Star Heterogeneity Analysis

<table><tr><td></td><td>DV = Log(Mins streamed)</td></tr><tr><td>Treat × After (Ninja)</td><td>-0.228***(0.037)</td></tr><tr><td>Treat × After × Shroud</td><td>0.101+(0.054)</td></tr><tr><td>Treat × After × Disguised Toast</td><td>0.184***(0.039)</td></tr><tr><td>Channel fixed effects</td><td>x</td></tr><tr><td>Time fixed effects</td><td>x</td></tr><tr><td>Time trend</td><td>x</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.402</td></tr></table>

Notes. OLS estimates. $\begin{array} { r c l } { N } & { = } & { 3 8 6 , 1 3 8 } \end{array}$ channel-day observations. Adjusted $R ^ { 2 }$ includes variation explained by the channel fixed effects. Standard errors in parentheses.  
<sup>+</sup>, \*, \*\*, \*\*\* indicate significance at the 10%, 5%, 1%, and 0.1% levels, 11 respectively.

Results are in Table 7 and indicate two key takeaways. First, we find support for the notion that star departure has a negative effect on creators’ minutes streamed. This corroborates our main estimations and refutes the concern that the drop in peer content production is simply a Ninja effect. Second, we find that Ninja’s departure had the largest effect, followed by Shroud, then Disguised Toast. We can see that the effect for Ninja is 100(e �0.228 $1 ) = - 2 0 . 4 \%$ , for Shroud $1 0 0 ( \mathrm { e } ^ { - 0 . 2 2 8 + 0 . 1 0 \dot { 1 } } - 1 ) = - 1 1 . 9 \% ,$ and for Disguised Toast $1 0 0 ( \mathrm { e ^ { - 0 . 2 2 8 + 0 . 1 8 4 } - \dot { 1 } ) = - 4 . 3 \% }$ This observation is in line with the interpretation that star popularity influences the magnitude of the effects with less popular stars having smaller effects on content supply.

## 6.3. Effect on Content Diversification

From a downsizing perspective, we would expect a further reaction by streamers, namely, that they attempt to diversify into streaming non-Fortnite content. Put simply, Ninja’s peers might diversify after Ninja’s departure in order to soften the decrease in Fortnite viewership on Twitch and to retain viewers by streaming a content category that is not affected by the viewer drain caused by Ninja’s departure. To account for the fact that the SHARE NON-FORTNITE CONTENT is conditional on streaming, we next interact the DiD coefficient with STREAMED. Results are in Table 8 and confirm that streamers significantly increased their share of non-Fortnite content.<sup>12</sup> This is plausible given that streamers who had a diversified streaming content portfolio before Ninja’s departure (Table 3, Hypothesis 2) exhibit a smaller decrease in minutes streamed compared with nondiversified streamers.

## 7. Discussion and Conclusion

This research makes a number of important contributions to research in information systems and beyond.

Table 8. Content Diversification After Star Departure

<table><tr><td></td><td>DV = Share Non-Fortnite Content</td></tr><tr><td>Treat × After</td><td>0.003(0.002)</td></tr><tr><td>Treat × After × Streamed</td><td>0.043*(0.019)</td></tr><tr><td>Channel fixed effects</td><td>x</td></tr><tr><td>Time fixed effects</td><td>x</td></tr><tr><td>Time trend</td><td>x</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.519</td></tr></table>

Notes. OLS estimates. $ { N _ { \mathrm { ~ \scriptsize ~ = ~ } } } 3 1 , 7 2 0$ channel–day observations Adjusted $R ^ { 2 }$ includes variation explained by the channel fixed effects Standard errors in parentheses.  
\* \*\*, \*\*\* indicate significance at the 5%, 1%, and 0.1% levels, 1 1 respectively.

Whereas much of the literature emphasizes the positive role stars play when joining a platform for demand-side adoption (Rochet and Tirole 2003, Binken and Stremersch 2009, Hogendorn and Ka Yat Yuen 2009), we are able to extend this understanding by examining the peer effects of star departures. To date, peer effects have mostly been examined via the presence of a star rather than the star’s departure (Ershov 2018, Zhang et al. 2019, Bockstedt et al. 2022, Lueker et al. 2022, Carroni et al. 2024). We find that losing a star to a rival platform has strong negative effects on the content production of the platform such that it suffers a reverberating loss in content. The effects we observe are sizeable and persistent, indicating a decline in production by �20.4%, and are detectable up to half a year after the star switch.

This finding is meaningful because it suggests that the departure of a star is a curse—rather than a blessing—for peer creators. Importantly, the reason is not that other creators follow the star to the rival platform, thus deserting their original platform, but rather that creators decrease their content supply to the original platform because of decreased demand. This finding provides a more nuanced view on the role of network effects, namely, that positive externalities created when a star joins a platform are not permanent but fragile and can turn negative once a star leaves a platform. Our findings challenge the assumption that stars solely generate positive network effects, highlighting instead how their departure can destabilize platform ecosystems.

A further contribution stems from the analysis of creator heterogeneity and its influence on content production. We provide empirical evidence that creators response to the departure of a star creator is not uniform but varies significantly depending on their content focus and audience size. Creators with more diversified content portfolios and larger followership are better equipped to maintain their content production in the wake of a star departure. This finding shows that the effect of star departures is not only a function of overall network effects but also the specific characteristics and strategies of individual creators. Creators who are less reliant on a single content category or a spillover from star creators are more likely to sustain their production, suggesting that platforms with more diversified creators are less vulnerable to shocks. The implication is, therefore, that platform ecosystems thrive not only through network growth but also through fostering heterogeneity in creators’ content.

The study also contributes to our understanding of platform management (Qiu et al. 2017, Foerderer et al. 2021, Li et al. 2022, Lee et al. 2023). Whereas much of the existing research focuses on the acquisition of star creators to boost platform attractiveness (Binken and Stremersch 2009, Corts and Lederman 2009, Hogendorn and Ka Yat Yuen 2009), our work highlights the importance of retaining star creators to avoid the adverse effects of their departure. Stars are crucially important for a platform because their departure does not only affect their viewership but the amount of content supplied by other channels (which, in many ways, casts them as a loss leader). Managers are, thus, compelled to engage in a complicated calculus when negotiating with stars (Elberse and Leszczynski 2020) because their departure not only yields the loss of the star’s content but yields negative spillovers for the residual human capital that remains after their departure. Moreover, the negative spillover stemming from the human capital loss likely has downstream effects for the advertising revenues collected by the platform. Every streamed minute represents potential advertising space, and as content declines, so does the space for advertising, one of the platforms main revenue streams. Platforms should reflect on the reasons behind turnovers to take appropriate actions in limiting them in the first place. For voluntary turnovers, platforms might need to understand streamers’ individual grievances with the platform and their preferences by creating feedback mechanisms or providing more support.

This work is subject to boundary conditions that represent fruitful avenues for future research. Although we find consistent results when analyzing the departures of two further stars, future work should consider star departures in more diverse contexts to probe the generalizability of our findings. For example, do similar effects manifest across platforms hosting different content types. Platforms emphasizing utilitarian content, such as educational resources, may exhibit different effects compared with those centered on hedonic content, such as gaming or entertainment. As a result, creators in utilitarian contexts may experience smaller demand spillovers because of a greater differentiation and demand for content. Future research should explore whether these content-based differences result in distinct reactions to star departures. More broadly, future research should consider star departures on platforms that do more than enable the production and consumption of user-generated content, such as e-commerce platforms such as Amazon or Etsy, on which stars may manifest as top sellers. In such markets, we might observe significant reductions in overall traffic if a star seller quits, notably if the seller forecloses the platform’s access to popular brands. However, unlike the focal context, desertion may play a much greater role because sellers can more easily move from platform to platform to sell their goods.

Another promising avenue for future research involves exploring the interplay between viewer migration and star departures. Our study does not track to where demand migrates after a star’s departure, and this remains a hole in academic understanding of how viewers react to stars. The key challenge in such investi gations is data access and the ability to track viewing time, migration, and preferences across platforms. In contrast, future studies might also investigate sta departures on platforms that are less prone to viewer migration, for example, Instagram, in which content boundaries are more fluid; recommendation algorithms guide users toward diverse content; and stars attract a broad, platform-wide audience rather than an audience confined to a specific segment. On such platforms, a star’s departure could create greater opportunities for creators, including those with diversified content, which eventually make it more likely for future work to observe a demand vacuum. Finally, to understand star departures better, scholarship should investigate effects conditional on the nature of the turnover event. Forced turnovers, such as bans because of policy violations, might provoke a different set of reactions than the vol untary turnover we study here: viewers might leave the platform in protest, perhaps causing a greater prevalence of desertion among streamers as well.

In conclusion, our quasi-experimental case study of star turnover on a live-streaming platform indicates that the turnover decreased peer creators’ content contribution markedly, suggesting the departure of a star contracts supply for the platform overall. The negative star turnover effect on content contribution is lesser for creators who have a diversified content portfolio and are relatively more popular. The overall negative effect operates through a downsizing rather than desertion mechanism, (i.e., the remaining creators reduce their contribution as opposed to abandoning the platform entirely) and is stronger as star popularity increases.

## Acknowledgments

The authors thank the senior editor, associate editor, and three anonymous reviewers for their thoughtful and constructive feedback throughout the review process. The authors are grateful for the insightful comments received from participants at research seminars hosted by Erasmus University Rotterdam, University of Bremen, Goethe University Frankfurt am Main, HEC Lausanne, Indian School of Business, Ludwig Maximilian University Munich, Uni versity of Munster, ¨ and University of Zurich. The authors also appreciate the valuable suggestions provided by attendees at the Workshop on Information Systems and Economics; workshop on Information Systems Design, Analytics, and Economic Behavior; the workshop on Statistical Challenges in E-Commerce Research; Digital Economy Workshop; the Conference on Information Systems and Technology; and the Platform Strategy Symposium. Their perspectives helped the authors refine and strengthen the arguments presented in this paper. The authors are particularly grateful to Joerg Claussen and Joost Rietveld for their valuable comments. The first two authors contributed equally to this research.

## Endnotes

<sup>1</sup> Online Appendix B briefly reviews the research on creator management from an incentive perspective, research on live-streaming platforms (e.g., Ghose et al. 2024), and the broader research on stars in non-multisided market settings (e.g., Azoulay et al. 2010).

Downsizing and desertion represent foundationally different strategic reactions to the change in the competitive landscape. At a high level, downsizing represents a marginal reallocation of resources away from an area of competition, whereas desertion represents a complete reallocation. Users may not be able to consume the star’s content elsewhere but on the new platform. As stars garner disproportional admiration from viewers, we might expect their departure to reduce demand for their competitors. This is important because, under a downsizing regime, content creators are compelled to maintain their presence in the competitive arena, whereas under desertion, those resources can be reallocated in full. Thus, if a crea tor downsizes, the creator is compelled to maintain the infrastructure and support activities that facilitate profitability (e.g., engaging with fans, cultivation of advertising streams, and so forth). Desertion requires none of these, meaning that the creator can target different competition and even rebrand entirely.

<sup>3</sup> This view is not uncontested. Following theory from classic competitive dynamics (see Chen and Miller 2012), star turnover could also increase the output of peer creators. The intuition derives directly from Cournot competition: insofar as a market participant’s exit can change the market’s structure (Doherty and Delener 2001), the demand that was previously concentrated on the star’s content is no longer being fulfilled, creating a vacuum (D’Aveni et al. 2010). To capture the glut of demand, peers may fill the holes left in the market by increasing production (e.g., Perloff et al. 1995, Ren et al. 2019). By doing so, they become more visible and thereby potentially attract new followers who are searching for similar content. Yet this is less likely in our context because low switching cost between digital platforms may prevent the buildup of a demand vacuum.

The German school system aims for students to reach an A2 level of English proficiency (with elements of B1) by the end of lower secondary education (Sekundarstufe I), as defined by the Common European Framework of Reference for Languages (Council of Europe 2001, Ministry of School and Education NRW 2019). A2 stipulates that students can “ … understand phrases and the highest frequency vocabulary related to areas of most immediate personal relevance (e.g., very basic personal and family information, shopping, local area, employment) … ” and “ … can catch the main point in short, clear, simple messages and announcements” (Council of Europe 2001, p. 26). This is typically insufficient to enjoy nativespeaking English streams characterized by fast-paced speech and the excessive use of slang. In the United States, only 20% of K–12 students are enrolled in foreign language classes. Moreover,

Spanish is the most popular second language (75%), and German one of the least popular ones (4.5%) (Pew Research Center 2018). Thus, we expect that German channels have different audiences and are, therefore, not affected.

This also suggests that platform competition (e.g., YouTube Gaming or Facebook Gaming) does not bias our estimates.

<sup>6</sup> Individual lags can be underpowered and show higher variability, which is why the confidence intervals can overlap with zero. Critically, it bears note that the estimates are jointly significant as can b seen in Table 3.

<sup>7</sup> Although the negative effects of Ninja’s switch also persist long term, the coefficient decreases in magnitude. This could be an empirical artifact caused by noise in the dependent variable increasing for longer windows around the switch. Another explanation is that some fraction of Ninja’s followership that left with him to Mixer returned to Twitch after some time, providing demand for Fortnite.

<sup>8</sup> An inspection of the top 100 Fortnite channels confirms that no other popular Fortnite streamers announced turnovers or breaks during our observation window of (�60,60).

<sup>9</sup> We thank an anonymous reviewer for this suggestion.

<sup>10</sup> The Online Appendix reports robustness checks. First, Online Table A9 uses the count of followers to infer demand. The result are consistent. Second, Online Figure A4 shows the standard sensi tivity checks on the assumption of sequential ignorability. To conclude that the ACME is not statistically different from zero correlation between the error terms would have to be almost perfect, namely, $\rho \geq 0 . 9 4 7 6 ,$ , which attributes considerable robustness to the observed mediation effect. Third, Online Table A10 reports consistent results when isolating the measurement of mediator and dependent variable over different time windows immediately afte the switch. Fourth, Online Table A11 uses two-stage least squares to predict the decline in viewer demand in the first stage and then plugs the predicted estimates into the second stage for estimating the content supply. The results we obtain from this exercise are consistent. Finally, Online Figure A5 provides descriptive evidence at the platform level by plotting Fortnite viewership and content production for all channels on Twitch. Consistent with the downsizing mechanism, we observe a decline in both Fortnite viewership and content production after Ninja switched to Mixer.

<sup>11</sup> We note that our use of German control group channels follows the typical recommendation of the literature (Baker et al. 2022) to leverage never-treated control units to obviate false comparisons in staggered difference-in-difference estimations.

<sup>12</sup> If we extend the window to 60 days, the effect turns insignificant. This suggests that, whereas channels attempt to diversify, they stop doing so after one month post turnover, plausibly because diversifying requires effort in terms of reskilling and may not have the intended effect of sufficiently increasing viewership.

## References

Abadie A, Athey S, Imbens GW, Wooldridge JM (2023) When should you adjust standard errors for clustering? Quart. J. Econom. 138(1):1-35

Ahuja G, Novelli E (2017) Redirecting research efforts on the diversification–performance linkage: The search for synergy. Acad. Management Ann. 11(1):342–390.

Ammann M, Horsch P, Oesch D (2016) Competing with superstars Management Sci. 62(10):2842–2858.

Angrist JD, Pischke JS (2009) Mostly Harmless Econometrics: An Empiricist’s Companion (Princeton Press, Princeton, NJ).

Armstrong M (2006) Competition in two-sided markets. RAND J. Econom. 37(3):668–691.

Azoulay P, Zivin JSG, Wang J (2010) Superstar extinction. Quart. J. Econom. 125(2):549–589.

Baker AC, Larcker DF, Wang CC (2022) How much should we trust staggered difference-in-differences estimates? J. Financial Econom. 144(2):370–395.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1):249–275.

Bhargava HK (2022) The creator economy: Managing ecosystem supply, revenue sharing, and platform design. Management Sci. 68(7):5233–5251.

Binken JLG, Stremersch S (2009) The effect of superstar software on hardware sales in system markets. J. Marketing 73(2):88–104.

Bockstedt J, Druehl C, Mishra A (2022) Incentives and stars: Competition in innovation contests with participant and submission visibility. Production Oper. Management 31(3):1372–1393.

Boudreau KJ (2012) Let a thousand flowers bloom? An early look at large numbers of software app developers and patterns of inno vation. Organ. Sci. 23(5):1409–1427.

Boudreau KJ (2018) Amateurs crowds & professional entrepreneurs as platform complementors. NBER Working Paper No. 22952, National Bureau of Economic Research, Cambridge, MA.

Boudreau KJ, Jeppesen LB (2015) Unpaid crowd complementors: The platform network effect mirage. Strategic Management J. 36(12):1761–1777.

Bru¨ ndl S, Matt C, Hess T, Engert S (2023) How synchronous participation affects the willingness to subscribe to social live streaming services: The role of co-interactive behavior on Twitch. Eur. J. Inform. Systems 32(5):800–817.

Burtch G, He Q, Hong Y, Lee D (2022) How do peer awards moti vate creative content? Experimental evidence from Reddit. Management Sci. 68(5):3488–3506.

Caillaud B, Jullien B (2003) Chicken & egg: Competition among intermediation service providers. RAND J. Econom. 34(2):309–328.

Carroni E, Madio L, Shekhar S (2024) Superstar exclusivity in twosided markets. Management Sci. 70(2):991–1011.

Chen MJ, Miller D (2012) Competitive dynamics: Themes, trends, and a prospective research platform. Acad. Management Ann. 6(1):135–210.

Corts KS, Lederman M (2009) Software exclusivity and the scope of indirect network effects in the U.S. home video game market. Internat. J. Indust. Organ. 27(2):121–136.

Council of Europe (2001) Common European Framework of Reference for Languages: Learning, Teaching, Assessment (Cambridge Uni versity Press, Cambridge, UK).

D’Aveni RA, Dagnino GB, Smith KG (2010) The age of temporary advantage. Strategic Management J. 31(13):1371–1385.

Doherty N, Delener N (2001) Chaos theory: Marketing & manage ment implications. J. Marketing Theory Practice 9(4):66–75.

Dou Y, Wu DJ (2021) Platform competition under network effects: Piggybacking and optimal subsidization. Inform. Systems Res. 32(3):820–835.

Elberse A, Leszczynski MT (2020) Ninja: Which platform wins Esports’ biggest star? Harvard Business School Case 520-036, Boston.

Ershov D (2018) Competing with superstars in the mobile app market. NET Institute Working Paper 18-02, Networks, Electronic Commerce and Telecommunications Institute, New York.

Esports Observer (2019) Twitch streamer ZeRo jumps ship to Face book gaming. Accessed March 31, 2024, https://archive. esportsobserver.com/zero-facebook-gaming-move/.

Foerderer J, Lueker N, Heinzl A (2021) And the winner is … ? The desirable and undesirable effects of platform awards. Inform. Systems Res. 32(4):1155–1172.

Forderer J, Burtch G (2025) Estimating career benefits from online community leadership: Evidence from Stack Exchange modera tors. Management Sci. 71(3):1865–1888.

German American Cultural Foundation (2024) American schools vs. German schools. Accessed March 31, 2024, https://www.gacfoundation.org/2015/06/24/american-schools-vs-german-schools.

Ghose A, Mayya R, Yu P (2024) Do non-monetary virtual gifts enhance or diminish voluntary paid gifts? Evidence from a video game live streaming platform. Working paper, NYU Stern School of Business, New York.

Goes PB, Guo C, Lin M (2016) Do incentive hierarchies induce user effort? Evidence from an online knowledge exchange. Inform. Systems Res. 27(3):497–516.

Groysberg B, Lee LE, Nanda A (2008) Can they take it with them? The portability of star knowledge workers’ performance. Management Sci. 54(7):1213–1230.

Gu M, Liu D, Kumar S (2024) Navigating platform-led affiliate marketing: Implications for content creation and platform profit ability. Inform. Systems Res., ePub ahead of print July 5, https:// doi.org/10.1287/isre.2022.0620.

Haviv A, Huang Y, Li N (2020) Intertemporal demand spillover effects on video game platforms. Management Sci. 66(10):4788–4807.

Hilvert-Bruce Z, Neill JT, Sjo¨ blom M, Hamari J (2018) Social motivations of live-streaming viewer engagement on Twitch. Comput. Human Behav. 84(7):58–67.

Hogendorn C, Ka Yat Yuen S (2009) Platform competition with ‘must-have’ components. J. Indust. Econom. 57(2):294–318.

Huang N, Mojumder P, Sun T, Lv J, Golden JM (2021) Not registered? Please sign up first: A randomized field experiment on the ex ante registration request. Inform. Systems Res. 32(3):914–931.

Hukal P, Henfridsson O, Shaikh M, Parker G (2020) Platform signaling for generating platform content. MIS Quart. 44(3):1177–1199.

Iacus SM, King G, Porro G (2012) Causal inference without balanc checking: Coarsened exact matching. Political Anal. 20(1):1–24.

Imai K, Keele L, Tingley D, Yamamoto T (2011) Unpacking the black box of causality: Learning about causal mechanisms from experimental and observational studies. Amer. Political Sci. Rev. 105(4):765–789.

Katz ML, Shapiro C (1994) Systems competition and network effects. J. Econom. Perspect. 8(2):93–115.

King G, Nielsen R (2019) Why propensity scores should not be used for matching. Political Anal. 27(4):435–454.

Kogan L, Papanikolaou D, Seru A, Stoffman N (2017) Technological innovation, resource allocation, and growth. Quart. J. Econom. 132(2):665–712.

Lacetera N, Cockburn IM, Henderson R (2004) Do firms change capabilities by hiring new people? A study of the adoption of science based drug discovery. Adv. Strategic Management 21:133–159.

Landsman V, Stremersch S (2011) Multihoming in two-sided markets: An empirical inquiry in the video game console industry. J. Marketing 75(6):39–54.

Lee MH, Han SP, Park S, Oh W (2023) Positive demand spillover of popular app adoption: Implications for platform owners’ management of complements. Inform. Systems Res. 34(3):961–995.

Li H, Zhang C, Kettinger W (2022) Digital platform ecosystem dynamics: The roles of product scope, innovation, and collabo rative network centrality. MIS Quart. 46(2):739–770.

Liang C, Zhan S, Raghu TS (2019) The spillover of spotlight: Platform recommendation in the mobile app market. Inform. Sys tems Res. 30(4):1296–1318.

Lin YK, Rai A (2024) The scope of software patent protection in the digital age: Evidence from alice. Inform. Systems Res. 35(2):657–672.

Lueker N, Foerderer J, Heinzl A (2022) Competing with superstars: Does exclusive third-party content discourage complementary innovation? Bjørn-Andersen N, ed. Proc. 43rd Internat. Conf. Inform. Systems (AIS Electronic Library (AISeL), Atlanta).

Marchese D (2021) Teenagers made Ninja a gaming superstar. He has a message for parents. The New York Times Online (January 24), https://www.nytimes.com/interactive/2021/01/25/magazine/ ninja-interview.html.

Merton RK (1968) The Matthew effect in science: The reward and communication systems of science are considered. Science 159(3810):56–63.

Ministry of School and Education NRW (2019) Kernlehrplan fuer die Sekundarstufe I Gymnasium in Nordrhein-Westfalen. Accessed March 20, 2025, https://www.schulentwicklung.nrw.de/lehrp laene/lehrplan/199/g9\_e\_klp\_%203417\_2019\_06\_23.pdf

Needleman SE (2019) Microsoft aims to reset videogame-streaming market with ‘Ninja’ pact. The Wall Street Journal Online (August 11), https://www.wsj.com/articles/microsoft-aims-to-reset-videogamestreaming-market-with-ninja-pact-11565547932.

Parker G, van Alstyne M (2005) Two-sided network effects: A theory of information product design. Management Sci. 51(10): 1494–1504.

Parker G, van Alstyne M (2018) Innovation, openness, and platform control. Management Sci. 64(7):3015–3032.

Perloff JM, Suslow VY, Seguin PJ (1995) Higher prices from entry: Pricing of brand-name drugs. Berkeley Competition Policy Working Paper No. CPC99-03, CA.

Pew Research Center (2018) Most European students are learning a foreign language in school while Americans lag. Accessed March 31, 2024, https://www.pewresearch.org/short-reads/ 2018/08/06/most-european-students-are-learning-a-foreignlanguage-in-school-while-americans-lag.

Qiu Y, Gopal A, Hann IH (2017) Logic pluralism in mobile platform ecosystems: A study of indie app developers on the iOS app store. Inform. Systems Res. 28(2):225–249.

Raj M (2024) More is (sometimes) merrier: Heterogeneity in demand spillovers and competition on a digital platform. Strategic Man agement J. 45(13):2611–2641.

Ren CR, Hu Y, Cui TH (2019) Responses to rival exit: Product vari ety, market expansion, and preexisting market structure. Strategic Management J. 40(2):253–276.

Robidoux B (2019) Pro gamer Ninja shocks fans by announcing he’s leaving Twitch & only streaming on Mixer. Hollywood Life Online (August 1), https://hollywoodlife.com/2019/08/01 ninja-leaves-twitch-mixer-announcement-tweet.

Rochet JC, Tirole J (2003) Platform competition in two-sided mar kets. J. Eur. Econom. Assoc. 1(4):990–1029.

Rosen S (1981) The economics of superstars. Amer. Econom. Rev. 71(5):845–858.

Rosman K (2022) Spotify bet big on Joe Rogan. It got more than it counted on. The New York Times Online (February 17), https://

www.nytimes.com/2022/02/17/arts/music/spotify-joe-roganmisinformation.html.

Singh A (2023) 5 Most unexpected streamer platform signings of all time. Sportskeeda Online (June 3), https://www.sportskeeda com/esports/unexpected-streamer-platform-signings-time.

Sjo¨blom M, Hamari J (2017) Why do people watch others play video games? An empirical study on the motivations of Twitch users Comput. Human Behav. 75(10):985–996.

Smith D (2019) Jessica Blevins, the 27-year-old manager and wife of the most popular video-game player in the world, reveals the inside story of Ninja’s move to Microsoft’s Mixer. Business Insider Online (October 2), https://www.businessinsider.com/ jessica-blevins-ninja-wife-manager-on-leaving-twitch-for-mixer-2019-9?r=US&IR=T.

Stephen B (2019) Ninja’s 80,000 Mixer viewers show that he’s bigger than just Twitch. The Verge Online (August 2), https://www. theverge.com/2019/8/2/20752172/ninja-mixer-viewers-twitch fortnite.

Susarla A, Oh JH, Tan Y (2012) Social networks and the diffusion of user-generated content: Evidence from YouTube. Inform. Systems Res. 23(1):23–41.

Tan TF, Netessine S, Hitt L (2017) Is Tom Cruise threatened? An empirical study of the impact of product variety on demand concentration. Inform. Systems Res. 28(3):643–660.

Tiwana A, Konsynski B, Bush AA (2010) Research commentary— Platform evolution: Coevolution of platform architecture, governance, and environmental dynamics. Inform. Systems Res. 21(4):675–687.

Venkatraman N, Lee C-H (2004) Preferential linkage and network evolution: A conceptual model and empirical test in the U.S. video game sector. Acad. Management J. 47(6):876–892.

Wang Z, Yang L, Hahn J (2023) Winner takes all? The blockbuster effect on crowdfunding platforms. Inform. Systems Res. 34(3): 935–960.

Zhang S, Singh PV, Ghose A (2019) A structural analysis of the role of superstars in crowdsourcing contests. Inform. Systems Res. 30(1):15–33.

Zhao K, Hu Y, Hong Y, Westland JC (2021) Understanding characteristics of popular streamers on live streaming platforms: Evi dence from Twitch.tv. J. Assoc. Inform. Systems 22(4):1076–1098.

Zhao K, Lu Y, Hu Y, Hong Y (2023) Direct and indirect spillovers from content providers’ switching: Evidence from online livestreaming. Inform. Systems Res. 34(3):847–866.

Copyright of Information Systems Research (INFORMS) is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
