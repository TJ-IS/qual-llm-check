---
otero_id: 18187
otero_key: "MB5A2FDY"
title: "Decision support in a guaranteed student loan program: Design and implementation of a model-based system"
authors: "John B. Hill; William A. Wallace"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90059-x"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Decision Support in a Guaranteed Student Loan Program: Design and Implementation of a Model-Based System \*

John B. Hill

Project Coordinator, Criminal Justice Information Systems Improvement Project, NYS Division of Criminal Justices Services, Albany, NY 12203, USA

and

William A. Wallace

Professor and Chairman, Statistical, Management, and Information Sciences Department, School of Management, Rensselaer Polytechnic Institute, Troy, NY 12180, USA

The development and implementation of a model-based DSS is described in this paper. The DSS was designed to assist executives at a public agency in the administration of the Guaranteed Student Loan Program. The purpose of the paper is to illustrate that a model-based DSS is an effective alternative to building a mathematical optimization model. In addition, we propose a design methodology for developing such a model-based DSS on a personal computer.

Keywords: Decision Support Systems, Markovian Models, Higher Education, Microcomputer, Guaranteed Student Loan Programs

## 1. Introduction

## 1.1. Purpose

Interactive Decision Support Systems (DSS) are providing a viable alternative to complex mathe-

![](/api/attachments/MB5A2FDY/fulltext/images/e09cf9a8f7a1aee7b0a4fab08908cd0950990443f80bb2263e951fe388b87c08.jpg)

John B. Hill is currently pursuing a masters degree in public administration at the John F. Kennedy School of Government, Harvard University. For the last seven years he has worked in the MIS field. While with the State of New York, he has served as Director of Research for the Higher Education Services Corporation and as Systems Improvement Project Coordinator for the Division of Criminal Justice Services. Mr. Hill holds a bachelors degree in mathematics and a masters degree in operations research from Rensselaer Polytechnic Institute.

![](/api/attachments/MB5A2FDY/fulltext/images/682cf79a980925af4beff38583b9aca30f222d8fb8559224e3a757dde3bed298.jpg)

As a researcher and a consultant in Management Science and Information Systems, Professor Wallace has over 15 years experience in developing, implementing, and evaluating decision support systems for industry and government. He is presently engaged in research and development in the use of microcomputers as decision aids for emergency managers and in command and control settings. Professor Wallace has authored and co-authored 4 books and over 70 articles and papers. He

has held academic positions at Carnegie-Mellon University and the State University of New York at Albany, was a research scientist at the International Institute of Environment and Society, Science Center, West Berlin, Germany and a project engineer at Illinois Institute of Technology Research Institute, and is a Navy veteran. He was selected as a Visiting U.S. Faculty, Management Information Systems, Decision Support Systems, National Center for Industrial Science and Technology Management Development, Dalian, People's Republic of China. His research has been reported on by national and international media including Associated Press, Christian Science Monitor and Business Week. His educational background includes a B.Ch.E. from Illinois Institute of Technology and a Master of Science and Doctorate in Management Science from Rensselaer Polytechnic Institute.

matical optimization models as decision aids for executives. An optimization model is an abstraction of the executive's decision-making process. It is a mathematical formulation that specifies his or her objective function and the process he or she must manage. In a sense, the optimization model takes the executive out of the decision-making process.

An interactive DSS, on the other hand, acts as an extension of the executive's decision-making process of “human information processing system” [13]. It does not optimize the objective function; rather, it provides a computational tool that allows the executive to test quickly assumptions about which combination of the decision variables will increase the objective function. The DSS and the executive act together in a heuristic fashion, developing alternative solutions and then selecting the most appropriate one.

Another advantage of the DSS is its relative simplicity. The techniques of the mathematical optimization model are too complex for many executives to understand. An intermediate technical person would probably be required to go between the executive and the model, which probably would reside on a mainframe computer. This would also add a time factor that would further remove the executive from the decision-making process.

In contrast, a DSS is a “hands-on” aid for the executive. Requiring only a microcomputer, the DSS enables the executive personally and immediately to assess the impact of his or her decisions for a particular decision situation. Because it is less complex and more available than the optimization model, a DSS is more likely to be used by the executive and thus should lead to improvement in the quality of the executive’s decision making.

The DSS that are replacing optimization models are often referred to as model-based DSS. They generally incorporate a conceptual model or normative construct of the process or system that the executive must manage. An example of a model-based DSS is an interactive simulation of a customer service process. It contains a normative model of customer service (e.g., queueing model) that the executive can adjust interactively (e.g., change the number of cashiers) to project the impact on customer flow. Unlike an optimization model, this DSS does not tell the manager which configuration of cashiers will optimize flow. Rather, it provides the manager with a computational tool that quickly enables him or her to see the impact of alternative decisions.

