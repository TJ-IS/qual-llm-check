---
otero_id: 14524
otero_key: "EQBBP2M6"
title: "Co-membership, networks ties, and knowledge flow: An empirical investigation controlling for alternative mechanisms"
authors: "Gang Peng"
year: "2019"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2019.01.005"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Co-membership, networks ties, and knowledge flow: An empirical investigation controlling for alternative mechanisms

![](/api/attachments/EQBBP2M6/fulltext/images/807946db66a90ccde1a9b82ec71d08909019e909f2671f5b60cb2429f58043db.jpg)

Gang Peng

Information Systems and Decision Sciences, Mihaylo College of Business and Economics, California State University Fullerton, Fullerton, CA 92831, United States of America

## A R T I C L E I N F O

Keywords: Knowledge flow Co-membership Network ties Experiential learning Vicarious learning Open source software

## A B S T R A C T

Co-membership has been considered as a major mechanism for knowledge flow. However, alternative mechanisms exist for the observed knowledge flow. One of the efective ways to reduce the possibility of alternative mechanisms is to make use of online settings. However. even at online settings. individuals can still directly watch and learn from each other, resulting in knowledge flow. This study investigates the impact of co-mem bership under the unique context of open source software (OSS) development at GitHub. It finds that both comembership and watching are efective for knowledge flow, which further increases OSS development technical success, measured as project commits. Moreover, the impact of co-membership is much stronger than watching. While co-membership is indeed an efective mechanism for knowledge flow, its impact tends to be biased without controlling for alternative mechanisms.

## 1. Introduction

Network ties are known to channel knowledge and expertise among teams or organizations, and further influence their performance and decision-making [1]. Network ties can arise from various mechanisms and one of the most important mechanisms is co-membership [2–4]. Members of a team or an organization can simultaneously participate in other teams or organizations, and therefore they become co-members between these teams or organizations. These co-members can potentially channel knowledge and expertise across the teams or organizations that are connected. As such co-membership is widely used to construct social networks to study knowledge flow and its impact.

However, while co-membership can be important, there are other possible mechanisms through which learning and knowledge flow can potentially occur, confounding the impact of co-membership. The challenge therefore is that, to establish a cleaner relationship between co-membership and knowledge flow, alternative mechanisms need to be controlled.

In real world, many alternative mechanisms may exist because individuals can get in touch with each other in numerous ways. In com parison, online or virtual settings can efectively reduce the possibility of alternative mechanisms—individuals online are distributed world wide and they might have never met or will never meet in person; as such the only viable venue for them to interact with each other is through online platforms. As such, online settings can efectively reduce the possibility of alternative mechanisms for knowledge flow.

However, even under online settings, there still exist other possible mechanisms through which knowledge and expertise can flow. The most important and often cited mechanism is direct watching or lurking online [5]. Prior studies have commented that individuals can directly watch other projects' development activities online and learn from them without joining these projects as members [6]. Thus, the following questions remain unanswered: 1) Does co-membership really matter for knowledge flow and thus can serve as an efective mechanism for constructing social networks? 2) As direct watching is often unobservable, how to control for it as an alternative mechanism for learning and knowledge flow? 3) Which mechanism, co-membership or watching, is more influential or efective for leaning and knowledge flow?

We intend to address the above questions in this study. Specifically, we use GitHub to examine the impact of co-membership and watching for learning and knowledge flow.<sup>1</sup> GitHub is currently the most popular hosting website for open source software (OSS) project development. It possesses the features aforded by traditional online platforms such as SourceForge.net and thus allows us to trace project co-membership. At the same time, it also exhibits certain features of social media such as watching, thus allowing us to tease out the learning efect due to direct watching. By controlling for both co-membership and watching through this unique online setting, we find that: 1) Co-membership indeed plays a critical role for learning and knowledge flow, even after controlling for watching. 2) Projects also learn from each other through the mechanism of watching, and without controlling for watching, the esti mated impact of co-membership tends to be biased upward. 3) The impact of co-membership is much stronger than that of watching in influencing leaning and knowledge flow.

Table 1  
Studies using co-membership to construct online social networks.

<table><tr><td>Studies</td><td>Levels of analysis</td><td>Related research findings</td></tr><tr><td>[16]</td><td>Individual</td><td>An editor&#x27;s centrality in the Wikipedia collaboration network is positively correlated to the editor&#x27;s total contribution and allocation of efforts.</td></tr><tr><td>[17]</td><td>Individual</td><td>Prior collaboration networks positively affect a developer&#x27;s decision to join a newly initiated OSS project.</td></tr><tr><td>[18]</td><td>Individual</td><td>Participation in industry events is positively related to an entrepreneur&#x27;s brokerage position in an industry network.</td></tr><tr><td>[19]</td><td>Project</td><td>The network position of the user-generated content in the content-contributor network is positively related to its viewership.</td></tr><tr><td>[20]</td><td>Project</td><td>Network ties of leader-follower type and follower-leader type are more beneficial to OSS success than other types of ties.</td></tr><tr><td>[21]</td><td>Project</td><td>Network centrality and internal cohesion positively affect the success of OSS projects.</td></tr><tr><td>[22]</td><td>Project</td><td>Network ties positively affect knowledge flow across OSS projects.</td></tr><tr><td>[23]</td><td>Project</td><td>Active human participation positively moderates the impact of network ties and resources on OSS success.</td></tr><tr><td>[12]</td><td>Project</td><td>Network centrality and closure among current adopters contribute positively to future technology adoption, whereas the same among potential adopters has the opposite impact.</td></tr><tr><td>[24]</td><td>Project</td><td>Software decoupling positively moderates the impact of network centrality on OSS project success.</td></tr><tr><td>[25]</td><td>Project</td><td>The license choice of a new OSS project is affected by the license types of connected OSS projects.</td></tr><tr><td>[26]</td><td>Project</td><td>OSS project internal cohesion has a positive impact on OSS project success, but external cohesion has a curvilinear relationship with project success.</td></tr><tr><td>[27]</td><td>Project</td><td>A project founder&#x27;s network centrality and brokerage reduce the time to release user-generated open source products.</td></tr><tr><td>[28]</td><td>Project</td><td>There are both direct and indirect knowledge spillovers across OSS projects through network ties.</td></tr><tr><td>[29]</td><td>Project</td><td>The position of a Wikipedia article in the affiliation network is positively associated with the quality of the article.</td></tr></table>

The rest of the paper proceeds as follows: Section 2 discusses prior literature and research background. Section 3 develops theory and testable hypotheses. Section 4 describes datasets and variables. Esti mation models and results, including robustness tests, are presented in Section 5. Finally, in Section 6 we summarize our findings, discuss our contributions, describe limitations, and ofer future research directions.

## 2. Literature review and research background

