---
otero_id: 24180
otero_key: "MRBJ5XD4"
title: "OFFICETECH®: a new paradigm in office services?"
authors: "Susan J. Winter, T. Grandon Gill"
year: "2001"
journal: "Journal of Information Technology"
doi: "10.1080/02683960122282"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Implementing enterprise resource planning packages in different corporate and national cultures

M. KRUMBHOLZ, J. GALLIERS, N. COULIANOS

AND N.A.M. MAIDEN

Centre for Human–Computer Interaction Design, City University, Northampton Square, London EC1V 0HB, UK

ERP (enterprise resource planning) packages provide generic off-the-shelf business and software solutions for customers. However, these packages are implemented in companies with different corporate and national cultures and there is growing evidence that failure to adapt ERP packages to  t these cultures leads to projects which are expensive and overdue. This paper describes research which synthesizes social science theories of culture in order to be able to model and predict the impact of culture on ERP package implementation. It describes a knowledge meta-schema for modelling the surface and deeper manifestation of culture and predictions of ERP implementation problems based on national culture differences. It report on an empirical study into the implementation of ERP packages in a large pharmaceuticals organization in Scandinavia and the UK. The results provide evidence for an association between corporate culture and ERP implementation problems but no direct evidence for an association between national culture and implementation problems. Furthermore, the results demonstrate that these diverse implementation problems can be caused by a mismatch between a small set of core values which are indicative of a customer’s corporate culture. The paper concludes with revisions to the design of our extended method for ERP package implementation to the design of the meta-model and to rules that codify culture constraints that are applied in order to analyse instances of the meta-model.

## The impact of culture on ERP implementation

A recent Standish Group report on enterprise resource planning (ERP) implementation projects reveals that these projects were, on average, 178% over budget, took 2.5 times as long as intended and delivered only 30% of promised bene t, while another recent survey of 12 recent projects revealed that adapting the implementation to the prevailing cultural style was one important cause of this project underperformance (Densley, 1999). These  ndings support anecdotal evidence for the impact of culture which has been reported in the information technology (IT) press (e.g. Warren, 1999). This importance of culture is hardly surprising. A customer who implements an ERP package has to change their business processes to the ERP supplier’s best-practice processes (Curran and Ladd, 1998). The change both impacts on the customer’s corporate culture (i.e. the ways that things are done in the organization) and is constrained by it. The picture is even more complex in Europe because companies also have diverse national cultures which in uence this corporate culture and make the successful implementation of multinational ERP implementations dif cult, as reported in Gulla and

Mollan (1999). Indeed, evidence suggests that ERP implementations in North America have been more effective because of the more complex European corporate and national cultures (Warren, 1999). If more ERP implementations are to deliver their promised bene ts within budget, we need to understand how corporate and national cultures impact on ERP implementations and how this understanding will deliver better methods for implementation partners and customers to use.

In contrast to the lack of research in computer science, social and management science have researched the in uence of corporate and national cultures on organizational behaviour. Unfortunately, this research neither addresses issues that are speci c to information systems (IS) development, nor does it have a tradition of the model-theoretic approaches which are familiar in IS research for describing and predicting problems and their solutions. If we are to implement ERP solutions which recognize corporate and national cultures, we at least need to model culture in order to describe and pre dict its impact on ERP implementation.

This paper reports on the synthesis of a meta-model of culture from social and management science theories of corporate (Schein, 1992) and national (Trompenaars, 1994) cultures. It also reports on the extension of this modelling approach to existing ERP implementation methods such as ASAP – (Accelerated SAP) is $\mathrm { s A P } ^ { \bullet } \mathbf { s }$ comprehensive implementation solution for streamlining R/3 projects – (Curran and Ladd, 1998) in order to enable implementation teams to infer the important properties of national and corporate cultures and thereby provide a theoretically grounded checklist of culture issues that might in uence these implementations. Our own studies of current ERP implementations (Krumbholz and Maiden, 2000) have identi ed three different types of culture-related clash that this paper predicts might in uence ERP implementations (predictions 1–3).

$\mathrm { P _ { 1 } } \mathrm { : }$ The current corporate culture clashes with the future culture that is planned.

$\mathbf { P } _ { 2 } \colon$ The supplier’s culture, which is implicit in the ERP package, clashes with the customer’s corporate culture.

$\mathrm { P } _ { 3 } \mathrm { : }$ The new business processes (con gured using the ERP solution) clash with the existing corporate culture.

The studies reported in this paper will explore these predictions and we will return to them at the end of the paper.

One consequence of the existence of these three types of culture clash is that, in order to handle culture, the implementation team will need to model (1) the customer’s business processes and solution systems, (2) the characteristics of the corporate and national cultures that impact on the implementation of these business processes and (3) how these facets of corporate and national cultures impact on the business and software solutions. Implementation teams will use current ERP modelling approaches (Curran and Ladd, 1998) to model current and future business processes, then extend these models using the meta-model of culture in order to model the important characteristics of the customer’s corporate and national cultures. The team will then analyse these extended models in order to infer potential problems from the differences between the two business process models using rules that codify the synthesized theories of corporate and national cultures. However, in order to deliver such a method, it is  rst necessary to synthesize new theories of culture and understand better the types of culturerelated clashes $( \mathrm { P } _ { 1 } \mathrm { - } \mathrm { P } _ { 3 } )$ that occur during ERP implementations.

The method is outlined in Figure 1. This paper reports on research that investigates how corporate and national cultures cause ERP implementation problems using the meta-model and predictions from social and management science research.

The remainder of this paper is presented in  ve sections. The next section summarizes existing social science theories of culture, the third section presents the  rst-draft model of culture and the fourth section reports on empirical studies into the implementation of the same ERP package in the UK and Scandinavian subsidiaries of a large European pharmaceutical organization. The  fth section describes the results from these empirical studies and the paper ends with a discussion of the results relevant to our predictions, implications for the meta-model of culture and future research plans.

