---
otero_id: 23764
otero_key: "8G22XKNW"
title: "Using DEKAF to understand data modelling in the practitioner domain"
authors: "S Hitchman"
year: "1997"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000265"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Using DEKAF to understand data modelling in the practitioner domain

S Hitchman

Faculty of Business and Social Studies, Cheltenham & Gloucester College of Higher Education, PO Box 220, The Park Campus, Cheltenham, GL50 2QF, UK

Despite the ubiquitous use of entity-relationship modelling for more than twenty years, there is surprisingly little evidence of how effective data modelling is in the commercial domain, and this evidence suggests that modelling is problematic. This paper evaluates the literature on the effectiveness of data modelling in the practitioner domain, showing that implicit objectivist assumptions about narrative are questionable. A domain expert knowledge approach framework (DEKAF) is described in the context of overcoming problems of research generalisability. DEKAF provides both a useful way of understanding and thinking about the data modelling process and a way of making assumptions explicit in a particular practitioner domain. A summary of the findings of action research shows that DEKAF can be successfully used and can give insight into effective practitioner domain modelling.

## Introduction

In a discussion of a ‘mythical’ case study by Turner and Jenkins (1995, p 7), a project involving three European Union countries is described in which there are three different analysis methodologies and technical platforms “... one of the few areas of commonality between organizations is over the importance of data models in development.” Data modelling is ubiquitous in analysis methods, particularly entity-relationship modelling (ERM), although challenged by the so-called object-oriented models (OOM) and by object-role modelling (ORM, also known as FACT modelling and within the NIAM method). However, what little evidence there is about effective data modelling in the commercial domain (for example, Batra & Marakas, 1995; Hitchman, 1995a) points to data modelling being problematic. This paper argues that current research is limited in informing the debate about modelling and that, given the widespread use of data modelling, a better research framework needs to be established.

Data modelling is studied from a theoretical viewpoint while also being carried out by practitioners and the literature can be characterised by distinguishing between texts aimed primarily at ‘theory’ (for example Batini et al, 1992) or at a ‘practitioner’ (for example Barker, 1989) audience; although particular texts are not necessarily exclusive. Veryard (1992), a text in a ‘practitioner series’, makes use of the work of ‘theorists’, but the reverse is not generally true. The practitioner literature tends to echo the literature concerning IT management consultancy, where “... much of the literature ... has tended to be of a descriptive and/or prescriptive nature ... fails to go beyond descriptions of what consultants themselves claim to do, and their prescriptions for best practice ...” (Bloomfield & Daieli, 1995, p 25).

Lewis (1994) shows that there is a tendency for texts on data modelling to adapt what he characterises as implicit ‘objectivist’ assumptions. For example, Batini et al (1992, p 15) claim “Data models are vehicles for describing reality. Designers use data models to build schemas, which are representations of reality”. Hirschheim et al (1995) characterise these approaches as ‘functionalist’ and, like Lewis, argue that data modelling in practice requires some ‘softer’ explicit paradigm. However, the ‘hard’ viewpoint, with objectivist approaches, is that most often implied. Not surprisingly, research methods have tended to adopt this hard approach, and the next section will argue that these assumptions make the research findings difficult to generalise to the practitioner domain.

The soft viewpoint is most clearly stated in the practitioner data modelling literature in the information engineering (IE) domain, although the theory did have a soft starting point. To illustrate the issue, consider part of Chen’s original definition for an entity; “Information concerning entities and relationships which exist in our minds” (Chen, 1976, p 10). This view is reinforced with the definition of an entity set as “... Let e denote an entity which exists in our minds”. (Chen, 1976, p 11). This was in the context of the ANSI/SPARC/X3 report on database models of 1975 (ANSI, 1975), which defined three realms in the philosophy of information: the real world, ideas about the real world existing in the minds of people, and symbols on paper or some other medium representing these ideas (ANSI, 1975, p. II-1). There are clearly non-objectivist issues here, although many texts define an entity only as a ‘thing’ in the real world. Indeed, the use of entity and object in names for modelling techniques suggests objectivity, whereas the models actually deal with entity-types or classes, which are much ‘softer’ concepts.

Practitioners do have to attribute meaning in the definition of entity-types, which is an indicator of non-objectivity. Wittgenstein’s (1958, p 31) definition of the entity-type ‘game’ is a well known example of the difficulties involved in defining seemingly simple concepts, and the issue is also discussed by Kent (1978). There is early evidence of practitioner appreciation of this in De Marco (1979, p 143) where data dictionary definitions are illustrated with, “When I use a word” Humpty Dumpty said, “it means just what I chose it to mean – nothing more nor less”. Interestingly, there are practitioner texts which imply some non-objectivist approaches to data modelling, for example Veryard (1992, pp 14 –15) deals with aspects of the underlying philosophical assumptions, including “... there is always a temptation to confuse symbol with reality, to confuse measurements with the things they measure” and “... a model is not just an objective description of a business situation, but expresses the intentions and perceptions of the key actors in the situation”.

Data modelling is a way to understand a business domain. Data models are “... representations with a specific purpose of helping to understand some aspect of the system”, Planch (1992, p 4). In practice, building a model helps the analyst to understand a business, it isn’t something done after that understanding is reached (some other way). If we could understand a domain without modelling, then there would be no need to model – we could simply write out a specification. Modelling is a technique for understanding, involving the problems of understanding social systems. “Entityrelationship models are not data structure models ... They are business models and, as such, they model business environments and depict business components”. (Modell, 1988, p 98). “... we as analysts must understand the user’s perspective. We must also understand the user’s words and the meanings which the user attributes to those words.... It is certainly critical to the analyst in the accumulation of that elusive body of facts known as ‘business knowledge’.” (Modell, 1988, pp 7–8). “Most methodologies do not allow for differences in data perspective or data use”. (Modell, 1992, p 30). Barker (1989), Martin (1990) and Veryard (1992), also from the IE domain discuss or imply these ideas, which are characterised by practitioner experience.

