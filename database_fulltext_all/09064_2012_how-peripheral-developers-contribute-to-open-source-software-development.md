---
otero_id: 9064
otero_key: "R724Z757"
title: "How Peripheral Developers Contribute to Open-Source Software Development"
authors: "Pankaj Setia; Balaji Rajagopalan; Vallabh Sambamurthy; Roger Calantone"
year: "2012"
journal: "Information Systems Research"
doi: "10.1287/isre.1100.0311"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/R724Z757/fulltext/images/f85b475dda8262b640aaeaa72f3200140b4ee25908ac7300b88c1f595bf26aa2.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# How Peripheral Developers Contribute to Open-Source Software Development

Pankaj Setia, Balaji Rajagopalan, Vallabh Sambamurthy, Roger Calantone,

## To cite this article:

Pankaj Setia, Balaji Rajagopalan, Vallabh Sambamurthy, Roger Calantone, (2012) How Peripheral Developers Contribute to Open-Source Software Development. Information Systems Research 23(1):144-163. http://dx.doi.org/10.1287/isre.1100.0311

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2012, INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/R724Z757/fulltext/images/119fbc394f71a596fe99eb2cce363d6fc1d4800e4b17315163b8e1ae1d1e27d4.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# How Peripheral Developers Contribute to Open-Source Software Development

Pankaj Setia

Sam M. Walton College of Business, University of Arkansas, Fayetteville, Arkansas 72701, psetia@walton.uark.edu

Balaji Rajagopalan

School of Business Administration, Oakland University, Rochester, Michigan 48309, rajagopa@oakland.edu

Vallabh Sambamurthy, Roger Calantone

Eli Broad School of Business, Michigan State University, East Lansing, Michigan 48824 {sambamurthy@bus.msu.edu, rogercal@bus.msu.edu}

pen-source software development is the next stage in the evolution of product development, particularly software products. Compared with the prevailing proprietary approaches, open-source software products are developed by co-opting external developers and prospective users. Although a core group of developers might still play a key role in the initial design and development, a notable aspect of the open-source software paradigm is the role of peripheral developers in the enhancement and popularization of the product. Peripheral developers are not formal members of the core development team. They voluntarily contribute their time and creative talent in improving the quality of the product or in popularizing the product through word-of-mouth advocacy. As volunteers, they are not subject to the traditional hierarchical controls, nor are they contractually obligated. Peripheral developers represent a novel and unique aspect of open-source software development, and there is a greater interest in tapping their potential. However, there has been limited evidence about how and when their participation has beneficial impacts. We examine how peripheral developers contribute to product quality and diffusion by utilizing longitudinal data on 147 open-source software products. Hierarchical linear modeling analysis indicates that peripheral developers make significant contributions to product quality and diffusion, especially on projects that are in the more mature stages of product development.

Key words: open source; diffusion; quality; new product development; adoption; software development; peripheral developers

History: Sandra Slaughter, Senior Editor. This paper was received June 1, 2007, and was with the authors for 23 <sup>1</sup> months for 4 revisions. Published online in Articles in Advance November 18, 2010.

## 1. Introduction

Traditionally, new product development processes have utilized a stage-gate approach, including design, development, and commercial launch as distinct and discrete stages (Krishnan and Ulrich 2001, Bajaj et al. 2004). Although the original models had emphasized that the activities in each stage should be performed sequentially, these processes have evolved by incorporating both overlap and iterations between the stages to enhance product quality and reduce development cycle time (Ha and Porteus 1995, Clark and Fujimoto 1991, Krishnan et al. 1997, Eisenhardt and Tabrizi 1995, Terwiesch and Loch 1999). Furthermore, in the prevailing approach a core group of developers tightly controlled the design and development activities. However, with growth in the industry for software products, users acquired a more active role in the enhancement of the product prior to its commercialization. Instead of an arms-length relationship with users, software product developers have sought to coopt potential users by seeking feedback to enhance the quality of the products or success of the commercial launch. However, the core developers still retain control and authority over key aspects of product development.

Open-source software (OSS) development represents the next paradigm in the continuing evolution of processes for the development and commercialization of software products. It utilizes a community perspective to software development by co-opting external developers and prospective users and providing them with broader access and authority in product enhancement. Because of the lack of controlled and monitored growth, OSS products further erode the partition between the product life-cycle stages as they continue to develop and diffuse simultaneously. The evolutionary growth of the software is associated with an open and free culture of development. In fact, the lack of control is often touted as a source of creativity in the OSS model. Bonaccorsi and Rossi (2003) note:

Hierarchical coordination based on the ownership of assets is not a necessary condition for carrying out complex software development tasks. On the contrary, such coordination would end up depressing the intellectual, aesthetic and pleasure-based motivation that seem intrinsic to the programming community. (p. 1248)

This open culture offers greater opportunities for external contributors, i.e., from those who are not formal or permanent members of the development team. Although a core group of developers might still play a key role in the design and initial development of the OSS product, a notable aspect of the OSS paradigm is the role of peripheral developers (AlMarzouq et al. 2005, Crowston and Howison 2005, Mockus et al. 2002, Gacek et al. 2001, Cox 1998). Peripheral developers are outside of the core development team, and they may temporarily and voluntarily contribute their time and creative talent to improving the quality of the product or to popularizing it (Crowston et al. 2006). They could infuse new ideas to improve products, reduce time to development, and enhance participation in development (Chesbrough 2003). Although the role of peripheral developers has gained increased interest, little is known about their contributions to OSS development projects. There is an ever-increasing interest among research organizations, government,<sup>1</sup> and corporations in emulating the OSS development model (Brown and Hagel 2006, Chesbrough 2003, Goldman and Gabriel 2005),<sup>2</sup> particularly with a desire to tap the contributions of peripheral developers. Corporations are integrating open innovation initiatives with the proprietary ways of software product development (Dinkelacker and Garg 2001, Gurbani et al. 2005, Fitzgerald 2006).

Some of the prior research has examined the behaviors and motivations of contributors to OSS development projects (Lakhani and von Hippel 2003, Lerner and Tirole 2002, Hertel et al. 2003, Shah 2006, Roberts et al. 2006). Whereas core developers are often motivated by an “itch,” the motivations for peripheral developer are not yet clearly known. Unlike the developers in proprietary development projects, peripheral participants are often not contractually obligated, and hence the nature of their contributions to OSS products is not clear. Thus, the first research question being examined is whether, in comparison with core developers, peripheral developers make more salient contributions to the OSS product quality. We also seek to understand whether peripheral developers have positive impacts on product diffusion. Open-source software development has a starkly different evolutionary life cycle, where the product’s survival, success, and commercializability increase over time through a life cycle characterized by alpha, beta, and mature stages (Stewart and Gosain 2006). The products often undergo starkly different development dynamics across these stages. Indeed, prior research has found that the development team’s impact on performance in OSS projects varies across the life-cycle stages (Stewart and Gosain 2006). This implies that the OSS life-cycle maturity might have an important influence on the nature of peripheral developer contributions. Therefore, our second research question is: How do the contributions and impacts of peripheral developers vary across the OSS product life cycle?

We develop a theory of peripheral developer contributions to OSS products in order to address these questions. Specifically, we focus on the contributions of peripheral developers to two aspects of OSS development: quality enhancement and product diffusion. Furthermore, we examine how these impacts on product quality and diffusion vary across the product life cycle of OSS products. The rest of this paper is organized as follows. In §2 we review prior work and develop hypotheses. Next, in §3, we present the details of data collection and the measures used. Empirical analysis using the hierarchical linear model (HLM) is presented in §4. We discuss the results in §5 and present concluding remarks in §6.

## 2. Research Model

OSS products develop through the contributions of two distinct types of developers: core and peripheral participants. Core developers are founders or initiators of the product, and they lead the development of the product architecture and core modules. In contrast, peripheral developers work on product enhancement (AlMarzouq et al. 2005). Crowston et al. (2006) identify ways to distinguish between core and peripheral participants according to the extent of contributions and the nature of developer interactions. Often, developers vary in the ways they contribute to an OSS product (AlMarzouq et al. 2005). Therefore, we propose that whereas core developers have longterm product affiliations, peripheral developers may be motivated by a more short-term focus on enhancing the utility of the OSS product to themselves, or by a desire to contribute to the community. Furthermore, OSS products are created with limited direct contact between peripheral participants. Very often, peripheral developers may not be directly involved in the initial design phase. Thus, they could contribute only to specific product quality aspects, such as detection or correction of defects. Their contributions are likely to be restricted to activities that meet these motivations. Therefore, we focus our attention on two plausible dimensions of product quality: product quality assessment and product quality enhancement. Product quality assessment involves activities to assess and report areas for improvements (such as by finding defects) in OSS products, whereas product quality enhancement entails making these improvements (for example, by fixing these defects). Although they are integral to the OSS domain, these activities may differ in the amount of required effort and engagement. We examine how peripheral developers’ contributions to these aspects of product quality development differ from the contributions of core developers.

Furthermore, OSS products differ from proprietary software in how they gain recognition among potential adopters. In the absence of vast advertising networks, adopters of OSS products rely on the members of the community in the evaluation of a product (Dalle and Jullien 2000, Bonaccorsi and Rossi 2003). Models of product adoption have largely focused on awareness and adoption as the two key stages (Bonus 1973, Kalish 1985, Mason 1962). These stages differ in the nature of communication required of product emissaries. The awareness stage involves “communication to inform,” because it entails less engaged evaluation by potential adopters whose intention is to gain awareness about the product and its attributes (Bucklin 1965, Lavidge and Steiner 1965, Mehta et al. 2008). On the other hand, adoption, especially of complex products (such as software innovations), often entails a more in-depth and engaged examination of the product (Kalish 1985, Aaker and Stayman 1990). Thus, similar to the quality outcomes, the two diffusion outcomes—OSS product awareness and OSS product adoption—may also differ in the level of engagement required from peripheral developers (see Table 1). In our research model, we theorize about the contributions of peripheral participants to open-source product quality and diffusion and examine their influence across the product life-cycle stages (Figure 1).

Table 1 The Categorization of Quality and Diffusion Outcomes According to Peripheral Developer Engagement

<table><tr><td></td><td>Low engagement</td><td>High engagement</td></tr><tr><td>Open-source product quality</td><td>OSS product quality assessment</td><td>OSS product quality enhancement</td></tr><tr><td>Open-source product diffusion</td><td>OSS product awareness</td><td>OSS product adoption</td></tr></table>

Figure 1 Research Model  
![](/api/attachments/R724Z757/fulltext/images/833c814aa234794e45e7008281557300903e309fbe4f99a14517fa4387042134.jpg)

## 2.1. The Influence of Peripheral Developers on OSS Product Quality Assessment

Quality assessment is an important element of product development. Because of the complexity of design and development, software products may never be completely developed Defects, also known as bugs, might be hidden in the software for long periods of time before a user discovers them. In the opensource model, the products are publicly available and peripheral developers might be able to contribute to quality assessment by detecting bugs. For example, as Raymond (1999, p. 41) notes, “Given enough eyeballs, all bugs are shallow.”

Peripheral developers have the motivation and capabilities to contribute to product quality assessment through bug detection. They are motivated to enhance the utility of the product for their own consumption. Utility arguments suggest that some developers are motivated to contribute to quality assessment so that they can meet their own needs from the use of the product (Shah 2006). The utility perspective might be particularly relevant for peripheral developers who are current or future users. A peripheral developer could be an end user or a core developer on another open-source product, who wants to access the functionality of the product for his or her own work. Peripheral developers have a unique perspective and potential use for the product. They test the product in different use environments, often different from the original environment where the core developers might have produced the product. The software is thus tested and stressed in more ways than is plausible with a team of direct product testers or core developers. As Raymond (2001, p. 32) points out, “More users find more bugs because adding more users adds more different ways of stressing the program.” Furthermore, once they find bugs, reporting them to the core team offers them an opportunity to get a fix for the functionality that they need (Shah 2006). Moreover, peripheral developers have a unique capability for quality assessment. They possess a different lens through which they view the code, one that is different from the core developers for the product. Raymond notes, “Each [user] approached the task of bug characterization with a slightly different perceptual lens and analytical toolkit, a different angle on the problem” (1999, pp. 41–44). Thus, product quality assessment is ideally suited for contributions from peripheral participants who possess the desired motivations and competencies. Given the potential contributions that peripheral developers can make toward product quality assessment, we propose that they are more suited than the core developers for this activity and that greater number of peripheral developers will enhance the assessment efforts on the product.