This paper concerns the development and implementation of a model-based DSS. The DSS is intended to assist executives at a public agency in the administration of the Guaranteed Student Loan Program. As such, the DSS contains a normative model of student-loan repayment behavior and enables the executives to adjust various inputs to test their impact on the agency's financial reserves.

The purpose of the paper is two-fold: to illustrate in an actual case that a model-based DSS is an effective alternative to a mathematical optimization model and to propose a design methodology for developing such a model-based DSS on a personal computer.

## 1.2. The Setting

The Student Loan Financial Model was designed to address a critical need at the Higher Education Services Corporation (HESC), a state-chartered public agency that administers the federal Guaranteed Student Loan Program in New York State. Its purpose is to assist the agency's executives in projecting the level of the agency's reserve account necessary for administering the Guaranteed Student Loan Program in the future.

The administration of the loan program is a complicated scheme of state fiscal outlays and federal reimbursements. Together, these create severe cash-flow problems at HESC. Although New York State lending institutions actually make the loans to students, HESC must purchase all loans for which the student has defaulted on the repayment obligation. (In fiscal 1983, HESC purchased over \$57 million in defaulted loans.) HESC is then reimbursed by the federal government for the purchase of defaulted loans at a rate between 80% and 100% depending on the current ratio of defaulted loans to outstanding student loans. Further, HESC is entitled to retain 30% of the proceeds from collection efforts against the defaulted loans.

The purchase, reimbursement, and collection of defaulted loans are the major sources of income and expense for the reserve account at HESC. However, in addition to these items, all agency operating expenses are drawn from this account, and any surplus is invested to create an additional source of revenue. In fiscal 1983, the balance of the agency's reserve account was about \$30 million.

By the summer of 1984, there was a pressing need for a computerized decision aid at HESC. The federal Guaranteed Student Loan Program had experienced a roller coaster of growth and retrenchment over the preceding five years. The dollar value of loans outstanding to New York State students had grown from \$1.5 billion in 1978 to \$3.8 billion in 1982, but since 1982, the number of new loans disbursed had declined by over 21% from the preceding year. It was becoming increasingly difficult to estimate the level of the agency's reserve requirements necessary to purchase defaulted loans because of the chaotic growth in the program. The traditional method of “straight lining” reserve requirements based on historical demand was inadequate because of the huge number of loans that were disbursed in the late '70s and that were now entering repayment.

## 1.3. Choosing on Interactive DSS Approach

The executive's goal at HESC is to increase the balance of the agency's reserve account. For a particular fiscal period, the balance is defined as the sum of all income minus all expenses plus the remaining balance from the preceding period. The income and expense items are given in Table 1.

The purchase of defaulted loans places the greatest single demand on the reserve account. The income from default collections is the greatest single source of income. The executive can exercise a fair amount of control over these items. The executive can reduce the number of defaulted loans by increasing the agency's "default aversion efforts". (Default aversion is an activity whereby agency personnel call potential loan defaulters and essentially scare them into repayment.) The executive can increase income from default collections by hiring additional collectors or by selling de-

Table 1

<table><tr><td>Income Items</td><td>Expense Items</td></tr><tr><td>Default Collections</td><td>Default Purchases</td></tr><tr><td>Reinsurance from Federal Gov&#x27;t State Subsidy</td><td>Refund to Federal Gov&#x27;t Administrative Expenses</td></tr><tr><td>Investment Income</td><td></td></tr></table>

Formulation of Loan Program Executive's Objective Function

Objective Function:

(1) Maximize $B_{p} = B_{p - 1} + I_{p} - E_{p}$

where

$$
\alpha D _ {p - 1} = \alpha \left(\sum_ {j = 0} ^ {5 6} V _ {p - j - 1} d _ {j}\right) \tag {2}
$$

and

$$
(3) \beta C _ {p} = \beta \left(\sum_ {n = 0} ^ {5 6} d _ {n} D _ {p - n}\right),
$$

therefore

(4) $I_{p} = \alpha D_{p - 1} + \beta C_{p} + S_{p} + \gamma \beta_{p - 1};$

(5) $D_{p} = \sum_{j = 0}^{36}V_{p - j}d_{j};$

$$
(1 - \beta) C _ {\rho} = (1 - \beta) \left(\sum_ {n = 0} ^ {5 6} c _ {n} D _ {p - n}\right);\tag{6}
$$

therefore

(7) $O_{p} = \epsilon C_{p} + \eta D_{p} + K_{p}$ ;

(8) $E_{p} = D_{p} + (1 - \beta)C_{p} + O_{p}$ .

Combining the above and letting $\theta = (2\beta - 1 - \epsilon)$ , the objective function can be expressed as