Knowledge has been defined as “justified true belief” that increases one's capacity for efective actions [7]. Knowledge is most widely conceptualized as tacit or explicit. Tacit knowledge is based on experience, insights, and intuitions in specific contexts, while explicit knowledge is articulated, codified, and communicated in symbolic forms [7,8]. Knowledge flow describes the process through which knowledge is channeled from the source to the destination, so that the knowledge state of one actor is afected by another [9]. For knowledge flow to occur, network ties between actors have to be established. It is through these ties that knowledge from the source is passed on to the destination. Therefore, network ties play a critical role for knowledge flow [10–12].

Network ties can arise from various mechanisms, such as friendship, alliance, mobility, and advice. One of the frequently invoked mechanisms is co-membership. Members of a team carry knowledge developed and accumulated from working with the team. When they simultaneously join another team, they become “co-members” of the two teams, and they bring knowledge accumulated previously to the other team, and thus transferring knowledge to the other team. The efect of co-membership on knowledge flow and eventually performance and decision-making has been widely documented under various settings. For example, prior literature suggests that member mobility can be efective for knowledge flow and performance improvement [9]. Similarly, business board-interlock can difuse expertise and influence decision-making across firms [13], co-members of TV production teams can bring in knowledge and expertise for movie production [4], and software development projects can benefit from knowledge leveraged by co-members [2].

Co-membership not only exists in physical world, but also in online settings. For example, in OSS development, a project team consists of multiple developers or project members, who in turn may participate in other projects. Thus, these developers become co-members between the projects. In this research, we distinguish between a focal project and a connected project: a focal project is the project under study, and a connected project is a project that is connected to the focal project through co-members. When a co-member works on a connected project, he can exchange ideas and discuss issues with other members through such tools as discussion forums, email lists, and bug tracker systems [14], and subsequently he learns from others and gains expertise and knowledge from participating in the connected project. Indeed, learning has been identified as one of the major motivations for OSS participation [15]. Furthermore, when the co-member works on the focal project, other members of the focal project learn and gain expertise from him as well. Therefore, through co-membership, knowledge and expertise can flow from the connected projects to the focal project. Efectively, co-membership constitutes network ties between OSS projects and acts as a conduit for knowledge flow across project boundaries. Through co-members, useful information and knowledge, including innovative ideas and techniques for OSS development, can be channeled across projects, influencing the success of OSS projects [2].

As such, project co-membership has been widely adopted to construct social networks among OSS or wiki projects. Table 1 summaries some key studies we found that have adopted co-membership to construct online social networks. A common finding of these studies is that co-membership is an efective mechanism for knowledge flow.

However, the impact of co-membership on knowledge flow has not always been positive. For example, some studies find no or even negative relationship between co-membership and knowledge flow [30,31]. What is more worrying is that, to the best of our knowledge, no prior studies have actually controlled for alternative mechanisms because it is very hard if not impossible to do so—in physical world, there are so many ways people can get in touch with each other and thus there are numerous channels through which expertise and knowledge can flow, such as co-workers, friendships, associations, memberships, alumni, gatherings, and conferences.

As mentioned earlier, traditional online development platforms, such as SourceForge, Wikipedia, or many other virtual environments, can efectively reduce the possibility of alternative mechanisms for knowledge flow, as interactions between participants typically occur online. However, other alternative mechanisms can still exist, and the most prominent one is watching. Surprisingly, when we examine the studies listed in Table 1, we do not find any evidence for controlling for this alternative mechanism that can possibly lead to the observed knowledge flow. Part of the reason is because there is virtually no way to keep track of watching under traditional online development platforms.

In this study, we examine the impact of co-membership on knowl edge flow under the setting of OSS project development at GitHub.

![](/api/attachments/EQBBP2M6/fulltext/images/422ad5e03017fa373598a5e72267ce9ca2ded90032cb35a5800efe35b81a3250.jpg)  
Fig. 1. Snapshots of a GitHub project.

GitHub not only provides features aforded by SourceForge or Wikipedia, but also afords features of social media where developers can directly watch and observe others that are of interest to developers [32]. By explicating the watching behavior, GitHub can help control for the potential alternative mechanism of watching. Therefore, our research setting provides a unique opportunity to better control for alternative mechanisms and trace out the impact of co-membership on learning and knowledge flow.

As a software development platform, GitHub provides a project repository through git, a distributed software version control system. At the same time, GitHub also acts as a social networking virtual space for developers [33]. Just like other social networking applications, developers at GitHub can “follow” other developers or “watch” other projects by subscribing them to a feed with frequent updates of other projects activities [6,32,34]. Fig. 1 shows a snapshot of a typical project at GitHub.<sup>2</sup> The project has 5 members who have made 389 commits to its code repository. Most importantly, it is being watched by 41 developers at the time. Usually, popular projects tend to be watched more often and have more followers [35].

## 3. Theory and hypotheses

The literature on learning and knowledge flow is vast and has a long history [36]. Learning can occur at various levels and through various mechanisms. Learning can be realized through ones' own experience or the experience of others [37]. Through learning, individuals, teams, and organizations accumulate stocks of knowledge, which can be applied to future activities. In this research, we adopt the view that team learning is an aggregate of the learning by team members [38,39].

## 3.1. Learning through co-membership

Project members learn by working on the project, and when they move on to new projects or work concurrently on other projects, they apply what they learnt to other projects [4]. Equivalently, these members become knowledge reservoirs and when they move, they carry the knowledge, expertise, and experience with them [9]. Learning from one's own experience has been referred to as experiential learning [40]. Experiential learning is particularly efective for gaining tacit knowledge that cannot be acquired easily through other types of learning. The impact of experiential learning on software development has been observed early on. For example, when developing the first real-time online air ticket reservation system, SABRE, many developers had participated in a prior project SAGE. Consequently, SABRE bene fited greatly from SAGE not only by reusing its innovative ideas, but also by avoiding many pitfalls in system development and project management [41]. Similarly, the development of FreeBSD, an OSS Unix like operating system, benefited greatly from 386BSD, a relatively mature and stable operating system software, as many of the developers on FreeBSD used to work on 386BSD [42,43]. At project level, through co-membership, the focal project is connected to other projects which share these co-members. The more connected projects the focal project has, the more knowledge and expertise can potentially flow into the focal project, increasing the odds of its success:

H1. OSS project success is positively associated with the number of connected projects.

## 3.2. Learning through watching

