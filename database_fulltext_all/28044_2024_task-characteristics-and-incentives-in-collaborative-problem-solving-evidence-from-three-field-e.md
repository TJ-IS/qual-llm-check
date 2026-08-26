---
otero_id: 28044
otero_key: "RXPGUTM2"
title: "Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments"
authors: "Jayarajan Samuel; Zhiqiang (Eric) Zheng; Vijay Mookerjee"
year: "2024"
journal: "Information Systems Research"
doi: "10.1287/isre.2021.0118"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Task Characteristics and Incentives in Collaborative Problem Solving: Evidence from Three Field Experiments

Jayarajan Samuel,<sup>a</sup> Zhiqiang (Eric) Zheng,<sup>b,</sup>\* Vijay Mookerjee<sup>b</sup>

<sup>a</sup> Information Systems and Operations Management, College of Business, The University of Texas at Arlington, Arlington, Texas 76019; <sup>b</sup> Information Systems and Operations Management, Jindal School of Management, The University of Texas at Dallas, Richardson, Texas 75080 \*Corresponding author

Contact: jayarajan.samuel@uta.edu, https://orcid.org/0009-0002-9607-2756 (JS); ericz@utdallas.edu, https://orcid.org/0000-0001-8483-8713 (Z(E)Z); vijaym@utdallas.edu, https://orcid.org/0000-0001-5583-3585 (VM)

Received: February 28, 2021 Revised: June 1, 2021; August 8, 2022; April 4, 2023 Accepted: April 20, 2023 Published Online in Articles in Advance: June 6, 2023

https://doi.org/10.1287/isre.2021.0118

Copyright: © 2023 INFORMS

Abstract. We study, using three sequential field experiments, collaborative problem solving in knowledge work enabled by information technology within the context of the customer support function in a leading high-technology firm. Experiment one examines the performance change after introducing a new collaborative problem-solving process, specifically whether the use of a team of experts across departments to solve problems can help reduce problem-solving costs. In addition to the extant process of supporting customers using problem solvers within a specific department, the experiment allowed two forms of engaging problem solvers outside the department: (1) formal handover (transferring the task to experts in an external department) and (2) using a new, collaborative process in which experts across two departments jointly work on the task. Interestingly, we find that the cost reduction occurs not because the collaborative process is always superior to formal handover, but becaus there is a shift of intradepartmental customer support work toward the new collaborative process. Building upon the findings of experiment one, experiment two aims to identify the conditions under which the new collaborative process works or fails. We discover that task features, such as novelty and time constraints, play a significant role in determining the appropriate mode of engaging an external department for problem solving. These findings are then utilized to develop an information system that provides recommendations on how to seek help through either formal handover or collaboration. In experiment three, we examine how users react to the recommendation. We find that local (department level) incentives can cause problem solvers to deviate from machine recommendations. We analyze the underlying reasons for this deviation and demonstrate how global (firm level) incentives can be aligned with local incentives to increase compliance with machine recommendations. The findings of this study offer practical implications for firms that aim to develop and implement information systems to support knowledge-intensive problem-solving tasks.

History: Param Singh, Senior Editor; Yili (Kevin) Hong, Associate Editor. Supplemental Material: The online appendix is available at https://doi.org/10.1287/isre.2021.0118.

Keywords: collaborative problem solving • field experiments • task-process matching • incentive alignment

## 1. Introduction

The organization of groups to accomplish work jointly in an effective and efficient manner is an important goal of management. However, creating and sustaining effective teams for work accomplishment is an ongoing challenge in firms. On the one hand, organizing a firm into distinctly bounded departments helps firms build expertise, allocate work, and achieve economies of scale. On the other hand, collaboration across functional teams adds new knowledge to problem solving, bringing new perspectives not found in functional specialization. Especially with knowledge work, collaboration among teams is the new norm (Wuchty et al. 2007, Singh and Fleming 2010, Toh and Polidoro 2013).

However, achieving successful collaboration across functional teams is not always easy. Although prio research identifies various obstacles to successful col laboration, such as team makeup (Jones 2009, Toh and Polidoro 2013), free-riding (Latane ´ et al. 1979), team dynamics (Reagans and Zuckerman 2001, Randel and Jaussi 2003, Onal Vural et al. 2013), the role of senio management decisions (Li et al. 2007), and coordination costs (Gardner 2016), the choice of appropriate tasks that are conducive to cross-functional team success has not received the needed attention. Early work by Hackman (1968) shows that task difficulty increases the need for collaboration. Subsequent work by Daley (1978) establishes, using surveys, that team collabora tion is the choice for highly uncertain tasks. Although some work documents that complex tasks require team collaboration (Autor et al. 2003, Fiore and Wiltshire 2016, Graesser et al. 2018), the literature is silent on how task characteristics, in general, shape collaborative problem solving. This is especially puzzling given the importance of task assignment; the existence of clearly defined task characteristics in a high-technology, industrial setting; and the common use nowadays of task management tools, such as Microsoft 365, Monday, and Jira software. In our first research question, we, hence, investigate the role of task characteristics (specifically complexity, uncertainty, and urgency) in the success of collaborative problem solving in cross-functional teams.

Another important aspect of making collaborative work successful is ensuring that individuals make the correct collaboration choices. Individuals’ decisions to collaborate are driven by both benefits to the organization and personal rewards (Merton 1968, Vakili et al. 2021). If these two benefits are not aligned, it is possible that knowledge workers may not choose to collaborate when, in fact, they must. As Bikard et al. (2015) and Kay et al. (2018) point out that the sum of individual credit exceeds 100% in successful collaboration. Despite its importance, how incentive misalignment impedes collaboration in an industrial setting and how to align individuals’ incentives with the goal of the firm has not received its due attention in the literature. Our second research questions, thus, aims to contribute to this important issue by providing strategies to correct incentive misalignment in order to sustain cross-functional collaboration.

These gaps in the research exist partially because of the lack of fine-grained data available to researchers. With the ability of information technology, in almost all industries, it is possible to collect, store, and use individual and task-level data for analysis. Our data are from a world-leading, high-tech firm within the information and communications industry. Engineers receive a troubleshooting case from a customer (an internet service provider) when certain telecommunication equipment malfunctions. The engineer receiving the case from a customer may solve it within the receiving department (called the customer specialist department, specializing in knowledge of customer operations). Otherwise, help could be sought from an engineer from an outside department (called the product specialist department, specializing in product knowledge). The key issue here is the manner of seeking product specialists’ help. This can occur in two ways: (1) using a formal handoff to the product specialist department or (2) using a collaborative approach, in which an ad hoc team comprising customer and product specialist personnel jointly work on the case. The formal handoff approach benefits from the efficiencies of functional specialization, whereas the cross-functional, collaborative approach can provide effective solutions to problems that require knowledge that spans departmental boundaries.

We first report the results of a field experiment (experiment one) conducted to study the value of collaboration in problem solving. A new work form, namely, collaborative problem solving, was introduced in the experi mental period. At the same time, the traditional, handoff work form was still kept as an available option of choice. Not surprisingly, the presence of the new work form (collaboration) was found to be beneficial in reducing problem-solving costs. A second field experiment (exper iment two) revealed insights on the source of benefits accruing from the collaborative work form as well as the characteristics of tasks conducive to collaboration. This experiment confirmed that tasks with high difficulty and urgency, that is, customer problems that originate from an emerging technology in wireless telecommunications,<sup>1</sup> which are under a time crunch to solve, are best accomplished in a collaborative manner. However, if a difficult task is not urgent with low task uncertainty, that is, a case originating from an emerging technology and not under a time crunch for which little investigation is needed to solve it, then the work is best accomplished within each functional team separately. In fact, in the latter type of tasks, collaboration has an adverse effect on the problem-solving cost.

Having established the task characteristics conducive (detrimental) to collaboration, the firm implemented an information system artifact, HRTech Analytics, to guide engineers on when to collaborate and when to use formal handover (FH). The recommendation system was designed to achieve the firm’s goal of reducing total problem-solving costs. In experiment three, we offered machine recommendations to problem solvers. The aim was to study how local (department level) incentives could affect whether problem solvers followed the recommendations. We found that, if engineers perceive a decrease in their team’s value in the problem-solving process, they tend to self-correct by under-collaborating. This gives us evidence that choices to collaborate on tasks could be affected negatively if local incentives are not aligned with the firm’s goals. We then proceeded to advise management to update their incentive system to remove any perception that collaboration may be reducing the customer support team’s value within the firm. After the realignment of incentives, we observed that engineers were then making decisions solely based on the merits of collaboration to the firm.

Our research makes two major contributions to organizations that are interested in implementing information systems to support knowledge-based problem-solving tasks. There are two levels of support that information systems offer in our study. First, the problem-solving process itself benefits from the use of information technology tools (collaboration tools). However, we find that collaboration tools must be used in a judicious manner. Here, we discover the importance of task characteristics that benefit (hurt) from a collaborative problem-solving approach. We find evidence that tasks with higher difficulty in their solution and those have high urgency in their solution timeline are best suited to use the collaborative problem-solving approach. Conversely, even difficult tasks may be accomplished without collaboration if the solution is not urgently needed. These results make an important contribution to the collaborative problem-solving literature by connecting task characteristics with the need for team collaboration.

Another level at which information systems can benefit problem solving is to guide problem solvers on workflow choices, that is, the solution process best suited to the problem (formal handover versus collaboration). Here, our research contributes by identifying the role of incentives in the successful implementation of a recommendation system. We show that, if local incentives are not aligned with the firm’s goals, then problem solvers tend to avoid collaborative problem solving even when it is warranted. Our findings, therefore, have wider managerial implications in an organizational setting in which an information system is used to guide problem solvers on workflow choices.

## 2. Prior Work

Our high-level goal is to study what makes a successful implementation of collaboration in cross-functional teams. However, in knowledge work, individuals are free to collaborate as they see fit. The decision to collaborate comes out as a trade-off between its benefits and costs.

Collaboration as a work form has many benefits: it increases productivity and performance (Jones 2009, Reagans et al. 2016); enhances innovativeness (Toh and Polidoro 2013); and increases the probability of generating good ideas, simultaneously curbing bad ones (Singh and Fleming 2010). However prior work mainly focuses on the makeup of teams to reap the benefits of collaboration (Reagans and Zuckerman 2001). Randel and Jaussi (2003) find that team members with strong personal identity perform poorly in cross-functional teams if they are in the minority. Onal Vural et al. (2013) focus on the team structure and experience in scientific inventions.

