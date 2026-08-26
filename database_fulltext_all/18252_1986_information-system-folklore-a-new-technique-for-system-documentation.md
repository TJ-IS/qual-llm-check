---
otero_id: 18252
otero_key: "FGSEC75Z"
title: "Information system FOLKLORE: A new technique for system documentation"
authors: "Kenneth E. Kendall; Robert D. Losee"
year: "1986"
journal: "Information & Management"
doi: "10.1016/0378-7206(86)90052-2"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information System FOLKLORE: A New Technique for System Documentation

Kenneth E. Kendall

Department of Management, The University of Nebraska-Lincoln, Lincoln, Nebraska 68588, USA

and

Robert D. Losee

Computer Services Network, The University of Nebraska-Lincoln, Lincoln, Nebraska 68588, USA

Effective system documentation is an essential part of a management information system. Yet it is common to witness users struggling with a system that has incomplete or missing documentation. This is a consequence of systems analysts feeling that there is no time to even start documenting; preferring to do more desirable or rewarding tasks; or simply being concerned that their documentation of an inherited system might be wrong. To overcome these barriers to good documentation, FOLKLORE was created and is now implemented at the University of Nebraska-Lincoln. The framework for FOLKLORE, its costs and benefits, and examples from FOLKLORE documents are presented.

Keywords: Systems analyst, system documentation, program documentation, lack of documentation, systems analysis techniques, folklore, documentation techniques.

## 1. Introduction

Documentation of programs and systems is typically a low priority for Systems Analysts (SAs) and programmers. It often comes as a relief to get a program or system put together and documenting it occurs as an afterthought.

The abundance of poor documentation is evidence that its worth, (as a memory aid, evaluation device, productivity tool, and as a means of reducing dependencies on key staff members), is undervalued. Rather, documenting is considered more of an aside to getting the “real” work done, revealing the attitude that real SAs don’t document.

Realizing these problems, Brooks [3] in 1975 stated, “The time has come to devise radically new approaches and methods for program documentation.” Yet the problems that surfaced in the last decade are still with us because innovative approaches for documenting systems and their programs are not in use.

This paper offers a new technique called FOLKLORE. This new approach was designed to take into consideration many of the shortcomings

![](/api/attachments/FGSEC75Z/fulltext/images/ceabaaa34d2f75a37a81de5cb03ec984839bb199dd83fe016dc8932ba8d82536.jpg)

Kenneth E. Kendall is an Associate Professor of Management Information Systems at the University of Nebraska-Lincoln. He received his Ph.D. degree in Management Systems from the State University of New York at Buffalo. Dr. Kendall's publications have appeared in Information and Management, Management Information Systems Quarterly, Decision Sciences, Management Science, Operations Research, and numerous other journals. He is currently developing innovative

techniques for use in systems analysis and design, and has been involved with the development and evaluation of numerous

![](/api/attachments/FGSEC75Z/fulltext/images/e7f51e45be631be1066a412fd402c232a91679c9edc0bbaf8670df588dcadec9.jpg)

Robert D. Losee is an MBA candidate at the University of Nebraska-Lincoln. Since 1980 he has been a programmer/analyst with the University of Nebraska's administrative computing department. In this capacity he developed his current interest in the methods and requirements of systems documentation. Other interests include strategies to reduce errors in the use of informations systems.

of more traditional documentation techniques and to augment them.

The FOLKLORE concept was implemented and is in use that the University of Nebraska-Lincoln. This paper describes the need for FOLKLORE, its development, and application.

## 2. Value of Documentation

Documentation of systems and programs serves several useful functions. The first is that documentation reduces uncertainties for its readers about decisions, rules, and methodologies which the SA employed in the past.

It is critical for systems analysts to document their past practices for their own future use. Psychological research has shown that memory is very short-lived. Recall, as opposed to recognition, drops about 10% in a week and falls to an alarming 0% in three weeks. Recognition goes from 70% to 50% in the same amount of time [20]. Since many of a SA's functions, responsibilities, and tasks are on an annual (or less frequent) basis, it is clear that they will need memory aids, even if they were once familiar with a system.

Documentation also provides a means to review and judge systems. This affects three phases of a project: evaluating or creating a system; system maintenance, and converting to a new system. During each phase a basis is needed to evaluate what is desirable and what is possible. Documentation provides a source and standard baseline for evaluation.

