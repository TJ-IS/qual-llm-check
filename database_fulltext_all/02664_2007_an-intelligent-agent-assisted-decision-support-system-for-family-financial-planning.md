---
otero_id: 2664
otero_key: "4GF3PBKG"
title: "An intelligent agent-assisted decision support system for family financial planning"
authors: "Shijia Gao; Huaiqing Wang; Dongming Xu; Yingfeng Wang"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2007.03.001"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Decision Support Systems 44 (2007) 60– 78

www.elsevier.com/locate/dss

# An intelligent agent-assisted decision support system for family financial planning <sup>☆</sup>

Shijia Gao <sup>a,b</sup>, Huaiqing Wang <sup>a,⁎</sup>, Dongming Xu <sup>b</sup>, Yingfeng Wang a

<sup>a</sup> Department of Information Systems, City University of Hong Kong, Hong Kong, China b UQ Business School, University of Queensland, Australia

Received 2 September 2005; received in revised form 9 September 2006; accepted 1 March 2007 Available online 12 March 2007

## Abstract

The demand for family financial planning (FFP) services is growing dramatically as the financial market grows more complex and people become more aware of the importance of qualified financial guidance. To provide decision support for FFP-related decisions, we formulate a conceptual model for FFP by following Simon's decision-making process model and map our model to the generic FFP process. The design, development, and empirical investigation of an intelligent FFP system for supporting FFP decisions by utilizing intelligent agents and Web-services technology are presented. © 2007 Elsevier B.V. All rights reserved.

Keywords: Family financial planning; Decision support systems; Conceptual model; Intelligent agents

## 1. Introduction

In September 2003, the Bank of Communications (Hong Kong Branch) (BCOM) and the City University of Hong Kong commenced a joint development project. By May 2004, the prototype, called “Financial Planner,” had been completed, launched, and utilized by all BCOM investment managers. Financial Planner, by its nature, is a computer-based system that provides investment-related advisory services to help high net worth individuals to manage their portfolios.

This project initiates our research in financial planning (FP), more specifically, in the family financial planning (FFP) area. Today, more people than ever recognize the importance of managing and controlling their family finances. Furthermore, the complex financial marketplace, changing tax laws, and other social and economic changes make it difficult for people to both keep up with all the changes and understand how these changes may affect them. As a result, the need for, and the complexity of, FFP has tremendously increased.

Our first attempt in the FFP research domain is the design and development of a Web-services, multi-agentbased system providing family wealth management advisory services to high-net wealth individuals [16,17]. This initial research is an extension of the BCOM development project. The objective is to improve the system developed for BCOM in terms of applying more innovative technology and integrating more family wealth management services.

However, FFP is not only for the wealthy. In contrast, everyone needs FFP. Thus, in this research, we extended FFP to the general public. FFP is a complex, dynamic, and distributed process, which requires the system to have a high degree of cooperative problem-solving capability [7]. It is very important to start from a decision-making/problem-solving perspective when analyzing and representing FFP domain knowledge [18]. In this study, we have adopted Simon's [41] well-known model of the decision-making process as a framework for a decision-based FFP model. Based on this conceptual model, we examined the various available resources and practices that assist families with FFP decisions, including printed materials, courses, financial institutions, the Internet, computer software, and FFP specialists [28]. We found that the current available resources and practices have limitations:

• Printed materials, courses and seminars, and the Internet may not be good options for many people, especially the elderly and the undereducated, who tend to seek quick and professional advice rather than attempting FFP themselves;

• Although the financial institutions and FFP specialists may provide seemingly effortless professional FFP-related services, these professionals may be specialists in one specific field and may not be qualified to provide the full range of advice required to develop a thorough financial plan. Those who can provide complete FFP advisory services typically first meet with individual customers one-on-one and determine the status, goals, and resources of the customer. They may then meet with the client's other advisors such as attorneys and bankers to obtain a complete understanding of the client's finances. After analyzing the information, planners may write a report detailing their recommendations. This approach is time-consuming, expensive, and inefficient. In addition, these resources are only for families with high incomes and large property or business interests, and not for the general public, especially those with low incomes;

• Over the last few years, there has been an increasing interest in developing FFP software or online program applications. Although contemporary FFP software or online programs help to improve the efficiency of the FFP decision-making process in some ways and are relatively inexpensive, they still have some of the following drawbacks: (i) Narrow focus. Current software/programs mainly provide one or two types of FFP-related services, such as investment strategy or risk management. The majority provide personal financial planning without taking other family members' finances into account. An ideal FFP system would include the aggregation of various FFP-related services while providing family-based FP services; (ii) Lack of autonomous and flexible problem-solving behavior. These applications are not capable of customer profiling so they cannot provide tailor-made services. Additionally, the software/programs always require user intervention to proceed; (iii) insufficient interaction and negotiation. Each existing software/program specializes in a certain FFP area; however they don't look at FFP as a whole, with few if any interactions among them. Separating these pieces of advice in each area from each other may result in conflicting information or important omissions that could lead to users suffering financial loss. Our proposed model requires different parties to evaluate the partial solution and to negotiate with each other; (iv) lack of proactive and reactive features. Our proposed model suggests the FFP solution needs to be revised when the situation changes or to react even before the change occurs. The existing software/programs neither respond to changes that occur nor exhibit goal-directed behaviors by taking initiative.

From the discussion above, it is evident that current FFP resources and practices suffer from a lack of popular use, flexibility, adaptability, and collaboration. Therefore, a new intelligent agent-assisted decisionsupport approach is proposed to achieve better FFP. FFP is a complex process involving many entities, where activities are delegated to a number of both autonomous and collaborative problem-solving agents. Each agent manages its FFP-related activities based on situational awareness and real-time decisions. From a holistic perspective, such agents have specific goals to achieve and interact with one another to manage their interdependencies. They work both autonomously and collaboratively to achieve the user's FFP goals — agents will collaborate in evaluating others' partial solutions, detecting conflicts and reconciling, in order to achieve the maximization of families' financial wellbeing.

The rest of this paper is organized as follows: Section 2, Background, briefly reviews the relevant literature on family financial planning, Simon's decision-making process model, intelligent agent theory and Webservices. Section 3 presents our proposed decisionmaking process model of FFP. Section 4 presents the system design architecture, prototype development, and operation of the proposed Intelligent family financial planning Decision Support System (IFFPS). In order to evaluate the prototype system, an empirical experiment is conducted to test the system's effectiveness in Section

5. Finally, Section 6 addresses our contribution and future work.

## 2. Background

## 2.1. Family financial planning (FFP)

Financial planning is a complex and rapidly changing process [2]. Even if we're managing our family finances reasonably well today, we worry about the future. The best way to achieve financial objectives is through FFP. FFP is “the establishment and development of a comprehensive financial plan that is tailored to a family's needs and which maximizes and protects financial resources, and is adapted to meet that family's changing circumstances during the various stages of the family life” [2]. FFP helps us define our financial goals and develop appropriate financial strategies to reach them. Because needs and goals change along with family circumstances, FFP is a lifelong activity. Among the rewards of FFP are improved standard of living, wiser spending patterns, and increased wealth [19].

Many people erroneously assume that FFP is only for the wealthy. However, while FFP can help the wealthy to spend and invest wisely it can also help those with an inadequate income to take steps to control their financial situation and lead to an improved lifestyle. The FFP process involves the translation of family objectives into specific plans and finally into financial arrangements to implement those plans. To this end, the FFP process is a logical, six-step procedure [28]: The first step of the FFP process is to determine a family's current financial situation with regard to income, savings, living expenses, and debts. The second step involves developing the financial goals and constraints of a family. The financial goals indicate the family's needs and wants of different time frames (short-term, mid-term, or longterm) while the financial constraints indicate the family's current circumstances (e.g., tax status, liquidity requirement, regulation restrictions). The third step is identifying alternative courses of action (i.e., FFP plans). Considering all of the possible FFP plans will help to make more effective and satisfying decisions. The fourth step is evaluating the alternatives, taking a family's life situation, personal values, and current economic conditions into consideration. The fifth step consists of creating and implementing a financial action plan. This step requires choosing ways to achieve a family's goals. The last step is to reevaluate and revise the financial plan. FFP is a dynamic process that does not end when a family takes a particular action. Changing personal, social, and economic factors may require a reassessment of the financial decisions. Regularly reviewing this decision-making process will help to make priority adjustments that will bring a family's financial goals and activities in line with its current life situation.

There are various resources available to assist families with FFP decisions, which include [28]:

• Printed periodicals. These can expand and update readers' FFP-related knowledge. For example, Business Week, Fortune, Money, The Wall Street Journal, etc.;

• Courses and seminars. Colleges and universities offer courses and seminars on investments, real estate, insurance, taxation, and estate planning. These courses have considerable popularity;

• The Internet. The World Wide Web enables people to access enormous FFP-related information (e.g., indices, stock quotes), tools (e.g., various calculators, converters), functions (e.g., FAQ, bulletin board, discussion forums), and online programs (e.g., finance.yahoo.com, moneycentral.msn.com, www.financialengines.com);

• Computer Software. The software available is able to perform a variety of FFP activities. The most popular are MS Excel, MS Money, Quicken, etc.;

• Financial institutions. These include banks, stock brokerage firms, savings and loan associations, credit unions, insurance companies, mutual funds, and real estate offices, which offer suggestions on budgeting, saving, investing, and other aspects of FFP. Among these institutions, Family Office (FO) or Multi-Family Office (MFO) has become one of the most sought-after platforms for providing FFP service. FOs or MFOs provide services including integrated tax and estate planning, investment strategy, risk management, lifestyle management, record keeping and reporting, and family philanthropy; and

• FFP specialists. These include accountants, bankers, credit counselors, certified financial planners, insurance agents, investment brokers, lawyers, real estate agents, tax preparers, etc., who provide specific financial assistance and advice.

## 2.2. Herbert A. Simon's model of the decision-making process

In his classic work [41], Herbert A. Simon proposed a decision process comprising four distinct phases — intelligence, design, choice, and review. In the intelligence phase, the decision maker recognizes the problem at hand and gathers information about the situation. The design phase is marked by structuring the problematic situation, developing criteria, and identifying the various alternatives through which the problem can be solved. In the choice phase, the decision maker chooses the best alternative that meets the criteria, and makes the final decision. Following these three phases, the decision maker uses the feedback from the results of the decision to review how well the process was executed. Such reflection on past processes can form a basis of the intelligence phase for future decisions. Although generic and simple in nature, Simon's decision-making process model has been applied and validated in a wide array of situations [10,15,39,45].

Referring to Simon's model and the FFP process described in the previous section, we formulated the decision-making process model for FFP, which includes gathering information about the FFP problem situation (intelligence), identifying various alternatives (i.e., formulating models) through which the problem can be solved (design), choosing the best alternative that meets the criteria (choice), and evaluating and revising the alternative (review) (see Section 3 for more details).

It is clear that Simon's model of the decision-making process matches the FFP process very well. However, very little previous research has adapted Simon's model to the FFP domain. In this research, we attempt to fill this gap by formulating a conceptual model of the FFP decision-making process according to Simon's model. Furthermore, we propose an FFP system whose design and implementation architectures are organized by the phases of Simon's model.

## 2.3. Intelligent agent-assisted decision support systems

The development of intelligent agents (IAs) and multiagent systems (MASs) has recently gained popularity among IS researchers [14,23]. Although there is ongoing debate and controversy on the best definition of the term “agent”, the central point of agents is that they are autonomous: capable of acting independently, exhibiting control over their internal state. Wooldridge and Jennings [52] suggest a precise description of agents; one that may be widely adopted in artificial intelligence communities as well as general computing areas. An agent is defined as a computer system that is situated in some environment, and is capable of autonomous action in that environment in order to meet its design objectives [51,52]. Furthermore, agents are able to act without the intervention of humans or other systems: they have control over their own internal state, and over their behavior [50]. An intelligent agent (IA) is one that is capable of flexible autonomous action in order to meet its design objectives, where flexibility includes properties such as autonomy, social capability, reactivity, and proactivity [51,52]. A generic agent has a set of goals, certain capabilities to perform tasks, and some knowledge about its environment. To achieve its goals, an agent needs to use its knowledge to reason about its environment and the behaviors of other agents, to generate plans and to execute these plans.

Various definitions from different disciplines have been proposed for the term MAS. The study of MAS originates from research in distributed artificial intelligence [8,12], where the activities of the system are distributed among multiple nodes for cooperative problem solving. More recently, the term MAS has been given a more general meaning: A MAS consists of a group of agents, interacting with one another to collectively achieve their goals. By absorbing other agents' knowledge and capabilities, agents can overcome their inherent bounds of intelligence [24]. One of the current factors (and arguably one of the more important ones) fostering MAS development is the increasing popularity of the Internet, which provides the basis for an open environment where agents interact with each other to reach their individual or shared goals.