## What do we know about effective data modelling in the practitioner domain?

Despite the use of data modelling for over twenty years, there is relatively little published research on modelling effectiveness and there is some difficulty in collecting relevant information over many disparate sources – the literature sources quoted here are more exhaustive than in previous papers. This limited research is spread over several areas that can be characterised as experiments involving models for query interfaces, end-user validation, user diagramming from narrative, and a few papers that attempt to research practitioner modelling. Most of the research has concerned comparative studies. Kim and March (1995) identified six papers (Juhn & Naumann, 1985; Ridjanovic, 1986; Jarvenpaa & Machesky, 1986; Shoval & Even-Chaime, 1987; Leitheiser, 1988; Batra et al, 1990) comparing the use of data models, all using subjects who were students. Five of the six experiments compared the performance of entityrelational and relational models, although, in IE for example, these two models are used in a complementary way. Five out of six experiments were mainly concerned with end-user issues, rather than with model building. Hitchman (1995a) delved back a little further to include three comparative studies of logical database models (Lochovsky & Tsichritzis, 1977; Brosey & Schneiderman, 1978; Hoffer, 1982).

Hitchman (1996) identified a further three papers; Batra and Anthony (1994), who compared the use, by students, of entity-relational and relational models; Palvia et al (1992) who used students to examine end-user model perceptions; and Mantha (1987) who compared practitioner performance with dataflow and entityrelationship diagramming from a written scenario. Although Mantha explicitly experiments on practitioners, the diagrams chosen are already used, for example in SSADM, in a complementary, rather than competitive way. Mantha concluded that though both models are needed, they are not exclusive. Two other papers are by Amer (1993), who compared relational and entity-relational models, validated by students representing end users, and Bock and Ryan (1993), who compared student performance with an extended entityrelationship model and a particular OOM.

Batra and Srinivasan (1992, p 405) review the literature on experiments concerning models and database query performance, concluding that semantic data models “lead to better performance in many situations” compared to the relational model, although this is affected by the complexity of the task and the experience of the subjects. This research is not directly concerned with building models, but it is interesting that there is similar use of comparative studies and novices. Research includes Jih et al (1989) who used student subjects that were deliberately selected for their lack of database knowledge, and Davis (1990), who used students to test query performance using a data structure diagram, a list of tables and an entity-relationship diagram as different forms of documentation to work from. The finding was that graphical documentation improved performance, although no diagram seemed to be superior. Chan et al (1993) experimented on students with little database experience and found that those using entity-relationship diagrams performed better than those using the logicallevel relational model. Catarci and Santucci (1995) compared student performance using SQL and QBD\* (Query by Diagram). Using QBD\*, students performed queries through a Chen style entity-relationship diagram. Respondents (students and professionals) included naive and intermediate users, who produced significantly more correct queries using QBD\*, and expert users, who showed no significant difference in correct performance, although QBD\* took them significantly less time. Naive users showed no significant time difference. (Perhaps demonstrating the difficulty in locating literature, these authors believed their experiment was the first rigorous comparative study of this type and did not reference Chan et al (1993)).

Becker et al (1977) performed an interesting laboratory experiment on student subjects that examined the ease with which the subjects could manipulate structured sets of words (that could be analogous to data items from a database), which were jumbled, back into their original structure. Lists, hierarchies, networks and tables were the four structures considered. The experiments showed that the subjects had, as mental models, all of these structures for organizing. Giving the subjects a skeleton structure to work from made their organizational task more efficient. One of their conclusions was that “... when entering data into an information retrieval system it may be of help to allow the user to decide first that the data is best expressed in a particular organization, such as a table”. (Becker et al, 1977, p 13).

There is a mix of research here, with an emphasis on the separate issue of end-user use and validation. This latter seems to be superficially simpler than research, involving perhaps just model checking (often simplified to just diagram checking) and generally seems to be related to the ease of finding student subjects. It is often assumed that the end-users who check the model do not take part in the previous modelling process and may have little modelling training. The suggestion from the research is that, for naive users, the entity-relationship approach is easier to use than the relational model. However, Goldstein and Storey (1990) concluded that entityrelationship modelling is not intuitive, asserting that the technique is useful only when properly understood by the user.

Students are often assumed to represent end users. It is questionable whether the motivation for high grades, for example, can be transferred directly to motivation in the user domain of work. However, it is obvious from all of the research discussed, that no firm generalisation can be made to account for the activities of a skilled and experienced modelling practitioner. There are a few papers that either do not compare diagrams, or deliberately use practitioners (Batra & Davis, 1989; Nordbotten & Crosby, 1996; Shanks, 1996). These papers illustrate the generalisation issue.

Batra and Davis (1989) used protocol analysis to confirm the general literature on the differences in performance between novice and expert, finding that in conceptual modelling there are, indeed, differences. Nordbotten and Crosby (1996) measured the eye movements of subjects reading various data diagrams. Although all of the subjects were students, some were considered skilled readers and were shown to use significantly different viewing patterns. Articulation strategies were shown to vary according to the type of diagram. NIAM, for example, producing a ‘detailed’ strategy, against other ‘structural’ strategies.

