---
otero_id: 16798
otero_key: "NG2ZVF87"
title: "The impact of enterprise architecture management on information systems architecture complexity"
authors: "Jannis Beese; Stephan Aier; Kazem Haki; Robert Winter"
year: "2023"
journal: "European Journal of Information Systems"
doi: "10.1080/0960085x.2022.2103045"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The impact of enterprise architecture management on information systems architecture complexity

Jannis Beese, Stephan Aier, Kazem Haki & Robert Winter

To cite this article: Jannis Beese, Stephan Aier, Kazem Haki & Robert Winter (2022): The impact of enterprise architecture management on information systems architecture complexity, European Journal of Information Systems, DOI: 10.1080/0960085X.2022.2103045

To link to this article: https://doi.org/10.1080/0960085X.2022.2103045

CO © 2022 The Author(s). Published by Informa UK Limited, trading as Taylor & Francis Group.

![](/api/attachments/NG2ZVF87/fulltext/images/7840f8640d81b6f227484599fa42715aed5c3c730e0a88699e650e795216a451.jpg)

Published online: 02 Sep 2022.

![](/api/attachments/NG2ZVF87/fulltext/images/8a8376331e868161e11a87f191bd939b06f2cc7be677f1975059b7e9671aca3f.jpg)

Submit your article to this journal

![](/api/attachments/NG2ZVF87/fulltext/images/f9a5d0404bd0049dc64f8dc1efd5d30d726030de92998d50f26eaedc0fc907db.jpg)

Article views: 595

![](/api/attachments/NG2ZVF87/fulltext/images/96e888c2755cda98d145fc41e1b75e711faab448361e93ac6c45efe0a0d81920.jpg)

View related articles

![](/api/attachments/NG2ZVF87/fulltext/images/24160a0c3517a37b226ecdc06623b6826df654eb860eefa8f2c2bc9cf6cbc939.jpg)

View Crossmark data

EMPIRICAL RESEARCH

∂ OPEN ACCESS

Check for updates

# The impact of enterprise architecture management on information systems architecture complexity

Jannis Beese<sup>a</sup>, Stephan Aier<sup>a</sup>, Kazem Haki <sup>b</sup> and Robert Winter<sup>a</sup>

<sup>a</sup>Institute of Information Management, University of St Gallen, St Gallen, Switzerland; <sup>b</sup>Geneva School of Business Administration (HES-SO), HEG Genève, Switzerland

## ABSTRACT

Significant investments in information systems (IS) over the past decades have led to increasingly complex IS architectures in organisations, which are dificult to understand, operate, and maintain. We investigate this development and associated challenges through a conceptual model that distinguishes four constituent elements of IS architecture complexity by diferentiating technological from organisational aspects and structural from dynamic aspects. Building on this conceptualisation, we hypothesise relations between these four IS architecture complexity constructs and investigate their impact on architectural outcomes (i.e., eficiency, flexibility, transparency, and predictability). Using survey data from 249 IS managers, we test our model through a partial least squares (PLS) approach to structural equation modelling (SEM). We find that organisational complexity drives technological complexity and that structural complexity drives dynamic complexity. We also demonstrate that increasing IS architecture complexity has a significant negative impact on eficiency, flexibility, transparency, and predictability. Finally, we show that enterprise architecture management (EAM) helps to ofset these negative efects by acting as a moderator in the relation between organisational and technological IS architecture complexity. Thus, organisations without adequate EAM are likely to face large increases in technological complexity due to increasing organisational complexity, whereas organisations with adequate EAM exhibit no such relation.

ARTICLE HISTORY Received 23 March 2020 Accepted 5 July 2022

KEYWORDS Information systems architecture; complexity; enterprise architecture management

## 1. Introduction

Technological advances over the last decade have led to the development of large-scale interconnected information systems (IS) architectures, upon which organisations rely to conduct their daily business operations (Henfridsson & Bygstad, 2013; Legner et al., 2017). Recent implications of IS, such as sophisticated digital service and product oferings have further fuelled this growth through significant IS investments (McKelvey et al., 2016). Examples range from public electronic health records (S. Hansen & Baroody, 2019) and sophisticated cross-organisational finance platforms (Gomber et al., 2018) to specific retailers that open up new digital sales and distribution channels (R. Hansen & Kien, 2015). We investigate this development and associated challenges from an architectural perspective that considers the complete ensemble of all IS components in an organisation. Consequently, the term IS architecture refers to the entire set of all fundamental IS components and their interdependencies, as well as organisational processes and management eforts to keep local IS investments in line with long-term, enterprise-wide objectives (Haki et al., 2020; Zachman, 1987).

On the one hand, the increasing prevalence of IS has been theorised as a competitive advantage (Mata et al., 1995) and large-scale interconnected

IS architectures are commonly associated with productivity increases (Melville et al., 2004). On the other hand, the inherent complexity of such rapidly growing and constantly changing IS architectures also causes issues in their development and maintenance (Dwivedi et al., 2014; Haki et al., 2020). For example, IS components generally do not act in isolation, but are interdependent with other IS components (Bernus & Schmidt, 2006). Therefore, any changes (e.g., in reaction to extended customer interactions or new business requirements) to a single IS component may have unintended efects on multiple related IS components (Mocker, 2009). Since IS development is usually carried out simultaneously in several diferent IS projects, this leads to potentially inconsistent or redundant applications, software systems, and IT infrastructure components (Hanseth & Lyytinen, 2010). In efect, increasing complexity causes the overall IS architecture to become dificult to maintain and organisations struggle to flexibly respond to required or desired changes (Schmidt & Buxmann, 2011).

In response to these challenges, researchers have investigated how to better restrain and control the development of IS architectures (Cram et al., 2016;

Wiener et al., 2016). In practice, large organisations commonly employ enterprise architecture management (EAM), referring to enterprise-wide IS standardisation and harmonisation eforts to avoid unnecessary redundancies and inconsistencies (Aier & Winter, 2009; Ross et al., 2006). EAM activities thereby allow to align local short-term, projectrelated IS investments with long-term, organisationwide objectives (Sidorova & Kappelman, 2011). In the following, we use the term architectural outcomes to refer to these long-term, organisation-wide EAM objectives, comprising eficiency, i.e., the ability to provide all necessary IS capabilities with minimal resources (Lange et al., 2016; Schmidt & Buxmann, 2011), flexibility, i.e., the ability to quickly adapt an organisation’s IS to changing conditions or objectives (Amarilli et al., 2016; Li & Madnick, 2015), transparency, i.e., the ability to understand how an organisation’s IS operate (Attewell, 1992), and predictability, i.e., the ability to predict the efects of changes on IS (Geraldi, 2009; Renn et al., 2011).

Conceptually, our research builds on the work of Xia and Lee (2005) on information systems development project (ISDP) complexity, who distinguish structural and dynamic, as well as technological and organisational aspects. This distinction provides a useful foundation, which, in line with the EAM perspective, goes beyond a purely technical view on IS architecture complexity to also include organisational aspects.

In this context, the purpose of the paper at hand is threefold. First, we transfer Xia and Lee's (2005) model to IS architecture and extend it by articulating the relations between the diferent building blocks of IS architecture complexity. Second, we analyse the efect of IS architecture complexity on architectural outcomes (i.e., eficiency, flexibility, transparency, and predictability). Third, we systematically specify the role of EAM in moderating the relation between IS architecture complexity and architectural outcomes. Overall, we pose the following research question:

RQ: What is the relation between IS architecture complexity and architectural outcomes, and how is this relation afected by EAM?

Methodologically, we first conduct a series of sequential focus group sessions to hypothesise relations between the identified constructs, based on the existing conceptualisation of Xia and Lee (2005), and to develop scale items for a quantitative survey instrument. Subsequently, we collect 249 survey responses from IS managers to test our hypotheses through a partial least squares (PLS) approach to structural equation modelling (SEM; Jr., J. Hair et al., 2014).

Our results clarify the links between the organisational and technological as well as the structural and dynamic aspects of IS architecture complexity. Furthermore, we use this conceptualisation to analyse the impact of IS architecture complexity on related architectural outcomes, which complements extant empirical studies (e.g., Cong & Romero, 2013; Schilling et al., 2017). Finally, we explicate the impact of EAM on the relation between IS architecture complexity and architectural outcomes by demonstrating a highly significant moderation efect of EAM on the relation between the organisational and technological components IS architecture complexity. Specifically, we find that EAM helps to limit the extent to which increases in structural organisational complexity lead to increases in structural technological complexity, thereby reducing the overall negative efects (in terms of architectural outcomes) of increasing IS architecture complexity in large organisations.

## 2. Background and theoretical development of hypotheses

IS architecture complexity is a multifaceted construct, which has been reflected in a number of research streams from both theoretical and empirical perspectives. Stated concisely, the theoretical research stream acknowledges complexity as an inherent property of many modern IS and discusses how theoretical perspectives, such as complex adaptive systems (CAS), can be applied to better understand this complexity (Benbya & McKelvey, 2006; Haki et al., 2020; Merali, 2006; Sharma & Yetton, 2007). Furthermore, the ever-increasing need to address practical issues arising from increasingly complex IS architecture in large organisations has led to another stream of empirical research that investigates specific challenges. Empirical studies include research on application portfolio complexity (Aleatrati Khosroshahi et al., 2016; Mocker, 2009), enterprise architecture complexity (Lakhrouit & Baïna, 2016; Schütz et al., 2013), IS program complexity (Piccinini et al., 2014), and dynamic efects of IS architecture complexity (Schilling et al., 2017). We aim to consolidate these insights, by considering both technological and organisational aspects of IS architecture complexity, while simultaneously evaluating the potential of EAM to reduce technological complexity.

Integrating this corpus of extant research requires a high-level organising frame of reference that allows to conceptualise, develop, and diferentiate key aspects of IS architecture complexity. We opt for the framework of Xia and Lee (2005), as it is empirically wellgrounded and suficiently general to be relevant to our context. Regarding the latter point, we note, however, that this framework was originally developed to measure information systems development project (ISDP) complexity, a construct that is diferent from our research context (i.e., single IS development projects vs enterprise-wide architectural considerations). Thus, construct development and validation requires a careful adaptation procedure to ensure that the phrasing of related measurement items matches the IS architecture context (MacKenzie et al., 2011), for which we collect foundational qualitative data from focus groups in the first phase of our research design.

![](/api/attachments/NG2ZVF87/fulltext/images/a15eb6852a39e0935b3667e6fe55cf62458505c574b79aa303dddc359d03da5b.jpg)  
Figure 1. Conceptualisation of IS architecture complexity, based on .Xia and Lee (2005)

Xia and Lee (2005) distinguish four diferent elements of ISDP complexity along two dimensions (see, Figure 1). First, structural complexity (capturing the size, multiplicity, diversity and interdependencies of related components) is diferentiated from dynamic complexity (capturing the rate and pattern of changes). Second, technological complexity (complexity in the technological setting, covering applications, users, interfaces, and technologies, as well as related interdependencies and coordination activities) is diferentiated from organisational complexity (complexity in the organisational setting, covering business processes, workflows, organisational roles and structures, as well as related interdependencies and coordination activities). Combining these two dimensions results in four components of IS architecture complexity (Xia & Lee, 2005, pp. 55–56): Structural organisational complexity (SORG), Dynamic organisational complexity (DORG), Structural technological (IT) complexity (SIT), and Dynamic technological (IT) complexity (DIT).

In the following, we elaborate on these distinctions in the context of IS architecture complexity. We also discuss the role and impact of EAM on IS architecture complexity as well as architectural outcomes that are impeded by high levels of IS architecture complexity.

## 2.1. Structural and dynamic aspects of IS architecture complexity

We distinguish between complexity arising from the structural setup of an IS architecture and complexity that is due to dynamic aspects (Schilling et al., 2017; Schneider et al., 2014; Xia & Lee, 2005).

## 2.1.1. Structural complexity

Structural complexity refers to complexity that can be evaluated through structural properties of the IS architecture, essentially capturing its scope, size, and variety, as well as the interdependencies among its constituent components (Xia & Lee, 2005). All these aspects (scope/ size, variety, and interdependencies) in combination lead to structurally complex IS architectures.

Regarding the scope and size of IS architectures, structurally complex systems generally involve a large number of interacting components (Benbya & McKelvey, 2006). Thus, related studies on IS architecture complexity commonly include measures that cap ture the size and scope of the entire set of IS in organisations (Aleatrati Khosroshahi et al., 2016; Mocker, 2009; Piccinini et al., 2014; Xia & Lee, 2005).

However, a large set of unconnected IS components alone does not imply a structurally complex IS architecture. Instead, structural complexity of IS architecture arises from multiple interdependencies among a large set of diverse, individual components, which create a tightly interrelated and entangled ensemble (Benbya & McKelvey, 2006; Mocker, 2009; Schneider et al., 2014). Therefore, it is necessary to evaluate interactions among subgroups of components (Tait & Vessey, 1988), the overall level of integration within the constituent components of IS architecture (Aleatrati Khosroshahi et al., 2016; Ribbers & Schoo, 2002), and the alignment between the diferent technical and organisational components (Wood, 1986). For example, Mocker (2009) investigates interfaces between IS components and functional overlaps to measure interdependency-related application portfolio complexity.

Finally, the structural complexity of IS architecture is compounded by the diversity of its constituent components. In this context, diversity is a multidimensional construct, comprising variety (i.e., a large number of diferent component types), separation (i.e., diferent component types are clearly distinguishable), and disparity (i.e., component types are evenly distributed; Baccarini, 1996; Ribbers & Schoo, 2002).

## 2.1.2. Dynamic complexity