In an online social computing platform, developers can watch activities of other projects. At GitHub, it has been documented that de velopers learn by observing other projects or developers [6]. Once a project is set to be watched, all the activities of the project will be forwarded to the follower automatically through feeds [6,34]. By watching other projects and getting updates on changes, developers learn how their technical peers were approaching related problems, informing their own development [6]. Therefore, through watching, the follower can examine and keep updated of the development activities of the watched projects and learn from them. Distinct from experiential learning or learning from one's own experience, learning from others' experience is referred to as vicarious learning [44,45]. Vicarious learning is important for OSS development. First, OSS development consumes scarce resources, such as time, energy, and cognitive and computational eforts [46]. By taking advantage of others' experience and expertise, the focal project can economize the cost in decisionmaking, save their scarce cognitive eforts and resources, and improve the odds of making the right decision. Second, vicarious learning helps apply experience and expertise of other projects to the focal project and yield insights that potentially can increase success of the focal project. Third, vicarious learning can also reduce risks associated with decision making. Uncertainty is intrinsic in OSS development [33]. When faced with the many tasks of software development, the focal project observes the actions of other projects and takes into consideration the experience and lessons of others. In doing so, they can reduce the uncertainty associated with project development and enhance the success of the project.

At project level, members of a focal project may watch many other projects, and through watching or vicarious learning, the focal project as a whole can gain knowledge and expertise, accumulate experience, and apply them to the focal project to enhance the odds of its success:

H2. OSS project success is positively associated with the number of projects that the focal project is watching.

## 3.3. Co-membership vs watching

As discussed above, co-membership and watching can both act as network ties and represent two diferent mechanisms for learning. A practical question to ask is: which mechanism is more efective? In the context of OSS development, we believe co-membership is more effective than watching in afecting knowledge flow and project success. First, being able to work on the connected projects directly allows developers to gain first-hand experience and knowledge, which in turn afords developers confidence in applying what they have learnt to the focal project. Although watching can speed up and economize cost of learning, these experience and knowledge are second-hand and thus can potentially cast doubt on their applicability to the focal project. Second, experience and knowledge through watching lack details and accuracy, thus they are hard to be implemented for the focal project. Third, compared to second-hand information, direct experience through co-membership lasts longer in memory and can be recalled and acted upon easier when needed [47]. Therefore, although both comembership and watching are expected to be efective for learning and knowledge flow, the former tends to be more powerful since the first hand learning tends to be more relevant, accurate, and lasts longer:

H3. The impact of co-membership is stronger than that of watching in afecting OSS project success.

## 4. Datasets and variables

To test hypotheses, we use datasets obtained from GitHub. Since established in February 2008, GitHub has grown rapidly into the world's largest hosting website for OSS project development. GitHub integrates a number of social features which allow developers and their activities to be visible within and across OSS projects [6]. At GitHub, project members are those who make code commits to a project.<sup>3</sup>

We took two snapshots of the whole projects at GitHub, one on January 8, 2016 and the other on November 11, 2016. Two datasets are built from them accordingly. The first one is used to construct independent variables in this study, and the second one, together with the first one. is used to construct the dependent variable.

There are 25,364,494 projects in the first dataset. However, as noted by prior studies that many of the projects are inactive [48]. Therefore, we restrict our sample to active projects, i.e., those have made any code commits during the study period, and this reduces the sample to 1,417,028. We further restrict the sample to projects that are not forked from any other projects—as commented by prior studies, forking makes it dificult to clearly identify the commits of the projects that are forked [33,46,48]; thus the sample is further reduced to 1,158,021. Since many of the projects are for individual use other than programming, we further restrict the sample to those having more than one member, and this leaves 308,127 projects which are used to construct the social networks we use in this study. All the network metrics in this study are based on the project universe of these projects. In total, 242 diferent programming languages are used to develop these projects. Fig. 2 shows the counts of the projects using the 14 most popular languages.

Because of the large number of projects, it is impractical to conduct analysis based on the whole project universe. Since Java is one of the most popular programming languages used at GitHub, and therefore, we focus on projects that use Java.<sup>4</sup> There are 21,786 Java projects among them.

From the first dataset, we construct two networks using the comembership and the watching mechanisms respectively. The steps for constructing the social network through co-membership is as follows: First, members of every focal (Java) project are identified; Second, for each member, the connected projects (out of the project universe identified) through co-members are identified; Third, all unique connected projects are counted as the number of alters to the focal project.<sup>5</sup> Next, we follow the same steps to construct the social network through the watching mechanism: First, members of every focal (Java) project are identified; Second, for each member, projects (out of the project universe identified) that are being watched by that member are identified; Third, all unique projects that are watched by the focal project are counted as alters\_watched.

![](/api/attachments/EQBBP2M6/fulltext/images/ab6d7aec087cde5300f523810c77cab036a0b8624fa5fe7bf4b380e47f2b467f.jpg)  
Fig. 2. Project Counts by Programming Languages at GitHub.

From the first dataset, we also construct other independent variables: project size, project age, project modularity, and member experience.

For the dependent variable, OSS project success, we use the number of code commits made by the focal project. Prior studies suggest that OSS projects have technical success as well as commercial success [2]. The number of code commits represents the technical success of OSS projects. We believe technical success is more relevant in our context, since it reflects how knowledge flow across projects can potentially contribute to learning and skill upgrade, which further increase code contribution. Specifically, we use the number of code commits made by the focal project during the study period, i.e., from January to November 2016—this represents the incremental changes made in the commits during the study period [49]. Through the time lag, we can use independent variables measured at an earlier time to explain the dependent variable that are afected by them at a later time. Because variables commits, alters, and alters\_watched are heavily right skewed, they are log-transformed for analysis. Detailed variable definitions are provided in Table 2.

## 5. Estimation results

## 5.1. Baseline results

We first present the correlation matrix in Table 3. It shows that variable commits is positively associated with both alters and alters\_watched, and this is consistent with our hypotheses.

In order to assess the degree of multicollinearity, we calculated the variance inflation factors (VIF) and the results are shown in Table 4. The VIF scores for all independent variables are well below the threshold of 10; therefore, multicollinearity is not an issue for our study [50].

To test if heteroscedasticity is present for our estimation, we conduct Breusch-Pagan test [51]. We reject the null that there is no heteroscedasticity in our data $( \chi ^ { 2 } = 4 2 9 . 9 5$ and $p \ < \ 0 . 0 0 1 ) ;$ therefore, we report the heteroscedasticity-robust standard errors in our results.

Table 2 Variable definitions.

<table><tr><td>Variables</td><td>Definitions</td></tr><tr><td>Commits</td><td>The logarithm of commits made by the focal project between January and November 2016. It measures OSS project technical success.</td></tr><tr><td>Alters</td><td>The logarithm of the total number of connected projects. It measures the impact of co-membership.</td></tr><tr><td>Alters_watched</td><td>The logarithm of the total number of projects that are watched by the focal project. It measures the impact of watching.</td></tr><tr><td>Project size</td><td>The total number of members of the focal project</td></tr><tr><td>Project age</td><td>The age (in months) of the focal project since its registration with GitHub until January 2016</td></tr><tr><td>Project modularity</td><td>The number of projects that fork from the focal project</td></tr><tr><td>Member experience</td><td>The average experience (in months) of the members of the focal project since their registration with GitHub until January 2016</td></tr></table>

