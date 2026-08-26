---
otero_id: 18660
otero_key: "N5WXYS3B"
title: "Cost comparison for the development and maintenance of application systems in 3rd and 4th generation languages"
authors: "Franz Lehner"
year: "1990"
journal: "Information & Management"
doi: "10.1016/0378-7206(90)90067-r"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cost Comparison for the Development and Maintenance of Application Systems in 3rd and 4th Generation Languages

Franz Lehner

Institut für Wirtschaftsinformatik und Organisationsforschung, University of Linz, A-4040 Linz/Auhof, Austria

Application systems represent considerable assets in many companies today. What they do is essential to the company's activities. This leads to an increasing lifetime of application systems. It may be presupposed that the costs for application systems may be more strongly influenced by management than by any other factor. Using data on costs for applications development and maintenance, this paper compares life cycle curves on the basis of empirical data. The basis for cost comparison is a longitudinal field study of the life cycles of application systems developed in third and fourth generation programming languages. This field study is complemented by a summary of the results of other studies.

Keywords: Software life cycle, Phase concept, Programming productivity, Maintenance, 3rd generation language, 4th generation language.

![](/api/attachments/N5WXYS3B/fulltext/images/a250a7119fd2af4ecd51ad74e85aeec7702fbfe300e7192fb29ae35b9aba4154.jpg)

Franz Lehner, born in 1958, has been assistant at the Institute for Organizational Research at the University of Linz, Austria, since 1986. Before this he gathered experience in the field of EDP as head of the educational center at a software house and as an independent consultant. He specialises in the management of computer applications, the development of informatic strategies, and the effects of technological change on organisational structures.

## 1. Introduction

Application systems represent considerable assets in many companies today. What they do is essential to the company's activities. This leads to an increasing lifetime of application systems. New developments in and the replacement of existing systems would often involve greater risks than adaptive maintenance or the extension of functions. Thus the importance of maintenance is growing. Until recently, most approaches to the problem were aimed at reducing maintenance efforts by using software engineering tools. Realising this potential requires, however, intensified support from management. The use of the lifecycle model allows for budgeting and personnel planning with regards to the prognosis for probable maintenance costs. It is to be avoided that the maintenance activity takes place as an unplanned and uncontrolled process.

Fourth generation programming languages (4GL) arouse a multitude of expectations on the part of both software designers and end users. Their hopes encompass, in particular, effects that increase productivity in the design of application systems. The rising interest in 4GL can be attributed to application design and maintenance backlogs that have accrued in many firms. Another factor proves to be reduction in maintenance costs for application systems already in service.

We still lack a definition of 4GL that is generally accepted. One of the main causes seems to be that they cannot be viewed in isolation: they have a close relationship to data base systems, end-user tools, and the like. Our definition encompasses all non-procedural programming languages. In addition, all tools for the design of application systems that incorporate at least the following properties are included: prototyping-oriented transaction development, standardized interface to a relational data base, and a report generator. For further details, see $[2,12,15,16]$ .

## 2. The Meaning of Programming Productivity

Despite pertinent differences in the term and its interpretation, the notion of programming productivity is so central to the discussion of the utilization of 4GL that more precise treatment is necessary. Professional literature and publications by producers and marketeers of these programming languages have made euphoric claims regarding increased productivity. These claims go as high as 10 times the productivity of third generation languages.

An objective increase in productivity is not disputed [compare 13, 14]. Although a clear increase is documented from second to third generation languages, productivity rises within third generation languages have been negligible. Studies have shown that even the effects of new methods (e.g., structured programming) are not predictable. The differences among programmers in the design of new programs is 16:1; in maintenance, 10:1. Through prototyping, fourth generation languages deliver clear improvements in the design phase, although the exact degree is disputed. A realistic measure of increased programming productivity seems to be a factor of 4 for simple programs and significantly less for complex programs. The price of this increased programming productivity tends to be an increased use of resources (CPU, I/O, memory) during program execution.

