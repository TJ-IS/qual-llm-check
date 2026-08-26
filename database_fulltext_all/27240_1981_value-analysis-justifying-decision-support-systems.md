---
otero_id: 27240
otero_key: "G42CTTUR"
title: "Value Analysis: Justifying Decision Support Systems"
authors: "Peter G. W. Keen"
year: "1981"
journal: "MIS Quarterly"
doi: "10.2307/249154"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
Value Analysis: Justifying Decision Support Systems
Author(s): Peter G. W. Keen
Source: MIS Quarterly, Vol. 5, No. 1 (Mar., 1981), pp. 1-15
Published by: Management Information Systems Research Center, University of Minnesota
Stable URL: http://www.jstor.org/stable/249154

Accessed: 08/05/2014 20:36

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# DSS Series Editor's Note

The MIS Quarterly has shown a special interest in the question of assessing the costs and benefits of information systems. In this second article in the series on Decision Support Systems, Peter Keen deals with this issue for DSS which, by their very nature, make traditional cost benefit analysis nearly useless. He suggests and outlines value analysis as an alternative approach, based on the incremental development of the system, and staged cost-value assessments.

Ralph H. Sprague, Jr.

# Value Analysis: Justifying Decision Support Systems

By: Peter G. W. Keen

## Abstract

Managers face a dilemma in assessing DSS proposals. The issue of qualitative benefits is central, but they must find some way of deciding if the cost is justified. A general weakness of the cost-benefit approach is that it requires knowledge, accuracy, and confidence about issues which for innovations are unknown, ill-defined, and uncertain. The benefit of a DSS is the incentive for going ahead. The complex calculations of cost-benefit analysis are replaced in value analysis by rather simple questions about its usefulness.

Keywords: Decision support systems, value analysis, innovation

ACM Categories: 3.5, 3.64

## Introduction

Decision Support Systems (DSS) are designed to help improve the effectiveness and productivity of managers and professionals. They are interactive systems frequently used by individuals with little experience in computers and analytic methods. They support, rather than replace, judgment in that they do not automate the decision process nor impose a sequence of analysis on the user. A DSS is in effect a staff assistant to whom the manager delegates activities involving retrieval, computation, and reporting. The manager evaluates the results and selects the next step in the process. Table 1 lists typical DSS applications. $^{1}$

Traditional cost-benefit analysis is not well-suited to DSS. The benefits they provide are often qualitative; examples cited by users of DSS include the ability to examine more alternatives, stimulation of new ideas, and improved communication of analysis. It is extraordinarily difficult to place a value on these. In addition, most DSS evolve. There is no “final” system; an initial version is built and new facilities are added in

Other DSS referred to in this article are:
AAIMS: Klaas [13], Alter [1]
CAUSE: Alter [1]
GPLAN: Haseman [9]

Table 1. Examples of DSS Applications

<table><tr><td>DSS</td><td>Applications</td><td>Benefits</td></tr><tr><td>GADSGeodata AnalysisDisplay System</td><td>Geographical resource allocation and analysis; applications include sales force territories, police beat redesign, designating school boundaries</td><td>Ability to look at more alternatives, improved teamwork, can use the screen to get ideas across, improved confidence in the decision</td></tr><tr><td>PMSPortfolio Management System</td><td>Portfolio investment management</td><td>Better customer relations, ability to convey logic of a decision, value of graphics for identifying problem areas</td></tr><tr><td>IRISIndustrial RelationsInformation System</td><td>Ad hoc access to employee data for analysis of productivity and resource allocation</td><td>Ad hoc analysis, better use of “neglected and wasted” existing data resource, ability to handle unexpected short term problems</td></tr><tr><td>PROJECTOR</td><td>Strategic financial planning</td><td>Insight into the dynamics of the business, broader understanding of key variables</td></tr><tr><td>IFPSInteractive Financial Planning System</td><td>Financial modelling, including mergers and acquisitions, new product analysis, facilities planning and pricing analysis</td><td>Better and faster decisions, saving analysts’ time, better understanding of business factors, leveraging managing skills</td></tr><tr><td>ISSPA - Interactive Support System for Policy Analysts</td><td>Policy analysis in state government; simulations, reporting, and ad hoc modelling</td><td>Ad hoc analysis, broader scope, communication to/with legislators, fast reaction to new situations</td></tr><tr><td>BRANDAID</td><td>Marketing planning, setting prices, and budgets for advertising, sales force, promotion, etc.</td><td>Answering “what if?” questions, fine-tuning plans, problem-finding</td></tr><tr><td>IMSInteractive Marketing System</td><td>Media analysis of large consumer database, plan strategies for advertising</td><td>Helps build and explain to clients the rationale for media campaigns, ad hoc and easy access to information</td></tr></table>