Table 3  
Variable correlation matrix.

<table><tr><td>Variables</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td></tr><tr><td>1. Commits</td><td>-</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Alters</td><td>0.138***</td><td>-</td><td></td><td></td><td></td><td></td></tr><tr><td>3. Alters_watched</td><td>0.173***</td><td>0.455***</td><td>-</td><td></td><td></td><td></td></tr><tr><td>4. Project size</td><td>0.282***</td><td>0.398***</td><td>0.409***</td><td>-</td><td></td><td></td></tr><tr><td>5. Project age</td><td>0.044**</td><td>0.235***</td><td>0.255***</td><td>0.251***</td><td>-</td><td></td></tr><tr><td>6. Project modularity</td><td>0.148***</td><td>0.190***</td><td>0.278***</td><td>0.526***</td><td>0.215***</td><td>-</td></tr><tr><td>7. Member experience</td><td>0.011*</td><td>0.384***</td><td>0.362***</td><td>0.143***</td><td>0.473***</td><td>0.105***</td></tr></table>

Notes: $N = 2 1 , 7 8 6$  
⁎⁎⁎ $p \ < \ 0 . 0 1 .$  
⁎⁎ $\begin{array} { r } { p \ < \ 0 . 0 5 . } \end{array}$  
⁎ $p < 0 . 1 .$

Table 4  
Variance inflation factors (VIF).

<table><tr><td>Independent Variables</td><td>VIF</td></tr><tr><td>Alters</td><td>1.43</td></tr><tr><td>Alters_watched</td><td>1.47</td></tr><tr><td>Project size</td><td>1.69</td></tr><tr><td>Project age</td><td>1.25</td></tr><tr><td>Project modularity</td><td>1.40</td></tr><tr><td>Member experience</td><td>1.36</td></tr><tr><td>Mean VIF</td><td>1.43</td></tr></table>

We apply three estimation models to test the hypotheses: ordinary least squares (OLS), generalized linear model (GLM), and the Bayesian linear regression (BLR). The last two models are more robust to OLS assumptions, particularly the i.i.d. assumption. The baseline estimation results are shown in Table 5.

Model 1 includes only the control variables $( \mathrm { R } ^ { 2 } = 0 . 0 8 1 )$ . The coeficient on project size is positive and significant (b = 0.048 and $p \ : < \ : 0 . 0 1 )$ . This suggests that as projects attract more members, more commits are made, which is expected. On the other hand, the coeficient on project age is negative and significant $( b = - 0 . 0 0 2$ and $\begin{array} { r } { p \ < \ 0 . 0 5 ) \ : } \end{array}$ as time passes, projects tend to make less commits. This echoes the observation that most of commits are made in the early stage when projects first get started [24]; however, the coding frenzy may subside as projects mature. Project modularity is positive but is not significant. Again, this is expected: modularity may increase coding activities due to easiness for concurrent coding, but at the same time it may reduce coding activities due to code reuse [52], and thus the impact of modularity is mixed. Last, member experience is negative and significant $( b = - 0 . 0 0 2$ and $p \ : < \ : 0 . 0 1 )$ ; this also makes sense: as members stay longer with GitHub, they tend to be less active due to subsiding of enthusiasm.

Model 2 $\colon ( \mathbf { R } ^ { 2 } = 0 . 0 9 5 )$ and Model 3 $( \mathrm { R } ^ { 2 } = 0 . 1 0 6 )$ further add alters, alters<sup>2</sup> (alters squared), and alters\_watched. Since the independent variable alters and the dependent variable commits are log-transformed, the coeficient on alters represents the percentage change of the absolute number of commits given 1% increase in the number of connected projects. The coeficient on alters\_watched in Model 3 takes the same interpretation.

Table 5  
Estimation of project success.

<table><tr><td>Independent variables</td><td>Model 1 (OLS)</td><td>Model 2 (OLS)</td><td>Model 3 (OLS)</td><td>Model 4 (GLM)</td><td>Model 5 (BLR)</td></tr><tr><td rowspan="2">Alters</td><td></td><td>0.211***</td><td>0.175***</td><td>0.071***</td><td>0.178***</td></tr><tr><td></td><td>(0.020)</td><td>(0.023)</td><td>(0.016)</td><td>(0.024)</td></tr><tr><td rowspan="2"> $Alters^2$ </td><td></td><td>-0.021***</td><td>-0.018***</td><td>-0.007***</td><td>-0.018***</td></tr><tr><td></td><td>(0.002)</td><td>(0.003)</td><td>(0.002)</td><td>(0.003)</td></tr><tr><td rowspan="2">Alters watched</td><td></td><td></td><td>0.075***</td><td>0.030***</td><td>0.076***</td></tr><tr><td></td><td></td><td>(0.009)</td><td>(0.007)</td><td>(0.010)</td></tr><tr><td rowspan="2">Project size</td><td>0.048***</td><td>0.043***</td><td>0.040***</td><td>0.012***</td><td>0.039***</td></tr><tr><td>(0.002)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">Project age</td><td>-0.002**</td><td>-0.002***</td><td>-0.003***</td><td>-0.001**</td><td>-0.003***</td></tr><tr><td>(0.0008)</td><td>(0.0008)</td><td>(0.0008)</td><td>(0.0005)</td><td>(0.001)</td></tr><tr><td rowspan="2">Project modularity</td><td>0.004</td><td>0.012</td><td>0.004</td><td>-0.003</td><td>0.004</td></tr><tr><td>(0.023)</td><td>(0.015)</td><td>(0.015)</td><td>(0.011)</td><td>(0.016)</td></tr><tr><td rowspan="2">Member experience</td><td>-0.002***</td><td>-0.010***</td><td>-0.013***</td><td>-0.005***</td><td>-0.013***</td></tr><tr><td>(0.0007)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td>N</td><td>21,786</td><td>18,290</td><td>16,271</td><td>16,271</td><td>16,271</td></tr></table>

Notes: estimated coeficients and their associated standard errors (in parentheses) are listed under each model  
<sup>⁎⁎⁎</sup> p < 0.01.  
⁎⁎ $\begin{array} { r } { p \ < \ 0 . 0 5 . } \end{array}$

