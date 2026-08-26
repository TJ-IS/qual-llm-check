---
otero_id: 5654
otero_key: "HQPYDFJA"
title: "A Structural Analysis of the Role of Superstars in Crowdsourcing Contests"
authors: "Shunyuan Zhang; Param Vir Singh; Anindya Ghose"
year: "2019"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0767"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [129.81.226.78] On: 08 February 2019, At: 09:57 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

![](/api/attachments/HQPYDFJA/fulltext/images/db3c3683945f3ac3bce6f0ffe1408b1a8bed5215fbcb33ca6a8a08b8e5d929b0.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# A Structural Analysis of the Role of Superstars in Crowdsourcing Contests

Shunyuan Zhang, Param Vir Singh, Anindya Ghose

To cite this article: Shunyuan Zhang, Param Vir Singh, Anindya Ghose (2019) A Structural Analysis of the Role of Superstars in Crowdsourcing Contests. Information Systems Research

Published online in Articles in Advance 31 Jan 2019

https://doi.org/10.1287/isre.2017.0767

Full terms and conditions of use: https://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2019, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# A Structural Analysis of the Role of Superstars in Crowdsourcing Contests

Shunyuan Zhang,<sup>a</sup> Param Vir Singh,<sup>a</sup> Anindya Ghose<sup>b,</sup> <sup>c</sup>

<sup>a</sup> Tepper School of Business, Carnegie Mellon University, Pittsburgh, Pennsylvania 15213; <sup>b</sup> Leonard N. Stern School of Business, New York University, New York, New York 10012; <sup>c</sup> Korea University Business School, Korea University, Seoul 136-701, South Korea Contact: shunyuaz@andrew.cmu.edu (SZ); psidhu@cmu.edu, http://orcid.org/0000-0002-0211-7849 (PVS); aghose@stern.nyu.edu (AG)

Received: October 26, 2016 Revised: July 11, 2017; September 18, 2017 Accepted: September 27, 2017 Published Online in Articles in Advance: January 31, 2019

https://doi.org/10.1287/isre.2017.076

Copyright: © 2019 INFORMS

Abstract. We investigate the long-term impact of competing against superstars in crowdsourcing contests. Using a unique 50-month longitudinal panel data set on 1677 software design crowdsourcing contests, we illustrate a learning efect where participants are able to improve their skills (learn) more when competing against a superstar than otherwise. We show that an individual’s probability of winning in subsequent contests increases significantly more after she has participated in a contest with a superstar coder than otherwise. We build a dynamic structural model with individual heterogeneity where individuals choose contests to participate in and where learning in a contest happens through an information theory-based Bayesian learning framework. We find that individuals with lower ability to learn tend to value monetary reward highly, and vice versa. The results indicate that individuals who greatly prefer monetary reward tend to win fewer contests, as they rarely achieve the high skills needed to win a contest. Counterfactual analysis suggests that instead of avoiding superstars, individuals should be encouraged to participate in contests with superstars early on, as it can significantly push them up the learning curve, leading to higher quality and a higher number of submissions per contest. Overall, our study shows that individuals who are willing to forego short-term monetary rewards by participating in contests with superstars have much to gain in the long term.

History: Vĳay Mookerjee, Senior Editor; Subodha Kumar, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0767.

Keywords: crowdsourcing contests • superstar efect • Bayesian learning • utility • economics of information system • dynamic structural model • dynamic programming • Markov chain Monte Carlo

## 1. Introduction

Crowdsourcing, a term initially coined by Howe (2006), refers to the act of an organization outsourcing a task that is traditionally performed by its employees to a large group of people (i.e., crowds) outside the organizational boundaries. By 2014, 85% of the best global brands had used crowdsourcing (Roth 2015). The market for crowdsourced professional services has crossed \$2.5 billion and is projected to double in the next five years (Shingles and Trichel 2014). Crowdsourcing has emerged as a popular approach for innovation, ideation, and software development because it enables firms to harness the power of crowds by reaching out to a large pool of potential talent.

Among the diferent types of crowdsourcing initiatives, crowdsourcing contests, where participants solve a well-defined problem and compete for a fixed prize, have attracted interest from practitioners as well as academics (Terwiesch and Xu 2008, Archak and Ghose 2010, Liu et al. 2014, Huang et al. 2012). Compared to in-house approaches, crowdsourcing contests allow firms access to a much larger and more diverse pool of workers and, as a result, arguably better solutions.

It also provides access to experts who evaluate the solutions, and the cost of failure is incurred by the solution providers. Popular examples of crowdsourcing platforms that follow the contest structure include Topcoder, Threadless, Hyve, and Freelancer.

While online crowdsourcing contests became quite popular only recently, they bear close resemblance to classical tournaments. Economic literature on tournament-style contests has highlighted a “superstar” efect, where participants may exert less efort and perform worse in the presence of a superstar contestant (who consistently far outperforms others), as their chances of winning are very low (Brown 2011, Tanaka and Ishino 2012). However, traditional tournaments difer from crowdsourcing contests on one critical dimension. In a traditional tournament setting, once a participant joins in a tournament, she cannot choose who her opponent will be in a particular contest/round. In contrast, in crowdsourcing contests, an individual can choose to join only that contest where her preferred opponents are participating. Hence, while an individual would find it dificult to avoid superstars in tournaments, they can do so in crowdsourcing contests. Archak (2010)

documented that individuals avoid competing with superstars because of the adverse superstar efect on Topcoder.com. The presence of superstars often leads to thin participation in contests, which has led to concerns expressed by practitioners (Mele 2011) because researchers have shown that the chances of achieving a high-quality best solution for an innovation-related task increase with the number of participants in a contest (Terwiesch and Xu 2008, Boudreau et al. 2011).

In this study, we argue that previous research on the role of superstars has considered superstars only as competitors and has largely ignored their role as a potential source to learn from. In crowdsourcing contests, the learning opportunities that participants provide to each other are particularly salient. For example, at Topcoder.com, participants interact with each other throughout a contest and can observe the best in action. Furthermore, participants who submit a solution gain access to the winning solution, which, along with the forum discussion, can help them learn what the winner did that bested them.

This study documents this learning efect using a 50-month longitudinal data set from Topcoder.com. We show that even though an individual’s probability of winning in a contest is significantly lower in the presence of a superstar, one’s performance in subsequent contests increases significantly after she has participated in a contest involving a superstar contestant. We build a dynamic structural model incorporating individual heterogeneity where individuals choose contests to participate in and where learning in a contest happens through an information theory-based Bayesian learning framework. We apply the Imai et al. (2009) (ĲC hereafter) method to obtain the full solutions of individuals’ dynamic programming (DP) problems. We find that individuals learn more when they compete in a contest involving a superstar than otherwise. We also find that individuals difer in their abilities to learn and their preferences for monetary awards. The results indicate that individuals who greatly prefer monetary rewards have a lower ability to learn. As a result, they tend to win fewer contests, as they rarely achieve the high skills needed to win a contest. In contrast, individuals who value monetary awards less have a higher ability to learn, they learn very quickly, and they end up winning most of the contests in the long run. The results also reveal that individuals who are unable to learn fast incur a much higher participation cost and, as a result, participate even less.

Our counterfactual analyses evaluate policy interventions to determine how a crowdsourcing contest platform such as Topcoder.com can improve the overall quality of submissions as well as help participants learn. The results show that if Topcoder.com incentivizes individuals to participate in projects with superstars initially, the average quality of solutions will increase significantly over time across projects. Additionally, on average, projects will receive more submissions, which will benefit both the crowdsourcing platform and contest sponsors.

Our paper makes several contributions. Ours is the first paper to document a positive learning efect from superstar competitors on others in crowdsourcing contests. We find that individuals may forgo shortterm monetary utility by participating in contests with superstars but may gain in the longer term because of learning benefits. Second, we show that participants on Topcoder.com difer in terms of their relative preferences for learning and earning, where participants who value earning more are more likely to avoid contests involving superstar participants. However, it is the learners who end up winning the most. Third, we show relevant policy interventions that may improve the quality and quantity of solutions at Topcoder, at the same time moving individuals faster through the learning curve. Finally, ours is one of the first frameworks that endogenizes learning as individuals selfselect into contests that difer in potential monetary reward and learning opportunities. Prior studies treat learning as an exogenous event that is not under the control of a user, a condition that may not hold in a number of settings. Our modeling framework can be used in such settings. Our information theoretic Bayesian learning model allows us to model learning over tasks that are partially related and helps us explain diferent learning rates across individuals and across tasks.

## 2. Relevant Literature

Our work is related to the emerging literature on crowdsourcing contests. Crowdsourcing contests, depending on the submission policy, can be generally categorized into three types: (1) completely blind contests, where the solutions are submitted confidentially only to the solution seekers (e.g., Bockstedt et al. 2016, Jeppesen and Lakhani 2010); (2) completely open contests, where the submitted solutions are public to all users before a winner is selected (e.g., Lu et al. 2017; Huang et al. 2012, 2014); and (3) partially blind contests, where the participants can access the solutions only after the contest is completed (Archak and Ghose 2010, Archak 2010). Our research context falls in to the third category. Completely blind contests ofer no opportunity for an individual to learn from others. Completely open contests ofer an open opportunity for an individual to learn from others. In contrast, partially open contests ofer this opportunity for an individual to learn from others only if he or she invests in competing with others. As a result, an individual’s choice of participating in a contest determines how much he or she can learn.

Most of the research on crowdsourcing contests has focused on finding the optimal design for crowdsourcing contests (Terwiesch and Xu 2008, Jeppesen and Lakhani 2010, Boudreau et al. 2011, Ales et al. 2017, Körpeoğlu and Cho 2018). Terwiesch and Xu (2008) establish that solution seekers facing innovation problems can benefit from a large pool of participants in crowdsourcing contests; that is, open entry is superior. Boudreau et al. (2011) show that an open innovation setting such as a crowdsourcing contest is eficient in finding at least one qualified solution. Jeppesen and Lakhani (2010) examine the impact of the technical expertise of a self-selected problem solver on the quality of a delivered solution to an openly broadcasted problem.

Two papers closely related to our research are those by Archak and Ghose (2010) and Archak (2010). Using data collected from Topcoder.com, Archak and Ghose (2010) show that when choosing new contests to participate in, the participants on Topcoder were more likely to choose those contests that involved programming language that they were less skilled in. They attribute this finding to a Topcoder participant’s preference for learning. Archak (2010) shows that potential participants are less likely to join a crowdsourcing contest involving superstars. He argues that a potential reason is that the probability of winning a contest decreases significantly when a superstar participates in it. These studies highlight the importance of learning and monetary rewards as motivations for individuals to participate in crowdsourcing contests. However, the learning captured in these studies ignores the influence of others on a coder’s learning. We build on this stream of literature and investigate how other contestants afect the learning of a participant in a contest.

Our paper is also related to the large body of economic literature studying the impact of dominant contestants on their opponents in tournament settings. On the theoretical literature side, Nti (2004) argues that lower-valuation players tend to decrease efort in the presence of asymmetry in contestants’ abilities. Baik (1994) argues that a player, under Nash equilibrium, may optimally reduce efort and perform worse if her competitor has a greater chance of winning. Harris and Vickers (1985, p. 194) analyze a perfect equilibrium in a tournament-style setting and show that if a contest player is “far enough ahead,” his or her opponents may give up as their probability of winning decreases. Empirical work on the superstar efect has found results that are consistent with what the aforementioned theoretical literature suggests. Brown (2011) found reduced performance of competitors associated with the presence of a superstar player in a contest (Tiger Woods, in her study). Tanaka and Ishino (2012) found a similar superstar efect in professional golf tournaments in Japan. In contrast to this literature, we highlight a long-term positive performance efect of competing against a superstar in crowdsourcing contests.

Finally, this paper is related to the learning (experience) curve literature as well as the Bayesian learning literature on individuals’ choices under uncertainty. Learning curves have been documented across a number of settings: manufacturing (aircraft production (Alchian 1963, Benkard 2000), truck manufacturing (Argote and Epple 1990), and semiconductor manufacturing (Hatch and Mowery 1998)), knowledge work (software development Boh et al. 2007, Singh et al. 2011), typing (Thurstone 1919), and learning lists of words (Delaney et al. 1998), and services (surgical procedures (Pisano et al. 2001, Reagans et al. 2005) and call centers (Mukhopadhyay et al. 2011)). The results from these studies indicate that individual performance improves when performing the same or a similar task repeatedly. However, in these studies, there is no clear underlying reasoning as to why learning occurs.

In contrast, the Bayesian learning models (Erdem and Keane 1996, Huang et al. 2014, Ackerberg 2003) capture learning through an information theory perspective. An individual is assumed to learn only when she receives new information. Jovanovic and Nyarko (1995) show how a Bayesian learning framework can be applied to explain learning curves in a variety of settings. They model that a manager updates her belief about the average optimal action for an activity by observing the outcome from the action on each repeated run. Similarly, Mitchell (2000) applies a Bayesian learning framework to explain the changes in firm size and the limits to firm scope.

While the classic learning curve framework is quite simple, we find that the Bayesian learning framework is more appropriate for our study because of some key advantages that it provides over the classical learning curve framework (Jovanovic and Nyarko 1995). A learning curve is typically modeled as a deterministic function between performance and experience, that is, $P _ { t + 1 } = a E _ { t } ^ { b }$ , where a and b are constants, $E _ { t }$ is the amount of experience (typically the number of repetitions) at time t, and $P _ { t + 1 }$ is the performance at t <sup>+</sup> 1. This model, while quite simple, captures two important properties of learning, the scope of learning through a progress ratio, say, c<sup>/</sup>a, where c is the maximum performance possible, and the speed of learning by learning rate b. However, this equation specifies only the first moments of the relationship; that is, the mean performance improves with experience. It cannot explain the variability in performance among equally experienced individuals. Individuals learn differently: some learn faster than others, and some may learn more from one task than another. An information theoretic based Bayesian learning model can precisely explain the learning curve as well as the variability in performance across individuals. Another advantage of the Bayesian learning model is that it can precisely capture learning even when the tasks in a sequence are only partially related, where some may be more related to prior tasks than others. A learning curve model assumes that all tasks are similar and that the amount of learning from a task depends only on the level of prior experience, and not the type of task. The crowdsourcing contests in our setting are related in several aspects, but each has a unique characteristic, making the application of classic learning curves problematic. Hence, a Bayesian learning model is an appropriate approach for us to adopt.

## 3. Research Context and

## Descriptive Statistics

This section discusses the research context of this paper. We also present descriptive information and model-free evidence from reduced-form analyses, which suggest that individuals learn more from contests involving superstars than otherwise.

## 3.1. Research Context and Data Statistics

The research context in this paper is software component design contests posted on Topcoder.com, the world’s largest software development community that hosts crowdsourcing contests.<sup>1</sup> Each contest (project) is open for a limited amount of time, typically a week or two.<sup>2</sup> Each of these contests entails developing a software solution for a scenario for which clear requirements are specified. Individuals can freely register to compete in a contest for a prespecified prize. Typically, a contest awards the best and second best solutions. The participant information is public, so everyone knows who is participating in a contest. Once a contest is launched, participants gain access to a contest-specific discussion forum, where they can ask a range of questions, from clarifications about requirements of the contest to assistance on any relevant aspect of programming. Typically, others participating in the contest actively help each other resolve any programming issues. The participants submit their solutions, which are evaluated by a community of experts, who assign each solution a final score. The solutions must be clearly documented, and once the contest is complete, all participants can download the solutions of others. Comparing one’s own approach with others’ in solving a problem provides great opportunities for learning. We argue that this learning would be even greater if one could compare her approach with that of a superstar, as the superstar’s approach would be closer to the optimal approach in solving the problem.

Contest information is posted on a contest-associated web page on which one can review information about the contest, such as the prize, requirements, participants, and deadlines. The whole process of a contest is split into multiple phases based on the deadlines announced on the web page. The registration phase starts at the “start date” and ends at the “register by” date. The submission phase starts at “register by” date and ends at the “submit by” date. Individuals who want to participate in a contest must register during the registration phase and submit a solution before the submission phase ends. A submission is graded by three reviewers and receives a score according to a scorecard that specifies project-specific requirements as well as technical requirements. Contestants may then appeal (if they feel necessary) the score given by the reviewers. After the appeal phase has ended, each submission receives a final score, and the placements of contestants in a contest are determined by the final scores.<sup>3</sup>

On the contest web page, individuals can also review registrant information, including their rating, which summarizes one’s performance history. Most of the ratings lie between 0 and 2700, with ratings in excess of 2700 being extremely rare. The rating indicates the skill level of an individual relative to others. The higher the rating, the higher the skill level. The rating of an individual increases (decreases) if she performs better (worse) on a contest than expected given her current skill and a number of other variables. Topcoder classifies developers into several segments based on their ratings. The highest-rated segment is developers with 2,200<sup>+</sup> ratings, whose IDs are coded red. The resulting distribution of coder ratings on Topcoder is a normal distribution. We classify an individual as a superstar if her rating is over 2,200 (i.e., her ID is red coded by Topcoder), because she is in the top 5% in terms of skills among all Topcoder developers.

We collect historical data from Topcoder.com. The data set contains 1,677 software design contests posted between January 2005 and April 2009. For each contest, we collect the prize and the contest-associated requirement specification document, which defines the problem to be solved and specifies the requirements to be met. Summary statistics for key variables are presented in Table 1.

## 3.2. Model-Free Evidence

To test whether competing with a superstar has any impact on one’s performance in a current or future contest, we run the following reduced-form linear regression:

$$
\begin{array}{r l} \text { Score } _ {i j} = & \text { Intercept } + \beta_ {1} \text { Rating } _ {i j} + \beta_ {2} \text { Rating } _ {i j} ^ {2} + \beta_ {3} \text { Superstar } _ {i j} \\ & + \beta_ {4} \text { Superstar } _ {i j - 1} + \beta_ {5} \text { Prize } _ {i j} + \beta_ {6} \text { SpecLength } _ {i j} \\ & + \text { Coder } _ {i} + \varepsilon_ {i j}. \end{array} \tag {1}
$$

Here, i represents the individual, and j represents the jth contest of individual i. The dependent variable, $S c o r e _ { i j } ,$ is the score received by individual i’s solution to contest $j .$ The variable $R a t i n g _ { i j }$ denotes the scaled rating (rating/100) of coder i at the time when she registered for contest j. Rating represents skill level. The score an individual receives should increase with her skill level. However, the margin of improvement with increasing skill should be lower once the skill level is high. To capture this nonlinear efect, we also account for the square of the rating in the model. $S u p e r s t a r _ { i j }$ is an indicator variable that equals 1 if coder i has a superstar opponent in contest $\dot { } \mathbf { \zeta } _ { j } \mathbf { ; \nabla }$ this variable accounts for the efect of the presence of a superstar in a project on the focal individual. Previous literature has argued that individuals perform worse in the presence of superstars in traditional tournaments. Supersta ${ \boldsymbol { r } } _ { i j - 1 }$ is an indicator variable that equals 1 (0) if coder i had (did not have) a superstar opponent in a previous contest <sup>(</sup>j <sup>−</sup>1<sup>)</sup>. This variable captures the impact of past participation in a project with a superstar on his performance in the current project. This is our key variable, which will reveal whether participation in projects with superstars leads to learning. We further control for two more variables that are contest specific and capture the challenging nature of a project. SpecLength represents the specified requirements involved in developing a solution for contest $j$ and is measured by the page length of the requirement specification document. Besides project-specified requirements, we also control for project prize, because projects that ofer a high prize amount may also have requirements that may be more dificult to complete. $P r i z e _ { i j }$ denotes the scaled monetary prize (first-place prize/USD 100) for the first-place winner in the jth contest of individual i. While we find that project prize and project requirements are positively correlated, the correlation coeficient is small. We have to rule out those individuals who submitted only once in our sample, and those projects for which the requirement specification documents were unavailable to be downloaded. In the end, we are left with 3,909 observations (i.e., 3,909 submission–score pairs). Coder , represents coder fixed efects and is incorporated to capture individual-specific and time-invariant factors that afect coders’ performance in a contest.

Table 1. Descriptive Statistics

<table><tr><td>Variable</td><td>Min</td><td>Max</td><td>Mean</td><td>Median</td><td>Std. dev.</td></tr><tr><td>First-place award (in USD)</td><td>100</td><td>3,000</td><td>674.7</td><td>700</td><td>348.2</td></tr><tr><td>Requirement specification length (in pages)</td><td>2</td><td>43</td><td>4.8</td><td>4</td><td>3.0</td></tr><tr><td>Number of submissions in a contest</td><td>1</td><td>26</td><td>2.7</td><td>2</td><td>1.9</td></tr><tr><td> $Mean\ rating^a$ </td><td>334</td><td>2,793</td><td>1,449.8</td><td>1,425.5</td><td>368.8</td></tr><tr><td>Max rating</td><td>334</td><td>2,793</td><td>1,694.2</td><td>1,684</td><td>440.8</td></tr><tr><td> $Mean\ score\ in\ a\ contest^b$ </td><td>50.4</td><td>99.9</td><td>87.7</td><td>89.1</td><td>6.9</td></tr><tr><td>Max score in a contest</td><td>50.4</td><td>100</td><td>91.1</td><td>93.1</td><td>6.7</td></tr><tr><td>Number of superstars in a contest</td><td>0</td><td>2</td><td>0.1</td><td>0</td><td>0.3</td></tr></table>

<sup>a</sup>Mean rating is the average of ratings of all contestants in that contest.  
<sup>b</sup>Mean score in a contest is the average of scores of all contestants in that contest.

The model specification in Equation (1) can help us disentangle the mechanisms of learning from superstars. The two mechanisms, learning through interactions with superstars and learning through accessing the superstar’s solution, lead to learning occurring at diferent stages. Learning through interactions with superstars would happen during the ongoing contest. If this learning were substantial, then a participant’s performance in the ongoing contest should be higher in the presence of a superstar contestant than otherwise. Learning through accessing the superstar’s solution takes place after a contest has ended and all the solutions have been evaluated by a review team. Only participants who submitted solutions for the project can access the solutions. Through reading and analyzing winning solutions, coders can learn and improve their skills. This learning happens after contest completion; hence, its efect would be demonstrated on a coder’s performance in future contests. If this learning were substantial, we should expect that the performance would be higher for a participant in a contest if he previously participated in a contest involving a superstar contestant than otherwise.

Table 2 reports the estimated coeficients from regressing coders’ submission scores on a set of variables, as specified in Equation (1). The results suggest a positive and significant impact of having a superstar contestant in a previous project on one’s performance in a current project. In our main model, we stick to the standard that a coder is a superstar if her rating is over 2,200 (column (2)), simply because 2,200 is the cutof Topcoder uses to define a “red coder,” which is the highest level a coder can achieve. To test whether this result is sensitive to the cutof position, we also present in the estimation results when diferent criteria, r, of superstars are taken. For example, for the case $r = 2 , 1 0 0$ (column (1)), a coder is a superstar if his individual rating is over 2,100. The qualitatively consistent results across the columns indicate that the results are robust to diferent rating cutof points.

Taking the results when the cutof is 2,200 (column (2)) as an example, while the presence of a superstar in a contest has a positive though insignificant $( \beta _ { 3 } = 0 . 2 1 2 ; \ p > 0 . 0 5 )$ impact on the performance of other participants, it has a positive and significant efect on the performance of participants in subsequent contests $( \beta _ { 4 } \dot { = } 0 . 8 2 0 ; p < 0 . 0 \dot { 5 } )$ ; that is, an individual’s submission score will significantly improve in future contests by nearly one point<sup>4</sup> if she competes with a superstar in the current contest. Our results indicate that competing with a superstar in a contest improves the performance of a contestant in future contests. Hence, learning by accessing and analyzing solutions by superstars is the main way of learning.

Table 2. Regression of Submission Score (Dependent Variable: score<sub>ij</sub>)

<table><tr><td>Variable meaning</td><td>Variable notation</td><td>Coef. notation</td><td>(1) (r = 2,100)</td><td>(2) (r = 2,200)</td><td>(3) (r = 2,300)</td></tr><tr><td>Rating/100</td><td> $Rating_{ij}$ </td><td> $\beta_1$ </td><td>1.901***(0.464)</td><td>1.913***(0.464)</td><td>1.924***(0.462)</td></tr><tr><td> $(Rating/100)^2$ </td><td> $Rating_{ij}^2$ </td><td> $\beta_2$ </td><td>-0.040**(0.014)</td><td>-0.041**(0.014)</td><td>-0.042**(0.014)</td></tr><tr><td>Presence of superstar in current contest</td><td> $Superstar_{ij}$ </td><td> $\beta_3$ </td><td>0.071(0.453)</td><td>0.212(0.415)</td><td>0.325(0.395)</td></tr><tr><td>Presence of superstar in previous contest</td><td> $Superstar_{ij-1}$ </td><td> $\beta_4$ </td><td>0.799*(0.389)</td><td>0.820*(0.363)</td><td>1.030**(0.352)</td></tr><tr><td>First-place prize/USD 100</td><td> $Prize_{ij}$ </td><td> $\beta_5$ </td><td>-0.054(0.051)</td><td>-0.052(0.051)</td><td>-0.044(0.052)</td></tr><tr><td>Length of specification document (page)</td><td> $SpecLength_{ij}$ </td><td> $\beta_6$ </td><td>-0.130*(0.052)</td><td>-0.131*(0.052)</td><td>-0.133*(0.052)</td></tr><tr><td>Intercept</td><td>Intercept</td><td>Intercept</td><td>69.685***(3.620)</td><td>69.573***(3.623)</td><td>69.446***(3.617)</td></tr><tr><td>R-squared</td><td></td><td></td><td>0.54</td><td>0.54</td><td>0.54</td></tr><tr><td>Fixed effect</td><td></td><td></td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Number of observations</td><td></td><td></td><td>3,909</td><td>3,909</td><td>3,909</td></tr></table>

Note. Robust standard errors are presented in parentheses.  
<sup>∗</sup>p < 0.05; <sup>∗∗</sup>p < 0.01; <sup>∗∗∗</sup>p < 0.001.

## 4. Model

In this section, we propose a structural model to explain the dynamics of individuals’ learning, winning, and contest choice behaviors. Typically, learning is modeled to either improve the performance on a task or to reduce the cost of performing a task. Our model captures both aspects of learning. First, we model that an individual’s solution quality may improve with experience. Second, we model an indirect efect of experience where the cost of producing a solution may also decrease for an individual as she learns. To identify the impact of participating in a contest with a superstar on learning, we allow the learning rate to be diferent from participating in a contest where a superstar is involved compared to otherwise.

## 4.1. Sequence of Events

We begin by summarizing the sequence of events in the model in each period (one week):

1. J software design projects are posted by Topcoder.com on its contest listing page.

2. An individual observes contest-specific information (i.e., prize, requirements, and descriptions) and registrant information (i.e., whether or not there is a superstar participant) for each posted project.

3. She estimates her expected lifetime value from participating in a contest. She then participates in at most one contest in a period.

4. During the contest, she may interact with other contestants on the contest discussion forum.

5. Upon completion of the contest, her submission receives a score. If she wins the contest, she receives the associated monetary reward.

6. Upon completion of the contest, she accesses other’s submissions.

7. The skill level of the participant is updated after the contest ends.

8. Steps 1–7 are repeated in the next period.

## 4.2. Learning

We first describe how learning to improve performance is captured in our structural model. As explained earlier, we follow Jovanovic and Nyarko (1995) and model this learning through an information theoretic Bayesian learning framework. Following this approach allows us to model learning in a structural framework and, hence, helps us avoid Lucas’s (1976) critique when running counterfactuals/policy simulations. Another advantage of this approach is that it allows us to model learning in scenarios where the contests are not identical and learning benefits may difer from one contest to another.

Let us say that the “best” way, not known to the individual at the outset, of solving a problem is $y .$

The problems on Topcoder.com are not exactly the same across contests but are closely related. As a result, we treat y as a random variable with mean y¯ and variance $\sigma _ { \omega } ^ { 2 }$ . This implies that for any contest, the best way to solve the problem is randomly drawn from this normal distribution of y. A problem j leads to its own optimal solution, $y _ { j } = \bar { y } + \omega _ { j } ,$ where $\omega _ { j } \sim N ( 0 , \sigma _ { \omega } ^ { 2 } )$ is transitory disturbances across contests capturing the diference across them. If an individual knows the exact value of $y _ { j } ,$ she can develop the optimal solution. The learning in our model entails learning the optimal ways to solve these problems, which corresponds to an individual’s learning about the distribution of $y ,$ specifically, the position of y¯. Let us represent an individual $i \prime \mathrm { s }$ belief about the mean optimal way to solve the problems at time t by a normal distribution with mean $\mu _ { i t }$ and variance $\sigma _ { \mu _ { i t } } ^ { 2 }$ . A contestant i learns about y¯ from each contest j she participates in through informative signals $\tilde { y } _ { i j } .$

$$
\tilde {y} _ {i j} = y _ {j} + \Delta_ {i j},\tag{2}
$$

where $\Delta _ { i j } \sim N ( 0 , \sigma _ { d } ^ { 2 } )$ captures the noise level in the delivered signal. The signal represents the information acquired by individual i by participating in contest $j ,$ analyzing the winning solution, and discussing it with others. The disturbance, $\Delta _ { i j } ,$ captures any deviations caused by instances where the winning solution may be the best among the submitted solutions but not the optimal solution, or the individual is unable to comprehend the solution even if it is optimal, or any other idiosyncratic reasons. Note that from the same contest $\dot { j } ,$ two participants may receive diferent signals. The received signal can also be written as

$$
\tilde {y} _ {i j} = \bar {y} + k _ {i j},\tag{3}
$$

where $k _ { i j } = \omega _ { j } + \Delta _ { i j }$ represents the combined noise. We model $k _ { i j } \sim \tilde { N } ( 0 , \sigma _ { k } ^ { 2 } )$ , where $\sigma _ { k } ^ { 2 } = \sigma _ { d } ^ { 2 } + \sigma _ { \omega } ^ { 2 }$ . Conditional on the received signals, the posterior variance over $\bar { y }$ is updated in a Bayesian manner (DeGroot 1970). To diferentiate between learning from the superstar versus others, we define $\Delta _ { i j } \sim \smile \smile { N } ( 0 , S u p e r s t a r _ { i j } \cdot \sigma _ { s s } ^ { 2 } + ( 1 -$ $S u p e r s t a r _ { i j } ) \cdot \sigma _ { n s } ^ { 2 } )$ , where Superst ${ \boldsymbol { \imath } } { \boldsymbol { r } } _ { i j }$ is an indicator variable that equals 1 if i faces a superstar opponent in contest $j ,$ and 0 otherwise. Here, $\bar { \sigma } _ { s s } ^ { 2 }$ is the signal variance specific to a contest involving a superstar, and $\sigma _ { n s } ^ { 2 }$ is the signal variance specific to contests not involving superstars. The total noise level received from a contest can be written as follows:

$$
\sigma_ {k} ^ {2} = \left\{ \begin{array}{l l} \sigma_ {s s} ^ {2} + \sigma_ {\omega} ^ {2} & \text { if   the   contest   involves   superstar } \\ & \text { opponents, } \\ \sigma_ {n s} ^ {2} + \sigma_ {\omega} ^ {2} & \text { otherwise. } \end{array} \right.\tag{4}
$$

Individuals will learn more from superstars than others if the signals from the contests involving superstars are more informative than others, that is, if $\dot { \phantom { } _ { s s } } \sigma _ { s s } ^ { 2 } < \sigma _ { n s } ^ { 2 }$

While we allow that diferent individuals may receive diferent signals from the same project, the differences are not systematic. However, individuals may inherently difer in their abilities to learn (Singh et al. 2011). To account for this heterogeneity, we allow the signals from same project to be systematically diferent across individuals. Specifically, we assume that the ability to infer the embedded information in a signal varies across individuals. We update the variance in the signal as $\sigma _ { k i } ^ { 2 }$ by incorporating an individual-specific variance component, $\tau _ { i } ,$ as follows:

$$
\sigma_ {k i} ^ {2} = \left\{ \begin{array}{l l} \sigma_ {s s} ^ {2} + \sigma_ {\omega} ^ {2} + \tau_ {i} & \text { if   the   contest   involves   superstar } \\ & \text { opponents, } \\ \sigma_ {n s} ^ {2} + \sigma_ {\omega} ^ {2} + \tau_ {i} & \text { otherwise. } \end{array} \right.\tag{5}
$$

We model log $\sqrt [ [object Object] ] { - ( \tau _ { i } , \sigma _ { \tau } ^ { 2 } ) }$ . Individuals will learn more if their $\tau _ { i }$ is smaller. Following Bayesian updating rules, we summarize the updating rules for $\sigma _ { \mu _ { i t } } ^ { 2 }$ and $\mu _ { i t }$ from participating in contest j at time t as (DeGroot 1970)

$$
\begin{array}{r} \mu_ {i t} = \left(\frac {\mu_ {i t - 1}}{\sigma_ {\mu_ {i t - 1}} ^ {2}} + \frac {\tilde {y} _ {i j}}{\sigma_ {k i} ^ {2}}\right) \left(\frac {1}{\sigma_ {\mu_ {i t - 1}} ^ {2}} + \frac {1}{\sigma_ {k i} ^ {2}}\right) ^ {- 1}, \\ \sigma_ {\mu_ {i t}} ^ {2} = \left(\frac {1}{\sigma_ {\mu_ {i t - 1}} ^ {2}} + \frac {1}{\sigma_ {k i} ^ {2}}\right) ^ {- 1}. \end{array}\tag{6}
$$

We now explain how learning afects the performance of an individual in a contest. Following Jovanovic and Nyarko (1995), we define a variable, $Q _ { i j t } ,$ that captures the relationship between individual $i ^ { \prime } \mathrm { s }$ solution $\mu _ { i t - 1 }$ and the optimal solution y, $Q _ { i j t } = A \cdot [ 1 -$ $\left( y _ { j } - \mu _ { i t - 1 } \right) ^ { 2 } ]$ . Here, A denotes the maximum score possible if the optimal solution $y _ { j }$ is reached, and $\mu _ { i t - 1 }$ represents individual $i \prime \mathrm { s }$ mean belief about the mean optimal solution at the beginning of period t when she chose contest $j .$ . Let us explain the logic behind this functional form. If a person knew the optimal solution, she would provide the optimal solution and would receive the maximum possible score of A in a contest. Similarly, a score an individual receives will vary based on how far her belief about the mean optimal solution is from its true value. The expected score of individual i on contest j, given her prior $\mu _ { i t - 1 }$ and $\sigma _ { \mu _ { i t - 1 } } ^ { 2 } ,$ can be written as

$$
E (Q _ {i j t}) = A \cdot (1 - \sigma_ {\mu_ {i t - 1}} ^ {2} - \sigma_ {\omega} ^ {2}),\tag{7}
$$

where $\sigma _ { \mu _ { i t - 1 } } ^ { 2 }$ is the prior variance of $i \prime \mathrm { s }$ belief over the mean optimal solution y¯ at the beginning of the contest. As one would notice from Equation (6), with learning, an individual would become more eficient because $\sigma _ { \mu _ { i t - 1 } } ^ { 2 }$ would decrease. As a result, the individual’s solutions would come closer to the optimal solutions. Note that Equation (7) suggests that an individual’s expected performance in period t depends only on $\sigma _ { \mu _ { i t - 1 } } ^ { 2 } .$ , that is, how far her belief deviates from the optimal solution, not the exact position of the optimal solution. In Online Appendix B, we present how to derive Equation (7) and discuss why, in our context, the exact position of the optimal solution is not needed to form an expectation on an individual’s performance.

## 4.3. Individual’s Per-Period Utility

We define the per-period utility function for an individual. Past literature has argued that individuals participate in crowdsourcing contests to earn money (Archak 2010). At the same time, participating in a contest is also time expensive. An individual has to spend time understanding the problem, producing the solution, asking for clarification, and so forth. Hence, we introduce two components in the utility function: winning benefits and cost disutility. Individuals may also care about learning (Archak and Ghose 2010), which is indirectly captured in the utility function, as it impacts winning benefits. Let $U _ { i j t }$ denote the utility that individual i derives from participating in contest $j \in \left\{ { 1 , 2 , \dots , J } \right\}$ in period t:

$$
U _ {i j t} = \left\{ \begin{array}{l l} \alpha_ {i} \cdot P r i z e _ {j t} + \gamma_ {i} \cdot C _ {i j t} + \varepsilon_ {i j t} & \text { if   } i \text {   wins   the   contest }, \\ \gamma_ {i} \cdot C _ {i j t} + \varepsilon_ {i j t} & \text { otherwise }, \end{array} \right.
$$

where $P r i z e _ { j t }$ denotes the monetary prize awarded to individual i in period t if she wins contest $j , \ C _ { i j t }$ denotes the hassle cost that individual i must incur in period t to complete contest $j ,$ and $\varepsilon _ { i j t }$ captures the individual’s action-specific random shocks and is assumed to follow a type I extreme value distribution. For identification, the mean utility from not participating in any contest (i.e., choosing the outside option) is normalized to zero. The decision-making process is governed by forming an expectation on the utility conditional on accumulated information, $I _ { i j t } . ^ { 5 }$ Let $\tilde { U } _ { i j t } ( a _ { i j t } \mid I _ { i j t } ) = E ( U _ { i j t } \mid I _ { i j t } , a _ { i j t } )$ denote the conditional expected utility. Then,

$$
\begin{array}{l} \tilde {U} _ {i j t} (a _ {i j t} \mid I _ {i j t}) \\ = \left\{ \begin{array}{l l} \alpha_ {i} \cdot E (P _ {i j t} \cdot P r i z e _ {j t} \mid I _ {i j t}) + \gamma_ {i} \cdot C _ {i j t} \mid I _ {i j t} \\ \text {   if   } a _ {i j t} = 1, \\ 0 \quad \text {   if   } a _ {i j t} = 0, \end{array} \right. \end{array}\tag{8}
$$

where $a _ { i j t }$ equals 1 if individual i participates in contest j in period t and 0 otherwise, $\bar { P _ { i j t } }$ represents the probability of i winning contest j at time $t ,$ and $E ( \bar { P _ { i j t } } \cdot \bar { P r i z e _ { j t } } | \bar { I _ { i j t } } )$ is the conditional expected monetary reward earned by individual i in contest j in period t.

## 4.4. Probability of Winning

There are three components that contribute to one’s chance of winning a contest. The first is the quality of the solution, $E ( Q _ { i j t } )$ , which represents individual $i \prime \mathrm { s }$ expected performance in contest j in period t. It represents the skill level of an individual. The second is the contest prize, $P r i z e _ { j t } ,$ which accounts for the possibility that contests with higher prizes may be dificult to win. The third is superstar presence, $S u p e r s t a r _ { i j t } ,$ which is included because superstars are highly skilled individuals who would be more likely to win the contest.<sup>6</sup> We write individual i’s probability of winning contest j posted in period t as

$$
\begin{array}{c} P _ {i j t} = 1 - (1) \cdot (1 + \exp (\varphi_ {1} \cdot P r i z e _ {j t} + \varphi_ {2} \cdot S u p e r s t a r _ {i j t} \\ + \varphi_ {3} \cdot E (Q _ {i j t}) + \varphi_ {4})) ^ {- 1}. \end{array}\tag{9}
$$

## 4.5. Hassle Cost

The hassle cost for individual i to complete project j at time t is expressed as

$$
\begin{array}{c} C _ {i j t} (a _ {i j t} = 1 \mid I _ {i j t}) = \eta_ {1} \cdot S p e c L e n g t h _ {j} + \eta_ {2} \cdot P r i z e _ {j t} \\ + \eta_ {3} \cdot \sigma_ {\mu_ {i t}} ^ {2} + \eta_ {4}. \end{array}\tag{10}
$$

We model the hassle cost for a project as a function of its requirements, its monetary prize, the skill of contestant $i , { \bar { } }$ and a fixed cost. The cost to develop a solution for the project should be afected by its requirements, SpecLength . The project prize is included to capture the complexity of the project. In equilibrium, projects that are more complex will ofer a higher prize. Thus, the prize ofered could signal a contest’s complexity.<sup>7</sup> Less skilled individuals can potentially incur greater costs because of repetition of efort. An individual’s skill, which is captured through the expected quality of the solution, is directly proportional to $\sigma _ { \mu _ { i t } } ^ { 2 }$ . Hence, we include $\sigma _ { \mu _ { i t } } ^ { 2 }$ to account for an individual’s skill level. Those with high values of $\sigma _ { \mu _ { i t } } ^ { 2 }$ do not know the optimal way to solve the problem and, hence, will have to exert more efort to come up with a solution.

## 4.6. State Variable

The individual-specific term that afects her utility over time is her skill, which is captured through expected the quality of the solution. The expected quality of the solution is determined by an individual’s belief about the mean optimal solution, which is afected by the contests in which a user has participated with and without a superstar opponent. Let $X _ { i t } ^ { n s }$ represent the number of contests until time t that individual i has participated in, where the contest involved no superstar opponent. Similarly, $X _ { i t } ^ { s s }$ represents the number of contests until time t involving a superstar opponent, that is, the number of times individual i has competed with a superstar opponent. We define the state space for individual i as $\dot { \boldsymbol { S } } _ { i t } = \{ X _ { i t } ^ { n s } , X _ { i t } ^ { s s } \}$ <sup>}</sup>. Note that we use the two experiences instead of the posterior variance $\sigma _ { \mu _ { i t } } ^ { 2 }$ because there is a one-to-one mapping from $X _ { i t } ^ { n s }$ and $X _ { i t } ^ { s s }$ to $\sigma _ { \mu _ { i t } } ^ { 2 }$ . Conditional on an individual’s action, the transition processes of the two state variables are deterministic and evolve as follows:

$$
X _ {i t} ^ {n s} = \left\{ \begin{array}{l l} X _ {i t - 1} ^ {n s} + 1 & i f \exists j \in \{1, 2, \ldots , J \}, \\ & s. t. a _ {i j t - 1} \cdot (1 - S u p e r s t a r _ {i j t}) = 1, \\ X _ {i t - 1} ^ {n s} & \text {otherwise}, \end{array} \right.\tag{11}
$$

$$
X _ {i t} ^ {s s} = \left\{ \begin{array}{l l} X _ {i t - 1} ^ {s s} + 1 & i f \exists j \in \{1, 2, \ldots , J \}, \\ & s. t. a _ {i j t - 1} \cdot (S u p e r s t a r _ {i j t}) = 1, \\ X _ {i t - 1} ^ {s s} & \text {otherwise}. \end{array} \right.
$$

The previously mentioned transition processes indicate that $i \prime \mathrm { s }$ experience of participating in a contest involving a superstar participant in period $t , \ X _ { i t } ^ { s s } .$ would increase by 1 if she competed with a superstar in the preceding period and would remain the same otherwise. Similarly, her experience of participating in a contest that did not involve a superstar participant in period $t , X _ { i t } ^ { n s }$ , would increase by 1 if she participated in a contest that did not have a superstar opponent in the preceding period, and would remain the same otherwise. Since we allow individuals to choose an outside option, the two experiences would both remain unchanged if the outside option was chosen in the preceding period.

## 4.7. Individual’s Optimal Contest Participation Choice

An individual chooses an action to maximize a discounted stream of the sum of the expected future utility flow. In other words, an individual i makes an infinite sequence of decisions $\{ a _ { i j t } , j = 0 , 1 , 2 , \ldots , J \} _ { t = 0 } ^ { \infty }$ 0 such that

$$
\begin{array}{r} \max _ {\{a _ {i j t} \} _ {t = 0} ^ {\infty}} E _ {\varepsilon_ {i j t}} \Bigg \{\tilde {U} _ {i j 0} (a _ {i j 0} \mid I _ {i j 0}) + \varepsilon_ {i j 0} \\ + \sum_ {t = 1} ^ {\infty} \beta^ {t} \cdot (\tilde {U} _ {i j t} (a _ {i j t} \mid I _ {i j t}) + \varepsilon_ {i j t}) \Bigg \}, \end{array}\tag{12}
$$

where $\tilde { U } _ { i j t } ( a _ { i j t } \mid I _ { i j t } )$ is individual $i \prime \mathrm { s }$ per-period utility conditional on his action $a _ { i j t }$ and available information $I _ { i j t } ,$ as expressed in Equation (8).

Alternatively, we drop subscripts i and j for simplicity and write a value function $\hat { V } ( \boldsymbol { S } _ { t } )$ to represent the stream of expected utility flow under the optimal contest choice policy function:

$$
\begin{array}{r l} & V (S _ {t}, \varepsilon_ {t}; \boldsymbol {\Theta}) = \max _ {\{a _ {t} \} _ {t = 0} ^ {\infty}} E _ {\{S _ {\tau}, \varepsilon_ {\tau} \} _ {\tau = t + 1} ^ {\infty}} \Bigg \{\tilde {U} _ {i j t} (S _ {t}, a _ {t}; \boldsymbol {\Theta}) + \varepsilon_ {t} \\ & \qquad + \sum_ {\tau = t + 1} ^ {\infty} \beta^ {\tau - t} \cdot \tilde {U} _ {\tau} (S _ {\tau}, a _ {\tau}; \boldsymbol {\Theta} | a _ {\tau - 1}, S _ {\tau - 1}) + \varepsilon_ {\tau} \Bigg \}, \end{array}\tag{13}
$$

where Θ is the set of structural parameters of the conjectured utility function, and $\varepsilon _ { t }$ is the unrealized transitory shock, which is assumed to follow a type I extreme value distribution and to be independent and identically distributed (i.i.d.) across individuals, periods, and contests.

Since individuals are dealing with the infinite horizon DP problem, the optimization can be solved by the Bellman (1957) equation. We drop the time subscript t in the value function $V ( S _ { t } , S _ { t } , \varepsilon _ { t } ; \mathbf { \hat { \Theta } } )$ because it is a stationary policy function. Following (Rust 1987), the DP problem can be characterized by the integrated value function (by integrating out future shocks), if assuming $\bar { V } ( S ^ { \prime } ; \Theta )$ independence and i.i.d. error terms. Then, we write the choice-specific value function (excluding shock ε) as follows:

$$
v (S, a; \boldsymbol {\Theta}) = \tilde {U} (S, a; \boldsymbol {\Theta}) + \beta \sum_ {S ^ {\prime}} \bar {V} (S ^ {\prime}; \boldsymbol {\Theta}) f _ {s} (S ^ {\prime} \mid a, S),\tag{14}
$$

where $S ^ { \prime }$ and $\varepsilon ^ { \prime }$ indicate the state and transitory shocks in the next period, respectively, conditional on the individual’s current state S and choice a; $\tilde { U } ( S , a ; \Theta )$ is the mean utility associated with state $S ,$ action $^ { a , }$ and parameters $\Theta ;$ and $f _ { s } ( \cdot )$ is the transition density function that governs the state transition process, conditional on the individual’s current state and contest choice. The integrated value function, which we refer to as Emax function, is

$$
\begin{array}{r l} & {\bar {V} (S ^ {\prime}; \Theta) = \int \max _ {a} \bigg \{\tilde {U} (S, a; \Theta) + \varepsilon} \\ & {\qquad + \beta \sum_ {S ^ {\prime}} \bar {V} (S ^ {\prime}; \Theta) f _ {s} (S ^ {\prime} \mid a, S) \bigg \} d G _ {\varepsilon} (\varepsilon),} \end{array}\tag{15}
$$

where $G _ { \varepsilon } ( \cdot )$ denotes the cumulative density function of the generalized extreme value function.

The individual’s dynamic optimization problem is summarized as follows: option j is chosen if and only if

$$
\begin{array}{r l} & v (S, j; \mathbf {\Theta}) + \varepsilon (j) \geq v (S, l; \mathbf {\Theta}) + \varepsilon (l) \\ & \quad \forall   l \in \{0, 1, 2, \ldots , J \} \text {and} l \neq j, \end{array}\tag{16}
$$

where option $l = 0$ represents an outside option.

## 4.8. Unobserved Heterogeneity

To account for unobserved heterogeneity among individuals, we allow the parameters governing the utility function to be individual specific, and we follow a hierarchical Bayesian framework (Rossi et al. 2005). Specifically, we assume a multivariate distribution on the set of individual-level coeficients.

We assume that individual-specific parameters $\mathbf { \theta } _ { i } =$ $( \alpha _ { i } , \rho _ { 1 i } , \rho _ { 2 i } , \rho _ { 3 i } )$ follow the following distribution, with α and $\rho$ capturing the individual’s preferences over the monetary awards from winning a contest and the hassle cost of completing a contest, respectively:<sup>8</sup>

$$
\boldsymbol {\theta} _ {i} = \left( \begin{array}{c} \alpha_ {i} \\ \rho_ {1 i} \\ \rho_ {2 i} \\ \rho_ {3 i} \end{array} \right) \sim \operatorname{MVN} (\bar {\theta}, \Sigma),\tag{17}
$$

where MVN denotes a multivariate normal distribution, $\bar { \theta }$ denotes the mean of $\mathbf { \boldsymbol { \mathsf { 6 } } } _ { i } ,$ , and $\Sigma$ denotes the variance and covariance matrix of $\mathbf { \theta } _ { \mathbf { \theta } _ { i } }$ . Hence, the parameters to be estimated are $\pmb { \Lambda } = ( \bar { \Theta } , \dot { \Sigma } , \rho _ { 4 } )$ . We discuss the estimation and identification in Section 5.

## 5. Estimation and Identification

The parameters to be estimated in our model are $\Theta = \hat { \{ } \{ \{ \alpha _ { i } , \rho _ { 1 i } , \rho _ { 2 i } , \rho _ { 3 i } \}  _ { i = 1 } ^ { I } , \rho _ { 4 } , \{ \tau _ { i } \} _ { i = 1 } ^ { I } , \sigma _ { \omega } ^ { 2 } , \sigma _ { s s } ^ { 2 } , \sigma _ { n s } ^ { 2 } , \varphi _ { 1 } , \varphi _ { 2 } ,$ $\varphi _ { 3 } , \varphi _ { 4 } \} ; ( \alpha _ { i } , \rho _ { 1 i } , \rho _ { 2 i } , \rho _ { 3 i } , \rho _ { 4 } )$ is the parameter vector in the utility function, $\\\dot { \sigma } ^ { 2 } = \dot { ( \bar { \tau } _ { i } , \sigma _ { \tau } ^ { 2 } , \sigma _ { \omega } ^ { 2 } , \bar { \sigma } _ { s s } ^ { 2 } , \sigma _ { n s } ^ { 2 } ) }$ <sup>)</sup> is the learning-related parameter vector, and $\varphi = ( \varphi _ { 1 } , \varphi _ { 2 } , \varphi _ { 3 } , \varphi _ { 4 } )$ is the parameter vector for estimating the probability of winning a contest. To alleviate the computational burden, we estimate the set of parameters sequentially in the following order: (1) learning-related parameters, (2) winning-related parameters, and (3) contest choice– related parameters. We start with the estimation of $\sigma ^ { 2 }$ .

5.1. Estimating Learning-Related Parameter $\sigma ^ { 2 }$ The likelihood of observed series of scores in contests participated in over time by individual i is given as

$$
\begin{array}{l} L (\text {Score} _ {i} \mid \sigma^ {2}, D a t a) \\ = \prod_ {t = 1} ^ {T _ {i}} \prod_ {j = 0} ^ {J} \left(\frac {\exp [ - (S c o r e _ {i j t} - E (Q _ {i j t})) ^ {2} / (2 \varepsilon^ {2}) ]}{\sqrt {2 \pi \varepsilon^ {2}}}\right) ^ {a _ {i j t}}. \end{array}\tag{18}
$$

The learning-related parameters consist of both individual-specific parameter $\tau _ { i }$ and parameters common across individuals, $\sigma _ { \omega } ^ { 2 } , \ \sigma _ { s s } ^ { 2 } ,$ and $\scriptstyle { \hat { \sigma } } _ { n s } ^ { 2 }$ . Hence, the estimation is performed in a hierarchical Bayesian framework by making draws from a posterior distribution of $\mathbf { \sigma } ^ { \sigma ^ { 2 } }$ using a Markov chain Monte Carlo (MCMC) approach. We discuss details of the estimation in Online Appendix A.

## 5.2. Estimating Winning-Related Parameter ϕ

Most contests ofer awards for the first two places. Since the second-place winner is awarded half of the prize amount awarded to the first-place winner, we employ two series of logistic regressions from Equation (9) to estimate $\varphi$ for the probabilities of winning first place and of winning either of the first two places.

## 5.3. Estimating Contest Choice–Related Parameters α and ρ

Conditional on the current state, an individual’s contest choice decision can be described as sequentially solving the following DP problem:

$$
\left\{a _ {i j t} \right\} _ {t = 0} ^ {\infty} = \underset {\left\{a _ {i j t} \right\} _ {t = 0} ^ {\infty}} {\arg \max} E _ {\varepsilon_ {i j t}} \left\{\sum_ {t = 0} ^ {\infty} \beta^ {t} \cdot (\tilde {U} _ {i j t} (a _ {i j t} \mid I _ {i j t}) + \varepsilon_ {i j t}) \right\},\tag{19}
$$

where $\tilde { U } _ { i j t }$ is individual $i \prime \mathrm { s }$ expected utility from choosing action $a _ { i j t }$ , conditional on i’s current period information set $I _ { i j t }$ and structural parameters Θ. The discrete choice dynamic programming (DDP) model has been widely applied in economics, information system, and marketing studies (Rust 1987, Hotz and Miller 1993, Aguirregabiria and Mira 2007, Zhang 2010, Huang et al. 2015). Traditional estimation methods include the nested fixed-point algorithm (Rust 1987) and conditional choice probability–based estimation strategies (Hotz and Miller 1993, Bajari et al. 2007, Arcidiacono and Miller 2011). In this study, we employ a Bayesian estimation algorithm developed by Imai et al. (2009), since it allows us to estimate heterogeneous parameters in a hierarchical Bayesian framework under a relatively low computational burden. Additionally, in the study of DDP, several methods have been proposed to approximate the DP solution (e.g., Keane and Wopin 1997, Ackerberg 2009) to overcome the “curse of dimensionality.”<sup>9</sup> One of the advantages of the ĲC method is that it provides an algorithm comparable to some of the state-of-the-art approximation approaches (Ching et al. 2012) while avoiding the complexity of searching for a global optimum of the data likelihood function.

The ĲC method combines the Bayesian MCMC approach with the DDP solution algorithm in a single algorithm, solving the DP problem and simulating the posterior distribution of parameter vectors simultaneously. The ĲC algorithm computes a pseudo-Emax function based on the parameter draw in each iteration. The pseudo-Emax function and associated parameter draw are saved to approximate the expected future value function, which will be used to calculate the probability of accepting a proposed draw of the parameter vector. The algorithm is eficient in that it keeps the most recent (and, hence, most accurate) parameter draws and past pseudo value functions to compute a (weighted average) approximation of the expected value function.<sup>10</sup> Imai et al. (2009) have shown that by repeatedly drawing parameter vectors from a pseudo Markov chain, most of the parameter vectors are drawn from a distribution close to the true posterior distribution after the initial draws (i.e., burn-in). Having the Bellman operator applied only once in each estimation step, the ĲC algorithm is able to provide a full solution of the DP problem at a computational burden with an order of magnitude comparable to that of solving for a static model. We provide the details of our estimation steps using ĲC in Online Appendix A and discuss the pros and cons of the ĲC estimation strategy in Online Appendix B. Table 3 summarizes the parameters through the three steps of the estimations and presents the explanation of each parameter.

## 5.4. Identification

We discuss the identification of our model here. All parameters are identified based on the variation in the data. Moreover, to identify our model, we fix discount factor $\beta$ as a constant between 0 and 1 (Rust 1987).

Table 3. Summary of the Parameters

<table><tr><td>Parameter name</td><td>Explanation</td></tr><tr><td colspan="2">Discount factor</td></tr><tr><td> $\beta$ </td><td>The amount (fraction) that an individual discounts from future payoff; fixed to 0.99 to identify other model primitives.</td></tr><tr><td colspan="2">Learning-related parameters</td></tr><tr><td> $\sigma_{\omega}^{2}$ </td><td>Transitory random shocks across contests</td></tr><tr><td> $\sigma_{ss}^{2}$ </td><td>Noise level in the signal from contests in the presence of superstars</td></tr><tr><td> $\sigma_{ns}^{2}$ </td><td>Noise level in the signal from contests in the absence of superstars</td></tr><tr><td> $\bar{\tau}_{i}$ </td><td>Mean of log individual learning ability</td></tr><tr><td> $\sigma_{\tau}^{2}$ </td><td>Variance of log individual learning ability</td></tr><tr><td colspan="2">Winning-related parameters</td></tr><tr><td> $\varphi_{1}$ </td><td>Coefficient corresponding to contest prize (in USD 100)</td></tr><tr><td> $\varphi_{2}$ </td><td>Coefficient corresponding to presence of superstar</td></tr><tr><td> $\varphi_{3}$ </td><td>Coefficient corresponding to individual&#x27;s quality of solution</td></tr><tr><td> $\varphi_{4}$ </td><td>Intercept in the equation for determining the probability of winning</td></tr><tr><td colspan="2">Contest choice–related parameters</td></tr><tr><td> $\alpha$ </td><td>Mean of individual&#x27;s coefficient of expected winnings (in USD 100)</td></tr><tr><td> $\sigma_{\alpha}^{2}$ </td><td>Variance of individual&#x27;s coefficient of expected winnings (in USD 100)</td></tr><tr><td> $\rho_{1}$ </td><td>Mean of individual&#x27;s coefficient of the length of specification document in hassle cost term</td></tr><tr><td> $\sigma_{\rho_{1}}^{2}$ </td><td>Variance of individual&#x27;s coefficient of the length of specification document in hassle cost term</td></tr><tr><td> $\rho_{2}$ </td><td>Mean of individual&#x27;s coefficient of prize in hassle cost term</td></tr><tr><td> $\sigma_{\rho_{2}}^{2}$ </td><td>Variance of individual&#x27;s coefficient of prize in hassle cost term</td></tr><tr><td> $\rho_{3}$ </td><td>Mean of individual&#x27;s coefficient of individual skill level in hassle cost term</td></tr><tr><td> $\sigma_{\rho_{3}}^{2}$ </td><td>Variance of individual&#x27;s coefficient of individual skill level in hassle cost term</td></tr><tr><td> $\rho_{4}$ </td><td>Fixed cost in hassle cost term</td></tr></table>

In general, a discount factor in a standard dynamic discrete choice model cannot be jointly identified with an individual’s utility function and belief about future states (Rust 1994, Magnac and Thesmar 2002). We fixed the discount factor to 0.99.<sup>11</sup>

To identify learning-related parameters, we fix A to 100, since A captures the maximum achievable score, and 100 is the maximum score a submission can receive. We further fix prior $\sigma _ { \mu _ { 0 } } ^ { 2 }$ to 0.2 for identification purposes. The rate at which the final score of an individual increases across contests as she gains experience by participating in contests helps identify the learningrelated parameters. The parameter that captures learning from a superstar is identified by comparing the performance trajectories of individuals who participated in contests without superstars to those of individuals who participated in contests with superstars. Individual-specific learning ability is identified via the variation in the performance improvement after participating in a project across individuals, conditional on other factors such as the presence of a superstar and one’s prior skill.

Winning-related coeficients $\varphi = ( \varphi _ { 1 } , \varphi _ { 2 } , \varphi _ { 3 } , \varphi _ { 4 } )$ are identified through the variations in the data of contestants’ placements in contests. For example, the coeficient of contest prize, $\varphi _ { 1 } ,$ is identified through the variation in contestants’ placement under varying contest prizes, everything else equal. The coeficient of superstar, $\varphi _ { 2 } ,$ is identified through the impact of a superstar on the likelihood of her opponent winning the contest. One should be more likely to win a contest as she improves her skill level, which helps us identify the coeficient of quality of solution, $\varphi _ { 3 }$

The utility is a function of the expected probability of winning and the hassle cost. When the hassle cost stays the same, the changes in the expected probability of winning help us estimate α. Similarly, when the expected probability of winning stays the same, the changes in hassle cost help us estimate gamma. Conditional on the identified $\mathbf { \hat { o } } ^ { 2 }$ and $\varphi ,$ , the parameters of hassle cost, $\rho ,$ are identified by the average frequency with which contestants submit solutions for a given contest. For instance, the coeficients of contest prize and length of the specification document are identified through the variations in the number of submissions for projects under varying prizes or complexities. The dynamics of contestants’ overall participation behaviors as individuals learn and improve helps us identify the coeficient of skill level; that is, if one has to incur a higher cost to complete a project when she has a lower skill level, then we will observe that one submits more frequently when she improves her skill level.

Conditional on identified $\textstyle \mathbf { \sigma } ^ { 2 } , \mathbf { \varphi } \varphi ,$ , and $\rho ,$ the parameter of expected reward, $\alpha ,$ can be identified from the dynamics in individuals’ contest choice behaviors. For example, consider that an individual’s per-period utility is composed of two parts: the expected reward from winning a contest and the expected hassle cost of completing the contest. Hence, a coder would be more likely to choose a contest with higher expected reward, holding hassle cost and learning benefit equal. Furthermore, when comparing two coders with the same $\sigma ^ { 2 }$ $\varphi , \mathsf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf { \mathbf \mathbf { \mathbf { \mathbf \mathbf { \mathbf { \mathbf \mathbf { \mathbf \Lambda } } } } } } } } } } } } } }$ and skill level, we would observe that the one with a greater α is more actively competing in contests, although for each project, they have the same probability of winning and the same amount of hassle cost.