response to the users' experience and learning. Because of this, the costs of the DSS are not easy to identify.

The decision to build a DSS seems to be based on value, rather than cost. The system represents an investment for future effectiveness. A useful analogue is management education. A company will sponsor a five day course on strategic planning, organizational development, or management control systems on the basis of perceived need or long term value. There is no attempt to look at payback period or ROI, nor does management expect a direct improvement in earnings per share.

## 2 MIS Quarterly/March 1981

This article examines how DSS are justified and recommends Value Analysis (VA), an overall methodology for planning and evaluating DSS proposals. The next section illustrates applications of DSS. Key points are:

1. a reliance on prototypes,

2. the absence of cost-benefit analysis,

3. the evolutionary nature of DSS development, and

4. the nature of the perceived benefits.

The section on the Dynamics of Innovation relates DSS to other types of innovation. It seems clear that innovation in general is driven by “demand-pull” — response to visible, concrete needs — and not “technology push.”

The Methodologies for Evaluating Proposals section briefly examines alternative approaches to evaluation: cost-benefit analysis, scoring techniques, and feasibility studies. They all require fairly precise estimates of, and tradeoffs between costs and benefits and often do not handle the qualitative issues central to DSS development and innovation in general. The final part of the article defines Value Analysis.

The overall issue this article addresses is a managerial one:

1. What does one need to know to decide if it is worthwhile to build a DSS?

2. How can an executive encourage innovation while making sure money is well spent?

3. How can one put some sort of figure on the value of effectiveness, learning, or creativity?

It would be foolish to sell a strategic planning course for executives on the basis of cost displacement and ROI. Similarly, any effort to exploit the substantial opportunity DSS provide to help managers do a better job must be couched in terms meaningful to them. This requires a focus on value and a recognition that qualitative benefits are of central relevance. At the same time, systematic assessment is essential. The initial expense of a DSS may be only in the \$10,000 range, but this still represents a significant commitment of funds and scarce programming resources. The methodology proposed here is based on a detailed analysis of the implementation of over, twenty DSS. It is consistent with the less formal approaches most managers seem to use in assessing technical innovations. Value analysis involves a two stage process:

1. Version 0: This is an initial, small scale system which is complete in itself, but may include limited functional capability. The decision to build Version 0 is based on:

a. An assessment of benefits, not necessarily quantified;

b. A cost threshold — is it worth risking this amount of money to get these benefits?

In general, only a few benefits will be assessed. The cost threshold must be kept low, so that this decision can be viewed as a low risk research and development venture, and not a capital investment.

2. Base System: This is the full system, which will be assessed if the trial Version 0 has successfully established the value of the proposed concept. The decision to develop it is based on:

a. Cost analysis: What are the costs of building this larger system?

b. Value threshold: What level of benefits is needed to justify the cost? What is the likelihood of this level being attained?

A major practical advantage of this two stage strategy is that it reduces the risks involved in development. More importantly, it simplifies the tradeoff between costs and benefits, without making the analysis simplistic. It is also a more natural approach than traditional cost-benefit analysis; until value is established, any cost is disproportionate.

## Decision Support Systems

The DSS applications shown in Table 1 cover a range of functional areas and types of task. They have many features in common:

1. They are non-routine and involve frequent ad hoc analysis, fast access to data, and generation of non-standard reports.

2. They often address “what-if?” questions; for example, “What if the interest rate is X%?” or “What if sales are 10% below the forecast?”

3. They have no obvious correct answers; the manager has to make qualitative tradeoffs and take into account situational factors.

The following examples illustrate the above points:

1. GADS. In designing school boundaries, parents and school officials worked together to resolve a highly charged political problem. A proposal might be rejected because it meant closing a particular school, having children cross a busy highway, or breaking up neighborhood groups. In a previous effort involving redistricting, only one solution has been generated, as opposed to six with GADS over a four day period. The interactive problem solving brought out a large number of previously unrecognized constraints such as transportation patterns and walking times, and parent's feelings.

2. BRANDAID. A brand manager heard a rumor that his advertising budget would be cut in half. By 5:00 p.m. he had a complete analysis of what he felt the effect would be on this year's and next year's sales.

