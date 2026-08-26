---
otero_id: 24932
otero_key: "7HD2WAGK"
title: "Supporting Inspections with an Electronic Meeting System"
authors: "Michiel Van Genuchten; Wieger Cornelissen; Cor Van Dijk"
year: "1997"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1997.11518179"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Supporting Inspections with an Electronic Meeting System

Michiel Van Genuchten, Wieger Cornelissen & Cor Van Dijk

To cite this article: Michiel Van Genuchten, Wieger Cornelissen & Cor Van Dijk (1997) Supporting Inspections with an Electronic Meeting System, Journal of Management Information Systems, 14:3, 165-178, DOI: 10.1080/07421222.1997.11518179

To link to this article: http://dx.doi.org/10.1080/07421222.1997.11518179

![](/api/attachments/7HD2WAGK/fulltext/images/8f9ef4ff7d554651d8b6c04035c11f9f85fb4e7c48a3f4dc45911f2aeca56b8a.jpg)

Published online: 08 Dec 2015.

![](/api/attachments/7HD2WAGK/fulltext/images/27f6bfff03f7c9ac0281d0d08102b9976f66e9ea2a107be231ce8e0e04299147.jpg)

Submit your article to this journal ↗

![](/api/attachments/7HD2WAGK/fulltext/images/4e0fd0b9dbd001f5d0c334ae11acaa977625719054148fe75a5519c6d770f656.jpg)

View related articles ↗

![](/api/attachments/7HD2WAGK/fulltext/images/80d4990d3bf9e37332d500cd7aca72436263dc9e8d90b29e70441822a14ab902.jpg)

Citing articles: 3 View citing articles ↗

# Supporting Inspections with an Electronic Meeting System

MICHIEL VAN GENUCHTEN, WIEGER CORNELISSEN, AND COR VAN DIJK

MICHIEL VAN GENUCHTEN is a partner of S&P Consulting and cofounder of Blenks Groupware. He was previously employed by Philips Electronics. He received an M.S. and a Ph.D. from the Eindhoven University of Technology, the Netherlands.

WIEGER CORNELISSEN is project manager of Philips Medical Systems. He was previously employed by Philips Industrial Electronics as software engineer and software manager. He received an M.S. in technical physics from the Eindhoven University of Technology, the Netherlands.

COR VAN DIJK is SPI (Software Process Improvement) manager for Baan Development. He was previously employed as software engineer and software manager.

ABSTRACT: Fagan inspections are a structured review of development documents that consists of individual preparation, a meeting, and rework by the author of the document. The meeting is used to log the defects found in preparation and to search for more defects. The effectiveness and efficiency of the meeting are typically low compared with those of preparation. This paper describes the use of an electronic meeting system (EMS) to support the logging meeting of a total of fourteen electronic inspections in Philips Medical Systems and Baan Company. The results indicate that the electronic logging meeting contributed much more to the overall result of the inspection than was the case in a traditional inspection. The results have implications for both software inspections and EMS. The implications for EMS discussed in this paper are opportunities for the use of EMS in routine meetings, increased use of meeting metrics, and the benefits of fixed-format input in an EMS.

KEY WORDS AND PHRASES: electronic meeting systems, software engineering, software inspections.

SOFTWARE ENGINEERING IS NOT KNOWN FOR ITS PREDICTABILITY and quality. One could argue that the software industry is a problem ahead and not a solution behind if it is compared with other disciplines. Constructing a high-quality, million-line program is a compelling task for a group of engineers. There is no question that software engineering needs to improve considerably and that it can use many methods and techniques originally developed in other disciplines.

Other disciplines, however, can also learn from the methods and techniques that software engineers devised to solve part of their problems. One example of such a technique is a Fagan inspection, which is a structured review aimed at detecting defects in development documents or code. The Fagan inspection has proven to be one of the most effective ways to improve software quality $[3, 5, 6, 11]$ . It consists of individual preparation, a meeting in which the defects are logged and the group searches for more defects, followed by reworking the defects by the author of the document. The effectiveness and efficiency of the logging meeting are typically low compared with those of the preparation. There is an ongoing discussion among software engineers and researchers $[10, 12]$ about whether an inspection needs a meeting.

