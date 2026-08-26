---
otero_id: 26930
otero_key: "UXC63BMT"
title: "Corporate Electronic Mail — A Communication-Intensive Application of Information Technology"
authors: "A.B. Crawford"
year: "1982"
journal: "MIS Quarterly"
doi: "10.2307/248652"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Corporate Electronic Mail - A Communication-Intensive Application of Information Technology Author(s): A. B. Crawford, Jr.

Source: MIS Quarterly, Vol. 6, No. 3 (Sep., 1982), pp. 1-13

Published by: Management Information Systems Research Center, University of Minnesota

Stable URL: http://www.jstor.org/stable/248652

Accessed: 27-10-2015 17:30 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# Corporate Electronic Mail — A Communication- Intensive Application of Information Technology

By: A.B. Crawford, Jr.

## Abstract

Extending the ARPANET technology of an asynchronous, packet-switched “electronic mailbox,” the Corporate Information Systems department introduced a pilot mail service within Digital Equipment Corporation which has now grown into a full-fledged production system with some 6,000 users — and is still growing. The architecture for the Electronic Mail System (EMS) is based on a multinode network of dedicated minicomputers. Technical, administrative and human factors, and cost considerations were recorded throughout the pilot and production period. Lessons learned have highlighted the need for better network engineering, capacity planning, and operational policies/procedures. User surveys were used to capture demographic data and reaffirmed the highly favorable impact on personal productivity and each manager’s effectiveness. Recommendations are offered on how to plan for a pilot and to assure a smooth transition to production service.

Keywords: EMS, electronic mail, office automation, office systems, telecommunications
ACM Categories: 2.9, 3.50, 3.70, 3.81

## Introduction

For Digital Equipment Corporation, a multinational Fortune 200 company, electronic mail has become an essential and highly effective interpersonal telecommunications medium. A pilot test launched in January 1978 led to approval of full scale production service in August 1979, and today we have over 6,000 active subscribers. It has become a foundation for the introduction of information technology into the office environment. It has also been an unanticipated learning experience for our Information Resource Managers in network management and distributed database administration.

The business problem being attacked is real and undoubtedly found in any organization which operates in multiple locations — be it government, industry, or academia. That problem is how to facilitate more timely and more cost-effective interpersonal communications. The telephone alternative is inefficient, particularly when the high percentage of incomplete calls is considered, and the typewritten memo is becoming increasingly costly as well as slow in reaching its destination via interoffice or external mail.

This article presents the highlights of lessons learned during the pilot and production implementation, distills the management/organizational impact of this communication-intensive application, and suggests proven approaches to those organizations that are considering the introduction of EMS into their applications portfolio.

It is assumed that the introduction of EMS will normally begin with a pilot stage. The article therefore emphasizes ways to ensure a successful pilot and a satisfactory transition to production service. Because there continues to be a high interest in relative cost savings of EMS, the preliminary results of a study still in progress are highlighted briefly.

## Primary Features of EMS

Our basic concept for the Electronic Mail System (EMS) was drawn from ARPANET — the pioneering packet-switching mail system sponsored by the Department of Defense's Advanced Research Project Agency. The fundamental personal electronic “mailbox” has been extended to include electronic “filing cabinet” features. (See Figure 1.) Additionally, tickler files and calendar keeping were added in the production version. A hard copy terminal was placed in the mailroom of major facilities to allow EMS subscribers the capability to direct mail to individuals within those facilities who were not EMS subscribers. Finally, to enhance the utility, off-net access was provided. In this manner, every location and every employee in the corporation can be reached via some form of message system, even if they are not subscribers on electronic mail. Messages can also be automatically refiled into commercial message systems such as TWX and TELEX.

![](/api/attachments/UXC63BMT/fulltext/images/286b4bcce5a8bdaa64cba289fde446e9480a263657bf404f421c28e40e94d95f.jpg)  
Figure 1. Electronic Mail at Digital — Primary Features

The pilot operation was hosted on a single PDP-11/70 node. Each node can handle up to 1,000 subscribers, with 750 being the preferred user load. Consistent with our strategic plan for supporting future office automation applications, our concept was to install dedicated mini-computer systems in selected facilities or clusters, tied together in a logical mail network through the Corporate Telecommunications backbone network. Expansion, therefore, was predicated on adding dedicated PDP-11/70 and VAX nodes in selected employee population centers [7].

## The Pilot Phase

