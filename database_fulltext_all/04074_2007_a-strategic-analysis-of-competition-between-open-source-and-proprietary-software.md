---
otero_id: 4074
otero_key: "AG5RSMTZ"
title: "A Strategic Analysis of Competition Between Open Source and Proprietary Software"
authors: "Ravi Sen"
year: "2007"
journal: "Journal of Management Information Systems"
doi: "10.2753/mis0742-1222240107"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
This article was downloaded by: [Chinese University of Hong Kong] On: 23 February 2015, At: 12:56 Publisher: Routledge Informa Ltd Registered in England and Wales Registered Number: 1072954 Registered office: Mortimer House, 37-41 Mortimer Street, London W1T 3JH, UK

![](/api/attachments/AG5RSMTZ/fulltext/images/b1b7b6838fb5f90e16ded335d133b92162b7a579414871a2ba730d5a430e63bc.jpg)

Journal of Management Information Systems

Publication details, including instructions for authors and subscription information: http://www.tandfonline.com/loi/mmis20

# A Strategic Analysis of Competition Between Open Source and Proprietary Software

Ravi Sen <sup>a</sup>

<sup>a</sup> Department of Information, Texas A&M University Published online: 08 Dec 2014.

To cite this article: Ravi Sen (2007) A Strategic Analysis of Competition Between Open Source and Proprietary Software, Journal of Management Information Systems, 24:1, 233-257

To link to this article: http://dx.doi.org/10.2753/MIS0742-1222240107

## PLEASE SCROLL DOWN FOR ARTICLE

Taylor & Francis makes every effort to ensure the accuracy of all the information (the “Content”) contained in the publications on our platform. However, Taylor & Francis, our agents, and our licensors make no representations or warranties whatsoever as to the accuracy, completeness, or suitability for any purpose of the Content. Any opinions and views expressed in this publication are the opinions and views of the authors, and are not the views of or endorsed by Taylor & Francis. The accuracy of the Content should not be relied upon and should be independently verified with primary sources of information. Taylor and Francis shall not be liable for any losses, actions, claims, proceedings, demands, costs, expenses, damages, and other liabilities whatsoever or howsoever caused arising directly or indirectly in connection with, in relation to or arising out of the use of the Content.

This article may be used for research, teaching, and private study purposes. Any substantial or systematic reproduction, redistribution, reselling, loan, sub-licensing, systematic supply, or distribution in any form to anyone is expressly forbidden. Terms & Conditions of access and use can be found at http://www.tandfonline.com/page/terms-and-conditions

# A Strategic Analysis of Competition Between Open Source and Proprietary Software

RAVI SEN

RAVI SEN is an Assistant Professor in the Department of Information and Operations Management at Mays Business School, Texas A&M University. He received his Ph.D. in Business Administration (major in MIS) in 2003 from the College of Business, University of Illinois at Urbana–Champaign. His research interests include open source software, electronic commerce, and software security. He has published in Journal of Management Information Systems, International Journal of Electronic Commerce, Communications of the AIS, and Electronic Markets.

ABSTRACT: This paper analyzes a software market consisting of a freely available open source software (OSS), the commercial version of this OSS (OSS-SS), and the competing commercial proprietary software (PS). We find that in software markets characterized by low direct network benefits, the PS vendor is better off in the presence of competition from OSS-SS. Furthermore, the OSS-SS vendor in these markets is better off by having lower usability than PS. Therefore, the PS vendor has little incentive to improve the usability of their software in these markets. On the other hand, in software markets characterized by high network benefits, a PS vendor is threatened by the presence of OSS-SS and can survive only if the PS is more usable than the competing OSS-SS.

KEY WORDS AND PHRASES: commercial open source, economics of open source, FLOSS, open source software, software competition, software market.

AS OPPOSED TO COMMERCIAL PROPRIETARY SOFTWARE (PS), open source software (OSS) allows the users to have access to the source code of the software, the freedom to use the software as they see fit, improve it, fix its bugs, augment its functionality, and redistribute the software or its derivative (for free, or at a charge) to other users who could, in turn, modify or use it according to their own needs [30]. Apache (a Web server), Linux (an operating system), and Sendmail (an Internet mail transfer agent) are some notable examples of OSS that have achieved remarkable success against their closed source or proprietary alternatives, as is evident in their large user base. Some other examples of PS and their open source competition are given in Table 1.

The increasing adoption of OSS poses some concern for commercial proprietary (or “closed source”) software vendors. This concern is best summed up in the following statement from a memo written by Microsoft CEO Steve Ballmer in 2003: “Noncommercial software products in general and Linux in particular present a competitive challenge for us and our entire industry and they require our concentrated focus and attention” (www.topdog04.com/000216.html).

Table 1. Open Source and Proprietary Applications

