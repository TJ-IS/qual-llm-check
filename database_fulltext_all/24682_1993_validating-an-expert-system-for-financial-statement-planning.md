---
otero_id: 24682
otero_key: "8PFPV7NV"
title: "Validating an Expert System for Financial Statement Planning"
authors: "Barbro Back"
year: "1993"
journal: "Journal of Management Information Systems"
doi: "10.1080/07421222.1993.11518015"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Validating an Expert System for Financial Statement Planning

Barbro Back

To cite this article: Barbro Back (1993) Validating an Expert System for Financial Statement Planning, Journal of Management Information Systems, 10:3, 157-177, DOI: 10.1080/07421222.1993.11518015

To link to this article: https://doi.org/10.1080/07421222.1993.11518015

![](/api/attachments/8PFPV7NV/fulltext/images/15073c117e0604285d19a11b25ac3d1c561a3d71b9269e18057f30f0ab581881.jpg)

Published online: 15 Dec 2015.

![](/api/attachments/8PFPV7NV/fulltext/images/4f86cf1b8f22209d3eb03744fbc62729c00b0942e3ee41cca6d76984b6ee18f0.jpg)

Submit your article to this journal ↗

![](/api/attachments/8PFPV7NV/fulltext/images/bb0f8a77bcd9faab599482bb53a39b30bb8a1d24df597b356feda4e62a08166e.jpg)

Article views: 3

![](/api/attachments/8PFPV7NV/fulltext/images/8f3722ea43f2189896c58f6a30a180a2379e1f2f879f33e90e8c6eee9ce22c1a.jpg)

View related articles ↗

![](/api/attachments/8PFPV7NV/fulltext/images/78afaaf25d119e864832566b7f445961298666c4c96d122b52df49bd55305bc8.jpg)

Citing articles: 4 View citing articles ↗

# Validating an Expert System for Financial Statement Planning

BARBRO BACK

BARBRO BACK is acting Associate Professor in Information Systems at Turku School of Economics and Business Administration, Turku, Finland. She received her Ph.D. in accounting from Åbo Akademi University, Turku, Finland, and an M.S. in business administration from the Swedish School of Economics and Business Administration, Helsinki. Prior to her current position she spent a year as Visiting Scholar at the University of Southern California, School of Accounting. Her research interests include accounting information systems, expert systems, decision support systems, and neural networks.

ABSTRACT: Validation is often considered the cornerstone of expert systems evaluation. Validating expert systems has, however, turned out to be a difficult task because an expert system is often both a piece of software and a model. The general procedures for validation of traditional software cannot, therefore, usually be followed when validating an expert system. This article shows how the validation of a concrete full-scale expert system for financial statement planning was conducted, utilizing guidelines on validation of expert systems given in literature and incorporating them into the classical spiral model used in developing the system.

KEY WORDS AND PHRASES: expert systems, financial statement planning, validation.

AN EXPERT SYSTEM'S VALUE CAN BE DETERMINED THROUGH VERIFICATION, validation, and usability evaluation. The focus here is on the validation procedures conducted in developing a concrete full-scale expert system for financial statement planning. This system was constructed to aid accountants in Finnish corporations in developing financial statements at the end of the accounting year. The task requires considerable

Acknowledgments: An earlier version of this article was published in the Proceedings of the Twenty-Sixth Hawaii International Conference on System Sciences (IEEE Computer Society Press, 1993). I want to thank R.J.R. Back, C. Carlsson, and three anonymous referees for their valuable comments on earlier drafts, S. Lahdenpohja for representing part of the knowledge in the system, and R. Rosenberg for his work on the user interface. I am grateful to the auditing company for providing expertise and time for the construction of the system and for providing the auditors for my experiment. I also want to thank the Research Institute of the Åbo Akademi Foundation and SITRA for the financial support. Part of this work was carried out at Åbo Akademi University, Turku, Finland, and at the University of Southern California, School of Accounting, Los Angeles.

expertise because of the planning dimension in the development process. Options in planning financial statements are mainly dependent on the way in which the Accounting Act, the Companies Act, and a number of tax laws are connected.

On the one hand, net profit in financial statements forms the basis for deciding how much dividend can be paid, how much can be given in loan to the shareholders and other partners, and how much can be retained in the equity capital of the company.

On the other hand, net profit also forms the basis for calculating taxes for the accounting period. The tax laws permit a company to use certain income smoothing techniques to reduce its taxes. A number of reserves can be created and charged against taxable income. Depreciation is permitted to be higher in taxation than that based on the estimated useful life of the asset. Such depreciation and reserves are, however, accepted as deductions in taxation only if they are also made in the books, to at least the same accumulated amount as in taxation.

This means that the financial statement planner is faced with trying to achieve two opposing goals: to show a high net profit and to pay as little tax as possible. Finnish legislation provides considerable scope for planning, and many different issues have to be considered in order to establish an optimal balance between these two goals.

There are very many acts, statutes, and directives that need to be known. The different acts directly concerning financial statement planning alone number to more than ten. Even if the individual pieces of information needed for planning are not difficult to master, the task becomes much more complex when an overall planning strategy is considered. The number of possible combinations of actions grows very quickly, indicating that there may be a need for computer support in managing the complexity of the problem in an effective and efficient way. The sheer wealth of information is often felt to be overwhelming by less experienced planners. The task is also usually executed under time and pressure constraints, making it even harder to consider all the relevant alternatives and factors involved.

A good solution may still be far from an optimal solution and thus cost the company a lot of money. Choosing between a multitude of possible alternatives, handling the chosen alternative in the best possible way, a lack of expertise, and the cost of expertise are typical problems encountered in financial statement planning. These were all areas where we thought an expert system could increase both effectiveness and efficiency, and this motivated us to develop the system.

In our development process, we followed Boehm's spiral model [6] in which requirement analyses, knowledge acquisition, knowledge representation, verification, validation, and evaluation cycles are repeated until the system converges to an adequate solution. The process resulted in a full-scale rule-based expert system for financial statement planning, described in Back [3].

Each of the five steps in their respective cycle is critically important in determining how good the system will be; that is particularly true for verification and validation, which are fundamentally important steps in the evaluation process. Adrion et al. [1, p. 188] define verification as “the demonstration of consistency, completeness, and correctness of the software at each stage and between each stage of the development life cycle,” and validation as “the determination of the correctness of the final program or software produced from a development project with respect to the user needs and requirements."

