---
otero_id: 2632
otero_key: "JRT2QP6E"
title: "Virtual organizational learning in open source software development projects"
authors: "Yoris A. Au; Darrell Carpenter; Xiaogang Chen; Jan G. Clark"
year: "2009"
journal: "Information & Management"
doi: "10.1016/j.im.2008.09.004"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Virtual organizational learning in open source software development projects

Yoris A. Au \*, Darrell Carpenter, Xiaogang Chen, Jan G. Clark

Department of Information Systems and Technology Management, College of Business, University of Texas at San Antonio, One UTSA Circle, San Antonio, TX 78249, USA

## A R T I C L E I N F O

Article history: Received 3 May 2007 Received in revised form 23 May 2008 Accepted 26 September 2008 Available online 28 November 2008

Keywords: Virtual organizational learning Organizational learning curve Virtual organization Open source software Software development Project performance

## A B S T R A C T

We studied virtual organizational learning in open source software (OSS) development projects. Specifically, our research focused on learning effects of OSS projects and the factors that affect the learning process. The number and percentage of resolved bugs and bug resolution time of 118 SourceForge.net OSS projects were used to measure the learning effects. Projects were characterized by project type, number and experience of developers, number of bugs, and bug resolution time. Our results provided evidence of virtual organizational learning in OSS development projects and support for several factors as determinants of performance. Team size was a significant predictor, with mid-sized project teams functioning best. Teams of three to seven developers exhibited the highest efficiency over time and teams of eight to 15 produced the lowest mean time for bug resolution. Increasing the percentage of bugs assigned to specific developers or boosting developer participation in other OSS projects also improved performance. Furthermore, project type introduced variability in project team performance.

\- 2008 Elsevier B.V. All rights reserved.

## 1. Introduction

Many people can work together on a task regardless of time, geographic location, or organizational affiliation by adopting a virtual approach [14]. Open source software (OSS) development projects exhibit many of the characteristics that make virtual organizations successful, including self-governance, a powerful set of mutually reinforcing motivations, effective work structures and processes, and technology for communication and coordination. Examples of thriving OSS projects include Linux, Apache, and Mozilla. Although seemingly disorganized, and lacking monetary incentives, the development approach is characterized by design simplicity, team work, a visible product, and communication.

But what makes OSS development projects successful? Mockus et al. [13] conducted a case study on the Apache Web server and Mozilla Web browser projects to learn their development process characteristics; they found that projects based on a relatively small core of developers (10–15 people) could be geographically dispersed, yet communicate and function without conflict via a set of implicit coordination mechanisms (i.e. informal email exchange). However, when the number of core developers exceeded this size, other explicit coordination mechanisms (e.g., a code ownership policy) had to be adopted. In a similar study, Huntley [9] used organizational learning to explain the success of OSS projects; he maintained that it decreased time in fixing bugs. However, there were significant debugging differences in Apache and Mozilla, with project maturity as the apparent reason, as opposed to other factors such as project size and number of programmers. Debugging data were modeled to fit a learning curve. Mozilla, an emerging project, was characterized as having improvements due to learning effects present in their team. Both these authors pointed out significant differences between the projects.

Our intent was to extend and refine their work by including a much larger number of OSS development projects of varying size (in terms of the number of developers involved) and type (from simple file management software to complex enterprise software suite). Specifically, we included 118 OSS projects in our sample. By focusing on multiple projects of varying size and type, we were better able to characterize OSS projects. Our study was initiated to answer the following research questions:

(1) Are learning effects universally present in OSS projects? (2) What are the factors that affect the learning process?

We used the number and percentage of resolved bugs and bug resolution time to measure learning effects. However, we also looked at how different project types, number of developers (project team size) and their experience, and the intensity of assigned bugs affected the learning rates. Data for this study were obtained from the SourceForge.net<sup>1</sup> database.

## 2. Theoretical framework and hypotheses

We developed several hypotheses based on theories that relate to virtual organizational learning. Our first hypothesis seeks to show that organizational learning exists in OSS development projects. The subsequent hypotheses seek to explain the variation of learning rates observed across projects.

## 2.1. Organizational learning curves

Group learning curves were first observed in the 1940s during construction of ships and aircraft [22]. The time required to build a complex product decreased at a diminishing rate as more products were produced.

Fiol and Lyles [6] postulated that there are two levels of organizational learning: higher- and lower-level. The first focuses on re-defining the overall organizational strategy under ill-defined context; examples include developing a new organizational culture and re-establishing organizational priorities [3]. Conversely, that lower-level learning focused on specific organizational behaviors and constraints within existing organizational rules, suggesting that minor managerial adjustments, improved problem-solving skills and that the development of formal rules were examples of it. This type of learning is primarily a process of repetition [5].

