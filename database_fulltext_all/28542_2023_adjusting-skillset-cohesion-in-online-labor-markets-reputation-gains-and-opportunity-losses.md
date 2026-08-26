---
otero_id: 28542
otero_key: "QBHFMCCN"
title: "Adjusting Skillset Cohesion in Online Labor Markets: Reputation Gains and Opportunity Losses"
authors: "Marios Kokkodis"
year: "2023"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.1177"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Adjusting Skillset Cohesion in Online Labor Markets: Reputation Gains and Opportunity Losses

Marios Kokkodis<sup>a</sup>

<sup>a</sup> Carroll School of Management, Boston College, Chestnut Hill, Massachusetts 02467 Contact: marios.kokkodis@gmail.com, https://orcid.org/0000-0002-5037-6060 (MK)

Received: July 1, 2019 Revised: July 29, 2020; June 28, 2021; August 11, 2022 Accepted: September 19, 2022 Published Online in Articles in Advance: November 14, 2022

https://doi.org/10.1287/isre.2022.1177

Copyright: © 2022 INFORMS

Abstract. In online labor markets, contractors’ ability to charge for their services largely depends on their skills. To keep up with shifting labor market needs, contractors often expand their skills with new skills. When the new skills are similar to the contractors’ current skills, they often increase skillset cohesion (i.e., the average similarity of skills in a skill set). However, when the new skills have little similarity with contractors’ current skills, skillset cohesion decreases. Despite the recent surge in research that studies remote contractor behavior, little is known on how such adjustments of skillset cohesion affect contractor value in digital workplaces for short-term work. To investigate, I argue that skillset adjustments affect market value through changes in the contractor’s perceived reputation on the new skills and the additional job opportunities that new skills create. Building on prior work on individual-level exploration-exploitation, I hypothesize that compared with skills that decrease cohesion, skills that increase cohesion result in reputation gains and opportunity losses. If reputation gains are greater than opportunity losses, increasing skillset cohesion will result in higher market value than decreasing skillset cohesion. However, if the opposite is true, increasing skillset cohesion will result in lower market value than decreasing skillset cohesion. Empirically, I measure a contractor’s market value through hourly wages and hiring rates and skillset cohesion through word embeddings. Analysis of a panel data set of 47,638 tasks illustrates these tradeoffs of increasing skillset cohesion: for hourly wages, reputation gains are smaller than opportunity losses; hence, all else being equal, increasing skillset cohesion has a relatively negative effect on wages. However, for hiring rates, the opposite is true: increasing skillset cohesion increases contractor hireability. As the first study to explain the effects of adjusting skillset cohesion in digital workplaces, the work allows contractors to make better-informed decisions and guides managerial interventions.

History: Ravi Bapna, Senior Editor; Yuliang Yao, Associate Editor. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.1177.

Keywords: online labor markets • empirical analysis • skillset cohesion • skillset diversification

## 1. Introduction

Online labor markets such as Freelancer and Upwork allow employers to connect with contractors around the globe to accomplish diverse tasks. These tasks span multiple categories, including web development, writing and translation, accounting, sales, and marketing. On par with other online platforms (e.g., Amazon), online labor markets grew significantly in the past two decades (Statista Research Department 2021). Upwork, for example, has more than 14 million contractors and more than 5 million employers. These contractors complete more than three million tasks annually—a total transaction volume of more than 1 billion USD (Lauren 2017, Brier and Pearson 2018). This growth will likely continue (if not accelerate) in the future, as the gig economy continues to structure the future of work (Sundararajan 2016, Jain et al. 2018).

In these digital workplaces, contractors charge for their services according to their skills and expertise (Kokkodis and Ipeirotis 2014, 2021). Because new skills emerge and old skills become obsolete (Autor et al. 1998, Autor 2001, Oliver 2015, Kokkodis and Ipeirotis 2016), online contractors must be diligently re-educating and reskilling themselves to keep up with shifting labor market needs (Kuhn and Skuterud 2004, Stevenson 2009, Oliver 2015). Digital workplaces recognize this need for reskilling, and they guide contractors toward appropriate skill acquisition through regular press releases of highly desirable skills (Enterprise 2017, Schultz 2018) and advanced skill recommendation systems (Patel et al. 2017, Kokkodis and Ipeirotis 2021).

When contractors learn new skills that are similar to their current skills, they often increase their skillset’s cohesion (i.e., the average similarity of skills in a skillset).

However, when the new skills have little similarity with contractors’ current skills, skillset cohesion decreases. Despite the recent surge in research that studies contractor behavior in online labor markets (Yoganarasimhan 2013; Moreno and Terwiesch 2014; Hong et al. 2015; Chen and Horton 2016; Lin et al. 2016; Hong and Pavlou 2017; Filippas et al. 2018; Rahman 2018; Kokkodis and Ipeirotis 2016, 2021), no prior work has investigated how skill choices that adjust the overall skillset composition affect contractors in these markets. Given that such skill choices occur frequently and are often costly (in time and potentially money; Kokkodis and Ipeirotis 2021), in this work, I ask the following:

How does adjusting skillset cohesion affect a contractor’s market value in digital workplaces for shortterm tasks?

A rich literature on online work suggests that a contractor’s market value changes over time according to two dynamic characteristics: the contractor’s reputation and job opportunities. When contractors learn new skills, their observed reputation on their current skills might not always transfer to the new skills. Similarly, the new skills might create heterogeneous job opportunities for different contractors. Building on prior works on individual exploitation and exploration, I structure a theoretical framework that compares the effects of increasing vs. decreasing skillset cohesion on contractor’s market value. Specifically, I argue that because a contractor’s current reputation transfers more directly to newly acquired similar (than dissimilar) skills, increasing skillset cohesion will result in reputation gains. Conversely, because dissimilar skills provide access to opportunities previously beyond the reach of the contractor, increasing skillset cohesion will result in opportunity losses. Combined, reputation gains and opportunity losses structure the tradeoffs of acquiring skills that increase skillset cohesion. If reputation gains are greater than opportunity losses, increasing skillset cohesion will increase market value. However, if opportunity losses are greater than reputation gains, increasing skillset cohesion will decrease market value.

To empirically investigate the theoretical framework, I use a panel data set of 47,638 completed tasks from a major online labor market. Contractors in the data follow independent career trajectories and create skillsets of varying degrees of cohesion. This within-contractor skillset variation allows us to disentangle the focal effect of adjusting skillset cohesion from private information and other static unobserved characteristics that drive contractors’ choices to work on specific tasks. I measure a contractor’s market value through hourly wages and hiring rates; I measure the degree of cohesion of any given skillset with a new approach that maps skills to numeric dimensions through word embeddings. Finally, fixed-effects specifications capture how contractors market values change as they make different skill choices that adjust their skillset cohesion.

The results of the empirical analyses highlight the tradeoffs of acquiring similar skills that increase<sup>1</sup> skillset cohesion: for hourly wages, reputation gains are smaller than opportunity losses; hence, all else being equal, increasing skillset cohesion negatively affects hourly wages. However, for hiring rates, reputation gains are greater than opportunity losses, and, as a result, increasing cohesion increases contractor hireability. Empirical evidence supports the hypothesized underlying mechanisms and assumptions. Furthermore, robustness and alternative tests (mediation analysis, instrumental variables, propensity score matching, alternative measures, sequential models, subsample analyses) corroborate the main findings.

The study contributes to research in online labor markets, skill choices, and the individual-level dilemma of exploration-exploitation. In particular, it is the first study to investigate and explain how adjusting skillset cohesion affects the market value of contractors in digital workplaces. Through a new theoretical framework, the work pinpoints the effects of increasing skillset cohesion on two competing forces: reputation gains and opportunity losses. Empirically, it shows for the first time that because reputation gains have a weaker effect on hourly wages than opportunity losses, increasing cohesion results in lower wages. However, because the opposite is true regarding hireability, increasing cohesion increases contractors’ hiring rates. Hence, it demonstrates that increasing skillset cohesion will likely result in significant tradeoffs that contractors, who make these choices, should consider.

The work has practical implications for online contractors and platform managers. By explaining the tradeoffs of acquiring different types of new skills, the work helps contractors make better-informed choices. For instance, digital workplaces can provide relevant information to contractors through their usual means of communication (i.e., blog and social media posts). In addition, managers can use the new measurement technique to track skillset cohesion and emulate the dynamic career paths of individual contractors. Monitoring of such career trends gives platform managers opportunities to make targeted interventions and guide contractors in terms of skill acquisition and task selection.

