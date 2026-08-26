---
otero_id: 25854
otero_key: "ABTRPPKX"
title: "Effects of introducing an online community in a crowdsourcing contest platform"
authors: "Jonathan (Hua) Ye; Matthew Jensen"
year: "2022"
journal: "Information Systems Journal"
doi: "10.1111/isj.12397"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
R E S E A R C H A R T I C L E

# Effects of introducing an online community in a crowdsourcing contest platform

Jonathan (Hua) Ye | Matthew Jensen

MIS Division, Price College of Business, University of Oklahoma, Norman, Oklahoma, USA

## Correspondence

Jonathan (Hua) Ye, MIS Division, Pric College of Business, University of Oklahoma, 307 W. Brooks, Suite 307E, Norman, OK 73019, USA.

Email: jonathan.ye@ou.edu

## Abstract

Crowdsourcing platform owners and operators constantly search for ways to improve contestant performance. One novel proposal for improving performance is the introduction of an online community to the crowdsourcing contest platform. However, research regarding the potential benefits of an online community on such platforms is unclear. Furthermore, prior research often assumes the single dimensionality of prior experience, whose impacts on crowdsourcing performance are also inconclusive. Building on knowledge collaboration and cognitive diversity research, we model the direct effects of introducing an online community on contestant performance and the moderating effects of the amount of experience and experience diversity. Leveraging a natural quasi-experiment in a large crowdsourcing contest platform, we collected 24 months of contestant data to test our hypotheses. Our propensity score matching and difference in differences analysis demonstrated that contestants' performance (winning contests and crowdsourcing income) increases significantly with the presence of an online community. Additionally, the positive effect of an online community on performance is more pronounced for contestants with less experience and those with more diverse experience. Our findings provide insights into the causality of incorporating an online community and inform community investment decisions for crowdsourcing contest platforms.

K E Y W O R D S

cognitive diversity, crowdsourcing contest, experience amount,

experience diversity, knowledge collaboration, online community

## 1 | INTRODUCTION

Contests are a popular form of crowdsourcing, where temporary online crowds (contestants) can be deployed to work on a variety of tasks for seeker firms (Jian et al., 2019; Mo et al., 2021). These crowdsourcing contests have generated innovative solutions for a variety of seeker firms and the global industry is excepted to grow to nearly \$155 billion in the next five years (Absolute Market Insights, 2020). However, crowdsourcing contests are not with out drawbacks. Intense competition can make contestants economise their effort and constrain their idea expression thereby affecting solution quality (Boudreau et al., 2011; Boudreau et al., 2016; Hofstetter et al., 2021). The uncer tainty inherent in such further decreases contestants' investment and hence their performance (Jian et al., 2019) Widespread poor contestant performance can deter seeker firms (Blohm et al., 2013) and damage platform viabilit (e.g., the bankruptcy of Quirky) (Fixson & Marion, 2016).

To counter this tendency in crowdsourcing contests, platform owners and seeker firms have begun exploring novel ways to improve the quality of contestants' submissions (Nevo & Kotlarsky, 2020). Researchers have joined in this exploration by systematically examining contestant motivations (Boons et al., 2015; Ye & Kankanhalli, 2017; Zheng et al., 2011) and the processes contestants use to innovate (e.g., remixing) (Han et al., 2020). But a recent, and seemingly paradoxical, addition has drawn significant interest: introduction of an online community within the crowdsourcing platform. Several prominent platforms (e.g., TopCoder, Kaggle) have invested to develop online com munities, providing a virtual space for knowledge collaboration and socialisation (Faraj et al., 2016). In these virtua spaces, contestants share knowledge, make friends, and ask or answer questions posted to the community; but the also compete against each other as contestants. Therefore, these platforms are sometimes called communitition platforms (Hutter et al., 2011). Past research has shown that online communities are a valuable source of outside solu tions (Majchrzak & Malhotra, 2016; Riedl & Seidel, 2018) that help produce organisational competitive advantages (Nagle, 2018). However, the collaborative nature of online communities is seemingly at odds with the competitiv structure and design of crowdsourcing contest platforms (Boudreau et al., 2011). Presumably, contestants who are rewarded to compete against one another would have little incentive to work together.

Scholars have begun to probe how online communities can alter crowdsourcing contest platforms and whethe these communities ultimately serve to improve the outcomes of crowdsourcing contests. For example, contestant have been shown to share knowledge and help each other, even in highly competitive contests (Dissanayake et al., 2021). Interaction between platform members can increase remixing of ideas to form new innovation (Stanko, 2016) and competition outcomes improve as contestants share high-quality and generative knowledge (Jin et al., 2021). However, such sharing may anchor contestants to publicly known approaches to contests and thus sup press innovative, high-quality submissions (Boudreau et al., 2011; Hofstetter et al., 2021). Furthermore, contestants demonstrate amoral manipulation, status seeking behaviour, and distrust of others on crowdsourcing platforms deriving increases in the number of ideas, number of comments, and quality of contributions from general distrust (Hutter et al., 2015). In other words, collaboration may not increase contestant performance. Prior research has also demonstrated clear intracommunity benefits for members' knowledge generation (e.g., Kane & Ransbotham, 2016 Kim et al., 2018). However, clear evidence for whether these benefits spill over to contestants on a crowdsourcing platform following introduction of an online community remains elusive (see Appendix A). Thus, it remains unknow if offering a space for collaboration (i.e., an online community) helps improve contestant performance (see Table 1).

Our primary research question is RQ1: How does the introduction of an online community in a crowdsourcing con test platform affect contestant performance? To explore spillover effects from the introduction of an onlin community, we integrate concepts from knowledge collaboration research (KCR) (e.g., Faraj et al., 2016) and empiri cal findings from crowdsourcing contest research to develop arguments suggesting that the introduction of an online community improves contestant performance. Specifically, we argue that through knowledge exchange and socialisation, contestants who participate in the online community will perform better in contests, as measured b number of winning contests (Bockstedt et al., 2016; Jeppesen & Lakhani, 2010) and the amount of prizes wo (Terwiesch & Xu, 2008).

T A B L E 1 Research positioning and contributions

<table><tr><td></td><td colspan="2">In-house assumption</td><td>Root metaphor assumption</td><td>Paradigmatic assumption</td></tr><tr><td>The literature</td><td>Knowledge collaboration research can explain intra-community outcomes, that is, knowledge reuse, contribution, or consumption</td><td>Everyone benefits equally from participating in an online community</td><td>Prior experience is a unidimensional construct.</td><td>Collaboration may not help in contest platforms</td></tr><tr><td>This study</td><td>Knowledge collaboration research can explain contestant crowdsourcing performance (extra-community outcomes)</td><td>Contestants benefit differently from participating in an online community</td><td>Prior experience comprises two distinct dimensions, that is, experience amount and experience diversity</td><td>Offering a space for collaboration is helpful for crowdsourcing contests</td></tr><tr><td>Contribution</td><td>·Identify the spillover effects of knowledge collaboration research·Extend the applicability of knowledge collaboration research</td><td>·Identify the contingencies of knowledge collaboration research</td><td>·Reconceptualize prior experience into two dimensions</td><td>·Test the effects of communion·Test the impacts of an online community artefact·Offer guidelines on if contest platforms should invest in building an online community</td></tr></table>

Prior research (e.g., Faraj et al., 2011; Faraj et al., 2016) has implicitly assumed that online communities will ben efit participants equally. However, the spillover effects from the introduction of an online community may not be uni form for all contestants – there may be boundary conditions. Prior research has demonstrated that online communities outside of crowdsourcing platforms effectively socialise (Liu et al., 2020) and bring newcomers up to speed (Kim et al., 2018) so they can be contributing members of the community. Crowdsourcing literature has shown that succeeding in contests depends heavily on the amount of prior contest experience (Huang et al., 2014; Liu et al., 2020), from which contestants learn how to improve their performance (Bockstedt et al., 2016; Riedl & Seidel, 2018). These findings suggest that online communities may be especially beneficial for contestants with little experience, but amount is only one dimension of experience. Prior research has also noted the importance of experi ence diversity (Bayus, 2013; Honoré, 2021; Wang & Hahn, 2015) and the introduction of an online community coul also interact with experience diversity to alter contestant performance. However, newcomers to an online commu nity on a contest platform may be unwelcome by the contestants already on the platform since more contestant mean more competition and the potential for lower rewards (Boudreau et al., 2011). Therefore, we pose a related research question: RQ2: How does experience amount and experience diversity interact with the introduction of an onlin community to affect contestant performance? To address the second research question, we draw on cognitive diver sity research (CDR) (e.g., Horn, 1989; Miller et al., 1998) to hypothesize distinct moderating effects of experience diversity and amount (see Appendix D for the rationale of integrating KCR with CDR)

Our study examined these research questions using a natural quasi-experiment created when a large crowdsourcing contest platform rolled out a new online community. We used propensity score matching (PSM) and a difference-in-differences (DID) approach to analyse panel data over a 24-month window centered at the mont when the online community was introduced. We identified a sample of 122 contestants who participated in the new online community and paired them with 122 contestants who never registered in the community during the window of our study. We then gathered 5856 observations from these contestants to test the model.

Empirical results demonstrated that, holding other variables constant, the number of winning contests and the amount of crowdsourcing income increased significantly for contestants who participated in the online community after its introduction. Thus, we observed the spillover effects from the introduction of an online community on contestant performance. We further demonstrated that amount and diversity are distinct dimensions of contestant experience and that participants in online communities benefit differentially. Contestants with less experienc benefited more from the introduction of a community in terms of winning contests and crowdsourcing income, rela tive to those with more experience. In addition, contestants with diverse experience benefited more from the com munity introduction than those with less diverse experience.

Findings of this study directly address the assumptions and contradictory findings of past crowdsourcing contest lit erature and offer direct evidence of positive spillover effects outside of an online community. Our results extend earl communitition research (Hutter et al., 2011), illustrating the viability of joining online communities with crowdsourcin contest platforms and demonstrating the likely benefit to contestants (see Table 1). These findings are relevant to plat form owners investigating techniques to improve the quality and vibrancy of crowdsourcing contest platforms. These findings will also benefit developers trying to figure out the functions of an online community that are conducive to th success of contest platforms as well as contestants trying to decide on whether to participate in a community.

## 2 | CONCEPTUAL BACKGROUND

## 2.1 | Prior crowdsourcing research

Through crowdsourcing contests, firms can gain access to a large pool of contestants for problem-solving and miti gate the risk of failures for seeker firms (Allen et al., 2018; Wang et al., 2017; Ye & Kankanhalli, 2015). Although con tests can solicit a diverse set of potential solutions, several factors can limit the utility of crowdsourcing contes platforms. For example, competition encourages contestants to economise their effort, constrain their idea expres sion, and reduce solution quality (Boudreau et al., 2011; Boudreau et al., 2016; Hofstetter et al., 2021). The uncer tainty inherent in such contests threatens contestants' investment in producing high-quality solutions (Jian et al., 2019).

