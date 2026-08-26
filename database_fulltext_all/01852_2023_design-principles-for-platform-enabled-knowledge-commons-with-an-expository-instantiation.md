---
otero_id: 1852
otero_key: "PXRJ7YYC"
title: "Design Principles for Platform-Enabled Knowledge Commons with an Expository Instantiation"
authors: "Muralidharan Ramakrishnan; ; Shirley Gregor; Anup Shrestha; Jeffrey Soar"
year: "2023"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00824"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Volume 24 Issue 5 Special Issue: Technology and Social Inclusion (pp. 1199-1357)

Article 1

2023

# Design Principles for Platform-Enabled Knowledge Commons with an Expository Instantiation

Muralidharan Ramakrishnan , Muralidharan.Ramakrishnan@usq.edu.au

Shirley Gregor , shirley.gregor@anu.edu.au

Anup Shrestha , Anup.Shrestha@usq.edu.au

Jeffrey Soar , jeffrey.soar@usq.edu.au

Follow this and additional works at: https://aisel.aisnet.org/jais

ISSN 1536-9323

# Design Principles for Platform-Enabled Knowledge Commons with an Expository Instantiation

Muralidharan Ramakrishnan,<sup>1</sup> Shirley Gregor,<sup>2</sup> Anup Shrestha,<sup>3</sup> Jeffrey Soar<sup>4</sup>

<sup>1</sup>School of Business, University of Southern Queensland, Australia, muralidharan.ramakrishnan@usq.edu.au <sup>2</sup>Research School of Management, The Australian National University, Australia, shirley.gregor@anu.edu.au

<sup>3</sup>School of Business, University of Southern Queensland, Australia, anup.shrestha@usq.edu.au <sup>4</sup>School of Business, University of Southern Queensland, Australia, jeffrey.soar@usq.edu.au

## Abstract

Knowledge commons play a pivotal role in knowledge creation and sharing in the digital economy. The motivation for this research was the opportunity to develop a knowledge commons for IT service management (ITSM) practitioners. To obtain guidance to design the knowledge commons, we critically reviewed commons design principles (DPs) that were based on a well-established economics theory. We observed that the commons DPs had significant gaps when applied to IS practice. Hence, we developed an alternate set of DPs that we refer to as platform-enabled knowledge commons (PEKC) DPs that are relevant to IS practice. This paper discusses the development of PEKC DPs and applies them in instantiating an IS artifact, Service-Symphony. Service-Symphony is a purpose-built, public-facing knowledge repository developed for the benefit of ITSM practitioners and students. Our research followed the design science research (DSR) paradigm and contributes to the body of knowledge by establishing a multigrounded design theory comprising meta-requirements and DPs. To bridge theory and practice, we assessed the reusability of PEKC DPs through focus group interviews with IS architects. Our case study illustrates the complete life cycle of DPs covering conceptualization, initial formulation, iterative refinement, application to an important real-world instantiation, and evaluation by a group of independent IS practitioners.

Keywords: Knowledge Commons, IS Knowledge Platform, Design Principles, Platform-Enabled Knowledge Commons, Design Science Research

Jan Pries-Heje was the accepting senior editor. This research article was submitted on March 25, 2021 and underwent three revisions. Muralidharan Ramakrishnan is the corresponding author.

## 1 Introduction

Knowledge commons play a pivotal role in the digital economy by facilitating knowledge collaboration within and across communities (Frischmann et al., 2014; Hess & Ostrom, 2007; Potts, 2022). There are several types of knowledge commons including open-source software, social media, and wikis (Mindel et al., 2018). These diverse applications of knowledge commons can provide significant value to stakeholders in different ways, ranging from individual benefits to global benefits such as disaster management (Comfort & Okada, 2013;

McNaughton & Rao, 2017) and mitigating pandemics including COVID-19 (Hensher et al., 2020).

Our research developed a purpose-built, public-facing knowledge commons for IT service management (ITSM). ITSM is a practice that encompasses diverse process frameworks such as IT governance, strategy, operations, project management, quality management, service improvement and related practices (Cater-Steel et al., 2006; Ekanata & Girsang, 2017; Veronica & Suryawan, 2017) that are intended to enable IT organizations co-create value within the business (Cronholm et al., 2020; Wilkin et al., 2013; Winkler &

Wulf, 2019). The knowledge commons we developed is referred to as Service-Symphony in this paper. Our target community for Service-Symphony comprises ITSM practitioners and students who study ITSM courses in higher education institutions. The objective of Service-Symphony is to help the target community comprehend the rapidly changing ITSM knowledge ecosystem.

A substantial body of research analyzes the technical design of knowledge platforms from different perspectives including affordances (Gaver, 1991; McLoughlin & Lee, 2007; Yeo & Arazy, 2012), user interfaces (Lamberti & Wallace, 1990; Reinecke & Bernstein, 2013; Vance et al., 2015), and information security (Roumani & Nwankpa, 2020). However, technical design is only one aspect of designing knowledge commons. There are social aspects that need to be considered to ensure that the knowledge commons provide value to the target community in a sustainable manner.

Our research aims to bridge the social and technological aspects of a knowledge platform design by adapting commons theory. Commons theory is a prominent economic theory that analyzes the sustainability of sharing natural resources such as rivers, forests, and fisheries (Ostrom, 1990). Knowledge commons is a subset of commons theory that considers knowledge as a shareable resource (Hess & Ostrom, 2007). As part of a wider research project, we conducted a systematic literature survey and found that knowledge commons research encompasses a broad scope covering intellectual property, knowledge cities, industrial commons, academic commons, open source systems, and learning commons (Ramakrishnan et al., 2021). This survey found that the role of IS platforms was not prominent in knowledge commons applications. Hence, in the current research, we focused on a problem we had encountered in information systems (IS) practice, namely the development of platform-enabled knowledge commons (PEKC). PEKC is a subset of knowledge commons where knowledge creation and consumption are facilitated by an IS knowledge platform.

One of the contributions of commons theory was the development of design principles (DPs) that codified the characteristics of successful commons (Hess & Ostrom, 2007). In the IS discipline, the formulation of DPs is one of the salient contributions in conveying design knowledge (Chandra et al., 2015; Cronholm & Göbel, 2018; Gregor et al., 2020). The purpose of DPs is to guide the design of different instances of IS artifacts that belong to the same type or class (Iivari et al., 2021). Commons DPs have been applied in the extant research to analyze existing IS platforms such as Wikipedia (Forte et al., 2009; Safner, 2016; Viégas et al., 2007). While the extant research provides a starting point, prior studies are not fully relevant and accessible to IS practice. As the commons DPs were developed in the context of natural resources, we argue that to be relevant to IS practice there are additional DPs required and the terminology of the DPs should be tailored to suit IS practitioners. We aimed at redefining the commons DPs to be accessible to IS practitioners. Accessibility is defined as “the degree to which members of the target community can understand and comprehend the set of design principles and whether they are individually and collectively intelligible” (Iivari et al., 2021, p. 292). In this research, we considered the research question:

RQ: What are the design principles that will provide guidance to IS practitioners when developing a PEKC ?

Our research follows the design science research (DSR) paradigm (Baskerville et al., 2018; Hevner et al., 2004), which is ideally suited for research that focuses on developing IS artifacts (Gregor & Hevner, 2013). We contribute to DSR knowledge by deriving and applying IS-specific DPs that capture the “know-how” aspect of building the IS artifact (Gregor et al., 2020; Gregor & Hevner, 2013). The DPs are considered a key part of design theory (Baskerville et al., 2018; Gregor et al., 2020; Gregor & Jones, 2007; Gregor et al., 2013). The application of the DPs was demonstrated in an instantiation and evaluated by target practitioners to ensure that they could potentially find them useful for creating other solution instances (Iivari et al., 2018; Iivari et al., 2021).

The remainder of the paper unfolds as follows. The background of ITSM practice and commons theory is discussed in the next section. The research methods section explains the adaption of DSR steps to suit this research. The remaining sections are aligned with the research steps of design, artifact evaluation, DP evaluation, and discussion.

## 2 Background and Related Literature

This research successfully developed and launched Service-Symphony for the benefit of ITSM practitioners and students in February 2019. ITSM is a practice that describes a customer-centric approach to managing IT services (Taylor, 2007). Service-Symphony serves as a portal for different practitioner communities to obtain a trusted view of state-of-the-art best practices.

Ramakrishnan et al. (2018) proposed a model for the ITSM knowledge ecosystem comprising process frameworks, tools, and skills. The model provides a holistic view of knowledge for different stakeholder communities. Since the ecosystem consists of many independent knowledge artifacts, it is a challenge to keep abreast of changes, as each knowledge community has its own release cycles. Figure 1 shows the release cycles of key frameworks within the date range of the years 2000-2020 that are relevant to ITSM.

![](/api/attachments/PXRJ7YYC/fulltext/images/aa5422a1b9163ea47940b87ae48e7090d58d0110c2ceec1fe6845f5245e7678a.jpg)  
Figure 1. Release Cycles of Process Reference Frameworks Relevant to ITSM (Ramakrishnan et al., 2020)

The release cycles of frameworks are independent of each other, and some frameworks are aperiodic. For example, between the years 2018 and 2020, three related ITSM frameworks—ISO/IEC 20000, COBIT 2019, and ITIL 4 were released. Although ITSM practices add value to businesses (Shrestha et al., 2020), organizations are often required to implement more than one process framework (Cater-Steel et al., 2006). However, the existence of multiple process frameworks can cause confusion, inefficiency, and ineffectiveness (Heston & Phifer, 2011). Without the aid of a holistic knowledge repository, it is effort intensive to study the impact of new releases and the relationship between the releases within an organization.

Another challenge in the ITSM knowledge ecosystem is monitoring emerging best practices (Shrestha et al., 2016). For example, interest in DevOps practice (Ebert et al., 2016) has steadily grown over the years. While there are industry forums and other platforms that can provide a view of emerging trends, the knowledge is often specific to one or two specific interest groups. For example, the DevOps community might discuss specific technologies and practices about DevOps rather than offering a holistic view across the broader IT practices. Service-Symphony is intended to address this gap by providing a current view of emerging best practices across the entire ITSM ecosystem.

In sum, in the ITSM ecosystem, there were no existing knowledge commons that provided the required holistic view. Before embarking on the Service-Symphony development, this view was validated in discussions with industry experts, academia, and professional bodies. After the launch of the portal, the positive feedback received from practitioner and student communities reinforced the relevance of having such a knowledge portal.

## 2.1 Overview of Commons Theory

For guidance in designing and developing Service-Symphony, we reviewed the management and IS literature. Commons theory, which was developed by Elinor Ostrom (Ostrom, 1990, 2008; Ostrom et al.,

1994), was found to be a good fit, as it was a credible economic theory and has been applied to comparable knowledge platforms such as Wikipedia.