## 6. Results

In this section, we present and discuss the estimation results, starting with the learning-related parameter $\mathbf { \sigma } ^ { \sigma ^ { 2 } }$

## 6.1. Learning-Related Parameter $\sigma ^ { 2 }$

We report the estimation results of $\mathbf { \sigma } ^ { \sigma ^ { 2 } }$ in Table 4. The estimation is performed in a hierarchical Bayesian framework by making draws from a posterior distribution of $\sigma ^ { 2 }$ using an MCMC approach. To guarantee that variances $\sigma _ { n s } ^ { 2 } , \sigma _ { s s } ^ { 2 } .$ , and $\tau _ { i }$ are positive, we estimate $\log ( \sigma _ { n s } ^ { 2 } )$ , log $\left( \sigma _ { s s } ^ { 2 } \right)$ , and $\log ( \tau _ { i } )$ instead. The MCMC diagnostic was performed to check the convergence of the Markov chains (Gilbride and Allenby 2004), which we checked at multiple starting points and by inspection of time-series plots. We noticed that chains reached stationarity and common convergence, suggesting that the chains had “forgotten” the initial values. In addition, we calculated Gelman and Rubin (1992) convergence statistics and found that the statistics were below 1.01, suggesting a good convergence of the Markov chains.

The mean of individual learning ability exp<sup>(−</sup>2.273<sup>)</sup> $= 0 . 1 0 3$ and the corresponding variance of 1.648 suggest a considerable level of heterogeneity across the population, as shown in Figure 1. This indicates that some individuals are very fast at learning compared to others. The parameter $\sigma _ { \omega } ^ { 2 }$ has a value of 0.0620, which shows that there is some variance for optimal solutions across contests. The values for parameters $\sigma _ { s s } ^ { 2 } = $ exp<sup>(−</sup>1.852<sup>) </sup> 0.157 and $\sigma _ { n s } ^ { 2 } = \exp ( - 0 . { \dot { 3 } } 4 0 ) = 0 . 7 1 2$ suggest a more informative signal from contests involving superstars than otherwise. This implies that individuals would learn more from contests involving superstars than otherwise. For example, to decrease the prior variance by approximately 50%, a representative individual, whose individual learning ability equals the population mean, that is, $\tau _ { i } = 0 . 1$ , could either participate in two contests with each involving a superstar opponent or participate in six contests with none involving a superstar opponent. In Figure 2, we show the speed of learning with and without participation in contests involving superstars. Since the learning is inversely proportional to the posterior variance $\sigma _ { \mu i t } ^ { 2 }$ of an individual, we plot the posterior variance on the y-axis and number of projects participated in on the x-axis.

