---
otero_id: 13470
otero_key: "YD7SGBF4"
title: "Situated DSS for personal finance management: Design and evaluation"
authors: "Rustam Vahidov; Xin He"
year: "2010"
journal: "Information & Management"
doi: "10.1016/j.im.2009.11.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Situated DSS for personal finance management: Design and evaluation<sup>§</sup>

Rustam Vahidov \*, Xin He

Department of Decision Sciences & MIS, John Molson School of Business, Concordia University, Montreal, QC, Canada

## A R T I C L E I N F O

Article history: Received 1 December 2007 Received in revised form 21 October 2008 Accepted 22 June 2009 Available online 12 November 2009

Keywords: Situated DSS Personal finance management Layered architecture Experimental studies

## A B S T R A C T

The Situated Decision Support System (SDSS) model is a type of DSS that maintains close links with the target environment and has capabilities for sensing, monitoring, decision support, and limited decisionmaking, action generation, and implementation. But though a generic description of SDSS had been provided, no empirical test has been made to prove its value. We performed experiments using human subjects to test an SDSS prototype. Personal finance management was chosen as an application domain, and the design and implementation of the SDSS prototype is discussed. The experiments involve subject who carry out their normal shopping tasks in a simulated setup. One group of subjects was provided with SDSS support, while the others used a traditional decision support model. Overall, the results attest to the superiority of the SDSS model in terms of key decision performance variables.

\- 2009 Elsevier B.V. All rights reserved.

## 1. Introduction

DSS have been traditionally been defined as interactive computer systems that help users make decisions. In the past, they were primarily conceived as ‘‘mind-expanding’’ tools for assisting managers in organizations. With the fast advance of computer and Internet technologies and the rapid growth of available information, the scope of decision support has expanded to satisfy an individual’s needs in decision-making. However, the traditional DSS offers mostly passive support, in which the decision-making process is isolated from the environment and depends on the decision maker’s intuition.

In today’s complex and dynamic environment, passive types of support are no longer sufficient to meet decision makers’ needs. To meet the new challenges, a situated DSS (SDSS) model was introduced by one of the authors [11]. It builds on a paradigm of direct and active interaction with the problem environment, facilitating problem identification, diagnosis, decision support, and action implementation and subsequent monitoring.

While the original generic model of an SDSS introduced a formal description of its capabilities and components, no empirical assessment of its benefits have yet been made. We decided to develop a prototype and application demonstrating the key features of an SDSS as a basis to test it in experimental settings.

To this end we have selected the problem of personal finance management. On the one hand, this could assist individuals better achieve their financial goals, and on the other help maintaining a healthy economy. Financial institutions could offer their clients a way of better managing their funds. Here, the traditional form of support for personal finance management was compared against the SDSS approach.

## 2. Background

DSS are one of the most popular software components today. Recently, improvements in communication technology have led to a business environment that is more complex and connected. As market conditions change, timely decisions need to be made using the most up-to-date information.

To some extent, a real-time DSS (RDSS) is better suited in the new networked environment. Its aim is to provide up-to-date information, and ‘‘guarantee end-to-end response time’’ to decision makers [2]. It is characterized as continuously monitoring the environment, gathering timely data from managed systems, and quickly generating views appropriate and useful for decision makers in making timely decisions.

Another stream of research looked to overcome the passive nature of traditional DSS. The ‘‘active’’ DSS (ADSS) model promotes active participation by the system in the decision-making process. The user is no longer the only party that takes the initiative; the system would be able to invoke decision-related tasks without receiving a specific command [1]. A recent study found that DSS users who do not have system expertise perform worse and are confused about the use of the system [7]. Thus, active DSS approaches might help alleviate cognitive burden on decision makers and promote system adoption.

Proactiveness and autonomy are among the key features of software agents, which perceive their environment through sensors and act upon it through effectors. It is, thus hardly surprising that researchers have tried to incorporate agent models to devise new types of DSSs; one such agent-based model was proposed in [5]. In it, the agents were organized around the key traditional components of DSS, including data, model, and dialog subsystems. An agent-based DSS for stock trading was described in [8]; in this system, agents monitored the status of stocks continuously and communicated with users to collect requests and deliver results. Agent-based simulations have also been used as part of DSS modeling capabilities. For example, multi-agent simulations were utilized for the analysis of the wholesale electricity market in the US [10].

