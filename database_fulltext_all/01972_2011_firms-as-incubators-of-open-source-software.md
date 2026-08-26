---
otero_id: 1972
otero_key: "EACE7BAZ"
title: "Firms as Incubators of Open-Source Software"
authors: "Amit Mehra; Rajiv Dewan; Marshall Freimer"
year: "2011"
journal: "Information Systems Research"
doi: "10.1287/isre.1090.0276"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [202.174.120.2] On: 12 November 2014, At: 23:16 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

## 6SR

![](/api/attachments/EACE7BAZ/fulltext/images/dadb001ef7fcd47d592c750210a3374956bae97abdd60ff16406d2a44f088e0c.jpg)

# Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Firms as Incubators of Open-Source Software

Amit Mehra, Rajiv Dewan, Marshall Freimer,

## To cite this article:

Amit Mehra, Rajiv Dewan, Marshall Freimer, (2011) Firms as Incubators of Open-Source Software. Information Systems Research 22(1):22-38. http://dx.doi.org/10.1287/isre.1090.0276

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2011, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/EACE7BAZ/fulltext/images/9f58289446ed9e2e0326fde96b91f87e589a5ffa3a25179f1696c0f670950223.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Firms as Incubators of Open-Source Software

Amit Mehra

Indian School of Business, Hyderabad 500032, India, amit\_mehra@isb.edu

Rajiv Dewan, Marshall Freimer

William E. Simon School of Business Administration, University of Rochester, Rochester, New York 14627 {dewan@simon.rochester.edu, freimer@simon.rochester.edu}

M<sup>any</sup> <sup>successful</sup> <sup>open-source</sup> <sup>projects</sup> <sup>have</sup> <sup>been</sup> <sup>developed</sup> <sup>by</sup> <sup>programmers</sup> <sup>who</sup> <sup>were</sup> <sup>employed</sup> <sup>by</sup> <sup>firms</sup>but worked on open-source projects on the side because of economic incentives like career improvement from the open-source software and if the productivity of the programmers on these projects improves through learning-by-doing effects. However, the programmers may work more or less on these projects than what is best for the firms. To manage the programmers’ efforts, the firms set appropriate employment policies and incentives. These policies and career concerns then together govern the programmers’ effort allocation between the open-source and proprietary projects. We examine this relationship using a variant of the principal/agent model. We derive and characterize optimal employment contracts and show that firms either offer a bonus for only one of the two projects or do not offer any bonuses. However, if attractive alternate employment opportunities are available, they change their strategy and may offer bonuses for both projects simultaneously.

Key words: open-source software; programmer incentives; programmer compensation; learning by doing; principal/agent; signalling; game theory; business models

History: Sumit Sarkar, Senior Editor; Srinivasan Raghunathan, Associate Editor. This paper was received on May 30, 2007, and was with the authors 10 months for 3 revisions. Published online in Articles in Advance April 14, 2010.

## 1. Introduction

Brian Behlendorf<sup>1</sup> was employed as a Web administrator at Wired<sup>2</sup> when he started to work on the open-source project that became Apache,<sup>3</sup> the Web server that today has almost 70% market share.<sup>4</sup> Similarly, Larry Wall<sup>5</sup> was employed at Unisys<sup>6</sup> as a programmer when he invented the Perl<sup>7</sup> language and wrote an open-source interpreter for it. Today, many consider Perl to be the “glue that holds the Web together.” Many open-source programmers are similar to Behlendorf and Wall in that they have a “day” job while they “moonlight” on open-source projects. Fifty-five percent of programmers in a survey by Lakhani and Wolf (2005) confessed to contributing open-source code on their work time. This is apparently a cause for worry for firms because their employees have extraneous opportunities to contribute time and energy to open-source projects, which is not what they were hired to do.

However, firms like IBM and Sun Microsystems have their programmers contribute code to Eclipse and OpenSolaris open-source projects, respectively. A study conducted by UNU-MERIT (2006) found that contributor firms to open source are significant players in the economy. Their sample of 158 open-source contributing firms indicates that such firms have in total 530,000 employees with a total annual revenue of <sup>E</sup>231.4 billion. Clearly, several firms benefit from the development of certain open-source projects.

To examine the incubation of open-source software in a firm, we first highlight some reasons why it may benefit from open-source activity. A common business model is to sell commercial software complements to a popular open-source software (Fink 2002). One example is IBM, which sells commercial complements to the Eclipse open-source development platform. The success of such an strategy obviously depends upon development of the base open-source software. Consequently, a firm with such a business model may endorse or encourage its employees to work on selected open-source projects.

Learning-by-doing benefits are another reason why a firm may encourage open-source programming activity by its programmers. Writing on the value of human capital, Arrow (1962), Becker (1962), and Blaug (1976) explain that learning takes place in one of two ways: learning by doing and learning by investing in training. Further, the two forms of learning are not substitutes in that they may provide mutually exclusive benefits (Killingsworth 1982). If skill improvement through learning by doing open-source projects is possible, and if this skill improvement helps the programmers do better on the firm’s projects, then the firm will have an incentive to let its programmers do open-source projects.

The learning-by-doing benefit of open-source software has been examined through survey-based papers by Lakhani and Wolf (2005), Hars and Ou (2002), and Hertel et al. (2003). All of these papers find overwhelming evidence that skill building is an important reason why programmers choose to contribute to open-source projects. von Krogh et al. (2003) suggest reasons why learning by doing happens through open-source participation. They observe that peers in the project community, software users, and interested outsiders who are involved in opensource projects help evaluate code submissions, find faults in programming, and often suggest changes to improve the performance of the code. This interactive process improves both the quality of code submission and the overall programming skills of the participants. Industry insiders like Moody (2002), Raymond (2001), and Wayner (2000) also confirm that an active peer review process forms the foundation on which learning by doing from open-source projects is based. Lakhani and von Hippel (2003) report on the motives of this peer review process. Besides helping the community and other forms of altruism, they find that programmers help each other in order to find out about the problems others have faced. This learning helps them to better manage their own software codes. A report compiled for the European Communities (UNU-MERIT 2006) delved deeper into the issues of skill building through open-source projects. It reports that programmers indicated that skills learned from open-source participation can even compensate for lack of formal degrees. In fact, many respondents felt that programming skills are better learned through open-source activities than through formal courses. Thus, we conclude that participation in opensource projects improves programmers’ skills significantly. Programmers with better skills can potentially earn higher compensation. Hence, they have a definite incentive to work on open-source projects.

Firms, too, benefit from improved programmer productivity because their skills improve from learning through working on open-source projects. UNU-MERIT (2006) found that 16% of companies in sectors such as retail, automobile, tourism, and construction allow their programmers to get involved in opensource activities during work hours even though their core business does not leverage the commercial potential of open-source projects. Hence, their motivation to let their programmers devote time in open-source projects must be different from that of firms such as IBM that enjoy direct commercial benefits from opensource projects such as Eclipse. The source of motivation for open-source participation of such diverse firms is also discussed in the UNU-MERIT (2006) study. It reports that employers believe that complex technical, management, and legal skills (writing reusable code, understanding of licensing, coordination of work with other people) are better learned through open-source activities. Tim O’Reilly, one of the experts on open source, exhorted Microsoft to contribute to open-source software because that would foster creative skills and innovative ideas that can be developed commercially.<sup>8</sup> There is sufficient evidence that learning from open-source projects benefits firms because programmers are able to do better jobs on firms’ projects. This is not surprising in light of Schilling et al. (2003) who used an experimental study and Boh et al. (2007) who used empirical data analysis to show that diverse experience in related systems improves programmers’ learning and thereby facilitates increased productivity. Thus, programmers working on commercial video game development may get significant learning benefits from developing open-source games.<sup>9</sup> The value of learning from open source for the firms can also be explained through the value of external knowledge (Menon and Pfeffer 2003). Because outside knowledge is valuable, firms resort to activities such as making acquisitions and hiring outside consultants to get access to such knowledge.

In addition to learning from open-source projects, programmers learn from working on a firm’s projects. Reagans et al. (2005) found that individuals working inside an organization become more productive as they learn from the cumulative experience of others in the organization. Further, Boh et al. (2007) show that programmer learning improves significantly from experience in a specific system. Thus, employed programmers learn from firm-specific learning opportunities that may not be available in open-source communities.

Finally, programming skills can be construed as industry-specific human capital (Neal 1995). Sturman et al. (2008) found that firms with similar requirements value each other’s human capital much more than firms with dissimilar requirements. Hence, any programming skills that programmers learn are useful in improving their productivity in both opensource projects and the firm’s projects to the extent that skill requirements are common across projects. Accordingly, our model incorporates the effect of learning by doing from both open-source and firm projects on programmers’ performance. In this way, we contribute to the literature on human capital formation.

Firms have increasingly adopted organizational structures that encourage multitasking (Lindbeck and Snower 2000, Pautrel 2004, Cartensen 2002, Lindbeck and Snower 1996, Breshnahan et al. 2002, Caroli and Reenen 2001). Sustaining both open- and closedsource activity by the programmers should therefore not be a problem. One more aspect of learning by working on open-source projects is that such training is costless for the firm beyond the opportunity cost of its programmers’ time spent on these projects.

In addition to learning by doing, career incentives also motivate programmers to contribute to opensource projects. Proof of high talent leads to high wages in the labor market (Weiss 1995). For a number of reasons, open-source projects may be better than a firm’s proprietary project for conveying programmers’ talent to the labor market. Anyone can examine the code base of an open-source project and directly evaluate a programmer because open-source projects traditionally document each contribution. In addition, the mere acceptance of a programmer’s contribution to the code base is in itself proof of high-quality work because only contributions that pass the scrutiny of open-source project leaders are included. This kind of evaluation is generally not possible for proprietary projects. Hann et al. (2006) empirically confirm that enhancement of career is one reason why programmers contribute to open-source projects. Their study was based on the analysis of the Apache Web server project and they found that successful open-source participation, measured by a higher rank in the hierarchy of programmers in the project, translated into higher wages.

Extant literature on career concerns examines situations where a firm’s inability to monitor its workers may result in their making suboptimal corporate investment choices (Milbourn et al. 2001) or suboptimal effort choices (Holmstrom 1999, Gibbons and Murphy 1992, Lal and Srinivasan 1993) because of distortions created by career incentive considerations. Hence, firms need to design employment contracts to control these distortions. Because programming is a task that requires significant autonomy and creativity, the firm cannot easily monitor (Kirsch 1996) the effort or attention devoted by programmers to the openand closed-source projects once they are allowed the flexibility to work on both of these. In this situation, absent any performance-contingent payments, programmers will make effort choices in the two projects to maximize the chances of exposing their talent to the labor market (which is the career incentive in this setting). To create incentives for the programmers to make a more appropriate effort choice from a firm’s perspective, the firm must design suitable employment contracts based on performance contingent payments. In this paper, we study the design of such contracts and consequently add to the literature on career concerns.

To summarize this discussion, both the hiring firms and their employed programmers have economic incentives to work on open-source projects. Firms value open-source work because of the strategic value they may derive from these projects and the learning-by-doing benefits to their programmers that helps improve productivity. Programmers value open-source work because of the career incentives and learning-by-doing effects that help them to do a good job and hence get better compensation. However, the incentives of the firm and the programmers are not aligned. Consequently, the programmer may choose to devote effort and attention in two projects that are not optimal from the firm’s perspective. In order to mitigate this problem, a firm may provide incentives to programmers through different bonuses for good performance in the closed- and open-source projects. Such bonuses will then induce programmers to devote effort and attention to projects that are favorable from the firm’s perspective. The study of this incentive problem for the firm forms the central theme of this paper. In order to analyze the different phenomena that arise from open-source participation, we construct a principal-agent model in which a programmer decides on effort allocation between a proprietary closed-source project and an open-source project. In this variant of the principal/agent model, we explicitly include effort division, learning by doing, and career concerns.

