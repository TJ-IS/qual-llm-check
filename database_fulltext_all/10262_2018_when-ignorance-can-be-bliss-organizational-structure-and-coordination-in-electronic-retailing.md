---
otero_id: 10262
otero_key: "MU28G7D7"
title: "When Ignorance Can Be Bliss: Organizational Structure and Coordination in Electronic Retailing"
authors: "Dengpan Liu; Yong Tan; Vijay Mookerjee"
year: "2018"
journal: "Information Systems Research"
doi: "10.1287/isre.2017.0725"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## H4R

![](/api/attachments/MU28G7D7/fulltext/images/3e41979d13fd6cae3c7dab11037bda11737c489be36b4d9c2b7a8d974d5248ce.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# When Ignorance Can Be Bliss: Organizational Structure and Coordination in Electronic Retailing

Dengpan Liu, Yong Tan, Vijay Mookerjee

Dengpan Liu, Yong Tan, Vijay Mookerjee (2018) When Ignorance Can Be Bliss: Organizational Structure and Coordination in Electronic Retailing. Information Systems Research

Published online in Articles in Advance 03 Jan 2018

https://doi.org/10.1287/isre.2017.0725

## Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

Copyright © 2018, INFORMS

Please scroll down for article—it is on subsequent pages

## inferms.

INFORMS is the largest professional society in the world for professionals in the fields of operations research, management science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# When Ignorance Can Be Bliss: Organizational Structure and Coordination in Electronic Retailing

Dengpan Liu,<sup>a</sup> Yong Tan,<sup>a,</sup> <sup>b</sup> Vijay Mookerjee<sup>c</sup>

<sup>a</sup> School of Economics and Management, Tsinghua University, 100084 Beĳing, China; <sup>b</sup> Michael G. Foster School of Business, University of Washington, Seattle, Washington 98195; <sup>c</sup> Naveen Jindal School of Management, University of Texas at Dallas, Richardson, Texas 75083 Contact: liudp@sem.tsinghua.edu.cn (DL); ytan@uw.edu, http://orcid.org/0000-0001-8087-3423 (YT); vĳaym@utdallas.edu (VM)

Received: June 7, 2015 Revised: August 16, 2016; December 3, 2016 Accepted: January 11, 2017 Published Online in Articles in Advance: January 3, 2018

https://doi.org/10.1287/isre.2017.072

Copyright: © 2018 INFORMS

Abstract. This study examines coordination issues that occur between the marketing department and the information technology (IT) department in electronic retail settings. We consider a marketing department that is responsible for choosing the level of advertising to generate trafic to the firm’s website and an IT department that is responsible for choosing IT capacity to provide web visitors a satisfactory experience. The focus here is to examine how duopolistic advertising competition among firms can afect the organizational structure (centralized or decentralized) within each firm. In essence, our interest lies in the question: How does the presence of interfirm competition afect intra-firm coordination (i.e., organizational structure)? As a benchmark, we develop and solve a centralized decision model wherein the levels of advertising and IT capacity are jointly chosen in each firm to maximize profit. This is compared with a decentralized decision model in which the marketing department could potentially advertise suboptimally because its assessment of IT factors (the served trafic rate) is inaccurate. We find that competition can lead to a decentralized equilibrium in which both firms choose not to coordinate among their internal departments. More importantly, we find that when marketing moderately underestimates IT service quality, coordination results in a prisoners’ dilemma (PD) equilibrium for each firm whereas decentralization is socially optimal but with an of-equilibrium outcome (resulting in higher profits for each firm). That is, the conventional wisdom that “more coordination is good” could push firms toward a PD equilibrium when they can both be better of by not coordinating internally in the face of competition. This result also implies that if marketing tends to underestimate the capabilities of the IT department, it may be better to encourage such firms to coordinate less rather than encouraging them to coordinate more.

History: Sanjeev Dewan, Senior Editor; Xue Bai, Associate Editor.

Funding: Dengpan Liu’s research was supported in part by the National Natural Science Foundation of China under [Grant 71490723]. Yong Tan is the Chang Jiang Scholar Visiting Chair Professor at Tsinghua University and was supported in part by the National Science Foundation of China [Grants 71490723, 71531013, and 71572004].

Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2017.0725.

Keywords: advertising competition • organizational structure • coordination

## 1. Introduction

In the past decade, there has been a remarkable increase in online shopping. According to Forrester Research, online retail sales in the United States are expected to reach nearly \$460 billion in 2017, about 12.9% of the total retail sales, and will account for 17.0% of retail sales by 2022 (Lindner 2017). This market is likely to keep growing, fueled in part by the growth in the worldwide online population that is projected to reach over 4 billion in 2020 (Garrity 2016).

As electronic commerce activity expands, the competition among electronic retailing firms is expected to intensify (Mullaney and Hof 2004), causing electronic retailers to advertise aggressively in a bid to attract customers. However, unless the trafic drawn to a website can be adequately served, excessive trafic can lead to poor consumer experience and lost customers. With many shopping alternatives and speedier broadband connections, consumers are becoming increasingly intolerant of website delays. According to online customer data platform QuBit, more than \$2.5 billion lost sales per year occur due to slow response times (Knowles 2012). In 2010, Bojan Simic, the founder of TRAC Research, estimated that revenue amounting to \$4,100 per hour was lost due to sluggish website performance (Choney 2011).

A slowdown can occur when system capacity is not suficient to handle the incoming trafic. For electronic retailers, this might be because of inaccurate trafic estimation and capacity requirements (Karpinski 2000).

Another cause could be an unbalanced allocation of resources across advertising efort and information technology (IT) capacity. If an e-tailer puts in too much advertising efort to attract trafic but does not match this with adequate capacity, customers are likely to be lost, often never to return. In e-retailing, along with marketing, IT is a core business function and must be integrated as a key player in organizational planning (Eschbach 2007). Hence, to take full advantage of e-tailing opportunities, it would appear that trafic generation decisions need to be coordinated with IT capacity decisions. However, our analyses reveal that while coordinated decision making is always optimal for a monopoly, it could be harmful in the presence of competition.

In e-tailing firms, the lack of coordination between IT and marketing can often result in slow website response and a loss in sales revenue. Even worse, the miscommunication between marketing and IT could lead to severe website failures (Hinds 2014). During Christmas of 2008, a marketing team at a major e-retailer, without giving the IT department any advance notice, launched a series of prime-time TV promotions showcasing its top products. Shortly afterward, the promotion brought in an overwhelmingly large amount of trafic, and the site crashed, leading to a huge loss in revenue (Moore 2009). Deloitte CIO Journal (2013) reported another recent story of a marketing failure from the lack of coordination between IT and marketing. A retailer launched a series of online promotions without apprising the IT department beforehand of its plans. Not surprisingly, the company’s websites crashed as the trafic the promotions had brought in spiked to unprecedented levels, leaving many shoppers frustrated. The cost of downtime for e-tailing firms can be huge. For example, a large retailer during downtime can lose more than \$2 million per hour in revenue loss and labor costs to fix the problem in addition to the damage to reputation and customer loyalty (Petersen 2015). Unfortunately, the lack of communication between the marketing and IT departments is all too common. It was reported that two-thirds of marketers admitted they never or rarely meet with their IT department to prepare for peaks in website traffic (Moore 2009). According to a survey conducted by Teradata in 2013, silos are present between marketing and other core functions, and 74% of marketers claim that marketing and IT are not strategic partners in their company (Teradata 2014). A more recent study in 2015 by Rackspace reveals that, among the IT leaders surveyed in the study, 42% believe that marketing does not understand the details of IT, and 35% claim that marketing commits to plans without even consulting IT (Ivey 2016).

This paper examines coordination issues between the marketing and IT functions of firms in a competitive setting. We question the commonly held belief that the lack of coordination (between marketing and IT) is always harmful for the firms. We refer to the marketing and IT units in a firm as centralized when these functions operate in a coordinated manner and decentralized if they act independently. Usually discussed in the context of a single firm, most previous research has regarded coordination as something beneficial with the potential to improve firm profit. We show that internal organizational units (namely, marketing and IT) may have to adjust their coordination strategies when outside competitive pressures act on the firms. Surprisingly, we find that firms can sometimes be better of by not coordinating internally in the face of competition.

To provide a clearer understanding of the need for coordination between the marketing and IT departments of an e-tailing firm, consider a customer’s visit to a typical e-commerce site. The visit may turn into an actual sale, or the customer may leave without buying. In the latter case, the customer may finish browsing but decide not to purchase, or the customer could renege from the website frustrated by slow response time. Our study concerns the last scenario in which lost sales occur because of poor website performance. To avoid such lost revenue, it may be better to increase IT capacity or attract less trafic and divert some resources to improve the response time. This requires coordination between the department responsible for choosing the level of advertising (for simplicity, marketing) and the department responsible for choosing the processing capacity of the site (for simplicity, IT). Of course, if the two decisions are made by a central authority, then coordination is naturally achieved. In this case, the problem reduces to one of jointly optimizing trafic generation and IT capacity decisions.

When two firms engage in advertising competition, the equilibrium trafic attracted by each firm is afected by the internal structure chosen by the two firms. This choice (to coordinate or not) needs to be examined in equilibrium. Here we find that being uncoordinated can sometimes be an equilibrium outcome. In other situations, decentralization (albeit, an of-equilibrium outcome) can result in higher profits for each firm while the equilibrium choice of centralization can be a prisoners’ dilemma (PD).

The rest of the paper is organized as follows. In Section 2, we provide a review of related work. In Section 3, we formally introduce the (centralized and decentralized) decisions made by marketing and IT in the context of a single firm (or monopoly). Section 4 presents and studies these decisions in a duopoly setting with a focus on the equilibrium analysis. Section 5 continues the analysis of the duopoly setting from the perspective of social optimality. In Section 6, we provide a high-level discussion of the results and conclude the paper.

## 2. Literature Review

Over the past few decades, coordination has been an extensively researched subject across a wide range of academic disciplines. Although the term coordination can be broadly defined as “the act of working together” (Malone and Crowston 1991, p. 3), its usage and meaning is often discipline- and context-sensitive. In computer science, the term coordination often refers to the process of managing activities that share resources. For example, operating systems use algorithms to allocate resources (e.g., memory) among diferent processes that request the resources (Deitel 1983). On the other hand, in economics and social science, the act of coordinating the work of humans additionally raises issues of incentive alignment that are typically not considered when coordinating inanimate agents. Thus, it is not surprising that coordination is considered to be an important element of organizational strategy and a key issue in the design of organizational structures and processes (De Vreede and van Eĳck 1998). Coordination within organizations, especially between other functional units and marketing, has been reported and extensively studied for many decades (Anderson and Cundif 1965). A considerable amount of research also exists on coordination across organizations. However, since our focus is on intra-firm coordination, we focus on the literature on coordination between the units of a firm.

## 2.1. IT Governance

Our study is related to the literature on IT governance, a field that has attracted extensive attention from academics and IT practitioners over the past decades. Weill (2004) defined IT governance as the framework for decision rights and accountabilities that can be used to promote desirable behavior in the allocation and use of IT. One stream of research in IT governance deals with single-firm, or monopolistic, settings. Two distinct governance structures are discussed here. In one structure, the authority for most IT decisions is located within the functional unit. This structure corresponds to the centralized decision-making framework we study in the paper, in which IT and marketing decisions are jointly made to maximize the overall profit. From a coordination perspective, this structure corresponds to the coordinated case in which IT and marketing (acting as two separate, decentralized decisionmaking units) have perfect information exchange with one other. In the other structure, the authority for the majority of IT decisions is located in the corporate IT group. In this structure, IT services are shared by the diferent functional units, and each functional unit may not have perfect knowledge about the details of the IT capabilities and priorities that are assigned to support it. This structure corresponds to the decentralized decision-making framework we study in the paper, where IT and marketing departments make independent decisions. From the perspective of coordination, this structure corresponds to the uncoordinated case in which IT and marketing (acting as two separate, decentralized decision-making units) have less than perfect information exchange with one another.

During the 1970s and 1980s, with the goal of improving end-user computing services, coordinated governance models began to be recommended over uncoordinated ones (Demb 1975; Golub 1975; D’Oliveria 1977; King 1978, 1983). For instance, according to King (1983), one of the benefits of adopting coordinated models is the opportunity for user departments to decide for themselves how computing can be best configured to serve their needs. Although corporate governance promotes IT standards and scale economies, bringing IT decision rights close to the end user can significantly improve IT’s overall responsiveness to the needs of individual business units (Brown and Grant 2005).

Many firms have now adopted federal governance architecture in which business units possess the authority for the management of IT applications and use, and the corporate IT unit possesses the authority for the management of IT infrastructure (Sambamurthy and Zmud 2000). The federal approach could also be thought of as an IT governance structure that promotes coordination between the end-user departments and IT. Researchers have proposed a variety of coordination mechanisms (e.g., service level agreements) for federal governance architecture (Zmud 1988). One common message in the extant research is that coordination between IT and other business units should be encouraged. This is in line with the analytical finding in our single-firm analysis (or the monopoly case), in which coordination is shown to maximize profit (assuming zero coordination cost).

There is relatively little literature on IT governance in a competitive setting. Tavakolian (1989) conducted a survey study of 52 large organizations and found that firms’ IT structure is reliant on their competitive strategy. Specifically, firms are more likely to have an uncoordinated IT governance structure if their competitive strategy is more conservative. On the other hand, firms are more likely to have a coordinated IT governance structure if they are more entrepreneurial and risktaking. Similarly, according to Das et al. (1991), organizations with a more aggressive competitive strategy are more likely to have coordinated IT structures as compared with firms with a more conservative competitive strategy. The suggestion in the literature is that firms tend to coordinate more as competition intensifies, implying that market structure is related to organization structure. This observation is consistent with our analytical finding that firms may choose internal coordination at equilibrium in the face of competition.

However, we have gone a step further to show that firms can sometimes be better of by not coordinating in the face of competition.

## 2.2. Organizational Information Sharing

There is extensive literature on intra-organizational information (knowledge) sharing. Using a game-theoretic approach, Barua et al. (1997) show that organizationally desirable information exchange can be achieved if individual and organizational goals can be aligned through elements of organizational culture. Yang and Chen (2007) study the relationship between knowledge sharing and organizational knowledge capabilities. They find that organizational knowledge sharing is positively related to organizational knowledge capabilities. Barua et al. (2007) study a setting with information complementarity in which the payof to a workgroup depends not only on the quality of its own information but also on that of the information provided by other workgroups. They show how a long-term vision combined with homogeneity in information management capabilities across workgroups can lead to organizationally desirable levels of information exchange. Using a novel agent-based modeling approach, Yang and Wu (2008) simulate the knowledge-sharing process in an organization and measure the efectiveness of diferent organizational incentive policies in promoting information sharing.

There is relatively little literature on organizational information sharing in a competitive market environment. According to Lubit (2001), fostering efective organizational sharing of tacit knowledge is critical for ensuring the sustainable competitive advantage of an organization. On the other hand, the sharing of explicit knowledge may lead to the loss of competitive advantage as it increases the risk that the knowledge will be copied by competitors. Kearns and Lederer (2003) examine how organizational information sharing accomplished through strategic IT alignment can lead to competitive advantage of an organization through producing enhanced organizational strategies.

As we can see, the extant literature on organizational information sharing has generally held that information sharing should be encouraged. However, in the present study, we challenge this commonly held belief by showing that organizations in a competitive market environment can be better of by discouraging information sharing among their internal units.

## 2.3. Advertising Competition

There exists a rich body of academic research that considers firms engaged in advertising competition. For example, Deal (1979) and Erickson (1985) study advertising competition between two firms. Note that, similar to our work, to focus on advertising competition, other marketing-mix variables are typically left out. As Erickson (1985) points out in his paper, marketing-mix variables (such as price and quality) are omitted so that advertising as one very important variable can be the focus of the study. Similarly, other papers (e.g., Sorger 1989; Mesak and Calloway 1995; Erickson 1995, 2009; Fruchter and Kalish 1997; Fruchter 1999; Wang and Wu 2001; Prasad and Sethi 2004; Bass et al. 2005; Naik et al. 2008) investigate firms’ advertising decisions in competitive settings without considering other marketingmix variables.

Table 1. Main Notation Used in the Paper

<table><tr><td>Parameters</td><td>Description</td></tr><tr><td> $b$ </td><td>Competition intensity</td></tr><tr><td> $a$ </td><td>Advertising cost parameter</td></tr><tr><td> $k$ </td><td>Marketing estimate of IT service quality</td></tr><tr><td> $\alpha$ </td><td>Marketing&#x27;s reward per unit of served traffic</td></tr><tr><td> $\beta$ </td><td>IT penalty per unit of lost traffic</td></tr><tr><td> $\gamma$ </td><td>IT capacity cost coefficient</td></tr><tr><td> $\lambda$ </td><td>Traffic level (marketing&#x27;s decision variable)</td></tr><tr><td> $\mu$ </td><td>IT capacity level (IT&#x27;s decision variable)</td></tr></table>

## 3. The Model

We start by considering a monopolistic, e-retailing firm with two departments that produce value through joint work. The M (marketing) department is responsible for attracting trafic (or visitors) to the firm’s website while the IT department is responsible for managing the website to allow visitors to browse and place orders. The main parameters and decision variables used in the analyses are summarized in Table 1.

## 3.1. Centralized Structure

We begin with a scenario in which decision making in a firm is centralized, and decisions are made to maximize the overall profit. The advertising spending (dollars per unit time) needed to sustain a trafic rate of λ is convex in the trafic, and a is a cost coeficient associated with trafic acquisition.

The visitors arriving at the firm’s website must be adequately served, or else they leave without completing a revenue-generating step (e.g., a sign-up, a purchase, etc.). We denote $L ( \lambda , \mu )$ as the fraction of the arriving trafic that is lost as a result of inadequate service (or delay); the quantity $1 - L ( \lambda , \mu )$ is defined as the IT service quality, service quality, or the served trafic rate. In customer-oriented industries, service quality is a critical component of customer satisfaction and retention (Anand et al. 2011).

To motivate an appropriate form for the fraction of customers lost, we consider a processor sharing queue that serves customers arriving at a Poisson rate of λ. The service time of each request can follow a generic distribution, and the server is assumed to be busy or available at any point in time. A loss occurs when a customer arrives and the server is busy. Otherwise, the customer is successfully served. Based on these conditions, it can be shown that the fraction of lost requests is given by (Tan and Mookerjee 2005)

$$
L (\lambda , \mu) = \frac {\lambda}{\mu + \lambda}.
$$

The fraction of lost requests has the following intuitive properties:

• All requests are lost when the IT capacity is zero $( L ( \lambda , 0 ) = 1 )$

• There is no loss under infinite capacity $( \operatorname* { l i m } _ { \mu \to \infty }$ $L ( \lambda , \mu ) = 0 )$

• The loss fraction is decreasing and convex in the capacity and increasing and concave in the trafic, implying diminishing returns of capacity and increasing efects of congestion.

The cost of IT capacity (or processing capacity) is $\gamma \mu ,$ where $\mu$ is the processing capacity, and $\gamma , \gamma \in ( 0 , 1 )$ , is a capacity cost coeficient. This is the cost of maintaining the capacity at the level $\mu .$ Following previous studies $( \mathrm { e . g . } ,$ Mendelson 1985, Tan and Mookerjee 2005), we assume that the cost to increase the capacity is linear. Thus, the coeficient $\gamma$ is a constant.

The revenue generated per completed transaction is normalized to 1. Thus the profit for the firm is given by

$$
\max _ {\lambda , \mu} \left\{(1 - L) \lambda - \frac {1}{2} a \lambda^ {2} - \gamma \mu \right\}.
$$

We therefore obtain the optimal trafic level

$$
\lambda^ {*} = a ^ {- 1} (1 - \sqrt {\gamma}) ^ {2},\tag{1}
$$

and the optimal capacity

$$
\mu^ {*} = \gamma^ {- 1 / 2} (1 - \sqrt {\gamma}) \lambda^ {*} = a ^ {- 1} \gamma^ {- 1 / 2} (1 - \sqrt {\gamma}) ^ {3}.
$$

## 3.2. Decentralized Structure

We next consider a monopolistic firm with diferent departments responsible for trafic generation (marketing) and trafic processing (IT). The marketing and IT departments are decentralized and make independent decisions. It is easier to conceptualize the process of decentralized decision making by working backward and starting at the capacity decision made by the IT department. This department is considered to be a cost center that responds to the level of trafic chosen by marketing.<sup>1</sup> To ensure that the IT department takes lost trafic into account while making its capacity decision, the firm imposes a penalty cost of $\beta$ per lost customer. The total cost for this department can therefore be expressed as

$$
C ^ {\mathrm{IT}} = \beta \lambda L (\lambda , \mu) + \gamma \mu ,
$$

where superscript IT stands for the IT department, $\mu$ is the processing capacity, $\gamma \in ( 0 , 1 )$ is the capacity cost coeficient, and $L ( \lambda , \mu )$ is the fraction of the arriving trafic that is lost. Based on the above, a costminimizing IT department will set the capacity

$$
\mu = \gamma^ {- 1 / 2} (\sqrt {\beta} - \sqrt {\gamma}) \lambda ,
$$

after observing the trafic level λ.

Substituting the capacity decision made by the IT department into the expression for the lost trafic we get

$$
L = \frac {\lambda}{\lambda + \mu} = \frac {\lambda}{\lambda + \gamma^ {- 1 / 2} (\sqrt {\beta} - \sqrt {\gamma}) \lambda} = \frac {\sqrt {\gamma}}{\sqrt {\beta}}.
$$

The served trafic rate $1 - L$ is therefore

$$
1 - \frac {\sqrt {\gamma}}{\sqrt {\beta}}.
$$

To set up the marketing department’s objective function, we consider a perfectly informed marketing department; that is, the true value of the served traffic rate, $1 - { \sqrt { \gamma } } / { \sqrt { \beta } } ,$ is known to marketing. To achieve incentive alignment, the firm rewards this department at the rate of $\alpha , \alpha \in [ 0 , 1 ] .$ , per unit of served trafic. In other words, the coeficient α in marketing’s objective is the per unit reward that marketing gets for the trafic that is served. Thus, the marketing department locally decides on a trafic level to maximize

$$
\pi^ {M} = \alpha \left(1 - \frac {\sqrt {\gamma}}{\sqrt {\beta}}\right) \lambda - \frac {1}{2} a \lambda^ {2}.
$$

The superscript M in the objective corresponds to the marketing department.

In the decentralized structure, we have used α to denote the reward to marketing per unit of served traffic and assigned IT a penalty of $\beta$ per unit of lost trafic. The following lemma shows how incentive alignment can be achieved.

Lemma 1. With $\alpha = 1 - \sqrt { \gamma }$ and $\beta = 1 .$ , marketing and IT departments achieve incentive alignment.

The values of α and $\beta$ in Lemma 1 guarantee that independent decisions made by the two departments will maximize the firm’s overall profit objective. For the rest of the paper, we set $\alpha = 1 - \sqrt { \gamma }$ and $\beta = 1$ to ensure incentive alignment. It should be noted here that these reward and penalty choices are not unique, but two simple choices that guarantee incentive alignment. However, the findings in this study hold for other reward and penalty choices that achieve incentive alignment. With these reward and penalty settings, the served trafic rate $1 - \sqrt { \gamma } / \sqrt { \beta }$ reduces to $1 - \sqrt \gamma$ Having resolved the incentive issues, for the rest of the paper, we focus on a diferent kind of misalignment that could arise from the lack of coordination.

## 3.3. Coordination

So far we have assumed that marketing is aware of the true service quality $( 1 - { \sqrt { \gamma } } ) ;$ that is, marketing has perfect information about the detailed workings of the IT department. However, there is ample evidence (e.g., Ivey 2016) of situations in which the exchange of information between the marketing and IT departments is less than perfect. Thus, for the rest of this paper, we relax this assumption and introduce coordination issues into the problem by proposing that the marketing department of a firm with a decentralized organizational structure may have imperfect information about the true service quality of the IT department. Specifically, we assume that the marketing department in a firm with a decentralized structure does not accurately know the loss function L and the parameter value $\mu .$ Because marketing’s reward depends on the trafic that is served, this department must estimate the fraction of arriving trafic that is served $( { \mathrm { i . e . } }$ , the service quality). We denote this estimate by $k \in [ 0 , 1 ]$ . Marketing people could make their estimation based on their past experience with the conversion rate of the trafic. One problem with this approach is that IT parameters may change very quickly (e.g., there could have been a server upgrade since the last campaign, or the server capacity available for marketing could be less, or more, than what was available in the last campaign). Thus, the conversion rate in the past could be very diferent (lower or higher) from the current one. When the coordination between marketing and IT is imperfect (e.g., Ivey 2016), we have the decentralized case in our study. Usually, in a decentralized scenario, marketing underestimates $( k < 1 - \sqrt { \gamma } )$ or overestimates $( k > 1 - \sqrt { \gamma } )$ the true service quality.<sup>2</sup> It should be noted that the firm rewards marketing based on the observed served trafic. This ensures that marketing will use the best possible estimate it has about the true service quality. That ${ \mathrm { i } } \mathbf { s } ,$ the reward structure is immune to any opportunistic (or wishful) estimation by the marketing department.

Acting with imperfect information (or the lack of coordination), the marketing department’s problem $\mathrm { i } \mathsf { s } ^ { 3 }$

$$
\max _ {\lambda} \pi^ {M} = \alpha k \lambda - \frac {a}{2} \lambda^ {2}.
$$

Thus the optimal trafic level (independently) chosen by marketing is

$$
\lambda^ {M} = \alpha k a ^ {- 1}.\tag{2}
$$

As before, IT responds to the trafic generated by marketing by choosing a capacity $( \mu )$ to minimize the cost, $\lambda ^ { M } \bar { L } ( \lambda ^ { M } , \mu ) + \gamma \breve { \mu }$ . We next compare the firm’s profits under a decentralized structure with the centralized structure.<sup>4</sup>

Corollary 1. A decentralized structure causes a profit loss of $( ( 1 - \sqrt { \gamma } ) ^ { 2 } - ( 1 - \sqrt { \gamma } ) k ) ^ { 2 } /$ <sup>/(</sup>2a<sup>)</sup> from the centralized structure.

The message in the corollary is clear: centralized decisions are always better (never worse) for a monopoly. Since the true value of the served trafic rate is $1 - { \sqrt { \gamma } } .$ , when the marketing department estimates IT service quality as $k = 1 - \check { \sqrt { \gamma } }$ , the two structures lead to the same profit. On the other hand, any departure from this estimate leads to a loss in profit.

In Section 4, we examine coordination issues from the lens of a duopoly. Here we find that competitive forces can reverse the virtues of intra-firm coordination.

## 4. Organizational Structure Under Advertising Competition

In this section, we examine coordination within marketing and IT in the context of two firms engaged in advertising competition. The presence of advertising competition afects not only the profit of the firms but also the organizational structure of each firm. We consider a duopoly in which the two competing firms have advertising and IT cost parameters $( a _ { 1 } , \gamma _ { 1 } )$ and $( a _ { 2 } , \gamma _ { 2 } ) .$ respectively. The advertising spending for firm i is denoted by $A _ { i } , i = 1 , 2$ . As shown in Section 3, in the absence of competition, we can write the trafic generated by spending $A _ { i }$ as

$$
\lambda_ {i} = \sqrt {2 / a _ {i}} \sqrt {A _ {i}}.\tag{3}
$$

We propose a duopolistic trafic model in which the trafic attracted by a firm is determined by its own advertising spending as well as that of its competitor. This model is similar to the formulation in the Lanchester (1916) model and its variants applied to advertising competition (see, for example, Case 1979). In these models, the total trafic is not conserved but can increase with the total amount of advertising in the market. In the duopolistic setting, we use b $( b > 0 )$ to represent the intensity of competition. I $\mathrm { \Delta } t b  0 ,$ the two firms do not compete, and the trafic at each firm tends to that in a monopolistic setting. To ensure a duopoly, both firms should receive positive trafic. Hence, we require that $\lambda _ { i } > 0 , \forall i$ . The constraint ensures that both firms exert suficient advertising efort so as to receive positive trafic.

The trafic attracted by firm i is (for the details of the consumer choice model used to derive the trafic, please refer to the online appendix)

$$
\lambda_ {i} = \sqrt {2 / a _ {i}} \sqrt {A _ {i}} + \sqrt {2} b (\sqrt {A _ {i} / a _ {i}} - \sqrt {A _ {j} / a _ {j}}); \quad \{i, j \} = \{1, 2 \},\tag{4}
$$

where $\lambda _ { i } > 0 . ^ { 5 , 6 }$

From (4), we obtain the advertising spending by firm i as a function of trafic

$$
A _ {i} = \frac {a _ {i}}{2 (1 + 2 b) ^ {2}} ((1 + b) \lambda_ {i} + b \lambda_ {j}) ^ {2}; \quad \{i, j \} = \{1, 2 \}.\tag{5}
$$

It is apparent from (5) that a firm’s spending to sustain a certain level of trafic not only depends on the trafic it desires to achieve but also on the trafic its competitor desires to achieve. In Sections 4.1 and $4 . 2 ,$ we study competition under centralized and decentralized structures. At this point, we impose symmetric structure decisions on the two firms (both centralized or both decentralized) and then determine the advertising level and IT capacity under these structures. Following this discussion, we present an analysis of how the two firms choose their structures in equilibrium. At the end of this section, we examine the impact of competition on firms and customers when both firms are centralized at equilibrium.

## 4.1. Competition Under a Centralized Structure

Assuming that the firms take centralized advertising and capacity decisions, we can write the profit function for firm i as

$$
\Pi_ {i} = \lambda_ {i} - A _ {i} - L _ {i} \lambda_ {i} - \gamma_ {i} \mu_ {i},
$$

where the loss fraction is given by $L _ { i } ( \lambda _ { i } , \mu _ { i } ) = \lambda _ { i } /$ $( \mu _ { i } + \lambda _ { i } )$ . Firm $i \prime \mathrm { s }$ objective is to maximize profit by choosing $\left( \lambda _ { i } , \mu _ { i } \right)$ for a given $\lambda _ { j } , \{ i , j \} = \{ 1 , 2 \}$

Lemma 2. The equilibrium profit for the two firms is as follows:

$$
\begin{array}{c} \Pi_ {i, c, c} ^ {*} = \frac {(1 - \sqrt {\gamma_ {i}}) ^ {2} (1 + 2 b)}{2} \bigg (\frac {(1 - \sqrt {\gamma_ {i}}) ^ {2} (1 + 2 b + 2 b ^ {2})}{a _ {i} (1 + b) ^ {2}} \\ \qquad - \frac {2 b (1 - \sqrt {\gamma_ {j}}) ^ {2}}{a _ {j} (1 + b)} \bigg); \quad \{i, j \} = \{1, 2 \}. \end{array}
$$

The subscript c in $\Pi _ { i , c , c } ^ { * }$ stands for centralized.

As seen in Lemma $^ { 2 , }$ the equilibrium profit for a firm depends on the advertising and IT parameters of both firms as well as the intensity of competition. The equilibrium solution in Lemma 2 is derived given the presence of a centralized structure at both firms. Given these structures, the entire profit function of each firm is considered to determine how advertising competition influences equilibrium levels of trafic and capacity. That is, using the profit function of each firm, we first find the optimal trafic response of firm i given the trafic of firm j. The trafic levels of the two firms are then derived in equilibrium in a simultaneous move game between the two firms. Finally, the IT capacities are chosen as a response to the equilibrium levels of trafic.

## 4.2. Competition Under a Decentralized Structure

When both firms are decentralized, the marketing departments in these firms make independent decisions. As before, we assume that the marketing department of firm i is rewarded at the rate $\alpha _ { i } ~ ( = 1 - \sqrt { \gamma _ { i } } )$ for each unit of served trafic, and the IT department is charged a penalty of 1 per unit of lost trafic.<sup>7</sup> Using $k _ { i }$ to denote the service quality estimate made by the marketing department of firm $\dot { \mathbf { \zeta } } _  i , $ the objective function for this department can be written as

$$
\pi_ {i} ^ {M} = \alpha_ {i} k _ {i} \lambda_ {i} - A _ {i}.
$$

The marketing department’s goal is to maximize its objective by choosing $\lambda _ { i }$ for a given $\lambda _ { j }$ . In turn, the IT department chooses capacity to minimize the following cost:

$$
C _ {i} ^ {I T} = \lambda_ {i} L _ {i} + \gamma_ {i} \mu_ {i} = \frac {\lambda_ {i} ^ {2}}{\mu_ {i} + \lambda_ {i}} + \gamma_ {i} \mu_ {i}.
$$

Lemma 3. The equilibrium profits for the two firms under a decentralized structure are

$$
\begin{array}{l} \Pi_ {i, d, d} ^ {*} = \frac {(1 + 2 b) (1 - \sqrt {\gamma_ {i}}) ^ {2}}{2} \\ \qquad \cdot \left(\frac {2 k _ {i} (1 + b) ^ {2} (1 - \sqrt {\gamma_ {i}}) - k _ {i} ^ {2} (1 + 2 b)}{a _ {i} (1 + b) ^ {2}} \right. \\ \qquad \left. - \frac {2 b k _ {j} (1 - \sqrt {\gamma_ {j}})}{a _ {j} (1 + b)}\right); \quad \{i, j \} = \{1, 2 \}. \end{array}
$$

The subscript d in $\Pi _ { i , d , d } ^ { * }$ stands for decentralized.

These expressions indicate that even in a decentralized structure, the equilibrium profits of the firms depend on the IT and advertising cost parameters of both firms as well as the intensity of competition. However, the expressions for the equilibrium profits are different. In the case of two centralized firms, we use the entire profit function for the two firms to obtain the equilibrium levels of trafic. In the decentralized case, the equilibrium levels of trafic are chosen in a simultaneous move game using only the marketing objectives of the two firms. The equilibrium profit expressions are then calculated by considering the response of the IT departments to these trafic levels.

Next, we numerically compare the sum of profits earned by the firms under the two structures in Figure 1. Here, we let $a _ { 1 } = a _ { 2 } = 0 . 4 , b = 0 . 9 , \gamma _ { 1 } = \gamma _ { 2 } = \gamma = 0 . { \overset { \_ } { } }$ and $k _ { 1 } = k _ { 2 } = k$

Since the true served trafic rate is $1 - \sqrt \gamma$ , in Figure $^ { 1 , }$ decentralization with perfect information $( \mathrm { i . e . , } k = 1 -$ $\sqrt { \gamma } \approx 0 . 6 8 )$ results in the centralized solution. However, as seen, the sum of profits under decentralization can be higher when the value of the served trafic rate is wrongly estimated. Based on this observation, several questions arise: Can such a result occur when the two firms choose their organization structures in equilibrium? Furthermore, can the profit under a decentralized equilibrium be socially optimal in the sense of the maximum sum of profits for the two firms? We explore these and other related questions in the rest of the paper.

Figure 1. Sum of Profits Under Diferent Organizational Structures  
![](/api/attachments/MU28G7D7/fulltext/images/85a9a41b0f646cd673a6335a0ce7c0ed3bf5e38c6c4bff65b5b1e43c6d950451.jpg)

## 4.3. Equilibrium Organizational Structure

So far, we have derived equilibrium solutions assuming that the organizational structure at each firm is given. We next consider a situation in which the organization structure is chosen by each firm in equilibrium. The order of play is as follows:

1. The two firms simultaneously choose and commit themselves to either a centralized (denoted by c) or a decentralized structure (denoted by d).

2. For each firm, if a centralized structure is chosen, then the firm chooses the trafic (based on the firm’s profit function) in a simultaneous advertising game. Otherwise, the marketing department of the firm chooses the trafic (based on marketing’s objective function) in a simultaneous advertising game.

3. The IT department at each firm chooses a capacity level based on the equilibrium level of trafic chosen in Step 2.

The solution process is in reverse order as is customary in backward induction. We first find the equilibrium profits of the two firms under four possible scenarios $( c , c ) , ( c , d ) , ( d , c )$ , and $( d , d )$ . Next, we find the equilibrium among these four scenarios. Let

$$
\zeta = 1 + \frac {2 b ^ {2}}{1 + 2 b}.
$$

It is easy to see that $\zeta \geq 1$ . The structure in equilibrium depends on two threshold quantities that we refer to as the upper structure threshold and the lower structure threshold. For firm i, the quantity $\zeta ( 1 - \sqrt { \gamma _ { i } } )$ is the upper structure threshold whereas the quantity $1 - \sqrt { \gamma _ { i } }$ is the lower structure threshold. It can easily be shown that the true value for the IT service quality (i.e., served trafic rate) at firm i is $1 - \sqrt { \gamma _ { i } }$ . For convenience, we say that the marketing of firm i significantly overestimates its<sub>√</sub> IT service quality if $k _ { i } > \zeta ( 1 - \sqrt { \gamma _ { i } } )$ , moderately overestimates its IT service quality $\mathrm { i f ~ } 1 - \sqrt { \gamma _ { i } } < k _ { i } \leq \bar { \zeta ( 1 - \sqrt { \gamma _ { i } } ) } .$ and underestimates its IT service quality if $k _ { i } < 1 - \sqrt { \gamma _ { i } } .$

Note that the structure thresholds for a particular firm do not depend on the IT capacity cost coeficient at the other firm.

Proposition 1. In a duopoly with competition, a firm adopts decentralization in equilibrium if its marketing department moderately overestimates its IT service quality. Otherwise, it adopts a centralized structure in equilibrium. Specifically, firm i adopts decentralization in equilibrium $i f 1 - \sqrt { \gamma _ { i } } < k _ { i } \leq$ $\zeta ( 1 - \sqrt { \gamma _ { i } } ) ;$ otherwise, it adopts centralization.

It is clear that the equilibrium structure only depends on how the marketing department estimates IT service quality. In a duopoly, for a given value of $k _ { i } ,$ centralization (or decentralization) is a dominant strategy for firm i $( \mathrm { i . e . , a }$ firm chooses a structure regardless of the structure chosen by the other firm). The equilibrium $( d , d )$ occurs only when the marketing departments of both firms moderately overestimate their IT service quality. The equilibrium $( c , c )$ occurs when both marketing departments underestimate or significantly overestimate their IT service quality. The asymmetric equilibrium $( c , d )$ or $( d , c )$ occurs when there is only one marketing department that moderately overestimates its IT service quality.

When marketing significantly overestimates the IT service quality $( \mathrm { i . e . , } k _ { i } > \zeta ( 1 - \sqrt { \gamma _ { i } } ) )$ , the firm prefers centralization to decentralization in equilibrium. Such a firm can sufer under a decentralized structure because it would over-advertise, and the IT department would not be able to adequately handle the trafic. Hence, the firm has a greater incentive to coordinate marketing with IT. When the service quality is moderately overestimated (i.e., $1 - \sqrt { \gamma _ { i } } < \hat { k _ { i } } < \zeta \bar { ( 1 - \sqrt { \gamma _ { i } } ) } )$ an interesting phenomenon occurs. In this situation, the firm’s equilibrium choice is to adopt a decentralized structure. This choice reflects a trade-of between two forces. First, by decentralizing, the firm has the ability to advertise more. This helps the firm in a competitive market. However, not all of the attracted traffic can be adequately served. This hurts the firm, and centralization avoids the problem of over-advertising. In the case of moderate overestimation by marketing, the net efect is such that the firm favors decentralization over centralization. On the other hand, a firm whose marketing department underestimates the IT service quality (i.e., $\bar { k } _ { i } < 1 - \sqrt { \gamma _ { i } } )$ advertises less and sufers in a competitive market. Thus, in the case of any underestimation, the decentralized equilibrium never occurs, and firms whose marketing departments underestimate always choose to centralize in equilibrium. To summarize, centralization is preferred when the marketing departments either underestimate or significantly overestimate the IT service quality. In these situations, centralization inhibits the firms from advertising too conservatively or too aggressively.

Another takeaway from Proposition 1 is that competition has a subtle impact on firms’ profits and the intraorganizational structures. Specifically, competition can lead to a decentralized equilibrium in which both firms choose not to coordinate among their internal departments. By contrast, the intra-organizational coordination is always a preferable choice for a monopolistic firm.

The results from Proposition 1 are illustrated in Figure 2. The solid lines in this figure separate the adjacent equilibria, and the axes are the IT service quality estimates for the two firms $( \mathrm { i . e . , } k _ { 1 }$ and $k _ { 2 } )$ . Letting $a _ { 1 } = 1$ $a _ { 2 } = 2 , b = 0 . 5 , \gamma _ { 1 } = 0 . 2 ,$ , and $\gamma _ { 2 } = 0 . 1 .$ , we have√ $\breve { \zeta } \approx 1 . 3 2$ The true served trafic rate for firm 1 is√ $1 - \sqrt { \gamma _ { 1 } } = 0 . 5 5$ Also, $\zeta ( 1 - \sqrt { \gamma _ { 1 } } ) = 0 . 7 3 . \mathrm { I f } \ k _ { 1 } > 0 . 7 3 ,$ then the IT service quality is significantly overestimated; if $0 . 5 5 < k _ { 1 } \leq 0 . 7 3 ,$ then it is moderately overestimated; and if $k _ { 1 } < 0 . 5 5$ then it is underestimated. Similarly, the true served trafic rate for firm 2 is 0.68 and the threshold for significant overestimation is 0.9. It is interesting to note that with all other model parameters held constant, as the intensity of competition increases, the lines in Figure 2 separating “Moderate overestimation” and “Significant overestimation” shift outward and therefore expand the region where the decentralized equilibrium, $( d , d )$ , occurs. This implies that decentralization is favored as the intensity of competition increases. In addition to the intensity of competition, advertising and IT capacity cost coeficients also afect the equilibrium organizational structure. We summarize our findings regarding the breakdown of centralization in the following corollary.

Corollary 2. If the marketing department of a firm significantly overestimates the service quality, then the equilibrium can shift away from centralization to decentralization in any of the following situations:

(a) The intensity of competition increases.

(b) Advertising becomes more costly.

(c) IT becomes less expensive.

From Corollary $^ { 2 , }$ an increase in the intensity of competition can break down centralization in equilibrium. When the marketing department of a firm overestimates the service quality $( \mathrm { i . e . , } k _ { i } > 1 - \sqrt { \gamma _ { i } } )$ , decentralization allows the firm to advertise more aggressively than the level of advertising that would have been chosen in a centralized structure. That is, under these conditions, centralization curbs the advertising level of a firm. Suppose we start with a situation in which $k _ { i } > \zeta ( 1 - \sqrt { \gamma _ { i } } ) , \zeta \geq 1 , i = 1 , 2 ,$ implying that both firms would choose centralization at equilibrium. However, as the competition intensity increases, since $\partial \zeta / \partial b > 0 .$ when b increases beyond a certain level, the condition $1 - \sqrt { \gamma _ { i } } < k _ { i } < \zeta ( 1 - \sqrt { \gamma _ { i } } )$ becomes true for either firm (or both firms), and centralization gives way to decentralization. Here, because competition is more intense, the firm’s marginal profit from advertising increases. Thus firms have a greater incentive to advertise more aggressively, and giving up centralization allows them to do so. As a result, the equilibrium shifts away from $( c , c )$ resulting in a breakdown of centralization. This result is in direct contrast to our finding that centralization is always the preferred choice in a monopoly.

It can also be observed from Corollary 2 that more costly advertising can also break down centralization in equilibrium. As discussed earlier, centralization can keep firms from over-advertising, which helps when there is insuficient capacity. However, as a firm’s advertising costs increase, the extent of overadvertising reduces. Hence, there is less damage from over-advertising in the presence of insuficient capacity. Therefore, the benefits of centralization reduce. It is interesting to note that the advertising costs of the two firms afect the upper structure threshold for either firm in the same way. Hence, even if a firm’s advertising costs do not change, its structure in equilibrium could be afected by a change in the advertising costs of the other firm. Changes in IT capacity costs can also impact organizational structure. As IT becomes less expensive, the equilibrium may switch from centralization to decentralization if service quality is significantly overestimated or switch from decentralization to centralization if service quality is moderately overestimated.

## 5. Can the Lack of Coordination Be a Good Thing?

It is generally held that coordination (especially, when it is costless) is a good thing. In this section, we examine the equilibrium results in Section 4 from the perspective of social optimality. As shown in Section 4, firms may adopt centralization (c) or decentralization (d) in equilibrium depending on how their marketing departments estimate IT service quality. We consider a symmetric setting in which the two firms are identical with respect to their advertising and IT cost parameters as well as their marketing departments’ estimation of IT service quality (i.e., $a _ { 1 } = a _ { 2 } = a , \gamma _ { 1 } = \gamma _ { 2 } = \gamma , k _ { 1 } =$ $k _ { 2 } = k )$ . In such a setting, it can easily be seen (Proposition 1) that asymmetric structure combinations $( \bar { ( } c , d )$ and $( d , c ) )$ cannot be an equilibrium outcome. Thus, the only possible Nash equilibria in a symmetric setting are $( c , c )$ and $( d , d )$

Under the symmetric setting, the properties of an equilibrium outcome (centralized or decentralized) can be characterized from the perspective of the IT service quality estimation parameter, k. The space of this parameter can be divided into four regions: significant overestimation, moderate overestimation, moderate underestimation, and significant underestimation. Each region of this parameter space has important implications for the structures chosen at equilibrium.

Figure 2. The Possible Equilibria  
![](/api/attachments/MU28G7D7/fulltext/images/c440fb13d68acc2c6026823a42f6d622e11dd9bb9377ed3c23ebec07471b6623.jpg)

## Significant Overestimation.

Lemma 4. When both marketing departments significantly overestimate IT service quality, the centralized equilibrium is unique and Pareto-dominant.<sup>8</sup>

From Lemma 4, when $k > \zeta ( 1 - \sqrt { \gamma } )$ , a centralized equilibrium, $( c , c ) ,$ , occurs at the two firms. A further examination of the centralized equilibrium leads to the above lemma. According to this lemma, when both marketing departments significantly overestimate their IT service quality, the centralized equilibrium is a Pareto-dominant equilibrium that is strictly preferred by each firm. This also implies that the centralized equilibrium is socially optimal (i.e., the profit of the twofirm system as a whole reaches its maximum). The centralized equilibrium is beneficial for all under these circumstances because the significant overestimation of IT service quality by marketing would have led to excessive advertising under a decentralized structure. Hence, the two firms are better of coordinating their internal units in the presence of competition.

Moderate Overestimation. From Proposition 1, when $1 - \sqrt \gamma < k \leq \zeta ( 1 - \sqrt \gamma )$ , a decentralized equilibrium, <sup>(</sup>d, d<sup>)</sup>, occurs at the two firms. A further examination of the decentralized equilibrium leads to the following lemma.

Lemma 5. When both marketing departments moderately overestimate IT service quality, decentralization is a prisoners’ dilemma (PD) equilibrium<sup>9</sup> and is Pareto-dominated by centralization that is socially optimal.

From Lemma 5, when the marketing departments moderately overestimate IT service quality $( 1 - \sqrt \gamma <$ $k \leq \zeta ( 1 - \sqrt { \gamma } ) )$ , firms will adopt decentralization at equilibrium. This outcome is a PD equilibrium and is Pareto-dominated by the socially optimal outcome $( c , c ) .$ , which is a socially optimal but of-equilibrium outcome. Under a decentralized structure, because the marketing departments overestimate, they advertise aggressively and hurt themselves. Centralization would have solved the problem but is unfortunately not an equilibrium choice.

Under any amount of overestimation, moderate or significant, we have the following corollary.

Corollary 3. Centralization is socially optimal if both marketing departments overestimate IT service quality.

Firms have a tendency to over-advertise in the presence of competition, and this tendency is aggravated when their marketing departments overestimate the IT service quality, and the aggression is not checked (decentralization is adopted). This problem can be resolved by adopting centralization.

Moderate Underestimation. The situation becomes very diferent when both marketing departments moderately underestimate the IT service quality. This leads to a somewhat puzzling outcome, namely, centralization can be a PD equilibrium. We present this finding, a key result in this study, in the following proposition.

Proposition 2. When both marketing departments moderately underestimate IT service quality<sub>√</sub> $( ( 1 - \sqrt { \gamma } ) / ( 1 +$ 2b $\sqrt { a } ) < k < 1 - \sqrt { \gamma } )$ , the firms participate in a PD game in the strong sense. The dominant strategy for both firms is centralization. This unique dominant strategy equilibrium, $( c , c ) .$ , is Pareto-dominated by $( d , d ) .$ , the socially optimal outcome. Hence, ignorance can be bliss.<sup>10</sup>

Moderately underestimating IT capacity under decentralization allows firms to advertise less aggressively, relative to the case in which the centralized structures are in place. This reduced aggression is socially optimal. Thus, in this situation, ignorance $( \mathrm { i . e . , }$ the underestimation) can be bliss. However, the reduced aggression is not realized since at equilibrium the firms choose centralized structures. These results are analogous to those in the traditional PD game, in which the two prisoners choose to betray the other (the dominant strategy) in equilibrium although they both could be better of choosing to remain silent (an of-equilibrium outcome). As we know, the remarkable result in a PD game is that actions taken in equilibrium can make both players worse of.

The analogy is that when marketing departments moderately underestimate the IT service quality, the firms participate in a PD game. Here, the of-equilibrium outcome $( d , d )$ is better than the equilibrium solution $( c , c )$ . Therefore, under these circumstances, the conventional wisdom—more coordination is good— encourages firms toward a PD equilibrium. The intuition behind this finding is the following. Firms tend to over-advertise in the presence of interfirm competition. However, when a decentralized structure is in force and marketing underestimates IT capability, this underestimation inhibits the tendency to overadvertise, resulting in higher profits for each firm.

The question naturally arises: If a moderate degree of underestimation favors decentralization, does a significant extent of underestimation make the argument for decentralization even stronger?

## Significant Underestimation.

Lemma 6. When both marketing departments significantly√ underestimate IT service quality $( k \overset { \cdot } { \leq } ( 1 - \sqrt { \gamma } ) / ( 1 + 2 b \sqrt { a } ) )$ the centralized equilibrium is unique and socially optimal.

As seen here, Lemma 6 reveals that a significant extent of underestimation by marketing can, once again, make centralization a good thing. Under significant underestimation, the benefit of curbing unhealthy advertising is no longer a virtue that is brought about by decentralization. Here, the lack of correct knowledge (of IT service quality) hurts because under decentralization the two firms become overly conservative with regard to their advertising choices. Once again, as in the case of significant overestimation (Lemma 4), centralized structures help the firms reach social optimality.

We summarize the results in this section in Table 2. Note from Table 2, that the asymmetric structure combinations $( \mathrm { i . e . } , \ ( c , d )$ and $( d , \dot { c } ) )$ can never be socially optimal under a symmetric setting. As shown in

Table 2. Nash Equilibrium and Social Optimum Under Symmetric Settings

<table><tr><td>Service quality estimation (k)</td><td>Nash equilibrium</td><td>Social optimum</td></tr><tr><td>Very low</td><td>(c,c)</td><td>(c,c)</td></tr><tr><td>Moderately low</td><td>(c,c)</td><td>(d,d)</td></tr><tr><td>Moderately high</td><td>(d,d)</td><td>(c,c)</td></tr><tr><td>Very high</td><td>(c,c)</td><td>(c,c)</td></tr></table>

Table 2, in the presence of interfirm competition, decentralized structures can be socially optimal. In particular, we find that when both marketing departments moderately underestimate the IT capacities (i.e., the value for k is moderately low), the firms adopt central ized structures in equilibrium; however, this equilib rium is a PD and is Pareto-dominated by the socially optimal choice $( d , d )$ . On the other hand, when both marketing departments overestimate $( \mathrm { i . e . , } k$ is moderately high or very high) or significantly underestimate $( \mathrm { i . e . , } k$ is very low) the IT capacities, the socially optimal combination is $( c , c )$ . In particular, when both marketing departments moderately overestimate $( \mathrm { i . e . , }$ k is moderately high) the IT capacities, the firms are stuck in the PD equilibrium $( d , \bar { d } )$ . As discussed, either $( c , c )$ or $( d , d )$ can be socially optimal or a PD equilibrium, depending on the values of model parameters. It is also interesting to note that the Nash equilibrium outcome does not match the socially optimal choice in two scenarios: moderate underestimation and moderate overestimation. A plausible explanation is as follows. When the underestimation is moderate, firms at equilibrium choose an organizational structure (centralization) that allows them to advertise more aggressively relative to the case in which the firms were not aware of the true IT capacity. By contrast, the social planner chooses an organizational structure (decentralization) that restrains advertising aggression. That is, the social planner deliberately allows the firms to be ignorant of the true IT capacity and benefit from the reduced advertising aggression. The reverse is true when there is moderate overestimation. Here, the socially optimal choice is centralization whereas the equilibrium outcome is decentralization. On the other hand, when the extent of misestimation (overestimation or underestimation) is very large, firms prefer centralization at equilibrium. In such situations, correcting the misestimation (via centralization) is preferable to the possible benefits from being overly aggressive (in the case of overestimation) or being overly defensive (in the case of underestimation). From a social perspective as well, when the extent of misestimation is very large, centralization is the best choice. Thus, the equilibrium and socially optimal outcomes match when the extent of misestimation is very large. Note that all of the analytical findings in this section are derived under symmetric settings. For a robustness check, we have also examined asymmetric settings through extensive numerical studies. Our analysis shows that the insights from the symmetric study can carry over to the asymmetric settings. However, because of space limitations, the details of the analysis are omitted from the paper.

## 6. Conclusions and Discussion

We examine two e-retailing firms engaged in duopolistic advertising competition. The issue of interest is how coordination structures internal to the firms are afected by the presence of competition. We find that internal organizational units (namely, marketing and IT) may have to adjust their organizational structure when outside competitive pressures act on the firms. Unlike the case of a monopoly in which coordinating internal units is always optimal, firms can sometimes be better of by not coordinating internally in the face of competition. Structure decisions need not always be symmetric in equilibrium. Moreover, one or more firms may choose decentralization over centralization. Another important conclusion of our analysis is that the breakdown of coordination can be a socially optimal outcome that results in higher profits for each firm while the equilibrium choice of centralization by both firms can be a PD. Similarly, the equilibrium choice of decentralization by both firms can be a PD as well. Such an outcome occurs when marketing departments of the firms moderately overestimate their IT service quality.

The marketing department’s assessment of IT capabilities (service quality) can afect a firm’s decision to centralize or decentralize at equilibrium. If marketing’s assessment of service quality is low (i.e., an underestimation) or very high (i.e., a significant overestimation), a firm prefers centralization to decentralization in equilibrium. This is so because over-advertising or underadvertising can be restrained with intra-firm coordination. As competition intensifies, firms are less likely to centralize marketing and IT. A moderate amount of underestimation by marketing is socially optimal if the firms use a decentralized structure. Additionally, competition moderates the impact of marketing’s estimation error on firm performance. Specifically, estimation errors made by the marketing department (which always lower profits in a monopoly) can act as a blessing in disguise for competing firms.

In practice, the results in our study could be used to guide companies to develop IT governance strategies in the face of competition. For instance, if the marketing departments of two competing companies are both moderately pessimistic about IT’s ability to serve trafic, these firms are better of with less coordination between marketing and IT. On the other hand, if the marketing departments of two competing companies are both moderately optimistic about their respective IT capabilities, they should be encouraged to coordinate more with IT.

At a higher level, the core of the problem studied in this paper is essentially about the mismatch that occurs in how other departments in a firm view the true capabilities of the IT function. Normally, in an organization, the detailed operations of the IT department are not visible to other departments. Thus, these departments make decisions based on assumptions of how they perceive the IT department to work. Of course, if the firm is centralized, decisions can be made with full visibility. When centralization is possible (either explicitly as a structural choice or by implementing coordination schemes to achieve centralized behavior), there is no mismatch between the perceived service quality of the IT department and its actual service quality. In decentralized scenarios, some mismatch is inevitable. In a monopoly, the results are expected: the mismatch always leads to a loss for the firm. Thus, we should not expect to see the mismatch to occur in a monopoly. In a duopoly, the mismatch could be present at equilibrium. In other cases, the mismatch could be eliminated at equilibrium but be harmful for the firms as in the case of a PD.

Our study is not without limitations. One limitation lies in the simplifying assumption of symmetric model parameters that we have made when deriving the analytically tractable results. Another limitation is that we have chosen to omit some marketing-mix variables (such as price and quality) so as to focus on advertising competition. One promising area for future work is to incorporate marketing-mix variables (e.g., price) into the advertising competition model and see if the main findings in the present study still hold. Another topic for future study is to investigate whether the findings in this study could be generalized to other business settings, such as the mismatch between the marketing and production departments. It would also be useful to examine interfirm incentive schemes that can induce firms to reach a better equilibrium. At a higher level, another avenue for future work is to develop a more general theory of competition between teams. While in team theory the focus is on coordination issues internal to the team, the focus in game theory is usually on competition between atomic decision makers. The joint action of coordination forces internal to a team and competitive forces across teams has rarely been studied. Our study is a step in this direction although it deals with a specific case of competition between teams. Because IT usually acts as a coordinating force within an organization, a theory of coordination in the presence of competition could provide specific insights for the information systems discipline.

## Acknowledgments

The authors thank the senior editor, the associate editor, and three anonymous referees for their insightful comments and suggestions that have greatly helped improve the quality of this paper.

## Endnotes

<sup>1</sup> We are considering an environment in which IT decisions are made to fulfill the demand for a particular marketing campaign.

<sup>2</sup> A special case arises when marketing accurately estimates the true service quality $( \mathrm { i . e . , } \ k = 1 - \sqrt { \gamma } )$ . Here, a decentralized structure is equivalent to a centralized one. That is, marketing and IT are in synch with one another and act as if they were a single decision maker.

<sup>3</sup> Marketing is only provided with the numerical value of α, not the formula to calculate it.

<sup>4</sup> We assume that marketing and IT have already achieved incentive alignment. Hence, the only misalignment (lack of coordination) occurs because marketing has an inaccurate estimate of the service quality.

<sup>5</sup> The bounds for the parameter b are implied by this constraint.

<sup>6</sup> It should be clear that we are considering a nonzero-sum game setting in this study; that is, the advertising spending of each firm not only attracts existing consumers from its rival but also brings new consumers to the duopoly system. However, it can be shown that the main findings of this study still hold qualitatively under a zero-sum game setting.

<sup>7</sup> In the duopolistic setting as well, $\alpha _ { i } = 1 - \sqrt { \gamma _ { i } }$ and $\beta _ { i } = 1$ achieve incentive alignment within Firm i.

<sup>8</sup> While the value of $\zeta ( 1 - \sqrt { \gamma } )$ is typically less than 1, this value can be greater than or equal to 1. When $\zeta ( 1 - \sqrt { \gamma } ) \geq 1 .$ , we have $k \leq \zeta ( 1 - \sqrt { \gamma } )$ since k <sup>∈</sup> <sup>[</sup>0, 1<sup>]</sup>. In such a case, we should instead consider Lemma 5, Proposition 2, or Lemma 6, depending on the value of k.

<sup>9</sup> For brevity, we refer to the “equilibrium in a prisoners’ dilemma game” as Prisoners’ dilemma equilibrium.

<sup>10</sup> Here, by “ignorance,” we mean that both firms adopt a decentralized structure (i.e., there is no coordination between the marketing and IT departments, and hence, marketing does not know the true value of IT service quality). Such ignorance can be bliss when both marketing departments moderately underestimate the IT service quality. By “bliss,” we mean that both firms are better of.

## References

Anand K, Pac F, Veeraraghavan S (2011) Quality-speed conundrum: Trade-ofs in customer-intensive services. Management Sci. 57(1):40–56.

Anderson RC, Cundif EW (1965) Patterns of communication in marketing organization. J. Marketing 29(3):30–34.

Barua A, Ravindran S, Whinston AB (1997) Efective intra-organizational information exchange. J. Inform. Sci. 23(3):239–248.

Barua A, Ravindran S, Whinston AB (2007) Enabling information sharing within organizations. Inform. Tech. Management 8(1): 31–45.

Bass FM, Krishnamoorthy A, Prasad A, Sethi SP (2005) Generic and brand advertising strategies in a dynamic duopoly. Marketing Sci. 24(4):556–568.

Brown AE, Grant GG (2005) Framing the frameworks: A review of IT governance research. Comm. Assoc. Inform. Systems 15(38): 696–712.

Case JH (1979) Economics and the Competitive Process (New York University Press, New York).

Choney S (2011) Facebook leads in social media site reliability, speed. http://www.nbcnews.com/technology/facebook-leads -social-media-site-reliability-speed-122316.

Das SR, Zahra SA, Warkentin ME (1991) Integrating the content and process of strategic MIS planning with competitive strategy. Decision Sci. 22(5):953–984.

De Vreede G-J, van Eĳck DTT (1998) Modeling and simulating organizational coordination. Simulation Gaming 29(1):60–88.

Deal KR (1979) Optimizing advertising expenditures in a dynamic duopoly. Oper. Res. 27(4):682–692.

Deitel HM (1983) An Introduction to Operating Systems (Addison-Wesley, Reading, MA).

Deloitte (2013) Capacity planning: How to prevent system overload. Wall Street Journal (May 2), http://deloitte.wsj.com/cio/2013/ 05/02/capacity-planning-how-to-prevent-system-overload/.

Demb AB (1975) Centralized vs. decentralized computer systems: A new approach to organizational impacts. CISR Report 12, Center for Information Systems Research, Sloan School, Massachusetts Institute of Technology, Cambridge.

D’Oliveria CR (1977) An analysis of computer decentralization. Report AD-A045 526, National Technical Information Service, Springfield, VA.

Erickson GM (1985) A model of advertising competition. J. Marketing Res. 22(3):297–304.

Erickson GM (1995) Advertising strategies in a dynamic oligopoly. J. Marketing Res. 32(2):233–237.

Erickson GM (2009) Advertising competition in a dynamic oligopoly with multiple brands. Oper. Res. 57(5):1106–1113.

Eschbach P (2007) Communication and IT: Taming the three-headed dog. Comm. World 24(5):48.

Fruchter GE (1999) The many-player advertising game. Management Sci. 45(11):1609–1611.

Fruchter GE, Kalish S (1997) Closed-loop advertising strategies in a duopoly. Management Sci. 43(1):54–63.

Garrity J (2016) Internet user growth over the next five years. Hufpost (June 22), https://www.hufingtonpost.com/john-garrity/ internet-user-growth-over\_b\_10603196.html.

Golub H (1975) Organizing information system resources: Centralization vs. decentralization. McFarlan FW, Nolan RL, eds. The Information Systems Handbook (Dow Jones-Irwin, Homewood, IL), 65–91.

Hinds T (2014) Website trafic: Marketing fantasies vs. IT realities. Neotys (March 12), http://www.neotys.com/blog/website -trafic-marketing-fantasies-vs-it-realities/.

Ivey J (2016) IT vs. marketing leaders: Bridging the CMO-CIO divide. Rackspace (June 9), http://blog.rackspace.com/it-vs-marketing -bridging-cmo-cio-divide/.

Karpinski R (2000) E-retailers balance IT, marketing. Internet Week 795:1.

Kearns GS, Lederer AL (2003) A resource-based view of strategic IT alignment: How knowledge sharing creates competitive advantage. Decision Sci. 34(1):1–29.

King JL (1978) Centralization vs. Decentralization of Computing: An Empirical Assessment in City Governments (Public Policy Research Organization, University of California, Irvine).

King JL (1983) Centralized versus decentralized computing: Organizational considerations and management options. ACM Comput. Surveys 15(4):319–349.

Knowles J (2012) Slow-loading e-commerce sites cost global retailers more than £1.7b in lost sales. TheNextWeb (May 3), http:// thenextweb.com/apps/2012/05/03/slow-loading-e-commerce -sites-cost-global-retailers-more-than-1-7b-in-lost-sales/.

Lanchester FW (1916) Aircraft in Warfare: The Dawn of the Fourth Arm (Constable, London).

Lindner M (2017) E-commerce is expected to grow to 17% of U.S. retail sales by 2022. Internet Retailer (August 9), https://www .digitalcommerce360.com/2017/08/09/e-commerce-grow-17-us -retail-sales-2022/.

Lubit R (2001) Tacit knowledge and knowledge management: The keys to sustainable competitive advantage. Organ. Dynam. 29(4): 164–178.

Malone TW, Crowston KG (1991) Toward an interdisciplinary theory of coordination. Technical Report 120, Massachusetts Institute of Technology, Center for Coordination Science, Cambridge.

Mendelson H (1985) Pricing computer services: Queueing efects. Comm. ACM 28(3):312–321.

Mesak HI, Calloway JA (1995) A pulsing model of advertising competition: A game theoretic approach, Part A—Theoretical foundation. Eur. J. Oper. Res. 86(2):231–248.

Moore G (2009) How to tackle online trafic delays and save brand reputation. utalkmarketing (August 10), http://www .utalkmarketing.com/pages/article.aspx?articleid<sup></sup>14875&title<sup></sup> how\_to\_tackle\_online\_trafic\_delays\_and\_save\_brand\_reputation.

Mullaney T, Hof R (2004) E-tailing finally hits its stride. Bus. Week (December 20):36–37.

Naik PA, Prasad A, Sethi SP (2008) Building brand awareness in dynamic oligopoly markets. Management Sci. 54(1):129–138.

Petersen G (2015) Downtime in retail costs millions: “Always on, always available” is the key to success! Omni-Channel (August 10), http://www.omni-channel-customer-engagement.com/ articles/408053-downtime-retail-costs-millions-always-alwaysavailable-the.htm.

Prasad A, Sethi SP (2004) Competitive advertising under uncertainty: A stochastic diferential game approach. J. Optim. Theory Appl. 123(1):163–185.

Sambamurthy V, Zmud RW (2000) Research commentary: The organizing logic for an enterprise’s IT activities in the digital era— A prognosis of practice and a call for research. Inform. Systems Res. 11(2):105–114.

Sorger G (1989) Competitive dynamic advertising: A modification of the case game. J. Econom. Dynam. Control 13(1):55–80.

Tan Y, Mookerjee VS (2005) Allocating spending between advertising and information technology in electronic retailing. Management Sci. 51(8):1236–1249.

Tavakolian H (1989) Linking the information technology structure with organizational competitive strategy: A survey. MIS Quart. 13(3):308–318.

Teradata (2014) Why breaking down marketing silos is essential to achieving customer satisfaction. The Drum (December 3), http://www.thedrum.com/industryinsights/2014/12/03/why -breaking-down-marketing-silos-essential-achieving-customer.

Wang Q, Wu Z (2001) A duopolistic model of dynamic competitive advertising. Eur. J. Oper. Res. 128(1):213–226.

Weill P (2004) Don’t just lead govern: How top-performing firms govern IT. MIS Quart. Executive 3(1):1–17.

Yang C, Chen L (2007) Can organizational knowledge capabilities afect knowledge sharing behavior? J. Inform. Sci. 33(1): 95–109.

Yang H, Wu TCT (2008) Knowledge sharing in an organization. Tech. Forecasting Soc. Change 75(8):1128–1156.

Zmud RW (1988) Building Relationships Throughout the Corporate Entity (ICIT Press, Washington, DC).
