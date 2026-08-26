---
otero_id: 17951
otero_key: "QP4C6X3V"
title: "Managing the development of database systems"
authors: "N. Revell"
year: "1981"
journal: "Information & Management"
doi: "10.1016/0378-7206(81)90060-4"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Managing the Development of Database Systems

N. Revell

The City University Business School, 23 Goswell Road, London ECIM 7BB, UK

The technical problems of database systems, if not solved, are at least now understood, whereas the problems of implementation, evaluation and operation of these systems are less well appreciated even though they are being experienced by many organizations. A survey of some 200 organizations in the UK who are (or claim to be) database users highlights some of these problems and paves the way to more successful implementation strategies. The project and some of its findings are presented here.

Keywords: Databases, database management, database implementation, database operation.

![](/api/attachments/QP4C6X3V/fulltext/images/bdee26642fc1926dece2a591353bf3ede79902f124e45d2e5d0c6310c5a1ae7b.jpg)  
also a consultant to (ROECE).

Norman Revell was educated at Oxford University where he obtained a first class honours degree in Physics; he subsequently spent 5 years working for IBM as a Systems Engineer. Since 1973, he has been a Lecturer in Systems Analysis at the City University Business School. His teaching and research effort have been mainly in the areas of online and database systems, and he is the author of several papers in these subjects. He is several UK companies and to IBM

## 1. Introduction

Much of the research work to date in the database area has been concerned with two aspects, namely, DBMS (database management systems) and the Data Model. In a way, these may be viewed as tactical issues, since both have been functionally necessary in order to produce working database systems. Much less work has centred on the wider issues of the database in the organizational environment. Whilst the tactical issues may impinge on the organization, e.g., the existence of a high level query language may be a determinant of the level of management involvement in an operational database system, it can be argued that technical issues do not have a fundamental bearing on the way in which organizations use database system.

The need to see database in a wider organizational content has been recognized by Nolan [3], Sprowls [6], Revell [4], and more recently by Wikorski [4], all of whom are concerned with the wider aspects of database systems, i.e., issues other than purely technical or conceptual. The City University project, which will be described in this paper, was started in 1976 and comprises a two stage survey of over 150 UK organization who are, or who claim to be, database users at least in a technical sense. It is dynamic, in that new organizations are being added and changes of state of organisations in the survey are monitored as they progress through the stages of database projects. It is in this respect, and also because an organizational perspective is taken, that the project differs from others. It is not intended to provide a 'Which' report (i.e., consumer guide) to database hardware, software, or data analysis techniques, but to concentrate on the management aspects of database systems.

The paper will discuss three areas, namely:

i) Practical issues involved in implementing a database system.

ii) The City University database project.

iii) Some of the results derived from the above project.

Also a new concept - the 'Organizational Schema' is discussed; this defines a database in its environment.

## 2. Practical issues involved in implementing a database system

The development of database systems can be seen as an evolutionary stage in the development of information systems in the organization. Whilst it is not necessary to go deeply into the philosophy of database systems in this paper, it is perhaps worth discussing the philosophy and some of its implications. The development of database systems represents a change of emphasis towards data processing. Whereas in the traditional approach information systems can be viewed as 'programme dominated', (that is the processing requirements determine the data that must be held to satisfy them) in the database approach data becomes the dominant factor. It is the recognition of data as a prime organizational resource that is the characteristic 'hallmark' of the database approach. Nolan [3] discusses the evolutionary aspects of database systems and Sprowls [6] discusses whether it is possible to make the 'quantum leap' straight to a database system.

There is a semantic problem here in that 'database system' is an expression used, quite logically, to describe software systems which make use of a database management system (DBMS), though use of a DBMS does not, in itself, imply that an organization has adopted a 'database approach' to its information systems development. Further there is a risk that organizations having implemented a DBMS believe that they have adopted a database approach and are deriving all the possible benefits from it. This point has been examined in our project and it will be discussed later in this paper when examining some of the results. The author uses the expression 'database approach' when discussing the database level of information systems development.