Equally important are the task characteristics that can influence the success or failure of team collaboration on which the literature is thin. The reasons are twofold. First, what task characteristics matter and the definition of the task characteristics lacks consensus. Works by Hackman (1968), Wood (1986), and Campbell (1988) highlight the importance of task difficulty and complexity. Hackman (1968) and Daley (1978) show that an increase in task complexity and uncertainty requires a higher level of collaborative work. More recent work also documents that task difficulty increases the use of team collaboration (Autor et al. 2003, Fiore and Wiltshire 2016, Graesser et al. 2018). However, in a knowledge-intensive work environment, other temporal characteristics of tasks, such as task urgency, also need to be accounted for. Second, it is only now that we have the ability to collect and analyze task characteristics at the microlevel because of the ubiquitous use of information technology tools in almost all industries. As far as we know, this research is the first to establish, empiri cally, the role of fine-grained task characteristics, such as difficulty, uncertainty, and urgency in successful work collaboration.

The costs to collaboration are also many. It can lead to social loafing (Latane ´ et al. 1979), increase coordination costs (Cummings and Kiesler 2007, Gardner 2016), and increase conflict (Goncalo et al. 2015). In addition, there could also be individual costs to engaging in collaborative problem solving. Early work by Merton (1968) shows that individuals could be disproportionately rewarded for joint work. Similarly, Lissoni et al. (2020) find that junior scientists are credited less than their senior colleagues for the same amount of work.

Individuals choose to collaborate if the benefits exceed its costs (Bikard et al. 2015). In scientific research collaboration, Vakili et al. (2021) show that authors increase collaboration if they are credited more individ ually. Surprisingly, this misalignment of incentives in an industrial setting is not reported. We, hence, posit that, if the individual’s incentives, for example, reward, recognition, etc., are not aligned with the firm’s goals, for example, higher productivity and performance, then individuals may not choose to collaborate when, in fact, they should. This misalignment of individual incentives can be a major detriment to successful implementation of cross-functional teams even in the presence of other facilitators of team success, such as team makeup and task characteristics. We, hence, fill in this gap by studying the role of incentives in an industrial setting with the aid of fine-grained data.

Our research first empirically shows that choosing the right work items, that is, task characteristics to col laborate, increases efficiency and decreases costs in the overall system. Second, we identify a major misalignment in individual incentive to collaborate that affects individual decisions to collaborate, thereby reducing firm performance. We, finally, address this misalignment and show how cross-functional teams can be made effective.

## 3. Research Context

We are motivated by the quest of a large firm in the information and communication technology (ICT) industry to increase its customer care division’s performance by fostering collaboration in work assignments. The ICT category of businesses includes computer hardware and software, communications, networking, and other information and technology products.

Our firm of study operates a highly profitable customer care services division that supports large communication network solutions for its customers. The customer care division has product support contracts with various network, internet, and telecommunication service providers. These contracts allow the customers to open support or service tickets with the firm for operational problems in their networks. For example, a customer might be experiencing an internet outage for its subscribers in a specific geographical area. This outage can be reported by opening a service ticket with the firm for troubleshooting and resolution.

In its existing business process, the firm employs two groups of engineers who work on customer cases. Cases that require knowledge of the customer’s deployment architecture are handled by a customer specialist team, and cases that require in-depth knowledge of the product architecture are handled by a product specialist team. Work items that fit in one of these two categories of expertise are solved by one of the two teams. With the increasing complexity of ICT networks and higher demands by the customers, increasingly, cases do not always fit exactly into either of these categories. Such new cases need to be solved in a collaborative manner by both the teams working together cross-functionally across their respective organizational units.

In order to tackle such cross-functional work items in a successful manner, we propose a data-driven approach to help augment the collaborative process and conducted a field experiment to assess the efficiency and effectiveness of this new process.

## 3.1. Customer Care Organizational Structure

The firm’s customer care business consists of two groups. A customer specialist group (CSG) maintains a team of customer specialist engineers to solve cases coming directly from customers. A more specialized product specialist group (PSG) supports work on more complex cases. These complex cases are sent to the product specialist by the customer specialist engineers after initial investigation. The customer and product specialists represent two separate functional teams. This two-tier structure is common to many customer care organizations in high-technology firms.

The customer specialist engineers have in-depth knowledge of their customer installations and can solve most of the cases that come in from their customers. However, these engineers have limited expertise in the design of the products they support and rely on the product specialist team for more in-depth technical help. Hence, a small number of cases that require in-depth product knowledge are sent over to be solved by the product specialist team.

## 3.2. Customer Care Process

Incoming cases are first assigned to customer specialist engineers. If the customer specialist engineer needs help with the resolution, the case is sent over to the product specialist group for more advanced investigation and resolution.

3.2.1. Traditional Customer Care Process. The tradi tional customer care process is illustrated in Figure 1 and works in the following way:

• Customer opens a new case (when the product malfunctions).

• The case is received by a customer specialist engineer in CSG who starts diagnosing the problem.

• If the engineer can solve the case at this point, the engineer provides the solution and responds back to the customer with a closure.

• Alternatively, the case may need more in-depth product knowledge and, hence, may be sent to the PSG for further investigation and resolution.

• The customer specialist engineer then documents the findings and hands over the case in a formal manner to the PSG. The case is in effect “tossed” over (for mal handoff) to the PSG.

• The case is picked up by a product specialist engineer who then investigates the case further. On completion, the engineer hands the case back with the findings documented to the customer specialist engineer.

• The customer specialist engineer then responds back to the customer with the final resolution.

The tossing of a case between customer and product specialist engineers involves formally documenting their findings, writing up specific questions on what is required, and plans for next steps before the case is handed to the next group. That is, a large amount of “overhead” is involved. Although tossing takes more time than an informal transfer of the case from one group to another, this level of formal handover allows companies to operationalize the resolution of a very large number of cases (several hundred cases per week) within the committed service levels to their customers. In addition, the high level of complexity of the cases warrants that the findings, logs, and detailed descriptions are all formally documented and communicated for quality and accuracy through this formal process, which, not coincidentally, made the design of a HRtech system of this study possible. Before we proposed this study, these rich data were never tapped. We contribute by leveraging the detailed data that archive every step of the customer service process and the outcome of the process toward building a datadriven collaborative process.

Figure 1. Traditional Customer Care Process  
![](/api/attachments/RXPGUTM2/fulltext/images/6d4ee3b78264ee24efa4e723ea60cbdfb8b2e310bf3fc5414dd6a9bb39966520.jpg)

The cases that are handled by the customer specialist engineer themselves (functional cases) are considered functional work within the CSG. Similarly, if a case is tossed to the product specialist team (cross-functional handover cases), that case then becomes functional work within the PSG. The traditional process has been in operation for more than 10 years and is taken for granted by top executives to be an effective process in managing the large number of cases. We next discuss the motivation for modifying the traditional process.

3.3. Motivation to Change the Traditional Process Over time, the firm’s field managers and engineers noticed that the knowledge required to solve some cases in the workflow did not clearly map into a single functional group. For example, there were cases that could mostly be solved by a CSG engineer but required some help from a PSG engineer. The management at the customer service unit conjectured that such cases might be better solved with a collaborative approach (henceforth, called cross-functional collaboration cases). If a cross-functional case were to be formally handed over to a product specialist, the customer specialist engineer may have to spend a large amount of time to formally document the case and the initial findings before the product specialist engineer could meaningfully contribute. In some situations, the effort spent in the formal handover could increase the overall hours logged on the cross-functional case (i.e., the cost to the firm could increase). The problem with the traditional process was not that the customer specialist engineer was seeking help; the customer specialist engineer sometimes did not have the necessary knowledge to solve the case. Rather, the inefficiency in the traditional process was caused by the manner in which help was sought. Offering the option of a collaborative approach showed promise in reducing the overall cost to the firm. But determining when and in which manner to seek help requires expertise that the company lacks. We offer a data-analytics approach by building machine learning algorithms to make such recommendations and then incorporating the algorithm’s recommendation into the new process.

However, process changes are complex and could have wide-ranging implications both positive and negative. This is especially so in high-tech firms in which the business environment is dynamic. In addition, collaboration across knowledge workers is complex as modern organizations often spread across a geographically diverse landscape, operating in different time zones. The cost of failure is high, so process changes are done incrementally with a lot of care. For example, a process change could fail to meet the service-level commitments or, in order to meet such commitments, the team could drive up costs to a prohibitive level. Because of these reasons, the management of the firm we studied was concerned that the process change could increase costs driven by the constraint to meet service-level commitments. Hence, they wanted material evidence of the benefits of collaboration and the underlying mechanisms at play before institutionalizing the process change.

## 3.4. New Customer Care Process

The traditional process was enhanced to include a collaboration option. Thus, in the new process, there were two ways for a customer specialist engineer to seek a product specialist’s help: (1) formal handover and (2) collaboration. Under the collaboration option, a CSG engineer could engage a product specialist using available collaboration tools (e.g., phone, video conference, etc.).

These steps illustrate the new process:

• Customer opens a new case.

• The case is received by a customer specialist engineer in CSG who starts working on it.

• If the engineer can solve the case at this point, the engineer provides the solution and responds back to the customer with a closure. We term these cases as “functional.”

• Alternatively, the case may require a crossfunctional solution approach, that is, involving both CSG and PSG engineers. For cross-functional cases, a customer specialist engineer could seek the help of a product specialist engineer in one of the following ways:

— The case is tossed or formally handed over to the product specialist for further investigation. After investigation, the case is tossed back to the customer specialist engineer. This is an asynchronous method of seeking help. We term these cases cross-functional handovers.

— The customer specialist engineer and a prod uct specialist engineer may collaborate (i.e., work synchronously) on the case using any of the supported collaboration tools and solve the case. This is a synchronous method of seeking help. We term these cases cross-functional collaboration.

• Finally, the customer specialist engineer responds to the customer with the final resolution.

This addition of the collaboration option in the new process was expected to extract the cases that would be more conducive for a cross-functional team to solve. The expected organizational structure resulting from this new process is shown in Figure 2. From this figure, we see that the case volume is divided between two functional groups, and a new ad hoc collaboration team is formed with members from both the CSG and PSG on an as-needed basis.

Figure 2. New Customer Care Process  
![](/api/attachments/RXPGUTM2/fulltext/images/c5508a2b59fcacbd0ac7f7cf47f1da263a4c6826aa219fe327d317a657a01ec6.jpg)

## 3.5. Data Description

Our data come from the firm’s customer care ticket database. Every case reported by a customer is logged into a ticket system, and the case details are updated with new information during the time that it is open. Once the ticket is closed to the customer’s satisfaction, all the data and logs associated with the case are archived. Table 1 presents the descriptions of major variables used in our analysis.

We further generalize the case characteristics following Hackman (1968), Wood (1986), and Campbell (1988) by aligning cases related to the new technology called Long Term Evolution (LTE) with high task difficulty, cases related to unknown ProblemType with high task uncertainty, and cases categorized as high severity with high task urgency.

## 3.6. Sequence of Experiments

