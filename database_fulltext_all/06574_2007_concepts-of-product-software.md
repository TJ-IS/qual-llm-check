---
otero_id: 6574
otero_key: "PPQK38FM"
title: "Concepts of product software"
authors: "Lai Xu; Sjaak Brinkkemper"
year: "2007"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000703"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Concepts of product software

Lai Xu<sup>1</sup> and Sjaak Brinkkemper<sup>2</sup>

<sup>1</sup>CSIRO ICT Centre, Hobart, Australia; <sup>2</sup>Institute of Information and Computing Sciences, Utrecht University, Utrecht, the Netherlands

Correspondence: Sjaak Brinkkemper, Institute of Information and Computing Sciences, Utrecht University, PO Box 80.089, Utrecht 3508 TB, The Netherlands. Tel: þ 31 (30) 253 3175; E-mail: S.Brinkkemper@cs.uu.nl

Revised: 10 May 2007

Accepted: 9 August 2007

## Abstract

Both the impact of software on life and our dependence on software is rapidly increasing. Using product software is an everyday phenomenon and product software is a major worldwide industry. Yet, there are very few scientific studies reported on the engineering of product software specifically. In this paper, we discuss specifics of the software business, the various terms used for product software and provide our definition of product software. Moreover, we explain difference between product software and tailor-made software from a software development perspective and provide a new framework for the categorization of product software. This paper points out the urgent need for more research on product software and the directions. European Journal of Information Systems (2007) 16, 531–541. doi:10.1057/palgrave.ejis.3000703

Keywords: product software; tailor-made software; commercial software; open-source software

## Introduction

In the early days of computing, any software that was not provided with a computer had to be custom-built. This was the era where information systems were designed and developed according to the specific wishes of the customer. The first product software came about as a result of an agreement reached between IBM and the United States Department of Justice in the later 1960s to unbundle the software from hardware (Carmel, 1997). In the 1980s, a new class of independent software vendors started to pre-build integrated software designed to fulfil a whole range of business functions, and these offerings became known as packaged software. This resulted in the creation of thousands of product software companies, of which Microsoft, SAP, Borland, and Oracle are examples of the ones that made it into large multi-nationals with billions of revenues.

Product software accounts for substantial economic activity all over the world (OECD, 2001, 2002). In 2001 (1999), the total market of the product software industry was estimated to be 196 (154.9) billion USD, which is just 9% of the overall ICT spending of 2.1 trillion USD worldwide. ‘The product software sector is among the most rapidly growing sectors in OECD countries, with strong increases in added value, employment and R&D investments’ (OECD, 2002). Although this percentage of product software usage differs between countries, the trend in many organizations is that the make-or-buy decision falls more and more in favour of the purchasing of standard product software.

Software is present in a multitude of products, in social, business and domestic human–machine interactive systems. It includes application software and system software. Application software offers functionality to an end-user, while system software consists of low-level programs that interact with a computer at a basic level. In Figure 1, we have categorized software into micro-program, embedded software, tailor-made software and product software, according to ‘what is sold?’ and ‘number of copies’.

![](/api/attachments/PPQK38FM/fulltext/images/a4fccb053aa30014f40b60710a206d865c1ec06462d08f0cd867a922d94e2a4f.jpg)  
Figure 1 Software classification.

Within a one-time application (e.g., a satellite or spacecraft), the software embedded in the appliance is normally called a micro-program. When appliances are made in multitude, such as the software embedded in the appliances such as TVs or mobile phones, the software is normally called embedded software. Tailor-made software is made specifically for an organization and sold only once, where as product software is developed for a specific market and sold many times within that market.

Additionally, software can be either a standalone software product or software embedded in a system. Tailor-made software can be further classified into contractual tailor-made software and in-house tailormade software, while product software can be grouped into business-to-business product software and businessto-consumer software (see Table 1, based on Iberle, 2003).

Despite the economic importance of product software, there is still very limited research activity on the development of software as a product. In the field of product software, academia and companies have not yet developed any satisfactory scientific theory on integrated business models, software development and software implementation. Some separate topics, for example, requirements management, software development process, and software delivery and configuration, have been discussed in general in the software engineering area. However, issues such as integrating corporate strategy, product strategy, service strategy, and software development and developing a generation of product software or customized development methods have not been addressed yet. These form barriers for product software companies.

Most work in the IS literature refers to adoption and implementation of software products. These papers are dominantly presented from the viewpoints of the customer organization and the end-users. We take the perspective of the developing vendor as a starting point for the research, and focus on the internal processes of the vendor. Our aim is to develop scientific concepts and theories for the development and deployment of software products, which is to a great extent lacking.

Table 1 Characteristics of tailor-made software and product software

<table><tr><td>Software</td><td>Typical characteristics</td></tr><tr><td colspan="2">Tailor-made software</td></tr><tr><td>Contractual tailor-made software</td><td>Software made for one particular buyerBudget and schedule fixedPenalties for late delivery</td></tr><tr><td>In-house tailor-made software</td><td>Used to improve efficiency/effective-ness of internal organizationLimited number of end-usersPossible conflicting interests between IT-department/end-user</td></tr><tr><td colspan="2">Product software</td></tr><tr><td>Business-to-business product software</td><td>Software sold to other businessesMany different buyersCritical to the buyer&#x27;s business</td></tr><tr><td>Business-to-consumer product software</td><td>Software sold to individual buyersHigh volume buyersMarket windows and buying seasonsFailures can have fatal consequences</td></tr></table>