We find the marginal effect of effort to be a key determinant of contract choices offered by the firm. For high expected marginal revenues with respect to effort in a closed-source project, the firm offers a contract that provides a bonus for good performance in the closed project only. For low levels of expected marginal revenues, the firm offers a contract that provides a bonus for good performance in the open project only. For moderate levels of expected marginal revenues, the firm does not offer any bonus for either project. If the programmers have alternate employment options, additional compensation may be required to make the firm’s employment as attractive as these alternate opportunities. In such cases, the firm may offer a contract that provides bonuses for both the open and closed projects. The contract in this situation is socially optimal because it maximizes the total value created by the programmer. Other contracts do not have this feature.

We find that the degree to which the proprietary project is open, i.e., the amount of information about individual contributions in proprietary projects that is revealed to the market, may be an important factor that influences the total value created for the firm. An intermediate value of the degree of openness of the proprietary project is sometimes optimal. However, when alternate employment options are good, which requires firms to give bonuses for both the open and closed projects, the impact of this factor on firm value vanishes.

Although we focus on learning by doing and career incentives of programmers as drivers of opensource contributions, alternative explanations that justify programmers’ contributions to open source also exist. Johnson (2002) analyzes open-source contributions in the spirit of the public good literature in economics. Other reasons that have been advanced are the entertainment value of working on what programmers might like doing and the ego gratification when their contributions are recognized in the community of programmers (Lerner and Tirole 2002). Some factors may be stronger than others in driving open-source participation depending on programmer demography. Our work is directly relevant when learning by doing and career incentives are the main forces (these are the likely drivers for fresh programmers). Even when other factors are important, their main effect is that open-source activity may be more attractive for the programmers than what we model. A firm can therefore adjust its contracts by perhaps paying lower bonuses.

In summary, we consider the issue of incentives for programmers to work on open-source programming projects while employed and we analyze the consequent optimal contract choices by hiring firms that may have some strategic value from open-source projects. The next section describes an analytical model for examining these questions. Section 3 provides an analysis of the model and specifies the choice of bonus contracts for a firm. Section 4 examines the impact of the degree of openness of a closed project on firm value. Finally, §5 provides concluding remarks. All lemmas and proofs of the propositions are in the appendix.

## 2. Model

## 2.1. The Market for Software Development

The labor market for programmers consists of several firms. Each firm hires programmers to do programming projects at the beginning of each of an infinite succession of time periods. A programming project is an individual task that is assigned to a programmer and the programmer is solely responsible for creating the output to complete that task. We now provide some details about both sides of this market: firms and programmers.

2.1.1. Programmers. A programmer may be either “talented” or “untalented.” To simplify the information structure of the problem, we assume that success, or good outcome, of a project is only possible if the programmer is talented. This is not an unreasonable assumption for the software industry; software industry experts have pointed out that the productivity of talented programmers is much higher than that of average programmers.<sup>10</sup> Further evidence comes from a study in Goleman (1998), where it was found that the top 1% of programmers were 1,272% more efficient than the average. Thus, it can be reasonably expected that in a given time period a talented programmer can achieve a better output compared to an average programmer.

Information on the talent of a programmer may or may not be known and depends on how long the programmer has been in the programming industry. A programmer who has freshly entered the labor market after completing formal education is termed a “rookie.” Although rookie programmers know their own capabilities, they are relatively unaware of industry requirements. Therefore, they are unable to ascertain how well their capabilities are suited for the requirements of the industry. In other words, their information set is insufficient to let them conclude whether they are talented or not with certainty. Similarly, though a hiring firm in the labor market is informed about the industry requirements, it has little information about the capabilities of an individual rookie programmer. Thus, the firm is also unable to conclude how well a particular individual is likely to perform. Because of these information asymmetries, we assume that neither the rookie programmers nor the labor market know whether a particular rookie is talented or not. We assume that there is a common prior probability m that a rookie programmer may be talented. Analysis of a labor market with a similar description was made earlier by Holmstrom (1999), where he studied how the incentives of workers to exert effort change along their career paths. We further assume that a rookie programmer when employed can create a minimum value of g per period (i.e., both talented and untalented programmers create this value). Furthermore, the market wage for rookies is normalized to zero.

As rookie programmers are used and their contributions evaluated, the hiring firm, the programmers themselves, and other firms in the market find out the talent of the programmers. The market wage for programmers who are known to be talented in the labor market is $w _ { t } > 0$ . Thus, if rookie programmers prove themselves to be talented, then their wages increase from zero to $w _ { t } .$ . This wage premium provides a career incentive to rookies to convey their talents to the labor market.

2.1.2. Firms. A firm can get an expected value of $w _ { t }$ by employing a talented programmer for one period.<sup>11</sup> However, if such a programmer is employed in low value projects, the value generated may be lower than w .

At the beginning of the game, the focus firm has a commercial closed project and a synergistic open-source project with learning-by-doing benefits between the two projects. A successful outcome (meaning that the program provides all the userdemanded functionality, does so without using too many computing resources, and is easy to maintain) in the open and closed projects creates a value $g _ { o }$ and ${ { g } _ { c } } ,$ respectively. These values are over and above the minimum value $g$ that is created by employing any programmer. We are interested in cases when $^ { g , }$ g<sub>o</sub>, and $g _ { c }$ are not so large that the firm will directly hire a programmer with proven talent at the high market wage (w ). We instead examine the case when these values are more moderate so that the firm will take a chance on hiring a rookie for its projects.

## 2.2. Revelation of Programmer Talent to the Market

The revelation of a rookie programmer’s talent depends on two events: success in open and closed projects and observation of this success by the market. Here, we discuss the probabilities of both these events.

2.2.1. Probabilities of Success in Open and Closed Projects. The probabilities of different outcomes of the two projects conditional on having a talented programmer are displayed in Table 1. A highly successful outcome is classified as good and the other outcome as bad.

Recall that, previously, we have assumed that the probability of success is zero in all projects for untalented programmers.

Table 1 Joint and Marginal Probabilities of Outcomes for a Talented Programmer

<table><tr><td></td><td>Good in open</td><td>Bad in open</td><td>Marginal probability</td></tr><tr><td>Good in closed</td><td> $p_{gg}$ </td><td> $p_{gb}$ </td><td> $p_c = p_{gg} + p_{gb}$ </td></tr><tr><td>Bad in closed</td><td> $p_{bg}$ </td><td> $p_{bb}$ </td><td> $1 - p_c$ </td></tr><tr><td>Marginal probability</td><td> $p_o = p_{gg} + p_{bg}$ </td><td> $1 - p_o$ </td><td></td></tr></table>

All of these joint and marginal probabilities are functions of effort division, with fraction x of the effort being devoted to the closed-source project and ${ 1 - x }$ of the effort to the open-source project.<sup>12</sup> As discussed in the introduction, we assume that this effort division is made by the programmer and is neither observable nor contractible by the firm in its employment contract with the programmer.

The marginal probabilities $( p _ { c }$ and $p _ { o } )$ are dependent on both the effort division x and learning by doing from the two projects. As the effort in a project increases, the positive impact of effort and learning by doing from this project on its own marginal probability of success reduces because of diminishing returns. Further, increase in effort in this project implies reduction of effort in the other project. Consequently, there is a negative impact on the marginal probability of success of this project because of a reduction in learning by doing from the other project. Because of the diminishing returns phenomenon, this negative impact increases as effort in the other project reduces. If this negative impact is strong enough, the slope of the marginal probability of success will eventually become negative. Thus, this probability will be at its maximum at intermediate effort levels in such situations.

Similar to the above, for intermediate values of $x ,$ the probability of failure in both projects $( p _ { b b } )$ will be low because of better learning opportunities and balanced effort in both projects. At more extreme values of $x ,$ the imbalance in learning opportunities and effort division will cause an increase in this probability.

We also assume that the two projects are sufficiently differentiated and that it is not the case that learning benefits from one project reduce effort requirement very significantly in the other. Such a situation may indeed happen ${ \dot { \operatorname { i f } } } ,$ for example, a piece of code developed for one project can be directly reused in the other project with minimal changes. The firm may lose valuable intellectual property if the code developed for closed-source project is reused in the opensource project. On the other hand, legal issues from the open-source license would arise if the code developed for the open-source project is reused in the closed-source project without making its source code open. We do not consider such situations because firms are unlikely to have programmers do both projects if this is the case. Given this, the marginal probability of success in a project would depend more on effort in that project rather than on effort in the other project. Consequently, this probability would be maximized at an effort division that favors that particular project.

Putting together the above, we state the following assumption.

Assumption 1. Marginal probabilities of success $p _ { c }$ and $p _ { o } f o r$ the closed- and open-source projects, respectively, and the probability of obtaining any success $p _ { g g } + p _ { g b } +$ $p _ { b g } = 1 - p _ { b b }$ are doubly differentiable w.r.t. x and strictly concave, i.e., $p _ { c } ^ { \prime \prime } , p _ { o } ^ { \prime \prime } < 0 .$ , and $p _ { b b } ^ { \prime \prime } > 0 ~ f o r ~ 0 \leq x \leq 1$ . Further, probabilities $p _ { c }$ and $p _ { o }$ are maximized at $x _ { c }$ and $\scriptstyle { \boldsymbol { x } } _ { o } ,$ respectively, such that $0 < x _ { o } < x _ { c } < 1$

One implication of Assumption 1 is that $p _ { c } ^ { \prime } > 0$ $\forall x < x _ { c }$ and $p _ { c } ^ { \prime } < 0 \ \forall x > x _ { c }$ . Similarly, $p _ { o } ^ { \prime } > 0 \ \forall x < x _ { o }$ and $p _ { o } ^ { \prime } < 0 \forall x > x _ { o }$

Our second assumption about probabilities requires that an increase in effort on the closed project increases $p _ { g b }$ and decreases $p _ { b g }$ . Such behavior is expected when effort is the only driver of project success. This assumption says that the moderating effect of learning by doing on probabilities is not too significant. Together, Assumptions 1 and 2 implicitly state lower and upper bounds of the impact of learning by doing.

Assumption 2. $p _ { g b } ^ { \prime } ( x ) \ > \ 0$ and $p _ { b g } ^ { \prime } ( x ) \ < \ 0$ for $0 < x < 1$

2.2.2. Difference in Observability of Outcomes of Open- and Closed-Source Projects. Open- and closed-source projects differ in the information they make available to the labor market. Consequently, there is a difference in what the labor market finds out about programmers’ talent from observing the closed and open projects.

The outcome in the open-source project is visible to all. This is because the open-source community has a tradition in which the contributions of individual programmers are explicitly recognized. For example, the website http://sourceforge.net/project/ memberlist.php?group\_id=93438 lists the programmers who have contributed to an open-source drawing tool called Inkscape, which is being developed as an open-source alternative to Adobe Illustrator and Corel Draw, etc. It is possible to get information about individual contributions from facilities like concurrent versions system/subversion (CVS/SVN) commits provided on the project Web pages. Further, as the community itself selects code fragments to be included in the released product, the acceptance of a contribution is in itself revealing of a programmer’s talent. Thus, the labor market gets a clear insight into the contribution made by each programmer.

Closed source, by its very nature, is much less revealing. Not only is the code not available for evaluation, the individual contribution is rarely made public. To focus on this difference between openand closed-source projects, we assume that the outcome of the open-source project, success or failure, is observed publicly by all. In contrast, we assume that success in a closed-source project is imperfectly and asymmetrically visible. Although the hiring firm and the programmer always observe the outcome of the closed-source project, the market gets to see the successful outcome of this project with probability p.

At this point, we define a useful class of probability functions as follows.

Definition 1. $p _ { r } ( z ) = p _ { o } + z p _ { g b } \ \forall z \in [ 0 , 1 ]$

From Assumptions 1 and 2, it is easy to see that $p _ { r } ( z )$ is concave<sup>13</sup> and that $p _ { r } ( z )$ is maximized at $x _ { r } ( z )$ such that $x _ { o } < x _ { r } ( z ) < x _ { c } . ^ { 1 4 }$

Using $p _ { r } ( z ) _ { . }$ , the probability that a talented rookie programmer is revealed to be so to the market is

$$
p _ {t} = p _ {r} (p).
$$

Consider the following example to illustrate all the probabilities discussed above.

