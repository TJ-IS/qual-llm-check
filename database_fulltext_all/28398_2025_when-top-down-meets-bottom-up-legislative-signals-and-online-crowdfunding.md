---
otero_id: 28398
otero_key: "WENUX7NK"
title: "When Top-Down Meets Bottom-Up: Legislative Signals and Online Crowdfunding"
authors: "Anqi Wu; Aravinda Garimella; Ramanath Subramanyam"
year: "2025"
journal: "Information Systems Research"
doi: "10.1287/isre.2022.0536"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
![](/api/attachments/WENUX7NK/fulltext/images/43c1ae928004590f72b027059d6b7bcd47e711725efe2b12b6b7be949c236248.jpg)

# When Top-Down Meets Bottom-Up: Legislative Signals and Online Crowdfunding

Anqi Wu,<sup>a</sup> Aravinda Garimella,<sup>b,</sup>\* Ramanath Subramanyam<sup>b</sup>

<sup>a</sup> Department of Information Systems and Business Analytics, Florida International University, Miami, Florida 33199; <sup>b</sup> Business Administration, University of Illinois Urbana-Champaign, Champaign, Illinois 61820

Contact: anwu@fiu.edu, https://orcid.org/0000-0001-5348-4932 (AW); aravinda@illinois.edu, https://orcid.org/0000-0003-0804-4836 (AG); rsubrama@illinois.edu, https://orcid.org/0000-0003-1938-3745 (RS)

Received: September 23, 2022 Revised: September 13, 2023; May 23, 2024; October 17, 2024 Accepted: December 3, 2024 Published Online in Articles in Advance: January 31, 2025

https://doi.org/10.1287/isre.2022.0536

Copyright: © 2025 The Author(s)

Abstract. Over the last two decades, online crowdfunding platforms have facilitated fundraising efforts to alleviate resource shortages across various sectors. As these platforms become increasingly important channels for bottom-up resource mobilization, it is essential to understand their vulnerability to shifts in public perception caused by top-down, offplatform events. In this paper, we examine the effect of an important top-down factor, legislative signals, on online giving behavior in the context of public education. We analyze how the ratification of the prominent Every Student Succeeds Act (ESSA) impacted donors decisions on a leading education crowdfunding platform. Importantly, we examine the effects of the signal sent by the state ratification of the act itself rather than any effect derived from the actual implementation of the act. We compiled a multidimensional and granular data set on public schools and online charitable contributions. Detailed empirical analyses revealed a substantial shift in donation patterns and evidence of two contrasting donor tendencies. Although donors contributed more to local initiatives following the ratification, they contributed less to nonlocal initiatives, leading to a substantial net decline in the funds raised. We established two mechanisms through which these effects manifested: information push and information pull. Using both mechanisms, we show that donors who have a higher awareness of the legislative signal exhibit stronger shifts in donation behavior. Importantly, as a consequence of the shift in contributions to local initiatives, we find that schools with students of lower socioeconomic status (SES) experienced a sharper decline in the proportion of projects funded than schools with students of higher SES. Our work has important implications for platform designers, donor communities, public school administrators, teachers, and policymakers.

History: Jason Thatcher, Senior Editor; Yuliang Yao, Associate Editor.

Open Access Statement: This work is licensed under a Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License. You are free to download this work and share with others, but cannot change in any way or use commercially without permission, and you must attribute this work as “Information Sustems Research. Copyright © 2025 The, Author(s). bttps: //doi,org /10.1287 isre.2022.0536, used under a Creative Commons Attribution License: https://creativecommons.org licenses/bv-nc-nd/4.0/.

Funding: The authors are grateful for the financial support from the Gies College of Business through the Gies Faculty Research Excellence Grant. The authors also thank their institutions (the University of Illinois Urbana-Champaign and Florida International University) for supporting this research. Supplemental Material: The online appendices are available at https://doi.org/10.1287/isre.2022.0536.

Keywords: digital platforms • online crowdfunding • signaling • quasi-experiment

## 1. Introduction

Equity and adequacy in funding are prerequisites for the provision of equal educational opportunity (Buchanan 1950, Augenblick et al. 1997, Baker 2021). However, it is a widely established concern that public schools in the United States are both underfunded and inequitably funded (Farrie and Johnson 2015). Educators often dip into their own pockets, with teachers in high-poverty schools spending more of their own money on basic classroom supplies (Walker

2019). Limited budgets and red tape have led many teachers to increasingly seek outside funds for classroom projects.

Over the last two decades, online crowdfunding platforms have facilitated fundraising efforts to alleviate resource shortages (Burtch et al. 2013, 2014; Hong et al. 2018; Burtch and Chan 2019; Geva et al. 2019; Kim and Viswanathan 2019; Lin et al. 2022). In education, platforms such as DonorsChoose.org have catalyzed teachers’ fundraising efforts to mitigate resource shortages in their classrooms, with successful campaigns providing teachers with speedy and efficient access to resources. Online crowdfunding platforms can mitigate, to some extent, market failures in public services and enable matching between demand and supply, potentially transcending geographic constraints. For example, DonorsChoose recently highlighted that more than 1.6 billion dollars have been raised since the year 2000, with all funds going to teacher-led projects fulfilling school needs.<sup>1</sup>

This bottom-up resource mobilization through crowdfunding platforms occurs in a larger context characterized by top-down activity such as legislation from governmental institutions. In the United States, periodically reauthorized federal initiatives (e.g., Elementary and Secondary Education Act: 1965, No Child Left Behind: 2002, Every Student Succeeds Act: 2015) have taken different approaches to address public education standards, accountability, proficiency, and funding concerns. Most recently, the Every Student Succeeds Act (ESSA), a bipartisan effort signed into law in December 2015, was enacted, offering states increased flexibility regarding accountability and proficiency standards within a federal framework (McGuinn 2016, Egalite et al. 2017, Jacob 2017, Hess and Eden 2021). ESSA falls into a category of laws known as devolution laws, which emphasize the decentralization of public sector responsibilities toward state and local governments (Senate Committee on Health, Education, Labor, and Pensions<sup>2</sup>). Long before any initiatives pursuant to the legislation are actually implemented, the announcement of such laws can serve as a signal to the community and shift public perceptions about societal needs (Tankard and Paluck 2016).

Although a growing stream of information systems (IS) research has examined charitable crowdfunding, there is a paucity of research examining the interaction between top-down signals (from the institutional environment) and bottom-up efforts (donor contributions on a crowdfunding platform) aimed at addressing resource gaps (He et al. 2024). One barrier to conducting such studies has been the lack of identification events needed to causally estimate these effects. In this paper, leveraging one of the largest education policies in the last two decades, we examine whether and how the ratification of ESSA affected donor behavior and the overall online fundraising ecosystem. Drawing from theories in philanthropy, public goods research, and information economics, we contribute to information systems literature that examines factors that influence crowdfunding success (Burtch et al. 2013, 2014, 2015; Younkin and Kuppuswamy 2018; Burtch and Chan 2019; Yang et al. 2020; Lin et al. 2022).

Legislative signals can influence donor behavior in two ways. First, the signal could alter overall giving behavior on the platform through changes in the overall public perceptions of need (Wagner and Wheeler 1969) and shifts in perceived psychological benefits or cost-benefit tradeoffs (Bekkers and Wiepking 2011). Alternatively, donors might simply realign their interests on the platform to certain subsets of initiatives, such as those favoring local schools whose needs might be better known to them. Hence, we believe that it is essential to separately examine whether and how overall giving and local giving are affected by such sig naling events. Accordingly, our research questions are as follows. (1) What are the effects of a legislative signal on overall and local donation behavior online? (2) What are the mechanisms underlying these effects?

We collated a 20-quarter (2015Q1–2019Q4) panel data set, representing 73,303 schools (nearly 70% of all U.S. K-12 public schools) and totaling 4,40,617 observations. These data consist of fundraising outcomes of K-12 schools whose teachers raised funds on DonorsChoose. We combined these rich data with school demographics and characteristics collected from the National Center for Education Statistics (NCES) and further augmented this data with ESSA-related Internet search data and media coverage data gathered from Google Trends and LexisNexis, respectively.

We adopted a staggered difference-in-differences research design consistent with state-of-the-art meth odological approaches (Seamans and Zhu 2014, Zhang et al. 2024) used to examine the effects of exogenous policy changes. Our focus is on changes in donor behavior on the online platform in response to states ESSA ratifications. There are at least two critical event windows that are relevant to wide-scoped federal legislation, such as ESSA. The first is the federal announce ment by the president reauthorizing the governing ESEA 1965 (December 2015). The second is the sign-off on each state’s submitted plan by the U.S. Department of Education. ESSA plans for different states went into effect at different points in time during the 2017–2018 school year (see Online Appendix A.1). Because the state plan signoff by the U.S. Department of Education is the tangible and concrete event that officially signals legislative action, we treat this as the primary event for each state.<sup>3</sup> A key strength of our research design is that the geographic and temporal variation in the ratification events allow us to disentangle the effect of the legislative signal on donation behavior from macro trends (Parvin and Beruvides 2021). For methodologi cal triangulation, we also employed an event-study analysis that examined both short-term and longerterm effects, finding consistent results.

We identified a substantial shift in donation patterns following state ESSA ratifications, with donations becoming more local following this event. We found an 11.9% increase in the donations contributed by local donors, who used to account for 25% of the total crowdfunding amount before the ratifications, and a 15.7% decrease in the donations contributed by nonlocal donors. Importantly, we observed a net negative effect following states

ESSA ratifications, with a significant drop—an 8% decline in total donation amounts, representing a \$2.45 million drop per quarter for the schools in our sample—across the platform. We further stratified the schools based on the social and economic status (SES) of their students and found that low-SES schools experienced a more precipitous drop in funding compared with higher-SES schools. We identified two awareness mechanisms through which these effects manifest: information push and information pull. Our analyses revealed that donors with a higher awareness of ESSA exhibited stronger shifts in donation behavior relative to others.