When talking about the database approach in organizations, one is talking about stages of information system development without a context. It is also necessary to consider the type of organization, since all organizations are not necessarily similar in their approach: specifically, there may be organizations that never benefit from a database approach at all. Effectively we have a matrix of industry type versus level of information systems development which should form the basis for any study of a database system in its environment. Would it be relevant, for example, to place a large government department and a small metals stockholder in the same category simply because they are at the same stage of database development? Also the 'organization' dimension would need to consider factors such as size and other classification parameters needed to differentiate between organizations in the same industry sector. Conceptually the matrix could be broken down into an 'n' dimensional array – each dimension representing an independent variable. From the point of view of a practical study, we may not consider all these dimension as independent, since the total size of the database population (in the UK) is too small at present. This project has considered a matrix of level of database development against organizational classifications.

One way of defining a database in the environment is to extend the levels of schema as defined in the ANSI/SPARC database model [1] to include a new concept, that of an ORGANIZATIONAL SCHEMA. This could be included as part of the conceptual level, though logically it would be at a higher level, as shown in fig. 1.

As far as implementation of current ANSI/SPARC proposals go, it could be argued that the considerations of organizational factors would be implicit in any practical specification of a conceptual schema.

At a more general level, Tricker [7] makes a classification of information systems as one of three levels – technical, operational or organizational. Database systems, being a special case of information systems, can be viewed in this way. Three levels of schema in the ANSI/SPARC architecture map approximately onto Tricker's technical and operational levels, whereas his organizational level represents a similar view to that provided by the 'Organizational Schema' discussed above. We shall not dwell on this concept further here; it has been introduced as an intellectual framework. Our project is, in effect, attempting to define the building blocks of an organizational schema.

![](/api/attachments/QP4C6X3V/fulltext/images/daef48123ed6a969393a2b2c83aa04fb35c639423b155be8cd85018a43666de8.jpg)  
Fig. 1. Organizational Schema.

## 3. The UK Database Project

When we started the project some three years ago, the development of database systems in the UK was mainly on the technical problems of using DBMS's. These, even if not solved, where at least understood. No answers had been provided to the very real and practical issues concerned with the implementation of a database approach. This resulted in such questions as:

'What does a database approach for our organization mean?'

'Will it benefit us?'

'How can we best implement database?'

'Do we need structural changes within the DP department?'

It was with such questions in mind that a study was initiated of organizations that were or planned to be database users. The study was made to see if there were any common principles which could be applied at a general level. In order to meet this objective, a large number of organizations would need to be studied in order to obtain representative coverage of the 'matrix' of industry-type versus level of database development. To cope with the numbers involved, the project was split into two stages: 1) a postal questionnaire survey, and 2) 'in depth' interviews with selected organizations. The postal survey was kept very simple in order to elicit a high response and to provide the basis for selecting organizations for the second stage. The survey is dynamic, i.e., as new organizations are identified as implementing database, they are sent a survey form and included in the project, even though stage two is well under way. This approach gives further validation of the results and makes it possible to identify any new trends are developing (it would be remarkable if patterns of database usage in the UK had become static within about 10 years of its introduction). A copy of the questionnaire is reproduced as Fig. 2.

As can be seen, questions cover staffing, benefits, and problems in implementation. Organizations were asked to identify themselves as being either at the feasibility stage, under implementation, or in operation. No mention of DBMS was made at this stage in order to preserve the intended balance of the whole project towards management and organizations issues. The temptation to ask more detailed questions was resisted in the interest of a high response; e.g., recipients were only asked to classify their problems as being 'political' or 'technical'.

Second stage in terviews were conducted with a senior DP executive, usually the DP manager or a person having the title 'Database Administrator'. Although a questionnaire (shown as Fig. 3) was designed for these interviews, it was mainly intended as an interviewing guide rather than a detailed checklist for every interview. The organizations for this stage of the project were selected so as to be representative of different stages of database development and also to provide a contrast of industry types.

To date, approximately 200 organizations have been surveyed at stage one and approximately 20 at stage two. These 200 organizations were selected by cross-referencing several different sources which included the following:

i) trade directories, the computing press, and journals;

