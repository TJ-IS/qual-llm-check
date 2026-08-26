---
otero_id: 2142
otero_key: "V5ECBFCV"
title: "SIMBA: A simulator for business education and research"
authors: "Fernando Borrajo; Yolanda Bueno; Isidro de Pablo; Begoña Santos; Fernando Fernández; Javier García; Ismael Sagredo"
year: "2010"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2009.06.009"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# SIMBA: A simulator for business education and research

Fernando Borrajo <sup>a,</sup>⁎, Yolanda Bueno <sup>a,1</sup>, Isidro de Pablo <sup>a,2</sup>, Begoña Santos <sup>a,3</sup>, Fernando Fernández <sup>b,4</sup>, Javier García <sup>b,5</sup>, Ismael Sagredo <sup>b,5</sup>

<sup>a</sup> Faculty of Economics and Business Administration, Universidad Autónoma de Madrid, Ctra. de Colmenar Viejo, Km 15, 28049 Madrid, Spain <sup>b</sup> Computer Science Department, Universidad Carlos III de Madrid, Avenida de la Universidad 30, 28911 Leganés, Madrid, Spain

## a r t i c l e i n f o

Available online 18 June 2009

Keywords: Business simulator Business intelligence Business education Multi-agent systems

## a b s t r a c t

Business simulators are used for decision-making since different scenarios can be evaluated without risk. They are also used in business management education. The main goal of this paper is to introduce SIMBA (SIMulator for Business Administration), a new simulator that serves as a web-based platform for business education, permitting both classroom and distance education. This paper also adds a research aspect in business intelligence because SIMBA can be used as a <sup>fi</sup>eldwork tool for the development and evaluation of intelligent agents. The simulator creates a more complex competitive environment in which intelligent agents play the role of business decision makers.

© 2009 Elsevier B.V. All rights reserved

## 1. Introduction

Business simulators cover the design and development of software, processes, and best practices for integrating, warehousing and analyzing business information. Identifying the right area to change is a very important factor in improving the success of an organization. Thus, business simulators are very useful to improve management decisionmaking processes. These tools help managers understand their business processes and how the modi<sup>fi</sup>cation of these processes impacts the organization. In this way, risk involved in such changes is identi<sup>fi</sup>ed before implementing decisions [22]. Once the risk factors are identi<sup>fi</sup>ed, the business simulator can be used to change desired parameters [41].

Business simulators are also promising tools for teaching and research [14]. Economic simulations emulate real-world problems, so they can be used for business education. A very important business game used in teaching is JA Titan (Junior Achievement Titan) [38]. JA Titan teaches students, in an entertaining way, how to run a global business in a competitive marketplace. The success or failure of an organization depends on how managers take key decisions such as pricing, marketing and capital investment. However, business simulators are not only used for learning and education, they also offer a complex domain where the researchers can investigate different areas. The bibliography describes business simulators as a tool for conducting psychological research [4]. In this case, the business simulator is used to investigate the decisionmaking process in complex situations [6]. This research process is used to draw conclusions about the human mind and to study its ability to solve apparently chaotic problems. Typical uses of business simulators in research are <sup>fi</sup>nancial planning (quantifying the impact of the decisionmaking process), risk management (measuring, managing and determining the right balance between pro<sup>fi</sup>tability and risks), forecasting (analyzing historical data and using the data obtained by the business simulator to predict the future), business process modeling (establishing the steps in the business process in a simple way), interactive learning (business simulators can be used in teaching economics), and arti<sup>fi</sup>cial intelligence research (using data mining, evolutionary computation or intelligent agents).

In this study, we would like to mention the contributions of Professor William W. Cooper in the development of different research areas. Professor Cooper has made a large contribution in the <sup>fi</sup>eld of linear programming, non-linear programming, goal programming, and other different optimization approaches. Furthermore, he has introduced new concepts in management science, economics, and other business-related <sup>fi</sup>elds. His research is a clear example of symbiosis among research in different <sup>fi</sup>elds, and of how research in one <sup>fi</sup>eld can contribute to research in others. Application of Data Envelopment Analysis (DEA) to improve the management of congestion in Chinese industries [7], or the application of mathematical programming models in air pollution management [8] are two clear examples of the application of mathematical theory to real problems in different areas.

The main goal of this study is to describe SIMBA, a simulator for both classroom and distance education in Business Administration. The main characteristic of SIMBA is that it emulates business reality using the same variables, relationships and events found in the business world. It can be used competitively, since different companies compete among themselves to improve their results. It addresses the main functional areas of the companies, and permits different levels of dif<sup>fi</sup>culty, depending on the users, which have a high level of interactivity with the simulator. This interaction is performed through the Internet, so that different teaching scenarios can be de<sup>fi</sup>ned from classical on-site courses to distance education. Finally, SIMBA incorporates the design innovation of including intelligent agents to assume the role of competitors, thus increasing the complexity of the simulated market, and opening the possibility to arrange multiplayer simulations in which only a few human teams engage in an open market competition. This is possible due to the undergoing research the designers are conducting in multi-agent systems and automated decision-making.

The remaining structure of this research is organized as follows. Section 2 describes some related studies in business simulators and business intelligence. Section 3 shows SIMBA's business model, describing the basic rationale used to implement it. Section 4 describes the main characteristics of SIMBA which make it very useful for students and teachers. Section 5 describes SIMBA as a platform for the study and integration of multi-agent systems in Educational Business Simulators. Finally, Section 6 describes the main conclusion, along with future research tasks.

## 2. Related works

This section provides an overview of the state of the art in research in business simulators, both as an educational and a research tool, considering different perspectives. Special emphasis is made, on the one hand, on teaching methodologies and the role simulators can play in the learning processes, and, on the other hand, the advanced technologies involved in the design of business simulators, such as business intelligence, and multi-agent systems. This analysis is summarized in Table 1.

## 2.1. Business simulators survey

