---
otero_id: 9862
otero_key: "GN55BXFS"
title: "<b>Research Note</b>—Perceived Firm Attributes and Intrinsic Motivation in Sponsored Open Source Software Projects"
authors: "Sebastian Spaeth; Georg von Krogh; Fang He"
year: "2015"
journal: "Information Systems Research"
doi: "10.1287/isre.2014.0539"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [157.211.3.38] On: 28 November 2014, At: 08:55 Publisher: Institute for Operations Research and the Management Sciences (INFORMS) INFORMS is located in Maryland, USA

# Information Systems Research

## HSR

![](/api/attachments/GN55BXFS/fulltext/images/42af912c1dbefbb27ec292829b5b0a73e123b85fd6e6a89c5f8ba216d00281ef.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Research Note—Perceived Firm Attributes and Intrinsic Motivation in Sponsored Open Source Software Projects

Sebastian Spaeth, Georg von Krogh, Fang He

To cite this article:

Sebastian Spaeth, Georg von Krogh, Fang He (2014) Research Note—Perceived Firm Attributes and Intrinsic Motivation in Sponsored Open Source Software Projects. Information Systems Research

Published online in Articles in Advance 24 Oct 2014

http://dx.doi.org/10.1287/isre.2014.0539

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2014, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/GN55BXFS/fulltext/images/2c915e3e52a18c67090e12a3082f76b303a80f73bb7fdcecde962cfc7efb041a.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Research Note

# Perceived Firm Attributes and Intrinsic Motivation in Sponsored Open Source Software Projects

Sebastian Spaeth

University of Hamburg, School of Business, Economics and Social Sciences, 20146 Hamburg, Germany, sebastian.spaeth@uni-hamburg.de

Georg von Krogh, Fang He ETH Zurich, 8092 Zurich, Switzerland {gvkrogh@ethz.ch, fhe@ethz.ch}

oluntary contributions are crucial to the success of open source software (OSS) projects. Firms sponsoring OSS projects may face substantial challenges in soliciting such contributions, since volunteer participants are neither regulated by an employment contract nor offered financial incentives. Although prior work has shown the positive impact of motivation on the effort expended by volunteer participants, there is limited understanding of how specific firm attributes shape volunteers’ intrinsic motivation. We offer a theoretical model of how the perceived community-based credibility and openness of the sponsoring firm have a positive impact on the intrinsic motivation of volunteer participants. The model is explored using survey data on volunteer participants from two sponsored OSS projects. Results show that a sponsoring firm’s community-based credibility (OSS developers’ perception of its expertise and trustworthiness) and openness (its mutual knowledge exchange with the community) strengthen the volunteer participants’ social identification with the firm-sponsored community, which in turn reinforces their intrinsic motivation to participate. Moreover, the perceived community-based credibility of a sponsoring firm directly enhances volunteer participants’ intrinsic motivation, whereas perceived openness fails to affect motivation without the mediating mechanism of social identification. Implications for firms seeking voluntary contributions for their sponsored OSS projects are discussed.

Keywords: open source software; firm sponsorship; firm attributes; intrinsic motivation; voluntary contributions History: Natalia Levina, Senior Editor; Sunil Mithas, Associate Editor. This paper was received on March 16, 2012, and was with the authors 15 months for 3 revisions. Published online in Articles in Advance.

## Introduction

Firm sponsorship in open source software (OSS) development is increasing rapidly (Mehra et al. 2011, O’Mahony and Bechky 2008). In September 2013, IBM announced plans to invest US \$1 billion in new Linux and open source technologies for its Power Systems servers. Besides the vast investment of IBM, the development of the latest Linux kernel (version 3.14) includes contributions by more than 200 other firms, according to LWN.net. Firms pledge substantial financial, human, and technological resources to the project with objectives such as increasing sales, improving reputation, cutting product development cost, shortening time to market of new products, and detecting new technologies and user needs (Dahlander and Magnusson 2008). The success of sponsored OSS projects hinges on a community with a mix of employed and volunteer participants (Setia et al. 2012). On one hand, the sponsor designs employment contracts that regulate employees’ involvement in the project (Mehra et al. 2011) and offers proper incentives for their contributions. On the other hand, it strives to provide an accessible platform to engage volunteer participants (Gruber and Henkel 2006). Despite significant investment, sponsoring firms face substantial challenges in soliciting such contributions, since volunteer participants are neither regulated by an employment contract nor offered direct financial incentives.

OSS participants are motivated to contribute by a wide range of factors, some of which are characterized by intrinsic motivation, a desire to engage in activities because they are interesting or inherently rewarding (Deci and Ryan 1985). Intrinsic motivation includes the fun and enjoyment of completing technical tasks, peer recognition (Lakhani and Wolf 2005), altruism (Bitzer et al. 2007), and learning (David and Shapiro 2008). Empirical evidence typically suggests that firm sponsorship provides extrinsic motivation through paid development or career opportunities but dampens intrinsic motivation because of its forprofit nature and control over the project (Shah 2006, Stewart and Ammeter 2002, Stewart and Gosain 2006). Extant literature on OSS development views nonfirm sponsorship as preferable by the intrinsically motivated, yet we continue to observe a substantial number of volunteer participants in firm-sponsored projects. Could certain aspects of a sponsoring firm exert a positive impact on the intrinsic motivation of volunteers and, if so, how?

Drawing on work motivation research (Colquitt et al. 2001, Eisenberger et al. 1990, Spreitzer 1996), our central thesis is that sponsoring firms can play a more encouraging role in shaping volunteers’ intrinsic motivation than prior research assumes. We propose that two important attributes of the sponsoring firm—community-based credibility and openness— when communicated to and perceived by volunteers, enhance their intrinsic motivation. Building on recent research on OSS as a social practice (Fang and Neufeld 2009, von Krogh et al. 2012), we further argue that the impact of these firm attributes is embedded in a social context through volunteers’ identification with the OSS community.

This paper proceeds as follows. The next section reviews relevant literature on OSS participation and develops a theoretical model with five hypotheses. The methodology of the survey study is then described, followed by a section reporting data analysis results. We conclude by discussing the contributions and limitations of the current study and avenues for future research.

## Background and Hypotheses

The intricate relationship between firm sponsorship and developers’ motivation has drawn substantial scholarly attention as firms become progressively involved in OSS development. Stewart and Ammeter (2002) explored a sample of 240 OSS projects and found that the popularity of projects over time was significantly strengthened by sponsorship. These authors also pointed out that firm sponsorship could reduce the enthusiasm of those participants who value independence from organizational constraints and disdain profit motives. Shah (2006) further examined the motivation of participants in two types of OSS communities, one nonsponsored and the other sponsored, in which the firm controlled the OSS development process and restricted contributors’ access to it. She found that contributors motivated by the use value of the software tended to participate in sponsored projects, whereas those motivated by fun and enjoyment preferred to participate in nonsponsored projects. Using a different categorization of projects, Stewart et al. (2006) identified instances of market (firm) and nonmarket (university, government, or other not-for-profit organization) sponsorship and analyzed license-based incentives in each category. Based on a sample of 138 OSS projects from Freshmeat.net, they concluded that participants considered signals about sponsorship and licensing when making decisions to contribute. For example, nonmarket sponsorship projects with nonrestrictive licenses attracted more contributors than those without sponsorship or with market sponsorship.

Together these studies have greatly improved our understanding of OSS sponsorship and its pronounced impact on participants’ attention and commitment to a project. One could infer from them that certain attributes associated with a sponsor, for example, a less restrictive license (Stewart et al. 2006) or an open governance structure (Shah 2006), are more compatible with the intrinsic motivation of volunteer participants. The dichotomy of firm and nonfirm sponsorship in existing work, however, prevents scholars from investigating the motivational implications of specific attributes of a sponsoring firm. Further, whereas empirical studies have thus far portrayed firm sponsorship as a liability in seeking voluntary contributions, it is not improbable that a sponsoring firm could also exhibit desirable attributes that enhance the intrinsic motivation of volunteers. These firm attributes, and their effect on motivation, need to be better understood (Crowston et al. 2012).

Individuals’ perception of situations and people with whom they interact are critical for their motivation to reciprocate (Dufwenberg 2011). Extensive research on work motivation suggests that individuals’ perception of a firm influences their intrinsic motivation. Important organizational characteristics for work motivation include perceived organizational support (Eisenberger et al. 1990), procedural and distributive justice (Colquitt et al. 2001), and level of inclusiveness (Spreitzer 1996). Perceptions regarding such attributes are particularly relevant to voluntary behavior that extends beyond an employment contract. For instance, extra-role or organizational citizenship behavior is more likely to occur when employees perceive a firm as fair, supporting, and inclusive (Organ and Moorman 1993, Rhoades et al. 2001, Robinson and Morrison 1995). These general mechanisms are present in the OSS context, although in particular ways. A sponsoring firm can display fairness in its treatment of the collective goods created by the community (Shah 2006) and in its support and inclusion of volunteer developers via providing source code, technical assistance, and even patented knowledge (Alexy et al. 2013). Firms that do so, as a consequence, are perceived by the community as credible and open.

We therefore center our arguments on these perceived attributes that distinguish one sponsoring firm from another, namely, community-based credibility and openness. In the following section, we advance a theoretical model considering the direct and indirect influences of these perceived attributes on volunteer participants’ intrinsic motivation in sponsored OSS projects. Consistent with the recent understanding of OSS development as a social practice (Fang and Neufeld 2009, von Krogh et al. 2012) and the critical role of identification in promoting proactive behaviors within organizations (Van Dick et al. 2006, Ma and Agarwal 2007), our model delineates the mediating mechanism engendered by social identification.

## Credibility

Although credibility has not yet been linked to developers’ motivation, marketing research shows that a company’s credibility gained from its socially responsible practices can bolster consumer preferences (Cornwell et al. 2005, Javalgi et al. 1994). The sponsor’s credibility within the community is one of the most salient attributes OSS participants would judge. Newell and Goldsmith (2001) examined corporate credibility and statistically clustered it into two categories: expertise, or the extent to which the firm is viewed as capable of fulfilling its claims, and trustworthiness, or the extent to which the firm can be trusted. For them, these elements of credibility are highly context specific and thus depend on the perception of individuals involved. Accordingly, we define the community-based credibility of a sponsoring firm as OSS developers’ perception of the firm’s level of expertise and trustworthiness.

There are compelling reasons why the communitybased credibility of a sponsoring firm can strengthen volunteer participants’ intrinsic motivation to contribute to OSS development. First, a credible sponsor offers valuable learning opportunities. One important motivational factor in participants’ involvement in open source projects is the opportunity to extend their programming skills, which requires knowledge sharing, assistance from others, and feedback on task performance (Hars and Ou 2002, Spaeth et al. 2008). Insofar as volunteer participants perceive firm employees to be experts in the field, they are intrinsically motivated to learn the desired skills through participating in the sponsored project (Deci and Ryan 1985). Second, a credible sponsor provides a safe environment for participation, where OSS contributors can expect their efforts to benefit themselves and/or the community (Fang and Neufeld 2009). When volunteer participants perceive a sponsoring firm as trustworthy in terms of acting benevolently and handling their innovations fairly, their intrinsic motivation to contribute to the project is reinforced (David and Shapiro 2008). If volunteer participants perceive the sponsoring firm as untrustworthy, they will reduce their efforts to avoid being exploited as “gratis employees” (Kerr 1983, Stewart et al. 2006). Empirical research on firm involvement in OSS communities confirms that a sponsor’s trustworthiness impacts contributors’ reported willingness to expend effort on the project (Dahlander and Magnusson 2005, Dahlander and Wallin 2006). This finding is consistent with the large body of work that draws connections between individuals’ trust in others and their intrinsic desire to act cooperatively (Callan et al. 2010).

<sup>Hypothesis</sup> <sup>1.</sup> The perceived community-based credibility of a sponsoring firm has a direct positive effect on the intrinsic motivation of the volunteer participants.

## Openness

A sponsoring firm can be well regarded as credible within the community but may not be perceived as “open” to the community. Openness is the degree to which the sponsoring firm encourages mutual knowledge exchange between the community and the firm (Jeppesen and Lakhani 2010). Research on virtual communities in general (Kollock 1999) and on OSS development in particular (Rossi 2006) has shown that generalized reciprocity, which is the expectation that knowledge flows in both directions, is a foundation of intrinsic motivation to contribute. The OSS context represents a reciprocity-based gift economy (Bergquist and Ljungberg 2001, Zeitlyn 2003), where both receiving a gift and having an influence over the gift making solicit participation. In the following text we elaborate on the importance of perceived openness in terms of knowledge and information provided by the firm, as well as the impact of voluntary contributions assimilated by the firm.

Accumulated research shows that there are many benefits for firms to share knowledge (e.g., product and process technologies, software code, algorithms, help), including downstream product improvements (Harhoff 1996), increased innovation activity by users and manufacturers (Harhoff et al. 2003), ease of access to innovation networks (Muller and Pénin 2006), lowcost marketing activity to enhance reputation (Gruber and Henkel 2006), and network externalities and technological standard setting (Bonaccorsi and Rossi 2006). Nevertheless, firms open up their knowledge stocks to volunteers with varied restrictions (Pénin 2007). For example, when sponsoring OSS projects, firms often blend open and proprietary source code within their products and choose to share some but not all of the software with the community under open source licenses (Henkel 2006, West 2003).

Firms that share extensive knowledge about development processes and source code can trigger reciprocal behavior from community members (Blau 1964) and attract volunteers who write and test programs, debug code, and enhance the firm’s services (Dahlander and Magnusson 2005). Knowledge sharing by a sponsoring firm provides participants with access to software code that they can use directly or improve for future usage. With additional documentation or technical specifications, volunteers can write new and test existing programs more easily. Providing developers access to sufficient information has been shown to increase contribution levels fivefold (Boudreau 2010) because support from the sponsoring firm in software architecture, source code, development plans, tasks, and relevant documentation enables and encourages volunteers to contribute (Eisenberger et al. 1990). Indeed, when participants perceive the sponsoring firm as openly sharing knowledge, they are more inclined to reciprocate (Lakhani and von Hippel 2003, Wu et al. 2007). Conversely, firms that constrain knowledge sharing deprive volunteers of important technical information, limit their understanding of software architecture and tasks, and underutilize their specialized skills.

Incorporating volunteer participants’ input constitutes another important aspect of openness. In unsponsored projects, developers become active participants and rise through an informal hierarchy by demonstrating their coding skills (Stewart 2005). In sponsored projects, firms grant only certain participants the right to alter a project’s official source code or to conduct other core activities. As such, firms differ not only in the extent to which they supply communities with information but also in the opportunities that they offer community members to influence a project’s development (West and O’Mahony 2008).

The more participants find themselves capable of influencing the end product, the higher their motivation to contribute to the making of that product. In the OSS context, this logic was tested by Hertel et al. (2003), who found that a higher perceived impact of one’s contributions led to increased efforts. In contrast, performance motivation deteriorates sharply when individuals perceive that their contribution does not matter or cannot be identified, even if they value the collective goals (Hertel et al. 2003). When a firm allows volunteers opportunities to influence the decision-making process of the project, or to adapt the source code for their own use, the volunteers experience a sense of autonomy. According to the self-determination framework, autonomy is a major component of intrinsic motivation (Hackman and Oldham 1980), whereas perceived external control exerts a negative impact on intrinsic interest in a task (Deci and Ryan 1985, Frey and Jegen 2001). Not surprisingly, empirical evidence demonstrates that volunteer participants tend to shy away from projects heavily controlled by an external party (Schroer and Hertel 2009, Shah 2006). Based on this background, we infer that the perceived openness of a sponsoring firm, both in terms of providing knowledge to and embracing input from volunteer participants, bolsters volunteer participants’ intrinsic motivation to engage in OSS projects.

<sup>Hypothesis</sup> <sup>2.</sup> The perceived openness of a sponsoring firm has a direct positive effect on the intrinsic motivation of the volunteer participants.

## Social Identification

Current research in OSS development recognizes OSS as a social practice and explains how it engages numerous volunteer participants (Fang and Neufeld 2009, von Krogh et al. 2012). This recent theoretical advancement leads us to expect that perceived community-based credibility and openness influence participants’ intrinsic motivation through a process of social identification. Social identity theory (Turner and Oakes 1986) proposes that individuals develop social identification with a group by categorizing themselves. The desire to feel connected to social groups is a basic human need, which has been proven powerful in work contexts by extensive research on “organizational commitment” (Allen and Meyer 1996) and “organizational identification” (Van Dick et al. 2006). People with higher commitment usually exhibit stronger motivation and greater engagement with the organization because they feel a strong emotional connection to it (Allen and Meyer 1996). Strong identification is also linked to feelings of obligation to support a social entity. Thus, people with high levels of identification with an organization tend to provide more support, as they consider belonging to the organization part of their social identity, so much so that the success of the organization increases their self-esteem (Van Dick et al. 2006). In a similar vein, Dutton et al. (1994) argued that a critical determinant of voluntary contributions is whether one identifies with and feels personally connected to the cause of an organization. In sum, the motivational and behavioral consequences of identification with a social group are generally positive.

The process of social identification in OSS communities is not likely to be identical to that in traditional organizations. Developing emotional bonds with and commitment to such communities is bound to be challenging because many traditional ways of establishing social connections are compromised by spatial distance and virtual communication. Nevertheless, mechanisms that foster social identification are present in the OSS context, and they manifest in such ways as sympathy and common identity, reduced uncertainty (Hogg and Terry 2000), shared standards of excellence (von Krogh et al. 2012), and feelings of similarity in terms of values and norms (Fiol and O’Connor 2005). As a result, many volunteers identify themselves with a community as, for example, “free” and “open source” developers (Stewart and Gosain 2006).

The motivational effect of social identification has received some support from studies on OSS and other online communities (Bagozzi and Dholakia 2006, Dholakia et al. 2004, Hertel et al. 2003). Specifically, Lakhani and Wolf (2005) showed that the strong identification of OSS developers with a “hacker community” is a crucial source of obligation. Since not all tasks are fun and enjoyable (i.e., user support), often it is the sense of responsibility derived from social identification that motivates volunteer participants to carry out mundane activities. Similarly, Bateman et al. (2011) found that affective commitment to an online community drives such engagement as posting replies and moderating discussions, pointing to the importance of emotional attachment and community identification.

<sup>Hypothesis</sup> <sup>3.</sup> Social identification with the OSS community sponsored has a direct positive effect on the intrinsic motivation of the volunteer participants.

Social identification can be strengthened by the perceived community-based credibility and openness of the sponsoring firm. Volunteer participants consider it beneficial to identify with a community initiated and supported by a credible sponsor (Amiot and Sansfaçon 2011, Simpson 2006). When the sponsoring firm is perceived as having high expertise, individuals will improve their self-worth through associating with this particular social group (Tajfel and Turner 1979). It also becomes attractive for volunteer participants to consider the firm’s employees and other community members a relevant and important “in-group.” When a firm has little credibility in the community, individuals outside the firm tend to be suspicious about hidden motives for its sponsorship and are more likely to perceive the firm’s actions negatively (Goldsmith et al. 2000). Such suspicions and mistrust will lower the willingness of volunteer participants to identify with the sponsored communities (Simpson 2006).

Through being open, sponsoring firms could reduce the physical and psychological distance between them and volunteer participants and, thus, facilitate social identification. By communicating their plans, sharing knowledge, and providing access to OSS projects, sponsoring firms offer volunteer participants additional opportunities to identify with the project. For example, providing access to new source code for the project makes participants feel more included (West and O’Mahony 2008). Obtaining access to a project’s important resources also signifies that a participant has become part of the “core team” of a project (Dahlander and O’Mahony 2011). Volunteer participants who are rewarded in this way are likely to experience increased feelings of self-worth because of the sharper distinction between “us,” the core team members, and “them,” the regular contributors with no access rights (Hertel et al. 2003, see also Kreiner et al. 2006). Additionally, giving volunteer participants opportunities to influence decision making reduces their uncertainty about the future of the project (Fiol and O’Connor 2005), which leads to greater identification with the community. Building on social identity theory and empirical evidence from the social practices of OSS, we propose the following:

<sup>Hypothesis</sup> <sup>4.</sup> The perceived community-based credibility of a sponsoring firm has an indirect positive effect on volunteer participants’ intrinsic motivation through their social identification with the community.

<sup>Hypothesis</sup> <sup>5.</sup> The perceived openness of a sponsoring firm has an indirect positive effect on volunteer participants’ intrinsic motivation through their social identification with the community.

## Method

## Sample and Procedure

Voluntary participants in two firm-sponsored OSS projects, Maemo and OpenMoko, constituted our sample. These two OSS projects were strategically chosen because they were firm sponsored and sustained by substantial voluntary contributions. Maemo was initiated by Nokia to develop an operating system for the company’s then new Internet tablet. Much of Nokia’s underlying software was open to the community, yet some end-user applications and hardware drivers remained restricted. Volunteer participants were able to report bugs in a tracking system and contribute source codes to fix them. OpenMoko was set up by FIC, a Taiwanese mobile phone manufacturer, to develop a new smartphone. The hardware schematic for the mobile phone—its blueprint— was made public under an open source license, which allowed developers to build their own “Open-Mokos.” The two projects shared an important structure: while providing and controlling the core source code repository, both sponsoring firms offered technical infrastructure that hosted voluntary contributions. Volunteer participants were able to provide feedback through mailing lists and bug trackers and develop modules or software using the source codes made available to them and, as a result, lively communities of volunteers had emerged.

With endorsement by the sponsors, we downloaded participants’ email addresses from the project database. Clearly duplicate (e.g., work and private) email addresses were removed. This process yielded 2,151 unique addresses from the Maemo community and 2,593 unique addresses from the OpenMoko community. We then sent out email invitations with a link to our web-based survey to all identified members of the two project communities. As an incentive, we offered to raffle off four Internet tablet devices. After three weeks and two reminders, 1,233 complete responses were received (Maemo: 429, OpenMoko: 804), rendering a response rate of 27.9%. In the survey, we asked participants whether they were employed or contracted by the sponsoring firm. Given our focus on volunteer participants, employees and subcontractors (Maemo: 61, OpenMoko: 21) were excluded.<sup>1</sup> Respondents came from 64 countries, with a significant portion from the United States (22.85%) and Germany (14.34%). The average age of the respondents was 32 (s.d. = 9020), and most had a bachelor’s degree (73.24%).

## Measures

Given an absence of suitable scales for intrinsic motivation to engage in OSS and for the perceived community-based credibility and openness of the sponsoring firm, we developed new measures. We based the items on an extensive literature review and a discussion among a panel of experts (consisting of management professors, doctoral students, and OSS practitioners) to ensure content validity. A pilot test was administered to 30 developers at a Maemo conference in Berlin. Based on their feedback, we refined the wording of several items to better adapt them to the OSS context. All measures employed a five-point Likert scale (1 = strongly disagree, 5 = strongly agree).

Intrinsic Motivation. Despite the long tradition of research on intrinsic motivation, there is no consensus regarding the definition of this construct. Given its central role in the current study, we decided to adopt a broader approach by considering enjoyment of the task at hand, feedback from others, and learning (Deci and Ryan 1985). We defined intrinsic motivation in the OSS context as the desire to engage in OSS for its own sake rather than to acquire material or careerrelated benefits and developed nine items that tapped into the OSS context. An example is “I contribute to the community because it is fun to contribute.”

Perceived Community-Based Credibility. Credibility results from the perceived technical expertise as well as the trustworthiness of the sponsoring firm (Newell and Goldsmith 2001). A sponsoring organization can develop credibility within an OSS community by demonstrating to developers its ability, benevolence, and integrity (Mayer et al. 1995). We developed six items to gauge community-based credibility, covering technical ability (e.g., “Nokia/OpenMoko’s employees are technically skilled”), benevolence (e.g., “Nokia/OpenMoko supports the community”), and integrity (“I trust Nokia/OpenMoko as a company.”).

Perceived Openness. The openness of a firm in OSS projects has two dimensions: (1) revealing sufficient information on technical details and future plans for the project, and (2) welcoming input from participants in terms of source code and suggestions (Waugh and Metcalfe 2007). We developed seven items to capture these two aspects. “I can get commit access to the source code repository if I want to” represented the first dimension, and “My opinion is sufficiently taken into account when decisions regarding the project are made” represented the second.

Social Identification. FromAllen andMeyer’s (1990) measurement scale of affective commitment, we adapted four items that were designed to gauge the social identification aspect of organizational commitment. Both affective commitment and social identification refer to individuals’ emotional connection with a community (Van Dick et al. 2006, Meyer et al. 2006). Given that volunteer participants were not officially affiliated with the sponsoring firm, the reference point was changed from a specific organization to an OSS project. An example is “I feel emotionally attached to Maemo/OpenMoko.”

Control Variables. A dummy variable (Project Type: 0 = OpenMoko, 1 = Maemo) was created to capture the unobservable variance between Maemo and OpenMoko. Individual differences in terms of age, nationality, and education were also controlled for.

## Validation of Scales

We followed a robust procedure recommended by Hinkin (1998) to examine the validity of the measurement scales we developed. We randomly split the initial sample into two subsamples and ran an exploratory factor analysis for item reduction using one subsample. Only items that loaded on a single appropriate factor and with loadings greater than 0.40 were retained (Ford et al. 1986). The final items for each measures are shown in Table 1. We further established the unidimensionality of these scales by conducting a confirmatory factor analysis with the other subsample (Segars 1997). Exploratory and confirmatory factor loadings for newly developed scales are presented in Appendix A. The total sample was used for further analysis.

Table 1 Final Measurement Scale Items, Factor Loadings, and Reliabilities

<table><tr><td>Constructs</td><td>Item</td><td>Description</td><td>Factor loading</td><td>Scale CR</td></tr><tr><td rowspan="5">Intrinsic motivation</td><td>moti1</td><td>I contribute to the Maemo/OpenMoko community because I enjoy helping others.</td><td>0.52***</td><td>0.78</td></tr><tr><td>moti2</td><td>I contribute to the Maemo/OpenMoko community because I enjoy working in this community.</td><td>0.78***</td><td></td></tr><tr><td>moti3</td><td>I contribute to the Maemo/OpenMoko community because it is fun to contribute.</td><td>0.65***</td><td></td></tr><tr><td>moti4</td><td>I contribute to the Maemo/OpenMoko community because I appreciate it if others value my contributions.</td><td>0.45***</td><td></td></tr><tr><td>moti5</td><td>I contribute to the Maemo/OpenMoko community because I learn a lot participating in the community.</td><td>0.61***</td><td></td></tr><tr><td rowspan="5">Perceived openness</td><td>open1</td><td>Nokia/OpenMoko publishes sufficient documentation.</td><td>0.55***</td><td>0.73</td></tr><tr><td>open2</td><td>I understand how the company makes decisions regarding the Maemo/OpenMoko project.</td><td>0.62***</td><td></td></tr><tr><td>open3</td><td>My code contributions are taken up in the official software release.</td><td>0.48***</td><td></td></tr><tr><td>open4</td><td>I can get commit access for the project&#x27;s source code repository if I want to.</td><td>0.46***</td><td></td></tr><tr><td>open5</td><td>My opinion is sufficiently taken into account when the company makes decisions regarding the Maemo/OpenMoko project.</td><td>0.65***</td><td></td></tr><tr><td rowspan="5">Perceived community-based credibility</td><td>cred1</td><td>Nokia/OpenMoko&#x27;s employees working on the Maemo/OpenMoko project are technically skilled.</td><td>0.52***</td><td>0.81</td></tr><tr><td>cred2</td><td>Nokia/OpenMoko&#x27;s open source activities are well managed.</td><td>0.64***</td><td></td></tr><tr><td>cred3</td><td>Nokia/OpenMoko would be a good company to work for.</td><td>0.63***</td><td></td></tr><tr><td>cred4</td><td>I trust Nokia/OpenMoko as a company.</td><td>0.69***</td><td></td></tr><tr><td>cred5</td><td>Nokia/OpenMoko supports the community.</td><td>0.71***</td><td></td></tr><tr><td rowspan="4">Social identification</td><td>iden1</td><td>I identify with the Maemo/OpenMoko community.</td><td>0.73***</td><td>0.86</td></tr><tr><td>iden2</td><td>I feel that the project&#x27;s problems are my own.</td><td>0.73***</td><td></td></tr><tr><td>iden3</td><td>I feel emotionally attached to the Maemo/OpenMoko project.</td><td>0.79***</td><td></td></tr><tr><td>iden4</td><td>The Maemo/OpenMoko project has a great deal of personal meaning for me.</td><td>0.86***</td><td></td></tr></table>

Note. CR1 Composite reliability.  
<sup>∗∗∗</sup>p < 00001.

## Results

The research model was tested using LISREL 9.1, a covariance-based structural equation modeling technique (Jöreskog and Sörbom 1996). We employed a two-step approach (Anderson and Gerbing 1988) to evaluate the quality of the measurement and structural models. A combination of fit indices (Kline 2011), including the chi-square statistic, the root mean square error of approximation (RMSEA), the comparative fit index (CFI), and the standardized root mean square residual (SRMR), was considered to determine model fit.

## Measurement Model Fit and Common Method Variance

In the first step, we assessed measurement model fit by loading all indicators to their respective constructs in a CFA model. CFA results indicated an excellent fit of the model (x<sup>2</sup> = 471077, d.f. = 146, p < 0001; RMSEA = 0004; CFI = 0095; SRMR = 0004). All factor loadings were larger than 0.44 and significant $( p < 0 . 0 0 1 ;$ ; see Table 1). The reliability of each measurement scale was assessed using composite reliability, in which a value of 0.70 or greater indicates a reliable scale (Fornell and Larcker 1981). Table 1 shows the composite reliability of all constructs. Discriminant validity was evaluated using the square root of average variance extracted (AVE).

As shown in Table 2, all AVE values exceeded 0.50, and for most constructs this value was greater than the correlations between constructs, demonstrating good discriminant validity (Fornell and Larcker 1981). Since the square root of AVE of perceived openness (0.56) was smaller than the correlation between perceived openness and credibility (0.65), we further tested a CFA model that combined these two constructs into one factor. The measurement model fit dropped significantly $( \Delta \mathrm { d . f . } = 3 , \ \Delta x ^ { 2 } = 2 6 7 . 5 7 ,$ p < 00001) after merging the two constructs, confirming that they should be treated as distinct.

Being aware that common method variance (CMV) presents a potential threat to self-reported data, we adopted procedural remedies such as creating counterbalancing question order and ensuring confidentiality to reduce evaluation apprehension (Podsakoff et al. 2003). We also tested for the existence of CMV by analyzing whether the model fit improved as the complexity of the research model increased—a technique that many consider more effective than Harman’s onefactor test (Iverson and Maguire 2000, Korsgaard and Roberson 1995, Podsakoff et al. 2003). The single-factor model fit the data significantly worse than the fourfactor measurement model $( \Delta \mathrm { d . f . } = 6 , \Delta = 1 , 9 7 4 . 3 0 _ { \cdot }$ $p < 0 . 0 0 1 )$ , indicating that CMV was unlikely to be a serious problem. In addition, we employed the latent marker technique to assess the extent that CMV biased the parameter estimates (Antonakis et al. 2010, Podsakoff et al. 2012). We first ran a CFA model with a latent marker that consisted of three items exhibiting the lowest correlations with the substantive variables (Richardson et al. 2009). The goal of the initial CFA model was to obtain the factor loadings of the three items on the latent marker. Next, the latent marker was included in a structural model, where relationships among substantive variables were as specified by the study hypotheses. The factor loadings of its composite items were fixed to the values obtained in the initial CFA model, whereas the factor loadings of all other items on this latent marker were estimated. The correlations between the latent marker and other substantive variables were set to zero under the orthogonal assumption (see Williams et al. 2010 for a review). The parameter estimates of the latter structural model were then calculated accounting for the presence of method effects.

Table 2 Descriptive Statistics and Correlations

<table><tr><td></td><td>Mean</td><td>S.d.</td><td>1</td><td>2</td><td>3</td><td>4</td></tr><tr><td>1. Intrinsic motivation</td><td>4.05</td><td>0.51</td><td>0.61</td><td></td><td></td><td></td></tr><tr><td>2. Social identification</td><td>3.30</td><td>0.83</td><td>0.55***</td><td>0.78</td><td></td><td></td></tr><tr><td>3. Perceived openness</td><td>3.08</td><td>0.52</td><td>0.42***</td><td>0.43***</td><td>0.56</td><td></td></tr><tr><td>4. Perceived community-based credibility</td><td>3.72</td><td>0.57</td><td>0.51***</td><td>0.46***</td><td>0.65***</td><td>0.64</td></tr></table>

Note. N = 11072, list-wise; leading diagonal shows the square root of average variance extracted of constructs.  
<sup>∗∗∗</sup>p < 00001.

## Structural Model Fit and Hypothesis Test

Having established the fit of the measurement model, we proceeded to evaluate the structural model. The hypothesized model (model 1), a partial mediation model specifying both the direct and indirect effects of perceived firm attributes, rendered a good fit to the data $( x ^ { 2 } = 4 3 9 . 5 6 , \mathrm { ~ d . f . } = 1 4 6 , p < 0 . 0 0 1 ; \mathrm { ~ R M S E A } =$ $0 . 0 4 ; \mathrm { C F I } = 0 . 9 5 ; \mathrm { S R M R } = 0 . 0 4 )$ . As shown in Figure 1, both the perceived credibility $( \beta = 0 . 3 5 , ~ p < 0 . 0 0 1 )$

Figure 1 Standardized Path Coefficients  
![](/api/attachments/GN55BXFS/fulltext/images/a141980aaba15e812fb4e9a212e70837934e02ccb888254046fde9d4ea99c8be.jpg)

Table 3 Comparison of Model Results Without and With Marker

<table><tr><td rowspan="2">Path</td><td colspan="2">Model without marker</td><td colspan="2">Model with marker</td></tr><tr><td>Coef.</td><td>P &gt; |z|</td><td>Coef.</td><td>P &gt; |z|</td></tr><tr><td>Openness → Social identification</td><td>0.15</td><td>0.004</td><td>0.12</td><td>0.02</td></tr><tr><td>Social identification → Intrinsic motivation</td><td>0.39</td><td>0.00</td><td>0.36</td><td>0.00</td></tr><tr><td>Community-based credibility → Intrinsic motivation</td><td>0.29</td><td>0.00</td><td>0.30</td><td>0.00</td></tr><tr><td>Openness → Intrinsic motivation</td><td>0.06</td><td>0.16</td><td>0.03</td><td>0.32</td></tr></table>

and openness $( \beta = 0 . 1 5 , ~ p < 0 . 0 1 )$ of a sponsoring firm had significantly positive impacts on volunteers’ social identification with the sponsored community, which in turn led to increased intrinsic motivation $( \beta = 0 . 3 9 , p < 0 . 0 0 1 ) . ^ { 2 }$ Perceived credibility also directly enhanced volunteer participants’ intrinsic motivation $( \beta = 0 . 2 9 , p < 0 . 0 0 1 )$ . Contrary to expectations, perceived openness did not have a direct impact on intrinsic motivation $( \beta = 0 . 0 6 , \ p = \mathrm { n } . s . ) . ^ { 3 }$

We then examined the direct and indirect effects of the two perceived firm attributes. As shown in Table 4 both the direct $( \beta = 0 . 2 7 , ~ p < 0 . 0 0 1 )$ and indirect $( \beta = 0 . 1 3 , ~ p < 0 . 0 0 1 )$ effects of perceived credibility on intrinsic motivation were significant. In contrast, perceived openness had a significant indirect effect $( \beta = 0 . 0 4 , \ p < 0 . 0 5 )$ through social identification, yet its direct effect on intrinsic motivation was not significant $( \beta = 0 . 0 4 , p = \mathrm { n . s . } )$ . The direct effect of social identification on intrinsic motivation was significantly positive $( \beta = 0 . 2 1 , ~ p < 0 . 0 0 1 )$ . Considering the path coefficients, model comparison, and direct and indirect effect sizes, Hypotheses 1, 3, 4, and 5 were supported, whereas Hypothesis 2 was not.

Table 4 Total, Direct, and Indirect Effect Sizes

<table><tr><td></td><td>Standard coefficient</td><td>Standard error</td><td>z</td><td>P &gt; |z|</td></tr><tr><td colspan="5">Total effect on intrinsic motivation</td></tr><tr><td>Perceived community-based credibility</td><td>0.39</td><td>0.06</td><td>6.49</td><td>0.00</td></tr><tr><td>Perceived openness</td><td>0.08</td><td>0.04</td><td>1.87</td><td>0.06</td></tr><tr><td colspan="5">Direct effect on intrinsic motivation</td></tr><tr><td>Perceived community-based credibility</td><td>0.27</td><td>0.06</td><td>4.80</td><td>0.00</td></tr><tr><td>Perceived openness</td><td>0.04</td><td>0.04</td><td>1.00</td><td>0.33</td></tr><tr><td>Social identification</td><td>0.21</td><td>0.02</td><td>8.74</td><td>0.00</td></tr><tr><td colspan="5">Indirect effect on intrinsic motivation</td></tr><tr><td>Perceived community-based credibility</td><td>0.13</td><td>0.02</td><td>5.20</td><td>0.00</td></tr><tr><td>Perceived openness</td><td>0.04</td><td>0.02</td><td>2.50</td><td>0.01</td></tr></table>

## Post Hoc Analysis

We further compared model 1 with the next two theoretically plausible models: model 2, which removed the path from perceived openness to intrinsic motivation; and model 3, which removed the path from perceived community-based credibility to intrinsic motivation. Fit indices of these models are shown in Table 5. Model $2 \ ( x ^ { 2 } = 4 4 0 . 5 2 , \ d . \mathrm { f . } = 1 4 7 , \ p < 0 . 0 0 1$ RMSEA = 0004; CFI = 0095; SRMR = 0004), which represents a partial mediation between perceived community-based credibility and intrinsic motivation and a full mediation between perceived openness and intrinsic motivation, did not fit the data worse than the hypothesized model (ã d0f0 = 1, $\Delta x ^ { 2 } = 0 . 9 6$ , p = n0s0). Based on the principle of parsimony, model 2 should be adopted.

Since a sponsoring firm’s openness, when perceived by volunteers, consists of both a willingness to open up to the community and to incorporate input from the community, these two interrelated dimensions call for further exploration. We thus split perceived openness into the two respective dimensions and tested them as independent constructs in a new model. In the new model, neither opening up to the community ( = 0031, p = n.s.) nor incorporating the community’s input ( = −0013, p = n.s.) alone affected social identification significantly. Similarly, regarding intrinsic motivation, neither opening up to the community $( \beta = - 0 . 3 8 , \ p = \mathrm { n } . s . )$ nor incorporating the community’s input $( \beta = 0 . 4 1 , \ p = \mathtt { n . s . } )$ had a significant influence. These preliminary results seem to suggest that for openness to have an impact on social identification or intrinsic motivation, both of its dimensions are indispensible.

Table 5 Comparison of Structural Models

<table><tr><td>Model</td><td>Description</td><td> $x^{2}$ </td><td>d.f.</td><td>RMSEA</td><td>CFI</td><td>SRMR</td></tr><tr><td>1</td><td>Hypothesized model</td><td>439.56***</td><td>146</td><td>0.04</td><td>0.95</td><td>0.04</td></tr><tr><td>2</td><td>Removed a path between perceived openness and motivation</td><td>440.52***</td><td>147</td><td>0.04</td><td>0.95</td><td>0.04</td></tr><tr><td>3</td><td>Removed a path between perceived community-based credibility and motivation</td><td>465.28***</td><td>147</td><td>0.05</td><td>0.95</td><td>0.04</td></tr></table>

<sup>∗∗∗</sup>p < 00001.

## Discussion

Based on survey data from two firm-sponsored OSS communities, we found support for a structural model that links volunteer participants’ perception of the firm’s community-based credibility and openness to their social identification with the sponsored OSS community, which in turn influences their intrinsic motivation. The perceived community-based credibility of a sponsoring firm can enhance volunteers’ intrinsic motivation, both directly and indirectly through social identification with their community. This result echoes previous research that associates the intrinsic motivation of OSS community participants with desirable characteristics of sponsorship (Dahlander and Magnusson 2005, David and Shapiro 2008, Lakhani and von Hippel 2003). Understandably, volunteers value the trustworthiness and openness of a sponsor (Kerr 1983, Stewart et al. 2006). We expand the literature on OSS sponsorship to show that not just nonfirm sponsors, but also firms, can be attractive sponsors for volunteer developers when exhibiting these attributes.

Perhaps a more intriguing finding of the present study lies in the fact that perceived openness does not seem to directly enhance volunteers’ intrinsic motivation. Although the sponsoring firm may generate energy, interest, and creativity from volunteer participants by being open (West 2003), unless these participants truly identify with the sponsored community and gear these positive forces towards OSS development, it is hard to predict their intrinsic motivation to contribute to a project. Our results suggest that the positive impact of perceived openness has to go through social identification, emphasizing that the motivational implications of a sponsoring firm’s openness depend on the social practice of OSS development. Via sharing knowledge and practicing inclusive decision making, a sponsor can help generate tight-knit communities that house the social practice of OSS development. Eventually, volunteers who “internalize” the OSS community’s prosperity as their own success are those who are willing to go the extra mile (Lakhani and von Hippel 2003).

The current study contributes to a growing literature on participants’ motivation and OSS sponsorship (Henkel 2009, Shah 2006, Stewart et al. 2006). First, it expands existing research by showing that in addition to boosting extrinsic motivation through financial rewards and career opportunities (Ke and Zhang

2010), the sponsoring firm can also enhance participants’ intrinsic motivation. In both projects examined, the volunteer participants’ contributions to the development of the mobile device software were extensive. Apparently, certain aspects of firm sponsorship, for example, community-based credibility and openness, when perceived by developers could draw contributions from volunteers who have traditionally been believed to be resistant to firm sponsorship. To our knowledge, this study is the first to reveal the positive impact of specific firm attributes on volunteer participants’ intrinsic motivation in OSS projects.

Second, this study contributes to the broader literature on collaborative open innovation (von Hippel and von Krogh 2003, Kuk 2006) by exploring how firms and developers form a symbolic relationship for innovation. This study takes the first step in substantiating an understanding that perceived firm attributes shape the extent to which participants identify with the community—a strong drive to allocate collaborative effort for open innovation. In integrating a social practice perspective, the study also delineates a process through which firm policies and actions intertwine with community engagement to impact the willingness to reciprocate.

The practical implications of our findings are not trivial. Firms seeking voluntary contributions to their OSS projects will benefit from communicating a credible and open image within the developer communities (Dutton and Dukerich 1991, Dutton et al. 1994). Note that it is one thing to establish credibility among the general public; it is another to establish credibility among OSS developers. Although firms usually build general public credibility by spending on advertising or public relations, establishing community-based credibility requires long-term commitment and substantial investments in technical capabilities to develop OSS. As our research clearly demonstrates, firms wooing voluntary participants must build such community-based credibility. Firms can cultivate a credible reputation inside a community by, for instance, providing continuous technical assistance and consistently protecting the community’s open source software and other public goods. Another effective way could be to identify and work with leading volunteers who understand the project’s goals, know the software in question, have experience from similar projects, and work with other communities whose software products are valuable to the focal project. Such leading figures may help the sponsoring firm build the necessary momentum in the project to attract newcomers to the community. Besides presenting the firm to potential contributors, these volunteers can also provide insights on policies and practices valued by their peers.

OSS sponsoring firms should also realize that establishing openness within the community requires opening up a two-way channel, which not only supplies information and knowledge but also incorporates volunteer participants’ input. As a unique gift economy, OSS communities host individuals who are as interested in giving as in receiving gifts (Kollock 1999, Rossi 2006). Firms might initially be reluctant to open themselves up to the influence of outside participants, because of the increased effort required to reduce community entry barriers, the difficulty of weighing business secrets and plans against transparency, and the organizational inertia that needs to be overcome to relent some control (Stuermer et al. 2009). However, the knowledge repertoire of a sponsor might be drained without constant replenishment. Furthermore, it is not sufficient for firms to simply increase their openness. Firms must invest to build a tight-knit community with which volunteer participants can identify, thus motivating them to capitalize on the knowledge shared and the opportunities offered there. Echoing a recent conceptualization of “selective revealing” of organizational knowledge (Alexy et al. 2013), we recommend that sponsoring firms develop “selective opening” strategies that take into account the types of knowledge to be shared and the cost of coordinating development with community participants, as well as the community’s capacity to absorb new knowledge.

Notwithstanding its theoretical and practical implications, this study has limitations. First, the crosssectional nature of the present study affords limited causal inference. One may speculate that volunteers’ intrinsic motivation in a firm-sponsored project could give rise to favorable perception of the firm, or intrinsic motivation could lead to identification with the community instead of vice versa. It is possible that people might try to justify their behavioral intention by altering perceptions accordingly. However, a large body of accumulated organizational research has established that perceptions of organizational character, such as support (Eisenberger et al. 1990), justice (Colquitt et al. 2001), and inclusiveness (Spreitzer 1996), are predictors of work motivation and motivation to engage in prosocial behaviors outside the work contract. Additionally, voluntary participation in OSS projects resembles collective actions in other domains such as civil rights, labor, and peace movements. Research on collective action has shown that social identification is an antecedent to rather than an outcome of motivation (Kelly 1993). Although the study’s hypotheses are theoretically grounded, they will benefit from a longitudinal design teasing out various influences over time. Future research should also focus on building a process theory of this phenomenon, explaining how individual contributors perceive firm attributes, socialize into the community, and become more or less involved in it.

Second, this study relies on data drawn from a single source (self-reported by the volunteer participants). This design is prone to common method bias, which could potentially inflate the relationships in question (Podsakoff et al. 2003). Besides employing a number of procedural remedies, we compared our model estimates before and after controlling for common method bias (Podsakoff et al. 2012). There was no substantial difference between the two sets of results, yet we are cautious in interpreting the results. The present study is exploratory and serves as a departure point for future research to investigate the motivational implications of perceived firm attributes, ideally backed up by multisource data.

Finally, the study focused on firm attributes perceived by individuals. This approach is appropriate to address our research question on how volunteer participants’ perceptions of the sponsoring firm shape their intrinsic motivation. However, some individuals might expect higher standards of knowledge sharing and accessibility from a dedicated OSS sponsor, such as OpenMoko, than a firm like Nokia, which is known for protecting most of its software through intellectual property rights. Although determining an “objective” degree of openness by comparing sponsoring firms is beyond the scope of this study, future research can employ a multilevel model and investigate a larger sample of OSS projects to examine how “relative openness” shapes “perceived openness.” Studying a mix of projects with different sponsors may also enable future researchers to disentangle the motivational effects of sponsor attributes from those of sponsorship types.

## Conclusion

Voluntary contributions are crucial to the success of OSS projects. In this study, we explored whether volunteers’ perception of firm attributes shaped their intrinsic motivation to contribute to firm-sponsored OSS projects. Our results showed that the perceived openness and community-based credibility of a sponsoring firm strengthened volunteer participants’ social identification with a firm-sponsored community, which in turn enhanced their intrinsic motivation to contribute. We found that whereas the perceived community-based credibility of a sponsoring firm directly reinforced volunteer participants’ intrinsic motivation, perceived openness strengthened intrinsic motivation only with the mediating mechanism of social identification. As the social practice of OSS links the perceptions and motivation of community participants, firms seeking voluntary contributions can benefit from building an engaged community, alongside establishing community-based credibility and opening up to the community.

## Acknowledgments

This research received funding from the Swiss National Science Foundation [Grant 146439]. The authors wish to thank Matthias Stuermer for his research assistance, and Natalia Levina, Sunil Mithas, Hart Posen, as well as three anonymous reviewers for their highly valuable feedback on previous versions of this paper. All three authors contributed equally and authorship is listed at random.

Appendix A. Factor Structures for Developed Scales

<table><tr><td>Scale</td><td>Item</td><td>Subsample 1</td><td>Subsample 2</td></tr><tr><td rowspan="5">Intrinsic motivation</td><td>moti1</td><td>0.62***</td><td>0.65***</td></tr><tr><td>moti2</td><td>0.76***</td><td>0.69***</td></tr><tr><td>moti3</td><td>0.74***</td><td>0.72***</td></tr><tr><td>moti4</td><td>0.54***</td><td>0.63***</td></tr><tr><td>moti5</td><td>0.58***</td><td>0.63***</td></tr><tr><td rowspan="5">Perceived openness</td><td>open1</td><td>0.64***</td><td>0.63***</td></tr><tr><td>open2</td><td>0.75***</td><td>0.71***</td></tr><tr><td>open3</td><td>0.72***</td><td>0.73***</td></tr><tr><td>open4</td><td>0.76***</td><td>0.77***</td></tr><tr><td>open5</td><td>0.78***</td><td>0.77***</td></tr><tr><td rowspan="5">Perceived credibility</td><td>cred1</td><td>0.61***</td><td>0.65***</td></tr><tr><td>cred2</td><td>0.71***</td><td>0.64***</td></tr><tr><td>cred3</td><td>0.58***</td><td>0.62***</td></tr><tr><td>cred4</td><td>0.58***</td><td>0.62***</td></tr><tr><td>cred5</td><td>0.71***</td><td>0.71***</td></tr></table>

<sup>∗∗∗</sup>p < 00001.

Appendix B. Comparison of Factor Loadings Without and With Marker

<table><tr><td>Scale</td><td>Item</td><td>Model without marker</td><td>Model with marker</td></tr><tr><td rowspan="5">Intrinsic motivation</td><td>moti1</td><td>0.52***</td><td>0.47***</td></tr><tr><td>moti2</td><td>0.78***</td><td>0.76***</td></tr><tr><td>moti3</td><td>0.65***</td><td>0.59***</td></tr><tr><td>moti4</td><td>0.45***</td><td>0.37***</td></tr><tr><td>moti5</td><td>0.61***</td><td>0.55***</td></tr><tr><td rowspan="5">Perceived openness</td><td>open1</td><td>0.55***</td><td>0.54***</td></tr><tr><td>open2</td><td>0.62***</td><td>0.61***</td></tr><tr><td>open3</td><td>0.48***</td><td>0.46***</td></tr><tr><td>open4</td><td>0.46***</td><td>0.44***</td></tr><tr><td>open5</td><td>0.65***</td><td>0.63***</td></tr><tr><td rowspan="5">Perceived credibility</td><td>cred1</td><td>0.52***</td><td>0.50***</td></tr><tr><td>cred2</td><td>0.64***</td><td>0.63***</td></tr><tr><td>cred3</td><td>0.63***</td><td>0.59***</td></tr><tr><td>cred4</td><td>0.69***</td><td>0.68***</td></tr><tr><td>cred5</td><td>0.71***</td><td>0.71***</td></tr><tr><td rowspan="4">Social identification</td><td>iden1</td><td>0.73***</td><td>0.68***</td></tr><tr><td>iden2</td><td>0.73***</td><td>0.71***</td></tr><tr><td>iden3</td><td>0.79***</td><td>0.75***</td></tr><tr><td>lden4</td><td>0.86***</td><td>0.83***</td></tr></table>

<sup>∗∗∗</sup>p < 00001.

∗p < 0005; ∗∗p < 0001; ∗∗∗p < 00001.

<table><tr><td></td><td>cred1</td><td>cred2</td><td>cred3</td><td>cred4</td><td>cred5</td><td>open1</td><td>open2</td><td>open3</td><td>open4</td><td>open5</td><td>iden1</td><td>iden2</td><td>iden3</td><td>iden4</td><td>moti1</td><td>moti2</td><td>moti3</td><td>moti4</td><td>moti5</td></tr><tr><td>cred1</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>cred2</td><td>0.32***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>cred3</td><td>0.35***</td><td>0.42***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>cred4</td><td>0.35***</td><td>0.41***</td><td>0.47***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>cred5</td><td>0.37***</td><td>0.49***</td><td>0.40***</td><td>0.50***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>open1</td><td>0.25***</td><td>0.33***</td><td>0.19***</td><td>0.27***</td><td>0.34***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>open2</td><td>0.22***</td><td>0.34***</td><td>0.27***</td><td>0.30***</td><td>0.33***</td><td>0.36***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>open3</td><td>0.11***</td><td>0.11***</td><td>0.13***</td><td>0.13***</td><td>0.16***</td><td>0.24***</td><td>0.25***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>open4</td><td>0.12***</td><td>0.13***</td><td>0.11***</td><td>0.17***</td><td>0.19***</td><td>0.25***</td><td>0.24***</td><td>0.34***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>open5</td><td>0.20***</td><td>0.29***</td><td>0.26***</td><td>0.30***</td><td>0.29***</td><td>0.30***</td><td>0.40***</td><td>0.38***</td><td>0.32***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iden1</td><td>0.24***</td><td>0.19***</td><td>0.30***</td><td>0.33***</td><td>0.27***</td><td>0.20***</td><td>0.22***</td><td>0.19***</td><td>0.15***</td><td>0.20***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iden2</td><td>0.15***</td><td>0.14***</td><td>0.25***</td><td>0.26***</td><td>0.22***</td><td>0.19***</td><td>0.24***</td><td>0.19***</td><td>0.20***</td><td>0.20***</td><td>0.52***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iden3</td><td>0.20***</td><td>0.15***</td><td>0.26***</td><td>0.26***</td><td>0.22***</td><td>0.19***</td><td>0.20***</td><td>0.13***</td><td>0.11***</td><td>0.15***</td><td>0.57***</td><td>0.57***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>iden4</td><td>0.22***</td><td>0.18***</td><td>0.29***</td><td>0.30***</td><td>0.24***</td><td>0.21***</td><td>0.24***</td><td>0.17***</td><td>0.20***</td><td>0.21***</td><td>0.61***</td><td>0.64***</td><td>0.69***</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>moti1</td><td>0.10***</td><td>0.16***</td><td>0.17***</td><td>0.14</td><td>0.19***</td><td>0.16***</td><td>0.13***</td><td>0.09**</td><td>0.10**</td><td>0.17***</td><td>0.20***</td><td>0.16***</td><td>0.16***</td><td>0.17***</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>moti2</td><td>0.20***</td><td>0.29***</td><td>0.26***</td><td>0.31***</td><td>0.30***</td><td>0.17***</td><td>0.22***</td><td>0.15</td><td>0.16***</td><td>0.24***</td><td>0.42***</td><td>0.29***</td><td>0.33***</td><td>0.36***</td><td>0.36***</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>moti3</td><td>0.16***</td><td>0.18***</td><td>0.19***</td><td>0.18***</td><td>0.19</td><td>0.14***</td><td>0.14***</td><td>0.10**</td><td>0.07*</td><td>0.15***</td><td>0.30***</td><td>0.18***</td><td>0.25***</td><td>0.26***</td><td>0.40***</td><td>0.51</td><td>1.00</td><td></td><td></td></tr><tr><td>moti4</td><td>0.07*</td><td>0.06</td><td>0.12***</td><td>0.11***</td><td>0.13***</td><td>0.07*</td><td>0.06</td><td>0.11**</td><td>0.03</td><td>0.07*</td><td>0.20***</td><td>0.13***</td><td>0.17***</td><td>0.15***</td><td>0.35***</td><td>0.29***</td><td>0.36***</td><td>1.00</td><td></td></tr><tr><td>moti5</td><td>0.19***</td><td>0.22***</td><td>0.21***</td><td>0.22***</td><td>0.21***</td><td>0.12***</td><td>0.14***</td><td>0.12***</td><td>0.05</td><td>0.16***</td><td>0.35***</td><td>0.23***</td><td>0.27***</td><td>0.29***</td><td>0.28***</td><td>0.50***</td><td>0.36***</td><td>0.24***</td><td>1.00</td></tr></table>

## References

Alexy O, George G, Salter AJ (2013) Cui bono? The selective revealing of knowledge and its implications for innovative activity. Acad. Management Rev. 38(2):270–291.

Allen NJ, Meyer JP (1990) The measurement and antecedents of affective, continuance and normative commitment to the organization. J. Occupational Psych. 63(1):1–18.

Allen NJ, Meyer JP (1996) Affective, continuance, and normative commitment to the organization: An examination of construct validity. J. Vocational Behav. 49(3):252–276.

Amiot CE, Sansfaçon S (2011) Motivations to identify with social groups: A look at their positive and negative consequences. Group Dynamics: Theory, Res., Practice 15(2):105–127.

Anderson JC, Gerbing DW (1988) Structural equation modeling in practice: A review and recommended two-step approach. Psych. Bull. 103(3):411–423.

Antonakis J, Bendahan S, Jacquart P, Lalive R (2010) On making causal claims: A review and recommendations. The Leadership Quart. 21(6):1086–1120.

Bagozzi RP, Dholakia UM (2006) Open source software user communities: A study of participation in Linux user groups. Management Sci. 52(7):1099–1115.

Bateman PJ, Gray PH, Butler BS (2011) The impact of community commitment on participation in online communities. Inform. Systems Res. 22(4):841–854.

Bergquist M, Ljungberg J (2001) The power of gifts: Organising social relationships in open source communities. Inform. Systems J. 11(4):305–320.

Bitzer J, Schrettl W, Schröder PJH (2007) Intrinsic motivation in open source software development. J. Comparative Econom. 35(1):160–169.

Blau PM (1964) Exchange and Power in Social Life (Wiley, New York).

Bonaccorsi A, Rossi C (2006) Comparing motivations of individual programmers and firms to take part in the open source movement: From community to business. Knowledge, Tech., Policy 18(4):40–64.

Boudreau K (2010) Open platform strategies and innovation: Granting access vs. devolving control. Management Sci. 56(10): 1849–1872.

Callan MJ, Kay AC, Olson JM, Brar N, Whitefield N (2010) The effects of priming legal concepts on perceived trust and competitiveness, self-interested attitudes, and competitive behavior. J. Experiment. Soc. Psych. 46(2):325–335.

Colquitt J, Conlon D, Wesson M, Porter C, Ng K (2001) Justice at the millennium: A meta-analytic review of 25 years of organizational justice research. J. Appl. Psych. 86(3):425–445.

Cornwell TB, Weeks CS, Roy DP (2005) Sponsorship-linked marketing: Opening the black box. J. Advertising 34(2):21–42.

Crowston K, Wei K, Howison J, Wiggins A (2012) Free/libre open source software: What we know and what we do not know. ACM Comput. Surveys 44(2):Article 7.

Dahlander L, Magnusson MG (2005) Relationships between open source companies and communities: Observations from Nordic firms. Res. Policy 34(4):481–493.

Dahlander L, Magnusson MG (2008) How do firms make use of open source communities? Long Range Planning 41(6):629–649.

Dahlander L, O’Mahony SC (2011) Progressing to the center: Coordinating project work. Organ. Sci. 22(4):961–979.

Dahlander L, Wallin MW (2006) A man on the inside: Unlocking communities as complementary assets. Res. Policy 35(8): 1243–1259.

Daniel S, Agarwal R, Stewart KJ (2013) The effects of diversity in global, distributed collectives: A study of open source project success. Inform. Systems Res. 24(2):312–333.

David PA, Shapiro JS (2008) Community-based production of opensource software: What do we know about the developers who participate? Inform. Econom. Policy 20(4):364–398.

Deci EL, Ryan RM (1985) Intrinsic Motivation and Self-Determination in Human Behavior (Plenum, New York).

Dholakia UM, Bagozzi RP, Pearo LK (2004) A social influence model of consumer participation in network- and small-groupbased virtual communities. Internat. J. Res. Marketing 21(3): 241–263.

Dufwenberg M (2011) Game theory. Wiley Interdisciplinary Rev.: Cognitive Sci. 2(2):167–173.

Dutton JE, Dukerich JM (1991) Keeping an eye on the mirror: Image and identity in organizational adaptation. Acad. Management J. 34(3):517–554.

Dutton JE, Dukerich JM, Harquail CV (1994) Organizational images and member identification. Admin. Sci. Quart. 39(2):239–263.

Eisenberger R, Fasolo P, Davis-LaMastro V (1990) Perceived organizational support and employee diligence, commitment, and innovation. J. Appl. Psych. 75(1):51–59.

Fang Y, Neufeld D (2009) Understanding sustained participation in open source software projects. J. Management Inform. Systems 25(4):9–50.

Fiol CM, O’Connor EJ (2005) Identification in face-to-face, hybrid, and pure virtual teams: Untangling the contradictions. Organization Sci. 16(1):19–32.

Ford JK, MacCallum RC, Tait M (1986) The application of exploratory factor analysis in applied psychology: A critical review and analysis. Personnel Psych. 39(2):291–314.

Fornell C, Larcker DF (1981) Evaluating structural equation models with unobservable variables and measurement error. J. Marketing Res. 18(1):39–50.

Frey BS, Jegen R (2001) Motivation crowding theory. J. Econom. Surveys 15(5):589–610.

Goldsmith RE, Lafferty BA, Newell SJ (2000) The impact of corporate credibility and celebrity credibility on consumer reaction to advertisements and brands. J. Advertising 29(3):43–54.

Gruber M, Henkel J (2006) New ventures based on open innovation—An empirical analysis of start-up firms in embedded Linux. Internat. J. Tech. Management 33(4):356–372.

Hackman JR, Oldham GR (1980) Work Redesign (Addison-Wesley, Boston).

Hann I-H, Roberts J, Slaughter SA, Fielding R (2002) Economic incentives for participating in open source software project. Proc. 23rd Internat. Conf. Inform. Systems (Curran Associates, Inc., Red Hook, NY), 365–372.

Harhoff D (1996) Strategic spillovers and incentives for R&D. Management Sci. 42(6):907–925.

Harhoff D, Henkel J, von Hippel E (2003) Profiting from voluntary information spillovers: How users benefit by freely revealing their innovations. Res. Policy 32(10):1753–1769.

Hars A, Ou S (2002) Working for free? Motivations for participating in open-source projects. Internat. J. Electronic Commerce 6(3): 25–39.

Henkel J (2006) Selective revealing in open innovation processes: The case of embedded Linux. Res. Policy 37(7):953–969.

Henkel J (2009) Champions of revealing—The role of open source developers in commercial firms. Indust. Corporate Change 18(3): 435–471.

Hertel G, Niedner S, Herrmann S (2003) Motivation of software developers in open source projects: An Internet-based survey of contributors to the Linux kernel. Res. Policy 32(7):1159–1177.

Hinkin TR (1998) A brief tutorial on the development of measures for use in survey questionnaires. Organ. Res. Methods 1(1): 104–121.

Hogg MA, Terry DJ (2000) Social identity and self-categorization processes in organizational contexts. Acad. Management Rev. 25(1):121–140.

Iverson RD, Maguire C (2000) The relationship between job and life satisfaction: Evidence from a remote mining community. Human Relations 53(6):807–839.

Javalgi RG, Traylor MB, Gross AC, Lampman E (1994) Awareness of sponsorship and corporate image: An empirical investigation. J. Advertising 23(4):47–58.

Jeppesen LB, Lakhani KR (2010) Marginality and problem-solving effectiveness in broadcast search. Organ. Sci. 21(5):1016–1033.

Jöreskog KG, Sörbom D (1996) LISREL 8 User’s Reference Guide (Scientific Software International, Chicago).

Ke W, Zhang P (2010) The effects of extrinsic motivations and satisfaction in open source software development. J. Association Inform. Systems 11(12):784–804.

Kelly C (1993) Group identification, intergroup perceptions and collective action. Euro. Rev. Soc. Psych. 4(1):59–83.

Kerr NL (1983) Motivation losses in small groups: A social dilemma analysis. J. Personality Soc. Psych. 45(4):819–828.

Kline RB (2011) Principles and Practice of Structural Equation Modeling (Guilford Press, New York).

Kollock P (1999) The economies of online cooperation: Gifts and public goods in cyberspace. Smith M, Kollock P, eds. Communities in Cyberspace: Perspectives on New Forms of Social Organization (Routledge, London), 220–239.

Korsgaard MA, Roberson L (1995) Procedural justice in performance evaluation: The role of instrumental and noninstrumental voice in performance appraisal discussions. J. Management 21(4):657–669.

Kreiner GE, Ashforth BE, Sluss DM (2006) Identity dynamics in occupational dirty work: Integrating social identity and system justification perspectives. Organ. Sci. 17(5):619–636.

Kuk G (2006) Strategic interaction and knowledge sharing in the KDE developer mailing list. Management Sci. 52(7):1031–1042.

Lakhani KR, von Hippel E (2003) How open source software works: “Free” user-to-user assistance. Res. Policy 32(6):923–943.

Lakhani KR, Wolf RG (2005) Why hackers do what they do: Understanding motivation and effort in free/open source software projects. Feller J, Fitzgerald B, Hissam S, Lakhani KR, eds. Perspectives on Free and Open Source Software (MIT Press, Cambridge, MA), 3–22.

Ma M, Agarwal R (2007) Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Inform. Systems Res. 18(1):42–67.

Mayer RC, Davis JH, Schoorman FD (1995) An integrative model of organizational trust. Acad. Management Rev. 20(3):709–734.

Mehra A, Dewan R, Freimer M (2011) Firms as incubators of opensource software. Inform. Systems Res. 22(1):22–38.

Meyer JP, Becker TE, van Dick R (2006) Social identities and commitments at work: Toward an integrative model. J. Organ. Behav. 27(5):665–683.

Muller P, Pénin J (2006) Why do firms disclose knowledge and how does it matter? J. Evolutionary Econom. 16(1-2):85–108.

Newell SJ, Goldsmith RE (2001) The development of a scale to measure perceived corporate credibility. J. Bus. Res. 52(3):235–247.

O’Mahony SC, Bechky BA (2008) Boundary organisations: Enabling collaboration among unexpected allies. Admin. Sci. Quart. 53(3): 422–459.

Organ DW, Moorman RH (1993) Fairness and organizational citizenship behavior: What are the connections? Soc. Justice Res. 6(1):5–18.

Pénin J (2007) Open knowledge disclosure: An overview of the evidence and economic motivations. J. Econom. Surveys 21(2): 326–347.

Podsakoff PM, MacKenzie SB, Podsakoff NP (2012) Sources of method bias in social science research and recommendations on how to control it. Annual Rev. Psych. 63(1):539–569.

Podsakoff PM, MacKenzie SB, Lee J-Y, Podsakoff NP (2003) Common method biases in behavioral research: A critical review of the literature and recommended remedies. J. Appl. Psych. 88(5): 879–903.

Rhoades L, Eisenberger R, Armeli S (2001) Affective commitment to the organization: The contribution of perceived organizational support. J. Appl. Psych. 86(5):825–836.

Richardson HA, Simmering MJ, Sturman MC (2009) A tale of three perspectives examining post hoc statistical techniques for detection and correction of common method variance. Organ. Res. Methods 12(4):762–800.

Roberts JA, Hann I-H, Slaughter SA (2006) Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7):984–999.