Shanks (1996) used information system practitioners to show that novice practitioners produced data models of a lower quality than the experts, given a narrative case study. The narrative was transcribed from a taped interview with a domain expert. Shanks showed that experts “... rapidly develop a holistic understanding of a problem, categorise problem descriptions into standard abstractions and reuse generic data models from their previous experience.... Both expert and novice data modellers were rated low on understandability however which questions the usability of conceptual data models”. (Shanks, 1996, p 12).

There are important implications for research methods adopted to study the practitioner domain since studies of novices will not necessarily be generalisable to practitioners. It is less clear how these differences will affect the reading and validation of diagrams, but it is clear that only research on practitioners will provide information about modelling in the practitioner domain. The comparative research has other generalisability problems, but the widespread use of students as research subjects means that their results cannot be used to directly gauge practitioner effectiveness in building models.

One of the few comparative studies to use practitioners was undertaken by Kim and March (1995), to compare the use of ORM and ERM, although the subjects were not necessarily data modelling experts. This would seem to extend the generalisability, but the research was carried out in a laboratory environment, rather than in a practitioner domain. Setting the research out of context still raises complex generalisability issues that are discussed in more detail in Hitchman (1996). Two key points are discussed here, which apply equally to the other comparative research and both arise because of the implicit objectivist assumptions of the researchers.

The first point is concerned with the use of narrative in the research methodology. Subjects are given a narrative description of a domain (interestingly this is ‘in the minds of the researchers’) and are asked to draw a diagram, in one of two standards, that represents this narrative. Notice that the drawing of a diagram can be separated from modelling, which involves much more than just diagramming – although researchers often equate the two. The problem with the use of narrative springs from the assumption that narrative is an objective representation of reality. The implication is that diagramming the narrative is like diagramming reality and hence like modelling in practice. The narrative is presumably supposed to represent the language that would be used about a domain. That such natural langauge exists does not imply that modelling is a trivial task of diagramming, rather than a technique that is required to build an understanding of a domain. If narrative were sufficient there would be no need to model. The assumption is that we can draw a diagram of the narrative and ignore the major modelling problems. Veryard (1992, pp 183–184) sums up the problem in relation to learning data modelling:

Here is evidence that practitioners understand the implicit non-objectivist issues, but that researches tend to ignore them. A similar point is made about NIAM itself, by Darke and Shanks (1994), who discuss some limitations of NIAM in specifying the modelling process. The objectivist assumptions of NIAM lead to, for example, an assumption that requirements are predefined. Consequently, NIAM does not support the eliciation of emergent requirements from the interaction between analysis participants.

Here the TWS is identical in context to the diagram – each could replace the other. Barker (1989) makes it clear that TWS is mandatory, and these are to be found on most of the examples in the text, and TWS are used as a strong validation technique. TWS are also mentioned in the literature on ORM but are often omitted from diagrams (see Nijssen & Halpin, 1989, p 52 for the rationale for this). Further, Halpin advises that “... choose one standard way of stating the predicate, but optionally allow the reverse reading to be shown ...” (Halpin, 1995, p 42) and “... If desired the inverse predicate may be included ...” (Halpin, 1995, p 62). Scanning through an ORM text there are few examples of TWS. Similar thinking occurs in OMT (Rumbaugh et al, 1991) and in the newer unified modelling language (Booch & Rumbaugh, 1996). Arguably the use of TWS is better developed in ERM. Clearly any narrative can be formalised to completely match a diagram. The narrative thus becomes crucial to any test of diagramming and the research results could be affected by the form that the narrative takes. If the narrative is exact – the task becomes trivial. Otherwise the diagrammer is guessing about the ambiguities or missing information. Experiments that use narrative are therefore testing how well the narrative could have been written, with respect to a particular diagram standard – the experiments are not measuring practitioner modelling.

![](/api/attachments/8G22XKNW/fulltext/images/e9f9fb14906ad1fbf70e12b8ebccec5f26029a1c5b57bddf3d9f084dda0a4e8d.jpg)  
An employee must work for one and only one department A department may include one or more employees  
Figure 1 Sentence pairs.

However, the situation is more confused than this. Kim and March (1995) framed hypotheses on the basis that ORM made use of TWS, whilst their chosen extended entity-relationship model did not. ORM uses ‘directional verbs’ at attribute level, which means there is more detail in ORM in this respect, but choosing an ERM standard that does not use TWS is obviously going to bias the results. The problem here is in comparative tests of particular standards that may, or may not, represent effective practice. Further, this example shows that the use of particular comparative standards cannot be generalisd to, for example, ERM. Whilst many models claim competitive status, this ignores the fact that alternative approaches offer many complementary features. To emphasise the point, Venable and Grundy (1995) describe the conceptual integration of ER and NIAM models.

A final example of the problem of generalising laboratory findings to the practitioner domain is demonstrated in an elegant experiment by Siau et al (1996), the final paper to be discussed. Subjects were given diagrams (using a Chen standard) of semantic concepts that were deemed to be understood. An example is shown in Figure 2. The respondents were asked to decide whether a sharehold ‘may own’ or ‘must own’ shares. The (0,\*) is a syntactic constraint that specifies that a shareholder (0,\*) shareholder owns share

![](/api/attachments/8G22XKNW/fulltext/images/a0c2fdbb5e9a33e110bd913ab6237d69bd923a321f155eae57670a93e34e8141.jpg)  
Figure 2 Semantic and syntactic conflict.

may own shares, which conflicts with the semantic information (derived from the entity-type names) that a shareholder ‘must own’ shares.