Figure 1. Histogram of Individual Learning Ability $\tau _ { i }$  
![](/api/attachments/HQPYDFJA/fulltext/images/ce1e61411ea9a17fb66d2bc340a3451ba4c0f393118ec70c193188d7c56310e6.jpg)

Figure 2. Comparison of Impact of Experience in Contests With and Without Superstars on Learning  
![](/api/attachments/HQPYDFJA/fulltext/images/0c2786aaaf1e3ac17a56e34eadee9fdf8f91288918d1a01f0e55bdf95df312c5.jpg)

Figure 2 shows that contests involving superstars provide better learning opportunities. On average, one’s submission score in the fourth contest would be 6.2 points higher if she had been constantly competing with superstars than if she had been constantly avoiding superstars. Therefore, competing with superstars helps one learn and improve their skills faster.

## 6.2. Winning-Related Parameter ϕ

We present estimated values of ϕ in Table 5. The coefficients corresponding to the presence of a superstar

Table 4. Estimated Learning-Related Parameters $\sigma ^ { 2 }$

<table><tr><td>Variable</td><td>Notation</td><td>Estimate $^{a}$ </td><td>95% credible interval</td></tr><tr><td>Mean of log individual learning ability</td><td> $\log(\bar{\tau}_{i})$ </td><td>-2.273</td><td>(-2.279,-2.266)</td></tr><tr><td>Variance of log individual learning ability</td><td> $\log(\sigma_{\tau}^{2})$ </td><td>1.648</td><td>(1.643,1.653)</td></tr><tr><td>Log noise level in signal from nonsuperstar</td><td> $\log(\sigma_{ns}^{2})$ </td><td>-0.340</td><td>(-0.351,-0.329)</td></tr><tr><td>Log noise level in signal from superstar</td><td> $\log(\sigma_{ss}^{2})$ </td><td>-1.852</td><td>(-1.854,-1.850)</td></tr><tr><td>Project-associated uncertainty</td><td> $\sigma_{\omega}^{2}$ </td><td>0.0620</td><td>(0.0618,0.0621)</td></tr><tr><td>Number of observations: 5,541</td><td></td><td></td><td></td></tr></table>

