---
otero_id: 16435
otero_key: "S2U4KS23"
title: "A Theory-Driven Design Framework for Social Recommender Systems"
authors: "Ofer Arazy; Nanda Kumar; Bracha Shapira"
year: "2010"
journal: "Journal of the Association for Information Systems"
doi: "10.17705/1jais.00237"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Theory-Driven Design Framework for Social Recommender Systems

Article  in  Journal of the Association for Information Systems · October 2010 DOI: 10.17705/1iais,00237· Source: DBI

CITATION 115

3 authors, including:

![](/api/attachments/S2U4KS23/fulltext/images/a3d77d114cf62c12731ded317fc0046714730db1577c35b491c2a4bdaeddf780.jpg)

Ofer Arazy University of Haifa 76 PUBLICATIONS   2,176 CITATIONS

SEE PROFILE

READS 1,816

![](/api/attachments/S2U4KS23/fulltext/images/fc0a057107c30628214b391b4abb3b81cece6746c3a8d0deac36c868e16f625d.jpg)

Bracha Shapira Ben-Gurion University of the Nege 202 PUBLICATIONS   8,732 CITATION

SEE PROFIL

Some of the authors of this publication are also working on these related projects:

Project

Masters Thesis View project

Collaborative Knowledge Production View project

# Journal of the Association for Information Systems JAIS

Research Article

# A Theory-Driven Design Framework for Social Recommender Systems

Ofer Arazy University of Alberta ofer.arazy@ualberta.ca

Nanda Kumar City University of New York Nanda.Kumar@baruch.cuny.edu

Bracha Shapira Ben-Gurion University of the Negev bshapira@bgumail.bgu.ac.il

## Abstract

Social recommender systems utilize data regarding users’ social relationships in filtering relevant information to users. To date, results show that incorporating social relationship data – beyond consumption profile similarity – is beneficial only in a very limited set of cases. The main conjecture of this study is that the inconclusive results are, at least to some extent, due to an under-specification of the nature of the social relations. To date, there exist no clear guidelines for using behavioral theory to guide systems design. Our primary objective is to propose a methodology for theory-driven design. We enhance Walls et al.’s (1992) IS Design Theory by introducing the notion of “applied behavioral theory,” as a means of better linking theory and system design. Our second objective is to apply our theory-driven design methodology to social recommender systems, with the aim of improving prediction accuracy. A behavioral study found that some social relationships (e.g., competence, benevolence) are most likely to affect a recipient’s advice-taking decision. We designed, developed, and tested a recommender system based on these principles, and found that the same types of relationships yield the best recommendation accuracy. This striking correspondence highlights the importance of behavioral theory in guiding system design. We discuss implications for design science and for research on recommender systems.

Keywords: Social Recommender Systems, Collaborative Filtering, Theory-Driven Design, Applied Theoretical Model, Advice Taking. Volume 11, Issue 9, pp. 455-490, September 2010

# A Theory-Driven Design Framework for Social Recommender Systems

## 1. Introduction

The explosive growth of available information online, fueled by the rapid adoption of the Internet, is making access to relevant information analogous to finding a needle in a haystack. This information overload problem hampers consumers’ ability to locate relevant information and select products online. Recommender systems play a significant role in reducing information overload by providing users with relevant information and are a key component of successful online stores such as Amazon, ePinion, and NetFlix. As a result, they have become an important topic of academic research (Adomavicius and Tuzhilin, 2005).

Two approaches to recommender systems design exist: The first is based on the contents of documents and user profiles, while the other is based on relationships among users (Shardanand and Maes, 1995; Resnick and Varian, 1997; Herlocker et al., 2004; Adomavicius and Tuzhilin, 2005). Our focus here is on the latter type of recommender systems, referred to as social recommender systems (SRS). Examples of social recommender systems include the recommendation engines of Amazon and ePinions. A typical social recommender process consists of three sequential steps: (1) identification of relevant sources for a user, (2) analysis of the sources’ consumption profiles (indicating which items they like), and (3) generation of recommendations for the user, based on these profiles (Konstan, 2004).

SRS can be classified based on the type of social data they employ in determining relevant sources (Arazy et al., 2009). The most common social recommender approach, referred to as Collaborative Filtering (from here onward, CF), suggests that users are associated with others based on the degree to which they share their preferences (i.e., the similarity of their preference profiles (Shardanand and Maes, 1995)). This approach is commonly used in online recommender systems such as Amazon.com (Linden et al., 2003). Recently, an alternative approach has emerged, where additional indicators of social relationships are used to associate a recipient with relevant sources; for example, friendship ties in online social networks (Goldberg et al., 1992; Kautz et al., 1997; Massa and Avesani, 2004; Golbeck and Hendler, 2006; Guy et al., 2009; Victor et al., 2010). This approach has recently been explored by popular recommendation sites such as ePinions, Amazon, and NetFlix. Similarly, users’ communications history, which may be extracted from e-mail and instant messaging applications, could also be used as an additional indicator of social relationships (Zheng et al., 2007). Commonly, both profile similarity and social relationship data are used in conjunction to associate a recipient with sources, such that the “strong” social ties are layered on top of the existing “weak ties” network (i.e., profile similarity). Figure 1 illustrates the architecture of a SRS that considers these various relationship indicators.

![](/api/attachments/S2U4KS23/fulltext/images/e36591ab63a65ce6286d8b56db5b25d75486a0dd64720ce3b09038e2bf66039f.jpg)  
Figure 1. An illustration of social recommender system architecture – predicting recipient A’s liking of item X

Research on social recommender systems that employ relationship information is in its early phases, and to date, results are inconclusive, showing modest accuracy enhancements only in a very limited set of cases. The main conjecture of this study is that the inconclusive results are due – at least to some extent – to an under-specification of the nature of the social relations, and SRS are often designed in an ad-hoc manner, where the choice of the type of social data that is employed is not informed by behavioral theory.

This study has two primary objectives. The first objective is associated with our research methodology and involves substantial enhancements to existing design science frameworks, creating a tight linkage between behavioral theory and system design. Specifically, we argue that existing approaches to “scientific” design (i.e., design science or design research (Hevner et al., 2004)) overlook the role of behavioral theory in design. Walls et al.’s approach (1992, 2004) does acknowledge the importance of “kernel theories,” defined as general explanatory theories from the natural or social sciences. However, such theory-driven design is very difficult, mainly due to a mismatch in terms of scope and granularity between the theoretical frameworks and the design problem. The Walls et al. framework does not provide guidelines on how general explanatory (i.e., kernel) theories could be linked to prescriptive statements of design, and studies of design research regularly overlook the role of behavioral theory. We argue that the gap between theory and design could be bridged through the development of an intermediate component between kernel theories and system design: an applied theoretical model. The applied model is articulated as a behavioral framework, but corresponds directly to the design problem, such that the choice of constructs and their granularity are informed by the design problem. Our second objective is associated with the specific problem at hand – the design of social recommender systems – and is aimed at developing a novel design framework that would improve the performance of SRS.

The remainder of this paper is organized as follows. Section 2 analyzes the design problem – identifying relevant sources in social recommender systems – in more detail. Section 3 elaborates on our proposed approach for theory-driven design: It reviews extant design science frameworks, discusses the role of behavioral theory in these frameworks, and argues for an extension that would help ground the design in theories of human behavior. The sections that follow adopt our proposed theory-driven design and describe the paths from kernel theories all the way to the design of a social recommender system. Section 4 discusses relevant kernel theories; Section 5 reviews the development and evaluation of an applied theoretical model of advice-taking that is intended to guide SRS design. Section 6 lays out our proposed SRS design principles (i.e., meta-requirements, metadesign, and testable design hypotheses, using the Walls et al. terminology); Section 7 describes a recommender system prototype that was built based on these design principles, and reports on system evaluation results; Section 8 discusses the findings from both the behavioral study and system testing, as well as the implications for research on design science; and Section 9 concludes the paper with some future research directions.

## 2. The Design Problem: Identifying Relevant Sources in Social Recommender Systems

Traditional social recommender systems, i.e., collaborative filtering systems, associate a recipient with sources based on the degree to which their consumption profiles are similar (Shardanand and Maes, 1995). In collaborative filtering, a rating of target item i for target user a can be predicted using a combination of the ratings of the neighbors of a (similar users) that are already familiar with item i (Resnick et al., 1994).<sup>2</sup>

$$
p (a, i) = \overline {{r}} _ {a} + \frac {\sum_ {u \in R ^ {+}} w _ {a , u} * (r _ {u , i} - \overline {{r}} _ {u})}{\sum_ {u \in R ^ {+}} w _ {a , u}}
$$

The unknown rating $p ( a , i )$ for item i and recipient a is predicted based on the mean

$r _ { a }$ of ratings by user a for other items, as well as on the ratings $r _ { u , i }$ by other users u

for i. The formula also takes into account the degree of similarity $w _ { a , u }$ between users a and $u ,$ often calculated as Pearson’s Correlation Coefficient (Herlocker et al., 2004). In practice, most often, only users with a positive correlation $w _ { a , u }$ who have rated i are considered. We denote this set by $R ^ { + }$

Notwithstanding the importance of profile similarity as an indicator of a source’s relevancy, evidence suggests that people tend to rely more on recommendations from their friends than on online recommender systems that generate recommendations based on anonymous people similar to them (Sinha and Swearingen, 2001). This observation, combined with the growing popularity of open social networks and the trend to integrate e-commerce applications with recommender systems, has generated a rising interest in social-network-enhanced recommender systems (Massa and Avesani, 2004; Avesani et al., 2005; Golbeck 2006; Golbeck and Hendler, 2006; Victor et al. 2008; Guy et al., 2009; Victor et al., 2010). A typical example is the e-commerce site ePinions.com, which developed a trust network by asking its users to indicate which members they trust. This type of SRS uses the knowledge that originates from social networks to generate more personalized recommendations, such that users receive recommendations not only from sources with similar profiles, but also from sources belonging to their social network.

$$
p (a, i) = \overline {{r}} _ {a} + \frac {\sum_ {u \in R ^ {+}} f (w _ {a , u} , t _ {a , u}) * (r _ {u , i} - \overline {{r}} _ {u})}{\sum_ {u \in R ^ {+}} w _ {a , u}}
$$

Recipient-source similarity is now based on a function of profile similarity $( w _ { a , u } )$ and social-network based similarity $( \mathrm { \Delta } t _ { a , u } )$ . Commonly, this function is a weighted sum (after similarity scores are normalized (Arazy et al., 2007)). Since the number of social network sources is often limited, it is possible to “propagate” social relationships to indirect ties (i.e., friend-of-a-friend (Guha et al. 2004)). However, findings suggest that in practice trust propagation beyond one degree does not enhance

effectiveness (Massa and Avesani, 2004).

To date, experiments with SRS that employ additional sources of social relationship data have yielded mixed results. For example, Massa and Avesani (2004) conducted an empirical evaluation on an ePinions.com dataset, comparing the social approach (i.e., a combination of trust data and CF) to standard CF. The result shows that the overall social relationship yields no improvements, except in he special cases where the recipient’s profile is highly sparse (i.e., cold start). Similarly, Golbeck and Hendler (2006) report that a social-network-based recommendation is overall not more accurate than traditional CF, except when users’ ratings of a specific item are highly varied (i.e., controversial items). On the other hand, others have shown that in some cases social-network data could be used to enhance recommendation accuracy (Bonhard and Sasse, 2006; Groh and Ehmig, 2007; Lerman, 2007; Guy et al., 2009). A recent survey of the field (Victor et al., 2010) demonstrates that, in general, this approach for utilizing additional sources of relationship data is no more effective than traditional CF, although in some specific cases – e.g., cold start or controversial items – some improvements are possible.

The main conjecture of this study is that the inconclusive results to date are due – at least in part – to an under-specification of the nature of the social relations in the systems design. That is, in the formula above, it is not clear what type of social relationship the term $t _ { a , u }$ represents. For example,

while the ePinions social relationship that was employed in the works of Massa and Avesani (2004, 2005) represents “trust,” others (e.g., Zheng et al., 2007; Arazy et al., 2009) propose that the duration and frequency of recipient-source communications could also be used to enhance recommendation accuracy. The discussion regarding the social relationships used in SRS has been lacking theoretica grounding, and to date there has been no empirical evaluation of how different relationship types affect recommendation accuracy. The aim of this study is, therefore, to fill this gap by grounding the design choice regarding the relationship data that is used to associate a recipient with sources on sound behavioral theory, and to empirically investigate whether such theory-driven design will yield performance enhancements.

## 3. Grounding System Design in Behavioral Theory

In this section we present our arguments for theory-driven information systems (IS) design. We start by reviewing the role of behavioral theory in extant design science literature in Section 3.1, and present our view of how current conceptualizations could be extended to more tightly link cognitive and social theories to systems design. There are major challenges in linking kernel theories and design. We argue that extending the Walls et al. (1992, 2004) conceptualization through the introduction of an intermediate component – termed “applied theoretical model” – could alleviate many of these problems. In Section 3.2, we proceed to discuss how we addressed the linkage between theory and design in our study, when working on the design problem of associating a recipient with relevant sources in SRS.

## 3.1 The Role of Behavioral Theory in IS Design

Grounding systems design in behavioral theory not only increases the designer’s understanding of the problem domain, but also helps formulate high-level design principles<sup>3</sup> that are independent of technological constraints and specific implementation details. This is not to say that all design research should always be grounded in cognitive or social theory; rather, we contend that for those design problems where the link to theory is apparent, grounding the design in the theoretical foundations could lead to more effective designs. Despite these potential benefits, behavioral theory has had a limited role in information systems design research, and the explication of the theoretical basis for making the design effective is often absent (Venable, 2006; Kuechler et al., 2007).