These definitions seem to be frequently used and widely accepted. However, as Bellman [5] and O'Keefe and O'Leary [12] discuss, they cannot be followed directly when verifying and validating expert systems because an expert system is both a piece of software and a model. Like any software, it can contain pure programming errors and therefore cause undesired behavior, but it is also a model of human knowledge that has not necessarily been modeled before, as is the case in our application. Even if the software is verified, the embodied model may be wrong. The validation process is extremely important because the implementation of an invalid system is useless. It is difficult to separate the model and the software, but verification usually concentrates on software aspects and validation on modeling aspects [12]. In short, verification is to "build the system right" and validation to "build the right system" [8, 11].

In verifying the system we used standard Prolog built-in debugging tools. A more detailed description of the verification process is reported in Back [3].

We present below the procedure used for the validation of our expert system for financial statement planning, following the spiral model and guidelines for rule-based expert systems outlined by O'Keefe et al. [11], O'Keefe and O'Leary [12], and O'Leary [13]. O'Leary et al. [16] used these guidelines in validating an expert system prototype. Our work extends theirs by using these guidelines not only on a prototype but also through the whole life-cycle in the development process, which ended in a full-scale expert system.

The rest of this article is organized as follows. The next section describes the underlying intuitive model for financial statement planning. The third section describes the system and its architecture. The fourth section presents a short description of the guidelines used in validation. The next three sections describe the validation methods, procedures, and results. The final section evaluates the validation procedure and concludes the discussion.

## Financial Statement Planning

THE FINNISH ACCOUNTING ACT, COMPANY ACT, Corporate Income Taxation Act, and Avoir Fiscal Act provide the financial statement developer with certain options for planning financial statements after the end of the accounting period.

Assume that we have the net income from the trial balance. This result can be increased or decreased through income smoothing. If income smoothing is utilized, we can then determine the result before taxes, which may be the same as taxable income, but very often is not because of certain adjustment items: for example, certain revenues are tax-exempt and certain costs are nondeductible expenses in taxation, or certain income that is not revenue in the books is included and certain expenses not included in the books are deducted.

The taxes for the period are based on taxable income. The taxable income consists in reality of two parts: local taxable income and state taxable income. These are not always the same because some of the adjustment items accepted for state taxation are not accepted in local taxation and vice versa.

There are also certain restrictions on minimum taxes and on free equity capital that have to be taken into account:

1. Local taxable income must be at least a sufficient amount; otherwise, a higher estimated level will be used instead when calculating local taxes.

2. If a dividend is paid, the comparative taxes (calculated according to specific rules stated in the Avoir Fiscal Act) must exceed the minimum taxes due to the dividend payment, or the company has to pay complementary taxes.

3. Negative free equity capital should be avoided.

Finally the accounting result (or profit) for the period is calculated by deducting taxes from the result before taxes.

The above procedure assumes that the financial statement planner has already determined the income smoothing instruments to be used. This will then determine the result for the period. However, the main problem in financial statement planning is usually the inverse, that is, how to choose the income smoothing instruments so that a certain required goal for the accounting result under certain constraints is met.

Interest in the planning process is therefore focused on profit, taxable income, result before taxes, income smoothing instruments, and the adjustment items. To be able to determine these terms one must go through three stages in the planning process: goal stating, analysis, and planning. The goal stating stage determines the goal and the constraints that have to be obeyed. The analysis stage determines whether the goal can be achieved. The planning process determines those income smoothing instruments that should be used to achieve the goal. Moreover, one must know the adjustment items.

To summarize, the purpose of financial statement planning is:

1. to fulfil financiers' requirements regarding the return of equity capital, incurring the lowest possible taxes;

2. to forecast the tax consequences of different income smoothing actions;

3. to try to create flexibility in the income statement for future income smoothing actions;

4. to enable the development of informative financial statements.

The financiers' requirements regarding the return of equity capital are operationalized in the following four commonly occurring goals:

1. Pay minimum taxes. No dividend is to be paid.

2. Pay minimum taxes. A certain dividend, which can be higher than the net profit for the year, will also be paid.

3. Show a specific net profit. No dividend is to be paid.

4. Pay a certain dividend, which is less than or equals the net profit for the year.

For each of these goals, the purpose is to find an optimal value for a certain quantity, under the assumption that certain constraints are satisfied. The constraints are the margin for income smoothing and the restrictions on free equity capital. Complementary taxes should be avoided when a dividend is paid.

For each goal, we can either (a) try to avoid taxation based on the Tax Board's estimate, or (b) permit taxation based on the Tax Board's estimate, even if it can be avoided. This choice is left to the planner.

Taxes are minimized by using income smoothing techniques. Forecasting is conducted by comparing, for example, the tax consequences of creating an inventory reserve with tax consequences of excess depreciation. Flexibility is created by considering the elasticity of different income smoothing techniques. The rationale behind the fourth item is that we want to avoid a planning process that follows only the minimum legal requirements concerning disclosure, and leads to financial statements totally lacking information value for outsiders. Therefore, options must exist to report the inventory reserve open, to divide the depreciation into depreciation according to a plan and tax depreciation, and to follow the all-inclusive-income concept principle.

## The System and its Architecture

AS SHOWN IN FIGURE 1, THE FINAL SYSTEM (III) evolved via two prototypes (I and II). The first prototype was constructed in one man-month and consisted of 100 rules. The second prototype was constructed in six man-months and consisted of 300 rules. The final system was constructed in two man-years and consists of about 800 rules written in LPA MacProlog.

