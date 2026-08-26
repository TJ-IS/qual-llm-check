---
otero_id: 23862
otero_key: "2PEQDHZQ"
title: "Ternary relationships—to three or not to three, is there a question?"
authors: "S Hitchman"
year: "1999"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000333"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
http://www.stockton-press.co.uk/eji

# Ternary relationships—to three or not to three, is there a question?

S Hitchman

steveKeggconnect.net

Recent empirical research offers general data modelling guidance, claiming to show that object-oriented modelling is less effective than entity-relationship modelling. The use of ternary relationship notation in these empirical experiments is examined in detail to reveal that assumptions made by researchers result in findings that are divorced from current modelling practice, cannot be generalised, and are misleading. Research assumptions are shown to be encouraged by inappropriate research methods and this supports the argument of some writers for the adoption of different research methods that inform practice.

## Introduction

Recent empirical research claims to offer general guidance that object-oriented modelling (OOM) is inferior to some varieties of entity-relationship modelling (ERM). This empirical research seems to contradict Russo and Wynekoop (1997), who argue that there is little evidence that the evaluation and improvement of the systems analysis development process is keeping pace with technological change, and that there is a need to add to the research methods being used. This paper critically appraises the findings of the recent empirical research to reveal that those who argue for a change in research methods are justified since current methods can result in misleading findings.

Examining one aspect of research assumptions and method, the use of ternary relationship notation in diagrams, provides the evidence to establish that the approach taken by some researchers is inappropriate. The work of Shoval et al (for example Shoval & Frumermann, 1994; Shoval, 1997; Shoval & Shiran, 1997) is representative of the research undertaken over several years and makes various claims including:

Shoval and Frumermann (1994, p 1) concluded that there was a need to propose a “. . . special symbol for objects representing ternary and higher order relationships in order to overcome the weakness of OO diagrams”;

and Shoval (1997, p 81) repeated in Shoval and Shiran (1997) that “ . . . even if the objective is to implement an OO database schema, the recommended procedure is to: (1) create an EER conceptual schema, (2) map it to an OO schema . . .”.

This is clear, unequivocal advice to practitioners which has accumulated over several years, and yet it will be shown to be misleading. These claims are similar to those made in other papers that compare notations and find in favour of one of them. As part of the evidence used to support the appraisal it will be shown that:

it is fallacious to talk about ternary relationships being in the entity-relationship model or not being in the object-oriented model;

in the papers examined, the various authors have chosen to ignore contemporary practitioner modelling;

in the case of the papers by Shoval (1977) and Shoval and Shiran (1997) the practitioners were already at least six years ahead of the research being undertaken.

## Ternary relationships in the comparative research method

The empirical research examined is based on the assumption that it is valid to compare two modelling approaches in an empirical experiment. This type of experiment is common, for example Sinha and Vessey (1997) experiment on twenty-two naive modellers who are asked either to design a relational schema (which the authors call a relational data model) or to design a schema based on ORION. There are considerable problems in generalising the findings in such research including, for example, the use of naive modellers and diagramming from narrative script to represent modelling (Hitchman, 1997). This kind of comparative research generally involves alternative notations for M:N relationships. For example, in Sinha and Vessey (1997) the relational schema required a new relation to hold what can be called the ‘intersection data’. This is a key point that practitioners who use the relational model must understand in order to implement databases. In the ORION schema the relationship is captured as a ‘multivalued domain’ in one of the classes of the relationship. Some comparison of modelling effectiveness is then made against the alternative representations.

A ternary relationship is a more complex situation although there is no particular mystery about ways in which practitioners deal with these. A clear explanation slanted towards practitioners is given by Simsion (1994) and also by D’Orazio and Happel (1996) who discuss an example of a ternary relationship based on employee, skill and project (p 162, Figure 7.8) which is later extended (pp 220–223) to discuss the differing business rules in the context of 4NF analysis. This is essentially the same business domain component used by the Shoval et al experiments. A more theoretical analysis is given by Jones and Song (1996). It is clear from the literature aimed at practitioners that ternary relationships in entityrelationship modelling are interlinked with the fourth and fifth normal form issue.