However, care must be exercised to avoid too much automation. Agents are suitable for well-structured tasks, but excessive automation may lead to a mismatch between ill-structured decision-making situations and the autonomous functioning of the tools.

SDSS was an attempt to combine the major features of the realtime and active DSS [14]. It is connected to the environment, and responds to changes by automating work within the limits of its delegated authority. The term ‘‘Situated’’ was borrowed from agent definitions; it emphasizes the fact that the DSS is intimately linked to, and is part of the problem domain. In addition to the components of traditional DSS, an SDSS has sensors and effectors which closely and actively link the system to its problem environment. A SDSS constantly senses the problem area, generating alerts, utilizes data, models and knowledge to provide decision support, implements decision on behalf of the user, and monitors the results.

An application of an SDSS model that can manage multiple negotiations has been proposed in [12]. While the generic architecture and formal description of the SDSS was provided, no empirical work has yet been done to prove the value of these systems for decision makers.

## 3. Personal finance management

Personal finance management (PFM) is becoming useful to the general public suggesting that decision support should be extended to individuals. Financial institutions could offer free PFM services to their customers to win their loyalty. A recent report on family finance indicated that the saving rate of Canadian families fell from 13% in 1989 to 2.1% in 2003, and the annual saving level in 2003 was only one quarter of that in the early nineties [9]. In 2005, the saving rate in the US sank to -0.5% [15].

To stop spending too much and saving too little, one not only needs to perform adequate planning and budgeting, but also to control spending, and follow the plan. Without proper management, it is difficult for individuals to adhere to a financial plan. PFM involves a number of important tasks, such as planning and budgeting, cash flow control, investment, taxation, and insurance. Specialized courses and software tools have been designed to help people manage their personal finances. PFM packages currently available include Microsoft Money and Quicken. While these software programs help people manage bills, organize taxes, and optimize investment portfolios, an SDSS could actively support users in setting up realistic financial goals and budgets, react to change, actively monitor the implementation of the plans and communicate with the user if significant changes are required. It would not only actively support the user in planning, but also attempt to minimize any deviation between what was planned and what is happening.

## 4. An SDSS for personal finance management (PFM)

## 4.1. A layered model of an SDSS

The generic architecture of an SDSS consists of four major components: Sensors and Effectors are components for detecting change in the environment, and for reacting to the change; the Kernel contains the essential parts of a traditional DSS. The Manager component of the kernel continuously assesses the environment, generate corrective actions as necessary, or informs the user and initiates the decision support process if this is within its span of authority. The Active User Interface is intended to model a user’s preference and deliver signals, recommendations, and decisions from other components.

To simplify the assignment of the tasks to different parts of the SDSS we proposed a layered model for it. The InteRRaP agents combined the features of both reactive (stimulus-response) and deliberative (planning) models [4]. The architecture contained three layers: one for reactive action, one for deliberative actions, and one for cooperative actions.

We separated the components into three layers: reactive, which included the sensors and effectors; operational, which contained the DSS kernel; and judgmental, which included the active user interface and the user (Fig. 1).

The reactive layer can access information from the sensors in the environment, process it, generate alerts when immediate action is required, adapt to different environments, and make plans. Effectors can implement the decision and obtain additional information as necessary. If immediate action is required, quick decisions can be made by sensors and implemented by effectors.

The operational layer contains the DSS kernel, which includes the traditional DSS components (data, models, and knowledge) and the manager. Data, models, and knowledge are its passive elements, and the DSS manager is the active component. In this layer, data is stored, information is analyzed, alternative solutions are generated, and recommendations are made. The DSS manager performs the analysis of the situation and generates decisions without the user’s direct command (within the predefined limits of its authority). If there is a need for human involvement, the judgmental layer will be invoked by the manager.

The user’s involvement is the key difference between DSSs and autonomous agents. The active user interface is an intermediary between the decision maker and the system. It transfers input from the user to the system and output from the system to the user. It generates alert signals to the user and queries for additional information, if necessary. It also maintains and updates the user’s profile in order to personalize the communications and provide decision-making support. In a nutshell, the reactive layer handles simple tasks, the operational layer targets more complex, but structured ones, and the judgmental layer is for less structured tasks.

## 4.2. Design method

Here, we outline the design method for SDSS and illustrate its application to PFM.

1. Define the scope of the decision problem. Make an overall analysis to define the decision problem. Thus, we scan the environment to decide what major decision and implementation tasks must be supported by the SDSS.

