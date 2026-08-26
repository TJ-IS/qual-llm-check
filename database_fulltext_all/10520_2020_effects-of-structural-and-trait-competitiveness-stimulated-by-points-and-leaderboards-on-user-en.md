---
otero_id: 10520
otero_key: "975EQNXG"
title: "Effects of structural and trait competitiveness stimulated by points and leaderboards on user engagement and performance growth: A natural experiment with gamification in an informal learning environment"
authors: "Laura Amo; Ruochen Liao; Rajiv Kishore; Hejamadi R. Rao"
year: "2020"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2020.1808540"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Effects of structural and trait competitiveness stimulated by points and leaderboards on user engagement and performance growth: A natural experiment with gamification in an informal learning environment

Laura Amo , Ruochen Liao , Rajiv Kishore & Hejamadi R. Rao

To cite this article: Laura Amo , Ruochen Liao , Rajiv Kishore & Hejamadi R. Rao (2020): Effects of structural and trait competitiveness stimulated by points and leaderboards on user engagement and performance growth: A natural experiment with gamification in an informal learning environment, European Journal of Information Systems, DOI: 10.1080/0960085X.2020.1808540

To link to this article: https://doi.org/10.1080/0960085X.2020.1808540

![](/api/attachments/975EQNXG/fulltext/images/0799d1a8834110ea823b4a0c0c2b92a8ea85a5b0e13a9dbfdaf43a5ccd6b5253.jpg)

View supplementary material

![](/api/attachments/975EQNXG/fulltext/images/5475c3fe0b632800e13abab4b2d647a38851c230ba736750318a2a59f7de7dce.jpg)

Submit your article to this journal

![](/api/attachments/975EQNXG/fulltext/images/292a2fa97b999386617c8c04c9d9d1e4eba87990deff0fc181e450c220f3fa8e.jpg)

View related articles

Published online: 09 Oct 2020.

![](/api/attachments/975EQNXG/fulltext/images/946d3bda07146c580d6acbdea2ba0264fa272018c595579be09b3cf0c806d80d.jpg)

![](/api/attachments/975EQNXG/fulltext/images/9e89a599dde97aadeb53c3cb62a07938c90b60b32af3209713803d476cb30cbc.jpg)

Article views: 13

![](/api/attachments/975EQNXG/fulltext/images/332921f6c6e81c186d8488d6a9074ba25c9ee6b363c96b12cad5e18afe9cc6db.jpg)

O View Crossmark data CrossMark

RESEARCH ESSAY

Check for updates

# Efects of structural and trait competitiveness stimulated by points and leaderboards on user engagement and performance growth: A natural experiment with gamification in an informal learning environment

Laura Amo <sup>a</sup>, Ruochen Liao <sup>b</sup>, Rajiv Kishore <sup>c</sup> and Hejamadi R. Rao <sup>d</sup>

<sup>a</sup>Management Science & Systems, University at Bufalo, the State University of New York, Bufalo, New York, United States; <sup>b</sup>Information Systems & Operations Management, University of Texas at Arlington, Arlington, Texas, United States; <sup>c</sup>Management, Entrepreneurship, and Technology, University of Nevada, Las Vegas, Las Vegas, United States; <sup>d</sup>Information Systems and Cyber Security, University of Texas at San Antonio, San Antonio, United States

## ABSTRACT

Rooted in theories of competitiveness and social comparison, we model the efects of users’ structural and trait competitiveness on their engagement and performance growth in an informal learning environment. We hypothesise that game elements of points and leaderboards stimulate users’ structural competitiveness, which afects users’ engagement and has an inverted-U efect on performance growth. We further hypothesise that these efects are stronger among individuals with higher trait competitiveness. We tested our hypotheses using data from a natural experiment conducted over 300 days on 88,310 unique users who made 215,920 game interactions within the Cyber Detectives exhibit at the Tech Interactive museum in California. Our results are based on two objective measures of trait-competitiveness as both behaviour and outcome (percentile ranking on total time spent and number of badges earned, respectively), multiple objective measures of user engagement (time spent per attempt, number of reattempts, and daily user attempts), and an objective measure of performance growth (points). Results provide overall support to our hypotheses. We contribute to the gamification literature by providing strong causal evidence of points and leaderboards triggering structural and trait competitiveness, which interact to afect both engagement and performance growth in informal learning contexts.

ARTICLE HISTORY Received 5 March 2019 Accepted 6 August 2020

KEYWORDS Gamification; competitiveness; performance growth; engagement; competitive game element; social comparison

## 1. Introduction

Gamification, or the addition of game-like features to non-game contexts (Deterding, 2011), is a growing market (MarketsandMarkets, 2017) with entire companies now dedicated to integrating various game elements to all types of non-gaming environments (e.g., Continu: https://continu.co; Hoopla: https://www.hoo pla.net/). Certain gamification scholars consider competitive game elements, such as points and leaderboards, to be instrumental in efective game design (Sepehr & Head, 2018), theoretically linking these elements to competition, recognition, performance and status (Blohm & Leimeister, 2013; Santhanam et al., 2016). A central focus of the information systems (IS) field is on improving application of computers and technology within organisations (Hirschheim & Klein, 2012), and competitive game elements have emerged as a popular design choice in information applications and systems (Koivisto & Hamari, 2019; Landers et al., 2019). Competition serves to motivate users through challenge and enjoyment (Franken & Brown, 1995) and gamified systems (i.e., information systems with competitive game elements) are considered efective because these types of systems meet both utilitarian (i.e., productivity) and hedonic needs of the user (Gerow et al., 2013; Koivisto & Hamari, 2019).

However, while competitive game elements are popular features of gamified applications, robust theoretical understanding of how various game elements stimulate diferent types of competitiveness is lacking in the gamification literature. Competitiveness has multiple dimensions (Kohn, 1992; Orosz et al., 2018) yet the majority of IS research focuses on how game elements serve as competitive aspects of the game itself (i.e., structural competitiveness) as opposed to individual diferences in competitiveness (i.e., trait competitiveness). Accordingly, popular theories used to explain the efects of competitive game elements, for example, self-determination theory (Deci et al., 2001; Ryan & Deci, 2000) and Festinger’s (1954) social comparison theory (used by Shepherd et al., 1995), have been applied in ways that tend to reflect a onedimensional theoretical perspective of competitiveness. Relatedly, there has been limited investigation into how personality traits (e.g., trait competitiveness) drive the efects of competitive game elements, despite

IS researchers highlighting the importance of considering individual user traits in the design of gamified systems (Liu et al., 2017).

Another drawback among studies of competitive game elements is that most tend to rely on methods that do not support causal inference rendering a need for gamification studies that allow for stronger causal inferences about the connections among game elements, heterogeneous competitive behaviours, and game engagement and performance outcomes (Hamari et al., 2014). Finally, the majority of gamification studies are set in highly-structured environments such as labs (e.g. Landers et al., 2019), classrooms (e.g., Boticki et al., 2015; Ke & Grabowski, 2007) and organisations (e.g., Rodrigues et al., 2016; Suh et al., 2016). While there is evidence that informal learning environments provide powerful learning opportunities (Alavi & Leidner, 2001; Warkentin et al., 2011), nuances of gamification efects in informal learning settings such as museums have not yet been conceptualised, leaving a significant void regarding the causal efects of gamification in settings wherein informal learning takes place.

To address the gaps in the literature, we integrate theories on competitiveness and social comparison (e.g., Festinger, 1954; Garcia et al., 2013; Kohn, 1992) to conceptualise how two distinct dimensions of competitiveness – structural competitiveness and trait competitiveness – are associated with game engagement and performance outcomes in an informal learning context using a natural experiment. In so doing, we address the following research questions: How do users’ structural and trait competitiveness as stimulated by points and a leaderboard afect their game engagement and performance outcomes in an informal learning context?

We model outcomes of engagement and performance because both are established objectives of gamification (e.g., Buil et al., 2020; Chang et al., 2008; Salas et al., 2009). To establish causal links from the two distinct forms of competitiveness to engagement and performance, we test our hypotheses using data collected from a natural experiment at the Cyber Detectives gaming kiosks in the Tech Interactive (formerly The Tech Museum of Innovation) in California (museum, henceforth). Our data set includes each museum user’s individual game interaction-level data and represents 215,920 distinct game attempt observations with 88,310 distinct users over a period of 300 days on the six Cyber Detectives kiosks. The experimentally-manipulated kiosk,<sup>1</sup> NetBuilder, is the only kiosk to award points and this allowed us to compare it against the other control kiosks, which did not ofer points; additionally, the museum introduced a leaderboard at the NetBuilder kiosk halfway during the data collection period. This aforded us the opportunity to analyse this data in a natural experiment setting (before and after leaderboard; and with and without points), bolstering causal inference and strengthening our contributions.

Our findings support hypotheses on users’ game engagement and show that engagement was higher among users on NetBuilder (i.e., the experimentallymanipulated kiosk with both points and leaderboard) in terms of higher time per attempt, lower number of reattempts, and lower number of unique user attempts on the kiosk, as compared to users on the remaining five control kiosks. As hypothesised, we also found that users’ game performance on the NetBuilder kiosk exhibited an inverted-U shaped efect after the introduction of leaderboard, with users demonstrating initial performance growth followed by a performance decline in points across successive attempts.

Further, our findings are robust across two diferent operationalisations of trait competitiveness – trait competitiveness manifested as a behaviour measured as total time expenditure on all games played in the museum exhibit, and trait competitiveness manifested as an outcome measured as the number of badges earned on all games played in the exhibit. Both operationalisations yield the same results, and suggest that users with higher trait competitiveness had significantly higher game engagement and spent more time per attempt, attempted fewer times, and accounted for a higher number of users relative to all users on the NetBuilder kiosk. Trait-competitive users also drove the inverted-U performance curve in the postleaderboard time period on the NetBuilder kiosk. With one exception, results pertaining to the moderation by trait competitiveness converged across the two separate manifestations and operationalisations of trait competitiveness.

Through this study, we make a significant contribution to the gamification literature by providing a comprehensive and nuanced perspective of how two distinct game elements (i.e., points and leaderboards) both stimulate diferent types of competitiveness (i.e., structural and trait competitiveness), and how these types of competitiveness interact to afect engagement and performance in informal learning contexts. We make this contribution in three ways. First, we follow expert recommendations to draw on diferent and complementary theoretical perspectives to explain complex phenomenon (Okhuysen & Bonardi, 2011; Liu et al., 2017), and accordingly integrate literature on competitiveness and social comparison theories to develop our research model. Our model provides insight by exploring two separate dimensions of competitiveness and examining both engagement and performance growth of game users in the same study. Notably, while the relationship between game elements and performance has been studied (e.g., Zainuddin et al., 2020), performance growth among game users has not been investigated and we extend our exploration to such growth in this paper. Furthermore, we operationalise trait competitiveness in terms of both manifestation of competitive behaviour measured as efort expenditure as well as manifestation of a competitive outcome measured as acquisition of badges, thereby providing robustness to our findings. Second, we leverage features of an ecologically strong and relevant dataset collected in a natural experimental setting and are able to make strong causal inferences about the impacts that points and leaderboards have on user engagement and performance by stimulating structural and trait competitiveness among game users. Lastly, ours is one of the few studies to explore the efect of points and leaderboard on user engagement and performance in an informal learning context, such as through hands-on learning exhibits in a museum.

In the following sections, we provide an overview of the literature on competitive game elements and then describe the integrated theoretical perspective that we adopt. We then present our research model and hypotheses, followed by our findings and discussion.

## 2. Gamification and competitive game elements

The idea that diferent game elements can be integrated into a non-gaming experience as a way to increase motivation, engagement and performance is known as gamification (Deterding, 2011). Scholars have investigated a number of game design elements in relation to diferent outcomes, with many identifying competition as fundamental to gamification (e.g., Sailer et al., 2017; Sepehr & Head, 2018) and pivotal to creating positive gaming experiences (Peng & Hsieh, 2012; Vorderer et al., 2003). Accordingly, there is extant literature on specific types of game elements that stimulate a sense of competition known as competitive game elements, the likes of which include rivals, rankings, leaderboards, points, levels, and badges.<sup>2</sup> Below, we provide an overview of existing literature on competitive game elements with regard to findings about the types of competitiveness, methods, contexts, and gamification outcomes.

## 2.1. Overview of research on competitive game elements

## 2.1.1. Types of competitiveness

Guided by the theoretical literature on competitiveness and social comparison, we acknowledge and explore two distinct types of competitiveness within our study, and provide an overview of how competitiveness and social comparison overlap in our forthcoming theoretical framework. Among existing gamification studies, there has been some exploration of how competitiveness may be structurally influenced by game elements (e.g., leaderboards in Höllig et al., 2018a; rivals in Liu et al., 2013). There has been relatively less attention, however, on the other main facet of competitiveness that is trait-based (i.e., trait competitiveness) which may also be invoked by game elements. Importantly, trait competitiveness accounts for heterogeneity in competitive behaviours and outcomes among users playing competitive games. Only a handful of gamification studies have conceptualised trait competitiveness (e.g., Höllig et al., 2018a; Landers et al., 2019), and these studies rely solely on selfreported measures of trait competitiveness (e.g., via questionnaire), which are arguably less credible than objective measures because such measures are neither observed nor validated by a third party.

Trait competitiveness manifests in a number of ways and can be observed by third parties in terms of both competitive behaviours as well as outcomes from competitive behaviours. These objective measures of trait competitiveness are relatively more reliable and valid compared to self-reported measures and, accordingly, are important to consider and use. However, studies in the gamification literature have yet to use behaviours and behavioural outcomes to measure trait competitiveness. Thus, we examine both behaviour- and outcome-based measures of trait competitiveness in our study using total time spent in a game and badges earned, respectively.

## 2.1.2. Methods used

The majority of studies on competitive game elements fail to establish causal relationships between specific game elements and outcomes due to weak study designs (Hamari et al., 2014). Causal inference is the ability to conclusively attribute a causal connection to an efect (Pearl, 2009; Varian, 2016). The ideal approach for establishing causality is a randomised controlled trial (RCT) wherein participants undergo random assignment and there are reasonably large sample sizes and suitable control groups. However, RCTs are often unfeasible or impractical, and there are alternative approaches without random assignment that can be as credible as RCTs in establishing causality, approaches that are often referred to as quasi-experimental or natural experiment designs (Kim & Steiner, 2016; Shadish et al., 2002; Stuart & Rubin, 2008).

Unfortunately, the majority of gamification studies do not allow for causal inference by way of RCTs. While there are a number of experiments within the gamification literature, these studies tend to have small sample sizes, lack appropriate control groups and/or bundle various game elements together within treatments; see Hamari et al. (2014) for a review of methodological limitations of gamification studies. Likewise, quasi-experimental approaches (i.e., regression discontinuity, instrumental variable, comparative interrupted time series, diference-in-diference) are not at all common in gamification studies. As a result, robust support for causal efects of distinct game design elements on engagement and performance is presently missing from the gamification literature.

## 2.1.3. Contexts

There are a limited number of settings and contexts associated with existing gamification studies. As shown in Tables A1 – A3 (please see Appendix), the most common contexts include formal learning environments (i.e., classrooms), labs, and organisations. While studies have been conducted in informal learning settings (see Table A3), these studies tend to sufer from the methodological issues noted above. Given the growing interest in how individuals learn through self-discovery within informal learning environments (e.g., National Science Foundation’s [NSF] initiative on informal STEM learning; National Science Foundation, 2020) alongside integration of gamification into informal learning exhibits (e.g., Cesário et al., 2017), it is important to determine causal efects of gamification in these types of settings.

## 2.1.4. Outcomes

Competitive game elements are expected to motivate players with the expectation of positively afecting game engagement and performance. Again, as shown in Table A1 – A3 (see Appendix), most studies on competitive game elements have focused on either engagement or performance outcomes as opposed to both. However, some recent studies (e.g., Cesário et al., 2017; Landers et al., 2019; Mekler et al., 2017) extended explorations to both types of outcomes within the same study. In terms of engagement outcomes, researchers have focused on self-reported indicators of engagement (Cesário et al., 2017; Liu et al., 2017; Mekler et al., 2017; Rodrigues et al., 2016; Sailer et al., 2017; Santhanam et al., 2016; Suh et al., 2016; Wang, 2015). Based on our literature review, we identified only two studies with objective indicators of engagement including engagement defined in terms of game attempts and time expenditure in Liu et al. (2013) and as online activity in Hamari (2015).

With regard to performance, researchers have studied performance on learning material (e.g., Cesário et al., 2017; Christy & Fox, 2014; Mikalef et al., 2013; Nebel et al., 2017; Tsay et al., 2018; Zainuddin et al., 2020), brainstorming tasks (e.g., Landers & Landers, 2014; Santhanam et al., 2016) and gameplay (Wang, 2015). However, researchers have yet to examine how competitive game elements are associated with performance growth, or within-individual changes in performance over successive attempts. Therefore, building upon recent approaches that focus on both engagement and performance outcomes, in the present study we extend our exploration to that of objective engagement indicators and performance growth to provide further insight on how these outcomes are associated with diferent types of competitiveness.

To summarise, the existing research on competitive game elements has limitations outlined above, this body of literature is informative and provides a pathway to our current work. We consider how our research extends gamification research in providing nuanced insights into gamification by theorising the interaction efects of two diferent types of competitiveness on users’ game engagement and performance. Next, we consider two theoretical perspectives in relation to competitive game elements and present an integrated theoretical lens to better explicate the process through which these elements afect engagement and performance.

## 3. Theoretical background

## 3.1. Competitiveness and social comparison in gamification

Towards developing a deeper understanding of the unique efects of diferent competitive game elements, we integrate theories of competitiveness and social comparison. Games, by definition, are competitive and involve some degree of social comparison; the primary definition of a game is “a physical or mental competition conducted according to rules with the participants in direct opposition to each other” (Merriam-Webster, 2020). Accordingly, both competitiveness and social comparison are often used as theoretical mechanisms to explain how and why game elements impact diferent outcomes (e.g., Cagiltay et al., 2015; Nebel et al., 2017; Simões et al., 2013).

## 3.1.1. Competitiveness

Competitiveness is a desire to be the best, or to be better than others of a comparable nature (Kohn, 1992; Spence & Helmreich, 1983). While there are diferent conceptualisations of competitiveness,<sup>3</sup> we highlight and focus on the distinction between trait (i.e., intentional) competitiveness vs. structural competitiveness (Kohn, 1992). Trait competitiveness pertains to the individual diferences in “the enjoyment of interpersonal competition and the desire to win and be better than others” (Fletcher & Nusbaum, 2008; Spence & Helmreich, 1983, p. 41). Structural competitiveness, on the other hand, pertains to competitiveness derived from environmental elements that create a more competitive psychological climate (or a situational facet of the environment due to scarcity of resources and limited opportunities for goal attainment) and subsequently trigger competitive behaviour (Brown et al., 1998). It is important to note that while a particular game element as a situational facet is the same for all game users and thereby stimulates the same level of structural competitiveness among all the game users, the users nonetheless exhibit heterogeneity in their competitive behaviours and associated outcomes. These heterogeneous behaviours and outcomes result from individual diferences in trait competitiveness among diferent users.

To remain competitive with others and improve ability and performance, humans engage in social comparison wherein they compare themselves to others and evaluate ability gaps relative to other individuals. Social comparison is a form of self-judgement that provides individuals with feedback on relative social rank and can serve as a source of information (Ertac, 2005; Hoorens & Damme, 2012); it is also related to identity formation (Locander et al., 2015) and self-concept (Li et al., 2015). Social comparison takes the form of either upward comparisons (e.g., comparison with a more competent other) or downward comparisons (comparison with a less competent other), with the direction of the comparison depending on both the individual and the context (Aspinwall & Taylor, 1993; Festinger, 1954; Latané, 1966). Humans tend to make upward self-comparisons (i.e., comparison against a “better of” other) when seeking self-improvement and tend to make downward selfcomparisons (i.e., comparison against a “worse of” other) when motivated by self-enhancement (Buunk et al., 1991; Wills, 1981). Bridging the constructs of competitiveness and social comparison together, competitive behaviour is conceptualised as a manifestation of the social comparison process (Festinger, 1954; Garcia et al., 2013). Garcia et al.’s (2013) social comparison model of competitive behaviour distinguishes between individual and situational factors that promote social comparison, which leads to competitive attitudes and behaviour.

We integrate Kohn’s (1992) and Garcia et al.’s (2013) theories to model how diferent competitive game elements impact engagement and performance outcomes in an informal learning context. Considered alongside one another, Kohn’s (1992) model of traitand structural-related competitiveness and Garcia et al.’s (2013) social comparison model of competitive behaviour share significant overlap. Both theories acknowledge the role of environmental or external factors influencing competitiveness or competitive behaviour; specifically, the structural aspects of a learning environment that Kohn (1992) theorised as afecting competitiveness align with Garcia et al.’s (2013) situational factors influencing social comparison that lead to more competitive behaviour. In terms of gamification, certain game elements are structural factors that ultimately encourage competitive behaviour.

In addition to both theories purporting structural competitiveness as influenced by the context and situation, a second area of overlap between the two theories is that both recognise individual factors associated with competitiveness. Kohn (1992) considers individual or inherent competitiveness and Garcia et al. (2013) describe individual factors associated with social comparison preceding competitive behaviour. Certain individuals are more aware of competitive opportunities compared to other individuals and, thus, respond very diferently in competitive environments. Herein, we refer to this as trait competitiveness or trait-competitive individuals.

Importantly, research on competitiveness converges to suggest that structural elements of competitiveness and trait competitiveness interact. Trait competitiveness has been shown to combine with competitive elements in the environment to produce diferent behavioural and performance outcomes (Brown et al., 1998; Fletcher & Nusbaum, 2008), and competitive individuals are more likely to perceive competitive features in the environment (Fletcher & Nusbaum, 2008). With few exceptions (e.g., Höllig et al., 2018a, 2018b; Landers et al., 2019), exploration of interactions between trait competitiveness and competitive environments is limited in gamification contexts.

Herein, we take the position that competitive game elements encourage competitive behaviour by creating opportunities and means for social comparison, and that these efects difer by individual. As presented in our model in the next section, we theorise that points and the leaderboard provide a means to compare ability and performance with others and, thus, serve as a structural competitiveness element in the environment. Furthermore, we expect that the nature of these efects on engagement and performance will depend on individual trait competitiveness.

## 3.2. Model, context, and hypotheses

We develop a research model and associated hypotheses to explain users’ game engagement and performance growth that result from users’ structural and trait competitiveness stimulated by the two distinct game elements of points and leaderboards, in the context of our natural experiment study at the Cyber Detectives exhibit at the museum. Our natural experiment setting involves one experimentallymanipulated kiosk, NetBuilder, which includes two separate treatments – points and leaderboard – compared against the five other control kiosks in the Cyber Detective exhibit (due to lack of competitive game elements in the form of points and a leaderboard). Figure 1 shows the leaderboard that was implemented at the NetBuilder. The leaderboard was implemented midway through the observation period, specifically on March 28 2016, only on the Netbuilder kiosk such that all users interacting with the NetBuilder kiosk, as well as nearby users interacting with other kiosks, could see the top scorers of NetBuilder. The top points included the daily top points as well as the weekly top points for NetBuilder. By default, the leaderboard displays the 9-digit tag ID (e.g., DWD14FZEZ), which is a unique ID assigned to a card provided to visitors entering the museum. Users have the option of customising the ID to reflect a more personalised naming (e.g., littlemissmango2006) as a display of their achievements (see Figure 1).

<table><tr><td colspan="3">TOP SCORES</td></tr><tr><td colspan="3">Today</td></tr><tr><td>Name</td><td>Score</td><td>Time</td></tr><tr><td>DWDJVCSGW</td><td>11350</td><td>3:14 PM</td></tr><tr><td>AZinzun</td><td>6197</td><td>2:05 PM</td></tr><tr><td>DWD14KVOV</td><td>6149</td><td>3:25 PM</td></tr><tr><td>Griffin Guidici</td><td>5167</td><td>4:00 PM</td></tr><tr><td>LUCASZDZ</td><td>4098</td><td>2:07 PM</td></tr><tr><td>DWD14KB5E</td><td>3980</td><td>2:07 PM</td></tr><tr><td>ander</td><td>3685</td><td>1:20 PM</td></tr><tr><td>DWD14JYF5</td><td>3559</td><td>11:34 PM</td></tr><tr><td>DWD14KB5K</td><td>3172</td><td>2:07 PM</td></tr><tr><td>DWD14KB5K</td><td>2543</td><td>12:27 PM</td></tr><tr><td>DWD14KB5E</td><td>2474</td><td>1:26 PM</td></tr><tr><td colspan="3"></td></tr><tr><td colspan="3">This Week</td></tr><tr><td>Name</td><td>Score</td><td>Time</td></tr><tr><td>H7ZOPFRDOM3</td><td>17545</td><td>Friday</td></tr><tr><td>DWD14FZEZ</td><td>17443</td><td>Friday</td></tr><tr><td>nad4han</td><td>13531</td><td>Sunday</td></tr><tr><td>DWDJVCSGW</td><td>11350</td><td>Saturday</td></tr><tr><td>littlemissmango2006</td><td>10125</td><td>Sunday</td></tr><tr><td>H7ZOPFRDONL</td><td>8485</td><td>Friday</td></tr><tr><td>H7ZOPFRDONM</td><td>6589</td><td>Friday</td></tr><tr><td>AZinzun</td><td>6197</td><td>Saturday</td></tr><tr><td>H7ZOPFRDRQB</td><td>6155</td><td>Friday</td></tr><tr><td>DWD14KVOV</td><td>6149</td><td>Saturday</td></tr><tr><td>H7ZOPFOJP4K</td><td>5706</td><td>Thursday</td></tr></table>

Figure 1. Leaderboard with daily and weekly top scores.

Figure 2 captures our 2 × 2 experimental design showing the two experimental treatments corresponding to the two game elements (points and leaderboard), each with two levels (pre- and post-implementation for leaderboard; and NetBuilder with points and control kiosks without points). Figure 2 also shows that users within each of the four quadrants are heterogeneously distributed in terms of their trait competitiveness inherent to individuals and also induced by the two game elements.

Broadly, we expect that both points and a leaderboard will encourage social comparison and subsequently trigger structural competitiveness to influence engagement and performance. Specifically, we consider how individual trait competitiveness afects the relationships between structural competitiveness stimulated by these two game elements and the two key outcomes of interest in this study – game engagement and performance growth. We expect that trait competitiveness will moderate the efects of points and leaderboards on users’ game engagement and performance. We consider two manifestations of trait competitiveness in our model: a) competitive behaviour in terms of time expenditure on games in the Cyber Detectives exhibit, and b) competitive outcome in terms of badges earned on the games in the Cyber Detectives exhibit. Time expenditure is tracked on all kiosks and badges are available at all kiosks in our study. While badges may be considered a game element that has the potential to stimulate structural competitiveness among users, this game element was available on all six kiosks in the Cyber Detectives exhibit and, accordingly, was not expected to invoke diferent levels of structural competitiveness across kiosks. Therefore, badges were not an experimental treatment in this study, and the diferent number of badges earned by diferent users captured individual diferences in their trait competitiveness.

