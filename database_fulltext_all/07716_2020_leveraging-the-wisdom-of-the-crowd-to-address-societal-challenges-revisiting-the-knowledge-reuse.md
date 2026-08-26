---
otero_id: 7716
otero_key: "G3PEG9MU"
title: "Leveraging the Wisdom of the Crowd to Address Societal Challenges: Revisiting the Knowledge Reuse for Innovation Process through Analytics"
authors: "Yue Han; Pinar Ozturk; Jeffrey Nickerson"
year: "2020"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00632"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Leveraging the Wisdom of the Crowd to Address Societal Challenges: Revisiting the Knowledge Reuse for Innovation Process through Analytics

Yue Han<sup>1</sup>, Pinar Ozturk<sup>2</sup>, Jeffrey V. Nickerson<sup>3</sup>

<sup>1</sup>Le Moyne College, USA, hany@lemoyne.edu <sup>2</sup>Duquesne University, USA, ozturkp@duq.edu <sup>3</sup>Stevens Institute of Technology, USA, jnickerson@stevens.edu

## Abstract

Societal challenges can be addressed not only by experts but also by crowds. Crowdsourcing provides a way to engage a crowd to contribute to the solutions of some of the biggest challenges of our era: how to cut our carbon footprint, how to address worldwide epidemic of chronic disease, and how to achieve sustainable development. Isolated crowd-based solutions in online communities are not always creative and innovative. Hence, remixing has been developed as a way to enable idea evolution and integration, and to harness reusable innovative solutions. Understanding the generativity of remixing is essential to leveraging the wisdom of the crowd to solve societal challenges. At its best, remixing can promote online community engagement, as well as support comprehensive and innovative solution generation. Organizers can maintain an active online community, community members can collectively innovate and learn, and, as a result, society can find new ways to solve important problems. We address what affects the generativity of a remix by revisiting the knowledge reuse for innovation process model. We analyze the reuse of proposals in Climate CoLab, an online innovation community that aims to address global climate change issues. Our application of several analytical methods to study factors that may contribute to the generativity of a remix reveals that remixes that include prevalent topics and integration metaknowledge are more generative. We conclude by suggesting strategies and tools that can help online communities better harness collective intelligence for addressing societal challenges.

Keywords: Societal Challenges, Climate Change, Innovation, Knowledge Reuse, Remixing, Online Communities, Collective Intelligence

Dr. Gautam Pant was the accepting senior editor. This research article was submitted on March 14, 2018 and underwent two revisions.

## 1 Introduction

Large-scale societal issues have been framed as wicked problems (Head & Alford, 2015; Rittel & Weber, 1973) and grand challenges (George et al., 2016). These challenges are difficult to solve. On the one hand, many of these challenges are urgent, yet there is no central authority to solve them. In fact, different stakeholders do not even agree on what these problems really are. On the other hand, these challenges are composed of complex dilemmas and emergent issues—all of which are dynamic, contextually bound, and require changes in individual and societal behaviors (George et al., 2016).

Traditionally, the policies and proposals to address societal challenges have been created by legislators, policy makers, and experts within organizations and businesses (Margolis & Walsh, 2003; Scherer & Palazzo, 2011; Callaghan, 2014). However, organizations and businesses are fundamentally unable to deal with these challenges on their own because their innovation pipeline is inherently replete with inefficiencies, delays, dictates of market mechanisms, and political decision-making (Chesbrough, 2006; Grimm et al., 2013). This problem has attracted interest in several different disciplines, including information systems (IS). One stream of IS research has focused on applying different information and communication technologies to help organizations address societal challenges (Leong et al., 2016; Srivastava, Teo, & Devaraj, 2016; Venkatesh et al., 2016). Another stream aligns with the open call to “consider emergent digital designing as a replacement for organizations” (Majchrzak, Markus, & Wareham, 2016). These IS researchers seek to solve societal challenges through the wisdom of the crowd, which is external to organizations (Brabham, 2008; Mergel & Desouza, 2013; Malone, 2018).

By nature, societal challenges reflect the issues and problems generally faced by society. Since crowds are often perceived to be capable of providing innovative solutions that may elude internal teams (Brabham et al., 2014; Certoma, Corsini, & Rizzi, 2015; Muller et al., 2015; Schlagwein & Bjørn-Andersen, 2014), crowdsourcing has recently been adopted to aid organizations and businesses in addressing societal challenges (Mergel & Desouza, 2013; Malone et al., 2017). One of the foremost examples of crowdsourcing is the Challenge.gov platform built following the principles of President Barack Obama’s Open Government initiative (White House, 2009). As an open innovation crowdsourcing initiative sponsored by the US government, Challenge.gov adopts a crowdsourcing approach aimed at engaging previously disenfranchised stakeholders to solve specific problems plaguing government agencies (Mergel & Desouza, 2013). Other crowdsourcing examples include Climate CoLab, which enables people from around the world to submit proposals for climate change solutions (Malone et al., 2017), and Foldit, which allows users to view and build on each other’s models of protein structures. Foldit has yielded solutions to medical problems in a matter of weeks that had thus far eluded scientists (Cooper et al., 2010; Khatib et al., 2011). Table A1 in the Appendix provides a summary of the main pros and cons of existing crowdsourcing usage for solving societal problems.

A major strength of crowdsourcing is that it generates a large number of ideas within a short amount of time, which is difficult to achieve within organizations (Chiu, Liang, & Turban, 2014; Majchrzak & Malhotra, 2013). Involving crowd members in solving societal challenges can also expand the exploration of the solution space because, by nature, the crowd engages in divergent thinking (Afuah & Tucci, 2012; Ward,

2001). In addition, inviting a general crowd to address a societal challenge increases public awareness of both related problems and potential solutions. Although crowdsourcing has many benefits, prior research has also expressed concerns regarding its potential problems (Bayus, 2013; Saxton, Oh, & Kishore, 2013). One main critique of crowdsourcing is that it lacks efficiency because many of the ideas generated are superficial or redundant (Bjelland & Wood, 2008). Another critique is that the crowd often fails to incorporate multiple perspectives when generating ideas (Schenk & Guittard, 2011). These two issues have stimulated general discussions regarding how to better use crowds to address complex problems, including societal challenges. One potential solution that has been identified is remixing, which involves a structure that allows for task division and integration. Through remixing, crowd members can build on, reuse, and recombine previous work performed by themselves and others to generate new ideas (Hill & Monroy-Hernández, 2013; Kyriakou, Nickerson, & Sabnis, 2017; Malone et al. 2017). Unlike the initial implementation of crowdsourcing, in which crowd members work on ideas independently, remixing allows crowd members to access others’ work, thus offering the potential to not only reduce redundancy but also deepen ideas, which, in turn, may yield lead to innovation at the collective level (Malone, 2018; Wisdom & Goldstone 2011). By integrating prior work, the crowd can also develop more comprehensive ideas. In addition, remixing presents a learning opportunity for all community members (Dasgupta et al., 2016) and crowd members can deepen their understanding of the domain knowledge through remixing each other’s work. Therefore, many online innovation communities have incorporated remixing into their platform design to harness collective intelligence (Cheliotis & Yew, 2009; Kyriakou et al. 2017; Resnick et al. 2009; Malone et al. 2017).

Remixing can be viewed as a process that supports knowledge reuse in online communities. While knowledge is sometimes reused for convenience—for example, reusing a piece of code to achieve the same result—we focus on knowledge reuse for the purpose of building deeper knowledge, a process called knowledge reuse for innovation (Armbrecht et al., 2001; Majchrzak, Cooper, & Neece, 2004). Previous studies on knowledge reuse for innovation (KRI) in offline settings mostly focus on examining factors that may affect the quality of the innovation (Boh 2008; Cheung, Chau, & Au, 2008), while studies on KRI in online settings tend to focus more on the generativity of the innovation (Hill & Monroy-Hernández, 2013; Kyriakou et al., 2017; Stanko, 2016). In general, a reusable innovation can trigger more contributions from other community members, which promotes online social engagement and supports innovative idea generation. In addition, generativity is essential to tackling societal challenges. Incentivizing reusable innovations may help increase the collective awareness of a societal challenge and expand the coverage of the solution space by inspiring more comprehensive solutions.

Although prior studies have examined multiple artifacts that affect the generativity of a newly created innovation (Hill & Monroy-Hernández, 2013; Kyriakou et al. 2017), these studies have not addressed remixing in the societal challenge domain. Solving a societal challenge is very different from the tasks addressed by online innovation communities that have been studied in previous research. This type of task has a specific objective, while other remixing tasks are generally more open-ended. Furthermore, while reuse in other online communities could occur at any point of the remix network, a sequential reuse process is critical for solving societal challenges in order to generate integrative new solutions. Finally, in solving societal challenges, no single solution or formulation of the problem is sufficient. Since different stakeholders may not even agree on the nature of the problem, there are no right or wrong answers, only answers that are better or worse from different points of view. Thus, bearing the uniqueness and complexity of these issues in mind, we explore possible ways of encouraging reusable innovative ideas to leverage the wisdom of the crowd to address societal challenges.

To better understand how remixing can help address societal challenges, it is important to clarify the nature of remixing in terms of the KRI process. Thus, we revisited the KRI process and implemented an analytical approach to understanding how the knowledge reuse process affects the generativity of an innovation. The KRI model is a six-stage process model that involves three major actions— reconceptualize the problem and approach, searchand-evaluate for ideas to reuse, and develop the selected idea (Majchrzak et al, 2004). Specifically, we pose the following research question in this paper: How do the three major actions in the knowledge reuse for innovation process affect the generativity of an innovation that addresses societal challenges? In other words, what processes may help someone reuse knowledge that can in turn generate more reuse for solving grand challenges?

