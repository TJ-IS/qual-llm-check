---
otero_id: 23400
otero_key: "URZH22D3"
title: "Achieving flexible information systems: the case for improved analysis"
authors: "Guy Fitzgerald"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.3"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Achieving flexible information systems: the case for improved analysis

GUY FITZGERALD

Oxford Institute of Information Management, Templeton College, Oxford OX1 5NY

Abstract: This paper examines the problems of change that continue to thwart the development of successful information systems. The symptom of maintenance is discussed and a variety of techniques and methodologies that seek to provide solutions are discussed. Changing business needs and user requirements are identified as enduring problems and the technique of Flexibility Analysis is proposed. Finally some preliminary results from a research study are discussed. The study looked at a number of information systems in organizations and examined the changes and enhancements that were subsequently made to those systems and the reasons for them. The results indicate the benefits and practicality of the technique of Flexibility Analysis.

## Introduction

The traditional systems development life-cycle is the way that information systems have been developed in the past. This approach has until relatively recently been practiced almost universally. Indeed some more recent approaches still exhibit many of the traditional life-cycle's characteristics but have simply changed the techniques and tools that are applied. This paper begins by examining the traditional life-cycle and identifies its deficiencies concerning the handling of change.

## Maintenance problems

The earliest recognition of the problem of change concerns maintenance. Maintenance of computer systems, once they were implemented, was observed to be absorbing disproportionate amounts of the data processing departments' time and effort. A number of authors quoted the statistic that about 70% of data processing resources were engaged in maintenance (Boehm, 1976), and as a result only 30% of the resources were available for the development of new systems. This in turn gave rise to the 'backlog problem'. That is the number of systems waiting in the pipeline to be developed. For a particular system there may be a considerable delay before resources can be devoted to developing that system. It has been calculated that in some organizations there is on average a three year backlog of systems waiting to be developed. Some commentators have also identified an 'invisible backlog'. This is the number of potential applications that might make sense to develop but have not been put forward due to the length of the application backlog.

Maintenance is usually identified as having two components: corrective work and enhancement work (Boehm, 1976), although some have identified three or even four categories (Lientz and Swanson, 1980). Corrective work is that which is necessary to make the system meet the original specification, i.e. remedial work to overcome problems in design and errors in programming and implementation. Enhancement work involves adapting the systems to accommodate changes to the specification, i.e. they are not due to errors in the system that has been constructed but are the result of changing user requirements. Studies have shown that corrective maintenance typically accounts for only a very small proportion of total maintenance costs, the actual figures varying between 2% and 12% (Ward, 1985; McKee, 1984).

Many attempts to reduce the levels of corrective maintenance have been made and some have been very successful. The development of software engineering techniques was largely a response to this problem, better designed and constructed programs, it was argued, would be easier to understand and therefore maintain. The use of Software Metrics (Gilb, 1977), Inspection Methods (Fagan, 1976; Fagan and Larson, 1976), and Quality Assurance techniques (Boehm et al., 1978) have also attempted to reduce the problem of corrective maintenance. More recently the development of formal methods, i.e. the mathematical expression of specifications and the ability to prove program correctness, seeks to continue that

improvement.

Software engineering of course addresses more than just the problem of corrective maintenance; any change, for whatever reason, will be much easier to achieve if software engineering principles have been employed. It has been argued that the widespread use of software engineering techniques has resulted in the reduction of the maintenance workload from approximately 70% to approximately 50%.

## Specification of user requirements

Most research effort has been devoted to addressing the problem of corrective maintenance and yet, as indicated earlier, corrective maintenance forms a relatively small proportion of total maintenance. Enhancement maintenance is where the real problems lie.

There are two basic reasons for enhancement maintenance. Firstly it might be caused by the fact that the original user requirements specification was not a true and accurate statement of the users' actual requirements; or secondly because the requirements of the business and users have changed since the requirements specification was produced, and so the associated computer systems need to be changed.

The cause of the first problem is often laid at the door of the documentation inherent in the traditional approach to systems development. The documentation is often very descriptive, particularly the specification of users' requirements. This natural language, narrative type description, is not a good way of specifying a process in an unambiguous way. The descriptions are generally long, unstructured and repetitious, so it is very difficult to be clear and precise. It is also very different to verify that it is correct. Such a specification is thus not a good communication tool and is also for the same reasons very difficult to update. Furthermore the idea that users or user management can 'sign off' the specification as an accurate statement of their exact requirements is very difficult if the specification is unstructured and ambiguous. The documentation argument thus asserts that user requirements are inadequately stated, and therefore not properly understood or validated by the users, due to the poor nature of the specification medium.