First, in Model 2 the coeficient on alters is positive and significant $( b = 0 . 2 1 1$ and $p \ < \ 0 . 0 1 )$ ), suggesting that 1% increase of the number of connected projects will increase the absolute number of commits by 0.211%. This impact is quite sizable. In Model 3, while the coeficient on alters is also positive and significant $( b = 0 . 1 7 5$ and $p \ : < \ : 0 . 0 1 )$ , it is lower than that in Model 2. The implication is that without controlling for the alternative mechanism of watching, and impact of co-membership will be biased upward, thus echoing the caveat in prior literature that it is necessary to control for alternative mechanisms when estimating the impact of co-membership [12]. In addition, the coeficient on alters<sup>2</sup> is negative and significant in both Model 2 and Model 3. This suggests that excessive number of alters may backfire, hurting the development of the focal project. This makes sense—co-membership requires members of the focal project to contribute codes to the connected projects as well, and as the number of alters continues to grow, these members will need to allocate and divert increasingly more time and energy to the connected projects, eventually hurting the develop ment of the focal project.<sup>6</sup>

The results from GLM and BLR are listed in Model 4 $( \mathrm { A I C } = 4 . 2 3 8 )$ and Model 5 ${ \overline { { ) } } } ( \sigma ^ { 2 } = 2 . 8 7 8 ) . ^ { 7 }$ The results are similar to those from Model 3. Taking into account the results from Model 3 to Model 5, it can be seen that the coeficients on alters and alters\_watched are both positive and significant, and thus H1 and H2 are supported that both co-membership and watching are efective for OSS project success. Furthermore, the coeficient on alters is much higher than that on alters\_watched across all models $( \boldsymbol { \mathrm { e . g . } } ,$ , F-statistics = 13.4 and $p \ < \ 0 . 0 1$ in Model 3), and therefore H3 is also supported that co-membership is more powerful than watching in afecting OSS project success. Indeed, in Model 3, the coeficient on alters is more than twice that on alters\_watched, suggesting that the percentage change of the number of commits due to 1% increase of connected projects is more than double that due to 1% increase of projects being watched.

## 5.2. Robustness tests

To further validate our results, we conduct three robustness tests below. They are related to construction of network ties, choice of a refined dependent variable, and the use of a second project sample.

## 5.2.1. Duplicated network ties

In Section 5.1. we count the unique connected projects as variable alters. This is because knowledge and expertise channeled from the same connected project by diferent members tend to be the same and thus redundant. However, one might argue that diferent members may focus on diferent aspects of the same connected project and therefore can bring in diferent expertise and knowledge. To account for this possibility, in the first robustness test, we count all projects connected by project members as alters, without restricting these projects to be unique. Similarly, we also count all projects that are watched by the focal project as variable alters\_watched, regardless of their uniqueness. We run the same analysis as in Table 5 and provide the results in Table 6.

It can be seen that the results are qualitatively the same as in Table 5: across all models, the coeficients on alters and alters\_watched are both positive and significant $( p < 0 . 0 1 )$ , supporting H1 and H2. Moreover, coeficient on alters is much higher than that on alters\_watched (e.g., F-statistics = 47.57 and $p \ < \ 0 . 0 1$ in Model 3), and therefore H3 is also supported.

## 5.2.2. Refined project commits

In our sample, although none of the projects are forked from other projects, but it is possible that a focal project may have forked projects, which make commits to the focal project through pull requests. These commits may not be merged into and become codes of the focal project. Therefore, unmerged code commits may not represent success of the focal proiect. In our second robustness test, we exclude these unmerged commits when calculating the dependent variable commits. We then run the same analysis as in Table 5 and report the results in Table 7. First, these results are consistent with the baseline results from Table 5: the coeficients on alters and alters\_watched are both positive and significant $( p < 0 . 0 1 )$ , and the coeficient on alters is much higher than that on alters\_watched (e.g., F-statistics = 14.33 and $p \ < \ 0 . 0 1$ in Model 3).

Table 6  
Estimation of project success (using duplicated network ties).

<table><tr><td>Independent variables</td><td>Model 1 (OLS)</td><td>Model 2 (OLS)</td><td>Model 3 (OLS)</td><td>Model 4 (GLM)</td><td>Model 5 (BLR)</td></tr><tr><td rowspan="2">Alters</td><td></td><td>0.210***</td><td>0.255***</td><td>0.099***</td><td>0.253***</td></tr><tr><td></td><td>(0.020)</td><td>(0.023)</td><td>(0.016)</td><td>(0.022)</td></tr><tr><td rowspan="2"> $Alters^2$ </td><td></td><td>-0.021***</td><td>-0.027***</td><td>-0.010***</td><td>-0.027***</td></tr><tr><td></td><td>(0.002)</td><td>(0.003)</td><td>(0.002)</td><td>(0.003)</td></tr><tr><td rowspan="2">Alters watched</td><td></td><td></td><td>0.071***</td><td>0.029***</td><td>0.069***</td></tr><tr><td></td><td></td><td>(0.009)</td><td>(0.006)</td><td>(0.009)</td></tr><tr><td rowspan="2">Project size</td><td>0.048***</td><td>0.044***</td><td>0.041***</td><td>0.012***</td><td>0.041***</td></tr><tr><td>(0.002)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td rowspan="2">Project age</td><td>-0.002**</td><td>-0.002***</td><td>-0.003***</td><td>-0.001*</td><td>-0.003***</td></tr><tr><td>(0.0008)</td><td>(0.0008)</td><td>(0.0008)</td><td>(0.0006)</td><td>(0.001)</td></tr><tr><td rowspan="2">Project modularity</td><td>0.004</td><td>0.012</td><td>0.001</td><td>-0.004</td><td>-0.015</td></tr><tr><td>(0.023)</td><td>(0.015)</td><td>(0.015)</td><td>(0.011)</td><td>(0.011)</td></tr><tr><td rowspan="2">Member experience</td><td>-0.002***</td><td>-0.010***</td><td>-0.014***</td><td>-0.005***</td><td>-0.014***</td></tr><tr><td>(0.0007)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td><td>(0.001)</td></tr><tr><td>N</td><td>21,786</td><td>18,290</td><td>16,271</td><td>16,271</td><td>16,271</td></tr></table>

Notes: estimated coeficients and their associated standard errors (in parentheses) are listed under each model  
<sup>⁎⁎⁎</sup> p < 0.01.  
<sup>⁎⁎</sup> p < 0.05.

$$
^ {*} p <   0. 1.
$$

Estimation of project success (excluding unmerged commits)