2. Identify the decision task breakdown structure. In this step, one needs to break down the decision problem into subtasks. This results in a tree-like structure, where the subtasks, are further divided into smaller subtasks.

3. Assign the tasks to one of the three layers of the SDSS. Tasks that are associated with the problem environment, such as sensing and reacting to change in the environment, should be assigned to the reactive layer. Tasks involving detailed analysis, computation, proposing alternatives, and generating reports, should be assigned to the operational layer. Tasks that involve the user and communication between the user and the system should be assigned to the judgmental layer.

![](/api/attachments/YD7SGBF4/fulltext/images/1d8db1f2c3b5a4333d590be482799b6ccec74886d739c375a578eaea6aea1b8c.jpg)  
Fig. 1. A layered model of an SDSS.

![](/api/attachments/YD7SGBF4/fulltext/images/b3020a6de1658d5b44dee6a0cd2656e881a72f8c6e305904583eb6228a68b678.jpg)  
Fig. 2. Breakdown structure of PFM and its main aspects.

4. For each task, define coordination requirements with other components. Tasks have now been assigned to one of the three layers but were not isolated. Therefore, methods of communication, flows of information, and operations of coordination must still be defined before development.

5. Design and implement the components. Once the scope of the problem has been identified, tasks and their coordination have been defined, and we can develop each component and implement it into a system.

## 4.3. Application of the design method to PFM

The scope of the system includes the major domain areas of PFM: financial planning, banking, investments, insurance, and taxation. These can be further broken down into subtasks. Fig. 2 shows the tree-like structure of PFM and its major aspects. Fig. 3 shows the subtasks of each major aspect.

After the subtasks have been identified, they are assigned to one of the three layers. Table 1 shows the allocation. Budgeting, for example, is assigned to the judgmental layer. The task of generating alternative budgets is allocated to the operational

Table 1

Allocation of subtasks.

<table><tr><td>Major task</td><td>Judgmental</td><td>Operational</td><td>Reactive</td></tr><tr><td>Planning</td><td>Developing financial goals; budgeting; revising financial goals; revising budget</td><td>Generating alternative budgets; assessing feasibility of goals; assessing spending pattern; generating periodical reports</td><td>Tracking spending; generating alerts; recommending corrective actions</td></tr><tr><td>Banking</td><td>Managing bank accounts; scheduling transactions; transferring money</td><td></td><td>Executing scheduled transactions; executing money transfer</td></tr><tr><td>Investing Insurance</td><td>Deciding on investment plan Developing insurance goals; developing insurance plan</td><td>Proposing investment plan; generating investment reports Proposing alternative insurance plans</td><td>Executing investment plan Scheduling insurance payments; finding insurance providers&#x27; information; monitoring insurance providers</td></tr><tr><td>Taxes</td><td>Preparing income tax return</td><td>Producing income tax return</td><td>Sending income tax return to governments</td></tr></table>

![](/api/attachments/YD7SGBF4/fulltext/images/eb968a58a1f6fee7362179c58e0c034e704bb82158b837e84fd00bbff154c560.jpg)  
Fig. 3. Breakdown structures of the main aspects.

layer because analysis and calculation are performed by the DSS kernel. Tracking spending is assigned to the reactive layer. The sensors monitor the user’s spending activities and generate alerts if necessary. Effectors are responsible for various execution tasks, such as automatic money transfer.

Coordination here is achieved by assigning specific subtasks to different components and exchanging information between them. There are four types of information being exchanged: (1) information collected from the environment by the sensors; (2) messages used to communicate with other components; (3) information exchanged between the active user interface and the user; (4) and information passed to the environment. We adopted an XML-like syntax for message exchange. For example, for the subtask of financial planning, one type of messages exchanged between sensors and the active UI are observations of abnormal spending. The structure of this type of message is presented in Fig. 4.

The first three lines in this message give the message ID, the sender, and the receiver. The <infotype> tag contains the body of the message. Tag <typ1> indicates the type of message, which here is observation. The body of the <activity> tag is the content of the message. From the content, the active UI can recognize that this is a message about overspending. The category in which overspending happens is ‘‘c1’’. The amount of overspending is \$170, and this event took place on April 21, 2006. ‘‘<action>infoImme</action>’’ indicates that the active UI should inform the user immediately about this.

## 5. SDSS prototype for PFM