To answer this research question, we collected and analyzed data from the Climate CoLab online innovation community, which specifically aims to address the societal challenge of global climate change (Malone et al., 2017). On the Climate CoLab website, community members are encouraged to participate in different contests by creating novel proposals that address global climate change. The creators of a proposal, also referred to as proposal contributors on the site, search for and integrate preexisting proposals when creating their novel entries, and these contests are designed to record traces of the knowledge reuse path: namely, what content has been reused, when it was reused, and whether this content emerged from previous content. Because of the complexity of societal challenges, we applied multiple text analytical methods, including a specialized technique that uses the community-generated Wikipedia ontology for topic detection and text similarity comparison. We examined the effect of the three major actions on the generativity of the final creation by analyzing three important outcome features of these actions: proposal topic prevalence, the number of high-quality proposals reused, and the encoded metaknowledge regarding the integration’s rationale.

This paper aims to contribute to both the knowledge reuse literature and the usage of emerging digital designs to leverage the wisdom of the crowd for tackling societal challenges (Majchrzak et al. 2016; Markus, 2001). Our findings reveal how the three major actions in the KRI process affect the reusability of a remix and suggest that incorporating prevalent topics when reconceptualizing the problem and encoding metaknowledge about the integration of the ideas reused when developing the integrated idea can increase the generativity of a final creation that addresses societal challenges. These findings can be generalized to other online innovation communities that may not be specifically designed to solve certain societal challenges but use collective intelligence to contribute to solutions for other complex problems. This paper also offers practical implications. Our findings provide knowledge workers with various strategies to increase the generativity of their creations and point to different tools that online innovation community designers can use to better support knowledge reuse for innovation in online communities.

Next, we present a brief review of related work, followed by our hypotheses. Then, we describe our empirical study and present our analyses and results. Finally, we discuss the implications for theory and practice and suggest future research possibilities.

## 2 Theoretical Development

## 2.1 Remixing as a Method to Support Innovation

Traditionally, in-house experts within an organization work on creating new product and service innovations via a private-collective innovation model (von Hippel & von Krogh, 2003). Currently, many organizations also use customers to generate new product and service ideas through open innovation initiatives (Chesbrough, 2006; Eservel, 2014). Open innovation can offer organizations new perspectives because it recognizes customers as not only a passive source of valuable information for marketing and sales divisions of organizations but also as active contributors to product innovation (Chesbrough & Crowther, 2006; Elmquist, Fredberg, & Ollila, 2009; Kristensson, Magnusson, & Matthing, 2002). While open innovation has been widely discussed by researchers, another term— crowdsourcing—has been used to describe the phenomenon in which strangers are recruited to accomplish tasks (Howe, 2006). Some researchers have identified crowdsourcing as a process that can produce open innovation (Estellés-Arolas & González-Ladrónde-Guevara, 2012; Phillips, 2010), while others have suggested that these two concepts exist at the same logical level and share the overlapping domain of crowd innovation (Howe, 2008).

The development of internet technology has promoted the reshaping of digital collaboration patterns in online communities (Hoegg et al. 2006), which has enabled the incorporation of knowledge reuse into the design of some online crowd innovation communities such as ccMixter, Climate CoLab, and Scratch (Cheliotis & Yew, 2009; Malone et al., 2017; Resnick et al., 2009). These sites allow users to search for and repurpose usergenerated content to generate creative outcomes and also trace the knowledge reuse path, i.e., what content has been reused and where this content came from within the community. Many scholars use remixing, a term originating in the music industry to describe the process of modifying music by changing the attributes of its component tracks, to refer to this traceable knowledge reuse and to describe combinations in online communities (Cheliotis et al., 2014; Faraj, Jarvenpaa, & Majchrzak, 2011; Lessig, 2008; Navas, 2012).

Remixing has a built-in feature of engagement in that it encourages people to build on each other’s work. Because of this, remixing can be used as a tool to support crowd creativity. Community members build upon others’ work to develop further innovations and then share these improvements for others to reuse (Hill & Monroy-Hernández, 2013; Nickerson, 2015; Sojer & Henkel 2010). Typical examples of this type of community include Wikipedia, where contributors collaborate in editing encyclopedia articles (Estellés-Arolas & González-Ladrón-de-Guevara, 2012); GitHub, where users build and reuse software code together (Dabbish et al., 2012); Scratch, where children create and remix projects using programming skills (Resnick et al., 2009); and Thingiverse, where participants design and recombine 3D printing ideas (Flath et al., 2017). Remixing can also be used to harness collective intelligence for citizen science projects such as the Climate CoLab website (Malone et al., 2017). To better use remixing for solving societal challenges and other complex tasks, it is essential to understand knowledge reuse in online communities.

## 2.2 Knowledge Reuse for Innovation

Knowledge reuse is commonly interpreted as the process of locating and using shared knowledge (Alavi & Leidner, 2001). Researchers believe that knowledge reuse is important to study because it contributes to combinative capabilities (Grant, 1996; Kogut & Zander, 1992) and innovation in organizations (Armbrecht et al., 2001; Majchrzak et al., 2004). To articulate knowledge reuse, researchers have created several frameworks, which have also served as foundations for later studies. For example, Grant (1996) developed a knowledgebased theory focusing on the analysis of knowledge integration mechanisms, Szulanski (2000) created a fourstage knowledge reuse process with a “knowledge reuse as replication” focus, and Markus (2001) developed a theory of successful knowledge reuse with an emphasis on knowledge management systems and repositories.

These models account for reuse for replication but not reuse for innovation. At best, reuse for replication contributes to incremental innovation rather than radical innovation, which involves different processes (Argote, 2012; Grant, 1996; Leonard & Sensiper, 1998). Knowledge reuse for replication focuses on knowledge acquisition in solving a problem or increasing productivity. In contrast, knowledge reuse for innovation involves knowledge integration—i.e., knowledge workers integrate others’ knowledge with their own knowledge to generate innovation. Therefore, Majchrzak, Cooper, and Neece (2004) built a staged process model for knowledge reuse for innovation that explains how innovators search for and recombine knowledge in order to generate new knowledge. In this paper, we refer to this model as the knowledge reuse for innovation (KRI) process model.

The KRI process model has been used as the foundation for a number of later studies. While a few researchers have extended the discussion and suggested enhancements (e.g., Chewar & McCrickard, 2005), most of these studies focus on the discussion of what artifacts affect the quality of the innovation and how to further optimize these artifacts to improve the knowledge reuse process (Boh, 2008; Durcikova & Fadel, 2016; Faniel & Majchrzak, 2007; Kankanhalli, Lee, & Lim, 2011; Khedhaouria & Jamal, 2015; Majchrzak & Malhotra, 2013). For example, Faniel and Majchrzak (2007) suggest ways to optimize knowledge management systems and technologies for knowledge reuse for innovation. Durcikova and Fadel (2016) discuss how knowledge electronic repositories can be better used at the search stage of knowledge reuse. In addition, several papers have explored how adaption, metaknowledge, and other factors influence knowledge reuse (McGrath & Parkes, 2007; Zhang & Watts, 2008). Despite the rich literature on knowledge reuse for innovation and the quality of the innovative outcome, few studies have explored the relationship between the process and the generativity/reusability of the innovative outcome.

## 2.3 Generativity in Remixing Research

The overarching goals of most online innovation communities are attracting more participation and generating creative work. Previous research suggests that remixing is an important form of online engagement (Banker, Bardhan, & Asdemir, 2006). Also, a reusable innovation may trigger more contributions from other community members, which could also contribute to the generation of innovative ideas. As both goals can be achieved by increasing the reusability of remixes, it is essential to study the reusability of creations in online innovation communities (Cheliotis et al., 2014; Hill & Monroy-Hernández, 2013). Previous studies have described the reusability of creations in online remixing communities as generativity or fecundity, which represents the number of times a work is remixed/reused (Hill & Monroy-Hernández, 2013), and have sought to determine factors that correlate with generativity (Hill & Monroy-Hernández, 2013; Jarvenpaa & Standaert, 2018; Stanko, 2016).

Some researchers have found that popularity, intertextuality, and derivativity, as well as the author’s fecundity and social embeddedness, all affect generativity (Cheliotis et al., 2014). To better understand generativity in a remixing community, Kyriakou, Nickerson, and Sabnis (2017) studied a 3D printing design community and discussed the relationship between reuse and metamodels—a type of reuse for innovation. However, metamodels are very specific components of the KRI process. By contrast, we are interested in the effects of the major actions in the knowledge reuse process on the reuse of the resulting innovation and the sequence of steps taken to create an innovation. Thus, there is a need to revisit the process of knowledge reuse for innovation to understand how the process affects generativity.

## 2.4 Three Major Actions in Knowledge Reuse for Innovation

The knowledge reuse for innovation process in Majchrzak, Cooper, and Neece (2004) has six stages: reconceptualize the problem and the approach for innovation, decide to search for reusable ideas, scan for reusable ideas, briefly evaluate reusable ideas, conduct in-depth analysis on reusable ideas and select one, and fully develop the reused idea. This process consists of three major actions: (1) reconceptualize the problem and approach, (2) search-and-evaluate ideas to reuse, and (3) develop the selected idea.

## 2.4.1 Major Action 1: Reconceptualize the Problem and Approach

The first major action in the knowledge reuse process model is to reconceptualize the problem and approach. In this action, creators redefine the problem and determine the main theme of their creation, seeking to find a balance between ambitious conceptualizations and the potential existence of an idea that they can reuse (Majchrzak et al., 2004). This leads to a tradeoff between novelty and prevalence. Examples of prevalent topics are commonly discussed fundamental topics or nonfundamental but popular topics trending within the community. Creators may be more likely to reuse prevalent topics because of their preferential attachment within the reuse network (Barabási & Albert, 1999) or because of familiarity (Brown & Duguid, 1991; Nonaka, 1994; Hutcheon, 2012). Therefore, we propose that prevalent topics are more likely to be reused, leading to the following hypothesis related to the performance of the first action in the knowledge reuse process model—the problem reconceptualization hypothesis:

H1: A remix containing more prevalent topics is more likely to be reused.

## 2.4.2 Major Action 2: Search-and-evaluate Ideas to Reuse

The second action in the knowledge reuse process model is searching for and evaluating ideas to reuse. In this action, creators select ideas that can be reused in their new idea. Both the quantity and quality of the ideas they select are indicators of the creator’s performance. Therefore, we measure the performance of this action by counting the number of high-quality ideas creators decide to reuse.

Some researchers have suggested that remixes tend to form chains; indeed, creations that are remixes themselves are more likely to generate future remixes in the online remixing community Scratch (Hill & Monroy-Hernández, 2013). However, another study examined a music remixing community and suggested that a music remix that reuses more previous music works is less likely to be reused by others because users find it easier to reuse a single work than to recombine multiple sources (Cheliotis & Yew, 2009). Later, researchers found that the relationship between the number of previous works reused in a remix and the generativity of the remix is not linear. Instead, there exists a U-shaped relationship (Cheliotis et al., 2014). Since the type of artifact studied in that paper is a special media form—music—we wanted to test whether the relationship observed in that study could be generalized to other remix communities. We therefore propose the following hypothesis related to the performance of the second action in the knowledge reuse for innovation process—the idea search and evaluation hypothesis:

H2: The number of high-quality ideas reused in a remix has a U-shaped relationship with the generativity of this remix.

## 2.4.3 Major Action 3: Develop the Selected Idea

The third action in the knowledge reuse for innovation process is idea development. In this action, creators incorporate the ideas reused to form a final creation. The key element in this action is the integration of the reused ideas. The performance of this action could be evaluated by the metaknowledge expressed about the integration, i.e., whether the creators have explicitly explained how they integrate the selected ideas and how well the aggregated information is related to the selected ideas.

Previous studies suggest that metaknowledge about an idea, such as describing the context and credibility of the source, affects a creator’s reuse decision, perhaps by reassuring the creator (Markus, 2001; Majchrzak et al., 2004). We extend this idea and hypothesize that including metaknowledge about how creators integrate reused knowledge has a positive influence on the generativity of this creation. That is, societal challenge solutions, such as proposals related to climate change, are complex artifacts that are composed of other artifacts. When this composition takes place, the composed elements relate to each other and to an overall goal. The extent to which the rationale for choosing a set of components and articulating how they contribute to each other matches the extent to which the proposal designers have provided integration metaknowledge. Previous work on design rationale has articulated the importance of such rationales to help designers think through their problem (Carroll & Rosson, 2003; Wang, Farooq, & Carroll, 2013). Other work on metaknowledge has noted that metaknowledge helps others understand design artifacts (Choi, Lee, & Yoo, 2010; Leonardi, 2014; Rico et al., 2008). Thus, more integration metaknowledge might be associated with more reuse for two reasons. It might reflect a more thoughtful design process leading to a better design, and it might serve as a signal to others that the design is, in fact, well-considered. In addition, metaknowledge about integration could serve as a boundary object: the higher the level of integration metaknowledge, the more effectively users across different boundaries will communicate (Carlile, 2002; Mark, Lyytinen, & Bergman, 2007; Nicolini, Mengis, & Swan, 2012; Star & Griesemer, 1989). This serves as the basis for our third hypothesis related to the performance of the third action in the knowledge reuse process model—the idea development hypothesis:

H3: A remix that encodes more integration metaknowledge is more likely to be reused.

## 3 Research Design

To answer our research question and test our hypotheses, we conducted an empirical study using data from Climate CoLab, an online innovation community addressing the important societal challenge of global climate change (Malone, Laubacher, & Dellarocas, 2010). In Climate CoLab, members collaborate with each other to enter contests by creating proposals. These contests aim to solve multiple subproblems associated with global climate change, such as carbon pricing, energy supply, and transportation (Figure 1). As of 2020, the website has a growing community of over 120,000 people.

We chose Climate CoLab for the following reasons. First, this online community seeks to harness collective intelligence using the remixing mechanism to solve an important societal challenge. Second, the goal of this online community is to generate innovative proposals, which is a form of innovation. Therefore, each innovative proposal is considered as an innovation in this study. Third, members of this community are from different backgrounds and geographic locations. The community members offer diverse and novel ideas, providing the exploration condition for knowledge reuse for innovation (Armbrecht et al., 2001). Fourth, Climate CoLab encourages knowledge reuse for innovation and has incorporated this approach into its contest design (Malone et al., 2017). There are three main types of contests offered by Climate CoLab: basic, regional, and global. Proposals for regional contests are encouraged to reuse proposals submitted to basic contests, and proposals for global contests are required to reuse proposals from regional contests (Figure 2). In addition, proposal contributors are required to provide links to the proposals they use. This reuse information helps identify reuse relationships and strengthens the proposal reuse network (Figure 3). More importantly, it makes it possible to quantify and examine the generativity of the remixes.

## 3.1 Data Collection

Given our focus on the generativity of remixes, our empirical study analyzed proposals in the regional contests because these contests both reuse knowledge (proposals in the basic contests) and have been reused by others (proposals in the global contest). We collected all the proposals submitted to the 2015 regional contests and global contest on the Climate CoLab website.

## 3.2 The Dependent Variable: Generativity

Since we evaluate reuse for innovation based on the generativity of a proposal, our dependent variable for all hypotheses in this paper is the generativity of a remix: i.e., how many times a remix has been reused. We measure generativity by counting the number of times a regional proposal has been reused in global proposals. As shown in Figure 4, in each global proposal, there is a section providing hyperlinks (in blue) to the specific regional proposals reused by the proposal contributors. We collected information from this section for all global proposals to calculate the generativity of each regional proposal. For example, if a regional proposal was reused in three different global proposals, we recorded the generativity of this regional proposal as 3.

## 3.3 Independent Variables

## 3.3.1 Independent Variable for H1

Proposal topic prevalence is the independent variable used for H1. To determine the prevalence of a proposal, we calculated the proposal topic prevalence for each regional proposal to see if the creator included knowledge that was prevalent in the contest. A proposal with a high proposal topic prevalence score included either fundamental topics that were commonly discussed or popular topics within the contest that were familiar to other community members, or both.

![](/api/attachments/G3PEG9MU/fulltext/images/62c0981cc9fff9355548a67bc448ac9f824e446dbfb56b666d9fa8414aa9b3c2.jpg)  
Figure 1. Contests on the Climate CoLab Website

![](/api/attachments/G3PEG9MU/fulltext/images/bae647c7b89552d81ae9d13ee0f5f3cf959925918abdc8787dd1b97d0927d9b2.jpg)  
Figure 2. Climate CoLab Proposal Reuse Structure

![](/api/attachments/G3PEG9MU/fulltext/images/de5d848f44e86e002eb4da58aeb715e954ea62c106bccda360da7fd6050a09b2.jpg)  
Note: Each node represents a proposal and is colored based on their owner. Proposals that share the same owner have the same color. If a proposal owner has only created one proposal, the proposal is colored in white.  
Figure 3. Proposal Reuse Network in the Climate CoLab Website

![](/api/attachments/G3PEG9MU/fulltext/images/1a7da4dec7644d3371caa8791229a2572a52ceb49009f6cd58c7400a0a08364f.jpg)  
Figure 4. Links to Regional Proposals in a Section of a Global Proposal

One of the most popular approaches to describing which topics are covered in a document (which is the proposal in our case) and what a document is about is to describe the document with relevant terms that represent semantic concepts important to the document. This is an ontology-based approach (Zouaq, Gasevic, & Hatala, 2011). Ontologies are defined as the explicit formal specifications of the terms in a domain and the relations among them (Gruber, 1993); hence, they tend to encompass only a single domain corpus (i.e., medicine, wine, etc.). The domain corpus must have good coverage of domain knowledge for generating a comprehensive ontology. Existing work has exploited different sources that may serve ontology corpora. Some early studies used corpora that were manually established by domain experts (Baker, Filmore, & Lowe, 1998) or corpora derived from books, magazines, or news organizations automatically or semi-automatically (Khan, Luo, & Yen, 2002). However, these corpora are difficult to extend because the knowledge contained in such corpora is fixed in time and by region and cannot be easily updated. Later studies utilized web-based corpora such as DBpedia and Wikipedia (Gabrilovich & Markovitch, 2007; Yu, Thom, & Tam, 2007)

because these sources contain vast amounts of highly organized human knowledge and they undergo constant development (Kane, 2011; Keegan, Gergle & Contractor, 2013), meaning that the breadth and depth of such corpora steadily increase over time.

Thus, in order to identify the topics of each proposal, we opted to use Wikipedia because it is currently the largest knowledge corpus on the Web. Wikipedia is available in dozens of languages. The largest version, the English version, contains over 3.6 billion words in over 3.6 million articles and is 90 times larger than the next largest online English-language encyclopedia, Encyclopedia Britannica (“Wikipedia: Size comparisons,” 2020, para. 3). To automatically identify the topics covered in a proposal, we extracted the plain text of each proposal and employed a twostep process developed by Genc, Mason, and Nickerson (2013).

In the first step, we identified candidate concepts within the main text of a proposal and mapped them to corresponding Wikipedia pages. To extract these concepts, we first removed stop-words and punctuation marks and segmented the main text into ngrams in sliding window fashion. Then, we searched for the n-grams using a Wikipedia title search. In Wikipedia, all pages are tagged with categories that they belong to and these categories are linked to each other in a network graph structure. For each proposal, we recorded all categories listed in the corresponding Wiki pages.

