---
otero_id: 21037
otero_key: "PF9965TX"
title: "Domain engineering for developing software repositories: a case study"
authors: "Karma Sherif; Ajay Vinze"
year: "2002"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(01)00130-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Domain engineering for developing software repositories: a case study

Karma Sherif <sup>a,</sup>\*, Ajay Vinze <sup>b,1</sup>

<sup>a</sup>Information Systems and Quantitative Sciences Department, College of Business Administration, Texas Tech University, Lubbock, TX, 79409, USA

<sup>b</sup>School of Accountancy and Information Management, College of Business, Arizona State University, Box 873606, Tempe, AZ, 85287-3606, USA

Received 1 April 2000; received in revised form 1 December 2000; accepted 1 June 2001

## Abstract

Software reuse promises to reduce software costs and shorten time to market, but despite major efforts undertaken by the software industry to boost the levels of reuse, there has been difficulty in installing workable repositories in corporate settings. This paper examines a promising approach to solving this problem, the methodology of Domain Engineering (DE). The paper reports the experiences of an oil and gas company that have successful adoption of DE to build a repository of software assets. Its goal is to provide practitioners with rich contextual information on both the technical and social issues involved in the development and deployment of software assets. <sup>D</sup> 2002 Elsevier Science B.V. All rights reserved.

Keywords: Domain engineering; Domain models; Software reuse; Success factors for software reuse

## 1. Introduction

Domain Engineering (DE) is a structured method of developing prefabricated building blocks to advance the development of software systems [1,2,9,11,14,15]. These blocks can take different shapes; the most widely known of which is code. In recent years, there has been an emphasis on the reuse of all deliverables of the software development cycle to include requirement analysis, design, architecture, and even test data. However, for these components to be reusable, they need to be designed with reuse in mind (we will refer to components that are built specifically for reuse as reusable assets). DE has emerged from the systematic reuse community as a methodical approach to analyzing, designing and implementing reusable assets [16]. The goal of DE is to develop design patterns that embody a generic solution to common problems within a specific domain. Such an approach focuses on ‘‘doing better with less.’’ Most of the requirements for new products are satisfied with existing reusable assets. In fact, reuse contributes up to 70% of the development effort, resulting in significant reduction in contributions of time and organizational resources [3].

DE research has been largely technical in nature. Very few have tackled the organizational changes involved to ensure that reuse is not just a fad but is in fact institutionalized [6,10,13,19,20]. Though technology plays a vital role in the development of reusable assets, it has been widely acknowledged that changes in technology must be accompanied by organizational changes to align the business with new technological shift [6,7,23,24]. Researchers [10,19 – 21] have came up with a set of critical success factors for the adoption of reuse however there is no clear understanding of the reuse processes and how organizations establish these prerequisites. In addition, there are no apparent relationships drawn among the factors to identify if they are mutually exclusive for example or totally dependent of others. The main reason behind this outcome is that earlier studies have implemented the survey methodology to identify factors that predict software reuse levels. The results are presented as a checklist of items with very limited details as to why these factors are important. It is thus the primary objective of this research to explain how organizations successfully implement systematic reuse and why the identified processes and concepts important for achieving success. Given the wide scope of operations involved in domain engineering and its complexity, it becomes necessary to study DE within its natural setting. The driving urge to conduct case research stems from the lack of a strong theoretical base to explain HOW and WHY organizations successfully implement domain engineering or systematic software reuse in general. The study focuses on both organizational and technical issues, a timely contribution to fill a gap in the reuse literature.

While this study reports findings for a single organization, the data sources are 13 different points of contact in different parts of the organization. The interviewees spanned the organization, providing different perspectives on the DE effort and the various contextual factors that affected the deployment of the DE project. The paper demonstrates the experiences of an oil and gas company in institutionalizing reuse. The data collected provides a rich description of the various factors that caused the DE initiative to be a success. The lessons learnt from the case are categorized according to the various stages of the project, providing insights to different reuse stakeholders: reuse experts, managers, asset creators, and asset utilizers.

Section 2 provides an overview of the different stages of DE and documents its legitimacy as a basis for developing software assets. Section 3 presents the case study and focuses in particular on the importance of determining organizational readiness in the context of implementing software repositories. In Section 4, lessons learnt from this implementation are presented to illustrate the concerns and potential risks that management needs to consider before implementing the DE methodology. The paper concludes with recommendations for both academicians and practitioners dealing with issues related to DE.

## 2. Domain engineering (DE)

The glossary of software reuse terms provided by the National Institute of Standards and Technology (NIST) defines Domain Engineering as a ‘‘Reusebased approach to defining the scope (Domain Analysis), specifying the structure (Domain Design), and building the assets (Domain implementation) for a class of systems, subsystems, or applications.’’ Unlike system development, DE analyzes all systems in a domain, generalizes their functionality and represents the requirements for the whole domain in a domain model [1,11,17,22]. It involves a paradigm shift from system development as it emphasizes the development and maintenance of a whole product-line rather than the development of a specific system [25].

The thinking behind DE is that reuse is most effective when applied within a specific domain, where software assets are developed as prefabricated building blocks and are used to build software in a product line [7]. The potential for a software asset to fit within systems already developed in a domain is high; provided that the systems are structurally or functionally similar to one another. Thus, researchers insist that the application domain be considered a generic measure of a component’s reusability. Such sharing of software assets among systems within a domain is called vertical reuse and is reported to have boosted reuse levels to as much as 85% of software development efforts [18].