We consider debugging as a way that organizational experience is accumulated in OSS development teams, thus establishing the software development learning curve. This is lower-level learning where developers repeatedly scan, review, and/or modify program code. As the team gains experience, it exhibits its learning curve by decreasing its average time to resolve a bug. Therefore, we hypothesized that:

H1. As the number of bugs resolved to date increases, the average bug resolution time decreases.

## 2.2. Cognitive capital and developer’s OSS experience

Cognitive capital consists of expertise and the knowledge about how to apply expertise in solving a problem. Over time, people develop it as they learn the skills, knowledge, specialized dialogue, and norms of their work and interact with others who share the same practice [18].

OSS developers can be concurrently involved in more than one project, allowing them a greater opportunity to work with others, learn about the norms of OSS development, and accumulate more experience. Overall, developer’s OSS expertise increases with the number of projects in which they are involved. This translates into larger cognitive capital that can be shared with other team members to improve team performance.

Social capital is defined as the number of the ties or interactions that an actor (e.g., a developer) has with another in a social event within a social network or community. For example, Okoli and Oh [15] found a significant relationship between developer performance on Wikipedia and their social ties within the Wikipedia community. Grewal et al. [7] measured social capital as ‘‘network embeddedness’’ using parameters derived from the number of projects in which an OSS developer had been involved. We therefore used number of OSS projects as a measure for OSS developer experience.

This lead to the hypothesis:

H2. Teams with more experienced OSS developers resolve bugs faster.

## 2.3. Task ownership

Task ownership occurs when a task performer takes personal interest and responsibility for it. Its degree can affect how the task is accomplished. It improves team effectiveness and facilitates individual learning; for example, students exhibit a sense of individual accountability when their grade is based on individual efforts in a group project. This also helps to eliminate nonparticipants.

The relationship between task ownership and individual/team performance can be explained by Goal-Setting Theory, which maintains that task ownership helps task performers clarify their task goals [12]. In turn, these help performers focus attention on goal-related activities, thus improving performance. Rasch and Tosi [16] validated Goal-Setting Theory in software development teams.

We hypothesized that:

H3. There is an inverse relationship between increasing the percentage of bugs assigned to specific developers and average bug resolution time.

## 2.4. Project category

At the time of our research, Sourceforge.net classified its projects into thirteen categories. These included Clustering, Database, Desktop, Development, Enterprise, Financial, Games, Hardware, Multimedia, Networking, Security, SysAdmin, and VoIP. Projects in different categories typically have different complexity and timeliness, affecting their bug resolution times. We hypothesized:

H4. Different project categories have different average bug resolution times.

## 2.5. Project team size

Prior work on traditional co-located teams has suggested that the appropriate team depends on the nature of the task; for example, Hwang and Guynes [10] reported that large computersupported groups generated more decision alternatives but took longer to reach a decision. If a team is too small, it does not effectively share the workload but if it is too large, coordination the overhead is large and social loafing becomes a concern.

The relationship between team size and team performance in OSS communities might exhibit a different pattern than that in a traditional setting, because the communication structure is different; the OSS project team generally consists of two subgroups of developers: core developers and code contributors. Core developers make the critical decisions (e.g., when to release the next version and whether or not to implement a new feature). However, to reach consensus on these decisions, intensive communication among core developers is critical and a small number of core developers per project is therefore recommended.

Code contributors produce the code. They receive well-defined subtasks (i.e. bugs), work on them independently, and, when finished, report back to core developers. As a result, the communication structure follows a star topology. The core developers are the central ‘‘hub,’’ and all the contributors connect to and through this hub.

We felt that different team sizes have different challenges: a large team may have coordination problems, whereas a small team may encounter resource problems. This lead to the hypothesis:

H5. Average bug resolution time varies among project team size.

## 3. Research methodology

## 3.1. Empirical model

Based on the production function and motivated by Argote et al. [2] and Huntley, we developed a log–log regression model with both qualitative and quantitative variables:

$$
\begin{array}{r l} \ln (\text { MeanBugResolutionTime } _ {i t}) & = \alpha_ {0} + \alpha_ {1} \ln (\text { CumBugsResolved } _ {i t}) \\ & + \alpha_ {2} \ln (\text { DeveloperExperience } _ {i}) \\ & + \alpha_ {3} \ln (\text { CumPctBugsAssigned } _ {i t}) \\ & + \sum_ {i = 1} ^ {1 2} \beta_ {i} \text { ProjectCategory } _ {i} \\ & + \sum_ {j = 1} ^ {3} \gamma_ {j} \text { DeveloperCategory } _ {i j} + \varepsilon_ {i t} \end{array}
$$