<sup>a</sup>Each parameter estimate shows the mean over the parameter draws after the posterior has achieved convergence.

Table 5. Estimated Winning-Related Parameters $\varphi$

<table><tr><td>Variable</td><td>Coefficient notation (win first place)</td><td>Parameter estimates</td><td>Coefficient notation (win first or second place)</td><td>Parameter estimates</td></tr><tr><td>Prize</td><td> $\varphi_1^1$ </td><td>0.029*</td><td> $\varphi_1^2$ </td><td>0.068***</td></tr><tr><td>Superstar</td><td> $\varphi_2^1$ </td><td>-2.441***</td><td> $\varphi_2^2$ </td><td>-1.228***</td></tr><tr><td>Expected solution quality</td><td> $\varphi_3^1$ </td><td>0.110***</td><td> $\varphi_3^2$ </td><td>0.094***</td></tr><tr><td>Intercept</td><td> $\varphi_4^1$ </td><td>-10.020***</td><td> $\varphi_4^2$ </td><td>-7.746***</td></tr><tr><td>Num. of observations</td><td>3,283</td><td></td><td>3,283</td><td></td></tr><tr><td>Log likelihood</td><td>-1,940.2</td><td></td><td>-18,726</td><td></td></tr></table>

$$
^ {*} p <   0. 0 5; ^ {* * *} p <   0. 0 0 1.
$$