![](/api/attachments/MRBJ5XD4/fulltext/images/c1d8a83dfb34ec663d5b83a14d07e5ea078935a2f76537348760e6487b2f118e.jpg)  
Figure 1 An outline of the extended ERP implementation model for culture-sensitive ERP implementation

## Social and management science research on corporate and national cultures

Most social and management science research on culture can be divided into two camps (Dobson et al. 1993). The  rst camp claims that culture is something tacit which arises naturally. The other, more common view is that culture is something explicit which arises from social interaction. Social and management science research also divides research into national cultures, business cultures and corporate cultures. A good starting point is Schein (1992) who provided the following de nition of corporate culture.

a pattern of basic assumptions – invented, discovered or developed by a given group as it learns to cope with its problems of external adaptation and internal integration – that has worked well enough to be considered valid and therefore to be taught to new members as the correct way to perceive, think and feel in relation to those problems (p. 12).

He argued that corporate culture can be divided into three layers. In the outer layer there are values, which are written down statements about the strategies, missions and objectives of the organization. In the middle layer there are beliefs, which are the issues that the employees of an organization talk about. In the inner layer there are the ‘taken for granted’ assumptions which are those aspects of organizational life which people  nd dif cult to recall and explain. Schein (1992) also described ten dimensions that he used for differentiating between corporate cultures in different organizations. These are (1) the observed behavioural regularities of human interaction, (2) the group norms, (3) the espoused corporate values, (4) the formal philosophy, (5) the rules of the game, (6) the climate, (7) the habits of thinking, (8) people’s mental models and/or linguistic paradigms, (9) their shared meanings, (10) their embedded skills and (11) the organization’s root metaphors’ or integration symbols. These dimensions indicate the important classes and attributes of culture to model in order to improve our understanding of culture’s impact on ERP implementation.

Hofstede (1994) also investigated corporate and national cultures. He argued that there are four manifestations of culture and that the differences between national and corporate cultures are due to these different manifestations. He also placed these manifestations in layers similar to those of Schein (1992). Hofstede (1994) differentiated between layers that have symbols which represent the most super cial culture often described as practice, layers which have values which represent the deepest manifestations of culture and intermediate layers which describe heroes and rituals indicative of the corporate culture. He claimed that national culture differences reside more in values and less in practices and that organizational culture differences reside more in practices and less in values. Furthermore, he claimed that we can detect national and corporate culture differences using a set of dimensions similar to those of Schein (1992). Derived from extensive empirical studies, Hofstede (1994) provided four dimensions which differentiate between national cultures: power distance, individualism– collectivism, masculinity–femininity and uncertainty avoidance (Hofstede, 1994). Likewise, he also detected six dimensions for differentiating between organizational cultures: process versus results oriented, employee versus job oriented, parochial versus professional dependent, open versus closed systems of communication, loose versus tight control and normative versus pragmatic organizations (Hofstede, 1994). As with Schein’s (1992)  ndings, Hofstede’s (1994) dimensions indicate the important elements of culture to model in order to improve our understanding of culture’s impact on ERP implementation.

Trompenaars (1994) argued that national culture can be described by three layers similar to those of Hofstede (1994). A central theme of Trompenaar’s (1994) argument is that people organize themselves in such a way as to increase the effectiveness of their problem-solving processes and, thus, have formed different sets of implicit logical assumptions in order to enable this to happen. Each culture distinguishes itself from others in terms of its solutions to these problems. These problems can also be classi ed in order to differentiate between national cultures in a similar way to that which Hofstede (1994) used for his six dimensions. These classes are how people relate to each other (subdivided into universalism versus particularism, individualism versus collectivism, neutral versus emotional, speci c versus diffuse and achievement versus ascription), people’s attitudes to time and people’s attitudes to the environment (Trompenaars, 1994). Again, these classes provide a basis for modelling the critical determinants of corpo rate and national cultures.

To summarize, the work of these and other social science authors reveal four basic conclusions which we might be able to exploit in order to improve ERP package implementations.

(1) Theories of corporate and national cultures have similar de nitions of culture and share important concepts that include values, beliefs and norms.

(2) These theories distinguish between the deep manifestations and super cial characteristics of corporate and national cultures.

(3) The critical determinants of corporate culture reside more in observable practices, whereas the critical determinants of a national culture reside more in the nation’s deeper set of values.

(4) Corporate and national cultures can be described using multiple dimensions which give us a set of overlapping characteristics with which to describe aspects of culture.

In order to explore the research predictions reported in this paper, we applied social science research in developing a  rst-draft model of corporate and national cultures which was applied in describing culturerelated problems during ERP package implementation processes.

## A model of culture and its impact on ERP implementation

The extended ERP implementation method proposed in the  rst section integrates current business process approaches with models of corporate and national cultures in order to discover potential problems using predictions of possible problems using social science theories of corporate and national cultures. The basis of the model is a knowledge meta-schema for modelling the critical characteristics of corporate and national cultures. This in itself is an innovative advance. Social and management sciences do not have a tradition of conceptual modelling for describing and analysing systems. Indeed, non-computer science disciplines resist conceptual modelling because it is too dif cult to capture and describe knowledge without losing the essential context of the knowledge. However, the common de nitions of culture from social science researchers offer exciting opportunities for IT disciplines. We have synthesized and extended these social science theories in modelling the problems observed in current ERP package implementations.

## A tentative knowledge meta-schema for culture

The  rst stage of the research was to design a knowledge meta-schema capable of representing both the deeper manifestations and super cial attributes of corporate and national cultures, and the critical causal associations between them. The knowledge metaschema also incorporates modelling concepts from standard business process models such as SAP’s EPC (event-driven process chains) models so that the knowledge meta-schema can be used in methods such as SAP’s ASAP method (Curran and Ladd, 1998). For readers unfamiliar with these models, EPC models specify events, processes and event  ows for business processes. The full  rst-draft knowledge meta-schema is shown in Figure 2.

