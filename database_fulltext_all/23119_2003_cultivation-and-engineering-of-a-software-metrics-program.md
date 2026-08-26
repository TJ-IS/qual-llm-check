---
otero_id: 23119
otero_key: "DBBZD2VN"
title: "Cultivation and engineering of a software metrics program"
authors: "Jakob Iversen; Lars Mathiassen"
year: "2003"
journal: "Information Systems Journal"
doi: "10.1046/j.1365-2575.2003.00136.x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cultivation and engineering of a software metrics program

Jakob Iversen\* & Lars Mathiassen<sup>†</sup>

\*College of Business Administration, University of Wisconsin Oshkosh, USA, email: iversen@uwosh.edu, and <sup>†</sup>J Mack Robinson College of Business, Georgia State University, USA, email: lars.mathiassen@eci.gsu.edu

Abstract. This paper reports from a case study of an organization that implements a software metrics program to measure the effects of its improvement efforts. The program measures key indicators of all completed projects and summarizes progress information in a quarterly management report. The implementation turns out to be long and complex, as the organization is confronted with dilemmas based on contradictory demands and value conflicts. The process is interpreted as a combination of a rational engineering process in which a metrics program is constructed and put into use, and an evolutionary cultivation process in which basic values of the software organization are confronted and transformed. The analysis exemplifies the difficulties and challenges that software organizations face when bringing known principles for software metrics programs into practical use. The article discusses the insights gained from the case in six lessons that may be used by Software Process Improvement managers in implementing a successful metrics program.

Keywords: metrics, software development, software management, software pro cess improvement

## INTRODUCTION

Software Process Improvement (SPI) is seen today as one of the most viable approaches to improve decisively the state of software development (Humphrey, 1989; Grady, 1997). A weakness in most SPI efforts is, however, the lack of effective measurements of the impact of the effort on the business. With little information on the negative or positive impact of improvement initiatives, it is difficult to manage the effort. Corporate-wide metrics programs paint a picture of the software operation that is different from those emerging from software assessments based on normative maturity models (Gray & Smith, 1998) and Jones (2001) argues that the industry leaders use such programs to know their quality and productivity levels. Although, a survey of the literature on the effect of SPI initiatives is provided by Emam & Briand (1997), relatively little has been written on the process of successfully implementing a metrics program in the context of an SPI program.

This paper presents a longitudinal case study (Galliers, 1992; Yin, 1994) of an organization in which the implementation of a software metrics program turns out to be long and complex, as the organization is confronted with dilemmas based on contradictory demands and value conflicts. The study describes and interprets the difficulties and challenges related to bringing known principles for software metrics programs into practical use. According to Dekkers (1999) ‘there is an overwhelming focus on the technical aspects of measurement but very little on the cultural and human side of metrics implementation’ in the general literature on metrics programs. In an attempt to fill this gap, we therefore, interpret, the case from both a technical and a cultural perspective.

First, we see the implementation process as a rational, engineering process (Dahlbom & Mathiassen, 1993; 1997) in which metrics programs are designed and constructed (Basili & Weiss, 1984; Carleton et al., 1992; Briand et al., 1996; Fenton & Pfleeger, 1997). From this point of view, the challenge is to build a device, i.e. a metrics program, which provides information about the software operation based on a number of indicators. The quality of the effort depends on how useful the provided information is in making decisions about the improvement effort. The underlying approach is that of instrumental problem solving (Schön, 1983) and the task is to build a signalling device to support rational decision-making about SPI (Feldman & March, 1981).

Second, we view the implementation as an evolutionary cultivation process in which interests and values within the software organizations are confronted and transformed (Schein, 1985; Dahlbom & Mathiassen, 1993; 1997). From this point of view, the challenge is to transform a software culture from being based on espoused theories, i.e. on what software developers and managers believe and say, to being based on indicators of the theories-in-use, i.e. the deeply rooted assumptions (Schein, 1985) that govern the actual software practices. The quality of the effort depends, from this viewpoint, on how successfully the measurement program is integrated into its use context. The underlying approach is that of organizational intervention (Argyris & Schön, 1978; Argyris & Schön, 1996) emphasizing the symbolic aspects of the metrics program as an element in changing management practices (Feldman & March, 1981).

The next section presents the case organization, its SPI project, and the underlying research approach. Then follows a detailed presentation of the sequence of events that took place in implementing the metrics program. Next, the engineering and cultivation perspectives are explored to make sense of the described events. Finally, we combine the experiences and interpretations from the case with state-of-the-art knowledge on software metrics (Pfleeger, 1993; Hall & Fenton, 1997; Herbsleb & Grinter, 1998; Dekkers, 1999) to arrive at a number of lessons on how to successfully implement software metrics programs.

## CASE: FINANCIAL SOFTWARE SOLUTIONS