Our study makes several important contributions to IS literature and practice. First, there is a clear paucity of research on how signals from the external institutiona environment influence activities on crowdfunding platforms (He et al. 2024). Our work directly examines this effect by adding an underexamined antecedent to fundraising performance. Importantly, we take a deliberate approach toward consideration of the institutional context and its interaction with the platform. By doing so, we offer insights that can inform platform design decisions in a more context-aware manner. Second, we combine theoretical perspectives on familiarity bias and signaling to empirically establish geographically asymmetric effects of legislative signaling on local and nonlocal crowdfunding outcomes. Our study is the first to highlight that legislative signals can significantly influence donor preferences for geographically proximal causes, thereby advancing the field’s understanding of home bias in crowdfunding research. Third, we examined two distinct awareness channels, information push and information pull, through which these effects manifest. Interestingly, these mechanisms function in different ways: Although the increase in local donations was driven largely through information pull, the decrease in nonlocal donations was more strongly impacted by information push. These findings have important practical implications. For example, to mitigate the resource-divide problem in public education that is further exacerbated by hyper-localization following such events, platforms should consider implementing timed and targeted nudges surrounding major legislative announcements. Carefully designed matching processes could help platforms mitigate, at least to some extent, inequitable access to resources in education.

## 2. Research Context

## 2.1. DonorsChoose

Our data were sourced from DonorsChoose.org, a leading online crowdfunding platform that allows individuals to donate directly to public school classroom projects posted by teachers. By early 2024, the platform had raised more than 1.6 billion USD, and more than 80% of U.S. public schools (from grades Pre-K to 12) the majority of requests coming from low-resource schools (Figure 1(a)).

Project page descriptions include information such as the specific needs, the name of the school, the school’s location and poverty level, the subject taught, the students’ grade level, the number of students impacted by the project, and the number of donors that have contributed to the project (Figure 1(b)). DonorsChoose uses an “all-or-nothing” model, where a teacher receives donations only if the amount raised equals or exceeds the funding goal. If a partially funded project expires (i.e., fails to attract full funding within a four-month period), the donations are refunded to donors as campaign credits, which can be used for other projects.

Figure 1. Public Schools Raise Funds Through DonorsChoose.org  
![](/api/attachments/WENUX7NK/fulltext/images/7fda4e3e6d8ca458c7c567ec1d355505ead6f14e760863551feda91aecb03673.jpg)  
Notes. (a) Proportion of projects by the poverty level of the school making the reguest, 2015–2019; 45% of all reguests come from schools in the highest poverty bracket (in which 65% or more students receive free or reduced-price meals). (b) Example of a project page on DonorsChoose.org.

## 2.2. ESSA: Delegation of Authority to States

ESSA is a comprehensive and elaborate law with nine titles spanning 392 pages<sup>5</sup> that was signed into law on December 10, 2015. ESSA is a major reauthorization of the 1965 Elementary and Secondary Education Act (ESEA) and seeks to decentralize public education by granting states and local school districts greater authority and flexibility in determining accountability and proficiency standards. ESSA attracted substantial local and national media coverage and was described as “the largest devolution of federal control to the states in a quarter-century” (Wall Street Journal 2015).

We collected more than 10,000 local and national news articles between February 1, 2015, and March 31, 2017, that contained the term “Every Student Succeeds Act” from Lexis Nexis and analyzed this content using natural language processing algorithms. This analysis revealed that more than 50% of all ESSA-related news articles emphasized devolution as the most important theme (see Section D.1 in the Online Appendix for details). Our interviews with education policy researchers and public school teachers corroborate that despite the breadth and complexity of ESSA, devolution was the most salient theme in ESSA media coverage. In Online Appendix A.2, we provide a summary of news articles and research papers that document devolution as a salient theme of ESSA.

Although ESSA was signed into law in December 2015, ESSA plans for different states went into effect at different time points during the 2017–2018 school year, based on when the U.S. Department of Education signed off on each state’s plan. We describe this timeline in detail and provide additional information on the law in Online Appendix A.1.

## 3. Literature Review

Our work draws from and contributes to two streams of IS literature. The first is online crowdfunding, and the second is signaling in online communities with a focus on crowdfunding.

## 3.1. Online Crowdfunding

This research examines crowdfunding success, a widely studied outcome in the IS literature, and contributes to the growing body of IS literature studying online crowdfunding (Burtch et al. 2014, Burtch and Chan 2019, Geva et al. 2019, Yang et al. 2020). Prior empirical research has examined several factors within the crowdfunding ecosystem that influence crowdfunding outcomes, such as the characteristics of crowdfunders (Lin and Viswanathan 2016, Younkin and Kuppuswamy 2018), reward structures and information controls (Burtch et al. 2015, Yang et al. 2020, Lin et al. 2022), risk disclosure (Kim et al. 2022), social networks and activities among advocates (Hong et al. 2018), historical information on antecedent contributors (Burtch et al. 2013, Kim and Viswanathan 2019, Jiang et al. 2022), algorithm choices and resource allocations (Song et al. 2022), and charity performance metrics (Kessler and Milkman 2018, Exley 2020).

A substream of this research that is contextually relevant to our work is the crowdfunding research focusing on the context of public education (Meer 2014, Wash and Solomon 2014, Weinmann and Mishra 2019, Gao et al. 2021, Xiao and Yue 2021, Keppler et al. 2022). An important finding that is theoretically relevant to our research is that the geographical proximity between lenders and borrowers has a positive influence on online crowdfunding outcomes, suggesting a home or familiarity bias<sup>6</sup> (Galak et al. 2011, Burtch et al. 2014, Lin and Viswanathan 2016). Geographical proximity can generate trust in transaction partners or opportunities in the same areas, even in the absence of any tangible economic benefits (Lai and Teo 2008).

This work makes two key contributions to this literature. First, although prior literature has documented a baseline level of home bias in all digital finance transactions, we identify a set of conditions that intensifies this bias and offer underlying reasons for this. Our study is among the first to highlight that home bias on online platforms is dynamic and that external signals can signif icantly influence donor preferences toward geographically proximal causes. Second, in a multidisciplinary literature review on crowdfunding, He et al. (2024) conducted a thematic synthesis, finding that the effects of the institutional environment (regulatory forces, etc.) on crowdfunding platforms are underexplored and that research thus far has predominantly examined the effects of within-platform signals on within-platform activities. Our work directly addresses this research gap in the crowdfunding literature by examining how external signals from the environment influence activities on crowdfunding platforms.

## 3.2. Signaling in Online Communities

A substantial body of IS literature has examined the effects of signaling on online platform user behavior. For instance, in the context of e-commerce, website informativeness (Pavlou et al. 2007) and website quality (Wells et al. 2011) can serve as quality signals for potential buyers. Signals also influence online behavior in the context of crowdsourcing platforms (Majchrzak and Malhotra 2016), social media (Nian and Sundararajan 2022), matching platforms (Shi and Viswanathan 2023), and online service marketplaces (Zheng et al. 2023).

In the area of crowdfunding, several studies in information systems and management have examined the role of signaling from the perspective of resource providers and resource seekers. Resource seekers often voluntarily provide personal information, which can serve as a signal that improves the likelihood of successful fundraising by helping to establish trust (Ahlers et al. 2015, Geva et al. 2019). Likewise, project pitches also contain signals, such as the readability of the text, the number of typos, and the quality of images and videos (Mollick 2014). Signals related to resource providers include word-of-mouth communications in blog posts (Qiu 2013), early investment by experts (Kim and Viswanathan 2019), and recommendations from friends and acquaintances, all of which can impact the probability of funding. Beyond the signals transmitted within the crowdfunding ecosystem, research has also documented the signaling effects of investors in the external environment such as venture capitalists (He et al. 2024).

This paper contributes to this literature in three ways. First, institutional signals have been documented to play a significant role in shaping individual behavior in the offline world (Tankard and Paluck 2016), but their effect has not been examined in the online world. Our work contributes to the IS literature by examining the effect of institutional signals on online donor behavior. Second, we also examine two mechanisms through which institutional signals are received, information push and information pull (Cybenko and Brewington 1998), showing that stronger external signals lead to stronger behavioral shifts in the online crowdfunding community. Finally, although existing studies focus on how signaling (e.g., from resource seekers) influences the perceived worthiness of a particular initiative relative to others, we examine how legislative signaling can impact the perceived worthiness of an entire class of initiatives (e.g., public education) altogether.

## 4. Theory and Hypotheses

Digital platforms operate within a larger context that includes social, cultural, economic, political, technological, and regulatory forces. In this larger context, formal institutions<sup>7</sup> (e.g., governments) frequently take measures aimed at the same societal problems targeted by informally organized online groups, such as donors on a crowdfunding platform, and transmit signals that play a pivotal role in shaping individuals’ beliefs about societal needs (Tankard and Paluck 2016) and their sense of personal responsibility in helping to meet those needs. We examine the effect of an institutional signal, namely a legislative signal, on the behavior of online donors and focus on two aspects: (1) the existence of the signal, that is, the mere presence of governmental action, which signifies commitment and attention and can have effects on donor perceptions and actions, and (2) the information content in the signal, that is, the devolutionary focus of the legislation.

A prerequisite for any change in individual giving behavior as a reaction to a legislation is awareness, because people will not change their donations when they are not aware of these changes. There are two possible mechanisms through which donors can receive legislative signals: information push and information pull (Cybenko and Brewington 1998). When an individual requests and receives a piece of information, say through an Internet search, this is information pull. If information is sent with out being directly solicited, such as through a newspaper, then the situation is characterized as information push. Two chief characteristics of efficacious signals have been theoretically postulated: signal observability and signal frequency (Janney and Folta 2003, 2006; Park and Mezias 2005). Although many laws are enacted, the degree to which ordinary citizens become aware about these changes in legislation depends on the efficacy of signals received through these mechanisms. We depict our conceptual framework in Figure 2.

## 4.1. Overall Crowding Out

Legislative signals can serve as vehicles of information that indicate governmental attention to a public cause. This attention carries meaning on its own, independent of the actual content of the legislation. We propose that legislative signals can reduce overall online giving, drawing reasoning from multiple streams of literature. The first stream of literature in philanthropy suggests that voluntary action emerges to satisfy the unmet demand for collective goods on the part of particular population segments. According to the substitutionbased view of volunteering (Dekker and Halman 2003, Prodi et al. 2023), donors conceptualize their voluntary action as a substitute for government action in supply ing collective goods. Thus, if a legislative signal indicates that the government is devoting resources to a collective good, donors are likely to discount the importance of their own contributions. If individuals perceive that legislative policies are already addressing their concerns, their intrinsic motivation to contribute is likely to decrease (Frey and Jegen 2001, Nyborg and Rege 2003). Indeed, an important factor that impacts a donor’s likeli hood to donate is the difference the donor believes thei contribution will make (Bekkers and Wiepking 2011). Therefore, legislative signal of governmental attention is likely to lead online donors to reduce or withhold their charitable contributions.