There is a long history of the use of ternary relationships in comparative model research. Nijssen et al (1990) used an example ternary relationship in a discussion of the entity-relationship model compared to a NIAM approach. The entity-relationship model is referred to, although only one particular variant of the Chen standard (notice that there should be hesitation to even say the Chen ERM standard) is used. Nijssen et al (1990, p 110) provide several attempts to model a particular ternary relationship and use an implicit assumption that this standard represents ERM in general. An adapted extract from an ER model is shown in Figure 1.

As presented, this is used by Nijssen et al, as evidence that ERM does not provide adequate domain modelling, whereas NIAM does. A similar argument is essentially used in the Shoval et al experiments, but to show that a variant of ERM with this notation is more effective than OOM.

## The ternary relationship research assumption

Put simply, some empirical researchers have assumed that specific ternary relationship notation is valid and useful. To examine this assumption, and also show that the Nijssen et al findings do not generalise, it is only necessary to ask how a practitioner of entity-relationship modelling will deal with ternary relationships. Of course, there are lots of practitioners and they will all adopt their own approach. A more competent and more experienced modeller might do this better and faster. There is no way of knowing what practitioners would do exactly—there has been no research on this. This is an account of an approach that a practitioner might take, based on experience and on reading practitioner texts—which are notably missing from the reference sections of the empirical research papers discussed. This discussion uses a well known notation that is roughly contemporary with the Nijssen et al paper (Barker, 1989).

![](/api/attachments/2PEQDHZQ/fulltext/images/40f48d544a0b43f8d394dc9d843f11034e9b9182b10aa355ce32d4d8b5724a8a.jpg)  
Figure 1 The ternary solution.

Firstly, it is clear that an implementation in a relational database will have a table that contains the data about what subject is in what room at what time. This design issue is well discussed in relation to ternary relationships in Batini et al (1992, p 323), which demonstrates a one-to-one mapping between the ternary relationship and the required relational table. This is shown diagrammatically in Figure 2.

This timetabling example shows a subject occurring at the same time in different rooms, and a room that is double booked. As a relational table the primary key would be a combination of all three columns, which would not constrain the domain properly—resulting in the problems discussed by Nijssen et al (ibid) that a room may be double booked and a subject may be taught in different rooms at the same time.

It is reasonable to assume that a practitioner understands the design and implementation of relational databases and that informs modelling knowledge at any level. It is also easier to understand the problem when a working implementation is built. This gives another view to the modelling solution. Contrary to the assertions of Nijssen et al, there is no problem here for the ERM practitioner who will bring experience from other domains.

Time slot, room and subject would all be regarded as entity-types. That is because there exists a list of valid time slots, rooms and subjects, and these are certainly going to appear as tables. Notice that there is no need to worry about whether these are entity-types (or not)— to assume that a practitioner works at an entirely conceptual level, or that ERM in practice is implementation independent is unlikely to be correct. Read almost any text book on ERM for practitioners, and it will give firm advice on always decomposing M:N relationships. Why? Well, these relationships contain data that has to be stored in a table. See, for example, Watson (1996, chapter 5) for typical guidance. Academic researchers often use the ERM as though it existed independently of the practitioner environment—it doesn’t. Decomposing M:N relationships in ERM is nothing to do with ERM, it is to do with the fact that ERM is used to specify relational databases.

<table><tr><td colspan="3">slot_room_subjects</td></tr><tr><td>slot</td><td>room</td><td>subject</td></tr><tr><td>Mon 0900-0100</td><td>R1</td><td>S1</td></tr><tr><td>Mon 0900-0100</td><td>R1</td><td>S2</td></tr><tr><td>Mon 0900-0100</td><td>R2</td><td>S1</td></tr></table>

Figure 2 The intersection table.