Space does not allow us to give a full de nition of the knowledge meta-schema. Instead, we provide key de nitions drawn from software and business process models which are common in current ERP implementation methods (e.g. Rosemann et al., 1999). An agent is a type of object which processes actions (Ncube and Maiden, 1999). Agents perform actions in order to achieve goals. With respect to culture, agents have beliefs, values and norms that govern their actions. An instance of an agent can be one individual person, a collection of people, one machine or a collection of machines. An action is the process of doing something with the intention of achieving a desired goal (Maiden, 1998). Actions are constrained by preconditions and post-conditions. Pre- and postconditions are conditions which must occur for an action to begin or end. An event is a moment in time when something happens. In the knowledge metaschema events start and end actions. An object is something which is manipulated for the attainment of a goal. An object can be a physical object (e.g. a radio), an infological object (e.g. information about an incident) or an object with both physical and infologica elements (e.g. an incident report). A goal is a highlevel objective that the system should meet. Goals are achieved by actions performed by agents manipulating objects (Darimont and Van Lamsweerde, 1997). All concepts except for goal are common in most current ERP business models and represent many of the more observable indicators of corporate culture according to Hofstede (1994). Goals were speci ed in the metaschema in order to provide a suitable new abstraction of intent, which is missing from current ERP modelling approaches (Mylopoulos, 1999).

![](/api/attachments/MRBJ5XD4/fulltext/images/b9669d0ff7702432796f7309e6c20ee20398f150785dba2364b233582fb6152a.jpg)  
Figure 2 The knowledge meta-schema that describes elements of corporate and national cultures which impact on ERP implementation

The rest of the knowledge meta-schema is drawn from social science research into culture, as summarized in the previous section, from philosophy and from research into arti cial intelligence models of rational agenthood. These concepts are also critical determinants of corporate and national cultures according to the theories reported in the previous section.

A role de nes the obligations of an agent. An agent can ful l one or more role types. Responsibilities de ne the liabilities of the agents associated with the role they perform. Agents are responsible for ful lling a role and initiating, controlling or undertaking actions related to their role (Maiden, 1998). A hero is a human agent admired by other agents in the organization (Deal and Kennedy, 1982). Heroes are agents that, through their role and responsibilities, undertake actions which re ect the organizational beliefs, norms and values. A social interaction describes an interaction between agents. It is a specialization of an action. Social interaction can in uence agents and their beliefs.

A belief is a mental state with properties that can be derived from its representation as a modal operator with a possible-worlds semantics (Hintikka, 1962; Galliers, 1989). Each belief is represented as a relationship between an agent (x) and a proposition (p) (BEL ´ p). Beliefs in uence agents; they are dispositions to act (Quine, 1970; Engel, 1984). A value is a special kind of belief; it is a belief that is less ‘vulnerable to removal’ (Levi, 1984), i.e. it is more persistent or entrenched (Harman, 1986; Gardenfors, 1988; Galliers, 1992). Values underpin other beliefs about the worth or importance of something. They thus provide for spectrums of belief about good versus evil or normal versus abnormal (e.g. Schein, 1992; Hofstede, 1994). A norm within a social grouping (G) is a kind of behaviour (A) that all the members of G perform in a certain context (C). In addition, all the members of G mutually believe they should perform A in C (Bach and Harnish, 1979). In other words, a norm is a standard expectation of normal behaviour including what is right or wrong in a particular context (Hofstede, 1994; Trompenaars, 1994).

A scenario is a sequence of events which start and end actions which describe current or future business processes and/or ERP software use (Maiden, 1998). Scenarios can describe norms and can be embellished with contextual information in order to create stories. A myth is a scenario, either factual or invented, which encapsulates the organization’s and/or agent’s beliefs, norms and values (Johnson, 1992). A custom is an established behaviour expressed as actions, codes or rules of behaviour (Deal and Kennedy, 1982). Customs are created and in uenced by norms, values and beliefs and in uence behaviour in the form of actions and events. A ritual is a repeated action or scenario that expresses the goals and values of the organization and dictates behaviour in the form of actions (Deal and Kennedy, 1982; Hofstede 1994). Symbols are objects explicit to people outside the organization, such as buildings and logos, which are manifestations of the organization’s hidden assumptions, beliefs, norms and values (Hofstede, 1994). Finally, the style is the way in which people deal with other people within an organization, such as the way they talk to each other. Symbols form the style of the organization (Peters and Waterman, 1982).

## Rules for applying the knowledge meta-schema

The informal and semi-formal de nitions of the critical determinants of culture above are underpinned by more formal rules for identifying determinants in data transcripts and for modelling them using the metaschema. For example, rules that are applied in detecting stakeholder norms include the following.

(1) If an agent expresses expectations of what is right and what is wrong then the agent expresses a norm.

(2) If an agent expresses principles of how things should or ought to be then the agent expresses a norm.

Likewise, a rule that is applied in guiding the detection of stakeholder’s values includes the following: if an agent expresses a persistent belief that he/she uses to underpin or justify another belief then the agent expresses a value. Similar guidelines have been developed for other knowledge meta-schema de nitions and these were applied during the data analysis reported in the next section.

## More predictions about culture

Krumbholz and Maiden (2000) reported that the knowledge meta-schema can be applied in detecting and modelling the critical determinants of culture that in uence problems with the implementation of ERP packages. However, for the proposed ERP implementation method to be effective, the model will also need to explain and predict the consequences of corporate and national cultures on ERP implementations. Our model also applies results from existing social science research into the impact of culture on change in making predictions about ERP implementations that inform three prototypical theoretical predictions.

Hofstede (1994) claimed that national culture differences reside more in values and less in practices and that corporate culture differences reside more in practices and less in values. As our model assumes that a customer’s national culture is manifest through its corporate culture, two further prototype predictions are made.

$\mathrm { P } _ { 4 } \mathrm { : }$ Critical determinants of corporate culture that reside more in a customer’s observable practices have causal associations with problems that arise during ERP package implementations.

