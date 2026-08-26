---
otero_id: 4424
otero_key: "V6EXWZD7"
title: "Open source project success: Resource access, flow, and integration"
authors: "Sherae Daniel; Katherine Stewart"
year: "2016"
journal: "The Journal of Strategic Information Systems"
doi: "10.1016/j.jsis.2016.02.006"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Open source project success: Resource access, flow, and integration

Sherae Daniel <sup>a,</sup>⇑, Katherine Stewart <sup>b</sup>

<sup>a</sup> University of Cincinnati, 2925 Campus Green Dr, Cincinnati, OH 45221, United States

<sup>b</sup> University of Maryland, 7621 Mowatt Ln, College Park, MD 20740, United States

## a r t i c l e i n f o

Article history: Received 5 March 2015 Received in revised form 22 December 2015 Accepted 16 February 2016 Available online xxxx

Keywords: Project co-membership Project success Open source software Resources Knowledge

## a b s t r a c t

Open source software projects share key resources including knowledge and developer attention. Developers who participate on multiple projects create ties among projects and facilitate access to those projects’ resources. However, projects also compete for developer attention, and they vary in their ability to integrate knowledge. This paper explores how factors that facilitate knowledge integration (low software coupling and high interactive discussion) impact project success and how developers’ attention to external projects may dampen a focal project’s success. Further, we explore how these factors may moderate the positive impact of a project’s network degree centrality to develop a more nuanced model of their influences on project success. Using data from 175 OSS projects we find that software coupling, interactive discussion and externally focused developer attention directly impact completed code commits. Interactive discussion also amplifies the benefit of high network degree centrality, while developers’ external attention weakens the positive impact of high network degree centrality. Results add to theory by providing a more nuanced view of how key strategic resources (knowledge and attention) drive OSS success. In particular it describes how knowledge integration ability, developer attention, and network degree centrality interact to influence project outcomes.

 2016 Published by Elsevier B.V.

## Introduction

Open source software (OSS) development has emerged as a viable model for creating and distributing software, transforming the software industry (Kogut and Metiu. 2001: Morgan and Finnegan. 2014: West. 2003) and serving as inspiration for adoption of more open practices in other domains (Von Krogh and Hippel, 2006). As such, OSS has had and continues to have significant impact on the strategy of firms in the software industry (Casadesus-Masanell and Ghemawat, 2006; Morgan and Finnegan, 2014; Von Krogh and Spaeth, 2007), and effectively managing the use and development of OSS is critical to success for many such firms (Dahlander and Magnusson, 2005; Gulati et al., 2012). Important strategic resources for organizations include knowledge (Grant, 1996) and attention (Ocasio, 1997); similarly, key resources that have been identified in the OSS setting are knowledge (Singh et al., 2011) and developers (Ke and Zhang, 2009). Recent work focuses on an OSS project’s network as a crucial source of resources facilitating project success (Grewal et al., 2006; Mallapragada et al., 2012; Singh et al., 2011). Several studies have shown positive effects of network degree centrality and argued that these result from access to knowledge (Singh et al., 2011). Other work has shown that increasing numbers of developers and developer effort has a positive effect on OSS project outcomes (Chengalur-Smith et al., 2010; Crowston and Scozzi, 2002) and that developers attention may be attracted through network connections (Hahn et al., 2008).

While research has established the importance of knowledge and developers as key resources, and the potential benefits of attaining these resources through network connections, little work examines the factors that allow an OSS project to effectively leverage those resources, or the possibility of losing resources to other projects in the network. Past work makes the implicit assumption that access to network knowledge equates to use of that knowledge (Grewal et al., 2006; Singh et al., 2011). However, research in the broader management literature establishes that individuals and groups vary in their ability to integrate and use new knowledge (Gulati et al., 2011; Lee et al., 2001; Pil and Leana, 2009; Reinholt et al., 2011). Knowledge integration refers to the combination of multiple sources of knowledge in a meaningful way (Alavi and Tiwana, 2002; Grant, 1996). A highly connected OSS project may fail to benefit from network knowledge access if the project developers experience difficulty integrating that knowledge. We argue that software structure and interaction among project participants are critical to knowledge integration capabilities, and ask how do these factors affect the extent to which a project benefits from its network connections?

Integrating knowledge into an OSS product requires effort from developers. Past work has shown that developers may be accessed via network connections without considering that, unlike knowledge, their attention is a limited (Ocasio, 2011) and a rival resource (Ocasio, 1997). While developers may contribute to multiple projects, the time they spend on one project cannot be spent on another, implying that while some projects may gain developer resources via network connections, others may lose those resources. We argue that developer engagement in project discussions indicates the level of attention a developer is devoting to a project and ask how does the proportion of developer engagement in external projects (vs. the focal project) influences project technical success?

The main contribution of this work is extending prior research to consider conditions under which projects may benefit more or less from resources available in the network, or may suffer detrimental consequences from resource flows away from a project. We draw on the literature that points to knowledge (Grant, 1996) and attention (Ocasio, 1997) as key strategic resources as well as recent work on consequences related to network participation (Trkman and Desouza, 2012). We highlight the importance of knowledge integration to enhance the benefit from knowledge access, and we explore the implications of developers’ attention shifting away from a focal project to other projects in the network.

The following sections describe OSS projects in general, explain why developers’ external attention, knowledge access and knowledge integration are important factors influencing the success of an OSS project, and describe the nature of OSS project network connections. We then hypothesize how technical success in the form of completed code modifications is influenced by network degree centrality, knowledge integration factors (software coupling and the level of interaction among project participants in a focal project), and the proportion of their attention developers devote to a focal project versus other projects. Section ‘Methodology’ describes the empirical study, and results suggest that projects benefit more from network degree centrality (knowledge access) when they have higher levels of interactive discussion, and less when developers external attention is higher.

## Resources for success in OSS: knowledge and attention

## What is ‘‘success” in OSS?

OSS projects focus on creating software applications. As such, outcomes related to the code created by a project have been viewed as crucial indicators of project success (Singh et al., 2011). Researchers have typically measured outcome variables that tap how much code an open source project generates, how many additions are made to the code, or how many bugs are fixed (Giuri et al., 2010; Grewal et al., 2006; Midha and Palvia, 2012; Singh et al., 2011). More broadly, completing individual code modifications, which may represent additions, changes, or deletions, has frequently been viewed as a key indicator of the progress of an OSS project (Giuri et al., 2010; Grewal et al., 2006; Singh et al., 2011; Yang et al., 2013). Completing modifications related to building the application precedes a project reaching other goals, such as achieving quality and gaining market share (Méndez-Durón and García, 2009; Setia et al., 2012; Subramaniam et al., 2009). As such, completing code modifications is of significant strategic importance for OSS projects. Thus we concentrate our theorizing around a project’s ability to achieve ‘‘technical success” in terms of completed code modifications, and focus on two key resources needed to develop code: knowledge and developer attention.

## Knowledge in OSS

Creating a software product requires significant knowledge resources (Patnayakuni et al., 2007; Sandhawalia and Dalcher, 2010: von Krogh et al., 2003) including “know-what." such as a knowledge of functional requirements, and “know-how." such as an understanding of programming principles (Rogers, 1995; Tornatzky and Fleischer, 1990). To attain technical success software projects must gain access to this knowledge. For this reason, past work explores how access to knowledge impacts OSS technical success and how knowledge enters OSS projects (Haefliger et al., 2008; Singh et al., 2011).

While traditional software development projects are housed within organizations that may provide a base of knowledge and a structure for drawing the needed knowledge into a project, many OSS projects exist outside traditional organizations.

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

OSS applications are publicly available and may be edited or redistributed by anyone (Chan and Husted, 2010; von Krogh and Hippel, 2003), making them an example of a ‘‘commons-based peer production project” (Benkler and Nissenbaum, 2006). OSS projects use public repositories to facilitate development work, and they allow participants to come and go (Seidel and Stewart, 2011). As such OSS projects may draw knowledge from a wide range of individual contributors (Ye and Kishida, 2003) and from a broad array of other open source projects (Singh et al., 2011). Individuals introduce knowledge into an OSS project by contributing to a project’s core artifact (i.e. code) or posting comments in project discussions (Hann et al., 2013; Okoli and Oh, 2007). Prior work differentiates between core developers, who make the most changes to code and tend to hold decision authority, and peripheral developers, who generally make fewer and smaller contributions, e.g. through participating in discussions and providing information about bugs (Gallivan, 2001; Setia et al., 2012), but not making changes to the code. Given their relatively high level of involvement, developers are especially important to furthering the goals of an OSS project, and a project must attract their attention to successfully integrate knowledge into a working application.

## OSS developer attention

Attention is ‘‘noticing, encoding, interpreting, and focusing of time and effort” (Ocasio, 1997). More simply, attention refers to time and effort expended on an object (Ocasio, 1997). Attention has been identified as a key strategic resource (Ocasio, 1997). Attention is a resource that can be unequally distributed across many kinds of objects including people, organizations, subsidiaries, ideas or documents (Bouquet and Birkinshaw, 2008; Davenport and Beck, 2000; Derber, 2000; Goldhaber, 1997; Hansen and Haas, 2001; Hoffman and Ocasio, 2001). Developer attention to a project may take the form of crafting and integrating software code, discussing project issues, or guiding newcomers (Ducheneaut, 2005; Fang and Neufeld, 2009).

A developer cannot write code for an OSS project without interpreting the existing code and expending time and effort on modifying or extending it. Prior research has highlighted the value of developer attention and effort in determining the level of OSS projects’ success. For instance, many studies use the number of listed developers as a predictor of OSS success (Chengalur-Smith et al., 2010; Crowston and Scozzi, 2002; Subramaniam et al., 2009), and Sen et al. (2012) argue that having many developers facilitates the easy identification and correction of errors. Thus to successfully integrate new knowledge into a working software product requires the attention of developers.