3. IFPS. A model had been built to assess a potential acquisition. A decision was needed by 9:00 a.m. The results of the model suggested the acquisition be made. The senior executive involved felt uneasy. Within one hour, the model had been modified and “what if” issues assessed that led to rejection of the proposal.

4. ISSPA AND IRIS. Data which had always been available, but not accessible, were used to answer ad hoc, simple questions. Previously, no one bothered to ask them.

These characteristics of problems for which DSS are best suited impose design criteria. The system must be:

1. Flexible to handle varied situations.

2. Easy to use so it can be meshed into the manager's decision process simply and quickly.

4 MIS Quarterly/March 1981

3. Responsive because it must not impose a structure on the user and must give speedy service.

4. Communicative because the quality of the user-DSS dialogue and of the system outputs are key determinants of effective uses especially in tasks involving communication or negotiation. Managers will use computer systems that mesh with their natural mode of operation. The analogy of the DSS as a staff assistant is a useful one.

Many DSS rely on prototypes. Since the task the system supports is by definition non-routine, it is hard for the user to articulate the criteria for the DSS and for the designer to build functional specifications. An increasingly popular strategy is thus to use a flexible DSS “tool” such as APL, or a DSS “Generator” [15]. These allow an initial version of a “Specific DSS” to be delivered quickly and cheaply. It provides a concrete example that the user can react to and learn from. It can be easily expanded or modified. The initial system, Version 0, clarifies the design criteria and specifications for the full DSS. Examples of this two phase strategy include:

1. ISSPA — built in APL. Version 0 took seventy hours to build and contained nineteen commands. The design process began by sketching out the user-system dialogue. New user commands were added as APL functions. Ten of the forty-eight commands were requested by users, and several of the most complex ones were entirely defined by users.

2. AAIMS — an APL-based “personal information system” for analysis of 150,000 time series. The development was not based on a survey or user requirements, nor on any formal plan. New routines are tested and “proven” by a small user group.

3. IRIS — a prototype was built in five months and evolved over a one year period. An “Executive language” interface was defined as the base for the DSS and a philosophy was adopted of “build and evaluate as you go.”

4. CAUSE — There were four evolutionary versions. A phased development was used to build credibility. The number of routines was expanded from 26 to 200.

There have been several detailed studies of the time and the cost needed to build a DSS in APL. A usable prototype takes about three weeks to deliver. A full system requires another twelve to sixteen weeks. $^{2}$

End-user languages similarly allow fast development. One such DSS “generator” is Execucom’s IFPS (Interactive Financial Planning System), a simple, English-like language for building strategic planning models. The discussion below is based on a survey of 300 IFPS applications in 42 companies. $^{3}$ The models included long range planning, budgeting, project analysis, evolution of mergers, and acquisitions.

The average IFPS model took five days to build and contained 360 lines (the median was 200). Documented specifications were developed for only 16%. In 66% of the cases, an analyst simply responded to a manager's request and got something up and running quickly. Cost-benefit analysis was done for 13%, and only 30% have any objective evidence of "hard" benefits. 74% of the applications replace manual procedures.

$^{3}$ IFPS is a proprietary product of Execucom, Inc., in Austin, Texas. The survey of IFPS users is described in Wagner [19].

Given that most of the responding companies are in the Fortune 100, this indicates the limited degree to which managers in the planning functions make direct use of computers.

Most DSS are built outside data processing, generally by individuals who are knowledgeable about the application area. Table 2 gives figures on where requests for IFPS applications came from and how they are built.

The IFPS users were asked to identify the features of the language that contributed most to the success of the DSS. In order of importance, these are:

1. speed of response,

2. ease of use,

3. package features (curve-fitting, risk analysis, what-if?),

4. sensitivity analysis, and

5. time savings.

The evolutionary nature of DSS development follows from the reliance on prototypes and fast development. There is no “final” system. In most instances, the system evolves in response to user learning. A major difficulty in designing DSS is that many of the most effective uses are unanticipated and even unpredictable. Examples are:

1. PMS — the intended use was to facilitate a portfolio based rather than security based approach to investment. This did not occur, but the DSS was invaluable in communicating with customers.

Table 2. IFPS Development Process

<table><tr><td></td><td>Data Processing</td><td>Staff Analyst</td><td>Middle Management</td><td>Top Management</td></tr><tr><td>Who requested the application</td><td>0</td><td>4</td><td>30</td><td>66</td></tr><tr><td>Who built it</td><td>3</td><td>53</td><td>22</td><td>22</td></tr><tr><td>Who uses the terminal</td><td>0</td><td>70</td><td>21</td><td>9</td></tr><tr><td>Who uses the output</td><td>0</td><td>6</td><td>42</td><td>52</td></tr></table>