![](/api/attachments/975EQNXG/fulltext/images/acb3eb887d13075995fc8ff77ff86a57ce7f4cdd670ce71d70a9f9f3712fffe5.jpg)  
Figure 2. Conceptual model and study design.

Engagement is conceptualised as the energy and involvement devoted to a task (Maslach & Leiter, 2008), and performance growth refers to the change in respective outcomes across successive attempts. Our model accounts for individual diferences in the extent to which users respond to the structural competitiveness invoked by the game elements of points and leaderboard. Building on research on the interactionist nature of trait competitiveness and competitive environments (e.g., Brown et al., 1998; Fletcher & Nusbaum, 2008), we expect efects attributed to points and to the leaderboard will be most salient among users who are relatively more sensitive to competitively structured environments (i.e., trait-competitive users). All hypotheses are explicated below and are displayed in Figures 3A and 3B.

## 3.3. Points, leaderboards and engagement

Our first hypothesis is that points and leaderboards are game elements that encourage social comparison and incite structural competitiveness in the environment, which results in longer periods of time per game attempt. We propose that both competitive game elements have independent and analogous efects; put diferently, we posit that both points and leaderboards will have significant efects in the same direction. Points serve as an indicator of progress (Bess, 2013), and leaderboards tend to reflect rankings based on metrics such as points. Thus, these competitive game elements are heavily intertwined yet, we argue, independent as we consider the efects of the separate game elements to be unique.

Existing research suggests that both competitive game elements in our study positively predict engagement. Points allow users to track progress which is linked to motivation (Kapp, 2012) and, when paired with other game elements such as levels and leaderboards, points are associated with engagement in formal learning environments (Cheong et al., 2013). Likewise, leaderboards have been associated with time-on-task (Landers & Landers, 2014) and have been shown to improve (i.e., decrease) the average response time between answers provided (Scales et al., 2016). Other competitive game elements have been linked to increased game time, with Liu et al. (2013) reporting that players spent more time persisting in competitive games against equally matched opponents. We consider the distinctive impact of points and leaderboards on time per attempt, and consider how both of these competitive game elements have unique, independent efects. Researchers have shown that leaderboards are associated with greater output compared to points alone (Mekler et al., 2013), yet it is not clear how these efects manifest after controlling for other competitive game elements. We hypothesise that game elements that invoke structural competitiveness, specifically the points and the leaderboard, will be associated with distinct efects resulting in significant increase in the average time spent per attempt at the kiosk.

![](/api/attachments/975EQNXG/fulltext/images/18c015e413f5403217ee0a01b54e10ec186e9049bbaa57a12d4d61bd43d44c75.jpg)  
Figure 3. A. Research model: Engagement outcomes. B. Research model: Performance growth.

At the same time, we acknowledge that a number of studies on competitive game elements report mixed efects on engagement outcomes (e.g., Costa et al., 2013; Mekler et al., 2017; Sailer et al., 2017). These mixed findings along with the literature on competitiveness, discussed earlier, suggest that game elements such as points and leaderboards may have diferent types of efects on diferent types of users, particularly users difering on trait competitiveness. This led us to explore a potential moderator of the relationship between separate competitive game elements and engagement outcomes for each set of hypotheses in our study. Again, there is evidence of interactions between individual trait competitiveness and competitive elements in the environment (Fletcher & Nusbaum, 2008) and we, accordingly, expect individual diferences in trait competitiveness to moderate the efects of structural competitiveness from game elements on users’ game engagement. Specific to our first hypothesis, we explore trait competitiveness as a moderator of the relationships between (a) points and time per attempt and (b) leaderboard and time per attempt. Thus, we propose the following two hypotheses:

## H1A (Structural Competitiveness Hypothesis):

The time per attempt is higher for users who interact with the experimental kiosk that awards points and has a leaderboard, compared to users who interact with control kiosks.

## H1B (Trait Competitiveness Hypothesis):

The higher time per attempt for users who interact with the experimental kiosk is even higher for traitcompetitive users, compared to non-trait-competitive users.

Based on our hypothesis that time spent per attempt will increase across all users (H1A) and even more among trait-competitive users (H1B), we argue that game reattempts for users will decrease as a result. We posit that if the amount of time per attempt in kiosks with points and/or leaderboards is greater than that in other kiosks as outlined in our first hypothesis, time extensions via additional attempts will become less necessary.

One potential reason for this is that users will be more likely to satiate the need to win and/or improve in fewer attempts, given that each attempt is longer. According to Franken and Brown (1995), competition (in this case, competitive game elements) may allow individuals to satisfy the need to win. If we assume that users spending more time per attempt at the gamified kiosk are consequently meeting this need with the additional time per attempt, this need to win will be satisfied in fewer attempts. Another potential reason suggesting additional attempts may be less necessary is that individuals will likely exert sustained focus and energy across each attempt due to the longer amount of time per attempt, as put forth in H1A, which may lead to eventual fatigue and, thus, make subsequent efortful attempts less likely (Ackerman et al., 2010).

Furthermore, building of our expectation that trait-competitive users are likely to be even more persistent on the experimentally-manipulated kiosk as compared to the control kiosks, as articulated in H1B, we likewise believe that users will make even fewer reattempts on the experimentally-manipulated kiosk relative to non-trait-competitive users. Again, competition is more motivating to certain individuals (i.e., trait-competitive users), meaning that the need to win and the threshold for satisfying this need is greater in some compared to others (Franken & Brown, 1995). Given our expectation that trait-competitive users will spend significantly more time per attempt at the gamified kiosk relative to time spent at other kiosks, as proposed in H1B, we hypothesise that traitcompetitive users will demonstrate even fewer reattempts at the experimentally-manipulated kiosk than among non-trait-competitive users. Accordingly, we propose the following two hypotheses:

## H2A (Structural Competitiveness Hypothesis):

The number of reattempts is lower for users who interact with the experimental kiosk that awards points and has a leaderboard, compared to users who interact with control kiosks.

## H2B (Trait Competitiveness Hypothesis):

The lower number of reattempts for users who interact with the experimentalkiosk is even lower for traitcompetitive users, compared to non-trait-competitive users.

Next, we explore the impacts on another form of engagement, i.e., the number of attempts among unique daily kiosk users. We expect both points and leaderboards to encourage social comparison and trigger structural competitiveness, which will be associated with fewer attempts among unique users at the experimental kiosk because the experimental kiosk will attract trait-competitive users and, at the same time, deter non-trait-competitive users. Again, we build of our expectation that points and leaderboards will result in longer periods of interaction time (i.e., H1A) particularly among trait-competitive users (i.e., H1B), and argue that this will yield even fewer opportunities for broader constituency of users to participate in games at the experimental kiosk.<sup>4</sup>

We expect the average number of attempts among unique users to be lower at the experimental kiosk for two potential reasons, the first of which is selfselection. Humans tend to select into environments that aford high status through competitive behaviour and wherein attainment of high status is most probable or likely (Anderson et al., 2015). As noted in our theoretical framework, according to social comparison theory (Festinger, 1954; Latané, 1966), humans tend to make upward self-comparisons (i.e., comparison against a “better of” other) when seeking self-improvement and tend to make downward selfcomparisons (i.e., comparison against a “worse of” other) when motivated by self-enhancement (Buunk et al., 1991; Wills, 1981). Accordingly, this means that some individuals will select out of environments particularly those wherein competition is intimidating or social comparison makes the user feel or appear incompetent relative to the others. Using this logic, the competitive game elements at the experimentallymanipulated kiosk may signal to certain users that the outcomes of social comparison may be unfavourable and subsequently dissuade these users from attempting games on that kiosk. In other words, certain users may withdraw from the experimentally-manipulated kiosk due to feelings of incompetency or intimidation (Johnson & Johnson, 1975) or fear of attracting attention to themselves. As such, just as we expect certain users to be attracted to the experimentallymanipulated kiosk due to the points and leaderboard, we likewise expect that certain users will be less likely to enter.

Another reason we expect the average number of daily unique attempts to be lower at the experimentally-manipulated kiosk as compared to that of the control kiosks is due to the hypothesised composition of users. As stated in H1B, we expect that traitcompetitive users will engage on the experimentallymanipulated kiosk for significantly longer periods of time per attempt. There are a limited number of spots at the experimentally-manipulated kiosk, and we expect that trait-competitive users will occupy these spots to such an extent that there will be less opportunity for other users to engage with the kiosk. The expectation that trait-competitive users will dominate the gamified kiosk coincides with the dominance path to social status in competitive environments (Cheng & Tracy, 2014) with status-dominant individuals characterised as those who use aggressive, controlling, and authoritative means to ascend social status hierarchies (Cheng et al., 2010).

Altogether, we expect the trait-competitive users to dominate the experimentally-manipulated kiosk to such an extent that there will be less opportunity overall for any user to engage on that kiosk. Accordingly, we posit that the number of unique users will be lower at the experimentally-manipulated kiosk compared to other kiosks. Furthermore, building of our preceding hypotheses regarding moderation by traitcompetitiveness, we posit that the proportion of traitcompetitive users relative to all users will be higher on the experimentally-manipulated kiosk. Therefore, we proposed the following two hypotheses:

## H3A (Structural Competitiveness Hypothesis):

The number of attempts by unique daily users is lower on the experimental kiosk that awards points and has a leaderboard compared to the control kiosks.

H3B (Trait Competitiveness Hypothesis):

The proportion of trait-competitive users relative to number of unique daily user attempts is higher on the experimental kiosk compared to the proportion of trait-competitive users on control kiosks.

## 3.4. Leaderboards and performance growth

In our final hypothesis, we focus completely on the experimentally-manipulated kiosk to consider how the leaderboard, as a competitive game element in afecting structural competitiveness, influences users’ performance growth pattern. The experimentally-manipulated kiosk is the only kiosk ofering points, so in our fourth hypotheses set, we compare the individual growth pattern in points before and after the leaderboard implementation. Overall, we expect the post-leaderboard time period at the experimentally-manipulated kiosk to be associated with a curvilinear growth pattern in points earned at each reattempt, specifically an inverted-U growth pattern. Drawing on work by Haans et al. (2016), we consider the specific aspects of this relationship as the net efect of two separate functions of time and performance.

First, we posit that once the leaderboard is introduced, users will be motivated to establish a high ranking on the leaderboard, which has a positive efect on performance that increases at a decreasing rate (i.e., logarithmic function). Growth between attempts will be larger at first as users initially make gains in points between attempts; however gains in points become smaller and smaller as users continue making more attempts at the kiosk. The decrease in growth may be attributed to exposure (Palaus et al., 2017) or because users withdraw efort after several attempts due to mismatched challenge (i.e., too easy or too dificult). Assuming that users are indeed drawn to the gamified kiosk in the postleaderboard time period because of the potential to attain a public rank on the leaderboard, there is an ultimate ceiling on performance growth in this context because this source of motivation may disappear once this need is satiated. Accordingly, the growth in performance over successive attempts eventually flattens.

Second, we posit that users’ rising sense of competitiveness imposes a cost on individual game players that likely negatively afects game performance over successive attempts. Further, the cost from competitiveness increases across attempts in an exponential manner; the higher the points one achieves, the more stif the competition. Successive gameplay with initial increase in points likely results in increased levels of stress hormones (e.g., higher testosterone, adrenaline) which are typically associated with higher performance in status-based environments (Mazur et al., 1992) However, high levels of stress hormones, in this case induced by increasing competitiveness, may also impose costs and interfere with performance. For example, there is research to suggest that testosterone can encourage users to withdrawal or submit from a game when status is dropping (Inoue et al., 2017) and that increased adrenaline can inhibit cognitive performance (Henderson et al., 2012). Thus, users experience stress hormones from the leaderboard competition, which compound over attempts and eventually negatively afect performance.

Altogether, the combination of these two efects (i.e., the logarithmic and exponential) results in an inverted-U trend, as discussed in Haans et al. (2016). The curvilinear relationship between a stimulus of structural competitiveness (in this case, the leaderboard) and output performance afected by competition (in this case, performance in terms of point on reattempts) is often referred to as the inverted-U hypothesis by Yerkes and Dodson (1908), which has been used in psychology (Teigen, 1994) and information systems (Wang et al., 2009) literatures.

As the first part of our fourth hypothesis, we posit that this inverted-U pattern will not be present in the preleaderboard time period and this pattern will emerge in the post-leaderboard time period. We further posit that the inverted-U pattern in the post-leaderboard time period will be attributed to trait-competitive users. Again, following the previous line of argument as for H1B and H2B, we propose that trait-competitive users will be most sensitive to the leaderboard stimulus and we expect efects on performance growth, specifically the inverted-U pattern, to be most prominent in trait-competitive users compared to non-trait competitive users. Therefore, we propose the following two hypotheses:

## H4A: (Structural Competitiveness Hypothesis):

Users who interact with the experimental kiosk that awards points and has a leaderboard will exhibit an inverted-U pattern between their successive reattempts on the kiosk and their performance growth in points in the post-leaderboard period while users who interact with the experimental kiosk in the pre-leaderboard period will not exhibit such a curvilinear pattern in performance growth.

## H4B: (Trait Competitiveness Hypothesis):

The inverted-U pattern between users’ successive reattempts on the experimental kiosk and their performance growth in points in the post-leaderboard period will be stronger among trait-competitive users compared to non-trait-competitive users.

## 4. Methods

## 4.1. Study context and data

Data for this study were collected at the Tech Interactive (formerly The Tech Museum of Innovation) in

California, which is a technology innovation centre that provides a range of highly interactive exhibit experiences to over half a million visitors per year. Certain exhibits in the museum capture unique visitor and location information using a unique RFID-enabled ID card that is provided to each visitor upon entry to the Tech Interactive. The exhibit that we studied was Cyber Detectives sponsored by Palo Alto Networks. There were six kiosks in the Cyber Detectives exhibit and one of those kiosks called NetBuilder had two distinct game elements that are associated with inducing structural competitiveness among users. Specifically, NetBuilder was the only kiosk to award points to users, and it was the only kiosk in the museum that had a leaderboard installed midway through our data collection period. Our data set includes each museum user’s individual game interaction-level data and represents 215,920 distinct game attempt observations made by 88,310 distinct users over a period of 300 days on the six Cyber Detectives kiosks at the museum. All data were collected between November 1 2015 and August 28 2016.

As a result, we were able to conduct a natural experiment setting with a 2 × 2 factorial design with four cells, see Figure 2. Specifically, the first factor in this study design is leaderboard as a game element, and it is shown as horizontal axis in Figure 2. The leaderboard was implemented midway through the observation period, specifically on March 28 2016, only on the Netbuilder kiosk such that all users interacting with the NetBuilder kiosk, as well as nearby users interacting with other kiosks, could see the top points of the NetBuilder kiosk. The leaderboard displayed points each time the user completed a gaming session, and the top points included the daily top points as well as the weekly top points for NetBuilder (see Figure 1). This allowed us to study the efect of structural competitiveness induced among users by the game element of a leaderboard in an experimental setting, with the two levels of this factor representing “No” for leaderboard (i.e., preleaderboard) and “Yes” for leaderboard (i.e., postleaderboard implementation), respectively. The second factor in our study is performance-based points (or points) ofered on only one of the kiosks in the museum – the Netbuilder kiosk, as shown on the vertical axis in Figure 2. This allowed us to study the efect of structural competitiveness induced among users by another game element of performance-based points awarded to game users in an experimental setting, with the two levels of this factor representing “Yes” for performance-based points (Netbuilder kiosk) and “No” for performance-based points (the remaining five control kiosks), respectively.

Overall, the setting and conditions allowed us to examine the efects of both structural competitiveness and trait competitiveness in relation to both engagement and performance outcomes in a natural setting while maintaining experimental controls. This type of natural experiment is widely adopted in psychology and economics (Dunning, 2012), and considered to be most efective in studying real life behaviours as it may be dificult to replicate the necessary experimental conditions in a laboratory setting, or the participants’ awareness of being studied may have confounding efects on the outcome (Meyer, 1995). Competitive behaviours and resulting outcomes in gaming contexts are susceptible to contextual factors often found in prior studies (e.g., employees of an organisation, students enrolled in a class), and our natural experimental setting for data collection minimises such potential confounding efects.

We transformed each of the outcomes with the natural log, standardised this points, and filtered out values that exceeded ± 3SD, as these were outliers. We performed our analysis regressing on the raw outcome variables, however our findings were robust with regard to the regression on the transformed variables. As users go through the facility, they interact with multiple kiosks within a single day, and this led to our decision to examine both interaction-level and user-level models.

To mitigate issues associated with internal validity threats typically associated with natural experiments, we considered potential exogenous variables (Campbell, 1957). Due to the complex nature of the data, we addressed this potential problem in several ways. First, we made sure that there were no major diferences or external changes occurring in the exhibit during the observational period, other than the addition of the leaderboard to the NetBuilder kiosk; this condition was verified by the museum staf and managers. Second, we took additional measures to ensure that the data were representative of a museumgoing population. The experiment was carried out over a long period of time (10 months), and the visitors to the informal learning facility change daily and rarely return within 12 months. We obtained records of RFIDs that were associated with employees and filtered out these observations because these individuals were not part of the experimental sample.

## 5. Samples and measures

## 5.1. Dependent variable: engagement outcomes

We used three separate units of analysis for the diferent outcomes in our engagement models. For estimating seconds per attempt as a measure of user engagement, we modelled at the level of each user interaction (N = 215,920 observations). For estimating the number of reattempts as a measure of user engagement, we modelled at the level of the user (N = 56,267 observations), which included all users who had attempted any of the kiosks more than one time. For estimating the number of unique daily user attempts as a measure of user engagement, we modelled at the level of the day (N = 300 days of unique user attempts for treatment and control kiosks). Correlations and descriptive statistics pertaining to these diferent aggregated datasets are provided in Table 2A – 2D.

## 5.2. Dependent variable: performance growth (points)

Performance-based points, or points, were only available on the NetBuilder kiosk, and we examined within-individual growth in points at NetBuilder pre- and post-leaderboard implementation. For H4A, we examined all individuals who attempted NetBuilder at least three times in November and December of 2015 (i.e., pre-leaderboard) and compared performance with all individuals who attempted NetBuilder at least three times in the months of April and May of 2016 (i.e., post-leaderboard).<sup>5</sup> This sample was 390 individuals with 1,381 observations total. In order to appropriately model growth, at least three observations are necessary (Andruf et al., 2009). The sample for post-leaderboard growth (H4B) consisted of 165 users with 580 observations total.

## 5.3. Independent variables: structural competitiveness (points and leaderboard)

There were two separate game elements associated with structural competitiveness in our study, as described above. The first factor is related to performance-based points, which is associated with the NetBuilder kiosk (where 0 = non-NetBuilder, 1 = NetBuilder). The second factor is related to the leaderboard, which was only installed at NetBuilder in the latter part of the observation period (where 0 = pre-leaderboard, 1 = post-leaderboard).

## 5.4. Moderator: trait competitiveness

Prior literature has shown that individuals who are competitive are more willing to expend time and energy in pursuit of skills and achievements (e.g., Kilduf et al., 2012; Shepard, 1954; Sutton & Hargadon, 1996). Our data from this natural experiment allowed us to compile two indicators of trait competitiveness, including: a) trait-competitiveness as a behaviour measured as the total time spent by a user on all the games played in the museum in a single visit; and b) trait competitiveness as an outcome measured as the total number of badges earned by a user on all the games played in the museum in a single visit. Then, we calculated the median $( 5 0 ^ { \mathrm { t h } }$ percentile) of these values across all users in our data set, and created dummy variables to indicate whether a user was above the median $( 0 = n o , 1 = y e s )$ for total time expenditure and for badges earned. The use of the median has been used by other IS researchers to explore groups identified at “high” and “low” levels (e.g., Mitra & Chaya, 1996). It made no diference in group designation by being above the median (as opposed to being at or above the median split) for total time spent as it remained an approximate equal (i.e., 50–50) split. This choice did, however, make a diference for badges earned, as using above the median resulted in only 20% (see Table 2A) and 32% (see Table 2B) of the observations being attributed to trait-competitive users. Thus, we operationalise expression of trait competitiveness in two distinct ways: total time expenditure, which captures traitcompetitive behaviour and where higher levels are attributed to approximately half of the observations, and badges earned, which refers to trait-competitive outcome and where higher levels are attributed to 30% or fewer observations.

## 5.5. Analytical models

For testing H1 – H3 (i.e., engagement outcomes in our natural experiment), we used Diferences-in-Diferences (DD) models to test the two-way interactions between NetBuilder and post-leaderboard time period, and Diferences-in- Diferences-in-Diferences (DDD) models to test the three-way interactions between NetBuilder and non-NetBuilder games, preand post-leaderboard, and trait-competitiveness (Angrist & Pischke, 2008). The DD and DDD models were estimated in SPSS (IBM 2016) using OLS regression models. This approach allowed us to test the isolated efects of both the points (as a main efect) and the leaderboard (as a two-way interaction) as well as the moderation by trait competitiveness.<sup>6</sup>

## 5.6. Engagement outcomes

## 5.6.1. Main efects of structural competitiveness (i.e., points and leaderboard)

In order to estimate causal efects of the points and the leaderboard implementation on engagement outcomes (i.e., H1A, H2A, H3A), we apply the DD estimation method to examine the extent to which the diferences between the NetBuilder kiosk and the control kiosks was diferent overall and whether this difference changed after the leaderboard was added to NetBuilder:

$$
Y = \beta_ {0} + \beta_ {1} L + \beta_ {2} K + \delta_ {1} L K + \beta_ {3} C + \epsilon
$$

where

Y = outcome (time per attempt, reattempts, unique users)

$$
L = \text { Leaderboard   implementation }
$$

$$
K = \mathrm{NetBuilderKiosk}
$$

$$
C = \text { Museum   attendance   (control) }
$$

We note that the betas in the equations represent the intercept (β0) and the main efects regression weights (e.g., β1), and the delta (δ1) represents the regression coeficient associated with the two-way interaction.

5.6.2. Moderation efects by trait competitiveness In comparing the extent to which trait competitiveness moderated the diferences between kiosks as a result of the NetBuilder implementation (i.e., H1B, H2B, H3B), we used DDD estimation methods:

$$
\begin{array}{c} Y = \beta_ {0} + \beta_ {1} L + \beta_ {2} K + \beta_ {3} S + \gamma_ {1} L K + \gamma_ {2} L S + \gamma_ {3} S K \\ + \delta_ {1} L K S + \beta_ {3} C + \epsilon \end{array}
$$

where

Y = outcome (time per attempt, reattempts, unique users)

L = Leaderboard implementation

K = NetBuilder Kiosk

S = Trait competitiveness

C = Museum attendance (control)

The betas in the equations represent the intercept $( \beta _ { 0 } )$ and the main efects regression weights $( \mathsf { e } . \mathsf { g } . , \mathsf { \beta } _ { 1 } ) ,$ the gammas $( \mathrm { e } . \mathrm { g } . , \gamma _ { 1 } )$ represent the regression weights associated with the two-way interactions, and the delta $( \delta _ { 1 } )$ represents the regression weight associated with the three-way interaction.

## 5.7. Performance growth

For testing H4, we used panel data models with fixed efects (FE) (Baum et al., 2003). The sample for this hypothesis is limited to all users who played at least three times on the NetBuilder kiosk, as this was the only kiosk that captured and displayed game points. For testing H4A, we estimated two separate FE models to assess the impact of successive game attempts of individual users on their game performance points, one for the pre-leaderboard period and the other for the post-leaderboard period.

For testing H4B, we estimated two separate FE models to assess the impact of successive game attempts of individual users on their game performance points, one for the trait-competitive users and the other for the non-trait-competitive users, both in the post-leaderboard period. FE models allow us to control for any unobserved fixed efects of individual users (e.g., their individual game ability and prowess) over successive game attempts on their game performance. Each FE model in this set of analyses uses a diferent panel (i.e., sample) of users. Specifically, users in the pre-leaderboard period are not the same as those in the post-leaderboard period. Similarly, the panel of trait-competitive users is diferent from the panel of non-trait-competitive users. Moreover, all panels are unbalanced panels because not every user had the same number of game attempts. Accordingly, we used unbalanced fixed efects models and clustered by user ID to control for the unobserved individual efects. For testing H4B, we estimated two separate FE models because trait-competitiveness is fixed for an individual user and cannot be used as a moderator in our FE models as it will be eliminated as a fixed efect. For each of these comparisons, we built a quadratic fixed efects model for the respective panel<sup>7</sup>:

$$
\begin{array}{c} Y = \beta_ {0} + \beta_ {1} A t t e m p t _ {i t} + \beta_ {2} A t t e m p t ^ {2} _ {i t} + \beta_ {3} S e c o n d s _ {i t} \\ + \mu_ {i} + e _ {i t} \end{array}
$$

where

Attempt<sub>it</sub> = attempt of person i at time t

Attempt<sup>2</sup> = attempt of person i at time t squared

Seconds<sub>it</sub> = number of seconds from the prior attempt

μ<sub>i</sub> = unobserved individual efect (fixed efect)

e = error associated with person i at time t

## 6. Results

## 6.1. Engagement outcomes

Points and the leaderboard, as separate game elements triggering structural competitiveness, were associated with more seconds per attempt, and our results supported Hypothesis 1A. There were significant diferences in the seconds per attempt between NetBuilder and the other kiosks, with NetBuilder associated with 206.02 additional seconds per attempt compared to that of other kiosks (B = 206.02, t = 168.4, p <.001). This suggests that users spent more time at NetBuilder overall, which we attributed to the points game element invoking structural competitiveness. Results also suggested that the diferences between kiosks were even bigger after the implementation of the leaderboard. Compared to the pre-post changes in the non-NetBuilder kiosks, there was a significant increase in seconds spent per attempt at NetBuilder after the leaderboard was implemented, B = 57.7, t = 23.6, p < .001 (see Model 1 in Table 3).

Results also supported H1B. As shown in Models 2A and 2B in Table 3, trait-competitive users of the NetBuilder game spent significantly more time at NetBuilder compared to the other kiosks. Findings were consistent with trait-competitiveness defined in terms of total time expenditure, $B \ = \ 2 3 5 . 5 ,$ t = 97.6, p < .001 (Model 2A, Table 3), and badges, B = 133.5, t = 37.7, p < .001 (Model 2B, Table 3). In the post-leaderboard period, trait-competitive users spent significantly more time per attempt compared to non-trait-competitive users of NetBuilder in the same period. Findings were consistent for traitcompetitiveness defined in terms of users being above the median for time invested, $B ~ = ~ 9 4 . 1$ $t = 1 9 . 7 , \ : p < . 0 0 1$ (see Model 2A, Table 3), and in terms of users being above the median badges earned, B = 28.9, t = 5.7, p < .001 (see Model 2B,

Table 1. Description of variables.

<table><tr><td>Tech Tag ID</td><td>This variable represents the unique ID of a particular user on a particular day at the museum. Upon entry to the facility, users are given tags with RFID chips. Each of these tags has a unique identifier allowing the user to be tracked across space and time in the museum.</td></tr><tr><td>Interaction ID</td><td>This variable represents the unique interaction ID of a particular user on a particular kiosk of the Cyber Detectives exhibit at the museum on a particular day. Each kiosk in the exhibit captures for each interaction a unique interaction ID that is associated with the user involved in the interaction, the kiosk, and has a time stamp for the start and stop time of the interaction of the user on that kiosk.</td></tr><tr><td>Day</td><td>This variable represents the number of days lapsed in our observation period and ranges from 1 (on November 1 2015) to 300 (on August 28 2016). There were two observed holidays in this period: November 26 2015 (Thanksgiving) and December 25 2015 (Christmas) where the informal learning facility was closed so these dates did not receive values. Our data set includes a total of 300 days worth of data excluding these holidays.</td></tr><tr><td>Daily attendance</td><td>This variable represents the total number of unique Tech Tag IDs captured on all the kiosks in the Cyber Detective exhibit on a particular day.</td></tr><tr><td>Kiosk Type</td><td>This variable represents whether a kiosk on which an interaction took place was the NetBuilder kiosk or not, and was coded as a dummy variable such that NetBuilder kiosk = 1; and Other Kiosks = 0.</td></tr><tr><td>Leaderboard Implementation</td><td>This variable represents whether the leaderboard had been implemented on the NetBuilder kiosk when a particular interaction on that kiosk took place. This variable was coded as a dummy variable such that Pre-leaderboard period = 0 and Post-leaderboard period = 1.</td></tr><tr><td>Trait-Competitiveness (Time-Based)(Subscripts: T for time-based measure; AK for All Kiosks; and NB for NetBuilder Kiosk)</td><td> $TC_{T-AK}$  This variable designates a user as a trait competitive user if s/he was in the  $50^{th}$  percentile and above for total time spent on all kiosks; calculated using all users in Quadrants I, II, III, and IV in Figure 2. $TC_{T-NB}$  This variable designates a user as a trait competitive user if s/he was in the  $50^{th}$  percentile and above for total time spent on the NetBuilder kiosk; calculated using all users in Quadrants III and IV in Figure 2 who attempted at least three times.</td></tr><tr><td>Trait Competitiveness (Badge-Based)(Subscripts: B for badge-based measure; AK for All Kiosks; and NB for NetBuilder Kiosk)</td><td> $TC_{B-AK}$  This variable designates a user as a trait competitive user if s/he was in the  $50^{th}$  percentile and above for total number of badges earned on all kiosks; calculated using all users in Quadrants I, II, III, and IV in Figure 2. $TC_{B-NB}$  This variable designates a user as a trait competitive user if s/he was in the  $50^{th}$  percentile and above for total badges earned on the NetBuilder kiosk; calculated among users in Quadrants III and IV in Figure 2 who attempted at least three times.</td></tr><tr><td>Time Spent per attempt</td><td>This variable represents the time a user spent on a particular interaction at a particular kiosk. A user can have multiple observations for this variable, each pertaining to the multiple interactions of the user on the same kiosk. A user can also have multiple observations for this variable, each pertaining to interactions of the user on different kiosks in the museum. Time was captured by day and time (hour/minute/seconds). Start time and stop time were recorded by each kiosk using Tech Tag and Interaction IDs for each user for each interaction. Time spent per attempt was calculated by subtracting the stop time from the start time for that interaction and is represented in terms of seconds.</td></tr><tr><td>Number of Reattempts by a User at a Kiosk</td><td>This variable represents the number of reattempts of a user at a particular kiosk. A user can have multiple observations for this variable, each pertaining to interactions of the user on different kiosks in the museum. The value of this variable for a particular user on a particular kiosk will be zero if s/he made only one game interaction on that kiosk.</td></tr><tr><td>Number of Unique Daily User Attempts at a Kiosk</td><td>This variable represents the number of attempts among unique users who interacted with a particular kiosk on a particular as captured by unique Tech Tag and Interaction IDs recorded at the kiosk that day.</td></tr><tr><td>Proportion of Unique Daily User Attempts who are Trait-Competitive</td><td>This variable represents the proportion of the number of attempts among unique daily users at a kiosk who are designated as Trait Competitive (using either  $TC_T$  and  $TC_B$  indicators, see above) relative to the total number of unique daily users at that kiosk. Unique users were identified using the Tech Tag IDs recorded at a kiosk on a particular day.</td></tr><tr><td>Attempt #Performance</td><td>This variable represents the  $i^{th}$  interaction of user j on the NetBuilder kiosk.This variable represents the points received by a user j on his/her  $i^{th}$  attempt on the NetBuilder kiosk.</td></tr></table>

Table 3). The interactions are modelled in Figure $\mathrm { 4 A - 4 D }$

As shown in Table 4, results also supported Hypotheses 2A and 2B. According to Model 3 Table 4, NetBuilder had significantly fewer reattempts compared to the other kiosks, $B = - . 5 4 , t = - 2 3 . 8 , p < . 0 0 1$ , which we attribute to the points game element. There was a significant decrease in the number of reattempts in NetBuilder after the leaderboard was implemented, $B ~ = ~ - . 1 , ~ t ~ = ~ - 2 . 2 , ~ p ~ < ~ . 0 5$ , and we attribute these diferences to the leaderboard implementation. According to Models 4A and 4B in Table 4, the interactions between structural competitiveness and trait competitiveness were as hypothesised. In terms of the efects of structural competitiveness triggered by points, the number of reattempts at NetBuilder compared to that of the other kiosks was much lower among trait-competitive users. The between-kiosk differences in reattempts attributed to points were magnified among individuals above the median for total time investment $( B = - 1 . 5 , t = - 2 7 . 8 , p < . 0 0 1 )$ and among individuals above the median for badges earned $( B = - . 9 , t = - 1 4 . 8 , p < . 0 0 1 )$

In terms of how trait competitiveness moderated the efects of structural competitiveness triggered by the leaderboard, findings also suggested that efects were more salient among trait-competitive users. Users who were above the median for total time investment were associated with significantly fewer reattempts at NetBuilder in the post-leaderboard time period $( B = - . 4 , t = - 4 . 7 , p < . 0 0 1 )$ and users who were above the median for badges earned were associated with fewer reattempts at NetBuilder in the post-leaderboard time period $( B = - . 2 , t = - 1 . 7 , p < . 0 5 )$

Table 2A. Descriptive statistics for H1A and H1B sub-sample; $\mathsf { N } = 2 1 5 , 9 2 0$ obs.(all interactions on all kiosks of all users on all days).

<table><tr><td colspan="2"></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Trait Competitiveness (Time-based)</td><td>.5</td><td>.5</td><td>0</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Trait Competitiveness (Badge-based)</td><td>.20</td><td>.40</td><td>0</td><td>1</td><td>.46***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Time Spent Per Attempt</td><td>206.62</td><td>223.62</td><td>6</td><td>3127</td><td>.24***</td><td>.05***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>4</td><td>NetBuilder Kiosk (Yes = 1; No = 0)</td><td>.16</td><td>.37</td><td>0</td><td>1</td><td>.10***</td><td>.01***</td><td>.34***</td><td>1</td><td></td><td></td></tr><tr><td>5</td><td>Daily Attendance</td><td>992.63</td><td>244.35</td><td>213</td><td>1607</td><td>-.01***</td><td>.04***</td><td>-.00</td><td>-.04***</td><td>1</td><td></td></tr><tr><td>6</td><td>Leaderboard Implemented (Yes = 1; No = 0)</td><td>.51</td><td>.50</td><td>0</td><td>1</td><td>-.05***</td><td>.02***</td><td>-.01***</td><td>-.02*</td><td>.07***</td><td>1</td></tr></table>

Table 2B. Descriptive Statistics for H2A and H2B sub-sample; $\mathsf { N } = 5 6 , 2 6 7$ obs. (interactions on all kiosks but only of users whose number of reattempts on a particular kiosk > 0).

<table><tr><td colspan="2"></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Trait Competitiveness (Time-based)</td><td>.41</td><td>.49</td><td>0</td><td>1</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Trait Competitiveness (Badge-based)</td><td>.32</td><td>.47</td><td>0</td><td>1</td><td>.35***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Number of Reattempts</td><td>3.49</td><td>1.98</td><td>2</td><td>13</td><td>.33***</td><td>.32***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>4</td><td>NetBuilder Kiosk (Yes = 1; No = 0)</td><td>.20</td><td>.25</td><td>0</td><td>1</td><td>.14***</td><td>.09***</td><td>-.10***</td><td>1</td><td></td><td></td></tr><tr><td>5</td><td>Daily Attendance</td><td>991.74</td><td>242.9</td><td>213</td><td>1607</td><td>-.03***</td><td>.04***</td><td>.01**</td><td>-.03***</td><td>1</td><td></td></tr><tr><td>6</td><td>Leaderboard Implemented (Yes = 1; No = 0)</td><td>.53</td><td>.499</td><td>0</td><td>1</td><td>-.06***</td><td>.01**</td><td>.00</td><td>-.03***</td><td>.09***</td><td>1</td></tr></table>

Table 2C. Descriptive statistics for H3A and H3B sub-sample; N = 600 obs. (aggregated observations for unique daily users for experimental and control kiosks).

<table><tr><td colspan="2"></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1</td><td>Number of Unique Daily Users at a Kiosk</td><td>374.96</td><td>274.2</td><td>28</td><td>1156</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Proportion of Unique Daily Users at a Kiosk who are Trait Competitive Users (Time-based)</td><td>.7620</td><td>.092</td><td>.45</td><td>.98</td><td>-.51***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Proportion of Unique Daily Users at a Kiosk who are Trait Competitive Users (Badge-based)</td><td>.38</td><td>.11</td><td>.09</td><td>.78</td><td>-.06</td><td>.66*</td><td>1</td><td></td><td></td><td></td></tr><tr><td>4</td><td>Daily Attendance</td><td>926.99</td><td>251.44</td><td>213</td><td>1607</td><td>.36***</td><td>-.06</td><td>.15***</td><td>1</td><td></td><td></td></tr><tr><td>5</td><td>NetBuilder Kiosk (Yes = 1; No = 0)</td><td>.50</td><td>50</td><td>0</td><td>1</td><td>-.88***</td><td>.55***</td><td>.11**</td><td>.00</td><td>1</td><td></td></tr><tr><td>6</td><td>Leaderboard Implemented (Yes = 1; No = 0)</td><td>.51</td><td>.50</td><td>0</td><td>1</td><td>-.01</td><td>-.07</td><td>.06</td><td>.13***</td><td>.00</td><td>1</td></tr></table>

Table 2D. Descriptive statistics for H4A and H4B sub-sample; N = 1381 obs. (interactions only for four months and only on the experimental, i.e., netbuilder, kiosk and only for users whose number of attempts on the experimental kiosk ≥ 3).

<table><tr><td colspan="2"></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr><tr><td>1</td><td>Performance</td><td>963.40</td><td>2685.48</td><td>2</td><td>43,674</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>Time Spent Per Attempt</td><td>361.83</td><td>426.60</td><td>1</td><td>3367</td><td>.46***</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>Number of Attempts</td><td>2.42</td><td>1.33</td><td>1</td><td>12</td><td>.10***</td><td>.01</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>4</td><td>Number of  $Attempts^2$ </td><td>7.64</td><td>9.81</td><td>1</td><td>144</td><td>.06***</td><td>.01</td><td>.92***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>5</td><td>Leaderboard Implemented (Yes = 1; No = 0)</td><td>.42</td><td>.49</td><td>0</td><td>1</td><td>.09***</td><td>.04</td><td>-.004</td><td>.03</td><td>1</td><td></td><td></td></tr><tr><td>6</td><td>Trait-Competitiveness (Time-Based)</td><td>.55</td><td>.50</td><td>0</td><td>1</td><td>.20***</td><td>.31***</td><td>.18***</td><td>.14***</td><td>-.04</td><td>1</td><td></td></tr><tr><td>7</td><td>Trait Competitiveness (Badge-Based)</td><td>.74</td><td>.44</td><td>0</td><td>1</td><td>.15***</td><td>.22***</td><td>.10***</td><td>.10***</td><td>.01</td><td>.49***</td><td>1</td></tr></table>