However, attention is a scarce resource in organizations generally (Barnett, 2008; Hansen and Haas, 2001; Ocasio, 1997, 2011; Simon, 1947) and OSS projects specifically (Benkler, 2002). OSS developer resources are limited (Peng et al., 2013b). Unlike knowledge that may be shared without being depleted, developers’ attention is finite. Developers often act as volunteers when they contribute to OSS projects and can therefore easily abandon projects. Given the hundreds of thousands of OSS projects on some platforms (e.g., see www.SF.net) and associated competition for attention, attracting attention to an OSS project may represent a challenge (O’Leary et al., 2011; Santos et al., 2013; Wang et al., 2013).

Among the many OSS projects that may be active on a platform, how does a developer decide where to devote his attention? Most literature addressing this question has focused on motivating factors such as utility of the software in meeting some developer need (Stewart et al., 2006a), developer identification with the project (Stewart and Gosain, 2006), and reputation or monetary benefits (Roberts et al., 2006). Hahn et al. (2008) examined project networks and found that developers are more likely to get involved in new projects if they have previously worked with the founder of the new project in another project. However, it was outside the scope of their work to consider the implications for those other projects, e.g., if a developer ‘‘follows” another developer to a new project, what does that mean for the first project? While prior research frequently demonstrates that more developer attention (e.g. number of developers or amount of developer effort) on a project is better (Chengalur-Smith et al., 2010), it does not consider how a developer’s attention may move from one project to another (Chua and Yeow, 2010; Grewal et al., 2006).

The shaded boxes in Fig. 1 represent the theoretical concepts discussed above. The white boxes show the specific constructs about which we develop hypotheses in the next section.

## Hypotheses

## Ease of knowledge integration

Creating source code relies on knowledge creation through knowledge integration processes (Nonaka, 1994; Patnayakuni et al., 2006; Sandhawalia and Dalcher, 2010). Since knowledge integration refers to the effective combination of multiple sources of knowledge, successful knowledge integration depends on both pre-existing, knowledge and on knowledgesharing practices (Nonaka, 1994; Sandhawalia and Dalcher, 2010). We posit that characteristics of pre-existing knowledge and knowledge sharing practices influence the ease or difficulty of integrating new knowledge. In the case of OSS, incorporating new contributions requires integration with existing application functions (Fang and Neufeld, 2009), thus we focus on the existing application as an important reserve of pre-existing knowledge (Gendreau and Robillard, 2009; Haefliger et al., 2008). The structure of the existing code is a factor that may influence project success because it determines the ease with which new code can be integrated. In OSS projects knowledge sharing is typically accomplished via project discussion channels, so we focus on the extent to which developers interact through those channels as an important aspect of knowledgesharing practices (Kuk, 2006).

![](/api/attachments/V6EXWZD7/fulltext/images/427e9c91dd80116aa6e7f70a06dd2a34753f1dfee824bfcfdce8471eb2992878.jpg)  
Fig. 1. Research model.

## Software coupling

As a base of existing knowledge, code represents both a potential aid to understanding how to contribute to a project and also the structure into which new contributions must be integrated (Morner and Krogh, 2009). Characteristics of existing knowledge influence the creation of new knowledge (Nonaka, 1994), and in the case of source code modularity is an important characteristic (Baldwin and Clark, 2006). In general, modularity refers to dividing the components of a system according to some plan in such a way as to ease future modifications (Baldwin and Clark, 2006). Structural complexity is an aspect of modularity that has been shown to have a significant impact on the ease with which developers can integrate new code (Benkler, 2002; Darcy et al., 2005; MacCormack et al., 2006). Structural complexity stands out as especially crucial in the OSS setting for two reasons. First, potentially high turnover in OSS projects (Howison et al., 2006; von Krogh et al., 2003) limits the time participants can devote to develop the tacit, project-specific knowledge needed to work efficiently and effectively with a very complex product (Flanagan et al., 2007; Sandhawalia and Dalcher, 2010). Second, because developers join and leave at will, and may be geographically distributed, coordination challenges may surface. Product structure may func tion as a coordination mechanism, reducing further coordination needs (Amrit and Hillegersberg, 2010; Bolici et al., 2009).

Minimizing the structural complexity of source code facilitates understanding, modification, and maintenance (Baldwin and Clark, 2006: Darcy et al. 2005: MacCormack et al. 2006) Coupling is an important aspect of structural complexity that represents the relationships between program elements. Coupling is conceptualized as the ‘relatedness’ of elements to other elements (Hutchens and Basili, 1985). If a developer needs to modify a program element such as a class, then the developer must also understand how the class interacts with the other program elements to which it is coupled. It is easiest for the developer to understand and modify the class if it is not coupled to any other elements. If the class is not coupled the developer need only understand that one element. If it is coupled with one other element then the developer would need to understand two elements to modify the class. For these reasons, the level of coupling within the software has been identified as especially crucial to the ease or difficulty of understanding code and integrating new code (Darcy et al., 2005). Higher coupling indicates higher structural complexity. When a design allows completion of smaller tasks without understanding the entire product, developers can integrate new ideas and functions quickly (Benkler, 2002). Because it inhibits knowledge integration:

H1. OSS project software coupling will be negatively associated with OSS project completed code modifications.

## Interactive discussion

Although an idea forms in an individual mind, ideas mature through interaction among individuals (Nonaka, 1994). Interactive discussion among individuals facilitates knowledge generation, combination, and transfer (Griffith and Sawyer, 2010). OSS projects generally include online channels such as threaded discussion forums to facilitate the interaction necessary for maturing ideas (Sack et al., 2006). OSS researchers note that interactions via mailing lists and public forums are a key part of the software development process (Howison and Crowston, 2014; Yamauchi et al., 2000). Interactive discussion represents an important means of knowledge sharing and integration for OSS projects (Dahlander and O’Mahony, 2011; Kuk, 2006). By breaking down complex ideas and providing an organizational memory (Yamauchi et al., 2000) interactive discussion can help a new developer or a developer with a new idea to integrate code quickly (Mallapragada et al., 2012). Thus, interactive discussions allow developers to bring together multiple sources and types of knowledge and combine them with existing project knowledge to improve functionality (Chua and Yeow, 2010; Mallapragada et al., 2012). The following quotes from the discussion forums of the Chakra project provide an example of how participants may use discussion forums to facilitate the kind of technical problem solving needed for code development (italics added).

Post: ‘‘as of now the stuff in qmlport branch is just some parts of the interface + dummydata, it needs to be connected to the installerLogic.

this is how the qml stuff is implemented atm:. . .

This is my proposal how to connect the stuff to the installer:. . .

i wanted to discuss this first, before i try to connect the qml-part with the installer logic, because i don’t know the code of the installer part well.”

Reply: ‘‘installhandler.cpp is the main code to handle the bash-backend. Here some examples:. . .

m\_postcommand are the switches added by installationhandler which the user creates during the setup. So if you say you want to use java or another language you can convert the bash-scripts to java-scripts or what ever language you prefer. We had just some developers knowing bash better than cc + so the backend was bash.

The logic is simple: UI collects the data > installhandler reads the data and generates the switches > bash-backend does the action.

I attached a installation.log to this mail.”

The first participant makes a proposal and asks for feedback, noting he needs a greater understanding of existing code to accomplish the task. Another participant provides an explanation as to why development choices were made in the past and examples of how the task can be accomplished. While discussion is clearly important to facilitating development work, OSS projects vary significantly in their level of interactive discussion. Some hold substantial interactive discussions; others remain quiet. We hypothesize:

H2. Interactive discussion among OSS project participants will be positively associated with completed code modifications.

## Attention

A project may have many associated developers, but if they focus their attention elsewhere, it is unlikely that application development will move forward. The tradeoffs developers make in terms of attention paid to one project versus another may be indicated by traces of their participation in those projects’ forums. Even if a focal developer does not hold a developer role on another project, his participation in other projects represents attention being devoted to those projects, and acting as a peripheral contributor in discussions may indicate a shifting focus. Prior research describes the important role that forum participation plays in the path individuals travel to become a core developer (von Krogh et al., 2003). Von Krogh et al. (2003) show how those who become developers in the Freenet OSS project often begin their project participation by contributing to the project discussions. Similarly Dahlander and O’Mahony (2011) find that participating in technical discussions leads to becoming a member of the GNOME leadership. Thus peripheral participation generally precedes joining the core development group of a project.

Interactive discussion has been generally recognized as a means for focusing attention (Ocasio, 1997), and Klamer and Dalen (2002) argue that attention attracted by an object (in our case, an OSS project) can be detected through examination of the signals that relate to the object. We suggest that participation in project discussions represents an important signal of attention and as the proportion of developers’ participation in project discussion forums shifts away from the focal project toward other projects, the success of the focal project will be compromised. Because developers may freely shift their attention among projects, and participation in discussions is both a signal of attention paid to a project and a means of indicating the intent to devote further attention to a project, we hypothesize:

H3. As developer external attention increases completed code modifications in the focal project will decrease.

## Potential resource flow (knowledge and developer attention): network degree centrality

While OSS projects have stores of knowledge and attention available within the bounds of the project (e.g., code repositories, developers), a growing body of work has highlighted connected OSS projects as additional pools of resources (Sojer and Henkel, 2010). This work supports the view that increasing network degree centrality is associated with increasing access to network knowledge (Liu and Iyer, 2007; Mallapragada et al., 2012; Singh et al., 2011) and developer attention (Hahn et al., 2008). In addition to the potential direct benefit of accessing resources in the network, we consider how the influence of network degree centrality may be moderated by knowledge integration ability (as indicated by interactive discussion and software coupling within a project) and the degree to which developers are attending to a focal project versus others (as indicated by the proportion of their participation outside the focal project).

OSS projects often exist within networks composed of many interconnected teams or individuals working on distinct projects (Grewal et al., 2006; Hu et al., 2012; Oh and Jeon, 2007). Most work on OSS networks considers connections that are formed between projects when one participant acts as a developer on two or more projects (Peng and Dey, 2013; Singh et al., 2011). Given their primary role in furthering the project’s application development, connections formed by core developers represent an important indicator of projects’ access to resources in their networks (Grewal et al., 2006; Liu and Iyer, 2007; Peng and Dey, 2013; Singh and Phelps, 2013; Singh et al., 2011).