Simulation games have their background in board games, dating back to China around 3000 B.C., Go, Weiqi and Igo, and were followed by other modern board games such as Monopoly, created by Charles Darrow in 1934. But modern business games, or simulators in business administration, arrived on the scene after 1955 [39]. In 1956, the <sup>fi</sup>rst management simulator appeared, the Top Management Decision Simulation, developed by the American Management Association [27], followed closely by the Business Management Game, developed by McKinsey and Company, Green and Andlinger [2]; Schreiber's Management Decision Game, the <sup>fi</sup>rst to be used in the classroom, and the Top Management Decision Game, used in the University of Washington in 1957. The evolution in the use, number and type of management simulators has been reviewed in different studies [9,11,17,19]. Of course, advances in IT (information technology) have improved gaming technology, providing a faster response, improved usability and accessibility.

Key topics and references in business simulators.

<table><tr><td rowspan="2">General business simulators</td><td>•Surveys on business simulators: [2,9,11,17,19,39,40]</td></tr><tr><td>•Business simulators: [27,1]</td></tr><tr><td rowspan="3">Business simulators in education</td><td>•Pedagogical advantages of the use of business simulators: [12,26,28,31,40]</td></tr><tr><td>•Definition of the simulator model: [13,10,30,32]</td></tr><tr><td>•Black-box models versus transparent models: [18,29]</td></tr><tr><td rowspan="4">Multi-agent systems in business intelligence</td><td>•Business intelligence: [24,25]</td></tr><tr><td>•Multi-agent systems and business intelligence: [3,5,23,33]</td></tr><tr><td>•Multi-agent Systems systems in business simulators: [34,35]</td></tr><tr><td>•Autonomous decision-making in business simulators: [20,21]</td></tr></table>

Educational outcomes highlight the success of these software products. Business simulation improves the transfer speed from theory to practice, with reduced cost and savings in training time [12,28]. It represents a change in mental models, making faster changing connections between the perceptions of decisions and actions, having quantitatively shown its effectiveness in attaining a change in mental processes involved in decisions [19,31,36]. As a result, improvement in capabilities, competences, skills and qualities, is well reported. The results are clear in management improvement of organizational contingencies, creativity, assessment criteria, interaction and discussion, and knowledge acquisition, [26,40].

Some controversy exists as to what types of simulators improve knowledge. On the one hand, there is a problem on the interrelationship among company's functional areas, organizational contingencies, company as an open socio-technical system, <sup>fl</sup>ow or stock variables and feedback, non-linear relations, qualitative information, structureresults [13], because simulators address only one functional area or problem of the company. The proposition of an integrated focus, the Systems Dynamics Approach, helps solve these problems [10,30]. With the emergence of the Dynamic Decision-Making in Systems Dynamics, simulators integrate this complexity, considering that decision makers do not have consistent and persistent goal structures, they are not using complex algorithms or calculating the optimal solution (there are no optimal solutions in the economy), nor are they trying to get all information to support decision-making; not all decisions are rational, and non-linear quantitative processes are not developed [15,32].

On the other hand, these aspects have arisen in discussions about the type of business game simulator to use: “black box” models or “transparent information” models. The black box model is justi<sup>fi</sup>ed by the arguments stated above: decision makers do not use all the information, they do not make calculations, nor do they solve complex problems and are not entirely rational. Business games with transparent information, white box or transparent box, offer the user a tool of causal diagrams and provide the methodology for making calculations, but have the disadvantage that they can only use equations and simple relationships since complex relationships and mathematical models would not be understandable for the user [18,10,29].

## 2.2. Business simulators and business intelligence

The origin of business intelligence (BI) can be traced back to the <sup>fi</sup>rst data processing applications [25]. Currently, business organizations are moving towards decision-making processes that are based on information. BI represents technologies and methods for following the best strategy in the marketplace [24]. AI includes several technologies that may be very useful in improving BI, such as intelligent agents, data mining and automatic decision-making.

Software agents are often used in BI. The interaction can be in the form of message passing, negotiating or changes in the environment [3]. Multi-agent systems (MAS) show great potential for advancing BI and solving complex problems in a changing environment. In the paper [3], the authors build a model proposing three <sup>fi</sup>elds in order to use an MAS combined with BI. These <sup>fi</sup>elds are: intelligence data acquisition, intelligent modeling and intelligent information brokerage. The agent approach is widely applied to business problems and decision support systems [5,23]. The paper [33] studies how two groups of agents handle business complexity related to power trading in the US. The proposed approach can estimate <sup>fl</sup>uctuations of electricity prices as well as other methods such as neural networks and genetic algorithms. Two adaptive models were prepared. One group consists of adaptive agents who were equipped with multiple learning capabilities and an exponential utility function. The other group consists of adaptive agents who were equipped with limited learning capabilities. A real application of these ideas can be found in [34], where the authors propose the use of a multi-agent intelligent simulator to numerically examine several reasons to explain why the electricity crisis happened between May 2000 and January 2001 in California. This simulator explains the price <sup>fl</sup>uctuation of wholesale electricity during the crisis with high accuracy. In [35], following the same line of investigation, the authors describe an application software for analyzing and understanding a dynamic price change in the US wholesale power market.

Some business simulator games use a mixture of human and machine learning agents [20]. The learning agents can use a typical genetic-based learning classi<sup>fi</sup>er system, XCS (eXtended learning Classi<sup>fi</sup>er System) [1]. In that study, the authors developed four kinds of agents as alternatives to human players. They implemented a random agent that makes its decision using uniform random numbers; a reactive agent whose decisions are based on the values of several variables; agents that imitate human behavior using the log information obtained in an interaction between the simulator and a human; a learning agent that uses a reinforcement learning approach to acquire action policies. Reinforcement learning (RL) allows decision-making agents to learn from the reward obtained from executed actions and, in this way, to <sup>fi</sup>nd an optimal behavior policy. In stochastic business games, the players take actions in order to maximize their bene<sup>fi</sup>ts. While the game evolves, the players learn more about the best strategy to follow. With this, RL can be used to improve the behavior of the players in a stochastic business game [21]. In Section 6 we will show an application of RL to acquire business policies which are able to take autonomous decisions.

As a conclusion, we can say that there is an open <sup>fi</sup>eld for the development of business simulators merging conventional business management decision-making frameworks together with the technologies from the <sup>fi</sup>elds of Business Intelligence and Arti<sup>fi</sup>cial Intelligence. In the previous studies, there is no evidence of such convergence in a web-based simulation platform for business education. This justi<sup>fi</sup>es the design effort of the tool presented in this paper. The next sections are dedicated to describe the functional and pedagogical characteristics of the new simulator, with special emphasis in the improvement of the teaching function via IT infrastructures.