In recent years, there has been considerable growth of interest in the design of a distributed, intelligent society of agents capable of dealing with complex problems and vast amounts of information collaboratively. Various research has been conducted into applying intelligent agent-based technology toward real-world problems. The early work led to SoftBot, a project aimed at autonomously performing predefined general Internet tasks, developed at the University of Washington [11], and an intelligent user assistant for information filtering, developed by MIT MediaLab [33]. Furthermore, there has been a rapid growth in developing and deploying intelligent agent-based systems to deal with real-world problems by taking advantage of the intelligent, autonomous, and active nature of this technology. UBC AgentWeb (http://agents.umbc.edu) has classified the applications into the categories of electronic commerce, manufacturing, network management, HCI, planning and scheduling, and the military. Since agent technology provides flexible, distributed, and intelligent solutions for business process management, researchers have proposed to design and develop numerous intelligent agent-based systems to support business processes management [25,54]. There has also been a recent acceleration in the design and development of intelligent agent-based financial systems [45,48]. The main benefits of an agent-based approach come from its flexibility, adaptability, and decentralization.

The potential contributions of intelligent agents to decision support systems (DSSs) have been described as enormous [49]. This has been reemphasized in the special issue of the DSS journal on future directions [5,40,47]. Intelligent agents appear in an increasing number of DSS applications.

Intelligent DSSs (IDSSs), incorporating knowledgebased methodology, are designed to aid the decisionmaking process through a set of recommendations reflecting domain expertise [46]. IDSSs are able to provide services to users and they try to satisfy the user's requirements through interaction, cooperation, and negotiation. IDSSs also offer tremendous potential in support of well-defined tasks [4] such as data conversion, information filtering, and data mining, as well as supporting illstructured tasks in dynamic cooperation [36,46].

## 2.4. Web-services incorporating agents

Web-services are currently one of the trends in network-based business services that offer a new paradigm for distributed computing. Web-services can be viewed as Internet-oriented and text-based integration adapters. Web-services are self-contained and modular business process applications that can be described, published, located, and invoked over a network, generally the World Wide Web (WWW), based on open standards. They enable integration models for facilitating program-to-program interactions [6,13]. Through Web-services, companies can encapsulate existing business processes, publish them as services, search for and subscribe to other services, and exchange information throughout and beyond the enterprise. While business environments are rapidly changing from centralized and closed to distributed and open, mainly by virtue of the proliferation of the WWW, scalability and interoperability features are getting more crucial to systems development. Among current Web technologies, Web-services are promising for open Web-based business applications and hence are adopted in this research for two reasons. First, the flexibility, interoperability, and extensibility of Web-services help streamline dynamic processes in FFP by creating an open, distributed system environment promising to reduce the cost of FFP. Second, the technology of Web-services is adopted in this research to standardize the communication among FFP agents and the interaction of agents with the end user. The messaging protocol SOAP (Simple Object Access Protocol), part of the Web-services standards, supports such communication.

A Web service is a “software application identified by a URL, whose interfaces and bindings are capable of being defined, described and discovered by XML (eXtensible Markup Language) artifacts, and which supports direct interactions with other software applications using XML based messages via Internet-based protocols” [1]. Web-services consist of a set of universally agreed-upon specifications including XML, SOAP, WSDL (Web-services Description Language) and UDDI (Universal Description, Discovery, and Integration) [13]. The self-describing nature of XML and WSDL allows disparate software components to understand each other. The messaging protocol SOAP supports the interaction between software components via RPC-like communication. UDDI represents a set of protocols for the description, registration, lookup, and integration of software components.

Typical agent architectures have many of the same features as Web-services, and extend them in several important ways [21]:

• a Web service knows only about itself, while agents often have awareness of other agents and their capabilities as interactions among the agents occur;

• Web-services, unlike agents, are not designed to use and reconcile ontologies;

• agents are inherently communicative, whereas Webservices are passive until invoked;

• a Web service, as currently defined and used, is not autonomous. However, as defined earlier, autonomy is a characteristic of agents;

• agents are cooperative, and by forming teams and coalitions, can provide higher-level and more comprehensive services. Standards for Web-services do not provide for composing functionalities.

In this paper, we integrate agent technology with Web-services for the purpose of overcoming such limitations and complementing each other. By so doing we seek to take advantage of the flexibility, interoperability, and extensibility of Web-services to illustrate feasibility in communicating with end users. By using Web-services, it is easy to add more business functionalities into our system by adding more Webservices agents, and reusing existing functionalities for other purposes.

## 3. Decision-making process model of family financial planning

The design purpose of our research is to propose a framework for an intelligent agent-assisted decision support system that targets improved end users' FFP decision making, parallels human problem-solving processes, and supports the major phases of decision making. To achieve decision support effectiveness, an ideal system should be built with reference to the adoption of a decision-making theory. We have developed a conceptual process model based on the well-known Simon framework [41], which identifies four different phases — intelligence, design, choice, and review. By comparing Simon's decision-making process model with the FFP process (Section 2.1), we found the process logic matches perfectly. Fig. 1 shows the FFP decision-making process conceptual model with specific activities contained within each decision-making phase, mapped together with the FFP process steps.

There has not been much automated support for the intelligence phase of FFP decision making. According to Simon [41], the intelligence phase involves searching the environment for conditions calling for decisions. However, as this phase relates to FFP, it is difficult to articulate the general reasoning process leading up to a problem statement. So the most common form of computer “support” for this initial phase in designing an FFP system is to provide convenient access to a variety of information sources, such as the user, and any external electronic sources and to detect developing problems and opportunities [10,45]. Use of agents for this task has been widely advocated. For example, Teo and Choo [43] stress the importance of automated gathering of relevant information for competitive intelligence. This intelligence phase is a “fact finding” procedure, which collects all necessary information to determine the client's financial situation — Step One in the FFP process.

![](/api/attachments/4GF3PBKG/fulltext/images/823e5db0f5759d480b20b14fb9bfc3346e5c5796c0afff11f3188cdc2323d0d1.jpg)  
Fig. 1. Decision-making process model (mapping to FFP process).

In the design phase, an FFP model needs to be developed. To achieve this, it is necessary to first analyze the data collected from the intelligence phase. It is very important at this stage to assemble the information in order to establish an individual's future intentions, goals, and ideals. It is also important to ascertain an individual's attitude toward making investments in terms of risk, time frames, ethical considerations, etc. [2]. In this regard, this phase is the development of financial goals — Step Two in the FFP process.

FFP is also the process that translates family financial goals into specific financial plans [29]. Furthermore, for different risk-tolerance level users, the financial strategies would differ even though their financial goals are the same. It is therefore necessary to develop tailored FFP models for different users with various financial goals. The FFP model is an optimization model, defined by decision variables, constraints, and family wealth maximization objective functions. To facilitate more user involvement, we also allow users to customize a part of the model (e.g., constraints, variables) in this phase. Through the user customization or trail and error, a number of FFP models have been developed, which is Step Three in the FFP process — identifying alternative courses of action.

In the choice phase, the “solve model” activity is not as straightforward as it may first appear. There can be multiple variants of a solution method along with specialized computer implementations of the same. For example, we use Linear Programming (LP) to solve the FFP model. However, there are many LP packages available, and they vary in the problem size they can handle, their memory requirements, and their execution speeds. Some simplex implementations use sparse matrix techniques to sacrifice speed for storage efficiencies. Thus, selection of a solution method may require the careful consideration of multiple factors. Occasionally, some solution procedures will require experimentation to set the values of certain starting or controlling parameters. Such a selection procedure is just like Step Four in the FFP process — evaluate alternatives. And based on the model selected, solving the model to work out an original financial plan is not difficult (Step Five in the FFP process). In addition, solution testing is necessary before model solutions can be adapted for FFP use [10] because a model rarely captures all aspects of a real problem and will usually make simplified assumptions. The numerical values used as inputs to the model often have uncertainty associated with them. Therefore, it requires considerable manual intervention from the user to ensure the solution's robustness.

In the final review phase, the solution made from previous phases will be assessed. Since this solution is generated mainly from a financial perspective, a number of other aspects, such as legal (estate planning) and accounting (money management) considerations, need to be evaluated in light of the solution. If there are any conflicts detected between different parties' interests, the previous solution will be revised based on some predefined rule-reasoning. This choice-review iteration will continue until the choice is conflict-free — Step Six in the FFP process. Finally, the integrated solution is sent to the end user for implementation.

Many research studies show that FFP is a complex decision situation in which decision makers attempt to gather a good deal of information before making their final choice. However, for different decision-making phases the required information differs, thus, it is not efficient to collect all the data at the very beginning and pass it throughout the entire decision-making process. Therefore, in our proposed framework, with the design, choice, and review phases, information corresponding to their tasks would be requested from the intelligence phase when required (bidirectional arrow means information requesting and providing).

## 4. Design and development of Intelligent Family Financial Planning Decision Support System (IFFPS)

This section presents the design and development of a novel prototype of the Web-services, multi agentbased FFP system — the Intelligent Family Financial Planning Decision Support System (IFFPS), based on the proposed conceptual model.

## 4.1. System design architecture

Our proposed intelligent FFP DSS (IFFPS) provides optimized long-term advice that maximizes family wealth, and identifies and subsequently resolves any possible conflicts among the advice. As discussed in the previous section, Simon's decision-making process logic was employed to model the FFP process, which in turn was converted to the design architecture of IFFPS consisting of entities and agents, shown in Fig. 2.

External entities include data and models that provide information such as financial figures and models, legal ordinances, etc., to different agents and the user, if required. The Intelligence Group contains two information agents that obtain, aggregate, and assess relevant information from the user as well as external electronic sources. All of the Design, Choice, and Review Groups may request information relating to their task from the Intelligence Group, if required. The Design Group contains two groups, namely analyzing ( ) and proposing ( ) agents [45]. They are:

![](/api/attachments/4GF3PBKG/fulltext/images/26dcdf1d79ced73320641ec90feb46dac843a73626692e7f83625a884e553aa1.jpg)  
Fig. 2. IFFPS architecture.

• Goal Assessment Agent ( ): To help the user identify long-, intermediate-, and short-term goals, the Goal Assessment Agent first assesses the user's financial status by asking the user about his or her employment (e.g., salary), compensation plans (e.g., stock options), personal assets and liabilities (e.g., real estate information and mortgages), investment assets (e.g., current holdings of bonds, equities, and insurance accounts), and details of income tax return [30]. The Goal Assessment Agent then provides two mechanisms to help the users to define their financial goals. The first mechanism is to provide the user with a list of financial goals by considering both the user profile and financial status data (i.e., providing goals that match the user's personal and financial situation). The users can select their financial goals from the list. The second mechanism is that the Goal Assessment Agent allows the user to specify his/her special financial goals (other than those provided in the list) to the agent. For example, for a middle-class married couple with children in their late 30s, the agent provides shortterm goals (covering a 12-month period) like repainting the house, diversifying investment portfolio; the intermediate goals (2–5 years) like buying a second car, increasing college fund contributions; and the long-term goals (6+ years) like buying a larger home, increasing retirement funds, developing an estate plan, [19]. After the couple chose the financial goals from the list, they also specify short-term goals like buying braces for children; intermediate-term goal like increasing second income from part-time to full-time; and long-term goal like overseas travel. The Goal Assessment Agent then summarizes the user's financial goals by grouping them by time frame (short-, intermediate-, and long-term), and allows the user to specify a priority for each goal (high/medium/low), a target date to reach the goal, and estimated cost.

• Investor's Risk Profiling Agent ( ): By asking questions regarding the user's preference on expected return of the investment, time horizon of the portfolio, and choice of portfolios with different risk and return [31], the Investor's Risk Profiling Agent is capable of identifying the user's reaction to market volatility and weigh the relative importance of his or her financial goal. After analyzing a user's risktolerance level and investment preference, the agent will identify one out of five investor profile models (Capital Preservation, Income, Income/Growth, Growth, and Aggressive Growth) [31] for the user.

• Asset Risk Estimation Agent ( ): For each financial asset, the Asset Risk Estimation Agent collects its 5 years' weekly price data, and conducts simulations to estimate its risk level [34].

• Portfolio Template Agent ( ): For different kinds of risk-tolerance users, the Portfolio Template Agent generates different investment templates by using fuzzy rules [45] for different investor profile models. Users can choose their favorite template as their portfolio and customize this template (i.e., add/ remove assets) with their own preferences.

