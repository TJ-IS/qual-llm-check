---
otero_id: 4192
otero_key: "RTA9ANK9"
title: "Open source software success: Measures and analysis"
authors: "Ravi Sen; Siddhartha S. Singh; Sharad Borle"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2011.09.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Open source software success: Measures and analysis

Ravi Sen <sup>a,</sup>⁎<sup>,1</sup>, Siddhartha S. Singh <sup>b,1</sup>, Sharad Borle <sup>c,1</sup>

<sup>a</sup> Department of Information and Operations Management, Texas A&M University, College Station, TX, USA

<sup>b</sup> Indian School of Business, Hyderabad, India

<sup>c</sup> Jones Graduate School of Business, Rice University, Houston, TX, USA

## a r t i c l e i n f o

Article history: Received 6 September 2010 Received in revised form 2 August 2011 Accepted 13 September 2011 Available online 21 September 2011

Keywords: OSS (open source software) FLOSS (free/libre/open source software) Longitudinal study Software project success Subscriber base

## a b s t r a c t

Despite a growing body of research on OSS production, much remains to be learned. One important issue concerns the measures of OSS project success and its determinants. In this paper, we empirically study the determinants of OSS success as measured by the number of subscribers and developers working on an OSS project. Furthermore, we demonstrate that our model forecasts these success measures more accurately as compared to a naive model.

We <sup>fi</sup>nd that OSS projects that develop software to work on Windows/UNIX/Linux operating systems, and developed using C or its derivative languages experience larger increase in subscribers and attract more developers than projects that do not have these characteristics. OSS projects with semi-restrictive licenses have fewer subscribers and attract fewer developers. Interestingly, OSS projects that accept <sup>fi</sup>nancial donations and are targeted at IS/IT professionals have more subscribers than others, although these characteristics do not affect the developer base. The number of subscribers and developers increases with the age of the OSS project. Finally, the impact of developers on subscribers and subscribers on developers is positive and signi<sup>fi</sup>cant.

© 2011 Elsevier B.V. All rights reserved.

## 1. Introduction

Unlike proprietary software, open source software (OSS) allows users to have access to the source code of the software, the freedom to use the software as they see <sup>fi</sup>t, modify the software to create derived works, and redistribute the derivative software for free or at a charge. OSS allows engagement, interaction, feedback and sharing of content (software) at the user level and <sup>fl</sup>ourishes as a result of this. The value creation process of OSS production is neither market nor hierarchy based. It constitutes a third production mode, often called peer production [1]. This OSS development approach is considered more ef-<sup>fi</sup>cient than traditional software development because it avoids the inef<sup>fi</sup>ciencies of a strong intellectual property regime [13] and it implements concurrent design and testing of software modules [10].

The widespread adoption of open source software (e.g. Apache, Sendmail, and various <sup>fl</sup>avors of Linux) has generated immense interest among academics, who want to understand and explain various aspects of this phenomenon [e.g. 15]. A key area of academic interest in OSS is the understanding of measures of OSS success and their determinants. The results from studies on OSS project success have signi<sup>fi</sup>cant managerial implications for relevant stakeholders in an OSS project (e.g. project administrators, sponsors, developers etc.) because successful OSS projects attract talented developers, large number of users, and more sponsors [8,11].

In this study, we investigate two OSS success measures namely subscriber base (as measured by the number of subscribers in a given time period) and developer base (as measured by the number of developers in a given time period). While both of these measures have been studies in the extant literature, e.g. “developer base” in Subramaniam et al. [23], and “subscriber base” in Stewart et al. [22], our study differs from these. While Subramaniam et al. [23] omit subscriber base as a measure of OSS success, Stewart et al. [22] use subscriber base to measure user-interest in an open source software. We believe that subscriber base by itself is an important success measure and is not an appropriate surrogate for user-interest. The main reason being that even non-users (e.g. developers working on competing software could become subscribers to monitor the progress of an OSS) could be subscribers while not all users would subscribe to the OSS project. Furthermore, a growth in subscriber count is an evidence of increasing interest in the OSS since subscribers actively agree to receive information about the OSS project, unlike many others who might have a passing interest. This group also offers important marketing bene<sup>fi</sup>ts that we discuss later. We investigate the relationship between OSS project success and its characteristics— both time invariant as well as time varying. In addition, unlike previous studies, we consider the success measures themselves as inter-related and include these inter-relationships in our model. Finally, we use our model for the success measures to forecast these and compare the accuracy of our forecast with that obtained using a naive model. A more accurate model to forecast the subscriber and developer bases can be very useful to the OSS project team for planning purposes.

We <sup>fi</sup>nd that OSS projects that develop software to work on Windows/ UNIX/Linux operating systems, and developed using C or its derivative languages experience larger increase in subscribers and attract more developers than projects that do not have these characteristics. OSS projects with semi-restrictive licenses have fewer subscribers and attract fewer developers. Interestingly, OSS projects that accept <sup>fi</sup>nancial donations and are targeted at IS/IT professionals have more subscribers than others, although these characteristics do not affect the developer base. The number of subscribers and developers increases with the age of the OSS project, and the impact of developers on subscribers and subscribers on developers is positive and signi<sup>fi</sup>cant. Finally, we <sup>fi</sup>nd that our model forecasts the subscriber and developer bases more accurately as compared to a naive model.

The rest of the paper is organized as follows. Section 2 discusses related research and Section 3 discusses the data. In Section 4, we present the model, its estimates, and the predictive performance using a holdout sample. This is followed by the discussion of results and implications. Section 5 concludes by highlighting the contribution of our paper and future research opportunities in this area.

## 2. Measures and determinants of OSS success: related research

The extant literature on OSS has focused on measures of developer participation and project activity to assess the success of an OSS project. For instance, project activity level, development team/community size (i.e. number of active contributors to the project), and time taken to <sup>fi</sup>x software bugs have been identi<sup>fi</sup>ed as some of the key measures for OSS project success [5]. Some similar measures include the extent to which a project attracts input from the development community (e.g. number of developers), and the extent to which it produces observable outputs such as the addition of new features to the software or <sup>fi</sup>xing of software bugs [21]. Stewart et al. [22] identify user interest over time (i.e. change in the number of Subscribers to an OSS project) and amount of development activity (i.e. the number of <sup>fi</sup>les released) as measures of OSS project success. Finally, Subramaniam et al. [23] identify project activity levels, user interest and developer interest in an OSS project as the key measures of OSS success and investigate the interaction effects between these measures.

In addition to these measures, we propose “subscriber base” as a key measure of success for OSS for reasons outlined earlier. Subscriber base is the number of individuals who chose to receive regular information (e.g. project progress, new release information, any major changes to the project team etc.) on the project. A growth in subscriber count could be an evidence of increasing interest in the OSS from committed and potential users, competitors, and other stakeholders. There are signi<sup>fi</sup>cant bene<sup>fi</sup>ts to understanding subscribers as a measure of OSS project success since the <sup>fi</sup>ndings from our study can help OSS administrators to develop long-term project management strategies. Unlike other non-subscribing users, subscribers of OSS choose to subscribe and hence have a deeper interest in the OSS project. Given these factors, they can be considered as more loyal to the OSS. Information about such a large group of loyal users can be an asset to the project management team. The relationship can be leveraged by several marketing instruments (e.g. customer communities, blogs, and other social networking initiatives) to attract more developers and users. These subscribers can provide clearer and better directions with respect to project development for long-term success. These committed users are also more likely to support the project <sup>fi</sup>nancially if needed because of their higher interest.