## 3. SIMBA: a simulator for business administration

SIMBA (SIMulation in Business Administration) was developed by following all the requirements stated in the previous sections. It is the work of a spin-off company from the Universidad Autónoma de Madrid in collaboration with Universidad Carlos III de Madrid. SIMBA is a webbased computer program that simulates the performance of a series of markets. This program, the result of over 20 years of experience in business simulation both in university education and executive training, emulates business reality using the same variables, relationships and events present in the business world. The purpose is to provide the users with an integrated vision of the company, using the same basic rules, relationships and market dynamics present in business management, simplifying complexity and highlighting the content and principles providing higher pedagogical value.

## 3.1. Main characteristics of SIMBA

SIMBA has a number of features that are worth highlighting. First, it is a competition simulator, where a team of participants can compete either against other companies automatically managed by the Simulator by means of intelligent agents, or have multiple teams of participants competing among themselves. It is also multifunctional because it addresses the main functional areas of the company. It is interactive because it allows the participant to communicate both with the Simulator and with other participants in the simulation.

It is very versatile because it provides different levels of dif<sup>fi</sup>culty, adapting to the participants' knowledge of business administration.

There is no limit to the number of users. It allows the diversi<sup>fi</sup>cation of products, markets, customer segments and technologies. Since it is a web-based system, the users can access it directly from any computer connected to the Internet, thus eliminating the need for the application to be installed in a local IT environment. Moreover, it can run on any platform or operating system. Therefore, it can be used anywhere and on any device allowing access to the web [16]. Furthermore, SIMBA can be customized to most institutional and training settings, using several languages and dialects, currencies and socioeconomic environments upon demand. Additional features include the availability of a wide number of graphics and data sheets on the main indicators to follow up both the companies and the market, the edition of markets, economic and company events which may alter market dynamics and a ranking and evaluation module to objectively assess the team's management performance. All these characteristics portray a unique tool to create an effective immersion-learning environment to achieve educational objectives.

## 3.2. Architecture of SIMBA

Fig. 1 gives a general perspective of SIMBA's structure, showing the different operating modules from the user's view point. It consists of sets of specialized subsystems designed to provide high standards of versatility and usability, both for the participant and the administrator of the simulation. We only describe the modules whose functionalities are somewhat singular. The Users' Module permits the system's administrator to de<sup>fi</sup>ne user pro<sup>fi</sup>les to satisfy the needs of the institutions which will use the simulator. This module allows the creation of customers, administrators, instructors or assistants and participants. SIMBA also provides the functionality to be run automatically responding to certain prede<sup>fi</sup>ned speci<sup>fi</sup>cations and does not need the involvement of an administrator. Instructor and assistant pro<sup>fi</sup>les can be designed to work with large teaching groups—such as a competition at international level—and to adapt to the academic regulations found in higher education.

The Customization Module covers a range of functions aimed at creating products, geographic and economic environments, the initial situations of the companies, news for the market Newsletter, together with the selection of the currency and the language of the competition. All this information allows for the generation of simulations tailor-made to the participants' needs. This module provides a very interesting and innovative adaptive capability and is the keystone for exploiting SIMBA's potential.

The Planning Module enables the instructor to organize and de<sup>fi</sup>ne the characteristics of each simulation. It creates teams by assigning participants, determining the number of decisions to be taken and their scheduling, de<sup>fi</sup>ning the number of markets and the number of companies in each market and assigning teams to companies. Later, the module must de<sup>fi</sup>ne how the markets will be structured in terms of currency, language, product, and economic and environmental parameters. The Knowledge Module is aimed to provide on-line support and tutoring to participants.

The Simulation Process consists of four highly specialized modules which con<sup>fi</sup>gure the competition dynamics that the users actually look for when participating in a simulation. Each of them performs a speci<sup>fi</sup>c task, requiring either a set of reports, system functionalities or management techniques and methods interwoven in a decision-making itinerary which constitutes the essence of management. This process starts with the Reporting Module, which generates all the information that the team needs about its company, its competitors and the competition's environment.

In the Analysis and Diagnosis Modules, the team's participants apply their management and negotiation skills, decision-making style, analysis technology, etc. to diagnose their company's competitive position, de<sup>fi</sup>ne strategic and operational goals. Finally, it makes the appropriate decisions by using the interface SIMBA in the Decision Making

![](/api/attachments/V5ECBFCV/fulltext/images/6d5b1dbeae619b56a38742d465f03b33ce87c645beff8d1c273ee140f5b07019.jpg)  
Fig. 1. Simulator model.

Module, including outsourcing negotiations. These two modules shape the core scenario in which participants play their roles as decision makers. They make use of approximately twenty-<sup>fi</sup>ve variables per market, organized in functional areas, a <sup>fi</sup>gure which can be expanded if companies engage in outsourcing negotiations. The average estimated decision-making time is 2 hours per market.

The Arbitrage Module is aimed at controlling the competition's dynamic and the interaction among teams and instructors. It is run every time a decision-making period ends, according to the scheduled calendar, verifying that all teams have taken their decisions. This module also allows the instructor to select news and incidents, some of which can be created in the Customization Module, which may alter the market dynamic, thus adapting the Simulator to the skills and abilities of the participants. This information is also published in the Simulation's Newsletter.

Then the “time machine” or the market arbitration is run. By doing this, the program integrates the previous period's situation, the teams decisions, and the parameters of the general economic environment together with those of each geographic market, and starts the Simulator's engine to generate output information for the new period. This process will be described in detail in a later point. This process is carried out for all the companies in one market, and then for all the markets run in a competition with SIMBA. Once this is <sup>fi</sup>nished, the results will be available for the participants to start a new decision cycle until the end of the competition, which leads to the use of the Ranking and Evaluation Module.