$$
\begin{array}{l} B _ {p} = (1 + \gamma) B _ {p - 1} + \alpha \left[ \sum_ {j = 0} ^ {5 6} V _ {p - 1, j - 1} d _ {j} \right] \\ + \theta \sum c _ {n} \left[ \sum_ {j = 0} ^ {5 6} V _ {p - j} d _ {j} \right] \\ + S _ {p} - (1 + \eta) \left[ \sum_ {j = 0} ^ {5 6} V _ {p - j} d _ {j} \right] - K _ {p}. \end{array}\tag{9}
$$

The objective of the loan executive is to maximize this equation, subject to

$$
\sum_ {j = 0} ^ {5 6} c _ {j} \leq 1, \sum_ {j = 0} ^ {1 5} d _ {j} \leq 0. 5 \text {   and   } c _ {j}, d _ {j} \geq 0.
$$

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
$B_{p} =$ reserve acct balance in period $p$ $I_{p} =$ income in period $p$ $E_{p} =$ expense in period $p$ $C_p =$ income from collections   
$S_{p} =$ state subsidy   
$K_{p} =$ fixed costs   
$D_{p} =$ default purchases   
$O_{p} =$ variable operating exp.   
$V_{p} =$ volume of loans disbursed   
$d_{j} =$ portion of loan volume in default $j$ periods after disbursal   
$c_{j} =$ portion of defaults collected in period $p$ $\alpha =$ portion of default purchases reinsured   
$\gamma =$ average rate of interest   
$\beta =$ portion of default collections kept by the agency   
$\epsilon =$ unit cost of collection   
$\eta =$ unit cost of aversion
</div>

Table 3

faulted accounts to an aggressive collections agency. These two variables are the decision variables in the executive's objective function.

Although it was possible to construct and solve a mathematical optimization model for this situation and presented in Table 2, an interactive DSS was considered the better choice. In addition to the advantages cited in section 1.1, a consideration of the executive's "cognitive style" led to the selection. Benbasat and Taylor [3] conclude that the executive's cognitive style affects the type of decision aid he or she prefers. Executives with an "analytic" style are more apt to rely on complex mathematical models than are "heuristic" style executives, who prefer to use a trial-and-error approach to decision making. The HESC executive who would be the primary user of the decision aid is clearly a heuristic decision maker. His decision style is one of reviewing an enormous amount of data and then formulating a solution through intuition and instinct. Further, this executive had rejected implementation of a mathematical model on a previous occasion. He had ignored a regression model to project volume of loan defaults [5] because he "didn't feel comfortable" with the projections it gave.

## 2. Developing the Interactive DSS

The development of a DSS typically lacks a clear, comprehensive plan at the beginning of the development process. Keen [12] suggests that the development process for DSS is amorphous for the following reasons:

1. The user does not know exactly what he or she wants at the beginning of the process;

2. The designer does not know what the user needs or expects;

3. The user's information needs will be shaped by the DSS;

4. Two different users will have different information needs for the same decision setting.

For these reasons, the development strategy needed for a DSS is not as structured as traditional systems analysis. Rather, an iterative process is employed that relies heavily on the relationship between the designer and the user to focus the design through successively more appropriate models of the system. The accepted wisdom, consistent with empirical results, is that high levels of user involvement are associated with higher probabilities of systems success [2,4].

For a high level of user involvement to be maintained throughout the development process, two conditions must be met:

1. The user must see results quickly. Both Ness [11] and Gambino [6] suggest that the first version of a DSS be delivered in weeks, not months. If it is several months before the user sees any tangible progress, his or her initial enthusiasm – and hence involvement – will fade;

2. The user must have real, "hands-on" responsibilities in the development process. To remain interested and involved, the user must have a stake in the project. The user must have a role where he or she (not only the designer) can make recommendations that will modify the design of the DSS.

## 2.1. The Evolutionary Development Approach

Both Keen [8] and Sprague [12] agree that the evolutionary development approach makes optimal use of user involvement and thus is best suited for DSS development. In a statistical study of user satisfaction, Alavi and Henderson [1] found that the evolutionary approach was the most likely to produce a successful DSS.

For these reasons, the evolutionary approach was chosen to develop the Student Loan Financial Model. But there were other factors suggesting that this was the correct choice. First, the model was to reside on a microcomputer, which would allow the rapid development of successive versions of the DSS. Second, the user of the DSS has a “hands-on” management style and a keen interest in microcomputers; he was very willing to be a part of the development process. Finally, there was a real need to get some kind of DSS, no matter how crude, operational in a short period of time to be able to prepare the agency’s budget.

Various models for the evolutionary approach to DSS development are found in the literature [2,8,11,12,13]. For developing the Loan Model, a composite of the salient features recommended in those articles was used and is summarized in Table 3.

The Evolutionary Development Approach