$\mathrm { P } _ { 5 } \mathrm { : }$ : Critical determinants of national culture residing more in an organization’s deeper values in uence the critical determinants of corporate culture that have causal associations with problems that arise during ERP package implementations.

Social and management science researchers also mak important predictions about differences in national cultures that might in uence the implementation of ERP packages in different countries such as the UK and Sweden. Hence, we drew on previous research into cul ture in these two countries in exploring one further prototype prediction from these theories in order to explore these theories’ capabilities for predicting th causal in uence of culture. Based on his empirical research, Hofstede (1994) argued that Swedish organizations have a lower masculinity index than British ones, leading to less stress and less competition between employees. Therefore, we predicted the following.

$\mathrm { \mathbf { P } } _ { 6 } \mathrm { \mathbf { : } }$ ERP implementation will be less stressful and more acceptable to employees in the Swedish organization, and more collaboration rather than competition will occur in order to ensure success of the implementation.

The next section reports on the empirical method applied to a large, multinational ERP package implementation that was undertaken in order to explore these predictions.

## The empirical method

Empirical studies were undertaken on-site at a large multinational European supplier of pharmaceuticals and laboratory equipment. The company was implementing the same German ERP package in its different national subsidiaries. This paper reports on the results from visits to the UK and Scandinavian subsidiaries. The Scandinavian subsidiary had sales and administrative of ces outside Stockholm and the warehouse was located in a small town 150 km west of Stockholm. The UK operation also had a separate sales and warehousing operation. The sales and administrative of ces were on the south coast of England and the warehouse was in the English Midlands.

## The R/3 implementations

The UK subsidiary started its ERP package implementation in 1994 in order to replace a non-Windowsbased bespoke system that enabled little interaction between the functions. Six modules were implemented. The  nance module was implemented in 1995. The sales and distribution and warehouse management modules were  rst implemented in a small division in order to allow thorough testing and adaptation before these modules were fully implemented. The subsidiary went live in November 1998.

The Swedish subsidiary started its ERP package implementation in 1997. The previous system was also a bespoke system that had been in operation since 1987. A similar number of modules, including sales and distribution and warehousing, were implemented in 1999 in order to provide a single business and IT solution for all four Nordic countries. In addition, the warehouse was physically relocated 150 km to a small town and new warehouse staff were hired to use the new system.

## The data gathering approach

Two bilingual (Swedish/English) academic researchers visited the Sweden site for 2 days in December 1999 and the UK site for 2 days in February 2000. The same data capture method was applied at both sites. The research team gathered data at both sites from the IT development managers, sales and distribution developers, materials management developers, sales managers, sales and distribution key users, the warehouse manager and warehouse key users. A questionnaire was sent to each participant in their native language requesting their name, background, position, length of time in the company and department, nature of their work and typical work routines. Eleven UK and ten Sweden questionnaires were returned.

On-site data gathering was in two phases. The  rst phase elicited surface manifestations of culture. The second phase used a variation of the laddering technique from knowledge engineering (Rugg et al., 1992) in order to elicit deeper determinants of culture which were possible causes of the surface manifestations and problems reported in the  rst phase. The characteristics of culture found on the outer layers of the social science models are the observable manifestations of culture. The characteristics of culture found in the inner layer are tacit, more important determinants of national and, to a lesser degree, corporate cultures. Our questions were designed for eliciting the observable manifestations of culture described on the outer layers and then used precise verbal probes for eliciting tacit rationale for these manifestations. This use of external manifestations of culture in eliciting deeper underlying causes was the principal reason for two phases rather than one. The speci c questioning approach was based on a synthesis of these layers of culture from social science research and is shown in Figure 3. The questioning method was derived from a synthesis of culture dimensions undertaken by the authors based on the dimensions of Hofstede (1994), Schein (1992) and Trompenaars (1994) which were reported in the second section. These dimensions enable us to describe and compare the critical manifestations of corporate and national cultures. The application of a ‘neutral’ method from social science research counters claims that the studies ‘found what they were looking for’ in terms of the posited knowledge meta-schema.

![](/api/attachments/MRBJ5XD4/fulltext/images/2bee267b5de670d840f2707f57e18adbfecfc43ad57e2b3c4ae90a3a357b5768.jpg)  
Figure 3 A synthesis of the layers of the elements of culture taken from social science research providing a basis for the questioning method

## First-phase data gathering

In the  rst phase, each stakeholder was interviewed for 30 min. Each stakeholder was interviewed individually and in their own language in order to elicit more data. The questions were derived from reports of major problems with ERP implementations and previous studies of culture impact on ERP implementations (Krumbholz and Maiden, 2000). Examples of the questions asked are as follows. ‘How was the ERP implementation decided (communicated throughout the company and mutually decided or announced)?’ ‘How aware would you consider yourself to be of the way the company is doing business (its business processes, way of doing things etc.)?’ All data elicited through the interviews were transcribed to provide a data corpus for analysis.

## Second-phase data gathering

Evidence of corporate and national cultures was elicited from each stakeholder using a short questionnaire and interview in order to elicit information that supported the questionnaire responses. The design of the questionnaire was based on a synthesis of research  ndings about corporate and national cultures (e.g. Hofstede, 1991; Trompenaars, 1994) and available methods for eliciting information about culture (Deal and Kennedy, 1982). The stakeholders responded to each statement and chose the answer that re ected their view the most from a scale of A–G (A, strongly agree; B, agree; C, tend to agree; D, neutral; E, tend to disagree; F, disagree; G, strongly disagree). Examples of statements are ‘the management is more concerned with employees getting the work done than with the employees as persons’ and ‘deadlines are loose and  exible’.

## Results

The method was effective in eliciting a large corpus of data about the ERP package implementations and the subsidiaries’ corporate and national cultures.

## Overview of the ERP package implementations

