---
otero_id: 26174
otero_key: "EVS4ZNZJ"
title: "Dealing with Risk: A Practical Approach"
authors: "Fred J. Heemstra; Rob J. Kusters"
year: "1996"
journal: "Journal of Information Technology"
doi: "10.1177/026839629601100407"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Dealing with risk: a practical approach

FRED J. HEEMSTRA

Open University, Department of Economics, Business and Public Administration, P.O. Box 2960, 6401 DL Heerlen, The Netherlands

ROB J. KUSTERS

Eindhoven University of Technology, Department of Technology Management, P.O. Box 513, 5600 MB
Eindhoven, The Netherlands

Most software projects take place in a volatile environment in which many dangers exist that may affect the successful outcome of the project. After completion of the project an evaluation may show that many of the problems encountered during the project could have been foreseen before they actually occurred. Risk management is an approach that is aimed at predicting the occurrence of this type of problem and at taking counter measures to either prevent them from affecting the project or to soften their impact. In this paper the basic activities related to risk management are described. Furthermore a concrete method aimed at supporting risk management is presented. This method has been used successfully in practice. Some of the results obtained by using it are presented on the basis of five cases. Some conclusions are that:

(1) the use of a short and structured checklist will ease identification of and discussions about risks,

(2) a risk management method in which explicit use is made of a group related approach, involving all parties, will increase reliability and acceptance of the results, and

(3) involvement of a neutral process risk advisor will further both the successful use of the method and the acceptance of the results.

## Introduction

This paper describes the result of an action research programme in which theoretical concepts from the area of risk management were tested and adapted in a number of practical settings. It is common knowledge that software projects do not always take place according to plan. Cost and time overruns, insufficient quality and even totally failed projects occur too often. When looking at these project with the benefit of '20-20 hindsight' it is most of the time possible to indicate a number of problems that have contributed towards the final result.

The premise behind risk management within the context of IT-project management is that these problems can not only be identified after the fact. However, it is feasible to identify potential problems before they occur and to take measures to prevent them from influencing the execution of the project or, at least, alleviate their impact. In this paper we will see how risk management can be successfully implemented in practice. The paper looks both at theory and practice. First the theoretical aspects of risk management are treated in the next section (basic definitions, risk management concepts and the link with project management). Then the link with practice is made by describing a concrete method for risk management. This is followed by a description of some results that were obtained by using this method. Finally, a discussion of the results is presented.

## Risk and risk management: some definitions

## Risk, risk impact and risk exposure

The classical definition of risk is ‘the potential for realization of unwanted, negative consequences of an event’. The basic elements of this definition are (Charette, 1990):

(i) a degree of uncertainty regarding the occurrence of the problem and

(ii) a (negative) effect on the project if the problem occurs.

The magnitude of the loss is referred to as risk impact. This impact can be experienced in several ways such as longer lead-times, additional expenditure, lower quality, a lack of functionality or, in a worst case scenario, a total failure of the project.

The element of uncertainty can be treated as a level of probability. This can be expressed as a number between 0 (impossible) and 1 (certainty), but more subjective metrics (e.g. 'small', 'medium', 'large') are also commonly used. This element of uncertainty is fundamental to the concept of risk. If it is extremely unlikely that a given problem will take place it can (and will) usually be safely discarded. If, on the other hand, it is certain that it will occur, normal project management practices will ensure that the problem is dealt with. The intermediate area is the subject of this paper.

When discussing the potential effect of risks and of counter measures two additional notions may be of use. The first concerns the loss expectation. This can be expressed as the product of the risk impact multiplied by the probability and is referred to as the risk exposure. It indicates that when looking at risks the combination of both aspects (probability as well as impact) will have to be taken into account. For example, a risk with a high impact will warrant a lot more attention when it has a high probability of occurring. When the odds are favourable, the risk merits less attention. A typical example is the risk of a fire destroying the project archive. The potential impact of this risk is high, but nonetheless it normally receives little or no attention since the chances of this happening are extremely low.

The second notion, risk reduction leverage, builds on the previous. The notion is aimed at determining the effectiveness of a possible counter measure by comparing its cost to its expected benefit. Risk reduction leverage (RRL) can be expressed as the decrease in risk exposure (RE) due to the measure divided by the cost of the measure (CM):

$$
R R L = \left(\mathrm{RE} _ {\text { before }} - R E _ {\text { after }}\right) / C M
$$

If we look again at the fire hazard example:

(1) for a paper archive a possible counter measure could be to insure that a recent copy of the archive always exists in another building. This is a fairly costly measure which will reduce a risk with minimal RE to practically zero. Most of the time this measure will not be seen to be cost effective.

(2) for an electronic archive a possible measure might be the inclusion of the archive in existing back-up procedures. This measure would cost hardly anything and would therefore be more likely to be cost effective.

## Risk management

Risk management is focused on (Boehm, 1991; SEI, 1991; Rook, 1993; SEI, 1993):

(1) risk assessment

(2) risk control

(3) risk monitoring

(4) risk evaluation

Risk assessment deals with determining threats to the project and consists of:

## (1) Risk identification

Risk identification is concerned with finding all risks that might influence the current project. Given this diversity in potential problems, all parties to the project should be involved in this process of risk identification. Risk identification is improved by reference to recorded experience, usually in the form of checklists. This approach can be traced back to McFarlan. At least as useful are checklists derived from recorded local experience.

## (2) Risk analysis

The goal of this activity is to determine for all the risks identified the risk exposure. Also interactions have to be taken into account. For instance, a small risk can become a big one after some time or risks interact mutually or a number of risks may be caused by one underlying factor. Techniques available (Heemstra and Kusters, 1993) are mostly a combination of expert judgement, expert group consensus techniques, use of historical data, analogy, what-if analysis and samples from probability distributions.

## (3) Risk prioritization

