---
otero_id: 20959
otero_key: "5D4668UM"
title: "A design knowledge management system to support collaborative information product evolution"
authors: "Amrit Tiwana; Balasubramaniam Ramesh"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00134-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A design knowledge management system to support collaborative information product evolution

Amrit Tiwana <sup>a,)</sup>, Balasubramaniam Ramesh <sup>b</sup>

a Goizueta Business School, Emory UniÕersity, Atlanta, GA, USA b Robinson College of Business, Georgia State UniÕersity, Atlanta, GA 30302-4015, USA

## Abstract

The Internet has led to the widespread trade of digital information products. These products exhibit unusual properties such as high fixed costs and near-zero marginal costs. They need to be developed on compressed time frames by spatially and temporally distributed teams, have short lifecycles, and high perishability. This paper addresses the challenges that information product development IPD teams face. Drawing on the knowledge intensive nature of IPD tasks, we identifyŽ . potential solutions to these problems that can be provided by a knowledge management system. We discuss a prototype Knowledge Management System KMS that supports linking of artifacts to processes, flexible interaction and hypermediaŽ . services, distribution annotation and authoring as well as providing visibility to artifacts as they change over time. Using a case from the publishing industry, we illustrate how contextualized decision paths<sup>r</sup>traces provide a rich base of formal and informal knowledge that supports IPD teams. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Information product development; Knowledge management system; Publishing industry; Knowledge integration

## 1. Introduction

The Internet provides the medium and digital information products IPs represent elusive ‘com- Ž . modities’ that have long been the capital market economist’s dream—a marketspace and the product with which several degrees of price discrimination are possible. An unprecedented surge in the trade of information products IPs has resulted from the Ž . widespread adoption of the Internet. Information products consist of a highly interdependent, primarily intangible package of information. They cannot be physically inspected before purchase, and traditional trading mechanisms provide no advantage over electronic ones 34 . The Internet has provided a<sup>w</sup> <sup>x</sup> channel for the distribution and trade of such products at low overhead costs 60 . When distributed<sup>w</sup> <sup>x</sup> over such a medium, their variable cost of production and distribution approaches zero, as the product has no physical form unlike retail packaged soft-Ž ware or non-digital information products . However,. their intangible nature also causes severe competitive market challenges that only worsen because of their low economic cost of reproduction coupled with high fixed costs 34,59 .<sup>w</sup> <sup>x</sup>

The centricity of knowledge in various activities of neo-industrial businesses, including IS organizations, is well recognized in recent research. Knowledge-based activities are increasingly becoming the primary internal function of firms wherein their competencies are largely determined by their ability to manage knowledge work and emergent knowledge assets that eventually drive most productivity gains <sup>w</sup> <sup>x</sup> 16,51 . Knowledge workers and their productivity are indeed the most valuable assets of the 21st century organization 21 . We begin this paper by <sup>w</sup> <sup>x</sup> defining information products and comparing their knowledge-centricity with that of physical products. In Section 2, we analyse characteristics of information products and introduce a case study involving a news publisher caught in the two-way cannibalisation caused by simultaneous distribution of their information product through the Web and in print. In Section 3, we identify largely unprecedented challenges faced by information product development Ž . IPD teams. Section 4 maps characteristics discussed in Section 2 and challenges identified in Section 3 to solutions that can be provided by a knowledge management system. We then describe a design prototype KMS that addresses a select set of problems involved in complex IPD. Using a case study and our prototype, we illustrate how tracking the history of critical decisions, maintenance of traces to context in which decisions are made and maintenance of metadata and lessons learned support the collaborative evolution of an information product in the context of evolving design goals and unstable market needs.<sup>1</sup> We conclude with a discussion of related work in Section 6, and outline the limitations of our work and directions for future research in Section 7.

## 2. An analysis of information products

Examination of the recent literature on information product development and new product development processes reveals several distinguishing characteristics of information products that distinguish them from tangible physical products. In the following discussion, we define information products, introduce the relationship between process knowledge and information products, and list their characteristics, followed by an analysis of the problems that result from these rather distinct characteristics. We draw up on a case study of a specific IPD activity Ž . i.e., the development of a newspaper in our discussion.

## 2.1. Defining information products

An information product is defined as a highly interdependent package of information 23 that is <sup>w</sup> <sup>x</sup> capable of being distributed in digital form 59 .<sup>w</sup> <sup>x</sup> Software engineering products, CD-ROM databases, print-on-demand services, electronic libraries, electronic newspapers, and Web content are examples of such products 42,57 . In economic terms, the fixed <sup>w</sup> <sup>x</sup> costs associated with their production are high and the variable costs are relatively low 73 . If left to the<sup>w</sup> <sup>x</sup> marketplace, the price of an information product will be low due to its low marginal cost of reproduction. Furthermore, because such products are experience goods, their pricing is perceived value-based and not cost-based 60,73 . If consumer perceived value is<sup>w</sup> <sup>x</sup> maximized through robust design and maintenance processes, sustainable increasing economic returns can be generated through self-reinforcing positive network feedback 23,60 . These factors necessitate<sup>w</sup> <sup>x</sup> differentiation among information products, as perfect competition can spell disaster for the producer sŽ . in the product’s markets 42,60 .<sup>w</sup> <sup>x</sup>

## 2.2. IPD as a knowledge intensiÕe actiÕity

Information product markets are dynamic in terms of growth and the pace of new product introduction <sup>w</sup> <sup>x</sup> 42 . Development of information products is a knowledge intensive activity 80 , and products in <sup>w</sup> <sup>x</sup> the information industries have high levels of embedded knowledge content 41 . As a firm gains<sup>w</sup> <sup>x</sup> experience through the development of information products, much of the lessons learned remain captured as information 81,82 . As teams in an organi- <sup>w</sup> <sup>x</sup> zation engage in the development of new products and services, the knowledge about the process of their development needs to be effectively captured and reused 77,79 to support the development of<sup>w</sup> <sup>x</sup> similar or different versions of the product or services. We argue that it is critical to apply lessons learned and reuse critical design decisions made in earlier projects. Effective management of knowledge associated with the development of products and services provides purposeful opportunism to organizations 68,69 . This necessitates a closer examina- <sup>w</sup> <sup>x</sup> tion of the role of knowledge in the development processes and mechanisms for supporting it.

## 2.3. Process knowledge in distributed team structures

Davenport and Prusak 17 point to the subtle<sup>w</sup> <sup>x</sup> difference between knowledge and information, defining knowledge as actionable information. Drucker 20 also introduces the concept of produc-<sup>w</sup> <sup>x</sup> tivity of knowledge, which he indicates is the deciding factor in the competitive position of a company. Drucker further cautions that knowledge is productive only if it is applied to make a difference in processes or tasks such as product development that are critical to the competitive position of an organization. This requires systematic and organized application of existing knowledge 8,26 . Bohn 4 charac-<sup>w</sup> <sup>x</sup> <sup>w x</sup> terizes various incremental levels of knowledge in business organizations along a process-capability continuum. As organisations move up on this process knowledge scale, the development of information products transforms from a process of ad-hoc learning to a systematic process that uses insights gained from past experience. Recent research in production management in publishing and design tasks discusses the importance of this transition from a craft identi-Ž fied by stages 1–4 in Bohn’s 4 process knowledge<sup>w</sup> <sup>x</sup> framework to process orientation as characterized. Ž by stages 5–8 . Bellander 2 cautions that this tran-. <sup>w</sup> <sup>x</sup> sition from a handicraft-based industry to a process industry is not an easy transition. Use of the term ‘handicraft’ emphasises the high level of tacit knowledge in such processes. A large part of underlying process knowledge is ‘totally portable . . . be- <sup>w</sup> cause it is . . . held between the ears of knowledge<sup>x</sup> <sup>w</sup> workers 21 ,’ i.e., held tacitly, but only by the<sup>x w</sup> <sup>x</sup> knowledge workers who posses it. The ability to develop a systematic process orientation largely depends on the ability to support the creation, sharing and use of knowledge.

New information product development often involves cross-functional teams, where different participants join a team with differing viewpoints. Such teams are often characterized by participants who achieve a high level of at-stakeness and synergy from their interactions with other team members <sup>w</sup> <sup>x</sup> 30 . This interaction brings in a need to organize, integrate, filter, condense and annotate the knowledge contributed by the various participants 23 .<sup>w</sup> <sup>x</sup>

Specifically in the context of knowledge that is used in product development, Court 14 proposed<sup>w</sup> <sup>x</sup> three broad categories. Table 1 elaborates on each category of knowledge and its role in IPD.

In the context of this paper, we refer to the collaborative activities involving conceptualisation, articulation and resolution of specialist viewpoints, development of shared understanding, decision making, design option selection and rejection, and the associated modes of reasoning and deliberation as the design process. This process begins with market needs, external information, technological and infrastructural knowledge, and information product requirements brought in by various participants and culminates in the final information product. The design process begins with preconceived notions of the final product held in different forms by team members. As the collective co-evolution of these views through the interaction of tacit and explicit knowledge held by team members is essential for successful IPD, we refer to the outcome as the information product’s evolution rather than development.

2.4. Case study: parallel deÕelopment of a big-city newspaper