DE consists of three main phases: Domain Analysis, Domain Design and Domain Implementation. The processes involved focus on the development of a whole family of systems that make it possible to aggregate different solutions within a domain into a general design that can be packaged for reuse in model-based repositories. The process and stages of DE are summarized in Fig. 1 and Table 1.

![](/api/attachments/PF9965TX/fulltext/images/a87ca8b3b6977cb207d84411496132032d8d891a04c83423369c9dcdd8218747.jpg)  
Fig. 1. Processes and knowledge sources of domain engineering.

During the analysis phase, information on past similar problems within a specific domain is collected and modeled to represent the general problem definition for the whole domain [2]. The main deliverable of this stage is the domain model that provides a representation of the requirements of the domain and identifies the structure of data, flow of information, as well as the functions, and constraints of software systems within the domain. It is important to realize that the domain model portrays the commonalties, as well as the variations among requirements for software systems in the domain [3,11]. The variations between systems will later be used to build flexible assets that can accommodate a larger scope of products within a given domain and survive changes in functionality or technology [22]. The goal for the domain model is to be perceived as a prescription when developing custom-made applications. Features missing from a domain model may intentionally have been left out because of their potential to cause stability problems within a system. On the other hand, features that are not part of user requirements may improve user work processes and thus be considered innovative. Application developers should thus view the domain model as a resource to optimize the selection of a cohesiveness feature set that will satisfy application requirements [24].

Table 1  
The stages of the Domain Engineering life cycle

<table><tr><td>Domain Engineering stage</td><td>Description</td><td>Deliverables</td></tr><tr><td>Domain Analysis</td><td>Scope the domain. Determine the functionality of the domain. Determine the composition of the domain</td><td>Domain model</td></tr><tr><td>Domain Design</td><td>Model the architecture for the domain. Come up with a generic design to recurring problems in the domain</td><td>Domain specific software architecture</td></tr><tr><td>Domain Implementation</td><td>Develop reusable assets Include code, test cases, documentation</td><td>Reusable components for the domain</td></tr></table>

A critical non-technical success factor of this stage is identifying the stakeholders’ objectives. It is important to identify aspects of the DE project that might promote stakeholders’ support or objections to set up a plan to reinforce commitment and cope with possible resistance [23]. It is the task of the domain engineers to negotiate and reconcile these conflicts. Researchers have long stressed the issue that organizational constraints may impose significant compromises on the success of a reuse project [4,5,7]. A widely cited cause is the limitation of financial and human resources due to constraints set by marketdriven application development projects.

Following the development of a domain model, the architecture showing the functional decomposition of the domain is defined. This stage employs knowledge of past similar solutions to develop a generic design of recurring problems in a narrow domain. The deliverable is a solution-oriented Domain Architecture [14]. This is a flexible multifaceted design of a domain that can be used to build different systems. The success of the design phase is dependent on the flexibility of the Domain Architecture representation. It is highly recommended that the architecture be prototyped to reduce the risk of rippling design defects through the whole domain. The architecture should be flexible enough to allow for its maintainability and continuing evolution.

The final stage of engineering the domain involves the actual development of reusable assets. Domain engineers can use the Domain Architecture to build reusable components that will permit software developers to assemble applications from the asset base. For each asset, the team must determine whether to build the component, to reuse existing ones or to generate the component using CASE tools. Legacy artifacts will obviously require structural or functional modifications to support reuse initiatives. The choice of technology must be considered before building assets to account for any customer constraints or the level of maturity of the technology.

Once the assets have been developed, it becomes imperative to market the assets to application developers. Support for searching, retrieving, adapting and integrating assets within applications will perpetuate interest in the asset base and the DE methodology as a whole. The higher the level of reuse of the assets in the asset base the higher the economies of scope and the lower the overall cost of developing applications.

## 3. DE basis for software reuse—lessons learnt at OGC

Our case analysis focused on an oil and gas company we call OGC. It is a large multinational corporation with over 10 million employees and US\$9.8 billion in revenue. We focused primarily on the IS organization within OGC, dealing with ‘‘subsurface’’ data. Applications in this field model and analyze the subsurface structure in the process of oil exploration. We further constrained our consideration to studying the reuse infrastructure OGC had created.

Given the nature and scope of those software systems, it became critical to create a software repository. The compelling need for a software repository originated from the fact that several disciplines in the sub-surfacing domain, like exploration and production, reservoir engineering, seismic interpretation, geophysics, geology, and many others, had discovered they were dissipating their resources by repetitively solving similar problems. With each discipline having its own programming shop, there was no incentive to extend the learning process across operating units. After perceiving the potential benefits of creating a shared repository to serve common needs, several disciplines decided to join forces and launch a reuse initiative. Developers believed reuse to be capable of a number of advantages ranging from shortening the development cycle to improving job satisfaction. They strongly believed in the technology and realized the importance of building an organizational memory to preserve their expertise and leverage it across disciplines. A reuse-working group, REUSE II, was established and was given the responsibility of analyzing the sub-surfacing domain as well as designing and implementing reusable assets for the application teams. At the time of the study, REUSE II was viewed by its customers as an exemplar of an initiative that successfully developed and institutionalized a repository of software assets.