Financial Software Solutions (FSS) is a subsidiary of Financial Group providing all aspects of financial services (e.g. banking, mortgaging, insurance). The primary business function of FSS is the development of IT systems for Financial Group, but FSS also sells systems to other financial institutions across Europe. FSS has expertise in the development of banking, insur ance, mortgage and finance applications. FSS has approximately 850 employees located at four geographically dispersed development centres.

## SPI in financial software solutions

The SPI project in FSS was initiated in early 1997 to help ensure the competitiveness of the organization. The SPI project was organized as shown in Figure 1. The improvement group acts as a catalyst for specific improvement projects and makes detailed decisions on how and what to improve. The presented case study is based on 3 years of participation in the process support group closely following the improvement efforts. During this period, a number of improvement projects took place: project management, diffusion and adoption of methods and techniques, quality assurance in projects, self-assessment and metrics.

The particular focus of this study is on the implementation of the metrics program. FSS decided very early in the SPI process to launch this initiative to enable the SPI project and senior management to assess the effect of the improvement activities and hence to make informed decisions about future initiatives. The measurements were also seen as a way of getting attention from and feedback to the rest of the organization on the SPI project.

![](/api/attachments/DBBZD2VN/fulltext/images/d9b068c6b44b15fbf6372f0e4f43f3f90bd7621605ef238c346167fc79b07b95.jpg)  
Figure 1. Organization of the software process improvement (SPI) project.

## Research approach

The goal of the presented research was to learn about the practical difficulties and challenges that software organizations face when bringing known principles for software metrics programs into practical use. The strength of the case study approach is that it provides rich insight into and allows for a broad interpretation of practices in one or a few organizations (Galliers, 1992; Yin, 1994). We therefore decided to design our research as a longitudinal case study focusing on the implementation of the metrics program at FSS.

The interaction between the researchers and the practitioners took place at monthly meetings in the process support group at FSS, at ad hoc meetings at FSS, and at workshops in which specific improvement initiatives were discussed. The researchers captured and discussed the status, problems and opportunities related to the implementation of the metrics program as it evolved, but they played no role in the actual implementation activities. The researchers followed the metrics program from its inception in January 1997 until the end of 1999.

The research was part of a large research program involving FSS, three other softwaredeveloping companies, two universities and a consultancy company (Mathiassen, 2002; Mathiassen et al., 2002). We systematically collected data about the SPI initiatives at FSS over the entire 3-year period and the resulting database includes all key documents of the SPI program, such as project plans, meeting minutes and memos, together with audio recordings of the monthly meetings in the process support group and of most of the ad hoc meetings and workshops. For this particular case study, all relevant segments of the tapes were transcribed, all documents related to the metrics program were selected and analysed, and the resulting presentation of the implementation process (see Key events in implementing the program) was checked and validated by the SPI practitioners at FSS.

One important weakness of case studies is the difficulty in generalizing the results (Galliers, 1992; Yin, 1994). We did not consider this a key weakness in our case as the primary purpose was to provide a rich description and complementary interpretations of one particular implementation effort to exemplify what happens when known principles for metrics implementation meet practice. Nevertheless, we decided to compensate for the limited ability to generalize by combining the experiences and interpretations of our case with related findings from other studies (Pfleeger, 1993; Hall & Fenton, 1997; Herbsleb & Grinter, 1998; Dekkers. 1999) to arrive at a number of lessons on implementation of software metrics programs.

## KEY EVENTS IN IMPLEMENTING THE PROGRAM

The following presentation of the implementation of the metrics program in FSS is structured around events that have influenced the process (see Table 1). Some of the key stakeholders are listed and described in Table 2.

Table 1. Timeline of key events

<table><tr><td>Year</td><td colspan="6">1997</td><td colspan="6">1998</td><td colspan="6">1999</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Month</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td>J</td><td>F</td><td>M</td><td>A</td><td>M</td><td>J</td><td>J</td><td>A</td><td>S</td><td>O</td><td>N</td><td>D</td><td></td></tr><tr><td>Event</td><td>1</td><td></td><td>2</td><td></td><td></td><td></td><td></td><td></td><td></td><td>3</td><td></td><td></td><td>4</td><td></td><td></td><td></td><td></td><td></td><td>6</td><td></td><td></td><td></td><td></td><td></td><td>7</td><td></td><td></td><td></td><td></td><td>8</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr><tr><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td>5</td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td><td></td></tr></table>

Table 2. Key stakeholders of the metrics program