One can also approach this from another angle: Can the meeting be improved to the extent that it can contribute to even more effective and efficient inspections? Improving meetings by the use of IT has been the main goal of researchers and practitioners working on electronic meeting systems (EMS) over the last twenty years $[8, 9]$ . This paper describes the use of an EMS to support the logging meeting of a total of fourteen electronic inspections in Philips Medical Systems and Baan Company.

## Inspections

AN INSPECTION AIMS TO DETECT THE DEFECTS IN DEVELOPMENT documents such as specifications, design, and code. Engineers around the world have carried out inspections for more than twenty years. Key characteristics of inspections are individual preparation, data collection, and a fixed syntax to report defects. The essence of inspections is given in figure 1. It shows the "LOW" documents that are to be inspected in a small piece of a functional requirements specification. The LOW documents are derived from the HIGH document, in this case a small piece of a commercial requirements specifications. The consistency between the high document and the low documents are to be inspected by means of the standard and checklist as provided to the inspectors.

Four documents are compared to look for defects. The high- and low-order documents are checked for mutual consistency and for consistency with the standard and the checklist. For example:

\- Standard 1 states that external interfaces should be specified in the low-order document. The LOW does not do this, so there is a defect.

\- Checklist 4 states that the response time should be quantified—another defect in the LOW document.

The Standard and Checklist represent the software process according to which the documents are to be produced. The Standard and Checklist both consist of only one page in order to make them usable in an inspection.

Well-executed inspections should be able to find 60 to 80 percent of the life-cycle defects before the software is tested. For example, in a project in which one of the authors was involved, 1,170 major defects were found in specification, design, and code inspections, while only 825 are found in the various tests [6]. Mature software groups spend 10 to 20 percent of their resources on inspections. More information on inspections and their results is available in numerous sources [3, 5].

<table><tr><td></td><td>HIGH1.1 Requirements- Information about end product: when produced; which components used- Product evaluation: collect, format manufacturing process over production batch or shift</td><td></td></tr><tr><td>STANDARD1 External interfaces should be specified.2 SRS should be according to IEEE 8303 Quality requirements should be specified</td><td></td><td>CHECKLIST3 Is the response time quantified?4 Is beta test defined?5 Can non-technician understand SRS?</td></tr><tr><td></td><td>LOWFour menu items for new reports must be added to the current menu structure. However, there are no positions available any more. The integration also requires adaptations to the user interface.</td><td></td></tr></table>

Figure 1. The Four Documents Used in an Inspection

Like any process, inspections can be improved. The focus of the effort described here has been to improve the effectiveness and efficiency of the logging meeting. A logging meeting has two purposes: consolidating the defects found by the inspectors into one list and looking for more defects during the logging meeting. The defects reported by the other inspectors function as a trigger to detect more defects.

During the logging meeting, the participants go through the document and state the defects out loud. The defects may have been found in preparation or during the logging meeting. The moderator leads the meeting and the scribe records all the defects. The logging meeting is key to an inspection. Experienced groups claim that they find many defects during the logging meeting.

The first and second goals of the logging meeting often turn out to be conflicting: Inspectors get distracted by the other inspectors stating a defect. The moderator is usually too busy to prevent discussion and control the logging rate. The logging meeting in an inspection was supported with an electronic meeting system (EMS) in an effort to overcome some of these problems.

## EMS Support for Inspections