It was largely acknowledged that the driving impetus behind their success was their use of a systematic methodology to build the software assets and their commitment to effectively utilize their software repository. REUSE II perceived the considerable need for adopting a solid methodology when developing the software assets because earlier unsystematic attempts initiated by several other departments across OGC had failed. After reviewing several alternatives, DE seemed a promising approach to achieving OGC’s sub-surfacing goals. An overview of the concepts behind DE ascertained that domain models would increase the level of reuse of software components. OGC realized that DE rigorously identifies common objects between a family of systems and design the resulting set in a way that makes it relatively simple for developers to reuse. Since domain models provide a representation of the backbone of all systems in a domain, they increase the granularity of reuse speeding up systems development cycles and reducing the overall cost of building systems. REUSE II decided to focus on functionality that promised high economic benefit through multiple reuse cycles by different application teams.

The primary factor behind REUSE II’s success has been the development of a solid infrastructure to support the DE initiative. The groundwork focused on the following cornerstones:

 building commitment by both top management and customers of the library

 establishing a target market for the software assets,

 restricting the assets scope to a particular domain,

 acquiring the necessary skills to develop and deploy software assets,

 establishing lines of communication among all stakeholders, especially management, application developers and end users,

 marketing high quality components.

As part of the study, we observed and recorded events at Reuse II. The observations were spread out over 2 months. Procedurally we interviewed 13 different developers from three different teams: the developing team, the reusing team and the clients. The developing team was mainly responsible for the creation of the assets and its adaptation to different application environment. The reusing team involved developers who utilized the Reuse II library assets to build new applications for the clients. Most of the clients of the OGC sub-surfacing group are internal geophysicists who need the applications to analyze and interpret sub-surface data. Also among the interviewees was the director of the project. Interviews lasted between an hour-and-a-half and two hours. All interviews were recorded and transcribed. A list of codes representing the important concepts related to DE and reuse was generated. The data collected were categorized under the codes to describe the development of Reuse II library and the critical success factors that accounted for the sustainability of the project. Excerpts from the interviews are included in the following sections to substantiate the discussion presented.

The codes evolved into three main categories that illustrate the stages of implementation for the domain repository. These are: initiation, deployment, and maintenance. At the initiation stage, Reuse II was preoccupied with laying the technical and organizational infrastructure for the project. In addition to closely monitoring the development of the assets, the project leader made sure that resources were procured to sustain the effort. At the second stage of the project, the group was focused on successfully deploying the assets to the application groups, providing all the necessary expertise to ensure smooth integration of the assets within applications. The last stage is ongoing and evolutionary, in the sense that it does not end. At this stage, the group is sustaining organizational interest in the project by evolving the library to better support its clients and creating a corporate culture that actively believes in the power of systematic reuse. The following sections are dedicated to detailing each stage and demonstrating the critical success factors that promoted the DE initiative.

## 3.1. Initiation

This project was started 8 years ago to create a reuse platform for the sub-surfacing domain. Each of several disciplines in the domain had its own programming shop for delivering applications to their customers. Members of the different disciplines had noticed overlap among their projects and a waste of effort resulting from lack of integration of their efforts. The case was presented to the CIO with a proposal to join forces to take advantage of the commonalties between the disciplines and to launch a reuse library.

The project was started with an attempt to uncover the commonalties that existed within applications developed in the domain of sub-surfacing. The drive behind the initiative was to reduce the cost of developing similar systems. A former member of Reuse II explains the reasons behind launching the program saying:

We’ve been building these same types of systems for over 10 years, probably even more. These are oil field monitoring and control systems, SKATA type systems. We’ve been using one particular set of technologies, and every system costs about the same amount. You would expect costs to go down over time because you’ve done that same system over and over again, but that just wasn’t happening. We recognized that we were just spending way too much building these systems given that we’d already built so many just like them. Everybody recognized that there’s an opportunity here; the IT professionals, management and the clients.

The group focused on developing one solution that could serve the different application groups, strategically focusing on the requirements of one influential customer for reasons highlighted by the project manager.

A lot of times what we do is we meet the requirements of a single application group with the full understanding that whatever they do, a lot of the other groups will follow.

The ability to reduce the cost of developing systems was not an instantaneous benefit accompanying the onset of the project. It has been realized only recently after an 8-year investment in the reuse infrastructure and an accumulation of expertise in the field. As the reuse expert explains it:

After one to two years of work, all of our managers were saying, ‘‘Oh well, how much savings have you had? What are the benefits?’’ And pretty much we said ‘‘nothing yet’’ because we are populating our library. It has only been recently, in the last, I guess, three years that we have really exploded, have really taken off because we had several years of actually populating our libraries.’’ It was. . .after ‘‘we’d built three systems, the fourth one cost a lot less. And that did work.

Stages of library development. The first step was to decide on the scope of the library. The group targeted a domain that was strategic to the organization and had influential application groups working on it. The components of the domain are core to OCR business. They are not available from outside vendors because they are tightly coupled to the business logic. The group’s awareness of the importance of the domain to the application developers encouraged them to target that domain in their first round. The importance of the domain has also kept the group from losing the loyalty of other stakeholders to alternative methods of development like outsourcing. As the reuse expert explains,

If it’s a domain that has been solved, then yes, you can probably outsource it quite easily because there have been other companies that have experience with providing services in that domain. But if it’s a domain that’s very complicated and technical it’s tougher to outsource because who else can do it? You have to find someone else that has a lot of experience solving those types of problems, otherwise you’re throwing your money away.