Astute readers will be aware that it is quite easy to fully specify this domain, with all of the required constraints dealt with by the relational database management system (RDBMS) using, for example, Oracle (version 7). This knowledge is bound to inform the data modelling process. The practitioner would be thinking about the kind of diagram shown in Figure 3. Some example primary key data (representing entities) is added to help understand the diagram—a technique often used in practice but rarely referred to in research papers.

There is no ternary relationship symbol in widely used versions of ERM notation. An experienced practitioner would recognise this not as a ternary relationship, but as the classic 4NF problem. Advice here is simply to examine all of the possible intersection entity-types (see, for example, Simsion, 1994). This would produce the diagram (probably drawn on a white-board as a temporary aid to thinking) shown in Figure 4.

For the practitioner, building the ERM is not just a question of modelling ‘what is in the domain’—it is a tool for trying out and thinking through issues. The business issues here would, probably, be to investigate whether the business keeps a list of room slots (these are the bookable slots that can be occupied)—a list of available slots as well as a list of booked slots. Will a head of department also have their preferred list of which times particular subjects will run, independently of whether resources (free rooms) are available? On the other hand, is no-one interested in what rooms the subjects would run in, independent of times? (Many computing courses have specially assigned subject rooms, for example, but this is not important in this domain.)

![](/api/attachments/2PEQDHZQ/fulltext/images/3878c7f6ed413ac8a1e995f45c7bded75160a5ac149a2bc55389eb5adb0f4180.jpg)  
Figure 3 The practitioner view.

There is, therefore, not necessarily a correct solution to this problem, it depends on the particular domain. A key problem with providing narrative and looking for correct solutions is that the narrative often leaves such detail unstated or unclear, raising the question of how a ‘correct’ solution can then be assessed. Assuming there is no interest in the ‘subject-room’ entity-type, one solution is shown in Figure 5 with some data to help understand the diagram, and the modeller has forgotten to include the relationship names (many practitioners will recognise this!).

It is important to make the point here that this diagram is different to any of the alternatives considered by Nijssen et al (1990). This diagram is a ‘bit tricky’ so a database might be generated to test out thinking. The code for this is shown in Figure 6 and a test run of the database is shown in Figure 7. Those practitioners who fully understand ERM will recognise that the diagram completely captures the required constraints, but the RDBMS needs two more constraints to enforce the ‘one’ constraint specified in the diagram.

From this implementation a decision might be that the table of room-timeslots is perhaps unnecessary, and can be incorporated with the main table. The implementation could then be reverse engineered to give the model shown in Figure 8. Here, the model proposes that information about available slots is stored in slot-roomsubject, and the foreign key to slot-subject is left blank until the slot is allocated a subject, when it becomes an allocated slot-room-subject. It would then be time to test out this model again. Probably, there would be an attempt to find names for the entity-types that made more sense to the clients. The entity-types represent the working data of the department heads, concerning subject times, and the central room booking system data. The data model is not concerned with the way in which departmental heads decide on prioritising and reorganising inter-departmental room clashes, although there would certainly be checks against the functional specification through a CURD matrix. Stability analysis, probably looking back at the consequences of not accounting for specialist rooming, would also be carried out.

This solution is not pursued, neither is it suggested that it is actually correct—it is difficult to work outside a real domain. However, demonstrating the process has made the point—the skilled practitioner deals with these kind of domain semantics in a way that is not considered by academic researchers, and without any special ternary relationship symbol. There is no general solution (i.e. the ‘ternary relationship’)—the solution always depends on the business needs. It is obviously the case that ternary relationships are not essential, since practitioners have been implementing such domains for many years.

This is not to say that, with a particular teacher on a particular course of study, some novice students will not benefit from ternary notation in helping them understand modelling. It is equally arguable that by using ternary notation and not teaching students how to deal with 4NF issues in a practical way, the students are missing important modelling skills—perhaps studying the theory of 4NF without applying it in practice. The empirical research examined does not constrain findings to the experimental context but offers general advice. Whether the use of ternary notation would be more effective in practice is unresolved in the literature. The assumption made is that ternary notation is both used and effective although there is no practitioner evidence elsewhere to support this view.