are $\varphi _ { 2 } ^ { 1 } = - 2 . 4 4 1$ and $\varphi _ { 2 } ^ { 2 } = - 1 . 2 2 8 ,$ , indicating a strong negative efect of the presence of a superstar opponent on one’s likelihood of winning. As expected, the coefficients of the expected solution quality are positive for winning first place (0.110) and winning the second place (0.094), indicating that as an individual becomes better at producing high-quality solutions, her chances of winning increase. The winning and learning parameters together highlight an interesting tension where participating in projects with superstars leads to higher learning and at the same time significantly decreases the chances of winning.

The estimated contest choice–related parameters are summarized in Table 6. We checked the convergence of the Markov chain at multiple starting points as well as by inspection of time-series plots. We noticed that the chains reached stationarity and common convergence, suggesting that they had “forgotten” the initial values. The Gelman and Rubin (1992) convergence statistics are below 1.05, confirming a convergence. For calculating the posterior mean, we discard the initial 5,000 iterations as burn-in and only use the 5,000 draws after the convergence, that is, after the initial 5,000 iterations.

## 6.3. Contest Choice–Related Parameters Λ

The estimates of parameters that difer across individuals suggest significant heterogeneity in the population. The population mean of the coeficient for expected reward, $\alpha ,$ is 0.458, indicating a positive impact of monetary incentive on an individual’s contest participation decision. The standard deviation of √ $\alpha _ { i }$ is ${ \sqrt { 0 . 0 3 0 } } = 0 . 1 7 3$ , indicating that some individuals value the monetary incentive significantly more compared to others.