## Scope and purpose

The technology behind EMS was not new, but making it part of the office routine certainly was new at that time. We in the Corporate information management function decided, therefore, to conduct an extensive controlled pilot to test its acceptance and to serve as a precursor to subsequent automated office tools $[2]$ . The goals of the pilot were to:

1. Gain experience with this new communications-intensive application.

2. Assess the organizational/behavioral implications of a computer based office system.

3. Gather hard data on the costs of ownership.

4. Determine the desired design features and architecture of a large EMS application.

The pilot was launched with approximately forty subscribers. Additional subscribers from across the U.S., Canada, and Europe were soon added under controlled conditions to investigate capacity limits, systems performance, and economic factors of wide-scale use. Pilot operations were conducted for about eighteen months. The last six months were devoted to data analysis, report preparation, and presentation of the findings to top management for decision. The user population was selected to include senior executives, managers, engineers, technicians, individual contributors, and administrative personnel. We purposely included employees with technical backgrounds, as well as those who had never before used a computer terminal to observe the reactions of the various categories of user to this new office tool.

## Pilot results

We met the goals of the pilot, gathered statistics, and organized the operating and support costs. After summarizing our findings regarding the technical design and suitability of the mail service, we prioritized our recommended enhancements. User surveys and human engineering experiments produced comprehensive behavioral and ergonomic conclusions [4].

Despite the diversity of user types and backgrounds, the test group's reaction was almost universally favorable. User demand for additional subscriber allocations and system capacity began to bear on the deliberate pace with which we were approaching production.

In general, the users were impressed by the speed and the effectiveness of non-simultaneous communication. They confirmed its effectiveness for broadcasting information, disseminating and following up on task assignments, communicating status reports, and handling short question and answer requests.

In particular, managers felt that by using EMS they were able to accomplish tasks they could not otherwise have done. Of prime importance was the more timely information exchange and the ease in distributing information to multiple addressees across many locations.

They reported that EMS did facilitate keeping their staffs informed and generally allowed for wider communication than previously. For example, meeting minutes which previously were kept on file or sent to only a few people could now be forwarded electronically with a few keystrokes. Or a task assignment from headquarters could now be easily annotated with additional instructions as it was passed down to the next level. Some managers even suggested that the accessibility of more timely information enabled them to defuse some potential crisis situations. Finally, managers found that the online filing and retrieval capabilities allowed them to have more rapid access to information in their personal message file which meant they did not have to keep a lot of detail in their heads as had been the case.

Perhaps the most important reported impact of EMS was the individual user's perceived productivity. A majority of users reported that their personal productivity had been increased by 5-15%. Many also suggested that the increase would have been substantially higher if all of the people with whom they regularly communicated with were also EMS subscribers.

## Behavioral findings

Near the conclusion of the pilot Digital employed an external consultant to identify and analyze the behavioral implications of EMS [8]. The consultant's major conclusions were: the majority of users appeared to be highly satisfied with the service primarily because of its speed and non-simultaneous nature. Many users quickly became dependent upon the system for much of their daily business communications. Finally, it was found that no major negative impacts, i.e., crises or adverse changes in work or interpersonal relationships, resulted from the massive introduction of EMS. However, some lesser impacts were apparently caused by this new communication medium. Those implications grouped primarily into four interesting categories.

## Effects of EMS on Communication Patterns, Style, and Usage

The implications in this category tended to affect managers more than secretaries. At the outset, many managers felt that EMS messages were too sterile, formal and terse, or that the medium seemed to mandate an action or response. On the other hand, they acknowledged that EMS offered a powerful alternative mode of communication. Most managers reported that EMS increased the speed of their decision making because information collection and staff coordination was facilitated. It also allowed lower-level managers to communicate with managers at a higher level. It provided an alternative mode for messages that were less personal than telephone and yet more personal than a written office memo. Several managers believed that EMS was abused in some cases, or that some messages were inappropriate for this form of communication. Inappropriate use was defined as sending messages that were too long and sending a lengthy series of messages back and forth when a short meeting would have been far more efficient. Others were broadcasting messages to users for whom the information was not important, thereby resulting in an information overload for some individuals.

## Effects on Personal Productivity

The majority of users did feel EMS saved them time and, therefore, they could accomplish more useful work during normal business hours or have more time to do higher quality work. Secretaries estimated that EMS saved them an average of eight to ten hours per week, and managers estimated their saving to be about seven hours per week. (This confirmed the earlier user survey findings.)