The extant literature has recognized the participation of developers in creating, debugging and maintaining the OSS as critical for its success. Hence, some of the OSS success factors identi<sup>fi</sup>ed in the literature are developer motivation and interest [3] and the presence of a critical mass of developers in the project [14]. Bonaccorsi and Rossi [3] suggest that the technological characteristics of the projects are also important for success and show that server-based OSS projects, such as Apache web server, are more successful than client-based OSS projects, such as Linux. Subramaniam et al. [23] show that the programming language used to develop the software and operating system for which the software is developed also affect the success of OSS. The freedom to modify and redistribute OSS is determined by its license and some studies have shown that the restrictiveness of the OSS license plays a role in the success or failure of the OSS projects [12,22,23].

While existing OSS research has helped us understand the above factors as important for OSS project success, they have limitations. Most omit “subscriber base” as a measure of OSS success and they have mostly relied on cross-sectional data for analysis. Active OSS projects are continually in development [4] and the interests of developers, non-developer users, and sponsors are likely to change throughout the life of the project. Hence, it is important to understand the changing dynamics over time of the relationships between the project's characteristics and its success. A notable exception is the study [23], which investigates the impact of project speci<sup>fi</sup>c characteristics on developer interest, user interest, and project activity levels. However, this study also does not consider the subscriber base as a possible measure of OSS success. An earlier study [22] investigates the determinants of subscriber base, and used two waves of data to investigate the determinants of project success. However, two waves can only help to capture the impact of incremental change and cannot highlight the longitudinal trends [19]. In contrast, the current study uses OSS project data from multiple time periods to capture the longitudinal trends in the relationships between OSS project's characteristic and its success as measured by the change in project's subscriber base.

Finally, OSS project administrators have an interest in forecasting the success measures for planning purposes. In this study, we use our model to forecast the number of developers and subscribers in an OSS project, and compare our forecast accuracy with that of a naive model.

## 3. Data

The longitudinal data used in this study comes from the information on open source projects listed at Sourceforge.net. Sourceforge.net is a free service that maintains the largest database of software applications, which are preferably released under an open source license. For each project, the database provides a description of the software, links to download it and to obtain more information, and a history of the project's releases.

At the time of our data collection, the Sourceforge.net database contained information on more than 200,000 software projects. For the purpose of this study we considered only those projects for which complete information was available, and which had been registered between January 1999 and December 2005. The number of such projects used in the study was 7720; a random sample of 5000 projects was used to calibrate the model and the remaining 2720 projects were held out for predictive analysis. The data on these projects is for 45 months starting April 2006.

In the following subsections we discuss the variables used in our study and provide descriptive statistics on them. There are two broad categories of variables which impact OSS project success — time-invariant and time-dependent.

## 3.1. Time-invariant variables

The time-invariant variables included in our model are the OSS license type, operating system, programming language, whether the project accepts <sup>fi</sup>nancial donations, and user type. These are all indicator variables taking a value “1” or “0”. Table 1 provides descriptive statistics on these variables and the following text describes them.

Table 1  
The time-invariant variables

<table><tr><td>Description</td><td>Variable</td><td>% of 1&#x27;s</td></tr><tr><td rowspan="2">OSS license</td><td>SCL</td><td>65.1%</td></tr><tr><td>WCL</td><td>16.1%</td></tr><tr><td rowspan="3">Operating system</td><td>WIN</td><td>68.4%</td></tr><tr><td>UNIX</td><td>91.2%</td></tr><tr><td>Other_OS</td><td>48.4%</td></tr><tr><td rowspan="2">Programming language</td><td>CGroup</td><td>49.4%</td></tr><tr><td>Other_Lang</td><td>66.1%</td></tr><tr><td>Accepts financial donations</td><td>Donation</td><td>19.6%</td></tr><tr><td rowspan="2">User type</td><td>Users</td><td>52.4%</td></tr><tr><td>Admin</td><td>58.66%</td></tr></table>

## 3.1.1. OSS license

OSS licenses are end-user license agreements used by open source software producers/developers to distribute their work. These licenses have been found to play a signi<sup>fi</sup>cant role in the success or failure of an OSS project [12,22,23]. As per OSI (Open Source Initiative), the organization responsible for approving open source licenses, all OSS licenses should have certain common characteristics. For example, they should allow free redistribution of the software and code, and modi<sup>fi</sup>cation of the said software.<sup>2</sup> While these licenses are similar in their basic characteristics, they could differ in the degree of restrictions imposed on the user to re-distribute software derived or modi<sup>fi</sup>ed from OSS software [6]. Some studies classify OSS licenses into two broad categories, restricted and non-restricted [12]. Others propose three classes of licenses. Examples are, highly restrictive, restrictive, and unrestrictive [6]; and Strong-Copyleft, Weak-Copyleft, and Non-Copyleft [17].

In this paper, we use the three categories of OSS licenses as de<sup>fi</sup>ned by [17]. These are Strong-Copyleft, Weak-Copyleft and Non-Copyleft. They are coded as two dummy variables SCL and WCL. Strong-Copyleft licenses (e.g. GNU General Public License or GPL) ensure that once software is licensed by a developer, the subsequent derivative software based on the original must also be licensed similarly. Weak-Copyleft licenses (e.g. GNU Lesser General Public License or LGPL) require that once a program is licensed by a developer, the subsequent programs based on the original must also be licensed similarly, however, the modi<sup>fi</sup>ed software can be released under a different license under certain conditions. Non-Copyleft licenses (e.g. Berkeley Software Distribution or BSD) provide that developers are not obligated to inherit the original license when they redistribute any derivative work.

## 3.1.2. Operating system

OSS can trace its roots to the Free Software Foundation' [20] and the Computer Science Research Group (CSRG) at the University of California at Berkeley. The efforts of these groups were targeted at improving the UNIX operating system in the 1970s and 80s. The programmers active in these initiatives pioneered OSS initiatives. In short, developers trained in UNIX, and later Linux (developed by Linus Torvalds in the early 1990s), formed the initial core of the OSS community. The earlier members of this OSS community built various other applications, libraries, and utilities that complemented or supplemented the various <sup>fl</sup>avors of UNIX and Linux in existence. It is only recently, that we have started to see OSS applications and utilities being developed for other operating systems such as Windows and Android. In our study we classify operating system into three independent categories viz. UNIX, Windows and Other\_OS. Note that an OSS can run on multiple operating systems. We code these three categories as three dummy variables WIN, UNIX, and Other\_OS.

## 3.1.3. Programming language