THE ORIGINAL INSPECTION PROCESS WAS FOLLOWED in the electronic inspections. Instead of declaring defects out loud, the inspectors enter the defects into a networked computer. Defects appear on all participants' screens. As such, the defects can still function as a trigger for the other inspectors. At the first electronic inspection, all the inspectors came in with their defects written down on a piece of paper, as is usually the case in an inspection. It took considerable time to type in all the defects. From the second inspection on, the defects that were found in preparation were mailed in beforehand and consolidated into a single list before the logging meeting started. The list was imported into the meeting system so that the only keyboarding required was for defects found during the meeting. During the first meeting, it also became clear that the author wanted an explanation for some of the defects reported. It was decided to allow a short electronic discussion between the author and one inspector. The discussion could only be provoked by the author and was not allowed to involve more than four comments. The advantage is that the discussion does not distract the others while they can see the result if they want to.

The EMS used was GroupSystems [8, 9]. The tool used was “categorizer.” This tool is often applied in structured brainstorms. It helps build a group list of remarks by individuals in the group and sorts the ideas into different categories. The categories were used to list the defects found on separate pages. This expands the overview of defects for inspectors, which should help them find new defects.

One characteristic of an electronic inspection is the silence in the meeting room. This may be new for software engineers in inspections but it is common during parts of many electronic meetings. Another characteristic is that it is not necessary for all inspectors to be at the same paragraph while inspecting. Some inspectors may go ahead or stay behind. One can read what the others have reported at any time. This is again well known from all kind of electronic meetings: People can do different things at the same time and still contribute to the success of the meeting.

Electronic support for inspections has been applied in Philips Medical Systems and Baan Development. While both companies have considerable experience with inspections and the electronic inspections in both companies were almost identical, we have chosen to stay on the safe side and present the results separately because of major differences in the software under development, the nature of the documents under inspection, and the fairly limited number of electronic inspections undertaken.

## Case 1: EMS-Supported Inspections in Philips Medical Systems

## Characteristics

PHILIPS IS ONE OF THE WORLD MARKET LEADERS in providing medical electronic equipment such as x-ray and magnetic resonance scanners. The amount of software in medical systems varies from 100,000 lines of code to multimillion-line programs.

Seven electronic inspections were executed. The documents inspected were specification, design, and code. The size of the inspected documents was around ten pages and the number of inspectors was four (including the author) on average. The inspectors had, on average, participated in six inspections (ranging from zero to twenty) before they joined the electronic inspections. The engineers had an average of nine years of experience (ranging from 0.5 to 14 years).

## Results

The results of inspections are often measured in terms of effectiveness, efficiency, and yield.

\- Effectiveness is the number of defects found per inspected page. A distinction is made between preparation effectiveness and meeting effectiveness. Preparation effectiveness is calculated as the number of defects found per page in preparation, whereas meeting effectiveness is the number of defects found per page during the meeting.

\- Efficiency is the number of defects found per person hour invested in the inspection [5]. Again, the preparation and meeting efficiency are distinguished. The preparation and meeting hours are calculated. The rework hours are not calculated.

\- Yield is the percentage of defects found during the inspection versus the percentage that slipped through and was detected during later inspections, in test or in the field [7]. It was not possible to calculate the yield of the electronics inspections yet for several reasons; one is that the software that was inspected is not in the field yet. Another reason is that the software that was inspected was an add-on to a multimillion-line system. The calculation of the yield is not trivial. It is clear, however, that the yield is a very important performance indicator for inspections and future inspections should provide the metrics that will allow us to calculate the yield of our (electronic) inspections.

It is important to acknowledge that other factors than the electronic support also have an impact on the effectiveness and efficiency of the inspection. Such other factors include the type and quality of the document as well as the preparation time. The number of inspections and the number of factors involved do not allow us to calculate the relative contribution of these factors.

The four figures in which the results are presented compare preparation effectiveness and efficiency with meeting effectiveness and efficiency. Figure 2 shows the effectiveness if only major defects are counted. Majors are defined in all inspections as defects that would have resulted in a test or field defect if not detected during inspection.