To preserve and enhance the utility of crowdsourcing contest platforms, past research has explored the anteced ents to contest performance in several ways (Bockstedt et al., 2016; Jeppesen & Lakhani, 2010; Terwiesch & Xu, 2008; Wooten & Ulrich, 2017). One novel approach has led some crowdsourcing contest platform (e.g., TopCoder, Kaggle) to support greater collaboration among their contestants by facilitating knowledge exchange on their platforms. Online communities have been shown to facilitate knowledge collaboration and individual learning (Faraj et al., 2011; Faraj et al., 2016). But unlike a collaborative crowdsourcing platform, of which an online com munity is a part (Liu et al., 2020; Shah & Nagle, 2019), there is typically minimal knowledge sharing and collaboration in a crowdsourcing contest platform (Majchrzak & Malhotra, 2016). Participants in crowdsourcing contests compete with each other for prizes and traditionally have little interaction and rarely share information with each othe (Jeppesen & Lakhani, 2010; Shah & Nagle, 2019).

Proponents of communitition platforms (that host competitions and an online community) (Hutter et al., 2011) argue that the benefits of online communities will spill over to contestants and improve their performance. Recent research has demonstrated that contestants help each other, even in highly competitive contests, and this help i often reciprocated (Dissanayake et al., 2021). This exchange of help improves contestant performance (Dissanayake et al., 2021), especially as contestants share high-quality and generative knowledge (Jin et al., 2021), and interaction between contestants also increases the remixing of ideas to form new innovations (Stanko, 2016). But past researc has yet to examine the effects of introducing an online community to a crowdsourcing contest platform (se Appendix A for a review). Instead, much of what is known about communitition platforms comes from examining knowledge exchange occurring within individual contests. Without direct observation of the introduction of an onlin community, examining spillover effects from the online community to contestant performance is clouded. Contes tants demonstrate amoral behaviour, seek status, and display general distrust for others on crowdsourcing platform (Hutter et al., 2015), which can also undermine the benefits of an online community as a technique to elevate con testant performance. With potential benefits of online communities on one side, the potential undermining effect of competition on the other side, and clouded observation of their coupling, the consequences of introducing an online community to a crowdsourcing contest platform as a way to improve contestant performance remain unclear.

Furthermore, scholars studying communities in contest platforms have begun to note contingencies and bound ary conditions that moderate the effect of online communities on contestant performance. For example, knowledg sharing, by itself, does not necessarily improve crowdsourcing contestant performance (Yang et al., 2008). Instead performance improvement is contingent on volume, quality, and generativity of shared knowledge (Jin et al., 2021) Early research on crowdsourcing performance identified prior experience among the most significant predictors of success (Bayus, 2013; Huang et al., 2014). However, additional examination revealed a more nuanced relationship between experience and contest performance with some positive (Bayus, 2013; Huang et al., 2014; Wang & Hahn, 2015), negative (Bayus, 2013; Hofstetter et al., 2021), inverted-U (Liu et al., 2020), and no impacts (Archak & Ghose, 2010; Yang et al., 2008). Such mixed findings could be due to the conceptualization of prior experienc (experience amount) as a single dimension, rather than viewing it in terms of two distinct aspects (i.e., experience amount and experience diversity). While experience amount has been recognised as an important component o prior experience (Huang et al., 2014; Liu et al., 2020), experience diversity has received relatively less attention (Bayus, 2013).

One of the key benefits of online communities is the learning and experience new participants develop as they engage with the community (Archak & Ghose, 2010; Chen et al., 2018; Jin et al., 2021; Mamykina et al., 2016). So, the introduction of an online community to a crowdsourcing contest platform may disproportionally benefit les experienced contestants. However, less experienced contestants deepening their knowledge may contribute to greater competition, which has been shown to constrain idea expression and reduce solution quality (Boudrea et al., 2011; Boudreau et al., 2016; Hofstetter et al., 2021). Furthermore, previous conceptualizations of experience have neglected its multiple dimensions (e.g., amount and diversity). Thus, the moderating effect of experience in communitition platforms remains unclear.

## 2.2 | Knowledge collaboration

Online communities are digital spaces of knowledge collaboration (Faraj et al., 2016), where users work collabora tively, voluntarily, and with minimal oversight to freely and openly develop and exchange knowledge for a common interest (Shah & Nagle, 2019). Online knowledge collaboration refers to individual acts of offering knowledge to others as well as adding to, recombining, modifying, and integrating knowledge that others have contributed to user communities (Faraj et al., 2011). Knowledge collaboration can take various forms. It could involve a user posting a question or an idea and then engaging in the process of reflecting on incoming responses and postings that clarif questions or ideas (von Krogh, 2012; Wasko & Faraj, 2005). It could also involve users engaging in editing contributions (Jarvenpaa & Majchrzak, 2010). Another form involves providing feedback on the knowledge contributed (Faraj et al., 2011). The knowledge collaboration research posits that users can collaborate with each other in knowledge creation and obtain better performance through participating in a community (Faraj et al., 2011)

Knowledge collaboration research also argues that the online sociality of an online community helps improve effectiveness in knowledge collaboration. Online sociality refers to individuals' tendency to relate to others, buil social ties, and organically assemble online (Faraj et al., 2016). The sociality of a community assists users around the globe to locate gatherings of interest, connect with similar relevant others, and enable generative communal engage ment (Felin et al., 2017; Ma & Agarwal, 2007). It facilitates the sharing of explicit knowledge and, more importantly supports the sharing of tacit knowledge (competence and experience) via the formation of a socialisation bond (e.g., swift trust), connection through the interaction history, shared goals, and community identity (Fara et al., 2016). Thus, it improves user effectiveness in collecting, integrating, and remixing knowledge in communities.

Past literature adopting the knowledge collaboration research finds that online communities can help generat better content (e.g., Ransbotham & Kane, 2011; Ransbotham et al., 2012), produce innovative ideas (Majchrzak & Malhotra, 2016; Ye et al., 2016), and facilitate learning (Nagle, 2018; Ye, 2022). For example, Ransbotham and Kane (2011) report that collaboration between new and experienced users in Wikipedia affects the success of content generation in terms of the articles being featured as ‘best articles’. Per this literature, effective knowledge collabora tion results in improved or refined knowledge, better content, and quality ideas for participants. Therefore, we expect that the introduction of an online community may improve knowledge collaboration among contestants an hence affect their performance.

Knowledge collaboration research has focused tightly on the benefits within online communities (Kim et al., 2018), with benefits mentioned above flowing to community members. However, knowledge collaboration research has yet to examine external effects of online communities. In other words, the potential benefits of spillover effects from online communities remain unclear. Moreover, scholars investigating knowledge collaboration that occurs in online communities often assume an even distribution of benefits (e.g., learning, social support) (Fara et al., 2011; Liu et al., 2020). Such assumptions are often implicit and evidenced by ignoring potential moderator that could alter the flow of benefits. In crowdsourcing contest literature, scholars have already uncovered importan antecedents to contest performance, antecedents which could interact with the introduction of an online commu nity. To explore potential contingencies for knowledge collaboration, we next turn to cognitive diversity research

## 2.3 | Cognitive diversity

The cognitive diversity research suggests that individuals with various contest experience would benefit more from collaboration (Horn, 1989; Miller et al., 1998; Olson et al., 2007), for example, knowledge collaboration in communities. It posits that individuals from different backgrounds or of various experience have diverse cognition and per spectives, which contribute to their work performance (Horn, 1989; Miller et al., 1998). On the one hand, cognitiv diversity stimulates individuals' creativity by activating concepts and topics that otherwise would not be activated and facilitating the subsequent recombination of such activated concepts into new ideas (Dennis & Valacich, 1993; Hofstetter et al., 2021). On the other hand, cognitive diversity helps prevent cognitive fixation in individuals and organisations (Bayus, 2013). With reduced cognitive fixation, individuals are likely to produce more creative solution (Liu et al., 2020).

Cognitive diversity can be derived from the diversity of past experience (Honoré, 2021; Wang & Hahn, 2015) Individuals with a variety of experience have diverse knowledge components, which can be combined into creative solutions (Boone & Hendriks, 2009; Taylor & Greve, 2006). Diverse experience equips individuals with multiple cog nitive templates for solution formation (Honoré, 2021). Besides experience diversity, experience amount matters as it determines the availability and salience of past experience for future reference (Boh et al., 2007; Boone & Hendriks, 2009). Greater experience exposes individuals to a variety of problems and solutions, increasing thei familiarity of certain idea characteristics (Archak & Ghose, 2010; Liu et al., 2020). However, rather than increasing cognitive diversity, greater but less diverse experience may bring to individuals cognitive fixation, harming creativ performance (Bayus, 2013; Liu et al., 2020). Therefore, we explore the moderating impacts of both experience diver sity and amount in this study.<sup>1</sup>

## 3 | RESEARCH MODEL AND HYPOTHESIS DEVELOPMENT

Based on the knowledge collaboration research, we model the direct impacts of introducing an online communit into a crowdsourcing contest platform on contestant performance. Contestant performance refers to the number of winning contests and the amount of crowdsourcing income. Drawing from the cognitive diversity research, w hypothesize the moderating effects of experience amount and diversity. All hypotheses are developed at the contes tant level.

## 3.1 | Introduction of an online community

Knowledge collaboration in an online community allows contestants to create new knowledge (Majchrzak & Malhotra, 2016) and solve problems that they cannot otherwise (Faraj et al., 2011; Faraj et al., 2016). It also allows individuals to contribute to common projects and learn from this process to improve their performance (Fara et al., 2011; Nagle, 2018; Ye et al., 2016). Furthermore, online sociality of an online community encourages contes tants to share knowledge with each other and peers to assess generated ideas for innovation (Faraj et al., 2016; Feli et al., 2017). This helps improve contestants' social capital in the community and professional skills (Felin et al., 2017 Ma & Agarwal, 2007).

Prior research exploring communitition has demonstrated that sociality and knowledge exchange are resilient in the presence of competitive pressures that could curtail collaboration and interaction (Dissanayake et al., 2021; Jin et al., 2021). In extending this recent work, we expect that an online community can complement a crowdsourcing contest platform by bringing in the benefits of online sociality and online knowledge collaboration, which assist th generation of quality solutions and contribute to success in crowdsourcing contests. Conversely, with the absence of an online community, contestants cannot reap the benefits of knowledge collaboration. Thus, we propose testing direct, positive spillover effect from the introduction of an online community. Hence, we propose:

Hypothesis 1. The introduction of an online community positively affects contestant performance in terms of (a) the number of winning contests and (b) the amount of crowdsourcing income

## 3.2 | Experience amount

Experience amount refers to the number of contests that contestants have participated in before. Past literature sug gests that contestants can pick up knowledge and skills from their experience to improve their performance (Bockstedt et al., 2016; Riedl & Seidel, 2018; Ye, 2022). In general, contestants gain knowledge and skills by performing tasks themselves and rating others' work (Riedl & Seidel, 2018). Past crowdsourcing literature has foun empirical evidence that individuals tend to replicate past solutions to new tasks (Jin et al., 2021) and hence increase the number of submissions (Archak & Ghose, 2010; Bayus, 2013; Li et al., 2016). However, greater prior experience (regardless of success or failure experience) does not necessarily improve contestants' likelihood of succes (Bayus, 2013; Bockstedt et al., 2016), that is, performance. The literature finds that the more contest experience contestants have (assuming such experience is not diverse), the more likely they will rely on such experience for solutio generation, resulting in cognitive fixation (Bayus, 2013; Liu et al., 2020). Cognitive fixation limits contestants' ability to propose novel ideas (Liu et al., 2020) and their likelihood of winning the contest (Hofstetter et al., 2021). A simila phenomenon, the capability-rigidity paradox, occurs in management where individuals tend to exploit existing com petence, which crowds out exploration and limits innovation (Atuahene-Gima, 2005; Leonard-Barton, 1992)