Figure 2. Conceptual Framework  
![](/api/attachments/WENUX7NK/fulltext/images/aa20f2419ced2a1918d57bed26b62e99d9ab603afcf1f09b369213765254e47e.jpg)

Along the same line, public goods theory also predicts that the size and scope of the nonprofit sector is larger when governments fail to meet the needs of heterogeneous societies (Weisbrod 1978). Voluntary contributions come from donors who see themselves as “gap-fillers” in response to private demands for collective goods not offered by the government (Salamon and Toepler 2015). When legislative signals indicate that the government is stepping in to address these needs, the perceived necessity for nonprofit intervention may diminish. In such cases, donors may feel that their role as gap-fillers is no longer necessary or relevant. As a result, their willingness to contribute financially decreases because the sense of responsibility is mitigated. This dynamic is likely to be particularly pronounced in online donation settings, where donors are already distanced from the cause. Thus, public goods theory suggests that governmental attention, signaled through legislation, can crowd out private charitable giving by reducing the demand for nonprofit action.

Third, economic crowding-out theories that follow a rational choice perspective have documented mixed evidence on the effects of financial governmental support. Warr (1983) and Roberts (1987) predict complete crowding out, although Andreoni (1990) predict fractional crowding out. We propose an overall crowding out effect even in contexts where explicit dollar-fordollar public-private tradeoffs cannot be established. We hypothesize that a major legislative signal can have a similar pull-back effect for an important reason. Many of the economic models assume full information on the part of the donors, that is, that donors are fully informed of the levels of government spending toward public causes. However, empirical data from studies in a wide range of contexts do not support the assumption of full information (Handy 2000, Horne et al. 2005, Shah et al. 2015, Lergetporer et al. 2016) and instead reveal that ordinary citizens are largely uninformed about governmental spending. Therefore, decisions of charitable giving may not be based on actual knowledge of government spending (de Wit and Bekkers 2016).

Facing complex information, citizens usually rely on coarse signals and simple information cues (Simon 1990, Kahneman and Tversky 2013). In the context of charitable giving, these signals often come from external sources, particularly when individuals do not actively seek out detailed information. We propose that information push, through channels like media coverage, plays a critical role in shaping public perception and donor behavior. When legislative signals are pushed through media outlets, the public becomes aware of governmental attention to specific causes, even if they were not previously looking for such information. This unsolicited information can form a narrative in the public mind that the government is taking sufficient action, thereby reducing the perceived need for their own donations. Therefore, we expect that a signal of governmental attention can evoke a similar withdrawal behavior from donors. Taken together, a legislative signal could lead to a reduction in donations due to donors discounting the importance of their own contributions to a collective public cause. We hypothesize the following.

Hypothesis 1. A legislative signal (governmental attention) pertaining to a public cause will lead to an overall decrease in online donations to the cause.

## 4.2. Local Crowding In

Although the existence of a signal, on its own, is likely to have an effect (I may not know exactly what the legislation is doing but I know the government is doing something), signaling theory posits that the informational content of a signal matters for how it influences decision making (Arrow 1973). As noted previously, donors can receive legislative signals through two mechanisms: information push and information pull (Cybenko and Brewington 1998). Between these, information pull, where donors actively seek out information, is likely to encourage potential donors to move from hesitation to active contribution.

With devolutionary legislation, the information-seeking behavior of donors points them toward the salient information content of the signal, which is greater delegation of control to state and local education authorities. Studies in IS literature on crowdfunding have noted the existence of home bias and noted the relevance of local interest, community, and distance as factors that influence online giving (Galak et al. 2011, Burtch et al. 2014, Lin and Viswanathan 2016). We posit that home bias on online platforms is dynamic and that external signals can significantly influence donor preferences toward geographically proximal causes. Specifically, we expect information pull by donors about a devolutionary legislative signal to intensify home bias in three ways.

First, the message of devolution is likely to draw public attention to the challenges faced by local schools. As donors become more aware of the plight of local schools, they are likely to view these causes as more pressing and tangible compared with broader, national issues. Second, donors are more likely to give when they feel that their individual actions make a difference (Bekkers and Wiepking 2011). The delegation of greater control to local donors would lead them to believe that their own actions, especially those aimed at local educational initiatives, will make a bigger difference. This belief stems from the idea that, with local schools gaining more autonomy, donations aimed at these institutions will translate into more immediate and effective outcomes. Third, familiarity effects, where donors are more inclined to support causes they know well (Jiang et al. 2019), are likely to be amplified by devolutionary legislative signals. As donors actively seek information, they become better informed about local schools and their specific needs, they feel more empowered to make decisions about contributing to local causes.

In summary, devolutionary legislative signaling (Shackleton et al. 2002) has the potential to motivate donors to respond more enthusiastically to requests from teachers in their state and local communities. This shift in donor behavior is driven by three key factors: heightened awareness of local needs, the perception that local contributions will have a greater impact, and the amplification of familiarity effects as donors gain more knowledge about local schools. Together, these factors work to intensify home bias, leading to a redistribution of donations toward local causes.

This effect would align with the complementarity theory (Dekker and Halman 2003, Dahlberg 2005) of voluntary action, according to which volunteers view their efforts as complementary to governmental action. As a result, donors are likely to perceive a diminished federal role and an increased and impactful local role in public education. In essence, we expect that the information content of a legislative signal with a devolutionary component will amplify familiarity bias and heighten the interest of donors in local causes.

Hypothesis 2. A legislative signal with a devolutionary focus (informational content) will lead to a redistribution of online donations toward local causes.

## 5. Data

We systematically assembled a multifaceted data set by gathering information from four independent data sources. In this section, we first introduce these data sources and then present the variables in the empirical model.

## 5.1. Data Sources

First, we obtained donation data from DonorsChoose. org via their application programming interface, which included details about classroom projects, teachers, schools, donors, and project donations. We obtained school demographic information from the NCES, which maintains the Department of Education’s primary database on public Pre-K to Grade 12 education in the United States. This information is available at the yearly level. To measure donor awareness, we utilized two supplementary data sources at the state level: (a) data on the relative volume of Internet search traffic for terms related to ESSA from Google Trends and (b) news and media releases about ESSA from Lexis Nexis (see Section 6.3 for details).

The school-quarter-level data set we compiled contained all active U.S. public Pre-K to Grade 12 schools present in both DonorsChoose and the NCES system. The final sample consisted of 73,303 unique schools, covering nearly 70% of all public Pre-K to Grade 12 schools in the United States. Our main analysis focused on 20 quarters from 2015 to 2019, ensuring that the ESSA ratifications in the majority of states (during the 2017–2018 school year) fell within the central part of our study period. We chose this period because (a) using quarters as the time unit allowed us to cover at least five quarters before and after ESSA ratification, and (b) comprehensive annual demographic information has been available in the NCES database since 2015. Our results are robust to alternative study periods and alternative units of analysis (details in Online Appendix E).

## 5.2. Variable Definitions

5.2.1. Dependent Variables. We used four crowdfunding performance measures as dependent variables in our analysis and measured crowdfunding success in two ways: We considered the Amount Raised, measured as the total dollar amount raised by the school in a given quarter (Younkin and Kuppuswamy 2018, Cornelius and Gokpinar 2020), and employed Proportion Funded as an alternative measure of crowdfunding performance to reflect the “all-or-nothing” funding mode of DonorsChoose, where a teacher receives donations only if the amount raised equals or exceeds the target funding goal. Given our focus on local and nonlocal giving, Local Amount captures the contribution amount raised from local donors sharing the same initial three zip code numbers as the focal schools, and Nonlocal Amount captures the contribution amount raised from donors outside this area. We adopted the three-digit zip code because (a) it is better suited than the fivedigit zip code with respect to alignment with school districts in a way that is appropriate for our study, and (b) the location of donors is restricted by the platform to the three-digit zip code level. In a robustness check, we also used a county-level operationalization and a continuous measure of the geographic distance between the focal school and its donors for triangulation (see Online Appendix E.11).

5.2.2. Independent and Control Variables. Our main independent variable of interest is ESSA, which we operationalized as a binary variable indicating the date on which it was announced that the respective state’s ESSA plan had been approved. This variable took the value of one for a school-quarter pair if the respective state’s ESSA plan was ratified during that quarter and retained the value of one in subsequent quarters. We also employed the federal announcement of ESSA as an alternative independent variable in a separate analysis (see Online Appendix E.2).

Based on recent empirical research identifying characteristics that could potentially be associated with a school’s crowdfunding performance (Meer 2014, Gao et al. 2021), we included a broad set of control variables. We summarized these variables, along with descriptive statistics in Table 1. Details of descriptions of the variables and a correlation matrix are presented in Online Appendix B.2.

## 6. Empirical Analysis and Results

In this section, we first introduce the model specification we used to estimate the effects of the state ESSA ratifications on the donations that schools received through the platform. We then present our empirical findings on the overall fundraising success, as well as local and nonlocal giving. Following that, we examine information push and pull as potential mechanisms through which donor behavior responds to legislative signaling (ESSA ratifications). In the post hoc analysis, we further investigate the impacts on equity by focusing on low-SES schools that have fewer resources to begin with. We conclude this section by offering a series of checks to demonstrate the robustness of our results to alternative explanations.

## 6.1. Empirical Strategy

As noted earlier, although the federal ESSA law was signed in December 2015, the individual ESSA plans for different states went into effect at different time points over the 2017–2018 school year based on when the U.S. Department of Education approved each state’s plan. This temporal and geographic variation provides us with a quasi-experimental setting, allowing us to examine the effect of the legislative signal (announcement of state ESSA ratification) on donor behavior and to rule out alternative explanations (Seamans and Zhu 2014). Specifically, we leveraged the date on which each state’s plan was ratified as an external shock to compare the crowdfunding activity of schools before and after the shock. We present model-free evidence for the shifts in funding following state ESSA ratification dates in Figure 3.