We must question whether productivity measures the relevant phenomenon that will permit us to compare the effects of the utilization of 4GL in various businesses. The meaningfulness of the measure, lines of code (LOC) per person-day, serves as an example. This is not suitable as a direct comparison because of the differences among programming languages. Furthermore, empirical studies have established that factors such as the size or complexity of the task at hand profoundly influence productivity [7].

What expectations does a business vest in a rise in productivity? Shorter development time, lower costs, or a longer service life of the application systems must emerge. Jones [10] found that two factors are intended when using the term programming productivity: reduced time for the development of new systems and diminished acquisition costs. This is in contradiction to the conventional economic definition of the term productivity, wherein the invested work (time or costs) is compared to the quantity produced. Thus the formulation of a system of goals is particularly important in order to be able to evaluate the utilization of 4GL.

## 3. Goals and Prerequisites for Utilization of 4GL

A closer look at the goal of increased productivity reveals other concealed goals. The goals of various user groups differ vastly. The following is a grouping of users with examples of goals listed in parentheses:

\- software houses (portability, flexibility, compatibility with standard software, rapid development, independence from system environment),

\- centralized data processing departments (reduction of application backlog, rapid development, low price, easily learnable, acceptable level of resource use, compatibility with system environment), and

\- end users in specialized departments (information independence, individualized data processing).

Theoretically, the goals should be formulated first and only then should the programming language be chosen. In the field, one often finds the opposite: the setting of goals for the service expected of the language is influenced by the functions and properties of the programming language. The identification of user groups has the advantage of taking the business aspects into account rather than the technical ones. Technical advantages of a programming language permit usefulness without demanding it. This leads us to consider other than technical aspects.

Many publications on the subject of 4GL carefully restrict potential areas of application (e.g., to simply structured tasks or pure queries) or match the areas to the properties of the programming languages. Application systems whose size or complexity requires a considerable organizational effort cannot be produced more quickly or made more accessible with 4GL. A clear indicator of this is the fact that reports of the successful use of these languages tend to come from software houses or very large businesses [1,14] which have the necessary personnel capacity for system planning and the important prerequisites (e.g., adaptation to various hardware) for the use of 4GL. A sudden change or a multiplicity of hardware are not, however, typical of the implementation of application systems in business.

## 4. The Life Cycle Model as a Basis for Comparison

The term software life cycle is often used synonymously with the concept of design phase. The two terms, however, describe essentially different things. The first, contrary to the design phase concept as a purely procedural approach, is used to emphasize the iterative and cyclical nature of the design and maintenance process. The implementation and maintenance phase usually is given special treatment.

Life cycle theory has long been known as a valuable instrument in the analysis of the dynamic development of products. The product life cycle combines a view that deviates from the phase concept with variable objectives. The idea of planning, monitoring, and controlling application systems in accordance with their life cycles was adopted from the product life cycle concept. Each application system is regarded as a product in its life cycle of four phases: system development and implementation, growth, maturity, and decline [8]. The individual phases of the life cycle are not artificial constructs but observed developmental stages in the life of an application system, the differenting and distinguishing of which should support decision-making.

Four goals accompany the application of life cycle theory: mapping, explanation, prognosis, and organizational goals. The mapping is the determination and representation of the costs of an application system. Building on the mapped costs, one seeks, on the basis of the explanation goal, to recognize connections in the origin of these costs. Categorizing the cost-producing elements with respect to the individual phases of the life cycle clearly shows the validity of the Law of Pareto, the so called 80/20 rule, that tells us that there are always a small number of elements (say 20%) which represent a large part (say 80%) of the cumulative costs. With the prognosis goal, one strives to make predictions about expected costs of an application system during its entire life cycle or in individual phases. The organizational goal encompasses the main focus of the application of the theory. The organization is assumed to be goal-oriented. This goal seeks to produce more cost-efficient application systems, i.e., a better relationship between system capabilities, duration of use, and investment.

Attempting to transfer the concept of product life cycle unchanged to application systems leads to contradictions. The design and maintenance of application systems are not production processes but product design processes. Likewise introduction and implementation (“sale”) do not occur under market conditions. In order to be able to formulate concrete goals with respect to product lifetime of an application system, we first need to analyse the starting conditions. Clarification of terms that make the dimensions of the problem recognizable lie in the answers to the following question: What empirical regularities are there in the design and maintenance of an application system?