A developer connection to another OSS project can facilitate knowledge flow both into and out of the focal project (Méndez-Durón and García, 2009). However, we expect the overall effect of connections to be positive for several reasons. Being listing as a developer is generally an indication of significant contribution to a project (Crowston and Howison, 2006), so our baseline assumption is that an individual who forms a tie is committed to and contributes to both projects. Through his connections to other projects, a focal project developer may identify explicit knowledge in the form of documented ideas (Kuk, 2006) or technical artifacts such as code (Haefliger et al., 2008; Howison and Crowston, 2014) that he can import into the focal project, Second, by participating in multiple proiects, a developer can learn from an array of development methods (Singh et al., 2011). He gains tacit knowledge through hands-on experience in related contexts (Nonaka and Toyama, 2003). Experience gained working on other projects increases the developer’s store of knowledge, which he can then apply in the development of the focal project application. Given the wider breadth of experience that a developer on multiple projects has access to, he will be better prepared to make whatever contributions he makes to the focal project. Further, increased network connections can reduce search costs and allow developers to find useful information faster. H4 seeks to replicate prior findings regarding the positive effect of access to knowledge in a project’s network (Singh et al., 2011) and serves as the starting point for developing a more refined model that considers how knowledge integration capabilities may enhance the benefit of network degree centrality, while external attention may reduce it.

## H4. OSS project network degree centrality will be positively associated with completed code modifications.

H4 suggests that developer connections among projects facilitate the flow of resources to a focal project thereby enhancing developers’ ability to complete code modifications. However, in addition to increasing access to resources, growing network degree centrality may create a more complex environment in which developers must work to make code additions. As the knowledge available to a project through its network connections increases, the challenges of integrating it will also increase. To the degree that network degree centrality increases, the increasing number and diversity of alters implies a wider range of knowledge available to the focal project. More diverse knowledge is more difficult to absorb because it is harder to relate to existing knowledge (Reagans and McEvily, 2003; Singh et al., 2011). Diverse knowledge is harder to relate to the existing knowledge because it is less likely to be immediately compatible with the existing knowledge base. Thus diverse knowledge gained through an extensive network may require significant coordination and contextualization in order to be useful (Barbagallo et al., 2008). As the average time and effort required for each knowledge integration task increases with increasing knowledge diversity, it is logical to believe that less of the knowledge available via the network will be utilized (especially given developer time constraints). So, when code is easy to integrate a project should be better able to make use of network resources.

H1 suggests that low software coupling, because it makes code development easier, will ease the integration of new knowledge into a product. Low software complexity can make the integration of diverse knowledge and thus code modifications easier. Thus we propose that the more efficiently changes can be made to the software, (that is, the lower the level of software coupling), the more a project will be able to take advantage of the increases in diverse knowledge available via increases in degree centrality. If a project has high software coupling, the access to network resources will still facilitate code modifications, but not to the same extent as it would if the project had low software coupling because the diverse knowledge is difficult to integrate.

H5. The positive impact of network degree centrality on completed code modifications is stronger when software coupling is low.

H4 developed the argument that developer connections among projects facilitate the flow of resources to a focal project thereby enhancing success, and H5 argued that this relationship is moderated by software coupling because low coupling facilitates knowledge integration. Similarly, H2 argued that interactive discussion eases knowledge integration. We now argue that the relationship between developer connections and success is moderated by interactive discussion also.

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

Interactive discussion can help participants plan interactions, delegate tasks and avoid duplication of work in OSS projects (Crowston et al., 2007; Zhang and Wang, 2012). The need for such coordination increases as knowledge access increases. For example, an extensive network may yield many potentially viable feature ideas, but some of them may conflict with each other and require developers to prioritize additions. Participants may use the discussion space to debate if and when to add functions (Fielding, 1999). Consequently, the extent to which knowledge from the network is translated into completed code modifications depends on interactive discussion. When there is high interactive discussion the impact of developer connections on success will be more positive than when there is low interactive discussion.

In addition to providing the increasing coordination needed to leverage knowledge, interactive discussion can also motivate individuals on alter projects to contribute to the focal project. The knowledge available through a project’s network connections can exist in both other projects’ repositories (e.g., other projects’ code or documentation), and in the minds of the individuals associated with other projects. These individuals represent a potential source of direct contribution to the focal project. Interactive discussion motivates these potential newcomers and makes them feel welcome (Howison and Crowston, 2014), which encourages them to contribute their knowledge to the development of the application (Burke et al., 2010). Thus there are two mechanisms by which interactive discussion may enhance the extent to which a project benefits from its network of connections: interactive discussion makes the project more appealing to individuals in alter projects such that they will be more inclined to contribute to the focal project, and it facilitates the integration of their contributions and other knowledge that may be gleaned from alters.

H6. The positive impact of network degree centrality on completed code modifications is increased in the presence of high levels of interactive discussion.

Finally, we believe that the relationship described in H4 suggesting that developer connections among projects facilitate the flow of resources to a focal project thereby enhancing success is also altered by developer external attention. While developer participation on multiple projects provides learning opportunities and access to knowledge (Singh et al., 2011), it also provides a path for knowledge to flow away from the focal project (Méndez-Durón and García, 2009). Thus for a given level of network degree centrality, the benefits a project sees from its connections may depend on the extent to which knowledge gleaned from alters is applied to the focal project versus knowledge gleaned on the focal project is applied to alters, as was suggested by the hypothesized effect of the proportion of developer participation outside the focal project in H3. We suggest that the competing demands individuals occupying developer roles on multiple projects face (Peng et al., 2013b) may also lead to an interaction effect between network degree centrality and the proportion of developer participation outside the focal project.

When focal project developers are listed as developers on external projects, attention as indicated by participation in discussions may also imply attention devoted to development tasks such as creating new features or fixing bugs. For projects with a low proportion of developer participation outside the project, increases in network degree centrality indicate increasing access to resources without a high level of competition for the developers’ time and effort. However, for projects that have a high proportion of participation outside the project, the benefits of increasing network degree centrality may be weaker because the high level of external participation indicates that developers may be focusing more of their time and effort on alter projects. Thus more resources may be flowing away from the focal project than toward it. As the balance of participation in discussions shifts away from the focal project to external projects, the balance of development effort and knowledge flow may also shift. Hence we suggest that the benefits of increasing network degree centrality will be greater when a project’s developers have a relatively low level of participation on other projects than when they participate on other projects more actively.

H7. The developer external attention dampens the positive impact of network degree centrality on completed code modifications.

## Methodology

Data and sample construction

As part of a larger research effort (Stewart et al., 2006b), we began tracking a set of OSS projects hosted on SourceForge (www.SourceForge.net) in 2002. Leveraging that dataset for this study provides a number of advantages. First, SourceForge facilitates the formation of network connections across projects by providing developers a centralized place to distribute applications and manage development. SourceForge offers communication tools, version control processes, and repositories for source code, This provides some consistency across projects, allowing us to collect comparable measures of the variables of interest. Second, researchers at the University of Notre Dame archive data on SourceForge projects and using this database avoids the problem of instability that researchers may encounter when scraping data from the website (e.g., there is historical data on individual’s associations with projects rather than only a snapshot of who is a developer currently) (Van Antwerp and Madey, 2008). Third, in our earlier work, extensive efforts were taken to thoroughly clean the dataset (e.g., manual inspection of every code file posted by the project to eliminate files not part of the focal application release), which allows

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

us to have greater confidence in our measure of software coupling as well as include important control variables (e.g., application size in lines of code). Finally, researchers frequently use SourceForge, facilitating an accumulation of knowledge across many studies (Chengalur-Smith et al., 2010; Daniel et al., 2013; Fershtman and Gandal, 2011; Grewal et al., 2006; Lerner and Tirole, 2005; Mallapragada et al., 2012; Peng and Mu, 2011; Singh et al., 2011; Wen et al., 2013; Zhang et al., 2013). Possible limitations related to the timing of data selection are discussed below.

To limit variability in performance due to differences in the focus of the project (e.g., end user entertainment versus software development tools), we selected projects from the two largest problem domains listed on SourceForge, ‘‘Internet” and ‘‘Networking,” both of which are of general interest to the technical audience that has formed the core of the open source movement. To avoid variability due to the project programming language, we selected projects built with one of the most popular languages, C++ or Java. Projects written in these languages tend to have higher activity levels than projects written in other languages (Subramaniam et al., 2009). Some projects represent multiple parallel development streams that are difficult to disentangle, and because variables were measured at the level of the SourceForge project, those measures could not be assigned to a single subproject. For this reason, projects that appeared to be a sub-project of a larger project or that appeared to be an umbrella project for smaller efforts were eliminated.

The SourceForge platform was created in 1999, and a variety of different types of projects use it. To center the analysis on projects that represent the open source movement, we include only projects that used Open Source Initiative-approved licenses. The majority of projects listed on SourceForge are inactive (English and Schweik, 2007; Fershtman and Gandal, 2011). To ensure we included only projects that generated software, we sampled only projects that released an initial software version by the end of 2002. Applying the selection criteria generated a total of 175 projects.

## Measurement

Archival data were drawn from the SourceForge Research Data Archive (Van Antwerp and Madey, 2008) to measure network degree centrality, the level of interactive discussion, posting activity directed to other projects and technical success and some control variables (described below). We analyzed source code to measure coupling and one control variables: lines of code (LOC). The code measures were calculated using Scientific Toolwork’s Understand (version 1.4). The independent and moderator variables were observed in 2002 and the dependent variable was measured in 2003.

## Dependent variable: completed code modifications

Knowledge creation in the form of completed code modifications is the relevant aspect of technical success in this study. Consistent with other OSS studies, we capture Concurrent Versions System (CVS) commits as an indicator of development in the OSS context (Giuri et al., 2010; Grewal et al., 2006; Midha and Palvia, 2012; Singh et al., 2011). CVS, a source code management tool, keeps tracks of different versions of the software. A CVS commit occurs when a contributor uploads some new or modified software code to a project (Howison and Crowston, 2014). Because they resemble completed modification requests (MRs) in commercial development environments CVS commits are frequently used to represent OSS project technical success (Giuri et al., 2010; Grewal et al., 2006; Midha and Palvia, 2012; Singh et al., 2011; Yang et al., 2013). We use the total number of CVS commits made on each project between January 1, 2003 and December 31, 2003 (at the time of data collection, CVS was the only code management system provided on SourceForge, allowing us to capture comparable mea sures across projects).

