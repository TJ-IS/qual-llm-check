---
otero_id: 21397
otero_key: "4627H9JB"
title: "A substance-theory-oriented approach to the implementation of organizational DSS"
authors: "Hannu Kivijärvi"
year: "1997"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(96)00069-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A substance-theory-oriented approach to the implementation of Organizational DSS

Hannu Kivijärvi \*

Helsinki School of Economics and Business Administration, Runeberginkatu 14-16, 00100 Helsinki, Finland

## Abstract

Organizational Decision Support Systems are general-purpose, multiple-user, large-scale systems that have a relatively definite, continuous and organized position in the planning and decision making processes of an organization and which are designed for a variety of organizational decisions. Because designing, developing, and implementing an ODSS is a more challenging task than that of one-function or one-user DSS, strong and clear methodological principles are needed to manage the development process. In this conceptual research a novel and comprehensive framework for the implementation of an organizational DSS is outlined. The proposed approach is a Substance-Theory-Oriented (STO) methodology to design and develop ODSS. According to the methodology, the emphasis in the implementation process is moved from technological aspects closer to managerial, substantive aspects. We believe that all phases of the development process can be supported by appropriate managerial theories. The central theme of this paper is to show that the managerial substance-theories can be used to direct what should be included in and how to develop an ODSS. © 1997 Elsevier Science B.V.

Keywords: Organizational Decision Support Systems; DSS development methodology; Substance-oriented; Managerial theories; Descriptive-normative

## 1. Introduction

"A DSS is a computer-based information system that affects or is intended to affect how people make decisions" [143]. Decision Support Systems (DSS) differ from the other information systems in respect of their structure, development, use, and research. DSS first appeared in the early 1970s and have since been applied to a variety of disciplines, including finance, marketing, and production [46,68,137]. During the last twenty years they have become mainstream within the information and decision sciences. The relevant research and other literature unquestionably show that DSS have extended the frontiers of traditional information systems as well as the capabilities of the decision makers.

The early DSS literature was mainly definitional $[8,9,81]$ ; it was important to make a clear distinction between DSS and the traditional data processing, MIS, and OR/MS models. Later in the 1980s, DSS scholars emphasized the building process of DSS $[20,22,114,115,146,150]$ . The goal has been to develop sound frameworks, theory-bases, and development principles that would lead to valuable applications in practice. Building and developing DSS is usually characterized to be an iterative process, and evolutionary prototypes are frequently employed. Practically and conceptually, it is difficult, if not impossible, to isolate the use and development phases of DSS from each other. Characteristically, also the role of the end-user is critical in the development process of DSS.

The proposed theoretical frameworks as well as the architectures of the systems have been mainly technological and problem-oriented. A reason for the generality of technique-orientation might be that all decision situations are perceived to be specific and entirely different; managers handle their actual decision problems without interference from general theoretical frameworks or research results $[26,113]$ . It is assumed that DSS can be discussed in general only at the technological level, otherwise the DSS are expected to be unique. Consequently, for example, all descriptions concerning the generic structures of DSS, the DSS architectures, are plainly technological. Some researchers (Stabell $[147,148]$ at the forefront) have made efforts to recall the original object of DSS – the decision making. Still, the DSS movement is almost completely technique- and problem-oriented.

Most DSS are designed to support a specific, relatively narrow decision problem met by a single decision maker. However, it is possible that DSS cover the whole organization and are aimed at supporting organizational decision making. Such organizational, corporate-wide systems have recently gained increasing attention in the DSS literature $[5,28,51,52,77,126]$ . In the present paper the emphasis is on institutional $[39,50]$ , Organizational Decision Support Systems (ODSS). “The focus of an ODSS is an organizational task or activity or a decision that affects several organizational units or corporate issues” and “an ODSS cuts across organizational functions or hierarchical issues” $[51]$ . By institutional, ODSS, as opposed to functional, ad hoc DSS, we mean general-purpose, multiple-user, large-scale systems that have a relatively definite, continuous and organized position in the planning and decision making processes of an organization and which are designed for a variety of organizational decisions. Specifically, ODSS support general coordination and integration of activities, consolidation of the budgets or other analyses presented by various divisions or departments, and test the implications of decisions by one part of the company on the rest of the company.

Designing, developing, and implementing an

ODSS, sometimes referred as a corporate-wide support system or even a global DSS, is a more challenging task than that of one-function or one-user DSS. The need for such systems, however, has been recently highlighted on several occasions. Eom [45], for instance, argues in favour of the global DSS: “A major challenging task during 1990s to both practitioners and theoreticians will be to integrate the separate DSS that coexist in an organization into a global DSS and a total system in order to create a system that integrates organizational decision making across functional fields, planning horizons (long-range, medium-range, and short-range) and national boundaries to create a coordinated global strategy”. The primary reasons for developing and, thus, studying the ODSS instead of the DSS are the potentially attainable synergetic advantages, or system economics within the organizational decision making.

While ODSS are recognized as important and demanding, no methodological principles have been proposed or discussed in the DSS literature to manage the implementation process of the ODSS. There is an obvious need for such conceptual and methodological considerations. However, where managerial decision making in companies and other organizations is concerned, a lot of common theories are developed for different kinds of decision situations. In principle, scientific theories in finance, marketing, and production are descriptive or prescriptive (normative) explanations of how decisions within these functional areas are made or should be made in the best possible way. These theories represent the finest knowledge we have on organizational behaviour, managerial problems, economic rules, etc. Unfortunately, these theories are lacking in the DSS literature, especially where ODSS are concerned. The central theme of this paper is to show that these theories can be used to direct what should be included in, and how to develop an ODSS.

In this study we propose a Substance-Theory-Oriented (STO) approach to design and develop ODSS. In principle, the substance-orientation of any methodology can vary from total ignorance to tight commitment to specific theories for given functional area. Here, the whole ODSS implementation process is explicitly tied to managerial substance theories.

The study has three classes of motivation. First, we would like to move the emphasis in DSS design and development from technological aspects closer to managerial, substantive aspects. Second, we believe that the requirements for managerial support cannot be obtained by direct inquiries from the decision makers. Third, a conceptual link between descriptive analysis and normative design in DSS development is needed. Otherwise they remain conceptually distinct and practically confused.

In this study we use the term “implementation process” broadly to refer to the different phases of the design, development and use activities of the entire DSS life time. By addressing the issues of the implementation process, certain methodologies of DSS design and development are discussed in the next section. A conceptual distinction is identified between conventional and substance-oriented methodologies. We then focus on how some managerial, functional theories can serve as a framework for the ODSS and how these theories can direct and guide the implementation process. We believe that this is the most fruitful approach to integrate the DSS movement into other managerial theories and, on a practical level, to develop ODSS that are explicitly linked to a larger organizational context.

## 2. Conceptual background

The wide range of literature concerning DSS methodologies has been evaluated and classified on several occasions $[3,4,14,15,147]$ . The next reassessment highlights the differences and similarities between the methodologies in order to find some conceptual background for the STO approach which is presented in the following section.

## 2.1. Conventional conceptualizations of DSS development methodologies

## 2.1.1. Procedural methodologies

Generally, the growth of computerized information systems follows the stages of the product life cycle process. The life cycle model is appropriate for most traditional information systems, MIS, and OR/MS models. According to the DSS literature, constructing a DSS differs significantly from other IS development activities; the different stages are interrelated and they tend to proceed concurrently. Although the traditional life cycle approach has not been accepted in the DSS literature, in practice, however, it has been applied more often than expected, especially with large-scale, institutional DSS [68].

The development of DSS is repeatedly characterized to apply evolutionary [6,119,135], adaptive [7,78,82], iterative [146,150] or middle-out [22,72] approaches. Most of the procedural methodologies are aimed at constructing DSS for a single user with a single decision problem. However, for developing ODSS, a staged implementation approach is presented [28]. It is a combination of life cycle and iterative/adaptive approaches.

## 2.1.2. Representation-centered approaches

The arguments for a representation-centered design [24,82] emphasize the value of features for minimizing the amount of the user's mental energy consumed in the technical operation of the system. The design of the dialog component, or user interface, is the main issue in this design approach. The representation-centered approach is concretized as ROMC method (Representations, Operations, Memory-aids, Control mechanisms) which is a process-independent approach for organizing and conducting the DSS development [146]. If DSS are understood broadly, then another representation-centered approach for designing and developing a DSS is the methodology for developing Executive Information Systems [131,149]. This approach emphasizes the format in which executives can use the information; reports, graphics, documents, mail, and data used in the decision making process.

## 2.1.3. Decision-oriented methodologies

In the decision-oriented [147,148] approach, analysis and diagnosis prior to the system design are key stages. The approach provides a basis for development of systems that are explicitly linked to the larger context of an organization's goals. The approach is meant to focus attention on how system development can be a vehicle for improving decision making. It is also important to develop systems that are compatible with the existing decision-making behaviour. The challenge is thus to provide a behaviourally grounded, but normatively oriented approach to building DSS. The main phases and the iterations of the decision-oriented design are described in Fig. 1. This model is a point of departure for the methodology to be presented in Section 4.

![](/api/attachments/4627H9JB/fulltext/images/a4ec90fa1422ecca12347f77632126b7a60d514cd7d65db951bfb41c504757db.jpg)  
Fig. 1. Decision-oriented DSS development process [147].

An alternative, but related decision-oriented approach is the methodology based on individual differences, especially on the cognitive styles and processes of decision makers $[71,81,105,128,130]$ . The issue-based approach $[43]$ is rather based on larger problem issues than primarily on decisions. It is a management process rather than a systems development process. The development procedure has a strategic issue structuring front-end and it explicitly distinguishes between information support services and decision support services.

## 2.1.4. Systemic approaches

The premise of the systemic view of DSS development $[13,85]$ is that in order to understand DSS, the environment, role, components, arrangements of components, and the resources required to support the system must all be considered simultaneously. The emphasis is on the whole range of organizational decision making.

## 2.1.5. Contingent approaches

Contingent approaches give guidance how to choose among the other, basic approaches. Ginzberg and Ariav [56] continue to develop their systems approach by proposing a contingency approach emphasizing the conditions under which the different approaches are appropriate and effective. Arinze [14] develops also a contingency model using three criteria: paradigm, structure, and orientation. He identifies ten DSS methodologies and then derives a contingency framework for methodology selection of DSS development. The primary benefit of the contingency approach is to enable a more conscious selection of appropriate design and development methods that fit to the original problem situation and are likely to lead to successful problem solving.

The different “schools” of DSS implementation methodologies cited above represent the dominant perspectives found in the DSS literature. They certainly overlap and have a lot of common properties. Ginzberg and Ariav [56], for example, treat the evolutionary, adaptive, and middle-out approaches similarly enough to permit generalizations about their salient features. We feel, however, that these approaches, although closely related, have some unique characteristics and can be treated as different approaches that describe the different midpoints in the DSS development.

