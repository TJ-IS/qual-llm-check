---
otero_id: 17823
otero_key: "W3NBB5Z4"
title: "On the nature of a data base and its use in inquiry — a tutorial"
authors: "E.Burton Swanson"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90032-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# On the Nature of a Data Base and Its Use in Inquiry - a Tutorial

E. Burton Swanson \*

Graduate School of Management, University of California, Los Angeles, Los Angeles, California 90024, USA

A tutorial on the nature of a data base is presented from the viewpoint of the human inquirer. The basic concepts associated with data bases and their use are identified and interrelated by means of a set of definitions. Data are seen to be natural language sentence expressions of a particular type, namely, statements given or taken as true for the purpose of inquiry. The concept of a structured datum is advanced as the basic semantic unit of communication in a data base. Information is regarded as a product of psychological inference, rather than a product of an automated data processing system.

Keywords: Management information systems, Data bases, Data semantics, Data architecture

![](/api/attachments/W3NBB5Z4/fulltext/images/fcb286877438fbbcfa6ceab30f269359c30cc95990b27d66c2f235d9ff4252e1.jpg)

Dr. Swanson is currently Assistant Professor of Computers and Information Systems at the Graduate School of Management, UCLA (1974–present). His primary teaching responsibilities are in the area of computer applications for management. His research has concentrated for the most part on the methodology of information system development, and in particular, on the relationships between designers and users of More recently, he has (with Dr.

information systems. More recently, he has (with Dr. B. Lientz) begun a study of the system maintenance process and its characteristics.

Previously, Dr. Swanson was Visiting Scientist with the Studengruppe für Systemforschung, Heidelberg (1972–1974), and prior to that, spent ten years with the IBM Corporation, mostly in the development of computer applications (1962–1972).

Dr. Swanson's Ph.D. is from the University of California, Berkeley (1971). His publications have appeared in Management Science, the General Systems Yearbook, Management Datamatics, and Data Management, among others.

## 1. Introduction

The emergence of “information systems” as a field of study has been accompanied by the introduction of many new terms. One reads today of “management information systems”, “decision support systems”, “distributed processing”, and so on, and the vocabulary for discussion grows daily.

Of particular significance at the moment is the terminology associated with data and data bases. In the earlier years of data processing, such terms as "files", "records", and "data items" were employed as a working vocabulary, but the conceptual foundations for their use were clearly weak. Subsequent developments in data base technologies have upset many an old notion, and a proliferation of new terms has resulted as researchers and practitioners have made new and finer distinctions at an increasing rate.

The current intellectual interest in data base theory is welcome, and new ways of thinking about data are now in evidence. However, until the essential portions of the theory are distilled from the unessential, the area will probably continue to suffer from a surfeit of, and a competition among, terms. (See ref. [21] for a review which draws correspondences among terms currently in use.)

The present situation is particularly difficult for the student of information systems who seeks an understanding of data bases independent of the terminological constraints imposed by any one of the competing models of implementation technologies. This paper is an attempt to respond to this difficulty.

The point of view of the information system user

## 1. SENTENCE EXPRESSION

An ordered selection of WORDS from an established VOCABULARY, formulated and expressed so as to communicate as a whole.

## 2. WRITTEN WORD

A configuration of one or more LANGUAGE CHARACTERS, representing a word in an established vocabulary.

## 3. WRITTEN MESSAGE

An ordered selection of language characters from an established CHARACTER SET, configured so as to communicate.

4. TEXT
Written messages consisting of a sequence of sentence expressions.

## 5. STATEMENT

A sentence expression admitting of evaluation as "true" or "false" within an established social context.

## 6. DATUM

A statement given or taken as "true" for the purpose of facilitating inquiry.

## 7. DATUM ELEMENT

A TERM, representing a PREDICATE included within a datum.

## 8. STRUCTURED DATUM

A representation of a datum, composed of a conjunction of datum elements, identifying and describing a single ENTITY observed.

## 9. DATA RECORD

Structured data associated with a given entity, formulated as a written message, encoded and recorded as required for storage, retrieval, and transmission.

## 10. DATA FIELD

A string of contiguous character positions within a data record, allocated to a datum element.

## 11. DATA FILE

A configuration of data records associated with the members of a particular class of observed entities.

## 12. DATA BASE

A configuration of data files which together represent some state-of-the-world relevant to an INQUIRER.

## 1. REPORT

Data, recieved and/or computed from a data base or other sources, arranged and presented so as to inform an inquirer.

14. MODEL BASE
A set of procedures which extends a data base by deduction.

15. QUERY
A written message, formulated by an inquires, used to generate a report from a data base.

Fig. 1. Definitional summary.

underlies the general question around which the paper is organized: what is the essential nature of a data base from the perspective of an inquirer who would make use of it?

In addressing this question, a definitional approach had been taken. The basic concepts associated with data bases and their use are identified, and related to each other by means of a set of definitions. In doing so, it is the concepts which are held to be important, not the particular words used. The viewpoint of Kaplan is adopted, who has remarked, "What makes a concept significant is that the classification it institutes is one into which things fall, as it were, of themselves. 'It carves at the joints', Plato said", [23]

![](/api/attachments/W3NBB5Z4/fulltext/images/29121f0b5b27e215b57cdce8e32194b03c9b5314ef5dc0080c2e707ae7bdbe70.jpg)  
Fig. 2. Terminological precedence relationships. Note: Defined terms appear in boxes, undefined terms do not.

Within the text to follow, each definition is numbered and offset for ease of recognition. Undefined terms appear in upper-case type at the point at which they are introduced. An attempt has been made to minimize their number and to clarify their use as needed.

A summary of the definitions is presented in fig. 1, together with a map of the terminological precedence relationships in fig. 2.

## 2. The world of the inquirer

A concept of an “information system” due to Mason and Mitroff [25] provides a point of departure for the discussion to follow:

We propose that an information system consists of at least one PERSON of a certain PSYCHOLOGICAL TYPE who faces a PROBLEM within some ORGANIZATIONAL CONTEXT for which he needs EVIDENCE to arrive at a solution (i.e., to select some course of action) and that the evidence is made available to him through some MODE OF PRESENTATION. [25] (authors' original emphasis)

In general, such a person may be termed an INQUIRER. Many special types of inquirers may be said to exist, e.g., a manager, a scientist, a student, or a philosopher.

In the absence of a formal information system, an inquirer obtains needed evidence through informal means, by "direct observation", and by verbal communication with others.

An inquirer may also search his own mind, calling forth past observations or communications, or generating new ones upon reflection. In any case, however received or generated, a fundamental form of evidence for an inquirer is the sentence expression in a "natural" language:

## 1. SENTENCE EXPRESSION

An ordered selection of WORDS from an established VOCABULARY, formulated and expressed so as to communicate as a whole.

WORD and VOCABULARY are treated here as primitives, although, as Quine has cautioned, "what counts as a word, as against a string of two or more, is less evident that what counts as a sentence, ..." [29:13]

Sentence expressions are individual events. Sentences themselves are universals, repeatedly approximable linguistic norms; i.e., the identical sentence may be recognized as expressed in a variety of situations (Quine [30]). The distinction is important, for it is sentence expressions which convey evidence, according to circumstances of issuance. Sentences have only the potential for doing so.

Sentence expressions are thus the outputs of persons communicating by means of a language, as well as fundamental inputs to any individual inquiry. Sentence expressions might, therefore, be considered the primary manifestation of thinking-type inquiry. (The notion that psychological thought processes are rooted in language has been explored by Whorf [45]. In a different vein, Chomsky [10] argues that innate “linguistic competence” is the central feature of human mental organization.)

A sentence expression may take any of several communicative forms; e.g., it may make an assertion, raise a question, or constitute an exclamation. The use of a written language is not presumed. Only a small fraction of the world's peoples possesses a written language, although a spoken language is common to all. (Pei [35: 5])

A spoken sentence communicates not only through its ordered word selection, but in other ways as well. For example, it is one thing to question:

Does John ever make mistakes?

Another, to assert:

Does John ever make mistakes!

An ordered word selection must thus be "formulated and expressed" so as to communicate clearly. A variety of vocal means are employed: e.g., (i) giving inflections to individual words—using certain prefixes, suffixes, and "internal changes" according to grammatical rule or custom; (ii) giving stress or pitch accent to individual word syllables; (iii) applying appropriate juncture—pauses of silence—between words and word syllables; and (iv) using intonation in pitch and cadence within the statement as a whole.

[28: 9, 52] Visual cues are also used to facilitate face-to-face verbal communication.

The expression of a sentence in written form requires new considerations. First, is the representation of a word:

## 2. WRITTEN WORD

A configuration of one of more LANGUAGE CHARACTERS, representing a word in an established vocabulary.

By LANGUAGE CHARACTER, we do not imply an alphabetic character. Syllabic-alphabetic writing is only one of two main varieties among the world's peoples. Pictographic-ideographic writing also exists, e.g., in Chinese, with its written symbols representing thought concepts "directly", rather than through corresponding spoken symbols.

Note also that the set of characters employed may include more than those used in the representation of words. Written sentences require various forms of punctuation to convey the meaning intended by their vocalized equivalents. And quantitative discourse often involves the use of special symbol systems.

While the language character is the basic building block in written communication, the WRITTEN MESSAGE is the product of its one-by-one deployment:

## 3. WRITTEN MESSAGE

An ordered selection of language characters from an established CHARACTER SET, configured so as to communicate.

One type of written message is TEXT:

## 4. TEXT

Written messages consisting of a sequence of sentence expressions.

But text is only one form which a written message may take. It might also consist of nothing more than the following:

## 200, 163, 50, 38, 27

which represents, in thousands of dollars, the five greatest annual municipal noise abatement expenditures in the United States for 1972, made respectively by New York, Chicago, Las Vegas, Boston, and Philadelphia. The communication of the semantic content of such a message presumes "a priori information" on the part of the receiver.

But even with text, the problem is not to simple, as Colin Cherry has noted:

A printed text is not simply a chain of words, picked one at a time; it is a whole. It has a structure, but it has meaning for us only if it represents a continuity of our experience of past texts. A text in some strange foreign language sets up an abrupt change in our experience, a discontinuity, and we make nothing of it. [9: 74]

Further, “foreign language” problems are not always geographically-based, as Kenneth Boulding lamented upon his readings of the new mathematical economics:

I'm like a rat within a maze.

When faced with sigma's i's and j's,

A. problems soon become enigmas

When wrapped in $i$ 's and $j$ 's and signis.'s. [2: 25]

A written message may also be encoded. Thus, a message stored on punched card employs a bit representation scheme based on the relative positions of holes within the card. Communication by means of an encoded message presumes that the receiver of the message knows a priori the code to be employed, or else is willing to decipher it.

## 3. The ontology of data

“Data” is commonly taken to be the basic substance for computer-based processing. But what are data, to an inquirer? Among the sentence expressions of a natural language, certain of these are of a particular type:

## 5. STATEMENT

A sentence expression admitting of evaluation as "true" or "false" within an established social context.

This follows the terminology of Quine, who has said: "The peculiarity of statements which sets them apart from other linguistic forms is that they admit of truth and falsity, and may hence be significantly affirmed and denied." [30: 1] Admission criteria are not well defined, however; hence the inclusion of an "established social context."

The sentence expression

"Corporate profits reached an all-time high last year."

should be affirmed or denied in many a specific situation and is thus an example of a statement.

The members of the social community need not all agree as to a statement's truth or falsity. However, agreement is assumed on the admissibility of the expression for evaluation as true or false.

Now if a statement is held to be "true" for the purposes of inquiry, it may be termed a DATUM:

## 6. DATUM

A statement given or taken as “true” for the purpose of facilitating inquiry.

That a datum is “given or taken” is held here to be noteworthy, as Kaplan has observed:

Nature might better be spoken of as an obedient child than as a protective mother; she speaks only when spoken to, is often seen but seldom heard. Data come to us only in answer to questions, and it is we who decide not only whether to ask but also how the question is to be put. Every question ... has its own presuppositions. It must be formulated in a language with a determinate vocabulary and structure, the contemporary equivalent of Kant's forms and categories of the knowing mind; and it follows upon determinate assumptions and hypotheses, on which the answer is to bear. How we put the question reflects our values on the one hand, and on the other hand helps determine the answer we get. [23: 385]

Thus, it is probably a mistake to think of data principally as "input" to an information system. For data are themselves a product of a process of inquiry. (See also ref. [12].)

But data, as processed by automated systems, do not typically present themselves in the form of statements. One speaks instead of "data items" or "data elements", "data fields" and "data records". We must therefore bridge the gap between the language natural to an inquirer, and the structure of data natural to a computer-based system.

Consider the datum:

"John P. Jones, Student Number 402-63-2644, is enrolled for graded credit in Mgt 225A, 'Introduction to Information Systems', on July 4, 1976. His enrollment position is 1st in class."

which describes a student enrollment in a university class. This “fact” would be one of a family of such during a period of enrollment.

Each datum within the family of enrollment data may be represented in terms of the same types of "elements", which are named here:

STUDENT NAME (E.SN)
STUDENT IDENTIFICATION NUMBER (E.SID)
COURSE TITLE (E.CT)
COURSE IDENTIFICATION NUMBER (E.CID)
DATE (E.DT)
FORM OF CREDIT (E.CR)
CLASS POSITION (E.CP)

Abbreviations for the names are shown in parentheses. The prefix 'E.' is used to specify that elements of an enrollment datum are being referenced.

For the particular datum of our example, we might write:

```txt
E.SN = 'John P. Jones'
E.SiD = '402-63-2644'
E.CT = 'Introduction to Information Systems'
E.CID = 'Mgt 225A'
E.DT = 'July 4, 1976'
E.CR = 'graded credit'
E.CP = '1'
```

where the names of elements thus assumes “values”, as if they were variables.

Each of the above might be thought equivalent to a statement, admissible in its own right as a datum. But the context for judging the truth or falsity of the element expressions is always one and the same specific enrollment. Taken individually, it is possible for each element expression to be true of more than one enrollment. (For example, the first element expression would be true of each enrollment in a course by a John P. Jones.) If we were to assert the truth of each for some enrollment, but the enrollment referred to was not the same in each case, the truth of the original datum would not be conveyed. Thus, the element expressions communicate as a whole, and not in isolation from one another. The datum is, in a sense, an irreducible unit of communication.

The element expressions of our example are best understood as PREDICATES, dependent for their truth or falsity on a specification of an enrollment. The elements 'John P. Jones', '402-63-2644', 'Intr duction to Information Systems', are examples of TERMS employed to convey predicates. The distinction between statements and terms is well expressed by Quine:

It is the peculiarity of a statement to be true or false. It is the peculiarity of a term, on the other hand, to be true of many objects, or one, or none, and false of the rest. [30: 64]

The objects, of which predicates may be true or false, are the ENTITIES around which much discussion in the data base literature has centered. In the example at hand the enrollment is the entity.

The concept of a datum element may now be defined:

## 7. DATUM ELEMENT

A TERM representing a PREDICATE included within a given data.n.

Note that a single term, e.g., “John P. Jones”, may represent the same predicate in more than one datum (e.g., where Mr. Jones enrolls in more than one course): and, further, that the same term may represent more than one predicate (e.g., in the case of a datum describing the admission of Mr. Jones to the University). However, a datum element is understood here to be local to a single datum. Multiple occurrences of “John P. Jones” in a collection of data represent multiple datum elements.

From the elements of a single datum, it is possible to represent the datum itself by means of the predicate calculus. For the example we may write:

E(E.SN = 'John P. Jones' ∧ E.SID = '402-63-2644' ∧
E.CT = 'Introduction to Information Systems' ∧
E.CID = 'Mgt 225A' ∧ E.DT = 'July 4, 1976' ∧
E.CR = 'graded credit' ∧ E.CP = 1)

which may be read:

"There exists an enrollment such that the enrolling student name is John P. Jones and the enrolling student identification number is 402-63-2644 and . . ."

Note that it is the conjunction of the simple predicates relative to a single enrollment which conveys the truth of the datum.

Significantly, the entity identified and described by a datum may or may not be uniquely identified by any single element within this datum. For example, in the case of the enrollment, identification is by student identification number and course identification number taken jointly within the context of an enrollment term. In some theoretical formulations, an attempt is made to categorize elements as either "identifiers" or "attributes". But this is misguided; all elements should be understood to represent predicates.

A general form for the structuring of a datum is the following:

## entity (predicate ∧ predicate ∧ ... ∧ predicate)

where as many predicates are included as there are elements of the datum. But note especially the ontological claim: "There exists an entity such that . . ." It is in this limited sense, perhaps, that data purport to represent "facts". Such expressions do constitute statements which may be affirmed or denied, accepted or rejected. But this does not prevent other than factual representations within the data; e.g., we might collect rumors as data, using the form, "There exists a rumor such that . . ."

One complication to the general formulation should be noted. Strictly speaking, it is only of "one-place predicates". That is, the predicates are true of a single entity. However, predicates may also be formulated for entities taken as pairs, triplets or n-a-t-a-time. "Relationships" are thus established. We regard the relationship simply as another entity, following the view of Date:

Many database texts (and systems) consider entities and relationships as two fundamentally dissimilar types of object. However, an association between entities may itself be considered as an entity. If we take as our definition of entity “an object about which we wish to record information”, then an association certainly fits the definition. [19: 4]

Note that the enrollment entity of our example may be considered as an association between a student entity and a class entity.

Should any datum be represented in the above general form or its equivalent, it will be termed a STRUCTURED DATUM:

## 8. STRUCTURED DATUM

A representation of a datum composed of a conjunction of datum elements, identifying and describing a single ENTITY observed.

The usefulness of structured data in computer-based processing is well established. For consider again the enrollment datum of our example: this datum will be but one of a family of enrollment data of the single structure:

$$
\begin{array}{r l} \mathrm{E(E.SN} & = t _ {1} \wedge \mathrm{E.SID} = t _ {2} \quad . \mathrm{E.CT} = t _ {3} \wedge \mathrm{E.CID} = t _ {4} \\ & \wedge \mathrm{E.DT} = t _ {5} \wedge \mathrm{E.CR} = t _ {6} \wedge \mathrm{E.CP} = t _ {7}) \end{array}
$$

where $t_{i}$ represents the ith term within the predicate conjunction. To represent the family of enrollment data, one need record only the sequence of terms specific to each enrollment. The structure is implicitly understood.

Data processing practitioners no doubt recognize the “structured datum” as akin to the “logical record” talked about elsewhere. And the concept of a “datum element” closely resembles a “data item”, or “field”. These parallels and close equivalents are not accidental; it is our purpose to bridge the gap between the world of the inquirer and that of the computer-based system. But a word of caution is in order: no presumptions about recorded data forms have been intended in this section. An attempt has been made to confine the discussion strictly to the “infological level” [38,39], i.e., to the question of what is represented by data to an inquirer. It is only in the section to follow that we take up the corresponding question of how these representations are physically structured.

## Background reading \*

One of the earliest contributions toward a theory of computer-based data was the "information algebra" [13]. For a recent review of subsequent work, see Verrijn-Stuart [44].

In another important early paper, Mealy [26] offered that "data are fragments of a theory of the real world". He went on to propose a model of data in which many of today's concept are to be found, including that of "entity". Chapin [8] in a following paper, questioned the inclusion of the concept of "entity": "The concept of an entity does not appear ... to be an essential feature or even a convenient concomitant. The entity, if it be posited, is apparently to enable a representation of a relationship between some 'reality' and 'values'. But this relationship lies in the mind of the beholder, it is a personal matter, external to a consideration of data and data processing". [8: 634] Following Chapin, Stamper [37] avoided the use of the entity concept. However, it remains an essential feature in the writings of most, e.g., Fry and Sibly [21].

The distinction between “infological” and “datalogical” levels of information processing (Langefors [24] and Sundgren [38,39]) represents another important contribution to a theory of data. According to Langefors: “... the special device of making a clear separation between the infological task of defining user needed information and the datalogical task of representing this information by data and data processing in a way that makes efficient use of data technology are basic to information system design.” [24: 937]

Langefors equates “information” to “knowledge” (of someone relative to an “object system”) and “data” to “physical signals or symbols”. Sundgren’s definition of data is perhaps equivalent: “If a person intentionally arranges one piece of reality to represent another, we shall call the former arrangement data, and we shall say that the arranged piece of reality is a medium, which is used for storing the data.” [39: 9]

Of particular importance to the development of the concept of a “structured datum” has been the work of Codd [16–18] on a relational model of data.

The work of Senko [31-35] has also been influential. The concept of entity plays a central role in Senko's theory, as it does here, though it is used somewhat differently.

## 4. The data base

In general, it is not necessary that a datum assume a written form. Much data will be verbally generated, communicated, and absorbed within any social group, without being set to paper or punched card. Often, however, a datum will be structured and formulated as a written message. Its elements will be assigned relative positions within the message structure, and these positions will be assumed to be understood by both sender and receiver.

If a structured datum is to be communicated in the form of a written message, it must be recorded. The DATA RECORD thus constitutes an important concept:

## 9. DATA RECORD

Structured data associated with a given entity, formulated as a written message, encoded and recorded as required for storage, retrieval, and transmission.

In the simple case, a data record may consist of one structured datum only. However, as understood here, a data record may also consist of more than one datum. Although the classes of entities referred to by data within a record may be various, one entity class is predominant in the sense that each datum makes reference to a common entity within it. An element identifying this common entity is often termed the record key. One knows from a particular record key that the data of the record refer to the one entity identified and to no other within the same entity class.

Data associated with a single entity may also be allocated among several distinct records. However, with the exception of a datum decomposable into smaller units of data, a single structured datum should always be contained within a single record.

A data record may itself be recorded over more than one physical unit of a storage medium; it is therefore not to be confused with the physical record, the unit stored or retrieved physically. But if a data record is to be broken up, such that its component parts are stored on distinct physical units, a nontrivial problem is introduced: that of maintaining the logical contiguity of the message. In some cases, this is dealt with rather simply; an ordering of the physical units is employed so that the reader knows that an interrupted message is continued on the next unit. However, other more sophisticated possibilities exist.

The recording of structured data requires that datum elements be assigned positions within the written message:

## 10. DATA FIELD

A string of contiguous character positions within a data record allocated to a datum element.

The term "field" has often been used interchangeably with, "datum element" as defined here, or with "data item". However, its origin in data processing was with the construction of "record layouts", where the character positions of the record were marked off according to the elements assigned. Hence our definition serves to make a distinction between "occupier" (the element) and "place of occupation" (the field).

It is noted that character positions are not identical to storage positions, per se. Computer-based data are stored typically in encoded form, and the choice of code, as well as the architecture of the storage medium, will influence the storage requirements.

In straightforward cases of data recording, the data of a record and the data fields associated with these data are physically contiguous as recorded and stored. However, where the record is stored over more than one physical unit the physical contiguity of the message is seldom maintained.

In the absence of physical contiguity, pseudo-data fields containing pointers are typically employed to maintain the logical organization of the record. A pointer refers to a location within the physical system where a continuation of the data record is to be found. It is an element of data about the data of primary informational interest; i.e., it is an item of metadata.

It is typical of data recording that metadata are introduced in a supporting role. In punched card systems, the use of the transaction code is one example; in magnetic tape systems, the use of a repeating-field indicator for variable-length records is another.

Metadata may be used to describe an information system to an inquirer, as well as to assist in its internal management. A data dictionary in which the elements of data within the system are defined and interpreted is an example. (see ref. [42].)

One further consideration here is important: hierarchical record structures. Hierarchies of data are typical within any established collection. Often, the data of the hierarchy are organized so as to be “superior” or “subordinate” to one another. Pointers are frequently employed in conveying the superior-subordinate relationships. Access to a superior datum typically provides directed access to its subordinate data. Access to a subordinate datum sometimes provide directed access to its superior datum, or to other of the data subordinate to this superior. A datum may be subordinate to more than one other datum where multiple hierarchies are established.

A more general network model may also be employed to portray the superior-subordinate relationship, permitting a datum to be subordinate to multiple data within the system. The architecture of the Data Base Task Group (DBTG) of the CODASYL Programming Language Committee provides an example of this more general approach. [14,15]

Two consequences of hierarchical record structuring are significant: first, a given datum may be recorded multiple times within the collection, e.g., where it must be forced into a tree structure model of data organization; second, a given datum may not be unique to a record, even where singly recorded. The classic example of hierarchical data is the bill of material common to the manufacturing organization. Here the “is contained in” relationship from which hierarchies are constructed finds c literal application.

But a careful distinction needs to be made at this point in the discussion: Hierarchical relationships among data and hierarchical record structures are not one and the same. Hierarchical record structures among data are those based on data content, so, on datum elements. Hierarchical record structures, on the other hand, are an artifact of record design; i.e., they are a consequence of choices made relative to “superior” and “subordinate”, or “owner” and “member”. In portraying hierarchical relationships among data, it is not necessary that record structures be hierarchical; however, hierarchical record structures are commonly employed.

Hierarchical record structures sometimes employ a tree structure model of the superior-subordinate relationship. In this situation, any datum is subordinate to at most one other datum. IBM's Information Management System (IMS) is an example of a database system employing this model.

We turn now to a consideration of collections of data records. Data records associated with entities which are members of the same class (e.g., the parts in an inventory, or the students in a school) are typically grouped together into a DATA FILE.

## 11. DATA FILE

A configuration of data records associated with the members of a particular class of observed entities.

As recorded, a sequence to the records in the file is typically established. A “random order” is said to exist where physical sequencing is independent of the content of the data within the records. Note that data files may share, in part, the same data. Further, data need not be multiply recorded in order for this to be the case.

When a set of data files is used to meet the information needs of inquirers, the term DATA BASE is often applied:

## 12. DATA BASE

A configuration of data files which together represent some state-of-the-world relevant to an INQUIRER.

A data base is often considered to be more than a configuration of data files [5,36]. Characteristics such as minimization of unnecessary redundancy of data, separation of data definition from procedural logic, company-wide application, and others are sometimes considered necessary considerations for regarding a data collection to be a data base. While recognizing the desirability of many of these characteristics, we do not regard them as essential to our definition.

Data bases may be defined in terms of certain organizational functions (e.g., marketing or personnel), or in terms of some organizational subunit (e.g., an agency or a division), or in terms of an organization as a whole (e.g., a firm). A data base is also usually associated with a particular information system; e.g., a "Shop Floor Control System" in a manufacturing plant may reference a data base which includes (i) an Item Master File containing planned production orders for which resources have yet to be committed, (ii) an Open Order File of released production orders for which resources have been committed; and (iii) a Work Center File of data relative to the resources of each work center in the shop to which a production order is or may be assigned.

The inclusion of a file in a data base which serves one organizational function (e.g., the Item Master File) need not preclude its inclusion in a data base defined to serve another function (e.g., the Item Master File would also serve a Requirements Planning System.) Certain files may thus be shared between data bases, or a single “higher-order” data base may be defined to serve several integrated organizational functions each of which accesses only a few of the files in the system.

## Background reading \*

A recent issue of Computing Surveys is a major publication on the subject of data bases. It contains a comprehensive review of the evolution of data-base management systems by Fry and Sibley [21], as well as individual studies of the three major theoretical approaches: the relational, Chamberlin [7]; the CODASYL Data Base Task Group (DBTG), Taylor and Frank [40]; and the hierarchical, Tsichritzis and Lochovsky [41]. A comparison of the relational and CODASYL approaches by Michaels, Mittman, and Carlson [27] completes the special issue, which 'been made available in Europe through IAG \*.

It will be useful to indicate the correspondences between the terminology here and that of the existing major approaches. First, the CODASYL DBTG uses the term "set occurrence" where we use "data record". [40: 71] The DBTG term "record (occurrence)" corresponds roughly to the occurrence of a datum. (A DBTG record is not necessarily of a single datum.) Under the hierarchical approach the data record is recognized as a "data-base tree", sometimes called also a "data-base record" [41: 111], or a "logical entry" [41: 116]. Under the relational approach, explicit definition of superior-subordinate relationships does not take place: the recording of a "tuple" constitutes the only form of data record as defined here.

Date [19] is an excellent source for the study of the major data base approaches.

A survey of the developing technology of data management and data base management systems may be found in Canning [5]. A second article [6] deals with the debate surrounding the proposal of the CODASYL Data Base Task Group (DBfG) for data definition and manipulation language specifications [14,15] in the light of a set of recommendations made by the Joint Guide-Share Data Base Requirements Group [22].

A recent text providing a good working introduction to data bases is that of Sprowls [36].

## 5. Computer-based inquiry

Data in a data base are encoded and organized to facilitate storage, processing, and retrieval, whereas data to be presented to an inquirer typically take the form of a REPORT:

## 13. REPORT

Data, retrieved and/or computed from a database or other sources, arranged and presented so as to inform an inquirer.

Perhaps the most basic form of a report is the one which simply lists structured data retrieved from a data base. However, reports may also consist of data which have been computed from the data base at the time of report generation. One common example is the accumulation and presentation of accounting totals based on the processing of an accounts receivable file. Such computed data are examples of derived data, i.e., facts established by a data base together with certain deductive procedures.

Reports may include more sophisticated forms of derived data; e.g., a forecast generated from the application of an econometric model, or an optimal reorder quantity in the management of an inventory. In the first case, the attempt is to facilitate the production of predictive information; in the second, to facilitate the production of decisive information [11]. In both cases, it is the use of a model which enables the informational capacity of the data base to be extended.

Models are typically expressed in terms of computational procedures, and constitute an important component of the information system:

## 14. MODEL BASE

A set of procedures which extends a data base by deduction.

Computed data generated from a data base may be considered an extension to a nucleus of the data base, an extension made possible by the model base [39]. Data within the nucleus are fundamental data. Their essential truth of falsity is a priori; i.e., not subject to deduction by means of the model base of the system.

The data cf a report, whether computed or simply retrieved, may further be presented in forms which extend their informational import in other ways, e.g., data may be displayed graphically. It may or may not be the case that “a picture is worth a thousand words” in such situations, but it is certainly true that new informational possibilities are opened up when pictorial techniques are employed.

The process of inquiry, whether computer-based or not, consists of asking questions, as well as receiving “answers” provided by reports. In the earlier years of data processing, an inquirer’s computer-based reports were always produced according to “pre-defined” needs. This practise sometimes sufficed; however, in many situations it was unresponsive to management’s new questions.

With modern computer-based systems, an inquirer can often make online inquiries from a terminal by means of a special “query language”. The concept of a QUERY is thus important:

## 15. QUERY

A written message, formulated by an inquirer, used to generate a report from a data base.

A query is not equated here with the natural-language

\* See announcement in the back of this issue.

question. Rather, a query is thought of as a command to a data processing system to produce a certain form of report.

An inquirer may sometimes engage in conversational interaction with a data processing system. Such a conversation is typically one-sided: queries are submitted by the inquirer and reports are provided by the data processing system. Information thus accrues to an inquirer, not a data processing system. However, in some cases, a data processing system may obtain new data from the inquirer, through the issuance of a message constituting a request to the user.

Perhaps the two most frequently defined concepts in the information systems literature are "data" and "information". While a definition of "information" will not be formally attempted in this paper, a distinction between data and information will be made.

“Data” is defined by Burch and Strater [4] as “raw facts in isolation which, when placed in a meaningful context by a data processing operations(s), allows inferences to be draw.” [4: 23] The task of data processing is thus perceived by some to be the converting of data to “information” through the editing and formatting of reports.

Placing data in context is sometimes thought of in the sense of imbedding a series of quantities, such as 54, 65, 74

within sentence expressions or their equivalents, e.g.,

"Albert is 74 inches tall, is 65 years old, and has 54 thousand dollars." [43]

Thus, by implication, while “data alone contains no information” [43: 44], a well-edited and presented report does.

But such an approach wrongly conceives of data as numerals, thus improvising the concept of data. Further, it leads to the conclusion that information may be generated by a data processing system, independent of the individuals who are to be informed.

Professor Horst Rittel's informally-made remark that "information isn't stored; it happens to somebody" seems to me the most insightful notion of "information". The context which converts data to information is not provided by data processing alone; it is brought to the problem by the inquirer as well.

"Data", as defined in this paper consists itself of sentence expressions of the type to provide the context for information. A series of numbers such as

## 54,65,74

are not data themselves, but, at most, datum elements, without import as data except within the context of full statements given or taken as "true" by an inquirer.

## 6. Conclusion

The term logical structure is currently used to describe a user's view of data; the term physical structure describes the way data are stored within a data base [21]. In this paper, we have been concerned fundamentally with the logical structure of data.

Research on the logical structure of data is vital to current efforts to establish “data independence” by means of data base management systems. According to Fry and Sibley, two types of data independence must be distinguished: “physical data independence” and “logical data independence.” In the first case, a system’s programs and user’s queries are relatively independent of the storage and access methods employed. In the second, there is “the ability to make logical change to the data base without significantly affecting the programs which access it.” At present, “… a serious attempt is being made to understand how much logical change can be made without adverse affect on the program … Full data independence appears, however, to involve an understanding of data semantics, the formalization of the meaning of data. Research on data semantics is currently in its infancy.” [21: 13]

This paper has sought in part to make a small contribution toward a theory of data semantics. Its particular emphasis, in this regard, has been on an interpretation of data in terms of language “natural to an inquirer”. Data are seen to be natural language sentence expressions of a particular type, namely, statements given or taken as true for the purpose of inquiry. Data are commonly represented as structured data, and it has been seen that the elements of a structured datum have full semantic import as a conjunctive whole rather than individually. The structured datum is thus the basic semantic unit of communication in a data base.

Other approaches to data semantics are to be found in Abrial [1], Biller and Neuhold [2], and Earley [20].

An understanding of the logical structure of data is of vital importance to the development of a methodology to support the architects of data structures. According to Taylor and Frank: "Data-base management systems are tools to be applied by the users of these systems to build an accurate and useful model of their organization and its information needs ... There is currently very little theory which can guide a designer in the construction of this model, though there are several guidelines that can be formalized." [40: 68]

The development of a theory of data architecture, which consists of the making of design choices among alternative logical and physical data structures, is one of the more pressing challenges facing researchers in the data base field. Three models of data—the network, hierarchical, and relational models—currently dominate those advanced as bases for data architecture. Comparisons between these models are popular; however a longer range need is for a theory into which each model fits.

The present paper has sought to take a wide view of data, from the perspective of the user. In doing so, perhaps some light has been shed on questions fundamental to a theory of data architecture. In particular, it should now be seen that a theory of data architecture should be based upon an understanding of the human inquirer and of the ways in which data are employed by the inquirer in psychological inference through the use of natural language. It is only in this way that a theory for a modeling of an organization and its information needs is likely to be successfully devised.

## References

[1] J.R. Abrial, Data Semantics, in: Klimbie, J.W. and Koffeman, K.L., eds., Data Base Management, Proceedings of the IFIP TC-2 Working Conference on Data Base Management Systems (North-Holland, Amsterdam, 1974).

[2] H. Biller and E.J. Neuhold, The Semantic Interrelationship of Data Models, 1976 ACM Computer Science Conference, Anaheim, California (February 1976).

[3] Kenneth Boulding, General Systems as a Point of View, in: Mesarovic, Mihajlo D., ed., Views on General Systems Theory (Wiley, 1974).

[4] John Burch Jr. and Felix R. Strater Jr., Information Systems: Theory and Practise (Hamilton Publishing Company, 1974).

[5] R.G. Canning, Trends in Data Management, EDP Analyzer (May, June 1971)

[6] R.G. Canning, The Debate on Data Base Management, EDP Analyzer (March 1972).

[7] Donald D. Chamberlin, Relational Data-Base Management Systems, Computing Surveys, 8, 1 (March 1976).

[8] Ned Chapin, A Deeper Look at Data, Proceedings of the ACM National Conference (1968).

[9] Colin Cherry, On Human Communication (MIT Press, 1957, 1966).

[10] Noam Chomsky. Language and Mind (enlarged edition) (Harcourt Brace Jovanovich, 1972).

[11] C. West Churchman, Suggestive, Predictive, Decisive and Systemic Measurements, 2nd Symposium on Industrial Safety Performance Measurement, National Safety Council (Chicago, December 1968).

[12] C. West Churchman, The Design of Inquiring Systems (Basic Books, 1971).

[13] CODASYL Development Committee, Language Structure Group, An Information Algebra, Phase 1 Report, Communications of the ACM, 5, 4 (April 1962), reprinted in Couger, J. Daniel and Knapp, Robert W., eds., System Analysis Techniques (Wiley, 1974).

[14] CODASYL Systems Committee, Feature Analysis of Generalized Data Base Management Systems (May, 1971). Available from IAG, BCS and ACM.

[15] CODASYL Systems Committee, Introduction to "Feature Analysis of Generalized Data Base Management Systems," Communications of the ACM (May 1971).

[16] E.F. Codd, A Relational Model of Data for Large Shared Data Banks, Communications of the ACM (June 1970).

[17] E.F. Codd, Further Normalization of the Data Base Relational Model, Data Base Systems, Courant Computer Science Symposia 6 (Prentice-Hall, 1971).

[18] E.F. Codd. Recent Investigations in Relational Data Base Systems, Proceedings of the IFIP Congress 1974 (North Holland, 1974).

[19] C.J. Date, An Introduction to Database Systems (Addison-Wesley, 1975).

[20] Jay Earley, On the Semantics of Data Structures, Data Base Systems, Cournat Computer Science Symposia 6, (Prentice-Hall, 1971).

[21] James P. Fry and Edgar H. Sibley, Evolution of Database Management Systems, Computing Surveys, 8, 1 (March 1976).

[22] Joint Guide-Share Data Base Requirements Group, Data Base Management System Requirements (November 1970).

[23] Abraham Kaplan, The Conduct of Inquiry (Chandler Publishing Company, 1969).

[24] Borje Langefors, Information Systems, Information Processing 74, Proceedings of the IFIPS Conference 1974 (North-Holland, 1974).

[25] Richard O. Mason and Ian I. Mitroff, A Program for Research on Management Information Systems, Management Science (January 1973).

[26] George H. Mealy, Another Look at Data, AFIPS Conference Proceedings, Fall Joint Computer Conference (1967).

[27] Ann S. Michaels, Benjamin Mittman and C. Robert Carlson, A Comparison of the Relational and CODASYL Approaches to Data-Base Management, Computing Surveys, 8, 1 (March 1976).

[28] Mario Pei, Invitation to Linguistics (Henry Regnery Company, 1965).

[29] Willard van Orman Quine, Word and Object (MIT Press, 196(1)).

[30] Willard van Orman Quine. Methods of Logic (revised edition) (Holt, Rinchard and Winston, 1964).

[31] M.E. Senko, E.G. Altman, M.M. Astrahan and P.L. Fehder, Data Structures and Accessing Data-Base Systems, IBM Systems Journal, 12, 1 (1973).

[32] Michael E. Senko, Information Systems: Records, Relations, Sets, Entities and Things, Information Systems, 1, 1 (January 1975).

[33] Michael E. Senko, The EDL in the Context of a Multilevel Structured Description: DIAM II with FORAL, in: Douque, B.C.M. and Nijssen, G.M., eds., Data Base Description (North-Holland Publishing Co., Amsterdam, 1975).

[34] Michael E. Senko, Specification of Stored Data Structures and Desired Output Results in DIAM II with FORAL, paper presented at the International Conference on Very Large Data Bases, 1977.

[35] Michael E. Senko, An introduction to FORAL for Users. Version 2, Parts I and II. Basic Information Structure and Basic Query Concepts, IBM Thomas J. Watson Research Center (Yorktown Heights, New York, undated).

[36] R. Clay Sprowls, Management Data Bases (Wiley, 1976).

[37] R.K. Stamper, Logical Data Structures, Data Organization, British Computer Society (1971).

[38] Bo Sundgren, Conceptual Foundation of the Infological Approach to Data Base, in: Klimbie, J.W. and Koffeman, K.L., eds., Data Base Management, Proceedings of the IFIP TC-2 Working Conference on Data Base Management Systems (North-Holland, 1974).

[39] Bo Sundgren, Theory of Data Bases (Petrocelli/Charter, 1975).

[40] Robert W. Taylor, and Randall L. Frank, CODASYL Data-Base Management Systems, Computing Surveys, 8, 1 (March 1976).

[41] D.C. Tsichritzis and F.H. Lechovsky, Hierarchical Data-Base Management: A Survey, Computing Surveys, 8, 1 (March 1976).

[42] P.P. Uhrowczik, Data Dictionary/Directories, IBM Systems Journal, 4 (1973).

[43] Andrew Vazsonyi, Information Systems in Management Science: Semantic Pollution in Information Systems, Interfaces (August 1973).

[44] A.A. Verrijn-Stuart. Information Algebras and Their Uses, Management Datamatics, 4, 5 (1975).

[45] B.L. Whorf, Language, Thought and Reality, Carroll, J.B., ed. (Wiley, 1956).