The term commons describes the institutional arrangement of managing a resource shared by a group of people who are subject to social dilemmas (Frischmann et al., 2014; Ostrom, 1990). Hardin (1968) introduced the term commons in academic research through his article on the tragedy of commons. Hardin (1968) explained the tragedy by arguing that in an open pasture, each herder will try to keep as many cattle as possible to maximize the economic return which will, in turn, lead to the deterioration of the pasture. However, Ostrom (1990) observed that there are many successful commons models based on mutual trust between the participating actors that use the commons. The body of work Ostrom has produced was acknowledged as one that “contributes to some of the most important questions of the twenty-first century” (Wall, 2014, p. 3), and she was awarded the Nobel prize for her analysis of economic governance, especially of commons, in 2009. Ostrom’s commons theory is underpinned by the principles of self-governance, collaboration, and collective action.

During the latter part of Ostrom’s career, she collaborated with another researcher, Charlotte Hess, and extended the application of the natural commons model to knowledge. Hess and Ostrom (2007, p. 21) observed that knowledge commons is an exciting field that enables us to “creatively design new systems that tap into the limitless capabilities of digital information technologies.” Knowledge commons theory has been applied to a wide range of overlapping practices including but not limited to public policy, intellectual property rights, legal studies, and innovation (Albagli et al., 2018; Allen & Potts, 2016; Frischmann et al., 2014; Rathwell et al., 2015).

In IS practice, the application of knowledge commons theory has been mostly confined to analyzing Wikipedia or similar knowledge platforms (Forte et al., 2009; Safner, 2016; Viégas et al., 2007). A noted exception is the research paper by Mindel et al. (2018), which unifies the tragedy of the commons and Ostrom’s theory to design a polycentric information commons. The polycentric information commons is a conceptual framework balancing collaboration and self-centric human behaviors to develop a sustainable implementation of information commons. The conceptual model, however, was not extended to develop DPs.

One of the contributions of Ostrom’s research is the development of eight DPs. The DPs emphasize factors that exist in most robust commons governance organizations and are absent in failed systems (Ostrom, 1990). IS researchers have applied Ostrom’s DPs to study the success of the online knowledge collaboration platform, Wikipedia. Viégas et al. (2007) applied four of the eight DPs in analyzing Wikipedia’s featured article (FA) process. Their research found that Principles 2, 3, 4, and 6 are applicable in the Wikipedia process. In subsequent research, Forte et al. (2009) analyzed the remaining DPs: 1, 5, 7,8. Studies by Safner (2016), Dourado and Tabarrok (2015) argued that all eight commons DPs apply to Wikipedia. Figure 2 shows a summary of how our research fits within the commons research landscape.

We found three major gaps in the extant research on the application of commons DPs.

The extant research is limited to examining whether commons DPs can be observed in IS platforms once constructed. This approach does not necessarily reveal additional DPs that may have been introduced by designers.

The extant research uses the concepts and terminology from commons theory, without any modification that would assist IS practitioners in embracing the DPs

• Commons DPs have not been formally evaluated by IS practitioners to demonstrate the practical significance of the DPs

This research addresses the identified limitations by:

• Systematically analyzing the characteristics of knowledge to propose additional DPs that are not covered in commons DPs

Examining the commons DP concepts and terminology and tailoring the principles to suit IS practitioners

• Applying the proposed expanded set of DPs to instantiate Service-Symphony

• Evaluating the DPs from the perspective of practitioners.

![](/api/attachments/PXRJ7YYC/fulltext/images/0549065e699ff625f8ee9041e7ded67d73a7ff373032b48f955064b62547bf58.jpg)  
Figure 2. Positioning of PEKC within the commons research landscape

## 3 Research Methods

This research followed the DSR paradigm. DSR is a research paradigm that addresses the relevance versus rigor gap in IS research by delivering useful artifacts and design theories to IS research (Baskerville et al., 2018; Hevner et al., 2004). DSR involves two primary activities: (1) the creation of new knowledge through the design of novel or innovative artifacts and (2) the analysis of the artifact’s use and/or performance (Vaishnavi & Kuechler, 2015).

This research broadly followed a six-step approach, comprising (1) problem identification and motivation, (2) objectives of a solution, (3) design and development, (4) demonstration, (5) evaluation, and (6) communication, as in Peffers et al. (2007) with some adaptations. Figure 3 shows the adaptation of the six-step approach.

First, we established that there is a problem in the ITSM industry practice (Box 1). To design a product, a set of meta-requirements (MRs) that describe the class of goals is required (Walls et al., 2004). The objectives of the solution were translated as MRs (Box 2). Before designing the artifact, we scanned the literature to find out whether there were any existing DPs that could be leveraged in the development of the artifact (Box 3a). Our scan led to the commons DPs as a starting point for the artifact design. However, while developing the artifact iteratively we found that the commons DPs were too generic to be relevant for IS practice. Hence the artifact development and DPs refinement were carried out in parallel in an iterative manner, i.e., IS development feeding to the refinement of DPs and the DPs driving the IS development features. We followed Agile development, which combines the development and demonstration phases (Conboy et al., 2015). These iterative development and demonstration steps are described in Box 3b, 3c, and 4. We carried out the development in fortnightly sprints that followed a demonstration to an expert panel. The reusability evaluation of the DPs (Box 5a) and the evaluation of Service-Symphony (Box 5b) were carried out in the next steps. The communication of the artifact was achieved through academic publications and industry presentations, as shown in Box 6. The following sections describe each step in detail.

![](/api/attachments/PXRJ7YYC/fulltext/images/45aca1f97b084dd57a56607b2bcec50a151b6bc499c25c8c272869c717658bc4.jpg)  
Figure 3. Research Approach Adapted from Peffers et al. (2007)

## 3.1 Identify Problems and Motivate

The motivation for the research came primarily from discussions with industry practitioners and academics teaching ITSM courses. The researchers engaged with practitioners through the IT Service Management Forum (ITSMF), which is a membership-based global ITSM practitioner community. ITSMF conducts a range of industry engagement activities, and these activities are managed nationally by country-specific ITSMF bodies. One of the researchers was active in ITSMF Australia and regularly attended face-to-face seminars. The researcher observed the problem of the changing landscape of process, technology, and skills within ITSM practice and the opportunity to develop a holistic knowledge platform. This opportunity was validated by conducting a systematic literature review (SLR) to demonstrate how comprehending the complexity of multiple process frameworks is addressed in the research landscape (Ramakrishnan et al., 2018) The industry inputs and literature review supported the view that the problem could be addressed through a holistic knowledge repository.

## 3.2 Define the Objectives of the Solution through MRs

MRs describe the goals that are addressed in the class of problems (Kuechler & Vaishnavi, 2012; Walls et al., 2004; Walls et al., 1992). MRs and DPs are essential components of a design theory (Gregor & Jones, 2007; Walls et al., 1992). Goldkuhl (2004) proposed that a good design theory should be grounded in multiple dimensions. These dimensions are an internal dimension, an external theoretical dimension, and an empirical dimension (Goldkuhl, 2004). Internal grounding implies the grounding of a design theory in its own specific background knowledge. The external theoretical grounding describes how the proposed design theory relates to other external theories. External theoretical grounding is also supported by Baskerville et al. (2018). The empirical grounding addresses how the design knowledge is practically relevant to the user community.

In this research, the internal grounding is demonstrated by deriving the MRs from the knowledge of ITSM practitioners. The commons theory served as a basis for external theoretical grounding. The evaluation of the artifact and reusability evaluation of the DPs contributed to the empirical grounding of the design theory.

MRs were identified by understanding stakeholder needs (Lins et al., 2019) and synthesizing literature from the relevant domain (Haj-Bolouri et al., 2020). One of the authors initially discussed the idea of developing a knowledge repository for ITSM knowledge with the ITSMF Australia stakeholders. The initial reaction was positive. Some of the questions that were raised by the practitioners were: “How is your repository going to be different from the ITIL online books?” “How do you keep the repository up to date?” and “How can we trust the knowledge in the repository?” These questions underpinned the objectives of the knowledge repository and formed a base for meta-requirements.

Since Service-Symphony development aimed at being public domain and serving a large audience, we formed an expert panel to represent the community. The expert panel served as a mechanism for bouncing around ideas and refining the requirements. The five panel members were experts with over 20 years of experience each and participated voluntarily. The panel members guided the artifact development by suggesting improvements in the usability design, reviewing knowledge, and mediating conflict resolution. The composition of the panel members is given in Table 1.

The first MR directly addresses the relevance aspect of DSR. One of the primary objectives of DSR is to develop IS artifacts that are relevant to the user community (Hevner, 2007; Wieringa, 2010). We captured “user stories” from different stakeholders’ perspectives and consolidated these stories as an MR. A user story is a method of requirements elicitation in Agile development that captures the needs of different users (Amorim et al., 2021; Dalpiaz & Brinkkemper, 2018; Kannan et al., 2019)

A user story is often written in the format “As a [type of user], I want [some goal] so that [some reason].” (Dalpiaz & Brinkkemper, 2018; Kannan et al., 2019). Based on this format, we developed the following user stories:

“As an ITSM practitioner, I want to understand the current ITSM processes so that I can apply them at my workplace”

“As an ITSM practitioner, I want to understand the complementary processes so that I can expand my career options”

“As an ITSM student, I want to understand current ITSM practices that are relevant to my course and complete my academic assignment”

PEKC was aimed at hosting a wide range of process frameworks, tools, and skills with a diverse user base. It was a challenge to remain relevant to a critical mass of users in a fast-changing environment. Ensuring that outcomes are fair and relevant to stakeholders is one of the core principles of commons theory and is referred to as congruence (Hess & Ostrom, 2007; Ostrom, 1990). The first MR aligns with this usage.

MR1—Stakeholder congruence: The PEKC instance design should be congruent with the needs of diverse stakeholder communities.

Table 1. Expert Panel Composition

<table><tr><td>Member</td><td>Member profile</td></tr><tr><td>M1</td><td>A freelance senior consultant specializing in ITSM, DevOps, and Governance. The consultant was recognised by the professional community for their contributions to practice.</td></tr><tr><td>M2</td><td>Chief information officer of a government organization with an interest in governance, service management, and usability</td></tr><tr><td>M3</td><td>A senior consultant from the private sector. This member held a PhD in IT service management and had a full-time teaching position.</td></tr><tr><td>M4, M5</td><td>Two members were nominated by the IT Service Management Forum (ITSMF), Australia.</td></tr></table>

Another MR was formulated after a literature review and internal reflection. PEKC must stay relevant over an extended period to provide value to the user community. Mindel et al. (2018) introduced the concept of sustainability in knowledge platform design. Sustainability is the capacity of the knowledge commons to continually provide value to stakeholders (Mindel et al., 2018). The sustainability concept is supported by the constructs of provision, appropriation, revitalization, and equitability (Mindel et al., 2018). The following user stories reflect the intent of sustainability:

As PEKC developers, we want Service-Symphony to be sustainable for at least for 5 years so that our research makes a tangible impact on the professional community.

As ITSM practitioners we want Service-Symphony to be sustainable for at least 5 years so that we have continuity in our knowledge gathering.

As ITSM students we want Service-Symphony to be sustainable for at least 5 years so that we can tap into the industry knowledge after we graduate.

One of the fundamental drivers of Ostrom’s contribution is to provide a counterargument to Hardin’s tragedy of commons, which hypothesizes that a common resource pool management is not sustainable (Ostrom, 1999). Ostrom showed that there is evidence of successful commons and they are sustainable through participative community arrangements. Hardin’s theory speculates that the resource would be depleted and not sustainable because of overconsumption. In contrast, Ostrom demonstrated that participative management contributed to the sustainability of the resources as the community contributes to replenishing the depleted resources. The sustainability aspect of the design is captured in MR2.

MR2—Artifact sustainability: The PEKC instance is designed to be sustainable for the desired period.

The trustworthiness of PEKC was one of the concerns flagged by the practitioners. Any information that is available online can be easily manipulated, which raises the question of trustworthiness (Cheshire, 2011; Pan & Chiou, 2011). Kittur et al. (2008, p. 477) ask a rhetorical question “Can you ever trust a wiki?,” noting that peer editing of Wikipedia leads “many to distrust it as a source of reliable information.” On the other hand, a study points out that one third of higher education students have used Wikipedia for academic purposes (Lim, 2009). The study notes that the frequency of Wikipedia usage is higher than that of the University’s library database. The dimensions of accuracy, stability, and validity can be used to assess the information’s trustworthiness (Huang et al., 2016). In addition to the information content, the user observes various credibility cues to assess trustworthiness. The credibility cues can be the way the information is presented, the reputation of the author, links to other references, and feedback from readers. The perceived importance of the credibility cues varies according to individual motivation and other factors (Machackova & Smahel, 2018). The following user stories articulate the requirements related to trustworthiness:

As ITSM practitioners, we want the PEKC knowledge to be trustworthy, without any commercial biases, so that we can use the information without compromising our integrity.

As ITSM students, we want to trust PEKC knowledge so that we can use the information in our academic assignments.

Trust is one of the key aspects of commons theory. The participative governance principles are underpinned by the mutual trust of the members within the community. To support the design of a PEKC that is trustworthy, the following MR is introduced.

MR3—Community trustworthiness: The PEKC instance should be considered trustworthy by the target communities.

The three MRs captured the objectives of the solution. The next section describes the design phase. Figure 4 visually represents the approach to developing MRs.

![](/api/attachments/PXRJ7YYC/fulltext/images/719330a4a71c93e8deedda3950b14ce95b9d6848e69f29e41e54bdf494132f72.jpg)  
Figure 4. Meta-Requirements Development Approach

![](/api/attachments/PXRJ7YYC/fulltext/images/964739c564b02528a99bebdf15c008d056805da5a5efd5e023bc880e7150bf65.jpg)  
Figure 5. Derivation and Application of PEKC DPs

## 3.3 Identify Generic DPs

Commons theory proposes eight DPs to analyze commons ecosystems, which are primarily intended to govern natural resources. While not all DPs are mandatory, at least some DPs are required to implement a successful, long-lived commons ecosystem (Dourado & Tabarrok, 2015). Though we used commons theory as a starting point, the commons DPs were generic and did not consider IS-specific aspects. We iteratively refined the commons DPs to suit IS while developing the IS artifact.

## 3.4 Develop IS-Specific DPs

To apply the DPs to PEKC, we followed a three-step analytical approach. In the first step, the differences between natural resources and knowledge were examined. The first step identified key attributes that were critical to analyzing the DPs in the second step, in which each DP was examined closely to consider whether it applied to PEKC. The third step applied PEKC DPs to Service-Symphony. In this last step, we evaluated whether a DP was relevant for the specific

PEKC and how the relevant principles could be applied. The three-step approach is presented in Figure 5 above.

The first step in the derivation process was to compare the characteristic attributes of natural resources and knowledge. Though many attributes can be compared between natural commons and PEKC, we identified four core attributes, namely creation, exclusion, subtractability, and revitalization (Hess & Ostrom, 2007; Ostrom, 1990). Each of the four attributes is discussed further below.

A knowledge resource must be created, as opposed to a natural resource that already exists in the environment (Frischmann et al., 2014). While the creation attribute may be self-evident, knowledge creation had to be explicitly considered to analyze the DPs as it differentiates the design of PEKC from other types of commons.

Commons theory considers two key attributes, namely exclusion and subtractability, to classify goods (Hess & Ostrom, 2007; Ostrom, 1990). The attribute of exclusion refers to the difficulty in restricting people who use the goods. For example, there could be physical fencing to restrict the use of a common herding pasture. Goods where individuals can be excluded from use are considered private goods, as opposed to public goods which are available to all. If one person’s use is subtracted from the available goods for others, the goods are said to be subtractable (Hess & Ostrom, 2007; Ostrom, 1990). Many natural commons like fisheries and forestry have subtractable resources, as consumption depletes the resource.

The attributes of exclusion and subtractability are relevant to PEKC, as these attributes can be artificially imposed through the design. We note that: (1) the PEKC can be designed for varying degrees of exclusion and subtractability, and (2) a single PEKC can have different combinations of exclusion and subtractability. For example, consider an online news platform. The headline news can be read by anyone without depleting the knowledge resource availability (no-exclusion / no-subtractability). The news platform can implement subscription-based access to access the premium content, thereby excluding nonsubscribers but still not depleting the knowledge resources (exclusion / no-subtractability). The subtractability attribute is implemented through a quota system. For example, the news platform can limit the number of free articles accessed by any user. There are no exclusions in this scenario, as anyone can access the content, but subtractability is implemented by restricting the number of accessed articles (noexclusion / subtractability). In this scenario, though the available articles are not depleted, from the consumption perspective, there is a depletion of articles with every access. Finally, if we consider a scenario where the news platform targets students and offers free access to premium content, which is limited by quota, the resultant model would fit into the exclusion-subtractability quadrant. Table 2 shows the different combinations of the exclusion and subtractability attributes in a single PEKC.

The attribute of revitalization is used to describe the difference between new active users and disengaged users (Mindel et al., 2018). The revitalization attribute is aligned with Rose’s (1986) “comedy of commons” argument. According to the comedy of commons, public properties will thrive only if there is patronage—in contrast to the tragedy of commons, which is only concerned only about depletion through overuse. Table 3 summarises the differences between natural commons and PEKC.

In the second step of the derivation process, each commons DPs (Ostrom, 1990) was analyzed considering the differences in attributes. The commons DPs do not address the attributes of creation and revitalization explicitly. To support creation and revitalization we introduce two additional DPs, i.e., DP9 and DP10, which address improving visibility to target communities and providing incentives to create and consume knowledge. Table 4 shows a summary of the PEKC DPs and their alignment with influencing attributes and MRs.

The following section presents the details of the derivation of the PEKC DPs.

PEKC\_DP1—Define broad knowledge boundaries: Commons DP1 proposes that the boundaries of the natural commons must be well-defined. Ostrom (1990) cites the case of the Torbel Community in Switzerland, a village of about 600 people. Written legal documents referring to the Torbel Community, dating back to 1224, define clear boundaries. The documents mention the type of properties, such as the alpine grazing meadows, forests, wastelands, and irrigation systems. Further, they also clearly articulate the paths and roads that connect the properties.

For knowledge resources, there are no naturally defined boundaries that regulate user access. Frischmann et al. (2014) pointed out that the boundaries for knowledge commons are built rather than found. As knowledge resources evolve, the boundaries will also correspondingly expand or contract. While we acknowledge that boundaries are important in PEKC, they need not be as clearly defined as in the case of natural commons. The boundaries can be broad and flexible. Hence, we tailored the DP to “Define broad knowledge boundaries.” This DP is influenced by the attribute of creation. One of the primary objectives of defining knowledge boundaries is to align the knowledge with diverse stakeholder expectations. Hence DP1 is aligned with MR1, stakeholder congruence.

PEKC\_DP2—Control participant access to the platform to enable the provision of tiered benefits: Commons DP2 addresses the distribution of benefits from appropriation rules. Ostrom (1990) uses the term “appropriation” to describe the process of withdrawing resource units from a resource system. For example, “appropriator” can be a generic term to describe communities such as herders, fishers, irrigators, and commuters. This DP is intended to impose a fair sharing of benefits. Appropriation is applicable in some types of PEKC that can impose appropriation through mechanisms such as tiered membership levels, subscriptions, and geographical access restrictions. To suit PEKC, we define this DP as “Control participant access to the platform to enable the provision of tiered benefits.” This DP is influenced by the attributes of exclusion and subractability. Providing tiered benefits ensures that knowledge provision is congruent with stakeholder expectations and improves trustworthiness. Hence, the underlying MRs that address effective benefits sharing are MR1, stakeholder congruence, and MR3, community trustworthiness.

Table 2. Applying Different Combinations of subtractability and exclusion in PEKC (Adapted from Hess and Ostrom, 2007)

<table><tr><td></td><td>No subtractability</td><td>Subtractability through quota</td></tr><tr><td>No exclusion</td><td>News headlines are available for all readers.</td><td>The number of free news articles is limited by quotas for individual readers.</td></tr><tr><td>Exclusion through access restriction</td><td>Premium news content is available by subscription.</td><td>Premium discounts are available for the selected user group (for example, students), limited by quotas.</td></tr></table>

Table 3. Differences between Natural Commons and Platform-Enabled Knowledge Commons for Four Key Attributes

<table><tr><td>Attribute</td><td>Natural commons</td><td>Platform-enabled knowledge commons</td></tr><tr><td>Creation(Frischmann et al., 2014)</td><td>Natural resources (for example, rivers, forests) are already present in the universe.</td><td>Knowledge resources are created by humans.</td></tr><tr><td>Subtractability(Hess &amp; Ostrom, 2007; Ostrom, 1990)</td><td>The units consumed will reduce the availability of resources in the common pool.</td><td>Varying levels of subtractability can be designed in PEKC.</td></tr><tr><td>Exclusion(Hess &amp; Ostrom, 2007; Ostrom, 1990)</td><td>Individuals can be excluded from using a resource.</td><td>Varying levels of exclusions can be designed in PEKC.</td></tr><tr><td>Revitalization(Mindel et al., 2018)</td><td>Natural resources need to be replenished as they are depleted</td><td>Though knowledge does not decay and the value of knowledge can change with time and needs to be maintained. Attracting more users is essential for the sustainability of PEKC.</td></tr></table>

Table 4. Derivation of PEKC DPs