## 2.2. Substantive conceptualizations of DSS development methodologies

A deficiency of traditional DSS development methodologies cited above, especially with procedural methods, is that they support present, possibly seriously deficient decision making routines. They fail to draw upon what we know about business, organizations, and decision making. Without a clear goal the development process is often groping. Within the traditional methods, with the exception of decision-oriented methods, the prevailing working principles and business processes are assumed to be given; their validity is not questioned. This leads to systems that support an inefficient action, that is, inefficient decision making is cemented by a DSS. Typically, they do not carry any new information into the organization.

A shortage of the traditional methodologies is that they do not define the substantive context of the system. Generally, substance is “the essence which underlies and is capable of having attributes or causing phenomena, but which in spite of changes in outward manifestation remain the same” [Webster’s].

In the organizational context, substance, as opposed to methods or procedures, means the underlying essence of the organizational processes, structures, decision making, business conditions, etc. In order to identify some conceptual background for the implementation of organizational, institutional DSS that would originate more closely from the substantive content of the decision-making environment, we need to reassess some alternative methodologies. In these methodologies, the contextual, substantive knowledge and its management is at least implicitly inherent.

## 2.3. Corporate models

One substance-oriented direction of research striving to integrate the different functions of a company and to look at a company holistically is corporate models. Although the conceptual similarities and differences between DSS and corporate models have been questioned $[121]$ , the corporate models, or corporate planning models, form a potential approach to identifying conceptual foundations for organizational, substance-oriented ODSS methodology.

The integrative and holistic views of the corporate models are frequently emphasized in the relevant literature $[59,61,65,120,132]$ . Recently, the term “Enterprise Modeling” has gained more attention $[16,38]$ . However, it is possibly a more information technology-oriented approach than corporate models tend to be.

The process of developing corporate models is much more problem-oriented than technique-oriented. Naylor [120], for example, formulates a six-step approach for integrating a corporate model into the planning process:

1. review of the planning environment;

2. specification of planning requirements;

3. definition of the goals and objectives for planning;

4. evaluation of the existing planning resources;

5. design of an integrated planning and modeling system;

6. formulation of a strategy for integrating the planning model into the planning system.

The design of the corporate model itself (Phase 5) certainly depends on the technique chosen. For example, if a model based on econometrics is chosen, then the phases of the modeling typically include model specification, parameter estimation, model validation, and policy simulation.

![](/api/attachments/4627H9JB/fulltext/images/abb61ade5051310f318a43fc9d70c2bf8bcf87477d78c7b6f2013de0bab1e603.jpg)  
Fig. 2. A conceptual framework for corporate models [120].

Modeling and model management have always been the main interests in corporate modeling whereas data base management and user interfaces are almost completely ignored. The diversity of interests is apparent in the different conceptual frameworks for corporate models. In Fig. 2, Naylor's framework for corporate models is described.

In Naylor's framework the marketing models – forecasting or econometric – provide the sales revenue projections to the other modules. Production models estimate the costs of producing at a given demand level. At the business unit level the financial models get the input data from the marketing and production models and produce as output, income statements, cash flow statements, and possibly, balance sheets. At the corporate level all financial plans of the business units are integrated and coordinated.

In principle, the corporate models have a direct connection to the different theories of a firm and thus, their design principles and structures are useful sources for theory-oriented frameworks for DSS design and architecture. Unfortunately, the concept of corporate model, a popular theme in the 1970s and 1980s, has almost disappeared from recent managerial literature. However, in the empirical study of Hogue and Watson [68], one half of the DSS was used in corporate planning and forecasting.

## 2.3.1. Expert systems

Expert Systems (ES) are “those computer-based systems that go beyond organizing and retrieving information to embody human reasoning and expertise that operates on information to either perform or assist in the performance of specific decision making” [62]. They are systems “that employ human knowledge captured in a computer to solve problems that ordinarily require human expertise” [150]. ES have been applied to a wide variety of managerial problems including investment portfolio management, tax planning, project management, credit analysis, financial statement analysis, material selection, inventory management, etc. [12,69,92,139,140,150].

The distinctive characteristics of ES are their ability to transfer knowledge, reason and explain. ES are designed for non-experts to increase their problem-solving capacity and for experts to serve as knowledgeable assistants. The primary difference between DSS and ES is that DSS manipulate numerical data whereas ES employ elements and sets of knowledge [150]. The procedure for designing and developing ES does not differ essentially from that of DSS. The distinctive phases are knowledge acquisition, knowledge representation, and inferencing.

Perhaps the most interesting part of any ES is the knowledge base which contains judgment rules, procedures and specialized facts related to the particular problem domain, that is, to the substance. For our purposes it is interesting to note that the knowledge base may also include theoretical knowledge related to the problem domain.

The main limitation of ES is that they work well only in a narrow problem domain. Therefore their usage for the organizational decision support is at the moment very limited. However, ES may be integrated into an ODSS as supplementary components. In addition, the features of knowledge (external or internal) orientation may also be emphasized in DSS.

In the sections above traditional and substance-oriented DSS development methodologies were briefly reviewed. The focus of the next section is to outline a systematic conceptual framework for Substance-Theory-Oriented DSS design and development, a framework which is sufficiently broad to include the entire corporation. The objective of the framework is to identify potential issues for ODSS development methodology and hold them together to enable us to create a substance-oriented process-model for ODSS development, which is presented in Section 4.

## 3. A framework for the substance-theory-oriented ODSS implementation methodology

## 3.1. Prerequisites for an ODSS methodology

In the previous section DSS research was classified into two groups: traditional methodologies and substance-oriented approaches. The main distinction between these two classes of development methodologies lies in their substance-orientation. Behind the traditional methodologies, the characteristics of the development process per se, the attributes of the decision making in general, or some other “how-aspect”, is the driving force. Within the corporate models, on the other hand, the emphasis is always on integrated solution of financial, marketing, and production problems. Similarly, within the expert systems, the whole development process is oriented at capturing the substantial knowledge of the expert and to diffuse it to wider utilization. In the substance-oriented methodologies, the “what-aspect” is always the primus motor.

The central theme of this paper is to show that the substance theories can be used to direct what should be included in and how to develop an ODSS. March and Simon [107] distinguish between procedural and substantive programs when defining the problem-solving process. By substantive programs they mean programs “that are meant as structuring of the problem-solving process that comes about as a reflection of the structure of the problem to be solved”. Recently, the need for such substance-oriented approaches has been well recognized in the DSS literature. Silver [143], for example, asks: “What do we do substantively as we design in an adaptive, middle-out, and evolutionary manner?”.

The theories presented in management and organizational literature are a potential source of substantive knowledge. By a managerial substance theory, as opposed to a methodological theory, we mean a theory, or a theoretical model, that explains the general principles how things are or should be related in a managerial context.

In principle, theories in finance, marketing, and production are descriptive or prescriptive (normative) explanations of how decisions within these functional areas are made or should be made in the best possible way. They have descriptive, explanatory, predictive and normative power. These substance theories represent the best, crystallized knowledge we have of organizational behaviour, managerial problems, economic rules, etc. They are, or at least intend to be, generic and independent, for example, on a specific company, and they are generally available.

If dichotomized, managerial theories can be classified into two categories: descriptive and normative (prescriptive) theories. Roughly, the descriptive theories aim to answer “How is” questions and normative “How ought to be” questions. Descriptive theories purely intend to describe the object. According to the most rigorous interpretation, descriptive theories only describe the present state, activities, conditions, rules, etc. without reference to their histories. They do not compare managerial practices or companies with each other or evaluate their actions by any measure. On the other hand, normative theories include ethical principles and value judgments, they give guidelines for action, or evaluate the object by some norm-natured criteria.

The quality of norms in normative theories can vary a lot. Theories that include some evaluative components are normative in a “weak” sense: there is a norm or some other evaluation premise against which the current situation can be compared. On the other hand, theories that produce explicit guidelines, strategies, policies, or other directions of action are normative in a “strong” sense: they transform the initial conditions and evaluation statements into decisions. All optimization-oriented theories are of that type. Normative theories, or theoretical models, typically originate from economics or Operations Research/Management Science.

For the development of all DSS both theory types are of value. During the different phases of development process descriptive understanding of the structures and processes of the organization as well as normative guidelines how it should work are always needed, explicitly or implicitly. The more explicit this knowledge is, the better is the outcome. If the theories are properly applied, they can carry along new information into the organization. They lead to “strong design” instead of “weak design” [119], help to concentrate on the essentials, and reduce the number of iterations during the process.

Although the development of ODSS is not a straight process but iterative, evolutionary courses of actions are needed, it is still possible to distinguish some main phases within the development process. In the decision-oriented approach as proposed by Stabell [147], the development process is divided into two main activities: descriptive and normative modeling. The last phases of Stabell's process model are related to the change of the object organization. Similarly, Keen and Scott Morton [81] make a distinction between descriptive and normative analyses.

The value of substance theories, especially the normative ones, cannot be overemphasized when ODSS are concerned. Because ODSS are not intended to support a single decision but are general-purpose systems, general managerial theories are a natural means to define the context of an ODSS. ODSS are used by a number of decision makers around the organization, and therefore, the analysis of contradictory requirements can be balanced and supported by normative theories. Equally, all phases of the development process – descriptive analysis, normative design, and directed change – can be strengthened by appropriate theories or theoretical models. From the economical point of view, ODSS are more expensive than single-user systems. Therefore, efforts should be made to reduce the number of iterations in the development process. Properly applied theories can do that. Generally, large, complicated systems cannot be developed without some guiding principles – the change of decision process is a directed process. Managerial theories are a forgotten resource that can satisfy this need.

## 3.2. The essence of the conceptual framework

When we are searching for a framework for the implementation methodology of ODSS, a natural starting point is the essence of the organization in general. Here, in the following discussion we concentrate only on business organizations. Consequently, the conception of the company determines the initial premises and requirements of the ODSS development methodology.

The classical view of the firm is that of a unified, profit maximizing entity. Another view, as emphasized by the agency theory $[133,156]$ , explains that the firm is constituted by self-interested agents (employees) whose objective is to maximize their own, individual utility. According to this view, one of the main tasks of management is to develop incentives that would push the agents to act so that, finally, the owners' utility is maximized. The conflict between the principal and agent can be generalized to all organizational levels and even to the interactions between organizational units at the same level. Thus, every organization needs both internal and external information about the goals and objectives of individuals, groups, departments, and the whole company. A great deal of information is needed for communication, coordination, control, etc. A major part of the internal information, if not all of it, is finally used to support decision making.