## 2. Theoretical Development

The recent emergence and growth of online labor markets (Agrawal et al. 2015) has provided new opportunities for managers to work with remote contractors efficiently (Horton and Chilton 2010, Ipeirotis et al. 2010, Moreno and Terwiesch 2014). By codifying widespread data, these markets facilitated running experiments at scale (Horton et al. 2011, Berinsky et al. 2012) to better understand individual businesses and overall market efficiency (Gopal et al. 2003, Arora and Forman 2007, Dey et al. 2010, Allon et al. 2012, Hong et al. 2015, Chen and Horton 2016, Hong and Pavlou 2017, Filippas et al. 2018, Kokkodis and Ipeirotis 2022, Kokkodis and Ransbotham 2022, Kokkodis et al. 2022). Yet, and although investing in human capital through new skill acquisition is critical for gaining a competitive advantage (Schultz 1961, Becker 1962, Coff 1997, Blundell et al. 1999, Lepak and Snell 1999, Bosma et al. 2004, Campbell et al. 2012), little is known about how contractors evolve in these markets. To fill this gap, I investigate how skill choices that structure career paths (Johnson 1970, Stevenson 2009, Agarwal and Ohyama 2013) affect contractors’ value in digital workplaces.

## 2.1. Contractor Value in Online Labor Markets

A contractor’s market value (i.e., ability to get hired and perform short-term remote work at a satisfying compensation rate) depends on both static and dynamic personal characteristics. For instance, gender and location are relatively static features that correlate with contractor success in online labor markets (Gefen and Carmel 2008, Agrawal et al. 2013, Ghani et al. 2014, Kokkodis et al. 2015, Lin and Viswanathan 2015, Chan and Wang 2017, Hong and Pavlou 2017). On the other hand, contractor reputation—often measured by the contractor’s average feedback score and observed experience on the platform—also affects market value (Gefen and Carmel 2008, Yoganarasimhan 2013, Moreno and Terwiesch 2014). Yet, reputation is dynamic, as it changes every time a contractor completes a new task (Kokkodis 2019, 2021).

Besides personal characteristics, market value also depends on the job opportunities that the contractor’s skillset creates in a marketplace (Kokkodis and Ipeirotis 2014, Christoforaki and Ipeirotis 2015, Claussen et al. 2018). A contractor with a skillset in higher demand can easily get hired and charge higher premiums. In comparison, a contractor with a skillset in lower demand might have trouble getting hired and be willing to accept lower premiums (Kokkodis and Ipeirotis 2021). As with reputation, job opportunities are relatively dynamic because they depend on shifting labor market needs (Institute of Business Value 2019). However, contractors are not passive either: They often adjust their skillsets to meet these dynamic conditions (Kuhn and Skuterud 2004, Stevenson 2009, Oliver 2015, BCG 2018). Hence, as new skills emerge and old skills become obsolete (Autor et al. 1998, Autor 2001, Oliver 2015, Kokkodis and Ipeirotis 2016), a contractor’s value also adjusts. However, not all new skills create equal market value improvements for all contractors. In fact, the same new skills might have heterogeneous effects across contractors with different skillsets (Djumalieva and Sleeman 2018, Kokkodis and Ipeirotis 2021). To dig deeper, I first need to understand how new skills alter a contractor’s skillset composition.

## 2.2. Skillset Cohesion

A new skill acquisition adjusts the average similarity of skills (henceforth cohesion) in a contractor’s skillset. In particular, a new skill that is similar to a contractor’s current skillset will increase (or leave unchanged) the contractor’s current skillset cohesion. Conversely, a new skill that is not similar to a contractor’s current skillset might decrease the contractor’s skillset cohesion. Contractors who concurrently acquire some skills with high and some skills with low similarity to their current skillset will adjust their skillset cohesion through the aggregated net effect of all new skills.

## 2.3. Tradeoffs of Adjusting Skillset Cohesion

Skill acquisition can affect a contractor’s market value through both reputation<sup>2</sup> and job opportunities (Section 2.1). Exploration-exploitation strategies (Mom et al. 2007, 2009; Rogan and Mors 2014; Navarro et al. 2016; Lee and Meyer-Doyle 2017; Lee 2019; Schnellba¨cher et al. 2019; Tempelaar and Rosenkranz 2019) and other expected contractor behaviors (Yoganarasimhan 2013, Moreno and Terwiesch 2014, Kokkodis and Ipeirotis 2016, Lin et al. 2016, Filippas et al. 2018, Rahman 2018) can provide a theoretical framework on how adjustments in skillset cohesion might affect a contractor’s reputation and job opportunities. For the rest, I use exploration and exploitation in the context of individual ambidexterity, as defined by Mom et al. (2007):

• Exploration: The process of “searching for, discov ering, creating, and experimenting with new opportunities” (Mom et al. 2007, p. 910).

• Exploitation: The process of “selecting, implementing, improving, and refining existing certainties” (Mom et al. 2007, p. 910).

2.3.1. Adjusting Skillset Cohesion and Contractor Reputation. Choices that increase skillset cohesion al low contractors to exploit, improve, and refine existing certainties (Mom et al. 2007). To exploit, individuals need to narrow focus on the existing parameters of the task at hand (Nelson 2009) and form more comprehen sive knowledge bases (Schilling et al. 2003, Beckman et al. 2004, Wiersma 2007). Because of this narrower focus, exploitation increases reliability (Levinthal and March 1993, Good and Michel 2013) and certainty on already known abilities (Holmqvist 2004, Good and Michel 2013). Hence, contractors who choose to exploit and increase their skillset cohesion will increase their perceived reliability. In online labor markets, reliability associates with contractor reputation, which predicts the contractor’s expected service quality (Kokkodis and Ipeirotis 2016, Filippas et al. 2018, Rahman 2018, Kokkodis 2021) and increases employers’ trust in contractors’ abilities (Yoganarasimhan 2013, Moreno and Terwiesch 2014, Lin et al. 2016). As a result, contractors who increase their skillset cohesion and signal higher expertise and increased reliability (exploitation; Good and Michel 2013) should (at least) project their current reputation to their newly acquired similar skills (Kokkodis and Ipeirotis 2016).

On the other hand, choices that decrease skillset cohesion allow contractors to explore and discover new opportunities by working on skills that require knowledge of new concepts and different abilities (Mom et al. 2007). When individuals choose to explore, they need to translate relevant knowledge from their primary focused tasks to their exploratory new tasks (Rogan and Mors 2014). In fact, by definition, exploration requires novel solutions that rely on new knowledge not used (and hence not evaluated) before (Lavie et al. 2010). But contractor reputation does not uniformly transfer to dissimilar skills that rely on not previously evaluated knowledge (Kokkodis and Ipeirotis 2016). Hence, employers will consider hiring workers on these new exploratory skills with relatively higher uncertainty.

Combined, when contractors exploit and increase their skillset cohesion, their transferred reputation on the newly acquired skills will be greater or equal than their reputation on any newly acquired exploratory skills that decrease their current skillset cohesion. Hence, increasing skillset cohesion should result in reputation gains.

2.3.2. Adjusting Skillset Cohesion and Job Opportunities. Compared with exploration that has uncertain and often negative returns, exploitation usually has “positive, proximate, and predictable” outcomes (March 1991). This explains why individuals, who are risk averse when it comes to decisions that affect their payoffs (Wiseman and Gomez-Mejia 1998, Holt and Laury 2002, Lee and Meyer-Doyle 2017), tend to keep exploiting (March 1991, Denrell and March 2001, Lee and Meyer-Doyle 2017). Yet, introducing different incentives (Lee and Meyer-Doyle 2017) and enhancing motivation (Mom et al. 2019) can encourage individuals to explore new opportunities (Gibson and Birkinshaw 2004, Mom et al. 2009, Rogan and Mors 2014, Lee and Meyer-Doyle 2017, Rosing and Zacher 2017, Lee 2019). In fact, strong incentives can be particularly effective when coupled with an individual’s pay (Zenger and Lazzarini 2004, Perryman and Combs 2012, Baumann and Stieglitz 2014).