The programming language is an important factor in determining OSS project success because the participants have to be familiar with the programming language in order to understand the source code and make any changes. The C programming language has played a vital role in early OSS development for several reasons, the main being that it was the system implementation language for the UNIX operating system [16]. Therefore, it is the preferred language of OSS developers for codes that are tightly coupled to the UNIX/Linux kernel. Furthermore, several software development tools are available for generating C code resulting in reduced effort to program using C language. As a result, C and its later derivatives such as C++, Visual C++, and C# are still the preferred languages of open source software developers. This was also evident in a survey in 2005 by Computerworld that found C# and C++ in the top <sup>fi</sup>ve programming languages used by software developers.<sup>3</sup>

As in the case of operating system, a project can use multiple languages. We code these variables as two independent dummy variables CGroup and Other\_Lang.

## 3.1.4. Accepts financial donations

While developers may volunteer to contribute code to open source projects and not expect any monetary rewards in return, project administrators still incur some costs associated with project management. There are several factors that can stretch a project team's budgets. For example, a project may get into situations where relatively expensive testing equipment is required, or the project might require extensive and expensive patent research in order to avoid legal hassles at a later stage. Due to reasons such as these, many open source projects cannot progress beyond a certain point unless they receive additional <sup>fi</sup>- nancial support to handle these expenses. This additional <sup>fi</sup>nancial support comes from individuals and organizations, and popular projects are likely to attract more donations. In practice, for various reasons some OSS projects accept <sup>fi</sup>nancial donations from individuals and organizations while others do not. We include a dummy variable (Donation) to study the impact of this decision on the measure of OSS success.

## 3.1.5. User type

OSS projects are targeted at different types of audiences or users. We use the target audience as another explanatory variable. This is measured using two independent dummy variables Admin (if the OSS is targeted at IS/IT professionals such as systems administrators, quality engineers, developers) and Users (if the OSS is targeted at non-developer users).

## 3.2. Time-dependent variables

We consider three time-dependent variables viz. age of the OSS project in years (Age), the number of developers working on the project in a month (Developers) and the number of subscribers in a month (Subscribers). Fig. 1a, b and c provides histogram plots of these variables across all projects and time periods.

## 3.2.1. Project age

Literature from software engineering suggests that software quality e.g. completeness, consistency, testability, usability, reliability, etc., improves as the software development advances towards completion. Age of the software is positively related to this progress toward completion [2,7]. Furthermore, projects' age could be a signal of commitment on the part of the project administrators to support, guide, and advance the project. This commitment could attract new developers who are interested in contributing to the project. Similarly, projects that have been around for some time would also attract more subscribers in comparison to relatively nascent projects. Finally, the age of a project may be a proxy for some factors affecting success, such as the developers' group experience and the entrenchment of the software in the OSS user community [22].

![](/api/attachments/RTA9ANK9/fulltext/images/deaad0321c95ff47ab91a42e9d507f19c2b2b3439830ce511903ce4eaed19247.jpg)  
No. of Subscribers to a Project in a given time period

![](/api/attachments/RTA9ANK9/fulltext/images/161d582aed0122dd0a22241b98fc9958a23aa20c7da975c07b7f09244b083953.jpg)  
No. of Developers on a Project in a given time period

![](/api/attachments/RTA9ANK9/fulltext/images/3d7d68172506ea535d2e853044c1053428d71e65b84d870a98fc57899179f7e5.jpg)  
Fig. 1. a. No. of subscribers to a project in a given time period. b. No. of developers on a project in a given time period. c. Age of the project (in years) in a given time period.

## 3.2.2. Developers

Survival of an OSS project depends on continued contribution from developers [23,23]. Therefore, the number of developers working on a project at any time is critical to its success. Also, an increase in the number of developers involved with the project results in an increase in the knowledge base for that software. This increase happens because more developers can now communicate with each other about their experiences with the software and seek help from each other when solving any problems related to the software. In addition, as the number of developers increase, so does the amount of feedback on the software (e.g. software bugs, request for new features etc.), which provides opportunities to improve the OSS.

## 3.2.3. Subscribers

Unlike [22] which uses a change in subscriber base between two time periods, we use the number of subscribers each month as a measure of success.

## 3.3. Interrelationships among OSS project success measures

Existing studies suggest that the measures of OSS success are likely to be correlated [5]. In our case, we simultaneously model the number of developers (Developers) and the number of subscribers (Subscribers) to investigate their impact on each other. More developers in an OSS project are likely to increase project activity thus affecting the number of subscribers. Similarly, higher number of subscribers is likely to affect the number of developers by attracting new developers and contributing additional developers from the subscriber base.

## 4. Model and estimation

In this section, we <sup>fi</sup>rst present the hierarchical Bayes model and then present and discuss the estimates. Finally, we use our model to forecast the number of subscribers and developers in a holdout sample and compare the accuracy of this forecast with that of a naive model.

## 4.1. Model

Given that both the dependent variables in our study (Subscribers<sub>pt</sub> and Developer ) are count variables we use a <sup>fl</sup>exible count distribution to model these variables and then impose a correlation across the two count models.

## Model 1. Number of subscribers

The variable Subscribe $\mathbf { \boldsymbol { S } } _ { p t }$ denotes the number of subscribers for project p in time period t (the time period t is in months). We specify a count distribution (a NBD distribution<sup>4</sup>) for this variable,

Subscriber $\begin{array} { r } { \mathsf { S } _ { p t } \sim \mathrm { N B D } \Big ( \mathsf { N } _ { p t } ^ { ( 1 ) } , \mathsf { \nu } _ { 1 } \Big ) } \end{array}$

ð<sup>1</sup>Þ

where ${ \bigl ( } \lambda _ { p t } ^ { ( 1 ) } , \nu _ { 1 } { \bigr ) }$ are the parameters of the NBD distribution. The parameterization used for the NBD distribution is such that $\lambda _ { p t } ^ { ( 1 ) }$ is the mean of the distribution. The pdf of the NBD is

$$
\begin{array}{l} \operatorname * {P r} (S u b s c r i b e r s _ {p t}) = \frac {\Gamma \left(v _ {1} + S u b s c r i b e r s _ {p t}\right)}{\Gamma (v _ {1})   \Gamma \left(S u b s c r i b e r s _ {p t} + 1\right)} \left(\frac {v _ {1}}{v _ {1} + \lambda_ {p t} ^ {(1)}}\right) ^ {v _ {1}} \\ \qquad \times \left(\frac {\lambda_ {p t} ^ {(1)}}{v _ {1} + \lambda_ {p t} ^ {(1)}}\right) ^ {S u b s c r i b e r s _ {p t}}. \end{array}
$$

The parameter $\lambda _ { p t } ^ { ( 1 ) }$ is further characterized as follows,

$$
\lambda_ {p t} ^ {(1)} = \exp \left[ \lambda_ {p} ^ {(1)} + \lambda_ {1 1} ^ {(1)} A g e _ {p t} + \lambda_ {2} ^ {(1)} D e v e l o p e r s _ {p, t - 1} \right].\tag{2}
$$

where $A g e _ { p t }$ is the age of project p (in years) in time period t and Develope $r s _ { p , t - 1 }$ is the number of developers working on project $p$ during time period (t−1).

