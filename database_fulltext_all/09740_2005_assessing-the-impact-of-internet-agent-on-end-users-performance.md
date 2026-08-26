---
otero_id: 9740
otero_key: "PGYRQE6F"
title: "Assessing the impact of internet agent on end users' performance"
authors: "R. Eric Hostler; Victoria Y. Yoon; Tor Guimaraes"
year: "2005"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2004.07.002"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Assessing the impact of internet agent on end users’ performance

R. Eric Hostler<sup>a</sup>, Victoria Y. Yoon<sup>a</sup>, Tor Guimaraes<sup>b,\*</sup>

<sup>a</sup>Department of Information Systems, University of Maryland Baltimore County, Baltimore, MD 21250, USA

<sup>b</sup>Department of Decision Sciences, Tennessee Technological University, Box 5022 Johnson Hall Room #412, Cookeville, TN 38505, USA

Received 2 July 2004; accepted 5 July 2004 Available online 18 October 2004

## Abstract

Intelligent software agents that can perform tasks on the user’s behalf independently of direct control of the user themselves, promise to evolutionize the way in which we use the Internet to conduct business. Research on how these agents will change the nature of Internet-based e-commerce and what its impact will be on consumers and businesses is only just beginning. To assess the impact of agent usage in a retail online shopping environment, an empirical study was conducted to determine what impact, if any, the use of Shopbots, a form of Internet agent, had on consumers looking to purchase a DVD player online via the World Wide Web [WWW]. Of particular interest was the Internet agent’s impact on the user’s task performance and task outcomes. These included the time spent on shopping activities, the shopper’s confidence in their purchase decision, the quality of the purchase decision made by the shopper and the amount of cognitive effort required to select a product for purchase. <sup>D</sup> 2004 Elsevier B.V. All rights reserved.

Keywords: Internet agent; Shopbot; Decision quality; Impact of internet agent; E-commerce; Intelligent agent systems

## 1. Introduction

Business to consumer [B2C] electronic commerce continues to become an increasingly important segment of the economy. It has been estimated that retail sales generated through online sales channels like e-commerce web sites have been growing at an average annual rate of 110% a year [11]. With that kind of phenomenal growth, it becomes critical for business managers to understand what influences consumers to buy over the web, as well as how different technologies impact those purchasing behaviors. One emerging technology that is theorized to have a significant, if not evolutionary, effect on e-commerce is intelligent software agents [15].

While the use of intelligent agents has been reported to offer great benefits, there have been relatively few studies to examine what tangible benefits intelligent agents really provide to consumers. Studies have been conducted to examine what factors motivate individuals to use the web [8,11,16], why they revisit individual web sites [31], what influences individuals to buy online [1,12,13,25] and the process online shoppers use to select a product [22,29,30]. A few studies have directly addressed the impacts of Internet agents on consumers [22,25]. These agents are often called Shopbots, which are a type of merchant brokering agent. Additionally, a study by Conway et al. [4] looked at what impact consumers’ use of intelligent agents may have on businesses that sell online.

The previous studies on these various aspects of web-based B2C e-commerce all have important theoretical implications for this study. They lay a theoretical groundwork that guide us in determining what factors, in the online buying process, may be important on which to measure the agent’s impact. While all these studies address various aspects of shopping online, none of them have been designed specifically to examine the impact agents have on end-user performance in the purchasing process.

The objective of this study is to assess the impact of Internet agent on end users’ performance. The next section presents the overview of agent technology. Followed are the theoretical framework of our conceptual model and the research method. The paper then presents the results of our experiment and discusses those results.

## 2. Agent technology overview

There are various definitions on what an agent is; however, an intelligent agent generally possesses three important properties: autonomy, social ability, and adaptation [20]. First, the autonomy means that an agent operates without the direct intervention of humans or others, and has some control over its own actions and internal state. An agent is capable of independent action [27]. Autonomy also includes an agent’s ability to react to its operating environment and modify its own behavior appropriately as environmental circumstances change. In other words, an agent does not blindly execute tasks, without regard to the state of the environment. Furthermore, autonomy means that an agent does not simply act in response to its environment, and it is able to exhibit goal-directed behavior by taking the initiative.

Second, the social ability refers to an agent’s ability to cooperate and collaborate with other agents and possibly human users to solve problems. Cooperation and collaboration are very important features, especially, for a Multi-Agent System [MAS]. Agents in a MAS share information, knowledge, and tasks among themselves, and cooperate with each other to achieve common goals. The capability of MAS is not only reflected by the intelligence of individual agents but also by the emergent behavior of the entire agent community.

Third, the adaptation refers to an agent’s ability to adapt to the environment, including other agents and human users. An agent learns from experience over time to improve its performance in a dynamic environment. Cantu [2] classified learning in MAS into two main categories: centralized learning and decentralized learning. A single agent performs centralized learning, also called isolated learning; thus, it does not require any interaction with other agents. On the other hand, decentralized learning, also called interactive learning, is performed through the interaction of several agents who cooperate to achieve the learning goals.