Dynamic complexity captures complexity due to the temporal dynamics of the IS architecture. Frequent technological and organisational changes require that organisations continuously adapt their IS architecture, often causing unintended consequences through complex interactions over time (Beese et al., 2015; Haki et al., 2020; Schilling et al., 2017). Therefore, studies on IS architecture complexity commonly include constructs that measure dynamism (referring to the overall rate of change, i.e., how often something changes; Meyer & Curley, 1991) and variability (referring to the extent of changes, i.e., how large changes are; Ribbers & Schoo, 2002). Additionally, several studies emphasise the role of uncertainty, instability, unpredictability (Gerow et al., 2014), and ambiguity (McKeen et al., 1994) during IS development.

## 2.1.3. Relation between structural and dynamic complexity

In their research on ISDP complexity, Xia and Lee (2005) find structural and dynamic complexity to be distinct yet related constructs (cf., Table 5, Xia & Lee, 2005, p. 70). If an organisation is structurally complex, it is very dificult to predict and control the dynamic efects of changes over time in IS development (Xia & Lee, 2005). Similarly, we expect the structural complexity of IS architectures to contribute to its dynamic complexity, since it becomes increasingly dificult to adequately prepare for and react to unforeseen organisational changes or shifts in technology trends (Gerow et al., 2014). We therefore hypothesise a relation between static and dynamic complexity in the context of IS architecture complexity: if the static structure of an IS architecture is already complex, this will impact the complexity of its dynamic behaviour over time:

H1. Structural complexity is positively associated with dynamic complexity.

## 2.2. Organisational and technological aspects of IS architecture complexity

IS architectures are recognised as complex sociotechnical systems, in which organisational components interact with technological components to process information (Alter, 2002; Haki et al., 2020; Lyytinen & Newman, 2008). Consequently, we distinguish organisational complexity from technological complexity in our conceptualisation (Lyytinen & Newman, 2008; Xia & Lee, 2005).

## 2.2.1. Technological complexity

Technological complexity refers to the complexity of the technological setting (Xia & Lee, 2005). This includes, for example, technology platforms (Hanseth & Ciborra, 2007), system design and integration techniques (France & Rumpe, 2007), computing languages (Meyer & Curley, 1991), and development methodologies (McKeen et al., 1994; Meyer & Curley, 1991). Studies on IS architecture complexity often also consider the age of technological IS components (Mocker, 2009), arguing that complexity is primarily an issue for outdated IS architectures with many legacy systems and obsolete components (Beetz & Kolbe, 2011; Kroenke et al., 2013).

## 2.2.2. Organisational complexity

Organisational complexity captures the complexity of the organisational setting (Xia & Lee, 2005). Since the technological components of an IS architecture are intractably linked to the surrounding organisational setting (Alter, 2002), the complexity of this organisational setting is thus reflected in the IS architecture itself. Organisational components that contribute to IS architecture complexity include, for example, organisational hierarchies and team compositions (Barki et al., 2001; Bosch-Rekveldt et al., 2011), business processes and workflows (Scott & Vessey, 2002), and the intricacy of IT supported business tasks (Petter et al., 2008).

## 2.2.3. Relation between organisational and technological complexity

In large organisations, IS managers and architects are continuously trying to align organisational and technological objectives (Brosius et al., 2018; Haki & Legner, 2013). In practice, this alignment usually takes place by making technological changes in reaction to organisational changes (Ramasubbu et al., 2014; Winter & Schelp, 2008). That is, the organisation first agrees on a target business architecture (e.g., new business processes, workflows, and organisational structures) and then the technological aspects of the IS architecture (e.g., new IT infrastructure and tools) are adapted adequately support these organisational requirements (Ross et al., 2006). This relation is further backed by empirical evidence that confirms Conway’s law (Conway, 1968) to still hold true in many modern organisations (Colfer & Baldwin, 2016), essentially arguing that the IT artefacts developed by an organisation tend to mirror the structure of the organisation itself (Constantinides et al., 2018). Consequently, we hypothesise a positive association between organisational complexity and technological complexity.

H2. Organisational complexity is positively associated with technological complexity.

## 2.3. The role of enterprise architecture management

In response to increasing IS architecture complexity, many organisations develop and maintain architectural plans, which reflect the organisation’s business and IT landscape in its current and targeted future states (Lange et al., 2016; Niemann, 2006). EAM, referring to associated management activities, aims to address associated challenges of IS architecture complexity by providing a holistic view on an organisation’s IS architecture (Ross et al., 2006; Schmidt & Buxmann, 2011) and by purposefully guiding its development towards enterprise-wide objectives (Aier et al., 2011; Boh & Yellin, 2006). In practice, EAM is commonly implemented through the aforementioned architecture plans (Lange et al., 2016) and architecture principles (Greefhorst & Proper, 2011), as well as related organisational roles and responsibilities for monitoring and enforcing these plans and principles through compliance assessments (Boh & Yellin, 2006; Cram et al., 2016; Foorthuis, 2012). More recently, there have also been increasing eforts to establish a more agile approach to EAM, aiming at a more direct interaction with all involved stakeholders while continuously revising and communicating the central architectural artefacts (Buckl et al., 2011; Schilling et al., 2018; Winter, 2014).

While acknowledging research that highlights adoption issues in EAM initiatives (Ross & Quaadgras, 2012; Simon et al., 2014), it is generally expected that a higher level of EAM maturity in an organisation will lead to improved architectural outcomes (Lange et al., 2016; Ross, 2003; Simonsson et al., 2010, 2008). Consequently, when studying the relation between organisational complexity and technological complexity, we expect that the observed efects will depend on the presence of a mature EAM function with well-established roles, responsibilities, and processes, and which has a high reach and impact in the overall organisation (Boh & Yellin, 2006; Lange et al., 2016; Schilling et al., 2018). Therefore, we hypothesise

H3. EAM moderates the relations between organisational complexity and technological complexity.

## 2.4. Architectural outcomes

Ultimately, we are interested in understanding the relative impact of IS architecture complexity in terms of architectural outcomes (Lange et al., 2016; Schmidt & Buxmann, 2011), referring to desirable, organisationwide objectives, which may be negatively impacted by high levels of IS architecture complexity. Several empirical studies discuss the efects of IS architecture complexity and highlight negative consequences, such as increased coordination eforts, higher failure rates of large implementation projects, and diminished flexibility (e.g., Beetz & Kolbe, 2011; Hanseth & Bygstad, 2012; Widjaja et al., 2012). EAM aims to prevent or mitigate these negative consequences by working towards desirable architectural outcomes, resulting from a systematically governed IS development in line with long-term, enterprise-wide objectives.

Common architectural outcomes include eficiency, flexibility, transparency, and predictability. Eficiency refers to the ability of the organisation to only use minimal resources while still ensuring that all necessary IS capabilities are provided with suficient quality (Lange et al., 2016; Schmidt & Buxmann, 2011). Flexibility captures how quickly an organisation can adapt their IS architecture in reaction to novel or changing objectives and conditions (Amarilli et al.,

2016; Li & Madnick, 2015). Transparency relates to the ability to track and understand the detailed operation of the organisation’s IS architecture (Attewell, 1992). Finally, predictability refers to the organisation’s ability to predict the overall impact of changes and adjustments made to the IS architecture (Geraldi, 2009; Renn et al., 2011).

In general, evidence points towards a negative relation between the technological complexity of IS architecture and architectural outcomes, i.e., for a group of otherwise similar organisations, those with a technologically more complex IS architecture are expected to score worse in terms of architectural outcomes. Both Mocker (2009) and Aleatrati Khosroshahi et al. (2016) confirm a negative correlation between several complexity indicators (e.g., a large amount of application interfaces or redundant IT applications) and architectural outcomes, demonstrating that more complex IS architectures tend to require higher operation and maintenance costs. Furthermore, high levels of IS architecture complexity prevent people from recognising optimal ways to adapt IS to cope with new requirements, thereby decreasing transparency (Arteta & Giachetti, 2004; Beese et al., 2015). This also reduces the capacity of the IT function to adequately adapt to changing demands and opportunities, leading to low levels of flexibility (Tiwana & Konsynski, 2010). Similarly, dynamic complexity has been linked to increasing dificulties to predict IS behaviour (Xue et al., 2011). Overall, we thus hypothesise

H4. Technological complexity is negatively associated with architectural outcomes.

Figure 2 depicts the overall research model and hypotheses.

## 3. Research method

For testing our theoretically derived research model (see, Figure 2), we first developed a survey by adapting existing scales to the context of IS architecture complexity (survey development), which was then used to quantitatively test our hypotheses (quantitative evaluation).

Survey development: We followed the recommendations of MacKenzie et al. (2011) for the measurement adaptation and development process. Building on our theoretical foundation, we first conducted a sequential series of focus group workshops to support the conception of a questionnaire (Freitas et al., 1998). We opted for focus groups as a means for collecting data from multiple participants, since this allowed us to evaluate the relevance of theoretically derived constructs from multiple perspectives and to discuss subtle nuances in expression and meaning in the formulation of specific measurement items (Freitas et al., 1998; Stewart et al., 2007).

![](/api/attachments/NG2ZVF87/fulltext/images/2a139d52d3078a2a26d51c080a6345c93ee0951775e8a4ddca2b276df310c228.jpg)  
Figure 2. Research model and hypotheses.

Specifically, we conducted a series of four two-day focus group workshops in 2014 and 2015 (see, Table 1) with senior enterprise architects and IS managers from ten large European companies from the banking, insurance, logistics, and utilities sectors. We selected participants based on their knowledge, their experience within the firm, and their ability to contribute to the topic. Each workshop was prepared and moderated by two of the authors, following the guidelines of Stewart et al. (2007), while two other researchers took notes for subsequent analysis. In between the workshops, we evaluated these notes and additional material (e.g., slide-sets, memos, and meeting notes from participating companies). During each workshop, participants were grouped into three smaller subgroups (two for the last workshop) for discussions, taking care to specifically grouped participants from diferent industries and diferent companies together to ensure a more general view on the topic.

Table 1. Overview of focus group workshops.

<table><tr><td>Date</td><td>Participants</td><td>Goal</td></tr><tr><td>June 2014</td><td>16</td><td>Develop an understanding of IS architecture complexity and its role in organisations.</td></tr><tr><td>October 2014</td><td>13</td><td>Identify drivers of complexity, as well as common goals of complexity management.</td></tr><tr><td>February 2015</td><td>13</td><td>Discuss relations between the constructs (i.e., hypotheses).</td></tr><tr><td>May 2015</td><td>8</td><td>Validate a preliminary version of the conceptual model and the questionnaire.</td></tr></table>

In general, the moderators first introduced the topic during each workshop, but then had almost no involvement during the actual sub-group discussions in order to avoid introducing any researcher bias. The aim of the first workshop was to develop a mutual understanding of IS architecture complexity in large organisations. Based on this understanding, participants then discussed their eforts to better manage IS architecture complexity and associated challenges during the second workshop. In the third workshop, participants grouped and positioned the previously identified constructs in relation to each other and discussed interdependencies. The final workshop was used to review and validate a preliminary version of the conceptual model, including a discussion of the specific formulations in the questionnaire (Freitas et al., 1998). This was the only focus group workshop during which we initially introduced a concrete artefact (the questionnaire constructs and formulations) into the discussion and more strongly moderated the discussion to ensure that all items are reviewed (Freitas et al., 1998).

Following MacKenzie et al. (2011), we then assessed the content validity of the items and the resultant measurement scales through a sorting exercise and a pilot test with twelve IS researchers. For the sorting procedure, participants were asked to group the proposed items into conceptually matching categories or assign them to a “not fitting” pile. Furthermore, participants should point out any potential issues with the items (e.g., ambiguous or badly phrased) or the constructs (e.g., missing aspects). A combined analysis of the focus group data, the results from the sorting procedure, and the statistics from the pilot test then led to the final set of measurement items that were included in the survey (see Appendix A).

Quantitative evaluation: We then collected a first data set from 106 respondents via a paper-based survey handed out to 123 participants of a European IS practitioner conference in July 2015 (86% response rate), using a five point Likert scale [(1) Strongly disagree; (2) Disagree; (3) Neither agree nor disagree; (4) Agree; (5) Strongly agree] to measure participant agreement with several statements about complexity, EAM, and architectural outcomes in their organisations (see Appendix A). At this conference, IT managers and enterprise architects, mostly from large European companies, presented and discussed current EAM-related developments in their organisations. As suggested by Cycyota and Harrison (2002), the research project was introduced by a wellknown and respected community member, resulting in a rather high response rate (Sivo et al., 2006). The survey was handed out after a break between two sessions when the participants entered the conference room, thereby ensuring that each participant was approached at most once. Based on this data set, an initial estimate of predictive power (following Faul et al., 2009) indicated that roughly 240 responses in total were required in order to be statistically significant at the p < .01 level. Thus, we sent an online survey to an additional 571 contacts and collected data from an additional 143 respondents (25% response rate) during July and August 2015, totalling 249 responses from both the paper-based survey and the online survey. For both surveys, we took care that only relevant respondents – experienced IS managers of large organisations – were targeted.

Survey data was analysed according to the PLS-SEM guidelines of Gefen et al. (2011) and Ringle et al. (2012). We chose PLS-SEM over covariancebased SEM approaches to reduce the risk of overfitting during analysis (Gefen et al., 2011). The tests were performed using SmartPLS version 3.2.9. (Ringle et al., 2015). Missing values were handled through mean replacement and bootstrapping was conducted with a sample size of 5000 to assess path estimate significance (Jr., J. Hair et al., 2014).

## 4. Construct operationalisation and survey development

In the following we report on the results of the survey development phase and discuss the specific formulations that are used in our survey. See Table 7 in Appendix A for the precise wordings of all items, their loadings (“Ld”.) on the respective scale, and the associated t-values; Section 5 subsequently describes the quantitative data that is used to calculate these values.