A newspaper is released in two different formats —Web and print, typically each morning; occasionally, new editions are released several times each day. This process involves extensive cross-functional collaboration spanning editorial, marketing and sales, advertising and management for the design and development of this information product. Critical layout decisions like the relative placement of the weather sidebar or daily sports scores on the front page requires inputs from a diverse variety of internal and external stakeholders. Further, the product is developed within the span of 1 day and needs to integrate diverse inputs that its correspondents and news feed services such as Reuters provide.Ž .

Table 1  
Categories and role of knowledge in information product development

<table><tr><td>Category</td><td>Characteristics and contribution to IPD</td></tr><tr><td>General knowledge</td><td>Knowledge that people gain through everyday experiences and apply without regard to any specific domain they might be working in. This type of knowledge might have no specific or direct relation with the task domain [14] of IPD.</td></tr><tr><td>Domain specific knowledge</td><td>This type of knowledge is gained through study and experience within a specific domain. Domain specific knowledge is generally improved as the person(s) involved in task domain gain more experience [14]. Since IPD teams are highly cross functional, links to artifacts and processes are needed to share domain specific knowledge [23]. Facilities to help IPD team members make contextual interpretations for decisions outside their domain of expertise [27,63] are critical for the effective use of domain knowledge in IPD.</td></tr><tr><td>Procedural or process knowledge</td><td>This is gained from experience of undertaking a task within the domain. Court [14] suggests that this is a combination of the above two types of knowledge. Procedural or process knowledge therefore includes domain specific knowledge and domain independent knowledge [14,46,68]. Since expertise might be distributed in an information product development team, mechanisms that support coordination and facilities that enhance the understanding of tasks and decisions and their context, bring together existing expertise.</td></tr></table>

Based on our examination of the publishing industry’s information product, it is important to note that development decisions fall into two distinct categories: 1 decisions related to the design, structure, Ž . and layout of the product as associated technical decisions, and 2 decisions about content. We ob- Ž . served that the boundaries between the two are fuzzy because of the inseparable interdependencies between the two. Contrary to popular belief, content selection e.g., how ‘hot’ a news item will be consid-Ž ered among local consumers and design. <sup>r</sup>structure do not necessarily follow a linear progression. Rather, it is the constant switching between the two phases and application of tacit knowledge that produces the final product.

An appropriate balance between what goes into the Web-based version and what goes into the print version is needed so that ‘sales’ of one version are not cannibalized by the other. For example, news content of the print version cannot be cut down extensively since it might affect daily newsstand sales. Cannibalization of print sales due to digital versions of products has been already been extensively observed in the newspaper industry 24 . On<sup>w</sup> <sup>x</sup> the other hand, the print version should not have too much content that the Web version is missing as that might de-motivate future ‘hits’ from potential readers and Website visitors. Besides content and layout issues, the balance of similarities and differences in the design of the print and the Web version of the newspaper are also critical issues 13,65 . Cannibal- <sup>w</sup> <sup>x</sup> ization across different digital and non-digital versions of information products is not encountered merely at an operational level, but also at the level of the underlying business model. Conflicts between business models underlying print and online editions of newspapers, and their inherent cannabilistic outcomes have been a topic of widespread concern in the newspaper publishing industry as observed recently at the 1999 Interactive Newspaper Convention <sup>w</sup> <sup>x</sup> 32 . We use the case study in the following discussions on the characteristics of IP, challenges faced by

IPD teams as well as decision support solutions provided by our research.

## 2.5. Characteristics of information products

## 2.5.1. Unusual economics of production

Information products have unusual economics of production and yet they are subject to the same market and competitive forces that govern the fate of any physical product 59,60 . In a local newspaper, <sup>w</sup> <sup>x</sup> the production of the first copy involves significant costs and effort; these represent the product’s fixed costs. However, every subsequent copy—whether print-or Web-based—has negligible marginal costs. In case of the Web-based version of the newspaper, the marginal cost of additional copies is that of serving the content through a Web Server—close to zero.

## 2.5.2. Timeliness of deliÕery

Timing and timeliness of delivery are more important in the information products industry than in almost any other 60 , and can be a major determi-<sup>w</sup> <sup>x</sup> nant of the product’s value to the consumer 1 .<sup>w</sup> <sup>x</sup> Ballou et al. 1 suggest that a firm can possibly<sup>w</sup> <sup>x</sup> create competitive advantage by delivering an information product in a shorter time-frame than the competitors. In our case study, the success of a newspaper depends on its ability to deliver news content in its final form at a minimum, once every morning. To take an example from the publishing industry, Stephen King’s novel Riding the Bullet was edited, proofed, designed, and delivered electronically within 2 weeks after the author delivered the manuscript 55 . The time frame from product <sup>w</sup> <sup>x</sup> conception to production and delivery spans 24 h in the case of the newspaper with new concessions afforded by subsequent versions that must be released every 24 h.

## 2.5.3. Short product lifecycles

Information products typically enjoy very short lifecycles 11,23,27 and information industries<sup>w</sup> <sup>x</sup> themselves are subject to a fast rate of change 41 . <sup>w</sup> <sup>x</sup> Furthermore, the underlying technologies are improving at a rapid pace, which makes the process lifecycle shorter as well 16 . Therefore, the time<sup>w</sup> <sup>x</sup> available for recouping expenses associated with IPD is compressed. In a Web-based news delivery service run by a local newspaper, the lifecycle of the product is 1 day, after which its economic value approaches zero.

## 2.5.4. Perishability

Perishability refers to the decrease in the value of a product over a period of time. Assessment of the perishability of an information product has to take into account the specific use for that occasion 34 . This supports our earlier argument that the value of an information product can be a time-dependent function. For example, a Web-based news service’s daily content diminishes in value after 1 day.

## 2.5.5. Cross-functional collaboration

In order to respond to competitive challenges and diverse skill sets needed to develop an information product, organizational units have become more closely coupled than in the past, often working in parallel to complete assignments spanning traditional boundaries of functional areas 27,63 . The creation<sup>w</sup> <sup>x</sup> of today’s complex systems of products requires amalgamation of knowledge from diverse disciplines, where creative cooperation is critical for innovation 38 . Analogous to physical product devel-<sup>w</sup> <sup>x</sup> opment that has been classically characterized by intricate interdependencies among areas such as manufacturing, marketing, and packaging, IPD might require collaboration among people with different specializations, affiliations, skill sets, and functional backgrounds 8,64,76 . Knowledge that exists but is<sup>w</sup> <sup>x</sup> not effectively shared within the team leads to product development glitches 25 .<sup>w</sup> <sup>x</sup>

In our example, a critical layout decision such as the placement of the weather forecast requires inputs from editorial, sales, marketing, advertising and weather specialists. These participants need to use their past knowledge of the sales impact of both relative placement of this content on the front-page and the content itself. Building a Web-based pushdelivery news service might need inputs from the technical staff, software coders, hardware specialists who decide on the hardware specifications needed to host such a system, network specialists who provide Web connectivity, creative design artists who work on the aesthetic design aspects and marketing staff who are responsible for generating advertising rev enue.

## 2.5.6. Ease of Õersioning

Versioning—also described as quality discrimination in economics 73 —refers to the ability to<sup>w</sup> <sup>x</sup> produce multiple instantiations of the same basic product for different consumer segments. Physical product manufacturers, including those of complex engineering products, have been able to version products and sell them at different price points. For example, Intel sells two versions of its Pentium II processor—a regular version and a feature disabled one called the Celeron Ž . e . Although these processors are internally identical and cost almost the same to produce, one is sold at a lower price point simply by disabling the internal cache memory section on the chip. Similarly, in information product industries, different versions of the same product can be created to address different market segments. These versions are derived from the same base product. The New York Times archives on the Web is an example: paying customers can retrieve several years of past issues while non-paying advertising supported cus-Ž . tomers can only access the current day’s edition. Consumers with high willingness to pay choose one version, while consumers with lower willingness to pay choose a different version 73 . While functional<sup>w</sup> <sup>x</sup> versioning of physical products can be expensive, relative costs of versioning information products to create artificial differentiation is less expensive 59 . <sup>w</sup> <sup>x</sup> Economists have long wished for a medium that would allow businesses to engage in first-degree price discrimination wherein prices are determined individually for each customer—a scenario made almost possible by Internet information products. Shapiro and Varian 60 suggest several dimensions <sup>w</sup> <sup>x</sup> along which information products can be versioned, as suggested in Table 2.

Examples of such versioning of information products include trial versions of software programs and Web sites that require a payment in order to access full content. Numerous product derivatives can be created from a central repository of sub-components through the process of value subtraction. Customisation and versioning of newspaper content bring to the Web, ‘local content and the unique perspective of the newspaper’ 32 . In case of a newspaper, for example, a common content base can be used to spin off a print version, a Web based version customized for different markets or locations and a CD-ROM archive of news content.

## 2.5.7. Inter-institutional collaboration

As products grow increasingly complex, it is inevitable for multiple organizations to be involved in their development 27 . This brings together partici- <sup>w</sup> <sup>x</sup> pants spanning multiple functional disciplines and specializations from multiple collaborating organizations. Effective collaboration is possible only when shared understanding has been reached among these participants 30 . This necessitates knowledge shar- <sup>w</sup> <sup>x</sup> ing among these participants 63 , and demands<sup>w</sup> <sup>x</sup> excellent coordination among participants in order collectively address the constraints posed by short time-to-market, compressed life-cycles, and design complexity 69 . Furthermore, these teams might be<sup>w</sup> <sup>x</sup> spatially and temporally distributed, necessitating distributed synchronous and asynchronous collaboration 64,70 .<sup>w</sup> <sup>x</sup>