• Asset Allocation Agent ( ): The Asset Allocation Agent automatically provides asset allocation recommendations to different investor profile models based on the Merrill Lynch Asset Allocation Strategies [32].

There is only one agent — Portfolio Optimization Agent — in the Choice Group. The optimization method we use is Linear Programming (LP). LP is a mathematical technique used to obtain an optimum solution to problems of allocating limited resources among competing activities [3]. Although there are many optimization techniques available, we chose LP because of the relative ease of the solution method, its popularity in financial optimization applications, and the widespread availability of LP software [3]. LP problems consist of a linear objective function (i.e., maximize FFP return) and a set of linear constraints (portfolio weights, budgets, etc.). The detailed LP model for a FFP problem is published in the previous study [17]. Based on the user's collective investment goals and personalized specifications, the Portfolio Optimization Agent determines the proportions for each asset in the portfolio by maximizing fuzzy objectives using a simple iterative improvement search. The agent optimizes the predefined constrained LP model [16, Appendix] by choosing the best LP solving package to efficiently find the optimal solution.

The outcome of the Design and Choice Groups is an optimized investment solution, which contains a selection from a weighted portfolio of assets that suits the investor's objectives and a suggested allocation that maximize the expected return while accepting the degree of risk the investor can tolerate. The Review Group consists of three advisory agents and one resolution agent:

• Cash Flow Management Advisory Agent (Accounting): The Cash Flow Management Advisory Agent will prepare a Net Income Statement [30] based on the monthly inflow and outflow information collected from the user. The agent will then evaluate the result to see whether there are any conflicts between the solvency and the portfolio.

• Estate Planning Agent (Legal): Based on the user's asset and liability information, the Estate Planning Agent will list all assets and determine the value of the estate. Then it will estimate estate transfer cost, such as legal fees, outstanding debt, estate tax, etc. An estate assessment report will be produced as a result.

• Tax Advisory Agent (Legal): The Tax Advisory Agent assesses the user's tax status, especially the estate tax. It will compare the user's estate duty with the estate value to see whether there are any conflicts with the user's goal.

• Resolution Agent: The investment optimization advice and corresponding evaluation reports will all be sent to the Resolution Agent. If there is no contradiction between the interests of the Design and Choice Groups and the Review Group, the investment optimization advice will be sent to the end user, indicating that the entire process is complete. If there are contradictions, the Resolution Agent will take some initiatives to make a judgment and resolve the conflict. Of course, the IFFPS can only automate the solutions for those conflicts that occur with a high degree of frequency. The resolution advice will be sent to the Choice Group to revise the previous solution, and the concessions will then be made. Such choice and review processes iterate until the solution is conflict-free and eligible to be sent to the user.

## 4.2. Prototype development

FFP is a distributed problem as discussed previously. The tentative solutions from different agents will iteratively exchange until the wealth maximization objective is met, which makes FFP a distributed constraint satisfaction problem [9]. In order to solve the FFP problem, we adopt Yokoo et al.'s [53] formalization and algorithms. Agent technology is applied to deal with the complex, dynamic, and distributed FFP processes; Web-services techniques are proposed for more interoperability and scalability in a network-based business environment. The complex FFP problem is delegated to a society of autonomous problem-solving agents, which behave on behalf of different specialists involved in FFP. These intelligent agents are wrapped as Web-services, communicating and interacting with each other in an open environment. By integrating agent technology with Web-services to make use of the advantages of both, this approach provides a more intelligent, flexible, autonomous, and comprehensive solution to FFP. Furthermore, in order to deal with the dynamic real-world environment, it is easy to add proactive capabilities to the Web-services agents. By so doing, our proposed system can sense the environment on regular basis and initiate proactive behaviors to reassess the current user's data and make further advices regarding FFP changes. Fig. 3 below shows the implementation architecture of the Webservices, multi-agent-based IFFPS, which is derived directly from the design architecture. The dashed frames represent decision-making groups.

In this architecture, all these Web-services agents work autonomously and collaboratively via the Internet. Each agent focuses on its particular task without interventions from outside, although there may be one or more agents involved in a particular service. Agents with different functionalities in one service cooperatively provide that specific service. By drawing on other agents' knowledge and capabilities, agents can overcome their inherent bounds of intelligence and work collaboratively to pursue their goals. This is an open environment. Different agents do not necessarily reside at the same location or belong to the same company. That means, in addition to our IFFPS, there are other companies providing financial, accounting, legal, or other FFP-related services. Through the standard communication protocol, each Web-services agent can freely select and call the other agents' services.

Based on the implementation architecture shown above, a Web-services-multi-agent-based FFP prototype has been implemented. At the lowest level, the operating system is Linux. The Web server component contains the Apache Web server, Jakarta Tomcat, JSP scripts, and the MySQL Database Server. Interaction among Webservice agents is set up on lower data communication levels, along with control information that contains semantics and knowledge. A popular language for agent communication, Knowledge Query and Manipulation Language (KQML), is used. Recent research has focused on the use of XML (eXtensible Markup

Language) in agent communication [20]. The Webservice agents have been developed by using the Java Web-Services Development Package (JWSDP) [22], which brings together a set of Java APIs for XML-based Java applications by supporting key XML standards, such as SOAP (Simple Object Access Protocol), WSDL (Web-Services Description Language), and UDDI (Universal Description, Discovery, and Integration). These APIs and their reference implements are bundled together with a set of runtime tools to form a JWSDP.

Web-services use the popular Internet standard technology-SOAP — to increase compatibility of the system. SOAP is the most common network communication protocol between software services. We use SOAP for agents' communication, while KQML is wrapped by SOAP. SOAP messages are represented by using XML, and can be sent over a transport mechanism-HTTP. In the prototype system, the communication among agents is done by Java API for XML Messaging (JAXM). Such JAXM messages follow SOAP standards, which prescribe the format for messages and specify the elements that are required, optional, or not allowed.

The Web-service agents are able to detect and resolve the conflicts by JESS (Java Expert system Shell and Scripting language) rules. JESS is a rule engine and scripting environment written entirely in Java language [26]. In the prototype system, each agent contains a JESS rule set for reasoning. The reasoning results are asserted JESS facts. An agent can send such facts to other agents by wrapping them to XML and SOAP messages.

After the Web-service agents have been set up, they are published on the Web. The WSDL specification is used to describe and publish Web-service agents a standard way. Finally, the UDDI is used to create and implement a directory of the Web-service agents.

## 4.3. Prototype system operation

The following case is used to demonstrate the system's operation. Assume that a user plans to buy a newly issued profitable security. However, he does not know how much to invest in this security and how to adjust the other securities that are already in his portfolio. The user wants our IFFPS to provide advice. In addition, his family has ordered a new car, which requires the user to pay the down payment this month.

The system (Information Service) first asks the user to input his personal information, financial data (including indicating the purchase of a new car), etc. At the same time, the Information Service collects the most updated financial information and models, and forwards all the

Fig. 3. IFFPS prototype implementation architecture.

![](/api/attachments/4GF3PBKG/fulltext/images/9eaed2070dddf67a28545c1ea3ab29385695063694bd9cc904d44cd65f1a2d70.jpg)

collected information to the Financial Service. The Financial Service returns the investor risk-tolerance level analysis report, portfolio template, and asset allocation recommendation to the user. Then the user modifies his portfolio by adding the newly issued profitable security and specifies his investment goal. Based on that, the Financial Service works out an initial optimized portfolio solution/advice, which is sent to Accounting, Legal, and Resolution Services simultaneously.

The Accounting Service requests cash flow-related information from the Information Service, and produces an income statement. Then, the adjusted cash balance result will be compared with the investment solution and asset allocation recommendation to see whether there is a conflict. In this case, a short fall of cash is detected because of the extra investment in both the asset and the car this month. A cash-flow evaluation report (indicating the conflict) will be produced and sent to the Resolution Service to activate its conflict-reconciliation activities.

While the Accounting Service is processing, the Legal Service requests estate tax related information from the Information Service, and produces a tax and estate planning report. Then the report will be evaluated based on the predefined business rules to see whether there is a conflict. In this case, estate tax increases more than four times because of the investment in the car (i.e., it increases the legacy), which is unfavorable to the user. A legal evaluation report (indicating the conflict) will be produced and sent to the Resolution Service to activate its conflict-reconciliation activities.