The respondents were graduate MIS students, trained in data modelling and considered to be modelling experts (although not modelling practitioners). One of the findings was that, faced with a conflicting syntactic constraint, the diagram viewer tended to accept the ‘may own’ specification, which overrides their assumed semantic knowledge that a shareholder ‘must own’ shares. Siau et al (1995) also found a tendency for modellers to prefer optional relationships, arguing that these were a super-set of mandatory relationships.

This seems compelling, and shows something about diagram verification, but even with this highly constrained experiment, attempting to generalise the findings to the practitioner domain is non-trivial. Firstly, we have to assume what is meant by ‘share’. Is this a share belonging to the shareholder, or a share in general (i.e. a list of shares quoted on the exchange)? In the first case, the relationship is 1:M, in the last case M:N. Secondly, the question to ask about the optionality of the relationship revolves around “... must participate in ... relationship ... at all times” Siau et al (1996, p 405). It is common that we will ‘know about’ a shareholder, in a business domain, before we ‘know about’ the shares they may own. This is not the same as saying that ‘shareholders own shares’. In terms of the Oracle standard, this difference is shown in Figure 3.

There is potential confusion between the meaning of the entity-type name, implying that shares must be owned, and the meaning of the relationship, specifying which shares are owned. Part of the reason for modelling this scenario would be to formalise knowledge about whether we always know, for each shareholder, which shares they own. It would be quite legitimate to model the optional choice since this is not a model of reality, it is a model of what is understood about a particular business domain. Generally, this issue results in the optional choice, which is why this relationship is most comonly found on models (Barker, 1989). Arguably, a well trained modeller is likely to accept the syntactic constraint since there is no conflict with the possibility that they may not always know which shares are owned. Moving the research into the practitioner domain raises new questions about how and why the modelling process is used.

![](/api/attachments/8G22XKNW/fulltext/images/70af72ffec6e54f860e33caf351eedecdbedce21b826ef75abd95525a2525e23.jpg)  
A shareholder may own one or more shares ... means that we may or may not know which shares they own

![](/api/attachments/8G22XKNW/fulltext/images/1341a799982e7368f36493f97bf91dae03caabe5de203ffc680b0f15712b9c88.jpg)  
A shareholder must own one or more shares ...means we will always know of at least one owned share  
Knowing THAT shares are owned and knowing WHICH shares are owned is not the same thing in this formal modelling process  
Figure 3 Do we always know which shares are owned?

The result of considering practitioner issues therefore shows that laboratory research has limited generalisability. In general, an examination of the research uncovers a pattern of generalisability issues for the practitioner domain:

I research has concentrated on student subjects, not practitioners;

research subjects may have little training (for example a couple of hours) and represent naive users and not practitioners;

I subjects find the ‘correct’ solution from some narrative text – this is not modelling in the practitioner domain;

modelling is seen as a description of requirements and not as the tool for understanding a domain – the understanding is assumed both to exist and to be objective;

I the focus is on the diagram notation and not on the modelling process.

models chosen for comparison may be used in a complementary way in methodologies (such as data flow diagrams and ERM or some interpretation of the relational model and ERM).

The conclusion is that research currently resides in the academic domain, is underpinned by objectivist assumptions, shows a selective choice of model semantics, and tends to ignore practitioner literature and practice.

This is not to say that the research is not useful, it has added something to our knowledge of conceptual modelling, particularly concerning novice modellers. However, doubts are raised concerning what we really know about modelling by practitioners since there seems to be little direct research about effective conceptual modelling in the practitioner domain. It is tempting to conclude that, after more than twenty years of modelling practice, the only thing we can say with certainty is that, if you show a diagram to a novice modeller, they will both behave differently to knowledgeable practitioners, and will make mistakes in using the diagram. Concentration on particular or on competing modelling notations raises more questions than are answered. What is required, therefore, is some framework for thinking about and examining the modelling process.

## A knowledge approach and framework for understanding data modelling

Hitchman (1995b) has proposed a preliminary framework for data modelling, developed, in part, from the use of a knowledgebase product in a practitioner domain which facilitates a complementary view of apparently different modelling methods. A full discussion of the framework can be found in Hitchman (1995b). The framework is underpinned by an assumption that modelling is not considered to be some objective representation of reality, but a formalism for exploring the domain expert knowledge ‘information concerning entities ... which exists in our minds’. Attention thus shifts from modelling reality, to a model of domain expert knowledge of a business domain. This is characterised by the acronym arising from providing a ‘domain expert knowledge approach framework’, (DEKAF). DEKAF is in a preliminary state since it is not yet adequately used and is expected to be refined through its use in action research.

Data modelling involves analysis of what Stamper et al (1988) call information management, involving intention and meaning. The work on MEASUR (method for eliciting, analysing and specifying user requirements) involving NORMA (a knowledge representation language) and LEGOL (a manipulation language) highlights the problem in “climbing from the level of syntactis to the level of semantics” (Stamper et al, 1988, p 69). Data modelling is interesting since it attempts, in practice, exactly this semantic-syntactic bridge. DEKAF, unlike MEASUR, is not a new method for requirements analysis, but proposes a way of understanding and thinking about the modelling process. In particular, DEKAF provides a pragmatic way of avoiding the generalisability issues discussed, and helps to focus on the process rather than a particular diagram notation.

Other assumptions of DEKAF, concerning practice, can be characterised as:

available data modelling methods are complementary, rather than entirely competitive and imply some non-objectivist paradigm;

issues such as the political dimension or responsible participation are currently outside the DEKAF, within a wider methodological framework;

participation – the domain expert is using the data model as a tool to explore, understand and formalise their knowledge of a domain;