<table><tr><td>Application</td><td>Proprietary</td><td>Open source</td></tr><tr><td>Web browser</td><td>Internet Explorer</td><td>Mozilla Firefox</td></tr><tr><td>Web server</td><td>Microsoft IIS, Netscape</td><td>Apache</td></tr><tr><td>Application server</td><td>WebMethods</td><td>JBoss, Apache Tomcat</td></tr><tr><td rowspan="2">Office suite</td><td>MS Office, Corel</td><td rowspan="2">OpenOffice.org (based on Sun&#x27;s proprietary StarOffice)</td></tr><tr><td>WordPerfect Office</td></tr><tr><td>E-mail/collaboration</td><td>MS Exchange, Lotus Notes</td><td>Ximian Evolution</td></tr><tr><td>Database</td><td>Oracle9i, DB2, MS SQL</td><td>MySQL, PostgreSQL</td></tr></table>

This statement illustrates the seriousness with which the commercial software producers are treating competition from OSS, and their concern is not misplaced. OSS user-license characteristics, combined with the fact that they are available for free, is resulting in their increasing adoption by the user population. In a November 2003 CIO survey of 375 information executives, 54 percent said that within five years open source would be their dominant platform [21]. Big vendors such as Dell, IBM, and Sun Microsystems support OSS development, and are developing applications that would work with open source platforms.

These successes of OSS have led to an increasing interest in understanding this form of software, its development process, and its impact on the software industry. The current research in this area can be classified into three broad categories [30]: (1) understanding the motivation on the part of individuals and organizations to initiate and participate in open source projects, (2) understanding the adoption of open source applications by individuals and organizations, and (3) understanding the impact of OSS applications on the industrial organization of the software industry and the social welfare of software users. Most of the current literature on open source projects focuses on the motivation of individuals and organizations to initiate and participate in these projects (e.g., [2, 13, 16, 24, 29, 34, 36]). Furthermore, adoption of OSS by individuals and organizations could be explained by the existing theories on technology diffusion [35] and technology adoption [6], and their numerous extensions (e.g., [1, 14, 18, 23, 28, 38, 39]). Similarly, literature on information systems’ success [7] and virtual teams [17] can help us understand the performance of OSS since OSS development teams have often been characterized as virtual teams [5, 15]. Some work has also been done to study software markets from the public policy point of view [3, 19], and the type of software license best for the software users [12]. There are a few studies that analyze the competition between open source and commercial software. However, these papers focus primarily on competition between particular operating systems [4, 8] or consider open source to be privately provided public goods and model a software user-developer’s choice between producing open source or closed source software [3, 16]. User-developers are individuals/organizations that not only participate as developers in open source projects but are also the primary users of the end product. However, they form a very small proportion of most software markets [33]. These markets are generally dominated by users who are never involved in the development of the software,<sup>1</sup> and software producers/developers compete for these nondeveloper users. However, there is a dearth of work that can help us understand the impact of OSS on competition in this segment of the software market. Furthermore, there is no study that analyzes the extent of this competition; is the competition serious enough to result in the demise of commercial PS vendors and, by extension, the end of the software industry as we know it, or will the commercial PS vendors survive this competition and coexist with OSS? Finally, the commercial software vendors would like to know about their strategic options for competing successfully against their open source rivals.

This paper takes a purely analytical approach to understanding the competition between open source and proprietary software. It differs from existing studies of a similar nature because it presents a mathematical model that not only captures the competition between commercial PS and OSS but also incorporates user-specific characteristics such as their valuation of software usability, and software-specific characteristics such as its usability and the strength of network benefits provided by the software. This model is then analyzed to explain the impact of OSS on competition in the software industry, and identify the conditions under which OSS has an adverse impact on the existence of commercial PS vendors.

## The Model

THE PROPOSED MODEL DOES NOT DWELL upon the reasons for the existence of the OSS. OSS exists because there are individuals and organizations willing to develop and distribute them. The existing literature does a good job of explaining the motivation of these individuals and organizations to initiate, develop, and distribute OSS [13, 19, 23, 25, 29]. Instead, we assume that both OSS and commercial PS exist and compete in their relevant market segment. It should be noted at this point that the competition is assumed to be between the same categories of software—that is, the competing software are assumed to address the same user needs. The objective of this paper is (1) to analyze this competition and determine the conditions under which OSS can have an adverse impact on the existence of commercial PS vendors in the same market, and (2) to suggest strategic solutions to commercial PS vendors that can help them to compete successfully against OSS.

## Software Characteristics

The model assumes that the software under consideration, whether open source or proprietary, meet the functional (i.e., whether it can perform some function) and reliability (e.g., error handling, security feature) needs of the potential users.<sup>2</sup> However, they differ in their usability. Overall software usability, a subjective measure, is typically described in terms of five characteristics—ease of learning, efficiency of use, memorability, error frequency and severity, and subjective satisfaction [32]. In this model, we define the lack of software usability (i.e., unusability) as the main differentiating factor between various software product options. Commercial PS is assumed to have the highest software usability (or lowest unusability) because of features such as extensive manuals that come with these software, multichannel support provided by the software vendor, and efforts by the vendor to make the software as user-friendly as possible (e.g., default installation options, intuitive graphical user interface [GUI], contextual help, demos and examples, and fault-tolerance features of the software, etc). On the other hand, freely available open source software without any support services (OSS) is assumed to have the lowest average software usability [11, 31] or highest unusability. Commercial open source software (denoted by OSS-SS) that comes bundled with support services (e.g., documentation, phone consultation, training options, etc.) is assumed to have unusability somewhere between that of OSS and PS. Thus, for an OSS-SS vendor, software usability is a decision variable that can be optimize to maximize profits. Finally, the proposed model assumes that users benefit from positive direct network effects generated by software’s expected installation base. For instance, as more people use MS Word, it becomes easier to share files written in Word format. The assumption about positive network effects is based on the existing literature rooted in industrial organizational theories, which has established the positive network benefits of software [9, 10, 20].

## Software Market

The basic setup of the model involves a software market that consists of commercial proprietary software (PS), an open source substitute with documentation and service support (OSS-SS), and this same open source substitute without documentation and service support (OSS).

• Commercial proprietary software vendor: This vendor sells commercial closed source software that comes with a full documentation and support services. We denote the unusability of PS by $\beta _ { { \scriptscriptstyle P } }$ . We also assume that the total cost associated with each unit of PS is $( 1 + \beta _ { P } ) c$ . The first component is a fixed cost, c. This cost captures any expenses related to packaging, distribution, rebates, and so on. The second component is a variable cost of providing support services as and when a user requests it. The variable cost is assumed to be proportional to the unusability of the software—that is, $\beta _ { { \scriptscriptstyle P } } c .$ . If, on an average, the software is perceived to be less usable, a user is more likely to contact the vendor for support services, resulting in a higher variable cost, whereas if the software is perceived to be highly usable, a user is less likely to contact the vendor for support, resulting in lower variable costs. Thus the total cost is higher for software that has less usability (or more unusability). However, because PS is assumed to be highly usable in comparison to commercial and freely available OSS, we assume that ${ \beta } _ { { P } } = 0 .$ . Therefore, for the PS vendor, total cost associated with each unit of PS sold is $^ { c , }$ and the PS vendor’s profit function is $\pi _ { _ P } = [ P _ { _ P } - c ] D _ { _ P } ,$ , where the demand for PS is $D _ { p } ,$ and the unit price is $P _ { { P } ^ { \bullet } }$

• Open source software with support services vendor: This vendor sells a nondivisible bundle of highly usable OSS and accompanying support services for this software. The total cost associated with each unit of OSS-SS sold is given by $( 1 + \beta _ { s } ) c$ , where $0 \leq \beta _ { s } < 1$ is the unusability of OSS-SS, $\beta _ { s } c$ is the variable costs associated with each unit of OSS-SS sold, and c is the fixed cost associated with each unit of OSS-SS sold. The profit function for OSS-SS vendor is $\pi _ { _ { S } } = [ P _ { _ { S } } - ( 1 + \beta _ { _ { S } } ) c ] D _ { _ { S } } ,$ , where the demand for OSS-SS is $D _ { s }$ and $P _ { s }$ is the price charged for one unit of OSS-SS.

• Open source software without support services: This includes OSS (both in executable form and its actual code) that can be downloaded for free from the Internet. A user can seek (e.g., on the Internet) additional help on using this software, but the “free” help that is available is not the same quality as the one provided by OSS-SS vendors, and therefore this help does not have any significant impact on the usability of the software. The unusability of OSS is assumed to be highest and is denoted by $\beta _ { o } ( = 1 )$ ), and the demand for this type of software is denoted by $D _ { o }$ in the model.

## Software Users

Software users derive an inherent value, A, by using a software. A is assumed to be relatively high so that the market is fully covered. Furthermore, we assume that the time spent by users on installing, configuring, and maintaining the software for proper use is a function of software usability and the value that these users attach to this usability. For example, skilled and experienced software users are more likely to put a low value on software usability because they can “figure out” the software. On the other hand, relatively less skilled users or users without much experience in software use will put a premium on software usability because usable software will cause them fewer problems. Therefore, we assume that the software users differ in the value that they attach to software usability. These users are indexed by their valuation of software usability, $0 < \nu \leq 1 ,$ <sup>3</sup> and are distributed uniformly over this interval with unit density. For a consumer of type v, we model the cost associated with using any software as a linear function of his or her valuation of usability of the software being used. This cost is $( 1 + \beta _ { P } ) \nu$ for PS, $( 1 + \beta _ { s } ) \nu$ for OSS-SS, and $( 1 + \beta _ { o } ) \nu$ for OSS. The total cost of ownership for the software is assumed to be the sum of the purchase price and the cost associated with using the software.

The utility for consumer of type v when he or she buys PS is given as follows:

$$
U _ {P} (v) = A + \theta q _ {P} - (1 + \beta_ {P}) v - P _ {P} = A + \theta q _ {P} - v - P _ {P},\tag{1a}
$$

where the expected market of PS is $q _ { P }$ and θ is the strength of network effects for this software category. A low value of θ implies that there are few if any direct network effects associated with the software. On the other hand, a high value of θ means that there are significant direct network benefits associated with the software.

Similarly, the utility for consumer of type v when he or she buys OSS-SS is given as follows:

$$
U _ {s} (v) = A + \theta (q _ {s} + q _ {o}) - (1 + \beta_ {s}) v - P _ {s} = A + \theta (1 - q _ {P}) - (1 + \beta_ {s}) v - P _ {s},\tag{1b}
$$

and the utility for consumer of type v when he or she buys OSS is given as follows:

$$
U _ {o} (v) = A + \theta (q _ {s} + q _ {o}) - (1 + \beta_ {o}) v = A + \theta (1 - q _ {p}) - 2 \mathrm{v}.\tag{1c}
$$

Note that the users of OSS-SS and OSS benefit from their combined user base. For example, the users of Linux will benefit from the total installation base of Linux, irrespective of the distribution of commercial and free Linux among these users. The utility functions have been modeled so that a software user’s utility is linearly proportional to the expected installation base of the software, and is reduced by the unusability of the software and the price paid for using that software. A user opts for the software that offers maximum utility. The variables, parameters used in the model, and the functional relationships between these variables are summarized in Table 2.

## Equilibrium in the Price-Setting Game

THE PRICE EQUILIBRIUM IS DETERMINED for a simple scenario consisting of PS, OSS-SS, and OSS. Because fixed costs are irrelevant to the pricing game, they are assumed to be zero [37]. The equilibrium prices, demands, and profits are derived in Appendix A. The equilibrium prices and demand are as follows:

$$
P _ {P} ^ {*} = \left(\frac {2 (1 - 2 \theta) (\beta_ {S} - \theta) + (1 - 2 \theta) (3 + \beta_ {S}) c - \theta (1 - \beta_ {S})}{3 + \beta_ {S} - 8 \theta}\right)\tag{2a}
$$