<table><tr><td>CEO</td><td>Sponsor of the SPI project. Stated that FSS should improve efficiency by 10% through SPI.</td></tr><tr><td>Vice presidents</td><td>Responsible for 20–25 people and three to five projects, they are what the CMM terms ‘first-line software managers’. Their attitude towards the metrics program is important to how the project managers and developers perceive the metrics program.</td></tr><tr><td>Project managers</td><td>Required to provide data on their project to the metrics program.</td></tr><tr><td>Peter</td><td>Project manager of the SPI project from March 1997 to February 1998, and again after 1 June 1998.</td></tr><tr><td>John</td><td>Project manager for the SPI project from February 1998 to 1 June 1998.</td></tr><tr><td>Ashley</td><td>Employed full time on the SPI project. Project manager for the metrics project until mid-1999.</td></tr><tr><td>Cole</td><td>Employed full time on the SPI project. Took over project manager responsibility for the metrics project mid-1999.</td></tr><tr><td>Finley</td><td>Vice President and member of the SPI improvement group. Was heavily involved in defining the metrics program.</td></tr><tr><td>Linda</td><td>Vice President and member of the SPI improvement group. Has not been directly involved in the metrics program.</td></tr></table>

## Press conference: January 1997

The SPI project was initiated with a press conference where the CEO of FSS stated that ‘We expect to gain a 10% improvement in efficiency through this project [. . .] that is equal to 30 mill. DKK.’ This statement has become an important focal point of the SPI project in FSS, and from the beginning of the project it has been important to document this 10% improvement. However, neither the CEO nor the contract was explicit on what should be measured to show this 10% efficiency improvement. This was left to those members of the improvement group who were responsible for implementing the metrics program.

## Decision to implement: March 1997

After some input from the researchers, the improvement group decided to measure the six factors listed in Table 3. This decision was discussed at the SPI project team meeting on 25 March 1997. Although no precise definitions existed at this point, the improvement group had some ideas about how to measure each factor. More precise definitions can be found in the decision memo of 13 May 1997 as reflected in the definition' column in Table 3

The decision memo also laid down some principles for the metrics program:

Table 3. Indicators of the metrics program

<table><tr><td>Factor</td><td>Definition</td></tr><tr><td>Project productivity</td><td>Resources used to develop the system relative to its size in function points.</td></tr><tr><td>Quality</td><td>Number of error reports both absolute and relative to size in function points.</td></tr><tr><td>Adherence to schedule</td><td>Variation from agreed time of delivery both absolute and relative to size in function points.</td></tr><tr><td>Adherence to budget</td><td>Variation from estimated use of resources.</td></tr><tr><td>Customer satisfaction</td><td>Satisfaction with the development process and the implemented solution (multiple-choice questionnaire).</td></tr><tr><td>Employee satisfaction</td><td>Satisfaction with the development process (multiple-choice questionnaire).</td></tr></table>

• Measurements should be relevant in relation to process improvement and quality, but also have general management interest.

Measurements should be made automatic where possible and information should be interpreted to minimize disturbance of the development organization.

• Cost of performing the measurements should be minimal.

• Use of questionnaires should be limited as the organization suffers from ‘questionnaire disgust’. If questionnaires are used, they should be placed at a milestone and be adapted to development practices.

Data should be collected on projects that were finished (to keep disturbances to a minimum) and results should be published every quarter. The responsibility for collecting the data was not discussed, and thus implicitly given to the improvement group. It was, however, believed that much of the data could be collected from already public sources (e.g. project budgets, project reports and contracts). The volume of the projects should be calculated using an automatic counting algorithm for function points (IFPUG, 1994). Function points are usually calculated by experts and few organizations have attempted counting function points automatically. The project concentrated some effort (approximately 1–2 man-months) on implementing a system to do this automatic calculation, although this was a relatively risky endeavour. If the design would succeed, the project managers would only have to report very few numbers manually, and there was already an on-line system in place for registering this information (planned and actual delivery dates for the system, as well as effort spent on the project).

## First report: September 1997

The first visible result of the measurement program was the first measurement report with results from 13 out of 56 projects that were completed in third quarter of 1997 (3Q97). The report had data on three out of the six factors (adherence to budget, time-to-market and project productivity). The data contained surprising information, especially regarding adherence to budget, causing senior management to withhold the report from wide distribution. Parts of the results were, however, disseminated to the development organization through a roadshow conducted by the improvement group to raise awareness towards the SPI project. The report was criticized for being too academic. A workshop was held in October 1997 to alleviate thi problem.

The problems in gaining acceptance for the report did not bother the improvement group sig nificantly, as it was the first report based on less than optimal data.

## Second report: March 1998

Data for the second report, covering projects that were completed in 4Q97, were ready in March 1998. The results were discussed in an SPI project team meeting on 20 February 1998 Data discipline had been greatly improved and the percentage of complete datasets had gone up from 37% to 65%.

This improvement in data discipline and thus in data quality was received with much enthusiasm at the meeting. However, the discussion soon centred on the issue of whether the report would be made public or not. There was general consensus that senior management had accepted this idea.

Linda: ‘I think we have [the CEOs] commitment that now he will [make it public], and we should of course make sure he sticks to that, once the report is completed.

The report had a much clearer layout than the first report. Data on customer and employee satisfaction was included, whereas productivity data were not, as the automatic calculation of function points did not match the developers’ perceptions of the relative complexities of the measured systems.