A variety of agents have been developed to work on many different problems. Nwana [18] classified agents in several categories: collaborative agent, reactive agent, mobile agent, hybrid agent, heterogenous agent, interface agent, Internet agent, and others. First, based on its architecture, an agent can be classified as either a deliberative or a reactive agent. A deliberative agent has an internal representation of the sequence of actions necessary to achieve a goal given or an event triggered. This agent maintains preplanned action for goals. Meanwhile, reactive agents do not store a priori specification or plan of the actions. No internal representation of pre-plan exists within any of the reactive agents and, hence, the plans have to emerge upon an event through collaboration. Reactive agents tend to operate on representations, which are close to raw sensor data, in contrast to the high-level symbolic representations that abound in the deliberative agents.

Second, based on the functionality, agents are classified as either an Internet agent or an interface agent. Internet agents, also called Shopbots, are designed to ameliorate the problem of information overload and the general issues of information management on the Internet. An Internet agent uses a host of Internet management tools such as Spiders and search engines in order to gather information. The Internet agent may be associated with some particular indexer[s], e.g. a Spider. The Internet agent, which has been requested to gather information on some subject, issues various search requests to one or several URL search engines to meet the request. Some of this search may even be done locally if it has a local cache. The information is then collated and sent back to the author. Meanwhile, the goal of an interface agent is to migrate from the direct command metaphor to one that delegates some of the tasks to the agents in order to accommodate novice users. In order to support and provide assistance to a user to interact with a computer, the interface agent builds a user model to better assist a user in accomplishing tasks by observing and monitoring the actions taken by the user. It learns to improve its performance through receiving positive and negative feedback from the user [14].

Last, the mobility of agents can be classified into mobile or stationary agent. Mobile agents are able to roam the network such as World Wide Web (WWW), interacting with foreign hosts, performing the various duties assigned at a remote site, and come back to its user upon the completion of its task.

Among various agents, we are particularly interested in Internet agents that help users find information on merchandise to purchase, and help the user organize the information for ease of comparison on attributes such as price and availability. To help identify areas where Internet agents may be useful in e-commerce, Maes et al. [15] looked at several consumer buying behavior models. The Nicosia model, the Howard Sheth model, the Engel-Blackwell model, the Bettman information-processing model and the Andreasen model were all found to share six similar stages in the buying process. The stages were need identification, product brokering, merchant brokering, negotiation, purchase and delivery, and product service and evaluation [15]. Uses were identified for agents in each of the first four stages. Several studies have looked at specific uses for intelligent agents [10,15] including managing service level agreements, bidding in online auctions, and price negotiation between buyer and merchant. While some work has been done with agents such as Anderson Consulting’s BargainFinder and Excite.com’s Jango, which are aimed at improving the ease with which consumers can compare prices among several merchants [15], previous studies mostly have addressed the technology used and have neglected the impact of the technology on the users.

## 3. Theoretical framework

The problem of assessing the impact of information systems on end-users performance has long plagued IS researchers. In choosing a method to assess the impact of Internet agents for gathering, sorting, organizing, presenting, and comparing the vast array of products available to consumers, we focus on assessing its impact on the individual user’s performance. System impact on user performance is one commonly used measure of IS success.

A wide variety of systems have been studied to determine their impact on users’ performance and the impact they have on users’ effectiveness and efficiency in performing tasks. Yoon et al. [28] studied the impact of Expert Systems on end users jobs. Several critical factors for the successful implementation of Expert Systems were identified. The relative importance of a factor of Expert System implementation was based on its impact on users performance and their attitudes about the system after implementation.

In a recent study of DSSs, the impact that decisional guidance has on end users’ performance was studied [19]. The researchers’ goal was to determine what impact decisional guidance provided by the system had on the user’s decision-making performance. The level of decisional guidance provided is based in part on how much aid the system provides the user for problem solving, which can range from simply supplying information to making suggestions for alternative courses of action. One of the measurements used was the impact on decision quality, an important factor included in this study as a measure of end-user performance.

Head et al. [9] studied the impact of a WWW navigation aid on end user’s performance. The navigation aid used in the study was a type of search history tool designed to aid users in finding previously viewed information on the WWW. In the sense that the system provides support for information retrieval, the tool has a similar function as an intelligent search agent, albeit using an entirely different strategy in providing that support. The study focused on the systems effect on the users’ efficiency and effectiveness both within the same web-browsing session and between web-browsing sessions. Included in the measure of efficiency is the concept that using the system will reduce the time required to perform a specified task. This, in effect, is a measure of the extent to which using the system improves the users’ performance by saving them time.