Documentation facilitates installation, operation, use, evaluation, and maintenance of a system [2]. It can be used as a training tool to move people up on the learning curve faster than is possible by trial and error. It can also serve as a cookbook filled with recipes detailing how to successfully accomplish tasks in a proven step-by-step manner.

Documentation reduces the dependencies of an organization on “gurus”, the systems experts who might leave, become ill, or ask for more money in exchange for not doing the first two. Such experts are relied upon heavily precisely because they are the repositories of a system’s documentation. As such their value to the organization is both immeasurable and disproportionate.

Most sources state that documentation should be written concurrently with the design effort (Atwood [1], Brooks [3], Lucas [15], and Senn [18]). Some even state that documentation should be done prior to programming, that is, during the analysis phase (Davis [5], Gore and Stubbe [8], and Katzan [10]). Used in this way, documentation functions as an SA tool for organizing and defining the system. The rationale is that if a system can be documented before programming, then system goals are probably clear in the SA's mind. In short, documentation accomplished before programming serves as a useful system definition.

Unfortunately, what is considered desirable is not always done. A whole class of undocumented and underdocumented systems exists. Several forces contributed to this problem.

## 3. A Lack of Documentation

Some systems, written long before documentation standards and procedures came into common practice, still exist. They have simply never had any documentation. Perhaps they are still running because they work with little intervention. It is a distinct possibility that no one is knowledgeable about pre-documentation systems and how they work, so there is a reluctance to record anything about them.

Other systems at one time were adequately documented but over time their documentation has grown unreliable and thus untrustworthy. This is because systems are modified without concurrent documentation change. Inadequate administrative guidelines that would coordinate and enforce maintenance and documentation of systems are frequently to blame when documentation does not keep pace.

Sometimes documentation is inadequate because the programs are acquired from an outside source. Fortunately, in response to marketplace demands, standards are improving in this area. However, many systems, particularly low-volume ones, still fail to supply complete documentation.

Some systems are poorly documented because they were cheaply obtained or were the best systems available at the time, despite the lack of documentation. Those who obtained them may have traded-off decent documentation for the system itself.

Documentation frequently falls short in reflecting system attributes which are realized only after using it. These might include hints about how to deal with a difficult phone line, who to call about problems with input documents, etc. These items do not fit well into a standard documentation scheme.

## 4. Why Systems are not Adequately Documented

There are a number of reasons systems analysts fail to adequately document the system. The first reason is not having sufficient time to do so. Other projects loom over the systems analyst, and SAs may feel an urgency to get on with the next project. Contributing to this is the concern that documentation must be complete. Ironically, systems documentation may never be undertaken because of this concern.

Another reason for under documentation is that SAs frequently do not want to document. Systems Analysts prefer to solve analysis and design problems while programmers want to do the “real” work of writing code. They sometimes feel their skills are better suited to more quantifiable pursuits, and less suited to verbal ones such as writing. Or they may simply feel that analysis and design are fun while documentation is a chore.

A third reason for under documentation is that SAs may feel uncomfortable writing up systems they know little about. This situation occurs when SAs are assigned to do maintenance on a project that was not originally their own. Committing to paper what may be in error is inviting the possibility of future corrections, reprimand, or even ridicule.

SAs frequently possess only a fragmentary understanding of systems and how the operating environment interacts with them. They do not have enough control to change environments, nor do they have the time for investigation and reflection on how an unknown system works.

In summary, there is a wealth of reasons that justify the poverty of documentation. Old systems, written before standardized documentation, are still running. Other systems have been modified, but their documentation has not kept pace. Low-volume systems may contain the only specialized programs available, and are purchased even without documentation. Realizations occurring only after a system is in use are not usually documented.

Systems Analysts fail to document systems properly because they lack sufficient time and reward; they feel that documenting is not their real work or is even a chore; and they are concerned about reprisal if erroneous material about someone else's system is included in documentation.

One way to address the imperative of documenting, while acknowledging the above concerns, is through use of a supplementary new technique of folklore. FOLKLORE will help the SA collect and disseminate information about the working of systems without the encumbrances carried by traditional documentation.

## 5. Developing the FOLKLORE Documentation Technique

Recently it has been demonstrated that techniques borrowed from other fields may be of great help to the systems analyst [11-13]. One approach to applying a framework adapted from another discipline, (in this case, film theory), was proposed by Kendall and Kendall [11]. They suggest building a one-to-one correspondence between the elements of the root discipline and elements of systems analysis. Table 1 draws this kind of relationship between traditional folklore and system documentation.

Folklore Elements and their Systems Analysis Equivalents