$$
P _ {S} ^ {*} = \left(\frac {\left(1 - \beta_ {S}\right) \left(\beta_ {S} - \theta\right) - 2 \theta \left(1 - \beta_ {S}\right) + \left[ 3 + \beta_ {S} + 4 \theta \left(1 + \beta_ {S}\right) \right] c}{3 + \beta_ {S} - 8 \theta}\right)\tag{2b}
$$

$$
D _ {P} ^ {*} = \left[ \left(\frac {\beta_ {S} - \theta}{\beta_ {S} - 2 \theta}\right) - \left(\frac {(1 + \beta_ {S} - 4 \theta) (\beta_ {S} - \theta) + \theta (1 - \beta) - 2 \theta (5 + 3 \beta_ {S}) c}{(\beta_ {S} - 2 \theta) (3 + \beta_ {S} - 8 \theta)}\right) \right]\tag{3a}
$$

$$
\begin{array}{c} D _ {S} ^ {*} = \left[ \left(\frac {(1 + \beta_ {S} - 4 \theta) (\beta_ {S} - \theta) + \theta (1 - \beta_ {S}) - 2 \theta (5 + 3 \beta_ {S}) c}{(\beta_ {S} - 2 \theta) (3 + \beta_ {S} - 8 \theta)} - \frac {\theta}{(\beta_ {S} - 2 \theta)}\right) \right. \\ \left. - \left(\frac {\beta_ {S} - 3 \theta}{3 + \beta_ {S} - 8 \theta}\right) - \left(\frac {3 + \beta_ {S} + 4 \theta (1 + \beta_ {S})}{(3 + \beta_ {S} - 8 \theta) (1 - \beta_ {S})}\right) c \right] \end{array}\tag{3b}
$$

<sub>sumptions</sub> A<sup>bout</sup> <sup>Software</sup> <sup>and</sup> <sup>User</sup> <sup>Char</sup>

<table><tr><td></td><td>Proprietary software</td><td>Commercial open source</td><td>Free open source</td></tr><tr><td>Inherent value of the software</td><td>A</td><td>A</td><td>A</td></tr><tr><td>Lack of software usability or unusability</td><td> $\beta_{P} = 0$ </td><td> $0 < \beta_{S} < 1$ </td><td> $\beta_{O} = 1$ </td></tr><tr><td>Strength of direct network effects</td><td> $0 \leq \theta \leq 1$ </td><td> $0 \leq \theta \leq 1$ </td><td> $0 \leq \theta \leq 1$ </td></tr><tr><td>Expected installation base that provides network effects</td><td> $q_{P}$ </td><td> $(1 - q_{P})^{*}$ </td><td> $(1 - q_{P})^{*}$ </td></tr><tr><td>Total network effects</td><td> $\theta q_{P}$ </td><td> $\theta(1 - q_{P})$ </td><td> $\theta(1 - q_{P})$ </td></tr><tr><td>Consumer&#x27;s valuation of software (un)usability</td><td> $0 < v \leq 1$ </td><td> $0 < v \leq 1$ </td><td> $0 < v \leq 1$ </td></tr><tr><td>Price paid for the software</td><td> $P_{P}$ </td><td> $P_{S}$ </td><td>0</td></tr><tr><td>Demand</td><td> $D_{P}$ </td><td> $D_{S}$ </td><td> $D_{O}$ </td></tr><tr><td>Profit functions</td><td> $\pi_{P} = [P_{P} - c]D_{P}$ </td><td> $\pi_{P} = [P_{S} - (1 + \beta_{S})c]D_{S}$ </td><td>0</td></tr><tr><td>Utility function for user of type  $v$ </td><td> $U_{P}(v) = A + \theta q_{P} - v - P_{P}$ </td><td> $U_{S}(v) = A + \theta(1 - q_{P}) - (1 + \beta_{S})v - P_{S}$ </td><td> $U_{O}(v) = A + \theta(1 - q_{P}) - 2v$ </td></tr><tr><td colspan="4">* Users of OSS benefit from overall installation base of this type of software, irrespective of whether the users install the commercial open source version or the free open source version.</td></tr></table>

$$
D _ {O} ^ {*} = \left(\frac {\beta_ {S} - 3 \theta}{3 + \beta_ {S} - 8 \theta}\right) + \left(\frac {3 + \beta_ {S} + 4 \theta (1 + \beta_ {S})}{(3 + \beta_ {S} - 8 \theta) (1 - \beta_ {S})}\right) c.\tag{3c}
$$

It should be noted at this point that the equilibrium values are constrained by $0 \leq \beta _ { s } <$ $1 , 0 \leq \Theta \leq 1$ and the values of c that result in positive profits. In order to simplify the analysis, we will look at scenarios representing two broad categories of software. These software categories are differentiated by the strength of network effects (θ); that is, for $\theta = 0$ (very weak or no direct network effects present) and $\theta = 1$ (high direct network effects present). For instance, when there are standards that allow multiple software (in the same category) to interoperate, the network affects the entire user population of these software, resulting in a low value of θ for individual software users. This is true for software such as server operating systems (e.g., Linux, Windows NT) and Web servers (e.g., Apache, MS IIS). In these software markets there are extremely strong market pressures to interoperate with preexisting or most widely accepted standards. Another instance when network effect is not strong is when the software is a stand-alone application such as a CD writer, antivirus, or personal firewall. The major part of the value derived from the use of these software tools is independent of the number of other users of these software applications. Although there are some indirect network effects present (e.g., a large installation base could result in a better support network), these are assumed to be weak and are ignored. On the other hand, in software markets where the competing products are based on proprietary standards and protocols, we are likely to see strong network effects playing a significant role in defining the competition. A good example is that of office productivity applications where MS Office users benefit from its large installation base. Table 3 illustrates this classification of software markets by providing relevant examples in each category. The equilibrium statistics for the two scenarios are given in Table 4.

## Market for Software Characterized by

## Weak Network Effects $( \Theta = 0 )$

Analysis of the equilibrium statistics (Table 4) for software characterized by weak network effects leads to the following propositions:

Proposition 1: For software that displays weak network effects $( i . e . , \ 0 = 0 )$ equilibrium price charged by the PS vendor is always more than that charged by the OSS-SS vendor.

Proof: If we compare the equilibrium prices when $\theta = O \left( T a b l e \mathcal { 4 } \right)$ , we have

$$
P _ {P} ^ {*} (\theta = 0) > P _ {S} ^ {*} (\theta = 0) \Rightarrow \frac {2 \beta_ {S}}{3 + \beta_ {S}} + c \frac {\beta_ {S} (1 - \beta_ {S})}{3 + \beta_ {S}} + c \Rightarrow \beta_ {S} (1 + \beta_ {S} ^ {2}) > 0.
$$

Because $O < \beta _ { s } < I , \beta _ { s } ( I + \beta _ { s } ^ { 2 } ) > O$ is always true. Therefore, $P _ { _ P } { } ^ { * } ( \Theta = { \cal O } ) >$ $P _ { s } ^ { * } ( \Theta = O )$ is true.

Table 3. Software Market Classification Based on Network Effects

<table><tr><td>Example: strength of network effects low</td><td>Example: strength of network effects high</td></tr><tr><td>Desktop stand-alone single-user applications (e.g., PC diagnostic tools, single-player PC games, personal firewalls, CD writers, Web browsers such as Firefox and Explorer, e-mail clients such as Thunderbird and Outlook).Infrastructure software based on universally accepted standards and protocols (e.g., Web servers such as Apache and IIS, DNS servers such as BIND, and e-mail servers)</td><td>Desktop office productivity software (e.g., MS Office)*Database servers (e.g., Oracle, MySQL)Network operating systems (e.g., Windows 2000, Red Hat Linux, Novell Netware)Desktop operating systems (e.g., Windows XP, SUSE Linux 9)</td></tr></table>

\* The availability of applications such as Google’s office products, which allow users to port their documents to MS Office, act to reduce the strength of direct network benefits associated with MS Office.

This result is evident in markets for software such as server operating systems (e.g., Linux, Windows NT) and Web servers (e.g., Apache, MS IIS), and is illustrated in Figure 1, which shows the effect of the level of (un)usability on the equilibrium prices for PS and OSS-SS. The reason can be explained by the gap in usability of PS and OSS-SS. In the absence of any network effects, usability plays an important role in the decision-making process of potential users. Therefore, the higher gap between the usability of PS and OSS, the larger price premium that the PS vendor can charge.