In order to support a strong and lasting industry that serves society with high-quality products, we need to find answers to the following questions:

1. What makes the software business unique?

2. What is an accurate definition of product software?

3. What is the difference between tailor-made software and product software?

4. How should we categorize product software?

A body of knowledge needs to be established, with theories methods and tools, possibly by generalizing experiences from a representative variety of product development. According to our observations, we are still at the beginning of a long journey.

This paper is organized as follows. First, we discuss the specifics of the software business in the next section. In a further section, the various terms in product software and our definition of product software are presented. Next, a comparison between product software and tailor-made software is provided in and then new categories of product software are explained. We conclude with some remarks on future work in the last section.

## What is specific to software business?

Like companies in other industries, software companies are faced with endless challenges: conflicting requirements, time-to-market pressure, complex platform/products and roadmap dependencies, resource allocation, and geographically dispersed teams (Cusumano & Selby, 1995; Carmel & Sawyer, 1998; Alajoutsijarvi et al., 2000; Cusumano, 2004; Xu & Brinkkemper, 2005a, b). Opposed to physical goods, software has unique characteristics as information goods (Varin, 2000). Software product development has some specific difficulties, mainly in its unpredictability. Therefore, many product software companies behave in an unpredictable manner (Boehm & Sullivan, 2000). In such an unpredictable business, it is difficult to determine when the software will be released, which features the software will have, the associated development costs or the quality of the resulting software. This may lead to dissatisfied customers and unforeseen situations. For instance, it will be difficult for a product software company to plan activities such as product promotions, customer training, maintenances support, etc. without a release date for their software. As a result, resource utilization across product software projects may become inefficient and difficult to manage when the projects fail to meet schedules or to achieve revenue targets, and the post-release cost of the software may become unexpectedly high. The unpredictable nature of software development carries high risks for a software business and may have a dramatic impact on a software company’s market position (Cusumano & Yoffie, 1999).

Despite the high-risk character of the business, software is a high return business. The software business is a special industry where making one copy or one million copies of software product costs about the same (Cusumano, 2004). Software investments can result in substantial productivity gain and strategic advantages (Brynjolfsson, 1993) like in the movie, music and medicine production industries. It is a business with up to 99% gross profit margins for product sales. However, software typically has a high fixed cost of production, which are sunk costs. If a software product is not successful, the development costs are usually not recoverable.

In the software business, productivity of the best employee and the worst one has frequently up to 10- or 20-fold difference. About 75–80% of the product-development projects are also late and over budget (Cusumano, 2004).

We finally mention that customers of software business are easily ‘locked in’ to a particular vendor because of product decisions made by someone a decade or two ago may not easily be reversed (Cusumano, 2004). Certain kinds of software, such as operating system, are also subject to network effects, causing near monopolies due to market consolidation. Those characters of software business cause fundamental differences between producing tailor-made software and product software, which provide significant support for devoting research efforts in this area.

## What is product software?

In the literature (Carmel & Sawyer, 1998; Sawyer & Guinan, 1998; Sawyer, 2000, 2001), the boundaries distinguishing shrink-wrapped software, commercial offthe-shelf software (COTS), packaged and commercial software are blurred, but the principle of ‘Make one, sell many’ is a common to them all. To understand the concept of product software, the meaning of those terms should be reviewed. Open source, both using open source software to develop product software and putting the product into open source, has affected the strategic direction of product software companies. Moreover, ASP presents a business model that provides compute-based services to customer over network. Using the application service provisioning (ASP) model, small medium enterprise (SME) would avoid the increasing costs of specialized software. For the vendors, huge costs in distributing the software to end-users can be avoided. Therefore, we also believe that open source software and ASP’s services should be considered within the context of product software. Relationships between these types of product software are presented in Figure 2.

We now discuss further the different types product software and software-based services.

Shrink-wrapped software is software on media that are boxed, shrink-wrapped and sold in stores. Nowadays shrink wrapped software can be also downloaded from the Web. Shrink-wrapped software also implies a widely supported standard platform.

COTS software (commercial off-the-shelf) is developed for a whole market instead of individual customers. COTS software is either used as is, or moderately personalized within the bounds of the application’s ability to be readily altered without changing its original functionality (e.g., modifying its appearance). A COTS product, such as an application or a component, is sold, leased, or licensed to the general public; offered by a vendor trying to profit from it; supported and evolved by the vendor, who retains the intellectual property rights; available in multiple, identical copies and used without source code modification (Brownsword et al., 2000).

![](/api/attachments/PPQK38FM/fulltext/images/7cc9b8fdebab2a9beaabc8bb0534108e48e1bcafe8970fd72d22b984c504d6ae.jpg)  
Figure 2 Relevant product software terms.

Within the context of COTS we must also consider complex COTS and customized information systems (Carney, 1997). A complex COTS is usually developed in separate products and versions to be able to bring out new features fast and to react flexibly to a changing market (Deifel, 1999). Customized information system typically integrates several COTS products with other components, commercial or developed by internalto-the-organization information technology departments or consulting/service firms (Carmel & Becker, 1995; Carmel & Sawyer, 1998; Sawyer, 2001; Cusumano & Smith, 2003).