Another study related to user’s performance in completing information retrieval tasks was that of Tanin et al. [24]. Their system provided <sup>b</sup>query previews<sup>Q</sup> which provide summary information on the result set returned by the query. Using query previews the user has the ability to assess the size and scope of the results their query will generate before examining the detailed information of the query results. The hypothesized results were that the use of query previews for unclearly defined information retrieval tasks would allow them to be performed faster [24]. The dependent variable used to test the hypothesis was task completion time. Once again, time savings was used as an important indicator of end user performance.

A final example of a study of system success using end user performance as a measure is a study by Chan et al. [3] on the impact of a database feedback system. They examined how users modified their queries based on feedback given by the database. They reasoned that the more feedback the database could provide, the more efficiently the user would be able to obtain the data they needed. To assess the impact the feedback had on the user’s query writing performance, they measured the user’s syntax accuracy, the user’s decision confidence, and task completion time [3].

Many dependent variables have been proposed for measuring system impact on end users’ performance. Among them are time savings, decision quality, decision confidence and cognitive effort [3,5– 7,21,23]. Our conceptual model in Fig. 1 shows the hypothesized relationships between Internet agent use and end-user performance measured by those four variables: time savings, decision quality, confidence in decision and cognitive effort.

Time has been used in many studies as an indicator of user efficiency. When users can perform tasks more efficiently, it increases their level of productivity, improving the users task performance. Previous studies used time spent performing a task as a measure of end-user performance [3,7,24]. Each of these studies found time to be an important indicator of the system’s influence on the performance of the user. Bellman et al. [1] stated that the potential for saving time is one reason people shop online. Limayem et al. [12] found that time savings was a significant perceived outcome of online shopping. Vijayasarathy et al. [26] concluded that using a Shopbot reduced the search and selection time needed to purchase online. Based on the above discussion, we propose:

![](/api/attachments/PGYRQE6F/fulltext/images/b2019ed254d8b248c269d87701dc14bed560456f822f17f8f445654d844dfc63.jpg)  
Fig. 1. The Conceptual Model.

Hypothesis 1. The use of an Internet agent will reduce the amount of time end users spend searching for and selecting a product to purchase online.

In the area of DSS research, decision effectiveness is a commonly used measure of user performance. Decision effectiveness relates to the quality of the decision made based on the information and support provided by the DSS. Decision quality is often measured by how closely the user’s choice or selection from a group of alternatives, matches the <sup>b</sup>ideal<sup>Q</sup> outcome or selection. Prior studies have used decision quality as a measure of user performance by rating the user’s selection against an optimal solution or selection [3,6,21]. Internet agents aid users in several stages of the decision-making process. Shopping aids are designed to be decision aids that help users locate products that closely match their preferences, evaluate and compare different alternatives, and select the best alternative. If Internet agents were effective at providing decision support, then we would expect them to have a measurable positive impact on user performance. More specifically, Internet agents should improve the quality of purchasing decisions made by consumers using online shopping agents over those who shop without the aid of an agent. Consequently, we propose:

Hypothesis 2. The use of an Internet agent will improve the decision quality of online shoppers purchasing decisions.

In addition to decision quality, the users’ level of confidence in their decision can also be an important measure of user performance. Users with more confidence in their decisions are usually regarded as having performed the task more effectively. Decision confidence was used as an indicator of user performance in this manner [3,6].

Consumers who use an Internet agent to help them locate and compare products online will be able to consider more alternatives than those that do not. Additionally, the aid the Internet agent provides in evaluating the possible alternatives should make the consumer more confident that they have found the product that best suits their needs. Shoppers who are not sure that any of the available alternatives meet their needs are also less likely to complete the purchase transaction. Finalizing the sales transaction and converting a prospect into a sale is what ultimately separates successful web-based retailers from the unsuccessful ones. Based on the above discussion, we propose:

Hypothesis 3. The use of an Internet agent will increase the user’s confidence in their purchase decisions for online purchases.

The level of cognitive effort required to perform a task has also been used as an indicator of the impact of a DSS in end-users’ performance. The more effective the DSS at supporting the user, the less mental effort we would expect the user to expend in completing the task. Intelligent agents can aid in the decision-making process by finding products that match the customer’s desired attributes [11]. By offloading detailed search procedures from the user to the agent, it is possible to reduce the cognitive load on the user. This reduction in cognitive load should in turn reduce the customer’s cognitive decision effort. Pereira [21] has shown that reducing cognitive load with the use of query-based decision aids increases the overall user satisfaction experienced by the customer. If the use of an Internet agent does in fact reduce cognitive load, as measured by the customer’s <sup>b</sup>cognitive decision effort<sup>Q</sup>, it is expected that an increase in the customer’s overall level of customer performance may occur. Therefore, we formulate the following hypothesis:

Hypothesis 4. The use of an Internet agent will decrease the amount of cognitive effort required during product search and selection in online shopping environments.

## 4. Research methodology

## 4.1. Experimental design