<table><tr><td>PEKC DPs</td><td>Corresponding commons (DPs—Ostrom, 1990)</td><td>Influencing attributes</td><td>Corresponding MRs</td></tr><tr><td>PEKC_DP1: Define broad knowledge boundaries</td><td>DP1: Clearly defined boundaries</td><td>Creation</td><td>MR1: Stakeholder congruence</td></tr><tr><td>PEKC_DP2: Control participant access to the platform to enable the provision of tiered benefits</td><td>DP2: Congruence that allows members to share the benefits and costs proportionally</td><td>Exclusion, Subtractability</td><td>MR1: Stakeholder congruenceMR3: Community trustworthiness</td></tr><tr><td>PEKC_DP3: Establish mechanisms for stakeholders to collaborate</td><td>DP3: Collective-choice arrangements that enable members to establish local rules</td><td>Creation, Exclusion, Subtractability</td><td>MR1: Stakeholder congruence,MR2: Artifact sustainabilityMR3: Community trustworthiness</td></tr><tr><td>PEKC_DP4: Analyze the performance of the platform and visitor behavior</td><td>DP4: Monitoring of community behaviors</td><td>Creation, Exclusion, Revitalization</td><td>MR1: Stakeholder congruence,MR3: Community trustworthiness</td></tr><tr><td>PEKC_DP5: Apply penalties to deter offenders</td><td>DP5: Graduated sanctions</td><td>Exclusion</td><td>MR2: Artifact sustainabilityMR3: Community trustworthiness</td></tr><tr><td>PEKC_DP6: Resolve conflicts between stakeholders</td><td>DP6: Community members will have conflict resolution mechanisms</td><td>Exclusion</td><td>MR3: Community trustworthiness</td></tr><tr><td>PEKC_DP7: Provide guidelines for local content customization, if applicable</td><td>DP7: The community rules are recognized by government authorities</td><td>Creation</td><td>MR1: Stakeholder congruence</td></tr><tr><td>PEKC_DP8: Implement knowledge structure hierarchy and management, if applicable.</td><td>DP8: Nested enterprises</td><td>Creation, Subtractability, Exclusion, Revitalization</td><td>MR1: Stakeholder congruence, MR2: Artifact sustainability, MR3: Community trustworthiness</td></tr><tr><td>PEKC_DP9: Improve visibility of the knowledge platform within the target community</td><td>New</td><td>Creation, Revitalization</td><td>MR2: Artifact Sustainability</td></tr><tr><td>PEKC_DP10: Provide incentives to motivate participants to create and consume knowledge</td><td>New</td><td>Creation, Revitalization</td><td>MR2: Artifact Sustainability</td></tr></table>

PEKC\_DP3—Establish mechanisms for stakeholders to collaborate: Commons DP3 deals with collective-choice arrangements. Collective choice refers to empowering individuals in an operating environment to participate in modifying the operating rules. The fishing villages of the eastern coast of Canada are cited by Ostrom (1990) as examples. These fishers developed their own rules. These local rules define who can enter the fishery and local fishing grounds were divided among fishers using different technologies.

In a PEKC, the collective choice is applicable in scenarios like collaborative development, making decisions about the inclusion of knowledge articles, and the retirement of knowledge. This DP is stated as “Establish mechanisms for stakeholders to collaborate” and is influenced by the attributes of creation, exclusion, and subtractability. Stakeholder collaboration is one of the primary principles of PEKC design; hence, it contributes to all the MRs.

PEKC\_DP4—Analyze the performance of the platform and visitor behavior: Monitoring the health and performance of the ecosystem and user behavior are addressed as part of the commons DP4 principle. Ostrom (1990) advocated monitoring for overseeing community members’ performance and compliance with rules. The fishing agreements in Alanya, Turkey were cited as an example. The annual fishing spot allocation was performed and agreed upon by the fishing community. On the allocated day, the fishers would show up at their allocated fishing spot. The community monitoring ensured that the fishers did not show up on other days or expand their allocated area. Monitoring is important for PEKC to ensure that knowledge value is retained and trusted by the community. Though the intent is the same, the implementation of monitoring between natural commons and PEKC is different. In natural commons, member behaviors are typically monitored through physical observations and manual interventions. In

PEKC, the performance can be monitored through data analytics reports. Hence, this DP is defined as “Analyze the performance of the platform and visitor behavior.” This principle is influenced by attributes exclusion, subtractability, and revitalization. As monitoring helps to ensure that actions are taken to align the knowledge with the community expectations, DP4 contributes to MR1, stakeholder congruence. Also, monitoring is related to MR3, community trustworthiness, as monitoring is a prerequisite to taking corrective actions to encourage appropriate behaviors.

PEKC\_DP5—Apply penalties to deter offenders: Commons DP5: “Graduated sanctions to regulate member violations” proposes applying sanctions gradually for users who violate operational rules, depending on the seriousness and context of the offense. Ostrom (1990) observes that sanctions are comparatively low in comparison to the monetary loss of the offense—Spanish farms, Philippine irrigation systems, and Japanese mountain commons are cited as examples.

PEKC needs to implement graduated sanctions to ensure that the repository is reliable. Safner (2016) suggests that in PEKC, communal shaming, temporary bans, and permanent bans can be considered to be graduated sanctions. We define this principle as “Apply penalties to deter offenders” which is primarily influenced by the attribute of exclusion, as the bans imply that the participants are excluded from accessing the PEKC temporarily or permanently. DP5 contributes to MR2, artifact sustainability, and MR3, community trustworthiness. Applying penalties through temporary or permanent bans ensures that cyberattacks and inappropriate member behaviors are immediately curbed. Without these measures, the PEKC cannot survive in the online environment. Even one cyberattack could erode the trust of the community that was built over many years.

PEKC\_DP6—Resolve conflicts between stakeholders: The commons DP6 on resolving conflicts is related to commons DP5 on applying sanctions. DP6 observes that an effective commons must have access to low-cost, local conflict resolution mechanisms. Ostrom (1990) observed that in governing natural commons, simple rules for irrigation canal clean-up roster can be interpreted quite differently by different individuals and argues the need for local conflict resolution mechanisms. The intent of implementing a conflict resolution process is the same for natural commons and PEKC. The principle is stated as “Resolve conflicts between stakeholders” and is influenced by the attribute of exclusion. Conflicts could arise while creating content, as each contributor might have an agenda to communicate certain messages to the public. PEKC design features can consider inherent conflict resolution mechanisms like blocking multiple changes by a single author within a brief period, or temporarily blocking a noncompliant author. Blocking participants exhibiting undesired behaviors is underpinned by the exclusion attribute. DP6 contributes to MR3, community trustworthiness, as conflict resolution enhances trust among the members of the community.

PEKC\_DP7—Provide guidelines for local content customization, if applicable: The rights of local communities to form local rules are addressed in the commons DP7 principle. Ostrom (1990) cited the example that in fisheries, local fishers devise extensive rules defining who can use a fishing ground and what kind of equipment can be used. In PEKC, we interpret this DP as the degree of flexibility provided to groups that enable local customization of content. This is an optional DP. A PEKC may impose strict standards across all the knowledge articles or may choose to allow some degree of flexibility as long the created knowledge adheres to the overall objective of the PEKC. This DP is stated as “Provide guidelines for local content customization” and is underpinned by the creation attribute. The local content customization should be relevant to the stakeholders; hence, it underpins MR1, stakeholder congruence.

PEKC\_DP8—Implement knowledge structure hierarchy and management, if applicable: The commons could have a nested organizational structure. Appropriation, provision, monitoring, enforcement, conflict resolution, and governance activities are organized in multiple layers of nested enterprises. Such a nested, hierarchical structure is an optional DP for PEKC. One example of a nested enterprise structure is the implementation of a PEKC within a multinational organization that shares a common knowledge repository. There could be local creation and governance of knowledge by various functional units with overarching central governance. This DP is stated as “Implement knowledge structure hierarchy and management, if applicable,” which is supported by all the attributes. As the knowledge structure and governance properties of the lower-level nodes inherit the structure and properties of the central node, DP8 contributes to all three MRs.

PEKC\_DP9—Improve the visibility of the knowledge platform within the target community: As the PEKC is part of the internet ecosystem, it needs to be visible to the target community. The usefulness of the internet rests to a significant degree on search engines, and PEKC need to consider the design of “findability” (Kallinikos et al., 2013). Search engine optimization (SEO) is considered an essential digital marketing technique (Bhandari & Bansal, 2018; Chan et al., 2020). Another channel for improving visibility is using social media (Felix et al., 2017; Tafesse & Wien, 2018). We argue that improving visibility is a critical aspect of the knowledge commons and thus warrants a DP. This DP is underpinned by the attributes of creation and revitalization. The environment demands that for survival and growth, the PEKC needs to be visible; hence, DP9 contributes to MR2, artifact sustainability.

PEKC\_DP10—Provide incentives to motivate participants to create and consume knowledge: In contrast to natural commons, the survival of PEKC depends upon the continued patronage of the users (Mindel et al., 2018). Commons DPs explicitly addressed sanctions but did not include “incentives” to encourage the use of the commons. The omission could be due to the implicit assumption that natural commons will be consumed without the need to incentivize participants. The incentives can be both financial and nonfinancial. The success of Wikipedia is attributed to the contribution of voluntary authors. Researchers have analyzed various aspects of Wikipedia’s motivational factors (Salehan et al., 2017; Wang et al., 2018). Salehan et al. (2017) and identified these motivations as vertical social, horizontal social, hedonic, and utilitarian. A different classification of motivational factors for virtual collaboration— namely, intrinsic, extrinsic, and community, is proposed by Wang et al. (2018). Specific attributes of the knowledge platforms influence motivations to contribute to knowledge (Park & Park, 2016; Pee, 2018). Hence, we introduce the DP, “provide incentives,” which is underpinned by the creation and revitalization attributes. Providing incentives contributes to MR2, artifact sustainability, as the incentives ensure that stakeholders continue to have an interest in maintaining the knowledge within the PEKC instance.

## 4 Application of PEKC DPs to Service-Symphony

This section discusses how the PEKC DPs were applied to Service-Symphony. Figure 6 shows the mapping between the MRs, DPs, and design features. DP7 and DP8 were not applicable to Service-Symphony as there was no hierarchy in the implementation structure. Further, some aspects of DP6, DP9, and DP10 were implemented using nontechnological means.

PEKC\_DP1—Define broad knowledge boundaries: Service-Symphony was designed with a broad boundary to include the knowledge of process frameworks, tools, and skills that are applicable in the ITSM domain. The broad boundary encompasses governance, project management, quality, ITSM, continual improvement, and any other complementary domains. Within these domains, there are multiple frameworks and overlaps between the domains. The repository currently hosts 12 process frameworks and 35 practices.

The landing page of Service-Symphony is shown in Figure 7, demonstrating the broad knowledge boundary encompassing processes and tools. The knowledge articles of the process areas cross-reference the skills.