The introduction of an online community provides a venue for contestants to explore new possibilities to develop contest solutions (Riedl & Seidel, 2018). Contestants with a greater amount of experience tend to have confidence in their own capability and are more likely to experience cognitive fixation (Bayus, 2013; Bockstedt et al., 2016). Con versely, contestants with less experience are less likely to suffer from cognitive fixation (Bayus, 2013). They are mor open to referring to external information to inform their solutions or to evaluate the appropriateness of their solution (Liu et al., 2020). Thus, contestants with a less amount of experience are likely to look for needs-related and means related knowledge as well as needed emotional support in the community (Chen et al., 2019). As a result, they are likel to come up with novel ideas and are more likely to win contests. Following the above logic, contestants with a greater amount of experience are less likely to explore the online community for new knowledge and hence should benefit les from interacting with others with similar interests in the community. Therefore, we hypothesize

Hypothesis 2. Experience amount negatively moderates the relationship between the introduction of an online community and contestant performance in terms of (a) the number of winning contests and (b) the amount of crowdsourcing income.

## 3.3 | Experience diversity

Experience diversity refers to the variety of contests that contestants have participated in before. The cognitiv diversity research suggests that diverse experience can expose individuals to relevant, but heterogeneous knowledg during the idea generation process, stimulate creativity, and prevent cognitive fixation (Boone & Hendriks, 2009; Horn, 1989; Miller et al., 1998). Such diversity is normally linked to individual innovation and performance (Bayus, 2013; Koh, 2019; O'leary et al., 2011). Past crowdsourcing literature has provided empirical evidence tha diverse experience is conducive to crowdsourcing success (Bayus, 2013; Riedl & Seidel, 2018)

With the presence of an online community, the online knowledge collaboration allows users with diverse experi ence to contribute to, comment on, and rate the knowledge repositories of the community (Faraj et al., 2011). Activi ties such as sharing, commenting, and rating can all contribute to the success of crowdsourcing (Bayus, 2013 Bockstedt et al., 2016; Riedl & Seidel, 2018). Contestants with diverse experience are likely to interact and engage with various types of contestants in the online communities (Bayus, 2013). As contestants interact more in communi ties, they are exposed to more diverse knowledge and likely receive more performance benefits (Nagle, 2018). Fo example, they can recombine diverse knowledge to generate ideas of higher quality (Singh & Fleming, 2010). Fur thermore, the sociality of an online community facilitates the sharing of diverse experience that contains tacit knowl edge and the development of innovative solutions (Faraj et al., 2016; Felin et al., 2017). Conversely, contestants with less diverse experience are likely to interact with a smaller group of contestants in the online community. Thus, the are likely to derive fewer benefits as they interact and engage with fewer others with similar interests in the commu nity. Such a limitation may limit creative performance of contestants. Hence, we hypothesize:

Hypothesis 3. Experience diversity positively moderates the relationship between the introduction of an online community and contestant performance in terms of (a) the number of winning contests and (b) the amount of crowdsourcing income.

## 4 | RESEARCH CONTEXT AND DATA

## 4.1 | Research context

Our research context is a large crowdsourcing contest platform in China, ZBJ.com. ZBJ.com is an ideal context to test our model for three reasons. First, ZBJ.com was founded in 2006 and is among the largest contest crowdsourcing platforms with over 19 million registered users.<sup>2</sup> This contest platform affords users to participate in contest tasks and win prizes (Feng et al., 2018). Tasks include logo and virtual identity design, programming, advertisement design marketing, animation design, and so forth. Second, an important advantage of this research context is the occurrence of a natural experiment resulting from the launch of an online community<sup>3</sup> on 7 February 2018.<sup>4</sup> This community contains forums for users to interact, discuss various topics, pose and answer questions, and learn from each other. Third, ZBJ.com now includes both contests and the online community. This is an ideal context to isolate the impacts of the introduction of an online community on the performance of crowdsourcing contestants. Platform and community screenshots with Google translate are shown in Appendix B (Figures B1 and B2).

## 4.2 | Data and measures

Our analysis approach is a quasi-experiment. We collected data on contestants' crowdsourcing activities from this ZBJ.com from 1 February 2017, to 28 February 2019. Launching an online community was an exogenous shock to platform users in the form of system changes. We defined the period from 1 February 2017 to 31 January 2018, as the pretreatment stage and the period from 1 March 2018 to 28 February 2019, as the post-treatment stage.<sup>5</sup>

## 4.2.1 | Dependent variables

We measured the contestants' performance using the number of winning contests and the amount of crowdsourcing income. Winning Contests refers to the number of contests that contestant i won in month t. Crowdsourcing Income refers to the amount of crowdsourcing income contestant i earned in month t. We coded t as the numbe of months elapsed since 1 February 2017.

## 4.2.2 | Independent variables

We are interested in how contestants' crowdsourcing performance changed after they joined the online communit by signing up for forum discussions compared with those who did not sign up. We captured contestants who signed up for forum discussion as the Treatment group. If contestant i signed up for the forum, the Treatment is 1; otherwise, 0. We limited our analysis to participants who joined the online community the first month it was introduce or those who did not join at all. Because contestants signed up for the forum at various times in the first month, we measured the treatment period as Post-treatment . Post-treatment is 1, when contestant i signed up in month t; oth erwise, 0. We measured the amount of prior experience as experience amount and the diversity of prior experienc as experience diversity Experience quantity is the number of contests contestant i has solved before month t. Expe rience diversity refers to the number of types of contests contestant i has participated before month t. Contest tasks include logo design, translation, programming, marketing campaigns, animation design, among others. Adapting from prior studies (Bayus, 2013), we measured experience diversity with an entropy measure over the contest types $- \sum _ { j } p _ { j }$ ln (p ), where p is the proportion of contests of type j that the contestant i undertook before month t.

## 4.2.3 | Control variables

We also considered additional variables that could have affected our dependent variables. We included dummy vari ables for each month for the time window of our data collection to control for time-specific effects. We also included the number of months contestants were on the platform (platform tenure), gender (male = 1), and the number of posts that the contestant contributed to the forum (forum contribution) as controls.

## 4.3 | Empirical estimations

Table 2 presents the descriptive statistics of contestants, and Table 3 presents the correlation among variables. We randomly selected contestants in the treatment group during this period (1 March 2018, to 28 February 2019). The

T A B L E 2 Descriptive statistics

<table><tr><td>Variable</td><td>Mean</td><td>Std. dev.</td><td>Min</td><td>Max</td></tr><tr><td>Ln(Winning Contest)</td><td>1.867</td><td>1.249</td><td>0</td><td>4.406</td></tr><tr><td>Treatment</td><td>0.500</td><td>0.500</td><td>0</td><td>1</td></tr><tr><td>Post-treatment</td><td>0.500</td><td>0.500</td><td>0</td><td>1</td></tr><tr><td>Gender</td><td>0.774</td><td>0.214</td><td>0</td><td>1</td></tr><tr><td>Ln(Forum Contribution)</td><td>0.054</td><td>0.270</td><td>0</td><td>3.178</td></tr><tr><td>Ln(Experience Amount)</td><td>2.804</td><td>0.767</td><td>0</td><td>6.383</td></tr><tr><td>Ln(Experience Diversity)</td><td>0.213</td><td>0.268</td><td>-0.172</td><td>0.356</td></tr><tr><td>Ln(Platform Tenure)</td><td>2.471</td><td>0.547</td><td>1.945</td><td>4.219</td></tr><tr><td>Ln(Crowdsourcing Income)</td><td>8.168</td><td>1.576</td><td>2.397</td><td>12.771</td></tr></table>

T A B L E 3 Correlation matrix

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td></tr><tr><td>1. Ln(Crowdsourcing Income)</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Ln(Experience Amount)</td><td>0.538</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Ln(Platform Tenure)</td><td>0.045</td><td>0.012</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Ln(Forum Contribution)</td><td>0.034</td><td>0.030</td><td>-0.113</td><td>1.000</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Ln(Experience Diversity)</td><td>0.302</td><td>0.527</td><td>-0.502</td><td>0.132</td><td>1.000</td><td></td><td></td><td></td><td></td></tr><tr><td>6. Treatment</td><td>0.017</td><td>0.025</td><td>-0.151</td><td>0.223</td><td>0.444</td><td>1.000</td><td></td><td></td><td></td></tr><tr><td>7. Post-treatment</td><td>0.056</td><td>0.047</td><td>-0.058</td><td>0.162</td><td>0.050</td><td>0.090</td><td>1.000</td><td></td><td></td></tr><tr><td>8. Ln(Winning Contests)</td><td>0.554</td><td>0.636</td><td>-0.089</td><td>0.098</td><td>0.425</td><td>0.160</td><td>0.189</td><td>1.000</td><td></td></tr><tr><td>9. Gender</td><td>0.234</td><td>0.125</td><td>0.112</td><td>-0.14</td><td>-0.10</td><td>0.020</td><td>0.010</td><td>0.152</td><td>1.000</td></tr></table>

T A B L E 4 Summary statistics of control and treat group before and after matching

<table><tr><td>Variable</td><td>Sample</td><td>Treatment group</td><td>Control group</td><td>Difference</td><td>S.E.</td><td>T-test</td></tr><tr><td rowspan="2">Ln(Winning Contests)</td><td>Unmatched</td><td>2.072</td><td>1.388</td><td>0.684</td><td>0.288</td><td>2.370</td></tr><tr><td>Matched</td><td>2.050</td><td>2.013</td><td>0.037</td><td>0.042</td><td>0.890</td></tr><tr><td rowspan="2">Ln(Platform Tenure)</td><td>Unmatched</td><td>1.734</td><td>1.954</td><td>-0.220</td><td>0.004</td><td>-57.180</td></tr><tr><td>Matched</td><td>1.754</td><td>1.730</td><td>0.024</td><td>0.019</td><td>1.220</td></tr><tr><td rowspan="2">Gender</td><td>Unmatched</td><td>0.753</td><td>0.708</td><td>0.045</td><td>0.072</td><td>6.100</td></tr><tr><td>Matched</td><td>0.757</td><td>0.775</td><td>-0.018</td><td>0.012</td><td>0.620</td></tr><tr><td rowspan="2">Ln(Crowdsourcing Income)</td><td>Unmatched</td><td>8.032</td><td>8.276</td><td>-0.244</td><td>0.062</td><td>-0.700</td></tr><tr><td>Matched</td><td>8.068</td><td>7.910</td><td>0.158</td><td>0.427</td><td>0.840</td></tr><tr><td rowspan="2">Ln(Experience Diversity)</td><td>Unmatched</td><td>2.830</td><td>2.420</td><td>0.410</td><td>0.231</td><td>3.540</td></tr><tr><td>Matched</td><td>2.829</td><td>2.716</td><td>0.112</td><td>0.032</td><td>1.770</td></tr><tr><td rowspan="2">Ln(Experience Amount)</td><td>Unmatched</td><td>0.832</td><td>0.744</td><td>0.088</td><td>0.086</td><td>2.200</td></tr><tr><td>Matched</td><td>0.824</td><td>0.799</td><td>0.025</td><td>0.011</td><td>1.020</td></tr></table>

Note: The comparisons are based on one-to-one matching without replacement (calibre = 0.03)

sample was 148.<sup>6</sup> We then collected the panel data for the treatment group contestants. We collected a control group of 194 contestants who never registered in the online community forum. For the control group, to reduce the self-selection bias, we used propensity score matching to identify similar users at the pretreatment stage.

## 4.3.1 | Propensity score matching

Propensity score matching (PSM) is useful to reduce self-selection bias by identifying contestants within the contro group with high similarity to members in the treatment group in terms of observed characteristics (Durward et al., 2020; Ho et al., 2011). PSM can help identify causal inferences from observational data (Nichols, 2007). Fol lowing Nichols (2007), we used the nearest neighbour match to calculate the propensity score via the psmatch2 com mand in STATA with the dichotomous outcome of being registered in the online community forum.

We used gender, platform tenure, experience quantity before February 2018, and experience diversity befor February 2018 to calculate the propensity score, that is, the probability of having registered in the forum. Table 4 shows the summary statistics of the treatment and control groups before and after matching using one-to-one nearest neighbour matching. We matched each contestant who registered in the forum with a contestant that did not register in the forum. The differences between the treatment group and the control group were reduced afte matching. The t-test results confirmed that the means of the two groups became more similar after matching. After the matching, our sample size was reduced to 122 registered contestants with 122 matched contestants who did not register in the forum.7 Our total observations are reduced to 5856.8

We used the matched sample to conduct a difference-in-differences (DID) estimation to detect the effects of introducing an online community. The DID regression estimation allowed us to task advantage of panel data to control for both time-specific and contestant-specific effects. Therefore, we were able to detect changes not onl between treatment and control contestants, but also changes in the same contestant before and after introduction of the online community. Our estimation equations for user i in month t are represented as follows

$$
\begin{array}{l} \text {Ln(WinningContests} _ {i t}) = \beta 0 + \beta 1 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {t} + \beta 2 ^ {*} \text {Post Treatment} _ {t} + \beta 3 ^ {*} \text {Treatment} _ {i} \\ \quad + \beta 4 ^ {*} \ln (\text {Platform Tenure}) _ {i t} + \beta 5 ^ {*} \ln (\text {Experience Amount}) _ {i t} + \beta 6 ^ {*} \ln (\text {Experience Diversity}) _ {i t} \\ \quad + \beta 7 ^ {*} \ln (\text {Forum Contribution}) _ {i t} + \beta 8 ^ {*} \text {Gender} \\ \quad + \beta 9 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {i t} ^ {*} \ln (\text {Experience Amount}) _ {i t} \\ \quad + \beta 1 0 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {i t} ^ {*} \ln (\text {Experience Diversity}) \\ \quad + \sum \text {Monthly\_Dummy} _ {t} + \alpha_ {i} + \mathcal {E} _ {i t} \end{array}
$$

$$
\begin{array}{l} \text {Ln(Crowdsourcing Income} _ {i t}) = \beta 0 + \beta 1 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {t} + \beta 2 ^ {*} \text {Post Treatment} _ {t} + \beta 3 ^ {*} \text {Treatment} _ {i} \\ \quad + \beta 4 ^ {*} \ln (\text {Platform Tenure}) _ {i t} + \beta 5 ^ {*} \ln (\text {Experience Amount}) _ {i t} \\ \quad + \beta 6 ^ {*} \ln (\text {Experience Diversity}) _ {i t} + \beta 7 ^ {*} \ln (\text {Forum Contribution}) _ {i t} + \beta 8 ^ {*} \text {Gender} \\ \quad + \beta 9 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {i t} ^ {*} \ln (\text {Experience Amount}) _ {i t} \\ \quad + \beta 1 0 ^ {*} \text {Treatment} _ {i} ^ {*} \text {Post Treatment} _ {i t} ^ {*} \ln (\text {Experience Diversity}) \\ \quad + \sum \text {Monthly\_Dummy} _ {t} + \alpha_ {i} + \mathcal {E} _ {i t} \end{array}\tag{1}
$$

ð<sup>2</sup>Þ

Besides our independent and dependent variables, we also included control variables in our estimations.

## 5 | RESULTS

The Hausman test results indicated that the fixed-effects model is more appropriate than the random effect mode $( \chi ^ { 2 } = 5 3 1 . 2 4 , p < 0 . 0 0 1 )$ . Tables 5 and 6 show the hypothesis testing results. All models used clustered standard errors at the contestant level and included all control variables. We used the propensity score-matched data to test the hypotheses. Column (1) in Tables 5 and 6 shows the impacts of control variables. Columns (2) and (4) in Tables 5 and 6 show the results of H1a and H1b, while Column (3) shows the results of H2 and H3, respectively

T A B L E 5 Hypothesis test results for winning contests

<table><tr><td>DV = ln(winning  $contests_{it}$ )</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Post-Treatment $_t$ </td><td></td><td>2.860*** (0.111)</td><td>1.759*** (0.121)</td></tr><tr><td>Treatment $_i$ * Post-Treatment $_t$ </td><td></td><td>0.679*** (0.084)</td><td>3.114*** (0.181)</td></tr><tr><td>Treatment $_i$ * Post-Treatment $_t$ *Ln(Experience Amount) $_{it}$ </td><td></td><td></td><td>-0.863*** (0.057)</td></tr><tr><td>Treatment $_i$ * Post-Treatment $_t$ * Ln(Experience Diversity) $_{it}$ </td><td></td><td></td><td>0.108** (0.035)</td></tr><tr><td>Ln(Forum Contribution) $_{it}$ </td><td>0.092** (0.042)</td><td>-0.055 (0.048)</td><td>-0.031 (0.042)</td></tr><tr><td>Ln(Experience Amount) $_{it}$ </td><td>0.512*** (0.045)</td><td>0.507*** (0.045)</td><td>0.781*** (0.034)</td></tr><tr><td>Ln(Experience Diversity) $_{it}$ </td><td>1.786*** (0.062)</td><td>1.757*** (0.059)</td><td>1.656*** (0.056)</td></tr><tr><td>Ln(Tenure) $_{it}$ </td><td>-0.882*** (0.152)</td><td>-0.176 (0.170)</td><td>0.152 (0.147)</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummy</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>R square</td><td>0.502</td><td>0.519</td><td>0.564</td></tr><tr><td>No. of Observations</td><td>5856</td><td></td><td></td></tr></table>

Note: Clustered-robust standard errors (clustered on contestants) are reported.  
\*\*\*p < 0.001; \*\*p < 0.01.

T A B L E 6 Hypothesis testing results for crowdsourcing income

<table><tr><td>DV = ln(crowdsourcing incomeit)</td><td>1</td><td>2</td><td>3</td></tr><tr><td>Post-Treatmentt</td><td></td><td>-3.350***(0.151)</td><td>-3.525***(0.167)</td></tr><tr><td>Treatmenti* Post-Treatmentt</td><td></td><td>0.351*(0.163)</td><td>0.733**(0.247)</td></tr><tr><td>Treatmenti* Post-Treatmentt* Ln(Experience Amount)it</td><td></td><td></td><td>-0.136*(0.068)</td></tr><tr><td>Treatmenti* Post-Treatmentt* Ln(Experience Diversity)it</td><td></td><td></td><td>-0.006(0.060)</td></tr><tr><td>Ln(Forum Contribution)it</td><td>0.2000**(0.066)</td><td>0.070(0.071)</td><td>0.077(0.072)</td></tr><tr><td>Ln(Experience Amount)it</td><td>0.966***(0.042)</td><td>0.960***(0.041)</td><td>1.003***(0.045)</td></tr><tr><td>Ln(Experience Diversity)it</td><td>1.358***(0.128)</td><td>1.335***(0.127)</td><td>1.352***(0.171)</td></tr><tr><td>Ln(Tenure)it</td><td>0.670**(0.227)</td><td>1.420***(0.258)</td><td>1.492***(0.260)</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummy</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>R square</td><td>0.303</td><td>0.308</td><td>0.310</td></tr><tr><td>No. of observations</td><td>5856</td><td></td><td></td></tr></table>

Note: Clustered-robust standard errors (clustered on contestants) are reported.  
\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Results in Column (2) of Table 5 show that Post-Treatment Treatment positively affected the number of winning contests $( \beta = 0 . 6 7 9 , p < 0 . 0 0 1 )$ . This finding suggests that holding other variables constant, a contestant who signed up for the online community forum increased winning contests by 67.9% compared to the matched con testant who did not. Similarly, results in Column (2) of Table 6 show that Post-Treatment Treatment positively affected the income that a contestant earns in a month $( \beta = 0 . 3 5 1 , p < 0 . 0 5 )$ ). This finding suggests that holding other variables constant, a contestant who signed up for the forum received an additional 35.1% of crowdsourcing income compared to the matched contestant who did not. Thus, H1a and H1b were supported.