I the modelling process is not step-by-step, the appropriateness of the various techniques in data modelling will vary, a contingency approach;

I the data modelling method will be interpreted by its users.

The last three of these assumptions are not new in the context of ‘methodology’ and are adopted here from reflections concerning the Multiview exploration (Avison & Wood-Harper, 1990, pp 265–267).

Figure 4 shows the framework that is used to explore complementary activities in data modelling. Whatever modelling method is chosen, the activities shown are likely to take place, in the practitioner domain, during data modelling. The principle point here is that diagramming is not the only activity – modelling in the practitioner domain involves, for example, defining entity-types, and this could be a key activity. DEKAF therefore highlights the generalisability issues involved in diagramming from a narrative as an analogy for the modelling process.

![](/api/attachments/8G22XKNW/fulltext/images/08458ec22b37ca0c401ba9863f6c489b4b3b0631e248597d89546de81c1b55df.jpg)  
Figure 4 The (adapted) iterative data modelling framework.

TWS are given prominence and might be considered as either rules or facts in a domain, although both rules and facts have a wider context. Rules are an important component of the framework since they are “the outcome of social habitualisation, negotiation and other types of social interaction” (Hirschheim et al, 1995, p 198), reflecting the social construction of reality, rules are socially produced and maintained, continuously applied and instantiated. Rules describe social knowledge and raise many questions ignored by facts. The DEKAF users can choose to think, about TWS for example, in terms of rules for the domain, used by the domain expert, and not as facts about an objective domain.

Entity-types and their definitions are central to DEKAF, they are the concepts with associated meanings needed to understand the domain. How the business domain is scoped and represented by entity-types is not an obvious technique, it is “... rife with subtle social, linguistic and political problems which are by and large ignored in the fact-based data modelling literature” (Hirschheim et al, 1995, p 181). (In this context fact modelling is not a reference to the ‘old’ name for ORM – it is the name for a particular school of objectivist modelling that includes [according to Hirschheim et al] both ERM and ORM). Facts can be viewed not as assertions about some real entity – they are propositions made by the domain expert. This is harder to accept with a fact such as “a student is born on a particular date”, but rather easier with “a student has a particular IQ”, which involves problems of whether IQ is a valid concept and whether an objective measurement can be made. An assumption is, thus, that a business domain is ‘in the mind of the user’ as a set of sometimes complex concepts. In part, this accounts for the name of ‘knowledge approach’.

It is possible to define various approaches to using the framework; Hitchman (1995b) discusses one approach within the IE context, and related to CASE\*METHOD defined by Barker (1990). This approach requires the following stages. In Stage 1 the modellers establish their appreciation of DEKAF and their underlying conceptual foundations and philosophical assumptions. In Stage 2 the modellers confirm their understanding of, and agree the use of, a particular data modelling standard on a contingency basis. In Stage 3 (and also in later stages) the modellers develop the domain model.

Thus, DEKAF seeks to make philosophical underpinnings and modelling concepts explicit to the analysis team. A trival example is that, whilst the use of examples is dealt with in ERM (see, for example, Barker, 1989), it is formalised in ORM, where it is part of the underlying philosophy of the approach. Pragmatic motivations for this are simply that different techniques may benefit different domains, or be suitable for different users, or aspects of models, such as two-way sentences, may be ‘lifted’ from one model and used to complement another.

## Using DEKAF in action research

Having a framework helps in understanding apparently diverse competing diagram notations, and encourages examination of the whole modelling process. It is a vital piece of equipment in trying to establish what happens in modelling practice. Using DEKAF and action research should provide interesting findings that avoid the generalisability issues revealed by other approaches. The principal question discussed in this section is ‘what happens when DEKAF is used?’ This section evaluates the findings from one use of DEKAF.

DEKAF was used by a practitioner with a domain expert to understand a Housing Benefits domain, part of a district council system in England. The practitioner was not an expert data modeller, but had extensive data modelling training as a part-time student on a degree course. A full account of the findings and research methology can be found in Bailey (1996). The domain expert had previously been involved in systems analysis projects, but had not been exposed to building data models (which is consistent with the findings of Hitchman, 1995a). The number of entity-types was small, with 39 ‘facts’ (in ORM terms), and is much simplified since only one domain expert is involved. Therefore the research concerns a well trained but not highly experienced data modeller, and the generalisability of the findings stem from the use of DEKAF in the practitioner domain, as opposed to diagramming a narrative, which therefore extends previous findings.

In Stage 1, the domain expert, despite having been involved in the analysis of systems, is given the chance to think about some of the available techniques, their underlying philosophy and concepts, and this resulted in some ‘empowerment’ in the modelling process. There had been some concern in designing the research method that the domain expert would not want to be concerned with these deeper issues – there was a feeling that the domain expert would want to ‘get on with it’. This reflected informal comments that have been made to the author, at several sites, concerning the fears of practitioner analysts (who tend to then model in private). On the contrary, this domain expert became fascinated with the opportunities for understanding the domain.

During Stage 2 the domain expert chose to use ORM, given that the Infomodeller tool (version 1.5) was available. This task acted as a confirmation stage, and the domain expert became committed to the modelling process. The finding here suggests that if domain experts are to be actively involved then being explicit on the need for understanding, commitment and choice of modelling approach, rather than relying on some enforcement of a modelling standard, is successful.

In Stage 3 the domain expert and practitioner developed the domain model. The domain expert’s preference for using ‘facts’ (in the ORM sense) confirmed the assertions of ORM proponents – attempts to define entity-types resulting in the following kind of discussion:

“What is the definition of a tenant, why is a tenant significant for the business?”

“A tenant is someone who rents a property”.

The eventual definition of a Tenant was “Also known as Private Tenant. Person who rents and/or is looking to rent from a landlord or agent. The tenant is claiming or has a view to claim housing beneft”. (Support for synonyms was through the Infomodeller description, whereas preference would be for more explicit support). However, this definition followed iterations in the use of facts, definitions, frames and examples – led by the domain expert. This resulted in the use of these various activities for thinking, rather than some prescribed sequence of events. The domain expert switched between different activities in order to follow through their thinking. The DEKAF was designed around the assumption that this is what happens implicitly during modelling, and this is shown to be the case for this domain expert. DEKAF provides a simple framework for controlling the different modelling activities in a visible way that is loosely analogous to the claimed advantages of the ‘six thinking hats’ (De Bono, 1994).

Frames were used to visualise, for example, enquiry screens with one-to-many relationships. These verified the fact statements. Here the domain expert preferred to use frames for thinking about the examples, rather than the formalised population boxes of the fact model. This is probably because the frames look like input screens, but also reflects a preference to view data as tables, rather than constrained to ORM prescribed population boxes. This supports the view that data modellers will take advantage of complementary techniques if helpful.

Another supporting point concerning the use of ORM was that, although ‘value types’ were included in the model, the domain expert concentrated on those objects that equated to entity-types – the modelling was actually based on entity-types, but using ORM notation. It is not known whether this represent some bias on the part of the researcher – who was initially trained in ERM. The feeling was that concentrating on the types in the model caused less confusion – the inclusion of ‘value types’ tended to clutter the diagram. In this sense the DEKAF had prompted the users to adopt the ORM standard to suit themselves (which is also commonly believed to occur in the use of methodologies). This strongly supports the idea of using DEKAF to understand what modelling is actually carried out, rather than to assume that a particular method will be applied as specified.

The strongest evidence for the success of DEKAF comes from the fact that the domain expert had, by now, acquired such a good domain understanding that it changed their status within the ‘user group’ responsible for steering the suppliers of the required package. The domain expert realised that they now had a superior understanding of the domain and adopted a central role in the user group, feeling that they had changed the group from supplier-led, to user-led. It is the success in improving understanding of the domain that is shown here, and not the successful specification for a database. Further, the ‘fame’ of this approach has spread through the client site and the analyst has had requests to use it again on other projects.

## Conclusion

DEKAF proved successful in removing the pressure to model reality and providing the opportunity to think about and explore the domain, helping the domain expert think. There was an explicit change from concentrating on the domain, to concentrating on the domain expert – it is their business knowledge that is being modelled, not some reality. DEKAF provided the basis for examining how data modelling took place in practice as well as making assumptions explicit to the modellers. DEKAF also exposes the rather weak analogy of modelling as diagramming from a narrative, and helped to establish a viewpoint in which the generalisability of modelling research can be examined.

This action research needs to be confirmed by other uses of DEKAF, but these initial results are promising. Findings about what happens in the practitioner domain are stronger than has been the case with previous research and suggests that examining complementary issues will be more productive than performing constrained competitive experiments. It is now possible to promote the use of DEKAF to, for example, analyse expert modelling sessions in terms of the DEKAF framework to see how particular modelling standards are actually used by practitioners.

## References

<sup>Amer</sup> <sup>TS</sup> (1993) Entity-relationship and relational database modelling representations for the audit review of accounting applications: an experimental examination of effectiveness. Journal of Information Systems 7(1), 1–15.

<sup>ANSI</sup> (1975) Interim Report ANSI/X3/SPARC Study Group on Data Base Management Systems. FDT 7 (2), 7(2).

<sup>Avison</sup> <sup>DE</sup> and <sup>Wood-Harper</sup> <sup>AT</sup> (1990) Multiview: An Exploration in Information Systems Development. Blackwell Scientific Publications.

<sup>Bailey</sup> <sup>C</sup> (1996) A Knowledgebase Modelling Approach to Housing Benefit Management. Unpublished final year dissertation, C.G.C.H.E.

<sup>Barker</sup> <sup>R</sup> (1989) Case\*Method: Entity Relationship Modelling. Addison Wesley.

<sup>Barker R</sup> (1990) CASE\*METHOD: Tasks & Deliverables. Oracle/Addison Wesley.

<sup>Batini C, Ceri S</sup> and <sup>Navathe SB</sup> (1992) Conceptual Database Design: An Entity-Relationship Approach. Benjamin Cummings.

<sup>Batra</sup> <sup>D,</sup> <sup>Hoffe</sup> <sup>JA</sup> and <sup>Bostrom</sup> <sup>RP</sup> (1990) Comparing representations with relational and EER models. Communications of the ACM 33(2), 126–139.

<sup>Batra D</sup> and <sup>Srinivasan A</sup> (1992) A review and analysis of the usability of data management environments. International Journal of Man-Machine Studies 36, 395–417.

<sup>Batra D</sup> and <sup>Anthony SR</sup> (1994) Effects of data model and task characteristics on designer performance: a laboratory study. International Journal of Human-Computer Studies 41, 481–508.

<sup>Batra</sup> <sup>D</sup> and <sup>Marakas</sup> <sup>GM</sup> (1995) Conceptual data modelling in

theory and practice. European Journal of Information Systems 4, 185–193.