To illustrate our approach and investigate the effectiveness of the SDSS, we developed a web-based prototype of PFM; it was developed for one of the major areas: financial planning. Effective planning includes setting up realistic financial goals, building feasible financial budgets, and implementing them in order to keep the goals reachable. The purpose of the prototype SDSS was to assist the user in setting up realistic financial plans and to guide him/her through the implementation process. The scenario began with activities pertaining to the development of feasible financial goals and budgets, including such items as retirement, children’s education, purchase of a house etc., along with the time horizon for each of them. The goals play a key role in further budget implementation monitoring with the user receiving periodical reports and alerts in case of significant variation.

The feasibility of financial goals is assessed against the userdefined budget in the operational layer (Fig. 5). If some goals cannot be reached, the DSS kernel will attempt to generate alternative budgets which are feasible. If no alternative budget can be generated an alert is sent to the judgmental layer where the user is asked to revise his/her goals and budget. If goals are feasible the system suggests four alternative budgets for consideration in addition to the one defined by the user (Fig. 6). The purpose of generating alternative budgets is to allow users to explore other options and invest their money with different levels of risk and surplus, while keeping their goals reachable. The risk level is determined by the allocation of money invested in the categories of stock, bond, and risk-free investments.

The alternative budgets are generated based on three criteria:

 make sure the user can meet all the predefined goals;

 take the categories’ flexibility into account; and

 let the user choose from budgets involving different risk and surplus levels.

![](/api/attachments/YD7SGBF4/fulltext/images/99508909ee5999fafe84fc7ea18e636b90690bf293a65b98c8c69f81db3cb1ce.jpg)  
Fig. 4. Message of abnormal observation

This is based on an expectation that generating diverse alternatives improves the overall decision-making; this approach has been used in the past for DSSs using Genetic Algorithms [3] and agent technology [13].

Each candidate budget should next be evaluated against the expected achievement of future goals. This procedure tries to ensure that all goals are met. The budgets differ by the manipulation of the resulting surplus and risk to set up concrete objective functions for each budget. The actual amounts suggested for each category in the budget are found by iterative optimization (hillclimbing) with consideration of the flexibility of the spending in a category where a flexibility of 0 means that the spending cannot be altered. The major simplification is the assumption of a more or less stable financial situation, in order to alleviate the experimental task for the subjects. The budget chosen by the user is stored as a baseline for future monitoring of the user’s financial behavior.

During the normal spending period, the sensors in the reactive layer monitor the user’s activities. The actual spending is sent to the operational layer for assessment. If significant variation is observed, alerts will be sent to the user. Each month a report is generated by the DSS kernel in the operational layer. The report tells the user how well he/she followed the budget and if his/her goals are still feasible with the current spending pattern. While observing the user’s spending, the DS manager processes the observation and updates the user’s data in the database. Every three months a quarterly report (Fig. 7) is presented to the user. The report summarizes how well the budget was followed. If the actual spending deviated significantly from the budgeted one, the DS manager would proactively generate another set of budgets for the user to consider.

In generating new alternative budgets, the system attempts to incorporate the information from the observed behavior of the user. The new estimated spending in each category is determined by exponential smoothing considering the planned and actual amounts. From these estimates, the new set of budgets is evolved; these, are supposed to be close to the user’s actual behavior, and thus are more realistic

## 6. Evaluation

## 6.1. Hypotheses

The SDSS provides effective decision support by sensing what is going on in the problem environment, utilizing DSS facilities to generate alternatives while undertaking and monitoring implementation. In doing so, it offers active support to decision makers in real-time.

Our research model includes the type of DSS as an independent variable and the user’s ‘‘degree of activeness in financial planning’ as a moderating variable. The effectiveness of the DSS is determined by the decision outcome and subjective variables. Our hypotheses therefore are:

<table><tr><td>Category</td><td>Description</td><td>Expected value</td></tr><tr><td>Income</td><td>Your totalmonthly net income, includes salary, scholarship, bursary, support from parents or spouse, etc.</td><td>$3000</td></tr><tr><td></td><td></td><td></td></tr><tr><td>Housing</td><td>Monthly rent, mortgage payments... The fixed amount you have to spend every month for your housing.</td><td>$700</td></tr><tr><td>Transportation</td><td>Automobile loan payments, gas, licenses, other transportation</td><td>$50</td></tr><tr><td>Food</td><td>Food from supermarkets or groceries</td><td>$200</td></tr><tr><td>Utilities</td><td>Telephone, electricity, water, cable TV, Internet, etc</td><td>$150</td></tr><tr><td>Insurance</td><td>Insurance payment</td><td>$100</td></tr><tr><td>Entertainment</td><td>Books, music, movie, etc</td><td>$100</td></tr><tr><td>Fashion</td><td>Clothes, shoes, etc</td><td>$200</td></tr><tr><td>Dining out</td><td>Fast food, coffee, restaurants</td><td>$100</td></tr><tr><td>Supplies</td><td>Bathroom paper, shower lotion, etc</td><td>$50</td></tr><tr><td>Remainder</td><td></td><td>$1350</td></tr></table>

