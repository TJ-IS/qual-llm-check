---
otero_id: 25750
otero_key: "49ZFR5YH"
title: "Project leaders as boundary spanners in open source software development: A resource dependence perspective"
authors: "John Qi Dong; Sebastian Johannes Götz"
year: "2021"
journal: "Information Systems Journal"
doi: "10.1111/isj.12313"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
SPECIAL ISSUE PAPER

WILEY

# Project leaders as boundary spanners in open source software development: A resource dependence perspective

John Qi Dong $^{1}$ | Sebastian Johannes Götz $^{2}$

$^{1}$ Trinity Business School, Trinity College Dublin, University of Dublin, Dublin, Ireland

$^{2}$ Syngroup Management Consulting GmbH, Vienna, Austria

Correspondence
John Qi Dong, Trinity Business School, Trinity College Dublin, University of Dublin, College Green, Dublin 2, Ireland.
Email: john.dong@tcd.ie

## Abstract

Digital social innovation is important for addressing various social needs, especially from those who are economically disadvantaged. For instance, open source software (OSS) is developed by mass collaboration on digital communities to provide software users free alternatives to commercial products. OSS is particularly valuable to meet the needs of numerous disadvantaged users for whom proprietary software is not affordable. While OSS projects are lack of formal organizational structure, project leaders play a significant role in initiating and managing these projects and eventually, influencing the degree to which the developed software is used and liked by users. Drawing on resource dependence theory, we investigate the impacts of two team-level characteristics of OSS project leaders (ie, size and tenure) on how well the developed software can address users' needs, with regard to the quantity of software being used by users and the quality of software to users' satisfaction. Further, from a resource dependence perspective, we examine the moderating role of project leaders' network ties in shaping the contingency of these effects. By using a large-scale dataset from 43 048 OSS development projects in SourceForge community, we find empirical evidence corroborating our theory. Taken together, our findings suggest the boundary-spanning role of project leaders in developing digital social innovation.

KEYWORDS

digital innovation, open source software, project leaders,

resource dependence theory, social innovation, software

development

## 1 | INTRODUCTION

During the past decades, the phenomenon of social innovation moved into the centre stage of public interest due to the emergence of new social challenges like climate change, worldwide epidemic of chronic disease, widening inequality and other rising social needs. For example, the United Nation proposes the sustainable development goals (SDGs), which are relevant to a number of critical problems that require the development of various social innovations. People feel the incentive to act in social innovation projects, because SDGs are relevant to social well-being of at least 4.5 billion people, but government policies and market solutions fail to meet the complex challenges of these growing social needs (Cajaiba-Santana, 2014). Social innovation is particularly valuable for addressing the social needs of economically disadvantaged groups, as they can often benefit little from commercialized innovation (Zheng & Yu, 2016).

As a result, social innovation projects—many of which leverage digital technologies to support mass collaboration and coordination—become increasingly important and popular to address social needs. Such digital social innovation projects make intensive use of distributed digital networks, emphasize digital collaboration and seek to improve the social well-being of disadvantaged groups (Davison, Vogel, Harris, & Jones, 2000; Khan, Lacity, & Carmel, 2018; Madon & Sharanappa, 2013). Digital technologies help social innovation projects to blur the physical boundaries between production and consumption, as developers and users of digital social innovation are overlapped (Mulgan, 2006; Mulgan, Tucker, Ali, & Sanders, 2007; Murray, Caulier-Grice, & Mulgan, 2010). In other words, many digital social innovations have become user-generated thanks to the digitally enabled engagement of users. By using digital technologies, social innovation projects can be well self-organized, different from commercial innovation projects that are managed in firms with a formal organizational structure.

Open source software (OSS) is a typical digital social innovation, as it (a) relies on input from mass collaboration of physically distributed volunteers on digital communities (eg, SourceForge.net), (b) produces output in a form of digital information good (ie, software) and (c) offers software innovation for free to address social needs, especially from economically disadvantaged groups for whom proprietary software is not affordable. Various kinds of needs in people's work or lives can be addressed by using OSS, including but not limited to word processing, data transfer, education and learning, software development, visual design and web surfing (see Table 1 for some notable examples). Addressing these social needs help to achieve multiple SDGs, such as quality education (Goal #4), decent work and economic growth (Goal #8), as well as industry, innovation and infrastructure (Goal #9). Thus, OSS projects provide a socially responsible way to address the social needs of using digital innovation from disadvantaged groups—similar to the ideas of other digital social innovation, such as impact sourcing (Kannothra, Manning, & Haigh, 2018; Khan et al., 2018) or social sourcing (Madon & Sharanappa, 2013).

Thanks to the support of digital technologies, OSS projects can benefit from mass collaboration of numerous distributed volunteers (Tim, Pan, Ractham, & Kaewkitipong, 2017; Zheng & Yu, 2016). Many OSS projects involve millions of developers and a multitude of project leaders (Mulgan et al., 2007). Project leaders play an important role in initiating and developing OSS projects, as many of them are the first developers and make key decisions for the projects. In an OSS project, development teams are self-organized without a formal organizational structure, so project leaders emerge in the development process and influence the development process through their work-related actions (Eseryel & Eseryel, 2013). Thus, OSS project leaders remain of indisputable importance for motivating and coordinating other developers to contribute to the success of a project (Li, Tan, & Teo, 2012).

TABLE 1 Examples of development OSS as digital social innovation

<table><tr><td>Project name</td><td>Description of software</td><td>Social needs</td><td>SDGs</td></tr><tr><td>OpenOffice</td><td>An open source office productivity software suit containing word processor, spreadsheet, presentation, graphics, formula editor and database management applications</td><td>Word processing</td><td>Goal #8: decent work and economic growth</td></tr><tr><td>FileZilla</td><td>An FTP/SFTP/FTPS client which allows its users to transfer files between your local computer and a website&#x27;s server</td><td>Data transfer</td><td>Goal #8: decent work and economic growth</td></tr><tr><td>Moodle</td><td>A course management system or online learning management system, which is designed for educators to create effective virtual online learning websites</td><td>Education and learning</td><td>Goal #4: quality education</td></tr><tr><td>Code:: Blocks</td><td>A cross platform integrated development environment which supports a variety of programming languages that provides comprehensive facilities to computer programmers for software development</td><td>Software development</td><td>Goal #9: industry, innovation and infrastructure</td></tr><tr><td>Scribus</td><td>A desktop publishing software designed to create professional layouts which supports professional publishing features, such as colour separation, spot colours and versatile PDF creation</td><td>Visual design</td><td>Goal #9: industry, innovation and infrastructure</td></tr><tr><td>Tor Browser</td><td>A browser which encrypts communication around a distributed network of relays run by volunteers and enables users to surf anonymous and get access to the dark websites</td><td>Web surfing</td><td>Goal #8: decent work and economic growth</td></tr></table>

Different from proprietary software project leaders, an OSS project leader emerges if he or she initiates a project by creating software from the start, inherits the source code from another leader who stopped working on it, or contributes significantly and obtains recognition and support from other developers. While proprietary software project leaders hold structural power, the authority of OSS project leaders naturally arises from a bottom-up investiture as a result of the contributions to the agreed goal (Bonaccorsi & Rossi, 2003). Primarily driven by the intrinsic motivation, OSS project leaders, often functioning as a team, possess unique characteristics to develop and articulate a clear vision, to persevere, to withstand social censure and, most importantly, to identify and meet the social needs (Swamy, 1990). Besides intensive work-related actions, the leaders of an OSS project hold exclusive rights to decide the features of the software, the tie to release updates, reward or punishment for developers and, ultimately, the next successors (Dong, Wu, & Zhang, 2019). Table 2 compares OSS and proprietary software project leaders and summarizes their differences.