Generally, a firm serves as an intermediary between the product markets, consumers, and the suppliers of different kinds of inputs. This holistic perspective indicates that the stakeholders of a firm go beyond the investors and managers to include customers, suppliers, employers, distributors, etc. Thus, in order to find a valid theoretical basis for the development of a corporate-wide DSS we need a theory or a collection of theories about the behaviour of a whole corporation including the behaviour of all significant stakeholders. In Fig. 3, a general conceptual framework, a classification schema, is proposed to outline the domain of potential theories.

In Fig. 3, actually, the structure and the process of a generic firm are described. The hypothetical firm is a decentralized, hierarchically organized firm, which makes products for the product markets, supplies production factors from the raw material and labour markets, and carries out financial operations on financial markets. The purpose of the framework is as much to identify and connect potential issues as to classify them.

## 3.3. Categories of managerial substance theories relevant to ODSS implementation

For our purposes, according to Fig. 3, the framework for implementing ODSS consists of the following generic categories of substance theories:

1. theories of goals, objectives and strategies of a firm;

2. theories of organization structures, planning levels, and decision-making processes;

3. theories of accounting, finance and financial markets;

4. theories of marketing and product markets;

![](/api/attachments/4627H9JB/fulltext/images/ed4ffee26c32bc8879d64a1d17210e5a0a8c6eb792b6959232cba9332ff26233.jpg)  
Fig. 3. A framework for the implementation of ODSS.

5. theories of production and the markets of production factors;

6. theories of information systems.

Thus, the theory base consists of a wide variety of managerial theories. Stabell [148] emphasizes that “no single, coherent theory can provide the necessary basis for describing and understanding decision behaviour in illstructured decision situations”.

Table 1 includes some examples of potential substance theories that can be used in ODSS implementation. The theories are classified into three groups according to the development phase which they are intended to support: descriptive analysis, normative design, and directed change. In principle, the distinction between descriptive and normative theories is clear. However, it is common that one single managerial theory may have both of these properties. Therefore, some of the examples in Table 1 could be moved from descriptive analysis to normative design, and vice versa.

Examples of the substance theories needed for ODSS development and potential sources

<table><tr><td>Development phase</td><td>Theory</td><td>Source</td></tr><tr><td>Descriptive analysis</td><td>1. Theories of goals, objectives and strategies of a firmBehavioural theory of the firm2. Theories of organization structure, planning levels,and decision making processesSystems approach to organization structureTheories of organizational decision processesTheories of organization growth and developmentTheory of planning and control3. Theories of accounting, finance and financial marketsPositive Accounting TheoryTheory of capital structure4. Theories of marketing and product marketsTheory of consumer behaviour5. Theories of production and markets of production factorsEvolution theory of manufacturing processesand technologies6. Theories of information systemsTheory of IS growth</td><td>[30,106][75][144,125,117][58,99,84][11][152][63][70,21][1]</td></tr><tr><td>Normative design</td><td>1. Theories of goals, objectives and strategies of a firmTheory of competitive strategyTheory of AHP2. Theories of organization structure, planning levels,and decision making processesUtility theoryTheory of choiceSystems theoryTheory of Hierarchical Systems3. Theories of accounting, finance and financial marketsBudgeting theoryTheory of Cost-Volume-Profit analysisPortfolio selection theoryInvestment theory4. Theories of marketing and product marketsTheory of demandTheoretical models of distribution, pricing,advertising, and sales force5. Theories of production and markets of production factorsTheory of production6. Theories of information systemsTheory of IS developmentRelational database theory</td><td>[127][134][158][94][54,47][116][10,66,154][40][109,140][96,64][33][100][48,49,37][151][29]</td></tr><tr><td>Directed change</td><td>Theory of organizational changeReliability theory</td><td>[97,136,93][27]</td></tr></table>

According to Table 1, for example, the behavioural theory of the firm as presented by Cyert and March [30] can be used to understand and describe the organizational goals and objectives, expectations, choice and control. Goals and objectives define the purpose of the firm, they show the direction to growth and development, and are arguments for rational decision making. The neoclassical theory of a firm, especially price theory, assumes that the purpose of a firm is to maximize its net profit. In the management literature this single-goal approach is constantly criticized. Levy and Sarnat [96], for instance, propose that the firms may have, among others, the following goals: maximization of profits, maximization of sales, survival of the firm, achieving a “satisfactory” level of profits, achieving a target market share, some minimum level of employee turnover, “internal peace”, and maximization of managerial salaries.

These and other goals are not necessarily in harmony but more usually are competitive and contradictory. This holds especially with large ODSS. A vast amount of literature on multicriteria decision making possibly describes the importance and generality of multicriteria decision-making problems $[41,157]$ . An alternative to maximizing expected monetary return is presented by multiattribute utility theory $[158]$ .

An enormous number of theories on organization structures and their development have been presented since the beginning of this century [75]. Mesarovic et al. [116] were among the first authors who gave formal presentations of multilevel, hierarchical structures. They formalized the hierarchy concept in the framework of mathematical systems theory and developed a mathematical theory of coordination.

Anthony's [11] classification of management process consists of three levels: strategic planning, management control, and operational control. These three planning levels are possibly the most frequently cited in the literature and possibly have had the greatest effect on managerial practice, too. The existence of different planning levels is also well recognized among the budgeting theories (build-up vs. top-down). One purpose of an ODSS is to tie the planning levels more closely together.

There are several ways of conceptualizing organizational decision making and the respective theories. For example, Keen and Scott Morton [81] classify the different conceptions of decision making into the following five schools: the rational view of decision making, “satisficing” and the process-oriented view of decision making, the organizational process view, decision making as a political process, and the individual differences view. Depending on the conception adopted in the development team, ODSS development can turn even into opposite directions.

The best-known process model of decision making is the one presented by Simon [144]: Intelligence, Design, and Choice (IDC). Unfortunately, the IDC model is relatively vague and it fits all decision processes. One purpose of an ODSS is to support all phases of this process and make the process flow smoothly. As an alternative, when Nutt [125] empirically studied 78 practical decision processes in detail, he was able to separate and classify the decision processes into the following five archetypal processes with some variations: Historical model, Off-the-shelf, Appraisal, Search, and Nova. Theoretical identification and conceptual understanding of the archetypes will certainly help the descriptive analysis in practice.

The problems of marketing managers extend over a variety of issues including the shape of aggregate sales response to a single marketing instrument, marketing mix interaction, competitive effects, delayed response, multiple territories, multiple products, marketing-corporation interactions, multiple goals, and environmental uncertainty effects [100]. Due to the extensive and important problems in marketing, a lot of theories are developed to describe and solve these and other problems at theoretical levels [141]. Some general marketing theories have been proposed [18,42] but a great number of theories about the special problems in marketing, e.g. prizing, advertising, consumer behaviour, etc. have been developed. For example, Sheth, Gardner and Garrett [141] classify the various marketing theories into twelve distinct schools.

Conceptually, an important concept for marketing management, and thus for a DSS supporting marketing decision making, is the sales-response function, which describes the relationship between the sales volume and the elements of the marketing mix. For the estimation of sales-response functions, statistical, experimental, or judgmental methods can be used. The estimated sales-response function can be used for profit maximization or demand forecasting. The theories of demand and the different forecasting methods – quantitative and qualitative – are the most relevant elements for the development of ODSS.

For the building of ODSS, the theory of demand has three potential functions. First, it is a basis in causal methods to forecast demand; it can be used in specification of the demand functions. Second, the marketing models specified on the grounds of demand theory and estimated on the grounds of available data can be directly used as a decision aid in marketing; by varying or simulating the values of explanatory variables (price, advertising, public relations, product quality, sales force, distribution, etc.) it is possible to predict changes in sales. Third, the theory of demand can be used in determining the information requirements of marketing managers. The information requirements direct the DSS design process and they can be satisfied by different strategies.

Theories of production have been developed both in engineering science and in economics. The production theories differ greatly, for example, by production type (process, job shop, etc.), time horizon, or the level of planning (strategic, tactical, operational). For the purposes of the ODSS, two areas of production theories are the most relevant – technology of production and production costs.

The core of most production theories in economics is the production function: it specifies the maximum rates of output that can be produced from each possible combination of inputs. Production functions are used to represent the physical relationship between the inputs the firm employs and the outputs that are produced. By means of the production functions it is possible to summarize the existing technologies, that is, the constraints under which the firms may carry on production.

Another relevant theoretical concept for the design of organizational DSS is the cost function, which expresses total costs as a function of production output. An alternative concept is the cost equation, which relates total costs to factor inputs. Accountants and economists may have different conceptualizations of costs. In accounting the outlays of the firm, expenses, form the cost concept but in economics the cost is “that payment required to keep resource in its present employment” [122].

Unfortunately, at the present time there is no comprehensive theory of accounting or finance. The American Accounting Association's Committee on Concepts and Standards for External Financial Reports concludes that no single governing theory of financial accounting is rich enough to encompass the full range of user-environment specifications effectively; therefore, in the financial accounting literature there does not exist a theory of financial accounting, but a collection of theories which can be arrayed over the differences in user-environment specifications. Thus, accounting and financial theories rather provide a coherent set of logically derived principles that serve as a frame of reference for evaluating and developing accounting principles than provide a basis for the prediction and explanation of accounting behaviour and events [19]. With the same principle, these theories can serve as a frame of reference for developing and using ODSS. For example, positive accounting theory [152] helps to analyze the choice of depreciation methods, inventories, association between earnings and stock prices, or earnings' time series properties.

In Fig. 4 the arrows describe the flows of material, money or information. Any organization will comprise a series of information systems (IS), and IS theories have become a vital part of managerial theories. Research on IS and the respective theories can be classified in a variety of ways beginning from the technological, “silicon chips” levels and ending with the cognitive information processes of a human being or the social impacts of IS on the whole society [111]. A lot of research relevant to ODSS implementation is done for example in the following areas: analysis of information requirements [31], design and implementation of information systems [102–104,159], evaluation of information systems [17,73], investments in information systems [76,153], value of information [44,108], quality of information [91], forms of information presentation [74], inter-organizational information systems [123,129], local, national, and international networks [60,110], group systems [35,36,57,112], user interfaces [142], and data bases and data base management systems [22,23,29,67].

## 3.4. Magnitude of the framework

When building a framework for the implementation methodology of ODSS, a natural starting point is the essence of the firm in general. Consequently, the conception of the firm determines the premises and requirements of the ODSS implementation methodology. In this section we have proposed a Substance-Theory-Oriented framework for the implementation of organizational DSS. It is a structure serving to hold the different parts of the methodology together. The wide scope of the framework lies on the holistic picture of the firm. It is hypothesized that the implementation and the respective architectures of ODSS should not be solely based on: 1. the technological capabilities, or

2. the ongoing organizational behaviour, or

3. the common theories of decision making, but multiple, functional models and theories of organizational decision making are needed to decide what to include in and how to develop an efficient DSS. Some examples of substance theories that might increase descriptive understanding or provide prescriptive guidelines for ODSS implementation are also briefly discussed. It is clear that the “review” is tentative and not meant to be exhaustive.