We leveraged the exogenous policy shock on schools in each state as a natural experiment and adopted a staggered difference-in-differences (DD) model using an ordinary least squares (OLS) estimation with fixed effects.<sup>8</sup> Our model specification for the DD analysis is as follows:

$$
\begin{array}{c} Y _ {i j t} = \beta \cdot E S S A _ {i j t} + \gamma \cdot X _ {i j t} + S c h o o l _ {i} + Q u a r t e r _ {j} \\ + Y e a r _ {t} + \epsilon_ {i j t}. \end{array}\tag{1}
$$

In the equation above, i denotes the school and jt denotes the time (quarter-year); $Y _ { i j t }$ denotes the dependent variables defined above, that is, Amount Raised, Proportion Funded, Local Amount, and Nonlocal Amount. We used the logs of the dependent variables measured in dollar amounts because these variables represent nonnegative continuous data. Our results are consistent when using the non-log dependent variables (Online Appendix E.14). $E S S A _ { i j t }$ is the treatment indicator variable, which equals one if the school state’s ESSA plan was approved by the U.S. Department of Education by the time jt; X represents a vector of time-variant control variables, such as the Amount Requested by the school in a given quarter, Prop. Basic Projects, and Minority.<sup>9</sup> The vectors, School , Quarter , and Year are school and time fixed effects that control for unobserved heterogeneity in school characteristics and temporal time trends. Note that rather than employing time (quarter-year) fixed effects, we chose to separately incorporate the quarter and year indicators (Wallis 1972, Ottonello and Winberry 2020). This multiway fixed effects approach allowed us to effectively account for annual shocks and seasonal variation, 10 although the use of quarter-year fixed effects adjusts for quarterly shocks only and cannot identify seasonal patterns or annual deviations (Statalist 2019). We clustered the standard errors at the state level to further control for potential correlations in error terms due to unobserved economic, demographic, and political characteristics at the state level.<sup>11</sup>

Table 1. Variables and Summary Statistics

<table><tr><td>Variable</td><td>Description</td><td>Mean</td><td>Standard deviation</td><td>No. of observations</td></tr><tr><td>Amount Raised</td><td>Total dollar amount raised through the platform</td><td>1,389.86</td><td>2,727.50</td><td>4,40,617</td></tr><tr><td>Prop. Funded</td><td>Proportion of fully funded projects</td><td>0.77</td><td>0.36</td><td>4,40,617</td></tr><tr><td>Local Amount</td><td>Dollar amount contributed by local donors</td><td>360.76</td><td>833.96</td><td>4,40,617</td></tr><tr><td>Non-Local Amount</td><td>Dollar amount contributed by nonlocal donors</td><td>1,029.10</td><td>2,341.66</td><td>4,40,617</td></tr><tr><td>ESSA</td><td>=1(0) if the respective state&#x27;s ESSA plan has (not) been ratified</td><td>0.40</td><td>0.49</td><td>4,40,617</td></tr><tr><td>Num. Projects</td><td>Number of projects posted on the platform</td><td>2.78</td><td>4.10</td><td>4,40,617</td></tr><tr><td>Amount Requested</td><td>Total requested dollar amount</td><td>1,875.12</td><td>3,396.84</td><td>4,40,617</td></tr><tr><td>Prop. Literacy Projects</td><td>Proportion of literacy-related projects</td><td>0.36</td><td>0.41</td><td>4,40,617</td></tr><tr><td>Prop. Basic Projects</td><td>Proportion of basic needs-related projects</td><td>0.33</td><td>0.41</td><td>4,40,617</td></tr><tr><td>Avg. Word Count</td><td>Average word count of project descriptions</td><td>52.97</td><td>6.35</td><td>4,40,617</td></tr><tr><td>Avg. Readability</td><td>Average Flesch Kincaid grade level of project descriptions</td><td>12.50</td><td>2.91</td><td>4,40,617</td></tr><tr><td>Avg. Sentiment</td><td>Average polarity sentiment score of project descriptions</td><td>0.50</td><td>0.27</td><td>4,40,617</td></tr><tr><td>Prop. Repeat Donors</td><td>Proportion of repeat donors</td><td>0.72</td><td>0.25</td><td>4,40,617</td></tr><tr><td>Prop. Teacher Donors</td><td>Proportion of donors who are teachers</td><td>0.17</td><td>0.20</td><td>4,40,617</td></tr><tr><td>Num. Donors</td><td>Number of unique donors</td><td>11.34</td><td>15.38</td><td>4,40,617</td></tr><tr><td>Prop. Giving Page</td><td>Proportion of donations through the giving page</td><td>0.40</td><td>0.31</td><td>4,40,617</td></tr><tr><td>Prop. Match Offers</td><td>Proportion of donations through match offers</td><td>0.06</td><td>0.12</td><td>4,40,617</td></tr><tr><td>Prop. Thank-Yous</td><td>Proportion of donations receiving thank you cards/gifts</td><td>0.09</td><td>0.16</td><td>4,40,617</td></tr><tr><td>Prop. Web GCs</td><td>Proportion of donations using online gift cards</td><td>0.16</td><td>0.22</td><td>4,40,617</td></tr><tr><td>Prop. Campaign Credits</td><td>Proportion of donations using campaign credits</td><td>0.07</td><td>0.15</td><td>4,40,617</td></tr><tr><td>Minority</td><td>Proportion of nonwhite students</td><td>0.58</td><td>0.32</td><td>4,40,617</td></tr><tr><td>Low Income</td><td>Proportion of students qualifying for NSLP</td><td>0.51</td><td>0.30</td><td>4,40,617</td></tr><tr><td>Num. FTEs</td><td>Number of full-time equivalent employees</td><td>38.45</td><td>25.56</td><td>4,40,617</td></tr><tr><td>Num. Students</td><td>Total number of students</td><td>648.44</td><td>460.05</td><td>4,40,617</td></tr><tr><td>Dist. Funding (log)</td><td>Total revenue of school district (log)</td><td>13.95</td><td>8.54</td><td>4,40,617</td></tr></table>

Figure 3. Signing Dates of States’ ESSA Plans and Funding Performance After These Dates  
![](/api/attachments/WENUX7NK/fulltext/images/1b2f76960d63f9962a0403f6f81c9d590a897431441299f15b3747ee6d26b084.jpg)  
Note. The figure presents the percentage of change in school crowdfunding performance after the ratification of the ESSA state plan (circle colors red � negative, green � positive), and the number of schools by state in our sample (circle sizes); most schools experienced a decrease in crowd funding performance after their state plans were signed.

To verify the validity of our empirical framework, we performed three sets of preliminary checks, with details described in Online Appendix C. First, following previous literature (Eftekhari et al. 2023, Dobrescu et al. 2024), we conducted placebo treatment simulations by generating random dates during the ratification period (January 1, 2017–June 20, 2019) and testing the effect of the random dates on crowdfunding outcomes. We found that the estimates from the placebo simulations are insignificant on average and across dependent variables, suggesting that there is no sufficient evidence to support an association between the random placebos and crowdfunding performance (details in Online Appendix C.1). Second, following Goodman-Bacon (2021), we performed event-study analyses and conducted a Goodman-Bacon decompo sition to check the validity of our staggered DD speci fication. The results of our event-study analysis show an absence of preshock trends in schools’ fundraising outcomes across all of the preshock periods (as indi cated by the nonblack bars in Figure 4); the results of our Goodman-Bacon decomposition show that the inverse weighting problem is not an issue (details in Online Appendix C.2). Third, we conducted a series of falsification tests to rule out demand-side shifts in the volume of teacher requests as a potential explanation for our findings (see Online Appendix C.3 for details). We did not expect the policy change to significantly affect demand-side trends because initiatives imple mented over a longer horizon are unlikely to alleviate teachers’ immediate need for classroom supplies. In line with our expectations, we applied the eventstudy analyses on teachers’ requests and found that schools’ fundraising requests stayed fairly stable over the periods before and after the state ESSA ratification (as indicated by the black bars in Figure 4). In sum, the results from these preliminary checks demonstrate the validity of our empirical specification.

![](/api/attachments/WENUX7NK/fulltext/images/a161b0c5a51b136b8e0f1619c0d92503673d6dcca6f73e14a76ebe6c61c039ab.jpg)  
Figure 5. (Color online) Model Free Evidence: Before-After Comparison in Dependent Variables  
Note. The figure shows the average values of the dependent variables for both the before and after periods, along with 95% confidence intervals

Figure 4. Shifts in Crowdfunding Demand and Supply Before and After State ESSA Ratifications  
![](/api/attachments/WENUX7NK/fulltext/images/73de85ce837786b901f1ab6ad0cbba2c035a23843fd99ce0da2e825daa300e6d.jpg)  
Notes. The outcomes of interest remain relatively stable in the time periods leading up to the state ESSA ratifications but shift afterward; in the contrast, the demand side, reflected by the Amount Requested, shows little variation both before and after each state’s ESSA ratification. ESSA-1 i omitted from the estimation (Freyaldenhoven et al. 2021). Estimation results are provided in Online Appendix C.2

## 6.2. Results

Figure 5 provides model-free evidence of shifts in private donations in response to the announcement of the major educational devolution policy. We observed a decrease in the overall funding success, reflected in the total amount raised and the proportion of funded projects following the state’s ESSA ratification. We also found that the local amount increased although the nonlocal amount decreased after the shock. Table 2 presents the key estimation results of Equation (1) for the effects of ESSA ratification on school crowdfunding outcomes.

6.2.1. Negative Overall Effect on Crowdfunding Success. Our analysis shows that a majority of schools experienced declines in crowdfunding success after their respective state plan approvals (as shown in Figure 3). The results from our empirical estimation are consistent with model-free observation. We estimate the impact of the state ESSA ratifications on the overall crowdfunding success of schools, reflected in the total amount raised (Amount Raised) and the proportion of fully funded projects (Proportion Funded), and report the results in columns (1) and (2) of Table 2. The negative and significant coefficients of the variable ESSA indicate that schools in states with ratified ESSA plans saw significantly inferior crowdfunding outcomes (corroborating Hypothesis 1). Specifically, following their state’s ESSA ratifications, schools saw a drop of 8% in the amount raised (amounting to a total of \$2.45 million for the sample schools in a quarter) and a 4% drop in the proportion of projects that met their funding goals compared with schools in states that had not yet ratified their ESSA plan. In summary, ESSA ratification at the state level was associated with a significant decline in the donations schools received.