<table><tr><td>Independent variables</td><td>Model 1 (OLS)</td><td>Model 2 (OLS)</td><td>Model 3 (OLS)</td><td>Model 4 (GLM)</td><td>Model 5 (BLR)</td></tr><tr><td>Alters</td><td></td><td>0.184***(0.020)</td><td>0.161***(0.023)</td><td>0.068***(0.017)</td><td>0.146***(0.019)</td></tr><tr><td> $Alters^2$ </td><td></td><td>-0.018***(0.002)</td><td>-0.016***(0.003)</td><td>-0.007***(0.002)</td><td>-0.015***(0.002)</td></tr><tr><td>Alters watched</td><td></td><td></td><td>0.059***(0.009)</td><td>0.025***(0.007)</td><td>0.060***(0.010)</td></tr><tr><td>Project size</td><td>0.046***(0.002)</td><td>0.042***(0.001)</td><td>0.039***(0.001)</td><td>0.013***(0.001)</td><td>0.038***(0.002)</td></tr><tr><td>Project age</td><td>-0.002**(0.0008)</td><td>-0.002***(0.0008)</td><td>-0.003***(0.0008)</td><td>-0.001*(0.0005)</td><td>-0.002***(0.001)</td></tr><tr><td>Project modularity</td><td>-0.010(0.023)</td><td>0.001(0.018)</td><td>-0.006(0.018)</td><td>-0.007(0.012)</td><td>-0.005(0.017)</td></tr><tr><td>Member experience</td><td>-0.002***(0.0007)</td><td>-0.009***(0.001)</td><td>-0.012***(0.001)</td><td>-0.005***(0.001)</td><td>-0.012***(0.001)</td></tr><tr><td>N</td><td>21,176</td><td>17,733</td><td>15,744</td><td>15,744</td><td>15,744</td></tr></table>

Notes: estimated coeficients and their associated standard errors (in parentheses) are listed under each model.  
<sup>⁎⁎⁎</sup> p < 0.01.  
<sup>⁎⁎</sup> p < 0.05.  
${ \mathrm { ~  ~ p ~ } } < 0 . 1 .$

Second, it can be seen that the coeficients on alters and watched\_alters are slightly diminished compared to those from Table 5: this is expected because unmerged commits are excluded from the dependent variable.

## 5.2.3. Analyses using Python projects

Another concern one might have is how the sample selection might afect the results. Do the findings hold for projects using other programming languages? To address this concern, we choose projects using another popular programming language: Python. From the first dataset described in Section 4, we identify 24,875 Python projects satisfying our research criteria: active, not forked from other projects, and have more than one member. We then repeat the same steps to construct independent variables (including network ties) and dependent variable. We then test the hypotheses using this new sample of Python projects. The results are provided in Table 8, and they correspond to the baseline results in Table 5.

Again, the results are qualitatively the same as those from Java projects: the coeficients on alters and alters\_watched are both positive and significant $( p < 0 . 0 1 )$ , and the coeficient on alters is much higher than that on alters\_watched (e.g., F-statistics = 27.05 and $p \ < \ 0 . 0 1$ in Model 3).

Table 8  
Estimation of project success (for Python projects).

<table><tr><td>Independent variables</td><td>Model 1 (OLS)</td><td>Model 2 (OLS)</td><td>Model 3 (OLS)</td><td>Model 4 (GLM)</td><td>Model 5 (BLR)</td></tr><tr><td>Alters</td><td></td><td>0.238***(0.019)</td><td>0.190***(0.022)</td><td>0.086***(0.015)</td><td>0.195***(0.017)</td></tr><tr><td> $Alters^2$ </td><td></td><td>-0.011***(0.002)</td><td>-0.007***(0.002)</td><td>-0.005***(0.002)</td><td>-0.008***(0.002)</td></tr><tr><td>Alters watched</td><td></td><td></td><td>0.059***(0.008)</td><td>0.017***(0.006)</td><td>0.057***(0.008)</td></tr><tr><td>Project size</td><td>0.013***(0.005)</td><td>0.011***(0.001)</td><td>0.010**(0.001)</td><td>0.005***(0.001)</td><td>0.010***(0.001)</td></tr><tr><td>Project age</td><td>-0.003**(0.001)</td><td>-0.004***(0.001)</td><td>-0.004***(0.001)</td><td>-0.002***(0.0005)</td><td>-0.004***(0.001)</td></tr><tr><td>Project modularity</td><td>-0.004(0.060)</td><td>0.009(0.018)</td><td>-0.001(0.018)</td><td>-0.026*(0.013)</td><td>-0.001(0.018)</td></tr><tr><td>Member experience</td><td>-0.008***(0.0007)</td><td>-0.018***(0.001)</td><td>-0.020***(0.001)</td><td>-0.008***(0.001)</td><td>-0.021***(0.001)</td></tr><tr><td>N</td><td>24,875</td><td>23,096</td><td>21,790</td><td>21,790</td><td>21,790</td></tr></table>

Notes: estimated coeficients and their associated standard errors (in parentheses) are listed under each model.  
<sup>⁎⁎⁎</sup> p < 0.01.  
<sup>⁎⁎</sup> p < 0.05.  
${ \mathrm { ~  ~ \cdot ~ } } p \ < \ 0 . 1 .$

In summary, results from the above three robustness tests are consistent with the baseline results. Therefore, our results are robust, and all three hypotheses are strongly supported.

## 6. Discussion and conclusion

Co-membership has been proposed as an efective mechanism for learning and knowledge flow. However, prior results have been hampered by the lack of controlling for alternative mechanisms. In this study we propose that online settings can efectively reduce the possibility of alternative mechanisms, and social computing platforms can further help control for another key confounding factor: online direct watching. This way we can better trace out the eficacy of co-membership on learning and knowledge flow. Specifically, by taking advantage of the unique opportunity aforded by GitHub, we identify two diferent mechanisms for knowledge flow and learning in this study: experiential learning through co-membership and vicarious learning through watching. We argue and empirically show that both mechanisms are efective for knowledge flow, which further lead to perfor mance improvement. Moreover, co-membership is more efective than watching. Our study makes both theoretical and practical contributions.

Although prior studies have shown the impact of co-membership, they do not control for alternative mechanisms. In this study, we show that learning and knowledge flow in the form of co-membership is indeed supported, even after controlling for alternative mechanisms through making use of an online platform and explicating the watching mechanism. With the accumulation of first-hand experience, members learn and accumulate knowledge from connected projects and apply it to the focal project to improve eficiency and economize cost. When faced with the constraints of time, cost, and most importantly uncertainty of the project development, project members are motivated to take advantage of learning from their own experience and apply what they have learnt to the focal project.

Literature suggests that vicarious learning is an efective way to gain access to valuable knowledge and information [5,44,45]. In OSS development, the social computing platforms such as GitHub also provide opportunities for vicariously learning through watching. We find that OSS development exhibits strong characteristics of vicarious learning through watching—observing peer projects afords the focal project the opportunity to learn second-hand information and knowledge from their peers and thus increasing performance of the focal project.