In alignment with the sequential experimental design by Fisher (1952) and Blot and Meeter (1973), we conduct a series of three experiments to comprehensively study the value of collaboration in problem solving, the underlying source of this value, and the role of incentives in facilitating effective collaborative problem solving. In experiment one, we establish that incorporating collaboration as an option in problem -solving leads to a reduction in overall costs. In experiment two, we identify the task characteristics that create conducive conditions for collaborative problem solving and explain why. Finally, in experiment three, we investigate and correct incentives to promote collaborative problem solving.

## 4. Experiment One: Value of Collaboration

In this experiment, we first examine whether the use of collaborative problem solving reduces average problem-solving costs. Although it may be apparent that collaboration as a work form is beneficial, the underlying mechanisms are not obvious. Do all crossfunctional tasks benefit from a collaborative problemsolving approach? Or are the benefits realized from certain functional work items being performed more effectively in a collaborative manner? In this experiment, we explore these questions empirically.

Table 1. Description of Variables for Each Case

<table><tr><td>Variable name</td><td>Variable type</td><td>Description</td></tr><tr><td>CaseTAT</td><td>Outcome</td><td>Case turnaround time in days</td></tr><tr><td>EngineerHours</td><td>Outcome</td><td>Hours logged by engineers</td></tr><tr><td>CaseIdleTime</td><td>Outcome</td><td>Hours a case was not actively worked on</td></tr><tr><td>CSGHours</td><td>Outcome</td><td>Hours logged by CSG engineer (experiment two period)</td></tr><tr><td>PSGHours</td><td>Outcome</td><td>Hours logged by PSG engineer (experiment two period)</td></tr><tr><td>USEPSGResources</td><td>Outcome</td><td>Equal to one if PSG help was sought and zero otherwise</td></tr><tr><td>Collaboration</td><td>Independent</td><td>Collaboration employed or not</td></tr><tr><td>ProblemType</td><td>Independent</td><td>Type of problem, for example, known or unknown (task uncertainty)</td></tr><tr><td>Severity</td><td>Independent</td><td>Severity of the case, for example, high or low (task urgency)</td></tr><tr><td>Engineer</td><td>Independent</td><td>Engineer ID</td></tr><tr><td>Site</td><td>Independent</td><td>Originating site or location of the case</td></tr><tr><td>Domain</td><td>Independent</td><td>Problem domain, for example, LTE or non-LTE (task difficulty)</td></tr><tr><td>OpenDate</td><td>Independent</td><td>Date of case origination</td></tr><tr><td>CloseDate</td><td>Independent</td><td>Date of case completion</td></tr></table>

The control (T1) and treatment (T2) periods of the experiment lasted for 22 and 8 months, respectively, with a total of 10,556 cases. EngineerHours represents the total number of hours logged against a case before it is solved. Hence, this is a direct measure of the cost to solve this case. The duration of the case from the time it is opened to the time it is closed is termed Case-TAT (for case turnaround time) and is measured in the number of days. The difference between the CaseTAT (converted to hours) and EngineerHours gives a measure of case idle time, denoted CaseIdleTime. Note that, in some cases, the number of EngineerHours could be larger than the CaseTAT (in hours) because of multiple engineers working on a case in parallel. If so, CaseIdle-Time is set to zero. Table 2 shows the summary statistics of the main outcome variables of interest during the field experiment period.<sup>2</sup>

## 4.1. Measuring the Impact of the New Process

In the traditional process, when a new case arrives, the assigned customer specialist engineer first performs an initial investigation on the case. Based on this initial evaluation, the engineer makes decisions on whether to solve the case or send it to the PSG for further investigation. If the case is sent to the PSG, the engineer always tosses the case with a formal handover. However, in the new process, the engineer had an additional choice in the decision, namely, the case could be either tossed or solved collaboratively. We use this decision point to investigate the benefits of collaboration.

At first glance, it may appear obvious that the outcome with fewer choices must be worse (greater expected hours) than that in which more choices are available. We expect that a relaxation (adding the new collaboration option) of the problem should provide better results. However, the source of these improved results is not immediately clear. For example, is the source of the benefit because some cases are better solved using collaboration instead of a formal handover? Or are some cases that were solved earlier within the customer care unit now solved using collaboration? Or does the benefit stem from a combination of the two possibilities? We next describe the design of experiment one to study the effect of the new collaboration process on the expected hours needed to solve a case.

## 4.2. Experiment Design

The firm receives cases that originate from 730 different locations or sites. Out of these sites, 238 sites (about 33%) were randomly designated to use the new process (TreatedSet of sites), and the remaining 492 sites were designated to use the traditional process (ControlSet of sites). The duration of the experiment was divided into two periods, namely, a pretreatment control period (T1) and treatment period (T2). Problems from each site at a particular time are reported as cases to be resolved, and over time, there may be multiple cases originating from a site. Each case consists of character istics, such as task severity and complexity, that may affect the effectiveness of collaboration. Hence, a caselevel analysis is necessary to tease out the impact of task characteristics on collaboration in contrast to an aggregated site-level analysis.<sup>3</sup> The method of case assignment to customer specialist engineers did not change between the first and second periods. In the first period (T1), 5,729 cases were used for the control and 1,948 cases for the treatment. In the treatment period (T2), 2,473 cases were used for the control, and 406 cases were treated. The details of the experiment, including randomization check, manipulation check, and a pilot study, are provided in the online appendix.

We begin with performing a difference of means analysis for each of the main outcome variables, comparing the values before and after the treatment period for both the control and treated sites. The negative values of the second difference of the means as displayed in Table 3 provide model-free evidence of the benefits of collaboration. However, given that each site generates multiple cases over time, we further conducted econometric analysis to analyze the effect of collaboration at the case level, taking into account the specific characteristics of each case.

## 4.3. Econometric Model

The experiment allows us to examine the impact of the process change for cases originating from some randomly chosen sites (TreatedSet of sites) and continue to use the traditional process for cases from the ControlSet of sites. We use difference-in-differences (DiD) analysis to compare the expected outcome before and after the introduction of the new process for both the control and treated groups (Seamans and Zhu 2013, Goldfarb et al. 2022). The first difference determines if there is a change in the value of a test statistic (for example, engineer hours) before and after the process change in the TreatedSet and ControlSet of sites. The second difference compares the change in first difference between the two groups. The hypothesis tested is whether the second difference is significantly different from zero. If so, then we can reject the hypothesis that collaboration had no significant effect on the statistic.

Table 2. Summary Statistics of Outcome Variables

<table><tr><td>Outcome variable</td><td>Number of cases</td><td>Mean</td><td>Standard deviation</td><td>Minimum</td><td>Maximum</td></tr><tr><td>CaseTAT $^{+a}$ </td><td>10,556</td><td>17.01</td><td>26.71</td><td>0.001</td><td>613.97</td></tr><tr><td>EngineerHours</td><td>10,556</td><td>10.45</td><td>19.10</td><td>0.0</td><td>531.50</td></tr><tr><td>CaseIdleTime</td><td>10,556</td><td>398.03</td><td>633.70</td><td>0.0</td><td>14,677.13</td></tr><tr><td>CSGHours $^b$ </td><td>879</td><td>11.87</td><td>21.21</td><td>0.0</td><td>453.53</td></tr><tr><td>PSGHours $^b$ </td><td>879</td><td>16.89</td><td>636.13</td><td>0.18</td><td>873.43</td></tr></table>

<sup>a</sup>Measured in days.  
<sup>b</sup>Experiment two period, cross-functional cases in the new customer care process only.

Table 3. Mean DiD of Outcome Variables

<table><tr><td>Outcome variable</td><td>Control vs. treated</td><td>After treatment</td><td>Before treatment</td><td>First difference (standard error)</td><td>DiD (standard error)</td></tr><tr><td rowspan="2">CaseTAT</td><td>Control</td><td>15.77</td><td>16.50</td><td>-0.73 (0.65)</td><td>-0.61*** (0.02)</td></tr><tr><td>Treated</td><td>19.34</td><td>20.68</td><td>-1.34 (1.37)</td><td></td></tr><tr><td rowspan="2">EngineerHours</td><td>Control</td><td>9.59</td><td>9.60</td><td>-0.01 (0.43)</td><td>-0.16*** (0.02)</td></tr><tr><td>Treated</td><td>13.40</td><td>13.57</td><td>-0.17 (1.23)</td><td></td></tr><tr><td rowspan="2">CaseIdleTime</td><td>Control</td><td>369.0</td><td>386.5</td><td>-17.5 (15.47)</td><td>-13.5*** (0.48)</td></tr><tr><td>Treated</td><td>450.9</td><td>482.9</td><td>-31.0 (32.50)</td><td></td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

In order to find the effect of collaboration on response time and costs, we estimate a DiD model for various metrics measuring economic outcomes associated with each case:

$$
\begin{array}{c} \ln (\Upsilon_ {i j t}) = \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} \times E x p e r i m e n t _ {t} \\ + \mathbf {C o n t r o l s} _ {i} + \mu_ {j} + \tau_ {t} + \varepsilon_ {i j t}. \end{array}\tag{1}
$$

The log-transformed dependent variable $\Upsilon _ { i j t }$ in Equation (1) represents the various economic measures that the firm considers important for each case i in every time period t. Whereas each case i is unique, the site from which it originates and the engineer who works on it can repeat; hence, $\mu _ { j }$ indexes the engineer and site combination fixed-effects related to each case.

The binary variables in Equation (1), Treatment and Experiment indicate whether a case was treated with the new collaboration process and whether the case originated during the experiment period, respectively. The interaction variable (Treatment × Experiment ) captures the DiD measure, and the significance of its coefficient $\beta _ { 1 }$ indicates the effect of the collaboration process on the dependent variable.<sup>4</sup> We also include Controls to capture any case-specific characteristics (ProblemType, Severity, Domain). The variable $\tau _ { t }$ captures the time or seasonal effects of the cases.

## 4.4. Results

The results of our regression on the entire case population are summarized in Table 4. We find a statistically significant average drop of $2 5 . 7 \% ^ { 5 }$ in the case turnaround time after collaboration is introduced. Additionally, the average number of engineer hours logged against each case (a direct measure of the problem-solving cost incurred by the firm) decreases by 13.6% and the CaseIdleTime (directly related to customer service experience and waiting time) decreases by 31.8%.

These results suggest that a collaborative approach is important and provides an overall beneficial result. Although there is an overall benefit, it is important to understand the mechanisms at play that yield these benefits.

Recall that, in Section 3.3, we posit that the new collaboration process would be effective in extracting the cases that are conducive to collaboration, thereby reducing costs and case turnaround times. Our results in Table 4 support this conjecture. We next analyze the data in more detail in order to understand why the new process improves outcomes.