In addition, results in Column (3) of Table 5 show that Post-Treatment Treatment Experience Amount nega tively affected the number of winning contests $( \beta = - 0 . 8 6 3 , p < 0 . 0 0 1 )$ . This finding suggests that contestants wit a greater amount of experience obtain fewer winning contests after signing up for the online community forum Results in Column (3) of Table 6 show that Post-Treatment Treatment Experience Amount negatively affected the crowdsourcing income $( \beta = - 0 . 1 3 6 , p < 0 . 0 5 )$ . This suggests that contestants with a greater amount of experi ence received less income after signing up for the online community forum. Thus, H2a and H2b were supported.

Furthermore, results in Column (3) of Table 5 show that Post-Treatment Treatment Experience Diversity positively affected the winning contests $( \beta = 0 . 1 0 8 , p < 0 . 0 1 )$ . This finding suggests that a contestant with diverse experience won more contests after signing up for the online community forum than a contestant with less diverse experience. Results in Column (3) of Table 6 show that Post-Treatment Treatment Experience Diversity did not affect the crowdsourcing income (β = 0.006, p > 0.05). Thus, H3a was supported but H3b was not.

## 5.1 | Robustness checks

The DID model has a critical parallel trend assumption that no pre-treatment trend exists between the treatment and control groups (Angrist & Pischke. 2008). We tested whether the parallel trend assumption holds in our study ir two ways. First, following Angrist and Pischke (2008), we conducted the correlated random trend model test. Th significance of the estimated effects of interest did not change (all p values < 0.05), demonstrating that our results are not driven by individual-specific time trends

Second, we conducted the relative time model test suggested by Autor (2003). The results in Table 7 show no significant effects on our dependent variables in the three-month period prior to the introduction of the online com munity, but sharp increases in effects on our dependent variables are noted after the introduction of the online com munity. This result suggests that it takes around 1 month for the introduction of an online community to take effect These results show no sign of pre-treatment trends in our study, providing further support to the robustness of our findings. Results from the parallel trend assumption test helped us rule out the potential influence caused by time variant unobservable confounds

T A B L E 7 Parallel trend test using the relative time mode