where MeanBugResolutionTime = mean time to resolve the bugs of Project i reported in Week t, measured in days, CumBugsResolve-$d _ { i t } = \mathrm { c u m u l a t i v e }$ resolved bugs of Project i, including Week t, DeveloperExperien $C e _ { i t } = \tt a v e r a g e$ number of other projects each developer in Project i has worked on up to Week t, CumPctBugsAssigned = cumulative percentage of assigned bugs in Week t of Project i, ProjectCategory = category of Project i, DeveloperCategor-$y _ { i t } = s \mathrm { i } z e$ of Project i in Week t, measured in terms of the number of developers in the project (1–2 developers; 3–7 developers; 8–15 developers; >15 developers), As the model indicates, our analysis was based on cross-sectional time series data or panel data, consisting of two-dimensional sets in which a group of people or objects are observed longitudinally. Thus Project i is the panel variable and Week t is the time variable. Each observation is a collection of information on a specific project in a given week. The descriptive statistics for the model variables are shown in Table 1.

Descriptive statistics for the model variables

<table><tr><td>Variable</td><td>Min</td><td>Max</td><td>Mean</td><td>Std. dev.</td></tr><tr><td>MeanBugResolutionTime (DV)</td><td>0.00</td><td>1546.1</td><td>33.8</td><td>97.6</td></tr><tr><td>CumBugsResolved</td><td>0.00</td><td>6148</td><td>484.0</td><td>881.8</td></tr><tr><td>DeveloperExperience</td><td>1.00</td><td>7.67</td><td>2.81</td><td>4.23</td></tr><tr><td>CumPctBugsAssigned</td><td>0.00</td><td>1.00</td><td>0.56</td><td>0.29</td></tr><tr><td colspan="5">ProjectCategory</td></tr><tr><td>Enterprise</td><td>0</td><td>1</td><td>0.06</td><td>0.24</td></tr><tr><td>Desktop</td><td>0</td><td>1</td><td>0.06</td><td>0.24</td></tr><tr><td>SysAdmin</td><td>0</td><td>1</td><td>0.10</td><td>0.31</td></tr><tr><td>Financial</td><td>0</td><td>1</td><td>0.01</td><td>0.11</td></tr><tr><td>Development</td><td>0</td><td>1</td><td>0.31</td><td>0.46</td></tr><tr><td>Games</td><td>0</td><td>1</td><td>0.08</td><td>0.27</td></tr><tr><td>Security</td><td>0</td><td>1</td><td>0.04</td><td>0.20</td></tr><tr><td>Multimedia</td><td>0</td><td>1</td><td>0.01</td><td>0.11</td></tr><tr><td>Database</td><td>0</td><td>1</td><td>0.07</td><td>0.26</td></tr><tr><td>Hardware</td><td>0</td><td>1</td><td>0.05</td><td>0.22</td></tr><tr><td>Networking</td><td>0</td><td>1</td><td>0.09</td><td>0.29</td></tr><tr><td>VoIP</td><td>0</td><td>1</td><td>0.01</td><td>0.11</td></tr><tr><td colspan="5">DeveloperCategory</td></tr><tr><td>1-2 Developers</td><td>0</td><td>1</td><td>0.08</td><td>0.28</td></tr><tr><td>3-7 Developers</td><td>0</td><td>1</td><td>0.30</td><td>0.46</td></tr><tr><td>8-15 Developers</td><td>0</td><td>1</td><td>0.28</td><td>0.45</td></tr><tr><td>&gt;15 Developers</td><td>0</td><td>1</td><td>0.33</td><td>0.47</td></tr></table>

## 3.2. Data collection

We collected data from SourceForge.net on a wide variety of project-related measures, including development status, rank, bugs reported, patches, feature requests, support requests, developer registrations, and project category. To avoid the pitfalls of spidering and parsing the Sourceforge.net website [8], we collected data directly from its database. SourceForge.net hosts over 100,000 OSS development projects with a centralized resource for managing projects, issues, communications, and code. It provides many tools to support collaborative development and allows developers to register their projects at no charge. These properties make it equally attractive to both large and small development efforts. Furthermore, the number of projects, the wide variety in terms of size and expertise, and the availability of event data made it an ideal data source for our research.

## 3.2.1. Project identification