<table><tr><td></td><td>Folklore</td><td>Systems Analysis</td></tr><tr><td>Who</td><td>Folklorist</td><td>Systems analyst alias FOLKLORE documenter</td></tr><tr><td rowspan="4">What</td><td>Customs</td><td>How users currently get the jobs to run</td></tr><tr><td>Tales</td><td>How we think somebody got the jobs to run</td></tr><tr><td>Sayings</td><td>Do this and it works</td></tr><tr><td>Art forms</td><td>Flowcharts, input/output screens, and tables of explanation</td></tr><tr><td rowspan="3">Where</td><td>Town meetings</td><td>Board room meetings</td></tr><tr><td>On the street</td><td>In the hall</td></tr><tr><td>In public records</td><td>In files and desks</td></tr><tr><td>When</td><td>Anytime, but there must be interest</td><td>When the need or opportunity arises</td></tr><tr><td rowspan="2">Why</td><td>Helps us understand who we are, Continuity</td><td>Helps us to understand the system Continuity</td></tr><tr><td>Person we would like to talk to is often deceased</td><td>Authors often leave</td></tr><tr><td rowspan="3">How</td><td>Interviews</td><td>Interviews</td></tr><tr><td>Observations</td><td>Observation</td></tr><tr><td>Investigation of other files and documents</td><td>Investigation of files, and existing output and code</td></tr></table>

Although a proliferation of definitions of folklore exists (see [7] and [16] for example) we need not take part in that controversy here. A straightforward and useful definition of folklore is “traditional customs, tales, sayings or art forms preserved orally among a people,” [19].

The term folklore was first coined in 1846 to replace the term “popular antiquities.” At the time the term meant oral traditions only but it has gradually come to include all “communication events structured and transmitted according to traditional practices,” [4].

Customs are repeated or habitual practices common to a place or group [9]. As any person involved with MIS and DP is aware, many things are done out of habit. This is in part self-protection. Customs develop as SAs attempt to run a system. Successful techniques are remembered and attempted again. These techniques are developed and saved in the SAs files, notes, etc., and much of it re-surfaces as shop talk, as we shall see in tales and sayings. Typically there are so many things to do, and there are so many complex tasks to complete that habits (or customs) are the main strategy for coping.

Tales, a traditional form of narrative with a beginning, middle and end, can explain the genesis of something, the consequences of some act, or can contain cautionary warnings. They may be true only in part [21]. Often there will be a hero and villain and some sort of dramatic pattern resolving problems (conflict). Tales are common in the SA environment. Ask how to do something and responses come back such as, “I think you do …” or “When I tried that it didn’t work, but the system was up and down a lot that day.”

Sayings can be thought of as distillations of many tales which are shorter generalizations about the way the world works [17]. Sayings lack a complete dramatic structure, but rather supply a blanket statement to guide the hearer in understanding relationships such as “April showers bring May flowers,” or “Step on a crack, break your mother’s back.” In data processing this becomes, “Omit this seemingly useless line of code, and the program will bomb.”

Finally, art forms are the traditional, graphic expressions of people [9]. They differ from tales and sayings in that they appeal to the eye as well as the ear, but they too are handed down by the community. Art forms are flow charts, Warnier/Orr diagrams, notes, and drawings that might be posted, put in drawers, manuals, or other places.

Folklore exists because of its usefulness in helping people cope with complex, incompletely understood, and largely uncontrollable environments. Success forms habits or customs, sayings, tales, and art forms that eventually crystallize. Thus encoded, the ability to recount successful coping methods is secured.

## 6. Implementation of the FOLKLORE Approach

FOLKLORE, a method for documenting systems, is implemented at the University of Nebraska-Lincoln (UNL). Currently, it is being used by the UNL Administrative Systems Group, part of the Computer System Network for the UNL system. The FOLKLORE concept is accepted and used by 6 systems analysts in over 20 separate FOLKLORE projects.

Below are guidelines typically provided for would-be contributors of FOLKLORE:

1. Assume the material in the FOLKLORE of documentation may be totally accurate, partially accurate, or even incorrect.

2. Assume that the material contained herein has been passed down from user to user, not from the program author.

3. Feel free to add, change or even delete items from the folklore section if you feel that it makes the documentation more understandable or accurate.

4. Try to think of information you add as one of the following:

a. customs

b. tales

c. sayings, or

d. art forms,

and use the pertinent style while relaying your information to the chief documenter.