Proposition 2: When software is characterized by weak network effects (i.e., $\theta = O ) ,$ , the OSS-SS vendor is better off having lower usability than the competing PS when $c \leq I / 3$

Proof: Differentiating

$$
P _ {S} ^ {*} (\theta = 0) = \frac {\beta_ {S} (1 - \beta_ {S})}{3 + \beta_ {S}} + c
$$

(see Table 4) with respect to $\beta _ { s }$ and equating it to zero gives

$$
\frac {d P _ {S} ^ {*} (\theta = 0)}{d \beta_ {S}} = \frac {3 - 6 \beta_ {S} - \beta_ {S} ^ {2}}{(3 + \beta_ {S}) ^ {2}} = 0 \Rightarrow \beta_ {S} ^ {*} = (2 \sqrt {3} - 3, - 2 \sqrt {3} - 3).
$$

The second derivative of $P _ { s } ^ { * } ( \Theta = { O } )$ at ${ \beta } _ { s } ^ { * } = 2 \sqrt { 3 } - 3$ is negative. Therefore, the $P _ { s } ^ { * } ( \Theta = O )$ maximizing value of $\Upsilon _ { s } ^ { ~ * } i s 2 \sqrt { 3 } - 3 = 0 . 4 6$ (see Figure 1), which is more than zero, implying that the OSS-SS vendor can charge maximum price only when

<sub>Equilibriu</sub>m <sup>Statistics</sup> <sup>for</sup> <sup>Scenario</sup>

<table><tr><td></td><td>Demand*</td><td>Price*</td><td>Profit*</td></tr><tr><td colspan="4">Equilibrium statistics for scenario 1 (i.e., when θ = 0)</td></tr><tr><td>PS vendor</td><td> $D_P^* = \frac{2}{(3 + \beta_S)}$ </td><td> $P_P^* = \frac{2\beta_S}{3 + \beta_S} + c$ </td><td> $\pi_P^* = \left[ \frac{4\beta_S}{(3 + \beta_S)^2} \right]$ </td></tr><tr><td>OSS-SS vendor</td><td> $D_S^* = \frac{1}{(3 + \beta_S)} - \frac{c}{(1 - \beta_S)}$ </td><td> $P_S^* = \frac{\beta_S(1 - \beta_S)}{(3 + \beta_S)} + c$ </td><td> $\pi_S^* = \left[ \frac{1}{(3 + \beta_S)} - \frac{c}{(1 - \beta_S)} \right] \left[ \left( \frac{\beta_S(1 - \beta_S)}{3 + \beta_S} \right) - \beta_S c \right]$ </td></tr><tr><td>OSS</td><td> $D_O^* = \frac{\beta_S}{(3 + \beta_S)} + \frac{c}{(1 - \beta_S)}$ </td><td>Zero</td><td>Zero</td></tr></table>

![](/api/attachments/AG5RSMTZ/fulltext/images/2b5ff92b4d543d08ce0eb286ef9455d9e33c697c09d7d0b04de5067e692abecd.jpg)  
<sub>u</sub>m <sup>statistics</sup> <sup>for</sup> <sup>scenario</sup> <sup>2</sup> <sup>(i.e.,</sup> <sup>whe</sup>

![](/api/attachments/AG5RSMTZ/fulltext/images/a3692089c46afce9f1bd3c98b47d8f0ac614594b03075b2a06b78e170e6fc28a.jpg)  
Figure 1. Equilibrium Software Prices (assume c = 0.05)

OSS-SS is about half as usable as PS. Similarly, we find that the optimal value of $\beta _ { s }$ that maximizes the OSS-SS vendor’s profit is

$$
\beta_ {S} ^ {*} = \frac {2 \sqrt {1 + 2 4 c} - 3 c - 5}{c - 7}
$$

(see Figure 2).<sup>4</sup> This $\beta _ { s } ^ { * }$ is greater than zero for $c \leq I / 3 , ^ { s }$ implying that the OSS-SS vendor is better off producing software that is more usable than OSS but less usable than its PS competition. This strategy is evident in the case of Linux servers, where we find that the commercial versions of the server operating system are more usable than the freely available versions [25]. However, they have yet to achieve the usability levels of the competing Windows NT operating system.

The level of software usability is controlled by the software vendor. This leads to the obvious question: What is the profit-maximizing optimal usability of OSS-SS relative to its PS competition? By improving software usability, or reducing $\beta _ { s } ,$ the OSS-SS vendor can reduce its total cost associated with each unit of OSS-SS sold and therefore increase its profit. Thus the intuitive answer to our question is that the OSS-SS vendor should ensure that ${ \beta } _ { s } = 0$ . However, we find that the OSS-SS vendor is better off producing software that has lower usability than the competing PS as long as the cost associated with each unit of OSS-SS is less than 0.33. This is an interesting result because it provides an economic rationale for the relatively poor usability of OSS-SS, which is considered a major limitation of OSS (e.g., [11, 31]). The result shows that if OSS-SS is as usable as PS, then both vendors are forced to compete at marginal cost and end up making zero profit (see Figure 1 where at $\theta = 0$ and $\beta _ { s } = 0 , P _ { s } = P _ { { } _ { P } } = c )$ Therefore, the OSS-SS vendor is better off making its software less usable than PS.

Proposition 3: When the competing software are characterized by weak network effects $( i . e . , \theta = O )$ , the market share of PS is always higher than that of OSS-SS (see Figure 3).

OSS-SS Profits

![](/api/attachments/AG5RSMTZ/fulltext/images/b0c283b5b6b242eaff56e04d93f818a23c7fe8e85725efb40cef9a707afb4ae0.jpg)  
Figure 2. Equilibrium Profits for OSS-SS When Software Is Characterized by Weak Network Effects (assume $\mathrm { c } = 0 . 0 5 )$ )

Proof: We compare the equilibrium demand for PS and OSS-SS at $\theta = O ( T a -$ ble 4):

$$
\frac {2}{3 + \beta} > \frac {1}{3 + \beta} - \frac {c}{1 - \beta} = > \frac {1}{3 + \beta} + \frac {c}{1 - \beta} > 0.
$$

This inequality is always true because $I / ( 3 + \beta ) + c / ( I - \beta )$ is always positive for $c > 0$ and $O \le \beta < I$

This is an interesting result in light of the fact that an increasing number of firms have already entered or are planning to enter software markets in various categories as OSS-SS vendors. Our analysis shows that the OSS-SS will not dominate the PS in terms of market share if they are competing in software markets characterized by weak network effects. This result does not imply that PS will always have more market share than its open source alternative. In fact, as the usability of OSS-SS decreases, freely available OSS’s share of the market increases. As a result, PS is also forced to compete with OSS, resulting in a loss of some market share to OSS. When OSS-SS and OSS are similar in terms of usability, the increase in the market share for OSS is enough to make it the dominant player in the software market (see Figure 2). However, the market share of OSS-SS per se still remains below that of PS. This result provides a possible explanation of why the infrastructure software (e.g., Web servers, DNS servers, e-mail servers, etc.) market is dominated by OSS such as Apache and BIND and why we do not find many OSS-SS vendors in this software category. The infrastructure software market consists of software based on well-established communication standards, resulting in weak network benefits. In addition, the potential users of infrastructure software are highly skilled software professionals such as systems administrators and network administrators. For these users, usability is not a major concern [31]. As a result, we see that the few remaining PS vendors in the infrastructure-software market are fast losing their once dominant market position to open source alternatives. For instance, Apache enjoys about 69 percent of the Web server market while IIS by Microsoft lags far behind with about 21 percent market share (www.serverwatch.com/stats/article. php/3487716); and in the market for DNS servers, the open source option BIND is the predominantly named server on the Internet.

![](/api/attachments/AG5RSMTZ/fulltext/images/261743530f5ef1aa0643e4f4e0af934586760c7e2fa7e5f554b09897b8762a6b.jpg)  
Figure 3. Equilibrium Software Demand (assume c = 0.05)

## Market for Software Characterized by Strong

## Network Effects (θ = 1)

Analysis of the equilibrium statistics (Table 4) for software markets characterized by strong network effects leads to the following:

Proposition 4: When software is characterized by high network effects $( i . e . , \theta =$ 1), the equilibrium prices for PS are higher than the equilibrium prices for OSS-SS when $0 < c < 0 . 2$ and