Hypothesis 3A was fully supported and Hypothesis 3B was partially supported (see Table 5). Overall, NetBuilder was associated with fewer unique users, $( B = - 4 7 1 . 0 , t = - 4 9 . 7 , p < . 0 0 1 )$ and there was a significant decrease in unique user attempts at NetBuilder in the post-leaderboard period compared to pre-post changes in the non-NetBuilder kiosks $( B ~ = ~ - 2 5 . 2 , ~ t ~ = ~ - 1 . 9 , ~ p ~ < ~ . 0 5 )$ These findings supported Hypothesis 3A. Turning to Hypothesis 3B, we determined that the percentage of trait-competitive users, as defined in terms of being above the median total time spent on all kiosks, was significantly greater at NetBuilder compared to non-NetBuilder games $\begin{array} { r l r } { ( B } & { { } = } & { . 0 8 . } \end{array}$ $t ~ = ~ 9 . 4 , ~ p ~ < ~ . 0 0 1 )$ , and this was even greater at

NetBuilder in the post-leaderboard time period $( B = . 0 3 , t = 2 . 6 , p < . 0 1 )$ . However, operationalisation of trait competitiveness in terms of above median number of badges did not yield the same results for the points game element $( B \ = \ . 0 1 _ { \mathrm { : } }$ $t = . 7 8 , \ p > . 1 )$ or the leaderboard game element $( B ~ = ~ . 0 3 , ~ t ~ = ~ 1 . 6 , ~ p ~ < ~ . 1 )$ . We conclude these findings partially support H3B. The interactions are shown in Figure 5A – 5D.

## 6.2. Performance growth

Turning to the efects of the leaderboard on performance growth outcomes, both Hypotheses 4A Tables 6 and 4B, Tables 7 and 8 were supported. In the NetBuilder game, across all users there was evidence of an inverted-U pattern in within-person performance in the postleaderboard time period, as shown by the negative coefficient associated with Attempt<sup>2</sup> $( B = - 7 5 . 3 9 , \ t = 2 . 4 ,$ p < .05) (see Model 7B in Table 6). After a leaderboard was introduced to the NetBuilder kiosk, users’ successive performance steadily improved until a certain point, then levelled of and declined. The inverted-U pattern for was not evident, however, among all NetBuilder users in the pre-leaderboard period, as the coeficient associated with Attempt<sup>2</sup> was not statistically significant (see Model 7A in Table 6). Thus, Hypothesis 4A is supported.

Table 
3. Tests of H1 – DD and DDD estimation; N = 215,920 obs.

<table><tr><td rowspan="2">DV: Time SpentPerAttempt</td><td colspan="6">Model 1 (H1A)</td><td colspan="8">Model 2A (H1B)Trait Competitiveness based on Time</td><td colspan="8">Model 2B (H1B)Trait Competitiveness based on Badges</td><td></td><td></td></tr><tr><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Constant</td><td>163.13</td><td>1.94</td><td>83.92***</td><td>163.11</td><td>1.94</td><td>84.02***</td><td>117.67</td><td>1.95</td><td>60.32***</td><td>117.87</td><td>1.95</td><td>60.49***</td><td>139.6</td><td>2.0</td><td>71.19***</td><td>157.44</td><td>1.96</td><td>80.43***</td><td>157.46</td><td>1.96</td><td>80.55***</td><td>166.92</td><td>1.97</td><td>84.83***</td></tr><tr><td>Attendance</td><td>.01</td><td>.00</td><td>5.65***</td><td>.01</td><td>.00</td><td>5.47***</td><td>.01</td><td>.01</td><td>5.83***</td><td>.01</td><td>.00</td><td>5.67***</td><td>.01</td><td>.00</td><td>4.96***</td><td>.01</td><td>.00</td><td>4.66***</td><td>.01</td><td>.00</td><td>4.49***</td><td>.01</td><td>.00</td><td>4.22***</td></tr><tr><td>NetBuilder Kiosk Yes/No? (NB)</td><td>205.28</td><td>1.23</td><td>167.59***</td><td>206.02</td><td>1.22</td><td>168.36***</td><td>192.87</td><td>1.2</td><td>160.4***</td><td>193.60</td><td>1.20</td><td>161.08***</td><td>54.9</td><td>1.8</td><td>29.72***</td><td>204.67</td><td>1.22</td><td>167.50***</td><td>205.67</td><td>1.22</td><td>168.24***</td><td>151.14</td><td>1.53</td><td>99.13***</td></tr><tr><td>Post-leaderboard Yes/ No? (LB)</td><td>-1.92</td><td>.91</td><td>-2.11*</td><td>-.96</td><td>.91</td><td>-1.06</td><td>2.32</td><td>.89</td><td>2.61***</td><td>3.17</td><td>.89</td><td>3.57***</td><td>-2.9</td><td>1.9</td><td>-2.23*</td><td>-2.26</td><td>.91</td><td>-2.46*</td><td>-1.28</td><td>.91</td><td>-1.41</td><td>-1.70</td><td>1.12</td><td>-1.51 $^{φ}$ </td></tr><tr><td>Trait Competitiveness (TC)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>90.52</td><td>.89</td><td>101.70***</td><td>90.09</td><td>.89</td><td>101.30***</td><td>51.45</td><td>1.3</td><td>39.61***</td><td>21.65</td><td>.94</td><td>22.92***</td><td>21.45</td><td>.94</td><td>22.74***</td><td>-.10</td><td>1.47</td><td>-.07</td></tr><tr><td>NBxLB</td><td></td><td></td><td></td><td>57.66</td><td>2.45</td><td>23.58***</td><td></td><td></td><td></td><td>52.25</td><td>2.4</td><td>21.86***</td><td>-2.6</td><td>3.7</td><td>-.70</td><td></td><td></td><td></td><td>57.17</td><td>2.44</td><td>23.41***</td><td>41.70</td><td>3.05</td><td>13.68***</td></tr><tr><td>NBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>233.5</td><td>2.4</td><td>97.58***</td><td></td><td></td><td></td><td></td><td></td><td></td><td>133.52</td><td>3.55</td><td>37.67***</td></tr><tr><td>LBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>4.7</td><td>1.8</td><td>2.67***</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-5.68</td><td>2.05</td><td>-2.77**</td></tr><tr><td>LBxNBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>94.1</td><td>4.8</td><td>19.66***</td><td></td><td></td><td></td><td></td><td></td><td></td><td>28.88</td><td>5.03</td><td>5.74***</td></tr><tr><td>R $^{2}_{Adj}$ </td><td>.115</td><td></td><td></td><td>.117</td><td></td><td></td><td>.116</td><td></td><td></td><td>.158</td><td></td><td></td><td>.19</td><td></td><td></td><td>.117</td><td></td><td></td><td>.120</td><td></td><td></td><td>.134</td><td></td><td></td></tr></table>

Note: φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001

To investigate the extent to which traitcompetitive users were driving this trend after the leaderboard was introduced, we compared the game performance pattern of trait-competitive users with non-trait-competitive users in the post-leaderboard period using both time expenditure (Model 8A and 8B in Table 7) and badges (Models 9A and 9B in Table 7) to operationalise trait competitiveness (i.e., users in Quadrant IV in Figure 1). This comparison revealed that only trait-competitive users in the postleaderboard period were following a quadratic growth model, while non-trait-competitive users were only marginally growing and not showing any eventual decline in performance over time. Findings were supported across both measures of trait competitiveness.

To further test the inverted-U pattern we observed among the trait-competitive users, we adopt the method proposed by Lind and Mehlum (2010) and Haans et al. (2016), and conducted our testing in three steps, as shown in Table 8. First, we test the inverted-U pattern among all users after the introduction of leaderboard. As model 7A shows, the coeficient for the quadratic term Attempt<sup>2</sup> is not statistically significant $( B = 1 4 . 9 0 , t = . 6 7 , p > . 0 5 )$ indicating that prior to the introduction of the leaderboard, performance is not afected in a quadratic way. Further, as model 7B shows, the coeficient for the quadratic term $A t t e m p t ^ { 2 }$ is significant and in the expected negative direction $( B = - 7 5 . 3 9 , t = 2 . 4 , p < . 0 5 )$ . This satisfies the first condition for establishing a quadratic relationship. The second condition involves determining that the slope at both ends of the data range is suficiently steep and significant. In our case, the slope at the lower end of the data range based on number of attempts is positive and significant (minimum number of attempts = 1, B = 523.34, t = 2.9, p < .01), and the slope at the higher end of attempt number is negative and significant (maximum attempt = 12, B = −1080.89, $t = - 2 . 4 , p < . 0 1 )$ . As the third and final condition for establishing a quadratic relationship, we determine that the turning point is located well within the data range. Following the recommendation of Hirschberg and Lye (2004) in Haans et al. (2016), we use the Fieller method (Fieller, 1954), which is robust even for finite samples, and estimate the turning point to be at attempt number 4.59, and the 95% confidence interval between 3.24 and 7.66 number of attempts. Both the turning point and the confidence interval values lie within our data range of 1 to 12 number of attempts. Overall, all conditions for establishing the quadratic nature of the relationship are met and we conclude that number of game attempts has a quadratic efect on game performance in terms of points after the introduction of the leaderboard.

Effect of Points on Seconds Per Attempt: Trait-Competitive Users (Total Time Expenditure)  
![](/api/attachments/975EQNXG/fulltext/images/0b1bc1a2153e93c5f4ef17db075b73de650187baf452316e0eeea3acb6bfa093.jpg)

Effect of Points on Seconds Per Attempt: Trait-Competitiv Users (Total Badges Earned)  
![](/api/attachments/975EQNXG/fulltext/images/4faef76882db9a1b98126028fa5cb74705093651dc9e4481554745abac618bca.jpg)

Effect of Leaderboard on Seconds Per Attempt: Trait-Competitive Users (Total Time Invested)  
![](/api/attachments/975EQNXG/fulltext/images/6d96115946cccab6e8daadf174079df89f48622793a6ed422714bc1601db6da0.jpg)

Effect of Leaderboard on Seconds Per Attempt: Trait-Competitive Users (Total Badges Earned)  
![](/api/attachments/975EQNXG/fulltext/images/f9f9cceccc4f574550e6f9bdc05958a47476b06c60a02819a8e3e1d317a22763.jpg)  
Figure 4. A. Positive two-way interaction between points and trait competitiveness (total time expenditure) on seconds per attempt. B. Two-way interaction between points and trait competitiveness (badges) on seconds per attempt. C. Three-way interaction between points, leaderboard, and trait competitiveness (total time expenditure) on seconds per attempt. D. Three-way interaction between points, leaderboard, and trait competitiveness (badges) on seconds per attempt.

For the post-leaderboard time period, we test whether the number of attempts of trait-competitive users show a stronger quadratic efect compared to non-trait-competitive users. We model the quadratic efect among the trait-competitive users using both time-spent (Model 8B) and badges-earned (Model 9B). Following the same steps for establishing a quadratic efect as described above, we first determine that results in Model 8B and 9B for the quadratic term $A t t e m p t ^ { 2 }$ are significant and in the expected negative direction $( B = - 1 0 0 . 3 5 , \ t = 2 . 3 , \ p < . 0 5$ for Model 8B and B = −86.52, t = 2.0, p < .05 for Model 9B). Secondly, we establish that the slopes at both ends of the data range (attempt number) are suficiently steep. For trait-competitive users, the slopes are positive and significant at the lower end of number of attempts in both models (minimum attempt = 1, B = 722.1, t = 2.5, p < .01 for Model 8B, B = 644.9, t = 2.2, p < .05 for Model 9B) while the slopes are negative and significant at the higher end of number of attempts in both models (maximum attempt = 12,

Table 
4. Tests of H2 – DD and DDD estimation; N = 56,267 obs.

<table><tr><td rowspan="2">DV: Number of Reattempts</td><td colspan="6">Model 3 (H2A)</td><td colspan="8">Model 4A (H2B)Trait Competitiveness based on Time</td><td colspan="8">Model 4B (H2B)Trait Competitiveness based on Badges</td><td></td><td></td></tr><tr><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Constant</td><td>3.5</td><td>.04</td><td>99.63***</td><td>3.5</td><td>.04</td><td>99.6***</td><td>2.89</td><td>.03</td><td>84.40***</td><td>2.89</td><td>.03</td><td>84.59***</td><td>2.80</td><td>.03</td><td>81.7***</td><td>3.23</td><td>.03</td><td>95.16***</td><td>3.24</td><td>.03</td><td>95.22***</td><td>3.16</td><td>.03</td><td>92.02***</td></tr><tr><td>Attendance</td><td>.00</td><td>.00</td><td>2.02*</td><td>.00</td><td>.00</td><td>2.0*</td><td>.00</td><td>.00</td><td>3.89***</td><td>.00</td><td>.00</td><td>4.12***</td><td>.00</td><td>.00</td><td>3.90***</td><td>-.00</td><td>.00</td><td>-1.37</td><td>-.00</td><td>.00</td><td>-1.35**</td><td>-.00</td><td>.00</td><td>-1.35</td></tr><tr><td>NetBuilder Kiosk Yes/No? (NB)</td><td>-.54</td><td>.02</td><td>-23.81***</td><td>-.5</td><td>.02</td><td>-23.9***</td><td>-.81</td><td>.02</td><td>-37.52***</td><td>-.82</td><td>.02</td><td>-37.80***</td><td>.12</td><td>.03</td><td>4.20***</td><td>-.71</td><td>.02</td><td>-32.60***</td><td>-.71</td><td>.02</td><td>-32.70***</td><td>-.31</td><td>.03</td><td>-11.27***</td></tr><tr><td>Post-leaderboard Yes/No? (LB)</td><td>-.02</td><td>.02</td><td>-1.44</td><td>-.03</td><td>.02</td><td>-1.9*</td><td>.07</td><td>.02</td><td>4.75***</td><td>.05</td><td>.02</td><td>3.31***</td><td>.07</td><td>.02</td><td>3.30***</td><td>-.02</td><td>.02</td><td>-1.40</td><td>-.04</td><td>.02</td><td>-2.21*</td><td>.01</td><td>.02</td><td>.31</td></tr><tr><td>Trait Competitiveness (TC)</td><td></td><td></td><td></td><td></td><td></td><td></td><td>11.43</td><td>.02</td><td>189.52***</td><td>1.42</td><td>.02</td><td>89.09***</td><td>1.64</td><td>.02</td><td>61.04***</td><td>1.4</td><td>.02</td><td>82.22***</td><td>1.40</td><td>.02</td><td>82.26***</td><td>1.62</td><td>.03</td><td>58.47***</td></tr><tr><td>NBxLB</td><td></td><td></td><td></td><td>-.1</td><td>.05</td><td>-2.2*</td><td></td><td></td><td></td><td>-.2</td><td>.04</td><td>-4.76***</td><td>-.06</td><td>.06</td><td>-2.10*</td><td></td><td></td><td></td><td>-.15</td><td>.04</td><td>-3.45**</td><td>-.05</td><td>.06</td><td>-.87</td></tr><tr><td>NBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-1.47</td><td>.05</td><td>-27.80***</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-.94</td><td>.06</td><td>-14.77***</td></tr><tr><td>LBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>.10</td><td>.03</td><td>-1.30</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-.07</td><td>.04</td><td>-1.73 $^{p}$ </td></tr><tr><td>LBxNBxTC</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>-.37</td><td>.08</td><td>-4.68***</td><td></td><td></td><td></td><td></td><td></td><td></td><td>-.15</td><td>.09</td><td>-1.67^</td></tr><tr><td>R $^{2}_{\text{Adj}}$ </td><td>.01</td><td></td><td></td><td>.01</td><td></td><td></td><td>.1.133</td><td></td><td></td><td>.134</td><td></td><td></td><td>.125</td><td></td><td></td><td>.116</td><td></td><td></td><td>.116</td><td></td><td></td><td>.124</td><td></td><td></td></tr></table>

Note: φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001

B = −1386.6, t = −2.1, p < .05 for Model 8B, $B = - 1 2 4 3 . 5 , t = - 1 . 9 , \dot { p } < . 0 5$ for Model 9B). Finally, the turning point for trait-competitive users in Model 8B is at attempt number 4.77, and the 95% confidence interval is between 2.97 and 9.54 number of attempts. The turning point for trait-competitive users in Model 9B is at attempt number 4.76, and the 95% confidence interval is between 2.35 and 13.01 number of attempts. The turning point and the confidence interval values lie within our data range of 1 to 12 number of attempts except for a small portion at the extreme right from 12 to 13.01.