While some prior studies have investigated leadership in OSS projects (see Table 3 for a summary), this literature has been largely focused on the antecedents of the emergence of leaders (Eseryel & Eseryel, 2013; Faraj et al., 2015; Fleming & Waguespack, 2007; Guiri et al., 2008; Johnson et al., 2015; O'Mahoney & Ferraro, 2007). Until recently, a couple of exceptions started to explore the roles of leadership style and followership of leaders in OSS development processes (Jiang et al., 2019; Li et al., 2012). To the best of our knowledge, the performance impacts of team-level characteristics of project leaders in addressing the needs of users have not been systematically studied. From a social innovation perspective, however, how project leaders may influence OSS projects to better address users' needs is an important question that requires further investigation.

In the social innovation literature, prior studies primarily focused on differentiating social innovation from other types of innovations (Mulgan et al., 2007; Pol & Ville, 2009; Stilgoe, Owen, & Macnaghten, 2013; Sun & Im, 2015), defining and conceptualizing the phenomenon of social innovation (Mulgan, 2006; Mulgan et al., 2007; Murray et al., 2010), investigating social innovation as a driver of social change (Cajaiba-Santana, 2014; Dawson & Daniel, 2010), explaining how profit-seeking firms can engage in social innovation while also accomplishing their corporate social responsibility (Altuna, Contri, Dell'Era, Frattini, & Maccarrone, 2015; Sun & Im, 2015; Varadarajan, 2014) and exploring social innovation in an entrepreneurial setting (Abu-Saifan, 2012; Daily, McDougall, Covin, & Dalton, 2002; Zahra, Gedajlovic, Neubaum, & Shulman, 2009). However, the role project leaders in influencing the degree to which a social innovation project can meet users' needs has not been systematically theorized and empirically examined.

TABLE 2 Differences between OSS and proprietary software project leaders

<table><tr><td></td><td>OSS project leaders</td><td>Proprietary software project leaders</td></tr><tr><td>Developmental role</td><td>Often the first developers</td><td>May or may not be the first developers</td></tr><tr><td>Organizational context</td><td>Taking the lead without formal organizational structure</td><td>Taking the lead with formal organizational structure</td></tr><tr><td>Source of authority</td><td>Work-related action and contribution</td><td>Structural power</td></tr><tr><td>Emerging process</td><td>Self-emergence</td><td>Organizational assignment</td></tr><tr><td>Major tasks</td><td>Intensive programming and key decision making</td><td>Less programming and more decision making</td></tr><tr><td>Primary motivations</td><td>Intrinsic motivation (personal need and fun)</td><td>Extrinsic motivation (economic wages)</td></tr></table>

TABLE 3 Summary of relevant literature on OSS leadership

<table><tr><td></td><td>Theory</td><td>OSS leadership</td><td>Antecedents/processes/impacts</td></tr><tr><td>Fleming and Waguespack (2007)</td><td>Social network theory</td><td>Emergence of leaders</td><td>Antecedents: technical contribution, network position</td></tr><tr><td>O&#x27;Mahoney and Ferraro (2007)</td><td>Grounded theory</td><td>Emergence of leaders</td><td>Antecedents: technical contribution, communication</td></tr><tr><td>Guiri, Rullani, and Torrisi (2008)</td><td>Theory of occupational choice</td><td>Emergence of leaders</td><td>Antecedents: diversity of skills</td></tr><tr><td>Li et al. (2012)</td><td>Path-goal and leadership theory</td><td>Management style of leaders</td><td>Processes: developers&#x27; motivation to participate in OSS development processes</td></tr><tr><td>Eseryel and Eseryel (2013)</td><td>Grounded theory</td><td>Emergence of leaders</td><td>Antecedents: leader perception, OSS development</td></tr><tr><td>Faraj, Kudaravalli, and Wasko (2015)</td><td>Behavioural and social network theory</td><td>Emergence of leaders</td><td>Antecedents: knowledge contribution, communication and network ties</td></tr><tr><td>Johnson, Safadi, and Faraj (2015)</td><td>Leadership theory</td><td>Emergence of leaders</td><td>Antecedents: formal role of authority, language use, network ties</td></tr><tr><td>Jiang, Tan, Sia, and Wei (2019)</td><td>Followership theory</td><td>Followership of leaders</td><td>Processes: code reuse in OSS development processes</td></tr><tr><td>This study</td><td>Resource dependence theory</td><td>Size, tenure, network ties of leaders</td><td>Impacts: social innovation performance of OSS addressing the needs of users</td></tr></table>

To address above gaps in the literatures on OSS leadership and social innovation, we draw on resource dependence theory and relevant literature in broad contexts other than OSS to identify two basic characteristics of OSS project leaders (ie, size and tenure) and examine their impacts on how the developed software can address users' needs, with regard to the quantity of software being used (measured by the number of user downloads) and the quality of software being liked by users (measured by user recommendation ratio). In particular, we view project leaders as boundary spanners who are readily bring important external resources into the development process of an OSS project. We argue that the value of these external resources could vary in terms of how many project leaders emerged in the development process (ie, size) and how long they served for the project (ie, tenure). To tease out the boundary-spanning theoretical mechanism that we propose above, we are guided by resource dependence theory to further look into project leaders' network ties to other OSS projects. If our theoretical explanations rooted in resource dependence really work, more network ties should allow project leaders to more readily bring external resources from other projects as they are involved in the focal project. If projects leaders are truly boundary spanners, their brokerage role in the OSS project network should enhance the impacts of their size and tenure. By using a large-scale dataset from 43 048 OSS development projects in SourceForge community, we find supportive evidence corroborating our theory.

The rest of the article is organized as follows. Next, we discuss our research context and explain why OSS is a digital social innovation. We then develop our theory and hypotheses, followed by empirical methods and results. Finally, we discuss the implications for theory and practice, as well as the limitations and directions for future research.

## 2 | OPEN SOURCE SOFTWARE AS DIGITAL SOCIAL INNOVATION

Digital technologies, particularly social media and digital communities on the Internet, have supported various social innovation projects by organizing collective actions (Bennett & Segerberg, 2012), responding to disasters (Tim et al., 2017), providing charitable programs (Zheng & Yu, 2016), offering governmental services (Rose, Persson, Heeager, & Irani, 2015), transforming healthcare (Stahl, Boherty, & Shaw, 2012) and developing free and open source tools (Dong et al., 2019). In the social innovation literature, OSS has been used as a notable example to derive implications for user engagement and development challenges of social innovation (Bhatt, Ahmad, & Roomi, 2016). OSS is a digital social innovation, as we explain next, for three reasons.

First, social innovation, different from commercial innovation, is not necessarily the product of a small group of employees who have the ability to detect new resources or recombine existing resources in creative ways and exploiting them to commercial ends (Mulgan et al., 2007). Instead, social innovation is often the outcome from much broader collective movements on digital communities. OSS projects have long been hosted on digital communities (Von Hippel, 2001), such as SourceForge.net. These digital communities allow distributed developers from all over the world to collaborate and co-develop software in one project, which sometimes could be a very large and complex project.

Second, OSS projects produce innovation output in a form of digital information good (ie, software). Different from physical social innovation, OSS is digitalized and is implemented as part of computer systems. The nature of OSS indicates that it is essentially a digital innovation (Kohli & Melville, 2019), which is developed to address users' needs. Thus, OSS is a combination of digital innovation and social innovation, or digital social innovation.

Third, social innovation takes various forms with an aim to meet social needs, especially those of socially disadvantaged groups (Mulgan et al., 2007; Murray et al., 2010; Qureshi, Sutter, & Bhatt, 2018). Unlike business innovation that focuses on exploiting an innovative idea to maximize a company's financial performance, social innovation aims to enhance society by developing goods of social importance (Mulgan, 2006). Thus, social innovation is characterized by a different motivation of addressing social needs and is often free. From this perspective, the motivation for participating in OSS projects is in line with the social and non-monetary aspects of social innovation (Lerner & Tirole, 2002). OSS projects provide people with access to free software and the possibility to forego on proprietary software. This is particularly valuable to address the social needs of those who are economically disadvantaged, as proprietary software may not be affordable for them. Without OSS projects, they may not be able to get access to useful tools in their work and lives.

The fact that OSS is a digital social innovation guides us to study the outcomes of OSS projects in terms of quantity and quality in addressing users' needs. Specifically, we are interested in how the developed software can address users' needs with regard to (a) the quantity of software being used (user downloads) and (b) the quality of software being liked by users (user recommendation ratio). Different from financial performance of commercial innovation, our OSS project outcomes capture user adoption and satisfaction with a social innovation—namely, how well the social innovation can address social needs. Wide adoption and high satisfaction in addressing users' needs represents the success of a digital social innovation (Datta, 2011; Meso, Musa, & Mbarika, 2005). Next, we review the literature on resource dependence theory, which is our overarching theoretical lens, and take a resource dependence perspective to explain the contingent impacts of project leaders' characteristics that we identify from the literature on user downloads and recommendation ratio.

## 3 | THEORY AND HYPOTHESES

## 3.1 | Resource dependence theory

Resource dependence theory was developed by Pfeffer and Salancik (1978) as a theoretical perspective to understand the control of various social entities, which has become one of the most influential theories in governance research. Resource dependence theory characterizes social entities as an open system depending on the contingencies in the external environment. In particular, social entities are not autonomous, but are constrained by a network of interdependencies with other social entities (Hillman & Dalziel, 2003; Hillman, Withers, & Collins, 2009; Pfeffer, 1973; Pfeffer & Salancik, 1978). This perspective recognizes the influence of external resources on social entities' performance outcomes and, although constrained by external resources, leaders of social entities can proactively manage the dependence of their social entities on external resources (Hillman et al., 2009).

Pfeffer and Salancik (1978) maintain that, in the organizational context, the board of directors is a key action that managers in firms to take for managing the environmental dependence of their organizations. This application of resource dependence theory stimulates a large literature of follow-up endeavours to investigate the role of directors from a resource dependence perspective (Hillman & Dalziel, 2003; Hillman, Keim, & Luce, 2001). In particular, Hillman et al. (2009) conduct a literature review on resource dependence theory and reveal that the research on board of directors is the area of greatest influence by resource dependence theory. In this area, research receives more empirical support for resource dependence theory than any other theories, including another predominant theory—agency theory (Johnson, Daily, & Ellstrand, 1996; Zahra & Pearce, 1989).

Prior studies have applied resource dependence theory to examine board of directors with a focus on board size, as it reflects the directors' ability to provide critical external resources to organizations. For example, board size has been documented to relate to an organization's dependence on the external environment (Certo, Daily, & Dalton, 2001; Pfeffer, 1973; Sanders & Carpenter, 1998), which, in turn, determines organizational performance (Certo, 2003; Dalton, Daily, Johnson, & Ellstrand, 1999). In our context, the most common governance structure of OSS projects is benevolent leaders, who have the obligation of decision making and crediting contributors fairly (Ljungberg, 2000). Given the literature rooted in resource dependence theory has widely revealed that size of a leader group is an important factor related to resource dependence, in the OSS context, we are motivated to examine size of project leaders (ie, the number of leaders of an OSS project) as one critical factor that influences resource dependence and OSS project outcomes.

Another stream of research has applied resource dependence theory to take a temporal perspective and consider the time over an organizational lifecycle in which board of directors' external resources are the most beneficial. For example, Zahra and Pearce (1989) suggest that resource dependence role of directors is dynamic and the importance of board resource provision is influenced by time. Further, empirical evidence shows that directors on board at early stages of an organizational lifecycle—those who join the board earlier than others—could be more beneficial (Daily & Dalton, 1993; Gabrielsson, 2007; Lynall, Golden, & Hillman, 2003). Extending this logic to the OSS context, we further consider tenure of project leaders (ie, the average time leaders spent in an OSS project) as another critical factor that influences resource dependence and OSS project outcomes.

The literature based on resource dependence theory also suggests that it is not just the size or tenure, but the composition of board that matters (Pearce & Zahra, 1992). For example, Boyd (1990) and Haunschild and Beckman (1998) suggest that board interlocks—the number of directorships in other organizations that each director holds—are a key characteristic of board composition, because interlocked directors are resource-rich and can bring a lot of resources from the external environment. This logic guides us to further look into network ties of project leaders (ie, the average number of other OSS projects that are led by each leader in an OSS project), as a key contingency factor that reflects the composition of a leader group and shapes the impacts of size and tenure of project leaders on OSS project outcomes. Like board of directors, a group of more and durable project leaders, especially with more network ties, can benefit an OSS project in various ways, by providing (a) information in the form of advice and counsel to other developers, (b) access to channels of information between the focal project and other projects and (c) preferential access to other external resources (eg, reusable code from other projects).

## 3.2 | The impacts of size and tenure of project leaders

As mentioned earlier, resource dependence theory has been used by a multitude of studies to examine the impact of board of directors on organizational performance (Boyd, 1990; Daily et al., 2002; Dalton et al., 1999; Dalton, Daily, Ellstrand, & Johnson, 1998; Hillman & Dalziel, 2003). It has been documented that a larger board of directors is, on average, associated with better performance (Daily & Dalton, 1993; Dalton et al., 1999). This is because, from a resource dependence perspective, board size reflects the directors' capacity to serve as boundary spanners by providing the access to external resources (Goodstein, Gautam, & Boeker, 1994; Pfeffer, 1973). We extend this logic to the OSS context and argue that a larger group of project leaders, as boundary spanners, can improve OSS project outcomes.

Similar to board of directors in organizations, the group of leaders in an OSS project is embedded in a network of different social actors that are marked by their interdependencies with other leaders, contributors, donators, platforms, organizations $^{1}$ and users. The project leaders' interdependencies on other social actors expose their OSS project to a high level of dependence on external resources. To develop and maintain a successful OSS project, therefore, it is of crucial importance that project leaders are able to support the development of software by attracting experienced developers, task executors and donators, as well as introducing reusable code from other projects to the focal project. OSS projects with a larger group of project leaders—who are boundary spanners—are exposed to richer access to critical developmental resources in the environment, and thereby better addressing users' needs with a greater number of downloads and higher satisfaction. Therefore, we propose the following hypothesis. $^{2}$

H1 Size of project leaders has a positive relationship with (a) user downloads and (b) user recommendation ratio of an OSS project.

The literature based on resource dependence theory also documents that the resource provision of board of directors also depends on the time over an organizational lifecycle. The directors joining board at early stages of organizational lifecycle are more beneficial than those on board later (Daily & Dalton, 1993; Gabrielsson, 2007; Lynall et al., 2003), because the resource provision of directors is related to the duration that they serve on board and the richness of their external resources accumulated over time (Becker, 1993; Coleman, 1988).

In the OSS context, project leaders gradually emerge in the development process (Eseryel & Eseryel, 2013) so there is heterogeneity in their tenure serving as a project leader and the accumulation of external resources. In an OSS project, project leaders act as boundary spanners and contribute considerably to the development of software by bringing external resources (eg, skilled developers and useful code). Such external resources are indispensable for the successful execution of an OSS project to address users' needs as OSS projects are largely lack of organizational support. Logically, the longer project leaders, on average, work on an OSS project (ie, greater tenure of project leaders), the more their external resources could be transferred across the boundary of the OSS project, and thereby increasing the adoption and user satisfaction of developed software. Hence, we propose the following hypothesis.

H2 Tenure of project leaders has a positive relationship with a) user downloads and b) user recommendation ratio of an OSS project.