A survey of IS papers that discuss the design science methodology reveals two approaches regarding the role of behavioral theory in systems design. The main IS design science camp does not explicitly discuss the role of behavioral theory in guiding design (Nunamaker et al., 1991; March and Smith, 1995; Gregg et al., 2001; Hevner et al., 2004; Gregor and Jones, 2007; March and Storey, 2008). Instead, this approach is interested in generalizing design principles and articulating them as theory, as well as in testing and evaluation methods. The second camp recognizes that design research involves designs that are clearly driven by supporting (kernel) theories from related disciplines (Pries-Heje and Baskerville, 2008). Goldkuhl (2004) argues for the importance of grounding design. Among the various ways of grounding design, one key approach relates prescriptive statements of design to general explanatory theories. This theory-driven design approach is best explicated by Walls et al. (1992, 2004), who introduced the IS Design Theory (ISDT; see Figure 2 below) as a prescriptive statement of how to develop design paths that rigorously derive their rationale from more fundamenta research in the natural or social sciences (referred to as kernel theories).

![](/api/attachments/S2U4KS23/fulltext/images/3dc50409a171faef2707ae070956da72bbc52f5d67e27d74bd4b81d6d7b3963a.jpg)

Thus, “the design embodies principles of the theory” (Walls et al., 1992; p. 38). Such designs are expected to produce more effective information systems, since “the laws of the natural and socia world govern the components that comprise an information system“ (Walls et al., 2004; p. 45). Walls et al. (1992) provide the example of how relational algebra serves as a kernel theory for the design of relational databases, and apply their ISDT approach to the design of vigilant information systems, building kernel theories of managerial information scanning and open loop control.<sup>5</sup> Despite Walls et al.’s formulation of theory-driven design, their framework provides very little direction on how the linkage between kernel theory and design could be achieved. It assumes that kernel theories are ready to be used as-is in guiding the design process, while in reality this is rarely the case, primarily because the scope and granularity of the generic kernel theory are often inadequate for guiding design (please see detailed discussion below). As a consequence, it is rare to encounter IS designs that are based on well-defined kernel theories (Iivari, 2002). Typically, when system design is informed by theory, the deduction from kernel theories to design is not a process of logical derivation; instead, theories are only used as sources for inspiration (Goldkuhl, 2004), and the transformation from theory to design is highly interpretative. As Gregor and Jones (2007) note, in the IS area “some design knowledge is originally presented with an underlying justification from the behavioral sciences, but this underlying justification is later either forgotten or neglected” (p. 328).

While kernel theory has thus far played a minor role in IS design research, it is well accepted in the engineering disciplines. For instance, the design of an airplane wing is based on technological rules that are grounded on the laws of aerodynamics and mechanics. In the context of IS design, the field of human-computer interaction (HCI) illustrates how knowledge of human cognitive processes can direct principles of human-computer interaction design (c.f. Shneiderman, 1998). This tradition of theory-driven design in HCI dates back to the 1980s (e.g. Malone, 1985; Carroll and Kellogg, 1989). Among the more recent examples of this theory-driven design in this field, the works of Robert Kraut, a social psychologist and a design researcher, stand out (e.g., Galegher et al., 1990; Kraut, 2003; Ling et al., 2005; Dabbish and Kraut, 2008). Kraut and colleagues have been involved in various stages of theory-driven design in the field of HCI, from the development of behavioral theory to the design and testing of systems based on these theories. They argue that employing cognitive and social science theories as sources of principles for design innovation is a generally useful strategy (Ling et al., 2005).

Despite the promise of the theory-driven design, there are some major challenges in bridging the gap between kernel behavioral theories and systems design. Based on our review of prior literature in this area, we synthesize four primary concerns. First, it is not easy to find relevant kernel theories for a specific design problem at hand. Walls et al. (2004), in their introspective article, point to this problem as one of the impediments to the adoption of their ISDT framework. The disconnect between behavioral and design researchers, who have different – and often incompatible – perspectives regarding research, exacerbates this problem. Second, the scope of the existing kernel theories is often too narrow, such that no single theory accounts for the set of constructs relevant to the design problem (Newell and Card, 1985; Carroll and Kellogg, 1989; Kraut, 2003; Ling et al., 2005). Third, the theoretical model guiding the design should employ a level of abstraction that is suited to the design problem at hand (Hooker, 2004), but often the granularity of the constructs, as they are formulated in the kernel theories, does not match the requirements of the design problem (Newell and Card, 1985; Ling et al., 2005). Last, kernel theories are not adequate for guiding design, as they commonly specify only the direction of effects, whereas making design choices requires that we also consider the effects’ magnitude (Newell and Card, 1985; Kraut, 2003; Ling et al., 2005).

Card and Newell (Card et al., 1983; Newell and Card, 1985) present an approach aimed at addressing these challenges. They provide a tight and direct linkage between kernel theories (in their specific case – cognitive theories) and design. One of the main novelties of the Card and Newell method is the development of applied psychological theoretical models (rather than borrowing existing kernel theories) for the purpose of designing interfaces. They refer to this type of newly developed applied theory as “engineering-style theory” (Newell and Card, 1985, p. 215). Their applied theoretical model, “Model Human Processor,” “is an approximate cognitive model of the user to be employed by the designer in thinking about the human interacting with the computer at the interface” (Newell and Card, 1985; p. 215). The Card and Newell vision intended the applied theoretical model to be a “calculational tool, rather than just a summary of the high-level structure of the cognitive system” (Newell and Card, 1985; p. 215), such that it could be easily translated into design. The main criticism of the Card and Newell approach is that it could only be applied to a few low-level design problems, e.g., keystroke-level methods for ideal expert performance or rote learning of scaled-down text editors. As Carroll and Kellogg (1989) put it: “It may be simplistic to imagine deductive relations from science to design, but it would be bizarre if there were no relation at all” (p. 13).

A main conjecture of our paper is that the Card and Newell approach still holds much value, and that it could potentially be applied to various classes of IS design problems. We believe that incorporating ideas from Card and Newell into extant frameworks of IS design science could prove valuable. Specifically, we contend that incorporating the notion of an applied theoretical model into the Walls et al. design science conceptualization could help bridge the gap between kernel theories and design. We propose, thus, an extension of the Walls et al. design science conceptualization that adds a new component – as illustrated in Figure 3 – to better link kernel theories and system meta-requirements. We refer to this new component as “applied behavioral theory”; it is an explanatory theory that borrows from the generic kernel theories and is formulated as a behavioral framework, yet it is informed and constrained by design requirements. This type of theory-driven design could be applied to an entire information system, or to a specific component of the system (Walls et al., 1992).

![](/api/attachments/S2U4KS23/fulltext/images/b892b30b292765811a49f9ade46ae860c0ccd6b9e8c9b8e90a10e945ce56a345.jpg)  
Figure 3. An illustration of our proposed IS design theory framework (1992)<sup>6</sup>

Our new conceptualization extends the Walls et al. (1992) ISDT not only by introducing the additional component, but also by suggesting additional paths of influence between the various components. Notwithstanding Walls et al.’s (192) argument for the paths from kernel theories to meta-requirements (path A in Figure 3), and then to meta-design (path B) and design propositions (path C), we make the case for additional possible paths of influence. Specifically, we argue that the system high-level specifications (i.e., meta-requirements and meta-design) may influence theory in two ways (path D in Figure 3). First, they may influence the choice of kernel theories that are employed (path D1). Second, they may apply some constraints on the development of the applied theoretical model (path D2). Other deviations from the ISDT (Wall et al., 2992) are the paths connecting to the applied behavioral model: the link between kernel and applied theory (path E) and the link between the applied model and design propositions (path F).

## 3.2 Linking Behavioral Theory to Systems Design

In this section, using our context of social recommender systems as an example, we outline the general heuristics one needs to apply when incorporating social or psychological theory into system design. The paths between kernel theories, meta-requirements, meta-design, and testable design product propositions have been described in detail in the works of Walls et al. (1992, 2004) and their followers (e.g., Markus et al., 2002). Here, we focus on the newly introduced paths between the design specification, kernel theory, applied behavioral theory, and design propositions. In the following section we describe a series of steps, each intended to address one of the four challenges for theorydriven design (see discussion in Section 3.1 above). Although we try to generalize our approach so that it can be applied to other contexts, we realize that other methods for theory-driven design are possible, and thus, our proposed approach should be seen as only one feasible heuristic.

The first move in the heuristics is to determine whether the application of psychological or social theories is warranted in a particular design problem. For example, design science that seeks to improve the performance of social recommendation systems can definitely benefit from social theory, as there is a large stream of literature that discusses the potential influence of relevant antecedents on an individual’s evaluation and acceptance of other entities’ recommendations. For other design problems, however, there may not be a clear theoretical basis. A difficult challenge facing a design science researcher is the need to dive into the foreign area of psychological, social, or natural science theories. Beginning with Nunamaker et al. (1991), several papers on IS design research have envisioned a close synergy between the behavioral and the design science research communities (Kuechler et al., 2007). Overcoming differences in training, styles, and worldviews is essential for the success of theory-driven design teams. Possibly, the mode of collaboration in the HCI and CSCW communities could serve as a model for IS design research teams (Orlikowski and Barley, 2001).

If the design research team deems the use of social or psychological theory productive in solving the design problem, then the second move in the heuristics is to survey the relevant theoretical domain to identify constructs that map well to the design goals. Although we cannot expect to find a direct oneto-one mapping, the correspondence should be clear. In our example of a social recommender system, the design goal was to associate a recipient with the sources that would provide the most relevant information for making a recommendation, and the corresponding construct was a recipient’s “likelihood of accepting a source’s advice.” The construct that represents the design goal would become the dependent variable (DV) in the applied theoretical model. These first two steps correspond to path D1 in Figure 3.

The third step is to specify an applied theoretical model that is based on kernel theories (path E in Figure 3), yet will help the researcher tackle to design problem. This step also requires the researcher to weigh the design problem at hand and match it with the theoretical model, with an eye toward the issues of scope and granularity. This entails identifying factors that (a) would be antecedents of the DV in the applied theoretical model, and (b) are important for achieving the design goal. Thus, we seek a mapping between design factors and theory-based constructs. This process is perhaps the most complicated step in our theory-driven design heuristic and requires moving back and forth between kernel theory and design problem. The issue of scope becomes critical in this step, as often there is no single theoretical framework that accounts for all the factors that are important to the design problem. Thus, it is necessary to search the theoretical base for any competing or complementary kernel theories that can explain the DV. Our “likelihood of accepting a source’s advice” construct has been studied in the areas of social psychology, marketing (with a special emphasis on word-of-mouth influence), and knowledge management (and specifically, knowledge sharing). Relevant kernel theories appear – among others – in the works of Levin and Cross (2004) and Gilly et al. (1998). The relevant theoretical frameworks in our context describe a large set of constructs that could impact the recipient’s likelihood of accepting advice, including source characteristics, receiver characteristics, and characteristics that describe the relation between source and receiver. We have chosen to concentrate on the most salient of these constructs: homophily, tiestrength, and a source’s perceived trustworthiness (specifically, competence and benevolence dimensions of trustworthiness).

Determining which constructs are relevant requires a detailed investigation of the design problem (i.e., path D2 in Figure 3). This often entails a thorough review of previous studies in the appropriate design field. In our example, one of the candidate constructs from the kernel theories was homophily (i.e., similarity), which includes both demographic and cognitive dimensions. Cognitive (and specifically, preference) homophily was directly related to the design problem, as it mapped onto one of the factors that could be employed in SRS to associate a recipient with sources (i.e., similarity in users’ purchase history, as employed in collaborative filtering). However, demographic similarity was irrelevant, since it is much more difficult to capture users’ demographic data, and none of the previous works in the area used this type of data. Thus, we included cognitive homophily in our applied

## theoretical model, but excluded demographic homophily (please see details in Section 4.1.4).

Another critical concern – granularity – plays an important role here. There is often a mismatch between the granularity of constructs as they are conceptualized in the kernel theory and the granularity that is necessary for addressing the design problem. In designing social recommender systems, we could harvest users’ communication history to help match a recipient with sources, and either the duration of their relationship or the interaction frequency could be used as an indicator for the relationship. Interestingly, both these factors have been studied in the advice-taking literature; however, these factors were conceptualized as dimensions of a higher level construct – tie strength – in relevant kernel theories. Due to design-related constraints (as well as a theoretical justification that will be explicated in a later section), we formulated these factors as two distinct constructs in our applied theoretical model of a recipient’s likelihood of accepting a source’s advice. Although not the primary goal, this reformulation of tie strength created an opportunity for us to make a contribution to the theoretical domain.

The applied theoretical model can be formulated once a set of constructs has been selected (based on both theoretical justification and design-related constraints) and relationships between these constructs are hypothesized (based primarily on theoretical justification). This applied model is formulated using standard behavioral methods, i.e., as a series of links between explaining and outcome variables. While this model is useful for understanding the complex relationship between constructs, it may be too complicated for guiding design decisions. In our case, the proposed applied theoretical model may be too complex for guiding the design of a social recommender system, as it describes the concurrent effect of all the factors that affect the willingness to accept advice. When designing a social recommender system, relationship data is hard to come by, requiring designers to make a choice between pursuing one type of relationship data over another, and thus, there is a need to simplify the applied theoretical model so that the model can generate specific design propositions (path F in Figure 3). In our case, we moved from a multi-stage path model to a simpler one-step regression model.

To summarize, this study has two primary objectives. The first objective of this paper is to advance the field of design science by incorporating ideas from HCI and extending the Walls et al. conceptualization, as argued above. While we aim to demonstrate the complete set of paths in our enhanced IS design science conceptualization, our focus (and – we believe – our primary contribution) is in the newly introduced component, “applied behavioral theory,” as well as in the new paths (D, E, and F in Figure 3). The second objective of this paper is to propose novel designs for social recommender systems and test the extent to which they improve accuracy. We apply our proposed theory-driven design approach in the context of social recommender systems (SRS) to demonstrate how an applied theoretical model of advice-taking can guide the articulation of a set of testable design product propositions.<sup>8</sup> Since movie and book recommendation systems have paved the way in the development of recommender systems, and some of the most prominent web recommendation systems focus on these domains (e.g., Amazon, NetFlix), we chose to test our model using the movie recommendation domain.