The first and second prototypes were developed by the author alone, whereas the development team for the final system consisted of five people: an auditor (CPA) and a tax expert (these two are referred to as the human experts), two computer science students (close to completing their master's degrees) and the author (these three are referred to as the developers). The auditor and the tax expert were both provided by one of the biggest auditing companies in Finland, and were considered by it to be experts.

We elicited the knowledge for the prototypes from secondary data sources, including books, articles, publications, and law texts concerning the development and planning of financial statements. The planning strategies for the prototypes were constructed by systematically analyzing the methods and substance needed in financial statement planning. The knowledge was implemented in the system and the system was run on both real-world and synthetic cases to check that it performed as required.

In developing the final system we elicited knowledge not only from secondary data sources, but also from the human experts through formal and informal in-depth interviews. The knowledge acquisition was an iterative process that also required resolving conflicts between the developers and the human experts. The developers and the human experts met about once a month for a year.

The system can either be used to assist in developing financial statements or as an intelligent knowledge base to be queried about restricted subproblems in financial statement planning. An example of the latter might be to check if a company is entitled to make a warranty reserve, and, if it is, to determine the maximum amount for that reserve.

![](/api/attachments/8PFPV7NV/fulltext/images/f1fa3177f57fbef18c674db9e126f304a25abd6cc3332d34d191d876f323f4b8.jpg)  
Figure 1. Spiral Model

## Knowledge Modules

The final system, named Finstex (Financial Statements Expert), consists of three main components: Planner, Analyst, and Tax Advisor (see figure 2). Finstex operates in the Finnish language.

Planner is the central component. It contains a menu with the planning goals. It has explicit knowledge about the relevant tax laws. It knows the available income smoothing instruments, who is entitled to them, and in what order they should be used to minimize taxes within a planning range of two to three years.

Analyst knows how to analyze the financial statements situation for the company. Analyst also incorporates an optimization algorithm that ensures a user can create optimal financial statements within a planning range of two to three years. This algorithm is described in more detail in Back [4].

Tax Advisor contains information about the items treated differently for taxation and financial purposes. The specific adjustment items to which a company is entitled are very much dependent on the specifics of the company and require an elaborate analysis of what different tax laws may be applied to the situation at hand and what options are available to the planner. Tax Advisor has a large rule base, containing those parts of statutes and laws that are relevant to financial statement planning.

![](/api/attachments/8PFPV7NV/fulltext/images/0173c93a9b6a119f00b210a016ed2cf47f052c35a081216ca38bdb7b9cac2fe9.jpg)  
Figure 2. Finstex

## The Function of the System

In consultation, where the aim is to obtain assistance in developing financial statements, the system takes a trial balance plus some additional information, such as the local taxation rate or line of business, as standard input. The system plans the financial statements, trying to achieve one of the goals listed in the previous section.

Once the user has chosen a goal, Planner takes control. It guides the user through the planning process and presents the proposed financial statements. Before it reaches this final stage, it must extract information from the trial balance, apply the knowledge stored in its own knowledge base, and consult Analyst and the user several times. Analyst can again contact Tax Advisor. The arrows in figure 2 illustrate this interaction.

As an example, the system is described below assuming that the user has chosen goal 3, “Show a specific net profit. No dividend is to be paid.”

It is also assumed that the tax rates and information from the trial balance are already facts in the Finstex knowledge base. Planner will then ask the user to state the goal result $(G)$ for the period.

Planner then contacts Analyst, which determines the result before taxes (RBT), so that the result after taxes will be equal to the goal result. The result before taxes (RBT) is calculated by minimizing

$$
\left| G - R B T \right. + t _ {l} \left(R B T - A _ {l}\right) + t _ {s} \left(R B T - A _ {s}\right) |,\tag{1}
$$

where $t_{l}$ is the local tax rate; $t_{s}$ is the state tax rate; $A_{l}$ describes the adjustment items in local taxation; and $A_{s}$ describes the adjustment items in state taxation.

The terms $A_{l}$ and $A_{s}$ must be determined first. Each can be separated into four parts:

$$
A _ {l} = A 1 _ {l} - A 2 _ {l} + A 3 _ {l} - A 4 _ {l},
$$

and

$$
A _ {s} = A 1 _ {s} - A 2 _ {s} + A 3 _ {s} - A 4 _ {s},
$$

where

(2)

$$
A 1 = \text { tax - exempt   income   in   the   books };\tag{3}
$$

$$
A 2 = \text { taxable   income   not   included   in   the   books };\tag{4}
$$

$$
A 3 = \text { deductible   costs   not   included   in   the   books };\tag{5}
$$

$$
A 4 = \text { nondeductible   costs   included   in   the   books. }
$$

For every item $A1_{l}, \ldots, A4_{s}$ , Analyst queries the user for the amount in FIM for that item. If the user knows the amounts, she or he inputs them and the system is able to calculate RBT. If the user does not know which items are treated differently for tax purposes and for financial accounting purposes, Tax Advisor is contacted.

Tax Advisor proceeds through an interactive dialog with the user. If the consultation is, for example, about tax-exempt items, Tax Advisor goes through a list of items such as can be tax-exempt income for the company. During any query posed by Tax Advisor to determine whether the item is applicable to the company, the user can ask the system why it requires the information. The system explains the query using an associated text file.

Once Tax Advisor has proceeded through all the adjustment items, it sends the final amounts to Analyst, which then continues its work—that is, Analyst utilizes information from the trial balance to calculate RBT. Thereafter, it analyzes this result with respect to the sufficient amount for avoiding taxation based on the Tax Board's estimate and discusses with the user how to proceed if the result before taxes is below the limit. Once it has determined the correct RBT, Analyst continues by comparing the income smoothing reserve with the calculated amount of RBT. Then it tells Planner whether or not the goal can be achieved. Planner depreciates and creates reserves in cooperation with the user, attempting to come as close as possible to the required result before taxes.

The result is set out in a planning report. The user can also ask for the income statement, balance sheet, and taxation reports. If desired, the user can perform one or more sensitivity analyses. Planner will then update the finished statements.

The planning module in the system is similar to an ordinary spreadsheet, although it is constructed and works in a different way. The user gets help in much the same way as when using a spreadsheet, provided she or he has experience with financial statement planning. In particular, the user has to know which items are treated differently for financial reporting versus tax purposes. The user must also understand the rather detailed and technical questions asked during a session. The system differs, however, from a common spreadsheet in that it is also able to help the user to answer questions or to explain the questions. Planner tries to help the user directly or in tandem with Tax Advisor.

## System Architecture

The three main modules—Planner, Analyst, and Tax Advisor—are each constructed as knowledge-based systems. The three knowledge bases are subdivided into smaller modules by information domain.

Dialog windows are used for exchanging information between the user and the system during a session. The system also contains dynamic question forms in which multiple questions are asked, and which really function as spreadsheets. These are used in calculating depreciation and different kinds of reserves.

The whole system is written in LPA MacProlog and runs on a Macintosh computer. It has also been translated to LPA Professional, which is the corresponding Prolog language for MS-DOS machines.

Prolog has also been used successfully in other similar applications (PAYE by Torsun [19]; TA by Schlobohm [17]; EXPATAX by Cunningham reported in [7]; FINSTA by O'Leary and Munakata [14]). A characteristic of these systems, as well as of the system described here, is that a considerable part of the knowledge is law text. Law text is often stated in the form of definition, for which logic programming in the form of Prolog is particularly suitable (e.g., [10]). When translating law text into Prolog, the structure and the style of the original text are kept more or less intact. The rules are therefore easy to read and understand and updates to the knowledge base are also reasonably easy to make.

## Validation Guidelines

THE IMPORTANT QUESTION TO BE ANSWERED IN VALIDATION is whether the right system has been built. Does the system include the knowledge needed to develop corporate financial statements at the end of the accounting year? If it does, it should perform at an acceptable level in assisting an accountant in developing the financial statements. The validating process should yield a proper answer to these questions. In our system's validation process, we primarily used guidelines also employed by O'Leary et al. [16], as mentioned earlier—that is, we had to determine what to validate, what to validate against, what to validate with, when to validate, how to control the cost of validation, and how to control bias.

## Validation Objects and Points

According to the spiral model, the system should be validated throughout the development process. We have been able to validate the different system modules in the system one by one as they have been developed. The overall behavior of the system was rechecked after each module had been linked to the system.

## What to Validate Against

Expert systems can be validated against known results as well as against expert performance [11]. We have done both. We validated both the different modules and the whole system against known results as well as against expert performance.

## Validation Instruments and Cost Control

Expert systems can be validated with historical cases or with a set of synthetic cases created by experts $[11]$ . Although historical cases are to be preferred, we were forced by cost and time constraints to use synthetic cases as well. The synthetic cases were mostly used in validating the modules, while historical cases have mostly been used in validating the final system. Test cases used in the development process were not used again in the validation process.

## How to Control Bias

The validation process can be affected by either expert bias or developer bias. Expert bias is introduced when we have experts who have negative or positive attitudes toward computer-based systems in general or expert systems in particular $[11]$ . To avoid this kind of bias, we used blind validation in the validation of the overall system performance. Developer bias is introduced when developers select test cases so as to guarantee good system performance. This can be avoided by using a different team for validating the overall performance. We were not able to use a separate validation team, but the test cases were selected by people not directly involved in programming the system.

## Validation Methods

One can use either qualitative or quantitative validation methods or a combination of the two. O'Keefe et al. [11] and O'Keefe and O'Leary [12] offer a collection of potential qualitative validation tests, such as face validation, predictive validation, Turing tests, field tests, subsystem validation, sensitivity analysis, and visual interaction. We used subsystem validation, face validation, predictive validation, and a kind of Turing test.

## Subsystem and Face Validation

SUBSYSTEM VALIDATION AMOUNTS TO IDENTIFYING AND EXAMINING the system's assumptions and critical procedures. As O'Leary et al. [16] state, this process usually focuses on the system's details and specifics that serve to identify areas in the system in need of further detailed revision. The first step is usually therefore to divide the code into modules with specific sets of inputs and outputs.

Face validation amounts to demonstrating the system in use to selected experts in order to elicit their comments on how the system performs in terms of its functionality, accuracy, and the like.

We used subsystem validation interlaced with face validation. Subsystem validation was usually conducted without experts, using examples from real companies or synthetical examples. Each of the four submodules of the tax-exempt income module, the tax-exempt income module itself, the four other modules in the Tax Advisor's knowledge base, the reserve module, and the depreciation module were validated separately.

The whole development team participated in the face validation procedure. Face validation was conducted throughout the development process on modules of the system and on the whole system. Sometimes the whole group gathered together and sometimes it was done with only two members present: one of the developers and the auditor or a developer and the tax expert. Face validation was performed about once a month over a nine-month period.

A session with the experts usually started by demonstrating either a submodule or the whole system to check that the new knowledge incorporated into the system was approved of by the experts. If they found some peculiarities in the system, these were thoroughly discussed and, if possible, immediately corrected in the system. When validating the overall performance of the system, we used real-world data as input, such as trial balances handled by the auditing company. These sessions were very useful; the experts acted as a guarantee that no serious mistakes prevailed in the system for a longer time. In this way the developers' view was checked for consistency against that of the experts.

A more thorough face validation was carried out with the second prototype. One of Finland's biggest auditing companies was contacted and asked to name six experts in financial statement planning. They chose one auditor, two financial managers, two people from two different bookkeeping firms, and one financial analyst. A larger sample was not considered necessary at this stage of development. The selected experts had a mean financial planning experience of 11 years with a range of 5 to 19 years.

The prototype was validated by these experts according to its potential usefulness, logic, user-friendliness, and potential for further development, rather than according to the actual expertise of the system. A larger test example was used to demonstrate the system's abilities and potential as well as possible at its current stage. Such an early validation of a prototype has been proposed by Gashnig et al. [9].

After seeing the system run, the experts were asked to answer a questionnaire similar to the one used by Steinbart [18] that tried to capture the experts' opinions about the system. Table 1 presents the results of the questionnaire items dealing with the particular items validated as, as above. The experts were asked to circle the response that best represented their feelings regarding each statement, where SA = strongly agree, A = agree, N = neutral, D = disagree, and SD = strongly disagree.

## Potential Usefulness

All of the experts considered an expert system in financial statement planning to be potentially useful (question 1). The main users were considered to be financial statement planners in larger companies, bookkeeping firms, financial statement planners in smaller companies, auditors, and auditing assistants (question 2). Some of the experts were skeptical about the use of the system in very small companies. They thought that the bookkeeping in these companies should be handled by bookkeeping firms. It was stressed that the auditor's task is not to plan financial statements but that the system could be used by auditors as a control instrument (question 4). The system could also be used in subsidiaries of large corporate groups and in teaching financial statement planning (questions 2 and 5). Five of the experts responded that they would use such a system for financial statement planning if it were available to them (question 3). They stressed the importance of a completed system.

Table 1 Face Validation

<table><tr><td>Question</td><td>SA</td><td>A</td><td>N</td><td>D</td><td>SD</td></tr><tr><td>1. A full-scale expert system in financial statement planning would be useful in practice</td><td>3</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2. The following persons would use it:(a) financial statement planners in larger companies</td><td>3</td><td>3</td><td>0</td><td>0</td><td>0</td></tr><tr><td>(b) financial statement planners in smaller companies</td><td>1</td><td>3</td><td>1</td><td>1</td><td>0</td></tr><tr><td>(c) assistant auditors</td><td>0</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>(d) auditors</td><td>0</td><td>3</td><td>2</td><td>1</td><td>0</td></tr><tr><td>(e) accounting companies</td><td>0</td><td>5</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3. Would use it myself for financial statement planning</td><td>1</td><td>4</td><td>0</td><td>1</td><td>0</td></tr><tr><td>4. Would use it myself as a control instrument for auditing</td><td>1</td><td>2</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5. Would be useful in teaching</td><td>0</td><td>6</td><td>0</td><td>0</td><td>0</td></tr><tr><td>8. Finstex asks irrelevant questions</td><td>0</td><td>0</td><td>0</td><td>6</td><td>0</td></tr><tr><td>9. Finstex&#x27;s logic easy to follow</td><td>2</td><td>3</td><td>0</td><td>1</td><td>0</td></tr><tr><td>10. Would proceed with the planning task in the same manner as Finstex</td><td>1</td><td>3</td><td>2</td><td>0</td><td>0</td></tr><tr><td>11. A mechanism that explains the questions is helpful</td><td>3</td><td>2</td><td>1</td><td>0</td><td>0</td></tr><tr><td>12. A mechanism that explains the conclusions is helpful</td><td>2</td><td>4</td><td>0</td><td>0</td><td>0</td></tr></table>

## Logic

The experts found the system's reasoning easy to follow (questions 8, 9, and 10). This was the result of the inference strategy—backward chaining—that the system utilizes.

The same observation has been previously reported in other studies by Aiello [2].

## User-Friendliness

All experts considered the system's ability to explain questions important (question 11). The fact that the system could not explain how it reached a certain conclusion in natural language was considered a shortcoming (question 12).

## Potential for Further Development

All experts agreed that it was sensible to build a full-scale expert system. They stressed that tax planning is a central issue in financial statement planning and that this part was extensively developed in the system. Some of the experts wanted to put more weight on financial statement planning. They wanted to be able to get help with the formulation of the goal in the initial planning process. They also wanted to see how planning affects the share capital item. The system was generally considered to be fast, responsive, and user-friendly. The experts saw potential in using the system continuously during the year as a planning tool, to see how different decisions affect the financial statements, although the system was originally constructed to be used only at the end of the accounting period.

## Predictive Validation

BASED ON A SURVEY BY O'LEARY AND WATKINS [15], predictive validation or testing is the most commonly used validation method for the systematic validation of expert systems. O'Keefe and O'Leary [12] list four testing guidelines for expert systems validation:

1. The problems to be encountered by the system should be reflected in the cases chosen.

2. A sufficient number of test cases should be utilized to elicit a range of parameters necessary to test the system, and to be able to establish some measures of statistical significance.

3. The nature of the problems investigated by the system should help establish the characteristics of the cases.

4. One must be aware that in some domains expert decisions may precipitate actual outcome.

The first requirement is usually met by using historical test cases with either known results or measures of human expert performance in those cases. Meeting the second and third requirements is more difficult because there is no best way to generate test data or to ensure adequate coverage, even heuristically. There is no algorithm to find consistent, reliable, valid, and complete test criteria $[1]$ . The fourth requirement can also be difficult to handle, but was not valid in our case.

Once the development process was finished, we conducted predictive validation on the system's overall performance. We asked the auditing company to provide us with as comprehensive a set of materials as possible. They came up with fifteen trial balances (eight from the tax year 1989 and seven from 1990). A bookkeeping company was also asked to deliver trial balances. They delivered two (both from the tax year 1989). Two of the trial balances delivered by the auditing company from tax year 1990 were synthetic cases; the rest were real-world trial balances. The reason for including synthetic cases from tax year 1990 was that the auditing company had no real cases of either companies with losses from previous years or companies with new equity capital, and they also wanted to test the system on such cases.

The material produced by the system for the synthetic cases and for two of the cases for the tax year 1990 was sent to the auditing company and checked by them. For the rest we had the official financial statements, audited by the auditing company, against which we could compare the results produced by the system.

The errors detected were divided into input, output, and performance errors. An input error meant that an item in the trial balance had no natural correspondence in the system's trial balance. An output error meant that an important result was not written out or some item was missing in the financial statements that should be there. A performance error meant that the system produced false results, either because of a missing definition with no conditions referring to it or because of a missing condition in a definition. The results are shown in Table 2.

The trial balances are named TB1–TB17 and are presented in chronological order according to the validation date. If missing knowledge or errors were detected, the knowledge was added to the system and the errors corrected before a new case (trial balance) was run. Where the errors were obvious to the developer, they were immediately corrected. If they were more subtle, the auditor or the tax expert was contacted. There was thus feedback into the knowledge acquisition process.

In eleven out of seventeen cases the results were very good—nothing was found to be wrong with the input questions, output results, or performance of the system. In two cases there were problems with input and output errors, respectively. For TB1, TB2, TB6, TB9, and TB12, the results produced by the system were exactly the same as the actual historical results in the financial statements for the company. TB3 and TB4 were trial balances provided by the bookkeeping company. The results produced by the system for these companies were presented and discussed with the manager of the bookkeeping company and with the person who was supposed to develop the financial statements for the company. They accepted that the results were fully correct after comparing them with the companies' actual financial statements.

For TB5 the result was not good. Five different questions regarding rather important input were missing. The corresponding knowledge was also missing. These missing input values caused two errors in the output produced by the system. For example, there was no cell in the depreciation form for 10 percent depreciation on buildings, causing an output error in the reports on depreciations. The runs with TB7, TB8, and TB10 also revealed minor errors in the input questions (TB7) and output results (TB7, TB8, and TB10). In TB11 and TB13 one performance error was detected in each. In determining the goal result in TB13, a condition regarding income taxes (when the taxable income is less than FIM 100,000) was missing, resulting in an incorrect goal result. From TB14 to TB17 (TB16 and TB17 being the synthetic cases), there was an unbroken sequence of correct results in every respect. For these, the validator only had the trial balances and the supplementary information needed. The results were checked and accepted as fully correct by the expert auditor from the auditing company. The results were considered very good, especially given that a new act, the Avoir Fiscal Act, came into force during the validation period. That meant that in validating the system the knowledge base also had to be updated to meet the requirements stated in the new act.

Table 2 Predictive Validation

<table><tr><td>TB</td><td>Input</td><td>Output</td><td>Performance</td><td>Validation date</td></tr><tr><td>TB1 (89)</td><td>0</td><td>0</td><td>0</td><td>1/9/90</td></tr><tr><td>TB2 (89)</td><td>0</td><td>0</td><td>0</td><td>1/10/90</td></tr><tr><td>TB3 (89)</td><td>0</td><td>0</td><td>0</td><td>1/29/90</td></tr><tr><td>TB4 (89)</td><td>0</td><td>0</td><td>0</td><td>1/29/90</td></tr><tr><td>TB5 (89)</td><td>5</td><td>2</td><td>0</td><td>5/23/90</td></tr><tr><td>TB6 (89)</td><td>0</td><td>0</td><td>0</td><td>6/4/90</td></tr><tr><td>TB7 (90)</td><td>1</td><td>1</td><td>0</td><td>6/18/90</td></tr><tr><td>TB8 (89)</td><td>0</td><td>1</td><td>0</td><td>7/13/90</td></tr><tr><td>TB9 (89)</td><td>0</td><td>0</td><td>0</td><td>7/13/90</td></tr><tr><td>TB10 (89)</td><td>0</td><td>2</td><td>0</td><td>7/14/90</td></tr><tr><td>TB11 (89)</td><td>0</td><td>0</td><td>1</td><td>7/17/90</td></tr><tr><td>TB12 (90)</td><td>0</td><td>0</td><td>0</td><td>7/17/90</td></tr><tr><td>TB13 (90)</td><td>0</td><td>0</td><td>1</td><td>7/18/90</td></tr><tr><td>TB14 (90)</td><td>0</td><td>0</td><td>0</td><td>11/22/90</td></tr><tr><td>TB15 (90)</td><td>0</td><td>0</td><td>0</td><td>11/22/90</td></tr><tr><td>TB16 (90)</td><td>0</td><td>0</td><td>0</td><td>1/23/91</td></tr><tr><td>TB17 (90)</td><td>0</td><td>0</td><td>0</td><td>1/23/91</td></tr><tr><td>Total</td><td>6</td><td>6</td><td>2</td><td></td></tr></table>

On the basis of the predictive validation, the validator concluded that the system exhibits an acceptable performance level, although there might well still be errors in it. Moreover, this phase indicated that the system adapts well, at least to small changes in the tax rules.

## Blind Performance Test

A BLIND PERFORMANCE TEST IS A VARIANT OF THE WELL-KNOWN Turing test. In such a test, a system is validated against human experts by comparing the results produced by the system with those produced by humans, without the evaluator knowing the identity of the performer. The test also avoids any pro or con computer bias—a positive side effect. Turing tests have been widely used in testing expert systems, especially medical expert systems $[12]$ . Their drawback, however, is that they are very expensive to conduct.

One test case made use of a blind performance test. In this test, we wanted to see how the system performed in comparison with experts in the field. We especially wanted to check if the experts could produce better solutions than the system. We asked the auditing company to provide a suitable trial balance for the test with the constraints that the task should be neither too easy nor too difficult. We also wanted to find some kind of tax-exempt income possibilities; otherwise the auditing company had complete latitude in its choice of dataset.

## Task

The task was to develop the financial statements for a real company, minimizing the taxes within a planning range of two to three years, and enabling a dividend payment for the year amounting to FIM 324,000.

## Subjects

The auditing company provided us with eleven auditors. They had been in the field for three to eighteen years, and could thus be classified as experienced auditors. Even if auditors do not usually develop the financial statements for a company, we think that, in order to be able to audit the financial statements, they should also be able to develop them. Moreover, they are in fact often used as consultants by companies for planning financial statements.

## Test Setup

The auditors were randomly assigned to two groups—five to the textbook-assisted group and six to the computer-assisted group. Those belonging to the computer-assisted group used the system to help them develop the financial statements for the company, whereas those belonging to the textbook-assisted group were supposed to develop the statements on the basis of their expertise, and using whatever help they usually relied upon. Both groups were allowed three hours for the task.

## Results

The results produced by the auditors were rewritten by machine in order to conceal which results were computer printouts and which were of human origin. Those working in the computer-assisted group produced two alternatives, here named alternatives 1 and 2. Alternative 1 was used in one solution and alternative 2 in five solutions. The results were examined by the same auditor who was used as an expert in the development process. Because all the computer results for respective alternatives were identical, only one of each was presented to the auditor in order not to reveal that the computer assisted in obtaining the results. The auditor ranked the overall performance of the participants in five categories ranging from very poor to very good. The results are shown in Table 3.

Results E1–E5 were those provided by the textbook-assisted group of human experts, and C1–C6 those provided by the computer-assisted group. The results show that the expert ranked the performance of E3 and of C1–C6 as very good. E3 was almost identical to alternative 2 produced by C2. The expert evaluated the financial statements developed by E1 and E2 as acceptable in spite of minor mistakes. The expert evaluated the financial statements developed by E4 and E5 as very poor, because both had made some serious mistakes. None of the human experts produced a solution to the task that was better than the solutions produced by the computer-assisted group.

Table 3 Performance Validation

<table><tr><td>Auditor</td><td>Very poor</td><td>Poor</td><td>Acceptable</td><td>Good</td><td>Very good</td></tr><tr><td>E1</td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>E2</td><td></td><td></td><td>x</td><td></td><td></td></tr><tr><td>E3</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>E4</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>E5</td><td>x</td><td></td><td></td><td></td><td></td></tr><tr><td>C1</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>C2</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>C3</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>C4</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>C5</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>C6</td><td></td><td></td><td></td><td></td><td>x</td></tr><tr><td>Total</td><td>2</td><td></td><td>2</td><td></td><td>7</td></tr></table>

It is interesting to compare the performance of the computer-assisted group with that of the textbook-assisted group, in particular to look at the kind of errors that humans typically make and that are easily avoided when using the expert system. Extracts from the Income Statement are shown in Table 4, from the Tax Report in Table 5, and from the Avoir Fiscal Report in Table 6 produced by C5, whose planning was considered to be very good, and by E4, whose planning was considered very poor. C5 and E4 had both chosen alternative 2, which allows taxation according to the Tax Board's estimate, as their planning strategy.

Table 4 shows that E4 has used more income smoothing than C5—that is, E4 has a result before taxes amounting to FIM 327,626 compared with that of C5, amounting to FIM 728,153. E4 ends up with less tax—FIM 378,412—and a loss for the period amounting to FIM 50,786, while the corresponding figures for C5 are FIM 497,497 with a profit of FIM 230,656.

In analyzing the Tax Report the validator found that E4 had calculated the local taxes wrongly at FIM 378,412 (Table 5, col. 4). They should have been FIM 417,366 as calculated by C5 (Table 5, col. 2). E4 had used the wrong basis for calculating the estimated taxes. The tax refund of FIM 191,588 anticipated by E4 would therefore in reality be smaller. This mistake has even more serious consequences than just a decrease in anticipated tax refunding, as E4 has used an unnecessarily high amount for income smoothing, which cannot be changed, and which might have been better used the following year.

In analyzing the Avoir Fiscal Report, the validator found that E4 had also calculated the comparative taxes incorrectly—that is, E4 included the estimated taxes, FIM

Table 4 Extract from Income Statement

<table><tr><td></td><td>C5</td><td>E4</td></tr><tr><td>Net Sales</td><td>164,885,530.61</td><td>164,885,530.61</td></tr><tr><td>Profit from operations before depreciation</td><td>11,324,322.24</td><td>11,324,322.24</td></tr><tr><td>Depreciation</td><td></td><td></td></tr><tr><td>Buildings</td><td>-645,092.00</td><td>-645,092.00</td></tr><tr><td>Machinery and equipment</td><td>-1,617,557.00</td><td>-1,617,557.00</td></tr><tr><td>Other capitalized expenditure</td><td>-139,797.00</td><td>-139,797.00</td></tr><tr><td>Profit/loss from operations</td><td>8,921,876.24</td><td>8,921,876.24</td></tr><tr><td>Profit/loss before appropriations and taxes</td><td>10,214,389.99</td><td>10,214,389.99</td></tr><tr><td>Changes in untaxed reserves</td><td></td><td></td></tr><tr><td>Bad debt reserve</td><td>550,000.00,</td><td></td></tr><tr><td>Operational reserve</td><td>-10,036,236.15</td><td>-9,886,763.00</td></tr><tr><td>Profit/loss before taxes</td><td>728,153.84</td><td>327,626.00</td></tr><tr><td>Income taxes for the period</td><td>-497,497.00</td><td>-378,412.00</td></tr><tr><td>Profit/loss for the period</td><td>230,656.00</td><td>-50,786.99</td></tr></table>

378,412, in the comparative taxes (Table 6, col. 2), but these should in reality have been calculated on the local taxable income which in E4's case were zero. Hence, E4 has in reality a tax liability amounting to FIM 234,620 (Table 6, col. 3). While the company has a tax excess from previous year amounting to FIM 100,000, based on E4's planning, it would have to pay complementary taxes amounting to FIM 134,620 (Table 6, col. 3) and the tax excess for forthcoming years would be zero instead of the FIM 243,801 (Table 6, col. 2) that E4 had calculated. These mistakes have even more serious consequences than the former mistake. The anticipated tax refund of FIM 191,588 (Table 5) would be even smaller and decrease to a refund of only FIM 18,014. Planning this way, the loss for the period is in reality FIM 224,360 instead of FIM 50,786.

E4 also wrongly included the investment deposit and the import deposit in the basis when calculating the bad debts reserve. In this specific case this mistake did not have any effect on planning or the planning result.

## Discussion and Conclusions

THE RESULTS OF THE VALIDATION OF FINSTEX are very encouraging. The system was successfully validated by means of face and subsystem validation, predictive validation, and blind performance validation. However, there are some critical comments to be made regarding validation with respect to selection and the number of test cases, subjects, and validators.

Table 5 Extract from Tax Report

<table><tr><td rowspan="2"></td><td colspan="2">C5</td><td colspan="2">E4</td><td rowspan="2">E4 corrected</td></tr><tr><td>State</td><td>Local</td><td>State</td><td>Local</td></tr><tr><td>Result before taxes</td><td>728,153.84</td><td>728,153.84</td><td>326,626.00</td><td>326,626.00</td><td></td></tr><tr><td>Deductions</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>Dividends received</td><td>7,628.40</td><td>7,628.40</td><td>7,628.40</td><td>7,628.40</td><td></td></tr><tr><td>Tax-exempt profits</td><td>400,000.00</td><td>400,000.00</td><td>320,000.00</td><td>320,000.00</td><td></td></tr><tr><td>Interest on investment deposit</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td></tr><tr><td>Other tax-exempt income</td><td>0.00</td><td>0.00</td><td>0.00</td><td>0.00</td><td></td></tr><tr><td>Taxable income</td><td>320,525.44</td><td>2,225,954.66</td><td>0.00</td><td>2,225,954.66</td><td></td></tr><tr><td>Tax 25.00 / 18.75</td><td>80,131.36</td><td>417,366.00</td><td></td><td>378,412.00</td><td></td></tr><tr><td>Total taxes</td><td></td><td>497,497.00</td><td></td><td>378 412.00</td><td>417,366.00</td></tr><tr><td>Taxes paid in advance</td><td></td><td>570,000.00</td><td></td><td>570,000.00</td><td>570,000.00</td></tr><tr><td>Complementary taxes</td><td></td><td>0.00</td><td></td><td>0.00</td><td>134,620.00</td></tr><tr><td>Tax refund</td><td></td><td>72,503.00</td><td></td><td>191,588.00</td><td>18,014.00</td></tr></table>

In the predictive validation we used historical test cases, which is the dominant method for validation of expert systems. In two cases, however, we used synthetic cases. This is considered inadvisable since it demands considerable objectivity on behalf of the validators, due to the temptation to make the cases reflect the known strengths of the system (see, e.g., [12]). However, we used the synthetic cases to meet the requirement that we cover the whole domain. We tackled the objectivity problem by asking the auditing company to produce the synthetic cases. The cases were thus produced by an outside auditor who was not in any way involved in the development procedure. We ran the cases on the system and the auditor received the solutions from us and validated them.

In the blind performance test we could be criticized for using auditors instead of real financial statement developers. In choosing subjects for this process, real financial statement developers would naturally have been preferable. However, it turned out to be extremely difficult to get a group of experts from companies. Optimistically, one could think of obtaining a sample of people doing the task with the system, but it was essentially impossible to obtain a control group. There was no incentive for people from companies to do the manual planning.

We used only one case in the blind performance test. The reasoning behind this is that the test requires a considerable amount of expert time. We had eleven auditors who used between two and three hours of their working time. Blinding the outputs from computer and human expert is also very time-consuming, but by doing so we avoided possible pro or con system bias.

The test case could also be criticized for being too difficult and for having too many unusual elements in it. However, before the test, the auditing company was very concerned that the task might be too easy for the auditors and that the results would therefore not differ from each other.

Table 6 Extract from Avoir Fiscal Report

<table><tr><td></td><td>C5</td><td>E4</td><td>E4 corrected</td></tr><tr><td colspan="4">Minimum income taxes:</td></tr><tr><td>Dividend planned</td><td>324,000.00</td><td>324,000.00</td><td></td></tr><tr><td>Tax rate</td><td>0.72</td><td>0.72</td><td></td></tr><tr><td>Minimum income taxes</td><td>234,620.00</td><td>234,620.00</td><td>234,620.00</td></tr><tr><td colspan="4">Comparative taxes:</td></tr><tr><td>State taxes</td><td>80,131.00</td><td>0.00</td><td>0.00</td></tr><tr><td>Local taxes</td><td>54,489.00</td><td>378,412.00</td><td>0.00</td></tr><tr><td>Total comparative taxes</td><td>134,620.00</td><td>378,412.00</td><td>0.00</td></tr><tr><td>Tax liability</td><td>-100,000.00</td><td>143,801.00</td><td>-234,620.00</td></tr><tr><td>Tax excess from previous years</td><td>100,000.00</td><td>100,000.00</td><td>100,000.00</td></tr><tr><td>Tax liability</td><td>-100,000.00</td><td></td><td>-134,620.00</td></tr><tr><td>Complementary taxes</td><td>0.00</td><td></td><td>134,620.00</td></tr><tr><td>Accumulated tax excess</td><td></td><td>243,801.00</td><td>0.00</td></tr></table>

Validation literature strongly stresses the use of a third-party validator. We were only partly able to fulfill that requirement due to time and cost constraints. In the face and subsystem validation, besides the development team, we also used the auditor and the tax expert. In some cases the tax expert and the auditor only validated that their own knowledge had been correctly interpreted by the developers. However, it must be stressed that a considerable amount of the knowledge in the system came from the two developers, and the tax expert and the auditor were often, therefore, acting as third-party validators. In validating the second prototype by face validation, six third-party validators were used.

In the predictive validation, one of the developers took care of the validation, but people not involved in programming the system selected the test cases. In the blind performance test the auditing company chose the test case but the auditor checked the results.

To sum up, we have presented how validation can be incorporated in the spiral model, using guidelines articulated in literature regarding the validation of expert systems. The extensive validation performed—face and subsystem validation, predictive validation, and blind performance validation—indicates that the model embodied in the system is correct. From this we draw the conclusion that we have built the right system.

## REFERENCES

1. Adrion, W.R.; Brandstad, M.A.; and Cherniavsky, J.C. Validation, verification, and testing of computer software, ACM Computing Surveys, 14, 2 (1982), 159–92.

2. Aiello, N. A comparative study of control strategies for expert systems: age implement-

tation of three variations of PUFF. Proceedings of the National Conference on Artificial Intelligence (1983), 1–4.

3. Back, B. An Expert System for Financial Statements Planning. Ph.D. dissertation, Åbo, Finland: Åbo Academy Press, 1991.

4. Back, B., and Back, R.J. Financial statement planning under tax constraints. European Journal of Operational Research, forthcoming.

5. Bellman, K.L. The modeling issues inherent in testing and evaluating knowledge-based systems. Expert Systems with Applications, 1, 3 (1990), 199–216.

6. Boehm, B.W. A spiral model of software development and enhancement. Computer, 21, 5 (May 1988), 61–72.

7. Edwards, A., and Connell, N.A.D. Expert Systems in Accounting. London: Prentice-Hall and The Institute of Chartered Accountants in England and Wales, 1989.

8. Fox, M.S. AI and expert system myths, legends, and facts. IEEE Expert, 5, 1 (1990), 8–20.

9. Gashnig, J.; Klahr, P.; Pople, H.; Shortliffe, E.; and Terry, A. Evaluation of expert systems: issues and case studies. In F. Hayes-Roth, D.A. Waterman, and D.B. Lenat (eds.), Building Expert Systems. Reading, MA: Addison-Wesley, 1983, 241–280.

10. Kowalski, R.A.; Sergot, M.J.; Kriwaczek, F.; Hammond, P., and Cory, H.T. The British Nationality Act as a logic program. Communications of the ACM, 29, 5 (May 1986), 370–386.

11. O'Keefe, R.M.; Balci, O.; and Smith, E.P. Validating expert system performance. IEEE Expert, 2, 4 (1987), 81–89.

12. O'Keefe, R.M., and O'Leary, D.E. The verification and validation of expert systems. Technical Report No. 37-89-192, Department of Decision Sciences and Engineering Systems, Rensselaer Polytechnic Institute, Troy, New York, 1990.

13. O'Leary, D.E. Methods of validating expert systems. Interfaces, 18, 6 (November 1988), 72–79.

14. O'Leary, D.E., and Munakata, T. Developing consolidated financial statements using a prototype expert system. In E. Turban and P.R. Watkins (eds.), Applied Expert Systems. Amsterdam: North-Holland, 1988, 143–157.

15. O'Leary, D.E., and Watkins, P.R. Expert Systems in Internal Auditing. Research Monograph, Institute of Internal Auditors, 1989.

16. O'Leary, T.J.; Goul, M.; Moffitt, K.E.; and Radvan, A.E. Validating expert systems. IEEE Expert, 5, 3 (1990), 51–58.

17. Schlobohm, D.A. TA-Prolog program which analyzes income tax issues under 318(a) of the Internal Revenue Code. In C. Walter (ed.), Computing Power and Legal Reasoning. St Paul, MN: West Publishing, 1985, 765–815.

18. Steinbart, P.J. The construction of a rule-based expert system as a method for studying materiality judgments. The Accounting Review, 62, 1 (January 1987), 97–116.

19. Torsun, I.S. PAYE: a tax expert system: research and development. In M.A. Bramer (ed.), Expert Systems III. Cambridge: Cambridge University Press, 1987.