The purpose of risk prioritization is to choose, from the full list of risks identified, the most important to form a subset of manageable proportions. The prioritized list is a dynamic subset of the total list of risk items. Risk assessment should be a repeated activity, and both lists will change as the project progresses. Risk items will disappear as their threat vanishes, new risks will be identified, and risk exposures will change with the passage of time or as the result of action to reduce or eliminate the risks.

Risk control consists of actions to reduce risk, and to run the project in a risk-free or risk tolerant way and to trigger further defensive actions in the case of occurrence of certain events. As an example one might imagine that when a certain number of customer complaints are logged a meeting with the customer representatives is scheduled in order to prevent further customer dissatisfaction. Monitoring actions are required to verify that the risks are indeed resolved or extra risk reducing measures are required.

Risk control consist of the following activities:

(1) determining the most suitable way of reducing the significant risks

If we do not know enough about the risks involved possible actions are buying information by expenditure on prototyping, simulation, surveys, benchmarks, reference checks etc. In dealing with known, assessed risk items many counter measures can be envisaged. These measures may be grouped into four categories:

(i) Risk elimination, eliminate the root of the risk.

(ii) Risk reduction, take measures aimed at reducing the impact of the risk if it occurs.

(iii) Risk transfer, by reallocating risks to other systems.

(iv) Risk compensation, where it is accepted that the risks exist and that if it occurs it will be dealt with.

## (2) producing risk management plans

The practice of Risk Management plans as part of the bidding process, and negotiation between supplier and customer is becoming widespread as it is seen as an effective way of dealing with risky projects. The Risk Management plans (primarily addressing the reduction of project-specific risks) must be co-ordinated with each other, and with the project plan (in which the reduction of generic risks has been addressed). This is especially necessary for the effect on schedule and the planned utilization of resources.

(3) setting up a basis for controlling the residual risks If adequate risk assessment and risk reduction is carried out at the start of the project then, as the project progresses, the planned actions will mostly have the intended effect of mitigating the risks.

Risk Monitoring on a regular basis has the goals of finding out whether the risks are being successfully controlled, identifying risks which have become problems which have not yet been detected, and gaining insight to foresee new risks (e.g., reliability of estimates for the next stages of the project). Two basic activities are:

(1) risk reporting

Risk Reporting recognizes responsibility of reporting to senior management in the organization and to the customer. Such reporting is best based on an assessment of the currently most threatening risks.

(2) risk reassessment

Risk Reassessment is a continuous process. The Risk Management Control loop depends on risk monitoring leading to risk reassessment, corrective action and adjustments to Risk Management plans to stay in control of the perceived risks.

Risk Evaluation will focus on two objects. First the finished project will have to be looked at in order to answer questions such as ‘has the project been executed the right way’. Furthermore the experience gathered during the project can now be consolidated. This information can be used to get a better grip in risk management during future projects. Secondly the process of risk management as carried out during the project will have to be evaluated and if necessary adapted.

## Risk management and project management

It is important to understand the relationship of Risk Management to Project Management. The goal of traditional Project Management is to control pervasive risks (such as availability of staff) by using systematic procedures (for example network planning) to estimate and plan the work, lead and direct the staff, monitor progress and control the project by replanning and reassignment of resources as necessary. This remains the fundamental basis for Project Management and is not invalidated by any considerations of Risk Management. However, on its own, it is a recipe for ‘problem management’ in that difficult decisions are addressed and actions taken only when a problem arises – and becomes apparent at management level. The Americans use an attention-getting phrase ‘a problem is a risk whose time has come’ to illustrate the principle that Risk Management is concerned with controlling risks by acting before risks become problems.

Risk Management is not synonymous with Project Management, nor a replacement for it, nor something entirely separate. Rather it is an explicit extension of traditional Project Management, closely intertwined with information gathering and decision making. The goal of Project Management is a project which meets its targets. When a project is successful, it is not because there were no problems, but because the problems were successfully overcome. Risk Management does not guarantee success, but has the primary goal of identifying and responding to potential problems with sufficient lead time to avoid crisis situations, so that it is possible for Project Management to achieve its goal.

## Design of a risk management method

After describing the basic theory of IT-project risk management we will now turn to some results from practice. To implement the (theoretical) ideas presented above a method was designed and tested in practice (Heemstra and Kusters, 1993a). This section of the paper will present this risk management method. First, a number of design choices that were made will be discussed. The method itself is then presented and some attention is paid to the introduction, use and control of a Risk Management method. The remaining sections will look at the results that were obtained using the method.

## Design choices

When designing a method based on a set of theoretical principles, many design choices will have to be made. Most of these will be trivial or obvious (for instance the decision to involve the project manager), but in our approach we made several choices which we think are useful to discuss and which in our opinion contribute towards the success of this approach.

The first of these choices was to take an approach in which all parties that are part of the problem will also participate in its resolution. Risk management is not an activity that can be carried out by a single person, even if this person is a very experienced project manager. There are several reasons for this:

(1) participation will increase the commitment of the staff involved and ensure professional acceptance,

(2) the amount of information involved and the uncertainty entailed make it almost impossible for one person to have a sufficient overview to perform a sufficient risk analysis,

(3) involvement of development staff insures that the required insight into the development process is available.

Even when all parties involved in the project are also represented in the risk management effort, it is wise to remember that (a) they are ‘parties’, in the sense that they all have their own agenda which may not be in alignment, and (b) risk management is not the main daily activity for the parties involved. They usually have other concerns, such as working on the project itself, which are often perceived to be more important.

For these reasons the role of ‘risk advisor’ was added to the method. The risk advisor is a neutral outsider who has no political goals hanging from the project. His task is to function as an impartial mediator between parties and to manage the risk management process. As such, this risk advisor should be acquainted with the areas of systems developed and of organization and information analysis. Furthermore he/she should possess social skills such as the ability to convince people, to lead meetings and to organize their own and other peoples activities. Any experienced project manager should be able to fulfil this role.