ii) professional sources; e.g., conference delegate lists, personal contacts, etc.; and

iii) contacts with other researchers.

The list of organizations obtained is clearly not exhaustive for the UK, but it is sufficiently large as to be representative.

Although the results of the project are specific to

Please tick a box in each row, or make an entry where appropriate.

![](/api/attachments/QP4C6X3V/fulltext/images/b59255166c1a2608e34253cc1f832019cdc2800b34815670bf4cb1f838570404.jpg)  
Please return the completed questionnaire in the enclosed self-addressed envelope.  
Fig. 2. Preliminary Questionnaire.

the UK at present, the methodology of the project is cross-cultural and may be applicable elsewhere. Some of the more general results can at least be used as guidelines.

Finally it is worth discussing some of the more specific objectives of the project. These are:

i) to develop a classification of approaches to data-

base system implementation;

ii) to study methods of database implementation; and

iii) to examine any organizational changes brought about by the database approach, in particular the role of the database administrator.

It was felt that the classification of database

Q1 What activities have been, or will be, undertaken as part of the database feasibility study?
Q2 What factors prompted your organization to undertake a database study?
Q3 At what management level was the proposal for a database study first initiated?
Months elapsed before study work commenced?
Q4 At what management level was the proposal for a database study first authorised?
Months elapsed before study work commenced?
Q5 What were the terms of reference/objectives of the feasibility study?
Q6 What staff have been involved in the feasibility study?
Q7 What is the interviewee's impression of what a database should be and do?
Q8 Was the use of outside consultants considered? What factors influenced the decision?
Q9 What strategy was adopted to obtain user involvement?
Q10 What form did user involvement take?
Q11 What was the most senior form of management involvement?
Q12 It is important to obtain user involvement?
What problems were faced in obtaining it?
Q13 What key decisions have been taken as a result of the study?
Q14 What were the information requirements for making each of the decisions recorded in Q13?
Q15 How was the cost/benefit exercise performed?
Q16 What are the technical problems envisaged on database implementation?
Q17 What are the expected organisational problems?
Q18 How are the findings of the feasibility study communicated to senior management?
Q19 What are the criteria for selecting a DBMS?
Q20 If database administration staff have been appointed, how do they view their responsibilities?

Fig. 3. Outline of Interview Questionnaire.

approaches was vital to the whole project, since organizations which adopted database for purely technical reasons, (such as ease of programming) would have an entirely different set of goals from those that had adopted database for a better MIS. In a previous paper [3], the author defines two basic approaches:

a) the 'functional approach', and

b) the 'strategic approach'.

The ‘functional approach’ is where an organization adopts a database approach for purely technical reasons or to take advantage of some DBMS feature (such as teleprocessing capabilities). A ‘strategic approach’ is where a database is implemented in order to help achieve long term organizational benefits. It should be stressed that our classification is conceptual, and in practice one would expect a whole spectrum of approaches from purely functional to purely strategic.

## 4. Current Results

Some of the more significant findings from both stages of the project are now reviewed.

## 4.1. Level of response

Considering the nature of our first stage (i.e., an unso!cited postal survey) a surprisingly high level of response (approximately 70%) was obtained. This suggests genuine concern among users for the problems of database systems.

## 4.2. Staffing of database projects

It is surprising that 65% of the organizations used only their existing staff to implement database systems. This statistic supports the view that many users have adopted a functional approach, since the installation of a DBMS is a relatively straightforward job involving programme and file conversion that should be well within the capability of most DP departments. This is further confirmed by the second stage interviews. The question about the nature of implementation problems revealed that organizations experience more serious 'political' problems than technical ones. This point was made by Sibley [5] and seems to be related to the 'functional' approach. A typical scenario is:

An organization decides to buy a DBMS in order to achieve greater programmer productivity. As applications are converted for the DBMS, the users (who were not involved in the initial decision) are faced problems such as ownership and control of data. Thus a purely technical decision has now triggered an organizational problem outside the DP department.