Therefore, we conclude that number of game attempts has a stronger quadratic efect on game performance in terms of points for the trait-competitive users after the leaderboard was added. Results from the above three steps along with the Sasabuchi-test of inverse-U shape provide strong evidence that traitcompetitive individuals in the post-leaderboard period were initially driven by the leaderboard to steadily improve, maximised feedback from previous attempts, hit a performance ceiling and declined in performance thereafter. Overall, findings support Hypothesis 4B.

## 7. Discussion

Competitive game elements such as points and leaderboards are used in various industries as a means to enhance users’ engagement and performance. However, the efectiveness of these competitive game elements has come under question due to mixed findings and the methodological limitations in existing gamification studies, as outlined herein. Consistent with past research, we found evidence of mixed efects in our study however, due to our natural experiment, we were able to provide some clarity surrounding our mixed findings.

With regard to engagement, we determined that the nature of the mixed efects was consistent across both types of game elements and that the efects were independent. Specifically, both points and leaderboards positively and independently afected average time spent per attempt, a finding that is consistent with that from Landers and Landers (2014) who reported positive associations between leaderboards and time expenditure. However, we also found that both competitive game elements in our study were negatively associated with other engagement indicators, specifically the number of reattempts and engagement of a broad audience, a finding that is consistent with research suggesting that competitive game elements such as leaderboards are unrelated or negatively related to engagement (Costa et al., 2013).

Furthermore, our findings related to efects on engagement suggest that competitive game elements successfully engage a smaller sub-set of users at the expense of disengaging other users, highlighting some of the potential trade-ofs in environments with competitive structures noted by Landers et al. (2019). While competitive game elements (i.e. points and leaderboards) engage a sub-set of trait-competitive users who tend to dominate the game space and spend more time trying to beat a game, the potential tradeof is that users with lower trait competitiveness are potentially driven away and have less opportunity to participate. Notably, tradeofs such as this are not just present in physical gamified settings such as the museum in our current study, but also appear in online games (Hinz et al., 2015). By identifying trait competitiveness as a moderator in our study and providing systembased mechanisms for its measurement, we provide insight on the types of users who are more (and less) likely to be drawn to certain games which, in turn, may inform future game design.

Table 5. Tests of H3 – DD estimation; N = 600 obs.

<table><tr><td rowspan="2"></td><td colspan="3">Number of Unique Daily User Attempts</td><td colspan="6">Proportion of Unique Daily User Attempts who are Trait-Competitive</td></tr><tr><td colspan="3">Model 5 (H3A)</td><td colspan="3">Model 6A (H3B)Trait Competitiveness based on Time</td><td colspan="3">Model 6B (H3B)Trait Competitiveness based on Badges</td></tr><tr><td>DV →</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Constant</td><td>255.59</td><td>13.6</td><td>18.8***</td><td>.74</td><td>.01</td><td>58.0***</td><td>.31</td><td>.97</td><td>16.93***</td></tr><tr><td>Attendance</td><td>.4</td><td>.01</td><td>30.15***</td><td>-.00</td><td>.00</td><td>-1.5</td><td>.00</td><td>.00</td><td>3.66***</td></tr><tr><td>NetBuilder Kiosk Yes/No? (NB)</td><td>-471.0</td><td>9.4</td><td>-49.7***</td><td>.08</td><td>.01</td><td>9.4***</td><td>.01</td><td>.01</td><td>.78</td></tr><tr><td>Post-leaderboard Yes/No? (LB)</td><td>-18.21</td><td>9.4</td><td>-1.9*</td><td>-.03</td><td>.01</td><td>-3.1**</td><td>-.00</td><td>.01</td><td>.18</td></tr><tr><td>NBxLB</td><td>-25.2</td><td>13.2</td><td>-1.9*</td><td>.03</td><td>.01</td><td>2.6**</td><td>.03</td><td>.02</td><td>1.58φ</td></tr><tr><td>R2Adj</td><td>.91</td><td></td><td></td><td>.316</td><td></td><td></td><td>.04</td><td></td><td></td></tr></table>

Note: φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001

In focusing on performance growth in our study, we extend existing gamification research, which tends to model performance at a single point (e.g., Nebel et al., 2017; Sailer et al., 2017). As with the research on engagement, research exploring the efect of competitive game elements on performance is mixed and shows both positive (e.g., Yang et al., 2016) and negative (e.g., Christy & Fox, 2014) efects. Again, our consideration of multiple dimensions of competitiveness proves valuable in reconciling these mixed findings. Beyond demonstrating how the leaderboard served to invoke structural competitiveness thereby afecting users’ performance trajectory, we also discovered that trait-competitive users difer from non-trait-competitive users on post-leaderboard performance growth. Modelling user’s performance trajectories with fixed efects growth models allowed us to control for user characteristics, with findings providing strong support of the inverted-U performance growth pattern.

Altogether, the combined findings on engagement and performance growth seem to indicate that observed efects of competitive game elements can cut both ways, sparking an initial boost in attention and performance followed by a performance decline. This is consistent with research in learning and psychology, which recognises roughly 20 minutes as an important threshold for human attention span; after about 20 minutes, sustained attention begins to lapse and performance eventually sufers due to distraction (Fortenbaugh et al., 2015; Ruf & Lawson, 1990). Correspondingly, NetBuilder users in our study spent around 5 min per attempt, with peak performance typically achieved around the $4 ^ { \mathrm { t h } }$ consecutive attempt and performance declining thereafter. This highlights an additional consideration for gamified systems design, as the efects of competitive game elements appear related to users innate attention span.

In conclusion, through our research, we provide a clearer understanding of efects of competitive game elements by drawing on social comparison theory and extending theory on multiple dimensions of competitiveness. Additionally, because strong causal links between competitive game elements and associated outcomes are largely missing from the gamification literature, our study ofers an important extension to the research by way of design (i.e., natural experiment). Lastly, our exploration of competitive game elements within an informal learning context allows us to determine the salience of these types of efects in these settings. Overall, we find support for seven hypotheses and partial support for one hypothesis. Our findings have implications for both theory and practice, outlined below.

## 7.1. Theoretical contributions

Our research provides a comprehensive and nuanced understanding of how competitive game elements such as points and leaderboards trigger diferent dimensions of competitiveness in ways that afect engagement and performance growth. We do this in several ways. First, by considering two theoretical perspectives – competitiveness and social comparison – in relation to diferent types of competitive game elements, we are able to articulate the process through which we hypothesise these elements afect engagement and performance growth. In adopting this integrated perspective, our study goes beyond existing gamification research to explicate how social comparison precedes competitive behaviour in gamified contexts. In terms of the competitive game elements, points quantify users’ performance and leaderboards publicly recognise high-performing users; both of these game elements encourage users to compare performance with others, which, as theorised by Garcia et al. (2013), brings about competitive behaviour. Our findings demonstrate that these separate game elements exert similar yet distinct efects on engagement outcomes, lending support to our argument that both points and leaderboard game elements follow similar paths through social comparison and competitiveness to afect changes in engagement and performance growth.

![](/api/attachments/975EQNXG/fulltext/images/9536370c700438e291c4483c2ba9b49bf77c57484b0a7bd89fd67ed899bb8817.jpg)

![](/api/attachments/975EQNXG/fulltext/images/cd277e352a74c63957d7b71a46d067554213fe0189b5cd0a3e7fd5898e7be5bb.jpg)

![](/api/attachments/975EQNXG/fulltext/images/7f02adf16c4caadf80384f7e17a8ec859a8980d4f7fc212ddcb6bd6dea6b6f2d.jpg)

![](/api/attachments/975EQNXG/fulltext/images/779a2ded024e046aea6e8793bec9f0e03c4bf0d675c1d1af5027a06a9d0fdb40.jpg)  
Figure 5. Two-way interaction between points and trait competitiveness (total time expenditure) on number of reattempts. B. Two-way interaction between points and trait competitiveness (total badges earned) on number of reattempts. C. Three-way interaction between points, leaderboard, and trait competitiveness (total time expenditure) on number of reattempts. D. Threeway interaction between netbuilder, leaderboard, and trait competitiveness (badges) on number of reattempts.

Second, by identifying and modelling diferent dimensions of competitiveness, we demonstrate how the efects of competitive game elements on engagement and performance growth vary across individuals. Many gamification studies tend to focus on structural aspects of competitiveness, which is only one dimension of competitiveness. We conceptualise competitiveness as multidimensional and consider individual diferences in competitiveness in addition to structural competitiveness as part of our study. We demonstrate that both points and leaderboards generate structural competitiveness, which encourages users to compare their points and their related position with others and leads to more aggressive, competitive behaviour as shown in overall changes in engagement and performance growth.

Furthermore, we demonstrate that the efects associated with structural competitiveness resonate most strongly with users higher in trait competitiveness; in other words, trait-competitive individuals have stronger responses in these types of competitive environments. The interaction between trait competitiveness and competitive settings is well-established in organisational contexts (e.g., Brown et al., 1998; Fletcher & Nusbaum, 2008), however the ways in which multiple dimensions of competitiveness interact to afect engagement and performance growth in gamification and IS contexts has been largely overlooked. Gamification researchers have applied theories of competitiveness to understand the efects of competitive game elements (e.g., Liu et al., 2013) however, with few exceptions (e.g., Höllig et al., 2018a, 2018b; Landers et al., 2019), gamification researchers have neither recognised individual diferences in trait competitiveness nor have they explored how these diferences potentially impact efects associated with game elements. Our exploration of trait competitiveness is aligned with recommendations by IS scholars to consider individual traits during design of gamified systems (Liu et al., 2017). Our model not only integrates multiple theories on psychological factors (i.e. competitiveness and social comparison) but also accounts for multiple dimensions of these factors, which helps enrich our understanding of how competitive game elements afect diferent individuals.

Lastly, our exploration of the diferent ways in which trait competitiveness may be expressed moves beyond existing research, which tends to rely on selfreports of competitiveness (e.g., Brown et al., 1998; Fletcher & Nusbaum, 2008; Höllig et al., 2018a). Instead of self-reported measures of competitiveness, we used observations of competitive behaviours and associated outcomes of competitive behaviours to operationalise trait competitiveness. Findings from both means of operationalisation converged to suggest that trait-competitive users demonstrated significantly stronger responses to competitive game elements.

Table 6. Test of H4A – FE estimation; N = 1381 obs.

<table><tr><td rowspan="3">DV: Performance of Users with Number of Attempts ≥ 3</td><td colspan="3">Pre-Leaderboard</td><td colspan="3">Post-Leaderboard</td></tr><tr><td colspan="3">Model 7A (H4A)</td><td colspan="3">Model 7B (H4A)</td></tr><tr><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Constant</td><td>-352.97</td><td>192.00</td><td> $-1.84^{\varphi}$ </td><td>-951.34</td><td>416.16</td><td> $-2.29^{*}$ </td></tr><tr><td>Time Spent per Attempt</td><td>1.71</td><td>.16</td><td>10.69***</td><td>2.97</td><td>.34</td><td>8.74***</td></tr><tr><td>Attempt #</td><td>165.46</td><td>133.72</td><td>1.24</td><td>686.68</td><td>238.36</td><td>2.88**</td></tr><tr><td>Attempt  $\#^{2}$ </td><td>14.90</td><td>22.12</td><td>0.67</td><td>-75.39</td><td>31.02</td><td> $-2.43^{*}$ </td></tr><tr><td> $R^{2}_{Adj}$ </td><td>.23</td><td></td><td></td><td></td><td>.25</td><td></td></tr><tr><td>K (Number of Users)</td><td></td><td>225</td><td></td><td></td><td>165</td><td></td></tr><tr><td>N (Number of Attempts by K Users)</td><td></td><td>801</td><td></td><td></td><td>580</td><td></td></tr><tr><td>F Statistic (Prob &gt; F)</td><td></td><td>F(3, 573) = 45.37***</td><td></td><td></td><td>F(3, 412) = 29.31***</td><td></td></tr><tr><td>Hausman test $^{2}$ </td><td></td><td> $\chi^{2}(3) = 10.01^{*}$ </td><td></td><td></td><td> $\chi^{2}(3) = 17.00^{***}$ </td><td></td></tr></table>

1.Note:  
φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001  
2.Hausman test indicates that the H<sub>0</sub> of a random efect model specification is rejected by our data; accordingly, a fixed efects model for our data is supported and used above.

Table 7. Tests of H4B – FE estimation: Performance on successive attempts on Netbuilder post-leaderboard.

<table><tr><td rowspan="4"></td><td colspan="6">Trait Competitiveness based on Time</td><td colspan="6">Trait Competitiveness based on Badges</td></tr><tr><td colspan="3">Non Trait-Competitive Users</td><td colspan="3">Trait-Competitive Users</td><td colspan="3">Non Trait-Competitive Users</td><td colspan="3">Trait-Competitive Users</td></tr><tr><td colspan="3">Model 8A</td><td colspan="3">Model 8B</td><td colspan="3">Model 9A</td><td colspan="3">Model 9B</td></tr><tr><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Constant</td><td>-1434.79</td><td>446.17</td><td>-3.22**</td><td>-1049.53</td><td>703.80</td><td>-1.49</td><td>-1396.79</td><td>500.56</td><td>-2.79**</td><td>-891.10</td><td>709.20</td><td>-1.26</td></tr><tr><td>Time Spent per Attempt</td><td>4.63</td><td>.35</td><td>13.23***</td><td>2.39</td><td>.49</td><td>4.88***</td><td>3.79</td><td>.35</td><td>10.83***</td><td>2.51</td><td>.52</td><td>4.83***</td></tr><tr><td>Attempt</td><td>733.72</td><td>408.09</td><td>1.80</td><td>1039.08</td><td>377.12</td><td>2.76**</td><td>847.61</td><td>425.94</td><td>1.99*</td><td>876.59</td><td>378.17</td><td>2.32*</td></tr><tr><td> $Attempt^2$ </td><td>-141.50</td><td>87.50</td><td>-1.62</td><td>-100.35</td><td>43.52</td><td>-2.31*</td><td>-141.66</td><td>84.94</td><td>-1.67</td><td>-86.53</td><td>43.22</td><td>-2.00*</td></tr><tr><td> $R^{2}_{Adj}$ </td><td></td><td>.46</td><td></td><td></td><td>.19</td><td></td><td></td><td>.38</td><td></td><td></td><td>.21</td><td></td></tr><tr><td>K (Number of Users)</td><td></td><td>86</td><td></td><td></td><td>79</td><td></td><td></td><td>86</td><td></td><td></td><td>79</td><td></td></tr><tr><td>N (Number of Attempts by K Users)</td><td></td><td>274</td><td></td><td></td><td>306</td><td></td><td></td><td>282</td><td></td><td></td><td>298</td><td></td></tr><tr><td>F Statistic(Prob &gt; F)</td><td colspan="3">F(3, 185) = 60.25***</td><td colspan="3">F(3, 224) = 11.90***</td><td colspan="3">F(3,193) = 41.04***</td><td colspan="3">F(3,216) = 10.23***</td></tr><tr><td>Hausman  $test^2$ </td><td colspan="3"> $\chi^2 (3) = 2.84$ </td><td colspan="3"> $\chi^2 (3) = 11.52**$ </td><td colspan="3"> $\chi^2 (3) = 0.57$ </td><td colspan="3"> $\chi^2 (3) = 15.46**$ </td></tr></table>

1.Note: φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001  
2.Hausman test indicates that the $\mathsf { H } _ { 0 }$ of a random efect model specification is rejected by our data; accordingly, a fixed efects model for our data is supported and used above.

## 7.2. Practical implications

Our findings demonstrate the importance of articulating strategic goals when undergoing game element design (Liu et al., 2017). In the case of the gamified kiosk in our study (i.e. NetBuilder), its “efectiveness” depends on the strategic goals of implementation. We, as researchers, did not design the kiosks nor did we have a role in determining the strategic outcomes associated with the kiosks. However, if the strategic goal of gamifying the kiosk via the points or the leaderboard was to increase the amount of time users spent on the kiosk, then we can conclude that these competitive game elements were indeed efective. At the same time, if the strategic goal was to increase participation across all types of users, then the elements associated with the kiosk actually worked against this goal; the number of unique user attempts at the NetBuilder kiosk was much lower than the other kiosks overall.