Another encouraging factor was the stability of the domain. The components of the applications in the subsurfacing domain did not require frequent changes. As one developer describes it,

[The assets] are locked in one technology. I think that is part of what made them successful. It is interesting now we are 8 years later and they have just now started up a study project to define how they are going to move to the next generation of technologies.

The stability of the requirements within the domain resulted in stable assets, a requirement often emphasized by the application groups. Reusers are always afraid of building applications around pieces of functionality that frequently change and disturb other dependencies.

The second step was to acquire the domain knowledge. The availability of domain knowledge is critical for the creation of reusable assets. The group depends mainly on two sources of information for knowledge mining in the domain: the availability of staff with long experience in developing systems in the domain and domain experts who understand the technology of the domain.

The third step was to abstract the information collected into a domain-specific architecture that different applications can easily modify to fit their needs. The architecture provides information about the software components that are used to develop applications, the interaction between the components and the array of functionality the components satisfy [22]. The architecture defines how the assets can be organized to produce large-grained components that support a combination of features. It also provides support for replacing components with application specific ones without agitating the structure.

The group divided the architecture into two main layers: a domain-independent layer (interact with the hardware and is only modified when a change in hardware occur) and a domain-dependent layer, which contains components common to applications in the domain. Components in the domain-independent layer are most likely to be reused without any modifications across applications within the domain.

The domain architecture at Reuse II helped identify the reusable assets relevant to a specific context and provided detailed information to the developer on how to integrate a component within a system. The establishment of the architecture was a critical success factor for the project. The comment one developer gave on the role of the architecture was:

I think what made them successful is that there was an application architecture behind the whole thing, and all of the components were built to that application architecture.

The architecture designers also generated rules to enable the developers to pin a system specific requirement to the right place in the overall domain architecture.

The fourth stage was the actual development of the assets. At the onset of the project, it was not easy for the developers to migrate from a mindset of building for one application to one that builds for several. As one developer explained,

Instead of just coding it up so that it only does what you need it to do, you need to think about doing a little bit more to design it properly so that it has reuse capability.

Quality of the assets often was lacking, but the group was constantly trying to upgrade it. As the project leader explained:

We understand that it’s an iterative process. We usually rewrite the object about three times before we get it right. We know that we’re not going to get it right the very first time, and we don’t even try because this is kind of a research area. We try to include as many people as possible to get the design right, if it doesn’t work out, we sit there and refine it.

The group set requirements for component building. The requirements dealt with the degree of generality and the level of quality an asset should pass to be reliable for reuse. Reliability is seriously considered by REUSE II because of a strong belief that losing the confidence of one customer can doom a whole effort.

The development of the assets necessitated the establishment of a software repository to host the reusable components. The group learned from past failures that the organization and search mechanisms of software repositories had significant impact on developers’ attitude and usage of the library. The structure of an Ad Hoc library as that mentioned in Ref. [19] makes it impossible for developers to locate assets without the support of the original asset creator. Developers are often frustrated when trying to locate assets that match their application requirements especially when the volume of the software repository is massive and the components are categorized under non-standardized parameters or keywords. The efficiency of the search tool is another factor that may add to the disappointment with the repository. With Reuse II, the group decided to categorize the repository along domains and to pub lish web pages to assist developers locate components in the library. However, the sheer size of reusable assets hosted in the library does not guarantee a swift access to the assets. The reuse expert justifiably admit the problem saying

There are over 1200 classes, so it’s pretty complicated. The learning curve is steep. To start learning it takes time. We try to keep our documentation evergreen and we also have our libraries partitioned up by functionality so that all of our data objects are in one library, all of our graphic objects are in a different library, all of our classes that involve reading from specific formats, like LANDMARK are broken up into their own separate libraries.

A number of resources were critical for the success of this stage. Among these were management support, time, funds, skills and dynamic communication. The effect of each of these resources is highlighted in the following sections.

## 3.1.1. Management support

Management support actually made time and funds available to the group. Management’s understanding that reuse pays only after an infrastructure has been put in place greatly helped the group during the initial stage. Management understood that it was not going to be an instant gain, that could only come after the reuse library had been populated. The project leader emphasized the role of management saying:

You’ve got to have commitment from management to stick with it. If you are building a reuse library from scratch, it does not pay out the first several years. It only pays out after the reuse libraries have been populated with well-tested components.

## 3.1.2. Time

Time is an important resource requirement for developing a reuse infrastructure. It is widely acknowledged in the literature and among reuse practitioners that reuse takes time to repay its benefits. One developer shared his experience when he was working on Reuse II, saying

It was probably a three- to four-year payoff, which is generally not acceptable in terms of how much greater return we expect on things these days. So, in some ways, you could say that economically it might not have been a wise choice. On the other hand it certainly is paying out now, down the road you know. We’re down the road almost 8 years now, and they’re able to build these systems very, very fast for low cost. They’re able to customize them to the given location and install them quickly.

The group was fortunate to be given time to build the library. During the initial years of development, the group was just populating the library. Its members were not servicing any application groups.

## 3.1.3. Funding

The availability of funds is another factor that allowed continuation of the program. At Reuse II, there was willingness by both IS management and client management to invest in building reusable components that could then be used on subsequent projects. At the beginning, the group was not recouping any of the investments but was concentrating on acquiring the skills and building the critical mass of components. As the director of Reuse II explained,