As a conclusion, SIMBA offers a rank of the participating teams in each simulation. To perform this assessment, it uses a multi-criteria procedure in which the behavior of a series of indicators (mainly economic, commercial, <sup>fi</sup>nancial and management magnitudes) is analyzed. SIMBA allows the instructor to give a weighting to each of them, depending on the importance he/she wants to give to each indicator. Moreover, when there are multiple markets in a simulation, a more complex evaluation procedure can be applied. SIMBA provides a consolidated ranking, or scoring, a “synthetic index” of the business units the teams manage during the competition. This index is calculated by consolidating the positioning of each strategic unit (products, markets, customers or alternative technologies) in each of the following criteria: positioning by business size weighted according to key economic, <sup>fi</sup>nancial and management indicators; positioning according to criteria such as diversi<sup>fi</sup>cation and risk of their business portfolio; and positioning according to the market value and the life cycle of the industry.

The three criteria are consolidated in a single weighted ranking and the results and details of the ranking are available to the teams as needed, depending on the instructor's criterion. The weights can be changed according to the instructor's criterion:

$$
\begin{array}{r l} \text { Ranking } & = 0. 2 * \text { puntROI } + 0. 1 5 * \text { puntROE } + 0. 1 * \text { puntProductivity } \\ & \quad + 0. 1 * \text { puntProdCost } + 0. 1 * \text { puntMktShare } \\ & \quad + 0. 1 * \text { puntDebt } + 0. 2 5 * \text { puntMktValue }. \end{array}
$$

This procedure provides an opportunity for the instructor to open a group discussion about the management and market behavior of the different teams, bringing out successes and failures, errors and achievements, together with the competitive dynamics that are worth discussing. Finally, a winner and a loser can be identi<sup>fi</sup>ed. This makes the Ranking Module a very useful and distinctive tool for educational purposes.

## 3.3. The Market Arbitrage Process

At the end of every decision-making period, what SIMBA creators call the “time machine” takes place. This is a procedure which triggers economic environmental events, market dynamics and administrative procedures to generate a new market situation, which indicates the beginning of a new decision-making period. This process is launched by the instructor and takes place for each of the markets active in a given simulation. The arbitrage starts when the decision-making time for a simulation period expires. This means that all teams should have taken the decisions for each of the markets in which their companies operate. Thus, the instructor checks that all teams have taken their decisions, intervenes in the environment if he/she decides to make a signi<sup>fi</sup>cant change in market or economic conditions and, <sup>fi</sup>nally, starts the “simulation engine” in order to come up with a new situation. Fig. 2 shows the work<sup>fl</sup>ow of the Market Arbitrage Process, the main milestones of which will be discussed next.

![](/api/attachments/V5ECBFCV/fulltext/images/eb96fa85c1150b9171bc968af16b1670cc210873e206df6f8d5a9badd266abae.jpg)  
Fig. 2. Work<sup>fl</sup>ow of the market arbitrage process.

As depicted in Fig. 2, the <sup>fi</sup>rst step is the Economic Environment Arbitrage, aimed at de<sup>fi</sup>ning the context in which market arbitrage will take place. The variables accountable for this arbitrage are, among others, in<sup>fl</sup>ation, consumer con<sup>fi</sup>dence index, interest rates both for loans and <sup>fi</sup>nancial assets, prices and availability of all production factors including labor and technology. They behave on a random basis that starts from an initial situation generated under the instructor's speci<sup>fi</sup>cations consistent with the evolution of in<sup>fl</sup>ation.

The Market Demand Arbitrage is aimed at generating the total product demand that the market is willing to absorb under the current economic environment conditions and the global marketing effort that the competing companies have made to stimulate demand. Demand generation is obviously in<sup>fl</sup>uenced by past economic and market conditions, and will also determine the future evolution of market behavior to the extent that companies are capable or not of meeting market expectations. The most signi<sup>fi</sup>cant variables affecting potential demand are long term demand projections, sales seasonality, marketing effort of all the companies in the market, and other environmental parameters obtained during the Economic Environment Arbitrage.

In the Quality Arbitrage, the market evaluates the marketing and R&D effort of both the companies and the industry as a whole as a <sup>fi</sup>rst step to assigning companies to the different market segments. This process is carried out by means of a complex function involving fortyseven variables and thirty-eight parameters which weigh them over a three-year weighted average time-span for the three customer segments present in each market. A simpli<sup>fi</sup>ed expression of the algorithm for running the Quality Arbitrage is:

```txt
Quality(t) = f[(pquality(t - 1, t - 2, t - 3)*Quality(t - 1, t - 2, t - 3)),
(pr&d(t, t - 1, t - 2, t - 3)*R&D(t, t - 1, t - 2, t - 3)),
ppublicity(t, t - 1, t - 2, t - 3)*(Publicity(t, t - 1, t - 2, t - 3)),
(psalesforce(t, t - 1, t - 2, t - 3)*Salesforce(t, t - 1, t - 2, t - 3)),
(ptraining(t, t - 1, t - 2, t - 3)*Training(t, t - 1, t - 2, t - 3))]
```

Consistency or volatility of decisions in R&D and marketing policy also account for the quality level assigned to each company, since management policies should be coherent over time. This testing is carried out by means of a set of logic rules embedded in the Quality Process.

This step gives place to the allocation of Potential Demand to each company in the market, or a de<sup>fi</sup>nitive measure of their marketing strategy success. This is done by comparing the marketing decisions of each company with those of others in the same market segment by means of an attraction index handling twenty-three variables and twenty-one parameters. A general expression of this function is as follows:

Company Potential Demand t

```txt
Company Potential Demand(t)

= f{company[(ppricevariations(t-1, t-2, t-3))
*Pricevations(t-1, t-2, t-3)),
(ppublicityvariations(t, t-1, t-2, t-3))
*(Publicityvariations(t, t-1, t-2, t-3)),
(psalesforcesvariation(t, t-1, t-2, t-3))
*Salesforcevariations(t, t-1, t-2, t-3)),
(ptrainingvariations(t, t-1, t-2, t-3))
*Trainingvariations(t, t-1, t-2, t-3))],
competitors [(ppricevariations(t-1, t-2, t-3))
*Pricevariations(t-1, t-2, t-3)),
(ppublicityvariations(t, t-1, t-2, t-3))
*Publicityvariations(t, t-1, t-2, t-3)),
(psalesforcesvariation(t, t-1, t-2, t-3))
*Salesforcevariations(t, t-1, t-2, t-3)),
(ptrainingvariations(t, t-1, t-2, t-3))
*Trainingvariations(t, t-1, t-2, t-3))]
```