## Ease of knowledge integration

Software coupling was measured using source code of the most recent release of the application before the end of 2002. Coupling was measured using a metric from the software engineering literature, CBO (Coupling Between Objects) (Chidamber and Kemerer, 1994). CBO captures the number of other classes coupled to a focal class. An instance of coupling occurs when there is evidence of a method of one obiect using methods or instance variables of another obiect (Chidamber and Kemerer 1994). A coupling is also introduced when an object of another class is passed into or out of a method invocation. Class A is coupled to class B if class A uses a type, data, or member from class B. One major source of coupling is that between a superclass and a subclass. Coupling Between Objects is a measure of the non-inheritance coupling between two objects. Any number of couplings to a given class counts as 1 toward the metric total. Coupling was assessed for each class in the focal release of the project. To calculate a release level coupling measure, the class level coupling measures were averaged across all classes for the given release of the project. The higher the value of this term, the higher is the coupling of the software

To be comprehensive, the level of interactive discussion was measured using all public forum activity associated with each project during 2002. One or more threads make up each project forum. A thread contains at least one post, and may also contain response posts from the original poster or a new person. A post is a message written by a project participant that anyone can view. Forum posts include discussions of software problems, potential solutions, updates to the project, organizational issues, responsibilities and division of labor, and other communications. We capture the extent to which communication is interactive, which is key to integrating knowledge from different sources. To indicate the level of interactivity we calculate the percentage of threads that include replies (i.e., the number of threads with replies divided by the total number of threads). Threads often take on a form of question and answer where one poster starts the thread with a question and another person answers the question, in the same thread, with an additional post. If threads have only one post, it indicates a

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

Table 1  
Constructs, variables, and measures.

<table><tr><td>Construct</td><td>Variable</td><td>Measurement</td></tr><tr><td>Technical success</td><td>Completed code modifications</td><td>CVS commits in 2003</td></tr><tr><td>Potential resource flow (knowledge and developer external attention)</td><td>Network degree centrality</td><td># of connected projects through shared developers in 2002</td></tr><tr><td>Ease of knowledge integration</td><td> $Software\ coupling^a$ </td><td>Average Coupling Between Objects in 2002</td></tr><tr><td>Ease of knowledge integration</td><td>Interactive discussion</td><td># of 2002 threads with replies divided by the total number of threads</td></tr><tr><td>Attention</td><td>Developer external  $attention^a$ </td><td># of 2002 posts by focal project developers outside the focal project divided by the total number of posts (on and off the focal project)</td></tr><tr><td rowspan="11">Control variables</td><td>Lines of code</td><td># of lines of code in last release in 2002</td></tr><tr><td>C</td><td>Binary variable indicating whether application is developed using C++ or Java</td></tr><tr><td>Internet</td><td>Binary variable indicating whether the application is for the internet or networking</td></tr><tr><td>Number of operating systems</td><td># of operating systems the application can be used on</td></tr><tr><td>Number of audiences</td><td># of intended audiences that can use the application</td></tr><tr><td>GPL license</td><td>Binary variable indicating whether the application uses the GPL license</td></tr><tr><td>Intended audience</td><td>Binary variable indicating whether the application is intended to be used by software developers</td></tr><tr><td>Number of releases</td><td># of releases in 2002</td></tr><tr><td>Number of CVS</td><td># of CVS commits in 2002</td></tr><tr><td>Number of developers</td><td># of developers listed in January 2003</td></tr><tr><td>Stage</td><td>Binary variable indicating whether the application had reached the beta stage of development</td></tr></table>

<sup>a</sup> This variable is inversely related to the construct.

lack of interactivity. Questions asked that do not receive answers may not be useful for integrating new knowledge into the project.

## Attention

The external developer attention was also measured using all public forum activity during 2002. We captured the overall quantity of discourse by the developers on the focal project across all projects in which they posted any message. We counted the posts that the developers made on the focal project and the posts the developers made on other projects on SourceForge. We then divided the number of posts made outside the focal project by the total number of posts the developers made (both on and off the focal project). As an example, assume the focal project has 2 developers. Developer A makes 4 posts on the focal project and 0 posts on other projects. Developer B makes 1 post on the focal project and 10 posts on other projects. In this case the proportion of participation outside the focal project would be 10/15, indicating 67% of their communication was on outside projects.

## Potential resource flow (knowledge and developer external attention): network degree centrality

Developers who engage in multiple proiects create network connections between OSS projects (Grewal et al 2006: Méndez-Durón and García, 2009; Peng and Dey, 2013; Peng et al., 2013a; Singh and Phelps, 2013; Singh et al., 2011). To measure network degree centrality we first identified the listed developers on SourceForge for each project as of January 2003 We selected January 2003 to allow projects sufficient time to attract participants and to capture all participants associated with the project by the end of 2002.<sup>2</sup> We then identified the other projects that those developers interacted with during 2002. A developer was associated with another SourceForge project if he was listed as a developer or administrator in January 2003. If two developers on one focal project are connected to the same alter project we count that alter project once. Conceptually, network degree centrality is influenced by the number of other projects that may be accessed through a focal projects’ connections. A summary of the constructs, variables and measurement can be found in Table 1.

## Control variables

Given our focus on knowledge access and integration, we sought to control for indicators of the amount of knowledge available internally in the project (i.e. vs. knowledge available through network connections). Four variables were measured as indicators of a project’s internal knowledge stores: size of the last release in 2002 (in lines of code, LOC) is an indicator of the amount of source code, which represents the base of pre-existing knowledge as explained above; the number of operating systems for which the software is developed (Sen et al., 2012) and the number of audiences for whom it is intended taps the breadth of technical knowledge that has gone into development of the software; the number of developers (based on who is listed as a developer in January 2003 (Chengalur-Smith et al., 2010)) captures the amount of knowledge available among core project participants.

```txt
Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006
```

We also measured seven other variables that have been shown to influence OSS project outcomes. These include several characteristics of the application: whether the application is developed using C++ or Java (Subramaniam et al., 2009), whether it is for the internet or networking, a dummy variable indicating whether the project used the GPL license (Stewart et al., 2006a) and whether the application is intended for use by software developers (Sen et al., 2012). Further, we control for the overall amount of activity associated with the project. We control for number of releases in 2002, the number of CVS commits in 2002 and the stage of development the application is in (Subramaniam et al., 2009), as projects that are more active and advanced in period one may be expected to have more activity in period two for reasons outside the boundaries of this research.

## Analyses and results

Analyses were conducted using SPSS version 19. Several skewed variables were log transformed prior to analysis: network degree centrality, interactive discussion, developer external attention, the number of listed developers, CVS commits in 2002, and releases in 2002 were all transformed.

Descriptive statistics of untransformed variables and correlations of the transformed variables used in hypothesis testing are in Table 2. The dependent variable, number of CVS commits (completed code modifications), is a non-negative, skewed count variable; therefore we used negative binomial moderated regression analysis (Allison, 1999). We took several steps to ensure that the data satisfy the underlying assumptions of the statistical technique. Variables were transformed to reduce skewness as noted above. We centered all variables to reduce the possibility of multicollinearity resulting from the inclusion of interaction terms for testing the moderation hypotheses (Edwards and Harrison, 1993). The model variance inflation factors were less than 3, suggesting that multicollinearity is unlikely to be a significant concern in model estimation. Observation of the residuals and Cook and White’s test suggest that the errors are normally distributed. Table 3 displays results of the main analyses.

Model 1 includes control variables only and is significant (p < .01). Model 2 includes control variables and main effects and is also significant (p < .01). The Bayesian Information Criterion for Model 2, 1601.14, is lower than the Bayesian Information Criterion for Model 1, 1757.87, suggesting that Model 2 is the superior model (Ramsey and Schafer, 2002). The coefficient for software coupling is negative and significant, indicating that higher levels of software coupling at the end of 2002 are associated with lower levels of completed code modifications (CVS commits) in 2003. This provides support for H $( b = - . 3 3 , p < . 0 1 )$ . The coefficient for interactive discussion is positive and significant, supporting H2 $( b = 1 . 9 9 , p < . 0 5 )$ The coefficient for proportion of developer external attention is negative and significant, providing support for H3 $( b = - . 4 7 , p < . 0 1 )$ . Finally, the coefficient for network degree centrality is positive and significant, providing support for H4 $( b = . 3 9 , p < . 0 1 )$ .

When the hypothesized interactions are added, Model 3 is significant $\left( p < . 0 1 \right)$ , and the Bayesian Information Criterion for Model 3 (BIC = 1572.09) is lower than the Bayesian Information Criterion for Model 2 (BIC = 1601.14), suggesting that Model 3 is the better model. Results in Model 3 support the hypothesized interactive discussion interaction with the network degree centrality, H6 (b = .82, p < .01), suggesting that high interactive discussion amplifies the benefits OSS projects receive from high network degree centrality. This interaction is shown in Fig. 2. The dotted line in the figure shows that when interactive discussion is low, network degree centrality has almost no positive impact on completed code modifications (CVS commits). The line represented by the long dashes indicates that for projects that have the most interactive discussion, network degree centrality has the most positive effect on completed code modifications (CVS commits).

The interaction between proportion of developer external attention and network degree centrality, H7 (b = .08, p < .01), is also supported. The negative coefficient indicates that the positive impact of network degree centrality on completed code modifications (CVS commits) is strongest when there is lower developer external attention on other projects. Fig. 3 shows this interaction, indicating that the positive impact of network degree centrality is most positive for those projects that have low developer attention outside the project (dotted line). The line (long dashes) reflecting projects with high developer attention focused outside the project shows no positive impact for network degree centrality. The interaction between network degree centrality and software coupling was not significant, thus H5 was not supported.