$$
\beta_ {S} <   \frac {1}{2} \left[ 3 (1 + 2 c) - \sqrt {1 + 7 6 c + 3 6 c ^ {2}} \right].
$$

Proof: $H$ we compare the equilibrium prices when $\theta = I ( T a b l e 4 )$ , we have

$$
P _ {P} ^ {*} (\theta = 1) > P _ {S} ^ {*} (\theta = 1) \Rightarrow \frac {1 - \beta_ {S} - (3 + \beta_ {S}) c}{\beta_ {S} - 5} > \frac {(1 - \beta_ {S}) (\beta_ {S} - 3) + (7 + 5 \beta_ {S}) c}{\beta_ {S} - 5},
$$

which gives $\beta _ { s } ^ { 2 } - 3 \beta _ { s } ( l + 2 c ) + 2 ( l - 5 c ) > 0 .$ . This inequality is true when<sup>6</sup> $c > 0$ and

$$
\beta_ {S} <   \frac {1}{2} \left[ 3 (1 + 2 c) - \sqrt {1 + 7 6 c + 3 6 c ^ {2}} \right].
$$

Furthermore,

$$
\beta_ {s} <   \frac {1}{2} \bigg [ 3 (1 + 2 c) - \sqrt {1 + 7 6 c + 3 6 c ^ {2}} \bigg ]
$$

is valid $( i . e . , O < \beta _ { s } < I )$ only when $\begin{array} { r } { O < c < 0 . 2 . } \end{array}$ . Therefore, as long as $\theta < c <$ 0.2 and

$$
\beta_ {S} <   \frac {1}{2} \left[ 3 (1 + 2 c) - \sqrt {1 + 7 6 c + 3 6 c ^ {2}} \right],
$$

$$
P _ {P} ^ {*} (\theta = 1) > P _ {S} ^ {*} (\theta = 1).
$$

This result implies that as the cost of operations $( \mathrm { i } . \mathrm { e } . , c )$ increases, the upper limit $\beta _ { s }$ decreases. In other words, as c approaches 0.2, $P _ { _ P } ^ { \ast } ( \Theta = 1 ) > P _ { _ S } ^ { \ast } ( \Theta = 1 )$ even when the usability gap between PS and OSS-SS is not significant. For example, at $c = 0 . 1 5$ 8 $P _ { _ P } ^ { ^ \ast } ( \Theta = 1 ) > P _ { _ S } ^ { ^ \ast } ( \Theta = 1 )$ as long as $0 < \beta _ { s } < 0 . 1 3$ . As we can see, the upper limit for $\beta _ { s }$ is quite low (i.e., OSS-SS is usable), suggesting that the usability gap between OSS-SS and the competing PS is not significant. On the other hand, at lower values of $^ { c , }$ the upper limit for $\beta _ { s }$ is relatively high. Therefore, $P _ { _ P } ^ { ^ \ast } ( \Theta = 1 ) > P _ { _ S } ^ { ^ \ast } ( \Theta = 1 )$ as long as there is a usability gap between PS and OSS-SS. This result is evident in the lower prices of commercial open source desktop operating systems (e.g., Red Hat Linux) in comparison to the price charged by the PS option (e.g., Windows). Traditionally, OSS-SS desktop operating systems have been perceived to be less usable than the competing PS [31], and therefore the PS vendor could charge a higher price for its product. Recently, however, there have been improvements in the usability of Linux [25]. However, the Windows desktop operating system still costs more, as suggested by P4.

Proposition 5: When the software market consists of PS, OSS-SS, and OSS options, and the software displays strong network benefits $( i . e . , \theta = I ) ,$ , the demand for PS and OSS-SS increases with a decrease in the usability of OSS-SS, while the demand for OSS decreases with a decrease in the usability of OSS-SS (see Figure 3).

While one would expect the demand for PS to increase as the usability of OSS-SS decreases, what is counterintuitive is the result that the demand for OSS-SS also increases with a decrease in its usability. The OSS-SS demand increases even with a decrease in its usability because (1) with reduced usability (in comparison to PS), its equilibrium price goes down, making it more attractive to consumers with low valuation of usability, and (2) OSS-SS users get the significant network benefits associated with the user base of both OSS-SS and OSS users.

Proposition 6: In a software market characterized by strong network effects, profit for the OSS-SS vendor is maximized at ${ \beta } _ { s } ^ { * } = { \cal O } ,$ and it decreases with a decrease in the usability of OSS-SS (i.e., for $O < \beta _ { s } ^ { * } < I )$

The optimal unusability for OSS-SS is ${ \beta } _ { s } ^ { * } = 0 ;$ that is, the usability of OSS-SS is similar to that of PS. At this level of usability, the OSS-SS vendor not only maximizes its profits, it also forces the PS vendor out of the software market because $\pi _ { _ P } ^ { ^ \ast } ( \beta _ { s } ^ { ^ \ast } =$ $0 ) < 0$ . Therefore, in these markets, the PS vendor can survive only by continuously keeping ahead of the OSS-SS in terms of usability.

## Discussion

## The Worst-Case Scenario for PS and OSS-SS Vendors

THE WORST-CASE SCENARIO FOR BOTH THE PS AND OSS-SS VENDORS is when OSS is as usable as PS and OSS-SS. In such a scenario, there is no incentive for the PS and the OSS-SS vendor to enter the software market. The OSS-SS vendor stays away because it faces zero demand when it competes against freely available and similarly usable OSS. On the other hand, both PS and OSS will have a positive demand. However, the equilibrium price for PS is not enough to cover the marginal cost of selling the software, resulting in negative profits for the PS vendor (see Appendix B). This will result in the exit of the PS vendor from the software market. Therefore, both PS and OSS-SS vendors have little incentive to improve the usability of freely available OSS. However, such a scenario begs an important question: What is the likelihood that the usability of OSS is comparable to that of PS? For this to happen, the developers involved with the OSS project will have to give as much importance to the usability of the application as to its utility or functionality. They will have to develop and enhance user-friendly interfaces and features for the OSS application. Although theoretically possible, a realistic assessment of OSS projects shows that this is not likely to happen soon. OSS application developers have traditionally favored function over form, which is evident in the lack of user-friendly features such as intuitive GUIs in these applications, and there is no evidence that this is changing [31]. One reason for this is that in most open source projects, the developers of OSS applications are also its core users [26]. For these developer-users, the usability of OSS is not a major concern because they are highly skilled software professionals and have access to the OSS code. Therefore, they have the ability to modify the software in accordance with their usability requirements. In addition, most OSS developers work under a license that prevents them from selling the code, so they develop features that are important to them and not necessarily to the market. Finally, there is hardly any mechanism to capture the feedback of average users who are not involved with the OSS application development process, but are most in need of user-friendly features. Therefore, we can safely assume that the likelihood of OSS usability matching that of PS or OSS-SS is very low.

## How Can Commercial PS Producers Compete Against OSS?

This is the key question that we posed at the beginning of this paper. In this study, we divide the software markets into two broad categories—those that are characterized by strong network effects and those that are characterized by weak network effects. A PS vendor needs to identify the software market that it is competing in and act accordingly.

![](/api/attachments/AG5RSMTZ/fulltext/images/707b60a5c4fd914ac6b8e9834c4133c805b2a4f546514e19d0bd5d900cb7b06d.jpg)  
Figure 4. Equilibrium Profits for PS When Software Is Characterized by Weak Network Effects (assume c = 0.05)

If PS is competing in software markets with strong network benefits, then it will remain an important player in the software market as long as OSS and OSS-SS remain highly unusable relative to the PS (see Figures 1 and 3). This makes the software markets such as desktop office productivity applications and desktop operating systems attractive for PS vendors. Furthermore, a PS vendor can improve its competitive position by ensuring that its software continues to remain highly usable in comparison to OSS-SS and OSS. In addition, it needs to ensure very low usability in freely available OSS. It can do so by participating in OSS projects and by encouraging the developers of OSS to focus their development efforts only on functionality and reliability of OSS. If the OSS becomes as usable as OSS-SS, then the OSS-SS vendor is forced to improve its own usability or exit the market (see Appendix C). If the OSS-SS vendor decides to improve its usability further, then all software end up with the same usability, resulting in negative profits for PS, and no demand for OSS-SS (see Appendix B).