Fig. 5. User-defined budget

![](/api/attachments/YD7SGBF4/fulltext/images/17496e10131d8e9d0950a00f31641cb2035974dac9a2b7d87e061ce0a0837c0e.jpg)  
Fig. 6. Suggested budgets.

H1. SDSS users will have greater projected achievement of goals than TDSS users. The achievement of financial goals is the number of goals a user can reach after determining the budget. Since the goals could be set up many years in advance, we used the ‘‘projected’’ achievement, i.e. the predicted achievement if a given spending behavior continues in the future. If a user overspends, some financial goals will not be feasible.

H2. SDSS users will show more improvement in projected achievement of goals than TDSS users. [The improvement in achievement of goals being defined as the increase in the number of goals a user can reach during some period of time]. SDSS not only helps the users set up financial goals but also provides active and timely support to help them keep their goals feasible.

H3. The proportion of SDSS users who can achieve all of their financial goals is larger than the proportion of TDSS users who can. A user’s ultimate objective is to realize all the financial goals. If more users can reach all of their goals by using the system, the system is considered more helpful.

![](/api/attachments/YD7SGBF4/fulltext/images/14d317507a20faab9a91de822984ecd99bfa36ad47c1d8f18c5bb058d5f5cf70.jpg)  
Fig. 7. Quarterly report.

H4. SDSS users will improve more in following a budget than TDSS users. The improvement is defined as the increase of the consistency between the spending activities and the budget. The SDSS encourages the users to set up realistic budgets and tries to minimize the deviation between what was planned and what is happening.

H5. The perceived usefulness of an SDSS is higher than that of a TDSS.

H6. The perceived ease of use of an SDSS is not lower than that of a TDSS.

H7. SDSS users will have more satisfaction with the decision process than TDSS users.

The main purpose of an SDSS is to assist users in finding the most reasonable budget and implement it successfully. Users who are active in financial planning are more willing to plan for their goals and more likely to review the progress frequently. For users not active in financial planning, the SDSS may provide support to help them set up financial goals and a budget, and provide constant support during the implementation process. For active financial planners, the support provided by the system may thus be less valuable.

H8. Passive financial planners will perceive SDSS as more useful, easier to use, and providing higher satisfaction with the process than active financial planners.

## 6.2. Measures

Objective measures. The achievement of goals was measured by the average percentage of the goals projected to be achieved in the three-month period. The improvement of goal achievement was measured as the average difference of the percentage of goals achieved between months. The proportion of users who could achieve all the goals was measured by dividing the number of users who could achieve all the goals by the total number of users. Finally, the improvement in following a budget was calculated as follows: we first calculated the deviation of the actual spending and the budget for each month. Then we calculated the difference between these deviations. The value of improvement was obtained by calculating the average of these differences.

Subjective measures. The subjective measures used to gauge the effectiveness of the system were perceived usefulness (PU), perceived ease of use (PEU), and satisfaction with the process (US). Whether a system is effective or not depends on how people perceive the quality of the assistance or support that they have received. To get this information, we used self-reporting measures because they collected people’s opinion directly.

The measures of PU and PEU were adopted from the old TAM model [8]. We employed the six items (seven-point Likert scale from ‘‘strongly disagree’’ to ‘‘strongly agree’’) for the measure of PU and three items for PEU. The measure of US included three items.

A measure of ‘‘activeness of financial planning’’ was created by using two indicators: the frequency of financial planning (measured with self-reported frequency on a 4-point scale (‘‘never’’, ‘‘less than 1 time a year’’, ‘‘1 to 3 times a year’’, and ‘‘more than 3 times a year’’)), and similarly the frequency of evaluating financial plans was measured by a self-reported frequency of a 6-point scale (labels: ‘‘never’’, ‘‘less than 1 time a year’’, ‘‘1 to 5 times a year’’, ‘‘5 to 10 times a year’’, ‘‘1 time a month’’, and ‘‘more than once a month’’).