In the second step, we used the category network to determine a common set of high-level topics based on the Wiki pages identified in the first step (Figure 5). At the time of our analysis, Wikipedia included 28 main topic categories (“Category: Main topic classifications,” 2019, para. 5). When we traversed five (or more) levels of the category graph, most of our initial topics hit one of those main topic categories, meaning that all of the proposals then shared a topic and were connected to each other. Thus, we stopped the traversal at level four for each proposal and recorded all identified categories as the topics covered.

We then calculated the topic prevalence score for each topic within a contest. The topic prevalence score is the degree of topic node divided by the maximum possible topic degree. For example (Figure 6), in contest X, there are four proposals and Topic 2 is covered in one proposal. The topic prevalence score for Topic 2 is then calculated as 1 divided by 4. After calculating this for each proposal, we computed a proposal topic prevalence score by summing up the topic prevalence score of all the topics presented in a proposal. For example, in Proposal B, two topics are covered, Topic 1 and Topic 2. Thus, the proposal topic prevalence score for this proposal would be 1.

![](/api/attachments/G3PEG9MU/fulltext/images/85ebe33205ad2ebea758b5be78b73eb849a7d9a29b9048d9f80987e608921dbe.jpg)  
Figure 5. Identifying Topics in a Regional Proposal

![](/api/attachments/G3PEG9MU/fulltext/images/5ee7e2557b7842cda42b40502f90aa15141ee8530cdc042b10526c6011770a69.jpg)  
Figure 6. Calculating Proposal Topic Prevalence

![](/api/attachments/G3PEG9MU/fulltext/images/4423a615cec3b6a88c4976a3fea394889b464f75a906b34509b67e476dcfe7c0.jpg)  
Figure 7. A Section in Regional Proposals that Provides Reuse Links and Integration Metaknowledge

![](/api/attachments/G3PEG9MU/fulltext/images/e9595f3c222ba9e11985011b53727edb1f7f66cd5882ab7e05362f06dfcca4ee.jpg)  
Figure 8. An Example of a High-Quality Basic Proposal

![](/api/attachments/G3PEG9MU/fulltext/images/0effa39ef802115dbbaae2418d5cfccf0cec0bfef7f3618db45dafef93aea975.jpg)  
Figure 9. The Integration Section of a Sample Regional Proposal

## 3.3.2 Independent Variable for H2

Number of high-quality proposals reused is the independent variable used for H2. In Climate CoLab contests, there is a special section in each regional proposal where proposal contributors can create hyperlinks to the basic proposals they reused and record how they incorporated these proposals (Figure 7). We analyzed the information in this section for each regional proposal to identify the basic proposals that were reused. Then, we checked each basic proposal’s expert evaluation to determine its quality.

In Climate CoLab, each proposal in a basic contest is rated by a group of experts. These experts evaluate proposals based on their quality and advance highquality proposals to enter the semifinal phase for further development. If a basic proposal has been selected by CoLab experts as a semifinalist in that basic contest (Figure 8), we counted this proposal as a high-quality proposal. Then, we calculated the total number of high-quality proposals reused by each regional proposal.

## 3.3.3 Independent Variable for H3

Integration metaknowledge is the independent variable used for H3. To understand how metaknowledge affects generativity, we extracted information from the section shown in Figure 7 for each regional proposal and automatically coded all regional proposals. We extracted the content from this integration section (e.g., Figure 9) and analyzed the hyperlinks (words in blue) and plain text (words in black). Hyperlinks indicate whether a regional proposal integrated basic subproposals and plain text contains information about the integration metaknowledge, i.e., whether metaknowledge was included in a regional proposal and, if so, the content of the metaknowledge. In addition, we extracted the text from the summary section (e.g., the summary section shown in Figure 8) from all basic proposals that had been reused by a regional proposal and conducted a text similarity analysis using Jaccard similarity between the integration section of the regional proposal and the summary section of all the basic proposals it reused. Therefore, the integration metaknowledge score calculated for each regional proposal includes two parts: (1) whether the regional proposal included direct links to the basic proposals it reused, and (2) whether the regional proposal integration section covered text similar to the basic proposals it reused, as indicated by the Jaccard similarity. Thus, beyond indicating the existence of metaknowledge, the integration metaknowledge score also reveals the amount of integration metaknowledge: the higher the score, the more metaknowledge coverage. The more metaknowledge coverage, we reason, the better the articulation of how all the components of the proposal relate to each other and the proposal as a whole.

## 3.4 Control Variables

Our study controlled for the factors related to the proposal contributors and the CoLab reuse structure (Figure 10). At the time of our analysis, the contributor who started a proposal was identified on the site as the proposal owner. The proposal owner can invite and add other CoLab members as proposal contributors. The control variables associated with the proposal contributors are the number of contributors, the proposal owner’s tenure, and owner network control. The number of contributors represents the number of participants who edited the proposal, which could influence the generativity of a remix because of preferential attachment within the user network (Barabási & Albert, 1999). Prior literature suggests that a creator’s experience is important in generating reusable creations (Lim, 1994; Kyriakou et al., 2017). As we found no information about a creator’s amount of experience outside of the community, we measured the level of expertise of proposal owners based on their Climate CoLab tenure—specifically, the number of days they belonged to CoLab before creating the proposal (proposal owner’s tenure). Such community tenure variables have been used in many other studies of online communities (Bateman, Gray, & Butler, 2011; Faraj, Kudaravalli, & Wasko, 2015; Kyriakou et al., 2017; Mein Goh, Gao, & Agarwal, 2016). Some proposal owners created more than one regional proposal, which may have led to a user-network effect. Therefore, we also controlled for this factor using an owner network control variable: If the owner of a regional proposal created more than one regional proposal, we marked the proposal as 1, otherwise 0.

The control variables associated with the CoLab reuse structure are the sequence of proposal creation and the fixed effect of the regional contest. The sequence of proposal creation is a time-related control variable that indicates which proposals were created early and which were created later. Proposals that were created earlier have greater potential to be seen by other community members, as they have been on the website for a longer time. Global proposals on the Climate CoLab website are required to reuse only one proposal from each regional contest. Since each regional contest varies in number of entries, proposals in different regional contests may face different levels of competition. Thus, we also controlled for this fixed effect.

![](/api/attachments/G3PEG9MU/fulltext/images/a55cb1fea9aa4ffbeca22d12267c398e8fa9057cce2e7b0ecdc2cad9892c36cc.jpg)  
Figure 10. Research Model

Table 1. Descriptive Statistics of All Variables

<table><tr><td>Variable</td><td>Obs</td><td>Mean</td><td>SD</td><td>Min</td><td>Median</td><td>Max</td></tr><tr><td>Generativity</td><td>81</td><td>1.148</td><td>1.476</td><td>0</td><td>1</td><td>5</td></tr><tr><td>Proposal topic prevalence</td><td>81</td><td>170.704</td><td>155.304</td><td>4</td><td>126</td><td>889</td></tr><tr><td>Number of high-quality proposals reused</td><td>81</td><td>0.975</td><td>2.392</td><td>0</td><td>0</td><td>11</td></tr><tr><td>Integration metaknowledge</td><td>81</td><td>0.312</td><td>0.480</td><td>0</td><td>0</td><td>1.118</td></tr><tr><td>Number of contributors</td><td>81</td><td>1.593</td><td>2.072</td><td>1</td><td>1</td><td>14</td></tr><tr><td>Sequence of proposal creation</td><td>81</td><td>9.481</td><td>7.321</td><td>1</td><td>7</td><td>29</td></tr><tr><td>Proposal owner&#x27;s tenure</td><td>81</td><td>260.815</td><td>407.472</td><td>0</td><td>52</td><td>1698</td></tr><tr><td>Owner network control</td><td>81</td><td>0.469</td><td>0.502</td><td>0</td><td>0</td><td>1</td></tr></table>

## 4 Analysis and Results

To test our hypotheses, we created a series of Poisson regression models. All regression models have the same dependent variable and control variables. We followed Green’s (1991) formula to determine the number of observations for our regression models. The descriptive statistics of all variables are listed in Table 1. We standardized all the independent variables and control variables in all regression models. We also conducted a post hoc power analysis for each model. The results for both the Poisson regression and power analysis are presented in Table 2. The correlation table and multicollinearity check can be found in the Appendix (Table A2 & A3).

Table 2 shows five Poisson regression models. Model 1 is a basic regression model with all control variables. The number of contributors, the owner network control, and the sequence of proposal creation have no significant influence on generativity. The proposal owner’s tenure is positively associated with the generativity of a remix: A regional proposal created by experienced users is more likely to be reused by global proposals.

Model 2 tests the relationship between the proposal topic prevalence with the generativity of a regional proposal. The result shows that proposal topic prevalence has a positive influence on the generativity of a remix, which suggests that proposals that include more prevalent topics are more likely to be reused in the future. Therefore, H1 is supported.

In Model 3, we study both the quantity and quality of proposals that have been reused. We examined whether the number of high-quality basic proposals reused in a regional proposal has a U-shaped relationship with the generativity of the proposal. The result shows that there is no significant curvilinear relationship between the two variables. Therefore, H2 is not supported.

Model 4 tests the integration metaknowledge. In this model, we examined the influence of integration metaknowledge on the generativity of a regional proposal. The result of Model 4 suggests that encoding more integration metaknowledge has a positive influence on the generativity of a remix: the higher the coverage of the metaknowledge, the more likely it is that the regional proposal will be reused by global proposals. Therefore, H3 is supported. Based on our analysis and results, we summarize our findings in Table 3.

Table 2. Poisson Regression Model for Generativity