<sup>Hypothesis</sup> <sup>1A</sup> <sup>(H1A).</sup> Compared with core developers, the degree of participation of peripheral developers will have a greater impact on quality assessment of the OSS products.

## 2.2. The Influence of Peripheral Developers on OSS Product Quality Enhancement

Product quality enhancement refers to actions for improving products, such as by fixing defects. These actions require a higher level of effort, commitment, and coordination than product quality assessment. Peripheral developers are likely to be motivated for quality enhancement for utilitarian and community affiliation reasons. On one hand, they will be motivated to enhance the product, particularly by fixing some of the discovered bugs.<sup>3</sup> On the other hand, the culture and values of open-source communities are similar to those of the scientific community (Bezroukov 1999) or social movements such as the civil rights, labor, and, peace movements (Hertel et al. 2003). In these communities, members voluntarily contribute their time and effort to improve the communal products or services and enhance their community’s visibility, goal accomplishment, and sustainability. By enhancing the quality of products being developed within the community, developers may demonstrate their citizenship and adherence to the collective goals of the community (Bonacorrsi and Rossi 2003). These perspectives are relevant in explaining why peripheral developers contribute toward product enhancement.

Peripheral developers also have unique competences to enhance the quality of OSS products. Research suggests that product manufacturers often have a strong mental model of the existing product and may fixate on the existing product, because of their existing real-world experiences (Lilien et al. 2002). Because of their fixation on the existing products, core developers may hold the current design of the product as constant. On the other hand, peripheral contributors might not be so fixated on the original code design. They are likely to have independent, novel, and unique insights and contribute solutions to bugs that are not fixated on the existing design. Hence, we propose the following hypothesis.

<sup>Hypothesis</sup> <sup>1B</sup> <sup>(H1B).</sup> Compared with core developers, the degree of participation of peripheral developers will have a greater impact on the quality enhancement of OSS products.

## 2.3. The Influence of Peripheral Developers on OSS Diffusion

The success of OSS products depends on their diffusion to a wide community of prospective users. Two diffusion outcomes—awareness and adoption— are most pertinent because these represent salient stages of product adoption (Bonus 1973, Kalish 1985, Van den Bulte and Lilien 1999). Therefore, we examine the impacts of peripheral developers on the awareness and adoption of OSS products.

The marketing literature has identified informative and persuasive communications as being necessary for awareness and adoption, respectively (Kalish 1985). The awareness stage often entails less effort because potential adopters simply gain information about the product and its attributes (Bucklin 1965, Mehta et al. 2008). On the other hand, adoption (such as software innovations) entails more effort and a deeper examination of the product and its merits (or demerits) (Kalish 1985, Aaker and Stayman 1990). In the awareness stage, “impersonal” informants may suffice. However, adopters often rely on more “personal” informants for adoption decisions. For example, studies of the physician’s adoption of drugs have found that they often decide to adopt a drug because of the influence of personal colleagues, even though sales people might increase their awareness of the drugs (Coleman et al. 1966, Peay and Peay 1984). Therefore, we differentiate between two aspects of diffusion—awareness and adoption—and examine the role of peripheral participants across the two behaviors.

The awareness of OSS products within a community of potential users could occur as the requisite information spreads through mass media and interpersonal channels. Although mass media is useful for sharing standard and codified information, products (such as software) that require the exchange of tacit knowledge could benefit from channels dominated by interpersonal networks. This channel of interpersonal communication is even more important for typical OSS products, because many of them do not have the institutional legitimacy, corporate image, or other resources to tout their products through mass communication vehicles. Most typical OSS products lack a corporate owner or management to organize and coordinate publicity activities for enhancing product awareness (Scacchi et al. 2006). Thus, potential adopters tend to rely more on information from members of the community to create awareness about their product. At a minimum, peripheral participants act as a knowledge source and help spread information about the OSS product. When there are more peripheral developers, they expand the information and, hence, enhance product awareness. Therefore, we propose the following.

<sup>Hypothesis</sup> <sup>2A</sup> <sup>(H2A).</sup> Greater degree of participation of peripheral developers in OSS projects will lead to more awareness about the product.

Word-of-mouth (WOM) communication occurs through person-to-person contact, and it influences individual adoption decisions (Mangold 1987, Webster 1991, Woodside et al. 1992, Murray 1991, Zeithamal et al. 1993). Because of the trusted reliability of the source and the flexibility of interpersonal communication, word of mouth may even have greater influence than printed information or advertising (Herr et al. 1991, Day 1971). Evidence of this one-to-one marketing through word of mouth has been found in prior research. For example, Dalle and Jullien (2000) have referred to local interaction to emphasize the role of close groups that influence the dissemination of Linux in place of Windows NT. Similarly, Bonaccorsi and Rossi (2003) characterize OSS participants as diffusion agents who “not only disseminate information about the new technology but also try to convince a group of potential users to do so simultaneously 0 0 0 ” (p. 1251). The electronic media, such as discussion groups, offer an opportunity to these peripheral developers to build a knowledge base around the products on which they work.

Prior research has found that WOM has a greater impact on individual judgments attributable to its vividness—i.e., emotionally interesting, concrete, and imagery provoking—and proximity (sensory, temporal, or spatial) (Nisbett and Ross 1980). Virtual wordof-mouth, similar to the face-to-face word-of-mouth, may also have a significant impact on individual decision making (Buttle 1998). Given their familiarity with technology, peripheral developers often use electronic means such as blogs, websites, and discussion groups to enhance the OSS product information. These media create the vividness typical of WOM advocacy. Usually, people trust (similar) others with whom they can talk in the same dialectic, mental models, and belief systems. Peripheral developers, by virtue of being members of the same OSS networks, have similar beliefs, education, and mind set. Hence, they may be ideally suited to have influence on potential adopters through their word-of-mouth actions.

Furthermore, peripheral developers have first-hand knowledge of the merits (or demerits) of these software products. Their deep involvement gives them an advantageous position to evaluate the innovation about its relative advantage, perceived usefulness, and perceived quality. Additionally, electronic means for WOM help answer questions from the prospective users, share details on product queries, and analyze the features and function. Hence, we propose that peripheral members are not only vital information sources in influencing awareness, but also they are important influences for actual adoption of software products through word-of-mouth spread of expert opinions. Therefore, we hypothesis the following.

<sup>Hypothesis</sup> <sup>2B</sup> <sup>(H2B).</sup> Greater degree of participation of peripheral developers in OSS projects will enhance the adoption of the product.

## 2.4. The Effects of Life-Cycle Stages on the Influence of Peripheral Developers

Unlike proprietary software, OSS has uncertainties related to programming consistency, licensing terms, and dynamic developer interests that will influence product diffusion and survival (Bitzer and Schröder 2005, Comino et al. 2007). Because not all OSS products survive to become mature, developers pay greater attention to near product maturity. The continued development of a product gives it legitimacy, reputation, and attracts more contributors from the developer community, especially as it gains maturity. In the case of peripheral developers, who may also be driven by the use value of a product, a mature product sends a stronger signal of a better-developed product.

Maturity signifies that a project has well-developed project-management capabilities. The governance mechanisms to seek inputs, give feedback, and incorporate inputs into the product may be better developed in the mature stages, leading to greater efficiency for peripheral developer contributions. Furthermore, as a product matures, the cumulative knowledge about project code is more widely available. Greater familiarity of peripheral participants with the project code makes their contributions even more efficient. As a net result, peripheral developers are more likely to be attracted toward a mature project where they expect that their contributions will be more efficiently managed. Mature projects also attract the best peripheral developers from the talent pool. According to the expectancy value models (that have been successfully applied to explain participation in open-source projects), contributors evaluate the expectancy of the outcomes and its value to determine the overall motivational impact (Atkinson 1957, Vroom 1964, Hertel et al. 2003). Peripheral developers may find mature projects to be a better stage for their contributions to be effective because these projects have better project management capabilities, enhanced governance mechanisms, and better-developed code. Given these expectations, mature products may attract the best peripheral participants, with greater ability and motivation to contribute to the open-source products. This impact is further accentuated because good peripheral developers attract other users and developers (Bitzer and Schröder 2005). Overall, we hypothesize that the contributions of peripheral participants toward product quality assessment and product quality enhancement would be greater in the mature stages of development. Formally, stated in the following hypotheses.

<sup>Hypothesis</sup> <sup>3A</sup> <sup>(H3A).</sup> The influence of the degree of participation of peripheral developers on product quality assessment is greater in mature stages of OSS product development than in the early (alpha and beta) stages.

<sup>Hypothesis</sup> <sup>3B</sup> <sup>(H3B).</sup> The influence of the degree of participation of peripheral developers on product quality enhancement is greater in mature stages of OSS product development than in the early (alpha and beta) stages.

With time, as the software product gains more recognition, the impact of peripheral developers on product diffusion increases. First, mature products lend more credence to the words of peripheral developers. Second, because of the experience and knowledge gained while working on the software, peripheral participants may be able to more convincingly influence potential adopters about the utility of the product. Furthermore, the experience may also affect their connectivity within the community. Over time, peripheral participants may become critical nodes in the interpersonal network that disseminates knowledge about the product. A stronger reach and reputation will increase their influence on the diffusion outcomes. Thus, we posit this hypothesis.

<sup>Hypothesis</sup> <sup>4A</sup> <sup>(H4A).</sup> The influence of the degree of participation of peripheral developers on product awareness is greater in mature stages of OSS product development than in the early (alpha and beta) stages.

<sup>Hypothesis</sup> <sup>4B</sup> <sup>(H4B).</sup> The influence of the degree of participation of peripheral developers on product adoption is greater in mature stages of OSS product development than in the early (alpha and beta) stages.

## 3. Data and Measures

Data for the research were gathered from sourceforge.net during the period December 2004–March 2005. Similar to prior data collection efforts (e.g.,

Garcia 2004), we used a Web crawler to gather a list of OSS products. We gathered data on product characteristics and development activity for 1,000 randomly selected products. Fifteen software products were dropped due to lack of information or duplication within the set; the effective sample size was 985. For all the software products on this list, we gathered data about developer-contributed lines of code from the concurrent version system (CVS) for each of the developer listed.<sup>4</sup> Many products did not use CVS sample sizes, which further reduced the sample to 431. We also dropped products without development activity and further reduced the usable sample to 320. Tables 1 and 2 show the variable descriptions and statistics, including simple correlation analysis. Furthermore, we conducted interviews with a random sample of 7% of the peripheral developers who were part of the frame for the quantitative analysis.<sup>5</sup> These interviews were used to explore insights from the empirical analysis.

## 3.1. Measures

The degree of participation of peripheral developers (NoOfPerD) is the primary independent variable used in this research, and it is a monthly count of the peripheral developers working on each project. Conceptually, the idea of peripheral developers is easy to comprehend, but operationalizing the conditions that define a peripheral contributor is not straightforward. Crowston et al. (2006) have identified various approaches to identify peripheral developers, of which one is based on contributions. They assert that “the core group is the few members that contribute the most while the others are the periphery (p. 2).” According to Mockus et al. (2000), core developers write around 88% of the code for the product, whereas the rest is written by peripheral developers. In line with this premise, peripheral developers were identified by analyzing the lines of code contribution of all the team members working on the OSS product. For each month, cumulative individual developer contributions to code until that period were computed, and all members having between 0% to 12% percent of the total code contributions were classified as peripheral developers. There were instances when the products had zero peripheral developers and these products were dropped from further analysis. The final sample was comprised of 1966 monthly observations over 147 products (OSS products). The basis for classifying developers as core or peripheral is largely based on the empirical findings of Apache (Mockus et al. 2002). However, to limit concerns about bias due to this classification measure, we also tested our hypotheses with five other cutoffs—8%, 10%, 15%, 18%, and 20% of total code contribution. The results with these cutoffs were found to be similar to the results with 12% percent cutoff reported in this research.

