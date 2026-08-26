---
otero_id: 5592
otero_key: "5H6GM42H"
title: "Catch Me If You Can: Effectiveness and Consequences of Online Copyright Enforcement"
authors: "Luis Aguiar; Jörg Claussen; Christian Peukert"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2018.0778"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

![](/api/attachments/5H6GM42H/fulltext/images/40bd69297d38bc33592c595df458cf7a3a791d629138c485bd20e5567fceb367.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Catch Me If You Can: Effectiveness and Consequences of Online Copyright Enforcement

Luis Aguiar, Jörg Claussen, Christian Peukert

To cite this article: Luis Aguiar, Jörg Claussen, Christian Peukert (2018) Catch Me If You Can: Effectiveness and Consequences of Online Copyright Enforcement. Information Systems Research

Published online in Articles in Advance 24 Jul 2018

https://doi.org/10.1287/isre.2018.0778

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics. For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Catch Me If You Can: Efectiveness and Consequences of Online Copyright Enforcement

Luis Aguiar,<sup>a</sup> Jörg Claussen,<sup>b,</sup> <sup>c</sup> Christian Peukert<sup>d</sup>

<sup>a</sup> Digital Economy Unit, Joint Research Center, European Commission, 41092 Seville, Spain; <sup>b</sup> Institute for Strategy, Technology and Organization, Munich School of Management, Ludwig-Maximilians University of Munich, 80539 Munich, Germany; <sup>c</sup> Department of Innovation and Organizational Economics, Copenhagen Business School, 2000 Frederiksberg, Denmark; <sup>d</sup> Católica Lisbon School of Business and Economics, Catholic University of Portugal, 1649-023 Lisbon, Portugal

Contact: luis.aguiar@ec.europa.eu, http://orcid.org/0000-0001-6176-7393 (LA); j.claussen@lmu.de, jcl.ino@cbs.dk,

http://orcid.org/0000-0001-8432-8860 (JC); christian.peukert@ucp.pt, http://orcid.org/0000-0003-3997-8850 (CP)

Received: July 14, 2015 Revised: May 31, 2016; April 30, 2017; November 10, 2017 Accepted: January 12, 2018 Published Online in Articles in Advance: July 24, 2018

https://doi.org/10.1287/isre.2018.077

Copyright: © 2018 INFORMS

Abstract. We evaluate the unexpected shutdown of kino.to, a major platform for unlicensed video streaming in the German market. Using highly disaggregated clickstream data in a diference-in-diferences setting, we compare the web behavior of 20,000 consumers in Germany and three control countries. We find that this intervention was not very efective in reducing unlicensed consumption or encouraging licensed consumption, mainly because users quickly switch to alternative unlicensed sites. We highlight that the shutdown additionally had important unintended externalities. Individuals who never visited kino.to and who additionally clicked on news articles that covered the shutdown increased their visits to piracy websites substantially. We show that this efect largely comes from articles that explicitly mention alternative websites or suggest that users do not have to fear legal consequences from unlicensed streaming. Finally, we document that the unlicensed video streaming market is much more fragmented after the shutdown, potentially afecting future interventions, at least in the short run. We argue that our results can be helpful to understand why online piracy rates are still high, despite a plethora of enforcement eforts.

History: Kai-Lung Hui, Senior Editor; Xiaoquan (Michael) Zhang, Associate Editor. Funding: The authors acknowledge the support from FCT–Portuguese Foundation of Science and Technology [UID/GES/00407/2013].

Keywords: antipiracy policy • copyright • movie industry • clickstream • natural experiment

## 1. Introduction

With the advent of file-sharing networks and, more recently, unlicensed online streaming, copyright-infringing content has become easily available to consumers. This raises concerns about sales displacement, continued investment in entertainment products, and overall welfare. Governments have reacted with diferent actions to enforce copyright on the Internet, such as stricter legislation, website blocking, and crackdowns on platforms that host or provide access to infringing content. Despite the many enforcement eforts carried out in the past decade, online piracy rates are still substantially high (UK Intellectual Property Ofice 2016) and have even increased regarding video content (Poort and Weda 2015). Additionally, the available evidence on the efectiveness of individual policies is mixed. Studies suggest that announcements and introduction of stricter laws did not have a lasting efect on box ofice movie revenues in the United States, France, New Zealand, South Korea, Taiwan, and the United Kingdom (Orme 2014, McKenzie 2017). In the context of digital music, new laws in France and Sweden led to an increase in sales of about 25%, but this efect diminished after six months (Adermon and Liang 2014, Danaher et al. 2014). Studies that look at the efect of website blocking find limited reductions in overall piracy consumption (Poort et al. 2014, Danaher et al. 2015a). Finally, the shutdown of the major hosting platform Megaupload was associated with an average increase in licensed digital and theatrical revenues of movie content of less than 10% (Danaher and Smith 2014). Box ofice revenues of narrow-release movies even declined, probably because of the word-of-mouth efects of piracy (Peukert et al. 2017).

The fact that online copyright enforcement policies have been rather unsuccessful in lowering piracy rates or increasing producer surplus remains a puzzle. Drawing on a large body of work across disciplines, we argue that the deterrence efect of online copyright enforcement eforts is likely to be challenged by adaptive behavior on the demand and supply side. In addition, we highlight that unintended externalities can be an important factor in policy implementations. Despite their importance for policy and management, the empirical significance of these efects has not yet been documented.<sup>1</sup> This paper is the first to provide individual-level evidence on the efects of a copyright enforcement intervention on consumer behavior.

The literature shows that increased enforcement efforts can deter unlawful or unethical behavior, both directly and indirectly (Levitt 1997, Ayres and Levitt 1998, DiTella and Schargrodsky 2004, Draca et al. 2011, Bertoni et al. 2013). Shutting down one supplier of infringing content could convince other piracy websites to voluntarily step down and deter new entry.<sup>2</sup> Because consumers’ intentions to pirate and willingness to pay for licensed content are correlated with the perceived risk of prosecution (Chiou et al. 2005, Chiang and Assane 2009, Liao et al. 2010), one could similarly expect enforcement eforts, either targeted at consumers or suppliers, to have externalities. On the other hand, theoretical insights from the economics of crime literature suggest that the effectiveness of law enforcement may be undermined by displacement efects, adaptive behavior, and the industry’s supply behavior (Cameron 1988). Stronger enforcement sometimes simply shifts criminal activity to a diferent time or place (Angrist and Kugler 2008, Adda et al. 2014, Dobkin et al. 2014), or even induces market entry after crackdowns have weakened incumbent criminals (Dell 2015). Recent evidence shows that international cooperation in law enforcement can reduce cybercrime, but also diverts hacker attacks to nonenforcing countries (Hui et al. 2017). Similarly, studies suggest that consumers simply switch the modus operandi of accessing and distributing unlicensed content as a response to stricter enforcement (Lauinger et al. 2013, Arnold et al. 2014, Poort et al. 2014). Such results are in line with the literature on search and switching costs on the Internet (Chen and Hitt 2002, Goldfarb 2006a, b). For example, Goldfarb (2006b) shows that consumers easily switch to a competing website when their preferred website is temporarily unavailable because of denial of service attacks.

An important source of (intended or unintended) externalities could result from the fact that piracy and copyright enforcement actions regularly trigger substantial media coverage.<sup>3</sup> Some authors have frequently articulated the idea that media coverage may reinforce the intended efects of enforcement, leading consumers to reduce piracy consumption and switch to licensed oferings (Al-Rafee and Cronan 2006, Hennig-Thurau et al. 2007, Sinha and Mandel 2008, Danaher et al. 2010, Cox and Collins 2014).<sup>4</sup> However, not all news articles contain a clear-cut antipiracy message. Zamoon and Curley (2008) study the contents of U.S. newspaper articles about software piracy and document that around the same number of articles condemn and condone piracy. Furthermore, in situations where the legal status of downloading and streaming is ambiguous, news articles may provide legal information—for example, by citing lawyers—that can afect consumption choices in diferent ways.<sup>5</sup> Indeed, there is some evidence that consumers use arguments put forward in the mass media to rationalize their piracy behavior (Vida et al. 2012). Regardless of their tone, news articles may also simply inform consumers about the existence of unlicensed content on the Internet. This information can facilitate switching to alternative unlicensed oferings for consumers already in the market, and it may lead previously uninformed consumers to start pirating following news reports.

While we are not aware of any systematical evidence of media-induced externalities of copyright enforcement, findings from a variety of empirical contexts show that information in mass media can have direct and indirect efects on individuals’ behavior. For example, Goh et al. (2011) show that newspaper reports afected how many consumers opt in for a consumer protection policy. Media coverage of suicides is also known to be related to subsequent increases in suicide rates (Gould 2001), and there is robust evidence of a link between media and violent behavior against others. For example, Yanagizawa-Drott (2014) and Adena et al. (2015) show that radio broadcasts increased participation in violence in the Rwandan genocide and Nazi Germany. Esser and Brosius (1996) document that the number of right-wing violent ofenses increases with the intensity of TV news coverage of previous right-wing violent ofenses. Finally, exposure to public health campaigns aiming at establishing social norms for issues such as smoking, drinking, unsafe sex, and cancer prevention can be negatively correlated to people’s attitudes and intentions of use (Cho and Salmon 2007).

We examine the extent of the intended and unintended consequences of online copyright enforcement using URL-level clickstream data that allow us to observe all web browsing of 20,000 individuals in Germany, France, Italy, and the United Kingdom throughout 2011. We exploit the exogenous timing of the shutdown of the then-dominant German streaming website kino.to in June 2011 as a natural experiment. In a diference-in-diferences setting, we compare licensed and unlicensed video consumption of consumers in Germany to a control group of consumers in three other countries, before and after the shutdown.

Our aggregate results show that the efectiveness of the shutdown of kino.to was limited, confirming previous findings regarding other copyright enforcement cases and diferent data. Comparing German users to international users, we see a moderate reduction in visits to piracy sites of 4.5%. We also fail to find much evidence for substitution into consumption of licensed video content, as German users do not diferentially change their visits to movie theaters’ websites, licensed online video services (such as Maxdome, Lovefilm, and iTunes), or DVD/Blu-ray-related pages on Amazon.

Our individual-level data allow us to go far beyond a simple aggregate analysis. Distinguishing diferent types of users, we find that individuals who were using kino.to before its shutdown decreased their piracy consumption by about 27%. Because consumers substitute toward existing and newly entering alternative unlicensed websites, this decrease is much lower than what could have been expected given kino.to’s 79% market share. Most interestingly, we find evidence of unintended externalities. On average, individuals who never visited kino.to increased their visits to other piracy websites by 0.8%. We show that this efect is driven by individuals who clicked on news articles that discussed the shutdown of kino.to. Those users increase their visits to piracy websites by about 35%. Looking at the content of these news articles, we find that this efect mainly comes from articles that directly mention alternative piracy websites, or indicate that consumers do not have to fear prosecution when using streaming sites.

Finally, we assess the postshutdown structure of the market for unlicensed video streaming in Germany. While the market was initially largely dominated by kino.to, it ended up being much more fragmented after its shutdown. In the observed six-month period after the shutdown, the market was evenly split between movie2k.to (the second largest player at the time of the shutdown), kinoX.to (a new entrant), and 17 other websites, which cumulatively accounted for onethird of the market. Future interventions in the German market may therefore be potentially more costly and less efective after the shutdown of kino.to, at least in the short run.

Our paper makes an important contribution to an emerging literature documenting the importance of public policy externalities for both policy and management (e.g., Goh et al. 2015). Our key contribution to the piracy literature is to highlight that not only direct but also indirect efects need to be taken into account when evaluating the efectiveness and consequences of copyright enforcement eforts. This can help us understand why we still observe high piracy rates despite the abundance of enforcement eforts that have been carried out in the past.

Our results generate at least two important and novel implications. First, we provide evidence that consumers find it easy to switch to alternative unlicensed services, which substantially reduces the efectiveness of the enforcement efort. Second, an enforcement efort that creates publicity can backfire if some consumers that were previously uninformed start using unlicensed oferings. This challenges the idea—often put forward in the piracy literature, but never tested in observational data—that the media can be helpful in educating consumers about possible consequences of unlicensed consumption, and in persuading them to stop pirating and switch to licensed oferings. With this in mind, we discuss implications for future antipiracy policy. From a managerial perspective, opening the “black box” of consumer behavior can be helpful to design private copyright enforcement strategies, as well as to understand the competition between licensed and unlicensed services.

While our analysis provides rich insights, it remains a case study with context-specific results. Based on a careful discussion of the available evidence and established results in the literature, we conclude that it is unlikely that a similar experiment in a diferent institutional and geographic setting would yield very diferent results. However, the historical context is likely to afect our results on substitution toward licensed consumption. We speculate that better availability and lower prices of licensed content can convince consumers to switch to licensed oferings (Danaher et al. 2010, 2015b; Poort and Weda 2015; Aguiar and Waldfogel 2018).

## 2. Movie Piracy and the Shutdown of kino.to

Consumption patterns of entertainment products have drastically changed in the 21st century. Ever since the advent of Napster in 1999 and the creation of subsequent file-sharing networks, individuals are able to freely share and access vast amounts of digital media files. The primary mode of access to unlicensed content in recent times is the system of cyberlockers and linking sites.<sup>6</sup> In their simplest form, cyberlockers are online services that allow Internet users to upload and store large files. While this type of service can be used to back up any type of personal data, it can also be used to share copyright-protected files such as movies and episodes of TV series (Antoniades et al. 2009, Liu et al. 2013). Once a file is uploaded, the uploader receives a download URL, which can be shared with other individuals, for example, by posting the link on a website where anyone can get direct access. These linking sites, or sometimes called streaming sites, would typically do more than simply provide access to these links, as they would also categorize content, make it searchable, and provide metainformation (such as credits and ratings).<sup>7</sup> Like many licensed services, this ecosystem essentially runs on advertising revenues.<sup>8</sup> The more visits a cyberlocker gets, the higher the advertising revenue. To generate trafic to its website, a cyberlocker will sometimes pay uploaders a share of the advertising revenue generated by their uploaded content. Linking sites also show third-party ads to final consumers. Therefore, an individual who visits the linking website and clicks on the link enjoys free content and generates revenue for the cyberlocker, the initial uploader, and the linking site. Of course, the content creator or rightsholder is usually not compensated at all. This is why we refer to this type of consumption as “unlicensed” throughout this paper. Overall, this whole process has enabled cyberlockers to store huge amounts of movies, episodes of TV series, e-books, and recorded music. Linking websites play a crucial role in the unlawful sharing of copyright-protected content by acting as platforms for uploaders and final consumers.

The German market for unlicensed video content had a substantial size in 2010, with at least one million people (more than 1% of Germany’s entire population) using cyberlockers and linking sites to stream or download 54 million movies and 23 million TV show episodes (GfK et al. 2011, p. 17).<sup>9</sup> While a significant number of linking sites were active in the German market, kino.to was—as will be detailed below—the dominant platform providing access to unlicensed video streaming in 2011. Following a complaint filed by movie industry representatives, a raid involving police, computer specialists, and tax oficers led to the seizure of kino.to on June 8, 2011, efectively removing access to copyright-infringing content. In the couple of months following the intervention, visitors of www.kino.to were shown a police notice stating that the domain had been seized, the owners had been arrested, and users that had created or distributed unlawful copies of copyrighted material may face prosecution. As a result of various court decisions between December 2011 and June 2012, six members of kino.to’s management team were sentenced to prison for up to four and a half years (Spiegel Online 2012).

Given the massive popularity of kino.to, its shutdown generated tremendous media attention, published in all kinds of outlets, including major ones such as Bild (Germany’s largest tabloid) or Süddeutsche Zeitung (Germany’s largest national daily newspaper). As we detail below, we observe 1,835 distinct URLs of news articles or blog posts covering or following up on the shutdown.

A verdict from a German court sheds some light on the contents of kino.to and the revenues it generated (Amtsgericht Leipzig 2011). Users of kino.to had clicked 1.74 billion times on links to movies and TV episodes between September 1, 2010, and June 8, 2011, alone, an average of some 7 million clicks per day. The district court considered that the website ofered at least 1.3 million links to some 21,000 motion pictures, 7,000 documentaries, and 106,000 TV episodes. Kino.to provided about 10 alternative links for each movie, about 2 for each documentary, and about 8 for each TV episode. Content was not directly hosted by kino.to, but mostly by external cyberlockers. Interestingly enough, kino.to owned some of these cyberlockers (freeload.to and ebays.to). The district court considered that at least 12,970 links (less than 1% of the total number of links) pointed to content hosted on vertically integrated cyberlockers. The owners of kino.to assumed an active role in obtaining links to video files, setting incentives for uploaders, and enforcing minimum quality standards. Monthly advertising revenues are estimated at e150,000, which amounts to almost e6 million over the period from March 2008 to June 2011. During the same period, revenues from integrated cyberlockers were some additional e634,000.

## 3. Data and Methodology 3.1. Data Source and Structure

We have access to clickstream data from Nielsen’s Internet audience measurement service, NetView. This service monitors the online activity of a large number of Internet users by recording all of their URL visits via an application that is installed on the consumer’s device (desktop PC or Mac) and operates in the background. Consumers are incentivized to take part and stay in the panel by a rewards program, in which they can exchange credit points for retail and travel vouchers. Consumers earn a fixed amount of credit points every month and take part in a lottery every quarter.<sup>10</sup> Upon signing up, Nielsen requires participants to fill out a survey about basic demographics, such as household size, net household income, age, gender, education, and employment status.<sup>11</sup>

Our sample consists of the browsing history of 5,000 individuals each in Germany, France, Italy and the United Kingdom throughout 2011, totaling 20,000 users. We observe the URL of every website an individual has visited together with a time stamp, the referral URL, and the amount of time spent on that URL.<sup>12</sup> The URL information lets us distinguish diferent kinds of online activities. Most importantly, it allows us to identify visits to web pages linking to copyright-infringing content—such as unlicensed video streaming—as well as domains related to licensed video consumption. The great level of detail in this data even allows us to go beyond the website level. For example, we distinguish diferent product categories users are browsing on Amazon, or identify whether users are accessing news articles related to the shutdown of kino.to. We aggregate the data from the clickstream level to the user-week level, so that the unit of observation for most of our analyses is the weekly sum of clicks per user in a specific content category, for example, unlicensed video streaming websites. With 52 weeks, 5,000 users per country, and four countries, we have 1,040,000 observations.

## 3.2. Variables

All variables are defined in Table 1 and introduced in more detail below. Descriptive statistics are reported in Table 2.

3.2.1. Piracy Consumption. Measuring the consumption of unlicensed video content requires the identification of websites providing access to such content.

Table 1. Variable Definitions

<table><tr><td>Variable</td><td>Definition</td></tr><tr><td colspan="2">Dependent variables</td></tr><tr><td>Piracy (ln +1)</td><td>Weekly visits to piracy websites</td></tr><tr><td>Piracy: Streams (ln +1)</td><td>Weekly number of downloads from piracy websites</td></tr><tr><td>Piracy: Days (ln +1)</td><td>Weekly number of weekdays where the user visited piracy websites</td></tr><tr><td>Piracy: Duration (ln +1)</td><td>Weekly duration of visiting piracy websites</td></tr><tr><td>Alt. Piracy (ln +1)</td><td>Weekly visits to alternative piracy websites, that is, all sites excluding kino. to</td></tr><tr><td>Licensed: Cinema (ln +1)</td><td>Weekly visits to cinema websites</td></tr><tr><td>Licensed: Online (ln +1)</td><td>Weekly visits to licensed streaming websites</td></tr><tr><td>Licensed: DVD (ln +1)</td><td>Weekly visits to the DVD section of Amazon</td></tr><tr><td colspan="2">Independent variables</td></tr><tr><td>After (0/1)</td><td>One after the shutdown of kino. to in week 23 of 2011</td></tr><tr><td>Kino (0/1)</td><td>One if a German user visited kino. to before the shutdown</td></tr><tr><td>Non-Kino (0/1)</td><td>One if a German user never visited kino. to</td></tr><tr><td>News (0/1)</td><td>One after a German user read news about the shutdown of kino. to</td></tr><tr><td>News: Background (0/1)</td><td>One after a German user read news on the kino. to shutdown that included a background report</td></tr><tr><td>News: Alternatives (0/1)</td><td>One after a German user read news on the kino. to shutdown that mentioned illegal alternatives</td></tr><tr><td>News: Legal (0/1)</td><td>One after a German user read news on the kino. to shutdown that considered streaming from kino. to as legal</td></tr><tr><td>News: Illegal (0/1)</td><td>One after a German user read news on the kino. to shutdown that considered streaming from kino. to as illegal</td></tr><tr><td>Kino: Single Homing</td><td>One if a German user visited kino. to and visited no other piracy websites before the shutdown</td></tr><tr><td>Kino: Multihoming</td><td>One if a German user visited kino. to and at least one other piracy website before the shutdown</td></tr><tr><td>Non-Kino: Pirate</td><td>One if a German user never visited kino. to and visited at least one other piracy website before the shutdown</td></tr><tr><td>Non-Kino: Nonpirate</td><td>One if a German user never visited kino. to and visited no other piracy websites before the shutdown</td></tr><tr><td>Germany</td><td>One for German users</td></tr></table>

We both manually went through the top 1,000 domains classified by Nielsen as entertainment-related websites and used available lists of piracy websites in 2011.<sup>13</sup> This led us to a total of 20 websites ofering unlicensed video streaming content, which defines our unlicensed video streaming market in Germany. By far, the most popular site in this set is kino.to, which was visited around 6,000 times per week between January 2011 and June 2011 in our sample. This is more than eight times the trafic received by the second most visited website in our data, movie2K.to, which had an average of 730 weekly visits over the same time period. The 20th and last website included in the definition of the German movie streaming piracy market, streams.to, received an average of less than 1 weekly click between January 2011 and June 2011. With a weekly average of 79% market share, kino.to was clearly the dominant unlicensed movie streaming platform in the German market at the time of its shutdown. We perform a similar exercise to define the corresponding unlicensed video streaming markets in Italy, France, and the United Kingdom.

Table 2. Descriptive Statistics

<table><tr><td rowspan="2"></td><td colspan="2">Kino before</td><td colspan="2">Kino after</td><td colspan="2">Non-Kino before</td><td colspan="2">Non-Kino after</td><td colspan="2">Control before</td><td colspan="2">Control after</td></tr><tr><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td><td>Mean</td><td>SD</td></tr><tr><td>Piracy</td><td>8.566</td><td>26.327</td><td>7.805</td><td>35.030</td><td>0.105</td><td>2.898</td><td>0.383</td><td>9.164</td><td>0.915</td><td>9.225</td><td>1.053</td><td>14.487</td></tr><tr><td>ln(Piracy + 1)</td><td>0.798</td><td>1.400</td><td>0.604</td><td>1.296</td><td>0.014</td><td>0.189</td><td>0.035</td><td>0.319</td><td>0.103</td><td>0.535</td><td>0.108</td><td>0.558</td></tr><tr><td>Piracy: Streams</td><td>0.986</td><td>4.458</td><td>0.687</td><td>4.389</td><td>0.004</td><td>0.150</td><td>0.022</td><td>0.711</td><td>0.172</td><td>1.900</td><td>0.195</td><td>2.679</td></tr><tr><td>Piracy: ln(Streams + 1)</td><td>0.255</td><td>0.654</td><td>0.169</td><td>0.549</td><td>0.001</td><td>0.045</td><td>0.007</td><td>0.105</td><td>0.043</td><td>0.289</td><td>0.044</td><td>0.299</td></tr><tr><td>Piracy: Days</td><td>0.697</td><td>1.445</td><td>0.530</td><td>1.314</td><td>0.012</td><td>0.179</td><td>0.027</td><td>0.274</td><td>0.096</td><td>0.557</td><td>0.099</td><td>0.572</td></tr><tr><td>Piracy: ln(Days + 1)</td><td>0.322</td><td>0.562</td><td>0.241</td><td>0.512</td><td>0.006</td><td>0.083</td><td>0.015</td><td>0.124</td><td>0.047</td><td>0.234</td><td>0.048</td><td>0.238</td></tr><tr><td>Piracy: Duration</td><td>143.802</td><td>447.674</td><td>152.198</td><td>835.740</td><td>2.578</td><td>68.715</td><td>9.852</td><td>272.952</td><td>31.950</td><td>364.358</td><td>27.629</td><td>371.705</td></tr><tr><td>Piracy: ln(Duration + 1)</td><td>1.567</td><td>2.567</td><td>1.185</td><td>2.383</td><td>0.033</td><td>0.413</td><td>0.079</td><td>0.656</td><td>0.240</td><td>1.161</td><td>0.237</td><td>1.140</td></tr><tr><td>Licensed: Cinema</td><td>0.505</td><td>3.050</td><td>0.426</td><td>3.095</td><td>0.194</td><td>2.013</td><td>0.190</td><td>1.986</td><td>0.599</td><td>6.416</td><td>0.539</td><td>4.459</td></tr><tr><td>Licensed: ln(Cinema + 1)</td><td>0.122</td><td>0.491</td><td>0.100</td><td>0.451</td><td>0.044</td><td>0.307</td><td>0.043</td><td>0.303</td><td>0.121</td><td>0.503</td><td>0.114</td><td>0.485</td></tr><tr><td>Licensed: Online</td><td>0.468</td><td>4.899</td><td>0.470</td><td>4.957</td><td>0.276</td><td>4.636</td><td>0.224</td><td>3.213</td><td>0.111</td><td>2.541</td><td>0.136</td><td>2.786</td></tr><tr><td>Licensed: ln(Online + 1)</td><td>0.079</td><td>0.421</td><td>0.074</td><td>0.417</td><td>0.044</td><td>0.316</td><td>0.041</td><td>0.301</td><td>0.022</td><td>0.216</td><td>0.025</td><td>0.233</td></tr><tr><td>Licensed: DVD</td><td>0.425</td><td>3.644</td><td>0.484</td><td>4.800</td><td>0.215</td><td>2.537</td><td>0.255</td><td>3.230</td><td>0.124</td><td>1.989</td><td>0.172</td><td>2.981</td></tr><tr><td>Licensed: ln(DVD + 1)</td><td>0.095</td><td>0.427</td><td>0.093</td><td>0.435</td><td>0.052</td><td>0.312</td><td>0.059</td><td>0.335</td><td>0.030</td><td>0.238</td><td>0.037</td><td>0.269</td></tr></table>

Note. Kino <sup>(</sup>N <sup></sup> 843<sup>)</sup>, Non-Kino <sup>(</sup>N <sup></sup> 4,157<sup>)</sup>, Control <sup>(</sup>N <sup></sup> 15,000<sup>)</sup>.

Piracy: Visits. Our preferred measure of piracy usage is the weekly number of visits to the piracy websites described above.

One may be worried that visits to those types of sites do not provide a perfect measure of video content consumption. Before being able to stream a movie, a user would need to make a number of navigational clicks, for instance, searching or browsing through content or selecting a server that provides the video stream. Therefore, a potential concern would be that the unlicensed websites in our sample difer in their design. For example, this may lead to a smaller number of necessary clicks to consume content on kino.to compared to alternative websites. It may be possible that some websites do not ofer the desired content, and that the observed clicks to those domains reflect only search as opposed to consumption. To address these issues, we rerun our regressions using three alternative measures of unlicensed video consumption, which we present below.

Piracy: Streams. We exploit the fact that a website like kino.to does not directly host video content, but only provides links to cyberlockers (external servers that operate under a diferent domain name, e.g., Megavideo.com). Using historical information available online, we compile a list of 34 cyberlocker services. In our raw clickstream data, we flag a streaming session whenever we observe a click to a linking site that is directly followed by a click to a cyberlocker site, or clicks to cyberlocker sites where a linking site is listed as the referral.

Piracy: Days. This is a measure of the extensive margin of piracy consumption, making use of daily variation within users. We count the number of days on which a given individual uses an unlicensed video streaming website in a given week. A piracy day is flagged as such if we observe at least one visit to an unlicensed website. In this way, we address the concern that some platforms may require more clicks than others to reach content.

Piracy: Duration. Our third alternative measure is the time spent on each URL (in seconds). While video consumption should result in much higher values compared to navigational clicks, a few practical issues challenge the accuracy. For example, Nielsen records only time spent on pages in focus and time stops recording once the user switches to another tab. While this implies that the duration provided by Nielsen will potentially underestimate the time spent on each URL, this measure is still strongly correlated with the true time spent on each URL.<sup>14</sup>

3.2.2. Licensed Consumption. Our data provide us with good proxies for several licensed video consumption channels. In particular, we can observe visits to websites related to movie theaters, licensed online video services, and DVD/Blu-ray purchases.

Licensed: Cinema. We proxy for movie theater visits by measuring clicks on the main movie portals that include showing times (e.g., kino.de, mymovies.it) as well as the websites of the major movie theater companies in a given country.<sup>15</sup>

Licensed: Online. We track visits to paid licensed video services. While European consumers could not subscribe to flat-rate services that were already popular in the United States (e.g., Netflix) and the number of digital pay-per-view services was limited in 2011, we are still able to measure the visits to platforms such as Canalplay, Mediaset Premium, CinemaNow, Lovefilm, and iTunes.<sup>16</sup>

Licensed: DVD. We proxy for DVD and Blu-ray sales by measuring visits to pages in the DVD and Bluray categories on Amazon.<sup>17</sup> The home video market was dominated by DVD and Blu-ray in 2011, with a market share of more than 96%, leaving less than 4% to digital channels, in Germany (GfK and Bundesverband Audiovisuelle Medien 2013), and similar shares in other European countries.<sup>18</sup>

3.2.3. User Types. Because individuals may be affected diferently by the shutdown of kino.to, it is useful to define groups according to their characteristics. In the German sample, 16.9% of the users visited the kino.to website at least once between January 1, 2011 and June 8, 2011. We refer to these individuals as the Kino users, and to the individuals who never visited kino.to before its shutdown as Non-Kino users.

For an additional analysis, we also construct a more granular distinction of user types. We distinguish between users of kino.to that did not visit any other piracy websites before the shutdown (Kino: Single Homing) and those that did (Kino: Multihoming). Similarly, we distinguish between nonusers of kino.to who visited unlicensed streaming sites before the shutdown (Non-Kino: Pirate) and those who did not (Non-Kino: Nonpirate). Finally, for the purpose of analyzing aggregate efects, we group all German users in a variable named Germany.

3.2.4. News Consumption. To measure news readership, we collected news articles and blog posts covering or following up on the shutdown of kino.to. We pulled search results for the term “kino.to” from Google, Google News, and the proprietary news databases Factiva and LexisNexis and went through all 112.7 million URLs accessed by German users in our data to identify those that included some version of “kino.to” (Zeit Online 2011). After careful manual cleaning, we arrived at 1,835 distinct URLs of news articles. When matching these URLs back to our clickstream data, we obtained 170 news articles that were actually visited by the individuals in our sample. We then created the dummy variable News, which turns one when a user clicks a corresponding URL for the first time.

In the next step, we classified the content of news articles (Zamoon and Curley 2008, Goh et al. 2011) into one of the four following categories: Background, Illegal, Legal, and Alternative websites. Roughly a third of the articles cover topics in multiple categories. Examples of background stories (News: Background; 44%) include “Polizei schaltet kino.to ab [Police takes down kino.to]” in Zeit Online (2011) and “Millionenkonten bei kino.to entdeckt [Millions found in kino.to bank accounts]” in Süddeutsche Zeitung (2011), which summarize key facts about kino.to and the procedure and surrounding events of the takedown. Articles like “Millionen Nutzer haben Angst [Millions of users fear legal action]” and “Kino.to: GVU will Nutzer verfolgen und bestrafen [GVU wants to prosecute and punish users]” quote industry representatives or lawyers saying that consumers may face criminal and civil prosecution. We include articles featuring such claims in the category News: Illegal (11%) (NTV 2011, Chip Online 2011). Typical claims in the News: Legal (7%) category are that streaming may not count as copying in the sense of German copyright law, and consumers therefore do not need to fear legal consequences (Focus Online 2011, Freenet 2011). The last category of media coverage, referring to unlicensed alternative websites (News: Alternatives; 46% of the articles), includes stories such as “Kino.to-Nachfolger bereits online: Video2k.tv [Kino.to successor already online]” in Gulli (2011) and “Illegales Filmportal ist zurück—Kino.to-Piraten verhöhnen Ermittler [Illegal movieportal is back—Kino.topirates mock investigators]” in Bild (2011).

The diferent types of stories published in news outlets following the shutdown of kino.to illustrate the idea that media coverage may generate externalities going in several directions. On one hand, coverage may deter consumers from using alternative websites out of fear of legal action. On the other hand, media coverage may inform users of the seized platform about the existence of alternative websites and therefore lower search and entry costs. Similarly, it may also inform individuals who were initially unaware of the existence of such websites, causing them to start consuming unlicensed content online.

## 3.3. Estimation Strategy

3.3.1. The Shutdown of kino.to as a Natural Experiment. The main goal of this paper is to contribute to the understanding of the efectiveness and consequences of online copyright enforcement. The richness of our highly disaggregated data allows us to not only investigate direct efects but also provide evidence for potentially confounding or reinforcing indirect efects. Like many recent studies that are interested in evaluating antipiracy or cybercrime enforcement policy (e.g., Adermon and Liang 2014, Danaher and Smith 2014, Reimers 2016, Peukert et al. 2017, Hui et al. 2017, Zhang 2018), we focus on a specific empirical setting, and interpret the shutdown of kino.to as a natural experiment that removes an important option from the consumers’ entertainment choice set, suddenly and unexpectedly.

A number of facts indicate that the timing of the shutdown was indeed exogenous to all parties involved—the movie industry, consumers, and the owners of kino.to. First, the management team did not seem to know about the intervention of kino.to as they did not relocate to a third country before their arrest.<sup>19</sup> We therefore do not expect them to have carried out any type of strategic action, for example, removing links, in anticipation of a crackdown. Second, our data show no evidence of consumers changing their visits to kino.to shortly before the domain went ofline. Finally, although industry representatives were seemingly involved in the investigations, it is very unlikely that they could have afected the exact timing of the operation in a way that would afect the dependent variables in our analysis. We could not find any evidence that movie theaters or ofline or online retailers (including licensed video platforms) strategically changed contents or prices—either in anticipation of the precise date of the shutdown or afterward.

3.3.2. Econometric Model. Following the policy evaluation literature (e.g., Card and Krueger 1994), we use a diference-in-diferences approach in which we compare the behavior of consumers that were afected by the policy to the behavior of consumers that remained unafected. Under some moderate assumptions, this allows us to establish a plausibly causal estimate of the impact of the shutdown of kino.to on the consumption of both unlicensed and licensed video content.

Individuals located outside of German-speaking countries constitute a good control group because they are unlikely to be afected by the shutdown of kino.to, either directly or indirectly. First, we observe essentially zero clicks to kino.to from users located in Italy, France, and the United Kingdom. Second, media coverage of the shutdown was almost exclusively limited to news articles in German outlets and written in German.<sup>20</sup> Because we are interested in testing for externalities caused by the intervention, we distinguish between two diferent treatment groups within Germany. The first group, which includes individuals that visited kino.to before its shutdown (Kino users), were directly afected by the intervention. The second group of consumers includes German individuals that never visited kino.to (non-Kino users). By definition, these individuals could have been afected only indirectly by the shutdown.

The identifying assumption in any diference-in-differences setting is that the dependent variable would have followed a similar trend in the treatment and control groups had the policy shock not happened. A necessary condition for this assumption to hold is that trends of treatment and control groups do not difer before the intervention. Using the long time dimension of our data, we provide some statistical insights that support this assumption, and therefore address the concern that changes in the dependent variable would have occurred in the absence of the policy shock.

The baseline specification of our diference-in-diferences model is defined as follows:

$$
\begin{array}{l} \ln (C l i c k s _ {i t} + 1) \\ = \alpha + \delta_ {1} (A f t e r _ {t} \times K i n o _ {i}) + \delta_ {2} (A f t e r _ {t} \times N o n - K i n o _ {i}) \\ \quad + \sum_ {c} \beta_ {c} (t \times C _ {c}) + \beta_ {1} (t \times K i n o _ {i}) + \beta_ {2} (t \times N o n - K i n o _ {i}) \\ \quad + w _ {t} + \mu_ {i} + \varepsilon_ {i t}, \end{array} \tag {1}
$$

where $C l i c k s _ { i t }$ refers to the number of visits to either unlicensed or licensed video consumption websites of individual i in week $t , t$ is a linear time trend, $K i n o _ { i }$ and Non-Kino indicate whether individual i is a Kino user or a German nonuser of Kino, After is a dummy variable equal to one during the weeks after the shutdown, the $\beta$ coeficients capture country- and group-specific time trends, and $\varepsilon _ { i t }$ is an individual-time specific error term. The δ coeficients correspond to the efects of the shutdown on the two treatment groups. Specification (1) also includes week fixed efects and individual fixed efects, which allow us to control for any unobserved week-specific and cross-sectional-invariant factors as well as individual-specific and time-invariant factors. Note that the terms corresponding to $A f t e r _ { t } ,$ $K i n o _ { i } ,$ and Non-Kino are not included in the specification as they are implicitly controlled for by the week and individual fixed efects. Following the literature, we estimate Equation (1) using ordinary least squares (OLS) and cluster standard errors at the individual level (Bertrand et al. 2004). As the individual-level data tend to be dispersed, and as we are interested in relative changes, we use the logarithm of the number of clicks as a dependent variable.<sup>21</sup>

## 4. Results

In what follows, we first show how the shutdown affected the consumption of unlicensed video content, both directly and indirectly. We then provide evidence that exposure to news articles that discuss the shutdown can explain the externalities we observe and show how this varies across categories of news articles. We go on to examine how the shutdown afected the consumption of licensed alternatives. We provide additional evidence that indirect efects and externalities are driven by how much knowledge individuals had about unlicensed alternatives, by distinguishing between single-homing and multihoming users. We then zoom out and discuss what our results imply on the aggregate and speculate about welfare efects. Finally, we discuss the changes in the overall structure of the market for unlicensed video consumption after the enforcement efort. Throughout, we present a range of robustness checks regarding the identifying assumption of the diference-in-diferences model and potential measurement error in the dependent variable.

## 4.1. Efects on Unlicensed Video Consumption

4.1.1. Descriptive Evidence and Parallel Trends. We start our analysis with a descriptive look at how the consumption of unlicensed content changed with the shutdown. The plot of average overall piracy levels in Figure 1 shows that the overall number of visits to unlicensed video streaming sites declined substantially right after kino.to was removed from the market. However, this decline is clearly not as strong as the decline in visits to kino.to. Furthermore, visits to piracy websites quickly increase again following the fifth week after the shutdown and almost return to pre-intervention levels toward the end of the observed period.

Figure 2 plots the average total clicks to piracy websites separately for Kino users, non-Kino users, and users in France, Italy, and the United Kingdom (termed “international users” in the remainder of the text). For Kino users, we observe a strong decline in piracy consumption directly after the shutdown, which quickly recovers and then stagnates from the fifth week after the shutdown onward. The postshutdown levels of Kino users stay below the preshutdown levels for the entire period of observation. Looking at non-Kino users, we first observe that their average piracy levels are substantially lower than the piracy levels of Kino users. However, we see a sharp increase directly after the shutdown, which still remains much lower than the piracy levels of Kino users. The group of international users shows fairly stable levels of piracy consumption throughout the observed period. Most importantly, Figure 2 provides evidence that the necessary condition of the parallel trends assumption seems to hold. Average piracy levels of Kino users, non-Kino users, and international users follow very similar trends before the shutdown. Furthermore, the fact that overall piracy levels of international users remain stable throughout the entire year, and do not markedly change with the shutdown, strongly suggests that these individuals constitute a valid control group.

We now go beyond this simple visual inspection and provide more detailed evidence supporting the validity of our parallel trends assumption. We estimate the following specification to test, week by week, whether the numbers of visits to piracy websites of Kino and

Evolution of online movie streaming piracy

Figure 1. (Color online) Evolution of Online Movie Streaming Piracy  
![](/api/attachments/5H6GM42H/fulltext/images/b92b59e3b37d6953fcf6fbfa0b871ced564c7e8fdc2b9d4f16f6b2cc775220ad.jpg)  
Notes. The vertical axis shows the average log weekly clicks per user. The horizontal axis shows calendar weeks in 2011. Solid blue line, average log weekly clicks per user on all unlicensed streaming websites; dashed red line, average log weekly clicks per user on kino.to.

non-Kino users difer from the number of visits to piracy websites of international users:

$$
\begin{array}{c} \ln (C l i c k s _ {i t} + 1) = \alpha + \sum_ {t} \beta_ {0} ^ {t} w _ {t} + \sum_ {t} \beta_ {1} ^ {t} (w _ {t} \times K i n o _ {i}) \\ + \sum_ {t} \beta_ {2} ^ {t} (w _ {t} \times N o n - K i n o) + \mu_ {i} + \varepsilon_ {i t}. \end{array}\tag{2}
$$

We define the week before the shutdown as the omitted reference week. Testing that $\beta _ { 1 } ^ { t } = 0$ and $\beta _ { 2 } ^ { t } = 0$ (no diference between treatment group users and international users) for all t in the preshutdown period therefore provides a more direct test of the parallel trends assumption. Estimates of $\beta _ { 1 } ^ { t }$ and $\beta _ { 2 } ^ { t }$ for all $t ,$ along with 90% confidence bands, are reported in Figure 3. Overall, most of the preshutdown coeficients appear to be statistically indistinguishable from zero prior to the intervention, and we do not observe a systematic trend.<sup>22</sup>

Figure 2. (Color online) Evolution of Online Movie Streaming Piracy, by Group  
![](/api/attachments/5H6GM42H/fulltext/images/4dc0d484eb09b698afc34d3a55b545accbdde101a80395e1ce6f78523f10b68b.jpg)  
Notes. The vertical axis shows the average log weekly clicks per group. The horizontal axis shows calendar weeks in 2011. Solid blue line, Kino users; dashed blue line, non-Kino users; solid red line, international users (control group).

4.1.2. Econometric Evidence. We now turn to the results of estimating Equation (1). Those baseline results are reported in column (1) of Table 3. The estimate for the average efect of the intervention on Kino users is significant and equal to <sup>−</sup>0.317 (SE <sup></sup> 0.033), indicating that the intervention was successful in reducing piracy consumption levels by $2 7 . 2 \% . ^ { 2 3 }$ If we put these results in relation to the average 79% market share of kino.to in the preshutdown period, the decline is much smaller than what we would expect if consumers did not switch to alternative piracy websites. Instead of only distinguishing between two time periods (before and after the shutdown) with the ${ \mathbf { } } A f t e r _ { t }$ interactions in Equation (1), we can also look at the postshutdown coeficients from the regression of Equation (2) in Figure 3. Confirming what we already saw in the descriptive statistics, we find the strongest decline in piracy levels for Kino users in the first five weeks after the shutdown, with some uptake afterward. This result indicates that the existence of alternative unlicensed platforms challenged the efectiveness of kino.to’s shutdown in deterring consumers from online piracy.

Figure 3. (Color online) Group Diference: Overall Piracy  
![](/api/attachments/5H6GM42H/fulltext/images/8e9d95b9de673e6445d543e0b86bdca918e3ea804004e825deb01dc850d9e208.jpg)

![](/api/attachments/5H6GM42H/fulltext/images/086d5ae11c604a6ba596a5db8180c2b2c446f052b4411a1403e76b2601c495fb.jpg)  
Notes. The vertical axis shows OLS coeficients. The horizontal axis shows Calendar weeks in 2011. Weekly diferences between the treatment group (Kino/Non-Kino) and the control group (users in France, Italy, and the United Kingdom) are shown. Solid blue circles show OLS estimates of the $\beta _ { 1 } ^ { t } w _ { t }$ (left panel) and $\beta _ { 2 } ^ { t } \bar { w } _ { t }$ (right panel) coeficients obtained from a regression of $\begin{array} { r } { \ln ( C l i c k s _ { i t } + 1 ) = \alpha + \sum _ { t } \beta _ { 0 } ^ { t } w _ { t } + \sum _ { t } \beta _ { 1 } ^ { t } ( w _ { t } \times } \end{array}$ Kino <sup>) +</sup> P β<sup>t (</sup>w <sup>×</sup> Non-Kino<sup>)</sup> $+ \mu _ { i } + \varepsilon _ { i t } ,$ . Bars indicate 90% confidence bands.

The estimated coeficient on the After <sup>×</sup> Non-Kino variable in column (1) of Table 3 is positive and significant at the 10% level.<sup>24</sup> This indicates that shutting down kino.to did not only afect Kino users directly but also individuals that never visited kino.to. On average, those individuals increase their visits to piracy websites by 0.8%. Estimates for the postshutdown period from the flexible form regression in Equation (2), reported in Figure 3, show how the efect of the shutdown changed over time. We find that the efects on non-Kino users did not immediately materialize, but became pronounced following the first five weeks after the shutdown. Note that this timing is symmetric to the timing of the increase in piracy usage we find for Kino users.

Before exploring the mechanism behind this externality in more detail, we report results of various additional specifications that provide further support to our identification strategy and address concerns regarding a potential measurement error in the dependent variable.

As a first robustness check, we construct an alternative control group by means of a propensity score matching based on observables, that is, gender, age, income, education, and overall news consumption. For each individual in the treatment group, we find a control individual using one-to-one matching without replacement. Following Lechner (2002), we use binary probit models to estimate propensity scores for the two treatment groups, Kino users and non-Kino users. The results in column (2) are similar to those results obtained with the control group of international users in column (1) of Table 3.

As a second robustness check, we consider three alternative measures of piracy. We first proxy for the number of streams of unlicensed content by measuring subsequent visits to cyberlockers. A second alternative measure involves the weekly number of days an individual visited websites ofering unlicensed content. The third proxy measures the weekly duration spent on piracy websites. Results are reported in columns (3)–(5) of Table 3 and are in line with our preferred specification. This alleviates the concern that our baseline results could be driven by measurement error, for example, that is caused by diferences in the design of alternative piracy websites that would make more clicks necessary to search for and consume content compared to kino.to.

Table 3. Piracy, Baseline Results, and Robustness Checks

<table><tr><td></td><td>(1) Piracy Coef. (SE)</td><td>(2) PSM Coef. (SE)</td><td>(3) Streams Coef. (SE)</td><td>(4) Days Coef. (SE)</td><td>(5) Duration Coef. (SE)</td><td>(6) Outliers Coef. (SE)</td></tr><tr><td>After × Kino</td><td>-0.317***(0.033)</td><td>-0.296***(0.034)</td><td>-0.161***(0.017)</td><td>-0.119***(0.013)</td><td>-0.546***(0.058)</td><td>-0.321***(0.028)</td></tr><tr><td>After × Non-Kino</td><td>0.008*(0.005)</td><td>0.012*(0.007)</td><td>0.003*(0.002)</td><td>0.003*(0.002)</td><td>0.029***(0.009)</td><td>0.008***(0.003)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.456</td><td>0.453</td><td>0.365</td><td>0.477</td><td>0.432</td><td>0.290</td></tr><tr><td>No. of ind.</td><td>20,000</td><td>9,017</td><td>20,000</td><td>20,000</td><td>20,000</td><td>19,808</td></tr><tr><td>No. of obs.</td><td>1,040,000</td><td>468,884</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,021,649</td></tr></table>

Notes. Standard errors are in parentheses and clustered at the individual level. All specifications include individual fixed efects, week fixed efects, and linear group-specific trends.  
<sup>∗</sup>Significant at the 10% level; <sup>∗∗∗</sup>significant at the 1% level.

Finally, because of the dispersed distribution of the dependent variable, a concern could be that our results are driven by outliers. We check the robustness of our results to outliers by dropping observations with the 1% smallest and largest residuals and 1% smallest and largest predicted values after running the baseline regression. Rerunning the regression on this new sample generates the results presented in column (6), which remain similar to those in column (1).

## 4.2. Externalities from News Coverage

Our results indicate that non-Kino users increased their consumption of unlicensed content following the intervention. We now test whether the media coverage surrounding the shutdown of kino.to can explain these unintended externalities.

Using visits to URLs of news articles and blog posts that cover and follow up on the shutdown of kino.to, we define the dummy variable News equal to one starting in the week where we observe the individual’s first visit to one of those URLs. To test whether the shutdown efect varies conditional on reading news about kino.to, we add the following interactions to our baseline model in Equation (1): $A f t e r _ { t } \times K i n o _ { i } \times$ News<sub>it</sub> and After <sup>×</sup> Non-Kino<sub>i</sub> <sup>×</sup> News<sub>it</sub>.<sup>25</sup>

The results are reported in Table 4.<sup>26</sup> To ease comparison with our baseline results, column (1) of Table 3 is included in the first column of the table. Column (2) reports estimates of the augmented model with threeway interaction terms comparing users that have read news about kino.to to those that did not. While there is no significant diference for Kino users, we observe a large and significant diference for non-Kino users: their consumption of pirated consumption increases 35% more than the insignificant baseline increase of 0.5%. We observe 100 non-Kino users that read news, which represents 2.4% of the total number of non-Kino users, and 11.9% of the total number of Kino users, making this an efect of substantial economic significance.

In column (3), we further distinguish the content of the news articles to identify possible mechanisms. As before, we do not find any significant diference within Kino users. For non-Kino users, we see that the strong positive efect of reading about the shutdown on piracy consumption is driven mainly by reading news articles that conclude that using streaming services would not lead to legal consequences for consumers, but also by reading news articles that mention unlicensed alternatives to kino.to. As expected, the efect of reading articles that conclude that using unlicensed streaming sites would be illegal is negative, yet not significant (p-value 0.104).

Table 4. Piracy, Externalities

<table><tr><td></td><td>(1) Coef. (SE)</td><td>(2) Coef. (SE)</td><td>(3) Coef. (SE)</td></tr><tr><td>After  $\times$  Kino</td><td>-0.317***(0.033)</td><td>-0.317***(0.033)</td><td>-0.318***(0.033)</td></tr><tr><td>After  $\times$  Non-Kino</td><td>0.008*(0.005)</td><td>0.005(0.005)</td><td>0.007(0.005)</td></tr><tr><td>After  $\times$  Kino  $\times$  News</td><td></td><td>-0.013(0.203)</td><td></td></tr><tr><td>After  $\times$  Non-Kino  $\times$  News</td><td></td><td>0.300***(0.107)</td><td></td></tr><tr><td>After  $\times$  Kino  $\times$  News:Background</td><td></td><td></td><td>-0.054(0.181)</td></tr><tr><td>After  $\times$  Kino  $\times$  News:Alternatives</td><td></td><td></td><td>0.084(0.165)</td></tr><tr><td>After  $\times$  Kino  $\times$  News:Legal</td><td></td><td></td><td>-0.095(0.209)</td></tr><tr><td>After  $\times$  Kino  $\times$  News:Illegal</td><td></td><td></td><td>0.205(0.218)</td></tr><tr><td>After  $\times$  Non-Kino $\times$  News:Background</td><td></td><td></td><td>0.004(0.064)</td></tr><tr><td>After  $\times$  Non-Kino $\times$  News:Alternatives</td><td></td><td></td><td>0.163*(0.086)</td></tr><tr><td>After  $\times$  Non-Kino  $\times$  News: Legal</td><td></td><td></td><td>0.283**(0.115)</td></tr><tr><td>After  $\times$  Non-Kino  $\times$  News: Illegal</td><td></td><td></td><td>-0.185(0.114)</td></tr><tr><td>Adjusted  $R^{2}$ </td><td>0.456</td><td>0.456</td><td>0.457</td></tr><tr><td>No. of ind.</td><td>20,000</td><td>20,000</td><td>20,000</td></tr><tr><td>No. of obs.</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td></tr></table>

Notes. Standard errors are in parentheses and clustered at the individual level. All specifications include individual fixed efects, week fixed efects, and linear group-specific trends.  
<sup>∗</sup>Significant at the 10% level; <sup>∗∗</sup>significant at the 5% level; <sup>∗∗∗</sup>significant at the 1% level.

## 4.3. Efects on Licensed Video Consumption

While we have shown that shutting down kino.to led to a decrease in overall piracy levels, it could only have benefited content creators and copyright holders if consumption of licensed content also increased as a result of the intervention. We analyze the efects of the shutdown on licensed video consumption proxied by clicks on movie theater websites, licensed video streaming services, and DVD/Blu-ray pages on Amazon.

The identifying assumption here is that clicks to licensed content of treatment and control groups would have followed similar trends had the shutdown not occurred. We can partially test this assumption by looking at cross-group diferences in trends prior to the intervention. Figures 4–6 plot the interactions of week dummies and user type from a regression of Equation $( 2 ) . ^ { 2 7 }$

Figure 4. (Color online) Group Diference: Cinema  
![](/api/attachments/5H6GM42H/fulltext/images/0667d4e80e1853a27587d1017706ae46248038de3f670fc34d753868219bfc5a.jpg)

![](/api/attachments/5H6GM42H/fulltext/images/f1b2d9c9999223d1267cd83a391a50a183b837013976a2c72a3c39f99d7d7115.jpg)  
Notes. The vertical axis shows OLS coeficients. The horizontal axis shows calendar weeks in 2011. Weekly diferences between the treatment group (Kino/Non-Kino) and the control group (users in France, Italy, and the United Kingdom) are shown. Solid blue circles show OLS estimates of the $\beta _ { 1 } ^ { t } w _ { t }$ (left panel) and $\beta _ { 2 } ^ { t } w _ { t }$ (right panel) coeficients obtained from a regression of $\begin{array} { r } { \ln ( C l i c k s _ { i t } + 1 ) = \alpha + \sum _ { t } \beta _ { 0 } ^ { t } w _ { t } + \sum _ { t } \beta _ { 1 } ^ { t } ( w _ { t } \times } \end{array}$ Kino<sub>i</sub><sup>) +</sup> P<sub>t</sub> β<sup>t (</sup>w<sub>t</sub> <sup>×</sup> Non-Kino<sup>)</sup> $+ \mu _ { i } + \varepsilon _ { i t }$ . Bars indicate 90% confidence bands.

The results are reported in Table $5 . ^ { 2 8 }$ Columns (1), (3), and (5) report the overall efects on Kino and non-Kino users. These specifications present no evidence of Kino users substituting into any of the licensed alternatives. For non-Kino users, we observe a slight reduction in paid licensed streaming services of 0.6%.

When we include the News interactions in columns (2), (4), and (6), we get positive and significant coefficients for the News interactions regarding visits to cinema websites. The News interactions are significant for both the Kino and non-Kino users, suggesting that both groups increase their visits to movie theaters after they read news about the shutdown. The decrease in consuming streamed licensed content for non-Kino users that we observed for the overall efects is not significantly moderated by reading news about the shutdown.

Figure 5. (Color online) Group Diference: Online  
![](/api/attachments/5H6GM42H/fulltext/images/95197c8c3de12d6f9cde328f6c75d1c23c3f51d22b410c35c81373bc1b8e9322.jpg)

## 4.4. Efects on Diferent Levels of Aggregation

We now assess the efect of the shutdown on alternative levels of aggregation. Speculating beyond what our analysis allows us to show in a causal manner, we first provide suggestive evidence that indirect efects and externalities are driven by the amount of knowledge individuals have about unlicensed alternatives. We then run a country-level analysis to assess the overall efect and speculate about the size of welfare efects.

![](/api/attachments/5H6GM42H/fulltext/images/011d2e65c21b173f03a84b67f6db511a06126c00f341939bbfd7066e986452b2.jpg)  
Notes. The vertical axis shows OLS coeficients. The horizontal axis shows calendar weeks in 2011. Weekly diferences between the treatment group (Kino/Non-Kino) and the control group (users in France, Italy, and the United Kingdom) are shown. Solid blue circles show OLS estimates of the $\beta _ { 1 } ^ { t } w _ { t }$ (left panel) and $\beta _ { 2 } ^ { t } w _ { t }$ (right panel) coeficients obtained from a regression of $\begin{array} { r } { \ln ( C l i c k s _ { i t } + 1 ) = \alpha + \sum _ { t } \beta _ { 0 } ^ { t } w _ { t } + \sum _ { t } \beta _ { 1 } ^ { t } ( w _ { t } \times } \end{array}$ Kino <sup>) +</sup> P β<sup>t (</sup>w <sup>×</sup> Non-Kino<sup>) +</sup> $\mu _ { i } + \varepsilon _ { i t } .$ . Bars indicate 90% confidence bands.

Figure 6. (Color online) Group Diference: DVD  
![](/api/attachments/5H6GM42H/fulltext/images/27c29ca30edc03f0832484958b35fd0b8b58d96b3cd8d59e2f115df4f340f1f0.jpg)

![](/api/attachments/5H6GM42H/fulltext/images/d83cc100b3847ddd415aeeae95ac896736f8127c0b4a2c004699677419136fb2.jpg)  
Notes. The vertical axis shows OLS coeficients. The horizontal axis shows calendar weeks in 2011. Weekly diferences between the treatment group (Kino/Non-Kino) and the control group (users in France, Italy, and the United Kingdom) are shown. Solid blue circles show OLS estimates of the $\beta _ { 1 } ^ { t } w _ { t }$ (left panel) and $\beta _ { 2 } ^ { t } w _ { t }$ (right panel) coeficients obtained from a regression of l $\begin{array} { r } { \iota ( C l i c k s _ { i t } + 1 ) = \alpha + \sum _ { t } \beta _ { 0 } ^ { t } w _ { t } + \sum _ { t } \beta _ { 1 } ^ { t } ( w _ { t } \times } \end{array}$ Kino <sup>) +</sup> P β<sup>t (</sup>w <sup>×</sup> Non-Kino<sup>)</sup> $\overline { { \mathbf { \nabla } } } \mu _ { i } + \boldsymbol { \varepsilon } _ { i t }$ . Bars indicate 90% confidence bands.

4.4.1. The Efect of Knowing About Unlicensed Alternatives. Our definition of Kino users includes users that visit only kino.to and no other unlicensed video streaming website (Kino: Single Homing, 57%) and users that visit kino.to along with other services (Kino: Multihoming, 43%). Similarly, our definition of non-Kino users includes users that did visit other piracy websites before the shutdown (Non-Kino: Pirate, 6%) as well as those that did not visit any piracy websites before the shutdown (Non-Kino: Nonpirate, 94%). We split each of the two treatment groups into two subgroups to get a more nuanced view of how existing knowledge about other piracy sites could influence the reaction to the shutdown.<sup>29</sup> Knowing about unlicensed alternatives could play out in two ways. First, because Kino multihomers already knew about alternative unlicensed video streaming websites before the removal of kino.to, they should perhaps find it easier to switch to those websites (Chen and Hitt 2002; Goldfarb 2006a, b). Second, because non-Kino pirates were already exclusively using alternative platforms before the shutdown of kino.to, we should not expect their usage of alternative piracy websites to be afected by the intervention.

Table 5. Licensed Alternatives

<table><tr><td></td><td>(1) Cinema Coef. (SE)</td><td>(2) Cinema Coef. (SE)</td><td>(3) Online Coef. (SE)</td><td>(4) Online Coef. (SE)</td><td>(5) DVD Coef. (SE)</td><td>(6) DVD Coef. (SE)</td></tr><tr><td>After × Kino</td><td>0.004(0.010)</td><td>-0.004(0.010)</td><td>0.012(0.009)</td><td>0.014(0.009)</td><td>-0.002(0.008)</td><td>-0.002(0.008)</td></tr><tr><td>After × Non-Kino</td><td>0.005(0.004)</td><td>0.004(0.004)</td><td>-0.006**(0.003)</td><td>-0.005*(0.003)</td><td>-0.004(0.003)</td><td>-0.004(0.003)</td></tr><tr><td>After × Kino × News</td><td></td><td>0.134**(0.059)</td><td></td><td>-0.043(0.049)</td><td></td><td>0.006(0.057)</td></tr><tr><td>After × Non-Kino × News</td><td></td><td>0.123**(0.056)</td><td></td><td>-0.045(0.071)</td><td></td><td>-0.038(0.057)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.284</td><td>0.284</td><td>0.261</td><td>0.261</td><td>0.316</td><td>0.316</td></tr><tr><td>No. of ind.</td><td>20,000</td><td>20,000</td><td>20,000</td><td>20,000</td><td>20,000</td><td>20,000</td></tr><tr><td>No. of obs.</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td></tr></table>

Notes. Standard errors are in parentheses and clustered at the individual level. All specifications include individual fixed efects, week fixed efects, and linear group-specific trends.  
<sup>∗</sup>Significant at the 10% level; <sup>∗∗</sup>significant at the 5% level.

Table 6. Knowing About Unlicensed Alternatives

<table><tr><td></td><td>(1) Alt. Piracy Coef. (SE)</td><td>(2) Cinema Coef. (SE)</td><td>(3) Online Coef. (SE)</td><td>(4) DVD Coef. (SE)</td></tr><tr><td>After × Kino:Single Homing</td><td>0.215***(0.028)</td><td>0.026**(0.012)</td><td>0.015(0.011)</td><td>-0.003(0.010)</td></tr><tr><td>After × Kino:Multihoming</td><td>0.395***(0.060)</td><td>-0.026(0.018)</td><td>0.009(0.013)</td><td>0.001(0.013)</td></tr><tr><td>After × Non-Kino:Pirate</td><td>0.000(0.041)</td><td>0.007(0.018)</td><td>-0.020(0.014)</td><td>-0.004(0.017)</td></tr><tr><td>After × Non-Kino:Nonpirate</td><td>0.009**(0.004)</td><td>0.005(0.003)</td><td>-0.005*(0.003)</td><td>-0.004(0.003)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.430</td><td>0.284</td><td>0.261</td><td>0.316</td></tr><tr><td>No. of ind.</td><td>20,000</td><td>20,000</td><td>20,000</td><td>20,000</td></tr><tr><td>No. of obs.</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td></tr></table>

Notes. Standard errors are in parentheses and clustered at the individual level. All specifications include individual fixed efects, week fixed efects, and linear group-specific trends.  
<sup>∗</sup>Significant at the 10% level; <sup>∗∗</sup>significant at the 5% level; <sup>∗∗∗</sup>significant at the 1% level.

We estimate our diference-in-diferences model using visits to alternative unlicensed video streaming websites (i.e., visits to all unlicensed streaming websites except kino.to) as well as visits to licensed video consumption as the dependent variable. Results are presented in Table 6. Column (1) shows that Kino users that visited alternative piracy websites before (multihomers) increase their visits to those sites more than single homers. Additionally, we observe no significant efect for the non-Kino users that visited alternative piracy websites before the shutdown (Non-Kino: Pirate). Taken together, these results provide evidence that prior knowledge about unlicensed alternatives triggers switching, not an unobserved trend that makes those sites more attractive per se. The efect for users that never visited piracy websites is positive and significant. This provides some additional evidence of unintended externalities and supports the results discussed above.

Regarding licensed consumption, we first find that single-homing Kino users increase their visits to movie theater websites in column (2). The efect size is 2.6%. This suggests that the intervention was somewhat efective in convincing some individuals to substitute toward licensed oferings. Intuitively, it makes sense to see this uptake only for single-homing users since they do not readily know about alternative unlicensed websites. Regarding licensed online video content in column (3), we observe no efect for Kino users and find that users that never pirated before the shutdown decrease their clicks to licensed oferings. This provides further supporting evidence for our main results. The unintended externalities only afect users that never pirated before the shutdown. Finally, we do not observe any efects when it comes to visiting DVD/Blu-Ray pages on Amazon in column (4).

4.4.2. The Aggregate Efect and Implications for Welfare. A necessary condition for the enforcement effort to be welfare enhancing—net of any enforcement costs—is that the resulting producer surplus exceeds the reduction in consumer surplus that results from lower piracy levels. To speculate about the welfare implications of the shutdown of kino.to, we assess the aggregate efect of the intervention by combining Kino users and non-Kino users into a single treatment group, labeled Germany. The results of this analysis are presented in Table 7. Compared to France, Italy, and the United Kingdom, we find an overall reduction in piracy levels in the German market of 4.5%, but do not observe any significant changes in any type of licensed consumption. We conclude that the shutdown reduced overall welfare as consumer surplus was reduced and there is no evidence of an uptake in licensed consumption.<sup>30</sup>

We try to quantify the welfare loss in a back-of-theenvelope calculation. A 4.5% decrease in clicks to piracy sites is equivalent to 0.17 streams per capita (using our Piracy Streams measure). Based on estimates of sales displacement rates in the literature (Hui and Png 2003; Rob and Waldfogel 2006, 2007; Bai and Waldfogel 2012; Danaher et al. 2010), we can assume that the monetary equivalent of the utility of streaming a movie via an unlicensed website is somewhere between 3.5%–20% of the price of the licensed version. The average price on iTunes in Germany is e3.00 for rentals and e7.99 for purchases, the average movie ticket price in 2011 in Germany is e7.39, and the average price of DVDs and Blu-rays at Amazon is e16.57.<sup>31</sup> Let us consider one scenario where consumers displace sales at the lowest displacement rate and always prefer the cheapest option (iTunes rentals), and another scenario where consumers have the highest displacement rate and prefer the most expensive option (DVD/Bluray). The resulting estimate of per-capita change in consumer surplus is in the range of 2–56¢.<sup>32</sup> Using census and data for the number of Internet users in Germany from the International Telecommunications Unit (65.21 million in 2011), our estimate of the total loss in consumer surplus (and therefore overall welfare) is somewhere between e1.16 million and e36.74 million per week.<sup>33</sup>

Table 7. Aggregate Analysis

<table><tr><td></td><td>(1) Piracy Coef. (SE)</td><td>(2) Cinema Coef. (SE)</td><td>(3) Online Coef. (SE)</td><td>(4) DVD Coef. (SE)</td></tr><tr><td>After × Germany</td><td>-0.046***(0.007)</td><td>0.005(0.004)</td><td>-0.003(0.003)</td><td>-0.004(0.003)</td></tr><tr><td>Adjusted  $R^2$ </td><td>0.455</td><td>0.284</td><td>0.261</td><td>0.316</td></tr><tr><td>No. of ind.</td><td>20,000</td><td>20,000</td><td>20,000</td><td>20,000</td></tr><tr><td>No. of obs.</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td><td>1,040,000</td></tr></table>

Notes. Standard errors are in parentheses and clustered at the individual level. All specifications include individual fixed efects, week fixed efects, and linear group-specific trends.  
<sup>∗∗∗</sup>Significant at the 1% level.

## 4.5. Postshutdown Market Structure

We now turn to the analysis of the overall structure of the market for unlicensed video streaming following the shutdown of kino.to. The raid on June 8, 2011, involved the seizure of servers, databases of the linking site itself, and integrated cyberlocker services. However, the shutdown resulted in a shock to only part of the whole piracy ecosystem. Because content hosted on other cyberlockers remained online, it was relatively easy for existing competitors or even new entrants to supply similar content as the one initially ofered by kino.to. Shutting down the major platform may therefore simply result in some existing or new website capturing most of the market. However, it is a priori not clear whether a new dominant platform would emerge to take kino.to’s place, or if a more fragmented market should be expected as a result of the intervention.

We look at the evolution of unlicensed platforms’ weekly market shares to assess how the streaming piracy market was afected by the shutdown of kino.to. Figure 7 presents the evolution of market shares for the diferent platforms defining our market, distinguishing between kino.to, kinoX.to, movie2k.to, and the 17 remaining websites included in our market definition. The figure shows remarkable changes in the structure of the streaming piracy market after the intervention. Before the shutdown, kino.to (dashed blue line) clearly dominated the market with an average market share of about 80%. The second largest player, movie2k.to, had a market share of about 10%, and the remaining websites jointly accounted for an average market share of 10%. During the first four weeks after the intervention, movie2k.to’s market share increased to about 55%, and the market share of all other streaming sites increased to about 45%. After four weeks, kinoX.to entered and immediately gained a 20% market share, while movie2k.to’s market share decreased to about 30%.<sup>34</sup> Eight weeks after the shutdown, the market shares changed to about one-third each.

Figure 7. (Color online) Market Shares of Unlicensed Video Streaming Websites  
Evolution of market shares of illegal movie streaming websites  
![](/api/attachments/5H6GM42H/fulltext/images/bcb288c31b721b7eb452864968ecac5579e9d7846606998ac33fc7330bc060e4.jpg)  
Notes. The vertical axis shows weekly market share. The horizontal axis shows calendar weeks in 2011. Dashed blue line, weekly market share of kino.to; solid red line, weekly market share of movie2k.to; dashed green line, weekly market share of kinox.to; dotted orange line, weekly market share of all other unlicensed streaming websites.

Figure 8. (Color online) Concentration in the Unlicensed Video Streaming Market  
Concentration in the unlicensed video streaming market  
![](/api/attachments/5H6GM42H/fulltext/images/14dcb497de34b28b0227b0ec1d8cb69547a9efeba35d044d3f08c6bb17465e10.jpg)  
Notes. The vertical axis shows the weekly HHI in Germany. The horizontal axis shows calendar weeks in 2011.

The changes in market shares imply changes in market concentration. Figure 8 shows the weekly evolution of the Herfindahl–Hirschman Index (HHI) of the unlicensed video streaming market.<sup>35</sup> This adds additional insights since we do not aggregate the “long tail” of websites in the HHI measure. Before the shutdown of kino.to, the HHI was around 6,500. It decreased sharply to 2,500 during the week of the shutdown, but immediately increased to about 3,500 after two weeks. After four weeks, and following the entry of kinoX.to, the HHI decreased again sharply to about 2,000, where it remained for six weeks before increasing slightly to about 3,000 at the end of the year.

While the shutdown of kino.to had important effects on the market structure of the German piracy market, it is important to note that these efects are also likely to be context-specific. One should therefore interpret and generalize our results with caution. First, we only observe six months of data after the shutdown of kino.to and therefore cannot test whether the observed market structure will remain stable in the long run. For instance, it is possible for one of the remaining platforms to increase its market share to the point of having a market structure similar to the one preceding the intervention. Second, marketspecific characteristics could influence the impact of the shutdown on the structure of the piracy market.<sup>36</sup>

We note that these changes in market structure, while context specific, can have important policy implications. In the case of the German market for unlicensed video streaming, our results suggest that the shutdown of kino.to made future interventions potentially more costly—as there would not be a single dominant platform to shutdown anymore—and potentially less efective if only a single website is targeted by the intervention.

## 5. Discussion

The robustness checks detailed above helped to address concerns regarding the internal validity of our findings, by discussing the choice of measures and control group. External validity of our results may nevertheless remain a concern. While our analysis provides insightful results, it is essentially a case study, with certain limits to generalizability. In particular, one may wonder whether similar results could be expected from a similar enforcement carried out in a diferent country or at a diferent point in time. Guided by the literature on threats to external validity in quasi-experimental research (Cook and Campbell 1979, Howell 2005) and the available evidence, we carefully discuss the boundaries of our research regarding its geographic, institutional, and historical contexts. Finally, we discuss alternative private and public enforcement policies and their potential to reduce piracy levels and increase licensed consumption.

## 5.1. External Validity Regarding Geography

A first concern is related to a potential interaction of setting and treatment, that is, that the efect may difer across institutional and geographic settings.

How Representative Are German Consumers? Evidence suggests that cross-country diferences in piracy rates can be explained by the strength of enforcement and aggregate demographics such as income and education (van Kranenburg and Hogenbirk 2005, Proserpio et al. 2005, Walls 2008). Reflecting such differences, the piracy rate in Germany in 2011 was lower than in other European countries, but higher than in the United States.<sup>37</sup> However, the per-capita propensity to pirate alone is not enough to draw conclusions about potential cross-country diferences regarding the displacement of licensed content. Although willingness to pay is clearly correlated with intentions to pirate (see the extensive review in Watson et al. 2015), we are not aware of systematic evidence showing that the willingness to pay for licensed content varies across countries.

How Representative is the German Market for Unlicensed Video Streaming? A concern could be that our results crucially depend on the structure of the piracy market and the relative quality of diferent unlicensed streaming options. Consider a scenario where, after the shutdown of a high-appeal website, consumers can access only low-appeal alternatives. Licensed options may consequently gain in relative attractiveness. Evidence suggests that such a scenario is probably not very realistic. Lauinger et al. (2013) show that it is fairly easy to replicate the content of a linking site, because the underlying video files are stored elsewhere, and multiple copies exist.<sup>38</sup> As a consequence, what we document in the German case—that other websites (including new entrants) quickly gain trafic— is likely to happen in other markets as well. Anecdotal evidence from recent examples is consistent with this idea. Within a few weeks following the shutdown of the hugely popular unlicensed sites kat.cr (global Alexa rank 69) and zone-telechargement.com (French Alexa rank 11) by legal authorities in late 2016, multiple new platforms entered the market (Protalinski 2016, Tual 2016). In general, Germany is no exception when it comes to antipiracy interventions. A number of other countries have introduced policies targeted at consumers and suppliers of unlicensed content, some of which are thoroughly documented in the literature (Danaher et al. 2014, Adermon and Liang 2014, Danaher and Smith 2014, Poort et al. 2014, Peukert et al. 2017, McKenzie 2017).

How Representative is the German Market for Licensed Video Consumption? A growing literature shows that availability of licensed content can reduce piracy (Danaher et al. 2010, 2013; Aguiar and Waldfogel 2018). Accordingly, a potential explanation for why we do not observe more substitution toward licensed consumption may be found in the relative quality of licensed online alternatives in the German market in 2011 (Poort and Weda 2015).<sup>39</sup> Compared to other (European)

countries, there is not much reason to believe that Germany is an exception when it comes to the availability and attractiveness of licensed content, either online or ofline. To date, in 2017, Apple does not ofer movies in 45 (24%) and TV shows in 149 (79%) of 189 markets where they operate an iTunes Store.<sup>40</sup> Data from 2013 suggest that the vast majority of movies in a countryspecific iTunes Store in Europe are available in only one language (Gomez-Herrera and Martens 2015). The streaming service Netflix had not started to roll out in Europe before 2012, arriving in Germany and France in 2014 and in Italy in 2015.

In addition, it also seems that prices of licensed oferings in Germany were not much diferent compared to other countries. Gomez-Herrera and Martens (2015) show that cross-country price diferences of digital content can be largely explained by overall price levels, which is essentially the same regarding cinema ticket prices.<sup>41</sup> Finally, in a study that looks at an entirely different experiment, analyzing very diferent data from the United States, Danaher et al. (2010) arrive at results very similar to ours. After the removal of content on iTunes, piracy rates for the same content increased, yet there was no efect on sales of respective DVDs at Amazon.

## 5.2. External Validity Regarding History

We now discuss the potential concern that the efects identified in our analysis may difer across time periods.

How Will Digital Piracy and Licensed Oferings Change? According to a joint report of the music and advertising industry in 2012, infringing websites are predominately financed by advertising or subscription models.<sup>42</sup> Hence, as long as there is demand for unlicensed content that can be monetized, the incentives to operate large-scale piracy websites are likely to remain strong. An emerging literature suggests that the appeal of piracy may decrease over time, mainly because of improvements in licensed alternatives. Theoretical work shows that content services where consumers can choose between fee-based or free and adsupported subscriptions (a model that is mostly ofered in the music market, much less so in the video market) can reduce the demand for piracy (Thomes 2013). Recent evidence in Aguiar and Waldfogel (2018) suggests that the licensed streaming platform Spotify— which operates a freemium business model—has had a negative and significant impact on recorded music piracy. Data from the Netherlands in Poort and Weda (2015) show that piracy levels of music declined from 35% to 23% between 2008 and 2012, while piracy levels of video content increased from 11% to 18% during the same time period. Relying on survey data, the authors conclude that this diference can be explained by diferences in how consumers perceive the availability and price of licensed music versus video ofers. The idea that consumers do not switch to licensed platforms because their preferred content is not available can be partly tested with our data. Looking at the URLs of visited pages on kino.to, we see whether users were watching movies or TV shows. This allows us to categorize users based on their content preferences. Distinguishing between the efects of the shutdown on users who mainly watched TV series on kino.to and users who mainly watched movies shows that the former group reacted to the shutdown to a larger extent. Usage of alternative piracy websites is similar for both types of users before the shutdown, and increased 50% more for users that mainly watched TV shows thereafter.<sup>43</sup> This suggests that it is mainly a preference for TV shows that convinces consumers to switch to alternative websites. An implication could be that firms might be able to strategically react to diferences in user preferences and ofer specialized products. However— in line with the results above—we do not find evidence that either type of Kino user increases visits to licensed video streaming services.

In conclusion, if the availability and pricing of licensed oferings become more attractive, it is likely that more consumers will switch to licensed oferings.<sup>44</sup> Yet, according to anecdotal evidence, the most significant changes toward full digital availability of movies are yet to come—more than five years after the enforcement efort we study. Recent news reports suggest that movie studios are negotiating with cinema owners about reducing the window between theatrical release and video on demand in exchange for a share of streaming revenues (Lang 2017). Reportedly, movies would become available for streaming three weekends after the theatrical release at a price of \$30–\$50 per movie.

## 5.3. Alternative Policy Levers

Based on suggestive evidence and established results in the literature, we conclude that the efects we document are not very likely to difer across institutional and geographic settings. However, we have reasons to speculate that our findings are specific to the historical timing of the shutdown. Better availability and lower prices of licensed consumption options introduced in recent years could help to convince more consumers to use legitimate oferings if further developed. Looking ahead, we discuss whether alternative policy levers could be more efective.

Public Enforcement. There are reasons to expect stronger efects from greater enforcement eforts on the supply side. In the model of Dey et al. (2016), stronger supply-side enforcement leads to higher entry costs for unlicensed websites, which in turn reduces the content available for consumers. The authors show that supply-side enforcement can lead to desirable welfare outcomes (which is similar to the result in Tsai and Chiou 2012). In light of this model, an interpretation of our results could be that the enforcement intensity was not high enough, in particular, because the intervention afected only one unlicensed website. The implication could be that shutting down multiple websites at a time would be more efective at decreasing piracy levels and increasing welfare.<sup>45</sup> Nevertheless, from a practical perspective, achieving a level of enforcement that is suficiently broad to be sustainable in the long run seems very dificult. For example, evidence shows that the rate of new cyberlockers entering the market increased after the shutdown of Megaupload (Lauinger et al. 2013), and consumers use virtual private network (VPN) services to circumvent the blocking of the Pirate Bay and a number of similar websites (Danaher et al. 2015a). Putting aside country-specific legal issues—which may make a largescale international raid dificult—the associated costs of physically raiding multiple websites hosted on geographically dispersed servers would also have to be taken into account. This could naturally reduce the welfare-enhancing efect of supply-side enforcement (Tsai and Chiou 2012, Dey et al. 2016). A relatively recent regulatory approach is to reduce the advertising revenues that piracy websites receive. Initiatives toward a self-regulation of the online advertising industry have been implemented in 2013 in the United Kingdom and are on the agenda of the European Commission since 2015.<sup>46</sup> Although economically appealing, except for a recent paper by Batikas et al. (2017), we are not aware of any academic literature that provides evidence on the overall efectiveness of such eforts.

Taxes and Subsidies. Theoretical work by Becker et al. (2006), using a model that is applied to illegal drugs, shows that a tax on legalized production is better able to reduce the quantity of drugs in the market than quantity-restricting enforcement eforts. This is in line with what Chen and Png (2003) find in their theoretical analysis of digital piracy. They compare the welfare implications of government policies and conclude that a tax on copying is superior to fining consumers, and that a subsidy for legal producers is optimal. Evidence from a discrete choice experiment carried out in the Netherlands shows that a tax of less than e2 on Internet subscriptions would keep revenues of music rights holders at the current level while simultaneously increasing consumer surplus (Handke et al. 2016).

Private Enforcement. Theory suggests that firms find it optimal to invest in private enforcement to deter piracy when public enforcement is too weak (Banerjee 2003, Sundararajan 2004, Kiema 2008, Ahn and Shin 2010, Lu and Poddar 2012). This is backed by evidence showing that private enforcement can be efective in settling infringement cases regarding digital images (Luo and Mortimer 2016), and increase sales of e-books (Reimers 2016). However, when copy protection reduces consumer utility, private enforcement can have negative implications for firm profits and social welfare (Ahn and Shin 2010). This idea is mirrored in evidence showing that music sales increase due to the removal of digital rights management technology (Zhang 2018).

## 6. Conclusion

We address the puzzle that online piracy rates remain high despite an abundance of enforcement eforts that involve large amounts of public resources. We study the unexpected shutdown of kino.to, the largest unlicensed video streaming site in the German market in 2011, using highly disaggregated clickstream data for a set of 20,000 Internet users in Germany, Italy, France, and the United Kingdom to provide detailed evidence on the efects of this intervention on consumer behavior and on the structure of the unlicensed video streaming market.

We show that the shutdown was rather inefective in reducing unlicensed consumption and moving consumers to licensed oferings. We highlight that indirect efects—consumers quickly switching to alternative unlicensed websites—and unintended externalities that operate via the type of story news articles tell about piracy, are important factors driving our results. The latter is quite surprising in light of the previous literature. Awareness about legal consequences of online piracy—in the form of the anticipation of stricter laws—has been causally linked to higher sales of licensed content (Adermon and Liang 2014, Danaher et al. 2014), and media and press coverage has often been presented as a potential mechanism to raise awareness about the negative consequences of piracy (Al-Rafee and Cronan 2006, Hennig-Thurau et al. 2007, Sinha and Mandel 2008, Danaher et al. 2010, Cox and Collins 2014). Our study shows that media coverage of copyright enforcement—which has happened regularly in the past—implies a trade-of for content creators and copyright holders, depending on the content of news articles. In the case of kino.to, only about 11% of news articles that individuals in our data read were discussing legal aspects that could have had deterring efects. Our results suggest that if that percentage had been higher, we would have seen less switching to alternative piracy websites and fewer consumers entering the market. In other settings, the introduction of journalistic standards have been shown to be efective in reducing unintended efects of news coverage. For example, Etzersdorfer and Sonneck (1998) show that the number of copycat suicides (or suicide attempts) decreased after newspapers adopted specific guidelines for journalists. From a policy perspective, it goes without saying that benefits from such eforts must be traded of against freedom of the press.

We also show that the structure of the piracy market changed after the shutdown of kino.to in a way that may make future interventions more costly and potentially even less efective. An interesting avenue for future research could be to evaluate whether broader public enforcement eforts, targeting multiple websites at the same time, or reducing the monetary incentives from advertising revenues could be more efective. From a managerial perspective, we get important insights into consumer behavior that can be helpful to design efective private copyright enforcement strategies, as well as to understand competition between licensed and unlicensed services. Although our study is specific to its historical context, we speculate that better availability and lower prices of licensed content can convince consumers to switch to licensed oferings.

## Acknowledgments

The views expressed are those of the authors and may not in any circumstances be regarded as stating an oficial position of the European Commission (EC), the EC Joint Research Center, or the Institute for Prospective Technological Studies (IPTS). The authors thank Tobias Kretschmer, Ulrich Kaiser, the senior editor, the associate editor, and three anonymous reviewers for their valuable comments and ideas. This paper benefited from feedback from conference participants at the National Bureau of Economic Research Summer Institute, International Industrial Organization Conference (Boston), European Association for Research in Industrial Economics Conference (Munich), Media Economics Workshop Stellenbosch, ZEW ICT Conference, ICT Workshop Évora, Media Workshop Florence, Munich Summer Institute, Digital Economy Workshop Liège, Verein für Socialpolitik Augsburg, and Swiss Society of Economics and Statistics Conference (Basel) and seminar presentations at Copenhagen Business School, IPTS Seville, the Düsseldorf Institute for Competition Economics, Télécom ParisTech, University of Zurich, ETH Zurich, and the Max Planck Institute Munich in 2014–2016.

## Endnotes

<sup>1</sup> Theoretical work highlights strategic reasons why too strong enforcement may be suboptimal for the firm (e.g., Conner and Rumelt 1991, Peitz and Waelbroeck 2006, Jain 2008, Tunca and Wu 2013).

<sup>2</sup> A few days after Megaupload was closed down, its competitors Filesonic and Fileserve restricted downloads to the person who uploaded the file, rendering the platform useless for the distribution of pirated content. Many other competitors subsequently followed. See http://tinyurl.com/75of8j6.

<sup>3</sup> A keyword search for prominent examples in the news database Factiva lists 37,597 articles related to “Napster” (period 1999–2002), 13,301 articles related to “Pirate Bay” (2003–2016), 13,760 articles related to “Megaupload” (2007–2013), 11,362 articles related to “HADOPI” (2009–2013), and 6,277 articles related to “PIPA” and “SOPA.”

<sup>4</sup> For example, Al-Rafee and Cronan (2006, p. 247) state that “one approach [to reduce piracy] would be to expand the media coverage on . . . digital piracy busts.” Cox and Collins (2014, p. 75) conclude that “public awareness campaigns may prove a more worthwhile investment of time and resources for the movie industry.”

Hennig-Thurau et al. (2007, p. 15) argue that “stressing the unethical element of appropriating copyrighted content . . . in marketing campaigns could increase the moral costs of illegal file sharing and lower file-sharing activities,” and Danaher et al. (2010, p. 1150) speculate that “large part of antipiracy eforts in the future may need to rely on the consumer’s ‘moral’ cost associated with piracy.” Experimental evidence in Sinha and Mandel (2008) shows that reading (madeup) news articles about piracy lawsuits can afect the perceived risk of getting caught and increase the willingness to pay for licensed content.

<sup>5</sup> In representative surveys among 10,000 Germans, only 39% stated that they find it easy to judge whether movie and TV content oferings on the Internet are legal or illegal. Eighty-six percent stated that they know about legal consequences of uploads and downloads of copyrighted material from news reports. See DCN-Studie 2013, available at https://drive.google.com/open?id<sup></sup>0Bxe11iVXrXgsd0dKeFE xWU9vWlE.

<sup>6</sup> According to a representative survey among German consumers conducted in 2011, 80% of the consumers that use unlicensed services for movie and TV series consumption do so mainly via cyberlockers and streaming sites. Only 2% use mainly BitTorrent. See DCN-Studie 2011, available at https://drive.google.com/open?id<sup></sup>0 Bxe11iVXrXgsSjBGRFpqR2txVFk.

<sup>7</sup> The name streaming site relates to the fact that the links provided on the websites often allow for the immediate consumption of the movie, without having to download the complete file. We will use the terms linking and streaming interchangeably in the remainder of the paper.

<sup>8</sup> According to a joint report of the music and advertising industry in 2012, more than two-thirds of infringing websites are predominately financed by advertising. See the report by Google and PRS for Music, available at https://docs.google.com/file/d/0Bw8Krj \_Q8UaENDhEOG1LVFRhVkU/view.

<sup>9</sup> A total of 4.3 million consumers accessed movies and 5.8 million accessed TV episodes online in 2010. Most commonly (47%), survey participants indicated that legal streaming sites (such as MyVideo) and TV station websites (many German TV stations have large online archives) were the primary sources to consume TV episodes. However, only 22% considered those services as the primary sources of movie consumption. The majority of consumers (38%) reported cyberlockers and streaming sites (such as kino.to) as their main sources of movie consumption, while 18% indicated that they mainly used cyberlockers and streaming sites for consuming TV episodes. For movies, 17% of the consumers mainly used paid download services, while only 9% mainly used such services for TV episodes.

<sup>10</sup> See https://digitalvoice.nielsen.com/us/en/home.html.

<sup>11</sup> To check whether our sample is representative of the population of Internet users, we compare key demographic variables to a representative sample of Internet users in Germany, which we construct using data from the representative German Socioeconomic Panel (Wagner et al. 2007). We find that diferences in household income, education, and age are significantly diferent from zero, but small in size. We note, however, that representativeness is not crucial for the purpose of our study, because we are interested in across- and within-group comparisons in the same sample. In an analysis not detailed here, we investigate whether the efects found in the main results difer across demographic groups. The results do not provide much evidence that this is the case.

<sup>12</sup> Nielsen measures time spent on a given URL while it is in focus (tab and browser window); see http://en-us.nielsen.com/sitelets/ cls/digital/Online-NetView-FAQ.pdf.

<sup>13</sup> See, for example, http://repat.de/2011/06/alternativen-zu-kino -to (accessed January 17, 2018).

<sup>14</sup> We randomly selected 500,000 URLs on Youtube.com that were visited by users in our data and collected information about the duration of respective videos via the YouTube API. The correlation between Nielsen’s measure of visit duration and the actual video duration is 0.79 (and 0.91 for YouTube videos shorter than 120 seconds, which are more likely to be watched completely).

<sup>15</sup> A representative survey among 8,639 German consumers estimates that 16.21 million people bought cinema, concert, or theater tickets online in 2011. Around 30.5 million Germans went to a movie theater in 2011. This implies that almost every second, a cinema visitor purchased tickets online. See http://tinyurl.com/nhur74u and GfK and German Federal Film Board (2012).

<sup>16</sup> We cannot observe purchases on iTunes, because the Nielsen NetView application captures only trafic within the browser, and iTunes is a stand-alone software. We are therefore only able to observe the visits to the iTunes web page, which is a proxy of individuals signing up of the service and downloading the iTunes application to make purchases later. Market shares for 2011 are not available, but data in the first half of 2014 show that Maxdome dominates the German market with a share of 35%, followed by iTunes with 18%, Lovefilm with 12%, and Videoload with 10%. See http://tinyurl.com/ qb3jjsw.

<sup>17</sup> We did this by crawling all Amazon URLs in our data to check the product categories of items. Amazon is by far the dominant online retailer in the German market, with a revenue of e4.8 billion in 2012. The second biggest online retailer is Otto, with e1.7 billion in revenue. Amazon’s market position is similarly dominant in other European countries. See “E-commerce markt Deutschland 2013,” EHI Retail Institute, https://www.handelsdaten.de/e-commerce/ umsatz-der-groessten-online-shops-deutschland-1 (accessed July 18, 2018) and Burn-Callander (2014).

<sup>18</sup> See “European video market–Resilient packaged media, DVD and beyond,” http://tinyurl.com/lzu6488 (accessed January 18, 2018) and The Guardian (2017).

<sup>19</sup> According to news articles, 13 suspects were immediately arrested. See Reißmann (2011).

<sup>20</sup> Less than 2.5% of the news articles and blog posts covering and following up on the shutdown of kino.to we observe are written in English, and 85% of the URLs have the German top-level domain “.de.”

<sup>21</sup> As we have many zeros in the dependent variable and want to avoid losing those observations, we follow the prior literature and take the log over Clicks <sup>+</sup> 1.

<sup>22</sup> An alternative way of checking for the validity of our identification assumption is to perform a placebo test, where we focus on the preshutdown period only and define a “placebo” shutdown at the middle point of that time period. Estimating our diference-indiferences model (1) on this subset of the data should provide statistically insignificant results if the identification assumption is valid. Performing such an exercise indeed leads to nonsignificant estimates for the corresponding coeficients $\delta _ { 1 }$ (coeficient <sup> −</sup>0.044, SE <sup></sup> 0.032) and $\delta _ { 2 }$ (coeficient <sup></sup> <sup>−</sup>0.002, SE <sup></sup> 0.004) in Equation (1). One might also be worried that some of the preshutdown coeficients are significantly diferent from zero (see Figure 3). If we exclude those weeks from the sample, the results, which are not presented here but are available on request, are again very similar to our main results.

<sup>23</sup> Point estimates are transformed to percentage values as follows: PercentageChange <sup> (</sup>exp<sup>(</sup>Coeficient<sup>)</sup> <sup>−</sup> 1<sup>)</sup> <sup>×</sup> 100.

<sup>24</sup> As shown in Table 4 and discussed below, the net efect is driven by two opposing efects. This explains that the coeficient is small in magnitude and relatively imprecisely estimated.

<sup>25</sup> We also add group-specific time trends of the News variable. Note that we cannot separately identify coeficients for lower-order interaction variables in this model. By definition, users cannot read news about the shutdown before it happened, and therefore News <sup></sup> 0 if

$A f t e r _ { t } = 0 .$ This makes After and News collinear, and therefore also any interaction with each.

<sup>26</sup> In results not reported here, but available on request, we can show that the efects are very similar when we use a control group generated from a propensity score model that matches individuals based on observable characteristics.

<sup>27</sup> As discussed in Endnote 22, we can also conduct placebo tests to check for the validity of our identification assumption. Performing such an exercise for our diferent dependent variables leads to nonsignificant estimates for the corresponding coeficients δ and δ in Equation (1) for all but one case (the δ coeficient when using clicks on Amazon DVD pages as a dependent variable, which turns out to be marginally significant: coeficient <sup> −</sup>0.007, SE <sup></sup> 0.004). We additionally perform our estimations by focusing on a shorter time window around the shutdown, which essentially removes weeks that are significantly diferent from zero (see Figures 3–6). Those results, which are not presented but available on request, are very similar to our main results presented in Table 5.

<sup>28</sup> The efects reported in Table 5 can be replicated to a large extent by using an alternative control group generated from a propensity score model that matches individuals based on observable characteristics. The results, which are not reported here but available on request, show small positive coeficients (significant at the 10% level) for After <sup>×</sup> Kino and After <sup>×</sup> Non-Kino regarding visits to movie theaters. All other coeficients are very similar to those in Table 5.

<sup>29</sup> Note that any measure of prior knowledge about alternative piracy websites, including the multihoming status, may be correlated to unobservables. For example, young and tech-savvy Internet users may be more interested in consuming contents online, and therefore also in multihoming on diferent piracy websites. The following results therefore need to be interpreted with caution.

<sup>30</sup> One should also take into account the potential efect of the intervention on prices. As mentioned in Section 3.3.1, we do not find any evidence that movie theaters or ofline and online retailers changed their content or prices as a result of the kino.to shutdown.

<sup>31</sup> Price information about purchase and rental prices on iTunes comes from the meta search site werstreamt.es (in 2014) and cinema ticket prices from the German Federal Film Board (FFA), and we calculate average DVD/Blu-ray prices directly from the Amazon pages that individuals visited in our data.

<sup>32</sup> The calculation is as follows: 0.17 <sup>×</sup> 0.035 <sup>×</sup> 3 <sup>×</sup> 100 <sup></sup> 1.79 and 0.17 <sup>×</sup> 0.20 <sup>×</sup> 16.57 <sup>×</sup> 100 <sup></sup> 56.34.

<sup>33</sup> If we were to take the enforcement costs into consideration, which are probably largely borne by taxpayers, the estimated loss in consumer surplus would of course be higher.

<sup>34</sup> Note that the decrease in movie2k.to’s market share is not due to a decrease in trafic to the platform, but an expansion of the overall piracy market driven by the entry of kinoX.to.

<sup>35</sup> The HHI is calculated by summing up the squared market shares of all active unlicensed platforms. Using percentages to express market shares leads to values of the HHI ranging from 0 to 10,000, the latter corresponding to the case where a single platform has a market share of 100%.

<sup>36</sup> For instance, the initial level of market concentration, the substitutability of content across existing sites, and even the severity of the punishment imposed on the platform’s owners could all afect the impact of the shutdown on the structure of the market. Such market specificities may also influence the entry decision of a new platform, which may in turn afect the efects of such an intervention on the structure of the piracy market.

<sup>37</sup> Germany’s piracy rate in 2011 was about two-thirds of a standard deviation below the European average, and 40% above the piracy rate of the United States. Calculations are based on data from

Table 1 in Danaher and Smith (2014) and page 9 in Business Software Alliance (2012).

<sup>38</sup> Looking at all links listed on rlslog.net, a linking site that is very similar to kino.to, Lauinger et al. (2013) show that the median number of alternative links to the same content (hosted on a variety of cyberlockers) is 48.

<sup>39</sup> We do not have access to reliable data on the catalogues of licensed services in 2011. However, according to the comparison website www.werstreamt.es, in November 2014, the licensed German market ofered less content than kino.to, with 11,600 movies on iTunes, 8,500 on Maxdome, 5,800 on Videoload, and 1,000 on Netflix compared to 20,000 movies on kino.to.

<sup>40</sup> See Wikipedia, s.v. “iTunes Store,” https://en.wikipedia.org/wiki/ ITunes\_Store (accessed January 17, 2018).

<sup>41</sup> To look into this, we collected yearly average cinema ticket prices for Germany (FFA), Italy (SIAE), France (CNC), and the United Kingdom (UK Cinema Association) and consumer price index data (Organisation for Economic Co-operation and Development) for 2010–2014. Regressing consumer price index data on an index of cinema ticket prices (both base year 2010) yields a coeficient of 0.9.

<sup>42</sup> See the report by Google and PRS for Music at https://docs .google.com/file/d/0Bw8Krj\_Q8UaENDhEOG1LVFRhVkU/view.

<sup>43</sup> Results are not reported here but are available on request.

<sup>44</sup> Note, however, that the mere availability of licensed oferings may not be enough to curtail piracy. Godinho de Matos et al. (2017) show that reducing piracy also requires ofering licensed content much earlier and at much lower prices than those currently ofered in the marketplace.

<sup>45</sup> A recent working paper by Danaher et al. (2015a) looks at this question and uses highly aggregated clickstream data to compare the efects of two policy experiments in the United Kingdom—court decisions that ordered Internet service providers to block one piracy website versus blocking multiple piracy websites. While they do not find evidence of an increase in visits to paid streaming services when one website is blocked, they find a positive efect in the case of the wide blockade. For both interventions, their analysis suggests that a change in the number of clicks to other torrent sites or cyberlockers is small or not significant, but the results also show that consumers increase clicks to VPN services that allow them to circumvent the blockade.

<sup>46</sup> See http://ec.europa.eu/growth/tools-databases/newsroom/cf/ itemdetail.cfm?item\_id<sup></sup>8974.

## References

Adda J, McConnell B, Rasul I (2014) Crime and the depenalization of cannabis possession: Evidence from a policing experiment. J. Political Econom. 122(5):1130–1199.

Adena M, Enikolopov R, Petrova M, Santarosa V, Zhuravskaya E (2015) Radio and the rise of the Nazis in prewar Germany. Quart. J. Econom. 130(4):1885–1939.

Adermon A, Liang C-Y (2014) Piracy and music sales: The efects of an anti-piracy law. J. Econom. Behav. Organ. 105:90–106.

Aguiar L, Waldfogel J (2018) As streaming reaches flood stage, does it stimulate or depress music sales? Internat. J. Indust. Organ. 57:278–307.

Ahn I, Shin I (2010) On the optimal level of protection in DRM. Inform. Econom. Policy 22(4):341–353.

Al-Rafee S, Cronan TP (2006) Digital piracy: Factors that influence attitude toward behavior. J. Bus. Ethics 63:237–259.

Amtsgericht Leipzig (2011) Urteil zum Verfahren KINO.TO. District Court Leipzig, Verdict 200 Ls 390 Js 184<sup>/</sup>11. Accessed January 17, 2018, http://www.justiz.sachsen.de/lentschweb/document .phtml?id<sup></sup>978.

Angrist JD, Kugler AD (2008) Rural windfall or a new resource curse? Coca, income, and civil conflict in Colombia. Rev. Econom. Statist. 90(2):191–215.

Antoniades D, Markatos EP, Dovrolis C (2009) One-click hosting services: A file-sharing hideout. Proc. 9th ACM SIGCOMM Conf. Internet Measurement Conf., IMC’09 (ACM, New York), 223–234.

Arnold M, Darmon E, Dejean S, Penard T (2014) Graduated response policy and the behavior of digital pirates: Evidence from the French three-strike (Hadopi) law. Working paper, University of Delaware, Newark.

Ayres I, Levitt SD (1998) Measuring positive externalities from unobservable victim precaution: An empirical analysis of lojack. Quart. J. Econom. 113(1):43–77.

Bai J, Waldfogel J (2012) Movie piracy and sales displacement in two samples of Chinese consumers. Inform. Econom. Policy 24(3): 187–196.

Banerjee DS (2003) Software piracy: A strategic analysis and policy instruments. Internat. J. Indust. Organ. 21(1):97–127.

Batikas M, Claussen J, Peukert C (2017) Follow the money: Piracy and online advertising. Working paper, LMU Munich.

Becker GS, Murphy KM, Grossman M (2006) The market for illegal goods: The case of drugs. J. Political Econom. 114(1):38–60.

Bertoni M, Brunello G, Rocco L (2013) When the cat is near, the mice won’t play: The efect of external examiners in Italian schools. J. Public Econom. 104:65–77.

Bertrand M, Duflo E, Mullainathan S (2004) How much should we trust diferences-in-diferences estimates? Quart. J. Econom. 119(1):249–275.

Bild (2011) Illegales Filmportal ist zurück–Kino.to-Piraten verhühnen Ermittler. Accessed January 17, 2018, http://tinyurl.com/ 5usgxsu.

Burn-Callander R (2014) Amazon dominates CD, DVD and game sales in the UK. The Telegraph (May 26). Accessed January 17, 2018, http://tinyurl.com/jwvhbpo.

Business Software Alliance (2012) Shadow market: 2011 BSA global software piracy study. Report, Business Software Alliance, Washington, DC.

Cameron S (1988) The economics of crime deterrence: A survey of theory and evidence. Kyklos 41(2):301–323.

Card D, Krueger AB (1994) Minimum wages and employment: A case study of the fast-food industry in New Jersey and Pennsylvania. Amer. Econom. Rev. 84(4):772–793.

Chen P, Hitt LM (2002) Measuring switching costs and the determinants of customer retention in Internet-enabled businesses: A study of the online brokerage industry. Inform. Systems Res. 13(3):255–274.

Chen Y, Png I (2003) Information goods pricing and copyright enforcement: Welfare analysis. Inform. Systems Res. 14(1):107–123.

Chiang EP, Assane D (2009) Estimating the willingness to pay for digital music. Contemporary Econom. Policy 27(4):512–522.

Chiou JS, Huang CY, Lee HH (2005) The antecedents of music piracy attitudes and intentions. J. Bus. Ethics 57(2):161–174.

Chip Online (2011) GVU will Nutzer verfolgen und bestrafen. Accessed January 17, 2018, http://tinyurl.com/635vgcl.

Cho H, Salmon CT (2007) Unintended efects of health communication campaigns. J. Comm. 57:293–317.

Conner KR, Rumelt RP (1991) Software piracy: An analysis of protection strategies. Management Sci. 37(2):125–139.

Cook T, Campbell D (1979) Quasi-Experimentation: Design and Analysis Issues for Field Settings (Houghton Miflin, Boston).

Cox J, Collins A (2014) Sailing in the same ship? Diferences in factors motivating piracy of music and movie content. J. Behavioral Experiment. Econom. 50:70–76.

Danaher B, Smith MD (2014) Gone in 60 seconds: The impact of the Megaupload shutdown on movie sales. Internat. J. Indust. Organ. 33(March):1–8.

Danaher B, Smith MD, Telang R (2013) Piracy and copyright enforcement mechanisms. Innovation Policy and the Economy, Vol. 14 (University of Chicago Press, Chicago), 25–61.

Danaher B, Smith MD, Telang R (2015a) The efect of piracy website blocking on consumer behavior. Working paper, Wellesley College, Wellesley, MA.

Danaher B, Dhanasobhon S, Smith MD, Telang R (2010) Converting pirates without cannibalizing purchasers: The impact of digital distribution on physical sales and Internet piracy. Marketing Sci. 29(6):1138–1151.

Danaher B, Dhanasobhon S, Smith MD, Telang R (2015b) Understanding media markets in the digital age: Economics and methodology. Goldfarb A, Greenstein SM, Tucker C, eds. Economic Analysis of the Digital Economy (University of Chicago Press, Chicago), 385–406.

Danaher B, Smith MD, Telang R, Chen S (2014) The efect of graduated response anti-piracy laws on music sales: Evidence from an event study in France. J. Indust. Econom. 62(3):541–553.

Dell M (2015) Traficking networks and the Mexican drug war. Amer. Econom. Rev. 105(6):1738–1779.

Dey D, Kim A, Lahiri A (2016) Online piracy and the “longer arm” of enforcement. Working paper, University of Washington, Seattle.

DiTella R, Schargrodsky E (2004) Do police reduce crime? Estimates using the allocation of police forces after a terrorist attack. Amer. Econom. Rev. 94(1):115–133.

Dobkin C, Nicosia N, Weinberg M (2014) Are supply-side drug control eforts efective? Evaluating OTC regulations targeting methamphetamine precursors. J. Public Econom. 120:48–61.

Draca M, Machin S, Witt R (2011) Panic on the streets of London: Police, crime, and the July 2005 terror attacks. Amer. Econom. Rev. 101(5):2157–2181.

Esser F, Brosius HB (1996) Television as arsonist? The spread of rightwing violence in Germany. Eur. J. Comm. 11(2):235–260.

Etzersdorfer E, Sonneck G (1998) Preventing suicide by influencing mass-media reporting. The Viennese experience 1980–1996. Archives Suicide Res. 4(1):67–74.

Focus Online (2011) Filmportal ist wieder online. (July 12), accessed January 18, 2018, http://tinyurl.com/6ad5dus.

Freenet (2011) Kino.to-Nutzer–diese rechtlichen Folgen drohen. Accessed January 17, 2018, http://tinyurl.com/lhx8ub8.

GfK, Bundesverband Audiovisuelle Medien (2013) Der Videomarkt 2013—GfK consumer panel. Accessed January 17, 2018, http://www.bvv-medien.de/jwb\_pdfs/JWB2013.pdf.

GfK, German Federal Film Board (2012) Der Kinobesucher 2011—Strukturen und Entwicklungen auf Basis des GfK panels. Accessed January 17, 2018, http://www.fa.de/start/ download.php?file<sup></sup>publikationen/kinobesucher\_2011.pdf.

GfK, Gesellschaft zur Verfolgung Von Urheberrechtsverletzungen, Börsenverein des Deutschen Buchhandels (2011) Studie zur digitalen Content-Nutzung (DCN Studie). Accessed January 17, 2018, http://www.musik industrie.de/uploads/media/DCN -Studie\_2011\_Presseversion\_FINAL\_02.pdf.

Godinho de Matos M, Ferreira P, Smith MD (2017) The efect of video-on-demand on piracy: Evidence from a household level randomized experiment. Management Sci., ePub ahead of print November 22, https://doi.org/10.1287/mnsc.2017.2875.

Goh KY, Hui KL, Png IPL (2011) Newspaper reports and consumer choice: Evidence from the do not call registry. Management Sci. 57(9):1640–1654.

Goh K-Y, Hui KL, Png IPL (2015) Privacy and marketing externalities: Evidence from do not call. Management Sci. 61(12):2982–3000.

Goldfarb A (2006a) State dependence at Internet portals. J. Econom. Management Strategy 15(2):317–352.

Goldfarb A (2006b) The medium-term efects of unavailability. Quant. Marketing Econom. 4:143–171.

Gomez-Herrera E, Martens B (2015) Language, copyright and geographic segmentation in the EU digital single market for music and film. Working paper, Institute for Prospective Technological Studies, Joint Research Center, European Commission, Seville, Spain.

Gould MS (2001) Suicide and the media. Ann. NY Acad. Sci. 932(1): 200–224.

Gulli (2011) Kino.to Nachfolger berets online: Video2k.tv. Accessed January 18, 2018, http://tinyurl.com/kkj3bbb.

Handke C, Balazs B, Vallbé JJ (2016) Going means trouble and staying makes it double: The value of licensing recorded music online. J. Cultural Econom. 40(3):227–259.

Hennig-Thurau T, Henning V, Sattler H (2007) Consumer file sharing of motion pictures. J. Marketing 71:1–18.

Howell DC (2005) External validity. Everitt BS, Howell DC, eds. Encyclopedia of Statistics in Behavioral Science, Vol. 2 (John Wiley & Sons, Ltd., Hoboken, NJ), 588–591.

Hui KL, Png I (2003) Piracy and the legitimate demand for recorded music. B.E. J. Econom. Anal. Policy 2(1):1–22.

Hui KL, Kim SH, Wang QH (2017) Cybercrime deterrence and international legislation: Evidence from distributed denial of service attacks. MIS Quart. 41(2):497–523.

Jain S (2008) Digital piracy: A competitive analysis. Marketing Sci. 27(4):610–626.

Kiema I (2008) Commercial piracy and intellectual property policy. J. Econom. Behav. Organ. 68(1):304–318.

Lang B (2017) Studios flirt with ofering movies early in home for \$30. Variety (March 21), accessed January 17, 2018, https://variety .com/2017/film/news/studios-premium-vod-early-1202013205/.

Lauinger T, Szydlowski M, Onarlioglu K, Wondracek G, Kirda E, Kruegel C (2013) Clickonomics: Determining the efect of antipiracy measures for one-click hosting. Proc. NDSS Sympos. 2013, San Diego, CA.

Lechner M (2002) Program heterogeneity and propensity score matching: An application to the evaluation of active labor market policies. Rev. Econom. Statist. 84(2):205–220.

Levitt SD (1997) Using electoral cycles in police hiring to estimate the efect of police on crime. Amer. Econom. Rev. 87(3):270–290.

Liao C, Lin HN, Liu YP (2010) Predicting the use of pirated software: A contingency model integrating perceived risk with the theory of planned behavior. J. Bus. Ethics 91(2):237–252.

Liu M, Zhang Z, Hui P, Qin Y, Kulkarni S (2013) Measurement and understanding of Cyberlocker URL-sharing sites: Focus on movie files. Adv. Soc. Networks Anal. Mining, 2013 IEEE/ACM Internat. Conf., 902–909.

Lu Y, Poddar S (2012) Accommodation or deterrence in the face of commercial piracy: The impact of intellectual property rights protection. Oxford Econom. Papers 64(3):518–538.

Luo H, Mortimer JH (2016) Copyright infringement in the market for digital images. Amer. Econom. Rev. Papers Proc. 106(5):140–145.

McKenzie J (2017) Graduated response policies to digital piracy: Do they increase box ofice revenues of movies? Inform. Econom. Policy 38:1–11.

NTV (2011) Millionen Nutzer haben Angst–Polizei schließt Kino.to. (June 9), accessed January 18, 2018, http://tinyurl.com/3mfm9tq.

Orme T (2014) The short- and long-term efectiveness of anti-piracy laws and enforcement actions. J. Cultural Econom. 38:351–368.

Peitz M, Waelbroeck P (2006) Piracy of digital products: A critical review of the theoretical literature. Inform. Econom. Policy 18: 449–476.

Peukert C, Claussen J, Kretschmer T (2017) Piracy and box ofice movie revenues: Evidence from Megaupload. Internat. J. Indust. Organ. 52:188–215.

Poort J, Weda J (2015) Elvis is returning to the building: Understanding a decline in unauthorized file sharing. J. Media Econom. 28(2):63–83.

Poort J, Leenheer J, van der Ham J, Dumitru C (2014) Baywatch: Two approaches to measure the efects of blocking access to the Pirate Bay. Telecomm. Policy 38:383–392.

Proserpio L, Salvemini S, Ghiringhelli V (2005) Entertainment pirates: Determinants of piracy in the software, music and movie industries. Internat. J. Arts Management 8(1):33–47.

Protalinski E (2016) KickassTorrents mirrors go down, but new KAT sites quickly spring up. Venture Beat (July 31), accessed January 17, 2018, https://venturebeat.com/2016/07/31/kickas storrents-mirrors-go-down-but-new-kat-sites-quickly-spring-up/.

Reimers I (2016) Can private copyright protection be efective? Evidence from book publishing. J. Law Econom. 59(2):411–440.

Reißmann VO (2011) Ermittler verhaften mutmaßliche Betreiber von Raubkopie-Seite. Spiegel Online (June 8), accessed January 17, 2018, http://www.spiegel.de/netzwelt/netzpolitik/kino-to -ermittler-verhaften-mutmassliche-betreiber-von-raubkopie-seite -a-767375.html.

Rob R, Waldfogel J (2006) Piracy on the high C’s: Music downloading, sales displacement, and social welfare in a sample of college students. J. Law Econom. 49(1):29–62.

Rob R, Waldfogel J (2007) Piracy on the silver screen. J. Indust. Econom. 55(3):379–395.

Sinha R, Mandel N (2008) Preventing digital music piracy: The carrot or the stick? J. Marketing 72:1–15.

Spiegel Online (2012) kino.to: Angeklagte und Urteile im Überblick. (June 14). Accessed January 17, 2018, http://www.spiegel.de/ netzwelt/web/kino-to-angeklagte-und-urteile-im-ueberblick-a -838822.html.

Süddeutsche Zeitung (2011) Millionenkonten bei kino.to entdeckt. (June 19), accessed January 17, 2018, http://tinyurl.com/ mam4sx9.

Sundararajan A (2004) Managing digital piracy: Pricing and protection. Inform. Systems Res. 15(3):287–308.

The Guardian (2017) Film and TV streaming and downloads overtake DVD sales for first time. (January 5), accessed January 17, 2018, http://tinyurl.com/guqwkya.

Thomes TP (2013) An economic analysis of online streaming music services. Inform. Econom. Policy 25(2):81–91.

Tsai MF, Chiou JR (2012) Counterfeiting, enforcement and social welfare. J. Econom. 107(1):1–21.

Tual M (2016) Zone Téléchargement est-il vraiment de retour? Le Monde (December 15), accessed January 17, 2018, https://www .lemonde.fr/pixels/article/2016/12/15/zone-telechargement -est-il-vraiment-de-retour\_5049581\_4408996.html.

Tunca T, Wu Q (2013) Fighting fire with fire: Commercial piracy and the role of file sharing on copyright protection for digital goods. Inform. Systems Res. 24(2):436–453.

UK Intellectual Property Ofice (2016) Online copyright infringement tracker—Latest wave of research Mar 16–May 16. Report, UK Intellectual Property Ofice, New port, UK.

van Kranenburg H, Hogenbirk A (2005) Multimedia, entertainment, and business software copyright piracy: A cross-national study. J. Media Econom. 18(2):109–129.

Vida I, Kos Koklič M, Kukar-Kinney M, Penz E (2012) Predicting consumer digital piracy behavior: The role of rationalization and perceived consequences. J. Res. Interactive Marketing 6(4): 298–313.

Wagner GG, Frick JR, Schupp J (2007) The German socio-economic panel study (SOEP)-evolution, scope and enhancements. Schmollers Jahrbuch 127(1):139–169.

Walls W (2008) Cross-country analysis of movie piracy. Appl. Econom. 40(5):625–632.

Watson S, Zizzo D, Fleming P (2015) Determinants of unlawful file sharing: A scoping review. PLoS One 10(6):e0127921.

Yanagizawa-Drott D (2014) Propaganda and conflict: Evidence from the Rwandan genocide. Quart. J. Econom. 129(4):1947–1994.

Zamoon S, Curley SP (2008) Ripped from the headlines: What can the popular press teach us about software piracy? J. Bus. Ethics 83(3):515–533.

Zeit Online (2011) Polizei schaltet kino.to ab. (June 8), accessed January 17, 2018, http://tinyurl.com/6bjxxo2.

Zhang L (2018) Intellectual property strategy and the long tail: Evidence from the recorded music industry. Management Sci. 64(1):24–42.