Usually, managerial theories are rather a standardized art than strictly defined and separated. A lot of competing theories, or theoretical models, explain the same phenomenon but still give only a partial explanation of its behaviour. Further, the theories may have hierarchical relationships with each other. For example, signal theories can be utilized in agent theories which are used to explain the behaviour of the capital markets. Methodological theories that concentrate only on the validation of better measurement instruments are of value, too (see, e.g. [32]).

In the managerial literature, the “quality” of theories varies widely. Theories in the textbooks at introductory level are obviously quite different from the theories presented in the top journals. For the implementation of ODSS the classical, ever-green theories may be more useful than the latest, sometimes quite “pathological” proofs of personal qualification. The usefulness of theories can also vary. Some theories are clearly defined and the conditions and assumptions under which they are valid are clearly articulated. On the other extreme, some theories are so loose that they can be used only indirectly as general training material. Most useable are those theories that are transformed into the form of computer programs. For example, the theory of the Analytic Hierarchy Process $[134]$ is available in some software packages (Expert Choice, LDW, Hipre). As such, the theory can be easily applied as a part of an ODSS $[83,89]$ .

When implementing ODSS, an additional problem may be met: most managerial theories are developed to characterize the behaviour of a single decision maker – not an organization's decision behaviour. In organizational decision-making the tasks and hence the decision problems are divided among groups of people. The “extra” problem in organizational decision-making is the necessity of coordinating the decision behaviour of individuals and groups. This need is usually ignored within managerial theories.

The discussion above was organized according to the structure and the process of a generic firm and the respective managerial substance theories. This short discussion forms the fundamental material for the Substance-Theory-Oriented ODSS implementation methodology to be presented in the next section. Although discussed separately, the different theories are, of course, highly interrelated and interdependent. This categorization of managerial research is more an illustrative example than an exhaustive typology; a lot of other relevant research has been done and can be included into the framework.

In the next section, a proposition for the Substance-Theory-Oriented implementation process of ODSS is offered. The main idea is that managerial substance theories can be utilized at each phase of the implementation process, beginning from the initial problem review and ending with the use and the evolution of the developed system. It is clear that all ODSS cannot be grounded on the same set of theories. The selection of theories depends on the type of organization and its environment (size, industry, competition), the scope and purposes of the system to be developed, management styles, available personnel, etc. Usually, when the meaning of substance theories is discussed in the context of DSS development, they are loosely related only to the “normative modeling” phase $[53,81,147,148]$ . We feel, however, that better results are achieved if every step of the procedure is based on the wide range of qualified managerial theories. Next, we describe such a procedure.

## 4. A proposition for the implementation activities of organizational, Substance-Theory-Oriented DSS

## 4.1. Outline of the procedure

In this section we will outline a Substance-Theory-Oriented procedure which helps to implement ODSS. Our goal is not to present detailed steps or tools but to concentrate on the most important principles that extend the traditional DSS development approaches.

The focus of the procedure to be discussed is that “managers alone are not likely to be able to systematically improve their decision making” [147]. The idea is that external knowledge and intelligence are needed, and even available, to direct the DSS implementation procedure. The developed procedure is based on previous DSS literature, as reviewed in Section 2. The elements of the procedure are Stabell’s decision-oriented DSS development process (Fig. 1), and Naylor’s process of developing corporate models and his conceptual framework for corporate models (Fig. 2). In Fig. 4, the Substance-Theory-Oriented procedure is outlined.

As Fig. 4 indicates, the DSS implementation procedure is divided into three main phases: descriptive analysis, normative design, and directed change. Each phase is then divided into several activities all of which have a theoretical basis to guide the process. Simply, the first main phase attempts to find an answer to the question “What is”, the second to the question “How should be” and the third to the question “How to change”. It is assumed that the descriptive analysis is mainly supported by descriptive theories whereas normative design is guided by normative theories. In addition to the phases, Fig. 4 emphasizes the evolutionary nature of DSS development by including feedback loops between the phases. In Fig. 4 some examples of the involved tasks and a subset of potentially useful theories are related to each activity. Next, each activity of the procedure is briefly discussed.

![](/api/attachments/4627H9JB/fulltext/images/5c1ded8ff8a92d4fd70a71052693f6c8bd1a4e8d3714e02d6c310fec0837495c.jpg)  
Fig. 4. Phases and sub-phases of a Substance-Theory-Oriented procedure for ODSS implementation.

## 4.1.1. Review of organizational decision making

The first phase of the implementation procedure, as depicted in Fig. 4, involves a holistic review of organizational decision making. The effective accomplishment of the phase includes the analysis of existing

• goals, objectives, and strategies,

\- organizational structure,

\- environment,

\- planning procedures, and

• information systems.

The analysis should be performed at the holistic, organizational level in order to build the first picture of the existing decision behaviour over the whole organization by diagnosing the perceived or underlying problems. The review phase may involve the use of different kinds of tools: questionnaires, structured interviews, group discussions, direct observations, etc. It is necessary to collect data from several individuals over the organization to build the organizational perspective from individual perspectives.

The review phase can be supported by several organizational and decision theories and research methodologies. For example, the five archetypal decision processes and their variations by Nutt [125] can help to structure, describe and understand the ongoing decision processes in the organization. The structured observation techniques used by Mintzberg [117] and his findings may serve as a reference methodology for investigating managerial activities. The state of the information systems can be compared to Nolan's [124] stage model.

The factual analysis of the goals and objectives of the firm forms the most fundamental premise for all subsequent activities in the entire implementation procedure.

## 4.1.2. Functional decision analysis

The major aims of the second phase are to identify and characterize the current functions of the company (or departments, subsidiaries, etc.) and to establish the functional requirements of decision support. By separating the main functions of the company we attempt to pay greater attention to the substance aspects of DSS development. Because the functions have a sufficient autonomy to handle their decision tasks in alternative ways, this sub-phase pursues to clarify the extent to which each functional unit has unique needs, organizational and technological constraints, etc. The reference viewpoint that directs the analysis is the goals and objectives and further, the needs and the requirements of the wider organizational system analyzed in the previous sub-phase.

The functional analysis can be supported by an extensive set of functional theories such as empirical financial theories, theories of the development of production systems, theories in logistics, theories of consumer behaviour, etc. All these theories help to understand the behaviour of the functions and the choices they are capable of making.

The primary purpose of the descriptive analyses phase, organizational or functional, is to settle the existing operations, decision procedures and the resulting requirements for decision support. The success of the analysis phases is best supported by the descriptive theories and research methodologies that “provide frameworks for studying the decision processes as they are actually performed within organizations” [92]. A measure of the quality of the phase is the number and quality of the links created between the axioms of the descriptive theories and observations of the business behaviour. These links strengthen the quality of the analyses. If the results are totally contradictory to the theories, analyses possibly have to be rechecked and verified.

As Fig. 4 indicates, it may be necessary to turn to the organizational analysis during the process of functional analyses. It is possible to capture the current managerial relationships between the organizational levels by this iterative process.

Although functional decision analysis is descriptive, as is organizational decision analysis, there is a slight but significant difference between them: functional decision analysis is evaluative in the sense of how well the functions have performed in terms of the goals and objectives given from the higher, organizational level. Still the purpose is to produce factual descriptions about the functional procedures -- as far as it is possible -- without any attempt to evaluate how or whether they ought to made. This is the task of the normative design phases.

## 4.1.3. Organizational design

The second main phase of the DSS implementation procedure is the normative design, which is conceptually a completely different task if compared to the descriptive analysis. The purpose of the phase is to find an answer to the question “How should be” or “How ought to be”, not to the question “How is”. It is often argued that it is impossible to derive an “ought” from an “is” (Hume’s Treatise). If this holds, it means that on the basis of the analysis phase we could not conclude how or what decisions should be made or what characteristics the DSS should have. Searle [138] has, however, shown that if there exists a “system of constitutive rules” involving “institutional facts”, then it is possible to derive “ought” from “is”. The system of constitutive rules forms the necessary logical gulf between the descriptive “is” and the normative “ought”. Now we have reached the culmination of this paper: the system of managerial (normative) theories is the essential element that is needed to join the normative design and the descriptive analysis. Without the normative theories the analysis and design phases remain conceptually distinct and practically confused.

A side effect of the normative theories, in addition to incorporating the descriptive analysis into prescriptive design, is the stabilization of the design and development effort. Along with Dery [34], Smith [145] notices the problem of goals' instability: “Because goals evolve and emerge during the course of problem solving, ‘what ought to be’ is a highly variable target”. A reason for the changing goals is “that the actual users of a DSS may be different from the originally intended ones” [146]. Because managerial theories do not change so quickly they tend to stabilize the process and minimize the number of adaptive iterations in DSS development.

As described in the previous section the descriptive analysis is performed under the “top down” principle. Similarly, the normative design will be performed from organizational design to functional design. The purpose is to build up systems that are explicitly linked to the larger context of the organizational goals, objectives, and strategies. In principle, the organizational design includes the same tasks as the organizational analysis but performed from the normative point of view: how things should be. This includes finding answers, for instance, to the following questions:

\- What goals, objectives and strategies should the firm have?

\- What kind of organization structure should the firm have?

\- If possible, how should the business environment be changed?

\- What kind of planning and decision making procedures should the firm have?

\- What kinds of information systems serve planning and decision making best?

All these and other similar questions aim at identifying ODSS opportunities for more effective decision making.

One of the key tasks of organizational design is to coordinate horizontally across the functional activities and vertically across organizational levels. Sprague and Carlson [146] highlight the issue: “The decision making which occurs at several levels must often be coordinated. Therefore, an important dimension of decision support is the communication and coordination between decision makers across organizational levels as well as at the same level”.

Because it is not feasible to build a whole DSS that initially contains all the facilities required, it is necessary to set priorities for the functional development activities in this phase. The purpose of the priority setting is to decide what to improve and when.

## 4.1.4. Functional design

The purpose of the functional design sub-phase is to define the functional information requirements that are based on the following three components:

1. current functional operations (functional analysis);

2. goals, objectives, and strategies of the predicted (designed) organizational system (organizational design); and

3. normative functional substance theories.

The predicted goals, objectives, and strategies of the company and, on the other hand, the normative functional theories establish the necessary conceptual link between the functional analysis and functional design.

A starting point for the functional design is the results of the functional analysis. The functional analysis is confined by the results of organizational design which establishes prerequisites and other limits. The normative functional theories provide insightful prescriptive guidelines for the functional design in order to change the current state within the constraints to the desired state. Strong and precise definitions of goals, objectives, and strategies in the organizational design reduce the salience of alternatives in functional design. Thus, there is a trade-off between these three components of functional design, and the most fundamental difficulty in functional design is to settle this “is-must-ought” trade-off between the three components.

