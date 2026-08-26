---
otero_id: 28422
otero_key: "CWQPNNWM"
title: "The Death of a Technical Skill"
authors: "John J. Horton; Prasanna Tambe"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0709"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# The Death of a Technical Skill

John J. Horton,<sup>a,b</sup> Prasanna Tambe<sup>c,</sup>\*

<sup>a</sup> Sloan School of Management, Massachusetts Institute of Technology, Cambridge, Massachusetts 02142; <sup>b</sup> National Bureau of Economic Research, Cambridge, Massachusetts 02138; <sup>c</sup> Wharton School, University of Pennsylvania, Philadelphia, Pennsylvania 19104 \*Corresponding author

Contact: john.joseph.horton@gmail.com, https://orcid.org/0000-0001-5426-0156 (JJH); tambe@upenn.edu, https://orcid.org/0000-0002-5308-1057 (PT)

Received: December 22, 2022 Revised: December 3, 2023; August 30, 2024; January 7, 2025 Accepted: January 18, 2025 Published Online in Articles in Advance: March 19, 2025

https://doi.org/10.1287/isre.2022.0709

Copyright: © 2025 INFORMS

Abstract. We analyze how the decline of a technology affects online labor market dynamics. We evaluate the effects of Steve Jobs’ announcement that Apple would no longer support Adobe Flash—a popular set of tools for creating internet applications. Despite a precipitous decline in Flash demand, there is no evidence of a reduction in Flash wages on this platform because the supply response was rapid, particularly among younger developers with readily available “fallback” skills. The key to this rapid adjustment was that the long-run value of the skills that developers expected to acquire on the job acted as a form of nonwage compensation that suddenly fell in its expected value, motivating many developers to switch to other technologies, even though wages themselves did not fall. Our findings underscore how the rise and fall of technologies influences matching in online markets and help to explain (i) why technological obsolescence leaves fewer, older participants in a skill and (ii) why technologies in decline can be contemporaneously characterized by wages that stay flat or even rise in a market setting. Management and policy implications are discussed.

History: Bin Gu, Senior Editor; Mohammad Rahman, Associate Editor. Funding: This work was supported by the W.E. Upjohn Institute for Employment Research and the Alfred P. Sloan Foundation [Grant G-2012-10-23]. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2022.0709.

Keywords: online labor markets • technical skills • IT workforce • human capital • technology adoption

## 1. Introduction

Tech workers often consider a variety of nonwage factors when deciding where to allocate services. For example, information technology (IT) workers are known to place considerable emphasis on whether projects will allow them to hone their skills for future work (Barley and Kunda 2011). Projects using skills that will be “hot” in the future, therefore, may offer greater value to technical workers than those based on skills that do not have a promising future, and the waxing and waning of technical skills—a defining feature of IT markets— could therefore have important implications for market dynamics.

We examine how changes to the future value of a technical skill, which can be viewed as an important nonwage component of a worker’s compensation, can impact where workers who participate on online markets choose to supply their services. Online markets merit focus because they have witnessed a surge in relevance in recent years and provide an efficient channel for employers to source talent from across the globe.<sup>1</sup> These marketplaces provide value that extends beyond cost arbitrage. For instance, managers often cite access to skills as a key incentive for hiring workers on these platforms (e.g., see Pofeldt 2020). Online markets accounted for over one trillion dollars in revenue in 2023, and an estimated 68% of Americans engaged in freelance work (Dua et al. 2022). The World Bank estimated that the gig economy could comprise as much as 12% of the global labor market, with most of this activity being transacted on smaller, regional platforms (Tapia et al. 2024). These markets also hold special importance because they can provide opportunities for disenfranchised workers, such as those from developing economies and for women and workers with little or no experience, to participate in the labor market.

Beyond market participation, understanding how online workers respond to changes in the future value of technical skills has important implications for corpo rate managers who engage with online labor markets. The relationship between technology choice and worker matching is particularly salient in online contexts, where employers have limited means beyond wages to attract talent. The opportunity to gain valuable skills through project work shapes both the available labor supply and market behavior during technological decline.

These dynamics are especially relevant given the noted challenges of realizing effective matching on these platforms (Cullen and Farronato 2021). These challenges are due in part to the skill intensity of the matching process and the rapid volatility on both sides of the market. These same attributes, however, make these platforms an attractive setting in which to evaluate how developers respond to changes in the value of skills. Workers on these platforms are repeatedly faced with options about which projects to pursue, bidding and switching are readily observed, and participants face few frictions when switching technologies. Within workers, separate wages are observed for each technical skill in which they work. Moreover, unlike offline markets, where employers compete on status, location, opportunity, benefits, and other attributes, employers on online labor markets only compete for talent on a small number of dimensions, including wages and the value of the skills gained when working on a project.