![](/api/attachments/PXRJ7YYC/fulltext/images/dc24e3613b669c888f578c9dd0492ae19f8de7e630db8e900d90ee205a9ac4a5.jpg)  
Figure 6. Mapping between MRs, PEKC DPs and the Design Features of Service-Symphony

![](/api/attachments/PXRJ7YYC/fulltext/images/8e01f7c44a21cc41bb9c1944b6e7664d94fcc16463d57b2a0390f7b1d5fe00d5.jpg)  
Figure 7. Implementation of Broad Knowledge Boundaries in Service-Symphony

PEKC\_DP2—Control participant access to the platform to enable the provision of tiered benefits: The participant access was controlled through three levels of access control. Any participant, without the need to register, could browse and read all articles without any restrictions. To post comments, the participants could log in through LinkedIn credentials, which was our way of ensuring that only members of the professional community were providing feedback on the knowledge articles and rating the tools listed in Service-Symphony. In addition, the comments were moderated by the administrator before they were made visible to the public. The third level was administrator access, which was managed by one of the researchers.

PEKC\_DP3—Establish mechanisms for stakeholders to collaborate: This DP was implemented outside the IS knowledge platform technical architecture. Whenever there was a major knowledge update or system feature addition, feedback was solicited from the expert panel. The expert panel provided inputs to prioritize the platform features and knowledge updates. Within PEKC the participants could post their views about the articles and rate their peer’s feedback. In the example given in Figure 8, the user rated the article 5 out of 5 and asked an open question.

PEKC\_DP4—Analyze the performance of the platform and visitor behavior: This DP was implemented within the IS knowledge platform. To monitor the knowledge repository performance, Google Analytics, a widely adopted web analytics service that provides statistics and analytical tools for search engine optimization was integrated into the repository. Figure 9 shows an overview of the analytics dashboard. The data indicates that there was a steady rise in users from April 2019 to September 2022, with around 137,000 visitors during this time. Around 28.5% (54,774) of visitors accessed Service-Symphony more than once, suggesting that they are interested in the knowledge presented by Service-Symphony. Further behavior analysis will be performed through the analytics data as a part of future research.

PEKC\_DP5—Apply penalties to deter offenders: The primary penalizing mechanism in Service-Symphony was blocking the user for a specific period and permanently blocking repeat offenders. This action was performed by the Service-Symphony administrator, the role played by the primary researcher.

PEKC\_DP6—Resolve conflicts between stakeholders: The conflict management process was executed externally through the expert panel. For example, there was a discussion of whether to include a process framework that was not a mainstream standard. One of the panel members advised rejecting the framework, stating: “I would be really careful about the use of additional frameworks. I note that frameworks under consideration are not amongst anything I have ever heard of before.” In the future, some aspects of conflict management could be incorporated through the features of the technical platform. For example, Wikipedia’s “talk” feature is one of the ways of managing conflicts within the author community (Safner, 2016).

![](/api/attachments/PXRJ7YYC/fulltext/images/f561e93e165871e3a39f9510b1bfd222f356fc6cec2529b3992da8a0de7c0b50.jpg)  
Figure 8. Establishing Mechanisms for Participant Collaboration

![](/api/attachments/PXRJ7YYC/fulltext/images/f8a0d75a1d6cbbf9821b6c0b1d5908a815fa0a5e743fb4f30af6d6de340f4a5a.jpg)

![](/api/attachments/PXRJ7YYC/fulltext/images/80e0c0d036284b6fcb68cd760a9f962355c4814a10cdcdda96b99aff0a46df35.jpg)

![](/api/attachments/PXRJ7YYC/fulltext/images/dc9629751b7b3de86db3855bc49fefab6f3dafff64b867049c94b4da96a964c9.jpg)  
Figure 9. Monitoring Performance of ITSM PEKC through Web-Analytics – April 2019 to September 2022

PEKC\_DP7 and PEKC\_DP8—The implementation of hierarchy and local content customization are relevant only to PEKC instances that have a decentralized governance structure. Since Service-Symphony is a single, centralized knowledge portal, DP7 and DP8 are not applicable.

of the user base was acquired through organic search indicating that Service-Symphony is visible to its target community, consistent with DP9.

PEKC\_DP9—Improve visibility of the knowledge platform within the target community: Providing visibility to the knowledge platform is critical to the success of the research. Visibility is provided through promotions during industry forums and on social media platforms. The knowledge portal was made a secure site to improve searchability within Google and improve trust. The platform did not include any advertisements. The content provided is relevant to the target audience. As a result, Service-Symphony is visible to stakeholders when they search online. Figure 10 shows that 86%

PEKC\_DP10—Provide incentives to motivate participants to create and consume knowledge: ITSM practitioners and students were the target audience of Service-Symphony. To encourage student community participation, Service-Symphony was integrated into the ITSM academic curricula of an Australian University (Ramakrishnan et al., 2022; Ramakrishnan et al., 2020). The students were encouraged to refer to the Service-Symphony as part of a research activity that was tied to an assessment. Hence, there were academic incentives for students to participate. As the platform is public facing, providing incentives was a challenge. Our research encouraged participation by posting topical articles on LinkedIn. The IS platform was integrated with LinkedIn to provide professional credibility and motivation to contribute to knowledge. Providing relevant knowledge to the practitioners was the key motivator for the participants to consume the knowledge.

## 5 Evaluation of the IS Artifact

Rigorous evaluation of artifacts is an important aspect of DSR (Peffers et al., 2012; Venable et al., 2016). Evaluation of artifacts can be performed at various stages of product development. Evaluation can be classified as ex ante vs. ex post (Venable et al., 2016). During the formative stages of artifact development, ex ante evaluation can be performed, which is a predictive evaluation. Ex post evaluation is an assessment of the value of the implemented system. To ensure that the repository is aligned with the practitioner community’s expectations, an expert panel was formed comprising four industry practitioners and one academic expert. During ITSM knowledge repository development, ex ante evaluation was performed by receiving feedback from the expert panel. The product development was carried out in fortnightly sprints. After every sprint, feedback was sought from the expert panel. The panel commented on the features, quality of the knowledge, and usability. The ex post evaluation of the instantiated artifact consisted of receiving feedback from practitioners, undergraduate students, and postgraduate students. Figure 11 shows the evaluation strategy of Service-Symphony (Ramakrishnan et al., 2022).

![](/api/attachments/PXRJ7YYC/fulltext/images/a64cd135326efd2725a2a9fc4d09b42d96d090aaf15d4bbcc2cd5e310abc4318.jpg)  
Figure 10. Service-Symphony User Acquisition by Channel

![](/api/attachments/PXRJ7YYC/fulltext/images/c21fa2eb601743027a6fbfb345d95730258c49b07b2d54cc3abdbcc7e294931e.jpg)  
Figure 11. Evaluation Strategy of Service-Symphony (Ramakrishnan et al., 2022)

Practitioner feedback was received after demonstrating the ITSM knowledge repository at an ITSMF state seminar in Brisbane, Australia. We administered a paper-based survey and received 26 responses from the participants. Participants indicated that the repository was useful and suggested improvement opportunities to include multilingual support and more case studies. In the student evaluation, 46 postgraduate students and 33 undergraduate students from an ITSM course at an Australian University participated. The methodological triangulation approach (Bekhet & Zauszniewski, 2012; Jack & Raturi, 2006) was followed to evaluate the student perception of the repository. The methodological triangulation used diverse measurements including the net promoter score (NPS), a product quality survey, and free-format written feedback about the usefulness of the repository. The three measurements showed a consistent theme, namely that the repository was useful to students. The students suggested improvement opportunities including engaging interface design and more case studies on the implementation of the frameworks (Ramakrishnan et al., 2022)

In addition to focused evaluation, visitor trends are being continually monitored. The visitor trends provide insight into geographic regions, the pages visited, and other useful metrics in order to improve Service-Symphony. Google Analytics for the knowledge portal indicates that there has been a steady rise in visitors accessing the portal.

Reusability evaluation of DPs guides the development of multiple instances of IT artifacts that belong to the same class (Iivari et al., 2021; Kruse et al., 2016). If reusability is not evaluated by practitioners, there is a risk that the DPs will not be useful in practice (Cronholm & Göbel, 2018; Iivari et al., 2021). To mitigate this risk, Iivari et al. (2021) propose a revaluation framework comprising the following five criteria: (1) accessibility, (2) importance, (3) novelty and insightfulness, (4) actability and guidance, and (5) effectiveness.

The key focus of this research is the development and evaluation of the DPs. Iivari et al. (2021) emphasize that the target audience of the DPs should be clearly defined. Our target audience for the DPs is IS solution architects. Solution architects are responsible for the design and communication of the design and development of integrated solutions that meet current and future business needs (SFIA, 2021).

This research employed the focus group (FG) method to conduct the DPs evaluation. The FG technique is suitable for research that aims to understand how people feel and think about an idea (Henriques & O’Neill, 2021). FG is one of the qualitative research methods employed in DSR (Gibson & Arnott, 2007; Hevner & Chatterjee, 2010; Tremblay et al., 2010). Depending on the goal of the research, the FG can be either exploratory or confirmatory (Hevner & Chatterjee, 2010). The exploratory FG should be used when the design artifact is intended to refine or improve the design. The confirmatory FG should be employed when the design artifact’s utility needs to be confirmed. In our research case, we consider the FG to be confirmatory, as the primary goal is to confirm the reusability of the DPs in practice. The activities of the FG are: (1) problem definition, (2) identification of the participants, (3) moderator discussion guide, (4) conducting the FG, and (5) analysis and interpretation (Stewart & Shamdasani, 2014). We describe the key activities of problem identification, participant identification, and results analysis in the following sections.

The objective of the FG is to perform a confirmatory evaluation of the PEKC DPs based on the five criteria of the reusability evaluation framework (Iivari et al., 2021). For the FG, we expanded the criteria into descriptive questions, as described in Table 5

The target audience for the DPs is solution architects, who are responsible for developing and communicating solution architecture (SFIA, 2021). The choice of architects to evaluate the DPs was guided by two considerations: we chose (1) architects who are familiar with IS design because they are responsible for designing optimal IS solutions for the business problem, and (2) architects who understand the importance of reusability and know how to design and evaluate reusable DPs.

The size of a traditional FG is typically 10-12 participants, with a meeting duration of two hours (Hevner & Chatterjee, 2010). The traditional FG is suitable for discussing exploratory questions. As the research objective is confirmatory, we opted for a mini-FG. A mini-FG typically has 6-8 participants (Hevner & Chatterjee, 2010). The architects were from an organization that employs around 7500 people, including the primary researcher. There were six architects in the practice, and all were invited to the FG. One architect declined the invitation due to work priorities, resulting in an FG size of five.

Each of the five participants had more than 15 years of industry experience. Among the five architects, four architects had a TOGAF 9.2 certification, which is a standard for IS architecture. The IS architects were considered to be external evaluators, as they were not involved in the research project (Iivari et al., 2021). Table 6 shows the participant profile. Two FG meetings were held, with three architects participating in the first meeting and the remaining two architects participating in the second.