## 4.5. Isolating the Source of Collaboration Benefits

From Section 3.4 and Figure 2, it is clear that cases undergoing collaboration can only be of two kinds: (1) cases that were solved using a functional approach earlier but are now solved using collaboration and/or (2) cases that used formal handover earlier, but now use collaboration. However, whatever be the source(s) responsible for the creation of the collaboration pool, we expect that, because the new process provides another way to seek PSG help, the propensity to seek outside help must weakly increase (never decrease). Based on this expectation, we develop a two-step evidencegathering process to isolate the source of collaboration benefits.

Table 4. Average Treatment Effect of Customer Care Collaboration Process on All Cases

<table><tr><td></td><td>Case TAT</td><td>Engineer Hours</td><td>Case IdleTime</td></tr><tr><td>Effect of Collaboration ( $\beta_1$ ) (standard error)</td><td>-0.2977***(0.0751)</td><td>-0.1470***(0.0513)</td><td>-0.3834***(0.1374)</td></tr><tr><td> $R^2$ </td><td>0.69</td><td>0.66</td><td>0.62</td></tr><tr><td>Number of observations</td><td>10,556</td><td>10,556</td><td>10,556</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

• Our first step is to study its impact on the propensity to seek PSG help as shown in the model:

$$
\begin{array}{r l} \text { Logit } (U s e P S G R e s o u r c e s _ {i j t}) & = \beta_ {0} + \beta_ {1} T r e a t m e n t _ {i} \\ & \times E x p e r i m e n t _ {t} + \mathbf {C o n t r o l s} _ {i} \\ & + \mu_ {j} + \tau_ {t}. \end{array}\tag{2}
$$

The dependent variable UsePSGResources is binary that is true (one) if the case i at time t was worked on by a PSG member $( \mathrm { i . e . , }$ the case used a cross-functional approach) and false (zero) otherwise. The covariates of the equation are as before. The results of the logistic regression are shown in Table 5. These results suggest an increase in the propensity to seek PSG help after the introduction of the new collaboration process: the odds of engaging PSG increase more than 13 times. This signifies that customer specialist engineers seek more help when the barriers to engaging with other groups are reduced (as a result of introducing the collaboration option).

• Given that PSG help is sought more, we next examine the possible movement of functional and/or formal handover cases to the collaboration pool. We first compare the difference between functional cases in the control and treated groups. The results of this comparison show if there was a cost change in the functional cases because of the introduction of the new process. Second, we compare the difference between crossfunctional cases in the control and treated groups. The results of this second comparison show whether the addition of collaboration cases in the treatment period affected the cost. All results are based on the DiD regression specified in Equation (1).

Here, we find evidence for the significant shift of cases from the functional to collaboration pool but no significant movement is found from the formal handover to collaboration pool.

— Concerning the movement of functional cases, we find in Table 6 that the average engineer hours (also idle time) in the functional pool reduced by

Table 5. Results of Logistic Regression for Seeking PSG Help

<table><tr><td></td><td>UsePSGResources(propensity to seek PSG help)</td></tr><tr><td>Effect of collaboration ( $\beta_1$ )</td><td>2.6279***</td></tr><tr><td>(standard error)</td><td>(0.5645)</td></tr><tr><td>Odds ( $e^{\beta_1}$ )</td><td>13.46</td></tr><tr><td>Number of observations</td><td>10,556</td></tr><tr><td>Fixed effects</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

Table 6. Effect of Collaboration Process on Functional Cases Only

<table><tr><td></td><td>CaseTAT</td><td>EngineerHours</td><td>Case IdleTime</td></tr><tr><td>Effect of collaboration $(\beta_1)$ (standard error)</td><td>-0.3361***(0.0893)</td><td>-0.1423***(0.0497)</td><td>-0.4600***(0.1712)</td></tr><tr><td> $R^2$ </td><td>0.65</td><td>0.62</td><td>0.59</td></tr><tr><td>Number of observations</td><td>8,841</td><td>8,841</td><td>8,841</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

13.3% (and idle time by 37%) after the introduction of the new process. This implies that engineers choose to collaborate on cases that would otherwise result in higher engineer hours if solved within the CSG group. That is, heavy engineer hour cases get solved using collaboration rather than seeking to resolve these cases within the CSG group alone.

— There is no evidence (insignificant $\beta _ { 1 }$ in Table 6) to suggest that formal handover cases moved to the collaboration pool as a result of the new process. The results in Table 7 show that the average case turnaround time reduces by a statistically significant 48%, which is almost entirely contributed by a reduction of 48% in the case idle time. Thus, for formal handover cases, there is no statistically significant change in the engineer hours as a result of the new process.

The results in this section reveal an interesting impact of introducing collaboration teams: the benefits of the new process accrue from a shift of functional to collaborative work. However, there is no evidence to suggest that the benefit of the new process stems from the shift of formal handover to collaborative work. This effect— shifting functional work to collaborative work—is likely because the barriers to seek PSG help are reduced by the new process.

## 5. Experiment Two: Impact of Task Characteristics

In this experiment, we aim to answer the following research question: under what conditions is collaborative problem solving effective? Specifically, what are the task characteristics that make cases conducive to a col laborative problem-solving approach? Previous research suggests that difficult tasks benefit from collaboration (Graesser et al. 2018) and that task complexity and uncertainty may increase the use of collaboration (Daley 1978). However, these findings are not verified in an industry setting with detailed case-level data. In addition, the interaction between these characteristics and their roles in facilitating collaboration work is not clear. Therefore, this experiment seeks to explore these generic task characteristics in the context of knowledge work and examine their impact on collaboration.

Table 7. Effect of Collaboration Process on Cross-Functional Cases Only

<table><tr><td></td><td>CaseTAT</td><td>EngineerHours</td><td>CaseIdleTime</td></tr><tr><td>Effect of collaboration $(\beta_1)$ </td><td>-0.6534**</td><td>-0.4116</td><td>-0.6562*</td></tr><tr><td>(standard error)</td><td>(0.2793)</td><td>(0.3220)</td><td>(0.3453)</td></tr><tr><td> $R^2$ </td><td>0.95</td><td>0.93</td><td>0.94</td></tr><tr><td>Number of observations</td><td>1,715</td><td>1,715</td><td>1,715</td></tr><tr><td>Fixed effects</td><td>Yes</td><td>Yes</td><td>Yes</td></tr><tr><td>Control variables</td><td>Yes</td><td>Yes</td><td>Yes</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

The primary outcome of interest is the number of engineer hours needed to solve a case, which is the main cost to the company.<sup>6</sup> The motivation for experiment two arises from the finding in experiment one that the benefits of the new process could not be attributed to a shift of work from formal handover to collaboration. Rather, the benefits of the new process stem from a shift of functional to collaborative work. This prompts us to further examine the task characteristics that are conducive to collaboration from the cost perspective.

In this experiment, we analyzed a set of 879 cases in which CSG engineers exercised their option to engage the product specialist team in either a collaborative manner or using formal handover. For these 879 cases, we also collected the number of hours logged by the CSG and PSG groups separately to form additional outcome variables (EngineerHours � CSGHours + PSG Hours).

## 5.1. Impact of Collaboration

The impact of the new process depends on the quality of the CSG engineer’s decision concerning the mode of engaging the PSG group. The outcome (engineer hours) is contingent on the CSG engineer’s decision (collaborate versus formal handover). However, because each engineer handles multiple cases, the cases handled by a specific engineer could possibly have correlated outcomes, indicating within-group observation dependence. This dependence could violate the need for independence across observations in the data, making an ordinary least squares (OLS) model unsuitable for measuring the impact of collaboration on the different outcomes.<sup>7</sup>

To study the presence of the observation dependence, we compute the within-group (engineer) correlation coefficient between case outcomes (intracorrelation coefficient (ICC)). The ICC is the proportion of the total variance of the outcome variable that is contributed by the variance within a group (engineer). Intuitively, ICC is a measure of heterogeneity across engineers. The presence of this heterogeneity implies the presence of within group observation (case) dependence (Wang et al. 2011).

We diagnose this problem by studying the mean outcome for an engineer using an empty (i.e., with no covariates) model (3). In this model, $\Upsilon _ { i j }$ is the outcome for case i solved by engineer $j , \beta _ { 0 j }$ is the mean outcome for engineer $j , \ \varepsilon _ { i j }$ is the error term, $\gamma _ { 0 0 }$ is the overall mean outcome, and $u _ { 0 j }$ is the deviation from the overall mean of the mean outcome for engineer j:

$$
\begin{array}{l} \Upsilon_ {i j} = \beta_ {0 j} + \varepsilon_ {i j} \\ \beta_ {0 j} = \gamma_ {0 0} + u _ {0 j}. \end{array}\tag{3}
$$

Based on the results in Table 8, we see that, for all the outcome variables, the engineer heterogeneity is large (0.63, 0.64, 0.59) and statistically significant. Hence, an OLS model with covariates such as engineer and case characteristics is not adequate to assess the impact of collaboration on the outcome variables. Instead, we employ a hierarchical linear model (HLM) in order to account for the engineer level heterogeneity in the data (Setia et al. 2012):

$$
\begin{array}{r l} & {l n (\Upsilon_ {i j}) = \beta_ {0 j} + \beta_ {1} C o l l a b o r a t i o n _ {i j} + \beta_ {2 j} S e v e r i t y _ {i j}} \\ & {\qquad + \beta_ {3} P r o b l e m T y p e _ {i j} + \beta_ {4} S i t e _ {i j}} \\ & {\qquad + \beta_ {5} D o m a i n _ {i j} + \varepsilon_ {i j}} \\ & {\beta_ {0 j} = \gamma_ {0 0} + u _ {0 j}} \\ & {\beta_ {2 j} = \gamma_ {2 0} + u _ {2 j}.} \end{array}\tag{4}
$$

Model (4) uses the characteristics of an arriving case: Severity, ProblemType, Site, and Domain. The Collaboration variable represents the decision of the CSG engineer (either collaborate or formal handover).

All these variables were first introduced in a model specification to use random coefficients, and the variances of variables were examined for statistical significance. Only the error term for Severity had statistically significant variance, indicating its role in explaining the betweenengineer variability. Hence, Severity was retained with a random coefficient. The coefficient $\beta _ { 1 }$ represents the effect of Collaboration on an outcome variable as dependent on the engineer working on the case. Thus, the mean engineer effect and Severity are associated with random coefficients $( \beta _ { 0 j }$ and $\beta _ { 2 j } ) _ { \cdot }$ , whereas the remaining three covariates are associated with scalar coefficients $( \beta _ { 3 } , \beta _ { 4 }$ , and $\beta _ { 5 } )$

Table 8. Heterogeneity Between Engineers: Intraengineer Correlation Coefficient