Several years ago, we did have our own budget, and it was very nice to acquire the resources that were important for building the infrastructure.

This is particularly constructive than acquiring funds from customers, especially at the early stages when the benefits are not realized. After laying the groundwork, the group was completely funded by the application groups. This transition had both positive and negative effects. On one side, Reuse II was always motivated to evolve their components and improve their performance to please their customers, knowing that their existence depended on the satisfaction of the application groups. On the other hand, application groups attempted to influence design in ways advantageous to their specific needs. It can be hard for a reuse group to convince application groups to pay for non-customized components as illustrated in the following quote:

Now it is tougher because we are at the mercy of the application groups, so I have to justify my work a lot more to convince them.

The availability of funds from both management and application groups has an impact on the scope of the domain repository, the type of assets developed and the support available to customers. If a specific domain is not allocated resources, the group does not address its problems or build components for it. The group does not even provide support for free. The reuse expert explained the process as follows:

If an application group really has some critical projects that they need to work on, they have to free up budget, and then we’d loan out some of my programmers to their group, and then they would get personal attention. They don’t get it for free because I don’t have my own budget. I get it through other people. So I’m like a little contracting company. We provide reuse services, and it’s up to other people to put up some money and actually contract some of my people out and allow us to consult and show them how to design certain things. That also takes time, and time is money.

## 3.1.4. Skills

The availability of talented staff is a vital resource for building a domain repository. The developers believed that a critical factor was having the right staff skills in place to carry out the initiative. OCR, in general, believes in the power of the people. As the director explained

If you have the best tools in the world, but you don’t have good people to use them, you’re doomed to failure. If you have really good people and crummy tools, I bet that those people will find a way to make a good product. I cannot stress the power of the people more. Without the people, we’re nothing.

The group believed that it had the necessary staff with the necessary skills to be successful. Several skills have been identified as critical for the success of reuse. The ability to design for reuse is crucial because of the different mindset required to generalize components to fit the needs of a family of systems. It is technically challenging to build and architect an effective reuse platform because reuse requires that the developer design reusable assets in a way that makes it easy for other developers to understand it, integrate it within their application and modify it if needed. Though designing abstract reusable assets is believed to be a challenging task, the group believed that ‘‘a lot of people have been doing reuse for such a long time that it’s just natural to design it that way.’’

One important factor that was believed to have an effect on funding is the communication skills of the reuse team member who worked with the application groups. As the reuse expert explains,

If a developer develops a reputation of being unfriendly and no one wants to work with him, I’ll have someone on my team that no one wants to pay for, and we’ll be eating the cost. . . Team skills are extremely important because, like I said, my little group is kind of like a consulting firm or a contracting company. As long as people want their services, I’m really happy because the clients will pay for them, and they’ll work on other projects. As soon as no one wants them, then it’s like what do I do with them?

## 3.1.5. Communication

Building a library of software assets involves a number of stakeholders whose agreement is important for the success of the repository. At Reuse II, the reuse team communicates closely with two main stakeholders: the application groups who are the customers and the end users who are the ultimate beneficiaries of the repository. Communication with the application groups is important because ‘‘the domain expertise typically resides with the application.’’ The application groups are involved in all stages of the development of reusable assets. They provide domain information during analysis, review the design of reusable assets and act as beta testers before assets are admitted to the library. The geographical proximity to application developers had a positive impact on communication and the ability of the reuse team to understand the business domain. Communication with end users had also contributed to the comprehension of the domain. The close relationship between the geophysicists and the reuse group led to the success of the reusable assets. As the reuse expert explains,

What we’re solving is complicated modeling of the way the subsurface structures look like, and you wouldn’t believe how complicated that work is. There’s no way that we could do that without having geophysicists located with us. So that has been extremely helpful because you would have to be a geophysicist to understand what we’re trying to do without having some type of person helping you out. With the geophysicists located right here with us, they worry about all of the complicated stuff, we worry about the computers. They supply us the algorithms, we supply how the programs interact with the algorithms. So it’s a very good working environment and working situation.

## 3.2. Deployment

The second stage in the implementation is the deployment of the assets in the repository. This requires marketing the repository to the various stakeholders with their different needs. To management, a Return on Investment (ROI) is an important criterion for judging the pertinence of investing in a domain repository. One way of gaining an appreciable ROI is to build a sizable customer base for the domain assets. Customers will be dedicated to the repository if the assets are dependable and support for using them is readily available. The promotion of the group’s success with its initial customers helped in perpetuating the interest in the domain repository.

## 3.2.1. Target market

A significant prerequisite of the development of a software repository is the presence of an adequate number of clients with common requirements to justify the development of reusable assets. In the case of Reuse II, there were 20 application groups interested in employing the services of Reuse II. Ten of their customers were over in Europe. The reuse group strategically focused on one influential client knowing that other application groups would follow the lead. By focusing on a powerful group that others follow, they guaranteed a perpetual market for their assets. As one developer explains,

There’s this one primary application group that’s doing all of the advanced programming. We are very aware of their needs, and we work so closely with them. All of the other groups kind of follow suit. So if I’m aware of their needs, then I’m kept aware of other peoples’ needs as well because they are kind of one in the same.

## 3.2.2. Available assets