A part of the “is-must-ought” trade-off is discussed by Moore and Chang [119]. They make a distinction between “weak” and “strong” DSS design: “This concept distinguishes between DSS designs that follow the user’s current preferences and existing capabilities (weak) and those designs that deliberately attempt to shape or refine the user’s decision-making process (strong)”.

The second objective of functional design is to move one abstraction level down in the ODSS design. An outcome of functional analysis is an initial plan for the primary architecture of DSS. Models, model bases, model management systems, databases, database management systems, etc. need to be specified. Within these initial designs, which later will be implemented, all previous work is materialized. Still, the outcome of the design phases is rather a statement of intention than a working DSS.

The following simple descriptive example of demand theory describes how demand theories can be used for determining the information requirements.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$X \in R^{n} =$ Commodity vector with $n$ components.  
$U(X) =$ Consumer's utility function.  
$P =$ The price vector of commodities.  
$I =$ Consumer's income (budget constraint).
</div>

According to the neoclassical theory of demand the consumer aims to maximize his total utility subject to his available income:

$$
\begin{array}{l l} \text { Maximize } & U (X) \\ \text { subject   to } & P ^ {\prime} X \leq I, \\ & X \geq 0. \end{array}
$$

By means of the Lagrange function and under some other assumptions it is possible to determine the necessary and sufficient conditions for the utility maximization and to deduct the demand functions for each commodity:

$$
X = X (P, I).
$$

What is the interpretation of this simplest theory of demand for the ODSS? According to the theory, the marketing manager needs the following information in order to make right decisions:

1. commodities available in the markets;

2. prices of the commodities;

3. the available income of consumers;

4. either the consumer's utility (preference) functions or demand functions.

These information needs are clearly requirements for the marketing modules of the ODSS. The requirements are directly determined by the theory, not by expensive empirical investigations within the marketing department. The different theories of competition, pricing, consumer behaviour, etc. also give valuable information for designing the marketing modules of ODSS.

It is interesting to note that the key concepts of DSS have actually been first introduced within the functional decision problems, in fact, before the first articulations of DSS itself, for example, before Ref. [137]. Montgomery and Urban [118] used such concepts as data banks, model bank, statistical bank, man-machine interaction, evolutionary approach, etc. at the end of the 1960s. Gerrity [53] applied his man-machine decision system to portfolio management. Later, Little's [101] concept of decision calculus was a significant movement to apply normative marketing theories in supporting actual marketing decision making.

As Fig. 4 indicates it is necessary to return to organizational design in order to sharpen the organizational requirements and to increase the coordination between the levels. Also, iterative coordination between financial, production and marketing function may be needed. Possibly, the cycles may be repeated several times.

## 4.1.5. Implementation

Broadly defined, the whole design and development process of an ODSS can be regarded as an implementation process. From a narrower perspective, implementation is the phase in the design and development process of an organizational DSS where the normative designs are changed into an operative DSS. It is a mapping from the design context to the managerial context and it is the first part of the directed change.

![](/api/attachments/4627H9JB/fulltext/images/5762c55dc3a5a09ad8a0c54cbf06c4bb260621bb3056561d738a03eddcf61565.jpg)  
Fig. 5. Portfolio creation with different combinations of stocks [140].

In the design sub-phase the preliminary plans that the system should include are drawn concerning the models, databases, and user-interfaces. In the implementation sub-phase efforts are made to fulfil these requirements technically. The initiative for a DSS effort, a problem or an issue, comes from managers' reality, in the course of the development process emphasis may move to technological dimensions, but in the implementation sub-phase the point of view is again moved to managerial reality.

Example. As an example how theoretical knowledge can be implemented to an ODSS consider a case where modern portfolio theory [109] is applied to the choice of investment alternatives (projects) [83]. The original theory states that the expected return and standard deviation (risk) are the key dimensions of any investment problem and we should choose the alternative from the efficient frontier (Pareto set) of the alternatives as described in Fig. 5.

When implementing the theory, it is sometimes impossible to define the monetary return and standard deviations. However, the original theory is valuable and can be utilized when building an evaluation procedure according to the principles of AHP [134]. In Fig. 6 a potential hierarchy of goals and investment alternatives is presented.

If Expert Choice software is used to implement the AHP analysis, a variety of sensitivity analyses can be made. In Fig. 7 an example of such kind of analysis is given. One can easily find the conceptual analogy between the theory (Fig. 5) and its respective implementation (Fig. 7); projects 2, 6, 3, and 1 are Pareto-optimal and worth considering.

![](/api/attachments/4627H9JB/fulltext/images/0e221b19f0efb769968413aca0cefff70d3167c61abb52b5320edc02597b15d1.jpg)  
Fig. 6. The effect of the investment projects on the company's well-being.

The distinction between the design and implementation sub-phases is not clear and it may be necessary to return to the preliminary phases or sub-phases from the implementation sub-phase. Because implementation is a relative concept, generally, the degree of implementation is related to the degree of changes made. The direction of the change is determined during the preceding phases. Also, the whole implementation sub-phase can be based on sound theories. The theories serve the implementation sub-phase as a means of how to achieve the goals given in the previous phases. The relevant theories for the implementation sub-phase can be classified into four groups:

1. methodological theories;

2. implementation theories;

3. theories of organizational change;

4. theories of personal decision making.

Depending on the system type (see, e.g. Alter [8]), the relevant methodological theories can include statistical, computational, OR/MS, etc. theories. Sprague and Carlson [146] classify the DSS technology into three levels: specific DSS, DSS generators, and DSS tools. Consequently, the methodological theories can also have hierarchical relations.

The general implementation theories aim to explain or predict the success of an IS development effort. Two main streams of implementation theories can be distinguished: factor approach and process approach $[55,79,85,90,95,103,104]$ . For the management of the implementation sub-phase the normative implementation theories are of great value: they give explicit instructions how to proceed to achieve the goals $[55,85]$ . Actually, one class of these implementation theories is an approach based on organizational change theories. Change theories $[80,93,97,136]$ explain how an organizational change is achieved effectively. The implementation of an ODSS has, of course, broad and quite intricate organizational implications.

The different types of personal decision making theories and cognitive theories [71,128] emphasize that decision makers have different customs and styles of perceiving phenomena, searching for information, evaluating information and phenomena, using information, deducting, searching for solutions, and coping with uncertainty and a complex environment. The primary purpose of personal decision theories in the implementation phase is to highlight that the DSS is consistent with the decision styles of the decision makers.

![](/api/attachments/4627H9JB/fulltext/images/7ef06e281334ea05451d519605c94e05368c1b485bd0c80a8df236e90013e4d3.jpg)  
Fig. 7. Expected return and risk in Expert Choice output.

## 4.1.6. Use and maintenance

The second part of the directed change is the use of the ODSS. In the use sub-phase the developed DSS is utilized to support in solving the original problem, or rather, in the case of an ODSS, to support in solving and coordinating the original problems. If properly designed and implemented, the ODSS supports all phases of the decision process, and integrates the plans across organizational levels and functional borders.

The scope of the usage of the ODSS can vary widely. It can be used interactively on a regular basis to support functional or organizational budgeting or on an ad-hoc basis, to settle a specific problem. The developed system can be used for an analysis or a synthesis; the sub-problems can be solved in the light of the whole, or the whole can be solved in the light of the parts. Of course, the mode of usage depends on the technological implementation. File drawer systems, for example, can be used to provide data queries, representational models provide empirical relationships between key variables, accounting models can be used to perform what-if analyses, optimization models produce optimal solutions to the specified problem, etc.

The ODSS most often consists of several sub-models which can be used independently, or together with others. The common usage of the submodels can be simultaneous or recursive. The parts of the system can be used either by an individual decision maker or they can be used to support group decision making.

Evaluation of the system is always included, explicitly or implicitly, into the usage of a DSS. An ODSS can be evaluated by its elements or by the whole system. It can be evaluated from the point of view of a single user or from the holistic, organizational point of view. Not unexpectedly, a number of different measurement approaches have been used to evaluate the effects of a DSS [90,146,155].

After successive, long-standing usage, the position, or status, of the system will be, and should be, institutionalized as a key managerial instrument. Because the implementation of an ODSS is a costly and risky activity, efforts should be made to institutionalize its position. Institutionalization is the refreezing stage in an organizational change process in the course of which the developed system is integrated into the organization $[97,136]$ . Voluntary systems, like DSS, can be institutionalized only by successive usage; the user must feel satisfaction with the new system if the system is going to be accepted and institutionalized. The institutionalization process can be accelerated by user education, organizational arrangements, and by ongoing technological maintenance.

![](/api/attachments/4627H9JB/fulltext/images/ca20ab6e82cc3852885274017ac59b64d033b02938bdf600d4f7d722c6ef9452.jpg)  
Fig. 8. The Main Menu of the Logistic Support System.

A part of this sub-phase is maintenance and improvement. Especially, the DSS is changed according to experiences and the learning process. Maintenance is thus closely related to the system evolution during which we can return to any phase of the design and development process.

Also, the usage of the DSS can be based on managerial theories. First, if the system is developed by the theory-oriented approach, then the managerial theories are embedded in the system's structure and, of necessity, the usage sub-phase is theoretically well-founded, too. Second, with the theory-oriented DSS the users should always have access to the theoretical knowledge to support their decision making. Help systems and direct connections to scientific libraries possibly give theoretical support in the use phase.

Example. As an example, Fig. 8 describes the main menu of a corporatewide DSS. This particular system concentrates on the investment planning of the corporatewide logistics system [89].

As the main menu indicates, the whole support process is built around Simon's theory of decision making [144]. The user can proceed in the investment analysis or return to any previous phase just by touching on the icons on the screen. For example, in the investment design, the investment alternatives can be studied by the simulation model and in the choice phase the best alternative is chosen by the Analytic Hierarchy Process. All results obtained during any phase of the decision-making process can be collected to a standardized investment form or stored to an ordinal text file. Through the Help key it is possible to get the definitions of the key concepts, references to the books and articles of the area.

Example. As a detailed example how the system usage can be supported by substance theories, Fig. 9 describes an input window of the investment planning system. In the system a theoretical relationship between the return on equity and stock prices is defined. In the actual usage situation, however, the decision maker may not be satisfied with the relationship but wants to give (by mouse) his/her own approximation for the relationship. The theoretical relationship still supports the decision maker to shape his/her preferences.

![](/api/attachments/4627H9JB/fulltext/images/7fb4ee226f2d856cede9c7eafdf5cd2d84be659fb6034a10c91d816257170e3c.jpg)  
Fig. 9. An input window for evaluating the effect of ROE on stock prices.

## 4.1.7. Evolution

