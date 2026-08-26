---
otero_id: 2704
otero_key: "SK7U3TEG"
title: "Unemployment and Digital Public Goods Contribution"
authors: "Michael Kummer; Olga Slivko; Xiaoquan (Michael) Zhang"
year: "2020"
journal: "Information Systems Research"
doi: "10.1287/isre.2019.0916"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [130.130.241.6] On: 12 August 2020, At: 02:54 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

![](/api/attachments/SK7U3TEG/fulltext/images/3afc9913dd0e3fd706c77c66f2f4cac915b0bb2d8c217231d9335a80a52562cb.jpg)

## Information Systems Research

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Unemployment and Digital Public Goods Contribution

Michael Kummer, Olga Slivko, Xiaoquan (Michael) Zhang

To cite this article:

Michael Kummer, Olga Slivko, Xiaoquan (Michael) Zhang (2020) Unemployment and Digital Public Goods Contribution. Information Systems Research

Published online in Articles in Advance 11 Aug 2020

https://doi.org/10.1287/isre.2019.0916

Full terms and conditions of use: https://pubsonline.informs.org/Publications/Librarians-Portal/PubsOnLine-Terms-and-Conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2020, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms

With 12,500 members from nearly 90 countries, INFORMS is the largest international association of operations research (O.R.) and analytics professionals and students. INFORMS provides unique networking and learning opportunities for individual professionals, and organizations of all types and sizes, to better understand and use O.R. and analytics tools and methods to transform strategic visions and achieve better outcomes.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Unemployment and Digital Public Goods Contribution

Michael Kummer,<sup>a,b,c</sup> Olga Slivko,<sup>c</sup> Xiaoquan (Michael) Zhang<sup>d</sup>

<sup>a</sup> University of East Anglia, Norwich, Norfolk NR4 7TJ, United Kingdom; <sup>b</sup> Georgia Institute of Technology, Atlanta, Georgia 30332; <sup>c</sup> ZEW–Leibniz Centre for European Economic Research, 68161 Mannheim, Germany; <sup>d</sup> Chinese University of Hong Kong, Shatin, NT, Hong Kong

Contact: m.kummer@uea.ac.uk, https://orcid.org/0000-0002-9664-5895 (MK); olga.slivko@zew.de,

https://orcid.org/0000-0001-6062-2870 (OS); zhang@cuhk.edu.hk, https://orcid.org/0000-0003-0690-2331 (X(M)Z)

Received: Revised: Accepted: Published Online in Articles in Advance: August 11, 2020

https://doi.org/10.1287/isre.2019.0916

Copyright:

Abstract. Economic crises often result in massive job loss. However, although reduced employment has been shown to have many negative consequences for the affected individuals, it may also push them into new activities, such as provision of service to their communities. In this paper, we show how individuals engage in socially useful activities after an increase in unemployment. Specifically we document increased online content generation at Wikipedia, the world’s largest user generated knowledge repository. Leveraging German district-level and European country-level unemployment data we analyze the relationship between the economic crisis in 2008–2010 and contributions to Wikipedia. For both data sets we find increased socially valuable activity in the form of knowledge acquisition and contributions to Wikipedia. For German districts, we observe an increased rate of content generation on Wikipedia in districts that faced greater increases in unemployment. The effect of unemployment on content generation is even stronger at the European country level. Our findings suggest that public goods provision increases as a positive side effect of economic crises.

History: Paul Pavlou, Senior Editor; Gordon Burtch, Associate Editor. Funding: The research is partially supported by the Research Grants Council of the Hong Kong Special Administrative Region, China [Grants T31-604/18-N, GRF 14503818, GRF 16504614, GRF 644511, GRF 694213, and GRF 11504815]. Financial support from SEEK Project 2014 “Side Effects of Economic Crises in Europe and Provision of Online Public Goods” is gratefully acknowledged. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2019.0916

Keywords: online platform • public goods • unemployment • user-generated content • Wikipedia

## 1. Introduction

Economic crises, such as the one that followed the bankruptcy of Lehman Brothers in 2008, have often had very negative effects on the economy, such as severely reduced income and massive layoffs. The impact of such economic crises is likely to be negative on organizations and communities that rely on donations and volunteers. But how do individuals change their charitable behavior when they are confronted with increased levels of unemployment? Specifically, how do individuals adjust their volunteering time during economic downturns?

Prior studies summarized in List (2011) examined the relationship between economic crises and monetary donations. The literature generally found that during economic downturns, money donations did not decrease as significantly as the economy, but they increased substantially after an economic upturn. As a result, during the past half century, money donations outpaced the growth of Standard & Poor’s 500 Index. Although such evidence is available for monetary donations, less is known for contributions of personal time and effort, volunteering, a second important form of giving to a charitable cause.

This paper examines the relationship between economic crises and volunteering time. This issue is highly important for organizations and platforms that coordinate volunteers to promote charitable causes. Such organizations need to form adequate expectations regarding future contributions of volunteering time to efficiently plan the scale and scope of their activities.

Understanding the relationship between economic crises and volunteering also matters from a societal perspective. First, many volunteering organizations provide valuable public goods that range from disaster relief to publicly accessible knowledge, which matter to the wider economy. Second, individual working hours have been decreasing for decades in many societies, and several recent innovations and economic developments suggest that the trend toward ever-decreasing needs for human labor could continue. This reduced demand for labor could free up resources that could become an input for the provision of the greater public good. Our paper sheds light on this potential mechanism.

To study the relationship of interest, we analyze how economic crises and unemployment affect one particular type of volunteering: contributions to online public goods. Similar to traditional forms of charitable giving, economic crises severely limit resources for online public goods provision. However, whereas unemployment statistics and charitable money donations are easily captured and measured, statistics on volunteering time for the provision of public goods are often hard to obtain. To tackle this challenge, we study contributions to Wikipedia, one of the world’s largest digital public goods. We collect a comprehensive data set on the economic crisis and empirically examine the impact of unemployment on Wikipedia contributions. We find that economic downturns are associated with increased contributions to the online public good Wikipedia.

We identify the effect of interest by examining the changes in the pattern of digital public goods provision during the period of significant social and economic crisis in Europe that followed the economic crisis in 2008–2010. Because this crisis was largely unexpected, it works as a natural experiment: participants in the economy took various actions to react to increased unemployment, and we use a difference-in-differences (DID) framework to tease out the resulting effects.

Charitable contributions, which include both money and volunteering time, are a significant part of the economy. Money donations in the United States now exceed about 2% of the gross domestic product, or \$314 billion in real 2008 dollars (List 2011). The Corporation for National and Community Service estimates that 63 million Americans (about 25% of the population) volunteered a total of 8 billion hours of service in 2016.<sup>1</sup> These estimates do not include contributions to online public goods and therefore severely underestimate the time and value of overall volunteering.

In this paper we aim at filling this gap and at estimating the extent of online volunteering. Although offline volunteering usually requires substantial physical activity and time, and might even require some initial training, these frictions are minimized in the digital sphere. Much smaller contributions can be made any time of the day, and even the tiniest contributions can instantly make a visible difference. Moreover, it is easy to give online volunteering a try, perhaps even anonymously, and to turn away again if the activity turns out to be less rewarding than expected.

Wikipedia is a perfect setting for studying online volunteering. As the fifth-most-visited website, Wikipedia receives numerous views, and volunteers from all over the world contribute their time and knowledge. Wikipedia is nonexcludable and nonrival and can thus be regarded as a digital public good (Hess and Ostrom

2003, Xu and Zhang 2014). It is both collaboratively produced and universally accessible to anyone with internet access, and it was highly active both before, during, and after the economic crisis. Moreover, the wiki software records every edit in the article history, which is the key ingredient for analyzing the relationship between economic pressure from unemployment and volunteering behavior.

Similar patterns likely apply to other digital content platforms such as Github, Stack Overflow, or Android mobile applications. Moreover, in the coming years, the rapid development of artificial intelligence (AI) will call for a rise of online volunteering platforms, such as Zooniverse, in which crowds participate in the creation of data sets subsequently used for training AI algorithms for research in many areas. Therefore, the potential value of the outcome of online volunteering and its societal impact is expected to grow drastically in the coming years.

The effect of an economic crisis on online volunteering is not straightforward ex ante. On the one hand, the observed shift in time allocation toward more computer use and increased civic engagement might lead to the increased provision of public goods— and thus more contributions to Wikipedia. Previous contributors might be able to allocate more time after they are displaced from their jobs and contribute their time to the public information good. Others who were not aware of Wikipedia might begin searching for information on the internet and discover Wikipedia. Consequently, they might become interested in volunteering. Even individuals who still have jobs might do more online search for useful information and end up contributing to Wikipedia. On the other hand, the crisis may lead to reduced contributions to Wikipedia, because contributing time to public goods is clearly not an obvious reaction when people’s jobs are threatened Employed and unemployed individuals may feel threatened by social decline and might find it difficult to contribute to Wikipedia during a period of largescale unemployment, as the opportunity cost of their time is higher. Our contribution is to shed light on these questions by empirically analyzing how unemployment affects online volunteering time and, specifically, contributions to Wikipedia.

We find that unemployment in German districts leads to higher participation by volunteers and increased content generation on Wikipedia. Both the number of participating editors and the number of highly active users increase. The number of edits to Wikipedia articles increases, and we also found (slightly weaker) evidence for increased growth of overall content. We replicate this study with a European Union country-level data set. The results for European countries are consistent with those at the district level in Germany. We find even stronger effects on content generation because of the higher variation in unemployment in Europe during the crisis.

Several of our findings are in line with a mechanism by which the crisis motivated a share of the population from regions with higher unemployment to begin editing and, over time, influenced existing participating editors to also increase their activity. Because Wikipedia functions as an important knowledge base for the economy, our results document a new and somewhat valuable side effect of the economic crisis that has been previously overlooked by policy makers.

The rest of this paper is structured as follows. Section 2 reviews the literature. Section 3 describes the data set, and Section 4 discusses the empirical approach. Sections 5 and 6 report results on contributions to Wikipedia from German districts and European countries, respectively. Section 7 discusses the findings and limitations of our study, with suggestions for further research, and Section 8 concludes.

## 2. Related Research

Our paper contributes to two major streams of the literature.

## 2.1. Motives to Contribute to Public Goods

Our paper adds to the literature about intrinsic and extrinsic motives for contributing to public goods by highlighting unemployment as an additional motivation to contribute. Existing theoretical and empirical studies analyzed private incentives for voluntary public goods provision from the perspective of the interplay between free-riding incentives and social effects (e.g., Andreoni 2007).<sup>2</sup> Other research on public goods contribution established the link between wealth/ income to donations to the public good. Such works commonly assume that only successful people contribute to public goods and that transfers from the rich to the poor are organized through this mechanism (cf. List 2011 for a recent systematization and overview).