<table><tr><td></td><td>Winning  $contests_{it}$ </td><td>Crowdsourcing  $income_{it}$ </td></tr><tr><td>Lead3 (November-2017) *  $Treatment_i$ </td><td>-0.018 (0.152)</td><td>0.111 (0.198)</td></tr><tr><td>Lead2 (December-2017) *  $Treatment_i$ </td><td>0.043 (0.150)</td><td>0.243 (0.196)</td></tr><tr><td>Lead1 (January-2018) *  $Treatment_i$ </td><td>0.220 (0.148)</td><td>0.238 (0.194)</td></tr><tr><td>Lag1(March-2018) *  $Treatment_i$ </td><td>0.454** (0.146)</td><td>0.517** (0.191)</td></tr><tr><td>Lag2 (April-2018) *  $Treatment_i$ </td><td>0.469** (0.147)</td><td>0.864*** (0.189)</td></tr><tr><td>Within panel R-squared</td><td>0.084</td><td>0.074</td></tr><tr><td>Controls</td><td>Yes</td><td></td></tr><tr><td>Individual FE</td><td>Yes</td><td></td></tr><tr><td>Observations</td><td>5856</td><td></td></tr></table>

Note: Results on control variables and fixed effects are omitted for simplicity. Standard errors are clustered at the individual level. $^ { * * * } p < 0 . 0 0 1 ; ^ { * * } p < 0 . 0 1$

T A B L E 8 Robustness checks for Poisson estimations

<table><tr><td rowspan="2"></td><td colspan="2">DV = winning  $contests_{it}$ </td><td colspan="2">DV = crowdsourcing  $income_{it}$ </td></tr><tr><td>Coefficient</td><td>Robust SE</td><td>Coefficient</td><td>Robust SE</td></tr><tr><td> $Post-Treatment_t$ </td><td>2.251***</td><td>0.137</td><td>-3.986***</td><td>0.224</td></tr><tr><td> $Treatment_i * Post-Treatment_t$ </td><td>4.447***</td><td>0.217</td><td>0.687*</td><td>0.319</td></tr><tr><td> $Treatment_i * Post-Treatment_t * Ln(Experience Amount)_{it}$ </td><td>-1.267***</td><td>0.065</td><td>-0.226*</td><td>0.100</td></tr><tr><td> $Treatment_i * Post-Treatment_t * Ln(Experience Diversity)_{it}$ </td><td>0.130***</td><td>0.022</td><td>-0.106</td><td>0.064</td></tr><tr><td> $Ln(Forum Contribution)_{it}$ </td><td>0.006</td><td>0.041</td><td>0.074</td><td>0.082</td></tr><tr><td> $Ln(Experience Amount)_{it}$ </td><td>1.148***</td><td>0.039</td><td>0.887***</td><td>0.067</td></tr><tr><td> $Ln(Experience Diversity)_{it}$ </td><td>1.413***</td><td>0.041</td><td>1.083***</td><td>0.131</td></tr><tr><td> $Ln(Tenure)_{it}$ </td><td>0.190</td><td>0.164</td><td>1.184***</td><td>0.252</td></tr><tr><td>Fixed effects</td><td>Yes</td><td></td><td>Yes</td><td></td></tr><tr><td>Monthly dummy</td><td>Yes</td><td></td><td>Yes</td><td></td></tr><tr><td>Model</td><td>Poisson</td><td></td><td>Poisson</td><td></td></tr><tr><td>No. of observations</td><td>5856</td><td></td><td></td><td></td></tr></table>

Note: Clustered-robust standard errors (clustered on contestants) are reported.  
\*\*\*p < 0.001; \*p < 0.05.

T A B L E 9 IV regression using generated instruments

<table><tr><td rowspan="2"></td><td colspan="2">DV = ln(winning contests)</td><td colspan="2">DV = ln(crowdsourcing income)</td></tr><tr><td>Coefficient</td><td>Robust SE</td><td>Coefficient</td><td>Robust SE</td></tr><tr><td>Post-Treatmentt</td><td>0.158***</td><td>0.018</td><td>-1.049***</td><td>0.041</td></tr><tr><td>Treatmenti* Post-Treatmentt</td><td>1.319***</td><td>0.043</td><td>0.049*</td><td>0.021</td></tr><tr><td>Treatmenti* Post-Treatmentt * Ln(Experience Amount)it</td><td>-0.767***</td><td>0.028</td><td>-0.117*</td><td>0.057</td></tr><tr><td>Treatmenti* Post-Treatmentt * Ln(Experience Diversity)it</td><td>0.064**</td><td>0.017</td><td>0.042</td><td>0.029</td></tr><tr><td>Control variables</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>Fixed effects</td><td colspan="2">Yes</td><td colspan="2">Yes</td></tr><tr><td>F-statistic</td><td colspan="2">2493.27 (9, 7163)</td><td colspan="2">403.73 (9, 7163)</td></tr><tr><td>Hansen J (p-value)</td><td colspan="2">5.478 (0.140)</td><td colspan="2">2.920 (0.232)</td></tr><tr><td>No. of observations</td><td colspan="2">5856</td><td colspan="2"></td></tr></table>

Note: Clustered-robust standard errors (clustered on contestants) are reported.  
\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

Besides the DID regression estimation, we conducted Poisson regression estimations on our dependent variables. Hypothesis testing results in Table 8 were similar to those in Tables 5 and 6. This suggests that our results ar consistent across fixed-effect estimation and Poisson estimation, establishing the robustness of our findings.

Furthermore, we employed Lewbel (2012)'s method of mathematically constructing instruments from covariates specified as exogenous. This method treats all variables except our independent variables as exogenous to the dependent variable. We implemented the regressions via the ivreg2h command in STATA. The results appear in Table 9. The p-value of Hansen J statistics for both dependent variables was higher than 0.05, suggesting there is no over-identification issue. The results in Table 9 were similar to those in Tables 5 and 6. This adds further support to the robustness of our findings.<sup>9</sup>

## 6 | DISCUSSION

With the increasing prevalence of crowdsourcing platforms, firms can tap external workers (contestants) for solu tions to their tasks (Liu et al., 2020). Contestant performance determines the quality of solutions and the value that firms can obtain from these platforms (Boons et al., 2015). Yet, the forces of contest platforms may induce contestants to economise their effort, constrain their idea expression and threaten their performance (Boudreau et al., 2011; Boudreau et al., 2016; Hofstetter et al., 2021). Searching for ways to maintain (or elevate) performance operators of crowdsourcing contest platforms have begun adding online communities to their platforms hoping that the benefits of online communities will spill over to contest performance. This study contributes to crowdsourcing literature by revealing the direct effects of introducing an online community on contestants' crowdsourcing perfor mance and the moderating effects of experience amount and diversity. The results of this study revealed that the introduction of an online community improves the average contestant performance in terms of winning contests and income. Furthermore, this impact was contingent on the amount and diversity of experience. However, we did not find a significant moderating effect of experience diversity on the relationship between introduction of an online community and contestant's crowdsourcing income. This could be due to the fact that crowdsourcing income depends heavily on the rewards of each task (Terwiesch & Xu, 2008).

## 6.1 | Limitations and future research

The results of this study should be interpreted in light of its limitations. First, this study involves one crowdsourcing contest platform (i.e., ZBJ) and individuals were not randomly assigned to treatment groups, so care should be take in generalising the results to other platforms. Our findings are likely to generalise if contest design, incentives and online communities are similar to those described here. However, various platform designs, incentive structures and communities exist. For example, InnoCentive requires specialised expertise to solve the tasks, so contestants must possess formal education or specialised training to provide winning solutions. Future studies should examine if results of this study apply to different types of platforms and communities and may employ other methods such a controlled, randomised experiments.

Second, while this study investigates the effects of launching an online community on contestant performance, future studies can probe further to examine the process of how contestants get involved in such communities and integrate community knowledge into actual performance. Other antecedents can also be examined in futur research. For example, future studies can explore the influence of introducing an online community on relational networks among contestants and their performance. Specifically, researchers can draw on network theor (e.g., Burt, 1992) to examine the effects of an online community on communication network structure (e.g., centrality, connectivity, and tie strengths) of contestants (e.g., Stephen et al., 2016).

Third, we study the moderating impact of two aspects of prior experience (i.e., experience amount and diversity) Future studies could examine other moderators, such as contestants' motivation, ability, skills or relevance and recency of prior experience (e.g., Bayus, 2013; Liu et al., 2020). These factors may influence the ability of contestants to extrac knowledge from their experience and translate it into performance. Also, future studies can explore how contestant can strategize in choosing tasks to maximise their winning rewards. For example, some contestants may do better b focusing on addressing one type of task, while other contestants may do better by attempting different types of tasks.

## 6.2 | Theoretical contributions

This study contributes to the crowdsourcing literature and other related research in several ways. These contribu tions are categorised according to Corley and Gioia (2011) and Weber (2012) in Appendix D. First, this study corrob orates the findings from other scholars (Dissanayake et al., 2021; Jin et al., 2021; Stanko, 2016) emphasising recently revealed benefits that can come from knowledge collaboration in crowdsourcing contests. Despite clear incentives to sustain competitive advantages (Boudreau et al., 2011; Boudreau et al., 2016; Hofstetter et al., 2021), contestant collaborated with each other within the online community and the benefits of interaction flowed to contestants These findings support the notion that the benefits of online communities are robust to competitive pressures and challenge the assumption that collaboration and competition cannot coexist on platforms. The findings also support the development of communitition platforms as a mechanism to support contestants through knowledge collabora tion and sociality, improve their performance and make their submissions more attractive to seeker firms

Central to this study is the direct observation of introducing an online community. Our unique dataset allowed us to isolate (or hold constant) effects that could have clouded the consequences of introducing the online commu nity. Our observations contrast with other research examining communitition, where the knowledge collaboration took place within the existing structure of the crowdsourcing platform (e.g., Liu et al., 2020). In our case, introductio of the online community was separate from the contest platform and was an exogenous shock. Yet even in these cir cumstances, its introduction produced significant improvements for contestants who participated. Our results offe strong evidence of positive spillover effects stemming from online communities, even when boundaries between contest and community spaces are explicit.

Second, our findings also have relevance for research in online communities. Prior studies on online communitie have conceptualised the impacts of online communities by focusing on their intra-community effects (e.g., Fara et al., 2011; Faraj et al., 2016; Majchrzak & Malhotra, 2016). This study not only extends prior work by theorising extensions to online communities (e.g., communitition), but also directly quantifies impacts introduced by online communities. This work explicitly examines spillover effects that originate from within the community but affect out comes outside of the community. Further, by quantifying the impacts of introducing an online community into a con test platform, our study contributes to the growing literature on online communities (e.g., Faraj et al., 2011; Fara et al., 2016; Majchrzak & Malhotra, 2016). Our study provides empirical evidence on the precise impacts of an onlin community and grounds future research by showing concrete payoffs for participants