These calculations provide the market with demand <sup>fi</sup>gures for each company which will be set against the companies' real capability to respond. This is carried out in the company's Sales Module, where the basic process is the comparison of the company's market demand with actual <sup>fi</sup>nished goods inventory. If demand exceeds inventories, then the difference would be allocated to other competitors with available stock and similar market positioning. This demand readjustment process is carried out with a logical iterative algorithm involving <sup>fi</sup>fteen variables.

This step completes the Market Arbitrage Process and opens the procedure to generate Internal Information regarding the other areas of the company and culminates with the report generation process involving both internal and external information (production, human resources, <sup>fi</sup>nancial statements, market information, stock market, etc.).

## 4. SIMBA for business education

The evolution of information technology and communications, together with the new demands of higher education models (adaptation to different user pro<sup>fi</sup>les, distance learning, etc.) justify the development of new training tools, as is the case of SIMBA. Focusing more speci<sup>fi</sup>cally on the pedagogical advantages of business simulators, we must highlight “immersion learning” as a feature of this methodology. This means that students use techniques and concepts acquired during their training, and are required to analyze, make decisions and evaluate results, thus obtaining practical experience and strengthened knowledge. This feature is enhanced by the possibility to choose speci<sup>fi</sup>c intelligent agents to act as competitors, thus adapting market and competitors' behavior to the characteristics of the student group.

Table 2 Survey results.

<table><tr><td></td><td>Mean</td><td>Standard error</td><td>Median</td><td>Mode</td><td>Standard deviation</td></tr><tr><td>Generic competencies</td><td>4.21</td><td>0.1302</td><td>4</td><td>4</td><td>0.9108</td></tr><tr><td>Instrumental competences</td><td>4.14</td><td>0.1271</td><td>4</td><td>4</td><td>0.8897</td></tr><tr><td>Personal competences</td><td>3.82</td><td>0.1318</td><td>4</td><td>4</td><td>0.9226</td></tr><tr><td>Systemic competences</td><td>4.28</td><td>0.1316</td><td>4</td><td>4</td><td>0.9201</td></tr><tr><td>Specific competencies</td><td>4.20</td><td>0.1303</td><td>4</td><td>4</td><td>0.9121</td></tr><tr><td>Working with SIMBA</td><td>4.33</td><td>0.1324</td><td>4</td><td>4</td><td>0.8946</td></tr><tr><td>Usability</td><td>4.34</td><td>0.1424</td><td>4</td><td>4</td><td>0.9460</td></tr><tr><td>Simulator attractiveness</td><td>4.58</td><td>0.1184</td><td>4</td><td>4</td><td>0.8285</td></tr><tr><td>Adaptation to business reality</td><td>4.07</td><td>0.1364</td><td>4</td><td>4</td><td>0.8946</td></tr><tr><td>General valuation</td><td>4.69</td><td>0.1013</td><td>4</td><td>4</td><td>0.6792</td></tr></table>

So far, SIMBA has been used in business schools and training programs in which business administration is either a core or complementary content. In these contexts SIMBA has played two alternative roles. On the one hand, it has been an integrating activity for the participants—a “neutral” business environment in which they interact, get to know each other, and play different professional roles—and, on the other hand, it is a tool to relate concepts and put into practice the knowledge and techniques provided in other subjects.

In addition, there are many other bene<sup>fi</sup>ts derived from using simulators in business education. Some of them are related to technical learning objectives, while others deal with the development of capacities and competencies highly valued in modern education systems and business settings.

To contrast the pedagogical outcomes, goals and advantages of SIMBA, a survey has been conducted with students of four different programs of undergraduate, graduate and executive education aimed at providing a complete <sup>fi</sup>eld test, as a sample of the kind of participants the simulator is to focus on. Seventy-one respondents answered a questionnaire with three groups of questions about capabilities, competences, skills and qualities, to determinate the implications the work experience with SIMBA has on creativity, assessment criteria, interaction, discussion, knowledge acquisition, and cause–effect relations in all functional areas. The questionnaire included forty-seven questions, in a 1 to 5 range (Kevin scale) classi<sup>fi</sup>ed as follows:

\- Generic competences: a total of twenty questions related to:

• Instrumental competences: seven questions, about information analysis and synthesis, organization and planning work, situation diagnosis, problem solving resolution, decision system, resource management, and IT use.

• Personal competences: <sup>fi</sup>ve questions related to working in teams, multicultural and multidisciplinary competences, criticism and self-criticism, ethics at work, and work under time pressure.

• Systemic competences: eight questions focusing on autonomous learning, adaptation to new situations, creativity, leadership, entrepreneurship, quality motivation work, results orientation, and negotiation skills.

\- Speci<sup>fi</sup>c competences: eleven questions about understanding of the fundamentals of business administration, the relationship between the business units and organizational areas, methods and techniques in decision system, <sup>fi</sup>nancial and economic analysis, business strategy, forecasting and planning, and marketing; besides, there were two additional questions about the application of knowledge to practice, and cause–effect relationships.

\- Work experience with SIMBA:

• Usability: easy learning perception, screen and menus design, and generic technical use.

• Simulator attractiveness: <sup>fi</sup>ve questions related to learning motivation, team-work experience, entertainment quality, and contribution to learning business dynamic.

• Adaptation to business reality: <sup>fi</sup>ve questions about interactive learning, perception of general reality of markets and business, cause–effect relationships in decision-making, market strategy and environment evolution, and competence behavior reality.

\- Overall evaluation: just one question summarizes the participant's perception of working with SIMBA.

Results of statistical analysis are shown in Table 2. There are no signi<sup>fi</sup>cant differences among the different population test groups. In any case, the statistical results obtained show high means, low standard deviations and low standard errors. Statistically nonconsistent results requiring further analysis are related to several issues approached in the study:

\- Competences derived from IT use: the results are consistent with the good usability of SIMBA, and the IT previous level of the participants in the business simulation.

\- Personal competences: it seems to be complicated for participants to establish, set or prioritize aspects and competences derived from the multicultural and multidisciplinary, criticism and self-criticism, and ethics at work aspects of SIMBA. Given the international and multicultural usage scope of the simulator, its creators and researchers must <sup>fi</sup>nd new ways to measure such items.