A between-subjects experimental design was used to examine the impact of software agent usage on Internet consumers. Subjects were randomly assigned to the treatment and control groups using a random number generator. Subjects in the treatment group performed a Web-based online shopping task with the aid of an agent-enabled web site while the control group performed the same task without the aid of the software agent.

The shopping task for the experiment involved shopping for a DVD player for a home entertainment system. Subjects were instructed to shop for a DVD player costing less than US\$300.00 and having certain specific features. The DVD player features specified in the shopping task included parental controls, S-Video, Component Video and Composite Video outputs in addition to Dolby Pro Logic, Dolby Digital, and DTS surround sound formats. The shopping task was designed to narrow the available product space so that all subjects would be engaged in a similar task environment while being specific enough to require some amount of effort to find a DVD player that satisfied the given criteria. Not all subjects were able to find a DVD player that matched the specified criteria before tiring of the search process. This was expected as consumers often make trade-offs between their ideal selection and the amount of time they are willing to search for the ideal product.

Subjects were first given a brief introduction to the purpose of the study and the shopping task they were to perform. While the subjects were informed that online shopping and consumer behavior were of interest to the researchers, at no time was the use of agent technology mentioned or discussed. The subjects were instructed to shop for a DVD player as if they intended to purchase one for themselves. After the introduction, subjects were taken to a college computer lab, which was physically laid out to facilitate the separation of the treatment and control groups. A four-foot high dividing wall passes down the center of the lab effectively dividing the room in half. Subjects were then divided into two groups, referred to as group one and group two, and seated in different halves of the lab based on whether they were a member of group one or group two. Subjects were not told which group was the treatment group and which was the control group, nor were they given any indication as to what the difference was between the two groups.

Once the subjects were seated at a workstation in the lab, they were provided with an instruction sheet that detailed the experiment procedure they were to follow. The treatment and control groups were given identical instruction sheets except that the initial URL the subjects were to set their web browsers to was different.

Upon opening the web browser on their workstation and typing in the URL specified on their instruction sheet, the web page that loaded provided the subject with a randomly generated subject ID number between 1 and 32,000. Subjects were instructed to record this subject ID number at the top of their paper-based pretest and posttest questionnaires. The subject ID served not only to link the data collected electronically during the online shopping simulation with the data collected from the survey questionnaires.

After recording the subject ID number on the survey questionnaire, subjects clicked on a button on the web page to begin the shopping simulation. When the button was pressed, the web page placed a stamp in a database to record the start time of the shopping simulation for each subject. For subjects in the treatment group, the button also opened a second browser window and loaded an agent enabled web site for the subjects to use to begin their shopping task. A second browser window was also opened for the subjects in the control group. However, they were presented with a simple web page that instructed them to use this browser window to search for a DVD player, and were left with their own knowledge of shopping online to decide where to begin shopping.

After completing the online shopping simulation, subjects were to return to the original browser window containing their subject ID number and click on a second button to signify they had completed the online shopping simulation. This button then placed an additional time stamp in the database signifying the ending time of the simulation portion of the experiment.

The final step after ending the shopping simulation was for the subjects to complete a survey questionnaire. The questionnaire contained Likert scale items of statements relating to both the subjects confidence in their purchase decision and the amount of cognitive effort needed to complete the shopping task. In addition to the Likert scale items, the subjects recorded the brand, model and price of the DVD player they selected during the shopping simulation.

## 4.2. Experimental shopbot

The shopbot used by the treatment group during the experiment phase of the study elicited specific information from the user about the type of product they were looking for. Users first needed to select what type of product they were searching for, in this case, a DVD player. After choosing a product type, the shopbot then had some information to work with and could elicit further product information based on the product category specified. The shopbot collected information from the user on product features such as brand, price, media formats, type and number of audio and video outputs, as well as a variety of other features.

The shopbot organized specific product features into groups under the primary product feature headings. Under the <sup>b</sup>brand<sup>Q</sup> product feature group, for instance, the user would find a list of specific brands such as Sony, Samsung, Panasonic, etc. Users could specify as many or as few product features as they liked, they were not required to select an option in each feature group. Users had the additional flexibility of choosing more than one option under each feature heading if they wanted the agent to consider products with more than one specific feature in a given category. For example, if a user wanted the shopbot to select DVD players that had either a component video output or an S-video output, they could select both options under the video output feature heading. This gave users the ability to make their search as broad and general or as narrow and specific as desired.

Finally, the shopbot gave the user the ability to rank the importance of each feature by weighting the attributes selected if they wanted to. Just as with product features, users were not required to provide feature importance rankings. If brand was the most important product feature to the user, they could assign that product feature the highest weighting among the product features specified. By weighting the importance of features, the shopbot could then attempt to make product selection tradeoffs by knowing which features were the most important to the user. Would the customer (user) be more likely to purchase the more expensive model with the all the features they specified, or a specific brand of DVD player with one of the features missing? The shopbot attempted to choose products based on not only the features they had, but also on which features were most important to the customer.