Structural organisational complexity (SORG): Discussions in the focus groups revealed that structural organisational complexity is mainly driven by the necessity to adapt a large set of interdependent organisational structures to a quickly and continuously changing competitive environment (Winter & Schelp, 2008). Our operationalisation of structural organisational IS architecture complexity therefore comprises items that capture the need to support many diverse and interrelated business tasks as well as related workflows and functionalities (SORG1, SORG2, SORG4, SORG5, SORG7). This is particularly dificult for organisations with many crossdepartmental tasks and projects (SORG6), which may lead to inconsistencies and interdependencies that are not easy to untangle. Furthermore, participants highlighted the structural organisational complexity that is introduced through highly diverse user requirements, ranging from diferences in expertise and terminology to diferent understandings of business task requirements (SORG3).

Dynamic organisational complexity (DORG): Focus group participants generally agreed with the conceptualisation of dynamic complexity as “rate and pattern of changes” (Xia & Lee, 2005, p. 56) in the structural setting. Therefore, the operationalisation of dynamic organisational complexity targets the rate and pattern of changes in business requirements (DORG1), business tasks (DORG2), employees’ roles and positions (DORG3), and related workflows and processes (DORG5). Furthermore, participants emphasised the organisational complexity that accompanies functional changes in employed technologies (DORG4), since major system updates often occur through complex organisational processes.

Structural technological (IT) complexity (SIT): In line with related literature (e.g., Aleatrati Khosroshahi et al., 2016; Mocker, 2009), focus group participants afirmed that structural technological complexity results from the number and diversity of technological components (SIT5) as well as their interrelations (SIT4), leading to dificulties with coordination and integration (SIT2). Additionally, many participants voiced particular dificulties resulting from large numbers of system users (SIT1), leading to structurally very complex user role and access management systems that need to meet the users’ requirements while simultaneously complying with extant data protection regulations (SIT3).

Dynamic technological (IT) complexity (DIT): Like its organisational counterpart, the discussion on dynamic technological complexity emphasised the rate and pattern of changes in the individual technological components (DIT3) as well as in the overall IT landscape (DIT4). Moreover, focus group participants highlighted the complexity introduced by uncertainties and unclarities (e.g., through lacking documentation) in this setting, which prevents organisations from getting a clear understanding of current developments. Thus, our conceptualisation of dynamic technological complexity also targets uncertainties in the development of the IT landscape (DIT1) as well as unclear relations between diferent system components (DIT2).

Enterprise architecture management (EAM): In agreement with empirical research on the use of EAM in organisations (Lange et al., 2016; Niemi & Pekkola, 2017; Winter & Fischer, 2007), discussions focussed on classical EAM artefacts such as principles (EAM2), processes (EAM3), and guidelines (EAM4). Focus group participants also confirmed classical discussions on EAM (Boh & Yellin, 2006) by highlighting the importance of an adequate assignment of roles and responsibilities (EAM1), such as allocating decision rights to committees that reach beyond individual departments and projects (EAM5).

Architectural outcomes (AO): In line with Schmidt and Buxmann (2011), focus group participants clearly stated that the main targeted architectural outcomes are to ensure a sustainable development of the IS architecture by increasing eficiency while simultaneously providing suficient flexibility. Additionally, the use of EAM in large organisations is also increasingly ratified with transparency and predictability, which are compulsory to meet regulatory requirements and to manage and reduce organisational risks. Discussions concluded that these are four distinct but related constructs (eficiency, flexibility, transparency, and predictability), which, in combination, reflect the most important architectural outcomes. Consequently, we operationalise architectural outcomes as a reflective second-order construct comprising four sub-constructs.

Eficiency (EFF): Conversations in the focus group sessions confirmed that eficiency should essentially capture the ability to provide a high level of performance for comparatively low cost (EFF1), which fundamentally includes the cost-eficient operation and development of IS (EFF2). Moreover, participants agreed that this is commonly achieved by avoiding unnecessary redundancies (EFF3), in line with related empirical studies (e.g., Mocker, 2009).

Flexibility (FLEX): Discussants argued that flexibility primarily refers to an organisation’s ability to react with speed and dexterity to changes, by conducting necessary adjustments in time and quality (FLEX1). This ability is directly related to the potential of the organisation to anticipate and react to foreseeable changes in the future, such as new technological trends or major shifts in the organisation’s business environment (FLEX2). Furthermore, organisations also require efective processes that quickly deal with urgent unforeseen issues, for example, by being able to quickly deploy critical updates (FLEX3). Finally, focus group participants emphasised the importance of being able to quickly adopt new ideas and technologies in their target architectures (FLEX4).

Transparency (TRSP): Deliberations in the focus group sessions showed that transparency, in the context of IS architecture, is on the one hand related to providing transparency to end users (TRSP1) as well as developers and IT managers. This can, for example, manifest in an IT landscape that is easy to explain and communicate (TRSP2), which makes its use and operation quickly accessible to new members of the organisation (TRSP3). On the other hand, transparency is also related to the organisation’s ability to explain unexpected behaviour (TRSP4) to both internal and external stakeholders, such as regulatory agencies.

Predictability (PRED): Finally, focus group participants agreed that predictability should capture both the organisation’s ability to reliably estimate the costs and efects of changes (PRED1) and the ability to reliably maintain and operate the overall IS architecture. Thereby, reliable operation on the one hand refers to few failures and critical errors (PRED2) and on the other hand to few major changes that disrupt daily operations in unforeseen ways (PRED3).

## 5. Results

We now present the results of our quantitative analysis based on PLS-SEM (Gefen et al., 2011).

## 5.1. Data analysis and descriptive statistics

Initially, we carefully inspected all 249 collected responses from both the online and the paper-based survey and did not find any unusual response patterns or outliers. Furthermore, at most three items were left unanswered by any given respondent. Thus, we employed the full dataset of 249 responses in our analysis, using mean value replacement to deal with missing values (Gefen et al., 2011).

Table 2 shows the demographics of our collected data (industry, company size, and length of employment). We specifically targeted experienced IS managers in large organisations. Consequently, more than half of our responses come from organisations with more than 5000 employees and two out of three respondents have been with their current company for more than 6 years.

Table 2. Demographics of survey respondents (249 total responses).

<table><tr><td>Industry (233 responses)</td><td>Percent</td><td>Company size (237 responses)</td><td>Percent</td></tr><tr><td>Utilities</td><td>6.4 %</td><td>&lt;50</td><td>2.9 %</td></tr><tr><td>Financial services</td><td>30.0 %</td><td>50–249</td><td>8.0 %</td></tr><tr><td>Health care</td><td>3.4 %</td><td>250–999</td><td>10.2 %</td></tr><tr><td>Retail</td><td>4.7 %</td><td>1000–4999</td><td>27.8 %</td></tr><tr><td>Information and communication</td><td>13.7 %</td><td>&gt;5000</td><td>51.1 %</td></tr><tr><td>Government</td><td>5.2 %</td><td colspan="2">Length of employment (212 responses)</td></tr><tr><td>Manufacturing and processing</td><td>8.6 %</td><td>&lt; 2 years</td><td>5.7 %</td></tr><tr><td>Insurance</td><td>17.2 %</td><td>2–5 years</td><td>27.4 %</td></tr><tr><td>Transport and logistics</td><td>6.4 %</td><td>6–10 years</td><td>25.0 %</td></tr><tr><td>Others</td><td>4.3 %</td><td>&gt; 10 years</td><td>42.0 %</td></tr></table>

Table 3. Overview of constructs and scales $( { \mathsf { R } } ^ { 2 }$ values of the final model).

<table><tr><td>Construct</td><td>No. of items</td><td>Mean</td><td>Standard deviation</td><td>Composite reliability</td><td>Cronbach&#x27;s α</td><td>AVE</td><td> $R^2$ </td></tr><tr><td>SORG</td><td>7</td><td>4.022</td><td>0.889</td><td>0.810</td><td>0.734</td><td>0.383</td><td>-</td></tr><tr><td>DORG</td><td>5</td><td>3.089</td><td>0.967</td><td>0.793</td><td>0.677</td><td>0.440</td><td>0.270</td></tr><tr><td>SIT</td><td>5</td><td>3.529</td><td>0.971</td><td>0.851</td><td>0.780</td><td>0.538</td><td>0.370</td></tr><tr><td>DIT</td><td>4</td><td>3.254</td><td>1.018</td><td>0.861</td><td>0.785</td><td>0.608</td><td>0.595</td></tr><tr><td>EAM</td><td>5</td><td>3.168</td><td>1.021</td><td>0.850</td><td>0.788</td><td>0.534</td><td>-</td></tr><tr><td>AO ( $2^{nd}$  order)</td><td>15</td><td>2.974</td><td>1.040</td><td>0.908</td><td>0.889</td><td>0.418</td><td>0.309</td></tr><tr><td>Efficiency</td><td>3</td><td>2.809</td><td>0.876</td><td>0.811</td><td>0.654</td><td>0.590</td><td>0.553</td></tr><tr><td>Flexibility</td><td>4</td><td>3.079</td><td>0.950</td><td>0.867</td><td>0.794</td><td>0.623</td><td>0.730</td></tr><tr><td>Transparency</td><td>4</td><td>2.827</td><td>0.937</td><td>0.869</td><td>0.798</td><td>0.624</td><td>0.767</td></tr><tr><td>Predictability</td><td>3</td><td>3.192</td><td>0.895</td><td>0.842</td><td>0.726</td><td>0.641</td><td>0.618</td></tr></table>

## 5.2. Measurement model and construct validity tests

Table 3 presents general scale information (number of items, mean, and standard deviation) and statistical quality criteria (composite reliability, Cronbach’s α, average variance extracted (AVE), and $\mathrm { R } ^ { 2 }$ values) of the final model (see, Figure $_ { 3 ; }$ Gefen et al., 2011). All constructs are measured in reflective mode, since the individual items are indicative of the latent variables, but do not constitute a complete, exhaustive description (Ringle et al., 2012). Similarly, the second order architectural outcomes (AO) construct is of the reflective-reflective type using the indicator reuse approach (Lohmöller, 1989). As recommended by Lohmöller (1989) and Gefen et al. (2011), the constituent first order components have similar numbers of indicators.

Regarding construct reliability, the values for the composite reliability (> 0.7) and Cronbach’s α (> 0.6) are within acceptable ranges (Jr., J. Hair et al., 2014). Since the average variance extracted is below 0.5 for the SORG and DORG constructs, we conducted a series of separate factor analyses for all first order constructs (i.e., all constructs except AO) following Gefen and Straub (2005), to ensure unidimensionality. In all cases a single underlying factor was extracted that explains most of the variance and on which the items load evenly. This, in combination with the good values for composite reliability (> 0.7, cf., Jr., J. Hair et al., 2014), provides evidence that the constructs are explained by their indicators rather than by error terms (Gefen & Straub, 2005), and consequently establishes convergent validity. In the final measurement model no indicator has a loading below 0.4 (Jr., J. Hair et al., 2014) and all indicators are highly significant at the 0.01 level (t-value $> 2 . 5 7 6 )$ , see Appendix A.

![](/api/attachments/NG2ZVF87/fulltext/images/cf19839dadb67af682e2922fd3ac688551f313eb115bdc273791f7f96cf9d09d.jpg)  
Figure 3. Final model with second order constructs.

Discriminant validity was confirmed using Heterotrait-Monotrait (HTMT) analysis in combination with a cross-loading analysis (see Appendix B). Finally, we tested the predictive relevance of the model with the non-parametric Stone-Geisser test $( \mathrm { J r . , J }$ . Hair et al., 2014); also see Appendix B.

## 5.2.1. Moderation analysis

Based on our theoretical discussion and on our focus group data, we hypothesise (H4) that EAM afects the strength of the relation between organisational complexity (SORG and DORG) and technological complexity (SIT and DIT). We analysed this moderation efect using a product indicator approach with orthogonalisation in SmartPLS, which is suitable for reflective models and recommended for hypothesis testing (Jr., J. Hair et al., 2014).

To avoid misinterpreting interaction efects and confusing simple direct efects with actual moderation efects, we first analysed alternative models, including a baseline model without the moderator variable (Model 1), a model with only direct efects (Model 2), and a model with full moderation efects (Model 3; J. F. Hair et al., 2013; Henseler & Fassott, 2010; Jr., J. Hair et al., 2014). Figure 3 displays these models as well as the final model (Model 4), which we used in subsequent analyses. Figure 3 also shows the path coeficients and significance levels $( ^ { * * } \colon \mathtt { p } < 0 . 0 5 ;$ $\mathsf { \Psi } ^ { \mathsf { * * * } } \colon \mathsf { p } < 0 . 0 1 )$ for each path, as well as the $\mathrm { R } ^ { 2 }$ values for all endogenous constructs. Statistically non-significant paths $\mathrm { ( p > 0 . 1 ) }$ are drawn as dashed lines.

Looking at Model 1 in Figure 3, we find our hypotheses confirmed in this baseline model, with the single exception of the path from SORG to DIT. Considering the statistically highly significant other paths, the relatively large $\mathrm { R } ^ { 2 }$ values, and the results from the previous validity tests, this establishes a good starting point for further moderation analysis. Model 2 in Figure 3 then shows that EAM has a strong direct efect on both SIT and DIT, thus requiring us to check all potential moderation efects (i.e., EAM×SORG→SIT, EAM×DORG→SIT, EAM×SORG→DIT, and EAM×DORG→DIT). Model 3 in Figure 3, however, reveals that only the moderation efect EAM×SORG→SIT is significant at the $\mathtt { p } < 0 . 0 1$ level, whereas all other moderation efects are not statistically significant $\mathrm { ( p > 0 . 1 ) }$ . Furthermore, Model 4 in Figure 3 confirms that this moderation efect (EAM×SORG→SIT) remains significant if the other moderation efects are removed from the model. Consequently, Model 4, including both direct efects (EAM→SIT and EAM→DIT), one moderation efect (EAM×SORG→SIT), and excluding the insignificant direct relation (SORG→DIT, which is fully mediated via the SIT and DORG constructs) is used for subsequent analysis and hypothesis testing.