A number of attempts have been made to overcome this aspect of the problem. The most popular probably being the development of graphical techniques for use in the requirements analysis process. Data flow diagrams (DeMarco, 1980) and entity models (Palmer and Rock-Evans, 1981) are both important and, in one form or another, widely used techniques that have been designed to help overcome the requirements specification documentation problem. Both techniques are stated to be easy for users to learn and understand, and thus enable much improved user participation in their construction and validation. These techniques are widely regarded as having improved, amongst other things, the specification of user requirements.

There remains an inherent problem with any document based specification, be it natural language, mathematics, or graphics, or indeed any combination. The specification is simply an abstract representation of user requirements, and it can never be an adequate substitute for the user seeing the system itself. What is required is a more tangible representation that the user can 'see' and interact with. This has led to the concept of prototyping. A prototype is essentially a rapidly developed mock-up or skeleton of the required system that can be shown to the user and changed as the actual requirements are evolved through use and experiment with the prototype. The idea of a software prototype as a way of accurately obtaining the user requirements has many advocates and has, in certain circumstances, proved extremely successful (Bally et al., 1977; Dearnley and Mayhew, 1983; Hekmatpour and Ince, 1986; Nauman and Jenkins, 1982). Sometimes the prototype may not only be used to help capture and refine the user requirements but may actually be used as the specification itself.

These developments have undoubtedly contributed to the process of obtaining and documenting the user requirements specification. However they do not address the second problem which is that user requirements often change after the specification has been developed. The idea of the user 'sign off', discussed earlier, implies that the requirements are frozen and will not change during the development process. In a large development project lead times of two or three years, or even longer, are not uncommon, and to have the requirements frozen in this period is not realistic, although it is frequently attempted. Where the requirements have been frozen, and subsequent circumstances change, the result is user dissatisfaction and an immediate catalogue of change requests once the system is implemented.

## Evolutionary development

It is clear that the business needs to at least react to changing external circumstances during the development of a project. But is it realistic to ask systems developers to build systems where the requirements specifications is liable to keep changing during the development process? In practice this happens and the user may demand that the developers change the system to cope, despite the cost in terms of time and effort.

In order to achieve this type of evolutionary development the use of support tools is usually necessary and a form of prototype without a 'final version' gives the possibility of iterative revisions even when the system is live (Avison and Fitzgerald, 1988). Such a prototyping system must be efficient enough to allow its immediate use as the application system. In effect, according to Sibley, there is a trade-off between capitalizing reprogramming costs and paying for overheads during run-time, and there now exist a few products that are sufficiently advanced to allow users this option (Sibley, 1986).

## Methodologies

Apart from these various individual techniques a wide range of information systems development methodologies have been developed in recent years that would also claim to help solve the problems of change.

Over 300 such methodologies have been identified and although many of these are only separated by marketing needs there is nevertheless still a wide variety. Most methodologies claim, although not always explicitly, that the addressing of maintenance and the overcoming of maintenance problems is a prime objective. However, it has been observed that few deal specifically with maintenance as a part of the methodology. It is usually simply argued that the improved development approach of the methodology will lead to a reduction in maintenance. We are generally left to guess whether they are referring to corrective or enhancement maintenance. Some argue that it is greater participation of the users that leads to improved accuracy of user requirements analysis. Others argue that it is improved by the use of the graphical techniques promoted by the methodology. A survey of 24 methodologies found 12 that claimed to cover requirements analysis and specification and of those the method in which the completed system is validated against the original requirements was almost exclusively by traditional user acceptance testing. Only two methodologies suggested the use of prototypes or other tools (Wasserman et al., 1983). It would thus appear that methodologies really only indirectly address the problems associated with change.

## Analysis of future changes

If all corrective maintenance and all enhancement maintenance due to problems with accurately specifying the user requirements were to be eliminated, we would still be left with some maintenance due to changing circumstances and changing user requirements. Admittedly improved development processes might make such change easier but change would continue to be necessary. What can be done about this? One possibility for improvement is to try and predict the changes that might prove necessary in the future. This is referred to in a number of systems analysis textbooks but is in practice hardly ever performed. Land (1982) proposes that the life-cycle be amended to include a 'futures analysis' stage. The stage is described as identifying the major areas in which change is possible. Various techniques are suggested such as Delphi and brainstorming methods, statistical analysis and simulation modelling. The resulting areas of possible change should be fed into the design stage where the implications could be analysed and if appropriate the designers would ensure that accommodating these changes would be relatively easy in the future.