With the presence of both experiential learning and vicarious learning, one important question to ask is which mode of learning is more efective for performance or decision-making. The answer to thi question has significant implication for individuals, team, and organi zations as well. Our study reveals that in the context of OSS development, experiential learning has a stronger impact than vicarious learning. However, we caution that quite often developers are constrained not only by the time and resources they possess, but also by their limited access to social networks to gain the needed information, thus they do not always have the luxury to decide on which mode of learning to pursue. When time and resources allowing, developers may well explore the problems at hand by themselves through experiential learning; otherwise developers are probably better of to take advantage of the knowledge and experience of others through vicarious learning.

Lastly, we show that although co-membership indeed is an efective mechanism for learning and knowledge flow, its impact is biased without controlling for alternative mechanisms. The implication is twofold: First, prior studies on knowledge flow based on co-membership are valid and co-membership is efective for constructing network ties. Second, it points out the necessity to control for alternative mechanisms of knowledge flow for future studies in this research stream. Given the burgeoning number of studies on online social networks and its importance [32,35,53–55], this seems particularly relevant.

This study also provides practical guidance for firms to configure their network ties to achieve strategic goals. Firms need resources to survive and prosper. Resources not only exist within firms, but also across firms. Therefore, efective use of resources outside the boundaries of firms is crucial to gain competitive advantages. The results of this study suggest that co-membership can serve as an efective mechanism for knowledge flow, enabling firms to tap into knowledge and expertise held by others. The results also bear implications for OSS development. To successfully develop OSS, teams not only need to motivate contribution from their members, but also need to proactively encourage their members to join other projects and use co-membership to channel in useful information; through these networking activities, the odds of OSS success can be improved. At the same time, we also want to caution that the networking eforts by team members also incur cost outlay, which may eventually ofset the benefit once the number of alters exceeds a certain threshold. Therefore, how to balance the cost and benefit of networking activities is a challenge for firm managers and team leaders

There are several limitations for this study. First, we follow prior literature and use project commits to measure the success of OSS projects. However, there are other possible metrics to be considered, such as project quality, complexity, and usage. Due to data limitation, we do not explore these metrics here, and leave them to future studies. Second, we assume members watch other projects primarily for learning. However, there are other possible reasons for watching. Nevertheless, this only strengthens the impact of watching, not weakens it. Third, we collect data only from two time-points, and this may limit the generalizability of the results. Future studies may collect data from multiple time-points to validate the results of this study. Fourth, there are other possible factors that can influence project success. and future studies may consider controlling for these factors. Last, our study essentially reveals the correlation between network ties and knowledge flow. To establish the causal relationship between the two, future studies may adopt better research designs. Despite these limitations, our study contributes to the literature on how co-membership can lead to knowledge flow and influence performance and decision-making.

Gang Peng is an Associate Professor at Mihaylo College of Business and Economics, California State University Fullerton. He earned hi PhD from the University of Washington, Seattle. His research interests include adoption, difusion, usage, and impact of information technology. His research has appeared in ACM Transactions on MIS, Decision Support Systems, Decision Sciences, Industrial Marketing Management, Information Systems Research, Journal of Management Information Systems, and Journal of Strategic Information Systems, among others.

## References

[1] R.S. Burt, Structural Holes: The Social Structure of Competition, Oxford University Press, Oxford, 1992.

[2] R. Grewal, G.L. Lilien, G. Mallapragada, Location, location, location: how network embeddedness afects project success in open source systems, Manag. Sci. 52 (7) (2006) 1043–1056.

[3] N.H. Lamb, P. Roundy, The ‘ties that bind’ board interlocks research: a systemati review, Manag. Res. Rev. 39 (11) (2016) 1516–1542.

[4] A. Zaheer, G. Soda, Network evolution: the origins of structural holes, Adm. Sci. Q. 54 (1) (2009) 1–31.

[5] S. Rafaeli, G. Ravid, V. Soroka, De-lurking in virtual communities: a social com munication network approach to measuring the efects of social and cultural capital. Proceedings of the 37th Hawaii International Conference on System Science, 7 (2004), p. 70203 (Big Island, HI).

[6] L. Dabbish, C. Stuart, J. Tsay, J. Herbsleb, Social coding in GitHub: Transparency and collaboration in an open software repository. Proceedings of the ACM 2012 Conference on Computer Supported Cooperative Work, ACM, 2012, pp. 1277–1286

[7] M. Alavi, D.E. Leidner, Review: knowledge management and knowledge management systems: conceptual foundations and research issues, MIS Q. 25 (1) (2001) 107-136.

[8] G. von Krogh, N. Geilinger, Knowledge creation in the eco-system: research im peratives, Eur. Manag. J. 32 (1) (2014) 155–163.

[9] L. Argote, P. Ingram, J.M. Levine, R.L. Moreland, Knowledge transfer in organiza tions: learning from the experience of others, Organ. Behav. Hum. Decis. Process. 82 (1) (2000) 1–8.

[10] G.S. Kearns, R. Sabherwal, Strategic alignment between business and information technology: a knowledge-based view of behaviors, outcome, and consequences, J. Manag. Inf. Syst. 23 (3) (2006) 129–162.

[11] G. Szulanski, The process of knowledge transfer: a diachronic analysis of stickiness, Organ, Behav, Hum, Decis, Process, 82 (1) (2000) 9–27.

[12] G. Peng, D. Dey, A dynamic view of the impact of network structure on technology adoption: the case of OSS development, Inf. Syst. Res. 24 (4) (2013) 1087–1099.

[13] P.R. Haunschild, C.M. Beckman, When do interlocks matter?: alternate sources of information and interlock influence, Adm, Sci, O. 43 (4) (1998) 815–844.

[14] J. Xu, S. Christley, G. Madey, Application of social network analysis to the study of open source software, in: J. Bitzer, P. Schroder (Eds.), Economics of Open Source Software Development. Elsevier Science. 2006

[15] Y.L. Fang, D. Neufeld, Understanding sustained participation in open source software projects, J. Manag. Inf. Syst. 25 (4) (2009) 9–50.

[16] X.Q. Zhang, C. Wang, Network positions and contributions to online public goods: the case of Chinese Wikipedia. J. Manag, Inf, Syst, 29 (2) (2012) 11–40.

[17] J. Hahn, J.Y. Moon, C. Zhang, Emergence of new project teams from open source software developer networks: impact of prior collaboration ties. Inf. Syst. Res. 19 (3) (2008) 369–391.

[18] W. Stam, Industry event participation and network brokerage among en trepreneurial ventures, J. Manag, Stud. 47 (4) (2010) 625–653.

[19] S. Ransbotham, G.C. Kane, N.H. Lurie, Network characteristics and the value of collaborative user-generated content, Mark, Sci, 31 (3) (2012) 387–405.

[20] G. Peng, Y. Wan, P. Woodlock, Network ties and the success of open source software development, J. Strateg, Inf, Syst, 22 (4) (2013) 269–281.