After gathering the relevant information from the user, the shopbot then performed a web search across a variety of vendor and retailer web sites looking for products that matched the users stated preferences. Once the shopbot had completed its search, it presented the search results to the user in a table format for product comparison purposes. The shopbot sorted the product information in the table based on which products it felt most closely matched the user’s criteria. Any products that exactly matched the user’s preferences are at the top of the table, and proceeding towards the bottom are products that begin to make tradeoffs between product features, but still closely match some portion of the stated criteria. If several products had the same features, feature weightings further sorted them, if the user provided any.

The shopbot used in the experiment provided decision support to the subjects in the treatment group through its ability to use this information to identify products of interest to the subject (customer). The shopbot was designed to alleviate the need for the subject to take all of this product feature and feature ranking information into account for every DVD player they examined because the shopbot only presented them with products that had already been filtered and sorted based on those criteria. It also alleviated the need for subjects to perform the same search repetitively on multiple web sites. The shopbot eliminated that extra effort by simultaneously searching a variety of sources for the requested information.

## 4.3. Sampling

A sample of 85 undergraduate students was invited to participate in this study. Of 85 students invited, 69 students agreed to participate in this experiment. Participation in the study was purely voluntary. The students were all from upper division Information Technology courses at a private liberal arts college.

## 4.4. Measurement of variables

To measure end-user performance, four variables were used: time spent, decision quality, confidence in the decision, and cognitive effort. Time spent on the online purchasing task was measured by the duration of time a subject spent on the online shopping simulation portion of the experiment. This included the amount of time spent selecting a website to shop on, product search time and product selection time. Time was measured by recording the start time and end time of the online shopping simulation from each subject. The difference between the start time and end time in minutes and seconds was the time spent on the online shopping task used in the data analysis.

Decision quality was measured by the degree to which the user’s product selection met the product feature criteria specified in the experiment procedures. The eight features specified were total cost [with shipping] of less than US\$300, parental controls, svideo, composite video and component video outputs, Dolby Pro-logic, Dolby Digital, and DTS surround sound formats. Each of the features was coded as either 1 (present) or 0 (absent) for the DVD player selected by the subject. The aggregate score of the feature set was used as an indicator of decision quality. Decision quality scores may range from 0 (no specified features present) to 8 (all specified features present).

The level of confidence a user had in their purchase decision was measured by a set of six Likert scale items adapted from Pereira [21]. For example, subjects were asked to rate the level of agreement, ranging from 1 (strongly disagree) to 7 (strongly agree), with how confident they felt regarding whether they had chosen the best DVD player to meet the specified criteria, whether or not they felt there may have been other DVD players that they should have examined more closely, and if they felt they would make the same purchase decision again. A <sup>b</sup>confidence in decision<sup>Q</sup> score was then derived as the sum of the subject’s responses from the six related questionnaire items.

The amount of cognitive effort required to perform the online shopping task was also measured using a set of six Likert scale items adapted from Pereira [21]. For example, using the same rating scheme specified above, subjects were asked to rate the level of agreement with statements regarding whether they felt finding the DVD player by shopping online was difficult, if it seemed to have taken a long time, and if they felt the online shopping process was simple or complex. As with the user’s confidence in their decision, a <sup>b</sup>cognitive effort<sup>Q</sup> score was derived as a sum of the responses from the related Likert scale items.

## 4.5. Data analysis

With a sample size of 69 subjects, comparisons of group means were performed using non-parametric procedures. Specifically, the Mann–Whitney test was used to test the homogeneity of variance between the control group and the treatment group. The same Mann–Whitney tests were also employed to test the four hypotheses proposed in this study.

## 5. Results

Standard demographic information about the subject was collected during the study as a part of the battery of questions on the survey questionnaire. Of 69 students participating in this study, the sample was comprised of 39 males and 30 females, with an average age of 22. Subjects reported working an average of 5.9 years, and most of the subjects stated that they did not use the Internet extensively in performing their current jobs.

## 5.1. Instrument validation

Factor analyses were performed to test the construct validity of multiple scales used to measure confidence in decision and cognitive effort. The factor analysis of the six items used for confidence in decision yielded the only factor whose eigenvalue is greater than one. Factor loadings on the six items were all high, ranging from 0.73 to 0.87. The factor analysis of the six items employed in cognitive effort also indicated a single factor, and factor loadings of those six items ranged from 0.75 to 0.91, which are all above an acceptable level of 0.5. Factor analyses showed that the items for each scale loaded unambiguously, thus indicating construct unidimensionality, a requirement for computing the Cronbach’s alpha.

Cronbach’s alpha was used to test for reliability for the item scales. The Cronbach’s alpha of the six-item scale employed to measure confidence in decision was 0.87, indicating very high-level internal consistency. The internal consistency reliability (Cronbach’s alpha) of the six-item scale used to measure Cognitive Effort was 0.93, which is also well above the level of 0.50 acceptable for exploratory studies [17].