The availability of a wide range of quality assets is a key factor in winning the application groups’ commitment to support Reuse II library. The existence of a wide variety of assets that satisfied the needs of the different application groups is perceived as an advantage. The quality of the assets played an important role in gaining the support of the application groups. The group involved their customers in reviewing the design and implementation of reusable assets to insure their approval on these assets. Object-Oriented technology was perceived as a propeller to the offering of wide variety of high-quality reusable assets [8].

## 3.2.3. Promotion and support

Promoting reusable assets to asset utilizers and management helped market the library across the organization and maintained support to it. Promotion of success stories to management motivated application groups that were not customers of Reuse II library to try the services of the group. An important factor in wining new customers was the support Reuse II offered. Different types of support were available to application groups to understand and utilize the assets. The group provided an on-line documentation that explained the structure and functionality of all assets hosted in the repository. A number of examples were also available on-line that showed the application groups how to use the assets in the library. In addition, personal consultation was also available in return for a fee. The group lent developers to individual projects to help with the integration of reusable assets into systems. The group genuinely believed in providing first class support to retain their customers’ loyalty and consequently maintain top management support. Their ability to win over new customers assisted in building a community that believed in the benefits of preserving the reuse repository.

## 3.3. Maintenance

A number of elements have been identified as critical for maintaining the organizational interest in the domain library. Among these factors are

 the commitment of all stakeholders to support the library,

 the evolution of the assets with the advent of new technologies or re-engineered processes,

 an assessment of the impact of the library services,

 motivation of the stakeholders to sustain their support of reuse,

 and the development of a corporate culture that supports reuse of past experiences,

## 3.3.1. Commitment

Commitment from all stakeholders is considered important for the continual support of a serviceable repository of software assets. Top management support is important for procuring the necessary resources to develop and market the repository. A number of factors contributed positively to management commitment at Reuse II. First, securing a customer base of 20 application groups worldwide made it easy to convince management of the value of an asset library to the organization. Second, the ability to deliver solutions quickly to clients was widely acknowledged. Third, establishing a reputation as experienced developers in the field and the industry in recognition of their software assets highlighted the group’s efforts and facilitated winning management support.

Application groups’ commitment is also important. Application groups must be committed to use the assets in the library and to provide feedback to the reuse group on the performance of the assets. As one developer explained:

They have to work with you and to help create the assets. They have to take part in the design reviews; they will not use what you write if they have not actively participated in designing the reuse components.

Application groups’ commitment to testing the assets and providing feedback to the reuse team was highly appreciated at Reuse II. The application groups were motivated to help the reuse team because reuse enabled them to reduce the cost and development time, freeing them to develop new functionality.

End-users also played a part in the success of the Reuse II project at OGC Services. Their commitment to providing domain knowledge was seen as a critical success factor. The reuse team believed that without the geophysicists, it would not have been possible to build the required components.

## 3.3.2. Evolution

The evolution of software assets helped Reuse II maintain clients’ interest in the library. The group is engaged in an ongoing effort to improve the assets quality. The assets have gone through two revolutionary stages during their 8-year life span. This is one factor that the director believed contributed to the success of the library.

The assets were locked in one technology. I think that is part of what made them successful, though. There was application architecture behind the whole thing, and all of the components were built to that application architecture. If you keep changing it all the time, then all the application groups have to keep changing all the time. And you don’t want to make them upset because, you know, you don’t want to alienate your customers.

It was rather unusual for assets to live with the same technology for 8 years given the rate of change in software technology today. However, it was the director strong belief that stability will drive the repository to higher levels of efficiency if the group focus on improving the design with every application development cycle rather than migrating to new technology platforms with the release of popular tools.

In addition to these two reengineering efforts, the group actively reviewed the stored assets to incorporate new information or to employ new technologies to increase the level of performance. The present focus of the group is to fill in gaps and to complete their tool kit. As one manager explains

The overall strategy is to put extra effort into reengineering, to fill in the framework properly. On occasion, if an application team needs a specific component early, the component will be built in a less generic fashion and later, when the pressure is off, replaced with a REUSE II components.

It is commitment to reuse that drove the group’s decision to accept only assets that meet the reusability requirements. The team firmly believed that reuse goes beyond just building an infrastructure and creating reusable assets to continually evolving that structure to higher standards.

## 3.3.3. Assessment of progress

The group is able to assess its progress through two measures; time and money. The application groups are able to deliver systems in significantly less time and with fewer resources. Applications have been developed with less than 20% new code and over 80% of the functionality being reused from the REUSE II libraries. This high level of reuse had a significant effect on the cost and time to market application. However, there are no exact measures of the savings.

The developers believed that careful observation of the number of developers and the number of applications using the library were the best way to assess progress. They thought that metrics create a barrier to allowing the organization to assess its progress objectively and determine the business value of reuse. Their well-deserved reputation for reducing costs and shortening time to market applications earned the loyalty and continuing support of their customers. This finding does not accord with the literature that asserts that metrics are critical for the success of reuse [18]. Our explanation to reconcile these two views is that the reuse group was fortunate to gain the support of management without having to offer a proof of concept for 5 years. During this time, the group was building a sound reuse infrastructure. Following the inauguration of the reuse library, success stories started to surface. It was not hard for the group to gain the support of both management and the customers given the vital service they were offering to the application groups and the results they could achieve.

## 3.3.4. Motivation