2. GPLAN — the DSS forced the users (engineers) to change their roles from analysts to decision makers.

3. PROJECTOR — the intended use was to analyze financial data in order to answer preplanned questions and the actual use was as an educational vehicle to alert managers to new issues.

Usage is also very personalized, since the managers differ in their modes of analysis and the DSS is under their own control. For example, six users of PMS studied over a six month period differed strongly in their choice of operators (see Table 3). $^{4}$

The benefits of DSS vary; this is to be expected given the complex situational nature of the tasks they support and their personalized uses. The following list shows those frequently cited in DSS case studies, together with representative examples. $^{5}$ Table 4 summarizes the list.

## 1. Increase in the Number of Alternatives Examined

\- Sensitivity analysis takes 10% of the time needed previously.

\- Eight detailed solutions generated versus one in previous study.

\- Previously took weeks to evaluate a plan; now takes minutes, so much broader analysis.

\- Users could imagine solutions and use DSS to test out hypotheses.

\- “No one had bothered to try price/profit options before.”

## 2. Better Understanding of the Business

\- President made major changes in company's overall plan, after using DSS to analyze single acquisition proposal.

\- DSS alerted managers that an apparently successful marketing venture would be in trouble in six month's time.

\- DSS is used to train managers; gives them a clear overall picture.

\- “Now able to see relationships among variables.”

Table 3. Relative Use of DSS Operators (PMS)

<table><tr><td colspan="7">percentage of use by each manager</td><td rowspan="2">percentage of use by all users</td></tr><tr><td>Operator</td><td>A</td><td>B</td><td>C</td><td>D</td><td>E</td><td>F</td></tr><tr><td>Table</td><td>22</td><td>22</td><td>38</td><td>22</td><td>76</td><td>57</td><td>47</td></tr><tr><td>Summary</td><td>40</td><td>10</td><td>30</td><td>8</td><td>0</td><td>38</td><td>17</td></tr><tr><td>Scan</td><td>0</td><td>26</td><td>5</td><td>24</td><td>0</td><td>0</td><td>4</td></tr><tr><td>Graph</td><td>14</td><td>4</td><td>13</td><td>30</td><td>5</td><td>0</td><td>8</td></tr><tr><td>Directory</td><td>2</td><td>0</td><td>0</td><td>0</td><td>1</td><td>4</td><td>1</td></tr><tr><td>Others</td><td>22</td><td>38</td><td>14</td><td>16</td><td>18</td><td>1</td><td>23</td></tr></table>

Table 4. DSS Benefits

<table><tr><td></td><td>Easy to measure?</td><td>benefit can be quantified in a “‘bottom line’” figure?</td></tr><tr><td>1. Increase in number of alternatives examined</td><td>Y</td><td>N</td></tr><tr><td>2. Better understanding of the business</td><td>N</td><td>N</td></tr><tr><td>3. Fast response to unexpected situations</td><td>Y</td><td>N</td></tr><tr><td>4. Ability to carry out ad hoc analysis</td><td>Y</td><td>N</td></tr><tr><td>5. New insights and learning</td><td>N</td><td>N</td></tr><tr><td>6. Improved communication</td><td>N</td><td>N</td></tr><tr><td>7. Control</td><td>N</td><td>N</td></tr><tr><td>8. Cost savings</td><td>Y</td><td>Y</td></tr><tr><td>9. Better decisions</td><td>N</td><td>N</td></tr><tr><td>10. More effective teamwork</td><td>N</td><td>N</td></tr><tr><td>11. Time savings</td><td>Y</td><td>Y</td></tr><tr><td>12. Making better use of data resource</td><td>Y</td><td>N</td></tr></table>

## 3. Fast Response to Unexpected Situations

\- A marketing manager faced with unexpected budget cut used the DSS to show that this would have a severe impact later.

\- Helped develop legal case to remove tariff on petroleum in New England states.

\- Model revised in twenty minutes, adding risk analysis; led to reversal of major decision made one hour earlier.

## 4. Ability to Carry Out Ad Hoc Analysis

\- 50% increase in planning group's throughput in three years.

\- The governor's bill was published at noon "and by 5 pm I had it fully costed out."

\- "I can now do QAD's — quick-and-dirties."

\- System successfully used to challenge legislator's statements within a few hours.

