---
otero_id: 722
otero_key: "FWEJZ8TG"
title: "E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact1"
authors: "Bo Xiao; Izak Benbasat"
year: "2007"
journal: "MIS Quarterly"
doi: "10.2307/25148784"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
E-Commerce Product Recommendation Agents: Use, Characteristics, and Impact
Author(s): Bo Xiao and Izak Benbasat
Source: MIS Quarterly, Vol. 31, No. 1 (Mar., 2007), pp. 137-209
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/25148784
Accessed: 24-12-2015 21:23 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# E-COMMERCE PRODUCT RECOMMENDATION AGENTS: USE, CHARACTERISTICS, AND IMPACT $^{1}$

By: Bo Xiao
Sauder School of Business
University of British Columbia
2053 Main Mall
Vancouver, British Columbia V6T 1Z2
CANADA
bo.xiao@ sauder.ubc.ca

Izak Benbasat
Sauder School of Business
University of British Columbia
2053 Main Mall
Vancouver, British Columbia V6T 1Z2
CANADA
izak.benbasat@sauder.ubc.edu

## Abstract

Recommendation agents (RAs) are software agents that elicit the interests or preferences of individual consumers for products, either explicitly or implicitly, and make recommendations accordingly. RAs have the potential to support and improve the quality of the decisions consumers make when searching for and selecting products online. They can reduce the information overload facing consumers, as well as the complexity of online searches. Prior research on RAs has focused mostly on developing and evaluating different underlying algorithms that generate recommendations. This paper instead identifies other important aspects of RAs, namely RA use, RA characteristics, provider credibility, and factors related to product, user, and user–RA interaction, which influence users' decision-making processes and outcomes, as well as their evaluation of RAs. It goes beyond generalized models, such as TAM, and identifies the RA-specific features, such as RA input, process, and output design characteristics, that affect users' evaluations, including their assessments of the usefulness and ease-of-use of RA applications.

Based on a review of existing literature on e-commerce RAs, this paper develops a conceptual model with 28 propositions derived from five theoretical perspectives. The propositions help answer the two research questions: (1) How do RA use, RA characteristics, and other factors influence consumer decision making processes and outcomes? (2) How do RA use, RA characteristics, and other factors influence users' evaluations of RAs? By identifying the critical gaps between what we know and what we need to know, this paper identifies potential areas of future research for scholars. It also provides advice to information systems practitioners concerning the effective design and development of RAs.

Keywords: Product recommendation agent, electronic commerce, adoption, trust, consumer decision making

## Introduction

## Recommendation Agents Defined

Recommendation agents $^{2}$ (RAs) are software agents that elicit the interests or preferences of individual users for products, either explicitly or implicitly, and make recommendations accordingly. RAs have been used in different areas, including e-commerce, education, and organization knowledge management. In the context of e-commerce, a distinction can be made between RAs involved in product brokering (i.e., finding the best suited product) and merchant brokering (i.e., finding the best suited vendor) (Spiekermann 2001). In this paper, we focus our attention on e-commerce product brokering RAs $^{3}$ for supporting product search and evaluation.

The study of RAs falls within the domain of information systems. An information technology artifact (Benbasat and Zmud 2003), RAs are characterized as a type of customer decision support system (DSS) (Grenci and Todd 2002) based on the three essential elements of DSS proposed by Mallach (2000): (1) DSSs are information systems, (2) DSSs are used in making decisions, and (3) DSSs are used to support, not to replace, people. Similar to other types of DSS, when employing RAs, a customer provides inputs (i.e., needs and constraints concerning the product desired and/or ratings on previously consumed products) that the RAs use as criteria for searching products on the Internet and generating advice and recommendations for the customer.

RAs are distinguished from traditional DSSs by several unique features. Specifically, the users of traditional DSSs are generally managers or analysts employing the systems for assistance in tasks such as marketing planning, logistics planning, or financial planning. As such, process models $^{4}$ (which assist in projecting the future course of complex processes) (Benbasat et al. 1991; Zachary 1986) are the primary decision support technologies employed by such DSSs. In the case of RAs, in contrast, the decision makers are customers facing a class of problems called preferential choice problems (Todd and Benbasat 1994). Thus, choice models, which support the integration of decision criteria across alternatives (Benbasat et al. 1991; Zachary 1986), are the primary decision support technologies employed by RAs. RAs also exhibit similarities to knowledge-based systems (KBS) inasmuch as they need to explain their reasoning to their users so that they will trust the RAs' competence and accept their recommendations (Gregor and Benbasat 1999; Wang and Benbasat 2004a), a functionality supported by analysis and reasoning techniques (Benbasat et al. 1991; Zachary 1986). Additionally, RAs are designed to understand the individual needs of particular users (customers) that they serve. Users' beliefs about the degree to which the RAs understand them and are personalized for them are key factors in RA adoption (Komiak and Benbasat 2006). Moreover, there is an agency relationship between the RAs and their users; users (principals) cannot be certain whether RAs are working solely for them or, alternatively, for the merchants or manufacturers that have made them available for use. Therefore, users may be concerned about the integrity and benevolence of the RAs, beliefs that have been studied in association with trust in IT adoption models (Wang and Benbasat 2005).

## Motivation, Scope, and Contribution

Due to the rapid growth of e-commerce, consumer purchase decisions are increasingly made in an online environment. As forecasted by Forrester research, $^{5}$ online retail will reach \$331 billion by 2010. The growing population of online shopping households combined with retailer innovations and site improvements will drive e-commerce to account for 13 percent of total retail sales in 2010, up from 7 percent in 2004. Between 2004 and 2010, online sales will grow at a 15 percent compound annual growth rate. Digital marketplaces offer consumers great convenience, immense product choice, and a significant amount of product-related information. However, as a result of the cognitive constraints of human information processing, identifying products that meet customers' needs is not an easy task. Therefore, many online stores have made RAs available to assist consumers in product search and selection as well as for product customization (Detlor and Arsenault 2002; Grenci and Todd 2002; O'Keefe and McEachern 1998). By providing product advice based on user-specified preferences, a user's shopping history, or choices made by other consumers with similar profiles, RAs have the potential to reduce consumers' information overload and search complexity, while at the same time improving their decision quality (Chiasson et al. 2002; Hanani et al. 2001; Haubl and Trifts 2000; Maes 1994).

In addition, we have seen the establishment of many successful comparison shopping websites, such as Shopping.com and