## Model 2. Number of developers

The number of developers for project p during time period t (Develope $\mathbf { \dot { \boldsymbol { s } } } _ { p t } )$ is speci<sup>fi</sup>ed as a shifted NBD process,<sup>5</sup>

$$
\text { Developers } _ {p t} - 1 \sim \text { NBD } \left(\lambda_ {p t} ^ {(2)}, v _ {2}\right)\tag{3}
$$

where $( \lambda _ { p t } ^ { ( 2 ) } , \nu _ { 2 } )$ are the parameters of the NBD distribution and $\lambda _ { p t } ^ { ( 2 ) }$ is de<sup>fi</sup>ned over the positive real line and is the mean of the NBD distribution. The pdf of the NBD is

$$
\begin{array}{l} \operatorname * {P r} (D e v e l o p e r s _ {p t} - 1) = \frac {\Gamma \left(\nu_ {2} + D e v e l o p e r s _ {p t} - 1\right)}{\Gamma (\nu_ {2}) \Gamma \left(D e v e l o p e r s _ {p t} - 1 + 1\right)} \left(\frac {\nu_ {2}}{\nu_ {2} + \lambda_ {p t} ^ {(2)}}\right) ^ {\nu_ {2}} \\ \times \left(\frac {\lambda_ {p t} ^ {(2)}}{\nu_ {2} + \lambda_ {p t} ^ {(2)}}\right) ^ {D e v e l o p e r s _ {p t} - 1}. \end{array}
$$

$\lambda _ { p t } ^ { ( 2 ) }$ is further characterized as follows,

$$
\lambda_ {p t} ^ {(2)} = \exp \left[ \lambda_ {p} ^ {(2)} + \lambda_ {1 1} ^ {(2)} A g e _ {p t} + \lambda_ {2} ^ {(2)} S u b s c r i b e r s _ {p, t - 1} \right]\tag{4}
$$

where Subscriber $\Im _ { p , t - 1 }$ is one lag of the number of subscribers, i.e. the number of subscribers to OSS project p during time (t−1).

## 4.1.1. Correlation structure

A correlation structure is speci<sup>fi</sup>ed across Model 1 and Model 2 as follows:we model the parameters $\lambda _ { p } ^ { ( 1 ) }$ and ${ \lambda } _ { p } ^ { ( 2 ) }$ (in Eqs. (2) and (4)) as,

$$
\left| \begin{array}{c} \boldsymbol {\lambda} _ {p} ^ {(1)} \\ \boldsymbol {\lambda} _ {p} ^ {(2)} \end{array} \right| = \lambda_ {p} \sim \text { MVNormal } \Big (\boldsymbol {\alpha} _ {p}, \Sigma \Big)\tag{5}
$$

$$
\begin{array}{l} \alpha_ {p} = \alpha_ {0} + \alpha_ {1} U s e r s _ {p} + \alpha_ {2} A d m i n _ {p} + \alpha_ {3} S C L _ {p} + \alpha_ {4} W C L _ {p} + \alpha_ {5} W I N _ {p} \\ \qquad + \alpha_ {6} U n i x _ {p} + \alpha_ {7} O t h e r _ {O} S _ {p} + \alpha_ {8} C G r o u p _ {p} + \alpha_ {9} O t h e r _ {L} a n g _ {p} \\ \qquad + \alpha_ {1 0} D o n a t i o n. \end{array}\tag{6}
$$

where $\begin{array} { r } { \boldsymbol { \alpha } _ { 0 } = \left[ \begin{array} { l } { \boldsymbol { \alpha } _ { 0 } ^ { ( 1 ) } } \\ { \boldsymbol { \alpha } _ { 0 } ^ { ( 2 ) } } \end{array} \right] , \boldsymbol { \alpha } _ { 1 } = \left[ \begin{array} { l } { \boldsymbol { \alpha } _ { 1 } ^ { ( 1 ) } } \\ { \boldsymbol { \alpha } _ { 1 } ^ { ( 2 ) } } \end{array} \right] , . . . . . . . . . , \boldsymbol { \alpha } _ { 1 0 } = \left[ \begin{array} { l } { \boldsymbol { \alpha } _ { 1 0 } ^ { ( 1 ) } } \\ { \boldsymbol { \alpha } _ { 1 0 } ^ { ( 2 ) } } \end{array} \right] , ~ \sum } \end{array}$ is the variance–covariance matrix and the variables are as de<sup>fi</sup>ned earlier in the Data section.

## 4.2. Estimates

The model is estimated using a MCMC estimation routine.<sup>6</sup> The estimation results in a set of posterior distributions on every parameter of interest. These distributions are summarized below using the posterior means and posterior standard deviations. Table 2 presents the estimates from the two models and the covariance structure. For comparison purposes we also present the estimates from the independent estimation of Models 1 and 2 in Appendix 1.

As mentioned earlier, Developers refers to the number of developers and Subscribers refers to the number of subscribers in a month. As shown in Table 2, both $\lambda _ { 1 1 } ^ { ( 1 ) }$ <sup>)</sup> and $\lambda _ { 1 1 } ^ { ( 2 ) }$ are positive and signi<sup>fi</sup>cant (values are 0.027 and 0.0135) implying that both Subscribers and Developers increase with the age of the project. For one-year increase in the age of the project, the number of subscribers and developers increases by 2.7% and 1.36% respectively.<sup>7</sup> This result can be explained by the fact that as the project ages, it moves toward a stable release, i.e. becomes safer and reliable to use. As a result, more users become interested in using it. Some of these users would also become subscribers in order to receive news about the project's progress and latest release of the software. Furthermore, the longer the project has been in existence, the more people become aware of it, resulting in increasing subscriber base and attracting new developers.

We <sup>fi</sup>nd that the number of developers in any period signi<sup>fi</sup>cantly impacts the number of subscribers in the next time period $( \lambda _ { 2 } ^ { ( 1 ) } =$ 0.0055 is signi<sup>fi</sup>cant and positive), and an increase in the number of developers by 10 leads to a 5.65% increase in the average number of subscribers.<sup>8</sup> One possible explanation could be that some of the developers also become subscribers to the project. Also, as more developers join the project, the project should be able to release stable versions of its software at a faster rate. This should attract more users to the project and therefore more subscribers. This result is consistent with the intuition that the measures of OSS success should correlate. An implication is that the project team can increase its subscriber base by attracting more developers. Similarly, the impact of the lag of Subscribers on Developers is positive and signi<sup>fi</sup>cant $( \lambda _ { 2 } ^ { ( 2 ) } = 0 . \bar { 0 } 0 0 1 1$ is signi<sup>fi</sup>cant and positive) indicating that a larger subscriber base in one period leads to more developers working on the project in the future. Speci<sup>fi</sup>cally, if the subscriber base increases by 1000 in a month, on average the developer base will increase by 11.6% in the next month. This relationship between subscribers and developers can be explained by the motivation of OSS developers. OSS developers are known to work on OSS project for extrinsic motivational factors such as to gain enhanced reputation among other developers, and/or signal their software development skills to potential employers [11]. By associating themselves with projects that have large subscriber base, OSS developers can achieve these objectives. In short, the project team can increase OSS success by attracting both Developers and Subscribers. Our <sup>fi</sup>nding concerning the effect of Developers and Subscribers on each other shows that the OSS project team needs to consider this relationship in evaluating the success of its initiatives to attract more developers and subscribers. If this relationship is ignored, the effectiveness of such initiatives will be overestimated.