## Decision not to publish: March 1998

The report was presented to the steering committee on 31 March 1998. Unlike the SPI project team, senior managers considered the data insufficiently reliable to warrant wide distribution. Moreover, the results of the satisfaction surveys showed very unfavourable results for key business areas for FSS. The presentation of the report to the steering committee was discussed at the SPI project team meeting on 22 April 1998.

Meeting minutes: ‘The report is not and will not be made public internally in FSS. A strong contributing factor to this is that [. . .] data validity is insufficient.

John [on presentation of the customer satisfaction report to senior management]: ‘But this number [customer satisfaction]–here he [the CEO] almost fell off his chair. For what is it that we in FSS should do? We should be business partners with the corporation. We are competent and should show them that.

The SPI project team discovered quickly that the problems could mainly be attributed to the customer satisfaction questionnaire. The questions were primarily directed towards customers, whereas in most cases users, who had not been involved in negotiating terms and contracts, had answered it.

Finley: ‘We send these questionnaires [. . .] to people who were involved in the acceptance test of the system, and what we then ask are managerial, contractual, overall processrelated questions on how the project was conducted. Then some random user has to answer if commitments were met. He hasn’t seen the contract or anything. It’s bound to go wrong, and that’s why management can’t recognize reality in these numbers.

The issue of management commitment towards metrics was discussed as well.

Finley: ‘I don’t know how much management commitment we have here [. . .] We ask for more resources, but nothing much is happening [. . .] We must end up with something that gives management a credible picture of reality. Otherwise they will say: this measurement stuff–forget it, I’ll be better off trusting my intuition.

Linda: ‘I get personally disappointed that [the CEO] does not release the report. I can understand that he is afraid of [Financial Group’s central IT co-ordinator], but if we are ever going to get people interested in SPI, then they need to see what the project is doing.

This is the single most important event causing a dramatic increase in the attention given to the program and resulting in the establishment of a project to improve the metrics program. So far, significant resources had been used on defining each metric, and deciding how to measure them. But some aspects had still been overlooked: the questions in the satisfaction questionnaires had not been carefully formulated, and the customer questionnaire was given to users instead of customers. On top of that, insufficient attention had been given to incentives for reporting the necessary data, resulting in poor data discipline.

## Project established: August 1998

After the disappointment that the second report was not made public, an SPI project team meeting on 22 April 1998 focused on actions that could be taken to improve the metrics program enough to enable publication of the next report.

Lars (researcher): ‘. . . it’s all about planning. If we think of the establishment of the metrics program as a systematic improvement effort, then we need to have a plan for this project; a plan of how to systematically improve the initiative. [. . .] As a first goal we need to give this sufficient solidity that the management group dare say that this is public. That should be a baseline for this year.

The project was proposed in June 1998, and the contract was signed in August 1998. The project was established with the expressed goal to improve the quality of the measurement report enough that it would be impossible for management to deny making it public.

The main success criterion for the project was that a measurement report should be completed in April 1999 containing data on all six indicators and from all projects completed in 1Q99. Compared with the second report, this report should have improved the measurement process for all the indicators, and the layout of the report should also be enhanced. Among other things, the data quality of each indicator should be displayed, for instance as a percent age of complete datasets (as in Table 4).

Table 4. Data discipline in the metrics program

<table><tr><td rowspan="2">Period</td><td rowspan="2">Report</td><td rowspan="2"># Projects</td><td colspan="2">Complete datasets</td></tr><tr><td>#</td><td>%</td></tr><tr><td>3Q97</td><td>1</td><td>56</td><td>21</td><td>37</td></tr><tr><td>4Q97</td><td>2</td><td>29</td><td>19</td><td>65</td></tr><tr><td>1Q99</td><td>3</td><td>44</td><td>10</td><td>23</td></tr><tr><td>2Q99</td><td>4</td><td>80</td><td>51</td><td>64</td></tr></table>

It was decided early that function points would not be included due to the problems of making a sufficiently accurate count. The possibility of using other size measures was examined and rejected. All of the measures proposed (lines of code, compiled size, function points and number of statements) had severe weaknesses. Excluding a size measure, of course, seriously impeded reaching the original objective of measuring efficiency and productivity, as there was no longer a measure of the output of the project.

## Third report: April 1999

On 29 March 1999 the results of the improvement effort were discussed in the SPI project team.

Ashley: ‘We have worked with this since October, and have achieved improvements of both the customer and employee satisfaction questionnaires. We pulled out data [. . .] for 1Q99 [. . .] and discovered that data discipline was as it had always been: lousy. Despite the fact that we have prompted people and sent out guidelines for how to fill in the fields [. . .]. So we have been a little depressed.

Only 10 projects had reported complete data in the period, and the data they had reported could not necessarily be trusted.