6.2.2. Increase in Local Donations and Decrease in Nonlocal Donations. Columns (3) and (4) of Table 2 show results for our main model specification, where the dependent variables are the amounts raised from local donors and nonlocal donors, respectively. We computed Local Amount as the contribution amount raised from donors located in the same geographical area

Table 2. Effects of ESSA Ratifications on School Crowdfunding Performance

<table><tr><td rowspan="2"></td><td colspan="4">Dependent variable</td></tr><tr><td>Overall amount raised(1)</td><td>Prop. funded(2)</td><td>Local amount raised(3)</td><td>Nonlocal amount raised(4)</td></tr><tr><td>ESSA</td><td>-0.079**(0.039)</td><td>-0.040**(0.015)</td><td>0.120***(0.030)</td><td>-0.156**(0.060)</td></tr><tr><td>Num. Project (Log)</td><td>0.242***(0.012)</td><td>0.085***(0.004)</td><td>0.298***(0.015)</td><td>0.128***(0.013)</td></tr><tr><td>Amount Requested (Log)</td><td>0.420***(0.012)</td><td>-0.201***(0.004)</td><td>0.165***(0.015)</td><td>0.391***(0.016)</td></tr><tr><td>Prop. Basic Projects</td><td>-0.017***(0.005)</td><td>-0.004*(0.002)</td><td>-0.060***(0.010)</td><td>-0.003(0.007)</td></tr><tr><td>Prop. Literacy Projects</td><td>-0.036***(0.004)</td><td>-0.015***(0.002)</td><td>0.043***(0.009)</td><td>-0.070***(0.007)</td></tr><tr><td>Avg. Word Count (Log)</td><td>-0.014(0.009)</td><td>-0.007**(0.003)</td><td>0.021(0.018)</td><td>-0.026*(0.015)</td></tr><tr><td>Avg. Readability (Log)</td><td>0.043***(0.011)</td><td>0.015***(0.004)</td><td>-0.047**(0.020)</td><td>0.072***(0.016)</td></tr><tr><td>Avg. Sentiment</td><td>-0.030***(0.005)</td><td>-0.016***(0.002)</td><td>-0.012(0.015)</td><td>-0.028**(0.011)</td></tr><tr><td>Num. Donors (Log)</td><td>0.546***(0.015)</td><td>0.170***(0.006)</td><td>1.080***(0.016)</td><td>0.940***(0.016)</td></tr><tr><td>Prop. Repeat Donors</td><td>0.258***(0.013)</td><td>0.084***(0.006)</td><td>-0.260***(0.043)</td><td>0.562***(0.024)</td></tr><tr><td>Prop. Teacher Donors</td><td>-0.307***(0.030)</td><td>-0.068***(0.010)</td><td>0.946***(0.048)</td><td>-1.329***(0.053)</td></tr><tr><td>Prop. Giving Page</td><td>0.017(0.017)</td><td>0.025***(0.006)</td><td>0.181***(0.026)</td><td>-0.034(0.026)</td></tr><tr><td>Prop. Matched Offers</td><td>0.041*(0.022)</td><td>0.032***(0.009)</td><td>-0.448***(0.063)</td><td>0.486***(0.039)</td></tr><tr><td>Prop. Thank-Yous</td><td>1.211***(0.024)</td><td>0.574***(0.010)</td><td>0.615***(0.041)</td><td>0.959***(0.049)</td></tr><tr><td>Prop. Web GCs</td><td>0.394***(0.024)</td><td>0.165***(0.009)</td><td>0.084*(0.043)</td><td>0.527***(0.044)</td></tr><tr><td>Prop. Campaign Credits</td><td>-0.646***(0.020)</td><td>-0.271***(0.008)</td><td>0.174***(0.044)</td><td>-0.865***(0.039)</td></tr><tr><td>Num. FTEs (Log)</td><td>-0.008(0.008)</td><td>0.002(0.004)</td><td>0.053(0.032)</td><td>-0.036(0.025)</td></tr><tr><td>Num. Students (Log)</td><td>0.012(0.019)</td><td>0.009(0.008)</td><td>0.002(0.034)</td><td>0.010(0.023)</td></tr><tr><td>Minority</td><td>0.043(0.071)</td><td>-0.002(0.032)</td><td>-0.290*(0.148)</td><td>0.143(0.151)</td></tr><tr><td>Low-Income</td><td>-0.030(0.021)</td><td>-0.013(0.009)</td><td>0.057(0.065)</td><td>-0.080*(0.042)</td></tr><tr><td>District. Funding (Log)</td><td>-0.001(0.001)</td><td>-0.001(0.001)</td><td>0.005**(0.002)</td><td>-0.003***(0.001)</td></tr><tr><td>School, quarter, year (fixed effects)</td><td>√</td><td>√</td><td>√</td><td>√</td></tr><tr><td>No. of observations</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td></tr><tr><td> $R^2$ </td><td>0.752</td><td>0.458</td><td>0.592</td><td>0.630</td></tr></table>

\*\*\*p < 0:01; \*\*p < 0:05; \*p < 0:1.  
Notes. The maximum variance inflation factor among the independent variables is 5.987 (<10), indicating that multicollinearity is not likely to b an issue. Standard errors are presented in the parentheses.

(based on the first three digits of the zip codes) as the school and Nonlocal Amount as the contribution amount raised from donors outside of this area. Note that because the segment of the population considered local to a particular school is a smaller the segment of the population considered nonlocal, our ex ante expectation is that the magnitude of local donations would be considerably lower than the magnitude of nonlocal donations. We observed a positive coefficient of ESSA for Local Amount and a negative coefficient Nonlocal Amount; the estimated coefficients are both statistically and economically significant. In particular, following their state’s ESSA ratification, schools raised 11.9% more from local donors and 15.7% less from nonloca donors, equaling a quarterly increase of \$0.95 million in local donations and a decrease of \$3.4 million in nonlocal donations for the sample schools (see Online Appendix E.11 for robustness checks). In summary, our results show that ESSA ratifications redistributed online donations, leading to increased localization in crowdfunding (corroborating Hypothesis 2).

## 6.3. Mechanism Examination: Information Push and Information Pull

In this section, we test the assumption that citizens are generally aware of the legislative signal and examine information push and information pull, the two channels through which donors can become aware of ESSArelated news. To capture information push, we first collected news and media releases from LexisNexis. Then, we constructed a binary variable, Push, which captured whether a school’s donations primarily originated from states with intensive ESSA-related news coverage.<sup>12</sup> Specifically, we included ESSA-relevant articles published over the December 1, 2015–March 31, 2017, time period, which included the period before the state ESSA ratifications.<sup>13</sup> Our analysis (details in Online Appendix D.1) shows that the moderation effect of information push for local crowding-in became insignificant when the information pushed was unrelated to the salient ESSA theme of devolution, providing further evidence that the informational content of the legislative signal— devolution in our case—matters. To examine information pull, we captured the effect of citizens actively seeking information to educate themselves about ESSA. Specifically, we examined search engine activity on ESSA. As described in Section 5, we used Google Trends to track ESSA-related search traffic<sup>14</sup> and created a binary variable, Pull, which indicates whether a school’s donations primarily originate from states displaying higher than median interest in the search terms; Pull equals one if over half a school’s donors were from such states.

We then expanded the staggered DD model of our main analysis by including the interaction terms, ESSA × Push and ESSA × Pull, in the model. When we separately included the interaction terms (Table D2 in

Online Appendix D), we observed that both information push and information pull strengthened the effects on the amount raised by local and nonlocal donors, indicating that donors in states with more interest in ESSA responded to the ratification by making more local donations and fewer nonlocal donations. Interestingly, when jointly considering the effects of information pull and push, we observed distinct results for local and nonlocal donations (Table 3). The local amount raised after ESSA is significantly and positively moderated by information pull, while the reduction in nonlocal donations is magnified by information push. This contrast suggests that the increase in local donations induced by legislative signals is shaped mainly through information pull via active search, although the decrease in nonlocal donations is more likely to be driven by information pushed through news and media releases.

## 6.4. Post Hoc Analyses

6.4.1. Impacts on Low-SES and Title I Schools. As observed in Figure 1(a), a majority of crowdfunding projects are posted by teachers at high-poverty schools, which typically receive fewer instructional resources to begin with. It is important to understand whether the resource inequity problem in public education might be intensified by the shifts in donation patterns observed following state ratifications. We examined this possibility by focusing on schools with a higher concentration of low-SES students. In particular, we stratified schools based on (1) the percentage of low-income students (Low Income, measured by the percentage of students qualifying for free or reduced school lunch), (2) the percentage of minority students (Minority), and (3) whether a school is a Title I school.<sup>15</sup> The plots in Figure 6 indicate that funding success (proportion of projects funded) decreased to a larger extent for low-SES schools (i.e., Title I schools and those with a higher percentage of low-income or minority students) following the state ESSA ratifications.

Table 3. Mechanism Examination

<table><tr><td rowspan="2"></td><td colspan="3">Information push and pull</td></tr><tr><td>Amount raised(1)</td><td>Local amount(2)</td><td>Nonlocal amount(3)</td></tr><tr><td>ESSA</td><td>-0.060(0.038)</td><td>0.051*(0.028)</td><td>-0.106*(0.059)</td></tr><tr><td> $ESSA \times Push$ </td><td>-0.031***(0.009)</td><td>0.026(0.023)</td><td>-0.069***(0.016)</td></tr><tr><td> $ESSA \times Pull$ </td><td>-0.019(0.016)</td><td>0.111**(0.044)</td><td>-0.060*(0.033)</td></tr><tr><td>Controls</td><td>√</td><td>√</td><td>√</td></tr><tr><td>School, quarter, year (fixed effects)</td><td>√</td><td>√</td><td>√</td></tr><tr><td>No. of observations</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td></tr><tr><td> $R^2$ (full model)</td><td>0.756</td><td>0.596</td><td>0.632</td></tr></table>