<table><tr><td rowspan="2"></td><td colspan="2">Model 1 (Subscribers)</td><td colspan="2">Model 2 (Developers)</td></tr><tr><td>Parameter</td><td>Estimate</td><td>Parameter</td><td>Estimate</td></tr><tr><td> $Age_{pt}$ </td><td> $\lambda_{11}^{(1)}$ </td><td>0.0270(0.00066)</td><td> $\lambda_{11}^{(2)}$ </td><td>0.0135(0.00088)</td></tr><tr><td> $Developers_{p,t-1}$ </td><td> $\lambda_{2}^{(1)}$ </td><td>0.0055(2.2 × 10-4)</td><td></td><td></td></tr><tr><td rowspan="3"> $Subscribers_{p,t-1}$ </td><td></td><td></td><td> $\lambda_{2}^{(2)}$ </td><td>0.00011(9.7 × 10-6)</td></tr><tr><td> $\nu_{1}$ </td><td>54.979(0.42754)</td><td> $\nu_{2}$ </td><td>367.33(15.9982)</td></tr><tr><td> $\alpha_{0}^{(1)}$ </td><td>1.3565(0.13378)</td><td> $\alpha_{0}^{(2)}$ </td><td>-2.4572(0.24427)</td></tr><tr><td> $Users_p$ </td><td> $\alpha_{1}^{(1)}$ </td><td>-0.0674(0.04933)</td><td> $\alpha_{1}^{(2)}$ </td><td>0.0745(0.09822)</td></tr><tr><td> $Admin_p$ </td><td> $\alpha_{2}^{(1)}$ </td><td>0.1849(0.05366)</td><td> $\alpha_{2}^{(2)}$ </td><td>0.0256(0.10753)</td></tr><tr><td>SCL</td><td> $\alpha_{3}^{(1)}$ </td><td>-0.2442(0.06255)</td><td> $\alpha_{3}^{(2)}$ </td><td>-0.2153(0.12021)</td></tr><tr><td> $WCL_p$ </td><td> $\alpha_{4}^{(1)}$ </td><td>-0.1158(0.07508)</td><td> $\alpha_{4}^{(2)}$ </td><td>0.0126(0.15022)</td></tr><tr><td> $WIN_p$ </td><td> $\alpha_{5}^{(1)}$ </td><td>0.1616(0.06186)</td><td> $\alpha_{5}^{(2)}$ </td><td>0.7860(0.12077)</td></tr><tr><td> $Unix_p$ </td><td> $\alpha_{6}^{(1)}$ </td><td>0.4205(0.09118)</td><td> $\alpha_{6}^{(2)}$ </td><td>0.3377(0.16799)</td></tr><tr><td>Other_OSp</td><td> $\alpha_{7}^{(1)}$ </td><td>-0.0292(0.05847)</td><td> $\alpha_{7}^{(2)}$ </td><td>0.1020(0.11319)</td></tr><tr><td> $CGroup_p$ </td><td> $\alpha_{8}^{(1)}$ </td><td>0.4665(0.06719)</td><td> $\alpha_{8}^{(2)}$ </td><td>0.8048(0.12872)</td></tr><tr><td>Other_Langp</td><td> $\alpha_{9}^{(1)}$ </td><td>0.1363(0.07145)</td><td> $\alpha_{9}^{(2)}$ </td><td>0.4830(0.12966)</td></tr><tr><td> $Donation_p$ </td><td> $\alpha_{10}^{(1)}$ </td><td>0.4353(0.05854)</td><td> $\alpha_{10}^{(2)}$ </td><td>-0.0795(0.11127)</td></tr></table>

Table 2 Model estimates<sup>⁎</sup>.  
Shaded cells imply parameter ‘insigni<sup>fi</sup>cance’ at a 95% level.  
<sup>⁎</sup>Posterior standard deviations shown in parentheses.

The coef<sup>fi</sup>cients of Users in Models 1 and $2 \left( \alpha _ { 1 } ^ { ( 1 ) } \right.$ and $\alpha \mathfrak { f } ^ { ( 2 ) }$ respectively) are not signi<sup>fi</sup>cant implying that OSS targeted at non-developer users does not have any impact on either the subscriber base or the developer base of the project. On the other hand, the coef<sup>fi</sup>cient of Admin (dummy variable equals to 1 if the OSS is targeted at IS/IT professionals) is signi<sup>fi</sup>cant and positive in Model 1 $( \bar { \alpha _ { 2 } ^ { ( 1 ) } } = 0 . 1 8 4 9 )$ and insigni<sup>fi</sup>cant in Model 2 implying that such a targeting increases the subscriber base but has no impact on the number of developers working on the project, which is counterintuitive. The estimates imply that for OSS targeted at Admin, the subscriber base on an average contains $2 0 . 3 \% [ = ( \exp ( 0 . 1 8 4 9 ) - 1 ) * 1 0 0 ]$ more subscribers than the OSS targeted at Users. Our results could be due to the possibility that signi<sup>fi</sup>cant part of the subscriber base consists of more technically savvy users such as IS/IT professionals who are interested in the software but might be reluctant to become part of the developer group. Furthermore, in comparison to non-IT users, administrative users (e.g. IT professionals, system admins etc.) are more likely to be interested in following the progress of the OSS so that they are aware of any changes in the OSS and latest releases in timely manner.

The license type of the OSS is represented by three categories, namely, Strong-Copyleft (SCL), Weak-Copyleft (WCL) and Non-Copyleft (NCL). We use NCL as the basis and code the license type using two dummy variables. The coef<sup>fi</sup>cients of SCL $( \alpha _ { 3 } ^ { ( 1 ) } = - 0 . 2 \dot { 4 } 4 2$ and $\alpha _ { 3 } ^ { ( 2 ) } = - 0 . 2 1 5 3$ in Models 1 and 2 respectively) represent the relative effect of a Strong-Copyleft license on the outcome variables— relative to both NCL and WCL (since the coef<sup>fi</sup>cients of WCL are insigni<sup>fi</sup>cant in both models). These coef<sup>fi</sup>cients show that OSS software with SCL has subscriber and developer bases smaller by 21.7% and 19.4% each month as compared to other license types. This is an interesting result in light of that fact that the proponents of open source software advise OSS developers to make their licenses Strong-Copyleft (e.g. GPL). However, the result is in agreement with some existing research that has found that Strong-Copyleft license has an adverse impact on user-interest in an OSS [22]. Since Strong-Copyleft licenses impose certain restrictions on how the software can be redistributed, this adverse impact could be attributed to resistance from OSS users who prefer to retain the rights for redistribution of the software code in a way that best serves their objectives. For example, software that includes any amount of GPL licensed (a Strong-Copyleft license) code has to be released under GPL license. Since not all users might be interested in redistributing any derivative software under the parent license, they might prefer a less restrictive end-user license, e.g. BSD (which is a Non-Copyleft license). With reduced user interest, the OSS will suffer from fewer subscribers, and as a result attract fewer developers.