## 4. Kernel Theories of Advice Taking

In this section we review relevant kernel theories and identify a few key constructs that are relevant to our context. Past work in the advice-taking literature has identified variables in three broad categories – source’s characteristics, recipient’s characteristics, and the characteristics that describe the relationship between the source and the receiver – as critical in explaining the likelihood of a receiver seeking a source and accepting his/her advice (Brown and Reingen, 1987; Gilly et al., 1998; Smith et al., 2005). In this research, since we are particularly concerned with the design of a process that associates a specific recipient with relevant sources in SRS, we focus on the two categories that we believe are relevant in generating recommendations for a given receiver – the source's characteristics and the relationship between the source and the recipient.

A recent article (Arazy et al., 2009) reviews the types of social data that are available online that could potentially be utilized in social recommender systems, namely, profile similarity (employed in traditional CF), communication logs (e-mail, instant messaging, etc.), and social network data. They suggest that the design-related factors map onto several theoretical constructs: profile similarity maps onto homophily, communication logs correspond to tie-strength, and social network data maps onto the construct of trustworthiness. Building on these suggestions, we conducted a survey of the advicetaking literature, as described in sub-sections 4.1.1, 4.1.2, and 4.1.3 below. Based on the synthesis of literature on advice taking, as well as the design considerations (as discussed in Section 3.2), we propose that cognitive homophily (source-recipient relationship), tie strength (source-recipient relationship), and competence- and benevolence-based trustworthiness (source characteristic) are central variables that should underpin an applied theoretical model to understand the recipient’s willingness to accept a source’s advice.

## 4.1 Advice Taking and Social Relationships

Work dating to Pelz and Andrews (1966), Mintzberg (1973), and Allen (1977) indicates that people prefer to turn to other people, rather than to documents, when seeking information. Recommendations often are received through word-of-mouth, and such communication tends to flow through interpersonal channels based on shared interests and friendship (Arndt, 1967), both offline and online (Cross and Sproull, 2004). Below, we review studies on the primary factors that determine a recipient’s willingness to accept advice: homophily, tie strength, and trustworthiness.

## 4.2 Tie Strength and Advice Taking

Granovetter (1973) first introduced the concept of tie strength—a characteristic of relationships ranging from weak ties at one extreme to strong ties at the other. Both strong and weak ties may impact the recipient’s decision making (Levin and Cross, 2004). Strong ties are important conduits of useful knowledge (Ghoshal et al., 1994; Hansen, 1999; Szulanski, 1996), and impact a recipient’s willingness to accept a source’s recommendation (Brown and Reingen, 1987; Gilly et al., 1998; de Bruyn and Lilien, 2008). Weak ties, on the other hand, are useful because they are more likely to be sources of novel information (Granovetter, 1973). Research on the importance of weak ties has demonstrated that they can be instrumental in the diffusion of ideas (Granovetter, 1982; Rogers, 1995) and receipt of work-related advice (Constant et al., 1996; Levin and Cross, 2004). Levin and Cross (2004) integrated the two perspectives and demonstrated that tie strength has a direct negative effect (i.e., “the strength of weak ties”), as well as an indirect positive effect (through the mediation of trustworthiness) on the receipt of useful knowledge.

Tie strength is a multi-dimensional construct (Granovetter, 1973; Marsden and Campbell, 1984; Money et al., 1998); it characterizes the closeness (i.e., emotional intensity) and time dimensions (i.e., duration and frequency) of a relationship between two parties (Granovetter, 1973; Marsden and Campbell, 1984; Mathews et al., 1998; Hansen, 1999; Petroczi et al., 2006).<sup>9</sup> Prior studies on advice taking have focused on closeness as the primary indicator of tie strength (e.g., Brown and Reingen, 1987; Bansal and Voyer, 2000; Smith et al., 2005).

## 4.3 Trustworthiness and Advice Taking

The concepts of trust and trustworthiness have attracted much interest recently and have been identified as a key factor in inter-personal relations, especially in the online environment. Mayer and others (1995, p. 712) define trust as “the willingness of a party to be vulnerable.” Our focus here is on the closely related concept of perceived trustworthiness, i.e., the quality of the trusted party (i.e., the recommendation source) that makes the recipient willing to be vulnerable. The trust literature (see Dirks and Ferrin, 2001; Mayer et al., 1995 for reviews) provides considerable evidence that trusting relationships lead to greater knowledge exchange (Gibbons, 2004; Carley, 1991; Mayer et al., 1995; Currall and Judge, 1995; Zaheer et al., 1998), and as a result, trustworthiness affects a recipient’s willingness to accept a source’s advice (Levin and Cross, 2004).

Trustworthiness is a multi-dimensional concept. Mayer et al. (1995) identify three dimensions of trustworthiness: benevolence (a trustee’s caring and motivation to act in the recipient’s interests), integrity (a trustee’s honesty and promise keeping), and competence (ability of the trustee to do whatever the recipient needs), and we adopt this conceptualization, as it was used most commonly in advice-taking studies (e.g., Levin and Cross, 2004; McKnight et al., 2002). Following Levin and Cross (2004), we have decided to concentrate on the dimensions of benevolence and competence, “given the relevance of these dimensions to the knowledge-seeking context” (p. 1478). Integrity, the third trustworthiness dimension, is less likely to impact the recipient’s likelihood of accepting a source’s recommendation, especially for interpersonal interactions (Levin and Cross, 2004, p. 1478). 10

## 4.4 Homophily and Advice Taking

Homophily – the similarity between individuals – is distinct from the concept of tie strength (Marsden and Campbell, 1984; Petroczi et al., 2006). Early literature on homophily examined its role in enabling the formation of social ties (see reviews in Huston and Levinger, 1978; McPherson et al., 2001) and its effect on tie strength (Marsden and Campbell, 1984). This suggests that homophily could impact a recipient’s likelihood of advice taking through the mediating role of tie strength. More recently, marketing literature has placed homophily on the center stage, and has demonstrated its substantial effect on a recipient’s willingness to accept a source’s recommendations (Gilly et al., 1998; de Bruyn and Lilien, 2008).

Homophily between two parties – recommendation recipient and source in our context – could be measured along various dimensions. Homophily research has focused on two key dimensions: sociodemographic (e.g., race, gender) and cognitive (e.g., preferences, attitudes, aspirations, values)<sup>11</sup> (McPherson et al., 2001). This study focuses on cognitive homophily, since it is “presumed to shape our orientation toward future behavior” (p. 419) and has a direct impact on a recipient’s choice of sources (Gilly et al., 1998; de Bruyn and Lilien, 2008), while socio-demographic homophily is usually seen as an antecedent of cognitive homophily (McPherson et al. 2001), and does not have a significant direct effect on a recipient’s choice of sources (Gilly et al., 1998; de Bruyn and Lilien, 2008). Moreover, this study is interested in movie recommendations, and in this context, recipientsource similarity in tastes and preferences is more likely to impact the recipient’s source selection (Smith et al., 2005).

## 5. An Applied Theory of Advice Taking to Guide SRS Design

In this section we develop our applied theoretical model, intended to guide the design of the SRS system module that associates a recipient with relevant sources. In Section 5.1 we propose a set of hypotheses regarding the relationships between the constructs that impact a recipient’s advice-taking decision and introduce our proposed applied path model; in Section 5.2 we present the method for evaluating the applied theoretical model; in Section 5.3 we report on the results of this evaluation; and in Section 5.4 we present a simplified linear regression model that could directly inform system design.

## 5.1. Hypotheses

Although the factors affecting a recipient’s willingness to accept advice have been explored in previous studies, existing theoretical frameworks of advice taking are lacking in their suitability to serve as an applied theory for guiding the design of SRS for two primary reasons: scope and granularity.

First, research on advice taking is fragmented into various research strands, and each strand focuses on only a partial set of factors that are important for SRS. Levin and Cross (2004) make an important step toward the goal of integrating advice-taking literatures, and have proposed a framework of knowledge sharing, which includes both tie strength and trust. However, their model is less appropriate for directing the design of SRS, since it overlooks the role of cognitive homophily. Similarly, marketing literature emphasizes the role of homophily in advice taking (e.g., Gilly et al., 1998), but overlooks other factors that are important in the SRS context, such as tie strength. Our goal is to develop an applied theory that includes those relationship factors that are relevant for social recommender system design.

A second limitation of existing theoretical models is that their granularity is not suitable for guiding the design of social recommender systems, as discussed in Section 3.2. The granularity at which we investigate the model’s constructs is guided by system design considerations, but is also informed by theory. Two constructs of interest – tie strength and trustworthiness – are multi-dimensiona constructs, and we argue for treating each of the dimensions of these constructs as distinct variables.

Prior studies on trustworthiness have demonstrated that this construct’s two dimensions – competence and benevolence – have distinct effects on willingness to accept advice (Levin and Cross, 2004). In addition, from a practical perspective, it is important that the proposed model treats competence and benevolence as distinct constructs, since they map onto alternative types of social network data; professional networks (e.g., LinkedIn) are likely to be based largely on competence, while relationships in friendship networks (e.g., Facebook) will likely contain a large benevolence component.

Tie strength has often been conceptualized in previous studies of advice taking as a one-dimensional construct (Levin and Cross, 2004; de Bruyn and Lilien, 2008), although it is acknowledged that this construct includes the dimensions of tie duration, interaction frequency, and perceived closeness (Marsden and Campbell, 1984; Mathews et al., 1998). From a SRS design perspective, there is an advantage in treating the dimensions of duration and frequency as distinct constructs, since they correspond to alternative metrics. For example, in online settings, interaction frequency could correspond to data computed from instant messaging communication logs, relationship duration could be operationalized based on the time a friend was added to the e-mail contact list, and closeness maps to relations that are captured in social networks such as NetFlix. From a theoretical perspective, empirical studies of tie strength demonstrate that closeness and relationship time (frequency and duration) are distinct constructs. For example, Marsden and Campbell (1984) report on three studies with relatively low correlations (ranging from 0.10 to 0.26) between frequency and closeness.

In summary, an applied theoretical model that would guide the design of SRS should include constructs and relationships that are justified from both theoretical and practical perspectives. Our proposed framework considers cognitive homophily, trustworthiness, and tie strength as the primary determinants of a recipient’s willingness to accept advice. Further, we treat both tie strength and trustworthiness as multi-dimensional constructs. Below, Table 1 provides an overview of our theory development, and Figure 4 presents a simplified view of our proposed applied model. In the section that follows, we will explicate a set of hypotheses and introduce our detailed applied theoretical model.

<table><tr><td colspan="4">Table 1: The development of our proposed applied theoretical model</td></tr><tr><td>Kernel Theories and key papers</td><td>Construct</td><td>Effect</td><td>Related Hypotheses</td></tr><tr><td>Theory of Interpersonal Attraction (Social Psychology): Byrne et al., 1967; Lazarsfeld &amp; Merton, 1954</td><td>Cognitive Homophily</td><td>Positive direct effect on: Tie Strength (Duration, Frequency, and Closeness)</td><td>1a, 1b, 1c</td></tr><tr><td>Reinforcement Theories (Social Psychology): Berger &amp; Calabrese, 1975</td><td>Tie Strength: Frequency, Duration</td><td>Positive direct effect on: Tie Strength: Closeness</td><td>1d, 1e</td></tr><tr><td>Word-of-Mouth Influence Theories (Marketing, Social Psychology): Gilly et al., 1998; Smith et al., 2005</td><td>Tie Strength: Closeness</td><td>Positive direct effect on: Willingness to Accept Advice</td><td>2a</td></tr><tr><td>The Strength of Weak Ties Theory (Sociology and Knowledge Sharing): Granovetter, 1973; Levin &amp; Cross, 2004</td><td>Tie Strength: Frequency, Duration</td><td>Negative direct effect on: Willingness to Accept Advice</td><td>2b, 2c</td></tr><tr><td>Social Influence Theories (Social Psychology, Marketing and Knowledge Sharing): Tsai &amp; Ghoshal, 1998; Levin &amp; Cross, 2004; Gibbons, 2004</td><td>Tie Strength: Closeness</td><td>Positive effect on: Willingness to Accept Advice mediated by: Trustworthiness (Competence and Benevolence-based)</td><td>3a, 3b, 3c, 3d</td></tr><tr><td>Word-of-Mouth Influence Theories (Marketing and Social Psychology): Gilly et al., 1998; Smith et al., 2005</td><td>Cognitive Homophily</td><td>Positive direct effect on: Trustworthiness (Competence and Benevolence-based)</td><td>4a, 4b</td></tr><tr><td>Word-of-Mouth Influence Theories (Marketing and Social Psychology: Yaniv, 2004; Gilly et al., 1998)</td><td>Cognitive Homophily</td><td>Positive direct effect on: Willingness to Accept Advice</td><td>4c</td></tr></table>

![](/api/attachments/S2U4KS23/fulltext/images/ffb60f0fddd7e18f9711bd7b8b8d8adffc3f7d488a29c38d96868e08e2785c3e.jpg)  
Figure 4. A simple view of our proposed applied theoretical model; all links represent a positive effect, except the link between tie strength and the willingness to accept advice (in dotted line), which has a mixed effect

## 5.1.1 Cognitive Homophily and Tie Strength

“Similarity breeds connection.” This principle structures network ties of every type, including marriage, friendship, work, advice, support, information transfer, exchange, co-membership, and other types of relationship” (McPherson et al., 2001, p. 415). Social ties often begin with attraction to similar others (Verbrugge, 1977; Carley, 1991). Lazarsfeld and Merton (1954), in a seminal work on homophily, argue that most human communication will occur between a source and a seeker who are similar. The theory of interpersonal attraction – one of the widely studied interpersonal theories – states that individuals who are similar to each other are attracted to each other (Byrne et al., 1967). Further, shared beliefs among similar individuals facilitate positive connections by reducing uncertainty and increasing predictability, thus facilitating improved communications (Berscheid and Walster, 1978; Huston and Levinger, 1978; McPherson et al., 2001). Online relationships resemble offline interaction patterns (Wellman, 1997, 2001), and thus, we expect an association between cognitive homophily and tie strength dimensions in online settings.