Note. Standard errors are presented in the parentheses.  
\*\*\*p < 0:01; \*\*p < 0:05; \*p < 0:1.

Figure 6. Before-After Comparison: Average Proportion of Projects Funded  
![](/api/attachments/WENUX7NK/fulltext/images/fddd330b58384e89f44fc90f90addbc25e6a449c55cee37883471b5f301145b3.jpg)

![](/api/attachments/WENUX7NK/fulltext/images/1a32a26d8c0da2ad4a85c59fb358dc7fdf99a909aad4ccd34f58d3d5ac75e50c.jpg)

![](/api/attachments/WENUX7NK/fulltext/images/212c9119c42545e689ca19640d4b911dd57bfbc512daed98427fc8e03000430e.jpg)  
Notes. This figure presents a before-after comparison of crowdfunding success among schools with different SES levels. We separate school based on (1) the percentage of low-income students, (2) the percentage of minority students, and (3) Title I classification. We observe that funding success decreased to a larger extent for low-SES schools, represented with a darker shade, following state the ESSA ratification

To empirically examine the impact of states’ ratifications on low-SES schools, we included interaction terms, ESSA × Low-Income, ESSA × Minority, and ESSA × Title I, in the model relating ESSA ratification and school crowdfunding outcomes. Table 4 presents the results measuring the impact on low-SES students and Title I schools. The coefficients of the interaction terms involving the three variables, ESSA × Low-Income, ESSA × Minority, and ESSA × Title I, are all negative and significant at the 5% level. For instance, as shown in column (5) of Table 4, Title I schools have raised an even lower total amount: specifically, 2.1% (equaling a total of \$0.64 million in a quarter) less than their counterparts. Our results suggest that Title I schools and schools with a higher percentage of low-SES students were disproportionately impacted by the shift in donor behavior following the ESSA ratifications.

6.4.2. Impacts on Number of Donors vs. Per-Donor Amount. Our main results indicate a significant decline in total donations associated with state ESSA ratifications, either due to a reduced number of donors or due to decreased donation amounts per donor. Our examination (detailed in Online Appendix D.3) reveals that the number of overall and local donors remained stable, although the average amount contributed by donors both overall and locally was impacted. These findings imply that the legislative signal did not substantially change the pool of donors but significantly changed donation behavior. This is further verified by our donorlevel analysis (shown in Online Appendix E.12).

6.4.3. Evaluation of Alternative Explanations and Additional Robustness Checks. We performed a series of additional robustness checks to confirm that possible confounds or alternative explanations did not drive our main results. We summarize our analyses in Table 5 (see tables and additional details in Online Appendix E).

## 7. Discussion

Information Systems research often aims to inform pol icy implications, which requires deeper engagement with the institutional context in which these policies

Table 4. Impacts on Low-SES Schools

<table><tr><td rowspan="3"></td><td colspan="6">Low-SES indicator</td></tr><tr><td colspan="2">Low income</td><td colspan="2">Minority</td><td colspan="2">Title I</td></tr><tr><td>Amount raised (1)</td><td>Prop. funded (2)</td><td>Amount raised (3)</td><td>Prop. funded (4)</td><td>Amount raised (5)</td><td>Prop. funded (6)</td></tr><tr><td rowspan="2">ESSA</td><td>-0.052**</td><td>-0.021**</td><td>-0.049**</td><td>-0.022**</td><td>-0.063**</td><td>-0.029**</td></tr><tr><td>(0.017)</td><td>(0.009)</td><td>(0.017)</td><td>(0.009)</td><td>(0.027)</td><td>(0.013)</td></tr><tr><td rowspan="2">ESSA × Low-SES Indicator</td><td>-0.052***</td><td>-0.036***</td><td>-0.051***</td><td>-0.031***</td><td>-0.021***</td><td>-0.014***</td></tr><tr><td>(0.009)</td><td>(0.004)</td><td>(0.008)</td><td>(0.004)</td><td>(0.006)</td><td>(0.003)</td></tr><tr><td>Controls</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>School, quarter, year (fixed effects)</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td><td>✓</td></tr><tr><td>No. of observations</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td><td>4,40,617</td></tr><tr><td>R2 (full model)</td><td>0.756</td><td>0.458</td><td>0.756</td><td>0.458</td><td>0.529</td><td>0.458</td></tr></table>

Notes. The interaction term coefficients represents the interactions between ESSA and each of Low income (columns (1) and (2)), Minority (columns (3) and (4)), and Title I (columns (5) and (6)), respectively. Clustered standard errors are presented in the parentheses. \*\*\*p < 0:01; \*\*p < 0:05; \*p < 0:1.

Table 5. Alternative Explanations and Robustness Tests

<table><tr><td>Potential concern</td><td>Empirical examination</td><td>Appendix</td></tr><tr><td></td><td>Panel A: Ruling out alternative explanations</td><td></td></tr><tr><td>Signal effect on demand side</td><td>We conducted falsification tests and found no impact of ESSA awareness on project request changes due to information push and pull mechanisms.</td><td>E.1</td></tr><tr><td>Federal announcement of ESSA</td><td>We tested the effect of the federal ESSA announcement (Dec. 2015) within a short window (two quarters before and after) to show consistent results using either state plan sign-off dates or the federal passage date as the shock.</td><td>E.2</td></tr><tr><td>Ratification window effects</td><td>We created a donation-level data set and used a seven-day window around state ratification dates to isolate the effect of ESSA ratification on donation behavior, minimizing potential confounding factors such as platform interface changes.</td><td>E.3</td></tr><tr><td>Seasonality</td><td>We employed two analyses to account for academic year cycles: (1) comparing crowdfunding outcomes to the period&#x27;s average, and (2) treating the ESSA ratification year as the treatment and the prior year as the control to compare outcomes before and after the ratification quarter.</td><td>E.4</td></tr><tr><td>Donors&#x27; history</td><td>We categorized donors as first-time or repeat and analyzed donations accordingly. Both groups showed consistent ESSA ratification effects in significance and magnitude, indicating that our main findings are robust in terms of donor history.</td><td>E.5</td></tr><tr><td>Flash funding</td><td>We verified the robustness of our local redistribution results by excluding large donors and high-donation dates, confirming that &quot;flash funding&quot; did not skew our findings.</td><td>E.6</td></tr><tr><td>School district partnerships</td><td>We demonstrated that excluding the schools engaged in partnership with the platform (only 1% of our sample) from our analysis did not change our results</td><td>E.7</td></tr><tr><td>Political funding and activities</td><td>We confirmed that excluding schools engaged in partnerships with the platform (only 1% of our sample) from our analysis did not affect our results.</td><td>E.8</td></tr><tr><td>On-platform interface changes</td><td>We scrutinized the archival interfaces of DonorsChoose.org over 2015–2019 on a monthly basis and ruled out potential effects of interface changes on online giving behavior after ESSA.</td><td>E.9</td></tr><tr><td></td><td>Panel B: Additional robustness checks</td><td></td></tr><tr><td>Selection bias</td><td>We used matching models, including propensity score matching (PSM) and coarsened exact matching (CEM) at the project level, to create matched groups of projects from before and after the shock, addressing concerns about self-selection based on school characteristics.</td><td>E.10</td></tr><tr><td>Alternative definitions of local donations</td><td>We confirmed our results are robust to alternative operationalizations of donation localization by: (1) defining local donors at the county level, and (2) creating continuous measure of donor distance.</td><td>E.11</td></tr><tr><td>Donor-level analysis</td><td>We analyzed serial donors at the individual level and found consistent shifts in donation behavior.</td><td>E.12</td></tr><tr><td>Continuous measurement of signal awareness</td><td>We used continuous measures for information push and pull and found stronger effects at the donor level.</td><td>E.13</td></tr><tr><td>Non-log outcome measures</td><td>We confirmed the results using nonlog outcome variables, including the total amount raised, local amount, and nonlocal amount.</td><td>E.14</td></tr></table>

are shaped. This study finds that legislative signals have substantial effects on online donor behavior, corroborating our hypotheses that the ratification of a major devolution law such as ESSA leads to the greater localization of online donations. Our results show a 11.9% increase in donations contributed by local donors and a 15.7% drop in nonlocal donations following state ESSA ratifications. The net effect is an 8% drop in the average amount raised by schools through the platform, totaling an average of \$2.4 million per quarter. These effects were qualitatively similar whether we considered the federal announcement or state-level ratifications.

We also explored the mechanisms through which the effects manifested. Specifically, we observed that donors behavioral shifts aligned consistently with the extent of information pull (Internet search) and information push (media coverage). Interestingly, the increase in local donations was shaped mainly by information pull, although the decrease in nonlocal donations was driven primarily by information push. We also observed that schools with a greater percentage of low-SES students and fewer resources to begin with were more adversely affected by these shifts in donation tendencies. These results are robust to a variety of alternate specifications.

We acknowledge certain limitations in our analyses. First, this study focused specifically on the effect of the legislative signal rather than on the actual implementation of the act. Second, while our staggered difference-indifference model in combination with other analyses makes for a strong identification strategy overall, we acknowledge that this methodology is not immune to caveats in identifying causal effects (Cunningham 2021). Third, our donation data came from one leading online platform, DonorsChoose. However, our field data show that DonorsChoose contributions significantly dwarfed other public school crowdfunding platforms in terms of economic reach during our study period. Fourth, although the measures we employed (i.e., capturing Google Trends data and news media coverage) may be imperfect, they are useful proxies that helped us uncover important mechanisms. Finally, we acknowledge that donors may relocate and that local donations could be more precisely measured if donation data with real-time location information were available. Our first-time donor analysis (Online Appendix E.5) allowed us to alleviate this concern to some extent.

## 7.1. Theoretical Implications

Research over the last two decades in information systems and related disciplines has discussed and debated the flattening effect of digital platforms. Platforms make information accessible beyond geographical constraints and serve as agents of coordination (Gefen and Carmel 2008, Chen and Horton 2016). Although the flat world hypothesis (Freidman 2005) points to the role of digital technology and platforms in transcending traditional physical and geographical limitations, IS research has documented evidence of home bias and role of geography in digital finance transactions (Galak et al. 2011, Burtch et al. 2014, Lin and Viswanathan 2016).