Of course, there is a fair amount of ‘‘noise’’ in SourceForge data; some OSS teams use SourceForge as the ‘‘repository of record’’ instead of the ‘‘repository of use,’’ and thus are not responding to bugs. This can lead to inaccurate bug resolution data in the database. To address this issue, we collected data from the top 50 projects in each of SouceForge.net’s 13 primary software categories, ensuring that only projects actively in use were included in our sample.

Identification of top projects was based on two factors: development status and site rank. The first limited projects to those that had produced a production/stable version of the application; the developers of some were unresponsive to externally reported events (such as bug reports) and thus they had to be excluded. The second was to use SourceForge.net’s internal ranking system. It used three sub-factors (traffic, communication, and development) to determine an overall ranking of projects. This multi-factor system had several desirable qualities that enhanced the sample validity. One benefit of using this ranking system was that older projects tended to drop in activity and thus in ranking. Using the rank criterion also ensured that the selected projects reflected the current state of development.

Based on these factors, a ‘‘snapshot’’ of the top 50 projects in each of 13 categories was collected on March 9, 2006. However, one category, VoIP, had only 47 projects that had developed a production/stable version, resulting in an initial sample of 647 projects.

The final data set was reduced by applying three additional criteria for the sample we used in testing our research hypotheses. The criteria are summarized in Table 2.

As shown, when we applied these criteria, the sample was reduced to 118.

## 3.2.2. Bug tracking

SourceForge.net provided developers with tools for tracking four primary types of events: (1) bugs, (2) support requests, (3) patches, and (4) feature requests. We included data on all of these in our data set, referring to them collectively as bugs throughout the paper. An important measure of organizational learning was the comparison of the ratio between reported and resolved bugs. After applying all project selection criteria our final pool of bugs across the 118 projects in the sample consisted of 91,745 reported and 73,253 resolved. The data was then aggregated to produce weekly averages for each project. The result was a data set capturing 14,293 observations (project-weeks) across the 118 projects.

Table 2  
Project selection criteria for data sampling.

<table><tr><td>Criterion</td><td>Comment</td><td>Number of projects after applying criterion</td></tr><tr><td>Select top 50 projects from the 13 project categories</td><td>Rankings were based on SourceForge.net&#x27;s internal ranking system. With only 47 for one category</td><td>647</td></tr><tr><td>Resolve data duplication issues</td><td>61 projects were multi-listed (in two or more categories). These projects were only included in the category where they received the highest rank</td><td>586</td></tr><tr><td>Limit projects to those that were 2 years or older</td><td>The minimum project duration was established to allow a long enough adaptive learning observation period. 446 projects were less than 2 years old</td><td>140</td></tr><tr><td>Limit projects to those with a minimum of 100 reported bugs</td><td>This ensured that each project had sufficient bug data for analysis</td><td>118</td></tr></table>

## 3.2.3. Developers

We also collected information about the developers of a given project. For each week of the project, we counted the number of registered developers (DeveloperCategory), as well as the number of projects (DeveloperExperience) in which each developer was registered. Of course, the number of registered developers on a given project changed over time. For time periods where data was missing, we calculated a trend value using a linear regression ‘‘least sum of squares’’ formula. A linear trend was preferable to a curvilinear trend line based on characteristics of the data. We used this data to test our hypotheses that the percentage of bugs assigned to specific developers was negatively related to bug resolution time and that the average number of projects in which a developer participated was negatively related to bug resolution time.

## 4. Data analysis and discussion

The distribution of projects and project-weeks across project categories is shown in Table 3. In addition, Table 4 shows the distribution of project-size and project-weeks.

We used Stata/SE 9.2 [17] for our data analysis. We started our analysis by checking for problems with pairwise correlations between all independent variables. This required calculating the phi coefficient when both of the variables compared were dichotomous, the point-biserial correlation coefficient when one variable was dichotomous and the other one was continuous, and the Pearson correlation coefficient when both variables were continuous. The highest pairwise correlation coefficient was 46.4%, which is below the commonly used threshold of 60–80% suggested by Kennedy [11].

We next checked for the presence of multicollinearity by calculating the variance inflation factor (VIF). Our calculations showed VIF values that ranged between 1.16 and 4.90, well below the threshold value of 10, suggesting no multicollinearity problems. To test for autocorrelation (serial correlation), we used Wooldridge’s test [20] for autocorrelation in panel data models. Our calculation resulted in an insignificant test statistic, indicating the absence of serial correlation.

Distribution of projects and project-weeks.