Example 1. Let $\pi ( x ) = e x$ (for $0 \leq e \leq 1$ and $0 \leq x \leq 1 )$ be the probability of success in any one project if proportion x of time is spent on it and there is no learning value of one project for the other.

Suppose that a talented programmer spends effort x on the closed project and thereby spends leftover effort 1 − x on the open project. The joint probabilities of the various outcomes for a talented programmer, taking into account the correlation between outcomes because of the learning effect, are:

Prob[good in closed, good in open]

$$
= p _ {g g} (x) = (1 + 2 d) \pi (x) \pi (1 - x),
$$

Prob[good in closed, bad in open]

$$
= p _ {g b} (x) = (1 - d) \pi (x) (1 - \pi (1 - x)),
$$

$^ { 1 3 } p _ { o } ^ { \prime \prime } + z p _ { g b } ^ { \prime \prime } = z ( p _ { g g } ^ { \prime \prime } + p _ { b g } ^ { \prime \prime } + p _ { g b } ^ { \prime \prime } ) + ( 1 - z ) p _ { o } ^ { \prime \prime } < 0$ because coefficients of z and $1 - z$ are both negative.

$^ { 1 4 } p _ { r } ^ { \prime } ( z ) | _ { x = x _ { o } } = p _ { o } ^ { \prime } | _ { x = x _ { o } } + z p _ { g b } ^ { \prime } | _ { x = x _ { o } } = z p _ { g b } ^ { \prime } | _ { x = x _ { o } } > 0$ because $p _ { o } ^ { \prime } | _ { x = x _ { o } } = 0$ and $p _ { g b } ^ { \prime } \big | _ { x = x _ { o } } > 0$ from Assumptions 1 and 2, respectively. Further, $p _ { r } ^ { \prime } ( z ) | _ { x = x _ { c } } ^ { \sim } = - ( 1 - z ) p _ { g b } ^ { \prime } | _ { x = x _ { c } } + p _ { b g } ^ { \prime } | _ { x = x _ { c } } < 0$ because $p _ { b g } ^ { \prime } \rvert _ { x = x _ { c } } < 0$ and $p _ { g b } ^ { \prime } \big | _ { x = x _ { c } } > 0$ from Assumption 2 and $\big { p } _ { c } ^ { \prime } | _ { x = x _ { c } } = 0$ from Assumption 1. These imply that $p _ { r } ( z )$ is maximized at some $x _ { r } ( z )$ , where $x _ { o } <$ $x _ { r } ( z ) < x _ { c }$

Figure 1 The Marginal Probabilities  
![](/api/attachments/EACE7BAZ/fulltext/images/aac8d83387dae1d89a3283e7ee54929ea04cf70723fd3785786b10182516e42f.jpg)  
Prob[bad in closed, good in open]

$$
= p _ {b g} (x) = (1 - d) (1 - \pi (x)) \pi (1 - x),
$$

$$
= p _ {b b} (x) = 1 - p _ {g g} (x) - p _ {g b} (x) - p _ {b g} (x).
$$

Note that the parameter d captures the correlation between the probabilities because of the learning effect and $d = 0$ corresponds to the no-learning case. Further, the probabilities make sense only when $d < 1$ . Using the definitions above, we can easily work out the marginal probabilities of success $p _ { c }$ and $p _ { o } .$ It is easy to verify that these probabilities agree with Assumption 2 and satisfy Assumption 1 $\mathrm { i } \widetilde { \mathrm { f } } \ 1 / ( 1 + 3 e ) \le d \le \dot { 1 }$ . Thus, as explained earlier, the assumptions put bounds on the extent of learning effects.

The marginal probabilities $p _ { c }$ and $p _ { o }$ and the probability of revelation of talent $p _ { t }$ are illustrated in Figure 1 for $d = 0 . 6 , e = 0 . 5 ,$ , and $p = 0 . 5$

## 2.3. Surplus for Rookie Programmers and the Firm

Recall that we are considering situations where the firm initially hires a rookie programmer for a single period for doing open- and closed-source projects. The rookie may be rehired in future either by this firm or by other market firms based on his or her performance. In this section, we focus on getting the expressions for the total surpluses of the rookie and the firm. In writing these surpluses, we use  as the discount rate per period. At this point, we introduce Table 2 to summarize various symbols and their definitions.

2.3.1. Surplus for Rookie Programmers. Suppose that the firm offers a contract that provides nonnegative bonuses $w _ { c }$ and $w _ { o }$ for good outcomes in the closed- and open-source projects, respectively, to a rookie in the first period. The expected bonus for the rookie in this period is

$$
E W = m p _ {c} w _ {c} + m p _ {o} w _ {o}.\tag{1}
$$

Table 2 Parameter and Variable Definitions

<table><tr><td>Symbol</td><td>Definition</td></tr><tr><td> $x$ </td><td>Fraction of effort in the closed-source or proprietary project</td></tr><tr><td> $x_c$ </td><td>Fraction of effort in the closed project at which  $p_c$  is maximized</td></tr><tr><td> $x_o$ </td><td>Fraction of effort in the closed project at which  $p_o$  is maximized</td></tr><tr><td> $w_c$ </td><td>Bonus for success in the proprietary project</td></tr><tr><td> $w_o$ </td><td>Bonus for success in the open-source project</td></tr><tr><td> $m$ </td><td>Probability that a rookie programmer is talented</td></tr><tr><td> $g$ </td><td>Minimum value created by any programmer in one period</td></tr><tr><td> $g_c$ </td><td>Value created by success in the firm&#x27;s first-period proprietary project</td></tr><tr><td> $g_o$ </td><td>Value created by success in the first-period open-source project</td></tr><tr><td> $w_t$ </td><td>Maximum expected value created by a talented programmer in one period, market wage of talented programmers</td></tr><tr><td> $u$ </td><td>Minimum utility for a programmer to accept a firm&#x27;s employment</td></tr><tr><td> $p_o$ </td><td>Marginal probability of success in the open project</td></tr><tr><td> $p_c$ </td><td>Marginal probability of success in the closed project</td></tr><tr><td> $p_t$ </td><td>Probability that a talented rookie programmer is revealed to be talented in the market</td></tr><tr><td> $p$ </td><td>Probability that the market observes the successful outcome of the closed project</td></tr><tr><td> $EW$ </td><td>Expected bonus a the rookie in period one</td></tr><tr><td> $ES$ </td><td>Expected surplus a the rookie programmer</td></tr><tr><td> $EV$ </td><td>Expected value for the firm</td></tr><tr><td> $EV_t$ </td><td>Total value created for the firm and the programmer</td></tr><tr><td> $MR$ </td><td>Marginal revenue for the firm as a function of  $x$ </td></tr><tr><td> $\delta$ </td><td>Discount rate per period</td></tr></table>

The rookie programmer’s future employment opportunities are contingent on the outcomes in the first period because these outcomes may reveal whether the programmer is talented or not publicly (information becomes available to programmer, firstperiod hiring firm, and all market firms) or privately (information becomes available to programmer and first-period hiring firm; market firms are excluded). The complete tree depicting the events and decisions is shown in Figure 2. The events are noted at each branch and the probabilities of the events are noted in parenthesis. The future surpluses earned by the programmer are noted at the culmination of a sequence of events. If a particular sequence of events is impossible (probability zero event), then the surpluses for that sequence are omitted. The circle in Figure 2 depicts a decision node; the programmer’s decision at this point influences future surpluses.

If a rookie is untalented, she fails in producing a good outcome in both projects. Further, even if the rookie is talented, she fails in producing a good outcome in both projects with probability $p _ { b b }$ Thus, a rookie who produced a bad outcome in both projects can only be talented with probability $m p _ { b b } / ( ( 1 - m ) + m p _ { b b } )$ . One can easily show that $m p _ { b b } / ( ( 1 - m ) + m p _ { b b } ) < m$ . A fresh rookie has a greater probability of being talented than a rookie who failed in producing a good outcome in both projects. Further, the market wage of rookies is zero. Thus, all firms will always prefer to use fresh rookies over failed rookies. Because of this, failed rookies will have no future earning potential. Accordingly, the lowest two branches in the event tree in Figure 2 show future earnings of zero.

Figure 2 Future Surplus for Rookie Programmer  
![](/api/attachments/EACE7BAZ/fulltext/images/03255ceb63b15e7284ba0e42c7426741aa5441b3eef6d80475ec64203ac8afbe.jpg)

If the rookie programmer is talented and has succeeded in one or more projects, and if her success is revealed to the labor market, then she can find employment in all subsequent periods with a wage of $w _ { t }$ in each period. Thus, the present value of the surplus is $\delta w _ { t } \mathrm { + } \delta ^ { 2 } w _ { t } \mathrm { + } \delta ^ { 3 } w _ { t } \mathrm { + \cdots }$ . This surplus is earned with probability $m ( p _ { g g } + p _ { b g } + p p _ { g b } ) = m p _ { t }$

An interesting situation arises when a talented programmer succeeds only in the closed project and this information does not become public. Will the market firms be interested in hiring such a programmer? Note that the market firms cannot distinguish between these programmers and those who genuinely failed in producing a good outcome in both projects. Thus, if the market firms pick a programmer from this pool, the probability that this programmer is talented is $( m ( \bar { 1 } - p ) p _ { g b } + m p _ { b b } ) / ( ( 1 - \bar { m } ) \bar { + } m ( 1 - p ) p _ { g b } + m p _ { b b } )$ . It is easy to show that $( m ( 1 - p ) p _ { g b } + m p _ { b b } ) / ( ( 1 - m ) +$ $m ( \bar { 1 } - p ) p _ { g b } + m p _ { b b } ) < m . ^ { 1 5 }$ The market firms can get talented programmers from the fresh rookie pool with a higher probability at zero wages. Therefore, these firms will never give an offer to such failed programmers. In other words, the outside opportunities for these programmers are zero in this period. As a result, these programmers will take an offer from the firstperiod hiring firm even at zero wages. Note that failure to publicly show a successful output results in a penalty because such programmers are reemployed at zero wages while their peers who could publicly show a successful output are reemployed at $w _ { t }$ . This is not a permanent problem because the act of rehiring by the first-period firm in the subsequent period informs the rest of the market firms that such a programmer was indeed talented. Therefore, the programmer is recognized as a talented programmer after a lag of one period and she then starts to earn the wage $w _ { t }$ per period, implying that the present value of future earnings are $0 \dot { + } \dot { \delta } ^ { 2 } w _ { t } + \delta ^ { 3 } w _ { t } + \dot { \cdot } \cdot \cdot$