## 5. New Insights and Learning

\- Quickened management's awareness of branch bank problems.

\- Gives a much better sense of true costs.

\- Identified underutilized resources already at analysts' disposal.

MIS Quarterly/March 1981 - Allows a more elegant breakdown of data into categories heretofore impractical.

• Stimulated new approaches to evaluating investment proposals.

## 6. Improved Communication

\- Used in “switch presentations” by advertising agencies to reveal shortcomings in customer’s present agency.

\- Can explain rationale for decision to investment clients.

\- Improved customer relations.

\- “Analysis was easier to understand and explain. Management had confidence in the results.”

\- “It makes it a lot easier to sell (customers) on an idea.”

## 7. Control

\- Permits better tracking of cases.

\- Plans are more consistent and management can spot discrepancies.

\- Can “get a fix on the overall expense picture.”

\- Standardized calculation procedures.

\- Improved frequency and quality of annual account reviews.

\- Better monitoring of trends in airline's fuel consumption.

## 8. Cost Savings

\- Reduced clerical work.

\- Eliminated overtime.

\- Stay of patients shortened.

\- Reduced turnover of underwriters.

## 9. Better Decisions

\- “He was forced to think about issues he would not have considered otherwise.”

\- Analysis of personnel data allowed management to identify for the first time where productivity gains could be obtained by investing in office automation.

\- Increased depth and sophistication of analysis.

\- Analysts became decision makers instead of form preparers.

## 10. More Effective Team Work

\- Allowed parents and school administrators to work together exploring ideas.

\- Reduced conflict — managers could quickly look at proposal without prior argument.

## 11. Time Savings

\- Planning cycle reduced from six man-days spread over twenty elapsed days to one half day spread over two days.

\- “Substantial reduction in manhours” for planning studies.

\- “(My) time-effectiveness improved by a factor of 20.”

## 12. Making Better Use of Data Resource

\- Experimental engineers more ready to collect data since they knew it would be entered into a usable system.

\- "More cost-effective than any other system (we) implemented in capitalizing on the neglected and wasted resource of data."

\- Allows quick browsing.

\- "Puts a tremendous amount of data at manager's disposal in form and combinations never possible at this speed."

Table 4 adds up to a definition of managerial productivity. All the benefits are valuable but few of them are quantifiable in ROI or payback terms.

In few of the DSS case studies is there any evidence of formal cost-benefit analysis. In most instances, the system was built in response to a concern about timeliness or scope of analysis, the need to upgrade management skills, or the potential opportunity a computer data resource or modelling capability provides. Since there is little a priori definition of costs and benefits, there is little a posteriori assessment of gains. A number of DSS failed in their aims, but where they are successful, there is rarely any formal analysis of the returns. Many of the benefits are not proven. In managerial tasks there is rarely a clear link between decisions and outcomes, and a DSS can be expected to contribute to better financial performance, but not directly cause it. In general, managers describe a successful DSS as “indispensable” without trying to place an economic value on it.

## The Dynamics of Innovation

DSS are a form of innovation. They represent:

1. a relatively new concept of the role of computers in the decision process,

2. an explicit effort to make computers helpful to managers who on the whole have not found them relevant to their own job, even if they are useful to the organization as a whole.

3. a decentralization of systems development and operation, and often a bypassing of the data processing department, and

4. the use of computers for "value added" applications rather than cost displacement.

There is much literature on the dynamics of technical innovations in organizations. $^{6}$ Its conclusions are fairly uniform and heavily backed by empirical data.

Surveys of the use of computer planning models support these conclusions. In nine cases studied $^{7}$ the decision to adopt planning models was based on:

1. comparison with an ongoing system which involves examining either a manual or partially computerized system and deciding that some change is desirable,

2. comparison with a related system, such as a successful planning model in another functional area,

3. initiation of a low cost project, and

4. comparison with competitors' behavior resulting in the use of a “reference model” which reduces the need to estimate the impact of a model not yet constructed on improved decisions and performance.

Even in traditional data processing applications, the emphasis on value rather than cost is common. A survey of all the proposals for new systems accepted for development in a large multinational company found that even though cost-benefit analysis was formally required, it was used infrequently. $^{8}$ The two main reasons for implementing systems were:

1. mandated requirements, such as regulatory reports, and

2. identification of one or two benefits, rarely quantified.