Transferred to the context, online contractors will likely keep acquiring contextually similar skills until they receive significant incentives and find the necessary motivation to explore new opportunities. This observation is not surprising: While choosing similar skills, contractors can accurately assess their ability to learn and perform well, and they can predict whether they will enjoy working on the new skills (White 2009). On the other hand, contractors who choose to explore skills that have low similarity with their existing skills might find themselves in unfamiliar environments. For instance, because contractors lack prior experience in similar skills, they might overestimate their learning abilities (Kahneman and Lovallo 1993, Robinson and Marino 2015) and fail to learn the new low-similarity skills. Even if they learn the new skills, they might discover later that they do not enjoy working on them and perform poorly (Demerouti 2006, Graves et al. 2012). This uncertainty around dissimilar skills suggests that contractors will explore new contexts when they expect that these new dissimilar skills will create greater job opportunities (incentive to explore; Lee and Meyer-Doyle 2017, Mom et al. 2019) than alternative choices of skills similar to their current skillsets (default choice to exploit; Lee and Meyer-Doyle 2017).<sup>3</sup>

Combined, I expect that when contractors choose to exploit and increase their skillset cohesion, they will experience a relatively lower increase in new job opportunities than when they choose to acquire skills that decrease their skillset cohesion. As a result, increasing skillset cohesion should result in opportunity losses.

2.3.3. Reputation Gains vs. Opportunity Losses. Increasing skillset cohesion results in relative reputation gains and opportunity losses. Because these two forces are at odds, the net effect on the contractor’s market value depends on their magnitudes. When the magnitude of reputation gains is greater than that of opportunity losses (reputation-dominant), increasing skillset cohesion will increase market value. However, when the magnitude of opportunity losses is larger than that or reputation gains (opportunity-dominant), increasing skillset cohesion will decrease market value. Formally, I have the following.

Hypothesis 1a (Reputation-Dominant). For a given contractor, increasing skillset cohesion will yield reputation gains and opportunity losses. If reputation gains are greater than opportunity losses, increasing skillset cohesion will increase the contractor’s market value.

Hypothesis 1b (Opportunity-Dominant). For a given contractor, increasing skillset cohesion will yield reputation gains and opportunity losses. If opportunity losses are greater than reputation gains, increasing skillset cohesion will decrease the contractor’s market value.

Out theoretical framework does not compare job opportunities of skillsets of different contractors: all comparisons happen within a fixed contractor and original skillset. The same skill can heterogeneously affect contractors who have different skillsets (Section 2.1). Furthermore, the framework relies on contractors making rational choices and choosing new skills that increase their job opportunities (Online Appendix B empirically supports this assumption). Given that they are rational (i.e., choose highly desirable skills to learn), the endogenous part of the choice (e.g., the contractor’s unobserved abilities, intuition, market understanding) does not affect the hypothesized reputation gains and opportunity losses, as these adjustments assume the unobserved endogenous contractor qualities fixed. (The empirical context described in Sections 3 and 4 helps disentangle the effect of changes to skillset cohesion from unobserved contractor qualities.)

## 2.4. Illustrative Example of Adjusting Skillset Cohesion

To illustrate the tension between reputation gains and opportunity losses, consider a hypothetical contractor, Maya, who is an expert graphic designer<sup>4</sup> that regularly uses Photoshop and Lightroom. Maya observes that many openings in the online labor market request Illustrator and CorelDRAW. She decides to extend her graphic design skills by learning these two additional software packages. Because Illustrator and Corel-DRAW require similar abilities to the skills she already has, they will likely increase (or leave unchanged) her skillset cohesion.

At the same time, Maya follows the blog posts of the market (Enterprise 2017, Schultz 2018) and knows that many employers are looking to hire contractors for WordPress<sup>5</sup> tasks. Although she has no prior experience in similar skills, Maya decides that learning WordPress will allow her to explore new opportunities. Learning WordPress will decrease her skillset cohesion as Word-Press has very little similarity with her graphic design skills.

Once Maya learns Illustrator and CorelDRAW, her prior reputation on Photoshop and Lightroom transfers to Illustrator and CorelDRAW, as the two new skills are similar to the original ones. As a result, she now signals greater knowledge of graphic design skills. Yet, these skills target the same group of employers who are looking for graphic designers.

On the other hand, Maya ’s prior reputation on Photoshop and Lightroom does not necessarily transfer to WordPress, as the two types of skills have little similarity and require different abilities. Even further, Maya has limited information to predict whether she can be a talented WordPress freelancer or whether she will enjoy working on managing digital content as she has not previously exercised any similar skills. Hence, for Maya, exploring by learning WordPress is a riskier option from which she likely expects a significant enough reward (explore under right conditions; Gibson and Birkinshaw 2004, Mom et al. 2009, Rogan and Mors 2014, Lee and Meyer-Doyle 2017, Rosing and Zacher 2017, Lee 2019) that justify—operating outside her comfort zone and—taking that extra risk (White 2009). Unsurprisingly, the reward is clear: Learning WordPress will create entirely new job opportunities, as she can now get hired by employers who are looking for digital content management contractors.

Figure 1 shows the tension between reputation gains and opportunity losses for Maya, as she competes for two hypothetical tasks: one that requires her expertise in graphic design (higher skillset cohesion) and one that requires her knowledge in WordPress (lower skill set cohesion). According to the theoretical framework, Maya ’s perceived reputation in the new graphic design skills is higher than her transferred reputation in Word-Press (reputation gains). However, the additional job opportunities due to learning Illustrator and Corel-DRAW are lower than the entirely new job opportunities due to learning WordPress (opportunity losses). Hence, reputation gains and opportunity losses are at odds: The realized effect of increasing skillset cohesion will depend on the magnitude of these two competing forces.<sup>6</sup>

## 3. Empirical Setting

I use real transactions from a major online labor market GigWork (pseudonym). The data includes 47,638 completed tasks by 12,434 individual contractors. GigWork supports diverse short-term tasks in categories such as web development, administrative, writing, translation, sales, marketing, graphic design, software development, and data science. Overall, there are 533 unique skills that create a total of 16,193 unique observed skillsets.<sup>7</sup> I follow the actions of contractors in the data set for 12 consecutive months. For the rest of the paper, a contractor’s skillset includes the skills that a contractor has exercised in the market.

## 3.1. Measuring Skillset Cohesion and Market Value

The goal is to quantify how adjustments in skillset cohesion affect a contractor’s market value. To do so, I need to measure both skillset cohesion and market value.

3.1.1. Skillset Cohesion. Despite efforts to create skill taxonomies (De Mauro et al. 2016, O\*Net 2018), no prior work has proposed a generalizable methodology for measuring the aggregated degree of similarity between skills in a skillset. One reason might be that capturing associations of skills is inherently hard, as it requires global knowledge of all available skills and the critical ability to identify pairwise similarities. Recent developments in deep learning and the abundance of fine-grained labor data provide an opportunity for new computational metrics to capture contextual associations between skills. Specifically, a distributed representation of words model (Word Embeddings–W2V; Mikolov et al. 2013) can project individual skills into a finite set of numeric dimensions. W2V embeds words from a vocabulary into a lower-dimensional space, in which semantically similar words appear close to each other, while semantically dissimilar words appear far away from each other (Mikolov et al. 2013). In the focal context, a “skill” maps to a “word,” and a “skillset” to a “document.” Based on this representation, W2V projects contextually similar skills (i.e., skills that are often required together to complete a task) close to each other. At the same time, it maps contextually dissimilar skills (i.e., skills that are rarely required together to complete a task) far away from each other (Kokkodis and Ipeirotis 2021).

Figure 1. (Color online) Increasing Skillset Cohesion Results in Relative Reputation Gains and Opportunity Losses  
![](/api/attachments/QBHFMCCN/fulltext/images/729fe78b163dac8f3ee21467daaca3d215c25b4adc629f7456bf41277eec04c1.jpg)  
Notes. The figure shows a contractor who chooses to both increase and decrease her skillset cohesion by acquiring similar and dissimilar skills The contractor’s perceived reputation for the similar skills will be higher than that for the dissimilar skills (reputation gains). However, the simi lar skills will create fewer new job opportunities than the dissimilar skills (opportunity losses). The net effect on the contractor’s market valu will depend on the magnitude of these two competing forces: reputation gains versus opportunity losses.

Once there is a numeric representation of skills, I define skillset cohesion as follows:

$$
\begin{array}{c} \text {Skillset cohesion} (y) = \frac {1}{\binom {| \mathcal {L} |} {2}} \sum_ {i, j} c o s (W 2 V _ {i}, W 2 V _ {j}), \\ \qquad \qquad \qquad \qquad \qquad \qquad \qquad \qquad \forall i \neq j, i \in \mathcal {L}, j \in \mathcal {L}, \end{array}\tag{1}
$$