<sup>15</sup> The inequality can be rewritten as m $( 1 - p ) p _ { g b } + m p _ { b b } < m ( 1 -$ m $+ m ^ { 2 } ( ( 1 - p ) p _ { g b } + p _ { b b } ) \Longrightarrow ( 1 - p ) p _ { g b } + p _ { b b } < 1 ,$ , which must be true because 0 < 1 $\begin{array} { r } { \dot { } p < 1 , 0 \le p _ { g b } \le 1 , 0 \le p _ { b b } \le 1 , } \end{array}$ , and $0 \leq p _ { g b } + p _ { b b } \leq 1$

According to this discussion, the programmer’s expected surplus from the current and all future periods is

$$
\begin{array}{c} E S = E W + m p _ {t} (\delta w _ {t} + \delta^ {2} w _ {t} + \dots) + \\ m (1 - p) p _ {g b} (0 + \delta^ {2} w _ {t} + \delta^ {3} w _ {t} + \dots) \\ = E W + m p _ {t} \frac {\delta w _ {t}}{1 - \delta} + m (1 - p) p _ {g b} \frac {\delta^ {2} w _ {t}}{1 - \delta}. \end{array}\tag{2}
$$

Examining Equation (2), we note that the market wage $w _ { t }$ for talented programmers sets up an incentive for the programmers to make effort choices in the current period to increase the chance of revealing their talent in future. This career concern is similar to that in Holmstrom (1999).

2.3.2. Firm Surplus. The expected value of the first period projects to the firm for which it hires rookies is $g + m p _ { c } g _ { c } + m p _ { o } g _ { o }$ . This is not the only value created for the firm when it rehires programmers in subsequent periods. With probability $m ( 1 - p ) p _ { g b }$ , the firm will be in a situation where it knows that its current employees are talented but the labor market does not. As pointed out in the last section, this allows the firm to rehire such programmers at zero wages for the subsequent period. In order to induce these programmers to work and avoid shirking, the firm must give a bonus $\epsilon > 0$ that is contingent on a successful outcome in this period. Even if  is made arbitrarily small, the programmers maximize their surplus by maximizing the chances of producing a successful outcome. Thus, shirking can be avoided at negligible cost. Consequently, the firm gets an expected rent of $m ( 1 - p ) p _ { g b } w _ { t }$ in the next period. Putting these terms together and considering the wage paid to the programmer, we get the total expected surplus, in net present value, for the firm by hiring a rookie programmer to be

$$
E V = g + m p _ {c} g _ {c} + m p _ {o} g _ {o} + m (1 - p) p _ {g b} \delta w _ {t} - E W.\tag{3}
$$

Assuming that $m > 0 ,$ , we drop it from expressions of $E S , E W ,$ , and EV in the following discussion because it multiplies all the terms in these expressions except for $g$ in EV . We scale g appropriately.

## 3. Analysis

The firm wants to maximize its surplus in the contract that it signs with a rookie programmer. Therefore, the firm’s problem is

$$
\max _ {w _ {c}, w _ {o}} E V (x ^ {*})
$$

subject to $x ^ { \ast } \in$ arg max ESx x 0≤x≤1

$$
(i n c e n t i v e \quad c o m p a t i b i l i t y (I C) \text { constraint })\tag{4}
$$

$$
E S (x ^ {*}) \geq u
$$

(individual rationality (IR) constraint)

$$
w _ {c}, w _ {o} \geq 0.\tag{5}
$$

The individual rationality (IR) constraint (5) expresses the requirement that the programmer get a minimum utility u from employment with the firm. Note that, with the career concerns, this is not just a constraint on wages and bonuses but also the value from future prospects.

The incentive compatibility (IC) constraint (4) results from the assumption that given the terms of the employment contract, the programmer picks the effort division that maximizes his personal expected surplus. Replacing (4) by its first-order condition, we have

$$
\begin{array}{l} \frac {d E S}{d x} = p _ {c} ^ {\prime} w _ {c} + p _ {o} ^ {\prime} w _ {o} \\ \qquad + (p _ {t} ^ {\prime} + (1 - p) p _ {g b} ^ {\prime} \delta) \frac {\delta w _ {t}}{1 - \delta} = 0 \quad (\mathrm{IC}). \end{array}\tag{6}
$$

In the appendix, we state and prove three lemmas that characterize the problem. In Lemma 1, we show that the effort division $x ^ { * }$ chosen by the programmer to maximize her own surplus lies between $x _ { o }$ and $x _ { c } .$ Thus, $x ^ { * }$ has an internal value and the first-order condition makes sense. If an extremely large bonus is offered for the closed project, then the programmer will effectively maximize $p _ { c . }$ , which occurs at $x _ { c }$ . Correspondingly, if the firm offers an extremely large bonus for the open project, the worker will maximize ${ p } _ { o } ,$ which occurs at $x _ { o } .$ . When no bonuses are given, Equation (6) will be satisfied when $( p _ { t } ^ { \prime } + ( 1 - p ) \bar { p _ { g b } ^ { \prime } } \delta ) = 0 ,$ implying that the effort choice is such that the expression $p _ { t } + ( 1 - p ) p _ { g b } ^ { \prime } \delta$ is maximized.<sup>16</sup> By doing this, the programmer maximizes the expected payoffs from the revelation of talent, which is the only payoff in absence of any incentives through bonuses. The optimal effort division for the firm depends upon the values of project successes $g _ { c }$ and $g _ { o } .$ Thus, the effort division chosen by the programmer in absence of bonuses and the one that is optimal for the firm may be quite different. The firm then provides bonuses to mitigate this discrepancy.

For the effort divisions that satisfy the incentive compatibility condition, i.e., for $x _ { o } < x < x _ { c }$ , we note that $p _ { o }$ is decreasing and $p _ { c }$ is increasing in x. As a result, increasing $w _ { c }$ increases the effort in the closed project while increasing $w _ { o }$ decreases effort in the closed project. This is proven in Lemma 2.

As a last observation, we note in Lemma 3 that when the individual rationality constraint is not binding, then the firm will not offer a positive bonus for both the open- and closed-source projects simultaneously in a particular contract. The intuition for this result follows from the fact that $w _ { c }$ and $w _ { o }$ have opposite effects on the effort division chosen by the programmer. Having them both positive adds to the expected wage but has no benefit in aligning the incentives of the programmer and the firm.

In order to characterize the optimal bonus choices by the firm, we define MR as the marginal revenue for the firm as a function of x:

$$
M R = g _ {c} p _ {c} ^ {\prime} + g _ {o} p _ {o} ^ {\prime} + (1 - p) \delta w _ {t} p _ {g b} ^ {\prime}.\tag{7}
$$

Proposition 1 lays down the optimal choice of bonuses in terms of the marginal value calculated at the effort division chosen by the programmer when the individual rationality constraint is trivially satisfied, for example, when $u = 0$

Proposition 1. If the IR constraint is not binding, then the choice $o f$ bonuses that locally maximize the firm’s value is reflected in the following menu:

Case I. $w _ { c } ^ { * } = 0$ and $w _ { o } ^ { * } = ( M R ^ { * } + A ^ { * } ) / ( p _ { o } ^ { \prime * } - p _ { o } ^ { * } p _ { o } ^ { \prime \prime * } / p _ { o } ^ { \prime * } ) .$ where $x ^ { * }$ is a solution to

$$
\frac {M R ^ {*} + A ^ {*}}{p _ {o} ^ {\prime *} - p _ {o} ^ {*} p _ {o} ^ {\prime \prime *} / p _ {o} ^ {\prime *}} = - \frac {(p _ {t} ^ {\prime *} + (1 - p) p _ {g b} ^ {\prime *} \delta) (\delta w _ {t} / (1 - \delta))}{p _ {o} ^ {\prime *}} i f f M R ^ {*} <   - A ^ {*}.
$$

Case II. $w _ { c } ^ { * } = ( M R ^ { * } - B ^ { * } ) / ( p _ { c } ^ { \prime * } - p _ { c } ^ { * } p _ { c } ^ { \prime \prime * } / p _ { c } ^ { \prime * } )$ and ${ w _ { o } ^ { * } } = 0 .$ where $x ^ { * }$ is a solution to

$$
\frac {M R ^ {*} - B ^ {*}}{p _ {c} ^ {\prime *} - p _ {c} ^ {*} p _ {c} ^ {\prime \prime *} / p _ {c} ^ {\prime *}} = - \frac {(p _ {t} ^ {\prime *} + (1 - p) p _ {g b} ^ {\prime *} \delta) (\delta w _ {t} / (1 - \delta))}{p _ {c} ^ {\prime *}}
$$

$$
i f f B ^ {*} <   M R ^ {*}.
$$

Case III. $w _ { c } ^ { * } = 0$ and $w _ { o } ^ { * } = 0$ when $x ^ { * }$ is a solution to $p _ { t } ^ { \prime * } + ( 1 - p ) p _ { g b } ^ { \prime * } \delta = 0 \ i f f - \check { A } ^ { * } \leq M R ^ { * } \leq B ^ { * }$ where

$$
\begin{array}{r} A = \frac {p _ {o}}{p _ {o} ^ {\prime}} \frac {\delta}{1 - \delta} w _ {t} (p _ {t} ^ {\prime \prime} + (1 - p) \delta p _ {g b} ^ {\prime \prime}) \\ B = - \frac {p _ {c}}{p _ {c} ^ {\prime}} \frac {\delta}{1 - \delta} w _ {t} (p _ {t} ^ {\prime \prime} + (1 - p) \delta p _ {g b} ^ {\prime \prime}) \\ M R = g _ {c} p _ {c} ^ {\prime} + g _ {o} p _ {o} ^ {\prime} + (1 - p) \delta w _ {t} p _ {g b} ^ {\prime} \end{array}
$$

and the starred terms indicate that the corresponding quantity is evaluated at $x ^ { * } ,$ , the optimal effort division chosen by the programmer.

The proof of Proposition 1 is presented in the appendix. Because the cases depicted in Proposition 1 represent local maximums, it may be possible for more than one case to be simultaneously satisfied.

Figure 3 Illustrating Proposition 1: Bonuses with IR Constraint Not Binding  
![](/api/attachments/EACE7BAZ/fulltext/images/56b5bb974f88bd8a8fe28d42b651d55c00baa209823b44df48e900ca837d2f83.jpg)

In such situations, the firm will pick the solution that provides the maximum $E V , \mathrm { i . e . , }$ the one that is globally optimal. The main points conveyed through Proposition 1 are that the firm will either pay no bonuses or pay a bonus for only one of the projects. Further, a positive bonus for the closed project is likely to be picked for large values of $M R ^ { * }$ , and the same for the open project for small values of MR<sup>∗</sup>. No bonuses are likely when $M R ^ { * }$ has intermediate values. This is illustrated in Figure 3. To obtain Figure 3, we use the probability functions exhibited in Example 1 and numerically solve the firm’s problem with the parameter values $\delta = 0 . 2 , ~ d = 0 . 5 , ~ \bar { e } = 0 . 9 , ~ g = 1$ $g _ { o } = 4 , p = 0 . 5 , w _ { t } = 2 8 , u = 0 . \mathrm { A l s o } , g _ { c }$ is varied from 10 to 20. The corresponding optimal bonuses are plotted against $M R ^ { * }$ . The bonus for the open project $( w _ { o } ^ { * } )$ is plotted as a dashed line whereas the bonus for the closed project $( w _ { c } ^ { * } )$ is plotted as a solid line. Note that for $M R ^ { * } < 9 . 6 ,$ , both $\boldsymbol { w } _ { o } ^ { * }$ and $\boldsymbol { w } _ { c } ^ { * }$ are zero. Once $M R ^ { * } > 9 . 6 , \ w _ { c } ^ { * } > 0$ while ${ w _ { o } ^ { * } } = 0$ . Thus, Figure 3 illustrates Cases II and III of Proposition 1. To relate the results of Proposition 1 to the primitive parameters, we use Figure 4. Here, the optimal bonuses are plotted against $g _ { c }$ and Figure 3 shows that with increasing ${ \boldsymbol { g } } _ { c } ,$ , the bonuses change the same way as with increasing $M R ^ { * }$ . For example at low values of ${ { g } _ { c } } ,$ both bonuses are zero but with increasing ${ { g } _ { c } } ,$ the bonus for only the closed project becomes positive. In other numerical experiments, we observe that $w _ { t }$ behaves similar to $g _ { c }$ while $g _ { o }$ and $p$ have an opposite behavior.

Figure 4 Illustrating Proposition 1: Bonuses with IR Constraint Not Binding  
![](/api/attachments/EACE7BAZ/fulltext/images/b76887ce3be8d442a31e1bd8f1fcb34427e78df761969f1ff03de5337aa1e511.jpg)

We next want to explore how the bonuses are changed when the programmer has a minimum utility that must be met for her to stay employed, $\mathrm { i . e . }$ , if the individual rationality constraint applies. In particular, our interest is to establish the contract characteristics when the firm pays bonuses for both projects simultaneously. Intuitively, this will happen when paying a bonus for only one project to meet the IR constraint distorts the programmer’s choice of effort division too far away from the firm’s optimal choice. Our next result describes this type of solution.

Proposition 2. An optimal solution $( x ^ { * } , w _ { c } ^ { * } , w _ { o } ^ { * } ) _$ where $w _ { c } ^ { * } > 0 , w _ { o } ^ { * } > 0$ when the IR constraint is binding is given as follows.

$1 . \ x ^ { * }$ maximizes total value $E V _ { t } = g + p _ { c } g _ { c } + p _ { o } g _ { o } +$ $p _ { o } ( \delta w _ { t } / ( 1 - \delta ) ) + p _ { g b } ( \delta w _ { t } / ( 1 - \delta ) )$ .

2. Using $x ^ { * } , w _ { c } ^ { * }$ and $\boldsymbol { w } _ { o } ^ { * }$ are obtained by simultaneously solving $E S ( x ^ { * } ) = u$ and $d E S / d x | _ { x = x ^ { * } } = 0$

The proof is presented in the appendix. Proposition 2 establishes that the solution with bonuses for both projects is also socially optimal because this maximizes the total value created for the firm and the programmer. We refer to this total value as $E V _ { t } ,$ , where

$$
E V _ {t} = g + p _ {c} g _ {c} + p _ {o} g _ {o} + p _ {o} \frac {\delta w _ {t}}{1 - \delta} + p _ {g b} \frac {\delta w _ {t}}{1 - \delta}.
$$

This is surprising; one might think that offering both types of bonuses must be inefficient because they have opposite effects on the choice of effort division (Lemma 2). The key intuition behind this result is as follows. Suppose the firm implements an effort division $x ^ { * }$ . This results in firm value $E V ( x ^ { * } )$ , which can be expressed as $E V _ { t } ( x ^ { * } ) - E S ( x ^ { * } )$ by rewriting (3). Note that $\bar { E } S ( x ^ { * } ) = u$ because the IR is binding. Thus, firm value can be maximized by implementing an $x ^ { * }$ that maximizes $E V _ { t } ( x )$

Finally, it is easily shown that $E V _ { t } ^ { \prime \prime } ~ < ~ 0$ and $E V _ { t } ^ { \prime } | _ { x = x _ { o } } > 0$ while $E \bar { V } _ { t } ^ { \prime } | _ { x = x _ { c } } \ < \ 0 ,$ , implying that the appropriate $x ^ { * }$ to maximize total value $E V _ { t }$ is such that $x _ { o } < x ^ { * } < x _ { c }$ . From Lemma 1, we know that such an $x ^ { * }$ can always be implemented with an appropriate choice of bonuses.

Having identified the solution with positive bonuses for both projects (Proposition 2), we now characterize when this particular solution will be picked by the firm, if at all.

Proposition 3. When the unconstrained solution specified in Proposition 1 is not feasible because of the IR constraint, the firm’s choice of bonuses that locally maximize its value is reflected in the following menu:

Case I. $w _ { c } ^ { * } = 0$ and $\boldsymbol { w } _ { o } ^ { * }$ and $x ^ { * }$ are obtained by simultaneously solving $E S ( x ^ { * } ) = u$ and $d E S / d x | _ { x = x ^ { * } } = \bar { 0 }$ iff

$$
M R ^ {*} <   - \frac {(1 - p _ {c} ^ {*} / p _ {o} ^ {*}) A ^ {*}}{1 - p _ {c} ^ {\prime *} / p _ {o} ^ {\prime *}} - \frac {u - Q ^ {*}}{p _ {o} ^ {*}} \bigg (p _ {o} ^ {\prime *} - \frac {(p _ {o} ^ {*} - p _ {c} ^ {*}) p _ {o} ^ {\prime \prime *}}{p _ {o} ^ {\prime *} - p _ {c} ^ {\prime *}} \bigg).
$$

Case II. $w _ { o } ^ { * } = 0$ and $\boldsymbol { w } _ { c } ^ { * }$ and $x ^ { * }$ are obtained by simultaneously solving $E S ( x ^ { * } ) = u$ and $d E S / d x | _ { x = x ^ { * } } = 0$ iff

$$
M R ^ {*} > - \frac {\left(1 - p _ {o} ^ {*} / p _ {c} ^ {*}\right) B ^ {*}}{1 - p _ {o} ^ {\prime *} / p _ {c} ^ {\prime *}} - \frac {u - Q ^ {*}}{p _ {c} ^ {*}} \left(p _ {c} ^ {\prime *} - \frac {\left(p _ {o} ^ {*} - p _ {c} ^ {*}\right) p _ {c} ^ {\prime \prime *}}{p _ {o} ^ {\prime *} - p _ {c} ^ {\prime *}}\right).
$$

Case III. The solution specified in Proposition $2 \ i f f$ $( M R ^ { * } - p _ { c } ^ { \prime * } w _ { c } ^ { * } - p _ { o } ^ { \prime * } w _ { o } ^ { * } ) ( p _ { o } ^ { \prime * } / p _ { c } ^ { \prime \prime * } w _ { c } ^ { * } + p _ { o } ^ { \prime \prime * } w _ { o } ^ { * } + Q ^ { \prime \prime * } ) - p _ { o } ^ { * } =$ $( M R ^ { * } - p _ { c } ^ { \prime * } w _ { c } ^ { * } - p _ { o } ^ { \prime * } w _ { o } ^ { * } ) ( p _ { c } ^ { \prime * } / p _ { c } ^ { \prime \prime * } w _ { c } ^ { * } + p _ { o } ^ { \prime \prime * } w _ { o } ^ { * } + Q ^ { \prime \prime * } ) - p _ { c } ^ { * } ,$ where $Q = ( p _ { t } + ( 1 - p ) p _ { g b } \delta ) ( \delta w _ { t } ) / ( 1 - \delta ) ;$ ; the starred terms indicate that the corresponding quantity is evaluated at $x ^ { * }$ , the optimal effort division chosen by the programmer.

As in Proposition 1, the cases in Proposition 3 represent local solutions and, in case of multiple solutions being possible, the firm will pick the one that is globally optimal. A comparison of the menu of bonuses given in Propositions 1 and 3 indicates that the firm’s choices are significantly different when the individual rationality constraint is binding vis-à-vis when this constraint does not apply. The important reason for this difference is reflected by the presence of $u ,$ explicitly or implicitly, in the conditions for the three cases in Proposition 3. Of particular interest is the situation where the firm provides positive bonuses for both projects, i.e., Case III of Proposition 3.

To better understand the situations where such a choice is made, we use Figures 5 and 6. To draw them, we start with a situation where u is so small that the IR constraint is not binding and hence Proposition 1 applies. Then, we increase u so that the IR constraint begins to bind and thereby show the impact of changing u. The parameter values used for drawing Figure 5 are $\delta = \stackrel { \textstyle - } { 0 . 2 } , ~ d = 0 . 5 , ~ e = 0 . 9 , ~ g = 1 , ~ g _ { c } = 1 \bar { 2 }$

Figure 5 Illustrating Proposition 3: Bonuses with Increasing u  
![](/api/attachments/EACE7BAZ/fulltext/images/615edb17dd06939b16d4466d53c72c4a9fdf2444ff5caa024560c7a43638cb25.jpg)

Figure 6 Another Illustration of Proposition 3: Bonuses with Increasing u  
![](/api/attachments/EACE7BAZ/fulltext/images/f48adcd0efa4a3e8c0aacbb77da9e35220c4ebfcc16860b2de5136f75580afff.jpg)  
$g _ { o } = 1 4 , p = 0 . 5 ,$ and $w _ { t } = 2 8 ;$ u is varied from 4 to $6 . 2$ The firm’s problem is numerically solved to determine the optimal bonuses using the probability functions specified in Example 1. The region to the left of the dark vertical line $( u < 4 . 2 )$ is the one where u is so small that the IR constraint does not bind. Figure 5 shows that Case III of Proposition 1 applies and that $w _ { c } ^ { * } = 0$ and $w _ { o } ^ { * } = 0 .$ . As u increases beyond $4 . 2 ,$ the IR constraint binds. Lemma 4 proves that an increase in any one of the bonuses increases the expected surplus ES of the rookie programmer. Figure 5 shows that the firm first meets the IR constraint by raising only one of the bonuses $( w _ { c } ^ { * } )$ . Increasing $\boldsymbol { w } _ { c } ^ { * }$ beyond the optimal level to meet the IR constraint makes $d E V / d w _ { c }$ increasingly more negative. This eventually makes $d E V / d w _ { o } > \dot { d E V } / d w _ { c }$ (see the proof of Proposition 3 in the appendix), and the firm finds that it is now attractive to raise $w _ { o }$ as well. In Figure 5, this happens when u increases beyond 5.4. The firm then provides $w _ { c } ^ { * } > 0$ and $w _ { o } ^ { * } > 0$ to meet the IR constraint. Figure 6 shows another instance of how an increase in u impacts bonus choices. The difference from Figure 5 is that initially the firm picks $\boldsymbol { w } _ { o } ^ { * }$ to meet the constraint and increases $w _ { c } ^ { * }$ only later. The reason for the difference is that in drawing Figure $6 ,$ the parameter $g _ { o }$ is increased to 25 and $g _ { c }$ is reduced to 5 while others are held fixed. It is useful to showcase that in Figure 5 Cases II and III of Proposition 3 and in Figure $6 ,$ Cases I and III of Proposition 3 apply.

We now comment on the social efficiency of the various solutions in Propositions 1 and 3. The point $x _ { 2 }$ in Figure 7 corresponds to the effort division that maximizes social efficiency. Proposition 2 establishes that this is the effort division that is picked by the programmer when $w _ { c } ^ { * } > 0 , w _ { o } ^ { * } > 0$ and the IR constraint is binding. In Lemma 5 (presented in the appendix), we show that dE $V _ { t } / d x > 0$ when $w _ { c } ^ { * } > 0 , \ w _ { o } ^ { * } = 0$ and the IR constraint is not binding. Hence, in this case, the bonuses offered by the firm induce the programmer

Figure 7 Social Efficiency  
![](/api/attachments/EACE7BAZ/fulltext/images/ab7c8aef08d8584c6f7b08b7f356afd46272af61a342e9bfec8a770a98e387f3.jpg)  
to pick an effort division that is too small for social efficiency. This is illustrated in Figure 7 by point $x _ { 1 }$ . When the IR constraint binds but $w _ { c } ^ { * } > 0$ and $w _ { o } ^ { * } = 0 ,$ , the bonus for the closed project must be raised to meet the IR constraint. Hence, in accordance with Lemma $^ { 2 , }$ the equilibrium effort level increases. This reduces the discrepancy from the socially optimal effort level at least initially. If the IR constraint is not binding and $w _ { o } ^ { * } > 0$ and $w _ { c } ^ { * } = 0 ,$ , then (as shown in Lemma 6 in the appendix) the effort choice in equilibrium is too $h i g h$ for social efficiency $( d E V _ { t } / d x < 0 )$ . This is illustrated in Figure 7 by point $x _ { 3 } .$ . As before, when the IR constraint binds, the bonus for the open project may be increased, which may reduce the discrepancy from the socially optimum effort.

## 4. Impact of Degree of Openness of the Proprietary Project

The open-source project is superior to the closedsource project for the programmer in that it more clearly reveals the talent of the programmer. In the absence of any direct incentives offered by the firm, this built-in career incentive dictates the effort division of the programmer between the open- and closed-source projects. In the preceding analysis, we showed that such effort division may not be optimal for the firm and thus it may give bonuses to induce a different effort division.

Another way in which the firm could possibly induce a favorable effort division is by changing the degree of openness of the proprietary project. As the proprietary project is made more open, success in this project is more likely to convey to the labor market that the programmer is talented. Thus, the programmer will pick an effort division that is more in favor of the proprietary project. Increasing the degree of openness of the proprietary project, however, comes at a cost to the firm because this reduces the chances that the firm will have private information that the programmer is talented. Hence, the benefits from employing a talented programmer at a low wage cost would be reduced. Increasing the degree of openness to induce higher effort in the closed project therefore comes with its own cost/benefit trade-off. This indicates that some intermediate level of openness of the proprietary project may be optimal for maximizing the firm’s value, as Figure 8 shows. Figure 8 is drawn using the parameter values $\delta = 0 . 2 { \overset { - } { , } } \ d = 0 . 5 ,$ $e = 0 . 9 , g = 1 , g _ { c } = 4 , g _ { o } = 6 , u = 0 ,$ , and $w _ { t } = 2 8 .$ . Recall that the programmer will exert effort $x _ { r } ( p + ( 1 - p ) \delta )$ to maximize the probability $p _ { r } ( p + ( 1 - p ) \delta )$  in absence of any bonuses. If it is optimal for the firm to implement an effort in the closed project greater than $x _ { r } ( p + ( 1 - p ) \delta )$ , then it has the options of either increasing $w _ { c }$ or increasing $p .$ It is in such cases that increasing the degree of openness turns out to be useful. ${ \mathrm { I f } } ,$ on the other hand, the optimal decision for the firm is to implement an effort lesser than $x _ { r } ( p + ( 1 - p ) \delta )$ in the closed project, then it should either reduce the degree of openness of the closed project or increase $w _ { o }$

Figure 8 Impact of Changing p with Bonus for Only One Project  
![](/api/attachments/EACE7BAZ/fulltext/images/0e3ae79d795c0816f3e4fcd58d43c8443dbef5c1fc486fd6c1f0555a55330392.jpg)

If the IR constraint is binding, the optimal decision for the firm changes because it now needs to ensure a minimum payoff to the programmer. If it is paying a bonus in only one project to ascertain the minimum payoff, the flexibility of adjusting the degree of openness may allow the firm a lower cost and may therefore improve the firm’s value. If, however, the firm is paying bonuses on both projects, it picks bonuses to implement an effort that maximizes the total surplus $\hat { E } V _ { t }$ (Proposition 2). The firm value $E V = E V _ { t } - u$ therefore remains unchanged even if the degree of openness of the closed project can be adjusted. This happens because, as the degree of openness of the closed project increases, the programmer gets additional future benefits because of an increase in the chances of revelation of talent. Consequently, the firm implements the socially optimal effort by lowering bonus payments. However, the savings in cost from bonus payments are exactly compensated for by the increase in cost to the firm because of increase in p. Hence, the net cost to the firm and the firm value remain the same.

## 5. Concluding Remarks

## 5.1. Discussion on Model Assumptions and Limitations

An artifact of our model is the assumption that only a talented programmer can produce a successful outcome, which can then be construed as an informational signal of talent. If even an untalented programmer can sometimes create a successful outcome, the major impact on our model will be that output created by rookies in the first period of employment will not be sufficient to conclude whether they are talented. $\operatorname { N o w } ,$ information on the output created over several periods will be needed to make a judgment on a programmer’s talent. Hence, the premium for being a talented programmer, reflected in the market wage $w _ { t } ,$ will be available only after several periods. Clearly, the future payoffs to signaling talent are reduced. The choice of effort division is made by a programmer to maximize his combined payoff from future payoffs and the expected bonus payment in the current period. Because the future becomes less valuable with the relaxing of this assumption, a firm may be able to influence a programmer’s choice of effort division by paying a lower bonus, which therefore results in a lower expected surplus for the programmer. However, this makes the IR constraint bind more quickly. The firm must then raise the bonus to meet the IR constraint until paying a bonus for just one project to meet the IR constraint results in a highly distorted effort division by the programmer. The firm must then resort to paying bonuses for both projects, just as in the current model. Thus, our key insights are expected to be robust to relaxing this assumption.

A limitation is that we have only focused on learning by doing and not on learning through classroom training. Thus, our model assumes that the impact of learning by doing is in addition to learning that is possible through classroom training. Support for the hypothesis that learning by doing provides unique learning opportunities that cannot be duplicated through learning by training is available through various sources such as UNU-MERIT (2006). This report also points out that many firms value the learning benefits that their programmers get by working on open-source projects. Hence, they explicitly or implicitly allow their programmers to work in open-source projects during work time.

If learning by training were modeled, one fundamental difference from learning by doing through open source is the moral hazard issue. Classroom training time can be explicitly controlled by the firm, but there is little control on programmers’ mindshare when they are allowed to simultaneously work on open- and closed-source projects. Consequently, firms can control the training time directly without providing any bonuses to programmers. Another major difference is that classroom training might not convey one’s talent to the market as well as a good outcome in a live open-source project. Thus, classroom training may have less career incentive connotations. Finally, classroom training comes at a cost while doing open source is free and may even have strategic value for the firm (which we capture through $g _ { o } )$ . Because of these differences, learning by training and learning by doing will have different implications from the firm’s and programmers’ perspectives. In particular, no bonus payments are necessary to induce programmers to learn through training because the firm can explicitly control programmers’ participation in these activities.

Assumptions 1 and 2 (§2.2.1) are central to our model and capture the impact of effort and learningby-doing effects. Because of the tension in the impact of effort and learning by doing, the marginal probabilities of success in the open- and closed-source projects are assumed to be concave with internal maxima. ${ \mathrm { I f } } ,$ however, the learning-by-doing effects are weak, the concavity and the internal maxima will disappear and Assumption 1 will not apply. Assumption 2 makes the point that the impact of learning by doing is not too strong. Our results thus apply to situations where the learning effects are significant but at the same time they are not too large so as to have an overriding influence.

## 5.2. Discussion of the Setting and Results

It has been observed that many programmers hired by software development firms contribute to opensource software projects in addition to working on projects for which they have been hired. Previous researchers have addressed this puzzle by pointing out that these programmers may derive some economic value from learning and career progression opportunities because good contributions in opensource projects help convince the market that these programmers are talented and deserve better compensation in future.

When programmers work on open-source projects, they use up time that they could have potentially invested in the proprietary projects for the hiring firms. This is not always harmful to hiring firms because those firms may get several sources of value from open-source projects. One such situation is the Eclipse open-source development platform supported by IBM. IBM’s programmers work on Eclipse while simultaneously working on the development of software tools complementary to the Eclipse platform.

These software tools are commercially sold by IBM. Clearly, IBM’s business depends on the popularity and success of the Eclipse project. In other words, IBM derives a strategic value from the success of the Eclipse platform. In addition to such strategic value, when a firm’s programmers work on opensource projects, they may learn useful skills that improve their success rate on the firm’s proprietary project(s) and vice versa. Again, the Eclipse platform and its complementary software are a good example. There is clearly alot of learning benefit because both projects are closely related. One can therefore surmise that both the firm and the programmers have definite incentives to succeed in both open and closed projects but these incentives may not be aligned (e.g., the programmer may have a higher incentive to do well in the open project than the firm). Because of this situation, firms may enter into performance-based contracts with programmers to align programme incentives with their own. We find that when the marginal revenue of effort for a closed project is high, a firm pays a bonus for this project. When this marginal revenue is low, the firm pays a bonus for the open project. For the midrange of marginal value, the firm pays no bonus. A programmer then makes an effort choice that maximizes the chance of exposing her talent in the labor market to get the wage premium for talented programmers in future. However, if the outside opportunities are attractive, future benefits may not be sufficient to attract a programmer to take the firm’s job offer. In this case, the firm may pay a bonus for both projects. The reader may wonder if any firm has ever paid bonuses to programmers for developing opensource projects. We found a real-world example of that on http://www.theserverside.com/news/thread. tss?thread\_id=18524. This news item (article date March 25, 2003) reports that the software firm JBoss paid bonuses to several programmers who contributed to the development of an open-source application server pioneered by this firm. We further note that a socially efficient outcome is obtained in circumstances in which the firm offers bonuses for both types of project. This is because, with bonuses chosen by the firm, the programmer picks an effort division that maximizes the total expected value created.

If a firm employs policies that showcase programmers’ contributions to proprietary projects in much better ways to other firms, programmers will have a higher incentive to invest effort in these projects. Thus, making a proprietary project more open can serve as a substitute to increasing the bonus for that project. Such a policy can come at a cost to the firm because it reduces the chances of the firm having access to the services of talented programmers at low wage costs in future. The strategy employed by

Firaxis Games<sup>17</sup> is similar to the one we discuss here. Firaxis owns the rights to a very famous game named Civilization. It lists the names of important developers of this game on its website. Adobe System Inc.<sup>18</sup> also employs a similar policy. When the Adobe Photoshop CS2 version 9.0 loads, the names of the important contributors are listed. This kind of policy is likely to be effective only when the outside market opportunities are not too attractive. When this is not the case, increasing the degree of openness for a closed project is unlikely to yield any benefit.

In summary, this paper shows how firms can maximize value creation by appropriately channeling programmer effort in open- and closed-source projects. This is achieved by augmenting the economic incentives of programmers to contribute to open-source software with output-based compensation schemes. As the open-source software movement gains momentum, these insights will help firms leverage open source more effectively.

## Acknowledgments

The authors thank the Senior Editor Sumit Sarkar, the Associate Editor Srinivasan Raghunathan, and three anonymous referees for their comments that helped improve the paper considerably.

## Appendix

Lemma 1. Let $x _ { c }$ and $x _ { o }$ be the maxima over $[ 0 , 1 ] o f p _ { c }$ and ${ p } _ { o } ,$ respectively. Only $x ^ { * }$ such that $x _ { o } \leq x ^ { * } \leq x _ { c }$ can satisfy the IC constraint.

First, note that Assumption 1 says that $0 < x _ { o } < x _ { c } < ~ 1$ We note that all terms of dES/dx are weakly positive if $x <$ $x _ { o }$ and so the programmer would prefer a larger x. Hence, $x ^ { * } \geq x _ { o }$

Turning to $x _ { c } ,$ we note that all terms of dES/dx are weakly negative if $x > x _ { c }$ and so the programmer would prefer a smaller x. Hence, ${ \boldsymbol x } ^ { * } \leq { \boldsymbol x } _ { c }$

Lemma 2. $H f x ^ { * }$ satisfies the incentive compatibility constraint, then $\partial x ^ { * } / \partial w _ { c } \geq 0$ and $\partial x ^ { * } / \partial w _ { o } \leq 0$

By using the implicit function theorem on (6),

$$
\begin{array}{l} \frac {\partial x ^ {*}}{\partial w _ {c}} = - E S _ {x w _ {c}} / E S _ {x x} \\ = - \frac {p _ {c} ^ {\prime}}{p _ {c} ^ {\prime \prime} w _ {c} + p _ {o} ^ {\prime \prime} w _ {o} + (p _ {t} ^ {\prime \prime} + (1 - p) \delta p _ {g b} ^ {\prime \prime}) \delta w _ {t} / (1 - \delta)}. \end{array}\tag{8}
$$

Note that $( p _ { t } ^ { \prime \prime } + ( 1 - p ) \delta p _ { g b } ^ { \prime \prime } ) = p _ { r } ^ { \prime \prime } ( p + ( 1 - p ) \delta )$ . From Definition $^ { 1 , }$ we know that $p _ { r } ^ { \prime \prime } \check { ( z ) } < 0$ . Hence, the denominator is negative by the strict concavity of the probability functions. The numerator $p _ { c } ^ { \prime }$ is positive in the interval $( x _ { o } , x _ { c } )$ This proves that $\partial x ^ { * } / \partial w _ { c } \geq 0$

The proof of $\partial x ^ { * } / \partial w _ { o } \leq 0$ is similar and is omitted here.

Lemma 3. If the IR constraint is not binding, then the firm sets either $w _ { c } ^ { * } > 0$ or $w _ { o } ^ { * } > 0$ but not both.

Let $( w _ { c } ^ { * } , w _ { o } ^ { * } )$ be any solution to the firm’s problem. Let $x ^ { * }$ be the effort level on the closed project chosen by the worker with these bonuses. Consider a problem of minimizing the cost of getting the worker to implement $x ^ { * } ,$ . Clearly, $( w _ { c } ^ { * } , w _ { o } ^ { * } )$ must solve this problem, too, or else these bonuses do not solve the firm’s problem as we have assumed. We will now use this simplified problem to characterize the optimal bonuses.

At a given $x ^ { * } ,$ , the problem of finding a least-cost set of bonuses to implement $x ^ { * }$ is a linear programming problem with two decision variables $w _ { c }$ and $w _ { o }$ and one constraint— the IC constraint (as the IR constraint is not binding). Because there is only one constraint, only one of the variables $w _ { c }$ or $w _ { o }$ will enter the basis. Therefore, either $w _ { c } ^ { * } > 0$ or $w _ { o } ^ { * } > 0$ but not both.

Proof of Proposition 1. For Case I, suppose the firm chooses $w _ { c } ^ { * } = 0$ . By Lemma 3, this implies that $w _ { o } ^ { * } \geq 0$

Taking $w _ { c } ^ { * } = 0 ,$ we examine the first-order condition for the firm’s objective function w.r.t. $w _ { o } \mathrm { . }$

$$
\left. \frac {d E V}{d w _ {o}} \right| _ {w _ {c} ^ {*} = 0, x = x ^ {*}} = (M R ^ {*} - p _ {o} ^ {\prime *} w _ {o}) \frac {d x ^ {*}}{d w _ {o}} - p _ {o} ^ {*} = 0.
$$

We substitute the value of $d x ^ { * } / d w _ { o }$ is (obtained in a fashion similar to the way $d x ^ { * } / d w _ { c }$ was obtained in Lemma 2) in the above equation and solve for $\boldsymbol { w } _ { o } ^ { * }$ . This gives

$$
w _ {o} ^ {*} = \frac {M R ^ {*} + A ^ {*}}{p _ {o} ^ {\prime *} - p _ {o} ^ {*} p _ {o} ^ {\prime \prime *} / p _ {o} ^ {\prime *}},\tag{9}
$$

where $A ^ { * } = p _ { o } ^ { * } / p _ { o } ^ { \prime * } \delta / ( 1 - \delta ) ~ w _ { t } ( p _ { t } ^ { \prime \prime * } + ( 1 - p ) \delta p _ { \sigma b } ^ { \prime \prime * } )$ . Note that the numerator of $A ^ { * }$ is negative because $( \dot { p } _ { t } ^ { \prime \prime } + \stackrel { \sim } { ( 1 - p ) } \delta p _ { \_ b } ^ { \prime \prime } ) =$ $p _ { r } ^ { \prime \prime } ( p + ( 1 - p ) \delta )$ , and from Definition 1 we know that $p _ { r } ^ { \prime \prime } \check { ( z ) } <$ 0. The denominator of $A ^ { * }$ is negative because $p _ { o } ^ { \prime }$ is negative at $x \geq x _ { o }$ . Hence, $A ^ { * }$ is a positive quantity. Note that $\boldsymbol { w } _ { o } ^ { * }$ is also positive provided $M R ^ { * } < - A ^ { * }$ because $\boldsymbol { w } _ { o } ^ { * }$ then has a negative numerator and denominator. This also rules out taking $w _ { o } ^ { * } < 0$

Given that $\boldsymbol { w } _ { o } ^ { * }$ and $w _ { c } ^ { * }$ are chosen as above, the programmer chooses the effort $x ^ { * }$ that maximizes her surplus ES. The corresponding first-order condition is $p _ { o } ^ { \prime } w _ { o } + p _ { c } ^ { \prime } w _ { c } +$ $( p _ { t } ^ { \prime } + ( 1 - p \bar { ) } p _ { \it \circ b } ^ { \prime } \delta ) ( \bar { \delta w } _ { t } / ( 1 - \delta ) ) = 0 .$ . Substituting in w<sup>∗</sup> and $\boldsymbol { w } _ { o } ^ { * }$ from above and simplifying, we get $( M R ^ { * } + \bar { A ^ { * } } ) / ( p _ { o } ^ { \prime * } - p _ { o } ^ { * } p _ { o } ^ { \prime \prime * } )$ $p _ { o } ^ { \prime * } \bigr ) = - ( p _ { t } ^ { \prime * } + ( 1 - p ) p _ { g b } ^ { \prime * } \delta ) ( \delta w _ { t } / ( 1 - \delta ) / p _ { o } ^ { \prime * } )$ , which gives us the solution for $x ^ { * }$