<table><tr><td> $\uparrow$  →</td><td>1. Design Man/Machine Interface2. Design Conceptual Model</td></tr><tr><td>6. Revise</td><td>3. Define Data Requirements4. Program System</td></tr><tr><td> $\uparrow \leftarrow$ </td><td>5. Obtain User Feedback</td></tr></table>

## 2.2. Designing the Man / Machine Interface

The most distinguishing feature of a DSS is that it is designed to be “user friendly” and interactive with the user. This aspect of a DSS is designed first because this is the mechanism through which the user gets information from the system. It defines the scope and extent to which the DSS supports the user’s decision process.

The Student Loan Financial Model (or Loan Model, as it came to be called) was to be used by only two executives at HESC: the Vice President and the Assistant Vice President in charge of the loan program. Both were currently using crude pencil-and-paper spreadsheets for projecting reserve account requirements. These spreadsheets were the starting point for the design of the man/machine interface. The final report or display of the Loan Model was to be a table that represented a single summary spreadsheet for the agency's reserve account.

Discussions with the executives led to a refinement in the man/machine interface. They agreed that the model should have an interconnected series of tables with more detailed data that supported the summary spreadsheet. For example, the item “default collections” should be the bottom line of a detailed table that presented the income stream from default collections by date of purchase and date of collection. Similarly, that table should be the summation of yet another, more detailed table.

## 2.3. Designing the Conceptual Model

This discussion not only advanced the design of the man/machine interface but also outlined the conceptual model of the DSS. The conceptual model embodies the manager's normative model of the process he manages. It enables the DSS to be a computerized extension of the user's thought process.

At HESC, the Loan Model was to appear to the user as a series of tables of actual and hypothetical data that were interconnected to a final spreadsheet. The interconnections between the tables were to be the mathematical assumptions that could be modified by the user. This model, interestingly enough, was conceived with the use of Lotus 1–2–3 in mind. The executives were already using Lotus 1–2–3 and were familiar with the concept of electronic spreadsheets.

Within two days of the first discussion, a conceptual model was developed that used Lotus 1–2–3 software. The model had data tables interconnected as in Table 4. The arrows connecting the tables were to be mathematical formulas that would calculate the values on one table from the data on another. For example, the connection between the “Loans Entering Repayment” table and the “Defaults Purchased” table could be expressed “X% of the loans entering repayment in 1983 will be in default in 1987”. The value of X could be modified by the user.

The conceptual model was presented to the executives as a series of hand-written tables juxtaposed to show their interconnection. This presentation sparked a significant refinement in the conceptual model. One of the executives quickly acknowledged that the mathematical relationships connecting the tables were stable with respect to time. For example, he claimed that if 14% of the dollar value of loans disbursed in 1980 was in default in 1984, it is then safe to assume that 14% of the dollar value of loans disbursed in 1981 will be in default in 1985. This led to the conceptualization of the Loan Model as a stochastic process with the formulation of Table 5.

## 2.4. Defining Data Requirements

The conceptual model of the decision setting largely defines the data requirements of the DSS. The initial input to the HESC model is aggregate data on the dollar amount of loan disbursals for each fiscal year between 1973 and 1993. Projected loan disbursal volumes for future years are available to the HESC executives from another model that considers trends in the college-age population and loan eligibility requirements. The “Historical Transition Rates” table is simply a matrix of proportions representing the expected distribution of loan amounts by the six loan statuses (i.e., in school, grace, deferment, repayment, default, amortized) for each of the 15 years after disbursal. These proportions are developed by the user from historical experience. The application of this matrix against the “Loan Disbursal Volume” table yields the projected dollar amounts in each of the six loan statuses. Of particular concern, of course, is the projected dollar amount of loans in default.

<table><tr><td colspan="2">Table 4Data Flow in First Version of Model</td></tr><tr><td>Reserve Account Spreadsheet↑</td><td>Default Collections</td></tr><tr><td>Defaults Purchased↑</td><td></td></tr><tr><td>Loans Entering Repayment↑</td><td></td></tr><tr><td>Loan Disbursal Volumes</td><td></td></tr></table>

Table 5  
Data Flow Model of Student Repayment Process

<table><tr><td colspan="3">A. Loan Aging Process</td></tr><tr><td>Historical and Estimated</td><td>× Transition Rates</td><td>Projected Loan Amounts in Repayment, Default, Grace, Amortization, etc.</td></tr><tr><td>Loan Disbursement Volume</td><td></td><td></td></tr><tr><td colspan="3">B. Collections Process</td></tr><tr><td>Projected Loan Amount in Defa-lault</td><td>× Collection Rates</td><td>Projected Income From Default Collections</td></tr></table>

A subsequent calculation performed by the Loan Model is the projection of the income stream expected from collections of defaulted loans. To do this, a matrix of collection probabilities is maintained that represents the proportion of a defaulted loan that HESC expects to collect during each of the 15 years following its purchase. This matrix is multiplied against the projected dollar value of loans in default.