We then conducted a simple slope analysis for the moderation efect (see, Figure 4) to better understand how the moderator variable EAM afects the relation between SORG and SIT (Aiken et al., 1991). Accordingly, we calculated two additional regressions that represent the relation between SORG and SIT when EAM is below or above average (i.e., when the z-value of EAM is +1 standard deviation $\mathrm { o r } \ - 1$ standard deviation). Figure 4 displays these two regressions in addition to the default regression (i.e., EAM at mean), where both axes are scaled to standard deviations of the respective constructs. This reveals a noticeable diference: while there is a clear relation between SORG and SIT on average (slope = 0.198), this relation is significantly more pronounced for low levels of EAM (slope = 0.406) and almost non-existent for high levels of EAM (slope = −0.008). In non-technical terms, this implies that organisations without a mature (in terms of well-established roles, responsibilities and processes) and organisationally wellanchored (in terms of reach and acceptance) EAM function are likely to face large increases in technological complexity as a consequence of increasing organisational complexity. In contrast, organisations with a mature and well-anchored EAM tend to see almost no increase in technological complexity due to increasing organisational complexity.

## 5.3. Analysis of the final structural model

Figure 5 shows the final model with second order constructs, including path coeficients (the numbers next to the arrows) and $\mathrm { R } ^ { 2 }$ values (the numbers at the bottom right of each construct). All relations in Figure 5 are significant at the $\mathrm { ~ p ~ } < 0 . 0 1$ (\*\*\*) level, implying that it is very unlikely to observe these relations by chance. Path coeficients indicate the direct efect that one variable has on another variable; for example, if SORG increases by one standard deviation, then SIT is expected to increase by 0.20 standard deviations. Negative numbers indicate inverse relationships, e.g., if SIT increases, we expect AO to decrease. Finally, the $\mathrm { R } ^ { 2 }$ values specify the extent to which a certain construct can be explained by the predictor variables (all incoming arrows). Higher $\mathrm { R } ^ { 2 }$ values correspond to less unexplained variance. For multi-faceted constructs such as AO (Architectural Outcomes, $\mathrm { R } ^ { 2 } = 0 . 3 1 )$ , we expect that we are only able to explain a fraction of the total variance, since many other factors specific to a single organisation will also influence these constructs.

![](/api/attachments/NG2ZVF87/fulltext/images/3e8396640dab5330239db2e454621030e3f3535de439d0dd9b8cddbf900bcb3d.jpg)  
Structural Organizational Complexity  
Figure 4. Diferent moderation models.

To ensure that no significant path has been left out in the final model, we compared these results with an analyses of the saturated model (Gerbing & Anderson, 1988); see Appendix D. Next, we performed linear regression analysis tests between connected constructs to ensure that the variance inflation factors (VIF) and Durbin-Watson statistics are within acceptable thresholds (Kutner et al., 2005). Finally, we employed multi-group-analysis (Jr., J. Hair et al., 2014) to confirm that our final model does not difer significantly for diferent the respondent characteristics from Table 2 within our sample (see Appendix C) as well as to check for common method bias (Podsakof et al., 2003) and nonresponse bias (Gefen et al., 2011; Sivo et al., 2006) in our survey data.

After confirming the robustness of the final model, we then calculated the total efects (see, Table 4), i.e., the sum of direct and indirect efects between constructs (Jr., J. Hair et al., 2014). The efect sizes in Table 4 thus also reflect additional efects through intermediate constructs, and can therefore be used to investigate relations between constructs that are not directly connected in the final model (cf., Figure 5). Notably, we can see that all IS architecture complexity constructs (SORG, DORG, SIT, DIT) have highly significant negative efects on architectural outcomes (AO), whereas EAM has a highly significant positive efect (column AO in Table 4).

## 5.3.1. Hypothesis testing

Considering the preceding analysis, we now review our hypotheses. Table 5 provides an overview of the hypotheses along with the related paths in the final model (see, Figure 5).

H1 is mostly supported: there is a positive relation between structural complexity and dynamic complexity. In detail, we find that for organisational complexity there is a significant positive relation between SORG and DORG (0.52\*\*\*) and similarly for structural complexity there is a significant positive relation between SIT and DIT (0.50\*\*\*). In contrast, SORG is not directly associated with DIT, but rather constitutes a fully mediated efect. Consequently, this does not mean that there is no efect, but rather that total efect (see, Table 4, SORG→DIT: 0.338\*\*\*) can be fully explained by the indirect efects through the mediating constructs (i.e., SORG→SIT→DIT and SORG→DORG→DIT).

![](/api/attachments/NG2ZVF87/fulltext/images/202137d360a1b243caab92d60d2e49d00b901d2f4c837e0d6050a1322fb41e08.jpg)  
Figure 5. Simple slope analysis.

Table 4. Total efects in the final model (\*\*\*: p < 0.01).

<table><tr><td></td><td>DORG</td><td>SIT</td><td>DIT</td><td>AO</td><td>EFF</td><td>FLEX</td><td>TRSP</td><td>PRED</td></tr><tr><td>SORG</td><td>0.520***</td><td>0.346***</td><td>0.338***</td><td>-0.204***</td><td>-0.152***</td><td>-0.174***</td><td>-0.179***</td><td>-0.160***</td></tr><tr><td>DORG</td><td></td><td>0.281***</td><td>0.457***</td><td>-0.208***</td><td>-0.155***</td><td>-0.178***</td><td>-0.182***</td><td>-0.163***</td></tr><tr><td>EAM</td><td></td><td>-0.402***</td><td>-0.410***</td><td>0.241***</td><td>0.179***</td><td>0.206***</td><td>0.211***</td><td>0.189***</td></tr><tr><td>SIT</td><td></td><td></td><td>0.502***</td><td>-0.480***</td><td>-0.357***</td><td>-0.410***</td><td>-0.421***</td><td>-0.378***</td></tr><tr><td>DIT</td><td></td><td></td><td></td><td>-0.231***</td><td>-0.172***</td><td>-0.197***</td><td>-0.202***</td><td>-0.181***</td></tr><tr><td>AO</td><td></td><td></td><td></td><td></td><td>0.744***</td><td>0.854***</td><td>0.876***</td><td>0.786***</td></tr></table>

Table 5. Overview of hypotheses testing.

<table><tr><td>ID</td><td>Statement</td><td>Related paths in Figure 5</td><td>Result</td></tr><tr><td>H1</td><td>Structural complexity is positively associated with dynamic complexity.</td><td>SORG→ DORG: 0.52***SIT→ DIT:0.50***SORG→ DIT:(not significant)</td><td>Mostly supporteda</td></tr><tr><td>H2</td><td>Organisational complexity is positively associated with technological complexity.</td><td>SORG→ SIT:0.20***DORG→ DIT:0.32***SORG→ DIT:(not significant)DORG→ SIT:0.28***</td><td>Mostly supporteda</td></tr><tr><td>H3</td><td>EAM moderates the relations between organisational complexity and technological complexity.</td><td>EAM→ SIT:-0.40***EAM→ DIT:-0.21***EAM×SORG → SIT: -0.21***</td><td>Supported</td></tr><tr><td>H4</td><td>Technological complexity is negatively associated with architectural outcomes.</td><td>SIT→ AO:-0.37***DIT→ AO:-0.23***</td><td>Supported</td></tr></table>

<sup>a</sup>Except for the insignificant SORG→DIT relation

We find support for H3 and our analysis clarifies the nature of the moderation efect of EAM on the relation between organisational and technical complexity. First, we find a significant direct negative relation between EAM and SIT (−0.40\*\*\*) as well as EAM and DIT (−0.21\*\*\*), meaning that adequate EAM reduces technological complexity. Second, we observe a significant moderation efect from EAM on the relation between SORG and SIT (−0.21\*\*\*). This moderation is confirmed through a simple slope analysis (see, Figure 4), showing that low levels of EAM strengthen the positive relation between SORG and SIT (slope 0.408), whereas high levels of EAM make this relation become insignificant (slope −0.008).

Similarly, H2 is mostly supported: there is a positive relation between organisational complexity and technological complexity. In detail, we find that for structural complexity there is a significant positive relation between SORG and SIT (0.20\*\*\*) and similarly for dynamic complexity there is a significant positive relation between DORG and DIT (0.32\*\*\*). Furthermore, the relation between DORG and SIT is highly significant (0.27\*\*\*). Similar to our discussion of H1, we note that the relation between SORG and DIT (−0.03) does show a statistically significant total efect (0.311\*\*\*, see, Table 4).

Finally, we find clear support for H4, i.e., there is a negative relation between technological complexity and architectural outcomes. Both the relation between SIT and AO (−0.37\*\*\*) and the relation between DIT and $\mathrm { A O } \ ( - 0 . 2 3 ^ { \ast \ast \ast } )$ are statistically significant at the p < 0.01 level.

## 6. Discussion

This research makes contributions in three areas (see, Table 6): First, we provide a theoretically developed and empirically validated model of IS architecture complexity, primarily building on and extending the work of Xia and Lee (2005). Second, we contribute to the growing body of empirical research that investigates the efects of increasingly complex IS architectures. Third, our analysis reveals and details the moderating efect of EAM on the relation between organisational and technical complexity.

## 6.1. Conceptualising IS architecture complexity

A central part of the theoretical model is the conceptualisation of IS architecture complexity, comprising the diferent IS architecture complexity constructs (SORG, SIT, DORG, and DIT) as well as their interrelations (see the box labelled “IS Architecture Complexity” in Figure 2). We follow the idea of Xia and Lee (2005) to distinguish organisational from technological complexity and static from dynamic complexity, and we extend the original conceptual model in two ways. First, we change the research context from ISDP complexity to IS architecture complexity. This change of context (ISDP complexity vs IS architecture complexity) is supported by an extensive instrument development phase preceding the quantitative analysis (MacKenzie et al., 2011). Second, we extend the model of Xia and Lee (2005) by hypothesising and testing relations between the diferent IS architecture complexity constructs. This further complements the original work of Xia and Lee (2005), who find similar statistical quality criteria for the uncorrelated second-order model (i.e., SORG, SIT, DORG, and DIT are all independent constructs) and the fully correlated model (i.e., SORG, SIT, DORG, and DIT are all connected to one another; cf., Table 5 in Xia & Lee, 2005). Our model may thus be considered an extension of Xia and Lee (2005) in the sense that we do not assume that all factors are either completely correlated or completely uncorrelated. Instead, our confirmation of H1 and H2, i.e., the relation between organisational vs technological and structural vs dynamic complexity respectively, explains in more detail how diferent aspects of IS architecture complexity are related.

Table 6. Summary of key contributions.

<table><tr><td>Contribution</td><td>Implications for research</td><td>Implications for practice</td></tr><tr><td>A theoretically developed and empirically validated model of IS architecture complexity</td><td>Provide an organising framework that integrates complementary perspectives on IS architecture complexity into a single model that clarifies interrelations.</td><td>Enable practitioners to clearly describe and communicate problems and levers for solutions in the context of IS architecture complexity.</td></tr><tr><td>An empirical analysis of the effects of IS architecture complexity on architectural outcomes</td><td>Complement extant studies by detailing relations between constructs and additionally highlighting the relevance of the organisational and dynamic aspects of IS architecture complexity.</td><td>Facilitate the development of suitable complexity management approaches by estimating expected effects.</td></tr><tr><td>Clarification of the moderating effect of EAM on the relation between organisational and technological complexity</td><td>Bridge research on EAM with research on IS architecture complexity by demonstrating a highly significant moderation effect and explaining its nature.</td><td>Support and guide investment decisions for EAM efforts by detailing how EAM contributes to desired architectural outcomes.</td></tr></table>

Conceptual models, and extensions thereof, make significant contributions to both research and practice. Researchers fundamentally rely upon well-developed and tested conceptual models as organising frameworks, which provide a basis for consistently defining constructs. This allows for a meaningful comparison of the results of diferent studies and thus enables the cumulative creation of scientific knowledge (Vom Brocke et al., 2009). A robust conceptual model also provides practitioners with a suitable language to describe and communicate problems and potential solutions in the context of IS architecture complexity.

## 6.2. Efects of IS architecture complexity

Our research builds on and adds to the growing body of knowledge on the efects of IS architecture complexity. In general, the $\mathrm { R } ^ { 2 }$ value of 0.31 in our final model (see, Figure 5) resembles approximately the values that can be expected from reviewing related survey-based SEM studies. For example, Schilling et al. (2017) use a similar conceptualisation for IS architecture complexity, which in their model leads to a $\mathrm { R } ^ { 2 }$ value of 0.31 for the IS architecture outcomes construct, comprising flexibility and eficiency (Schilling et al., 2017, see Figure 2, p. 11). Likewise, Schmidt and Buxmann (2011), find that their EAM construct allows them to explain flexibility $( \mathrm { R } ^ { 2 } = 0 . 4 0 )$ and eficiency $( \mathrm { R } ^ { 2 } = 0 . 2 8 )$ . In comparison to both studies, we present a more detailed view on the predictor construct (i.e., the IS architecture complexity part of Figure 2) by detailing the relations between the SORG, DORG, SIT, and DIT constructs, and accordingly explicitly measuring the individual contributions of both SIT (−0.482\*\*\*) and DIT (−0.234\*\*\*) on architectural outcomes (see, Table 4). Furthermore, our analysis of total efects in Table 4 also allows to measure the contributions of the preceding constructs on architectural outcomes, i.e., SORG (−0.197\*\*\*), DORG (−0.211\*\*\*), and EAM (0.242\*\*\*).