The effectiveness of the EMS-supported inspections is considerably higher. The preparation effectiveness is also higher, despite the fact that the only change to the preparation process was the fact that a defect list had to be provided the day before the meeting. Metrics revealed that the preparation effort for the electronic inspections was higher than that for the traditional inspections. The fact that the engineers had to submit their defect list in advance apparently motivated them to put in more time. This was confirmed during the inspection evaluation.

![](/api/attachments/7HD2WAGK/fulltext/images/2e82c739819a1063402b4d921b510ca98b5bf4f59fd3ec5153ebe9ef44a270c6.jpg)  
Figure 2. Effectiveness (Majors Only)

The ratio of preparation to meeting effectiveness for traditional inspections is 13 and is 3 for EMS-supported inspections. This is remarkable given that the preparation takes place first and therefore typically catches the more obvious defects. The fact that the obvious defects have already been found is apparently compensated for to a large extent by the synergy of the group in the EMS-supported inspections. One of the goals of electronic meeting systems is to do work in meetings instead of between meetings. The ratios found here indicate that, for electronic inspections, the EMS are at least approaching that goal.

Figure 3 compares effectiveness if only minors are considered. In this study, hardly any minors were reported during the traditional logging meeting. This can be explained by the fact that engineers do not want to report too many minors in a traditional logging meeting because that may be perceived as splitting hairs. This is consistent with results found by Porter [10], who reported meeting losses in excess of meeting gains. In an electronic meeting, engineers are not restrained about reporting minors because they know that this will not distract the meeting.

Figure 4 shows efficiency limited to majors, while figure 5 shows efficiency with regard to minors.

The ratio between preparation and meeting efficiency for majors for traditional inspections is 9 while it is 2 for EMS-supported inspections. The ratio between the preparation and meeting efficiency for minors for traditional inspections is 13 while it is 3 for EMS-supported inspections.

## Participants' Opinions

The opinion of the participants was evaluated by means of a questionnaire at the end of each inspection and by soliciting comments on the electronic inspections. The questionnaire asked for opinions on eight statements on a five-point scale: strongly agree (5 points), agree (4), neutral (3), disagree (2), and strongly disagree (1). The statements are numbered 1 to 8:

![](/api/attachments/7HD2WAGK/fulltext/images/5faf21f52778e8f5f6fa140ce0423a12cfbc706da74d203552b854485d0d7a22.jpg)  
Figure 3. Effectiveness (Minors Only)

![](/api/attachments/7HD2WAGK/fulltext/images/deec15598a35e5b8fc6694edad6d76c1ddb2b95ae978bf5590873ae7482b0f86.jpg)  
Figure 4. Efficiency (Majors Only)

1. The computer-aided process is better than the manual process.

2. The computer-aided process helps the group concentrate on defect detection during the meeting.

3. The computer-aided process helps the group focus on major rather than minor defects.

4. The computer-aided process helps the group achieve its goals.

5. The group's problem-solving process was fair.

6. The group's problem-solving was efficient.

7. I am satisfied with the computer-aided process.

8. It is worth coming back.

Most of the statements are derived from a standard evaluation of electronic meetings.

![](/api/attachments/7HD2WAGK/fulltext/images/ed89c1ed78d43634227ad13cef4d82049fe21a7e93476d7adb5d630b5b00f9aa.jpg)  
Figure 5. Efficiency (Minors Only)

Statements 2 and 3 are specific to the electronic inspections. The opinions of over twenty participants in EMS-supported inspections are given in Table 1.

The opinion of the participants was favorable toward all but one statement. The participants disagreed with the statement that the electronic inspections helped them focus on major rather than minor defects. Apparently, EMS support alone is not sufficient. A combination of a scenario detection method $[10]$ with EMS support may help the inspection team focus on majors over minors.

The participants' qualitative evaluation revealed:

\- The meeting was considered less stressful than a traditional logging meeting. Both the authors of the document and the inspectors stated this.

\- Some inspectors still doubted the usefulness of the inspection meeting, despite data indicating the benefits. The evaluation of the inspection metrics by participants showed that their intuition did not match the metrics in all respects.