<table><tr><td></td><td></td><td>Model 1</td><td>Model 2</td><td>Model 3</td><td>Model 4</td></tr><tr><td rowspan="5">Control</td><td>Constant</td><td>-0.822*</td><td>-0.883*</td><td>-0.706*</td><td>-0.886*</td></tr><tr><td>Number of contributors</td><td>0.099</td><td>0.084</td><td>0.120</td><td>0.153</td></tr><tr><td>Sequence of proposal creation</td><td>-0.099</td><td>-0.024</td><td>-0.023</td><td>-0.129</td></tr><tr><td>Proposal owner&#x27;s tenure</td><td>0.449***</td><td>0.487***</td><td>0.541***</td><td>0.450***</td></tr><tr><td>Owner network control</td><td>-0.020</td><td>-0.096</td><td>-0.177</td><td>-0.041</td></tr><tr><td rowspan="5">Fixed effect (contest)</td><td>1303007</td><td>1.262**</td><td>0.864</td><td>0.596</td><td>0.665</td></tr><tr><td>1302013</td><td>1.348**</td><td>0.368</td><td>-0.038</td><td>0.148</td></tr><tr><td>1302019</td><td>0.549</td><td>0.827</td><td>0.651</td><td>0.908</td></tr><tr><td>1302025</td><td>0.875*</td><td>0.954*</td><td>0.725</td><td>0.618</td></tr><tr><td>1302031</td><td>1.177**</td><td>0.983*</td><td>0.718</td><td>0.923*</td></tr><tr><td>H1</td><td>Proposal topic prevalence</td><td></td><td>0.478***</td><td>0.557***</td><td>0.528***</td></tr><tr><td rowspan="2">H2</td><td>Number of high-quality proposals reused</td><td></td><td></td><td>0.226</td><td>-0.432</td></tr><tr><td>Number of high-quality proposals reused (squared)</td><td></td><td></td><td>-0.373</td><td>0.131</td></tr><tr><td>H3</td><td>Integration metaknowledge</td><td></td><td></td><td></td><td>0.366**</td></tr><tr><td colspan="6"></td></tr><tr><td colspan="2">Number of observationsMcFadden&#x27;s R-square</td><td>810.208</td><td>810.277</td><td>810.285</td><td>810.310</td></tr><tr><td colspan="2">Power analysis: Effect sizePower (sig.level = 0.05)</td><td>0.260.88</td><td>0.380.97</td><td>0.400.97</td><td>0.450.98</td></tr><tr><td colspan="6">Note: ***p&lt;0.001, **p&lt;0.01, *p&lt;0.05</td></tr></table>

Table 3. Summary of Findings

<table><tr><td>Hypotheses</td><td>Results</td></tr><tr><td>H1: A remix containing more prevalent topics is more likely to be reused.</td><td>Supported</td></tr><tr><td>H2: The number of high-quality ideas reused in a remix has a U-shape relationship with the generativity of this remix.</td><td>Not supported</td></tr><tr><td>H3: A remix that encodes more integration metaknowledge is more likely to be reused.</td><td>Supported</td></tr></table>

## 5 Discussion

This empirical study explored the relationship between the three major actions in the knowledge reuse for innovation process and the generativity of the innovative outcome created to address societal challenges. As shown in Table 3, H1 is supported. This finding suggests that the decision a creator makes when reconceptualizing the problem is essential to the generativity of a remix. Addressing a given problem with prevalent topics lowers the barrier for future adaptation and thus increases the reusability of a remix.

Previous studies have suggested that the number of previous works reused in a remix and the generativity of this remix follows a U-shaped relationship (H2). In our study, this was not supported, a finding that may be potentially related to the difference in the media form of the creations examined here. Previous studies were conducted using data from either ccMixter or Scratch; the former generates music remixes and the latter generates projects using a drag and drop programming language. In both communities, the knowledge reuse is direct and explicit. Creators in these communities are allowed and encouraged to embed the reused work or part of the work to serve a specific need. For example, in ccMixter, creators can directly incorporate a piece of drumbeat for the background in a music remix. Meanwhile, creators in Scratch can also fork a piece of code to achieve a function in their remixes. On the other hand, the knowledge reuse in Climate CoLab is quite different. Proposal contributors are unlikely to directly reuse sentences from the ideas that they are reusing; rather, the reuse is more likely to happen on the conceptual level. This suggests that the number of highquality proposals reused may be less important than the interrelationship among reused ideas.

Integration is the key component when developing an idea by reusing knowledge. Our results support the argument that encoding more integration metaknowledge increases the generativity of a remix (H3). Including integration metaknowledge and providing better coverage of topics in the component artifacts of the proposal signal the quality of integration, as it shows that the creator has fully understood the reused content and developed a clear logic when integrating the knowledge. In addition, integration metaknowledge serves as an index that may help people better understand the structure of the idea and the connections between the knowledge reused in a remix and hence increases the remix’s potential for adaptation in the future. Especially for members of online innovation communities who mostly participate in their spare time and are limited in terms of the time they can devote to a creation (Paulini, Maher, & Murty, 2014; Zhang, Hahn, & De, 2013), integration metaknowledge creates quick access to knowledge and improves the efficiency of knowledge reuse.

## 5.1 Theoretical Contributions

The theoretical contributions of our study are twofold. First, our study contributes to improved use of crowdsourcing for tackling societal challenges by explicating the role of remixing in leveraging the wisdom of the crowd. For complex tasks like solving societal challenges, remixing can better harness collective intelligence and motivate more comprehensive creations, as it encourages collaboration and integration, which can help cross the knowledge boundaries that exist in most crowdsourcing contexts. Second, our study also contributes to the knowledge reuse literature in that it is one of the first attempts to examine the relationship between the KRI process and the generativity of the innovative outcome in online settings. The analytical approach in our study deepens the understanding of the impact of the performance of the three major actions addressed here and shows that incorporating prevalent topics when reconceptualizing the problem and encoding more integration metaknowledge when developing the integrated idea can increase the generativity of the final creation.

## 5.2 Implications for Knowledge Creators and Platform Designers

Our study also has practical implications because it can help both knowledge workers and online innovation community designers better harness the wisdom of the crowd through remixing to address societal challenges. Our findings suggest that creators can adopt certain strategies to increase the reusability of their creations when they build off previous artifacts. Creators can widely browse previous creations and incorporate prevalent topics when reconceptualizing the problem; they can also think through their integration rationale carefully and provide an explicit and comprehensive summary through integration metaknowledge.

Increasing the generativity of remixes is beneficial not only to generating individual innovative ideas but also to maintaining an active community because it encourages more collaboration and communication among community members and potentially leads to more user activity. Thinking along these lines, another implication of our study is that designers of online innovation communities might consider introducing features and applying analytics to help creators perform better in each step of the knowledge reuse for innovation process.

One essential factor that influences creators when they are reconceptualizing the problem is their knowledge of the solution space. It is almost impossible to adopt a good strategy if they have little understanding of what knowledge is available. Due to the constantly growing number of artifacts in online communities, it may be very difficult to browse all submissions. Therefore, it could be helpful to conduct large-scale text analytics and incorporate a design feature that automatically detects and summarizes the solution space for community members. For example, creating an idea heat map or an idea network could be a good way to help people create an overall picture of the current solution space.

When searching for and evaluating ideas to reuse, creators face a different environment in online communities. These communities tend to provide a more open environment that allows all community members to see each other’s creations. Creators in these communities can easily access many resources. However, this often leads to information overload. The way to support this action in online communities is not by maximizing the number of available artifacts but streamlining search. Therefore, we conjecture that applying text analytics and similarity calculations to develop tools like recommender systems (e.g., Siangliulue et al., 2016) will improve the efficiency of search and, in turn, lead to increased generativity.

Those performing the third action in the knowledge reuse for innovation process—developing the idea— may seek to access the source of the reused knowledge to better understand and thus integrate the knowledge. Making this communication easier aids the performance of integration. Currently, many online communities have already incorporated a withincommunity email system. To help community members communicate in a timely fashion, it might also be worthwhile to consider including an instant messaging system. In addition, expression of integration metaknowledge might be motivated through templates that encourage short summaries of all artifacts and short rationales to explain why some sets of artifacts were reused in a particular work. The short summaries could encourage recombination and the rationales could serve to demonstrate that the work has solid foundations. In addition, large-scale text analytics could be applied to help improve the quality of integration metaknowledge: the coverage calculation described above could be automatically calculated and provided to users to encourage revisions and improvements.

## 6 Limitations and Future Work

Adopting remixing does not guarantee the success of an online innovation community. Large-scale problem solving requires the task to be well divided and solutions to be well combined (Kittur et al., 2013; Malone, 2018). The platform studied in this paper, Climate CoLab, has fulfilled these requirements. The task was well divided by experts based on the topic and geographic location, and the remixing structure was also well designed, as it allows multiple modes of inheritance, encouraging both diversity and integrity (Malone et al., 2017). These strengths of the platform design greatly aided our analytical approach in addressing the research question. Yet our analytical methods may not be applied to all online remixing communities. For platforms that do not provide such traceable reuse structures or sections for integrating metaknowledge, other analytical methods may be adopted to automate the analyses. And, given that this study was observational, and given that online communities often have feedback loops that create endogeneity issues, future research might use experiments to better understand the causal factors that drive quality.

Our study subject is an online innovation community that aims to solve global climate change issues. We suggest that remixing can be used in a similar fashion to leverage crowdsourcing creativity to address other societal challenges. In evaluating whether our findings are generalizable to other types of innovation communities, it is possible to look at other online open innovation communities such as GitHub (Dabbish et al., 2012) and Scratch (Resnick et al., 2009) to see if the reuse processes in these communities are similar. The proposals in our study are text-based creations. Future studies might involve sites that allow for remixing in different media forms.