Since the unique context in which we are interested requires that duration, frequency, and closeness be treated as distinct constructs, we will model the impact of cognitive homophily on each of these constructs. To the extent that interaction is voluntary, similar individuals are, thus, likely to spend more time together. Moreover, cognitive homophily acts as the glue that cements relationships, and similar individuals are likely to maintain their relationships over longer time periods, and we propose:

H 1a: Cognitively similar individuals will maintain relationships that are longer temporally.

Past research has shown that people who are similar to each other not only communicate with each other more frequently (Lincoln and Miller, 1979; Ibarra, 1992) but also use a variety of communication tools to increase the frequency of interaction (Haythornthwaite, 2001). Formally stated:

H 1b: Cognitively similar individuals will interact more frequently.

Homophily also fosters friendship and enables the formation of close personal ties, as noted by the classical Greek philosopher. Aristotle writes that people “love those who are like themselves” (Aristotle, 1934, p. 1371). Plato observed that “similarity begets friendship” (Plato, 1968, p. 837). Modern psychology literature has demonstrated experimentally that attraction is affected by perceived similarity (Huston and Levinger, 1978). Recent research has shown that a baseline level of cognitive homophily is essential for more intense and closer relationships between individuals (Reagans, 2005). Thus, we propose:

H 1c: Cognitively similar individuals will feel close to one another.

The sheer time that people spend together often leads to a feeling of closeness, especially if the interactions are on a voluntary basis (Huston and Levinger, 1978; McPherson et al., 2001). Research on tie strength has found association between both time dimensions – frequency and duration – and closeness (Marsden and Campbell, 1984). Specifically, reinforcement theories in psychology emphasize the role of uncertainty reduction as the more time (frequency and duration) cognitively similar individuals spend together, the better they understand their underlying similarities, resulting in more intense and closer relationships (Berger and Calabrese, 1975). Thus, we propose:

H 1d: Individuals who interact frequently will feel close to one another.

H 1e: Individuals who have known each other for a long time will feel close to one another.

## 5.1.2 Tie Strength and Willingness to Accept Advice

Prior research demonstrates that strong ties are important conduits of useful knowledge (Ghoshal et al., 1994; Hansen, 1999; Szulanski, 1996). To the extent that interaction frequency and duration are voluntary, they are likely to have a positive effect on closeness (see Hypotheses 1d, 1e). Closeness, in turn, is likely to have a positive impact on the willingness to accept advice, and this effect has been demonstrated in online settings (Smith et al., 2005). Thus, we propose:

H 2a: (After controlling for indirect effects), tie strength expressed in terms of closeness will have a positive impact on willingness to accept advice.

Beyond the mediated (by closeness) positive impact of frequency and duration, these constructs may exhibit a negative effect on the willingness to accept advice. Weaker ties have the potential to expose the recipient to novel information, and this notion of advice seekers receiving new and useful information from casual acquaintances – i.e. “the strength of weak ties” – has been well documented in previous literature (Granovetter, 1973; Levin and Cross, 2004). Hence, we propose:

H 2b: (After controlling for indirect effects), tie strength expressed in terms of frequency of interaction will have a negative impact on willingness to accept advice.

H 2c: (After controlling for indirect effects), tie strength expressed in terms of relationship duration will have a negative impact on willingness to accept advice.

## 5.1.3 Trustworthiness, Tie Strength, and Willingness to Accept Advice

Many studies have shown that strong ties – and specifically closeness – impact the recipient’s willingness to accept a source’s recommendation (Brown and Reingen, 1987; Gilly et al., 1998; de Bruyn and Lilien, 2008).<sup>12</sup> We argue, consistent with Tsai and Ghoshal (1998) and Levin and Cross (2004), that close relationships are helpful because they tend to be trusting. Moreover, both trustworthiness dimensions – competence and benevolence – could impact the willingness to accept advice, as “trusting a knowledge source to be benevolent and competent should increase the chance that the knowledge receiver will learn from the interaction” (Levin and Cross, 2004; p. 1479).

Benevolence-based trust is more likely to occur among close ties (Currall and Judge, 1995; Glaeser et al., 2000; Ma, 1985; Huston and Levinger, 1978), presumably due to greater emotional bonds (Levin and Cross, 2004). When advice seekers ask for information, they become vulnerable to the benevolence of the knowledge source (Lee, 1997), e.g., in terms of their reputation (Burt and Knez, 1996). Therefore, placing faith in the sources’ good intentions increases willingness to consider their suggestions (Gibbons, 2004). Specifically, the effect of benevolence on advice taking was observed in the context of e-commerce (McKnight et al., 2002). Thus, benevolence mediates the relationship between closeness and the willingness to accept advice, and we propose:

H 3a: Tie strength expressed in terms of closeness will have a positive impact on a source’s benevolence-based trustworthiness.

H 3b: A source’s benevolence-based trustworthiness will have a positive impact on the

recipient’s willingness to accept advice.

Competence, too, plays an important role in advice taking. Through shared experiences, the recipient forms a perception of the source’s expertise and learns to seek advice in those domains in which the source is perceived to be competent (Rulke and Rau, 2000). This narrowing process should increase the source’s competence-based trustworthiness (Gibbons, 2004), as restricting the domain of queries to the other party’s area of expertise will lead to increasingly positive interactions (Levin and Cross, 2004). Positive perception of a source’s competence, in turn, increases the recipient’s willingness to accept the source’s advice (Gibbons, 2004; Bristor, 1990; Bansal and Voyer, 2000; Briggs et al., 2002). Advice seekers who trust a source’s competence in a specific domain are “more likely to listen to, absorb, and take action on that knowledge” (Levin and Cross, 2004, p. 1480). Competence has been shown to affect the recipient’s advice-taking process in a variety of settings (Bansal and Voyer, 2000; Gilly et al., 1998, McKnight et al., 2002; Smith et al., 2005). Thus, competence, too, mediates the relationship between closeness and the willingness to accept advice. Stated formally:

H 3c: Tie strength expressed in terms of closeness will have a positive impact on a source’s competence-based trustworthiness.

H 3d: A source’s competence-based trustworthiness will have a positive impact on the recipient’s willingness to accept advice.

## 5.1.4 Homophily, Trustworthiness, and Willingness to Accept Advice

The previous sections elucidated the rationale behind how personal similarity could lead to social interaction (Hypotheses 1a-1e), and, subsequently, to the development of trust (Hypotheses 3a-3d). However, similarity could also have a direct impact on the source’s perceived trustworthiness, even with very limited social interaction. Based on appearance, body language, and accent, a recipient may associate the source with a certain stereotype, approximate his cognitive similarity (i.e., cognitive homophily) to the source, and develop preliminary perceptions of the source’s trustworthiness.

This interpersonal process has been investigated in marketing literature, in the context of an agentconsumer interaction. Findings suggest that the perceived similarity between a consumer and an information agent may influence the amount of trust that is placed in an information agent (Brown and Reingen, 1987; Feick and Higie, 1992; Gilly et al., 1998). This effect also prevails in online environments where recipients may base their judgments of the trustworthiness and relevance of the recommendation upon the perceived similarity of the source’s attitudes and tastes (Smith et al., 2005).

Information about another individual’s similarity is often interpreted as an indicator of the other’s benevolence (Johnson and Johnson, 1972; Sole et al., 1975; Stapleton et al., 1973; Huston and Levinger, 1978) or competence (Huston and Levinger, 1978; Brickman et al., 1975). Thus, we propose:

H 4a: Cognitive homophily has a direct positive impact on the source’s benevolence-based trustworthiness.

H 4b: Cognitive homophily has a direct positive impact on the source’s competence-based trustworthiness.

Yaniv (2004) argues that, in domains where consumption choices are primarily based on personal preferences (“taste domains,” e.g., movies), the most important factor in determining the benefit of a piece of advice is recipient-source similarity. This research argues that cognitive homophily has a direct impact on a recipient’s willingness to accept advice, beyond its influence through the mediation of trustworthiness (for both familiar and unfamiliar sources). The Theory of Interpersonal Similarity suggests that when an individual perceives someone to be similar, she is likely to evaluate the opinions of the source more positively (Byrne et al., 1967). Past research in marketing has demonstrated that cognitive homophily has a direct influence on a seeker’s decision and has suggested that homophilious sources have a greater impact than experts on advice seekers’ decision making (Gilly et al., 1998). The direct influence of cognitive homophily is also evident in the popular recommendation systems employed by websites such as Amazon.com and Netflix.com, which use actual, computed values of perceptual similarity to make recommendations even if the users have never met. Thus, we propose:

H 4c: Cognitive homophily has a direct positive impact on a recipient’s willingness to accept a source’s recommendation.

In sum, we propose an applied theoretical model of advice taking that includes relations between cognitive homophily, tie strength, trustworthiness, and a recipient’s willingness to accept a source’s advice. The detailed research model, including the hypothesis, is presented in Figure 5 below.

![](/api/attachments/S2U4KS23/fulltext/images/edad7d5cc89c434fab83e85845bbdc1fdbcba83d25f21896eca3f87c17d22d8d.jpg)  
Figure 5. The detailed applied theoretical model; tie strength and trustworthiness are presented at their various dimensions; hypotheses are indicated along the links

## 5.2 Research Method for Testing the Applied Theory

This research employed a survey methodology to test the hypotheses proposed in the previous section. We adopted the perceptual measures (see Appendix A) from existing instruments used in previous studies. Survey items were measured using seven-point Likert scale, with 1 indicating “strongly disagree” and 7 indicating “strongly agree.” Cognitive homophily was operationalized based on the validated scale used by Gilly et al. (1998). We adopted Tie strength operationalization from Levin and Cross (2004), but separated it into its constituent dimensions – frequency, duration, and closeness<sup>13</sup> – based on past literature (Marsden and Campbell, 1984). We adopted the items for measuring competence and benevolence-based trustworthiness from McKnight et al. (2002). The dependent variable, recipient’s willingness to accept advice, was adopted from Gilly et al. (1998). We chose to use survey data, rather than data logs of online communications, because a survey allows us to capture all the recipient-source relationships that are specified by our research model, while most of the existing online systems capture only a partial set of relationships that they develop by trial and error (e.g., Amazon’s recommendation system primarily utilizes consumption profile similarity).

We translated the survey items administered from English to Hebrew according to the guidelines proposed by Brislin et al. (1973), as is common in cross-cultural information systems research (Karahanna et al., 2002). Translation from English to Hebrew was performed independently by two of

<sup>13</sup> The scale for measuring frequency and duration was anchored in specific numbers For example, Tie Strength Frequency was measured by: 1 = once every 3 months or less (or never); 2 = once every second month; 3 = once a month; 4 = twice a month; 5 = once a week; 6 = twice a week; and 7 = daily.

the researchers (who are fluent in both languages), and the measures were finalized after the researchers discussed the items to resolve any differences that may have arisen. A third party (fluent in both languages) then back-translated the items from Hebrew to English, thus ensuring correctness of the translation.

We recruited 116 participants from among undergraduate students of a large public university in Israel. The average age of the participants was 24.5 (the youngest participant was 20 years old and the oldest was 28 years old). The students were pursuing an engineering degree and were enrolled in the third year of the program. Even though the classroom can be perceived as a non-voluntary setting, we argue that voluntary relationships are likely to develop for students jointly taking courses for two to three years. The results of the study confirmed that such relationships, indeed, developed for our sample.

The participants were asked to imagine a scenario where they were planning to go out for a movie and were looking for movie recommendations. We adopted the methodology used by Marsden and Campbell (1984), and required participants to choose three sources within their cohort from whom they would likely seek advice on movies. The participants then rated these sources on the perceptua measures that are included in the research model. The participants were assured that their ratings would be kept private, and that the researchers would strip common identifiers, such as names and email addresses, before beginning data analysis.

## 5.3. Results from Testing the Applied Theoretical Model

We conducted data analyses using the Partial Least Squares (PLS) path-modeling algorithm (Fornell and Cha, 1994; Chin and Newsted, 1999; Marcoulides et al., 2009). The PLS algorithm estimates path models using composite variables, sometimes called latent variables, from a number of indicator items, sometimes called manifest variables.

We analyzed the psychometric properties of the instrument before examining the data for hypotheses testing. Table 2 presents the composite reliability, average variance extracted (AVE), and correlations between the composite constructs. The estimates for composite reliability exceed 0.7 for each of the constructs, demonstrating good internal consistency. The convergent validity of the measures was assessed by examining the individual item loadings between an item and its corresponding underlying factor, as well as the AVE. All item loadings were greater than the suggested minimum level of 0.7, and the AVE for each construct was substantially greater than the suggested minimum of 0.5 (Fornell and Larcker, 1981).

We assessed discriminate validity by comparing the square root of the AVE (RAVE) of a particular construct (presented in Table 2 on the diagonal, in bold) and the correlation between that construct and other latent constructs (presented by the off-diagonal position of the table). We found that the constructs’ RAVE ranges from 0.88 to 1.00, while correlations between constructs do not exceed 0.55. Moreover, RAVE for every construct is substantially higher than the correlation between that construct and all other constructs, signifying good discriminate validity.