\- Several suggestions were made for improvements of the inspection process and electronic meeting system. One suggestion was to provide the author of the document with the combined defect list half a day before the meeting. This would allow him or her to study the defect list before the meeting, which would make him or her an even more effective inspector.

\- The experience with electronic inspections inspired one engineer to replicate some of the group support functionality on a workstation-based development platform. This prototype allowed participants to share comments made before the meeting and those generated within the meeting. The inspections were carried out in a room with enough workstations. The software group executed another seven inspections using this system. The inspections done on this platform were more effective and more efficient than the traditional inspections, but not as effective and efficient as the EMS-supported inspections.

Table 1. Opinions of the Participants at Philips

<table><tr><td>Percentage of responses</td><td>SA (5)</td><td>A (4)</td><td>N (3)</td><td>D (2)</td><td>SD (1)</td><td>Mean</td><td>N</td></tr><tr><td>1. Better</td><td>10</td><td>48</td><td>33</td><td>10</td><td>0</td><td>3.57</td><td>21</td></tr><tr><td>2. Concentrate</td><td>29</td><td>33</td><td>13</td><td>25</td><td>0</td><td>3.67</td><td>24</td></tr><tr><td>3. Major over minor</td><td>5</td><td>27</td><td>23</td><td>41</td><td>5</td><td>2.86</td><td>22</td></tr><tr><td>4. Achieve goals</td><td>0</td><td>65</td><td>30</td><td>4</td><td>0</td><td>3.61</td><td>23</td></tr><tr><td>5. Fair</td><td>8</td><td>67</td><td>21</td><td>4</td><td>0</td><td>3.79</td><td>24</td></tr><tr><td>6. Efficient</td><td>4</td><td>42</td><td>38</td><td>17</td><td>0</td><td>3.33</td><td>24</td></tr><tr><td>7. Satisfied</td><td>13</td><td>54</td><td>25</td><td>8</td><td>0</td><td>3.71</td><td>24</td></tr><tr><td>8. Worth coming back</td><td>17</td><td>70</td><td>13</td><td>0</td><td>0</td><td>4.04</td><td>23</td></tr></table>

## Case 2: EMS-Supported Inspections in Baan Development

## Characteristics of the Inspections

BAAN IS ONE OF THE WORLD MARKET LEADERS in enterprise resource planning software. Seven electronic inspections were performed; all involved inspections of source code that is part of a multimillion-software package. The inspectors had, on average, participated in thirty-three inspections (ranging from 5 to 100) before joining the electronic inspections. The engineers had an average of four years of experience (ranging from 0.25 to 22 years). Most engineers participated in one electronic inspection.

## Results

The results of the electronic inspections were compared with the results of another 100 traditional inspections of source code executed in the same development organization in the previous quarter. All inspections concerned were similar code inspections. The results are given in Table 2.

The following observations can be made:

\- The absolute number of defects—both majors and minors—found in the inspections increases considerably. The percentage found during the meeting does not change for majors but increases significantly for minors. In fact, in the traditional meetings, hardly any minors were found during the meeting.

\- The ratio between preparation and meeting efficiency for majors is 5 for both the traditional inspections and the EMS-supported inspections. The ratio between the preparation and meeting efficiency for minors is 25 for traditional inspections and 5 for EMS-supported inspections. The gains in this case are in catching more minors during the meeting.

Table 2. A Comparison of Traditional and Electronic Inspections

<table><tr><td></td><td>Traditional</td><td>EMS-supported</td></tr><tr><td>Number of inspections</td><td>100</td><td>7</td></tr><tr><td>Majors per inspection</td><td>1.5</td><td>3</td></tr><tr><td>Minors per inspection</td><td>21</td><td>57</td></tr><tr><td>Defects per inspection</td><td>22.5</td><td>60</td></tr><tr><td>Majors in meeting</td><td>0.25</td><td>0.57</td></tr><tr><td>Minors in meeting</td><td>0.75</td><td>8</td></tr><tr><td>Percentage of majors in meeting</td><td>17</td><td>17</td></tr><tr><td>Percentage of minors in meeting</td><td>4</td><td>16</td></tr><tr><td>Percentage of defects in meeting</td><td>5</td><td>16</td></tr><tr><td>Logging rate</td><td>36</td><td>60</td></tr></table>