This kind of analysis would seem to be eminently sensible and would probably lead to more flexible systems and thus reduced maintenance. It is unlikely in practice that all future changes could be predicted in this way but even if only a few were identified it would be beneficial. Current analysis techniques tend to adopt the snapshot view which implies that the only aspect of interest is what is happening today. The analysis stage documents the current situation and then any modifications required for the new system are specified in order to define the 'as should be' model. Analysts try to include any new requirements but do not search for what these might be other than to ask the end-users if they can think of any improvements. The improvements that are suggested are typically low-level changes to interfaces and minor adjustments to existing functions.

These kind of improvements are generally ones that the user community already know about, sometimes these improvements are the reason for developing the new system in the first place. What we are not so good at is identifying possible events or changes that might occur in the future which will fundamentally affect the system. As a starting point we need to know the factors which might change and affect the user requirements. Land has suggested that the major categories are:

\- changes in available technology;

\- changes in legal requirements;

\- changes in economic and environmental factors;

\- change in attitudes, expectations, tastes, or in climates of opinion;

\- changes within the organization.

Longworth (1985), as part of an NCC study based on some user experiences, has also identified some causes of change:

• government legislation;

\- impositions of organizations that supply data, e.g. banks;

\- impositions of organizations which accept data, e.g. Inland Revenue;

\- changing user requirements, e.g. organizational structure, policies, takeovers,

\- Changing DP requirements:

\- new philosophies, e.g. distributed processing, database

\- changes of hardware

\- changes of software

\- new performance requirement, e.g. security or accuracy

\- withdrawal of maintenance support

\- new contingency plans, e.g. industrial action

\- staff turnover, e.g. help facilities required

\- removal to a new site

\- changes to interfacing systems.

These are useful checklists and would appear to be a good starting point for what I have termed Flexibility Analysis. Yet in a study of a number of popular methodologies, none provided any such checklist, nor any recommendations, steps, or techniques that would be relevant to any type of Flexibility Analysis. Only one methodology mentioned the desirability of such analysis and then provided no detail.

The probable reason for this lack of advice concerning futures analysis is that whilst it is desirable and may reap significant benefits it is actually very difficult to do. Some of the reasons for this are suggested (Fitzgerald, 1988) as follows:

\- it requires significant management commitment;

\- it asks uncomfortable questions, e.g. what are the prospects of structural reorganization. There may be good reasons why this must not become widely known, or indeed known that management are even contemplating the possibility. Organizational politics are involved;

\- it requires an open, participative style of management;

\- it prolongs the analysis and design stages and as a possible result the implementation date;

\- it requires resources;

\- it requires experienced analysts and designers;

● analysts are not trained for this kind of analysis;

\- it requires insight into the business and its internal and external functioning, relationships, and organizational culture;

\- it requires political awareness.

## Flexibility Analysis

Despite these formidable problems a recent study (Sutton, 1988)\* indicates that not only is this kind of analysis desirable but, also possible and practical. This study analysed 20 computer systems, of various different types, that had been implemented over the past few years. All these systems have been the subject of various forms of enhancement maintenance since they were implemented. The reasons for these enhancements have been analysed and broadly fell into three main groupings; environmental, technical and organizational.

Environmental changes are basically external influences on the organization, for example government legislation, dependencies on external agencies, and changes in social behaviour or expectations which affect the industry within which the system is active. Organizational change refers to influences from strategy, policy, organizational structure, procedures, etc. Technical change is caused by developments in hardware, software, communications and the technical environment in general. The initial analysis of the major changes that occurred to the identified systems identified five to be due to environment changes, three to technical developments or constraints and the remaining twelve to organizational changes. More detailed analysis, including interviews with some of the people involved, refined the categories further. Organizational changes were subdivided into:

\- strategy/policy

\- logical structure

\- physical structure

\- financial constraints

\- procedures/process

\- personnel.

Technical aspects were subdivided into:

\- future (new) products

\- supplier stability.

Environmental aspects were subdivided into:

• government legislation

\- industrial relations

● external agencies (suppliers/customers).

This refined categorization highlighted a number of problems. Firstly it was not always possible to allocate a change to just one particular category and secondly that some categories were overlapping. Nevertheless after the further analysis it emerged that approximately 70% of the enhancements to the systems could be attributed to organizational factors. The majority of which were internally controllable by the individual organizations. The implication being that the system development personnel should be more aware of the potential of these organizational factors to change and take account of them in their system designs.

The study also examined the system components that needed to be changed in each case. The affected components were; hardware, software, interfaces, data, and processing. The results showed that both data and processing were the components most sensitive to change and thus were deserving of special attention in design to achieve flexibility. The fact that data and processing emerged as just about equal is interesting as it is often argued that data is more stable than processes and is thus a better basis upon which to construct information systems. It is suggested that this aspect needs further investigation and