Our research extends this conversation and makes the following contributions to IS crowdfunding literature. First, our study is among the first in the crowdfunding stream to hypothesize and demonstrate geographically asymmetric effects of external signals on fundraising outcomes, contributing to the field’s understanding of familiarity bias and home bias (Lin and Viswanathan 2016, Sabzehzar et al. 2023). Second, although policy scholars have examined the high-level impacts of significant federal policies, and IS scholars have examined factors that make bottom-up crowdfunding efforts more effective, our study is unique in that it focuses is on the interaction between these two forces (top-down policy and bottom-up crowdfunding efforts) by adding an antecedent to fundraising performance, top-down leg islative signaling, that has not been previously examined. We provide evidence of hyperlocalization in online crowdfunding following legislative decentralization, which intensifies the resource-divide issue in education and advances the understanding of resource allocation in the context of crowdfunding platforms (Song et al. 2022).

Next, we contribute to IS literature that examines the role of signaling on user behavior on online platforms (Pavlou et al. 2007, Wells et al. 2011, Majchrzak and Mal hotra 2016, Nian and Sundararajan 2022, Shi and Viswanathan 2023, Zheng et al. 2023). Although prior work has examined within-platform signals (e.g., within-platform policies and actions) and off-platform, postfundraising resource mobilization, our research examines the effect of the institutional environment on crowdfunding plat forms. Although literature documents institutional signals shaping behavior in the offline world (Tankard and Paluck 2016), their effect remains underexamined in the online world. Specifically, the signal we examine shapes donors’ perceived worthiness of the entire class of initiatives (e.g., public education) in ways that require greater understanding.

## 7.2. Managerial Implications

ESSA has some important characteristics (e.g., devolution, complexity) resembling factors observable in other domains. For instance, as devolutionary laws become more common in other public policy domains (e.g., healthcare, financial services, utilities, poverty, small business growth, entrepreneurship, etc.), our results can provide a starting point for predictions about online crowdfunding efforts in these domains. One key crowdfunding platform concern is interface design and its role in aligning user behavior with platform owners’ goals regarding resource allocation. During important policy actions, it becomes essential for platform designers to use guidance corrections to keep the community momentum going forward. Timed and deliberate nudges, such as targeted campaigns, reprioritized project placement, and email promotions, become increasingly important surrounding major pol icy announcements. For instance, instead of showing potential donors projects from their own areas, plat forms might consider explicitly exposing donors from wealthy areas to projects from schools in poorer areas to counteract the potential “rich-get-richer” problem. By improving their matching processes, platforms could mitigate inequities in public education resources. Public school administrators with firsthand knowledge of funding inequities can work with platforms to address resource gaps in their planning cycles. Similarly, school teachers might be wise to reprioritize projects if they are vulnerable to major policy events. Public school teachers using digital platforms such as DonorsChoose for fundraising might need to participate in conscious messaging, particularly when there are external changes and discussions around initiatives concerning public education. For example, teachers may need to remind donors that the effects of federal measures such as ESSA trickle down to the schools only gradually and that many day-to-day classroom needs still remain unmet.

The existence and growth of platforms such as DonorsChoose and GoFundMe highlight market failures in public education funding. When public policies have a devolution component, policymakers need to engage with platforms to help them serve as counterforces against inefficiencies that might accompany such policies.<sup>16</sup> Further, our findings highlight the tendency of online donors to focus on the needs of their immediate communities, which can exacerbate the rich-getricher and poor-get-poorer problems. Policymakers could seek to mitigate such problems by, for example, providing tax-based incentives for certain forms of philanthropy that promote the equitable distribution of resources. Nevertheless, given donors’ tendencies to prioritize local projects, it is clear that no matter how well-intentioned and helpful for meeting teachers immediate needs, philanthropic platforms such as DonorsChoose should not be viewed as a substitute for comprehensive policies that address the needs of low-SES students, families, and communities.

## Acknowledgments

All three authors contributed equally to this work.

## Endnotes

<sup>1</sup> Source: https://www.donorschoose.org/about/impact.html, last accessed August 2024.

<sup>2</sup> Source: https://www.help.senate.gov/imo/media/doc/ESSA: Largest devlolution of federal control to states.pdf.

<sup>3</sup> In Online Appendix E.2, we perform a robustness test using the federal announcement as the main event.

<sup>4</sup> Source: https://www.donorschoose.org/about/impact.html, last accessed April 2024.

<sup>5</sup> See https://www.govinfo.gov/content/pkg/BILLS-114s1177enr/ pdf/BILLS-114s1177enr.pdf, last accessed September 2023.

<sup>6</sup> Familiarity bias is broader than home bias; it includes the tendency to contribute to causes that are not only geographically proximal but also proximal along other dimensions (e.g., culturally, socially).

<sup>7</sup> Here we rely on the definition of formal institutions as “entities that organize, govern, or educate a group” (Tankard and Paluck 2016).

<sup>8</sup> Note that, although Proportion Funded represents proportion data that are suitable for a fractional Probit model estimation, we ran the DD analysis for Proportion Funded using the ordinary least squares (OLS) model to make the results more interpretable. We observed consistent findings when using the fractional Probit model.

<sup>9</sup> All the control variables were scaled by log-transformation except the proportion variables.

<sup>10</sup> We made this specification precisely based on the recognition of the inherent seasonality present in our school fundraising data and ensured that our results remained consistent with further controls for seasonality (see Online Appendix E.4).

<sup>11</sup> Our results remained consistent when we changed our state-level fixed effects to the three-digit zip code level.

<sup>12</sup> In the main analysis, the variable reflects the topic-relevant push. For details on its operationalization, refer to Online Appendix D.

<sup>13</sup> We also conducted an additional donor-level analysis using continuous measures of information push and information pull and observed stronger moderation effects at this granular level (see Online Appendix E.12).

<sup>14</sup> We searched for the terms “ESSA” and “Every Student Succeeds Act” and excluded irrelevant terms to make sure that the results were relevant to the policy. The search period was December 1, 2015, to March 31, 2017, time period, consistent with the information push mechanism.

<sup>15</sup> Title I is the largest federally funded educational program, providing supplemental funds to school districts to assist schools with the highest student concentrations of poverty to meet educational goals.

<sup>16</sup> See https://www.donorschoose.org/superintendents for a recent attempt in this direction by DonorsChoose, last accessed August 30, 2024.

## References

Ahlers GK, Cumming D, Gu¨ nther C, Schweizer D (2015) Signaling in equity crowdfunding. Entrepreneurship Theory Practice 39(4):955–980.

Andreoni J (1990) Impure altruism and donations to public goods: A theory of warm-glow giving. Econom. J. 100(401):464–477.

Arrow KJ (1973) Information and Economic Behavior, vol. 28 (Federation of Swedish Industries, Stockholm).

Augenblick JG, Myers JL, Anderson AB (1997) Equity and adequacy in school funding. Future Child 7(3):63–78.

Baker BD (2021) Educational Inequality and School Finance: Why Money Matters for America’s Students (Harvard Education Press, Cam bridge, MA).

Bekkers R, Wiepking P (2011) A literature review of empirical studies of philanthropy: Eight mechanisms that drive charitable giving. Nonprofit Voluntary Sector Quart. 40(5):924–973.

Buchanan JM (1950) Federalism and fiscal equity. Amer. Econom. Rev. 40(4):583–599.

Burtch G, Chan J (2019) Investigating the relationship between med ical crowdfunding and personal bankruptcy in the United States: Evidence of a digital divide. MIS Quart. 43(1):237–262

Burtch G, Ghose A, Wattal S (2013) An empirical examination of the antecedents and consequences of contribution patterns in crowd-funded markets. Inform. Systems Res. 24(3):499–519.

Burtch G, Ghose A, Wattal S (2014) Cultural differences and geography as determinants of online prosocial lending. MIS Quart. 38(3):773–794.

Burtch G. Ghose A, Wattal S (2015) The hidden cost of accommodating crowdfunder privacy preferences: A randomized field experiment. Management Sci. 61(5):949–962.

Chen DL, Horton JJ (2016) Research note: Are online labor markets spot markets for tasks? A field experiment on the behavioral response to wage cuts. Inform. Systems Res. 27(2):403–423.

Cornelius PB, Gokpinar B (2020) The role of customer investor involvement in crowdfunding success. Management Sci. 66(1): 452–472.

Cunningham S (2021) Causal Inference: The Mixtape (Yale University Press, New Haven, CT).

Cybenko G, Brewington B (1998) The foundations of information push and pull. Cybenko G, O’Leary DP, Rissanen J, eds. The Mathematics of Information Coding, Extraction and Distribution (Springer, New York), 9–30.

Dahlberg L (2005) Interaction between voluntary and statutory social service provision in Sweden: A matter of welfare pluralism, substitution or complementarity? Soc. Policy Admin. 39(7):740–763.

de Wit A, Bekkers R (2016) Government support and charitable donations: A meta-analysis of the crowding-out hypothesis. J. Public Administration Res. Theory 27(2):301–319.

Dekker P, Halman L (2003) The Values of Volunteering: Cross-Vultural Perspectives (Springer, New York).

Dobrescu L, Motta A, Shanker A (2024) The power of knowing a woman is in charge: Lessons from a randomized experiment. Management Sci. 70(12):8217–8244.

Eftekhari S, Yaraghi N, Gopal RD, Ramesh R (2023) Impact of health information exchange adoption on referral patterns. Management Sci. 69(3):1615–1638.

Egalite AJ, Fusarelli LD, Fusarelli BC (2017) Will decentralization affect educational inequity? The every student succeeds act. Ed. Admin. Quart. 53(5):757–781.

Exley CL (2020) Using charity performance metrics as an excuse not to give. Management Sci. 66(2):553–563.

Farrie D, Johnson M (2015) Newark Public Schools: Budget Impacts of Underfunding and Rapid Charter Growth (Education Law Center, Pittsburgh).

Freidman T (2005) The World Is Flat (Farrar, Straus and Giroux, New York).

Frey BS, Jegen R (2001) Motivation crowding theory. J. Econom. Sur veys 15(5):589–611.