This conceptual design dictated the functional design of the model. To support the conceptual design, the Loan Model had to perform the following functions:

1. Data Maintenance: the maintenance by the user of the data tables on loan disbursal volumes, transition rates, and collection probabilities. These data are actually the assumptions that the executives wish to test.

2. Projection: the multiplication and manipulation of these data to yield the projected reserve account requirements of the agency.

With this rough, functional design, programming of the Loan Model began.

## 2.5. Programming the System

The new conceptual model precluded the use of spreadsheet software. Moreover, during the design process, the expectations of the HESC executives had been raised to expect a more customized and elaborate system than Lotus 1–2–3 could provide. Thus, the programming was done in BASIC, a language better suited to matrix manipulation.

The programming began without documentation or program specification. The conceptual model and man/machine interface dictated a model with the following functional characteristics:

\- Data Files To Be Maintained by the User
● Historical and Projected Loan Disbursal Volumes

● Historical Default Purchases

● Loan Status Transition Rates

● Default Collection Probabilities

● Reinsurance, Subsidy, and Investment Parameters

\- Output Tables To Be Provided to the User
  ● Projected Loan Amounts by Status

● Projected Income from Default Collections

● Projected Reserve Account Spreadsheet

The lack of a complete systems design and a strong desire to build in as much flexibility as possible led to the adoption of a modular programming technique. Each of the eight subfunctions is performed by a separate BASIC module with data passed between modules as a disk file. The user can select which function he wishes to perform by entering a selection on a menu. All program modules are “chained” to the menu. Once the user selects a function, the user communicates with the Loan Model through a question-and-answer dialogue. The Loan Model communicates its answer to the user through numerical tables on the CRT. The first version of the Loan Model was programmed in about four weeks and presented to the users.

## 2.6. Obtaining User Feedback and Revising

The executives at HESC became familiar with the Loan Model by “walking through” each of its functions. Their initial reaction was favorable, but after about an hour of use, they voiced the following criticisms:

1. The Loan Model is too slow.

```txt
I. Develop Conceptual Model
1. Define Scope and Purpose of DSS
2. Outline Final Products of DSS
3a. Define Input Parameters to DSS
3b. Define Mathematical Formulas of Conceptual Model
4. Outline Intermediate Products of DSS
5. Obtain User Feedback and Revise
II. Develop Operational DSS
1. Define Data Requirements
2. Program Model
3. Obtain User Feedback and Revise
```

2. There is no way for the user to distinguish between actual and projected data.

3. The output tables are too crowded with data.

4. The question-and-answer dialogue gives no indication of the range of valid options.

5. The reserve account spreadsheet has incorrect entries.

6. The sequence by which the modules must be performed assumes some familiarization on the part of the user.

7. There is a need to explain to the user how the model works.

These comments lead to significant reprogramming of the Loan Model. The revised version was completed in about two weeks. During this period, the executives continued to user the first version of the Loan Model.

## 2.7. The Second Operational Version of the Loan Model

The second version of the model incorporated improvements for all of the problems identified by the executives. In sum, the Loan Model was changed so that the user needed no additional training, only an understanding of loan program administration. The model employed several “help” screens that assisted the user at various points during the model’s execution. All question-and-answer dialogue was supplemented with the range of options from which the user could select. Graphics, such as reverse video and high intensity, were used to increase the effectiveness of the output tables. The calculations of the model were streamlined to reduce the time the user spent waiting for a response.

## 2.8. The Second User Review

To test the Loan Model under actual conditions, it was given to the executives at HESC for their use without any assistance. After about six weeks of actual use, the second user review was conducted. The review indicated that the users were using all features of the model. Feedback from them took the form of suggestions or recommendations rather than complaints or criticisms, as was the case during the first review. Primarily, their suggestions concerned streamlining the model so that they could jump easily from one function to another. The final structure of the model is given in the Appendix.

## 3. A Revised DSS Development Approach

## 3.1. Introduction

The development of the Loan Model attempted to follow the evolutionary methodology presented earlier. However, the unique nature of the Loan Model and the development environment resulted in modifications to this approach since:

1. The Loan Model is highly computational in nature. As a result, the design of the conceptual model of student repayment behavior is the most critical in the entire development process.

2. The user had a very clear sense of the purpose of the model. He knew exactly what he needed as output and how he would use it.

For these two reasons, the user was not overly concerned with the man/machine interface nor did he have to be subtly led by the designer to specify the outputs of the DSS. Rather, the development process focused immediately on the design of the conceptual model.