The author carried out an investigation to clarify the empirical similarities. The goal of the study was to compare application systems developed in 3 and 4GLs. The users' expectations were compared in the effects on development time and maintenance costs during service. A life cycle model was chosen as the basis for comparison; it is particularly suitable because it affords a longitudinal section of the development and service life of an application system. The effects of the use of 4GL should be clearly demonstrable.

A particular problem was encountered in defining measurement quantities used to follow the development of the application system. Traditional quantities, such as turnover or profit, used in product life cycle have no equivalent. Likewise, the existing theoretical life cycle models cannot be transferred to application systems, because of the lack of prerequisites. Based on data found in the field, the description of the life cycle of application systems will use maintenance investment and frequency of use. Similar to the product life cycle, the indications are that the life cycle of application systems are not autonomous, but embody a dependent variable that can be consciously controlled.

## 5. Choice of Businesses and Procedure

The collection of data on the development and maintenance of application systems extended from January 1987 to June 1988. Because the study required longitudinal data about the life cycle of application systems as well as about the organisation of its management, businesses that fit the profile were approached for records of this kind of data. The study was conducted among the 80 largest businesses in Upper Austria. Only about 20 of these systematically recorded data that could be useful in our evaluation. For the description of the life cycle, the two quantities maintenance investment and frequency of use were used, where:

\- maintenance investment is represented by the number of program changes, programming hours per application system, maintenance costs per period, etc. and

\- frequency of use from transactional statistics, terminal statistics, billing statistics, resource use (CPU, storage, printer) etc.

Of 20 businesses with systematic records, 16 had data suitable for statistical evaluation (i.e., values on a monthly basis over a period of at least three years). The fact that practically every business used a different form of record keeping proved to be a particular problem for the compilation of statistics. The reasons for this are numerous. Differences in frequency of use are partially explained by variations in the operational systems transaction concepts or through various logging systems. As far as maintenance investment is concerned, the data was collected in various businesses by time units, frequency of changes or costs, and compiled according to very different activities, programs, areas of application or periods. This reflects a lack of understanding of the management aspects in the businesses rather than specific management goals. Systematic recording of growth data for application systems, personnel requirements, and development costs were not found anywhere.

It is interesting to compare the study by Lientz and Swanson, where they also found that only a few businesses maintained “good data concerning maintenance activities. In three cases the businesses even refused to provide any data, so that, in the end only 13 businesses remained for further analysis. Their reasons were the additional work load on their employees and internal rules forbidding passing information to persons outside their business.

## 6. Relation Between Age and Maintenance Costs

One hypothesis is that maintenance costs tend to escalate with the age of an application system. This is based on the theory of continuous growth. A further explanation resides in analogy to the area of capital investment. The so-called “bath tub curve” describes the empirically documented fact that early breakdowns of a machine are, at first, caused by a rather large number of errors. After an installation period, the number of errors falls off to just random failure. With age, the number of errors rises again. Such an analogy has problems, because no “wear” occurs in software systems. Paradoxically, however, maintenance itself can be a cause of “wear”.

References to the law of statistically continuous growth can be found in professional literature. The growth of large application systems in the long run is subject to an increase in the amount of code and the number of modules. This could serve as an explanation for an ascending error rate or increasing maintenance costs in old application systems. The constant addition of new functions to an application serves to explain its ever-increasing size. Meanwhile, functions that are no longer needed are seldom removed; they are simply disabled. This is partially a precaution intended to avoid undesirable side effects and partially a matter of convenience or time-imposed stress.

Lientz and Swanson statistically documented the relation of age to maintenance costs. Stearns undertook the documentation of this relation in terms of the life cycle curve. According to him, the graph of maintenance activities inclines sharply after installation in business. Stearns credits this to the detection of errors. Maintenance costs then fall by about half, but begin slowly but continuously to rise with increasing age. This opinion was adopted uncritically by many publications and is still considered valid today, although no proof was produced by means of longitudinal studies.