Table 2 Description of Variables Used in the Study

<table><tr><td>Variable</td><td>Description</td></tr><tr><td>OSS product adoption (Downloads—Dwnld)</td><td>Number of downloads for the product in the given period.</td></tr><tr><td>OSS product awareness (Page Views—PagView)</td><td>Number of page views for the product for the period.</td></tr><tr><td>OSS product quality Assessment (Bugs Reported—BugsRep)</td><td>Number of bugs reported for the product in the given period.</td></tr><tr><td>OSS product quality enhancement (BugsFixed—BugsFix):</td><td>Number of bugs fixed for the product for the period.</td></tr><tr><td>Peripheral participation (Peripheral Developers—NoOfPerD)</td><td>Number of peripheral developers for the product for the period.</td></tr><tr><td>Core developers (NoOfCorD)</td><td>Number of core developers on the product for the period.</td></tr><tr><td>Beta (BetIncr)</td><td>Dummy variable that identifies the incremental results for the product as it moves from alpha to beta stage of development.</td></tr><tr><td>Mature (MatIncr)</td><td>Dummy variable that identifies the incremental results for the product as it moves from alpha to mature stage.</td></tr><tr><td colspan="2">Controls</td></tr><tr><td>Size (Size)</td><td>Total lines of code written for the product up to this period.</td></tr><tr><td>Duration (Duration)</td><td>The time since the product was initialized.</td></tr><tr><td>End user focused (EndUser)</td><td>Dummy variable that measures if the product is focused for end users.</td></tr><tr><td>Developer focused (Dvlpr)</td><td>Dummy variable that measures if the product is focused for developers.</td></tr><tr><td>System administrator focused (SysAdmn)</td><td>Dummy variable that measures if the product is focused for system administrators.</td></tr></table>

The number of core developers (NoOfCord) was another variable used in our research. It was measured as the count of developers contributing more than 12% of code to the project. Product Quality of an OSS product is examined as the extent of quality assessment and quality enhancement. These are measured as the number of bugs reported (BugsRep) and bugs fixed (BugsFix), respectively, for each product during the month. Reports of bugs indicate the defects in quality, whereas bugs fixed indicate the enhancement of quality by finding solutions to these bugs.

Open-Source Software Product Diffusion: In a recent study, Crowston et al. (2003) defined various measures of OSS product success, including product awareness and use. In our research, we focus on two aspects of product diffusion—OSS product awareness and OSS product adoption. Analogous to the idea of product success in commercial settings, usually based on the number of customers with an interest in buying the product and actual number of units sold, we examine open-source product awareness and adoption in terms of the number of product page views (PagView) and the number of product downloads (Dwnld). In the OSS literature, these are important measures of system use that in general are important antecedents of individual and overall impacts (DeLone and McLean 1992, Crowston et al. 2003)

Maturity: We collected data on the six-stage Source -forge.net categorization—Planning, Prealpha, Alpha, Beta, Production/stable, or Mature for measuring product development maturity. These categorizations are self-reported by product managers, and the guidelines for product development managers to categorize their products are less than clear (Comino et al. 2007). Thus, we used only three categories to reduce variance due to reporting errors and form exclusive categorization. The first stage includes products in alpha or preceding stages. Because products in the planning and prealpha stage usually have limited code, the categorization is theoretically consistent and removes ambiguity. Lakhani and Wolf (2005) used a similar rationale to remove planning and prealpha products from their analysis. Similarly, the stages of production/stable and mature are combined into the maturity stage. Products in the beta stage are classified without any change from other conceptualizations. The stages were coded using two categorical variables (BetIncr and MatIncr), representing increases in beta and mature stages of development over the base case—alpha stage (Cohen et al. 2003).

Control Variables. We controlled for the duration of the product (Duration), size of the product (Size), and product type based on audience for the product. A dummy code was inserted for the type of the product: end-user focused (EndUser), developer focused (Devlpr), or system administrator focused (SysAdmn). Size of the product was measured as total lines of code for the product.<sup>6</sup> Size varies for each product across months and was controlled for at the periodic level, whereas duration<sup>7</sup> (the time from the inception of the product to the start of data collection) and product type were controlled at the product level (also see Tables 1 and 2).

## 4. Empirical Model

We used the hierarchical linear modeling (HLM) to test the research model because of the nested nature of the research design (Raudenbush and Bryk 2002). Although periodic contributions by a peripheral developer are hypothesized to impact product quality and product diffusion (H1 and H2), we also proposed that these impacts would vary across products. Thus, the periodic-level impacts are nested within the product-level impacts, i.e., relationships observed in monthly observations may vary across product. HLM helps to statistically analyze the information across levels and is more robust for the analysis of multilevel data. The failure to incorporate information across levels may lead to aggregation bias, misestimated precision, and the “unit of analysis” problem (Raudenbush and Bryk 2002).

Our HLM analysis adopted an incremental modelbuilding approach to analyze multilevel data, similar to the approach adopted by Ang et al. (2002). Thus, our first model (Model 1) is a null model, and it is a simple one-way ANOVA with random effects, but without any predictors at the periodic or product level. Model 1 assesses variability in diffusion and quality at each level and is a prerequisite for the detailed multilevel analysis. After estimating Model 1, we included the predictors and control variables to test the hypothesized main effects in Model 2. This model identifies the direct impact of the predictors—peripheral developers, core developers, and product stage variables—on quality development and diffusion of open source software products. Finally, Model 3 tests the cross-level effects at the periodic and product levels. These cross-level effects help us to assess the differential impact of peripheral developers on product diffusion and quality development across different stages of the product development.

We centered our raw variables before the analysis (e.g., Ang et al. 2002). The periodic-level variables were centered at the group level, and the coefficients represent change with respect to the group mean. Centering leads to a decrease in multicollinearity, increases the robustness of results, and enhances the quality and interpretation of the HLM results. Similarly, our product-level coefficients are centered on the grand mean of the variable. Product-level variables are dichotomous, and the coefficients represent the mean impact for these after adjusting for the proportion of total software products in that category (Bryk and Raudenbush 1992).

In HLM, we utilized the full maximum-likelihood procedure to test our model (Raudenbush and Bryk 2002, Ang et al. 2002). Our model specification is based on the fixed effects for the level 1 coefficient with random intercept. Thus, we incorporated the measurement error in the intercept term while modeling all other level 1 coefficients as fixed. This random coefficient fixed-slope specification helps us to assume the level 1 coefficient to be nonstochastic and aids computational stability of the model.<sup>8</sup> The model specifications for OSS product quality development and diffusion are presented in the following sections.

## 4.1. OSS Product Quality

Incremental models were analyzed to assess the impact of peripheral developers on the quality of OSS products. Both aspects of quality were tested using the incremental Models 1–3:

Model 1A (One-way ANOVA with Random Effects),

$$
\begin{array}{l} \text {Quality} _ {i j} = \beta_ {0 j} + r, \\ \beta_ {0 j} = \gamma_ {0 0} + u _ {0}, \end{array}
$$

Main Effects Model (Model 2A)

$$
\begin{array}{r l} & {\mathrm{Size} _ {i j} = \beta_ {0 j} + \beta_ {1 j} * (S I Z E) + \beta_ {2 j} * (N o O f P e r D)} \\ & {\qquad + \beta_ {3 j} * (N o O f C o r D) + r,} \\ & {\beta_ {0 j} = \gamma_ {0 0} + \gamma_ {0 1} * (B e t I n c r) + \gamma_ {0 2} * (M a t I n c r)} \\ & {\qquad + \gamma_ {0 3} * (E n d U s e r) + \gamma_ {0 4} * (D e v l p r)} \\ & {\qquad + \gamma_ {0 5} * (S y s A d m n) + \gamma_ {0 6} * (D u r a t i o n) + u _ {0},} \end{array}
$$

$$
\beta_ {1 j} = \gamma_ {1 0}; \quad \beta_ {2 j} = \gamma_ {2 0}; \quad \beta_ {3 j} = \gamma_ {3 0}.
$$

Cross-Level Effects Model (Model 3A)

$$
\begin{array}{c} \text {Size} _ {i j} = \beta_ {0 j} + \beta_ {1 j} * (S I Z E) + \beta_ {2 j} * (N o O f P e r D) \\ + \beta_ {3 j} * (N o O f C o r D) + r, \end{array}
$$

$$
\begin{array}{r l} \beta_ {0 j} = & \gamma_ {0 0} + \gamma_ {0 1} * (B e t I n c r) + \gamma_ {0 2} * (M a t I n c r) \\ & + \gamma_ {0 3} * (E n d U s e r) + \gamma_ {0 4} * (D e v l p r) \\ & + \gamma_ {0 5} * (S y s A d m n) + \gamma_ {0 6} * (D u r a t i o n) + u _ {0}, \end{array}
$$

$$
\begin{array}{l} \beta_ {1 j} = \gamma_ {1 0}, \\ \beta_ {2 j} = \gamma_ {2 0} + \gamma_ {2 1} * (B e t I n c r) + \gamma_ {2 2} * (M a t I n c r) \\ \qquad + \gamma_ {2 3} * (E n d U s e r) + \gamma_ {2 4} * (D e v l p r) \\ \qquad + \gamma_ {2 5} * (S y s A d m n) + \gamma_ {2 6} * (D u r a t i o n), \\ \beta_ {3 j} = \gamma_ {3 0}. \end{array}
$$

Quality assessment and enhancement were measured as bugs reported (BugsRep) and bugs fixed (BugsFix), respectively. The periodic observations are represented as $i ,$ with ranges from 1 to 1,966, and j represents the software product, with ranges from 1 to 147. The $\gamma _ { p q }$ represents the impacts of the productlevel variable $q$ (maturity, duration, or product type) on the corresponding $\beta _ { p j }$ that measures the effect of level 1 variable—p (size, number of peripheral developers, or number of core developers) on quality.

4.2. Open-Source Software Product Diffusion The following models were fitted for the diffusion measures of the dependent variable (namely, page views and downloads).

Model 1S (One-way ANOVA with Random Effects)

Diffusio $\begin{array} { r } { \mathfrak { r } _ { i j } = \beta _ { 0 j } + r , } \end{array}$

$$
\beta_ {0 j} = \gamma_ {0 0} + u _ {0}
$$

Main Effects Model (Model 2S)

$$
\begin{array}{c} \text {Size} _ {i j} = \beta_ {0 j} + \beta_ {1 j} * (S I Z E) + \beta_ {2 j} * (N o O f P e r d) \\ + \beta_ {3 j} * (N o O f C o r d) + r, \end{array}
$$

$$
\begin{array}{r l} \beta_ {0 j} = & \gamma_ {0 0} + \gamma_ {0 1} * (B e t I n c r) + \gamma_ {0 2} * (M a t I n c) \\ & + \gamma_ {0 3} * (E n d U s e r) + \gamma_ {0 4} * (D e v l p r) \\ & + \gamma_ {0 5} * (S y s A d m i n) + \gamma_ {0 6} * (D u r a t i o n) + u _ {0}, \end{array}
$$

$$
\beta_ {1 j} = \gamma_ {1 0}, \quad \beta_ {2 j} = \gamma_ {2 0}, \quad \beta_ {3 j} = \gamma_ {3 0}.
$$

Cross-Level Effects Model (Model 3S)

$$
\begin{array}{c} \mathrm{Size} _ {i j} = \beta_ {0 j} + \beta_ {1 j} * (S I Z E) + \beta_ {2 j} * (N o O f P e r d) \\ + \beta_ {3 j} * (N o O f C o r d) + r, \end{array}
$$

$$
\begin{array}{r l} & {\beta_ {0 j} = \gamma_ {0 0} + \gamma_ {0 1} * (B e t I n c r) + \gamma_ {0 2} * (M a t I n c)} \\ & {\qquad + \gamma_ {0 3} * (E n d U s e r) + \gamma_ {0 4} * (D e v l p r)} \\ & {\qquad + \gamma_ {0 5} * (S y s A d m n) + \gamma_ {0 6} * (D u r a t i o n) + u _ {0},} \end{array}
$$

