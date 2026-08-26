---
otero_id: 17183
otero_key: "U3QCH6UH"
title: "Knowledge-based systems for strategic market planning in small firms"
authors: "Odd J. Borch; Gunnar Hartvigsen"
year: "1991"
journal: "Decision Support Systems"
doi: "10.1016/0167-9236(91)90053-e"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Knowledge-based systems for strategic market planning in small firms \*

Odd J. Borch

Nordland Research Institute, Bodø, Norway

Gunnar Hartvigsen

Department of Computer Science, University of Tromsø, Tromsø, Norway

This paper gives an overview of strategic planning and decision-making in small firms, together with a discussion of the use of knowledge-based systems in strategic market planning. Furthermore, we describe the STRATEX system, which is a knowledge-based system for strategic market planning in the export trade of fish and fisheries products. The results of the pilot system development of STRATEX are briefly presented, along with a discussion of needs for further developments in this field.

Keywords: Artificial intelligence, Decision support systems, Expert systems, Fish industry, Knowledge-based systems, Marketing, Market segments, Strategic decision making, Strategic market planning.

This research was supported by the Norwegian Fisheries Research Council (NFFR), grant no. IV 833.013.

## 1. Introduction

The use of information technology to create or sustain competitive advantages is one of the success factors in today's industry. Computer-based information systems, often coupled with advances in telecommunication, decision support and expert system technology, enable such operations. Recent applications of information technology to corporate strategy have been widely discussed, both in research and commercial literature. Porter and Millar [46], for example, state that information technology affects corporate strategy in three ways: improving internal efficiency, creating competitive advantages, and spawning new businesses. In this paper we are giving attention to the use of information technology in market planning, an important part of the corporate strategy formulation process.

Marketing is one of the area being considered as promising in Porter and Millar's [46] framework. Christopher, McDonald, and Wills [16] argue that good information is a facilitator of successful marketing action. As a result, marketing management becomes first and foremost an information processing activity. Piercy and Evans [45] state that

“it is possible to view the marketing organization primarily as an information processing structure, on the boundary of the company between decision makers and the environment”. (p. 7)

Decision support systems and expert systems represent one of the most interesting sub areas of the use of information technology in market planning. A decision support system is an interactive computer-based system that helps decision makers utilize data and models to solve unstructured problems [56]. Expert systems are designed to represent and apply factual knowledge of specific areas of expertise to solve problems [64]. In recent years, the literature on both areas have addressed the potential intersection, or even the convergence, between decision support systems and expert systems (cf. e.g., [63,26,18,19,62]). In this paper we use knowledge-based systems for the intersection of decision support systems and expert systems. Since the early 1980's, expert systems have captured a growing commercial interest. An increasing number of industrial expert system applications are entering the market. However, expert systems have made little headway in market planning [40].

This paper will focus on strategic market planning and the choice of market segments. Strategic segment management focus on where the firm should be at a given time as well as how the same firm will attain a prefixed destination. Michman [37] claims that a strategic approach used in planning would place the (marketing) manager in a better position to adapt to the market and to choose the right distribution channels. Furthermore, we will give an brief overview of the STRATEX system. STRATEX is a knowledge-based system for strategic market planning supporting the choice of marketing segments. The system is developed for the export trade of fish and fisheries products from Norwegian fish processing plants [9,12]. This paper describes how the system helps the manager to clarify his goals and capability in the market. In addition, we discuss the problem of the use of new technology in an open-ended, complex problem area. Finally, we take up the experiences from STRATEX and the needs for further development in knowledge-based system technology and the knowledge acquisition methodology.

## 2. Theoretical Background

In developing strategic knowledge-based systems, we have to take as a starting point the special demands of decision making and the strategic planning process. Secondly, we have to examine the special characteristics of the type of organization in question, as well as the line of business the system is supporting. The development of the STRATEX system is based on knowledge of strategic decision making, management in small firms, and recent research on the market segment for raw and manufactured fish products in Europe. In this chapter we will outline the theoretical bases for such systems.

## 2.1. Strategic Planning

In trying to cope with an ever-changing and challenging environment – in terms of technology, consumer behavior, political situation, economic conditions and other factors, the area of strategic planning has gained wide acceptance and interest among both academicians and practicing managers. Strategic planning is the decision-making process leading to final connections between organization and environment. Hirshfield [27] identifies four conceptual levels of planning in an organization: strategic planning, tactical planning, operational planning, and scheduling and dispatching. Planning may differ according to the organizational level of responsibility identified, the scope of planning issues addressed, and the planning horizons. The characterization corresponds to the framework of Anthony [2] (strategic planning, management control and operational control), with the addition of scheduling and control.

In strategic planning, business firms must be regarded as open systems dependent on resources from their environment for survival and goal achievement. In most businesses, the environment has changed from low competition, low complexity conditions to more turbulent, complex and demanding characteristics. This makes it necessary to focus on the firm's strategic relations to its total environment [20]. It is now necessary for the management to cope simultaneously with competitive as well as entrepreneurial and socio-political challenges [4].