## Robustness

To assess the robustness of the results, we explored several alternate measures and models. First, we ran the analysis using an alternate measure for interactive discussion: the total number of reply posts in 2002. In some cases, the initial thread post requires multiple responses to arrive at an answer, thus more reply posts may indicate greater efforts toward knowledge integration. The results are consistent with what is reported above. We ran a second robustness test using the average number of posters per thread to capture the number of different people participating as an alternate measure of interactive discussion. Results yield a significant main effect but no significant interaction with network degree centrality. Results may be weaker with this measure because more participants may represent not only more interaction, but also a greater number of potentially conflicting viewpoints that could slow progress

Table 2  
Variable descri<sub>p</sub>tive stati stics and correlations

<table><tr><td>Variables</td><td>Mean</td><td>Std. dev.</td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>1. CVS commits</td><td>174.79</td><td>534.51</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Software coupling</td><td>2.81</td><td>1.76</td><td>-.01</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Interactive discussion</td><td>.11</td><td>.25</td><td>.16*</td><td>.02</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Developer external attention</td><td>.29</td><td>.43</td><td>.08</td><td>-.02</td><td>.18*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>5. Network degree centrality</td><td>3.39</td><td>6.63</td><td>.19*</td><td>.03</td><td>.14</td><td>.37**</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>6. Lines of code</td><td>9208.40</td><td>17752.30</td><td>.11</td><td>.22**</td><td>.15*</td><td>.03</td><td>.13</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>7. C</td><td>.49</td><td>.50</td><td>-.02</td><td>.08</td><td>-.11</td><td>-.23**</td><td>-.05</td><td>-.17*</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>8. Internet</td><td>.53</td><td>.50</td><td>.09</td><td>.00</td><td>.10</td><td>.07</td><td>.11</td><td>.09</td><td>-.25**</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>9. Number of operating systems</td><td>1.24</td><td>.90</td><td>.06</td><td>-.02</td><td>.23**</td><td>-.03</td><td>.13</td><td>.01</td><td>.09</td><td>-.06</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>10. Number of audiences</td><td>1.57</td><td>0.81</td><td>.07</td><td>-.09</td><td>.04</td><td>.05</td><td>.06</td><td>.01</td><td>-.07</td><td>.05</td><td>.00</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>11. GPL license</td><td>.57</td><td>.50</td><td>-.09</td><td>.11</td><td>.05</td><td>-.10</td><td>-.06</td><td>.02</td><td>.17*</td><td>-.13</td><td>-.11</td><td>.17*</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>12. Intended audience</td><td>.70</td><td>.46</td><td>.07</td><td>-.08</td><td>.06</td><td>.03</td><td>.07</td><td>.02</td><td>-.25**</td><td>.08</td><td>.05</td><td>.33**</td><td>-.28**</td><td></td><td></td><td></td><td></td></tr><tr><td>13. Number of releases</td><td>2.90</td><td>3.52</td><td>.25**</td><td>.00</td><td>.24**</td><td>.11</td><td>-.05</td><td>.10</td><td>.00</td><td>-.01</td><td>.14</td><td>.02</td><td>-.01</td><td>-.01</td><td></td><td></td><td></td></tr><tr><td>14. Number of CVS</td><td>284.50</td><td>626.93</td><td>.28**</td><td>.01</td><td>.20**</td><td>.08</td><td>-.01</td><td>.08</td><td>.01</td><td>-.15</td><td>.08</td><td>-.16*</td><td>-.16*</td><td>-.05</td><td>.55**</td><td></td><td></td></tr><tr><td>15. Number of developers</td><td>2.80</td><td>4.39</td><td>.18*</td><td>.08</td><td>.19*</td><td>.35**</td><td>.38**</td><td>.31**</td><td>-.24**</td><td>.16*</td><td>.14</td><td>.09</td><td>-.14</td><td>.02</td><td>.06</td><td>.12</td><td></td></tr><tr><td>16. Stage</td><td>.62</td><td>.49</td><td>-.03</td><td>-.01</td><td>.06</td><td>-.04</td><td>.19*</td><td>.19*</td><td>.05</td><td>.01</td><td>.05</td><td>.03</td><td>.07</td><td>-.01</td><td>.04</td><td>.01</td><td>.01</td></tr></table>

N = 1 7 5 .

Correlation is significant at the .05 level ( 2 tailed )

Co rrel ati o n i s s igni fi cant at the . 0 1 l eve l ( 2 tai l ed )

Table 3  
Regression results (2003 completed code modifications – CVS commits).

<table><tr><td>Independent variables</td><td>Model 1</td><td>Model 2</td><td>Model 3</td></tr><tr><td>Lines of code</td><td>0.00</td><td>0.00*</td><td>0.00**</td></tr><tr><td>C</td><td>0.51</td><td>0.20</td><td>0.31</td></tr><tr><td>Internet</td><td>-0.35</td><td>0.33</td><td>0.39</td></tr><tr><td>Number of operating systems</td><td>0.66*</td><td>0.44</td><td>0.45</td></tr><tr><td>Number of audiences</td><td>1.16**</td><td>1.21**</td><td>1.20**</td></tr><tr><td>GPL license</td><td>-0.23</td><td>-0.51</td><td>-0.38</td></tr><tr><td>Intended audience</td><td>0.74</td><td>-0.11</td><td>-0.02</td></tr><tr><td>Number of releases</td><td>0.37**</td><td>0.40**</td><td>0.41**</td></tr><tr><td>Number of CVS</td><td>0.24**</td><td>0.33**</td><td>0.31**</td></tr><tr><td>Number of developers</td><td>1.23**</td><td>0.85*</td><td>1.16**</td></tr><tr><td>Stage</td><td>-2.45**</td><td>-2.91**</td><td>-3.04**</td></tr><tr><td>Software coupling</td><td></td><td>-0.33**</td><td>0.34</td></tr><tr><td>Interactive discussion</td><td></td><td>1.99*</td><td>1.27</td></tr><tr><td>Developer external attention</td><td></td><td>-0.47**</td><td>-0.53**</td></tr><tr><td>Network degree centrality</td><td></td><td>0.39**</td><td>0.26*</td></tr><tr><td>Interactive discussion * network degree centrality</td><td></td><td></td><td>.82**</td></tr><tr><td>Software coupling * network degree centrality</td><td></td><td></td><td>-.05</td></tr><tr><td>Developer external attention * network degree centrality</td><td></td><td></td><td>-.08*</td></tr><tr><td>Likelihood ratio chi squared</td><td>50.76</td><td>103.92</td><td>140.66</td></tr></table>

a. Listwise N = 175.  
The bold values are significant and related to the hypotheses.  
<sup>\*</sup> Significant at the 0.05 level (2-tailed).  
<sup>\*\*</sup> Significant at the 0.01 level (2-tailed).

![](/api/attachments/V6EXWZD7/fulltext/images/7ce0837a29c5dcbceddab770b4cc3c3128822b3bc92eda137ebbc40a8903f134.jpg)  
Fig. 2. Interactive discussion and network degree centrality.

![](/api/attachments/V6EXWZD7/fulltext/images/ae678e012455653c9957ac6a8d22487ed5ac8aabce20c01ae1b34df3ed63bc07.jpg)  
Fig. 3. Developer external attention and network degree centrality.

<table><tr><td>Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006</td></tr></table>

Because there are many types of software structural complexity, we performed a robustness test including a different dimension of structural complexity, cohesion. Cohesion is the ‘togetherness’ of individual elements within an application (Bieman and Ott, 1994), and lower complexity is indicated by higher cohesion. Prior work suggests that developers make tradeoffs between coupling and cohesion, and that a combined measure is therefore a more holistic way to capture structural complexity (Darcy et al., 2005). We measured cohesion using the metric from the Chidamber and Kemerer suite (Chidamber and Kemerer, 1994): LCOM (Lack of Cohesion Metric). LCOM is calculated as the percentage of class methods that use a given class instance variable. Average percentages for all of a classes instance variables is calculated and subtracted from 100%. We re-ran our analyses substituting Darcy et al.’s (2005) combined measure of coupling (CBO) multiplied by cohesion (LCOM) Results were consistent with the main analysis.

The highest correlation among the independent variables of interest was .37, between degree centrality and external attention. Though the variance inflation factors indicated no problem with multicollinearty, we also re-ran Model 2 twice, once omitting each of these variables. In each case, results for the retained variable were consistent with the full model. Finally, to more thoroughly explore the potential impacts of our independent variables, we considered the possibility that developer external attention could interact with software coupling or interactive discussion, however these interaction terms were not statistically significant when added to the model.

## Discussion

This study investigated two important strategic resources for OSS projects, knowledge and developer attention. Results of the analyses generally supported the hypotheses (see Table 4). Source code coupling and interactive discussion were argued to ease knowledge integration and results showed they positively influence completed code modifications. Developers external attention indicated by forum participation on other projects negatively impacts completed code modifications. Consistent with prior research, we argued that network degree centrality increases access to knowledge and attention resources and showed it positively impacts completed code modifications. We extended prior work on network effects in OSS by demonstrating that projects benefit more from network degree centrality (knowledge access) when they have higher levels of interactive discussion, and less when developer attention is focused more outside the focal project

We found a direct effect of software coupling on completed code modifications, but no interaction between software coupling and network degree centrality. Our hypothesis (H5) suggested that the positive impact of diverse knowledge coming through network degree centrality would be more positive when software coupling was low compared to when it was higher. However, this effect may be counteracted in our study. If the focal project has lower software coupling than the connected projects, it may be easier to port code from the focal project to the other connected projects than vice versa. So while low software coupling may make it easier to incorporate network knowledge into the focal project application (the interaction we argued), low software coupling could also result in shifting the balance of knowledge flow away from the focal project toward alters, counteracting the hypothesized benefit. Future research is necessary to unravel these relationships.

## Contributions to research and practice