Various dimensions and contributing IP characteristics that facilitate versioning based on Ref. 60Ž <sup>w</sup> <sup>x</sup>.

<table><tr><td>Dimension</td><td>Characteristic of information product</td><td>Examples</td></tr><tr><td>Delay</td><td>Value deterioration with time</td><td>Stock quotes and news content</td></tr><tr><td>User interface</td><td>Level of user expertise involved and functionality desired</td><td>Professional versus basic software versions</td></tr><tr><td>Resolution</td><td>Need to view, print, or publish</td><td>Photographs, clipart, journal papers</td></tr><tr><td>Delivery speed</td><td>Complexity of operations involved</td><td>Same as delay</td></tr><tr><td>Capability</td><td>Specialization involved</td><td>Standard versus specialized voice recognition toolsAcrobat reader (free) versus writer</td></tr><tr><td>Comprehensiveness</td><td>Casual or professional usersLevel of task dependence</td><td>Professional versus basic software versions</td></tr><tr><td>Support</td><td>Price premium for technical help with high-end software versions</td><td>Free technical support minutes bundled</td></tr><tr><td>Advertising</td><td>Negative value associated with mixed messages</td><td>Free ad-supported online services versus paid services</td></tr></table>

In our case study, different sister newspapers belonging to the same parent publishing company collaborate on their news stories. Besides, most newspapers depend on services such as Reuters for their national and international news feeds and weekend and daily comic strips from feature syndicate services. Distributed electronic collaboration is increasingly used in what the publishing industry describes as pre-flighting—developmental electronic proofing—of print information products 55 . Conse-<sup>w</sup> <sup>x</sup> quently, putting together such an information product requires collaboration and coordination among participants in several organizations.

## 2.5.8. Temporary nature of IPD teams

In large development projects, membership of the development team changes both across time and across project phases. As specialized skills are needed, members from within the collaborating organizational units are drawn into the project on an ad-hoc basis and they return to their original units after their tasks are completed 27,51 . Rapid growth<sup>w</sup> <sup>x</sup> in the consumer market and the specialized skill-sets necessary are critical factors contributing to the severe shortage of qualified personnel and high turnover, especially in high technology areas.

## 2.5.9. Uncertainty in eÕolÕing markets

Due to the rapid pace of change and evolution in the information product markets as observed by Ž <sup>w</sup> <sup>x</sup> 42 , organizations involved in information product. development need to cope with high degrees of uncertainty over fundamental issues that normally drive the product development process 43 . Such<sup>w</sup> <sup>x</sup> issues might include the appropriateness of a certain technology standard over another, the nature and extent of customer needs, uncertainty about the level of resources that must be invested and the timing of commitments 43 .<sup>w</sup> <sup>x</sup>

## 2.5.10. Interoperability

An information product may be delivered through a variety of channels. Interoperability among the technologies employed in these channels is a critical for business success. For example, in the case of an electronically delivered newspaper, the development team must take into account mechanisms such as Web browsers, wireless handheld computers, and software platforms as well as networks through which content will be delivered. Conflicts among these technological choices can undermine the very survival of the business 60 .<sup>w</sup> <sup>x</sup>

## 3. Challenges faced by information product development teams

In the following section, we identify key challenges faced by information product development teams. These stem from the lack of shared understanding in diversely structured ad-hoc teams, loss of process knowledge and collaborative synergy due to team fluidity, repetition of mistakes and reinvention of solutions due to inaccessibility of existing design knowledge, versioning inconsistencies, inaccuracy of decisions or lack of shared goals stemming from unstated assumptions, and issues of knowledge-based distributed coordination. We specifically examine these problems in the context of distributed IPD teams collaborating over the Web—an activity that further faces limitations posed by the characteristics of the medium itself 23 . Each problem is identified with a problem code such as XX . The development 4 of a knowledge management system to mitigate these problems is a central focus of our work; the role of IT for supporting knowledge management has been explicitly highlighted in recent literature see Ref.Ž <sup>w</sup> <sup>x</sup> 56 for a review . The goals of the KMS and the. technologies enabling the satisfaction of these goals are mapped to these problems in Section 4.

## 3.1. Lack of shared understanding SU{ }

IPD teams are drawn from different functional areas and streams of expertise 27,63 which bring in<sup>w</sup> <sup>x</sup> differences in understanding, viewpoints, and perspectives of the problems faced throughout the design process 38 . Team members often lack an<sup>w</sup> <sup>x</sup> understanding of the critical design factors affecting areas other than their own. Lack of a common vocabulary and inadequate knowledge of functional areas that do not fall under a participant’s domain create hinder the development of co-evolved understanding and consensus during IPD processes 15,74 .<sup>w</sup> <sup>x</sup>

In our example, there are multiple stakeholders involved in the production of a newspaper. Advertising, editorial and marketing departments need to provide inputs to maximize a common design goal and success metric: improved sales and increased customer value. However, the achievement of these might mean different things to different participants depending on their individual functional background. Therefore, mechanisms to allow the co-evolution of shared understanding are necessary.

## 3.2. Loss of design decision context due to changing team membership LC{ }

Ad-hoc teams formed for new product development are often dissolved at the end of the project <sup>w</sup> <sup>x</sup> 10,39 and team members often are reassigned to other projects where their functional expertise is required 39 . When design decisions are made by<sup>w</sup> <sup>x</sup> IPD teams, recording these decisions without their context is insufficient for subsequent reference 11 .<sup>w</sup> <sup>x</sup> While static teams can partially retain the context of past decisions within their social fabric, recent research suggests that dynamically collated, and often distributed teams employed in IPD face serious difficulties in understanding past decisions in the absence of detailed contextual knowledge 39,71 . Design <sup>w</sup> <sup>x</sup> processes are largely dependent on tacit knowledge possessed by team members. Tacit knowledge manifested in the forms of know-how, judgement and intuition cannot be easily transmitted among team members. The ability to support learning in organizational units and teams is an essential precedent to meaningful transfer and sharing of knowledge between groups 48 . The success of IPD often depends<sup>w</sup> <sup>x</sup> on the effective transfer of the tacit component of knowledge that collaborative information systems do not typically support 17 .

## 3.3. ReinÕention of solutions RS { }

Reinvention is defined as ‘making as if for the first time something already invented’ 75 . Develop-<sup>w</sup> <sup>x</sup> ment teams often reinvent solutions to problems <sup>w</sup> <sup>x</sup> 11,39 due to their lack of awareness of solutions developed in other projects both within and outside the organization 66 . IPD team members might re- <sup>w</sup> <sup>x</sup> peatedly discuss issues that have been resolved earlier, as no reliable record of these deliberations may exist 52 . Court 14 strengthens this argument by <sup>w x</sup> <sup>w x</sup> suggesting that product designers often tend to use incomplete information that they already possess, which results in designs being generated without the benefit of knowledge and expertise that might already exist within the organization.

## 3.4. Repetition of design mistakes RM{ }

Organizations often repeat past mistakes in design decisions 17–19 because they lack episodic knowl- <sup>w</sup> <sup>x</sup> edge of mistakes that might have been made in the past 52,57 . Processes that would support active <sup>w</sup> <sup>x</sup> transfer of knowledge from successful projects to new ones, and mechanisms that facilitate maintaining traces of abandoned, interrupted and failed decisions can potentially reduce the repetition of such mistakes <sup>w</sup> <sup>x</sup> 52 . Retaining and actively applying episodic knowledge facilitates allocation of resources into activities other than previously traced design paths that the IPD design team might simply be unaware of.

To give an overly simplified example, the news design team might have realized that not placing baseball scores on the opening page negatively affects customer satisfaction and<sup>r</sup>or sales in certain seasons. If the design team is unaware that this was a mistake made earlier, say 3 years back, it is at risk to make the same design error again.

## 3.5. Skills deÕeloped due to collaboration may be lost for subsequent use LS{ }

As a design team involved in the development of a successful product is moved to the next high profile project, expertise gained during development of the product is not readily available to design teams working on its subsequent evolutionary versions 54 . The primary obstacle to successful learn-<sup>w</sup> <sup>x</sup> ing from alliances is the lack of specific organizational processes necessary to access, assimilate, and disseminate knowledge such as the organizational memory created in team-based projects 28 . Recent<sup>w</sup> <sup>x</sup> research indicates that the turnover of personnel poses a threat to the collective knowledge and expertise possessed by the group since much of the knowledge is tacit and situated in the minds of the collaborating personnel 44–47 . In contrast, low turnover<sup>w</sup> <sup>x</sup> —an infrequently observed characteristic in high technology industries—allows for the development of organizational knowledge and expertise as well as fostering a high degree of socialization 40 .

## 3.6. Inconsistent Õersioning of design information { } IV

When the same fragment of IPD knowledge such Ž as design artifacts, design decisions etc. is kept at . multiple locations, it is often difficult to identify the correct version 54 . Furthermore, there is no way to<sup>w</sup> <sup>x</sup> guarantee that the information is current unless the upkeep is somehow automated 67 . The need for<sup>w</sup> <sup>x</sup> redundancy suggested in organizational learning literature must be simultaneously balanced with the need for maintaining consistency across different copies of information that may be possessed by different team members 58 . Therefore, knowledge<sup>w</sup> <sup>x</sup> sharing activities must make sure that conflicting versions do not hinder or misdirect organizational learning 9 . <sup>w</sup> <sup>x</sup>