Perhaps the most essential difference between the development of a DSS and the other information systems (MIS, OR/MS models) lays in the attitudes towards the degree of system completeness. Traditional IS development activities tend to aim to the finished systems, products, which are then used and, in the long run, probably evolve. Decision Support Systems, on the other hand, are never meant to be complete systems but they are expected to be under continuous modification, expansion, and movement, that is, in a state of continuous evolution.

The second, but related, difference between the DSS and other forms of information systems is in the trade-off between the system and its environment. Traditional information systems are relatively easy to isolate from their environment but DSS are designed, developed, and they evolve with their environment. For example, the decision maker with his/her knowledge and the DSS may live in a near symbiosis with each other.

Actually, an ODSS can evolve in three fashions. First, as Fig. 4 indicates, an ODSS evolves during the development process before the system is truly “used”. Iterations are needed between and within the three main phases.

Second, an ODSS evolves toward an internal stability or system efficiency. Because the ODSS deal with semistructured or unstructured problems the initial versions of the system will prove to be incomplete. Therefore, the first iterations after dissatisfied experiences with the system aim to improve the system quality by filling the gap between expectations and achieved results. As Sprague and Carlson [146] put it: “After a short period of use (a few weeks), the system is evaluated, modified, and incrementally expanded. This cycle is repeated three to six times over the course of a few months until a relatively stable system is evolved which supports decision making for a cluster of tasks”. Generally, the theory-oriented approach may possibly decrease the number of iterations needed to reach the internal stability.

Third, a DSS evolves toward an external stability or system effectiveness. When the system has reached its internal stability, internal or external conditions can change and the system must adapt to the new conditions.

According to Ackoff [2], “a system is adaptive if, when there is a change in its environmental and/or internal state which reduces its efficiency in pursuing one or more of its goals which define its function(s), it reacts or responds by changing its own state and/or that of its environment so as to increase its efficiency with respect to that goal or goals”. Then Ackoff defines four types of system adaptation: Other–Other, Other–Self, Self–Other, and Self–Self adaptation. When this conceptual classification is applied to the DSS setting, we must remember the close relationship of a DSS to its environment.

The other-other adaptation of a DSS meditates the changes in external conditions to changed decisions. For example, when financial markets, production technologies, raw materials, product markets, or even managerial theories change, the DSS adapts by supporting decision making in the new situation. No change in the internal structure of a DSS is required. Within the other-self adaptation the changes in the external conditions lead to the internal change of the DSS. If the decision maker is assumed to belong to the environment of a DSS, then the evolution due to his learning represents these classes of adaptation. The self-evolving DSS, as proposed by Liang and Jones [98], where the DSS is aware of how it is used and then adapts to the evolution of its users, are extreme examples of the co-evolution of the user and the system.

In the self-other adaptation the environment of a DSS is changed by an internal stimulus. For example, if a new version of a DSS generator includes new methods for a decision analysis, then improved decisions can be made. In the self-self adaptation the structure of a DSS is changed by an internal stimulus. For example, if a new version of a DSS generator permits movement from record-oriented data files to data base management, it will cause significant changes to the whole structure of an organizational DSS. Generally, improvements in DSS tools will cause changes at higher technological levels.

Together the different types of adaptation emerge as a continuous process of evaluation, modification and expansion of system capabilities as well as in increasing capabilities of the decision maker due to the learning process. Also, the theory base will expand, and in the best case, new managerial theories are created during the iterative evolution $[25]$ .

## 4.2. Organizing the implementation process

In the sections above a procedure for the STO approach for implementing an ODSS is proposed. The effort for designing and developing an organizational, institutional DSS might seem to be an overwhelmingly extensive and complicated task. This is not necessarily the case, because the organizational, holistic system can be a relatively simple specialized system. However, the organization of the development effort certainly depends on the scope of the proposed system.

Implementation of a theory-oriented ODSS differs substantially from other DSS development efforts. First, “the development of an ODSS requires a formal, structured approach” [28]. Second, it is almost impossible for one person only to manage all elements of the whole system; coordination and assignment of the work among specialists from different functional areas are needed. The specialist knowledge of finance, production, and marketing should be integrated into an harmonious, holistic conception. Third, an organization probably does not possess enough theoretical knowledge to successfully complete the project. Thus, outside help is needed. Competent consultants with sufficient theoretical education from universities, or from consulting companies, will substantially reinforce the project team.

The responsibility for the efforts to develop an organizational, corporatewide ODSS is at the corporate level – at top management or the corporate planning department level immediately below the top management. Their primary duty is to allocate sufficient resources to the different phases of the development process.

The importance of the intermediary's role [146] is increased and partly changed in developing organizational, theory-oriented DSS. In addition to the fact that the intermediary “helps the user, perhaps merely as a clerical assistant, to push the buttons of the terminal, or perhaps as a more substantial staff assistant, to interact and make suggestions”, his role includes coordination between the different planning levels, and between the different functions, standardizing and connecting the sub-systems. In the extensive development efforts, it is perhaps necessary to nominate a special coordinator to play the role of a facilitator in order to perform these tasks effectively.

During the evolution process the different roles and the organization of the DSS group will change. Some roles, like toolsmiths, may become unnecessary and the characteristics of the other roles may change. Especially, the role of the decision maker (user) will change: the manager becomes the iterative designer of the system. Only he/she is responsible for the further development of the system.

## 5. Discussion and conclusions

In this conceptual research the Substance-Theory-Oriented approach to the implementation of an organizational DSS is proposed. We believe that greater attention to substance theories will help to decide the content of an organizational DSS. Although the DSS literature offers a number of good cases where the theoretical knowledge concerning the specific decision area is utilized, these cases have generally been applied only to support a narrow, specific decision task encountered by a single decision maker. No cohesive, substance-oriented method has been proposed to manage the design and development of the ODSS. One purpose of this paper is to serve as a counterbalance to the numerous technology-oriented methods as well as to those methodologies that are grounded on the general decision-making theories.

Methodologically, although the proposed approach has adopted Stabell's decision-oriented approach as the starting point and extended it by the features of corporate models, it still has some characteristics of traditional DSS development procedures: the final system evolves through tentative, prototype systems and the focus is to support decision making, not to replace it.

The adopted substance conceptualization and the proposed methodology have some significant contributions. First, the current decision-making behaviour in the organization or the technological possibilities do not determine the content of the planned system but the developed systems are based on the best knowledge of the substance area. The present approaches to DSS design and development center on the techniques and the most relevant managerial issues get pushed aside. The proposed Substance-Theory-Oriented approach, on the contrary, is linked to descriptive and prescriptive managerial theories. Also, all phases of the development process are supported by the appropriate managerial theories, not only a particular phase of the process.

Second, the described procedure has an integrative perspective. It integrates the different activities of the implementation process, different theories, and different functions and levels of the organization. Especially, a logical chain between the descriptive analysis and normative design is established. Normative managerial theories are needed to join descriptive analysis and normative design. Without the normative theories the analysis and design phases remain conceptually distinct and practically confused.

Third, the adapted holistic, organizational strategy facilitates synergy effects. Managing larger organizational systems and understanding the direct and indirect effects of decisions over an organization are motives to develop ODSS instead of functional DSS and, thus, motives for this research. “The whole is more than the sum of its parts”.

A problem of the approach is the difficulty to join the pluralistic practice and uniform theories together.

Also, sometimes it might be difficult to find the best theories suitable to a specific situation from the extensive set of competing theories. Another difficulty is to integrate the advice given by specific theories to form a coherent, organizational DSS.

The STO approach described above has been successfully applied in some actual DSS development projects. Due to the available space and because the projects are described elsewhere $[83,86–89]$ they are not discussed here. The projects include a system to support corporatewide budgeting decisions, a system for logistic management, a system for holistic investment and pricing decisions, and a system for a small wholesale company to support financial and inventory decisions. Generally, if properly used, the proposed methodology is a management-development rather than solely a DSS-development approach; emphasis is moved from DSS technology to managerial methodology. DSS are seen in the wider managerial context and the design and development criteria are established on managerial substance theories.

In the future, the methodological principles described in this paper have to be transformed into practical procedures and working instructions. For practical purposes the guiding procedures can be compiled in a book or even in an expert system to support the implementation process of the ODSS. Such kind of general ES would help to analyze the present situation, to find relevant theories, to chose proper technology, etc.

In the future research, relevant theories need to be searched, evaluated, and applied. Also, the integration of single theories in the organization-wide systems is not a trivial task. The described methodology needs to be sharpened for different classes of ODSS: data- and model-oriented systems, systems for small and large companies, systems at different industries, etc. The developed systems, their organizational and individual effects, and the actual role of theories must be carefully assessed. If unsuccessful cases appear, as they certainly will, it is important to know whether the reason lies in wrong theories or in their wrong adoption. This is the only way to convince the value of the approach.

Partly, the issue of a design and development method is the question of language and concepts used in the development process. In this paper we argue that managerial substance theories, instead of DSS technology, should be the “native” language of DSS design and development. There should be a much closer relationship between management theories and DSS development than is the case at present. If evaluated on the basis of those cases thus far implemented, the approach has shown remarkably good results.

## Acknowledgements

I would like to thank the editor-in-chief of the journal and the two anonymous referees for their insightful comments and suggestions.

## References

[1] W.J. Abernathy, P.L. Townsend, Technology, policy, and process changes, Technological Forecasting and Social Change 7 (4) (1975) 379–396.

[2] R.L. Ackoff, Towards a system of systems concepts, Management Science 17 (11) (1971) 661–671.

[3] C. Adams, M. Eierman, F. Niederman, The development of DSS research: a descriptive and prescriptive view, Working Paper Series MISRC-WP-90-06, University of Minnesota, February 1990.

[4] C. Adams, F. Niederman, Towards a theory of DSS design, Working Paper Series MISRC-WP-91-03, University of Minnesota, September 1990.

[5] A.K. Aggarwal, R. Mirani, Macro issues in the development of organizational Decision Support Systems, in: Proceedings of the 28th Annual Hawaii International Conference on Systems Sciences, IEEE Computer Society Press, Silver Spring, MD, 1995, pp. 917–926.

[6] M. Alavi, J.C. Henderson, An evolutionary strategy for implementing a Decision Support System, Management Science 27 (11) (1981) 1309–1323.

[7] M. Alavi, H.A. Napier, An experiment in applying the adaptive design approach to DSS development, Information and Management 7 (1) (1984) 21–28.

[8] S. Alter, A study of computer aided decision making in organizations, Ph.D. Dissertation, Massachusetts Institute of Technology, 1975.

[9] S. Alter, Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading, MA, 1979.

[10] L.R. Amey, Budget Planning and Control Systems, Pitman, London, 1979.

[11] R.N. Anthony, Planning and Control Systems: A Framework for Analysis, Cambridge University Press. Cambridge, MA, 1965.

[12] L.M. Applegate, T.T. Cheng, B.R. Konsynski, J.F. Nuna-