<table><tr><td colspan="10">Table 2: composite reliability, AVE, and correlations between the composite constructs</td></tr><tr><td>Constructs</td><td>Composite Reliabilities</td><td>AVE</td><td>Cognitive Homophily</td><td>- Tie strength - Frequency</td><td>- Tie strength - Duration</td><td>- Tie strength - Closeness</td><td>Benevolence</td><td>Competence</td><td>Willingness to Accept Advice</td></tr><tr><td>Cognitive Homophily</td><td>0.87</td><td>0.78</td><td>0.88</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tie strength - Frequency</td><td>1.00</td><td>1.00</td><td>0.32</td><td>1.00</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Tie strength - Duration</td><td>1.00</td><td>1.00</td><td>0.17</td><td>0.35</td><td>1.00</td><td></td><td></td><td></td><td></td></tr><tr><td>Tie strength - Closeness</td><td>1.00</td><td>1.00</td><td>0.49</td><td>0.55</td><td>0.35</td><td>1.00</td><td></td><td></td><td></td></tr><tr><td>Benevolence</td><td>0.91</td><td>0.84</td><td>0.49</td><td>0.31</td><td>0.20</td><td>0.61</td><td>0.92</td><td></td><td></td></tr><tr><td>Competence</td><td>0.93</td><td>0.87</td><td>0.21</td><td>0.04</td><td>0.10</td><td>0.17</td><td>0.26</td><td>0.93</td><td></td></tr><tr><td>Willingness to Accept Advice</td><td>0.88</td><td>0.78</td><td>0.48</td><td>0.19</td><td>0.14</td><td>0.44</td><td>0.47</td><td>0.44</td><td>0.88</td></tr></table>

These results support the convergent validity of the measures

After corroborating the validity of the measures, we tested the research model through the PLS structural model. We specified paths in the PLS structural model corresponding to the relationships hypothesized in our research model. The significance of structural path estimates was computed using the bootstrapping re-sampling method (with 100 re-samples; c.f. Tenenhaus et al., 2005). We evaluated the structural model on the basis of R² for each composite latent variable and statistica significance of structural paths. Figure 6 shows that the results of the PLS analysis support all the proposed hypotheses, except for H2b, H2c and H3b (paths were insignificant at p<0.05).

![](/api/attachments/S2U4KS23/fulltext/images/ad3a8dda7f1cce313532dbf3447032a446d48305232a35f01976871736ad52b4.jpg)  
Figure 6. Results of PLS analysis; values along arrow represent path significance and R² values in latent construct boxes represent the variance explained for that construct.

## 5.4 A Simplified Model to Guide System Design

The results of the structural model reveal the intricate relationship between the various factors that affect a recipient’s advice-taking decision. Such a complex model helps us understand how the various relationship constructs impact one another, and would be useful in directing system design for several indicators of social relationships that are available. However, for practical reasons, attaining more than one relationship data type – on top of preference similarity – is often not feasible.

In designing social recommender systems (see Section 2 for details), source selection is typically based on both profile similarity (i.e., traditional CF) and an additional social relationship indicator. The practical question, then, is which type of relationship data will provide the best system performance? To answer this question, we developed a simple model that included homophily as the single antecedent of willingness to accept advice (WAA), and then added one relational construct at a time. This simplified applied model would have immediate implications for SRS design. Table 3 below reports on the results of the regression analysis.

<table><tr><td colspan="3">Table 3: Results of regression analysis on Willingness to Accept Advice (WAA)</td></tr><tr><td>WAA Antecedents</td><td>Adjusted R2</td><td>R2 Changes</td></tr><tr><td>Homophily</td><td>0.237</td><td></td></tr><tr><td>Homophily + TS Frequency</td><td>0.234</td><td>-0.003 (-1%)</td></tr><tr><td>Homophily + TS Duration</td><td>0.238</td><td>+0.001 (+0%)</td></tr><tr><td>Homophily + TS Closeness</td><td>0.286</td><td>+0.049 (+21%)</td></tr><tr><td>Homophily + Competence-Based Trustworthiness</td><td>0.351</td><td>+0.114 (+48%)</td></tr><tr><td>Homophily + Benevolence-Based Trustworthiness</td><td>0.301</td><td>+0.064 (+27%)</td></tr></table>

## 6. Design Principles for Social Recommender System

In this section, we proceed to develop the remaining components of our proposed theory-driven design framework for the specific design context of SRS. Our proposed frameworks extend the Walls et al. (1992) ISDT by introducing the applied theoretical model. In the previous sections, we discussed the kernel theories and our applied theoretical model. The remaining components of the framework – meta-requirements, meta-design, and testable design product propositions – correspond to Walls et al.’s original conceptualization, as illustrated in Figure 3. Below, we formulate the principles for the design of the SRS module associating recipients with sources.

## 6.1 Meta Requirements

As defined by Walls et al. (1992), meta-requirements describe the class of goals to which the design theory applies. The meta-requirements for the design problem at hand are informed by both kernel and applied behavioral theories of advice taking. We derived a set of high-level requirements for the SRS module that associates a recipient with relevant sources, as follows (see summary in Table 4).

Establish a metric of users’ preference similarity by first developing users’ profiles, through tracking their consumption history or asking users to explicitly state their preferences (e.g., rating of consumed items). Second, the system would need an algorithm for comparing profiles and producing a similarity score.

Establish metrics of users’ tie strength (in terms of duration, frequency, and closeness). This could be done by harvesting data from existing communications systems (such as phone, email, or instant messaging), by analyzing online social network data, or by allowing users to explicitly describe the strength of their ties.

Establish metrics of users’ trustworthiness (in terms of both competence and benevolence). This could be done by harvesting data from online social networks, or, alternatively, by asking the users to explicitly describe their perceptions of sources’ competence and benevolence.

Table 4: Meta-requirements for associating a recipient with relevant sources in SRS

Arrive at a single similarity score, based on the various relationship data available. This entails normalizing the various relationship metrics so they all share the same scale and aggregating the various relationship indicators weighting each source by its importance.

Predict relevant items for a user by considering related sources (linked to the user through any of the social relationships indicators reviewed above) and these sources’ consumption profiles. For example, by using the Resnick (1994) prediction formula described in Section 2.

 Recommend these potentially relevant items to the user.

Protect users’ privacy by ensuring that (a) users are made aware of what data is collected, (b) users’ consent is obtained, and (c) data related to users’ relationships and consumption is protected.

<table><tr><td>Meta-Requirement</td><td>Description of SRS Goals</td><td>Associated Applied Theoretical Model Hypotheses</td></tr><tr><td>MR1</td><td>Establish a metric of users&#x27; preference similarity.</td><td>1a-c, 4a-c</td></tr><tr><td>MR2</td><td>Establish metrics of users&#x27; tie strength</td><td>1d-e, 2a-c</td></tr><tr><td>MR3</td><td>Establish metrics of users&#x27; trustworthiness</td><td>3a-d</td></tr><tr><td>MR4</td><td>Arrive at a single similarity score, based on all the relationship data</td><td>All hypotheses (1a-c, 2a-c, 3a-d, 4a-c)</td></tr><tr><td>MR5</td><td>Predict the relevancy of items to users</td><td>NA</td></tr><tr><td>MR6</td><td>Make recommendation of the relevant items to users</td><td>NA</td></tr><tr><td>MR7</td><td>Protect users&#x27; privacy</td><td>NA</td></tr></table>

## 6.2 Meta Design

As defined by Walls et al. (1992), meta-design "describes a class of artifacts hypothesized to meet the meta-requirements." We derive the meta-design specification for the SRS by building on the articulation of meta-requirements, as described in Table 5. Meta design items MD1-4 were inferred directly from the first meta-requirement, MR1, which handles the elicitation of users’ preferences. To enable collection of feedback (e.g., rating of recommended items, similarly to Amazon), a SRS must include an interface for users to provide explicit feedback (MD1). Alternatively, the system may automatically track the users’ interactions (e.g., purchasing history, time spent browsing items) and implicitly infer their feedback on specific items based on their online behavior (MD2). MD3 provides the data structure to maintain users’ interaction behavior and their preferences. MD4 handles the calculation of users’ preference similarity, based on their profiles. MD5 and MD6 allow the SRS to gather relevant social relationship data. MD7 provides the data structure to maintain users’ relationship data. MD8 combines all relationship data into a single similarity score. MD9 handles the prediction of items for each user by associating the user with others with whom he has relationships, and by analyzing the preferences of these relevant others to find items the user has not yet consumed/rated. MD10 handles the presentation of recommendations to users. Finally, MD11 deals with appropriate measures required to protect users’ privacy.

<table><tr><td colspan="3">Table 5: Meta-design for associating a recipient with relevant sources in SRS</td></tr><tr><td>Meta-Design</td><td>Description of SRS Design to Meet the Goals</td><td>Corresponding Meta-Requirement</td></tr><tr><td>MD1</td><td>A user interface to allow users to report their feedback</td><td>MR1</td></tr><tr><td>MD2</td><td>An automatic algorithm for monitoring users&#x27; interaction</td><td>MR1</td></tr><tr><td>MD3</td><td>A data structure to maintain users&#x27; interaction history</td><td>MR1</td></tr><tr><td>MD4</td><td>An algorithm for comparing users&#x27; preference profiles</td><td>MR1</td></tr><tr><td>MD5</td><td>A process for estimating the strength of users&#x27; ties, by linking to existing applications where the strength of ties are already specified, or by allowing users to explicitly specify the strength of their ties</td><td>MR2</td></tr><tr><td>MD6</td><td>A process for estimating the users&#x27; trustworthiness in one another, by linking to existing online social network where trust relations are already specified, or by letting users explicitly specify their perceptions of others&#x27; trustworthiness</td><td>MR3</td></tr><tr><td>MD7</td><td>A data structure to maintain users&#x27; relationship data</td><td>MR1, MR2, MR3</td></tr><tr><td>MD8</td><td>An algorithm for combining the various social data into a single similarity score</td><td>MR4</td></tr><tr><td>MD9</td><td>An algorithm to predict which items are relevant to a user</td><td>MR5</td></tr><tr><td>MD10</td><td>An interface to recommend relevant items to users</td><td>MR6</td></tr><tr><td>MD11</td><td>Privacy consent forms, a privacy policy, and data security measures.</td><td>MR7</td></tr></table>

## 6.3 Testable Design Propositions

One could articulate numerous testable design propositions (or hypotheses) regarding the extent to which the meta-design satisfies the meta-requirements. However, within the context of a single study, only a few propositions could be articulated and tested (Walls et al., 1992). For the purpose of this study, we have articulated a set of propositions regarding social recommender systems, as described in Table 6.

The first set of design propositions, TDP1a-e, describe the feasibility of the proposed SRS design, and were derived directly from the meta-design. The remaining propositions, TDP2-2e, relate to the ability to enhance SRS prediction accuracy, and were articulated based on the findings from the evaluation of the applied theoretical model. Evaluation of the applied theoretical model showed that competence, benevolence, and closeness yield substantial improvements, while duration and frequency of interaction do not seem to affect the outcome variable much (see Table 3 for details). Thus, we expect that recommender system accuracy will improve (beyond the use of preference similarity) when we add relationship data that captures competence, benevolence, or closeness. In contrast, we anticipate no yield enhancements when communication data that capture duration or frequency are employed.

<table><tr><td colspan="3">Table 6: Testable design product propositions</td></tr><tr><td>Testable Design Proposition</td><td>Description of a Proposition about the Design</td><td>Corresponding Meta-Design</td></tr><tr><td>TDP1</td><td>It is feasible to design a social recommender system that associates a recipient with relevant sources by employing various indicators of social relationships</td><td>See below specific meta-design items for TDP1a-e</td></tr><tr><td>TDP1a</td><td>It is feasible to obtain users&#x27; preference information (through implicit or explicit feedback) and to compute users&#x27; preference similarity</td><td>MD1, MD2, MD3, MD4</td></tr><tr><td>TDP1b</td><td>It is feasible to gather social data about users, by either linking to existing online applications that capture these relationships or by having users explicitly specify their relationships to others</td><td>MD5, MD6, MD7</td></tr><tr><td>TDP1c</td><td>It is feasible to combine various social data into a single recipient-source similarity score</td><td>MD8</td></tr><tr><td>TDP1d</td><td>It is feasible to predict the relevancy of items to users</td><td>MD9, MD10</td></tr><tr><td>TDP1e</td><td>It is feasible to set privacy procedures and security measures that would satisfy users</td><td>MD11</td></tr><tr><td>TDP2</td><td>Recommendation accuracy could be improved when social relationship data is utilized (in addition to profile similarity data)</td><td>All the meta-design items corresponding to TDP1a-e, in addition to specific meta-design items for TDP2a-e</td></tr><tr><td>TDP2a</td><td>Recommendation accuracy would improve when we include recipient&#x27;s perceived competence of the source</td><td>MD6</td></tr><tr><td>TDP2b</td><td>Recommendation accuracy would improve when we include recipient&#x27;s perceived benevolence of the source</td><td>MD6</td></tr><tr><td>TDP2c</td><td>Recommendation accuracy would improve when we include recipient&#x27;s perceived closeness to the source</td><td>MD5</td></tr><tr><td>TDP2d</td><td>Recommendation accuracy would not improve when we include users&#x27; interaction frequency</td><td>MD5</td></tr><tr><td>TDP2e</td><td>Recommendation accuracy would not improve when we include users&#x27; tie duration</td><td>MD5</td></tr></table>

## 7. Recommender System Evaluation

In the following section we report on experiments with a recommender system prototype. Our objective was to explore the source-selection system component, rather than to develop a full-scale SRS. Our evaluation considered various alternatives methods for associating a recipient with relevant sources, based on the types of social relationships that were explored in our applied theoretica model. Since the first four design propositions, TDP1-4, were confirmed through the implementation of many commercial applications and research prototypes (see Section 2 for details), our evaluation focused on the extent to which relationship data could improve recommendation accuracy.

## 7.1 Recommender System Architecture

We implemented and compared different recommender algorithms: collaborative filtering (CF; used as a baseline) and various social-data-enhanced algorithms. We used the same sample of users from the behavioral study reported in Section 5.2. We asked the same subjects who reported on their relationships to rate movies (70 popular recent movies, as well as movies specified by individual users), which resulted in a set of 240 unique movies. For the system evaluation experiments, we used the data obtained from the 99 subjects who completed both the relationship survey and movie ratings (averaging about 16.6 ratings per user). Users’ movie ratings were used to establish users taste-similarity for the CF algorithm. For the method that is based on additional relationship data, we employed the survey data regarding users’ perceptions of competence, benevolence, and tie strength (frequency, duration, and closeness). Then, we adjusted the data to a [-1, 1] scale. Each user, thus, was associated with three others.