\- High perception in the overall evaluation of SIMBA: results for this question are higher than the mean of the other items. This <sup>fi</sup>nding is consistent with the originality, fun, and immersion learning results associated with business games, not only SIMBA.

Finally, the main contributions of SIMBA in education are summarized in Table 3. All these advantages indicate that the business simulator SIMBA stands out as a powerful training tool, since it meets many of the demands set by best practice in education.

## Table 3

Contributions of SIMBA in education.

<table><tr><td colspan="2">Contributions of SIMBA in education</td></tr><tr><td>Learning objectives</td><td>Supplement theoretical training provided by conventional methods, strengthen the knowledge acquired.Acquire experience in decision-making practice without taking the risks of learning in real business situations.Self-confident handling of concepts and management techniques used in decision-making processes.Analyze the “cause-effect” relationship of decisions, that is, the market and business consequences of the actions taken by the participants.Understand the relationship between the various activities and functional areas of the company.Opportunity to learn from errors as a means of reinforcing learning.Allow students to familiarize themselves with business and economic terms in other languages.</td></tr><tr><td>Development of work abilities and skills</td><td>Develop management skills.Develop negotiation abilities.Time management.Develop workgroup and even intercultural and interdisciplinary abilities.Promote the use of the computer as a prime management work tool.</td></tr><tr><td>Teaching function</td><td>Enables the professor to follow up students’ involvement by checking connection time.Can be translated into several languages fostering the integration of foreign students, or even organizing international competitions.Allows the professor to plan very structured course content.Provides an efficient and objective evaluation system.Bridges the lack of “hands on training found in many educational programs.</td></tr></table>

![](/api/attachments/V5ECBFCV/fulltext/images/e8728942466c6fef2b862094b536b3c81a7544960b84028b8c88754f2bd6fcee.jpg)  
Fig. 3. MAS perspective of the business simulator.

## 5. SIMBA as a framework for business and arti<sup>fi</sup>cial intelligence research

A very important issue of SIMBA architecture is that humans can interact with autonomous agents. This section describes how SIMBA can be used for research in the application of AI, speci<sup>fi</sup>cally multiagent systems, to the area of business administration, which may provide us in the future with new methodologies for intelligent business and decision support systems. This means that SIMBA can include several autonomous agents to play the role of competing teams, and, based on the research on decision-making patterns of human teams, further research is made to improve the complexity and effectiveness of such intelligent agents.

The architecture of SIMBA enables us to use different players, including both software agents and human players. The different players participate in a simulation in a step by step round mode. In every step, the player (software or human) receives the current state of the environment and the player chooses the best decisions to make. Then the round proceeds. In this case, our architecture is based in a multi-agent system (MAS). Fig. 3 shows the architecture of the business simulator from a MAS perspective.

We have developed the Simulation Control (SC) and the agents using Java and secure sockets. The main components of the system are:

\- Simulation server: it receives the decisions of the software or human players following SOAP (Simple Object Access Protocol). In addition, once all decisions are taken for the current round, the Simulation Engine computes the values of variables in the marketplace for every player. Finally, the Simulation Server sends the results computed to each player. The player (software or human) uses these results to make the best decisions in the next round of the simulation.

\- Simulation control: it manages the software agents and their decisions. The simulation control receives the decisions taken by the software agents and sends them to the simulation engine. The simulation engine computes the results for every software agent and sends the results to the simulation control. The simulation control sends the results to the corresponding software agent.

\- Software agent: it represents an alternative to human players. In every step, the software agents receive the results computed for the simulation engine. The software agents use this information to take the decisions for the next round of the simulation.

We have developed three kinds of software agents as alternatives to human players. All the actions that these agents can perform are constrained by the semantic of the business model, so that we assume that the agents only take “in range” decisions.

\- Random agent: it chooses the best decisions to make using uniform random numbers. We use this agent to explore the action space.

\- Hand-coded agent: it sets decision variables increasing their values using the Consumer Price Index (CPI). Its behavior is more intelligent than that of the random agents.

\- Reinforcement learning (RL) agent: it uses the current state of the environment, action and rewards information for choosing the best decisions to make in every decision period.

Reinforcement learning is widely used in multi-agent systems in order to improve the behavior of the agents [1]. Among many different reinforcement learning algorithms, Q-learning [36,37] has been widely used. Q-learning is based on learning an action–value function, Q(s, a), that gives a utility measure of executing an action (or decision), a, from a situation or state, s. The update of such a function is performed following Eq. (1), where α is a learning parameter, and γ is a discount factor that reduces the relevance of future decisions. The Qlearning update function becomes as follows:

$$
Q (s _ {t}, a _ {t}) \leftarrow Q (s _ {t}, a _ {t}) + \alpha \left[ r _ {t + 1} + \gamma \max _ {a} Q (s _ {t + 1}, a) - Q (s _ {t}, a _ {t}) \right].\tag{1}
$$

Except in very small environments, it is impossible to enumerate the state and action space, and the Q function cannot be stored in a single table. The problem of learning in large spaces is addressed as generalization techniques. We skip the details of the learning process, since they are out of the scope of this manuscript. We compare the behavior of a reinforcement learning agent with the behavior of a hand-coded and random agent. In the evaluation, each of the agents plays against <sup>fi</sup>ve hand-coded agents that manage companies 2, 3, 4, 5 and 6. We perform simulations with 20 rounds or simulation periods. Fig. 4 shows these results.

Fig. 4 shows that random decisions make an agent decrease its performance. Both the hand-coded agent and the reinforcement learning agents are able to increase their pro<sup>fi</sup>ts, although the reinforcement learning agent obtains much better results from the early periods. The reinforcement learning agent obtains, after 5 years (or 20 simulation periods), a mean value for the result of the exercise of 5,973,019.70 €. The hand-coded agent obtains a result of 2,460,728.6 € and the random agent obtains a mean value of −2,041,121.82 €. These results show how the application of reinforcement learning can be useful for obtaining new behaviors that can outperform previous ones, and that SIMBA offers a multi-agent benchmark domain for the study, development and comparison of different reinforcement learning approaches, as well as other methods for autonomous decision-making.