The development process that was actually followed for the Loan Model is probably generalizable to the development of any model-based DSS. This revised development process is clearly evolutionary in nature but places increased emphasis on the design of the conceptual model before programming begins. The reason for this is simple: the conceptual model of a model-based DSS is invisible to the user. It is better represented through schematics and mathematical formulas. And because the conceptual model largely dictates the

1. Use of the Loan Model
A. How many hours per week do you use the model?
B. Do you expect that this level of use will change in the future?
2. Cost Effectiveness of the Loan Model
A. Is the Loan Model replacing any operations that you or your staff previously performed by hand? If so, how difficult or time-consuming were these manual operations?
B. Do you expect that the model will cause HESC management to make a decision that will result in a dollar savings for the agency or any of its clients?
3. User Satisfaction with the Loan Model
A. Have you personally benefitted from the model?
B. Are you satisfied with the model?
C. Have you become dependent on the model?
D. Do you think the model is important to HESC?
4. Management Change as a Result of the Loan Model
A. Specifically, have you used this model to make a decision? If so, which decision? Would you have decided otherwise without the model?
B. Are you presently collecting data to refine the data tables of the model?
C. Do you see the need for another model at HESC?

functional structure of the DSS, these representations of the conceptual model should be reviewed first. The revised development approach appears in table 6. Each of the two components in the revised approach has its own final product (for the first, a conceptual model; for the second, an operating DSS), and each is enclosed by a review loop with the user. For this reason, they can be viewed as two distinct and separate processes in the overall development process.

## 3.2. Developing the Conceptual Model

As stated earlier, the conceptual model is of critical importance in a model-based DSS. It is the framework or perspective from which the user views the decision setting. For example, the executives of HESC viewed the student loan program as a stochastic process where loan recipients move from one loan status (e.g., in repayment) to another (e.g., in default). This conceptualization was not agreed to immediately; it took a series of iterations with the user and the designer working as a team and doing the steps in Part I of Table 6.

In the case of the Loan Model, the first two steps were performed almost instantaneously. The user had a clear sense of the role of the DSS and how the output should appear. However, the user had little idea of the inputs to the DSS and of how the DSS should project the agency's future reserve account requirements. To accomplish steps three and four, therefore, the designer would propose the conceptual model to the user as a hand-drawn schematic and the user would make an in-depth critique of it. This process was repeated about three times.

It is important to note that each iteration took about three days and that, in each case, the proposed conceptual model was presented in terms of how the final DSS would appear to the user. For example, one of the early conceptual models was presented to the user as a series of “mocked up” spreadsheets showing how and where the user would interact with the DSS. This type of “hands on” presentation of conceptual material served to spark a user-designer dialog that led to further refinements.

## 3.3. Developing the Operational DSS

The steps followed for implementing the operational DSS (see Part II of Table 6) very closely followed the steps of the traditional evolutionary approach. Because the conceptual model was already well-defined prior to the beginning of programming, these series of steps served primarily to refine the man/machine interface of the DSS. For example, in the case of Loan Model, “help screens” and refinements in the question-and-answer dialogue resulted from this process. No changes, however, were made to the conceptual model of the Loan Model.

## 3.4. Summary

Keen and Scott-Morton [10] suggest that in the development of a DSS, the design and implementation processes are concurrent and thus are often indistinguishable from one another. The experience with the Loan Model indicates that for a certain type of DSS, this may not be true. In the case of a model-based DSS, the design of the conceptual model may—and probably should—take place prior to any implementation activity. This is because the conceptual model is complex and is best presented to the user in a schematic or graphical form that relates the mathematical formulation of the conceptual model to the user

## Table 7 DSS Evaluation Questionnaire

interface. When the conceptual model is programmed and presented to the user in the form of an operating DSS, the actual mathematical formulation of the conceptual model is often obscured.

## 4. Evaluation of the Student Loan Financial Model

To determine the success of the Loan Model at HESC, an evaluation interview was held with the two executive users/sponsors of the model six weeks after the first operational version of the model was supplied to HESC. (The questions they were asked are shown on Table 7) In those six weeks, the executives had taken several steps to install the model and test its applicability to loan program administration:

1. They had learned how to use the model and had uncovered a few obscure “bugs”, indicating they were using all features of the model.

2. They had installed the model on a new microcomputer in the agency's Finance Department and had made one junior-level accountant responsible for maintaining it.

3. They had shown the model to loan executives from other states (e.g., Michigan) as well as from New York's major student-loan lending institutions (e.g., Citibank).

The executives' answers to the evaluation questions were based on that six-week experience. Their responses are summarized in sections 4.1–4.4. Although anecdotal in nature [9], the evaluation process did provide insights into the value of the development process and the resulting DSS.

## 4.1. Patterns of Use