## 3.3 | The moderating role of network ties of project leaders

Prior studies based on resource dependence theory have investigated interlocks of directors across corporate boards and found that they can largely shape the resource provision of the board of directors for a focal organization (Boyd, 1990; Haunschild & Beckman, 1998). This is because interlocked directors are resource-rich in the inter-organizational network and can bring a lot of resources from the external environment. To tease out the theoretical mechanism of the boundary-spanning role of project leaders in an OSS project, we look into their network ties that are related to project leaders' richness of external resources and shape the impacts of size and tenure on project outcomes.

In the social innovation literature, research suggests that network ties serve as an important factor enabling or constraining the process of social changes (Morrison, 2002; Qureshi, Kistruck, & Bhatt, 2016). Network embeddedness of project leaders has a positive influence on the technical success of OSS projects (Grewal, Lilien, & Mallapragada, 2006). Further, network structure and position positively influence OSS project success (Daniel & Stewart, 2016; Fershtman & Gandal, 2011). On the digital community, an OSS project is embedded in the network of projects, in which OSS projects are connected by co-leadership, as many leaders are involved in multiple OSS projects (Daniel & Stewart, 2016; Peng, Wan, & Woodlock, 2013). Such network ties across boundaries can influence the frequency of communication and knowledge sharing (Qureshi et al., 2018; Singh, 2005). More network ties provide timelier access to more and diverse knowledge (Dong, McCarthy, & Schoenmakers, 2017), thereby increasing the boundary-spanning benefits of an OSS project from its project leaders.

A successful OSS project involves massive collaboration and knowledge exchange among developers on the digital community. Project leaders with more network ties give them the opportunities to know-skilled developers in other projects, make themselves well known in the project network on the digital community, as well as attract more capable contributors to the focal project. Additionally, projects leaders are deeply involved in knowledge sharing by giving and receiving advice on features to be developed and open source code from other projects to be reused. From a resource dependence perspective, the software development of a focal project may benefit from its project leaders' multiple participations in other OSS projects via knowledge spillover and code reuse across projects. Knowledge spillover stemming from the boundary-spanning role of project leaders enables the focal project to take advantage of functional code made in other projects. As a result of the open source copyright, code reuse is common in the software development of OSS projects (Sojer & Henkel, 2010).

In H1 and H2, we hypothesize that size and tenure of project leaders will have positive relationships with user downloads and recommendation ratio of an OSS project. In an OSS project, if leaders on average have more network ties, the positive effects of size will be amplified because project leaders have greater access to external resources (eg, skilled developers and useful code) from other projects. Similarly, the positive effects of tenure will also be amplified by more network ties due to project leaders' access to more developers and useful code available in the network. Hence, the focal project will benefit more from the boundary-spanning role of project leaders, allowing the developed software to better address users' needs in terms of quantity and quality. Therefore, we propose the following two moderation hypotheses.

H3 Network ties of project leaders positively moderate the relationship between size of project leaders and (a) user downloads and (b) user recommendation ratio of an OSS project, such that the positive relationship is stronger when project leaders have more network ties.

H4 Network ties of project leaders positively moderate the relationship between tenure of project leaders and (a) user downloads and (b) user recommendation ratio of an OSS project, such that the positive relationship is stronger when project leaders have more network ties.

## 4 | METHODOLOGY

## 4.1 | Data

To test our hypotheses, we collected archival data from SourceForge community (sourceforge.net). SourceForge is one of the largest digital communities hosting OSS projects and has over 500 000 projects, 850 000 developer activities, 3.4 million registered users and more than 4 million daily downloads. It provides OSS projects certain management tools (eg, discussion forums, issue tracking, code repository, documentation and statistics), which facilitates and supports the development of OSS projects. Focusing on one community helps us control the unobservable heterogeneity across different communities and networks.

All our sampled projects are released in the project category ‘development software’ in SourceForge community. Development software can be best described as software that provides all users in the society to address a wide variety of social needs, including programming, word processing, file sharing, web surfing, education and learning, and so on. Development software addresses the social needs by providing people with access to free alternatives to expensive proprietary software. Thus, development software projects are particularly suitable for the purpose of our study on digital social innovation. In January 2013, we gathered a cross-sectional dataset from all development software projects that were launched between November 1999 and January 2013 in SourceForge community, encompassing a large sample of 43 048 OSS projects.

## 4.2 | Dependent variables