![](/api/attachments/N5WXYS3B/fulltext/images/057128e6276109ac6da2c85efaeabf17091de1726b59c79113b36bf70e28012e.jpg)  
Fig. 1. Maintenance Curve of a Personnel Information System.

Seibt comes to the same conclusion in a study of a personnel information system. This is the only documented life cycle in literature in the field that extends over several years. Fig. 1 shows the curve of the maintenance costs of the personnel information system over a period of eight years. The graph depicts relative changes in the annual share of maintenance costs relative to the total costs of development. The total costs are thus 100% at implementation time at the beginning of operations.

Seibt's interpretation of the curve clearly reflects the above hypothesis: The drop in the percentage share of total costs for maintenance in the first three years of operation is the result of increasing stability of the software because of the elimination of errors and increasing efficiency of the programs. The increased share for maintenance in the fourth year reflects an increase in internally (= personnel department), the number of built-in special cases, and changes necessitated by external factors.

An empirical study by Selig was the first to question this relationship between age and maintenance. Selig concluded that an increased percentage share for maintenance with the increasing age of an application system cannot be supported by the data he collected. He also studied the life cycles published by Stearns and concluded that a time-shifted summation of such curves produces a constant share for maintenance. A cross-sectional view of all application systems does not suggest an increasing share of maintenance costs with advancing age of the system.

Further aspects, such as interdependencies among individual application systems, influences of new programming languages and tools, prototyping, etc., need to be included in newer studies; the following basic criticism needs to be stated:

\- Cross-sectional studies are methodologically unsuitable for examining maintenance costs over time.

\- The life cycle documented by Stearns only extends over 18 months.

\- The number of application systems studied so far is too small to produce a useful result.

The results obtained by Selig can be stated more precisely: the hypothesis that no relation exists between maintenance costs and the age of an application system is largely supported; certain environmental influences strongly influence the maintenance costs. Application systems in a dynamic environment show distinctly higher average maintenance costs and an irregular curve for the graph of maintenance costs. Such irregularity seems to have deluded observers in the past – over time periods that were too short and with inadequate data – into believing that maintenance costs rise almost linearly with age.

## 7. Results of the Study

Two basic types of life cycles can be distinguished. In one, we have a nearly ideal curve. Alter implementation of the application system, the maintenance investment fluctuates around a low base level. In the second, the curve behaves irregularly. The evaluated life cycles displayed large variance, which could, however, partially be explained by a project-oriented organization. Reasons for maintenance can vary extremely in individual cases, regularities could be observed that were the result of either maintenance organization (periodic meetings of the maintenance committee or a “watering can” policy) or the area of application (e.g., modification of an inventory program at the start of a new year).

Fig. 2 shows a characteristic example of an irregular life cycle curve. The main cause of irregularity can be seen in the dynamic environment of such application systems. Characteristics of a dynamic environment include a high level of competition (e.g., in large wholesale houses) or frequent changes in applicable laws (e.g., tax write-offs for stocks in the banking business). The dynamics of the environment are reflected in a high measure of

![](/api/attachments/N5WXYS3B/fulltext/images/38a9fd5ac9eb73b3f59dc5272ee3bd6f36c3b992a8beebb66b5883a358c57404.jpg)  
Fig. 2. Maintenance Curve in a Dynamic Environment (Programming Languages PL/1 and RPG II).

variance in the maintenance investment, an unfavorable relation between design and maintenance investments, and difficulties in distinguishing the life cycle phases. Such environmental dynamics, which are not rooted in the application system itself, lead to a maintenance curve that is most difficult to represent and predict.

Fig. 3 shows the life cycle of an application system that is typical for the class of systems having a regular curve. A static environment is the most important requirement. For application systems with static environments (i.e., few unpredictable external influences on maintenance), the maintenance investment fluctuates around a low level after implementation. Such life cycles are typical of applications in areas such as wage and salary accounting and bookkeeping. Other factors – such as work organization in programming, personnel capacities, the decision-making process, or seasonal differences – can be ignored, because they scarcely affect the trend of the curve.