It must be very tempting for a DP department to view the purchase of a DBMS in much the same way as the acquisition or adoption of other technical aids (i.e., solely internal to the DP department and 'transparent' to user departments in the organization). A thesis emerging from this project is that:

Organizations in which the decisions to adopt a DBMS has been taken by the DP department alone are likely to experience serious 'political' problems elsewhere.

4.3. Cost-savings and benefits of the database approach

This section of the questionnaire was intended to help in evaluating some of the reasons that organizations have adopted the database approach. Perhaps the most interesting result is that almost fifteen

Table 1
Approaches to Database

<table><tr><td>Stage of Database development</td><td colspan="3">Feasibility</td><td colspan="2">Under implementation</td></tr><tr><td rowspan="2">Topics</td><td colspan="5">Organisations</td></tr><tr><td>1 Toy Manufacturer</td><td>2 Investment House</td><td>3 National Research Laboratory</td><td>4 Transportation Company</td><td>5 Public Corporation</td></tr><tr><td>Database concept</td><td>‘Removes the historical constraints in the way a DP department can service users by providing greater flexibility for manipulating data’</td><td>‘Encompasses all the company’s data – should also be capable of deriving new data automatically’</td><td>‘Provides an easy means of storage, ensuring data integrity and security’</td><td>‘A file which can be accessed quickly and efficiently from all directions’</td><td>‘A collection of files which support more than one application’</td></tr><tr><td>Management level/ function at which idea first proposed</td><td>Management Services Manager</td><td>DP Management</td><td>DP Management</td><td>Senior Analyst</td><td>DP Management</td></tr><tr><td>Management level at which development authorised</td><td>Management Services Manager</td><td>Board of Directors</td><td>DP Management</td><td>DP Management</td><td>DP Steering Committee comprising senior user management</td></tr><tr><td>Strategy on DBMS</td><td>Buy Package</td><td>Buy Package</td><td>Buy Package</td><td>Buy Package</td><td>Build Own</td></tr><tr><td>Key criteria for selecting DBMS package/reason for building own DBMS</td><td>Undecided which DBMS</td><td>1. Ability to model data relation-chips2. Portability</td><td>1. Portability2. Ability to model data relation ships3. Costs4. User experiences</td><td>1. TP facilities2. Ability to model data relation ships3. Operating systems compatibili-ity</td><td>To minimise coverage problems</td></tr></table>

percent of the organizations said that there was a definite cost saving, and all but one has operational systems. Cost-savings therefore are not a prime motivating factor for the database approach. On a first consideration, this would seem to contradict previous results (the hypothesis that many organizations have adopted a 'functional' approach), but on further examination, the type of technical benefits derived from a DBMS would not be expected to show up directly. There was much more positive response to the question on the provision of better information as a reason for the adoption of database. One half of the organizations had identified a definite improvement in the provision of information as a reason for a database approach, with over half of these respondents coming from organizations that had operational systems. Analysis of this stage of the survey indicates this factor to be the principal one of interest in the UK. This in itself does not imply that all of these organizations have adopted a strategic approach, since the provision of better information for users could be seen as a technical response by the DP department in answering existing technical limitations; e.g., the difficulty of providing 'ad hoc' management reports might be resolved by the installation of a DBMS with a good query language – a purely technical response which fits into the 'functional' approach.

<table><tr><td>Under implementation</td><td colspan="4">In operation</td></tr><tr><td>6Local Authority</td><td>7Chemicals Company</td><td>8Office Products Manufacturer</td><td>9Teaching Hospital</td><td>10Computer Manufacturer</td></tr><tr><td>‘Provides data independence’</td><td>‘A collection of subject orientated databases which support a number of projects’</td><td>‘Links all the company data and provides controlled redundancy’</td><td>‘Centralised store, holding each data item uniquely and providing easy access’</td><td>‘A collection of data, centrally co-ordinated though not necessarily held at one physical location’</td></tr><tr><td>Chief Executive</td><td>Planning Group</td><td>DP Management</td><td>DP Management</td><td>Management Services Manager</td></tr><tr><td>Chief Executive</td><td>Director of Administra-tion</td><td>DP Management</td><td>DP Management</td><td>Finance Director</td></tr><tr><td>Buy Package</td><td>Buy Package</td><td>Buy Package</td><td>Build Own</td><td>Build Own</td></tr><tr><td>1. Expand- ability</td><td>1. Vendor support</td><td>1. Processing efficiency</td><td rowspan="3">Packages found to lack flexibility</td><td rowspan="3">No package available on H/W when system designed</td></tr><tr><td>2. Report writer</td><td>2. Ability to model data relation-ships</td><td>2. Ease of maintenance</td></tr><tr><td>3. Ability to model data relation-ships</td><td>3. Processing efficiency</td><td></td></tr><tr><td>4. Vendor Support</td><td></td><td></td><td></td><td></td></tr></table>