Traditional cost-benefit analysis is effective for many computer-based systems. It seems clear, however, that it is not used in innovation. This may partly be because innovations involve R&D; they cannot be predefined and clear specifications provided. There is some evidence that there is a conflict in organizations between groups concerned with performance and those focused on cost. In several DSS case studies, the initiators of the system stress to their superiors that the project is an investment in R&D, not in a predefined product.

Surveys of product innovations consistently find that they come from customers and users rather than centralized technical or research staff. Well over three-quarters of new products are initiated by someone with a clear problem looking for a solution. $^{9}$ Industrial salesmen play a key role as “gatekeepers” bringing these needs to the attention of technical specialists. Even in the microprocessor industry, the majority of products are stimulated in this way by “demand-pull,” not by “technology-push.” $^{10}$

Case studies indicate that DSS development reflects the same dynamics of innovation as in other technical fields. Table 5 states the same dynamics of innovation as in other technical fields.

## Methodologies for Evaluating Proposals

There are three basic techniques used to evaluate proposals for computer systems in most organizations:

1. cost-benefit analysis and related ROI approaches — this views the decision as a capital investment,

$^{9}$ See Utterback [14].

$^{10}$ See von Hippel [15].

2. scoring evaluation — this views it in terms of weighted scores, and

3. feasibility study — this views it as engineering.

Each of these is well-suited to situations that involve hard costs and benefits, and that permit clear performance criteria. They do not seem to be useful — or at least used — for evaluating innovations or DSS.

Cost-benefit analysis is highly sensitive to assumptions such as discount rates and residual value. It needs artificial and often arbitrary modifications to handle qualitative factors such as the value of improved communication and improved job satisfaction. Managers seem to be more comfortable thinking in terms of perceived value and then asking if the cost is reasonable. For example, expensive investments on training are made with no effort at quantification. The major benefits of DSS listed in Table 4 are mainly qualitative and uncertain. It is difficult to see how cost-benefit analysis of them can be reliable and convincing in this context.

Scoring methods are a popular technique for evaluating large-scale technical projects, such as the choice of a telecommunications package, especially when there are multiple proposals with

## Table 5. Dynamics of DSS Innovation

<table><tr><td>Innovations are value-driven</td><td>Main motivation for DSS is “better” planning, timely information, ad hoc capability, etc.</td></tr><tr><td>Early adopters differ from late adopters</td><td>DSS are often initiated by line managers in their own budgets; once the system is proven other departments may pick it up.</td></tr><tr><td>Informal processes are central</td><td>DSS development usually involves a small team; key role of intermediaries knowledgeable about the users and the technology for the DSS; data processing rarely involved; frequently DSS are “bootleg” projects.</td></tr><tr><td>Cost is a secondary issue</td><td>Costs are rarely tracked in detail; DSS budget is often based on staff rather than dollars; little charge out of systems (this may reflect item below).</td></tr><tr><td>Uncertainty reduced by trialability, ease of understanding, clear performance value</td><td>Use of prototypes, emphasis on ease of use.</td></tr></table>

varying prices and capabilities. Scoring techniques focus on a list of desired performance characteristics. Weights are assigned to them and each alternative rated. For example:

<table><tr><td>characteristic</td><td>weight</td><td>alternative</td><td>weighted score</td></tr><tr><td>response time</td><td>.30</td><td>15</td><td>4.5</td></tr><tr><td>ease of use</td><td>.20</td><td>20</td><td>4.0</td></tr><tr><td>user manual</td><td>.10</td><td>17</td><td>1.7</td></tr></table>

Composite scores may be generated in several ways: mean rating, pass-fail, or elimination of any alternative that does not meet a mandatory performance requirement. Cost is considered only after all alternatives are scored. There is no obvious way of deciding if alternative A, with a cost of \$80,000 and a composite score of 67, is better than B, with a cost of \$95,000 and a score of 79.

Feasibility studies involve an investment to identify likely costs and benefits. They tend to be expensive and to focus on defining specifications for a complete system. They rarely give much insight into how to build it, and assume that the details of the system can be laid out in advance. DSS prototypes are a form of feasibility study in themselves. They are a first cut at a system. Some designers of DSS point out that Version "0" can be literally thrown away. Its major value is to clarify design criteria and establish feasibility, usefulness, and usability. The differences between a prototype and a feasibility study are important:

1. The prototype moves the project forward, in that a basic system is available for use and the logic and structure of the DSS already implemented.

2. The prototype is often cheaper, if the application is suited to APL or an end-user language.

3. The feasibility study is an abstraction and the prototype is concrete. Since DSS uses are often personalized and unanticipated, direct use of the DSS may be essential to establishing design criteria.