Given that the games under exploration related directly to cybersecurity content, we consider implications for cyber training. Presently, there is an enormous talent shortage in cybersecurity (Global Information Security Workforce Study, 2017) and companies need to provide ongoing training and upskilling in the cyber workforce (Van Zadelhof, 2017). Our findings support the efectiveness of existing endeavours of gamified cyber training (Adams & Makramalla, 2015). However, while we find that the use of points and implementation of a leaderboard in the NetBuilder game significantly improved performance on networking and cybersecurity tasks, we found that this efect was attributed to the traitcompetitive users. In this way, the use of gamified training systems for such a critical organisational area should consider and ideally adapt to individual diferences in user motivation and trait competitiveness.

## 7.3. Limitations and future research directions

Our study had certain limitations. First, the museum exhibit in our study included only a single gamified kiosk and we determined that this kiosk was dominated by trait-competitive users. Thus, we are unable to determine if users with lower trait-competitiveness were actively avoiding the gamified kiosk or if these users simply did not have an opportunity due to the resource constraint. Future research might determine how users with lower trait-competitiveness experience competitive game elements in environments without these resource constraints. Additionally, the data collected was secondary, meaning that we were not able to collect information on individual demographics such as age and gender. Accordingly, we encourage future researchers to explore the extent to which demographic characteristics afect the relationships we observed.

<table><tr><td rowspan="3"></td><td colspan="3">Model 7B</td><td colspan="6">Trait Competitiveness based on Time</td><td colspan="6">Trait Competitiveness based on Badges</td></tr><tr><td colspan="3">Post Leaderboard</td><td colspan="3">Model 8A</td><td colspan="3">Model 8B</td><td colspan="3">Model 9A</td><td colspan="3">Model 9B</td></tr><tr><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td><td>B</td><td>SE</td><td>t</td></tr><tr><td>Slope at lower bound (min-attempt)</td><td>523.34</td><td>180.46</td><td>2.90**</td><td>373.75</td><td>229.29</td><td> $1.63^{\Phi}$ </td><td>722.10</td><td>292.35</td><td>2.47**</td><td>568.06</td><td>254.74</td><td>2.23*</td><td>644.93</td><td>297.20</td><td>2.17*</td></tr><tr><td>Slope at high bound (max-attempt)</td><td>-1080.89</td><td>452.26</td><td>-2.39**</td><td>-630.40</td><td>573.09</td><td>-1.10</td><td>-1386.6</td><td>657.16</td><td>-2.11*</td><td>-823.36</td><td>534.65</td><td>-1.54Φ</td><td>-1243.51</td><td>640.98</td><td>-1.94*</td></tr><tr><td>Test of joint significance of attempt and attempt-squared (p-value)</td><td colspan="3">p = 0.01**</td><td colspan="3">p = 0.48</td><td colspan="3">p = 0.005**</td><td colspan="3">p = 0.32</td><td colspan="3">p = 0.03*</td></tr><tr><td>Sasabuchi-test of inverse U-shape in attempt</td><td colspan="3">t = 2.39**</td><td colspan="3">t = 1.10</td><td colspan="3">t = 2.11*</td><td colspan="3">t = 1.54Φ</td><td colspan="3">t = 1.94*</td></tr><tr><td>Estimated extreme point (attempt)</td><td colspan="3">4.59</td><td colspan="3">2.86</td><td colspan="3">4.77</td><td colspan="3">3.04</td><td colspan="3">4.76</td></tr><tr><td>Interval (attempt)</td><td colspan="3">[1; 12]</td><td colspan="3">[1; 6]</td><td colspan="3">[1; 12]</td><td colspan="3">[1; 6]</td><td colspan="3">[1; 12]</td></tr><tr><td>95% confidence interval - Fieller method</td><td colspan="3">[3.24; 7.66]</td><td colspan="3">[-Infinite; +Infinite]</td><td colspan="3">[2.97; 9.54]</td><td colspan="3">[-Infinite; +Infinite]</td><td colspan="3">[2.35; 13.01]</td></tr></table>

Table 
8. Inverted-U Test on FE estimation post-leaderboard.  
Note: φ p <.1, \* p <.05, \*\* p <.01, \*\*\* p <.001

Consistent with observations by other IS scholars, notably Santhanam et al. (2016) and Liu et al. (2013), the efects of competitive game elements within our study proved to be complicated and nuanced, and we emphasise the importance of devoting ongoing empirical attention to understanding the role of competitive game elements in IS. While the existing research converges to suggest that the efects of competitive game elements are mixed (Hamari et al., 2014; Koivisto & Hamari, 2019), we are able to provide insight into the nature of these varied efects in several ways. For one, we theorised and confirmed that the efects associated with two separate competitive game elements (points and leaderboards) were consistent with one another and that both explained distinct variance in the respective outcomes. We encourage future researchers to consider efects of competitive game elements in ways that methodologically account for the unique efects of multiple competitive game elements, as this will help determine which game elements matter most.

Perhaps more importantly, our consideration of trait competitiveness as a moderator in our study enabled us to reconcile mixed findings and ofer strong theoretical arguments as to why competitive game elements have strong efects on some individuals and not others. Aligned with recommendations from Liu et al. (2017) who encourage IS scholars to identify individual traits that potentially inform systems design, we identify competitiveness as an important trait to consider. That trait competitiveness moderates the efects of competitive game elements indicates that the usefulness of competition in IS may be conditional on individual traits, notably trait competitiveness. Future IS research may benefit from conceptualisation of such individual diferences and from performing similar moderation analyses that explore other user characteristics to determine if efects change according to gender, age, and other variables.

Our research provides insight on how users perform and learn in gamified informal learning environments. As noted above, our results related to performance growth demonstrate that performance starts to diminish after about 27 minutes<sup>8</sup> in this environment, which is consistent with research suggesting that students’ attention diminishes after about 20 minutes (see Bradbury, 2016 for review). This finding sets the agenda for future studies to investigate whether this performance pattern (i.e. rise-plateau-decline) manifests in contexts other than informal learning environments and to explore other nuanced moderators, such as game design and other contextual factors, that could impact users performance curve.

Our study was conducted in an informal learning setting and, thus, we expect that our findings would generalise to similar settings such as science museums with interactive experiences. Further methodologically rigorous research is needed to determine if our results generalise to more formal learning settings. Future research may explore how diferent types of leaderboards demonstrate diferential efects contingent on trait competitiveness. We encourage researchers to consider trait competitiveness in future gamification studies and explore alternative operationalisations of trait competitiveness, as this will provide further insight on the boundary conditions. Lastly, to shed light on the causal mechanisms explaining the links between competitive game elements and related outcomes, future research may benefit from mediation analyses.

## Notes

1. Experimentally-manipulated kiosk is synonymous with experimental kiosk.

2. There are a number of diferent types of categorisations of game elements (e.g., Blohm & Leimeister, 2013; Hamari et al., 2014). Based on our review of the literature, each of the included elements were designated in at least one study as a competitive element and thus included in the review.

3. For example, scholars distinguish between direct vs. indirect competitiveness (Liu et al., 2013), and identify various facets of individual competitiveness (e.g., Orosz et al., 2018).

4. We address how this may be attributed to space and time constraints and therefore control for daily attendance in all of our models.

5. These users were those who reattempted at least three times on the same day.

6. We note that the Points x Trait Competitiveness moderation is represented as a two-way interaction because the points game element was consistent throughout both time period; we report results from the full model as this controls for the effects of all other variables in the respective model.

7. pre- vs. post-leaderboard; post-leaderboard traitcompetitive vs. post-leaderboard non-traitcompetitive for both total time expenditure and badges earned.

8. noting that the turning point of the curve for H4 was 4.59 attempts, we multiplied this by the average number of seconds per attempt presented in Table 2D.

## Disclosure statement

No potential conflict of interest was reported by the authors.

## Funding

This work was supported by the National Science Foundation (NSF), Directorate for Education and Human Resources [1523174].

## ORCID

Laura Amo http://orcid.org/0000-0002-6433-788X Ruochen Liao http://orcid.org/0000-0003-1059-4087 Rajiv Kishore http://orcid.org/0000-0002-9476-4479 Hejamadi R. Rao http://orcid.org/0000-0002-2307-231X

## References

Ackerman, P. L., Kanfer, R., Shapiro, S. W., Newton, S., & Beier, M. E. (2010). Cognitive fatigue during testing: An examination of trait, time-on-task, and strategy influences. Human Performance, 23(5), 381–402. https:// doi.org/10.1080/08959285.2010.517720

Adams, M., & Makramalla, M. (2015). Cybersecurity skills training: An attacker-centric gamified approach. Technology Innovation Management Review, 5(1), 5–14. https://doi.org/10.22215/timreview/861

Alavi, M., & Leidner, D. E. (2001). Research commentary: Technology-mediated learning—A call for greater depth and breadth of research. Information Systems Research, 12 (1), 1–10. https://doi.org/10.1287/isre.12.1.1.9720

Anderson, C., Hildreth, J. A. D., & Howland, L. (2015). Is the desire for status a fundamental human motive? A review of the empirical literature. Psychological Bulletin, 141(3), 574. https://doi.org/10.1037/a0038781

Andruf, H., Carraro, N., Thompson, A., Gaudreau, P., & Louvet, B. (2009). Latent class growth modelling: A tutorial. Tutorials in Quantitative Methods for Psychology, 5(1), 11–24. https://doi.org/10.20982/tqmp. 05.1.p011

Angrist, J. D., & Pischke, J. S. (2008). Mostly harmless econometrics: An empiricist’s. companion: Princeton University Press.

Aspinwall, L. G., & Taylor, S. E. (1993). Efects of socia comparison direction, threat, and self-esteem on afect, self-evaluation, and expected success. Journal of Personality and Social Psychology, 64(5), 708. https://doi. org/10.1037/0022-3514.64.5.708

Baum, C. F., Schafer, M. E., & Stillman, S. (2003). Instrumental variables and GMM: Estimation and testing. The Stata Journal: Promoting Communications on Statistics and Stata, 3(1), 1–31. https://doi.org/10. 1177/1536867X0300300101

Bess, C. (2013). Gamification: Driving behavior change in the connected world. Cutter IT Journal, 26(2), 31–37. Retrieved from https://www.cutter.com/sites/default/ files/itjournal/fulltext/2013/02/itj1302.pdf

Blohm, I., & Leimeister, J. M. (2013). Gamification: Design of IT-based enhancing services for motivational support

and behavioral change. Business & Information Systems Engineering, 5(4), 275–278. https://doi.org/10.1007 s12599-013-0273-5

Boticki, I., Baksa, J., Seow, P., & Looi, C.-K. (2015). Usage of a mobile social learning platform with virtual badges in a primary school. Computers & Education, 86, 120–136. https://doi.org/10.1016/j.compedu.2015.02.015

Bradbury, N. (2016). Attention span during lectures: 8 seconds, 10 minutes, or more? Advances in Physiology Education, 40(4), 509–513. https://doi.org/10.1152 advan.00109.2016

Brown, S. P., Cron, W. L., & Slocum, J. W., Jr. (1998). Efects of trait competitiveness and perceived intraorganizational competition on salesperson goal setting and performance. Journal of Marketing, 62(4), 88–98. https://doi.org/10. 1177/002224299806200407

Buil, I., Catalán, S., & Martínez, E. (2020). Engagement in business simulation games: A self-system model of motivational development. British Journal of Educational Technology, 51(1), 297–311. https://doi.org/10.1111/bjet. 12762

Buunk, B. M., Vanyperen, N. W., Taylor, S. E., & Collins, R. L. (1991). Social comparison and the drive upward revisited: Afiliation as a response to marital stress. European Journal of Social Psychology, 21(6), 529–546. https://doi.org/10.1002/ejsp.2420210607

Cagiltay, N. E., Ozcelik, E., & Ozcelik, N. S. (2015). The efect of competition on learning in games. Computers & Education, 87, 35–41. https://doi.org/10.1016/j.compedu. 2015.04.001

Campbell, D. T. (1957). Factors relevant to the validity of experiments in social settings. Psychological Bulletin, 54 (4), 297. https://doi.org/10.1037/h0040950

Cesário, V., Radeta, M., Matos, S., & Nisi, V. (2017). The Ocean Game: Assessing Children's Engagement and Learning in a Museum Setting Using a Treasure-Hunt Game. Paper presented at the Extended Abstracts Publication of the Annual Symposium on Computer-Human Interaction in Play, Amsterdam, The Netherlands doi:10.1145/3130859

Chang, K.-E., Chen, Y.-L., Lin, H.-Y., & Sung, Y.-T. (2008). Efects of learning support in simulation-based physics learning. Computers & Education, 51(4), 1486–1498. https://doi.org/10.1016/j.compedu.2008.01.007

Cheng, J. T., & Tracy, J. L. (2014). Toward a unified science of hierarchy: Dominance and prestige are two fundamental pathways to human social rank. In J. T. Cheng, J. L. Tracy, & C. Anderson (Eds.), The Psychology of Social Status (pp. 3–27). Springer.

Cheng, J. T., Tracy, J. L., & Henrich, J. (2010). Pride, personality, and the evolutionary foundations of human social status. Evolution and Human Behavior, 31(5), 334–347. https://doi.org/10.1016/j.evolhumbehav.2010.02.004

Cheong, C., Cheong, F., & Filippou, J. (2013). Quick quiz: A gamified approach for enhancing learning. Paper presented at the Pacific Asia Conference on Information Systems, Jeju Island, Korea.

Christy, K. R., & Fox, J. (2014). Leaderboards in a virtual classroom: A test of stereotype threat and social comparison explanations for women’s math performance. Computers & Education, 78, 66–77. https://doi.org/10. 1016/j.compedu.2014.05.005

Costa, J. P., Wehbe, R. R., Robb, J., & Nacke, L. E. (2013). Time’s up: Studying leaderboards for engaging punctual behaviour. Paper presented at the Proceedings of the First

International Conference on Gameful Design, Research, and Applications, Toronto, Canada.

Deci, E. L., Ryan, R. M., Gagné, M., Leone, D. R., Usunov, J., & Kornazheva, B. P. (2001). Need satisfaction, motivation, and well-being in the work organizations of a former eastern bloc country: A cross-cultural study of self-determination. Personality & Social Psychology Bulletin, 27(8), 930–942. https://doi.org/10.1177/ 0146167201278002

Deterding, S. (2011). Situated motivational afordances of game elements: A conceptual model. Paper presented at the gamification: Using game design elements in nongaming contexts, a workshop at the ACM Conference on Human Factors in Computing Systems, Vancouver, Canada.

Dunning, T. (2012). Natural experiments in the social sciences: A design-based approach. Cambridge University Press.

Ertac, S. (2005). Social comparisons and optimal information revelation: Theory and experiments. Job Market Paper, UCLA.

Festinger, L. (1954). A theory of social comparison processes. Human Relations, 7(2), 117–140. https://doi. org/10.1177/001872675400700202

Fieller, E. C. (1954). Some problems in interval estimation. Journal of the Royal Statistical Society: Series B (Methodological), 16(2), 175–185. Retrieved from http://www.jstor.com/stable/2984043

Fletcher, T. D., & Nusbaum, D. N. (2008). Trait competitiveness as a composite variable: Linkages with facets of the big-five. Personality and Individual Diferences, 45(4), 312–317. https://doi.org/10.1016/j.paid.2008.04.020

Fortenbaugh, F. C., DeGutis, J., Germine, L., Wilmer, J. B., Grosso, M., Russo, K., & Esterman, M. (2015). Sustained attention across the life span in a sample of 10, 000: Dissociating ability and strategy. Psychological Science, 2 6 ( 9 ) , 1 4 9 7 – 1 5 1 0 . h t t p s : / / d o i . o r g / 1 0 . 1 1 7 7 / 0956797615594896

Franken, R. E., & Brown, D. J. (1995). Why do people like competition? The motivation for winning, putting forth efort, improving one’s performance, performing well, being instrumental, and expressing forceful/ aggressive behavior. Personality and Individual Diferences, 19(2), 175–184. https://doi.org/10.1016/ 0191-8869(95)00035-5