Our study also suggests a few additional research questions that could be examined in future research: Are there any relational variables that influence the generativity of a remix in online communities? For example, does the creator’s position in the user network affect the generativity of his or her creation? This could be examined via network analysis that checks for network autocorrelation. In addition, the co-occurrence of proposals that are being reused could be analyzed: What kind of proposals and proposal topics are more likely to be reused together? How does this affect the generativity and quality of the higher-level proposal? In this paper, we briefly mentioned that online communities provide more open environments than organizations. Future research could examine what the major differences between knowledge reuse processes in online communities and in organizations are, using qualitative analysis to explore and reveal these major differences.

## 7 Conclusion

Reusing knowledge to generate innovative ideas to address societal challenges is a complex task. This study examines the relationship between the knowledge reuse process model and the generativity of the outcome. Our findings suggest that the major actions in this process model directly influence the generativity of a remix. Knowledge workers could adopt varied strategies to generate reusable artifacts and designers of online communities could build tools that make exploration of artifacts easier in order to encourage recombination. They could also apply multiple analytical methods to build tools that help users think through their reasoning for reusing combinations of artifacts. Rationales may be helpful for both the integrator and the future creator who may wish to reuse the integrated package. Together, a knowledge repository could be developed for solving societal challenges. That is, creators could communicate with themselves and also with the prospective remixers of their work, thus creating a kind of structured memory for their future selves as well as their future community.

## Acknowledgments

This material is based upon work supported by the National Science Foundation under grants 1909803, 1717473, 1442840, and 1422066.

## References

Afuah, A., & Tucci, C. L. (2012). Crowdsourcing as a solution to distant search. Academy of Management Review, 37(3), 355-375.

Alavi, M., & Leidner, D. E. (2001). Knowledge management and knowledge management systems: Conceptual foundations and research issues. MIS Quarterly, 25(1), 107-136.

Argote, L. (2012). Organizational learning: Creating, retaining and transferring knowledge. Springer

Armbrecht Jr, F. R., Chapas, R. B., Chappelow, C. C., Farris, G. F., Friga, P. N., Hartz, C. A., Mcllvaine, E., Postle, S. R., & Whitwell, G. E. (2001). Knowledge management in research and development. Research Technology Management, 44(4), 28-48.

Baker, C. F., Fillmore, C. J., & Lowe, J. B. (1998). The Berkeley framenet project. Proceedings of the 17th International Conference on Computational Linguistics.

Banker, R. D., Bardhan, I., & Asdemir, O. (2006). Understanding the impact of collaboration software on product design and development. Information Systems Research, 17(4), 352-373.

Barabási, A. L., & Albert, R. (1999). Emergence of scaling in random networks. Science, 286(5439), 509-512.

Bateman, P. J., Gray, P. H., & Butler, B. S. (2011). Research note—the impact of community commitment on participation in online communities. Information Systems Research, 22(4), 841-854.

Bayus, B. L. (2013). Crowdsourcing new product ideas over time: An analysis of the Dell IdeaStorm community. Management Science, 59(1), 226- 244.

Bjelland, O. M., & Wood, R. C. (2008). An inside view of IBM’s “Innovation Jam.” MIT Sloan Management Review, 50(1), 32.

Boh, W. F. (2008). Reuse of knowledge assets from repositories: A mixed methods study. Information & Management, 45(6), 365-375.

Brabham, D. C. (2008). Crowdsourcing as a model for problem solving: An introduction and cases. Convergence, 14(1), 75-90.

Brabham, D. C. (2009). Crowdsourcing the public participation process for planning projects. Planning Theory, 8(3), 242-262.

Brabham, D. C., Ribisl, K. M., Kirchner, T. R., & Bernhardt, J. M. (2014). Crowdsourcing applications for public health. American

Journal of Preventive Medicine, 46(2), 179- 187.

Brown, J. S., & Duguid, P. (1991). Organizational learning and communities-of-practice: toward a unified view of working, learning, and innovation. Organization Science, 2(1), 40-57.

Callaghan, C. W. (2014). Crowdfunding to generate crowdsourced R&D: The alternative paradigm of societal problem solving offered by second generation innovation and R&D. The International Business & Economics Research Journal (Online), 13(6), 1599.

Carlile, P. R. (2002). A pragmatic view of knowledge and boundaries: Boundary objects in new product development. Organization Science, 13(4), 442-455.

Carroll, J. M., & Rosson, M. B. (2003). Design rationale as theory. In J. M. Carroll (Eds.), HCI models, theories and frameworks: Toward a multidisciplinary science (pp. 431-461). Morgan Kaufmann Publishers.

Category: Main topic classifications. (2019). Wikipedia. https://en.wikipedia.org/wiki/ Category:Main\_topic\_classifications.

Certoma, C., Corsini, F., & Rizzi, F. (2015). Crowdsourcing urban sustainability. Data, people and technologies in participatory governance. Futures, 74, 93-106.

Cheliotis, G., & Yew, J. (2009). An analysis of the social structure of remix culture. Proceedings of the Fourth ACM International Conference on Communities and Technologies.

Cheliotis, G., Hu, N., Yew, J., & Huang, J. (2014). The antecedents of remix. Proceedings of the 17th ACM Conference on Computer Supported Cooperative Work & Social Computing.

Chesbrough, H. W. (2006). Open innovation: The new imperative for creating and profiting from technology. Harvard Business Press.

Chesbrough, H., & Crowther, A. K. (2006). Beyond high tech: Early adopters of open innovation in other industries. R&d Management, 36(3), 229- 236.

Cheung, P. K., Chau, P. Y., & Au, A. K. (2008). Does knowledge reuse make a creative person more creative? Decision Support Systems, 45(2), 219-227.

Chewar, C. M., & McCrickard, D. S. (2005). Links for a human-centered science of design: Integrated design knowledge environments for a software development process. Proceedings of the 38th

Annual Hawaii International Conference on Systems Sciences.

Chiu, C. M., Liang, T. P., and Turban, E. (2014). What can crowdsourcing do for decision support? Decision Support Systems, 65, 40-49.

Choi, S. Y., Lee, H., & Yoo, Y. (2010). The impact of information technology and transactive memory systems on knowledge sharing, application, and team performance: A field study. MIS Quarterly, 34(4), 855-870.

Cooper, S., Khatib, F., Treuille, A., Barbero, J., Lee, J., Beenen, M., Leaver-Fay, A., Baker, D & Popović, Z. (2010). Predicting protein structures with a multiplayer online game. Nature, 466(7307), 756.

Dabbish, L., Stuart, C., Tsay, J., & Herbsleb, J. (2012). Social coding in GitHub: Transparency and collaboration in an open software repository. Proceedings of the 15th ACM Conference on Computer Supported Cooperative Work & Social Computing.

Dasgupta, S., Hale, W., Monroy-Hernández, A., & Hill, B. M. (2016). Remixing as a pathway to computational thinking. Proceedings of the ACM 2016 Conference on Computer-Supported Cooperative Work & Social Computing.

Durcikova, A., & Fadel, K. J. (2016). Knowledge sourcing from repositories: The role of system characteristics and psychological climate. Information & Management, 53(1), 64-78.

Elmquist, M., Fredberg, T., & Ollila, S. (2009). Exploring the field of open innovation. European Journal of Innovation Management, 12(3), 326-345.

Eservel, U. Y. (2014). IT-enabled knowledge creation for open innovation. Journal of the Association for Information Systems, 15(11), 805.

Estellés-Arolas, E., & González-Ladrón-De-Guevara, F. (2012). Towards an integrated crowdsourcing definition. Journal of Information Science, 38(2), 189-200.

Faniel, I. M., & Majchrzak, A. (2007). Innovating by accessing knowledge across departments. Decision Support Systems, 43(4), 1684-1691.

Faraj, S., Jarvenpaa, S. L., & Majchrzak, A. (2011). Knowledge collaboration in online communities. Organization Science, 22(5), 1224-1239.

Faraj, S., Kudaravalli, S., & Wasko, M. (2015). Leading collaboration in online communities. MIS Quarterly, 39(2), 393-412.

Flath, C. M., Friesike, S., Wirth, M., & Thiesse, F. (2017). Copy, transform, combine: Exploring the remix as a form of innovation. Journal of Information Technology, 32(4), 306-325.

Gabrilovich, E., & Markovitch, S. (2007). Computing semantic relatedness using Wikipedia-based explicit semantic analysis. Proceedings of the International Joint Conference on Artificial Intelligence.

Genc, Y., Mason, W. A., & Nickerson, J. V. (2013). Classifying short messages using collaborative knowledge bases: Reading Wikipedia to understand Twitter. Making Sense of Microposts Workshop Concept Extraction Challenge Proceedings.

George, G., Howard-Grenville, J., Joshi, A., & Tihanyi, L. (2016). Understanding and tackling societal grand challenges through management research. Academy of Management Journal, 59(6), 1880-1895.

Gossel, B. M., Brüntje, D., & Will, A. (2016). Crowd and society: Outlining a research programme on the societal relevance and the potential of crowdfunding. In D. Brüntje & O. Gajda (Eds.), Crowdfunding in Europe (pp. 55-67). Springer.

Grant, R. M. (1996). Prospering in dynamically competitive environments: Organizational capability as knowledge integration. Organization Science, 7(4), 375-387.

Green, S. B. (1991). How many subjects does it take to do a regression analysis. Multivariate Behavioral Research, 26(3), 499-510.

Grimm, R., Fox, C., Baines, S., & Albertson, K. (2013). Social innovation, an answer to contemporary societal challenges? Locating the concept in theory and practice. Innovation: The European Journal of Social Science Research, 26(4), 436-455.