The insight into the project which is required for proper risk management to take place can be enhanced if unambiguous data on this project and comparable previous projects are available. For this reason we based the risk management method on the use of a checklist. However, since no checklist, however detailed, can ever be complete, we opted for an approach in which a relatively low number of high level risk factors were identified (Appendix A). On the one hand this provides sufficient information and is sufficiently unambiguous to facilitate the discussion. On the other hand it still stimulates people to think for themselves.

On the basis of these three choices a risk management method was designed and tested. Later, based on the practical experience described, we will again look at these choices to see if they can be justified.

When designing the method the three design choices described above were taken as a starting point, together with the general list of risk management activities which was described earlier. Based on these premises a number of different methods can be designed. The method described below is designed specifically to fit in with the culture and customs of a specific organization. This is reflected in many details. Examples are:

(1) The terms used (in the original Dutch version at least) adhere to the local usage of language within the test organization.

(2) Also, the method requires the formation of a specific risk management team which also contains people from outside the project team. These were necessary since in the test organization the project team consisted of IT-staff thus providing too small a basis. Organizations using broader based project teams can staff their risk management team with a subset of the project team, which will usually be easier.

When applying the method described here to another organization we would advise adherence to the basis principles, but to adapt anything else to the specific local circumstances. The method we used is described in more detail below.

## A risk management method

The Risk Management method (Heemstra and Kusters, 1993 and 1993a) described in this section can

## Dealing with risk

be roughly divided into three phases, each containing several steps.

The first phase is called the initiation phase and consists of two steps:

Step 1: Selection of members of the Risk Management team,

Step 2: Explanation of the method to the members of the team and planning of the ‘risk activities’.

The second phase is called the execution phase. In this phase activities are carried out regarding identification, analysis and monitoring of risks. More specifically the next steps must be executed:

Step 3: Identification of risks,

Step 4: Pre-selection of identified risks,

Step 5: Final risk identification and selection via a joint risk management team meeting,

Step 6: Risk monitoring, (repeat steps 4 and 5).

The last phase is called the evaluation phase and consists of:

Step 7: Compiling a Risk Management evaluation report.

Each of these steps will be discussed more in detail below.

## Step 1: Selection of members Risk Management team

The goal of the first step is the composition of a Risk Management team. The representation of each party involved in the project by at least one person is an important point in the selection procedure. Arguments for involvement of this large number of parties are (Howard et al., 1992):

(1) the acceptance of and commitment to the results,

(2) the communication between the parties concerned is promoted,

(3) working as a team makes use of the advantages of group work compared to individual work in uncertain/risky situations.

The project leader, in co-operation with a so-called risk advisor are the initiators for the selection. The risk advisor, an experienced user of the Risk Management method, should be someone from outside the project. Our experiences with the described procedure indicate that the contribution of a risk advisor is very desirable. Later, these experiences will be discussed in more detail.

Step 2: Explanation of the method to the members of the team and planning of the ‘risk activities’

The goals of step 2 are to inform all members about the work procedure and to acquire the required commitment. It must be clear what is to be expected of the team members, how much time it costs, and what the results will be. This step may take place in the form of a kick-off meeting in which the risk advisor presents the goal and method of the risk management activities and together with the project manager answers any questions that might arise. It will conclude with making appointments for interviews and the joint team meeting (see step 5). If all participants have experience with the method this meeting may be skipped.

## Step 3: Indentification of risk sources

The risk advisor meets each team member to carry out an interview to make a member's risk identification. For this purpose a checklist is used. Based on literature, previous experiences, local circumstances and usage of language of the organization a checklist was designed (see Appendix A). This checklist contains 36 risk factors which are organized in nine categories. In each of these clusters a series of relevant risk factors was identified. An example of a cluster is the cluster ‘application’ where the risk factors ‘size’, ‘complexity’, and ‘degree of innovation’ were distinguished. To operationalize this list, for each risk factor one or more questions were formulated to help the interviewees in determining the amount of risk involved. If answered, these questions provide a project specific description of the risk factor. The checklist has to be adapted to the language and the specific characteristics of the organization concerned. In the interview people are asked for each risk factor to:

(1) estimate the probability of occurrence (low/medium/high/very high),

(2) describe the impact of the risk factor if it did occur, and

(3) provide any additional comment they might wish to make.

## Step 4: Pre-selection of identified risks

After competing all the interviews a critical analysis must be carried out in order to select the most relevant risk factors.

Step 5: Final risk source identification and selection via a joint team meeting

The objective of the Risk Management team meeting is:

(1) to confront the team members with each other's perception of potential risks,

(2) to start a discussion on risk probabilities and effects,

(3) to reach the most uniform team decision possible about risks, probabilities and effects, (4) to agree upon risk reducing actions, such as assigning an assistant project manager to counter the adverse effects of a sudden career move by the project manager, provide additional training to combat a knowledge shortfall, or assure that Mr Jones will be part of the project team because of his specialist knowledge,

(5) to decide who is responsible for the execution of these actions, who will supervise this, what are the time limits within which each action has to be completed, how to report, etc.

The result of the meeting is a final list of the most important risks, with for each identified risk an overview of actions, responsibilities, competencies, work-schedules, etc. An additional result is an increase in the level and effectiveness of communication between the parties involved together with a higher level of commitment to the project goals and the risk management effort.

## Step 6: Risk monitoring

During the execution of the project the risk team has to meet regularly to monitor the status of the identified risks. When and how often depends on the size, complexity, importance, number and type of risks. As a preparation to these meetings all members are contacted to see:

(1) if the measures decided in the previous meeting have been carried out,

(2) what the status of the relevant risk factors is, (3) if any new relevant risk factors have developed during the last period.

This information is gathered and presented at a meeting. During this meeting each relevant risk factor and the measures associated with it are discussed. This leads to:

(1) dismissal of some factors from further consideration,

(2) continuation of the status for other factors, or (3) formulation of additional measures for the remaining factors.

Step 7: Compiling a Risk Management evaluation report The objective is to:

(1) give an overview of the risks and the chosen actions,

(2) conclude the ‘lessons learned’ for future projects.

## Introduction, use and control of a risk management procedure

## Introduction

Introducing a risk management procedure takes a lot of time and effort and requires therefore a well prepared introduction within an organization. An introduction is needed to convince all parties of the importance of identifying and controlling risks. To enlarge the acceptance the organization has to combine it with existing risk approaches, project control methods and working procedures within the organization. This means e.g., adapting the risk management procedure to the organization's language, definitions and ideas. Adjusting the checklist is inevitable. It is generally advisable to start the introduction with a pilot project.

## Costs and benefits

Risk management is not limited to a specific type of project. It is however a matter of course that the costs using the method must be in a proper perspective to the costs of the complete project. For small projects a so-called ‘short cut’ version of the method is advisable. The costs of using such a method can be calculated straightforward from the data in Table 1 which are based on our experiences.

If we take a project with four meetings $(M=4)$ over a period of a year and a risk management team which apart from the risk advisor and the project manager comprises 8 team members (N = 8). The risk advisor will now spend approximately 75 hours, the project leader 16 hours and each team member 15 hours. This gives a total of 211 hours, but it has to be kept in mind that both project manager and a number of team members most likely would have spent time on informal risk management activities.

Table 1 Costs of using the risk management procedure (N = number of risk team members, M = number of risk team meetings)

<table><tr><td>Step</td><td>Risk advisor</td><td>Project leader</td><td>Member</td></tr><tr><td>1 Selection members</td><td>1 hour</td><td>1 hour</td><td>0 hours</td></tr><tr><td>2 Explanation</td><td>4 hours</td><td>1.5 hours</td><td>1.5 hours</td></tr><tr><td>3 Risk identification</td><td> $3 \times N$ hours</td><td>1.5 hours</td><td>1.5 hours</td></tr><tr><td>4 Pre-selection</td><td>4 hours</td><td>0 hours</td><td>0 hours</td></tr><tr><td>5 Group meeting</td><td>8 hours</td><td>3 hours</td><td>3 hours</td></tr><tr><td>6 Risk monitoring</td><td> $8 \text{ hours} \times M$ </td><td> $3 \text{ hours} \times M$ </td><td> $3 \text{ hours} \times M$ </td></tr><tr><td>7 Evaluation report</td><td>8 hours</td><td>0 hours</td><td>0 hours</td></tr><tr><td>Total</td><td> $24 + 3N + 8M$ </td><td> $7 + 3M$ </td><td> $6 + 3M$ </td></tr></table>

Table 2 Overview of number of risks identified by the individual team members

<table><tr><td>project</td><td colspan="15">Risk team member:</td></tr><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td><td>8</td><td>9</td><td>10</td><td>11</td><td>12</td><td>13</td><td>14</td><td>15</td></tr><tr><td>A</td><td>13</td><td>2</td><td>17</td><td>3</td><td>5</td><td>8</td><td>2</td><td>10</td><td>10</td><td>10</td><td>11</td><td>15</td><td>18</td><td>13</td><td>9</td></tr><tr><td>B</td><td>11</td><td>19</td><td>9</td><td>6</td><td>4</td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>C</td><td>8</td><td>11</td><td>11</td><td>17</td><td>12</td><td>8</td><td>3</td><td>13</td><td>9</td><td>9</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>D</td><td>8</td><td>6</td><td>14</td><td>11</td><td>9</td><td>6</td><td>5</td><td>9</td><td>5</td><td>12</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>E</td><td>8</td><td>4</td><td>2</td><td>3</td><td>8</td><td>4</td><td>17</td><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

The benefits are most difficult to quantify. A successful application of risk management enables the project manager to deal in a structured way with the uncertainties surrounding the project. In doing so the level of uncertainty is decreased and a successful outcome of the project is more likely. The occurrence during the project of a number of problems, each with their associated costs, may have been prevented. Whether or not this benefit outweighs the costs can not be decided on the basis of theoretical reasoning only, although the known tendency of IT projects to get out of control would tend to support a positive answer. The practical experiences recorded in the next section will provide some additional arguments.

## Control

The Risk Management method should be evaluated during use within an organization. This allows the procedure to be adapted to changing circumstances, opinions etc. This all means that the evaluation results must be gathered, that changes must be realised, and that new releases must be distributed. To carry out these activities, a central point in the organization which can double as a help desk is recommended.

## Some results from practice

The risk management method has been tested on consistency and usefulness several times in 5 ‘real life’ projects. In Appendix B short descriptions and evaluations of these projects are represented. All projects took place within a large Dutch governmental organization and can be characterized as:

(1) Project A: a package implementation;

(2) Project B: the design of specifications for external use;

(3) Project C: the design of a long term architecture;

(4) Project D: the design and building of an application;

(5) Project E: the implementation of a test application for evaluation purposes.

In each project we were able to implement the method, sometimes with minor changes. In case A only it was necessary to make more radical changes to the checklist, thereby placing more emphasis on the human aspect and downplaying the technical development risks.

In all projects the authors acted as risk advisors and carried out the interviews. Table 2 shows the number of risks that were identified by each participant during the interviews. As can be seen the numbers are widely divergent. Within a project the number of risks identified by each individual risk management team member could vary from as low as 2 to as high as 17. This divergence can be noticed in every project. Apparently there existed different impressions as to which risks might trouble each project.

Analysing the results it was always possible to come up with a plausible list of pre-selected risks for further discussion. This pre-selection consisted on average of 9 risks (see Table 3). These were in general risks that were mentioned in the checklist, but in one case a risk was included that was added during the interviews. The summary result, together with the (anonymous) individual interview results were always sent to each participant before the joint meeting. This enabled them to prepare so the meeting itself could run more smoothly.