## 5.2. Pretest

The Mann–Whitney tests were performed to test for differences between the control group and the treatment group in 12 pretest items. The pretest results show that homogeneity of variance between the treatment and control groups held in all 12 items. There were no significant differences between the two groups regarding their experience with personal computers, knowledge of Internet usage, on-line shopping on the Internet, or knowledge of consumer electronics, as shown in Table 1.

## 5.3. Hypotheses testing

The Mann–Whitney tests were also utilized to test the four hypotheses formulated in this study. As presented in Table 2, the mean time spent searching for a DVD player during the on-line shopping simulation for the control group was 17 min, 42 s. The mean time spent by the treatment group for the same task was 12 min, 17 s. The Mann–Whitney test results indicated a significant difference between the times the two groups spent on the on-line shopping simulation with a significance level of $\scriptstyle p = 0 . 0 1 5 .$ . The data collected suggest that on average, the subjects who used the agent in their product search took 5 min, 25 s less time to find a DVD player. This outcome supports Hypothesis 1, which states that using an Internet agent will increase the users performance by saving them time.

The analysis results also support Hypothesis 2 as a statistically significant difference in decision quality between the treatment and control groups. The mean score of the decision quality variable for the control group was 7.3, while the corresponding score from the treatment group was 7.7. The Mann–Whitney test shows a significant difference ( p value of 0.023), indicating that the subjects who shopped with the aid of the agent made better overall purchase decisions.

The data analysis revealed no significant differences in either the subjects’ decision confidence or their perception of the mental effort required to perform this particular online shopping task. Therefore, Hypotheses 3 and 4 must be rejected. A possible explanation for these negative results is that the shopping task used in this study was not complex enough to allow discrimination between the use or nonuse of Internet agents. Further research in this area is needed to explore the possible impact of Internet agents on these two facets of user performance.

Table 1  
Result of pretest for homogeneity between two groups

<table><tr><td>Pretest items</td><td>Mean control group</td><td>Mean treatment group</td><td>M-W test [p value]</td></tr><tr><td>Computer experience</td><td>5.76</td><td>5.89</td><td>0.638</td></tr><tr><td>Internet experience</td><td>5.85</td><td>5.78</td><td>0.568</td></tr><tr><td>On-line shopping experience</td><td>4.76</td><td>5.03</td><td>0.526</td></tr><tr><td>Internet search experience</td><td>5.61</td><td>5.81</td><td>0.501</td></tr><tr><td>Frequency of internet use</td><td>6.12</td><td>6.11</td><td>0.770</td></tr><tr><td>Frequency of on-line shopping</td><td>3.67</td><td>3.78</td><td>0.674</td></tr><tr><td>Computer literate</td><td>5.79</td><td>5.81</td><td>0.950</td></tr><tr><td>Knowledge about consumer electronics</td><td>5.00</td><td>4.92</td><td>0.960</td></tr><tr><td>Shopping experience of consumer electronics</td><td>4.70</td><td>4.69</td><td>0.717</td></tr><tr><td>Knowledge about DVD technology</td><td>4.61</td><td>4.42</td><td>0.946</td></tr><tr><td>Experience in using a DVD player</td><td>4.73</td><td>4.39</td><td>0.573</td></tr><tr><td>Experience in purchasing a DVD player</td><td>3.76</td><td>3.69</td><td>0.902</td></tr></table>

Table 2  
Result of hypotheses testing

<table><tr><td>Major study variables</td><td>Mean control group</td><td>Mean treatment group</td><td>M-W test [p value]</td></tr><tr><td>Time</td><td>17 min 42 s</td><td>12 min 17 s</td><td>0.015</td></tr><tr><td>Confidence in decision</td><td>27.76</td><td>27.83</td><td>0.356</td></tr><tr><td>Cognitive effort</td><td>28.12</td><td>29.94</td><td>0.178</td></tr><tr><td>Decision quality</td><td>7.3</td><td>7.7</td><td>0.023</td></tr></table>

## 6. Discussion and conclusions

The main objective of this study was to assess the impact of an Internet agent on end users’ shopping decision performance. As measured by reducing the necessary time, improving decision quality, user confidence about the decision made, and the reduction of the necessary mental effort. The assessment was at least partially successful and provided useful insights for the continuation of studies on this important topic. Before discussing the study limitations and further research opportunities, we discuss the implications of the results from this study to e-commerce shoppers and service providers.

This study has shown that the use of Internet agents can be useful for individual shoppers at home or at work for saving time and improving decision quality. As Internet shopping proliferates and the number of purchasing decisions per user increases, the use of decision aids becomes increasingly necessary. It behooves consumers to learn about the potential and limitations of Internet Agents as decision support tools. Needless to say, the characteristics of specific agents must be well understood before such tools can gain widespread acceptance.