The average of the coeficient for the hassle cost associated with the length of the requirement specification document, $\rho _ { 1 } ,$ is <sup>−</sup>1.199, suggesting that as the task requirements increase, the hassle cost increases. To see the impact of the task requirements on an individual’s project choice, let us consider increasing the requirement specification length from five pages (the average length of the requirement specification documents in our sample) to six pages. Then, for a representative coder, with parameters at the population mean, the extra hassle cost is approximately 0.120. This is equivalent to a decrease in her expected payment of approximately USD 25 in terms of her likelihood of participating in a project, everything else being equal.

The negative population mean of the coeficient for prize-associated hassle cost, $\rho _ { 2 } ,$ suggests that contests with high prizes require more efort. This estimate is consistent with our observation that tasks with high prizes generally received few submissions, which may be explained by the high perceived efort/cost that one has to invest to complete the task. The population level of the coeficient for skill level, $\rho _ { 3 } ,$ is negative, suggesting that less skilled individuals will have to pay higher costs to complete a project. Consequently, coders are likely to become more active as they decrease their uncertainties regarding the optimal solution. The fixed cost, $\rho _ { 4 } ,$ is <sup>−</sup>2.344. For a representative coder, having to incur the fixed cost is equivalent to adding $( - 2 . 3 4 4 ) / ( - 1 . 1 9 9 ) = 1 9 . 5$ extra pages to a requirement specification document.

Table 6. Estimated Choice-Related Parameters α and $\rho$

<table><tr><td rowspan="2">Variable</td><td rowspan="2">Coefficient notation</td><td colspan="2"> $Mean^a$ </td><td colspan="2">Variance*</td></tr><tr><td>Estimate</td><td>95% CI</td><td>Estimate</td><td>95% CI</td></tr><tr><td>Discount factor</td><td>β</td><td>0.99 (fixed)</td><td></td><td></td><td></td></tr><tr><td>Expected monetary reward (unit: USD 100)</td><td>α</td><td>0.458</td><td>(0.457,0.460)</td><td>0.030</td><td>(0.0297,0.0303)</td></tr><tr><td>Hassel cost</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Specification length</td><td>ρ1</td><td>-1.199</td><td>(-1.202,-1.195)</td><td>0.405</td><td>(0.4047,0.4053)</td></tr><tr><td>Prize</td><td>ρ2</td><td>-0.372</td><td>(-0.373,-0.371)</td><td>0.024</td><td>(0.0238,0.0241)</td></tr><tr><td>Skill level (uncertainty about optimal solution)</td><td>ρ3</td><td>-2.156</td><td>(-2.161,-2.150)</td><td>1.373</td><td>(1.3642,1.3818)</td></tr><tr><td>Fixed cost</td><td>ρ4</td><td>-2.344</td><td>(-2.347,-2.341)</td><td></td><td></td></tr><tr><td>Number of observations 121,460</td><td></td><td></td><td></td><td></td><td></td></tr></table>

Note. Displayed estimates are the posterior means of the 5,000th<sup>∼</sup>10,000th draws. CI, Credible interval.  
<sup>a</sup>Each individual-level parameter has a distribution over the population of coders. The mean and variance are the mean and variance of the distribution.

(a) Winning versus learning ability  
Figure 3. Individual Learning Ability vs. Monetary Reward Preference  
![](/api/attachments/HQPYDFJA/fulltext/images/a1a3f9a15c2cb7be4b2d9fac568b206774d9028e1a6f915cd2e2705fe7f4400f.jpg)