During the group meeting a structured approach was taken in order to be able to cover all pre-selected risks and to leave time for additional risks that might come up. As can be seen in Table 3, the pre-selection generally gave a good starting point for the discussion. On average all but two of the pre-selected risks were felt by the joint team to be of interest to the project. These risks needed further watching. In three out of five meetings an additional point came up, showing that the pre-selection can not be taken as the only basis for discussion.

Table 3 Overview of number risks identified during the group meeting

<table><tr><td>Project</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td></tr><tr><td>Average number of risks mentioned during the interview</td><td>11.1</td><td>9.0</td><td>10.1</td><td>8.2</td><td>6.8</td></tr><tr><td>Number of risks pre-selected</td><td>10</td><td>6</td><td>7</td><td>10</td><td>10</td></tr><tr><td>Number of pre-selected risks that were accepted by the team</td><td>9</td><td>4</td><td>5</td><td>7</td><td>8</td></tr><tr><td>Number of additional risks discussed during the team meeting</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Number of risks accepted from these additional risks</td><td>1</td><td>1</td><td>1</td><td>0</td><td>0</td></tr><tr><td>Number of counter measures decided upon</td><td>8</td><td>11</td><td>7</td><td>6</td><td>6</td></tr></table>

For all risks, serious attention was paid to the identification of relevant counter measures.

Project E was followed by a formal evaluation of the method. The most important conclusions were:

(1) All the team members were enthusiastic about the use of the risk checklist. The list turned out to be a valuable tool for risk identification. The team members did not have the feeling that they were pushed to select the risk factors mentioned in the checklist.

(2) Also the group meetings were unanimously positively appreciated. Not only did the discussions about risks, risk reduction etc., appear to be useful but also the side effects namely communication about goals, expectations, responsibilities etc., were found helpful.

(3) The team members were of the opinion that the implementation of the method was a success factor for the project. Some went as far as to state that this specific project would have failed without the use of the method.

(4) The participation of the external risk advisor stimulated objectivity.

(5) Some weaker points were:

(i) the description of the risks was sometimes abstract;

(ii) the method was time intensive;

(iii) the relation with project management was not clear.

This formal evaluation led to adoption of the method. However, given the size and diversity of the organization in question coupled with a reluctance to impose methods and techniques, the usage of the method was not made obligatory. Instead, the manual describing the method was made freely available to the organization. Furthermore, a one day course was developed aimed at teaching basic risk management concepts and the risk management method as well as providing some hands-on experience with the method. Approximately 40 members from the organization participated in this course. Finally, a central help desk was installed which also acts as a broker in providing mutual risk advisor support within the organization.

## Discussion

In this discussion we will again focus on the three design choices that we think contributed to the success of the method, namely the checklist, the group aspect and the risk advisor.

## The checklist

Using a checklist has advantages and disadvantages. The most important advantage is, that a comprehensive coverage of relevant risk factors is presented which can help in determining the most relevant risk factors for a project in a relatively easy manner. As stated, it is unlikely that any checklist, however meticulously assembled, can cover all possible risks that might endanger a project. It has been our experience that it is very difficult to get people to look beyond the checklist to see if new factors play a part in the project in hand. The danger of using a checklist is that these factors will be consistently overlooked. On the whole it is our experience that the advantages of using such a list outweighs this danger. However, this required the checklist to be of manageable size. We used a checklist of 36 risk factors, which have been formulated based on a higher level of abstraction. This provided a solid basis for discussion. What was found to be important is the formulation of the checklist by using local definitions and language (jargon) that fit in with the organization.

## The group aspect

In the interviews each team member came up with his own set of relevant risk factors. There was some overlap between them, but there was rarely a complete agreement about the impact of any specific risk factor. During the group session it was found that it was relatively easy to reconcile these differences, resulting in a relatively small set of relevant risk factors and accompanying measures. If the risk analysis had been performed by a single person, the result would no doubt have been different as can be seen in Table 2. It is clear that no single person has sufficient overview to assess all the relevant aspects of the project in hand. This certainly is a plea for using a group approach for this type of problem (Howard et al., 1992).

Dealing with risk

Another advantage of the group approach is that afterwards not only are all the relevant risk factors known to all team members, but the team also agree what factors are relevant to the project. This ensures a greater commitment to the measures and facilitates overall effectiveness.

## Process guidance

An interesting phenomenon is that of the influence of the participation of the risk advisor. We got the impression that the discussion with the (neutral) interviewer about the meaning of terms and the possible effect on the project in hand were seen to be at least as useful as the use of the checklist. The use of a checklist without this discussion is in danger of turning into a mechanical activity. On the other hand, a discussion without the use of a checklist is very difficult to structure. Both elements complement one another very well.

A similar effect was noted during the group meetings. All other participants were at one moment or another partisan in the discussion where they defended or attacked a given position. It would probably have caused problems if one of them had chaired the meeting since either the chairman would become party in the discussion, thereby taking advantage of his position, or he would abstain from advancing an issue, thereby denying it sufficient representation in the discussion. The risk advisor could chair the meetings without these adverse effects. Furthermore the presence of a neutral outsider kept the discussion on a businesslike footing.

Also during the preparation of the meetings the involvement of the advisor in the day to day running of the project had positive effects. The project leader, who definitely is an interested party in the project cannot carry out this role since there can be a conflict of interest between the primary goal of any project leader, getting the project out in time, and the goals promoted by the advisor.

## Conclusion

The final conclusion to this study is that the approach as depicted above works in practice. The theoretical benefits of risk management, being able to cope better with the uncertainties surrounding any IT project, could be realized at acceptable costs by using the method. The idea of a locally defined checklist, used by a group of involved people and supported by an uninvolved project guide was considered by all parties involved to be a useful contribution towards controlling the project. True, this does not prove that the design choices we made are the best imaginable, but it is an indication that they result in a useful method. The next step now is to set in motion a learning curve where experience from previous projects, registered in a standard way can contributed towards control of future projects.