It is important for business managers considering a web-based e-commerce sales strategy to understand the potential positive and negative implications intelligent agent technology has in the online shopping space. Those organizations that understand this new technology and its impact are then better positioned to compete in the market. In the future, it may not be enough just to provide consumers with a large selection of products to browse from the comfort of their homes. Websites, which find new ways to leverage the available technology to help and guide the user through the online shopping experience, will have a distinct advantage. Shopbots and other forms of intelligent shopping agents are likely to play an integral role in that evolutionary process.

Not only does this study have implications for online retailers and their customers, it also has implications in the B2B e-commerce arena. One of the fastest growing segments of B2B e-commerce is e-Procurement. Agent technology such as shopbots could be particularly useful to purchasing agents who need to purchase highly specialized products or components. For example, a purchasing agent who is responsible for buying electronic components with highly specific specifications such as power requirements, voltages levels, etc., could use a shopping agent to help locate the best supplier that can provide the appropriate components. In situations that require technical expertise or specialized knowledge, the agent’s ability to assess a product’s appropriateness for a given application could be a significant advantage, given that the agent can improve the user’s decision-making.

For businesses that sell product lines of highly complex products like electronic components, providing an agent to assist their customers in finding and selecting the appropriate products could yield a significant competitive advantage over their competitors. Before a vendor decides to embark on this kind of technology initiative, they need to understand how the agents will affect their customers and how that influences agent design. Knowing that agents can increase customer’s decision-making performance will not be enough. Further research will need to be done to determine which agent features or characteristics produce the desired effects. Our research suggests that agents can save customers time, but what is it exactly that the agent does that has the most significant impact on time savings? Is it the agent’s ability to search across multiple information sources, its ability to analyze and organize data, or must all these features be present? We see our research as a beginning point for further research in these areas. If agents are good at providing user performance benefits such as time savings and decision confidence, then we should ask what it is that they do that provides those benefits. Moreover, when research such as ours suggests that agents are not very proficient in increasing decision confidence or reducing cognitive effort, again we should ask why this is so.

While this study provided useful insights into the use of Internet agents as shopping tools, it has many limitations, which represent opportunities for further research on this important topic. There is need for the identification and assessment of other user performance variables, which may benefit from the use of agents. Another important study would be the identification and assessment of various agent characteristics, which may make them more useful for ecommerce. From a methodological viewpoint, the use of a larger sample size may allow for the identification and assessment of user characteristics, which may provide useful clues for the design and development of new agent systems. The research opportunities are endless and represent a very important component of making the Internet an important new area of economic activity.

## References

[1] S. Bellman, G.L. Lohse, E.J. Johnson, Predictors of online buying behavior, Communications of the ACM 42 (12) (1999) 32 – 38.

[2] F. Cantu, Reinforcement and Bayesian Learning in Multiagent Systems: The MACS Project, Working Paper, 2000.

[3] H.C. Chan, K.K. Wei, K.L. Siau, The effect of a database feedback system on user performance, Behaviour & Information Technology 14 (3) (1995) 152 – 162.

[4] D.G. Conway, G.J. Koehler, Interface agents: caveat mercator in electronic commerce, Decision Support Systems 27 (4) (2000) 355 – 366.

[5] W.H. DeLone, E.R. McLean, Information systems success: the quest for the dependent variable, Information Systems Research 3 (1) (1992) 60 – 95.

[6] G.W. Dickson, G. DeSanctis, D.J. McBride, Understanding the effectiveness of computer graphics for decision support: a cumulative experimental approach, Communications of the ACM 29 (1) (1986) 40–47.

[7] J. Etezadi-Amoli, A.F. Farhoomand, A structural model of end user computing satisfaction and user performance, Information and Management 30 (1996) 65– 73.

[8] T. Fenech, Using perceived ease-of-use and perceived usefulness to predict acceptance of the World-Wide Web, Computer Networks and ISDN Systems 30 (1–7) (1998) 629 – 630.

[9] G. Haubl, V. Trifts, Consumer decision making in online shopping environments: the effects of interactive decision aids, Marketing Science 19 (1) (2000) 4 – 21.

[10] M. Head, N. Archer, Y. Yuan, World Wide Web navigation aid, International Journal of Human–Computer Studies 53 (2000) 301 – 330.

[11] M. Klusch, Information agent technology for the internet: a survey, Data and Knowledge Engineering 3 (2001) 337 – 372.

[12] A.L. Lederer, D.J. Maupin, M.P. Sena, Y. Zhuang, The technology acceptance model and the World Wide Web, Decision Support Systems 29 (3) (2000) 269 – 282.

[13] M. Limayem, M. Khalifa, A. Frini, What makes consumers buy from internet? A longitudinal study of online shopping, IEEE Transactions on Systems, Man and Cybernetics 30 (4) (2000) 421–432.

[14] G.L. Lohse, P. Spiller, Electronic shopping, Communications of the ACM 41 (70) (1998) 81 – 87.