Packaged software describes ready-made software products that can be readily obtained from software vendors and which generally require little modification or customization. Nowadays the term typically refers to upscale enterprise software suites, such as enterprise resource planning (ERP) or customer relationship management (CRM) systems. These examples of packaged software, although ready-made, rarely come ready-to-run (Light & Papazafeiropoulou, 2004; Light, 2005). Large packaged software typically requires weeks or months of deployment and implementation work to set it up for the specific needs of each individual business and often require organizational changes in the business (Light, 2001). There are also differences between packaged software and a separate software package (Carmel & Sawyer, 1998). The software package also contains materials such as utility programs or tutorial programs recorded on a medium suitable for delivery to the user and from which the user can transfer the software to a dataprocessing device. At the same time, instructional materials may include items such as handbooks and manuals, update information, and possibly support services information.

Commercial software is a software which is purchased through the retail market and must be licensed before usage. Making copies of this software without the express permission of the author or controlling party is usually prohibited.

Standard software is that software that, by certain consent, is routinely installed by the vendor and/or IT staff on most of computers within certain organizations. Standard software includes business applications and operating systems.

Open source software is software for which the underlying ‘source’ code is readily available for inspection, distribution, and modification by any interested person.

This contrasts with most commercial software, for which the source code is a closely guarded trade secret. Advocates of open source software believe that the more eyes that can see and hands that can change the source code, the quicker ‘bugs’ are found and fixed, and new features added and tested by the open source community. Most open source software has some type of license agreement for its use that may cover rights to modify, redistribute, use for commercial purposes, and so on. Open source software is not necessarily free in price, redistribution is allowed though. Both open source software and commercial software companies can make profit. In this sense, they are overlapping. The difference is formed by open source companies only being able to change for services related to the software product.

ASPs also offer application software that runs behind the web servers at hosting services. Some of them are free to use and most of them are not.

Given all these different terms in product software, it is important to standardize views and establish one common definition. We therefore propose the following definition:

Product software is defined as a packaged configuration of software components or a software-based service, with auxiliary materials, which is released for and traded in a specific market.

In this definition, we emphasize four concepts: ‘packaged components’, ‘software-based services’, ‘auxiliary materials’, and ‘release and trading’. ‘Packaged components’ refers to all software discussed above which implies code, executables and web pages. ‘Software-based services’ covers concepts like ASP sold commercial software services. ‘Auxiliary materials’ consists of software documentation, web pages (in e.g. HTML, XML, etc.), user manuals, training material, brochures and the like. Finally, the concept of ‘release and trading’ identifies product software’s commercial value. These activities not only include the release of the product software into the market, but also the deployment of the customer system, training users, and related commercial activities. For some software products, adaptation, integrations with other applications, customizations and maintenance services are also needed.

## Differences between product software and tailormade software

The differences in customers, markets, and goals of product software and tailor-made software are so diverse that comparisons are often difficult (Carmel & Sawyer, 1998; Sawyer & Guinan, 1998). Looking from a software engineering point of view, a number of basic differences between product software and tailor-made software can be observed. Firstly, market introduction requires precise synchronization of dependable software engineering activities for product software, that is, market oriented instead of working for one customer in tailor-made software. Secondly, product software requires installation and usage in different organizations, with different hardware and software platforms, while tailor-made software has fixed conditions of the hardware and software platforms. Thirdly, with product software the vendor normally retains ownership of the software and auxiliary materials and licences customers to use the software, while a tailor made piece of software will generally be owned by the customer, not the vendor.

In the following sections we will discuss the differences between the development process of product software and tailor-made software, specifically differences in the development life cycles, in requirements and release management, in architecture and in delivery and implementation.

## Differences in development life cycle and development methods

Generally, there are two categories of software development methods:

\- Sequential method: Using a sequential approach, each phase of the development life cycle is performed and completed before the next phase is started. Major development phases are defined as: Requirements, Design, Code, Test and Deployment phases. Each of the phases is performed only once, within the entire life cycle, and each phase is performed to its completion before moving onto the next phase. The sequential model builds on the assumption that the problem to be solved can be completely understood and described before a solution is designed. A design that satisfies all aspects of a problem can be specified before implementation. All implementation can be done before validation and delivery. This approach is most suitable for developing software where the requirements are clearly stated and stable.

\- Incremental method: The incremental model is a software development model where software is designed, implemented and tested incrementally. It involves both development and maintenance. This approach is essentially a rapid prototyping framework, which assumes the requirements will become more complete, and change as the development progresses. The development life-cycle has short iterations, each including collection requirements, designing, coding, testing and deploying for that small part of the software system.

Most tailor-made software development follows the five phases described in the sequential model and at some point the software/information system project is ‘finished’. With product software, however, there is a continual need to improve the product, so there is no fixed point when the development is finished. This makes the incremental model a more appropriate model for the development product software.

Microsoft uses a ‘synch-and-stabilize’ model for their software development. In this model, there are three different phases. The life cycle model they use (Cusumano & Selby, 1995) includes:

\- Planning phase:

\* create vision statement, based on user input,

\* define functionality, based on version, just enough to arrange teams,

\* schedule and arrange teams, per feature.

\- Development phase:

\* implement basic functionality, the most critical features, first 1/3 of features,

\* implement extra functionality, second 1/3 of features,

\* implement more functionality, the least critical features, final 1/3 of features.

\- Stabilization phase:

\* internal testing, in house testing,

\* external testing, the well know beta versions,

\* release preparation.

Another popular way of development product software is arrange specialized teams for different development phases. These specialized teams can work in parallel where the following phases are used:

\- Requirements management: The requirements needed for the first release normally stem from perceived deficiencies in the marketplace. Other requirements could come from developers, customers, analysis and interviewing of different potential customers, from questionnaires and from market analysis. All constant flow of requirements needs to be registered and managed (Natt och Dag et al., 2005; van de Weerd et al., 2006).