<table><tr><td></td><td>EngineerHours</td><td>CSGHours</td><td>PSGHours</td></tr><tr><td>Variance between engineers</td><td>4,257.71***(845.17)</td><td>587.03***(120.24)</td><td>1,440.54***(297.81)</td></tr><tr><td>Variance within an engineer</td><td>2,509.07***(137.85)</td><td>333.08***(18.40)</td><td>1,010.93(55.67)</td></tr><tr><td>Heterogeneity between engineers (ICC)</td><td>0.63</td><td>0.64</td><td>0.59</td></tr></table>

Note. Standard errors in parenthesis.  
\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

We consider three outcome variables, that is, EngineerHours, CSGHours, and PSGHours. The impact of collaboration on these outcomes is reported in Table 9. We find that, on average, the decision to collaborate does not significantly impact EngineerHours.<sup>8</sup> To find whether collaboration matters for certain kinds of cases, we cluster the 879 cases into homogeneous groups of similar cases and further analyze the impact of collaboration decisions within each cluster.<sup>9</sup>

Whereas our findings concerning the impact of collaboration on engineer hours are mixed (i.e., in some clusters, the decision matters, whereas in others there is no impact), when we consider the CSGHours and PSGHours separately, there is a significant impact of the collaboration decision. Relative to the CSG and PSG hours incurred in formal handover, collaboration increases PSG hours and reduces CSG hours. Taken together, these findings, namely, that collaboration impacts engineer hours for some kinds of cases and always reduces (increases) CSG (PSG) hours for all cases, we develop a policy to guide CSG engineer decisions so as to improve certain outcomes for the firm.

## 5.2. Exploratory Cluster Analysis

In the previous sections, we find that, on average, the collaboration decision does not impact EngineerHours variable (cost of a case) when all 879 cases are considered altogether. However, when we cluster the data set into more homogeneous groups consisting of similar cases, we observe that the collaboration decision indeed matters in certain clusters. We cluster the 879 cases into six clusters using the arriving case characteristics based on the K-means algorithm.<sup>10</sup> The elbow method was used to determine the slope of the sum of squared errors, which produced six clusters (see the online appendix).

Table 9. Average Effect of Collaboration on Hours Logged by Engineers

<table><tr><td></td><td>TotalHours</td><td>CSGHours</td><td>PSGHours</td></tr><tr><td>Effect of collaboration ( $\beta_1$ )</td><td>0.0722</td><td>-0.8547***</td><td>0.6668***</td></tr><tr><td>Severity ( $\beta_{2j}$ )</td><td>0.1901***</td><td>0.1828**</td><td>0.0766</td></tr><tr><td>Problem type ( $\beta_3$ )</td><td>-0.1156</td><td>-0.1262</td><td>0.2218***</td></tr><tr><td>Domain ( $\beta_5$ )</td><td>-0.2462</td><td>-0.3057</td><td>0.0097</td></tr><tr><td>Number of observations</td><td>879</td><td>879</td><td>879</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

Next, in each cluster, we employ the HLM specification in (4) to study whether the collaboration decision matters to the outcome in that cluster. Table 10 reports the impact of the collaboration decisions in each of the six clusters. From the perspective of total cost, we observe that collaboration decisions are Relevant in clusters 4 (161 cases) and 5 (152 cases). In cluster 4, the choice to collaborate results in a reduction in Engineer-Hours (the coefficient $\beta _ { 1 }$ is negative). The exact opposite is seen in cluster 5. The collaboration decision is nonrelevant in the other clusters. However, in one of the nonrelevant clusters (cluster 2), whereas the impact of the collaboration decision is insignificant for total cost, the balance of the cost between CSG and PSG engineers is impacted.

The two relevant clusters are of two kinds: collaboration positive and negative. We use the independent variables of each case given in Table 1 to understand the characteristics of the clusters. In the collaboration positive cluster (cluster 4), collaboration reduces cost over formal handover. This cluster has 156 out of 161 cases with high severity (97%). A high-severity case is one in which the engineer has very little time to complete the case and yet meet the contractual service-level commitments. All 100% of the cases in this cluster are from the LTE domain, which is a new technology with many unknown issues and bugs. In this cluster, collaboration reduces the overall cost (37%). This reduction is due to to a significant reduction in CSG hours (16.9%). However, the change in PSG hours is not statistically significant.

All 152 cases in the collaboration negative cluster (cluster 5) are of low severity, implying that there is sufficient time to complete the case and meet the contrac tual service-level commitments. In addition, all 100% of the cases in this cluster are from the LTE domain. Another interesting characteristic of this cluster is that all the cases in this cluster are of known problem type, implying that the customer has identified a specific problem and wants a resolution. In this cluster, the CSG hours reduce significantly (59%) but the PSG hours increase much more (232%). As a whole, collaboration increases the overall cost of cases by 55%.

Within the nonrelevant clusters, cluster 2 is of interest. Here, the collaboration decision shifts the load from CSG to PSG engineers. However, the total cost is not significantly affected. This cluster consists exclusively of new technology, low-severity cases. We find that all the cases in this cluster are of unknown problem type, implying that neither the customer nor the engineers know the cause of the problem. We do not see an overall benefit of collaboration on total cost, that is, CSG hours decrease and PSG hours increase (both are statistically significant).

Table 10. Average Effect of Collaboration on Various Outcomes for Each Cluster of Cases

<table><tr><td></td><td>Cluster 0</td><td>Cluster 1</td><td>Cluster 2</td><td>Cluster 3</td><td>Cluster 4</td><td>Cluster 5</td></tr><tr><td>Total hours</td><td>-0.2725</td><td>NA</td><td>0.1633</td><td>0.8882</td><td>-0.4821***</td><td>0.4382***</td></tr><tr><td>CSG hours</td><td>-1.0936</td><td>NA</td><td>-0.7779***</td><td>NA</td><td>-0.1846***</td><td>-0.8966***</td></tr><tr><td>PSG hours</td><td>0.2055</td><td>NA</td><td>0.7739***</td><td>1.4418</td><td>0.1124</td><td>1.2005***</td></tr><tr><td>Observations</td><td>175</td><td>61</td><td>310</td><td>20</td><td>161</td><td>152</td></tr><tr><td>Collaboration ratio</td><td>0.44</td><td>0.0</td><td>0.44</td><td>0.3</td><td>0.19</td><td>0.08</td></tr></table>

Note. NA, not applicable.  
\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

These results are described in Table 10. We next perform a robustness test to determine if a subset of the cases with the characteristics of clusters 4, 5, and 2 yield consistent results. To this end, we partition the data set using the tree structure shown in Figure 3. The results in these partitions exactly match our expectations and are shown in Table 11. Clusters 4 and 5 cases result in a 24.7% decrease and 64.9% increase in total cost, respectively.

## 5.3. Validation Study

We conducted a study to validate the categorization of the cases in Figure 3. The study was conducted for three months using 184 cases that required help from the PSG team.<sup>11</sup> We focused on intervening on the two collaboration relevant clusters (clusters 4 and 5) only. There were 71 and 51 of clusters 4 and 5 cases, respectively. Figures 4 and 5 show the subsets of data for which we intervened (I) on the collaboration or formal handover decision and the results of the t-test.

In Figure 4, we depict the strategy used to validate the results of the analysis in Table 11. All incoming cases in this figure are from the LTE domain and of high severity. In all these cases, the engineer indicated that PSG help was needed. Out of the 71 cases, we intervene in about 50% of cases (35), implying that the engineer was asked to use a collaborative approach to seek help. Thus, in the remaining cases (36), the engineer was allowed to choose the mode of engaging the PSG group: in 20 cases, a formal handover approach was used, whereas in 16 cases, the engi neer engaged the PSG group using a collaborative approach. The difference in mean EngineerHours bet ween the intervened (I) cases (in which the engineer was asked to use a collaborative approach) versus ones in which the engineer chose to use FH at the engineer’s own discretion is significant and negative.<sup>12</sup> On the other hand, there is no significant difference in mean engineer hours when the engineer was asked to use a collaborative approach (I) versus when the engineer chose to use a collaborative approach (NI). For completeness, we also report the difference in mean between all cases in which a collaborative approach was used by either choice (C) or intervention versus cases in which FH was used. As expected, this difference is significant and negative, implying that collaboration reduces engineer hours for cases that display characteristics similar to cluster 4.

Figure 3. Categorization of Data According to Cluster Characteristics  
![](/api/attachments/RXPGUTM2/fulltext/images/6b4d9fd91eb7ef2025554320af42a2c3e878d0cf97e7a9dc150c29f98fc0b9c0.jpg)

In Figure 5, we again depict the value of intervention when the incoming case has characteristics similar to cluster 5 (LTE and low severity). Here, engineers are asked to use formal handover for about 50% cases (25 out of 51). Once again, we find that the cases in the intervention subset (I) have significantly lower mean engineer hours than those of the cases in which the engineer chose to collaborate (C).<sup>13</sup> Other comparisons of mean engineer hours are in line with our expectation that for cases of this type: it is better to use formal handover to engage the PSG group.

For completeness, we also report the difference in cost between the intervening decision and human decisions for both cluster 4 and 5 cases, for example, I � (NI + FH). In both cases, we find that the recommendation yields lower costs.

Table 11. Average Effect of Collaboration on Various Outcomes for Subsets of Cases

<table><tr><td></td><td>LTE, high, cluster 4 type</td><td>LTE, low, known, cluster 5 type</td><td>LTE, low, unknown, cluster 2 type</td><td>Non-LTE, other types</td></tr><tr><td>Total hours</td><td>-0.2831*</td><td>0.4999***</td><td>0.1107</td><td>-0.2561</td></tr><tr><td>CSG hours</td><td>-0.9193***</td><td>-0.8112***</td><td>-0.8070***</td><td>-1.4879***</td></tr><tr><td>PSG hours</td><td>0.2304</td><td>1.2333***</td><td>0.7090***</td><td>0.2288</td></tr><tr><td>Observations</td><td>215</td><td>215</td><td>282</td><td>167</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

Figure 4. Comparison of Cluster 4–Type Cases (Collaboration Helps)  
![](/api/attachments/RXPGUTM2/fulltext/images/bd929ba0325f276d25b8cfb62f50d83c4bce9fb14860f8565291625fe3daed4f.jpg)

From this study and mapping task characteristics to those defined by Kay et al. (2018), we confirm that difficult and urgent tasks, that is, tasks from a new technology and that need to be solved in a time crunch, benefit from a collaborative solution, for example, LTE cases with high severity. However, difficult but nonurgent tasks are better solved in a noncollaborative manner if they have low uncertainty, for example, LTE cases with low severity and a known problem type. Interestingly, difficult, nonurgent, and uncertain tasks (e.g., LTE cases with low severity and an unknown problem type) are unaffected by a collaborative problem-solving approach but result in a shift of cost from one functional group to another. These insights on task characteristics are very important when designing efficient cross-functional teams and processes.