where L is the set of skills that a contractor has already exercised in the platform, and cos(:) is the cosine similarity between the W2V skill representations $W 2 V _ { i } , W 2 V _ { j }$ Conceptually, this measure captures the average similarity between skills in a skillset. If a contractor focuses only on tasks that require similar skills (e.g., administrative tasks), skillset cohesion will be high. Otherwise, if a contractor works on uncorrelated tasks (e.g., virtual assistant tasks, technical writing tasks, data entry tasks) that require dissimilar skills, skillset cohesion will be low.

3.1.2. Contractor Market Value. I capture a contractor’s market value through two components: hourly compensation wages (hourly wage) and hireability (hiring rate—the ratio of hires over job applications). These two components provide a holistic view of an online contractor’s market value, as they measure both the premiums that contractors charge and the contractors’ ability to find work. (Online Appendix D.3 presents alternative hireability measures.)

## 3.2. Model-Free Evidence

Figure 2 shows model-free information regarding the focal market’s characteristics, the behavior of the focal contractors in terms of skillset cohesion, and evidence that the proposed measure of Equation (1) captures the intended levels of skillset cohesion. Figure 2(a) shows that the focal market mainly supports short-term work: 90% of the completed tasks in the data set require fewer than 100 hours of work, and 50% require fewer than 10 hours of work.