Gruber, T. (1993). What is an ontology? WWW Site. http://www-ksl.stanford.edu/kst/what-is-anontology.html.

Head, B. W., & Alford, J. (2015). Wicked problems: Implications for public policy and management. Administration & Society, 47(6), 711-739.

Hill, B. M., & Monroy-Hernández, A. (2013). The remixing dilemma: The trade-off between generativity and originality. American Behavioral Scientist, 57(5), 643-663.

Hoegg, R., Martignoni, R., Meckel, M., & Stanoevska-Slabeva, K. (2006). Overview of business models for Web 2.0 communities. In K. Meißner & M. Engelien (Eds.), Virtuelle

Organisation und neue Medien 2006 (pp. 33- 50). TUDpress.

Howe, J. (2006). The rise of crowdsourcing. Wired. https://www.wired.com/2006/06/crowds/

Howe, J. (2008). Crowdsourcing: Why the power of the crowd is driving the future of business. Crown Publishing Group.

Hutcheon, L. (2012). A theory of adaptation. Routledge.

Jarmolowicz, D. P., Bickel, W. K., Carter, A. E., Franck, C. T., & Mueller, E. T. (2012). Using crowdsourcing to examine relations between delay and probability discounting. Behavioural Processes, 91(3), 308-312.

Jarvenpaa, S., & Standaert, W. (2018). Digital probes as opening possibilities of generativity. Journal of the Association for Information Systems, 19(10), 982-1000.

Kane, G. C. (2011). A multimethod study of information quality in Wiki collaboration. ACM Transactions on Management Information Systems, 2(1), Article 4.

Kankanhalli, A., Lee, O. K. D., & Lim, K. H. (2011). Knowledge reuse through electronic repositories: A study in the context of customer service support. Information & Management, 48(2-3), 106-113.

Keegan, B., Gergle, D., & Contractor, N. (2013). Hot off the wiki: Structures and dynamics of Wikipedia’s coverage of breaking news events. American Behavioral Scientist, 57(5), 595-622.

Khan, L., Luo, F., & Yen, I. L. (2002). Automatic ontology derivation from documents. Proceedings of the 15<sup>th</sup> Conference on Advanced Information Systems Engineering.

Khatib, F., DiMaio, F., Cooper, S., Kazmierczyk, M., Gilski, M., Krzywda, S., Zabranska, H., Pichova, I., Thompson, J., Popović, Z., & Jaskolski, M. (2011). Crystal structure of a monomeric retroviral protease solved by protein folding game players. Nature Structural and Molecular Biology, 18(10), 1175.

Khedhaouria, A., & Jamal, A. (2015). Sourcing knowledge for innovation: knowledge reuse and creation in project teams. Journal of Knowledge Management, 19(5), 932-948.

Kittur, A., Nickerson, J. V., Bernstein, M., Gerber, E., Shaw, A., Zimmerman, J., Lease, M., & Horton, J. (2013). The future of crowd work. Proceedings of the 16<sup>th</sup> ACM Conference on Computer Supported Cooperative Work & Social Computing.

Kogut, B., & Zander, U. (1992). Knowledge of the firm, combinative capabilities, and the replication of technology. Organization Science, 3(3), 383-397.

Kristensson, P., Magnusson, P. R., & Matthing, J. (2002). Users as a hidden resource for creativity: Findings from an experimental study on user involvement. Creativity and Innovation Management, 11(1), 55-61.

Kyriakou, H., Nickerson, J. V., & Sabnis, G. (2017). Knowledge reuse for customization: metamodels in an open design community for 3D printing. MIS Quarterly, 41(1), 315-332.

Lessig, L. (2008). Remix: Making art and commerce thrive in the hybrid economy. Penguin.

Leonard, D., & Sensiper, S. (1998). The role of tacit knowledge in group innovation. California Management Review, 40(3), 112-132.

Leonardi, P. M. (2014). Social media, knowledge sharing, and innovation: Toward a theory of communication visibility. Information Systems Research, 25(4), 796-816.

Leong, C. M. L., Pan, S. L., Newell, S., & Cui, L. (2016). The emergence of self-organizing ecommerce ecosystems in remote villages of China: A tale of digital empowerment for rural development. MIS Quarterly, 40(2), 475-484.

Lim, W. C. (1994). Effects of reuse on quality, productivity, and economics. IEEE Software, 11(5), 23-30.

Majchrzak, A., Cooper, L. P., & Neece, O. E. (2004). Knowledge reuse for innovation. Management Science, 50(2), 174-188.

Majchrzak, A., & Malhotra, A. (2013). Towards an information systems perspective and research agenda on crowdsourcing for innovation. The Journal of Strategic Information Systems, 22(4), 257-268.

Majchrzak, A., Markus, M. L., & Wareham, J. (2016). Designing for digital transformation: Lessons for information systems research from the study of ICT and societal challenges. MIS Quarterly, 40(2), 267-277.

Malone, T. W., Laubacher, R., & Dellarocas, C. (2010). The collective intelligence genome. MIT Sloan Management Review, 51(3), 21-31.

Malone, T. W., Nickerson, J. V., Laubacher, R., Hesse Fisher, L., De Boer, P., Han, Y., & Towne, W. B. (2017). Putting the Pieces back together again: Contest webs for large-scale problem solving. Proceedings of the 20th ACM

Conference on Computer Supported Cooperative Work & Social Computing.

Malone, T. W. (2018). Superminds: the surprising power of people and computers thinking together. Little, Brown & Company.

Margolis, J. D., & Walsh, J. P. (2003). Misery loves companies: Rethinking social initiatives by business. Administrative Science Quarterly, 48(2), 268-305.

Mark, G., Lyytinen, K., & Bergman, M. (2007). Boundary objects in design: An ecological view of design artifacts. Journal of the Association for Information Systems, 8(11), 34.

Markus, L. M. (2001). Toward a theory of knowledge reuse: Types of knowledge reuse situations and factors in reuse success. Journal of Management Information Systems, 18(1), 57- 93.

Marom, D., Robb, A., & Sade, O. (2016). Gender dynamics in crowdfunding (Kickstarter): Evidence on entrepreneurs, investors, deals and taste-based discrimination. SSRN Electronic Journal. http://ssrn.com/abstract=2442954.

Mein Goh, J., Gao, G., & Agarwal, R. (2016). The creation of social value: Can an online health community reduce rural–urban health disparities? MIS Quarterly, 40(1), 247-263.

Merchant, R. M., Asch, D. A., Hershey, J. C., Griffis, H. M., Hill, S., Saynisch, O., Leung, A. C., Asch, J. M, Lozada, K., Nadkarni, L.D., Kilaru, A.S., Branas, C, Stone, E.M., Starr, L., Shofer, F, Nichol, G., & Becker, L.B. (2013). A crowdsourcing innovation challenge to locate and map automated external defibrillators. Circulation: Cardiovascular Quality and Outcomes, 6(2), 229-236.

Mergel, I., & Desouza, K. C. (2013). Implementing open innovation in the public sector: The case of Challenge. gov. Public Administration Review, 73(6), 882-890.

McGrath, F., & Parkes, C. (2007). Cognitive style fit and effective knowledge reuse. International Journal of Knowledge Management Studies, 1(3-4), 484-496.

Muller, C. L., Chapman, L., Johnston, S., Kidd, C., Illingworth, S., Foody, G., Overeem, A., & Leigh, R. R. (2015). Crowdsourcing for climate and atmospheric sciences: Current status and future potential. International Journal of Climatology, 35(11), 3185-3203.

Navas, E. (2012). Remix theory: The aesthetics of sampling. Springer.

Nickerson J. V. (2015) Collective Design: Remixing and Visibility. In: Gero J., & Hanna S. (Eds), Design Computing and Cognition ‘14 (pp. 263- 276). Springer.

Nicolini, D., Mengis, J., & Swan, J. (2012). Understanding the role of objects in crossdisciplinary collaboration. Organization Science, 23(3), 612-629.

Nonaka, I. (1994). A dynamic theory of organizational knowledge creation. Organization Science, 5(1), 14-37.

Paulini, M., Maher, M. L., & Murty, P. (2014). Motivating participation in online innovation communities. International Journal of Web Based Communities, 10(1), 94-114.

Phillips, J. (2010). Open innovation typology. International Journal of Innovation Science, 2(4), 175-183.

Resnick, M., Maloney, J., Monroy-Hernández, A., Rusk, N., Eastmond, E., Brennan, K., Silver, J., Silverman, B., & Kafai, Y. (2009). Scratch: programming for all. Communications of the ACM, 52(11), 60-67.

Rico, R., Sánchez-Manzanares, M., Gil, F., & Gibson, C. (2008). Team implicit coordination processes: A team knowledge-based approach. Academy of Management Review, 33(1), 163- 184.

Rittel, H. W., & Webber, M. M. (1973). Dilemmas in a general theory of planning. Policy Sciences, 4(2), 155-169.

Saxton, G. D., Oh, O., & Kishore, R. (2013). Rules of crowdsourcing: Models, issues, and systems of control. Information Systems Management, 30(1), 2-20.

Schenk, E., & Guittard, C. (2011). Towards a characterization of crowdsourcing practices. Journal of Innovation Economics & Management, (1), 93-107.

Scherer, A. G., & Palazzo, G. (2011). The new political role of business in a globalized world: A review of a new perspective on CSR and its implications for the firm, governance, and democracy. Journal of Management Studies, 48(4), 899-931.

Schlagwein, D., & Bjørn-Andersen, N. (2014). Organizational learning with crowdsourcing: The revelatory case of LEGO. Journal of the Association for Information Systems, 15(11), 754-778.

Siangliulue, P., Chan, J., Huber, B., Dow, S. P., & Gajos, K. Z. (2016). IdeaHound: Self-