<sup>Batra D</sup> and <sup>Davis JG (1989)</sup> Conceptual database design by novice and expert database designers. Proceedings of the Tenth International Conference on Information Systems, Boston, Mass, pp 91– 99 (see also the later version: <sup>Batra</sup> <sup>D</sup> <sup>&</sup> <sup>Davis</sup> <sup>JG</sup> (1992) Conceptual data modelling in database design: similarities and differences between expert and novice designers. International Journal of Man-Machine Studies 37, 83–101).

<sup>Becker CA, Durding BM</sup> and <sup>Gould JD</sup> (1977) Data organization. Human Factors 19(1), 1–14.

<sup>Bloomfield</sup> <sup>BP</sup> and <sup>Daieli</sup> <sup>A</sup> (1995) The role of management consultants in the development of information technology: the indissoluble nature of socio-political and technical skills. Journal of Management Studies 32(1), 22–46.

<sup>Bock DB</sup> and <sup>Ryan T</sup> (1993) Accuracy in modeling with extended entity relationship and object oriented data models. Journal of Database Management 4(4), 30–39.

<sup>Booch</sup> <sup>G</sup> and <sup>Rumbaugh</sup> <sup>J</sup> (1996) The Unified Notation. Rational Software Corporation.

<sup>Brosey M</sup> and <sup>Shneiderman B</sup> (1978) Two experimental comparisons of relational and hierarchical database models. Journal of Man-Machine Studies 10, 625–637.

<sup>Catarci</sup> <sup>T</sup> and <sup>Santucci</sup> <sup>G</sup> (1995) Diagrammatic versus textual query languages: a comparative experiment. In Visual Database Systems 3 (Proceedings of the third IFIP 2.6 working conference on visual database systems), (<sup>Spallapietra</sup> <sup>S</sup> and <sup>Jain</sup> <sup>R</sup>, Eds), pp 69–83, Chapman & Hall.

<sup>Chan H, Wei K</sup> and <sup>Siau K</sup> (1993) User-database interface: the effect of abstraction levels on query performance. Management Information Systems Quarterly 17(4), 441–464.

<sup>Chen PP-S</sup> (1976) The entity relationship model: towards a unified view of data. ACM Transactions on Database Systems 1(1), 9–36.

<sup>Darke</sup> <sup>P</sup> and <sup>Shanks</sup> <sup>G</sup> (1994) Defining system requirements: a critical assessment of the NIAM conspetula schema design procedure. In Proceedings of the 5th Australian Conference on Information Systems (ACIS), 27–29 September, Monash University, Australia.

<sup>Davis</sup> <sup>JS</sup> (1990) Experimental investigation of the utility of data structure and ER diagrams in database query. International Journal of Man-Machine Studies 32, 449–459.

<sup>De</sup> <sup>Bono</sup> <sup>E</sup> (1986) Six Thinking Hats. Viking (Reprinted by Penguin in 1990).

<sup>DeMarco</sup> <sup>T</sup> (1979) Structured Analysis and System Specification. Prentice Hall.

<sup>Goldstein</sup> <sup>R</sup> and <sup>Storey</sup> <sup>V</sup> (1990) Some findings on the intuitiveness of entity-relationship constructs. In Entity-Relationship Approach to Database Design and Querying (<sup>Lochovsky</sup> <sup>F</sup>, Ed), pp 9–23, Elsevier Science.

<sup>Halpin</sup> <sup>T</sup> (1995) Conceptual Schema & Relational Database Design, second edition, Prentice Hall.

Hirschheim R, Klein HK <sub>and</sub> Lyytinen K <sub>(1995) Information</sub> <sub>Sys-</sub> tems Development & Data Modelling: Conceptual & Philosophical Foundations. Cambridge University Press.

<sup>Hitchman S</sup> (1995a) Practitioner perceptions on the use of some semantic concepts in the entity-relationship model. European Journal of Information Systems 4, 31–40.

<sup>Hitchman S</sup> (1995b) The development and evaluation of a knowledgebase approach to a method for the analysis and design of commercial computer systems. Unpublished PhD Thesis. Bristol University, England.

<sup>Hitchman</sup> <sup>S</sup> (1996) Doing Business with Active Research Studies of the Object-Role Model. In Proceedings of the BCS/ISM Fourth Conference on Information Systems Methodologies (<sup>Jayaratna, N</sup> and <sup>Fitzgerald</sup> <sup>B</sup> , Eds), pp 153–164, 12–14 September, University College Cork, Ireland.

<sup>Hoffer</sup> <sup>JA</sup> (1982) An Empirical Investigation of Individual Differences in Database Models. In Proceedings of the Third International Conference on Information Systems, December, pp 153–168.

<sup>Jarvenpaa SL</sup> and <sup>Machesky JJ</sup> (1989) Data analysis and learning: an experimental study of data modelling tools. International Journal of Man-Machine Studies 31, 367–391.

<sup>Jih K</sup> et al (1989) The effects of relational and entity-relationship data models on query performance of end users. International Journal of Man-Machine Studies 31, 257–267.

<sup>Juhn</sup> <sup>S</sup> and <sup>Naumann</sup> <sup>JD</sup> (1985) The effectiveness of data representation characteristics on user validation. Proceedings of the Sixth International Conference on Information Systems 212–226.

<sup>Kent</sup> <sup>W</sup> (1978) Data and Reality. North-Holland, Amsterdam.

<sup>Kim</sup> <sup>Y-G</sup> and <sup>March</sup> <sup>T</sup> (1995) Comparing data modelling formalisms. Communications of the ACM 38(6), 103–115.

<sup>Leitheiser</sup> <sup>R</sup> (1988) An examination of the effects of alternative schema descriptions on the understanding of database structure and the use of a query language. Ph.D. dissertation, University of Minnesota, Mineapolis (Quoted in <sup>Kim & March</sup>, 1995).