$$
\beta_ {1 j} = \gamma_ {1 0},
$$

$$
\begin{array}{c} \beta_ {2 j} = \gamma_ {2 0} + \gamma_ {2 1} * (B e t I n c r) + \gamma_ {2 2} * (M a t I n c r) \\ \qquad + \gamma_ {2 3} * (E n d U s e r) + \gamma_ {2 4} * (D e v l p r) \\ \qquad + \gamma_ {2 5} * (S y s A d m n) + \gamma_ {2 6} * (D u r a t i o n), \end{array}
$$

$$
\beta_ {3 j} = \gamma_ {3 0}.
$$

Diffusion represents either downloads (Dwnld) or page views (PagView), i represents the periodic observation and ranges from 1 to 1,966, and j represents the products and ranges from 1 to 147. The $\gamma _ { p q }$ is the impact of the product-level variable q (stage, duration, or product type) on the corresponding $\beta _ { p j }$ that measures the effect of level 1 variable p (size, number of peripheral developers, or number of core developers) on product diffusion.

## 5. Results

## 5.1. Model Statistics and Comparisons

As specified in §4.1, Models 1A and 1S help analyze the variance in the dependent variable (quality development and diffusion) across levels and compare the variance explained by the introduction of independent variables in the Models 2A, 2S and 3A, 3S. The intraclass correlation coefficient $( \mathrm { I C C } ) ^ { 9 }$ for Model 1A and 1S helps assess relative variation in the dependent variables (quality development and diffusion of open source software products) across the periodic and product levels (Raudenbush and Bryk 2002). The ICC indicates that a significant proportion of variance in the outcomes is at the product level (40.10% for downloads, 42.92% for page views, 32.69% for bugs reported, and 34.77% for bugs fixed), with remaining variance in these outcomes at the periodic level. Although this confirms the underlying multilevel structure, ICC also acts as a basis for comparison of the proportional reduction in variance across the two levels. The residual variance in Models 2A, 2S, and 3A, 3S is compared to the corresponding residual variance in the null model.<sup>10</sup> For each of the four outcome variables, there is a positive reduction in the variance in outcomes due to the introduction of independent variables, as compared with the level 1 variance in the Model 1. The hypothesis testing for specific impacts of these independent variables was done in Models 2A, 2S, and 3A, 3S. Finally, the models are compared using the deviance statis-$\mathrm { t i c } , ^ { 1 1 }$ and the deviation differences are tested using a variance covariance comparison test (see Tables 3–6). For downloads, page views, and bugs reported, the model fit improves as more predictors are added. However, for bugs fixed, predictors explain incremental variance for the main effects model (Model 2) but not for the cross-level model (Model 3). The hypotheses are formally tested in Models 2A, 2S, and 3A, 3S.

<sub>ptive</sub> S<sup>tatistics</sup> <sup>and</sup> <sup>Correl</sup> <sub>a</sub>b<sup>le</sup>

<table><tr><td></td><td>Mean (s.d.) $^{a}$ </td><td>Mean (s.d.) $^{b}$ </td><td>Alpha</td><td>Beta</td><td>Mature</td><td>EndUsr</td><td>Dvlpr</td><td>SysAdmn</td><td>Duration</td><td>PagView</td><td>Dwnld</td><td>BugsRep</td><td>BugsFix</td><td>Size</td><td>NoOfPerD</td><td>NoOfCorD</td></tr><tr><td>Alpha</td><td>0.44 (0.5)</td><td></td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Beta</td><td>0.38 (0.49)</td><td></td><td>-0.657***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Mature</td><td>0.18 (0.38)</td><td></td><td>-0.325***</td><td>-0.499***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EndUsr</td><td>0.48 (0.5)</td><td></td><td>0.019</td><td>-0.104***</td><td>0.108***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dvlpr</td><td>0.71 (0.46)</td><td></td><td>0.098***</td><td>-0.128***</td><td>0.047**</td><td>-0.187***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SysAdmn</td><td>0.17 (0.38)</td><td></td><td>-0.028</td><td>-0.234***</td><td>0.326***</td><td>0.043*</td><td>-0.118***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Duration</td><td>36.26 (12.58)</td><td></td><td>0.09***</td><td>-0.15***</td><td>0.085***</td><td>0.23***</td><td>0.019</td><td>0.099***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>PagView</td><td>6,849.16(30,542.4)</td><td>4,763.15(18,084.33)</td><td>-0.243***</td><td>0.075***</td><td>0.186***</td><td>0.115***</td><td>0.066***</td><td>0.02</td><td>-0.115***</td><td>1</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dwnld</td><td>3,601.52(19,054.26)</td><td>2,133.25(10,485)</td><td>-0.237***</td><td>0.06***</td><td>0.198***</td><td>0.176***</td><td>-0.03</td><td>0.068***</td><td>0.084***</td><td>0.53***</td><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>BugsRep</td><td>2.27 (9.66)</td><td>2.3 (5.98)</td><td>-0.092***</td><td>-0.04*</td><td>0.157***</td><td>0.13***</td><td>0.052**</td><td>-0.073***</td><td>-0.097***</td><td>0.375***</td><td>0.526***</td><td>1</td><td></td><td></td><td></td><td></td></tr><tr><td>BugsFix</td><td>1.48 (5.24)</td><td>0.91 (2.80)</td><td>-0.280***</td><td>0.176**</td><td>0.140*</td><td>0.063</td><td>-0.055</td><td>0.046</td><td>0.57</td><td>0.106***</td><td>0.167***</td><td>0.171***</td><td>1</td><td></td><td></td><td></td></tr><tr><td>Size $^c$ </td><td>331,095.33(1,846,701.63)</td><td>208,047.97(1,481,553.33)</td><td>-0.224***</td><td>0.023</td><td>0.229***</td><td>0.17***</td><td>-0.074***</td><td>0.015</td><td>0.05**</td><td>0.001</td><td>0.01</td><td>0.004</td><td>-0.011</td><td>1</td><td></td><td></td></tr><tr><td>NoOfPerD</td><td>2.81 (3.07)</td><td>2.11 (2.01)</td><td>-0.02</td><td>0.139***</td><td>-0.15***</td><td>0.053**</td><td>-0.02</td><td>-0.02</td><td>-0.156***</td><td>0.278***</td><td>0.417***</td><td>0.306***</td><td>0.180***</td><td>-0.01</td><td>1</td><td></td></tr><tr><td>NoOfCorD</td><td>1.58 (0.78)</td><td>1.38 (0.63)</td><td>-0.066***</td><td>0.07***</td><td>-0.01</td><td>-0.041*</td><td>0.082***</td><td>-0.093***</td><td>-0.02</td><td>0.068***</td><td>0.071***</td><td>0.054**</td><td>0.105***</td><td>-0.073***</td><td>0.367***</td><td>1</td></tr></table>

<sub>es</sub> m<sup>easured</sup> <sup>at</sup> <sup>the</sup> <sup>produc</sup>  
<sub>d</sub>i<sub>an</sub> <sub>s</sub>i<sub>ze</sub> <sub>of</sub> <sub>the</sub> <sub>p</sub>r<sup>oject</sup> i<sup>s</sup> <sup>27</sup>,<sup>8</sup> <sub>ce</sub> <sub>of</sub> <sub>coeffic</sub>i<sub>ents</sub> i<sub>s</sub> <sub>eva</sub>l<sub>uated</sub> <sub>as</sub> <sub>∗p</sub> <sub><0</sub>0<sub>10</sub>, <sup>∗∗p</sup> <sup><0</sup>0<sup>05</sup>

Table 4 Results of HLM Estimation (OSS Product Quality Assessment)

<table><tr><td rowspan="2">Variable (coefficient)</td><td colspan="3">Bugs reported</td></tr><tr><td>Model 1A</td><td>Model 2A</td><td>Model 3A</td></tr><tr><td>INTERCPT ( $\gamma_{00}$ )</td><td>1.61*** (0.49)</td><td></td><td></td></tr><tr><td>Size ( $\gamma_{11}$ )</td><td></td><td>0.01 (0.01)</td><td>-0.01 (0.01)</td></tr><tr><td>Peripheral developers ( $\gamma_{20}$ )</td><td></td><td>0.70*** (0.10)</td><td></td></tr><tr><td>Core developers ( $\gamma_{30}$ )</td><td></td><td>-2.29*** (0.43)</td><td>-1.1** (0.45)</td></tr><tr><td>Alpha ( $\gamma_{00}$ )</td><td></td><td>1.67*** (0.46)</td><td>1.65*** (0.45)</td></tr><tr><td>Beta ( $\gamma_{01}$ )</td><td></td><td>0.03 (1.01)</td><td>0.03 (0.99)</td></tr><tr><td>Mature ( $\gamma_{02}$ )</td><td></td><td>4.29*** (1.32)</td><td>4.24*** (1.30)</td></tr><tr><td>End user focused ( $\gamma_{03}$ )</td><td></td><td>2.18** (0.98)</td><td>2.14** (0.97)</td></tr><tr><td>Developer focused ( $\gamma_{04}$ )</td><td></td><td>1.32 (1.04)</td><td>1.30 (1.02)</td></tr><tr><td>System administrator focused ( $\gamma_{05}$ )</td><td></td><td>-0.43 (1.19)</td><td>-0.41 (1.18)</td></tr><tr><td>Duration ( $\gamma_{06}$ )</td><td></td><td>-0.09** (0.04)</td><td>-0.09** (0.04)</td></tr><tr><td>Peripheral dev * Alpha ( $\gamma_{20}$ )</td><td></td><td></td><td>0.72*** (0.17)</td></tr><tr><td>Peripheral dev * Beta ( $\gamma_{21}$ )</td><td></td><td></td><td>0.74* (0.38)</td></tr><tr><td>Peripheral dev * Mature ( $\gamma_{22}$ )</td><td></td><td></td><td>3.43*** (0.47)</td></tr><tr><td>Peripheral dev * End User Focused ( $\gamma_{23}$ )</td><td></td><td></td><td>-1.69*** (0.33)</td></tr><tr><td>Peripheral dev * Developer Focused ( $\gamma_{24}$ )</td><td></td><td></td><td>-0.23 (0.32)</td></tr><tr><td>Peripheral dev * System Administrator Focused ( $\gamma_{25}$ )</td><td></td><td></td><td>-1.53*** (0.23)</td></tr><tr><td>Peripheral dev * Duration ( $\gamma_{26}$ )</td><td></td><td></td><td>0.11*** (0.02)</td></tr><tr><td>Deviance (-2 log likelihood)</td><td>13,596.57</td><td>13,495.10</td><td>13,302.09</td></tr><tr><td>Deviation difference (Δ Dev)</td><td></td><td>100.26***</td><td>193.82***</td></tr></table>

Notes. There are 1,966 observations at the periodic level that correspond with 147 products at level 2. The standard errors are reported in the parenthesis below the beta coefficients. The dependent variable is bugs reported, and independent variables and controls are shown in the first column. The dummy coding scheme implies that the statistics for beta and mature stages reflect the increments over the alpha stage, which acts as the base case in the analysis (Cohen et al. 2003). Deviation differences are calculated as the difference between the current model and the previous model, i.e., ã D3A = D3A−D2A and ã D2A = D2A−D1A. Significance of difference is tested after accounting for the estimated parameters in the two models.  
Significance levels: $^ { * } p < 0 . 1 0$ level, $^ { * * } p < 0 . 0 5$ level, $^ { * * * } p < 0 . 0 1$ level.

Table 5 Results of HLM Estimation (OSS Product Quality Enhancement)