Table 4 presents the description of our variables. OSS project outcomes could be assessed in terms of the quantity of usage in the society by tracking the number of user downloads and the quality of usage in the society as user satisfaction. The number of downloads has been used as an indicator for OSS project success (Crowston, Howison, & Annabi, 2006; Murray et al., 2010) and therefore the number of downloads represents an appropriate quantity perspective to indicate the social popularity of an OSS project, reflecting the degree to which the developed software can meet users' needs. OSS projects with high user downloads will be perceived as more effective to address social needs. On the other hand, user recommendation ratio adds another quality perspective to evaluate how well the developed software can address social needs. User ratings have been widely used to evaluate user satisfaction about products or services and therefore user recommendation ratio should represent an appropriate proxy of user satisfaction (Agarwal & Rathod, 2006; Zhu & Zhang, 2010). Accordingly, we used two measures for OSS project outcomes as (a) user downloads for the developed software and (b) user recommendation ratio for the developed software—the number of positive ratings over total number of (positive and negative) ratings—both of which could be obtained based on the information available on project pages of SourceForge community. To reduce data skewness, we took the natural logarithm of user downloads to normalize this variable.

TABLE 4 Description of variables

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>User downloads</td><td>The logged number of downloads</td></tr><tr><td>User recommendation ratio</td><td>The number of positive ratings divided by the total number of ratings</td></tr><tr><td>Size of project leaders</td><td>The logged total number of leaders guiding the project</td></tr><tr><td>Tenure of project leaders</td><td>The logged average number of days project leader have worked on a project</td></tr><tr><td>Network ties of project leaders</td><td>The logged average number of projects leaders are participating in</td></tr><tr><td>Developer effort</td><td>The logged number of times developers write the project code/file</td></tr><tr><td>Project description</td><td>The logged number of words used for the project&#x27;s description in SourceForge community</td></tr><tr><td>User diversity</td><td>The logged number of user categories a project belonged to</td></tr><tr><td>Project size</td><td>The logged kilobytes of the project&#x27;s first version released in SourceForge community</td></tr><tr><td>Code reuse</td><td>Dummy variable indicates whether the focal project reuse codes from other projects</td></tr><tr><td>License diversity</td><td>The logged number of licenses used for a specific project</td></tr><tr><td>Initial release time</td><td>The reciprocal of the number of days from project launch to the initial release</td></tr><tr><td>Update frequency</td><td>The number of updates per month</td></tr><tr><td>Project age</td><td>The logged number of days since project launch</td></tr></table>

## 4.3 | Independent variables and moderator

On each project page, SourceForge community provides a list of leaders, which we consider as project leaders. They may be founders of the project or emerge as leaders by showing visionary behaviour or by acting as a task executor. We measured size of project leaders by the total number of leaders who participated in an OSS project. We measured tenure of project leaders by the average number of days project leaders have worked on an OSS project. We took the natural logarithm of these two variables to reduce data skewness.

The moderator, network ties of project leaders in an OSS project, was captured by (a) summing up the number of each project leader's different OSS projects for a focal project and (b) dividing the sum by the number of project leaders (ie, size) for each focal project (Daniel & Stewart, 2016; Peng et al., 2013). This is because simply using the sum of projects without scaling by the number of project leaders will confound with the size of project leaders in our empirical analysis. Our measurement of the moderator can get rid of size effect and reflect the average network ties per leader for each focal project. We took the natural logarithm of this variable to reduce data skewness.

## 4.4 | Control variables

We controlled a number of factors that may influence user downloads and recommendation ratio of an OSS project. First, developers' effort has a positive influence on the success of OSS projects (Grewal et al., 2006; Roberts, Hann, & Slaughter, 2006; Stewart & Gosain, 2006). Therefore, we controlled developer effort by counting the number of writes in code or file made by developers as proxy for their effort in an OSS project. We took the natural logarithm to reduce the skewness of this variable.

Second, each OSS project in SourceForge community has a short description of its functions and features on the project page. Kessler and Chakrabarti (1996) suggest that the success of an OSS project is related to its goal and target clarity. We followed Hahn, Moon, and Zhang (2008)'s approach to measure project description as the total number of words describing the project. The more words the description contains, the higher the level of goal clarity. The natural logarithm was used to reduce the skewness of this variable.

Third, Singh and Tan (2010) state that the audience type that an OSS belongs to has an impact on which group of users are attracted to the software. As an OSS project might offer a variety of application possibilities, it is possible that it will be simultaneously listed in multiple categories in SourceForge community. Since a certain type of audience is usually attracted by a certain type of category, we used the number of categories a project belongs to as a proxy for user diversity. We took the natural logarithm to reduce the skewness of this variable.

Fourth, a comparatively big file size indicates a variety of functions in the developed software from an OSS project, therefore it might affect user downloads and satisfaction. We controlled the first version size in kilo bites as the proxy of project size (Dong et al., 2019). The natural logarithm was used to reduce the skewness of this variable.

Fifth, since code reuse is common to see in OSS projects (Majchrzak, Cooper, & Neece, 2004; Sojer & Henkel, 2010), we controlled it by a binary variable indicating whether an OSS project has used any code from other projects. Specifically, we followed Nyman and Mikkonen (2011) to search related keywords (ie, clone, fork, repackage, reuse, library, libraries, integrate, integration, redefine and overlap) in project description to identify projects with code reuse.

Sixth, licenses can be seen as the most important institution in the governance structure of OSS projects (Bonaccorsi & Rossi, 2003). Furthermore, research has suggested that OSS diffusion is influenced by license choice. License restrictiveness may influence the users' benefits and costs by using the software (Stewart & Gosain, 2006). As the number of licenses can be seen as an indicator for license restrictiveness of an OSS project, we controlled license diversity. The higher the number of licenses owned by a certain project, the more restricted the project is. We took the natural logarithm to reduce the skewness of this variable.

Seventh, initial release time may determine the first mover advantage of an OSS project, we controlled the reciprocal of the number of days from project launch to the initial release of developed software (Dong et al., 2019).

Eighth, we controlled update frequency of an OSS project, which may indicate the enduring effort of addressing social needs over time. Specifically, update frequency was measured by the average number of significant updates per month after the initial release based on four criteria: (a) non only updates in the root directory but also updates in the second level and the third level directory of the file folders, (b) multiple updates on the same day are counted only once, (c) small changes in text, pdf or jpg files are excluded and (d) the updates are downloadable files (Dong et al., 2019).

Finally, we controlled project age by counting the number of days since project launch. $^{3}$ Again, the natural logarithm was used to reduce the skewness of this variable. Table 5 reports the descriptive statistics, and Table 6 shows the correlations of these variables.

## 5 | RESULTS

We used ordinary least squares regression to analyse the data and test our hypotheses. Table 7 reports the regression results for user downloads. In general, our model demonstrated a good fit, which can explain about 76% variation in user downloads. We first estimated a control model and found that most control variables had statistically significant effects on user downloads. We then added size and tenure of project leaders into control model to test H1a and H2a. We found that size of project leaders had a statistically significant and positive effect on user downloads ( $\beta = 0.367; P < .001$ ). Thus, H1a is supported. We further found that tenure of project leaders had a statistically significant and positive effect on user downloads ( $\beta = 0.104; P < .001$ ). Thus, H2a is also supported.

TABLE 5 Descriptive statistics

<table><tr><td></td><td>Mean</td><td>SD</td><td>Min</td><td>Max</td></tr><tr><td>User downloads</td><td>3.288</td><td>3.649</td><td>0</td><td>17.809</td></tr><tr><td>User recommendation ratio</td><td>0.214</td><td>0.398</td><td>0</td><td>1</td></tr><tr><td>Size of project leaders</td><td>0.777</td><td>0.225</td><td>0.693</td><td>3.258</td></tr><tr><td>Tenure of project leaders</td><td>7.646</td><td>0.989</td><td>0</td><td>8.489</td></tr><tr><td>Network ties of project leaders</td><td>1.339</td><td>0.796</td><td>0</td><td>5.209</td></tr><tr><td>Developer effort</td><td>1.071</td><td>2.381</td><td>0</td><td>13.089</td></tr><tr><td>Project description</td><td>3.106</td><td>0.698</td><td>0</td><td>5.215</td></tr><tr><td>User diversity</td><td>1.013</td><td>0.343</td><td>0</td><td>2.303</td></tr><tr><td>Project size</td><td>2.720</td><td>3.214</td><td>0</td><td>15.087</td></tr><tr><td>Code reuse</td><td>0.005</td><td>0.073</td><td>0</td><td>1</td></tr><tr><td>License diversity</td><td>0.706</td><td>0.192</td><td>0</td><td>2.079</td></tr><tr><td>Initial release time</td><td>0.128</td><td>0.257</td><td>0.0002</td><td>1</td></tr><tr><td>Update frequency</td><td>0.037</td><td>0.187</td><td>0</td><td>9.643</td></tr><tr><td>Project age</td><td>7.517</td><td>0.715</td><td>2.079</td><td>8.486</td></tr></table>

To test the moderating effects of network time of project leaders, we created the interaction term between size/tenure and network ties of project leaders and estimated a full model for user downloads. We found that network ties of project leaders had a statistically significant and positive effect on user downloads ( $\beta = 0.189; P < .001$ ). More importantly, the interaction term size and network ties of project leaders had a statistically significant and positive effect on user downloads ( $\beta = 0.137; P < .001$ ), supporting H3a. Moreover, the interaction term between tenure and network ties of project leaders also had a statistically significant and positive effect on user downloads ( $\beta = 0.239; P < .001$ ), supporting H4a.