![](/api/attachments/V5ECBFCV/fulltext/images/3fe0aa518a1937f028b6361e6c2974f1f646459c0d9b9cee491c793f0a48ae4a.jpg)  
Fig. 4. Results of random agent, hand-coded agent and RL agent.

## 6. Conclusion

This paper introduced SIMBA, a web-based business simulator, and describes its logical model, software architecture and main functionalities. We have found that SIMBA can be successfully used both for teaching and business practice.

From the perspective of training in Business Administration, we have shown that SIMBA offers several key advantages over traditional business teaching in different pedagogical areas, such as learning objectives, the development of work skills and the teaching function. SIMBA provides a level of complexity broad enough to have the students apply a scienti<sup>fi</sup>c approach in their decision-making processes, encouraging them to use multiple methodologies both in the <sup>fi</sup>eld of General Management and in the area of Management Science, especially Mathematical Programming and Simulation. SIMBA stands out as a powerful training tool, since it meets many of the demands set by best practice in education. Moreover, its playful and competitive qualities provide a high degree of satisfaction and involvement, both for the student and the professor. “Learning by playing” is the golden rule that guarantees success.

In contrast, the main challenges associated with the use of business simulators are the high development cost and the need for an effective training methodology to exploit their potential. Besides, it is necessary to train instructors in both the tool and the teaching methodology. It requires a minimum technological infrastructure and the activity becomes an intensive teaching experience when its use is complemented by mentoring support to participants. Even though the abovementioned bene<sup>fi</sup>ts have made simulators an innovative educational tool, the needs perceived in the educational market at all levels, and the continuous technological development and innovation in this type of tool, suggest new development trends:

\- Implement arti<sup>fi</sup>cial intelligence algorithms to improve the tool and, gradually, its behavior. We have shown that SIMBA architecture facilitates the use of the simulator to study different AI technologies. This is aimed, in short, at emulating users' behavior in the decision-making process, feeding this information back to the tool, thus making it more sensitive to participants' decision-making styles.

\- Access the descriptions and formulations of the different variables, concepts, and logical rules via hypertext techniques, linking information generated by the Simulator with the conceptual underpinnings and scienti<sup>fi</sup>c foundation in the Training Module.

\- Develop the Knowledge Module into a more sophisticated tool, allowing, on the one hand, the participant to perform a self-assessment of what they have learned, and, on the other, the instructor to track the participants' learning progress.

\- Apply videogame technology to obtain more realism in the simulator's business environment.

Thus, there is wide scope for continuing work in the <sup>fi</sup>elds of content design and technical improvement.

## Acknowledgements

This work has been partially sponsored by a regional project CCG08-UC3M/TIC-4141 of the Comunidad de Madrid, a national project TIN2008-06701-C03-03 of the Ministerio de Ciencia e Innovación of Spain and a contract with Simuladores Empresariales S.L.

## References

[1] E. Alonso, M. D Inverno, D. Kudenko, M. Luck, J. Noble, Learning in multi-agent systems, Knowledge Engineering Review 16 (3) (2001) 277–284.

[2] G.R. Andlinger, Business games—play one! Harvard Business Review 36 (11) (1958) 277–284.

[3] S. Bobek, I. Perko, Intelligent agent based business intelligence, Current Developments in Technology-Assisted Education 2 (2006) 1047-1051

[4] B. Brehmer, D. Dörner, Experiments with computer-simulated microworlds: escaping both the narrow straits of the laboratory and the deep blue sea of the <sup>fi</sup>eld study, Computers in Human Behavior 9 (1993) 171–184.

[5] T. Bui, J. Lee, Agent-based framework for building decision support systems, Decision Support Systems 25 (1999) 225–237.

[6] Frada Burstein, George Widmeyer, Decision support in an uncertain and complex world, Decision Support Systems 43 (4) (2007) 1647–1649.

[7] W.W. Cooper, H. Hemphill, Z. Huang, V. Lelas, S. Li, D. Sullivan, Survey of mathematical programming models in air pollution management, European Journal of Operational Research 96 (1996) 1–35.

[8] W.W. Cooper, H. Deng, B. Gu, S. Li, R.M. Thrall, Using DEA to improve the management of congestion in Chinese industries (1981–1997), Socio-Economic Planning Sciences 35 (2001) 227–242.

[9] A.G. Dale, C.R. Klasson, Business Gaming: A Survey of American Collegiate Schools of Business, Bureau of Business Research, University of Texas, Austin, TX, 1962.

[10] J.A. Dominguez Machuca, Improving POM learning: systems thinking and transparentbox business simulators, Production and Operations Management 7 (2) (1998) 210–227.

[11] A.J. Faria, W.J. Wellington, A survey of simulation game users, former-users, and never-users, Simulation & Gaming 35 (2) (2004) 178–207

[12] C. Farrell, Perceived effectiveness of simulations in international business pedagogy: an exploratory analysis, Journal of Teaching in International Business 16 (3) (2005) 71–88.

[13] J.W. Forrester, Industrial Dynamics, Mit press, Cambridge, Massachusetts, 1961.

[14] A. Größler, Methodological Issues of Using Business Simulators in Teaching and Research, System Dynamics Conference, 2000.

[15] A. Größler, E. Rouwette, J. Vennix, Exploring in<sup>fl</sup>uencing factors on rationality: a literature review of dynamic decision-making studies in system dynamics, System Research and Behavioral Science 21 (4) (2004) 351–370.

[16] K. Hemant, D. Bhargava, J. Power, D. Sun, Progress in web-based decision support technologies, Decision Support Systems 43 (4) (2007) 1083–1095.

[17] R.E. Horn, A. Cleaves, The Guide to Simulation/Games for Education and Training Sage Publications, Newbury Park, CA, 1980.

[18] W.N. Isaacs, P. Senge, Overcoming limits to learning in computer based learning environments, European Journal Of Operational Research 59 (1) (1992) 183–196.

[19] J.M. Kibbee, C.J. Craft, B. Nanus, Management Games, Reinhold Publishing Company, New York, 1961.

[20] M. Kobayashi, T. Terano, Exploring business gaming strategies by learning agents, Proc. 34th Conf. Int. Simulation and Gaming Assoc. (ISAGA) Social Contributions and Responsibilities of Simulation and Gaming, 2003, pp. 557–566.