<table><tr><td rowspan="2">Variable (coefficient)</td><td colspan="3">Bugs fixed</td></tr><tr><td>Model 1A</td><td>Model 2A</td><td>Model 3A</td></tr><tr><td>INTERCPT ( $\gamma_{00}$ )</td><td>1.08***(0.28)</td><td></td><td></td></tr><tr><td>Size ( $\gamma_{11}$ )</td><td></td><td>-0.01**(0.01)</td><td>-0.01***(0.01)</td></tr><tr><td>Peripheral developers ( $\gamma_{20}$ )</td><td></td><td>0.11*(0.06)</td><td></td></tr><tr><td>Core developers ( $\gamma_{30}$ )</td><td></td><td>-0.14(0.25)</td><td>0.09(0.27)</td></tr><tr><td>Alpha ( $\gamma_{00}$ )</td><td></td><td>1.13***(0.26)</td><td>1.13***(0.26)</td></tr><tr><td>Beta ( $\gamma_{01}$ )</td><td></td><td>-0.01(0.05)</td><td>-0.01(0.57)</td></tr><tr><td>Mature ( $\gamma_{02}$ )</td><td></td><td>2.34***(0.75)</td><td>2.34***(0.75)</td></tr><tr><td>End user focused ( $\gamma_{03}$ )</td><td></td><td>1.08*(0.55)</td><td>1.07*(0.55)</td></tr><tr><td>Developer focused ( $\gamma_{04}$ )</td><td></td><td>0.81(0.58)</td><td>0.81(0.58)</td></tr><tr><td>System administrator focused ( $\gamma_{05}$ )</td><td></td><td>-0.12(0.67)</td><td>-0.12(0.67)</td></tr><tr><td>Duration ( $\gamma_{06}$ )</td><td></td><td>-0.05(0.02)</td><td>-0.05***(0.02)</td></tr><tr><td>Peripheral dev * Alpha ( $\gamma_{20}$ )</td><td></td><td></td><td>0.16(0.10)</td></tr><tr><td>Peripheral dev * Beta ( $\gamma_{21}$ )</td><td></td><td></td><td>-0.07(0.23)</td></tr><tr><td>Peripheral dev * Mature ( $\gamma_{22}$ )</td><td></td><td></td><td>-0.37(0.28)</td></tr><tr><td>Peripheral dev * End User Focused ( $\gamma_{23}$ )</td><td></td><td></td><td>0.32(0.20)</td></tr><tr><td>Peripheral dev * Developer Focused ( $\gamma_{24}$ )</td><td></td><td></td><td>0.24(0.19)</td></tr><tr><td>Peripheral dev * System Administrator Focused ( $\gamma_{25}$ )</td><td></td><td></td><td>-0.13(0.14)</td></tr><tr><td>Peripheral dev * Duration ( $\gamma_{26}$ )</td><td></td><td></td><td>0.01(0.01)</td></tr><tr><td>Deviance (-2 log likelihood)</td><td>11,213.95</td><td>11,188.73</td><td>11,180.57</td></tr><tr><td>Deviation difference (Δ Dev)</td><td></td><td>25.22***</td><td>8.16</td></tr></table>

Notes. There are 1,966 observations at the periodic level that correspond with 147 products at level 2. The standard errors are reported in the parenthesis below the beta coefficients. The dependent variable is bugs fixed, and independent variables and controls are shown in the first column. The dummy coding scheme implies that the statistics for beta and mature stages reflect the increments over the alpha stage, which acts as the base case in the analysis (Cohen et al. 2003). Deviation differences are calculated as the difference between the current model and the previous model, i.e., $\Delta \mathsf { D 3 A } = \mathsf { D 3 A } - \mathsf { D 2 A }$ and $\Delta \mathsf { D } 2 \mathsf { A } = \mathsf { D } 2 \mathsf { A } - \mathsf { D } 1 \mathsf { A } .$ Significance of difference is tested after accounting for the estimated parameters in the two models.  
Significance levels: $^ { * } p < 0 . 1 0$ level, $^ { * * } p < 0 . 0 5$ level, $^ { * * * } p < 0 . 0 1$ level.

## 5.2. Peripheral Developers’ Influence on Product Quality Assessment and Enhancement

Hypotheses 1A and 1B propose that greater number of peripheral developers significantly increase the quality assessment and enhancement efforts, in comparison with the contributions of core developers. Model 2A tests these hypotheses. The results in Tables 3 and 4 show that the peripheral developers have a positive impact on quality assessment, i.e., reporting of bugs $( \bar { \gamma } _ { 2 0 } = 0 . 7 0 , \ \bar { p } < \bar { 0 } . 0 1 )$ . Interestingly, the impact of a greater number of core developers on bugs reported is negative $( \gamma _ { 3 0 } = - 2 . 2 9 , p < 0 . 0 1 )$ . Statistical tests comparing the coefficients representing the effects of peripheral and core developers reveal that peripheral developers have a greater impact on quality assessment $( p < 0 . 0 1 )$ . For quality enhancement (bugs fixed), the impacts of peripheral developers are weakly significant $( \gamma _ { 2 0 } = 0 . 1 1 , ~ p < 0 . 1 0 )$ whereas the impacts of core developers are not significant. We elaborate more on these findings in the discussion section.

In addition, H3A and H3B propose that the effects of peripheral developers on OSS product quality improvement efforts should vary across the stages of the projects. Therefore, we test these hypotheses through an analysis of cross-level effects (Model 3A). We find that the number of peripheral developers at the alpha stage has a significant impact on product quality assessment (bugs reported) $( \gamma _ { 2 0 } = 0 . 7 2 ;$ $p < 0 . 0 1 )$ , but not on product quality enhancement (bugs fixed) $( \gamma _ { 2 0 } = 0 . 1 6 ; \mathrm { n . s . } )$ . At the beta stage, the incremental impact of peripheral developers is not significant for OSS product quality enhancement or quality assessment. Finally, at the mature stage, the impact of the number of peripheral developers on quality assessment (bugs reported) increases significantly $( \gamma _ { 2 2 } = 3 . 4 3 ; p < 0 . 0 1 )$ , but the incremental effect is not significant for product quality enhancement (see Figure 2). Overall, these cross-level effects show support for H3A (effects on product quality assessment), but not for H3B (effects on product quality enhancement).

## 5.3. Peripheral Developer Influence on Open-Source Product Diffusion

Hypotheses 2A and 2B state that the number of peripheral developers impacts product diffusion. Model 2S describes our approach to the testing of these hypotheses. The impacts of the number of peripheral developers on both of these dimensions of product diffusion, OSS product adoption $( \gamma _ { 2 0 } = 2 0 0 1 . 9 1 , p < 0 . 0 1 )$ ) and OSS product awareness $( \gamma _ { 2 0 } = 2 1 5 9 . 5 , p < 0 . 0 1 )$ , were found to be significant (see Tables 6 and 7).

Hypotheses 4A and 4B propose that the stages will have a significant effect on the relationship between the number of peripheral developers and product diffusion outcomes. We test these hypotheses through the cross-level effects model (Model 3S). This model suggests that the number of peripheral developers has a positive impact on product downloads and page views during the alpha development stage. In the beta stage, the impact of peripheral developer contribution shows no change in either downloads or page views. However, as hypothesized in H4A, the impact of the number of peripheral developers is greater on page views in the mature development stages than in the alpha stage $( \gamma _ { 2 0 } = 1 , 5 3 8 . 0 1 ; p < 0 . 0 1 _ { \cdot }$ $\gamma _ { 2 2 } = 6 , 6 1 3 . 7 9 ; \ p < 0 . 0 1 )$ . This result is identical for downloads, thereby supporting H4B $( \gamma _ { 2 0 } = 1 , 3 8 0 . 6 6 ;$ $p < 0 . 0 1 , \ \gamma _ { 2 2 } = 7 , 1 5 1 . 0 7 ; \ p < 0 . 0 1 )$ . Thus, in Figure 2, greater slopes in the mature stages (than in the alpha and beta stages) for both the download and page views suggest that peripheral developers have greater impacts on OSS product adoption in the mature stages. Both H4A and H4B are thus supported.

## 5.4. Robustness Analysis

We performed several other tests to check for the robustness of our results. First, we examined whether our choice of 12% of code contribution to classify developers as peripheral might influence the results. In order to verify that there is no bias in the results due to the choice of percentage contribution attributed to peripheral developers, the hypotheses were retested for five other cutoffs—8%, 10%, 15%, 18%, 20%. The results did not change with the use of each additional cutoff. These model runs strongly suggest that within the given range, our results are robust to the choice of cutoff percentage point. Next, we also controlled for the rank of the project in assessing the impact of peripheral participants on product success, and found no change in results. The popularity of the OSS product did not affect our results. Furthermore, to test for the impacts of distributional assumptions, we identified extreme outliers for all of the dependent variables and repeated the analyses. All of the results were found to be unchanged. Ang et al. (2002) suggest that the robust standard errors can be used to test the relationships and to determine if the results are robust to the violation of any HLM assumptions such as normality and homoscedasticity. In our retests, the use of robust standard errors supports our earlier results and confirms our findings. Additionally, in another analysis that considers the time series pattern of data, results are also found to be robust against the violation of serial correlation. Finally, to examine if product quality, and not peripheral developers, might be the factor increasing the diffusion outcome, we examined the influence of peripheral developers on diffusion, after controlling for quality outcomes.<sup>12</sup> We did not find a qualitative difference in the results.

Table 6 Results of HLM Estimation (OSS Product Adoption)

<table><tr><td rowspan="2">Variable (coefficient)</td><td colspan="4">Downloads</td></tr><tr><td>Model 1S</td><td>Model 2S</td><td colspan="2">Model 3S</td></tr><tr><td>INTERCPT ( $\gamma_{00}$ )</td><td>2,246.35*** (979.79)</td><td></td><td></td><td></td></tr><tr><td>Size ( $\gamma_{11}$ )</td><td></td><td>0.01*** (0.01)</td><td>0.01</td><td>(0.01)</td></tr><tr><td>Peripheral developers ( $\gamma_{20}$ )</td><td></td><td>2,001.91*** (168.94)</td><td></td><td></td></tr><tr><td>Core developers ( $\gamma_{30}$ )</td><td></td><td>-1,321.51* (730.52)</td><td>2,249.90***</td><td>(653.52)</td></tr><tr><td>Alpha ( $\gamma_{00}$ )</td><td></td><td>2,234.85** (954.60)</td><td>2,173.86**</td><td>(922.12)</td></tr><tr><td>Beta ( $\gamma_{01}$ )</td><td></td><td>1,685.77 (2114.39)</td><td>1,682.83*</td><td>(2,045.14)</td></tr><tr><td>Mature ( $\gamma_{02}$ )</td><td></td><td>5,152.63* (2,760.43)</td><td>4,895.02*</td><td>(2,665.54)</td></tr><tr><td>End user focused ( $\gamma_{03}$ )</td><td></td><td>3,701.26* (2,065.09)</td><td>3,558.53</td><td>(2,001.8)</td></tr><tr><td>Developer focused ( $\gamma_{04}$ )</td><td></td><td>-816.21 (2,172.19)</td><td>-850.53</td><td>(2,101.11)</td></tr><tr><td>System administrator focused ( $\gamma_{05}$ )</td><td></td><td>-2,288.94 (2,520.57)</td><td>-2,171.17</td><td>(2,450.82)</td></tr><tr><td>Duration ( $\gamma_{06}$ )</td><td></td><td>-67.14 (78.55)</td><td>-63.35</td><td>(76.28)</td></tr><tr><td>Peripheral dev * Alpha ( $\gamma_{20}$ )</td><td></td><td></td><td>1,380.66***</td><td>(250.13)</td></tr><tr><td>Peripheral dev * Beta ( $\gamma_{21}$ )</td><td></td><td></td><td>-847.09</td><td>(557.10)</td></tr><tr><td>Peripheral dev * Mature ( $\gamma_{22}$ )</td><td></td><td></td><td>7,151.07***</td><td>(680.43)</td></tr><tr><td>Peripheral dev * End User Focused ( $\gamma_{23}$ )</td><td></td><td></td><td>-1,076.19**</td><td>(477.79)</td></tr><tr><td>Peripheral dev * Developer Focused ( $\gamma_{24}$ )</td><td></td><td></td><td>1,729.42***</td><td>(463.86)</td></tr><tr><td>Peripheral dev * System Administrator Focused ( $\gamma_{25}$ )</td><td></td><td></td><td>-903.25***</td><td>(334.81)</td></tr><tr><td>Peripheral dev * Duration ( $\gamma_{26}$ )</td><td></td><td></td><td>63.14***</td><td>(23.18)</td></tr><tr><td>Deviance (-2 log likelihood)</td><td>43,016.28</td><td>42,605.89</td><td colspan="2">41,779.91</td></tr><tr><td>Deviation difference (Δ Dev)</td><td></td><td>2,434.33***</td><td colspan="2">825.98***</td></tr></table>

