---
otero_id: 1384
otero_key: "7BZEDDV6"
title: "Generating Value Through Open Source: Software Service Market Regulation and Licensing Policy"
authors: "Terrence August; Hyoduk Shin; Tunay I. Tunca"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0726"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
## Information Systems Research

## H4R

![](/api/attachments/7BZEDDV6/fulltext/images/a518c1cbd9832b39c917aae5f7e129a8ea1d6988db0fce2922bac40e5123d2c1.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

## Generating Value Through Open Source: Software Service Market Regulation and Licensing Policy

Terrence August, Hyoduk Shin, Tunay I. Tunca

To cite this article:

Terrence August, Hyoduk Shin, Tunay I. Tunca (2017) Generating Value Through Open Source: Software Service Market Regulation and Licensing Policy. Information Systems Research

Published online in Articles in Advance 29 Nov 2017

https://doi.org/10.1287/isre.2017.0726

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2017, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Generating Value Through Open Source: Software Service Market Regulation and Licensing Policy

Terrence August,<sup>a,</sup> <sup>b</sup> Hyoduk Shin,<sup>a</sup> Tunay I. Tunca<sup>c</sup>

<sup>a</sup> Rady School of Management, University of California, San Diego, La Jolla, California 92093; <sup>b</sup> Korea University Business School, Seoul 136-701, Korea; <sup>c</sup> Robert H. Smith School of Business, University of Maryland, College Park, Maryland 20742 Contact: taugust@ucsd.edu, http://orcid.org/0000-0002-4085-1147 (TA); hshin@rady.ucsd.edu (HS); ttunca@rhsmith.umd.edu (TIT)

Received: November 30, 2015 Revised: December 23, 2016; March 4, 2017 Accepted: April 11, 2017 Published Online in Articles in Advance: November 29, 2017

https://doi.org/10.1287/isre.2017.0726

Copyright: © 2017 INFORMS

Abstract. In the software industry, commercial open-source software vendors have recognized that providing services to help businesses derive greater value in the implementation of open source–based systems can be a profitable business model. Moreover, society may greatly benefit when software originators choose an open-source development strategy as their products become widely available, readily customizable, and open to community contributions. In this study, we present an economic model to study how software licensing attributes afect a software originator’s decisions, aiming to provide policy makers with insights into how welfare-improving, open-source outcomes can be incentivized. We show that when a competing contributor is apt at reaping the benefits of software development investment, a less restrictive open source license (e.g., Berkeley Software Distribution, or BSD style) can improve welfare. On the other hand, when the originator is better at leveraging investment and service costs are high, a more restrictive license (e.g., General Public License, or GPL style) can be best for social welfare even when a contributor can cost-eficiently develop the software.

History: Sanjeev Dewan, Senior Editor; Wolfgang Ketter, Associate Editor. Funding: This material is based on work partially supported by the National Science Foundation under [Grant CNS-0954234]. Supplemental Material: The opline appendix is available at bttps://doi org /10.1287 /isre 2017 0726

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0726.

Keywords: open-source software • software licensing • services market • proprietary software

## 1. Introduction

Open-source software (OSS) has assumed an increasing role in the operations of businesses and governments. Surveying organizations with either 500 or more employees or revenues in excess of \$500 million, the Linux Foundation found that the use of Linux for mission-critical workloads has increased from 60% in 2010 to 73% in 2012 (Linux Foundation 2013). Broadly speaking, businesses indicate that the improved qualities of OSS over the past two decades have now made OSS preferable to proprietary alternatives in many implementation contexts (Noyes 2014). In the public sector, the U.S. Department of Defense has advocated OSS by formalizing their position in the plan Open Technology Development, which makes openness a priority for both internally developed and externally acquired software (Herz et al. 2006). The UK government recently also indicated a clear preference for OSS in its Government Service Design Manual (Glick 2013). Increasingly, governments have realized that migration to OSS enables a shift in information technology (IT) “spend” from proprietary products to professional services (Herz et al. 2006).

OSS quality benefits from the eforts and investments of both originators and others who contribute to its development. As Craig Paulnock, an Associate VP at YMCA states, “Open-source software maintains its high quality by empowering a large number of users from diverse backgrounds with unique perspectives to make frequent updates to improve the value and flexibility of the code” (Paulnock 2016). Development eforts to improve OSS quality are typically distributed across various but necessary activities. Ibrahim Haddad, head of the open source innovation group at Samsung Research America suggests that OSS allows Samsung “to concentrate on aspects of product development where the company can actually distinguish itself” (King 2014). In a similar vein, Red Hat’s CEO James Whitehurst indicates, “So the innovation, or the original feature development, happens in the open source community. But all of the downstream sustaining engineering, the patching, all of that’s what we do” (Vanian 2016). The open nature of OSS is a mechanism that empowers contributors to significantly increase software quality through updates, patches, and new features by distributing the cost of development across all contributors who directly benefit from the software’s existence (Lakshminarayanan 2014, Columbus 2016). Many of these strategic contributors leverage their investments and established expertise by ofering professional services.

In fact, the provision of value-added services has been the primary source of revenue for commercial OSS.<sup>1</sup> Today, Red Hat generates more than \$1 billion in revenues for subscription-based support services driven mostly by its two flagship products: Red Hat Enterprise Linux and JBoss (McMillan 2012). Cloudera, which provides an open-source distribution of Apache Hadoop called CDH, invests heavily in the open-source projects composing CDH and similarly relies on the services market to generate revenues. Cloudera recently was backed by Intel with a \$740 million investment to support its revenue goals (Cohan 2013, Clark 2014). These examples underscore how high-quality software alone often does not benefit an organization unless it is suficiently integrated with business processes to generate value. For organizations to achieve such higher value-added implementations, they require services, and it is the firms who have developed extensive expertise that are in the best position to help as is the case for Red Hat and Cloudera in their respective markets. While there are many firms who could also provide basic support and services for Linux and Apache Hadoop, the quality associated with obtaining services from firms such as Red Hat and Cloudera is considerably higher because of their substantial investments in developing this expertise.

With the services market, firms have an economically viable business model that can justify investments in the development of OSS even though the software itself is essentially available for free. For a software originator, an important advantage of pursuing an open-source path is that the quality of its OSS product leverages efort investments from the community, which in turn increases the value derived by its consumers on service contracts. However, some contributors to OSS can also be motivated to invest in development in an efort to gain expertise and compete for these service contracts.<sup>2</sup> Thus, a software originator going open source faces a trade-of between an increase in the quality of software and services by leveraging community contributions and an increase in the services market competition from these extrinsically motivated contributors as well as the many providers of basic services packages. Examples of strategic contributors who invest efort and compete for OSS service contracts include Shadow-Soft (JBoss), Synolia (Sugar-CRM), Bista Solutions (OpenERP), and Hortonworks (Hadoop).<sup>3</sup> On the other hand, a software originator could simply pursue a more traditional, proprietary approach by which it does not directly benefit from the eforts of third-party developers because of the closedness of the source code, but it can generate revenues by selling copies of the software at a positive price.

From a social perspective, however, there are several benefits associated with a software originator choosing the open-source path. First, the broader participation in software development that characterizes OSS can boost quality significantly while keeping development costs relatively low, with distributed costs being more eficiently incurred (Holmstrom and Milgrom 1991). Second, when active contributors to OSS invest in development and expertise, there is greater competition in the services market, which can also be beneficial to consumers. Third, by contrast to proprietary software, an originator of OSS does not (practically) have the ability to charge for the software itself given that it is open and freely downloadable. This additional pricing power retained by a proprietary originator has a negative efect on both consumer surplus and the incentives of potential service providers. Taken together, there can be gainful opportunities to substantially increase social welfare if open-source outcomes are encouraged to prevail in certain software markets. On the other hand, because of the increased competition it faces in the services market, an originator may have a reduced incentive to invest in development since its return on investment could be lower under open source. Its reduced investment can lead to lower quality solutions brought to market if not adequately compensated by increased contributions from the community. Therefore, despite the promising benefits associated with OSS, it is critical to understand how the strategic interactions between an OSS originator and contributor ultimately determine market outcomes.

In this paper, our goal is to present insights into how regulation and policy can provide incentives to help stimulate open-source outcomes. The primary factor we focus on in this study is OSS licensing. By OSS licensing, we refer to the terms and conditions that govern an OSS product, generally specifying the rules by which an end user or developer of the software can use, modify, and/or redistribute the software. OSS licenses vary significantly in their level of restrictiveness. The most common broad forms of licensing are GNU GPL (General Public License) and BSD (Berkeley Software Distribution) with GPL being the most widely used license employed (Fishman 2004). GPL is based on the notion of “copyleft,” which requires that derivative works of the software also adopt the GPL license. Under this license, all code that others develop based on the originator’s software must be made publicly available, including potential use by the originator. Thus, a GPL-style license is a relatively more restrictive license and gives the originator a higher direct benefit from a contributor’s eforts. An example of this case is Red Hat’s obligatory acceptance of the GPL (Hillesley 2008).

On the other hand, BSD-style licenses are very permissive, placing minimal restrictions on software use and redistribution (Rusin 2008). Under such licenses, contributors are not required to make their code developed based on the originator’s code available to the public, instead permitting contributors to retain the rights to their modifications and improvements. Thus, BSD-style licenses are less restrictive, and the originator’s benefit from others’ contributions is limited relative to that under GPL. PostgreSQL and the Apache Software Foundation are two prominent adopters of this style of license (Montague 2008). A number of other licenses lie between these two extremes, including GNU LGPL (lesser GPL), which eases restrictions on software that only links to binaries of GPL-licensed code (Rusin 2008). JBoss, for instance, is licensed under the GNU LGPL (see JBoss 2008).

There are advantages and disadvantages for each license. For example, Stewart et al. (2006) explore the impact of OSS license choice on user interest by considering users’ perception of the costs and benefits of using the software as well as perceived risks related to legal uncertainties and enforceability. Lerner and Tirole (2005b) point to “hĳacking” by commercial software contributors/vendors, that is, outside contributors utilizing the open software code to develop (and potentially undermine) commercial software for profit under unrestrictive licenses. Among many other factors, our focus in this paper is on the economic incentives. More restrictive licenses provide an advantage to OSS originators who can benefit from subsequent contributors’ developments. On the other hand, less restrictive licenses can provide stronger incentives for these contributors to actually make these developments (Fishman 2004). However, because of the strategic nature of contributions, the way licensing afects investments in equilibrium can be dificult to ascertain. Given that commercial firms increasingly invest in and contribute to OSS products, our goal is exploring and focusing on those issues related to the economic incentives to contribute to an OSS project.

Since we study open-source software as motivated by the services market, the level of service costs is relevant to the analysis. By service costs, we refer to the variable costs incurred by firms when providing services to customers of the software. These costs can vary considerably depending on the class of software in question. For example, an enterprise resource planning (ERP) or customer relationship management (CRM) system integration would require high service costs because it is typically a time-consuming project involving extensive customization (Hitt et al. 2002). On the other hand, supporting a MySQL implementation as part of an application server stack would involve lower service costs, and providing training and support for productivity tools such as OpenOfice would be even less costly to the provider.

In this paper, we formulate a model to study how service costs and OSS licensing attributes afect a software originator’s decision to pursue an open-source development strategy. To develop the originator’s choice problem, our model captures the economic incentives of open-source contributors who also compete in the services market and whose strategic efort investment can be seen as both complementary and competitive. Using this model, we study the efects of licensing on the incentives of both the originator and subsequent contributor to invest in the development of OSS. Since whether open-source or proprietary outcomes are realized can greatly impact the total value generated by software to society, we examine welfare considerations in this complex production and service environment and study policy implications for regulators.

The rest of this paper is organized as follows. Section 2 discusses the relevant literature. In Section 3, we formally present the model. Section 4 presents the equilibrium consumer market structure and prices, and studies the originator’s selection of open-source license restrictiveness and its implications on welfare and policy. Section 5 discusses our model’s assumptions and limitations. Section 6 ofers our concluding remarks. All proofs and technical equilibrium derivations are given in the online appendix.

## 2. Literature Review

The primary contribution of this paper is its examination of how (i) open-source software licensing impacts the incentives of (ii) profit-motivated OSS contributors operating in the services market, thereby afecting an OSS originator’s (iii) decision to pursue a proprietary or OSS strategy. To our knowledge, our paper is the first to integrate these three facets into a single model that facilitates an understanding of the role of OSS licensing in enterprise software markets, which tend to be driven by services. Again, to our knowledge, August et al. (2013) is the first paper to study the source code decision while including contributors with extrinsic motivations in the services market who make endogenous investments toward the development of the OSS product and attainment of service-related expertise (i.e., facets (ii) and (iii)). Therefore, we build on August et al. (2013) to formally examine how OSS licensing (facet (i)) interacts with participants’ investments in OSS and subsequently characterizes varying parameter regions under which permissive and restrictive licensing schemes can ultimately be beneficial to social welfare.

August et al. (2013) provides a discussion of literature related to facets (ii) and (iii). For a deeper exploration of these two facets, we direct the reader to that discussion as well as the following papers: those that model extrinsically motivated OSS firms (see, e.g., Sen 2007, Kumar et al. 2011, August et al. 2013) stem from a broader literature on the economic incentives of open-source developers (see, e.g., Lerner and Tirole 2002, Hars and Ou 2002, Lerner and Tirole 2005a, von Krogh and von Hippel 2006, Roberts et al. 2006, Iansiti and Richards 2006, Mehra et al. 2011, Mehra and Mookerjee 2012, Von Krogh et al. 2012). There is also a growing body of work that studies competition between open-source and proprietary firms (see, e.g., Gaudeul 2004a, Bessen 2006, Casadesus-Masanell and Ghemawat 2006, Sen 2007, Lee and Mendelson 2008, Casadesus-Masanell and Llanes 2011, Cheng et al. 2011, Zhu and Zhou 2012, August et al. 2014). The strategic choice between developing open-source and proprietary software has gathered significant attention in the literature as well (see, e.g., Lerner and Tirole 2005b, Lerner et al. 2006, Haruvy et al. 2008, August et al. 2013, Wen et al. 2016). In particular, August et al. (2013) find that if an originator is suficiently eficient in development, the licensing decision mainly depends on the originator’s ability to harness the contributor’s development to improve quality: if the originator is adept at improving the quality of the originator’s software/service package by utilizing the contributor’s development, then an OSS strategy is optimal; otherwise, the originator is better of keeping the software proprietary. They also show that increased contributor eficiency can unexpectedly decrease welfare. This result can manifest when the contributor is highly eficient because if the originator opens up the source code, the originator can be squeezed out of the services market as the contributor uses his development eficiency and strategic pricing to open up a large gap between the overall attractiveness of his ofering and that of the originator. In such circumstances, the originator may instead choose a proprietary strategy, which results in lower software and service quality and decreased welfare.

Turning attention to the integration of facet (i), when an open-source approach is preferred to a proprietary one, an important question is how restrictive should the open-source license be. West (2003) argues that competing forces of adoption and appropriability make firms choose among proprietary, open-source, and hybrid licensing strategies. Hawkins (2004) identifies the primary costs associated with proprietary and open-source development and, through a series of examples, demonstrates when it is optimal to open the code and the conditions under which viral licensing is preferred to public-style licensing. Gaudeul (2004b) concludes that when developer wages are high and costs are low, GPL is preferred although the existence of GPL can hurt social welfare. Asundi et al. (2012) show that firms may choose to release open-source versions of their software products under competition because, by doing so, they can increase the value of their closed-source product because of enhancements. Sen et al. (2011) model open-source license choice for a project leader when the license afects the incentives of subsequent developers. They find that leaders should adopt less restrictive licenses when significant efort of subsequent developers is required to create derivative works. On the other hand, a more restrictive license is preferred when the efort required is smaller.

There is a rich stream of literature that empirically examines licensing of OSS. Lerner and Tirole (2005b) build a simple model to examine the licensing decision and empirically find that restrictive licenses, such as GPL, would be unlikely candidates for OSS that runs in proprietary environments. Stewart et al. (2006) study how both licensing and organizational sponsorship influence the success of open-source projects. They find that projects with a nonmarket sponsor and a nonrestrictive license tend to garner the most user interest, which positively afects development activity. More recent studies examine the relationships between OSS licensing and developer motivations and attitudes (Sen et al. 2009), developer membership and activity characterization (Colazo and Fang 2009), and social influence (Singh and Phelps 2013).

Our paper complements this literature on OSS licensing by theoretically exploring how diferent licenses afect an originator firm’s decision on whether to choose an open-source strategy or a proprietary strategy and how the social value associated with software can be increased by advocating particular licenses. Selecting an open-source strategy has two efects: a complementarity efect and a strategic efect. The complementarity efect stems from the benefits associated with contributions from the community. These benefits can help increase the quality of both the base product as well as the services ofered in the market by the originator. The strategic efect stems from strategic contributors who invest efort into the OSS with the intention of competing against the originator for service contracts. The core contribution of our paper is that we are able to characterize the influence of license restrictiveness on development incentives and ultimately on the originator’s preferred source code strategy across diferent economic regimes. In our model, the answer to the licensing question ultimately relates to how licensing impacts the originator’s ability to generate revenue in the services market. License restrictiveness sways the investment incentives of contributors, which in turn modifies the pricing landscape for services. Since our model captures sequential endogenous investment choices and Nash equilibrium pricing strategies for services, it enables us to formally study the influence of cost structure, OSS licenses, and preferences on source code strategy.

## 3. Model

Our model builds on the one presented in August et al. (2013): A software originator (o) chooses a source code strategy and price and how much to invest in a software product the originator has created. The originator’s first decision in the sequence, $\rho ,$ is to choose whether to license the product as a proprietary product (P) or an open-source one (O), that is, $\rho \in \{ P , O \}$ . Once this decision has been made, the originator’s next decision is how much to invest in efort and development of the software, $e _ { o } \geq 0 ,$ , where these improvements to the software product and services incur a convex cost of efort $C _ { o } ( \dot { e } _ { o } ) \triangleq \beta _ { o } e _ { o } ^ { 2 } / 2$ . After the initial investment and development by the originator firm, a follower firm, the contributor (c), can also choose to invest $e _ { c } \ge 0$ in the software with the hope of profiting from providing services associated with the software product, incurring a cost of efort that is $C _ { c } ( e _ { c } ) \triangleq \beta _ { c } e _ { c } ^ { 2 } / 2 . ^ { . }$ 1

After obtaining the software, to efectively operate it and derive value, a customer needs integration and support services. To the customer, the total quality of the software, including services, depends on the efort invested by the originator and the contributor. There is a continuum of consumers defined by the consumer type parameter $\theta ,$ which is uniformly distributed on $\Theta = [ 0 , 1 ]$ . Consumer type θ indicates the customer’s sensitivity to the quality of the software package, including services. A consumer can choose either the originator or contributor to provide the necessary services. In addition, we extend August et al. (2013) to give consumers the option to obtain a base level of service from either a competitive services market or self service, which we denote by b. The base level of service is important to consider because its presence not only captures a significant way that many low-end users obtain open-source integration services, but it also substantially shapes the strategic interaction between the originator and the contributor. A type θ consumer derives value $\theta Q _ { k }$ if the consumer chooses to obtain services from provider $k \in \{ o , c , b \}$ , where $Q _ { k }$ is the total quality of the software solution.

The development eforts of the originator and the contributor have two efects. First, they improve the total base quality of the software solution itself, $Q _ { g } .$ We model the efect of the originator and contributor investments on the base software quality as $Q _ { g } \triangleq g _ { o } e _ { o }$ + $g _ { c } e _ { c } ,$ where $g _ { o } , g _ { c } > 0$ are multipliers capturing the relative impact of each player’s efort. The parameters $g _ { o }$ and $g _ { c }$ in our model are associated with the private provision of public good in that they reflect the extent to which private eforts expended build quality into the freely available base product.<sup>5</sup> Public goods tend to be undersupplied by voluntary contributions because of the free-rider problem (Groves and Ledyard 1977). Nonaltruistic motivations are central to the discussion of the private provision of public goods (Andreoni 1988). In this vein, our work captures how the base OSS product hinges on incentives of the contributing participants to distinguish themselves as experts in the value-added software services market, which we next discuss.

The second efect lies in the quality of firm-specific integration and support services, $Q _ { s }$ . This efect has two components: First, as a firm invests resources and efort in a software product, it builds expertise and competency in providing integration and services. This boosts the quality of the total software solution the firm provides to customers. Second, a firm’s service quality can also be positively impacted by other firms’ investments, which can yield publicly available OSS service support components, utility contributions, and information. Therefore, in general, a firm that spends efort in building expertise may benefit from eforts and investments of all developers. Hence, we model the efect of originator’s and contributor’s investments on their respective service qualities as $Q _ { s o } \triangleq s _ { o o } e _ { o } + s _ { o c } e _ { c }$ and $Q _ { s c } \triangleq s _ { c o } e _ { o } + s _ { c c } e _ { c }$ . We employ an additive model. By doing so, we do not assume any complementary eforts but will instead formally demonstrate that the originator and contributor eforts can be strategic complements or strategic substitutes (Bulow et al. 1985) in equilibrium. In the broader literature, quality is frequently modeled as a linear function of efort or investment of producers (see, e.g., Radner et al. 1986, Moldovanu and Sela 2001, Kuan 2001, Varian 2004). In many cases, this is a simplifying assumption that is made for tractability and model transparency without sacrificing the core variable relationships and insights from the model.

The parameters $s _ { o o } ^ { O }$ and $s _ { c c } ^ { O }$ represent the accumulation of knowledge, experience, and expertise. Dutton and Thomas (1984), building on Levy (1965), aptly categorize learning into two types: autonomous and induced. Autonomous learning refers to the improvements that automatically result from sustained production over a long period of time (Dutton and Thomas 1984). Induced learning refers to specific investments or eforts made by the firm toward improvement. Models of autonomous learning often use cumulative production as a proxy of experience or knowledge (see, $\mathrm { e . g . }$ , Spence 1981, Fine 1986). Models of induced learning use cumulative investments instead as a proxy (see, $\mathrm { e . g . , }$ Arrow 1962, Dorroh et al. 1994). Li and Rajagopalan (1998) model both types of learning on productivity and quality in a production environment. The OSS literature reflects the expertise of service providers gained by eforts invested into OSS (i.e., induced learning) in a similar manner. For example, Sen (2007) models the expertise of a support services vendor as reducing the variable cost associated with usability with quality levels being held fixed. August et al. (2013) model services expertise as an increase in quality for a fixed variable cost, further capturing the service provider’s incentives to invest eforts. We similarly capture the impact of induced learning on quality for the strategic players in our model with $s _ { o o } ^ { O }$ and $s _ { c c } ^ { O }$

The parameters $\dot { s } _ { c o } ^ { O }$ and $s _ { o c } ^ { O }$ capture the cross-complementarities of strategic project participants as determined by licensing and the governance structures of the OSS project. Such complementarities can exist among firms contributing to OSS production. Specifically, OSS licensing can significantly influence the extent to which an originator can leverage a contributor’s eforts toward the originator’s total quality. For example, restrictive licenses that require a contributor to fully document and contribute any new functionality back to the OSS project and governance structures that require a contributor to provide unit tests, use cases, and other information can altogether enhance the originator’s quality level in the marketplace. This is particularly true for service-related utilities, including system administration tools. In a similar fashion, the contributor can also benefit from the originator’s eforts to the extent that the governance structures are shaped to empower contributors in the services market. In Section 4.3, we explore the impact of license restrictiveness on software outcomes.

The magnitudes of coeficients $s _ { i j }$ and $g _ { k }$ quantify the relative importance of common quality factors versus firm-specific ones to consumers, which is largely determined by the particular software product market and can change under proprietary and open-source regimes, and critically depends on the restrictiveness of the open-source license. When the software is proprietary, it is not open to outside contributions; hence, the contributor cannot add to the base software quality nor can the originator benefit from the contributor’s eforts and investment, that is, $g _ { c } ^ { P } = 0$ and $s _ { o c } ^ { P } = 0$ Furthermore, since there is no major factor that would necessarily change how the originator benefits from its own efort between proprietary and open-source cases, we also assume $s _ { o o } ^ { \bar { P } } = \stackrel { \bullet } { s } _ { o o } ^ { O }$ . Finally, when the consumer obtains a base level of service, that is, when $k = b .$ , the consumer does not receive the quality premium associated with obtaining service from an agent who has committed significant resources toward the development of the software and gained expertise. We normalize this quality component to 0, that is, $Q _ { s b } = 0$ . The total quality of the software solution when a customer obtains service from provider $k \in \{ o , c , b \}$ is $Q _ { k } = Q _ { g } + Q _ { s k }$

Consumers’ usage decisions are made in the last stage, at which point the policy, efort levels, and prices are fixed. If the product is licensed as proprietary, the originator sets a price for the product $\dot { \boldsymbol { p } } ^ { P }$ and a price for the originator’s services $p _ { o } ^ { P }$ while a contributor only sets a price for the contributor’s services ofering $p _ { c } ^ { \bar { P } }$ Under an open-source strategy, the pricing of integration and services still occurs with the originator and contributor setting their service prices at $\overset { \sim } { p } _ { o } ^ { O }$ and $p _ { c } ^ { O } .$ respectively, but the product price is zero $( \mathbf { i . e . , } p ^ { O } = 0 )$ We denote the marginal cost of providing services with $c > 0 .$ . Under a software license strategy $\bar { j } \in \{ P , O \}$ (proprietary or open source), denote the price charged by a competitive integrator as $p _ { c i } ^ { j }$ . Then, the unit profit for that integrator is $\pi _ { c i } ^ { j } = p _ { c i } ^ { j } - c$ . That is, each competitive integrator makes a revenue of $p _ { c i } ^ { j }$ at a cost of c for an integration service. Under either licensing scenario, the competitive integrators are not diferentiated from each other in service quality.<sup>6</sup> Since their services are undiferentiated from one another and there are many of them, the competitive integrators engage in perfect price competition, and hence, their services are competitively priced at the marginal cost, that is, ${ \boldsymbol { p } } _ { b } = { \boldsymbol { c } }$

In the proprietary case, a consumer with type θ can choose not to use the software product, purchase the product and obtain competitive services, purchase both the product and services from the originator, or purchase the product from the originator and contract with the contributor for services. The consumer’s net payof from each action is given by

$$
V ^ {P} (\theta) \triangleq \left\{ \begin{array}{l l} Q _ {o} ^ {P} \theta - p ^ {P} - p _ {o} ^ {P} & \text { if   purchased   the   software   and   contracted } \\ & \text { service   with   the   originator; } \\ Q _ {c} ^ {P} \theta - p ^ {P} - p _ {c} ^ {P} & \text { if   purchased   the   software   and   contracted } \\ & \text { service   with   the   contributor; } \\ Q _ {b} ^ {P} \theta - p ^ {P} - c & \text { if   purchased   the   software   and   contracted } \\ & \text { service   with   a   competitive   integrator; } \\ 0 & \text { if   not   purchased. } \end{array} \right.\tag{1}
$$

In the open-source case, the price of the software itself is zero, and the net payof for a consumer with type θ is

$$
V ^ {O} (\theta) \triangleq \left\{ \begin{array}{l l} Q _ {o} ^ {O} \theta - p _ {o} ^ {O} & \text { if   contracted   service   with } \\ & \text { the   originator; } \\ Q _ {c} ^ {O} \theta - p _ {c} ^ {O} & \text { if   contracted   service } \\ & \text { with   the   contributor; } \\ Q _ {b} ^ {O} \theta - c & \text { if   contracted   service   with   a } \\ & \text { competitive   integrator; } \\ 0 & \text { if   not   used. } \end{array} \right.\tag{2}
$$

In summary, the model timeline is as given in Figure 1.

Two industry structures commonly observed in practice can be characterized by specific relationships between fundamental parameters of the model. A strong originator would be characterized by high $\beta _ { c }$ and $s _ { o c } ^ { O ^ { - } } \left( \beta _ { o } \ll \beta _ { c } \right.$ and $s _ { c o } ^ { O } \ll s _ { o c } ^ { O } )$ ; that is, the originator is relatively more cost-eficient and can strongly leverage the efort exerted by any subsequent contributor. These conditions reflect that the originator has better resources for both developing the software at a lower cost and harnessing the contributions of others in comparison to the outside contributor.<sup>7</sup> On the other hand, a strong contributor would be characterized by low $\beta _ { c }$ and $s _ { o c } ^ { \ j } \left( \beta _ { c } \ll \beta _ { o } \right.$ and $s _ { o c } ^ { O } \ll s _ { c o } ^ { O } )$ ; that is, the contributor has the resources to be adept at developing the software at a lower cost as well as leveraging the efort invested in the project by others toward its own benefit. This often happens when the main outside contributor is a bigger and more powerful firm than the originator.<sup>8</sup> Strong Contributor and Strong Originator refer to these mathematical conditions and are used in Section 4.3.

Figure 1. The Model Timeline  
![](/api/attachments/7BZEDDV6/fulltext/images/12ddc7509799e0bd49a08b55f1ce0a527fdbf0277d13d5f474e27a89bfd6bdf2.jpg)

## 4. Licensing Policy Analysis

In this section, we give an overview of the equilibrium derivation for the two licensing strategies, proprietary (Section 4.1) and open source (Section 4.2). The technical derivations are given in the online appendix.

## 4.1. Proprietary Licensing Equilibrium Characterization

The analysis of the equilibrium is by backward induction. Given the efort levels, $e _ { o } ^ { P }$ and $e _ { c } ^ { P } ,$ , and prices, $p ^ { P } , p _ { o } ^ { P } .$ , and $p _ { c } ^ { P } .$ , as fixed, each consumer of type $\theta \in \Theta$ chooses an action that maximizes the consumer’s net payof given in (1) which reflects the choices the consumer has for obtaining services. Lemma EC.2 in the online appendix presents the structure of the consumer market equilibrium in the final stage.

After the efort levels and the service quality levels are set, projecting the customers’ responses to the prices as described above, the originator and the contributor set their prices. The originator sets $p ^ { P }$ and $p _ { o } ^ { P }$ to maximize her final stage profit function. Her corresponding optimization problem can be formulated as

$$
\begin{array}{l} \text {maximize} _ {p ^ {P}, p _ {o} ^ {P}} \breve {\Pi} _ {o} ^ {P} (p ^ {P}, p _ {o} ^ {P} \mid p _ {c} ^ {P}, e _ {o} ^ {P}, e _ {c} ^ {P}) \\ \triangleq p ^ {P} \int_ {\Theta} \mathbf {1} _ {u} (\theta) d \theta + (p _ {o} ^ {P} - c) \int_ {\Theta} \mathbf {1} _ {o} (\theta) d \theta . \end{array}\tag{3}
$$

The contributor’s profit maximization problem at this stage is

$$
\underset {p _ {c} ^ {P}} {\text { maximize }} \breve {\Pi} _ {c} ^ {P} (p _ {c} ^ {P} | p ^ {P}, p _ {o} ^ {P}, e _ {o} ^ {P}, e _ {c} ^ {P}) \triangleq (p _ {c} ^ {P} - c) \int_ {\Theta} \mathbf {1} _ {c} (\theta) d \theta .\tag{4}
$$

Solving (3) and (4) simultaneously gives rise to the Nash equilibrium product and service prices. The following lemma summarizes the equilibrium outcome in the pricing stage.<sup>9</sup>

Lemma 1. Let $e _ { o } ^ { P }$ and $e _ { c } ^ { P }$ be fixed, and $\operatorname* { m a x } ( Q _ { o } , Q _ { c } ) \geq c$ The equilibrium prices, $p ^ { \check { P } } , p _ { o } ^ { \check { P } } .$ , and $p _ { c } ^ { P } .$ , satisfy

Region I: $I f Q _ { c } > Q _ { o } > Q _ { b }$ and $Q _ { o } \leq 3 c$ , then

$$
\begin{array}{c} p ^ {P} = \frac {Q _ {c} (Q _ {c} - c)}{3 Q _ {c} - Q _ {o}}, \quad p _ {o} ^ {P} = \frac {(Q _ {o} + Q _ {c}) c - (Q _ {c} - Q _ {o}) ^ {2}}{3 Q _ {c} - Q _ {o}}, \\ p _ {c} ^ {P} = \frac {Q _ {c} (Q _ {c} - Q _ {o} + 2 c)}{3 Q _ {c} - Q _ {o}}, \end{array}\tag{5}
$$

and only the originator and the contributor are active in the services market.

Region II: I $f Q _ { c } > Q _ { o } > Q _ { b }$ and $Q _ { o } > 3 c ,$ , then

$$
\begin{array}{c} p ^ {P} = \frac {2 Q _ {c} + Q _ {o} - 3 c}{6}, \quad p _ {o} ^ {P} = c - \frac {Q _ {c} - Q _ {o}}{3}, \\ p _ {c} ^ {P} = c + \frac {Q _ {c} - Q _ {o}}{3}, \end{array}\tag{6}
$$

and only the originator and the contributor are active in the services market.

Region III: $H Q _ { o } \geq Q _ { c } \geq Q _ { b }$ , then

$$
p ^ {P} = \frac {Q _ {o} - c}{2}, \quad p _ {o} ^ {P} = c, p _ {c} ^ {P} = c,\tag{7}
$$

and only the originator is active in the services market.

Lemma 1 states that for any given efort levels, under a proprietary license, in equilibrium, competitive integrators are pushed out of the services market, and only the firms who invest in building expertise in the software are active in selling services. The competitive integrators, who have not invested and hence are not diferentiated in quality, provide service at the base quality level at the unit price equaling the marginal cost c. By comparison, larger firms that invested and improved their service quality can charge prices that are higher than the marginal service cost since their quality levels generate additional value for the customers. If the high-quality options are priced suficiently low, it can be the case that no customer finds it preferable to procure service from the competitive integrators as better quality service at a good price is available. Given this, in certain cases, the originator and the contributor firms may choose in equilibrium to lower their prices so much that there is zero demand for purchasing services from the competitive integrators. Such equilibrium outcomes, called limit pricing, are common in models of price competition (see, e.g., Bain 1949, Modigliani 1958, Gabszewicz and Thisse 1979, Tunca and Wu 2013). In particular, and diferent from prior studies on software competition, Lemma 1 demonstrates that, for the proprietary license case, limit pricing is likely to occur because the originator has additional pricing power when the base software and value-added services are priced separately. The originator charges both a price $\dot { \boldsymbol { p } } ^ { P }$ for the product and a price for services $p _ { o } ^ { \tt S p }$ while a contributor only sets a price for services, ofering $p _ { c } ^ { P }$ . Because the contributor is a strategic player, the contributor can invest efort to diferentiate the quality of the contributor’s ofering and be active in the market. However, the competitive integrators do not invest efort toward diferentiation. Therefore, an originator can utilize the additional price lever, $p ^ { P }$ , efectively as a limit price to push them out of the market while still using its service price, $p _ { o } ^ { P } .$ , to extract surplus. As stated in Regions I and II, if the contributor has a higher service quality, then the originator and the contributor share the services market. However, if the originator has a higher quality (Region III), the originator can use the originator’s flexibility to price the product itself as well as the software services provided to push the contributor out of the market and become a monopolist.

At the investment stage, taking the equilibrium price formation given in Lemma 1 into account, the contributor chooses an efort level, $e _ { c } ^ { P } ( e _ { o } ^ { P } )$ , that maximizes the contributor’s total profit function, $\Pi _ { c } ^ { P } ( e _ { c } ^ { P } \mid e _ { o } ^ { P } ) =$ $\breve { \Pi } _ { c } ^ { P } ( e _ { c } ^ { P } \mid e _ { o } ^ { P } ) \ : - \ : C _ { c } ( e _ { c } ^ { P } )$ , where $\breve { \Pi } _ { c } ^ { \cal P }$ is as given in (4) after observing the originator’s efort investment level. Considering this optimal contributor efort characterization, $e _ { c } ^ { P } ( e _ { o } ^ { P } )$ , the originator sets an efort level to maximize the originator’s own total profits, $\Pi _ { o } ^ { P } ( e _ { o } ^ { P } ) =$ $\check { \Pi } _ { o } ^ { P } ( e _ { o } ^ { P } ) - C _ { o } ( e _ { o } ^ { P } )$ , where $\breve { \Pi } _ { o } ^ { \cal P }$ is as given in (3). Formally, let $\vec { p } = ( p ^ { P } , p _ { o } ^ { P } , p _ { c } ^ { P } )$ , which reflects the equilibrium prices as functions of efort levels. The originator solves

$$
\begin{array}{l} \underset {e _ {0} ^ {P} \geq 0} {\text {maximize}} \Pi_ {o} ^ {P} (e _ {o} ^ {P}) = p ^ {P} \int_ {\Theta} \mathbf {1} _ {u} (\theta , \vec {p}, e _ {o} ^ {P}, e _ {c} ^ {P} (e _ {o} ^ {P}))   d \theta \\ \qquad + (p _ {o} ^ {P} - c) \int_ {\Theta} \mathbf {1} _ {o} (\theta , \vec {p}, e _ {o} ^ {P}, e _ {c} ^ {P} (e _ {o} ^ {P}))   d \theta - \frac {1}{2} \beta_ {o} (e _ {o} ^ {P}) ^ {2} \end{array}\tag{8}
$$

$$
\begin{array}{l} \text {s.t.} \vec {p} \text {solves (3) and (4) given e_{o} ^{P} ,e_{c} ^{P} (e_{o} ^{P})} \\ \text {as characterized in Lemma 1;} \end{array}
$$

and

$$
\begin{array}{l} e _ {c} ^ {P} (e _ {o} ^ {P}) = \underset {e _ {c} ^ {P} \geq 0} {\arg \max} \Pi_ {c} ^ {P} (e _ {c} ^ {P} \mid e _ {o} ^ {P}) \\ = \underset {e _ {c} ^ {P} \geq 0} {\arg \max} \left\{(p _ {c} ^ {P} - c) \int_ {\Theta} \mathbf {1} _ {c} (\theta , \vec {p}, e _ {o} ^ {P}, e _ {c} ^ {P})   d \theta - \frac {1}{2} \beta_ {c} (e _ {c} ^ {P}) ^ {2} \right\} \end{array}
$$

## s.t. $\vec { p }$ solves (3) and (4) given $e _ { o } ^ { P } , e _ { c } ^ { P }$ as characterized in Lemma 1.

For convenience, we use $\Pi _ { o } ^ { P }$ and $\Pi _ { c } ^ { P }$ to refer to the equilibrium payofs of the originator and the contributor under the proprietary strategy. The related equilibrium derivations are given in the online appendix.<sup>10</sup> In the resulting equilibrium, the originator and the contributor may form a duopoly in the services market, or the originator may emerge as the exclusive service provider.

## 4.2. Open Source Licensing Equilibrium Characterization

The analysis of the equilibrium is similar to the proprietary case and again proceeds by backward induction. The main diference is that when the software is licensed as open source, the originator cannot charge a price for the software itself, and both firms aim to make profits purely from service provision. Given efort levels, $e _ { o } ^ { O }$ and $e _ { c } ^ { \breve { O } }$ , and service prices, $p _ { o } ^ { O }$ and $p _ { c } ^ { O } .$ , each consumer of type $\theta \in \Theta$ chooses an action that maximizes the consumer’s net payof given in (2), which reflects the choices she has for obtaining services. Lemma EC.3 in the online appendix presents the structure of the consumer market equilibrium in the final stage.

At the pricing stage, projecting the consumer market equilibrium as described previously and given the development efort levels $e _ { o } ^ { O }$ and $e _ { c } ^ { O }$ , the originator and the contributor’s respective optimization problems are

$$
\max _ {p _ {o} ^ {O}} \check {\Pi} _ {o} ^ {O} (p _ {o} ^ {O} \mid p _ {c} ^ {O}, e _ {o} ^ {O}, e _ {c} ^ {O}) \triangleq (p _ {o} ^ {O} - c) \int_ {\Theta} \mathbf {1} _ {o} (\theta) d \theta ,\tag{9}
$$

and

$$
\max _ {p _ {c} ^ {O}} \check {\Pi} _ {c} ^ {O} (p _ {c} ^ {O} \mid p _ {o} ^ {O}, e _ {o} ^ {O}, e _ {c} ^ {O}) \triangleq (p _ {c} ^ {O} - c) \int_ {\Theta} \mathbf {1} _ {c} (\theta) d \theta .\tag{10}
$$

The firms compete in the services market by solving (9) and (10), which gives rise to Nash equilibrium prices. The pricing equilibrium outcome is summarized in the next lemma.

Lemma 2. Given $Q _ { i } { > } Q _ { j } { > } Q _ { b }$ and $Q _ { i } > c ,$ , where i denotes the higher quality provider between the originator (o) and contributor (c) and j denotes the remaining one, let ${ \vec { Q } } =$ $\left( Q _ { i } , Q _ { j } , Q _ { b } \right)$ . There exist threshold values $0 \leq \tau _ { A } ( \vec { Q } ) \leq \tau _ { B } ( \vec { Q } )$ ${ \leq } Q _ { j } / 2 { \leq } \tau _ { C } ( \vec { Q } ) ^ { 1 1 }$ such that

Region I: $I f c \leq \tau _ { A } ( \vec { Q } )$ , then

$$
\begin{array}{r} p _ {i} ^ {O} = c + \frac {2 (Q _ {i} - Q _ {b}) (Q _ {i} - Q _ {j})}{4 (Q _ {i} - Q _ {b}) - (Q _ {j} - Q _ {b})}, \\ p _ {j} ^ {O} = c + \frac {(Q _ {j} - Q _ {b}) (Q _ {i} - Q _ {j})}{4 (Q _ {i} - Q _ {b}) - (Q _ {j} - Q _ {b})}, \end{array}\tag{11}
$$

and the originator, contributor, and competitive integrators are active in the services market.

Region II: $I f \tau _ { A } ( \vec { Q } ) < c \leq \tau _ { B } ( \vec { Q } )$ , then

$$
p _ {i} ^ {O} = \frac {Q _ {i} - Q _ {j}}{2} + \frac {c (Q _ {j} + Q _ {b})}{2 Q _ {b}}, p _ {j} ^ {O} = \frac {c Q _ {j}}{Q _ {b}},\tag{12}
$$

and only the originator and contributor are active in the services market.

Region III: $I f \tau _ { B } ( \vec { Q } ) < c \leq Q _ { j } / 2 ,$ then

$$
\begin{array}{l} p _ {i} ^ {O} = \frac {Q _ {i} (2 (Q _ {i} - Q _ {j}) + 3 c)}{4 Q _ {i} - Q _ {j}}, \\ p _ {j} ^ {O} = \frac {Q _ {j} (Q _ {i} - Q _ {j}) + c (2 Q _ {i} + Q _ {j})}{4 Q _ {i} - Q _ {j}}, \end{array}\tag{13}
$$

and only the originator and contributor are active in the services market.

Region IV: If $Q _ { i } / 2 < c \leq \tau _ { c } ( \vec { Q } )$ , then $p _ { i } ^ { O } { = } c Q _ { i } / Q _ { j } ,$ $p _ { i } ^ { O } = c ,$ , and only the higher quality of the originator and contributor is active in the services market.

Region V: If $c > \tau _ { C } ( \vec { Q } )$ , then $p _ { i } ^ { O } = ( Q _ { i } + c ) / 2 , p _ { i } ^ { O } = c ,$ and only the higher quality of the originator and contributor is active in the services market.

As seen in Lemma 2, under an open-source license, depending on the level of service costs, $^ { c , }$ there can be five diferent market structures in the pricing equilibrium. First, if the service costs are low, that is, in Region I, the potential net value from services in the market is high, and in equilibrium, the providers can profitably target distinct consumer segments with their pricing. As a result, all three service providers (the originator, contributor, and competitive integrators) will be actively present as a three-way oligopoly in the market. In Regions II and $\operatorname { I I I } ,$ as the service cost increases, the consumer population for which the value from services is higher than the service costs to have net positive value for using the software shrinks. Consequently, the originator and the contributor have to price their services closer to marginal cost c. This tight pricing squeezes the competitive integrators who provide inferior quality service at marginal cost out of the market. The market structure becomes a duopoly between the originator and contributor. Finally, in Regions IV and V, the service costs are so high that the profitable consumer segment becomes small. Then, in equilibrium, there is room for only one firm to operate profitably, and the higher quality one between the originator and contributor prices out the other two options and becomes a monopoly in the services market.

Using the equilibrium service price characterization given in Lemma 2, we can analyze the sequential efort investment problems for both the originator and contributor. Similar to the proprietary software case, taking the efort level of the originator $e _ { o } ^ { O }$ as fixed, the contributor chooses $e _ { c } ^ { O } \geq 0$ to maximize $\Pi _ { c } ^ { O } ( e _ { c } ^ { O } \mid e _ { o } ^ { O } ) =$ $\breve { \Pi } _ { c } ^ { { \cal O } } ( e _ { c } ^ { { \cal O } } \mid e _ { o } ^ { { \cal O } } ) - C _ { c } ( e _ { c } ^ { { \cal O } } )$ . Taking this contributor efort best response, $e _ { c } ^ { O } ( e _ { o } ^ { O } ) .$ , the originator chooses $e _ { o } ^ { O } \geq 0$ to maximize $\Pi _ { o } ^ { \cal O } ( e _ { o } ^ { \cal O } ) { = } \breve { \Pi } _ { o } ^ { \cal O } ( e _ { o } ^ { \cal O } ) { - } C _ { o } ( e _ { o } ^ { \cal O } )$ , where $\breve { \Pi } _ { o } ^ { O }$ and $\breve { \Pi } _ { c } ^ { O }$ are as given in (9) and (10), respectively. Formally, let ${ \vec { p } } =$ $( p _ { o } ^ { O } , p _ { c } ^ { O } )$ . The originator solves

Figure 2. The Nature of the Contributor’s Profit Curve  
![](/api/attachments/7BZEDDV6/fulltext/images/d7681202fe2c18000aee8ac5cf27c7a0e514aed7627ff019f88dd855350c62f7.jpg)  
Note. Region labels match the distinct consumer market structures identified in Lemma 2. The parameter values are $e _ { o } ^ { O } = 2 . 5 , \ g _ { o } = 3 ,$ $g _ { c } = 3 , s _ { o o } ^ { O } = 4 , s _ { o c } ^ { O } = 1 , s _ { c c } ^ { O } = 3 , s _ { c o } ^ { O ^ { * } } = 0 . 1 , c = 2 , \beta _ { o } = 0 . 3 , \mathrm { a n d } \check { \beta } _ { c } = 0 . 0 6 5 , c = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check { \xi } _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 , \check \xi _ { c } = 0 . 3 \check \xi _ { c }$

$$
\begin{array}{l} \underset {e _ {o} ^ {O} \geq 0} {\text { maximize }} \Pi_ {o} ^ {O} (e _ {o} ^ {O}) = (p _ {o} ^ {O} - c) \int_ {\Theta} \mathbf {1} _ {o} (\theta , \vec {p}, e _ {o} ^ {O}, e _ {c} ^ {O} (e _ {o} ^ {O})) d \theta \\ \qquad \qquad \qquad - \frac {1}{2} \beta_ {o} (e _ {o} ^ {O}) ^ {2} \\ \text { s.t. } \vec {p} \text {   solves   (9)   and   (10)   given   } e _ {o} ^ {O}, e _ {c} ^ {O} (e _ {o} ^ {O}) \\ \text { as   characterized   in   Lemma   2; } \end{array}\tag{14}
$$

and

$$
\begin{array}{l} e _ {c} ^ {O} (e _ {o} ^ {O}) = \underset {e _ {c} ^ {O} \geq 0} {\operatorname{argmax}} \Pi_ {c} ^ {O} (e _ {c} ^ {O} | e _ {o} ^ {O}) \\ = \underset {e _ {c} ^ {O} \geq 0} {\operatorname{argmax}} \left\{(p _ {c} ^ {O} - c) \int_ {\Theta} \mathbf {1} _ {c} (\theta , \vec {p}, e _ {o} ^ {O}, e _ {c} ^ {O}) d \theta - \frac {1}{2} \beta_ {c} (e _ {c} ^ {O}) ^ {2} \right\} \\ \text {s.t.} \quad \vec {p} \text {solves (9) and (10) given} e _ {o} ^ {O}, e _ {c} ^ {O} \\ \text {as characterized in Lemma 2.} \end{array}
$$

For convenience, we use $\Pi _ { o } ^ { O }$ and $\Pi _ { c } ^ { O }$ to refer to the equilibrium payofs of the originator and contributor under the open-source strategy.

Figures 2 and 3 illustrate the equilibrium investment decisions, $e _ { o } ^ { O }$ and $e _ { c } ^ { O }$ , for the originator and the contributor and their efects on the resolution of the rest of the game. In particular, Figure 2 depicts the contributor’s decision problem by tracing how the contributor’s profit function changes as a function of his development efort level $e _ { c } ^ { O }$ given the originator’s investment level $e _ { o } ^ { O }$ . The market structure labels are as given in Lemma 2 for open-source licensing. In the figure, since the originator has suficient committed investment in the software, the overall starting software quality is high even with zero investment from the contributor. Therefore, at small $e _ { c } ^ { O }$ , there is enough value for the consumers in the market that the originator and contributor can coexist as a duopoly (Region II) with the originator having a higher service quality.

Figure 3. Market Structure and Firms’ Efort Investments  
![](/api/attachments/7BZEDDV6/fulltext/images/d3034de0ce997755b555bb39a04e0612e9dc8a84704d44acef7fd4f28af27148.jpg)  
Notes. Region labels indicate whether one, two, or three firms have positive market shares in the services market. The parameter values are $g _ { o } = 3 , g _ { c } \stackrel { \smile } { = } 3 , s _ { o o } ^ { O } = 4 , s _ { o c } ^ { O } = 1 , s _ { c c } ^ { O } = 3 , s _ { c o } ^ { O } = 0 . 1 , c = 2 , \beta _ { o } = 0 . 3 ,$ , and $\beta _ { c } = 0 . 0 \dot { 6 } 5$

As the contributor invests more in developing the software, after a certain point, the service qualities for the originator and the contributor become closer, and price competition between the two firms intensifies, resulting in lower profits for both firms. Beyond a certain investment level $e _ { c } ^ { O } .$ , the contributor becomes the quality leader. However, as the contributor investment level increases, the overall software quality becomes high enough that competitive integrators can have a segment of the service market; the market structure becomes a three-way oligopoly as can be seen in Figure 2 (Region I). In this region, the contributor is the highest quality service provider and the contributor’s overall profits are maximized by choosing a high investment level that induces a market structure in which all three service options are actively present in equilibrium.

Figure 3 demonstrates the regions for the equilibrium service market structure. As can be seen in the figure, when both the contributor’s and originator’s investment levels are very low (in the lower left corner of the figure with white background), the software does not have suficient quality to generate net value from service so there are no users of the software— the product does not make it to the market. As either the contributor’s or originator’s investment increases, the overall software solution starts to have net positive value. However, for small investment levels, the quality of the total software solution is low, and the providers cannot charge a high price for their services. As a result, there is room for only one provider in the market—the overall quality leader—and the leader prices both the lower quality developer and the competitive integrators out of the market, becoming a monopolist for services (Regions IV and V).

On the other end of the spectrum, if one of the developer firms has significantly higher quality than both the other developing firm and the competitive integrators $( \mathrm { i . e . , }$ either the originator or the contributor invest heavily and one significantly more so than the other), then both providers will have suficient value, and the quality leader will achieve sizable separation from the other firm. In this case, all three service options $o , c ,$ and b can have their own distinct customer segments, actively contracting in equilibrium, and the market structure will be a three-way oligopoly (Region I). In the middle, however, when the originator’s and contributor’s investments are close to one another, the service oferings of the two firms are close substitutes, and intense price competition emerges. In that case, the equilibrium prices of the two higher quality service providers (o and c) drop low enough that the competitive integrators are priced out of the market, resulting in a duopoly (Regions II and III).

The general structure of the equilibrium regions in Figure 3 is robust. In fact, as the parameters change, the layout of the regions stays the same, but the picture can sway in two ways, which are displayed in Figure 4. First, if the originator becomes stronger by, for instance, having an improved ability to benefit from the contributor’s development eforts (higher $s _ { o c } ^ { O } )$ , then when the contributor invests in development at a high level $( \mathrm { i . e . , }$ for high $e _ { c } ^ { O }$ levels) the two firms can push the competitive integrators out of the market more easily and achieve duopoly (Regions II and III) when the contributor is the product quality leader. As a result, for the same investment levels, Region I in the upper quadrant $( \mathrm { i . e . , }$ where $Q _ { o } ^ { O } < Q _ { c } ^ { O } )$ shrinks and is replaced mainly by Region III as can be seen in Figure $4 ( \mathsf { a } ) ;$ that is, the pattern sways counterclockwise. On the flip side, if the contributor becomes stronger by, for instance, improved ability to benefit from his own efort (higher $s _ { c c } ^ { O } \hat { ) }$ , then for the same investment levels the contributor quality moves up, and the competitive integrators are more easily pushed out of the market for the cases in which the originator is the quality leader. Therefore, the region where the market structure is oligopoly (Region I) shrinks for $Q _ { o } ^ { O } > Q _ { c } ^ { O }$ . However, if the contributor is the quality leader, higher $s _ { c c } ^ { O }$ results in an increased quality gap between the contributor and the originator, which allows the lower quality competitor, namely the originator, to increase the price. This increase relieves pressure on the low-cost competitive integrators and allows them to survive, resulting in a three-provider oligopoly (Region I) replacing duopoly (Regions II and III) for $\check { Q } _ { o } ^ { O } < \check { Q } _ { c } ^ { O }$ . Consequently, in this case, the pattern of the market structures sways clockwise as can be seen in Figure 4(b).

Figure 4. Sensitivity of Market Structure to Parameter Variations  
![](/api/attachments/7BZEDDV6/fulltext/images/041c930e033b2aec5a28e419a42fc777c710fcdcb19f59f023f7b26c8d01e508.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/8420b0d9124ea4cc8000159290730c5857c2f22070fc9b5f6e53d29c44df2775.jpg)  
Notes. The parameter values are $g _ { o } = 3 , \ g _ { c } = 3 , \ s _ { o o } ^ { O } = 4 , \ s _ { c o } ^ { O } = 0 . 1 , \ c = 2 , \ \beta _ { o } = 0 . 3 ,$ and $\beta _ { c } = 0 . 0 6 5 ; s _ { o c } ^ { O } = 2 . 5$ and $s _ { c c } ^ { O } = 3$ for Panel (a), and $s _ { o c } ^ { O } = 1$ and $s _ { c c } ^ { O } = 5 0$ for Panel (b). The market structure labels, I–V, are the same as those in Figure 3.

## 4.3. Impact of Open-Source Licensing Policy

In this section, we explore the impact of license restrictiveness and project organization on profitability and social welfare and discuss under which conditions each style of license is better suited. Social welfare is the sum of consumer surplus and the profits of the firms in the market. Consumer surplus for a given licensing policy $\rho \in \{ P , O \} , C S ^ { \rho } .$ , is

$$
\begin{array}{l} C S ^ {\rho} = \int_ {\Theta} \mathbf {1} _ {o} (Q _ {o} \theta - p ^ {\rho} - p _ {o} ^ {\rho}) d \theta + \int_ {\Theta} \mathbf {1} _ {c} (Q _ {c} \theta - p ^ {\rho} - p _ {c} ^ {\rho}) d \theta \\ \quad + \int_ {\Theta} \mathbf {1} _ {b} (Q _ {b} \theta - c) d \theta . \end{array} \tag {15}
$$

Substituting into the profit expressions (3), (4), (9), and (10), social welfare is then given by

$$
\begin{array}{l} W ^ {\rho} = C S ^ {\rho} + \Pi_ {o} ^ {\rho} + \Pi_ {c} ^ {\rho} \\ \qquad = C S ^ {\rho} + \check {\Pi} _ {o} ^ {\rho} - C _ {o} (e _ {o} ^ {\rho}) + \check {\Pi} _ {c} ^ {\rho} - C _ {c} (e _ {c} ^ {\rho}) \\ \qquad = \int_ {\Theta} \mathbf {1} _ {o} (Q _ {o} \theta - c) d \theta - C _ {o} (e _ {o} ^ {\rho}) + \int_ {\Theta} \mathbf {1} _ {c} (Q _ {c} \theta - c) d \theta \\ \qquad - C _ {c} (e _ {c} ^ {\rho}) + \int_ {\Theta} \mathbf {1} _ {b} (Q _ {b} \theta - c) d \theta . \end{array}\tag{\(d\theta\}
$$

(16)

In our model, the parameter $s _ { o c } ^ { O }$ captures the contributor-to-originator cross-complementarity of efort investment on the originator’s ofering and reflects the restrictiveness of the open-source license. Under more restrictive licenses, the originator can reap the benefits of the contributor’s efort, and hence, this type of license is characterized by a high value of $s _ { o c } ^ { O }$ . Under more permissive licenses, since the contributor can keep the contributor’s software developments from the public, the originator benefits less from the contributor’s efort. Hence, this style of license corresponds to a low value of $s _ { o c } ^ { O }$ . In practice, there are only a few categories of license available, which vary in their strength of restrictiveness. In many cases, a new OSS project may rely on the components of existing OSS projects, which significantly constrains OSS license selection for the new project. As an example, if an originator’s OSS project utilizes even one component governed by the GPL, then the originator’s OSS project necessarily must also be GPL. For these reasons, we parameterize license restrictiveness, and Table 1 gives an overview of the perspective that we employ in this section.

Table 1. The Relative Magnitude of $s _ { o c } ^ { O }$ Across Diferent Licensing Scenarios

<table><tr><td>Low  $s_{oc}^{O}$ </td><td>Medium  $s_{oc}^{O}$ </td><td>High  $s_{oc}^{O}$ </td></tr><tr><td>Permissive licensesNoncopyleftMinimal requirementsEx. BSD, MIT, Apache</td><td>Partially restrictive licensesWeak copyleftExceptions granted when only linkingEx. LGPL, MPL</td><td>Restrictive licensesCopyleft/ReciprocalAll derivative works inherit licenseEx. GNU GPL, GNU AGPL</td></tr></table>

We begin by exploring the potential desirability of a less restrictive license for an originator and its efect on developer efort levels, product quality, and welfare. From a software originator’s point of view, a restrictive license is preferable to a permissive one in many respects. For example, a restrictive license can maximize the returns an originator receives from the developments of subsequent contributors to the project. An open question then is whether it is possible for a permissive license to actually be preferred by a software originator. The following proposition explores this question.

Proposition 1. When a strong contributor’s eforts benefit its own firm-specific quality component to a greater extent than the originator’s, a less restrictive license can increase originator profits and social welfare. Technically, let $4 / 9 < s _ { o c } ^ { O } / s _ { c c } ^ { O } < 1$ . Then there exists $\bar { \beta } > \check { 0 }$ such that $i f \beta _ { c } < \bar { \beta } ,$ then the contributor is the quality leader, that is, $Q _ { c } > Q _ { o } ,$ and

(i) A less restrictive license increases the quality gap, the originator’s profits, and social welfare; that is, $i f s _ { o c } ^ { O }$ decreases then $Q _ { c } - \dot { Q _ { o } } , \dot { \Pi } ^ { O }$ , and $W ^ { O }$ increase;√

(ii) Define $\bar { r } = 4 0 / ( 3 7 + \sqrt { 2 , 1 6 9 } ) . I f s _ { o c } ^ { O } / s _ { c c } ^ { O } < \bar { r } ,$ , then there exists $\gamma > 0$ such that a less restrictive license decreases con-<sup>¯</sup>sumer surplus if and only $i f g _ { c } < \gamma . I f s _ { o c } ^ { O } / s _ { c c } ^ { O } > \bar { r } .$ , then a less <sup>¯</sup>restrictive license increases consumer surplus.<sup>12</sup>

Proposition 1 makes an interesting observation: Despite the fact that a permissive license can limit the benefits that a software originator who chooses to go open source can reap from the product, it can still be the case that the originator selects an open approach to the licensing style. This result emerges from strategic considerations. Specifically, when the contributor is cost-eficient in development, the contributor has the potential to improve the overall quality of the product both for the contributor and the originator. However, if the license is too restrictive and requires the contributor to make the developed code publicly available (i.e., if $s _ { o c } ^ { O }$ is high), the originator benefits in quality and then uses it to more efectively compete against the contributor in the services market. On the other hand, if the license is less restrictive, the total quality of the contributor’s ofering may exceed that of the originator. Furthermore, in such a case, as stated in part (i) of Proposition 1, a less restrictive license increases the quality diference between the contributor’s and the originator’s service quality levels since it results in the originator benefiting less from the contributor’s investments. Yet, even in such a case, the originator can increase profit by diferentiating from the contributor, serving a lower valuation consumer segment, and avoiding intense competition against the contributor. In this case, under a restrictive license, the complementarity efect is dominated by the strategic efect, and the price competition in the services market becomes too intensive. However, under a less restrictive license, the complementarity efect dominates the strategic efect because it enables the contributor to become the quality leader, which, in turn, enables the originator to benefit from contributions while providing services in a less competitive market. Hence, a less restrictive license, such as LGPL, can indeed benefit the originator’s profits as stated in part (i) of Proposition 1 even though the originator sacrifices being the quality leader in equilibrium. Moreover, provided that the efects of the contributor’s eforts on improving common quality factors are appreciable, a permissive license is not only more profitable to the originator, but can also improve welfare by boosting developer eforts and improving overall software quality ofered to consumers.

It is important to note that consumer surplus does not always go hand in hand with social welfare. Part (ii) of Proposition 1 states that when the contributor’s impact on the base software quality is less pronounced, choosing a less restrictive (i.e., low $s _ { o c } ^ { O } )$ license can hurt consumer surplus despite increasing social welfare. This is because when the license becomes less restrictive and the contributor is strong, as explained previously, the originator allows the contributor to become the quality leader in the services market, and to diferentiate the originator’s service quality from that of the contributor’s, the originator does not invest as much in quality improvement. As a consequence, the service quality increases, but price competition between the two firms in the services market is less intense, and the consumers face higher prices. In addition, if the firm that makes the main investment (i.e., the contributor) does not have a strong impact on improving the base software quality (i.e., if $g _ { c }$ is small), then the originator’s overall quality does not suficiently improve to compensate for the higher prices consumers face. Therefore, the net efect is that consumer surplus suffers. At the same time, the firm profits increase as a result of increased prices; the firm reaps the benefits of improved service quality, which can result in increased total welfare. This can also be seen in Figure 5(a). As the figure demonstrates, there is a wide range of $s _ { o c } ^ { O }$ values (marked as range A), for which decreased opensource license restrictiveness (lower $s _ { o c } ^ { O } )$ can decrease consumer surplus while increasing total welfare.

Figure 5. Social Welfare and Consumer Surplus with Respect to $s _ { o c } ^ { O }$  
![](/api/attachments/7BZEDDV6/fulltext/images/3eea2a91e396df12f2cac34ba43624ff1dfec063073a24ff6e2d3a95999895a2.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/b610f290492a9c726cb0699c1ca785ebedf4eafd8259aad1344a4a50c968e58b.jpg)  
Notes. The parameter values for panel (a) are $g _ { o } = 1 , \ g _ { c } = 0 . 1 , \ s _ { o o } ^ { O } = 2 , \ s _ { c c } ^ { O } = 2 , \ s _ { c o } ^ { O } = 0 . 1 , \ s _ { c o } ^ { P } = 0 . 0 5 , \ s _ { c c } ^ { P } = 0 , \ c = 0 . 1 , \ \beta _ { o } = 0 . 1 , \ \gamma _ { o } = 1 . 0 5 , \ M _ { e c } = 0 . 1 , \ M _ { o } = 1 . 0 5 , \ M _ { o } = 1 . 0 5 , \ M _ { o } = 1 . 0 5 , \ M _ { o } = 1 .$ , and $\beta _ { c } = 0 . 0 0 2$ . The parameter values for panel (b) are $\begin{array} { r }  \overline { { g _ { o } } } = 0 . 1 , g _ { c } = \overline { { 1 } } , s _ { o o } ^ { O } = 2 , s _ { c c } ^ { O } = 2 , s _ { c o } ^ { \overline { { O } } } = 0 . 5 , \overline { { s _ { c o } ^ { P } } } = 0 . \overline { { . 5 } } , s _ { c c } ^ { P } = 0 , c = 0 . 0 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1 , \beta _ { o } = 0 . 1  \end{array}$ and $\beta _ { c } = 0 . 0 0 6$

Under these conditions, when the contributor is stronger than the originator of the product, a social planner who weighs consumer surplus higher than firm profits may choose to impose regulations to strengthen open-source licensing restrictions despite the fact that such action would reduce the overall social value generated by the software. Consistent with the mission of the Federal Trade Commission (FTC), it is important to address market situations such as this one in which a firm becomes relatively too strong and leverages its market power to leave consumers in a manner that is worse of (FTC 2017). Our work advises regulating bodies, such as the FTC, to determine promising ways forward that help protect consumer surplus under such circumstances. One way is to advocate that OSS originators structure project governance to ensure that project contributors commit suficient code to common code bases so that the impact of license restrictiveness on consumer surplus and social welfare is well aligned. In particular, if the contributor’s impact on base software quality is high enough, this pushes the overall product quality up and compensates for the higher prices paid by the consumers, and both consumer surplus and social welfare can increase together with decreased open-source license restrictiveness as stated in Proposition 1 and can be seen in Figure 5(b).

Since permissive licenses increase the incentives for contributors to invest in software development and thus help improve software quality, one may suggest that this type of licensing is better from a policy perspective as it creates the right incentives for developers. In fact, one argument against GPL-style licenses is that such licenses restrict the freedom of contributors by forcing them to release their software developments to the public against their own interests, which can, in turn, hurt software development, quality, and ultimately welfare. However, the strategic involvement of firms in open-source licensing is inherently complex, and as demonstrated in the following proposition, the efect of GPL-style licensing can, in fact, be quite the opposite.

Proposition 2. If the contributor is eficient in development, a more restrictive license can increase the originator and contributor development investments, total software quality, originator profits, consumer surplus, and social welfare. Technically, there exist $\underline { { \nu } } , \bar { \nu } > 0 ,$ such that when $s _ { o c } ^ { O } > s _ { c c } ^ { O } , \ \underline { { \nu } } < c < \bar { \nu } , \ { g } _ { c } ( 4 s _ { o c } ^ { O } - 7 s _ { c c } ^ { O } ) < s _ { c c } ^ { O } ( 4 s _ { o c } ^ { O } - s _ { c c } ^ { O } )$ , and $\beta _ { c }$ is suficiently low, $Q _ { o } > Q _ { c }$ , and a more restrictive license increases $\mathrm { ( i ) } \ : \overline { { e _ { o } ^ { O } } }$ and $e _ { c } ^ { O } , Q _ { o }$ and $Q _ { c } ,$ and the quality gap, $Q _ { o } - Q _ { c } ; ( \mathrm { i i } ) \Pi _ { o } , \Pi _ { c } , C S ^ { O }$ , and $W ^ { O }$

Proposition 2 demonstrates that, despite the arguments suggesting that GPL-style licenses conflict with contributor incentives and, hence, may hurt the value generated by the open-source project as a whole, GPLstyle licensing may actually create the right incentives and improve not only originator profits, but welfare as well. Furthermore, although it forces a contributor to share the product of the contributor’s eforts with the public, including the originator who is the contributor’s main competitor, even the contributor can still be better of with such a restrictive license. The key here is the strategic interaction between the originator and the contributor.

Figure 6. The Impact of Licensing Choice on Firm Profits  
(a) Π<sup>O</sup><sub>o</sub>(e<sup>O</sup><sub>o</sub> ), permissive license (s<sup>O</sup><sub>oc</sub> = 4)  
![](/api/attachments/7BZEDDV6/fulltext/images/93381dc689c04731a97c4862bda0b50b70adf78415ceac236af7e156119158b8.jpg)

(b) Π<sup>O</sup>(e<sup>O</sup> ⎪ e<sup>O</sup>), permissive license $( s _ { o c } ^ { O } = 4 )$  
![](/api/attachments/7BZEDDV6/fulltext/images/82c20b3827b63bca9d731c380236e0b4d32501f067ed9654cfafa5ea4c22fcc5.jpg)

(c) $\Pi _ { o } ^ { O } ( e _ { o } ^ { O } ) .$ , restrictive license $( s _ { o c } ^ { O } = 7 )$  
![](/api/attachments/7BZEDDV6/fulltext/images/beadf28a86e9e597e90c4c8bb418c6155023e1162ac6e8f2c19405185da85c62.jpg)

(d) $\Pi _ { c } ^ { o } ( e _ { c } ^ { O } \mid e _ { c } ^ { O } ) ,$ restrictive license $( s _ { o c } ^ { O } = 7 )$  
![](/api/attachments/7BZEDDV6/fulltext/images/c1adc38931e39479ff4aeb1e8bcfdfe860f96d61bae6eda37cb4b9bae2e7d574.jpg)  
Notes. Panels (a) and (b) illustrate the originator and contributor profit curves, respectively, under a less restrictive license $( s _ { o c } ^ { O } = 4 ) _ { \cdot }$ , and panels (c) and (d) show the impact of a more restrictive license $( s _ { o c } ^ { O } = 7 )$ . The parameter values for all panels are $g _ { o } = 3 , g _ { c } = 3 , s _ { o o } ^ { O } = 7 , s _ { c c } ^ { O } = 3 , s _ { c o } ^ { O } = 0 . 1 0 ,$ $s _ { c o } ^ { P } = 0 . 0 5 , s _ { c c } ^ { P } = 0 , c = 2 1 , \mathbf { \hat { \beta } } _ { o } = 0 . 3 0 ,$ , and $\beta _ { c } = 0 . 0 4 .$

The intuition for this result is best illustrated in Figure 6, which contrasts the firms’ incentives under a permissive license, characterized by low $s _ { o c } ^ { O }$ (panels (a) and (b)), and a restrictive license, characterized by high $s _ { o c } ^ { O }$ (panels (c) and (d)). As demonstrated in Figure 6(a), the originator loses money for low levels of investment since the overall quality of the originator’s package is too low to charge high enough prices to recover the costs of providing service. As the originator’s investment increases, the originator begins to make positive profits. However, until the originator’s investment reaches a certain level, the contributor’s profit curve is strictly decreasing in $e _ { c } ^ { O }$ as depicted in Figure 6(b) at the optimal originator investment level of $\stackrel { \smile } { e _ { o } ^ { O } } = 7 . 7 2$ for this given level of $s _ { o c } ^ { O }$ . For higher levels of originator contribution, it becomes optimal for the contributor to make positive investments as seen in Figure 6(b) when the originator sets an investment level of $e _ { o } ^ { O } = 1 2 . 7 5 $ Examining the contributor’s profit curves, which are illustrated in panels (b) and (d), it is important to note that the contributor’s profit as a function of the contributor’s own efort can be bimodal. As a result, the originator’s profit function can have a discontinuity, which reflects the contributor’s jumping up of efort when $e _ { o } ^ { O }$ increases past a critical level.

However, since the originator does not benefit much from the contributor’s eforts in this case, the originator prefers to restrict the originator’s own efort level such that the contributor does not invest and stays out of the services market (i.e., the strategic efect outweighs the complementarity efect). On the other hand, under a restrictive license such as GPL, the originator can strongly benefit from the contributor’s software developments $( \mathrm { i . e . } , s _ { o c } ^ { O }$ is high) while maintaining the originator’s position as the quality leader. In this case, the originator can be better of with a high level of investment, which also induces the contributor to invest in the project as seen in Figure 6(c) and 6(d). Therefore, both originator and contributor qualities increase with a more restrictive license compared with a permissive one, as stated in part (i) of Proposition 2. Furthermore, the quality diference is also amplified, which allows the contributor and the originator to better differentiate from one another, which in turn increases both their profits as stated in part (ii) of Proposition 2.

Figure 7. The Impact of Licensing Choice on Firm Profits and Social Welfare  
![](/api/attachments/7BZEDDV6/fulltext/images/48103bc441545a48dbe236a6969012a5d08ab49cb9449cb1f40de9ddcce88309.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/b430adf9d65943195f93b02264403093c033c783efa1aa16de0b4690822df256.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/d8a16d749406d117de76ec58580051855166073d7d409652879710b7d4668eba.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/63763dd1c4879428b230d05bf2c2e7d1099410dbcc967c9d7bcf0c8c152c75cd.jpg)  
Notes. Panels (a) and (c) illustrate the originator’s profit under open source and proprietary strategies, while panels (b) and (d) plot social welfare. The parameter values for panels (a) and (b) are $g _ { o } = 0 . 1 , \dot { g _ { c } } = 1 , s _ { o o } ^ { o } = 1 , s _ { c c } ^ { o } = \dot { 1 } , s _ { c o } ^ { \hat { o } } = 0 . 5 , \dot { s } _ { c o } ^ { P } = 0 . \dot { 2 } 5 , s _ { c c } ^ { P } = 0 , c \dot { = } 0 . 0 1 , \beta _ { o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 , \dot { s } _ { c o } = 0 . 1 \dot { s } _ { c o }$ and ${ \overline { { \beta } } } _ { c } = 0 . 0 0 6 .$ Parameter values for panels (c) and (d) are $g _ { o } = 0 . 1 , \ g _ { c } ^ { - } = 1 , \ s _ { o o } ^ { o } = 1 , \ s _ { c c } ^ { o } = 1 , \ s _ { c o } ^ { o } = 0 . 1 , \ s _ { c o } ^ { \bar { P } } = 0 . 1 , \ \tilde { s } _ { c c } ^ { \bar { P } } = 0 , \ c = \bar { 0 } . 0 0 1 , \ \beta _ { o } = 0 . 0 1 , \ \tilde { s } _ { c o } ^ { o } = 1 .$ , and $\beta _ { c } = 0 . 0 1$ . Social welfare under the proprietary strategy is $W ^ { P } = 0 . 7 5$ in panel (b). In panels (b) and (d), $W _ { \mathrm { S P } }$ denotes social welfare under the social planner, $W _ { \mathrm { F M } }$ denotes social welfare under the free market outcome, and $\Delta W = \hat { W } _ { \mathrm { S P } } - W _ { \mathrm { F M } }$

Thus, the stronger complementarity efect helps limit the impact of the strategic efect. Finally, the acrossthe-board increase in quality with the more restrictive license also increases consumer surplus and the overall welfare, again as stated in part (ii) of Proposition 2.

Figure 7 illustrates the originator’s licensing choice and its impact on welfare. As can be seen in Figure $7 ( \mathsf { a } )$ if the license is too permissive so that the originator cannot strongly benefit from the contributor’s eforts (i.e., when $s _ { o c } ^ { \breve { O } }$ is low), it does not pay of for the originator to pursue an open-source strategy under this licensing, and the originator’s best option is to keep the software proprietary. As the originator’s returns from contributor eforts increase, that is, as $s _ { o c } ^ { O }$ increases, a more restrictive open-source license can become the best option for the originator: by becoming the lowerquality service provider in the market, the originator can induce increased investment by the contributor. However, structuring more restrictive licenses to extract increased returns does not necessarily pay of. With further increases in $s _ { o c } ^ { O } ,$ , the quality gap between the contributor and the originator decreases, which reduces the contributor’s incentives for development. Hence, such an increase in license restrictiveness can reduce originator profits as we discussed in Proposition 1.<sup>13</sup> This decrease in originator profits can be seen in Figure 7(a).

In Figure 7(b), we plot the welfare associated with an open-source outcome. In this case, the discontinuity observed stems from a significant scaling back of contributor efort because of increases in $s _ { o c } ^ { \dot { O } } .$ . In particular, when the originator’s ability to benefit from the contributor’s investment increases beyond a certain point, the contributor is better of limiting the contributor’s investment; higher investment levels tend to strongly serve the quality of the originator. Therefore, as depicted in Figure 6, the contributor may lower the contributor’s investment, $e _ { c } ^ { O } .$ , by shifting to a distant local maximizer, which discontinuously reduces the overall software and service quality and, hence, results in a discontinuity on the welfare curve. At a certain point, a proprietary strategy may become the best strategy for a software originator. However, higher $s _ { o c } ^ { O }$ values can create incentives for the originator to invest at high levels, engendering more separation and inducing further investments by the contributor. Consequently, an open-source strategy can be obtained, and these increased license requirements that enable the originator to extract larger benefits from contributor eforts can be preferred as Proposition 2 indicates.

Moreover, as illustrated in Figure 7(b), in the lower end of the $s _ { o c } ^ { O }$ spectrum, increasing the openness requirements of the software license may reduce welfare by inducing decreased investments by the contributor. On the other hand, in the higher end of the spectrum, imposing stricter openness requirements, as in GPL-style licenses, can benefit welfare by improving quality for all participants. To gain intuition through a simple example, note that the originator often will have a discrete set of licensing options. Suppose that the originator has two licensing options with $s _ { o c } ^ { O } ,$ corresponding to the two levels marked in Figure 7: $s _ { o c } ^ { L }$ and $s _ { o c } ^ { H }$ (low and high license restrictiveness, respectively). In the free market outcome, as can be seen in Figure $7 ( \mathsf { a } )$ , the originator’s profit is higher under the more restrictive option, $s _ { o c } ^ { H } ,$ , so the originator chooses this restrictive license option. However, as shown in Figure 7(b), social welfare is significantly higher under the less restrictive license option $s _ { o c } ^ { L } ;$ a welfare maximizing social planner would want to enforce limitations on license restrictiveness, eliminating the restrictive option $s _ { o c } ^ { H } .$ In this case, there would be a significant welfare diference between the free-market licensing outcome and the social planner–enforced outcome, which is depicted in Figure 7(b).

By contrast, when the originator is strong, the diference between the free-market outcome and the social planner’s choice for licensing tends to decrease. As the originator becomes stronger compared with the contributor, the originator’s trade-of between harvesting the benefits of the contributor’s investment (complementarity efect) and keeping the contributor in check in the services market (strategic efect) weakens $( \mathrm { i . e . , }$ the complementarity efect starts to dominate). This is because when the originator is strong relative to the contributor, the originator no longer needs nor relies on a large investment by the contributor. Hence, the originator no longer needs to incentivize the contributor to invest a significant amount to develop the software. Therefore, a restrictive license (high $s _ { o c } ^ { O } )$ maximizes the originator’s profit as can be seen from Figure $7 ( \mathrm { c } )$ since benefitting from the contributor’s investment helps prevent the contributor from gaining a quality advantage in the services market. Continuing with the simple example discussed, given an option between the same two $s _ { o c } ^ { \star }$ levels, $s _ { o c } ^ { L }$ and $s _ { o c } ^ { H } .$ , in the free-market outcome, the originator would choose $s _ { o c } ^ { H } .$ , the restrictive license. Unlike the strong contributor case, however, in a setting with a strong originator, this restrictive license also maximizes welfare since it maximizes the originator’s investment and the overall software and service quality as displayed in Figure $7 ( \mathrm { d } )$ . Consequently, both the free market and social welfare maximizing outcomes have the same licensing choice, $s _ { o c } ^ { H } ,$ and the diference in welfare between the two outcomes is zero.

## 5. Discussion of the Model, Analysis, and Limitations

## 5.1. Profit-Seeking Contributors

To our knowledge, our model is one of the first to capture the simultaneously collaborative and competitive relationship between the profit-seeking firms that invest in open-source software development intending to profit from provision of software integration services. The profit-seeking behavior of the contributor firm and the ensuing strategic interaction play a critical role in licensing decisions. To see this, we have analyzed a version of our model with contributors who are not profit-seeking and participate in software development for other reasons, such as altruism or hobbyism. We show that with such contributors, the originator’s critical strategic considerations of pricing, investment, and licensing decisions we discuss in the paper disappear. In particular, the efect of license restrictiveness on the originator’s profits would simply be monotonically increasing, and the originator would set the opensource license as restrictive as possible to maximize the benefits derived from their eforts.<sup>14</sup> Therefore, we conclude that the profit-seeking behavior of open-source contributors plays a critical role in open-source development investments and licensing choice.

## 5.2. The Role of Competitive Integrators

Competitive integrators are pervasive and serve an important role in IT services markets. We include them in the model because their role in these markets significantly shapes the strategic decisions being made by the originator and contributor, particularly when contemplating diferent OSS licensing arrangements. In particular, their existence becomes quite impactful as the implementation cost of these services becomes higher. In such cases, it becomes more dificult to retain adequate margins in the services market because higher quality levels are necessary and investments to achieve them are quite costly. Higher licensing restrictiveness can help boost quality by leveraging the contributor’s efort, but ultimately, it will be in the best interest of the strategic players to set prices in a manner that strategically push the competitive integrators out of the market. We demonstrate that the existence of competitive integrators pricing at cost can lead to more competitive outcomes when strategic players utilize limit pricing and GPL licenses can have a positive impact on qualities, profits, and welfare. Competitive integrators are fundamental to this result.

Figure 8. Numerical Illustration of the Region of Applicability for Propositions 1 and 2  
![](/api/attachments/7BZEDDV6/fulltext/images/d0146dc849d936733ce4a3ed81f9c962cc2cc003f7fe7ad126298fb6ef6366e8.jpg)

![](/api/attachments/7BZEDDV6/fulltext/images/ea6ec9aaf42f6b9cb797afaeab844ff0c4d18f32570445e5e790b41e2680d376.jpg)  
Notes. The grey shaded areas, labeled A and B, are delineated by the parameter bounds described in Propositions 1 and 2 and indicate the regions where the proposition statements are satisfied. The parameter values for panel (a) are $g _ { o } = 0 . 1 , g _ { c } = \hat { 0 . 1 } , s _ { o o } ^ { O } = 1 , s _ { c c } ^ { O } = 1 , s _ { c o } ^ { O } = 0 . 5 , s _ { c o } ^ { P } = 0 . 0 5 ,$ $s _ { c c } ^ { P } = 0 , \beta _ { o } = 0 . 1$ and c <sup></sup> 0.01. The parameter values for panel (b) are $g _ { o } = 3 , g _ { c } = 3 , \\bar { s } _ { o 0 } ^ { O } = 7 , s _ { c c } ^ { O } = 3 , \bar { s } _ { c o } ^ { O } = 0 . \bar { 1 0 } , s _ { c o } ^ { P } = 0 . \bar { 0 5 } , s _ { c c } ^ { P } = 0 , \beta _ { o } = 0 . 3 0 , ( s _ { o c } ^ { O } ) ^ { L } = 3 . 1$ and $( s _ { o c } ^ { \dot { O } } ) ^ { \dot { H } } = 2 5$

## 5.3. Service Provision Costs

In our model, we assumed that service provision costs are independent of service quality. This is a reasonable assumption from the perspective of practice and modeling. In general, when firms invest to develop software, the service quality improves from built-in expertise and better developed utilities and tools. That is, a service provider firm can charge more for the higher quality service, but it does not mean that the marginal cost of providing the service has gone up. In other words, the built-in expertise and the developed support software in this case can be considered as fixed costs as once those are attained there is no real increase in economic costs of providing services. Furthermore, even if there were an increase in the marginal costs of providing services, from a modeling perspective, as long as there were some gains in quality through investment, the model outcome would be similar or equivalent in substance to a constant service cost model in that an increase in costs can be mathematically transformed and absorbed in the value generated by the quality increase.

## 5.4. Robustness and the Regions of Applicability

Some of our results use asymptotic analysis, which is standard and often used in microeconomic analysis when the analysis is complex (see, e.g., Li et al. 1987, Lafont and Tirole 1988, Pesendorfer and Swinkels 2000, and Vereshchagina and Hopenhayn 2009, among others). Given the complexity of the setting (e.g., involvement of multiple layers of nested optimizations), it is not possible to obtain a full analytical identification of the regions under all parameter sets. However, our results are not restricted to limits and instead are robust and satisfied for wide parameter regions. One can perform a sensitivity analysis and numerically identify the parameter regions where the results are valid. Figure 8(a) and 8(b) demonstrate sample applicability regions for Propositions 1 and 2, respectively. As can be seen from Figure 8(a), Proposition 1 is valid on a broad region. Fixing other parameters under the strong contributor regime (i.e., when $\beta _ { c } \ll \beta _ { o } )$ with any combination of $\beta _ { c } / \beta _ { o }$ and $s _ { o c } ^ { O } / s _ { c c } ^ { O }$ ratios in the region labeled with $A ,$ the statement of the proposition would hold. Similarly, Figure 8(b) demonstrates an example for the upper and lower bounds of the service cost parameter $c , \underline { { \nu } }$ and ν¯ as a function of $\beta _ { c } / \beta _ { o }$ as is characterized in Proposition 2. One can observe that there is a broad parameter region (labeled B) in which the proposition statement is valid.

## 6. Concluding Remarks

In this research note, we presented a model of OSS development that captures the incentives for firms to pursue and contribute to an open-source project, driven by a market for software services. We studied the trade-ofs faced by an originating firm deciding between open and proprietary approaches for the originator’s software products. If the originator pursues a proprietary strategy, the firm does not benefit from the contributions of other developers dedicating resources toward creating higher quality software that carries a higher value in the consumer market. However, the firm retains the ability to generate revenues from selling copies of the originator’s product regardless of whether the originator provides the associated services aspect. Should a firm choose an open-source strategy, the originator can benefit from the positive quality efects. However, the originator can no longer charge purely for the originator’s software product. The originator’s primary source of revenue under an open-source path lies with ofering integration and support services, which is of significant value to consumers in most cases. This competitive aspect is characterized by quality competition between originating and contributing firms as they invest efort into opensource development, followed by price competition in the services market.

Given the wide range of licenses employed in the open-source domain, we studied whether restrictive or permissive licenses are better for profitability and welfare. We find that in cases in which an open-source contributor is adept in reaping the benefits of the contributor’s own eforts to a greater extent than the originator, requiring or favoring less restrictive licenses (e.g., BSD style) can increase both the originator’s profits and welfare. However, if the originator can harness contributor eforts well and the service costs are high, a more restrictive (e.g., GPL style) license can increase developers’ contributions and overall software quality.

Note that with a permissive license, the contributor could, in certain cases, have the option of opening up the contributor’s contributions and benefiting the originator in the services market, efectively replicating the outcome of the restrictive license. In other words, under open-source licensing, in some cases, the contributor can efectively increase $\stackrel { \cdot } { s _ { o c } ^ { O } }$ if the contributor’s profit increases. However, there are a couple of concerns about including this option in the current paper. First, modeling it would add yet another layer of optimization on top of the two firms’ pricing and efort levels, and would make the problem much more complex, the exposition less transparent, and the solution less tractable. Second, it is likely that, in many cases, facing an option of opening up the contributor’s software when the contributor is not required to do so, the contributor would likely not choose such an option that would benefit the contributor’s competitor and reduce the contributor’s own profit in the services marketplace. Hence, given that including this option is unlikely to change the outcome while making the analysis and the exposition significantly more complex and less transparent and aiming to keep the paper’s focus sharp, we chose not to include this option in the current paper. However, this is an interesting potential extension to the model that could be explored in a future study to deepen the understanding of license restrictiveness on the contributor firms’ strategic decisions to voluntarily open their contributed code when they are not required to do so by the license set by the software originator.

With significantly increased usage and attention in the past decade, OSS is an increasingly prominent tool in today’s business economic environment and promises to generate tremendous value for its users. What is even more encouraging is the recent emergence of service-based revenue models that provide steady revenue streams for companies that invest, develop, maintain, and support this important software solution approach. Regulating bodies and policy makers as well as companies that develop, support, or use OSS, whether they are government agencies or software and trade associations, should be aware of the economic dynamics of OSS and how to harness its potential value.

## Acknowledgments

The authors thank the senior editor, the associate editor, and the anonymous reviewers for their helpful suggestions throughout the review process. The authors also thank seminar participants at Georgia Tech and participants at the Workshop on Information Systems Economics 2014 for their helpful comments and discussions.

## Endnotes

<sup>1</sup> See, for example, August et al. (2013) for a discussion of integration, support, and consulting services.

<sup>2</sup> In some cases, contributors to OSS can be large, cost-eficient firms, such as Hewlett-Packard (HP) and IBM. HP has more than 2,500 developers working on OSS (HP 2007); similarly, IBM dedicates vast resources to OSS because its global services divisions generate \$58 billion in revenue, which exceeds revenues from its software and hardware businesses (IBM 2012).

<sup>3</sup> The originator in the case of Hadoop is now the chief architect of Cloudera, which competes in the same space.

<sup>4</sup> In some contexts, the contributor can be the individual developers who are not profit seeking. We also consider this case in Section B of the online appendix and analytically show that profits, social welfare, and consumer surplus increase as OSS licensing becomes more restrictive, which is similar to the cases discussed in Figure 7(c) and 7(d). Please see the online appendix for a detailed analysis. We thank an anonymous reviewer for this suggestion.

<sup>5</sup> Typically, the base OSS product is both nonrival and nonexcludable, consistent with the nature of a public good (Samuelson 1954).

<sup>6</sup> By “competitive integrator,” we mean any IT human resource who is able to provide basic services on the OSS product but is not involved in the development of the product and its direction (and therefore has not built the extensive expertise that comes from OSS project involvement). A competitive integrator can include (i) small companies that ofer basic IT services, such as Open Source Architect, a small business in Nevada that provides JBoss consulting services, and (ii) individuals hired in-house who have basic knowledge of an OSS product. It can even be the case that a large IT consulting company sends out resources for paid help on technologies that they do not possess expert level knowledge of, this being an unfortunately common occurrence in practice (Markon and Crites 2013).

<sup>7</sup> Such cases usually happen when the originator is a relatively big and established firm compared with the major outside contributors. One open source project that fits well with this characterization is the JBoss application server. The JBoss project was started in 1999 and quickly became a force in the middleware market with an entirely services-based business model (Kerstetter 2004). JBoss Inc. harnessed the open source developer community well, becoming the leading services provider of the open-source product and maintaining tight control over the project’s evolution.

<sup>8</sup> An example of this case is the Apache Software Foundation (ASF) project Geronimo. Geronimo is an open-source application server that was founded by members of the ASF. One company that ofers services related to many ASF open-source projects, including Geronimo, is Covalent Technologies, which employs some of the founders of Geronimo. However, IBM dedicates a significant amount of resources to the Geronimo project because of its own acquisition of Gluecode and interest in providing services to the lower tier of the application server market, and IBM is the most prominent development leader for the project. In this case, the contributor (IBM) is the more cost-eficient entity that can strongly leverage the originator’s efort while the originator tends to provide services to a smaller market.

<sup>9</sup> For simplicity in exposition and to avoid trivialities, in Lemmas 1 and 2 we focus only on the parameter regions that are relevant to the full game equilibrium.

<sup>10</sup> See Lemma 1 as well as Lemma EC.2 in the online appendix.

<sup>11</sup> Full characterizations of $\tau _ { A } ( \vec { Q } ) , \tau _ { B } ( \vec { Q } )$ , and $\tau _ { C } ( \vec { Q } )$ are given in the proof of Lemma 2 in the online appendix.

<sup>12</sup> The closed form expression of $\underline { { \boldsymbol \gamma } }$ is given in the proof provided in the online appendix.

<sup>13</sup> By taking a point in this region $( \mathbf { e . g . } , s _ { o c } ^ { O } = 0 . 6 0 )$ , we can demonstrate the wide parameter range for which Proposition 1 is satisfied. Consistent with the results from Proposition 1, by slightly decreasing $s _ { o c } ^ { O }$ from 0.60, profits increase, and, as can be seen in Figure 7(b), social welfare increases. Furthermore, we find that these results continue to hold for any g satisfying 0 <sup>≤</sup> g < <sup>∞</sup>, and $\beta _ { c }$ can be increased up to fivefold.

<sup>14</sup> We provide this model and its analysis in Section B of the online appendix.

## References

Andreoni J (1988) Privately provided public goods in a large economy: The limits of altruism. J. Public Econom. 35(1):57–73.

Arrow KJ (1962) The economic implications of learning by doing. Rev. Econom. Stud. 29(3):155–173.

Asundi J, Carare O, Dogan K (2012) Competitive implications of software open-sourcing. Decision Support Systems 54(1):153–163.

August T, Chen W, Zhu K (2014) Competition among proprietary and open-source software firms: The role of licensing on strategic contribution. Working paper, University of California, San Diego.

August T, Shin H, Tunca TI (2013) Licensing and competition for services in open source software. Inform. Systems Res. 24(4): 1068–1086.

Bain JS (1949) A note on pricing in monopoly and oligopoly. Amer. Econom. Rev. 39(2):448–464.

Bessen J (2006) Open source software: Free provision of complex public goods. Bitzer J, Schroder PJ, eds. The Economics of Open Source Software Development (Emerald Group Publishing, Bingley, UK), 57–82.

Bulow JI, Geanakoplos JD, Klemperer PD (1985) Multimarket oligopoly: Strategic substitutes and complements. J. Political Econom. 93(3):488–511.

Casadesus-Masanell R, Ghemawat P (2006) Dynamic mixed duopoly: A model motivated by Linux vs. Windows. Management Sci. 52(7):1072–1084.

Casadesus-Masanell R, Llanes G (2011) Mixed source. Management Sci. 57(7):1212–1230.

Cheng HK, Liu Y, Tang QC (2011) The impact of network externalities on the competition between open source and proprietary software. J. Management Inform. Systems 27(4):201–230.

Clark D (2014) Intel’s investment into Cloudera totals \$740 million. Wall Street Journal (March 31). https://www.wsj.com/articles/ intels-investment-into-cloudera-totals-740-million-1396281655.

Cohan P (2013) With \$141 million in capital, IPO-bound Cloudera sprints to \$1 billion in revenue. Forbes (October 29). https:// www.forbes.com/sites/petercohan/2013/10/29/with-141 -million-in-capital-ipo-bound-cloudera-sprints-to-1-billion-in -revenue/#5f2e794c368b.

Colazo J, Fang Y (2009) Impact of license choice on open source software development activity. J. Amer. Soc. Inform. Sci. Tech. 60(5):997–1011.

Columbus L (2016) Miško Hevery, inventor of angular and how open source languages are redefining enterprise software. Forbes (November 14). https://www.forbes.com/sites/louis columbus/2016/11/14/misko-hevery-inventor-of-angular-and -how-open-source-languages-are-redefining-enterprise-software/ #15ef0c29270d.

Dorroh JR, Gulledge TR, Womer NK (1994) Investment in knowledge: A generalization of learning by experience. Management Sci. 40(8):947–958.

Dutton JM, Thomas A (1984) Treating progress functions as a managerial opportunity. Acad. Management Rev. 9(2):235–247.

Fine CH (1986) Quality improvement and learning in productive systems. Management Sci. 32(10):1301–1315.

Fishman S (2004) Open source licenses are not all the same. O’Reilly ONLamp.com (November 18). http://www.onlamp.coms/pub/ a/onlamp/2004/11/18/licenses.html.

FTC (2017) About the FTC. Federal Trade Commission, Washington, DC. https://www.ftc.gov/about-ftc/.

Gabszewicz JJ, Thisse J-F (1979) Price competition, quality and income disparities. J. Econom. Theory 20(3):340–359.

Gaudeul A (2004a) Competition between open-source and proprietary software: The LaTeX case study. Working paper, University of East Anglia, Norwich, UK.

Gaudeul A (2004b) Open source software development patterns and license terms. Working paper, University of East Anglia, Norwich, UK.

Glick B (2013) Government mandates “preference” for open source. ComputerWeekly (March 15). http://www.computerweekly .com/news/2240179643/Government-mandates-preference-for -open-source.

Groves T, Ledyard J (1977) Optimal allocation of public goods: A solution to the “free rider” problem. Econometrica 45(4):783–809.

Hars A, Ou S (2002) Working for free? Motivations for participating in open-source projects. Internat. J. Electronic Commerce 6(3): 25–39.

Haruvy E, Sethi SP, Zhou J (2008) Open source development with a commercial complementary product or service. Production Oper. Management 17(1):29–43.

Hawkins RE (2004) The economics of open source software for a competitive firm. Why give it away for free? Netnomics 6(2): 103–117.

Herz J, Lucas M, Scott J (2006) Open technology development: Roadmap plan. U.S. Department of Defense, Washington, DC.

Hillesley R (2008) Red Hat at the crossroads. ITPRO (January 14). http://www.itpro.co.uk/155277/red-hat-at-the-crossroads.

Hitt LM, Wu DJ, Zhou X (2002) Investment in enterprise resource planning: Business impact and productivity measures. J. Management Inform. Systems 19(1):71–98.

Holmstrom B, Milgrom P (1991) Multitask principal-agent analyses: Incentive contracts, asset ownership, and job design. J. Law, Econom., Organ. 7:24–52.

HP (2007) Open source and Linux from HP. Hewlett-Packard, Palo Alto, CA.

Iansiti M, Richards GL (2006) The business of free software: Enterprise, incentives, investment, and motivation in the open source community. Working paper, Harvard Business School, Cambridge, MA.

IBM (2012) IBM 2012 annual report. Armonk, NY.

JBoss (2008) Professional open source licensing. JBoss, Inc., http:// www.jboss.org/company/licensing/.

Kerstetter J (2004) Redemption for JBoss’s boss. BusinessWeek. https://www.linuxtoday.com/it\_management/2004102000726 insvsw.

King R (2014) Open source “eating” software world: Samsung. Wall Street Journal. https://blogs.wsj.com/cio/2014/05/05/open -source-eating-software-world-samsung/.

Kuan J (2001) Open source software as consumer integration into production. Working paper, Stanford University, Stanford, CA.

Kumar V, Gordon BR, Srinivasan K (2011) Competitive strategy for open source software. Marketing Sci. 30(6):1066–1078.

Lafont J-J, Tirole J (1988) The dynamics of incentive contracts. Econometrica 56(5):1153–1175.

Lakshminarayanan R (2014) Open source provides compelling benefits to business. ZDNet (July 31). http://www.zdnet.com/ article/open-source-provides-compelling-benefits-to-business/.

Lee D, Mendelson H (2008) Divide and conquer: Competing with free technology under network efects. Production Oper. Management 17(1):12–28.

Lerner J, Pathak PA, Tirole J (2006) The dynamics of open-source contributors. Amer. Econom. Rev. 96(2):114–118.

Lerner J, Tirole J (2002) Some simple economics of open source. J. Indust. Econom. 50(2):197–234.

Lerner J, Tirole J (2005a) The economics of technology sharing: Open source and beyond. J. Econom. Perspect. 19(2):99–120.

Lerner J, Tirole J (2005b) The scope of open source licensing. J. Law, Econom., Organ. 21(1):20–56.

Levy FK (1965) Adaptation in the production process. Management Sci. 11(6):B136–B154.

Li G, Rajagopalan S (1998) Process improvement, quality, and learning efects. Management Sci. 44(11):1517–1532.

Li L, McKelvey RDM, Page T (1987) Optimal research for cournot oligopolists. J. Econom. Theory 42(1):140–166.

Linux Foundation (2013) 2013 enterprise end user report. Linux Foundation, San Francisco.

Markon J, Crites A (2013) Health-care web site’s lead contractor employs executives from troubled IT company. Washington Post (November 15). https://www.washingtonpost.com/politics/ health-care-web-sites-lead-contractor-employs-executives-from -troubled-it-company/2013/11/15/6e107e2e-487a-11e3-a196 -3544a03c2351\_story.html?utm\_term=.25a635d47832.

McMillan R (2012) Red Hat becomes open source’s first \$1 billion baby. Wired (March 28). https://www.wired.com/2012/03/red -hat/.

Mehra A, Mookerjee V (2012) Human capital development for programmers using open source software. MIS Quart. 36(1): 107–122.

Mehra A, Dewan R, Freimer M (2011) Firms as incubators of opensource software. Inform. Systems Res. 22(1):22–38.

Modigliani F (1958) New developments on the oligopoly front. J. Political Econom. 66(3):215–232.

Moldovanu B, Sela A (2001) The optimal allocation of prizes in contests. Amer. Econom. Rev. 91(3):542–558.

Montague B (2008) Why you should use a BSD style license for your open source project. https://www.freebsd.org/doc/en\_US .ISO8859-1/articles/bsdl-gpl/article.html.

Noyes K (2014) Security and quality top companies’ reasons for using open source. PCWorld (April 7). https://www.pcworld.com/ article/2140210/why-use-open-source-security-and-quality-top -companies-lists.html.

Paulnock C (2016) Open source solves and supports today’s business needs. CIOReview. https://opensource.cioreview.com/ cxoinsight/open-source-solves-and-supports-today-s-business -needs-nid-23389-cid-92.html.

Pesendorfer W, Swinkels JM (2000) Eficiency and information aggregation in auctions. Amer. Econom. Rev. 90(3):499–525.

Radner R, Myerson R, Maskin E (1986) An example of a repeated partnership game with discounting and with uniformly ineficient equilibria. Rev. Econom. Stud. 53(1):59–69.

Roberts JA, Hann I-H, Slaughter SA (2006) Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7):984–999.

Rusin Z (2008) Open source licenses. KDE, Brighton, MA. http:// developer.kde.org/documentation/licensing/licenses\_summary .html.

Samuelson PA (1954) The pure theory of public expenditure. Rev. Econom. Statist. 36(4):387–389.

Sen R (2007) A strategic analysis of competition between open source and proprietary software. J. Management Inform. Systems 24(1):233–257.

Sen R, Subramaniam C, Nelson ML (2009) Determinants of the choice of open source software license. J. Management Inform. Systems 25(3):207–239.

Sen R, Subramaniam C, Nelson ML (2011) Open source software licenses: Strong-copyleft, non-copyleft, or somewhere in between? Decision Support Systems 52(1):199–206.

Singh PV, Phelps C (2013) Networks, social influence, and the choice among competing innovations: Insights from open source software licenses. Inform. Systems Res. 24(3):207–239.

Spence AM (1981) The learning curve and competition. Bell J. Econom. 12(1):49–70.

Stewart KJ, Ammeter AP, Maruping LM (2006) Impacts of license choice and organizational sponsorship on user interest and development activity in open source software projects. Inform. Systems Res. 17(2):126–144.

Tunca TI, Wu Q (2013) Fighting fire with fire: Commercial piracy and the role of file sharing on copyright protection policy for digital goods. Inform. Systems Res. 24(2):436–453.

Vanian J (2016) Red Hat CEO on Microsoft, Google, and cutting edge software. Fortune (November 18). http://fortune.com/2016/11/ 18/red-hat-ceo-james-whitehurst-microsoft-google-software/.

Varian H (2004) System reliability and free riding. Camp LJ, Lewis S, eds. Economics of Information Security (Springer, New York), 1–15.

Vereshchagina G, Hopenhayn HA (2009) Risk taking by entrepreneurs. Amer. Econom. Rev. 99(5):1808–1830.

von Krogh G, von Hippel E (2006) The promise of research on open source software. Management Sci. 52(7):975–983.

Von Krogh G, Haefliger S, Spaeth S, Wallin MW (2012) Carrots and rainbows: Motivation and social practice in open source software development. MIS Quart. 36(2):649–676.

Wen W, Ceccagnoli M, Forman C (2016) Opening up intellectual property strategy: Implications for open source software entry by start-up firms. Management Sci. 62(9):2668–2691.

West J (2003) How open is open enough? Melding proprietary and open source platform strategies. Res. Policy 32(7):1259–1285.

Zhu KX, Zhou ZZ (2012) Lock-in strategy in software competition: Open-source software vs. proprietary software. Inform. Systems Res. 23(2):536–545.