## 3.7. Loss of process knowledge after project completion PK{ }

When a team is disbanded or redistributed, the process knowledge acquired by the team and needed for tasks such as product modification or maintenance, is lost 39,51,52 . Further, collective tacit<sup>w</sup> <sup>x</sup> knowledge that the team collaboratively develops gets redistributed 22 . The larger the extent to which<sup>w</sup> <sup>x</sup> IPD process knowledge has been codified, the lower are the costs of transferring this knowledge across teams 67 . Given the high correlation between codi-<sup>w</sup> <sup>x</sup> fication of knowledge and the cost of its transfer from one group to another 66 , mechanisms that <sup>w</sup> <sup>x</sup> help codify explicable portions of process knowledge can be very helpful in the IPD process.

## 3.8. Unstated assumptions UA { }

Several design decisions made in the process of developing a new product might be based on some technical 52 or procedural 4 assumptions made by<sup>w</sup> <sup>x</sup> <sup>w x</sup> design team participants. Drucker 21 cautions that<sup>w</sup> <sup>x</sup> assumptions are so deeply and subconsciously held by practitioners that they are assumed to be reality and are rarely apparent. These assumptions might be about technologies, markets, end users, scope, and boundaries of work processes. Assumptions made at an early stage in the design process may substantially affect subsequent stages of product design. As the number of decisions grows, their interdependencies become increasingly complex, and it becomes difficult to trace the effects of changes in such assumptions on the rest of the design. Court 14<sup>w</sup> <sup>x</sup> highlights another source of change: the requirements that a product needs to satisfy might also evolve over the period of its development. Iansiti and MacCormack 27 further strengthen this argument <sup>w</sup> <sup>x</sup> by giving the example of Netscape’s development effort for its early browser an information product ,Ž . where the design requirements and underlying assumptions evolved even after the information product development team began building the product. Lacking the ability to trace the effect of a changed assumption on the rest of the design decisions might negatively affect the outcomes of the development effort and in turn success of the product.

In our example of the newspaper IPD team, participants come with different assumptions and biases that are brought in from their respective areas of specialization. The most important design factor for an advertising manager ‘advertisement revenue’Ž . might be different from the editor’s perspective ‘in-Ž formation density’ 13 , which in turn may differ. <sup>w</sup> <sup>x</sup> from the factors considered important by Web developers ‘snazzy’ or content managers ‘sticky con-Ž . Ž tent’ . Whether in advertising supported or fully paid. versions of information products, Turek 72 suggests<sup>w</sup> <sup>x</sup> that there exists a triangle of success Fig. 1 . The Ž . degree to which content meets reader needs drives usage and continued readership. This usage creates a return on investment for the publisher and<sup>r</sup>or advertisers. This in turn justifies renewal and maintenance of content 72 . Meeting reader needs and keeping <sup>w</sup> <sup>x</sup> abreast of changes in reader behaviour—much of which is assumptive—and integrating that knowledge with the redesign process is crucial for success of information products in the electronic publishing industry.

![](/api/attachments/5D4668UM/fulltext/images/97ec71d9512cd3008ec080ddc1bf26466bc8c284608b42c6384a347cbca4c611.jpg)  
Fig. 1. The ‘triangle of success’ model followed in one electronic news publishing business adapted from Ref. 72 . Ž <sup>w</sup> <sup>x</sup>.

## 4. Characteristics of a design knowledge management system to support IPD

In this section, we examine approaches for managing design knowledge to mitigate the problems identified in the previous section. Prior research suggests a variety of options.

v Tracking the history of design decisions 57<sup>w</sup> <sup>x</sup> can help information product designers account for changes in design assumptions and evolving market needs 59 .<sup>w</sup> <sup>x</sup>

v Maintenance of traces for abandoned and interrupted design decisions can help avoid rework <sup>w</sup> <sup>x</sup> 57 .

v Metadata on past decisions can help designers apply and reuse historical lessons learned 23 .<sup>w</sup> <sup>x</sup>

Our work is based on the premise that if knowledge about the history of development is captured and maintained, it can alleviate many of these problems associated with IPD. The challenge then is to represent this knowledge in a way that it supports decision-makers involved in the development of an information product, and in a manner that is neither obtrusive nor imposes high overhead costs. As our research is geared towards developing a KMS for this purpose, it is focused on capturing and representing a slice of such history, viz. knowledge about the decisions made during IPD process. Recent research recognizes that maintaining knowledge about just the decisions themselves is not sufficient to foster shared understanding among IPD participants; the historical context of various decisions must also be maintained <sup>w</sup> <sup>x</sup> 57 .

Table 3  
Enabling technology for design decision support in distributed collaborative IPD

<table><tr><td>Goal [23]</td><td>IPD problems addressed</td><td>Enabling technology for design decision support</td></tr><tr><td>Distributed coordination and design decision making</td><td>{SU},{RS},{RM},{IV}</td><td>All of the below</td></tr><tr><td>Linking artifacts to processes</td><td>{LC},{RM}</td><td>Links between process knowledge and artifacts</td></tr><tr><td>Flexible interaction model and hypermedia services</td><td>{PK},{UA}</td><td>Formal and informal media; hyper-media links to contextual information (including embedded assumptions)</td></tr><tr><td>Distributed annotation</td><td>{SU},{RM}</td><td>Distributed annotation of artifacts with concept maps</td></tr><tr><td>Distributed authoring</td><td>{LS},{IV}</td><td>Distributed authoring of process knowledge and concept maps</td></tr><tr><td>Visibility of artifacts over time</td><td>{LC},{RS},{RM},{PK}</td><td>Recording of design development history/ process knowledge</td></tr></table>

## 4.1. Mapping IPD problems to system goals and characteristics

Recent research on information products proposes several goals for supporting distributed coordination and design decision making in IPD 23 . In Table 3, <sup>w</sup> <sup>x</sup> we identify the problems discussed in Section 3 that can be mitigated by these goals. These goals are then used to provide the foundation for our knowledge management system. Further, we identify technologies that are essential for accomplishing the goals. The first column in Table 3 describes the goals as described by Fielding et al. 23 . IPD challenges <sup>w</sup> <sup>x</sup> from Section 3 are represented by their corresponding codes in the second column. Enabling technologies to support IPD processes are identified in column 3.

4.2. Toward a mechanism for supporting IPD knowledge

We have developed a design decision support system to provide a variety of enabling technologies identified in Table 3. The facilities provided by this system include the following.

v A Web-based collaborative environment in which the various participants can conduct deliberations leading to IPD decisions.

v Facilities for capturing the context in which these decisions are made. Using a distributed multimedia annotation system, the decisions and the rationale for these decisions can be linked to the artifacts, supporting documents and other related information on the WWW.

v A facility to manage the complex network of dependencies among the various components of knowledge often thinly spread across the various participants in collaborative teams.

v A facility for intelligent retrieval of components of design decision knowledge based on ad-hoc requirements of the various participants.

v A mechanism to maintain the consistency of the captured knowledge so that the knowledge is current and accurate.

## 4.3. Linking artifacts to processes

Kline and Saunders 33 stress the importance of<sup>w</sup> <sup>x</sup> integrating tools for supporting collaborative work within the context of the work environment. Our KMS addresses this issue in several ways. We recognize the importance of relating artifacts to the knowledge about the processes that create or modify them Žas suggested by Refs. 26,50 . For example, design <sup>w</sup> <sup>x</sup>. fragments are linked to design decisions that led to their creation. Further, the deliberations among IPD team members that lead to these decisions may also be represented as a component of IPD process knowledge. Other components of this process knowledge may include requirements, issues, alternative solutions considered, assumptions made, etc. For example, conversations may be conducted using the IBIS argumentation model or its extensions such as REMAP 52 . Using our tool, users cannot only<sup>w</sup> <sup>x</sup> capture details of the deliberations, but also maintain links to the artifacts that are the ‘inputs’ and ‘outputs’ of these deliberations. The components of a deliberation on the production different versions of a CD-ROM IPD can have links to the actual code Ž . represented in the HTML format embedded in them. Similarly, a link embedded in the artifacts can be used to retrieve a discussion related to its creation and maintenance. Fig. 2 highlights these facilities provided by our KMS.

4.4. Flexible interaction model and hypermedia ser-Õices

IPD knowledge can be represented in varying degrees of precision or formality. Whereas precise or formal representations are useful for automated reasoning, it is difficult to capture formal knowledge in most complex, dynamic design situations 6 . Infor- <sup>w</sup> <sup>x</sup> mal knowledge, on the other hand, helps create thick descriptions. However, it is difficult to index and retrieve this knowledge. Also, such knowledge is not amenable for reasoning in an automated way. Our approach is to provide flexibility to the IPD team to represent process knowledge in a variety of forms ranging from formal specifications to hypermedia objects. For example, a design specification can be represented formally, whereas, the video<sup>r</sup>audio clips of discussions involving demonstrations of various versions of the IP can be represented using hypermedia. The ability to represent non-formalized knowledge is important because forced explication can lead to the loss of context 6 .