## Effects on the Quality of Work Life

The impact of EMS on job satisfaction was found to be more significant for secretaries than for managers. Secretaries cited a decrease in menial, mundane tasks now delegated to EMS, and to the amount of time EMS saved. Examples included reduction of typing, reproducing, and addressing interoffice memos. The time saved could be used for more interesting, challenging work.

## Effects on Working Relationships

The effects in this category were primarily experienced by managers. One frequent observation was that the amount of face-to-face contact had been reduced. Many managers stated that it was a problem because it reduced the “interpersonal flavor of working.” Others said, however, that they liked some reduction in face-to-face contact because it saved them time.

The consultant added a footnote to her study that could be pertinent to other companies. She observed that the absence of adverse implications and the relatively early and high degree of satisfaction may be related to factors that are specific to the Digital work environment. Because Digital is in the computer industry, many Digital employees are professionally interested in new applications such as EMS, are willing to experiment, and are not particularly intimidated by information technologies. She also observed that users generally tried to solve in “real time” many of the concerns they initially confronted with EMS, apparently because of Digital’s norm for verbalizing such concerns openly and directly. She concluded, therefore, that the findings did not necessarily predict the behavioral implications of EMS in companies where interest in new technologies or confrontation of work life issues were not encouraged.

## Transition From Pilot to Production

Based on the overall success of the pilot, and in the face of a clamor from the user base to accelerate expansion of the EMS service, we prepared and presented a business plan to the Corporate Operations Committee [6]. As anticipated, it was difficult to verify hard cost savings, but we did prepare an estimate of the cost displacement in reducing the amount of telephone traffic and the number of interoffice memos. This cost displacement by itself did not produce a return on investment to economically justify the recommended production system. Our subjective user perceptions indicated that personal productivity was improved by EMS in the range of 5-15%. We did do the perfunctory calculation of translating that labor savings into a monetary equivalent and suggested that these could be considered soft savings — which of course could not be “dropped to the bottom line.”

We had purposely convinced several members of the Operations Committee and their secretaries to be a part of the pilot activity. Their own experience, therefore, helped to fill in for the lack of hard savings in justifying the transition. Somewhat on that basis, the Operations Committee accepted the recommendation to move into full production.\*

## Lessons Learned

## Multinode impacts

The expedient we employed at the outset of production to support multinode distributed operation was built around our administrative store-and-forward message switch which we call Record Communication System, or RCS. More nodes were brought online and as the volumes increased above forecasts one difficult problem was the severe saturation of the message switch in handling intermode traffic transfer. The first step to alleviate this bottleneck was to install a second RCS switch located in Geneva. (See Figure 2.) This offloaded the intra-European traffic from the Maynard switch and also significantly reduced line costs by keeping most of the European traffic within Europe. The next and longer term solution was to introduce a higher speed, higher capacity synchronous file switch to handle the growing U.S. traffic needs. (See Figure 3).

We learned the hard way that with multinode service we no longer had a simple mail system to manage, but an elaborate and ever-expanding telecommunications network. And unlike more conventional business data processing systems, we found that the user expectation was such that high availability was demanded — comparable to that of the telephone system.

The requirement to interface additional electronic mail and text handling systems within the company has added to the complexity of network planning and design. Integration of several different word processing systems was a high priority and did add substantially to the utility and richness of EMS in the office environment. Then, as the Corporate marketed mail product, hosted on the VAX rather than the PDP-11/70, came into field test, we were obliged to work out a gateway to interconnect with that particular mail system. Further, an additional gateway has been installed to reach several hundred software and hardware

![](/api/attachments/UXC63BMT/fulltext/images/3d2d96aca587a379aa2b0830bbb69934a78b1c958d3874c29b4ac6a908e72439.jpg)  
Figure 2. Phase I — Network

![](/api/attachments/UXC63BMT/fulltext/images/a7401fdd0f57629b7197e82dc147dedc24436d16b9da6d5ae093fe1c7c094983.jpg)  
Figure 3. Phase II — Network

engineers and engineering managers who had their own form of electronic mail on an extensive engineering software development network. This particular complication will undoubtedly be confined to high technology companies in the information industry.

I stress that any extensive multinode electronic mail system does require all aspects of data network engineering and management, in addition to management of a distributed application which in itself is non-trivial. Our expansion plans would have been more comprehensive had we understood the extent of dependency on telecommunications capacity and robustness.