![](/api/attachments/2PEQDHZQ/fulltext/images/963d4bf8271e947fb16f972e86c6d4f1fe390cbddcbb677d9a5afefdb3a13377.jpg)  
Figure 4 Examining the domain.

![](/api/attachments/2PEQDHZQ/fulltext/images/846de54fb62ed81fa4af8c3e04c26291c740248eb9f569d1b89896c60c1d95c3.jpg)  
Figure 5 The practitioners’ view of ternary relationships.

## Ternary notation in object-oriented modelling

The previous section has established that any assumptions about ternary relationship notation—for example that it is characteristic of ERM, characteristic of practitioner modelling, or effective in practice, cannot be sustained. However, when researchers build on this assumption they may generate further confusion. The experiments of Shoval et al argue that (Shoval & Frumermann, 1994, p 31) there is no ‘standard’ OO model and adopt a diagram notation of no particular standard but in which ‘notations detail all necessary information’. The authors do not include any ternary notation in the OO model, but use a special ternary notation in the comparator extended ERM (EERM).

There are several ternary relationships used in this research, one of them is the employee-skill-project relationship in Figures 3 and 4 of Shoval and Shiran (1997, pp 310–311), which appears in other research scenarios. Here, an employee is assigned to a project using a particular skill. This is similar to the assignment of subjects to room at particular times, but the business needs are different. For example, in order to assign an employee we will need to know what skills they have. Similarly we will need to know what skills are required on a project. This is the same process of examining the relationships between the three key entity-types that we conducted previously. However, in the model answers given in the research methodology, there is no information about who can do what, or about which project needs which skills. In other words, from a practitioner point of view, the supplied models would not support the business, although it is not possible to be sure since we are not given enough detail about the domains.

The suspicion is that the model answer is wrong—in the practitioner context. This may not be the same as saying the answer is wrong in the context of the paper. For example, the model has no indication of optionality in relationships, which appears to provide a mandatory recursive relationship on the employee in the practitioner domain. The suggestion is that when experts use ternary relationship notation it leads to models that will not support the business—which may be a good reason for not using such notation. Thus, an examination of research answers that have used ternary notation (Nijssen et al,

```sql
create table subjectslots
( timeslotID varchar2(2),
subjectID varchar2(2),
primary key (subjectID, timeslotID) );

create table roomslots
( timeslotID varchar2(2),
roomID varchar2(2),
primary key (roomID, timeslotID) );

create table slotroomsubject
(
timeslotID varchar2(2),
roomID varchar2(2),
subjectID varchar2(2),
constraint check_unique roomsubjecttime
primary key (subjectID, roomID, timeslotID),
constraint check_slotsubjectexists
foreign key (subjectID, timeslotID) references
subjectslots(subjectID, timeslotID),
constraint check_roomslotexists
foreign key (roomID, timeslotID) references
roomslots(roomID, timeslotID),
constraint check_uniquetimeslotsubject
unique (subjectID, timeslotID)
constraint check_uniquetimeslotroom
unique (roomID, timeslotID) );
```  
Figure 6 Implementing the model.

1990; Shoval & Frumermann, 1994; Shoval, 1997; Shoval & Shiran, 1997) is very revealing. It is left for the reader to perform the practitioner analysis on the other ternary relationships used in the research scenarios—