Figure 2(b) shows that contractors exercise, on average, 8.9 skills (median, 8). The number of exercised skills does not necessarily imply cohesion in skillsets as contractors might work on many similar skills (e.g., {java, c#} or {PowerPoint, keynote}). However, intui tively, the more skills contractors exercise on the market, the higher is the chance to complete relatively diverse tasks.

Figure 2(c) shows that the decision to work on new skills (i.e., skills that the contractors have not exercised before) correlates positively with time. On average, during the observational window, contractors work on 1.7 new skills (median, 1).

Through Equation (1), I estimate the level of cohesion of each skillset. Figure 2(d) shows that the vast majority (97%) of contractors in the sample who complete at least three tasks exercise new skills over time that alter their skillset cohesion. In fact, a significant majority (75%) of contractors who complete five or more tasks end up making a mixture of choices over time, some of which increase and some of which decrease their skillset cohesion. As I discuss later in Section 4, this within-contractor variation facilitates the empirical identification of the hypothesized effects.

Finally, Figure 2(e) shows examples of observed skillsets of different levels of skillset cohesion. For visualization purposes, this figure reduces the W2V dimensions to only two through stochastic neighbor embedding (Hinton and Roweis 2002). In practice, W2V maps skills in 10-dimensional vectors. Figure 2(e) displays how similar skills cluster close to each other (e.g., jquery, javascript, php), whereas dissimilar skills appear distant from each other $( \mathrm { e . g . , }$ creative writing versus website development). It further shows how contractors’ choices to exercise different skills generate skillsets of various levels of cohesion . For instance, a contractor that keeps completing tasks that require jquery, javascript, php, html5, and css generates a skillset of high cohesion. On the contrary, a contractor who completes very diverse tasks that require website development, adobe photoshop, t-shirt design, administrative support, Internet marketing, and creative writing generates a skillset of low cohesion. Overall, the plot shows how skillsets of various levels of cohesion can map into a lower-dimensional space of real numbers and provides visual evidence that the proposed metric of Equation (1) captures a skillset’s level of cohesion.

Figure 2. (Color online) Model-Free Evidence of the Focal Data Set  
(a)  
![](/api/attachments/QBHFMCCN/fulltext/images/a8dcada2910df59f5ed366323477273a1f678485ae4b430ac90d04156b3e52c3.jpg)

(b)  
![](/api/attachments/QBHFMCCN/fulltext/images/6bafff9a7dc1ac6d14ec68589af4af18e5b59209f379832526f66027965e596e.jpg)  
(d)

(c)  
![](/api/attachments/QBHFMCCN/fulltext/images/6e992a08fd61544d3e31b55f674ba3f476ead6ffc078bdb6fb6b8e4852619174.jpg)

![](/api/attachments/QBHFMCCN/fulltext/images/8d4a919b61d6a51c531b2e2b943474770c0b3617a9e9d79909f685751b6baedc.jpg)

(e)  
![](/api/attachments/QBHFMCCN/fulltext/images/043878b739e0306bd456075168f2c9e52b58ee25d07e486e22f2b6fffab32b67.jpg)  
Notes. (a) Online labor markets offer primarily short-term contracts. (b) Distribution of the number of skills that contractors exercise on GigWork. (c) Over time, many contractors exercise new skills. (d) 97% of contractors who complete three or more tasks expand their skillsets. (e) Skills according to their word embeddings mapping in a reduced, two-dimensional space through stochastic neighbor embedding (Hinton and Roweis 2002). Contextually similar skills appear close to each other, whereas contextually dissimilar skills appear distant from each other. Skills in trian gles create a skillset of high cohesion; skills in circles create a skillset of medium cohesion; and skills in rectangles create a skillset of low cohesion CI, confidence interval.

## 4. Empirical Analysis

Model-free evidence suggests that contractors make heterogeneous skill choices and follow independent career trajectories with skillsets of varying degrees of cohesion. This existence of variation is critical for the empirical identification strategy. In particular, for a given contractor i at time $t ,$ I estimate the focal effect of skillset cohesion through the following fixed-effects specification:

$$
\text { Market   Value } _ {i t} \sim \boldsymbol {\beta} \mathbf {X} _ {i t} + \delta y _ {i t} + A _ {i} + T _ {t} + \varepsilon ,\tag{2}
$$

where Market Value $\in$ {hourly wage, hiring rate}, $y _ { i t }$ measures the level of cohesion of the current skillset of contractor i at time t through Equation (1), $A _ { i }$ captures contractor fixed effects, $T _ { t }$ captures time fixed effects, and vector $\mathbf { \boldsymbol { X } } _ { i t }$ includes contractor time-varying control variables. The coefficient of interest δ captures the effect of increasing skillset cohesion on the contractor’s market value: if $\delta > 0 ,$ , then increasing cohesion associates with a higher market value; otherwise, if $\delta < 0$ , increasing cohesion associates with a lower market value.

## 4.1. Variables and Descriptive Statistics

Equation (2) controls for a series of observed and unobserved confounding factors that could endogenize the estimates of the focal variable. In particular, the contractor fixed effects account for private information that contractors have when choosing to work on certain tasks, and hence they eliminate the time-invariant portion of the unobserved error that correlates with the contractor’s compensation wages and hiring rates. In addition, contractor fixed effects further encode any other static characteristics (e.g., gender, education, country, field of work, background, age, experience), whereas they also capture the static part of self-selection to work on new skillsets.

Furthermore, the vector of contractor time-varying control variables captures the observed heterogeneity across tasks within each contractor. Controlling for this heterogeneity allows us to isolate better the focal effect of adjusting skillset cohesion. The rich focal data set provides several time-varying measures that, according to prior research, drive contractor compensation wages and hiring rates. In particular, the data set includes the internal log of the marketplace that collects snapshots of each contractor’s profile at the time of a job application, allowing us to form a complete picture of the actual state of each job application.

I begin the construction of the time-varying control variables vector by capturing the observed experience of each contractor at the time of application (contractor experience is a significant driver of a contractor’s market value in these workplaces; see Moreno and Terwiesch 2014, Chan and Wang 2017). I measure experience through snapshots of (1) the total number of completed tasks at the time of each application (“Completed tasks”), (2) the total number of completed hours of work at the time of each application (“Total work-hours”), and (3) the contractor’s total earnings at the time of each application(“Contractor earnings”).

Besides measures of experience, vector ${ \bf { X } } _ { i t }$ needs to include measures of the contractor’s observed prior performance and skillset desirability, as these characteristics also affect market value in online labor markets (Yoganarasimhan 2013, Moreno and Terwiesch 2014, Kokkodis et al. 2015, Lin et al. 2016). I control for a contractor’s prior performance through the listed accumulated feedback score (“Feedback score”) on the contractor’s profile at the time of each application. I proxy the contractor’s skillset desirability through the task-specific ratio of the hired contractors over the total number of applicants (“Skillset desirability”).<sup>8</sup>

Furthermore, to control for the possibility of penalizing contractors who change their behavior over time and apply to relatively more (or less) tasks, I also control for the number of tasks that a contractor is working on concurrently at the time of each application (“Concurrent tasks”) and the contractor’s total number of job applications at the time of each application (“Total applications”). These two controls allow us to isolate better the effect of skillset cohesion on hireability from a change in job-search behavior.

Finally, I control for task-specific observed characteristics that correlate with a contractor’s hiring probability (Gefen and Carmel 2008, Lin et al. 2016). In particular, I consider binary variables that (1) identify whether the contractor was invited to apply for the task at hand (“Invited”; Gefen and Carmel 2008), and (2)

Table 1. Descriptive Statistics of the Focal Data Set

<table><tr><td></td><td>Mean</td><td>Median</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td colspan="6">Dependent variables</td></tr><tr><td>Hourly wage (USD)</td><td>12</td><td>10</td><td>11</td><td>1</td><td>150</td></tr><tr><td>Hiring rate</td><td>0.07</td><td>0.06</td><td>0.07</td><td>0</td><td>1</td></tr><tr><td colspan="6">Focal variable</td></tr><tr><td>Skillset cohesion</td><td>0.59</td><td>0.62</td><td>0.21</td><td>-0.72</td><td>0.99</td></tr><tr><td colspan="6">Contractor time-varying control variables (snapshots of contractor profiles at the time of application)</td></tr><tr><td>Total applications</td><td>48</td><td>29</td><td>60</td><td>0</td><td>1,337</td></tr><tr><td>Total work-hours</td><td>481</td><td>36</td><td>1,393</td><td>0</td><td>36,457</td></tr><tr><td>Contractor earnings (USD)</td><td>4,617</td><td>542</td><td>15,332</td><td>0</td><td>897,526</td></tr><tr><td>Completed tasks</td><td>10</td><td>3</td><td>22</td><td>0</td><td>401</td></tr><tr><td>Feedback score</td><td>4.9</td><td>4.9</td><td>0.21</td><td>1.2</td><td>5</td></tr><tr><td>Concurrent tasks</td><td>6</td><td>3</td><td>7</td><td>0</td><td>90</td></tr><tr><td>Skillset desirability</td><td>0.32</td><td>0.21</td><td>0.28</td><td>0.01</td><td>1</td></tr><tr><td colspan="6">Task-specific variables</td></tr><tr><td>Invited</td><td>0.24</td><td>0</td><td>0.43</td><td>0</td><td>1</td></tr><tr><td>Contract type (fixed-price = 1)</td><td>0.59</td><td>1</td><td>0.49</td><td>0</td><td>1</td></tr></table>

control for the type of contract of each task (hourly rated or fixed priced; Lin et al. 2016).

Table 1 summarizes the dependent, focal, and control variables of this study. Online Appendix A shows the correlations and the variance inflation factors for these variables (Online Appendix 3 and 4): The focal variable captures a different portion of the observed variance than the control variables (no evidence of multicollinearity). I log-transform variables with long tails; I standardize the control variables for straightforward interpretability.

## 4.2. Results

Table 2 shows the resulting coefficients δ, for variations of Equation (2). The first four columns show results for the complete data set; the last two columns focus only on contractors who increase and decrease their skillset cohesion over time (dynamic contractors). Models A1 and B1 show specifications that do not include the focal variable (skillset cohesion). Models A2 and B2 show the complete specification of Equation (2). Because, over time, contractors adjust their skillsets frequently (Figure 2(d)), there is enough within-subject variation for the specifications to identify the focal effect of skillset cohesion.

For both dependent variables in columns A2 and B2, the coefficients δ are statistically significant (p < 0.001). Yet, the signs of the coefficients are at odds. For wages, all else being equal, higher cohesion yields lower premiums: A unit increase in skillset cohesion associates with an 8.6% decrease in hourly wage. This observation supports Hypothesis 2 and suggests an opportunitydominant view: In terms of hourly wages, opportunity losses are greater than reputation gains. Hence, compared with decreasing skillset cohesion, increasing skillset cohesion will result in relatively lower hourly wages.

However, the effect of cohesion on hiring rates is the opposite: All else being equal, higher skillset cohesion increases hireability. In fact, a unit increase of skillset cohesion associates with a 14.2% increase in a contractor’s hiring rate. This observation supports Hypothesis 1 and suggests a reputation-dominant view: in terms of hireability, reputation gains are greater than opportunity losses. Hence, compared with decreasing skillset cohesion, increasing skillset cohesion will result in relatively higher hiring rates.

Of particular interest are the results of columns C1 and C2 that focus on dynamic contractors. These contractors behave according to the hypothetical contractor of Figure 1. Because they choose to increase and decrease their skill set cohesion during a short period, they provide a unique opportunity to empirically compare within-contractor cohesion adjustments. In other words, focusing on this subset of contractors allows us to pinpoint whether the contractors’ differences in skillset cohesion (and not other static contractor-specific choices) drive the observed results. Similar to the results of the complete data set, this analysis of dynamic contractors shows that higher skillset cohesion associates with lower wages and higher hiring rates. Compared with the complete data set, the effect size of cohesion on the dynamic contractors is significantly (at least p < 0.05) larger: A unit increase of skillset cohesion associates with 12.1% lower wages and 17% higher hiring rates.

The opposing effects of skillset cohesion on the two dependent variables reveal the tradeoffs that contractors who adjust their skillsets are likely to face. On the one hand, due to the opportunity-dominant effect on wages, contractors who increase their skillset cohesion will likely experience a relative drop in their hourly wages. On the other hand, due to the reputation-dominant effect on hireability, they will be able to get hired relatively easier.

Table 2. Tradeoffs of Adjusting Skillset Cohesion

<table><tr><td rowspan="3"></td><td colspan="4">All contractors</td><td colspan="2">Dynamic contractors</td></tr><tr><td colspan="2">Hourly wage (log)</td><td colspan="2">Hiring rate (log)</td><td>Hourly wage (log)</td><td>Hiring rate (log)</td></tr><tr><td>(A1)</td><td>(A2)</td><td>(B1)</td><td>(B2)</td><td>(C1)</td><td>(C2)</td></tr><tr><td>Total applications</td><td>0.024***(0.007)</td><td>0.023***(0.007)</td><td>0.027***(0.006)</td><td>0.029***(0.006)</td><td>0.026***(0.008)</td><td>0.027***(0.006)</td></tr><tr><td>Total work-hours</td><td>0.097***(0.027)</td><td>0.097***(0.027)</td><td>0.007(0.030)</td><td>0.006(0.030)</td><td>0.103**(0.033)</td><td>-0.026(0.037)</td></tr><tr><td>Contractor earnings</td><td>-0.122***(0.027)</td><td>-0.119***(0.026)</td><td>0.055.(0.028)</td><td>0.051.(0.028)</td><td>-0.119***(0.032)</td><td>0.046(0.034)</td></tr><tr><td>Completed tasks</td><td>0.066*(0.028)</td><td>0.066*(0.028)</td><td>-0.023(0.026)</td><td>-0.025(0.025)</td><td>0.059.(0.031)</td><td>-0.010(0.025)</td></tr><tr><td>Feedback score</td><td>0.003(0.003)</td><td>0.004(0.003)</td><td>0.020***(0.004)</td><td>0.020***(0.004)</td><td>0.005(0.004)</td><td>0.021***(0.004)</td></tr><tr><td>Invited</td><td>0.054***(0.004)</td><td>0.053***(0.004)</td><td>-0.018***(0.004)</td><td>-0.017***(0.004)</td><td>0.056***(0.005)</td><td>-0.018***(0.004)</td></tr><tr><td>Concurrent tasks</td><td>0.063***(0.011)</td><td>0.061***(0.011)</td><td>-0.076***(0.010)</td><td>-0.072***(0.010)</td><td>0.059***(0.012)</td><td>-0.056***(0.010)</td></tr><tr><td>Skillset desirability</td><td>0.007***(0.002)</td><td>0.006**(0.002)</td><td>0.003*(0.002)</td><td>0.004*(0.002)</td><td>0.007**(0.002)</td><td>0.002(0.002)</td></tr><tr><td>Skillset cohesion</td><td></td><td>-0.086***(0.017)</td><td></td><td>0.142***(0.013)</td><td>-0.121***(0.022)</td><td>0.170***(0.015)</td></tr><tr><td>Contractor fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Contract type fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Time fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td> $R^2$ </td><td>0.914</td><td>0.914</td><td>0.944</td><td>0.945</td><td>0.903</td><td>0.939</td></tr><tr><td>Observations</td><td>47,038</td><td>47,038</td><td>47,038</td><td>47,038</td><td>32,069</td><td>32,069</td></tr></table>

Notes. The first four columns show results of the complete data set (all contractors). The last two columns focus only on contractors who increas and decrease their skillset cohesion during the observation window. Clustered standard errors in parentheses. The constant term is estimated but omitted from the table.

$$
^ {* * *} p <   0. 0 0 1; ^ {* *} p <   0. 0 1; ^ {*} p <   0. 0 5.
$$

## 4.3. Support of the Theoretical Framework and Additional Robustness Tests

Online Appendices B and C provide various empirical tests—including a full mediation analysis—that show support of the theoretical framework and mechanisms of action (reputation gains and opportunity losses). In addition, Online Appendices D and E test the sensitivity of the findings to various sources of endogeneity, selection biases, measurement errors, modeling approaches, and heterogeneity. Online Appendix Table 6 provides an overview of these tests, all of which corroborate the main findings.

## 5. Discussion

This research investigates the tradeoffs of adjusting skillset cohesion in online labor markets. Theoretically, I argue that increasing skillset cohesion results in relative reputation gains and opportunity losses. Methodologically, I measure skillset cohesion through word embeddings. Empirically, I find that higher skillset cohesion associates with lower wages but higher hiring rates.

## 5.1. Research Contributions

This work extends current research in online labor markets by investigating a new question: How does adjusting skillset cohesion affect a contractor’s market value in digi tal workplaces for short-term work? I answer this question by structuring a new theoretical framework that combines prior work on individual-level explorationexploitation with research on contractor behavior in online labor markets to pinpoint the effects of increasing skillset cohesion on two competing forces: reputation gains and opportunity losses. This theoretical framework deepens the understanding of how skill choices affect contractor market value and guides the empirical identification of the studied effects. Through a comprehensive empirical analysis, the study is the first to show that the two competing forces have different effects on different measures of market value. Because opportunity losses have a stronger effect on hourly wages than reputation gains, increasing cohesion results in lower wages. How ever, because the opposite is true in terms of hireability, increasing cohesion increases contractors’ hiring rates. Hence, the research shows that adjusting skillset cohesion results in significant trade-offs that contractors who make these choices should consider.

Beyond expanding the understanding of how different skill choices affect the market value of contractors in a digital workplace, this work also provides a new technique that measures skillset cohesion. In particular, this paper is the first to describe the average similarity of skills in a skillset through word embeddings. Future works investigating various aspects of online labor markets can use the measure of skillset cohesion either as a control or a focal variable. Besides, this methodological contribution spans beyond the specific context of online labor markets. Companies such as LinkedIn, Burning Glass, and Monster can combine the approach with their comprehensive data sets on skillset evolution and career choices to investigate how adjusting skillset cohesion affects the market value of offline workers.

The research further answers the recent call for studies that focus on the individual-level explore-exploit dilemma (Lavie et al. 2010, Rogan and Mors 2014, Lee and Meyer-Doyle 2017). Specifically, although prior research agrees that studies of individual-level exploration-exploitation are particularly important, such studies are rare (Raisch et al. 2009), primarily due to a lack of individual-level observations (Rogan and Mors 2014, Lee and Meyer-Doyle 2017). In fact, prior works often use organization-level data to infer individual-level behavior (Gibbons and Waldman 2004, Rogan and Mors 2014). The unique data set presents an opportunity to study the individual-level explore-exploit dilemma in a brand new context (online labor markets) that allows the detailed observation of online contractors’ microactions. As a result, the work demonstrates new exploration-exploitation tradeoffs that appear in the context of short-term remote work.

## 5.2. Implications for Online Contractors and Platform Managers

Given the projected growth of the number of online contractors in the coming years (Agile-1 2016, Sundararajan 2016) and their dynamic nature (Oliver 2015, Kokkodis and Ipeirotis 2016), understanding the tradeoffs of different career choices could help contractors make betterinformed skill choices and provide platform managers with an additional tool to facilitate contractor success. In particular, this work is the first to provide online contractors with an explanation of the tradeoffs they should expect when adjusting their skillset cohesion. Digital workplaces can provide such information to contractors through their usual means of communication (i.e., blog posts and social media posts). Even further, markets can explore the heterogeneous effects of cohesion (Online Appendix D.4) and provide personalized information to different types of contractors. Through such interventions, contractors can make better choices, improving the platform’s talent base.

Furthermore, measuring skillset cohesion and modeling contractor dynamic behavior provide platform managers with the means to improve their data analytics functions. Specifically, through sequential modeling of career paths (Online Appendix E), managers can monitor dynamic career trends of contractors and make targeted interventions to guide contractors both in skill acquisition and task selection. In addition, skillset cohesion is likely to be a key component in building matching systems and improve candidate recommendations (Kokkodis et al. 2015, Abhinav et al. 2017, Kokkodis 2018). Similarly, newly designed reputation systems can consider the dynamic nature of skillset cohesion to generate more accurate estimates of skillsetspecific candidate quality (Kokkodis and Ipeirotis 2013, Daltayanni et al. 2015, Kokkodis 2021). Overall, through measuring skillset cohesion and modeling career paths, managers can better monitor skillset trends and get a more accurate view of their marketplace.

## 5.3. Limitations and Future Directions

The work relies on observational data. This limits the ability to uniquely attribute the observed effects to the hypothesized mechanism of reputation gains and opportunity losses. The empirical analysis in Online Appendices B and C shows that indeed the hypothe sized mechanisms contribute to the observed effects. However, I cannot eliminate any other alternative mechanisms that could also be contributing to creating a multicausal structure that comprises these tradeoffs. To fully isolate the effect of reputation gains and opportunity losses, a different type of study is needed, one that will likely require (1) surveying employer perceptions of reputation and (2) random assignment of new skills (or new skill recommendations). However, such a study would also have limitations, including but not limited to ethical considerations of skill randomization and inherent survey biases. Regardless, I hope the work will motivate researchers to pursue these directions in the future.

Another limitation of the approach is that it does not explicitly model the equilibrium effects of contractor behavior. For instance, if a platform broadcasts the find ings, contractors might start considering trade-offs of adjusting their skillset cohesion and alter their skill choices. If such a shift in contractor behavior is systematically one sided, it could potentially alter the observed results. However, given that the study provides information about the tradeoffs of cohesion and does not necessarily make recommendations to either increase or decrease cohesion, I argue that it is unlikely to generate such a homogeneous shift in contractor behavior. Future research can extend the theoretical framework to include equilibrium effects by explicitly modeling supply changes and explain how such changes could affect the results.

## 5.4. Conclusion

In conclusion, this work is the first to investigate how adjusting skillset cohesion affects contractors in online labor markets for short-term work. The theoretical and empirical analyses illustrate the trade-offs of increasing skillset cohesion . In terms of compensation wages, opportunity losses are greater than reputation gains and generate a negative net effect of increasing cohesion . However, in terms of hireability, reputation gains are greater than opportunity losses and drive a positive effect of increasing cohesion . These tradeoffs can guide contractors to make better-informed decisions when expanding their skillsets and platform managers to make targeted interventions.

## Endnotes

<sup>1</sup> The reverse tradeoffs are true for acquiring dissimilar skills that decrease skillset cohesion.

<sup>2</sup> Skill acquisition does not affect static personal characteristics such as gender and location.

<sup>3</sup> This is a rational assumption in the context as contractors receive a constant flow of information regarding highly desirable skills (Enterprise 2017, Patel et al. 2017, Schultz 2018, Kokkodis and Ipeirotis 2021).

<sup>4</sup> Graphic designers frequently use software such as Photoshop, Lightroom, Illustrator, and CorelDRAW. See https://en.wikipedia. org/wiki/Graphic\_design.

<sup>5</sup> WordPress is a software application that manages the creation and modification of digital content. WordPress is relatively easy to learn (Editorial 2020).

<sup>6</sup> I do not argue that WordPress creates, in general, more job opportunities than CorelDraw across contractors. Instead, for Maya, who is already an expert in graphic design, the relative increase in job opportunities due to acquiring WordPress will likely be greater than the relative increase in job opportunities due to acquiring CorelDraw.

<sup>7</sup> I use standardized skill names provided by GigWork. Figure 2(e) shows examples of actual skills and skillsets.

<sup>8</sup> Intuitively, the more desirable the skillset, the higher the ratio of hired contractors over applicants.

## References

Abhinav K, Dubey A, Jain S, Virdi G, Kass A, Mehta M (2017) Crow dadvisor: A framework for freelancer assessment in online marketplace. 2017 IEEE/ACM 39th Internat. Conf. Software Engrg.: Software Engrg. Practice Track (ICSE-SEIP), 93–102.

Agarwal R, Ohyama A (2013) Industry or academia, basic or applied? Career choices and earnings trajectories of scientists. Management Sci. 59:950–970.

Agile-1 (2016) Gig economy. Accessed November 28, 2020, http:// www.hrotoday.com/wp-content/uploads/2016/07/Whitepaper\_ Agile2016-single.pdf.

Agrawal A, Lacetera N, Lyons E (2013) Does information help or hinder job applicants from less developed countries in online markets? Technical report, National Bureau of Economic Re search, Cambridge, MA.

Agrawal A, Horton JJ, Lacetera N, Lyons E (2015) Digitization and the contract labor market. Economic Analysis of the Digital Economy, 219. https://www.nber.org/books-and-chapters/economic-analysisdigital-economy/digitization-and-contract-labor-market-researchagenda.

Allon G, Bassamboo A, C¸il EB (2012) Large-scale service marketplaces: The role of the moderating firm. Management Sci. 58:1854–1872.

Arora A, Forman C (2007) Proximity and information technology outsourcing: How local are it services markets? J. Management Inform. Systems 24:73–102.

Autor DH (2001) Wiring the labor market. J. Econom. Perspective 15:25–40.

Autor DH, Katz LF, Krueger AB (1998) Computing inequality: Have computers changed the labor market? Quart. J. Econom. 113: 1169–1213.

Baumann O, Stieglitz N (2014) Rewarding value-creating ideas in organizations: The power of low-powered incentives. Strategic Management J. 35:358–375.

BCG (2018) Toward a Reskilling Revolution: A Future of Jobs for All (World Economic Forum, Boston Consulting Group).

Becker GS (1962) Investment in human capital: A theoretical analysis. J. Political Econom. 70(5):9–49.

Beckman CM, Haunschild PR, Phillips DJ (2004) Friends or strangers? Firm-specific uncertainty, market uncertainty, and network partner selection. Organ. Sci. 15:259–275.

Berinsky AJ, Huber GA, Lenz GS (2012) Evaluating online labor markets for experimental research: Amazon.com’s mechanical turk. Political Anal. 20:351–368.

Blundell R, Dearden L, Meghir C, Sianesi B (1999) Human capital investment: The returns from education and training to the individual, the firm and the economy. Fiscal Stud. 20:1–23.

Bosma N, Van Praag M, Thurik R, De Wit G (2004) The value of human and social capital investments for the business perform ance of startups. Small Bus. Econom. 23:227–236.

Brier E, Pearson R (2018) Upwork’s SVP of marketing explains what it takes to perfect an offering that relies on people. Accessed November 28, 2020, https://www.prnewswire.com/news-releases/snagajobappoints-former-upwork-ceo-to-board-of-directors-300417689.html.

Campbell BA, Coff R, Kryscynski D (2012) Rethinking sustained competitive advantage from human capital. Acad. Management Rev. 37:376–395.

Chan J, Wang J (2017) Hiring preferences in online labor markets: Evidence of a female hiring bias. Management Sci. 64:2973–3468.

Chen DL, Horton JJ (2016) Are online labor markets spot markets for tasks? A field experiment on the behavioral response to wage cuts. Inform. Systems Res. 27:403–423.

Christoforaki M, Ipeirotis PG (2015) A system for scalable and reliable technical-skill testing in online labor markets. Comput. Networks 90:110–120.

Claussen J, Khashabi P, Kretschmer T, Seifried M (2018) Knowledg work in the sharing economy: What drives project success in online labor markets? Preprint, submitted January 23, https:// dx.doi.org/10.2139/ssrn.3102865.

Coff RW (1997) Human assets and management dilemmas: Coping with hazards on the road to resource-based theory. Acad. Man agement Rev. 22:374–402.

Daltayanni M, de Alfaro L, Papadimitriou P (2015) Workerrank: Using employer implicit judgements to infer worker reputation. Proc. 8th ACM Internat. Conf. Web Search Data Mining (ACM, New York), 263–272.

De Mauro A, Greco M, Grimaldi M, Nobili G (2016) Beyond data scientists: A review of big data skills and job families. Toward a New Architecture of Knowledge: Big Data, Culture and Creativity, 1844–1857. https://www.academia.edu/26869215/Beyond\_Data\_Scientists\_ a\_Review\_of\_Big\_Data\_Skills\_and\_Job\_Families.

Demerouti E (2006) Job characteristics, flow, and performance: The moderating role of conscientiousness. J. Occupational Health Psych 11:266.

Denrell J, March JG (2001) Adaptation as information restriction: The hot stove effect. Organ. Sci. 12:523–538.

Dey D, Fan M, Zhang C (2010) Design and analysis of contracts for software outsourcing. Inform. Systems Res. 21:93–114.

Djumalieva J, Sleeman C (2018) An open and data-driven taxonomy of skills extracted from online job adverts. Developing Skills in a Changing World of Work: Concepts, Measurement and Data Applied in Regional and Local Labour Market Monitoring Across Europe, 425 http://escoe-website.s3.amazonaws.com/wp-content/uploads/ 2018/08/29113127/ESCoE-DP-2018-13.pdf.

Editorial (2020) How to learn wordpress for free in a week (or less). Accessed July 5, 2020, https://www.wpbeginner.com/beginnersguide/how-to-learn-wordpress-for-free-in-a-week-or-less/.

Enterprise (2017) Quarterly trends report. Accessed November 28, 2020, https://www.upwork.com/s/enterprise-trends/.

Filippas A, Horton JJ, Golden J (2018) Reputation inflation. Proc. 2018 ACM Conf. Econom. Comput. (ACM, New York), 483–484.

Gefen D, Carmel E (2008) Is the world really flat? A look at offshoring at an online programming marketplace. Management Inform. Systems Quart. 32(2):367–384.

Ghani E, Kerr WR, Stanton C (2014) Diasporas and outsourcing: Evidence from odesk and India. Management Sci. 60:1677–1697.

Gibbons R, Waldman M (2004) Task-specific human capital. Amer. Econom. Rev. 94:203–207.

Gibson CB, Birkinshaw J (2004) The antecedents, consequences, and mediating role of organizational ambidexterity. Acad. Management J. 47:209–226.

Good D, Michel EJ (2013) Individual ambidexterity: Exploring and exploiting in dynamic contexts. J. Psych. 147:435–453.

Gopal A, Sivaramakrishnan K, Krishnan MS, Mukhopadhyay T (2003) Contracts in offshore software development: An empiri cal analysis. Management Sci. 49:1671–1683.

Graves LM, Ruderman MN, Ohlott PJ, Weber TJ (2012) Driven to work and enjoyment of work: Effects on managers’ outcomes. J. Management 38:1655–1680.

Hinton GE, Roweis ST (2002) Stochastic neighbor embedding. Becker S, Thrun S, Obermayer K, eds. Adv. Neural Inform. Processing Systems, vol. 15 (MIT Press), 857–864.

Holmqvist M (2004) Experiential learning processes of exploitation and exploration within and between organizations: An empiri cal study of product development. Organ. Sci. 15:70–81.

Holt CA, Laury SK (2002) Risk aversion and incentive effects. Amer. Econom. Rev. 92:1644–1655.

Hong Y, Pavlou PA (2017) On buyer selection of service providers in online outsourcing platforms for IT services. Inform. Systems Res. 28:547–562.

Hong Y, Wang C, Pavlou PA (2015) Comparing open and sealed bid auctions: Evidence from online labor markets. Inform. Systems Res. 27:49–69.

Horton JJ, Chilton LB (2010) The labor economics of paid crowd sourcing. Proc. 11th ACM Conf. Electron. Commerce (ACM, New York), 209–218.

Horton JJ, Rand DG, Zeckhauser RJ (2011) The online laboratory: Conducting experiments in a real labor market. Experiment. Econom. 14:399–425.

Institute of Business Value (2019) The enterprise guide to closing the skills gap. Accessed December 2, 2019, https://www.ibm.com downloads/cas/EPYMNBJA.

Ipeirotis PG, Provost F, Wang J (2010) Quality management on Amazon Mechanical Turk. Proc. Workshop on Human Comput., 64–67.

Jain H, Padmanabhan B, Pavlou PA, Santanam RT (2018) Call for papers: Special issue of information systems research–humans, algorithms, and augmented intelligence: The future of work, organizations, and society. Inform. Systems Res. 29:250–251.

Johnson T (1970) Returns from investment in human capital. Amer. Econom. Rev. 60:546–560

Kahneman D, Lovallo D (1993) Timid choices and bold forecasts: A cognitive perspective on risk taking. Management Sci. 39:17–31.

Kokkodis M (2018) Dynamic recommendations for sequential hiring decisions in online labor markets. Proc. 24th ACM SIGKDD Internat. Conf. Knowledge Discovery Data Mining (ACM, New York), 453–461.

Kokkodis M (2019) Reputation deflation through dynamic expertise assessment in online labor markets. World Wide Web Conf. (ACM, New York), 896–905

Kokkodis M (2021) Dynamic, multidimensional, and skillset-specific reputation systems for online work. Inform. Systems Res. 32:688–712.

Kokkodis M, Ipeirotis PG (2013) Have you done anything like that? Predicting performance using inter-category reputation. Proc. 6th ACM Internat. Conf. Web Search Data Mining (ACM, New York), 435–444.

Kokkodis M, Ipeirotis PG (2014) The utility of skills in online labor markets. Proc. Internat. Conf. on Inform. Systems.

Kokkodis M, Ipeirotis PG (2016) Reputation transferability in online labor markets. Management Sci. 62:1687–1706.

Kokkodis M, Ipeirotis PG (2021) Demand-aware career path recommendations: A reinforcement learning approach. Management Sci. 67:4362–4383.

Kokkodis M, Ipeirotis PG (2022) The good, the bad, and the unhirable: Recommending job applicants in online labor markets. Working paper, Boston College, Boston.

Kokkodis M, Ransbotham S (2022) Learning to successfully hire in online labor markets. Management Sci., ePub ahead of print August 26, https://doi.org/10.1287/mnsc.2022.4426.

Kokkodis M, Adamopoulos P, Ransbotham S (2022) Asymmetric reputation spillover effects from digital agencies in online markets. Management Inform. Systems Quart. Forthcoming.

Kokkodis M, Papadimitriou P, Ipeirotis PG (2015) Hiring behavior models for online labor markets. Proc. 8th ACM Internat. Conf. Web Search Data Mining (ACM, New York), 223–232.

Kuhn P, Skuterud M (2004) Internet job search and unemployment durations. Amer. Econom. Rev. 94:218–232.

Lauren D (2017) Snagajob appoints former Upwork CEO to board of directors. Accessed November 28, 2020, https://www.prne wswire.com/news-releases/snagajob-appoints-former-upwork ceo-to-board-of-directors-300417689.html.

Lavie D, Stettner U, Tushman ML (2010) Exploration and exploitation within and across organizations. Acad. Management Ann. 4:109–155.

Lee S (2019) Learning-by-moving: Can reconfiguring spatial proximity between organizational members promote individual-level exploration? Organ. Sci. 30:467–488.

Lee S, Meyer-Doyle P (2017) How performance incentives shape individual exploration and exploitation: Evidence from micro data. Organ. Sci. 28:19–38.

Lepak DP, Snell SA (1999) The human resource architecture: Toward a theory of human capital allocation and development. Acad Management Rev. 24:31–48.

Levinthal DA, March JG (1993) The myopia of learning. Strategic Management J. 14:95–112.

Lin M, Viswanathan S (2015) Home bias in online investments: An empirical study of an online crowdfunding market. Management Sci, 62:1393-1414

Lin M, Liu Y, Viswanathan S (2016) Effectiveness of reputation in contracting for customized production: Evidence from online labor markets. Management Sci. 64:345–359.

March JG (1991) Exploration and exploitation in organizational learning. Organ. Sci. 2:71–87.

Mikolov T, Chen K, Corrado G, Dean J (2013) Efficient estimation of word representations in vector space. Preprint, submitted September 7, https://arxiv.org/abs/1301.3781.

Mom TJM, Van Den Bosch FAJ, Volberda HW (2007) Investigating managers’ exploration and exploitation activities: The influence of top-down, bottom-up, and horizontal knowledge inflows. J. Management Stud. 44:910–931.

Mom TJM, Van Den Bosch FAJ, Volberda HW (2009) Understanding variation in managers’ ambidexterity: Investigating direct and interaction effects of formal structural and personal coordi nation mechanisms. Organ. Sci. 20:812–828.

Mom TJM, Chang Y-Y, Cholakova M, Jansen JJP (2019) A multilevel integrated framework of firm HR practices, individual ambidexterity, and organizational ambidexterity. J. Management 45:3009–3034.

Moreno A, Terwiesch C (2014) Doing business with strangers: Reputa tion in online service marketplaces. Inform. Systems Res. 25:865–886.

Navarro DJ, Newell BR, Schulze C (2016) Learning and choosing in an uncertain world: An investigation of the explore–exploit dilemma in static and dynamic environments. Cognitive Psych. 85:43–77.

Nelson RR (2009) An Evolutionary Theory of Economic Change (Har vard University Press, Cambridge, MA).

Oliver B (2015) Redefining graduate employability and work-integrated learning: Proposals for effective higher education in disrupted economies. J. Teaching Learn. Graduate Employability 6:56.

O\*Net (2018) Taxonomies of skills. Accessed November 28, 2020 https://www.onetonline.org/find/descriptor/browse/Skills/.

Patel B, Kakuste V, Eirinaki M (2017) CaPaR: A career path recommendation framework. 2017 IEEE 3rd Internat. Conf. Big Data Comput. Service Appl. (BigDataService), 23–30.

Perryman AA, Combs JG (2012) Who should own it? An agencybased explanation for multi-outlet ownership and co-location in plural form franchising. Strategic Management J. 33:368–386.

Rahman HA (2018) Reputational Ploys: Reputation and Ratings in Online Markets (Academy of Management Proceedings).

Raisch S, Birkinshaw J, Probst G, Tushman ML (2009) Organiza tional ambidexterity: Balancing exploitation and exploration for sustained performance. Organ. Sci. 20:685–695.

Robinson AT, Marino LD (2015) Overconfidence and risk perceptions: Do they really matter for venture creation decisions? Internat. Entrepreneurial Management J. 11:149–168.

Rogan M, Mors ML (2014) A network perspective on individual level ambidexterity in organizations. Organ. Sci. 25:1860–1877.

Rosing K, Zacher H (2017) Individual ambidexterity: The duality of exploration and exploitation and its relationship with innovative performance. Eur. J. Work Organ. Psych. 26:694–709.

Schilling MA, Vidal P, Ployhart RE, Marangoni A (2003) Learning by doing something else: Variation, relatedness, and the learning curve. Management Sci. 49:39–56.

Schnellba¨cher B, Heidenreich S, Wald A (2019) Antecedents and effects of individual ambidexterity: A cross-level investigation of exploration and exploitation activities at the employee level Eur. Management J. 37:442–454.

Schultz TW (1961) Investment in human capital. Amer. Econom. Rev. 51:1–17.

Schultz C (2018) Upwork press release. Accessed November 28, 2020 https://www.upwork.com/press/2018/05/01/q1-2018-skillsindex/.

Statista Research Department (2021) Online shopping behavior in the United States: Statistics & facts. Accessed February 21, 2021, https:// www.statista.com/topics/2477/online-shopping-behavior/.

Stevenson B (2009) The Internet and job search. Studies of Labor Mar ket Intermediation (University of Chicago Press, Chicago), 67–86.

Sundararajan A (2016) The Sharing Economy: The End of Employment and the Rise of Crowd-Based Capitalism (MIT Press, Cambridge, MA).

Tempelaar MP, Rosenkranz NA (2019) Switching hats: The effect of role transition on individual ambidexterity. J. Management 45:1517–1539.

White A (2009) From Comfort Zone to Performance Management (White & MacLean Publishing, Baisy-Thy, Belgium).

Wiersma E (2007) Conditions that shape the learning curve: Factors that increase the ability and opportunity to learn. Management Sci. 53:1903–1915.

Wiseman RM, Gomez-Mejia LR (1998) A behavioral agency model of managerial risk taking. Acad. Management Rev. 23:133–153.

Yoganarasimhan H (2013) The value of reputation in an online freelance marketplace. Marketing Sci. 32:860–891.

Zenger TR, Lazzarini SG (2004) Compensating for innovation: Do small firms offer high-powered incentives that lure talent and motivate effort? Management Decision Econom. 25:329–345.

C<sub>opy</sub>ri<sub>g</sub>ht 2023 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