## Organizational placement

This raises a significant strategic planning and organizational issue regarding office automation. Our Corporate Telecommunications Department took the initiative in sponsoring EMS, and they are now assigned management over Digital's internal office technology and systems program. The logic is that the critical factor in planning for introduction of technology in the office is information transfer, as compared with data processing or word processing. Followup on office systems projects has confirmed the validity of this organizational alliance within our overall Information Resource Management function at the Corporate level. Also drawing on our EMS experience, the program team is a multi-skilled group with engineers, telecommunication specialists, organizational development consultants, MIS professionals, and educators.

## User support/training

Several aspects of user support were found essential. First, a telephone hotline for users who have a specific question on system use is a good “first line of defense.” Second, self-help aids should be very simple and capable of being understood by the naive or non-technical user. Two-thirds of the subscriber base are managers and executives; they are not amenable to an extended formal training course — nor, for that matter, reading detailed instructional manuals. Third, some short formal courses are useful to cover administrative users. At the same time, a tailored “tutoring” course for the very senior users is recommended. Finally, refresher training or short “guidelines” newsletters can increase the learning curve of those users who have been on the system for a while but have not yet used its full capabilities.

We have now found it effective to delegate ongoing user training to our internal departments which provide routine educational support on office/administrative subjects. This enhances the concept that EMS is not a mysterious, high technology application, but is as commonplace as typewriters and telephones and copiers in the office.

## Distributed database — a surprise

Again, our pilot experience with a single node did not prepare us for the complexities of administering the Corporate EMS Directory across a multinode network. In fact, the Directory became one form of a truly distributed database with all of the implications of database synchronization and control. Subscribers are permitted to change their own directory data fields and to add or change distribution lists within certain limits. Change transactions must pass through their nodes and on to the Corporate Directory node. There the online “Postmaster” utility updates the master database and promulgates the changes back out to all other nodes for updating the local directories. This too is a non-trivial task! And it creates a significant amount of network traffic flowing across the switch!

This sophisticated directory service is highly regarded by the users. It allows users to address both individuals and predefined distribution lists by name, irrespective of node location. In essence, the network is thereby transparent to the users. As the service is extended to more and more of the Corporate population, however, we must assess other alternatives to this full-service directory. It may be that size and operating cost will exceed a reasonable limit, and some form of addressing placed back on the message originating user.

## Service challenges

We learned that the pilot users must be reminded continually of the prototype nature of this service and that some inconveniences should be expected. In a sense, expectations can be bounded during the pilot period $[5]$ . This will not be possible once production services have been introduced. In fact, a major challenge of the transition is to reset expectations of the providers of the EMS service as well as the receivers. Production will certainly entail an expansion of service, delivery to many more subscribers, and possible early incorporation of a multinode network. By the end of the pilot the operations staff must either be performing at a production level quality or should have well-defined action plans to raise service levels to provide sustained production quality service. For this reason, implementation should not be rushed into production before quality service levels can be guaranteed.

In planning for production, it is important to realize that usage patterns observed during the pilot may be misleading. Because expectations are bounded during the pilot, users will not depend on the system as heavily as they will during production. The transition to production undoubtedly will reflect increased usage. Capacity plans for production must take this probable increase into account, to include estimating the number of users who can be supported on the system, communications ports, and disk storage. Further, usage increases actually may not appear until after the first two or three months of production service. Expansion of the user base should be handled carefully to avoid overload.

We learned some fundamental lessons of communications traffic engineering: (1) as users are added, connect time by each individual user increases; (2) as connect time increases, fewer users can be adequately supported by each node; and (3) as users are added, the demand for still more users increases [3].

I cannot emphasize too strongly the importance of planning for an adequate service level. The system became an essential component of the users' work habits even before we were out of the pilot stage. We severely underestimated the capacity constraints in several dimensions and brought on too many new users too early. The result for a period of several months was high frustration for all users because of poor response time, undue internode message delays, and even worse, low probability of access to the system during prime time. The popularity of the new tool almost became its downfall!

## Policies to Facilitate Transition

munities of interest," rather than expect the system manager to attempt to allocate individual slot allocations. Blocks of accounts should be allocated only to groups with a demonstrated business need for the capability. The allocation policy should also deal with the treatment of EMS subscribers who move from one organization to another.

The following guidelines were published to help prioritize EMS allocations:

The transition from pilot to production is not a serious technical challenge. The more important and difficult tasks have to do with the establishment of management plans and administrative policies appropriate to sustained production. The following three policy areas are important.

## Allocation of EMS user accounts

\- The employee should have a need to send at least five interoffice memos per day.

\- They should have a need to communicate frequently across time zones.

\- They should have a need to communicate rapidly on a frequent basis to geographically dispersed Digital locations.

\- They should have a need to coordinate and keep current on project information, especially involving work on different shifts.

\- They should have a need to communicate with staffs or managers who are continually traveling and difficult to reach via telephone.

As indicated earlier, our experience is that the demand for electronic mail grows much more rapidly than can be satisfied. Unless clearly defined allocation policies are put in place, the demand will lead to frustration, political wrangling, and other business inefficiencies. I suggest that blocks of EMS accounts be assigned to “com-

## Records management

A records management policy must also be established before moving into production. EMS offers powerful electronic filing, search, and retrieval capabilities. Because of the search capability, there may be a tendency to retain the more-or-less informal EMS memos that would have been thrown out rather than filed manually had they been written on paper. As a result, the mass storage capabilities of the system can become swamped rather quickly. Rules should also be stated whereby the System/Node Managers can purge or archive messages beyond a stipulated age. During the pilot this is not likely to be a problem. Insofar as possible, the records management policies for EMS should be consistent with corporate record retention policies for other files.

## Terminated accounts

It is essential to have a clear policy for the removal of EMS users from the system. The most obvious case is that of a terminated employee. A procedure should be established whereby the EMS Account Coordinator becomes immediately informed of any subscribers who leave the organization so that they can be denied further access to the system for obvious security reasons. Similarly, a policy must also be established for the disposition of the files of people so removed. This policy might be developed to parallel those policies that already exist in the organization for the recovery of assets, including files, from terminated employees.

## Demographics and Cost Considerations

As a form of post-implementation audit, an extensive user survey was undertaken recently to capture a profile of the user base, how they were using this system, and what we might infer in the way of incremental cost savings [1].

## Profile and terminal use

As we have continued to expand the user base, the percentage of managers/executives has continued to increase. Reflected in Figure 4 is the current profile, in which we find 63% managers, 23% individual contributors, and 14% secretarial/administrative users on the system. As for access style, 62% of the users interact directly with their EMS terminal. The remaining 38% rely on their secretary or administrative support person to provide their messages in hard copy and in turn transcribe all input messages for them. (This may be misleading in that a substantial number of the executives do access the system directly when they are away from the office or when their secretary is doing other things.)

Two-thirds of the EMS terminals are shared among users. Only one-fourth of the terminals are dedicated to EMS as opposed to also serving as an input/output device for other interactive business applications. (See Figure 5). And we did confirm that 42% of the users have a second terminal at home, primarily for EMS. As a rule of thumb, we assume one new terminal must be acquired for every three new subscribers added to the directory.

![](/api/attachments/UXC63BMT/fulltext/images/f87c831c065a7e809c6d22aa1fa3485b16dc96713f3ae77be45672845fc2a332.jpg)  
Figure 4. EMS User Profile

## Costs/benefits

In the difficult and obviously nebulous area of quantifying benefits of EMS, we reached the unsurprising conclusion that the interoffice memo simply does not compete with EMS. Nor was it surprising to learn that the cost of a single telephone call was lower than the preparation and transmission of a single EMS message. The break-even was found to be one additional phone call or one additional copy or addressee. For any additional copies or addressees beyond the second, EMS is significantly less costly than either the interoffice memo or the telephone call, even if the manager relied on an administrative support person to do EMS work. Table 1 and Table 2 summarize the cost components which support that conclusion. Table 3 then annualizes those unit costs based on actual yearly volumes, factored by the users' estimate of how they would handle their mail if EMS were not available. The resultant marginal cost savings for EMS used by a manager are thereby estimated to be \$2.7 million. If that manager relies on an intermediary, then the marginal cost savings would be \$1.5 million.

That amount of cost savings does not totally displace the full ownership costs for this system. The “value-added” features and productivity gains continue, in the view of our users and corporate management, to be the overriding justification for further EMS expansion and penetration of the company.

We had already established through pilot experience that “telephone tag” would be decreased significantly and that interoffice memos would also decrease. As a surprise in this most recent survey, we learned from the user responses that the number of meetings scheduled by many of the users has decreased slightly. (This was not indicated during the pilot.) However, everything has its price. We also learned that some 60% of the users did feel that their junk mail had increased somewhat.