The UK subsidiary invested a lot of time and resources prior to the implementation in order to involve and train stakeholders and simulate the new business processes and determine their effectiveness. All stakeholders participated in brainstorming sessions to elicit their requirements for the new system. The  nance module had a good  t with stakeholder requirements. However, the  t with the warehousing module was poor and extensive con guration was needed in order for the module to operate. This caused staff to be negative towards the ERP package because the warehousing module had not satis ed all of the stakeholder requirements that had emerged. Furthermore, in the  rst 2 months of implementation, the sales and warehouse operations experienced performance problems that led to a fall in the level of service to customers. This was due to speci c problems in the creation of deliveries and inef ciencies in the warehouse. A recovery plan that was implemented to rectify this fall in service took 3–4 months to reintroduce a stable level of service with customers. Today, after 2 years of system operation, most stakeholders are satis ed with its functions and consider the implementation to be positive for the subsidiary. The sales department takes longer to process each sales order. However, the warehousing module makes the warehouse available for longer periods and this has enabled the introduction of more ef cient shift patterns due to more ef cient processes and longer availability times.

The Scandinavian subsidiary set out to harmonize business processes across the four Nordic countries. It also tried to con gure the ERP package to support its current business processes rather than adapt them to the package’s own reference models. It set up a core team of 70 people to manage the transfer of knowledge and training from the Swedish implementation partner. The warehousing module required con guration to support missing functions, including the handling of dangerous goods such as chemicals and direct deliveries. However, the stakeholders stil believed that the modi ed warehousing system was less  exible and ‘intelligent’ than its predecessor, with more need for user acknowledgement, which did not re ect the  at and dynamic organization structures found in Swedish companies. Sales staff found the package more tedious to use due to numerous order entry screens. In contrast, controllers in the sales and logistics areas had greater access to information. Overall the implementation led to more effective integration of the subsidiary’s business solutions but at the loss of local advantage and customization.

## Modelling warehouse problems

The UK and Scandinavian subsidiaries encountered both similar and different problems during the implementation of the ERP packages. This section examines the problems with the warehousing system by modelling them with the knowledge meta-schema in order to make otherwise tacit knowledge about relevant corporate and national cultures explicit. Data describing these problems were modelled using the knowledge meta-schema. Interview transcripts with the relevant personnel were analysed in order to produce model fragments. Each model fragment identi es each stakeholder’s norms, values and beliefs and other critica determinants that indicate the corporate and national cultures causally associated with each problem.

## The importance of training

One cultural value elicited from stakeholders was the importance of training, which was lacking from this implementation process. The model fragment that was produced by applying the knowledge meta-schema is shown in Figure 4. Evidence from the data transcripts to the IT materials manager supported the model: ‘the personnel would have needed more practical work in the system before we went live’, ‘there was not enough training for the warehouse personnel’ and ‘I felt like we jumped off a cliff and did not know what would happen’.

## Job satisfaction

Another cultural value elicited from stakeholders was job satisfaction. An important cultural norm was that warehouse personnel worked ‘out there’ in the warehouse and performed physical tasks such as moving products. The organization valued employee satisfaction in their work. However, the IT materials manager believed that ‘especially in the beginning the warehouse staff did not want to sit by the desk, they wanted to be out there in the warehouse’. This re ected a problem that warehouse staff were spending more time using the system and less time ‘out there’ in the warehouse. The relevant model fragment is shown in Figure 5.

## ERP package complexity

Several stakeholders identi ed the ERP package itself as a source of problems. End-users perceived it to be too complex for a distribution company. They identi- ed one norm, i.e. that computerized systems should empower the organization. Values about the previous system included ‘the old system was just for our needs and was very effective’ (marketing manager) and, hence, a stated belief about the ERP package was ‘we bought a jumbo when we needed a bicycle’ (marketing key user). The model fragment is shown in Figure 6. Similar evidence was elicited from the IT development manager who highlighted the importance of typical Swedish  exible working practices to the effectiveness of the warehouse, but identi ed that the over-acknowledgement in the ERP package system was typical of a more ‘German’ way of doing things and that package was designed for manufacturing rather than distribution organizations. Note that, to produce this mode fragment so that it remained faithful to the origina data, the authors introduced a new modelling concept to model observations of system problems.

![](/api/attachments/MRBJ5XD4/fulltext/images/7bd6f54232a42a4914011fe5d4a54fd175cf5cb4a9e4d49b4b84b039bb00fc02.jpg)  
Figure 4 A model fragment describing facets of culture relating to staff training in the Scandinavian warehouse

![](/api/attachments/MRBJ5XD4/fulltext/images/24cdf873339f4cd8fe38da5d1fc9ac83c118cbf8fe182688304f506ae43936ba.jpg)  
Figure 5 A model fragment describing facets of culture relating to job satisfaction in the Scandinavian warehouse

## Failure to meet stakeholder requirement

UK stakeholders also identi ed problems with the initial warehousing system. An often-repeated problem was that the initial version of the warehousing module failed to meet the warehouse requirements: ‘The standard package did not do all the work we wanted it to and particularly not in the warehouse’ (warehouse site manager) (see Figure 7). It was considered normal that the warehouse was central to the organization and its success was critical the organization’s performance. However, stakeholders believed that the ERP package was inadequate: ‘warehousing was very weak to start with and we did a lot of development there to make it better’ (IT development manager) and ‘For warehousing, this package was a nightmare when we implemented it’ (sales lead user).

![](/api/attachments/MRBJ5XD4/fulltext/images/a05af1ca7cb68dac430efd7c36a2a7062536a6fb258a395ef7b045d911bd7779.jpg)  
Figure 6 A model fragment describing facets of culture relating to the perceived complexity of the ERP package for the Scandinavian warehouse system

## Fit with legislation