OSS using only the UNIX operating system has the largest subscriber base, an average of 52.3% subscribers more per month $( \alpha _ { 6 } ^ { ( 1 ) } =$ 0.4205 is positive and signi<sup>fi</sup>cant) than OSS using Other\_OS. Similarly, OSS using the Windows operating system (WIN) has an average of 17.5% subscribers more $( \alpha _ { 5 } ^ { ( 1 ) } = 0 . 1 \bar { 6 1 6 }$ is positive and signi<sup>fi</sup>cant) than the OSS working only on Other\_OS. One explanation for the result could be the fact that various Linux/UNIX distributions and Windows versions taken together account for the major share of operating system in use. Since the subscribers to OSS projects are interested in the OSS, they are more likely to subscribe to projects that are developing software for Linux/UNIX/Windows operating systems resulting in relatively larger subscriber bases for such projects. In Model 2, while the coef<sup>fi</sup>- cients of Win and UNIX $( \alpha _ { 5 } ^ { ( 2 ) } = \dot { 0 } . 7 \dot { 8 } 6$ and $\alpha _ { 6 } ^ { ( 2 ) } = 0 . 3 3 7 7$ respectively) are signi<sup>fi</sup>cant and positive, the coef<sup>fi</sup>cient of Other\_OS $( \alpha _ { 7 } ^ { ( 2 ) } )$ is not signi<sup>fi</sup>cant. This interesting result shows that OSS using only the Windows operating system has a larger developer base (119.5% developers more per month than in OSS using Other\_OS) than OSS using only the UNIX operating system that has a larger developer base (40.2% developers more per month than in OSS using Other\_OS) than OSS using any other operating system. Therefore, OSS operating on Windows attracts more developers while those operating on UNIX attract more subscribers. One explanation for the different results could be the difference in motivations of developers and subscribers. The subscribers to a project are interested in just that particular project and therefore could be in<sup>fl</sup>uenced by the operating system that the OSS would run on. The developers, on the other hand, could be in<sup>fl</sup>uenced by other factors such as the potential user-base of the OSS. Since most nondeveloper users use Windows, developers might see better exposure of their skills if they work on Windows compatible OSS projects. Thus, OSS using the UNIX and Windows operating systems is more successful, however, each is successful in a different way.

We <sup>fi</sup>nd that OSS using programming languages categorized as CGroup has larger subscriber and developer bases as compared to those using other languages $( \alpha _ { 8 } ^ { ( 1 ) } = 0 . 4 6 6 5$ and $\alpha _ { 8 } ^ { ( 2 ) } = 0$ .8048 are positive and signi<sup>fi</sup>cant, and respectively greater than $\alpha _ { 9 } ^ { ( 1 ) } = 0 . 1 3 6 3$ and $\alpha _ { 9 } ^ { ( 2 ) } = 0 . 4 8 3$ that are also positive and signi<sup>fi</sup>cant). These estimates translate to an average of 44.8% more subscribers and 61.5% more developers in a month for OSS using CGroup as compared to those using other languages (Other\_Lang). This result can be explained by the fact that C language is one of the preferred languages of OSS developers for codes that require portability, need faster processing, have real-time requirements, or are tightly coupled to the UNIX/Linux kernel. Furthermore, existing programs like parser generators or GUI builders that generate C code also add to its advantages, since these programs can reduce the effort required to code using C. Finally, high-quality C compilers are available as open-source software over the Internet (e.g. the Free Software Foundation's GNU C compiler). Therefore, an open source software project written in C or its later versions will attract more developers, resulting in a larger subscriber base.

Table 3  
Predictive analysis.

<table><tr><td colspan="3">a) Subscribers</td><td colspan="3">b) Developers</td></tr><tr><td>Description</td><td>Prediction</td><td>MAD</td><td>Description</td><td>Prediction</td><td>MAD</td></tr><tr><td>Average of the number of Subscribers across all 2720 projects, all time periods</td><td>67.9</td><td></td><td>Average of the number of Developers across all 2720 projects, all time periods</td><td>4.7</td><td></td></tr><tr><td>Average of the predicted Subscribers using the developed model</td><td>10.1</td><td>64.4</td><td>Average of the predicted Developers using the developed model</td><td>1.5</td><td>3.5</td></tr><tr><td>Average of the predicted Subscribers using the ‘naive’ approach</td><td>71.94</td><td>97.8</td><td>Average of the predicted Developers using the ‘naive’ approach</td><td>4.5</td><td>4.0</td></tr></table>

OSS projects that accept <sup>fi</sup>nancial donations have a larger subscriber base per month (54.5% larger) as compared to those that do not $( \alpha _ { 1 0 } ^ { ( 1 ) } = 0 . 4 3 5 3 )$ . However, this variable has no impact on the developer base. This could be explained by the fact that OSS projects accepting <sup>fi</sup>nancial donations will include among their subscribers some of the donors to the project who could be interested in following the progress made by the project. On the other hand, OSS developers mostly work as volunteers and do not expect any <sup>fi</sup>nancial rewards for their efforts [11]. Therefore, they might not be interested in whether an OSS project accepts <sup>fi</sup>nancial donation or not. Finally, as expected, we <sup>fi</sup>nd signi<sup>fi</sup>cant positive residual correlation between our two measures of OSS success (covariance=2.0334). Therefore, the net effect of unmeasured factors in our two models is such that they act to either increase or decrease both the subscriber and developer bases in any period.

## 4.3. Predictive analysis

The model developed can be used for predicting the number of subscribers and the number of developers working on a project in any given time period. Such a prediction is particularly helpful for new projects and is valuable information for planning purposes. In this sub-section we use the model estimates to predict the number of subscribers and developers in a holdout sample of 2720 projects. We use Eqs. (1) through (6) along with the estimates in Table 2 to make predictions for the number of subscribers in each project in each time period, as well as the number of developers working on each project in each time period. These predictions are then compared with the actual data and the Mean Absolute Deviations (MAD) calculated. Table 3 presents the results of this analysis for the number of subscribers and number of developers respectively. We also present prediction results from a naive approach wherein the average number of subscribers and developers observed in the estimation sample is used as predictions in the holdout sample.

As seen from Table 3, the Mean Absolute Deviations (MAD statistics) from the model predictions are much better than the MAD statistics from the naive approach.

To further illustrate the predictive ability of the model we present the predictions in a slightly more detailed manner in Fig. 2a and b. We plot the MAD statistics for the predictions across each time period (recollect that there are a total of 45 time periods). Therefore, the MAD statistics corresponding to a particular time period will be the mean of the absolute differences between the predictions and actual values for all projects during that time period.