## 6. Experiment Three: Incentive Misalignment

Our goal in this experiment was to study the role of incentives in successful collaboration. Prior work examines the role of individual incentives in people’s decision to collaborate (Bikard et al. 2015, Vakili et al. 2021). However, the interplay of individual incentives and firm goals in an industrial setting could impact the benefits of collabora tion in different ways. More specifically, we determine whether engineers comply with machine recommendations and explore the reasons underlying why engineers may deviate from these recommendations. We next use the findings from this experiment to improve compliance. The extent to which engineers complied with machine recommendations was important because introducing machine recommendations in this environment was new, and accordingly, there could be reluctance on the part of engineers to adopt them. Hence, our focus was to study the level of adoption of machine recommendations by engineers and the factors that influenced this adoption.

The findings in experiment two were used to develop a recommendation system called HRTech Analytics<sup>14</sup> by the firm. The machine recommendations (formal hand over and collaboration) were communicated to engineers via a recommendation system, and the actual choices that the engineers made after receiving these recommendations were observed. Because the collaboration method of problem solving was new to the organization, it was decided to leave all other processes unchanged. A dashboard (presented in the online appendix) was used to display the weekly ratio of collaborated versus formally handed over cases.

Figure 5. Comparison of Cluster 5–Type Cases (Collaboration Hurts)  
![](/api/attachments/RXPGUTM2/fulltext/images/b77500dc70227ed694bc7ec57ea3b95d93050adf26a19d408e6c859e59cbab4d.jpg)

Figure 6. (Color online) Previous Week Solved Case Ratio and Current Week Compliance Ratio  
(a)  
![](/api/attachments/RXPGUTM2/fulltext/images/f8ae81fc7d4d269acdc47dec6ff840721d1cad7419816f1c83afb37860f7d86d.jpg)

(b)  
![](/api/attachments/RXPGUTM2/fulltext/images/464879fb5e7beb18285a7e0f39bf1d645582559e1f90a0fb4e5ead5e3dabb6f6.jpg)

## 6.1. Compliance Study

Immediately after the deployment of the HRTech Analytics system, data were collected for a period of 29 weeks to observe how often engineers followed the recommendation given by the system.<sup>15</sup> During this period, we collected the following data for each week: (a) cases recommended for collaboration, (b) cases recommended for formal handover, (c) cases solved using collaboration, and (d) cases solved using formal handover. At the end of the 29-week data-collection period, we analyzed the compliance of engineers in the CSG team with machine recommendations. We separately collected data on compliance corresponding to collaboration versus formal handover recommendations. The compliance ratios under each category (number of recommendations followed divided by the total number recommended) are plotted in Figure 6.

We note from Figure 6(a) that, for formal handover cases, compliance with recommendations is fairly constant at a mean of 0.79 and a standard deviation of 0.006, implying that engineers deviate little from such recommendations made by the system. However, from Figure 6(b), we find that collaboration compliance has a lower mean of 0.7 and a higher variance of 0.099. This shows that engineers do not consistently follow collaboration recommendations.

We next investigated why compliance to machine recommendations was lower for collaboration cases. Interviews with the department managers indicated that low collaboration ratios were a matter of pride for the CSG team because they viewed collaboration with the PSG team as a form of dependence on an entity that was external to the CSG department. Interestingly, formal handover cases were not viewed the same way. Here, dependence on the PSG team was not seen as an issue because, unlike collaboration cases, these cases always remained under the exclusive control of the CSG engineer. Also, the CSG engineer was viewed to play a primary role here, and this role was clearly documented in the handover instructions to the PSG engineer. Thus, whereas there were disincentives associated with excessive collaboration, the same was not true for formal handover.

As discussed earlier, machine recommendations were designed to reduce total engineer hours (cost) associated with the CSG and PSG teams. That is, machine recommendations were aligned with the firm’s goals of reducing total cost. However, total cost (total engineer hours) to solve a case was not a metric used to evaluate a CSG engineer nor was this metric displayed on the dashboard. We, therefore, conjecture that the lower compliance with collaboration recommendations was a result of a misalignment between the goal to reduce total cost and the CSG team’s incentive to limit its dependence on the PSG team.

If our conjecture holds, we should expect to see a reduction in compliance with collaboration recommendations in response to a perceived overuse of collaboration in the recent past. In order to investigate the impact of this effect, we plotted the previous week’s actual ratio of col laborated cases (to formally handed over cases) with the current week’s collaboration compliance ratio. Figure 7(b) shows that collaboration compliance stays high with very low variance as long as the previous week’s collaboration case ratio is below 0.5. However, if the previous week’s collaboration case ratio increases beyond 0.5, the current week’s ratio drops. We do not see such an effect with the formal handover compliance as shown in Figure 7(a) as expected. Thus, we see model-free evidence that engineers comply less with collaboration recommendations in the current week if they believe that they excessively collaborated in the previous week.

## 6.2. Root Cause Analysis

From Figure 7(b), we see a break point in the compli ance; that is, to the left of this break point, engineer collaboration compliance is high and stable, and to the right, the compliance declines. Hence, similar to Imbens and Lemieux (2008), we use a local regression around the break point to study the effect of personal incentives on collaboration decisions.

Figure 7. Collaboration Case Compliance Ratio Analysis  
(a)  
![](/api/attachments/RXPGUTM2/fulltext/images/09af14d6690e35f12cba9d569abb3f65a61839581a8b520660261ce5eda1049d.jpg)

In order to identify this break point formally, following Card et al. (2008) and Ozier (2018), we regress the weekly collaboration compliance ratio on the previous week’s collaboration solved cases ratio and an indicator for a hypothetical discontinuity at different points. The discontinuity points chosen are from 0.2 to 0.8 in 0.05 increments, resulting in a total of 13 regressions. We then pick the discontinuity point that has the highest $R ^ { 2 }$ value as being the best one. In our case, from Figure 8(a), it is clear that the discontinuity in collaboration compliance occurs when the previous week’s collaboration solved cases ratio exceeds 0.6. This is our cutoff point.

We now formally select a boundary or bandwidth around the cutoff point of 0.6. If the bandwidth around the cutoff point is too wide, the estimates will be imprecise. Conversely, if the bandwidth is too narrow, the results might be biased. In order to find a bandwidth that involves an optimal balance between precision and bias we use a “leave one out” cross-validation (CV) algorithm as specified in Ludwig and Miller (2007), Imbens and Lemieux (2008), and Jacob et al. (2012). In this leave-one-out CV algorithm, we select different bandwidth values, for example, $h _ { 1 } , h _ { 2 } , \ldots e t c .$ and calculate the mean square error for each point within each bandwidth, that is, $h _ { i } .$ The bandwidth with the lowest mean square error is chosen as the final bandwidth to use. Based on this procedure, we find that the bandwidth value of 0.35 is the optimal window for the ratio of collaboration cases solved in the previous week (Figure 8(b)). We use this value to proceed with local regression in the next step.

Figure 8. Break Point and Bandwidth Selection  
(a)  
![](/api/attachments/RXPGUTM2/fulltext/images/884dfc9e24065a19630f4601af23b7e6fb249c7191593be634a879c9b69e603c.jpg)

(b)  
![](/api/attachments/RXPGUTM2/fulltext/images/1892aa3c298019f06d6c7413521b1c5caa9f77d1413d0ae71578b47eb248dd21.jpg)

We select the data points that fall within the bandwidth of 0.35 above and below the break point. Using these data points, we conduct a local linear regression to estimate the local average treatment effect as specified in Imbens and Angrist (1994). Because the decisions to collaborate by the engineers can also be influenced by other environmental factors, such as the ratios of high severity cases, LTE cases, and known versus unknown problem types, we use these variables as controls in the regression. We ran the following Regression (5) to estimate the effect that the previous week’s proportion of solved collaboration cases has on the current week’s compliance of machine recommendations:

(b)  
![](/api/attachments/RXPGUTM2/fulltext/images/ec3fb0f7ab1a21a63f17ef893904e467a0ea68ea6bc3c0d56b308c0a75f72624.jpg)

Table 12. Description of Variables used in Collaboration Compliance Analysis

<table><tr><td>Variable name</td><td>Description</td></tr><tr><td> $Y_t$ </td><td>Percentage of machine recommendation compliance in week t.</td></tr><tr><td> $T_{t-1}$ </td><td>Indicator whether collaboration versus formal handover solved cases is greater than 0.5 in week t - 1.</td></tr><tr><td> $C_{t-1}$ </td><td>Ratio of collaboration versus formal handover solved cases in week t - 1.</td></tr><tr><td> $X1_t$ </td><td>Ratio of high- versus low-severity cases in week t.</td></tr><tr><td> $X2_t$ </td><td>Ratio of LTE cases in week t.</td></tr><tr><td> $X3_t$ </td><td>Ratio of known versus unknown problem cases in week t.</td></tr><tr><td>t</td><td>Week number.</td></tr></table>

$$
\begin{array}{c} \mathrm{Y} _ {t} = \beta_ {0} + \beta_ {1} \mathrm{T} _ {t - 1} + \beta_ {2} \mathrm{C} _ {t - 1} + \beta_ {3} \mathrm{T} _ {t - 1} \times \mathrm{C} _ {t - 1} \\ + \beta_ {4} \mathrm{X} 1 _ {t} + \beta_ {5} \mathrm{X} 2 _ {t} + \beta_ {6} \mathrm{X} 3 _ {t} + \varepsilon_ {t}. \end{array}\tag{5}
$$

Table 12 gives the descriptions of the variables used.

The results of the regression in Equation (5) are presented in Table 13. The coefficient of interest $\left( \beta _ { 1 } \right)$ is the effect of the variable T, which represents the influence of the previous week’s collaboration ratio on engineers’ deviation from the machine recommendations to collaborate.

As discussed earlier, interviews with the team yielded the hypothesis that, when the previous week’s share of collaborated cases is higher than the share of formally handed over cases (data are displayed in a weekly dashboard), the engineers self-correct by collaborating less in the current week. The value of $\beta _ { 1 }$ is negative and statistically significant, lending support to this hypothesis. Also, the magnitude of self-correction reduces the collaboration compliance ratio by 0.371.

## 6.3. Incentive Correction

Having established local incentives can adversely (from the firm’s perspective) impact an engineer’s decision to collaborate, so we explore how local (department level)

and global (firm level) incentives can be aligned. Recall that during the 29 weeks of data collection using the HRTech Analytics recommendation system, management added a dashboard to showcase the ratio of collaboration versus formal handover cases at the end of every week. This display likely reinforced a CSG engineer’s belief that excessive collaboration with the PSG team was undesirable. To address this incentive misalignment, we proposed and implemented a change to the engineer incentive to directly evaluate engineers on the basis of the average total number of hours spent (CSG + PSG) per case. In addition, the weekly collaboration ratio dashboard indicator was removed.