In comparison with non-survey based quantitative studies on IS architecture complexity (e.g., Aleatrati Khosroshahi et al., 2016; Mocker, 2009) we ofer a more complete conceptualisation of the phenomenon. Following Xia and Lee (2005), we also consider dynamic and non-technical aspects of IS architecture complexity. For example, complementary to Aleatrati Khosroshahi et al. (2016) and Mocker (2009), who focus on the structural technological aspects (i.e., SIT in our model), we find that the other DORG, SORG, and DIT constructs also have significant efects (see, Table 4). Thus, our study contributes an extended perspective on IS architecture complexity and related efects on architectural outcomes.

In addition to this theoretical contribution, practitioners may use the estimates from the final model (see, Figure 5 and Table 4) to guide complexity management eforts in their organisation. This helps to develop suitable complexity management approaches, as it facilitates the evaluation of potential consequences of actions.

## 6.3. The moderating efect of EAM

In their Delphi study on the complexity of IS programs Piccinini et al. (2014, p. 9) conclude:

“[An] interesting overall result of our study is that a new meta-category emerged, i.e., CCD [coordination and control deficiencies], which appears with one component in the final ranking, i.e., ‘unclear or illdefined program methodology’. This means that if a sound methodology is not in place in an IS program, complexity as perceived by IS program practitioners increases”.

Similarly, early discussions in our focus groups clearly indicated that EAM, or similar coordination and control activities, need to be considered when studying IS architecture complexity, as these are expected to strongly influence the extent to which organisational complexity manifests as technological complexity. Our confirmation of H4 and the total efect of EAM on AO (0.242\*\*\*, see, Table 4) strongly afirms this expectation. Thus, our work extends previous exploratory studies, such as Piccinini et al. (2014), by clarifying the nature of the moderating efect of EAM on the relation between organisational and technological complexity (see, Figure 3 and Figure 4).

Practitioners may use this insight to justify investment decisions in EAM. At the time of the focus group workshops, all participating companies had launched significant IS architecture complexity management programmes with multi-million-dollar budgets per year. The expected and actual contribution of such programmes is, however, dificult to measure. Our research ofers a scientifically tested confirmation that there are noticeable benefits of EAM, ofering an efective way to avoid unnecessary technological complexity arising from potentially necessary organisational complexity. Furthermore, we find that the notion of necessary and unnecessary complexity is frequently misconstrued in practice. Practitioneroriented studies on organisational and technologica complexity – including the excellent work of Martin Mocker (Mocker & Boochever, 2020; Mocker & Heck, 2015; Mocker et al., 2016, 2014) – correctly argue that increases in organisational complexity tend to coincide with increases in technological complexity, so that organisations should take great care to (i) avoid unnecessary organisational complexity in general and (ii) try to reduce unnecessary technological complexity that is not corresponding to organisational complexity. Consequently, many complexity reduction initiatives initially focus on relatively simple organisational areas, since they expect these to have a very low level of “necessary organizational complexity”, thereby providing the highest potential to reduce “unnecessary technological complexity”. Our results contradict this idea: While we also confirm a clear positive relation between technological complexity and organisationa complexity, we additionally find that the expected impact of EAM to reduce technological complexity becomes higher as the organisational complexity increases. In the most extreme cases – considering only the companies that do EAM really well – we do not find any correlation between organisational complexity and IT complexity; i.e., your organisation may become very complex, but this need not manifest in IT complexity at all. Consequently, it might be beneficial to specifically focus eforts to reduce technological complexity on the most complex areas of the organisation, which may seem counterintuitive at first.

## 6.4. Generalisability, limitations, and research opportunities

Regarding generalisability, we first note that our data sample mostly covers large European companies and certain industries (e.g., insurance) are overrepresented. We believe, however, that our results will apply to most large organisations that fundamentally rely on IT systems in the execution of their core business processes, since we explicitly test the robustness of the final model via multigroup-analysis against specific methodological biases and against variations in our sample demographics (see Appendix B; Seddon & Scheepers, 2012, 2015). Furthermore, several statistical results in our model are closely in line with other studies (e.g., Aleatrati Khosroshahi et al., 2016; Mocker, 2009; Schilling et al., 2017; Schmidt & Buxmann, 2011) that investigate similar constructs (IS-related complexity) in similar populations (large organisations from common industries), thereby giving additional evidence that the observed relations in our model are likely apply to other large organisations as well (Seddon & Scheepers, 2012). In contrast, we do not expect our results to apply to small organisations (e.g., start-ups, which might not experience complexity in the same way as larger organisations with a long history) and to niche industries, which use fundamentally diferent IS (e.g., high-security military operations).

Furthermore, unforeseen technological disruptions, such as, for example, fundamentally new ways to build IS architectures in cloud environments could make our results obsolete. One promising avenue for future research therefore lies in investigations that try to evaluate the impact of disruptive technologies on IS architecture complexity and on EAM. A recent informal discussion of our survey results with several practitioners in February 2020 suggested that our findings currently still apply to their organisations. However, they are closely monitoring advances in cloud technologies, artificial intelligence, as well as new DevOps practices as potential solutions to long-standing issues with IS architecture complexity. Newer trends in EAM, such as agile EA and architectural thinking (Buckl et al., 2011; Schilling et al., 2018; Winter, 2014), also warrant further investigations.

Concerning limitations, the combination of focus group data and a quantitative survey-based PLS-SEM analysis enables us to derive interesting results; but it also limits the extent to which we can understand the observed phenomenon in more detail. We therefore point out three important limitations of this research to avoid misinterpretations.

First, the participants in our focus group discussions are rather homogenous (IT afine people from large European companies). Thus, while we took great care to allow for open discussions without pushing participants into specific directions (Freitas et al., 1998), the individual perceptions and group dynamics may lead to focal points in the survey that are not fully representative for other cultures (e.g., Asian or African corporations).

Second, one needs to consider the methodological implications of using PLS-SEM with SmartPLS when analysing complex phenomena that may fundamentally be non-linear. PLS essentially conducts a simultaneous series of linear regressions to minimise an overall errorterm in the model. While we find the paths in our model to be statistically significant, these may, in many cases, be only rough approximations of truly non-linear relations. For example, Aleatrati Khosroshahi et al. (2016) observe an exponential relation between IS architecture complexity indicators and outcome measures, based on a large dataset from a single organisation. Consequently, we conducted tests for similar exponential models in R, but did not find a statistically satisfactory relation, most likely due to our analysis being limited by a comparatively (for non-linear analyses) small data set of 249 survey responses.

Third, neither the design of our focus group workshops, nor our survey data is suitable for longitudinal or multi-level analyses. IS architecture complexity is generally assumed to be an emergent phenomenon that arises over time (Beese et al., 2015; Haki et al., 2020) and consequently many of the hypothesised positive or negative relations are expected to difer for diferent parts of an organisation and in diferent points in time. Our model does not pick up on such efects but instead averages perceptions across a large set of organisations.

Considering these limitations, another promising avenue for future research are more in-depth qualitative investigations – or quantitative studies with a lot of data – that aim to understand the nature and the precise mechanisms of the statistical relations that we observed. We argue that our analysis demonstrates that, on a high level, there is a significant benefit of more mature EAM, in particular when an organisation’s IT needs to support very complex organisational structures and processes. In reality, however, EAM and IS architecture complexity are very intricate constructs, whose mechanisms need to be understood in detail to be efectively managed in a given organisational context (Haki et al., 2020).

## Disclosure statement

No potential conflict of interest was reported by the author(s).

## ORCID

Kazem Haki http://orcid.org/0000-0002-8807-0147

## References

Aier, S., Gleichauf, B., & Winter, R. 2011. “Understanding enterprise architecture management design – An empirical analysis,” The 10th International Conference on Wirtschaftsinformatik (WI 2011), Zurich, Switzerland. Association for Information Systems.

Aier, S., & Winter, R. (2009). Virtual decoupling for It/ Business alignment – conceptual foundations, architecture design and implementation example. Business & Information Systems Engineering, 1(2), 150–163. https:// doi.org/10.1007/s12599-008-0010-7

Aiken, L. S., West, S. G., & Reno, R. R. (1991). Multiple Regression: Testing and Interpreting Interactions. Sage.

Aleatrati Khosroshahi, P., Beese, J., & Aier, S. 2016. “What drives application portfolio complexity? An empirical analysis of application portfolio cost drivers at a global automotive company,” 18th Conference on Business Informatics (CBI 2016), Paris, France. IEEE.

Alter, S. (2002). The work system method for understanding information systems and information systems research. Communications of the Association for Information Systems, 9(1), 6. https://doi.org/10.17705/1CAIS.00906

Amarilli, F., van Vliet, M., & van den Hoof, B. 2016. “Business it alignment through the lens of complexity science,” Proceedings of the 37th International Conference on Information Systems (ICIS 2016), Dublin, Ireland. Association for Information Systems.

Arteta, B. M., & Giachetti, R. E. (2004). A measure of agility as the complexity of the enterprise system. Robotics and Computer-Integrated Manufacturing, 20(6), 495–503. https://doi.org/10.1016/j.rcim.2004.05.008

Attewell, P. (1992). Technology difusion and organizational learning: The case of business computing. Organization Science, 3(1), 1–19. https://doi.org/10.1287/orsc.3.1.1

Baccarini, D. (1996). The concept of project complexity—a review. International Journal of Project Management, 14 (4), 201–204. https://doi.org/10.1016/0263-7863(95) 00093-3

Barki, H., Rivard, S., & Talbot, J. (2001). An integrative contingency model of software project risk management. Journal of Management Information Systems, 17(4), 37. https://doi.org/10.1080/07421222.2001.11045666

Beese, J., Aier, S., & Winter, R. (2015). On the role of complexity for guiding enterprise transformations. In D. Aveiro, R. Pergl, & M. Valenta (Eds.), Advances in Enterprise Engineering Ix. EEWC 2015. Lecture Notes in Business Information Processing (Vol. 211, pp. 113–127). Springer.

Beetz, R., & Kolbe, L. 2011. “Towards managing it complexity: An it governance framework to measure business-it responsibility sharing and structural it organization,” 17th Americas Conference on Information Systems (AMCIS), Detroit, USA. Association for Information Systems.

Benbya, H., & McKelvey, B. (2006). Toward a complexity theory of information systems development. Information Technology & People, 19(1), 12–34. https://doi.org/10. 1108/09593840610649952

Bernus, P., & Schmidt, G. (2006). Architectures of information systems. In P. Bernus, K. Mertins, & G. Schmidt (Eds.), Handbook on architectures of information systems (pp. 1–9). Springer Berlin Heidelberg.

Boh, W. F., & Yellin, D. (2006). “Using enterprise architecture standards in managing information technology. Journal of Management Information Systems, 23(3), 163–207. https://doi.org/10.2753/MIS0742-1222230307

Bosch-Rekveldt, M., Jongkind, Y., Mooi, H., Bakker, H., & Verbraeck, A. (2011). Grasping project complexity in large engineering projects: The toe (technical, organizational and environmental) framework. International Journal of Project Management, 29(6), 728–739. https:/ doi.org/10.1016/j.ijproman.2010.07.008

Brosius, M., Aier, S., Haki, K., & Winter, R. 2018. The Institutional Logic of Harmonization: Local Versus Global Perspectives. In Aveiro, D., Guizzardi, G., Guédria, W.(Eds.). Advances in Enterprise Engineering XII. EEWC 2018. Lecture Notes in Business Information Processing, 334, 3–17. Springer. https://doi.org/10.1007 978-3-030-06097-8\_1

Buckl, S., Matthes, F., Monahov, I., Roth, S., Schulz, C., & Schweda, C. M. 2011. “Towards an agile design of the enterprise architecture management function,” 2011 IEEE 15th International Enterprise Distributed Object Computing Conference Workshops, pp. 322–329.

Colfer, L. J., & Baldwin, C. Y. (2016). The mirroring hypothesis: Theory, evidence, and exceptions. Industrial and Corporate Change, 25(5), 709–738. https://doi.org/10.1093/icc/dtw027

Cong, Y., & Romero, J. (2013). On Information Systems Complexity and Vulnerability. Journal of Information Systems, 27(2), 51–64. https://doi.org/10.2308/isys-50562

Constantinides, P., Henfridsson, O., & Parker, G. G. (2018). Platforms and Infrastructures in the digital age. Information Systems Research, 29(2), 381–400. https:/ doi.org/10.1287/isre.2018.0794

Conway, M. E. (1968). How Do Committees Invent? Datamation, 14(4), 28–31.

Cram, W. A., Brohman, M. K., & Gallupe, R. B. (2016). Information systems control: A review and framework for emerging information systems processes. Journal of the Association for Information Systems, 17(4), 216–266. https://doi.org/10.17705/1jais.00427

Cycyota, C. S., & Harrison, D. A. (2002). Enhancing survey response rates at the executive level: Are employee-or consumer-level techniques efective? Journal of Management, 28(2), 151–176. https://doi.org/10.1177/ 014920630202800202

Dwivedi, Y. K., Wastell, D., Laumer, S., Henriksen, H. Z., Myers, M. D., Bunker, D., Elbanna, A., Ravishankar, M. N., & Srivastava, S. C. (2014). Research on information systems failures and successes: Status update and future directions. Information Systems Frontiers, 17(1), 143–157. https://doi.org/10.1007/s10796-014-9500-y

Faul, F., Erdfelder, E., Buchner, A., & Lang, A.-G. (2009). Statistical power analyses using G\*power 3.1: Tests for correlation and regression analyses. Behavior Research Methods, 41(4), 1149–1160. https://doi.org/10.3758/BRM.41.4.1149

Foorthuis, R. M. (2012). Project compliance with enterprise architecture. Universiteit Utrecht.