<sup>Lewis</sup> <sup>PJ</sup> (1994) Information-Systems Development. Pitman.

<sup>Lochovsky</sup> <sup>FH</sup> and <sup>Tsichritzis</sup> <sup>DC</sup> (1977) User Performance considerations in DBMS selection. Proceedings of ACM SIGMOD August, 128–134.

<sup>Mantha</sup> <sup>RW</sup> (1987) Data flow and data structure modelling for datab-

## About the author

Steve Hitchman is currently completing a sabbatical at Massey University, in the Department of Information Systems. He teaches data modelling and databases to undergraduate students and practitioners, as well as providing data modelling consultancy. His research interests include the use of knowledge-

ase requirements definition: a comparative study. MIS Quarterly 11 (Part 4), 531–546.

<sup>Martin</sup> <sup>J</sup> (1990) Information Engineering – A Trilogy. Prentice Hall, New York.

<sup>Modell</sup> <sup>ME</sup> (1988) A Professional’s Guide to Systems Analysis. McGraw-Hill.

<sup>Modell</sup> <sup>ME</sup> <sup>(1992)</sup> Data Analysis, Data Modelling, and Classification. McGraw Hill.

<sup>Nijssen GM</sup> and <sup>Halpin TA</sup> (1989) Conceptual Schema & Relational Database Design: A Fact Oriented Approach. Prentice Hall.

<sup>Nordbotten</sup> <sup>JC</sup> and <sup>Crosby</sup> <sup>ME</sup> (1996) Reading strategies for graphic models from an experiment in data model perception. In Proceedings of the Fifth International Conference on User Modelling (UM-96) pp 44–48, 2–5 January Kailua-Kona, Hawaii.

<sup>Palvia</sup> <sup>PC,</sup> <sup>Liao</sup> <sup>C</sup> and <sup>To,</sup> <sup>P-L</sup> (1992) The impact of conceptual data models on end-user performance. Journal of Database Management 13(4), 4–15.

<sup>Planch R</sup> (1992) Data Driven Systems Modelling. Prentice Hall International.

<sup>Ridjanovic</sup> <sup>D</sup> (1986) Comparing Quality of Data representations Produced by Non-Experts Using Logical Data Structure and Relational Data Models. PhD Dissertation. University of Minnesota 1986, reported in <sup>Batra</sup> et al (1990).

<sup>Rumbaugh</sup> <sup>J</sup> et al (1991) Object-Oriented Modelling & Design. Prentice Hall.

<sup>Shanks G</sup> (1996) Conceptual Data Modelling: An empirical study of expert and novice data modellers Monash IS Working Paper Series 6/96.

<sup>Siau</sup> <sup>K,</sup> <sup>Wand</sup> <sup>Y</sup> and <sup>Benbasat</sup> <sup>I</sup> (1995) A psychological study on the use of relationship concept: some preliminary findings. In Proceedings of the 7th International Conference on Advanced Information Engineering (CAiSE’95) (<sup>Iivari</sup> <sup>J,</sup> <sup>Lyytinen</sup> <sup>K</sup> and <sup>Rossi</sup> <sup>M</sup>, Eds), Finland, 12–16 June (Published as Lecture Notes in Computer Science 932) Springer Verlag.

<sup>Siau</sup> <sup>K,</sup> <sup>Wand</sup> <sup>Y</sup> and <sup>Benbasat</sup> <sup>I</sup> (1996) When parents need not have children: cognitive biases in information modelling. In Proceedings of the 8th International Conference in Advanced Information Systems Engineering (CAiSE’96), May, Heraklion, Crete (published as Constantopoulos P, Mylopoulos J <sub>and</sub> Vassiliou Y<sub>,</sub> <sub>Eds),</sub> pp 402–420, Lecture Notes in Computer Science 1080 Springer Verlag).

<sup>Shoval</sup> <sup>P</sup> and <sup>Even-Chaime</sup> <sup>M</sup> (1987) Data base schema design: an experimental comparison betwen normalisation and information analysis. Data Base Spring, 30–39.

<sup>Stamper</sup> <sup>R</sup> et al (1988) MEASUR: Method for eliciting, analysing, and specifying user requirements. In Proceedings of the IFIP WG 8.1 Working Conference on Computerised Assistance during the Information Systems Life Cycle (CRIS88), (<sup>Olle</sup> <sup>TW</sup> et al, Eds), (Published as Computerized Assistance During the Information Systems Lifecycle).

<sup>Turner P</sup> and <sup>Jenkins T</sup> (1996) Euromethod and Beyond: Open Frameworks for European Information Systems. International Thomson Computer Press.

<sup>Venable</sup> <sup>JR</sup> and <sup>Grundy</sup> <sup>JC</sup> (1995) Integrating and supporting entity relationship and object role models. In Proceedings of the fourth international conference in object-Oriented and Entity-Relationship Modelling (OOER’95) Gold Coast, Australia, December pp 318– 328, (Published as <sup>Papazoglou</sup> <sup>MP</sup> (Ed), Lecture Notes in Computer Science 1021, Springer Verlag).

<sup>Veryard</sup> <sup>R</sup> (1992) Information Modelling: Practical Guidance. Prentice Hall (BCS Practitioner Series).

<sup>Wittgenstein</sup> <sup>L</sup> (1958) Philosophical Investigations. Translated by Anscombe GEM, Basil Blackwell.

base models, understanding practitioner modelling in the analysis of commercial systems, and the development and implementation of data modelling standards and policies within commercial MIS departments.