Another problem was that new versions of the ERP package were updated in order to keep in step with changes in German legislation which did not always correspond to changes in UK legislation, for example regarding chemicals and other hazardous materials. In particular, ‘when there is new legislation in Europe, the UK tends to change very fast’ (IT development manager), whereas ‘this package keeps pace with German laws, so we have to develop ourselves’ (IT development manager). Stakeholders identi ed the norm that system changes should re ect local legislation and believed that slower changes in the ERP package were bad. The model fragment is shown in Figure 8.

## Unsuitable operating assumptions

Another signi cant problem with the UK warehouse that was identi ed by stakeholders was the operating assumptions for the ERP package. For example, the package’s updates of purchase orders assumed perfect information and processes, even when this was not always the case. The IT materials management developer claimed that ‘You can have a complex delivery schedule against the purchase order in theory and then the supplier may acknowledge different quantities and different dates and it is not actually possible logically to match those perfectly, but the package has made an attempt and it just falls down’. He identi ed a clear expectation of such systems as being to ‘achieve the minimum safe, what can logically be done and not attempt to do it perfectly, because logically it cannot be done perfectly, there are too many variables’. Instead, computerized systems must adapt to prevailing local circumstances. The model fragment is shown in Figure 9.

![](/api/attachments/MRBJ5XD4/fulltext/images/83db3486aa6f1adfb02054c575201217f30d4d6b51a7ee0b404b942aa078ecf9.jpg)  
Figure 7 A model fragment describing facets of culture relating to the initial failures of the warehousing system

## Comparing the implementation problems

Table 1 summarizes our  ndings from the development of the warehouse system model fragments. There are both similarities and differences between the UK and Scandinavian subsidiaries. Stakeholders in the UK warehouse articulated one essential value, i.e. that the new system shall meet customer requirements. In contrast, Scandinavian warehouse stakeholders also identi ed this essential value, but also revealed two other critical values, i.e. that personnel are well-trained and satis ed in their work. Second-phase questionnaires provided evidence to support these cultural differences. For example, UK warehouse staff were more enthusiastic about their training scheme and more content with the  nal training received. In contrast, Scandinavian warehouse staff were more dissatis ed with the volume of training received. Evidence from the second-phase questionnaire also supported this: eight out of 11 UK respondents agreed with the statement ‘there are numerous training and career development programmes within the company’ whereas  ve out of ten Scandinavian respondents disagreed with that same statement. Follow-up interviews elicited similar views from UK stakeholders: ‘All employees received high-class training prior to implementation’ and ‘the training in SAP within the organization has been excellent. The amount of effort and time that was put into developing and implementing training programmes was huge’. In contrast, Scandinavian respondents claimed that ‘I would like to be able to get training through the laboratory, but there is a time problem’, ‘I think we should get more training’ and ‘there was not enough time to get enough education’.

![](/api/attachments/MRBJ5XD4/fulltext/images/8236fc24bd15047f3347b94befbf0ccfce2d2b764f058733850975f6ee678e3b.jpg)  
Figure 8 A model fragment describing facets of culture relating to the mismatch in UK and German legislation about hazardous chemicals and goods

![](/api/attachments/MRBJ5XD4/fulltext/images/ce3347bc713b3dca12c706e7b64475b6245c1a19ed78f2c285677c1919941d14.jpg)  
Figure 9 A model fragment describing facets of culture relating to failure to adapt the ERP package to local circum stances

## Modelling sales/marketing problems

Both Scandinavian and UK stakeholders also identi- ed important problems with the sales function implemented. Relevant stakeholder interview transcripts were again analysed in order to produce model fragments of the stakeholder norms, values and beliefs associated with these problems. Table 2 summarizes the critical determinants of culture from the model fragments describing problems with the new sales and marketing system. It reveals that both subsidiaries identi ed good customer service as the single overriding culture value that was associated with problems in the implementation of the sales and distribution module. Evidence from the second-phase questionnaires and interviews supported this. For example, UK stakeholders reported that ‘the company will look after its people and make sure that it offers the best customer service’, ‘the customers are extremely important to us and we must make sure that we offer the best customer service’ and ‘the company wants to do the best it can for the bene t of the customers’.

## Conclusions and Discussion

This paper reports on studies of the implementation of a German ERP package in the UK and Scandinavian subsidiaries of a multinational pharmaceutical and laboratory equipment supplier. The empirical method captured a large corpus of data about the implementation approach and about the problems with the implementations in the two subsidiaries. It applied a knowledge meta-schema  rst reported in Krumbholz and Maiden (2000) for analysing data in the corpus, both to drive the capture of data and determine the critical stakeholder values, norms and beliefs indicative of each subsidiary’s corporate and nationa cultures. In this respect, the studies were successfu in the development of a large number of mode fragments describing critical determinants of culture. This paper focuses on the model fragments related to problems with the implementation of the warehousing and sales/marketing systems. Each of the model fragments is an important contribution to the increasing body of knowledge about ERP implementations.

In order to investigate how culture impacts on ERP package implementations, the paper set out six predictions from our model of culture, which is outlined in the third section.

Table 1 Summary of the model fragments for problems with the new warehousing system

<table><tr><td>Figure</td><td>Location</td><td>Surface problem features</td><td>Underlying problem</td><td>Cultural values</td></tr><tr><td>4</td><td>Sweden</td><td>Lack of practical system use before implementation</td><td>Lack of training</td><td>Employees are trained to use the new system</td></tr><tr><td>5</td><td>Sweden</td><td>Warehouse staff not working in the warehouse enough</td><td>Job satisfaction</td><td>Warehouse staff should perform physical tasks</td></tr><tr><td>6</td><td>Sweden</td><td>System over-acknowledges warehouse operations</td><td>Poor fit with ERP package</td><td>The computer system should empower the organization</td></tr><tr><td>7</td><td>UK</td><td>Failure to meet local requirements for warehouse system</td><td>Failure to fit customer requirements</td><td>Success of the warehouse critical to whole company</td></tr><tr><td>8</td><td>UK</td><td>Failure to meet UK legislation for hazardous materials</td><td>Failure to fit customer requirements</td><td>System that fits the local legislation requirements</td></tr><tr><td>9</td><td>UK</td><td>Cannot match delivery schedules and purchase orders</td><td>ERP system assumes perfect information</td><td>Purchase orders are processed flexibly</td></tr></table>