In Figures 1 and 2, we plot the marginal effects of size/tenure of project leaders on user downloads at different levels of network ties, where high and low levels are defined as mean plus or minus one standard deviation. Consistent with H3a and H4a, increasing size/tenure of project leaders can increase user downloads to a larger extent when project leaders' network ties are at a higher than lower level. $^{4}$

Table 8 reports the regression results for user recommendation ratio. Overall, our model can explain about 13% variation in user recommendation ratio. Again, we first estimated a control model and found that all control variables had statistically significant effects on user recommendation ratio. We then added size and tenure of project leaders into control model to test H1b and H2b. We found that size of project leaders had a statistically significant and positive effect on user recommendation ratio ( $\beta = 0.123; P < .001$ ), and tenure of project leaders had a statistically significant and positive effect on user recommendation ratio ( $\beta = 0.004; P < .1$ ). Thus, both H1b and H2b are supported.

Furthermore, we added the interaction term between size/tenure and network ties of project leaders and estimated a full model for user recommendation ratio. We found that network ties of project leader had a statistically significant and positive effect on user recommendation ratio too ( $\beta = 0.007; P < .01$ ). More importantly, the interaction term between size and network ties of project leaders had a statistically significant and positive effect on user recommendation ratio ( $\beta = 0.023; P < .05$ ), and the interaction term between tenure and network ties of project leaders also had a statistically significant and positive effect on user recommendation ratio ( $\beta = 0.018; P < .001$ ). Thus, H3b and H4b are also supported.

In Figures 3 and 4, we plot the marginal effects of size/tenure of project leaders on user recommendation ratio at different levels of network ties, where high and low levels are defined as mean plus or minus one standard deviation. Consistent with H3b and H4b, increasing size/tenure of project leaders can increase user recommendation ratio to a larger extent when project leaders' network ties are at a higher than lower level.

<table><tr><td></td><td>(1)</td><td>(2)</td><td>(3)</td><td>(4)</td><td>(5)</td><td>(6)</td><td>(7)</td><td>(8)</td><td>(9)</td><td>(10)</td><td>(11)</td><td>(12)</td><td>(13)</td></tr><tr><td colspan="14">(1) User downloads</td></tr><tr><td>(2) User recommendation ratio</td><td>0.384</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(3) Size of project leaders</td><td>0.172</td><td>0.134</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(4) Tenure of project leaders</td><td>0.148</td><td>0.014</td><td>0.092</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(5) Network ties of project leaders</td><td>0.131</td><td>0.058</td><td>0.332</td><td>0.062</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(6) Developer effort</td><td>0.146</td><td>0.176</td><td>0.183</td><td>0.042</td><td>0.085</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(7) Project description</td><td>0.196</td><td>0.109</td><td>0.045</td><td>0.062</td><td>0.017</td><td>0.033</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(8) User diversity</td><td>0.106</td><td>0.087</td><td>0.077</td><td>0.052</td><td>0.049</td><td>0.061</td><td>0.152</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(9) Project size</td><td>0.838</td><td>0.308</td><td>0.162</td><td>0.056</td><td>0.133</td><td>0.164</td><td>0.196</td><td>0.100</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>(10) Code reuse</td><td>0.014</td><td>0.017</td><td>0.006</td><td>0.001</td><td>0.015</td><td>0.003</td><td>0.024</td><td>0.002</td><td>0.019</td><td></td><td></td><td></td><td></td></tr><tr><td>(11) License diversity</td><td>0.028</td><td>0.027</td><td>0.014</td><td>0.062</td><td>0.016</td><td>0.032</td><td>0.037</td><td>0.080</td><td>0.020</td><td>0.005</td><td></td><td></td><td></td></tr><tr><td>(12) Initial release speed</td><td>0.397</td><td>0.143</td><td>-0.056</td><td>-0.101</td><td>0.033</td><td>-0.047</td><td>0.094</td><td>-0.011</td><td>0.383</td><td>0.008</td><td>-0.034</td><td></td><td></td></tr><tr><td>(13) Update frequency</td><td>0.254</td><td>0.182</td><td>0.085</td><td>-0.051</td><td>0.073</td><td>0.112</td><td>0.077</td><td>0.049</td><td>0.252</td><td>0.023</td><td>0.017</td><td>0.136</td><td></td></tr><tr><td>(14) Project age</td><td>0.222</td><td>-0.023</td><td>0.127</td><td>0.467</td><td>0.063</td><td>-0.001</td><td>0.048</td><td>0.077</td><td>0.063</td><td>-0.015</td><td>0.111</td><td>-0.207</td><td>-0.151</td></tr></table>

TABLE 6 Correlations  
Note: Correlations greater than .009 are significant at P < .05.

TABLE 7 Regression results for user downloads

<table><tr><td></td><td>Test</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Size of project leaders</td><td>H1</td><td></td><td>0.367***(0.040)</td><td>-0.069(0.059)</td></tr><tr><td>Tenure of project leaders</td><td>H2</td><td></td><td>0.104***(0.010)</td><td>0.250***(0.011)</td></tr><tr><td>Size of project leaders × Network ties of project leaders</td><td>H3</td><td></td><td></td><td>0.137**(0.047)</td></tr><tr><td>Tenure of project leaders × Network ties of project leaders</td><td>H4</td><td></td><td></td><td>0.239***(0.008)</td></tr><tr><td>Network ties of project leaders</td><td></td><td></td><td></td><td>0.189***(0.013)</td></tr><tr><td>Developer effort</td><td></td><td>0.333***(0.004)</td><td>0.027***(0.004)</td><td>0.020***(0.004)</td></tr><tr><td>Project description</td><td></td><td>0.101***(0.013)</td><td>0.096***(0.013)</td><td>0.077***(0.013)</td></tr><tr><td>User diversity</td><td></td><td>0.103***(0.026)</td><td>0.091***(0.026)</td><td>0.091***(0.026)</td></tr><tr><td>Project size</td><td></td><td>0.841***(0.003)</td><td>0.836***(0.003)</td><td>0.835***(0.003)</td></tr><tr><td>Code reuse</td><td></td><td>-0.012(0.119)</td><td>-0.025(0.119)</td><td>-0.045(0.118)</td></tr><tr><td>License diversity</td><td></td><td>-0.174***(0.046)</td><td>-0.172***(0.046)</td><td>-0.173***(0.045)</td></tr><tr><td>Initial release time</td><td></td><td>2.091***(0.038)</td><td>2.125***(0.038)</td><td>2.115***(0.038)</td></tr><tr><td>Update frequency</td><td></td><td>1.474***(0.049)</td><td>1.443***(0.049)</td><td>1.434***(0.049)</td></tr><tr><td>Project age</td><td></td><td>1.105***(0.013)</td><td>1.026***(0.014)</td><td>0.974***(0.014)</td></tr><tr><td>Constant</td><td></td><td>-7.956***(0.106)</td><td>-7.322***(0.117)</td><td>-6.881***(0.117)</td></tr><tr><td> $R^2$ </td><td></td><td>.754</td><td>.755</td><td>.760</td></tr><tr><td>Adj. $R^2$ </td><td></td><td>.754</td><td>.755</td><td>.760</td></tr><tr><td>F</td><td></td><td>14 628.680***</td><td>12 040.670***</td><td>9713.480***</td></tr></table>

Note: N = 43 048. Standard errors are in parentheses.  
\*\*P < .01. \*\*\*P < .001.

## 6 | DISCUSSISON AND CONCLUSION

## 6.1 | Theoretical implications

Taking OSS projects as an example, our work provides important theoretical implications for research on digital social innovation. On the one hand, we demonstrate that resource dependence theory is a power theoretical lens to understand the role of project leaders in developing digital social innovation projects. On the other hand, we also identify a key contingency condition that shapes projects leaders' benefits for digital social innovation projects. From a resource dependence perspective, their social network embeddedness facilitates or constraints the boundary-spanning role that they play in developing digital social innovation projects. Next, we discuss each of the theoretical implications in detail.

FIGURE 1 Marginal effects of size of project leaders on user downloads at vayring levels of network ties of project leaders [Colour figure can be viewed at wileyonlinelibrary.com]  
![](/api/attachments/49ZFR5YH/fulltext/images/288d1ab28b3f2135b139a531685e3537848cbcd9af50cced8a6b66e43dcf772e.jpg)

FIGURE 2 Marginal effects of tenure of project leaders on user downloads at varying levels of network ties of project leaders [Colour figure can be viewed at wileyonlinelibrary.com]  
![](/api/attachments/49ZFR5YH/fulltext/images/86d8ec94282b3210df56501bbcff1cd4420bdfa76e9aeacb62ab0def324a7809.jpg)

## 6.1.1 | Resource dependence perspective as a powerful theoretical lens for digital social innovation research

Resource dependence theory is a powerful theoretical lens informing the role of leaders (Hillman et al., 2009; Pfeffer & Salancik, 1978), which, for instance, fosters the research on board of directors and receives the strongest empirical support over competing theories (Johnson et al., 1996; Zahra & Pearce, 1989). We broaden the research based on resource dependence theory and introduce it to the digital social innovation context. Using OSS projects as an example, this study elaborates resource dependence theory in explaining the boundary-spanning role of project leaders for developing digital social innovation. The literature on board of directors rooted in resource dependence theory (Certo et al., 2001; Gabrielsson, 2007; Lynall et al., 2003) guides us to look into size and tenure of project leaders as two basic characteristics that influence how well an OSS project can address social needs in terms of quantity and quality.