## 6.3. Experiments

We performed empirical experiments to investigate the effectiveness of the SDSS prototype, comparing the performance and the user’s experience of the SDSS with that of a TDSS, which was a subset of the SDSS that included data, models, and interface. The data in the TDSS included the user’s financial goals, self-defined budget, and actual activities. The models in the TDSS allowed calculations that assessed the feasibility of financial goals based on the self-defined budget, and the difference between actual activities and the self-defined budget. The interfaces for developing financial goals and budgets were similar to those in the SDSS. The interfaces also allowed viewing of the assessment of goals and the difference between activities and budget. Overall, we tried to match the functionality of the TDSS with the existing PFM packages.

The participants included undergraduate and graduate students from a major North American business school. Participants were randomly assigned to one of the two treatments. Before they started the experiment, a brief introduction was given by the instructor. Detailed written instructions on how to use the system were also given to the participants, and they were required to read it carefully before they started the experiment.

The experimental task involved selecting and following a feasible budget. Prior to the selection, participants were asked to set up their financial goals, monthly budget, and investment. For the group of SDSS users, the system then evaluated the feasibility of goals based on the self-defined budget and proactively generated four alternative budgets. Once the participants chose a budget, they were invited to indicate their normal spending week by week in a simulated environment. The use of simulations instead of actual spending behavior was dictated by the ethical and legal problems related to monitoring their spending behavior.

During the simulated period, the SDSS monitored the participants’ activities and generated alerts and reports. The TDSS users could invoke functions such as comparing the planned and actual spending, assessing the projected achievement of goals, etc. After three (simulated) months, the TDSS generated a detailed report which included the differences between the budget and the actual activities, and the evaluation of the activities based on the user’s financial goals.

To monitor a user’s spending pattern, we created a simulated environment, which allowed participants to do their shopping activities in the lab environment. We simulated twelve weeks of shopping activities in five categories of spending activities: food, dining out, entertainment, supplies, and clothing (fashion). The actual experiment duration was restricted to a maximum of two hours. The categories of activities contained the major shops that belonged to these categories. For example, the category of entertainment included going to clubs, bars, and movie theatres. To increase the sense of reality, instead of the name, we used the store’s logo to represent a store. Subjects who normally do shopping in these stores are very familiar with the logo. The amount of money subjects spent in each shop was calculated automatically. A typical individual’s spending was set as the mean, and the actual spending was randomly distributed around the mean.

Subjects visited the stores by clicking on the logo. Once the logo was clicked, the amount of money spent was determined by the system and shown to the subject. As the subject visited more stores in the category, he/she would be informed of the total amount of money spent for the category. Fig. 8 shows a screenshot of the simulated shopping.

## 7. Results

A total of 68 subjects participated in the experiment. Two of them did not complete the experimental task and were thus considered non-responders. The remaining 66 sets were retained for further analysis. Among these participants, 38 were male and 28 were female. The average age of the participants was 29 years and the average computer experience was 6.8 years. The average

![](/api/attachments/YD7SGBF4/fulltext/images/c7c32c88c04d8da8c60af9475810066b9cf65f5d2574ddc511e79c0a278ba81b.jpg)  
Fig. 8. Simulated shopping

Table 2 Factor loadings.

<table><tr><td>Items</td><td>PU</td><td>PEU</td><td>US</td></tr><tr><td>PU1</td><td>0.822</td><td>0.232</td><td>0.421</td></tr><tr><td>PU2</td><td>0.811</td><td>0.305</td><td>0.302</td></tr><tr><td>PU3</td><td>0.651</td><td>0.315</td><td>0.378</td></tr><tr><td>PU4</td><td>0.640</td><td>0.095</td><td>0.454</td></tr><tr><td>PU5</td><td>0.609</td><td>0.404</td><td>0.343</td></tr><tr><td>PU6</td><td>0.603</td><td>0.491</td><td>0.187</td></tr><tr><td>EU1</td><td>0.462</td><td>0.610</td><td>0.084</td></tr><tr><td>EU2</td><td>0.096</td><td>0.790</td><td>0.215</td></tr><tr><td>EU3</td><td>0.326</td><td>0.677</td><td>0.281</td></tr><tr><td>SP1</td><td>0.365</td><td>0.071</td><td>0.708</td></tr><tr><td>SP2</td><td>0.280</td><td>0.345</td><td>0.749</td></tr><tr><td>SP3</td><td>0.300</td><td>0.355</td><td>0.755</td></tr></table>