![](/api/attachments/N5WXYS3B/fulltext/images/96606eefcf9aef755abf64af3975138c5fe3cbc94412e47eb8431b69369b2f8b.jpg)  
Fig. 3. Maintenance Curve in a Static Environment (Programming Language PL/1).

An intuitive explanation of the results can be found in Sneed, who establishes that the life cycle of an application system is determined by its static or dynamic environment. He distinguishes between three types of systems: disposable, static, and evolutionary. The first two reflect a static environment, while the latter is a dynamic environment.

Disposable systems are, in part, the result of individual solutions. They arise, however, in the maintenance or upgrading of application systems (e.g., to support a conversion task). They have only local importance and can generally be designed with little investment. Their lifetime generally extends less than a year. They are neither maintained nor enhanced. They are replaced as needed. Their maintainability is therefore irrelevant.

Static systems are integrated operative applications for a clearly defined area of application. They have global importance, but tend not to be enhanced after implementation. The annual rate of modification is under 10%. Alter their design, they remain in service until they are outdated by technical or application-oriented developments. With an average design time of up to two years and an average lifetime of up to seven years, maintenance definitely takes place. Such application systems must be conceived, from the start, in a maintainable and expandable way.

The design of evolutionary systems can stretch over many years. The application is either insufficiently defined or in a state of flux, so that the design phase is never completely terminated. Maintenance and continuing design are hardly separable. This kind of application system is to a large extent a model of reality and thus subject to changes in that reality. A different set of rules applies than those for simple static systems. Often these are the central and strategically important application systems of a business (e.g., merchandise policy in trade production planning and control in industry).

The second part of the study dealt with those application systems developed with 4GL. Few of the companies could produce a combination of sufficiently long application experience and relevant record keeping. The study involved 15 application systems, grouped into the following programming languages: ORACLE (2), dBASE (1), POWERHOUSE (2) and INSIGHT (10). ORACLE is a hardware and operating system dependent tool for the development of application systems (UNIX environment) with SQL as its data base language. POWERHOUSE and dBASE are data base systems that employ nonprocedural programming languages. INSIGHT was developed especially for HP computers and includes a mask generator and a nonprocedural programming language.

![](/api/attachments/N5WXYS3B/fulltext/images/e06cd79664710826da0e3cdba6e4b42019330f5c30f1a75a34aaf754931ae641.jpg)  
Fig. 4. Maintenance Costs in a Dynamic Environment (Programming Languages 75% INSIGHT, 25% COBOL).

![](/api/attachments/N5WXYS3B/fulltext/images/340fd326022acc2ff3dc9c85f104d3a77359eddcbfd9f533be1a5b491669a023.jpg)  
Fig. 5. Maintenance Costs in a Static Environment (Programming Language INSIGHT).

On average fourth generation application systems required a shorter development phase. About half of the application systems were developed in part (15–50%) with conventional programming languages.

It is important to note that the sizes of projects in this group were significantly smaller than the others. This difference can be due to several factors. The use of fourth generation languages is considered experimental by many companies. The recognition that very large projects tend to be obsolete by the time they are finished has led to more modest program dimensions. For the sake of unity, enhancements, particularly more extensive ones, of existing application systems tend to be done in conventional programming languages. As far as the life cycle is concerned, the results are very similar to those of third generation languages. Figs. 4 and 5 show two typical life cycles of application systems that were produced with 4GL.

The high degree of similarity to 3GL can be explained as follows: the application backlog is an important problem. Because of the enormously increased demand for application systems, this application backlog has shifted from the programming area to the analysis and organization area. This means that it is not the capacity, in terms of programmers, that is creating the bottleneck but the preceding phases. For implemented application systems, regardless of the programming language used, the same regularities and influences seem to apply as far as maintenance costs are concerned.

Increasing the number of programmers can contribute little to solving the problem of the development and implementation of application systems. Raising capacity in the area of system planning seems to be much more important. This requires both a quantitative and qualitative improvement in personnel capacity, while prototyping, supported by 4GL, can also help.