Note that $w _ { c } ^ { * } , w _ { o } ^ { * }$ , and $x ^ { * }$ above form a consistent solution iff $M R ^ { * } < - A ^ { * }$

Cases II and III are proved similarly.

To complete the proof, we also show that for any values of $A ^ { * }$ and ${ \bar { B } } ^ { * } .$ , it must be true that $- A ^ { * } < B ^ { * }$ . We have already established that $A ^ { * } > 0$ . Take $B ^ { * } \colon$ Employing parallel logic to that used for showing $A ^ { * } > 0$ , we see that its numerator is negative and its denominator is positive. With the negative sign of the expression, we have $B ^ { * } > 0 ,$ . Because both $A ^ { * }$ and $B ^ { * }$ are positive quantities, it must be that $- A ^ { * } < B ^ { * }$ Therefore, for some parameter values, the solution specified in Case III is the only solution.

Lemma 4. Increasing $w _ { c }$ or $w _ { o }$ increases a programmer’s expected surplus.

Using Equation (2), we can write

$$
\frac {d E S}{d w _ {c}} = \left(E S ^ {\prime} \frac {d x}{d w _ {c}}\right) \Bigg | _ {x = x ^ {*}} + p _ {c} ^ {*}.
$$

Because $E S ^ { \prime } | _ { x = x ^ { * } } = 0 ,$ , we have $d E S / d w _ { c } = p _ { c } ^ { * } > 0$ . Similarly, we can show that $d E S / d w _ { o } > 0$