The CF algorithm was implemented based on the standard user-user approach (Resnick et al. 1994; Herlocker et al. 2004), where taste-similarity was based on Pearson Correlation for users’ rating vectors. Each recipient was associated with a set of close sources using K-Nearest Neighbor algorithm. For the social-data-enhanced method, we used the following formula:

$$
p (a, i) = \bar {r} _ {a} + \frac {\sum_ {u \in R ^ {+}} \left(0 . 4 * w _ {a , u} + 0 . 6 * t _ {a , u}\right) * \left(r _ {u , i} - \bar {r} _ {u}\right)}{\sum_ {u \in R ^ {+}} w _ {a , u}}
$$

where recipient-source similarity is calculated as a weighted average of the profile similarity $( w _ { a , u } )$ and the social similarity $( t _ { a , u } )$ . We explored various weighting schemes, attained optimal results when using 40/60 weighting, and applied this scheme for our experiments. In order to explore the impact of various social relationships, we tested the system several times, each time calculating social similarity $t _ { a , u }$ based on an alternative type of relationship indicator.<sup>15</sup> Similar to CF, each recipient was then associated with close sources using K-Nearest Neighbor algorithm.

In order to assure the robustness of the results, we performed a 10-fold re-sampled paired t-test (Dietterich, 1998), where in each of the 10 simulations, we randomly divided the available sample into a training set R and a test set T. The algorithms we studied – both the baseline CF and the methods that employ additional relationship indicators – are trained on R and then tested on T. We randomly divided our user ratings dataset: 80 percent of the ratings were employed as a training set (used to create users’ profiles) and the remaining 20 percent as a test set. Based on users’ profiles in the training set, the recommendation algorithms made predictions for items in the testing set.<sup>16</sup> Our measure of system performance was based on the prediction error, i.e., the difference between the system’s prediction and a user’s actual rating. We employed the well-accepted Root Mean Squared Error (RMSE) metric, which emphasizes larger errors (Herlocker at al., 2004; Victor et al., 2010). Even small RMSE improvements are considered valuable in the context of recommender systems. For example the Netflix prize competition<sup>17</sup> offered a one million dollar reward for an RMSE reduction of 10 percent.

We report on the combined results of all 10 simulations. For the social-data-enhanced method, over these 10 simulations, there were 217 cases where social relationships were employed in the prediction $( \mathsf { i . e . , } ^ { t _ { a , u } } > 0 )$ , while in the rest of the cases, we fell back on traditional CF. Since our interest was in evaluating the value of using social relationship information (as compared to traditiona CF), we base the analysis of results on these 217 cases.

## 7.2 Recommender System Evaluation

Table 7 reports on the system evaluation results (please note that reduction in RMSE is desired).

<table><tr><td colspan="3">Table 7: RMSE results for various methods of calculating recipient-source similarity</td></tr><tr><td>Method for Measuring User Similarity</td><td>RMSE</td><td>Changes from CF</td></tr><tr><td>CF</td><td>1.244</td><td></td></tr><tr><td>CF + Tie Strength Frequency</td><td>1.277</td><td>(+0.033; 3%)</td></tr><tr><td>CF + Tie Strength Duration</td><td>1.266</td><td>(+0.022; 2%)</td></tr><tr><td>CF + Tie Strength Closeness</td><td>1.248</td><td>(+0.004; 0%)</td></tr><tr><td>CF + Competence-Based Trustworthiness</td><td>1.179</td><td>(-0.066; 5%;)</td></tr><tr><td>CF + Benevolence-Based Trustworthiness</td><td>1.165</td><td>(-0.079; 6%;)</td></tr></table>

Simulation results demonstrate that alternative types of social relationship data impact recommender system accuracy differently. While some relationships (namely competence and benevolence-based trustworthiness) enhance accuracy, other relationships (i.e., interaction duration and frequency) add noise and impede system performance.

## 8. Discussion

The primary contribution of this paper is in proposing a theory-driven design methodology, which extends extant conceptualizations. Existing approaches to scientific design (i.e., design science research) overlook to a large extent the potential role of behavioral theory in design (Nunamaker et al., 1991; March and Smith, 1995; Gregg et al., 2001; Hevner et al., 2004; Gregor and Jones, 2007; March and Storey, 2008). The Walls et al. IS design theory (ISDT; 1992, 2004) does acknowledge the importance of behavioral theories (referred to as kernel theories). However, the gap between these kernel theories and the design problem is difficult to bridge, primarily due to incompatibility in terms of scope and granularity. We have proposed an extension to the ISDT by introducing an intermediate component – applied theoretical model – between kernel theories and system design. This applied model is articulated as a behavioral framework, but corresponds directly to the design problem, such that the choice of constructs and their granularity are informed by the design problem. In addition, we extend the ISDT by proposing new paths among components of the framework, suggesting that the transition between theory and design is reciprocal and ongoing, in contrast to the linear process described in the ISDT. We have described our experience in applying our proposed framework in the context of social recommender systems and articulated guidelines to help apply our approach to other design problems.

The most striking finding from our investigation of theory-driven design in the context of social recommender systems is the high correspondence between the theoretical predictions from the newly introduced applied theoretical framework and the results from system testing. A comparison of the findings from the simplified one-stage applied theoretical model (see Section 5.4) and the recommender system simulation results (see Section 7.2), strongly demonstrates that advice-taking theory can, indeed, be used to direct social recommender system design. First, in our simplified applied model, homophily alone was able to explain a large portion of WAA’s variance, and similarly, the profile-similarity-based CF algorithm yielded good performance. Second, the simplified theoretica model suggests that, given homophily as a baseline, the addition of competence and benevolence has the largest impact (in terms of $R ^ { 2 }$ enhancements) on the recipient’s WAA. The very same relationship types also provided the best system performance (in terms of RMSE) when added on top of CF’s profile similarity, confirming propositions TDP2a-b. Closeness, which had a moderate impact on recipient’s WAA in the applied theoretical model, proved as accurate as the baseline in our evaluation of the SRS, thus, we found no support for proposition TDP2c. Third, frequency and duration proved insignificant in the simplified theoretical model, and these same relationships also proved ineffective in the recommender system, confirming propositions TDP2d-e. Hence, an important contribution of this study is the establishment of a link between advice-taking theory and recommender system design.

The intricate multi-stage applied theoretical model (see Section 5.1) could be useful in directing design in cases when multiple relationship indicators are available. Recent studies illustrate the ability to mine multiple sources of online relationship data (Guy et al., 2009), e.g., both social networks and communication logs. For these cases, an applied path model, which represents the various links connecting the constructs, could be useful for a system designer in considering which type of relationship data to employ. The findings from the evaluation of the applied theoretical model, as well as their design implications, are discussed below.

We found that cognitive homophily plays an important role in facilitating the formation of social ties. Cognitive homophily plays an important role in the participant’s willingness to accept advice, both directly as well as through a set of mediating influences – tie strength and trustworthiness beliefs. We discuss below some specific theory-based design guidelines based on this path model.

The prominence of cognitive homophily provides a theoretical grounding for the collaborative recommendation method (e.g., Shardanand and Maes, 1995), suggesting that shared-preference data should be used as the primary source for source selection, and that it should be preferred over tie strength and trustworthiness data. We also found that tie closeness and trustworthiness beliefs have a significant positive impact on advice-taking decisions, suggesting that in some cases (e.g., when shared-preference data is incomplete)

social network data can serve as a proxy for preference similarity. This conclusion is supported by empirical studies that demonstrate how online community members create ties of friendship and trust primarily with persons who have similar preferences (Abdul-Rahman and Hailes, 2000; Ziegler and Lausen, 2004). While our results show that competence, benevolence, and closeness positively influenced willingness to accept advice, we found that the effect of competence (0.31) on the outcome variable is larger than the effects of benevolence (0.16) and closeness (0.20), implying that competence-based networks (social networks based on domain expertise, e.g., ePinions) are a better source of data for SRS than benevolence-based social networks (networks based on friendship, e.g., Facebook). In addition, our findings suggest that the role of tie strength’s time dimensions – duration and frequency – is not substantial: they have minor positive indirect effects and insignificant direct negative effects on recipients’ willingness to accept advice. We suspect that the insignificance of the negative effects stems from the small sample size, and that with a larger sample we should be able to observe the strength of weak ties (Granovetter, 1973).

In addition to the set of design propositions regarding the accuracy improvements due to social data (TDP2a-e), we have articulated a set of propositions regarding efficiency and privacy (TDP1a-e) that were not tested in our study. While a full discussion of these issues is beyond the scope of this paper, we would like to note that using consumption profiles for calculating shared preferences requires the least effort and poses minimum risks to privacy. Thus – from a practical perspective – the traditional CF approach is more desirable than using alternative sources of relationship data. For a more comprehensive discussion of these issues, please refer to Arazy et al., 2009.

Finally, our proposed applied model makes theoretical contributions to the study of advice taking, which goes beyond its relevance for directing recommender system design. Specifically, we contribute to research in both marketing and social networks. The word-of-mouth marketing literature has been primarily concerned with the effects of cognitive homophily and trustworthiness on the advice-taking process (Gilly et al., 1998; Smith et al., 2005), and we contribute to that literature by demonstrating how different dimensions of tie strength mediate the relationship between cognitive homophily and trustworthiness. The social networks literature, on the other hand, discusses the impact of tie strength and trustworthiness on the recipient’s advice-taking process (Levin and Cross, 2004; Ghoshal et al., 1994). Our findings add to that literature by demonstrating that cognitive homophily has a direct impact on the willingness to accept advice, beyond its indirect effect (mediated by tie strength and trustworthiness). Another important theoretical contribution is the decomposition of tie strength into its various dimensions. While prior studies of advice taking have considered tie strength as a onedimensional construct (e.g., Levin and Cross, 2004; de Bruyn and Lilien, 2008), our results demonstrate that the various dimensions of tie strength should be treated as distinct constructs. These novel conceptualizations should serve to inform behavioral theories of advice taking.

## 9. Conclusion

Recommender systems play an important role in the online environment, and data regarding the social relationships of users is essential for delivering relevant information to recipients. In recent years, a number of different social recommender system designs have been proposed, utilizing alternative types of relationship data. Moreover, it is now feasible to automatically extract meaningful relationships from various online sources (Guy et al., 2009). Despite the promise of these new approaches, to date they have failed to provide consistent accuracy improvements. The use of additional relationship data has been rather ad-hoc, where system design choices are divorced from behavioral theory. We argue that under-specification of the social relationship types is the cause – at least to some extent – for the inability of existing SRS to provide substantial accuracy improvements. Existing kernel theories are limited in guiding the design of social recommender systems for two primary reasons: (1) Research on advice taking is fragmented into various research strands, and each strand focuses on only a partial set of factors that are important for SRS (i.e., the problem of scope), and (2) The granularity at which constructs are studied in the existing theoretical models is too coarse for guiding SRS design. In this paper, we take a first step toward filling this gap. We introduce an applied theoretical framework of the relationship factors that determine willingness to accept advice that is tailored for guiding SRS design, and provide an initial test of the model. We then design, develop, and test a SRS. We find that the results of the applied theoretical model regarding the types of relationships that are most valuable for advice taking, indeed, predict the relationship types that will enhance SRS accuracy, demonstrating the suitability of the proposed applied theory for directing SRS design.

While design science research presents a large opportunity to increase the relevance of IS research, it often lacks appropriate theoretical grounding (Goldkuhl, 2004). Despite the potential use of theory for grounding design, most design science works do not rely on theoretical foundations from the natural or social sciences. This is largely due to the mismatch between the nature of kernel theories and the requirements of the design problem. This has led several design science scholars to question the possibility of theory-driven design. Iivari (2002) questions the possibility of “any theorizing that is able to link IS meta-artifacts and descriptive-explanatory theories” (p. 577), and Ling et al. (2005) state that it is not clear “whether relevant theories can be parameterized sufficiently to guide designers.” Our proposed approach to theory-driven design extends the Walls et al. (1992, 2004) ISDT framework by incorporating the notion of an applied theoretical model. Our novel conceptualization is intended to allow for a more straightforward move from kernel theory to design principles, demonstrating that theoretically grounded design may be feasible after all. That being said, we do recognize that such an approach may not suit all design problems, and our understanding of when such theory-driven design is possible is still in its infancy (Hooker, 2004; Ling et al., 2005).

Although this study enhances our understanding of the factors determining the willingness to accept advice and the relationship data that is important for SRS, several issues warrant further research. In terms of SRS design, the experiments reported here were only intended to provide a proof of concept for theory-driven SRS design. Future studies could expand on these preliminary experiments in various ways, e.g., explore the combination of multiple relationship indicators simultaneously, develop alternative methods for combining the various relationship data, and investigate performance in special cases (e.g., cold start, controversial items).

In terms of the applied theoretical model, in the future we would like to conduct a more comprehensive evaluation of the proposed model. First, we modeled our methodology after Marsden and Campbell (1984), asked recipients to choose three sources from whom they would like to receive advice, and, thus, over-sampled relationships from the “strong” end of the continuum. We do not think that the limitation is severe, as it permitted statistically significant correlations to emerge; if there were greater variability, correlations among measures could be expected to be larger. Second, as a result of decomposing tie-strength into three distinct constructs, we measured each of these constructs using a single-item scale. However, we do not perceive this as a serious concern to measurement reliability, since interaction frequency and tie duration are objective measures. Moreover, correlations with single item scales likely underestimate the correlation that would have been observed with multiitem scales, thus, our findings serve as a lower bounds to the true correlations. Third, the study used university students as participants, and the results generalize to this target population. While students are an important segment of the social network user population and are appropriate for the context of this study, care should be exercised in interpreting our results across the board. Fourth, our study was conducted in only one domain – movie recommendations – and in the future we plan to test the applied theoretical model in other domains. In principle, our model could be applied to various online recommendation tasks, e.g., file sharing or music downloads. However, the factors affecting source selection may differ across task domains. For example, it is possible that for utilitarian tasks, recipients tend to rely more on a source’s domain expertise (Feick and Higie, 1992; Smith et al., 2005), while in hedonic tasks cognitive homophily plays a more central role. Finally, our study was conducted in an offline setting, while recommender systems are often used over the Internet. Nonetheless, relationships in an online setting are essentially similar to offline relationships (Wellman, 1997), especially when many of the ties included in online social networks are with people who we know from face-to-face interactions (Wellman, 2001). Thus, we expect that our findings will persist in online settings.