## 8. Influence on Maintenance Costs

As far as can be determined by data in this study, third and fourth generation application systems differ primarily in size. Systems developed in 3GL are significantly larger in terms of development time and LOC. This naturally also affects the maintenance costs, as measured in terms of the total cost of developing the application system. If the life cycles are compared, however, then no structural differences can be determined.

Are there advantages in the maintenance of application systems that were developed in 4GL? This question deserves a conditional “yes” at this point. The increased productivity due to 4GL is limited by a lack of standards among these languages and the habit of solving certain problems via exits to 3GL. The necessity of such exits comes from a limited ability to represent complex algorithms in a 4GL; a further reason could be the use of capable standard software called via “own code hooks”.

Certain structural or other properties of newer programming languages do have a positive effect on maintenance costs. This could lead one to miss the point that actual maintenance costs arises from actual use of the application system. The major factors at play here are not so much the technical attributes of the programming language as the dynamism of the environment and the experience and acceptance of the user.

In summary, one must conclude that the utilization of 4GL reduces the application backlog but does not lead to any immediate changes in the maintenance situation.

## 9. Results of other Studies

The general situation regarding the utilization of 4GL is marked with a great deal of uncertainty in terms of the actual effect. The cause of this is their relative newness and the lack of available data. The studies can be grouped into four types.

## 9.1. Function Comparisons

4GL do not provide universal tools. They are often intended for restricted classes of tasks and limited user groups. In the selection of a suitable programming language, the user is confronted with methodological problems in formulating his selection criteria and subsequent evaluation of the product spectrum on the basis of these criteria. Function comparisons have the following goals:

\- overview of availability on the market:

\- analysis of the range of functions and capabilities of each; and

\- comparison of results as the basis for selection.

Diebold's study of software tools for the end user [3] serves this purpose well. Other models can be found in [4] and [15].

## 9.2. User Reports

The term “user reports” is intended to mean the results published by computer companies or users. Critical attention needs to be given to the fact that the conditions and methods used in the studies are not generally published. Repeating or critically analyzing the studies is very seldom possible. Examples of user reports can be found in $[5]$ and $[22]$ . Fig. 6 shows an example of users’ experience with 4GL. The illustration depicts a study carried out at the end of 1986 in German-speaking regions $[1,21]$ . The basis for comparison was the programming effort with 3GL, set at 100%.

![](/api/attachments/N5WXYS3B/fulltext/images/0014bd48d539462769c605e4850bb5726dd45c070bebf51d774e189370283f92.jpg)  
Fig. 6. Users' Experiences with 4 GLs.

<table><tr><td rowspan="2" colspan="2"></td><td rowspan="2" colspan="4">development design pgm test totals</td><td rowspan="2" colspan="2">resources CPU I/O</td><td colspan="2">productivity</td></tr><tr><td>LOC</td><td>LOC/h</td></tr><tr><td rowspan="2">S-1</td><td>COBOL</td><td>2</td><td>26</td><td>3</td><td>31</td><td>1</td><td>30</td><td>383</td><td>12</td></tr><tr><td>FOCUS</td><td>5</td><td>7</td><td>2</td><td>14</td><td>25</td><td>22</td><td>34</td><td>2</td></tr><tr><td rowspan="2">S-2</td><td>COBOL</td><td>12</td><td>30</td><td>13</td><td>55</td><td>1</td><td>11</td><td>530</td><td>10</td></tr><tr><td>FOCUS</td><td>1</td><td>2</td><td>8</td><td>11</td><td>16</td><td>64</td><td>62</td><td>6</td></tr><tr><td rowspan="2">C-1</td><td>COBOL</td><td>24</td><td>55</td><td>16</td><td>95</td><td>1</td><td>11</td><td>656</td><td>7</td></tr><tr><td>FOCUS</td><td>1</td><td>5</td><td>6</td><td>12</td><td>4</td><td>27</td><td>150</td><td>12</td></tr><tr><td rowspan="2">S-3</td><td>COBOL</td><td>2</td><td>16</td><td>8</td><td>26</td><td>1</td><td>13</td><td>108</td><td>4</td></tr><tr><td>FOCUS</td><td>1</td><td>1</td><td>4</td><td>4</td><td>2</td><td>17</td><td>4</td><td>1</td></tr><tr><td rowspan="2">C-2</td><td>COBOL</td><td>3</td><td>9</td><td>4</td><td>16</td><td>1</td><td>4</td><td>550</td><td>34</td></tr><tr><td>FOCUS</td><td>1</td><td>3</td><td>5</td><td>9</td><td>7</td><td>65</td><td>630</td><td>70</td></tr><tr><td rowspan="2">C-3</td><td>COBOL</td><td>4</td><td>40</td><td>30</td><td>74</td><td>1</td><td>64</td><td>893</td><td>12</td></tr><tr><td>FOCUS</td><td>12</td><td>19</td><td>18</td><td>49</td><td colspan="2">29593</td><td>333</td><td>7</td></tr></table>