![](/api/attachments/UXC63BMT/fulltext/images/38d57ab5e0dcc516b2a828673fde6d2be240565b1546cd085ee190ff59e93886.jpg)  
Figure 5. Use of EMS Terminal

Table 1. EMS Cost Analysis
Cost Components
Original Copy

<table><tr><td></td><td>Interoffice Memo</td><td>Phone Call</td><td>RCS Message</td><td>EMS Memo Orig: Mgr</td><td>EMS Memo Orig: Intrm</td></tr><tr><td>Originator (Labor)</td><td>$2.88</td><td>$1.80</td><td>$2.88</td><td>$2.16</td><td>$2.88</td></tr><tr><td>Secy/Operator (Labor)</td><td>$3.42</td><td>—</td><td>.92</td><td>—</td><td>1.08</td></tr><tr><td>Non-Productive</td><td>.25</td><td>1.23</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Materials/Mail</td><td>.61</td><td>—</td><td>.41</td><td>—</td><td>—</td></tr><tr><td>Communication</td><td>—</td><td>.82</td><td>.71</td><td>.27</td><td>.27</td></tr><tr><td>System</td><td>—</td><td>—</td><td>.19</td><td>.83</td><td>.83</td></tr><tr><td>Peripheral: Equipment</td><td>.44</td><td>.46</td><td>.10</td><td>.14</td><td>.14</td></tr><tr><td>Communication</td><td>—</td><td>—</td><td>.33</td><td>.83</td><td>.83</td></tr><tr><td>Access Factor</td><td></td><td></td><td></td><td>90%</td><td>90%</td></tr><tr><td>Total Unit Cost</td><td>$7.60</td><td>$4.31</td><td>$5.54</td><td>$4.70</td><td>$6.70</td></tr></table>

Table 2. EMS Cost Analysis

Cost Components for Additional Copies

<table><tr><td></td><td>Interoffice Memo</td><td>Phone Call</td><td>RCS Message</td><td>EMS Memo Orig: Mgr</td><td>EMS Memo Orig: Intrm</td></tr><tr><td>Originator (Labor)</td><td>—</td><td>$1.80</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Secy/Operator (Labor)</td><td>.90</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Non-Productive</td><td>.05</td><td>1.23</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Materials/Mail</td><td>.61</td><td>—</td><td>.41</td><td>—</td><td>—</td></tr><tr><td>Communication</td><td>—</td><td>.82</td><td>.71</td><td>.27</td><td>.27</td></tr><tr><td>System</td><td>—</td><td>—</td><td>.19</td><td>.83</td><td>.83</td></tr><tr><td>Peripheral: Equipment</td><td>—</td><td>.46</td><td>.10</td><td>.14</td><td>.14</td></tr><tr><td>Communication</td><td>—</td><td>—</td><td>—</td><td>—</td><td>—</td></tr><tr><td>Total Unit Cost</td><td>$1.56</td><td>$4.31</td><td>$1.41</td><td>$1.24</td><td>$1.24</td></tr></table>

Table 3. EMS Cost Analysis
Cost Savings

<table><tr><td colspan="4">Annualized EMS Deliveries</td></tr><tr><td colspan="2">Originals</td><td colspan="2">788.4K</td></tr><tr><td colspan="2">Copies</td><td colspan="2">1,768.7K</td></tr><tr><td colspan="4">Overall System Statistics:</td></tr><tr><td colspan="2">If handled via:</td><td>Marginal CostEMS: Mgr</td><td>Marginal CostEMS: Intermediary</td></tr><tr><td colspan="2">Interoffice Memo</td><td>$2,852.4K</td><td>$1,275.6K</td></tr><tr><td colspan="2">Phone Call</td><td>$5,122.4K</td><td>$3,545.6K</td></tr><tr><td colspan="2">RCS Message</td><td>$963.0K</td><td>$613.8K*</td></tr><tr><td colspan="4">User Perceptions:</td></tr><tr><td>Percent</td><td></td><td rowspan="2">Marginal CostEMS: Mgr</td><td rowspan="2">Marginal CostEMS: Intermediary</td></tr><tr><td>Handled</td><td>Via:</td></tr><tr><td>37.6%</td><td>Interoffice Memo</td><td>$1,072.5K</td><td>$479.6K</td></tr><tr><td>29.1%</td><td>Phone Call</td><td>$1,490.6K</td><td>$1,031.8K</td></tr><tr><td>14.2%</td><td>RCS Message</td><td>$136.7K</td><td>$87.2K*</td></tr><tr><td>Total</td><td></td><td>$2,699.8K</td><td>$1,424.2K</td></tr></table>