Third, we have developed a nuanced approach to examining the effects of experience and how it alters the effects of introducing an online community in a crowdsourcing contest platform. Prior research has demonstrated mixed effects from experience in crowdsourcing contests (Bockstedt et al., 2016; Liu et al., 2020; Menon et al., 2020). Thus, we followed other scholars (e.g., Bayus, 2013), who revealed the effects of multiple dimensions of experience (e.g., experience amount, experience diversity) in crowdsourcing. Our findings reinforce the notion that dimensions of experience exert unique effects on crowdsourcing outcomes. Therefore, dimensions of experience should be separated and accounted separately in empirical crowdsourcing research. The dimensions of experience could work in tandem (e.g., in our case low experience amount, high experience diversity) or be at odds (e.g., hig experience amount, high experience diversity). But neglecting these dimensions could cloud the effects of experi ence in crowdsourcing performance.

Fourth, our findings revealed important boundary conditions altering the effects of an online community. Specif ically, we demonstrated that contestants with low experience amount or contestants with high experience diversit are likely to derive much greater benefit from online communities, while those with higher experience amounts or low experience diversity derive less benefit. We hypothesised this boundary condition would emerge based on cognitive diversity and this finding challenges the implicit assumption that participants in online communities benefit equally (Faraj et al., 2011; Faraj et al., 2016). This finding joins with the work of others (e.g., Jin et al., 2021) who demonstrate important contingencies on the benefits of communtition platforms. Our work clearly shows that not everyone benefits equally from the introduction of an online community. Therefore, critical questions emerge regarding the motivations of communitition platform contributors and how sustainable the platforms are. For exam ple, if a limited number of contributors are deriving most of the benefit, how do platform owners maintain long-term viability? Although online communities have been shown to be remarkably resilient (Butler et al., 2014), such ques tions need to be addressed regarding communitition platforms.

## 6.3 | Practical implications

From a practical perspective, this study offers insights to crowdsourcing platform owners and operators regarding investment in an online community for crowdsourcing contests and to firms regarding harnessing the knowledge that contestants provide as suitable solutions for their tasks. Our results suggest that the introduction of an online com munity helps enhance contestant performance by encouraging knowledge collaboration and sociality among contes tants. Hence, our study demonstrates the importance of designing innovation contest platforms with features that support knowledge sharing and collaboration among contestants. Previously, innovation contest platforms incentivised contestants and addressed underinvestment problems by managing the reward structure and regulating competition by the number of contestants allowed to enter in a task contest (Boudreau et al., 2016; Mo et al., 2018) Our study offers an additional way to address low performance by contestants by providing a virtual space for con testants to collaborate and socialise.

In addition, our results demonstrated that contestants with diverse experience benefit more from participating in an online community. To enhance contestant performance, crowdsourcing contest platforms can encourage contestants to experience different types of contests. Several mechanisms could be explored to develop greater experi ence diversity in contestants. For example, offering guidance, recommendations, incentives to join various types of contests could be helpful in encouraging experience diversity. Contest platforms should also consider designing and utilising recommender systems that balance the conflicting needs of exploitation and task diversity by graduall extending the scope of a contestant's work. Our study suggests that contestants with a greater amount of experi ence benefit less from the introduction of an online community. Our research, therefore, provides some level of con fidence that participating in more contests may not help improve performance (Archak & Ghose, 2010 Bayus, 2013). Combining this finding with the results of experience diversity, it is advisable for contestants to try dif ferent types of tasks instead of working only on one type of task.

Finally, our study suggests that those with little experience will derive large benefits from participating in the online community. For platform owners and operators, this finding suggests that guidance and encouragement for new contestants should be given to participate in the online community. Similarly, new contestants should themselves seek out, join and actively participate in these communities. Doing so will quickly help them improve their performance in contests

## 7 | CONCLUSION

Current trends show that crowdsourcing contests will increasingly be relied upon by firms to seek solutions for thei tasks (Mo et al., 2021). Hence, it is important to understand how to improve contestant performance for the benefit of firms, contestants and crowdsourcing platforms (Allen et al., 2018; Ye & Kankanhalli, 2017). Leveraging the launch of an online community in a contest crowdsourcing platform, this study develops and empirically tests a causal rela tionship between the introduction of an online community and crowdsourcing performance. This study also concep tualises two aspects of prior experience (i.e., experience quantity and diversity) as moderators of contestant performance. The results indicate that the two aspects of prior experience distinctly affect the relationship between the introduction of an online community and contestants' performance. These results extend our theoretical under standing of the impacts of an online community on a crowdsourcing contest platform and offer practical guidance on how to make this form of crowdsourcing more effective

## DATA AVAILABILITY STATEMENT

Research data are not shared.

## ORCID

Jonathan (Hua) YeD https://orcid,org/0000-0002-9119-7886

Matthew Jensen https://orcid.org/0000-0001-8711-1827

## REFERENCES

Absolute Market Insights. (2020). Crowdsourcing Market 2019–2027. Retrieved from https://www. absolutemarketsinsights.com/reports/Crowdsourcing-Market-2019-2027-296

Allen, B., Chandrasekaran, D., & Basuroy, S. (2018). Design crowdsourcing: The impact on new product performance of sourcing design solutions from the crowd . Journal of Marketing, 82(2), 106–123

Althuizen, N., & Chen, B. (2021). Crowdsourcing ideas using product prototypes: The joint effect of prototype enhancement and the product design goal on idea novelty. Management Science, 68, 3008–3025

Angrist, J. D., & Pischke, J.-S. (2008). Mostly harmless econometrics: An Empiricist's companion. Princeton University Press

Archak, N., & Ghose, A. (2010). Learning-by-Doing and Project Choice: A Dynamic Structural Model of Crowdsourcing International Conference on Information Systems, St. Louis, USA.

Atuahene-Gima, K. (2005). Resolving the capability–rigidity paradox in new product innovation. Journal of Marketing, 69(4) 61–83.

Autor, D. H. (2003). Outsourcing at will: The contribution of unjust dismissal doctrine to the growth of employment out sourcing. Journal of Labor Economics, 21(1), 1–42.

Bayus, B. (2013). Crowdsourcing new product ideas over time: An analysis of the Dell Ideastorm community. Management Science, 59(1), 226–244.

Blohm, I., Leimeister, J. M., & Krcmar, H. (2013). Crowdsourcing: How to benefit from (too) many great ideas. MIS Quarterly Executive, 12(4), 199–211.

Bockstedt, J., Druehl, C., & Mishra, A. (2016). Heterogeneous submission behavior and its implications for success in innova tion contests with public submissions. Production and Operations Management, 25(7), 1157–1176.

Boh, W. F., Slaughter, S. A., & Espinosa, J. A. (2007). Learning from experience in software development: A multilevel analy sis. Management Science, 53(8), 1315–1331

Boone, C., & Hendriks, W. (2009). Top management team diversity and firm performance: Moderators of functional background and locus-of-control diversity. Management Science, 55(2), 165–180.

Boons, M., Stam, D., & Barkema, H. G. (2015). Feelings of pride and respect as drivers of ongoing member activity on crowdsourcing platforms. Journal of Management Studies, 52(6), 717–741

Boudreau, K., Lakhani, K. R., & Menietti, M. (2016). Performance responses to competition across skills-level in rank-order tournaments: Field evidence and implications for Tournamenet design. RAND Journal of Economics, 47(1), 140–165

Boudreau, K. J., Lacetera, N., & Lakhani, K. R. (2011). Incentives and problem uncertainty in innovation contests: An empiri cal analysis. Managemnt Science, 57(5), 843–863

Burt, R. S. (1992). Structural holes: The social structure of competition. Harvard University Press.

Butler, B., Bateman, P. J., Gray, P. H., & Diamant, E. I. (2014). An attraction–selection–attrition theory of online communit size and resilience. MIS Quarterly, 38(3), 699–729.

Chen, X., Li, X., Yao, D., & Zhou, Z. (2019). Seeking the support of the silent majority: Are lurking users valuable to Ugc platforms? Journal of the Academy of Marketing Science, 47(6), 986–1004

Chen, Y., Boh, W. F., & Mo, J. (2018). Learning from experience vs. learning from others: Evidence from crowdsourcing contests. Academy of Management Global Proceedings, p. 189.

Corley, K. G., & Gioia, D. A. (2011). Building theory about theory building: What constitutes a theoretical contribution? Acad emy of Management Review, 36(1), 12–32.

Dennis, A. R., & Valacich, J. S. (1993). Computer brainstorms: More heads are better than one. Journal of Applied Psychology, 78:4, 531.

Dissanayake, I., Nerur, S., Wang, J., Yasar, M., & Zhang, J. (2021). The impact of helping others in Coopetitive crowdsourcing communities. Journal of the Association for Information Systems. 22:1.7

Dissanayake, I., Zhang, J., & Gu, B. (2015). Task division for team success in crowdsourcing contests: Resource allocatio and alignment effects. Journal of Management Information Systems, 32(2), 8–39.

Durward, D., Blohm, I., & Leimeister, J. M. (2020). The nature of crowd work and its effects on Individuals' work perception Journal of Management Information Systems, 37(1), 66–95.

Faraj, S., Jarvenpaa, S. L., & Majchrzak, A. (2011). Knowledge collaboration in online communities. Organization Science, 22(5), 1224–1239.

Faraj, S., von Krogh, G., Monteiro, E., & Lakhani, K. R. (2016). Special section introduction: Online community as space for knowledge flows. Information Systems Research, 27(4), 668–684.

Felin, T., Lakhani, K. R., & Tushman, M. L. (2017). Firms, crowds, and innovation. Strategic Organization, 15(2), 119–140

Feng, Y., Ye, H. J., Yu, Y., Yang, C., & Cui, T. (2018). Gamification artifacts and crowdsourcing participation: Examining the mediating role of intrinsic motivations. Computers in Human Behavior, 81, 124–136

Fixson, S., & Marion, T. (2016). A Case Study of Crowdsourcing Gone Wrong. Retrieved from https://hbr.org/2016/12/a case-study-of-crowdsourcing-gone-wrong

Han, Y., Ozturk, P., & Nickerson, J. V. (2020). Leveraging the wisdom of the crowd to address societal challenges: Revisiting the knowledge reuse for innovation process through analytics. Journal of the Association for Information Systems, 21:5, 8

Haried, P., Han, Y., & Annino, D. (2021). Fintech in information systems research: A 2010–2020 review of the Ais senio Scholars' basket. Journal of International Technology and Information Management, 30(2), 1–29.

Ho, D. E., Imai, K., King, G., & Stuart, E. A. (2011). Matchit: Nonparametric preprocessing for parametric causal inference Journal of Statistical Software, 42, 1–28.

Hofstetter, R., Dahl, D. W., Aryobsei, S., & Herrmann, A. (2021). Constraining ideas: How seeing ideas of others harms crea tivity in open innovation. Journal of Marketing Research, 58(1), 95–114.

Honoré, F. (2021). Joining forces: How can founding Members' prior experience variety and shared experience increase startup survival? Academy of Manggement Journal. 65. 248–272

Horn, J. L. (1989). Cognitive Diversity: A Framework of Learning.

Huang, N., Hong, Y., & Burtch, G. (2017). Social network integration and user content generation: Evidence from natura experiments. MIS Quarterly, 41(4), 1035–1058.

Huang, Y., Singh, P. V., & Srinivasan, K. (2014). Crowdsourcing new product ideas under consumer learning. Management Sci ence, 60(9), 2138–2159.

