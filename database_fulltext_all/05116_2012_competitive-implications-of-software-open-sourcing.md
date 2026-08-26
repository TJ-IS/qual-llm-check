---
otero_id: 5116
otero_key: "HR5XJFSH"
title: "Competitive implications of software open-sourcing"
authors: "Jai Asundi; Octavian Carare; Kutsal Dogan"
year: "2012"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2012.05.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Competitive implications of software open-sourcing

Jai Asundi <sup>a,b</sup>, Octavian Carare <sup>c,d</sup>, Kutsal Dogan <sup>e,</sup>⁎

<sup>a</sup> Center for Study of Science, Technology, and Policy, India

<sup>b</sup> School of Management, University of Texas at Dallas, United States

<sup>c</sup> Federal Communications Commission, United States

<sup>d</sup> Johns Hopkins University, United States

<sup>e</sup> Ozyegin University, Turkey

## a r t i c l e i n f o

Article history: Received 1 March 2011 Received in revised form 19 January 2012 Accepted 9 May 2012 Available online 24 May 2012

Keywords: Open source software Game theory Open-sourcing

## a b s t r a c t

We analyze the economic trade-offs associated with open-sourcing, the business strategy of releasing free open-source versions of commercial software products. We argue that the effect of the release of opensource versions on the customers' perception of products is an important determinant of open-sourcing outcomes. Open-sourcing is modeled as a strategic option for duopolists that compete in a market for software products. We show that open-sourcing can arise as an equilibrium outcome in our simple two-stage game. If the enhancement of customer values from open-sourcing is moderate or high, <sup>fi</sup>rms may <sup>fi</sup>nd it optimal to release open-source versions of their products.

© 2012 Elsevier B.V. All rights reserved.

## 1. Introduction

In the past decade, the development of open-source software (OSS) has received considerable attention from practitioners and academics. There is very little doubt that the process of developing free, useful and complex software initiated by the OSS movement has made customers better off. Existing research on open-source has focused mainly on issues concerning the underlying motivation of programmers. Our interest here is of a different nature. We wish to investigate the observation, puzzling to many, that many <sup>fi</sup>rms in the current business environment choose to open-source some of their software products. In what follows, we refer to the release of a software product to the open-source community as open-sourcing. These open-sourced versions directly compete with the <sup>fi</sup>rms' commercial product offerings. The coexistence of the commercial and open-sourced versions of the same product by the same <sup>fi</sup>rm is our main research question.

The observation that many <sup>fi</sup>rms choose to open-source their products as direct competitors to their own commercial products is at <sup>fi</sup>rst sight puzzling because open-sourcing can hardly be thought of as consistent with pro<sup>fi</sup>t maximization. Clearly, the commercial product and its open-source counterpart are substitutable to some degree. It seems intuitive that by making a substitute product available free of charge, any software producer would lower its pro<sup>fi</sup>t from the sale of the commercial product. Thus, we are uneasy about the tension that arises between this apparent reduction in pro<sup>fi</sup>t and the observation that an increasing number of software <sup>fi</sup>rms choose to open-source their commercial products.

Initial interest about OSS from commercial entities has been materialized by adoption of an OSS product as a core component of a commercial product. An example is IBM's adoption of the Apache web server as a core engine for their WebSphere product. Another example is Apple's development of the Mac OS X operating system, which is based on the FreeBSD open-source operating system.

We have witnessed in the past few years an interesting and intriguing trend that constitutes, in a sense, the reverse side of OSS product adoption. An increasing number of <sup>fi</sup>rms release their products, free of charge. For instance, in October 2004, IBM released Cloudscape, a relational database product, to the Apache Software Foundation, an active member of the OSS community.<sup>1</sup> Other examples of open-sourcing include the release by Sun Microsystems of Open Of<sup>fi</sup>ce Suite, a collection of of<sup>fi</sup>ce productivity programs that are derived from their commercial product Star Of<sup>fi</sup>ce. In August 2004 Computer Associates released their database product Ingres as an open-source product. Also notably, in November of 2005 Computer Associates created a new company, Ingres Corp., to provide support and services for their OSS database product. Examples of open-sourced infrastructure software products also abound. In 2009, Citrix Systems, for example, open-sourced XenServer, a software for server virtualization.

The list of examples above is by no means meant to be exhaustive. The evidence points to an increasing number of <sup>fi</sup>rms that release “community editions” of their commercial software to customers who can download the executable programs and their source codes and run them free of charge. We <sup>fi</sup>nd this evidence rather intriguing. Why would a <sup>fi</sup>rm that enjoys a sizable stream of pro<sup>fi</sup>t from the sale and service of a product choose to create its own competition by releasing a free open-source product? How does open-sourcing affect the competitive environment faced by software <sup>fi</sup>rms? And, importantly, is there an economic mechanism through which open-sourcing can contribute to software <sup>fi</sup>rms enhancing their competitive position?

The following two quotes suggest some explanations. According to John Prial, IBM's vice president of marketing and information management software,

“By open sourcing Cloudscape, IBM hopes to accelerate development of Java-based applications and drive more innovation around Linux and Java. […] We think it will especially create new business opportunities […].” (Prial [22])

Bertrand Serlet, senior vice president of software at Apple, argues that

“[With open-source code,] thousands of people look at the critical portions of source code and check those portions are right. It's a major advantage to have open-source code.” [30]

An increased pace of innovations and improved security through increased exposure are, indeed, two of the major candidate explanations for the recent examples of open-sourcing. But are these suf<sup>fi</sup>- cient reasons to open-source a product? We argue that the answer is a quali<sup>fi</sup>ed yes.

Open-sourcing may result in product innovation and quality. The literature mentions several other reasons for open-sourcing. An important such reason is the use of open-source products by <sup>fi</sup>rms who wish to gain an advantage over their competitors. Few of the explanations in the literature, however, discuss the impact of opensource products on the customer's perception of the commercial and open-source products. We argue in what follows that the release of an open-source product affects the customers' valuations for the product. We show how this change in customer valuations, in turn, is an important determinant of a <sup>fi</sup>rm's open-sourcing strategy.

It is unlikely that the puzzle of open-sourcing can be explained by using a small set of economic arguments. It would be a signi<sup>fi</sup>cant departure from reality to expect that one can build a simple, onesize-<sup>fi</sup>ts-all economic model of open-sourcing. Instead of setting out to provide such a comprehensive model of open-sourcing, we have a more modest goal, but also one that is easier to achieve. We intend to show by way of a simple model how open-sourcing can arise as an equilibrium strategy. Even though our model is somewhat stylized, we are able to capture some of the principal economic trade-offs involved in the software developer's decision to release open-source products.

We <sup>fi</sup>nd that open-sourcing can be pro<sup>fi</sup>table in some situations. We show that open-sourcing can arise as a result of competition despite the apparent reduction in pro<sup>fi</sup>t that is caused by the diminished market share of the commercial product that is due to open-sourcing. We show that if the enhancement of customer value that results from open-sourcing is moderate or high, <sup>fi</sup>rms may <sup>fi</sup>nd it optimal to release open-source products. We also show that when the value gains to the customers from open-sourcing are high, <sup>fi</sup>rms cannot fully capture these gains. A <sup>fi</sup>rm's inability to funnel some of the customer value gains into higher pro<sup>fi</sup>ts is due to the increased level of competition that is due to open-sourcing. Overall, our results indicate that it is the customers, not the <sup>fi</sup>rms, who are likely to bene<sup>fi</sup>t the most from open-sourcing.

Our paper has two important managerial implications. First, we show that open sourcing is more likely to be an outcome of competition when <sup>fi</sup>rms anticipate that the presence of an open-source product in the marketplace enhances customer values for its commercial counterpart. This value enhancement may be primarily attributable to new product features, to bug <sup>fi</sup>xes and to improved security that arise in connection with open-sourcing. Second, as intuition suggests, increased competition from the free open-source products of their competitors erodes the pro<sup>fi</sup>ts of the <sup>fi</sup>rms that do not release open-source products.

The next section provides a review of the relevant literature. Section 3 gives a brief outline of the market for open-source products. We develop our model in Section 4 and summarize our results in Section 5. Concluding remarks are in Section 6. Some of the proofs and calculations are presented in the accompanying online Technical Appendix.

## 2. Related literature

Our work is related to the literature on OSS and to the literature on pricing of information goods. We provide <sup>fi</sup>rst a brief review of the related literature on OSS. The recent developments associated with OSS, including the emergence of Linux as a free and viable operating system option, appear to have gained some notoriety. In turn, this has signi<sup>fi</sup>cantly stimulated the interest of academics and practitioners. A few seminal articles about OSS, notably including Raymond [24], have given rise to a wave of empirical and theoretical work. Schiff [26] provides a comprehensive survey of this early literature on OSS. The current research on OSS can be classi<sup>fi</sup>ed into three broad categories (see [32]). Analysis of the motivations of open source contributors is by far the most popular research topic, perhaps because at its core is the puzzling observation that cohorts of talented programmers choose to contribute to OSS projects with no apparent compensation. This stream of research includes empirical and theoretical papers that aim to explain the motivations of OSS contributors (see [4,13,19]).

Unlike the programmers of most commercial software projects, OSS project contributors are volunteers located in various parts of the world. Topics concerning the governance, organization and innovation processes associated with OSS constitute the second main stream of OSS research. Some of the important research issues include the challenges of managing OSS projects, such as the allocation of tasks and responsibilities, the management of innovation, and the scheduling of product feature enhancements and OSS product releases [17,20,29].