The following are examples from various FOLKLORE documents, still in the evolutionary phase, where contributors followed the guidelines above. Fig. 1 is part of the preface from the FOLKLORE Document [6]. Essentially it explains what folklore is and invites users to “add, change, or delete from this body of knowledge,” so that all those who come in contact with the system will be able to better understand it.

![](/api/attachments/FGSEC75Z/fulltext/images/dcd94ab7c380437bcb9a83b43baf5a69bb5b3f101f836f41a0c06182740ff0a1.jpg)

Under the heading, “standards,” contributors and users are told how to distinguish among revisions, questionable statements (after all, some parts of the legend way not be true), and archaic information (material that is no longer salient, but which helps the user understand how and why the system developed).

An example of custom from the Financial Aids FOLKLORE Document [6] is found in Fig. 2. Words and phrases such as “normally,” “since this same job will run again in the month of July,” and “re-run,” demonstrate that the user is detailing a habitual or customary way of doing the job, which establishes continuity with past performances and will presumably bring about desired results if followed.

A FOLKLORE tale from the Library Acquisitions FOLKLORE Document [14] is provided in Fig. 3. It opens with a brief history, providing a link with the past and establishing a once-upon-a-time fairy tale quality, “These library programs were written in the late 1960’s.” The author is the hero who has triumphed over several perils, “This

Fig. 2. A Custom from the Financial Aids FOLKLORE Document.

PROGRAM NOTES
These library programs were written in the late 1960's. Although the users feel that they have admirably meet their needs the programming techniques are primitive, at least in regard to account number and fund changes. These were hard coded into the program so that each year, as these accounts change, it is necessary to update programs.
Another problem was encountered in 1981. As I remember it, if some record types were not present (financial records I believe) then merging of some data in certain programs would not occur. Several steps later in the job this would cause a GDG tape to be cataloged but it would never be opened so the next runs data would actually be several generations old. To correct this potentially serious problem I put fixes in some programs to ABEND if these critical cards were not present. At the time we got around the problem by running phony financial(?) cards through the program. This problem occurred again in 1984. In this case the LIB003M job (monthly serials) ran with only type "6" financial records in it. The effects of this cascaded through out the job until the last step when data merging was to occur. In this step there were no financial records in the input file so opens were done, a read of this file was done and, since it was empty, immediate closing of the files occurred. Thus the GDG tape was cataloged so that on the next weekly run there was no input an balances came out as zero. The problem was corrected by rerunning the job with a "7" type record.

Fig. 3. A Tale from the Library Acquisitions FOLKLORE Document.  
![](/api/attachments/FGSEC75Z/fulltext/images/98587586997508935f4eea6e2984792035b8af9b44d6ca951a3d795f0e5b5427.jpg)  
Fig. 4. A Saying from the Financial Aids FOLKLORE Document.

would cause the GDC tape to be catalogued but it would never be opened so the next runs would actually be several generations old." The hero has devised a way for others who read the tale and heed it to avoid earlier problems: "To correct this potentially serious problem I put fixes in some programs," and finally, "The problem was corrected by ..." This amounts to a modern-day cautionary tale.

A FOLKLORE saying from the Financial Aids FOLKLORE Document [6] is given in Fig. 4. It is concise in providing a formula to prevent future problems. “Save the future FA Master File … for one year, in case re-run is needed.” It is analogous to a saying such as, “Save it for a rainy day.” The saying lacks the dramatic structure and cast of the previous tale, but retains the essential truth of experience. Such sayings are useful to readers in covering many situations briefly, without need of further explanation.

![](/api/attachments/FGSEC75Z/fulltext/images/1b2a00b35be6c5d6d13ea293800fe2714af960269018db69e6fa5dadfe0593e3.jpg)  
Fig. 5. An Art from the Financial Aids FOLKLORE Document.

Finally, an example of a FOLKLORE art form, again from the Financial Aids FOLKLORE Document [6], is shown in Fig. 5. In this instance, the art form is put into a simple matrix that allows the reader to quickly grasp the relationship between criteria for awarding financial aid and the type of financial aid given. This is an interesting example since the matrix is a commonly used form and actually belongs to the folklore of the larger mathematical community. Here it has been adapted and shaped for the specific purpose of the reader. The matrix as art form is bound to be repeated because of its inherent flexibility.

The above examples and other pieces of folklore were collected in a number of different ways. Some were submitted directly by the users, others came from interviews, still others arose in group meetings. Other information such as input/output diagrams and flowcharts came from user's files, blackboards and bulletin boards. Customs were observed and tales were recalled.