Hutter, K., Füller, J., Hautz, J., Bilgram, V., & Matzler, K. (2015). Machiavellianism or morality: Which behavior pays off i online innovation contests? Journal of Management Information Systems, 32(3), 197–228

Hutter, K., Hautz, J., Füller, J., Mueller, J., & Matzler, K. (2011). Communitition: The tension between competition and collab oration in community-based design contests. Creativity and Innovation Management, 20(1), 3–21

Järvenpää, S.‐L., & Majchrzak, A. (2010). Vigilant interaction in knowledge collaboration: Challenges of online user participation under ambivalence. Information Systems Research, 21(4), 773–784

Jeppesen, L. B., & Lakhani, K. R. (2010). Marginality and problem solving effectiveness in broadcast search. Organization Sci ence, 21(5), 1016–1033.

Jian, L., Ba, S., Lu, L., Jiang, L. C., & Yang, S. (2019). Managing the crowds: The effect of prize guarantees and in-proces feedback on participation in crowdsourcing contests. MIS Quarterly, 43(1), 97–112.

Jin, Y., Lee, H. C. B., Ba, S., & Stallaert, J. (2021). Winning by learning? Effect of knowledge sharing in crowdsourcing con tests. Information Systems Research, 32, 836–859

Kane, G. C., & Ransbotham, S. (2016). Content as community regulator: The recursive relationship between consumptio and contribution in open collaboration communities. Organization Science, 27(5), 1258–1274

Kim, Y., Jarvenpaa, S. L., & Gu, B. (2018). External bridging and internal bonding: Unlocking the generative resources of member time and attention spent in online communities. MIS Quarterly, 42(1), 265–283.

Koh, T. K. (2019). Adopting Seekers' solution exemplars in crowdsourcing ideation contests: Antecedents and consequences Information Systems Research, 30(2), 361–710

Lee, H. C. B., Ba, S., Li, X., & Stallaert, J. (2018). Salience bias in crowdsourcing contests. Information Systems Research, 29(2), 401–418.

Leonard-Barton, D. (1992). Core capabilities and Core rigidities: A paradox in managing new product development. Strategic Management Journal, 13(S1), 111–125.

Lewbel, A. (2012). Using heteroscedasticity to identify and estimate Mismeasured and endogenous Regressor models. Jour nal of Business and Economic Statistics, 30(1). 67–80

Li, M., Kankanhalli, A., & Kim, S. H. (2016). Which ideas are more likely to be implemented in online user innovation commu nities? An empirical analysis. Decision Support Systems, 84, 28–40.

Lin, M., Lucas, H. C., Jr., & Shmueli, G. (2013). Research commentary—Too big to fail: Large samples and the P-value prob lem. Information Systems Research, 24(4), 906–917.

Liu, Q., Du, Q., Hong, Y., Fan, W., & Wu, S. (2020). User idea implementation in open innovation communities: Evidenc from a new product development crowdsourcing community. Information Systems Journal, 30(5), 899–927.

Lowry, P. B., Zhang, J., Moody, G. D., Chatterjee, S., Wang, C., & Wu, T. (2019). An integrative theory addressing Cyber harassment in the light of technology-based opportunism. Journal of Management Information Systems, 36(4), 1142–1178.

Ma, M., & Agarwal, R. (2007). Through a glass darkly: Information technology design, identity verification, and knowledg contribution in online communities. Information Systems Research, 18(1), 42–67.

Ma, X., Khansa, L., & Kim, S. S. (2018). Active community participation and crowdworking turnover: A longitudinal mode and empirical test of three mechanisms. Journal of Management Information Systems, 35(4), 1154–1187.

Majchrzak, A., & Malhotra, A. (2016). Effect of knowledge-sharing trajectories on innovative outcomes in temporary onlin crowds. Information Systems Research, 27(4), 685–703

Mamykina, L., Smyth, T. N., Dimond, J. P., & Gajos, K. Z. (2016). Learning from the Crowd: Observational Learning i Crowdsourcing Communities. Poceedings of the 2016 CHI Conference on Human Factors in Computing Systems, San Jose, CA, USA: ACM, pp. 2635–2644.

Menon, N., Mishra, A., & Ye, S. (2020). Beyond related experience: Upstream vs. downstream experience in innovation con test platforms with interdependent problem domains. Manufacturing & Service Operations Management, 22, 1045–1065

Miller, C. C., Burke, L. M., & Glick, W. H. (1998). Cognitive diversity among upper-echelon executives: Implications for stra tegic decision processes. Strategic Management Journal, 19(1), 39–58

Mo, J., Sarkar, S., & Menon, S. (2018). Know when to run: Recommendations in crowdsourcing contests. MIS Quarterly 42(3), 919–944.

Mo, J., Sarkar, S., & Menon, S. (2021). Competing tasks and task quality: An empirical study of crowdsourcing contests. MI Quarterly, 45(4), 1921–1948.

Nagle, F. (2018). Learning by contributing: Gaining competitive advantage through contribution to crowdsourced publi goods. Organization Science, 29(4), 569–587.

Nevo, D., & Kotlarsky, J. (2020). Crowdsourcing as a strategic is sourcing phenomenon: Critical review and insights for future research. Journal of Strategic Information Systems, 29, 1–22

Nichols, A. (2007). Causal inference with observational data. The Stata Journal, 7(4), 507–541.

Okhuysen, G., & Bonardi, J.-P. (2011). The challenges of building theory by combining lenses (pp. 6–11). Academy of Manage ment Briarcliff Manor.

O'leary, M. B., Mortensen, M., & Woolley, A. W. (2011). Multiple team membership: A theoretical model of its effects o productivity and learning for individuals and teams. Academy of Management Review, 36(3), 461–478

Olson, B. J., Parayitam, S., & Bao, Y. (2007). Strategic decision making: The effects of cognitive diversity, conflict, and trust on decision outcomes. Journal of Management, 33(2), 196–222

Ransbotham, S., & Kane, G. C. (2011). Membership turnover and collaboration success in online communities: Explaining rises and falls from grace in Wikipedia. MIS Quarterly, 35(3), 613–627.

Ransbotham, S., Kane, G., & Lurie, N. H. (2012). Network characteristics and the value of collaborative user generated con tent. Marketing Science, 31(3), 387–405

Riedl, C., & Seidel, V. P. (2018). Learning from mixed signals in online innovation communities. Organization Science, 29(6) 1010–1032.

Shah, S., & Nagle, F. (2019). Why do user communities matter for strategy? Harvard Business School Strategy Unit Working Paper. pp. 19–126.

Singh, J., & Fleming, L. (2010). Lone inventors as sources of breakthroughs: Myth or reality? Management Science, 56(1), 41–56.

Stanko, M. A. (2016). Toward a theory of remixing in online innovation communities. Information Systems Research, 27(4), 773–791

Stephen, A. T., Zubcsek, P. P., & Goldenberg, J. (2016). Lower connectivity is better: The effects of network structure on redundancy of ideas and customer innovativeness in interdependent ideation tasks. Journal of Marketing Research, 53(2) 263–279.

Taylor, A., & Greve, H. R. (2006). Superman or the fantastic four? Knowledge combination and experience in innovative teams. Academy of Management Journal, 49(4), 723–740.

Terwiesch, C., & Xu, Y. (2008). Innovation contests, open innovation, and multiagent problem solving. Management Science, 54(9), 1529–1543.

Von Krogh, G. (2012). How does social software change knowledge management? Toward a strategic research agenda. The Journal of Strategic Information Systems. 21(2). 154–164

Wang, J., Ipeirotis, P., & Provost, F. (2017). Cost-Effectie quality Assurance in Crowd-Labeling. Information Systems Research, 28(1), 137–158.

Wang, Z., & Hahn, J. (2015). Crowd Experience and Performance: An Empirical Analysis of Crowdsourced New Product Development, Proc, International Conference on Information Systems (ICIS). Eort Worth. TX

Wasko, M. M., & Faraj, S. (2005). Why should I share? Examining social capital and knowledge contribution in electronic net works of practice. MIS Quarterly, 29(1), 35–57.

Weber, R. (2012). Evaluating and developing theories in the information systems discipline. Journal of the Association for Information Systems, 13:1, 2

Wooten, J. O., & Ulrich, K. T. (2017). Idea generation and the role of feedback: Evidence from field experiments with innova tion tournaments. Production and Operations Management, 26(1), 80–99.

Yang, J., Adamic, L., & Ackerman, M. (2008). Crowdsourcing and Knowledge Sharing: Strategic User Behavior on Taskcn. ACM Conference on Electronic Commerce, Chicago, pp. 246–255.

Ye, H., & Kankanhalli, A. (2015). Investigating the antecedents of organizational task crowdsourcing. Information & Management, 52(1), 98–110.

Ye, H., & Kankanhalli, A. (2017). Solvers' participation in crowdsourcing platforms: Examining the impacts of trust, and benefit and cost factors. Journal of Strategic Information Systems, 26(2), 101–117.

Ye, H. J. (2022). Effects of learning and uncertainty on crowdsourcing performance of solvers: Insights from performance feedback theory. Internet Research, Forthcoming.

Ye, H. J., Blohm, I., Breschneider, U., Goswami, S., Leimeister, J. M., & Krcmar, H. (2016). Promoting the Quality of User Generated Ideas in Online Innovation Communities: A Knowledge Collaboration Perspective. International Conference o Information Systems, Dublin: Association for Information Systems.

Zheng, H., Li, D., & Hou, W. (2011). Task design, motivation, and participation in crowdsourcing contests. International Journal of Electronic Commerce, 15(4), 57–88.

Zheng, H., Xu, B., Zhang, M., & Wang, T. (2018). Sponsor's Cocreation and psychological ownership in reward-based crowdfunding. Information Systems Journal, 28(6), 1213–1238

## AUTHOR BIOGRAPHIES

Hua (Jonathan) Ye is an associate professor in the MIS Division of the Price College of Business at the University of Oklahoma. His research interests include IT-enabled open innovation, user-generated content, crowdsourcing as well as service innovation. His research has been published in top journals for example, MIS Quarterly, Journa of Management Information Systems, Journal of the Association for Information Systems, Journal of Strategic

Information Systems, Information & Management, Information Systems Frontiers, Service Science, Computers in Human Behaviour, Electronic Commerce Research and Applications, and so forth and premium conferences. He has been serving as the Associate Editor for the European Journal of Information Systems, Information Systems Frontiers, Electronic Commerce Research and Applications and IEEE Transactions on Engineering Management

Matthew L. Jensen is an associate professor of Management Information Systems and a co-director of the Center for Applied Social Research at the University of Oklahoma. His interests include computer-aided decision making, human-computer interaction, and computer-mediated communication. He studies how people attribute credibility in mediated interactions and how people filter and evaluate information they find online. His research has been published in the Journal of Management Information Systems, Information Systems Research, MIS Quarterly, and other journals. He has been the primary investigator or co-primary investigator on externally funded research projects totaling more than \$8 million.

How to cite this article: Ye, J. (H.), & Jensen, M. (2022). Effects of introducing an online community in a crowdsourcing contest platform. Information Systems Journal. 32(6). 1203-1230, https://doi,org/10.1111/isi 12397

## APPENDIX A: LITERATURE REVIEW