The third stream of research is focused on the competition between open source and traditional. closed-source software, This stream of research includes empirical and theoretical analyses of the public and free nature of OSS products and their impact on the marketplace [5,6,9,21]. Our paper belongs to the third stream of OSS research. We seek to provide some economic explanations for the increased incidence of <sup>fi</sup>rms that compete by releasing open-source counterparts of their proprietary software products. Like our analysis, a few studies examine hybrid business models that include proprietary and open source software [5,18]. Krishnamurthy [18] analyzes business models of <sup>fi</sup>rms that package, use or provide services for code produced primarily by the OSS community. Bonaccorsi et al. [5] survey Italian <sup>fi</sup>rms that have combined proprietary and open source offerings under differing licensing schemes. They provide evidence indicating that <sup>fi</sup>rms are keen to adopt new hybrid models. Wichmann [34] provides an early account of the motivations of large <sup>fi</sup>rms that participate in OSS activities. Some of the motivations of large <sup>fi</sup>rms suggested by Wichmann include the enhancement of a <sup>fi</sup>rm's business prospects in a market of a complementary good (e.g., hardware or services), strategic considerations like the adoption of Java-based technologies and the need for product standardization that could enable compatibility among various subsystems, like the adoption of open document formats for word processing software. Lerner and Tirole [19] view open-sourcing as the “razor” that is given for free (the code) to sell more “razor blades” (the hardware that is a complement for their code). They emphasize that opensourcing is more likely to be a strategic tool for <sup>fi</sup>rms that are too small to compete or who are lagging behind in the commercial segment. Fosfuri et al. [11] investigate the interest of pro<sup>fi</sup>t-oriented <sup>fi</sup>rms in OSS products. Their empirical study highlights the importance of market position and technological capabilities in a commercial <sup>fi</sup>rm's decision to introduce OSS products. The empirical study of Rossi and Bonaccorsi [25] discusses the motivations of Italian <sup>fi</sup>rms that choose to open their proprietary code. An important motivation in their study is that <sup>fi</sup>rms that open their code expect to obtain contributions and feedback in order to <sup>fi</sup>x bugs and improve the software. Other explanations for open-sourcing include, as perhaps best articulated by IBM's Jon Prial Prial [22], an increase in the rate of innovations and the resulting increase in demand for a complementary commercial product of the same <sup>fi</sup>rm.

A few studies examine the competition between commercial software and OSS. Casadesus-Masanell and Ghemawat [6] analyze the dynamic interaction in a vertically differentiated duopoly consisting of a pro<sup>fi</sup>t-maximizing <sup>fi</sup>rm and a competitor that prices its output at marginal cost. Their model is inspired by the competition between Linux and Windows and emphasizes dynamic network externalities that arise as a result of demand-side learning. Similarly inspired by the competition between Windows and Linux, Economides and Katsamakas [9] develop a framework for the two-sided pricing strategy of a software product developer whose product serves as a platform for complementary applications. The studies of [6], and [9] assume the existence of an OSS product without speci<sup>fi</sup>cally addressing the determinants of a <sup>fi</sup>rm's decision to open source.

Hawkins [14] makes an important point that the release of code may be pro<sup>fi</sup>table because it entails a reduction in the cost of maintaining the code. The basic economic trade-off of open-sourcing is between the increase in the buyers' willingness to pay and the loss of market share that arises as a result of providing a free substitute (and any additional costs incurred in the process of supporting the free substitute software). Mustonen [21] develops a model in which a <sup>fi</sup>rm can choose to support a rival “copyleft free” software to gain compatibility. The <sup>fi</sup>rm's decision not to support the rival software results in incompatibility between its commercial program and the freely available substitute. In Mustonen [21], compatibility is viewed as a way to increase the customer's willingness to pay for the commercial product because of network effects. The model is similar to ours in that it considers customers who are heterogeneous with respect to their valuations of the competing products, but in his model only one <sup>fi</sup>rm acts strategically. A similar analysis by Sen [28] explores the competition between proprietary software, an OSS product and a commercially-supported offering of the OSS product. The three products are modeled to differ in terms of their usability. Customers with the highest valuation for usability end up purchasing the proprietary software, while customers with an intermediate valuation for usability purchase the commercial open-source product, and the rest use the free open-source software. Product differentiation in Sen's model arises because of different product documentation and support services, not because of different product characteristics as proposed in our model. August et al. [1] consider a model in which a <sup>fi</sup>rm chooses between open- and closed-source architectures. Pro<sup>fi</sup>ts are obtained from services such as integration, support and consulting associated with the open source product. Choosing the open-source alternative enables a competitive developer to enter the market to provide services for the same product. Their model analyzes the impact of increased competition in the services market. They <sup>fi</sup>nd that the developer may forgo pro<sup>fi</sup>ts from product sales and rely on an open-sourcing strategy to enhance the pro<sup>fi</sup>ts from the services market.

Our work is also related to the literature on the pricing of information goods, in particular, to the work on versioning of information goods [2,3,8,12,15,16,23,31,33]. These studies focus on situations in which a <sup>fi</sup>rm releases quality-differentiated versions of an information good. Each differentiated version creates an opportunity for increased pro<sup>fi</sup>ts through price discrimination, but the release of a new version carries a danger of cannibalizing the sales of other versions. The versioning literature also considers additional factors like the existence of network externalities, different market structures and the type of product differentiation (vertical or horizontal) as determinants of a <sup>fi</sup>rm's versioning decision. While, like most models of versioning, our model views the open source product as a differentiated version of the closed-source product, our model does not view open-sourcing as a tool for price discrimination or as a source of network effects. The fundamentals of our model parallel those of versioning models, but in our model open-sourcing does not entail the same economic trade-offs that occur in connection with versioning.

The explanations given in the literature for the existence of open source software, while providing valuable insight, go only some way toward identifying the reason why software <sup>fi</sup>rms choose to opensource their products. In the academic literature and in the media, two stories seem to coalesce as the most likely candidate explanations for open-sourcing. First, the release of open-source products increases market size, so that <sup>fi</sup>rms bene<sup>fi</sup>t from the sale of complementary products or services. Second, the release of open-source products reduces the cost of maintaining and debugging the code. The logic of both arguments relies on the fact that open-sourcing may be, from a dynamic perspective, pro<sup>fi</sup>table for a software <sup>fi</sup>rm. Both explanations rely on the intuition that a favorable economic trade-off arises for an open sourcing software <sup>fi</sup>rm between short run losses in revenue that stem from “customer loss” (i.e., the reduction of revenue that arises as a result of making a substitute product available free of charge) and, in the long run, increased pro<sup>fi</sup>tability that is due to higher revenues or lower costs. Clearly, the intuition behind this argument is misguided. If the main consequence of open-sourcing is an increase in the number of customers who use a product, market size could also be increased through free distribution of closed-source software. Free distribution could also result in better testing and reporting of bugs. Furthermore, the reduction in the cost of maintaining or debugging the source code achieved as a result of “more eyeballs” scanning the released source code for bugs could be achieved through the release of the source code to a set of quali<sup>fi</sup>ed <sup>fi</sup>rms or individuals, and not to the community at large.

It is unlikely that the economic drivers of a <sup>fi</sup>rm's decision to release open source products could be clearly and easily enumerated. A <sup>fi</sup>rm's open-sourcing decision is affected by a multitude of factors. Some of these factors are identi<sup>fi</sup>ed in the literature. Our contribution is to bring to the fore an important, yet little explored aspect of opensourcing: the impact of open source releases on the customer's valuation of the product. In the next section we highlight some of the important characteristics of open-source products and explore the ways in which these characteristics affect the customer's perception of open- and closed-source products.

## 3. OSS market and products

Hardly any online forum devoted to a particular software product lacks complaints concerning the product features or, more often, the absence of desired features. In their out-of-the-box state, most software products fail to meet all the requirements of <sup>fi</sup>rms and individuals that buy them. The adoption of a particular software product by customers (<sup>fi</sup>rms and individuals) is typically associated with the modi<sup>fi</sup>cation of a basic underlying software product. By modi<sup>fi</sup>cation we mean altering the characteristics and functionality of a product in order to suit the needs and to integrate within the existing infrastructure of a customer.

The lack of access to elements of the code that affect functionality makes closed-source products less modi<sup>fi</sup>able than OSS products. Access to the source of the program in the latter type of product enables easier modi<sup>fi</sup>cations by OSS users. Indeed, OSS users may go as far as to signi<sup>fi</sup>cantly change the product's functionality to integrate it with their information systems. Users of closed-source software products are typically restricted to making only minor customization changes to the closed-source products. Some of their business processes or technologies may need to be changed in order to effectively integrate the closed software. Clearly, the time and effort spent incorporating desired functionality into OSS products or adapting to the requirements of closed-source products are re<sup>fl</sup>ected in costs incurred by the user. Our view is that the cost of customizing an open source product is in general lower than the cost of adapting to the requirements and customizing, to the extent possible, its commercial counterpart.