## References

Boehm, B. (1991) Software risk management: principles and practices. IEEE Software, 8.

Charette, R.N. (1990) Application Strategies for Risk Analysis, (McGraw-Hill).

Heemstra, F.J. and Kusters, R. (1993) Risk management for information system development (Risk-management van de informatiesysteem-ontwikkeling bij Rijkswaterstaat). Eindrapport, Dutch Ministry of Transport, RWS/AVV.

Heemstra, F.J. and Kusters, R. (1993a) Advisory report: Risk Management in a governmental organisation (Advies rapport: Risico-management van de informatiesysteem-ontwikkeling bij Ritswaterstaat). Dutch Ministry of Transport, RWS/AVV.

Howard, M., Kusters, R.J., Heemstra, F.J. and Genuchten, M. van (1992) Software cost estimation as a group process, an alternative approach (Begroten van software als groepsproces: een alternatieve benadering). Bedrijfskunde, 64, 143–53.

Rook, P. (1993) Risk management for software development. Proceedings of the European Software Cost Modelling Meeting, Ivrea, (Software Reliability Institute, London).

SEI, (1991) Proceedings of the SEI Software Risk Management Conference, (SEI).

SEI, (1993) Proceedings of the Second SEI Conference on Software Risk, (SEI).

## Appendix A: Checklist risk management

## Introduction

The checklist consists of nine clusters of risk categories. In each cluster a series of relevant risk factors is identified. The list covers the most well-known risk factors. However the list doesn't pretend to be complete. A complete checklist list does not and cannot exist, given the enormous variety of possible events which can influence (negatively) the execution of an automation project. The checklist starts with a general discussion of project goals. It further consists of nine clusters representing the most important risk categories

\- sponsor

\- users

\- project planning

\- developers

\- user management

\- means

\- the system

\- systems management

\- specifications

In each of these categories several risk factors are distinguished. Each risk factor must be evaluated using the checklist. In order to facilitate the evaluation each risk factor is defined. This is not done by means of a formal definition, but by the formulation of a number of questions. The answers and the underlying argumentation provide project specific insights into the potential of the risk factor. The answers can also support a discussion if the evaluations of several interviewees differ.

In order to estimate the influence of a specific risk factor a distinction is made between the probability that the risk factor occurs during the project and the impact of the risk factor. The distinction facilitates the evaluation of the risk factors. For reasons of simplicity the probability of risk occurrence will only be formulated using one of the next four fixed values.

\- small The probability of risk occurrence is negligible (in statistical terms: smaller than 0.1). Further discussion of these risk factors has no meaning as long as the impact is not dramatic.