After these steps were completed, we collected data for a further period of 12 weeks. We first plotted the weekly collaboration compliance and then plotted the ratio of collaboration cases solved in the previous week against the collaboration compliance ratio (from the machine recommendation) of the current week. The results are shown in Figure 9(a) and (b). The mean level of compliance is 0.786 with a standard deviation of 0.01, indicating that now collaboration compliance is fairly steady and unaffected by the previous week’s solved collaboration ratio.

To further validate the results in Figure 9, we regressed the current week’s collaboration compliance against last week’s solved collaboration case ratio along with the con trol variables given in Table 12 according to the following equation:

$$
\Upsilon_ {t} = \beta_ {0} + \beta_ {1} \mathrm{T} _ {t - 1} + \beta_ {2} \mathrm{X} 1 _ {t} + \beta_ {3} \mathrm{X} 2 _ {t} + \beta_ {4} \mathrm{X} 3 _ {t} + \varepsilon_ {t}.\tag{6}
$$

The results of Equation (6) are reported in Table 14. We note that the value of $\beta _ { 1 }$ is statistically insignificant, indi cating that the previous week’s collaboration case ratio no longer affects the current week’s collaboration compliance. This validates our hypothesis that the implemented incentive realignments addressed the problem of the low collaboration compliance by the engineers.

## 7. Discussion

This paper is the first attempt to investigate experimentally the role of task characteristics and incentive alignment on collaborative problem solving. Our large-scale field experiments in a leading ICT firm enabled us to observe the most granular task-level characteristics and engineer-level behaviors that influence the success (failure) of collaboration, which are critical for the firm to determine the proper intervention as necessary. We further demonstrate the effectiveness of the information technology (IT) artifact we implemented, the HRTech Analytics System, in nudging users to follow the system recommendation on when to collaborate. As such, this study enriches the literature in several dimensions. First, it sharpens our understanding on how task characteristics can influence collaboration outcomes. Our use of the HLM and clustering analysis shows that subtle heterogeneity can arise from both the engineer and task characteristics, such as task complexity, uncertainty, and urgency, extending prior work (Hackman 1968, Daley 1978). Second, our identified source of recommendation noncompliance and incentive misalignment enriches the small but growing literature on the importance of designing the right incentive to foster collaboration (Kay et al. 2018, Vakili et al. 2021). Third, our HRTech Analytics System further adds a positive use case to the emergent literature on human–machine collaboration (Fu¨ gener et al. 2022, 2021), in which we show how to design the right recommendation system to improve collaboration effectiveness.

Table 13. Effect of Previous Week’s Solved Collaboration Ratio on Current Week’s Collaboration Compliance

<table><tr><td> $\beta_1$ (standard error)</td><td> $\beta_2$ (standard error)</td><td> $\beta_3$ (standard error)</td><td> $\beta_4$ (standard error)</td><td> $\beta_5$ (standard error)</td><td> $\beta_6$ (standard error)</td></tr><tr><td>-0.3708***(0.0107)</td><td>-0.0005(0.0067)</td><td>-0.4824***(0.0215)</td><td>-0.0071(0.0337)</td><td>-0.0054(0.0289)</td><td>-0.0013(0.0292)</td></tr></table>

\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

Figure 9. (Color online) Collaboration Case Compliance Ratio Analysis After Incentive Correction (a) (b)  
![](/api/attachments/RXPGUTM2/fulltext/images/1a592a96bbff7f1c5181f88bdc70e9a48ba106eb1f0a43bef5aa076e13a0ed11.jpg)

Our findings also have wide managerial implications in an organizational setting. First, we demonstrate the importance of assigning the right task to collaborative problem solving. Our identification of task characteristics conducive to a collaborative problem-solving approach is vital in industries in which knowledge tasks can be differentiated and defined. We find that new technology cases that are on an urgent time schedule from the customers (cluster 4–type cases) are most suited to be solved collaboratively. However, if a new technology case is on a lowe priority schedule with a known problem type that needs little investigation (cluster 5–type cases), then collaboration, in fact, hurts. Most interestingly, new technology cases on a lower priority schedule with an unknown problem type that require an ample amount of investigative work shift the effort from the CSG to the PSG team when solved collaboratively (cluster 2–type cases). The identification of these task characteristics enables managers to implement machine recommendations that can be used to guide engineer decisions as necessary. Second, our findings bring up an interesting managerial question: when should an engineer be urged to follow a recommendation that differs from the engineer’s own choice? The results of our study show that, in some cases, total engineer hours can be reduced by intervening to ask the CSG engineer to use a particular mode of seeking PSG help (collaboration versus formal handover). This constitutes a first level of intervention. A second level of intervention can be considered for situations that do not result in any change in overall EngineerHours, but there is an impact on the relative workload of the two engineer groups (CSG and PSG). Because the CSG and PSG teams are managed by different departments, the impact of increasing PSG hours may not be visible to a CSG engineer. For example, in the PSG team, some members could be moved tempo rarily to training or some other special assignments. This temporary deficit in the PSG team’s capacity can be ful filled by guiding the CSG engineers to choose a compensating collaboration decision.

Table 14. Effect of Previous Week’s Solved Collaboration Ratio on Current Week’s Collaboration Compliance After Incentive Correction

<table><tr><td> $\beta_1$ (standard error)</td><td> $\beta_2$ (standard error)</td><td> $\beta_3$ (standard error)</td><td> $\beta_4$ (standard error)</td></tr><tr><td>-0.0142(0.0158)</td><td>-0.1211(0.0838)</td><td>0.0029(0.0682)</td><td>-0.0433(0.0683)</td></tr></table>

![](/api/attachments/RXPGUTM2/fulltext/images/387fdd1aca9c1d9b6b325b990970998e20c50340f97abf63fad11cc399e8ab96.jpg)  
\*Significant at 0.1; \*\*significant at 0.05; \*\*\*significant at 0.01.

More generally our study emphasizes the role recommendation systems can play in assisting human tasks. Of particular interest is to develop a strategy to intervene only when necessary, that is, allow humans the freedom to choose even if this choice deviates from the machine recommendation. To this end, we identify situations of at least three kinds that can be generalized to domains beyond the study of collaboration between silos of a large organization. First, there are situations in which humans may know more about something than what the machine knows. An example of this in our study is the decision of whether to seek help. It may be best to leave this decision to the CSG engineer. This is because only the CSG engineer assigned to the problem knows what the engineer knows about the problem and whether help is needed. Thus, it may not be reasonable to intervene here. Next, if help is needed, the CSG engineer must decide how PSG help should be sought. Here, the machine can play a role. This situation is one in which human and machine knowledge overlap. Here, intervention (altering the human’s choice or urging the human to follow the machine’s recommendation) should be considered only if it makes a real difference to the outcome. Examples of these situations in our study are the collaboration choice an engineer makes in relevant and nonrelevant clusters. Intervention makes more sense in relevant clusters in which engineer hours can be reduced. Finally, there are situations in which the machine knows something that the human does not. An example of this in our context is when a CSG engineer makes a collaboration decision in a nonrelevant cluster. Here, whereas engineer hours are not impacted, the collaboration decision could impact CSG and/or PSG hours. The current free capacity of the PSG team (and to a lesser extent, the CSG team) may not be visible to a specific CSG engineer. Here, intervention could be actively pursued to balance the workloads of the two teams.

Our third important implication to practice involves the alignment of incentives to the firm’s goals for collaboration. We find evidence that, when engineers incentives are misaligned with the firm’s goals, engineers, in fact, do not collaborate when they should. This shows that the introduction of any collaborative work form needs to be considered hand in hand with a thorough evaluation of all existing incentives that may impede employees from collaborating. And, in some cases, incentive alignment may also involve changes to any individual culture that the firm may have established in the past.

Finally, our identification of task characteristics and the frictions that hinder proper collaboration were discovered from data. If firms equip engineers and managers with such fine-grained information about tasks that need to be solved, they can evaluate and correct inefficiencies in the system and continue to improve economic outcomes.

## 8. Conclusion

We conduct three field experiments in which a real and profitable business rolled out collaboration in its service delivery workflow. Our results show that work items suited for cross-functional teams are effectively filtered out of the work list and result in cost reductions for both functional and cross-functional work items. After the firm implemented the task characteristics into a recommendation system (HRTech Analytics), we further analyzed the reluctance of engineers to engage in collaborative problem solving. We traced the frictions to an archaic and misaligned incentive system in which the engineers’ collaborative work was not recognized as it should be. After changing the incentive system to remove any misalignment with collaborative work, we finally show the benefits of cross-functional teams.

Hence, we fill the void in the literature along two important dimensions. First, we demonstrate that successful collaboration also hinges on the right assignment of tasks, that is, task characteristics that aid collaboration. Further, we find that, even in the presence of the right task mix and team composition, if personal incentives are misaligned with the firm’s goals, collaboration can be counterproductive. Finally, we show how to effectively align personal incentives with the firm’s goals to unleash the full potential of collaborative problem solving.

Although our goal in this research is to measure the effects of collaboration on a specific industry (ICT), these results are applicable to a much larger class of service delivery scenarios. Any business that involves customers opening trouble or support tickets on installed solutions or equipment will benefit from our analysis. For example, warranties and customer care calls for products could use similar solutions suggested by us as related to collaboration. With a few changes and creative extensions, our methodology can also be applied to workflows that are not necessarily case- or ticket-based but are more long term projects. Examples for application of this methodology can be found in project management, business process management, and research and development and opera tions. This is a rich area for future investigation that promises to deliver considerable value to organizations.

The study is not without limitations. We focus on the effect of collaboration on productivity and costs. However, the benefit of a collaborative process could extend beyond cost to include benefits such as work satisfaction and skill enhancement. The relevance of this research was driven by the reality of the situation and the specific problem at hand. We did not account for employee learning in our model. Whereas this does not appear to be a serious limitation in the context of this specific study, it is clearly an important area of future work that seeks to generalize the methodologies proposed in this study.<sup>16</sup> In the future, the company is contemplating the implementation of collaboration processes with the specific goal of increasing employee learning and crosspollination of expertise. Such strategic goals—different from immediate productivity and costs—would be interesting areas of future research that extend the value of our findings. Our research was conducted in an in-person office setting in which collaboration was accomplished both in a face-to-face manner as well as over IT tools such as Microsoft Teams, phone calls, and email. With the shift in work culture because of the Covid-19 pandemic, an area of future research clearly would be to understand the effects of collaboration in a work-from-home scenario. Finally, the framework outlined in this research can be used to evaluate the effects of collaboration in other business situations. Results from future studies could seek to shed more light on the different mechanisms at play and how collaboration might fare in other problem-solving tasks in business.