After the presentation and discussion, the participants were asked to evaluate and discuss the questions identified in Table 5. We clarified that the questionnaire was not a quantitative survey but would only be used to facilitate individual reflection preceding the team discussion. An online anonymous questionnaire was created to facilitate individual reflection and the collective sharing of the results, as shown in Figure 12.

All the participants agreed that the DPs were easy to understand and address an important real-world problem. All agreed that they gained new insights from the DPs, except for one participant. The architect who disagreed had a specific solution in mind that was implemented in a previous organization, which was similar to the PEKC instantiation knowledge platform. It was clarified that the focus was on DPs, not the instantiated artifact. The remaining participants agreed that the DPs were “novel and insightful.” They mentioned that they were not familiar with knowledge commons and that the entire concept would be quite useful in designing knowledge systems in the organizational context. The architects acknowledged that their solution design would be primarily technology-centric and the DPs provided a way to consider people/community interactions. They also agreed that the additional DPs on providing incentives and managing visibility and trust were important considerations that were sometimes overlooked.

Table 5. Focus Group Questions Based on Reusability Criteria (Iivari et al., 2021)

<table><tr><td>DPs reusability criteria (Iivari et al., 2021)</td><td>Focus group questions</td></tr><tr><td>Accessibility</td><td>Can you understand and comprehend the PEKC DPs?</td></tr><tr><td>Importance</td><td>Do the DPs address important real-world problems?</td></tr><tr><td>Novelty and insightfulness</td><td>Did you get any new insights from the DPs?</td></tr><tr><td>Actability and guidance</td><td>Can the DPs be realistically applied in practice?</td></tr><tr><td>Effectiveness</td><td>Can the knowledge repositories that are created using the DPs create business value?</td></tr></table>

Table 6. Focus Group Participant Profile

<table><tr><td>Participant ID</td><td>Years of IT experience</td><td>Title</td><td>TOGAF certification</td></tr><tr><td>P1</td><td>15 years</td><td>Manager architecture</td><td>Yes</td></tr><tr><td>P2</td><td>16 years</td><td>Principal applications architect</td><td>Yes</td></tr><tr><td>P3</td><td>18 years</td><td>Principal ICT architect</td><td>Yes</td></tr><tr><td>P4</td><td>23 years</td><td>Principal ICT architect</td><td>No</td></tr><tr><td>P5</td><td>27 years</td><td>Manager ICT solutions</td><td>Yes</td></tr></table>

## PEKC Design Principles Evaluation

![](/api/attachments/PXRJ7YYC/fulltext/images/5a093cfcd330414935fb46811b5cc8d48d0b7de8bbf67d2931662d0b6d1536a5.jpg)  
Figure 12. Summary of Focus Group Results

For the question about DPs’ applicability to practice, the discussions centered around the ability to tailor the DPs. The researcher explained that the DPs are meant to be tailored and not all DPs are mandatory. A participant said while they appreciated that the DPs could be tailored, they were not clear on how a new DP could be added. The participant proposed that governance criteria on how the DPs can be tailored should be addressed. The researcher agreed with that feedback.

Another practitioner was not sure whether the DPs could be applied in all scenarios in practice. The researcher probed whether the feedback concerned the knowledge commons or the DPs. The participant said that he was referring to the DPs, not the knowledge commons concept. The participant was referring to a specific application where certain aspects of knowledge commons should not be shared due to confidentiality reasons. The participant argued that the confidential asset could be part of the larger knowledge commons, but only that area should be governed separately. They noted that the DPs do not cover this specific application of governing confidential data. This argument was refuted by another participant who noted that the DPs were applicable to most typical scenarios and could be tailored to suit any scenario.

Though all participants agreed with Question 5 in the online questionnaire, during discussion one participant was not sure whether the question was relevant as the business value would depend upon the type of instances being created. The researcher agreed with the position that it is difficult to estimate the business value without describing the context of the instance.

## 6 Discussion

We embarked on this research to develop PEKC DPs and apply them in the instantiated artifact, Service-Symphony, which provides value to ITSM students and practitioners. Initially, we attempted to apply the commons DPs from the economics discipline to develop Service-Symphony. This attempt identified the limitations of commons DPs, which led us to develop a separate set of DPs that are accessible, relevant, and reusable by the IS target audience. We claim that the proposed PEKC DPs are novel and insightful because they guide IS researchers and practitioners to consider the larger sociotechnical environment instead of limiting their focus to the technical environment only. We realized that deriving IS-specific DPs from economic theory is not a straightforward process. The influencing attributes impact multiple DPs, and the relationship is complex. There are also interrelationships between DPs. For example, applying penalties, providing incentives, and conflict management are closely related. We acknowledged this complexity and presented a mapping table that reflects the one-to-many relationships of these parameters. It was also difficult to identify design features that support the DPs in terms of applying penalties, providing incentives, and conflict management. We realized that the technology platform only supports these DPs where possible. For example, conflict management was implemented outside the technology platform. Hence, while presenting the DPs to the IS practitioners, we emphasized that the DPs are to be considered as guidelines and not as stringent product specifications.

The evaluation of the DPs by the architects validated that the DPs are accessible and relevant to the IS practitioners. The architects agreed that the DPs allowed them to think beyond the technical aspects of the instantiated artifact and were useful for designing other instances. The DPs also challenged them to consider design features to improve trust, providing incentives and applying penalties—the “soft aspects” that are normally not considered during a solution design.

The application of DPs to the instantiated artifact enabled us to appreciate whether the DPs are pragmatic. The instantiation helped us to clearly articulate the intended interpretation of the DPs. The instantiation was an important aspect of getting the buy-in from the IS practitioners. We recommend that when presenting DPs to IS practitioners, the researchers should also provide instantiated examples of how the DPs are applied.

The decision to conduct an FG interview was rewarding. Before engaging the practitioners, the research team was focused on academic rigor. As part of FG preparation, the researchers were motivated to revisit the DPs to determine whether they were articulated to suit IS practitioners. One of the methods that differs from conventional FG is that we used an online, live survey. This deviation proved to be effective, as the meeting was conducted in an online collaborative environment due to COVID-19 restrictions, as opposed to face-to-face meetings.

## 6.1 Contributions to Theory

The seminal paper by Gregor and Hevner (2013) proposed three levels of knowledge contribution in DSR research. They proposed that the DSR contributions can be at Level 1, situated instantiations of artifacts; Level 2, Nascent design theory, which could include DPs, methods, models, and technological rules; or Level 3, grand theories and midrange theories. This research contributes to both Level 2 and Level 1 by developing DPs and applying them to an instantiated artifact that was developed through the research.

DPs are regarded as one of the important outcomes of design knowledge (Cronholm & Göbel, 2018; Iivari et al., 2018; Iivari et al., 2021). The DPs are targeted at solution architects who can use diverse ways to apply the DPs to create specific instances. For example, solution architects could design a knowledge commons specific to their organization to enable diverse teams to innovate together to solve a problem.

This research contributes to the DSR body of knowledge through the development of PEKC MRs and DPs and provides the following significant insights for DSR knowledge.

This research developed DPs for a problem class, PEKC. As the problem class is critical in this knowledge economy, the underpinning DPs also play a pivotal role as they provide prescriptive guidance to IS developers. The scope of the DPs is broad to cover the sociotechnological arena as opposed to focusing only on the technical platform.

The approach to developing the DPs is also significant as the derivation of the IS DPs from a non-IS external theory is not a typical path for developing DPs. IS DPs typically codify the principles for an abstract problem class from an IS artifact (Cronholm & Göbel, 2018; Kruse et al., 2016). This research’s approach of commencing with an economics theory, refining the theory to suit IS practice and then applying the theory pragmatically to build an IS artifact is novel.

While the extant research acknowledges that MRs are an important aspect of DSR, there is no systematic process for developing the MRs (Möller et al., 2020). Our research used a method that grouped Agile user stories to develop MRs.

The MRs and DPs are internally, externally, and empirically grounded, which is one of the aspects of a good design theory, according to Goldkuhl (2004).

Finally, the reusability evaluation of the DPs (Iivari et al., 2021) by the IS practitioner community represents a significant step toward closing the gap between research and practitioner communities.

## 6.2 Contributions to Practice

The contribution of this research is significant to ITSM practitioners who play a pivotal role in organizations. The broad ITSM community is a global community, with an estimated population of more than half a million IS practitioners. This community comprises consultants, practice managers, auditors, project managers, DevOps professionals, service desk professionals, technology providers, training providers, certification bodies, students, and higher education institutions. The analytics data indicated that the target audience considered Service-Symphony to be relevant, as 137,000 users have visited Service-Symphony since its launch in February 2019. Around 28.5% (54,774) of visitors accessed Service-Symphony more than once suggesting that they are interested in the knowledge delivered by Service-Symphony.

To align with the expectations of practitioners, the professional body ITSM Australia was involved in the development of Service-Symphony from its inception and recognized the contributions of Service-Symphony to the ITSMF community with the “Business Innovation of the Year 2019” award at their annual conference. This award further substantiates the relevance of our DSR research to practice.

Service-Symphony was also used as a complementary teaching resource for undergraduate and postgraduate students enrolled in an ITSM course at an Australian University. To date, 79 students have used Service-Symphony to learn about emerging industry practices. We argue that introducing Service-Symphony as an additional learning resource in the curriculum helps the students gain contemporary industry knowledge and contributes to continual learning (Ramakrishnan et al., 2022).

## 7 Conclusions, Limitations, and Future Work

This paper addressed the research question around the formulation and evaluation of DPs: What are the design principles that will provide guidance to IS practitioners when developing a PEKC? This research answered this question through an exemplar case study, contributing to both DSR theory and practice. The key aspects of our research are:

Begin with a practitioner problem that impacts a global practitioner community and is not confined within any specific organizational boundaries. To manage scope, we worked closely with a professional body and formed a governance group. We translated the objectives of the design into a set of MRs.

We also identified an applicable economics theory during the initial stages of research. This position ensured that theory and artifact design fed each other iteratively.

We adapted the Agile development method to engage an expert panel, which ensured that Service-Symphony met the diverse needs of practitioners.

• We assessed the DPs with a focus group of IS architects to demonstrate the pragmatic, reusability value of the DPs to IS practice.

We grounded the MRs and DPs externally, internally, and empirically, thus contributing to a coherent, multigrounded design theory.

The researchers acknowledge the following limitations. We applied PEKC theory in only one expository instantiation, which is a limitation of the DPs’ evaluation. For a more comprehensive study, applying DPs to multiple instances would provide more insights. The evaluation using Google Analytics was limited to high-level trends. Advanced behavior analytics are being explored and will be addressed in future research. The evaluation by students was limited to a single university and hence we cannot rule out bias. Similarly, all the solution architects who evaluated the reusability aspects of the DPs were from a single organization. Though the architects were external to the research, there could have been some bias in the evaluation.