\- Release decision: A few days before the start of the next development cycle a decision must be made about which features will be in the next release. For each bug report there is a decision to make: must it be solved in the next release or is it not that important and will it be decided in the next release decision phase.

\- Development: In this phase, the chosen features will be implemented and tested. This phase can be implemented as a cycle model with steps like choosing, implementing and testing a requirement. This can be done in parallel per feature.

\- Preparation for distribution: If the product is fully tested and declared ready for distribution, it is time to build the setup and make the products.

\- Sales and distribution: The final goal to sell the product software in a specific market.

There are many different development methods that could easily adopted by product software development for different purposes, such as Rapid Application Development (RAD) (McConnell, 1996), Rational Unified Process (RUP) (Kruchten, 2000), Scrum (Schwaber & Beedle, 2001), Dynamic Systems Development Method (DSDM) (Stapleton & Constable, 1997), eXtreme Programming (XP) (Beck, 2000) and so on.

In short, developing product software is different with developing tailor-made software from the development life cycle perspective. At a certain time, a tailor-made program is ‘finished’, after which the maintenance phases starts. Product software is continuously under development. After finishing one release, there will be others. Some bugs will be fixed in a later release or service packs or patches will be provided. Developing product software and developing tailor-made software can thus use different development methods.

## Differences in requirements and release management

A major difference between tailor-made software and product software is the origins of the requirements. With tailor-made software the source of requirements is clear, since there is a known customer for the software. It is not so clear for product software. The requirements for the first release normally stem from perceived deficiencies in the marketplace; other requirements come from market analysis and potential customer interview, etc.

Requirements management for product software includes capturing market trends, analysing requirements and releasing the software at the right time (e.g. in time for the Christmas shopping season). This is key for the software business (Sawyer & Guinan, 1998; Carlshamre & Regnell, 2000; Natt och Dag et al., 2004). It is the first step in the development of product software. Mapping market trends to product software design is becoming the central issue in new product software development (Garvin, 1998; Hauser & Clausing, 1998). It is also important to use customer feedback during the product life cycle to enhance customer satisfaction. Moreover, one must still look for features that could allow the product to enter a completely different market, that is, change the productmarket combination (Rao & Klein, 1994).

Product software firms also have a major pressure on time-to-market. This means that for the product strategy, it is essential to prioritize the customer requirements (Natt och Dag et al., 2004) as external pressures may mean that only a limited number of the requirements can be initially implemented (Natt och Dag et al., 2005). In short, it is important to determine when a software product will be released, the features the product will have, the associated development costs and the resulting product quality. Product software is often offered to a market through releases with significant increases in functionality. This requires careful release planning and requirements prioritization (Regnell et al., 2001).

There are usually a diverse set of stakeholders (including customers) who determine the requirements of a piece of product software. Selecting and prioritizing requirements are significant processes in establishing a business strategy of a software firm. Release management is then concerned with the overall management of all tasks concerning planning, building, testing, version control and configuration management (van de Weerd et al., 2006).

After product software has been developed, different tests must be conducted before the product is put into operational use (Myers, 1979; Sommerville, 1995; Pressman, 2000; Vliet, 2000). The product software might first be internally released for alpha testing, which is a very early version of a software product that may not contain all of the features that are planned for the final version. The objective of alpha testing is to find and eliminate the most obvious defects. Subsequently, the software product can be released to a limited number of external users for beta testing to test the software for all functions in different situations, and to find those failures likely to show in actual use. After the second beta test, the product software can be finally released to its intended markets.

Releasing tailor-made software to one known customer or internal organization will be different to releasing product software to mass markets. The release date of tailor-made software is normally agreed upon and included within the contract. With product software, the release date is determined by the software company without involvement of customers. Therefore, while tailor-made software has no strong need for release management, it is a crucial stage in product software development.

## Differences in architecture

There is not really a standard to evaluate whether architectures are good or bad for developing product software. There are however a few aspects that are more important for developing product software than for building a tailor-made software.

Software architecture is fundamental for the development of product software. The software architecture can be seen as attempting to codify the structural commonality among a series of product software so that the highlevel design decisions inherent in each product need not be re-invented, re-validated and re-described (Bass et al., 1998). The architecture on which product software is built must be able to adapt easily to new requirements, not only to new user requirements but also to the always changing environment (new releases of the operating systems, middleware and changes in the underlying database management system). The different components in the architecture need to be as independent as possible (weak coupling). It is common to sell different versions of a product for different users (stand-alone, multi-user or enterprise versions) or different operating systems (Windows, Mac or Unix), which require an adequate device-independent software architecture.

In short, a future proof architecture is crucial for developing product software. The architecture needs to define clearly distinguishable components for achieving long-term uses. Architecture design is not so crucial for developing tailor-made software.

## Differences in delivery and implementation

In developing tailor-made software, the cost and specifics of delivery and implementation will have been taken into account within the contract. It will involve installation (probably manual) of the software at a limited number of known customer sites.

Product software on the other hand must be delivered to a large number of unknown customers (potentially millions) and implemented on a huge number of unknown systems. It is obviously too expensive to manually deliver or customize product software for all potential customers. So the delivery and implementation to market is an important consideration for product software.