According to the initial investment solution and two evaluation reports, the Resolution Service may advise the user to sell some assets on hand (that are less profitable) in order to afford the new car, as well as to invest some in the new profitable asset. In addition, in order to avoid the estate tax, the user should invest taxaccrued money in buying life insurance that is tax-free. The resolution report will be sent to the Financial Service to revise the previous investment advice. The revised investment solution from the Financial Service will be sent to Accounting and Legal Services for further evaluation. Such an evaluation and revision process will iterate until there is no further conflict. Finally, all the reports and advice will be sent to the end user.

## 5. Empirical investigation

In order to rationalize a decision-aiding system in support of the decision-making process, an appropriate evaluation method must address the effectiveness of decision making with the system [29,35]. In this section, a laboratory experiment was designed and conducted to investigate the performance of our proposed IFFPS and the ramifications of its impact on decision-making effectiveness.

We compared the performance of the IFFPS with that of a FFPS without agent and Web-services features (i.e., the system we developed for BCOM mentioned in Introduction). In the experiment, subjects were asked to act as people represent their family to ask for FFP services. Our major expectation was that IFFPS would promote higher effectiveness of decisions than the regular FFPS.

## 5.1. Hypotheses

Sharda et al. [39] and Udo [44] have summarized varying approaches proposed for measuring effectiveness of DSSs, such as case study, field study, and laboratory study. Sprague and Carlson [42] described four major categories — productivity, process, perception, and product measures — which have proven to be valid evaluation models in the later research [38,39,45]. Based on our research domain, following on this successful approach, we examined whether IFFPS has been successful in the sense that it improves the outcomes, process, and user perceptions regarding decision making.

## 5.1.1. Decision outcomes

Several researchers have claimed that outcome is one dimension of DSS performance measurement [27,38,45]. The outcomes are measured in terms of 1) Expected Return on Portfolio, which is the estimated value of a portfolio; and 2) Implied Volatility of Portfolio, which is the estimated volatility (i.e., a statistical measure of the tendency of a market or security to rise or fall sharply within a period of time) of a portfolio. It is expected the portfolio return from IFFPS will be higher than that from FFPS, and the implied volatility from IFFPS will be lower than that from FFPS. In other words, the suggestions provided by IFFPS will yield a higher return but with lower risk than that by FFPS:

H1. The IFFPS provides a more comprehensive solution than FFPS.

H1a. The optimal portfolio suggested by IFFPS yields a higher expected return than the optimal portfolio suggested by FFPS.

H1b. The optimal portfolio suggested by IFFPS offers lower volatility than the optimal portfolio suggested by FFPS.

## 5.1.2. Decision process

Alternative generation is an important step in decision making. Much of the literature uses the “number of alternatives” as the measurement of the decision process [15,37,39,45]. Thus, Hypothesis 2 examined the number of alternatives that were generated by both systems:

## H2. The IFFPS generates more alternatives than FFPS.

Another important process measure is the number of variables considered in the decision-making process [37]. In this study, the data captured from the users is the same between IFFPS and the FFPS. However, the way these two systems use the data is different. “The number of variables” here is the measure of how many data is used during the system process. The improved DSS should analyze the problem more thoroughly by considering more variables before reaching a decision:

H3. The IFFPS considers more variables than FFPS.

## 5.1.3. User perception

The perceived reactions to the system are defined as the group members' feelings about the decision process and the decision outcome. The most commonly used user perception measures are user satisfaction and decision confidence [15,45]. We expected the user to be more satisfied and confident in the decision when using a more active system:

H4. The IFFPS user has more satisfaction with the system than the FFPS user.

H5. The IFFPS user has a higher perceived confidence in the final decision than the FFPS user.

Another measure that has been used in some previous work is perceived learning [27,45], which is one dimension of performance. On the learning dimension, the IFFPS user could learn more and improve understanding about FFP problems than could an FFPS user, since the former was exposed to the divergence of approaches/views on the FFP process. Therefore, we hypothesize:

H6. The IFFPS user learns more FFP concepts than the FFPS user.

## 5.2. Experimental design

## 5.2.1. The experimental systems