Robinson SL, Morrison EW (1995) Psychological contracts and OCB: The effect of unfulfilled obligations on civic virtue behavior. J. Organ. Behav. 16(3):289–298.

Rossi MA (2006) Decoding the “free/open source puzzle”: A survey of theoretical and empirical contributions. Bitzer J, Schröder PJH, eds. The Economics of Open Source Software Development (Emerald Group Publishing, Bingley, UK), 15–56.

Schroer J, Hertel G (2009) Voluntary engagement in an open webbased encyclopedia: Wikipedians and why they do it. Media Psych. 12(1):96–120.

Segars AH (1997) Assessing the unidimensionality of measurement: A paradigm and illustration within the context of information systems research. Omega 25(1):107–121.

Setia P, Rajagopalan B, Sambamurthy V, Calantone R (2012) How peripheral developers contribute to open-source software development. Inform. Systems Res. 23(1):144–163.

Shah SK (2006) Motivation, governance, and the viability of hybrid forms in open source software development. Management Sci. 52(7):1000–1014.

Simpson B (2006) Social identity and cooperation in social dilemmas. Rationality Soc. 18(4):443–470.

Spaeth S, Haefliger S, von Krogh G, Renzl B (2008) Communal resources in open source software development. Inform. Res. 13(1). http://informationr.net/ir/13-1/paper332.html.