![](/api/attachments/5D4668UM/fulltext/images/24e213f888f7e84eb072338c0ec02e4ee979acec0f8bad333f37298095c8e10f.jpg)  
Fig. 2. Linking artifacts to processes in temporally distributed, collaborative hyperspace.

Depending on the complexity and importance of a decision, the rationale behind it may be captured at different degrees of detail. Our system provides the flexibility to represent decision rationale at different levels of granularity or detail. In the simple view, the users can annotate their decisions with notes and assumptions. In the detailed view, however, they can create a complex network of requirements, issues, alternatives, arguments and assumptions that were critical in arriving at a decision.

## 4.5. Distributed annotation

Boland et al. 5 argue that it is essential to<sup>w</sup> <sup>x</sup> support explicit representations for exchange of views and undertakings among distributed team members. We support explicit representation of ideas and viewpoints using concept maps. These maps can be used by the participants to create detailed representation of the variables used in defining problem and solution spaces. For example, different team members may use different variables to describe how a requirement can be achieved. Further, different members of a team may use the same term with different meanings. The concept maps representing such information can be thought of as annotations 5 explaining the viewpoints of individual participants that contributed to the development of the information product. Consider the scenario in which an editorial staff member proposes a layout of the WWW version of a newspaper that prominently places an editorial segment. This team member may explain the philosophy behind her design by clearly identifying the variables she considers important in prioritizing various segments to be accommodated in the newspaper. This ability to link knowledge about the problems and solutions to the artifacts can be used by the various team members to created distributed annotations on the information products developed collaboratively.

## 4.6. Distributed authorship

Our tool is based on a client server architecture in which clients may be distributed over local or wide area networks. The clients connect to a centralized knowledge base to retrieve, define and modify components of process knowledge and concept maps. This architecture supports distributed authoring by team members.

## 4.7. Visibility of artifacts oÕer time

A major concern with the development of information products is loss of knowledge about the history of the evolution of information products over time, which leads to many of the problems discussed in Section 3. For example, the current layout of an online newspaper can be best understood only if the previous versions of the layout as well as the reasons behind the changes made to the prior versions that led to the current version are readily available. Our system provides the facilities to capture this information about the history of evolution. By capturing the various issues considered, the alternative solutions proposed, the arguments supporting and opposing each of these alternatives and the assumptions behind each of these, the designers can explicitly articulate the rationale behind the evolution of their artifacts over time.

In Section 5, we describe our prototype KMS that illustrates the characteristics discussed above.

## 5. Functionalities of KMS for IPD

Our KMS provides facilities for defining, browsing and modifying knowledge about the history of development of information products. We illustrate the capabilities of the system using scenarios on the development of various versions of an online newspaper.

![](/api/attachments/5D4668UM/fulltext/images/1408fceca34c9ba8f9e8ef38bb41f5dcf34388bb4677bfdc8b34f334ffb1e1ce.jpg)  
Fig. 3. A design decision discussion with two-way links between artifacts.

## 5.1. Linking artifacts to processes

Consider the situation in which a team of developers is involved in designing the layout of the newspaper. Several participants contribute to this important decision. They include the editors in charge of the various sections such as sports, business, technology, etc., as well as functional areas such as marketing that is responsible for the sale of the paper and advertising that is responsible for generating advertisement revenues. Discussions among these team members may be conducted using our tool. Fig. 3 shows the results of such a discussion. The discussion centers on the requirements for designing the front page of the layout. Some of concerns or issues that are raised by the team members include the following.

v Does information about weather belong in the front page?

v Does information on sports scores belong in the front page?

Each of these issues in turn may lead to more specific questions such as where in the front page will the weather information be? How much space should be allocated in the front page for the weather information? The team members involved in the weather section may propose alternative solutions. For example, a team member suggests that this segment belongs in the banner, based on the argument that it will provide high visibility. This argument is based on the assumption that the target audience desires such a high visibility placement of weather. Similarly, other team members propose different alternatives. Any team member may also suggest their reasons for supporting or opposing the proposed alternatives. As mentioned in Section 4.3, such a deliberation can be conducted using our tool. Fig. 3 shows the results of a structured conversation, conducted using the REMAP model 52 . In such<sup>w</sup> <sup>x</sup> conversations any team member can raise issues or questions, suggest alternative solutions to solve the issues, provide arguments supporting and objecting to the various alternatives and identify critical assumptions that need to be explicitly understood. Our tool provides the ability for the IPD to define any such model of conversation by specifying the nodes and links representing the knowledge componentsŽ and the legal moves, respectively . Fig. 3 also shows. a fragment of a discussion on the placement of sports scores. Each of the proposed alternatives has a direct effect on the final layout to be chosen. Based on the evaluation of the various alternatives to be dis-Ž cussed in more detail below the team makes a. decision to choose one of the alternatives. Our tool provides the ability to hyperlink this decision to the corresponding layout design. Thus, the rich history behind the choice of the layout is captured in detail and linked to the artifact itself.

A field study 78 established the feasibility and<sup>w</sup> <sup>x</sup> usefulness of capturing conversations such as those illustrated in Fig. 3 in complex IPD activities. However, any complex problem solving activity such as IPD will involve the use of a variety of tools such as groupware systems and email to facilitate informal and formal interactions, synchronously as well as asynchronously. Integration of our KMS with such sources of knowledge is essential for non-intrusive capture of IPD history. The capture and maintenance of IPD history can be very expensive. Therefore, non-intrusive capture of this information is essential for the successful adoption of our KMS. We illustrate such integration with an example on the capture of process knowledge from electronic mail exchanges.

Fig. 4 shows the output of an email exchange among the members of the IPD team. A team member is reviewing an email that addresses the issue of placement of weather information on the front page of the newspaper. While using her familiar tool for such exchanges Microsoft Outlook, in this case ,Ž . she highlights a portion of a mail message as relevant for the focused discussion that was illustrated in Fig. 3. Notice that the Microsoft Outlook window has a customized toolbar with the following options: Set Connection, Copy to REMAP, Extract Requirement, etc. Our system provides such an interface to the knowledgebase containing IPD design history knowledge illustrated in Fig. 3 from common pro- Ž . ductivity tools such as Microsoft Office. Using the customized toolbar from these tools, a user can connect to the knowledgebase, highlight and copy information text, spreadsheets, database tables, etc.Ž . and ‘send’ them to the knowledgebase. In our example, the user highlights text corresponding to the argument about following the competitor’s strategy and sends it to the knowledgebase. In a subsequent synchronous or asynchronous meeting with the tool Ž shown in Fig. 3 this fragment of process knowledge. can be linked to other relevant pieces to provide complete traceability to the various components of the discussion. Such a facility, while enabling users to work within their familiar environments, also helps incrementally acquire knowledge about IPD process.

![](/api/attachments/5D4668UM/fulltext/images/4fdd50d9f69b0e25312e860cc269974e6fe2159bf0c726906582c56117a9fb72.jpg)  
Fig. 4. Capturing knowledge fragments from e-mail messages.

Thus, our approach also recognizes the importance of relating IPD process knowledge to the artifacts that are the outcomes of the process. Specifically, various knowledge components in our semi-structured process knowledgebase such as as-Ž sumptions and decisions are linked to the products. produced during IPD. Further, our approach supports a wide spectrum of representations from formal toŽ hypermedia to facilitate the capture of process .

knowledge in its most natural and useful form. This is similar in spirit to the call for representing artifact evolution as a component of rationale advocated in the DICE project 49 . Our efforts at providing a<sup>w</sup> <sup>x</sup> customizable environment in which different primitives could be used for conducting conversations are a first step towards this goal.

## 5.2. Flexible representation and hypermedia

In the above scenario, the representation of history behind design decisions was guided using the primitives of an extended issue-based information system model 12,52 . However, the tool provides <sup>w</sup> <sup>x</sup> the flexibility to customize the representation in a number of ways. First, simply changing the schema that represents the nodes and links in the model of collaboration may use a different conversation protocol. Second, we recognize that a team may wish to represent the history behind decisions at varying levels of detail or granularity. The discussion in Fig. 3 represents a very detailed model. Instead, the users may switch to a simple model in which only the decision and the assumptions may be recorded. By providing this flexibility, the tool enables the capture of history at the desired level of detail. Two-way linking between the artifacts and the design history is provided by the ability to embed the reference to any specific discussion within any hypermedia document. For example, various segments of a layout represented in the hypermedia format may have references to the discussions corresponding to that choice. A user can therefore seamlessly move from the discussion to the artifact and vice versa.

The need to represent the context in which decisions are made is supported by the ability to hyperlink any component in the knowledgebase any hypermedia document. For example, the alternative of using a weather strip at the bottom of the page may be supported by the argument that it is the format employed by a competing publication. A hyperlink to that publication may be created to completely capture the context in which this argument was made Ž . see Add Node Form in Fig. 3 .

## 5.3. Distributed annotation

Our KMS supports distributed annotation with concept maps. Recall that the concepts to be used to help communicate different viewpoints may be specified by the team members. For example, a team may use decision criteria as the concept of interest. Each member of the team involved in layout design may describe the various variables that they consider as important in arriving at a layout. Marketing and Advertising may mention that attractive design and potential for increased advertising revenues are their top priorities, respectively. The other team members may seek clarifications on these concepts to fully understand the viewpoints. Marketing may elaborate on its choice and mention that the use of color and rich media enhance the attractiveness of the design. Similarly, other team members may use this facility to specify their choices and elaborate on them. This ability to exchange viewpoints enhances the chances for developing shared understanding among team members, which is essential for successful collaboration.