Notes. There are 1,966 observations at the periodic level that correspond with 147 products at level 2. The standard errors are reported in the parenthesis below the beta coefficients. The dependent variable is Downloads, and independent variables and controls are shown in the first column. The dummy coding scheme implies that the statistics for beta and mature stages reflect the increments over the alpha stage, which acts as the base case in the analysis (Cohen et al. 2003). Deviation differences are calculated as the difference between the current model and the previous model, i.e., ã D3S = D3S−D2S and ã D2S = D2S−D1S. Significance of difference is tested after accounting for the estimated parameters in the two models.  
Significance levels: $^ { * } p < 0 . 1 0$ level, $^ { * * } p < 0 . 0 5$ level, $^ { * * * } p < 0 . 0 1$ level.

Table 7 Results of HLM Estimation (OSS Product Awareness)

<table><tr><td rowspan="2">Variable (coefficient)</td><td colspan="4">Page views</td></tr><tr><td>Model 1S</td><td>Model 2S</td><td colspan="2">Model 3S</td></tr><tr><td>INTERCPT ( $\gamma_{00}$ )</td><td>2,246.35** (976.38)</td><td></td><td></td><td></td></tr><tr><td>Size ( $\gamma_{11}$ )</td><td></td><td>0.01*** (0.01)</td><td>0.01</td><td>(0.01)</td></tr><tr><td>Peripheral developers ( $\gamma_{20}$ )</td><td></td><td>2,159.5*** (295.45)</td><td></td><td></td></tr><tr><td>Core developers ( $\gamma_{30}$ )</td><td></td><td>-1,453.41 (1,277.6)</td><td>1,421.34</td><td>(1,343.5)</td></tr><tr><td>Alpha ( $\gamma_{00}$ )</td><td></td><td>5,224.14*** (1,638.66)</td><td>5,195.38***</td><td>(1,627.26)</td></tr><tr><td>Beta ( $\gamma_{01}$ )</td><td></td><td>2,403.55 (3,628.99)</td><td>2,415.68</td><td>(3,604.77)</td></tr><tr><td>Mature ( $\gamma_{02}$ )</td><td></td><td>12,807.21*** (4,738.75)</td><td>12,706.72***</td><td>(4,705.48)</td></tr><tr><td>End user focused ( $\gamma_{03}$ )</td><td></td><td>7,120.86** (3,543.29)</td><td>7,060.5**</td><td>(3,521.51)</td></tr><tr><td>Developer focused ( $\gamma_{04}$ )</td><td></td><td>3,502.98 (3,728.13)</td><td>3,452.63</td><td>(3,703.34)</td></tr><tr><td>System administrator focused ( $\gamma_{05}$ )</td><td></td><td>2,216.54 (4,323.17)</td><td>2,241.63</td><td>(4,299.44)</td></tr><tr><td>Duration ( $\gamma_{06}$ )</td><td></td><td>-294.09** (134.74)</td><td>-291.94**</td><td>(133.97)</td></tr><tr><td>Peripheral dev * Alpha ( $\gamma_{20}$ )</td><td></td><td></td><td>1,538.01***</td><td>(514.21)</td></tr><tr><td>Peripheral dev * Beta ( $\gamma_{21}$ )</td><td></td><td></td><td>213.29</td><td>(1,145.29)</td></tr><tr><td>Peripheral dev * Mature ( $\gamma_{22}$ )</td><td></td><td></td><td>6,613.79***</td><td>(1,398.82)</td></tr><tr><td>Peripheral dev * End User Focused ( $\gamma_{23}$ )</td><td></td><td></td><td>253.05</td><td>(982.24)</td></tr><tr><td>Peripheral dev * Developer Focused ( $\gamma_{24}$ )</td><td></td><td></td><td>-274.55</td><td>(953.61)</td></tr><tr><td>Peripheral dev * System Administrator Focused ( $\gamma_{25}$ )</td><td></td><td></td><td>-453.9</td><td>(688.3)</td></tr><tr><td>Peripheral dev * Duration ( $\gamma_{26}$ )</td><td></td><td></td><td>44.49</td><td>(47.66)</td></tr><tr><td>Deviance (-2 log likelihood)</td><td>45,040.22</td><td>44,787.64</td><td colspan="2">44,549.28</td></tr><tr><td>Deviation difference (Δ Dev)</td><td></td><td>252.58***</td><td colspan="2">238.37***</td></tr></table>

Notes. There are 1,966 observations at the periodic level that correspond with 147 products at level 2. The standard errors are reported in the parenthesis below the beta coefficients. The dependent variable is page views, and independent variables and controls are shown in the first column. The dummy coding scheme implies that the statistics for beta and mature stages reflect the increments over the alpha stage, which acts as the base case in the analysis (Cohen et al. 2003). Deviation differences are calculated as the difference between the current model and the previous model i.e., ã D3S = D3S − D2S and ã D2S = D2S−D1S. Significance of difference is tested after accounting for the estimated parameters in the two models  
Significance levels: $^ { * } p < 0 . 1 0$ level, $^ { * * } p < 0 . 0 5$ level, $^ { * * * } p < 0 . 0 1$ level.

## 6. Discussion

With the growing popularity of OSS development, there is a growing interest in this paradigm. One of the unique and important, but underexplored, elements of the OSS development approach is the role of peripheral developers. Because peripheral developers volunteer their time and talent to the OSS project out of their desire to enhance their own utility or be affiliated with a community, their motivations and contributions to the project may be different from those of core developers. Thus, it is important to understand if, and how, open-source projects also benefit from the participation of peripheral developers. Without clear evidence of how peripheral developers might benefit open-source projects, it would be difficult to advocate concerted efforts to attract and leverage such developer’s contributions toward open-source projects.

Our research examines the contributions of peripheral developers and how they vary across the product life cycle of OSS projects. We differentiate between the product quality and diffusion outcomes on the basis of the level of engagement required from developers. We examine their contributions to two aspects of OSS product quality, namely, assessment and enhancement; and two product diffusion outcomes, viz. awareness and adoption. Table 8 presents a summary of the hypotheses and the results of our empirical analysis. Our analyses suggest three important findings about the influence of peripheral developers: (a) they contribute to product quality assessment in a more significant way than core developers; (b) they significantly influence product diffusion by increasing awareness and actual adoption of OSS products; and, (c) their influence on product quality and product diffusion varies across the product life-cycle stages. We discuss each of these findings, along with their theoretical and managerial implications.

## 6.1. Peripheral Developer Influence on OSS Product Quality Enhancement: A Paradox

Although we find a positive impact of the number of peripheral developers on product quality assessment, our findings cast a doubt on their contributions to quality enhancement. Although quality enhancements are more engaging, we do not find evidence of the contributions of peripheral developers to this activity. However, peripheral developers have a the detection of defects. We investigated these effects further through some follow-up interviews.

Peripheral Developer Impacts on OSS Product Quality Development and Diffusion Across OSS Product Life-Cycle Stages  
![](/api/attachments/R724Z757/fulltext/images/f9bf99fda8589c463569ec78303cc03b2a01e2636d1d2e9ac14d82d6a8820ac9.jpg)

![](/api/attachments/R724Z757/fulltext/images/79b82bccac6556b0cb92e7165c3c16e8f778e9409eedb7c722ff4870410c93a6.jpg)

![](/api/attachments/R724Z757/fulltext/images/e50b1a698051c35afde34864880ce512436f7c266b0ce4ebf7ccd7b4b2946dab.jpg)

![](/api/attachments/R724Z757/fulltext/images/609cd302d115f9762bc8fcdf41609e3ea7a608ebbb4d1fe96e2365fa91480ca8.jpg)  
greater impact on quality assessment than core developers. Furthermore, although core developers may not make significant contributions to the product enhancement activities, they have a negative effect on

Table 8 Summary of Hypotheses Testing

<table><tr><td>Hypothesis</td><td>Empirical support</td></tr><tr><td>H1A: Compared with core developers, the participation of peripheral developers will have a greater impact on quality assessment of the open-source products.</td><td>Supported</td></tr><tr><td>H1B: Compared with core developers, the participation of peripheral developers will have a greater impact on quality enhancement of the open-source products.</td><td>Not supported</td></tr><tr><td>H2A: Greater participation of peripheral developers in open-source projects will lead to greater awareness about the open-source product.</td><td>Supported</td></tr><tr><td>H2B: Greater participation of peripheral developers in open-source projects will enhance the adoption of the OSS product.</td><td>Supported</td></tr><tr><td>H3A: The influence of the participation of peripheral developers on product quality assessment is greater in mature stages of OSS product development than in the early (alpha and beta) stages.</td><td>Supported</td></tr><tr><td>H3B: The influence of the participation of peripheral developers on product quality enhancement is greater in mature stages of OSS product development than in the early (alpha and beta) stages.</td><td>Not supported</td></tr><tr><td>H4A: The influence of the participation of peripheral developers on product awareness is greater in mature stages of OSS product development than in the early (alpha and beta) stages.</td><td>Supported</td></tr><tr><td>H4B: The influence of the participation of peripheral developers on product adoption is greater in mature stages of OSS product development than in the early (alpha and beta) stages.</td><td>Supported</td></tr></table>

During our follow-up interviews, one peripheral developer remarked: “I’ve let the Linux version know of some bugs, but we mostly go our own separate ways with it. We have different priorities. Nope (I did not contribute any bug fixes to Linux).” One plausible reason for the lack of significant effects of peripheral developers on product quality enhancement may be the nature of the OSS product. For instance, a peripheral developer’s impacts could be less significant for larger products because of the greater coordination complexities. Smaller-sized products might facilitate greater interactions across developers (core and peripheral), and hence may speed up the fixing of defects. Larger products, on the other hand, might require more elaborate governance mechanisms to facilitate developer interactions and engagement, and hence the impacts of peripheral participants may not be significant for these larger OSS products. We tested this reasoning through a model that included the interaction of the number of peripheral developers and size of the OSS product. We found that size significantly moderates the relationship between the number of peripheral developers and product quality enhancement. In particular, we found that more peripheral developers increase the product quality enhancement effort on smaller projects, but not on larger projects.<sup>13</sup> Although we have demonstrated the moderating effects of size, future research should examine the effects of other contingencies (e.g., product attributes and governance mechanisms).

Another plausible explanation for the missing impacts may be the lack of appropriate coordination mechanisms to facilitate contributions from geographically dispersed peripheral developers. The need for meaningful interactions and greater engagement among developers to enhance product quality is well established (Martin 1991, Connell and Shafer 1989, Tyre and von Hippel 1997, Kristensen 1992).<sup>14</sup> Von Hippel (2005) emphasized that newer developments on an innovation occur through repeated cycles of trial and error, because some information is tacit and localized for users (sticky information: information related to their needs and some ideas), whereas other information related to product design resides with core developers (design information). Crowston et al. (2006) argue that peripheral developers in OSS development projects are less interconnected, less central, and have fewer interactions than the core group of developers. Thus, due to the lack of appropriate (technological or managerial) mechanisms to integrate peripheral developers with the team of core developers and facilitate interactions, the development environment may be unable to tap the potential of these peripheral developers for product quality enhancement. Hence, the absence of governance mechanisms to facilitate engagement and interactions between core and peripheral developers might lead to the lack of influence of peripheral developers on product quality enhancements, particularly on large products. A more in-depth examination of these effects is essential to enhance our understanding regarding product enhancement.

Furthermore, it is surprising that the core developers have no significant effects on product enhancements. To further test these effects, we examined the interactive effects of core and peripheral developers. Results suggest that although core developers, on their own, may not have any significant effects on quality enhancement, they have positive impacts in the presence of peripheral developers. The results indicate that core developers’ knowledge of product design is a positive influence on product enhancement when it is combined with fresh insights from peripheral developers.