Spreitzer GM (1996) Social structural characteristics of psychological empowerment. Acad. Management J. 39(2):483–504.

Stewart D (2005) Social status in an open-source community. Amer. Sociol. Rev. 70(5):823–842.

Stewart KJ, Ammeter AP (2002) An exploratory study of factors influencing the level of vitality and popularity of open source projects. Proc. 23. Internat. Conf. Inform. Systems (Curran Associates, Inc., Red Hook, NY).

Stewart KJ, Gosain S (2006) The impact of ideology on effectiveness in open source software development teams. MIS Quart. 30(2):291–314.

Stewart KJ, Ammeter AP, Maruping LM (2006) Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Inform. Systems Res. 17(2):126–144.

Stuermer M, Spaeth S, von Krogh G (2009) Extending privatecollective innovation: A case study. R&D Management 39(2): 170–191.

Tajfel H, Turner JC (1979) An integrative theory of intergroup conflict. Austin WG, Worchel S, eds. The Social Psychology of Intergroup Relations (Brooks Cole Publishing, Monterey, CA), 33–47.

Turner JC, Oakes PJ (1986) The significance of the social identity concept for social psychology with reference to individualism, interactionism and social influence. British J. Soc. Psych. 25(3): 237–252.

Van Dick R, Grojean MW, Christ O, Wieseke J (2006) Identity and the extra mile: Relationships between organizational identification and organizational citizenship behaviour. British J. Management 17(4):283–301.

Von Hippel E, von Krogh G (2003) Open source software and the “private-collective” innovation model: Issues for organization science. Organ. Sci. 14(2):209–223.

Von Krogh G, Haefliger S, Spaeth S, Wallin MW (2012) Carrots and rainbows: Motivation and social practice in open source software development. MIS Quart. 36(2):649–676.

Waugh P, Metcalfe R (2007) The Foundations of Open—Evaluating Aspects of Openness in Software Projects (Waugh Partners & OSS Watch, Redfern, NSW, Australia).

West J (2003) How open is open enough? Melding proprietary and open source platform strategies. Res. Policy 32(7):1259–1285.

West J, O’Mahony SC (2008) The role of participation architecture in growing sponsored open source communities. Indust. Innovation 15(2):145–168.

Williams LJ, Hartman N, Cavazotte F (2010) Method variance and marker variables: A review and comprehensive CFA marker technique. Organ. Res. Methods 13(3):477–514.

Wu C-G, Gerlach JH, Young CE (2007) An empirical analysis of open source software developers’ motivations and continuance intentions. Inform. Management 44(3):253–262.

Zeitlyn D (2003) Gift economies in the development of open source software: Anthropological reflections. Res. Policy 32(7): 1287–1291.