Cole: ‘We have called them up and asked what their estimate was, and some of them said “oh, well, yes it must be something like . . .” . . . Many of these are not real estimates, then.

Rather than make a measurement report, it was therefore decided to produce a memo to senior management describing the problems with data discipline and recommending a strategy for alleviating the problems. The memo also described three problems involved in obtaining complete and accurate data about the projects.

Ashley: ‘There are some who simply do not enter data into the system. There are some that have misunderstood the definition of the fields [. . .] There are some who are not particularly good at maintaining the data they have entered, if there are any changes later.

During the improvement project a bonus system was introduced. In one of the divisions complete and accurate reporting of data for the metrics program was considered one of the bonus factors.

Cole: ‘But because it has become a bonus goal in Division I, then the [Division vice President] wants this to happen, and that helps [. . .] Perhaps it will be possible to spread this practice to the rest of the organization.

In addition, the satisfaction surveys had been integrated into the quality assurance process, and seemed to work well. The projects had given the questionnaires to their customers and employees, and the results were discussed in one or two quality meetings towards the end of the project.

## Decision to publish: September 1999

On 21 September 1999, the measurement report for 2Q99 was presented to management. The report contained data from 51 out of the 80 projects that were completed in the period. The report states that:

‘[This] is the best data foundation ever. The report’s result should therefore provide a credible picture of the actual state of affairs in FSS.’

The report was released to all vice presidents, and the senior vice presidents had a few corrections. On that basis, it was decided to distribute the next report (3Q99) to project managers as well, and every report from 4Q99 on to all employees of FSS. The metrics team would have liked to see the 2Q99 report distributed to all employees, but the decision nevertheless expressed the kind of recognition that the group had hoped for since the first measurement report was withheld by management in September 1997.

## ENGINEERING AND CULTIVATION