Although the use of the model had not stabilized, a usage pattern could be seen. The accountant from the Finance Department foresaw that he would be using the model for a four-hour period once a month to prepare the monthly financial report of the loan program. In this report, he must estimate the reserve account requirements for the remainder of the fiscal year. The executives are using the model on an “as needed” basis in order to test policy scenarios. As expected, for these uses the executives are using the model themselves and are not asking the accountant to perform the run.

## 4.2. Cost Effectiveness

The Loan Model has radically changed the manner by which HESC projects the reserve account requirements. Previously, one accountant worked full time to perform manually the calculations now performed by the model. He is now responsible for maintaining and operating the model and, because of the resultant time savings, is now able to perform other tasks. Therefore, some portion of his salary has been saved as a result of the model. However, this saving is probably offset by the programming and clerical effort now required to prepare the data tables of the model.

A far more significant dollar savings that may result from the model will be enjoyed by the state's student-loan recipients. Presently, New York State loan recipients pay a 0.5% surcharge (about ten dollars) to HESC at the time of loan disbursal to offset the cost of future loan defaults. The amount of this surcharge is determined by the agency's Board of Directors within limits set by the federal government. Although the loan executives at HESC had always suspected that the rate of this surcharge was unnecessarily high, they plan to use the model to justify their recommendation to reduce the rate of this surcharge to 0.25%. The total resultant dollar savings for all loan recipients will be about \$5 million per year. Even with the cost of the design, at this rate of savings, the project would prove cost effective by the third quarter of the first year.

## 4.3. User Satisfaction

One of the executives summarized his attitude toward the model as, “It opens new doors”. He meant, of course, that it enables him to analyze policy alternatives that he had previously been unable to consider. His satisfaction with the model is evident by his willingness to promote the model to loan agencies in other states. In January of 1985, he presented the model to the National Conference of Higher Education Loan Programs.

## 4.4. Management Change

Besides enabling the executive to analyze policy alternatives that he had previously been unable to consider, the DSS is being used to assist decisions concerning the daily operations of the agency. For example, the executives at HESC are beginning to use the volume projections of the model to project future manpower needs in the agency's certification, aversion, and default units.

Another indicator of management change as a result of the model is the effort that the agency has expended to make the model accurate. HESC has recently undertaken a sizable programming and clerical effort to collect data for the transition-rate and default-collection-rate tables of the model. To estimate these data, the agency is conducting a sample analysis of a cohort of loan recipients over a 15-year span.

## 5. Conclusion

The designer of a decision aid may have a choice between a complex mathematical optimization model and a model-based DSS. The experience at HESC has indicated that the model-based DSS can be the more effective alternative. The DSS can be developed quickly on a microcomputer using standard software. Further, it can be designed to be interactive with the executive so that it becomes an extension of his or her own decision-making process, because it can project quickly the future impact of the decisions the executive is considering. In this manner, the executive and the DSS can act together in a heuristic manner to find the “best” solution from the set of alternatives.

At HESC, the executives quickly incorporated the DSS into their decision-making process. The reasons for this were simple: the DSS was easy to use, and the executives had played an active role in its design and fully understood the normative model of the student repayment process that it contained. This probably would not be the case for a mathematical optimization model. Such a model would be far more complex and more difficult to use, and the executives would have played a far less significant role in its design.

Because a model-based DSS contains a normative model of the process that the executive is managing (in the case of the Loan Model, it was student repayment behavior), it provides an excellent framework for structuring the executive's objective function as an optimization problem. Optimizing features can be built into the model-based

DSS through the same evolutionary manner that was successful in producing the first version of the Loan Model. The result will be an optimization model that the executive will incorporate into his decision-making process.

The true measure of success of any management science technique is the extent to which it is used by the manager. Ginzberg [7] reported that mathematical optimization models are frequently not used by the manager because they are to complex, too difficult to use, and too rarely understood by the decision maker. The experience with the Loan Model at HESC shows that a model-based DSS does not suffer from these problems. A DSS can be developed that a manager will integrate into his or her decision-making process. Although the model-based DSS does not provide the optimum solution for the manager, it can later be enhanced to include optimizing features similar to a mathematical model. In this manner, the implementation of a model-based DSS can be viewed as an evolutionary process with two phases. During the first phase, the model-based DSS serves only as a computational tool that the manager uses to project the impact of alternative decisions. In the second phase, the DSS is enhanced to optimize and actually to select a decision for review by the manager.

## Appendix

## The Formulation of the Repayment Process

The student loan program can be thought of as a stochastic process for the purpose of the Loan Model because a student loan can exist in only a finite number of states which are mutually exclusive and exhaustive. There are six states, and they are generally referred to as “loan statuses”. The definition of the loan statuses is

In School --The student is currently enrolled in college and thus is not required to begin repayment.

Grace -The student has left school within the last six months and thus is not required to begin repayment.

Deferment -The student has joined the Armed Forces or the Peace Corps and thus is not required to begin repayment.

