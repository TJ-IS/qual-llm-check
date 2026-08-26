---
otero_id: 17871
otero_key: "7KXA3VX7"
title: "Models, metrics, and management of IS development"
authors: "D.R. Jeffrey; I. Vessey"
year: "1980"
journal: "Information & Management"
doi: "10.1016/0378-7206(80)90007-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Models, Metrics, and Management of IS Development

D.R. Jeffrey \*

University of South Wales, Sydney, Australia

and

I. Vessey \*

University of Queensland, Brisbane, Australia

Two types of models can assist the information system manager in gaining greater insight into the system development process. They are: isomorphic models that represent cause-effect relationships between certain conditions (e.g., structured techniques) and certain observable states (e.g., productivity change); and paramorphic models that describe an outcome but do not describe the processes or variables that influence the outcome (e.g., estimation of project time or cost). The two models are shown to be interrelated since the relationships of the first model are determinants of the parameters of the second model.

IS managers can make significant contributions by developing isomorphic models tailored to their own organizations. However, metrics that measure relevant characteristics of programs and systems are required before substantial progress can be made. Although some initial attempts have been made to develop metrics for program quality, program complexity, and programmer skill, much more work remains to be done. In addition, other metrics must be developed that will require the involvement of personnel, not only in the computer sciences, but also in information systems, the behavioral sciences, and IS management.

Keywords: system development, information system management, software production models, software metrics.

## 1. Introduction

If the much maligned information systems (IS) managers were to believe everything they read, they would severely doubt their own management capabilities. Statements abound in the literature such as: "Few managers are able to predict the time and resources needed to develop large-scale software systems" [8], and "Software is often delivered late. It is frequently unreliable and usually expensive to maintain" [12]. These statements are made, however, without empirical evidence of their accuracy. Of course, many systems have been observed to overrun both on time and cost, but many systems are implemented within time and cost objectives. Recent ob-

![](/api/attachments/7KXA3VX7/fulltext/images/9ccff7bbca4849526b6a14e45c20e65b42b61acff073c7d3abf8a2729156cdb1.jpg)

publications include papers in the areas of organisational objectives, programming productivity, and edp management, and three books on information systems. He is a member of ACM, ACS, AAANZ, SMIS and ASA.

![](/api/attachments/7KXA3VX7/fulltext/images/2584d0b1727d8f9a71e55fcea4941a702f137eaced3e534bb33a8a74a068bc32.jpg)

Ross Jeffrey is currently a Lecturer in Information Systems at the University of New South Wales (Australia). He received a B.Com (Hons.) in accountancy from The University of Queensland and an M.Com (Hons.) in Information Systems from the University of New South Wales. During the last ten years he has also held positions at the University of Queensland and The Bendigo College of Advanced Education. His servations suggest that IS management is able increasingly to complete projects within time estimates [9]. This is most likely due to increasing knowledge and experience, and the application of techniques emerging from research into the system life cycle. Current research spans the area from very large systems to small systems and includes work on individual program and analyst/programmer characteristics [2].

The aim of this article is to provide a structure so that management can apply this research to their own environment, in such a way that they can use the insights provided in the literature, while expanding these ideas so that their models incorporate corporate management objectives, management style, and environmental constraints.

## 2. Software production models

The research into software production models is concerned with methods of constructing models that assist the IS management process. Such models attempt to describe the IS environment and products in terms of relationships between observable variables, so that their manipulation leads to a desired state. Thus, the researcher is attempting to describe relationships that can be used as the basis for actions that will lead to the attainment of the manager's own set of objectives.

These models fall into the two broad areas of isomorphic and paramorphic models [5]. An isomorphic model describes real world processes or relationships. It is prescriptive in that it permits us to state what should be done to achieve a desired end result. A paramorphic model describes an outcome but does not describe the processes or variables that influence that outcome. The distinction between these two approaches may be shown by comparison of the work of, say, Walston and Felix [10], with that of Putnam [7,8]. Walston and Felix set out to describe the relationships between twenty-nine programming project characteristics, (e.g., customer interface complexity, availability of the development computer, structured programming, and complexity of the application processing) and programming productivity. They are attempting to determine whether certain observable states (e.g., productivity change) are determined by certain conditions (e.g., the introduction of structured techniques). This is an isomorphic model. In contrast, Putnam states that an IS manager can determine project cost or development time by the application of his model. The form of the model is:

$$
S _ {\mathrm{s}} = C _ {\mathrm{k}} K ^ {1 / 3} t _ {\mathrm{d}} ^ {4 / 3},
$$

where

$S_{s}$ is the number of end product source lines of code delivered;

K is the life cycle effort in man-years;

$t_{\mathrm{d}}$ is the development time; and

$C_{k}$ is a constant that depends on the local state of technology.

This is a paramorphic model. In this model, the value of $C_{k}$ depends on such factors as the programming language, the development environment, and the software tools used. However, this equation does not fully characterize the development process because the skills of the project personnel, when dealing with a difficult project, also affect the solution. Putnam describes this as the constraint condition, given by:

## Constraint condition = $K/t_{d}^{3}$

His model uses global parameters to describe the relationship between K and $t_{d}$ ; it does not describe the underlying relationships that impact the values of these parameters.

This then reveals an interesting relationship between the two approaches: the types of conditions or variables investigated by Walston and Felix and others are the possible determinants of the values of $C_{k}$ and the constraint condition in Putnam's equations. But despite this link, there remains a very important distinction between the two approaches. The paramorphic approach defines the manager's goals in terms of the development time and life cycle effort, whereas an isomorphic approach makes no assumption as to goals, but states that certain conditions must be met to produce the required state. The selection of the desired state of affairs is then determined by management in the light of their objectives.

This raises the question of the use of the models. Management is fundamentally the process of planning, directing, organizing, staffing, and controlling activities; reliable forecasting is a necessary adjunct to these processes. The macro approach, as illustrated by the Putnam model, often proves to be a suitable forecasting technique. This is because, if it is sufficiently reliable, its simplicity makes it eminently applicable, in practice. The micro approach, characterized by the isomorphic type studies, can result in a complex network of relationships that may or may not provide a better forecast.

The reliability of the Putnam model has been proved by empirical study [7]. Its advantages, therefore, include both simplicity and reliability. The major disadvantage is that it relies on forecasts of the project size (lines of code), the technology constant $C_{k}$ for the particular project, and the constraint condition. In a commercial environment that is often characterized by changing technology and high staff turnover, these forecasts may be difficult to derive from past history. Factors that may make the forecast of $C_{k}$ difficult include: modified hardware environments; increasingly sophisticated system software (DBMS, on-line systems, distributed systems); changing system development methodologies; and increased use of packaged application software. In addition, statistics on past projects (which are the basis of the forecast) are often not available, and many commercial installations have recently found themselves in a period of heavy commitment to maintenance; therefore, the determination of accurate values of $C_{k}$ and the constraint condition may be very difficult.

IS management is concerned with more than the forecasting problem, however. They must also attempt to improve the processes and products generated by their personnel. The Putnam model allows the IS manager to determine the "best" relationship in terms of time and cost tradeoffs between manpower and development time, but does not provide insights into how improvements can be achieved. It is in this area that the isomorphic model is needed.

Unfortunately, isomorphic models, to date, have limitations. These include:

(i) disagreement on those factors that influence the process, and therefore the variables selected for study;

(ii) conflicting findings; and (iii) large variance in data in many studies that cannot be attributed to specific causes.

However, it is in this very area that IS manager can make a significant contribution. They are in a position to develop a much greater understanding if they track organizational performance (in light of the objectives) and thereby develop isomorphic models tailored to their own organizations.

## 3. Software Metrics

Before the development of isomorphic models can progress far, the development of measurement methods and metrics to measure relevant characteristics of programs and systems is essential. The need for standardized measures is highlighted by the different possible definitions of lines-of-code (e.g., in COBOL). Do we mean SOURCE lines of code (including or excluding comments and blank lines)? And, because a “statement” can span several lines, do we mean “statements” rather than lines?

To date, most isomorphic studies have included only the programming phase of the systems life cycle. Even here, there has been little attempt to develop and test metrics of factors influencing the programming process. In general, the approach has been to collect and analyze data on as many variables as possible – in an attempt to determine those which produce significant correlations. Many of these variables fall into two categories – (1) those that attempt to measure program complexity, and (2) those that try to measure programmer experience or skill. It is clear, then, that we require reliable metrics for these two factors.

Before we attempt to measure these variables, however, we require a standard by which to measure the finished product. The development of a software system can be compared to the production of a physical product. Production can be defined as a process that attempts to produce a product of desired quality, on time, and within given cost constraints. Up to now, IS managers mostly have been concerned with time and cost; there has been too little recognition that quality is also of prime importance.

## 3.1. Quality

Many claims have been made regarding ways in which the quality of a systems product can be improved; an example is the use of structured methodologies. However, little success has been achieved in measuring those improvements because of the difficulties in conducting controlled experiments and the lack of adequate metrics. Some of the quality factors are maintainability, robustness, clarity, performance, cost, portability, and useability [11]. Managers of different organizations will, of course, differ in their ordering of the importance of these characteristics.

Even in the reported studies little attempt has been made to assess the quality of the finished product: Does it make good use of hardware? Is it easy to maintain? Is it easily expanded? Can it be run on other hardware configurations? Can we, in fact, attempt to measure productivity without knowing whether the programs do the job? Is it sufficient to get a program working (without concern for satisfaction of user needs, maintainability, etc.)? In summary, can we compare two programs when one of them satisfies management's objectives better than the other?

Software engineers have studied the quality of FORTRAN programs [3] using automated techniques. Other approaches use expert judgment or peer assessment (involving rating of program attributes by knowledgeable people) [1]. As yet, commercial organizations have given little formal attention to quality measurement.

## 3.2 Complexity