We conclude with a call to behavioral and design researchers to join arms in developing theoretical models that are suitable for directing information systems design. Collaboration applications, such as SRS, are socio-technical systems, where people and computers work together. Thus, the design of these systems should pay as much attention to an understanding of human behavior as it pays to technical considerations. As the lines between users and designers begin to blur (e.g., open source software development) and users tailor products to their own needs, there is a need for an even deeper consideration of human facets. In recent years, proponents of design science (Hevner et al., 2004) have stressed the need for rigor in the design process, but their focus was primarily on the technical and procedural aspects. While some IS designers have considered human cognition and social interaction in their design, typically, they used behavioral theory only to inform design at an intuitive level. In line with early works in HCI (Newell and Card, 1985), we argue that behavioral theory should be given a central role in guiding design, and that design science methodologies should provide structure for incorporating theoretical considerations. Walls et al. (2004), in a retrospective of their original conceptualization, have identified different possible applications and extensions to the ISDT, and at the highest level “the richness of ISDT itself is enhanced through usage as scholars discover gaps and omissions and improvements that can be made to ISDT that are revealed by working through it in their own context. At that level, double loop learning from ISDT occurs and advances in theory building methodologies are made” (p. 56). This precisely has been the aim of our study. We followed up on Walls et al.’s suggestion (2004) to enhance the ISDT “through richer interactions between the components, or standard modularization with inter-changeability, or other creative additions” (p. 56). We hope that our re-conceptualization of the theory-driven design framework opens the door for further work on this exciting area.

## Acknowledgements

We thank Ibrahim Sana for his work on this project. The authors also thank the JAIS Senior Editor an d anonymous reviewers for very constructive comments on earlier drafts of this paper. This research was funded in part by the Canadian Social Sciences and Humanities Research Council (SSHRC) and by PSC-CUNY.

## References

Abdul-Rahman, A. and Hailes, S. (2000). “Support Trust in Virtual Communities.” Proceedings of the 33rd Hawaii International on System Science. Maui, Hawaii, USA, 1769–1777.

Adomavicius, G. and Tuzhilin, A. (2005). “Toward the Next Generation of Recommender Systems: A Survey of the State-of-the-Art and Possible Extensions.” IEEE Transactions on Knowledge and Data Engineering; 17(6), 734–749.

Allen, T. (1977). Managing the Flow of Technology, MIT Press, Cambridge, MA.

Arazy, O., Elsane, I., Shapira, B., and Kumar, N. (2007). “Social Relationships in Recommender Systems.” Proceeding of the 17<sup>th</sup> Workshop on Information Technologies & Systems (WITS’07), Montreal, Canada.

Arazy, O., Kumar N., and Shapira, B. (2009). “Improving Social Recommender Systems.” IEEE IT Professional, May/June 2009, 31-37.

Arazy, O., and Woo, C. (2007). “Enhancing Information Retrieval through Statistical Natural Language Processing: A Study of Collocation Indexing.” Management Information Systems Quarterly (MISQ), 31(3), 525-546.

Aristotle (1934). Rhetoric. Nichomachean ethics, Aristotle in 23 Volumes, Translated by Rackman, Harvard University Press.

Arndt, J. (1967). Word of Mouth Advertising: A Review of the Literature. Advertising Research Federation, New York.

Avesani, P., Massa, P., and Tiella, R. (2005). “Moleskiing.it: a Trust-Aware Recommender System for Ski Mountaineering.” International Journal for Infonomics, September 2005, 1-10.

Bansal, H.S. and Voyer P.A. (2000). "Word-of-Mouth Processes within a Services Purchase Decision Context." Journal of Service Research, 3(2),166-177.

Berger, C.R., and Calabrese, R.J. (1975). “Some Explorations in Initial Interaction and Beyond: Toward a Developmental Theory of Interpersonal Communication.” Human Communication Research, 1, 99-112.

Berscheid, E., and Walster, E. (1978). Interpersonal Attraction (2nd ed.), Addison-Wesley, Reading, MA.

Bonhard, P. and Sasse, M.A. (2006). “’Knowing Me, Knowing You' - Using Profiles and Social Networking to Improve Recommender Systems.” BT Technology Journal, 24(3), 84-98.

Brickman, P., Meyer, P., and Fredd, S. (1975). “Effects of Varying Exposure to Another Person with Familiar or Unfamiliar Thought Processes.” Journal of Experimental Social Psychology, 11(2), 61-70.

Briggs, P., Burford, B., De Angeli, A., and Lynch, P. (2002). “Trust in Online Advice,” Social Science Computer Review, 20(3), 321-332.

Brislin, R.W., Lonner, W.J., and Thorndike, R.M. (1973). Cross-cultural Research Methods, John Wiley and Sons, New York, NY.

Bristor, J.M. (1990). “Enhanced Explanations of Word of Mouth Communications: The Power of Relationships.” Research in Consumer Behavior, 4, 51-83.

Brown, J.J. and Reingen, P.H. (1987). "Social Ties and Word-of-Mouth Referral Behavior." Journal of Consumer Research, 14(3), 350-62.

Burt, R., and Knez, M. (1996). “Trust and Third-Party Gossip,” in Trust in Organizations: Frontiers of Theory and Research, in Kramer R.M. and Tyler T.R. (eds.), Sage Publications, Thousand Oaks, CA, 68–89.

Byrne, D., Griffitt, W. and Stefaniak, D. (1967). “Attraction and Similarity of Personality Characteristics.” J. of Personality and Social Psych., 5, 82-90.

Card, S., Moran, T. P., and Newell, A. (1983). The psychology of Human-Computer Interaction. Hillsdale, NJ: Lawrence Erlbaum Associates, Inc.

Carley, K. (1991). “A Theory of Group Stability,” American Sociological Review, 56(3), 331–354.

Carroll, J. M., and Kellogg, W. A. (1989). “Artifact as Theory-Nexus: Hermeneutics Meets Theory-Based Design.” Proceedings of the SIGCHI Conference on Human Factors in Computing Systems: March 1989, 7-14.

Chang M.K. and Woo C. (1994). “A Speech Act Based Negotiation Protocol: Design, Implementation and Test Use.” ACM Transactions on Information Systems, 12(4), 360-38.

Chin, W.W., and Newsted, P.R. (1999). “Structural Equation Modeling Analysis with Small Samples Using Partial Least Squares.” in Hoyle R.H. (eds.), Statistical Strategies for Small Sample Research, Thousand Oaks, CA: Sage, 307-341.

Constant, D. Sproull, L.,and Kiesler, S. (1996). “The Kindness of Strangers: The Usefulness of Electronic Weak Ties for Technical Advice.” Organization Science, 7(2), 119–135.

Cross, R., and Sproull, L. (2004). “More Than an Answer: Information Relationships for Actionable Knowledge.” Organization Science, 15(4), 446–462.

Currall, S., and Judge, T. (1995). “Measuring Trust Between Organizational Boundary Role Persons.” Organization Behavior Human Decision Processes, 64(2), 151–170.

Dabbish, L. and Kraut, R. (2008). “Awareness Displays and Social Motivation for Coordinating Communication.” Information Sys. Research,19(2), 221-238.

de Bruyn, A. and Lilien, G.L. (2008). “A Multi-Stage Model of Word of Mouth Through Electronic Referrals." International Journal of Research in Marketing 25(3), 151-163.

Dietterich, T.G. (1998). “Approximate Statistical Tests for Comparing Supervised Classification Learning Algorithm, Neural Computation, 10(7), 1895-1924.

Dirks, K.T., and Ferrin, D.L. (2001). “The Role of Trust in Organizational Settings.” Organization Science, 12(4), 450–467.

Feick, L., and Higie, R.A. (1992). “The Effects of Preference Heterogeneity and Source Feick, L., and Higie, R.A. (1992). “The Effects of Preference Heterogeneity and Source

Characteristics on Ad Processing and Judgments about Endorsers.” Journal of Advertising, 21(2), 9–24.

Fornell, C., and Cha, J. (1994). “Partial Least Squares.” in Bagozzi (ed.), Advanced Methods of Marketing Research, Cambridge, MA: Blackwell, 52-78.

Fornell, C., and Larcker, D.F. (1981). “Evaluating Structural Equation Models with Unobservable Variables and Measurement Error.” Journal of Marketing Research, 18(1), 39-50.

Galegher, J., Kraut, R.E., and Egido, C. (eds.) (1990). Intellectual Teamwork: Social and Technological Basis for Cooperative Work, Hillsdale, NJ: Lawrence Erlbaum Associates.

Ghoshal, S., Korine, H., and Szulanski, G. (1994). “Interunit Communication in Multinational Corporations.” Management Science, 40(1), 96–110.

Gibbons, D.E. (2004). “Friendship and Advice Networks in the Context of Changing Professional Values.” Administrative Science Quarterly, 46(2), 238-262.

Gilly, M.C., Graham, J.L., Wolfinbarger, M.F., and Yale, L.J. (1998). "A Dyadic Study of Interpersona Information Search." Journal of the Academy of Marketing Science, 26(2), 83-100.

Glaeser, E.L., Laibson, D.I., Scheinkman, J.A., and Soutter, C.L. (2000). “Measuring Trust.” Quarterly Journal of Economics, 115(3), 811–846.

Golbeck, J. and Hendler, J. (2006). “FilmTrust: Movie Recommendations Using Trust in Web-Based Social Networks.” Proceedings of the IEEE Consumer Communications and Networking Conference, 282–286.

Golbeck, J. (2006). “Generating Predictive Movie Ratings from Trust in Social Networks.” Lecture Notes in Computer Science, 3986, 93-104.

Goldberg, D., Nichols, D., Oki, B., and Terry, D. (1992). “Using Collaborative Filtering to Weave an Information Tapestry.” CACM, 35(2), 61-70.

Goldkuhl, G. (2004). “Design Theories in Information Systems – a Need for Multi-Grounding.” J. of Information Tech. Theory and Application, 6(2), 59-72.

Granovetter, M., “The Strength of Weak Ties,” American Journal of Sociology, 78(6), 1360–1380.

Granovetter, M. (1982). “The Strength of Weak Ties: A Network Theory Revisited.” in Marsden P.V. and Lin N. (eds.), Social Structure and Network Analysis, Beverly Hills, CA: Sage. 105- 130.

Gregg, D., Kulkarni, U. and Vinze, A. (2001). "Understanding the Philosophical Underpinnings of Software Engineering Research in Information Systems." Information Systems Frontiers, 3(2), 169-183.

Gregor, S. and Jones, D. (2007). “The Anatomy of a Design Theory.” Journal of the Association for Information Systems, 8(5), 312-335.

Groh, G., and Ehmig, C. (2007). “Recommendations in Taste Related Domains: Collaborative Filtering vs. Social Filtering”, Proceedings of GROUP’07, 127-136.

Guha, R, Kumar, R., Prabhakar, R., and Tomkins, A. (2004). “Propagation of Trust and Distrust.” Proceedings of the 13th Conference on World Wide Web, 17-20 May 2004, New York, NY, USA, 403-412.

Guy, I., Zwerdling, N., Carmel, D., Ronen, I., Uziel, E., Yogev, S., and Ofek-Koifman, S. (2009). “Personalized Recommendation of Social Software Items Based on Social Relations.” Proceedings of The 3rd ACM Conference on Recommender Systems, New York, NY, USA, October 22-25, 2009.

Hansen, M.T. (1999). “The Search-Transfer Problem: The Role of Weak Ties in Sharing Knowledge Across Organization Subunits,” Administrative Science Quarterly, 44(1), 82–111.

Haythornthwaite, C. (2001). “The Strength and the Impact of New Media.” Proceedings of the 34th Annual Hawaii International Conference, 3-6 January 2001.

Herlocker, J.L., Konstan, J.A., Terveen, L.G., and Riedl, J.T. (2004). “Evaluating Collaborative Filtering Recommender Systems”, ACM Transactions on Information Systems, 22(1), 5–53.

Hevner, A., March, S., Park, J. and Ram, S. (2004). "Design Science in Information Systems Research." MIS Quarterly, 28(1), 75-105.

Hooker, J.N. (2004). “Is Design Theory Possible?” Journal of Information Technology Theory and Application (JITTA), 6(2), 63-72.

Huston, T.L., Levinger, G. (1978). “Interpersonal Attraction and Relationships.” Annual Review of Psychology, 29(1), 15–56.

Ibarra, H. (1992). “Homophily and Differential Returns: Sex Differences in Network Structure and Access in an Advertising Firm.” Administrative Science Quarterly, 37(3), 422–447.

Iivari J. (2002). “Towards Information Systems as a Science of Meta-Artifacts.” Communications of the Association for Information Systems,12(37), 568-581.

Johnson, D.W. and Johnson, S. (1972). “The Effects of Attitude Similarity, Expectation of Goal Facilitation, and Actual Goal Facilitation on Interpersonal Attraction.” Experimental Social Psychology, 8(3), 197-206.

Karahanna, E., Evaristo, R., and Srite, M., (2002). “Methodological Issues in MIS Cross-Cultural Research.” J. of Global Info. Management, 10(1), 48-55.

Kautz, H., Selman, B., and Shah, M. 1(997). “ReferralWeb: Combining Social Networks and Collaborative Filtering. CACM, 40(3), 63-65.