A relatively recent literature on public goods provision established that other forces, such as social pressure, guilt, or sympathy, may motivate users to contribute to public goods (Andreoni 1988, 1989, 1990, 2007; Wang and Zhang 2009; Zhang and Wang 2012; Wang et al. 2018; Sun et al. 2019). This finding receives empirical support in the context of online public goods, such as open-source software and online peer productive communities (Kandel and Lazear 1992, Comino et al. 2007, Algan et al. 2013). Comino et al. (2007) found that the size of the community of developers in open-source projects increased the chances of progress, but this effect decreased as the community became large. Zhang and Zhu (2011) showed the importance of the recipient group size for individual incentives for knowledge provision.<sup>3</sup> Chen et al. (2010) proposed social comparison as the motivating mechanism for contributions of movie ratings to the online community MovieLens.

2.2. The Effects of Unemployment on Volunteering The second related strand of literature tackles the effect of unemployment on individual activities and on volunteering.

Previous research suggested that unemployment might lead to a decrease in volunteering in general. For civic public goods, unemployment has been shown to be negatively correlated with both religious and secular volunteering (Freeman 1997, Uslaner 2002), but they could not observe within variation over time in their data.<sup>4</sup> Lim and Laurence (2015) further distinguished between formal volunteering and informal helping behavior. Both declined during the recession of 2008–2009 in the United Kingdom, but their individual-level analysis suggests that unemployed individuals in particular are more likely to contribute to both formal and informal volunteering activities. Looking at aggregate effects, we also observe a general decrease in content contributions for Germany during the recession. However, unemployment moderated this common negative trend, and we show that in regions more severely hit by unemployment, the decrease in contributions is lower as a result of the influx of new contributors who did not belong to the community (anonymous contributors) at the time.

Another line in the literature discussed how the unemployed reallocate their time, considering a wide range of potential uses of time (Aguiar and Hurst 2007; Knabe et al. 2010; Aguiar et al. 2012, 2013; Krueger and Mueller 2012). Although unemployed people were found to have more time to spend on leisure, they are less satisfied with life and specific activities (Knabe et al. 2010).<sup>5</sup> Although only 2% of the foregone market hours were allocated to civic and religious engagement (Aguiar et al. 2013), the studies suggested that most of the additional online leisure time was spent on social networks, online games, email, and portals, and young people spent more time online (Wallsten 2013).<sup>6</sup>

Because “online” and “offline” volunteering share many features, it is plausible that many of our findings apply to offline volunteering. However, even though “online volunteering” is an integral part of general volunteering, these two types of volunteering are not exactly the same. A key difference between online and offline volunteering is the flexibility in terms of the minimum necessary time spent on contributions and effort required to contribute. Although contributing to an online public good certainly has a lower hurdle, we also note that increased contributions may be a by-product of increased consumption of online information as a result of recession, so that volunteering becomes a side effect of self-interested online activities. In that sense, our results suggest that the negative impact of economic crises on charitable activities from the previous literature (Freeman 1997, Uslaner 2002) might not carry over to information goods. Therefore, provided that unemployment increases time spent online, we could expect even a stronger effect on volunteering online compared with volunteering offline.

In our analysis, different from the previous literature, we focus on observational data from online contributions to the largest online encyclopedia, Wikipedia. We exploit variation in unemployment from the recent economic crisis in Europe in the aftermath of the financial crisis in 2008. This crisis generated an exogenous shock to the time spent online because people who were laid off during the economic crisis had to reduce their working hours. Our data, hence, provide an extraordinary opportunity to shed light on the relationship between economic pressure from unemployment and volunteering behavior as an instance of public goods provision by less successful economic agents.

Unemployment might drive prosocial behavior if people feel threatened by unemployment and thus contribute in order to learn or maintain their skills as well as increase their self-esteem. This would be consistent with the research about prosocial behavior, which has documented a positive impact of regular volunteering on subjective well-being and happiness (Liang et al. 2001, Post 2005, Borgonovi 2008, Dunn et al. 2008, Cattan et al. 2011, Aknin et al. 2013, Binder and Freytag 2013).

We record increased online volunteering during a period of high unemployment on observational data that combine contributions of content to Wikipedia with data from a shock to unemployment. Moreover, other factors such as prestige, respect, or guilt are relatively less important in this setting, because the volunteers’ livelihood and well-being are jeopardized. The recorded increase in contributions to Wikipedia during the economic crisis highlights a novel channel through which private motivations foster contributions to an online public good. Note that a similar mechanism could prevail on other digital content platforms such as GitHub, Stack Overflow, or Android mobile applications.

Summarizing our contributions, our study (1) uses a novel data set of German and European Wikipedia contributions to study the effect of unemployment, (2) contributes to the literature on public goods by highlighting a new channel that fosters content contributions to an important digital public good, and (3) identifies a socially valuable activity that results from higher unemployment.

## 3. Data

Our main analysis of the relationship between unemployment and contributions of content is based on

German data that we collected at the district (NUTS 3) level. Despite the fact that the German economy held up relatively well during the economic crisis, different districts were affected differently by the rise in unemployment as well as by the Kurzarbeit (temporarily reduced working hours) program. In our analysis, we combine economic indicators of unemployment and reduced working hours at the district level with data on online activity and contributions to the German Wikipedia in the districts. Note that we ensure that the uncovered patterns are not specific to Germany. We do this by running the analogous analysis using data from the European country level in Section 6.

## 3.1. Unemployment and Reduced Working Hours in Germany in 2009–2010

In January 2009, the German government announced the need to combat the crisis. The German unemployment rate started rising early in 2009; in addition, many companies applied the extended Kurzarbeit program.<sup>7</sup> As a result, the government proposed to address the crisis by massively expanding the existing Kurzarbeit program. According to the rules of the program, employers experiencing a negative demand shock could activate reduced working hours for their employees. They would keep paying employees according to their hours worked, and the government would pay the workers about 60% of the foregone income. In January 2009, this program was extended from 6–12 to 18 and later 24 months, and its scope was broadened to cover a much larger number of industries (Walz et al. 2012).<sup>8</sup> Overall, the seasonally adjusted unemployment rate rose by 1%, and 300,000 people participated in Kurzarbeit. We thus define January 2009 as the onset of the great economic crisis and the moment when the crisis becomes significant for the German economy.

We obtained monthly data on the number of unemployed, unemployment rates, and participants in the Kurzarbeit programs at the district level and generated a district-level data set. Across all 16 German federa states, we observe 402 districts (Kreise) shown in Online Appendix Figure A.1. Our main estimation data are based on the 402 German Kreise, which are similar to midsize U.S. counties.<sup>9</sup> Appendix Table A.1 summarizes the monthly panel data at the Kreise level. We observe 402 Kreise in the six months before and after the shock. The average unemployment rate is 7.5%, and unemployment increased on average by 1%. The smallest change in unemployment was a decrease by 1.1%, and the maximum increase was 3.4%. In the same table we also show our variables that allow us to analyze content generation on Wikipedia.<sup>10</sup>

Whether the districts are affected or unaffected by the economic crisis is defined based on changes in their unemployment rate after the crisis. To have sufficient variation between affected and unaffected districts, we rank the districts in terms of the change of unemployment rate and define the top 30% as affected by the crisis. The 30% of districts with the lowest, sometimes even negative, changes are defined as unaffected and used as the control group for our estimation. Note that the magnitude of the treatment was considerable, because unemployment increased by approximately 1.1% more on average in the affected districts.<sup>11</sup>

Figure 1. Unemployment and Reduced Working Hours in Germany in 2008–2010  
![](/api/attachments/SK7U3TEG/fulltext/images/4f26846e32dda7eb05534182b5beb2288dbe7ea22fa324d84ff42db8666e3a9b.jpg)  
Source. Bundesagentur für Arbeit.

Application to the Kurzarbeit program in Germany  
![](/api/attachments/SK7U3TEG/fulltext/images/df4e20c62ef05c5eac0a192991bf4e5e328c951ccf7b60809df45cf208026b60.jpg)  
Note. Combined, the trends show that the rise in unemployment between 2009 and 2010 in Germany corresponded to a massive application of the Kurzarbeit program in the same period.

Table A.2 in Online Appendix A shows a comparison of the two groups before the crisis began. This comparison highlights the big difference in the changes in unemployment rate. Departing from initially similar unemployment rates, the affected group experienced an average increase of 1.86% in the unemployment rate, and the unaffected group experienced an average increase of approximately 0.33% only. Although similar on most parameters, the affected districts have a generally smaller population and slightly lower income per capita. The difference in the number of inhabitants is also reflected in the number of aggregate edits. Even though per-capita differences are much smaller, these differences stress the importance

Table 1. Unemployment Indicators in 16 German States

<table><tr><td rowspan="3">District name</td><td>Workers</td><td colspan="3">Unemployment rate</td><td>Districts</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td></tr><tr><td>No. of unemployed (1000s)</td><td>All workers (%)</td><td>Youth (age ≤ 25) (%)</td><td>Change (%)</td><td>Share affected</td></tr><tr><td>Baden-Wuerttemberg</td><td>254.1</td><td>4.69</td><td>4.13</td><td>1.15</td><td>0.62</td></tr><tr><td>Bavaria</td><td>291.2</td><td>4.46</td><td>4.08</td><td>1.18</td><td>0.73</td></tr><tr><td>Berlin</td><td>232.6</td><td>13.80</td><td>15.36</td><td>1.03</td><td>0.00</td></tr><tr><td>Brandenburg</td><td>169.6</td><td>13.21</td><td>13.27</td><td>0.87</td><td>0.55</td></tr><tr><td>Bremen</td><td>37.1</td><td>13.23</td><td>11.83</td><td>0.61</td><td>0.50</td></tr><tr><td>Hamburg</td><td>75.2</td><td>8.33</td><td>7.72</td><td>0.79</td><td>0.00</td></tr><tr><td>Hessen</td><td>209.2</td><td>6.71</td><td>6.78</td><td>0.78</td><td>0.18</td></tr><tr><td>Lower Saxony</td><td>304.3</td><td>7.85</td><td>7.91</td><td>0.68</td><td>0.11</td></tr><tr><td>Mecklenburg-Western Pomerania</td><td>120.1</td><td>13.74</td><td>12.41</td><td>1.05</td><td>0.83</td></tr><tr><td>North Rhine-Westphalia</td><td>774.7</td><td>8.47</td><td>8.11</td><td>0.90</td><td>0.26</td></tr><tr><td>Rhineland-Palatinate</td><td>120.4</td><td>6.18</td><td>6.71</td><td>1.01</td><td>0.42</td></tr><tr><td>Saarland</td><td>37.5</td><td>6.62</td><td>6.47</td><td>1.01</td><td>0.00</td></tr><tr><td>Saxony</td><td>277.2</td><td>12.80</td><td>12.59</td><td>1.61</td><td>0.82</td></tr><tr><td>Saxony-Anhalt</td><td>169.7</td><td>13.72</td><td>13.32</td><td>1.40</td><td>0.80</td></tr><tr><td>Schleswig-Holstein</td><td>108.4</td><td>8.10</td><td>8.62</td><td>0.72</td><td>0.10</td></tr><tr><td>Thuringia</td><td>135.3</td><td>11.35</td><td>10.53</td><td>1.76</td><td>0.76</td></tr></table>