Again, looking at Fig. 2a and b it is clear that the model consistently outperforms the ‘rule-of-thumb’ approach in predicting the number of subscribers and developers (the MAD from the model predictions are consistently better). An interesting point observed in Fig. 2b is the ‘kink’ observed across time periods 27, 28 and 29. Upon further investigation we <sup>fi</sup>nd that these time periods correspond to the months of June, July and August 2008. One reason for this unusual data feature could be some problem in the data collection procedure itself during these 2 months. We have no way of checking this issue. Another possibility is that the sudden decrease in the number of developers during these months is due to some wider economic factors. Indeed, we <sup>fi</sup>nd that the US economy and the real estate market went into severe downturn during this period. Given that developers volunteer to work on OSS projects, such a situation might make many of them focus their energies elsewhere to improve their economic condition. Either case opens up the possibility of not considering the data in estimating the model and making predictions. Using this recourse might improve the model <sup>fi</sup>t and predictions.

a) Prediction of Subscribers across time periods  
![](/api/attachments/RTA9ANK9/fulltext/images/9a779050ada17eaa27588f4361a3bdb0b6477b897785720559a3dfbdb3d6c9bd.jpg)

b) Prediction of Developers across time periods  
![](/api/attachments/RTA9ANK9/fulltext/images/fa8b6bfdcf6bb28731884b15aeb19fd429dc0c4fe8fe5a9eae7259f1ff7fc9f1.jpg)  
Fig. 2. a. Prediction of subscribers across time periods. b. Prediction of developers across time periods.

## 5. Conclusion

In this paper, we empirically investigate the effects of OSS projectspeci<sup>fi</sup>c characteristics on the success of OSS projects as measured by the number of subscribers and developers working on the project. We <sup>fi</sup>nd that both the number of subscribers and the number of developers increase with the age of the OSS project, and OSS projects that develop software to work on Windows/UNIX/Linux operating system, and use C/C#/C++ experience larger increase in subscribers and attract more developers than projects that do not have these characteristics. Furthermore, we <sup>fi</sup>nd that OSS projects with semi-restrictive licenses experience a decrease in the number of subscribers and attract fewer developers. Interestingly, OSS projects that accept <sup>fi</sup>nancial donations and are targeted at IS/IT professionals have more subscribers than projects that do not. We also <sup>fi</sup>nd the impact of developers on subscribers and that of subscribers on developers to be signi<sup>fi</sup>cant and positive.

One limitation of this study is that we did not investigate the impact of software functionality on the subscribers and developers associated with an OSS project. The reasons for doing so were as follows. First, we found that our data-source has 10 major software categories based on software functionality, and that one software could belong to two or more categories. To capture the software classi<sup>fi</sup>cation we will have to add more independent variables, which would be inconsistent with the objective of keeping the model parsimonious while investigating our key variables of interest. Furthermore, if we had increased the number of independent variables in the model (while keeping the sample size same), we ran the risk of compromising our ability to test the model (e.g. reduced statistical power). However, these reasons do not imply that software category does not have an impact on subscriber base of an OSS project or the number of developers associated with the project. In fact, one could argue that software with strong network effects could have a different impact on the subscriber base and developer-interest than software with weak network effect. Similarly, infrastructure software could attract different numbers of developers/subscribers in comparison to desktop application software.<sup>9</sup> Therefore, we believe that the impact of this variable on OSS project success needs to be investigated empirically in future studies on OSS project success. Given the literature on software classi<sup>fi</sup>cation, the large number of software categories among OSS projects can be reduced to a few broad categories (e.g. desktop application vs. systems software, network applications vs. non-network applications, or infrastructure software vs. non-infrastructure software). This should take care of any concerns regarding the complexity of models used in these future studies and the power of these models.

Finally, we would like to address any concerns about the accuracy of the data from Sourceforge since it is self-reported by project owners/ administrators [9]. Lerner and Tirole [12] provide a plausible reason for not suspecting the accuracy of this data. They explain “… the project leaders are trying to recruit new developers, attract new users, and solicit donations for their project. Undertaking a “bait-and-switch” strategy to do so, $e . g .$ making the project appear something other than what it really is, is unlikely to be a positive signal for prospective developers, users and/ or sponsors.” Hence, we believe that the use of project data from Sourceforge.net is valid for our study. Use of this data for several published and ongoing studies using this same data source also exempli<sup>fi</sup>es the validity of this data source for studies on open source software.

## Acknowledgment

We would like to thank Dr. Greg Madey for permitting us to use the Sourceforge data available at the University of Notre Dame.

## Appendix 1

The results of independent estimation of Models 1 and 2.

<table><tr><td rowspan="2"></td><td colspan="2">Model 1 (Subscribers)</td><td colspan="2">Model 2 (Developers)</td><td rowspan="2" colspan="2"> $\sum$ </td></tr><tr><td colspan="2">Parameter Estimate</td><td colspan="2">Parameter Estimate</td></tr><tr><td> $Age_{pt}$ </td><td> $\lambda_{11}^{(1)}$ </td><td>0.0269(0.00052)</td><td> $\lambda_{11}^{(2)}$ </td><td>0.0135(0.00137)</td><td>2.7153(0.05686)</td><td>0.0(0.0)</td></tr><tr><td> $Develo-pers_{p,t-1}$ </td><td> $\lambda_{2}^{(1)}$ </td><td>0.0057(1.9× $10^{-4}$ )</td><td></td><td></td><td>0.0(0.0)</td><td>9.6784(0.27120)</td></tr><tr><td> $Subscri-bers_{p,t-1}$ </td><td></td><td></td><td> $\lambda_{2}^{(2)}$ </td><td>0.00012(1.6× $10^{-6}$ )</td><td></td><td></td></tr><tr><td></td><td> $\nu_{1}$ </td><td>54.980(0.43413)</td><td> $\nu_{2}$ </td><td>369.20(15.7615)</td><td></td><td></td></tr><tr><td></td><td> $\alpha_{0}^{(1)}$ </td><td>1.3696(0.14428)</td><td> $\alpha_{0}^{(2)}$ </td><td>-2.5253(0.28399)</td><td></td><td></td></tr><tr><td> $Users_{p}$ </td><td> $\alpha_{1}^{(1)}$ </td><td>-0.0697(0.05239)</td><td> $\alpha_{1}^{(2)}$ </td><td>0.0730(0.09998)</td><td></td><td></td></tr><tr><td> $Admin_{p}$ </td><td> $\alpha_{2}^{(1)}$ </td><td>0.1801(0.05735)</td><td> $\alpha_{2}^{(2)}$ </td><td>0.0047(0.10880)</td><td></td><td></td></tr><tr><td> $SCL_{p}$ </td><td> $\alpha_{3}^{(1)}$ </td><td>-0.2394(0.06339)</td><td> $\alpha_{3}^{(2)}$ </td><td>-0.2244(0.12423)</td><td></td><td></td></tr><tr><td> $WCL_{p}$ </td><td> $\alpha_{4}^{(1)}$ </td><td>-0.1135(0.08231)</td><td> $\alpha_{4}^{(2)}$ </td><td>0.0147(0.15833)</td><td></td><td></td></tr><tr><td> $WIN_{p}$ </td><td> $\alpha_{5}^{(1)}$ </td><td>0.1600(0.06186)</td><td> $\alpha_{5}^{(2)}$ </td><td>0.8003(0.12652)</td><td></td><td></td></tr><tr><td> $UNIX_{p}$ </td><td> $\alpha_{6}^{(1)}$ </td><td>0.4159(0.09256)</td><td> $\alpha_{6}^{(2)}$ </td><td>0.3336(0.18180)</td><td></td><td></td></tr><tr><td> $Other\_OS_{p}$ </td><td> $\alpha_{7}^{(1)}$ </td><td>-0.0274(0.05957)</td><td> $\alpha_{7}^{(2)}$ </td><td>0.1126(0.12532)</td><td></td><td></td></tr><tr><td> $CGroup_{p}$ </td><td> $\alpha_{8}^{(1)}$ </td><td>0.4599(0.07129)</td><td> $\alpha_{8}^{(2)}$ </td><td>0.8441(0.13497)</td><td></td><td></td></tr><tr><td> $Other\_Lang_{p}$ </td><td> $\alpha_{9}^{(1)}$ </td><td>0.1301(0.07521)</td><td> $\alpha_{9}^{(2)}$ </td><td>0.5076(0.14016)</td><td></td><td></td></tr><tr><td> $Donation_{p}$ </td><td> $\alpha_{10}^{(1)}$ </td><td>0.4337(0.05989)</td><td> $\alpha_{10}^{(2)}$ </td><td>-0.0719(0.11560)</td><td></td><td></td></tr></table>