Typical product software delivery consists of configuration management and documentation. Software configuration management is the control of the evolution of complex systems (Estublier, 2000) and its goal is to keep evolving product software under control and help satisfy time and quality constraints. Software configuration management focuses on versioning (Wingerd & Seiwald, 1997), rebuilding (Feldman, 1979), composition (Tryggeseth et al., 1995), and synchronized team coordination (Buffenbarger, 1995).

After more than 30 years of software development, most software applications, such as large-scale information systems and ERP systems, are constructed by adapting existing product software (Light, 2005). Researchers in the information systems area have argued that customer satisfaction is critical to adoption and use of information systems (Leong, 2003; Light & Papazafeiropoulou, 2004). While product software firms aim to extend their solutions into as many different settings as possible, there are two choices for implementing product software at the IT infrastructure with the customer systems. Product software firms can do implementation (such as training, installation and custom services) by themselves or outsource this part of business to consulting firms. Both business strategies for implementation have there own advantages and disadvantages, but this falls beyond the scope of this paper (Nelson et al., 1996; Cusumano, 2004).

## Overview of differences between tailor-made and product software

In this section, we have explored differences between product software and tailor-made software from a software development perspective. The development life cycles of product software and tailor-made software are different. While tailor-made software goes though five software development stages, product software is continuously under development. Requirements and release management are also different between product software and tailor-made software. Management and prioritization of the requirements and allocation of different requirements into different product software releases is a distinguishing factor between developing product software and tailor-made software. Furthermore, choosing a useful long-term architecture is especially critical for product software. Moreover, delivery and implementation have been identified as unique activities for product software. Table 2 outlines differences between tailormade software and product software from a development perspective.

Most widely known software project management methods, development methods, software improvement methods, standards and implementation methods ignore the specific issues and needs of product software. For example, there is little support for software release decisions; the different roles and responsibilities, the required information as input to the release decision, the release process itself, and product implementation aspects. Delivery of product software to a large volume of customers is also a relatively new issue for software engineering research (Jansen et al., 2006). Studying differences between tailor-made software and product software has a scientific relevance, and will be contribution to the existing body of knowledge.

Although we have discussed the differences between tailor-made software and product software, the line between tailor-made software and product software is actually not sharp. Product software often originates from tailor-made software, so from this perspective, tailormade software and product software share the same development processes.

On the other hand, large packaged software, such as ERP software, needs to be changed or extended to provide the available functionalities to meet the needs of an organization (Light, 2001). The process of the larger packaged software customization can use the same methods as used for tailor-made information systems.

Developing tailor-made software or information systems has a far longer history than development of product software. The product software industry can learn a lot from the experiences, practices and lessons obtained throughout the years, and focus on the particular nature of developing products.

## Categories of product software

Product software ranges from small personal computer applications to large distributed systems, from common accounting systems to strategic operational systems, from commercial software to open source software. There are several classifications of product software. For example, Glass & Vessey (1995) classified commercial products by application domain . In the papers Morisio & Torchiano (2002), Carney & Long (2000), Konttio, (1996), Morisio & Tsoukı´as (1997), Ochs et al. (2001) and Jaccheri & Torchiano (2002) several categories of COTS software are identified by defining a set of attributes.

## Existing classification of product software

Previously product software has been classified in different ways. From the architectural standards view, possible architectural patterns are centralized, clientserver, two-tier, three-tier, peer-to-peer, pipe and filter and blackboard, etc. (Bass et al., 1998). For example, the following Microsoft products can be classified by their differences in architecture; Microsoft Internet Explorer uses client engine; Microsoft Biztalk server 2000 uses server engines and Microsoft Access uses architectural data level.

Table 2 Comparison of tailor-made software and product software

<table><tr><td rowspan="2">Development aspect</td><td colspan="2">Tailor-made software</td><td colspan="2">Product software</td></tr><tr><td>Contractual tailor-made software</td><td>In-house tailor-made software</td><td>Business-to-business product software</td><td>Business-to-consumer product software</td></tr><tr><td>Development life-cycle &amp; development methods</td><td>Could follow &#x27;requirement-design-code-test-deploy&#x27; life-cycle;Sequential or iterative methods and sequential model could be benefit.</td><td>Could follow &#x27;require-ment-design-code-test-deploy&#x27; life-cycle;Sequential or iterative methods and sequential model could be benefit.</td><td>Various development life-cycle;Iterative methods.</td><td>Various develop-ment life-cycle;Iterative methods.</td></tr><tr><td>Requirements and release management</td><td>One known consumerRelease date is fixed, with possible penalties for late delivery</td><td>Limited number of end-usersRelease decisions can have certain flexibilities.</td><td>Market determines requirementsRelease decisions are critical to the customer&#x27;s business</td><td>Market determines requirements;Release decisions are important for the vendor;Release decisions should also consider buying seasons.</td></tr><tr><td>Architecture</td><td>It is not so critical;It is chosen by the developers.</td><td>It is not so critical.It is chosen by internal IT department of the organization which would have possible conflicting interests</td><td>It is critical for the vendor;Required a future proof architecture</td><td>It is critical for the vendor;Required a future proof architecture</td></tr><tr><td>Delivery and implementation</td><td>Facing penalties for late delivery;Possible delivery and implementing final system on scene.</td><td>Possible delivery and implementing the final system on scene.</td><td>Delivery is critical for the vendor;Implementation is critical for the customer&#x27;s business</td><td>Delivery is critical for the vendor</td></tr></table>