\- The logging rate (defined as the number of defects reported per hour in the logging meeting) is considerably higher for the electronic inspections.

## Participants' Opinions

The opinions of the participants were evaluated by means of the same questionnaire, with the same eight questions, used at Philips Medical Systems. The results for Baan are in Table 3.

Baan participants' opinions are similar to those at Philips. A comparison of the results of these studies with earlier studies [8, 9] indicates a less favorable judgment of the electronic support. Possible explanations are discussed later.

## Implications for Inspections

THE FOLLOWING IMPLICATIONS FOR INSPECTIONS ARE FORESEEN:

\- More effective and efficient inspections process.

This is a significant improvement for the overall development process, given that inspections have proved to be the most effective way to detect defects. On top of that, mature software groups spend 10 to 20 percent of their time in inspections.

\- Defect lists available in electronic form.

The defect lists are available in electronic form. This facilitates the author's rework. This is also beneficial for the use of the data in later test or regulatory purposes.

\- Abandon sequential nature of preparation and logging.

Traditional inspections clearly distinguish individual preparation from the logging meeting. It may be possible to combine the two with the same or better results in an electronic meeting. The triggering of one inspector by defects found by one of his or her colleagues now only takes place during the logging meeting. It may work as well during preparation. Experimentation and analysis of the inspection metrics should tell the impact.

Table 3. Opinions of Participants at Baan

<table><tr><td>Percentage of responses</td><td>SA (5)</td><td>A (4)</td><td>N (3)</td><td>D (2)</td><td>SD (1)</td><td>Mean</td><td>N</td></tr><tr><td>1. Better</td><td>4</td><td>57</td><td>17</td><td>22</td><td>0</td><td>3.43</td><td>23</td></tr><tr><td>2. Concentrate</td><td>4</td><td>48</td><td>24</td><td>16</td><td>8</td><td>3.24</td><td>25</td></tr><tr><td>3. Major over minor</td><td>4</td><td>16</td><td>28</td><td>48</td><td>4</td><td>2.68</td><td>25</td></tr><tr><td>4. Achieve goals</td><td>9</td><td>52</td><td>26</td><td>9</td><td>4</td><td>3.52</td><td>23</td></tr><tr><td>5. Fair</td><td>5</td><td>57</td><td>24</td><td>14</td><td>0</td><td>3.52</td><td>21</td></tr><tr><td>6. Efficient</td><td>8</td><td>46</td><td>29</td><td>17</td><td>0</td><td>3.46</td><td>24</td></tr><tr><td>7. Satisfied</td><td>16</td><td>60</td><td>12</td><td>12</td><td>0</td><td>3.80</td><td>25</td></tr><tr><td>8. Worth to come back</td><td>25</td><td>46</td><td>21</td><td>8</td><td>0</td><td>3.88</td><td>24</td></tr></table>

## • Distributed inspections.

Distributed inspections are feasible. Experiences in electronic meetings have shown that it is not always necessary to be at the same time at the same place. This may also hold for electronic inspections. It may be very beneficial to to have engineers in different places to participate in an inspection. One of the companies involved intends to do distributed inspections with engineers from sites in Europe and India.

## Implications for EMS

## FIVE IMPLICATIONS FOR EMS ARE DISCUSSED.

## Support of Routine Meetings Imposes New Requirements on EMS

Inspections are a routine meeting in a mature software organization. Every engineer typically participates in more than one inspection a week. The fact that it is a routine meeting with a clear structure differentiates an inspection from the kind of meetings typically supported by an EMS. This imposes new requirements on the EMS and its use. Some examples:

\- An EMS meeting typically requires a facilitator to prepare and manage the EMS tools. After one electronic inspection, it became obvious that an EMS facilitator was superfluous: The participants knew what to do and the inspection moderator could easily handle the limited tasks that needed to be executed from the session leader's point of view. It is obvious too, by the way, that inspections cannot afford a specialized person to handle the EMS tools, given that inspections are a routine meeting of three to four persons. To allow one person to manage the tools would increase the overhead significantly. The use of the EMS in fact decreased the overhead in the case of inspections: The inspection moderator could spend more time looking for defects as an inspector because the EMS relieved him from some of his meeting manager's tasks.

\- Inspections are an integrated part of software development. EMS support should therefore also be integrated in the support environment for inspections. Engineers who are used to integrated environments do not tolerate manual input into an EMS before the inspections. An EMS cannot afford to be an island in itself when it intends to support routine meetings.

\- Performance requirements will be stricter in the case of routine meetings. This is true, for example, for reliability. It also has consequences for the preparation time of the tools for a meeting. For a one-day meeting, it may be tolerable that it takes one hour to prepare the tools. For an inspection, ten minutes to prepare the tools may be too much, given that there may be as many as twenty inspections per week.

## Benefits of EMS Support Are Less Obvious for Participants

The opinions of the participants were less favorable toward EMS support than those reported in previous studies $[8, 9]$ . We have three possible explanations for this.

\- Software engineers are very demanding users of information technology.

\- A manual inspection is already a very mature meeting with extensive preparation and a very clear structure. In other kinds of meetings, the introduction of EMS often brings improved preparation and structure to meetings, which is appreciated by the participants. In inspections, the participants do not experience this benefit because the preparation and structure were already there before the EMS support. In some cases, the contrary was true—for example, the output provided by the EMS was perceived as less clear than the handwritten forms used in manual inspections.

\- In some groups the use of an EMS may have revealed a deteriorated process. Inspections are executed according to strict rules. One example is the limited discussion allowed during inspection. In some groups rules such as these have been relaxed over the years. The use of an EMS reinforces the original rules and therefore tends to encounter some opposition. One group stopped using an EMS for inspections for this reason. The first priority was to put the inspection process back in place. The main contribution of the use of the EMS was that it revealed the deteriorated process.

## Encourage Use of Meeting Metrics in Other Areas

Inspections are the only meeting in the world, to our knowledge, that is managed in quantitative terms. It is interesting that so little measurement is applied to meetings, an activity that consumes vast amounts of resources. Why would “If you cannot measure it, you cannot manage it” not apply to business meetings?

It must be possible to exploit the benefits of metrics in other meetings as well. For example, household meetings could be planned and tracked based on metrics such as the number of action items generated and handled. The benefits are huge if one realizes the improvements in other disciplines after quantitative understanding was accumulated and put to use. One example is the manufacturing industry. A more recent example is the software industry, which is trying to get a grip on its problems by means of metrics.

Acceptance of metrics is often limited if they do not reinforce participants' perceptions. We have experienced this while introducing metrics into software $[1, 4]$ and we also encountered it in the experiment described here. Some of the groups were not convinced of the benefits of using electronic support, despite the metrics showing the difference. The use of metrics requires management maturity.

A next generation of EMS should provide more tools to plan and track meetings in quantitative terms. This should go much further than logging the number of comments per minute. It includes norms, analysis of deviations, and quantitative insight into optimal numbers of participants and amount of work to be done.

## Use Inspections as Guinea Pigs

Inspections could be a benchmark meeting to study the impact of independent variables such as remote meetings, multiple languages, or cultures on the results of electronic meetings. The impact of these variables can be measured and metrics can be compared. As such, inspections can serve as a guinea pig.

## Allow Fixed-Format Input in EMS