To accurately gauge the state of the knowledge surrounding the emergence of online communities in crowdsourcing contests, we conducted a systematic examination of the literature. We performed a Google Scholar search using th search terms crowdsourcing and online community . We limited our results to publications in the eight Senio Scholars Basket Journals (Haried et al., 2021) from 2015 to 2021. The search yielded a total of 80 candidate paper (EJIS: 6; ISJ: 6; ISR: 22; JAIS: 9; JIT: 8; JMIS: 11; JSIS: 5; MISQ: 13).

We then reviewed the abstracts of each of the candidate papers and removed papers that did not include origi nal research (e.g., literature reviews). We also excluded papers that did not address online communities in crowdsourcing or competitions in crowdsourcing. This process resulted in 12 papers that are conceptually proxima to our phenomenon of interest. A summary of these papers, including a summary of their findings, theoretica approach, and methods, is produced in Table A1.

TABLE A1 Literature review on online community and crowdsourcing

<table><tr><td>References</td><td>Effects of introducing an online community?</td><td>Effects of prior experience?</td><td>Method: theoretical lens</td><td>Relevant findings</td></tr><tr><td>Dissanayake et al. (2021)</td><td>No</td><td>No</td><td>Econometrics analysis of archival data: social capital theory</td><td>Help offered by community members in highly competitive crowdsourcing contests is reciprocatedHelp from members improved crowdsourcing contest performance</td></tr><tr><td>Han et al. (2020)</td><td>No</td><td>No</td><td>Quantitative analysis of archival data: knowledge reuse for innovation model</td><td>Remixes of existing knowledge that include prevalent topics and integration metaknowledge generate more innovative solutions</td></tr><tr><td>Hutter et al. (2015)</td><td>No</td><td>No</td><td>Quantitative analysis of archival data: personality characteristics (Machiavellianism)</td><td>Contestants in a crowdsourced contest are prone to amoral manipulation, striving for status, and distrust of othersAmoral manipulation and striving for status lead to submitting fewer ideas and fewer commentsDistrust of others increases the number of ideas, number of comments, and quality of contributions</td></tr><tr><td>Ma et al. (2018)</td><td>No</td><td>No</td><td>Survey: intertemporal relationship mechanisms; motivation theory</td><td>Crowdworkers participation in online communities reduces their desire to quit crowdwork</td></tr><tr><td>Dissanayake et al. (2015)</td><td>No</td><td>Yes: Experience as intellectual capital</td><td>Econometrics analysis of archival data: social and intellectual capital</td><td>The effect of a contestant&#x27;s social and intellectual capital on team performance varies depending on roles (leader vs. expert)Highly competitive competitions exacerbate problems with misalignment of social and intellectual capital in leaders and experts</td></tr><tr><td>Huang et al. (2017)</td><td>No</td><td>No</td><td>Natural field experiments, difference in differences models: social presence theory</td><td>Platform integration with Facebook increased content and positive emotion in review textPlatform integration with Facebook decreased review quality, since positive, emotional reviews are less helpful</td></tr><tr><td>Mo et al. (2021)</td><td>No</td><td>Yes: Experience as similarity between tasks</td><td>Quantitative analysis of archival data: mechanisms for competing tasks and task quality</td><td>The number of contestants decreases as tasks grow, negatively impacting task qualityThe number of simultaneous tasks increases as tasks grow.Learning transfers between tasks, positively impacting quality</td></tr><tr><td>Stanko (2016)</td><td>No</td><td>No</td><td>Quantitative analysis of archival data: innovation diffusion theory</td><td>Interaction among members increases remixing by the communityFront page presence has little effect on remixing</td></tr></table>

TABLE A1 (Continued)

<table><tr><td>References</td><td>Effects of introducing an online community?</td><td>Effects of prior experience?</td><td>Method: theoretical lens</td><td>Relevant findings</td></tr><tr><td>Jin et al. (2021)</td><td>No</td><td>No</td><td>Quantitative analysis of archival data: motivations for knowledge sharing</td><td>Having a platform to share knowledge is not sufficient for knowledge sharing to occur in crowdsourcing platformsContestant performance increased by quality, and generativity of shared knowledgeContestant performance also increased by derivation breadth</td></tr><tr><td>Majchrzak and Malhotra (2016)</td><td>No</td><td>No</td><td>Qualitative analysis of archival data: framing of knowledge sharing structures</td><td>A paradox-framed trajectory was more likely to be followed by innovative outcomes</td></tr><tr><td>Lee et al. (2018)</td><td>No</td><td>Yes: Experience as experience amount</td><td>Quantitative analysis of archival data and survey: feedback and cognitive bias mechanisms</td><td>Salience bias influences the performance of contestants, including the winners of the contests.The number of participating contestants may alter the effect of the salience bias on the outcomes of contests, depending on task effort</td></tr><tr><td>Zheng et al. (2018)</td><td>No</td><td>Yes: Experience as intimate knowing</td><td>Quantitative analysis of archival data: Psychological Ownership Theory</td><td>Psychological ownership significantly affects their commitment to projectsCocreation alters perceived control and intimate knowing, which contribute to psychological ownership</td></tr></table>

APPENDIX B: PLATFORM AND COMMUNITY SCREENSHOTS

![](/api/attachments/ABTRPPKX/fulltext/images/6b0f38a826609844579b8db41568673a805f2b5b88e8764b7858451eb9ff9274.jpg)  
F I G U RE B 1 Screenshot of the forum

![](/api/attachments/ABTRPPKX/fulltext/images/cc02b43e8b076b202613b4a13ac67819984c765284b4bc8099442440fcbd98e2.jpg)  
F I G U R E B 2 Screenshot of contestant profile

## APPENDIX C: ROBUSTNESS CHECK

We used the data of contestants three months before the launch of the online communities to match the contro group with the treatment group. The results in Table C1 are largely the same as those in Tables 5 and 6, except for the significance of the moderating effect of experience diversity.

T A B L E C 1 PSM robustness check with new matching data

<table><tr><td></td><td>Winning  $contests_{it}$ </td><td>Crowdsourcing  $income_{it}$ </td></tr><tr><td> $Post-treatment_t$ </td><td>0.352*** (0.062)</td><td>0.125 (0.112)</td></tr><tr><td> $Treatment_i * Post-treatment_t$ </td><td>1.054*** (0.211)</td><td>2.747** (0.396)</td></tr><tr><td> $Treatment_i * Post-treatment_t * Ln(Experience Amount)_{it}$ </td><td>-0.223*** (0.045)</td><td>-0.215*** (0.070)</td></tr><tr><td> $Treatment_i * Post-treatment_t * Ln(Experience Diversity)_{it}$ </td><td>0.315** (0.078)</td><td>0.016* (0.008)</td></tr><tr><td> $Ln(Forum Contribution)_{it}$ </td><td>-0.035 (0.054)</td><td>0.037 (0.045)</td></tr><tr><td> $Ln(Experience Amount)_{it}$ </td><td>0.983*** (0.153)</td><td>0.073*** (0.022)</td></tr><tr><td> $Ln(Experience Diversity)_{it}$ </td><td>0.4537*** (0.031)</td><td>0.434*** (0.124)</td></tr><tr><td> $Ln(Tenure)_{it}$ </td><td>0.551 (0.447)</td><td>0.351* (0.162)</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td></tr><tr><td>Monthly dummy</td><td>Yes</td><td>Yes</td></tr><tr><td>R square</td><td>0.472</td><td>0.614</td></tr><tr><td>No. of observations</td><td>5856</td><td></td></tr></table>

Note: Clustered-robust standard errors (clustered on contestants) are reported.  
\*\*\*p < 0.001; \*\*p < 0.01; \*p < 0.05.

## APPENDIX D: CONTRIBUTION TABLES

Knowledge collaboration research (KCR) is a body of literature that explains individual behaviour in an online com munity while cognitive diversity research (CDR) is a body of literature that explains individual behaviour and perfor mance in general. Both theoretical foundations have a proximate conceptual space. KCR posits that individua characteristics and situational factors are important drivers of behaviour, while CDR highlights the importance of individual characteristics. They have overlap on some of their proposed antecedents (e.g., individual backgrounds and individual effort), but each provides unique explanations for some situational factors for human behaviour (e.g., experience amount, experience diversity). KCR and CDR share the common assumption that individuals are boundedly rational and that individuals have free will to control their behaviours. Therefore, they have compatibl assumptions. According to (Okhuysen & Bonardi, 2011), it is reasonable to combine the two perspectives

We followed the same procedure for discussing our theoretical contribution as Lowry et al. (2019). Table D1 characterises our research contributions using Corley and Gioia (2011)). Table D2 characterises our research contri butions using Weber (2012))

<table><tr><td colspan="4">TABLE D1 Theoretical contribution based on Corley and Gioia (2011)</td></tr><tr><td rowspan="2">Originality</td><td>Revelatory</td><td>Demonstrate the feasibility of introducing an online community on a crowdsourcing platformDemonstrate that providing a space for collaboration is helpful for competitive crowdsourcing (test the effects of communitition, offer guidelines on whether crowdsourcing platforms should invest in building an online community)Demonstrate interaction of experience diversity and experience amount with online communities to advantage certain contestants over others.</td><td>Develop knowledge collaboration research by exploring its contingencies based on cognitive diversityDevelop crowdsourcing literature by conceptualising the impacts of introducing an online community to create communitition platformExtend knowledge collaboration research which focuses on intra-community outcomes by exploring its spillover effect outside community outcomes, that is, crowdsourcing performanceChallenge the view that rational contestants will collaborate to decrease their competitiveness, for example, by helping others.Highlight boundary conditions antecedents to performance on communitition platforms based on experience amount and experience diversity</td></tr><tr><td>Incremental</td><td>Integrate knowledge collaboration research with cognitive diversity research to provide a more holistic view of online communities in crowdsourcingPractically useful</td><td>Not ApplicableScientifically useful</td></tr><tr><td colspan="4">Utility</td></tr></table>

T A B L E D 2 Contribution based on Weber (2012)

<table><tr><td>Evaluative aspects of a theory</td><td>Contributions of our theory beyond existing literature</td></tr><tr><td>Construct(s)</td><td>Our study focuses on theorising the impacts of technology artefact, that is, introducing an online community new technology construct.</td></tr><tr><td>Association(s)</td><td>Linearity and interaction, dynamic approach to study phenomenaCausality rather than correlation studied in prior literatureLongitudinal comparison (before/after comparison) versus cross-sectional studyExplore theory boundary/contingencies</td></tr><tr><td>State(s)</td><td>In our paper, there are two examples of states, that is, participated to the online community versus not participated to the online community, and before the presence of the online community versus after the presence of the online community</td></tr><tr><td>Event space</td><td>The primary components of this event space are the presence of an online community, contestant participation in the online community, contestant prior experience in influence contestant crowdsourcing performance.</td></tr><tr><td>Novelty</td><td>Testing the feasibility of communition in crowdsourcing platformsTheorising and causally inferring the impacts of introducing an online communityDemonstrating the interaction with between the presence of an online community and contestant experience quantity and diversityDeveloping knowledge collaboration research by contextualising it to this study, integrating it with cognitive diversity research for theory boundaries, and exploring its spillover effects on outer community outcomes (crowdsourcing performance)</td></tr></table>