If the PS vendor is competing in software markets characterized by weak network effects, then the presence of OSS-SS actually helps the PS vendor make more profits (see Figure 4). This is an interesting result because it identifies the condition under which the presence of the OSS-SS vendor actually helps the competitive position of the PS vendor. To ensure that the OSS-SS vendor remains in the market, the PS vendor has to take steps that result in OSS with poor usability. If OSS continues to improve in terms of usability, then OSS-SS has two options—to improve its usability further in relation to OSS or to exit the market (see Appendix C). If the OSS-SS decides to improve its usability, it is constrained by the relationship between its usability and profitability (see Figure 2; P2), which ensures that the OSS-SS is never as usable as PS (because OSS-SS profits are maximized at

$$
\beta_ {S} ^ {*} = \frac {2 \sqrt {1 + 2 4 c} - 3 c - 5}{c - 7}
$$

and $c \leq 1 / 3 )$ . If the OSS continues to improve its usability, it will eventually catch up with the OSS-SS, and the OSS-SS vendor will be forced to exit the software market (see Appendix C), which is not good for the PS vendor (Figure 4). However, if the usability of the OSS remains very low, the PS has the best usability, and the OSS-SS has usability corresponding to

$$
\beta_ {S} ^ {*} = \frac {2 \sqrt {1 + 2 4 c} - 3 c - 5}{c - 7},
$$

all three types of software exist in the market.

## How Can OSS-SS Vendors Compete Against Well-Established PS?

OSS-SS vendors who sell usable OSS plus support services face a very competitive environment. On one hand, they have to compete with the highly usable PS option and, on the other hand, they have to compete with freely available OSS. To compete successfully, the OSS-SS vendor needs to benchmark its usability against the competing PS. If it is competing in a software market characterized by weak network effects, then it is better off ensuring that the OSS-SS is highly usable compared to the OSS, but not as usable as the competing PS (see Figures 1 and 2; P2). On the other hand, if the OSS-SS is competing in software markets characterized by high network effects, then it needs to offer a product that is at least as usable as the competing PS, thereby forcing the competing PS vendor to exit the software market (P6). OSS-SS vendors also need to keep in mind that users differentiate between OSS and OSS-SS mainly on the basis of usability. If OSS starts to become more usable, then OSS-SS vendors lose this strategic advantage. Therefore, OSS-SS vendors need to ensure that the “free” OSS is not as usable as PS or OSS-SS. This can be achieved by actively participating in relevant open source projects and influencing the direction of the project by focusing the development efforts toward improving software functionality and reliability. In addition, they should provide a highly usable version of OSS only if the users also buy the support services. For instance, some OSS-SS vendors continue to provide highly usable versions of relevant OSS for “free” (e.g., SUSE 9 by Novell is a highly usable Linux version for desktops and it is available for free download). This strategy will have an adverse impact on their market shares and profitability in relevant software markets (see Appendix B).

## Conclusion

THIS PAPER PROPOSES AN ANALYTICAL MODEL to study the competition between commercial software and OSS. The main results obtained after analyzing the model are summarized in Table 5.

Table 5. Threat from OSS, OSS-SS, and PS Vendor’s Strategic Options

<table><tr><td rowspan="2">Usability of commercial open source software(OSS-SS)</td><td colspan="2">Strength of network effects</td></tr><tr><td>Scenario 1 (low)</td><td>Scenario 2 (high)</td></tr><tr><td>Low</td><td>OSS dominates PS in terms of market share. In this segment, the dominance of noncommercial OSS is evident in infrastructure software segment (e.g., Web servers, DNS servers, e-mail servers).Managerial implications for PS vendor: Encourage the entry of OSS-SS, and participate in OSS projects to ensure that OSS has lower usability than the OSS-SS.</td><td>Currently, PS has the dominant market share in this software segment (e.g., Windows desktop operating system versus Linux desktop version).Managerial implications for PS vendor: PS can remain competitive by ensuring that it remains more usable than OSS and OSS-SS.</td></tr><tr><td>High</td><td>In this segment, OSS-SS and OSS will emerge as major alternatives to PS (e.g., personal firewalls, Web browsers, e-mail clients).Managerial implications for PS vendor: Encourage the entry of OSS-SS, and remain more usable than OSS-SS.</td><td>We have yet to see a commercial version of open source in this software category that is as usable as the PS. Therefore, we have yet to see any competition in this segment. However, we should expect OSS-SS to dominate this segment if it closes the usability gap with PS.Managerial implications for PS vendor: PS can remain competitive by ensuring that it remains more usable than OSS and OSS-SS.</td></tr></table>

There are several types of software available today. We are already familiar with the proprietary closed source software. In the past decade or so, we have seen the emergence of free closed source software (e.g., shareware applications), free OSS, and OSS-SS. More recently, we have been witnessing the introduction of Internetbased software applications that can be closed or open source, and a combination of free and commercial components (e.g., Web 2.0 applications, Web services). In order to explain the competition between these various types of software, we can either develop models specific to software characteristics or propose more generic models that can be applied (with minor modifications) to most software markets. The model proposed in this paper is generic in nature because, irrespective of the software category (e.g., desktop application, systems software, enterprise applications, etc.) and type of potential users (i.e., individuals, organizations, system administrators, programmers, etc.), the users’ choices are decided on the basis of factors such as their needs, the perceived value offered by various options, and total cost of software ownership. The model proposed in this paper incorporates these factors. For instance, software category is controlled for by assuming that competing software have the required functionality and reliability, and whether they offer weak or strong network benefits; perceived value from the software is represented by the users’ utility functions; and the cost of ownership is represented by the price paid by the potential users. Thus the proposed general utility model captures the essential decision variables (although in an aggregate form) that determine a user’s choice of software, and provides us with some significant insights about the impact of this decision on the market structure of the software industry.

Like most analytical models, the proposed model also has its limitations. One limitation of the model is that OSS-SS and OSS are assumed to be compatible with any existing software that may be required to run in conjunction with them. However, this is not a serious limitation for the simple reason that most OSS are late entrants to the market, which already consists of the PS and its complementary/supplementary products. In order to attract users in this market, the OSS will have to be compatible with these existing complementary/supplementary products. This was the case with Linux and most other OSS. In fact, Linux now allows users to emulate Windows on a Linux machine. Another limitation of the model is that the assumptions about users choice between the PS and OSS are straightforward—that is, choice is influenced by the software price, software usability, and expected installation base. Although this simplicity is important for a flexible yet robust model, it is important to acknowledge that users’ choice of software is guided by more complex heuristics as suggested in technology adoption literature. Incorporating these to develop a more rich and realistic mathematical model should be undertaken in future research. Finally, the model does not take into account some additional benefits offered by OSS—that is, access to the software code and the freedom to modify the software. However, few people except developers or code reviewers need direct access to source code. In fact, most users do not even participate in the development of OSS, and the major part of the software development is done by a relatively small number of people [22]. In most instances, even the “power users,” such as developers and systems administrators, have other full-time jobs and responsibilities, and as a result, they do not want to spend time to modify an OSS, fix a bug in the software, or tailor it to their own unique needs. They are just looking for a software (open source or otherwise) that meets their functional requirements. Therefore, this limitation in the model is not significant in the context of most software users.

Finally a cautionary note: the proposed model variables should be interpreted in the proper context to get meaningful interpretations of the results. For example, even though the model does not differentiate between the type of software (e.g., desktop application and network operating systems), its results should still qualify as long it is applied to study the competition between the same categories of software—that is, they address the same functional needs of the users and display similar network effects.

## NOTES

1. Some of these end users could be involved as beta testers, but they do not contribute any code to the software.

2. This paper assumes that PS, OSS-SS, and OSS to be equally reliable because there is a lack of consensus about which form of software is more secure—PS or OSS (e.g., [40]).

3. For instance, highly skilled and experienced software users might not place as much emphasis on software usability as those users who are relatively less skilled or experienced in the use of software.

4. Differentiate $\pi _ { \mathrm { { s } } } ^ { * } ( \Theta = 0 )$ with respect to $\beta _ { s }$ and equate the resulting derivative to zero.

5. Other values of $\beta _ { s } ^ { * } ( \theta = 0 )$ are either outside the range of [0, 1] or result in minimal profits.

6. We ignore those solution in which $c < 0$ and $\beta _ { s } < 0 \mathrm { o r } \beta _ { s } > 1$

## REFERENCES