Internet usage experience was 6.5 years. Thus, the participants had no trouble in interpreting and using the web-based systems. Out of the total of 66 subjects, exactly half were assigned to the treatment group, and the rest were assigned to the control group.

Reliability of the subjective measures was assessed by the Cronbach’s alpha and found to be adequate (0.93 for PU; 0.807 for PEU; and 0.874 for US). Exploratory factor analysis was conducted to examine the validity of the measures. The loadings revealed reasonable degrees of convergent and discriminant validities (Table 2).

Participants were classified as either active or inactive based on a median split of their combined activeness scores.

The level of goal achievement was measured by the average percentage of achievable goals in the period of three months. To test hypothesis H1, we used the Mann–Whitney Test. The results (Tables 5 and 6) showed that the level of goal achievement accomplished by SDSS users (mean rank 42.2) was significantly higher than that achieved by the TDSS users (mean rank 24.9, p = 0.000). Therefore, hypothesis H1 was supported.

Hypothesis H2 was tested by using an independent samples ttest. The result suggested that the improvement achieved by the SDSS user was higher than the TDSS user (0.062 vs. 0.021). However, as shown in Table 8, the result was only significant at the 0.10 level (p-value = 0.09).

For hypothesis H3, we obtained a z-score of 3.81, and a p-value of 0.00, which suggested that hypothesis H3 was supported. Hypotheses H4 was tested by an independent sample t-test. Results showed that H4 had been supported (49 vs. 31, with a pvalue = 0.025). Thus, the basic hypotheses comparing two systems in terms of objective measures were supported.

For the subjective variables the t-tests were conducted using factor scores. Results indicated that PU for SDSS users was significantly higher than that for TDSS users (p-value = 0.037), while there was no significant difference in terms of PEU (pvalue = 0.19) and satisfaction with the process (p = 0.27). The lack

## Table 3

Summary of hypotheses testing.

<table><tr><td>Hypothesis</td><td>SDSS mean</td><td>TDSS mean</td><td>P-value</td><td>Confirm. (α=0.05)</td></tr><tr><td>H1 - goal achievement</td><td>42.2</td><td>24.9</td><td>0.00</td><td>Yes</td></tr><tr><td>H2 - improvement of goal achievement</td><td>0.062</td><td>0.021</td><td>0.093</td><td>Yes</td></tr><tr><td>H4 - budget improvement</td><td>49.1</td><td>31.1</td><td>0.026</td><td>Yes</td></tr><tr><td>H5 - perceived usefulness</td><td>0.220</td><td>-0.220</td><td>0.037</td><td>Yes</td></tr><tr><td>H6 - perceived ease of use</td><td>-0.109</td><td>0.109</td><td>0.191</td><td>No</td></tr><tr><td>H7 - process satisfaction</td><td>0.078</td><td>-0.078</td><td>0.265</td><td>No</td></tr><tr><td>H8 - effect of financial planning activeness</td><td></td><td></td><td>PU: 0.222, PEU: 0.446, SP: 0.194</td><td>No</td></tr><tr><td>H3 - users proportion</td><td colspan="2">z-score: 3.8</td><td>0.000</td><td>Yes</td></tr></table>

of significant difference between the subject groups regarding ease of use may be attributed to the fact that both prototypes had similar user interface layouts and elements. No difference in US with the process was puzzling. Apparently, while the subjects found one system significantly more useful, both groups were equally satisfied with their interaction (mostly in shopping) In summary, only one hypothesis found significant support. Table 3 summarizes the results of hypotheses testing.

## 8. Conclusions

The purpose of this work has been the empirical assessment of the value of S decision support model. We proposed a layered model of SDSS which contains a reactive layer, an operational layer, and a judgmental layer. We chose PFM as an application domain for the SDSS. Using a proposed method we assigned various PFM tasks to different layers of the system. We further have built a prototype supporting the planning task of PFM. Our experiments have revealed the improvement of the PFM indicators for the subjects using SDSS. Also, there was some evidence regarding positive subjective assessments of the SDSS model as compared with the traditional means.

These findings provide first empirical support for the value of SDSS model. Furthermore, they also have significant implications for the researchers interested in systems for support of PFM: an area, which has been largely overlooked in the past.