The input into most current EMS is free in format. An inspection is a structured meeting that could benefit from fixed-format input. For example, if one is sure that the second position always contains the defect code, it is possible to sort the defects during the meeting and use the insight gained in the current meeting. There are more meetings that could benefit from fixed-format input. Two examples:

1. When generating action items, it is useful to fix the format and ascertain that the first position always contains the person who will take the action and that the last will always indicate the estimated effort required to implement the action. This would allow the estimated total effort for one person to be calculated and the data could be used in the meeting while the rest of the work is being distributed.

2. Even brainstorms can benefit from fixed-format input. Experienced facilitators often fix the format by requiring a sentence to start with a verb (e.g., "increase the market share to 30 percent"). Enforcing such a format electronically does facilitate later sorting of ideas [13].

## Conclusions

BASED ON FOURTEEN EMS-SUPPORTED INSPECTIONS, we conclude that electronic support of the logging meeting can improve the effectiveness and efficiency of the inspections. This conclusion is based on the data collected and the opinions of the participants. This conclusion is confirmed by the fact that electronic inspections have now been implemented as part of the normal operation of some software engineering groups.

It is clear that more empirical data are required to further improve the electronic support of inspections. We will continue electronic inspections in industry and collect data as presented here as part of our industrial work. We encourage scientific studies of questions such as:

\- What is the quantitative effect on inspections that are distributed in time and/or place? What is the quantitative impact of inspections that are distributed over different time zones? What does this teach about other distributed meetings?

\- What will the effect be if the document to be inspected is presented electronically?

\- How can software tools as artificial inspectors contribute to the effectiveness of inspections?

We are convinced that many will benefit from these kinds of studies, in both the software engineering and EMS communities.

## REFERENCES

1. Cornelissen, W; Klaassen, A.; Matsinger, A.; and Van Wee, G. How to make intuitive testing more systematic. IEEE Software, 5 (September 1995), 87–89.

2. Dean D.L.; Orwig, R.E.; and Vogel, D.R. Facilitation methods to enable rapid development of high quality business process models. Proceedings of the 29th Annual Hawaiian Conference on System Sciences, 1996, pp. 472–481.

3. Fagan, M. Advances in software inspections. IEEE Transactions on Software Engineering, 7 (July 1986), 741–755.

4. Genuchten, M. van. Why is software late, an empirical study of reasons for delay in software development. IEEE Transactions on Software Engineering, 6 (July 1991), 582–590.

5. Gilb, T., and Graham, D. Software Inspections. Reading, MA: Addison Wesley, 1993.

6. Humphrey, W.S. Managing the Software Process. Reading, MA: Addison Wesley, 1989.

7. Humphrey, W.S. A Discipline for Software Engineering. Reading, MA: Addison Wesley, 1994.

8. Nunamaker, J.F.; Briggs, R.O.; and Mittleman, D.D. Lessons from a decade of group support systems research. Proceedings of the 29th Annual Hawaiian Conference on System Sciences, 1996, pp. 418–427.

9. Nunamaker, J.F.; Dennis, A.R.; Valacich, J.S.; Vogel, D.R.; and George, J.F. Electronic meeting to support group work. \*Comunications of the ACM\*, 7 (July 1991), 40–61.

10. Porter, A.A.; Votta, L.G.; and Basili, V.R. Comparing detection methods for software requirements inspections: a replicated experiment. IEEE Transactions on Software Engineering, 6 (June 1995), 563–575.

11. Rooijmans, J.; Aerts, H.; and Van Genuchten, M. Software quality in consumer electronic products. IEEE Software, 1 (January 1996), 55–64.

12. Votta, L.G. Does every inspection need a meeting? Proceedings of the ACM SIGSOFT 1993 Symposium on foundations of software engineering, Assoc. for Computing Machinery, December 1993.

13. Weatherall, A., and Nunamaker, J.F. An Introduction to Electronic Meeting Systems. Hampshire, UK: Electronic Meetings Services Ltd., 1995.