1. Adams, D.A.; Nelson, R.R.; and Todd, P.A. Perceived usefulness, ease of use, and usage of information technology: A replication. MIS Quarterly, 16, 2 (June 1992), 227–247.

2. Bagozzi, R., and Dholakia, U. Open source software user communities: A study of participation in Linux user groups. Management Science, 42, 7 (July 2006), 1099–1115.

3. Bessen, J. What good is free software? In R. Hahn (ed.), Government Policy Towards Open Source Software. Washington, DC: AEI Brookings Joint Center for Regulatory Studies, 2002 (available at www.aei.brookings.org/admin/authorpdfs/page.php?id=212).

4. Casadesus-Masanell, R., and Ghemawat, P. Dynamic mixed duopoly: A model motivated by Linux vs. Windows. Management Science, 42, 7 (July 2006), 1072–1084.

5. Crowston, K., and Scozzi, B. Open source software projects as virtual organizations: Competency rallying for software development. IEE Proceedings Software, 149, 1 (2002), 3–17.

6. Davis, F.D. Perceived usefulness, perceived ease of use and user acceptance of information technology. MIS Quarterly, 13, 3 (September 1989), 319–340.

7. DeLone, W.H., and McLean, E.R. The DeLone and McLean model of information systems success: A ten-year update. Journal of Management Information Systems, 19, 4 (Spring 2003), 9–30.