• From the study it is shown that when an intermediary (secretary) initiates an EMS message it is more expensive than sending an RCS message.

## Future Direction and Significant Issues

Continuing expansion of the user base is a priority. I indicated earlier, that we need to identify alternatives to the master, and distributed, directory approach. One alternative that looks reasonable is to design the local node to maintain limited directories for those individuals often addressed by the users on that node. This looks attractive because it lends itself to subsequent implementation on the professional workstation (personal computer) which we expect to bring onto EMS within the next year.

Other significant issues facing our EMS and office systems planners include enhancement to the system security, purging and non-electronic archiving, and the introduction of store-and-forward voice mail and image (facsimile) traffic. Plans are in process to integrate EMS with the other office applications and tools, such as graphics capability, Visicalc-type spread sheet calculators, and other document handling or text management systems. Also, preliminary plans are pointed toward pilot extension of EMS to select vendors and customers.

## Conclusion

By all measures Digital's Electronic Mail System has been judged a success — not merely by its sponsors, but by its users and by senior management. This can perhaps be best summed up by recent statements of two officers in the company. Ed Kramer, Digital's Vice President for U.S Sales, stated, "The goals of the U.S. Sales organization include increasing the level of customer satisfaction along with increasing our own internal productivity. One of the key tools in allowing us to do this is the ability to communicate rapidly and simply. We can accomplish this communication via the use of our electronic mail system." And Ken Olsen, President of Digital, recently stated, "We are so used to electronic mail, and we have become so dependent upon it, that I have forgotten what life was like without it. Being able to immediately send and receive messages to approximately 6,000 stations around the world is so efficient that we now can't conceive of life without electronic mail."

We have established a solid basis for our continuing initiative to enhance internal office productivity through information technology. And the credibility and image of our information management function has been enhanced by the leadership we took with EMS.

## References

[1] Abramson, N.F. "Preliminary Report, Electronic Mail System Financial Analysis," Corporate Telecom & Office Systems, Digital Equipment Corporation, Maynard, Massachusetts, April 15, 1982.

[2] Cooper, C.A., Jones, P.C., and Messier, C.V. "Report on the Results of the EMS Pilot Project," Corporate Message Services, Digital Equipment Corporation, Maynard, Massachusetts, January 1979.

[3] Copp, M.L. "Plan a Pilot Study for Electronic Mail System," The Office, Volume 95, Number 4, April 1982, pp. 112-124.

[4] Hersh, H.M. “EMS/VMS Learning Analysis,” Corporate Research Group,

Digital Equipment Corporation, Maynard, Massachusetts, July 31, 1981.

[5] Mayers, K. "DECMail Pilot Handbook," Corporate Telecomm & Office Systems, Digital Equipment Corporation, Maynard, Massachusetts, March 1982.

[6] Messier, C.V. "Program Plan for Internal use of Electronic Mail," Digital Equipment Corporation, Maynard, Massachusetts, June 1979.

[7] Messier, C.V. “Electronic Mail System Phase II Expansion Project Plan,” Office Systems Program, Digital Equipment Corporation, Maynard, Massachusetts, September 4, 1981.

[8] Wilkerson, W.S. "A Study of the Behavioral Implications of the COMET Electronic Mail System at the Digital Equipment Corporation," Maynard, Massachusetts, July 1979.

## About the Author

Albert B. Crawford, Jr. is the corporate functional manager of all internal management information processing, telecommunications services, and office systems in support of company operations, control and planning for Digital Equipment Corporation. The Digital Information Systems (DIS) function is responsible for policies, standards, strategic direction, and Long Range Planning of internal information resource management, for corporate network architecture and development, for coordinating career planning for MIS skills and disciplines, and for accounting to senior corporate management for the overall effectiveness of the function.

Prior to Digital, he held progressively more responsible positions with the U.S. Army in communications, research and development, automated command and control, and general electronics systems management. He holds a Bachelor's Degree in Military Science from West Point and Masters Degrees in Electrical Engineering and in Industrial Engineering from Stanford University.