Overall, these findings suggest that the effects of peripheral and core developers on product quality enhancement are not as straightforward. However, it must be noted that our study focused on the numbers of each type of developers. Other developer characteristics such as their skills and motivations might provide more robust evidence of the developers’ contributions to product quality enhancement, especially since it requires more intellectual effort. Furthermore, as our results demonstrate, there is the need to examine how product characteristics moderate the effects of these developers on quality enhancement.

## 6.2. Peripheral Developer Influence on OSS Product Diffusion

Our empirical results provide support for peripheral developers serving as information sources to enhance product awareness and as word-of-mouth agents to enhance actual adoption. The interviews revealed that peripheral developers use personal channels (such as their blogs and websites) to serve as diffusion agents. Our interviews suggest that peripheral developers are very active promoters of the products with which they are involved.

“We’ve had a lot of help from many people who have posted info on their blogs” (core developer comment about peripheral developer value for product diffusion).

“It’s great work, they find and fix bugs, they test the system or program, they do some kind of advertisement, translate into other languages” (on role of peripheral developer in open source product development).

## 6.3. Peripheral Developer Influence Across the Product Life-Cycle Stages

Finally, the results of our research differentiate the influence of peripheral developers across the lifecycle stages of product development, and thereby extend previous findings related to development stage effects. The primary goals of the products change as they move through the development stages. In the prebeta stages, the emphasis is mostly on design. In contrast, in the beta stages, use testing gains emphasis, and products in the mature stages are characterized by greater stability (Stewart and Gosain 2006). Our empirical results indicate that peripheral developer contributions are the greatest in the mature stages. Furthermore, the interview results highlight the learning and product development effects as primary reasons for the increased influence of peripheral developers with increasing maturity. For example, elaborating on the motivations to participate in open-source product development, a developer noted: “Definitely. I think maturity is a major factor,” and a second developer observed that, in the mature stages,“0 0 0 it’s harder to make “bad” changes, but people are also generally going to be more familiar with it (or able to train others).” Another developer commented that increased participation in more mature stages of product development is due to the better structure of the product that facilitates activities like bug detection. Explaining this idea, a developer pointed out that “code base should be more well-defined” in the mature stages of the development. The increased influence of peripheral developers in the later stages of the development alludes to learning effects. Over time, the peripheral developers’ familiarity and skills may improve as they become indoctrinated into the community and are more familiar with the product. The product structure itself improves as the product matures. Although our findings indirectly support the assertion that these mechanisms may be driving peripheral participation, additional research is needed to directly confirm the learning and indoctrination effects underlying the empirical relations found in this study.

## 6.4. Limitations of the Research

Before discussing the contributions of the study, we note some of its key limitations. Our operationalization of peripheral developers as a percentage of code contributed could have some limitations because it is based on post hoc observation of effort. It is certainly possible that some peripheral developers write little code, yet they contribute frequently and significantly. Our approach is consistent with the prevailing perspectives on identifying peripheral developers, but there is an opportunity to elaborate on other means of categorizing core and peripheral developers on the basis of a priori intent. Furthermore, the lack of data reports linking activities (such as commits made) to an individual developer limits our ability to develop more comprehensive criteria for defining peripheral developers. In addition, as indicated earlier, our interviews confirmed amount of code contributions to be a valid way to classify the developers as peripheral.<sup>15</sup>

One core developer categorized the procedure to be one of the many ways in which peripheral developers can be identified and summarized: “not the only metric but it would be a useful metric.”

Furthermore, because the data were collected from Source Forge, our sample has few projects championed by organizations. Hence, more analysis is needed to examine the dynamics of developer contributions for projects championed specifically by organizations. Additionally, it is also not known if the OSS products for which CVS data is not available exhibit significantly different behavior patterns from those used in this study. Finally, although we have focused on defects, other measures of product quality assessment and enhancement may have different dynamics. Notwithstanding these limitations, our study contributes to a significant academic understanding of peripheral developer participation in OSS communities and has important implications for practicing managers.

## 6.5. Contributions to Research

Developer contributions have continually intrigued OSS researchers, and recent research has revealed that developers may vary in the level and nature of contributions (AlMarzouq et al. 2005, Crowston and Howison 2005, Krishnamurthy 2002, Mockus et al. 2002, Gacek et al. 2001, Cox 1998). Specifically, peripheral participants that contribute in many ways other than being a part of the core design and development team are important constituents and are gaining increased attention from researchers and mainstream corporate software development teams. Although developers’ motivations and contributions are quite well studied, our research opens the black box of all open-source developers and examines the contributions of a subgroup (i.e., peripheral developers). In the open-source domain, we contribute to the literature on developer roles by examining how increased peripheral participation may influence product quality assessment and enhancement as well as diffusion outcomes and how these impacts vary across the product life-cycle stages. The results clearly delineate the role of peripheral developers from that of core developers, and we find that peripheral contributors make more significant contributions to quality assessment than core developers. Furthermore, our results also have implications for peripheral participation in virtual communities. Prior research has found that participants with diverse backgrounds may contribute to the virtual communities to gain extrinsic (e.g., economic), or intrinsic (e.g., sense of self-worth, identity verification, and social affiliation) rewards (Bock et al. 2005, Ma and Agarwal 2007, Kankanhalli et al. 2005); or to develop social capital (Chiu et al. 2006, Wasko and Faraj 2005). Our results extend this literature, and offer insights into the type of activities to which peripheral participants may contribute the most in virtual communities. In particular, our results suggest that peripheral participants bring valued novel ideas or perspectives to the existing stream of ideas or products in virtual communities. Their participation is valuable because they can help improve the products of the virtual communities or popularize it among others who are not aware of the community. However, peripheral participants are not substitutes for a core group of members. Instead, they complement the roles of the core members, particularly in improving the products of the community or in evangelizing the products of the community through word of mouth.

By delineating the peripheral developer impacts from those of the core developers, this study opens up the black box of developer contributions and differentiates the contributions of core from peripheral developers. This may help explain some of the surprising findings in prior research that has examined developer impacts across the open-source product life-cycle stages. For example, Stewart and Gosain (2006) found that the developer team size negatively impacted team performance (more negative in early stages than in the later stages). We believe that differentiating peripheral developers from core developers might help explain the effects of team size and composition, and resolve the seemingly paradoxical finding regarding developer contributions.<sup>16</sup> The differentiation of core versus peripheral developers should stimulate interesting questions for future research on opensource products. For example, research should study factors that influence peripheral developer contributions across the stages of a product life cycle. Fur thermore, integration mechanisms in the form of development tools, processes, and systems to manage distributed contributions often help enhance a product (Thomke 2006). It would be important to examine whether the implementation of technology-facilitated mechanisms such as developer tool kits may lead to more effective contributions from peripheral developer participants. In addition, it would be interesting to examine how the relationships assessed in this study are contingent on the nature, size, or complexity of software products. Also, although we have assessed the role of peripheral developers on product quality and success, more research is needed to examine if product quality may influence the success of open-source products. Finally, our results also show that peripheral participants have an even greater impact on product quality and diffusion outcomes in advanced and mature stages of product life cycle. More research is needed to ascertain the reasons (for example, learning and maturation effects) that may lead to these differences in peripheral developer impacts across product life-cycle stages.

## 6.6. Managerial Implications

Our research has important implications for the peripheral participation in OSS development, an exemplar of virtual communities that are gaining increased interest among corporations. For example, there is increased interest amongst corporations in harnessing the untapped potential of peripheral developers through the open-source model (Fitzgerald 2006). Following the open innovation approach, firms are increasingly headhunting for top developers from a global pool of OSS developers. Therefore, it is important to understand differences in the contributions of different types of developers (Ågerfalk and Fitzgerald 2008). Our research will help managers champion these initiatives in private corporations to effectively govern the inclusion of peripheral contributors in the open-source domain. Specifically, we offer the following insights to practicing managers.

First, the role and contributions of peripheral participants vary according to the nature of the activity. We observe that peripheral developers have a greater use focus and although they have positive impacts on product quality assessments, their impacts are not universal. They may be able to contribute to product quality enhancement on smaller projects. On the other hand, larger projects will require coordination mechanisms to facilitate their contributions to quality enhancement. Indeed, recent research has identified that in corporate-driven open innovation communities, informal and formal social structures play an important role in managing external contributors (von Krogh et al. 2003, West and O’Mahony 2005). Organizations need to carefully explore if these various mechanisms may motivate peripheral developers to contribute to product quality enhancement, without any adverse controls that suppress their intellectual, aesthetic, and pleasure-based motivations.

Second, our study has important implications for leveraging peripheral participants to enhance the outreach and success of OSS products. Peripheral participants significantly influence awareness and actual adoption of OSS products. They have a greater credibility with potential consumers. They are ideal product emissaries because they associate their identities with the products they are working on and use contemporary technologies, such as blogs, to further the diffusion of OSS products. Thus, our study has important implications for marketing managers within firms espousing open innovations. The peripheral participants may be an important way for marketing managers to defy the traditional trade-off between the mass outreach of advertising medium and personalized affect of word-of-mouth advertising. With their personalized message and use of technology, peripheral participants might be any OSS marketer’s ideal product emissaries.

Finally, organizations have to variably set the expectations of impacts from peripheral participation across the product life-cycle stages. Peripheral impacts for both the product quality and product diffusion outcomes are found to be greater for mature projects than for products in the early stages. Besides varying their own internal expectations of peripheral developer contributions, firms using open innovations might engage in initiatives that convey stability and maturity of a project to the targeted population of peripheral developers.

Overall, our research develops a comprehensive theory of peripheral developer contributions to OSS product quality and diffusion. We delineate the impact of peripheral developers from those of core developers on product quality and examine the impacts of peripheral developments on quality development and diffusion of OSS products across their life cycle. This helps firms understand the opportunities and challenges for leveraging peripheral participation in software development. Although we focus specifically on the OSS model, the study is likely to stimulate a focus on the role of peripheral developer contributions, interests, motivations, and governance mechanisms in other virtual communities.

## Acknowledgments

The authors thank the research workshop participants at Michigan State University, Oklahoma State University, University of Oklahoma, INFORMS Conference on Information Systems and Technology 2005 held in San Francisco, and the Academy of Management Conference 2006 in Atlanta for their feedback on earlier versions of the paper. Thanks also to Katherine Stewart, Sanjay Gosain, Nilesh Saraf, and Kevin Crowston for input on earlier versions of this paper. The authors also thank the senior editor Dr. Sandra Slaughter and two anonymous reviewers for their feedback and suggestions throughout the review cycle.

## References

Aaker, D. A., D. M. Stayman. 1990. Measuring audience perceptions of commercials and relating them to ad impact. J. Advertising Res. 30(4) 7–17.

Ågerfalk, P., B. Fitzgerald. 2008. Outsourcing to an unknown workforce: Exploring opensourcing as a global sourcing strategy. MIS Quart. 32(2) 385–410.

AlMarzouq, M., L. Zheng, G. Rong, V. Grover. 2005. Open source: Concepts, benefits, and challenges. Comm. Assoc. Inform. Systems 16(37) 756–784.

Ang, S., S. A. Slaughter, K. Y. Ng. 2002. Human capital and institutional determinants of information technology compensation: Modeling multilevel and cross-level interactions. Management Sci. 48(11) 1427–1445.

Atkinson, J. W. 1957. Motivational determinants of risk-taking behaviors. Psych. Rev. 64(6, Part 1) 359–372.

Bajaj, A., S. Kekre, K. Srinivasan. 2004. Managing NPD: Cost and schedule performance in design and manufacturing. Management Sci. 50(4) 527–528.

Bezroukov, N. 1999. Open source software development as a special type of academic research (critique of Vulgar Raymondism). First Monday 4(10). http://firstmonday.org/htbin/ cgiwrap/bin/ojs/index.php/fm/article/view/696/606.

Bitzer, J. P., J. H. Schröder. 2005. Bug-fixing and code-writing: The private provision of open source software. Inform. Econom. Policy 17(3) 389–406.

Blau, J. 2002. German government adopts Linux in IBM deal. Networkworld (June 3).

Bock, G. W., R. W. Zmud, Y. G. Kim, J. N. Lee. 2005. Behavioral intention formation in knowledge sharing: Examining the roles of extrinsic motivators, social-psychological forces, and organizational climate. MIS Quart. 29(1) 87–111.