<table><tr><td>Project category</td><td>Number of projects</td><td>Number of project-weeks</td></tr><tr><td>Clustering</td><td>6</td><td>599</td></tr><tr><td>Networking</td><td>8</td><td>1342</td></tr><tr><td>Multimedia</td><td>3</td><td>187</td></tr><tr><td>Hardware</td><td>7</td><td>709</td></tr><tr><td>VoIP</td><td>3</td><td>174</td></tr><tr><td>SysAdmin</td><td>12</td><td>1492</td></tr><tr><td>Games</td><td>9</td><td>1163</td></tr><tr><td>Security</td><td>9</td><td>1221</td></tr><tr><td>Development</td><td>32</td><td>4405</td></tr><tr><td>Database</td><td>9</td><td>1062</td></tr><tr><td>Enterprise</td><td>8</td><td>883</td></tr><tr><td>Desktop</td><td>9</td><td>868</td></tr><tr><td>Financial</td><td>3</td><td>188</td></tr><tr><td>Total</td><td>118</td><td>14,293</td></tr></table>

A likelihood ratio (LR) test indicated the presence of heteroskedastic data in our panel data. To correct for this, we used the Stata/SE 9.2 xtgls command, which fit panel-data linear models by using feasible generalized least squares analysis (FGLS) and allowed estimation in the presence of heteroskedasticity across panels. The model summary results and coefficient estimates are shown in Table 5.

## 4.1. Learning curve effect as reflected on bug resolution time

H1 stated that as the number of bugs resolved increased, the average bug resolution time decreased. The variable CumBugsResolved was defined as the total number of bugs resolved, per week, for weeks 1 thru 108. The regression model was applied to each ProjectCategory over the first 108 weeks of the life of the project.

As shown in Table 5, the negative coefficient for ln(CumBugs Resolved) (p < 0.00) indicated that average bug resolution time decreased as the cumulative number of bugs resolved increased, providing support for the hypothesis. This indicated the presence of a learning curve effect.

In addition to learning curve effect, we also investigated the presence of adaptive learning in our sample by examining the ratio of cumulative resolved bugs to cumulative reported bugs. We plotted a graph of project efficiency to show the effect of adaptive learning. For comparison, our study was based on the same 108- week period as Huntley’s study. Our study compared the first 108 weeks of 118 projects. The projects were categorized according to the number of developers (i.e., 1–2, 3–7, 8–15, and >15). The graph (Fig. 1) indicates that there was an adaptive learning process, but they depended on the number of developers. It was interesting to note that the fluctuation of efficiency over time was the smallest in projects with >15 developers and largest in projects with 1 to 2 developers.

One potential pitfall in measuring project efficiency and learning was the open source phenomenon of project branching. It was possible for several projects within the same project

Distribution of project size and project-weeks.

<table><tr><td>Project size</td><td>Number of project-weeks</td></tr><tr><td>1-2 Developers</td><td>1199</td></tr><tr><td>3-7 Developers</td><td>4349</td></tr><tr><td>8-15 Developers</td><td>4024</td></tr><tr><td>&gt;15 Developers</td><td>4721</td></tr><tr><td>Total</td><td>14,293</td></tr></table>

Model summary results and coefficient estimates (estimated using xtgls in Stata/SE 9.2).

<table><tr><td></td><td>Coefficient</td><td>Std. error</td><td>p-Values (P&gt;|z|)</td></tr><tr><td>(Constant)</td><td>2.48***</td><td>0.28</td><td>0.00</td></tr><tr><td>ln(CumBugsResolved)</td><td>-0.05***</td><td>0.01</td><td>0.00</td></tr><tr><td>ln(DeveloperExperience)</td><td>-0.42***</td><td>0.05</td><td>0.00</td></tr><tr><td>ln(CumPctBugsAssigned)</td><td>-0.08***</td><td>0.00</td><td>0.00</td></tr><tr><td colspan="4">ProjectCategory</td></tr><tr><td>SysAdmin</td><td>-2.55***</td><td>0.27</td><td>0.00</td></tr><tr><td>Clustering</td><td>-2.26***</td><td>0.28</td><td>0.00</td></tr><tr><td>Security</td><td>-2.05***</td><td>0.29</td><td>0.00</td></tr><tr><td>Hardware</td><td>-1.56***</td><td>0.28</td><td>0.00</td></tr><tr><td>Enterprise</td><td>-0.82***</td><td>0.30</td><td>0.01</td></tr><tr><td>Desktop</td><td>-0.73***</td><td>0.28</td><td>0.01</td></tr><tr><td>Development</td><td>-0.73***</td><td>0.27</td><td>0.01</td></tr><tr><td>Database</td><td>0.08</td><td>0.28</td><td>0.77</td></tr><tr><td>Networking</td><td>0.41</td><td>0.28</td><td>0.15</td></tr><tr><td>Games</td><td>0.43</td><td>0.28</td><td>0.13</td></tr><tr><td>Multimedia</td><td>1.40***</td><td>0.29</td><td>0.00</td></tr><tr><td>VoIP</td><td>5.38***</td><td>0.31</td><td>0.00</td></tr><tr><td colspan="4">DeveloperCategory</td></tr><tr><td>3-7 Developers</td><td>-2.42***</td><td>0.10</td><td>0.00</td></tr><tr><td>8-15 Developers</td><td>-3.06***</td><td>0.10</td><td>0.00</td></tr><tr><td>&gt;15 Developers</td><td>-2.70***</td><td>0.10</td><td>0.00</td></tr><tr><td colspan="4">Model summary</td></tr><tr><td>Estimated covariances</td><td>118</td><td></td><td></td></tr><tr><td>Estimated autocorrelations</td><td>0</td><td></td><td></td></tr><tr><td>Estimated coefficients</td><td>19</td><td></td><td></td></tr><tr><td>Log likelihood</td><td>-37,580.1</td><td></td><td></td></tr><tr><td>Wald  $\chi^2$ </td><td>6529.7</td><td></td><td></td></tr><tr><td>Prob. &gt; $\chi^2$ </td><td>0.00</td><td></td><td></td></tr></table>