France, R., & Rumpe, B. (2007). Model-driven development of complex software: A research roadmap Briand, L., Wolf, A. In Future of Software Engineering (pp. 37–54). IEEE Computer Society.https://doi.org/10.1109/FOSE.2007.14

Freitas, H., Oliveira, M., Jenkins, M., & Popjoy, O. (1998). The focus group, a qualitative research method. Journal of Education, 1(1), 1–22.

Gefen, D., Rigdon, E. E., & Straub, D. (2011). An update and extension to SEM guidelines for administrative and social science research. MIS Quarterly, 35(2), 3–14. https://doi. org/10.2307/23044042

Gefen, D., & Straub, D. (2005). A practical guide to factorial validity using PLS-Graph: Tutorial and annotated example. Communications of the AIS, 16(5), 91–109. https://doi.org/10.17705/1CAIS.01605

Geraldi, J. (2009). What complexity assessments can tell us about projects: Dialogue between conception and perception. Technology Analysis & Strategic Management, 21(5), 665–678. https://doi.org/10.1080/ 09537320902969208

Gerbing, D. W., & Anderson, J. C. (1988). An updated paradigm for scale development incorporating unidimensionality and its assessment. Journal of Marketing Research, 25(2), 186–192. https://doi.org/10.1177/002224378802500207

Gerow, J. E., Grover, V., Thatcher, J. B., & Roth, P. L. (2014). Looking toward the future of IT-business strategic alignment through the past: A meta-analysis. Mis Quarterly, 38(4), 1059–1085. https://doi.org/10.25300/ MISQ/2014/38.4.10

Gomber, P., Kaufman, R. J., Parker, C., & Weber, B. W. (2018). “On the fintech revolution: interpreting the forces of innovation, disruption, and transformation in financial services”. Journal of Management Information Systems, 35(1), 220–265. https://doi.org/10.1080/07421222.2018.1440766 .

Götz, O., Liehr-Gobbers, K., & Kraft, M. (2010). Evaluation of structural equation models using the partial least squares (PLS) approach. In V. E. Vinzi, W. W. Chin, J. Henseler, & H. Wang (Eds.), Handbook of partial least squares: Concepts, methods and applications (pp. 691–711). Springer.

Greefhorst, D., & Proper, H. A. (2011). Architecture principles – The cornerstones of enterprise architecture. Springer.

Hair, J J, Hult, F., Ringle, C. M, G. T. M., & Sarstedt, M. (2014). A primer on partial least squares structural equation modeling (PLS-SEM). Sage.

Hair, J. F.,sJr., Ringle, C. M., & Sarstedt, M. (2013). Partia least squares structural equation modeling: rigorous applications, better results and higher acceptance. Long Range Planning: International Journal of Strategic Management, 46(1–2), 1–12. https://doi.org/10.1016/j. lrp.2013.01.001

Haki, K., Beese, J., Aier, S., & Winter, R. (2020). The evolution of information systems architecture: An agent-based simulation model. MIS Quarterly, 44(1), 155–184. https:// doi.org/10.25300/MISQ/2020/14494

Haki, M. K., & Legner, ca. 2013. “Enterprise architecture principles in research and practice: Insights from an exploratory analysis,” European Conference on Information Systems (ECIS), Utrecht, The Netherlands, p. 204.

Hansen, S., & Baroody, A. J. (2019). “Electronic health records and the logics of care: Complementarity and conflict in the U.S. healthcare system. Information Systems Research, 31(1), 57–75. https://doi.org/10.1287/ isre.2019.0875

Hansen, R., & Kien, S. S. (2015). Hummel’s digital transformation toward omnichannel retailing: key lessons learned. MIS Quarterly Executive, 14(2), 51–66. https:// aisel.aisnet.org/misqe/vol14/iss2/3

Hanseth, O., & Bygstad, B. 2012. “ICT architecture and project risk in inter-organizational settings”, 20th European conference on information systems (ECIS), Barcelona, Spain. Association for Information Systems.

Hanseth, O., & Ciborra, C. (2007). Risk, complexity and ICT. Edward Elgar Publishing.

Hanseth, O., & Lyytinen, K. (2010). Design theory for dynamic complexity in information infrastructures: The case of building internet. Journal of Information Technology, 25(1), 1–19. https://doi.org/10.1057/jit.2009.19

Henfridsson, O., & Bygstad, B. (2013). The generative mechanisms of digital infrastructure evolution. MIS Quarterly, 37(3), 907–931. https://doi.org/10.25300 MISQ/2013/37.3.11

Henseler, J., & Fassott, G. (2010). Testing moderating efects in pls path models: An illustration of available procedures. In V. Esposito Vinzi, W. W. Chin, J. Henseler, & H. Wang (Eds.), Handbook of partial least squares: Concepts, methods and applications (pp. 713–735). Springer.

Henseler, J., Ringle, C. M., & Sarstedt, M. (2015). A new criterion for assessing discriminant validity in variance-based structural equation modeling. Journal of the Academy of Marketing Science, 43(1), 115–135. https://doi.org/10.1007/s11747-014-0403-8

Kroenke, B., Mayer, J. H., Reinecke, A., Feistenauer, H., & Hauke, J. (2013). Self-service management support system – There is an app for that. In vom Brocke, J., Hekkala, R., Ram, S., Rossi, M.(Eds.) DESRIST 2013 (pp. 420–424). Springer.

Kutner, M., Nachtsheim, C., Neter, J., & Li, W. (2005). Applied linear statistical models (5th ed.). McGraw-Hill Irwin.

Lakhrouit, J., & Baïna, K. (2016). Enterprise architecture complexity component based on Archimate language. In Advances in ubiquitous networking. Springer. (pp. 535–546).

Lange, M., Mendling, J., & Recker, J. (2016). An empirical analysis of the factors and measures of enterprise architecture management success. European Journal of Information Systems, 25(5), 411–431. https://doi.org/10.1057/ejis.2014.39

Legner, C., Eymann, T., Hess, T., Matt, C., Boehmann, T., Drews, P., Maedche, A., Urbach, N., & Ahlemann, F. (2017). Digitalization: Opportunity and challenge for the business and information systems engineering community. Business & Information Systems Engineering, 59(4), 301–308. https://doi.org/10.1007/s12599-017-0484-2

Li, X., & Madnick, S. E. (2015). Understanding the dynamics of service-oriented architecture implementation. Journal of Management Information Systems, 32(2), 104–133. https://doi.org/10.1080 07421222.2015.1063284

Lohmöller, J.-B. (1989). Latent variable path modeling with partial least squares. Physica.

Lyytinen, K., & Newman, M. (2008). Explaining information systems change: A punctuated socio-technical change model. European Journal of Information Systems, 17(6), 589–613. https://doi.org/10.1057/ejis.2008.50

MacKenzie, S. B., Podsakof, P. M., & Podsakof, N. P. (2011). Construct measurement and validation procedures in mis and behavioral research: Integrating new and existing techniques. MIS Quarterly, 35(2), 293–334. https://doi.org/10.2307/23044045

Mata, F. J., Fuerst, W. L., & Barney, J. B. (1995). Information technology and sustained competitive advantage: A resource-based analysis. MIS Quarterly, 19(4), 487–505. https://doi.org/10.2307/249630

McKeen, J. D., Guimaraes, T., & Wetherbe, J. C. (1994). The Relationship between User Participation and User Satisfaction: An Investigation of Four Contingency Factors. MIS Quarterly, 18(4), 427–451. https://doi.org/10. 2307/249523

McKelvey, B., Tanriverdi, H., & Yoo, Y. 2016. “Complexity and information systems research in the emerging digital world,” MIS Quarterly, 39(4), 995–996.

Melville, N., Kraemer, K., & Gurbaxani, V. (2004). Review: Information technology and organizational performance: An integrative model of it business value. MIS Quarterly, 28(2), 283–322. https://doi.org/10.2307/25148636

Merali, Y. (2006). Complexity and information systems: The emergent domain. Journal of Information Technology, 21 (4), 216–228. https://doi.org/10.1057/palgrave.jit.2000081

Meyer, M. H., & Curley, K. F. (1991). An applied framework for classifying the complexity of knowledge-based systems. MIS Quarterly, 15(4), 455–472. https://doi.org/ 10.2307/249450

Mocker, M. 2009. “What is complex about 273 applications? Untangling application architecture complexity in a case of European investment banking,” 42nd Hawaii international conference on system sciences (HICSS 2009), Big Island, USA. IEEE Computer Society Press.

Mocker, M., & Boochever, J. O. (2020). How to avoid enterprise systems landscape complexity. MIS Quarterly Executive, 19 (1), 57–68. https://doi.org/10.17705/2msqe.00025

Mocker, M., & Heck, E. 2015. Business-driven IT transformation at Royal Philips: Shedding light on (Un)rewarded complexity, Thirty Sixth International Conference on Information Systems (ICIS 2015). Association for Information Systems.

Mocker, M., Ross, J., & Kosgi, K. 2016. MIT CISR Working papers (405). MIT Center for Information Systems Research, pp. 11-15.

Mocker, M., Weill, P., & Woerner, S. L. (2014). “Revisiting Complexity in the digital age. MIT Sloan Management Review, 55(4), 73–81. https://sloanreview.mit.edu/article/ revisiting-complexity-in-the-digital-age/

Niemann, K. D. (2006). From enterprise architecture to it governance. elements of efective it management. Vieweg.

Niemi, E., & Pekkola, S. (2017). Using enterprise architecture artefacts in an organisation. Enterprise Information Systems, 11(3), 313–338. https://doi.org/10.1080/ 17517575.2015.1048831

Petter, S., DeLone, W. H., & McLean, E. R. (2008). Measuring information systems success: Models, dimensions, measures, and interrelationships. European Journa of Information Systems, 17(17), 236–263. https://doi.org/ 10.1057/ejis.2008.15

Piccinini, E., Gregory, R., & Muntermann, J. 2014. “Complexity in is programs: A delphi study”, 22nd European conference on information systems (ECIS 2014), Israel, 1–13. Association for Information Systems.

Podsakof, P. M., MacKenzie, S. B., Lee, J.-Y., & Podsakof, N. P. (2003). Common method biases in behavioral research - a critical review of the literature and recommended remedies. Journal of Applied Psychology, 88(5), 879–903. https://doi.org/10.1037/0021-9010.88.5.879

Ramasubbu, N., Woodard, C. J., & Mithas, S. 2014. “Orchestrating service innovation using design moves: the dynamics of fit between service and enterprise it architectures,” in: 35th international conference on information systems (ICIS 2014). Auckland, New Zealand: Association for Information Systems, pp. 1–17.

Renn, O., Klinke, A., & Asselt, M. (2011). “Coping with complexity, uncertainty and ambiguity in risk governance: A synthesis. AMBIO, 40(2), 231–246. https://doi. org/10.1007/s13280-010-0134-0

Ribbers, P. M. A., & Schoo, K.-C. (2002). Program management and complexity of ERP implementations. Engineering Management Journal, 14(2), 45. https://doi. org/10.1080/10429247.2002.11415162

Rigdon, E. E., Ringle, C. M., & Sarstedt, M. (2010). Structural modeling of heterogeneous data with partial least squares. Review of Marketing Research 7, 255–296. https://doi.org/10.1108/S1548-6435(2010)0000007011

Ringle, C. M., Sarstedt, M., & Straub, D. W. (2012). A critical look at the use of pls-sem in mis quarterly. MIS Quarterly, 36(1), 3–14. https://doi.org/10.2307/41410402

Ringle, C. M., Wende, S., & Becker, J.-M. 2015. “Smartpls 3.2.6”. Retrieved 13 November 2016. http://www. smartpls.com

Ross, J. W. (2003). Creating a strategic it architecture competency: Learning in stages. MIS Quarterly Executive, 2 (1), 31–43. http://dx.doi.org/10.2139/ssrn.416180

Ross, J. W., & Quaadgras, A. (2012).CISR Research Briefings XVII-9.

Ross, J. W., Weill, P., & Robertson, D. C. (2006). Enterprise architecture as strategy. creating a foundation for business execution. Harvard Business School Press.

Schilling, R. D., Beese, J., Haki, M. K., Aier, S., & Winter, R. 2017. “Revisiting the impact of information systems architecture complexity: A complex adaptive systems perspective,” 38th International Conference on Information Systems (ICIS 2017), Seoul, South Korea.

Schilling, R. D., Haki, K., & Aier, S. 2018. “Dynamics of control mechanisms in enterprise architecture management: a sensemaking perspective,” 39th international conference on information systems (ICIS 2018), San Francisco, USA. Association for Information Systems.

Schmidt, C., & Buxmann, P. (2011). Outcomes and success factors of enterprise it architecture management: Empirical insight from the international financial services industry. European Journal of Information Systems, 20(2), 168–185. https://doi.org/10.1057/ejis.2010.68

Schneider, A. W., Marin, Z., & Matthes, F. 2014. “Adopting notions of complexity for enterprise architecture management,” in: 20th Americas conference on information systems. Savannah.

Schütz, A., Widjaja, T., & Kaiser, J. 2013. “Complexity in enterprise architectures - conceptualization and introduction of a measure from a system theoretic perspective,” 21st European conference on information systems (ECIS), Utrecht, Netherlands: Association for Information Systems.

Scott, J. E., & Vessey, I. (2002). Managing risks in enterprise systems implementations. Communications of the ACM, 45(4), 74. https://doi. org/10.1145/505248.505249

Seddon, P. B., & Scheepers, R. (2012). Towards the improved treatment of generalization of knowledge claims in is research: drawing general conclusions from samples. European Journal of Information Systems, 21(1), 6–21. https://doi.org/10.1057/ejis.2011.9