According to the OECD, product software can be categorized into system infrastructure software, software development tools, or application software (OECD, 2002). ‘System infrastructure software’ includes systemlevel operating system and other software, middleware, system management, and security software. ‘Software development tools’ contains database management systems, development environments, development lifecycle management, and internet tools. ‘Application software’ covers ERP systems, cross-industry business software, CAD/CAM/CAE and other vertical industry business software.

## Product software classification from development perspectives

A product flow pipeline includes some operations and stocks, which are represented by rectangles and triangles respectively. The product flow pipeline represents a primary business process, which shows how a product is produced. Besides, some decoupling points can be used to show where supply and demand meet and where the primary stock is located in a primary business process.

To develop product software, there are four development stages (Xu & Brinkkemper, 2005a, b), namely, requirements and architectural design, development, delivery, and implementation service. We use them as the operations in the product flow pipeline for product software (see Figure 3). During the production process, all components, prototype system, stocks of product software and local stock need places to be stored after each operation. The relevant stocks for product software are design specifications after the operation of the requirements and architectural design (D), source codes and packaged components after the operation of the development (S), delivered software after the operation of the delivery (P), and running systems after the operation of the implementation service (R). Figure 3 shows a product flow pipeline for product software and its decoupling points (point A, B, and C in Figure 3). Decoupling points are the points in the product flow pipeline where the business transaction between the vendor and the customer is made. Figure 3 shows therefore also a variety of business models in the product software industry.

Software firms produce or buy many different components for building product software. The components need to be run and tested as a system. After all components work reasonably well together, they are packaged as products. Different components or source codes can also be sold or licensed. This process describes the decoupling point C, the packaged components and source codes are sold to meet the other businesses. Both open source and closed source packaged components belong to this category.

![](/api/attachments/PPQK38FM/fulltext/images/3fa60a69d7e8f7165e57fd37af288561a89fe451964be9c9304eff46b8e713cc.jpg)  
Figure 3 Product flow pipeline for product software and its decoupling points.

Those packaged components and source codes can be continually developed as packaged software that allows different functional choices to be delivered to different countries or markets. This process describes the decoupling point B, the packaged components and software sold to meet the customer demands. Typical product software like shrink-wrapped software, some of COTS and packaged software belong to the second category. As an example, Microsoft Office or Symantec AntiVirus can be purchased in local stores as it is easy enough for most people to install and update by themselves.

Conversely, enterprise product software like the SAP R3 ERP and Siebel CRM are not simple to deploy. After a lengthy selection and contracting phase, a useable installation has to be implemented by specialists. The customer may require changes to be made within their organization to fully utilize the software and will only be able to use this software after the custom implementation. The decoupling point will be thus at the position A in Figure 3. In general, large packaged software and software-based services belong to this last category.

From a development perspective, product software can be classified into three categories according to the position of the decoupling point. The first category is some software products like software components or source codes that could be sold or licensed to other business partners. Those semi-finished products can be critical to other business partners for further development of product software or software-based services. The second category contains software products that are distributed by vendors and can be installed by the customers without special help. The third category includes software products that require professional help for implementation into the business (Table 3).

The way we categorized product software is useful for aligning different categories of product software with different software development methods. There are widely known software project management methods, development methods, maturity models and implementation methods. How and when should one adopt which methods is one of our main concerns and an option for future research. A clear classification of product software is the first step to achieve our goals.

Table 3 Product software categories

<table><tr><td>Product software category</td><td>Typical characteristics</td></tr><tr><td>Semi-finished-products</td><td>Software made for further developmentCritical for other business partners.</td></tr><tr><td>Self-install software</td><td>Software made for the end-user The required installation should be straightforward.</td></tr><tr><td>Professional-deploy software</td><td>Software requiring professional deploymentCertain products may even require organizational changes.</td></tr></table>

## Conclusions

In this paper, we presented the specific characters of the business of software product and have reviewed product software-related concepts and provided our definition of product software.

Developing product software is different from building tailor-made software and we have investigated the differences from various perspectives. We believe that the main differences are found in development life cycles, requirements and release management, architecture, and delivery and implementation. By using an appropriate development life cycle, it is possible to decrease the release cycle time and improve product software quality. From an architecture design perspective, it is important to define a useful long-term architecture, which can easily be adapted to changes in user requirements, technical platforms and customer environments.

Choosing a proper delivery approach is definitely important for product software business.

Furthermore, we proposed three categories of product software according to the product flow pipeline of product software and their decoupling points. The new categories classify product software from a software development perspective and the moment the vendor and customer complete their business transaction. It implies that different categories of product software should use or adopt different methods for development.

In our future research, we will focus on product software development as a product and as a web-based

## About the authors

Lai Xu is a Senior Research Scientist at CSIRO ICT Centre, Australia. Previously, she worked as a post-doctoral researcher at the Organization and Information Group of the Institute of Information and Computing Sciences of the Utrecht University, The Netherlands and at the Artificial Intelligence group of the Department of Computer Science of the Free University Amsterdam. She received her Ph.D. in Computerized Information Systems from Tilburg University, the Netherlands in 2004. Her main research areas are in process integration, multiparty process monitoring, web services and serviceoriented applications, development methods for product software.

Sjaak Brinkkemper is full professor of organization and information at the Department of Information and Computing Sciences of the Utrecht University, The

## References

ALAJOUTSIJARVI K, MANNERMAA K and TIKKANEN H (2000) Customer relationships and the small software firm a framework for understanding challenges faced in marketing. Information and Management 37, 153–159.

BASS L, CLEMENTS P and KAZMAN R (1998) Software Architecture in Practice. Addison-Wesley, Reading, MA.