## References

[1] Y. Benkler, The Wealth of Networks: How Social Production Transforms Markets and Freedom, Yale University Press, New Haven, Conn, 2006, p. 515.

[2] B.W. Boehm, J.R. Brown, M. Lipow, Quantitative evaluation of software quality, in the Proceedings of the 2nd International Conference on Software Engineering, October 13-15 (1976) 592–605.

[3] A. Bonaccorsi, C. Rossi, Why open source software can succeed? Research Policy 32 (7) (2003) 1243.

[4] K. Crowston, B. Scozzzi, Open source software projects as virtual organizations: competency rallying for software development, IEEE Proceedings Software 149 (1) (2002) 3–17.

[5] K. Crowston, J. Howison, H. Annabi, Information systems success in free and open source software development: theory and measures, Software Process: Improvement and Practice 11 (2) (2006) 123–148.

[6] C. Fershtman, N. Gandal, Open source software: motivation and restrictive licensing, International Economics and Economic Policy 4 (2) (2007) 209–225

[7] I. Gorton, A. Liu, Software component quality assessment in practice: successes and practical impediments, The Proceedings of the 24th International Conference on Software Engineering, 2002, pp. 555–558.

[8] I. Hann, J. Robert, A. Slaughter, Why developers participate in open source software projects: an empirical investigation, The Proceedings of 25th International Conference on Information Systems, 2004, pp. 821–830.

[9] J. Howison, K. Crowston, The perils and pitfalls of mining Sourceforge, The Proceedings of Mining Software Repositories Workshop, International Conference on Software Engineering, Edinburgh, Scotland, May 25 2004.

[10] B. Kogut, A. Metiu, Open source software development and distributed innovation, Oxford Review of Economic Policy 17 (2) (2001) 248–264.

[11] J. Lerner, J. Tirole, Some simple economics of open source, Journal of Industrial Economics 52 (2002).

[12] J. Lerner, J. Tirole, The scope of open source licensing, Journal of Law, Economics, and Organization 21 (1) (2005) 20–56.

[13] B. Martin, , Available at, Information Liberation, Freedom Press, London (UK), 1998, pp. 29–56 http://www.bmartin.cc/pubs/98il/ilall.pdf.

[14] A. Mockus, R.T. Fielding, J.D. Herbsleb, Two case studies of open source software development: Apache and Mozilla, ACM Transactions on Software Engineering and Methodology 11 (3) (2002) 309–346.

[15] M. Neslon, R. Sen, C. Subramaniam, Understanding open source software development — a research classi<sup>fi</sup>cation framework, Communications of AIS 17 (12) (2006) 266–287.

[16] D.M. Ritchie, The development of the C programming language, in: T.J. Bergin, R.G. Gibson (Eds.), History of Programming Languages, ACM Press, 1996.

[17] R. Sen, C. Subramaniam, M. Nelson, Determinants of open source software license choice, Journal of Management Information Systems 25 (3) (Winter 2008–2009) 207–240.

[18] G. Shmueli, T.P. Minka, J.B. Kadane, S. Borle, S.P. Boatwright, A useful distribution for <sup>fi</sup>tting discrete data: revival of the Conway–Maxwell–Poisson distribution, Applied Statistics 54 (2005) 127–142.

[19] J.D. Singer, J.B. Willett, Modeling change and event occurrence, Applied Longitudi nal Data Analysis, Oxford University Press, New York, 2003, p. 10.

[20] R.M. Stallman, The GNU operating system and the free software movement, Available at, Open Sources: Voices from the Open Source Revolution, O'Reilly Media, Sebastopol, CA, 1999 http://www.oreilly.com/catalog/opensources/book/stallman.html.

[21] K.J. Stewart, S. Gosain, The impact of ideology on effectiveness in open source software development teams, MIS Quarterly 30 (2) (2006) 291–314.

[22] K.J. Stewart, A.P. Ammeter, L.M. Maruping, Impact of license choice and organizational sponsorship on success in open source software development projects, Information System Research 17 (2) (2006) 126–144.

[23] C. Subramaniam, R. Sen, M. Nelson, Open source software: determinants of OSS project success, Decision Support Systems 46 (2) (2009) 576–585.

## Further Reading

[1] G. Madey, ed., The SourceForge Research Data Archive (SRDA). University of Notre Dame. (Accessed January 2009) http://srda.cse.nd.edu/.

Dr. Ravi Sen is an Associate Professor in the Department of Information and Operations Management at the Mays Business School, Texas A&M University. He received his Ph.D. in Business Administration from the University of Illinois at Urbana–Champaign in 2003. His research interests include economics of electronic commerce, open source software, and software security. He has published in the Journal of Management Information Systems, Decision Support Systems, International Journal of Electronic Commerce, Communications of the AIS, Electronic Markets, Journal of Electronic Commerce Research, and others.

Dr. Sinddharth S. Singh is an Associate Professor of Marketing at the Indian School of Business. He received his Ph.D. in Marketing from the J.L. Kellogg School of Management, Northwestern University in 2003. His research interests include quantitative models of consumer behavior. He has published in leading management and marketing journals such as Marketing Science, Management Science, Journal of Service Research, Quan titative Marketing and Economics, and others.

Dr. Shard S. Borle is an Associate Professor of Marketing at the Jesse H. Jones Graduate School of Business, Rice University. He received his Ph.D. in Marketing from Carnegie Mellon University in 2003. His research interests include quantitative models of consumer behavior and Bayesian econometrics. He has published in leading management and marketing journals such as Marketing Science, Management Science, Statistical Science, Bayesian Analysis, Journal of the American Statistical Association, Quantitative Marketing and Economics and others.