Freyaldenhoven S, Hansen C, Pe´rez JP, Shapiro JM (2021) Visualization, identification, and estimation in the linear panel eventstudy design. Technical report, National Bureau of Economic Research, Cambridge, MA.

Galak J, Small D, Stephen AT (2011) Microfinance decision making: A field study of prosocial lending. J. Marketing Res. 48:S130–S137.

Gao Q, Lin M, Wu D (2021) Education crowdfunding and student per formance: An empirical study. Inform. Systems Res. 32(1):53–71.

Gefen D, Carmel E (2008) Is the world really flat? A look at offshoring at an online programming marketplace. MIS Quart. 32(2):367–384.

Geva H, Barzilay O, Oestreicher-Singer G (2019) A potato salad with a lemon twist: Using a supply-side shock to study the impact of opportunistic behavior on crowdfunding platforms. MIS Quart. 43(4):1227–1248.

Goodman-Bacon A (2021) Difference-in-differences with variation in treatment timing. J. Econometrics 225(2):254–277.

Handy F (2000) How we beg: The analysis of direct mail appeals. Nonprofit Voluntary Sector Quart. 29(3):439–454.

He VF, Tro¨binger M, Murray A (2024) The crowd beyond funders: An integrative review of and research agenda for crowdfunding. Annals 18(1):348–394.

Hess FM, Eden M (2021) The Every Student Succeeds Act (ESSA): What It Means for Schools, Systems, and States (Harvard Education Press, Cambridge, MA).

Hong Y, Hu Y, Burtch G (2018) Embeddedness, pro-sociality, and social influence: Evidence from online crowdfunding. MIS Quart. 42(4):1211–1224.

Horne CS, Johnson JL, Van Slyke DM (2005) Do charitable donors know enough–and care enough–about government subsidies to affect private giving to nonprofit organizations? Nonprofit Vol untary Sector Quart. 34(1):136–149.

Jacob B (2017) The changing federal role in school accountability. J. Policy Anal. Management 36(2):469–477.

Janney JJ, Folta TB (2003) Signaling through private equity placements and its impact on the valuation of biotechnology firms. J. Bus. Venturing 18(3):361–380.

Janney JJ, Folta TB (2006) Moderating effects of investor experience on the signaling value of private equity placements. J. Bus. Ven turing 21(1):27–44.

Jiang F, Qian Y, Yonker SE (2019) Hometown biased acquisitions. J. Financial Quant. Anal. 54(5):2017–2051.

Jiang Y, Ho YC, Yan X, Tan Y (2022) What’s in a “username”? The effect of perceived anonymity on herding in crowdfunding. Inform. Systems Res. 33(1):1–17.

Kahneman D, Tversky A (2013) Prospect theory: An analysis of decision under risk. MacLean LC, Ziemba WT, eds. Handbook of the Fundamentals of Financial Fecision Faking: Part I (World Scientific, Singapore), 99–127.

Keppler SM, Li J, Wu D (2022) Crowdfunding the front lines: An empirical study of teacher-driven school improvement. Management Sci. 68(12):8809–8828.

Kessler JB, Milkman KL (2018) Identity in charitable giving. Management Sci. 64(2):845–859

Kim K, Viswanathan S (2019) The “experts” in the crowd: The role of experienced investors in a crowdfunding market. MIS Quart. 43(2):347–372.

Kim K, Park J, Pan Y, Zhang K, Zhang X (2022) Risk disclosure in crowdfunding. Inform. Systems Res. 33(3):1023–1041.

Lai S, Teo M (2008) Home-biased analysts in emerging markets. J. Financial Quant. Anal. 43(3):685–716.

Lergetporer P, Schwerdt G, Werner K, Woessmann L (2016) Informa tion and preferences for public spending: Evidence from representative survey experiments. Working paper, CESifo (Center for Economic Studies and Ifo Institute), Munich, Germany.

Lin M, Viswanathan S (2016) Home bias in online investments: An empirical study of an online crowdfunding market. Management Sci.62(5):1393-1414

Lin YK, Rai A, Yang Y (2022) Information control for creator brand management in subscription-based crowdfunding. Inform. Systems Res. 33(3):846–866

Majchrzak A, Malhotra A (2016) Effect of knowledge-sharing trajectories on innovative outcomes in temporary online crowds. Inform. Systems Res. 27(4):685–703.

McGuinn P (2016) From no child left behind to the every student succeeds act: Federalism and the education legacy of the Obama administration. Publius 46(3):392–415.

Meer J (2014) Effects of the price of charitable giving: Evidence from an online crowdfunding platform. J. Econom. Behav. Organ. 103: 113–124.

Mollick E (2014) The dynamics of crowdfunding: An exploratory study. J. Bus. Venturing 29(1):1–16.

Nian T, Sundararajan A (2022) Social media marketing, quality signaling, and the goldilocks principle. Inform. Systems Res. 33(2): 540–556.

Nyborg K, Rege M (2003) Does public policy crowd out private contributions to public goods. Public Choice 115(3):397–418

Ottonello P, Winberry T (2020) Financial heterogeneity and the investment channel of monetary policy. Econometrica 88(6): 2473–2502.

Park NK, Mezias JM (2005) Before and after the technology sector crash: The effect of environmental munificence on stock market response to alliances of e-commerce firms. Strategic Management J. 26(11):987–1007.

Parvin AJ, Beruvides MG (2021) Macro patterns and trends of US con sumer technological innovation diffusion rates. Systems 9(1):16.

Pavlou PA, Liang H, Xue Y (2007) Understanding and mitigating uncertainty in online exchange relationships: A principal-agent perspective. MIS Quart. 31(1):105–136.

Prodi E, Ghinoi S, Rubini L, Silvestri F (2023) Do informal institutions matter for the economic resilience of European regions? A study of the post-2008 shock. Econom. Politics 40(1):189–223.

Qiu C (2013) Issues in crowdfunding: Theoretical and empirical investigation on Kickstarter. Working paper, University of Cambridge, Cambridge, UK.

Roberts RD (1987) Financing public goods. J. Political Econom. 95(2): 420–437.

Sabzehzar A, Burtch G, Hong Y, Raghu T (2023) Putting religious bias in context: How offline and online contexts shape religiou bias in online prosocial lending. MIS Quart. 47(1):33–62.

Salamon LM, Toepler S (2015) Government–nonprofit cooperation: Anomaly or necessity? Voluntas 26:2155–2177.

Seamans R, Zhu F (2014) Responses to entry in multi-sided markets: The impact of craigslist on local newspapers. Management Sci. 60(2):476–493.

Shackleton S, Campbell B, Wollenberg E, Edmunds D (2002) Devo lution and community-based natural resource management: Creating space for local people to participate and benefit. National Resource Perspectives 76(1):1–6.

Shah KK, Sussex J, Hernandez-Villafuerte K (2015) Government and charity funding of cancer research: Public preferences and choices. Health Res. Policy Systems 13:1–14.

Shi L, Viswanathan S (2023) Optional verification and signaling in online matching markets: Evidence from a randomized field experiment. Inform. Systems Res. 34(4):1603–1621.

Simon HA (1990) Bounded rationality. Eatwell J, Milgate M, Newman P, eds. Utility and Probability (The New Palgrave, Palgrave Macmillan, London), 15–18.

Song Y, Li Z, Sahoo N (2022) Matching returning donors to projects on philanthropic crowdfunding platforms. Management Sci. 68(1):355–375.

Statalist (2019) Forum post by Clyde Schechter. (April 18), https:// www.statalist.org/forums/forum/general-stata-discussion/ general/1440510-high-dimensional-fixed-effects-firm-quarter and-year-quarter.

Tankard ME, Paluck EL (2016) Norm perception as a vehicle for social change. Soc. Issues Policy Rev. 10(1):181–211.

Wagner C, Wheeler L (1969) Model, need, and cost effects in help ing behavior. J. Personality Soc. Psych. 12(2):111.

Walker T (2019) Teacher spending on school supplies: A state-by-state breakdown. Nea Today (August 26), http://neatoday.org/2019/ 08/26/teachers-spending-on-school-supplies

Wall Street Journal (2015) No child left behind’s successor. Wall Street Journal (November 29), https://www.wsj.com/articles no-child-left-behinds-successor-1448838727.

Wallis KF (1972) Testing for fourth order autocorrelation in quar terly regression equations. Econometrica 40(4):617–636.

Warr PG (1983) The private provision of a public good is independent of the distribution of income. Econom. Lett. 13(2–3): 207–211.

Wash R, Solomon J (2014) Coordinating donors on crowdfunding websites. Proc. 17th ACM Conf. Comput. Supported Cooperative Work Social Comput. (Association for Computing Machinery New York), 38–48.

Weinmann M, Mishra A (2019) The effect of social distance in donation-based crowdfunding. ICIS 2019 Proc. (Association for Information Systems, Atlanta), 15.

Weisbrod BA (1978) Public Interest Law (University of California Press, Berkeley, CA).

Wells JD, Parboteeah V, Valacich JS (2011) Online impulse buying: Understanding the interplay between consumer impulsivenes and website quality. J. Assoc. Inform. Systems 12(1):3.

Xiao S, Yue Q (2021) The role you play, the life you have: Donor retention in online charitable crowdfunding platform. Decision Support Systems 140:113427.

Yang L, Wang Z, Hahn J (2020) Scarcity strategy in crowdfunding: An empirical exploration of reward limits. Inform. Systems Res. 31(4):1107–1131.

Younkin P, Kuppuswamy V (2018) The colorblind crowd? Founder race and performance in crowdfunding. Management Sci. 64(7): 3269–3287.

Zhang K, Wang Q, Qiu L, Wang N (2024) Unveiling the cost of free: How an ad-sponsored model affects serialized digital content creation. Inform. Systems Res. 0(0).

Zheng J, Wang Y, Tan Y (2023) Platform refund insurance or being cast out: Quantifying the signaling effect of refund options in the online service marketplace. Inform. Systems Res. 34(3): 910–934.

Copyright of Information Systems Research is the property of INFORMS: Institute for Operations Research & the Management Sciences and its content may not be copied or emailed to multiple sites without the copyright holder's express written permission. Additionally, content may not be used with any artificial intelligence tools or machine learning technologies. However, users may print, download, or email articles for individual use.