Proof of Proposition 2. Equation (3) can be rewritten as $E V ( x ) = E V _ { t } ( x ) - E S ( x )$ , where $E V _ { t } ( x ) = g + p _ { c } g _ { c } + p _ { o } g _ { o } +$ $p _ { o } ( \delta w _ { t } / ( 1 - \delta ) ) + p _ { g b } ( \delta w _ { t } / ( 1 - \delta ) )$ . The Lagrangian function of the firm’s problem is

$$
{\cal L} = E V _ {t} (x ^ {*}) + (\lambda - 1) E S (x ^ {*}) + \mu w _ {c} + \nu w _ {o} - \lambda u,
$$

where $x ^ { * }$ has been substituted in from the IC constraint. $\lambda ,$ $\mu ,$ and ) are the Lagrange multipliers of the IR constraint and the nonnegativity constraints on $w _ { c }$ and $w _ { o } ,$ respectively. Dropping the parentheses in the expression for the Lagrangian function and taking its derivatives with respect to $w _ { c }$ and $w _ { o } ,$ we get

$$
\frac {d L}{d w _ {c}} = \frac {d E V _ {t}}{d w _ {c}} + (\lambda - 1) p _ {c} + \mu = 0,\tag{10}
$$

$$
\frac {d L}{d w _ {o}} = \frac {d E V _ {t}}{d w _ {o}} + (\lambda - 1) p _ {o} + \nu = 0.\tag{11}
$$