Note. This table shows mean values of unemployment indicators, the number of unemployed and the rates, and the difference in the unemployment rate before and after the shock and the share of districts affected by the shock for each German state.

Table 2. Difference-in-Differences Regressions for German Districts

<table><tr><td rowspan="3"></td><td colspan="3">Anonymous content</td><td colspan="3">Registered content</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>log(Added (KB))</td><td>log(Deleted (KB))</td><td>log(# Edits)</td><td>log(Added (KB))</td><td>log(Deleted (KB))</td><td>log(# Edits)</td></tr><tr><td>Treated Districts After T</td><td>0.110**(0.054)</td><td>-0.145(0.113)</td><td>0.060**(0.027)</td><td>-0.012(0.197)</td><td>-0.036(0.187)</td><td>-0.041(0.101)</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>District FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td></tr><tr><td>Number of districts</td><td>240</td><td>240</td><td>240</td><td>240</td><td>240</td><td>240</td></tr><tr><td> $R^2$ </td><td>0.06</td><td>0.16</td><td>0.44</td><td>0.00</td><td>0.01</td><td>0.00</td></tr></table>

Notes. The table shows the results of our main difference-in-difference analysis that contrasts affected and unaffected German districts around the onset of the European financial crisis in January 2009. The columns contain different measures of contribution activity to Wikipedia: (1) the total length of anonymously added content (in kilobytes), (2) the total length of anonymously deleted content (in kilobytes), (3) the number of edits (revisions) by anonymous editors, (4) the total length of content added by registered users (in kilobytes), (5) the total length of conten deleted by registered users (in kilobytes), and (6) the number of edits (revisions) by registered editors. The variable of interest, which captures the treatment effect, Treated districts after T, is an interaction term between dummies for the districts that are affected by the crisis with the time dummy indicating the period after the crisis. Observations range from six months before to six months after the onset of the crisis. Al specifications include time period (month-year) dummies and district fixed effects. Standard errors, clustered by districts, are in parentheses FE, fixed effects.

$$
^ {* * *} p <   0. 0 1; ^ {* *} p <   0. 0 5; ^ {*} p <   0. 1.
$$

of using a difference-in-differences strategy and of analyzing the similarity of the trends in district-level editing activities before the crisis.

In Table 1 we aggregate the unemployment rates at the state level to show how unemployment varied across the 16 states. The table also shows the shares of affected districts per German state. Our definition of crisis based on change in the unemployment rate implicitly controls for the baseline of economic status of the states. As a result, the highest shares of affected districts can be observed in traditionally economically strong industrial German states, such as Bavaria or Baden-Wuerttemberg. Weaker states such as Thuringia also had a large share of affected districts.

## 3.2. Contributions to Wikipedia

We focus on three different measures of contributions to Wikipedia: (1) additions of content, (2) deletions of content, and (3) editing activity. To quantify additions and deletions, we measure the bytes that were added or deleted to the platform each month. It is useful to quantify additions and deletions separately to shed light on the nature of the effort that individuals exert. To quantify editing activity, we counted the number of edits. Moreover, when constructing our three measures of content generation, we were able to distinguish contributions from anonymous and registered users and calculated the content generation of both groups separately. In what follows, we describe how we matched anonymous contributions to districts via the recorded IP addresses and how we used registered contributors that reveal their location to match them to their corresponding districts.

3.2.1. Anonymous Contributions to German Wikipedia at the District Level. Using a large data set that contains the revision history of all articles of German Wikipedia, we aggregate individual monthly contributions and compute total contributions by districts. For this aggregation, we map the IP addresses associated with edits to the corresponding German districts. 12

In terms of overall editing activities on German Wikipedia, anonymous edits represent about 16% of all edits during our period of analysis (2008–2010). Although we do not suppose that anonymous edits are representative for all editing activities, we deem it highly relevant for our research question, because anonymous edits are typically made by occasional or unexperienced editors. Thus, our measures of anonymous contributions to Wikipedia at the district level account either for contributions by newcomers or for occasional and relatively small contributions in terms of the content generated.

3.2.2. Registered Contributions at the German District Level. In addition to anonymous editing activities, we collect information on the location of registered Wikipedia contributors, whenever they reveal it publicly on their user talk/profile page. We thus match almost 25% of the registered edits by users who edited Wikipedia under their username to a district of origin. Given that these registered edits were made by editors with a well-developed user talk/profile page, we consider them representative of edits by very active Wikipedia users, thus covering the other side of the spectrum.

The middle panel of Table A.1 shows both anon ymous and registered monthly edits from a district to

German Wikipedia, together with the number of registered users and the number of reverted edits. Because registered users are very active, they generate a much larger amount of content than anonymous users do. We also show the total number of edits that we could match to each district via one of the two approaches. Together, we could thus associate about 35% of the activities on the German-language Wikipedia to a district of origin. By analyzing a significant part, but not all, of the edits by German contributors, we introduce an additional identification assumption to our analysis. Specifically, we assume that registered Wikipedia editors who did not add a regional identifier to their profile adjust their editing behavior in similar ways as editors who did add such an identifier. Even though we deem this assumption plausible, we cannot directly test it because we cannot match users without identifiers to any regions.

In our German district-level analysis, we do not examine the contributions made by German users to Wikipedia versions of other languages such as Austrian, Swiss, and English. This data limitation is an issue only if users in affected German districts change their cross-country contribution behavior in a systematically different way than unaffected users, which we believe is unlikely. Even if there is a systematic difference, our country-level analysis would address this issue.<sup>13</sup>

We verify that the large uncovered share of edits does not distort our results in a robustness check (see Online Appendix Section B.9). Specifically, we analyze district-specific content by matching the edits of all users who edit in categories that can be associated with local interests in a district. Moreover, we conduct analysis at the country level that also includes all contributions by registered users, and the results are even stronger. We report these results in Section 6.

## 3.3. Descriptive Evidence

Figure 2 clarifies our empirical approach using data on the German Kreise. The left panel shows anonymous edits from the districts, whereas the right panel shows anonymous edits about these districts over time. We show the district-specific anonymous editing behavior six months before and after the onset of the crisis (highlighted by the thin red line at t 0). The two figures in the upper row show the median values of the normalized number of edits, and the lower row shows the absolute difference between affected and unaffected districts.

Contributions from and about affected districts (i.e., the treatment group) increased relative to those from and about unaffected districts (i.e., the control group). A comparison of the normalized trends reveals that both anonymous contributions (from districts) and registered contributions (about districts) experienced a relative increase in the districts that were more strongly affected by the crisis.

## 4. Empirical Approach

We analyze the relationship between the economic crisis and voluntary contributions of online knowledge to Wikipedia in the DID framework. The shock to unemployment is used as a source of exogenous variation in “disposable time” in the German economic system, and we compare content generation in German districts where the crisis was felt more strongly to the other, less affected, districts. In Section 6, we adopt this approach to compare severely affected European countries with countries that experienced only a moderate increase in unemployment. Compared with the country-level analysis, the analysis of German districts in this section allows us to focus on a framework with many units of observations (al most 400) in a homogeneous institutional context. The advantage of country-level analysis lies in the considerably larger variation in European unemployment rates.

Our difference-in-differences approach uses data from German administrative districts. The first difference compares content generation on Wikipedia before and after the shock, and the second difference compares content generation in German districts affected by the rise in unemployment to content generation in relatively unaffected districts. Our out comes of interest are the number of edits and the size of contributions in bytes by anonymous and registered users. This identification strategy allows us to measure the impact of the economic crisis on contributions to Wikipedia over a given time interval while controlling for all other possible sources of influence. The central assumption we need to make in the DID framework is that the changes in the readership and contribution activities are indeed due to the crisis rather than to some unobservable factors that correlate with the timing of the crisis. Moreover, treated and untreated districts have to share their pretrend dynamics, which we consider plausible, given the descriptive evidence.

The unit of observation in our data is a district in Germany with all corresponding statistics (e.g., unemployment rates) and aggregated contributions to Wikipedia observed every month before and after the official beginning of the economic crisis in Germany, which was announced in January 2009. The estimated equation is as follows:

$$
\begin{array}{c} C o n t r i b u t i o n s _ {i t} = \alpha_ {i} + \beta (A f t e r T _ {t} \times T r e a t e d _ {i}) \\ + X _ {i t} \gamma + \nu_ {t} + \epsilon_ {i t}, \end{array}\tag{1}
$$

where AfterT and Treated are dummy variables; Treated separates districts that were affected by the

Figure 2. (Color online) Development of the Main Outcomes for Content at the District Level  
![](/api/attachments/SK7U3TEG/fulltext/images/2c3eeb153b448e127af66c07398ab7d82867f31236b1c5be8a81406cc373b294.jpg)  
Difference between Treated and Control from Districts

Edits about Districts  
![](/api/attachments/SK7U3TEG/fulltext/images/e3138ea1d0e065dff3c069ddfebc432c46ad113cf17246964568fa408c575b36.jpg)

![](/api/attachments/SK7U3TEG/fulltext/images/cc7fe08e8e33616ac088b4b6bf791191632826818dd9bb94395769938432e9d5.jpg)

Difference between Treated and Control about Districts  
![](/api/attachments/SK7U3TEG/fulltext/images/9c8ec7208ea6783028846eb06fc6b910727b9300365521513029c43c43c68791.jpg)  
Notes. The figure shows the median values of the normalized number of edits from users in the district (left) and median values of the normalized number of edits to the district’s “local interest” content (right). The upper panel graphs show the median of the normalized number of edits for th affected and unaffected districts separately. The figure is based on monthly data six months before and after the crisis. The lower panel graphs show the absolute difference in the number of edits by the two user groups.

economic crises from those unaffected, and AfterT equals 1 if the time period is after the shock t . As the variable Treated does not vary over time, it drops out in the fixed effects specification. Similarly, in the analysis for German regions, the crisis moment is determined by switching from December 2008 to January 2009; therefore, the effect of $A f t e r T _ { t }$ is captured by one of the time dummies, $\nu _ { t } .$ . The coefficient of interest is the coefficient for the interaction term between these two dummies, $\beta ,$ which measures the DID after the shock to unemployment. In all regressions, as before, we include month dummies as well as district fixed effects of German districts to rule out district-specific unobserved heterogeneity and common time trends. Like before, the vector $\gamma$ is a vector of parameters, to allow including additional (time-varying) control variables in $X _ { i t } \ \left( \mathrm { i . e . } \right.$ ., district characteristics).

The contribution of district i in month t is measured in several ways. As explained in Section 3.2, we distinguished contributions from anonymous or registered users, and we computed (1) added bytes, (2) deleted bytes, and (3) the number of edits for both groups.

## 5. Results for German Districts

In this subsection we present the results for all content generated by users within German districts. The subsequent section (Section 6) repeats the analogous analysis at the country level. Overall total contributions to German-language Wikipedia fall after the crisis, but our findings suggest that in districts with higher unemployment, the negative overall trend is slower.

In the next subsection we present the results for content about districts. The results of this section focus on content contributed to Wikipedia, added or deleted, that has not been reverted. In Wikipedia, a revert means that the content contributed recently by a user can be removed if the user fails to satisfy the guidelines (e.g., vandalism, editing wars). The analysis of the content reverts is included in the online appendix (Section B.2) and is briefly discussed below. It provides us an insight into how valuable the added content is or whether the deletion of the content was appropriate. For example, an increase in reverts after the crisis could indicate that a substantial share of content added as a result of the crisis is nonvaluable and represents vandalism, or that an inflow of new users to the platform triggered editing wars in the community.

## 5.1. Difference-in-Differences Analysis

Our main results on the relationship between the unemployment rate and contributions to Wikipedia are presented in Table 2. These results are based on a DID specification for German districts. The observed outcomes include content generated anonymously (columns (1)–(3)) and by registered users (columns (4)–(6)). For both groups of users, we differentiate between the amount of content (in kilobytes), added (columns (1) and (4)) and deleted (columns (2) and (5)), as well as the editing activity, measured by the number of edits (columns (3) and (6)). All dependent variables are transformed into logarithms, and we control for monthly dummies to capture the country-wide temporal dynamics. The coefficient of interest, which measures the treatment effect, is the cross-term Treated districts after T. It is the interaction term between dummies for districts that are affected by the crisis, with the time dummy indicating the period after the crisis.

The results for a 12-month interval (6 months before and 6 months after the shock) suggest several interesting patterns. In affected districts that experienced an increase in unemployment, we can see an increase in anonymous content contributions but not in contributions by registered users, who are actual members of the community. Our DID estimates suggest that this effect is about 6% in edits and 10% in kilobytes. Interestingly, the contributions of valuable content that remained on article pages are driven by content addition, not by deletion.14

Alternative specifications and the robustness of our results are summarized below and shown in Appendix B (from Table B.1 onwards).

The results suggest an increase in participation of anonymous members of Wikipedia; moreover, the main sources of this increase are not only anonymous but also likely new members of the community. Inevitably, this provoked an increase in content contributions that do not satisfy the guidelines, as well as potential vandalism or editing wars. Tables B.2 and B.3 (in the online appendix) present the effect of the shock to unemployment on the number of vandal edits and on the share of malicious content contributions in total content contributions, respectively. As we can see, the number of vandal edits in the affected districts slightly increases in absolute numbers (Table B.2). However, the share of malicious content is not affected (Table B.3), suggesting that a slight increase in malicious activity by anonymous users during the crisis did not bring significant quality deterioration in relative terms.

The picture becomes slightly more nuanced after we decompose the treatment effect after the shock into effects by months after treatment (see Table 3). In this table, the positive effect on the number of anonymous edits is strongest over the first four months after the shock. As for the size, in the month of the shock the amount of contributed kilobytes rises by about 9% and in the second month by almost 10%. The effect on anonymous edits fades in the fifth month after the shock. Content additions, as opposed to content deletions, show a positive dynamic in the districts affected by the unemployment rise, and the effect on edits gets stronger as the effect of the crisis strengthens.

Overall, we find that total contributions to the German Wikipedia fall after the crisis, but additiona activity by new users mitigates the negative overal trend in districts with increased unemployment.

As mentioned in Section 3, in our DID regressions we compare the top 30% of districts that are affected strongly by the unemployment shock with the bottom 30% to ensure the districts in treatment and control groups are sufficiently different. The choice of the cutoff point is determined by the trade-off between the need to compare groups of districts with substantially different change in unemployment and, at the same time, the need to use as many observations as possible. We perform an analysis of how this choice may affect the results of our study and show in Table B.4 (in Online Appendix B) that our results are robust to the choice of the cutoff point as soon as the districts that are just in the median of distribution are eliminated. As a dependent variable, we choose our main result from column (3) in Table 2. This result is replicated in column (5) of Table B.4, and column (4) shows that we could still eliminate fewer districts in the middle, using in the regression the top 40% with the highest increase in unemployment and the bottom 40% with the lowest increase in unemployment, and the effects of interest would remain. As expected, columns (6) and (7) show that we could also further eliminate the districts in the middle of distribution and get even stronger effects.

Table 3. Difference-in-Differences Regressions for German Districts

<table><tr><td rowspan="3"></td><td colspan="3">Anonymous content</td><td colspan="3">Registered content</td></tr><tr><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>log(Added (KB))</td><td>log(Deleted (KB))</td><td>log(# Edits)</td><td>log(Added (KB))</td><td>log(Deleted (KB))</td><td>log(# Edits)</td></tr><tr><td>Treated in Month -3</td><td>0.025(0.100)</td><td>0.153(0.196)</td><td>0.054(0.037)</td><td>-0.429*(0.255)</td><td>-0.190(0.209)</td><td>-0.124(0.103)</td></tr><tr><td>Treated in Month -2</td><td>-0.041(0.102)</td><td>0.128(0.203)</td><td>0.048(0.035)</td><td>-0.093(0.263)</td><td>0.133(0.220)</td><td>-0.021(0.113)</td></tr><tr><td>Treated in Month -1</td><td>-0.064(0.102)</td><td>0.433**(0.182)</td><td>0.049(0.040)</td><td>-0.029(0.269)</td><td>0.195(0.238)</td><td>0.021(0.118)</td></tr><tr><td>Treated in Month 0</td><td>0.070(0.102)</td><td>0.100(0.190)</td><td>0.091**(0.038)</td><td>-0.168(0.333)</td><td>0.029(0.282)</td><td>-0.031(0.145)</td></tr><tr><td>Treated in Month 1</td><td>0.072(0.098)</td><td>-0.195(0.201)</td><td>0.096**(0.038)</td><td>-0.369(0.297)</td><td>-0.228(0.256)</td><td>-0.107(0.140)</td></tr><tr><td>Treated in Month 2</td><td>0.258**(0.105)</td><td>0.111(0.212)</td><td>0.104***(0.038)</td><td>-0.285(0.314)</td><td>-0.051(0.290)</td><td>-0.127(0.149)</td></tr><tr><td>Treated in Month 3</td><td>0.084(0.115)</td><td>-0.025(0.271)</td><td>0.100*(0.052)</td><td>-0.049(0.293)</td><td>-0.076(0.274)</td><td>-0.069(0.139)</td></tr><tr><td>Treated in Month 4</td><td>0.131(0.107)</td><td>-0.063(0.240)</td><td>0.128**(0.050)</td><td>-0.044(0.301)</td><td>0.044(0.296)</td><td>-0.024(0.145)</td></tr><tr><td>Treated in Month 5</td><td>-0.007(0.109)</td><td>0.102(0.250)</td><td>0.029(0.050)</td><td>-0.011(0.295)</td><td>0.199(0.271)</td><td>0.013(0.138)</td></tr><tr><td>Treated in Month 6</td><td>0.010(0.105)</td><td>-0.266(0.228)</td><td>0.052(0.053)</td><td>0.052(0.315)</td><td>0.074(0.285)</td><td>-0.101(0.150)</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>District FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td><td>3,120</td></tr><tr><td>Number of districts</td><td>240</td><td>240</td><td>240</td><td>240</td><td>240</td><td>240</td></tr><tr><td> $R^2$ </td><td>0.10</td><td>0.17</td><td>0.44</td><td>0.01</td><td>0.01</td><td>0.01</td></tr></table>

Notes. The table shows the per-period results of our main difference-in-difference analysis that contrasts affected and unaffected Germa districts around the onset of the European financial crisis in 2009. The columns contain different measures of contribution activity to Wikipedia (1) the total length of anonymously added content (in kilobytes), (2) the total length of anonymously deleted content (in kilobytes), (3) the numbe of edits (revisions) by anonymous editors, (4) the total length of content added by registered users (in kilobytes), (5) the total length of content deleted by registered users (in kilobytes), and (6) the number of edits (revisions) by registered editors. The variables of interest that decompose the treatment effect are Treated in Month 1 to Treated in Month 6. These variables are interactions between a dummy for districts that are affected by the crisis with time dummies that correspond to the respective period after the crisis. All specifications include time period (month-year dummies and district fixed effects. The time range studied is six months before and after the crisis start. Standard errors, clustered by districts are in parentheses. FE, fixed effects.

$$
^ {* * *} p <   0. 0 1; ^ {* *} p <   0. 0 5; ^ {*} p <   0. 1.
$$

## 5.2. Robustness Check: Alternative Estimation Strategies

Our first set of robustness checks investigates how sensitive our results are to our estimation strategy. We first use a linear fixed effects panel regression framework. Table B.1 in Online Appendix B shows the results for regressing several measures of content generation on the unemployment rate and district fixed effects.<sup>15</sup> As before, we present the results for the anonymously added and deleted amount of content (in kilobytes) and the number of edits by anonymous users (columns (1)–(3)), as well as the same measures for content contributed by registered users (columns (4)–(6)).

The results suggest that an increase in the regional unemployment rate is strongly related to the variation in anonymous contributions to Wikipedia. A 1% increase in unemployment rate is associated with a 3% increase in anonymous edits. Moreover, it is related to content deletion, though the significance of the coefficient is marginal. Based on the average editing activity on German Wikipedia in 2009 and 2010, that corresponds to almost 4,340 additional edits and 55 megabytes over the six-month period after the shock we observe. Because of limitations in the availability of control variables, which are collected for German districts on a yearly basis, Table B.1 does not include any control variables. Tables B.5 and B.6 (in the online appendix B.4) demonstrates that the inclusion of the available control variables does not affect the results.

In addition to the ordinary least squares (OLS) regressions, we verified robustness to using the fuzzy DID approach (De Chaisemartin and D’Haultfoeuille 2017). These results are shown in Table B.7 in Online Appendix B.

Table 4. Country-Level Difference-in-Differences Regressions for the Period of 12 Months Before and 12 Months After the Crisis

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td></tr><tr><td>ln(Views)</td><td>ln(Active Editors (5–100 edits))</td><td>ln(Very Active Editors (&gt; 100 edits))</td><td>ln(Avg. Edits per Article)</td><td>ln (New Words)</td><td>ln(# Wikilinks)</td><td>ln(# External Links)</td></tr><tr><td>After treatment</td><td>0.163***(0.030)</td><td>-0.003(0.032)</td><td>-0.009(0.038)</td><td>0.095***(0.014)</td><td>0.039(0.047)</td><td>0.249***(0.015)</td><td>0.309***(0.027)</td></tr><tr><td>Treated countries after T</td><td>0.146**(0.068)</td><td>0.142***(0.044)</td><td>0.127***(0.042)</td><td>0.056**(0.025)</td><td>0.133**(0.058)</td><td>0.057(0.037)</td><td>0.141**(0.053)</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Country FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>432</td><td>480</td><td>480</td><td>480</td><td>480</td><td>480</td><td>480</td></tr><tr><td>Number of countries</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td> $R^2$ </td><td>0.39</td><td>0.20</td><td>0.29</td><td>0.87</td><td>0.11</td><td>0.93</td><td>0.92</td></tr></table>

Notes. The table shows the effect of increased unemployment on contributions to the corresponding country’s Wikipedia in Europe for the following indicators: (1) views of Wikipedia, (2) the number of active Wikipedians (with at least 5 edits), (3) the number of very activ Wikipedians (with more than 100 edits), (4) the average number of edits per article, (5) the new words added, (6) hyperlinks to Wikipedia articles, and (7) hyperlinks to external sources. All measures of contributions to Wikipedia are in logs, and the month of the estimated crisis onset wa: omitted from the regressions. The variable of interest, which represents the treatment effect, Treated countries after T, is an interaction term between dummies for the countries that are affected by the crisis with the time dummy indicating the period after the crisis. All specification include time (month-year) dummies and country fixed effects (FE). Standard errors, clustered by countries, are in parentheses ∗∗∗p < 0.01; ∗∗p < 0.05; ∗p < 0.1.

## 5.3. Robustness Check: Controlling for District-Speci<sup>fi</sup>c Pretreatment Trends

We now perform a check in which we control for any district-specific patterns in the contributions to Wikipedia before the crisis. Such district-specific patterns, if systemic, could interfere with the assumptions of our natural experiment setting. To implement this check, we compute each district’s individual pretreatment trend for each dependent variable before the shock. We then extrapolate each district’s pretreatment trend to the period after the shock and include this new variable in the regression equations. We show the corresponding results in Table B.8. By construction, it should be significant and control for any trends in the dependent variables that would have been there in the absence of treatment. Despite the inclusion of the pretreatment trends in the dependent variable in our regressions, the results on our main dependent variables of interest remain unchanged when districtspecific pretreatment trends in the contributions to Wikipedia are controlled for.

## 5.4. Robustness Check: Source of Change in Contributions

Additionally, we investigate the channels behind the changes in contributions in affected districts. First, we

Table 5. Country-Level Content Contributions: Fixed Effects Regressions for the Effect of Views During the Period of 12 Months Before and 12 Months After the Crisis

<table><tr><td rowspan="2"></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td></tr><tr><td>ln(Active Editors (5–100 edits))</td><td>ln(Very Active Editors (&gt; 100 edits))</td><td>ln(Avg. Edits per Article)</td><td>ln(New Words)</td><td>ln(# Wikilinks)</td><td>ln(# External Links)</td></tr><tr><td>log(Views)</td><td>0.306***(0.103)</td><td>0.184**(0.086)</td><td>0.020(0.026)</td><td>0.203***(0.058)</td><td>0.150***(0.049)</td><td>0.158***(0.050)</td></tr><tr><td>Time FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Country FE</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Observations</td><td>432</td><td>432</td><td>432</td><td>432</td><td>432</td><td>432</td></tr><tr><td>Number of countries</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td><td>20</td></tr><tr><td> $R^2$ </td><td>0.25</td><td>0.22</td><td>0.85</td><td>0.11</td><td>0.94</td><td>0.92</td></tr></table>

Notes. The table shows the relationship between a country’s Wikipedia views and different measures of content contribution to Wikipedia Shown are the fixed effects regressions for the effect of views during the period of 12 months before and 12 months after the crisis. The independent variable of interest is log(Views), In each column we show a different measure of contribution activity: (1) the number of active Wikipedians (with at least 5 edits), (2) the number of very active Wikipedians (with more than 100 edits), (3) the average number of edits per article, (4) the new words added, (5) hyperlinks to Wikipedia articles, and (6) links to external sources. All indicators of contributions to Wikipedia are in logs. All specifications include time (month-year) dummies and country fixed effects (FE) and exclude the period of treatment Standard errors, clustered by countries, are in parentheses.

$$
^ {* * *} p <   0. 0 1; ^ {* *} p <   0. 0 5; ^ {*} p <   0. 1.
$$

explore the time stamps of edits in our sample. On the basis of the time of contribution, we aggregate edits made during working hours, from Monday to Friday, from 8 a.m. to 6 p.m. (local time in Germany), and in the remaining leisure hours of the day, including the weekend.

Table B.9 in Online Appendix B shows that the effect of treatment on anonymous editing activity remains stable during both working and leisure hours. The pattern corresponds exactly to our main results during leisure time, and during working hours, an increase is found for the number of edits but not for total content generation.<sup>16</sup> Taken together, these results suggest that the additional content could be generated by non-Wikipedians who skip the registration procedure (anonymous users) and, during the crisis, spend more time online in both working and leisure hours, as well as by committed Wikipedians who contribute more during working hours.

We also explore how district-specific characteristics could moderate the treatment effects of interest. Tables B.10 and B.11 (in the online appendix) show that the districts with a larger share of manufacturing in the total output (above the median) are not driving the results. The rise in unemployment touched districts with a specialization in manufacturing as well as in services, and it changed the internet behavior of all affected regions, including contributions of online knowledge. On the contrary, in the districts where the higher shares of households have access to a high-speed internet (16 Mb per second and more), contributions to Wikipedia increased more strongly than in other districts that were affected by the crisis. This finding is consistent with our interpretation that the increased readership of Wikipedia channeled knowledge contributions.

## 5.5. Robustness Check: Additional Shock in Part-Time Employment (Kurzarbeit)

To shed more light on the mechanism, we exploit the fact that Germany addressed the crisis with a special part-time labor program (Kurzarbeit), which was aimed at preventing layoffs.<sup>17</sup> Because of this program, many workers were effectively working considerably shorter hours for many months, without having to look for a new job and without bearing the high cost of being unemployed. This second type of labor market adjustment allows us to deepen our analysis in two ways. First, we can analyze whether “normal” unemployment and Kurzarbeit have different effects. Second, districts that experienced both shocks were arguably most strongly affected by the economic crisis.

We analyze the interplay of unemployment and Kurzarbeit by dividing our districts into four groups: (1) completely unaffected districts, (2) districts that experienced an increase in the number of part-time employees, (3) districts that had an increase in unemployment, and (4) districts that experienced both shocks. In Online Appendix Table B.12, we analyze the four groups of districts separately. The table shows the three groups of districts with at least one shock separately (“no shock” serves as the baseline). The results show that the effects are driven by districts that were affected by both shocks. One shock alone did not result in an increase in contributions to Wikipedia.

This result corroborates our main finding, by highlighting that the result is driven by more strongly affected districts that experienced both shocks. Because neither of the shocks individually has any significant effect, we cannot discern whether anonymous editors increase their activity because they have more spare time or because they experience the pressure of unemployment. In Online Appendix Table B.14, we show that these results do not change when controlling for economic activity and the industrial structure of a district.

## 6. Analysis for European Countries

To examine the robustness and the potential to generalize our results from the German data set, we perform an additional analysis for a sample of European countries. We focus on countries that were severely affected by the economic crises during the period 2008–2009 and compare them to countries relatively less affected by the economic crises or those where successful policies were implemented to prevent the deepening of the crises. This allows us to examine the relationship of interest in a setting where the variation in the intensity of shocks to unemployment is much higher than across German districts. Another advantage of this analysis is that we can consider total edits to Wikipedia, and hence, we have more and better measures of Wikipedia content, such as views, new words, or active users with various frequency of contributions. We can even observe average edits per article and the average number of hyperlinks set between articles within Wikipedia and to external websites. Different from the previous analysis, we can also leverage the well-established differential timing of different countries entering a crisis.

Before presenting the empirical specification and the results (in Sections 6.2 and 6.3), we briefly discuss our data, which cover 20 European countries and their Wikipedia editions. More details about our data collection can be found in Online Appendix C.2.

## 6.1. Country-Level Data

To analyze content generation at the European country level, we combine data on European countries’ labor markets with aggregate contributions to various versions of Wikipedia of the corresponding countries. Contributions to Wikipedia come from Wikipedia’s monthly statistics for different language editions of Wikipedia provided by the Wikimedia Foundation. We focus on countries that have a unique language, and we also excluded the United Kingdom, Spain, and Portugal, because their languages are spoken in many other parts of the world. We substituted for the Spanish Wikipedia using the Catalan version, which is similarly actively promoted by the Catalan population. Online Appendix Table C.1 shows the Wikipedia language versions that we analyzed. The share of language speakers who live in the corresponding country of origin varies from 71% to 99% (see column (1)).

Wikipedia’s language statistics include aggregates such as the number of Wikipedians, the number of articles in Wikipedia, database sizes, number of words, and readership statistics for all language versions of Wikipedia. We retrieved seven relevant indicators of user activity: (1) aggregate views per month, (2) active Wikipedians with 5–100 monthly edits, (3) active Wikipedians with more than 100 monthly edits, (4) average edits per article, (5) the content growth of the given language edition in terms of words, (6) the total number of hyperlinks between the articles, and (7) the total number of references from the Wikipedia version to external websites. These seven indicators allow us to analyze different aspects of the quantity and quality in the increased contributions to Wikipedia. For example, words capture quantity, whereas edits per article better capture quality.

We consulted the European Central Bank reports to find information about whether a country was affected by the crisis 2008–2009 and when the crisis started. Countries were considered to be affected by the crisis if they experienced a significant decrease in hours worked or an increase in unemployment. For the beginning of the shock we looked at the months of 2008 or 2009 mentioned in the reports and also at the country-level statistics on hours worked. Online Appendix C.2 provides the details of this procedure, and Online Appendix Table C.2 gives an overview over the countries in the sample. It also clarifies which countries we consider affected or unaffected by the crisis.<sup>18</sup>

Figure 3 describes the evolution of a key outcome in Wikipedia: monthly growth measured in words added. We show the medians of the affected and unaffected language editions of Wikipedia in our sample 12 months before and after the crisis together with a scatterplot of different language versions of Wikipedia. The graph illustrates that before the crisis, countries that would be affected grew slower than the unaffected countries, whereas after the crisis, content growth in the affected countries was faster than in unaffected ones. The patterns are similar for views, edits per article, and active Wikipedians, but not for occasional editors. For this variable, we see a difference in the trends that must be accounted for in the regression analysis.

Figure 3. (Color online) Monthly Development of Words Contributed  
![](/api/attachments/SK7U3TEG/fulltext/images/aa2015bbba464d910937074ec0b250d0f8db2feea4969f2138694b3cc09041da.jpg)  
Notes. The figure shows monthly content growth measured in words added. The median values for affected and unaffected countries across the 20 language versions of Wikipedia in our sample are shown as the two lines. The time spans the 12 months before and afte the crisis.

One of the main concerns about these country-level data is the fact that the countries are quite heterogeneous both culturally and economically. Although we cannot easily deal with this issue at the country level, the figure above with the sharp behavioral change gives some confidence that the economic crisis played a role in changing people’s incentives to contribute to Wikipedia.

## 6.2. Empirical Approach

At the country level, we again estimate the differencein-differences model. The regression equation is the following:

$$
\begin{array}{l} \text {Contributions} _ {i t} \\ = \alpha_ {i} + \beta (A f t e r T _ {t} \times T r e a t e d _ {i}) + \nu_ {t} + \epsilon_ {i t}. \end{array}\tag{2}
$$

The unit of observation is country i (and its corresponding Wikipedia language edition) in month t. The dependent variable Contributions measures contributions to Wikipedia (page views, the number of editors who contribute minor and major changes, hyperlinks, etc.). We use the log transformation on all measures of contributions to Wikipedia.<sup>19</sup> The dummy variable Treated distinguishes between countries that were stronger or weaker affected by the economic crises, and $A f t e r T _ { t }$ is another dummy variable, which equals 1 after the month of the shock $t _ { 0 } .$ . As the variable Treated does not vary over time, it drops out in the fixed effects specification. The coefficient for the interaction term of these two dummies $\beta$ measures the treatment effect of interest. The country fixed effect $\alpha _ { i }$ and time fixed effects $\nu _ { t }$ are also included in the regressions. Because we have only 20 units of observation at the country level, we use a 24-month interval, which covers the 12 months before and 12 months after the onset of the crisis.

The timing of the shock, specifically the onset of the crisis for affected countries, is defined as the month when they were hit by the crisis. However, we omitted the month when the crisis began in all specifications, because the crisis broke out gradually in most countries rather than on the first day of the month. By leaving out the month of the onset, we ensure that the treatment period is clearly after the onset of the crisis and the pretreatment period is clearly before the onset. Moreover, omitting that month also gives credit to the notion that an economic crisis typically takes some time to pick up its full momentum.

## 6.3. Results

The results of the baseline DID estimation are shown in Table 4. Each column shows the results for one of our seven dependent variables measuring activity on Wikipedia: (1) article views (Views), (2) active editors with 5–100 edits (Active Editors (5–100 e)), (3) active editors with more than 100 edits (Very Active Editors (>100 e)), (4) edits per article (Avg. Edits per Article), (5) growth of total data in Wikipedia (New Words), (6) internal links (# Wikilinks), and (7) external links (# External Links). The coefficient of interest Treated countries after T suggests that after the shock, there is a 14% increase in the number of active users with few monthly contributions and a 13% increase in active users who heavily edit Wikipedia, contributing more than 100 edits per month. Contributions of new words to language editions of Wikipedia grow by 13%. Articles received on average 6% more edits and 14% more links to external sources of information on the web.

The country-level analysis provides more measures of activity on Wikipedia; therefore, we can take the analysis one level further to generate additional insight into the mechanisms that enable increased content provision to Wikipedia. In Table 5, we highlight the role of viewership as a key mediating factor by analyzing the relationship between viewership and content growth. The table shows the results when using a fixed effects panel analysis in which we regress activity on Wikipedia on views over a 24-month period, 12 months before and 12 months after the onset of crisis. Again, in each column of Table 5, we show our six different measures of contributions to Wikipedia.<sup>20</sup>

The results in Table 5 confirm that views are a crucial predictor for edit-related outcomes except the number of edits per article. An increase in views by 1% is associated with more active editors (0.31% and 0.18%) and more words in Wikipedia articles (0.2%). Moreover, views are positively related to our measures of content quality, the number of internal links set between Wikipedia articles, and external links to information sources. These findings show the role of views as a key mediating factor for additional content generation.

To illustrate the magnitude of the effects we found, we consider the example of Italy, which was one of the countries that was most severely affected by the rise in unemployment. The average unemployment rate in Italy over the observed period was 7.6%, and it increased by 1.2%, which is equivalent to approximately 300,000 additional unemployed people.<sup>21</sup> After the shock, the number of editors with few edits grows by 14%, and, as suggested by our results in Table 4, we would observe 0.14 × 2,440 = 342 additional editors.

## 6.4. Speci<sup>fi</sup>cation Tests

In Online Appendix C, we show several tests that we ran to check the validity of our specification. First, we ran the DID analysis period by period. The results in Online Appendix Table C.3 suggest that the effect was first felt for active editors and then carried over to very active editors and content. We see a lagged effect on views. This analysis further highlights that these variables are properly identified, whereas we cannot reject that edits per article and links to outside references might be on different trends. Second, we control for country-specific trends in Wikipedia content development before the shock (Online Appendix Table C.4). Even after accounting for country-specific trends, our results hold on the number of new active users with small monthly contributions, for monthly views, and for contributed text (“word growth”).

In the third specification test, we verify that the unemployment rate was not positively correlated with contributions before the crisis. This is important, because the crisis is likely to hit weaker economies harder. If contributions to Wikipedia were correlated with unemployment before the crisis, then we could not exploit the European economic crisis to study how an increase in unemployment affects contributions to Wikipedia. We would simply capture the preexisting correlation and erroneously attribute it to the crisis. Hence, we explore the correlation between unemployment and precrisis contributions in Online Appendix Table C.5. We find no correlation between unemployment and contributions to Wikipedia before the shock. Finally, we check the robustness of our OLS approach by using the rate of unemployment among young people (15–24 years old) as an explanatory variable. As expected, young people are more likely to use the internet and, consequently, to contribute to online public goods than older generations. The results (see Online Appendix Table C.6) suggest that both magnitude and significance of the unemployment effect are larger for the young population.

## 7. Discussion, Limitations, and Further Research

Human history includes many instances of social and economic advancement. Each such social and economic restructuring brings new methods of production and consumption, but one unfortunate consequence of progress is that workers with older skills are displaced from their jobs. Our results support that human beings respond to structural economic shifts by reallocating their time to peer production-related activities.

In this paper, we show that higher unemployment is associated with higher participation by volunteers in Wikipedia and an increased rate of content generation. We exploit that some districts/countries were affected by relatively large increases in unemployment whereas others were not, and we show that Wikipedia articles were read more frequently in areas where unemployment increased. The increase in readership was followed by more edits of anonymous or casual editors (“beginners”), and subsequently, the number of highly active users grew. Over time, content growth increased.

Our main analysis is based on a comparison of German districts and a country-level analysis of European economies. At the German district level, districts with higher increases in unemployment had relatively more contributions than less affected districts when the overall downward trend in total contributions to German-language Wikipedia during the crisis are controlled for. We observe almost 4,340 additional edits and 55 MB over the six-month period after the shock. At the European level, contribution growth was more rapid where the crisis hit harder.

We stress several aspects of our findings: First, the effects are consistently found for edits from German districts (Table 2), for edits about German districts (Online Appendix Table B.17), and at the European level (Table 4). Second, the pattern of contributions in Germany and at the European level aligns, because we find that a downward trend in generally less affected Germany was partially mitigated in districts with higher unemployment. Finally, the effects are sizable, and the estimated increases in editing activities typically range from 5% to 20%. For example, our country-level analysis suggests that the number of casual editors (with 5–100 edits/month) grew by 9.5%–14%, as suggested by our results in Table 4 and Online Appendix Table C.4. For the Italian-language Wikipedia, this would mean about 300 additional editors, with 5–100 edits every month. Thus, the overall effect suggests that the threat of unemployment is associated with an increased online contribution of public goods. Because Wikipedia functions as an important knowledge base for the economy, our results document a new and somewhat valuable side effect of the economic crisis.

Our findings open up further questions. Higher unemployment may be associated with greater volunteering and productive time use. Research about prosocial behavior has documented a positive impact of regular volunteering on subjective well-being and happiness, which even increased over time if regular volunteering is sustained (Borgonovi 2008, Binder and Freytag 2013).<sup>22</sup> Moreover, giving and volunteering can have particularly strong, positive, and esteem-enhancing effects in older people and unhappier people (Liang et al. 2001, Post 2005, Cattan et al. 2011, Binder and Freytag 2013).

The relationship of unemployment and online volunteering for Wikipedia highlights a positive energy that might fruitfully be channeled into Wikipedia and similar projects in times of economic crisis. These results are in line with previous findings about the positive effects of volunteering. As such, online volunteering could complement public employment schemes, which are frequently considered useful for inclusion and social skills but are also expensive and of doubtful efficiency (Fervers 2018). Contributing to Wikipedia might be a way that might enhance the cognitive skills and computer skills of those who decide to edit. Likewise, by growing a project that helps millions of others, such contributors might improve their well-being and self-esteem.

Note, however, that the positive effects of prosocial actions have been shown to depend on the volunteer’s autonomous motivation for helping (Weinstein and Ryan 2010). Moreover, the entry threshold for prospective contributors might be high. These findings should be taken into account when designing any interventions that try to leverage the potential of online volunteering. A way to do so would be a coordinated effort of local authorities and the Wikipedia community to integrate prospective new users who are temporarily unemployed but would volunteer to contribute local knowledge to Wikipedia (or contribute their time in similarly constructive ways). Moreover, we cannot fully answer how this mechanism works. In particular, it seems that new editors begin to acquire new capabilities and devote their time to contributing to online public goods. As more new articles are created in Wikipedia every day, the increased participation is focused on adding to existing knowledge as well as on introducing new topics.

Although it is hard to draw definitive conclusions on the identity of the new editors, several of our findings are in line with a mechanism by which the crisis first motivated new users to begin to edit and existing participating editors subsequently increased (to make it “increased”) their activity. First, the effect was strongest in districts that were most severely affected, by both unemployment shock and the adoption of the Kurzarbeit program. Second, the increase was clearly driven by anonymous users, but a large share of the edits seemed to be more valuable than other anonymous edits.<sup>23</sup> Although the number of reverted edits increased, the relative share of reverted edits did not significantly increase. Moreover, there were no robust effects on content deletions. Third, editing by anonymous users preceded more registrations of new users at the European level, and we provided some evidence that the content generation came from edits that were made during leisure time in Germany. Meanwhile, we found much weaker effects in the number of hyperlinks between Wikipedia articles and to external sources. When pretrends were controlled for, the coefficient for Wikipedia links even turned negative, and the coefficient for external links showed nonsignificant effects. These findings might indicate that the observed increase in content generated was due to the activity of inexperienced contributors or minor edits. Unfortunately, fewer links in the content also suggest a decrease in content quality, which would then have been a negative consequence of more activity.<sup>24</sup> In the German data, this pattern was mirrored by a small increase in unproductive edits that had to be reverted. The fact that the share of these edits remained constant does not indicate any negative effect on the quality of content production as a result of unemployment. In sum, these results suggest that a share of the population that faced unemployment first accessed the knowledge in Wikipedia at a higher rate and then began to contribute to the public good.

Although we tested our hypotheses and explored the robustness of our findings from several angles, some limitations cannot easily be overcome. For example, we used the economic crisis as a source of exogenous variation in the economic state and the unemployment rates. This strategy is based on the following identification assumptions. First, contributions to Wikipedia should not be correlated with the likelihood of countries to be affected by the crisis. A specification test in online appendix B.7 provides first supporting evidence for this assumption. Second, using districts and countries as controls requires that the various Wikipedia editions be sufficiently similar and that the districts/countries be somewhat homogeneous with respect to economic and social developments in the period of observation. The qualitatively similar findings in both the country-level and the district-level analyses offer some confidence. Clearly, the institutional, macroeconomic, and political setup is more homogeneous for German districts than it is for European countries. Also, assuming similar Wikipedia editions is no problem for German districts, because the Wikipedia under study is the same.

However, two concerns remain about this analysis, because the regional analysis is based on the IP addresses of anonymous contributions. First, using IP addresses of anonymous contributors allowed for only a restricted set of available dependent variables. Specifically, we can only determine two measures of the efforts in any given region—that is, we have to focus on the number of edits and the length of edits in kilobytes. This is because computing statistics such as the number of active editors, or edits per article, becomes meaningless when we can observe only a part of the edits (from anonymous editors and editors with self-reported location). Second, the use of IP addresses implies that we can look only at a specific set of contributions. These contributions most likely come from new or occasional users, because experienced users typically edit under their user name. In our research, we mitigate this problem by examining edits by registered users who reveal their (self-reported) location.

In addition, even if our identifying assumptions are satisfied, we can only provide indicative evidence on whether the additional content generation is driven by unemployed or employed users. Although this question cannot even be addressed for the country level, for the German district-level data, we could provide an indication that additional edits are more likely during leisure time.<sup>25</sup> Still, it remains unclear as to whether the employed users increase their activity during leisure hours or whether the unemployed prefer to contribute during the hours that we classified as leisure times.

Another fruitful avenue for further research could investigate what is actually written. This question has to remain unanswered at the current stage of our research. Perhaps people are simply writing about the crisis. Such a pattern seems unlikely, given the overall growth that we observe. However, a smaller or larger proportion of the additional readership and content generation in the affected countries might be a direct increase in demand for economic information or the consequence of updating the encyclopedia with current events. Alternatively, increased editing activity might be dedicated to improving the overall quality of articles, or individual users might contribute to their favorite topic of interest, which they also find enjoyable to write about.

Further research could analyze the nature of contributions and the type of articles that are edited. Also, the extent to which district-specific articles are improved or whether articles related to affected professions are edited would be very interesting. These questions are beyond the scope of this paper, and especially at the article level, this analysis is computationally intensive but might lead to additional insights in further research. At the country level, such an analysis is almost unthinkable though, because the data available are too highly aggregated. Beyond that, we could contrast Wikipedia editing activities with other ways in which the newly unemployed use their additional time.

## 8. Conclusion

This study investigated how individuals reallocate their time to the provision of online public goods when faced with increased unemployment. We uncovered a moderate increase in socially valuable volunteering in the form of contributions to Wikipedia. We found this pattern both at the European and the German district levels. The patterns are suggestive of a creative and constructive potential that is freed up as a positive side effect of unemployment and that might carry over to job displacement in general.

The question as to whether unemployment can result in an increased provision of public (online) goods and private learning is crucial, given that we observe accelerating labor substitution as a result of digitization. If a part of the liberated capacity results in increased knowledge documentation and generation, this may be a positive surprise. Even though it remains to be tested how easily the effects we found carry over to digitization-induced job displacement, we highlight a constructive pattern. Our findings show that individuals reacted to increased unemployment during the European economic crisis by reallocating their time to production-related activities and contributing more to Wikipedia.

The results obtained in our study have important practical and policy implications. During the recession that started in late 2008, UK newspapers found increased volunteering. For example, BBC News reported that volunteering agencies such as Community Service Volunteers and YouthNet saw increased inquiries and applications.<sup>26</sup> But at the same time, the Guardian questions whether high youth unemployment may pose a serious challenge for charities to recruit and retain volunteers.<sup>27</sup> Similarly, in the United States, although the Washington Post argued that volunteering had increased despite the recession, the New York Times found decreased volunteering during the same time.<sup>28</sup> These newspaper findings were mostly based on data about offline and formal volunteering and missed important information about online and informal volunteering. To reconcile the mixed findings, Lim and Laurence (2015), using a large survey data set, suggested that overall formal and informal volunteering both declined in the United Kingdom since 2008. They found that the decline is more salient in communities that suffer from social and economic disadvantages, and this decline cannot be explained by individual hardship following financial insecurity. Our paper differs from the prior work in two important ways: First, our data set is based on observed rather than self-reported contributions Second, we focus on online and informal contributions. These two differences allow us to offer additional and complementary evidence. Although, in the offline world, people’s contributions to volunteering work may increase their individual employability, volunteering online through contributions to Wikipedia may not have direct individual benefits, but it creates a positive externality of generating useful knowledge.

The valuable knowledge contributions that occur as a result of worsened economic conditions represent a beneficial side effect that has been overlooked by policy makers. Our results suggest that measures aimed at encouraging knowledge contributions could have a strong effect on volunteering. Policy makers could enhance these beneficial effects by encouraging the active groups in the society to contribute online knowledge more systematically. Although financial aid may jump-start economic recovery, government support on contributions to online public goods will provide valuable channels for knowledge exchange and help encourage skill upgrades in society, turning a crisis into an opportunity. To this end, it is important to better measure online and informal contributions (in addition to those reported by traditional volunteering agencies such as YouthNet and the Red Cross) so that the increased contributions to knowledge can be better captured in official statistics.

## Acknowledgments

The authors benefitted from discussions with Rodrigo Belo, Erik Brynjolfsson, Irene Bertschek, Vivek Ghosal, Shane Greenstein, Marit Hinnosaar, Toomas Hinnosaar, Markus Mobius, Marianne Saam, Patrick Schulte, Frank Verboven Steffen Viete, Joel Waldfogel, and Michael Ward. They thank participants in several presentations at ZEW and in the following conferences: the 13th Conference on the Economics of Information and Communication Technologies (Mannheim), the SEEK Workshop on the Digital Economy (Moncalieri), the 8th Conference on the Economics of Information and Com munication Technologies (ParisTech), the European Associ ation for Research in Industrial Economics 2015 (Munich), and the 5th Strengthening Efficiency and Competitiveness in the European Knowledge Economies (SEEK) Conference (Mannheim). The authors are grateful to the Wikimedia Foundation and Frédéric Schütz for access to the Wikipedia data. They are grateful to Manfred Knobloch for initial sup port with data processing. Ruetger Egolf, Justus Steins, and Alaina Totten provided outstanding research assistance.

## Endnotes

<sup>1</sup> See https://independentsector.org/resource/the-value-of-volunteer -time/ (accessed August 2019)

<sup>2</sup> In Andreoni (2007), the provision of public goods was shown to be subject to congestion. That is, an increase in the number of recipients increased the total provision of public goods but at a decreasing rate

<sup>3</sup> In addition, since the late 1980s, researchers have increasingly contrasted theoretical models with experimental studies in the laboratory. The main insights of this extensive literature have been surveyed by Vesterlund (2006).

<sup>4</sup> Uslaner (2002) uses cross-sectional data from the United States and Canada but cannot use variation from changes in unemployment over time. The outcomes of survey-based studies suggest that volunteers are relatively wealthier, predominantly male, and econom ically more active (Freeman 1997), and that unemployment is negatively correlated with volunteering by men but not by women (Taniguchi 2006).

<sup>5</sup> This finding is in line with Pissarides (1992), who noted that recently unemployed face a threat of a permanent loss of skills and subsequent social decline as time proceeds. Krueger and Mueller (2012) found that the previously unemployed sharply decreased their hours de voted to leisure activities at the time of reemployment (by 35% of the time now allocated to working). In their paper, leisure included computer and internet use. The American Time Use Survey (ATUS) analysis of Aguiar et al. (2013) focused on the period of the global recession in the late 2000s and confirmed earlier findings. They found that more than 50% of the additional time was spent on leisure ac tivities, yet two-thirds were absorbed by watching TV and sleeping. This is in line with the Aguiar et al. (2012) analysis of ATUS data and the changing trends in time allocation. Since the 1960s, individuals have spent more time on leisure, which includes personal computing (but also watching television or engaging in sports). Burda and Hamermesh (2010) analyzed time diary data and concluded that only a small share of the additional time is used for home production. Unemployed people spent more time on other activities such as computer use.

<sup>6</sup> These findings are complemented by Goldfarb and Prince (2008), who showed that poorer people (with internet access) spend more time online, as their opportunity cost for time is lower than that of wealthier people. During economic crises, young and poor people can be threatened by increased unemployment rates or decreased salaries.

<sup>7</sup> In the last decade, the German economy was constantly growing. Therefore, the unemployment rate had a general trend of decreasing. Rather than focusing on the absolute unemployment rate, we focus on changes in the unemployment rate and examine how the changes affect economic agents’ behaviors. In years 2009 and 2010, the decreasing trend of unemployment rate experienced a shock of an increase and then continued decrease after the crisis. This period is very interesting, as it shows that in the generally growing German economy, there was a financial crisis that changed the trend of unemployment.

<sup>8</sup> The Kurzarbeit program existed before the official announcement of the financial crisis. In general, the period of application is six months. However, under exceptional economic conditions, the program can be extended. To combat the economic crisis, German government varied this extension period. Thus, from January to June 2007, employers could use this program to retain their important employees for up to 15 months if the company faces a temporal reduction in demand. Then, this period was reduced to 12 months, but as Germany officially entered into recession, in January 2009, this period was extended to 18 months. Six months later, this period was extended to 24 months for employees who joined the program during the first six months of the recession. As a result, the workers of in dustries experiencing the negative shock could apply reduced working hours up to two years starting in January 2009.

<sup>10</sup> We observe edits and content (in kilobytes) and distinguish reg istered users from anonymous IP addresses.

<sup>11</sup> The standard error is less than 0.05; results are available upon request.

<sup>12</sup> Contributions associated with IP addresses are made only by contributors who skipped the log-in procedure—that is, only by “anonymous” contributors.

<sup>13</sup> Some measurement errors may still exist in the outcome variables. However, as long as these errors are random and uncorrelated with other variables in the model, they induce a bias that works against finding significant results (inflated standard errors) and thus would lead us to err on the side of caution.

<sup>14</sup> Two of the dependent variables—namely, the number of edits performed by anonymous users and that of registered users—could be alternatively estimated using a count data model. Because o distribution properties (the distributions of variables are overdispersed), we chose the negative binomial model for an alternative estimation. Table 21 in the online appendix presents the results, which are consistent with the linear estimations in the baseline specification.

<sup>15</sup> The fixed effect essentially covers all available control variables, because macroeconomic indicators such as the population structure or internet penetration do not vary month to month.

<sup>16</sup> Registered editors increased their activity only during working time (results available upon request)

<sup>17</sup> Rather than laying off their workers, firms could massively reduce working hours, and the state would compensate the workers for a part of their income loss.

<sup>18</sup> Note that the country-level crisis start sometimes differs from the start date we used for the regional-level analysis of Germany (January 2009), where we have more precise data available.

<sup>9</sup> Our findings do not change if we instead normalize the variables with respect to their mean and standard deviation values such that the coefficients represent the changes in the dependent variables in standard deviations.

<sup>20</sup> The measures are as follows: (1) number of active Wikipedians (with at least 5 edits), (2) number of very active Wikipedians (with more than 100 edits), (3) average number of edits per article, (4) new words added, (5) number of internal hyperlinks between articles on Wikipedia, and (6) number of references from Wikipedia articles to an external website.

<sup>26</sup> See http://news.bbc.co.uk/2/hi/uk\_news/8008428.stm (accessed November 2018).

<sup>27</sup> See https://www.theguardian.com/voluntary-sector-network/2012/ jun/07/unemployment-charities-volunteering (accessed November 2018).

<sup>28</sup> See http://www.washingtonpost.com/wp-dyn/content/article/2010/ 06/15/AR2010061501449.html?noredirect=on and https://www.nytimes .com/2009/08/27/us/27volunteer.html (accessed November 2018).

## References

Aguiar M, Hurst E (2007) Measuring trends in leisure: The allocation of time over five decades. Quart. J. Econom. 122(3):969–1006.

Aguiar M, Hurst E, Karabarbounis L (2012) Recent developments in the economics of time use. Annual Rev. Econom. 4(1):373–397.

Aguiar M, Hurst E, Karabarbounis L (2013) Time use during the great recession. Amer. Econom. Rev. 103(5):1664–1696.

Aknin LB, Barrington-Leigh CP, Dunn EW, Helliwell JF, Burns J, Biswas-Diener R, Kemeza I, Nyende P, Ashton-James CE, Norton MI (2013) Prosocial spending and well-being: Crosscultural evidence for a psychological universal. J. Personality Soc. Psych. 104(4):635–652.

Algan Y, Benkler Y, Morell MF, Hergueux J (2013) Cooperation in a peer production economy: Experimental evidence from Wikipedia. Sciences Po Publications info:hdl:2441/5ulf84sluc9.

Andreoni J (1988) Privately provided public goods in a large econ omy: The limits of altruism. J. Public Econom. 35(1):57–73

Andreoni J (1989) Giving with impure altruism: Applications to charity and Ricardian equivalence. J. Political Econom. 97(6): 1447–1458.

Andreoni J (1990) Impure altruism and donations to public goods: A theory of warm-glow giving. Econom. J. 100(401):464–477.

Andreoni J (2007) Giving gifts to groups: How altruism depends on the number of recipients. J. Public Econom. 91(9):1731–1749.

Anthony D, Smith SW, Williamson T (2009) Reputation and reliability in collective goods: The case of the online encyclopedia Wiki pedia. Rationality Soc. 21(3):283–306.

Binder M, Freytag A (2013) Volunteering, subjective well-being and public policy. J. Econom. Psych. 34(February):97–119.

Borgonovi F (2008) Doing well by doing good. The relationship between formal volunteering and self-reported health and happiness. Soc. Sci. Medicine 66(11):2321–2334.

Burda MC, Hamermesh DS (2010) Unemployment, market work and household production. Econom. Lett. 107(2):131–133.

Cattan M, Hogg E, Hardill I (2011) Improving quality of life in ageing populations: What can volunteering do? Maturitas 70(4):328–332.

Chen Y, Harper FM, Konstan J, Li SX (2010) Social comparisons and contributions to online communities: A field experiment on MovieLens. Amer. Econom. Rev. 100(4):1358–1398.

Comino S, Manenti FM, Parisi ML (2007) From planning to mature: On the success of open source projects. Res. Policy 36(10): 1575–1586.

De Chaisemartin C, D’Haultfoeuille X (2017) Fuzzy differences-indifferences. Rev. Econom. Stud. 85(2):999–1028.

Dunn E, Aknin L, Norton MI (2008) Spending money on others promotes happiness. Science 319(5870):1687–1688.

Fervers L (2018) Can public employment schemes break the negative spiral of long-term unemployment, social exclusion and loss of skills? Evidence from Germany. J. Econom. Psych. 67(C):18–33.

Freeman RB (1997) Working for nothing: The supply of volunteer labor. J. Labor Econom. 15(1, Part 2):S140–S166.

Goldfarb A, Prince J (2008) Internet adoption and usage patterns are different: Implications for the digital divide. Inform. Econom. Policy 20(1):2–15.

Hess C, Ostrom E (2003) Ideas, artifacts, and facilities: Information as a common-pool resource. Law Contemporary Problems 66(1):111–145.

Kandel E, Lazear EP (1992) Peer pressure and partnerships. J. Political Econom. 100(4):801–817.

Kaplan HS, Robson AJ (2002) The emergence of humans: The coevolution of intelligence and longevity with intergenerationa transfers. Proc. Natl. Acad. Sci. USA 99(15):10221–10226.

Knabe A, Ratzel S, Sch ¨ ob R, Weimann J (2010) Dissatis ¨ fied with life but having a good day: Time-use and well-being of the unem ployed. Econom. J. 120(547):867–889.

Krueger AB, Mueller AI (2012) Time use, emotional well-being, and unemployment: Evidence from longitudinal data. Amer. Econom. Rev. 102(3):594–599.

Lee RD (2003) Rethinking the evolutionary theory of aging: Transfers, not births, shape senescence in social species. Proc. Natl. Acad. Sci. USA 100(16):9637–9642.

Liang J, Krause NM, Bennett JM (2001) Social exchange and well being: Is giving better than receiving? Psych. Aging 16(3): 511–523.

Lim C, Laurence J (2015) Doing good when times are bad: Volunteering behaviour in economic hard times. British J. Sociol. 66(2): 319–344.

List JA (2011) The market for charitable giving. J. Econom. Perspect. 25(2):157–180.

Pissarides CA (1992) Loss of skill during unemployment and the persistence of employment shocks. Quart. J. Econom. 107(4): 1371–1391.

Post SG (2005) Altruism, happiness, and health: It’s good to be good Internat. J. Behav. Medicine 12(2):66–77.

Sabatini F (2014) The relationship between happiness and health: Evidence from Italy. Soc. Sci. Medicine 114:178–187.

Sun, M, Zhang X, Zhu F (2019) U-shaped conformity in online social networks. Marketing Sci. 38(3):461–480.

Taniguchi H (2006) Men’s and women’s volunteering: Gender dif ferences in the effects of employment and family characteristics. Nonprofit Voluntary Sector Quart. 35(1):83–101.

Uslaner EM (2002) Religion and civic engagement in Canada and the United States. J. Sci. Study Religion 41(2):239–254.

Vesterlund L (2006) Why do people give. Powell WW, Steinberg R, eds. The Nonprofit Sector: A Research Handbook, 2nd ed. (Yale University Press, New Haven, CT), 168–190.

Wallsten S (2013) What are we not doing when we’re online? Goldfarb A, Greenstein SM, Tucker CE, eds. Economic Analysis of the Digital Economy (National Bureau of Economic Research, Cambridge, MA), 55–82.

Walz G, Buiskool BJ, Collewet M, de Koning J Calavrezo O (2012) Short-time working arrangements during the crisis and lessons to learn. Final report, Panteia, Zoetermeer, Netherlands.

Wang C, Zhang X (2009) Sampling of information goods. Decision Support Systems 48(1):14–22.

Wang C, Zhang X, Hann I-H (2018) Socially nudged: A quasi experimental study of friends’ social influence in online product ratings. Inform. Systems Res. 29(3):641–655.

Weinstein N, Ryan RM (2010) When helping helps: Autonomous motivation for prosocial behavior and its influence on well-being for the helper and recipient. J. Personality Soc. Psych. 98(2):222–244.

Xu X, Zhang X (2014) Impact of Wikipedia on market information environment: Evidence on management disclosure and investo reaction. MIS Quart. 37(4):1043–1068.

Zhang, X, Wang C (2012) Network positions and contributions to online public goods: The case of Chinese Wikipedia. J. Man agement Inform. Systems 29(2):11–40.

Zhang XM, Zhu F (2011) Group size and incentives to contribute: A natural experiment at Chinese Wikipedia. Amer. Econom. Rev 101(4):1601–1615.