TABLE 8 Regression results for user recommendation ratio

<table><tr><td></td><td>Test</td><td>(1)</td><td>(2)</td><td>(3)</td></tr><tr><td>Size of project leaders</td><td>H1</td><td></td><td>0.123***(0.008)</td><td>0.086***(0.012)</td></tr><tr><td>Tenure of project leaders</td><td>H2</td><td></td><td>0.004+(0.002)</td><td>0.015***(0.002)</td></tr><tr><td>Size of project leaders × Network ties of project leaders</td><td>H3</td><td></td><td></td><td>0.023*(0.010)</td></tr><tr><td>Tenure of project leaders × Network ties of project leaders</td><td>H4</td><td></td><td></td><td>0.018***(0.002)</td></tr><tr><td>Network ties of project leaders</td><td></td><td></td><td></td><td>0.007**(0.003)</td></tr><tr><td>Developer effort</td><td></td><td>0.021***(0.001)</td><td>0.019***(0.001)</td><td>0.018***(0.001)</td></tr><tr><td>Project description</td><td></td><td>0.023***(0.003)</td><td>0.023***(0.003)</td><td>0.022***(0.003)</td></tr><tr><td>User diversity</td><td></td><td>0.053***(0.005)</td><td>0.050***(0.005)</td><td>0.050***(0.005)</td></tr><tr><td>Project size</td><td></td><td>0.030***(0.001)</td><td>0.028***(0.001)</td><td>0.028***(0.001)</td></tr><tr><td>Code reuse</td><td></td><td>0.047+(0.025)</td><td>0.045+(0.024)</td><td>0.045+(0.024)</td></tr><tr><td>License diversity</td><td></td><td>0.032***(0.009)</td><td>0.034***(0.009)</td><td>0.034***(0.009)</td></tr><tr><td>Initial release time</td><td></td><td>0.056***(0.008)</td><td>0.066***(0.008)</td><td>0.066***(0.008)</td></tr><tr><td>Update frequency</td><td></td><td>0.200***(0.010)</td><td>0.191***(0.010)</td><td>0.191***(0.010)</td></tr><tr><td>Project age</td><td></td><td>-0.013***(0.003)</td><td>-0.019***(0.003)</td><td>-0.023***(0.003)</td></tr><tr><td>Constant</td><td></td><td>0.045***(0.022)</td><td>0.102***(0.024)</td><td>0.132***(0.024)</td></tr><tr><td> $R^2$ </td><td></td><td>.127</td><td>.132</td><td>.134</td></tr><tr><td>Adj. $R^2$ </td><td></td><td>.127</td><td>.131</td><td>.134</td></tr><tr><td>F</td><td></td><td>696.390***</td><td>593.130***</td><td>477.230***</td></tr></table>

Note: N = 43 048. Standard errors are in parentheses.  
$^{+}$ P < .1.  
\*P < .05.\*\*P < .01.\*\*\*P < .001.

Our empirical analysis on user downloads and satisfaction of an OSS project consistently provides support for resource dependence theory by revealing that a large and enduring group of project leaders can improve user downloads and satisfaction with the developed software. Consistent with resource dependence theory, our results could be explained by the boundary-spanning role of project leaders, who can provide the focal project more and timely access to external resources if more project leaders are involved for a longer period of time. Taken together, our findings highlight the importance of a resource dependence perspective to understand the critical role of project leaders as boundary spanners in developing digital social innovation. Future research could thus leverage resource dependence theory as a power lens to account for the boundary-spanning resource provision of project leaders.

FIGURE 3 Marginal effects of size of project leaders on user recommendation ratio at varying levels of network ties of project leaders [Colour figure can be viewed at wileyonlinelibrary.com]  
![](/api/attachments/49ZFR5YH/fulltext/images/ac1e37860a01bbbb3294f4e11cf6553e45d074305651ef2c14854e13da9a1c4f.jpg)

FIGURE 4 Marginal effects of tenure of project leaders on user recommendation ratio at varying levels of network ties of project leaders [Colour figure can be viewed at wileyonlinelibrary.com]  
![](/api/attachments/49ZFR5YH/fulltext/images/02c20616abec2e105e22985b1c51027d8b52f2cd27aa4dd5891a900246d35250.jpg)

## 6.1.2 | Social network embeddedness as a key contingency condition for digital social innovation research

From a resource dependence perspective, a key contingency in the boundary-spanning role of project leaders is the external resources available in the social network in which the digital social innovation project is embedded. Using OSS projects as an example, we find that network ties of project leaders can strengthen or weaken the benefits of size and tenure on user downloads and satisfaction with the developed software. Project leaders who possess more network ties with other social actors will be exposed to a higher frequency of communication, have access to high-fidelity information, and hold greater influential power on various stakeholders. All these benefits are essential for the success of digital social innovation projects, by facilitating access to external resources, decreasing development costs and reducing the development cycle time. In summary, social network embeddedness is a key contingency condition of project leaders' influence on how well a digital social innovation project can address social needs. Future research needs to consider the moderating role of social network embeddedness to understand the contingency and tease out the boundary-spanning mechanisms in the resource provision of project leaders.

## 6.1.3 | Performance impacts of team-level project leader characteristics for OSS leadership research