Fig. 7. Productivity comparison: FOCUS-COBOL.

## 9.3. Productivity Studies

One example of a direct comparison of the productivity of 3 and 4GL is the Harel/McLean study. Fig. 7 shows part of their results. The figures on development costs are in person-hours. The authors distinguish two types of programs: simple (marked with an S) and complex (marked with a C).

The applications S-1, S-2 and C-1 were developed by beginners; the rest were developed by experienced programmers. The results show that greater differences were seen between COBOL and FOCUS solutions among beginners than among veterans. For organizations that plan greater decentralization of their applications systems development, appropriate conclusions can be drawn regarding the suitability of 4GL. In general, the reduction of the time investment by no means reaches a factor of 10; instead, it is significantly lower. For complex programs, this factor falls even more.

Jones reaches similar conclusions. However, in another comparison of FOCUS and COBOL, Bertelsmann observed time savings of 15 to 25%, and that only in the module development and the coding stages. Other stages showed no improvement [22]. It must be noted, however, that these types of productivity comparisons set the main emphasis of a study very one-sidedly, so that it is difficult to draw conclusions.

## 10. Conclusions

The empirical results of this study are based on a longitudinal study of maintenance and utilization tion of application systems. Because of the difficulty of representing the returns of an application system in a quantitative way, no profits can be shown to balance out the costs. The following conclusions can be drawn:

\- The hypothesis that maintenance costs for "old" programs are higher than for newly developed programs cannot be supported.

\- The classical life cycle as a normal distribution is not observed among application systems. Models known from diffusion theory are not applicable because important prerequisites for their application are not met.

\- A characteristic curve is seen to be typical for maintenance as well as for utilization of application systems.

\- The functions of this curves are different in a static environment (quadratic trend) and in a dynamic environment (1st order autoregressive process).

\- There are no differences in these functions between 3 and 4GLs.

The study leads to the conclusion that the utilization of 4GL alone does not lead to a change in the maintenance. A precise analysis of the development and maintenance of application systems in the business as well as the formulation of the system of goals for the use of 4GL need to be undertaken before utilization decisions are made. The life cycle is a suitable instrument for monitoring and controlling these tasks.

Furthermore the study supports the acceptance of the following statements:

\- A higher quality of programming education is required. Both old and new programming languages and methods need to be mastered, since many large third generation application systems with immense longevity are still present in the field and will be still further developed.

\- The complexity of application systems to be maintained will increase. The causes are rooted in the longevity, size, and complexity of the application systems, and in multi-organizational application systems. There are scarcely any pure application systems with fourth generation languages.

\- The programming effort for disposable programs (e.g., adhoc surveys) has frequently been attributed to maintenance. This effort can be significantly reduced by 4GL. In such a case, even the increased use of resources (CPU, I/O, memory) during program execution proves negligible.

\- Maintenance costs can be influenced or reduced (e.g. by tablemanaged maintenance, quota control tables). The reduction of maintenance costs, however, is often only apparent. It is transferred to the user and is no longer comprehensible.

\- Measuring the capability of programming languages in terms of productivity statements does not permit prediction of effects on existing bottlenecks in the development and maintenance of application systems. Thus productivity statements have limited practical value.