There are some limitations of the study. First, we only implemented one aspect of PFM in the prototype systems. Another limitation concerns the use of a simulated environment instead of observing actual activities. One more issue concerns our experiment design; no performance-based incentives were offered to our subjects. However, the effectiveness of using monetary incentives has been called into question. Specifically, the tasks studied and the outcomes involved in incentivized studies can fail to be either realistic or relevant.’’ In particular, real-world decisions usually involve both gains and losses, but monetary incentives are only one way.

Another concern is in the choice of students as subjects and the use of measures related to TAM. A recent study found the constructs to be invariant and valid across different respondent groups including subgroups of different age and computer competence [6]. Thus the acceptance-related findings might generalize across other groups in the general population.

## References

[1] C. Carlsson, O. Kokkonen, P. Walden, On the improvement of strategic investment decisions and active decision support systems, in: Proceedings of the 32nd Hawaii International Conference on System Sciences, 1999.

[2] K.A. Delic, L. Douillet, U. Dayal, Towards an architecture for real-time decision support systems: challenges and solutions, International Symposium on Database Engineering & Applications, Grenoble, France, 2001, pp. 303–311.

[3] B. Fazlollahi, R. Vahidov, A method for generation of alternatives by decision support systems, Journal of Management Information Systems 18 (2), 2001, pp. 229–250.

[4] K. Fischer, J.P. Muller, M. Pischel, Unifying Control in a Layered Agent Architecture Agent Theory, Architecture and language Workshop, 1995

[5] T.J. Hess, L.P. Rees, T.R. Rakes, Using autonomous software agents to create next generation of decision support systems, Decision Sciences 31 (1), 2000, pp. 1–31.

[6] V.S. Lai, H. Li, Technology acceptance model for internet banking: an invariance analysis pages, Information & Management 42 (2), 2005, pp. 373–386.

[7] Z. Lee, C. Wagner, H.K. Shin, The effect of decision support system expertise on system use behavior and performance, Information & Management 45 (6), 2008, pp. 349–358.

[8] Y. Luo, K. Liu, D.N. Davis, A multi-agent decision support system for stock trading IEEE Network (January/February), 2002, pp. 20–27.

[9] R. Sauve, The Current State of Canadian Family Finances - 2003 Report, Contemporary Family Trends, The Vanier Institute of the Family, Ottawa, Ontario, Canada, 2004.

[10] T. Sueyoshia, G.R. Tadiparthic, An agent-based decision support system for wholesale electricity market decision support systems 44 (2) (2008) 425–446.

[11] R. Vahidov, Decision station: a notion for a situated DSS, 35th Hawaii International Conference on System Sciences, 2002.

[12] R. Vahidov, Situated decision support approach for managing multiple negotiations, in: H. Gimpel, N.R. Jennings, G.E. Kersten, A. Ockenfels, C. Weinhardt (Eds.), Negotiation, Auctions, and Market Engineering, Springer, Berlin, Heidelberg, 2008 , pp. 179–189.

[13] R. Vahidov, B. Fazlollahi, Pluralistic multi-agent decision support system: a framework and an empirical test, Information & Management 41 (7), 2004, pp. 398–883.

[14] R. Vahidov, G.E. Kersten, decision station: situating decision support systems, Decision Support Systems 38 (2), 2004, pp. 283–303.

[15] J. Waggoner, How Long Can Households Sustain Negative Savings? www. usatoday.com/money/perfi/general/2006-03-01-savings-cover-usat\_x.htm, vol March 2006.

![](/api/attachments/YD7SGBF4/fulltext/images/cf49de7a933d01032cd2c5280bb8bd571199016ed6d3328ad7efb339aa1766af.jpg)

Rustam Vahidov is an associate professor of MIS at the Department of Decision Sciences and MIS, John Molson School of Business, Concordia University (Montreal, Canada) He received his Ph D and M B A from Georgia State University. He has published papers in a number of journals, including Information and Management, Decision Support Systems, Journal of MIS, E-commerce Research and Applications, IEEE Transactions on Systems, Man and Cybernetics, Fuzzy Sets and Systems, and others. His primary research interests include: decision support systems, e-commerce systems, agent-based systems, negotiation software agents, and soft computing.

Xin He has earned her M.Sc. and B.Sc. in Management Information Systems from Concordia University (Montreal, Canada). Her research interests include decision support systems and e-commerce.

![](/api/attachments/YD7SGBF4/fulltext/images/fa76db1b9b4ae1439de1dd555d2ca3f930b3cac1adc37b32d7e83d3c1c62b680.jpg)