maker, Knowledge management in organizational planning, Journal of Management Information Systems, 3 (4), Spring (1987) 5–6.

[13] G. Ariav, M.J. Ginzberg, DSS design: a systemic view of decision support, Communications of the ACM 28 (10) (1985) 1045–1052.

[14] B. Arinze, A contingency model of DSS development methodology, Journal of Management Information Systems 8 (1) (1991) 149–166.

[15] B. Arinze, Decision Support Systems (DSS) development using a model of user inquiry types: methodological proposals and a case study, Systems Practice 5 (6) (1992) 629–650.

[16] S. Ba, A.B. Whinston, K.R. Lang, An enterprise modelling approach to organizational decision support, in: J.F. Nunamaker, Jr., R.H. Sprague, Jr., (Eds) Proceedings of the 28th Hawaii International Conference on Systems Sciences, vol. III, 1995, pp. 312–320.

[17] J.E. Bailey, S.W. Pearson, Development of a tool for measuring and analyzing computer user satisfaction, Management Science 29 (5) (1983) 519–529.

[18] R. Bartels., The general theory of marketing, Journal of Marketing 32 (1968) 29–33.

[19] A. Belkaoui, Accounting Theory, Harcourt, Brace and Jovanovich, New York, 1985.

[20] J.L. Bennet, Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983.

[21] J.R. Bettman, An Information Processing Theory of Consumer Choice, Addison-Wesley, Reading, MA, 1979.

[22] H. Bidgoli, Decision Support Systems – Principles and Practice, West, St. Paul, 1989.

[23] J. Bradley, Introduction to Data Base Management in Business, Holt, Rinehart & Winston, 1987.

[24] E.D. Carlson, An approach for designing decision support systems, in: J.L. Bennet: Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 15–39.

[25] C. Carlson, New Instruments for Management Research, Human Systems Management 10 (3) (1991) 203–220.

[26] C. Carlson, R. Östermark, Interactive heuristics vs. optimization as planning strategies, in: R. Kulikowski (Ed.), Methodology and Applications of Decision Support Systems, Polaska Akademia, Warszawa, 1989.

[27] E.G. Carmines, R.A. Zeller, Reliability and Validity Assessment, SAGE Publications, Beverley Hills, CA, 1979.

[28] G.M. Carter, M.P. Murray, R.G. Walker, W.E. Walker, Building Organizational Decision Support Systems, Academic Press, New York, 1992.

[29] E.F. Codd, Relational completeness of data base sublanguage, in: Data Base Systems, Prentice-Hall, Englewood Cliffs, NJ, 1972.

[30] R.M. Cyert, J.G. March, A Behavioral Theory of the Firm, Basil Blackwell, Oxford, 1992.

[31] G.B. Davis, Strategies for information requirements determination, IBM Systems Journal 21 (1) (1982) 4–30.

[32] F.D. Davis, Perceived usefulness, perceived ease of use, and user acceptance of information technology, MIS Quarterly 13 (3) (1989) 319–339.

[33] A. Deaton, J. Muellbauer, Economics and Consumer Behaviour, Cambridge University Press, Cambridge, 1989.

[34] D. Dery, Problem Definition in Policy Analysis, University Press of Kansas, Lawrence, KS, 1984.

[35] G. Desanctis, R.B. Gallupe, A foundation for the study of Group Decision Support Systems, Management Science 33(5) (1987) 589–609.

[36] G. Desanctis, B. Gallupe, Computer-based support for group problem-finding: an experimental investigation, MIS Quarterly 12 (2) (1988) 277–295.

[37] A. Dogramaci, R. Fare, Applications of Modern Production Theory: Efficiency and Productivity, Kluwer Academic Publishers, Dordrecht, 1988.

[38] R.D. Dolk, M. Ackroyd, Enterprise modeling and object technology, in: Proceedings of the Third International Conference on Decision Support Systems, vol.1, Hong Kong, 1995, pp. 235–245.

[39] J.J. Donovan, S.E. Madnick, Institutional and ad-hoc decision support systems and their effective use, Data Base 8(3) (1977) 79–88.

[40] C. Drury, Management and Cost Accounting, Van Nostrand Reinhold International, London, 1988.

[41] J. Dyer, P.C. Fishburn, R.E. Steuer, J. Wallenius, S. Zionts, Multiple criteria decision making, multiattribute utility theory: the next ten years, Management Science 38 (5) (1992) 645–654.

[42] A.I. El-Ansary, The general theory of marketing revised, in: O.C. Ferrell, S.W. Brown, C.W. Lamb, Jr., Conceptual and Theoretical Developments in Marketing, 1979, pp. 399–407.

[43] O.A. El Sawy, H.E. Sherif, Issue-based decision support systems for the Egyptian cabinet, MIS Quarterly 12 (4) (1988) 551–569.

[44] J.C. Emery, Organizational Planning and Control Systems, Theory and Technology, Macmillan, New York, 1969.

[45] H.B. Eom, The emergence of global decision support systems, OR/MS Today, October (1990) 12–13.

[46] H.B. Eom, S.M. Lee, A survey of Decision Support System applications (1971–April 1988), Interfaces 20 (3) (1990) 65–79.

[47] J.G. Forrester, Industrial Dynamics, Wiley, New York, 1961.

[48] R. Frisch, Theory of Production, Reidel, Dordrecht, 1965.

[49] R. Färe, Fundamentals of Production Theory, Springer, Berlin, 1988.

[50] C. Garnto, H.J. Watson, An investigation of data base requirements for institutional and ad hoc DSS, Data Base, Summer (1985) 3–9.

[51] J.F. George, Organizational Decision Support Systems, Journal of Management Information Systems Quarterly 8(3) (1991–1992) 109–127.

[52] J.F. George, J.F. Nunamaker, J.S. Valacich, ODSS: Information technology for organizational change, Decision Support Systems 8 (4) (1992) 307–314.

[53] J.R.T.P. Gerrity, The design of man-machine decision systems: application to portfolio management, Sloan Management Review 12 (2) (1971) 59–75.

[54] J.P. van Gigch, Applied General Systems Theory, Harper & Row, New York, 1974.

[55] M.J. Ginzberg, A process approach to management science implementation, Ph.D. dissertation, Massachusetts Institute of Technology, 1975.

[56] M.J. Ginzberg, G. Ariav, Methodologies for DSS analysis and design: a contingency approach to their application, in: L. Maggi, R. Zmud, J. Wetherbe (Eds.): Proceedings of the Seventh International Conference on Information Systems, San Diego, CA, 1986, pp. 46–56.

[57] P. Gray, L. Olfman, The user interface in-group decision support systems, Decision Support Systems 5 (2) (1989) 119–137.

[58] L.E. Greiner, Evolution and revolution as organizations grow, Harvard Business Review 50 (4) (1972) 37–46.

[59] P.H. Grinyer, J. Wooller, Corporate models today, Institute of Chartered Accountants in England and Wales, 1978.

[60] J.L. Hammond, J.P. O'Reilly, Performance Analysis of Local Computer Networks, Addison-Wesley, Reading, MA, 1988.

[61] J.S. Hammond III, Do's and dont's of computer models for planning, Harvard Business Review 52 (3) (1974) 110–123.

[62] P. Harmon, R. Maus, W. Morrissey, Expert Systems Tools and Applications, Wiley, New York, 1988.

[63] M. Harris, A. Raviv, The theory of capital structure, Journal of Finance 46 (1) (1991) 297–355.

[64] R.A. Haugen, Modern Investment Theory, Prentice-Hall, Englewood Cliffs, NJ, 1986.

[65] R.L. Hayen, How to design a financial planning model, Long Range Planning 16 (5) (1983) 111–122.

[66] A.F. Herbst, Capital Budgeting - Theory, Quantitative Methods, and Applications, Harper & Row, New York, 1982.

[67] T. Hirouchi, T. Kosaka, An effective database formation of Decision Support Systems, Information Management 8 (1984) 183–195.

[68] J.T. Hogue, H.J. Watson, Current practices in the development of Decision Support Systems, in L. Maggi, J.L. King, K.L. Kraemer (Eds.), Proceedings of the Fifth International Conference on Information Systems, Tucson, AZ, 1983, pp. 117–127.

[69] C.W. Holsapple, A.B. Whinston, Business Expert Systems, Richard D. Irwin, Homewood, IL, 1987.

[70] J. Howard, J.N. Sheth, The Theory of Buyer Behaviour, Wiley, 1969.

[71] G.P. Huber, Cognitive style as a basis for designing MIS and DSS: much ado about nothing?, Management Science 29 (5) (1983) 567–579.

[72] E.G. Hurst, D.N. Ness, T.J. Gambino, T.H. Johnson, Growing DSS: A flexible evolutionary approach, in: J.L. Bennet, Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 111–132.

[73] B. Ives, M.H. Olson, J.J. Barroudi, The measurement of user information satisfaction, Communications of the ACM 26 (10) (1983) 785–793.

[74] S.L. Järvenpää, The effect of task demands and graphical

format on information processing strategies, Management Science 35 (3) (1989) 285–303.

[75] F.E. Kast and J.E. Rosenzweig, Organization and Management: A Systems and Contingency Approach, McGraw-Hill, New York, 1985.

[76] R.J. Kauffman, P. Weill, An evaluative framework for research on the performance effects of information technology investments, in: Proceedings of the Tenth International Conference on Information Systems, December 4–6, 1989, Boston, MA, pp. 377–388.

[77] R. Kaula, U.R. Dumdum, Towards an organization DSS architecture: an open-systems perspective, in: I. Zigurs (Ed.), DSS-91 Transactions, Eleventh International Conference on Decision Support Systems, Manhattan Beach, CA, 1991, pp. 168–176.

[78] P.G.W. Keen, Adaptive design for Decision Support Systems, Data Base 12 (1–2) (1980) 15–25.

[79] P.G.W. Keen, Implementation research in OR/MS and MIS: description versus prescription, Research Paper No. 390, Graduate School of Business, Stanford University, 1977.

[80] P.G.W. Keen, Information systems and organizational change, Communications of the ACM 24 (1) (1981) 24–33.

[81] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[82] G.W. Keen, T.J. Gambino, Building a Decision Support System: the mythical man-man revisited, in: J.L. Bennet, Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 133–172.

[83] O. Keski-Äijö, H. Kivijärvi, M. Tuominen, Decision support for managing intangible investments – a two-phased approach, Research Report No. 90, Lappeenranta University of Technology, 1996.

[84] J. Kimberly, R. Miles, The Organizational Life Cycle, Jossey-Bass, San Francisco, CA, 1980.

[85] H. Kivijärvi, Implementing model-oriented decision support systems, Series A:53, The Helsinki School of Economics, Helsinki, 1987.

[86] H. Kivijärvi, M. Kuula, An experiment of applying some substance-theories on the design and development of a corporatewide DSS in a small company, Working Paper W-24, Helsinki School of Economics and Business Administration, 1992.