SQL> insert into slotsubjects values (Tr,'S1); 1 row created. SQL> insert into slotsubjects values (T1,'S2); 1 row created. SQL> insert into slotsubjects values (T2,'S1); 1 row created. SQL> insert into slot\_rooms values (Tr,Rr,'S1); 1 row created. SQL> insert into slot rooms values (Tr,R2,'S1); ERROR ORA-00001: unique constraint (STEVEH.CHECK UNIQUETIMESLOTSUBJECT) violated SQL> insert into slot\_rooms values (T1,'R1,S2'); ERROR ORA-00001: unique constraint (STEVEH.CHECK\_UNIQUETIMESLOTROOM) violated

they can all be considered to be similarly flawed in practitioner terms. In practitioner terms these experts did not manage to specify a domain using ERM with ternary notation. This strongly suggests that the notation is flawed.

However, there is a more fundamental problem with the assumptions made in this research. In 1997 the situation is assumed to be that “The OO model is still evolving and as yet no standard has been defined” (Shoval & Shiran, 1997, p 300). No standard model is used, but the authors say it is based on O2 (Deux et al, 1991) and ODE (Agrawal & Gehani, 1989). Presumably the OO model has not advanced very much since these models were defined before the original 1994 paper and six years before the publication of the 1997 papers. The diagrams in the 1977 paper seem to have an identical notation to those used in the 1974 paper and there is no notation for a ternary relationship.

Figure 7 A test run on the model.  
![](/api/attachments/2PEQDHZQ/fulltext/images/b55f4f6e7c39325025ca90e66815598b09ed3e4c13aef93952d157aee55c4eee.jpg)  
Figure 8 The model with sub-types.

![](/api/attachments/2PEQDHZQ/fulltext/images/ee12eb581d86762bd8506b4cecd0e3effff8c7917fe8991616ecbda0f366e176.jpg)  
Figure 9 UML notation equivalence.

Why is this choice of notation problematic if the findings of the paper are to be applied to the practitioner context? The reason is that a well used OOM notation has been available since 1991—OMT (Rumbaugh et al, 1991) and specifically defines a notation for ternary relationships. Researchers are choosing to ignore available OO notation and concluding that, for example, “Here too the EER model was indeed, better: 85.23% vs. 67.61% to OO! . . . In summary, we concluded that it is easier to model complex relationships with EER . . . This is opposed to OO, where the different options turned out to be misleading . . . EER was better for . . . M:N relationships, and . . . EER was better for ternary relationships” (Shoval & Shiran, 1997, pp 306–307). Notice that these findings are not referenced to a particular OO model, by implication the claim applies to all OO models. Their conclusion is that the EER model is superior in dealing with complex relationships and then explicitly advise practitioners to firstly use an EER model and then map to an OO model.

To emphasise the point about assuming the validity of assertions about the OOM notation, Figure 9 shows a UML (universal modelling language) version of the scenario in Figures 3 and 4 of Shoval and Shiran (1997, pp 310–311). This diagram was generated by Caroline Webb when a second year undergraduate student, using the SELECT case tool. Caroline found that the description of the domain, in Shoval and Shiran was not complete enough to be certain that the diagram reflects the imagined domain. Although UML is not contemporary with the research paper, an almost identical contemporary OMT model could have been generated in a previous version of this case tool. Differences from OMT notation are minor in this case, and involve the cardinality notation. The reader can easily see that this diagram is extremely similar to the Shoval and Shiran EER solution and entirely different to their ‘OO’ solution.

In short, if the experiment had used OMT as a comparator the results may have been very different and this undermines the findings. Interestingly this does not mean that we would expect the OO notation to ‘win out’. In fact, the two comparative notations would then be so similar we might expect to see no difference in the effectiveness of the notations.

What would an OMT modeller make of the Shoval et al research? Since 1991 the modellers have had available ternary relationship notation, and here is research that ignores this, and then advises them to use an EER model.

Should that OMT modeller check with ER practitioners they could find them modelling without any special ternary notation. The OMT modeller might be confused, and could well consider this research is offering advice that is at least six years out of date.

What of the ER modeller, could they be confused as well? Here is research which tells them they should be using a ternary notation, which up to now they have not seemed to need. How will they be able to assess whether this ternary notation is more effective than the approach they currently take? The ER modeller might well be impressed that 67% of naive student modellers, with only six hours training, could correctly model a domain without any ternary notation (Shoval & Shiran, 1997; Shoval, 1997). That could well suggest that special notation is not needed (with experience).

## Conclusion

The findings of the papers examined are correct within their context—naive student modellers given a particular training course, using a particular version of ERM, a particular version of OO modelling and a particular narrative to work from. However, that is as far as the findings can be taken—they are not general findings. Research methods using contrived comparative studies are shown to encourage flawed experimental design and this supports the arguments of Russo and Wynekoop (1997), that research methods need to be changed. Three problems are identified. Firstly it is fallacious to talk about ternary relationships being in the entity-relationship model or not being in the object-oriented model. There is no basis for generalising such assumptions into the practitioner domain. Secondly, in the papers examined, the various authors have chosen to ignore the contemporary modelling that practitioners do. Thirdly, in the case of the papers by Shoval (1977) and Shoval and Shiran (1997) the practitioners were already at least six years ahead of the research being undertaken.

The assumption that ERM is more effective when ternary relationship notation is used seems to be unsupported by any evidence. As to the question referred to in this paper title—the proponents of the ternary relationship notation should provide empirical evidence that answers the question of whether the ternary relationship notation is effective in the practitioner domain, before using the notation to underpin further research methods.

## References

Agrawal R and Gehani N (1989) ODE (object database and environment): The language and the data model. ACM SIGMOD International Conference on Management of Data, pp 36–45 (referenced in Shoval and Shiran, 1997).

Barker R (1989) Case \* Method: Entity Relationship Modelling. Addison Wesley.

Batini C, Ceri S and Navathe S (1992) Conceptual Database Design: An Entity-Relationship Approach. Benjamin Cummings.

Deux O et al (1991) The O2 System. Communications of the ACM 34(10), 34–48 (referenced in Shoval and Shiran, 1997).

D’Orazio R and Happel G (1996) Practical Data Modelling For Database Design. John Wiley.

Hitchman S (1997) Using DEKAF to understand modelling in the practitioner domain. European Journal of Information Systems 6(3), 181–189.

Jones TH and Song I-Y (1996) Analysis of binary/ternary cardinality combinations in entity-relationship modeling. Data & Knowledge Engineering 19, 39–64.

Nijssen GM, Duke DJ and Twine SM (1990) The entity-relationship data model considered harmful. In Proceedings of The Sixth Symposium on Empirical Foundations of Information Systems and Software Science. October 19–21, 1988, Atlanta, Georgia, pp 109– 130. Published as Zunde P and Hocking D (Eds) Empirical Foundations of Information and Software Science V. Plenum Press.

## About the author

Steve Hitchman has taught data modelling to students and practitioners for many years, as well as providing data modelling consultancy. His research interests include understanding

Rumbaugh J et al (1991) Object Oriented Modelling and Design. Prentice Hall.

Russo NC and Wynekoop SL (1997) Studying system development methodologies: an examination of research methods. Journal of Information Systems 7, 47–65.

Simsion G (1994) Data Modelling Essentials Analysis, Design & Innovation. Van Norstrand Reinhold.

Sinha AP and Vessey I (1997) Modeling relationships using the relational and object-oriented data models. In Proceedings of the Third Conference of the Association for Information Systems (AIS’97) available on http:hsb.baylor.edu/ramsower/ais.ac.97/papers/sinha.htm

Shoval P and Frumermann I (1994) OO and EER conceptual schemas: a comparison of user comprehension. Journal of Database Management 5(4), 28–39.

Shoval P (1997) Experimental comparisons of entity-relationship and object-oriented data models. Australian Journal of Information Systems 4(2), 74–81.

Shoval P and Shiran S (1997) Entity-relationship and object-oriented data modelling – an experimental comparison of design quality. Data & Knowledge Engineering 21, 297–315.

Watson RT (1996) Data Management: An Organizational Perspective. Wiley.

data modelling in the practitioner domain, and he currently works full time as a data modeller and data architect for an e-commerce financial business.