The performance evaluation of members of the Reuse II group is directly related to the satisfaction of the application groups. This is mainly dependent on the quality of the assets they deliver and the services they provide. The realization that funding is totally dependent on the quality of services offered is a strong motivation for Reuse II to develop rigorous assets. Even without a formal reward system specific to the development or utilization of software assets, members of the group are dedicated to ensuring the quality and rigor of software assets. In fact, the director of the center believes that creating a formal reward system is not necessary, contrary to what has been hypothesized in the reuse literature. At Reuse II the director believes that

The fact that it’s a shared vision creates no need for monetary incentives. I don’t think it would have any effect on other peoples’ jobs, I think it would actually add a layer of administration of keeping track of who’s doing what.

## 3.3.5. Culture

The reuse team has been successful in creating a culture that supports the development and reuse of software assets. Management, on the one hand, understands that software assets pay off only after an infrastructure has been put in place. The asset creators ‘‘are committed to doing whatever it takes to have a successful asset. They don’t try to take shortcuts.’’ The asset utilizers are willing to devote the time it takes to put up with the struggles of putting an asset library in place. The support of the customers is very unusual since they normally are concerned with the customized solution of a particular problem. The director of Reuse II recognized the importance of gaining the support of the customers especially after gradually being weaned off management financial support. He stressed the need of maintaining high quality assets in the repository as a way of sustaining the loyalty of his customers.

‘‘What’s more important is that you get the commitment from application groups or your customers to help you solve that problem through the first couple of years.’’

## 3.4. Summary

Some subtle lessons learned from the endeavor may prove useful to practitioners in the field of reuse. The following section categorizes these lessons along the three stages of development and summarizes what was learnt from the case.

Recommendations during initiation are as follows.

(1) Assess the need for building reusable assets based on the domain of focus. Determine the degree of commonality that exists among problems in the domain. Determine the strategic importance of the domain to the business.

(2) Make a business case for developing the reusable assets comparing the costs of not having a software repository with the costs of having one. Present the results to all stakeholders; managers and decision-makers. The presentation should be in appropriate language that the stakeholders would understand.

(3) Assess the receptivity of decision-makers to the idea and carefully study any concerns that might surface. Convey the reasons for adopting a software repository and its importance to the organization as a whole.

(4) Depending on the organizational culture, determine the scope of the repository. The program can start with a small pilot project to demonstrate the feasibility of building a software library. Collect metrics during the pilot project and communicate results to all stakeholders. Stress the importance of learning from past experience.

(5) Determine the resources required for taking the repository beyond a pilot study. Resources include funding, time, and staffing.

(6) Assess the skills available and determine the roles of asset creators and asset utilizers based on experience in the domain of focus and competency in analysis and design.

(7) Stress the importance of communication between asset creators and asset utilizers to the success of reuse. Incorporate communication throughout the structure by having a facilitator who coordinates interaction between the two groups.

(8) Assess the currently adopted processes for software development and their compatibility with reusing software assets. Determine any necessary changes needed to incorporate reuse in all stages of the development cycle. Convey to decision-makers the need for changing current methods and get feedback regarding the applicability of the new methods.

(9) Educate decision-makers about DE.

Recommendations during deployment are as follows:

1. Promote the results achieved by projects. Aggregate the results in the form of lessons learnt that highlight both success factors and possible barriers.

2. Make sure that developers in different fields are aware of the available assets and advantages associated with their use.

3. Collect reuse metrics and attach them to the assets in the organizational library.

4. Get feedback from developers about the performance of the assets with suggestions to improve its quality. Attach performance evaluations to the assets so developers know what to expect from the assets.

5. Get developers’ feedback regarding new functionality that would be needed in the future and work on getting resources for their development as quickly as possible.

6. Provide reliable sources of support for using reusable assets. Documentation by itself is usually not adequate. The active participation of an asset creator in a reuse-oriented project is definitely appreciated by asset utilizers.

Recommendations during maintenance are as follows.

(1) Evaluate the productivity of the assets and the possibility of upgrades as new technologies are introduced. Remember that shareholders’ commitment to the library is not bestowed but earned through the reputation of the assets and the availability of support of asset creators in achieving cost reduction and customer satisfaction.

(2) Remember that creating a shared organizational culture that fosters and nurtures reuse is the only sustainable support for a reuse program in today’s continuously changing economy.

## 4. Implications

The process of using DE to build a repository of software assets for the sub-surfacing domain was effective for two main reasons: (1) its methodical nature of acquiring information, modeling it and developing software assets, and (2) the recognition of the role of non-technical factors. The majority of the factors grounded by our data have already been identified in the literature as success factors [10,12,19–21]. In fact, two of the studies [20,21] have organized these factors in a reference model for benchmarking the reuse initiative in organizations. The studies have tested the predictability of the model using a set of cases and data from a survey. However, the main strength of our study is the contextual information provided around the factors. The data collected from our case study provided us with rich details on the reuse life cycle and the processes involved during each stage. There is a clear understanding of the relationship between the factors and why they are considered critical for the success of reuse. Our study also introduced a set of new factors that were not intro duced in the literature. Among these is the choice of a strategic and stable domain of focus for building reusable assets. The stability of the domain increases the possibility of higher return on investment since the assets go through a larger number of development cycles before being changed. In addition, assets that belong to strategic domains are less likely to have substitutes and thus sustain their competitive advantage. Another important finding is the role customers’ play in the success of a reuse initiative. Though customers are normally depicted in the literature as short sighted when they focus on customized one time solutions, this study showed that the involvement of customers in the development of a reuse infrastructure assisted in gaining commitment and support to the reuse initiative. The reward to customers is future gains from on going evolution of assets in the library. The third finding relates to the communication skills of members of the reuse group. Reuse champions are more like change agents who are capable of tipping the odds of IT projects toward success because of their effective change management behavior.