## 5.4. Distributed authoring

Our prototype KMS supports distributed development of information products with a client server architecture. The clients can be invoked from a Web browser. IPD team members using the client interface can connect to a central knowledge server that maintains process knowledge components. This facilitates distributed authoring of design history and concept maps by the team members.

Fig. 5 illustrates the use of the KMS in conjunction with Netmeeting, a collaboration support environment. The IPD team is using the ‘chat’ utility of Netmeeting to discuss the position of the weather segment in the front page. A team member who suggests positioning weather in the banner, displays the competitor’s design by bringing it up on his web browser and sharing this application with other participants. Our KMS complements Netmeeting’s ability to support conversations and share applications in a number of ways. The essential aspects of unstructured conversations conducted within Netmeeting, can be captured within our tool in a semi-structured format. Segments of the conversations can be directly imported into the nodes in our network of IPD history. Further, the artifacts themselves can be twoway linked to the contents of the conversations. As mentioned earlier, the competitor’s Web page can be linked to the argument made by the team member, the decision resulting from the discussion as well as the final layout.

## 5.5. Decision support with Õisibility of artifacts oÕer time

Our tool provides a variety of decision support aids to not only capture knowledge about the history of development, but also to maintain the consistency of such knowledge and perform automated decision support with that knowledge, especially when the context in which the decisions are made changes. For example, the validity of the alternatives proposed also depends on the validity of the assumptions behind these alternatives. Simon suggests that all stakeholders involved in the delivery of a product must be involved from its inception 62 . He gives an <sup>w</sup> <sup>x</sup> example of manufacturing industries where failure to consider manufacturability at an early stage usually causes extensive redesign with a product, thereby causing major delays in production and subsequent delivery.

Consider the placement of the banner for weather based on the assumption that the customer market segment desires such a high visibility placement. The marketing department may be asked to evaluate this assumption. If they invalidate this assumption, then its effect is to invalidate the decision. Our KMS automates the process of maintaining such dependencies. Similarly, the evaluation of the assumption about the current interest in the sports segment may lead to the validation of the alternative to use the banner for sports scores. This ability to dynamically synthesize the layout based on IPD history can be very valuable in a variety of ways. For example, two editions of the same paper produced in different cities may be composed with different layouts based on their specific conditions while sports may be theŽ top priority for a city in Southern California currently hosting a sporting event, weather may be the most appropriate item for the front-page banner for a city in the north east facing a major storm . First, our . KMS helps in synthesizing these designs based on a common and consistent set of design principles discussed by the team members. Second, when the context in which the decisions are made changes

![](/api/attachments/5D4668UM/fulltext/images/bf32f900ba06fa334e4b050b7d551d5dbc688d59e81f4e30744f3b2d8d400485.jpg)  
Fig. 5. Distributed authoring, links to external knowledge sources in this case, a competitor’s site and synchronous deliberations can be Ž . captured and linked to design decisions as they are made.

Žwhich is common in the development of information products like an online newspaper where new stories of high importance may develop at any time ,. the KMS helps in automatically identifying components of the design that are valid. Finally, the history of the development of the information product is captured in its complete form so that the teams will have access to this information when designing other versions of the product. Our system supports ad-hoc queries to retrieve components of this history to support decision-making. For example, a design team may want to review what the layout looked like when similar conditions existed in the past and more importantly, why so? The ability to access and reuse such information will be extremely valuable.

## 6. Related work

Research on supporting groupwork can be classified into two categories: research that emphasizes supporting the communication aspects of group decision making 35 and efforts that emphasizes provid-<sup>w</sup> <sup>x</sup> ing analytical support for group decision making 7 . Our research addresses both aspects to provide collaborative group decision support.

Systems that aim to support communication focus on supporting information structuring and exchange rather than on reasoning with the information. Their emphasis is on capture and communication of information, rather than providing intelligent decision support with the captured and exchanged information <sup>w</sup> <sup>x</sup> 35 .

Systems that attempt to provide analytical decision support to groups, such as those that employ decision theoretic models assume the decision problem and the alternative ways of solving the problem are well understood and the consequences of choosing one or more alternatives are clearly known 7 . In<sup>w</sup> <sup>x</sup> contrast, we argue in group decision making situations, the identification and elaboration of goals orŽ selection criteria and alternatives that resolve the. issues is very critical for arriving at a consensus or group solution often leads to controversies and deliberations to resolve them. Our work is based on the premise that the process of elaboration and refinement of the issues, alternatives and decision criteria itself is an important component of the problem solving and may guide a group towards a solution. In this respect, our work is similar to many group support systems that support argumentation models.

Many tools for capturing design rationale use argumentation models such as issue based information systems gIBIS 12 . Tools such as gIBIS 12<sup>w x</sup> <sup>w x</sup> and IBE 36 provide only passive support for the <sup>w</sup> <sup>x</sup> capture of rationale. In contrast, we advocate active support for both capture and use of history. In providing automated reasoning tools, the goals of our work are similar to those of the SYBYL project 37 .<sup>w</sup> <sup>x</sup> Our work significantly differs from other argumentation model based systems in that it is capable of supporting any user-defined model of argumentation. The ConceptBase system 29,31 provides a robust <sup>w</sup> <sup>x</sup> infrastructure for defining arbitrary meta-models and their instantiations and supports powerful inferencing mechanisms. In comparison, our current implementation is geared towards providing services specific to the task of supporting knowledge management in IPD.

In addition, we provide a mechanism for distributed coordination with annotation and authoring, as well as support linking artifacts and IPD history. The need for hypermedia annotation of artifacts has been suggested by prior research 3 . Our approach is<sup>w</sup> <sup>x</sup> more comprehensive as it also helps document detailed design history in a semi-structured way so that automated support for the use of this information can be provided. Further, our research differs from earlier work on the capture of semi-structured history information exemplified by tools that support IBIS and its extensions 12,52 due to its focus on provid-<sup>w</sup> <sup>x</sup> ing a tight integration between the IPD history knowledge and the IP themselves. In the domain of information product development, the tight integration between the process knowledge components and artifacts themselves can be very valuable in rapidly evolving different versions of the product. Further, the synthesis of a design solution can readily be supported when the context for the design decisions changes. Thus, the focus of decision support in the current research is the synthesis of information products. In contrast, prior research has concentrated on providing access to passive design. The scope for opportunistic planning and synthesis are high in IPD <sup>w</sup> <sup>x</sup> 57 and our decision support tools are geared towards supporting these activities. Recent studies on the use of structured argumentation techniques to capture organizational memories suggests that complex models are appropriate for some ‘wicked’ problems whereas simpler schemes are more appropriate for other contexts. This finding supports our approach of capturing and using IPD history at multiple levels of abstraction or detail. Though the WWW has emerged as an important medium for the production and delivery of information products, the current WWW infrastructure has several missing elements for the development of annotation systems 23 . We <sup>w</sup> <sup>x</sup> have proposed an annotation system that complements the capabilities currently available on the WWW.

Learning from history is an important focus of organizational memory systems that help in the acquisition and management of such organizational memory. Our research emphasizes knowledge sharing to support such learning. In this respect, our approach is similar in spirit to that employed in the NEST project 61 . The knowledgebase of semi-<sup>w</sup> <sup>x</sup> structured experiential knowledge is an excellent candidate for the use of induction and case based reasoning approaches CBR to learning. Recent re- Ž . search indicates that integration of induction and CBR can be very effective. In contrast to this work focusing on the use of captured knowledge, our work also addresses the automated capture of IPD history. As a first step, our research uses concept-learning techniques to learn concept descriptions from past experiences of commonly occurring design situations.

## 7. Limitations and future work

Capture of knowledge about the history of development can be very expensive. However, studies in the domain of software engineering e.g., Ref. 78 Ž <sup>w</sup> <sup>x</sup>. document the feasibility and usefulness of such efforts even in large-scale projects. Even in domains where the tight integration of design process knowledge and the artifacts can be expensive, the benefits of maintaining comprehensive design history have been observed 53 . In the context of IPD, the bene-<sup>w</sup> <sup>x</sup> fits of IPD history knowledge can be significantly higher. Bellander 2 notes that such a process-ori-<sup>w</sup> <sup>x</sup> ented approach to publishing is generalizable to a certain level of granularity for all companies developing information products. While our case study involved only scenarios on layout and content design issues in the development of information products, it can also be applied to other IPD processes such as color configuration in the product planning stages, ‘repurposing’ components of an information product and distribution 2 . However, detailed empirical<sup>w</sup> <sup>x</sup> studies to establish the effectiveness of the approach proposed here is the subject of ongoing research.

We are also exploring ways to support the non-intrusive capture of process knowledge with mechanisms such as automated classification of group meeting transcripts collected from group support systems and electronic mail messages. Such automated support for the capture and use of IPD history knowledge is likely to greatly enhance usefulness of the KMS. We seek to provide stakeholders in IPD with comprehensive support tools for facilitating effective groupwork.

## Acknowledgements