## Acknowledgments

The authors gratefully acknowledge and thank the senior editor, associate editor, and reviewers for their constructive comments during the review process.

## Endnotes

<sup>1</sup> During the period of our study, LTE was an emerging wireless communication technology.

<sup>2</sup> Summary statistics of other covariates are given in the online appendix.

<sup>3</sup> Note that our randomization is conducted at the site level, whereas our analysis requires a case-level analysis. This limitation is due to the operational constraints of the collaborating company, which prevented us from conducting randomization at the case level. Conducting case-level randomization could be perceived as disruptive by customers as it would result in two cases coming from the same loca tion of a customer going through two different processes.

<sup>4</sup> Note that, in our DiD specification, the main effects coefficients for Treatment<sub>i</sub> and Experiment are subsumed by the two-way fixed effects and are not directly estimable. If these coefficients are of interest. then one must drop the fixed effects to estimate these main effects.

<sup>5</sup> All effects are calculated as e<sup>β</sup> � 1. For example, for this coefficient of �0.2977, e<sup>β</sup> � 1 is approximately �25.7%.

<sup>6</sup> These billable hours constitute the primary cost to the company. In contrast, factors related to customer satisfaction, that is, CaseTAT and CaseIdleTime, are secondary and are not considered in this analysis.

<sup>7</sup> Similar results were obtained by using a fixed effects model.

<sup>8</sup> Whereas there is no overall impact, we see later that, for some kinds of cases, the collaboration decision does have a significant impact on the engineer hours logged.

<sup>9</sup> Using interaction terms renders the data too thin for any meaningful results; hence, we used a clustering approach that prunes the data that is not influenced by collaboration.

<sup>10</sup> Other alternative algorithms, such as K-medoids and agglomerative hierarchical clustering, produced similar results.

<sup>11</sup> More details on the validation study are provided in the online appendix.

<sup>12</sup> The mean of formal handover cases is 35.63 hours, and the mean of intervened collaboration cases is 13.86 hours, resulting in a 61% improvement.

<sup>13</sup> The mean of collaboration cases is 33.83 hours, and the mean of intervened formal handover cases is 15.13 hours, resulting in a 55.3% improvement.

<sup>14</sup> Details of the recommendation system are given in the online appendix.

<sup>15</sup> More details of experiment three are provided in the online appendix.

<sup>16</sup> The engineers in the study were experienced experts in their tasks. Although differences existed in their inherent abilities, these differences were accounted for using appropriate model specifications, such as engineer-level fixed effects.

## References

Autor DH, Levy F, Murnane RJ (2003) The skill content of recent tech nological change: An empirical exploration. Quart. J. Econom. 118(4):1279–1333.

Bikard M, Murray F, Gans JS (2015) Exploring trade-offs in the organization of scientific work: Collaboration and scientific reward. Management Sci. 61(7):1473–1495.

Blot WJ, Meeter DA (1973) Sequential experimental design procedures. J. Amer. Statist. Assoc. 68(343):586–593.

Campbell DJ (1988) Task complexity: A review and analysis. Acad. Management Rev. 13(1):40–52.

Card D, Mas A, Rothstein J (2008) Tipping and the dynamics of segregation. Quart. J. Econom. 123(1):177–218.

Cummings JN, Kiesler S (2007) Coordination costs and project outcomes in multi-university collaborations. Res. Policy 36(10):1620–1634.

Daley RC (1978) The role of team and task characteristics in R&D team collaborative problem solving and productivity. Management Sci. 24(15):1579–1588.

Fiore SM, Wiltshire TJ (2016) Technology as teammate: Examining the role of external cognition in support of team cognitive processes. Frontiers Psych. 7:1531.

Fisher RA (1952) Sequential experimentation. Biometrics 8(3):183–187.

Fu¨ gener A, Grahl J, Gupta A, Ketter W (2021) Will humans-in-theloop become borgs? Merits and pitfalls of working with AI Management Inform. Systems Quart. 45(3):1527–1556.

Fu¨ gener A, Grahl J, Gupta A, Ketter W (2022) Cognitive challenges in human–artificial intelligence collaboration: Investigating the path toward productive delegation. Inform. Systems Res. 33(2):678–696.

Gardner HK (2016) Smart Collaboration: How Professionals and Their Firms Succeed by Breaking Down Silos (Harvard Business Review Press, Boston).

Goldfarb A, Tucker C, Wang Y (2022) Express: Conducting research in marketing with quasi-experiments. J. Marketing 86(3):1–20.

Goncalo JA, Chatman JA, Duguid MM, Kennedy JA (2015) Creativity from constraint? How the political correctness norm influences creativity in mixed-sex work groups. Admin. Sci. Quart. 60(1):1–30.

Graesser AC, Fiore SM, Greiff S, Andrews-Todd J, Foltz PW, Hesse FW (2018) Advancing the science of collaborative problem solv ing. Psych. Sci. Public Interest 19(2):59–92.

Hackman JR (1968) Effects of task characteristics on group products J. Experiment. Soc. Psych. 4(2):162–187.

Imbens GW, Angrist JD (1994) Identification and estimation of local average treatment effects. J. Econometric Soc. 467–475.

Imbens GW, Lemieux T (2008) Regression discontinuity designs: A guide to practice. J. Econometrics 142(2):615–635.

Jacob R, Zhu P, Somers MA, Bloom H (2012) A Practical Guide to Regression Discontinuity (MDRC, New York).

Jones BF (2009) The burden of knowledge and the “death of th renaissance man”: Is innovation getting harder? Rev. Econom. Stud. 76(1):283–317.

Kay MB, Proudfoot D, Larrick RP (2018) There’s no team in I: How observers perceive individual creativity in a team setting. J. Appl. Psych. 103(4):432–442.

Latane ´ B, Williams K, Harkins S (1979) Many hands make light the work: The causes and consequences of social loafing. J. Personality Soc. Psych. 37(6):822–832.

Li H, Bingham JB, Umphress EE (2007) Fairness from the top: Perceived procedural justice and collaborative problem solving in new product development. Organ. Sci. 18(2):200–216.

Lissoni F, Montobbio F, Zirulia L (2020) Misallocation of scientific credit: The role of hierarchy and preferences. An extension of Lissoni et al. (2013). Indust. Corporate Change 29(6):1471–1482.

Ludwig J, Miller DL (2007) Does Head Start improve children’s life chances? Evidence from a regression discontinuity design. Quart. J. Econom. 122(1):159–208.

Merton RK (1968) The Matthew effect in science: The reward and com munication systems of science are considered. Sci. 159(3810):56–63.

Onal Vural M, Dahlander L, George G (2013) Collaborative benefits and coordination costs: Learning and capability development in science. Strategic Entrepreneurship J. 7(2):122–137.

Ozier O (2018) The impact of secondary schooling in Kenya: A regres sion discontinuity analysis. J. Human Resources 53(1):157–188.

Randel A, Jaussi KS (2003) Functional background identity, diversity, and individual performance in cross-functional teams. Acad. Management J. 46(6):763–774.

Reagans R, Zuckerman EW (2001) Networks, diversity, and produc tivity: The social capital of corporate R&D teams. Organ. Sci. 12(4):502–517.

Reagans R, Miron-Spektor E, Argote L (2016) Knowledge utilization, coordination, and team performance. Organ. Sci. 27(5):1108–1124.

Seamans R, Zhu F (2013) Responses to entry in multi-sided markets: The impact of craigslist on local newspapers. Management Sci. 60(2):476–493.

Setia P, Rajagopalan B, Sambamurthy V, Calantone R (2012) How peripheral developers contribute to open-source software development. Inform. Systems Res. 23(1):144–163.

Singh J, Fleming L (2010) Lone inventors as sources of break throughs: Myth or reality? Management Sci. 56(1):41–56.

Toh PK, Polidoro F (2013) A competition-based explanation of collaborative invention within the firm. Strategic Management J. 34(10):1186–1208.

Vakili K, Teodoridis F, Bikard M (2021) Detrimental collaborations in creative work: Evidence from economics. Organ. Sci. 33(5): 1741–1755.

Wang J, Xie H, Fisher JF (2011) Multilevel Models: Applications Using SAS (Walter de Gruyter, Berlin).

Wood RE (1986) Task complexity: Definition of the construct. Organ Behav. Human Decision Processes 37(1):60–82.

Wuchty S, Jones BF, Uzzi B (2007) The increasing dominance of teams in production of knowledge. Sci. 316(5827):1036–1039.

C<sub>opy</sub>ri<sub>g</sub>ht 2024 b<sub>y</sub> INFORMS <sub>a</sub>ll ri<sub>g</sub>ht<sub>s</sub> r<sub>ese</sub>r<sub>ve</sub>d<sub>.</sub> C<sub>opy</sub>ri<sub>g</sub>ht <sub>o</sub>f Inf<sub>o</sub>rm<sub>a</sub>ti<sub>o</sub>n S<sub>ys</sub>t<sub>e</sub>m<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h i<sub>s</sub> th<sub>e</sub> <sub>p</sub>r<sub>ope</sub>rt<sub>y</sub> <sub>o</sub>f INFORMS <sub>:</sub> In<sub>s</sub>tit<sub>u</sub>t<sub>e</sub> f<sub>o</sub>r O<sub>pe</sub>r<sub>a</sub>ti<sub>o</sub>n<sub>s</sub> R<sub>esea</sub>r<sub>c</sub>h <sub>a</sub>nd it<sub>s</sub> <sub>co</sub>nt<sub>e</sub>nt m<sub>ay</sub> <sub>no</sub>t b<sub>e cop</sub>i<sub>e</sub>d <sub>or ema</sub>il<sub>e</sub>d t<sub>o mu</sub>lti<sub>p</sub>l<sub>e s</sub>it<sub>es or pos</sub>t<sub>e</sub>d t<sub>o a</sub> li<sub>s</sub>t<sub>serv w</sub>ith<sub>ou</sub>t th<sub>e copyr</sub>i<sub>g</sub>ht h<sub>o</sub>ld<sub>er</sub><sup>'</sup><sub>s</sub> <sub>expres s</sub> <sub>wr</sub>itt<sub>en</sub> <sub>perm</sub>i<sub>s s</sub>i<sub>on.</sub> H<sub>owever</sub> <sub>users</sub> <sub>may</sub> <sub>pr</sub>i<sub>n</sub>t d<sub>own</sub>l<sub>oa</sub>d <sub>or</sub> <sub>ema</sub>il <sub>ar</sub>ti<sub>c</sub>l<sub>es</sub> f<sub>or</sub> i<sub>n</sub>di<sub>v</sub>id<sub>ua</sub>l <sub>use</sub>