We next discuss how an individual’s learning ability, log<sup>(</sup>τ<sub>i</sub><sup>)</sup>, is correlated with the weight she gives to monetary reward, $\alpha _ { i } .$ . We provide a scatter plot of $\alpha _ { i }$ and $\log ( \tau _ { i } )$ in Figure 3. The figure reveals a positive correlation<sup>12</sup> between $\alpha _ { i }$ and log<sup>(</sup>τ <sup>)</sup>, suggesting that individuals who have a lower ability to learn tend to highly value monetary reward. Similarly, individuals who have a higher ability to learn tend to value monetary reward less. Figure 4(a) presents the probability of winning a contest versus the learning ability of an individual. We first divide all individuals into four equispaced segments based on their estimated value of log<sup>(</sup>τ <sup>)</sup>. We then calculate the average probability of winning a contest for each segment. As can be seen from Figure 4(a), individuals in the first segment (0–25), which corresponds to the lowest values of $\tau _ { i } ,$ have the highest probability of winning a contest. The probability of winning decreases as τ increases. Similarly, Figure 4(b) shows that individuals who value monetary reward the least are those most likely to win the contest. This finding is quite surprising. The reason driving this result is that to win, an individual needs to have very high skill to receive a high score in the contest. As shown earlier, individuals who have a higher ability to learn and those who participate in projects with superstars are those who would improve their skills the fastest. However, individuals who value monetary reward the most tend to have a very low learning ability and avoid superstar opponents. Thus, such individuals learn very slowly and rarely reach the high level of skill needed to win a contest. In contrast, individuals who value the monetary reward less tend to have a high learning ability and tend to pick contests with superstar opponents more often. As a result, such individuals improve their skills quickly and start winning contests more often.

## 6.4. Disentangling the Cause of Learning

We have argued that individuals learn from other participants in contests through two potential mechanisms—interactions with them during a contest and accessing the solutions of the winners. We do not have data on interactions within a contest or whether individuals accessed and analyzed the winners’ solutions. However, we can still tease these efects out, as these two mechanisms would cause the learning to happen at diferent times. The interactions within a contest would lead to learning during the contest, which would show in performance improvement within the contest. However, the results from the model-free evidence section show that the presence of a superstar in a current project had an insignificant efect on the performance of others in the project. This indicates that the efect of interactions within the project on an individual’s performance does not vary in the presence or absence of a superstar participant.

Figure 4. Impact of Learning Ability and Monetary Reward Preference in Winning a Contest  
![](/api/attachments/HQPYDFJA/fulltext/images/5dd8076fbe1cfc1b42e1c8fb70a625dbd94abe89d18bf4aa22b72b4750101f5a.jpg)

(b) Winning versus monetary reward preference  
![](/api/attachments/HQPYDFJA/fulltext/images/3dde2e3dd14159af128a10fb651143c74bae609035714bba5dcad9364af29fdf.jpg)

Table 7. Setting for the Policy Simulations

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Policy Simulation Settings
Number of projects in each period = 30
 $Prize_{jt}(USD) \sim N(500, 100)$ $SpecLength_{jt}(page) \sim N(5, 1)$ 
Number of individuals = 220
 $\sigma^{2}_{\mu0} = 0.2$ 
Probability of a project involving a superstar = 0.12
</div>

In contrast, the learning from accessing and analyzing the winners’ solutions would lead to learning happening after project completion, and it would show as performance improvement in subsequent projects. Both the model-free results and the structural model results show that individuals’ performance increases in subsequent projects more after they have competed with a superstar in a current project than otherwise. This shows that the learning from superstars occurs primarily through participants’ accessing and analyzing their winning solutions at project completion. Note that individuals learn from all winning solutions; however, they learn more from the winning solutions of superstars than from other solutions. The data show that the winning solutions for projects with superstar participants have higher scores than those for projects without superstar participants.

## 7. Policy Simulation

In this section, we conduct counterfactual analysis to study how a crowdsourcing contest platform such as Topcoder.com can encourage individuals to participate as well as improve the overall quality of delivered solutions. These simulations are conducted under the settings provided in Table 7. For each policy, we solve for the DP problem and then use the DP solution to simulate user behavior over time. Each policy is implemented for 5,000 runs of simulations, and we report the averages of the variables of interest across the 5,000 runs.

## 7.1. Should Topcoder Incentivize Individuals to Compete with Superstars Initially?

Our first policy is motivated by the finding that contests with superstars provide a greater learning opportunity. Hence, we want to see the impact of a policy where Topcoder incentivizes individuals to participate in contests with superstar opponents. However, we allow this incentive for only the first five projects an individual undertakes at Topcoder, because the highest benefit of learning happens when an individual is least skilled. We refer to this policy as “incentive to all.” We next compare the impact of this policy with two alternate policies. In the “current policy,” no incentive is given to participate in contests involving superstar opponents. In the second policy, incentive is given only to individuals who value the monetary reward the most, $\alpha _ { i } > 5 0 t { } \mathrm { h }$ percentile. This policy is motivated by the finding that individuals who value monetary award the most tend to have low learning ability. Because they highly value monetary award, they tend to avoid contests involving superstars. These are the individuals who need the most help improving their skills, and a policy that incentivizes them to participate in contests involving superstars would be useful.

In practice, a crowdsourcing platform could imple ment the incentive policy by giving financial rewards to coders, for each of their first five projects, if the project involves a superstar contestant. The reward could be a monetary reward, such as a cash, another reward, such as platform points. In the simulations, we implemented these policies by giving individual contest participation utilities positive terms on participating in contests where a superstar is involved for their first five projects. To ensure that the total amount of incentive provided in the two policies, incentive to all and incentive to the $\alpha _ { i } > 5 0 t { } \hslash$ percentile, is same, we set the reward for the first policy equal to 0.5 <sup>∗</sup> fixed cost, and that for the second policy to 1.0 <sup>∗</sup> fixed cost. We report the number of submissions and the average expected score over time for the three policies in Figure 5, (a) and (b), respectively. The figure shows that both policies that provide incentives to individuals for participating in contests with superstars outperform the current policy of no incentive, both in terms of number of submissions and the average expected score. More interestingly, the policy that incentivizes individuals who value the monetary reward the highest outperforms the other two policies. This policy targets and helps people who need the incentive the most. The individuals with high values of $\alpha _ { i }$ are those who are inherently slow at learning, and their preference for monetary reward makes them avoid contests with superstars, which also hurts their learning. In contrast, for individuals with low values of $\alpha _ { i } ,$ the presence of a superstar in a contest is not going to deter them much from participating. These individuals also tend to have a high ability to learn and, hence, can increase their skill significantly when participating in projects with superstars. As a result, these individuals are not as averse to participating in projects with superstars without additional incentive as those who highly value monetary reward. The incentive to all policy provides incentive to individuals who do not need it. These policy simulations show that it is pertinent to identify individuals who have high valuation for reward and low learning ability and incentivize them to participate with superstars rather than incentivizing all. In the long run, it is beneficial to have highly skilled individuals who also value monetary reward highly.

Figure 5. Policy Simulation: Impact of Incentives to Compete with Superstars  
![](/api/attachments/HQPYDFJA/fulltext/images/0f5d6891c66c90ffce81c61239a04f340c52b14b2302c7b92c3de9e73d35955e.jpg)

This is because, compared to individuals who value monetary reward less, they have a greater incentive to participate in contests.

## 7.2. Should Topcoder Help Individuals with Low Learning Abilities to Learn?

In this policy simulation, we ask how beneficial it is for Topcoder to help individuals with low learning ability improve their learning. Topcoder can actively reach out to individuals with low learning ability and teach them how to learn when participating in a contest. This could involve teaching them how to ask questions in a contest and how to compare their solutions with the winning solutions. They could also build a community that helps teach these individuals their shortcomings and helps them improve their skills. To implement this strategy in our simulations, we change the parameter representing learning ability, $\tau _ { i } ,$ to population mean of 0.1 for individuals for whom it is greater than 0.1. We compare the performance of this policy with that of the current policy and report the results in Figure $^ { 6 , }$ (a) and (b). As shown in the figure, helping improve the low learning ability of individuals has a significantly positive impact on number of submissions and the average expected score per period. More interestingly, the diference between the performances of the two policies is increasing over time. As discussed earlier, individuals with low learning ability have a high preference for monetary reward. In the current policy, these individuals improve very slowly, and thus their incentive to participate in a contest increases slowly. In contrast, when we help improve the low learning ability, these individuals learn faster, and as their skills increase, their probability of winning contests also increases. As a result, as time goes on, they have even more incentive to participate in contests and provide high-quality solutions.

![](/api/attachments/HQPYDFJA/fulltext/images/2e226395380cc0356c35eb34fea03c1736f1ea665f1d431f5edd3f808a77ec68.jpg)

## 8. Discussion and Conclusion

Crowdsourcing contests are becoming increasingly popular. Platforms such as Topcoder.com allow clients to tap into massive knowledgeable crowds. The projects are hosted in the form of contests where individuals interested in working on a project compete with others. These projects provide the participants a chance of winning the contest and receiving a monetary reward as well as improving their skills. As a project sponsor, one would prefer to have highly skilled individuals compete on her project. At the same time, one would prefer to have many participants compete on a project because the likelihood of achieving an extremely high-quality solution increases with the number of contestants. However, prior theoretical studies in tournament-style competitions as well as empirical studies in crowdsourcing contests indicate that individuals are less likely to participate in contests involving superstars, as their chances of winning decrease significantly in the presence of a superstar opponent. As a result, the presence of a superstar in a contest can lead to a thinly contested competition. Our paper, to the best of our knowledge, presents the first empirical evidence on the positive superstar efect in the context of crowdsourcing contests. Understanding the impact of a superstar on individuals’ contest choice behaviors and on their performances provides managerial implications for both the crowdsourcing platforms and firms that aim to harness the power of crowds in seeking high-quality solutions.

Figure 6. Policy Simulation: Impact of Helping Individuals with Low Learning Ability  
(a) Impact on number of submissions over time  
![](/api/attachments/HQPYDFJA/fulltext/images/d8ef308be838e9f68e281cbe020e277c598e6460af9cdad9f999024e1baf6d92.jpg)

(b) Impact on average expected score over time  
![](/api/attachments/HQPYDFJA/fulltext/images/598cf1d173a49cb7465ae47c62f8fe8361c29de393d7bf467ed884ad02ad26c7.jpg)

In this study, we build a dynamic structural model to analyze the role of superstars in crowdsourcing contests. We apply the ĲC method to obtain the full solution of individuals’ DP problems. The model captures three distinct processes: learning, contest outcome, and choice of contest. The learning and contest outcome processes feed into the contest choice process. The learning process, which is the central theme of this paper, follows an information theoretic Bayesian learning framework. To account for unobserved heterogeneity, we allow the ability to learn and parameters in the utility function to be individual specific. We estimate the model parameters using unique longitudinal data from Topcoder.com. Our main finding highlights a positive spillover efect of a superstar on others, in contrast to only a negative impact, as highlighted by prior literature. Specifically, we show that while an individual’s chances of winning decrease significantly when competing with a superstar, she learns much more from a contest involving a superstar than otherwise. This learning-induced improvement in coders’ skills implies that the individuals who forgo temporary monetary rewards can win significantly more in the future.

We find significant heterogeneity across individuals in terms of their ability to learn and their preference for monetary awards. The individuals with low ability to learn tend to prefer the monetary reward and vice versa. An implication of this relationship is that individuals with low ability to learn will avoid projects with superstars because they mostly care about winning. As a result, individuals who value monetary reward the most end up winning the least because they are unable to increase their skills to a level where they could win. In contrast, individuals who have a high ability to learn value monetary reward less and, as a result, participate in contests involving superstars and learn quickly. They reach the high skills needed to win quickly and start winning contests.

We look into how a platform like Topcoder can encourage more people to participate and improve the average skill level of the participants. Both outcomes are important, as they directly impact the chances of a contest receiving an extremely high-value outcome, which is preferred by clients. Through policy simulations, we show that Topcoder could provide incentives early on to individuals who highly value the monetary reward to participate in projects involving superstars. This policy outperforms the current policy of no incentives and a proposed policy of providing uniform incentives to everyone early on to participate in projects involving superstars. Another policy simulation finds that helping improve the learning ability of individuals who have low learning ability can also significantly increase the number and quality of submissions in a contest. While in both these policies, the incentives are provided upfront only, the impact of these policies persists over a long time. Note that both policies are aimed at helping individuals with a lower ability to learn and who highly value monetary reward to learn faster. Under these policies, these individuals would gain the skills needed to win a contest. When their skills are high enough to win, these individuals will be more likely to participate in contests, as they highly value monetary reward.