Research studies on complexity generally use variables such as lines-of-code, number of files, number of reports, and number of subprograms, to name but a few. The highest correlation with development time is shown by lines-of-code. In association with an effective means of estimating the expected number of lines-of-code (see, [7]), this may, therefore, be a useful predictor of development time.

M.H. Halstead [4] provides a different approach to the measurement of program complexity. He has developed objective measures in terms of the number of distinct operators and operands in the program, and their frequency of occurrence. Studies have shown that the theory predicts the number of bugs and correlates with time to develop a program with remarkable accuracy. The problem, however, lies in the a priori assessment of the numbers of operators and operands.

## 3.3. Skill

Most commercial studies test the effect of programmer experience on the development process. Experience has been formulated in many ways, all objective and readily measureable; however, the results are inconclusive, some showing experience to be significant, others not. There are many possible reasons, but probably the relevant variable is skill or ability, not experience. Clearly, a programmer with 5 or more years' experience in COBOL should be quicker and leave fewer residual errors than one with less than a year's experience. But when does innate ability begin to overtake time-on-the-job? It is apparent that we need a measure of programmer skill.

At present, the most common method is peer assessment. Some preliminary studies are being carried out using process tracing (to trace an expert's thought patterns while performing a task) in order to identify the types of skills needed [6].

## 4. Software Management

The variables of quality, complexity, and skill are only three of several factors affecting software development. They are perhaps the most basic, and hence ones that already have received attention. However, there are several other areas of significance to the formulation of an isomorphic model of the software development process. Table 1 shows disciplines and roles they are playing or may play in the future.

Table 1. Relevant Disciplines in System Development

<table><tr><td>Discipline</td><td>Role</td></tr><tr><td>Computer Science</td><td>Development of metrics for program quality and program complexity</td></tr><tr><td>Information Systems</td><td>Development of metrics for system quality system complexity, and programmer and analyst productivity.</td></tr><tr><td>Behavioral Sciences</td><td>Development of metrics for programmer/analyst skills.Application of theories of group dynamics, communications, leadership, and motivation.</td></tr><tr><td>IS Management</td><td>Study of the effects of organization structure and supervision.</td></tr></table>

Research into management's role is virtually non-existent. This is not surprising, since programming is far more formalized than other phases of the system life cycle. Behavioral and organizational factors, however, do impact the software process (even though their effects may be somewhat harder to measure); hence, these areas should be fruitful sources of increased productivity for an IS department.

## 5. Conclusions

There is growing feeling in industry that IS managers should be able to implement a system on time and within budget; they are now held responsible more than ever before. To achieve this, it is imperative for IS managers to measure productivity within their own operations.

Determination of all factors underlying the software process is still far in the future; however, IS departments can find some guidance in the literature to begin initial measurements. Further, IS managers are in a unique position to apply theories relating to groups, organizational characteristics, and supervision to the software production process. They can contribute to knowledge by developing and applying their own metrics across the range of activities encountered within IS departments.

If IS management quantitatively define their objectives, decide on appropriate metrics, and measures their productivity, they will be better able to meet the challenges of top management.

## References

[1] N. Anderson, and B. Shneiderman, Use of Peer Reviews in Evaluating Computer Program Quality, Proceedings of 15th Annual Conference of the ACM Special Interest Group on Computer Personnel Research, (Aug., 1977).

[2] I. Benbasat, and I. Vessey, Programmer and Analyst Performance Measurement, MIS Quarterly, 4(2), (June, 1980).

[3] B.W. Boehm, J.R. Brown, H. Kaspar, M. Lipow, and M.J. Merritt, Characteristics of Software Quality, (North-Holland Publishing Company, Amsterdam, 1978).

[4] M.H. Halstead, Elements of Software Science, (Elsevier-North-Holland, Inc., 1977).

[5] P.J. Hoffman, The Paramorphic Representation of Clinical Judgment, Psychological Bulletin, 57(2), (1960) 116–131.

[6] J.W. Payne, M.L. Braunstein, and J.S. Carrol, Exploring Predicisional Behavior: An Alternative Approach to Decision Research, Organizational Behavior and Human Performance. 22 (1978) 17–44.

[7] L.H. Putnam, A General Empirical Solution to the Macro Software Sizing and Estimating Problem, IEEE Transactions on Software Engineering, SE-4(4), (July, 1978) 345–361.

[8] L.H. Putnam, and A. Fitzsimmons, Estimating Software Costs, Datamation, 25(9), (10, (11), (Sept., Oct., Nov., 1979).

[9] Society for Management Information Systems, Changing Aspects in MIS Management, Panel Discussion, Proceedings of the 11th National Conference, Minneapolis, (Sept., 1979).

[10] C.E. Walston, and C.P. Felix. A Method of Programming Measurement and Estimation, IBM Systems Journal, 16(1), (1977) 54–73.

[11] W.A. Wulf, Programming Methodology, Proceedings of a Symposium on the High Cost of Software, J. Goldberg (ed.), Stanford Research Institute, (Sept., 1973).

[12] M.V. Zelkowitz, Perspectives on Software Engineering, Computing Survey, 10(2), (June, 1978) 197–216.