We have an ambitious vision to further extend the research to contribute to theory, methodology, and practice perspectives. To design an IS artifact, DPs should be considered from multiple perspectives. PEKC DPs address the knowledge governance aspect of the design. In the future, we will expand the DPs to address innovation-centric knowledge and enterprise architecture. Commons theory proposes a conceptual model, the institutional analysis and development (IAD) framework, to systematically analyze commons (Albagli et al., 2018; Frischmann et al., 2014; Ostrom, 2019). Our future work will consider a more refined design theory, comprising MRs, multidimensional DPs, and a conceptual model. There are research opportunities to refine DSR methodology to align with

Agile development, and from the practice perspective, the application of Service-Symphony could be expanded as a complementary learning resource for IT governance, project management, and DevOps curricula. We are exploring opportunities with other universities about the possibility of including Service-Symphony in their ITSM curricula. To expand the value proposition to practitioners, we will be discussing providing the targeted content to members of other professional bodies, such as ISACA.

Our work demonstrates that a DSR project can contribute to both theory and practice. The identification of a relevant theory was one of the early steps of this research. The adaptation of an economic theory to suit the IS domain has been an interesting challenge and we believe that this work will motivate other researchers to explore ideas from other disciplines to provide inspiration in designing IS artifacts.

## References

Albagli, S., Clinio, A., Parra, H., & Fonseca, F. (2018). Beyond the dichotomy between natural and knowledge commons: Reflections on the IAD framework from the Ubatuba open science project. Proceedings of the International Conference on Electronic Publishing. Available at https://doi.org/10.4000/ proceedings.elpub.2018.28

Allen, D., & Potts, J. (2016). How innovation commons contribute to discovering and developing new technologies. International Journal of the Commons, 10(2). 1035-1054.

Amorim, A. C., da Silva, M. M., Pereira, R., & Gonçalves, M. (2021). Using agile methodologies for adopting COBIT. Information Systems, 101, Article 101496.

Baskerville, R., Baiyere, A., Gregor, S., Hevner, A., & Rossi, M. (2018). Design science research contributions: finding a balance between artifact and theory. Journal of the Association for Information Systems, 19(5), 358-376.

Bekhet, A. K., & Zauszniewski, J. A. (2012). Methodological triangulation: An approach to understanding data. Nurse researcher, 30(2), 40-43.

Bhandari, R. S., & Bansal, A. (2018). Impact of search engine optimization as a marketing tool. Jindal Journal of Business Research, 7(1), 23-36.

Cater-Steel, A., Tan, W.-G., & Toleman, M. (2006). Challenge of adopting multiple process improvement frameworks. Proceedings of the 14th European Conference on Information Systems (pp. 1375-1386).

Chan, Y. E., Krishnamurthy, R., & Desjardins, C. (2020). Technology-driven innovation in small firms. MIS Quarterly Executive, 19(1), 39-55.

Chandra, L., Seidel, S., & Gregor, S. (2015). Prescriptive knowledge in IS research: Conceptualizing design principles in terms of materiality, action, and boundary conditions. 2015 48th Hawaii International Conference on System Sciences (pp. 4039-4048).

Cheshire, C. (2011). Online trust, trustworthiness, or assurance? Daedalus, 140(4), 49-58.

Comfort, L. K., & Okada, A. (2013). Emergent leadership in extreme events: A knowledge commons for sustainable communities. International Review of Public Administration, 18(1), 61-77.

Conboy, K., Gleasure, R., & Cullina, E. (2015). Agile design science research. Proceedings of the

International Conference on Design Science Research in Information Systems

Cronholm, S., & Göbel, H. (2018). Guidelines supporting the formulation of design principles. Proceedings of the 29th Australasian Conference on Information Systems.

Cronholm, S., Göbel, H., & Åkesson, M. (2020). ITIL compliance with service-dominant logic. E-Service Journal, 11(2), 74-97.

Dalpiaz, F., & Brinkkemper, S. (2018). Agile requirements engineering with user stories. Proceedings of the IEEE 26th International Requirements Engineering Conference.

Dourado, E., & Tabarrok, A. (2015). Public choice perspectives on intellectual property. Public Choice, 163(1-2), 129-151.

Ebert, C., Gallardo, G., Hernantes, J., & Serrano, N. (2016). DevOps. IEEE Software, 33(3), 94-100.

Ekanata, A., & Girsang, A. S. (2017, 18-19 Sept. 2017). Assessment of capability level and IT governance improvement based on COBIT and ITIL framework at Communication Center Ministry of Foreign Affairs. Proceedings of the International Conference on ICT For Smart Society.

Felix, R., Rauschnabel, P. A., & Hinsch, C. (2017). Elements of strategic social media marketing: A holistic framework. Journal of Business Research, 70, 118-126.

Forte, A., Larco, V., & Bruckman, A. (2009). Decentralization in Wikipedia governance. Journal of Management Information Systems, 26(1), 49-72.

Frischmann, B. M., Madison, M. J., & Strandburg, K. J. (2014). Governing knowledge commons. Oxford University Press.

Gaver, W. W. (1991). Technology affordances. Proceedings of the SIGCHI Conference on Human Factors in Computing Systems (pp. 79- 84).

Gibson, M., & Arnott, D. (2007). The use of focus groups in design science research. 18th Proceedings of the Australasian Conference on Information Systems.

Goldkuhl, G. (2004). Design theories in information systems-a need for multi-grounding. Journal of Information Technology Theory and Application, 6(2), 59-72.

Gregor, S., Chandra Kruse, L., & Seidel, S. (2020). Research perspectives: the anatomy of a design principle. Journal of the Association for Information Systems, 21(6), 1622-1652.

Gregor, S., & Hevner, A. R. (2013). Positioning and presenting design science research for maximum impact. MIS Quarterly, 37(2), 337- 355.

Gregor, S., & Jones, D. (2007). The anatomy of a design theory. Journal of the Association for Information Systems, 8(5), 312-335.

Gregor, S., Müller, O., & Seidel, S. (2013). Reflection, abstraction and theorizing in design and development research. Proceedings of the European Conference on Information Systems.

Haj-Bolouri, A., Winman, T., & Svensson, L. (2020). Meta-requirements for immersive collaborative spaces in industrial workplace learning: Towards a design theory. Proceedings of the International Conference on Design Science Research in Information Systems and Technology.

Hardin, G. (1968). The tragedy of the commons. Science, 162(3859), 1243-1248.

Henriques, T. A., & O’Neill, H. (2021). Design science research with focus groups: A pragmatic metamodel. International Journal of Managing Projects in Business, 16(1), 119-140.

Hensher, M., Kish, K., Farley, J., Quilley, S., & Zywert, K. (2020). Open knowledge commons versus privatized gain in a fractured information ecology: lessons from COVID-19 for the future of sustainability. Global Sustainability, 3, Article e26.

Hess, C., & Ostrom, E. (2007). Understanding knowledge as a commons. MIT Press.

Heston, K. M., & Phifer, W. (2011). The multiple quality models paradox: How much “best practice” is just enough? Journal of Software Maintenance & Evolution: Research & Practice, 23(8), 517-531.

Hevner, A., & Chatterjee, S. (2010). Design science research in information systems. In A. Hevner & S. Chatterjee (Eds.) Design Research in Information Systems: Theory and Practice (pp. 9-22). Springer.

Hevner, A., March, S. T., Park, J., & Ram, S. (2004). Design science research in information systems. MIS Quarterly, 28(1), 75-105.

Hevner, A. R. (2007). A three cycle view of design science research. Scandinavian Journal of Information Systems, 19(2), 87-92.

Huang, J., Shi, S., Chen, Y., & Chow, W. S. (2016). How do students trust Wikipedia? An examination across genders. Information Technology & People, 29(4), 750-773.

Iivari, J., Hansen, M. R. P., & Haj-Bolouri, A. (2018). A framework for light reusability evaluation of design principles in design science research. Proceedings of the 13th International Conference on Design Science Research and Information Systems and Technology.

Iivari, J., Rotvit Perlt Hansen, M., & Haj-Bolouri, A. (2021). A proposal for minimum reusability evaluation of design principles. European Journal of Information Systems, 30(3), 286- 303.

Jack, E. P., & Raturi, A. S. (2006). Lessons learned from methodological triangulation in management research. Management Research News, 29(6), 345-357.

Kallinikos, J., Aaltonen, A., & Marton, A. (2013). The ambivalent ontology of digital artifacts. MIS Quarterly, 37(2), 357-370.

Kannan, V., Basit, M. A., Bajaj, P., Carrington, A. R., Donahue, I. B., Flahaven, E. L., Medford, R., Melaku, T., Moran, B. A., & Saldana, L. E. (2019). User stories as lightweight requirements for agile clinical decision support development. Journal of the American Medical Informatics Association, 26(11), 1344-1354.

Kittur, A., Suh, B., & Chi, E. H. (2008). Can you ever trust a Wiki? Impacting perceived trustworthiness in Wikipedia. Proceedings of the 2008 ACM Conference on Computer Supported Cooperative Work (pp. 477-480).

Kruse, L. C., Seidel, S., & Purao, S. (2016). Making use of design principles. Proceedings of the International Conference on Design Science Research in Information Systems and Technology.

Kuechler, W., & Vaishnavi, V. (2012). A framework for theory development in design science research: multiple perspectives. Journal of the Association for Information Systems, 13(6), 395-423.

Lamberti, D. M., & Wallace, W. A. (1990). Intelligent interface design: An empirical assessment of knowledge presentation in expert systems. MIS Quarterly, 14(3), 279-311.

Lim, S. (2009). How and why do college students use Wikipedia? Journal of the American Society for Information Science and Technology, 60(11), 2189-2202.

Lins, S., Schneider, S., Szefer, J., Ibraheem, S., & Sunyaev, A. (2019). Designing monitoring systems for continuous certification of cloud services: deriving meta-requirements and design guidelines. Communications of the

Association for Information Systems, 44(1), Article 25.

Machackova, H., & Smahel, D. (2018). The perceived importance of credibility cues for the assessment of the trustworthiness of online information by visitors of health-related websites: The role of individual factors. Telematics and Informatics, 35(5), 1534-1541.

McLoughlin, C., & Lee, M. (2007). Social software and participatory learning: Pedagogical choices with technology affordances in the Web 2.0 era. Proceedings of Ascilite Singapore (pp. 664- 675).

McNaughton, M., & Rao, L. (2017). Governing knowledge commons in Caribbean disaster management: A comparative institutional analysis. Information Services & Use, 37(4), 437-449.

Mindel, V., Mathiassen, L., & Rai, A. (2018). The sustainability of polycentric information commons. MIS Quarterly, 42(2), 607-632.