Note: Significance level $= ^ { * * * } p$ < 0.01.

category to be project branches in which the same or similar code was used. This could lead to data confounding if bugs were moved from one project to another as branching occured. The selection procedure used to acquire our sample minimized the impact of project branching by relying, in part, on SourceForge.net’s internal ranking mechanism. This reduced the likelihood that projects with significant branches would be included in the sample. Only two of the projects in our sample produced branches. In each of these cases, the branches were formed to provide new functionality and thus did not impact bug data.

![](/api/attachments/JRT2QP6E/fulltext/images/a2bbf05717d0d88e0757bea99aa63ebff67b4174e1e940e924138a683a979e02.jpg)  
Fig. 1. Debugging efficiency of OSS projects.

## 4.2. Effect of developer’s OSS experience

H2 stated that teams with more experienced OSS developers resolved bugs faster. Developer’s OSS experience was based on the number of OSS projects in which a developer was registered for a given week. At $p < 0 . 0 0 ,$ the coefficient for ln(DeveloperExperience) was negative, indicating a decrease in MeanBugResolutionTime as DeveloperExperience increased.

We speculated that developers who worked on multiple OSS projects learned new coding techniques and other ‘‘best practices’’ from those projects and conveyed that knowledge to other teams to which they belonged. Each team thus benefits from a developer’s involvement with other teams.

Our results indicated the breadth of developer experience in and of itself had a significant effect on project performance in virtual teams. Thismay indicate that the coordinationmechanisms invirtual teams are conducive to social integration and knowledge sharing and may lead to improvement in transactive memory [19] where the team leverages its knowledge of who knows what to improve its application of resources and thus bug resolution efficiency.

## 4.3. Effect of bug assignment (task ownership)

H3 stated there is an inverse relationship between increasing the percentage of bugs assigned to specific developers and average bug resolution time. The results $( p < 0 . 0 0 0 )$ supported this with a negative coefficient for ln(CumPctBugsAssigned). If developers are assigned a task, or have ownership of a task, they are less likely to avoid resolving bugs in it. This finding also suggests that OSS projects can benefit from some of the practices commonly found in the more traditional software development projects.

## 4.4. Effect of project category

It was hypothesized that different project categories had different bug resolution times. To study this, we divided the projects into the primary categories used by SourceForge.net. We coded these categories using binary dummy variables. The analysis compared projects in the Financial (the reference category) to the other 12 categories. The primarily negative coefficients for the ProjectCategory variables showed that most project types had lower average bug resolution times than the reference category. Only Multimedia and VoIP projects had higher average bug resolution times. Although positive, the average times for Database, Games, and Networking projects were not significantly different from that of Financial projects. The other 9 project categories had coefficients that were different in value and statistically significant. This provided partial support for hypothesis H4.

Projects may also tend to differ in scope across categories and the nature of some project types, such as security, may demand frequent and rapid updates while others may require extensive reliability testing.

## 4.5. Effect of number of developers or team size