Intimately related to open-sourcing is the issue of perception of OSS by the customer. Some customers may have a hard time assessing whether an open-source product has the same performance as the original, proprietary product (or a competing developer's product).<sup>2</sup> Consider the following example. SugarCRM is a provider of commercial open source customer relationship management software for companies with several deployment options to suit the customer's security, integration and con<sup>fi</sup>guration needs. They offer two distinct products: Sugar Enterprise Edition and Sugar Community Edition. The Community Edition allows users to view and change the source as long as they follow the Sugar Public License (currently GPLv3). Unlike the free Community Edition, the Enterprise Edition is provided to users at a cost. In addition to price, users of the Sugar software may perceive other differences between the enterprise and the Community Editions. The Community Edition lacks the functionality required to create teams or to assign access levels to the teams [10]. The inability to keep users from deleting each other's contacts, schedules, leads, etc. makes the Community Edition relatively un<sup>fi</sup>t for commercial use. The Enterprise Edition does offer these functional elements. SugarCRM employs full-time developers and the new features incorporated into the commercial product are generally missing from the free OSS product. The SugarCRM example indicates that the OSS counterpart of the proprietary software product is “crimped” in that it has reduced functionality. The concept of crimping is not new. Deneckere and McAfee [7] describe product crimping in the context of technology products. Our example from the software industry is similar in that the commercial developer incurs a cost to provide the lower functionality product. However, the analogy breaks down when we consider that sophisticated OSS users may re-establish the “crimped” functionality by re-writing the relevant code. The free availability of the source code allows the user to make changes to the product at a cost that we believe is lower than the cost of changing the functionality of the proprietary product.

Our model formalizes these features of open-source products. We examine a market where the commercial version of a product provides more functionality (and thus, more intrinsic value to the customers) than the OSS version. We analyze how the impact of open-sourcing on customer's values affects the <sup>fi</sup>rm's decision to provide an opensource version in addition to its commercial product offerings. We model the co-existence of open-source and commercial versions of a product by the same <sup>fi</sup>rm.

## 4. The model

We consider the incentives for open-sourcing in a duopoly where the two <sup>fi</sup>rms are selling comparative software products. Even though our model may seem more appropriate for desktop software, we do observe several examples of infrastructure software being released as open-source. These applications include VMWare's Zimbra and Citrix's XenServer. SugarCRM may also, at least in part, fall into this category. We would thus like to believe that our model might well be applicable to all types of software as long as the assumptions of price, <sup>fi</sup>t cost and bene<sup>fi</sup>ts we describe next hold.<sup>3</sup> The strategies of the <sup>fi</sup>rms in our model include a decision to open-source their output by introducing an additional open-sourced versions of their products. These additional versions would compete with each <sup>fi</sup>rm's own commercial version as well as its competitor's open-source and/or commercial products. Prior work (Sen [28], August et al. [1]) analyzes the competition between an OSS alternative and a closed-source commercial alternative, and shows that there may be bene<sup>fi</sup>ts to open-sourcing when services are considered in conjunction with the software product. However, these papers do not focus on the <sup>fi</sup>rm's incentives to open-source their products in the absence of competition in the services market. In contrast, our model analyzes the competition between closed- and open-source products as an outcome of the <sup>fi</sup>rm's strategic decisions to open source their products. Also, our model assumes that differentiation is embodied in the product itself and not due to differences in documentation and support services. While often software and service are not easy to disentangle, we gain some modeling <sup>fl</sup>exibility by focusing only on the product market.

We model the variability of the <sup>fi</sup>t of a software product to a <sup>fi</sup>rm's existing systems and needs using a spatial model of product differentiation. As it is commonplace in the literature on product differentiation, we assume that the two <sup>fi</sup>rms are located at the ends of a line segment of unit length and share a measure of customers that we normalize to one without loss of generality. We also assume that the customers are continuously (and uniformly) distributed over the unit length segment and that a customer demands at most one product. We interpret the location of a customer relative to a <sup>fi</sup>rm as that customer's ideal product requirement. A customer who is closer to a given <sup>fi</sup>rm incurs a smaller disutility to use the <sup>fi</sup>rm's software than a customer who is farther away. As such, we model customers as heterogeneous in their <sup>fi</sup>t for the products of the two <sup>fi</sup>rms. We assume that the two <sup>fi</sup>rms are symmetric in all relevant attributes, except location. To operationalize the notion of <sup>fi</sup>t, we assume that customers incur a speci<sup>fi</sup>c unit fit cost (τ) to use a given software. Given the symmetry of the <sup>fi</sup>rms, at equal prices, a customer prefers the <sup>fi</sup>rm that is closer. In this sense, customers located relatively close to a <sup>fi</sup>rm are “captive” and thus each <sup>fi</sup>rm does enjoy some degree of market power.

Fig. 1 provides a depiction of our main setup. Let x denote the distance of a customer from Firm 1 on the unit line. The customer could purchase the output of either <sup>fi</sup>rm. We assume that customers purchase at most one unit of output from either of the two <sup>fi</sup>rms. If the customer buys the closed-source product of Firm 1, the customer enjoys utility $V - \tau x - P _ { 1 } .$ . If the customer buys the closed-source product of Firm 2, the customer enjoys utility level $V { - \tau ( 1 - x ) - P _ { 2 } } .$

Either <sup>fi</sup>rm has the option of open-sourcing its software product. We note that the closed-source product provides additional value through the use of proprietary features such as specialized tools for archiving or for management, clip art, etc. Since these enhancements are available only to purchasers of the commercial product, the opensource product lacks these proprietary features. As such, the opensource product provides customers with less value than the commercial product.<sup>4</sup> We denote this reduction in value by $\varDelta _ { 3 } .$ . In addition, we recognize that users of both products (commercial and open-source) gain additional value from the availability of the source-code of the open-source product be due to various bug <sup>fi</sup>xes that are offered by the product users. It must be noted that the commercial and the open-source products share the same code-base. Hence, the availability of the source code allows all users to inspect the source code and identify bug <sup>fi</sup>xes or develop enhancements that are available to all users. Even though a customer may purchase the commercial version to get the additional functionality, it can and may still inspect the code-base and provide feedback, this is speci<sup>fi</sup>cally true for infrastructure software. We denote this increase in value by $\varDelta _ { 1 } .$ . Accordingly, we assume that the value of the commercial product to a customer is $V +$ $\varDelta _ { 1 } .$ . Letting $\Delta _ { 2 } = \Delta _ { 3 } - \Delta _ { 1 } ,$ , the value of the OSS product becomes $V -$ $\varDelta _ { 2 } .$ We assume that $\varDelta _ { 1 , 2 } > 0$ . Note that the term $\Delta _ { 1 } + \Delta _ { 2 }$ represents the difference in value associated with purchasing the commercial product over its open-source counterpart. Since we view that the OSS product is more easily modi<sup>fi</sup>able than the closed-source product, we assume that a customer's <sup>fi</sup>t cost for the open-source product is ατ where $0 { \le } \alpha { \le } 1$ . It follows that a customer located at distance x in product space from the <sup>fi</sup>rst <sup>fi</sup>rm enjoys utility levels $U C _ { 1 } = \left( V + \Delta _ { 1 } \right) -$ $\tau x - P _ { 1 } ,$ , and $U C _ { 2 } = ( V + \Delta _ { 1 } ) - \tau ( 1 - x ) - P _ { 2 }$ if the customer buys the closed-source product from Firm 1 and Firm 2, respectively. If the customer chooses the open-source alternative of either <sup>fi</sup>rm, the customer's net utility level $U O _ { 1 } = \left( V - \Delta _ { 2 } \right)$ −ατx, or $U 0 _ { 2 } = ( V - \Delta _ { 2 } ) - \alpha \tau ( 1 - x ) .$ . Implicit in our de<sup>fi</sup>nition of open-sourcing is that the OSS products are offered free of charge by the two <sup>fi</sup>rms. We take as given in our model, without loss of generality, that customers have the ability to install and use the open-source products without $\cos t ^ { 5 }$

<table><tr><td colspan="3">User Market(V, τ)</td></tr><tr><td>Firm 1</td><td>x</td><td>Firm 2</td></tr></table>

Fig. 1. Market for a software product in duopoly.

Before analyzing the possible outcomes in market con<sup>fi</sup>gurations involving open-sourced products, we note that our analysis focuses only on those situations where all customers in the market are served prior to the <sup>fi</sup>rms' decision to open-source. The parameters of our model can be chosen so that the two <sup>fi</sup>rms are each local monopolies. In such situations, open sourcing by a <sup>fi</sup>rm may result in an increase in the market share of the commercial product, and indeed open sourcing may result in higher pro<sup>fi</sup>ts. To see this, note that the two <sup>fi</sup>rms in our model are local monopolies prior to choosing their open-sourcing strategy when $V { < } \tau .$ Intuitively, the higher the <sup>fi</sup>t cost, the more customers become captive to the <sup>fi</sup>rm that is closest to them. If the <sup>fi</sup>t cost is high relative to values, some customers would forgo purchases altogether, and thus a <sup>fi</sup>rm's pricing decision has no effect on the other <sup>fi</sup>rm's pro<sup>fi</sup>t. It is easily shown that a <sup>fi</sup>rm's pro<sup>fi</sup>t in a local monopoly con<sup>fi</sup>guration is equal to $V ^ { 2 } / ( 4 \tau )$ . Open sourcing in such situations may increase the market share of a <sup>fi</sup>rm's commercial product. In particular, when $\tau > \frac { \Delta _ { 1 } + \Delta _ { 2 } } { 1 - \alpha }$ (i.e., when the difference between the value of the open-source and the commercial products is small relative to the reduction of <sup>fi</sup>t cost as a result of open-sourcing), the market share of each <sup>fi</sup>rm's commercial product is less than 1/2, so the two <sup>fi</sup>rms do not compete head-tohead with their commercial products. Furthermore, whenever $\Delta _ { 1 } + \Delta _ { 2 }$ also satis<sup>fi</sup>es $\Delta _ { 1 } + \Delta _ { 2 } > V \sqrt { 1 - \alpha } ,$ that ${ \mathrm { i } } s ,$ when the difference in value between the closed- and open-source products of a <sup>fi</sup>rm is large relative to the value prior to the release of the open-source version, it can be shown that a <sup>fi</sup>rm's pro<sup>fi</sup>t increases as a result of open-sourcing. However, we <sup>fi</sup>nd these situations strategically less interesting because in equilibrium the open-sourcing decision of a <sup>fi</sup>rm that maintains its local monopoly status does not affect the pro<sup>fi</sup>ts of its opponent. We thus focus only on those situations in which open-sourcing has strategic implications. We discuss next the outcomes of the various modes of competition.

## 4.1. Duopoly with closed-source products

The simplest case in our environment is that of two <sup>fi</sup>rms competing with closed-source products.

Let $x _ { 0 }$ denote the location of the customer who is indifferent between purchasing a closed-source product from either <sup>fi</sup>rm. We use subscript 0 to indicate outcomes that are obtained in a closedsource duopoly. All customers to the left of $x _ { 0 }$ prefer to purchase the output of Firm 1, whereas the customers to the right of $x _ { 0 }$ prefer to purchase the output of Firm 2. The pro<sup>fi</sup>t functions for Firm 1 and Firm 2 respectively are: $\pi _ { 1 0 } = x _ { 0 } P _ { 1 0 }$ and $\pi _ { 2 0 } = ( 1 - x _ { 0 } ) P _ { 2 0 } .$ . Since the customer located at $x _ { 0 }$ is indifferent between purchasing either product, we have $x _ { 0 } = \frac { P _ { 2 0 } - P _ { 1 0 } + \tau } { 2 \tau } .$ In equilibrium, the two <sup>fi</sup>rms choose their prices $P _ { 1 0 }$ and $P _ { 2 0 }$ to maximize their pro<sup>fi</sup>t, given that their opponent's price is at the equilibrium level. Since the <sup>fi</sup>rms are symmetric, we are looking for a symmetric equilibrium that entails $P _ { 1 0 } = P _ { 2 0 } .$ . Fixing Firm 2's price at its equilibrium level $P _ { 2 0 } ,$ Firm 1's pro<sup>fi</sup>t as a function of its price P is:

$$
\pi_ {1} (P) = P \frac {P _ {2 0} - P + \tau}{2 \tau}
$$

maximizing with respect to P and requiring that, by symmetry, the pro<sup>fi</sup>t-maximizing price be equal to $P _ { 2 0 }$ yields $P _ { 1 0 } = P _ { 2 0 } = \tau$ . Intuitively, as customers incur a higher <sup>fi</sup>t cost they become more captive, and thus the <sup>fi</sup>rms enjoy more market power and could afford to increase their prices. The equilibrium pro<sup>fi</sup>ts of the two <sup>fi</sup>rms are $\pi _ { 1 0 } = \pi _ { 2 0 } = \frac { \tau } { 2 } ,$ consistent with the notion that more market power, indicated by higher customer <sup>fi</sup>t costs, translates into higher pro<sup>fi</sup>ts for the two <sup>fi</sup>rms. Having established our benchmark, we turn next to an analysis of competition in which one of the firms also offers an open-source product.

## 4.2. Duopoly with only one firm offering an open-source product

Suppose Firm 1 decides to offer, free of charge, an open-source version of its commercial software product. The introduction of the open-source product has two main effects. First, some of Firm 1's customers would <sup>fi</sup>nd it more pro<sup>fi</sup>table to choose the free open-source product. This effect works so as to reduce the pro<sup>fi</sup>t of Firm 1. The second effect entails making Firm 2 compete with the free open-source product of Firm 1. This essentially works so as to dampen the effect on Firm 1's pro<sup>fi</sup>ts of changes in the price charged by Firm 2, and also as a way for Firm 1 to “steal” some of Firm 2's customers. It is important to note that the customer who is indifferent between acquiring the product of either <sup>fi</sup>rm is contemplating a choice between the free open-source product of Firm 1 and the commercial closed-source product of Firm 2.

Analyzing competition in the presence of an open-source product is somewhat complicated because, depending on the model parameters, three con<sup>fi</sup>gurations are possible involving varying measures of customers who acquire some of the three products. We depict the most general situation in Fig. 2 below.

The customer located at $x _ { 1 1 }$ is indifferent between the OSS product and the commercial product offered by Firm 1. The customer located at $y _ { 1 1 }$ is indifferent between the OSS product (Firm 1's) and the commercial product offered by Firm 2.

$$
\text { User   Market } (V + \Delta_ {1}, V - \Delta_ {2}, \tau , \alpha) \tag {Firm1}
$$

Fig. 2. Market for software products in duopoly where Firm 1 has open-sourced.

## 4.2.1. Interior solution

We start with an analysis of the “interior solution” in which nonzero measures of customers choose each of the three products.<sup>6</sup> We use superscript I to identify the corresponding parameters. In this setting, all customers to the left of $x _ { 1 1 } ^ { I }$ purchase Firm 1's closedsource commercial product, while all customers located to the right of $y _ { 1 1 } ^ { I }$ purchase Firm 2's commercial product. The customers located between $x _ { 1 1 } ^ { I }$ and $y _ { 1 1 } ^ { I }$ <sup>fi</sup>nd it optimal to use Firm 1's OSS product. It follows that a fraction $x _ { 1 1 } ^ { I }$ of the customers purchase Firm 1's commercial product and that a fraction $1 - y _ { 1 1 } ^ { I }$ of the customers purchase Firm 2's commercial product. The remaining fraction $y _ { 1 1 } ^ { I } - x _ { 1 1 } ^ { I }$ of customers choose Firm 1's OSS product. Given the demands for the three products, we can write down the two <sup>fi</sup>rms' pro<sup>fi</sup>ts as $\pi _ { 1 1 } ^ { I } = x _ { 1 1 } ^ { I } P _ { 1 } ^ { I } .$ <sub>1</sub> and $\pi _ { 2 1 } ^ { I } = ( 1 - y _ { 1 1 } ^ { I } ) P _ { 2 1 } ^ { I }$ <sub>1</sub>, where $P _ { i 1 } ^ { I }$ is the price charged by Firm i.

To <sup>fi</sup>nd x<sup>I</sup> and $y _ { 1 1 } ^ { I }$ we need to set $U C _ { 1 } = U O _ { 1 }$ and $U O _ { 1 } = U C _ { 2 }$ . Doing so, we <sup>fi</sup>nd that:

$$
x _ {1 1} ^ {I} = \frac {\Delta_ {1} + \Delta_ {2} - P _ {1 1} ^ {I}}{\tau (1 - \alpha)}
$$

and

$$
y _ {1} ^ {I} = \frac {P _ {2 1} ^ {I} + \tau - \Delta_ {2}}{\tau (1 + \alpha)}.
$$

Since in equilibrium the two <sup>fi</sup>rms choose prices to maximize pro<sup>fi</sup>t, differentiating the two <sup>fi</sup>rms' pro<sup>fi</sup>ts with respect to prices and solving for the two prices yields $P _ { 1 1 } ^ { I } = \frac { \Delta _ { 1 } + \Delta _ { 2 } } { 2 }$ and $P _ { 2 1 } ^ { I } = \frac { \alpha \tau + \Delta _ { 2 } } { 2 }$ . In equilibrium, these prices give rise to values of $x _ { 1 1 } ^ { I }$ and $y _ { 1 1 } ^ { I }$ that can be expressed as:

$$
x _ {1 1} ^ {I} = \frac {\Delta_ {1} + \Delta_ {2}}{2 \tau (1 - \alpha)}
$$

and

$$
y _ {1 1} ^ {I} = \frac {\tau (2 + \alpha) - \Delta_ {2}}{2 \tau (1 + \alpha)}.
$$

In equilibrium the pro<sup>fi</sup>ts of the two <sup>fi</sup>rms are:

$$
\pi_ {1 1} ^ {I} = \frac {\left(\Delta_ {1} + \Delta_ {2}\right) ^ {2}}{4 \tau (1 - \alpha)}
$$

and

$$
\pi_ {2 1} ^ {I} = \frac {\left(\alpha \tau + \Delta_ {2}\right) ^ {2}}{4 \tau (1 + \alpha)}.
$$

We need to ensure that, according to our assumption, the parameters of our model are chosen so that $0 { < } x _ { 1 1 } ^ { I } { < } y _ { 1 1 } ^ { I } { < } 1$ . It is readily veri<sup>fi</sup>ed that, given our choice of parameters, $x _ { 1 1 } ^ { I } > 0$ and $y _ { 1 1 } ^ { I } < 1$ . To ensure that $x _ { 1 1 } ^ { I } < y _ { 1 1 } ^ { I }$ , we require that:

$$
\Delta_ {1} <   \frac {(2 + \alpha) (1 - \alpha) \tau - 2 \Delta_ {2}}{1 + \alpha}.\tag{1}
$$

When condition (1) is satis<sup>fi</sup>ed, there is a positive measure of customers who choose the free OSS version. Since some of these customers could have purchased the commercial product of Firm 1, we term the segment of customers who choose the free OSS version “customer loss.” It turns out that, depending on the choice of parameters, it is possible that customer loss could be avoided altogether by the <sup>fi</sup>rm that releases an open-source product. We turn next to an analysis of this situation.

## 4.2.2. No customer loss $( y _ { 1 1 } \leq x _ { 1 1 } )$

If condition 1 is not satis<sup>fi</sup>ed, all customers prefer Firm 1's commercial product to its free OSS version available. Intuitively, Eq. (1) is more likely to be violated if Δ or $\varDelta _ { 2 } - 0 \mathrm { r }$ both Δ and $\Delta _ { 2 } \mathrm { ~ - ~ } \mathrm { i } s$ relatively high, implying that the inherent value of the additional features offered in the commercial version is suf<sup>fi</sup>ciently higher than in the free OSS version. Note that the <sup>fi</sup>rms' commercial offerings compete head-to-head in this case. To <sup>fi</sup>nd conditions under which there is no customer loss, we assume that while no customer <sup>fi</sup>nds it optimal to use the OSS version, Firm 1's commercial product still bene<sup>fi</sup>ts from the release of the open-source product (perhaps through a better management of code errors). Let superscript II denote this region. The pro<sup>fi</sup>ts of the two <sup>fi</sup>rms are: $\pi _ { 1 1 } ^ { I I } \dot { = } x _ { 1 1 } ^ { I I } P _ { 1 1 } ^ { I I }$ and $\pi _ { 2 1 } ^ { I I } = ( 1 - x _ { 1 1 } ^ { I I } ) P _ { 2 1 } ^ { I I }$ Since the two commercial versions compete head-to-head, we <sup>fi</sup>nd $x _ { 1 1 } ^ { I I }$ by solving for x in $U C _ { 1 } = U C _ { 2 }$ (note also that we need to check that $\bar { x } _ { 1 1 } ^ { I I } \in ( 0 , \bar { 1 } )$ , so that Firm 2 still serves a fraction of the market). Straightforward calculations yield equilibrium prices chosen by the two <sup>fi</sup>rms that can be expressed as $P _ { 1 1 } ^ { I I } = \tau + \frac { \Delta _ { 1 } } { 3 }$ and $P _ { 2 1 } ^ { I I } = \tau - \frac { \Delta _ { 1 } } { 3 }$ Thus, in equilibrium

$$
x _ {1 1} ^ {I I} = \frac {3 \tau + \Delta_ {1}}{6 \tau}.
$$

Note that Firm 1 enjoys a higher market share than in the benchmark case of Section 4.1 because of the higher value that customers have for its product. The equilibrium pro<sup>fi</sup>ts of the two <sup>fi</sup>rms can be written as:

$$
\pi_ {1 1} ^ {I I} = \frac {(3 \tau + \Delta_ {1}) ^ {2}}{1 8 \tau}\tag{2}
$$

and

$$
\pi_ {2 1} ^ {I I} = \frac {(3 \tau - \Delta_ {1}) ^ {2}}{1 8 \tau}.\tag{3}
$$

If the value enhancement provided by the open-source product is large enough, Firm 2 may be driven out of the market entirely. We present an analysis of this case below.

## 4.2.3. Firm 2 is driven out of the market $\left( x _ { 1 1 } \ge 1 \right)$

We use superscript III to indicate the parameter region where $x _ { 1 1 } \geq 1$ . It can be easily checked that when the following condition holds, Firm 2 can no longer compete and Firm 1 becomes a monopoly:

$$
\Delta_ {1} \geq 3 \tau\tag{4}
$$

Note that, as in the previous case, customers prefer the commercial version of Firm 1's product to its open-source alternative. Thus, it turns out that to maximize its pro<sup>fi</sup>t Firm 1 chooses price $P _ { 1 1 } ^ { I I I } = \Delta _ { 1 } - \tau$ and has pro<sup>fi</sup>t $\pi _ { 1 1 } ^ { I I I } = \Delta _ { 1 } - \tau .$

Having exhausted the set of possible outcomes when one of the <sup>fi</sup>rms opens up its source code, we turn to an analysis of competition when both <sup>fi</sup>rms offer an open-source product.

## 4.3. Duopoly with open-source products

When both <sup>fi</sup>rms decide to open their products, there are four products in the market. The most general market situation is depicted in Fig. 3 below in which non-zero measures of customers choose to purchase one of the four products.

In Fig. 3, the customer at $x _ { 1 2 }$ is indifferent between the OSS product and the commercial product offered by Firm 1, while the customer located at distance $y _ { 1 2 }$ from Firm 1 is indifferent between the two OSS products. In addition, the customer located at $x _ { 2 2 }$ is indifferent between Firm 2's OSS product and the commercial product of Firm 2.

## 4.3.1. Interior solution

As above, we start with an analysis of the situation in which nonzero measures of customers choose each of the four products. Let superscript I denote the corresponding parameter region. In this setting, all customers who are located on the left of $\cdot _ { x _ { 1 2 } ^ { I } }$ purchase Firm 1's closed-source commercial product and all customers located on the right of $x _ { 2 2 } ^ { I }$ purchase Firm ${ 2 ^ { \prime } s }$ commercial product. The customers who are located between $x _ { 2 2 } ^ { I }$ and $x _ { 1 2 } ^ { I }$ use either Firm 1's or Firm 2's free OSS product. Note that these customers do not contribute to the pro<sup>fi</sup>ts of either <sup>fi</sup>rm, so their choice of Firm 1's or Firm 2's OSS product has no effect on the two <sup>fi</sup>rms' pro<sup>fi</sup>ts. In this situation, Firm 1 sells its commercial product to a fraction $x _ { 1 2 } ^ { I }$ of the customers, while a fraction $1 - x _ { 2 2 } ^ { I }$ of the customers choose Firm 2's commercial product. A fraction of customers equal to $x _ { 2 2 } ^ { I } - x _ { 1 2 } ^ { I }$ choose one of the two OSS products. Once again we refer to the segment of customers of measure $x _ { 2 2 } ^ { I } - x _ { 1 2 } ^ { I } \ \mathsf { a s }$ ‘loss.’ Given these demands, the pro<sup>fi</sup>t functions of Firm 1 and Firm 2 are $\pi _ { 1 2 } ^ { I } = x _ { 1 2 } ^ { I } P _ { 1 2 } ^ { I }$ and $\pi _ { 2 2 } ^ { I } = \bar { ( 1 - x _ { 2 2 } ^ { I } ) } P _ { 2 2 } ^ { I }$ Note that $x _ { 1 2 } ^ { I }$ is determined by solving for x when $U C _ { 1 } = U O _ { 1 } .$ . Similarly, $y _ { 1 2 } ^ { I }$ can be found by setting $U O _ { 1 } = U O _ { 2 } $ <sub>2</sub> and $x _ { 2 2 } ^ { I }$ is found by solving for x in $U O _ { 2 } = U C _ { 2 }$ . Straightforward calculations yield $x _ { 1 2 } ^ { I } =$ $( \varDelta _ { 1 } + \varDelta _ { 2 } - P _ { 1 2 } ^ { I } ) / ( \tau ( 1 - \alpha ) ) , y _ { 1 2 } ^ { I } = 1 / 2$ and $x _ { 2 2 } ^ { I } = 1 - ( \Delta _ { 1 } + \Delta _ { 2 } - P _ { 2 2 } ^ { I } ) /$ $( \tau ( 1 - \alpha ) )$

Differentiating the pro<sup>fi</sup>t functions of the two <sup>fi</sup>rms with respect to their prices, and solving for the prices that jointly maximize the two <sup>fi</sup>rms' pro<sup>fi</sup>ts yield:

$$
P _ {1 2} ^ {I} = P _ {2 2} ^ {I} = (\Delta_ {1} + \Delta_ {2}) / 2.\tag{5}
$$

The equilibrium values of $x _ { 1 2 } ^ { I } , \ y _ { 1 2 } ^ { I }$ and $x _ { 2 2 } ^ { I }$ are $x _ { 1 2 } ^ { I } = ( \varDelta _ { 1 } + \varDelta _ { 2 } ) /$ $( 2 \tau ( 1 - \alpha ) ) , y _ { 1 2 } ^ { I } { = } 1 / 2 \ \mathrm { a n d } \ x _ { 2 2 } ^ { I } { = } 1 - ( \Delta _ { 1 } { + } \Delta _ { 2 } ) / ( 2 \tau ( 1 - \alpha ) )$

Hence, the equilibrium pro<sup>fi</sup>ts of the two <sup>fi</sup>rms can be written as:

$$
\pi_ {1 2} ^ {I} = \pi_ {2 2} ^ {I} = \frac {\left(\Delta_ {1} + \Delta_ {2}\right) ^ {2}}{4 \tau (1 - \alpha)}.\tag{6}
$$

Note that since the assumed solution entails non-zero measures of customers that use any of the four products, we need $x _ { 1 2 } ^ { I } < y _ { 1 2 } ^ { I } < x _ { 2 2 } ^ { I } .$ Since the <sup>fi</sup>rms are symmetric, this translates into a single condition involving the two $\Delta ^ { \prime } s .$ . It can be checked that if the following condition is to be satis<sup>fi</sup>ed in order for the parameters to yield such a solution:

$$
\Delta_ {1} <   (1 - \alpha) \tau - \Delta_ {2}.\tag{7}
$$

When this condition is violated, in equilibrium both $x _ { 1 2 } \geq y _ { 1 2 }$ and $y _ { 1 2 } \ge x _ { 2 2 }$ . We derive the <sup>fi</sup>rms' optimal pricing solution in this case next.

## 4.3.2. No customer loss $( x _ { 2 2 } = x _ { 1 2 } )$

In this case, the two <sup>fi</sup>rms compete head-to-head with their closed-source commercial products. As above, we maintain the assumption that the release of the open-source product increases the value that customers derive from using the commercial version of a product, even though no customer could gain utility from using an open-source product. It turns out that, with or without this assumption, the equilibrium has the same properties as the equilibrium that we analyzed in the benchmark case above (so that $x _ { 2 2 } ^ { I I }$ is equal to 1/2 and the pro<sup>fi</sup>ts of the two <sup>fi</sup>rms are equal, $\pi _ { 1 2 } ^ { I I } = \pi _ { 2 2 } ^ { I I } = \tau / 2 )$

Having established the outcome of competition in all possible situations in our model, we turn next to an analysis of the incentives that <sup>fi</sup>rms may have to open-source their products.

## 5. Results

## 5.1. Unilateral open-sourcing

We analyze <sup>fi</sup>rst the effect of open-sourcing on prices when only one of the <sup>fi</sup>rms chooses to open-source its code. We <sup>fi</sup>nd that the open-sourcing <sup>fi</sup>rm will charge a lower price than its opponent only if there is customer loss. The optimal solution entails customer loss if the additional value that is due to open-sourcing $\left( \varDelta _ { 1 } \right)$ )is relatively small (i.e., if Eq. (1) holds). Recall that if this is the case, the opensourcing <sup>fi</sup>rm cannibalizes some of its sales of the commercial product by issuing the free open-source product. The existence of a free opensource product implies that the open-sourcing <sup>fi</sup>rm will need to lower its price so as to reduce the extent of customer loss. However, somewhat less intuitive is that when there is no loss, as a result of opensourcing, a <sup>fi</sup>rm will be able to increase the price it charges for its commercial product. The following proposition summarizes this result.

Proposition 1. With customer loss, the price charged by the firm that unilaterally opens its source code is lower than the price it would have charged had the firm not opened its source code. With no loss, the price charged by the open-sourcing firm for its commercial product is higher.

Proof. Suppose Firm 1 unilaterally releases an open-source version of its product. If there is no loss, in equilibrium the open-sourcing <sup>fi</sup>rm sells its commercial product at $P _ { 1 1 } ^ { I } = ( \Delta _ { 1 } + \Delta _ { 2 } ) / 2$ (see Eq. (5)). We show next that this equilibrium price is less than the price in the benchmark case (τ) if the following holds:

$$
\Delta_ {1} <   2 \tau - \Delta_ {2}.\tag{8}
$$

Note that condition (8) implies that there is a restriction on the <sup>fi</sup>rm's price, $P _ { 1 1 } ^ { I } { < } \tau$ . We can easily show that Eq. (8) is satis<sup>fi</sup>ed when the solution is interior, as in Section 4.2.1 above. To see this, observe that the right hand side of Eq. (8) is greater than the right hand side of Eq. (1) for all values of $\alpha \in ( 0 , 1 )$ . Thus, in an equilibrium with customer loss, open-sourcing forces Firm 1 to charge a lower price than in the benchmark case. With no loss, depending on the values of parameters, either Firm 2 is active on the market (in which case the price charged by Firm 1 is $\tau + \Delta _ { 1 } / 3 )$ , or Firm 2 is driven out of the market by the introduction of the open-source product (in which case the price charged by Firm 1 is $\Delta _ { 1 } - \tau )$ . Evidently, in both cases, Firm 1's price is greater than the benchmark price τ. □

![](/api/attachments/HR5XJFSH/fulltext/images/27a639fbc7719bfbffa267bf00b778729d83abb2048c4c2e19307f87db1e854c.jpg)  
Fig. 3. Market for software products in duopoly where both <sup>fi</sup>rms have open-sourced.

Since in any interior solution the open-sourcing <sup>fi</sup>rm lowers its price relative to the benchmark, in order for open-sourcing to be profitable the open-sourcing <sup>fi</sup>rm's market share has to increase to compensate the revenue loss on the customers it served in the benchmark equilibrium. This market share increase can compensate the revenue loss only for open-source products that bring about a relatively high incremental value gain $\varDelta _ { 1 } .$ . For small values of this incremental gain, open-sourcing is not a viable option. In the following proposition we derive the minimum $\varDelta _ { 1 }$ that guarantees that unilateral open-sourcing is pro<sup>fi</sup>table.

Proposition 2. A firm will increase its profit by unilaterally open-sourcing if

$$
\Delta_ {1} > \max \left\{0, \min \left\{\tau \sqrt {2 (1 - \alpha)} - \Delta_ {2}, \frac {(2 + \alpha) (1 - \alpha) \tau - 2 \Delta_ {2}}{1 + \alpha} \right\} \right\}.\tag{9}
$$

Proof. Suppose that Firm 1 unilaterally releases an open-source version of its product. We <sup>fi</sup>rst show when $\pi _ { 1 1 } > \pi _ { 1 0 }$ for the cases discussed in Sections 4.2.1, 4.2.2 and 4.2.3. We start with the two corner solutions. When Eq. (1) does not hold, Firm 2's market share can either be positive (as in Section 4.2.2 above), or zero (as in Section 4.2.3). When Firm 2 is active, $\pi _ { 1 1 } > \pi _ { 1 0 }$ is satis<sup>fi</sup>ed whenever $\begin{array} { r } { \varDelta _ { 1 } > 0 . } \end{array}$ . When Firm 2 is driven out of the market by the introduction of the open-source product, the <sup>fi</sup>rst <sup>fi</sup>rm's pro<sup>fi</sup>t increases relative to the benchmark pro<sup>fi</sup>t whenever $\Delta _ { 1 } > \left( 3 \tau / 2 \right)$ . This condition holds true whenever Firm 2 exits the market (i.e., whenever $\Delta _ { 1 } > 3 \tau )$ . Therefore, when $\Delta _ { 1 } > \left( ( 2 + \alpha ) ( 1 - \alpha ) \tau - 2 \Delta _ { 2 } \right) /$ (1+α), a <sup>fi</sup>rm will have an incentive to open its source code unilaterally.

Suppose now that condition (1) holds, i.e., that $\Delta _ { 1 } < ( ( 2 + \alpha ) ( 1 - \alpha )$ $\tau - 2 \Delta _ { 2 } ) / ( 1 + \alpha )$ . If so, it is straightforward to show that π $_ { 1 1 } > \pi _ { 1 0 }$ whenever $\Delta _ { 1 } > \tau \sqrt { 2 ( 1 - \alpha ) } - \Delta _ { 2 }$ (see Section 4.3.1 above). Combining the results yields the condition in Eq. (9). □

The next question we would like to answer concerns the effect of open-sourcing on the pro<sup>fi</sup>t of the <sup>fi</sup>rm that does not open its source code. We show next that open-sourcing unambiguously makes the opponent <sup>fi</sup>rm worse off.

Proposition 3. By unilaterally releasing an open-source version of its product, a firm makes its opponent worse off.

Proof. Suppose, as before, that Firm 1 unilaterally releases an opensource version of its products and that the solution is interior. We need to show that $\pi _ { 2 1 } < \pi _ { 2 0 } .$ . Suppose to the contrary that $\pi _ { 2 1 } \geq \pi _ { 2 0 } .$ . If so, we need $\begin{array} { r } { \big ( \sqrt { 2 ( 1 + \alpha ) } - \alpha \big ) \tau - \Delta _ { 2 } \leq 0 } \end{array}$ : Since, for $\alpha \in ( 0 , 1 ) , \sqrt { 2 ( 1 + \alpha ) } -$ $\alpha > 1$ , for $\pi _ { 2 1 } \geq \pi _ { 2 0 }$ to be true we require $\tau \leq \Delta _ { 2 } .$ Thus,

$$
\frac {(2 + \alpha) (1 - \alpha) \tau - 2 \Delta_ {2}}{1 + \alpha} \leq \tau (1 - \alpha) - \Delta_ {2} \leq 0,\tag{10}
$$

a contradiction, since Eq. (10) implies that the solution cannot be interior, as we assumed, since Eq. (1) is violated. Thus, Firm 2's pro<sup>fi</sup>t is lower in this situation. Evidently, Firm 2 is also worse off when it is driven out of the market. When there is no customer loss and Firm 2 has positive market share, Firm 2 competes head-to-head with a higher-value product, Firm 2's pro<sup>fi</sup>t is reduced. This can be easily seen by inspection (compare Eq. (3) with the benchmark pro<sup>fi</sup>t of τ/2). □

It is interesting to note that unilateral open-sourcing leads to higher surplus for all customers, since both <sup>fi</sup>rms lower their prices.

We have shown that when one of the duopolists releases an open source version of its product, its pro<sup>fi</sup>t may increase. Furthermore, the release of the open-source version entails a reduction of the competing <sup>fi</sup>rm's pro<sup>fi</sup>t. The question then naturally arises, what is the outcome of competition when both <sup>fi</sup>rms release an open-source version of their products? We provide an answer in the next section.

## 5.2. Both firms open-source

Suppose that the parameters of the model are chosen so that all four products in the market (two commercial products and two free opensource products) have positive market shares. As discussed above, this “interior” solution requires that $0 { < } x _ { 1 2 } ^ { I } { < } y _ { 1 2 } ^ { I } { < } x _ { 2 2 } ^ { I } { < } 1$ . Using the results presented in Section 4.3.1 above, it can be veri<sup>fi</sup>ed that $x _ { 1 2 } ^ { I } > 0 , y _ { 1 2 } ^ { I } < 1$ and $x _ { 2 2 } ^ { I } < 1$ for all feasible parameter values. To ensure that all four products have positive market shares, we also require that the parameters of the model satisfy the condition imposed by Eq. (7).

We provide next an analysis of the effect of open-sourcing on the prices charged by the two <sup>fi</sup>rms in equilibrium.

Proposition 4. The prices charged by the two firms in equilibrium are (weakly) lower when they both open their source code than without open-sourcing.

Proof. Suppose that the parameters of the model are chosen so that we are in the situation discussed in Section 4.3.1. The equilibrium prices in that case are $( \Delta _ { 1 } + \Delta _ { 2 } ) / 2 ;$ it can be shown that prices are greater than τ (the equilibrium price with no open-sourcing) if $\Delta _ { 1 } > 2 \tau - \Delta _ { 2 } .$ In turn, $2 \tau - \Delta _ { 2 } > ( 1 - \alpha ) \tau - \Delta _ { 2 }$ for all values of $\alpha \in ( 0 , 1 )$ , so as long as Eq. (7) is satis<sup>fi</sup>ed, the desired result is obtained. When Eq. (7) fails, as discussed in Section 4.3.2, the equilibrium price is equal to the equilibrium price with no open-sourcing. □

It is noteworthy that <sup>fi</sup>rms cannot increase their prices when they both open-source their products. We assumed that the commercial versions of the two products are more valuable to the customers when an open-source version is released. Despite the higher value that customers place on the products of the two <sup>fi</sup>rms, the additional value accrues to the customers alone, since in equilibrium the two <sup>fi</sup>rms do not pro<sup>fi</sup>t from the release of the open-source version of their products. Any potential pro<sup>fi</sup>t gains are lost due to competition. Firms not only compete with each other, but also compete with their open-source versions. The joint release of a free open-source version leads to lower prices for customers. However, since none of the <sup>fi</sup>rms is able to increase its market share, the <sup>fi</sup>rms' pro<sup>fi</sup>ts cannot increase as a result of open-sourcing. The best the <sup>fi</sup>rms can do is to compete head-to-head when there is no customer loss — in this situation the release of the open-source versions of their products has no effect on prices, market shares, and consequently, pro<sup>fi</sup>ts. We summarize this result in the following proposition.

Proposition 5. The two firms' profits cannot increase as a result of both firms releasing open-source versions of their products.

Proof. When all four products have positive market shares, the pro<sup>fi</sup>t for each <sup>fi</sup>rm is $\frac { ( \Delta _ { 1 } + \Delta _ { 2 } ) ^ { 2 } } { 4 \tau ( 1 - \alpha ) }$ (see the calculations in Section 4.3.1 above). Suppose that Eq. (7) holds. It is straightforward to check that these pro<sup>fi</sup>ts are smaller than τ/2 $\mathrm { i f } \Delta _ { 1 } > \sqrt { 2 ( 1 - \alpha ) } \tau - \Delta _ { 2 } : = \hat { \Delta } _ { 1 5 }$ . In $\tan , \Delta _ { 1 } >$ $\sqrt { 2 ( 1 - \alpha ) } \tau - \Delta _ { 2 }$ holds – for all values of α∈(0,1) – whenever Eq. (7) is satis<sup>fi</sup>ed, so pro<sup>fi</sup>ts are indeed reduced as a result of the two <sup>fi</sup>rms releasing open-source versions of their products.

When Eq. (7) fails there is no customer loss and the equilibrium price and pro<sup>fi</sup>ts are unchanged from the benchmark case (see Section 4.3.2 above). □

Our results so far indicate that under some circumstances it is pro<sup>fi</sup>table for a <sup>fi</sup>rm to unilaterally release an open-source version of its product. Our results also suggest when both <sup>fi</sup>rms release opensource versions, their pro<sup>fi</sup>ts are reduced. Our model is predicated on the assumption that the two <sup>fi</sup>rms are symmetric. While it is possible that the observed pattern of releasing open-source versions of commercial products is driven in part by asymmetries between <sup>fi</sup>rms related to costs, customer perception of the products, or the timing of the opensource releases, we wish to investigate next the outcome of competition when the two symmetric <sup>fi</sup>rms choose – simultaneously and independently – whether or not to release open-source versions of their products. We turn next to an analysis of the dynamic game induced by the <sup>fi</sup>rms' open-sourcing and pricing decisions.

Table 1 Payoff matrix structure.

<table><tr><td rowspan="3" colspan="2"></td><td colspan="2">Firm payoffs (Firm 1,Firm 2)</td></tr><tr><td colspan="2">Firm 2</td></tr><tr><td>Closed</td><td>Open</td></tr><tr><td rowspan="2">Firm 1</td><td>Closed</td><td> $\pi_{neither}$ ,  $\pi_{neither}$ </td><td> $\pi_{rival}$ ,  $\pi_{self}$ </td></tr><tr><td>Open</td><td> $\pi_{self}$ ,  $\pi_{rival}$ </td><td> $\pi_{both}$ ,  $\pi_{both}$ </td></tr></table>

## 5.3. Open-sourcing equilibrium

We <sup>fi</sup>rst describe the sequential-move game between our two <sup>fi</sup>rms. The game proceeds as follows: In the <sup>fi</sup>rst stage, the <sup>fi</sup>rms independently and simultaneously choose whether or not to release open-source versions. In the second stage, upon observing their opponent's opensourcing decision, the <sup>fi</sup>rms, independently and simultaneously, choose their prices to maximize pro<sup>fi</sup>t. Our equilibrium concept is subgame perfection (see [27]). A strategy pro<sup>fi</sup>le for each of the two players is a subgame perfect equilibrium if it is an equilibrium in any of the subgames of the original game. We <sup>fi</sup>nd the subgame perfect equilibria of our game using backward induction. We start with the second stage of the game. Depending on the <sup>fi</sup>rms' actions in the <sup>fi</sup>rst stage, there are four possible open-sourcing con<sup>fi</sup>gurations. Only three of which are distinct, due to symmetry. The optimal pricing decisions and payoffs in each of these second stage con<sup>fi</sup>gurations are discussed in Section 4. The three main cases of Section 4 provide the necessary payoff values for the <sup>fi</sup>rst stage problem. Thus, we can evaluate the <sup>fi</sup>rst-stage equilibrium outcomes using the payoffs we deduced in Section 4. We denote the pro<sup>fi</sup>t of each of the two <sup>fi</sup>rms when no <sup>fi</sup>rm releases an opensource version by $\pi _ { n e i t h e r } .$ The pro<sup>fi</sup>t of each of the two <sup>fi</sup>rms when both <sup>fi</sup>rms release open-source versions is denoted by $\pi _ { b o t h } .$ In the asymmetric case when one of the <sup>fi</sup>rms releases an open-source version, we denote by π the pro<sup>fi</sup>t of the <sup>fi</sup>rm that released the open-source version and by $\pi _ { \mathit { n i v a l } }$ the pro<sup>fi</sup>t of its opponent. Table 1 summarizes the payoffs that correspond to the <sup>fi</sup>rst-stage actions of the two <sup>fi</sup>rms.<sup>7</sup>

The equilibrium outcome can be found by inspecting the <sup>fi</sup>rms payoffs. The outcome of competition depends on the choice of the model's parameters since we have multiple solutions derived in Sections 4.2 and 4.3. Thus, a different payoff structure may exist for different regions of the parameter space. We <sup>fi</sup>nd that there are four different symmetric payoff matrices to be considered. We relegate the derivation of these payoff matrices to the accompanying online Technical Appendix. Table A-1 in the accompanying online Technical Appendix presents these payoffs.

Relevant in the computation of equilibria is the ranking of the <sup>fi</sup>rms' payoffs in different competitive regimes. By choosing different values of the parameters of our model, the ranking of the pro<sup>fi</sup>ts that correspond to the <sup>fi</sup>rst-stage actions of the two <sup>fi</sup>rms changes. Different equilibria were obtained that correspond to the different ranking of the <sup>fi</sup>rms' payoffs. We explore the parameter space in terms of the value of $\varDelta _ { 1 }$ , the incremental gain in the value of the commercial product brought about by the release of its open-source version, relative to the other parameters of the model. We <sup>fi</sup>nd that the pro<sup>fi</sup>ts that result from the two <sup>fi</sup>rms' <sup>fi</sup>rst-stage open-sourcing decisions can be ranked differently depending on how the value of $\varDelta _ { 1 }$ compares to the other parameters of the model.

Table 2 Order of payoffs.

<table><tr><td colspan="2">Order of payoffs for different regions</td></tr><tr><td>Region A</td><td> $\pi_{neither} \geq \pi_{rival} \geq \pi_{self} = \pi_{both}$ </td></tr><tr><td>Region B</td><td> $\pi_{neither} \geq \pi_{self} = \pi_{both} \geq \pi_{rival}$ </td></tr><tr><td>Region C</td><td> $\pi_{neither} = \pi_{both} \geq \pi_{self} \geq \pi_{rival}$ </td></tr><tr><td>Region D</td><td> $\pi_{self} \geq \pi_{neither} = \pi_{both} \geq \pi_{rival}$ </td></tr></table>

We start by assuming that Δ<sub>2</sub> and τ satisfy Δ<sub>2</sub> b τ. We turn to discuss next the ordering of the payoffs in the various parameter regions. The ordering of the payoffs is summarized in Table 2; a more detailed version of this table is provided as Table A-2 in the accompanying online Technical Appendix. We also relegate the de<sup>fi</sup>nition of the cutoffs that de<sup>fi</sup>ne each region to the accompanying online Technical Appendix.

Given these parameter regions and the ordering of the <sup>fi</sup>rms' payoffs in each region, we can <sup>fi</sup>nalize our equilibrium analysis. Fig. 4 summarizes the equilibria in each of the regions of the parameter space that correspond to Table 2. We note that multiple equilibria co-exist in some of the regions of the parameter space. In region A, since $\pi _ { n e i t h e r } 2$ $\pi _ { s e l f }$ and $\pi _ { r i \nu a l } { \geq } \pi _ { b o t h } ,$ the <sup>fi</sup>rms' dominant <sup>fi</sup>rst-stage action is not to release an open-source version. Regardless of its opponent's action, each <sup>fi</sup>rm is better off with a closed-source product. Therefore, in this case (the benchmark discussed in Section 4.1), in the unique equilibrium the two <sup>fi</sup>rms do not release open-source versions.

The equilibria that correspond to parameters that fall in region B also contain outcomes in which the two <sup>fi</sup>rms do not release opensource versions. No <sup>fi</sup>rm would consider a release of an open-source version if its opponent were not to release an open-source version (since in this region $\pi _ { n e i t h e r } { \ge } \pi _ { s e l f } )$ . However, not releasing an opensource version is no longer the best action irrespective of the opponent's open-sourcing decision. Given that the other <sup>fi</sup>rm has an open-source product, the best response would be to have an open-source product as well, $\pi _ { r i v a l } { \le } \pi _ { b o t h } .$ . Thus, opening the source code can also be part of the equilibrium. However, both <sup>fi</sup>rms are better off in the equilibrium that does not involve the opening of source code.

As above, in region C, there are two equilibria in which the <sup>fi</sup>rms either release or do not release open-source versions. Unlike the situation that arises when the model's parameters fall within region B, in region C the <sup>fi</sup>rms' payoffs in both equilibria are the same (so the equilibrium that involves releasing an open-source version is no longer payoff dominated).

Inspection of the payoffs in Table 2 indicates that a <sup>fi</sup>rm could profitably open up their code when its opponent does not whenever the model's parameters fall within region D. In this region $\pi _ { s e l f } { \geq } \pi _ { n e i t h e r }$ and $\pi _ { b o t h } { \geq } \pi _ { r i v a l } .$ Thus, irrespective of the action of its opponent, a <sup>fi</sup>rm's best <sup>fi</sup>rst-stage action is to release its source code. Thus, the unique equilibrium has both <sup>fi</sup>rms releasing of an open-source version.

It can be easily seen by inspecting the values of the cutoffs that as the value of $\varDelta _ { 2 }$ increases relative to τ, the two regions A and B decrease in size. When $\varDelta _ { 2 } \geq \tau$ the regions I and II vanish. In that case, both <sup>fi</sup>rms open their source code in the unique equilibrium for all values of $\varDelta _ { 1 }$ .

## 6. Conclusions

In this paper we analyzed the conditions under which <sup>fi</sup>rms <sup>fi</sup>nd it optimal to release open-source versions of their products. Conventional wisdom suggests that open-sourcing increases the size of the market. As some would argue, as a result of open-sourcing software products gain more exposure, which in turn allows <sup>fi</sup>rms to reap higher pro<sup>fi</sup>ts through either increased sales of complementary products (e.g., hardware) or through reduced future costs of maintaining and managing the software code. This explanation is incomplete and somewhat fallacious, as clearly greater pro<sup>fi</sup>t increases could be achieved through limited releases of the source code or through free distribution of the closed-source product.

![](/api/attachments/HR5XJFSH/fulltext/images/48feaf76d4b9992a913fc8aed4868fc1dac74da00cfeddb774f720d74b75ab35.jpg)  
Fig. 4. The equilibria with respect to $\varDelta _ { 1 }$ when Δ ≤τ.

Recent research has considered the incentives for open-sourcing in relation to a complementary service market. While in today's business environment the software and service markets are hard to disentangle, we gain some insight by focusing only on the software product market. The main driving force of our model is the impact of opensourcing on the customers' values. Open-source versions tend to provide less functionality than their commercial versions. However, customers could <sup>fi</sup>nd the open-source product more valuable than its closed-source counterpart because of the better opportunities for customization. In our model, the “crimped” product competes headto-head with the products of the competing <sup>fi</sup>rm. As a result, the release of an open-source version better insulates a <sup>fi</sup>rm from the pricing strategy of its opponent. All things equal, this implies that the <sup>fi</sup>rm that releases the open-source version has a competitive edge over its opponent. Clearly, the <sup>fi</sup>rm that unilaterally releases the open-source version increases its pro<sup>fi</sup>t, provided that it can maintain its customer base. If there is customer loss (i.e., when the release of the open-source version causes some of the releasing <sup>fi</sup>rm's customers to migrate to the free, open-source version) the outcome is in<sup>fl</sup>uenced by the trade-off between higher prices and a smaller customer base. We have shown how these trade-offs affect the <sup>fi</sup>rms decision to release open-source products. We identi<sup>fi</sup>ed parameter regions in which the equilibrium has the <sup>fi</sup>rms releasing open-source products. An important managerial implication is that open-sourcing is likely to occur when the difference in customer valuation between the proprietary and the open-source products is high relative to the <sup>fi</sup>t cost. It is useful to note that in most examples in which opensourcing arises in a competitive environment, there is a sizable gap between the customers' valuations of the open- and closed-source products. Clearly, as a result, not all <sup>fi</sup>rms in today's software business environment have included open-sourcing in their strategic repertoire. Another implication of our analysis shows that in order to stay competitive, software <sup>fi</sup>rms should open-source their products whenever a competitor chose to do so.

The market for software products and services is under continuous evolution. Our model suggests that open- and closed-source software products are bound to co-exist. However, co-existence of the two types of products is more likely when the open-source product lacks signi<sup>fi</sup>cant features, or when the closed-source version becomes more valuable as a result of better code maintenance (including eliminating some bugs in the code). Also important for the open-sourcing decision of <sup>fi</sup>rms is the ease with which customers could modify the open-source product. Easier modi<sup>fi</sup>cation of the open-source product implies that, all other things equal, an equilibrium is more likely to arise in which competitive <sup>fi</sup>rms release open-source versions of their software products.

## Disclaimer

The opinions expressed in this article are those of the author and do not necessarily represent the views of the Federal Communications Commission, its commissioners, or the United States Government.

## Appendix A. Supplementary data

Supplementary data to this article can be found online at http:// dx.doi.org/10.1016/j.dss.2012.05.001.

## References

[1] T. August, H. Shin, T. Tunca, Open source software: incentives and the market for services, Workshop on Infomation System Economics, (WISE), 2007. http://www. wise2007.org/program.html, Montreal, Canada.

[2] H. Bhargava, V. Choudhary, Information goods and vertical differentiation, Journal of Management Information Systems 18 (2) (2001) 89–106.

[3] H. Bhargava, V. Choudhary, Research note — when is versioning optimal for information goods? Management Science 54 (5) (2008) 1029–1035.

[4] J. Bitzer, Wolfram Schrettl, Philip J.H. Schröder, Intrinsic motivation in open source software development, Journal of Comparative Economics 35 (2007) 160–169.

[5] A. Bonaccorsi, S. Giannangeli, C. Rossi, Entry strategies under competing standards: hybrid business models in the open source software industry, Management Scienc 52 (7) (2006) 1085–1098.

[6] R. Casadesus-Masanell, P. Ghemawat, Dynamic mixed duopoly: a model motivated by linux vs. windows, Management Science 52 (7) (2006) 1072–1084.

[7] R.J. Deneckere, R.P. McAfee, Damaged goods, Journal of Economics and Management Strategy 5 (2) (1996) 149–174.

[8] R. Dewan, B. Jing, A. Seidmann, Product customization and price competition on the internet, Management Science 49 (8) (2003) 1055–1070.

[9] N. Economides, E. Katsamakas, Two-sided competition of proprietary vs. open source technology platforms and the implications for the software industry, Man agement Science 52 (7) (2006) 1057–1071.

[10] D. Farber, Commercial open source, a misnomer?downloaded on August 13 2007, http://blogs.zdnet.com/BTL/?p=1787 2005.

[11] A. Fosfuri, M.S. Giarratana, A. Luzzi, Firm assests and investments in open source software products, DRUID Working Paper Series 05–10, 2005.

[12] Anindya Ghose, Arun Sundararajan, Software versioning and quality degradation? An exploratory study of the evidence, Working Paper, CeDER-05-20, Center for Digital Economy Research, New York University, 2005.

[13] Kholekile L. Gwebu, Jing Wang, Adoption of open source software: the role of social identi<sup>fi</sup>cation, Decision Support Systems 51 (1) (2011) 220–229.

[14] Hawkins, E. Richard, The economics of open source software for a competitive firm – why give it away for free? NETNOMICS: Economic Research and Electronic Networking (2), 2004 URL http://slytherin.ds.psu.edu/hawk/research/opensource/opensource.pdf.

[15] Bing Jing, Market segmentation for information goods with network externalities, Information Systems Working Papers Series, 2003, Available at SSRN: http://ssrn. com/abstract=1281325.

[16] Bing Jing, Network externalities and market segmentation in a monopoly, Economics Letters 95 (1) (2007) 7–13.

[17] S. Koch, G. Schneider, Effort, cooperation and coordination in an open source software project: Gnome, Information Systems Journal 12 (1) (2002) 27–42.

[18] S. Krishnamurthy, An analysis of open-source business models, in: Joseph Feller, Brian Fitzgerald, Scott A. Hissam, Karim R. Lakhani (Eds.), Perspectives on Free and Open Source Software, MIT Press, Cambridge, MA, 2005, pp. 279–296.

[19] J. Lerner, J. Tirole, Some simple economics of open source, The Journal of Industrial Economics (L(2)) (2002) 197–234.

[20] A. MacCormack, J. Rusnak, C.Y. Baldwin, Exploring the structure of complex software designs: an empirical study of open source and proprietary code, Management Science 52 (7) (2006) 1015–1030.

[21] M. Mustonen, When does a <sup>fi</sup>rm support substitute open source programming? Journal of Economic and Management Strategy 14 (1) (2005) 121–139.

[22] J. Prial, Why ibm is open sourcing cloudscape as derby downloaded on August 13 2007, URLhttp://www-128.ibm.com/developerworks/db2/library/ techarticle/dm-0410prial2004

[23] Srinivasan Raghunathan, Software editions: an application of segmentation theory to the packaged software market, Journal of Management Information Systems 17 (1) (2000) 87–114.

[24] Eric S. Raymond, The Cathedral and the Bazaar: Musings on Linux and Open Source by an Accidental Revolutionary, O'Reilly and Associates, Sebastopol, California, 1999.

[25] C. Rossi, A. Bonaccorsi, Why pro<sup>fi</sup>t-oriented companies enter the OS <sup>fi</sup>eld? Intrinsic and extrinsic incentives, Fifth Workshop on Open Source Software Engineering, 2005 St. Louis MO USA

[26] A. Schiff, The economics of open source software: a survey of the early literature, Review of Network Economics 1 (1) (2002) 66–74.

[27] R. Selten, A reexamination of the perfectness concept for equilibrium points in extensive games, International Journal of Game Theory (1975) 4

[28] R. Sen, A strategic analysis of competition between open source and proprietary software, Journal of Management Information Systems 24 (1) (2007) 233–257.

[29] R. Sen, S.S. Singh, S. Borle, Open source software success: measures and analysis, Decision Support Systems 52 (2) (2012) 364–372.

[30] Bertrand Serlet, Apple: Open-source pedigree will protect tiger downloaded on August 13 2007, http://news.com.com/2100-1016\_3-5341689.html2004

[31] A. Sundararajan, Nonlinear pricing of information goods, Management Science 50 (12) (2004) 1660–1673.

[32] G. von Krogh, E. von Hippel, The promise of research on open source software, Management Science 52 (7) (2006) 975–983.

[33] T.A. Weber, Delayed multiattribute product differentiation, Decision Support Systems 44 (2008) 447–468.

[34] T. Wichmann, Firms' open source activities: motivations and policy implications, Final report, <sup>fl</sup>oss:survey and study, International Institute of Infonomics, University of Maastricht and Berlecon Research, GmbH, 2002, URL http://www.infonomics.nl/ FLOSS/report.

![](/api/attachments/HR5XJFSH/fulltext/images/5d54f69128937b2513eac84895fe6f0f9d322c17689187bdaabbf066eeb4d6f7.jpg)

Dr. Jai Asundi is a Principal Research Scientist at the Center for Study of Science Technology and Policy(CSTEP) in Bengaluru, India and a Visiting Assistant Professor in Information Systems at the University of Texas at Dallas. His interests lie in the areas of software engineering and project management, economics of open source software and information technology for development. He is currently working on the development of decisions support systems for a variety of public policy problems. His prior work includes the development of methods for software architecture design, characterization of software outsourcing between the US and India and economic analysis of commercial open-source software. He is a member of the

IEEE. Dr. Asundi has been associated with the Software Engineering Institute in Pittsburgh and holds a B.Tech. degree from IIT Bombay and M.S. and Ph.D. degrees from Carnegie Mellon University, Pittsburgh.

![](/api/attachments/HR5XJFSH/fulltext/images/7d4b8917b77432bf0664d88f795fbfe2995cbd722dac41db528459f54b4c0dc8.jpg)

Octavian Carare is an Economist at Federal Communications Commission and a Lecturer at Johns Hopkins University. He has previously taught at the University of Texas in Dallas and at the University of Maryland — College Park. Octavian holds a PhD in economics from Rutgers University. His research interests include theoretical and empirical issues related to open source, auctions, and the economics of information. His publications include articles in Management Science, Economics Letters, and Experimental Economics.

![](/api/attachments/HR5XJFSH/fulltext/images/b982cce422d7944ac9328583301e84d1d7908c3081c7d4e7abe3467b8769d686.jpg)

Kutsal Dogan is an Associate Professor and the Associate Dean in the Faculty of Economics and Administrative Sciences at Ozyegin University. Dr. Dogan holds a PhD degree from the University of Florida, an MBA degree from Virginia Tech and a B.S. degree in management engineering from Istanbul Technical University. He previously taught at the University of Florida and served on the faculty of the school of management at the University of Texas at Dallas as an assistant professor between 2002 and 2009, where he received the college's Outstanding Undergraduate Teacher of the Year award in 2007.

Dr. Dogan's research interests lie broadly in management information systems, economics, and marketing. In man-

agement information systems, he is interested in economics of information products and services such as software. His works in marketing promotions mainly deal with second-degree price discrimination and its effects on consumers and competition. He is also interested in behavioral issues in marketing and economics. His articles appeared in Information Systems Research, Decision Sciences, International Journal of Industrial Organization, Decision Support Systems, Quantitative Marketing and Economics, and Information Technology and Management journals.

He serves on the editorial boards of Decision Sciences Journal and International Journal of E-Business Research and on the program committees of prestigious conferences and workshops in Management Information Systems.