[21] K. Kumar Ravulapati, J. Rao, A reinforcement learning approach to stochastic business games, IIE Transactions 36 (2004) 373–385.

[22] M. Laguna, J. Marklund, Business Process Modeling, Simulation and Design, Prentice-Hall, 2005.

[23] T.P. Liang, J.S. Huang, Framework for applying intelligent agents to support electronic trading, Decision Support Systems 28 (2000) 305–317.

[24] H.P. Luhn, A business intelligence system, IBM Journal of Research 2 (4) (2008) 314–319.

[25] K. McDonald, A. Wilmsmeier, D.C. Dixon, W.H. Inmon, Mastering the SAP business information warehouse, Chapter 1: The Origins of Business Intelligence, Wiley Publishing, 2004.

[26] M.J. McGuinness, A simulation game for an introductory course in international business, Journal of Teaching in International Business 15 (4) (2004) 47–66.

[27] A.C. Meier, W.T. Newell, H.L. Pazer, Simulation in Business Economics, Prentice-Hall Publishing Company, Englewood Cliffs, N.J., 1969.

[28] Chris Musselwhite, University Executive Education Gets Real, Training and Development Magazine 6 (2006) 57–59.

[29] S. Peterson, Software for model-building and simulation: an illustration of design philosophy, European Journal Of Operational Research 59 (1992) 197–202.

[30] G. Richardson, A.L. Pugh, Introduction to System Dynamics Modelling with DYNAMO, Mit Press, Cambridge, Massachusetts, 1981.

[31] C.M. Scherpereel, Changing mental models: business simulation exercises, Simulation & Gaming 36 (3) (2005) 388–403.

[32] H.A. Simon, A behavioral model of rational choice, Quarterly Journal of Economics 69 (1)(1955) 99–118.

[33] T. Sueyoshi, G.R. Tadiparthi, An agent-based approach to handle business complexity in US wholesale power trading, IEEE Transactions on Power Systems 22 (3) (2007) 532-543

[34] T. Sueyoshi, G.R. Tadiparthi, Why did California electricity crisis occur?: a numerical analysis using multiagent intelligent simulator, IEEE Transactions on Systems, Man and Cybernetics Part C: Applications and Reviews 38 (6) (2008) 779–790.

[35] T. Sueyoshi, G.R. Tadiparthi, An agent-based decision support system for wholesale electricity market, Decision Support Systems 42 (2008) 425–446.

[36] G.J. Summers, Today's business simulation industry, Simulation & Gaming 35 (2) (2004) 208–241.

[37] R. Sutton, R.G. Barto, Reinforcement Learning: An Introduction, MIT Press, Cambridge, Massachusetts, 1998.

[38] JA Achievement, JA TITAN. The ultimate business simulator (2000). http://titan.ja.org/.

[39] J. Wolfe, A history of business teaching games in English-speaking and post-socialist countries, Simulation & Gaming 24 (1993) 446–467.

[40] M. Wynder, Facilitating creativity in management accounting: a computerized business simulation, Accounting Education 13 (2) (2004) 231–250.

[41] B.P. Zeigler, Theory of Modelling and Simulation, Krieger Publishing Co. Inc., 1984.

Fernando Borrajo holds a Ph.D. in Business Administration by the Universidad Autónoma de Madrid (UAM), and Master in Quantitative Finance by EFA. Actually an associate full time professor in Strategic and Business Organization at UAM, where he is Director of Master of Business Administration (Executive) and Director of Doctorate Program of Financial Economics.

Yolanda Bueno holds a degree in Business and an MBA by the Universidad Autónoma de Madrid (Spain). Now she is a Collaborator Professor in Business Organization at UAM, where she is currently Vicedean for Students at the Faculty of Economics. Her professional activity at the university is research, teaching and consulting in the areas of Management Science and Operations Management. This professional expertise has been applied, amongst other results, to the design and development of several Business Games, both as training and research tools.

Isidro de Pablo holds an MBA by the State University of New York, and a Ph.D. in Business Administration by the Universidad Autónoma de Madrid (UAM), Spain. Now he is a full professor in Business Organization at UAM, where he is currently in charge of the Center for Entrepreneurial Initiatives (CIADE). His professional background starts in the Auditing and Management Information Systems Consulting practice until his incorporation to the university where he has developed an intensive research, teaching and consulting activity in the areas of MIS, General Management and Entrepreneurship. This professional expertise has been applied, amongst other results, to the design and development of several Business Games, both as training and research tools. He is the founder of Simuladores Empresariales, S.L. the spin-off company from the UAM specialized in business games development.

Begoña Santos holds a Ph.D. in Economics and Business by the Universidad Autónoma de Madrid (UAM), Spain. Now she is a professor in Business Organization at the Faculty of Economics of the UAM. Her professional activity at the University is research, teaching and consulting in the areas of Management Information Systems. This professional expertise has been applied, amongst other results, to the design and develop ment of several Business Games, and she has given numerous seminars with this tool in Business School and in-Company Programs. She is one of the founders of Simuladores Empresariales S.L., a spin-off company of the UAM dedicated to developing simulators.

Fernando Fernández is a faculty of the Computer Science Department of Universidad Carlos III de Madrid, since October 2005. He received his Ph.D. degree in Computer Science from the University Carlos III of Madrid (UC3M) in 2003, He received his B.Sc, in 1999 from UC3M, also in Computer Science. He was a postdoctoral fellow at the Computer Science Department of Carnegie Mellon University since October 2004 until December 2005. He is the recipient of a pre-doctoral FPU fellowship award from the Spanish Ministry of Education (MEC), a Doctoral Prize from UC3M, and an MEC-Fulbright postdoctoral fellowship. He is interested in intelligent systems that operate in continuous and stochastic domains

Javier García received his B.Sc, in Computer Science in 2006 from the Universidad Carlos III de Madrid (UC3M), Spain. He is currently a Ph.D. student in the Computer Science Department at UC3M. His research interests include machine learning, reinforcement learning and multi-agent systems.

Ismael Sagredo received his B.Sc. in Computer Science in 2006 from the Universidad Carlos III de Madrid (UC3M), Spain. He is currently an M.Sc. student in the Computer Science Department at UC3M. His research interests include instance based learning machine learning and multi-agent systems.