Prior work in the OSS setting has mainly focused on the positive effects of network connections (Singh et al., 2011). A significant contribution of this research is in demonstrating that the network may also facilitate important resources, i.e. developer attention, flowing away from focal projects. When projects were highly connected, increasing the proportion of developer attention focused outside the project was more damaging than when a project had fewer connections. To the degree that OSS leaders can influence developers’ focus and participation in other projects, our research may be used as an input to their strategic decision-making. For instance, if a developer leads a project that is well connected, it may be especially beneficial to try to keep participants’ attention focused on his project and discourage high levels of participation in outside projects.

This study implies that future work should take a more nuanced view of how increasing the number of developers on a project may (or may not) enhance its success. Research has predicted that the amount of developer effort drives CVS

## Table 4

Summary of hypotheses.

<table><tr><td></td><td>Hypothesis</td><td>Supported?</td></tr><tr><td>H1</td><td>OSS project software coupling will be negatively associated with OSS project completed code modifications</td><td>Yes</td></tr><tr><td>H2</td><td>Interactive discussion among OSS project participants will be positively associated with completed code modifications</td><td>Yes</td></tr><tr><td>H3</td><td>As the developer external attention increases completed code modifications in the focal project will decrease</td><td>Yes</td></tr><tr><td>H4</td><td>OSS project network degree centrality will be positively associated with completed code modifications</td><td>Yes</td></tr><tr><td>H5</td><td>The positive impact of network degree centrality on completed code modifications is stronger when software coupling is low</td><td>No</td></tr><tr><td>H6</td><td>The positive impact of network degree centrality on completed code modifications is increased in the presence of high levels of interactive discussion</td><td>Yes</td></tr><tr><td>H7</td><td>The developer external attention dampens the positive impact of network degree centrality on completed code modifications</td><td>Yes</td></tr></table>

<table><tr><td>Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006</td></tr></table>

commits or other success outcomes (Stewart and Gosain, 2006). Some hypothesize the relationship between the ability to attract developers and code generation directly (Crowston and Scozzi, 2002; Stewart and Gosain, 2006), while others acknowledge the importance of human capital by using the number of developers as a control (Singh et al., 2011). Previous studies count the number of listed developers on the project as a way to approximate developer effort on the project (Crowston and Scozzi, 2002; Stewart and Gosain, 2006). However, this study highlights the fact that developers associated with a project may vary in the amount of attention they devote to the project. Developers may easily quit contributing to a focal project and focus their attention on other projects while remaining listed as a developer on the focal project. This can mislead potential application adopters and researchers alike. The findings in this study reinforce the importance of attention as a strategic resource for organizations and groups (e.g. OSS projects) that operate in information rich contexts (Gosain, 2007).

By observing forum posting behavior on both the focal project and on other projects our analysis allows a more finegrained assessment of the extent to which developers make trade-offs among multiple projects. Results show that including indicators of forum participation on multiple projects explains more variance in completed code modifications than does including the number of developers alone. As for-profit organizations and users seek to adopt and interact with OSS projects they often want to predict whether the OSS project will be successful (Santos et al., 2013). Adopting an OSS project that developers abandon wastes the organization’s resources. Forum activity that signals developer attention to projects is easily observed and may help practitioners and researchers obtain a better understanding of developers’ commitment to a project. Organizations considering the strategic role of adopting OSS in their software portfolio (Marsan et al., 2012) may find it helpful to assess the amount of attention that developers devote to the project.

Fig. 3 suggests that projects that perform best in terms of completed code modifications hold central network positions, but their developers participate relatively little in the forums of other projects. Our data does not tell us why these developers are listed as developers on multiple projects but mainly post to the forums on the focal one. One explanation may be that the developers were active on the alter projects, but have completed the contribution they planned to make to the alter project. So, they may carry wisdom gained from participation on those projects, yet no longer contribute to them. The results presented here suggest that future research might fruitfully investigate the movement of developers from one project to another and what it means to be a developer listed on two projects.

A second contribution of the study is presenting a more nuanced consideration of the conditions under which a project may benefit from the knowledge in its network: benefits are greater when participants in the project engage in more interactive discussions. We argue that this effect emerges because interactive discussion influences a project’s knowledge integration ability, and the need for knowledge integration is greater for more connected projects. Our work adds to this line of research by showing how encouraging interactive discussion on a focal project’s forums can enhance the benefits of connections to other projects (see Fig. 2).

More broadly, this study brings another perspective to the OSS literature by considering how internal characteristics of projects interact with environmental characteristics. Several studies examine how an OSS project’s internal characteristics, such as ideology adoption (Stewart and Gosain, 2006), license choice (Colazo and Fang, 2009; Stewart et al., 2006a), and governance practices (Midha and Bhattacherjee, 2012) impact its success. Other research explores impacts of a project’s environment on its success (Chengalur-Smith et al., 2010; Grewal et al., 2006; Singh et al., 2011; Wen et al., 2013). This study unites both perspectives to demonstrate the benefits of synergy between internal characteristics (interactive discussion) and external environment (network degree centrality).

Because of the practical and strategic implications of the findings, the results presented here should interest managers of OSS projects. OSS participants can proactively change software coupling (structural complexity) and the level of interactive discussion. Therefore, OSS participants may find results useful for deciding how to direct their limited resources, which is a key strategic decision. Results reinforce the importance of facilitating interactive dialog within the project. Results (i.e. Fig. 3) also suggest that managers should consider potential downsides of developer engagement in other projects. Managers may want to work hard to engage externally connected developers in the focal project and ensure that those developers’ tacit knowledge about the focal project is made explicit or otherwise transferred to other participants. This transfer of knowledg will help the focal project continue if those developers’ attention shifts away to other projects in the network.

## Implications for future research outside the OSS setting

While the hypotheses and empirical study focus on OSS projects, we believe results suggest implications for studies of other kinds of open projects. Many kinds of projects develop open products, leveraging contributions from participants working in geographically and organizationally distributed locations (Benkler and Nissenbaum, 2006). These kinds of projects thrive when contributors can make contributions in small increments of time (Benkler, 2002). Our study highlights pro duct complexity as a factor relevant to minimizing the time needed for individuals to integrate new contributions. In essence our findings support Benkler's point that a fundamental limitation of a project rests in its ability to integrate knowledge (Benkler, 2002), and demonstrates some factors that are important to knowledge integration. Based on our findings we may expect similar effects within Wikipedia. For instance, a Wiki article that is well structured (akin to low coupling (structural complexity) in the software development setting) and has active talk pages (i.e. interactive discussion) may make it easier for contributors to integrate ideas into the article. Our model offers guidance for leadership in open organizations to operate strategically in the way work is organized so as to facilitate collaboration.

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

## Limitations

Important limitations in the study also present opportunities for further research. The archival nature of the study limited our ability to observe the proposed underlying theoretical mechanisms. For example, the actual difficulty or ease with which developers integrate knowledge remains unobserved, nor do we observe the extent to which knowledge integration occurs in the interactive discussion threads. While past work (Barcellini et al., 2008; Scacchi, 2002) and our reading of several threads indicates discussion forums are used for knowledge integration, there may be many threads in the forums that do not focus on knowledge integration and including them adds noise to the model. Similarly, while we observe a major form of OSS developer communication (online forums), developers could communicate in a variety of other ways that could not be observed in our archival data: e.g. telephone communication, text and instant messaging. To confirm the implications of the study requires further research. For example, qualitative analysis of discussion forums and survey studies to assess how developers divide their attention across projects would complement the current study.

A second limitation stems from the extent to which we controlled for other potentially important network characteristics, such as connections to for-profit companies or foundations (Dahlander and Wallin, 2006; Daniel et al., 2011; Henkel, 2008; Niederman et al., 2006; O’Mahony, 2005; Scacchi, 2010). These connections could bring unique resources requiring different types of knowledge integration. For example, a connection to a for-profit organization might bring financial resources or paid labor (Henkel, 2008) requiring knowledge integration in the form of greater business savvy. At the same time, such connections may result in deleterious effects. A connection to a for-profit could signal a threat to the ‘‘openness” of the product (Stewart et al., 2006a); this implies that increasing knowledge access in this way may not uniformly yield positive results.

A third potential limitation of the study relates to the fact that the organizational context of OSS has changed over the last 15 years, with a variety of new players entering the domain (Fitzgerald, 2006). Nonetheless the relatively small, volunteerdriven projects that are represented in our sample remain a prevalent organizational form of OSS development as may be observed on platforms such as SourceForge, and it is these kinds of projects that may be informed by the results of the study.

Fourth, just as other OSS projects indicate only one set of possible alters, technical success represents only one outcome of interest, which may not be equally important to all OSS projects. Market success is another outcome of concern, indicating the degree to which users value the application (Fershtman and Gandal, 2011; Setia et al., 2012; Subramaniam et al., 2009; Wu et al., 2007). While technical success influences market success (Stewart et al., 2006a), the factors associated with knowledge integration capabilities could also directly impact market success, e.g. because interactive discussion acts as a signal of project viability to potential adopters.

## Conclusion

This paper develops arguments that go beyond the well-established hypothesis that an OSS project’s access to knowledge and developer attention via network degree centrality yields performance (Mallapragada et al., 2012). We consider the degree to which that knowledge is easily integrated (e.g. software coupling and interactive discussion). Further we examine indicators of how developer attention moves through the network. Results highlight the importance of developer participation in forums both on the focal project and on alter projects. We hope the findings serve as a basis for further work that explores the nuances of network constructs and their effects in OSS settings.

## References

Alavi, M., Tiwana, A., 2002. Knowledge integration in virtual teams: the potential role of KMS. Journal of the American Society for Information Science and Technology 53 (12), 1029–1037.

Allison, P., 1999. Logistic Regression Using the Sas System: Theory and Application. Sas. SAS Institute and Wiley, Cary, NC.

Amrit, C., Hillegersberg, J.v. (Eds.), 2010. Coordination Implications of Software Coupling in Open Source Projects. Springer, Berlin, Heidelberg.

Baldwin, C., Clark, K., 2006. The architecture of participation: does code architecture mitigate free riding in the open source development model. Management Science 52 (7). 1116–1127.