The value of technical skills can change slowly, though, so it can be challenging to demarcate when workers’ expectations about the value of working in a skill begin to shift. To meet this challenge, we identify a negative adverse shock to a skill where expectations about the future value of working in the technology were clearly and irrevocably put on a path to decline. The technology we examine is Adobe Flash—a oncepopular collection of software tools used for creating multimedia games, advertisements, and applications delivered over the internet. The inflection point in Flash demand is clear and well documented, marked not by the emergence of a superior technology, but rather by a business decision made by Apple. On Apri 29, 2010, Steve Jobs—the chief executive officer (CEO) of Apple at the time—published an open letter entitled “Thoughts on Flash” (TOF) (https://web.archive.org/ web/20170615060422/https://www.apple.com/hotnews/ thoughtson-flash/), which announced that Apple would no longer support Flash on iOS devices such as the iPhone, iPod, and iPad, an announcement that was widely covered by the news media.<sup>2</sup> This announcement was viewed by developers as being a turning point in the market for Flash development. Our data suggest it was an effective—albeit slow-acting— poison, and as we illustrate, the decline in Flash can be observed in a variety of data sources. This decline forced developers to consider whether to continue acquiring experience in the skill given the decline in its value for future work.

Our main analysis is based on archival data from an online technical labor market. Before analyzing this market activity, however, we discuss survey results collected from 186 former Flash developers still active on this platform to understand their perspectives on the decline of the Flash market. Their responses indicated that developers were keenly aware of the declining fortunes of Flash after the Apple announcement. They adjusted to changes in this market by switching to new skills they acquired by learning them on the job at other projects, often at a discounted wage because they were novices at the new skill. These adjustment choices generate testable implications about how technological decline affects IT workers’ labor supply choices.

To test these predictions, we construct an individuallevel, monthly, nine-year (2007–2016) panel of workers specializing in Flash prior to TOF. We use a differencein-differences (DID) matching design, where TOF indicates the timing of the shock and Flash developers are the treated group. To form our control group, we conduct a granular match on observables between our Flash developers and developers on the platform who were not specialized in Flash. We find that Flashspecialized workers abandoned Flash even as wages remained steady which is consistent with the view that the nonwage component of the value of Flash projects became less attractive to developers on this platform. When aggregated to the market level, there is no evidence employers were inundated with applications from out-of-work Flash programmers—the number of applicants per opening remained roughly constant. There was no increase in the likelihood that a Flash opening was filled, nor was there a reduction in the wages paid to hire Flash developers.

There was little observed reduction in Flash wages because the negative demand shock was offset by a rapid supply shift as workers responded to a decline in the future value of the skill. Workers specializing in Flash prior to TOF increased job search intensity—submitting more applications per month—and shifted their job search focus. Younger, less-specialized workers abandoned Flash most quickly, as did workers who had skills to which they could easily pivot. Younger workers demanded a compensating differential to work with the dying technology to offset their opportunity costs, whereas older workers, who cared less about the long run value of the skill, did not. In sum, our analysis reveals that because developers are sensitive to the longrun value of the skills they acquire on the job, technological obsolescence affects how employers and contractors match on online markets. Our findings are consistent with the observation that wages can remain steady for a technology as demand falls, a fact that has been observed in offline markets for programming languages like Cobol and is explained by our theory and evidence but cannot be explained by models that do not account for the nature of IT skill accumulation.<sup>3</sup>

These effects vary by worker attributes. Workers who were highly specialized in Flash were more likely to stay with the technology. We find that younger workers, who had longer career horizons to consider, switched quickly. Workers who had complementary skills in their technical portfolio, like HTML5—a popular successor to Flash for web projects—experienced better outcomes. We also find that workers in countries with a lower standard of living (SOLV) were slightly more likely to lower the number of Flash hours they provided to the market, but these effects are not large. Age and skill were more important factors in explaining how workers responded to this negative shock.

We also report results from a battery of robustness tests. The market adjustments we observe are coincident with the TOF announcement itself—online workers were not turning away from Flash prior to this announcement—and we show that our estimates are insensitive to a number of different estimator choices. Finally, the TOF post made by Steve Jobs is a convenient empirical device, but like any technical skill, Flash has unique characteristics, so we evaluate whether our findings generalize to observed changes in online demand for other technical skills. As with Flash, our analysis of other technical skills corroborates the argument that expectations about the future value of skills shifts interpretation of market activity away from a basis upon which wages alone provide a trustworthy signal of market dynamics.

Our findings principally contribute to the literature analyzing factors affecting supply and demand in online markets (Chen and Horton 2016, Hong et al. 2016, Kokkodis and Ipeirotis 2016, Stanton and Thomas 2016, Huang et al. 2020, Kokkodis 2023, Liang et al. 2023). We contribute to this literature by demonstrating how the decline of technologies influences market matching. Employers on these sites have only a few levers they can use to compete for talent, so understanding how technology choice matters is important. Furthermore, interest in how workers adapt in online markets has been attracting greater interest as new technologies, like generative artificial intelligence tools, threaten to accelerate skill obsolescence on these platforms. In that context, as well, important questions arise about how workers might fare if they invest in a skill that subsequently loses value. This can inform discussions of how workers who rely on these markets for income will adjust to coming waves of technological change.

## 2. Theoretical Background and Survey 2.1. Apple’s Announcement

On April 29, 2010, Apple CEO Steve Jobs published an open letter, “Thoughts on Flash,” announcing Apple’s decision to no longer support Flash applications on the iPhone, iPad, or iPod Touch. Although Jobs claimed that technical considerations were driving Apple’s announcement, it was widely believed that these arguments were a pretext and that Apple wanted to withdraw support from Flash because it was unwilling to concede so much control over the user interface and device performance to third parties (see, e.g., Rayburn 2010, Richmond 2010). Tony Bradley (2010), of PC World, wrote:

It boils down to Apple wanting to maintain tight, proprietary control over app development for the iPhone and iPad, and not wanting to share the pie. It also seems suspicious given Apple’s foray into mobile advertising with the iAd platform competing directly with the fairly ubiquitous Flash-based ads.

In the years following Jobs’ letter, the popularity of Flash waned considerably, though the effect was not immediate nor universally anticipated: on August 26, 2010, the Wall Street Journal touted rising demand for Flash workers—a “trend” that seems to have had no empirical basis (Tam 2010). Apple’s decision may have also catalyzed other changes in the industry that hastened the demise of Flash. For example, in late 2011, it was announced that Flash would no longer be natively supported on the Android operating system, starting with the “Jellybean” release. Although still used for some applications today, the decline continued, and in July 25, 2017, Adobe published a blog post announcing that they would remove all support for Flash by the end of 2020.

The decline in Flash that occurred after Jobs announcement can be readily observed in a variety of data sources. Perhaps the best contemporary indicators of software developer interest in a given technol ogy are the questions being asked on Stack Overflow, an enormously popular programming question-andanswer (Q&A) site. The left facet of Figure 1 shows the volume of questions per month for Flash and for comparison, a basket of popular IT skills, all normalized to one in the TOF month. HTML is a markup language for making websites; CSS is a language for styling websites and controlling their appearance; Java is a general-purpose programming language; whereas PHP is another programming language frequently used for server-side scripting. The y-axis is on a log scale. The numbers of questions about Flash and our chosen basket of skills are growing more or less in lockstep pre-TOF, reflecting growth in the Q&A platform and the wider IT industry, but after TOF, Flash shows a clear absolute decline. There is some delay in this drop, likely reflect ing the diffusion of the news of Apple’s plans as well as the time needed to complete already-planned projects.

The decline in Flash is also readily apparent in the longitudinal data from the online labor market we analyze in this study: the right facet of Figure 1 plots the number of job openings posted per month requiring Flash skills and for those requiring PHP (one of the “basket skills” from the left facet of Figure 1). Both Flash and PHP are normalized to one for the TOF month. As with the Stack Overflow data, both Flash and PHP move closely together pre-TOF. Following TOF, the number of Flash job openings declined relative to PHP, falling by more than 80% between 2010 and 2015.<sup>4</sup>

Today, Flash is a moribund technology confined to a small number of niche applications. Even legacy uses of Flash are becoming inoperable soon for most users, as modern browsers are beginning to block Flash applications by default—a development ghoulishly reported by the tech blog Gizmodo under the heading “Google sticks another knife in Flash’s Corpse” (McKay 2019).

Figure 1. (Color online) The Decline of Flash on Two Platforms  
![](/api/attachments/CWQPNNWM/fulltext/images/77b44e0a2c89f337f7ef1cc544fb54c9cdf3278094faf30746d7d4bfce89705a.jpg)  
Monthly observations (vertical line is “Thoughts on Flash” day)  
Notes. The left facet plots number of questions, by technical skill, posted on Stack Overflow between 2008 and 2016. The right facet shows the number of job posts requiring Flash or PHP in an online labor market. All series are normalized to have a value of one in the post-TOF period The unit of observation is the month.

## 2.2. Technological Decline and Market Dynamics

Workers should abandon a dying skill when it becomes profitable to do so. We consider a simplified setting where workers maximize the net present value of taking a project which consists of (i) the wage payment and (ii) a nonwage component, which is the net present value of the skills acquired while working on the project. The latter component is what differentiates our online, technical context from occupational contexts where on-the-job learning plays a less important role, and where wages alone may be a more trustworthy signal of market demand.

The value of the nonwage component of a project varies across workers. Inexperienced workers gain significant human capital when working in a new skill; experienced workers learn less. The value that a worker derives from working in a technical skill will be lower if (a) the worker is experienced in the technology, (b) demand for the skill is expected to fall in the future, or (c) the worker will exit the market soon. Young, inexperienced contractors working in a skill that is gaining popularity have the most to gain from working in a new skill and may even accept a lower wage—that is, a compensating differential—if they expect to learn a lot.

These considerations suggest that technological obsolescence can affect how workers choose projects. As a skill declines, the nonwage value of a project can fall if workers expect less work in the technology in the future. The market can adjust in three ways: (1) some new market entrants continue to take projects in the dying skill; (2) no entrants choose the dying skill, but workers in the market stay with the dying skill; and (3)

even workers already in the market exit the dying skill. The likelihood of each outcome depends on the size of the negative demand shock relative to the supply curve of incumbent workers. As the future value of a skil falls, workers specialized in it will switch to new skills at a greater rate than comparable workers.

Which workers switch? Ceteris paribus, workers who are very productive with a skill and who command a high wage face a higher cost when switching to a new skill. For these workers, a skill must lose greater value to compel them to switch. That is, workers with significant human capital in a dying skill should aban don it less quickly.

Yet, even holding a worker’s human capital fixed, the future value of the skill might vary among workers. Older workers who will exit the market soon may not be too negatively affected by a decline in the value of any skills they work in and may not find it worthwhile to switch to a new skill, but younger workers who expect to remain in the market for many periods may not want to invest in a dying skill unless they earn higher offsetting wages. These younger workers have a longer horizon over which to earn back investments they make in a new technical skill. Therefore, younger workers may choose not to work in the dying skill or may seek a compensating wage differential to offset the opportunity cost they incur when spending their time working in the dying skill.

Worker’s existing skill endowments may also affect their choices, because workers who have skills that substitute for or complement the dying skill will abandon it more or less quickly, respectively. For instance, employers who want to switch from an old technology standard to a new technology standard may prefer workers familiar with both standards because they can help with conversion tasks, or workers with skills that complement the dying skill may stay with the dying skill longer. Alternatively, it could be less costly for IT workers to switch to new skills if they are already equally productive with other skills.<sup>5</sup>

Finally, although workers online can bid for the same online projects no matter their location, they each face different offline opportunities. The decline of a technical skills likely also lowers the demand for the skill in offline markets, and how much this decline impacts workers depends on how important the skill is in their local labor market. If it significantly reduces offline demand in the local market, it can drive excess supply from the local market online. If the platform provides higher levels of income share in some markets (e.g., in less-developed countries), participants from these markets may react differently than workers for whom this platform only provides supplementary income. A change in the geographic distribution of contractors who choose to work in a skill on an online platform can impact equilibrium wages and other outcomes if there are wage disparities arising from differences in the quality or variety of services provided by workers in different countries. Therefore, when a technology declines, market dynamics could be affected by how workers residing in different markets choose whether to spend more or less of their time on the skill.

## 2.3. Survey Evidence on the Perceptions and Adjustments of Flash Developers

Before evaluating theoretical predictions in the market data, we summarize results from a survey of 186 Flash workers active on Apple’s platform at the time of TOF.

The full text of the survey questions is provided in Online Appendix B. These survey results describe the perceptions and motivations of developers as they adjusted to changes in the Flash market.

Surveyed workers perceived Flash’s dim future contemporaneously and felt a need to switch skills. Many made note of the Jobs announcement when describing a decline in postings for Flash skills, and many respondents mentioned Apple’s role without prompting:

Since Steve Jobs’ infamous speech about Flash, there has been a decline in the use of Flash across the web.

Steve jobs wrote a nasty little hit piece before he died and that really was a turning point.

The actions they took in response to this change are depicted in Figure 2(a). Seventy percent of developers reported switching mostly or entirely to other skills. Figure 2(b) shows that among workers who switched skills, most chose new skills rather than falling back to existing skills. Figure 2(c) illustrates that respondents said that their primary adjustment strategy when switching to new skills was taking projects in the skills they wished to learn. Selecting projects to build human capital was a key theme of the responses, with survey respondents recommending that developers “bid low to build up experience in that technology” and that it was “a pretty good deal to get paid anything at all if you’re learning a bunch while you $\mathrm { g o . } ^ { \prime \prime }$ In our quantitative analysis of the survey response data, an “earn-whileyou-learn” strategy (O’Mahony and Bechky 2006) was the most important method of acquiring new skills and was regarded as more important than more traditional approaches like reading books or taking classes.

Figure 2. (Color online) Adjustment Strategies Used by Developers—Survey Evidence  
(a) Adjustment to Flash market changes  
![](/api/attachments/CWQPNNWM/fulltext/images/56fa48c499d951939e6934a942cfbbd6b8a9582200e130be0de913f6bbfcb99b.jpg)

(c) How workers learn new skills  
![](/api/attachments/CWQPNNWM/fulltext/images/5ddedddf9f310fadc083a519cbf3555a77151e1a7be2cbc78e1b37ea8f6943c2.jpg)

(b) Strategies when switching to new skills  
![](/api/attachments/CWQPNNWM/fulltext/images/52b5340db41b44c3a0f6bd55c408d7e4fdbb57c01a1c258481be4980ea9dfb39.jpg)

(d) Bidding for projects requiring new skills  
![](/api/attachments/CWQPNNWM/fulltext/images/b74ce9a8e23ae90d5d6c61b23f1e259372dbd8157f5fa21242b3a766502f918f.jpg)  
Notes. These figures summarize survey responses to questions about how developers adjusted to the decline in the Flash market. Facet (a) show how developers adjusted to the market change. Facet (b) illustrates how developers decided which skills to switch to. Facet (c) shows what resources developers used when trying to learn new skills. Facet (d) illustrates how workers adjust their bidding strategies when pursuing pro iects based in new skills

The wage implications of this earn-while-you-learn strategy are reflected in Figure 2(d), which shows that surveyed workers reported a willingness to lower rates to obtain work in new skills, which is consistent with the compensating differential arguments put forth in the prior section. This margin of adjustment has been reported in other contexts (Bessen 2003) but might be particularly important for IT skills, where there is typically no additional physical capital required to acquire skills and change outpaces formal education (Ang et al. 2002, O’Mahony and Bechky 2006, Mithas and Krishnan 2008, Barley and Kunda 2011, Bessen 2016). With these survey results providing initial evidence for our arguments on how workers evaluate projects when facing technical change, we now turn toward the market data to test our theoretical predictions.

## 3. Empirical Setting

## 3.1. Description of the Online Labor Market

Our primary empirical setting for studying the demise of Flash is an online labor market for technical contract labor. This is one of the largest markets for gig work in the world, with millions of clients and freelancers. Freelancers from the United States comprise about 40% of the freelance base, followed by India and the Philippines. Together, these three countries comprise about 70% of the freelancer base for the site. Employers are more heavily weighted toward the United States, with about 66% being U.S. based.

The largest single category of work on this platform is “Web, mobile, and software development” (34%) and most Flash projects fall within this category. Workers spend significant time on this market, although whether this is a full-time or part-time job for them varies by worker. The distribution of hours worked is consistent with some workers using the platform for part-time work, whereas others work close to full time. The distribution of hourly wages on the platform likely tracks what is available offline, with some premium due to the flexibility afforded online, because a large gap in the returns to an online/offline hour of work would tend to create a financial arbitrage opportunity that workers would quickly exploit—see Horton (2021). In 2022, the average hourly pay on the platform was \$21.80, which would have been about \$15.50 in 2010 dollars and reflects the fact that these prices are set in the global market. In 2023, the pay range for HTML5, a key successor technology to Flash, was \$15 to \$30,<sup>6</sup> which would have been about \$11 to \$21 when represented in 2010 dollars, the year of the TOF announcement. The average Flash wage on the platform during our sample period was about \$13 per hour, which is within this range.

On this market, employers self-categorize job openings depending on the nature of the work. Employers also label each job opening with up to 10 skills, which must match a “controlled vocabulary” of skills maintained by the platform. The controlled vocabulary of skills contains several thousand distinct skills, and new skills are frequently added. As expected, given the platform’s focus on technical work, many of the skills are programming languages, tools, and software frameworks, for example, Flash, PHP, C, HTML, etc. The extensive skill labeling on the platform allows us to characterize a worker’s skill focus—particularly whether they used Flash—as well as whether there is a change in skill focus. We take all jobs that workers had prior to TOF and compute a measure based on skill weights. For example, if the worker had completed one project that used skill A and B and another that used B and ${ \dot { \mathsf { C } } } ,$ we would compute their share vector as $( 1 / 4 , 1 / 2 , 1 / 4 )$ for $( A , B , C )$ . As with most job listings, the listings on this platform do not provide information about the intensity of skills used in different jobs. As we observe new applications being submitted, we can characterize how “close” an applied-to job is to a worker’s skill history by computing the cosine similarity between that job and the worker’s skill weight vector. We call this term frequency–based cosine similarity metric “application similarity.” A lower dot product means a worker is applying to jobs further “away” from their historical focus.

The skills added to a listing by an employer are used by workers to find jobs that match their skills. Wouldbe applicants use these skills—as well as the category of the job opening—to decide which jobs to apply to. Workers also list skills in their own profiles. Employers can see the details of past jobs completed by the appli cant, which are labeled with the skills selected by the original employer. Employers can solicit applications from workers or workers can apply to openings they find. For hourly jobs such as those we study here, workers bid hourly rates for project work. Therefore, it is the bidding choices of the workers, rather than the posting choices of employers, that determine whether wages rise or fall for a particular skill. Employers then screen applicants. If a hire is made, the wage and number of hours worked are observed. On the platform, hours worked and earnings are measured essentially without error, as workers use a kind of digital punch clock to record hours, and payment is transacted through the platform.<sup>8</sup>

## 3.2. Construction of a Matched Sample

Our empirical goal is to compare the choices and trajectories of workers with Flash experience with a counterfactual group of workers who were not specialized in Flash. Workers are not randomly assigned to technologies though, and some workers may have foreseen the declining fortunes of Flash even before TOF and chosen to switch to other skills. Moreover, the market is divided into technical and nontechnical work, with large associated differences in hourly earnings, which mixes workers that are not truly comparable. Therefore, to construct our comparison group, we use a matching approach to construct a sample of comparable workers, and then proceed with a standard panel analysis (Borusyak and Jaravel 2016).

Our panel window, drawn to include periods before and after TOF, extends from 40 months before the 2010 TOF announcement to 70 months after for a total sample period spanning over nine years. Before matching, the average worker in our sample sent 181 applications and delivered a total of 684 billed hours. They worked in 34 different periods (months) and earned an average hourly wage of slightly over \$10.

Our preferred specification is to restrict the panel to Flash workers who (a) have at least 1% of their pre-TOF hours in Flash, (b) have at least 40 hours of platform work in total, and (c) work in at least two distinct months prior to TOF. We truncate the end of the panel by one quarter, as some panel measures are “incomplete” near the end of our data. We also truncate the start of the panel to 40 months before TOF because this corresponds to the true launch of the platform (nearly the entire sample joined the platform after this date). We restrict hourly wages to be positive and less than \$100/hour—this removes a very small number of observations that likely reflect users who were not on bona fide hourly contracts but were instead using the time-tracking features of the platform or were using lump-sum payments but billed them as hours worked.

Our baseline identifying assumption is that, conditional upon worker and time fixed effects (FEs), Flash workers are observationally equivalent to workers in the control group.<sup>9</sup> This assumption is analogous to the one made in the literature on the effects of job loss (Jacobson et al. 1993, von Wachter et al. 2009, Couch and Placzek 2010). In our setting, because we have a measure of Flash concentration, we can allow effects to differ based on how focused workers were on Flash pre-TOF. This is in contrast to the displacement literature where job loss is binary.

Ideally, for a sample of counterfactual workers, all that should differ is exposure to the “treatment” which is having a technical skill that is placed on a path toward zero demand. To construct the matched sample, we take all workers active on the platform at the time of TOF, with “active” defined as having worked at least 40 hours on platform before TOF. We indicate workers with Flash experience with a binary measure, ANYFLASH. We also record the fraction of total hours worked that were in Flash, which we denote by FRAC FLASH. The mean value for FRACFLASH is about 25%.<sup>10</sup>

We match Flash workers to a control group of non-Flash workers (those with no pre-TOF Flash experience).

For matching, we construct a cross-sectional data set by computing worker-level summary statistics at the time of TOF, including (1) platform tenure, (2) average wage, (3) cumulative hours worked, (4) cumulative earnings, and (5) cumulative number of applications sent.<sup>11</sup> We break up the matching into quartiles by pre-TOF Flash focus. Our estimator implements a one-to-one match using genetic matching as implemented in the Matching package in R (Sekhon 2011). Before matching, there are 1,325 contractors in the treated group and 17,725 in the control group after limiting the sample to having worked the minimum number of hours (40) and working in at least two separate periods. After matching, we are left with 1,100 contractors in the treated group and 1,097 contractors in the control group. Table A.7 in the Online Appendix makes clear that we obtain excellent covariate balance.<sup>12</sup>

## 4. Descriptive Evidence on Changes in the Market for Flash Skills

Before analyzing our matched sample, we plot Flash market attributes over time to illustrate features of its decline. For illustrative purposes, we compare job openings for Flash with those for PHP, a popular server-side scripting language used for creating web applications (e.g., Facebook was originally written in PHP). PHP is an attractive comparison technology because it was popular at the start of our time series and continued to be widely used up until the end of the panel.<sup>13</sup> As not everything of interest can be measured at the job opening level, we also construct supply-side measures that allow us to characterize the flow in and out of Flash and the number of hours worked per active worker.

## 4.1. Attributes of Posted Job Openings

Monthly measures at the job opening level are plotted in Figure 3. These measures are scaled such that they have a mean value of zero for the period before TOF for both Flash and PHP. In the top-left facet of the figure, the log number of openings is plotted, and it recapitulates what we observed in Figure 1. There is a clear decline in Flash openings following TOF. The facet at top right is the mean of the log of the number of applications per opening. The number of applications submitted for each PHP and Flash opening track very closely even post TOF. There is no evidence that Flash jobs were oversubscribed by out-of-work Flash specialists despite a fall in demand.

Despite no apparent post-TOF change in the numbers of applicants, it is possible that Flash workers may have started bidding less, allowing more openings to be “filled”—defined as the employer hiring at least one worker. This does not appear to be the case—in the bottom left facet, the measure is the fraction of filled job openings, and, if anything, the fill rate for Flash jobs seems to decline relative to PHP post-TOF. Again, this is the opposite of what we would expect if the decline of the Flash technology was interpreted primarily as a negative demand shock.

Figure 3. (Color online) Attributes of Flash and PHP Markets Over Time on the Platform  
![](/api/attachments/CWQPNNWM/fulltext/images/f72fb8dbc569dbfefbffa694058497eb28486aaa1f811cfb27e21f16f6075371.jpg)  
Notes. This figure shows a variety of per-month attributes of job openings that require either Flash or PHP, a comparison skill. The vertica dashed line indicates TOF. Average wage is reported in nominal U.S. dollars. All values are scaled such that they have zero mean in the pre-TOF period.

The conjecture that Flash workers started bidding less also does not seem to be borne out, as measured by wages of the hired worker. In the bottom right facet, we can see that average (demeaned) wages stay about the same relative to PHP. Near the end of the data, there are not many observations, and so the estimates of the hourly earnings rate grows imprecise.

## 4.2. Attributes of Workers

For our worker analyses, we construct a monthly panel of Flash and non-Flash workers where the latter set is no longer restricted to PHP. There are 324,097 workers in the panel. Of these, the number that were active before TOF and had some Flash experience is 1,871. Flash workers are defined as those that had earned some amount of money on a Flash project before TOF. By TOF, they had collectively worked 248,491 hours on Flash projects.

We plotted the number of job openings requiring Flash in Figure 3, but not the quantity of Flash hours delivered. In the top facet of Figure 4(a), we see that the total hours worked peaks at the time of TOF and then declines. In the middle facet, the output is the total number of Flash workers active that month, with “active” defined as working at least some number of hours. It also peaks near TOF, but it seems to decline more steeply compared with the total-hours-worked plot.

A greater relative decline in numbers of workers than in hours is borne out in the bottom facet of Figure 4(a), which plots hours worked per active worker. We can see that it was about 40 hours per month at the time of TOF but then rises post-TOF to nearly 60 hours per month.<sup>14</sup> In contrast to a view in which existing projects are split over more workers, we see greater concentration of the available hours in some develo pers on the platform.

To explore the flow of workers in and out of Flash, we calculate the first and last months a worker worked on a Flash project. We then plot the number entering (top facet), the number exiting (middle facet), and the net flow (bottom facet) in Figure 4(b). Prior to TOF, the flow is positive but it turns negative shortly after. The flow of workers out of Flash reaches a maximum of about five months after TOF. The patterns in Figure 4 suggest that a change in Flash hours was better explained by some workers entirely abandoning Flash projects and other workers staying with it, rather than an even decline in Flash activity across all Flash workers.

## 5. Matched Sample Regression Estimates 5.1. Time Series Comparison for the Matched Sample

After matching on a cross-sectional data set of what workers “looked like” on TOF, we can compare the matched samples over time, pre-TOF. If the two groups moved similarly pre-TOF, it suggests that the groups are truly comparable. In Figure 5, we plot monthly averages for treated and control workers, demeaning each worker by their preperiod mean, and then demeaning each aggregated series with the TOF value (so each series has a value of zero for that period). Focusing on the preperiod, we see that Flash and non-Flash samples move together for all outcomes. We report the results of pretreatment trend tests in Online Appendix A.

Post-TOF, the groups begin to diverge on some measures, previewing some of our main regression results. In the top-left facet, we see no evidence for a decline in average wages for Flash workers. It is important to note

Skill Flash Non−Flash

Figure 4. (Color online) By-Month Grand Means for All Flash Workers  
![](/api/attachments/CWQPNNWM/fulltext/images/64d8e8ea63eef2f312cd4595084e51d3ed9109a152ae0058fc77472716b7e173.jpg)

![](/api/attachments/CWQPNNWM/fulltext/images/148fc9c6cc80d3b494db981295256fff230a61fe3c6f4b155d71a34fc02d891e.jpg)  
Notes. This figure shows the weekly time series of a number of attributes of workers active in Flash. The vertical dashed line indicates TOF. Th horizontal dashed line indicates the mean value of the attribute at the time of TOF. The x-axis indicates time in months since TOF.

that this is the average wage for all work, including Flash and non-Flash projects. On the other hand, in the facet at the top-right, we can see some evidence of a decline in hours worked. This decline comes despite an increase in applications sent, which we can see in the bottom-left facet. In addition to increasing application intensity, there is also evidence of a move away from skills relied on in the past: in the bottom-right facet, we see that Flash workers begin applying to jobs that have fewer skills in common with their previous jobs. Interestingly, there is also a general decline over time in the similarity measure for non-Flash workers, consistent with claims of rapid STEM obsolescence (Deming and Noray 2020).

## 5.2. The Effects of TOF on Flash Workers Choices

We now turn toward our main results, which are regression estimates of the effects of TOF computed on the matched panel. To compute these estimates, we use the model

Figure 5. (Color online) Matched Sample Monthly Averages for Treatment and Control Groups, Demeaned  
![](/api/attachments/CWQPNNWM/fulltext/images/b95dcda86510ff3744f22ac3c58f2ea6f7c571403c639c01506e6bea1d41561a.jpg)  
Notes. This figure plots the monthly averages for worker attributes for the treated (Flash) and control (non-Flash) groups in our matched sample Before calculating each monthly average, we demean each worker’s value by their pre-TOF value. From these monthly means, we subtract the value on TOF month so that each series has a value of zero at TOF. Average wage is reported in nominal U.S. dollars. Organic apps refer to those applications that are not solicited by the employer. App similarity refers to similarity in skills between workers’ prior project history and the jobs they apply to, as described in the text.

$$
y _ {i t} = (\mathrm{ANYFLASH} _ {i} \times \mathrm{POST} _ {t}) \beta + \gamma_ {i} + \delta_ {t} + \epsilon_ {i t},\tag{1}
$$

where $y _ { i t }$ is an outcome of interest for worker i at period $t ,$ POST<sub>t</sub> is an indicator for whether the period was after TOF, and ANYFLASH is a binary indicator of whether the worker has worked in Flash prior to TOF. The $\gamma _ { i }$ represents worker fixed effects, which will absorb the impact of time-invariant worker characteristics, and $\delta _ { t }$ represents period fixed effects. The error term, $\epsilon _ { i t } ,$ includes all other time-varying unobservable shocks to the worker’s outcome in that period. The β coefficient is interpretable as the average effect of TOF on Flash developers over the full post period.

We can also allow the effects of TOF to depend on how focused the worker was on Flash pre-TOF. For each worker, we compute the fraction of hours worked spent on Flash projects, FRACFLASH. We restrict this analysis to workers with at least 40 hours of project work on the platform, to ensure they have a meaningful basis on which to measure focus. This focus measure is zero for the control group. We can interact this measure with the POST indicator by creating an independent variable FRACFLASH × POST . This changes the interpretation of $\beta$ to a measure of the effect for workers spending 100% of their time on Flash projects, with effects linearly scaled down for workers less focused on Flash.

In Figure 6, we report estimates of $\beta$ from Equation (1), for both independent variable specifications (ANYFLASH and FRACFLASH). The left column outcomes are in logs with zeroes removed, whereas the right column outcomes are in levels. Differences in observations across facets are due to the use of unbalanced panels when the outcome cannot be computed (such as an average wage or application similarity measure if the worker did not work or send any applications that period, or when the outcome is the log of a count, such as hours worked). The outcomes from top to bottom are average wages, hours worked, number of applications sent, and application similarity. In all regressions, standard errors are clustered at the level of the individual worker.

For average wages in logs, we can see the effect of TOF was a precise zero for both specifications—there is no evidence of a decline in hourly wages for Flash workers. This matches what we observed in Figure 5. In levels, there is some evidence that the most experienced Flash developers had an increase in average wages—the FRACFLASH specification is positive and nearly significant.<sup>15</sup>

In the second facet from the top, the outcomes are log hours worked and hours worked. Every point estimate is negative. In logs, the ANYFLASH specification point estimate is about 10% fewer hours, whereas the F F estimate is 20% fewer hours worked. Given that more Flash-focused workers had to make a larger transition skill-wise, this could reflect greater difficulty in finding work, assuming preferences have not changed and this is not an intensive margin response to changed wages. In levels, we also observe a decline but the magnitudes are “switched” with a larger reduction in the ANY-FLASH specification. It is noteworthy that the levels estimates are fairly imprecise relative to those in logs. This likely reflects the large number of zeroes in hours worked that are dropped from the log estimates. The variance in the levels estimates, therefore, includes variation between workers who stayed in the market and those who exited the market, whereas the log estimates include only worker periods where some work was done.

In the bottom two facets, the outcomes are numbers of applications sent and application similarity (scaled from 0 to 100). There is a marked decline in application similarity for Flash workers in all specifications. The effects are stronger in the FRACFLASH group, which implies that those workers more specialized in Flash had to make larger adjustments in application focus. This group also submits a greater number of applications.

Online Appendix A presents the results of a number of robustness tests of these estimates. These include the results of parallel trend tests, alternative matching estimators, synthetic DID estimators, random shuffle tests, and a pretreatment placebo test. We also present diagnostic tests to evaluate the sensitivity of our findings to issues raised in the recent econometrics literature on the use of two-way fixed effects estimators with continuous treatments (Callaway et al. 2024).

## 6. The Role of Worker Attributes 6.1. Degree of Flash Specialization

If returns to prior Flash experience are small, workers may be faster to switch to other skills. However, Flash applications can be complex, requiring a mix of programming, graphic design, and other complementary skills. A would-be Flash programmer must learn the underlying programming language, ActionScript, as well as Adobe’s Flash authoring tools and best practices for building and debugging Flash applications. Even for programmers who are experienced in other languages, acquiring Flash skills would be a nontrivial investment, requiring months of sustained effort to achieve a significant level of expertise.<sup>16</sup>

Alternatively, learning Flash could make developers productive in other skills. In a typical setting, such spillovers would be challenging to estimate for Roy (1951) model reasons, as we would not see workers working in both Flash and non-Flash. However, in our online context, we observe non-Flash workers working in other skills: the treated group in our sample worked in other skills at observable wages—for no worker is FRACFLASH � 1. Using only the treatment group of Flash developers, we can estimate the wage-tenure curve for hours of experience in Flash and non-Flash hours worked for both Flash and non-Flash wages, using the panel. The two regressions are

Figure 6. (Color online) Effects of TOF on Flash Worker Outcomes  
![](/api/attachments/CWQPNNWM/fulltext/images/cf663e7a0fdba54256600079e57905bb4371e51cb95fd1df8cdc86dc7772d15d.jpg)  
Notes. This figure reports estimates of β from Equation (1). In each panel, we estimate models with a single treatment indicator, ANYFLASH, and models where the independent variable is FRACFLASH, which is the fraction of pre-TOF hours worked that were on projects requiring Flash. We show logged outcomes in the left column, and level outcomes on the right. Average wage is reported in nominal U.S. dollars. App similarity refer to similarity in skills between workers’ prior project history and the jobs they apply to, as described above. Num. applications sent refers to applica tions that are not solicited by the employer. Sample sizes for each regression are reported under the estimates labels. All models include worker and month fixed-effects. The variation in observations across facets arises because regressions are run with unbalanced panels when the outcom cannot be computed (such as an average wage or application similarity measure if the worker did not work or send any applications that period, or when the outcome is the log of a count, such as hours worked).

$$
\begin{array}{r} \log w _ {N o n - F l a s h} = \beta_ {E F} \log H _ {F l a s h} + \beta_ {E E} H _ {N o n - F l a s h} + \delta_ {t} + \gamma_ {i} + \epsilon , \\ \log w _ {F l a s h} = \beta_ {F F} \log H _ {F l a s h} + \beta_ {F E} H _ {N o n - F l a s h} + \delta_ {t} + \gamma_ {i} + \epsilon . \end{array}\tag{2}
$$

In column (1) of Table 1, returns to experience are positive and significant. It is clear that some of the human capital acquired in one skill is transferrable to other skills (Gathmann and Scho¨nberg 2010). However, “own-skill”

returns are always greater. These results are inconsistent with the argument that Flash experience produces human capital that is just as valuable in some other non-Flash skill area. There are spillovers, but it is not the case that experience is completely general, and so we expect Flash specialists to be relatively disadvantaged. These findings are consistent with the effects on FRACFLASH we observe in Figure 6.

## 6.2. Worker Age

As Flash projects declined in demand, continuing to work on Flash projects may have come with a highe opportunity cost for younger workers than for older workers. Young workers have a long career horizon and so would experience larger potential gains from climbing the learning curve in a new skill. On the other hand, given the skill-based nature of the platform, developers may be considering a forward time-window that is short enough that developer age might not impact workers’ human capital investment choices.

Table 1. Returns to Hours Worked in Flash and Non-Flash Jobs

<table><tr><td rowspan="2">Variable</td><td colspan="2">Dependent variable</td></tr><tr><td>Non-Flash log wage (1)</td><td>Flash log wage (2)</td></tr><tr><td rowspan="2">Cumulative Flash hours</td><td>0.021***</td><td>0.019**</td></tr><tr><td>(0.003)</td><td>(0.006)</td></tr><tr><td rowspan="2">Cumulative non-Flash hours</td><td>0.031***</td><td>0.014*</td></tr><tr><td>(0.005)</td><td>(0.007)</td></tr><tr><td>Week FEs</td><td>Yes</td><td>Yes</td></tr><tr><td>Worker FEs</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>15,373</td><td>5,442</td></tr><tr><td>R2</td><td>0.797</td><td>0.920</td></tr></table>

Note. This table reports estimates of the effects of project experience on post-TOF wages for Flash and non-Flash projects.  
\*p ≤ 0.05; \*\*p ≤ 0.01; \*\*\*p ≤ 0.001.

We do not directly observe worker age, but we can impute it from data provided by workers on their final year of schooling.<sup>17</sup> The average worker in the sample is 14.4 years past their final year of schooling. Figure 7 illustrates how our key labor outcomes compare for treated and control workers after separating workers into terciles by age. In each plot, the solid line is for Flash developers, and the dashed line is the matched developer group.

The first row indicates that developers in the top two terciles experienced a wage reduction, but there is no visible reduction for workers with the most recent schooling year, consistent with a larger loss of Flash-specific human capital in older workers. The second row shows that hours fall in all three groups, but the effects are larger in older workers. The figures for numbers of submitted applications are similar for Flash developers and the comparison group, although they are slightly higher for workers in the middle tercile. We do not observe a change in types of applications submitted by younger workers, who may not have accumulated much Flash human capital by TOF and may not have yet begun to “focus” on Flash technologies. Older workers made more significant adjustments in the types of applications they submitted beginning at the time of TOF. These findings suggest that younger workers, who had little Flash human capital, abandoned Flash quickly enough that wages did not change in the short-run for more experienced workers. As demand for Flash further declined, workers in the middle and older cohorts with more Flash human capital also had to move away from Flash, toward other skills.

We can also report aggregate post-TOF effects for each age group by estimating the following specification, which interacts age cohort with post (POST) and treatment (TRT) indicators:

$$
y _ {i t} = \beta_ {A C (t)} \mathrm{AgeCohort} _ {i} \times (\mathrm{POST} _ {t} \times \mathrm{TRT} _ {i}) + \gamma_ {i} + \delta_ {t} + \epsilon_ {i t}.\tag{3}
$$

Figure 8(a) reports $\beta _ { A C }$ for age cohorts for each outcome. The oldest group of workers experienced the most significant declines in wages and hours worked. They also submitted fewer applications, perhaps exiting the market. In contrast, if anything, younger workers experienced an increase in wages and hours worked although they had to submit more applications and switch to new skills which may have been costly.

We can evaluate some of these costs through the bidding mechanism. In the model, workers choose to exit the dying skill or stay, but in reality, workers have the ability to straddle both markets. For an earn-while-youlearn approach, younger workers particularly value the human capital they acquire when working with a skill. These workers can be expected to bid less for projects where they acquire new skills with high future value, or if future demand for a skill declines as it did with Flash, they might be expected to demand a premium to work with that skill. Younger workers, therefore, may choose to work with an emerging skill at a lower wage than a dying skill at a higher wage. In contrast, older workers place less value on new human capital due to a shorter career horizon, and can be expected to simply work on projects that offer the highest wage.

Figure 8(b) illustrates project bidding behavior for workers in different age cohorts. It shows mean bids submitted for Flash and non-Flash projects by Flash developers in each period. The facet on the left suggests that younger workers required higher pay to work with Flash than they did for working on projects requiring other technical skills. We observe a similar bifurcation for workers in the middle age cohort, and the separation between these bid categories is larger, which is consistent with workers in this cohort having accumulated more Flash human capital than younger workers. In contrast, for older workers, any human capital obtained by working on new skills may be less valuable, so a bifurcation in bids is less visible.<sup>18</sup>

## 6.3. Prior Skill Endowments

One question to ask when considering how Flash developers adjusted is where demand for Flash “went.” The product market niche for interactive, online, graphicsheavy applications that Flash occupied did not disappear post-TOF. Post-Flash, HTML5 and CSS3 were widely viewed as successor technologies to Flash. Indeed, we can see in Figure A.3 in the Online Appendix that Flash jobs being created post-TOF increasingly reference HTML5 as another required skill; about 20% of Flash jobs at the time of TOF mentioned HTML5, and by the end of our panel, more than 30% mentioned HTML5.

Figure 7. (Color online) Flash Market Outcomes by Years Since Leaving School  
![](/api/attachments/CWQPNNWM/fulltext/images/2d7bd901ac3482755bb158bce54a7abe252c70f8102535caebdf94a4ce3b91e3.jpg)  
Notes. This figure shows how workers and workers' hours responded after TOF where workers are divided into terciles according to the number of years they have been out of school. The x-axis in each figure indicates the number of months elapsed since TOF. The top row shows averag wage for each group, where average wage is reported in nominal U.S. dollars. The second row shows the number of total billed hours for each group. The third row shows the number of applications sent by each group, where organic apps refer to applications that are not solicited by the employer. The fourth row shows application similarity measures for each group where app similarity refers to similarity in skills between work ers’ prior project history and the jobs to which they apply.

We analyze how worker outcomes differed according to their ability to follow successor demand for Flash. In Figure 9, workers’ skill portfolios are measured in this application using data they self-report. There is no indication in the portfolio data of the degree of skill that workers have with each of these technologies, and we do not know when workers acquired these skills. However, most workers on this platform tend to enter skills when they first join the platform and leave them unchanged thereafter. We evaluate the

following specification:

$$
y _ {i t} = \beta (\mathrm{SKILL} _ {i} \times \mathrm{POST} _ {t}) + \gamma_ {i} + \delta_ {t} + \epsilon_ {i t}\tag{4}
$$

This estimates a stylized version of how being located at different points on the skill investment frontier impacted developer outcomes post-TOF. Each point in Figure 9 corresponds to an estimate (β) on the interaction effect between POST and SKILL. We compare developers at three specific points along this frontier: (1) Adobe-related skills comprise more than 50% of their skill portfolio; (2) familiar with HTML5, viewed as an increasingly popular alternative to Flash; and (3) familiar with technical programming languages, specifically C++ or Java.

Figure 8. (Color online) Differences by Workers’ Age  
(a) Treatment effect by years since leaving school  
![](/api/attachments/CWQPNNWM/fulltext/images/066bb6ea4c5d2c06558d7069eeea22d679dce88588029dac1a8112e49a529657.jpg)

(b) Bids for Flash and non-Flash jobs by age tercile  
![](/api/attachments/CWQPNNWM/fulltext/images/b6eae4f6f354e19a03310c8145a59143e5fe208a161c964d8a494da206e1044e.jpg)  
Notes. The top panel depicts estimates from Equation (3). It illustrates differences in treatment effects for developers from different cohorts, measured by when they had their final year of schooling. Average (Avg.) wage is in nominal U.S. dollars. Num Apps refer to those applications that are not solicited by the employer. App similarity (sim.) refers to similarity in skills between workers’ prior project history and the jobs to which they apply. The lower panel illustrates bidding behavior for new projects by different developer age cohorts, where workers are divided into cohorts by tercile. Project bidding values are reported in nominal U.S. dollars. Months refer to the number of months elapsed since TOF.

In all comparisons, developers in the control group with the focal skill are removed from the sample. Our findings provide support for assertions made earlier in the paper. Specialization in Adobe technologies which complement Flash (e.g., Adobe Dreamweaver or Adobe Illustrator) makes workers more vulnerable to Flash decline: for these workers, there was no change in wage, but a significant decline in hours. Flash developers who were familiar with other programming technologies earned higher hourly wages than those who were not post-TOF, which may have been the case if it was relatively easy for them to transition to other high-paying skills. Flash developers familiar with HTML5 experienced an increase in hours rather than a reduction, which would have been consistent with a rising incidence of conversion projects or rising demand for HTML5 more generally as a substitute technology.

Figure 9. (Color online) Outcomes by Worker Skills  
![](/api/attachments/CWQPNNWM/fulltext/images/fdf5715f7ac2d6ccc338361f962f1b6d6a236138e1c8f1bd04ad725471babd7c.jpg)  
Notes. This figure illustrates differences in outcomes for Flash developers with differing skill endowments, relative to a control group. Develo pers are removed from the control group if they have the skill. Average (Avg.) wage is in logs and reported in nominal U.S. dollars. Hours are in logs. App similarity (sim.) refers to similarity in skills between workers’ prior project history and the jobs they apply to, as described earlier. Th reported estimate value is the β value from the regression $y _ { i t } = \beta \left( { \mathrm { S K I L L } } _ { i } \stackrel { \cdot } { \times } \mathrm { P O S \bar { T } } _ { t } \right) + \gamma _ { i } + \delta _ { t } + \dot { \epsilon } _ { i t } .$

Table 2. Top Countries and Their Standard-of-Living Labels

<table><tr><td>Country</td><td>Percentage of sample</td><td>SOLV</td></tr><tr><td>United States</td><td>39.22</td><td>Higher</td></tr><tr><td>Philippines</td><td>22.90</td><td>Lower</td></tr><tr><td>India</td><td>12.28</td><td>Lower</td></tr><tr><td>Pakistan</td><td>3.89</td><td>Lower</td></tr><tr><td>Bangladesh</td><td>3.74</td><td>Lower</td></tr><tr><td>Canada</td><td>3.14</td><td>Higher</td></tr><tr><td>Great Britain</td><td>2.10</td><td>Higher</td></tr><tr><td>Russia</td><td>2.10</td><td>Lower</td></tr><tr><td>Australia</td><td>0.60</td><td>Higher</td></tr><tr><td>China</td><td>0.60</td><td>Lower</td></tr></table>

Notes. This table reports the top 10 countries in our sample by percentage of contractors on the platform from each country along with the standard-of-living classifications for each country. The worker’s country is imputed from where they received their las schooling. Countries are classified as lower or higher standard-ofliving categories by ChatGPT-4o.

## 6.4. Country of Origin

To evaluate whether location plays a role in these market dynamics, we conduct an analysis of the sample of contractors for whom home country information can be imputed from where they report receiving their last schooling. We use a large language model to assign universities to countries and to classify countries according to their SOLV. About 25% of this sample of workers report this information.

Table 2 reports the most common countries of origin for contractors in our sample, the percentage of contractors from each of these countries, and the SOLV categories assigned to each country. As discussed earlier, many contractors from the platform are from the United States, Philippines, or India. Online Appendix A contains additional statistics on differences among countries, including mean wages for contractors from these countries, as well as how the fraction of Flashfocused workers changed in these countries before and after TOF.

Geographic categorization of workers allows us to account for the effects of economic heterogeneity across regions. Figure 10 illustrates how treated and control outcomes in each economic region differ before and after TOF. Key differences are that workers from low-SOLV countries provide fewer hours after TOF, which may be because they were less easily able to switch to other in-demand skills. Beyond this difference, how ever, country of origin does not appear to drive large differences in how TOF affected worker choice. For explaining workers’ transition choices, location differences appear less important than age and skill.<sup>19</sup>

Figure 10. (Color online) Differences in Outcomes by Workers’ Home Country Origin  
![](/api/attachments/CWQPNNWM/fulltext/images/bd13bd3ce3f1e4bb4529566a3844d744ec63c45565c7d3b3e2564dc603728276.jpg)  
Notes. This figure plots average values of the dependent variables for the treated and control groups where the sample is divided by the stan dard of living for the worker’s home country (low or high). The x-axis in each panel indicates the number of weeks elapsed since TOF.

To test the robustness of the findings in Figure 6 to unobserved differences in the economic structure of the worker’s country, Figure 11 adds country fixed effects to our main regressions for the sample of workers for which this geographic information is available. Across most panels (outcome variables), the results are qualitatively similar on the left- and right-hand sides, which correspond to our original analysis and an analysis with country fixed effects, respectively. The standard errors are larger on the right, as expected, because of the smaller sample of workers for whom we have information on their home countries. The point estimates for wages, hours, and numbers of applications are largely in line, however, across the two models.

One notable difference is for application similarity, where the estimates fall to zero and are actually more precise when we account for heterogeneity across economic region. This suggests that the application similarity results in our main models likely reflect differences in application strategies across countries. Workers in some countries may have been more likely to stay with the technology, whereas workers in other countries may have been more prone to exit the market. These differences may be driven by the complementarity between Flash and other skills in different regions—for example, if Flash was more commonly bundled with design skills in some countries but programming skills in others, this could affect workers’ ability and incentives to transition to new technologies based on their local skil ecosystem.

Figure 11. (Color online) Effects of TOF With and Without Country FEs  
![](/api/attachments/CWQPNNWM/fulltext/images/919ffde374dca2891349f9cbab9a9b709d98e03a92de819fe6c7e5f7c4862fa4.jpg)  
Notes. This figure reports estimates of β from Equation (1). In each panel, we estimate models with a single treatment indicator, A F , and models where the independent variable is F F , which is the fraction of pre-TOF hours worked that were on projects requiring Flash. We show logged outcomes in the left column, and logged outcomes with country fixed effects on the right. Average wage is reported in nominal U.S. dollars. App similarity refers to similarity in skills between workers’ prior project history and the jobs they apply to, as described above. Num. applications sent refers to applications that are not solicited by the emplover. Sample sizes for each regression are reported under the Estimat labels. All models include worker and month fixed effects.

## 7. Generalizing Beyond Flash

We focused on Flash because it was widely used, can be learned by workers from all backgrounds, and we could identify an inflection point in demand for the technology, but we now turn toward the question of whether these findings generalize to other technical skills.

The value of the skills workers acquire on the job can vary for different technologies. Like Flash, some technologies are industry standards and easily transferable, but other skills support a specific platform and might be less valuable on the open market. Like Flash, some technical skills may be bundled with complementary skills like graphic design that only transfer to specific IT design tasks. Other skills may have a steeper (or shallower) learning curve which affects how experience matters for gaining skill mastery. Therefore, it is an empirical question as to whether workers would make similar choices when changes occur in the demand for other technical skills.

There are thousands of technical skills which vary along these and other dimensions so a comprehensive analysis of factors like industry uptake and returns to experience is beyond the scope of this analysis, but we can assess the generalizability of our findings by analyzing whether a decline in market demand affects workers’ choices in broadly similar ways as it pertains to our theoretical discussion, at least for a limited set of other skills.

Figure 12 illustrates changes in the demand for different skills during our window as measured by numbers of job openings posted that require that skill. These are skills that were particularly popular on this platform. Much of the work on this platform is related to web technologies, and this is reflected in the basket of skills. For some skills, there is an explicable reason for the observed variation in demand. For example, the change in the number of job openings related to “link building,” a search optimization technique, is due to changes in Google’s ranking algorithm, which made this activity less useful. Changes in demand for other skills, however, may reflect aggregate changes in market demand rather than the impact of singular events.

We use the market data for these skills to construct a panel at the skill-month level beginning in 2012, which is when a controlled vocabulary for skills first became available. Some skills emerge later in the panel and thus have periods with zero job posts, and when they first enter the market, the number of job posts might be small. Under the assumption that month-to-month variation in the number of jobs posted is exogenous, we can estimate

Figure 12. Number of Job Openings per Month for a Sample of Skills on the Platform  
![](/api/attachments/CWQPNNWM/fulltext/images/fceb140a13e344e7382c5242b4d548095fb60e811053f912cf7950914c90d988.jpg)  
Notes. This figure shows the number of job openings that require a given skill. Each observation in each panel corresponds to the number of job openings in a month.

Table 3. Effects of Skill-Specific Demand on Labor Market Tightness, Job-Filling Probability, and Wages

<table><tr><td rowspan="2">Variable</td><td colspan="3">Dependent variable</td></tr><tr><td>Mean log apps/opening(1)</td><td>Fill rate(2)</td><td>Mean hired wage(3)</td></tr><tr><td>Log count of job openings</td><td>-0.028***(0.007)</td><td>-0.013***(0.003)</td><td>0.006(0.006)</td></tr><tr><td>Skill FEs</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Month-year FEs</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>5,743</td><td>5,743</td><td>5,743</td></tr><tr><td> $R^2$ </td><td>0.857</td><td>0.894</td><td>0.950</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.849</td><td>0.888</td><td>0.947</td></tr><tr><td>Residual standard error (df = 5,437)</td><td>261.520</td><td>128.490</td><td>235.004</td></tr></table>

Notes. This table reports the results of regressions of skill-month outcomes, such as the mean log number of applicants per job opening, in column (1), the fill rate and the mean log hired wage (in U.S. dollars) on measures of demand, such as the log number of job openings posted. Each regression includes skill-specific FEs and month-year FEs. Standard errors are clustered at the level of skill  
\*\*\*p ≤ 0.001.

$$
y _ {s t} = \alpha_ {s} + \gamma_ {t} + \beta \cdot \log D _ {s t} + \epsilon_ {s},\tag{5}
$$

where $y _ { s t }$ is some skill-specific outcome in month $t , \alpha$ is a skill specific fixed effect, $\gamma$ is a month specific fixed effect, and $D _ { s t }$ is the number of job openings requiring skill s at time t. Table 3 reports estimates from Equation (5), with outcomes of mean log apps per opening in column (1), the fill rate in column (2), and the mean hired wage in column ${ ( 3 ) . } ^ { 2 0 }$ From column(1), the coefficient on log $D _ { s t }$ is negative, meaning that when more openings are posted, applications per opening falls. However, the effect is very small, with a 10% increase in the number of job openings leading to a little less than 3/10ths of a percent reduction in applications per job opening.

What we should expect this number to be? If we assume that the number of workers in a skill market is fixed from month to month and workers apply to a fixed number of job openings, then percentage changes in the number of job openings should have a one-to-one correspondence with percentage changes in applications per opening: if there are 10% more job openings, on average, job openings should receive 10% fewer applications.<sup>21</sup> For the effect to be as small as it is in terms of applications per openings, when the number of job openings rises, more workers must enter the market or each of the workers in the market must submit more applications.

In our broader basket of skills, fluctuations in demand do not translate into substantive changes in the number of applications per opening which is similar to what we saw for Flash. As such, from the buyer’s perspective, more job openings do not lead to an appreciably tighter labor market. This may explain the other two results from Table 3: in column (2), the coefficient on log $D _ { s t }$ is negative and significant, but small in magnitude: a 10% increase in demand is associated with only a 1/10th of a percent decrease in the fill rate. For the wage regression in column (3), the coefficient on log $D _ { s t }$ is negative (which is the wrong sign) but is very close to zero and not significant.

The whole market analysis, despite focusing on a broader basket of skills, underscores the main point of the Flash analysis. The wage response to a rise or fall in demand appears muted (flattened) because workers turn away from skill where the experience they gain is no longer valuable in the future. The strength of this relationship is likely to differ by skill and depend on the nature of jobs that include that skill (e.g., what other skills are bundled with the focal technical skill) or the costs of switching to other skills (Bessen 2003). These results suggest our findings are likely not limited to Flash, but the magnitude of the relationship for a skill may depend on the steepness of the learning curve, the transferability of the skill, and other factors. We leave a comprehensive analysis of how technical skill characteristics affect the underlying market dynamics to future work.

## 8. Conclusions

Our main finding is that a fall in the expected future value of gaining Flash human capital impelled workers to change their labor supply choices in our online market context. The rapid adjustment indicates that a price-centric interpretation of markets for technical skills may miss an important part of how supply and demand adjusts in these markets.

A number of managerial implications arise from these findings. Matching in online IT markets appears to be particularly influenced by opportunities to upskill. Professionals adept with frontier technologies are scarce; this may prompt employers to reevaluate the trade-offs between maintaining older systems and transitioning to newer ones, particularly in an online context like ours because employers have few levers when it comes to attracting talent. For instance, employers may assume that moving away from the technological frontier where labor markets are tight can alleviate the challenges of attracting talent, but we show that such a strategy may generate other costs, as workers may avoid these technical projects absent a substantial wage differential.

A second implication of our findings relates to our results on employee age. Young workers require a wage differential for working with dying technologies but older workers place less importance on the decline in future skill value because they have shorter career horizons. This means that it could be beneficial to match older workers with older technologies because these workers have less of a financial disincentive to work with these technologies. Such initiatives may be particularly valuable because many policy makers and employers are concerned about explicit or implicit ageism in IT hiring processes both offline and online (Rosales and Ferna´ndez-Arde\`vol 2020).<sup>22</sup>

Some policy implications also arise from these findings. In markets for scarce skills, tightness is normally temporary as markets adjust, but employers in online technical markets frequently voice concerns about finding workers with the right skills regardless of whether they are using decades-old skills or cutting-edge skills. Our research shows that there are no bargains to be had if choosing older technologies instead of newer ones. This is a by-product of learning by doing in this market, and implies that scarcity in a market for a particular skill cannot be circumvented by choosing older technologies. These findings help explain why concerns about labor supply and elevated wages are pervasive in the IT sector; employers cannot engage in labor arbitrage by staying away from the technological frontier, which means that labor policies should be kept malleable enough to address specific shortfalls no matter where they arise. A secondary policy implication is underscored by the data we use and also pertains to offline labor markets. Although resources like Bureau of Labor Statistics (BLS) data sets are extremely valuable, there is a need for more granular data sets that can capture the evolution of specific skills in the technical labor market.

Online work differs from offline work in several ways, including in the type of workers it attracts, the costs of switching to new employers, and how skills are bundled together in projects. Nonetheless, in its potentially broader lessons for the economics of technical skills, this paper may provide lessons about institutional or environmental factors affecting IT wages. Digital platforms can provide new insights about the economics of technical change because administrative data sets, such as those published by the BLS, elide over distinctions in technical skills—the BLS occupational code covering all developers is “Programmer,” making it impossible to study how individual developers switch skills or how frictions related to job switching can cloud inference about why workers switch to new technologies. There has been little analysis in this literature of the role of technology skill obsolescence in determining market outcomes, even though the need to adjust to this type of change arguably plays the largest role in distinguishing IT careers from other jobs. Our study therefore joins a growing body of literature analyzing the granular data generated by digital platforms to attempt to illuminate broader economic mechanisms. Despite its limitations, our stylized context provides insight into the underlying mechanics of the adverse shock and captures activity at a level of detail that has yet no offline equivalent. As such, our findings underscore the importance of skill diversification for IT professionals. Corporate decisions, such as the deprecation of a technical standard, can cas cade into the labor market and impact the employment landscape. In sum, our findings stress the importance of policies that emphasize reskilling, continuous learning, and adaptability in a rapidly changing landscape.

Of course, there are limitations to this study worth noting. Our results are derived from an empirical context where technological shocks are commonplace, where the pace of technological change is quick, and where there are relatively few frictions associated with moving to new technologies or employers. Furthermore, there are “nearby” skills that impacted workers could switch to. Other contexts might offer fewer adjustment options to affected workers, though our results do suggest what features seem to help adjustment—namely, a relatively easy way to gain on-the-job training. The relatively low stakes of hiring decisions and the short duration of the relationships on the online platform we study might limit the generalizability of our findings to offline markets.

Our findings also suggest other avenues for future research. Future work might examine how the market for Flash evolved in the post period, particularly whether jobs using declining technologies shift toward requiring different complementary skills like soft skills or industry expertise, beyond the aggregate wage and skill similarity dynamics we document. There may also be opportunities to empirically explore theoretical distinctions across technologies and examine how the learning curve for new technologies impacts labor dynamics. Future work might also consider how workers balance skill portfolios to navigate market disruption.

As institutions continue to encourage investment into technical skills, it is important to understand the economics of this human capital. The rise and fall in the value of skills within this labor market is its most important feature, and future work should continue to study how this turbulence affects how this market functions and what it means for workers and digitization.

## Acknowledgments

The authors acknowledge valuable feedback from seminar participants at the National Bureau of Economic Research IT and Digitization Summer Institute, the INFORMS Conference on Information Systems and Technology, Cornell University, Arizona State University, the Rotterdam Schoo of Management, the University of Texas-Austin, the University of Maryland, the University of Utah, Carnegie Mel lon University, and McGill University. Thanks to James Bessen, Apostolos Filippas, Richard Zeckhauser, Chis Stanton, David Autor, Rob Seamans, Jacques Cre´mer, Adam Ozimek, Sebastian Steffen, Andrey Fradkin, Erina Ytsma, Abhishek Nagaraj, Emma van Ingwen, Joe Golden, Brett Danaher, and Daniel Rock for helpful comments and suggestions. Prasanna Tambe is grateful for financial support from the Alfred P. Sloan foundation. John Horton is grateful for financial support from the Upjohn Institute. Thanks to Jeff Bigham and Elliot Geno for insight into the labor market for Flash skills.

## Endnotes

<sup>1</sup> For example, see the report on the growth of the gig economy at https://blog.kleros.io/content/files/wpcontent/uploads/2019/05/ gig-economy-white-paper-may-2019.pdf.

<sup>2</sup> Despite Jobs’ claims that the decision was made for technical reasons, this was viewed by many as a pretext—the “real” reason for this withdrawal of support was a desire for greater control over the experience on Apple devices, particularly the iPhone. The contemporaneous discussion of the announcement on Hacker News, a discussion site run by Y Combinator and known for insider takes on IT and the startup/tech industry—is illustrative, as it contains many arguments that Apple’s choice was self-interested and made on flimsy technical arguments (see https://news.ycombinator.com/ item?id=1304310). Even if Jobs’ arguments had technical merit, it was clearly self-serving to make them at that particular moment in time.

<sup>3</sup> Within this specific occupational context, our findings stand as a counterpoint to the literature equating negative demand shocks to earnings losses on the order of 10%–15% (Jacobson et al. 1993, Kletzer 1998, von Wachter et al. 2009, Couch and Placzek 2010, Davis and von Wachter 2011), even for work requiring little or no training.

<sup>4</sup> It is possible that a fall in demand for offline Flash work may have been offset by a movement of this type of work online. Nonetheless, the net effect was a fall in demand on the platform itself.

<sup>5</sup> In the simplified context discussed above, gaining skills in Flash does not help with becoming productive with other technologies but this is an over simplification, if, for example, knowledge of web design is likely to teach more general programming and graphic design skills. Instead of our “pick a single skill” assumption, we can also allow workers to split a unit of time between skills. Work in one skill would translate into human capital in both skills, under the assumption that the best experience in a skill is actually working in that skill. This would create an investment frontier, as in Murphy (1986), where risk-neutral workers pick a corner solution but the higher the value of α, the lower the cost of transition.

<sup>6</sup> See https://www.upwork.com/hire/html5-developers/cost/ (last accessed November 15, 2023).

<sup>7</sup> An alternative approach for computing application similarity might use Term Frequency - Inverse Document Frequency (TF–IDF), a lead ing approach for measuring similarity between text documents that places greater weight on rare topics and words and which is known to work particularly well for document clustering, search, and other applications. In our context, however, TF-IDF has the undesirable property that it dilutes the economic interpretability of the measure. All words in this corpus are skills, and TF-IDF would place greater weight on unique or rare skills when computing the distance between a job listing and the worker’s skill vector. TF-IDF, therefore, implicitly introduces notions of supply and demand to our measure, whereas a cosine similarity measure has a more straightforward economic interpretation, which is simply the extent to which the worker’s skills overlaps with what is in the job listing.

<sup>8</sup> As in conventional labor markets, the precise manner by which prices—wages—are arrived at is an open question. In a descriptive sense, the process is simple: workers propose hourly wages when they apply, which employers are free to take as take-it-or-leave-it offers or counter. Workers can counter, mirroring the kind of wage negotiations that are commonplace in many settings. However, when we talk about price formation in markets, we often mean whether prices should be thought of as competitive, which, in a labor market, means workers are paid their marginal product, or as bargained outcomes, which can lead to equilibrium wage dispersion (Mortensen and Pissarides 1994). Another perspective can have equilibrium wages, but workers are not paid their marginal product, but rather are exploited to some degree by monopolist employers (Dube et al. 2020). It is important to note that with labor, differences in wages due to differences in experience level are not considered a violation of the law of one price, or evidence of price dispersion per se. Rather, more experienced workers are more pro ductive and have a higher marginal product of labor in some unit of work.

<sup>9</sup> In studies of displaced workers, the consensus view seems to be that the fixed effect approach works best with long observation windows and relatively mature workers whose hourly earnings likely reflect their market earnings potential (von Wachter et al. 2009). We have some insight into a worker’s age and off-platform experience (which we will discuss), but in this market, the short duration of projects and the lack of other factors that could affect earnings (amenities, benefits, relational contracts, etc.) implies that worker productivity is frequently “marked to market.” We have a relatively long panel, and so we can observe workers for some time prior to TOF, though as we saw earlier, entry was peaking just prior to TOF.

<sup>10</sup> For FRACFLASH, the min is 0.01 and the max is 1. The 25th, 50th, and 75th percentiles are 0.045, 0.131, and 0.34, respectively. The mean is 0.25, and the standard deviation is 0.28

<sup>11</sup> We have information on location for a large fraction of our sample (inferred from place of most recent schooling), but we do not match workers on location. In the whole (matched) sample, about 29% (37%) of workers are from the United States. We see very little difference in the global distribution of Flash workers before and after TOF. Moreover, our main results are qualitatively similar when we incorporate country fixed-effects into our regression analyses using the subsample of workers for whom we have country location.

<sup>12</sup> As our samples are drawn from a marketplace, a natural concern is how these two groups interact, potentially creating a Stable Unit Treatment Value Assumption (SUTVA) violation (Blake and Coey 2014). As we can observe all applications, we can characterize the degree to which the two groups were competing. In over 70% of openings, there was no overlap in applicants; in the remainder, where there was some overlap, there was typically just one applicant from the other group. As workers send many applications and at least some Flash developers have at least some non-Flash skills, this speaks to how “clustered” this market is by skill. Furthermore, this “overlap” fraction falls over time, contrary to the notion that out-of-work Flash developers were crowding out workers in the control group. One of the reasons why SUTVA is unlikely to be a first-order concern is that the Flash sample was relatively small compared to the market as a whole—at the time of TOF, the total number of workers who had applied to at least one job was over 250,000.

<sup>13</sup> It is also historically the mostly commonly requested skill on the platform with, by far, the largest volume of hours worked, making it less likely that Flash “refugees” are affecting PHP measures.

<sup>14</sup> We do not plot early values of this ratio, as the market was relatively small and the estimate of hours per worker is imprecise.

<sup>15</sup> One question is whether the workers were differentially likely to be active on the platform. We find no evidence that they differed from the control on several definitions of “exit.” (This analysis is available upon request.)

<sup>16</sup> To provide a sense of the size of the human capital investment required to learn Flash, the last published Flash user’s guide is over 527 pages, and the full documentation (made up of HTML files) is nearly 17 million words. There are hundreds of books on Flash still listed on Amazon. As of June 22, 2019, there are still over 350 books returned on Amazon.com for the query “Adobe Flash” (https:// www.amazon.com/s?k=Adobe+Flash). The user’s guide is here: https://www.adobe.com/support/documentation/archived\_ content/en/flash/cs3/flash\_cs3\_help.pdf. The documentation word count was obtained by downloading http://help. adobe.com/en\_US/FlashPlatform/reference/actionscript/3/ PlatformASR\_Final\_en-us.zip and running: find . -name \*html -type f -print0 — xargs -0 wc — tail -n 1 on the unzipped folder.

<sup>17</sup> Just under 21% of freelancers do not report their schooling end date, so we cannot compute age for these workers. Our analysis of age is restricted to the 80% of workers who do report a schooling end date. In terms of dealing with this missing data problem, it is difficult to reliably impute this field from the available data. Although the reporting of this data is almost certainly nonrandom, contractors may choose not report age because they have not finished school yet (in which case they will be younger), because they are concerned about ageism from employers (in which case they are on the older side), or perhaps because they have no formal educa tion (which would not be closely tied to any age category). One thing we can do is to separately estimate treatment effects for the 20% of workers with missing data to see how they compare to those for other workers (that chart is shown below). We can see that workers with missing data on schooling end date apply to different jobs, in a pattern that is similar to the youngest group. However, unlike this group (which has formal schooling), the group with missing education does not do as well from a longer-run wage perspective.

<sup>18</sup> It is also possible that differences in bids for Flash projects and other projects reflect tastes for working with one technology or another. Developers are known to have strong preferences for the tools with which they work. However, the timing and pattern of bidding across age groups suggests that workers are considering the future value of skills in their bidding choices.

<sup>19</sup> We can also directly estimate how a treatment effect varies across these regions. In results not shown but available upon request, we find that the largest difference in the magnitude of a treatment effect across economic regions is with total hours which is consistent with Figure 10, but none of the differences are significant across regions.

<sup>20</sup> To provide an example of how the column (1) outcome measure is constructed, if a skill had only three openings that received 10, 15 and 20 job applications, the outcome measure for that skill would be (log 10 + log 15 + log 20)=3 ≈ 2:67. Standard errors in this regres sion are clustered at the skill level. However, as in Bertrand et al. (2004), this does little to deal with serial correlation, if serial correlation is an issue. It is not an issue with this data set however, as a group bootstrap returns a sampling distribution for the β coeffi cient with the same variance as that implied by the regular robust clustered standard errors.

<sup>21</sup> For example, if applications per opening for a particular job j in a skill is a � knS=Dɛ , where ɛ captures some job-specific idiosyn cratic component, the log number of applications would be $\log a = \log k + \log n + \log S + \log D + \log \epsilon$

<sup>22</sup> Also see Lindell (2023) and Roumayah (2023).

## References

Ang S, Slaughter S, Yee Ng K (2002) Human capital and institutional determinants of information technology compensation: Modeling multilevel and cross-level interactions. Management Sci. 48(11):1427–1445.

Barley SR, Kunda G (2011) Gurus, Hired Guns, and Warm Bodies: Itinerant Experts in a Knowledge Economy (Princeton University Press, Princeton, NJ).

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust differences-in-differences estimates? Quart. J. Econom. 119(1): 249–275.

Bessen JE (2003) Technology and learning by factory workers: The stretch-out at Lowell, 1842. J. Econom. Hist. 63(1):33–64.

Bessen JE (2016) Information technology and learning on-the-job. Working paper, Boston University School of Law, Boston.

Blake T, Coey D (2014) Why marketplace experimentation is harder than it seems: The role of test-control interference. Proc. 15th ACM Conf. Econom. Comput. (Association for Computing Machinery, New York), 567–582.

Borusyak K, Jaravel X (2016) Revisiting event study designs. Work ing paper, University of California, Berkeley.

Bradley T (2010) Apple v. Adobe: Something just doesn’t add up. Accessed February 15, 2025, https://www.pcworld.com/ article/512482/apple\_v\_adobe\_something\_just\_doesnt\_add\_up. html.

Callaway B, Goodman-Bacon A, Sant’Anna PH (2024) Differencein-differences with a continuous treatment. Working Paper No. 32117, National Bureau of Economic Research, Cambridge, MA.

Chen DL, Horton JJ (2016) Research note—Are online labor markets spot markets for tasks? A field experiment on the behavioral response to wage cuts. Inform. Systems Res. 27(2):403–423.

Couch KA, Placzek DW (2010) Earnings losses of displaced workers revisited. Amer. Econom. Rev. 100(1):572–589.

Cullen Z, Farronato C (2021) Outsourcing tasks online: Matching supply and demand on peer-to-peer internet platforms. Management Sci. 67(7):3985–4003.

Davis SJ, von Wachter T (2011) Recessions and the costs of job loss Brookings Papers Econom. Activity 2011(2):1–72.

Deming DJ, Noray K (2020) Earnings dynamics, changing job skills and STEM careers. Quart. J. Econom. 135(4):1965–2005.

Dua A, Ellingrud K, Hancock B, Luby R, Madgavkar A, Pemberton S (2022) Freelance, side hustles, and gigs: Many more Americans have become independent workers. Report, McKinsey & Company, New York

Dube A, Jacobs J, Naidu S, Suri S (2020) Monopsony in online labor markets. Amer. Econom. Rev. Insights 2(1):33–46.

Gathmann C, Scho¨nberg U (2010) How general is human capital? A task-based approach. J. Labor Econom. 28(1):1–49.

Hong Y, Wang C, Pavlou PA (2016) Comparing open and sealed bid auctions: Evidence from online labor markets. Inform. Systems Res. 27(1):49–69.

Horton JJ (2021) The ruble collapse in an online marketplace: Some lessons for market designers. Working Paper No. 28702, National Bureau of Economic Research, Cambridge, MA.

Huang N, Burtch G, Hong Y, Pavlou PA (2020) Unemployment and worker participation in the gig economy: Evidence from an online labor market. Inform. Systems Res. 31(2):431–448.

Jacobson LS, LaLonde RJ, Sullivan DG (1993) Earnings losses of dis placed workers. Amer. Econom. Rev. 83(4):685–709.

Kletzer LG (1998) Job displacement. J. Econom. Perspect. 12(1):115–136.

Kokkodis M (2023) Adjusting skillset cohesion in online labor markets: Reputation gains and opportunity losses. Inform. Systems Res. 34(3):1245–1258.

Kokkodis M, Ipeirotis PG (2016) Reputation transferability in online labor markets. Management Sci. 62(6):1687–1706.

Liang C, Peng J, Hong Y, Gu B (2023) The hidden costs and benefits of monitoring in the gig economy. Inform. Systems Res. 34(1):297–318.

Lindell MJ (2023) Ageism common in the tech industry. Accessed September 29, 2024, https://www.gu.se/en/news/ageismcommon-in-the-tech-industry.

McKay T (2019) Google sticks another knife in flash’s corpse. Giz modo (July 31), https://gizmodo.com/google-sticks-another knife-in-flashs-corpse-1836840400.

Mithas S, Krishnan MS (2008) Human capital and institutional effects in the compensation of information technology profes sionals in the United States. Management Sci. 54(3):415–428.

Mortensen DT, Pissarides CA (1994) Job creation and job destruction in the theory of unemployment. Rev. Econom. Stud. 61(3):397–415.

Murphy KM (1986) Specialization and human capital. Doctoral dis sertation, The University of Chicago, Chicago.

O’Mahony S, Bechky BA (2006) Stretchwork: Managing the career progression paradox in external labor markets. Acad. Management J. 49(5):918–941.

Pofeldt E (2020) The coming boom for freelancers. Forbes (June 12), https://www.forbes.com/sites/elainepofeldt/2020/06/12/thecoming-boom-for-freelancers/.

Rayburn D (2010) Steve Jobs is lying about Adobe Flash. Business Insider (April 29), http://www.businessinsider.com/steve-jobsis-lying-about-flash-2010-4.

Richmond S (2010) Adobe hits back at Apple’s “smokescreen.” Telegraph (April 30), http://blogs.telegraph.co.uk/technology/ shanerichmond/100005034/adobe-hits-back-at-applessmokescreen/.

Rosales A, Ferna´ndez-Arde\`vol M (2020) Ageism in the era of digital platforms. Convergence 26(5–6):1074–1087.

Roumayah TT (2023) Why age discrimination is baked into many online job sites. Accessed November 17, 2024, https://www. sommerspc.com/blog/2017/07/why-age-discrimination-is baked-into-many-online-job-sites/.

Roy AD (1951) Some thoughts on the distribution of earnings. Oxford Econom. Papers 3(2):135–146.

Sekhon JS (2011) Multivariate and propensity score matching software with automated balance optimization: The matching package for R. J. Statist. Software 42(7):1–52.

Stanton CT, Thomas C (2016) Landing the first job: The value of intermediaries in online hiring. Rev. Econom. Stud. 83(2): 810–854.

Tam PW (2010) Flash back: Demand up in engineering specialty. Wall Street Journal (August 26), https://www.wsj.com/articles SB10001424052748703846604575447600001479266.

Tapia CR, Iacob NA, Datta N (2024) Working without borders—The promise and peril of online gig work: Short note series number five: The role of local online gig platforms. Report, World Bank Group, Washington, DC.

von Wachter T, Song J, Manchester J (2009) Long-term earnings losses due to mass layoffs during the 1982 recession: An analysis using US administrative data from 1974 to 2004. Working paper, UCLC, Los Angeles.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites or posted to a listserv without the copyright holder's express written permission. However, users may print, download, or email articles for individual use.