In order to investigate the effectiveness of our proposed IFFPS, a regular FFP system (that was developed for BCOM as mentioned in the Introduction) as a counterpart system was also implemented. FFPS was a subset of the IFFPS including data, models, and interface, functioning as a Financial Service but without agents and Web-services. The Accounting and Legal Services were developed in IFFPS, while FFPS only kept the financial features. The interfaces and the page flows of both systems are the same; even though the technologies behind the systems are different (IFFPS uses agent technology while FFPS doesn't). Both systems are web-based, but IFFPS is more flexible than FFPS by using Web-services. The data required from the user are the same; however, IFFPS processes the data iteratively and analyses the data from different dimensions (i.e., from finance, accounting, and legal aspects) while FFPS processes the data only once and only considers in finance perspective. For the end user, the only difference is that the IFFPS users can choose whether to accept the resolution proposed by the system or reject it; whilst FFPS users do not have this option.

## 5.2.2. Subject population

The subjects for the study were postgraduate and upper-level undergraduate business administration Finance/Financial Engineering major students recruited through campus email broadcasting at a major university in Hong Kong. Participation in the study was voluntary. To avoid additional financial planning and investment training time, the recruitment emails specified that participants must have exposure to the basic principles of investments and FP as part of their general business education.

Of the 62 subjects participating in the study, some were part-time students with financial working experience or research backgrounds. To ensure homogeneity, all subjects were randomly assigned to one of the two groups — the experimental group (IFFPS) or the control group (FFPS). The method we used for random sampling is as follows: we first put the names of the subjects in a column in a spreadsheet, and then created a second column consisting of random numbers from the spreadsheet's random number generator. By sorting using the second column as the sort key we put the subject names in random order. Finally, we selected the odd numbered subjects into the experimental group and even numbered subjects into the control group.

## 5.2.3. The experimental task

Subjects participating in the experiment assumed the role of persons representing their family request for FFP. The experimental task for both experimental and control groups was the same. This involved selecting a portfolio

Summary of instruments

Table 1

<table><tr><td>Instruments</td><td>Sources</td></tr><tr><td>The system helps me in making good investment decision.</td><td>[27]</td></tr><tr><td>The system helps me in making good financial planning decision.</td><td>[27]</td></tr><tr><td>The system has made it easier to respond to the investment problem.</td><td>[27]</td></tr><tr><td>The system has made it easier to respond to the financial planning problem.</td><td>[27]</td></tr><tr><td>The system enhances better investment decision.</td><td>[38,44]</td></tr><tr><td>The system enhances better financial planning decision.</td><td>[38,44]</td></tr><tr><td>The system provides comprehensive solution, which considers various aspects, to financial planning.</td><td>[37]</td></tr><tr><td>The system provides me with alternatives.</td><td>[15,37,39,45]</td></tr><tr><td>The system analyzes the investment problem thoroughly.</td><td>[38]</td></tr><tr><td>The system analyzes the financial planning problem thoroughly.</td><td>[38]</td></tr><tr><td>The system provides me with additional learning related to investment.</td><td>[27,38,45]</td></tr><tr><td>The system provides me with additional learning related to financial planning.</td><td>[27,38,45]</td></tr><tr><td>I will be more confident about the investment decision after using the system.</td><td>[15,27,39,45]</td></tr><tr><td>I will be more confident about the financial planning decision after using the system.</td><td>[15,27,39,45]</td></tr><tr><td>I&#x27;m satisfied with the quality of the suggested investment solution.</td><td>[15,27,44,45]</td></tr><tr><td>I&#x27;m satisfied with the quality of the suggested financial planning solution.</td><td>[15,27,45,45]</td></tr><tr><td>The system is useful.</td><td>[27]</td></tr></table>

of securities suitable for the participants' objectives and preferences; at the same time, the portfolio should yield the highest possible return with the lowest acceptable risk. The task here centered only on the security selection. The relative weight for each security is provided by the system. Prior to selection, the participants were asked to provide their real financial status data, including personal information (age, marital status, education, occupation, etc.), asset/liability information, and monthly income and expenses. They also needed to indicate their financial goals and preferences in terms of return and risk. The participants then used the available facilities and functions in the system to make their choice and selection. In our proposed system, IFFPS, users also received the detected conflict warnings and recommendations on resolution.

## 5.2.4. Experimental procedures

The experimental procedures for both experimental and control groups are the same. At the beginning of the experiment, the subjects were asked to sign a consent form and fill out a pretest that measured their knowledge of investment and FP. The participants were then guided in the use of the system, from personal information collection to customer profiling; from investment instruments template selection to portfolio customization; and from constraints specifying to final optimization recommendation (for IFFPS, it also included conflict detection and resolution). Participants subsequently answered a questionnaire concerning their perceptions of the outcome, process, and confidence and satisfaction levels. A follow-up post-test was later used to measure the improvement of the subjects' knowledge of investments and FP concepts after using one of the two systems. The entire experiment took about an hour to complete.

## 5.3. Measurements

Outcome was measured by the ultimate portfolio expected return and volatility, which are calculated by the system and stored in the database. Process was measured by the number of alternatives generated and the number of variables used during the system running time. User perception of decision making was measured by a questionnaire with 17-item instruments. The items were used to measure the perceptions of outcome, process, perceived learning, decision confidence, and satisfaction levels toward the investment and FFP decision making derived from an extensive review of DSS literature [15,27,37–39,44,45]. Table 1 below shows a summary of the sources of the instruments.

## 5.4. Results

A total of 62 subjects participated and provided complete and valid data in the experiment. Thirty-one of them (exactly half, 16 female and 15 male) used IFFPS (in the experimental group) and the rest (14 female and 17 male) used FFPS (in the control group). The average age was 25.3. The results of the T-tests indicated that there were no significant differences between the participants in experimental and control groups, in terms of age, marital status, education, occupation, and working experience.

Table 2  
Outcome comparison

<table><tr><td rowspan="2"></td><td colspan="2">IFFPS</td><td colspan="2">FFPS</td><td rowspan="2">t</td><td rowspan="2">p-value</td><td rowspan="2">Confirm</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>Expected return</td><td>22.55%</td><td>.0369</td><td>15.99%</td><td>.0182</td><td>8.877</td><td>.000</td><td>Yes</td></tr><tr><td>Volatility</td><td>9.92%</td><td>.0118</td><td>14.58%</td><td>.0182</td><td>-11.961</td><td>.000</td><td>Yes</td></tr></table>

SPSS was used for data analysis. Through an Independent Sample T-test, we derived the outcome and process comparison of the two groups, shown in Tables 2 and 3, respectively.

The result shows the outcome between the two systems differed significantly, that is, the users using IFFPS achieved statistically significantly higher return (22.55% vs. 15.99%) with lower risk (9.92% vs. 14.48%) in the resultant investment/FP suggestion than their counterparts using FFPS. This indicates that IFFPS provides more comprehensive outcomes than FFPS.

The results of the process measurement show that the number of alternatives generated and the number of variables considered by the system are both significantly different between the two groups. IFFPS generated more alternatives for users to choose from than did FFPS (4.10 vs. 1.52). In addition, IFFPS uses more variables to work out the solution during the process than does FFPS (6.97 vs. 5.45). This result is in accord with the previous finding and the IFFPS design features. The decision support process of IFFPS surpasses that of FFPS.

In the statistical analysis of the user perception questionnaire, a two-way analysis of variance (ANOVA) model was applied to all dependent measures. The results are summarized in Table 4.

All results were statistically significant, supporting our hypothesis that IFFPS improves user perception of decision making. The users of IFFPS perceived the system outcome as more helpful to support their investment as well as financial planning (FP) decision making than did the users of FFPS. Users also perceived that

Table 3  
Process comparison

<table><tr><td rowspan="2"></td><td colspan="2">IFFPS</td><td colspan="2">FFPS</td><td rowspan="2">t</td><td rowspan="2">p-value</td><td rowspan="2">Confirm</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>No. of alternatives generated</td><td>4.10</td><td>.700</td><td>1.52</td><td>1.06</td><td>8.877</td><td>.000</td><td>Yes</td></tr><tr><td>No. of variables considered</td><td>6.97</td><td>1.14</td><td>5.45</td><td>.506</td><td>6.770</td><td>.000</td><td>Yes</td></tr></table>

Table 4  
User perception: ANOVA results

<table><tr><td></td><td>F</td><td>Sig.</td><td>Confirm</td></tr><tr><td>Perceived outcome</td><td>13.567</td><td>.000</td><td>Yes</td></tr><tr><td>Perceived process</td><td>14.844</td><td>.000</td><td>Yes</td></tr><tr><td>Perceived learning</td><td>10.020</td><td>.002</td><td>Yes</td></tr><tr><td>—Investment knowledge</td><td>4.828</td><td>.032</td><td></td></tr><tr><td>—FP knowledge</td><td>12.823</td><td>.001</td><td></td></tr><tr><td>Decision confidence</td><td>10.599</td><td>.002</td><td>Yes</td></tr><tr><td>—Investment decision</td><td>4.874</td><td>.031</td><td></td></tr><tr><td>—FP decision</td><td>13.846</td><td>.000</td><td></td></tr><tr><td>User satisfaction</td><td>11.453</td><td>.001</td><td>Yes</td></tr><tr><td>—Investment decision</td><td>7.156</td><td>.010</td><td></td></tr><tr><td>—FP decision</td><td>14.340</td><td>.000</td><td></td></tr></table>

IFFPS analyzed the FFP-related problem more thoroughly and provided more alternatives than FFPS. Although the results show perceived learning, decision confidence and user satisfaction are all significant for both investment and FP decision making, F values demonstrated that users find IFFPS to be more helpful in FP decision making than in investment decision making. This again proves that the investment features between the two systems are basically the same.

As we mentioned during the experimental procedure, we asked the participants to fill out multiple choicebased pretests and post-tests that measured their knowledge of investment and FP before and after the system usage, in order to assess whether there was any improvement in knowledge and understanding. Both tests were graded with 10 marks, 5 marks concerning investment knowledge and the other 5 marks asking about FP-related questions. Table 5 list the Independent Samples T-test results in detail.

There was no significant difference in all pretest results (Items 1, 3, and 5), which supports the assumption of homogeneity between the two groups. The results of investment questions in the post-test (Item 2) also showed no significant difference, which proves that the investment/finance features between the two systems are the same. But the results for the FP-related questions (Item 4) between the two groups differed significantly; the users using IFFPS got statistically significantly higher scores than the users using FFPS. This indicates that IFFPS can help users learn more about FP knowledge, which in turn assists users in making better FFP decisions. Overall, users using IFFPS can achieve significantly greater knowledge improvement than users using FFPS (Item 6).

Table 5  
Pre- and post-knowledge comparison

<table><tr><td rowspan="2" colspan="2">Item</td><td colspan="2">IFFPS</td><td colspan="2">FFPS</td><td rowspan="2">t</td><td rowspan="2">p-value</td></tr><tr><td>Mean</td><td>S.D.</td><td>Mean</td><td>S.D.</td></tr><tr><td>1</td><td>Pretest (investment)</td><td>.03</td><td>1.402</td><td>2.00</td><td>1.291</td><td>0.094</td><td>.925</td></tr><tr><td>2</td><td>Post-test (Investment)</td><td>2.71</td><td>1.755</td><td>2.65</td><td>1.518</td><td>0.155</td><td>.877</td></tr><tr><td>3</td><td>Pretest (FP)</td><td>2.23</td><td>1.117</td><td>2.16</td><td>1.508</td><td>0.191</td><td>.849</td></tr><tr><td>4</td><td>Post-test (FP)</td><td>3.52</td><td>0.962</td><td>2.13</td><td>1.477</td><td>4.381</td><td>.000</td></tr><tr><td>5</td><td>Pretest (overall)</td><td>4.26</td><td>1.483</td><td>4.16</td><td>2.002</td><td>0.216</td><td>.829</td></tr><tr><td>6</td><td>Post-test (overall)</td><td>6.23</td><td>1.892</td><td>5.10</td><td>2.166</td><td>2.186</td><td>.033</td></tr></table>

## 5.5. Discussion

Based on the results of this research, it was found that our proposed IFFPS provides higher DSS effectiveness than a regular FFPS in terms of decision outcome quality, decision process, and user perception. Decision outcome quality was measured by the output portfolio expected return and its volatility. The statistical analysis revealed that IFFPS outcomes yield higher returns with less volatility than FFPS outcomes on average $( \scriptstyle { p = 0 . 0 0 0 } )$ . This is because FFPS considers only static financial aspects while IFFPS also takes dynamic accounting and legal dimensions into account. IFFPS is able to detect and resolve conflicts amongst FP data, whilst FFPS totally overlooks any possible conflicts. By adding these two dimensions to the solution and resolving FFP conflicts to enlarge the feasible solution boundary [3], IFFPS can further optimize the family wealth, yields higher return. At the same time, by considering more FFP aspects, the risk (i.e., volatility) is reduced by diversification [19].

The decision process was measured by the number of alternatives generated and the number of variables considered during the system process time for both FFP systems. Statistical analysis revealed that both numbers from IFFPS are significantly higher compared to the numbers measured from FFPS $( \scriptstyle { p = 0 . 0 0 0 } )$ . The implications of this are straightforward. “More alternatives” has two meanings here. First, since IFFPS evaluated more perspectives of FFP, more options or plans are produced from the system, and thus the users have more flexibility and freedom to make a preferential choice. Second, IFFPS is capable of detecting any contradiction among different agents (or FFP actors) and providing resolution suggestions. Therefore, when conflicts take place, users are free to choose whether to take the reconciliation or leave the conflicts alone. As we stated before, the data captured from the users by both systems is the same. However, FFPS processes the data only once, and only from a financial perspective. In contrast, IFFPS processes the data iteratively, analysing the data from financial, accounting, and legal perspectives. For example, both systems captured the user income and expenses data. FFPS uses these data only to measure user's financial goals while IFFPS also uses these data to prepare an Income Statement to assess user's cash flow status. Therefore, by analysing the data more thoroughly and from different perspectives, IFFPS considers more variables than FFPS in the decision support process.

User perception was measured in terms of users' perceived outcome quality, process, learning, decision confidence, and satisfaction. Statistical analysis revealed that participants using the IFFPS perceived significantly higher DSS effectiveness in comparison to their counterparts in the FFPS group. The user's learning was measured by both subjective (user perception questionnaire) and objective data (pre-test and post-test scores). The results indicate that the users of IFFPS can learn more about FP and investmentrelated knowledge than their counterparts using FFPS, and thus in turn perceived a higher level of confidence and satisfaction with the system's FFP solutions.

As discussed before, FFP is a complex, dynamic, and distributed process. Agents are well-suited for use in the following applications: (1) distributed computation; (2) communications between components, sensing or monitoring of the environment, or autonomous operation; and (3) processing messages or objects received over a network [50]. This explains why agent-based system — IFFPS — outperforms the regular web-based system for FFP problem. As an agent-based system, IFFPS has sophisticated capabilities such as an ability to reason, learn, or plan. In addition, IFFPS can utilize extensive amounts of knowledge about the FFP problem domain. All these contribute to greater effectiveness in FFP decision support. On the other hand, as IFFPS processes more data and has more capabilities in reasoning, learning, and planning, it should consume more resources and time to achieve the solutions. However, based on the time of two laboratory experiments in our study, there is no significant difference in the system processing time between IFFPS and FFPS.

## 5.6. Limitations

One limitation of this study relates to the university students who were used as subjects. Although they have substantial knowledge of financial planning from their university education and work experience, they cannot really be representative of potential realworld users. Many of the subjects are single, which implies that they have little concern regarding FFP in their personal lives. A further limitation was the fact that the personal financial information provided by the subjects could not be validated. Personal financial information is a key factor in making FFP decisions, and providing real data is critical. Despite asking the subjects to provide real data, we are unable to verify the authenticity of the provided data. In future research, we intend to ask actual potential users to test the system.

## 6. Conclusion and implications

In this study, we proposed a decision-making process model for FFP by applying Simon's [41] classical model of a decision process to the FFP process. Based on this conceptual model, limitations of traditional FFP systems were revealed, such as a unilateral FFP perspective and the lack of multi-party social capabilities. To overcome these limitations, a Web-services, multi-agent-based FFP system was designed and implemented. The system effectiveness was investigated empirically. The main contribution of this study to the research literature can be summarized as follows:

• The decision-making process model of FFP: This is a conceptual model that identifies the specific activities involved in each decision-making phase for FFP. The application of this model can lead to better understanding of the concepts of FFP, and provide a uniform framework within which different approaches can be integrated to provide more sophisticated functions and facilities. By creating a rich conceptual model, the study provides a solid framework for FFP system development practice. This model provides the basis for formal study and leads to analysis, design, and development of FFP systems.

• System design innovation: A novel and open architecture for FFP has been designed by integrating agent technology with Web-services to make use of the advantages from both. This approach leads to more intelligence, flexibility, autonomy, and collaboration in FFP. Different Web-services agents can cooperate to provide comprehensive FFP services, or each Web-service agent can be separated to function as a stand-alone system, selecting and calling other agents' services freely through the Internet, if required. In addition, it is easy to add more business functionalities into our IFFPS by adding more Webservice agents. All Web-service agents are reusable by other business applications. In addition, a laboratory experiment has been designed and conducted to evaluate the effectiveness of our proposed approach. The results show that our proposed solution improves the outcomes, process, and user perception of FFP decision making. This crossdiscipline practice provides a scientific methodology to evaluate DSS effectiveness.

• Business value: A more aggregative and comprehensive solution that can better meet business requirements and support decision making has been proposed. First, most existing FFP systems focus on financial or investment aspects only and do not consider other important issues. In contrast, the IFFPS is able to deal with a much wider business context, including legal and accounting aspects. Second, because of its user-profiling capability, the IFFPS can provide customized solutions to individual users. Third, the IFFPS provides more standard, timely, cost-effective, and conflict-free advisory services, which are superior to the human-based specialist team. Therefore, this approach will bring greater benefit to the current FFP business, such as cutting staff costs, speeding up the business process, standardizing the services provided, etc.

This study yields a new and more general perspective on the use of intelligent-decision support agents to support financial decision making. We believe our research findings will lead to a new stage of technologymediated financial decision support. The results of this study highlight the fact that these important concepts, including the conceptual model, the agent and Webservices technologies, and the architectural considerations required for developing a financial application, can assist in financial decision making.

In the future, we will focus on the following: (i) further development of the FFP system for real-world application followed by a field experiment. To achieve this, we may cooperate with financial institutions, such as banks, stock brokerage firms, and insurance companies to develop the FFP application and ask the real potential users to test the system; (ii) improving our conceptual model, system architecture, and development based on the feedback collected in this study; and (iii) investigating the coordination and negotiation mechanism of agents in FFP.

## Acknowledgements

The authors would like to thank the Bank of Communications (Hong Kong Branch) team, Dr. Michael Wong (Associate Professor, Department of

Economics and Finance, City University of Hong Kong), and Mr. Chen Wang (Merrill Lynch), for their professional advices and supports on this research.

## References

[1] D. Austin, A. Barbir, C. Ferris, S. Garg (Eds.), Web Services Architecture Requirements — W3C Working Group Note 11 February 2004, July 6 2005, Retrieved from the World Wide Web: http://www.w3c.org/TR/wsa-reqs.

[2] C. Barrie, RSM Robson Rhodes Personal Financial Planning Manual 2002–03, 18th ed., Tolley, London, 2002.

[3] F.E. Bender, G. Kahan, W.C. Mylander, Optimization for Profit: A Decision Maker's Guide to Linear Programming, Haworth Press, New York, 1992.

[4] T. Bui, J. Lee, An agent-based framework for building decision support systems, Decision Support Systems 25 (3) (1999) 225–237.

[5] C. Carlsson, E. Turban, DSS: directions for the next decade, Decision Support Systems 33 (2) (2002) 105–110.

[6] J. Clabby, Web Services Explained: Solutions and Applications for the Real World, Upper Saddle River, NJ, Prentice Hall PTR, 2003.

[7] J. Dugdale, M. Keynes, Cooperative problem-solver for investment management, International Journal of Information Management 16 (2) (1996) 133–147.

[8] E.H. Durfee, Distributed problem solving and planning, in: G. Weiss (Ed.), Multiagent systems: a modern approach to distributed artificial intelligence, Cambridge, MA, the MIT Press, 1999, pp. 121–164.

[9] E.H. Durfee, Distributed problem solving and planning, in: M. Luck, et al., (Eds.), Multi-agent systems and applications lecture notes in artificial intelligence, vol. 2086, Berlin, Springer, 2001, pp. 118–149.

[10] A. Dutta, Integrating AI and optimization for decision support: a survey, Decision Support Systems 18 (3–4) (1996) 217–226.

[11] O. Etzioni, D. Weld, A Softbot-based interface to Internet, Communications of the ACM 37 (7) (1994) 72–76.

[12] J. Ferber, Multi-agent Systems: An Introduction to Distributed Artificial Intelligence, Harlow, Addison–Wesley, 1999.

[13] C. Ferris, J. Farrell, What are web services? Communications of the ACM 46 (6) (2003) 31.

[14] S. Franklin, A. Graesser, Is it an agent, or just a program? in: J. Muller, M. Wooldridge, N. Jennings (Eds.), Intelligent Agents III: Agent Theories, Architectures, and Language: ECAI'96 Workshop (ATAL), Budapest, Hungary, August 12–13, 1996 Proceedings, Springer– Verlag, Berlin, 1997, pp. 1–20.

[15] R.B. Gallupe, G. Desanctis, G.W. Dickson, Computer-based support for group problem-finding: an experimental investigation, MIS Quarterly 12 (2) (1988) 277–296.

[16] S.J. Gao, D.M. Xu, Y.F. Wang, H.Q. Wang, Development of a Web-Service-Agents-Based Family Wealth Management System, Proceeding of the Tenth Americas Conference on Information Systems (AMCIS 2004), New York, USA, 2004, pp. 1841–1950.

[17] S.J. Gao, H.Q. Wang, Y.F. Wang, W.Q. Shen, S.B. Yeung, Webservice-agents-based family wealth management system, Expert Systems with Applications 29 (1) (2005) 219–228.

[18] S.J. Gao, H.Q. Wang, D.M. Xu, Y.F. Wang, W.Q. Shen, S.B. Yeung, Intelligent decision support for family financial planning, Proceeding of the 39th Hawaii International Conference on System Science (HICSS-39), Hawaii, USA, 2005.

[19] L.J. Gitman, M.D. Joehnk, Personal Financial Planning, 9th ed., Cincinnati, OH, South-Western/Thomson Learning, 2002.

[20] R.J. Glushko, J.M. Tenenbaum, B. Meltzer, An XML framework for agent-based e-commerce, Communications of the ACM 42 (3) (1999) 106–114.

[21] M.N. Huhns, Agents as Web services, IEEE Internet Computing 6 (4) (2002) 93–95.

[22] Java.sun.com, Java Web Services Developer Pack 1.4, http://java. sun.com/webservices/downloads/webservicespack.html2004.

[23] N.R. Jennings, On agent-based software engineering, Artificial Intelligence 117 (2000) 227–296.

[24] N.R. Jennings, M. Wooldridge, Agent Technology: Foundations, Applications, and Markets, Berlin, Springer–Verlag, 1998.

[25] N.R. Jennings, P. Faratin, T.J. Norman, P. O'Brien, B. Odgers, Autonomous agents for business process management, International Journal of Applied Artificial Intelligence 14 (2) (2000) 145–189.

[26] JESS — the Rule Engine for the Java™ Platform, http://herzberg. ca.sandia.gov/jess/(2004)

[27] S. Kanungo, S. Sharma, P.K. Jain, Evaluation of a decision support system for credit management decisions, Decision Support Systems 30 (2001) 419–436.

[28] J.R. Kapoor, L.R. Dlabay, R.J. Hughes, Personal Finance, 6th ed., McGraw Hill/Irwin, Boston, Mass, 2001.

[29] P.G.W. Keen, M.S. Scott Morton, Decision Support Systems: An Organizational Perspective, Addison–Wesley, Reading, MA, 1978.

[30] A.J. Keown, Personal Finance: Turning Money into Wealth, 3rd ed., Prentice Hall, Upper Saddle River, N.J., 2003.

[31] Merrill Lynch, Identifying Your Investor Profile , 2002 Retrieved from the World Wide Web: http://askmerrill.ml.com/example display/1,534,00.pdf(10 April 2004).

[32] Merrill Lynch, Asset Allocation Strategies, 2004 Retrieved from the World Wide Web: http://askmerrill.ml.com/product\_details 1,2270,20367,00.html (10 April 2004).

[33] P. Maes, Agents that reduced work and information overload, Communications of the ACM 37 (7) (1994) 31–40.

[34] H.M. Markowitz, W.F. Sharpe, M.H. Miller, The Founders of Modern Finance: Their Prize-winning Concepts and 1990 Nobel Lectures, Research Foundation of the Institute of Chartered Financial Analysts, Charlottesville, V.A., 1991.

[35] R.M. O'Keefe, The evaluation of decision-aiding systems: guidelines and methods, Information & Management 17 (1989) 217–226.

[36] R. Orwig, H. Chen, D. Vogel, J. Nunamaker, A multi-agent view of strategic planning using group support systems and artificial intelligence, Group Decision and Negotiation 6 (1) (1996) 37–59.

[37] G.E. Phillips-Wren, E.D. Hahn, G.A. Forgionne, A multiplecriteria framework for evaluation of decision support systems, Omega-International Journal of Management Science 32 (4) (2004) 323–332

[38] F.C. Sainfort, D.H. Gustafson, K. Bosworth, R.P. Hawkins, Decision support systems effectiveness: conceptual framework and empirical evaluation, Organizational Behavior and Human Decision Processes 45 (2) (1990) 232–252.

[39] R. Sharda, S.H. Barr, J.C. McDonnell, Decision support system effectiveness: a review and an empirical test, Management Science 34 (2) (1988) 139–159.

[40] J.P. Shim, M. Warkentin, J.F. Courtney, D.J. Power, R. Sharda, C. Carlsson, Past, present, and future of decision support technology, Decision Support Systems 33 (2) (2002) 111–126.

[41] H.A. Simon, The New Science of Management Decision, Prentice–Hall, Englewood Cliffs, N.J., 1977.

[42] R.H. Sprague, E.D. Carlson, Building Effective Decision Support Systems, Prentice–Hall, Englewood Cliffs, N.J., 1982.

[43] T.S.H. Teo, W.Y. Choo, Assessing the impact of using the Internet for competitive intelligence, Information & Management 39 (1) (2001) 67–83.

[44] G. Udo, Rethinking the effectiveness measures of decision support systems, Information & Management 22 (1992) 123–135.

[45] R. Vahidov, B. Fazlollahi, Pluralistic multi-agent decision support system: a framework and an empirical test, Information & Management 41 (7) (2004) 883–898.

[46] H.Q. Wang, Intelligent agent assisted decision support systems: integration of knowledge discovery, knowledge analysis, and group decision support, Expert Systems with Applications 12 (3) (1997) 323–335.

[47] H.Q. Wang, S. Liao, L. Liao, Modeling constraint-based negotiating agents, Decision Support Systems 33 (2) (2002) 201–217.

[48] H.Q. Wang, J. Mylopoulos, S. Liao, Intelligent agents and financial risk monitoring systems, Communications of the ACM 45 (3) (2002) 83–88.

[49] A. Whinston, Intelligent agents as a basis for decision support systems, Decision Support Systems 20 (1) (1997) 1.

[50] M. Wooldridge, Intelligent agents, in: G. Weiss (Ed.), Multiagent systems: a modern approach to distributed artificial intelligence, the MIT Press, Cambridge, MA, 1999, pp. 27–77.

[51] M. Wooldridge, An Introduction to Multiagent Systems, J. Wiley, Chichester, England, 2002.

[52] M. Wooldridge, N.R. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115–152.

[53] M. Yokoo, E.H. Durfee, T. Ishida, K. Kuwabara, The distributed constraint satisfaction problem: formalization and algorithms, IEEE Transactions on Knowledge and Data Engineering 10 (5) (1998) 673–685.

[54] H. Zhuge, Workflow- and agent-based cognitive flow management for distributed team cooperation, Information & Management 40 (5) (2003) 419–429.

Shijia Gao is currently a PhD candidate at the Business School at the University of Queensland. She was finishing her MPhil degree in the City University of Hong Kong the time she wrote this paper. Her research interests are in the areas of multi-agent support financial applications, decision support systems, knowledge-based systems, knowledge management, and business process management.

Huaiqing Wang is a professor at the Information Systems Department at the City University of Hong Kong. He specializes in research and development of business intelligence systems, intelligent agents and their applications (such as multiagent supported financial information systems, virtual learning systems, knowledge management systems, and conceptual modeling). He received his PhD in computer science from the University of Manchester in 1987.

Dongming Xu received her PhD degree from the City University of Hong Kong in 2004. Currently, she is a Senior Lecturer at the Business School at The University of Queensland. Her research interests include applications of artificial intelligence on business information systems, in particular, specializing on Web-based intelligent agents and their applications, such as knowledge management systems, financial information systems, intelligent virtual learning environments and intelligent Web services. She also undertakes the research of social aspects relating to information systems with particular interest in organizational culture.

Yingfeng Wang is currently a PhD candidate at the Department of Information Systems at the City University of Hong Kong. He was finishing his MPhil degree at the City University of Hong Kong. His research interests are in the areas of multi-agent support financial applications, decision support systems, and business process management.