Konstan J. (2004). “Introduction to Recommender Systems: Algorithms and Evaluation.” ACM Transactions on Information Systems, 22(1), 1–4.

Kraut, R.E. (2003). “Applying Social Psychological Theory to the Problems of Group Work.” In Carroll J. (ed.), HCI Models, Theories and Frameworks: Toward A Multidisciplinary Science, New York: Morgan Kaufman, 325-356.

Kuechler, W., Vaishnavi, V., and Kuechler W.L. (2007). “Design [Science] Research in IS: A Work in Progress.” Proceedings of 2nd International Conference on Design Science Research (DESRIST '07), May 13-16, 2007, Pasedena, CA.

Lazarsfeld, P.F. and Merton, R.K. (1954). “Friendship as A Social Process: A Substantive and Methodological Analysis.” In Berger M. (eds.), Freedom and Control in Modern Society, Van Nostrand, New York, 18–66.

Lee, F. (1997). “When the Going Gets Tough, Do the Tough Ask for Help? Help Seeking and Power Motivation in Organizations.” Organizational Behavior and Human Decision Processes, 72(3), 336–363.

Levin, D. and Cross, R. (2004). “The Strength of Weak Ties You Can Trust: The Mediating Role of Trust in Effective Knowledge Transfer,” Management Science, 50(11), 1477–1490.

Lerman, K. (2007). “Social networks and social information filtering on Digg”, Proceedings of the International Conference on Weblogs and Social Media (ICWSM 2007), March 26-28, 2007, Boulder, Colorado, USA.

Lincoln, J.R. and Miller J. (1979). “Work and Friendship Ties in Organizations: A Comparative Analysis of Relational Networks, Administrative Science Quarterly, 24(2), 181–199.

Linden, G., Smith, B., and York, J. (2003). “Recommendations: Item-to-Item Collaborative Filtering.” IEEE Data Engineering Bulletin, 76-80.

Ling, K., Beenen, G., Ludford, P., Wang, X., Chang, K., Li, X., Cosley, D., Frankowski, D., Terveen, L., Rashid, A.M., Resnick, P., and Kraut, R. (2005). “Using Social Psychology to Motivate Contributions to Online Communities.” Journal of Computer-Mediated Communication, 10(4).

Ma, H.K. (1985).“Cross-Cultural Study of the Hierarchical Structure of Human Relationships.” Psychological Reports, 57(3), 1079–1083.

Malone, T.W. (1985). “Designing Organizational Interfaces.” Proceedings of Human.Factors in Computing Systems (CHI '85), 66-71. New. York: ACM.

March, S.T. and Storey V.C. (2008). “Design Science in the Information Systems Discipline.” MIS Quarterly, 32(4), 725-730.

March, S.T. and Smith, G.F. (1995). “Design and Natural Science Research on Information Technology.” Decision Support Systems, 15(4), 251-266.

Marcoulides, G.A., Chin W.W., and Sounders, C., 2009, A Critical Look at Partial Least Squares Modeling, MIS Quarterly, 33(1), 171-175.

Markus, L., Majchrzak, A. and Gasser, L. (2002). “A Design Theory for Systems that Support Emergent Knowledge Processes.” MIS Quarterly, 26(3), 179-212.

Marsden, P. and Campbell, K. (1984). “Measuring Tie Strength,” Social Forces, 63(2), 482–501.

Massa, P. and Avesani, P. (2004). “Trust-Aware Collaborative Filtering for Recommender Systems, Proceedings of International Conference on Cooperative Information Systems. Agia Napa, Cyprus

Mathews, K.M., White, M.C., Long, R.G., Soper, B. and Von Bergen, C.W. (1998). "An Analysis of the Relationship Between Indicators and Predictors of Tie Strength," Psychological Reports, 83(2), 1459-1470.

Mayer, R.C., Davis, J.H., and Schoorman, F.D. (1995). “An Integrative Model of Organizational Trust.” Academy of Management Review, 20(3), 709-734.

McAllister, D.J. (1995). “Affect- and Cognition-Based Trust as Foundations for Interpersonal Cooperation in Organizations.” Acad. Manage. J., 38(1), 24-59.

McKnight, D.H., Choudhury, V., and Kacmar, C. (2002). “Developing and Validating Trust Measures for e-Commerce: An Integrative Typology.” Information Systems Research, 13(3), 334–359.

McPherson, M., Smith-Lovin, L., and Cook J.M. (2001). “Birds of a Feather: Homophily in Social Networks.” Annual Review of Sociology, 27(1), 415-444.

Mintzberg, H. (1973). The Nature of Managerial Work, Harper Row, New York.

Money, R.B, Gilly, M.C., and Graham, J.L. (1998). “Explorations of National Culture and Word-of-Mouth Referral Behavior in the Purchase of Industrial Services in the United States and Japan,” Journal of Marketing, 62(4), 76-87.

Newell, A. and Card, S.K. (1985). “The prospects for psychological science in human-computer interaction.” Human-Computer Interaction, 1(3), 209-242.

Nunamaker, J.F., Chen, M., and Purdin, T. (1991). “Systems Development in Information Systems Research.” Journal of Management Information Systems, 7(3), 89-106.

Orlikowski, W. and Barley, S. (2001). “Technology and Institutions: What can Research on Information Technology and Research on Organizations Learn from Each Other?” MIS Quarterly, 25(2), 145-165.

Pelz, D.C. and Andrews, F.M. (1966). “Scientists in Organizations: Productive Climates for Research and Development. John Wiley and Sons, New York.

Petroczi, A., Nepusz, T. and Bazsó, F. (2006). “Measuring Tie-Strength in Virtual Social Networks, Connections, 27(2), 49-57.

Plato. (1968). Laws. Plato in Twelve Volumes, Vol. 11. translated by Bury. Harvard University Press.

Pries-Heje, J. and Baskerville, R. (2008). “The Design Theory Nexus.” MIS Quarterly, 32(4), 731-755.

Reagans, R. (2005). “Preferences, Identity, and Competition: Predicting Tie Strength from Demographic Data.” Management Science, 51(9), 1374-1383.

Resnick, P. and Varian, H. (1997). “Recommender Systems.” CACM, 40(3), 56-58.

Rogers, E., (1995). Diffusion of Innovations (4th Ed). Free Press, New York.

Rulke, D.L. and Rau, D. (2000). “Investigating the Encoding Process of Transactive Memory Development in Group Training.” Group and Organization Management, 25(4), 373–396.

Shneiderman, B. (1998). Designing the User Interface: Strategies for Effective Human-Computer Interaction, Reading, MA: Addison-Wesley.

Sinha, R. and Swearingen, K. (2001). “Comparing Recommendations Made by Online Systems and Friends.” Proceedings of the DELOS-NSF Workshop on Personalization and Recommender Systems in Digital Libraries.

Smith, D., Menon, S., and Sivakumar, K. (2005). “Online Peer and Editorial Recommendations, Trust, and Choices in Virtual Markets.” Journal of Interactive Marketing, 19(3), 15-37.

Sole, L., Martin, J., and Hornstein, H.A. (1975). “Opinion Similarity in Helping. Three Field Experiments Investigating the Bases of Promotive Tension,” Experimental Social Psychology, 11(1), 1-13.

Stapleton, R.E., Nacci, P., and Tedeschi, J.T. (1973). “Interpersonal Attraction and the Reciprocation of Benefits.” J. Person & Soc. Psychol., 28, 199-205.

Szulanski, G. (1996). “Exploring Internal Stickiness: Impediments to the Transfer of Best Practice within the Firm.” Strategic Management Journal, 17(2), 27-43.

Tenenhaus, M., Vinzi, V.E., Chatelin, Y.M. and Lauro, C. (2005). “PLS Path Modeling,” Computational Statistics and Data Analysis, 48(1), 159-205.

Tsai, W., and Ghoshal, S. (1998).“Social Capital and Value Creation: The Role of Intrafirm Networks.” Academy of Management Journal, 41(4), 464-476.

Venable, J. (2006) “The Role of Theory and Theorizing in Design Science Research.” Proceedings of the 1<sup>st</sup> Inter. Conf. on Design Science Research in Information Systems and Technology, Claremont, CA, 1-18.

Verbrugge, L.M. (1997). “The Structure of Adult Friendship Choices.” Social Forces, 56(2), 576-597.

Victor, P., Cornelis, C., De Cock, M., and Teredesai, A.M. (2008). “Key Figure Impact in Trust-Enhanced Recommender Systems.” AI Communications, 21(2-3), 127-143.

Victor, P., De Cock, M., and Cornelis, C. (2010). “Trust and Recommendations.” in Kantor, P.B., Ricci, F., Rokach, L., and Shapira, B. (eds.), Recommender Systems Handbook, Springer.

Walls, J.G., Widmeyer, G.R., and El Sawy, O.A. (1992). "Building an Information System Design Theory for Vigilant EIS." Info. Sys. Research, 3(1), 36-59.

Walls, J.G., Widmeyer, G.R. and El Sawy, O.A. (2004). “Assessing Information System Design Theory in Perspective.” J. of Information Technology Theory and Application, 6(3), 43-58.

Wand, Y. and Weber, R. (2006) “On Ontological Foundations of Conceptual Modeling”, Scandinavian Journal of Information Systems, 18(1), 127-138.

Wellman, B. (1997). “An Electronic Group is Virtually a Social Network.” in Kiesler, S. (ed), Culture of the Internet, Lawrence Erlbaum, 179–205.

Wellman, B. (2001).“Computer Networks as Social Networks.” Science, 293(5537), 2031-2034.

Yaniv, I. (2004). "Receiving Other Peoples' Advice: Influence and Benefit." Organizational Behavior and Human Decision Processes, 93(1), 1-13.

Zaheer, A., McEvily, B., and Perrone, V. (1998). “Exploring the Effects of Interorganizational and Interpersonal Trust on Performance,” Organization Science, 9(2), 141–159.

Zheng, R., Provost F., and Ghose A. (2007). “Social Network Collaborative Filtering: Preliminary Results.” Proceedings of the $\dot { \boldsymbol { 6 } } ^ { t h }$ Workshop on e-Business (WeB), Montreal, Canada.

Ziegler, C.N. and Lausen, G. (2004). “Analyzing Correlation Between Trust and User Similarity in Online Communities.” Proceedings of the ${ \dot { 2 } } ^ { n d }$ International Conference on Trust Management, Oxford, UK, LNCS, 2995, 251–265.

Appendix A. Operationalization of Constructs and Original Items List

<table><tr><td>Construct</td><td>Items</td><td>Mean (/7)</td><td>S.D</td></tr><tr><td rowspan="2">Cognitive Homophily</td><td>This person shares similar interests with me.</td><td>5.44</td><td>1.04</td></tr><tr><td>This person has similar preferences to me.</td><td>5.27</td><td>1.17</td></tr><tr><td>Tie Strength-Frequency</td><td>How often did you communicate with this person? (1 = once every 3 months or less (or never); 2= once every 2nd month; 3 = once a month; 4 = twice a month; 5 = once a week; 6 = twice a week; 7 = daily)</td><td>1.79</td><td>1.34</td></tr><tr><td>Tie Strength-Duration</td><td>How long have you known this person? (1 = less than a day; 2 = about a week; 3 = about two weeks; 4 = about a month; 5 = about three months; 6 = about a year; 7 = more than a year)</td><td>6.89</td><td>0.40</td></tr><tr><td>Tie Strength-Closeness</td><td>I feel close to this person.</td><td>5.41</td><td>1.30</td></tr><tr><td rowspan="2">Competence</td><td>Overall, this person is well informed about movies.</td><td>4.95</td><td>1.30</td></tr><tr><td>In general, this person is very knowledgeable about movies.</td><td>4.40</td><td>1.37</td></tr><tr><td rowspan="2">Benevolence</td><td>I believe that this person would act in my best interest.</td><td>5.55</td><td>1.08</td></tr><tr><td>This person is interested in my well-being, not just his/her own.</td><td>5.34</td><td>1.39</td></tr><tr><td rowspan="2">Willingness to Accept Advice</td><td>I would choose a movie to watch based on the advice I received from this person.</td><td>5.63</td><td>0.91</td></tr><tr><td>I would watch a movie recommended by this person.</td><td>5.77</td><td>0.79</td></tr><tr><td colspan="4">List of Acronyms:Average Variance Extracted - AVECollaborative Filtering - CFInformation Systems - ISInformation Systems Design Theory - ISDTPartial Least Squares - PLSSocial Recommender Systems - SRSStructural Equation Modeling - SEM</td></tr></table>

## About the Authors

Ofer Arazy is currently an Assistant Professor at the University of Alberta (Canada), Alberta School of Business. He holds a Ph.D. in Information Systems from the University of British Columbia (UBC, Canada), and B.Sc. and MBA degrees from the Technion (Israel). Ofer’s industry experience includes positions as project manager and operations manager. His research interests are in the areas of computer-supported cooperative work (CSCW) and knowledge management. His work has appeared in MIS Quarterly and JASIST among others, and has been presented in conferences such as WWW, CSCW, CHI, and WITS.

Nanda Kumar is an Associate Professor of Information Systems at Baruch College, City University of New York. He received his Ph.D. in Management Information Systems from the University of British Columbia in 2003. His current research interests include Technology Policy, Human-Computer Interaction and the Sociology of IS-enabled work. His work has been published in journals such as Information Systems Research, MIS Quarterly, Decision Support Systems and Communications of the ACM.

Bracha Shapira is currently a senior lecturer at the department of Information Systems Engineering in Ben-Gurion University of the Negev in Israel. She holds a M.Sc. in computer science from the Hebrew University in Jerusalem and a Ph.D. in Information Systems Engineering from Ben-Gurion University. Dr. Shapira’s articles have been published JASIST, DSS, IP&M and CACM among others, and her work was presented at professional conferences. Her current research interests include information retrieval and filtering and digital libraries especially user modeling and profiling for these domains. Bracha is currently leading a few research projects related to her research interests in the Deutsche-Telekom Laboratories at Ben-Gurion University.