research.

As part of the study the degree to which the change could have been predicted was examined and whilst this is somewhat subjective and based on hindsight some interesting results emerged. The majority of major changes were planned by the organization over a considerable period of time and were not the result of sudden impulses. However these changes often appeared as bolts from the blue to the systems developers and maintainers.

It was discovered that 45% of the changes analysed were known about by the functional area concerned during the development stages, and that a further 50% were thought probably to have been known about by somebody in the organization, although not by the developers. Only in one case was the cause of the change thought not to have been known about during development. The implication being that a large proportion of major changes to our information systems are potentially predictable. The arguments for performing some kind of Flexibility Analysis seem to be quite strong.

## Performing Flexibility Analysis

The arguments against have been discussed above. These are mainly of a practical nature and although they are significant they may not be insurmountable. A number of ways of overcoming these problems are proposed.

Firstly that we must take time, despite the continuing pressure of deadlines for Flexibility Analysis. In the past, time has been found for analysis and design techniques that have been shown to be beneficial, despite the arguments that their use would increase the overall development timescales. For example, software engineering techniques increase the time and effort required at the program design stage but they are seen to be worthwhile in the long run. Further research and practical experiments will help in this process.

Secondly it is argued that the development of Flexibility Analysis support software can overcome some of the problems identified above, some features of such a support system are described in a related paper mentioned earlier (Fitzgerald, 1988).

Thirdly it is argued that a stage of Flexibility Analysis must be included in the analysis stage of systems development. This does not mean that it must be part of, or an acceptance of, the traditional life-cycle and methods. It could well be used alongside prototyping for example, or included as part of almost any methodology.

Wherever it fits the stage should include a detailed examination of potential changes to the organization, the business, and the environment in which the system is being developed in the short, medium and long term. This task is probably not the province of systems analysts as we currently perceive them. It would need to be performed by a team (a Flexibility Analysis Team) that includes senior functional and strategic management and representatives of important groups in the business, for example lawyers, suppliers, trade unionists. This analysis of potential changes should not be restricted in the first instance, it should be as wide ranging as possible. When potential change scenarios have been identified, the impact or effect they might have on the system under consideration is assessed. Once this has been achieved a process of allocating probabilities to each change scenario can be attempted. This may result simply in changes being categorized as probable, possible and unlikely, if this is the most that people will commit to, or it may be a more sophisticated categorization.

As an example, in one company the impact of a particular potential piece of legislation on a system was thought to be high and the probability of that legislation being enacted in some form within five years was assessed as probable. This information had not previously been considered by the system developers although once presented with it they thought it to be of significance.

Another example considered the possibility of future organizational change in terms of restructuring of management roles and responsibilities. This it was concluded was unlikely although it was recognized that if it did happen its impact could be enormous on the system under consideration.

In principle any changes identified as being probable and with the greatest potential impact should be revisited so that the Flexibility Analysis team can spend more time on them and make sure that their original assessments were correct. This may involve detailed analysis dealing with people that would not normally be involved in the systems development process. The results of this Flexibility Analysis should then be fed into the systems design process.

The design team should evaluate them in terms of how easy or difficult they would be to achieve given the existing user requirements and system design. Some potential changes may be relatively easy to incorporate in the design. This means that it is relatively easy to design the system in such a way that should the identified change be needed it could be achieved without major upheaval or redesign being necessary. Examples of this might be something as simple as allowing extra characters in attributes to accommodate future business growth, or capturing extra data that is not currently needed, such as ethnic origin; or making sure that a new process could be easily added in the future by splitting an existing process into two so that the new process could logically be fitted in between, if and when necessary.

Other potential changes may be much more difficult and costly to accommodate as it may, for example, involve large amounts of extra code. In such cases a decision needs to be made by the Flexibility Analysis team in conjunction with the systems development team as to whether it should be done or not. The probabilities and costs will clearly help in the decision making process. Something which is unlikely with high cost will probably be rejected but something with reasonable likelihood but high cost will present problems but at least a proper decision will have been made based on good information. However if a decision is made at the design stage not to take account of a potential change because it is too costly then if it does turn out to be required in the future it is likely to be considerably more costly to implement.

It has been argued that major changes of this type really demand complete re-analysis and design rather than attempting to amend the existing system. This may be right but research indicates that, in the past at least, our systems are made to last much longer than we think or envisage when we design them. In such cases Flexibility Analysis might prove even more beneficial.