\- medium There is a probability (not large however) that the risk factor has an influence (in statistical terms: between 0.1 and 0.3. Further discussion is only necessary if the impact is significant.

\- large The probability of risk occurrence is large (in statistical terms: between 0.4 and 0.7). Risk factors with a medium or large impact need further discussion.

\- very large These factors will almost certainly occur (in statistical terms: larger than 0.7). Further discussion is always necessary independent of the impact level.

Besides a choice between small, medium, large and very large the interviewee should also estimate the potential impact of the risk factor. The occurrence of a risk factor can influence the project and/or the system. The effects on the project are in general costs and lead time effects. Effects on the system are mostly loss of functionality or quality. Both aspects – product and project – are closely related. Gains on one aspect, for example shorter lead time, will in general cause losses on the other aspect. Assessment of the impact in general terms tend to provide a sufficient basis for further discussion.

## The checklist

0 PROJECT GOAL

I SPONSOR

1.1 Position sponsor

1.1.1 How important is the sponsor, can he provide sufficient support to the project

1.1.2 Has the sponsor sufficient budgetary freedom to compensate possible (financial) setbacks

1.2 Clarity as to who is the sponsor

1.2.1 How many sponsors does the project have

1.2.2. Will the sponsor remain the same during the project

1.3 Clarity of the goals of the sponsor

1.3.1 Is the sponsor able to assess the functional and non-functional requirements

1.4 Commitment sponsor

1.4.1 Are the benefits of the system clear

1.4.2 Are the costs of the system clear

1.4.3 Does the sponsor assign high priority to the system

1.4.4 Is the sponsor willing to spend time and money on a preliminary study

1.4.5 Does the sponsor like the project

1.4.6 Does the sponsor want to be involved closely with the project

1.5 Position of the project in the organization

1.5.1 When did the first ideas originate within the organization to develop such a system

1.5.2 Does a clear defined reason exist for starting systems development now

1.5.3 Was the start-up of the project characterized by a long political decision process

2 USERS

2.1 User organization

2.1.1. Is the systems environment unstable

2.1.2 What is education level of the users

2.1.3 Is the user organization formal/informal

2.1.4 Does the user organization contain different and conflicting cultures

2.1.5 In how many departments will the system be implemented

2.2 IT experience

2.2.1 Is the user organization computer minded

2.2.2 How many automated system are active within the user organization

2.2.3 Is the organization familiar with IT development projects

2.2.4 Will the user organization show resistance to change

2.2.5 Has the user organization had previous bad experiences with IT development projects

2.3 Position of a project approach in the user organization

2.3.1 Is the user organization familiar with a project approach

2.3.2 Do the users book time in their work plans in order to participate in projects

## Dealing with risk

2.4 Importance of the system for the users

2.4.1 What are the consequences for the user organization in case of system development failure

2.4.2 Is systems development related to the core business/core activities or to a support function

2.5 Acceptance by the users

2.5.1 Will the user be confronted with many changes in his daily work

2.5.2 Are the users eager to work with the system

2.5.3 Will the user be confronted with new hardware

2.6 Participation

2.6.1 How many people from the user organization are added to the project

2.6.2 What is the status of the involved users (are they experts?)

2.6.3 How is the involvement of these employees with the development project

2.6.4 Are all (relevant) stakeholders of the user organization involved in the project

2.6.5 Have agreements been made concerning user involvement

2.7 Transfer of knowledge

2.7.1 How much domain knowledge has to be transferred from user to systems developer

2.7.2 Do users and systems developers speak the same 'language'

## 3. USER MANAGEMENT

3.1 Clarity of goals of user management

3.1.1 Is the user management able to assess the functional and non-functional requirements

3.2 Commitment

3.2.1 Is user management aware of system benefits

3.2.2 Is user management aware of system costs

3.2.3 Does user management like this project

3.2.4 Does user management want to be involved closely in the project

## 4. THE SYSTEM

4.1 System size and project duration

4.1.1 Do you have an estimation of system size

4.1.2 Are you experienced/familiar with systems development of comparable size

4.1.3 Do you have an estimation of project lead-time

4.1.4 Are you experienced/familiar with projects of comparable lead-time

4.2 System complexity

4.2.1 Do you have an estimation of systems complexity

4.2.2 Do you know which factors complicate systems development

4.2.3 Are you experienced/familiar with system development of this complexity

4.3 Type of system

4.3.1 Are you experienced/familiar with this type of system

4.3.1 Is the system innovative for you

4.3.3 Is the system in general innovative

4.3.4 Must the system be implemented in a network environment

4.3.5 Must the system be integrated with existing systems

4.3.6 Is an information/automation plan available

4.3.7 What is your opinion of the quality of this plan

4.3.8 Does the information impose limitations on the system

## 5. SPECIFICATIONS

5.1 Clarity of specifications

5.1.1 Are specifications currently available

5.1.2 Do you think that the specification currently available are complete

5.1.3 Will it be difficult to complete the specifications

5.1.4 Does the system replace manual procedures

5.1.5 Have system parts already been automated

5.2 Stability of specifications

5.2.1 What is the probability that the specifications will change during systems development

5.2.2 Have agreements been made with user or sponsor concerning ‘freezing of specifications’

5.2.3 Have agreements been made with user or sponsor concerning extra costs in case of added or changed specifications

5.3 Acceptance of specifications

5.3.1 Are the specifications known to all parties involved

5.3.2 Have the specifications been accepted by all parties involved

5.3.3 Has this acceptance been formalized

5.4 Quality of the specifications

5.4.1 Are you satisfied with the quality of the specifications

5.4.2 Are the demands concerning privacy and security difficult/severe

5.4.3 The same question concerning system reliability

5.4.4 The same question concerning response time

5.4.5 The same question concerning user friendliness

5.4.6 The same question concerning maintainability

5.4.7 The same question concerning system adaptability

5.4.8 The same question concerning system flexibility

5.4.9 Do specifications include non-functional specifications like the ones mentioned above

## 6. PROJECT PLANNING

6.1 Project plan

6.1.1 Has a project plan been made for the development of the system

6.1.2 Is a work breakdown structure included in this plan

6.1.3 Is an allocation of tasks (who does what and when) included in this plan

6.1.4 Is the project manageable (less than two years lead time)

6.2 Degrees of freedom in planning

6.2.1 Do we have a fixed price, fixed time and fixed quality project

6.2.2 Is it possible to negotiate with the sponsor changes in required time, price and quality

6.2.3 Has the delivery time been fixed

6.2.4 Has the system to be realized under severe time constraints

6.2.5 Does the plan contain too much slack

6.3 Progress control

6.3.1 Is it known which products have to be produced

6.3.2 Is it known when these products have to be produced

6.3.3 Is it known who has to authorise these products

6.3.4 Do reports in the development organization tend to reflect the actual situation

6.4 Dependencies

6.4.1 Is project progress depending on another project

6.4.2 If so, is this other project executed according to plan

6.4.3 Is the other project risky

6.4.4 Does the project depend on other parties, not involved in the project

6.4.5 Are these other parties sufficiently motivated in order to contribute to the project

6.4.6 How long is the waiting time for external authorization, for instance the inter phase time required by a steering committee at the end of a developing phase

7. DEVELOPERS

7.1 Experience with systems development

7.1.1 How much experience has the project team with IT development projects

7.1.2 How experienced is the project leader with this type of system (size, duration, complexity)

7.2 Experience with subject matter

7.2.1 Is sufficient domain knowledge available in the project team

7.2.2 Is it easy to obtain additional domain knowledge

7.3 Staff availability

7.3.1 Is a capacity plan available for systems development (who does what and when and for how long)

7.3.2 What percentage of the system is built by externals

7.3.3 How many people are involved in the development for more than 50% of their time

7.3.4 Have agreements been made concerning the availability of these people

7.3.5 What is the probability that the continuity of the project is endangered by staff turnover

## 8. MEANS

8.1 Hardware

8.1.1 Does systems development require hardware that is new/unknown to the developers

8.1.2 How experienced are the developers with the required hardware

8.2 Software

8.2.1 Do the developers have standard development tools available

8.2.2 Will the system be developed with tools (generators)

8.2.3 Are specific/new developments tools required for systems development

8.2.4 Will standard software be used

8.2.5 How experienced are the developers with the required development tools

8.3 Techniques

8.3.1 Do the developers have standard development techniques available

8.3.2 Will the system be developed with a development technique

8.3.3 Is it possible to develop the system with the available techniques

8.3.4 How experienced are the developers with the required development techniques

8.4 Reuse

8.4.1 To what extent will reuse be used

## Dealing with risk

8.4.2 Do you know/guarantee the quality of the reused parts

8.5 Suppliers

8.5.1 How experienced are you with the supplier(s); this means; is it the first time you have worked with this supplier or have you had a longer relation with the supplier

8.5.2 To what extent is the supplier familiar with your organization

8.5.3 With how many suppliers are you dealing

8.5.4 How reliable is the supplier in delivering in time and quality

## 9. SYSTEMS MANAGEMENT

9.1 User support

9.1.1 Are staff and means available for training during introduction and use of the system

9.1.2 Are staff and means available for user support (for instance a help desk)

9.1.3 Are staff and means available for maintaining the technical infrastructure the system is depending on

## 9.2 Maintenance

9.2.1 Are staff and means available for adapting the system to changes in user requirements in the years to come

9.2.2 How fast will user requirements change

9.3 Data input

9.3.1 Are staff and means available for data input

9.3.2 How much effort is required for conversion and data input during the implementation of the system

9.3.3 How much effort is required for update of data during the first year of system use

9.3.4 How reliable are these data

## Appendix B: Case descriptions

## Project A: implementation of a staff information system

## Short description

The project was a study, aimed at preparing the implementation of a single staff information system where up until then a number of systems had been in use. This was seen as a very sensitive project, given the differences in culture between the departments. The result aimed for was a go-no-go decision by the senior management, together with the acceptance of this decision by the main parties involved.

## Evaluation

The most important value added aspect of implementing risk analysis during this project was that a support platform was created for this politically very sensitive project. All parties involved participated in the project. Representatives were of a very senior level and the risk management approach, together with the measures taken in consequence, convinced a number of them to lend more active support to the project. Critics of the project were able to voice their criticism, first in an informal setting, and later during the group session. The session provided all with an opportunity to identify and solve differences of opinion and reconcile vested interests. For a number of remaining potential problems counter measures were identified. These proved successful and the implementation has in the mean time taken place with the approval of all parties involved. The project manager was very pleased with the material (the interview reports), which he described as ‘a gold mine of information’. The checklist used, a slightly modified version of the one found in Appendix A, was seen as valuable. Only a single risk was mentioned which could not be derived from the list.

## Project B: Certification Monitoring Station

## Short description

The project Certification Monitoring Stations (CMS) was aimed at designing the specifications for a motor-way monitoring station. These stations allow the monitoring of traffic and aid in managing the flow of traffic. According to EC regulations substantial contracts, such as the one for producing these stations, have to be submitted to an open tender. This requires the existence of a set of high quality specifications, all the more since road monitoring stations are complex systems which will have to be highly reliable while working under extreme conditions (e.g. extremes in temperature and humidity).

## Evaluation

The project had been under way for some time when the risk management procedure started. Use of the method encouraged the involved parties to communicate directly. This led to the identification of a number of risks with the potential of terminating the project. All involved parties found the exercise to be very helpful.

## Project C: Highway Information System

## Short description

The project Highway Information System was aimed at developing the basic architecture within which all future development of information systems linked to main road management will have to function. At the same time the project was aimed at upgrading existing facilities.

## Evaluation

Risk analysis clearly showed that this project was in trouble. The long term goals of the project were generally accepted by all parties involved. However, it was found that the demands placed on people by the short term goals were incompatible with the demands put on them by the long term goals. The long term solution required that the technical basis of the system would have to be designed very carefully. The short term upgrade required that a decision, any decision, would have to be taken immediately. Partly due to heavy political pressure these problems were either not sufficiently recognized, or had been set aside. Application of the risk management method brought it all out in the open. The risks were discussed openly by all parties involved, which in the end led to a cancellation of the project. The goals were not abandoned, but it was decided to untie the long term from the short term goals and to set up a series of new projects aimed at fulfilling them.

## Project D: Traffic Management Systems

## Short description

The project was aimed at enhancing a current traffic management system, which no longer fulfils the user requirements. In communication with the user community a set of basic requirements has been agreed which were used to start this project.

## Evaluation

When applying the risk management method it was found that the level of risk attached to this project was relatively high. The main problems were caused by the relations this project had with other projects that were being developed concurrently. One of these projects was aimed at developing a network standard for roadside use and another was project B, the road monitoring system. Design choices in all three projects were influencing the other projects. The matter came up time and again, with new counter measures being taken at each new meeting. The risk management meeting thus proved effective as a forum both for identifying and rectifying the risks associated with the project. Especially in this case such a forum, with participants from affected parties from outside the project, was very effective in solving the problems.

## Project E: Geographical River Information System

## Short description

The project Geographical River Information System was aimed at providing more insight into the costs and benefits associated with introducing geographical information systems (GIS) on a wider scale. To this effect a small section of a river was mapped, and a series of GIS-applications based on this map were developed.

## Evaluation

During the risk management meetings a fundamental disagreement as to the goals of the project became apparent. Also it was found that several problems existed with project planning and systems requirements definitions. If unsolved, these would lead to a nice GIS-based system without the intended benefit: more insight into the costs and benefits of GIS. The sequence of meetings succeeded in focusing sufficient attention on these problems. This resulted in a timely shift in focus and enabled the completion of a well documented report on potential costs and benefits of GIS-based systems for the organization.

## Biographical notes

Fred J. Heemstra is a professor in Industrial Engineering and Informatics and Dean of the Department of Economics, Business and Public administration at the Open University. He received his Masters in Industrial Engineering and his Ph.D (on the subject of Software Cost Estimation) both at Eindhoven University of Technology.

Areas of research interest are Software Cost Estimation, Cost Benefits of IT projects, Quality Management, Risk Management.

Rob J. Kusters is an assistant professor at Eindhoven University of Technology, Department of Technology Management, Information & Technology Section. He received his Masters in Business Econometrics at Tilburg University and his Ph.D at Eindhoven University (admission planning in general hospitals). Areas of research interest are Software Cost Estimation, Cost Benefits of IT projects, Quality Management, Risk Management and Work-flow Management.

Address for correspondence: F.J. Heemstra, Department of Economics, Business and Public Administration, Open University, P.O. Box 2960, 6401 DL Heerlen, The Netherlands.