There is no evidence that any of these methods are used in evaluating DSS, except occasionally as a rationale or a ritual. More importantly, almost every survey of the dynamics of innovation indicates that they do not facilitate innovation and often impede it.

## Value Analysis

The dilemma managers face in assessing DSS proposals is that the issue of qualitative benefits is central, but they must find some way of deciding if the cost is justified. What is needed is a systematic methodology that focuses on:

1. value first, cost second,

2. simplicity and robustness. Decision makers cannot, and should not have to, provide precise estimates of uncertain, qualitative future variables,

3. reducing uncertainty and risk, and

4. innovation, rather than routinization.

The methodology recommended here addresses all these issues. It relies on prototyping which:

1. factors risk, by reducing the initial investment, delay between approval of the project, and delivery of a tangible product; and

2. separates cost and benefit, by keeping the initial investment within a relatively small, predictable range.

If an innovation involves a large investment, the risk is high. Since estimates of costs and benefits are at best approximate, the decision maker has no way of making a sensible judgment. Risk is factored by reducing scope. An initial system is built at a cost below the capital investment level; the project is then an R&D effort. It can be written off if it fails. By using the DSS one identifies benefits and establishes value. The designer is also likely to learn something new about how to design the full system. The prototype accomplishes the same things as a feasibility study, but goes further in that a real system is built.

The benefit of a DSS is the incentive for going ahead. The complex calculations of cost-benefit analysis are replaced in value analysis by simple questions that most managers naturally ask and handle with ease:

1. What exactly will I get from the system?

\- it solves a business problem,

\- it can help improve planning, communication, and control, and

\- it saves time.

2. If the prototype costs \$X, do I feel that the cost is acceptable?

Obviously the manager can try out several alternatives — “If the prototype only accomplishes two of my three operational objectives, at a lower cost of \$Y, would I prefer that?” The key point is that value and cost are kept separate and not equated. This is sensible only if the cost is kept fairly low. From case studies of DSS, it appears that the cost must be below \$20,000 in most organizations for value analysis to be applicable.

This first stage of value analysis is similar to the way in which effective decisions to adopt innovations are made. It corresponds to most managers' implicit strategy. The second stage is a recommendation; there is no evidence in the literature that it is widely used, but it seems a robust and simple extension of Version "0". Once the nature and value of the concept has been established the next step is to build the full DSS. The assessment of cost and value now needs to be reversed:

1. How much will the full system cost?

2. What threshold of values must be obtained to justify the cost? What is the likelihood they will occur?

If the expected values exceed the threshold, no further quantification is required. If they do not, then there must either be a scaling down of the system and a reduction in cost, or a more detailed exploration of benefits.

Value analysis follows a general principle of effective decision making — simplify the problem to make it manageable. A general weakness of the cost-benefit approach is that it requires knowledge, accuracy, and confidence about issues which for innovations are unknown, illdefined, and uncertain. It therefore is more feasible to:

1. Establish value first, then test if the expected cost is acceptable.

2. For the full system, establish cost first, then test if the expected benefits are acceptable.

Instead of comparing benefits against cost, value analysis merely identifies relevant benefits and tests them against what is in effect a market price: "Would I be willing to pay \$X to get this capability?" It is essential that the benefits be accurately identified and made operational. The key question is how would one know that better planning has occurred? The prototype is in effect an experiment in identifying and assessing it.

Figure 1 illustrates the logic and sequence of value analysis. The specific details of the method are less important than the overall assumptions, which have important implications for anyone trying to justify a DSS whether as a designer or user. Marketing a DSS requires building a convincing case. Figure 1 can be restated in these terms:

1. Establish value — the selling point for a DSS is the specific benefits it provides for busy managers in complex jobs.

2. Establish cost threshold — “trialability” is possible only if the DSS is relatively cheap and installed quickly. If it costs, say, \$200,000, it is a capital investment, and must be evaluated as such. This removes the project from the realm of R&D and benefits as the focus of attention to ROI and tangible costs and inhibits innovation.

3. Build Version "0" — from a marketing perspective this is equivalent to "strike while the iron is hot." Doing so is possible only with tools that allow speedy development, modification, and extension.

4. Assess the prototype — for the marketer this means working closely with the user and providing responsive service.

![](/api/attachments/G42CTTUR/fulltext/images/00c9c620758cf1075fb43e9fa548f00c821458c785c085469e518f9c4019ee91.jpg)  
Figure 1. Value Analysis