8. Economides, N., and Katsamakas, E. Linux vs. Windows: A comparison of application and platform innovation incentives for open source and proprietary software platforms. Law and Economics Research Paper No. 05-21, New York University, October 2005 (available at http://ssrn.com/abstract=822894).

9. Farrell, J., and Saloner, G. Standardization, compatibility, and innovation. Rand Journal of Economics, 16, 1 (Spring 1985), 70–83.

10. Farrell, J., and Saloner, G. Installed base and compatibility: Innovation, product pronouncements, and predation. American Economic Review, 76 (December 1986), 940–955.

11. Frishberg, N.; Dirks, A.M.; Benson, C.; Nickell, S.; and Smith, S. Getting to know you: Open source development meets usability. In CHI 2002. New York: ACM Press, 2002, pp. 932–933 (available at http://delivery.acm.org/10.1145/510000/506666/p932-frishberg.pdf?ke y1=506666&key2=1429429711&coll=&dl=&CFID=15151515&CFTOKEN=6184618).

12. Gaudeul, A. The LaTeX project: A case study of open-source software. TUGBoat, 24, 1 (2003), 1001–1015.

13. Green, E.L. Economics of open source. December 6, 2002 (available at http://badtux. org/home/eric/editorial/economics.php).

14. Hartwick, J., and Barki, H. Explaining the role of user participation in information system use. Management Science, 40, 4 (December 1994), 440–465.

15. Hughes, J., and Lang, K.R. Open source culture and digital remix: A theoretical framework. McCombs School of Business, University of Texas at Austin, April 14, 2006 (available at www.mccombs.utexas.edu/events/osworkshop/Open%20Source%20Culture%20and%20 Digital%20Remix%20JMIS%202006.doc.pdf).

16. Johnson, J.P. Economics of open source software. Journal of Economics and Management Strategy, 11, 4 (2002), 637–662.

17. Kankanhalli, A.; Tan, C.Y.; and Wei, K. Conflict and performance in global virtual teams. Journal of Management Information Systems, 23, 3 (Winter 2006–7), 237–274.

18. Karahanna, E.; Straub, D.W.; and Chervany, N.L. 1999. Information technology adoption across time: A cross-sectional comparison of pre-adoption and post-adoption beliefs. MIS Quarterly, 23, 2 (June 1999), 183–213.

19. Katz, M., and Shapiro, C. Technology adoption in the presence of network externalities. Journal of Political Economy, 94, 4 (August 1986), 822–841.

20. Katz, M., and Shapiro, C. Antitrust in software markets. In J. Eisenach and T. Lenard (eds.), Competition, Innovation and the Microsoft Monopoly: Antitrust in the Digital Marketplace. Boston: Kluwer Academic Publishers, 1999, 29–82.

21. Koch, C. Your open source plan. CIO (March 15, 2003) (available at www.cio.com. au/index.php/id;219455497).

22. Krishnamurthy, S. Cave or community? An empirical examination of 100 mature open source projects. First Monday, 7, 6 (June 2002) (available at www.firstmonday.org/issues/issue7\_6/krishnamurthy/).

23. Lederer, A.L.; Maupin, D.J.; Dena, M.P.; and Zhuang, Y. The technology acceptance model and the Worldwide Web. Decision Support Systems, 29, 3 (October 2000), 269–282.

24. Lerner, J., and Tirole, J. Some simple economics of open source. Journal of Industrial Economics, 50, 2 (June 2002), 197–234.

25. Manes, S. Linux gets friendlier. Forbes (June 10, 2002), 134–136.

26. Mockus, A.; Fielding, R.; and Herbsleb, J. A case study of open source software: The Apache server. In Proceedings of the Twenty-Second International Conference on Software Engineering. New York: ACM Press, 2002, pp. 263–272.

27. Moon, J.Y., and Sproull, L. Essence of distributed work: The case of the Linux kernel. First Monday, 5, 11 (2000) (available at www.firstmonday.org/issues/issue5\_11/moon/).

28. Moore, G.C., and Benbasat, I. Development of an instrument to measure the perceptions of adopting an information technology innovation. Information System Research, 2, 3 (September 1991), 192–222.

29. Mustonen, M. Copyleft—The economics of Linux and other open source software. Information and Economics Policy, 15, 1 (2003), 99–121.

30. Nelson, M.; Sen, R.; and Subramanium, C. Understanding open source software development—A research classification framework. Communications of the AIS, 17, 12 (February 2006), 266–287.

31. Nichols, D.M., and Twidale, M.B. The usability of open source software. First Monday, 8, 1 (January 2003) (available at www.firstmonday.org/issues/issue8\_1/nichols/).

32. Nielsen, J. Usability Engineering. Boston: Academic Press, 1993.

33. Raymond, E.S. The Cathedral and Bazaar. Sebastopol, CA: O’Reilly, 2000.

34. Roberts, A.J.; Hann, I.; and Slaughter, S. Understanding the motivations, participation, and performance of open source software developers: A longitudinal study of the Apache project. Management Science, 42, 7 (July 2006), 984–999.

35. Rogers, E.M. Diffusion of Innovations. New York: Free Press, 1995.

36. Shah, S. Motivation, governance, and the viability of hybrid forms in open source software development. Management Science, 52, 7 (July 2006), 1000–1014.

37. Tirole, J. The Theory of Industrial Organization. Cambridge, MA: MIT Press, 2000. 38. Venkatesh, V., and Davis, F.D. Theoretical extension of the technology acceptance model:

39. Venkatesh, V., and Morris, M.G. Why don’t men ever stop to ask for directions? Gender, social influence, and their role in technology acceptance and usage behavior. MIS Quarterly, 24, 1 (March 2000), 115–139.

40. Viega, J. Open source security: Still a myth. O’Reilly Network, September 2004 (available at www.oreillynet.com/pub/a/security/2004/09/16/open\_source\_security\_myths.html).

## Appendix A. Equilibrium Demand, Prices, and Profits

CONSUMERS OF TYPE v purchase one unit of software that offers them the most utility. This gives the following demand:

$$
D _ {P} = 1 - \frac {P _ {P} - P _ {S}}{\beta_ {S}} - \frac {\theta (1 - 2 q _ {P})}{\beta_ {S}}.
$$

In a symmetric fulfilled-expectation Nash equilibrium, $q _ { P } = D _ { P ^ { ' } }$ . Therefore,

$$
D _ {P} = 1 - \frac {P _ {P} - P _ {S}}{\beta_ {S}} - \frac {\theta (1 - 2 D _ {P})}{\beta_ {S}} \Rightarrow D _ {P} = \frac {\beta_ {S} - P _ {P} + P _ {S} - \theta}{\beta_ {S} - 2 \theta}\tag{A1a}
$$

$$
D _ {S} = \frac {P _ {P} - \theta}{\beta_ {S} - 2 \theta} - \frac {1 - 2 \theta}{(\beta_ {S} - 2 \theta) (1 - \beta_ {S})} P _ {S}\tag{A1b}
$$

$$
D _ {O} = \frac {P _ {S}}{1 - \beta_ {S}}.\tag{A1c}
$$

Profit made by the PS vendor is

$$
\pi_ {P} = \left[ \frac {\beta_ {S} - \theta - P _ {P} + P _ {S}}{\beta_ {S} - 2 \theta} \right] \left[ P _ {P} - c \right]\tag{A2a}
$$

Differentiating $\pi _ { { } _ { P } }$ with respect to $P _ { \scriptscriptstyle P }$ and equating it to zero gives the profit-maximizing price:

$$
P _ {P} = \frac {1}{2} \left[ \beta_ {S} + c - \theta + P _ {S} \right].\tag{A2b}
$$

Similarly, the demand for OSS-SS is

$$
\frac {P _ {P} - \theta}{\beta_ {S} - 2 \theta} - \frac {1 - 2 \theta}{(\beta_ {S} - 2 \theta) (1 - \beta_ {S})} P _ {S},
$$

and profit made by the OSS-SS vendor is

$$
\pi_ {S} = \left[ \frac {P _ {P} - \theta}{\beta_ {S} - 2 \theta} - \frac {1 - 2 \theta}{(\beta_ {S} - 2 \theta) (1 - \beta_ {S})} P _ {S} \right] \left[ P _ {S} - (1 + \beta_ {S}) c \right].\tag{A3a}
$$

Differentiating $\pi _ { d }$ with respect to $P _ { d }$ and equating it to zero gives the profitmaximizing price:

$$
P _ {S} = \frac {1}{2 (1 - 2 \theta)} \left[ (1 + \beta_ {S}) (1 - 2 \theta) c + (1 - \beta_ {S}) P _ {P} - \theta (1 - \beta_ {S}) \right].\tag{A3b}
$$

Solving for $P _ { _ P }$ and $P _ { s }$ from Equations (2b) and (3b) gives the optimal prices for PS and OSS-SS as follows:

$$
P _ {P} ^ {*} = \left(\frac {2 (1 - 2 \theta) (\beta_ {S} - \theta) + (1 - 2 \theta) (3 + \beta_ {S}) c - \theta (1 - \beta_ {S})}{3 + \beta_ {S} - 8 \theta}\right)\tag{A4a}
$$

$$
P _ {S} ^ {*} = \left(\frac {\big (1 - \beta_ {S} \big) \big (\beta_ {S} - \theta \big) - 2 \theta \big (1 - \beta_ {S} \big) + \Big [ 3 + \beta_ {S} + 4 \theta \big (1 + \beta_ {S} \big) \Big ] c}{3 + \beta_ {S} - 8 \theta}\right).\tag{A4b}
$$

Equilibrium demand for OSS, OSS-SS, and PS, respectively, are as follows:

$$
D _ {P} ^ {*} = \left[ \left(\frac {\beta_ {S} - \theta}{\beta_ {S} - 2 \theta}\right) - \left(\frac {(1 + \beta_ {S} - 4 \theta) (\beta_ {S} - \theta) + \theta (1 - \beta_ {S}) - 2 \theta (5 + 3 \beta_ {S}) c}{(\beta_ {S} - 2 \theta) (3 + \beta_ {S} - 8 \theta)}\right) \right]\tag{A5a}
$$

$$
\begin{array}{c} D _ {S} ^ {*} = \left(\frac {(1 + \beta_ {S} - 4 \theta) (\beta_ {S} - \theta) + \theta (1 - \beta_ {S}) - 2 \theta (5 + 3 \beta_ {S}) c}{(\beta_ {S} - 2 \theta) (3 + \beta_ {S} - 8 \theta)} - \frac {\theta}{(\beta_ {S} - 2 \theta)}\right) \\ - \left(\frac {(\beta_ {S} - \theta) - 2 \theta}{3 + \beta_ {S} - 8 \theta}\right) - \left(\frac {3 + \beta_ {S} + 4 \theta (1 + \beta_ {S})}{(3 + \beta_ {S} - 8 \theta) (1 - \beta_ {S})}\right) c \end{array}\tag{A5b}
$$

$$
D _ {O} ^ {*} = \left(\frac {\left(\beta_ {S} - \theta\right) - 2 \theta}{3 + \beta_ {S} - 8 \theta}\right) + \left(\frac {3 + \beta_ {S} + 4 \theta (1 + \beta_ {S})}{(3 + \beta_ {S} - 8 \theta) (1 - \beta_ {S})}\right) c.\tag{A5c}
$$

## Appendix B. Competition When PS, OSS-SS, and OSS PS

Have the Same High Usability

WHEN PS, OSS-SS, AND OSS PS HAVE THE SAME high usability, the utility functions for consumers are as follows:

$$
U _ {P} (v) = A + \theta q _ {P} - v - P _ {P}\tag{B1a}
$$

$$
U _ {s} (v) = A + \theta (1 - q _ {P}) - v - P _ {s}\tag{B1b}
$$

$$
U _ {o} (v) = A + \theta (1 - q _ {P}) - v.\tag{B1c}
$$

Consumers of type v purchase one unit of software that offers them the most utility. Therefore, OSS-SS has zero demand because users always prefer OSS over it. However, a consumer of type v will prefer PS over OSS if $P _ { { \scriptscriptstyle P } } \leq 6 ( 2 q _ { { \scriptscriptstyle P } } - 1 )$ . Therefore, the profit-maximizing price for the PS vendor is $P _ { _ P } = \Theta ( 2 q _ { _ P } - 1 )$ , and the profit function is given by $\pi _ { { \scriptscriptstyle P } } = D _ { { \scriptscriptstyle P } } [ \Theta ( 2 q _ { { \scriptscriptstyle P } } - 1 ) - c ]$ . In a symmetric fulfilled-expectation Nash equilibrium, $D _ { { P } } = q _ { { P } } ,$ the profits are maximized at $q _ { _ { P } } ^ { \mathrm { ~ * ~ } } = ( \Theta + c ) / 4 \Theta$ . The equilibrium price is given by $\boldsymbol { P } _ { p } ^ { \ast } = 1 / 2 ( \boldsymbol { c } - \boldsymbol { \Theta } )$ . Because ${ P _ { _ P } } ^ { \ast } = 1 / 2 ( c - \theta ) < c .$ , the PS firm does not make any profit.

## Appendix C. Competition When OSS Is as Usable as OSS-SS

WHEN OSS IS AS USABLE AS OSS-SS, utility functions for the consumers are as follows:

$$
U _ {P} (v) = A + \theta q _ {P} - v - P _ {P}\tag{C1a}
$$

$$
U _ {s} (v) = A + \theta (1 - q _ {P}) - (1 + \beta_ {s}) v - P _ {s}\tag{C1b}
$$

$$
U _ {o} (v) = A + \theta (1 - q _ {P}) - (1 + \beta_ {S}) v.\tag{C1c}
$$

Consumers of type v purchase one unit of software that offers them the most utility. Therefore, OSS-SS has zero demand because users always prefer OSS over it. However, a consumer of type v will prefer PS over OSS if

$$
v > \frac {\theta (1 - 2 q _ {P}) + P _ {P}}{\beta_ {S}}.
$$

Because, in a symmetric fulfilled-expectation Nash equilibrium, the expected demand is the same as the actual demand,

$$
D _ {P} = q _ {P} \Rightarrow q _ {P} = 1 - v = 1 - \frac {\theta (1 - 2 q _ {P}) + P _ {P}}{\beta_ {S}} \Rightarrow q _ {P} = \frac {\beta_ {S} - \theta - P _ {P}}{\beta_ {S} - 2 \theta}.
$$

The profit function for the PS vendor is given by

$$
\pi_ {P} = D _ {P} \left(P _ {P} - c\right) = \left(\frac {\beta_ {S} - \theta - P _ {P}}{\beta_ {S} - 2 \theta}\right) \left(P _ {P} - c\right).
$$

This profit is maximized at $P _ { _ P } ^ { ^ * } = 1 / 2 ( \beta _ { _ S } + c - \theta )$ . The equilibrium demand is given by

$$
D _ {P} ^ {*} = \frac {\beta_ {S} - \theta - c}{2 (\beta_ {S} - 2 \theta)},
$$

and the equilibrium profits are

$$
\pi_ {P} ^ {*} = \frac {\left(\beta_ {S} - \theta - c\right) ^ {2}}{4 \left(\beta_ {S} - 2 \theta\right)}.
$$