Barbagallo, D., Francalenei, C., Merlo, F., 2008. The impact of social netowrking on software design quality and development effort in open source projects. In: International Conference on Information systems, Paris, France.

Barcellini, F., Détienne, F., Burkhardt, J.-M., Sack, W., 2008. A socio-cognitive analysis of online design discussions in an open source software community. Interacting with Computers 20 (1). 141–165.

Barnett, M.L., 2008. An attention-based view of real options reasoning. Academy of Management Review 33 (3), 606–628.

Benkler, Y., 2002. Coase’s Penguin, or, Linux and ‘‘the nature of the firm”. The Yale Law Journal 112 (3), 369–446

Benkler, Y., Nissenbaum, H., 2006. Commons-based peer production and virtue. Journal of Political Philosophy 14 (4), 394–419.

Bieman, J.M., Ott, L.M., 1994. Measuring functional cohesion. IEEE Transactions in Software Engineering 20 (8), 644–657.

Bolici. F.. Howison, I.. Crowston, K., 2009, Coordination without discussion? Socio-technical congruence and Stigmergy in free and open source software projects. In: Socio-Technical Congruence Workshop in Conj Intl Conf on Software Engineering, Vancouver, Canada.

Bouquet, C., Birkinshaw, J., 2008. Weight versus voice: how foreign subsidiaries gain attention from corporate headquarters. Academy of Management Journal 51 (3), 577–601.

Burke, M., Kraut, R., Joyce, E., 2010. Membership claims and requests: conversation-level newcomer socialization strategies in online groups. Small Group Research 41 (1), 4–40.

Casadesus-Masanell. R., Ghemawat. Pankai, 2006, Dynamic mixed duopoly: a model motivated by Linux ys. Windows. Management Science 52 (7), 1072– 1084.

Chan I. Husted, K. 2010 Dual allegiance and knowledge sharing in open source software firms, Creativity & Innovation Management 19 (3). 314–326

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006

Chengalur-Smith, I., Sidorova, A., Daniel, S., 2010. Sustainability of free/libre open source projects: a longitudinal study. Journal of the Association fo Information Systems 11 (11), 657–683.

Chidamber, S.R., Kemerer, C.F., 1994. A metrics suite for object oriented design. IEEE Transactions on Software Engineering 20 (6), 476–493.

Chua, C.E.H., Yeow, A.Y.K., 2010. Artifacts, actors, and interactions in the cross-project coordination practices of open-source communities. Journal of the Association for Information Systems 11, 838–867.

Colazo, J., Fang, Y., 2009. Impact of license choice on open source software development activity. Journal of the American Society for Information Science and Technology 60 (5), 997–1011.

Crowston, K., Howison, J., 2006. Assessing the health of open source communities. Computer 39 (5), 89–91.

Crowston, K., Li, Q., Wei, K., Eseryel, U.Y., Howison, J., 2007. Self-organization of teams for free/libre open source software development. Information and Software Technology 49 (6), 564–575.

Crowston, K., Scozzi, B., 2002. Open source software projects as virtual organizations: competency rallying for software development. IEE Proceedings Software 149 (1), 3–17.

Dahlander, L., Magnusson, M., 2005. Relationships between open source software companies and communities: observations from Nordic firms. Research Policy 34 (4), 481–493.

Dahlander, L., O’Mahony, S., 2011. Progressing to the center: coordinating project work. Organization Science 22 (4), 961–979.

Dahlander, L., Wallin, M., 2006. A man on the inside: unlocking communities as complementary assets. Research Policy 35 (8), 1243–1259

Daniel, S., Agarwal, R., Stewart, K.J., 2013. The effects of diversity in global, distributed collectives: a study of open source project success. Information Systems Research 24 (2), 312–333.

Daniel, S., Maruping, L., Cataldo, M., Herbsleb, J., 2011. When cultures clash: participation in open source communities and its implications for organizational commitment. In: International Conference on Information Systems, Shanghai.

Darcy, D.P., Kemerer, C., Slaughter, S., Tomayko, J., 2005. The structural complexity of software: an experimental test. IEEE Transactions on Software Engineering 31 (11), 982–995.

Davenport, T.H., Beck, J.C., 2000. Getting attention. Harvard Business Review 119, 118–126.

Derber, C., 2000. The Pursuit of Attention: Power and Ego in Everyday Life. Oxford University Press, New York, NY.

Ducheneaut, N., 2005. Socialization in an open source software community: a socio-technical analysis. Computer Supported Cooperative Work 14 (4), 323– 368.

Edwards, J.R., Harrison, R.V., 1993. Job demands and worker health: three-dimensional reexamination of the relationship between person environment fit and strain. Journal of Applied Psychology 78 (4), 628.

English, R., Schweik, C., 2007. Identifying success and tragedy of floss commons: a preliminary classification of Sourceforge.Net projects. In: First International Workshop on FLOSS: Emerging Trends in FLOSS Research and Development, Minneapolis, MN.

Fang. Y, Neufeld, D., 2009, Understanding sustained participation in open source software proiects, Journal of Management Information Systems 25 (4), 9- 50.

Fershtman, C., Gandal, N., 2011. Direct and indirect knowledge spillovers: the ‘‘social network” of open source projects. The RAND Journal of Economics 42 (1), 70–91.

Fielding, R., 1999. Shared leadership in the apache project. Communications of the ACM 42 (4), 2.

Fitzgerald, B., 2006. The transformation of open source software. Management Information Systems Quarterly 30 (3), 587–598

Flanagan, T., Eckert, C., Clarkson, P.J., 2007. Externalizing tacit overview knowledge: a model-based approach to supporting design teams. Artificial Intelligence for Engineering Design, Analysis and Manufacturing 21 (3), 227–242.

Gallivan, M.J., 2001. Striking a balance between trust and control in a virtual organization: a content analysis of open source software case studies. Information Systems Journal 11 (4), 277–304.

Gendreau, O., Robillard, P.N., 2009. Exploring knowledge flow in software project development. In: International Conference on Information, Process, and Knowledge Management, Montreal.

Giuri, P., Ploner, M., Rullani, F., Torrisi, S., 2010. Skills, division of labor and performance in collective inventions: evidence from open source software. International Journal of Industrial Organization 28 (1), 54–68.

Goldhaber, M.H., 1997. The attention economy and the net. First Monday 2 (4).

Gosain, S., 2007. Mobilizing software expertise in personal knowledge exchanges. The Journal of Strategic Information Systems 16 (3), 254–277.

Grant, R.M. 1996, Toward a knowledge-based theory of the firm, Strategic Management Journal 17 (2). 109–122

Grewal, R., Lilien, G.L., Mallapragada, G., 2006. Location, location, location: how network embeddedness affects project success in open source systems. Management Science 52 (7), 1043–1056.

Griffith, T.L., Sawyer, J.E., 2010. Multilevel knowledge and team performance. Journal of Organizational Behavior 31 (7), 1003–1031.

Gulati, R., Lavie, D., Madhavan, R.R., 2011. How do networks matter? The performance effects of interorganizational networks. Research in Organizationa Behavior 31 207-224

Gulati, R., Puranam, P., Tushman, M., 2012. Meta-organization design: rethinking design in interorganizational and community contexts. Strategic Management Journal 33 (6), 571–586.

Haefliger, S., Krogh, G.v., Spaeth, S., 2008. Code reuse in open source software. Management Science 54 (1), 180–193.

Hahn, J., Moon, J.Y., Zhang, C., 2008. Emergence of new project teams from open source software developer networks: impact of prior collaboration ties. Information Systems Research 19 (3), 369–391.

Hann, I.-H., Roberts, J.A., Slaughter, S.A., 2013. All are not equal: an examination of the economic returns to different forms of participation in open source software communities. Information Systems Research 24 (3), 520–538.

Hansen, M.T., Haas, M.R., 2001. Competing for attention in knowledge markets: electronic document dissemination in a management consulting company. Administrative Science Ouarterly 46 (1). 1–28.

Henkel, J., 2008. Champions of revealing—the role of open source developers in commercial firms. Industrial and Corporate Change 18 (3), 435–471.

Hoffman, A.J., Ocasio, W., 2001. Not all events are attended equally: toward a middle-range theory of industry attention to external events. Organization Science 12 (4), 414–434.

Howison, J., Crowston, K., 2014. Collaboration through open superposition. Management Information Systems Quarterly 38 (1), 29–50.

Howison, J., Inoue, K., Crowston, K., 2006. Social dynamics of free and open source team communications. Open Source Systems IFIP International Federation for Information Processing, 319–330.

Hu. D., Zhao. I.L., Cheng, I., 2012. Reputation management in an open source developer social network: an empirical study on determinants of positive evaluations. Decision Support Systems 53 (3), 526–533.

Hutchens. D.H., Basili, V.R., 1985, System structure analysis: clustering with data bindings, IEEE Transactions in Software Engineering 11 (8). 749–757.

Ke, W., Zhang, P., 2009. Motivations in open source software communities: the mediating role of effort intensity and goal commitment. International Journal of Electronic Commerce 13 (4).39–66

Klamer, A., Dalen, H.P.V., 2002. Attention and the art of scientific publishing. Journal of Economic Methodology 9 (3), 289–315.

Kogut, B., Metiu, A., 2001. Open source software development and distributed innovation. Oxford Review of Economic Policy 17 (2), 248–264.

Kuk, G., 2006. Strategic interaction and knowledge sharing in the KDE developer mailing list. Management Science 52 (7), 1031–1042.

Lee, C., Lee, K., Pennings, J.M., 2001. Internal capabilities, external networks, and performance: a study on technology-based ventures. Strategic Management Journal 22 (6–7), 615–640.

Lerner, J., Tirole, J., 2005. The scope of open source licensing. Journal of Law, Economics, and Organization 21 (1), 20–56.

Liu, X., Iyer, B., 2007. Design architecture, developer networks and performance of open source software projects. In: International Conference on Information Systems, Montreal.

MacCormack, A., Rusnak, J., Baldwin, C.Y., 2006. Exploring the structure of complex software designs: an empirical study of open source and proprietary code. Management Science 52 (7), 1015–1031.