Interpreting these events from a rational, engineering perspective we see a rather inefficient effort with only modest success. The effort got a flying start with explicit goals and maximum management attention (event #1). A detailed design of the involved metrics was created together with basic principles for the implementation of the program (event #2). This design was debated with and accepted by management. The first measurement report only included 20% of the projects and only three out of six factors. In addition, the report was criticized for being too academic (event #3). Data discipline was improved in the next report and the report had a much clearer lavout than the first report (event #4). The data were, however, still considered too unreliable by management (event #5) and that led to the establishment of a new, intensified metrics project in which the metrics program was redesigned. As part of this redesign the metrics to provide information on productivity (based on function points) were dropped (event #6). Some improvements were then made in gathering information about customer satisfaction (event #7). Finally, after 2.5 years of effort, the quality of the quarterly report was con sidered to have a quality that warranted publication. One of the major problems as seen from an engineering purpose was that the purpose of collecting the data (i.e. to use the resulting information to direct the SPI effort and give input to senior management) was not fulfilled; no one outside the SPI project was yet using the data to support learning or decision making. In addition, having dropped the output measure (function points), it became impossible for the metrics program to fulfil the original goal of showing whether the SPI project would generate a 10% improvement in efficiency.

Quite a different picture emerges, however, when the same events are interpreted from an evolutionary, cultivation point of view. An ambitious statement was announced by top management implying that a transformation of current management practices was needed (event #1). The productivity should improve and a metrics program should be implemented to evaluate whether this goal was being achieved. The existing management practice, which was mainly based on espoused theories of software developers and managers, was to be complemented with a data-driven intervention approach based on indicators of the theories-in-use in the soft ware organization. When the first report was presented to management it contained surprising and negative information on current practices causing senior management to withhold the report (event #3). A dilemma emerged between, on the one hand, publication to increase knowledge, stimulate debate, increase participation in the project, and improve data quality, and, on the other hand, a concern for negative effects. But no shared understanding of possible strategies to overcome this dilemma was reached (event #4). The failure to automatically measure function points confronted the effort with another dilemma between the relevance of the data and the economy of gathering them. As a consequence it was decided to drop the productivity metrics (events #5 and #7) and the effort was reorganized as a proper improvement initiative with more resources and incentive schemes (event #6). After intensive efforts to improve the quality of the quarterly report, management finally made its first move towards new managerial practices by publishing the reports (events #7 and #8).

From a technical point of view, we see an engineering project with very slow progress and limited success. But, from a cultural point of view, we see an initiative that was first conceived as a rather straightforward engineering effort being transformed into a successful transformation of managerial practices. The organization has, in this second view, gained significant experience in implementing data-driven intervention. Data is now being collected and distributed on a regular basis so they can contribute to critical reflections on the beliefs and intuitions about how the organization operates. The case demonstrates in this way the importance of comple menting a technical view of measurement with ‘the cultural or human side of metrics imple mentation’ (Dekkers, 1999).

## LESSONS LEARNED

The general lesson that can be drawn from this case is not new: successful use of technology in organizational contexts requires efforts that go beyond instrumental problem solving. Traditional engineering approaches must be supplemented with a focus on the involved formative contexts (Ciborra & Lanzara, 1994) and an understanding of how to transform the involved communities-of-practice (Brown & Duguid, 1991). The reported experiences do, however, give rise to a number of specific lessons that combines engineering and cultivation aspects of software metrics implementation. The following lessons are structured based on the experiences from FSS and systematically related to similar findings (Pfleeger, 1993; Hall & Fenton, 1997; Herbsleb & Grinter, 1998; Dekkers, 1999). In this way, we increase the validity of the lessons as well as their potential applicability to other software organizations. Each individual organization is, however, advised to carefully consider its particular context in designing its own implementation strategy.

## Establish a project

At first, the metrics program at FSS was considered an integrated part of the SPI project. There was no plan and the objectives were described in vague terms in the SPI project contract. It was only because of the dedication of a few employees that a metrics program was being developed at all. Later in the process, when a real project was established, it became far easier to argue that adequate resources should be available, and the focus on the initiative generally increased. Missing or unreliable data were no longer seen as defects. They became baselines for tracking improvements in the quality of the metrics.

Dekkers recommends setting solid objectives and plans for the measurement program (secret #1). The measurement program should be conducted as if it were a regular software engineering project with requirements, design and project management. She recommends applying an approach such as Goal-Question-Metric (Basili & Weiss, 1984). Briand et al. (1996) offer engineering guidelines for this approach based on the following steps: (1) characterize the environment; (2) identify measurement goals and develop measurement plans; (3) define data collection procedures; (4) collect, analyse and interpret data; (5) perform postmortem analysis and interpret data; and (6) package experience.

Hall and Fenton (Hall & Fenton, 1997) agree that it is imperative to establish a dedicated metrics team. External gurus and internal champions should be included in the team and software developers should participate in designing the metrics program.

## Start simple

The attempt at FSS to measure six complex indicators with no previous measurement process in place is extremely ambitious. You become disappointed when the collected data does not have the expected quality, and measuring some indicators must be abandoned. A more sensible approach is to start measuring a few indicators, perhaps just collecting and analysing data that are already there. Later, when the organization has gained experience in measuring and being measured, other measures can be added. Such a stepwise introduction of a metrics program will take longer than the ambitious one-shot approach. But the likelihood of success is greater.

Dekkers advocates applying a complementary suite of measures (secret #7) as in the bal anced score card approach (Kaplan & Norton, 1996). Several measures provide a more com plete understanding of the software development process, minimizing the risk of suboptimizing management actions. We strongly advice, however, to adopt a stepwise strategy in which relatively simple measures are implemented first.

We are supported in this viewpoint by Briand et al. (1996) who state that ‘it is a good strategy to start with a small number of goals, gain experience, and then develop the program further. The technical complexity together with the cultural uncertainty warrants a cautious strategy in which learning from experience minimizes the risk of failure. A stepwise learning process will, as advocated by Dekkers, help the SPI group gain a thorough understanding of what measurement is all about, including benefits and limitations (secret #3). Hall & Fenton (1997) propose an incremental implementation of the program. Pfleeger (1993) argues that a few metrics are better than no metrics and she suggests keeping things simple so that developers understand the relationship between collected metrics and their use.

## Create incentives

The FSS case illustrates the value of creating incentives to improve data quality. From the out set, all projects were required to record data in an on-line registration system. But almost no projects recorded complete and accurate data mainly because they saw no immediate use fo the data. A marked improvement of data quality was achieved by informing the project man agers of what data they should report and about the importance of the data they provided and by showing them results based on the data. When reporting complete and accurate data became part of the bonus system, a very clear incentive scheme was established, and the data quality clearly improved.

Dekkers argues that the measurement program should be a natural part of the development process (secret #2). When the results of the program are readily useful to those who supply the data, they are far more likely to supply the necessary data of sufficient quality and at the right time. This also protects the program from budget cuts. Dekkers also recommends realigning the corporate reward system to promote collection of complete and accurate data (secret #5), thus tying the existing, formal incentive structure to the metrics program. Pfleeger (1993) argues that you should not force developers to collect a particular metrics if they do not wan to as this will result in inaccurate and incomplete data. This situation can be circumvented if data can be collected automatically.

## Publish widely

The biggest disappointment for the measurement team at FSS was management’s decisions to withhold reports. It is vital that the development organization be given the opportunity to provide feedback on the quality and relevance of the metrics program. But measurements provide views on sensitive issues and they must therefore be based on data that are sufficiently accu rate to support fruitful discussions.

Metrics will probably yield unpleasant information about the software operation. Being able to cope with such information and use it to improve the organization is an important part of the cultivation involved in implementing metrics programs. It is important that performance measures of individuals be kept to the individual. Otherwise, everybody would make their data look better, and the entire purpose of the metrics program to establish indicators of current theoriesin-use would be lost.

Dekkers calls for creating a safe environment for collecting and reporting data (secret #5). It is important that those who report the data feel safe that the data will not in any way be used against them. One possibility is to publish what the data are used for together with relevant aggregate results. Another possibility pointed to by Pfleeger (1993) is to keep the metrics close to the developers and enable them to access the metrics, evaluate them and take actions accordingly. Hall & Fenton (1997) point out that practitioners should get feedback on the data they collect to give them a clear indication that the data is being used rather than going into a black hole.

## Facilitate debate

The different versions of the metrics program at FSS have been subject to intensive discussions in the SPI group and with management. These discussions have revealed several weaknesses, and the decision to publish future reports widely will provide additiona feedback.

Implementing a metrics program forms an important shift towards a culture where decisions are based on relevant and accurate data about practice rather than vague intuitions. For the metrics to reach a sufficiently high level of quality, the organization must be willing to make less than optimal data available for broad discussions about the accuracy and underlying assumptions of the measurements. Even if the accuracy of data is not as high as could be desired, the information gained might still carry some relevance. Numbers should never be taken as absolute truths. Instead, the data and their quality should be debated amongst those involved in and affected by the metrics program.

In a situation as the one in FSS, where metrics results cannot be made widely available to the entire organization, it may still be valuable to facilitate debate over local results. This could help developers and project managers see the value of the data they provide and, in turn, help improve the data quality of the overall metrics program. In fact, such an activity was carried out in FSS through the road show conducted after the first report was completed.

Broad discussions critically evaluate the program and help make sense of the provided data and results. This is in line with Dekkers’ general advice to focus on cultural issues (secret #4). Those affected by the program must be involved in its design so that resistance to change is minimized. This can best be achieved through an iterative process of redesigns in which results and procedures are continuously published and debated. Another option pointed out by Hall & Fenton (1997) is to organize training sessions to acquire the necessary skills but also to raise awareness amongst practitioners at all levels in the organization.

## Use the data

After 2.5 years of effort, FSS is now in a position where managers, SPI specialists and systems developers in general can start making use of the data and results. If the data are not used to gain insight and as a basis for making corrective actions, the metrics program will soon degenerate into a bureaucratic procedure that merely adds to the overhead of developing software without contributing to the continuous improvement of the software operation.

This fundamental lesson is in line with Hall and Fenton who stress that a metrics program’s usefulness should be obvious to practitioners (Hall & Fenton, 1997). Moreover, Dekkers points out that the organization must be ready to take corrective actions based on the measurements (secret #6). Herbsleb & Grinter (1998) elaborate on the different organizational systems in which the data can be used (the project management system, the SPI system and the strategic management system) and Pfleeger provides detailed insights into the practical use of metrics data in software projects (Pfleeger, 1993).

## SUMMARY

A corporate-wide metrics program has been developed at FSS by using post-mortem measurements. The information obtained is to be used as an indicator of the effect of ongoing SPI initiatives within the organization. The paper has presented a detailed account of the imple mentation effort, the events have been interpreted using a combination of an engineering and a cultivation perspective, and lessons have been derived and validated against similar findings from other studies on how to implement software metrics programs.

The key contribution of the paper is that it offers insights into the practical process of imple menting metrics programs. This process illustrates how known principles for software metrics programs meet practice and it shows that the combination of engineering and cultivation perspectives offers a useful and interesting way of looking at the implementation of a metrics pro gram. The insights gained by the authors have been captured and discussed in six lessons that hopefully will provide researchers and practitioners alike with assistance in understanding what it takes to implement and operate successful metrics programs.

To overcome the limitations introduced by using case studies to research software metrics practices it may be advantageous to introduce research tools such as the one proposed by Berry & Jeffery (2000) in which an on-line questionnaire is used to gather information about a number of organizations' metrics programs. Such research could help further generalize and refine the lessons, recommendations, and advice that currently exist about software metrics programs (Fenton et al., 1994).

## ACKNOWLEDGEMENTS

Financial Software Solutions is thanked for granting access to their SPI project and providing excellent conditions for conducting this research. The Danish National Center for IT Research has financially supported this research. The following colleagues have provided valuable input to the paper: Ivan Aaen, Jesper Arent, Gro Bjerknes, Karlheinz Kautz, Jacob Nørbjerg and Rens Scheepers. An earlier version of the paper appeared at the 22nd Information Systems Research Seminar in Scandinavia (IRIS 22) (Iversen & Mathiassen, 1999). We thank all those who gave constructive feedback at that workshop. In addition, we wish to thank the associate editor and the reviewers for valuable feedback and constructive criticism in developing this fina version of the paper.

## REFERENCES

Argyris, C. & Schön, D.A. (1978) Organizational Learning: a Theory of Action Perspective. Addison-Wesley, Reading, MA.

Argyris, C. & Schön, D.A. (1996) Organizational Learning II: Theory, Methods, and Practice. Addison-Wesley, Reading, MA.

Basili, V.R. & Weiss, D.M. (1984) A methodology for collecting valid software engineering data. IEEE Transactions on Software Engineering, 10, 728–738.

Berry, M. & Jeffery, R. (2000) Empirical Software Engi neering Conference, Staffordshire, UK.

Briand, L.C., Differing, C.M. & Rombach, H.D. (1996) Practical guidelines for measurement-based process improvement. Software Process–Improvement and Practice, 2, 253–280.

Brown, J.S. & Duguid, P. (1991) Organizational learning and communities-of-practice: toward a unified view o working, learning, and innovation. Organization Science, 2, 40–57.

Carleton, A.D., Park, R.E., Goethert, W.B., Florac, W.A., Bailey, E.K. & Pfleeger, S.L. (1992). Software Engineering Institute, Pittsburgh, PA.

Ciborra, C. & Lanzara, G.F. (1994) Formative contexts and information technology. understanding the dynamics of innovation in organizations. Accounting, Management and Information Technology, 4, 61–86.

Dahlbom, B. & Mathiassen, L. (1993) Computers in Context–the Philosophy and Practice of System Design Blackwell, Cambridge, MS.

Dahlbom, B. & Mathiassen, L. (1997) The future of our profession. Communications of the ACM, 40.

Dekkers, C.A. (1999) The secrets of highly successfu measurement programs. Cutter IT Journal, 12, 29–35.

Emam K E & Briand L(1997) Costs and Benefits of Software Process Improvement, ISERN-97-12. Fraunhofer-Institute for Experimental Software Engineering.

Feldman, M.S. & March, J.G. (1981) Information in organization as signals and symbols. Administrative Science Quarterly, 26, 171–186.

Fenton, N.E. & Pfleeger, S.L. (1997) Software Metrics–a Rigorous and Practical Approach. PWS Publishing Co, Boston, MA.

Fenton, N., Pfleeger, S.L. & Glass, R.L. (1994) Science and substance: a challenge to software engineers. IEEE Software, 11, 86–95.

Galliers, R.D. (1992) Information Systems Research: Issues, Methods and Practical Guidelines Galliers, R.D. (ed.), pp. 144–162. Blackwell Scientific Publications, Oxford.

Grady, R.B. (1997) Successful Software Process Improvement. Prentice Hall PTR, Upper Saddle River, NJ.

Gray, E.M. & Smith, W.L. (1998) On the limitations of software process assessment and the recognitions of a required re-orientations for global process improvement. Software Quality Journal, 7, 21–34.

Hall, T. & Fenton, N. (1997) implementing effective software metrics programs. IEEE Software, 14, 55–65.

Herbsleb, J.D. & Grinter, R.E. (1998) The 20th International Conference on Software Engineering, pp. 271– 280. IEEE, Kyoto, Japan.

Humphrey, W.S. (1989) Managing the Software Process Addison-Wesley, Pittsburgh, PA.

IFPUG (1994) The International Function Point Users Group (IFPUG).

Iversen, J.H. & Mathiassen, L. (1999) Information Systems Research Seminar in Scandinavia (IRIS 22), Vol. 2, Käkolä, T.K. (ed.), pp. 111–124. University of Jyväskylä, Keuruu, Finland.

Jones, C. (2001) Software measurement programs and industry leadership Crosstalk-the Journal of Defense and Software Engineering, 14, 4–7.

Kaplan, R.S. & Norton, D.P. (1996) Strategic learning and

the balanced scorecard. Strategy & Leadership, 24, 18– 20.

Mathiassen, L. (2002) Collaborative Practice Research. Scandinavian Journal of Information Systems, 14.

Mathiassen, L., Pries-Heje, J. & Ngwenyama, O. (eds) (2002) Improving Software Organizations: From Principles to Practice. Addison-Wesley, Boston, MA.

Pfleeger, S.L. (1993) Lessons learned in building a corporate metrics program. IEEE Software, 10, 67– 74.

Schein, E.K. (1985) Organizational Culture and Leader ship. Jossey-Bass, San Francisco, CA.

Schön, D.A. (1983) The Reflective Practitioner. How Professionals Think in Action. Basic Books, New York.

Yin, R. (1994) Case Study Research. Sage Publications, Newbury Park, CA.

## Biographies

Jakob Iversen holds an MSc in software engineering from Aalborg University and a PhD in computer science from Aalborg University. He is currently an Assistant Professor at the College of Business Administration, University of Wisconsin Oshkosh. He has worked with software process improvement and measurement for 7 years.

Lars Mathiassen is a Professor in Computer Information Systems at Georgia State University with 27 years of experience as researcher, teacher and consult ant. His research interests focus on engineering and management of IT systems. More particularly, he has worked with project management, object orientation, organiza tional development, management of IT and the philosophy of computing.