Table 2 Summary of the model fragments for problems with the new sales/marketing system

<table><tr><td>Location</td><td>Surface problem features</td><td>Underlying problem</td><td>Cultural norms and values</td></tr><tr><td>Sweden</td><td>Unable to enter short delivery times into R/3 system</td><td>Inflexible delivery times</td><td>Important to have delivery times that are as short as possible</td></tr><tr><td>Sweden</td><td>Extra work needed to enter data into R/3 system</td><td>Increases the work load</td><td>Staff are productive and effective at work</td></tr><tr><td>Sweden</td><td>Unable to obtain holistic, integrated view of the data</td><td>Poor system navigation</td><td>Expect to obtain the benefits of integration</td></tr><tr><td>Sweden</td><td>Unable to handle customer enquiries adequately</td><td>Poor screen layout</td><td>Importance of good customer relations</td></tr><tr><td>UK</td><td>Difficult and time-consuming to enter sales data</td><td>Poor screen layout</td><td>Good level of customer service is key to success</td></tr><tr><td>UK</td><td>Users generate own non-R/3 solutions to problems</td><td>Failure to find or use R/3 functions</td><td>Required services should be the best available</td></tr></table>

## Prediction p1: the current corporate culture clashes with the future culture

Studies of the warehouse and sales operations revealed no evidence to support this prediction. The results indicated that the UK and Scandinavian stakeholders did not believe that the organization intentionally undertook an undesirable change in its corporate culture.

## Prediction p2: the supplier’s culture, which is implicit in the ERP package, clashes with the customer’s corporate culture

The results revealed evidence in the form of stakeholders’ claims about ERP package implementation problems that indicated that the supplier’s culture, which was tacit in the ERP package’s solution, clashed with the customer’s corporate culture. The paper reports three values that were not supported in the ERP package: (1) warehouse staff should perform physical tasks, (2) computer systems empower the organization and (3) warehouse staff process orders in a  exible manner. However, implementation of the ERP package led to greater administrative work and in exible processes in the warehouse, which the IT development manager identi ed as a more ‘German’ way of doing things.

## Prediction p3: the new business processes (con gured using the ERP solution) clash with the existing corporate culture

Whereas $\mathrm { P } _ { 2 }$ reported on problems that arose from the immediate implementation of the ERP package, there was little evidence to support $\mathrm { P } _ { 3 } ,$ i.e. that new business processes clashed with the existing corporate culture. Although UK sales take longer to process sales orders and the Scandinavian operations were less speci c to local conditions, stakeholders did not report problems speci c to the new embedded processes: the new corporate culture appears to have been accepted by most stakeholders.

## Prediction $\mathbf { P } _ { 4 } \mathbf { : }$ critical determinants of corporate culture that reside more in a customer’s observable practices have causal associations with problems that arise during ERP package implementations

The model fragments reported in this paper provide evidence to support this prediction. Each model fragment shown in Figures 4–9 describes phenomena elicited verbally from stakeholders in response to focused questions about implementation problems and causal associations to observable actions and other observations (added to improve the knowledge metaschema) that describe problems with the ERP package implementation. More model fragments that provide evidence to support this prediction are reported in Coulianos (2000).

## Prediction ${ \bf \cal P } _ { 5 } \mathbf { : }$ critical determinants of national culture residing more in an organization’s deeper values in uence the critical determinants of corporate culture that have causal associations with problems that arise during ERP package implementations

In contrast to $\mathrm { P } _ { 4 } ,$ there was no evidence to support $\mathrm { P } _ { 5 } .$ The studies revealed few differences in the implementation problems encountered in the two subsidiaries. There are several possible explanations for this. One is that the multinational had a strong corporate culture across the two subsidiaries and that this corporate culture subsumed national differences in similar warehousing and sales/marketing tasks in the two countries. Another explanation might be that the ‘culture shock’ felt in both subsidiaries due to their ERP package implementations led to domination of the essential values of the current corporate culture in the face of disruptive change.

Prediction 6: ERP implementation will be less stressful and more acceptable to employees in the Swedish organization and more collaboration rather than competition will occur in order to ensure success of the implementation

Retrospective  ndings provided no evidence to support this prediction: there was no difference in the UK and Scandinavian attitudes to stress, collaboration and competition arising from the ERP package implementations. This result suggests a third, more tantalizing explanation, that is that our predictions about national culture differences were based on out-of-date research. Hofstede’s (1994) dimensions of national culture were based on extensive empirical work carried out in the 1980s. However, both UK and Swedish societies and organizations have undergone substantial change since then and this leaves us with an intriguing thought: are current social science theories of culture out-of-date and, hence, irrelevant to the challenges of standardization and localization for today’s multinational IT implementations?

More generally, the results summarized in Tables 1 and 2 show that the diverse range of ERP implementation problems were causally associated with a smaller number of clashes with core customer values. This has important implications for our extended ERP implementation method: eliciting and analysing core customer values for their  t with the ERP package can give greater leverage when predicting and handling the implementation problems shown graphically in Figure 3.

## Future work

These results have important implications for the extended ERP package implementation method and, in particular, for the need for eliciting, modelling and analysing the ERP supplier’s culture, which is tacit in the ERP package. The authors are currently planning studies for eliciting and modelling the corporate culture of the German supplier reported in this paper in order to investigate hypotheses about the impact of the supplier’s culture on implementation success. We look forward to reporting our  ndings in the near future.