The theory of strategy formulation has developed from a concentration around long range planning towards the activity of strategic planning. Long range planning was developed as a tool suitable in stable environments. The future was predicted through extrapolation of the past market trends. This approach is heavily based on quantitative techniques as operational research methods. Long range planning often takes better performance in the future for granted, which make it less suitable as a planning approach in the turbulent and unpredictable areas, e.g. as the fish industry.

Today the strategic planning concept incorporates the management of all environmental exchange relations as well as design of the internal capability matching these relations. The strategic planning approach does not necessarily expect the future to be an improvement over the past, nor does it assume extrapolation to be possible. Anthony, Dearden and Bedford [3] state that

“Strategic planning is a process for the formulation of long-range activities that spans both goal establishment and guiding policies and strategies for reaching the goals. Changes, in such long-range strategic plans, change the character and direction of an organization. Strategic planning includes plans for the acquisition and disposition of major facilities, divisions, or subsidiaries; the markets to be served and distribution channels for serving them; the organization structure; research and development activities; sources of long-term capital; and dividend policy.” (p. 14)

As most firms have to face turbulent and sometimes unpredictable markets, their managers not only have to watch and decide about their product-market strategy, but also to take into consideration their internal capability in order to achieve the fit needed between the firm and its environment.

A comprehensive specification of a strategic planning process is made by Ansoff [4]. As shown in fig. 1, the first step in his strategic planning process is an analysis of the firm's prospects, identifying of objectives for the firm as a whole, as well as trends, threats and opportunities. The next step is competitive analysis which tries to determine possible performance improvement obtained from changes in the competitive strategies in the different business areas of the firm. In order to choose between more or less promising areas, the firm has to do a strategic portfolio analysis, which includes comparing different business area prospects, establishing priorities, and allocating future strategic resources. Depending on whether or not this presents a potential line toward a future goal that is acceptable, the analysis is completed. Otherwise the firm continues with a diversification analysis, which means detecting what is missing in the present portfolio and identifying new business areas. By adding the performance anticipated from the new business areas to the present potential line, the firm gets the overall goals and objectives of the firm.

The strategic planning process described by Ansoff [4] constitutes a suitable basis for strategic planning in an ever-changing and turbulent market like the international fish market. Nevertheless, Ansoff's framework has to be adjusted to small firm competitive position and the domain characteristics.

## 2.2. Strategic Planning in Small Firms

Small firms are characterized by a simple organizational structure and a strong centralized leadership [38]. A low degree of organizational specialization and few administrative resources makes it necessary to concentrate the decision making in the hands of the top-manager. When constructing strategic decision support systems, one has to be aware of the fact that decision making is very much a cognitive process in the head of the leader.

Another characteristic feature of small firms is the lack of resources and power to dominate their environments. Smaller organizations have to adjust to changes in environmental conditions. They also have to be flexible as regards organizational goals. Because of this, it may be rational for small firms to change strategy in small steps instead of making wide, long range decisions $[48,10,11]$ .

A third characteristic side of small business management is the focus on personal relationship and cooperation. When markets become turbulent, with mutual dependency and uncertainty concerning goals as well as performance, market coordination through the price mechanism is not sufficient. The result of this is the generation of transaction cost in the exchange channels [65,42].

![](/api/attachments/U3QCH6UH/fulltext/images/18d5513467274f1292677c023cde4c1b5da02b2a001fd005ead2153c7234955e.jpg)  
Fig. 1. The strategic planning process by Ansoff [4].

A solution to the transaction cost problem may be vertical and horizontal integration, incorporating the areas creating uncertainty. Through internalizing the transaction problem using a hierarchy of leaders, it may be easier to control the sources of friction in the production process $[65]$ . Small firms do not have the financial resources for such expansions. They may also loose their small business advantages through integration.

An alternative to this is communicative networks with a broad set of personal and social contracts between exchange partners $[35,10,11]$ . The social contracts are founded in the values of the social groups that the participants are connected to. Personal contracts are based on mutual confidence, affiliation, self-expression and satisfaction of needs among participants. Communication networks are coordinated through speech action and the expectation of sharing of benefits between participants.

An ideal knowledge-based system should take into consideration the different kinds of communicative action as well as the needs and values connected to them. The subtle and non-quantitative characteristics of this type of information, as well as the need for contextual knowledge to understand the meaning of the action, create quite an enormous challenge for the constructors of strategic decision support systems.

## 2.3. Decision-Support Systems and Expert Systems

A decision support system is a coherent system of computer-based technology (hardware, software, and supporting documentation). Such a system is used by managers as an aid to their decision making in semi-structured decision tasks, and focus on supporting rather than replacing managerial judgments. They also focus on improving the effectiveness of decision making rather than merely improving its efficiency $[32]$ . Decision support systems are most valuable in helping decision makers understand their specific circumstances and preferences and the effects these have on the availability and desirability of various possible actions $[29]$ (see fig. 2). To be effective, a decision support system demands a symbiosis between the users and the system. As a result, there is an interplay between user and computer that produces a total effort greater than attained by the user and the computer operating independently. This provides synergistic decision-making $[23]$ .