Our paper also has certain limitations. First, our model is a partial equilibrium model. While we are studying crowdsourcing contests, we do not model them as dynamic games. We have incorporated the competition in reduced form. We are not aware of any published method that can computationally eficiently solve a dynamic game with more than 200 individuals and several dominating players (superstars). Furthermore, while modeling a game would lead to tighter analysis, it would increase the complexity significantly without providing much new insight. Second, for identification purposes, we excluded individuals who participated in only one contest. Since our model is a learning model, we need at least two data points per individual to measure the extent of learning. Third, because of our limited data set, we assume a common projectassociated noise $\left( \sigma _ { \omega } ^ { 2 } \right)$ in contests. If we could have a data set in which we could allow each category of project to have a category-specific $\sigma _ { \omega } ^ { 2 } ,$ it would be interesting to predict the impact of project-specific characteristics on participants’ responses to a given contest. Fourth, we assume that an individual decides to participate in a project based on whether a superstar is participating in it or not. Sometimes, this information may not be available to an individual when she makes her contest choice decision. Finally, our model focuses on the contest-participation behaviors of coders, while it treats the contest-posting behavior of Topcoder (and of its customers) as exogenous. In fact, it is possible that Topcoder strategically and selectively posts contests in response to the overall performance of participants. Understanding the project-posting behavior and how it corresponds to participants’ behavior may also have managerial implications.

## Endnotes

<sup>1</sup> As of May 2015, over 630,000 developers, data scientists, and designers from more than 200 countries were involved on Topcoder.

<sup>2</sup> In this paper, we will use the words contest and project interchangeably.

<sup>3</sup> The final score refers to the score after the appeal phase. We do not have data about the score before the appeal phase.

<sup>4</sup> An improvement of one is economically quite significant, considering that the distance would add up to six points after six contests. The average distance between a first-place score and a second-place score over all contests in our sample is approximately six points.

<sup>5</sup> The information set $I _ { i j t }$ consists of contest-specific information (i.e., prize, registrants, and presence/absence of superstars) and individual-specific information (i.e., individual’s current state, i.e., her belief about the optimal solution).

<sup>6</sup> We observe in our data that the likelihood of a superstar winning first place is 0.89.

<sup>7</sup> Our data suggest that the specification document itself may not be enough to capture the complexity of a project. The data show a negative correlation between the number of participants and the contest prize, suggesting that the prize should be included when conjecturing about the project’s complexity.

<sup>8</sup> In Equation (17), $\rho _ { 1 i } = \gamma _ { i } \cdot \eta _ { 1 } ; \rho _ { 2 i } = \gamma _ { i } \cdot \eta _ { 2 } ; \rho _ { 3 i } = \gamma _ { i } \cdot \eta _ { 3 } ,$ where η<sub>1</sub>, η , η , are shown in Equation (10) and $\gamma _ { i }$ is shown in Equation (8). We are unable to estimate η and $\gamma _ { i }$ separately, hence we estimate their products $\rho$ as a whole.

<sup>9</sup> The size of the state space grows exponentially with the dimensionality of the state space, which could cause the evaluation of the Bellman operator at each possible point in the state space to be infeasible when solving the infinite horizon DP problem.

<sup>10</sup> The weights depend on how “close” the current parameter draw is to the past parameter draws. The weights are determined by a multivariate Gaussian kernel.

<sup>11</sup> We chose to fix the discount factor rather than identify it, because we are more interested in identifying individuals’ heterogeneous preferences over contest choice. We further tested our estimation with alternative discount factors of <sup>(</sup>0.9, 0.95, 0.975<sup>)</sup> and found the results to be robust to these values.

<sup>12</sup> The correlation coeficient for the two variables is 0.16, with a pvalue of 0.021, suggesting a significant correlation at a 0.05 significance level.

## References

Ackerberg DA (2003) Advertising, learning, and consumer choice in experience goods markets: An empirical examination. Internat. Econom. Rev. 44(3):1007–1040.

Ackerberg DA (2009) A new use of importance sampling to reduce computational burden in simulation estimation. Quant. Marketing Econom. 7(4):343–376.

Aguirregabiria V, Mira P (2007) Sequential estimation of dynamic discrete games. Econometrica 75(1):1–53.

Alchian A (1963) Reliability of progress curves in airframe production. Econometrica 31(4):679–693.

Ales L, Cho S-H, Körpeoğlu E (2017) Optimal award scheme in innovation tournaments. Oper. Res. 65(3):693–702.

Archak N (2010) Money, glory and cheap talk: Analyzing strategic behavior of contestants in simultaneous crowdsourcing contests on TopCoder.com. Proc. 19th Internat. Conf. World Wide Web (Association for Computing Machinery, New York), 21–30.

Archak N, Ghose A (2010) Learning-by-doing and project choice: A dynamic structural model of crowdsourcing. Proc. Internat. Conf. Inform. Systems (ICIS) Thirty First Internat. Conf. Inform. Systems, St. Louis, 239.

Arcidiacono P, Miller RA (2011) Conditional choice probability estimation of dynamic discrete choice models with unobserved heterogeneity. Econometrica 79(6):1823–1867.

Argote L, Epple D (1990) Learning curves in manufacturing. Science 247(4945):920–4.

Baik K (1994) Efort levels in contests with two asymmetric players. Southern Econom. J. 61(2):367–378.

Bajari P, Benkard CL, Levin J (2007) Estimating dynamic models of imperfect competition. Econometric 75(5):1331–1370.

Bellman R (1957) Dynamic Programming (Princeton University Press, Princeton, NJ).

Benkard CL (2000) Learning and forgetting: The dynamics of aircraft production. Amer. Econom. Rev. 90(4):1034–1054.

Bockstedt J, Druehl C, Mishra A (2016) Heterogeneous submission behavior and its implications in innovation contests with public submission. Production Oper. Management 25(7):1157–1176.

Boh WF, Slaughter S, Espinosa A (2007) Learning from experience in software development: A multilevel analysis. Management Sci. 53(8):1315–1331.

Boudreau KJ, Lacetera N, Lakhani KR (2011) Incentives and problem uncertainty in innovation contests: An empirical analysis. Management Sci. 57(5):843–863.

Brown J (2011) Quitters never win: The (adverse) incentive efects of competing with superstars. J. Political Econom. 119(5):982–1013.

Ching A, Imai S, Ishihara M, Jain N (2012) A practitioner’s guide to Bayesian estimation of discrete choice dynamic programming models. Quant. Marketing Econom. 10(2):151–196.

DeGroot MH (1970) Optimal Statistical Decisions (McGraw-Hill, New York).

Delaney PF, Reder LM, Staszewski JJ, Ritter FE (1998) The strategy specific nature of improvement: The power law applies by strategy within task. Psych. Sci. 9(1):1–7.

Erdem T, Keane MP (1996) Decision-making under uncertainty: Capturing dynamic choice processes in turbulent consumer goods markets. Marketing Sci. 15(1):1–20.

Gelman A, Rubin DB (1992) Inference from iterative simulation using multiple sequences. Statist. Sci. 7:457–511.

Gilbride TJ, Allenby GM (2004) A choice model with conjunctive, disjunctive, and compensatory screening rules. Marketing Sci. 23(3):391–406.

Harris C, Vickers J (1985) Perfect equilibrium in a model of a race. Rev. Econom. Stud. 52(2):193–209.

Hatch N, Mowery D (1998) Process innovation and learning by doing in semiconductor manufacturing. Management Sci. 44(11): 1461–1477.

Hotz VJ, Miller RA (1993) Conditional choice probabilities and the estimation of dynamic models. Rev. Econom. Stud. 63(3):497–529.

Howe J (2006) The rise of crowdsourcing. Wired Magazine 14(6):1–4.

Huang Y, Singh PV, Ghose A (2015) A structural model of employee behavioral dynamics in enterprise social media. Management Sci. 61(12):2825–2844.

Huang Y, Singh PV, Mukhopadhyay T (2012) How to design crowdsourcing contest: A structural empirical analysis. Workshop Inform. Systems Econom., Orlando, FL.

Huang Y, Singh PV, Srinivasan K (2014) Crowdsourcing new product ideas under consumer learning. Management Sci. 60(9): 2138–2159.

Imai S, Jain N, Ching A (2009) Bayesian estimation of dynamic discrete choice models. Econometrica 77(6):1865–1899.

Jeppesen LB, Lakhani KR (2010) Marginality and problem-solving efectiveness in broadcast search. Organ. Sci. 21(5):1016–1033.

Jovanovic B, Nyarko Y (1995) A Bayesian learning model fitted to a variety of empirical learning curves. Brookings Papers Econom. Activity: Microeconomics 26:247–305.

Keane M, Wolpin K (1997) The career decisions of young men. J. Political Econom. 105(3):473–522.

Körpeoğlu E, Cho S-H (2018) Incentives in contests with heterogeneous solvers. Management Sci. 64(6):2709–2715.

Liu TX, Yang J, Adamic LA, Chen Y (2014) Crowdsourcing with allpay auctions: A field experiment on Taskcn. Management Sci. 60(8):2020–2037.

Lu Y, Singh P, Sun B (2017) Is a core—Periphery network good for knowledge sharing? A structural model of endogenous network formation on a crowdsourced customer support forum. MIS Quart. 41(2):607–628.

Lucas RE (1976) Econometric policy evaluation: A critique. Carnegie-Rochester Conf. Ser. Public Policy 1(1):19–46.

Magnac T, Thesmar D (2002) Identifying dynamic discrete decision processes. Econometrica 70(2):801–816.

Mele E (2011) Mitigating Topcoder client’s concerns (blog). (November 30), http://elizabethmele.blogspot.com/2011/11/ mitigating-topcoder-clients-concerns.html.

Mitchell MF (2000) The scope and organization of production: Firm dynamics over the learning curve. RAND J. Econom. 31(1): 180–205.

Mukhopadhyay T, Singh PV, Kim SH (2011) Learning curves of agents with diverse skills in information technology-enabled physician referral systems. Inform. Systems Res. 22(3):586–605.

Nti KO (2004) Maximum eforts in contests with asymmetric valuations. Eur. J. Political Econom. 20(4):1059–1066.

Pisano G, Bohmer R, Edmondson A (2001) Organizational differences in rates of learning: Evidence from the adoption of minimally invasive cardiac surgery. Management Sci. 47(6): 752–768.

Reagans R, Argote L, Brooks D (2005) Individual experience and experience working together: Predicting learning rates from knowing who knows what and knowing how to work together. Management Sci. 51(6):869–881.

Rossi PE, Allenby GM, McCulloch RE (2005) Bayesian Statistics and Marketing (John Wiley & Sons, Hoboken, NJ).

Roth Y (2015) The state of crowdsourcing in 2015. Report, eYeka, https://eyeka.pr.co/99215-eyeka-releases-the-state-of-crowd sourcing-in-2015-trend-report.

Rust J (1987) Optimal replacement of GMC bus engines: An empirical model of Harold Zurcher. Econometrica 55(5):999–1033.

Rust J (1994) Structural estimation of Markov decision processes. Engle RF, McFadden DL, eds. Handbook of Econometrics, Vol. 4 (North-Holland, Amsterdam), 3081–3143.

Shingles M, Trichel J (2014) Tech trends 2014: Industrialized crowdsourcing. Deloitte Insights (February 21), https://www2 .deloitte.com/insights/us/en/focus/tech-trends/2014/2014-tech -trends-crowdsourcing.html.

Singh P, Tan Y, Youn N (2011) A hidden Markov model of developer learning dynamics in open source software projects. Inform. Systems Res. 22(4):790–807.

Tanaka R, Ishino K (2012) Testing the incentive efects in tournaments with a superstar. J. Japanese Internat. Econom. 26(3):393–404.

Terwiesch C, Xu Y (2008) Innovation contests, open innovation, and multiagent problem solving. Management Sci. 54(9):1529–1543.

Thurstone LL (1919) The learning curve equation. Psych. Monographs 26(3):1–51.

Zhang J (2010) The sound of silence: Observational learning in the U.S. kidney market. Marketing Sci. 29(2):315–335.