[87] H. Kivijärvi, M. Soismaa, Investment and pricing strategies of competing firms: a computational approach, Managerial and Decision Economics 13 (2) (1992) 371–387.

[88] H. Kivijärvi, M. Soismaa, Investment and harvest strategies of the Finnish forest sector under different forest-tax policies: a differential game approach with a computer-based decision aid, European Journal of Operational Research 56(2) (1992) 192–209.

[89] H. Kivijärvi, M. Tuominen, A Decision Support System for semistructured strategic decisions: a multi-tool method for evaluating of intangible investments, Journal of Decision Systems 1 (4) (1992) 253–276.

[90] H. Kivijärvi, R. Zmud, DSS implementation activities, problem domain characteristics and DSS success, European Journal of Information Systems 2 (3) (1993) 159–168.

[91] J.P.C. Kleijnen, Computers and Profits, Addison-Wesley, Reading, MA, 1980.

[92] M. Klein, L.B. Methlie, Knowledge-based Decision Support Systems, with Applications in Business, Wiley, 1995.

[93] D.A. Kolb, A.L. Frohman, An organization development approach to consulting, Sloan Management Review 12 (1) (1970) 51–65.

[94] D.M. Kreps, Notes on the Theory of Choice, Westview Press, Boulder, CO, 1988.

[95] T.H. Kwon, R.W. Zmud, Unifying the fragmented models of information systems implementation, in: J.R. Boland, R. Hirscheim (Eds.), Critical Issues in Information Systems Research, Wiley, New York, 1987, pp. 227–251.

[96] H. Levy, M. Sarnat, Capital Investment and Financial Decisions, Prentice-Hall, Englewood Cliffs, NJ, 1990.

[97] K. Lewin, Group decision and social change, in: G.E. Swanson, T.M. Newcomb and E.L. Hartley (Eds.), Readings in Social Psychology, Holt, Rhinehart & Winston, New York, 1952, pp. 197–211.

[98] T.P. Liang, C.V. Jones, Design of a self-evolving decision support system, Journal of Management Information Systems 4 (1) (1987) 59–82.

[99] B.C.J. Lievegoed, The Developing Organization, Tavistock, London, 1973.

[100] G.L. Lilien, P. Kotler, Marketing Decision Making - A Model-building Approach, Harper & Row, New York, 1983.

[101] J.D.C. Little, Models and managers: the concept of a decision calculus, Management Science 16 (8) (1970) 466–485.

[102] H.C. Lucas, The Analysis, Design and Implementation of Information Systems, 3rd ed., McGraw-Hill, New York, 1985.

[103] H.C. Lucas, Implementation – The Key to Successful Information Systems, Columbia University Press, New York, 1981.

[104] H.C. Lucas, M.J. Ginzberg, R.L. Schultz, Information Systems Implementation: Testing a Structural Model, Ablex, Norwood, NJ, 1990.

[105] R.I. Mann, H.J. Watson, P.H. Cheney, C.A. Gallagher, Accommodating cognitive style through DSS hardware and software, in: Proceedings from the 19th Hawaii International Conference on Systems Science, 1986.

[106] J.G. March, Decisions and Organizations, Basil Blackwell, Oxford, 1988.

[107] J.G. March, H.A. Simon, Organizations, Blackwell, Cambridge, MA, 1993.

[108] J. Marschak, Economics of Information Systems. Journal of the American Statistical Association 66 (333) (1971) 192–218.

[109] H. Markowitz, Portfolio Selection: Efficient Diversification of Investments, Wiley, New York, 1959.

[110] J. Martin, Computer Networks and Distributed Processing, Prentice-Hall, Englewood Cliffs, NJ, 1981.

[111] Y. Masuda, The Information Society as Post-Industrial Society, World Future Society, Bethesda, MD, 1981.

[112] C. McCoff, A. Hunt, D. Vogel, J. Nunamaker, IBM's experiences with groupsystems, Interfaces 20 (6) (1990) 39–52.

[113] M.H. McCormac, What They Don't Teach You at Harvard Business School, Bantam Books, New York, 1986.

[114] C.L. Meador, M.J. Guyote, W.L. Rosenfeld, Decision support planning and analysis: the problems of getting large scale DSS started, MIS Quarterly 10 (2) (1986) 159–177.

[115] C.L. Meador, M.J. Guyote, P.G.W. Geen, Setting priorities for DSS development, MIS Quarterly 8 (2) (1984) 117–129.

[116] M.D. Mesarovic, D. Macko, Y. Takahara, Theory of Hierarchical, Multilevel Systems, Academic Press, New York, 1970.

[117] H. Mintzberg, The Nature of Managerial Work, Prentice-Hall, Englewood Cliffs, NJ, 1980.

[118] D.B. Montgomery, G.L. Urban, Management Science in Marketing, Prentice-Hall, Englewood Cliffs, NJ, 1969.

[119] J.H. Moore, M.G. Chang, Meta-design considerations in building DSS, in: J.L. Bennet: Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 173–204.

[120] T.H. Naylor, Corporate Planning Models, Addison-Wesley, Reading, MA, 1979.

[121] T.H. Naylor, Decision Support Systems or whatever happened to M.I.S.?, Interfaces 12 (4) (1982) 92–94.

[122] W. Nicholson, Intermediate Microeconomics and Its Application, Dryden Press, Chicago, IL, 1987.

[123] S.R. Nidomolu, Interorganizational information systems and the structure and climate of seller-buyer relationships, Information and Management 28 (1995) 89–105.

[124] R.L. Nolan, Managing the crises in data processing, Harvard Business Review 57 (2) (1979) 115–126.

[125] P.C. Nutt, Types of organizational decision processes, Administrative Science Quarterly 29 (3) (1984) 414–450.

[126] A.S. Philippakis, G.I. Green, An architecture for organization-wide Decision Support Systems, in: Proceedings of the Ninth International Conference on Information Systems, Minnesota, 1988.

[127] M.E. Porter, Competitive Advantage: Creating and Sustaining Superior Performance, Free Press, New York, 1985.

[128] A. Ramaprasad, Cognitive process as a basis for MIS and DSS design, Management Science 33 (2) (1987) 139–148.

[129] F. Riggins, T. Mukhopadhyay, Interdependent benefits from interorganizational systems: opportunities for business partner reengineering, Journal of Management Information Systems 11 (2) (1994) 37–57.

[130] D. Robey, Cognitive style and DSS design: a comment on Huber's paper, Management Science 29 (5) (1983) 580–582.

[131] J.F. Rockart, D.W. Delong, Executive Support Systems, Dow Jones-Irwin, Homewood, IL, 1988.

[132] F. Rosenkranz, An Introduction to Corporate Modeling, Duke University Press, 1979.

[133] S. Ross, The economic theory of agency: the principal's problem, American Economic Review LXII (2) (1973) 134–139.

[134] T.L. Saaty, The Analytic Hierarchy Process, McGraw-Hill, New York, 1980.

[135] V.L. Sauter, J.L. Schofer, Evolutionary development of Decision Support Systems: important issues for early phases of design, Journal of Management Informations Systems 4(4) (1988) 77–92.

[136] E.H. Schein, Management development as a process of influence, Industrial Management Review 2 (2) (1961) 59–77.

[137] M.S. Scott Morton, Management Decision Systems, Harvard University Press, Boston, MA, 1971.

[138] J.R. Searle, How to derive “ought” from “is”, Philosophical Review 73 (1964) 43–58.

[139] B. Shane, M. Fry, R. Toro, The design of an investment portfolio DSS using two Expert Systems as a consulting system, Journal of Management Information Systems, 3 (4) Spring (1987) 13–14.

[140] A.C. Shapiro, Modern Corporate Finance, Macmillan, New York, 1991.

[141] J.N. Sheth, D.M. Gardner, D.E. Garrett, Marketing Theory: Evolution and Evaluation, Wiley, New York, 1988.

[142] B. Schneiderman, Designing the user interface – strategies for effective human-computer interaction, Addison-Wesley, Reading, MA, 1987.

[143] M.S. Silver, Systems that Support Decision Makers, Wiley, New York, 1991.

[144] H. Simon, The New Science of Management Decision, Harper & Row, New York, 1960.

[145] G.F. Smith, Defining managerial problems: a framework for prescriptive theorizing, Management Science 35 (8) (1989) 963–981.

[146] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice-Hall, Englewood Cliffs, NJ, 1982.

[147] C.B. Stabell, A decision-oriented approach to building DSS, in: J.L. Bennet: Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 211–260.

[148] C.B. Stabell, A decision research-based approach to DSS development, Working Paper 1988/13, Norwegian School of Management.

[149] R.J. Thierauf, Executive Information Systems: A Guide for Senior Management and MIS Professionals, Quorum Books. Greenwood Press, Westport, CT, 1991.

[150] E. Turban, Decision Support and Expert Systems, Prentice-Hall International, Englewood Cliffs, NJ, 1995.

[151] J.G. Walls, G.R. Widmeyer, O.A. El Sawy, Building an information systems design theory for vigilant EIS, Information Systems Research 3 (1) (1992) 36–59.

[152] R.L. Watts, J.L. Zimmerman, Positive accounting theory: a ten year perspective, The Accounting Review, January (1990) 131–156.

[153] P. Weill, M.H. Olson, Managing investment in information technology: mini case examples and implications, MIS Quarterly 13 (1) (1989) 3–17.

[154] G.A. Welsch, Budgeting: Profit Planning and Control, Prentice-Hall, Englewood Cliffs, NJ, 1976.

[155] G.M. Welsch, The information transfer specialist in successful implementation of Decision Support Systems. Data Base 18 (1) (1986) 32–40.

[156] R. Wilson, The theory of syndicates, Econometrica 36 (1968) 119–132.

[157] D.J. White, A bibliography on the applications of mathematical programming multiple-objective methods, Journal of the Operational Research Society 41 (8) (1990) 669–691.

[158] J. Von Neumann, O. Morgenstern, Theory of Games and Economic Behavior, Princeton University Press, Princeton, NJ, 1972 (original work published 1944).

[159] R.W. Zmud, Information Systems in Organizations, Scott, Foresman, Glenview, IL, 1983.

![](/api/attachments/4627H9JB/fulltext/images/a28c74c5d60c21dd7876bd75b32485788cce1f419cb9416f84d65b6e9c61415f.jpg)

Hannu Kivijärvi is an associate professor in Information Systems Science at the Helsinki School of Economics and Business Administration. He received his M.Sc. in 1977 and a Ph.D. in 1987 in management systems. His research interests include decision support systems in financial, production and marketing planning, implementation of information systems, and investments in information systems. His publications have appeared in a number of journals, including European Journal of Information Systems, European Journal of Operational Research, Managerial and Decision Economics, International Journal of Production Economics, and Interfaces.