Expert systems represent another class of decision-making and problem solving tools. An expert system is a computer program using expert knowledge to attain high levels of performance in a narrow problem area. By applying a symbolic representation of human expertise, instead of employing more algorithmic or statistical methods, the problem solving process becomes more human-like [30,64]. As shown in fig. 2, expert systems can offer decision makers important support for dealing with the domain of their decision. This is attained through the representation of skill and factual knowledge of experienced domain experts in extensive knowledge bases [29].

![](/api/attachments/U3QCH6UH/fulltext/images/86cba4925c1fa14f7e9869e388653b113d37e14f22ebf9bfe3beedef4411b126.jpg)  
Fig. 2. Integration of ES and DSS into KBS in order to assist decision-makers with both the generic and the unique aspects of their decisions (partly adopted from Holtzman [29], p. 157).

In recent years, we have seen a growing interest of combining features from expert and decision support systems (cf. e.g., [63,26,18,19,62]). Doukidis [19] argues that several attempts have been made to incorporate artificial intelligence techniques into decision support system design frameworks with the expectations of procuring a more powerful decision support and improving the decision-making process. The artificial intelligence improvement includes expert systems features such as employment of an inference engine mechanisms improving the model base, knowledge representation techniques improving the knowledge management, and intelligent front-end system improving the user dialogue and interface. Fig. 2 illustrates how knowledge-based systems provide the benefits of both expert and decision support systems. By this, such systems can address both the generic and unique aspects of their decisions. In addition, by employing expert knowledge to assist the decision-making, knowledge-based systems can go significantly beyond traditional decision analysis and support [29].

## 2.4. Knowledge-Based Systems in Strategic Decision Making

In turbulent environments, strategic management has to be a continuing process to prepare the company for fast moving threats and opportunities in the years to come. The managers have to respond to weak signals and early indicators of events that will have impact on the company. This kind of environmental turbulence is closely linked with the technology-intensity of the products. Products and markets using advanced technology will change faster and with greater uncertainty than low technology markets with less processed products. The larger the complexity and turbulence of the environment, the more difficult the strategic decision making process. The modern manager has to make decisions under great uncertainty, evaluating a broad range of issues, taking into consideration environmental signals as well as information about internal capacity and attainable resources [12].

The strategic planning process involves a large number of both physical and intellectual activities. Physical processes are data elicitation, construction of physical models, and so on. In addition to these physical processes, collected data need to be organized. This kind of operation demands conceptual knowledge of how to interpret the data. Furthermore, the manager has to apply his own reasoning knowledge in order to evolve possible future movements, to describe new phenomena in the environment, to compute risks, and to distinguish future openings in the market.

This means that before we manage to develop a successful commercial planning system, we need an indisputable understanding of the cognitive aspects of planning. Simon $[53,54]$ has laid the groundwork of this understanding in his discussion of ‘bounded rationality’, which suggests that decision-makers must construct simplified mental models when dealing with complex problems. In addition, Simon $[54]$ and Taylor $[61]$ argue that decision-makers can only approximate rationality in their attempts to solve complex problems. Another aspect within these kind of decision making is the possibility of selective perception, since the decision-maker is unable to evaluate comprehensively all variables relevant to a decision $[28,36]$ .