Seddon, P. B., & Scheepers, R. (2015). Generalization in is research: A critique of the conflicting positions of Lee & Baskerville and Tsang & Williams. Journal Of Information Technology, 30(30), 30–43. https://doi.org 10.1057/jit.2014.33

Sharma, R., & Yetton, P. (2007). The contingent efects of training, technical complexity and task interdependence on successful information systems implementation. MIS Quarterly, 31(2), 219–238. https://doi.org/10.2307 25148789

Sidorova, A., & Kappelman, L. A. (2011). Better business-it alignment through enterprise architecture: An actor-network theory perspective. Journal of Enterprise Architecture, 7(1), 39–47.

Simon, D., Fischbach, K., & Schoder, D. (2014). Enterprise architecture management and its role in corporate strategic management. Information Systems and E-Business Management, 12(1), 5–42. https://doi.org/10.1007/ s10257-013-0213-4

Simonsson, M., Johnson, P., & Ekstedt, M. (2010). The efect of it governance maturity on it governance performance. Information Systems Management, 27(1), 10–24. https:// doi.org/10.1080/10580530903455106

Simonsson, M., Lagerström, R., & Johnson, P. 2008. “A bayesian network for it governance performance prediction,” International Conference on Electronic Commerce (ICEC 2008), Innsbruck, Austria. Association for Computing Machinery.

Sivo, S. A., Saunders, C., Chang, Q., & Jiang, J. J. (2006). “How low should you go? low response rates and the validity of inference in is questionnaire research. Journal of the Association for Information Systems, 7(1), 17.

Stewart, D. W., Shamdasani, P. N., & Rook, D. W. (2007). Focus groups: Theory and practice (2 ed.). Sage Publications.

Tait, P., & Vessey, I. (1988). The efect of user involvement on system success: A contingency approach. MIS Quarterly, 12(1), 91–108. https://doi.org/10.2307/248809

Tiwana, A., & Konsynski, B. (2010). Complementarities between organizational it architecture and governance structure. Information Systems Research, 21(2), 288–304. https://doi.org/10.1287/isre.1080.0206

Vom Brocke, J., Simons, A., Niehaves, B., Riemer, K., Plattfaut, R., & Cleven, A. 2009. “Reconstructing the giant: On the importance of rigour in documenting the literature search process”, 17th European Conference on Information Systems, In S. Newell, E. Whitley, N. Pouloudi, J. Wareham, & L. Mathiassen (Eds.), Verona, pp. 2206–2217.Association for Information Systems.

Widjaja, T., Kaiser, J., Tepel, D., & Buxmann, P. 2012. “Heterogeneity in it landscapes and monopoly power of firms: A model to quantify heterogeneity,” 33rd International Conference on Information Systems (ICIS), Orlando, USA. Association for Information Systems.

Wiener, M., Mähring, M., Remus, U., & Saunders, C. (2016). Control configuration and control enactment in information systems projects - review and expanded theoretical framework. MIS Quarterly, 40(3), 741–774. https://doi. org/10.25300/MISQ/2016/40.3.11

Winter, R. (2014). Architectural Thinking. Business & Information Systems Engineering, 6(6), 361–364. https:// doi.org/10.1007/s12599-014-0352-2

Winter, R., & Fischer, R. (2007). Essential layers, artifacts, and dependencies of enterprise architecture. Journal of Enterprise Architecture, 3(2), 7–18.

Winter, R., & Schelp, J. 2008. “Enterprise architecture governance: The need for a business-to-it approach,” The 23rd annual ACM symposium on applied computing (SAC2008), Mar 16- 20, 2008, Fortaleza, Ceará, Brazil, L. M. Liebrock (ed.), Fortaleza, Ceará, Brazil: ACM Press, pp. 548–552.

Wood, R. E. (1986). Task complexity: Definition of the construct. Organizational Behavior and Human Decision Processes, 37(1), 60–82. https://doi.org/10.1016/0749- 5978(86)90044-0

Xia, W., & Lee, G. (2005). Complexity of information systems development projects: Conceptualization and measurement development. Journal of Management Information Systems, 22(1), 45–83. https://doi.org/10. 1080/07421222.2003.11045831

Xue, L., Ray, G., & Gu, B. (2011). Environmental uncertainty and it infrastructure governance: A cur-vilinear relationship. Information Systems Research, 22(2), 389–399. https://doi.org/10.1287/isre.1090.0269

Zachman, J. A. (1987). A Framework for Information Systems Architecture. IBM Systems Journal, 26(3), 276–292. https://doi.org/10.1147/sj.263.0276

Table 7. List of survey items with loadings (Ld.) and t-values. Items marked with (\*) are reverse-coded.

<table><tr><td>Item-ID</td><td></td><td>Item</td><td>Ld.</td><td>t-values</td></tr><tr><td rowspan="7">Structural Organisational Complexity</td><td>SORG1</td><td>The IT systems support many different functionalities.</td><td>.654</td><td>12.94</td></tr><tr><td>SORG2</td><td>Most IT supported tasks are rather extensive and complex.</td><td>.745</td><td>19.17</td></tr><tr><td>SORG3</td><td>The expertise and requirements of system users vary considerably.</td><td>.518</td><td>7.33</td></tr><tr><td>SORG4</td><td>Diverse IT systems are involved in managing and controlling workflows.</td><td>.664</td><td>10.29</td></tr><tr><td>SORG5</td><td>The successful completion of a task is often interdependent with other tasks and processes.</td><td>.498</td><td>6.15</td></tr><tr><td>SORG6</td><td>In your organisation, many interdependencies between organisational units and many cross-departmental tasks and projects exist.</td><td>.586</td><td>9.63</td></tr><tr><td>SORG7</td><td>IT-supported workflows are highly integrated. The successful completion of a work process often depends on processes in other systems.</td><td>.629</td><td>11.16</td></tr><tr><td rowspan="5">Dynamic Organisational Complexity</td><td>DORG1</td><td>System requirements often are short-lived and change rapidly.</td><td>.709</td><td>16.39</td></tr><tr><td>DORG2</td><td>The number of different tasks that need to be addressed by the IT rises quickly.</td><td>.746</td><td>21.23</td></tr><tr><td>DORG3</td><td>Employees frequently change their roles and positions, and thus also their area of responsibility.</td><td>.681</td><td>13.35</td></tr><tr><td>DORG4</td><td>The employed technologies often still receive functional updates, which frequently lead to large system updates.</td><td>.682</td><td>14.60</td></tr><tr><td>DORG5*</td><td>Most workflows and processes remain stable throughout longer time periods.</td><td>.460</td><td>5.86</td></tr><tr><td rowspan="5">Structural IT Complexity</td><td>SIT1</td><td>The IT systems support a large number of users.</td><td>.572</td><td>8.80</td></tr><tr><td>SIT2</td><td>Coordination and integration of the different systems is a difficult and not yet adequately solved task.</td><td>.820</td><td>30.74</td></tr><tr><td>SIT3</td><td>Coordination between human users, software and hardware is difficult and often leads to problems.</td><td>.795</td><td>30.77</td></tr><tr><td>SIT4</td><td>Interactions and dependencies between individual system components lead to a complex system landscape and are often the cause of problems.</td><td>.723</td><td>18.99</td></tr><tr><td>SIT5</td><td>The number and variety of systems leads to a complex and hard to comprehend information system landscape.</td><td>.731</td><td>22.87</td></tr><tr><td rowspan="4">Dynamic IT Complexity</td><td>DIT1</td><td>The development of the IT landscape is characterised by uncertainties, making the impact of individual changes difficult to evaluate.</td><td>.796</td><td>29.98</td></tr><tr><td>DIT2</td><td>The relationships between individual components are unclear, leading to ambiguous results, which are difficult to understand without additional information.</td><td>.811</td><td>39.75</td></tr><tr><td>DIT3</td><td>In the organisation, there exists a large and rapidly changing range of different systems, technologies and requirements.</td><td>.720</td><td>16.89</td></tr><tr><td>DIT4</td><td>The development of the IT landscape is very dynamic, requiring frequent and often difficult to understand adjustments.</td><td>.788</td><td>25.25</td></tr><tr><td rowspan="5">Enterprise Architecture Management</td><td>EAM1</td><td>Roles and responsibilities are assigned through well-defined processes, which include relevant stakeholders from business and IT.</td><td>.743</td><td>14.26</td></tr><tr><td>EAM2</td><td>The development of the system landscape follows well-defined and established principles.</td><td>.806</td><td>21.07</td></tr><tr><td>EAM3</td><td>IT system requirements are developed through well-defined processes, which include relevant stakeholders from business and IT.</td><td>.612</td><td>7.87</td></tr><tr><td>EAM4</td><td>There are established guidelines on what types of tools and technologies are included in the portfolio of the organisation.</td><td>.757</td><td>17.86</td></tr><tr><td>EAM5*</td><td>Decisions about the use of technologies are made opportunity-driven by individual departments and projects.</td><td>.720</td><td>16.96</td></tr><tr><td rowspan="3">Efficiency</td><td>EFF1</td><td>The operating and development costs of the IT landscape are low compared to the scope of performance.</td><td>.748</td><td>15.82</td></tr><tr><td>EFF2</td><td>The time and costs required to use, operate and develop the system landscape are comparatively low.</td><td>.812</td><td>30.40</td></tr><tr><td>EFF3</td><td>Redundancies are avoided. There is little overlap between different applications and functional capabilities.</td><td>.742</td><td>18.73</td></tr><tr><td rowspan="4">Flexibility</td><td>FLEX1</td><td>The IT department is able to react with speed and dexterity. Even larger adjustments are implemented in time and quality.</td><td>.853</td><td>47.98</td></tr><tr><td>FLEX2</td><td>Foreseeable adjustments are well anticipated and can be implemented without much difficulty.</td><td>.847</td><td>41.00</td></tr><tr><td>FLEX3</td><td>The IT department can implement critical updates and bug fixes quickly. There is little time between the decision to change something and the implementation of the change.</td><td>.819</td><td>35.67</td></tr><tr><td>FLEX4</td><td>The company is innovative and technologically advanced. New ideas and technologies are quickly adopted and used in production.</td><td>.615</td><td>13.42</td></tr><tr><td rowspan="4">Transparency</td><td>TRSP1</td><td>The system landscape is transparent. Processes and results are understandable for the end-users.</td><td>.770</td><td>23.78</td></tr><tr><td>TRSP2</td><td>The development and behaviour of the IT landscape can be explained and communicated easily.</td><td>.861</td><td>61.80</td></tr><tr><td>TRSP3</td><td>Use and operation of the system landscape is easy to learn. New employees become acquainted with the systems quickly and without major problems.</td><td>.719</td><td>19.51</td></tr><tr><td>TRSP4</td><td>The behaviour of the system landscape is comprehensible. The causes of exceptions and errors can be quickly traced.</td><td>.803</td><td>35.64</td></tr><tr><td rowspan="3">Predictability</td><td>PRED1</td><td>The effects of adjustments and changes are predictable. Costs and expenses for developments can be estimated reliably.</td><td>.818</td><td>41.29</td></tr><tr><td>PRED2</td><td>The IT systems operate reliably. Failures and critical errors occur rarely or not at all.</td><td>.836</td><td>31.21</td></tr><tr><td>PRED3</td><td>The IT system landscape is relatively stable. Major changes occur infrequently and affect only few components.</td><td>.745</td><td>18.69</td></tr></table>

## Appendix B: Analysis of discriminant validity and predictive validity

Discriminant validity was tested using Heterotrait-Monotrait (HTMT) analysis (see Table 8) and the results are within the recommended thresholds (< 0.9) of Henseler et al. (2015). One notable exception is the second order AO construct (bold in Table 8), since it shares the same indicators with the underlying lower order constructs (Jr., J. Hair et al., 2014).

However, a detailed cross loadings analysis shows that each indicator has a stronger correlation with the assigned latent variable than with any other latent variable (see, Table 9), indicating that the model has good discriminant validity. Furthermore, we tested the predictive relevance of the model with the non-parametric Stone-Geisser test by applying a blindfolding procedure with an omission distance of 7 in SmartPLS (Jr., J. Hair et al., 2014). All Q<sup>2</sup> values (DORG: 0.110, SIT: 0.176, DIT: 0.334, AO: 0.119) are larger than zero, indicating that the model has predictive validity (Götz et al., 2010).

Table 8. Heterotrait-monotrait (HTMT) analysis of discriminant validity.

<table><tr><td></td><td>SORG</td><td>DORG</td><td>SIT</td><td>DIT</td><td>EAM</td><td>AO</td><td>EFF</td><td>FLEX</td><td>TRSP</td></tr><tr><td>DORG</td><td>0.673</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>SIT</td><td>0.454</td><td>0.536</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>DIT</td><td>0.382</td><td>0.707</td><td>0.872</td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>EAM</td><td>0.229</td><td>0.229</td><td>0.456</td><td>0.471</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>AO</td><td>0.290</td><td>0.370</td><td>0.627</td><td>0.576</td><td>0.406</td><td></td><td></td><td></td><td></td></tr><tr><td>EFF</td><td>0.384</td><td>0.322</td><td>0.509</td><td>0.490</td><td>0.269</td><td>0.988</td><td></td><td></td><td></td></tr><tr><td>FLEX</td><td>0.143</td><td>0.230</td><td>0.493</td><td>0.417</td><td>0.423</td><td>1.004</td><td>0.770</td><td></td><td></td></tr><tr><td>TRSP</td><td>0.267</td><td>0.350</td><td>0.651</td><td>0.564</td><td>0.542</td><td>1.026</td><td>0.740</td><td>0.766</td><td></td></tr><tr><td>PRED</td><td>0.284</td><td>0.436</td><td>0.552</td><td>0.655</td><td>0.449</td><td>0.950</td><td>0.608</td><td>0.663</td><td>0.781</td></tr></table>