Frost & Sullivan. 2017 Global Information Security Workforce Study. (2017). Retrieved from https://www. isc2.org/-/media/Files/Research/GISWS-Report-Europe. a s h x ? l a = n & h a s h = 6BCA521488491848DBCF91E8F350DBE3E0A65367

Garcia, S. M., Tor, A., & Schif, T. M. (2013). The psychology of competition: A social comparison perspective. Perspectives on Psychological Science, 8(6), 634–650. https://doi.org/10.1177/1745691613504114

Gerow, J. E., Ayyagari, R., Thatcher, J. B., & Roth, P. L. (2013). Can we have fun@ work? The role of intrinsic motivation for utilitarian systems. European Journal of Information Systems, 22(3), 360–380. https://doi.org/10. 1057/ejis.2012.25

Haans, R. F., Pieters, C., & He, Z. L. (2016). Thinking about U: Theorizing and testing U-and inverted U-shaped relationships in strategy research. Strategic Management Journal, 37(7), 1177–1195. https://doi.org/10.1002/smj.2399

Hamari, J. (2015). Gamification-motivations & efects. [Doctoral Dissertation, Aalto University].

Hamari, J., Koivisto, J., & Sarsa, H. (2014). Does gamification work?–a literature review of empirical studies on gamification. Paper presented at the 2014 47th Hawaii International Conference on System Sciences, Waikoloa, Hawaii

Henderson, R. K., Snyder, H. R., Gupta, T., & Banich, M. T. (2012). When does stress help or harm? The efects of stress controllability and subjective stress response on stroop performance. Frontiers in Psychology, 3, 179. https://doi.org/10.3389/fpsyg.2012.00179

Hinz, O., Spann, M., & Hann, I.-H. (2015). Research note— can’t buy me love . . . or can i? Social capital attainment through conspicuous consumption in virtual environments. Information Systems Research, 26(4), 859–870. https://doi.org/10.1287/isre.2015.0596

Hirschberg, J., & Lye, J. (2004). Inferences for the extremum of quadratic regression models. The University of Melbourne.

Hirschheim, R., & Klein, H. K. (2012). A glorious and not-so-short history of the information systems field. Journal of the Association for Information Systems, 13 (4), 5. https://doi.org/10.17705/1jais.00294

Höllig, C. E., Tumasjan, A., & Welpe, I. M. (2018a). Individualizing gamified systems: The role of trait competitiveness and leaderboard design. Journal of Business Research, 106, 288–303. https://doi.org/10.1016/j.jbusres. 2018.10.046

Höllig, C. E., Tumasjan, A., & Welpe, I. M. (2018b). The interaction of trait competitiveness and leaderboard design-an experimental analysis of efects on perceptions and usage intention. Paper presented at the Proceedings of the 51st Hawaii International Conference on System Sciences, Waikoloa, Hawaii.

Hoorens, V., & Damme, C. V. (2012). What do people infer from social comparisons? Bridges between social comparison and person perception. Social and Personality Psychology Compass, 6(8), 607–618. https://doi.org/10. 1111/j.1751-9004.2012.00451.x

IBM Corp. Released 2016. IBM SPSS Statistics for Windows, Version 24.0. Armonk, NY: IBM Corp.

Inoue, Y., Takahashi, T., Burriss, R. P., Arai, S., Hasegawa, T., Yamagishi, T., & Kiyonari, T. (2017). Testosterone promotes either dominance or submissiveness in the Ultimatum Game depending on players’ social rank. Scientific Reports, 7(1), 5335. https://doi.org/10. 1038/s41598-017-05603-7

Johnson, D., & Johnson, R. (1975). Learning together and alone: Cooperation, competition, and individualization. Prentice-Hall.

Kapp, K. M. (2012). The gamification of learning and instruction: Game-based methods and strategies for training and education. John Wiley & Sons.

Ke, F., & Grabowski, B. (2007). Gameplaying for maths learning: Cooperative or not? British Journal of Educational Technology, 38(2), 249–259. https://doi.org 10.1111/j.1467-8535.2006.00593.x

Kilduf, G., Galinsky, A. D., Gallo, E., & Reade, J. J. (2012). Whatever it takes: Rivalry and unethical behavior. Paper presented at the 25th Annual Conference of International Association for Conflict Management, Stellenbosch, South Africa.

Kim, Y., & Steiner, P. (2016). Quasi-experimental designs for causal inference. Educational Psychologist, 51(3–4), 395–405. https://doi.org/10.1080/00461520.2016.1207177

Kohn, A. (1992). No contest: The case against competition. Houghton Miflin Harcourt.

Koivisto, J., & Hamari, J. (2019). The rise of motivational information systems: A review of gamification research.

International Journal of Information Management, 45, 191–210. https://doi.org/10.1016/j.ijinfomgt.2018.10.013

Landers, R. N., Collmus, A. B., & Williams, H. (2019). The greatest battle is within ourselves: An experiment on the efects of competition alone on task performance. International Journal of Human-computer Studies, 127, 51–61. https://doi.org/10.1016/j.ijhcs.2018.09.011

Landers, R. N., & Landers, A. K. (2014). An empirical test of the theory of gamified learning: The efect of leaderboards on time-on-task and academic performance. Simulation & Gaming, 45(6), 769–785. https://doi.org/10.1177/ 1046878114563662

Latané, B. (1966). Studies in social comparison— Introduction and overview. Journal of Experimental Social Psychology, 1, 1–5. https://doi.org/10.1016/0022- 1031(66)90060-6

Li, X., Hou, Z. J., & Jia, Y. (2015). The influence of socia comparison on career decision-making: Vocational identity as a moderator and regret as a mediator. Journal of Vocational Behavior, 86, 10–19. https://doi.org/10.1016/j. jvb.2014.10.003

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. Oxford Bulletin of Economics and Statistics, 72(1), 109–118. https://doi.org/10.1111/j.1468-0084.2009.00569.x

Liu, D., Li, X., & Santhanam, R. (2013). Digital games and beyond: What happens when players compete? MIS Quarterly, 37(1), 111–124. https://doi.org/10.25300/ MISQ/2013/37.1.05

Liu, D., Santhanam, R., & Webster, J. (2017). Toward meaningful engagement: A framework for design and research of gamified information systems. MIS Quarterly, 41(4), 1011–1034. https://doi.org/10.25300/MISQ/2017/41.4.01

Locander, D. A., Weinberg, F. J., Mulki, J. P., & Locander, W. B. (2015). Salesperson lone wolf tendencies: The roles of social comparison and mentoring in a mediated model of performance. Journal of Marketing Theory and Practice, 23(4), 351–369. https://doi.org/10. 1080/10696679.2015.1049680

MarketsandMarkets. (2017). Gamification market - global forecast to 2020. Seattle, Washington: MNM. Retrieved f r o m h t t p s : / / w w w . m a r k e t s a n d m a r k e t s . c o m / PressReleases/gamification.asp

Maslach, C., & Leiter, M. P. (2008). The truth about burnout: How organizations cause personal stress and what to do about it. John Wiley & Sons.

Mazur, A., Booth, A., & Dabbs, J. M., Jr. (1992). Testosterone and chess competition. Social Psychology Quarterly, 55(1), 70–77. https://doi.org/10.2307/2786687

Mekler, E. D., Brühlmann, F., Opwis, K., & Tuch, A. N. (2013). Do points, levels and leaderboards harm intrinsic motivation?: An empirical analysis of common gamifica tion elements. Paper presented at the Proceedings of the First International Conference on gameful design, research, and applications, Toronto, Canada.

Mekler, E. D., Brühlmann, F., Tuch, A. N., & Opwis, K. (2017). Towards understanding the efects of individual gamification elements on intrinsic motivation and performance. Computers in Human Behavior, 71, 525–534. https://doi.org/10.1016/j.chb.2015.08.048

Merriam-Webster Game (2020). In Merriam-Webster.com dictionary. Retrieved from https://www.merriam-webster.com/dictionary/game

Meyer, B. D. (1995). Natural and quasi-experiments in economics. Journal of Business and Economic Statistics, 13(2), 151–161. Retrieved from http://www.jstor.com/ stable/1392369

Mikalef, K., Giannakos, M. N., Chorianopoulos, K., & Jaccheri, L. (2013). Does informal learning benefit from interactivity? The efect of trial and error on knowledge acquisition during a museum visit. International Journal of Mobile Learning and Organisation 11, 7(2), 158–175. https://doi.org/10.1504/IJMLO.2013.055620

Mitra, S., & Chaya, A. K. (1996). Analyzing cost-efectiveness of organizations: The impact of information technology spending. Journal of Management Information Systems, 13(2), 29–57. https://doi.org/10. 1080/07421222.1996.11518122

National Science Foundation, 2020. Advancing Informal STEM Learning (AISL). Retrieved from https://www.nsf. gov/funding/pgm\_summ.jsp?pims\_id=504793

Nebel, S., Schneider, S., Beege, M., & Rey, G. D. (2017). Leaderboards within educational videogames: The impact of dificulty, efort and gameplay. Computers & Education, 113, 28–41. https://doi.org/10.1016/j.com pedu.2017.05.011

Okhuysen, G., & Bonardi, J-P. (2011). The Challenges of Building Theory by Combining Lenses. Academy of Management Review, 36(1), 6–12. Retrieved from https://doi.org/10.5465/amr.36.1.zok006

Orosz, G., Tóth-Király, I., Büki, N., Ivaskevics, K., Bőthe, B., & Fülöp, M. (2018). The four faces of competition: The development of the multidimensional competitive orientation inventory. Frontiers in Psychology, 9, 779. https:/ doi.org/10.3389/fpsyg.2018.00779

Palaus, M., Marron, E. M., Viejo-Sobera, R., & Redolar-Ripoll, D. (2017). Neural basis of video gaming: A systematic review. Frontiers in Human Neuroscience, 11, 248. https://doi.org/10.3389/fnhum.2017.00248

Pearl, J. (2009). Causal inference in statistics: An overview. Statistics Surveys, 3, 96–146. https://doi.org/10.1214/09- SS057

Peng, W., & Hsieh, G. (2012). The influence of competition, cooperation, and player relationship in a motor performance centered computer game. Computers in Human Behavior, 28(6), 2100–2106. https://doi.org/10.1016/j. chb.2012.06.014

Rodrigues, L. F., Oliveira, A., & Costa, C. J. (2016). Playing seriously–How gamification and social cues influence bank customers to use gamified e-business applications. Computers in Human Behavior, 63, 392–407. https://doi. org/10.1016/j.chb.2016.05.063

Ruf, H. A., & Lawson, K. R. (1990). Development of sustained, focused attention in young children during free play. Developmental Psychology, 26(1), 85. https://doi.org 10.1037/0012-1649.26.1.85

Ryan, R. M., & Deci, E. L. (2000). Intrinsic and extrinsic motivations: Classic definitions and new directions. Contemporary Educational Psychology, 25(1), 54–67. https://doi.org/10.1006/ceps.1999.1020

Sailer, M., Hense, J. U., Mayr, S. K., & Mandl, H. (2017). How gamification motivates: An experimental study of the efects of specific game design elements on psychological need satisfaction. Computers in Human Behavior, 69, 371–380. https://doi.org/10.1016/j.chb.2016.12.033

Salas, E., Wildman, J. L., & Piccolo, R. F. (2009). Using simulation-based training to enhance management education. Academy of Management Learning & Education, 8(4), 559–573. Retrieved from http://www. jstor.com/stable/27759193

Santhanam, R., Liu, D., & Shen, W.-C. M. (2016). Research Note —Gamification of technology-mediated training: Not all competitions are the same. Information Systems Research, 27(2), 453–465. https://doi.org/10.1287/isre.2016.0630

Scales, C. D. J., Moin, T., Fink, A., Berry, S. H., Afsar-Manesh, N., Mangione, C. M., & Kerfoot, B. P. (2016). A randomized, controlled trial of team-based competition to increase learner participation in quality-improvement education. International Journal for Quality in Health Care, 28(2), 227–232. https://doi.org/10.1093/intqhc/mzw008

Sepehr, S., & Head, M. (2018). Understanding the role of competition in video gameplay satisfaction. Information & Management, 55(4), 407–421. https://doi.org/10.1016/ j.im.2017.09.007

Shadish, W. R., Cook, T. D., & Campbell, D. T. (2002). Experimental and quasi-experimental designs for generalized causal inference. Houghton Miflin.

Shepard, H. A. (1954). The value system of a university research group. American Sociological Review, 19(4), 456–462. https://doi.org/10.2307/2087466

Shepherd, M. M., Briggs, R. O., Reinig, B. A., Yen, J., & Nunamaker, J. F., Jr. (1995). Invoking social comparison to improve electronic brainstorming: Beyond anonymity. Journal of Management Information Systems, 12(3), 155–170. https://doi.org/10.1080/07421222.1995.11518095

Simões, J., Redondo, R. D., & Vilas, A. F. (2013). A social gamification framework for a K-6 learning platform. Computers in Human Behavior, 29(2), 345–353. https:// doi.org/10.1016/j.chb.2012.06.007

Spence, J. T., & Helmreich, R. (1983). Achievement and achievement motives: Psychological and sociological approaches. W.H. Freeman.

Stuart, E. A., & Rubin, D. B. (2008). Best practices in quasi-experimental designs. In J. Osborne (Ed.), Best Practices in Quantitative Social Science (pp. 155–176). Thousand Oaks, CA: Sage. Retrieved from http://citeseerx.ist.psu.edu/viewdoc/download? doi=10.1.1.584.1057&rep=rep1&type=pdf

Suh, A., Wagner, C., & Liu, L. (2016). Enhancing user engagement through gamification. Journal of Computer Information Systems, 8(3), 204–213. doi:10.1080/ 08874417.2016.1229143.

Sutton, R. I., & Hargadon, A. (1996). Brainstorming groups in context: Efectiveness in a product design firm. Administrative Science Quarterly, 41(4), 685–718. https://doi.org/10.2307/2393872

Teigen, K. H. (1994). Yerkes-Dodson: A law for all seasons. Theory & Psychology, 4(4), 525–547. https://doi.org/10. 1177/0959354394044004

Tsay, C.-H.-H., Kofinas, A., & Luo, J. (2018). Enhancing student learning experience with technology-mediated gamification: An empirical study. Computers & Education, 121, 1–17. https://doi.org/10.1016/j.compedu.2018.01.009

van Zadelhof, M. (2017). Cybersecurity Has a Serious Talent Shortage. Here’s How to Fix It. Harvard Business Review. Retrieved from https://hbr.org/2017/05/cyberse curity-has-a-serious-talent-shortage-heres-how-to-fix-it

Varian, H. R. (2016). Causal inference in economics and marketing. Proceedings of the National Academy of Sciences, 113(27), 7310–7315. https://doi.org/10.1073/ pnas.1510479113

Vorderer, P., Hartmann, T., & Klimmt, C. (2003). Explaining the enjoyment of playing video games: The role of competition. Paper presented at the Proceedings of the Second International Conference on Entertainment Computin., Pittsburgh, Pennsylvania.

Wang, A. I. (2015). The wear out efect of a game-based student response system. Computers & Education, 82, 217–227. https://doi.org/10.1016/j.compedu.2014.11.004

Wang, J., Chen, R., Herath, T., & Rao, H. (2009). Visual e-mail authentication and identification services: An investigation

of the efects on e-mail use. Decision Support Systems, 48(1), 92–102. https://doi.org/10.1016/j.dss.2009.06.012

Warkentin, M., Johnston, A. C., & Shropshire, J. (2011). The influence of the informal social learning environment on information privacy policy compliance eficacy and intention. European Journal of Information Systems, 20(3), 267–284. https://doi.org/10.1057/ejis.2010.72

Wills, T. A. (1981). Downward comparison principles in social psychology. Psychological Bulletin, 90(2), 245. https://doi. org/10.1037/0033-2909.90.2.245

Yang, J. C., Quadir, B., & Chen, N.-S. (2016). Efects of the badge mechanism on self-eficacy and learning performance

in a game-based English learning environment. Journal of Educational Computing Research, 54(3), 371–394. https:// doi.org/10.1177/0735633115620433

Yerkes, R. M., & Dodson, J. D. (1908). The relation of strength of stimulus to rapidity of habit-formation. Journal of Comparative Neurology, 18(5), 459–482. doi:10.1002/ cne.920180503

Zainuddin, Z., Shujahat, M., Haruna, H., & Chu, S. K. W. (2020). The role of gamified e-quizzes on student learning and engagement: An interactive gamification solution for a formative assessment system. Computers & Education, 145, 103729. https://doi.org/10.1016/j.compedu.2019.103729