Haber [25] argues that much of the research trying to identify and explain the mental processes that underlie human behavior has adopted an information processing approach based on two major assumptions. The first is that cognitive activity can be analyzed through a number of separate stages. The second proposes a limit to the amount of processing that occurs at any moment. Within the information processing approach, we have seen two general lines of research evolution. One direction has been concerned with the identification of the separate stages of the cognitive process, and the explanation of how each stage operates (e.g., [57,58,14,33,50,47]). The other has taken a broader view, concentrating on complicated cognitive skills such as problem solving, and considering how stages operate and interact in the execution of these skills (e.g., [52,21,41,15,43, [44,55,31]). The development of different stage models have increased our understanding with respect to decision making and behavior. The cognitive approach has in many ways increased our understanding of decision strategies and the perceptual aspects of decision making. For instance, the prospect theory of Kahneman and Tversky [31] is important for the development of input/output routines in a strategical planning system. However, a lot of work remains before we develop a complete understanding of all aspects of planning.

Systems capable of helping the manager through the physical and cognitive stages of the strategic planning process seems very valuable. This is especially true in small and medium sized firms where administrative capacity is scarce. Knowledge-based systems might enable a company that can not afford a live expert to have one ‘on disk’. The alternative is often the use of expensive consultants leaving the firm on its own after a short period. A knowledge-based system may support and rationalize the cognitive as well as the physical process of planning.

The manager may use a knowledge-based system as a training tool, as well as an analytic instrument in the strategy formulation process. Instead of learning all the details of strategy analysis, the manager can make use of the computer program as a support in his managerial work. By including decision support functions to serve decision makers in different environments, we may get flexible, task oriented tools. These tools must support planning in stable, low complexity type environments as well as turbulent, strategically discontinuous ones. We need systems which provides simple ‘what-if’ decision models, relying on historical data, as well as more interactive symbiotic decision models.

The ‘what-if’ decision models usually work as an expert contributing the necessary data as well as the decision solving model, giving the optimal solution. This is possible when the manager has a problem that is well structured, and where the input data and/or the criteria of choice can be quantified and specified in advance. A symbiotic model must give the decision maker the opportunity to build in the necessary data. The manager needs to be in control of the decision making process. He also must be able to change the data and reanalyze by going back to preceding steps in the process. The system should also be able to stimulate thinking and learning behavior by relating the decision in question to past decisions and performances, and to support the perception and interpretation of environmental signals. A critical factor is the quality and applicability of the system explanations. Swartout and Smoliar [60] describe three kinds of expertise that must be modelled to provide adequate explanations: knowledge of terminology, domain descriptive knowledge, and abstract problem solving knowledge.

As Moutinho and Paton [40] have pointed out, knowledge-based systems have made little headway in marketing. This is especially true in strategic planning of market segments. In a more general view, Baldwin and Kasper [8] argue that the lack of knowledge-based management support systems “is likely due to a combination of the difficulties associated with representing ill-defined relationships such as those found in many management decision-making domains, the lack of system design and application guidelines, and the limited interchange of knowledge between MIS and AI professionals” (p. 159). During the last years we have seen an enlarged scepticism concerning the possible commercial success of knowledge-based systems. Luconi, Malone and Scott Morton [34] claim that expert systems have been ‘oversold’ in some of the literature. Riet [49] argues that

"As is not uncommon in AI, first systems are successful, because they are made for demonstrative reasons, as prototypes to show that certain techniques really can be used. When it comes to systems to be used in actual practice, it turns out that they are much more complex than originally foreseen." (p. 15)

Denning [17] argues that “we cannot expect an expert system to help if we do not know how something is done” (p. 83). And this is the core of the problem - the development of knowledge-based systems has to be founded on an understandable domain. Stevenson [59] demonstrates through an examination of knowledge-based systems in the UK financial service sector, that “from a rational perspective, there existed a dichotomy between ubiquitous optimistic rhetoric and the ‘reality’ of few experimental developments” (p. 297).

On the other hand, Fredricks and Venkatraman [24] claim that it is necessary to employ computer-based systems to realize the full power of multidimensional strategy analysis. Today's strategy problems are inherently multidimensional, and the challenge will be to integrate the multiple dimensions affecting a business. Furthermore, Fredricks and Venkatraman [24] report that "strategy support systems are now being developed that combine powerful means of matching analytical strategy tools to particular business situations, with the flexibility to respond to market changes." (p. 54).

However, even if knowledge-based systems and techniques in recent years have taken huge steps towards commercial use in several areas, still much work is left to be done before we will find commercial use of strategic planning systems. The introduction of a successful commercial planning system relies heavily on having an indisputable understanding of the cognitive aspects of planning as well as having a conceptual description of the planning process (for support functions in strategic planning, the process of strategic planning, and in learning to do these kinds of tasks). In addition, as stated by Fredricks and Venkatraman [24], “the innovative strategies of the future will unite creative thinking with a detailed understanding of multiple business dimensions. The rewards for good multidimensional strategy will be increasingly substantial-and the penalties for oversimplistic strategy increasingly severe.” (p. 54)

In order to construct a proper knowledge-based system, we have to be aware of and adjust to the special characteristics of the system domain. In the next chapter, we describe the context of strategic decision making, and the challenges of smaller Norwegian fishing export companies in foreign markets.

## 3. Domain Description-the Norwegian Export of Fish and Fisheries Products

## 3.1. Market Situation

In 1988, more than 90 percent of the turnover from Norwegian fish and fish products comes from the export trade. Norway, with its 4.1 million inhabitants, constitutes no more than a limited market for Norwegian fish products (the domestic market). Therefore, the only way to increase the total trade is to expand the sales abroad, which again requires intensive marketing and planning operations. A Norwegian processing and exporting firm in the fish industry may operate in several types of markets. The export trade of fish from Norway includes distribution of raw fish in wholesale markets. In these markets, each supplier is relatively small and has no influence on the prices in markets. The markets are to a certain degree characterized by free competition and seasonal variations in demand and supply. For the experienced supplier, it is possible to estimate the development in pricing by using historical data and week to week information on fish catches and distribution capacities. In this market, it is possible to design a knowledge-based system building upon the experience of the most competent fish buyers and sales persons in the market. The system may use numerical information describing the connection between demand, supplies and prices in the market [12]. Because of the need to adjust the data of such a system to the weekly changes in market conditions, the costs of running a system in this area will be higher than the time spared in decision making for an experienced broker. Only in the case of a newcomer in the market, will decision support systems be useful.

During recent years, an increased marketing effort has been made in the export trade of processed fish products to sell in more sophisticated market segments, for example, supermarkets, large fast-food chains and the catering sector. In these segments there are high competition and turbulence, a continuous need for product and market development, and therefore a need for frequent controlling of the different aspects of strategy. This kind of complex and ill-structured environment with non-linear behavior makes it necessary to combine numerical calculation as well as logical reasoning, also giving the decision maker the possibility to identify new factors affecting the results.

Fish and fisheries products represent a complex group of food. For instance, the cod-group alone consists of several hundred potential products. Another problem that must be taken into consideration is the rules and regulations controlling the different markets. The last and largest problem is the lack of stability in fish supplies. This means that the market depends on variations concerning the raw material. It is impossible to make long term predictions of catch sizes. Some of these problems are to a certain degree solved through fish farming, securing more stable deliveries. But this causes new problems, such as the need for coordination of a larger number of small fish farming plants, a long production period (3 years), risk of illness, etc.

From this we may conclude that the fishing sector as a whole is a very complex and ill-structured domain. Furthermore, the complexity makes it difficult for the average fish firm to be aware of all the possibilities and pitfalls in the export market.

## 3.2. Facing the Market Situation

Meeting the market challenges means handling a great number of tasks, environments and a complex net of external and internal relations. A decision support system for strategic planning in the market of fish and fisheries products must be able to serve several environmental elements. It must have the opportunity to coordinate the streams of information into useful databases in different decision sectors. Secondly, the system must be able to undertake statistical operations manipulating historical data. The third part of the system has to cover decision-making models. These models make it possible to use the system as an expert. In addition, the system must also contain more loosely structured parts, making it possible for the decision maker to analyze the data in his own ways, giving a model structure for describing new phenomena in the environment. These facilities increase the possibility for double-loop learning $[5]$ . An examination of environmental factors affecting decision making uncertainty in marketing channels, indicated that the four dimensions, diversity among consumers, dynamism, concentration, and applicability, are principal $[1]$ .

A major problem within this field is the dependency on political decisions, currency decisions, catch limitations, tariffs, etc. These may in few hours turn operational knowledge into historical facts [6]. Therefore, one has to regard parts of the domain as unsuitable for expert system applications. Another problem is the continuing knowledge elicitation necessary to keep the knowledge base as good as possible (operational). These observations cause a reserved attitude to knowledgebased systems within this field. Such systems have to be regarded as an assistant rather than an expert. One solution is to look for semi-structured tasks within the domain, where it is possible to find a balance between the computing system and human judgments [32]. In the case of STRATEX, the system is not giving operational information, but is concentrating on long range elements of importance in strategic decision making.

According to this description, a knowledge-based system for strategic market planning in the export trade may be of great value even if it is limited to containing information concerning more permanent aspects of the market. Another valuable function for an export firm is the possibility to make competitive strategy, through analyzing the different market segments with respect to their strategic business areas (SBA's); priority and attractiveness, and their extrapolated competitive position (ECP) [4]. Both functions may be included in a knowledge-based system. Due to the fluctuations in the market, the user also has to be able to neglect any results from the system or/and redo parts of previous tasks (incremental decision-process) to get an adequate result.

## 4. The STRATEX System

STRATEX (the STRATEGic decision-making system for EXport firms) is a knowledge-based system for strategic market planning in export of fish and fisheries products from Norwegian fish processing plants. STRATEX has been developed at Nordland Research Institute in Northern Norway.

In the STRATEX project, we have paid attention to the use of knowledge-based systems (decision support systems and expert systems) in the sub area of strategic planning and market choices. In this area, we have experienced, since the beginning of the 1980's, the use of decision support systems, also referred to as marketing information systems, in order to meet the particular needs in managerial decision making. These systems provide managers with an integrated range of software tools. These tools include mathematical modeling techniques, forecasting and statistical routines, communications links, data management tools, graphics routines and easily used output reporting facilities [7]. But, as indicated by

Moutinho and Paton [40], few expert systems exist within this area.

Most Norwegian fishing industry firms are small with very little administrative capacity. Profitability in the market is very low. The 1987 annual account of 600 small fishing industry firms shows a total deficit of more than NOK 100 million (US \$15 mill.). The reason for this deficit is complex, including small catches as well as price decline in the market. However, to change this downward trend, costs have to be reduced and higher prices achieved. Some of these goals may be fulfilled by using knowledge-based systems like STRATEX. Therefore, the main purpose of STRATEX is to procure a tool for analyzing the firm (according to the users's own parameters: the initial values, the product he wants to sell, etc.) and the market situation. Using the system in strategic planning may improve the firm's profit by [12]:

\- Reducing export costs by tracing cost areas when the firm is above average.

Improving the profitability by presenting the most attractive area to the user (the most attractive combination: minimum of capital investment together with maximum price).

The STRATEX system has been developed using the Xi $^{TM}$ Plus expert system shell by Expertech. In addition we have used the Lotus 123 $^{TM}$ for representation of financial data, and the Turbo

Pascal $^{TM}$ to make certain input/output routines, sorting and calculation.

## 4.1. Model

Fig. 3 gives an overview of how STRATEX guides the user through the strategic market planning process, from problem definition, via segment evaluation to choice of segment. Furthermore, the system presents action programs for capability improvement (see fig. 1).

The details of the STRATEX system have been adjusted to the small firm competitive position and the characteristics of the industry in question. The knowledge-base contains the market information needed for the planning process. The use of expert system technology also makes it possible for the decision maker to correct the system by adding rules, although such a user may need more knowledge about how such a program works than the average user. The system takes into consideration environmental elements of importance for the choice of segment. The segments are ranked accordingly to match between market characteristics, the goals of the firm and the existing capability. Finally, as shown in fig. 3, STRATEX recommends a plan for capability improvements with regard to the segments chosen. The system provides qualitative ranking as well as financial calculation of the profitability of each segment.

![](/api/attachments/U3QCH6UH/fulltext/images/fe30ed93956a4cf3097644d5b6e887e571ff716fc2e90c50bd9896ab30bf2441.jpg)  
Fig. 3. The decision-making procedure of the STRATEX system.

Even if the scope of the STRATEX project is delimited to the area of fish and fisheries products, we consider the STRATEX system to constitute a general framework for strategic market planning. Through the replacement of the domain knowledge, the system may fit most markets.

During the development of STRATEX, we have stressed the flexibility aspects of the strategic planning process. The manager is given the ability to go back to previous steps if he finds a segment interesting, and if he wants to reduce uncertainty. He may then go back in order to search for more information and then recalculate the whole segment. The system will recommend sources of information that the manager may use in his search. After having decided what segments to serve, the manager must find the right strategy for his segment or segments. This is done by deciding upon what products to present in the market and capability needed to serve the market, using an analysis of the possible future success factors of the segment. By comparing these demands and the present capability, the system presents an action program for capability improvement that the firm may use in the implementation of the strategy. He is also advised on how to proceed step by step into the new segment, if the manager wants a more incremental implementation. The manager is asked whether he thinks it is possible to follow the capability development plan. If not, he is recommended to go back and choose other segments from the list. In this way, the system fulfils some of the demands regarding adjustment to the individual's decision making style $[22]$ .

## 5. Concluding remarks

This paper has described the use of decision support and expert system technology in the problem area of strategic decision making. The results of the project show that the development of systems in this area is a great challenge to the information technology industry. The research reveals new problems and weaknesses in today's technology.

One of the fundamental problems is the lack of understanding of the cognitive processes of management in ill-structured areas. In recent years, we have seen that the cognitions of key decision-makers are receiving increased research attention in strategic management [51]. As argued in section 2.4, the strategic planning process, as in STRA-TEX, involves a large number of both physical and intellectual activities, ranging from data elicitation and construction of physical models to data interpretation and cognitive processes. This implies that before we will get a successful commercial planning system, we need an indisputable understanding of the cognitive aspects of planning. Therefore, a lot of scepticism exists concerning the possibility of developing effective planning systems. Mockler [39] states that

‘Until more is learned about what goes on inside the head of an expert strategic planner, we won’t know how experts really do strategic planning. And if we don’t know that, it will be difficult to develop truly effective ways to help others learn to do planning. Nor will computers be used extensively to assist in these difficult thinking aspects of planning.’ (p. 33)

According to Mockler [39], most authors concerned with strategic corporate planning do not explain how the manager's imagination proceeds with regard to perceiving new success requirements in the marketplace. Based on the general assumption that knowledge-based systems are able to deal with unknown and uncertain information, such systems may have the possibility to do, or at least to assist, some of the cognitive work necessary for strategic planning. In addition, it is assumed that such system might be able to learn how to do these kinds of work. However, there is reason to believe that many problems faced in strategic planning simply do not lend themselves to solutions of the sort that expert knowledge-based systems offer [39].

Zinkhan, Joachimsthaler, and Kinnear [66] found in their study on how managers interact with marketing decision support systems that risk averseness, involvement, cognitive differentiation, and age were important predictors of utilization and satisfaction. In the development of STRATEX, we have especially emphasized the aspects concerning cognitive understanding and limitations. The user dialogue and interface, for example, have been carefully worked out in order to avoid misunderstandings. The user may ask for explanations at any step of the process, and control the sources of the data in use. He may also overrule the expert with regard to the importance of data elements and the content. Nevertheless, we believe that the degree of understanding of the cognitive aspects of planning (necessary to get an appropriate strategic planning tool) is partly related to the complexity of the domain and the general knowledge level among the decision makers. In the fish industry, where the level of formal education is somewhat low, and the experience of systematic market planning is low, such a system might be of commercial interest as an assistant as well as an expert in certain decision areas. STRATEX is developed to be more like an assistant, i.e. acting more as a decision support system rather than an expert system. Altogether, experience shows that research in this area should proceed.

Buzzell [13] shows the importance of information technology in marketing by declaring

“Throughout history, marketing methods and institutions have been shaped by changes in the technologies available for obtaining, analyzing and communicating information”. (p. 1)

Moutinho and Paton [40] stress several facts that enable the development of commercial knowledge-based systems in marketing within the next years: - Falling hardware and software costs.

\- The majority of firms will have access to some form of computer technology.

\- Several firms will have basic computing expertise, and may be interested in more advanced systems.

\- The larger firms, employing their own functional experts, including computer services, can also directly benefit from the application of expert systems based technology.

## Holtzman [29] argues that

“By substantially lowering the cost and speeding up the delivery of decision analysis assistance, intelligent decision systems open a wide new range of possibilities for assisting decision-makers. Thus, such arenas as personal decisions, small-business decisions, tactical and operational decisions in industry, and decisions performed by autonomous systems - all of which are well outside for current economic scope of professional decision analysis - can now be addressed with intelligent decision systems." (p. 98)

We believe that within a few years we will experience commercial use of knowledge-based systems for strategic planning. Results so far have shown that the STRATEX concept has the potential to assist, and to some extent, to act as a colleague, in a strategic market planning process in uplimited parts of the domain.

## References

[1] R.S. Achrol and L.W. Stern, Environmental Determinants of Decision-Making Uncertainty in Marketing Channels. Journal of Marketing Research 25 (1988) 36–50.

[2] R.N. Anthony, Planning and Control Systems: A Framework for Analysis (Harvard University, Graduate School of Business Administration, Boston, 1965).

[3] R.N. Anthony and N.M. Dearden, Management Control Systems (Irwin, Homewood, Illinois, 1984).

[4] H.1. Ansoff, Implanting Strategic Management (Prentice-Hall, Englewood Cliffs, New Jersey, 1984).

[5] C. Argyris, Single-Loop and Double-Loop Models in Research on Decision-Making, Administration Science Quarterly 21 (1976) 363–377.

[6] I. Arnarson, Computer-Based Systems for Information Processing and Decision Making in the Marketing of Fish and Fisheries Products, Preliminary Report Nr. 1018/87, Nordland Research Institute, Bodø, Norway (1987) (In Norwegian).

[7] M.E. Arnold and J.M. Penn, The Information Technology Revolution in Marketing (1). A Review of Some Current Applications, Quarterly Review of Marketing 12. Nr. 2 (1987) 1–6.

[8] D. Baldwin and G.M. Kasper, Toward Representing Management-Domain Knowledge, Decision Support Systems 2 (1986) 159–172.

[9] O.J. Borch, STRATEX-an Expert System for Competitive Strategy Analysis in Export Firms, Preliminary Report Nr. 1017/86, Nordland Research Institute, Bodo, Norway (1986) (In Norwegian).

[10] O.J. Borch, Strategy and Management Behavior, PhD-dissertation, University of Umeaa, Dept. of Business and Administration, Umeaa, Sweden (1989).

[11] O.J. Borch, Small Firms and the Coordination of Environmental Exchange. Communicative Action as a Transaction Coordinating Mechanism in Small Business Environment Channels, HSN-Report Nr. 6. Bodø University Center, Bodø, Norway (1989).

[12] O.J. Borch and G. Hartvigsen, Stratex-a Knowledge-Based System for Export of Fish and Fish Products, in: T. O'Shea and V. Sgurev, eds., Artificial Intelligence III. Methodology, Systems, Applications (North-Holland, Amsterdam, 1988, 425–432).

[13] R. Buzzell, Marketing 1995. A Scenario for the Future, in: R. Buzzell, ed., Marketing in an Electronic Age (Harvard Business School Press, Cambridge, Massachusetts, 1985).

[14] W.G. Chase, Elementary Information Processes, in: W.K. Estes, ed., Handbook of Learning and Cognitive Processes, Vol. 5 (Erlbaum, Hillsdale, New Jersey, 1978).

[15] W.G. Chase and H.A. Simon, Perception in Chess, Cognitive Psychology 4 (1973) 55–81.

[16] M. Christopher, M. McDonald and G. Wills, Introducing Marketing (Pan, London, 1980).

[17] P.J. Denning, Towards a Science of Expert Systems, IEEE Expert 1, Nr. 2 (1986) 80–83.

[18] G.I. Doukidis, Decision Support System Concepts in Expert Systems: An Empirical Study, Decision Support Systems 4 (1988) 345–354.

[19] G.I. Doukidis, General Considerations on Knowledge-Based Management Support Systems, in: G.I. Doukidis, F. Land and G. Miller, eds., Knowledge-Based Management Support Systems (Ellis Horwood, Chichester, West Sussex, 1988).

[20] P.F. Drucker, Managing in Turbulent Times (Heinemann, London, 1980).

[21] H.J. Einhorn, Use of Nonlinear, Noncompensatory Models as a Function of Task and Amount of Information, Organizational Behavior and Human Performance 6 (1971) 1–27.

[22] M.C. Er, Decision Support Systems: A Summary, Problems, and Future Trends, Decision Support Systems 3 (1988) 355–363.

[23] F.N. Ford, Decision Support Systems and Expert Systems: A Comparison, Information and Management 8 (1985) 21–26.

[24] P. Fredericks and N. Venkatraman, The Rise of Strategy Support Systems, Sloan Management Review 29, Nr. 2 (1988) 47–54.

[25] R.N. Haber, Information Processing, in: E.D. Carterette and M.P. Friedman, eds., Handbook of Perception, Vol. 1 (Academic Press, New York, 1974).

[26] J.C. Henderson, Finding Synergy Between Decision Support Systems and Expert Systems Research, Decision Sciences 18 (1987) 333–349.

[27] D.S. Hirshfield, From the Shadows, Interfaces 13, Nr. 2 (1983) 72–76.

[28] R.M. Hogarth, Judgment and Choice: The Psychology of Decision (Wiley, Chichester, West Sussex, 1980).

[29] S. Holtzman, Intelligent Decision Systems (Addison-Wesley, Reading, Massachusetts, 1989).

[30] P. Jackson, Introduction to Expert Systems (Addison-Wesley, Wokingham, 1976).

[31] D. Kahneman and A. Tversky, Prospect Theory: An Analysis of Decisions Under Risk, Econometrica 47 (1979) 263–291.

[32] P.G.W. Keen and M.S. Scott Morton, Decision Support Systems: An Organizational Perspective (Addison-Wesley, Reading, Massachusetts, 1978).

[33] D. LaBerge, Automatic Information Processing: A Review, in: J. Long and A. Baddeley, eds., Attention and Performance, Vol. 9 (Academic Press, New York, 1980).

[34] F.L. Luconi, T.W. Malone and M.S. Scott Morton, Expert Systems: The Next Challenge for Managers, Sloan Management Review 27, Nr. 4 (1986) 3–14.

[35] I.R. Macneil, The New Social Contract: An Inquiry into Modern Contractual Relations (Yale University Press, New Haven, 1980).

[36] R.O. Mason and I.I. Mitroff, Challenging Strategic Planning Assumptions (Wiley, New York, 1981).

[37] R.D. Michman, Marketing Channels: A Strategic Approach, Managerial Planning 32, Nr. 2 (1983) 38–42.

[38] H. Mintzberg, Structures in Fives: Designing Effective Organizations (Prentice-Hall, Englewood Cliffs, New Jersey, 1983).

[39] R.J. Mockler, Computer Information Systems and Strategic Corporate Planning, Business Horizons 30, Nr. 3 (1987) 32–37.

[40] L. Moutinho and R. Paton, Expert Systems: A New Tool in Marketing, Quarterly Review of Marketing 13, Nr. 4 (1988) 5–12.

[41] A. Newell and H.A. Simon, Human Problem Solving (Prentice-Hall, Englewood Cliffs, New Jersey, 1972).

[42] W.G. Ouchi, Markets, Bureaucracies and Clans, Administrative Science Quarterly 25 (1980) 129–142.

[43] J.W. Payne, Task Complexity and Contingent Processing in Decision Mmaking: An Information Search and Protocol Analysis, Organizational Behavior and Human Performance 16 (1976) 366–387.

[44] J.W. Payne, Contingent Decision Behavior, Psychological Bulletin 92 (1982) 382–402.

[45] N. Piercy and M. Evans, Managing Marketing Information (Croom Helm, London, 1983).

[46] M.E. Porter and V.E. Millar, How Information Gives You Competitive Advantages, Harvard Business Review 63, Nr. 4 (1985) 149–160.

[47] M.I. Posner and P. McLeod, Information Processing Models-In Search of Elementary Operations, Annual Review of Psychology 33 (1982) 477–514.

[48] J.B. Quinn, Strategies for Change: Logical Incrementalism (Irwin, Homewood, Illinois, 1980).

[49] R.P. van de Riet, Problems With Expert Systems? Future Generations Computer Systems 3, Nr. 1 (1987) 11–16.

[50] A.F. Sanders, State Analysis of Reaction Processes, in: E. Stelmach and J. Requin, eds., Tutorials in Motor Behavior (North-Holland, Amsterdam, 1980).

[51] C.R. Schwenk, The Cognitive Perspective on Strategic Decision Making, Journal of Management Studies 25, Nr. 1 (1988) 41–55.

[52] H.A. Simon, Behavioral Model of Rational Choice, Quarterly Journal of Economics 69 (1955) 99–118.

[53] H.A. Simon, Models of Man (Wiley, New York, 1957).

[54] H.A. Simon, Administrative Behavior (Free Press, New York, 1976).

[55] H.A. Simon and J.R. Hayes, The Understanding Process: Problem Isomorphs, Cognitive Psychology 8 (1976) 165–190.

[56] R.H. Sprague and E.D. Carlson, Building Effective Decision Support Systems (Prentice-Hall, Englewood Cliffs, New Jersey, 1982).

[57] S. Sternberg, The Discovery of Processing Stages: Extension of Donder's Method, Acta Psychologica 30 (1969) 276–315.

[58] R.J. Sternberg, Intelligence, Information Processing, and Analogical Reasoning: The Componential Analysis of Human Abilities (Erlbaum, Hillsdale, New Jersey, 1977).

[59] H. Stevenson, Expert Systems in the UK Financial Services Sector: A Symbolic Analysis of the Hype, in: G.I. Doukidis, F. Land and G. Miller, eds., Knowledge-Based

Management Support Systems (Ellis Horwood, Chichester, West Sussex, 1988).

[60] W.R. Swartout and S.W. Smoliar, On Making Expert Systems More Like Experts, Expert Systems 4, Nr. 3 (1987) 196–207.

[61] R.N. Taylor, Psychological Determinants of Bounded Rationality: Implications for Decision-Making, Decision Sciences 6 (1975) 409–29.

[62] E. Turban, Decision Support and Expert Systems: Managerial Perspectives (Macmillan, London, 1988).

[63] E. Turban and P.R. Watkins, Integrating Expert Systems

and Decision Support Systems, MIS Quarterly 10, Nr. 2 (1986) 121–136.

[64] D.A. Waterman. A Guide to Expert Systems (Addison-Wesley, Reading, Massachusetts, 1986).

[65] O.E. Williamsson, Markets and Hierarchies: Analysis and Antitrust Implications (Free Press, New York, 1975).

[66] G.M. Zinkhan, E.A. Joachimsthaler and T.C. Kinnear. Individual Differences and Marketing Decision Support System Usage and Satisfaction, Journal of Marketing Research 24 (1987) 208–214.