So far, management has had no pertinent way to describe application systems and monitor their use. The results of this study provides an empirically supported model that describe the evolution of an application system already in use. This model can be employed in order to obtain a better understanding of the use of information and communication techniques in a business. One can also obtain a glimpse into possible future developments and derive appropriate management strategies in order to coordinate the use of an application system with management goals. This enables the support of tasks related to the utilization and further development of application systems, which have for the most part evaded management and control (e.g., cost or personnel management).

## References

[1] Bauer, M.: Sprachen der 4. Generation. In: Bauer, M.: Strategien für den Datenbankeinsatz. Seminarunterlagen, Informatik-Training GmbH, Höristr. 4, D-7760 Rudolfzell, S4G-5–S4G-120.

[2] Bolkart, W.: Programmiersprachen der vierten und fünften Generation. McGraw Hill, Hamburg 1987.

[3] Diebold Deutschland GmbH (Ed.): Individuelle Datenverarbeitung, Softwarewerkzeuge für den Endbenutzer. Frankfurt 1982.

[4] Friedrichs, K.J.: Sprachen der 4. Generation: für wen, für was? Müller Verlag, Köln 1986.

[5] Grass, A. and Roth, M.: Erfahrungen mit Dataflex, einem 4. Generationsansatz für die PC-Welt. In: Information Management 2/1987, 44–48.

[6] Griese, J. et al.: Ergebnisse des Arbeitskreises Wirtschaftlichkeit der Informationsverarbeitung. In: ZfbF, 7/1987, 515–551.

[7] Harel, E.C. and McLean, E.R.: The Effects of Using a Nonprocedural Computer Language on Programmer Productivity. In: MIS Quarterly 2/1985, 108–121.

[8] Heinrich, L.J. and Burgholzer, P.: Informationsmanagement. 2nd ed., Oldenbourg Verlag, München/Wien 1988.

[9] International Data Corporation (IDC) (Ed.): Fourth Generation Languages in Western Europe. IDC Deutschland GmbH, Stuttgarter Strasse 10, D-6236 Eschborn, Eschborn 1987.

[10] Jones, T.C.: Effektive Programmentwicklung. McGraw Hill, Hamburg 1987.

[11] Knolmayr, G. and Disterer, G.: 4GL-Vergleich an einem Beispiel aus dem Berichtswesen. In: Computer Magazin 7/8/1987, 41–47.

[12] Kurbel, K. and Eicker, S.: Ein Streifzug durch die Welt der Programmiersprachen. Arbeitsbericht Nr. 10, Lehrstuhl für Betriebsinformatik, Universität Dortmund, Oct. 1987.

[13] Lehner, F.: Anwendungssystem-Management. In: Handbuch der modernen Datenverarbeitung (HMD), No 142,1988, 47–61.

[14] Lientz, B.P. and Swanson, E.B.: Software Maintenance Management. Reading/Massachusetts 1980.

[15] Martin, J.: Fourth Generation Languages. Prentice Hall, Englewood Cliffs 1986.

[16] Nelte, H.-U.: Produktivitätssteigerung durch Anwendungsentwicklung der 4. Generation bei Krupp MaK. In: Information Management 3/1986, 41–45.

[17] Scibt, D.: DV-Unterstützung des betrieblichen Personalwesens. In: Kay, R. (Ed): Management betrieblicher Informationsverarbeitung. Springer Verlag, München/Wien 1983.

[18] Selig, J.: EDV-Management. Springer Verlag, Berlin 1986.

[19] Sneed, H.M.: Software Management. Müller Verlag, Köln 1987.

[20] Stearns, S.K.: Experience with Centralized Maintenance of a large Application System. In: Parikh, G. (Ed.): Techniques of Program and System Maintenance. Cambridge, Mass. 1982.

[21] without Author: Complete Natural Adabas. In: Kompatibel 7/1985, 4–10.

[22] Wix, B. and Balzert, H. (Eds.): Softwarewartung. Bibliografisches Institut, Mannheim et al. 1988.