BECK K (2000) Extreme Programming Explained: Embrace Change. Addison-Wesley, Reading, MA.

BOEHM BW and SULLIVAN KJ (2000) Software Economics: A Roadmap. ACM Press, New York.

BROWNSWORD L, OBERNDORF T and SLEDGE C (2000) Developing new processes for cots-based system. IEEE Software 17, 83–86.

BRYNJOLFSSON E (1993) The productivity paradox of information technology. Communication of the ACM 36, 66–77.

BUFFENBARGER J (1995) Syntactic software merging. In Software Configuration Management: ICSE SCM-4 and SCM-5 Workshops: Selected Papers (ESTUBLIER J, Ed), Lecture Notes in Computer Science, Vol. 1005, Springer Verlag, Berlin, pp 153–172.

CARLSHAMRE P and REGNELL B (2000) Requirements lifecycle management and release planning in market-driven requirements engineering processes. In 11th International Workshop on Database and Expert Systems Applications (DEXA’00). Digital Library, IEEE Computer Society Press, Silver Spring, MD, pp 961–965.

service. Specifically, we will concentrate on how product software companies structure their internal development roles for developing different kinds of product software and software-based services.

## Acknowledgements

We thank Slinger Jansen, Gillian van Hees, the anonymous reviewers, and the editors of the special issue for their valuable remarks that led to considerable improvement of the paper.

Netherlands. He leads a group of about 20 researchers specialized in product software development and entrepreneurship. The main research themes of the group are methodology of product software development, implementation and adoption, and business-economic aspects of the product software industry.

Before, he was a consultant at the Vanenburg Group and a Chief Architect at Baan. Before Baan, he held academic positions at the University of Twente and the University of Nijmegen, both in the Netherlands, and visiting positions at the University of Texas at Austin (U.S.A.) and Tokyo Institute of Technology (Japan). He holds an M.Sc. and a Ph.D. in Mathematics and Computer Science from the University of Nijmegen. He has published six books and about 120 papers on his research interests: software product development, information systems methodology, meta-modelling and method engineering.

CARMEL E (1997) American hegemony in packaged software trade and the culture of software. The Information Society 12, 125–142.

CARMEL E and BECKER S. (1995) A process model for packaged software development. IEEE Transactions on Engineering Management 41, 50–61.

CARMEL E and SAWYER S (1998) Packaged software development teams: what makes them different? Information Technology & People 11, 7–19.

CARNEY D (1997) Assembling large systems from cots components: opportunities, cautions, and complexities. SEI Monographs on Use of Commercial Software in Government Systems. Software Engineering Institute, Pittsburgh, USA.

CARNEY D and LONG F. (2000) What do you mean by cots? Finally, a useful answer. IEEE Software 17, 83–86.

CUSUMANO MA (2004) The Business of Software. Free Press, New York.

CUSUMANO MA and SELBY RW (1995) Microsoft Secrets. Free Press, New York.

CUSUMANO MA and SMITH SA (2003) Beyond the waterfall: Software development at Microsoft. Technical report, Massachusetts Institute of Technology (MIT), Sloan School of Management.

CUSUMANO MA and YOFFIE DB (1999) Software development on internet time. Computer 32(10), 60–69.

DEIFEL B (1999) A model for version planning of CCOTS. In Proceedings of the Workshop on Software Change and Evolution (SCE’99) (RAJLICH V, Ed), IEEE Computer Society Press, Los Angeles, USA.

ESTUBLIER J (2000) Software configuration management: a roadmap. In The Future of Software Engineering 2000 (FINKELSTEIN A, Ed), pp 279– 289, ACM Press, New York.

FELDMAN SI (1979) Make-a program for maintaining computer programs. Software – Practice and Experience 9, 255–265.

GARVIN DA (1998) Managing Quality: The Strategic and Competitive Edge. Free Press, New York.

GLASS RL and VESSEY I (1995) Contemporary application-domain taxonomies. IEEE Software 12, 63–76.

HAUSER J and CLAUSING D (1988) The house of quality. Harvard Business Review 66, 63–73.

IBERLE K (2003) They don’t care about quality. Paper presented at the Software Testing and Analysis & Review (STAR) East Conference. Retrieved 28 February 2006, from http://www.kiberle.com/ articles.htm.

JACCHERI ML and TORCHIANO M (2002) Classifying COTS products. In Software Quality – ECSQ‘02, 7th International Conference (KONTIO J and CONRADI R, Eds), Lecture Notes in Computer Science, Vol. 2349, Springer-Verlag, Berlin, pp 246–255.

JANSEN S, BALLINTIJN $\mathsf { G } ,$ BRINKKEMPER S and VAN NIEUWLAND A (2006) Integrated development and maintenance for the release, delivery, deployment, and customization of product software: a case study in mass-market ERP software. Journal of Software Maintenance and Evolution: Research and Practice 18(2), 133–151.

KONTIO J (1996) A case study in applying a systematic method for COTS selection. In Proceedings of the 18th international conference on Software engineering (ICSE ’96). IEEE Computer Society Press, Silver Spring, MD, pp 201–209, see http://esdl2.computer.org/persagen/DLPublication. jsp?pubtype=p&acronym=icse.

KRUCHTEN P. (2000) The Rational Unified Process: An Introduction. Addison-Wesley, Reading, MA.

LEONG L (2003) Theoretical Models in IS Research and the Technology Acceptance Model (TAM). Idea Group Publishing, Hershey, PA, USA.