The results presented from this stage of the project covered the main problem areas; detailed statistical tabulations have been published elsewhere [4]. They provided valuable feedback in determining the issues for further study in stage two.

## 4.4. Some results of stage two interviews

Table 1 illustrates the answers provided by 10 organizations at different stages of database development to five key question areas.

The concept of database can be seen to range across the whole spectrum from a purely technical view, such as 'A file which can be accessed quickly and efficiently from all directions', to a 'strategic' view which 'Removes the historical constraints in the way a DP department can service users, by providing greater flexibility for manipulating data'. It would be very difficult, if not impossible, to classify this sample, since there are elements of several approaches in most.

The next two questions dealt with the initiation and authorization of database projects; they provide an interesting perspective on the management level at which the database decision was approved – nearly always at a technical level. Some organizations (e.g., 2 and 10) provided good examples of higher management involvement in the decision, and it is not surprising that both these organizations have taken a more 'strategic' approach. In organizations 6 and 7, the decision was to be functional. This may be because their senior management plays a 'rubber stamp' role, and thus they merely endorse the DP department decision, or maybe the problems encountered in the non-database environment have been of sufficient gravity to sensitize senior management.

The questions concerned with DBMS strategy show some of the reasons why some organisations have built their own package. Organisations 1 and 5 gave purely technical reasons, whereas organization 9 made this approach part of its overall strategy. Given the necessary size of the commitment in terms of initial development and maintenance, it is surprising that any organization has taken this step. Clearly, there is little statistical significance in a sample of one organization, but this one organization felt sufficiently strongly about the rigidity of the available packages that it chose to 'go it alone'.

## 5. Summary and Conclusions

Our project arose out of a desire to study the wider implications of the database approach as part of the technical infrastructure of the organization. To date, the impetus to develop database systems in the U.K. has tended to come from within the data processing function of the organization (with the attendant risk that a more limited or 'functional' approach will be taken rather than a long-term or 'stategic' approach). The awareness of senior management of the benefits of the database approach seems to be a key factor here. Further stages of the project will be looking at specific management issues of the database approach (implementation methodologies, database administration, etc.) with the long term goal of developing an 'organization schema' or definition of a database in its environment.

## Acknowledgements

The author would like to thank his colleagues in this project - O.J. Hanson and J. Sherif for their support, and also Professor E.H. Sibley for his helpful comments on the first draft of the paper.

## References

[1] J. Jardine, Ed., ANSI/SPARC, The ANSI/SPARC DBMS Model, (North Holland, 1977).

[2] O.J. Hanson, N. Revell and M.A. Sherif, Perspectives on databases and Computing, V6N36.

[3] R.L. Nolan, Restructuring the Data Processing Organization for data resource management, in proc. IFIP 77, North Holland.

[4] N. Revell, Some practical aspects of database systems, in proc. I.C.C.A., Bangkok 1977.

[5] E.H. Sibley, The impact of database technology on business systems, in proc. IFIP77, (North Holland).

[6] R.C. Sprowls, Can developing nations make the quantum jump in utilizing computers? in proc. ICCA Bangkok 1977.

[7] R.I. Tricker, Impact of Information systems on organizational thinking, in proc., IFIP 77 (North Holland).

[8] G. Wikorski and J.J. Wikorski, Does a DBMS pay off?, Datamation, April 1978.