A further benefit of flexibility analysis is that it involves new people in the systems development process, people such as long range planners, corporate strategists, customers, suppliers, etc. An unforeseen benefit is that this not only affects future systems and changes but it impacts the existing requirements as it often emerges that the existing analysis has been inadequate. What this really indicates is that these people need to be involved in systems development irrespective of any Flexibility Analysis. What Flexibility Analysis does is to provide a way of achieving this involvement, although it has to be admitted that it is not always an easy task.

It has been argued by some that good business related information systems/information technology planning will achieve everything that Flexibility Analysis seeks to achieve. I believe that this is not the case because Flexibility Analysis examines a particular development rather than generic plans and developments. Certainly the business analysis implicit in the IS/IT planning will help to set the context for flexibility analysis but it is not detailed enough nor does it relate to particular systems designs to be a total substitute. To achieve successful and flexible systems they both need doing!

## Summary and conclusion

This paper has analysed the problems of change and the implications for the development of information systems. The different types of maintenance have been discussed and a variety of techniques and methodologies that seek to provide solutions identified. Changing business needs and user requirements have been shown to be continuing problems and techniques relating to the prediction of possible future changes in organizations are suggested as possible improvements. Some reasons for their lack of impact in the past are given and some evidence from a retrospective study of changes to systems is presented showing that many of the reasons for those changes could have been identified at the time the systems were developed. The case for doing this is made and the required features of what is termed Flexibility Analysis are identified. These ideas are at an early stage of development and further research and experiments are required.

\*Many thanks are due to Howard Sutton who undertook much of the work of this study as part of his MBA at Warwick University under the supervision of the author.

## References

Avison, D.E. and Fitzgerald, G. (1988) Information Systems Development: Methodologies, Techniques, and Tools. Blackwell Scientific, Oxford.

Bally, M., Britton, J. and Wagner, K.H.A. (1977) A Prototype Approach to Information Systems Design and Development. Information and Management, 1, 1, 21–26.

Boehm, B.W. (1976) Software Engineering, IEEE Transactions on Computing Dec 1976, 1226–41.

Boehm, B.W., Brown, J.R., Kasper, H., Lipow, M., Macleod, G.J. and Merritt, M.T. (1978) Characteristics of Software Quality, TRW Series on Software Technology, Vol 1, Elsevier, North Holland.

Dearley, P.A. and Mayhew, P.J. (1983) In favour of System Prototypes and their Integration into the Systems Development Cycle. Computer Journal, 26, 1, 36–42.

DeMarco, T. (1980) Structured Analysis: Systems Specifications. Prentice-Hall, New York.

Fagan, M.E. (1976) Design and code inspections to reduce errors in program development. IBM Systems Journal, 15, 3.

Fagan, M. and Larson, R. (1976) Inspection Methods. IEEE Transactions on Computing.

Fitzgerald, G. (1988) Information Systems Development for Changing Environments. In Bullinger, H.J., Protonotarios, E.N., Bouwhuis, D. and Reim, F. (eds), Proceedings of the First European Conference on Information Technology for Organisational Systems: Concepts for Increased Competitiveness, Elsevier, North Holland, 587–93.

Gilb, T. (1977) Software Metrics. Winthrop, Cambridge MA.

Hekmatpour, S. and Ince, D. (1986) Rapid Software Prototyping. Open University Technical Report, 86/4.

Land, F.F. (1982) Adapting to Changing User Requirements. Information and Management, 5, 2, 59–75.

Lientz, B.P. and Swanson, E.B. (1980) Software Maintenance Management. Addison-Wesley.

Longworth, G. (1985) Designing Systems for Change.
NCC Publications, Manchester.

McKee, J.R. (1984) Maintenance as a Function of Design. AFIPS National Computing Conference.

Naumann, J.D. and Jenkins, A.M. (1982) Prototyping: The new paradigm for systems development. MIS Quarterly, 6, 3, 29–44.

Palmer, I. and Rock-Evans, R. (1981) Data Analysis. IPC Publications, Surrey.

Sibley, E.H. (1986) The Evolution of Approaches to Information Systems Design Methodology. In Olle, T.W., Sol, H.G. and Verrijn–Stuart, A.A. (eds), Information Systems Design Methodologies: Improving the Practice. Elsvier, North Holland.

Sutton, J. (1988) Analysing the Future Requirements of Computer Systems. MBA Project, Warwick University.

Ward, J.M. (1985) Evaluating IS Projects and Charges for Services. Management Accounting, 63, 1, 30–32.

Wasserman, A.I., Freeman, P. and Porcella, M. (1983) Characteristics of Software Development Methodologies. In Olle, T.W. et al., (eds), Information Systems Design Methodologies: A Feature Analysis, Elsevier, North Holland.