This study also contributes to the OSS leadership literature by shifting the focus from the emergence of project leaders to the performance impacts of project leaders. Prior research has primarily investigated how project leaders emerge in OSS development processes, providing useful knowledge about various antecedents of emerging leadership in OSS projects (eg, Eseryel & Eseryel, 2013; Faraj et al., 2015; Fleming & Waguespack, 2007; Guiri et al., 2008; Johnson et al., 2015; O'Mahoney & Ferraro, 2007). This study generates new insights into the performance impacts of project leaders. Using resource dependence theory as an overarching framework, we identify key team-level characteristics of project leaders and examine their impacts on the quantity and quality of addressing the social needs of OSS users. Our results unveil that the size and tenure of leaders in an OSS project matter for addressing social needs, conditional on their social capital embedded in project network ties. Future research needs to pay attention to these structural team-level characteristics and their contingencies when understanding the performance impacts of projects leaders in OSS development.

## 6.2 | Practical implications

Taking OSS projects as an example, our findings provide useful guidance for practitioners about how to organize digital social innovation projects by leveraging project leaders. Our results indicate that size of project leaders matters. A larger group of project leaders can enhance project outcomes to address social needs, by bringing rich and timely access to external resources. While in the OSS context it is the larger the better for a group of project leaders, the size of project leaders is often small. Caution is needed when generalizing our findings to other types of digital social innovation projects with a very large group of project leaders, as in this case huge size might do more harm than good. Our results also indicate that tenure of project leaders matters. Hence, to succeed, project leaders should be experienced and dedicated, and their accumulated resources over time are of indisputable importance for digital social innovation projects.

Digital social innovation projects are often embedded in social networks. Project leaders' network ties in social networks determine how much a project can benefit from project leaders as boundary spanners with access to relevant knowledge and strategic assets, which are indispensable for the success of the project. Better connected project leaders will be able to provide access to more external resources and boost the development of digital social innovation project. In particular, project leaders who simultaneously participate in different projects are often hold highly valuable external resources for the focal project. The knowledge spillover between digital social innovation projects may also considerably decrease the development costs and shorten its development cycle time.

## 6.3 | Limitations and concluding remarks

This study aims to take an initial step to understand the role of project leaders in digital social innovation by taking OSS projects as an example. Nevertheless, it is important to mention that our findings do not claim for generalizability, as we focus on OSS projects by contextualizing our theory and empirical analysis. While it has been suggested that significant theoretical advances related to core IS phenomena can be derived by contextualizing a study (Chiasson & Davidson, 2005; Hong, Chan, Thong, Chasalow, & Dhillon, 2014), OSS is one type of digital social innovations and our findings are not applicable all types of digital social innovation projects. Hence, it should be cautious when generalizing our findings to other types of digital social innovation projects. Future research may collect data from other types of digital social innovation projects to examine our findings. It is particularly interesting to examine the nuanced impacts of size of project leaders in other large projects, especially when the size of project leaders is considerable.

Our empirical analysis is conducted with archival data from a large sample of OSS projects with a cross-sectional design. Admittedly, in order to get more insight into the dynamism of managing digital social innovation projects, future research could apply a longitudinal design to trace how the dynamic changes of project leaders influence project outcomes in addressing social needs. Due to the cross-sectional design, our analysis cannot testify the causation, but offers initial evidence for association. Future research with panel data may be able to establish temporal sequences and employ advanced techniques to test causal relationships underlying our theory.

## ACKNOWLEDGEMENTS

The authors thank the editor-in-chief Robert Davison, the guest senior and associate editors, and two anonymous reviewers for their comments and guidance. Also, thanks to the Hong Kong University of Science and Technology and the University of Groningen for partial financial support for conducting this research. Weifang Wu provided excellent research assistance for data collection. Any opinions, findings and suggestions expressed in this paper are those of the authors, which do not necessarily reflect the views of SourceForge.

## ORCID

John Qi Dong https://orcid.org/0000-0002-3169-7790

## ENDNOTES

$^{1}$ Some leaders of OSS projects are likely to be affiliated to organizations, such as software firms (Ho & Rai, 2017).

$^{2}$ One may argue that very large size of project leaders could require a lot of coordination and be detrimental to user downloads and recommendation ratio, implying an inverted U-shaped relationship. We do not hypothesize such a decline in H1 because in the OSS context, the size of project leaders is often small due to the shortage of financial incentives and the time-consuming emergence of project leaders (Eseryel & Eseryel, 2013). Thus, the coordination costs of leaders are not inevitably high in OSS projects. For example, in our large sample of 43 048 OSS projects the largest number of leaders in a project is 25. To formally address this concern, we tested the curvilinear effects of size of project leaders by adding its squared term to the regression model. Consistent with our arguments, we did not find support for an inverted U-shaped relationship, as shown in Appendix.

$^{3}$ One may ask if the temporal growth of a project can mitigate the impacts of the size of project leaders. To address this concern, we conducted a test by adding the interaction term between project age and the size of project leaders. Interestingly, we found that the size of project leaders has stronger, rather than weaker, effects when a project grows or matures (user downloads: $\beta = 1.041$ , P < .001; user recommendation ratio: $\beta = 0.040$ , P < .01).

$^{4}$ In Figure 1, increasing size of project leaders slightly reduces user downloads when they have a low level of network ties. This possible downside of size may be explained as coordination costs outweigh resource benefits in a larger group of project leaders without much access to external resources in the network. At the average level of networks ties, however, we did not find support for any negative or curvilinear effects of size on user downloads (see Model (1), Appendix). Thus, our results support H1a.

## REFERENCES

Abu-Saifan, S. (2012). Social entrepreneurship: Definition and boundaries. Technology Innovation Management Review, 2(2), 22–27.

Agarwal, N., & Rathod, U. (2006). Defining ‘success’ for software projects: An exploratory revelation. International Journal of Project Management, 24(4), 358–370.

Altuna, N., Contri, A., Dell'Era, C., Frattini, F., & Maccarrone, P. (2015). Managing social innovation in for-profit organizations: The case of Intesa Sanpaolo. European Journal of Innovation Management, 18(2), 258–280.

Becker, G. S. (1993). Human capital: A theoretical and empirical analysis, with special reference to education. Chicago, IL: University of Chicago Press.

Bennett, W. L., & Segerberg, A. (2012). The logic of connective action. Information, Communication and Society, 15(5), 739–768.

Bhatt, P., Ahmad, A. J., & Roomi, M. A. (2016). Social innovation with open source software: User engagement and development challenges in India. Technovation, 52(1), 28–39.

Bonaccorsi, A., & Rossi, C. (2003). Why open source software can succeed. Research Policy, 32(7), 1243–1258.

Boyd, B. (1990). Corporate linkages and organizational environment: A test of the resource dependence model. Strategic Management Journal, 11(6), 419–430.

Cajaiba-Santana, G. (2014). Social innovation: Moving the field forward. A conceptual framework. Technological Forecasting and Social Change, 82(1), 42–51.

Certo, S. T. (2003). Influencing initial public offering investors with prestige: Signaling with board structures. Academy of Management Review, 28(3), 432–446.

Certo, S. T., Daily, C. M., & Dalton, D. R. (2001). Signaling firm value through board structure: An investigation of initial public offerings. Entrepreneurship Theory and Practice, 26(2), 33–50.

Coleman, J. S. (1988). Social capital in the creation of human capital. American Journal of Sociology, 94, 95–120.

Crowston, K., Howison, J., & Annabi, H. (2006). Information systems success in free and open source software development: Theory and measures. Software Process: Improvement and Practice, 11(2), 123–148.

Daily, C. M., & Dalton, D. R. (1993). Board of Directors' leadership and structure: Control and performance implications. Entrepreneurship Theory and Practices, 17(3), 65–81.

Daily, C. M., McDougall, P. P., Covin, J. G., & Dalton, D. R. (2002). Governance and strategic leadership in entrepreneurial firms. Journal of Management, 28(3), 387–412.

Dalton, D. R., Daily, C. M., Ellstrand, A. E., & Johnson, J. L. (1998). Meta-analytic reviews of board composition, leadership structure and financial performance. Strategic Management Journal, 19(3), 269–290.

Dalton, D. R., Daily, C. M., Johnson, J. L., & Ellstrand, A. E. (1999). Number of directors and financial performance: A meta-analysis. Academy of Management Journal, 42(6), 674–686.

Daniel, S., & Stewart, K. (2016). Open source project success: Resource access, flow, and integration. Journal of Strategic Information Systems, 25(3), 159–176.

Datta, P. (2011). A preliminary study of E-commerce adoption in developing countries. Information Systems Journal, 21(1), 3–32.

Chiasson, M., & Davidson, E. (2005). Taking industry seriously in information systems research. MIS Quarterly, 29(4), 591–606.

Davison, R. M., Vogel, D. R., Harris, R. W., & Jones, N. (2000). Technology leapfrogging in developing countries: An inevitable luxury? Electronic Journal of Information Systems in Developing Countries, 1(5), 1–10.

Dawson, P., & Daniel, L. (2010). Understanding social innovation: A provisional framework. International Journal of Technology Management, 51(1), 9–21.

Dong, J. Q., McCarthy, K. J., & Schoenmakers, W. W. M. E. (2017). How central is too central? Organizing interorganizational collaboration networks for breakthrough innovation. Journal of Product Innovation Management, 34(4), 526–542.

Dong, J. Q., Wu, W., & Zhang, Y. S. (2019). The faster the better? Innovation speed and user interest in open source software. Information and Management, 56(5), 669–680.

Eseryel, U. Y., & Eseryel, D. (2013). Action-embedded transformational leadership in self-managing global information systems development teams. Journal of Strategic Information Systems, 22(2), 103–120.

Faraj, S., Kudaravalli, S., & Wasko, M. (2015). Leading collaboration in online communities. MIS Quarterly, 39(2), 393–411.

Fershtman, C., & Gandal, N. (2011). Direct and indirect knowledge spillovers: The ‘social network’ of open-source projects. RAND Journal of Economics, 42(1), 70–91.

Fleming, L., & Waguespack, D. M. (2007). Brokerage, boundary spanning, and leadership in open innovation communities. Organization Science, 18(2), 165–180.

Gabrielsson, J. (2007). Correlates of board empowerment in small companies. Entrepreneurship Theory and Practice, 31(5), 687–711.

Guiri, P., Rullani, F., & Torrisi, S. (2008). Explaining leadership in virtual teams: The case of open source software. Information Economics and Policy, 20(4), 305–315.

Goodstein, J., Gautam, K., & Boeker, W. (1994). The effects of board size and diversity on strategic change. Strategic Management Journal, 15(3), 241–250.

Grewal, R., Lilien, G. L., & Mallapragada, G. (2006). Location, location, location: How network embeddedness affects project success in open source systems. Management Science, 52(7), 1043–1056.

Hahn, J., Moon, J. Y., & Zhang, C. (2008). Emergence of new project teams from open source software developer networks: Impact of prior collaboration ties. Information Systems Research, 19(3), 369–391.

Haunschild, P. R., & Beckman, C. M. (1998). When do interlocks matter? Alternate sources of information and interlock influence. Administrative Science Quarterly, 43(4), 815–844.

Hillman, A. J., & Dalziel, T. (2003). Boards of directors and firm performance: Integrating agency and resource dependence perspectives. Academy of Management Review, 28(3), 383–396.

Hillman, A. J., Keim, G. D., & Luce, R. A. (2001). Board composition and stakeholder performance: Do stakeholder directors make a difference? Business and Society, 40(3), 295–314.

Hillman, A. J., Withers, M. C., & Collins, B. J. (2009). Resource dependence theory: A review. Journal of Management, 35(6), 1404–1427.

Ho, S. Y., & Rai, A. (2017). Continued voluntary participation intention in firm-participating open source software projects. Information Systems Research, 28(3), 603–625.

Hong, W., Chan, F. K. Y., Thong, J. Y. L., Chasalow, L. C., & Dhillon, G. (2014). A framework and guidelines for context-specific theorizing in information systems research. Information Systems Research, 25(1), 111–136.

Jiang, Q., Tan, C.-H., Sia, C. L., & Wei, K.-K. (2019). Followership in an open-source software project and its significance in code reuse. MIS Quarterly, 43(4), 1303–1319.

Johnson, J. L., Daily, C. M., & Ellstrand, A. E. (1996). Boards of directors: A review and research agenda. Journal of Management, 22(3), 409–438.

Johnson, S. L., Safadi, H., & Faraj, S. (2015). The emergence of online community leadership. Information Systems Research, 26(1), 165–187.

Kannothra, C. G., Manning, S., & Haigh, N. (2018). How hybrids manage growth and social-business tensions in global supply chains: The case of impact sourcing. Journal of Business Ethics, 148(2), 271–290.

Kessler, E. H., & Chakrabarti, A. K. (1996). Innovation speed: A conceptual model of context, antecedents, and outcomes. Academy of Management Review, 21(4), 1143–1191.

Khan, S., Lacity, M., & Carmel, E. (2018). Entrepreneurial impact sourcing: A conceptual framework of social and commercial institutional logics. Information Systems Journal, 28(3), 538–562.

Kohli, R., & Melville, N. P. (2019). Digital innovation: A review and synthesis. Information Systems Journal, 29(1), 200–223.

Lerner, J., & Tirole, J. (2002). Some simple economics of open source. Journal of Industrial Economics, 50(2), 197–234.

Li, Y., Tan, C.-H., & Teo, H.-H. (2012). Leadership characteristics and developers' motivation in open source software development. Information and Management, 49(5), 257–267.

Ljungberg, J. (2000). Open source movements as a model for organizing. European Journal of Information Systems, 9(4), 208–216.

Lynall, M. D., Golden, B. R., & Hillman, A. J. (2003). Board composition from adolescence to maturity: A multitheoretic view. Academy of Management Review, 28(3), 416–431.

Madon, S., & Sharanappa, S. (2013). Social IT outsourcing and development: Theorising the linkage. Information Systems Journal, 23(5), 381–399.

Majchrzak, A., Cooper, L. P., & Neece, O. E. (2004). Knowledge reuse for innovation. Management Science, 50(2), 174–188.

Meso, P., Musa, P., & Mbarika, V. (2005). Towards a model of consumer user of mobile information and communication technology in LDCs: The case of sub-Saharan Africa. Information Systems Journal, 15(2), 119–146.

Morrison, E. W. (2002). Newcomers' relationships: The role of social network ties during socialization. Academy of Management Journal, 45(6), 1149–1160.

Mulgan, G. (2006). The process of social innovation. Innovations: Technology, Governance, Globalization, 1(2), 145–162.

Mulgan, G., Tucker, S., Ali, R., & Sanders, B. (2007). Social innovation: What it is, why it matters and how it can be accelerated. London: Young Foundation.

Murray, R., Caulier-Grice, J., & Mulgan, G. (2010). The open book of social innovation. London: National Endowment for Science, Technology and the Art.

Nyman, L., & Mikkonen, T. (2011). To fork or not to fork: Fork motivations in SourceForge projects. International Journal of Open Source Software Process, 3(3), 1–9.

O'Mahoney, S., & Ferraro, F. (2007). The emergence of governance in an open source community. Academy of Management Journal, 50(5), 1079–1106.

Pearce, J. A., & Zahra, S. A. (1992). Board composition from a strategic contingency perspective. Journal of Management Studies, 29(4), 411–438.

Peng, G., Wan, Y., & Woodlock, P. (2013). Network ties and the success of open source software development. Journal of Strategic Information Systems, 22(4), 269–281.

Pfeffer, J. (1973). Size, composition, and function of hospital boards of directors: A study of organization-environment linkage. Administrative Science Quarterly, 18(3), 349–364.

Pfeffer, J., & Salancik, G. (1978). The external control of organizations: A resource-dependence perspective. New York, NY: Harper and Row.

Pol, E., & Ville, S. (2009). Social innovation: Buzz word or enduring term? Journal of Socio-Economics, 38(6), 878–885.

Qureshi, I., Kistruck, G. M., & Bhatt, B. (2016). The enabling and constraining effects of social ties in the process of institutional entrepreneurship. Organization Studies, 37(3), 425–447.

Qureshi, I., Sutter, C., & Bhatt, B. (2018). The transformative power of knowledge sharing in settings of poverty and social inequality. Organization Studies, 39(1), 1575–1599.

Roberts, J. A., Hann, I. H., & Slaughter, S. A. (2006). Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the apache projects. Management Science, 52(7), 984–999.

Rose, J., Persson, J. S., Heeager, L. T., & Irani, Z. (2015). Managing E-government: Value positions and relationships. Information Systems Journal, 25(5), 531–571.

Sanders, W. M. G., & Carpenter, M. A. (1998). Internationalization and firm governance: The roles of CEO compensation, top team composition, and board structure. Academy of Management Journal, 41(2), 158–178.

Singh, J. (2005). Collaborative networks as determinants of knowledge diffusion patterns. Management Science, 51(5), 756–770.

Singh, P. V., & Tan, Y. (2010). Developer heterogeneity and formation of communication networks in open source software projects. Journal of Management Information Systems, 27(3), 179–210.

Sojer, M., & Henkel, J. (2010). Code reuse in open source software development: Quantitative evidence, drivers, and impediments. Journal of the Association for Information Systems, 11(12), 868–901.

Stahl, B. C., Boherty, N. F., & Shaw, M. (2012). Information security policies in the U.K. healthcare sector: A critical emulation. Information Systems Journal, 22(1), 77–94.

Stewart, K. J., & Gosain, S. (2006). The impact of ideology on effectiveness in open source software development teams. MIS Quarterly, 30(2), 291–314.

Stilgoe, J., Owen, R., & Macnaghten, P. (2013). Developing a framework for responsible innovation. Research Policy, 42(9), 1568–1580.

Sun, S. L., & Im, J. (2015). Cutting microfinance interest rates: An opportunity co-creation perspective. Entrepreneurship Theory and Practice, 39(1), 101–128.

Swamy, R. (1990). The makings of a social entrepreneur: The case of Baba Amte. Vikalpa, 15(4), 29–38.

Tim, Y., Pan, S. L., Ractham, P., & Kaewkitipong, L. (2017). Digitally enabled disaster response: The emergence of social media as boundary objects in a flooding disaster. Information Systems Journal, 27(2), 197–232.

Varadarajan, R. (2014). Toward sustainability: Public policy, global social innovations for base-of-the-pyramid markets, and demarketing for a better world. Journal of International Marketing, 22(2), 1–20.

Von Hippel, E. (2001). Open source shows the way: Innovation by and for users—no manufacturer required. MIT Sloan Management Review, 42(4), 82–86.

Zahra, S. A., Gedajlovic, E., Neubaum, D. O., & Shulman, J. M. (2009). A typology of social entrepreneurs: Motives, search processes and ethical challenges. Journal of Business Venturing, 24(5), 519–532.

Zahra, S. A., & Pearce, J. A. (1989). Boards of directors and corporate financial performance: A review and integrative model. Journal of Management, 15(2), 291–334.

Zheng, Y., & Yu, A. (2016). Affordances of social media in collective action: The case of free lunch for children in China. Information Systems Journal, 26(3), 289–313.

Zhu, F., & Zhang, X. (2010). Impact of online consumer reviews on sales: The moderating role of product and consumer characteristics. Journal of Marketing, 74(2), 133–148.

## AUTHOR BIOGRAPHIES

John Qi Dong is Chair & Professor of Business Analytics at the Trinity Business School at Trinity College Dublin, University of Dublin. His research interests include business analytics, digital innovation and a variety of topics related to behavioural strategy. His work has been published or is forthcoming in MIS Quarterly, Strategic Management Journal, Journal of Management, Journal of Management Information Systems, Journal of the Association for Information Systems, Journal of Product Innovation Management, European Journal of Information Systems, Information Systems Journal, and Journal of Strategic Information Systems, among others. He serves as Associate Editor for MIS Quarterly and Journal of the Association for Information Systems.

Sebastian Johannes Götz is a Senior Consultant at Syngroup Management Consulting GmbH. His research interests are focused on open source software. His work is forthcoming in Information Systems Journal.

How to cite this article: Dong JQ, Götz SJ. Project leaders as boundary spanners in open source software development: A resource dependence perspective. Inf Syst J. 2020;1–23. https://doi.org/10.1111/isj.12313

## APPENDIX: TESTING CURVILINEAR EFFECTS OF SIZE OF PROJECT LEADERS

<table><tr><td></td><td>(1)DV: User downloads</td><td>(2)DV: User recommendation ratio</td></tr><tr><td>Size of project leaders</td><td>0.308***(0.074)</td><td>0.140***(0.015)</td></tr><tr><td>Size of project leaders squared</td><td>0.081(0.085)</td><td>-0.023(0.017)</td></tr><tr><td>Tenure of project leaders</td><td>0.104***(0.010)</td><td>0.004+(0.002)</td></tr><tr><td>Developer effort</td><td>0.027***(0.004)</td><td>0.019***(0.001)</td></tr><tr><td>Project description</td><td>0.096***(0.013)</td><td>0.023***(0.003)</td></tr><tr><td>User diversity</td><td>0.091***(0.026)</td><td>0.050***(0.005)</td></tr><tr><td>Project size</td><td>0.836***(0.003)</td><td>0.028***(0.001)</td></tr><tr><td>Code reuse</td><td>-0.027(0.119)</td><td>-0.046(0.024)</td></tr><tr><td>License diversity</td><td>-0.172***(0.046)</td><td>0.034***(0.009)</td></tr><tr><td>Initial release time</td><td>2.125***(0.038)</td><td>0.067***(0.008)</td></tr><tr><td>Update frequency</td><td>1.442***(0.049)</td><td>0.191***(0.010)</td></tr><tr><td>Project age</td><td>1.026***(0.014)</td><td>-0.020***(0.003)</td></tr><tr><td>Constant</td><td>-7.329***(0.117)</td><td>0.104***(0.024)</td></tr><tr><td> $R^2$ </td><td>.755</td><td>.132</td></tr><tr><td>Adj.  $R^2$ </td><td>.755</td><td>.131</td></tr><tr><td>F</td><td>11 037.340***</td><td>543.860***</td></tr><tr><td colspan="3">Note: N = 43 048. Standard errors are in parentheses. $^+P < .1$ .***P &lt; .001.</td></tr></table>