Table 9. Cross loading analysis.

<table><tr><td>Item-ID</td><td>SORG</td><td>DORG</td><td>SIT</td><td>DIT</td><td>EAM</td><td>EFF</td><td>FLEX</td><td>TRSP</td><td>PRED</td></tr><tr><td>SORG1</td><td>0.654</td><td>0.352</td><td>0.189</td><td>0.217</td><td>-0.047</td><td>-0.190</td><td>-0.054</td><td>-0.156</td><td>-0.145</td></tr><tr><td>SORG2</td><td>0.745</td><td>0.482</td><td>0.291</td><td>0.241</td><td>0.045</td><td>-0.239</td><td>0.008</td><td>-0.165</td><td>-0.175</td></tr><tr><td>SORG3</td><td>0.518</td><td>0.216</td><td>0.174</td><td>0.093</td><td>-0.087</td><td>-0.165</td><td>-0.087</td><td>-0.130</td><td>-0.097</td></tr><tr><td>SORG4</td><td>0.664</td><td>0.357</td><td>0.192</td><td>0.185</td><td>0.009</td><td>-0.194</td><td>0.011</td><td>-0.104</td><td>-0.083</td></tr><tr><td>SORG5</td><td>0.498</td><td>0.136</td><td>0.177</td><td>0.126</td><td>0.078</td><td>-0.097</td><td>-0.081</td><td>-0.122</td><td>-0.161</td></tr><tr><td>SORG6</td><td>0.586</td><td>0.302</td><td>0.197</td><td>0.202</td><td>0.136</td><td>-0.150</td><td>0.061</td><td>-0.063</td><td>-0.074</td></tr><tr><td>SORG7</td><td>0.629</td><td>0.247</td><td>0.122</td><td>0.118</td><td>0.118</td><td>-0.138</td><td>0.051</td><td>-0.062</td><td>-0.107</td></tr><tr><td>DORG1</td><td>0.375</td><td>0.709</td><td>0.192</td><td>0.329</td><td>0.003</td><td>-0.066</td><td>0.020</td><td>-0.108</td><td>-0.130</td></tr><tr><td>DORG2</td><td>0.447</td><td>0.746</td><td>0.296</td><td>0.397</td><td>0.049</td><td>-0.262</td><td>-0.145</td><td>-0.207</td><td>-0.246</td></tr><tr><td>DORG3</td><td>0.308</td><td>0.681</td><td>0.323</td><td>0.386</td><td>-0.070</td><td>-0.181</td><td>-0.080</td><td>-0.109</td><td>-0.147</td></tr><tr><td>DORG4</td><td>0.396</td><td>0.682</td><td>0.211</td><td>0.312</td><td>-0.003</td><td>-0.077</td><td>0.045</td><td>-0.098</td><td>-0.157</td></tr><tr><td>DORG5</td><td>0.125</td><td>0.460</td><td>0.226</td><td>0.261</td><td>-0.048</td><td>-0.124</td><td>-0.162</td><td>-0.322</td><td>-0.297</td></tr><tr><td>SIT1</td><td>0.483</td><td>0.392</td><td>0.572</td><td>0.353</td><td>-0.153</td><td>-0.280</td><td>-0.184</td><td>-0.288</td><td>-0.248</td></tr><tr><td>SIT2</td><td>0.076</td><td>0.228</td><td>0.820</td><td>0.584</td><td>-0.421</td><td>-0.278</td><td>-0.347</td><td>-0.433</td><td>-0.362</td></tr><tr><td>SIT3</td><td>0.189</td><td>0.210</td><td>0.795</td><td>0.559</td><td>-0.379</td><td>-0.287</td><td>-0.306</td><td>-0.401</td><td>-0.301</td></tr><tr><td>SIT4</td><td>0.330</td><td>0.281</td><td>0.723</td><td>0.450</td><td>-0.181</td><td>-0.257</td><td>-0.294</td><td>-0.299</td><td>-0.301</td></tr><tr><td>SIT5</td><td>0.174</td><td>0.307</td><td>0.731</td><td>0.560</td><td>-0.259</td><td>-0.251</td><td>-0.309</td><td>-0.455</td><td>-0.356</td></tr><tr><td>DIT1</td><td>0.205</td><td>0.389</td><td>0.638</td><td>0.796</td><td>-0.393</td><td>-0.144</td><td>-0.256</td><td>-0.423</td><td>-0.387</td></tr><tr><td>DIT2</td><td>0.083</td><td>0.332</td><td>0.537</td><td>0.811</td><td>-0.415</td><td>-0.285</td><td>-0.371</td><td>-0.411</td><td>-0.470</td></tr><tr><td>DIT3</td><td>0.407</td><td>0.458</td><td>0.435</td><td>0.720</td><td>-0.177</td><td>-0.314</td><td>-0.241</td><td>-0.293</td><td>-0.359</td></tr><tr><td>DIT4</td><td>0.240</td><td>0.440</td><td>0.535</td><td>0.788</td><td>-0.269</td><td>-0.180</td><td>-0.193</td><td>-0.274</td><td>-0.354</td></tr><tr><td>EAM1</td><td>0.118</td><td>0.059</td><td>-0.210</td><td>-0.238</td><td>0.743</td><td>0.122</td><td>0.207</td><td>0.270</td><td>0.200</td></tr><tr><td>EAM2</td><td>0.123</td><td>0.105</td><td>-0.285</td><td>-0.263</td><td>0.806</td><td>0.180</td><td>0.316</td><td>0.351</td><td>0.301</td></tr><tr><td>EAM3</td><td>0.097</td><td>0.028</td><td>-0.236</td><td>-0.181</td><td>0.612</td><td>0.203</td><td>0.295</td><td>0.317</td><td>0.255</td></tr><tr><td>EAM4</td><td>0.104</td><td>0.096</td><td>-0.234</td><td>-0.289</td><td>0.757</td><td>0.105</td><td>0.255</td><td>0.386</td><td>0.267</td></tr><tr><td>EAM5</td><td>-0.128</td><td>-0.212</td><td>-0.391</td><td>-0.430</td><td>0.720</td><td>0.102</td><td>0.161</td><td>0.255</td><td>0.272</td></tr><tr><td>EFF1</td><td>-0.167</td><td>-0.120</td><td>-0.205</td><td>-0.175</td><td>0.136</td><td>0.748</td><td>0.365</td><td>0.329</td><td>0.194</td></tr><tr><td>EFF2</td><td>-0.198</td><td>-0.209</td><td>-0.342</td><td>-0.259</td><td>0.140</td><td>0.812</td><td>0.480</td><td>0.467</td><td>0.381</td></tr><tr><td>EFF3</td><td>-0.276</td><td>-0.172</td><td>-0.283</td><td>-0.226</td><td>0.152</td><td>0.742</td><td>0.446</td><td>0.431</td><td>0.424</td></tr><tr><td>FLEX1</td><td>-0.044</td><td>-0.091</td><td>-0.363</td><td>-0.283</td><td>0.236</td><td>0.540</td><td>0.853</td><td>0.553</td><td>0.458</td></tr><tr><td>FLEX2</td><td>-0.032</td><td>-0.148</td><td>-0.377</td><td>-0.365</td><td>0.315</td><td>0.476</td><td>0.847</td><td>0.572</td><td>0.503</td></tr><tr><td>FLEX3</td><td>-0.015</td><td>-0.065</td><td>-0.281</td><td>-0.294</td><td>0.262</td><td>0.418</td><td>0.819</td><td>0.461</td><td>0.484</td></tr><tr><td>FLEX4</td><td>0.092</td><td>0.062</td><td>-0.210</td><td>-0.094</td><td>0.205</td><td>0.332</td><td>0.615</td><td>0.343</td><td>0.230</td></tr><tr><td>TRSP1</td><td>-0.115</td><td>-0.090</td><td>-0.442</td><td>-0.376</td><td>0.479</td><td>0.431</td><td>0.460</td><td>0.770</td><td>0.439</td></tr><tr><td>TRSP2</td><td>-0.080</td><td>-0.188</td><td>-0.418</td><td>-0.387</td><td>0.386</td><td>0.446</td><td>0.501</td><td>0.861</td><td>0.563</td></tr><tr><td>TRSP3</td><td>-0.298</td><td>-0.262</td><td>-0.335</td><td>-0.265</td><td>0.224</td><td>0.438</td><td>0.400</td><td>0.719</td><td>0.401</td></tr><tr><td>TRSP4</td><td>-0.127</td><td>-0.208</td><td>-0.440</td><td>-0.400</td><td>0.252</td><td>0.400</td><td>0.589</td><td>0.803</td><td>0.550</td></tr><tr><td>PRED1</td><td>-0.142</td><td>-0.207</td><td>-0.428</td><td>-0.468</td><td>0.352</td><td>0.457</td><td>0.580</td><td>0.632</td><td>0.818</td></tr><tr><td>PRED2</td><td>-0.110</td><td>-0.183</td><td>-0.307</td><td>-0.351</td><td>0.274</td><td>0.274</td><td>0.408</td><td>0.446</td><td>0.836</td></tr><tr><td>PRED3</td><td>-0.233</td><td>-0.308</td><td>-0.269</td><td>-0.380</td><td>0.209</td><td>0.313</td><td>0.258</td><td>0.367</td><td>0.745</td></tr></table>

## Appendix C: Analysis of control variables and methodological biases

We test our final model (see, Figure 5) against variation of the collected demographic characteristics (company size, industry sector, and employee tenure) in our sample population by using multi-group-analysis (Jr., J. Hair et al., 2014). The idea is to split the original data set into distinct smaller subsets (e.g., one subset with all responses from companies with less than 5000 employees and one subset with all responses from companies with more than 5000 employees). Then, the final PLS-SEM model is calculated for each subset and the output is compared to test for statistically significant diferences (i.e., non-

Table 10. Results (p-values) of the SmartPLS multi-group-analysis.

<table><tr><td rowspan="2">Path</td><td colspan="5">Comparison groups (p-values)</td></tr><tr><td>Company size (&gt;5000 vs ≤5000 employees)</td><td>Industry(Finance vs IT)</td><td>Industry(Finance + IT vs all others)</td><td>Tenure(&gt;10 years vs ≤10 years)</td><td>Survey(Paper vs online)</td></tr><tr><td>SORG→DORG</td><td>0.225</td><td>0.262</td><td>0.616</td><td>0.138</td><td>0.718</td></tr><tr><td>SORG→SIT</td><td>0.546</td><td>0.325</td><td>0.660</td><td>0.841</td><td>0.898</td></tr><tr><td>DORG→DIT</td><td>0.902</td><td>0.517</td><td>0.501</td><td>0.896</td><td>0.243</td></tr><tr><td>DORG→SIT</td><td>0.459</td><td>0.765</td><td>0.993</td><td>0.372</td><td>0.615</td></tr><tr><td>EAM→SIT</td><td>0.949</td><td>0.185</td><td>0.432</td><td>0.332</td><td>0.995</td></tr><tr><td>EAM→DIT</td><td>0.327</td><td>0.286</td><td>0.395</td><td>0.441</td><td>0.125</td></tr><tr><td>SIT→AO</td><td>0.758</td><td>0.359</td><td>0.100</td><td>0.769</td><td>0.774</td></tr><tr><td>DIT→AO</td><td>0.531</td><td>0.158</td><td>0.911</td><td>0.778</td><td>0.965</td></tr><tr><td>Moderation</td><td>0.797</td><td>0.565</td><td>0.896</td><td>0.900</td><td>0.930</td></tr></table>

overlapping confidence intervals). In our case, we are required to group several smaller categories together (e.g., combining industries with few responses in our sample) to allow for statistically meaningful comparisons. We compare several diferent subgroups (see the comparisons and p-values in Table 10) and find no significant (p > 0.1) diferences. This only implies that there are no significant diferences for specific variations within(!) our sample in terms of company size, industry, tenure, and the survey instrument (paper vs online survey). However, certain populations (e.g., very small organisations, Asian/African organisations, or specific niche industries) are still excluded from our analysis.

Additionally, we argue that this multi-group-analysis (Jr., J. Hair et al., 2014) can be employed to test for inflated estimates due to common method bias (Podsakof et al., 2003). To this end, we compared the responses from the online and the paperbased survey and found no significant diferences (Jr., J. Hair et al., 2014; Rigdon et al., 2010). In combination with the high response rate (88%) of the paper-based survey, this also allows us to rule out nonresponse bias (Gefen et al., 2011; Sivo et al., 2006).

## Appendix D: Saturated model analysis

To ensure that no significant path has been left out in the final model, we compared the results from our final model (see, Table 4 and Figure 5) with the results obtained from the saturated model (Gerbing & Anderson, 1988), in which there are paths among all pairs of latent variables (see, Table 11 of Appendix B). We find that all significant paths in our theoretical model (Figure 2) remain significant in the saturated model (Gefen et al., 2011). Furthermore, we checked that adding paths from the saturated model would not significantly increase the observed efect sizes (Gefen et al., 2011).

Table 11. Path coeficients of the saturated model (\*\*\*: p < 0.01, \*: p < 0.1).

<table><tr><td></td><td>DORG</td><td>SIT</td><td>DIT</td><td>AO</td></tr><tr><td>SORG</td><td>0.514***</td><td>-0.201***</td><td>-0.032</td><td>-0.050</td></tr><tr><td>DORG</td><td></td><td>-0.280***</td><td>-0.345***</td><td>-0.034</td></tr><tr><td>SIT</td><td></td><td></td><td>-0.494***</td><td>-0.304***</td></tr><tr><td>DIT</td><td></td><td></td><td></td><td>-0.150*</td></tr><tr><td>EAM</td><td></td><td>-0.398***</td><td>-0.207***</td><td>-0.242***</td></tr></table>