If $w _ { o } , w _ { c } > 0 ,$ , then $\mu = 0$ and $\nu = 0 .$ . Furthermore,

$$
\frac {d E V _ {t}}{d w _ {c}} = \left(p _ {c} ^ {\prime} g _ {c} + p _ {o} ^ {\prime} g _ {o} + p _ {o} ^ {\prime} \frac {\delta w _ {t}}{1 - \delta} + p _ {g b} ^ {\prime} \frac {\delta w _ {t}}{1 - \delta}\right) \frac {d x ^ {*}}{d w _ {c}}
$$

and

$$
\frac {d E V _ {t}}{d w _ {o}} = \left(p _ {c} ^ {\prime} g _ {c} + p _ {o} ^ {\prime} g _ {o} + p _ {o} ^ {\prime} \frac {\delta w _ {t}}{1 - \delta} + p _ {g b} ^ {\prime} \frac {\delta w _ {t}}{1 - \delta}\right) \frac {d x ^ {*}}{d w _ {o}}.
$$

Using Lemma 2, dE $V _ { t } / d w _ { c }$ and $d E V _ { t } / d w _ { o }$ must be of opposite signs. Hence, for Equations (10) and (11) to be consistent, it must be that $\lambda = \bar { 1 , ~ } d E V _ { t } / d w _ { c } = 0 ,$ , and $d E V _ { t } / d w _ { o } =$ $0 , \lambda > 0$ implies that the IR constraint is binding.

Note that $d E V _ { t } / d w _ { c } = 0$ and $d E V _ { t } / d w _ { o } = 0$ imply that $p _ { c } ^ { \prime } g _ { c } + p _ { o } ^ { \prime } g _ { o } + p _ { o } ^ { \prime } ( \delta w _ { t } / ( 1 - \delta ) ) + p _ { \it g _ { b } } ^ { \prime } ~ ( \delta w _ { t } ( 1 - \delta ) ) = 0 .$ . We can determine the firm’s choice of x to be implemented by solving this last equation. Notice that this equation also implies maximization of

$$
E V _ {t} = g + p _ {c} g _ {c} + p _ {o} g _ {o} + p _ {o} \frac {\delta w _ {t}}{1 - \delta} + p _ {g b} \frac {\delta w _ {t}}{1 - \delta} \quad \mathrm{w.r.t.} x.
$$

Once $x ^ { * }$ is determined, we solve (IR) and (IC) simultaneously at $x ^ { * }$ to find the optimal bonus wages ${ w _ { c } ^ { * } }$ and $\boldsymbol { w } _ { o } ^ { * }$ . All the probabilities are evaluated at $x ^ { * }$ and, hence, these two equations are linear. Therefore, using Cramer’s rule, we get

$$
\begin{array}{l} w _ {c} ^ {*} = \frac {\left| \begin{array}{c} u - p _ {t} (\delta w _ {t} / (1 - \delta)) - (1 - p) p _ {g b} (\delta^ {2} w _ {t} / (1 - \delta)) p _ {o} \\ - p _ {t} ^ {\prime} (\delta w _ {t} / (1 - \delta)) - (1 - p) p _ {g b} ^ {\prime} (\delta^ {2} w _ {t} / (1 - \delta)) p _ {o} ^ {\prime} \end{array} \right|}{\left| \begin{array}{c c} p _ {c c} & p _ {o} \\ p _ {c c} ^ {\prime} & p _ {o} ^ {\prime} \end{array} \right|}, \\ w _ {o} ^ {*} = \frac {\left| \begin{array}{c c} p _ {c c} & u - p _ {t} (\delta w _ {t} / (1 - \delta)) - (1 - p) p _ {g b} (\delta^ {2} w _ {t} / (1 - \delta)) \\ p _ {c c} ^ {\prime} & - p _ {t} ^ {\prime} (\delta w _ {t} / (1 - \delta)) - (1 - p) p _ {g b} ^ {\prime} (\delta^ {2} w _ {t} / (1 - \delta)) \end{array} \right|}{\left| \begin{array}{c c} p _ {c c} & p _ {o} \\ p _ {c c} ^ {\prime} & p _ {o} ^ {\prime} \end{array} \right|} \end{array}\tag{12}
$$

Proof of Proposition 3. When the unconstrained solution given in Proposition 1 is not feasible, either or both of w<sup>∗</sup> and $\boldsymbol { w } _ { o } ^ { * }$ must be positive to ensure that $E S = u .$ . Notice that the IR constraint can always be satisfied for some values of $w _ { c }$ and $w _ { o }$ . Hence, the optimization problem always has a solution, and it takes one of the following forms:

$$
\begin{array}{l l} \text {I.} & w _ {c} ^ {*} > 0 \text {and} w _ {o} ^ {*} = 0. \\ \text {II.} & w _ {c} ^ {*} = 0 \text {and} w _ {o} ^ {*} > 0. \\ \text {III.} & w _ {c} ^ {*} > 0 \text {and} w _ {o} ^ {*} > 0. \end{array}
$$

First, we consider the solution specified in Case I. In this case, $w _ { o } ^ { * } = 0$ . Then, $E S ( x ^ { * } ) = u$ implies $w _ { c } ^ { * } = ( u - Q ^ { * } ) / p _ { c } ^ { * } > 0 .$ Substituting in the values of ${ w _ { c } ^ { * } }$ and $\boldsymbol { w } _ { o } ^ { * }$ in the first-order condition of the expected surplus ES of the programmer, we obtain $x ^ { * }$ . The optimality of the solution depends on the slopes of EV with respect to the bonuses $w _ { c }$ and $w _ { o } .$ We have the following derivatives

$$
\left. \frac {d E V}{d w _ {o}} \right| _ {w _ {o} ^ {*} = 0} = \left(g _ {c} p _ {c} ^ {\prime *} + g _ {o} p _ {o} ^ {\prime *} + (1 - p) p _ {g b} ^ {\prime *} \delta w _ {t}\right) \frac {d x ^ {*}}{d w _ {o}}
$$