Two analogies for DSS have been mentioned in this article: the staff assistant and management education. The strategy used to justify DSS depends upon the extent to which one views such systems as service innovations and investments in future effectiveness as opposed to products, routinization, and investment in cost displacement and efficiency. The evidence seems clear — DSS are a potentially important innovation. Value is the issue, and any exploitation of the DSS approach rests on a systematic strategy for identifying benefits, however qualitative, and encouraging R&D and experimentation.

## References

[1] Alter, S. Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, 1980.

[2] Andreoli, P. and Steadman, J. “Management Decision Support Systems: Impact on the Decision Process,” Master's thesis, Sloan School of Management, Massachusetts Institute of Technology, 1975.

[3] Berger, P. and Edelman, F. "IRIS: A Transaction Based DSS for Human Resources Management," in Carlson, E.D., ed., "Proceedings of a Conference on Decision Support Systems," Data Base, Volume 8, Number 3, Winter 1977, pp. 22-29.

[4] Blanning, R. "How Managers Decide to Use Planning Models," Long Range Planning, Volume 13, April 1980.

[5] Carlson, E.D., ed. "Proceedings of a Conference on Decision Support Systems," Data Base, Volume 8, Number 3, Winter 1977.

[6] Carlson, E.D. and Sutton, J.A. “A Case Study of Non-programmer Interactive Problem Solving,” IBM Research Report, RJ13H2, San Jose, California, 1974.

[7] Ginzberg, M.J. “A Process Approach to Management Science Implementation,” Ph.D. dissertation, Sloan School of Management, Massachusetts Institute of Technology, 1975.

[8] Grajew, J. and Tolovi, J., Jr. "Conception et Mise en Oeuvre des Systems Interactifs

d'aide a la Decision: l'approche Evolutive," Doctorial dissertation, Universite des Sciences Sociales de Grenoble, Institut d'Administration des Entreprises, France, 1978.

[9] Haseman, W.D. "GPLAN: An Operational DSS," in Carlson, E.D., ed., "Proceedings of a Conference on Decision Support Systems," Data Base, Volume 8, Number 3, Winter 1977, pp. 73-78.

[10] Keen, P.G.W. “Decision Support Systems and Managerial Productivity Analysis,” paper presented at the American Productivity Council Conference on Productivity Research, Houston, Texas, April 1980.

[11] Keen, P.G.W. and Gambino, T. “The Mythical Man-Month Revisited: Building A Decision Support System in APL,” paper presented at the APL Users Meeting, Toronto, Canada, September 1980.

[12] Keen, P.G.W. and Scott Morton, M.S. Decision Support Systems: An Organizational Perspective, Addison-Wesley, 1978.

[13] Klaas, R.L. “A DSS for Airline Management,” in Carlson, E.D., ed., “Proceedings of a Conference on Decision Support Systems,” Data Base, Volume 8, Number 3, Winter 1977, pp. 3-8.

[14] Little, J.D.C. "BRANDAID," Operations Research, Volume 23, Number 4, May 1975, pp. 628-673.

[15] Sprague, R.H., Jr. “A Framework for the Development of Decision Support Systems,” MIS Quarterly, Volume 4, Number 4, December 1980, pp. 1-26.

[16] Tornatzky, L.G., et al. “Innovation Processes and Their Management: A Conceptual, Empirical, and Policy Review of Innovation Process Research,” National Science Foundation Working Draft, October 19, 1979.

[17] Utterback, J.M. "Innovation in Industry and the Diffusion of Technology," Science, Volume 183, February 1974.

[18] von Hippel, E. “The Dominant Role of Users in the Scientific Instrument Innovation Process,” Research Policy, July 1976.

[19] Wagner, G.R. “Realizing DSS Benefits with the IFPS Planning Language,” paper presented at the Hawaii International Conference on System Sciences, Honolulu, Hawaii, January 1980.

## About the Author

Peter G. W. Keen, Assistant Professor at the Sloan School of Management at M.I.T., received his DBA from Harvard University and has been on the faculties of the Harvard Business School, Stanford University, and the Wharton School at the University of Pennsylvania.

His publications include the first book in the Decision Support series, Decision Support

Systems: An Organizational Perspective with M.S. Scott Morton, and articles on cognitive style, implementation, design and development of DSS, and political aspects of data and software engineering. His current research includes a study of support systems for policy analysts in educational finance, funded by the Ford Foundation. He is a member of the editorial policy board and coordinator for the DSS area in a new journal, Human Systems Management.