[15] P. Maes, R.H. Guttman, A.G. Moukas, Agents that buy and sell, Communications of the ACM 42 (3) (1999) 81– 87.

[16] J.W. Moon, Y.G. Kim, Extending the TAM for a World-Wide-Web context, Information and Management 38 (4) (2001) 217– 230.

[17] J.C. Nunally, Psychometric Theory, McGraw-Hill, New York, NY, 1978.

[18] M. Parikh, B. Fazlollahi, S. Verma, The effectiveness of decisional guidance: an empirical evaluation, Decision Sciences 32 (2) (2001) 303–331.

[19] Y. Peng, T. Finin, Y. Labrou, R. Cost, B. Chu, J. Long, W. Tolone, A. Boughannam, An Agent-based Approach For Enterprise Integration—The CIIPLEX Experience (1998) http://umbc.edu/\~finin/papers/aai98.pdf.

[20] R. Pereira, Influence of query-based decision aids on consumer decision making in electronic commerce, Information Resources Management Journal 14 (1) (2001) 31 – 48.

[21] J. Rowley, Product searching with shopping bots, Internet Research: Electronic Networking Applications and Policy 10 (3) (2000) 203 – 214.

[22] M. Smith, E. Brynjolfsson, Consumer Decision-Making at an Internet Shopbot: Brand Still Matters, Journal of Industrial Economics 4 (2001) 541 – 558.

[23] B. Szajna, Empirical evaluation of the revised technology acceptance model, Management Science 2 (1) (1996) 85 – 92.

[24] E. Tanin, A. Lotem, I. Haddadin, B. Schneiderman, C. Plaisant, L. Slaughter, Facilitating data exploration with query previews: a study of user performance and preference, Behaviour & Information Technology 19 (6) (2000) 393 – 403.

[25] L.R. Vijayasarathy, J.M. Jones, Print and internet catalog shopping: assessing attitudes and intentions, Internet Research: Electronic Networking Applications and Policy 10 (30) (2000) 191– 202.

[26] L.R. Vijayasarathy, J.M. Jones, Do internet shopping aids make a difference? An empirical investigation, Electronic Markets 11 (1) (2001) 75–83.

[27] M. Woolbridge, N.R. Jennings, Intelligent agents: theory and practice, Knowledge Engineering Review 10 (2) (1995) 115– 152.

[28] Y. Yoon, T. Guimaraes, A.B. Clevenson, Assessing determinants of desirable ES impact on end-users jobs, European Journal of Information Systems 5 (1996) 273 – 285.

[29] S.T. Yuan, A. Liu, Next-generation agent-enabled comparison shopping, Expert Systems with Applications 18 (4) (2000) 283 – 297.

[30] S.T. Yuan, A. Liu, Next-generation agent-enabled comparison shopping, Expert Systems with Applications 18 (4) (2000) 283 – 297.

[31] P. Zhang, G.M. von Dran, Satisfiers and dissatisfiers: a twofactor model for website design and evaluation, Journal of the American Society for Information Science 51 (14) (2000) 1253– 1268.

R. Eric Hostler is an Assistant Professor of Information Systems in the Business Administration Department of York College of Pennsylvania. He has a BS in Information Systems and an MBA, both from York College. Currently, he is studying the effects of intelligent software agents in electronic commerce as a doctoral student in Information Systems Management at the University of Maryland Baltimore County. His other research interests include the implications of information visualization techniques to web-based e-commerce.

Victoria Y. Yoon is an Associate Professor in the Department of Information Systems at University of Maryland Baltimore County. Before that, she was an Associate Professor in the Department of Information Systems at Virginia Commonwealth University. She received her MS from the University of Pittsburgh, and her PhD from the University of Texas at Arlington. She has published over 30 articles in leading journals such as MIS Quarterly, Decision Support Systems, Journal of Management Information Systems, Information and Management, Journal of Operation Research Society, and others.

Tor Guimaraes has been rated by several independent sources as one of the top researchers in the world based on publications in the top IS journals. He holds the Jesse E. Owen Chair of Excellence at Tennessee Technological University. He earned a PhD in MIS from the University of Minnesota and an MBA from California State University, Los Angeles. Tor was Department Chairman and Professor at St. Cloud State University. Before that, he was Assistant Professor and Director of the MIS Certificate Program at Case-Western Reserve University. He has been the keynote speaker at numerous national and international meetings sponsored by organizations such as the Information Processing Society of Japan, Institute of Industrial Engineers, Sales and Marketing Executives, IEEE, Association for Systems Management, and the American Society for Quality Control. Tor has consulted with many leading organizations including TRW, American Greetings, AT and T, IBM and the Department of Defense. He is on the board of directors of several national and international business organizations and is a top strategic advisor to their CEOs. Working with partners in more than 30 countries, Tor has published over 150 articles dealing with the effective use and management of IS and related technologies.