BizRate. Equipped with different types of high-end RAs, these websites facilitate access to a wide range of products across many merchants, promising to help consumers locate the best product at the lowest price. According to a survey by Burke (2002), over 80 percent of the respondents were enthusiastic about using the Internet to search for product information and to compare and evaluate alternatives. As reported by BusinessWire, $^{6}$ during the 2003 holiday season, 22 percent of shoppers began their shopping at comparison shopping sites. The Economist (June 4, 2005, p. 11) reported that EBay recently bought Shopping.com for \$620 million, further indicating the importance of recommendation technologies to e-commerce leaders. Regardless of the type of websites (online retailers' websites or comparison shopping websites) in which the RAs are embedded, RAs “hold out the promise of making shopping on the Internet better not just by finding lower prices but by matching products to the needs and tastes of individual consumers” (Patton 1999).

The design of RAs consists of three major components: input (where user preferences are elicited, explicitly or implicitly), process (where recommendations are generated), and output (where recommendations are presented to the user). Since the advent of the first RA, Tapestry, about a decade ago, research on RAs has focused mostly on process, which consists of developing and evaluating the different underlying algorithms that generate recommendations (Cosley et al. 2003; Swearingen and Sinha 2002), while failing to focus on and adequately understand input and output design strategies. Similarly, the majority of the review articles regarding RAs (Herlocker et al. 2004; Montaner et al. 2003; Sarwar et al. 2000; Schafer et al. 2001; Zhang 2002) provide either evaluations of different recommendation-generating algorithms (focusing primarily on criteria such as accuracy and coverage) or taxonomies of currently available RAs (mostly in terms of the underlying algorithms and techniques), without paying much attention to other design issues. However, from the customers' perspective, the effectiveness of RAs is determined by many factors aside from the algorithms (Swearingen and Sinha 2002), including the characteristics of RA input, process, output, source credibility, and product-related and user-related factors. This study reviews the literature on e-commerce RA design beyond algorithms to derive propositions for identifying promising areas for future research. This review is organized along the following research questions:

1. How do RA use, RA characteristics, and other factors influence consumer decision-making processes and outcomes?

1.1 How does RA use influence consumer decision-making processes and outcomes?

1.2 How do the characteristics of RAs influence consumer decision-making processes and outcomes?

1.3 How do other factors (i.e., factors related to user, product, and user–RA interaction) moderate the effects of RA use and RA characteristics on consumer decision-making processes and outcomes?

2. How do RA use, RA characteristics, and other factors influence users' evaluations of RAs?

2.1 How does RA use influence users' evaluations of RAs?

2.2 How do characteristics of RAs influence users' evaluations of RAs?

2.3 How do other factors (i.e., factors related to user, product, and user–RA interaction) moderate the effects of RA use and RA characteristics on users' evaluations of RAs?

2.4 How does provider credibility influence users' evaluations of RAs?

This review makes the following contributions to research and practice:

1. It develops a conceptual model with supporting propositions derived from five theoretical perspectives concerning (1) the effects of RA use on consumer decision-making processes and outcomes, as well as the effects on users' evaluations of RAs, (2) how such effects are moderated by RA characteristics and other contingency factors, and (3) the effect of provider credibility on users' evaluations of RAs.

2. It not only compiles and synthesizes existing knowledge from multiple disciplines that contribute to and shape our understanding of RAs, but also identifies critical gaps between what we know and what we need to know, thereby alerting scholars to potential opportunities for key contributions.

3. It offers suggestions about how additional propositions can be developed and how they can be empirically investigated.

4. It provides advice to IS practitioners concerning the effective design and development of RAs.

The unit of analysis for this review is an instance of using the RA. This paper reviews previous theoretical and empirical studies of RAs, as defined in this paper, in both online and offline shopping environments. The review covers a period from the early 1990s, when the first RAs came into being, to the present. A search of literature in information systems, marketing, consumer research, computer science, decision science, and human computer interaction was undertaken to identify the relevant studies. Databases for published journal articles, conference proceedings, and unpublished dissertations, theses, and working papers were searched by using relevant keywords. Leading journals and conference proceedings were also scanned by their table of contents. The criteria for including a particular empirical study $^{7}$ are

\- The study must be “empirical” in the sense that the study has to involve actual use of an RA (prototype or operational, web-based or stand-alone) by human users (similar to the definition of empirical studies in Gregor and Benbasat 1999) in either online or physical settings. $^{8}$

\- The study must have dependent variables that go beyond “accuracy” and “coverage,” $^{9}$ which are the variables commonly investigated as dependent variables in algorithm-focused research.

In the next section, the conceptual model is introduced and the constructs that make up the model are defined. Propositions concerning the relationships among the constructs are then presented and evidence from empirical studies is introduced to test the propositions. In the final section, recommendations to practitioners and researchers are provided and directions for future work are suggested.

## Conceptual Model and Constructs

## Conceptual Model

The conceptual model for this review is depicted in Figure 1. $^{10}$ The key constructs of the conceptual model, from right to left, are outcomes of RA use (consisting of consumer decision making and users' evaluations of RAs), product, user, user–RA interaction, RA characteristics, provider credibility, and RA use. They are identified based on previous conceptual and empirical research in information systems in general, and decision support systems and RAs in particular, as discussed in the following sections. To explicitly indicate the connection between the conceptual and the research questions stated earlier, relationships among the constructs are marked with the corresponding research question number(s). This high level conceptual model will be decomposed into more focused, lower level models in the “Propositions” section to map the relationships among different constructs (and elements of the constructs).

This paper focuses on two classes of outcomes associated with RA use. First, it intends to enquire into the differences in decision making (1) between consumers who are assisted by RAs and those who are not, as well as (2) between consumers using different types of RAs or RAs with differing design characteristics. Hence, the construct consumer decision making is included in the conceptual framework to investigate how the different groups of consumers differ in their decision making processes and outcomes. Second, this paper aims to examine users' perceptions of RAs, represented by the construct users' evaluations of RAs. Since RAs are a particular type of information system, we focus on the two dominant approaches to examining user perceptions of information system success—user satisfaction and IT acceptance (Wixom and Todd 2005)—hence including satisfaction and TAM (technology acceptance model) constructs (perceived usefulness and perceived ease of use) in the conceptual model. In addition to being information technology artifacts, RAs are also trust objects (Gefen et al. 2003; Wang and Benbasat 2005), that is, consumers must have confidence in the RAs' product recommendations, as well as in the processes by which these recommendations are generated (Haubl and Murray 2003). Furthermore, the relationship between RAs and their users can be described as an agency relationship. By delegating the task of product screening and evaluation to

![](/api/attachments/FWEJZ8TG/fulltext/images/ce6c1a3963385f81e0a83e1f4cef338159fa3915aa9b947197cd7cc419dbeee4.jpg)  
Note: Solid lines indicate relationships and constructs investigated in this paper.  
Figure 1. Conceptual Model

RAs (i.e., the agents), users assume the role of principals. Thus, as a result of the information asymmetry underlying any agency relationship, users usually cannot determine whether RAs are capable of performing the tasks delegated to them, and whether RAs work solely for the benefit of the users or the online store where they reside. As such, trust is also an integral part of the conceptual framework.

Eierman et al. (1995) identified six broad DSS constructs (i.e., environment, task, implementation strategy, DSS capability, DSS configuration, and user) that affect user behavior and DSS performance. Brown and Jones (1998) also recognized decision aid features, decision-maker characteristics, and decision-task characteristics as important factors influencing users' reliance on decision aids. Table 1 illustrates the correspondence between the constructs proposed in this review and those included in the two earlier frameworks. Abstracting from the two studies, we include RA characteristics, product, user, user–RA interaction, and provider credibility $^{11}$ in the model as important determinants of both RA-assisted consumer decision making and user evaluation of RAs.

<table><tr><td colspan="4">Table 1. Selection of Constructs</td></tr><tr><td rowspan="2">Constructs Included in Conceptual Model</td><td colspan="2">Sources</td><td rowspan="2">Reasons for Including the Constructs in the Conceptual Model</td></tr><tr><td>Brown and Jones (1998)</td><td>Eierman, Niederman, and Adams (1995)</td></tr><tr><td>RA Characteristics</td><td>Decision aid features</td><td>DSS configuration</td><td>The correspondence between RA characteristics (in this study), decision aid features (Brown and Jones 1998), and DSS configuration (Eierman et al. 1995) is apparent.</td></tr><tr><td>User; User–RA Interaction</td><td>Decision-maker characteristics</td><td>User</td><td>The correspondence between user (in this study), decision-maker characteristics (Brown and Jones 1998), and user (Eierman et al. 1995) is apparent.The construct user–RA interaction (in this study), as the name suggests, captures the relationship between RA and user (e.g., user–RA similarity) as well as users&#x27; experience with RA (e.g., user&#x27;s familiarity with RA, confirmation/disconfirmation of expectation)</td></tr><tr><td>Product</td><td>Decision task characteristics</td><td>Task</td><td>In this study, “task” is fixed, namely, to purchase products with/ without an RA. Since “product” is an integrated component of the buying task, its type (i.e., search or experience) and complexity may affect the effectiveness of the RAs.</td></tr><tr><td>Provider Credibility</td><td></td><td>Environment</td><td>According to Eierman et al. (1995), environment is the setting in which the DSS is developed and used. Since RAs are typically embedded in different websites, referred to as RA provider in this paper, the credibility of such RA provider will influence users&#x27; evaluations of the RA.</td></tr></table>

Finally, the use of RAs is a necessary condition that affects consumers' decision making effectiveness and users' evaluations of the RAs. Although the intent to use IS is modeled as a main dependent variable in most IS adoption research, based on TAM, we explicitly include RA use as an independent variable in the conceptual model for two reasons. First, initial or trial RA use serves as a context for the majority of empirical studies included in this review. TAM specifies that perceived usefulness (PU) and perceived ease of use (PEOU) are two salient beliefs determining users' behavioral intentions (i.e., about future use). Although TAM is silent about where these two beliefs come from, the basic concept underlying TAM as well as other user acceptance models is that an individual's reactions to using IT/IS contribute to the intention to use IT/IS, which, in turn, determines the actual use of IT/IS (Venkatesh et al. 2003). Fishbein and Ajzen (1975) have differentiated three types of beliefs based on three different belief formation processes: descriptive beliefs (based on direct experiences), inferential beliefs (based on prior descriptive beliefs or a prior inference), and informational beliefs (based on information provided by an outside source). In line with Fishbein and Ajzen's account, in the context of RAs, beliefs about RAs may come from two sources: (1) from perceptions acquired from other sources, colleagues, newspapers, etc. (if people have not used RAs yet), or (2) from individuals' direct experiences based on RA use. In this review paper, we are dealing with the second case only. In almost all of the studies reviewed in this paper, the participants are using an RA for the first time. This use of RAs constitutes direct experience through which descriptive beliefs about the RAs are formed. Indeed, in many prior studies validating TAM (e.g., Davis 1989; Davis et al. 1989), subjects were allowed to interact with a system for a brief period of time before their beliefs about the system and intention to use the system were measured, although such interaction with the system (or system use) was not explicitly included in the conceptual model. This paper explicitly models RA use as an independent variable to account for the results of the many experimental studies included in our review.

Second, prior IS research (e.g., Bajaj and Nidumolu 1998; Kim and Malhotra 2005a; Limayem et al. 2003) has investigated the effects of initial or prior IS use on users' evaluations and their subsequent use or adoption of the IS. Bajaj and Nidumolu (1998) have demonstrated that past use itself could be a basis for the formation of user evaluations (i.e., perceived ease of use) at a subsequent stage. Limayem et al. (2003) explicitly incorporate initial IS use in an integrative model explaining subsequent IS adoption and post-adoption. The results of a multistage online survey revealed that initial IS use confirmed or disconfirmed users' prior expectations, thus affecting users' satisfaction with the IS and, subsequently, their intention to continue the use of the IS. Kim and Malhotra (2005b) have developed a longitudinal model of how individuals form (and update) their evaluations of an IT application and adjust their system use over time. The model includes two instances of the IS use construct (use at t = 0 – 1 and Use at t = 1 – 2), representing the use of the IS during two different time periods. In a two-wave survey in the context of web-based IS use, they found that prior use of a personalized web portal influenced users' evaluations of the portal (i.e., the perceived usefulness, perceived ease of use, and future use intention), which in turn influenced the users' future use of the portal.

The two reasons presented above justify our treatment of RA use as an independent variable in the model.

## Definitions of Constructs

Although the constructs in Figure 1 have been labeled, measured, and applied differently in different studies, some common definitions of the constructs are provided below to facilitate the comparison and synthesis of the results from various studies.

Outcomes of RA use includes two general classes of consequences associated with the application of RAs in decision making. Consumer decision making (see Table 2 for definitions) is a broad construct referring to decision processes, including consumers' product evaluations, preference functions, decision strategies, and decision effort, and decision outcomes, including consumers' choice and decision quality (both subjective and objective). Users' evaluations of RAs (see Table 3 for definitions) refers to users' perceptions and assessment of RAs, including their trust in RAs, perceptions of RAs' usefulness and ease of use, and satisfaction with RAs.

Factors related to product (see Table 4 for definitions) include product type and product complexity. Product-related factors have been shown to influence both users' decision-making processes and outcomes and their evaluations of RAs (Swaminathan 2003).

Factors related to user (see Table 4 for definitions) include consumers' characteristics, such as their product expertise and perceptions of product risks. Similar to product-related factors, user-related factors have been investigated as an antecedent of both objective and subjective measures of RA effectiveness (Senecal 2003; Spiekermann 2001; Swaminathan 2003; Urban et al. 1999).

Factors related to user–RA interaction (see Table 4 for definitions) include user–RA similarity (i.e., the user's similarity with RAs in terms of ratings, goals, and needs, decision strategy, and attribute importance), user's familiarity with RAs through repeated use, and confirmation/disconfirmation of the user's prior expectations related to RAs.

In Figure 1, factors related to product, user, and user–RA interaction are modeled as moderators of the effects of RA use and RA characteristics on outcomes of RA Use (i.e., consumer decision making and users' evaluations of RA).

Provider credibility (see Table 4 for definitions) refers to users' perception of the credibility of the providers of RAs. This is influenced by the type of websites in which the RAs are embedded (e.g., sellers' websites, third party websites commercially linked to sellers, or third party websites not commercially linked to sellers) (Senecal 2003; Senecal and Nantel 2004), as well as by the reputation of the websites. The credibility of RAs' providers has a direct impact on users' evaluations of the RAs.

RA characteristics (see Table 5 for definitions) include RA type as well as features and characteristics of RAs related to the following stages:

\- Input (the stage where users' preferences are elicited)

\- Process $^{12}$ (the stage where recommendations are generated by the RAs)

\- Output (the stage where RAs present recommendations to the users).

RA characteristics have been shown to influence the customers' decision-making processes and outcomes, as well as their evaluation of RAs, which in turn influence their behavioral intention to adopt RAs. While a majority of the factors relate to both content-filtering and collaborative-filtering RAs, some (e.g., product attributes included in the

<table><tr><td colspan="2">Table 2. Variables Associated with Consumer Decision Making</td></tr><tr><td>Variables</td><td>Definitions</td></tr><tr><td>Decision processesDecision effortDecision timeExtent of product searchAmount of user inputPreference functionsProduct evaluationDecision strategies</td><td>The amount of effort exerted by the consumer in processing product information, evaluating product alternatives, and arriving at choice decision.The time taken for the consumer to search for product information and make a purchase decision.The number of product alternatives that have been searched, for which detailed information is acquired, and have seriously been considered for purchase by the consumer.The amount of preference information provided by the user prior to receiving recommendations.The consumer&#x27;s attribute-related preferences (e.g., product attribute importance weight).The consumer&#x27;s evaluation (e.g., ratings) of the product alternatives recommended by the RA.The strategies with which the consumer evaluates product alternatives to arrive at product choice.</td></tr><tr><td>Decision OutcomesChoiceDecision quality (objective)Preference matching scoreQuality of consideration setChoice of non-dominated alternative(s)Product switchingDecision quality (subjective)Confidence</td><td>The consumer&#x27;s final choice from the products in the alternative set.The objective quality of the consumer&#x27;s purchase decision, indicated by such measures as:Calculated score of how the chosen alternative matches the consumer&#x27;s preferencesAverages quality of the alternatives that the consumer considers seriously for purchase.Whether the product chosen by the consumer is a dominant or dominated alternative within the context of the whole set of products she selects (when there exists a dominant product) or on a particular attribute dimension (when there is no dominant product).Whether the consumer, after making a purchase decision, changes her mind and switches to another alternative when given an opportunity to do so.The subjective quality of the consumer&#x27;s purchase decision, indicated by such measure asThe degree of a consumer&#x27;s confidence in the RA&#x27;s recommendations.</td></tr></table>

<table><tr><td colspan="2">Table 3. Variables Associated with Users’ Evaluations of RAs</td></tr><tr><td>Variables</td><td>Definitions</td></tr><tr><td>TrustCompetenceBenevolenceIntegrity</td><td>The user beliefs in the RA’s competence, benevolence, and integrity. The beliefs thatthe RA has the ability, skills, and expertise to perform effectivelythe RA cares about the user and acts in the user’s interestthe RA adheres to a set of principles (e.g., honesty and promise keeping) that the user finds acceptable</td></tr><tr><td>Satisfaction</td><td>The user’s satisfaction with RA and her decision-making process aided by the RA.</td></tr><tr><td>Perceived usefulness</td><td>The user’s perceptions of the utility of the RA or the RA’s recommendations.</td></tr><tr><td>Perceived ease of use</td><td>The user’s perceptions of the effort necessary to operate the RA.</td></tr></table>

<table><tr><td colspan="3">Table 4. Factors Related to Product, User, User–RA Interaction, and Provider Credibility</td></tr><tr><td colspan="2">Factors</td><td>Definitions</td></tr><tr><td rowspan="2">Product</td><td>Product type</td><td>Whether a product is a search product or an experience product. Search product is characterized by attributes that can be assessed based on the values attached to their attributes, without necessitating the need for the user to experience the products directly. Experience product is characterized by attributes that need to be experienced prior to purchase.</td></tr><tr><td>Product complexity</td><td>Product complexity is defined along four dimensions: the number of product alternatives, the number of product attributes, variability of each product attribute, and inter-attribute correlations.</td></tr><tr><td rowspan="2">User</td><td>Product expertise</td><td>The user&#x27;s knowledge about or expertise with the intended product.</td></tr><tr><td>Perceived product risks</td><td>The user&#x27;s perceptions of uncertainty and potentially adverse consequences of buying a recommended product.</td></tr><tr><td rowspan="3">User–RA Interaction</td><td>User–RA similarity</td><td>Similarity between the user and the RA in terms of past opinion agreement, goals, decision strategies, and attribute weighting.</td></tr><tr><td>User&#x27;s familiarity with RAs</td><td>The user&#x27;s familiarity with the workings of RAs through repeated use.</td></tr><tr><td>Confirmation/disconfirmation of expectations</td><td>Consistency/inconsistency between the user&#x27;s pretrial expectations about the RA and the actual performance of the RA.</td></tr><tr><td>Provider Credibility</td><td>Provider credibility• Type of RA provider• Reputation of RA provider</td><td>The user&#x27;s perception of how credible the provider of an RA is.• The type of website in which the RA is embedded.• The reputation of the website in which the RA is embedded.</td></tr></table>

RAs' preference-elicitation interface) pertain only to content-filtering ones. RA characteristics are modeled as having direct effect on outcomes of RA use. $^{13}$

RA use refers to the application of RAs to assist in shopping decision making. In most of the empirical studies reviewed in this paper, RA use is an independent variable implemented by comparing use to nonuse of RAs. $^{14}$ RA use is also binary in our research model.

## Propositions

When individuals engage in online or offline shopping with the assistance of web-based RAs, they are simultaneously consumers shopping for products as well as users of an IT artifact. Accordingly, there have been two streams of empirical research on RAs, one focusing on consumers' decision-making processes and outcomes with the assistance of RAs, and the second focusing on users' subjective evaluation of RAs. This paper also adopts this dual focus. In the following subsections, propositions concerning the effects of RA use, RA characteristics, and other factors (i.e., those related to product, user, user–RA interaction, and provider credibility) on consumers' decision making processes and outcomes, as well as on their evaluation of RAs are derived from five theoretical perspectives $^{15}$ : (1) theories of human information processing, (2) the theory of interpersonal similarity, (3) the theories of trust formation, (4) the technology acceptance model (TAM), and (5) the theories of satisfaction. Whereas propositions related to RA-assisted consumer decision making are primarily derived from theories of human information processing, those concerning users' evaluations of RAs and their adoption intention are developed based on the theories of trust formation, TAM, and satisfaction. The theories of interpersonal similarity are drawn upon to explain phenomena in both streams of research.

<table><tr><td colspan="2">Factors</td><td>Definitions</td></tr><tr><td>RA Type</td><td>RA typeContent-filtering vs. collaborative filtering vs. hybridCompensatory vs. non-compensatoryFeature-based vs. needs-based vs. hybrid</td><td>Type of RAsContent filtering RAs generate recommendations based on product attributes the consumer likes; collaborative filtering RAs mimic “word-of-mouth” recommendations and use the opinions of like-minded people to generate recommendations; hybrid RAs integrate content filtering and collaborative filtering methods in generating recommendations.Compensatory RAs allow tradeoffs between attributes. All attributes simultaneously contribute to computation of a preference value; non-compensatory RAs do not consider tradeoffs between attributes.Feature-based RAs ask the consumer to specify what features she wants in a product and then help the consumer narrow the available choices and recommend alternatives; needs-based RAs ask the consumer to provide information about herself and how she will use the product, and then recommend alternatives from which the consumer can make a choice; hybrid RAs allow the consumer to specify both desired product features and product-related needs.</td></tr><tr><td>Input</td><td>Preference elicitation methodIncluded product attributesEase of generating new/additional recommendationsUser control</td><td>Whether feature-based or needs-based preference elicitation method is used.Whether explicit or implicit preference elicitation method is used.What attributes of the product are included in the RA’s preference-elicitation interfaceEase for the user to generate new/additional recommendations (e.g., is the user required to repeat the entire rating or question-answer process to see new recommendations? Can the user modify their previous answers/ratings to generate new recommendations?).The amount of control the user has over the interaction with the RA (e.g., the user may choose what and how many preference-elicitation questions to answer).</td></tr><tr><td>Process</td><td>Information about search progressResponse time</td><td>Whether or not the RA provides information about search progress (e.g., what percentage of the database has the search engine reviewed and what percentage remains to be reviewed).Amount of time elapsed for the user to receive recommendations (after providing ratings or answers to preference-elicitation questions).</td></tr><tr><td>Output</td><td>Recommendation content• Recommendations• Utility scores or predicted ratings• Detailed information about recommended products• Familiar recommendations• Composition of the list of recommendations• ExplanationRecommendation format• Recommendation display method• Number of recommendations• Navigation and layout</td><td>What is presented to the users at output stage?• The product recommendation generated by the RA• Whether or not the RA displays utility scores or predicted product ratings (calculated on the basis of the user’s profile) for the products recommended by the RA• Whether or not the RA provides detailed information about recommended items (e.g., detailed item-specific information, pictures, community ratings)• Whether or not the list of recommendations contains familiar products• The composition of the list of recommendations presented by the RA (e.g., whether there is a balance of both familiar and novel recommendations)• Whether or not explanations are provided on how the recommendations are generated by the RAHow is the recommendation content presented to the users output stage?• Whether the recommendations are displayed in sorted or non-sorted list• The number of recommended products displayed by the RA• Navigational path to product information and layout of the product information</td></tr></table>

The discussion in each subsection follows a common structure:

\- A brief introduction of the subsection is provided.

\- Each proposition is advanced as a triplet of (1) theoretical explanations and past empirical findings (in areas other than RAs) that provide rationale for the proposition; (2) the proposition (and sub-propositions); and (3) existing empirical findings in RA research (if available) that are used to support (or qualify) the proposition.

\- The research question relevant to the discussion in that subsection is answered. Propositions and relevant empirical findings for the subsection are summarized in a table.

## Consumer Decision Making

Consumer behavior is defined as the “acquisition, consumption, and disposition of products, services, time and ideas by decision making units” (Jacoby 1998, p. 320). Major domains of research in consumer behavior include information processing, attitude formation, decision making, and factors (both intrinsic and extrinsic) affecting these processes (Jacoby 1998). This paper focuses on consumer decision making related to the acquisition or buying of products, and separates the outcomes of decision making from the processes of decision making. What follows is a discussion of how RA use, RA characteristics, and other contingencies affect consumer decision making processes and outcomes. The guiding theories for the development of propositions P1 to P13 are the theories of human information processing and the theory of interpersonal similarity. The propositions provide answers to our first research question: How do RA use, RA characteristics, and other factors influence consumer decision-making processes and outcomes? The relationships investigated in this section are depicted in Figure 2.

## RA Use

The application of RAs to assist in consumers' shopping task influences their decision-making processes and outcomes. As predicted by the theoretical perspective of human information processing, and represented in propositions P1 and P2, when supported by RAs in decision making, consumers will enjoy improved decision quality and reduced decision effort.

The Impact of RA Use on Decision Processes. In complex decision-making environments, individuals are often unable to evaluate all available alternatives in great depth prior to making their choices due to their limited cognitive resources. According to Payne (1982; see also Payne et al. 1988), the complexity can be reduced with a two-stage decision-making process, in which the depth of information processing varies by stage. At the first stage (i.e., the initial screening stage), individuals search through a large set of available alternatives, acquire detailed information on select alternatives, and identify a subset (i.e., the consideration set) of the most promising candidates. Subsequently (i.e., at the in-depth comparison stage), they evaluate the consideration set in more detail, performing comparisons based on important attributes before committing to an alternative (Edwards and Fasolo 2001; Haubl and Trifts 2000). Since typical RAs facilitate both the initial screening of available alternatives and the in-depth comparison of product alternatives within the consideration set, they can provide support to consumers in both stages of the decision-making process.

Table 6 illustrates the two-stage process of online shopping decision making, with and without RAs, as well as the tasks performed by RAs and by consumers at each stage. It also shows the different alternative sets $^{16}$ involved in the two-stage decision-making process: (1) the whole set of products available in the database(s) (i.e., the complete solution space), (2) the subset of products that is searched (or search set), (3) the subset of alternatives for which detailed information is acquired (or in-depth search set), (4) the subset of alternatives seriously considered (or consideration set), and the (5) the alternative chosen. As one moves from each set to the next—that is, from (2) to (3) or from (3) to (4)—some form of effortful information-processing occurs.

RA use affects the consumer's decision-making process by influencing the amount of effort exerted during the two stages (as well as the individual phases in each stage) of the shopping decision-making process as illustrated in Table 6. Dictionary.com defines effort as “the use of physical or mental energy to do something.” Consumer decision effort, in online shopping context, refers to the amount of effort exerted by the consumer in processing information, evaluating alternatives, and arriving at a product choice. It is usually measured by decision time and the extent of product search. Decision time refers to the time consumers spend searching for product information and making purchase decisions. Since RAs assume the tedious and processing intensive job of screening and sorting products based on consumers' expressed preferences, consumers can reduce their information search and focus on alternatives that best match their preferences, resulting in decreased decision time.

![](/api/attachments/FWEJZ8TG/fulltext/images/99fc034475cb3e05974006a1d56d29bae59370d1d338398c89cdebcfd5acc7b3.jpg)  
Figure 2. Effects of RA Use, RA Characteristics, and Other Factors on Consumer Decision Making

<table><tr><td colspan="5">Table 6. Two-Stage Process of Online Shopping Decision Making</td></tr><tr><td colspan="2"></td><td>Tasks Performed by Consumers</td><td>Tasks Performed by RA</td><td>Alternative Sets</td></tr><tr><td rowspan="5">Online Shopping Without RA</td><td rowspan="3">Stage 1 Initial Screening</td><td>Searches through a large set of relevant products, without examining any of them in great depth</td><td></td><td>Search set</td></tr><tr><td>Acquires detailed information on a select set of alternatives</td><td></td><td>In-depth search set</td></tr><tr><td>Identifies a subset of alternatives that includes the most promising alternatives for in-depth evaluation</td><td></td><td rowspan="2">Consideration set</td></tr><tr><td rowspan="2">Stage 2 In-Depth Comparison</td><td>Performs comparisons across products (in previously identified subset) on important attributes</td><td></td></tr><tr><td>Makes a purchase decision</td><td></td><td>Final choice</td></tr><tr><td rowspan="7">Online Shopping with RA</td><td rowspan="5">Stage 1 Initial Screening</td><td>Indicate preferences in terms of product features or ratings</td><td></td><td></td></tr><tr><td></td><td>Screens available products in the database to determine which ones are worth considering further and presents a list of products sorted by their predicted attractiveness to the customer (based on the customer&#x27;s expressed preferences)</td><td>Complete solution space</td></tr><tr><td>Searches through the list of recommendations</td><td></td><td>Search set</td></tr><tr><td>Acquires detailed information on a select set of alternatives</td><td></td><td>In-depth search set</td></tr><tr><td>Identifies a subset of products (that includes the most promising alternatives) to be included in comparison matrix</td><td></td><td rowspan="2">Consideration set</td></tr><tr><td rowspan="2">Stage 2 In-Depth Comparison</td><td>Performs comparisons across products (in previously identified subset) on select attributes</td><td>The comparison matrix organizes attribute information about multiple products and allow for side-by-side comparisons of products in terms of their attributes</td></tr><tr><td>Makes a purchase decision</td><td></td><td>Final choice</td></tr></table>

The extent of product search refers to the number of product alternatives that have been searched, for which detailed information is acquired, and have seriously been considered for purchase by consumers. Thus, a good indicator for the extent of product search is the size of the alternative sets (as illustrated in Table 6) and, in particular, the size of the search set, the in-depth search set, and the consideration set. Since RAs present lists of recommendations ordered by predicted attractiveness to consumers, compared to consumers who shop without RAs, those who use RAs are expected to search through and acquire detailed information on fewer alternatives (i.e., only those close to the top of the ordered list), resulting in a smaller search set, in-depth search set, and consideration set. Thus, the use of RAs is expected to reduce the extent of consumers' product search by reducing the total size of alternative sets as well as the size of the search set, in-depth search set, and consideration set.

An additional indicator of consumer decision effort, the amount of user input, occurs during RA-assisted online shopping (see Table 6). The amount of user input refers to the amount of preference information (e.g., desired product features, importance weighting, and product ratings) provided by the users prior to receiving recommendations. Such decision effort will not be incurred by consumers shopping without RAs. It is therefore proposed that

## P1: RA use influences users' decision effort.

P1a: RA use reduces the extent of product search by reducing the total size of alternative sets processed by the users as well as the size of the search set, in-depth search set, and consideration set.

P1b: RA use reduces users' decision time.

P1c: RA use increases the amount of user input.

Dellaert and Haubl (2005) found that RA use reduced the number of products subjects looked at in the course of their search (i.e., the total size of the alternative sets). Similar results were obtained by Moore and Punj (2001). Haubl and Trifts (2000) observed that consumers who shopped with the assistance of RAs acquired detailed product information on significantly fewer alternatives (i.e., the in-depth search set) than did those who shopped without RAs. Haubl and his colleagues (Haubl and Murray 2006; Haubl and Trifts 2000) found that the use of RAs led to a smaller number of alternatives seriously considered at the time the actual purchase decision was made. However, there are some contradictory reports concerning the effects of RA use on the size of consideration set. Pereira (2001) observed that the use of RAs significantly increased the set of alternatives the subjects seriously considered for purchase in the first stage of the phased narrowing process. Pedersen (2000) found no significant effect of RA use on the size of the consideration sets (based on the subjects' self-reports). Swaminathan (2003) observed that the effect of RA use on the size of consideration set was moderated by product complexity.

Concerning decision time, a few studies (Hostler et al. 2005; Pedersen 2000; Vijayasarathy and Jones 2001) noted that, compared to those who did not utilize RAs, RA users spent significantly less time searching for information and completing the shopping task. However, Olson and Widing (2002) observed that consumers who used RAs had longer actual decision time and perceived decision time. They explained that the benefit of less information processing time may be offset by the extra time required to enter product attribute importance weights for the RAs.

The Impact of RA Use on Decision Outcomes. Decision quality refers to the objective or subjective quality of a consumer's purchase decision. It is measured in various ways: (1) whether a product chosen by a consumer is a nondominated (an optimal decision) or dominated (a suboptimal decision) alternative (Diehl 2003; Haubl and Trifts 2000; Swaminathan 2003), (2) as a calculated preference matching score of the selected alternatives, which measures the degree to which the final choice of the consumer matches the preferences she has expressed (Pereira 2001), (3) by the quality of consideration set (Diehl 2003), averaged across individual product quality, (4) by product switching, that is, after making a purchase decision, when given an opportunity to do so, if a customer wants to change her choice and trade her initial selection for another (Haubl and Trifts 2000; Swaminathan 2003), and (5) by the consumer's confidence in her purchase decisions or product choice (Haubl and Trifts 2000; Swaminathan 2003).

The typical decision maker often faces two objectives: to maximize accuracy (decision quality) and to minimize effort (Payne et al. 1993). These objectives are often in conflict, since more effort is usually required to increase accuracy. Since RAs perform the resource-intensive information processing job of screening, narrowing, and sorting the available alternatives, consumers can free up some of the processing capacity in evaluating alternatives, which will allow them to make better quality decisions. Moreover, RAs enable consumers to easily locate and focus on alternatives matching their preferences, which may also result in increased decision quality. It is therefore proposed that

## P2: RA use improves users' decision quality.

Pereira (2001) observed that query-based RAs improved consumers' decision quality, measured both objectively by the preference matching score of the chosen alternative and subjectively by customers' confidence in their decision. Similar results were also obtained by Dellaert and Haubl (2005). Haubl and his colleagues (Haubl and Murray 2006; Haubl and Trifts 2000) found that RAs led to increased decision quality, namely, a decrease in the proportion of subjects who purchased non-dominated alternatives and a decrease in the proportion of subjects who switched to another alternative when given an opportunity to do so. Olson and Widing (2002) also observed that the use of RAs resulted in a lower proportion of subjects who switched from their actual choice to the computed best choice as well as a greater confidence in their choices. Van der Heijden and Sorensen (2002) showed that the use of RAs increased the number of non-dominated alternatives in the consideration set as well as consumers' decision confidence. Hostler et al. (2005) found that RAs increased users' objectively measured decision quality, but had no effect on their decision confidence. The predicted impact for RAs on decision quality, measured by subjects' choices of non-dominated products, was not borne out in another study (Swaminathan 2003). This was attributed to the lack of time pressure in the study. The longer time given to subjects in the control group (the group without RAs) to search for information might have resulted in better decision quality even in the absence of RAs. Vijayasarathy and Jones (2001) noted a negative relationship between the use of decision aids and decision confidence, attributing this outcome to users' lack of trust (which is discussed later in the paper $^{17}$ ) in the decision aids.

<table><tr><td colspan="4">Table 7. The Impact of RA Use on Decision Process and Decision Outcomes</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 1.1.Q1.1: How does RA use influence consumer decision making processes and outcomes?</td></tr><tr><td colspan="2">Relationship Between</td><td>Empirical Support</td><td>P</td></tr><tr><td>RA Use</td><td>Decision Effort• Extent of product search• Decision time• Amount of user input</td><td>RA use reduced the total number of products subjects examined (Dellaert and Haubl 2005; Moore and Punj 2001); RA use reduced the number of products about which detailed information are obtained (Haubl and Trifs 2000); RA use led to smaller consideration sets (Haubl and Murray 2006; Haubl andTrifts 2000); RA use led to larger consideration sets (Pereira 2001); RA use had no effect on self report consideration set size (Pedersen 2000); The effect of RA use on the size of consideration set size was moderated by product complexity (Swaminathan 2003).RA users spent less time searching for information and completing the shopping task (Hostler et al. 2005; Pedersen 2000; Vijayasarathy and Jones 2001); RA users had longer actual and perceived decision time (Olson and Widing 2002).No empirical study available</td><td>P1• P1a• P1b• P1c</td></tr><tr><td>RA Use</td><td>Decision Quality</td><td>RA use improved consumers&#x27; decision quality, in terms of preference matching scores (Dellaert and Haubl 2005; Hostler et al. 2005; Pereira 2001), confidence in decision (van der Heijden and Sorensen 2002; Olson and Widing 2002; Pereira 2001), choice of non-dominated alternatives (Haubl and Murray 2006; Haubl and Trifts 2000; van der Heijden and Sorensen 2002), product switching (Haubl and Murray 2006; Haubl and Trifts 2000; Olson and Widing 2002); RA use had no impact on decision confidence (Hostler et al. 2005); RA use had no impact on decision quality (Swaminathan 2003); RA use reduced decision confidence (Vijayasarathy and Jones 2001).</td><td>P2</td></tr></table>

Summary. The two propositions advanced above help answer research question (1.1): How does RA use influence consumer decision-making processes and outcomes? Using RAs during online shopping is expected to improve consumers' decision quality while reducing their decision effort. While many studies have shown that RA use did result in improved decision quality and decreased decision effort, there also exists some counter evidence. Thus, the empirical evidence in support of the positive effects of RA use on decision quality and decision effort is still inconclusive. Table 7 summarizes the propositions as well as the available empirical support for these propositions.

## RA Characteristics

All RAs are not created equal. As such, the effects of RA use on consumer decision making are determined, at least in part, by RA characteristics (i.e., RA type and characteristics associated with the input, process, and output design). In the following subsections, guided by the theories of human information processing, particularly the effort-accuracy framework and the constructed preferences perspective, we develop propositions P3 through P7 (illustrated in Figure 2) concerning the effects of RA characteristics on consumers' decision-making processes and outcomes. $^{18}$

RA Type. The most common typology of RAs is based on filtering methods: (1) content-filtering RAs, and (2) collaborative-filtering RAs (Adomavicius and Tuzhilin 2003; Ansari et al. 2000; Cosley et al. 2003; Massa and Bhattacharjee 2004; Schein et al. 2002; Wang and Benbasat 2004a; West et al. 1999; Zhang 2002). Content-filtering RAs generate recommendations based on consumers' desired product attributes. Examples of current commercial implementations of content-filtering RAs include Active Buyers Guide and My Simon. Collaborative-filtering RAs, on the other hand, mimic "word-of-mouth" recommendations (Ansari et al. 2000) and use the opinions of like-minded people to generate recommendations (Ansari et al. 2000; Maes et al. 1999). Notable commercial implementations of collaborative-filtering RAs are offered by Amazon, CD Now, and MovieLens. To take advantage of both individuals' desired item attributes and community preferences, many researchers (Balabanovic and Soham 1997; Claypool et al. 1999; Good et al. 1999) have advocated the construction of hybrid RAs that combine content-filtering and collaborative-filtering; Tango, an online RA for newspaper articles, is an example. $^{19}$

RAs can also be classified in terms of decision strategies. Compensatory RAs allow tradeoffs between attributes, that is, desirable attributes can compensate for less desirable attributes. All attributes simultaneously contribute to the computation of a preference value. Weighted additive decision strategy is the most widely used form of the compensatory model. Non-compensatory RAs do not consider tradeoffs between attributes. Since aggregate utility scores are not typically calculated, some attributes may not be considered at all. Also, some attributes may be considered before others. Non-compensatory decision strategies do not form preference scores for products as much as they narrow the set of products under consideration. Most of the currently available RAs, including the ones at My Simon, are non-compensatory RAs.

Grenci and Todd (2002) differentiated between two types of web-based RAs in terms of the amount of support provided by the RAs for consumer purchase. Decision-assisted RAs ask customers to specify what features they want in a product and then help customers narrow down the available choices and recommend alternatives. Expert-driven RAs, on the other hand, ask customers to provide information about themselves and how they will use the product, and then recommend alternatives, from which the customers can make a choice.

Other researchers (Felix et al. 2001; Komiak and Benbasat 2006; Stolze and Nart 2004) have used the terms feature-based RAs and needs-based RAs to refer to decision-assisted RAs and expert-driven RAs, respectively. Stolze and Nart (2004) have also advocated the use of hybrid RAs which allow consumers to specify both desired product features and product-related needs.

The type of RAs used by consumers is expected to have an effect on their decision-making outcomes and decision-making processes. First, hybrid RAs combine both content-filtering and collaborative-filtering techniques, thus integrating individual and community preferences. As such, they may lead to better decision quality than either pure content-filtering or pure collaborative-filtering RAs. However, since hybrid RAs require users to both indicate their preferred product attribute level (as well as importance weights) and provide product ratings, they may require higher user effort than do the other two types of RAs.

Additionally, research conducted by decision scientists has shown that compensatory strategies are generally associated with more thorough information search and accurate choices than non-compensatory ones. Therefore, it is expected that the use of compensatory RAs will improve decision making more than non-compensatory RAs. However, since compensatory RAs typically require users to provide more preference information (e.g., attribute weights), they may increase users' decision effort (as indicated by the amount of user input).

Finally, an assumption made about RA use, which is not always justified, is that the customers recognize their own needs or at least have the ability to understand and answer the preference elicitation questions (Patrick 2002; Randall et al. 2003). It is likely that customers may not possess the required knowledge about the product or its use to specify their preferences correctly. It is also not uncommon for customers to answer a different question than the one asked simply because they may not understand the question actually asked and thus answer the question that they think is being asked. Since needs-based RAs provide support to consumers by asking for their product related needs rather than their specifications of product attributes (Felix et al. 2001; Grenci and Todd 2002; Komiak and Benbasat 2006; Randall et al. 2003; Stolze and Nart 2004), they help consumers better recognize their needs and answer the preference-elicitation questions, which should result in better decision quality.

In sum, the type of RAs provided to the consumers to assist in their shopping tasks will affect consumers' decision quality and decision effort. It is therefore proposed that

P3: RA type influences users' decision effort and decision quality.

P3a: Compared with pure content-filtering RAs or pure collaborative-filtering RAs, hybrid RAs lead to better decision quality and higher decision effort (as indicated by amount of user input).

P3b: Compared with non-compensatory RAs, compensatory RAs lead to better decision quality and higher decision effort (as indicated by amount of user input).

P3c: Compared with feature-based RAs, needs-based RAs lead to better decision quality.

Schafer et al. (2002) observed that hybrid RAs generate more confidence from the users compared to traditional collaborative-filtering ones. Fasolo et al. (2005) found that individuals using compensatory RAs had more confidence in their product choices than did those using non-compensatory RAs.

RA Input Characteristics. A central function of RAs is the capturing of consumer preferences, which allows for the identification of products appropriate for a consumer's interests. The way a consumer's preferences are gathered during the input stage can significantly influence her online decision making. The input characteristics discussed in this section are preference elicitation method and included product attributes.

Consistent with the notion of bounded rationality (Simon 1955), as a result of their limited information processing capacity, individuals often lack the cognitive resources to generate well-defined preferences. Instead of having preferences that are revealed when making a decision, individuals tend to construct their preferences on the spot, for example, when they must make a choice (Bettman et al. 1998; Payne et al. 1992). Since formation of consumer preferences is influenced by the context in which product choices are made (Bellman et al. 2006; Lynch and Ariely 2000; Mandel and Johnson 1998; West et al. 1999), preference reversals often occur. Prior research (Nowlis and Simonson 1997; Tversky et al. 1988) has shown consistent preference reversals when preferences were elicited with different tasks (e.g., choice task versus rating task, choice task versus matching task). In the context of RA use, consumer preferences can either be gathered implicitly (by building profiles from customer's purchase history or navigational pattern) or elicited explicitly (by asking customers to provide product ratings/rankings or answer preference elicitation questions). The means by which preferences are elicited may affect what consumers do with the RAs' recommendations. According to

Kramer (2007), lacking stable preferences, consumers may need to infer their preferences from their responses to preference elicitation tasks, use those self-interpreted preferences to evaluate the alternatives recommended by the RAs, and make a choice decision based on the evaluations. Since an implicit preference elicitation method makes it hard for consumers to have insight into their constructed preferences, they may make suboptimal choice decisions based on their incorrectly inferred preferences. As such, we expect that the means by which preferences are elicited will influence consumers' decision quality. Moreover, since an explicit preference elicitation method requires users to indicate their preferences with product ratings or answers to preference elicitation questions, it demands more decision effort (e.g., in terms of increased user input and decision time) from consumers than does an implicit preference elicitation method. It is therefore proposed that

P4: The preference elicitation method influences users' decision quality and decision effort. The explicit preference elicitation method leads to better decision quality and higher decision effort (as indicated by amount of user input) than does the implicit preference elicitation method.

Aggarwal and Vaidyanathan (2003a) found that the preferences inferred from profile building and the preferences explicitly stated by customers may not be similar. Kramer (2007) observed that respondents were significantly more likely to accept top-ranked recommendations (resulting in better decision quality) when their preferences had been elicited using a more transparent task (i.e., a self-explicated approach in which users explicitly rate the desirability of various levels of attributes as well as the relative importance of the attributes) as opposed to a less transparent task (i.e., a full-profile conjoint analysis). The transparent (i.e., explicit) preference elicitation method enabled users to infer their preferences from their responses to the measurement task and to use these preferences in evaluating the RAs' recommendations.

When consumers depend on RAs for screening and evaluating product alternatives, the RAs influence how consumers construct their preferences. The way a consumer's preferences are obtained during the input stage can significantly influence their online shopping performance. Haubl and Murray (2003) note that real-world RAs $^{20}$ are inevitably selective “in the sense that they include only a subset of the pertinent product attributes.” As such, “everything else being equal, the inclusion of an attribute in an electronic recommendation agent renders this attribute more prominent in consumers' purchase decisions" (p. 75). Thus, when consumers perform comparisons across products in the consideration set during the in-depth comparison stage (as illustrated in Table 6), they are likely to consider the product attributes included in the RAs' preference-elicitation interface to be more important than those not included. Consequently, products that are superior on the included attributes will be evaluated more favorably and will be more likely to be chosen by consumers than products that are superior on the excluded attributes. It is therefore proposed that

P5: Included product attributes $^{21}$ influences users' preference function and choice. Included product attributes (in RA's preference elicitation interface) are given more weight in the users' preference function and considered more important by the users than those not included. Product alternatives that are superior on the included product attributes are more likely to be chosen by users than are products superior on the excluded product attributes.

Haubl and Murray (2003) observed that the number of subjects who chose a product with the most attractive level of the product attribute included in the RAs' preference-elicitation interface was significantly larger than the number of subjects who chose a product with the most attractive level of the product attribute excluded in the RAs' preference-elicitation interface, thereby confirming the hypothesized "inclusion effect." Furthermore, they found that the inclusion effect persisted into subsequent choice tasks, even when no RA was present.

RA Output Characteristics. RA output characteristics discussed in the section include recommendation content (e.g., specific recommendations generated by the RAs and the utility scores or predicted ratings for recommended products) and recommendation format (e.g., the display method for presenting recommendations and the number of recommendations).

Given that the primary function of RAs is to assist and advise consumers in selecting appropriate products that best fit their needs, it is expected that the recommendations presented by the RAs will influence consumers' product choices. In addition to providing product recommendations to consumers, some RAs also provide utility scores (when content-filtering RAs are used) or predicted ratings (when collaborativefiltering RAs are used) for the recommended alternatives. In line with the theory of constructed preferences, due to human cognitive constraints, consumer preferences are frequently influenced by the context in which particular product evaluations and product choices are made. As such, the utility scores or predicted ratings accompanying recommendations are likely to influence consumers' product evaluations during both the initial screening stage and the in-depth comparison stage of the online shopping decision-making process (see Table 6) as well as their final product choice. It is therefore proposed that

P6: Recommendation content influences users' product evaluation and choice.

P6a: Recommendations provided by RAs influence users' choice to the extent that products recommended RAs are more likely to be chosen by users.

P6b: The display of utility scores or predicted ratings for recommended products influences users' product evaluation and choice to the extent that products with high utility scores or predicted ratings are evaluated more favorably and are more likely to be chosen by users.

Senecal (2003; see also Senecal and Nantel 2004), in investigating the influence of online relevant others (including other customers, human experts, and RAs), found that the presence of online product recommendations significantly influenced subjects' product choices. All subjects participating in the study were asked to select one out of four product alternatives. They were free to consult RAs (which would then recommend an alternative out of the four) or not. Senecal observed that subjects who utilized the RAs were much more likely to pick the recommended alternative than those who did not utilize the RA. Similar effects have also been observed by Wang (2005). Focusing on an online collaborative-filtering movie RA, Cosley et al. (2003) conjectured that showing the predicted rating $^{22}$ (the RA's prediction of a user's rating of a movie, based on the user's profile) for a recommended movie at the time the user rates it $^{23}$ (at the output stage) might affect a user's opinion. They conducted an experiment where users were asked to re-rate a set of movies which they had previously rated, after they were given an RA's rating, which was either higher, lower, or the same as the user's initial rating of the movie. A comparison of the new ratings and the original ratings showed that users tended to adjust their opinions to coincide more closely with the RA's prediction, whether the prediction was accurate or not, demonstrating that users can be manipulated by such information.

Recommendation format can also exert significant influence on RA users' decision processes and decision outcomes. First, recommendations are displayed to the users either in the order of how they satisfy users' preferences or in a random order. The display method for presenting recommendations has an effect on strategies used to evaluate products during the initial screening stage of a user's decision-making process. With a sorted recommendation list from RAs, there will be many products that are close in their overall subjective utility (Diehl et al. 2003) but which differ on several attributes (Shugan 1980). According to Shugan (1980), if the difference in overall subjective utility between two products is small, consumers must make many attribute comparisons between the two products to determine the source(s) of this small difference, hence the choice is more difficult than when the utility difference is large between the two products. As choice difficulty increases, consumers tend to depart from the normative, utility-based comparisons (i.e., evaluating the currently inspected product against the most attractive product, in terms of subjective utility, that they have inspected up to that point) and instead base their choice on simplifying heuristics, such as attribute-based processing (rather than alternative-based processing) and local optimization (i.e., comparing the utility between contiguously inspected products) (Haubl and Dellaert 2004; Payne et al. 1988). Consequently, consumers may rely more on heuristic decision strategies when distinguishing among the product alternatives in the sorted list of recommendations and deciding on the ones to be included in the consideration set. Recommendation display method can also result in higher decision quality. Sorted recommendation lists contain many good choices of comparable quality (Diehl et al. 2003), with the most promising options at the beginning of the list. Simply by choosing product alternatives close to the beginning of the sorted list, consumers can achieve better-than-average decision quality.

Second, the number of recommendations presented to the consumers may affect their decision effort and decision quality. Providing too many recommendations may prompt consumers to compare a larger number of alternatives, thus increasing their decision effort by increasing decision time and the size of the alternative sets. Moreover, in a sorted recommendation list, the most promising options are located at the beginning of the list. As such, considering more options in the recommendation list may degrade consumers' choice quality by lowering the average quality of considered alternatives and diverting the consumers' attention from the better options to the more mediocre ones (Diehl 2003).

## It is therefore proposed that

P7: Recommendation format influences users' decision processes and decision outcomes.

P7a: Recommendation display method influences users' decision strategies and decision quality to the extent that sorted recommendation lists result in greater user reliance on heuristic decision strategies (when evaluating product alternatives) and better decision quality.

P7b: The number of recommendations influences users' decision effort and decision quality to the extent that presenting too many recommendations increases users' decision effort (in terms of decision time and extent of product search) and decreases decision quality.

Dellaert and Haubl (2005) found that a sorted list of personalized product recommendations increased consumers' tendency to engage in heuristic local utility comparison when evaluating alternatives. Diehl et al. (2003) have shown that, with a sorted list of recommendations (in the order of how each is predicted to match users' preferences), consumers had better decision quality and paid lower prices. Aksoy and Bloom (2001) also observed that, compared to a randomly ordered list of options, a list of recommendations sorted based on consumers' preferences resulted in higher consumer decision quality. As to the number of recommendations to be presented to RA users, Diehl (2003) found that recommending more alternatives significantly increased the number of unique options searched, decreased the quality of the consideration set, led to poor product choices, and reduced consumers' selectivity. Basartan (2001) constructed an RA in which response time and the number of alternatives displayed were varied. She found that, when the RA provided too many recommendations, it increased the users' effort of evaluating these alternative recommendations.

Summary. The propositions presented in this section help answer research question (1.2): How do the characteristics of RAs influence consumer decision-making processes and outcomes? Various types of RAs exert differential influence on consumers' decision quality and decision effort. RAs' preference elicitation method (i.e., explicit or implicit) also affects consumers' decision quality and decision effort. Included product attributes in RAs' preference elicitation interface, recommendations provided by the RAs, and the utility scores (or predicted ratings) attached to RAs' recommendations, influence consumers' preference functions and product choices. Whereas a sorted recommendation list results in greater consumer reliance on heuristic decision strategies when evaluating alternatives and better decision quality, an excess of recommendations leads to increased decision effort and decreased decision quality. Table 8 summarizes the propositions concerning the impact of RA type, as well as of RA characteristics associated with input and output design, on consumers' decision processes and outcomes. Empirical support (when available) for these propositions is also included.

<table><tr><td colspan="4">Table 8. The Impact of RA Characteristics on Decision Process and Decision Outcomes</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 1.2:Q1.2: How do the characteristics of RAs influence consumer decision making processes and outcomes?</td></tr><tr><td colspan="2">Relationship Between</td><td>Empirical Support</td><td>P</td></tr><tr><td colspan="4">RA Type</td></tr><tr><td>RA TypeContent-filtering,collaborative filtering,vs. hybridCompensatory vs. non-compensatoryFeature-based vs.needs-based</td><td>Decision Qualityand DecisionEffort</td><td>Hybrid RAs generated more confidence from the users than did traditional collaborative-filtering ones (Schafer et al. 2002).Individuals using compensatory RAs had more confidence in their product choices than did those using non-compensatory RAs (Fasolo et al. 2005).No empirical study available.</td><td>P3P3aP3bP3c</td></tr><tr><td colspan="4">RA Input</td></tr><tr><td>Preference ElicitationMethod (implicit vs.explicit)</td><td>Decision Qualityand DecisionEffort</td><td>Inferred and explicitly stated consumer preferences may not converge (Aggarwal and Vaidyanathan 2003a); respondents were more likely to accept top-ranked recommendations when their preferences had been elicited using a more transparent task as opposed to a less transparent one (Kramer 2007).</td><td>P4</td></tr><tr><td>Included productattributes</td><td>PreferenceFunction andChoice</td><td>Attributes included in an RA&#x27;s preference-elicitation interface and sorting algorithm were given more weight during the users&#x27; product choice (Haubl and Murray 2003).</td><td>P5</td></tr><tr><td colspan="4">RA Output</td></tr><tr><td>Recommendation contentRecommendationsUtility Scores orPredicted Ratings</td><td>ProductEvaluation andChoice</td><td>Subjects who used the RA were much more likely to select the recommended alternative than those who did not (Senecal 2003; Wang 2005).The display of predicted rating for a recommended movie at the time the user rates it affected a user&#x27;s opinions: users adjusted their opinions to coincide more closely with the RA&#x27;s prediction (Cosley et al. 2003).</td><td>P6P6aP6b</td></tr><tr><td>Recommendation formatRecommendation Display Method (sorted vs. non-sorted)Number ofRecommendations</td><td>DecisionStrategies,Decision Effort,and DecisionQuality</td><td>Sorted recommendation list increased consumers&#x27; tendency to engage in local utility comparison when evaluating alternatives (Dellaert and Haubl 2005) and resulted in higher decision quality (Aksoy and Bloom 2001; Diehl et al. 2003).Recommending more alternatives increased information searched, decreased the quality of the consideration set, led to poor product choices, and reduced consumers&#x27; selectivity (Diehl 2003); a shopbot that provided too many recommendations increased the users&#x27; cognitive effort and decreased their preference for the shopbot (Basartan 2001).</td><td>P7P7aP7b</td></tr></table>

## Factors Related to Product, User, and User–RA Interaction

The impacts of RA use and RA characteristics on consumers' decision-making processes and outcomes are contingent upon factors related to product, user, and user–RA interaction as well as the interactions between these factors and RA characteristics. The following sections discuss how the different factors related to product (i.e., product type and product complexity), user (i.e., product expertise and perceived product risks), and user–RA interaction (i.e., user–RA similarity) moderate the effects of RA use on consumers' decision making processes and outcomes, as captured in P8 through P13 and illustrated in Figure 2.

Product-Related Factors. Product-related factors such as product type and product complexity moderate the effects of RA use on consumers' decision-making processes and outcomes.

In the context of online shopping, products can be categorized into search products and experience products. Search products (e.g., cameras, calculators, or books) are characterized by attributes (e.g., color, size, price, and components) that can be assessed based on the values attached to their attributes, without necessitating the need to experience them directly. Experience products (e.g., clothing or cosmetics), on the other hand, are characterized by attributes (e.g., taste, softness and fit) that need to be experienced prior to purchase.

Because of the inherent difficulty associated with the evaluation of experience products prior to purchasing online, consumers tend to feel uncertain as to whether the products would meet their expectations, which may lead to increased information search activities (Spiekermann 2001). Moreover, Olshavsky (1985) differentiated between own-based decisionmaking process (whereby consumers reply on themselves to search for information, evaluate alternatives, and make purchase decisions) and other-based decision-making process (whereby consumers subcontract either part or all of their decision-making process). Whereas own-based decision-making processes occur when consumers have the capacity to process information and perform a complex decision-making process, other-based decision-making processes occur when consumers do not have the capacity to process information. King and Balasubramanian (1994) found that product type had a significant impact on consumers' reliance on a particular decision-making process: consumers evaluating a search product (e.g., a camera) were more likely to use own-based decision-making processes; in contrast, those evaluating an experience product (e.g., a movie) tended to rely more on other-based decision-making processes. Prior research has shown that consumers who employed other-based decision-making processes were likely to make purchasing decision in keeping with salespersons' recommendations (Formisano et al. 1982). Following this chain of reasoning, we conclude that consumers evaluating experience products are more likely to rely on salespersons' assistance and adopt their recommendations. Since the role of RAs in online shopping is similar to that of the salespersons in a traditional shopping environment, it is expected that, compared to consumers who use RAs to shop for search products, those who shop for experience products aided by RAs are more likely to choose the products recommended by the RAs. It is therefore proposed that

P8: Product type moderates the effects of RA use on users' choice. RA use influences the choice of users shopping for experience products to a greater extent than that of those shopping for search products.

Senecal (2003; see also Senecal and Nantel 2004) found that product type affected consumers' propensities to follow RAs' product recommendations. Recommendations for experience products (wines) appeared significantly more influential than recommendations for search products (calculators).

Products can differ along another dimension, product complexity, which is the extent to which the product is perceived by the consumer as difficult to understand or use (Rogers 1995). Prior literature in marketing and IS has revealed different schemes for characterizing products in terms of complexity. In marketing research, the complexity of a product is usually defined in terms of the number of attributes used to describe the product (Keller and Staelin 1987; Swaminathan 2003), the number of alternatives for the product category (Keller and Staelin 1987; Payne et al. 1993; Swaminathan 2003), or the number of steps involved in the use of the product (Burnham et al. 2003). E-commerce literature defines product complexity along three dimensions: number of product attributes, variability of each product attribute, and interdependence of product attributes (Jahng et al. 2000). The higher the number of attributes of a product, the higher the level of variation of each attribute and the greater the degree of interdependence among product attributes, the greater the product complexity. This paper adopts the definition of product complexity by Jahng et al. (2000), but it adds an additional criterion, namely, how the product attributes correlate with one another. When product attributes are positively correlated, an alternative that is favorable on one attribute tends to also be favorable on other attributes. In contrast, when product attributes are negatively correlated, a more attractive level of one attribute is associated with a less attractive level of another. Products characterized by negative inter-attribute correlations are considered more complex (Fasolo et al. 2005), since purchase decisions of such products require consumers to make trade-offs among attributes.

Previous research into information search has examined the impact of product complexity on consumer decision quality and search behavior (Bettman et al. 1998; Keller and Staelin 1987; Payne et al. 1993). Keller and Staelin (1987) developed an analytical model, which showed that higher number of product attributes and alternatives resulted in decreased decision effectiveness. Payne et al. (1993) and Bettman et al. (1998) suggest that product complexity increases consumers' cognitive load, resulting in decision biases. As product complexity increases, consumers often resort to heuristics to manage information overload, hence decision quality decreases. Therefore, the benefits of using RAs, in terms of decision quality and search efforts, are likely to be greater when a product is complex. It is therefore proposed that

P9: Product complexity moderates the effects of RA use on users' decision quality and decision effort. The use of RAs for more complex products leads to greater increase in decision quality and greater decrease in decision effort than for less complex products.

Empirical results from prior research, however, are not supportive of this proposition. Fasolo and her colleagues (2005) found that, in the presence of negatively related attributes (an indicator of product complexity), consumers using RAs engaged in more information search, rated the decisions to be more difficult, and were less confident in their product choices. Swaminathan (2003) found that the RAs had a more significant impact on search efforts when product complexity was relatively low, contrary to what he had hypothesized. Swaminathan explains that when the product is complex (i.e., when the number of attributes is greater), there are more dimensions on which the alternatives are different from one another, making it more difficult for users to identify the best option and thus leading to greater search even in the presence of the RA. On the other hand, when the product is of low complexity (i.e., when the number of attributes is fewer), users have little difficulty finding the best option with the assistance of the RA. However, this unexpected finding may also be a result of Swaminathan's manipulation of product complexity by varying the number of attributes used to describe the product. Users may have prior perceptions of the complexity of a given product and therefore may not be sensitive to such artificial manipulations.

As noted by Haubl and Murray (2003), inter-attribute correlation moderates the impact of product attributes included (in RAs' preference elicitation interface) on consumers' product choice. They argue that, for products characterized by negative inter-attribute correlations, the relative importance attached to different attributes tends to be highly consequential with respect to the decision outcome: even very small differences in relative attribute importance may affect which product is chosen from a set of alternatives. In contrast, for products characterized by positive inter-attribute correlation, the relative importance attached to different attributes has much less of an impact on determining which product is chosen. Therefore, although product attributes included in the RAs' preference elicitation interface will be considered more important by consumers, such a change in the relative importance of product attributes will have a stronger impact on consumers' product choice for products with negative inter-attribute correlations than for those with positive ones. It is therefore proposed that

P10: Product complexity moderates the effect of included product attributes on users' choice. The inclusion effect is stronger for products with negative inter-attribute correlations (i.e., more complex products) than for those with positive inter-attribute correlations (i.e., less complex products).

Haubl and Murray (2003) demonstrated that the preference-construction effect of RAs depended on the inter-attribute correlation structure across the set of available products. There existed a strong inclusion effect when there were negative inter-attribute correlations, but not for positive inter-attribute correlations.

User Related Factors. The effects of RA use on consumers' decision-making processes and outcomes are also moderated by user-related factors, including product expertise and perceived product risks.

RAs do not have the same impact on decision outcomes across different types of users. Hoeffler and Ariely (1999) posit that consumers construct their preferences when they are new to a product category and eventually develop more stable preferences with experience in a domain. Coupey et al. (1998) also state that consumers who are highly familiar with a product category are less subject to framing effects during preference elicitation. As such, compared with individuals with low product expertise, RA users with high product expertise are likely to have more stable, better-defined preferences and thus are less likely to be affected by the RA's preference elicitation method. It is therefore proposed that

P11: Product expertise moderates the effect of preference elicitation method on users' decision quality. Preference elicitation method has less effect on the decision quality of users with high product expertise than on the decision quality of those with low product expertise.

In his investigation of the effect of measurement task transparency on preference construction and evaluations of personalized recommendations, Kramer (2007) observed that, although respondents were in general more likely to accept a top-ranked recommendation (resulting in better decision quality) when their preferences had been measured using a more transparent task, the effect was modified by the product expertise of the users. Differences in accepting a recommendation occurred only for those who did not have product expertise.

Several dimensions of product risks have been identified and measured in consumer research, including financial, functional, social, and psychological (Spiekermann and Paraschiv 2002). One or more of these sources may drive consumers' overall perceptions of product risks, which are considered to be central to their product evaluations and product choice (Campbell and Goodstein 2001). Inasmuch as information searches are used as part of risk-reduction strategies (Dowling and Staelin 1994), RAs that are designed to facilitate consumers' online product searches by assisting them in screening and evaluating product alternatives are likely to play a more significant role in improving decision quality and reducing search efforts when product risks are high. It is therefore proposed that

P12: Perceived product risks moderate the effects of RA use on users' decision quality and decision effort. When perceived product risks are high, RA use leads to greater improvements in decision quality and reduction in decision effort than when perceived product risks are low.

Swaminathan (2003) conducted an investigation of the moderating role of perceived product risk on the impact of RAs on consumer evaluation and choice. He found that RAs had a more significant impact on decision quality when perceptions of product risk were high. Spiekermann (2001), however, observed that RA users addressed products with different risk structures with different information search behaviors. While users viewed fewer alternatives and spent more time on each alternative for products with high functional and financial risks (i.e., cameras), they viewed more alternatives but spent less time on each alternative for products with high social-psychological risks (i.e., winter jackets).

Factors Related to User–RA Interaction. To serve as “virtual advisers” for consumers, RAs must demonstrate similarity to their users, that is, they must internalize users’ product-related preferences and incorporate such preferences into their product screening and sorting process. RAs that generate and present recommendations not concordant with the consumers’ own needs are not likely to enhance consumers’ decision quality. Moreover, in accordance with the theory of interpersonal similarity (Byrne and Griffitt 1969; Levin et al. 2002; Lichtenthal and Tellefsen 1999; Zucker 1986), the similarities (actual and/or perceived) between RAs and their users (in attribute importance weightings, decision strategies, goals, etc.) are expected to improve the predictability of the RAs’ behavior and focus users’ attention on more attractive product alternatives (Levin et al. 2002; Zucker 1986), thus resulting in improved decision quality and reduced decision effort in online shopping tasks. It is therefore proposed that

P13: User–RA similarity moderates the effects of RA use on users' decision quality and decision effort. RA use leads to greater increase in decision quality and greater decrease in decision effort when the RAs are similar to the users than when the RAs are not similar to the users.

Aksoy and Bloom (2001) examined the effect of actual similarity of attribute weights and perceived similarity of decision strategies between users and RAs on decision quality and decision effort (as indicated by decision time). In their study, perceived similarity was measured by the degree of similarity (1) between the proportionate weight attached to an attribute by an RA and the proportionate weight determined by consumers, and (2) between the decision-making strategy used by an RA and the consumers' own decision-making strategies. The researchers observed that consumers who were presented with recommendations based on attribute weights similar to their own tended to make better decisions (e.g., they were less likely to choose dominated alternatives) and spend less time examining alternatives. However, no significant effect was found for similarities in decision-making strategies.

<table><tr><td colspan="4">Table 9. The Impact of Factors Related to Product, User, and User–RA Interaction on Decision Process and Decision Outcomes</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 1.3.Q1.3: How do other factors (i.e., factors related to user, product, and user–RA interaction) moderate the effects of RA use and RA characteristics on consumer decision making processes and outcomes?</td></tr><tr><td>Moderator</td><td>Relationship Moderated</td><td>Empirical Support</td><td>P</td></tr><tr><td colspan="4">Product-Related Factors</td></tr><tr><td>Product Type (search vs. experience)</td><td>RA Use on Choice</td><td>Recommendations for experience products were more influential than those for search products (Senecal, 2003; Senecal and Nantel 2004).</td><td>P9</td></tr><tr><td>Product Complexity</td><td>RA Use on Decision Quality and Decision Effort</td><td>In the presence of negatively related attributes, consumers using decision aids engaged in more information search and were less confident in product choices (Fasolo et al. 2005); RAs had a more significant impact on search efforts when product complexity was relatively low (Swaminathan 2003).</td><td>P9</td></tr><tr><td>Product Complexity</td><td>Included Product Attributes on Choice</td><td>There existed a strong inclusion effect in a scenario characterized by negative inter-attribute correlation, but not in the case of positive inter-attribute correlation (Haubl and Murray 2003).</td><td>P10</td></tr><tr><td colspan="4">User-Related Factors</td></tr><tr><td>Product Expertise</td><td>Preference Elicitation Method on Decision Quality</td><td>Although users were in general more likely to accept a top-ranked recommendation when their preferences had been measured using a more transparent task, the effect was modified by the product expertise of the users: differences in accepting recommendation occurred only for those who did not have product expertise (Kramer 2007).</td><td>P11</td></tr><tr><td>Perceived Product Risks</td><td>RA Use on Decis-sion Quality and Decision Effort</td><td>RAs caused a more significant impact on decision quality under conditions involving perceptions of relatively high product risk (Swaminathan 2003); RA users addressed products with different risk structure with different information search behavior (Spiekermann 2001).</td><td>P12</td></tr><tr><td colspan="4">User–RA Interaction</td></tr><tr><td>User–RA Similarity</td><td>RA Use on Decis-sion Quality and Decision Effort</td><td>User–RA similarity in attribute weights resulted in better decision quality and less information search; No effect was found for user–RA similarity in decision making strategies (Aksoy and Bloom 2001).</td><td>P13</td></tr></table>

Summary. The propositions presented here provide answers to research question (1.3): How do other factors moderate the effects of RA use and RA characteristics on consumer decision-making processes and outcomes? The effects of RA use and RA characteristics on decision quality, product choice, and decision effort are stronger for complex products. RAs' effects on influencing consumers' product choice are stronger for experience products. The higher the consumers' product expertise, the less likely their decision quality is influenced by RAs. RAs are expected to exert the greatest effects on decision quality and decision effort when the consumers' perceptions of product risks are high or when RAs are perceived to be similar to the user. Table 9 summarizes the theoretical propositions as well as their empirical support.

## Users' Evaluations of RAs

The criteria users apply to evaluate RAs are based on their general perceptions of the RAs, which are affected by RA use, RA characteristics (RA type as well as RA input, process, and output characteristics), RA provider credibility, and factors related to product, user, and user–RA interactions. All five theoretical perspectives are drawn upon to guide the development of hypotheses P14 through P28, which provide answers to our second research question: How do RA use, RA characteristics, and other factors influence users' evaluations of RAs? The relationships investigated in this section are depicted in Figure 3.

## RA Use

According to Fishbein and Ajzen (1975), an individual's descriptive beliefs about an object can be formed through direct experiences with such object. Prior IS research (e.g., Bajaj and Nidumolu 1998; Kim and Malhotra 2005a; Limayem et al. 2003; Venkatesh et al. 2003) has also shown that IS use can serve as a basis for the formation (or update) of user evaluations (i.e., usefulness, ease of use, trustworthiness, and satisfaction) of the IS at a subsequent stage. In the context of RA-assisted online shopping, the use of RAs is expected to influence consumers' evaluations of the RAs. However, such an effect will be determined, at least in part, by RA characteristics and factors related to product, user, and user–RA interaction. A general proposition such as "RA use will influence users' perceived usefulness of, perceived ease of use of, trust in, and satisfaction with an RA" does not provide much insight into our understanding of the effects of RA use on users' evaluations. In order to answer research question (2.1)—How does RA use influence users' evaluations of RAs?—it is important to take into account RA characteristics and other important moderating factors.

## RA Characteristics

Just as the effects of RA use on consumers' decision-making processes and outcomes are influenced by the RA characteristics, their effects on users' evaluations of RAs are also determined partially by the type of RAs, as well as by the characteristics of the RAs associated with the input, process, and output design. In the following subsections, guided by the theories of trust formation, theories of interpersonal similarity, and TAM, we develop a set of propositions, P14 through P21 (illustrated in Figure 3) concerning the effects of RA characteristics on users' evaluations of RAs. $^{24}$

The Impact of RA Type on Users' Evaluations of RA. In addition to its effects on consumers' decision making processes and outcomes, the type of RA used is also expected to affect users' evaluations of RAs. First, since hybrid RAs base their recommendations both on individual users' specifications for product attributes and on inputs from similar others (i.e., other consumers who are similar in tastes and preferences to the users), users may develop greater trust in such RAs and consider them more useful than pure content-filtering or collaborative-filtering RAs. However, hybrid RAs generally require more user input in the form of answers to preference elicitation questions and ratings on alternatives.

Therefore, users may consider that hybrid RAs require more effort.

Second, prior research has shown that, although consumers do not enjoy exerting their own decision making effort, they react positively to the effort exerted by others (Mohr and Bitner 1995). For instance, Kahn and Baron (1995) investigated the preferred choice rules by individuals and found that, although most participants chose the simple non-compensatory rules, they wanted their doctors or financial officers to use compensatory rules (which require more effort) when making decisions on their behalf. In an RA-assisted shopping context, cognitive effort has shifted, at least partially, from consumers to RAs. Since consumers in such a context rely mostly on RAs' efforts rather than on their own, we expect that they will evaluate compensatory RAs more favorably (i.e., more trustworthy, useful, and satisfactory) than non-compensatory RAs. However, since compensatory RAs require more user input (e.g., attribute weights) than non-compensatory ones, users may perceive the former as more difficult to use.

In sum, RA type affects users' trust in, perceived usefulness of, perceived ease of use of, and satisfaction with RAs. It is therefore proposed that

P14: RA type influences users' evaluations of RAs.

P14a: Compared with pure content-filtering or pure collaborative-filtering RAs, hybrid RAs lead to greater trust, perceived usefulness, and satisfaction but to lower perceived ease of use.

P14b: Compared with non-compensatory RAs, compensatory RAs lead to greater trust, perceived usefulness, and satisfaction but to lower perceived ease of use.

Schafer et al. (2002) compared meta-recommender systems that combine collaborative-filtering and content-filtering techniques to traditional recommender systems (using only collaborative-filtering technique) and found that users considered the former more helpful than the latter.

Users' evaluations of certain RA types are also contingent on user related factors. For instance, users' product expertise will influence their evaluation of collaborative-filtering versus content-filtering and needs-based versus feature-based RAs. The theoretical justifications, propositions and empirical support (when available) are presented later in this section.

RA Input Characteristics. The means by which users' preferences are elicited, the ease for users to generate new or additional recommendations, and the amount of control users have when interacting with the RAs' preference elicitation interface influence users' evaluations of the RAs.

![](/api/attachments/FWEJZ8TG/fulltext/images/b691e24ae238c08061090148b0a8aeead2fe3f28653bbac1a84a4189dd701e0b.jpg)  
Figure 3. Effects of RA Use, RA Characteristics, and Other Factors on User Evaluation of RA

Given users' reluctance to extend cognitive effort, RAs that employ explicit (implicit) preference elicitation method will be considered more difficult (easier) to use, all other things being equal. Additionally, since individuals typically do not have stable preferences, they may need to modify their previously specified preferences while interacting with the RAs to generate new or additional recommendations. As such, compared to RAs that require users to repeat the entire preference-elicitation process when they desire new recommendations, RAs that make it convenient for users to adjust their preferences to generate new recommendations will be considered easier to use. In line with DeLone and McLean's (2003) IS success model, ease of use will enhance users' perception of RAs' system quality, which in turn contributes to their satisfaction with the RAs. It is therefore proposed that

P15: The preference elicitation method influences users' perceived ease of use of and satisfaction with the RAs. Compared to an explicit preference elicitation method, an implicit preference elicitation method leads to greater perceived ease of use of and satisfaction with the RAs.

P16: The ease of generating new or additional recommendations influences users' perceived ease of use of and satisfaction with RAs. The easier it is for the users to generate new or additional recommendations, the greater their perceived ease of use of and satisfaction with the RAs.

No study has investigated the effect of the preference elicitation method on users' perceptions of how easy it is to use the RAs. Swearingen and Sinha (2001, 2002) observed that simplifying a process whereby a user can generate new or additional recommendations (i.e., not requiring users to repeat an entire set of ratings or a question-answer process to obtain new recommendations), improved estimations of the ease of use of RAs. Pereira (2000) found that giving the users the capability to return to the preference specification stage at any time and restate their preferences significantly increased their positive responses to RAs. Bharati and Chaudhury (2004) also demonstrated the net positive effect of RAs' system quality (i.e., ease of use, convenience of access, and reliability) on users' decision making satisfaction.

The attainment of the goal of a decision aid to improve users' decision-making processes may be undermined by system restrictiveness, defined as “the degree to which and the manner in which a DSS limits its users’ decision-making processes to a subset of all possible processes” (Silver 1990, p.52). Not only can users perceive physical limitations of the system, they can also be induced to employ a much narrower range of decision processes than that for which the system was originally designed (Chu and Elam 1990; Silver 1988). As such, instead of trying to force changes in users' decision-making processes, system designers should implement a minimally restrictive DSS and provide support for a variety of decision models that the decision maker might choose to employ (Silver 1990). A comprehensible, predictable, and controllable system will give users the feeling of accomplishment (Shneiderman 1997) and assurance (DeLone and McLean 2003). In the same vein, in the context of RA-assisted online shopping, allowing users to control their interactions with RAs to meet their personal needs (e.g., allowing the users to specify the type of information they are most interested in and to personalize the interface) will increase their trust and personal satisfaction (West et al. 1999) and reduce their perceived functional, financial, and socio-psychological risks (Spiekermann 2001; Spiekermann and Paraschiv 2002). Moreover, such control increases the degree of active involvement of users in the decision task and thus creates an illusion of control (see Davis and Kottemann 1994; Kottemann and Davis 1994; Langer 1975), which, as discussed previously, can cause users to overestimate the advantage of RAs that allow user control. This in turn results in the perception of such RAs as more useful than those that put the users in a more passive role. An example of user control of interaction with RAs is the flexibility afforded to users to choose the length and depth of the interactions with RAs. It is therefore proposed that

P17: User control of interaction with RAs' preference-elicitation interface influences users' trust in, satisfaction with, and perceived usefulness of the RAs. Increased user control leads to increased trust, satisfaction, and perception of usefulness.

Pereira (2000) observed that increased user control over interaction with RAs resulted in more positive affective reactions to RAs. The three ways of increasing the degree of user control (i.e., giving the users the ability to return to the preference specification stage at any time and restate their preferences, to skip responses to certain attribute specifications requested, and to express their degree of confidence in the preference specifications for each attribute) significantly increased users' trust in and satisfaction with two content-filtering RAs. McNee et al. (2003) contrasted system-controlled RAs (i.e., the RAs decide which items the users can rate) with user-controlled ones (i.e., the users are allowed to specify some or all of the items to be rated) and found that the user-controlled RAs generated higher user satisfaction than system-controlled RAs. Users of user-controlled RAs also thought the RAs best understood their tastes and were most loyal to the RAs. Komiak et al. (2005) found that control process (i.e., a process whereby users have more control over their interaction with the RAs) was one of the top contributors to users' trust in a virtual salesperson. Wang (2005) also observed that RAs that were perceived by users as more restrictive (i.e., restricting users' decision strategies to a greater extent) were considered as less trustworthy and useful.

RA Process Characteristics. Characteristics of RAs during the recommendation generation process, such as the information about search process and system response time, will moderate the effects of RA use on users' evaluations of RAs.

King and Hill (1994) have noted that it is necessary to distinguish between consumers' involvement with the decision process and their experience with the outcome of the process. West et al. (1999) also suggest that, when measuring consumer satisfaction, it is important to consider satisfaction with both the decision-making process and the final product choice. In the context of online shopping with the assistance of RAs, cognitive effort is partly shifted from consumers to the RAs. While customers may be reluctant to exert their own efforts, they generally welcome efforts expended by others (Kahn and Baron 1995; Mohr and Bitner 1995). Consumers use various cues or indicators to assess the amount of effort saved by decision aids (Mohr and Bitner 1995), such as indications of the amount of information that has been searched by a decision aid (Bechwati and Xia 2003). For example, Microsoft Expedia informs users that the system is searching thousands of databases for the best airfare while the customers are waiting for results. It is expected that customers who are informed about the RA's search progress (while waiting for recommendations) will perceive that the RAs have saved them a higher amount of effort, and thus will be more impressed with the RAs' empathy (i.e., care and attention). As predicted by DeLone and McLean (2003), empathetic RAs are considered of higher service quality and thus result in higher user satisfaction with the RAs and with the RA-assisted decision-making process. It is therefore proposed that

P18: The provision of information about search progress, while users await results influences users' satisfaction with RAs. Users who are informed about RAs' search progress (while waiting for recommendations) are more satisfied with the RAs.

Bechwati and Xia (2003) observed that consumers' satisfaction with a decision process increased with the level of effort they saved. They conducted two empirical studies on the use of a job search RA, discovering that informing online shoppers about the progress of a search augmented the shoppers' perceptions of the effort saved for them by an RA. Consequently, their satisfaction with the decision-making process concerning purchasing the product also increased.

System response time, the time between the user's input and the computer's response, has been widely recognized as one of the strongest stressors during human-computer interaction (Thum et al. 1995). Assessments of the effects of response time have been conducted for personal computer use in a variety of contexts. Long response time increases stress levels (Weiss et al. 1982), self-reports of annoyance (Schleifer and Amick 1989), frustration, and impatience (Sears and Borella 1997) of personal computer users. According to DeLone and McLean (2003), response time influences users' perception of system quality and thus their satisfaction with information systems. Prior research has shown that lengthy system response times cause lower satisfaction among users (e.g., Hoxmeier and DiCesare 2000; Shneiderman 1998). In the context of RA-assisted shopping, we also expect longer response times to negatively affect users' satisfaction with RAs. It is therefore proposed that

P19: Response time influences users' satisfaction with RAs. The longer the RAs' response times, the lower the users' satisfaction with the RAs.

Basartan (2001) constructed a simulated shopbot in which response time was varied. She found that users' preference for the shopbot decreased when they had to wait a long time before receiving recommendations. Swearingen and Sinha (2001, 2002), however, found that the time taken by users to register and to receive recommendations from RAs did not have a significant effect on users' perceptions of the RA. The seemingly contradictory research findings regarding response time may be explained by users' cost–benefit assessments; when they perceive that the benefits of waiting (e.g., obtaining quality recommendations) outweigh its costs, they will not form negative evaluations of the RAs.

RA Output Characteristics. The output stage is where RAs' recommendations are presented to users. The content and the format of these recommendations can have significant impact on users' evaluations of RAs.

Specifically, three aspects (i.e., the familiarity of the recommendations, the amount of information on recommended products, and the explanations on how the recommendations are generated) are relevant to how recommendation content influences users' evaluations of RAs. First, according to knowledge-based trust theorists (Luwicki and Bunker 1995) individuals develop trust over time as they accumulate knowledge relevant to trust, through their experiences with another party (McKnight et al. 1998). Knowledge-based trust is grounded substantially in the predictability of the other party, which develops as each party proceeds to know the other well enough to be able to anticipate his or her behavior and thereby to avoid surprises. Familiarity builds trust (Komiak 2003; Komiak and Benbasat 2006). Therefore, we expect that consumers will trust RAs that provide familiar recommendations (i.e., product recommendations with which consumers have had positive experience previously) more than those that provide unfamiliar or novel recommendations (i.e., product recommendations consumers have not experienced before). However, to be considered useful RAs that provide relevant information to consumers, the RAs must present them with unfamiliar alternatives that fit the consumers' needs. One possible solution suggested by Cooke et al. (2002) to overcome users' negative reactions to RAs that provide unfamiliar recommendations involves embedding unfamiliar recommendations among a set of recommendations that the users are known to like (based on their purchase history or previous feedback). Recommendations of familiar products can serve as a context within which unfamiliar recommendations are evaluated, hence improving the attractiveness of the unfamiliar recommendations and the evaluation of the RAs.

Second, detailed information about recommendations generated by RAs (e.g., product descriptions in text or multimedia format, expert reviews, or other customers' evaluations) can signal to the users that the RAs care about them, act in their interests, and behave in an honest and unbiased fashion, thereby contributing to users' assessments of the RAs' benevolence and integrity. Additionally, RAs that provide detailed information can educate users about the product category in general and the recommended alternatives in particular, thus contributing to the users' perception of the RAs' usefulness. Detailed information also promotes users' perception of RAs' information quality, thereby enhancing their satisfaction with the RAs.

Third, research on explanation facilities in knowledge-based systems (KBS) has demonstrated that explanations can help alleviate information asymmetry (which occurs when the trustee has more or better information than the trustor) and make a KBS more transparent to its users, thus contributing to the users' trust in the KBS (Gregor and Benbasat 1999). In the same vein, the provision of explanations on how the RAs' recommendations reflect users' preferences and requirements will increase users' trust in the RAs.

It is therefore proposed that

P20: Recommendation content influences users' evaluations of RAs.

P20a: Familiar recommendations increase users' trust in the RAs.

P20b: The composition of the list of recommendations, as reflected by a balanced representation of familiar and unfamiliar (or new) product recommendations, influences users' trust in, perceived usefulness of, and satisfaction with RAs.

P20c: The provision of detailed information about recommended products increases users' trust in, perceived usefulness of, and satisfaction with RAs.

P20d: The provision of explanation on how the recommendations are generated increases users' trust in and satisfaction with RAs.

Sinha and Swearingen (2001; Swearingen and Sinha 2001) found that, although novel recommendations were generally considered more useful than familiar recommendations, recommended products that were familiar to users or that had previously met the users' approval played an important role in establishing users' trust in RAs. Cooke et al. also showed that unfamiliar recommendations lowered users' evaluations of a simulated music CD RA.

Available empirical evidence also supports the positive effect of detailed product information on users' evaluations of RAs. Sinha and Swearingen (2001; Swearingen and Sinha 2001) found that users' trust in RAs increased when the RAs provided detailed product information. Expert reviews and other consumers' ratings, for example, were very helpful in consumers' decision-making processes. Cooke et al. demonstrated that a technique RAs could use to increase the attractiveness of unfamiliar recommendations was to provide users with additional information about a new product. Bharati and Chaudhury (2004) also observed a net positive effect of factors related to information quality (i.e., relevance, accuracy, completeness, and timeliness) on users' decision-making satisfaction.

Investigating the effects of different types of explanations on users' trust in content-based RAs for digital cameras, Wang and Benbasat (2004a) found that the explanations of RAs' reasoning logic (how explanations) strengthened users' trusting beliefs in the RAs' competence and benevolence. Likewise, Herlocker et al. (2000) showed that the addition of explanation facilities increased the acceptance of MovieLens, an online collaborative-filtering movie RA. Most participants in their study valued the RA's explanations and wanted them to be included in MovieLens. Sinha and Swearingen, in a series of studies involving RAs in different domains (Sinha and Swearingen 2001, 2002; Swearingen and Sinha 2001,

2002), also confirmed that explanations can enhance perceptions of the transparency of RAs' inner workings, which in turn result in increased user trust in the RAs. Similar effects have also been observed by Wang (2005).

How users evaluate RAs is also influenced by recommendation format, as reflected by the navigation and layout of the recommendation presentation interface. Given human reluctance to extend unnecessary cognitive effort, consumers generally negatively evaluate an RA that is inconvenient to use. Although providing detailed information about recommended alternatives is desirable, its benefits will not be fully realized unless the navigational paths to product information and the layout of the product information are clear. It is therefore proposed that

P21: Recommendation format influences users' perceived usefulness of, perceived ease of use of, and satisfaction with the RAs. RAs with a clear navigational path and layout are considered more useful, easier to use, and more satisfactory than those without.

In their investigation of RAs in different domains, Sinha and Swearingen (2001; Swearingen and Sinha 2002) found that interface features, such as navigation and layout, were most significant when they presented excess obstacles to users. For instance, users were generally dissatisfied when too many clicks were required to obtain detailed information about recommended items, or when only a few recommendations were displayed on each screen. Bharati and Chaudhury, however, failed to find a significant relationship between navigational efficiency and user satisfaction.

Summary. The propositions presented here help answer research question (2.3): How do characteristics of RAs influence users' evaluations of RAs? Users' trust in, perceived usefulness and ease of use of, and satisfaction with an RA are influenced by RA type as well as by RA characteristics associated with input, process, and output designs. Various types of RAs result in different user perceptions of RAs. For instance, whereas hybrid or compensatory RAs are perceived as more difficult to use, they generally lead to higher trust and are considered more useful and satisfactory. Adequate user control, familiar recommendations, detailed information about recommended products, and explanations on system logic enhance users' trust in RAs and their perception of the usefulness of RAs. Implicit preference elicitation methods, ease of generating new recommendations, clear navigational paths, and neat layout will increase perceived ease of use of the RAs. Moreover, information about search progress and short response time will increase users' satisfaction with the RAs. Table 10 summarizes the relationships investigated in this section.

## Factors Related to Product, User, User–RA Interaction

The effects of RA use and RA characteristics on users' evaluations of RAs are contingent upon such user and product related factors as the type of products, users' expertise with the products or product categories, RA-user similarity, and user's familiarity with RAs. The following sections discuss the moderating effects of factors related to products, users, and user–RA interactions, as captured in propositions P22 through P27 and illustrated in Figure 3.

Product-Related Factors. User evaluations of RAs are not likely to be consistent across different product types. In the context of online shopping, products can be categorized into search products and experience products. On the one hand, currently available RAs (with text and static images) allow search products (but not experience products) to be adequately assessed. This gives users opportunities to appraise the usefulness of RAs. As such, users may perceive RAs for search products more useful than RAs for experience products. On the other hand, as discussed earlier, since the assessment of experience products is more complex than the evaluation of search products, consumers shopping for experience products are more likely to employ other-based (rather than own-based) decision-making processes. As a result, compared with consumers shopping for search products, those shopping for experience products may perceive RAs to be more trustworthy and thus be more inclined to follow the RAs' recommendations. It is therefore proposed that

P22: Product type moderates the effects of RA use on users' trust in and perceived usefulness of RAs. Users have higher trust in RAs for experience products and higher perceived usefulness of RAs for search products.

Aggarwal and Vaidyanathan (2003b) examined the perceived effectiveness (measured by user perceptions of the quality of RAs' recommendations, satisfaction with the recommendations, and intention to acquiesce to a recommendation) of two types of RAs (content-based RAs and collaborative-filtering RAs). They found that users perceived RAs to be more effective for search goods than for experience goods. Senecal (2003; see also Senecal and Nantel 2004) observed that consumers' were more likely to follow RAs' recommendations for experience products (wines) than for search products (calculators).

User-Related Factors. Research by Nah and Benbasat (2004) regarding knowledge-based systems revealed that expert and novice users exhibited different levels of criticality and involvement in their area of expertise. Not only were experts

<table><tr><td colspan="4">Table 10: The Impact of RA Characteristics on Users Evaluations of RA</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 2.2.Q2.2: How do characteristics of RAs influence users' evaluations of RAs?</td></tr><tr><td colspan="2">Relationship Between</td><td>Empirical Support</td><td>P</td></tr><tr><td colspan="4">RA Type</td></tr><tr><td>RA Type• Hybrid vs. Content-Filtering (or collaborative-filtering)• Compensatory vs. Non-compensatory</td><td>Trust,PerceivedUsefulness,Perceived Ease of Use, and Satisfaction</td><td>Users considered meta-recommender systems that combine collaborative-filtering and content-filtering more helpful than traditional recommender systems (using only collaborative-filtering technique) (Schafer et al. 2002).No empirical study available.</td><td>P14• P14a• P14b</td></tr><tr><td colspan="4">RA Input</td></tr><tr><td>Preference Elicitation Method</td><td>Perceived Ease of Use and Satisfaction</td><td>No empirical study available.</td><td>P15</td></tr><tr><td>Ease of Generating New/Additional Recommendations</td><td>Perceived Ease of Use and Satisfaction</td><td>Ease of generating new or additional recommendations improved estimations of the ease of use of an RA (Swearingen and Sinha 2001, 2002); giving users the capability to return to the preference specification stage at any time and restate their preferences increased their positive responses to RAs (Pereira 2000); an RA's system quality (i.e., ease of use, convenience of access, and reliability) had positive effect on users' decision making satisfaction (Bharati and Chaudhury 2004).</td><td>P16</td></tr><tr><td>User Control</td><td>Trust,Satisfaction,and PerceivedUsefulness</td><td>Increased user control over interaction with RA resulted in increased users' trust in and satisfaction with two content-filtering RAs (Pereira 2000); user-controlled RAs generated higher user satisfaction than did system-controlled RAs. Users of user-controlled RAs also thought the RA better understood their tastes and were more loyal to the system (McNee et al. 2003); control process was one of the top contributors to users' trust in a virtual salesperson (Komaik et al. 2005); RAs that were perceived by users as more restrictive were considered less trustworthy and useful by them (Wang 2005).</td><td>P17</td></tr><tr><td colspan="4">RA Process</td></tr><tr><td>Information about Search Progress</td><td>Satisfaction</td><td>Informing online shoppers about the progress of a search augmented shoppers' perceptions of the effort saved for them by an RA and, consequently, increased their satisfaction with the decision-making process before purchasing the product (Bechwati and Xia 2003).</td><td>P18</td></tr><tr><td>Response time</td><td>Satisfaction</td><td>Long wait time before receiving recommendations decreased users' preference for shopbots (Basartan 2001); the time taken by users to register and to receive recommendations from RAs did not have a significant effect on users' perceptions of the RA (Swearingen and Sinha 2001, 2002).</td><td>P19</td></tr><tr><td colspan="4">Table 10: The Impact of RA Characteristics on Users' Evaluations of RAs (Continued)</td></tr><tr><td colspan="2">Relationship Between</td><td>Empirical Support</td><td>P</td></tr><tr><td colspan="4">RA Output</td></tr><tr><td>Recommendation contentFamiliar recommendationsComposition of the list of recommendationsDetailed information about recommended productsExplanation</td><td>Trust,PerceivedUsefulness, and Satisfaction</td><td>Familiar recommendations played an important role in establishing user trust in an RA (Sinha and Swearingen 2001; Swearingen and Sinha 2001); unfamiliar recommendations lowered users' evaluations of a simulated music CD RA (Cooke et al. 2002).No empirical study availableUser trust in an RA increased when the RA provides detailed product information (Sinha and Swearingen 2001; Swearingen and Sinha 2001); a technique RAs can use to increase the attractiveness of unfamiliar recommendations was to provide users with additional information about a new product (Cooke et al. 2002); an RA's information quality (i.e., relevance, accuracy, completeness, and timeliness) had a significant effect on users' decision making satisfaction (Bharati and Chaudhury 2004).Explanations of an RA's reasoning logic strengthened users' trusting beliefs in the RA's competence and benevolence (Wang and Benbasat 2004a); the addition of explanation facilities increased the acceptance of MovieLens, an online collaborative-filtering movie RA (Herlocker et al. 2000); explanations enhanced perceptions of the transparency of an RA's inner workings, resulting in increased user trust in the RA (Sinha and Swearingen 2001, 2002; Swearingen and Sinha 2001, 2002; Wang 2005).</td><td>P20P20aP20bP20cP20d</td></tr><tr><td>Recommendation formatNavigation and layout</td><td>PerceivedUsefulness,Perceived Ease of Use, and Satisfaction</td><td>Interface features such as navigation and layout were most significant when they presented excess obstacles to users. Users were generally dissatisfied when too many clicks were required to obtain detailed information about recommended items, or when only a few recommendations were displayed on each screen (Sinha and Swearingen 2001; Swearingen and Sinha 2002); there was no significant relationship between navigational efficiency and user satisfaction (Bharati and Chaudhury 2004).</td><td>P21</td></tr></table>

less likely to be persuaded by a knowledge-based system than were novices, experts also found such a system less useful than did novices. In the context of RAs, the extent to which consumers have expertise in a particular product affects their evaluation of RAs for that product (King and Hill 1994). While RAs may be a necessity for consumers with low product expertise who require assistance in selecting and evaluating alternatives, individuals with high product expertise may perceive RAs as constraining and hampering their knowledge-based search, feeling that the RAs make them do something other than what they are capable of doing (Kamis and Davern 2004). As such, users with low product expertise are expected to evaluate RAs more favorably than are users with high product expertise. It is therefore proposed that

P23: Product expertise moderates the effects of RA use on users' evaluations of RAs (i.e., trust, perceived usefulness, perceived ease of use, satisfaction). The higher the product expertise of the users, the less favorable the users' evaluations of RAs.

Van Slyke and Collins (1996) noted that users' knowledge (including both domain knowledge and technical knowledge) is a key component in the trust-building process between the users and the RAs. Consumers with little product knowledge are more likely to develop trust when a salesperson recognizes their concerns, listens to their needs, and takes on the role of a consultant. Similarly, less knowledgeable consumers generally exhibit greater preferences for using web-based advisors than more knowledgeable consumers. Urban et al. (1999) compared subjects' relative preferences for two websites selling pick-up trucks online: in their experiment, one website was equipped with an RA, the other was not. Although the overall preferences for the two sites appeared to be about equal, consumers participating in the study who were not very knowledgeable about trucks expressed stronger preferences for an RA-enabled website, whereas those who were experts demonstrated stronger preferences for the website that lacked an RA. Thus, in the pick-up truck study, RA advice appeared to be more valuable to consumers with a lower level of product knowledge. Similarly, Spiekermann (2001), in an experiment that involved a three-dimensional anthropomorphic RA, observed that highly knowledgeable subjects were generally less satisfied with the RA and therefore less reliant on it for choosing products than less-knowledgeable subjects. Finally, examining the effects of product category knowledge on users' perceptions of online shopping tools, Kamis and Davern (2004) observed that product category knowledge was negatively related to perceived ease of use and perceived usefulness of the decision tools.

Product expertise is also expected to influence users' perceptions of different types of RAs. For instance, while experienced consumers can process attribute information efficiently, individuals with low product expertise will likely find such tasks more difficult (Pereira 2000). Attribute-oriented messages are found to be less informative to novices. Given the difficulty for individuals with low product expertise to enumerate the product attributes considered and gauge attribute importance, it is expected that they will find feature-based RAs uninformative but show positive affective reactions (i.e., trust, perceived usefulness and ease of use, satisfaction) to needs-based RAs. In contrast, for consumers with high product expertise, needs-based RAs may hamper their ability to specify exact attribute-related requirements and will thus be considered less useful and more difficult to use than feature-based RAs. Moreover, needs-based RAs have a knowledge component that translates users' needs to attribute specifications, which are in turn translated to recommendations. Users with high product expertise may consider needs-based RAs less transparent and thus less trustworthy than feature-based RAs that directly translate users' specifications to recommendations. As such, we expect consumers with high product expertise to favor feature-based RAs and those with lower product expertise to desire needs-based RAs.

Additionally, while experienced consumers tend to base their product choice on attribute information, individuals with low product expertise have been found to seek more summary information (Brucks 1985), given their lack of ability to process attribute information as efficiently. As such, collaborative-filtering RAs, which do not require users to specify product attribute preferences, are likely to appeal more to consumers with lower product expertise than to those with higher product expertise, who may perceive the absence of attribute information in the collaborative-filtering RAs as preventing them from using their knowledge in evaluating alternatives (Pereira 2000).

In sum, users' product expertise affects their evaluation of different types of RAs. It is therefore proposed that

P24: Product expertise moderates the effects of RA type on users' evaluations of RAs (i.e., trust, perceived usefulness, perceived ease of use, satisfaction). The higher the product expertise of the users, the more (less) favorable the users' evaluations of feature-based (needs-based) RAs. The higher the product expertise of the users, the more (less) favorable the users' evaluations of content-filtering (collaborative-filtering) RAs.

Focusing on users with low product knowledge, Komiak and Benbasat (2006) found that needs-based RAs led to users' beliefs that the RAs fully understood their true needs and took their needs as the RAs' own preferences, which in turn resulted in higher trust regarding the RAs' competence, benevolence, and integrity. Felix et al. (2001) further observed that users considered advice from needs-based RAs better suited for product novices than that from feature-based RAs. Stolze and Nart (2004) also found that users preferred RAs equipped with both needs-based and feature-based questions to those equipped with feature-based questions only. Pereira (2000) investigated the interaction effects between RA type (content-filtering versus collaborative-filtering) and users' product class knowledge. He found that users with high product class knowledge had more positive affective reactions (trust and satisfaction) to the content-filtering RAs than the collaborative-filtering ones. The reverse was true for users with low product class knowledge.

Factors Related to User–RA Interaction. The similarity between RAs and their users, user's familiarity with RAs, as well as the confirmation/disconfirmation of users' expectations will also moderate the effects of RA use on users' evaluations of the RAs.

In line with the theory of interpersonal similarity, individuals will be attracted to other individuals who exhibit similar characteristics (Byrne and Griffith 1969). They tend to identify with and have positive attitudes toward similar others (in terms of decision-making strategies, attitudes, tastes, goals, or preferences). McKnight et al. (1998) describe unit grouping as one type of cognitive categorization processes individuals use to develop trusting beliefs in new relationships. Unit grouping means “to put the other person in the same category as oneself” (p. 480). They argue that individuals who are grouped together tend to form more positive trusting beliefs about each other, because they tend to share common goals and values. Studies conducted by Brewer and Silver (1978) and Zucker et al. (1996) have likewise provided evidence that unit grouping quickly leads to highly positive trusting beliefs. In the context of RAs, similarities between users and RAs can promote a sense of group membership, and thus enhance users’ perceptions of attractiveness and trustworthiness of RAs. Moreover, insomuch as the main utility of the RAs lies in their capability to provide recommendations that match users’ preferences, similarities between users and RAs may result in recommendations that better fit users’ needs and thus contribute to more optimistic perceptions of the usefulness of the RAs. It is therefore proposed that

P25 User–RA similarity moderates the effects of RA use on users' trust in, satisfaction with, and perceived usefulness of RAs. The more the RAs are perceived to be similar to their users, the more they are considered to be trustworthy, satisfactory, and useful.

In their study of consumer acceptance of online movie RAs' advice, Gershoff et al. (2003) observed that when assessing how informative RAs were, consumers paid greater attention to past instances when they agreed with the RAs' opinions and ratings (an indication of similarity in tastes or preferences). Higher rates of agreement led to greater confidence in and greater likelihood of accepting the RAs' advice. Moreover, in addition to the overall agreement rate, consumers paid special attention to the intensity of the agreements (i.e., agreement on extreme, highly positive or negative, past opinions). Hess et al. (2005) observed that personality similarity between the users and the RAs contributed to increased involvement with the decision aid, which in turn resulted in increased user satisfaction with the RAs. Aksoy and Bloom (2001) also demonstrated that similarities in the significance vested in certain attributes by RAs and the significance that would be given to those attributes by users influenced user perceptions of the utility of the recommendations generated by the RA.

Individuals develop trust over time as they accumulate knowledge relevant to trust through their experiences with each other (Luwicki and Bunker 1995; McKnight et al. 1998). Familiarity is a necessary condition for developing knowledge-based trust. Therefore, users may judge the trustworthiness of RAs on the basis of their behavioral experiences. Repeated use of RAs, or RA training, not only familiarizes the user with the workings of the RAs but also enables them to assess the performance and consistency of the RAs. Sinha and Swearingen (2002) suggest that one way for a user to decide whether to trust recommendations is to examine the success of prior suggestions from the RAs, as evidence of the RAs' credibility. It is therefore proposed that

P26: User's familiarity with RAs moderates the effects of RA use on trust in the RAs. Increased familiarity with RAs leads to increased trust in the RAs.

Komiak and Benbasat (2006) observed that users' familiarity with the workings of RAs (e.g., the way to specify their preferences to the RAs, to access the explanations, and to review information on recommended items) allowed them to develop trust-relevant knowledge and to assess the consistency of the RAs' actions. Their empirical study demonstrated that familiarity increased users' trust in the RAs' benevolence and integrity, but it did not influence their trust in the RAs' competency.

According to the confirmation-disconfirmation paradigm, consumers form satisfaction based on their confirmation level and the expectation on which that confirmation was based (Bhattacherjee 2001). Confirmation occurs when perceived performance meets the expectation. Positive (negative) disconfirmation occurs when perceived performance exceeds (falls below) the expectation. Satisfaction is achieved when expectations are fulfilled (i.e., confirmed). Negative disconfirmation of expectations will result in dissatisfaction, whereas positive disconfirmation will result in enhanced satisfaction (Selnes 1998).

Applying confirmation-disconfirmation theory to RA context, we expect that the confirmation or the positive disconfirmation of users' expectations about RAs' functionalities and performance will enhance users' satisfaction with RAs, whereas the negative disconfirmation of their expectations will lead to dissatisfaction. It is therefore proposed that

P27: The confirmation/disconfirmation of expectations about RAs moderates the effects of RA use on users' satisfaction with the RAs. Confirmation or positive disconfirmation of users' expectations about RAs contributes positively to users' satisfaction with the RAs. In contrast, negative disconfirmation of users' expectations about RAs contributes negatively to users' satisfaction with the RAs.

No empirical study has directly investigated the effects of expectation (dis)confirmation on satisfaction with RAs. However, several IS researchers have called attention to the importance of managing consumer expectations in the design of RAs (Komiak and Benbasat 2006; Wang and Benbasat 2004b; West et al. 1999), suggesting that consumers might lose faith in and stop using an RA when it provides recommendations that do not meet with their expectations. Sinha and Swearingen (2001; Swearingen and Sinha 2002) found that, although users generally trusted RAs that provide familiar recommendations, they were often disappointed with RAs that provided too many familiar recommendations, because such RAs failed to help them broaden their horizons. Komiak and Benbasat (2004) suggest that RAs should use needs-based preference-elicitation questions as a way of managing users' expectations. Protocol analyses by Komiak et al. (2005) and Wang and Benbasat (2004b) revealed that expectation disconfirmation was an important factor contributing to distrust in RAs.

Summary. The propositions presented here provide the answer to research question (2.3): How do other factors (factors related to user, product, and user–RA interaction) moderate the effects of RA use and RA characteristics on users' evaluations of RAs? RAs for search (experience) products are considered more useful (trustworthy). Users with more product expertise tend to have less favorable perceptions of RAs in general. However, the higher the product expertise of the users, the more favorable their evaluations of feature-based and content-filtering RAs. In addition, the greater the RAs are perceived to be similar to their users and the greater the users' familiarity with the RAs, the higher the users' trust in the RAs. Finally, whereas confirmation (or positive disconfirmation) of users' expectations about RAs will enhance their satisfaction with the RAs, negative disconfirmation of their expectations will hamper their satisfaction with RAs. Table 11 summarizes the relationships investigated in this section.

## Provider Credibility

The effect of source credibility has been extensively investigated by researchers studying communications (Smith and

Shaffer 1991; Stamm and Dube 1994; Verplanken 1991). Sources that consumers attribute with high credibility appear to influence consumer attitudes more significantly (Goldberg and Hartwick 1990; Stamm and Dube 1994), and their efforts to persuade consumers are more effective (Lirtzman and Shuv-Ami 1986; Mondak 1990). In the context of this paper, source credibility refers to the credibility of RA providers, determined by the type and the reputation of the RA providers, both of which influence users' trusting beliefs in RAs' competence, benevolence, and integrity, as captured in proposition P28 and illustrated in Figure 3.

According to Doney and Cannon (1997), trust can develop through a transference process, in which “trust can be transferred from one trusted ‘proof source’ to another person or group with which the trustor has little or no direct experience” (p. 37). For example, a new salesperson representing a reputable company would benefit from buyers’ previous positive experiences with the company. A website that features an RA is referred to in this paper as the provider of the RA. The type and the reputation of the RA providers may affect users’ trusting beliefs in the RAs’ competence, benevolence, and integrity, because the user may transfer trust, or distrust, from the providers to the RAs provided at those websites. West et al. (1999) call attention to the fact that characteristics of a website provide important cues for building trust in an online shopping advisor. Urban et al. (1999) also state that trust in a specific website is the first stage toward development of trust in an expert advisor; trust cannot be vested in an expert advisor until trust has been established toward the Internet and the website that provides the advisor.

RAs are embedded either in the websites of online vendors (e.g., Amazon.com) or in third party websites (e.g., Priceline.com). Prior research (see Senecal 2003; Senecal and Nantel 2004) has shown that consumers tend to discredit recommendations from endorsers if they suspect that the latter have non-product related motivations to recommend a particular product (e.g., overstocking of that product). Therefore, as endorsers of RAs' recommendations, independent third party websites may be perceived by consumers as less biased and more credible than vendor websites.

Moreover, McKnight et al. (1998) describe reputation categorization, the assignment of attributes to another person based on second-hand information about the person, as one type of process individuals use to develop trusting beliefs in a new relationship. Individuals with good reputations are categorized as trustworthy individuals who are competent, benevolent, honest, and predictable. Individuals will quickly develop trusting beliefs about a person with a good reputation, even without firsthand knowledge of them. Applying this reputation categorization in the context of RAs, we posit that users will consider reputable providers more trustworthy than those that are unknown or had a bad reputation, and subsequently they will transfer that trust to the RAs featured by the providers. For instance, a consumer may trust the RA at Amazon.com more than a similar RA at an unknown website.

<table><tr><td colspan="4">Table 11. The Impact of Factors Related to User, Product, and User–RA Interaction on Users' Evaluations of RA</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 2.3.Q2.3: How do other factors (i.e., factors related to user, product, and user–RA interaction) moderate the effects of RA use and RA characteristics on users' evaluations of RAs?</td></tr><tr><td>Moderator</td><td>Moderated Relationship</td><td>Empirical Support</td><td>P</td></tr><tr><td colspan="4">Product-Related Factors</td></tr><tr><td>Product Type (search vs. experience)</td><td>RA Use on Trust and Perceived Usefulness</td><td>Users perceived RAs to be more effective for search goods than for experience goods (Aggarwal and Vaidyanathan 2003b); consumers' were more likely to follow RA's recommendations for experience products than for search products (Senecal 2003; Senecal and Nantel 2004).</td><td>P22</td></tr><tr><td colspan="4">User-Related Factors</td></tr><tr><td>Product Expertise</td><td>RA Use on Trust, Perceived Usefulness, Perceived Ease of Use, and Satisfaction</td><td>Less knowledgeable consumers expressed stronger preferences for an RA-enabled website, whereas those who were experts evinced stronger preferences for the website that lacked an RA (Urban et al. 1999); highly knowledgeable subjects were generally less satisfied with the RA and therefore less reliant on it for choosing products than less-knowledgeable subjects (Spiekermann 2001); product category knowledge was negatively related to perceived ease of use and perceived usefulness of the decision tools (Kamis and Davern 2004).</td><td>P23</td></tr><tr><td>Product Expertise</td><td>RA type on Trust, Perceived Usefulness, Perceived Ease of Use, and Satisfaction</td><td>For users with low product knowledge, a needs-based RA resulted in higher trust (Komiak and Benbasat 2006); users considered advice from needs-based RAs better suited for product novices than that from feature-based RAs (Felix et al. 2001); users preferred RAs equipped with both needs-based and feature-based questions to those equipped with feature-based questions only (Stolze and Nart 2004); users with high product class knowledge had more positive affective reactions (trust and satisfaction) to the content-filtering RAs than the collaborative-filtering ones. The reverse was true for users with low product class knowledge (Pereira 2000).</td><td>P24</td></tr><tr><td colspan="4">User–RA Interaction</td></tr><tr><td>User–RA Similarity</td><td>RA Use on Trust, Perceived Usefulness, and Satisfaction</td><td>When assessing how informative an RA was, consumers paid greater attention to past instances when they had agreed with the RA's opinions and ratings. Higher rates of agreement led to greater confidence in and greater likelihood of accepting an RA's advice (Gershoff et al. 2003); personality similarity between the user and the decision aid contributed to increased involvement with the decision aid, which in turn resulted in increased user satisfaction with the decision aid (Hess et al. 2005); user–RA similarity in attribute weighting had a significant impact on user perceptions of the utility of the recommendations generated by the RA (Aksoy and Bloom 2001).</td><td>P25</td></tr><tr><td>User's Familiarity with RAs</td><td>RA Use on Trust</td><td>The user's familiarity with the workings of an RA increased trust in an RA's benevolence and integrity, but not its competency (Komiak and Benbasat 2006).</td><td>P26</td></tr><tr><td>Confirmation/ Disconfirmation of Expectations</td><td>RA Use on Satisfaction</td><td>No empirical study available.</td><td>P27</td></tr><tr><td colspan="4">Table 12. The Impact of RA Use and Provider Credibility on Users' Evaluations of RA</td></tr><tr><td colspan="4">The propositions in this table provide answers to research question 2.4.Q2.4: How does provider credibility influence users' evaluations of RAs?</td></tr><tr><td colspan="2">Relationship Between</td><td>Empirical Support</td><td>P</td></tr><tr><td>Provider Credibility (Provider Type and Provider Reputation)</td><td>Trust</td><td>The type of a website (i.e., seller, commercially linked third-party, or independent third-party) that provides an RA did not affect the perceived trustworthiness of the RA (Senecal 2003; Senecal and Nantel 2004).</td><td>P28</td></tr></table>

In sum, the type and reputation of RA providers determine their credibility, which in turn influences users' trust in the RAs. It is therefore proposed that

P28: Provider credibility, determined by the type of RA providers and the reputation of RA providers, influences users' trust in RAs. RAs provided by independent third party websites are considered more trustworthy than those provided by vendors' websites. RAs provided by reputable websites are considered more trustworthy than those provided by websites that are unknown or non-reputable.

Senecal (2003; see also Senecal and Nantel 2004) identified three types of websites: seller, commercially linked third-party, and independent third-party. She hypothesized that the type of the website that provides an RA will affect the perceived trustworthiness of the RA: the RA at an independent third-party website will be perceived as the most trustworthy, while the RA at a seller's website will be perceived as the least trustworthy. However, her experimental data did not support this hypothesis. We believe that this failure may be a result of the limited number of alternatives (only four) available in her study for each product, as well as the relatively low value of the products (calculators and wine) involved in the experiment. No other reported study has directly examined the effect of provider credibility on trust in RAs.

Summary. Proposition P28 provides answers to research question (2.4): How does provider credibility influence users' evaluations of RAs? Users' trust in RAs is proposed to be influenced by the type and reputation of RA providers, as summarized in Table 12. Users will have higher trust in RAs provided by independent third party websites than those provided by vendors' websites. Additionally, they will have higher trust in RAs provided by reputable websites than those provided by unknown or non-reputable websites.

## Relationships among Other Variables

This paper focuses on investigating the effects of RA user, RA characteristics, and other factors (i.e., factors related to user, product, user–RA interaction, and provider credibility) on two groups of outcomes of RA use: (1) consumer decision-making processes and outcomes and (2) users' evaluations of RAs (i.e., perceived usefulness, perceived ease of use, trust, and satisfaction). The relationships between the two groups of outcome variables, among the variables in each group, as well as between the outcome variables and RA reuse intention and reuse behavior, albeit important, are beyond the scope of this paper. Although empirical investigations of these relationships can be found in general IS literature, there is little discussion in specific RA literature, which is the focus of this review. Therefore, no proposition is stated for these relationships in this section. However, for compatibility with prior IS work, such relationships are highlighted by the dashed lines in Figure 1 and briefly explained below.

Prior research (e.g., Davis and Kottemann 1994; Kottemann and Davis 1994) reveals that active involvement of users in interacting with a decision support system may create an “illusion of control” (defined as a person’s expectation of success on a task that is inappropriately higher than objective circumstances warrant—Langer 1975) causing users to overestimate its effectiveness, resulting in an effort—confidence link and a related mismatch between actual performance (e.g., objective decision quality) and performance beliefs (e.g., confidence belief and usefulness belief). Therefore, the relationships between decision effort and decision quality as well as between decision quality and perceived RA usefulness will be influenced by users’ illusion of control.

There is also ample empirical evidence in the IS literature supporting the causal link from subjective evaluations (such as trust, perceived usefulness, perceived ease of use, and satisfaction) to adoption intention and adoption behavior (Davis 1989; Gefen et al. 2003; Taylor and Todd 1995; Venkatesh 2000). Several researchers have developed integrated models of TAM, trust, and satisfaction. For instance, integrating trust, risk, and TAM, Pavlou (2003) and Gefen et al. (2003) hypothesized about and empirically confirmed the links from trust to perceived usefulness and adoption intention. Wixom and Todd (2005) integrated technology acceptance and satisfaction literature and empirically demonstrated that system satisfaction and information satisfaction contribute to perceived ease of use and perceived usefulness, respectively. Wang and Benbasat (2005) have extended the integrated trust–TAM model (Gefen et al. 2003) to online RA adoption and proven the causal link from trust to adoption intention. Abstracting from all of this literature, we expect that trust, perceived usefulness, perceived ease of use, and satisfaction will positively contribute to users' intentions to use RAs in the future and, subsequently, their future use of RAs. In addition, we expect to observe the following relationships: satisfaction → perceived ease of use; perceived ease of use → trust; perceived ease of use, trust, and satisfaction → perceived usefulness.

Only a few studies have directly investigated the relationship between perceptions of RAs and intention to adopt the RAs. Wang and Benbasat (2005) found that consumers' initial trust not only directly influenced their intention to adopt RAs but it also exerted an indirect effect on such intention by enhancing perceptions of the usefulness of the RAs. Users' perceptions of the ease of use of RAs, however, did not have a significant impact on their adoption intention. Komiak and Benbasat (2006) distinguished between two levels of RA use intentions: intention to use RAs as decision aids (i.e., to let RAs narrow down product choices) and intention to use RAs as delegated agents (i.e., to let RAs make decisions on behalf of consumers). The results of their experimental study of a digital camera RA demonstrated that both cognitive trust and emotional trust were significant predictors of consumer intention to use RAs as decision aids. Additionally, emotional trust fully mediated the impact of cognitive trust on the intention to use RAs as delegated agents.

## Discussion and Concluding Comments

In this paper, we have presented a set of theory-based propositions concerning the outcomes of RA use and RA adoption intentions in e-commerce settings. The propositions provide answers to the two research questions that initially motivated the paper. $^{25}$ The answers should be of interest to academic researchers, designers of RAs, and current or potential providers of RAs. Next, we present the contributions of this study and identify areas for future research.

## Contributions to Research

Prior research on RAs has focused mostly on developing and evaluating different underlying algorithms that generate recommendations. This paper has attempted to identify other important aspects of RAs, namely RA use, RA characteristics, provider credibility, and factors related to product, user, and user–RA interaction, which exert influence on users' decision making processes and outcomes as well as their evaluations of RAs. One of our objectives was to go beyond generalized models such as TAM to identify the RA-specific features, such as RA input, process, and output design characteristics that influence users' beliefs and evaluations, including usefulness and ease-of-use concerning RA use.

Using the conceptual model illustrated in Figure 1 as a starting point, we derived 28 propositions concerning the outcomes of RA use from five main theoretical perspectives, including theories of human information processing, the theory of interpersonal similarity, the theories of trust formation, TAM, and the theories of satisfaction. We have also justified the propositions with existing empirical work in RAs (when available). Tables 7 through Table 12 provide summaries of the propositions that have been presented and empirical evidence (if available) associated with each of them. As delineated in Table 13, the majority of the propositions are supported fully (including 13 propositions and four sub-propositions) or partially (including three propositions and four sub-propositions) by available empirical evidence. However, there also exist three propositions and two sub-propositions that lack conclusive empirical support, in addition to two propositions that were not bolstered by available empirical studies, which signals the existence of contingency factors not yet uncovered and/or problems with experimental designs and RA implementations. As such, further theorizing or more rigorous experimental designs are needed to investigate the proposed relationships. Moreover, there are two propositions and four sub-propositions that are yet to be empirically tested. Table 13 highlights the discrepancy between what we know and what we need to know, pinpointing venues of future research to close this breach, as discussed further in the “Suggestions for Future Research.”

<table><tr><td colspan="3">Table 13. Summary of Empirical Support for Propositions</td></tr><tr><td></td><td>Propositions</td><td>Sub-Propositions</td></tr><tr><td>Fully Supported</td><td>P5, P7, P8, P10, P11, P16, P17, P18, P22, P23, P24, P25, P26</td><td>P6a, P20a, P20c, P20d</td></tr><tr><td>Partially Supported</td><td>P4, P12, P13</td><td>P3a, P3b, P6b, P14a</td></tr><tr><td>Inconclusively Supported</td><td>P2, P19, P21</td><td>P1a, P1b,</td></tr><tr><td>Not Supported</td><td>P9, P28</td><td></td></tr><tr><td>No Empirical Study Available</td><td>P27, P15</td><td>P1c, P3c, P14b, P20b</td></tr></table>

Note: The shaded areas are those in which promising future studies can be conducted.

To keep our conceptual model manageable, we have not intended for it to encompass all of the constructs discussed in prior RA studies. Although an examination of the empirical studies reviewed in this paper reveals a few constructs (e.g., users' cost–benefit consideration, multimedia vividness) outside of the research framework that we have proposed, they either do not appear to influence outcomes of RA use or their effects are still not well-understood. For instance, it is possible that cost–benefit considerations associated with RA use might influence users' perceptions of and interactions with RAs. Spiekermann (2001) hypothesized that perceived costs and benefits of searching for product information may affect users' interactions with RAs. However, experimental data has not supported her hypothesis. Neither costs nor benefits were found to influence users' willingness to interact with RAs. A few other studies (Komiak and Benbasat 2006; Wang and Benbasat 2004a) have included effort–quality preference as covariates in their analyses, but none of these constructs were found to be significant. Similarly, Hess et al. (2005) hypothesized about the positive impact of multimedia vividness on user involvement with RAs, only to be surprised with a significant hard-to-explain negative effect.

Based on the fact that (1) the conceptual model presented in Figure 1 integrates most of the constructs, as well as the interrelationships among the constructs, identified in previous research in RAs, and (2) the model and propositions derived from five different theoretical perspectives not only summarize prior empirical effort but also provide directions for future research (as illustrated in Table 13 and discussed further below), we conclude that the conceptual model and the theoretical propositions provide an adequate framework to account for phenomena relating to the outcomes of RA use in e-commerce.

## Contributions to Practice

In this section, prescriptive guidelines are suggested to practitioners concerning the design and implementation of RAs in e-commerce websites, following from our improved understanding of such phenomena. It must be noted, however, that such prescriptions are dependent on the empirical validation of the appropriate propositions.

This review has identified two sets of factors affecting consumers' decision-making processes and outcomes and users' evaluations of e-commerce RAs: (1) factors that are under the control of RA designers or providers, and (2) those that are not.

The following factors can be controlled to a certain extent by developers of RAs or websites providing RAs, hence they are suggested to be implemented (or, in the case of RA characteristics, be incorporated into the design of RAs) to improve users' shopping decision-making and enhance their positive evaluation of the RAs.

\- Insomuch as the use of RAs generally results in increased decision quality (P2) and reduced decision effort (P1), RAs should be implemented in e-commerce websites to assist consumers with shopping decision making.

\- Explicit preference elicitation methods are considered more transparent by users and lead to higher decision quality (P4). However, implicit preference elicitation methods demand less decision effort (P4) and are considered easier to use and more satisfactory (P15). It is suggested that explicit and implicit preference elicitation methods be integrated so as to balance quality with effort.

\- The provision of explanations augments perceptions of the transparency of RAs' reasoning logic and increases users' trust in and satisfaction with the RAs (P20d). As such, explanations should be provided for how the RAs derive their recommendations.

\- Since different types of RAs (1) result in different decision-making processes and outcomes as well as in different user evaluations (P3 and P14) and (2) appeal to users of different product expertise (P24), it is suggested that multiple RAs be provided (if cost permits) to give different users the flexibility of choosing the desired RAs to assist in their shopping tasks.

\- Inasmuch as familiar recommendations increase users' trust, RAs should present unfamiliar recommendations in the context of familiar ones (as indicated by sub-propositions P20a and P20b). To be able to provide familiar recommendations, RAs must track and apply users' shopping history, feedback, and Internet navigation patterns. A possible way to facilitate the provision of familiar recommendations to new users is to generate recommendations known to be very popular.

\- The provision of detailed information about RAs' recommendations increases users' trust in, perceived usefulness of, and satisfaction with the RAs (as indicated by sub-proposition P20c). The information can include product descriptions, expert reviews, and other consumers' evaluations. This information must also be easily accessible by the users. Thus, clear navigational paths and clear layout (P21) are very important design considerations. Furthermore, RAs should provide their recommendations in the format of sorted lists (P7a) but avoid presenting too many product recommendations, particularly on a single screen (P7b).

\- RA designers should allow users to control their interactions with the RAs (P17) and provide capabilities for them to generate new or additional recommendations easily (P16). Additionally, the RAs should keep their response times to a minimum (P19). When the users are waiting to receive recommendations, RAs should display information about their search progress to demonstrate their effort to the users (as indicated by proposition P18).

\- RAs can have greater influence on product choice, decision quality, and/or decision effort for complex products and experience products (P8, P9, and P22); thus online retailers are advised to provide RAs for such products, although the implementation of RAs for experience products may require extra investment in advanced multimedia presentation technologies. Since current Internet technology allows search products to be adequately assessed prior to purchase, the RAs for such products are generally considered more useful than those for experience products (P22). Therefore, retailers of search products are advised to incorporate RAs in their online stores.

\- Similarity between RAs and their users simplifies and reduces product search, improves decision quality, and increases trust in, perceived usefulness of, and satisfaction with the RAs (P13 and P25). RAs can be made “similar” by the use of needs-based questions that elicit users’ product preferences and their choices of the decision strategies the users prefer (e.g., elimination by aspect), when such information is available. RAs can also be designed to assume personalities (e.g., extraversion or introversion) similar to those of their users, as illustrated by Hess et al. (2005).

\- The confirmation/disconfirmation of users' expectations about RAs influences their satisfaction with the RAs (P27). West et al. (1999) suggest that one way to manage consumer expectations regarding RAs' performance is to communicate the RAs' limitations and requirements (e.g., the kind and amount of user input required) to customers before they begin using the RAs, so that they can set realistic expectations for the agents. For instance, MovieCritic, a movie RA, educates users about the importance of providing input to the RA, and it provides movie recommendations only after users have rated at least 12 films and answered a battery of questions. It manages users' expectations by informing them that the quality of its product recommendations is related to the quality and quantity of input users provide to the system. Spiekermann and Paraschiv (2002) argue that, when conceiving a system for commercial purposes, it is important to consider the specific expectations of potential buyers regarding an interface's functionalities. They propose a "user-centric" approach to RA design (i.e., an approach to RA design that emphasizes the users' points of view) in order to motivate user interaction with RAs.

\- The type and reputation of RA provider can increase users' trust in the RA (P28). RA providers are advised to implement such mechanisms as trust-assuring arguments (Kim and Benbasat 2003) and third party seals to signal their competence, benevolence, and integrity to RA users.

\- Since RAs can serve as “double agents,” the product attributes included in the RA’s preference-elicitation interface (P5), the recommendations generated by the RAs (P6a), and the utility scores or predicted ratings for recommended alternatives (P6b) may exert significant impact on consumers’ decision processes and decision outcomes. However, retailers should avoid manipulating these factors in their own interest and misleading consumers intentionally. It is much easier to destroy than to establish consumer trust and confidence.

On the other hand, although the following user-related factors also have significant impact on the outcomes of RA use and RA adoption intention, they are comparatively difficult to control a priori:

\- Users' familiarity with the operations of RAs can increase their trust in the RAs (P26).

\- Users' product expertise affects their perceptions (P23). Novices consider RAs more useful and trustworthy than do experts.

\- Users' perceptions of risk attendant to particular products affect their shopping performance and their perceptions of RAs. RAs have the greatest impact on decision quality and information search under conditions of high product risk (P13).

## Suggestions for Future Research

## Testing the Conceptual Model

Our conceptual model presented Figure 1 is a causal model and its propositions should be best tested as such. The impacts of RA use, RA characteristics, and other contingency factors on users' decision-making processes and outcomes, as well as on their evaluations of RAs, would preferably be tested utilizing the laboratory experiment method to facilitate the manipulation of independent variables (in particular, different RA characteristics) and the control of extraneous factors. In fact, most of the empirical studies reported in this paper have used the laboratory experimental method. Field experiments are also possible when partnerships with e-commerce RA providers can be fostered.

Since the complexity of the conceptual model makes it infeasible to validate the model as a whole, it is suggested that the higher-level conceptual model (Figure 1), and even the two lower-level models (Figures 2 and 3), be broken into smaller and more manageable parts, allowing different RA characteristics as well as user- and product-related factors to be tested one small group at a time. For example, propositions P17, P19, P20, P22, P25, and P28 can be tested as a group to validate the proposed effects of three RA characteristics associated with input, process, and output, respectively (i.e., user control, response time, and recommendation content), one product-related factor (i.e., product type), one user–RA interaction factor (i.e., user–RA similarity), and provider credibility on users' evaluations of RAs. Whereas studies on one period of use are appropriate for validating most of the propositions, a longitudinal approach may be required to test the propositions related to user–RA interaction factors such as users' familiarity with RA and the confirmation/disconfirmation of users' expectations.

As noted above, part of our conceptual model has already been validated by prior RA research. However, in many cases, even fully validated propositions have received only limited support (e.g., P6a, P7), demonstrating a lack of knowledge accumulation in this area. As such, additional testing of these propositions is suggested. Moreover, further validation should be conducted in areas where no empirical investigations have been undertaken or where unexpected or inconclusive results have been obtained in prior endeavors, as demonstrated in Table 13.

## Developing the Conceptual Model

Our review suggests important areas for further theoretical development. First, this paper has investigated only a limited number of user-related factors. Future studies should investigate such additional factors as control propensity (i.e., the extent to which an individual is naturally inclined to control other parties in general), trust propensity, effort and quality preferences, cost–benefit analysis, and susceptibility to interpersonal influence. For instance, users' effort and quality preference may determine their preference for different types of RAs: whereas individuals who favor better decision quality may prefer to use compensatory, hybrid, or manual–ephemeral RAs, those who desire less effort may choose to employ non-compensatory, pure collaborative-filtering or content-filtering, or automatic–permanent RAs.

In addition, this review focuses on two major outcomes of RA use—consumer decision making and users' evaluations of RAs—in a parallel fashion, without hypothesizing about the interrelationships between the two groups of dependent variables or among the variables in each group. Further theorization is needed to explore the between-group relationships, as well as those among the variables in the consumer decision making group, given that the relationships among the four user evaluation variables (i.e., perceived usefulness, perceived ease of use, trust, and satisfaction) have already been extensively studied in prior literature. In addition to the relationships highlighted with dashed lines in Figure 1 and discussed in the section “Relationships among Other Variables,” that is, the relationships between decision effort and decision quality, as well as between decision quality and perceived RA usefulness, other pair-wise relationships (e.g., trust and decision effort, satisfaction and decision quality, trust and decision quality) can also be explored. For instance, when users have trusting beliefs in RAs' competence, benevolence, and integrity, they may engage in less product search (an indicator of reduced decision effort), which, according to Diehl (2003), will enhance their decision quality in an ordered environment. They may also have greater confidence in their decisions, an indicator of decision quality. Conversely, increased decision quality and reduced decision effort during trial use of RAs may contribute to users' positive perceptions of the RAs. Moreover, there may exist strong correlations between decision quality and satisfaction, as demonstrated by Parikh and Fazlollahi (2002).

The current conceptual model can be expanded not only with variables discussed in prior RA studies (e.g., users' cost-benefit consideration, multimedia vividness), but also with those suggested by pervious DSS research in general. For instance, task is identified by Eierman et al. (1995) as an important factor affecting user behavior and performance; it is defined "as the set of functions that a working person, unit, organization is expected to fulfill or accomplish. It is the job that is to be done using the decision support system" (p. 5). The construct is not included in our conceptual model since the "task" is fixed in this paper (i.e., to purchase a product with/without an RA individually). However, this construct may become relevant when investigating RA characteristics needed for online shopping tasks of different complexity and structuredness (e.g., individual shopping versus group shopping, or shopping for oneself versus shopping for someone else). An additional construct worth further investigation is perceived risk. The concept of perceived risk is founded on a large body of literature developed in marketing since the 1960s (Bauer 1960; Cunningham 1967; Dowling and Staelin 1994; Jacoby and Kaplan 1974). It is defined as "an assessment consumers make of the consequences of making a purchase mistake as well as of the probability of such a mistake to occur" (Spiekermann and Paraschiv 2002, p. 265). Spiekermann and Paraschiv have identified two different types of perceived risks in an online environment: product risks (which consist of functional, financial, socio-psychological, and delivery risks $^{26}$ ) and privacy risks. Whereas perceived product risk is part of our conceptual model, the impact of perceived privacy risk on the two groups of outcome variables should be explored in the future.

Finally, many IS researchers have emphasized the importance of studying inhibitors to use. For instance, Parthasarathy and Bhattacherjee (1998) have called attention to the importance of examining why customers choose to discontinue services to which they subscribe. Venkatesh and Brown (2001) have identified a set of critical barriers (e.g., rapid change, high cost, and lack of knowledge) to home PC adoption. Cenfetelli and Benbasat have developed an integrated model of usage inhibitors, which include beliefs about information, systems, and services (Cenfetelli 2004; Cenfetelli and Benbasat 2003). Despite their apparent advantages, RAs are currently adopted by only about 10 percent of shoppers, according to a study by Montgomery et al. (2004), which lists lack of awareness, lack of benefits, lack of information, slow response time, and poor interface design as the reasons why people do not use RAs. Previous literature about RAs has focused mostly on factors that contribute to better decision-making quality, trust, and adoption of RAs. Future research effort should be extended to uncovering more factors hampering users' positive evaluation of RAs and inhibiting their use intentions.

## Exploring New RA Design Issues

Only RA characteristics discussed in prior conceptual or empirical work are included in our model to keep its complexity manageable. Future research may explore other RA design issues. First, with the emergence of new characteristics related to RAs' input, process, and output design, the impact of such characteristics on users' decision-making processes and outcomes, as well as on their evaluation of RAs should be investigated. For instance, Jiang and Benbasat (2005) have advocated the provision of virtual product experience (VPE) to simulate direct experience. Enabled by visual control (which enables online consumers to manipulate product images, for example, to move, rotate, and magnify a product's image so as to view it from different angles and distances) and functional control (which enables consumers to sample the different functions of products) technologies, VPE has been shown to increase consumers' product understanding, brand attitude, purchase intention, and affect, as well as to decrease their perceived risks (Griffith and Chen 2004; Jiang and Benbasat 2005; Li et al. 2003; Suh and Lee 2005). Jiang et al. (2005) have designed a "multimedia-based interactive advisor" that integrates visual control and functional control with product recommendation technologies. It will be interesting to explore whether such RAs can improve users' understanding of product features, promote their trust in the RAs, and enhance their shopping enjoyment. Qiu (2005) proposes the investigation of the potentials of enhancing users' social experience from interacting with RAs, with the help of emerging multimedia technologies, such as animated face and speech output. Specifically, he aims to explore how RAs' multimedia and anthropomorphic interfaces shape and affect users' perceptions of social presence, their trusting beliefs toward the RAs, and perceived enjoyment from interacting with the agents.

Additionally, Brusilovsky and Tasso (2004) advocate the abandonment of the typical “one-size-fits-all” approach by providing better mechanisms for gathering users’ information needs. Current RAs provide the same set of preference-elicitation questions to all users, which results usually in an extended list of questions intended to cover all of the important aspects of products. However, not all aspects of a given product conveyed by the questions are likely to be important to all users; sets of questions of importance to users of different gender, expertise, or goals are usually not uniform. For instance, according to a CNET report on the gender gap in digital camera purchases, $^{27}$ men and women are different in their buying motivations and the features they desire. It is important to investigate whether or not RAs that are context-sensitive, customizing preference-elicitation questions according to users’ backgrounds, expertise, and current goals, are more likely to be adopted for use.

Furthermore, previous studies on RAs have treated them as stand-alone systems, independent of other functionalities provided by their hosting websites. Inasmuch as the ultimate purpose of RAs is to facilitate consumers' online shopping, and considering that RAs are just one of the technologies employed by websites to either provide more information to customers or to try to convert browsers into buyers, it makes sense to study RA effectiveness as part of an overall interactive online system. For instance, a "live help" function with instant chatting and co-browsing capabilities (Qiu and Benbasat 2005; Zhu 2004) can be incorporated into RAs to enable customer service representatives to help consumers answer difficult preference-eliciting questions, to "push" pages containing recommended products or detailed information about those products to the customers (e.g., expert reviews or other customers' testimonies), or to direct customers through the entire shopping process. Such RAs will have the potential to assist customers in all six stages of online shopping processes (needs identification, product brokering, merchant brokering, negotiation, purchase and delivery, product services, and product evaluation), as identified by Maes et al. (1999), whereas currently available RAs focus primarily on product brokering and merchant brokering. We believe that this is an important area for future studies.

As indicated by the recent EBay acquisition of Shopping.com (a successful comparison shopping website), recommendation technologies are considered to be a valuable competitive advantage to e-commerce leaders. By providing product recommendations based on consumers' preferences, RAs have the potential to support and improve the quality of the decisions consumers make when searching for and selecting products online as well as to reduce the information overload facing consumers and the complexity of online searches. Despite such apparent advantages, RAs are currently used by only 10 percent of online shoppers (Montgomery et al. 2004). Based on a comprehensive review of empirical RA research conducted in multiple disciplines, this paper organizes the knowledge about the effective design and development of RAs and provides advice to IS practitioners on how to improve RA design, in addition to identifying those areas in which research is needed to advance our understanding of RA use and impact

## Acknowledgments

We would like to thank the Natural Science and Engineering Research Council of Canada (NSERC) and the Social Science and Humanities Research Council of Canada (SSHRC) for their support of this research. We are grateful to the senior editor, associate editor, and three anonymous reviewers whose comments have improved this paper considerably.

## References $^{28}$

Adomavicius, G., and Tuzhilin, A. “Recommendation Technologies: Survey of Current Methods and Possible Extensions,” MISRC Working Paper 03-29, MIS Research Center, University of Minnesota, Minneapolis, MN, 2003.

\*Aggarwal, P., and Vaidyanathan, R. “Eliciting Online Customers’ Preferences: Conjoint vs Self-Explicated Attribute-Level Measurements,” Journal of Marketing Management (19:1-2), 2003a, pp. 157-177.

\*Aggarwal, P., and Vaidyanathan, R. “The Perceived Effectiveness of Virtual Shopping Agents for Search vs. Experience Goods,” Advances in Consumer Research (30:1), 2003b, pp. 347-348.

\*Aksoy, L., and Bloom, P. N. “Impact of Ordered Alternative Lists on Decision Quality: The Role of Perceived Similarity,” paper presented at the Society for Consumer Research Winter Conference, Scottsdale, AZ, February 15-17, 2001.

Ansari, A., Essegaier, S., and Kohli, R. “Internet Recommendation Systems,” Journal of Marketing Research (37:3), 2000, pp. 363-375.

Ariely, D., Lynch, J. G., and Aparicio, M. “Learning by Collaborative and Individual-Based Recommendation Agents,” Journal of Consumer Psychology (14:1-2), 2004, pp. 81-95.

Bajaj, A., and Nidumolu, S. R. “A Feedback Model to Understand Information System Usage,” Information and Management (33:4), 1998, pp. 213-224.

Balabanovic, M., and Soham, Y. “Fab: Content-Based, Collaborative Recommendation,” Communications of the ACM (40:3), 1997, pp. 66-72.

\*Basartan, Y. “Amazon Versus the Shopbot: An Experiment About How to Improve the Shopbots,” Unpublished Ph.D. Summer Paper, Carnegie Mellon University, Pittsburgh, PA, 2001.

Bauer, R. A. “Consumer Behavior as Risk Taking,” in Dynamic Marketing for a Changing World, R. Hancock (ed.), American Marketing Association, Chicago, 1960, pp. 389-398.

\*Bechwati, N. N., and Xia, L. “Do Computers Sweat? The Impact of Perceived Effort of Online Decision Aids on Consumers’ Satisfaction with the Decision Process,” Journal of Consumer Psychology (13:1-2), 2003, pp. 139-148.

Bellman, S., Johnson, E. J., Lohse, G. L., and Mandel, N. "Designing Marketplaces of the Artificial with Consumers in Mind: Four Approaches to Understanding Consumer Behavior in Electronic Environments," Journal of Interactive Marketing (20:1), 2006, pp. 21-33.

Benbasat, I., DeSanctis, G., and Nault, B. R. “Empirical Research in Managerial Support Systems: A Review and Assessment,” in Recent Developments in Decision Support Systems, A. B. Whinston (ed.), Springer-Verlag, Berlin, 1991, pp. 383-437.

Benbasat, I., and Todd, P. “The Effects of Decision Support and Task Contingencies on Model Formulation: A Cognitive Perspective,” Decision Support Systems (17:4), 1996, pp. 241-252.

Benbasat, I., and Todd, P. “The Use of Information in Decision Making: An Experimental Investigation of the Impact of Computer-Based Decision Aids,” MIS Quarterly (16:3), 1992, pp. 373-393.

Benbasat, I., and Zmud, R. W. “The Identity Crisis Within the IS Discipline: Defining and Communicating the Discipline’s Core Properties,” MIS Quarterly (27:2), 2003, 183-194.

Bettman, J. R., Luce, M. F., and Payne, J. W. “Constructive Consumer Choice Processes,” Journal of Consumer Research (25), December 1998, pp. 187-217.

\*Bharati, P., and Chaudhury, A. “An Empirical Investigation of Decision-Making Satisfaction in Web-Based Decision Support Systems,” Decision Support Systems (37:2), 2004, pp. 187-197.

Bhattacherjee, A. “Understanding Information Systems Continuance: An Expectation-Confirmation Model,” MIS Quarterly (25:3), 2001, pp. 351-370.

Breese, J. S., Heckerman, D., and Kadie, C. “Empirical Analysis of Predictive Algorithms for Collaborative Filtering,” in Proceedings of the 14 $^{th}$ Conference on Uncertainty in Artificial Intelligence, G. F. Cooper and S. Moral (eds.), Morgan Kaufmann, San Francisco, April 1998, pp. 43-52.

Brewer, M. B., and Silver, M. “Ingroup Bias as a Function of Task Characteristics,” European Journal of Social Psychology(8:3), 1978, pp. 393-400.

Brown, D. L., and Jones, D. R. “factors That Influence Reliance on Decision Aids: A Model and an Experiment,” Journal of Information Systems (12:2), 1998, pp. 75-94.

Brucks, M. “The Effects of Product Class Knowledge on Information Search Behavior,” Journal of Consumer Research (12:1), 1985, pp. 1-16.

Brusilovsky, P., and Tasso, C. “Preface to Special Issue on User Modeling for Web Information Retrieval,” User Modeling and User-Adapted Interaction (14:2-3), 2004, pp. 147-157.

Burke, R. R. “Technology and the Customer Interface: What Consumers Want in the Physical and Virtual Store,” Journal of the Academy of Marketing Science (30:4), 2002, pp. 411-432.

Burnham, T. A., Frels, J. K., and Mahajan, V. “Consumer Switching Costs: A Typology, Antecedents, and Consequences,” Academy of Marketing Science (31:2), 2003, pp. 109-126.

Byrne, D., and Griffith, W. “Similarity and Awareness of Similarity of Personality Characteristics as Determinants of Attraction,” Journal of Experimental Research in Personality (3:3), 1969, pp. 179-186.

Campbell, M. C., and Goodstein, R. C. “The Moderating Effect of Perceived Risk on Consumers’ Evaluations of Product Incongruity: Preference for the Norm,” Journal of Consumer Research (28:3), 2001, pp. 439-449.

Cenfetelli, R. T. “An Empirical Study of the Inhibitors of Technology Usage,” in Proceedings of the 25 $^{th}$ International Conference of Information Systems, R. Agarwal, L. Kirsch, and J. I. DeGross (eds.), Washington, DC, December 2004, pp. 157-170.

Cenfetelli, R. T., and Benbasat, I. “Frustrated Incorporated: An Exploration of the Inhibitors of IT-Mediated Customer Service,” in Proceedings of the 9 $^{th}$ Americas Conference on Information Systems, J. Ross and D. Galletta (eds.), Tampa, FL, 2003, pp. 281-288.

Chiasson, T., Hawkey, K., McAllister, M., and Slonim, J. “An Architecture in Support of Universal Access to Electronic Commerce,” Information and Software Technology (44:5), 2002, pp. 279-289.

Chu, P.-C., and Elam, J. J. “Induced System Restrictiveness: An Experimental Demonstration,” IEEE Transaction on Systems, Man, and Cybernetics (20:1), 1990, pp. 195-201.

Claypool, M., Gokhale, A., Miranda, T., Murnikov, P., Netes, D., and Sartin, M. “Combining Content-Based and Collaborative Filters in an Online Newspaper,” paper presented at the ACM SIGIR Workshop on Recommender Systems—Implementation and Evaluation, Berkeley, CA, August 19, 1999.

\*Cooke, A. D. J., Sujan, H., Sujan, M., and Weitz, B. A. "Marketing the Unfamiliar: The Role of Context and Item-Specific Information in Electronic Agent Recommendations," Journal of Marketing Research (39:4), 2002, pp. 488-497.

\*Cosley, D., Lam, S. K., Albert, I., Konstan, J., and Riedl, J. “Is Seeing Believing? How Recommender Systems Influence Users’ Opinions,” in Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, Fort Lauderdale, FL, April 2003, pp.585-592.

Coupey, E., Irwin, J. R., and Payne, J. W. “Product Category Familiarity and Preference Construction,” Journal of Consumer Research (24), March 1998, pp. 459-468.

Cunningham, M. “The Major Dimensions of Perceived Risk,” in Risk Taking and Information Handling in Consumer Behavior, D. Cox (ed.), Harvard University Press, Boston, 1967, pp. 82-108.

Davis, F. D. “Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology,” MIS Quarterly (13:3), September 1989, pp. 319-340.

Davis, F. D., Bagozzi, R. P., and Warshaw, P. R. “User Acceptance of Computer-Technology: A Comparison of Two Theoretical Models,” Management Science (35:8), 1989, pp. 982-1003.

Davis, F. D., and Kottemann, J. E. “User Perceptions of Decision Support Effectiveness: Two Production Planning Experiments,” Decision Sciences (25:1), 1994, pp. 57-78.

\*Dellaert, B. G. C., and Haubl, G. “Consumer Product Search with Personalized Recommendations,” unpublished working paper, Department of Marketing, Business Economics and Law, University of Alberta, Edmonton, AB, 2005.

DeLone, W., and McLean, E. “The DeLone and McLean Model of Information System Success: A Ten-Year Update,” Journal of Management Information Systems (19:4), 2003, pp. 9-30.

DeLone, W., and McLean, E. “Information Systems Success: The Quest for the Dependent Variable,” Information Systems Research (3:1), 1992, pp. 60-95.

Detlor, B., and Arsenault, C. “Web Information Seeking and Retrieval in Digital Library Contexts: Towards an Intelligent Agent Solution,” Online Information Review (26:6), 2002, pp. 404-412.

\*Diehl, K. “Tempted by the Cheap and Easy: Searching Too Much in Ordered Environments,” unpublished working paper, Marketing Department, Moore School of Business, University of South Carolina, Columbia, SC, 2003.

\*Diehl, K., Kornish, L. J., and Lynch, J. G. “Smart Agents: When Lower Search Costs for Quality Information Increase Price Sensitivity,” Journal of Consumer Research (30:1), 2003, pp. 56-71.

Doney, P. M., and Cannon, J. P. “An Examination of the Nature of Trust in Buyer-Seller Relationships,” Journal of Marketing (61:2), 1997, pp. 35-51.

Dowling, G. R., and Staelin, R. “A Model of Perceived Risk and Intended Risk-Handling Activity,” Journal of Consumer Research (21:1), 1994, pp. 119-134.

Edwards, W., and Fasolo, B. “Decision Technology,” Annual Review of Psychology (52:1), 2001, pp. 581-606.

Eierman, M. A., Niederman, F., and Adams, C. “DSS Theory: A Model of Constructs and Relationships,” Decision Support Systems (14:1), 1995, pp. 1-26.

Farhoomand, A. F., and Drury, D. H. “Managerial Information Overload,” Communications of the ACM (45:10), 2002, pp. 127-131.

\*Fasolo, B., McClelland, G. H., and Lange, K. A. “The Effect of Site Design and Interattribute Correlations on Interactive Web-Based Decisions,” in Online Consumer Psychology: Understanding and Influencing Behavior in the Virtual World, C. P. Haughvedt, K. Machleit, and R. Yalch (eds.), Lawrence Erlbaum Associates, Mahwah, NJ, 2005, pp. 325-344.

\*Felix, D., Niederberger, C., Steiger, P., and Stolze, M. “Feature-Oriented vs. Needs-Oriented Product Access for Non-expert Online Shoppers,” in Towards the E-Society: E-Commerce, E-Business, and E-Government, B. Schmid, K. Stanoevska-Slabeva, and V. TschammerZürich (eds.), Springer, New York, 2001, pp. 399-406.

Fishbein, M., and Ajzen, I. Belief, Attitude, Intention and Behavior: An Introduction to Theory and Research, Addison-Wesley, Reading, MA, 1975.

Fitzsimons, G. J., and Lehmann, D. R. “Reactance to Recommendations: When Unsolicited Advice Yields Contrary Responses,” Marketing Science (23:1), 2004, pp. 82-94.

Formisano, R. A., Olshavsky, R. W., and Tapp, S. “Choice Strategy in a Difficult Task Environment,” Journal of Consumer Research (8:4), 1982, pp. 474-479.

Gefen, D., Karahanna, E., and Straub, D. W. “Trust and TAM in Online Shopping: An Integrated Model,” MIS Quarterly (27:1), 2003, pp. 51-90.

\*Gershoff, A. D., Mukherjee, A., and Mukhopadhyay, A. “Consumer Acceptance of Online Agent Advice: Extremity and Positivity Effects,” Journal of Consumer Psychology (13:1-2), 2003, pp. 161-170.

Goldberg, M. E., and Hartwick, J. “The Effects of Advertiser Reputation and Extremity of Advertising Claim on Advertising Effectiveness,” Journal of Consumer Research (17:2), 1990, pp. 172-179.

Good, N., Schafer, J. B., Konstan, J. A., Borchers, A., Sarwar, B. M., Herlocker, J. L., and Riedl, J. “Combining Collaborative Filtering with Personal Agents for Better Recommendations,” in Proceedings of the 16 $^{th}$ National Conference on Artificial Intelligence, Orlando, FL, July 1999, pp. 439-446.

Gregor, S., and Benbasat, I. “Explanations from Intelligent Systems: Theoretical Foundations and Implications for Practice,” MIS Quarterly (23:4), 1999, pp. 497-530.

Grenci, R. T., and Todd, P. A. “Solutions-Driven Marketing,” Communications of the ACM (45:2), 2002, pp. 64-71.

Griffith, D. A., and Chen, Q. “The Influence of Virtual Direct Experience (VDE) on On-line Ad Message Effectiveness,” Journal of Advertising (33:1), 2004, pp. 55-68.

Hanani, U., Shapira, B. and Shoval, P. “Information Filtering: Overview of Issues, Research and Systems,” User Modeling and User-Adapted Interaction (11:3), 2001, pp. 203-259.

Haubl, G., and Dellaert, B. G. C. “A Behavioral Theory of Consumer Product Search,” unpublished working paper, Department of Marketing, Business Economics and Law, University of Alberta, Edmonton, AB, 2004.

\*Haubl, G., and Murray, K. B. “Double Agent: Assessing the Role of Electronic Product-Recommendation Systems,” Sloan Management Review (47:3), 2006, pp. 8-12.

\*Haubl, G., and Murray, K. B. “Preference Construction and Persistence in Digital Marketplaces: The Role of Electronic Recommendation Agents,” Journal of Consumer Psychology (13:1-2), 2003, pp. 75-91.

\*Haubl, G., and Trifts, V. “Consumer Decision Making in Online Shopping Environments: The Effects of Interactive Decision Aids,” Marketing Science (19:1), 2000, pp. 4-21.

\*Herlocker, J., Konstan, J. A., and Riedl, J. “Explaining Collaborative Filtering Recommendations,” in Proceedings of the 2000 ACM Conference on Computer Supported Cooperative Work Philadelphia, PA, December 2000, pp. 241-250.

Herlocker, J., Konstan, J. A., Terveen, L. G., and Riedl, J. "Evaluating Collaborative Filtering Recommender Systems. ACM Transactions on Information Systems (22:1), 2004, pp. 5-53.

\*Hess, T. J., Fuller, M. A., and Mathew, J. “Involvement and Decision-Making Performance with a Decision Aid: The Influence of Social Multimedia, Gender, and Playfulness,” Journal of Management Information Systems (22:3), 2005, pp. 15-54.

Hoeffler, S., and Ariely, D. “Constructing Stable Preferences: A Look into Dimensions of Experience and Their Impact on Preference Stability,” Journal of Consumer Psychology (8:2), 1999, pp. 113-139.

\*Hostler, R. E., Yoon, V. Y., and Guimaraes, T. “Assessing the Impact of Internet Agent on End Users’ Performance,” Decision Support Systems (41:1), 2005, pp. 313-325..

Hoxmeier, J. A., and DiCesare, C. “System Response Time and User Satisfaction: An Experimental Study of Browser-Based Applications,” in Proceedings of the 6 $^{th}$ Americas Conference on Information Systems, H. M. Chung (ed.), Long Beach, CA, 2000, pp. 140-145.

Jacoby, J. “Consumer Behavior: A Quadrennium.” Annual Review of Psychology (49:1), 1998, pp. 319-344.

Jacoby, J., and Kaplan, L. B. “Components of Perceived Risk: A Cross-Validation,” Journal of Applied Psychology and Marketing (59:3), 1974, pp. 287-291.

Jahng, J., Jain, H., and Ramamurthy, K. “Empirical Investigation into Impact of Electronic Commerce Systems Richness on User Behavior: The Case of a Complex Product,” in Proceedings of the 6 $^{th}$ Americas Conference on Information Systems, H. M. Chung (ed.), Long Beach, CA, 2000, pp. 1393-1397.

Jiang, Z., and Benbasat, I. “Virtual Product Experience: Effects of Visual and Functional Control of Products on Perceived Diagnostics and Flow in Electronic Shopping,” Journal of Management Information Systems (21:3), 2005, pp. 111-148.

Jiang, Z., Wang, W., and Benbasat, I. “Multimedia-Based Interactive Advising Technology for Online Consumer Decision Support,” Communications of the ACM (48:9), 2005, pp. 92-98.

Kahn, B. E., and Baron, J. “An Exploratory Study of Choice Rules Favored for High-Stakes Decisions,” Journal of Consumer Psychology (4:4), 1995, pp. 305-328.

\*Kamis, A., and Davern, M. J. “Personalizing to Product Category Knowledge: Exploring the Mediating Effect of Shopping Tools on Decision Confidence,” in Proceedings of the 37 $^{th}$ Annual Hawaii International Conference on System Sciences, Big Island, HI, January 2004, p. 70202a.

Keller, K. L., and Staelin, R. “Effects of Quality and Quantity of Information on Decision Effectiveness,” Journal of Consumer Research (14:2), 1987, pp. 200-214.

Kim, D. J., and Benbasat, I. “The Effects of Trust-Assuring Arguments on Consumer Trust in Internet Stores,” in Proceedings of the 24 $^{th}$ International Conference on Information Systems, S. T. March, A. Massey, and J. I. DeGross (eds.), Seattle, WA, 2003, pp. 767-773.

Kim, S. S., and Malhotra, N. K. “A Longitudinal Model of Continued IS Use: An Integrative View of Four Mechanisms Underlying Postadoption Phenomena,” Management Science (51:5), 2005a, pp. 741-755.

Kim, S. S., and Malhotra, N. K. “Predicting System Usage from Intention and Past Use: Scale Issues in the Predictors,” Decision Sciences (36:1), 2005b, pp. 187-196.

King, M. F., and Balasubramanian, S. K. “The Effects of Expertise, End Goal, and Product Type on Adoption of Preference Formation Strategy,” Journal of the Academy of Marketing Science (22:2), 1994, pp. 146-159.

King, M. F., and Hill, D. J. “Electronic Decision Aids: Integration of a Consumer Perspective,” Journal of Consumer Policy (17:2), 1994, pp. 181-206.

Komiak, S. The Impact of Internalization and Familiarity on Trust and Adoption of Recommendation Agents, unpublished Doctoral Dissertation, University of British Columbia, Vancouver, BC, Canada, 2003.

\*Komiak, S., and Benbasat, I. “The Effects of Personalization and Familiarity on Trust and Adoption of Recommendation Agents,” MIS Quarterly (30:4), 2006, pp. XXX-XXX.

Komiak, S., and Benbasat, I. “Understanding Customer Trust in Agent-Mediated Electronic Commerce, Web-Mediated Electronic Commerce, and Traditional Commerce,” Information Technology and Management (5:1-2), 2004, pp. 181-207.

\*Komiak, S., Wang, W., and Benbasat, I. “Comparing Customer Trust in Virtual Salespersons with Customer Trust in Human Salespersons,” in Proceedings of the 38 $^{th}$ Annual Hawaii International Conference on System Sciences, Big Island, HI, January 2005, p. 175a.

Kottemann, J. E., and Davis, F. D. “Computer-Assisted Decision Making: Performance, Beliefs, and the Illusion of Control,” Organizational Behavior and Human Decision Processes (57:1), 1994, pp. 26-37.

\*Kramer, T. “The Effect of Measurement Task Transparency on Preference Construction and Evaluations of Personalized Recommendations,” Journal of Marketing Research, 2007, forthcoming.

Langer, E. J. “The Illusion of Control,” Journal of Personality and Social Psychology (32:2), 1975, pp. 311-328.

Levin, D. Z., Cross, R., and Abrams, L. C. “Why Should I Trust You? Predictors of Interpersonal Trust in a Knowledge Transfer Context,” paper presented at the Academy of Management Annual Meeting, Denver, CO, August 9-14, 2002.

Li, H., Daugherty, T., and Biocca, F. “The Role of Virtual Experience in Consumer Learning,” Journal of Consumer Psychology (13:4), 2003, pp. 395-407.

Lichtenthal, J. D., and Tellefsen, T. “Toward a Theory of Buyer–Seller Similarity,” Paper No. 22-1999, Institute for the Study of Business Markets, The Pennsylvania State University, University Park, PA, 1999.

Limayem, M., Cheung, C. M. K., and Chan, G. W. W. “Explaining Information Systems Adoption and Post-adoption: Toward an Integrative Model,” in Proceedings of the 24 $^{th}$ International Conference on Information Systems, S. T. March, A. Massey, and J. I. DeGross (eds.), Seattle, WA, 2003, pp. 720-731.

Lirtzman, S. I., and Shuv-Ami, A. “Credibility of Sources of Communication on Products’ Safety Hazards,” Psychological Reports (58:3), 1986, pp. 707-718.

Luwicki, R. J., and Bunker, B. B. “Trust in Relationships: A Model of Trust Development and Decline,” in Conflict, Cooperation and Justice, B. B. Bunker and J. Z. Rubin (eds.), Jossey-Bass, San Francisco, 1995, pp. 133-173.

Lynch, J. G., and Ariely, D. “Wine Online: Search Costs Affect Competition on Price, Quality, and Distribution,” Marketing Science (19:1), 2000, pp. 83-103.

Maes, P. “Agents that Reduce Work and Information Overload,” Communications of the ACM (37:7), 1994, pp. 31-40.

Maes, P., Guttman, R. H., and Moukas, A. G. “Agents that Buy and Sell,” Communications of the ACM (42:3), 1999, pp. 81-91.

Mak, B., and Lyytinen, K. “A Model to Assess the Behavioral Impacts of Consultative Knowledge Based Systems,” Information Processing & Management (33:4), 1997, pp. 539-550.

Mallach, E. G. Decision Support and Data Warehouse Systems: Irwin McGraw-Hill, Boston, 2000.

Mandel, N., and Johnson, E. “Constructing Preferences Online: Can Web Pages Change What You Want?,” unpublished working paper, Marketing Department, The Wharton School, University of Pennsylvania, Philadelphia, PA, 1998.

Massa, P., and Bhattacharjee, B. “Using Trust in Recommender Systems: An Experimental Analysis,” paper presented at the Second International Conference on Trust Management, Oxford, United Kingdom, March 29-April 1, 2004.

McKinney, V., Yoon, K., and Zahedi, F. M. “The Measurement of Web-Customer Satisfaction: An Expectation and Disconfirmation Approach,” Information Systems Research (13:3), 2002, pp. 296-315.

McKnight, D. H., Cummings, L. L., and Chervany, N. L. “Initial Trust Formation in New Organizational Relationships,” Academy of Management Review (23:3), 1998, pp. pp. 473.

\*McNee, S., Lam, S. K., Konstan, J. A., and Riedl, J. “Interfaces for Eliciting New User Preferences in Recommender Systems,” in Proceedings of the $9^{th}$ International Conference on User Modeling (User Modeling 2003), Johnston, PA, June 2003, pp. 178-187.

Mohr, L. A., and Bitner, M. J. “The Role of Employee Effort in Satisfaction with Service Transactions,” Journal of Business Research (32:3), 1995, pp. 239-252.

Mondak, J. J. “Perceived Legitimacy of Supreme Court Decisions: Three Functions of Source Credibility,” Political Behavior (2:4), 1990, pp. 363-384.

Montaner, M., Lopez, B., and De La Rosa, J. L. “A Taxonomy of Recommender Agents on the Internet,” Artificial Intelligence Review (19:4), 2003, pp. 285-330.

Montgomery, A. L., Hosanagar, K., Krishnan, R., and Clay, K. B. "Designing a Better Shopbot," Management Science (50:2), 2004, pp. 189-206.

\*Moore, R., and Punj, G. “An Investigation of Agent Assisted Consumer Information Search: Are Consumers Better Off?,” Advances in Consumer Research (28:1), 2001, p. 128.

Nah, F. F., and Benbasat, I. “Knowledge-Based Support in a Group Decision Making Context: An Expert-Novice Comparison,” Journal of the Association for Information Systems (5:3), 2004, pp. 125-150.

Nowlis, S. M., and Simonson, I. “Attribute-Task Compatibility as a Determinant of Consumer Preference Reversals,” Journal of Marketing Research (34), May 1997, pp. 205-218.

O'Keefe, R. M., and McEachern, T. "Web-Based Customer Decision Support Systems," Communications of the ACM(41:3), 1998, pp. 71-78.

Olshavsky, R. W. “Perceived Quality in Consumer Decision-Making: An Integrated Theoretical Perspective,” in Perceived Quality: How Consumers View Stores and Merchandise, J. C. Olson (ed.), D. C. Heath and Company, Lexington, MA, 1985, pp. 3-29.

\*Olson, E. L., and Widing, R. E. “Are Interactive Decision Aids Better than Passive Decision Aids? A Comparison with Implications for Information Providers on the Internet,” Journal of Interactive Marketing (16:2), 2002, pp. 22-33.

Olson, J., and Dover, P. A. “Disconfirmation of Consumer Expectations through Trial,” Journal of Applied Psychology (64:2), 1979, pp. 179-189.

Parikh, M. A., and Fazlollahi, B. “An Empirical Examination of the User Satisfaction/System Effectiveness Interrelation,” in Proceedings of the $8^{th}$ Americas Conference on Information Systems, R. Ramsower and J. Windsor (eds.), Dallas, TX, 2002, pp. 208-215.

Parthasarathy, M. B., and Bhattacherjee, A. “Understanding Post-Adoption Behavior in the Context of Online Services,” Information Systems Research (9:4), 1998, pp. 362-379.

Patrick, A. S. “Building Trustworthy Software Agents,” IEEE Internet Computing (6:6), 2002, pp. 46-53.

Patton, P. “Buy Here, and We’ll Tell You What You Like,” The New York Times on the Web, September 22, 1999.

Pavlou, P. A. “Consumer Acceptance of Electronic Commerce: Integrating Trust and Risk with the Technology Acceptance Model,” International Journal of Electronic Commerce (7:3), 2003, pp. 101-134.

Payne, J. W. “Contingent Decision Behavior,” Psychological Bulletin (92:2), 1982, pp. 382-402.

Payne, J. W., Bettman, J. R., and Johnson, E. The Adaptive Decision Maker, Cambridge University Press, New York, 1993.

Payne, J. W., Bettman, J. R., and Johnson, E. “Adaptive Strategy Selection in Decision Making,” Journal of Experimental Psychology: Learning, Memory, and Cognition (14:3), 1988, pp. 534-552.

Payne, J. W., Bettman, J. R., and Johnson, E. “Behavioral Decision Research: A Constructive Processing Perspective,” Annual Review of Psychology (43:1), 1992, pp. 87-131.

\*Pedersen, P. “Behavioral Effects of Using Software Agents for Product and Merchant Brokering: An Experimental Study of Consumer Decision Making,” International Journal of Electronic Commerce (5:1), 2000, pp. 125-141.

\*Pereira, R. E. “Influence of Query-Based Decision Aids on Consumer Decision Making in Electronic Commerce,” Information Resources Management Journal (14:1), 2001, pp. 31-48.

\*Pereira, R. E. “Optimizing Human-Computer Interaction for the Electronic Commerce Environment,” Journal of Electronic Commerce Research (1:1), 2000, pp. 23-44.

Pornpitakpan, C. “The Persuasiveness of Source Credibility: A Critical Review of Five Decades’ Evidence,” Journal of Applied Social Psychology (34:2), 2004, pp. 243-281.

Punj, G., and Rapp, A. “Influence of Electronic Decision Aids on Consumer Shopping in Online Stores,” paper presented at the Home Oriented Informatics and Telematics 2003 (HOIT 2003) Conference, Irvine, CA, April 6-8, 2003.

Qiu, L. “Designing Social Interactions with Animated Face and Speech Output for Product Recommendation Agents in Electronic Commerce,” unpublished paper (Doctoral Dissertation proposal), University of British Columbia, Vancouver, 2005.

Qiu, L., and Benbasat, I. “An Investigation into the Effects of Text-to-Speech Voice and 3D Avatars on the Perception of

Presence and Flow of Live Help in Electronic Commerce," ACM Transactions on Computer-Human Interaction (12:4), 2005, pp. 329-355.

Randall, T., Christian, T., and Ulrich, K. T. “User Design of Customized Products,” unpublished seminar paper, Operations and Information Management Department. The Wharton School, University of Pennsylvania, Philadelphia, Philadelphia, PA, 2003.

Rogers, E. M. Diffusion of Innovations ( $4^{th}$ ed.), The Free Press, New York, 1995.

Sarwar, B. M., Karypis, G., Konstan, J. A., and Riedl, J. “Analysis of Recommendation Algorithms for E-Commerce,” in Proceedings of the $2^{nd}$ ACM Conference on Electronic Commerce, Minneapolis, MN, October 17-20, 2000, pp. 158-167.

Schafer, J. B., Konstan, J. A., and Riedl, J. “E-Commerce Recommendation Applications,” Data Mining and Knowledge Discovery (5:1-2), 2001, pp. 115-153.

Schafer, J. B., Konstan, J. A., and Riedl, J. “Meta-Recommendation Systems: User-Controlled Integration of Diverse Recommendations,” paper presented at the 11 $^{th}$ International Conference on Information and Knowledge Management, McLean, VA, November 2002.

\*Schein, A. I., Popescul, A., Ungar, L. H., and Pennock, D. M. “Methods and Metrics for Cold-Start Recommendations,” in Proceedings of the 25 $^{th}$ Annual International ACM Special Interest Group on Information Retrieval (SIGIR) Conference on Research and Development in Information Retrieval, Tampere, Finland, August 2002, pp. 253-257.

Schleifer, L. M., and Amick, B. C. “System Repines Time and Method of Pay: Stress Effects in Computer-Based Tasks,” International Journal of Human-Computer Interaction (1:1), 1989, pp. 23-39.

Sears, A., and Borella, M. S. “WANDS: Tools for Designing and Testing Distributed Documents,” Technical Report No. #97-01, School of Computer Science, DePaul University, 1997.

Selnes, F. “Antecedents and Consequences of Trust and Satisfaction in Buyer-Seller Relationships,” European Journal of Marketing (32:3-4), 1998, pp. 305-322.

\*Senecal, S. Essays on the Influence of Online Relevant Others on Consumers' Online Product Choices, unpublished doctoral dissertation, HEC Montreal, University of Montreal, 2003.

\*Senecal, S., and Nantel, J. “The Influence of Online Product Recommendations on Consumers’ Online Choices,” Journal of Retailing (80:2), 2004, pp. 159-169.

Shneiderman, B. Designing the User Interface: Strategies for Effective Human-Computer Interaction ( $3^{rd}$ ed.). Addison-Wesley, Reading, MA, 1998.

Shneiderman, B. “Direct Manipulation for Comprehensible, Predictable and Controllable User Interfaces,” in Proceedings of the $2^{nd}$ International Conference on Intelligent User Interfaces, Orlando, FL, January 6-9, 1997, pp. 33-39.

Shugan, S. M. “The Cost of Thinking,” Journal of Consumer Research (7:2), 1980, pp. 99-111.

Silver, M. S. “Decision Support Systems: Directed and Non-directed Change,” Information Systems Research (1:1), 1990, pp. 47-70.

Silver, M. S. “User Perceptions of Decision Support System Restrictiveness: An Experiment,” Journal of Management Information Systems (5:1), 1988, pp. 51-65.

Simon, H. A. “A Behavioral Model of Rational Choice,” Quarterly Journal of Economics (69), February 1955, pp. 99-118.

\* Sinha, R., and Swearingen, K. “Comparing Recommendations Made by Online Systems and Friends,” in Proceedings of the 2 $^{nd}$ DELOS Network of Excellence Workshop on Personalisation and Recommender Systems in Digital Libraries, Dublin, Ireland, June 18-20, 2001.

\* Sinha, R., and Swearingen, K. “The Role of Transparency in Recommender Systems,” in CHI 2002 Extended Abstracts on Human Factors in Computing Systems, Minneapolis, MN, April 20-25, 2002, pp. 830-831.

Smith, S., and Shaffer, D. R. “Celerity and Cajolery: Rapid Speech May Promote or Inhibit Persuasion Through its Impact on Message Elaboration,” Personality and Social Psychology Bulletin (7:6), 1991, pp. 663-669.

\*Spiekermann, S. Online Information Search with Electronic Agents: Drivers, Impediments, and Privacy Issues, unpublished doctoral dissertation, Humboldt University Berlin, Berlin, 2001.

Spiekermann, S., and Paraschiv, C. “Motivating Human-Agent Interaction: Transferring Insights from Behavioral Marketing to Interface Design,” Electronic Commerce Research (2:3), 2002, pp. 255-285.

Stamm, K., and Dube, R. “The Relationship of Attitudinal Components to Trust in Media,” Communications Research (2:1), 1994, pp. 105-123.

Stolze, M., and Nart, F. “Well-Integrated Needs-Oriented Recommender Components regarded as Helpful,” in CHI 2004 Extended Abstracts on Human Factors in Computing Systems, Vienna, Austria, April 24-29, 2004, p. 1571.

Suh, K. S., and Lee, Y. E. “Effects of Virtual Reality on Consumer Learning: An Empirical Investigation in Web-Based Electronic Commerce,” MIS Quarterly (29:4), 2005, pp. 673-697.

\*Swaminathan, V. “The Impact of Recommendation Agents on Consumer Evaluation and Choice: The Moderating Role of Category Risk, Product Complexity, and Consumer Knowledge,” Journal of Consumer Psychology (13:1-2), 2003, pp. 93-101.

\*Swearingen, K., and Sinha, R. “Beyond Algorithms: An HCI Perspective on Recommender Systems,” paper presented at the ACM SIGIR Workshop on Recommender Systems, New Orleans, LA, September 13, 2001.

\*Swearingen, K., and Sinha, R. “Interaction Design for Recommender Systems,” paper presented at the International Conference on Designing Interactive Systems (DIS 2002), London, June 25-28, 2002.

Taylor, S., and Todd, P. “Understanding Information Technology Usage: A Test of Competing Models,” Information Systems Research (6:2), 1995, pp. 144-176.

Thum, M., Boucstein, W., Kuhman, W., and Ray, W. J. “Standardized Task Strain and System Response-Times in Human-Computer Interaction,” Ergonomics (38:7), 1995, pp. 1342-1351.

Todd, P., and Benbasat, I. “The Influence of Decision Aids on Choice Strategies: An Experimental Analysis of the Role of Cognitive Effort,” Organizational Behavior and Human Decision Processes (60:1), 1994, pp. 36-74.

Tversky, A., Sattath, S., and Slovic, P. “Contingent Weighting in Judgment and Choice,” Psychological Review (95:3), 1988, pp. 371-384.

\*Urban, G. L., Sultan, F., and Qualls, W. “Design and Evaluation of a Trust Based Advisor on the Internet,” unpublished Working Paper 123, Sloan School of Management, Massachusetts Institute of Technology, 1999.

\*van der Heijden, H. V. D., and Sorensen, J. B. “The Mobile Decision Maker: Mobile Decision Aids, Task Complexity, and Decision Effectiveness,” unpublished working paper 2002-25, Copenhagen Business School, Frederiksberg, Denmark, 2002.

Van Slyke, C., and Collins, R. “Trust Between Users and Their Intelligent Agents,” paper presented at the Annual Meeting of the Decision Sciences Institute, Orlando, FL, November 24-26, 1996.

Venkatesh, V. “Determinants of Perceived Ease of Use: Integrating Control, Intrinsic Motivation, and Emotion into the Technology Acceptance Model,” Information Systems Research (11:4), 2000, pp. 342-365.

Venkatesh, V., and Brown, S. A. “A Longitudinal Investigation of Personal Computers in Homes: Adoption Determinants and Emerging Challenges,” MIS Quarterly (25:1), 2001, pp. 71-102.

Venkatesh, V., Morris, M., Davis, G. B., and Davis, F. D. “User Acceptance of Information Technology: Toward a Unified View,” MIS Quarterly (27:3), 2003, pp. 425-478.

Verplanken, B. “Persuasive Communication of Risk Information: A Test of Cue Versus Message Processing Effects in a Field Experiment,” Personality and Social Psychology Bulletin (7:2), 1991, pp. 188-193.

\* Vijayasarathy, L. R., and Jones, J. M. “Do Internet Shopping Aids Make a Difference? An Empirical Investigation,” Electronic Markets (11:1), 2001, pp. 75-83.

\*Wang, W. Design of Trustworthy Online Recommendation Agents: Explanation Facilities and Decision Strategy Support, unpublished Doctoral Dissertation, University of British Columbia, Vancouver, 2005.

\*Wang, W., and Benbasat, I. “Impact of Explanations on Trust in Online Recommendation Agents,” Working Paper No. 02-MIS-002, MIS Division, Sauder School of Business, University of British Columbia, Vancouver, 2004a.

\*Wang, W., and Benbasat, I. “Trust and Distrust Building Processes in Online Recommendation Agents: A Process-Tracing Analysis,” unpublished Working Paper 04-MIS-003, MIS Division, Sauder School of Business, University of British Columbia, Vancouver, 2004b.

\*Wang, W., and Benbasat, I. “Trust In and Adoption of Online Recommendation Agents,” Journal of the AIS (6:3), 2005, pp. 72-100.

Weiss, S. M., Boggs, G., Lehto, M., Hodja, S., and Martin, D. J. "Computer System Response Time and Psychophysiological Stress," in Proceedings of the Human Factors Society $26^{th}$ Annual Meeting, Seattle, WA, October 1982, pp. 698-702.

West, P. M., Ariely, D., Bellman, S., Bradlow, E., Huber, J., Johnson, E., Kahn, B., Little, J., and Schkade, D. “Agents to the Rescue?,” Marketing Letters (10:3), 1999, pp. 285-300.

Wixom, B. H., and Todd, P. “A Theoretical Integration of User Satisfaction and Technology Acceptance,” Information Systems Research (16:1), 2005, pp. 85-102.

Zachary, W. “A Cognitively Based Functional Taxonomy of Decision Support Techniques,” Human-Computer Interaction (2:1), 1986, pp. 25-63.

Zhang, Y. Literature Review for Online Communities and Recommender Systems: State of the Art Paper, unpublished doctoral dissertation, University of Minnesota, Minneapolis, 2002.

Zhu, L. B. I. Let's Shop Online Together: An Investigation of Online Collaborative Shopping Support, unpublished Master's thesis, University of British Columbia, Vancouver, 2004.

Zucker, L. G. “Production of Trust: Institutional Sources of Economic Structure, 1840-1920,” in Research in Organizational Behavior, B. M. Staw and L. L. Cummings (eds.), JAI Press, Greenwich, CT, 1986, pp. 53-111.

Zucker, L. G., Darby, M. R., Brewer, M. B., and Peng, Y. "Collaboration Structure and Information Dilemmas in Biotechnology: Organizational Boundaries as Trust Production," in Trust in Organizations: Frontiers of Theory and Research, R. M. Kramer and T. R. Tyler (eds.), Sage Publications, Thousand Oaks, CA, 1996, pp. 90-113.

## About the Authors

Bo Xiao is a Ph.D. student in Management Information Systems at the Sauder School of Business, University of British Columbia, Vancouver, Canada. Her research focuses on intelligent decision support systems, with special interest in electronic commerce product recommendation agents.

Izak Benbasat, Fellow-Royal Society of Canada, is CANADA Research Chair in Information Technology Management at the Sauder School of Business, University of British Columbia, Vancouver, Canada. He currently serves on the editorial boards of Journal of the Association for Information Systems and Journal of Management Information Systems. He was editor-in-chief of Information Systems Research, editor of the Information Systems and Decision Support Systems Department of Management Science, and a senior editor of MIS Quarterly. The general theme of his research is improving the communication between information technology (IT), management, and IT users. This communication exits at different levels of the organization and has different facets, for example, interaction between individual managers and intelligent decision support systems, design of interfaces for customers shopping at web stores, and dialogues between IT professionals and line managers.

## Appendix A

## Summary of Empirical Studies

## Aggarwal and Vaidyanathan (2003a)

Context

• Computer aided experiment with 109 student subjects

Independent Variables

• Product type (search/experience)

Dependent Variables

\- Recommendation development process (rule-based filtering vs. collaborative filtering) Perceived agent effectiveness:

• Perceived quality of recommendations

• Satisfaction with the recommendations

\- Intent to follow-up on a recommendation

Results

\- Agents were more effective for search goods than for experience goods.

\- Rule-based filtering process was perceived to be more effective than collaborative-based filtering process.

## Aggarwal and Vaidyanathan (2003b)

Context

• A study with 42 subjects

\- Two preference elicitation tasks for refrigerators

Independent Variables

\- Preference elicitation methods (conjoint based inference vs. self-explicated ratings)

Dependent Variables

\- Convergence of ratings

Results

\- Inferred preferences varied significantly from stated inferences.

\- Implications: the two methods are not equivalent and using one method over the other may result in a recommendation that does not match the preferences of the consumer.

## Aksoy and Bloom (2001)

Theory

Theories of human decision-making

Context

\- RA embedded in a simulated fictitious online shopping site

• Lab experiment with 172 subjects

• A search and choice task for a cellular phone

Independent Variables

\- Degree of similarity between attribute weights used by the agent to generate the listing and the consumers' own weights

\- Degree of similarity between the decision strategy used by the agent and the consumers' own decision strategies

Dependent Variables

\- Perceived utility

\- Cognitive cost

• Amount of information searched

Results

\- Decision quality

\- Attribute weight similarity was important in increasing perceived utility of using ordered listings, decreasing the cognitive cost and amount of information searched, and improving decision quality.

\- Subject's perceptions of correspondences between the decision strategy used by an RA and the subject's preferred decision strategy moderated the effect of decision strategy similarity manipulations on the dependent variables.

## Basartan (2001)

Theory

Analytical model of consumer utility by Montgomery et al. (2001)

Context

\- Simulated shopbots

• Experiment with 190 student subjects

\- The task was to complete an exercise to estimate utility models, shop at several shopbots, and evaluate preferences for shopping at the presented shopbot or Amazon

Independent Variables • Number of alternatives displayed

\- Response time

\- User preference

Results

\- Shopper preference for shopbots declined with too many alternatives and long waiting times.

## Bechwati and Xia (2003)

## Theory

\- Effort-accuracy model

• Equity theory

• Expectation-performance paradigm

## Context

• Electronic aid for job search

\- Two studies with 180 and 52 student subjects, respectively

\- In Study 1, subjects completed a paper and pencil task, responding to the questionnaire based on imagination of a scenario described in a booklet

\- In Study 2, subjects performed a simulated job search with a simple web-based decision aid

## Independent Variables Study 1:

\- Type of aid (no aid, human aid, electronic aid)

Study 2:

• Information about search progress

\- Customization of results

## Dependent Variables

Study 1:

• Perception of own effort

\- Perception of aid's effort

• Perception of effort saving

Study 2:

• Satisfaction with the process

## Results

• Perception of effort saving

\- Study 1: Consumers believed that electronic decision aids saved them an equal level of effort. Consumers, however, perceived electronic aids as exerting less effort than human aids.

\- Study 2: Online shoppers' satisfaction with decision process was positively associated with their perception of the effort saved for them by electronic aids. Moreover, informing shoppers about search progress led to a higher level of perceived saved effort and, consequently, satisfaction.

## Bharati and Chaudhury (2004)

Theory

IS success model

Context

• A survey with 210 subjects

• Different web-based decision support systems

## Independent Variables

\- System quality

• Information quality

• Information presentation

## Dependent Variables

• Decision making satisfaction

\- Decision confidence

○ Decision effectiveness

## Results

\- System quality and information quality were directly and positively correlated with decision-making satisfaction.

\- The relative weight of information quality was higher than system quality.

\- Presentation was not directly and positively correlated with decision-making satisfaction.

## Cooke, Sujan, Sujan, and Weitz (2002)

## Theory

## Importance of context

Context

• Three studies with 179, 118, and 65 student subjects respectively

• Simulated music CD shopping agents

\- Subjects were asked to rate the agent as well as to indicate their likelihood of buying each of the unfamiliar CDs

## Independent Variables

• Number of recommended items

• Familiarity of the recommended items

\- Preference (well-liked or moderately liked)

\- Context

\- recommendations

○ Simultaneous condition

\- Sequential condition

\- Item-specific information

○ With music clips

○ Without music clips

\- Similarity of information provided for the familiar and unfamiliar recommendations

○ Endorsed by the same reviewer

○ Endorsed by different reviewers

## Dependent Variables

\- Agent competence

\- Agent usefulness

\- Likelihood of buying the unfamiliar CDs

## Results

\- Unfamiliar recommendations lowered agent evaluations.

\- Additional recommendations of familiar products served as a context within which unfamiliar recommendations were evaluated.

\- When the presentation of the recommendations made unfamiliar and familiar products appear similar, evaluative assimilation resulted.

\- When additional information about the unfamiliar products was given, consumers distinguished them from the familiar products, producing evaluative contrast.

## Cosley, Lam, Albert, Konstan, and Riedl (2003)

Theory

Context

Literature on conformity and persuasive computing

• Three experiments with 536 users

• Movie-Lens movie recommender system

\- Users were asked to rate a set of movies

## Independent Variables

\- Types of rating scales

\- Whether or not predictions are shown when users rate movies

## Dependent Variables

• Accuracy of CF predictions

\- Users' ratings

## Results

\- Users preferred finer-grained scales; however, granularity was not the only factor.

\- Users rated fairly consistently across rating scales.

\- The display of predicted ratings on unrated movies led users to rate in the direction of the prediction.

\- Users could detect systems that manipulated predictions.

## Dellaert and Haubl (2005)

## Theory

• Normative search theory

• Research in behavioral decision making

## Context

• Lab experiment with 455 subjects

• RAs for compact stereo systems and home rentals

• A preference-elicitation task followed by a product choice task

## Independent Variables

\- The availability of personalized product recommendations

\- Expected increase in utility that the consumer derives from looking at the next alternative in the recommendation list

\- The standard error in the prediction of the expected utility of the next alternative in the list

• Utility difference between current and most preferred prior alternative

\- Attribute-based difference between current and most preferred prior alternative

\- Utility difference between current alternative and the one inspected just prior to it

## Dependent Variables

• The probability of continuing to search

## Results

• Currently most preferred alternative

\- Significant positive effect of the expected difference in utility between the next alternative in the personalized list and the currently most preferred alternative on the probability of continuing to search.

\- Significant positive effect of the utility difference between the currently inspected product and the best previously encountered one on the choice of the currently most preferred alternative.

\- Personalized product recommendations increased consumers' tendency to rely on local utility comparisons in deciding which alternative was their currently most preferred one.

\- Personalized product recommendations reduced consumers' tendency to rely on a comparison of the utility of the current alternative and that of the best previously inspected one in determining the currently most preferred alternative.

## Diehl (2003)

Theory

Research on consumer decision making

Context

\- Three lab experiments with 51, 47, and 100 subjects, respectively

• RAs for greeting cards and MP3 players

\- All three experiments are based on principal-agent tasks. Subjects were asked to choose an alternative that would be liked by a target customer

## Independent Variables Experiment 1

\- Search cost

\- Type of recipient

Experiment 2

• Number of recommendations presented

\- Type of recipient

Experiment 3

\- Search costs

• Accuracy (high accuracy goal vs. low accuracy goal)

## Dependent Variables

Experiment 1

\- Amount of search

• Quality of consideration set

• Quality of the chosen card

\- Selectivity

Experiment 2

\- Amount of search

• Quality of consideration set

• Quality of the chosen card

\- Selectivity

Experiment 3

\- Amount of search

• Size of consideration set

• Quality of consideration set

• Quality of the chosen card

## Results

Experiment 1

\- Lower search costs significantly increased the number of unique options searched, decreased the quality of the consideration set, led to worse choices, and reduced selectivity.

Experiment 2

\- Recommending more cards significantly increased the number of unique options searched, decreased the quality of the consideration set, led to worse choices, and reduced selectivity.

Experiment 3

\- The negative effects of lower search costs were heightened if consumers had a greater motivation to be accurate.

## Diehl, Kornish, and Lynch (2003)

Theory

Research on search costs and price sensitivity

Context

\- Three lab experiments with 64, 43, and 36 subjects, respectively

• RA for greeting cards

\- Task was to choose greeting cards for two specifically described recipients

## Independent Variables

• Type of search agent (ordered vs. random)

\- Assortment size

\- Order of recipient

Experiment 2

\- Sequence of search

\- Order of recipient

\- Trial (1 vs. 2)

Experiment 3

\- Relative importance of price in the reward function

\- Type of search agent

\- Order of search

## Dependent Variables

Experiment 1

• Price of the chosen card

• Quality of the chosen card

Experiment 2

• Price of the chosen card

Experiment 3

• Price of the chosen card

## Results

• Quality of the chosen card

\- With a good ordering agent, consumers had better decision quality and paid lower price when the underlying assortment was larger.

\- Consumers paid lower prices when recommendations were ordered than when they were not.

• Repeated use of the ordered search agent decreased prices more.

\- Ordered search agent led to higher/lower prices being chosen when price was relatively less/more important.

## Fasolo, McClelland, and Lange (2005)

Theory

Effort-accuracy framework

Context

• Web-based experiment with 60 subjects

• RA for digital cameras

\- Task was to make four distinct choices, using four different decision sites

• Interattribute correlations

\- Site design (Compensatory vs. noncompensatory)

Dependent Variables • Clicks

○ Total clicks

○ Option clicks

○ Attribute clicks

\- Choice quality

• Satisfaction with the choices made

• Confidence in the choices made

• Difficulty of the choice tasks

\- Ease of use of the decision site

## Results

• Satisfaction with the decision site used

\- Site design influenced users' choice behavior

○ Compensatory site: more option clicks

○ Noncompensatory site: more attribute clicks

\- Interattribute correlation also affected choice behavior

\- More total clicks when the correlation was negative than when it was positive

\- The interaction between interattribute correlation and site design

○ Compensatory site (Negative correlation: more option clicks)

○ Noncompensatory site (Negative correlation: more attribute clicks)

\- Site design and interattribute correlation affected users' psychological perceptions

\- More positive perceptions were associated with the compensatory site than with the noncompensatory site

\- More positive perceptions were choices characterized by positive rather than negative interattribute correlations

\- The real difference between the two designs emerged when attributes were negatively related

\- Decision quality

○ The compensatory site enabled more choices that were of high quality

## Felix, Niederberger, Steiger, and Stolze (2001)

Context

\- Digital camera RA

• Lab experiment with 20 subjects

\- The task was to engage in two RA-assisted shopping sessions for digital cameras (one with the assistance of a feature-based RA and the other with a needs-based RA)

Independent Variables • Type of RA (feature-based vs. needs-based)

• Order (which type of RA is used first)

Dependent Variables • Preference for the RA

\- Perceived suitability of the RA's advice to product novices

## Results

\- Most subjects recommended needs-based RAs for novices.

\- No significant difference was found for user preferences between the two types of RAs.

\- Self-reported preferences did not match the observations of the experimenter—some novices considered themselves experts.

## Gershoff and Mukhopadhyay (2003)

## Theory

• Goal-based emotion

• Social categorization

\- Anchoring and adjustment

• Correspondence judgments

• Extremity effect (negativity and positivity effects)

## Context

\- Agent: an internet-based movie critic (movie rating service)

\- Two lab experiments with 85 and 43 student subjects, respectively

\- The task was for the subjects to examine their own movie ratings with those provided by the online movie critic and then evaluate the likelihood of accepting the agent's advice

## Independent Variables Study 1:

• Overall agreement (high/low)

• Extreme agreement (high/low)

Study 2:

• Extreme agreement (positive/negative)

• Advice valence (positive/negative)

## Dependent Variables

Study 1:

\- Likelihood of accepting the agent's advice

Study 2:

\- Acceptance of agent advice

• Confidence in agent advice

## Results

• Perceived similarity of attributes likes and dislikes

\- Study 1: In addition to the overall agreement rate, consumers paid special attention to extreme opinion agreement when assessing agent diagnosticity (i.e., extremity effect).

\- Study 2: Positive extreme agreement was more influential than negative extreme agreement when advice valence was positive, but the converse did not hold when advice valence was negative (i.e., positivity effect).

## Haubl and Murray (2003)

Theory

## Context

Constructive preferences

• Online attribute-based RA

• Lab experiment with 347 student subjects

\- Three tasks: one agent assisted shopping task for backpacking tents and two paired choice tasks

## Independent Variables

\- Attribute inclusion in RA calibration interface

\- Inter-attribute correlation (negative, positive)

\- Perceived rationale for attribute inclusion (strong, neutral, weak)

## Dependent Variables

\- Relative importance of the attributes (included in RA calibration) to the user when making decisions

• Amount of information searched

○ Total amount of time spent searching

## Results

○ Number of alternatives for which a detailed description is viewed

\- The inclusion of an attribute in an RA rendered this attribute more important when consumers made product choices.

\- This preference-construction effect was moderated by the inter-attribute correlation and the perceived rationale for the selective inclusion of attributes.

\- This type of preference-construction effect persisted into subsequent choice tasks where no electronic decision aid was present, and the extent of such persistence was greater if a stronger rationale for the selective inclusion of attributes in an RA had been provided during an earlier shopping trip.

## Haubl and Murray (2006)

## Theory

• Effort/accuracy trade-off

\- Constructive preferences

## Context

\- RA for notebooks

• Lab experiment with 265 subjects

• Eight repeated shopping trips

## Independent Variables

\- RA (with/without)

## Dependent Variables

\- Decision effort

○ Number of alternatives subjects looked at before making product choice across eight shopping trips

\- Decision quality

○ Subjective utility score of the chosen product

## Results

\- The presence of personalized product recommendations reduced search effort.

\- Using an RA dramatically increased subjects' decision quality.

## Haubl and Trifts (2000)

## Theory

• Effort/accuracy trade-off

• Strengths and weaknesses of human decision makers in information processing

\- Two stage process to decision making

## Context

\- Custom built product-brokering RA

• Lab experiment with 249 student subjects

\- The task was to shop for a product in each of two categories—backpacking tents and compact stereo systems

## Independent Variales

\- RA (with/without)

• Comparison matrix (with/without)

\- Product category

• Product category order

## Dependent Variables

• Amount of product information searched

• Size and quality of consideration set

\- Decision quality

\- Whether non-dominated alternatives were selected

○ Product switching

## Results

○ Confidence in purchase decisions

\- The use of RAs reduced search effort for product information, decreased the size but increased the quality of consideration sets, and improved the quality of purchase decisions.

\- The use of a comparison matrix (CM) led to a decrease in the size but an increase in the quality of consideration sets, and it tended to have a favorable effect on objective decision quality.

\- Product category and order did not have a moderating effect on the relationship between RA/CM and the dependent variables.

## Herlocker, Konstan, and Riedl (2000)

Theory

Theory of explanation

## Context

\- MovieLens online movie RA

\- Two studies with 78 and 210 subjects, respectively

## Independent Variables

• Different techniques of providing explanation

\- Explanation facilities (with, without)

## Dependent Variables

• How likely the users would go and see the movie.

\- User acceptance of the collaborative filtering (CF) RA

• Filtering performance of user

## Results

\- What models and techniques are effective in supporting explanation in an automated collaborative filtering (ACF) system? (Study 1)

Big winners: histograms of neighbors' ratings, past performance, similarity to other items in the user's profile, and favorite actor or actress.

\- Can explanation facilities increase the acceptance of automated collaborative filtering systems? (Study 2) Most users valued the explanations and would like to see them added to their ACF system.

\- Can explanation facilities increase the filtering performance of ACF system users? (Study 2) Unable to prove or disprove our hypothesis.

Users performed filtering based on many different channels of input.

## Hess, Fuller, and Mathew (2005)

Theory

Effort-accuracy framework

Context

• Lab experiment with 259 subjects

• Computer-based decision aid for apartments

• An apartment selection task

## Independent Variables

\- Multimedia vividness (text only, text and voice, animation)

\- Personality similarity (between user and decision aid)

\- Gender

\- Computer playfulness

## Dependent Variables

• Involvement with decision aid

• Decision making outcomes

○ Satisfaction

○ Understanding

\- Decision time

○ Use of decision aid features

\- Decision quality

## Results

\- Computer playfulness increased user involvement.

\- Women were more involved with the decision aid than men.

\- When the personalities of the user and the decision aid were more similar (lower difference scores), users were more involved with the decision aid.

\- The vividness of the multimedia did significantly affect involvement, but not in the hypothesized direction. The addition of animation appeared to reduce user involvement with the decision aid.

\- Involvement positively affected user satisfaction and understanding with the decision aid.

\- Users that were more involved with the decision aid also spent more time using the decision aid.

\- Involvement did not significantly affect the number of decision aid features used or decision quality/accuracy.

## Hostler, Yoon, and Guimaraes (2005)

## Context

• Lab experiment with 69 subjects

\- Shopbot for DVD

\- DVD shopping task

Independent Variables • Use of shopbot

Dependent Variables

• End-user performance

○ Time spent

\- Decision quality

○ Confidence in the decision

○ Cognitive effort

## Results

\- Using the shopbot saved users time and increased their decision quality. There were no significant differences in either the subjects' decision confidence or their perception of the mental effort required to perform this particular online shopping task.

## Kamis and Davern (2004)

## Theory

• Research in product category knowledge

• TAM

## Context

• Lab experiment with 66 subjects

\- Decision tools implementing different decision strategies for printers and computers

• Shopping tasks for printers and computers

## Independent Variables

• Product category knowledge

## Dependent Variables

• Perceived usefulness

• Perceived ease of use

\- Decision confidence

## Results

\- Product category knowledge was negatively related to perceived ease of use and perceived usefulness.

\- Perceived usefulness was positively related to decision confidence.

## Komiak and Benbasat (2006)

Theory

• Identification-based trust

• Unit-grouping-based trust

• Cognitive-emotional trust

## Context

• Lab experiment with 100 student subjects

\- Two constraint-satisfaction online product brokering RAs

\- Task was to shop for notebook computers, desktop computers, and/or digital cameras using an RA

## Independent Variables

• Perceived internalization

\- Familiarity

Control variables:

\- Control propensity

\- Trust propensity

\- Product experience

\- Preference for decision quality vs. effort saving

## Dependent Variables

• Cognitive trust:

○ Competence

○ Benevolence

○ Integrity

\- Emotional trust

\- Intention to use an RA as a decision aid

## Results

\- Intention to use an RA as a delegated agent

\- Internalization increased cognitive trust and emotional trust in an RA.

\- Familiarity increased cognitive trust in benevolence and integrity.

• Cognitive trust and emotional trust predicted intentions to use an RA as a decision aid.

\- Emotional trust fully mediated the impact of cognitive trust on the intention to use an RA as a delegated agent.

\- No significant differences between the groups in terms of four control variables.

## Komiak, Wang, and Benbasat (2005)

Theory

Context

## Trust formation

• An exploratory study with 44 subjects

• Virtual salesperson at RadioShack website

\- Task was to compare the services of virtual salesperson and human salesperson

## Independent Variables

• Type of salesperson (virtual vs. human)

## Dependent Variables

## Results

• Processes for trust and distrust formation

\- Similar to trust in a human salesperson, trust in a virtual salesperson contained trust in competence, benevolence, and integrity.

\- The formation processes of trust in virtual salespersons, trust in human salespersons, distrust in virtual salespersons, and distrust in human salespersons were different.

## Kramer (2007)

## Theory

## Constructed preferences

## Context

\- Three lab experiments with 102, 123, and 164 subjects, respectively

• RA for digital cameras and PDA

## Independent Variables

\- Tasks for all three experiments consisted of a preference measurement and a recommendation evaluation part Experiment 1

\- Task transparency

○ Full-profile conjoint analysis

○ Self-explicated approach

○ Product expertise

## Experiment 2

\- Task transparency

\- Offer timing (immediate vs. delayed)

\- Recommendation content (higher-price/quality vs. lower-price/quality)

Experiment 3

\- task transparency

\- reminder of measured responses (absent vs. present)

## Dependent Variables Experiment 1

\- Recommendation acceptance (the acceptance by users of the top-ranked digital camera)

## Experiment 2

\- Recommendation acceptance

\- Likelihood of buying any one of the recommended PDAs

\- Difficulty of choosing a PDA from the list of recommendations

Experiment 3

\- Recommendation acceptance

## Results

## Experiment 1

\- Respondents were significantly more likely to accept a personalized recommendation when their preferences had been measured using a more transparent task, i.e., self-explicated approach.

\- Difference in recommendation acceptance occurred only for novices (i.e., those who did not own a digital camera). Experiment 2

\- Respondents were significantly more likely to choose the recommended PDA following the more transparent measurement task.

\- The effect was moderated by offer timing and recommendation content.

Experiment 3

\- Significant transparency × reminder interaction.

## McNee, Lam, Guetzlaff, Konstan, and Riedl (2003)

## Context

• Online experiment with 223 users

\- MovieLens: RA for movies

\- Task was to use MovieLens to perform movie selections

## Independent Variables

• Presence of confidence display

\- Experience with MovieLens (New vs. experienced users)

\- Training vs. no training

## Dependent Variables

\- User satisfaction

• Perceived value of the confidence display

## Results

\- Adding a confidence display to an RA increased user satisfaction.

\- Adding a confidence display to an RA altered users' behavior when engaging tasks with varying amounts of risks.

\- New and experienced users reacted differently to the addition of a confidence display.

\- Training had a profound impact on user satisfaction in a recommender system: providing training to new users increased user satisfaction over just adding the confidence display to the system; providing training to experienced users increased their usage of the confidence system, but decreased their overall satisfaction with the recommender.

## McNee, Lam, Konstan, and Riedl (2003)

## Context

• Web-based experiment with 225 subjects

\- MovieLens: RA for movies

• Preference elicitation task

## Independent Variables • Three types of RAs

○ System-controlled

○ User-controlled

\- Mix-initiative: provides users with a choice of the system

## Dependent Variables

\- User satisfaction

• Quality of user models

## Results

\- User-controlled interface had the best model quality.

\- User-controlled interface had the highest user satisfaction.

\- Users of user-controlled interface thought the system best understood their tastes.

○ They also had the highest retention rate.

\- There was often a tradeoff between giving users control and increasing their effort.

\- Users of user-controlled interface spent nearly twice as long as the other two groups in the signup process. However, they did not feel that they were spending a long time in the signup process, because asking them to recall titles created focus and engagement with the system.

## Moore and Punj (2001)

Context

\- Lab experiment

\- RA for apartment

• An apartment search task

## Independent Variables

• Environment (web vs. traditional print)

\- Time pressure

• Number of alternatives

## Dependent Variables

\- Amount of search

\- Satisfaction with search

\- Decision confidence

## Results

\- Amount of information search was higher in the traditional environment.

\- Amount of search was not shown to affect satisfaction.

## Olson and Widing (2002)

Context

\- Two lab experiments with 59 and 70 subjects, respectively

\- Four different interactive decision aids for word processing programs

\- Choice task for word processing programs

## Independent Variables

\- Type of decision aids

○ Alphabetical

○ Discordant

○ Equal weight

○ Interactive linear weighted

## Dependent Variables

\- Subjective reactions

\- Decision accuracy

○ Confusion experienced

\- Frustration experienced

○ Confidence in choice

○ Format satisfaction

\- Time

○ Perceived decision time

○ Decision time

\- Decision quality

○ Relative accuracy

○ Discrete accuracy

○ Switching

○ Selection of dominated alternative

## Results

\- Interactive decision aid led to higher relative accuracy and discrete accuracy than did discordant one.

\- Interactive decision aid led to less switching than alphabetical and discordant ones.

\- Interactive decision aid led to higher perceived accuracy, confidence, satisfaction and less frustration, confusion, perceived decision time than did alphabetical and discordant ones.

\- Interactive decision aid performed as well as the equal weighted one on both subjective and objective measures.

## Pedersen (2000)

## Theory Context

Decision making model based on Solomon's four-stage buying process

• Web-based experiment with 144 subjects

• A shopbot for selecting financial service providers

\- Task consisted of choosing a financial service provider for a mortgage, a savings account, and a current account for monthly average outstanding salary after tax

## Independent Variables

\- Access to shopbot service

## Dependent Variables

\- Problem attention

\- Problem complexity

\- Search time

• Information sources

• Amount of information

\- Internet search satisfaction

\- Consideration set size

\- Attributes evaluated

\- Attention to quantitative attributes

• Quantitative criteria used in choice

\- Single quantitative criteria

• Combined quantitative criterion

## Results

\- At the problem recognition stage, no differences in consumer buying behavior between shopbot users and nonusers in terms of focused attention to choice problem and understanding of the complexity of choice problem.

\- At the information search stage, there was strong evidence of differences in buying behavior. Shopbot users
    - Spent less time searching for information.

○ Reported a significantly larger number of information sources.

○ Collected a greater amount of information.

\- Were generally more satisfied with using the Internet as an information search medium.

\- At the judgment stage, no differences in consumer buying behavior between shopbot users and nonusers in terms of consideration set size, attributes evaluated, and attention to quantitative attributes.

\- At choice stage, there was only partial and weak support for the hypotheses of differences.

## Pereira (2000)

## Theory

Research in information filtering strategies

## Context

\- Two lab experiments with 160 and 80 subjects, respectively

• A smart agent for cars

\- Car choice tasks

## Independent Variables

## Experiment 1

\- Product knowledge

\- Agent search strategy (elimination by aspect, weighted average, profile building, simple hypertext)

## Experiment 2

\- Product knowledge

\- WAD vs. EBA

(the software application for the EBA and WAD search strategies was modified to increase the degree of control provided to the user and to increase the amount of information provided to the user)

## Dependent Variables

• Satisfaction with decision process

\- Trust in the agent's recommendations

• Confidence in the decision

\- Propensity to purchase

• Perceived cost savings

• Cognitive decision effort

Experiment 1

\- Subjects with high product class knowledge had more positive affective reactions to the agent in the WAD and EBA conditions than in the profile building condition.

\- Subjects with low product class knowledge had more positive affective reactions to the agent in the profile building condition than in the EBA and WAD conditions.

Experiment 2

\- Subjects responded more positively to the previously less preferred strategy, thus weakening the interaction effect.

## Pereira (2001)

Effort-accuracy framework

• Lab experiment with 173 subjects

• A query-based decision aid for cars

• A choice task for cars

## Independent Variables

\- Access to the query-based decision aid

## Dependent Variables

• Confidence in the decision

• Satisfaction with the decision process

• Number of stages in the phased narrowing of the consideration set

\- Decision quality

Mediating variables

• Cognitive decision effort

• size of the consideration set

\- similarity among the alternatives in the consideration set

## Results

• perceived cost savings

\- QBDA had a significant impact on all the mediating and dependent variables (e.g. satisfaction, confidence, and accuracy).

## Schafer, Konstan, and Riedl (2002)

Context

\- Three web-based experiments with 50, 32, and 60 subjects, respectively

• A hybrid RA for movies: MetaLens

\- Movie selection tasks

## Independent Variables

Experiment 1 and 2

\- Formats for displaying recommendations (Default, All, Custom, Automatic)

Experiment 3

\- Type of RA (meta-recommender vs. traditional recommenders)

## Dependent Variables

Experiment 1 and 2

• Confidence in movie selection

• Helpfulness of recommendations

\- Reliance on previous knowledge in making selections

Experiment 3

• Confidence in movie selection

\- Reliance on previous knowledge in making selections

## Results

Experiment 1 and 2

\- The All format that provided the most information was considered most helpful.

\- As the amount of recommendation data increased, users found the All format less helpful and began to prefer the Custom format.

Experiment 3

\- A meta-recommender system was considered more helpful and generated more confidence from the users than traditional recommender systems.

## Senecal (2003)

## Senecal and Nantel (2004)

## Theory

Information influence

Human decision-making process

Discounting principle of attribution theory

## Context

• Online experiment with 488 subjects

\- Custom-built RA embedded in three different types of websites

\- Three different sampling frames: consumers, people interested in e-commerce, students

\- Shop for two products: calculators, and wine

## Independent Variables

\- Type of website (seller, $3^{\text{rd}}$ party commercially linked to sellers, $3^{\text{rd}}$ party not commercially linked to sellers)

\- Type of recommendation source (No recommendation source, human experts, other consumers, recommender system

• Degree of recommendation uniformity

• Product type (search, experience)

\- Perceived risks (determined by product type, product class knowledge, product class familiarity)

\- Recommendation source credibility (determined by type of website and type of recommendation source)

\- Susceptibility to interpersonal influence

## Dependent Variables

\- Consultation or non-consultation of the product recommendation

\- Influence of the recommendation source on consumers' online product selections

• Product choice confidence

\- Reason for product choice

## Results

\- RAs were found to be the most influential recommendation source even if they were perceived as possessing less expertise than human experts and as being less trustworthy than other consumers.

\- The type of website on which recommendation sources were used did not affect their perceived trustworthiness as recommendation sources and did not influence consumers' propensity to consult or follow the product recommendations.

\- The type of product did not influence subjects' propensity to consult a product recommendation; but for subjects who did consult a product recommendation, the product type had an influence on their propensity to follow a product recommendation. Recommendations for experience products were significantly more influential than for search products.

\- Online product recommendations significantly influenced subjects' online product choices.

\- Subjects who consulted and followed a product recommendation showed less confidence in their product choices than subjects who did not consult the product recommendation and those who did consult the recommendation but did not follow it.

\- Subjects who were influenced by product recommendations tended to lessen the recommendation influence by attributing their choice to various product attributes.

## Sinha and Swearingen (2001)

## Context

• Three-book RAs and three-movie RAs

• A user study with 19 student subjects

\- The task was to test either three-book or three-movie systems as well as to evaluate recommendations made by three friends

Independent Variables • Source of recommendation (friend vs. online RA)

\- Item domain (books vs. movies)

\- RA characteristics

## Dependent Variables

• Quality of recommendation (good recommendations, useful recommendations, trust-generating recommendations)

\- Overall satisfaction with recommendations and with online RA (usefulness and ease of use)

Results from both quantitative and qualitative analysis.

\- Users found friends' recommendations better and more useful; however, they also found items recommended by online RAs useful; recommended items were often new and unexpected.

\- Recommended items that had been previously liked by users played a unique role in establishing the credibility of the RA.

\- Increase in number of ratings (i.e., amount of user input) did not negatively affect ease of use.

\- Users preferred continuous scale to binary choice scale to provide initial ratings.

\- Detailed information about recommended items correlated positively with both the usefulness and ease of use of RAs.

\- Users liked easy ways to generate new recommendation sets.

\- Interface (navigation and layout) mattered, mostly when it got in the way.

## Sinha and Swearingen (2002)

Theory

Literature on explanation (expert systems, search engines)

Context

• A user study of 5 music RAs

• 12 student subjects

\- The task was to rate 10 recommendations provided by the RAs

Independent Variables • Perceived transparency

## Dependent Variables

\- Liking of recommendations

• Confidence in recommendations

## Results

\- In general, users liked and felt more confident in recommendations perceived as transparent.

## Spiekermann (2001)

## Theory

Literature on information search

## Context

• A 3-D anthropomorphic advisor agent – Luci

\- Two products: compact cameras and winter jackets

\- An experiment with 206 subjects and a survey with 39 subjects

\- The task for the experiment was to shop either for a winter jacket or for a compact camera at an online store supported by Luci

\- The task for the survey was to judge the 112 agent questions employed by Luci (56 questions per product)

## Independent Variables Experiment

• Product nature (search vs. experience)

• Purchase involvement

• Stage in the buying process

• Product class knowledge

\- Perceived risk (functional, financial, social-psychological, delivery)

\- Privacy concerns

\- Flow

• Time cost of search

\- Benefit of interaction

• Perceived uncertainty

Survey

• Perceived importance of information request

• Perceived legitimacy of information request

• Perceived difficulty of information request

## Dependent Variables

Experiment

\- Interaction with agent

\- Manual information search

Both variables are measured on two dimensions: time and the number of page requests

\- Private consumer information cost

## Results

Experiment

\- Consumers preferred to manually control the search process if they perceived more risk..

\- Product involvement positively affected both agent interaction and manual searches.

\- Product class knowledge negatively influenced the perception of risk.

\- More perceived product knowledge led to less interaction with an agent. However, the reduced level of interaction with an agent may be attributable to the failure of Luci to satisfy the needs of highly knowledgeable customers.

\- Higher perceived time cost led to less manual information searches.

\- Expressed privacy concerns led to reduced levels of interaction with the agent.

\- Unfavorable privacy settings induce a feeling of discomfort among some users which then led to less interaction with agent.

\- Customers associated different types of purchase risk with the products they sought.

\- Higher levels of uncertainty in product judgment led to more manual searches and less interaction with an agent. Survey

\- Perceived legitimacy and difficulty of information request affected private consumer information cost.

\- The legitimacy of agent questions was relatively stronger when driven by their perceived importance in the purchase context.

\- Users accepted personal questions as long as they relate to the product context.

## Stolze and Nart (2004)

Context

• A prototype RA for digital cameras

• Comparative user tests with 8 subjects

## Independent Variables

• Full system (needs-oriented plus feature-oriented) vs. Baseline system (feature-oriented only)

Dependent Variables

\- User preferences

Results

\- Users preferred the full system to the baseline system.

## Swaminathan (2003)

Theory

Literature on information overload

Context

• Web-based attribute-based RA

• Computer-based experiment with 100 subjects

\- RA-assisted shopping task for backpacking tent and power toothbrush

\- Subjects were given 2 weeks to complete the task

## Independent Variables

\- RA (yes/no)

Moderating variables:

\- Product complexity

\- Category risk

\- Category knowledge

\- Category order

## Dependent Variables

\- Amount of searched

\- The proportion of available alternatives for which detailed product information is viewed

\- Decision quality

\- Whether or not non-dominated alternative is purchased

## Results

\- RA had a greater impact on decision quality under conditions of high category risk.

\- RA had a greater impact on reducing the amount of search when the number of attributes used to describe a product was fewer.

## Swearingen and Sinha (2001)

## Context

• Three book RAs and three movie RAs

\- User study with 19 student subjects

\- The task was to test either three-book or three-movie systems as well as to evaluate recommendations made by three friends

## Independent Variables

\- Source of recommendation (friend vs. online RA)

\- Item domain (books vs. movies)

\- RA characteristics

## Dependent Variables

• Quality of recommendation (good recommendations, useful recommendations, trust-generating recommendations)

\- Overall satisfaction with recommendations and with online RA (usefulness and ease of use)

\- Time measures: time spent registering and receiving recommendations from the system

## Results

\- From a user's perspective, an effective RA inspired trust in the system; had system logic that was at least somewhat transparent; pointed users towards new, not-yet-experienced items; provided details about recommended items, including pictures and community ratings; and, finally, provided ways to refine recommendations by including or excluding particular genres.

\- Users expressed willingness to provide more input to the system in return for more effective recommendations.

## Swearingen and Sinha (2002)

## Context

• 11 online RAs

\- Two user studies with a total of 32 student subjects

\- The task was to interact with several RAs, provide input to the system, and evaluate 10 recommendations from each system

## Independent Variables System as a whole

\- System transparency

• Familiar recommendations

Input:

\- Type of rating process (open-ended, ratings on Likert Scale, binary liking, hybrid rating process)

• Amount of input (number of items to rate)

\- Genre filtering (whether RA offers filter-like controls over genres)

## Output:

\- Ease of getting more recommendations

• Information about recommended items (basic item information, expert and community ratings, item sample)

\- Navigational path to detailed information

## Dependent Variables

\- Liking

• Action towards item

\- Usefulness

\- Ease of use

\- Preferred RA

## Results

\- Trustworthiness

\- From a user's perspective, an effective RA inspired trust in the system; had system logic that was at least somewhat transparent; pointed users towards new, not-yet-experienced items; provided ease of obtaining more recommendations; provided details about recommended items, including pictures and community ratings; and, finally, provided ways to refine recommendations by including or excluding particular genres. Users expressed willingness to provide more input to the system in return for more effective recommendations.

\- Trust was affected by several aspects of the users' interactions with the systems, in addition to the accuracy of the recommendations themselves: transparency of system logic, familiarity of the items recommended, and the process for receiving recommendations.

## Urban, Sultan, and Qualls (1999)

## Theory Literature on trust

\- A prototype virtual personal advisor for pickup truck purchasing

\- A use study with 250 respondents (all of whom had purchased a truck in the last 18 months)

\- The task was to evaluate the virtual personal advisor in terms of trust, quality of recommendations and willingness to use and pay for the service

## Independent Variables Types of systems:

\- A virtual advisor-based Internet site – Truck Town

\- An information intensive site with no advisor

• Traditional auto dealer system

## Product knowledge

## Dependent Variables • Trust

• Quality of recommendations

\- Willingness to use and pay for the service

## Results

\- Overall preference

\- The proposed virtual advisor-based site could build trust; most customers would consider buying a vehicle at this site and would be willing to pay for the service.

\- A combination of the advisor site and an information intensive site together dominated the existing auto dealer system in terms of customer acceptance.

\- The preference for the two Internet sites was equal, but analysis indicates segmentation in the site preferences. Consumers who were not very knowledgeable about trucks, who visited more dealers, and who were younger and more frequent Internet users had the highest preference for the virtual personal advisor.

## van der Heijden and Sorensen (2002)

Theory

Context

\- Two-stage consumer decision process

\- An experiment at an artificial camera store with 86 subjects

• A mobile decision aid for digital cameras

• A camera selection task

\- Task complexity

• Availability of the decision aid

## Dependent Variables

\- Consideration set quality

\- Decision confidence

## Results

• The availability of the decision aid

\- increased the number of non-dominated alternatives in the users' consideration set.

\- increased users' confidence in the final decision when the task complexity was high.

\- There were no correlations between the three decision effectiveness measures

\- users held opinions about accuracy which were decidedly unrelated to actual consideration set quality.

## Vijayasarathy and Jones (2001)

## Context

• A lab experiment with 124 subjects

• RA at MySimon.com

• Purchase simulation task for televisions

## Independent Variables • Access to RA

## Dependent Variables Perceptions

\- Convenience

\- Ease of use

\- Enjoyment

\- Speed

• Helpfulness of comparisons

• Confidence in product selected

• Confidence in merchant selected

Search activities

\- Search strategies

\- Type of comparisons

• Time to complete task

• Number of vendor sites visited

## Results

\- Those with decision aid perceive online shopping to be more convenient.

\- Those with decision aid took less time to complete shopping task.

\- Those with decision aid were less confident in their decisions.

## Wang (2005)

## Theory

## - Trust

\- System restrictiveness

## Context

• Lab experiment with 156 student subjects

\- Custom built RA for digital cameras

\- Two tasks: select one digital camera with RA for a friend and another one for a relative

## Independent Variables

Agent types (decision strategy support)

\- Additive compensatory agent

\- Elimination by aspect agent

\- Hybrid agent

Use of explanations

## (with and without)

## Dependent Variables

\- Trust

\- Perceived usefulness

• Perceived ease of use

\- Intention to adopt RA

• Perceived cognitive effort

\- Consideration set size

\- Decision time

• Perceived agent restrictiveness

• Perceived agent transparency

## Results

\- Explanation use exerted significant effects on perceived agent transparency.

\- Decision strategy support had significant effects on perceived cognitive effort.

\- Perceived strategy restrictiveness was negatively correlated with both trust and perceived usefulness.

\- Perceived agent transparency was positively correlated with trust.

\- Perceived cognitive effort was negatively correlated with perceived ease of use.

\- There was an interaction effect between decision strategy support and explanation use—the benefits of hybrid agents were achieved when explanations were provided.

## Wang and Benbasat (2004a)

## Theory

\- Trust

• Literature on explanation

## Context

• Lab experiment with 120 student subjects

\- Custom built product-brokering RA based on content filtering

\- Two tasks: select one digital camera with RA for a friend and another one for a relative

## Independent Variables

Type of explanation

\- How explanation

\- Why explanation

\- Decisional guidance

Control variables:

\- Trust propensity

\- Product experience

• Effort/quality preference

## Dependent Variables

Trusting beliefs

\- Competence

\- Benevolence

\- Integrity

## Results

\- How explanations affected users' competence and benevolence beliefs.

\- Why explanations affected users' benevolence beliefs.

\- Decisional guidance affected users' integrity beliefs.

\- Trust propensity affects users' competence beliefs.

## Wang and Benbasat (2004b)

Theory

Context

• Theories of initial trust formation

• Lab experiment with 120 subjects

\- Custom built RA for digital cameras

\- Two tasks: choose a digital camera for a good friend and then select another camera for a close family member

\- Subjects were asked to answer several essay questions to justify their trust level in the RA

## Independent Variables

Type of explanation

\- How explanation

\- Why explanation

\- Decisional guidance

Dependent Variables

Trust in RA

\- Competence

\- Benevolence

Results

\- Integrity

\- Different trusting beliefs existed in the initial stage of trust formation.

\- Consumers formed different trusting beliefs in different ways.

\- Consumers' trust building and inhibiting processes co-existed in the initial formation stages.

## Wang and Benbasat (2005)

Theory

Context

Integrated Trust-TAM model

• Lab experiment with 120 subjects

\- Custom built RA for digital cameras

\- Two tasks: select one digital camera for a friend and another for a close relative

## Independent Variables

Type of explanation

\- How explanation

\- Why explanation

\- Decisional guidance

## Dependent Variables

Trust in RA

\- Competence

\- Benevolence

\- Integrity

• Perceived usefulness

\- Perceived ease of use

\- Intention to adopt RA

## Results

\- Consumers' initial trust and PU had a significant impact on their intentions to adopt RAs, while PEOU did not.

\- Consumers' initial trust and PEOU influenced their PU of the RAs significantly.

\- PEOU also influenced consumers' trust in RA significantly.

\- The significant results regarding the impact of trust on PU and on intentions, as well as the impact of PEOU on trust, confirmed the nomological validity of trust in online RAs.

## Appendix B

## Theoretical Perspectives

Five theoretical perspectives are proposed to account for the phenomena concerning outcomes of RA use. These perspectives are used in the “Propositions” section to generate propositions that are evaluated in light of available empirical evidence. These propositions form the basis for answering the research questions raised in the “Motivation, Scope, and Contribution” subsection, and for describing the connections among the key constructs identified in Figure 1.

The following are the theoretical perspectives are utilized:

• Theories of human information processing

• Theory of interpersonal similarity

• Theories of trust formation

• Technology Acceptance Model (TAM)

• Theories of satisfaction

A brief description of each theory follows.

## Theories of Human Information Processing

An information processing approach to studying consumer choice is based on the observation that consumers have limited cognitive capacity to process information (Payne 1982; Payne et al. 1988), which leads to bounded rationality, the notion that individuals seek to attain a satisfactory, although not necessarily an optimal, level of achievement (Simon 1955).

The effort–accuracy framework epitomized by Payne et al. (1993) is based on the idea that, although consumers have a number of available strategies in making choices, which strategy is ultimately chosen depends “on some compromise between the desire to make an accurate decision and the desire to minimize cognitive effort. Since the accuracy and effort characteristics generally differ across strategies for a given decision environment and across environments for a given strategy, strategy usage will vary depending on the properties of decision task” (Bettman et al. 1998, p. 192). Therefore, a consumer’s decision-making process is seen as a trade-off between the accuracy of the decision and the effort required to make the decision. There has been mixed evidence on whether the use of electronic decision aids results in better decisions or simply reduces time and effort. For instance, a series of studies by Benbasat and Todd (1992, 1996) have demonstrated that electronic decision aids are mainly used to conserve user effort, not necessarily leading to improved decision quality. Other research (Haubl and Trifts 2000) has shown that electronic decision aids can have favorable effects on both decision quality and decision effort. Punj and Rapp (2003) also suggest that the use of the aid may increase consumers’ cognitive capacity and help remove cognitive limitations. In line with the theory of bounded rationality, as limitations are removed, increased effort will lead to better decisions.

Due to the limitation in information processing capacity, it is not feasible for consumers to always evaluate all available alternatives in detail before making their decisions. Consequently, in order to reduce complexity, it is necessary for them to adopt a two-stage process to decision making, including an initial screening of available alternatives followed by an in-depth comparison of selected alternatives, before making their final decision (Payne 1982; Payne et al. 1988).

Furthermore, the theory of constructive preferences postulates that individuals often lack the requisite cognitive resources to form well-defined preferences that are stable over time and invariant to the context in which decisions are made (Bettman et al. 1998). Instead, they often construct preferences on the spot when prompted to make decisions (Haubl and Murray 2003). Since these preferences are constructed, rather than absolute, they are sensitive to the characteristics of the decision environment.

While electronic shopping environments make it possible for consumers to access large amounts of product information, consumers still need to process increasingly more information with the same limited processing capacity (West et al. 1999). One method of coping with information overload is to filter and omit information (Farhoomand and Drury 2002; Senecal 2003). Another is to use decision support tools, such as RAs, to perform resource-intensive information processing tasks, thus freeing up some of the human processing capacity for decision making (Haubl and Trifts 2000).

## Theory of Interpersonal Similarity

Prior research in psychology, sociolinguistics, communication, business, and related fields has supported a positive similarity–attraction relationship (Byrne and Griffitt 1969), which postulates that the greater degree of similarity between two parties (e.g., in behavior, communication style, attitude, personality, physical appearance, religion, status), the greater the attraction will be. Interpersonal similarity increases the ease of communication between two individuals who are similar to each other, improves the predictability of the behavior exhibited by each of them, and fosters relationships of trust and reciprocity among the parties (Levin et al. 2002; Zucker, 1986). Lichtenthal and Tellefsen (1999) synthesize findings from past research in sales, marketing, and psychology, which indicate that buyers often judge their degree of similarity with a salesperson in terms of observable characteristics (physical attributes and behavior) and internal characteristics (perceptions, attitudes, and values). While internal similarity can increase a buyer’s willingness to trust a salesperson and follow his/her guidance, observable similarity often exerts a negligible influence on buyer perceptions of a salesperson’s effectiveness.

In the same vein, Levin et al. (2002) define interpersonal similarity both in terms of demographics, such as race, gender, education, and age, and in terms of cognitive processes, such as shared vision and shared language. They have found that, out of the three categories of variables that affect interpersonal trust (attributes of the relationship between a knowledge seeker and a source of information, attributes of a knowledge source, and attributes of a knowledge seeker), similarity in the cognitive processes between a knowledge seeker and a source of knowledge has the most significant effect on trust building, whereas similarity in demographics has little or no effect.

## Theories of Trust Formation

RAs are both trust objects and IT artifacts (Gefen et al. 2003). For RAs to be effective, consumers must have confidence in the RAs' product recommendations, as well as in the processes by which these recommendations are generated (Haubl and Murray 2003). Therefore, trust remains a major issue for users of RAs. Furthermore, the relationship between RAs and their users can be described as an agency relationship. By delegating the task of product screening and evaluation to an RA (i.e., the agent), a user assumes the role of a principal. Thus, as a result of the information asymmetry underlying any agency relationship, users usually cannot tell whether or not RAs are capable of performing the tasks delegated to them, and whether RAs work solely for the benefits of the users or the online store where they reside.

Prior trust research (Doney and Cannon 1997; McKnight et al. 1998) has identified many distinct trust formation processes, examples of which include knowledge, cognition, calculation, transference, prediction, and goodwill. The present paper focuses on three major trust formation processes, because they cover all of the processes identified in the empirical studies reviewed: knowledge-based processes, cognitive processes, and transference.

Knowledge-based trust is developed over time as individuals accumulate knowledge that is relevant to trust through experiences with the object of their trust (Luwicki and Bunker 1995; McKnight et al. 1998). Cognition-based trust is formed by two types of cognitive processes: (1) an assessment of the trust object's competence, benevolence, and integrity, and (2) a categorization process, which in turn comprises two sub-processes (McKnight et al. 1998)—unit-grouping (i.e., when an individual identifies a trust object in the same category as herself or himself) and reputation categorization (i.e., an assignment of attributes to a trust object based on second-hand information). Trust can also be developed through transference (Doney and Cannon 1997), that is, it can be transferred from one trusted source to the trust object.

## Technology Acceptance Model (TAM)

An RA is essentially a sample of information technology. As such, user intentions to adopt RAs should be explicable in part by the technology acceptance model (TAM), the parsimony and robustness of which have been demonstrated in numerous empirical studies in IS literature (see Venkatesh et al. 2003). According to TAM, an intention to adopt a new technology is determined by the perceived usefulness (PU) of using the technology and the perceived ease of use (PEOU) of the technology.

## Theories of Satisfaction

The user satisfaction literature is one of the two dominant research streams (the other being the technology acceptance literature) investigating perceptions of information system (IS) success (Wixom and Todd 2005). Despite a proliferation of theoretical and conceptual frameworks related to user satisfaction with information systems, two particularly influential ones are the IS success model (DeLone and McLean 1992, 2003) and the expectation–disconfirmation paradigm (see McKinney et al. 2002).

DeLone and McLean (1992) presented the IS success model and postulated that information quality (which measures semantic success) and system quality (which measures technical success) are two key antecedents of user satisfaction. Many empirical undertakings have tested and validated DeLone and McLean's IS success model (see DeLone and McLean 2003). Whereas system quality was usually measured in terms of ease of use, functionality, reliability, flexibility, data quality, portability, integration, and importance, information quality was generally assessed in terms of accuracy, timeliness, completeness, relevance, and consistency. DeLone and McLean (2003) have updated their model by adding service quality (usually measured in terms of the dimensions of tangibles, reliability, responsiveness, assurance, and empathy) to information quality and system quality in their research model.

The expectancy-disconfirmation paradigm has been commonly used in academic marketing studies to measure customer satisfaction (see McKinney et al. 2002). Based on this paradigm, customer satisfaction is determined by three primary factors: expectation, disconfirmation, and perceived performance. Expectation is a customer's "pretrial beliefs" about a product; it is often formed by the customer's prior experiences and his or her exposure to vendors' marketing efforts. Perceived performance is a customer's perceptions of how product performance fulfills his or her needs and desires. Disconfirmation occurs when a customer's evaluations of product performance are different from his or her expectations about the product (McKinney et al. 2002; Olson and Dover 1979). Satisfaction is achieved when expectations are fulfilled (confirmed). Negative disconfirmation of expectations will result in dissatisfaction, whereas positive disconfirmation will result in enhanced satisfaction (Selnes 1998).

## Appendix C

## Propositions Answering Research Questions

<table><tr><td>1</td><td>How do RA use, RA characteristics, and other factors influence consumer decision-making processes and outcomes?</td></tr><tr><td rowspan="3">1.1</td><td>How does RA use influence consumer decision-making processes and outcomes?</td></tr><tr><td>P1: RA use influences users' decision effort.P1a: RA use reduces the extent of product search by reducing the total size of alternative sets processed by the users as well as the size of the search set, in-depth search set, and consideration set.P1b: RA use reduces users' decision time.P1c: RA use increases the amount of user input.</td></tr><tr><td>P2: RA use improves users' decision quality.</td></tr><tr><td rowspan="5">1.2</td><td>How do the characteristics of RAs influence consumer decision-making processes and outcomes?</td></tr><tr><td>P3: RA type influences users' decision effort and decision quality.P3a: Compared with pure content-filtering RAs or pure collaborative-filtering RAs, hybrid RAs lead to better decision quality and higher decision effort (as indicated by amount of user input).P3b: Compared with non-compensatory RAs, compensatory RAs lead to better decision quality and higher decision effort (as indicated by amount of user input).P3c: Compared with feature-based RAs, needs-based RAs lead to better decision quality.</td></tr><tr><td>P4: The preference elicitation method influences users' decision quality and decision effort. The explicit preference elicitation method leads to better decision quality and higher decision effort (as indicated by amount of user input) than does the implicit preference elicitation method.</td></tr><tr><td>P5: Included product attribute influences users' preference function and choice. Included product attributes (in RA's preference elicitation interface) are given more weight in the users' preference function and considered more important by the users than those not included. Product alternatives that are superior on the included product attributes are more likely to be chosen by users than are products superior on the excluded product attributes.</td></tr><tr><td>P6: Recommendation content influences users' product evaluation and choice.P6a: Recommendations provided by RAs influence users' choice to the extent that products recommended RAs are more likely to be chosen by users.P6b: The display of utility scores or predicted ratings for recommended products influences users' product evaluation and choice to the extent that products with high utility scores or predicted ratings are evaluated more favorably and are more likely to be chosen by users.P7: Recommendation format influences users' decision processes and decision outcomes.P7a: Recommendation display method influences users' decision strategies and decision quality to the extent that sorted recommendation lists result in greater user reliance on heuristic decision strategies (when evaluating product alternatives) and better decision quality.P7b: The number of recommendations influences users' decision effort and decision quality to the extent that presenting too many recommendations increases users' decision effort (in terms of decision time and extent of product search) and decreases decision quality.</td></tr><tr><td rowspan="7">1.3</td><td>How do other factors (i.e., factors related to user, product, and user-RA interaction) moderate the effects of RA use and RA characteristics on consumer decision-making processes and outcomes?</td></tr><tr><td>P8: Product type moderates the effects of RA use on users' choice. RA use influences the choice of users shopping for experience products to a greater extent than that of those shopping for search products.</td></tr><tr><td>P9: Product complexity moderates the effects of RA use on users' decision quality and decision effort. The use of RAs for more complex products leads to greater increase in decision quality and greater decrease in decision effort than for less complex products.</td></tr><tr><td>P10: Product complexity moderates the effect of included product attributes on users' choice. The inclusion effect is stronger for products with negative inter-attribute correlations (i.e., more complex products) than for those with positive inter-attribute correlations (i.e., less complex products).</td></tr><tr><td>P11: Product expertise moderates the effect of preference elicitation method on users' decision quality. Preference elicitation method has less effect on the decision quality of users with high product expertise than on the decision quality of those with low product expertise.</td></tr><tr><td>P12: Perceived product risks moderate the effects of RA use on users' decision quality and decision effort. When perceived product risks are high, RA use leads to greater improvements in decision quality and reduction in decision effort than when perceived product risks are low.</td></tr><tr><td>P13: User-RA similarity moderates the effects of RA use on users' decision quality and decision effort. RA use leads to greater increase in decision quality and greater decrease in decision effort when the RAs are similar to the users than when the RAs are not similar to the users.</td></tr><tr><td>2</td><td>How do RA use, RA characteristics, and other factors influence users' evaluations of RAs?</td></tr><tr><td>2.1</td><td>How does RA use influence users' evaluations of RAs?</td></tr><tr><td rowspan="7">2.2</td><td>How do characteristics of RAs influence users' evaluations of RAs?</td></tr><tr><td>P14: RA type influences users' evaluations of RAs.P14a: Compared with pure content-filtering or pure collaborative-filtering RAs, hybrid RAs lead to greater trust, perceived usefulness, and satisfaction but to lower perceived ease of use.P14b: Compared with non-compensatory RAs, compensatory RAs lead to greater trust, perceived usefulness, and satisfaction but to lower perceived ease of use.</td></tr><tr><td>P15: The preference elicitation method influences users' perceived ease of use of and satisfaction with the RAs. Compared to an explicit preference elicitation method, an implicit preference elicitation method leads to greater perceived ease of use of and satisfaction with the RAs.</td></tr><tr><td>P16: The ease of generating new or additional recommendations influences users' perceived ease of use of and satisfaction with RAs. The easier it is for the users to generate new or additional recommendations, the greater their perceived ease of use of and satisfaction with the RAs.</td></tr><tr><td>P17: User control of interaction with RAs' preference-elicitation interface influences users' trust in, satisfaction with, and perceived usefulness of the RAs. Increased user control leads to increased trust, satisfaction, and perception of usefulness.</td></tr><tr><td>P18: The provision of information about search progress, while users await results influences users' satisfaction with RAs. Users who are informed about RAs' search progress (while waiting for recommendations) are more satisfied with the RAs.</td></tr><tr><td>P19: Response time influences users' satisfaction with RAs. The longer the RAs' response time, the lower the users' satisfaction with the RAs.P20: Recommendation content influences users' evaluations of RAs.P20a: Familiar recommendations increase users' trust in the RAs.P20b: The composition of the list of recommendations, as reflected by a balanced representation of familiar and unfamiliar (or new) product recommendations, influences users' trust in, perceived usefulness of, and satisfaction with RAs.P20c: The provision of detailed information about recommended products increases users' trust in, perceived usefulness of, and satisfaction with RAs.P20d: The provision of explanation on how the recommendations are generated increases users' trust in and satisfaction with RAs.</td></tr><tr><td></td><td>P21: Recommendation format influences users' perceived usefulness of, perceived ease of use of, and satisfaction with the RAs. RAs with clear navigational path and layout are considered more useful, easier to use, and more satisfactory than those without.</td></tr><tr><td rowspan="7">2.3</td><td>How do other factors (i.e., factors related to user, product, and user-RA interaction) moderate the effects of RA use and RA characteristics on users' evaluations of RAs?</td></tr><tr><td>P22: Product type moderates the effects of RA use on users' trust in and perceived usefulness of RAs. Users have higher trust in RAs for experience products and higher perceived usefulness of RAs for search products.</td></tr><tr><td>P23: Product expertise moderates the effects of RA use on users' evaluations of RAs (i.e., trust, perceived usefulness, perceived ease of use, satisfaction). The higher the product expertise of the users, the less favorable the users' evaluations of RAs.</td></tr><tr><td>P24: Product expertise moderates the effects of RA type on users' evaluations of RAs (i.e., trust, perceived usefulness, perceived ease of use, satisfaction). The higher the product expertise of the users, the more (less) favorable the users' evaluations of feature-based (needs-based) RAs. The higher the product expertise of the users, the more (less) favorable the user's evaluations of content-filtering (collaborative-filtering) RAs.</td></tr><tr><td>P25: User-RA similarity moderates the effects of RA use on users' trust in, satisfaction with, and perceived usefulness of RAs. The more the RAs are perceived to be similar to their users, the more they are considered to be trustworthy, satisfactory, and useful.</td></tr><tr><td>P26: User's familiarity with RAs moderates the effects of RA use on trust in the RAs. Increased familiarity with RAs leads to increased trust in the RAs.</td></tr><tr><td>P27: The confirmation/disconfirmation of expectations about RAs moderates the effects of RA use on users' satisfaction with the RAs. Confirmation or positive disconfirmation of users' expectations about RAs contributes positively to users' satisfaction with the RAs. In contrast, negative disconfirmation of users' expectations about RAs contributes negatively to users' satisfaction with the RAs.</td></tr><tr><td rowspan="2">2.4</td><td>How does provider credibility influence user's evaluations of RAs?</td></tr><tr><td>P28: Provider credibility, determined by the type of RA providers and the reputation of RA providers, influences users' trust in RAs. RAs provided by independent third party websites are considered more trustworthy than those provided by vendors' websites. RAs provided by reputable websites are considered more trustworthy than those provided by websites that are unknown or non-reputable.</td></tr></table>