Mallapragada, G., Grewal, R., Lilien, G., 2012. User generated open source products: founder’s social capital and time to market. Marketing Science 31 (3), 474–492.

Marsan, J., Paré, G., Beaudry, A., 2012. Adoption of open source software in organizations: a socio-cognitive perspective. The Journal of Strategic Information Systems 21 (4), 257–273.

Méndez-Durón, R., García, C.E., 2009. Returns from social capital in open source software networks. Journal of Evolutionary Economics 19 (2), 277–295.

Midha, V., Bhattacherjee, A., 2012. Governance practices and software maintenance: a study of open source projects. Decision Support Systems 54 (1), 23– 32.

Midha, V., Palvia, P., 2012. Factors affecting the success of open source software. The Journal of Systems and Software 85 (4), 895–905

Morgan, L., Finnegan, P., 2014. Beyond free software: an exploration of the business value of strategic open source. The Journal of Strategic Information Systems 23 (3), 226–238.

Morner, M., Krogh, G.v., 2009. A note on knowledge creation in open-source software projects: what can we learn from Luhmann’s theory of social systems? Systemic Practice and Action Research 22 (6), 431–443.

Niederman, F., Davis, A., Greiner, M.E., Wynn, D., York, P.T., 2006. A research agenda for studying open source I: a multi-level framework Communications of the Association for Information Systems 18 (1).

Nonaka, I., 1994. A dynamic theory of organizational knowledge creation. Organization Science 5 (1), 14–37.

Nonaka, I., Toyama, R., 2003. The knowledge-creating theory revisited: knowledge creation as a synthesizing process. Knowledge Management Research & Practice 1 (1), 2–10.

O’Leary, M.B., Mortensen, M., Woolley, A.W., 2011. Multiple team membership: a theoretical model of its effects on productivity and learning for individuals and teams. Academy of Management Review 36 (3), 461–478.

O’Mahony, S. (Ed.), 2005. Non-Profit Foundations and Their Role in Community-firm Software Collaboration. MIT Press, Cambridge, MA.

Ocasio, W., 1997. Towards an attention based view of the firm. Strategic Management Journal 18 (Summer). 187–206

Ocasio. W., 2011. Attention to attention. Organization Science 222 (5). 1286–1296.

Oh, W., Jeon, S., 2007. Membership herding and network stability in the open source community: the Ising perspective. Management Science 53 (7), 1086– 1101.

Okoli, C., Oh, W., 2007. Investigating recognition-based performance in an open content community: a social capital perspective. Information and Management 44 (3), 240–252.

Patnayakuni, R., Rai, A., Tiwana, A., 2007. Systems development process improvement: a knowledge integration perspective. IEEE Transactions on Engineering Management 54 (2), 286–300.

Patnayakuni, R., Ruppel, C.P., Rai, A., 2006. Managing the complementarity of knowledge integration and process formalization for systems development performance. Journal of the Association for Information Systems 7 (8), 545–567.

Peng, G.. Dey, D.. 2013. Research note-a dynamic view of the impact of network structure on technology adoption: the case of OSS development. Information Systems Research 24 (4), 1087–1099.

Peng, G., Mu, J., 2011. Network structures and online technology adoption. IEEE Transactions on Engineering Management 58 (2), 323–333.

Peng, G., Mu, J., Benedetto, C.A.D., 2013a. Learning and open source software license choice. Decision Sciences 44 (4), 619–643.

Peng, G., Wan, Y., Woodlock, P., 2013b. Network ties and the success of open source software development. The Journal of Strategic Information Systems.

Pil, F., Leana, C., 2009. Applying organizational research to public school reform: the effects of teacher human and social capital on student performance Academy of Management Journal 52 (6).1101-1124

Ramsey, F., Schafer, D., 2002. The Statistical Sleuth – A Course in Methods of Data Analysis. Cengage Learning, New York, NY, USA.

Reagans, R., McEvily, W., 2003. Network structure and knowledge transfer: the effects of cohesion and range. Administrative Science Quarterly 48 (2), 240– 267.

Reinholt, M., Pedersen, T., Foss, N.J., 2011. Why a central network position isn’t enough: the role of motivation and ability for knowledge sharing in employee networks. Academy of Management Journal 54 (6), 1277–1297.

Roberts, J.A., Hann, I.-H., Slaughter, S.A., 2006. Understanding the motivations, participation, and performance of open source software developers: a longitudinal study of the apache projects. Management Science 52 (7), 984–1000.

Rogers, E.M., 1995. Diffusion of Innovations. The Free Press, New York.

Sack, W., Détienne, F., Ducheneaut, N., Burkhardt, J.-M., Mahendran, D., Barcellini, F., 2006. A methodological framework for socio-cognitive analyses of collaborative design of open source software. Computer Supported Cooperative Work 15 (2–3), 229–250.

Sandhawalia, B.S., Dalcher, D., 2010. Knowledge flows in software projects: an empirical investigation. Knowledge and Process Management 17 (4), 205– 220.

Santos, C., Kuk, G., Kon, F., Pearson, J., 2013. The attraction of contributors in free and open source software projects. The Journal of Strategic Information Systems 22 (1), 26–45.

Scacchi, W., 2002. Understanding the requirements for developing open source software systems. IEE Proceedings on Software 149 (1), 24–39.

Scacchi, W. (Ed.), 2010. Collaboration Practices and Affordances in Free/Open Source Software Development. Springer, Berlin, Heidelberg.

Seidel, M.-D., Stewart, K.J., 2011. An initial description of the C-form. In: Lounsbury, M. (Ed.), Research in the Sociology of Organizations. Emerald Group Publishing Limited, United Kingdom, pp. 37–72.

Sen, R., Singh, S., Borle, S., 2012. Open source software success: measures and analysis. Decision Support Systems 52, 364–372.

Setia, P.., Rajagopalan, B., Sambamurthy, V., Calantone, R., 2012. How peripheral developers contribute to open-source software development. Information Systems Research 23 (1), 144–163.

Simon, H., 1947. Administrative Behavior: A Study of Decision-Making Processes in Administrative Organizations. Chicago, IL.

Singh, P., Phelps, C., 2013. Networks, social influence, and the choice among competing innovations: insights from open source software licenses. Information Systems Research 24 (3), 539–560.

Singh. P.. Tan. Y., Mookeriee, V., 2011. Network effects: the influence of structural social capital on open source project success, Management Information Systems Quarterly 35 (4), 813–829.

Sojer. M., Henkel. I., 2010. Code reuse in open source software development: quantitative evidence, drivers, and impediments. Journal of the Association for Information Systems 11 (12), 868–901.

Stewart, K., Ammeter, A.P., Maruping, L.M., 2006a. Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Information Systems Research 17 (2), 126–145.

Stewart, K., Darcy, D.P., Daniel, S.L., 2006b. Opportunities and challenges applying functional data analysis to the study of open source software evolution. Stat. Sci. 21 (2), 167–178.

Stewart, K., Gosain, S., 2006. The impact of ideology on effectiveness in open source software development teams. Management Information Systems Quarterly 30 (2), 291–314.

Subramaniam, C., Sen, R., Nelson, M., 2009. Determinants of open source software project success: a longitudinal study. Decision Support Systems 46 (2), 576–585.

Tornatzky, L., Fleischer, M., 1990. The Processes of Technological Innovation. Lexington Books, Lexington.

Trkman, P., Desouza, K.C., 2012. Knowledge risks in organizational networks: an exploratory framework. The Journal of Strategic Information Systems 2 (1), 1–17.

Van Antwerp, M., Madey, G., 2008. Advances in SourceForge research data archive (SRDA). In: Fourth International Conference on Open Source Systems, Milan, Italy.

von Krogh, G., Hippel, E.V., 2003. Special issue on open source software development. Research Policy 32 (7), 1149–1157.

Von Krogh, G., Hippel, E.V., 2006. The promise of research on open source software. Management Science 52 (7), 975–983

Von Krogh, G., Spaeth, S., 2007. The open source software phenomenon: characteristics that promote research. The Journal of Strategic Information Systems 16 (3), 236–253.

von Krogh, G., Spaeth, S., Lakhani, K., 2003. Community, joining, and specialization in open source software innovation: a case study. Research Policy 32 (7), 1217–1241.

Wang, X., Butler, B., Ren, Y.C., 2013. The impact of membership overlap on growth: an ecological competition view of online groups. Organization Science 24 (2), 414–431.

Wen, W., Forman, C., Graham, S.J.H., 2013. The impact of intellectual property rights enforcement on open source software project success. Information Systems Research 24 (4), 1131–1146.

West, J., 2003. How open is open enough? Melding proprietary and open source platform strategies. Research Policy 32 (7), 1259–1285.

Wu, J., Goh, K.-Y., Tang, Q., 2007. Investigating success of open source software projects: a social network perspective. In: International Conference on Information Systems, Montreal.

Yamauchi, Y., Yokozawa, M., Shinohara, T., Ishida, T., 2000. Collaboration with lean media: how open-source software succeeds. In: 2000 ACM Conference on Computer Supported Cooperative Work, Philadelphia, PA, pp. 329–338.

Yang, X., Hu, D., Robert, D.M., 2013. How microblogging networks affect project success of open source software development. In: Hawaii International Conference on System Sciences, Grand Wailea, Maui, Hawaii, pp. 3178–3186.

Ye, Y., Kishida, K., 2003. Toward an understanding of the motivations of open source software developers. In: Twenty-Fifth International Conference on Software Engineering, Portland, Oregon.

Zhang, C., Hahn, J., De, P., 2013. Continued participation in online innovation communities: does community response matter equally for everyone? Information Systems Research 24 (4). 1112-1130.

Zhang, X, Wang, C., 2012, Network positions and contributions to online public goods: the case of Chinese Wikipedia, Journal of Management Information Systems 29 (2), 11–40.

Please cite this article in press as: Daniel, S., Stewart, K. Open source project success: Resource access, flow, and integration. J. Strateg. Inform. Syst. (2016), http://dx.doi.org/10.1016/j.jsis.2016.02.006