Möller, F., Guggenberger, T. M., & Otto, B. (2020). Towards a method for design principle development in information systems. Proceedings of the International Conference on Design Science Research in Information Systems and Technology,

Ostrom, E. (1990). Governing the commons: The evolution of institutions for collective action. Cambridge University Press.

Ostrom, E. (2019). Institutional rational choice: An assessment of the institutional analysis and development framework. In P. A. Sabatier (Ed.), Theories of the policy process (2<sup>nd</sup> ed., pp. 21-64). Routledge.

Ostrom, E. (1999). Coping with tragedies of the commons. Annual Review of Political Science, 2(1), 493-535.

Ostrom, E. (2008). The challenge of common-pool resources. Environment: Science and Policy for Sustainable Development, 50(4), 8-21.

Ostrom, E., Gardner, R., Walker, J., Walker, J. M., & Walker, J. (1994). Rules, games, and commonpool resources. University of Michigan Press.

Pan, L.-Y., & Chiou, J.-S. (2011). How much can you trust online information? Cues for perceived trustworthiness of consumer-generated online information. Journal of Interactive Marketing, 25(2), 67-74.

Park, H., & Park, S. J. (2016). Communication behavior and online knowledge collaboration:

Evidence from Wikipedia. Journal of Knowledge Management, 20(4), 769-792.

Pee, L. G. (2018). Community’s knowledge need and knowledge sharing in Wikipedia. Journal of Knowledge Management, 22(4), 912-930.

Peffers, K., Rothenberger, M., Tuunanen, T., & Vaezi, R. (2012). Design science research evaluation. Proceedings of the International Conference on Design Science Research in Information Systems (pp. 398-410).

Peffers, K., Tuunanen, T., Rothenberger, M. A., & Chatterjee, S. (2007). A design science research methodology for information systems research. Journal of Management Information Systems, 24(3), 45-77.

Potts, J. (2022). Innovation commons: New innovation policy for a digital economy. Available at https://doi.org/10.2139/ssrn.4095561

Ramakrishnan, M., Gregor, S., Shrestha, A., & Soar, J. (2022). Achieving industry-aligned education through digital-commons: A case study. Journal of Computer Information Systems, 63(4), 950-964.

Ramakrishnan, M., Shrestha, A., Cater-Steel, A., & Soar, J. (2018). IT service management knowledge ecosystem–literature review and a conceptual model. Proceedings of the 29th Australasian Conference on Information Systems.

Ramakrishnan, M., Shrestha, A., & Soar, J. (2020). Inclusion of complementary industry knowledge in IT service management curriculum: A case study. Proceedings of the 23rd Pacific Asia Conference on Information Systems.

Ramakrishnan, M., Shrestha, A., & Soar, J. (2021). Innovation centric knowledge commons: A systematic literature review and conceptual model. Journal of Open Innovation: Technology, Market, and Complexity, 7(1), Article 35.

Rathwell, K. J., Armitage, D., & Berkes, F. (2015). Bridging knowledge systems to enhance governance of the environmental commons: A typology of settings. International Journal of the Commons, 9(2), 851-880.

Reinecke, K., & Bernstein, A. (2013). Knowing what a user likes: A design science approach to interfaces that automatically adapt to culture. MIS Quarterly, 37(2), 427-453.

Rose, C. (1986). The comedy of the commons: custom, commerce, and inherently public property. The University of Chicago Law Review, 53(3), 711-781.

Roumani, Y., & Nwankpa, J. (2020). Examining exploitability risk of vulnerabilities: A hazard model. Communications of the Association for Information Systems, 46(1), Article 18.

Safner, R. (2016). Institutional entrepreneurship, Wikipedia, and the opportunity of the commons. Journal of Institutional Economics, 12(4), 743-771.

Salehan, M., Kim, D. J., & Kim, C. (2017). Use of online social networking services from a theoretical perspective of the motivationparticipation-performance framework. Journal of the Association for Information Systems, 18(2), 141-172.

SFIA. (2021). Solution architecture ARCH. SFIA. Retrieved on August 21, 2021 from https://sfiaonline.org/en/sfia-7/skills/solution-architecture

Shrestha, A., Cater-Steel, A., & Toleman, M. (2016). Innovative decision support for IT service management. Journal of Decision Systems, 25(sup1), 486-499.

Shrestha, A., Cater-Steel, A., Toleman, M., Behari, S., & Rajaeian, M. M. (2020). Development and evaluation of a software-mediated process assessment method for IT service management. Information & Management, 57(4), Article 103213.

Stewart, D. W., & Shamdasani, P. N. (2014). Focus groups: Theory and practice. SAGE.

Tafesse, W., & Wien, A. (2018). Implementing social media marketing strategically: An empirical assessment. Journal of Marketing Management, 34(9-10), 732-749.

Taylor, S. (2007). The official introduction to the ITIL service lifecycle. The Stationary Office.

Tremblay, M. C., Hevner, A. R., & Berndt, D. J. (2010). The use of focus groups in design science research. In M. C. Tremblay, A. R. Hevner & D. J. Berndt (Eds.), Design research in information systems (pp. 121-143). Springer.

Vaishnavi, V. K., & Kuechler, W. (2015). Design science research methods and patterns: innovating information and communication technology. CRC Press.

Vance, A., Lowry, P. B., & Eggett, D. L. (2015). Increasing accountability through the user interface design artifacts: A new approach to addressing the problem of access-policy violations. MIS Quarterly, 39(2), 345-366.

Venable, J., Pries-Heje, J., & Baskerville, R. (2016). FEDS: a framework for evaluation in design

science research. European Journal of Information Systems, 25(1), 77-89.

Veronica, & Suryawan, A. D. (2017, 15-17 Nov. 2017). Information technology service performance management using COBIT and an ITIL framework: A systematic literature review. Proceedings of the 2017 International Conference on Information Management and Technology.

Viégas, F. B., Wattenberg, M., & McKeon, M. M. (2007). The hidden order of Wikipedia. Proceedings of the International Conference on Online Communities and Social Computing

Wall, D. (2014). The sustainable economics of Elinor Ostrom: Commons, contestation and craft. Routledge.

Walls, J. G., Widermeyer, G. R., & El Sawy, O. A. (2004). Assessing information system design theory in perspective: How useful was our 1992 initial rendition? Journal of Information Technology Theory and Application, 6(2), 43- 58.

Walls, J. G., Widmeyer, G. R., & El Sawy, O. A. (1992). Building an information system design theory for vigilant EIS. Information Systems Research, 3(1), 36-59.

Wang, J., Zhang, R., Hao, J.-X., & Chen, X. (2018). Motivation factors of knowledge collaboration in virtual communities of practice: a perspective from system dynamics. Journal of Knowledge Management, 23(3), 466-488.

Wieringa, R. (2010). Relevance and problem choice in design science. Proceedings of the International Conference on Design Science Research in Information Systems

Wilkin, C., Campbell, J., Moore, S., & Van Grembergen, W. (2013). Co-creating value from IT in a contracted public sector service environment: Perspectives on COBIT and Val IT. Journal of Information Systems, 27(1), 283- 306.

Winkler, T. J., & Wulf, J. (2019). Effectiveness of IT service management capability: Value cocreation and value facilitation mechanisms. Journal of Management Information Systems, 36(2), 639-675.

Yeo, M. L., & Arazy, O. (2012). What makes corporate wikis work? Wiki affordances and their suitability for corporate knowledge work. Proceedings of the International Conference on Design Science Research in Information Systems.

## About the Authors

Muralidharan Ramakrishnan is an industry practitioner who completed his PhD in 2023 at the University of Southern Queensland, Australia. His research focuses on IT Service management, governance, knowledge management, and business process management. Murali has consulted businesses to enhance their business and IT services across multiple sectors, such as financial services, higher education, utilities, telecom, transport, and governmental organizations. Murali’s contributions to industry have been recognized through several prestigious awards in innovation. Notably, he was honored with the Business Innovation Award 2019 by ITSMF Australia. Mural holds a master’s degree in software-systems and possesses an MBA qualification, further bolstered by numerous industry certifications, such as the Six Sigma Black Belt.

Shirley Gregor is a professor emerita at the Australian National University. Her research interests include artificial intelligence, human-computer interaction, and the philosophy of science and technology. Professor Gregor spent a number of years in the computing industry in Australia and the United Kingdom before beginning an academic career. She obtained her PhD in information systems from the University of Queensland in 1996. Her research has appeared in outlets including MIS Quarterly, Journal of Management Information Systems, Journal of the Association of Information Systems, International Journal of Electronic Commerce, European Journal of Information Systems, and Information Technology & People. Professor Gregor was made an Officer of the Order of Australia in the Queen’s Birthday Honour’s list in June 2005. Also in 2005, she was elected as a Fellow of the Australian Computer Society. In 2010 she was made a Fellow of the Association for Information Systems, the premier global body for the discipline. In 2014, she was awarded a Schöller Senior Fellowship at the Friedrich Alexander University of Erlangen-Nurenberg. She was given a DESRIST Lifetime Achievement Award in 2017 for contributions to design science research in information systems and technology.

Anup Shrestha is a senior lecturer in information systems at the University of Southern Queensland, Australia. Hi PhD research, working on an Australian Research Council industry linkage grant in the IT service management industry, was awarded the Best Australian PhD in Information Systems Prize in 2016 by ACPHIS (Australian Council of Professors and Heads of Information Systems) and he received the Queensland IT Innovation Award in 2015. Anup’s research focuses on understanding the interplay between information systems and management principles in organizations and societies, including theories and applications related to business and the social impact of IT. He is currently serving as the Standards Australia national representative for the development and review of ISO/IEC JTC1/SC7 standards of software engineering. He has published over 80 peer-reviewed articles, including in top-tier journals such as Information and Management, International Journal of Information Management, Technological Forecasting and Social Change, Government Information Quarterly, Computer Standards & Interfaces, and Journal of Knowledge Management. Prior to his academic journey, Anup worked in the IT industry, where his career progressed from programmer to project manager over eight years.

Jeffrey Soar has over 200 peer-reviewed publications as well as other papers, posters, abstracts, and commissioned reports to governments; he has given over 40 invited keynote addresses at national and international events and has attracted grants and commissions to support over \$10M in research. His research interests include smart homes and intelligent assistive technologies, AI development and adoption, and alt-protein and the transition to sustainable agriculture.

Copyright © 2023 by the Association for Information Systems. Permission to make digital or hard copies of all or part of this work for personal or classroom use is granted without fee provided that copies are not made or distributed for profit or commercial advantage and that copies bear this notice and full citation on the first page. Copyright for components of this work owned by others than the Association for Information Systems must be honored. Abstracting with credit is permitted. To copy otherwise, to republish, to post on servers, or to redistribute to lists requires prior specific permission and/or fee. Request permission to publish from: AIS Administrative Office, P.O. Box 2712 Atlanta, GA, 30301-2712 Attn: Reprints, or via email from publications@aisnet.org.