## 5. Conclusion

The current research focused on identifying factors that affect the successful implementation of a DE initiative. It sought to build a theoretical framework, seeking data from a multinational oil and gas corporation that was able to reap tangible benefits from its

DE initiative. The analysis of the data suggested that enablers of reuse adoption occur at three stages: initiation, deployment, and maintenance.

The findings make an important contribution to the study of reuse adoption in general and DE adoption in particular. The model presented here indicates that the procurement of tangible resources is important at the early stages of adoption to guarantee the development of a certified asset base that can service different applications within the domain of focus. During the deployment stage of the assets, marketing plays an important role in propagating the assets to the different developers and promoting success stories to potential customers. The ultimate success of the initiative will rely on the ability of the reuse group to sustain shareholders’ commitment and build an organizational culture that strongly believes in reuse.

## References

[1] G. Arango, R. Prieto-Dı´az, Domain Analysis and Software Systems Modeling, IEEE Computer Society Press, Los Alamitos, CA, 1991.

[2] V. Basili, L. Briand, W. Thomas, Domain Analysis for the Reuse of Software Development Experiences (ftp://gandalf.umcs.maine.edu/pub/WISR, 1992).

[3] P. Basset, Framing Software Reuse: Lessons from The Real World, Yourdon Press Computing Series, Upper Saddle River, NJ, 1997.

[4] T.J. Biggerstaff, A.J. Perlis, Software Reusability: Applications and Experience, ACM Press, Reading, MA, 1989.

[5] T.B. Bollinger, S.L. Pfleeger, The economics of reuse: issues and alternatives, Proceedings of the 8th Annual National Conference on ADA Technology, Atlanta, GA, 1990.

[6] L. Brownsword, P.C. Clements, A Case Study in Successful Product Line Development (CMU/SEI-96-TR-016), Software Engineering Institute, Carnegie Mellon University, Pittsburgh, PA, 1996.

[7] D. Card, E. Comer, Why do so many reuse programs fail? IEEE Software 11 (September 1994).

[8] D. Champeaux, D. Lea, P. Faure, Object-Oriented System Development (http://agora.leeds.ac.uk/knowtis/Applets/docs/ oosdw3/ch13/ch13.html, 1995).

[9] P.C. Clements, Successful Product Line Engineering Requires More Than Reuse, International Workshop on Software Reuse (http://www.umcs.maine.edu/\~ftp/wisr/wisr8/papers/clements/ clements.html, 1997).

[10] W. Frakes, C. Fox, Sixteen questions about software reuse, Communications of the ACM 38 (1995).

[11] H. Gomaa, L. Kerschberg, Domain modeling for reuse and evolution, 7th International Workshop On Computer-Aided Software Engineering, 1995.

[12] I. Jacobson, M. Griss, P. Jonsson, Software Reuse: Architecture Process and Organization for Business Success, Addison Wesley, Reading, MA, 1997.

[13] R. Joos, Software reuse at Motorola, IEEE Software 11 (Sep tember 1994).

[14] D. Laforme, M. Stropky, An automated Mechanism for effectively applying Domain Engineering in Reuse Activities, http:/ arc-www.belvoir.army.mil/htmldocs/arc/da.papers/applying domain-engineering.html, (June 1996).

[15] R. Macala, L. Stuckey, D.C. Gross, Managing domain specific product-line development, IEEE Software 13 (3)(1996).

[16] J. Neighbors, An assessment of reuse technology after ten years. International Conference on Software Reuse, 1994.

[17] J. Neighbors, DARCO: A Method For Engineering Reusable Software Systems, in: T. Bifferstaff, A. Perlis (Eds.), Software Reusability, ACM Press, Addison-Wesley, 1989, pp. 295–319.

[18] J.S. Poulin, Measuring Software Reuse: Principles, Practices, and Economic Models, Addison Wesley, Reading, MA, 1997.

[19] D. Rine, R. Sonnemann, Investments in reusable software: a study of software reuse investment success factors, The Journal of Systems and Software 41 (1998).

[20] D. Rine, N. Nada, An empirical study of a software reuse reference model, Information and Software Technology 42 (2000).

[21] D. Rine, N. Nada, Three empirical studies of a software reuse reference model software, Practice and Experience 30 (2000).

[22] Software Engineering Institute (SEI), A Reuse-Based Software Development Methodology, CMU/SEI-92-SR-004, Carnegie Mellon University, Pittsburgh, PA, 1992.

[23] Software Technology for Adaptable Reliable Systems (STARS), Learning and Inquiry Based Reuse Adoption: A Field Guide to Reuse Adoption through Organizational Learning, STARS Technical Report, STARS-PA33-O1/001/02, STARS Technology Center, Arlington, VA, February 1996a.

[24] Software Technology for Adaptable Reliable Systems (STARS), Organizational Domain Modeling (ODM) Guidebook, Version 2.0, Lockheed Martin Tactical Defense Systems, STARS-VC-A025/001/00, Reston, VA, 1996b.

[25] J. Withey, Investment Analysis of Software Assets for Product Lines, (CMU/SEI-96-TR-010), Software Engineering Institute, Carnegie Mellon University, Pittsburgh, PA, 1996.