$$
- p _ {c} ^ {\prime *} w _ {c} \frac {d x ^ {*}}{d w _ {o}} - p _ {o} ^ {*},\tag{13}
$$

$$
\begin{array}{c} \frac {d E V}{d w _ {c}} \bigg | _ {w _ {o} ^ {*} = 0} = \left(g _ {c} p _ {c} ^ {\prime *} + g _ {o} p _ {o} ^ {\prime *} + (1 - p) p _ {g b} ^ {\prime *} \delta w _ {t}\right) \frac {d x ^ {*}}{d w _ {c}} \\ - p _ {c} ^ {\prime *} w _ {c} \frac {d x ^ {*}}{d w _ {c}} - p _ {c} ^ {*}. \end{array}\tag{14}
$$

Combining (13) and (14), we get

$$
\left. \frac {d E V}{d w _ {o}} \right| _ {w _ {o} ^ {*} = 0} = \left(p _ {c} ^ {*} + \frac {d E V}{d w _ {c}} \right| _ {w _ {o} ^ {*} = 0}) \frac {d x ^ {*}}{d w _ {o}} \bigg / \frac {d x ^ {*}}{d w _ {c}} - p _ {o}.\tag{15}
$$

From Equation (8), in the proof of Lemma 2, from and a similar equation for $d x ^ { * } / d w _ { o } ,$ , we note that

$$
\left. \frac {d x ^ {*}}{d w _ {o}} \right/ \frac {d x ^ {*}}{d w _ {c}} = \frac {p _ {o} ^ {\prime *}}{p _ {c} ^ {\prime *}}.\tag{16}
$$

Substituting this into (15), we get

$$
\left. \frac {d E V}{d w _ {o}} \right| _ {w _ {o} ^ {*} = 0} = \left(p _ {c} ^ {*} + \frac {d E V}{d w _ {c}} \right| _ {w _ {o} ^ {*} = 0}) \frac {p _ {o} ^ {\prime *}}{p _ {c} ^ {\prime *}} - p _ {o} ^ {*}.
$$

The firm will choose $w _ { c } ^ { * } > 0$ and $w _ { o } ^ { * } = 0$ as assumed iff $d E V / d w _ { o } \big | _ { w _ { o } ^ { * } = 0 } < d E V / d w _ { c } \big | _ { w _ { o } ^ { * } = 0 } .$ Because $p _ { c } ^ { \prime * } > 0$ and $p _ { o } ^ { \prime * } < 0 ,$

$$
\left. \frac {d E V}{d w _ {o}} \right| _ {w _ {o} ^ {*} = 0} <   \left. \frac {d E V}{d w _ {c}} \right| _ {w _ {o} ^ {*} = 0} \quad \text { iff } \quad \left. \frac {d E V}{d w _ {c}} \right| _ {w _ {o} ^ {*} = 0} > \frac {p _ {c} ^ {*} p _ {o} ^ {\prime *} - p _ {o} ^ {\prime *} p _ {c} ^ {\prime *}}{p _ {c} ^ {\prime *} - p _ {o} ^ {\prime *}}.
$$

In the above condition, note that the numerator is negative and the denominator is positive. Thus, the choice of $w _ { c } ^ { * } > 0$ by the firm is optimal even when $d E V / d w _ { c } | _ { w _ { o } = 0 } < 0 .$ This shows that the IR constraint forces the firm to choose bonuses that would otherwise be suboptimal.

Using Equation (14), $d E V / d w _ { c }$ can be rewritten as $( M R ^ { * } -$ $p _ { c } ^ { \prime * } w _ { c } ^ { * } ) ( d x ^ { * } / d w _ { c } ) - p _ { c } ^ { * }$ . Further, substituting $w _ { c } ^ { * } = ( u - Q ^ { * } ) / p _ { c } ^ { * }$ and using Lemma 2 to substitute for $d x ^ { * } / d w _ { c } | _ { w _ { o } ^ { * } = 0 } ,$ , we find that $w _ { c } ^ { * } = ( u - Q ^ { * } ) / p _ { c } ^ { * }$ and $w _ { o } ^ { * } = 0$ is a consistent solution iff

$$
M R ^ {*} <   - \frac {(1 - p _ {c} ^ {*} p _ {o} ^ {*}) A ^ {*}}{1 - p _ {c} ^ {\prime *} / p _ {o} ^ {\prime *}} - \frac {(u - Q ^ {*})}{p _ {o} ^ {*}} \left(p _ {o} ^ {\prime *} - \frac {(p _ {o} ^ {*} - p _ {c} ^ {*}) p _ {o} ^ {\prime \prime *}}{p _ {o} ^ {\prime *} - p _ {c} ^ {\prime *}}\right).
$$

The proof for Case II is similar.

The proof for Case III also proceeds along similar lines, and the requirement for both $w _ { c } ^ { * } > 0$ and $w _ { o } ^ { * } > 0$ is that $d E V / d w _ { o } \bar { | } _ { w _ { c } ^ { * } , w _ { o } ^ { * } } = d E V / d w _ { c } | _ { w _ { c } ^ { * } , w _ { o } ^ { * } }$ . Using this, we get the condition specified in Case III.

Though we cannot prove that the solutions specified by all three cases must exist because of the generality of our specifications and the algebraic complexity of the expressions, the illustrations in the main body of the paper show that these may indeed exist.

Lemma 5. The effort choice in equilibrium when the IR constraint is not binding and $w _ { c } ^ { * } > 0 , \ w _ { o } ^ { * } = 0$ is lower than the socially optimal effort division.

Because $w _ { o } ^ { * } = 0 ,$ , the firm picks ${ w } _ { c } ^ { * }$ to maximize $E V ,$ i.e., $\boldsymbol { w } _ { c } ^ { * }$ is obtained by solving $d E V / d w _ { c } = 0$ . Now, $d E V / d w _ { c } =$ $E V _ { t } ^ { \prime } ( x ^ { * } ) ( d x ^ { * } / d w _ { c } ) ^ { } - p _ { c } ^ { * } .$ , where $x ^ { * }$ is the incentive compatible effort choice of the programmer. From Lemma $^ { 2 , }$ we know that $d x ^ { * } / d w _ { c } > 0$ . Therefore, we must have $E V _ { t } ^ { \prime } ( x ^ { * } ) > 0$ at the equilibrium effort choice.

Lemma 6. The effort choice in equilibrium when the IR constraint is not binding and $w _ { o } ^ { * } > 0 , \ w _ { c } ^ { * } = 0$ is higher than the socially optimal effort division.

The proof of Lemma 6 is similar to that of Lemma 5 and is omitted here.

## References

Arrow, K. J. 1962. The economic implications of learning by doing. Rev. Econom. Stud. 29(3) 155–173.

Becker, G. S. 1962. Investment in human capital: A theoretical anal ysis. J. Political Econom. 40 9–49.

Blaug, M. 1976. The empirical status of human capital theory: A slightly jaundiced survey. J. Econom. Literature 16 827–855.

Boh, W. F., S. A. Slaughter, J. A. Espinosa. 2007. Learning from experience in software development: A multilevel analysis. Man agement Sci. 53(8) 1315–1331.

Breshnahan, T. F., E. Brynjolfsson, L. M. Hitt. 2002. Information technology, workplace reorganization, and the demand for skilled labor: Firm-level evidence. Quart. J. Econom. 117(1) 339-376.

Caroli, E., J. V. Reenen. 2001. Skill based organizational change? Evidence from a panel of British and French establishments. Quart. J. Econom. 116(4) 1449–1492.

Cartensen, V. 2002. The from-Tayloristic-to-holistic-organization model from an empirical perspective. Discussion paper 256, University of Hannover, Department of Economics, Institute for Quantitative Economic Research, Hannover, Germany.

Fink, M. 2002. The Business and Economics of Linux and Open Source. Prentice Hall PTR, Indianapolis.

Gibbons, R., K. J. Murphy. 1992. Optimal incentive contracts in the presence of career concerns: Theory and evidence. J. Political Econom. 100(3) 468–504.

Goleman, D. 1998. Working with Emotional Intelligence. Bantam Books, New York

Hann, I. H., J. Roberts, S. Slaughter, R. Fielding. 2006. Understanding the motivations, participation, and performance of open-source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7) 984–999.

Hars, A., S. Ou. 2002. Working for free? Motivations for participating in open source projects. Internat. J. Electronic Commerce 6(3) 25–39.

Hertel, G., S. Niedner, S. Herrmann. 2003. Motivation of software developers in open source projects: An Internet based survey of contributors to the Linux kernel. Res. Policy 32 1159–1177.

Holmstrom, B. 1999. Managerial incentive problems: A dynamic perspective. Rev. Econom. Stud. 66(1) 169–182.

Johnson, J. P. 2002. Open source software: Private provision of a public good. J. Econom. Management Strategy 11(4) 637–662.

Killingsworth, M. R. 1982. “Learning by doing” and “investment in training”: A synthesis of two “rival” models of the life cycle. Rev. Econom. Stud. 49(2) 263–271.

Kirsch, L. J. 1996. The management of complex tasks in organizations: Controlling the systems development process. Organ. Sci. 7 1–21.

Lakhani, K. R., E. von Hippel. 2003. How open source software works: “Free” user-to-user assistance. Res. Policy 32 923–943.

Lakhani, K. R., R. G. Wolf. 2005. Perspectives on Free and Open Source Software. MIT Press, Cambridge, MA.

Lal, R., V. Srinivasan. 1993. Compensation plans for single and multiproduct salesforces: An application of the Holmstrom-Milgrom model. Management Sci. 39(7) 777–793.

Lerner, J., J. Tirole. 2002. Some simple economics of open source. J. Indust. Econom. 50(2) 197–234.

Lindbeck, A., D. J. Snower. 1996. Reorganization of firms and labormarket inequality. Amer. Econom. Rev. 86(2) 315–321.

Lindbeck, A., D. J. Snower. 2000. Multitask learning and the reorganization of work: From Tayloristic to holistic organization. J. Labor Econom. 18(3) 353–376.

Menon, T., J. Pfeffer. 2003. Valuing internal vs. external knowledge: Explaining the preference for outsiders. Management Sci. 49(4) 497–513.

Milbourn, T. T., R. R. Shockley, A. V. Thakor. 2001. Managerial career concerns and investments in information. RAND J. Econom. 32(2) 334–351.

Moody, G. 2002. Rebel Code: Inside Linux and the Open Source Revolution. Perseus Press, New York.

Neal, D. 1995. Industry specific human capital: Evidence from displaced workers. J. Labor Econom. 13(4) 653–677.

New York Times Magazine. 1999. The search engine. (October 10) 667.

Pautrel, X. 2004. A note on multitask learning and the reorganization of work. Econom. Bull. 10(5) 1–6.

Raymond, E. S. 2001. The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary. O’Reilley Publications, Sebastopol, CA.

Reagans, R., L. Argote, D. Brooks. 2005. Individual experience and experience working together: Predicting learning rates from knowing who knows what and knowing how to work together. Management Sci. 51(6) 869–881.

Schilling, M. A., P. Vidal, R. E. Polyhart, A. Marangoni. 2003. Learning by doing something else: Variation, relatedness, and the learning curve. Management Sci. 49(1) 39–56.

Sturman, M. C., K. Walsh, R. A. Cheramine. 2008. The value of human capital specificity versus transferability. J. Management 34(2) 290–316.

UNU-MERIT. 2006. Study on the economic impact of open source software on innovation and the competitiveness of the information and communication technologies (ICT) sector in the EU. http://ec.europa.eu/enterprise/sectors/ict/files/2006-11- 20-flossimpact\_en.pdf.

von Krogh, G., S. Spaeth, K. R. Lakhani. 2003. Community, joining, and specialization in open source software innovation: A case study. Res. Policy 32(7) 1217–1241.

Wayner, P. 2000. Free For All: How Linux and the Free Software Movement Undercut the High-Tech Titans. HarperBusiness, New York.

Weiss, A. 1995. Human capital vs. signaling explanation of wages. J. Econom. Perspect. 9 133–154.