## 7. FOLKLORE Costs and Benefits

FOLKLORE documentation is an additional step in providing services to users. As such it incurs additional costs. Table 2 is a list of these costs, as well as a list of the primary benefits of FOLKLORE.

Costs and Benefits of FOLKLORE Documentation

<table><tr><td>Costs</td><td>Benefits</td></tr><tr><td>1. Taking time to gather FOLKLORE information</td><td>1. Filling the void that exists when an author leaves</td></tr><tr><td>2. Taking time to organize FOLKLORE information</td><td>2. Providing more effective documentation because of the team effort</td></tr><tr><td>3. Typing FOLKLORE documentation and printing FOLKLORE manuals</td><td>3. Making more information available</td></tr><tr><td>4. Storing FOLKLORE information</td><td>4. Shortening time it takes users to find answers5. Creating a place to find answers6. Documenting is easier for the analyst7. Documenting is less intimidating</td></tr></table>

The first cost is incurred when analysts telephone users and search through files turned over by program authors who have long since left. Next there is the time required to gather all of the information into one place and organize it. Thirdly, costs accrue from typing material into computer files and then printing new FOLKLORE manuals. Finally, storing FOLKLORE information requires space on computer disks and user's shelves.

FOLKLORE affords benefits by improving the effectiveness of documentation, increasing its efficiency, and increasing the efficiency of systems analysts. The first benefit comes in more effective documentation. Keeping in mind that FOLKLORE is often undertaken because the author is not present to do more structured documentation, the result of the FOLKLORE effort is better than no documentation at all. FOLKLORE fills the void that exists because the program author has left.

Documentation is improved because users become more involved with the project through the FOLKLORE process. Users are part of the team, and they feel they can talk with systems analysts. In turn, SAs will listen to their concerns. More information is available using FOLKLORE. Since the FOLKLORE process encourages the documentation of gray or ambiguous areas of the program, as well as what is black and white, users tell systems analysts more.

User efficiency is also improved using FOLK-LORE. Anecdotal evidence supplied by users leads us to believe they are spending much less time hunting for answers to their questions. Users now have a common place (the FOLKLORE document) to go to learn more about the programs.

FOLKLORE also provides benefits for the systems analyst responsible for documentation, when there is no program author around to complete the it. Documentation is easier because the users feel they are part of a team. Furthermore, the FOLKLORE approach is less intimidating, thus overcoming the inertia of documenting something the systems analyst did not write originally.

In summary, there are both costs and benefits that come with the use of FOLKLORE and they are indeed difficult to measure. The alternative, that is, not using FOLKLORE, means higher costs without the benefits. Remember that FOLKLORE is intended to replace an informal, often haphazard way of finding out how a program or system runs.

## 8. Findings

Experience with FOLKLORE thus far has led to the following observations.

1. Users felt that something was being done to help them understand the programs and the running of programs.

2. Programmer analysts felt less pressure since the FOLKLORE concept provided for sharing responsibility with users. Furthermore, documentation was allowed to evolve under the FOLKLORE concept. There was no insistence that documentation be complete at the outset.

3. Both users and analysts felt that the burden of documentation was lightened. Users actually seemed to have fun telling tales. They also assigned status to being around “back then,” or being one of the “early users.” Users also liked describing customs and rituals they or others enacted to induce a job to run successfully.

4. Users were not as worried about making a mistake. The FOLKLORE philosophy encouraged the user to contribute his/her insights without worrying about their accuracy. From our experience very little has been proven wrong, yet users are given the caveat that the FOLKLORE section consists of information believed to be true, not proven to be true.

5. Customs and tales were the easiest forms of FOLKLORE to obtain. Users freely described procedures in sufficient detail (customs) and enjoyed relaying stories about actions they took that did or did not work (tales).

6. Sayings and art forms were more difficult to obtain directly from users. In order to elicit worthwhile sayings, the FOLKLORE documenter needs to talk with many users, extract rules from these interviews, and re-phrase them as sayings. The best art forms came from observations, made by the FOLKLORE documenter, of blackboards used during meetings and bulletin boards used for posting existing art forms.

Preliminary findings point to the ease of implementation of FOLKLORE; and its acceptance, enjoyment and use by SAs and users.

## 9. Conclusion

Documentation is vital. FOLKLORE is a new supplementary technique now being used at the University of Nebraska-Lincoln to make documentation more efficient and more effective.