This research was sponsored in part by a grant from the National Science Foundation, the Defence Acquisition University EARP, Office of Naval Research Project on Engineering of Complex Systems project of the NSWCDD and the Air Force Research Laboratory.

## References

<sup>w</sup> <sup>x</sup> 1 Ballou, Wang, Pazer, Tayi, Modeling information manufacturing systems to determine information product quality, Management Science 44 4 1998 462–484.Ž . Ž .

<sup>w</sup> <sup>x</sup> 2 M. Bellander, Workflow bottlenecks and problem areas influencing production management need in commercial printing, Proceedings of Intergrafica, Zagreb, Croatia, 1997.

<sup>w</sup> <sup>x</sup> 3 H. Bhargava, R. Krishnan, A. Whinston, On integrating collaboration and decision technologies, Journal of Organizational Computing 3 4 1994 297–317.Ž . Ž .

<sup>w</sup> <sup>x</sup> 4 R.E. Bohn, Measuring and managing technological knowledge, Sloan Management Review 36 1994 61–73.Ž .

<sup>w</sup> <sup>x</sup> 5 J. Boland, R. Tenkasi, D. Te’eni, Designing information technology to support distributed cognition, Organization Science 5 3 1994 456–477.Ž . Ž .

<sup>w</sup> <sup>x</sup> 6 J.S. Brown, P. Dugid, Balancing act: how to capture knowledge without killing it, Harvard Business Review 2000Ž . 3–7, May–June.

<sup>w</sup> <sup>x</sup> 7 T. Bui, Coop: A Group Decision Support System for Cooperative Multiple Criteria Group Decision Making, Springer, Berlin, 1987.

<sup>w</sup> <sup>x</sup> 8 J. Carrillo, C. Gaimon, Improving manufacturing performance through process change and knowledge creation, Management Science 46 2 2000 263–288.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 A. Chang, M.E. Jackson, Managing Resource Sharing in the Electronic Age, AMS Studies in Library and Information Science 4, AMS Press, New York, 1996.

<sup>w</sup> <sup>x</sup> 10 C. Ciborra, Teams, Markets, and Systems: Business Innovation and Information Technology, Cambridge Univ. Press, Cambridge, 1993.

<sup>w</sup> <sup>x</sup> 11 K.B. Clark, S.C. Wheelwright, The Product Development Challenge: Competing Through Speed, Quality, and Creativity, Harvard Business School Press, Boston, 1994.

<sup>w</sup> <sup>x</sup> 12 J. Conklin, M. Begeman, Gibis: a hypertext tool for exploratory policy discussion, ACM Transactions on Office Information Systems 6 1988 303–331.Ž .

<sup>w</sup> <sup>x</sup> 13 L. Cottrell, A. Faulkner, Print Publishing Guide, Adobe Press, San Francisco, 1998.

<sup>w</sup> <sup>x</sup> 14 A.W. Court, The relationship between information and personal knowledge in new product development, International Journal of Information Management 17 2 1997 123–138.Ž . Ž .

<sup>w</sup> <sup>x</sup> 15 E.Y. Cross, M.B. White, The Diversity Factor: Capturing the Competitive Advantage of a Changing Workforce, Irwin, Chicago, 1996.

<sup>w</sup> <sup>x</sup> 16 T.H. Davenport, Process Innovation: Reengineering Work Through Information Technology, Harvard Business School Press, Boston, 1993.

<sup>w</sup> <sup>x</sup> 17 T.H. Davenport, L. Prusak, Working Knowledge: How Organizations Manage What They Know, Harvard Business School Press, Boston, 1998.

<sup>w</sup> <sup>x</sup> 18 P.M. Dillon, The Quest for Knowledge Management: A New Service Organization to Address the Challenges and Opportunities, Technology Research Report T-303, Information Management Forum, Atlanta, 1997.

<sup>w</sup> <sup>x</sup> 19 R.J. Dolan, Managing the New Product Development Process: Cases and Notes, Addison-Wesley, Reading, 1993.

<sup>w</sup> <sup>x</sup> 20 P. Drucker, Post Capitalist Society, Harper Business Press, New York, 1993.

<sup>w</sup> <sup>x</sup> 21 P. Drucker, Management Challenges for the Twenty-first Century, Harper Business Press, New York, 1999.

<sup>w</sup> <sup>x</sup> 22 L. Fahey, L. Prusak, The eleven deadliest sins of knowledge management, California Management Review 40 3 1998Ž . Ž . 265–276.

<sup>w</sup> <sup>x</sup> 23 R. Fielding, Whitehead, Anderson, Web-based development of complex information products, Communications of the ACM 41 8 1998 84–92.Ž . Ž .

<sup>w</sup> <sup>x</sup> 24 M. Gunther, Publish or Perish? Fortune 2000 141–154,Ž . January 10.

<sup>w</sup> <sup>x</sup> 25 D. Hoopes, S. Postrel, Shared knowledge, ‘glitches,’ and product development performance, Strategic Management Journal 20 1999 837–865.Ž .

<sup>w</sup> <sup>x</sup> 26 M. Iansiti, How the incumbent can win: managing technological transitions in the semiconductor industry, Management Science 46 2 2000 169–185.Ž . Ž .

<sup>w</sup> <sup>x</sup> 27 M. Iansiti, A. Maccormack, Developing Products on Internet Time, Harvard Business Review 1997 108–117, Septem-Ž . ber–October.

<sup>w</sup> <sup>x</sup> 28 A. Inkpen, Creating knowledge through collaboration, California Management Review 39 1 1996 123–140.Ž . Ž .

<sup>w</sup> <sup>x</sup> 29 M. Jarke, R. Galersdoerfer, M. Jeusfeld, M. Staudt, S. Eherer, Conceptbase—a deductive object base for metadata management, Journal of Intelligent Information Systems 5 2 1995Ž . Ž . 167–192.

<sup>w</sup> <sup>x</sup> 30 A.R. Jassawalla, H.C. Sashittal, An examination of colloboration in high technology new product development process, Journal of Product Innovation Management 15 1998 237–Ž . 254.

<sup>w</sup> <sup>x</sup> 31 M. Jeusfeld, M. Jarke, H. Nissen, M. Staudt, Conceptbase— managing conceptual models about information systems, in: P. Bernus, K. Mertins, G. Schmidt Eds. , Handbook onŽ . Architectures of Information Systems, Springer, New York, 1998, pp. 265–285.

<sup>w</sup> <sup>x</sup> 32 F. Katz, Digital age challenges acknowledged at interactive newspapers conference, Atlanta Journal of Constitution Ž . 1999 March 19.

<sup>w</sup> <sup>x</sup> 33 P. Kline, B. Saunders, Ten Steps to a Learning Organization, 2nd edn., Great Ocean Publishers, Arlington, 1998.

<sup>w</sup> <sup>x</sup> 34 Koppius, Dimensions of intangible goods, Proceedings of 32nd Hawaii International Conference on System Sciences, 1999.

<sup>w</sup> <sup>x</sup> 35 K. Kraemer, J. King, Computer-based systems for cooperative work and group decision making, ACM Computing Surveys 20 1988 115–146.Ž .

<sup>w</sup> <sup>x</sup> 36 M. Lease, M. Lively, J. Leggett, Using an issue-based hypermedia system to capture the software lifecycle process, Hypermedia 2 1 1990 . Ž . Ž .

<sup>w</sup> <sup>x</sup> 37 J. Lee, Sybil: a qualitative decision management system, in: Whinston, Shellard Eds. , Artificial Intelligence at MIT:Ž . Expanding Frontiers, MIT Press, Cambridge, 1990.

<sup>w</sup> <sup>x</sup> 38 D. Leonard-Barton, S. Sensiper, The role of tacit knowledge in group innovation, California Management Review 40 3Ž . Ž . 1998 112–131.

<sup>w</sup> <sup>x</sup> 39 D. Mankin, S. Cohen, T. Bikson, Teams and Technology, Harvard Business School Press, Boston, 1996.

<sup>w</sup> <sup>x</sup> 40 J.G. March, The Pursuit of Organizational Intelligence, Blackwell, Malden, 1999.

<sup>w</sup> <sup>x</sup>41 H. Mendelson, K. Kraemer, The information industries: introduction to the special issue, Information Systems Research 9 4 1998 1–4.Ž . Ž .

<sup>w</sup> <sup>x</sup> 42 M. Meyer, M. Zack, The design and development of information products, Sloan Management Review 37 3 1996Ž . Ž . 43–59.

<sup>w</sup> <sup>x</sup> 43 Mullins, Sutherland, New product development in rapidly changing markets: an exploratory study, Journal of Product Innovation Management 15 1998 224–236.Ž .

<sup>w</sup> <sup>x</sup> 44 I. Nonaka, Managing innovation self-renewing process, Journal of Business Venturing 4 1989 299–315.Ž .

<sup>w</sup> <sup>x</sup> 45 I. Nonaka, N. Konno, The concept of ‘Ba’: building a foundation for knowledge creation, California Management Review 40 3 1998 40–55.Ž . Ž .

<sup>w</sup> <sup>x</sup> 46 I. Nonaka, H. Takeuchi, The Knowledge-Creating Company: How Japanese Companies Create the Dynamics of Innovation, Oxford Univ. Press, New York, 1995.