The results also have implications for the model of culture which we posited in the third section. Evidence of culture was elicited from different people in the UK and Scandinavian subsidiaries. Hence, the in uence of different personalities has to be considered when modelling a homogeneous corporate culture and, in particular, the in uence of leaders and founders in the organization. Schein (1983) argued that ‘founders usually have a major impact on how the group de nes and solves external problem of surviving and growing, and how it will internally organise itself and integrate its own efforts’ (p. 15). This suggests that founders and leaders in the two subsidiaries (e.g. the IT development managers) might have in uenced the corporate and national cultures and their impact on implementation. However, these studies did not produce any evidence about the nature of this in uence, for example whether or not the IT development managers either nulli ed or reinforced different facets of corporate and/or national culture. Further studies that take into account stakeholder personalities and in uences are needed for answering this question.

## Acknowledgements

The authors wish to thank the ERP package vendor and its customer for their support in undertaking the studies reported in this paper.

## References

Bach, K. and Harnish, R.M. (1979) Linguistic Communication and Speech Acts (MIT Press, Cambridge, MA).

Coulianos, N. (2000) The Impact of Culture on the Implementation of ERP Systems such as SAP’s R/3. (Centre for HCI Design, City University, London).

Curran, T.A. and Ladd, A. (1998) “SAP R/3 Business Blueprint” (Prentice-Hall, Upper Saddle River, NJ).

Darimont, .R. and Van Lamsweerde, A. (1997) Formal re nement patterns for goal-driven requirements elaboration. In Proceedings of the Fourth ACM Symposium Foundations of Software Engineering (ACM Press, San Francisco), pp. 179–90.

Deal, T. and Kennedy, A. (1982) Corporate Cultures: The Rites and Rituals of Corporate Life (Penguin Books, London).

Densley, B. (1999) The magni cent seven: getting the biggest bang from the ERP buck. In Proceedings of the First International Workshop EMRPS99, Eder, J., Maiden, N. and Missikoff, M. (eds) (Istituto de Analisi dei Sistemi ed Informatica, CNR Roma), pp. 59–65.

Dobson, P., Williams, A. and Walters, M. (1993) Changing Culture: New Organisational Approaches, 2nd edn (Institute of Personnel Management, London).

Engel, P. (1984) Functionalism, belief and content. In The Mind and the Machine – Philosophical Aspects of Arti cial Intelligence, Torrence, S. (ed.) (Ellis Horwood Ltd, Chichester).

Galliers, J. (1989) A Theoretical Framework for Computer Models of Cooperative Dialogue, Acknowledging Multiagent Con ict. (University of Cambridge Computer Laboratory, Cambridge).

Galliers, J. (1992) Autonomous belief revision and communication. In Belief Revision, Gardenfors, P. (ed.) (Cambridge University Press, Cambridge), pp. 220–46.

Gardenfors, P. (1988) Knowledge in Flux. Modelling the Dynamics of Epistemic States. (MIT Press, Cambridge, MA).

Gulla, J.A. and Mollan, R. (1999) Implementing SAP R/3 in a multi-cultural organisation. (eds) Proceedings of the First International Workshop EMRPS99, Eder, J., Maiden, N. and Missikoff, M. (Istituto de Analisi dei Sistemi ed Informatica, CNR Roma), pp. 127–34.

Harman, G. (1986) Change in View – Principles in Reasoning (Bradford Book, MIT Press, Cambridge, MA).

Hintikka, J. (1962) Knowledge and Belief. (Cornell University Press, New York).

Hofstede, G. (1994) Cultures and organisations: Inter-cultural Co-operation and its Importance for Survival. Software of the Mind (Harper Collins, London).

Johnson, G. (1992) Managing strategic change: strategy, culture and action. Long Range Planning, 25(1).

Krumbholz, M. and Maiden, N.A.M. (2000) How culture might impact on the implementation of enterprise resource planning packages. In Proceedings of Computeraided Information System Engineering (Springer-Verlag) pp. 279–93.

Levi, I. (1984) Decisions and Revisions. (Cambridge University Press, Cambridge).

Maiden, N.A.M. (1998) SAVRE: scenarios for acquiring and validating requirements. Journal of Automated Software Engineering, 5, 419–46.

Mylopoulos, J.M. (1999) Goal-oriented analysis for software customisation. In Proceedings of the First International Workshop EMRPS99, Eder, J., Maiden, N. and Missikoff, M. (eds) (Istituto de Analisi dei Sistemi ed Informatica, CNR Roma), p. 375.

Ncube, C. and Maiden, N.A.M. (1999) Guidance for parallel requirements acquisition and COTS software selection.

In Proceedings of the Fourth IEEE Symposium on Requirements Engineering (IEEE Computer Society Press, Limerick), pp. 133–40.

Peters, T.J. and Waterman, R.H. (1982) In Search of Excellence (Harper & Row, New York).

Quine, W.V. (1970) The Web of Belief (Random House, New York).

Rosemann, M., Frink, D., Von Uthmann, C and Friedrich, M. (1999) Work ow-based ERP: a new approach for ef cient order processing. In Proceedings of the First International Workshop EMRPS99, Eder, J., Maiden, N. and Missikoff, M. (eds) (Istituto de Analisi dei Sistemi ed Informatica, CNR Roma), pp. 239–48.

Rugg, G., Corbridge, C., Major, N.P., Burton, A.M. and Shadbolt, N.R. (1992) A comparison of sorting techniques in knowledge elicitation. Knowledge Acquisition 4(3), 279–91.

Schein, E.H. (1983) The role of the founder in the creation of organisational culture. Organisational Dynamics.

Schein, E.H. (1991) Organizational culture and leadership, in Frost, P.J. (ed.) Reframing Organizational Culture. Sage, Newbury Park, pp. 14–25.

Trompenaars, F. 1994 Riding the Waves of Culture: Understanding Cultural Diversity in Business (Nicholas Brealey Publishing, London).

Warren, L. (1999) ERP sans frontiers. Computer Weekly, 2 November, 32–3.

Address for correspondence: M. Krumbholz, Centre for Human–Computer Interaction Design, City University, Northampon Square, London, EC1V 0HB, UK.