FOLKLORE was developed from methods used in gathering traditional folklore. The use of existing techniques allows the systems analyst a structured, rather than haphazard, approach to supplementing documentation. The method includes obtaining detail from users on customs, tales, sayings, and art forms. Information was gathered through interviews, group meetings, observation of users running their jobs; and investigation of their existing flowcharts and diagrams.

We found that FOLKLORE has three advantages over older documentation techniques. First of all, the adoption of FOLKLORE as a supplementary method allows documentation to evolve. Secondly, users and analysts feel that documentation is less of a chore than before. Finally, those concerned about documentation can contribute without fear of being found wrong.

FOLKLORE is successful in that it was accepted and adopted by users and other systems analysts in a relatively short time. Currently over 20 projects at the University of Nebraska-Lincoln are being documented using the FOLKLORE approach. While future effort in this area might include setting up an experiment to more appropriately measure the effectiveness of this method, experience so far indicates that FOLKLORE is a valuable new technique for systems analysts.

## References

[1] J.W. Atwood, The Systems Analyst, Hayden Book Company, Inc., Rochelle Park, New Jersey, 1977.

[2] P.F. Barbuto, Jr. "A Structured Approach to Maintenance," in Auerbach Information Management Series; Computer Programming Management, Auerbach Publishers Inc., Pennsauken, New Jersey, 1983, pp. 14-05-04.

[3] F.P. Brooks, Jr. The Mythical Man-Month, Addison-Wesley, Reading Massachusetts, 1975.

[4] J.H. Brunvand, \*Folklore--a Study and Research Guide\*, St. Martin's Press, New York, 1976, p. 138.

[5] W.S. Davis, Systems Analysis and Design, Addison-Wesley Publishing Company, Reading, Massachusetts, 1983.

[6] Financial Aids FOLKLORE Document, Computing Services Network, University of Nebraska, Lincoln, May 1, 1985.

[7] K.S. Goldstein, A Guide for Field Workers in Folklore, Folklore Associates, Inc., Hatboro, Pennsylvania, 1964.

[8] M. Gore, and J. Stubbe, Elements of Systems Analysis, (3rd edition), Wm. C. Brown Company, Dubuque, Iowa, 1983.

[9] E.S. Katz, \*Folklore for the Time of Your Life\*, Oxmoor House, Inc., Birmingham, Alabama, 1978.

[10] H. Katzan, Jr., Systems Design and Documentation, Van Nostrand Reinhold Company, New York, 1976.

[11] K.E. Kendall, & J.E. Kendall, "Observing Organizational Environments: A Systematic Approach for Information Analysts," Management Information Systems Quarterly, 5, 1981, pp. 43–55.

[12] K.E. Kendall, & J.E. Kendall, “Structured Observation of the Decision-making Environment: A Reliability and Validity Assessment,” Decision Sciences, 15, 1984, pp. 107–118.

[13] K.E. Kendall, & J.E. Kendall, "STROBE: A Structured Approach to Observation of the Decision-making Environment," Information & Management, 7, 1984, pp. 1–11.

[14] Library Acquisitions FOLKLORE Document, Computing Services Network, University of Nebraska-Lincoln, May 1, 1985.

[15] H.C. Lucas, Jr., The Analysis, Design, and Implementation of Information Systems, (3rd edition), McGraw-Hill Book Company, New York, 1985.

[16] V.J. Newall, “Introduction” in \*Folklore Studies in the 20th Century\*, (V.J. Newall, ed.), D.S. Brewer, Suffolk, England, and Rowman & Littlefield, Totowa, New Jersey, 1980, p.xv.

[17] L. Rohrich, “Folklore and Advertising,” in \*Folklore Studies\* in the 20th Century, (V.J. Newall, ed.), D.S. Brewer, Suffolk, England, and Rowman & Littlefield. Totowa, New Jersey, 1980, pp. 114–116.

[18] J.A. Senn, Analysis and Design of Information Systems, McGraw-Hill Book Company, New York, 1984.

[19] Webster's New Collegiate Dictionary, G. & C. Merriam Company, Springfield, massachusetts, U.S.A., 1979, p. 442.

[20] B. Wilkinson, “Documentation Conventions for the Programmer,” in Auerbach Information Management Series; Computer Programming Management, Auerbach Publishers Inc., Pennsauken, New Jersey, 1982, p. 12–03–01.

[21] J. Van Maanen, J.M. Dabbs, Jr., and R.R. Faulkner, Varieties of Qualitative Research, Sage Publications, Beverly Hills, California, 1982, pp. 103–151.