We also hypothesized that bug resolution time depended on project team size. To test this we divided the projects into four categories. We used dummy variables to represent these developer categories. The negative coefficients of the DeveloperCategory variables (indicated that all categories had lower resolution times than the reference category of 1 to 2 developers. The coefficients indicate a curvilinear pattern. The causes for this curvilinear pattern in the average bug resolution time include communication complexity, organizational complexity, management effectiveness and project complexity as the size of the project changes.

Table 6  
Summary of results.

<table><tr><td>Hypothesis</td><td>Variable</td><td>Supported?</td></tr><tr><td>H1</td><td>CumBugsResolved</td><td>Yes</td></tr><tr><td>H2</td><td>DeveloperExperience</td><td>Yes</td></tr><tr><td>H3</td><td>CumPctBugsAssigned</td><td>Yes</td></tr><tr><td>H4</td><td>ProjectCategory</td><td>Partial—Database, Financial, Games, and Networking did not show a significant difference in average bug resolution times</td></tr><tr><td>H5</td><td>DeveloperCategory</td><td>Yes</td></tr></table>

## 4.6. Summary of results

As shown is Table 6, all of our hypotheses were supported. Based on these results, we provide the following suggestions:

 Performance is best in moderately sized teams. OSS project managers formulate a strategy for breaking projects into subgroups when the number of active developers exceeds 15. The ideal size of each sub-group may be dependent on the project manager’s perception of the relative importance of efficiency versus bug resolution time. Each sub-group should have a leader that coordinates with the central development team, which takes on an oversight role to ensure the direction remains consistent with the goals of the overall project.

 Project performance improves when a greater percentage of bugs are assigned to specific developers. Therefore, OSS project managers should assign bugs to specific developers whenever possible. Preferably, bug assignment should be based on expertise and experience with a given task or module.

 Projects with developers who participate in a large number of other projects are more efficient in resolving bugs. Thus managers should encourage developers who work on multiple projects to participate in similar development projects.

 Knowledge sharing apparently increases when developers work on more projects. Developers learn when participating in projects and bring their knowledge back to teams in which they participate. Thus, managers should foster an environment that facilitates knowledge sharing.

## 5. Conclusions

Our study contributes to the body of literature by providing empirical evidence of virtual organizational learning in a large number of OSS development projects.

Our results suggest that both adaptive and organizational learning were observed in the projects. We also found that OSS development project performance was influenced by the number of developers on the team, the amount of experience that they possessed, project category, and percentage of bugs assigned to a person. In addition, our results indicated that though smaller teams learned faster, they suffered from greater variability in efficiency.

Open source developers work on projects voluntarily. As such, they tend to work on projects or tasks that they consider fun, interesting, challenging, and/or that can bring them notoriety. It is rare for traditional developers to be able to pick and choose projects or tasks. Also in OSS projects, end-users play a more interactive role. They review the actual code during development, run and test modules, suggesting modifications and even how to fix bugs.

Reliability and decreased cost are often cited as benefits of OSS [1]. There appears to be a camaraderie among the OSS community in which the lesser skilled developers can learn from the more experienced ones [21].

Development costs are lower because many, if not all, developers are volunteers. However, the cost of using the actual software may not be less. End-users and support staff still need training and more resources may be required to take full advantage of the software.

## Acknowledgments

The authors wish to thank the anonymous reviewers from the 18th Information Resources Management Association International Conference (IRMA2007) for useful suggestions on an early version of this paper, Greg Madey for providing access to SourceForge.net database, the participants in a seminar at the University of Texas at San Antonio in 2007 for their helpful comments, and the College of Business of the University of Texas at San Antonio for providing financial and technical support for this research.

## References

[1] M. AlMarzouq, L. Zheng, G. Rong, V. Grover, Open source: concepts, benefits, and challenges, Communication of the Association for Information Systems 2005 (16) 2005, pp. 756–784.

[2] L. Argote, S.L. Beckman, D. Epple, The persistence and transfer of learning in industrial settings, Management Science 36 (2), 1990, pp. 140–154.

[3] C. Argyris, D.A. Sch?n, Organizational Learning, Addison-Wesley, Readings, MA 1978.

[4] S. Christley, G. Madey, Analysis of activity in the open source software development community, in: R.H. Sprague, Jr. (Ed.), in: Proceedings of the 40th Hawaii International Conference on System Sciences, IEEE Computer Society Press, Los Alamitos, CA, 2007.

[5] R.M. Cyert, J.G. March, A Behavioral Theory of the Firm, Prentice-Hall, Englewood Cliffs, NJ, 1963.

[6] C.M. Fiol, M.A. Lyles, Organizational learning, Academy of Management Review 10 (4), 1985, pp. 803–813.

[7] R. Grewal, G.L. Lilien, G. Mallapragada, Location, location, location: how network embeddedness affects project success in open source systems, Management Science 52 (7), 2006, pp. 1043–1056.

[8] J. Howison, K. Crowston, The perils and pitfalls of mining SourceForge, in: Proceedings of Mining Software Repositories Workshop, International Conferenc on Software Engineering, Edinburgh. Scotland. 2004

[9] C.L. Huntley, Organizational learning in open-source software projects: an analysis of debugging data, IEEE Transactions on Engineering Management 50 (4), 2003, pp. 485–493

[10] H.G. Hwang, J. Guynes, The effect of group size on group performance in computer-supported decision making, Information & Management 26 (4), 1994, pp. 189–198.

[11] P. Kennedy, A Guide to Econometrics, fifth ed., The MIT Press, Cambridge, MA, 2003.

[12] E.A. Locke, G.P. Latham, Building a practically useful theory of goal setting and task motivation, American Psychologist 57 (2), 2002, pp. 705–717.

[13] A. Mockus, R.T. Fielding, J.D. Herbsleb, Two case studies of open source software development: Apache and Mozilla, ACM Transactions on Software Engineering and Methodology 11 (3), 2002, pp. 309–346

[14] B.E. Munkvold, I. Zigurs, Process and technology challenges in swift-starting virtual teams, Information & Management 44 (3), 2007, pp. 287–299.

[15] C. Okoli, W. Oh, Investigating recognition-based performance in an open content community: a social capital perspective, Information & Management 44 (3), 2007, pp. 240–252.

[16] R.H. Rasch, H.L. Tosi, Factors affecting software developers’ performance: an integrated approach, MIS Quarterly 16 (3), 1992, pp. 395–413.

[17] StataCorp, Stata Statistical Software: Release 9, StataCorp LP, College Station, TX 2005.

[18] M.M. Wasko, S. Faraj, Why should I share? Examining social capital and knowledge contribution in electronic networks of practice MIS Quarterly 29 (1), 2005, pp. 35–57.

[19] D.M. Wegner, Transactive memory: a contemporary analysis of the group mind, in: B. Mullen, G.R. Goethals (Eds.), Theories of Group Behavior, Springer-Verlag, New York NY 1986 pp. 185-205.

[20] J.M. Wooldridge, Econometric Analysis of Cross Section and Panel Data, The MIT Press, Cambridge, MA, 2002.

[21] C.-G. Wu, J.H. Gerlach, C. Young, An empirical analysis of open source software developers’ motivations and continuance intentions, Information & Management 44 (3), 2007, pp. 253–262.

[22] L.E. Yelle, The learning curve: historical review and comprehensive survey, Decision Sciences 10, 1979, pp. 302–328.

![](/api/attachments/JRT2QP6E/fulltext/images/1a4ba4dc084e9876eb4e0f67371fe9bc02783ba84fe6255299866610af83c5e4.jpg)

![](/api/attachments/JRT2QP6E/fulltext/images/82e4197f99bb8bd1e27144bbf24604e309000bbaaadf3c75101f7da05b18d38b.jpg)

Yoris A. Au is an assistant professor in the Department of Information Systems and Technology Management ofthe College of Business at the University of Texas at San Antonio. He received a Ph.D. in Information and Decision Sciences from the University of Minnesota. His research interestsincludeeconomicsoftechnologyadoption,open source software, and electronic billing and payment. He has published in such journals as Communications of the AIS, Electronic Commerce Research and Applications, Information & Management, Information Systems and E-Business Management, and Journal of Management Information Systems. He currently serves as an associate editor for Electronic Commerce Research and Applications.

Darrell R. Carpenter is Ph.D. candidate in information technology at The University of Texas at San Antonio. He received his masters degree in Information Technology from The University of Texas at San Antonio. His research interests include biometrics, information systems privacy, the influence of ethnicity on information system adoption, measurement of information system success in non-profit organizations, and open source software development.

![](/api/attachments/JRT2QP6E/fulltext/images/2d9ffd6a343e292b5985f90de1c11392ba944aabfd7a29444e6b3161997b00c6.jpg)

![](/api/attachments/JRT2QP6E/fulltext/images/a0a1ff3bb1fdae7251acbd3745925c3a95264d071b173a9634d6e555e919ccc0.jpg)

Xiaogang Chen is Ph.D. candidate of information technology at The University of Texas at San Antonio. He received his masters degree in Management Information Systems from Claremont Graduate University. His research interests include open source software, knowledge management, and virtual team cognition.

Jan Guynes Clark is professor of information systems at The University of Texas at San Antonio. She received her Ph.D. from the University of North Texas. Her research interests include the impact of information technologies on productivity and performance, information security, and IS strategies. Her publication have appeared in leading journals such as Commu nications of the AIS, Communications of the ACM, IEEE Transactions on Engineering Management, and Informa tion & Management.