Bonaccrosi, A., C. Rossi. 2003. Why open source software can succeed. Res. Policy 32(7) 1243–1258.

Bonus, H. 1973. Quasi-Engel curves, diffusion, and the ownership of major consumer durables. J. Political Econom. 81(3) 655–677.

Brown, J. S., J. Hagel III. 2006. Creation nets: Getting the most from open innovation. McKinsey Quart. 2(2) 40–51.

Bryk, A. S., S. W. Raudenbush. 1992. Hierarchical Linear Models: Application and Data Analysis. Sage Publications, Newbury Park, CA.

Bucklin, L. P. 1965. The informative roles of advertising. J. Advertising Res. 5(3) 11–15.

Buttle, F. A. 1998. Word of mouth: Understanding and managing referral marketing. J. Strategic Marketing 6(3) 241–254.

Chesbrough, H. 2003. Open Innovation: The New Imperative for Creating and Profiting from Technology. Harvard Business School Press, Boston.

Chiu, C. M., M. H. Hsu, E. T. G. Wang. 2006. Understanding knowledge sharing in virtual communities: An integration of social capital and social cognitive theories. Decision Support Systems 42(3) 1872–1888.

Clark, K. B., T. Fujimoto. 1991. Product Development Performance. Harvard Business School Press, Boston.

Cohen, J., P. Cohen, S. G. West, L. S. Aiken. 2003. Applied Multiple Regression/Correlation Analysis for the Behavioral Sciences. Lawrence Erlbaum Associates, Mahwah, NJ.

Coleman, J. S., E. Katz, H. Menzel. 1966. Medical Innovation: A Diffusion Study. The Bobbs-Merrill Company, Indianapolis.

Comino, S., F. M. Manenti, M. L. Parisi. 2007. From planning to mature: On the determinants of open source take-off. Res. Policy 36 1575–1586.

Connell, J. L., L. B. Shafer. 1989. Structured Rapid Prototyping: An Evolutionary Approach to Software Development. Prentice Hall International, Yourdon Press, Upper Saddle River, NJ.

Cox, A. 1998. Cathedrals, bazaars and the town council. Slashdot (October 13), http://slashdot.org/features/98/10/13/ 1423253.shtml.

Crowston, K., J. Howison. 2005. The social structure of free and open source software development. First Monday 10(2). http://firstmonday.org/htbin/cgiwrap/bin/ojs/index.php/fm/ article/viewArticle/1207/1127.

Crowston, K., H. Annabi, J. Howison. 2003. Defining open source software project success. S. T. March, A. Massey, J. I. DeGross, eds. Proc. 24th Internat. Conf. Inform. Systems, Seattle, 327–340.

Crowston, K., K. Wei, Q. Li, J. Howison. 2006. Core and periphery in free/libre and open source software team communications. Proc. 39th Ann. Hawaii Internat. Conf. System Sci. (HICSS 2006), IEEE Computer Society Washington, DC.

Dalle, J. M., N. Jullien. 2000. NT vs. Linux, or some explorations into the economics of free software. G. Ballot, G. Weisbuch, eds. Applications of Simulation to Social Sciences. Hermès, Paris, 399–416.

Day, G. S. 1971. Attitude change, media and word of mouth. J. Advertising Res. 11(6) 31–40.

DeLone, W. H., E. R. McLean. 1992. Information systems success: The quest for the dependent variable. Inform. Systems Res. 3(1) 60–95.

Dinkelacker, J., P. K. Garg. 2001. Applying open source concepts to a corporate environment. Proc. 1st Workshop Open Source Software Engrg., Toronto. http://opensource.ucc.ie.icse2001.

Eisenhardt, K. M., B. N. Tabrizi. 1995. Accelerating adaptative processes—Product innovation in the global computer industry. Admin. Sci. Quart. 40(1) 84–110.

Fitzgerald, B. 2006. The transformation of open source software. MIS Quart. 30(3) 587–598.

Gacek, C., T. Lawrie, B. Arief. 2001. The many meanings of open source. Technical report 1, DIRC—InterDisciplinary Research Collaboration in Dependability. http://www.dirc.org.uk/ publications/techreports/papers/1.pdf.

Garcia, J. M. 2004. Quantitative analysis of the structure and dynamics of the SourceForge project and developer populations: Prospective research themes and methodologies. Stanford Inst. Econom. Policy Res. Accessed May 29, 2010, http:// www-siepr.stanford.edu/programs/OpenSoftware\_David/ Prospective\_Research\_Themes.html.

Goldman, R., R. P. Gabriel. 2005. Innovation Happens Elsewhere: Open Source as Business Strategy. Morgan Kaufmann, San Francisco.

Gurbani, V. K., A. Garvert, J. D. Herbsleb. 2005. A case study of open source tools and practices in a commercial setting. Proc. 5th Workshop on Open Source Software Engrg., 27th Internat. Conf. Software Engrg.: (ICSE 2005), St. Louis, ACM, New York, 1–6.

Ha, A. Y., E. L. Porteus. 1995. Optimal timing of reviews in concurrent design for manufacturability. Management Sci. 41(9) 1431–1447.

Herr, P. M., F. R. Kardes, J. Kim. 1991. Effects of word-of-mouth and product-attribute information on persuasion: An accessibilitydiagnosticity perspective. J. Consumer Res. 17(4) 454–462.

Hertel, G., S. Niedner, S. Herrmann. 2003. Motivation of software developers in open source projects: An Internet based survey of contributors to the Linux kernel. Res. Policy 32(7) 1159–1177.

Howison, J., K. Crowston. 2004. The perils and pitfalls of mining SourceForge. Proc. Workshop Mining Software Repositories (MSR 2004), 26th Internat. Conf. Software Engrg. (ICSE 2004), Edinburgh, 7–11.

Kalish, S. 1985. A new product adoption model with price, advertising, and uncertainty. Management Sci. 31(12) 1569–1585.

Kankanhalli, A., B. C. Y. Tan, K. K. Wei. 2005. Contributing knowledge to electronic knowledge repositories: An empirical investigation. MIS Quart. 29(1) 113–143.

Krishnamurthy, S. 2002. Cave or community? An empirical examination of 100 mature open source projects. First Monday 7(6). http://firstmonday.org/htbin/cgiwrap/bin/ojs/index.php/fm/ article/view/960/881.

Krishnan, V., K. T. Ulrich. 2001. Product development decisions: A review of the literature. Management Sci. 47(1) 1–21.

Krishnan, V., S. D. Eppinger, D. E. Whitney. 1997. A model-based framework to overlap product development activities. Management Sci. 43(4) 437–451.

Kristensen, P. S. 1992. Flying prototypes: Production departments’ direct interaction with external customers. Internat. J. Food Agribusiness Marketing 4(3) 107–118.

Lakhani, K. R., E. von Hippel. 2003. How open source software works: “Free” user-to-user assistance. Res. Policy 32(6) 923–943.

Lakhani, K. R., R. G. Wolf. 2005. Why hackers do what they do: Understanding motivation and effort in free/open source software projects. J. Feller, B. Fitzgerald, S. Hissam, K. R. Lakhani, eds. Perspectives on Free and Open Source Software. MIT Press, Cambridge, MA, 36–55.

Lavidge, R. J., G. A. Steiner. 1961. A model for predictive measurements of advertising effectiveness. J. Marketing 25(6) 59–62.

Lerner, J., J. Tirole. 2002. Some simple economics of open source. J. Indust. Econom. 50(2) 197–234.

Lilien, G., P. D. Morrison, K. Searls, M. Sonnack, E. von Hippel. 2002. Performance assessment of the lead user generation process for new product development. Management Sci. 48(8) 1042–1059.

Ma, M., R. Agarwal. 2007. Through a glass darkly: Information technology design, identity verification, and knowledge contribution in online communities. Inform. Systems Res. 18(1) 42–67.

Mangold, W. G. 1987. Use of commercial sources of information in the purchase of professional services: What the literature tells us. J. Professional Services Marketing 3(1–2) 5–17.

Martin, J. 1991. Rapid Application Development. Macmillan Publishing, New York.

Mason, R. 1962. Information source use in the adoption process. Unpublished Ph.D. thesis, Stanford University, Stanford, CA.

Mehta, N., C. Xinlei, O. Narasimhan. 2008. Informing, transforming, and persuading: Disentangling the multiple effects of advertising on brand choice decisions. Marketing Sci. 27(3) 334–355.

Mockus, A., R. T. Fielding, J. D. Herbsleb. 2000. A case study of open source software development: The Apache server. Proc. 22nd Internat. Conf. Software Engrg. (ICSE 2000), Limerick, Ireland, 263–272. http://www.computer.org/postal/Web/ csdl/doi/10.1109/ICSE.2000.10136.

Mockus, A., R. T. Fielding, J. D. Herbsleb. 2002. Two case studies of open source software development: Apache and Mozilla. ACM Trans. Software Engrg. Methodology 11(3) 309–346.

Murray, K. B. 1991. A test of services marketing theory: Consumer information acquisition activities. J. Marketing 55(1) 10–25.

Nisbett, R., L. Ross. 1980. Human Inference: Strategies and Shortcomings of Social Judgment. Prentice-Hall, Englewood Cliffs, NJ.

Peay, M. Y., E. R. Peay. 1984. Differences among practitioners in patterns of preference for information sources in the adoption of new drugs. Soc. Sci. Medicine 18(12) 1019–1025.

Raudenbush, S. W., A. S. Bryk. 2002. Hierarchical Linear Models: Application and Data Analysis. Sage, Thousand Oaks, Newbury Park, CA.

Raymond, E. S. 1999. The Cathedral & the Bazaar. O’Reilly, Sebastopol, CA.

Raymond, E. S. 2001. The Cathedral & the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary. O’Reilly, Sebastopol, CA.

Roberts, J. A., I.-H. Hann, S. A. Slaughter. 2006. Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache projects. Management Sci. 52(7) 984–999.

Scacchi, W., J. Feller, B. Fitzgerald, S. Hissam, K. Lakhani. 2006. Understanding free/open source software development processes. Software Process: Improvement Practice 11(2) 95–105.

Shah, S. 2006. Motivation, governance, and the viability of hybrid forms in open source software development. Management Sci. 52(7) 1000–1014.

Stewart, K. J., S. Gosain. 2006. The moderating role of development stage in affecting free/open source software project performance. Software Process: Improvement Practice 11(2) 177–191.

Stewart, K. J., D. P. Darcy, S. L. Daniel. 2006. Opportunities and challenges applying functional data analysis to the study of open source software evolution. Statist. Sci. 21(2) 167–178.

Terwiesch, C., C. H. Loch. 1999. Measuring the effectiveness of overlapping development activities. Management Sci. 45(4) 455–465.

Thomke, S. 2006. Capturing the real value of innovation tools. MIT Sloan Management Rev. 47(2) 24–32.

Tyre, M., E. von Hippel. 1997. The situated nature of adaptive learning in organizations. Organ. Sci. 8(1) 71–83.

von Hippel, E. 2005. Democratizing Innovation. MIT Press, Cambridge, MA.

von Krogh, G., S. Spaeth, K. Lakhani. 2003. Community, joining, and specialization in open source software innovation: A case study. Res. Policy 32(7) 1217–1241.

Vroom, V. 1964. Work and Motivation. John Wiley & Sons, New York.

Wasko, M. M., S. Faraj. 2005. Why should I share? Examining social capital and knowledge contribution in electronic networks of practice. MIS Quart. 29(1) 35–57.

Webster, C. 1991. Influences upon consumer expectations of services. J. Services Marketing 5 516–533.

West, J., S. O’Mahony. 2005. Contrasting community building in sponsored and community founded open source projects. Proc. 38th Annual Hawaii Internat. Conf. System Sci. (HICSS 2005), Waikola Village, HI, IEEE, Los Alamitos, CA.

Woodside, A. G., E. J. Wilson, P. Milner. 1992. Buying and marketing CPA services. Indust. Marketing Management 21(3) 265–272.

Zeithaml, V. A., L. L. Berry, A. Parasuraman. 1993. The nature and determination of customer expectation of service. J. Acad. Marketing Sci. 21(1) 1–12.