Repayment -The student is currently repaying the loan according to the original conditions of the agreement.

Default -The student has failed to meet the repayment obligations delineated in the original loan agreement.

Paid-in-Full -The student has paid completely all principal (Amortized) and interest of the student loan.

This formulation can be made to exhibit Markovian properties if the above statuses are further partitioned with regard to year-in-status. For example, if “Deferment” is split into D1, D2, D3, and so on, where D2 is the second year in deferment status, the probability of any future event is dependent only on the current loan status.

The executives at HESC acknowledged that the transition probabilities between statuses are stationary with respect to time. Therefore, we construct a vector S so that $\Sigma_{i=1}^{6}S_{ij}=1$ . Such a vector for j=3 may appear as follows.

<table><tr><td>In School</td><td>0.52</td></tr><tr><td>In Grace</td><td>0.05</td></tr><tr><td>Deferment</td><td>0.01</td></tr><tr><td>Repayment</td><td>0.32</td></tr><tr><td>Default</td><td>0.06</td></tr><tr><td>Paid-in-Full</td><td>0.04</td></tr></table>

This vector indicates that three years after disbursal, 52% of the value of the loans disbursed is held by students still in school and 6% is in default. In Loan Model, 15 of these vectors, for j equals 0 to 14, are assembled into a matrix P, improperly referred to as the “Transition Matrix”. This matrix is created and maintained by the user from data extracted from the student loan database at HESC.

With the matrix P, the following calculation can be performed to project the value of all loans in default in year Y:

$$
D _ {Y} = \sum_ {j = 0} ^ {1 4} V _ {Y - j} P _ {j},
$$

where $V_{Y}$ equals volume of loans disbursed in year Y. Therefore, the projected value of defaulted loans purchased by HESC in year Y is $D_{Y}.D_{Y-1}$ .

To calculate the projected income for default collections, the following vector of proportions is maintained by the user: $\left[c_{0},c_{1},c_{2}\ldots c_{j}\ldots c_{14}\right]$ ,

where $c_{j}$ equals dollars collected j years after purchase, as percent of volume purchased.

Therefore, the projected income from collections from all defaulted loans is:

$$
I _ {Y} = \sum_ {j = 0} ^ {1 4} c _ {j ^ {\prime}} \left[ D _ {Y - 1} - D _ {Y - j - 1} \right],
$$

The calculations presented here have been simplified for the sake of clarity. In the Loan Model, an additional dimension exists for all matrices. That dimension is the type of school that the student attends, know as institutional sector (i.e., vocational school, community college, four-year college, graduate school). This dimension was added because student repayment and default behavior differ quite widely among the four sectors.

## References

[1] Alavi, M. and Henderson, J., "Implementing a Decision Support System", Management Science, Volume 27, Number 11, 1981, pp. 1309–1323.

[2] Alter, S.L., Decision Support Systems: Current Practice and Continuing Challenges, Addison-Wesley, Reading, MA, 1980.

[3] Benbasat, I. and Taylor, R.N., “The Impact of Cognitive Styles on Information Systems Design”, MIS Quarterly, June 1978, pp. 43–54.

[4] Burch, J. and Strater, F., "Information Systems: Theory and Practice", John Wiley and Sons, New York, NY, 1979.

[5] Faris, N., “Budgetary Forecasting Model for Defaulted Loans Purchased”. Paper developed for Higher Education Services Corporation, Albany, NY, June 1982.

[6] Gambino, T.J., “Building Decision Support Systems: The Mythical Man-Month Revisited”, in J.L. Bennett (ed.), Building Decision Support Systems, Addison-Wesley, Reading, MA, 1983, pp. 133–172.

[7] Ginzberg, M.J., “Finding an Adequate Measure of OR/MS Effectiveness”, Interfaces, Volume 8, Number 4, 1978, pp. 59–62.

[8] Keen, P.G.W., “Decision Support Systems: A Research Perspective”, In G. Fick and R.H. Sprague (eds.), Decision Support Systems: Issues and Challenges, Pergamon Press, Elmsford, NY, 1980, pp. 23–44.

[9] Keen, P.G.W., “Computer-based Decision Aids: The Evaluation Problem”, Sloan Management Review, Spring 1975, pp. 17–29.

[10] Keen, P.G.W. and Scott-Morton, M.S., Decision Support Systems: An Organizational Perspective, Addison-Wesley, Reading, MA, 1978.

[11] Ness, D., “Interactive Systems: Theories of Design”, Joint Wharton/ONR Conference, University of Pennsylvania, 1975.

[12] Sprague, R.H., “A Framework for the Development of Decision Support Systems”, MIS Quarterly, December 1980, pp. 1–26.

[13] Zmud, R.W., Information Systems In Organizations, Scott, Foresman and Company, Glenview, IL, 1983.