[21] O. Temizkan, R.L. Kumar, Exploitation and exploration networks in open source software development: an artifact-level analysis, J. Manag. Inf. Syst. 32 (1) (2015 116–150.

[22] R. Mendez-Duron, C.E. Garcia, Returns from social capital in open source software networks, J. Evol. Econ. 19 (2) (2009) 277–295

[23] J. Wang, M.Y. Hu, M. Shanker, Human agency, social networks, and FOSS projec success, J. Bus. Res, 65 (7) (2012) 977–984.

[24] S. Daniel, K. Stewart, Open source project success: resource access, flow, and integration, J. Strateg. Inf. Syst. 25 (3) (2016) 159–176.

[25] P.V. Singh, C. Phelps, Networks, social influence, and the choice among competing innovations: insights from open source software licenses, Inf. Syst. Res. 24 (3) (2013).539–560

[26] P.V. Singh, Y. Tan, V. Mookerjee, Network efects: the influence of structural capital on open source project success, MIS Q. 35 (4) (2011) 813–829.

[27] G. Mallapragada, R. Grewal, G. Lilien, User-generated open source products: Founder's social capital and time to product release, Mark, Sci, 31 (3) (2012)

474–492.

[28] C. Fershtman, N. Gandal, Direct and indirect knowledge spillovers: the “socia network” of open-source projects, RAND J. Econ. 42 (1) (2011) 70–91.

[29] G.C. Kane, S. Ransbotham, Content and collaboration: an afiliation network approach to information quality in online peer production communities, Inf. Syst. Res. 27 (2) (2016) 424–439.

[30] E.M. Fich, L.J. White, Why do CEOs reciprocally sit on each other's boards? J. Corp. Finan. 11 (1–2) (2005) 175–195.

[31] N. Fligstein, P. Brantley, Bank control, owner control, or organizational dynamics: who controls the large modern corporation? Am. J. Sociol. 98 (2) (1992) 280–307.

[32] Y. Yu, G. Yin, H. Wang, T. Wang, Exploring the patterns of social behavior in GitHub, Proceedings of the 1st International Workshop on Crowd-based Software Development Methods and Technologies, ACM, Hong Kong, China, 2014, pp. 31–36.

[33] J. Tsay, L. Dabbish, J. Herbsleb, Influence of social and technical factors for evaluating contribution in GitHub, Proceedings of the 36th International Conference on Software Engineering, ACM, 2014, pp. 356–366.

[34] A. Begel, J. Bosch, M.-A. Storey, Social networking meets software development: perspectives from GitHub, MSDN, Stack Exchange, and TopCoder, IEEE Softw. 30 (1) (2013) 52–66.

[35] A. Lima, L. Rossi, M. Musolesi, Coding together at scale: GitHub as a collaborative social network. Proceedings of the Eighth International AAAI Conference on Weblogs and Social Media, (2014), pp. 295–304 (Ann Arbor, MI)

[36] D.A. Levinthal, J.G. March, The myopia of learning, Strateg. Manag. J. 14 (1993) 95-112.

[37] L. Argote, E. Fahrenkopf, Knowledge transfer in organizations: the roles of mem bers, tasks, tools, and networks, Organ. Behay. Hum, Decis, Process, 136 (2016) 146-159.

[38] A.C. Edmondson, The local and variegated nature of learning in organizations: a group-level perspective, Organ. Sci. 13 (2) (2002) 128–146.

[39] A.P.J. Ellis, J.R. Hollenbeck, D.R. Ilgen, C. Porter, B.J. West, H. Moon, Team learning: collectively connecting the dots, J. Appl. Psychol. 88 (5) (2003) 821–835.

[40] G.P. Huber, Organizational learning: the contributing processes and the literatures, Organ. Sci. 2 (1) (1991) 88–115.

[41] W. Scacchi, Managing software engineering projects: a social analysis, IEEE Trans. Softw. Eng, 10 (1) (1984) 49–59.

[42] T.T. Dinh-Trong, J.M. Bieman, The FreeBSD project: a replication case study of open source development, IEEE Trans. Softw. Eng, 31 (6) (2005) 481–494.

[43] bjk, A Brief History of FreeBSD, http://www.freebsd.org/doc/en\_US.ISO8859-1/ books/handbook/history.html, (2017).

[44] P. Ingram, J.A.C. Baum, Opportunity and constraint: Organizations' learning from the operating and competitive experience of industries, Strateg. Manag. J. 18 (1997) 75–98.

[45] A. Terlaak, Y. Gong, Vicarious learning and inferential accuracy in adoption pro cesses, Acad. Manag. Rev. 33 (4) (2008) 846–868.

[46] C. Casalnuovo, B. Vasilescu, P. Devanbu, V. Filkov, Developer onboarding in GitHub: the role of prior social links and language experience, Proceedings of the 2015 10th Joint Meeting on Foundations of Software Engineering, ACM, 2015, pp. 817–828.

[47] J.P. Bonardi, G.D. Keim, Corporate political strategies for widely salient issues Acad, Manag, Rev, 30 (3) (2005) 555–576.

[48] E. Kalliamvakou, G. Gousios, K. Blincoe, L. Singer, D.M. German, D. Damian, The promises and perils of mining GitHub. Proceedings of the 11th Working Conference on Mining Software Repositories. ACM. 2014. pp. 92–101.

[49] Y. Yoshikawa, T. Iwata, H. Sawada, Collaboration on Social Media: Analyzing Successful Projects on Social Coding (arXiv preprint arXiv:1408.6012 ), (2014).

[50] J. Neter, M. Kutner, C. Nachtsheim, W. Wasserman, Applied Linear Statistical Models, McGraw-Hill, Chicago, IL, 1996.

[51] T.S. Breusch, A.R. Pagan, A simple test for heteroscedasticity and random coeficient variation, Econometrica 47 (5) (1979) 1287–1294.

[52] C.Y. Baldwin, K.B. Clark, The architecture of participation: does code architecture mitigate free riding in the open source development model? Manag, Sci. 52 (7) (2006)1116-1127.

[53] B. Heller, E. Marschner, E. Rosenfeld, J. Heer, Visualizing collaboration and influence in the open-source software community, Proceedings of the 8th Working Conference on Mining Software Repositories, ACM, Waikiki, Honolulu, HI, USA 2011, pp. 223–226.

[54] N. Kerzazi, I. El Asri, Knowledge flows within open source software projects: a social network perspective, in: R. El-Azouzi, D. Menasche, E. Sabir, F. De Pellegrini, M. Benjillali (Eds.), Advances in Ubiquitous Networking 2, Springer, Singapore, 2017.

[55] F. Thung, T.F. Bissyande, D. LO, L. Jiang, Network structure of social coding in GitHub, CSMR 2013: Proceedings of the 2013 17th European Conference on Software Maintenance and Reengineering, IEEE, Genova, Italy, 2013, pp. 323–326.