<sup>w</sup> <sup>x</sup> 47 Nonaka, Reinmoeller, Senoo, The ART of knowledge: systems to capitalize on market knowledge, European Management Journal 16 6 1998 673–684.Ž . Ž .

<sup>w</sup> <sup>x</sup> 48 C.S. O’Dell, APQC International Benchmarking Clearinghouse and American Productivity and Quality Center, Knowledge Management: Consortium Benchmarking Study Final Report American Productivity and Quality Center,Ž Houston, 1996 ..

<sup>w</sup> <sup>x</sup>49 E. Pena-Mora, D. Sriram, R. Logcher, SHARED-DRIMS: shared design recommendation-intent management system, Proceedings of Second Workshop on Enabling Technologies: Infrastructure for Collaborative Enterprises, Morgantown, WV, 1993.

<sup>w</sup> <sup>x</sup>50 J. Pfeffer, R. Sutton, Knowing ‘what’ to do is not enough: turning knowledge into action, California Management Review 42 1 1999 83–108.Ž . Ž .

<sup>w</sup> <sup>x</sup> 51 J.B. Quinn, P. Anderson, S. Finkelstein, Managing professional intellect: making the most of the best, Harvard Business Review 1996 71–80, March–April.Ž .

<sup>w</sup> <sup>x</sup> 52 B. Ramesh, V. Dhar, Supporting systems development using knowledge captured during requirements engineering, IEEE Transactions on Software Engineering 18 6 1992 498–510.Ž . Ž .

<sup>w</sup> <sup>x</sup> 53 B. Ramesh, K. Sengupta, Multimedia in a design rationale decision support system, Decision Support Systems 15 1995 Ž . 181–196.

<sup>w</sup> <sup>x</sup> 54 B. Ramesh, A. Tiwana, Supporting collaborative process knowledge management in new product development teams, Decision Support Systems 27 1–2 1998 213–235.Ž . Ž .

<sup>w</sup> <sup>x</sup> 55 B. Reimers, New technologies transform publishing industry, Informationweek 2000 138–144, March 27.Ž .

<sup>w</sup> <sup>x</sup> 56 D. Robey, M. Boudreau, G. Rose, Information technology and organizational learning: a review and assessment of research, Accounting, Management, and Information Technology 10 2000 125–155.Ž .

<sup>w</sup> <sup>x</sup> 57 J. Robillard, The role of knowledge in software development, Communications of the ACM 42 1 1999 87–92.Ž . Ž .

<sup>w</sup> <sup>x</sup> 58 R. Sanchez, A. Heene, Strategic Learning and Knowledge Management, Wiley, Chichester, 1997, The Strategic Management Series.

<sup>w</sup> <sup>x</sup> 59 C. Shapiro, H. Varian, Versioning: The smart way to sell information, Harvard Business Review 1998 16–114,Ž . November–December.

<sup>w</sup> <sup>x</sup> 60 C. Shapiro, H. Varian, Information Rules: A Strategic Guide to the Network Economy, Harvard Business School Press, Boston, 1999.

<sup>w</sup> <sup>x</sup> 61 M. Shaw, M. Fox, Distributed artificial intelligence for group decision support, Decision Support Systems 9 1993 349–Ž . 367.

<sup>w</sup> <sup>x</sup> 62 H.A. Simon, Bounded rationality and organizational learning, Organization Science 2 1 1991 125–134.Ž . Ž .

<sup>w</sup> <sup>x</sup> 63 M. Song, M. Montoya-Weiss, Critical development activities

for really new versus incremental products, Journal of Product Innovation Management 15 1998 124–135. Ž .

<sup>w</sup> <sup>x</sup> 64 J. Storck, P. Hill, Knowledge diffusion through ‘Strategic Communities’, Sloan Management Review 2000 63–74, Ž . Winter.

<sup>w</sup> <sup>x</sup> 65 Techart, Digital Prepress Book for Macintosh Power User Designers, vol. 1, Techart Japan, Tokyo, 1993.

<sup>w</sup> <sup>x</sup> 66 D. Teece, Research directions for knowledge management, California Management Review 40 3 1998 289–292.Ž . Ž .

<sup>w</sup> <sup>x</sup> 67 R.E. Teigland, C. Fey, J. Birkinshaw, Knowledge Dissemination in Global R&D Operations: Case Studies in Three Multinationals in the High Technology Electronics Industry, Stockholm School of Economics, 1998.

<sup>w</sup> <sup>x</sup>68 A. Tiwana, The Knowledge Management Toolkit: Practical Techniques for Building a Knowledge Management System, Prentice Hall, New Jersey, 2000.

<sup>w</sup> <sup>x</sup> 69 A. Tiwana, Managing micro- and macro-level design process knowledge across emergent internet information system families, in: R. Rajkumar Ed. , Industrial KnowledgeŽ . Management: A Micro Level Approach, Springer, London, 2000.

<sup>w</sup> <sup>x</sup> 70 A. Tiwana, A. Bush, Peer-to-peer valuation as a mechanism for reinforcing active learning in virtual communities: an application of social exchange theory, Proceedings of HICSS-33, Hawaii, IEEE Press, 2000.

<sup>w</sup> <sup>x</sup> 71 D. Tjosvold, M.M. Tjosvold, Leading the Team Organization: How to Create an Enduring Competitive Advantage, Macmillan, Toronto, 1991, Issues in Organization and Management Series.

<sup>w</sup> <sup>x</sup> 72 N. Turek, Publisher’s goal: become a powerful portal player, Informationweek 2000 168–172, March 27.Ž .

<sup>w</sup> <sup>x</sup> 73 H. Varian, Versioning information goods, Proceedings of Digital Information and Intellectual Property, Cambridge, MA, 23–25 January, 1997, pp. 1–13.

<sup>w</sup> <sup>x</sup> 74 A. Webber, What’s so new about the economy, Harvard Business Review 1993 4–11, January–February.Ž .

<sup>w</sup> <sup>x</sup> 75 M. Webster, Merriam Webster Dictionary on the Web Http:<sup>rr</sup>Www.M-W.Com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 76 P. Windrum, M. Tomlonson, Knowledge-intensive services and international competitiveness: a four country comparison, Technology Analysis and Strategic Management 11 3Ž . Ž . 1999 391–405.

<sup>w</sup> <sup>x</sup> 77 W. Wong, Management Guide to Software Reuse, NBS Special Publication, Nbs, Gaithersburg, MD, 1988, pp. 100– 155.

<sup>w</sup> <sup>x</sup>78 K.B. Yakemovic, E.J. Conklin, Report on a development project use of issue-based information system, Proceedings of Computer-Supported Cooperative Work, 1990, pp. 105– 118.

<sup>w</sup> <sup>x</sup> 79 K.P. Yglesias, Information reuse parallels software reuse, IBM Systems Journal 32 4 1993 615–620.Ž . Ž .

<sup>w</sup> <sup>x</sup> 80 M. Zack, Electronic publishing: a product architecture perspective, Information and Management 31 1996 75–86.Ž .

<sup>w</sup> <sup>x</sup> 81 M. Zack, An architecture for managing explicated knowledge, Sloan Management Review 1999 45–58, Summer.Ž .

<sup>w</sup> <sup>x</sup> 82 M.H. Zack, Developing a knowledge strategy, California Management Review 41 3 1999 125–145.Ž . Ž .

![](/api/attachments/5D4668UM/fulltext/images/ba62ba9ea133a4ad3b373498d5cb3e91206d1ae4950742a72c1e995fe420e923.jpg)

Amrit Tiwana is finishing up his doctoral work in the Computer Information Systems department at Robinson College of Business at Georgia State University. In August 2001, he begins his appointment as an Assistant Professor at Goizueta Business School at Emory University. His research interests include knowledge management in innovative e-business projects and knowledge integration in business networks. In addition to his journal and conference

papers, he has authored The Knowledge Management Toolkit Ž .Prentice Hall, 2000 . He is a member of the Academy of Management, the IEEE, and the ACM.

![](/api/attachments/5D4668UM/fulltext/images/5dfa7faabcdc9d7dcff97b7c20925e528c109e7bd6de80ddb0bf48bc1d5837a3.jpg)

Balasubramaniam Ramesh is Associate Professor and Departmental Director of Research and Sponsored Programs in the Computer Information Systems Department at Georgia State University. Dr. Ramesh received his PhD degree in Information Systems from New York University. He has taught at the Naval Postgraduate School, Monterey, CA, Syracuse University and the Stern School of Business at New York University. His research work has appeared

in several leading conferences and journals including the IEEE Transactions on Software Engineering, IEEE Expert, Annals of Software Engineering, Annals of Operations Research, IEEE Com puter , IEEE Internet Com puting , Concurrent Engineering — Research and Applications, Decision Support Systems, Journal of Systems Integration. His research interests include supporting collaborative work with artificial intelligence, decision support and multimedia technologies in the areas of requirements engineering and traceability in systems development, concurrent engineering, new product development, knowledge management and business process redesign. His other research interests include data mining and e-services. Dr. Ramesh’s work has been supported by several government and private organizations including the Software Technology Program of the Microelectronic Computer Technology Corporation, Andersen Consulting’s Center for Strategic Technology Research, Office of Naval Research<sup>r</sup>Naval Surface Warfare Center Dahlgren Division, USAF’s Rome Laboratory and Army Research Laboratory, and the National Science Foundation.