LIGHT B (2001) The maintenance implications of the customization of ERP software. The Journal of Software Maintenance: Research and Practice 13(6), 415–430.

LIGHT B (2005) Potential pitfalls in packaged software adoption. Communications of the Association for Computing Machinery 48(5), 119–121.

LIGHT B and PAPAZAFEIROPOULOU A (2004) Reasons behind ERP package adoption: A diffusion of innovations perspective. In Proceedings of the 12th European Conference on Information Systems (LEINO T, SAARINEN T and KLEIN S, Eds), pp 1062–1074, Turku, Finland.

MCCONNELL S (1996) Rapid Development: Taming Wild Software Schedules. Microsoft Press, Redmont, WA.

MORISIO M and TORCHIANO M (2002) Definition and classification of COTS: a proposal. In Proceedings of the first International Conference on COTS Based Software Systems (ICCBBS’ 2002) (DEAN J and GRAVEL T, Eds), Lecture Notes in Computer Science, Vol. 2255, Springer-Verlag, Berlin, pp 165–175.

MORISIO M and TSOUK´ıAS A (1997) Iusware: A methodology for the evaluation and selection of software products. IEEE Proceedings – Software 144, 162–174.

MYERS GJ (1979) The Art of Software Testing. John Wiley & Sons, New York.

NATT OCH DAG J, GERVASI V and BRINKKEMPER S (2005) A linguisticengineering approach to large-scale requirements management. IEEE Software 22, 32–39.

NATT OCH DAG J, GERVASI V, BRINKKEMPER S and REGNELL B (2004) Speeding up requirements management in a product software company: Linking customer wishes to product requirements through linguistic engineering. In Proceedings of the 12th International Requirements

Engineering Conference. IEEE Computer Society Press, Silver Spring, MD, pp 283–294, see http://esdl2.computer.org/persagen/DLPublication. jsp?pubtype ¼ p&acronym ¼ re.

NELSON P, RICHMOND W and SEIDMANN A. (1996) Two dimensions of software acquisition. Communication ACM 39, 29–35.

OCHS M, PFAHL D, CHROBOK-DIENING G and NOTHHELFER-KOLB B (2001) A method for efficient measurement-based COTS assessment and selection-method description and evaluation results. In Proceedings of the Seventh International Software Metrics Symposium (METRICS’01). IEEE Computer Society Press, Silver Spring, MD, pp 285–297, see http://esdl2.computer.org/persagen/DLPublication.jsp?pubtype ¼ p&acronym ¼ metrics.

OECD (2001) The software sector: Growth, structure and policy issues. OECD Report DSTI/ICCP/IE(2000)8/REV2.

OECD (2002) Highlights of the OECD information technology outlook 2002. OECD Report.

PRESSMAN RS (2000) Software Engineering: A Practitioner’s Approach. McGraw-Hill, New York.

RAO P and KLEIN JA (1994) Growing importance of marketing strategies for the software industry. Industrial Marketing Management 21, 29–37.

REGNELL B, Ho¨ST M and NATT OCH DAG J (2001) An industrial case study on distributed prioritization in market-driven requirements engineering for packaged software. Requirements Engineering 6, 51–62.

SAWYER S (2000) Packaged software: implications of the differences from custom approaches to software development. European Journal of Information System 9, 47–58.

SAWYER S (2001) A market-based perspective on information systems development. Communications of the ACM 44, 97–102.

SAWYER S and GUINAN PJ (1998) Software development: processes and performance. IBM system Journal 37, 552–569.

SCHWABER K and BEEDLE M (2001) Agile Software Development with Scrum. Prentice-Hall, Englewood, Cliffs, NJ.

SOMMERVILLE I (1995) Software Engineering. Addison-Wesley, Reading, MA.

STAPLETON J and CONSTABLE P (1997) DSDM: A Framework for Business Centered Development. Addison-Wesley, Reading, MA.

TRYGGESETH E, GULLA B and CONRADI R (1995) Modeling systems with variability using the proteus configuration language. In Software Configuration Management – ICSE SCM-4 and SCM5-5 Workshops, Selected Papers (JACKY ESTUBLIER, Ed), pp 216–240, Springer Verlag, Berlin.

VARIN HR (2000) Buying, sharing and renting information goods. Journal of Industrial Economics 48, 473–488.

VAN VLIET H (2000) Software Engineering Principles and Practice, 2nd edn, John Wiley & Sons, New York.

VAN DE WEERD I, BRINKKEMPER S, NIEUWENHUIS R, VERSENDAAL J and BIJLSMA L (2006) Towards a reference framework for software product management. In Proceedings of the 14th International Requirements Engineering Conference. IEEE Computer Science Press, pp 312–315.

WINGERD L and SEIWALD C (1997) Constructing a large product with jam. In Proceedings of the SCM-7 Workshop on Software Configuration Management, Lecture Notes in Computer Science, Vol. 1235, Springer-Verlag, Berlin, pp 36–48.

XU L and BRINKKEMPER S (2005a) Concepts and research framework of product software. In Proceedings of the first International Workshop on Development and Deployment of Product Software 2005 (DDoPS’05) (DEY PP et al., Eds), pp 1–11, US Education Service 2005, San Diego.

XU L and BRINKKEMPER S (2005b) Concepts of product software: Paving the road for urgently needed research. In The first International Workshop on Philosophical Foundations of Information Systems Engineering (PHISE’05) (CESER J ACUN˜ A and BELEN VELA, Eds), FEUP Press, Porto, Portugal, pp 523–528.