sustainable Idea Generation in Creative Online Communities. Proceedings of the 19th ACM Conference on Computer Supported Cooperative Work & Social Computing.

Sojer, M., & Henkel, J. (2010). Code reuse in open source software development: Quantitative evidence, drivers, and impediments. Journal of the Association for Information Systems, 11(12), 868-901.

Srivastava, S. C., Teo, T. S., & Devaraj, S. (2016). You can't bribe a computer: Dealing with the societal challenge of corruption through ICT. MIS Quarterly, 40(2), 511-526.

Stanko, M. A. (2016). Toward a theory of remixing in online innovation communities. Information Systems Research, 27(4), 773-791.

Star, S. L., & Griesemer, J. R. (1989). Institutional ecology, translations' and boundary objects: Amateurs and professionals in Berkeley's Museum of Vertebrate Zoology, 1907-39. Social Studies of Science, 19(3), 387-420.

Szulanski, G. (2000). The process of knowledge transfer: A diachronic analysis of stickiness. Organizational Behavior and Human Decision Processes, 82(1), 9-27.

Vashistha, A., Vaish, R., Cutrell, E., & Thies, W. (2015). The whodunit challenge: Mobilizing the crowd in India. In J. Abascal, S. Barbosa, M. Fetter, T. Gross, P. Palanque, & M. Winckler (Eds.), Proceedings of Human-Computer Interaction.

Venkatesh, V., Rai, A., Sykes, T. A., & Aljafari, R. (2016). Combating infant mortality in rural India: Evidence from a field study of eHealth kiosk implementations. MIS Quarterly, 40(2), 353-380.

Vilarinho, T., Pappas, I. O., Mora, S., Dinant, I., Floch, J., Oliveira, M., & Jaccheri, L. (2018). Experimenting a digital collaborative platform for supporting social innovation in multiple settings. Proceedings of the International Conference on Innovations for Community Services.

Von Hippel, E., & von Krogh, G. (2003). Open source software and the “private-collective” innovation model: Issues for organization science. Organization Science, 14(2), 209-223.

Wang, J., Farooq, U., & Carroll, J. M. (2013). Does design rationale enhance creativity? In J. M. Carrol (Ed.), Creativity and rationale (pp. 197- 222). Springer.

Ward, T. B. (2001). Creative cognition, conceptual combination, and the creative writing of Stephen R. Donaldson. American Psychologist, 56(4), 350.

White House. (2009). Transparency and open government. https://obamawhitehouse. archives.gov/the-press-office/transparencyand-open-government.

Wikipedia: Size comparisons. (2019). Wikipedia. https://en.wikipedia.org/wiki/Wikipedia:Size\_ comparisons.

Wisdom, T. N., & Goldstone, R. L. (2011). Innovation, imitation, and problem solving in a networked group. Nonlinear Dynamics-Psychology and Life Sciences, 15(2), 229.

Yu, J., Thom, J. A., & Tam, A. (2007). Ontology evaluation using Wikipedia categories for browsing. Proceedings of the Sixteenth ACM Conference on Information and Knowledge Management.

Zhang, C., Hahn, J., & De, P. (2013). Research note— Continued participation in online innovation communities: Does community response matter equally for everyone? Information Systems Research, 24(4), 1112-1130.

Zhang, W., & Watts, S. A. (2008). Capitalizing on content: Information adoption in two online communities. Journal of the Association for Information Systems, 9(2), 73-94.

Zouaq, A., Gasevic, D., & Hatala, M. (2011). Towards open ontology learning and filtering. Information Systems, 36(7), 1064-1081.

## Appendix

Table A1. Existing Usage of Crowdsourcing to Address Societal Challenges

<table><tr><td>Methods</td><td>Pros</td><td>Cons</td><td>Example paper</td><td>Societal challenge and context</td></tr><tr><td rowspan="2">Crowdsourcing in the form of a web-enabled open call</td><td rowspan="2">Enables deeper levels of public participation; harnesses collective intelligence and creative solutions with nonexpert knowledge; low cost.</td><td rowspan="2">Challenges in sustaining of the online community; harder to motivate nonlocal participants; risk of low-quality individual entries.</td><td>Brabham, 2009</td><td>Urban planning and sustainability</td></tr><tr><td>Jarmolowicz et al., 2012</td><td>Health—smoking cessation</td></tr><tr><td rowspan="2">Crowdsourcing in the form of web-enabled contests and competitions</td><td rowspan="2">Active citizen participation; contributes to the advancement of democracy and the validity of public institutions.</td><td rowspan="2">Unclear goal definition leads to failure in generating desired solutions; challenges in collaboration; redundancy in ideas.</td><td>Mergel &amp; Desouza, 2013</td><td>Governmental challenges (e.g., science and technology, health, international relations, etc.)</td></tr><tr><td>Vilarinho et al., 2018</td><td>Social innovation in multiple settings</td></tr><tr><td rowspan="2">Crowdsourcing in the form of mobile-enabled tournament</td><td rowspan="2">Low monetary and time cost; high mobility; high diversity.</td><td rowspan="2">Labor intensive quality control; high solution validation time; low scalability.</td><td>Merchant et. al, 2013</td><td>Health—mapping of automated external defibrillators</td></tr><tr><td>Vashistha et al., 2015</td><td>Social mobilization in developing countries</td></tr><tr><td rowspan="2">Crowdsourcing in the form of crowdfunding</td><td rowspan="2">Leverages the internet and social network to reach out to an undefined large number of potential investors.</td><td rowspan="2">Limited to monetary contribution.</td><td>Marom, Robb &amp; Sade, 2016</td><td>Gender equality and female entrepreneurship</td></tr><tr><td>Gossel, Brüntje, &amp; Will, 2016</td><td>Financial crisis</td></tr><tr><td>Crowdsourcing in the form of remixing</td><td>Promotes crowd collaboration; allows task division and integration; deepens domain knowledge and generates comprehensive solutions.</td><td>Tech difficulty in platform construction; limited support for encouraging reusability</td><td>Malone et al. 2017</td><td>Global climate change</td></tr></table>

Table A2. Correlation Table of All Variables

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td></tr><tr><td>1. Generativity</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2. Integration metaknowledge</td><td>0.40*</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>3. Number of high-quality proposals reused</td><td>0.19</td><td>0.60*</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>4. Proposal topic prevalence</td><td>0.66*</td><td>0.37*</td><td>0.40*</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>5. Number of contributors</td><td>-0.06</td><td>0.03</td><td>0.23</td><td>-0.03</td><td>1</td><td></td><td></td><td></td></tr><tr><td>6. Sequence of proposal creation</td><td>-0.27</td><td>-0.05</td><td>-0.15</td><td>-0.35*</td><td>-0.01</td><td>1</td><td></td><td></td></tr><tr><td>7. Proposal owner&#x27;s tenure</td><td>0.53*</td><td>0.32*</td><td>0.25</td><td>0.28</td><td>-0.17</td><td>-0.16</td><td>1</td><td></td></tr><tr><td>8. Owner network control</td><td>0.24</td><td>-0.01</td><td>-0.01</td><td>0.21</td><td>-0.25</td><td>-0.22</td><td>0.37*</td><td>1</td></tr><tr><td colspan="9">Note: ***p&lt;0.001, **p&lt;0.01, *p&lt;0.05</td></tr></table>

Table A3. Multicollinearity Check

<table><tr><td>Variable</td><td>VIF</td><td>1/VIF</td></tr><tr><td>Number of contributors</td><td>1.34</td><td>0.749</td></tr><tr><td>Sequence of proposal creation</td><td>1.70</td><td>0.587</td></tr><tr><td>Proposal owner&#x27;s tenure</td><td>1.45</td><td>0.691</td></tr><tr><td>Owner network control</td><td>1.48</td><td>0.674</td></tr><tr><td>Proposal topic prevalence</td><td>2.19</td><td>0.456</td></tr><tr><td>Number of high-quality proposals reused</td><td>17.12</td><td>0.058</td></tr><tr><td>Number of high-quality proposals reused (squared)</td><td>15.05</td><td>0.066</td></tr><tr><td>Integration metaknowledge</td><td>2.14</td><td>0.468</td></tr><tr><td colspan="3">Contest</td></tr><tr><td>1302007</td><td>1.67</td><td>0.598</td></tr><tr><td>1302013</td><td>1.88</td><td>0.532</td></tr><tr><td>1302019</td><td>2.28</td><td>0.440</td></tr><tr><td>1302025</td><td>1.49</td><td>0.672</td></tr><tr><td>1302031</td><td>1.87</td><td>0.534</td></tr><tr><td>Mean VIF</td><td>3.97</td><td></td></tr></table>

## About the Authors

Yue Han is an assistant professor of information systems in the Madden School of Business at Le Moyne College. She holds a PhD degree in Business administration with a concentration in information systems and analytics, and a master’s degree in project management from Stevens Institute of Technology. Her research primarily focuses on collective intelligence and crowd innovation, online collaborations, and information diffusion on social media platforms.

Pinar Ozturk is an assistant professor of information systems management in the Palumbo-Donahue School of Business at Duquesne University. She holds a PhD in business administration from Stevens Institute of Technology, and an MBA and an MEng in electrical engineering from University of Hartford, CT. Her research interests include collective computer-supported cooperative work, collective intelligence, crowdsourcing, and online collaborations. Specifically, she focuses on understanding the origins and dynamics of collective group behavior on mass collaboration systems and social media platforms.

Jeffrey V. Nickerson is a professor in the School of Business at Stevens Institute of Technology. His research is focused on collective creativity: how teams, online communities, and crowds produce new knowledge. He is currently investigating how systems composed of humans and machines explore the space of potential designs for 3D objects, encyclopedia articles, skills, occupations, and policies.

Copyright © 2020 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
