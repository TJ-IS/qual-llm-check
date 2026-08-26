---
otero_id: 26291
otero_key: "QV34YAYS"
title: "Depicting the Use and Purpose of Documents to Improve Information Retrieval"
authors: "Michael D. Gordon; Scott A. Moore"
year: "1999"
journal: "Information Systems Research"
doi: "10.1287/isre.10.1.23"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Information Systems Research

## HSR

![](/api/attachments/QV34YAYS/fulltext/images/525563270536e6ccaf6e68be1cae586250dbd7c8300c5a0aa15af6242e2622cc.jpg)

Publication details, including instructions for authors and subscription information: http://pubsonline.informs.org

# Depicting the Use and Purpose of Documents to Improve Information Retrieval

Michael D. Gordon, Scott A. Moore,

To cite this article:

Michael D. Gordon, Scott A. Moore, (1999) Depicting the Use and Purpose of Documents to Improve Information Retrieval. Information Systems Research 10(1):23-37. http://dx.doi.org/10.1287/isre.10.1.23

Full terms and conditions of use: http://pubsonline.informs.org/page/terms-and-conditions

This article may be used only for the purposes of research, teaching, and/or private study. Commercial use or systematic downloading (by robots or other automatic processes) is prohibited without explicit Publisher approval, unless otherwise noted. For more information, contact permissions@informs.org.

The Publisher does not warrant or guarantee the article’s accuracy, completeness, merchantability, fitness for a particular purpose, or non-infringement. Descriptions of, or references to, products or publications, or inclusion of an advertisement in this article, neither constitutes nor implies a guarantee, endorsement, or support of claims made of that product, publication, or service.

© 1999 INFORMS

Please scroll down for article—it is on subsequent pages

![](/api/attachments/QV34YAYS/fulltext/images/b1bd21829cdbe36ed014a69c505d196917e81aed36b19b58c0b92d7fa6a0bc13.jpg)

INFORMS is the largest professional society in the world for professionals in the fields of operations research, managemen science, and analytics.

For more information on INFORMS, its publications, membership, or meetings visit http://www.informs.org

# Depicting the Use and Purpose of Documents to Improve Information Retrieval

Michael D. Gordon • Scott A. Moore

Computer and Information Systems Department, University of Michigan Business School, 701 Tappan, Ann Arbor, Michigan 48109-1234 {mdgordon,samoore}@umich.edu

n this paper we discuss a new kind of information system that helps people be ready for I information work and locate documents. This system differs from a traditional information retrieval system by relying extensively on descriptions of both how a document is used and the purposes it is used for. These descriptions are gathered as the document is electronically used and manipulated (e.g., by a word processor or e-mail system). A formal language represents this information.

(Information Retrieval; Work Flow; Information Acts; Speech Act Theory)

## 1. Introduction

The discipline of information retrieval is focused on locating needed information. After several decades of research, the field has made many advances in both commercial and laboratory settings. Predominantly, these efforts have centered on describing the content of documents, using keywords or other representational systems; to a lesser degree, other efforts have concentrated on a document’s contextual information, such as its author or publisher.

We claim that, in office contexts, document descriptions can be strengthened and retrieval improved by paying attention to how documents are used and what their purposes are. We describe a formal language for describing and capturing such information. By “formal” we mean that the language has a defined syntax and grammar that allows it to be interpreted by a computer. Information about an electronic document’s use and purpose can be systematically and easily gathered, and should improve a person’s ability to find the document when it is heeded. Our work does not address the retrieval of paper documents or documents whose purpose, history of creation, or use are foreign to a searcher.

In §2, we describe the readying problem—the problem of making sure that information workers can effectively locate and make use of the information they require. In §3 and §4, we describe a formal language for describing work, and in §5 we show how this language assists in addressing the readying problem and in improving retrieval. We compare this work with other research in §6 and summarize and discuss our findings in §7.

## 2. Readying

For an information worker, being ready to work takes many forms. For one, before she begins work, an information worker needs relevant information for the problem or assignment at hand. For another, while switching among tasks, she must be able to resume work on those that are suspended or interrupted as effectively and effortlessly as possible. Finally, even after she completes a task, it may be important later for someone (even the original worker) to understand its conclusions, assumptions, sources of evidence, etc. So, being ready to work means locating and making sense of the information necessary for information work— before, during, and after it is conducted. We call this the readying problem. A system that provides this capability is a readying system.

In other words, the readying problem is concerned with how an information worker can eliminate or reduce the overhead and wasteful, nonvalue-adding tasks that surround attempts to find, store, share, and make appropriate use of information. One way to reduce such overhead is through business process reengineering, an activity that often results in task reassignment and work redesign (Hammer and Champy 1993, Harrington 1991). But even after reengineering a worker is never assured of locating needed information. Nor is she assured of uninterrupted work, or of being able to make sense of work already completed.

We contend that two activities can go a long way toward improving the readying problem: recording and documenting.

Recording. Recording means describing the events associated with a document’s use. This means detailing when a document was created, modified, transmitted, and looked at, and who performed these events. Normally, such a history is never officially written down, though a chronology of these events can be useful in identifying needed information (Lamming and Newman 1992). In this paper, we show how recording can be automatically performed and exploited for the purpose of locating documents more effectively.

Documenting. Documenting means describing the associations one has to a document. For instance, a document’s author may annotate it either while writing it or after completing it. Documenting allows people who might later need the document both to locate it more effectively and to recall more easily its origin, use, limitations, context, etc. A worker may anticipate a specific need for a particular document: “I’ll need to have this document at the next Winter Retreat so that I can explain things to the Board.” Or the need may be more serendipitous: “This might be nice to hold on to; I’m just not sure when I’ll need it again.” The more carefully and completely the worker’s mental state in relation to a document can be captured and documented, the more effectively she or others will be able to use that document in the future. Even the author of a document who resumes work on it after a considerable interruption may find she is unable to do so effectively unless she can recapture her thought processes while she was last working on it. Documenting can be as simple as using a designated folder for a project or can involve more elaborate means of making a document’s context evident. Recording can even be considered a form of documentation if the resultant records remind a worker of people or events associated with a document.

Locating documents and making effective use of them (in terms of recognizing their impact, context, limitations, etc.) are the reasons for recording and documenting. Locating and making effective use of information can support activities deemed vital to the firm (“Find me all the information relevant to the decision to build the new manufacturing plant.”), or far more pedestrian. Generally, what is common to most attempts to locate information is that much needed information is out of file, not locateable, incomplete, or somehow different than what one had imagined; finding the information one truly requires can occupy up to 25 percent of one’s day (Gordon 1997). Still, even though being able to easily locate needed information can greatly reduce the wasteful, nonvalue-adding efforts that beset information workers, most rarely make a concerted effort to document or record. They consider these tasks peripheral to their main responsibilities. But, just as a building contractor attends to the “small task” of the timely delivery of mortar—to keep from delaying the mason and thus the plumbers and electricians, finally causing a project to miss its deadline—information workers benefit when attention is paid to the small tasks of recording and documenting by recapturing some of their lost ten hours per week.

In the next section, we describe the bases of a computer-processable language that is used to record and document information work. The focus of the language is on the small tasks common to all information workers whether clerk, loan officer, bank vice president, or professor—creating documents, editing them, transmitting them, etc. Because these small activities can be described independently of what each profession uses documents for, a common language can be used to record and document work. Since this information can be automatically captured, simply doing work provides a basis for improved retrieval. We provide examples of this significant result in §5.

## 3. Foundations of a Readying System

A readying system is system-level software that interacts with application software and other system software. Much of the time a readying system works unobtrusively, recording the actions of users as they use word processors, e-mail systems, fax machines, printers, and other office equipment and applications. Work conducted manually and information that cannot be stored on a computer lie outside of our interest in readying systems.

A readying system can also perform various information tasks including: creating, sending, or storing documents; responding to requests for information; and reminding one of deadlines or appointments. It does some of these activities automatically (for example, responding to a request for information similarly to the way an edi system might automatically respond to a request for a price quotation). It partially automates others, relieving an information worker of certain responsibilities better suited to a computer, but not totally absolving her. In this sense a readying system is similar to office automation (e.g., Malone et al. 1993, Mora et al. 1992, Sohlenkamp and Chwelos 1994) or work flow systems (e.g., Radosevich 1995, Trammell 1996, Wilson 1994).

In either case, as well as when an individual is simply using a computer without receiving any apparent support from her readying system, a readying system records and documents the work she is doing. In this paper, our primary aim is to show how a readying system offers a new form of information retrieval based on its ability to record and document, and we pay less attention to the way the system provides some level of automation.

Next, we describe the theoretical concepts that are the basis for a readying system.

## 3.1. Information Acts

A readying system is based on a computer-processable or formal language for information work. The language’s fundamental construct is an information act— an action that can be performed on or with a document or some other information object. Information acts can describe a document’s use, its purpose, and how it has been annotated. Table 1 lists the first two levels of an information act hierarchy. Except for more detailed actions that cannot be shown in just two levels, it describes the full set of actions that can be performed on documents. As a rule, an information act should be decomposed into more specialized acts only when these subacts are useful for later retrieval. Other typologies might do the same even though they include different acts, different numbers of levels, or different specialized acts. As we will see, information acts form the basis of our system’s recording mechanism.

The first type of information act shown in Table 1, use acts, describes various acts involved in composing and examining a document. The create and destroy acts denote the creation and deletion of a document. Open and close denote opening and closing a document for the purpose of either modifying or reading it. Beginchange denotes that the document is no longer merely open—some change has been made to it. When these changes are committed to long term storage, a commitchange act occurs. A retrieve denotes retrieving a document from an information base. Finally, a move denotes moving a document from one “place” (electronic or otherwise) to another. Each information act in Table 1 will have more specialized cases, possibly several levels deeper than shown. For instance, create has create-email-doc and create-wordprocessor-doc as two of its specializations at the next level. A readying system can detect and capture each of these information acts (including annotative and documentary acts which we discuss next) in a database as an information worker uses her computer for e-mail, word processing, looking for files, etc. For instance, a Save command in a word processor would be represented by a commit-change.

Table 1 Information Acts Classified by Type—Top Two Levels

<table><tr><td>Types</td><td>Acts</td></tr><tr><td>Use acts</td><td>Create, open, begin-change, commit-change, close, destroy, retrieve, move</td></tr><tr><td>Annotative acts</td><td>Link, make-note</td></tr><tr><td>Documentary acts</td><td>Send, receive</td></tr></table>

Sequences of use acts more fully describe how a document is composed and examined. For instance, a completed first draft of a document written in two editing sessions might be recorded as follows (with details deferred until §4): create-wordprocessor-doc; open; beginchange; commit-change; begin-change; commit-change; close; open; begin-change; commit-change; close; open; close.

Annotative acts are a second type of information act. They describe the acts involved in documenting work (i.e., keeping track of mental associations to documents). Two specializations of this type of information act are the following: link, which creates a pointer that suggests that one document refers to another; and makenote, which is a note on a document written to ensure that the document will be better understood and more useful.

A third type of information act is a documentary act. A documentary act is a communication act involved in sending or receiving a document. Documentary acts are analogous to speech acts. Speech act theory, a linguistic theory originally developed by Austin (1975), states that when people say something (with words), they are actually doing something as well. Examples of this phenomenon are the sentences “I now pronounce you husband and wife,” and “I find the defendant not guilty.” In both cases saying so makes it so. Documentary acts are an analogous concept in our theory, where our focus is on what people can do with documents. So, while Austin used the phrase speech act to mean “doing something with words,” we coin the phrase documentary act to mean “doing something with documents.” In speech act theory, speech acts take effect only when a speaker says something, and a listener hears it. Analogously in our theory, we suggest that documents “do something” only when they are sent to one (or many) “listeners.” Broadcasting refers to sending a message to two or more recipients. The receive documentary act is the act that occurs when the recipient receives the send documentary act.

Austin argued that there are many different kinds of speech acts, which differ based on their illocutionary force. This force defines the utterance’s function or purpose—that is, what the utterance is supposed to accomplish. A speech act has the structure F(P), where F is its illocutionary force and P is the proposition it is applied to. For example, the utterance “Is it raining?” is a speech act with an illocutionary force of question and a proposition that it is raining.

Austin proposed a typology of illocutionary forces. Speech act theorists propose that, no matter what a person says, the statement can be meaningfully classified by a speech act typology, thereby equating innumerable sentences according to their illocutionary force—that is, according to their function. For present purposes we wish to describe a document’s function when it is sent. When a user (or the readying system) performs a documentary act, she (or it) must pick the appropriate force, F, and supply the proposition, P. We discuss this process later.

We use the following illocutionary forces: confirm, inform, offer, permit, predict, promise, question, require, and retract. This list is a subset of those proposed by Bach and Harnish (1979) that Moore (1996) found sufficient to handle many business transactions. Others (e.g., Ballmer et al. 1981 or Searle et al. 1985) have devised their own typologies. We can add forces if the need arises to make our typology more expressive though Moore’s work suggests this should not be necessary.

Collectively, the speech acts that we use express many of the things one can do by sending a document. For instance, a document may inform its recipient about some new development. It may retract (or confirm) ideas previously presented. It may predict some future state of affairs or present a question that needs addressing. Documents can also have more official functions: they may require that something occur, promise that something will occur, permit something to occur, or make an offer.

As with information acts, speech acts can be specialized in many different ways. For instance, “to remind” is a specialization of the speech act “to inform” that depends on the hearer already knowing what she is being told. “To allocate” is a specialization of “to promise” where the promise concerns a scarce resource.

To summarize what we have said in this section: We have introduced the idea of information acts—which we view as the smallest meaningful unit of description of how documents are used. Information acts describe 1) the ordinary things one does with a document (use acts); 2) the activities that take place as a worker attempts to make permanent certain associations she has to a document (annotative acts); and 3) the purposes documents are used for when they are transmitted to others (documentary acts). Information act descriptions of documents can supplement keywords or other types of descriptions that attempt to explain what a document is about.

A readying system unobtrusively records a worker’s actions as if it were a camera with a special lens that only detects information acts. The readying system “camera” will record each type of information act. Jumping ahead, some quick examples show how information acts can be useful in information retrieval. Responding to the query “It’s the document I received from Sue just before I received the new strategic direction from Joe” depends on recording what one is doing with a document and when (use acts). Responding to the query “It’s the document in which I requested that Sue be transferred” depends on keeping track of documentary acts, which record via speech acts a document’s purpose (here, a request). And the query “It’s a document that I annotated as contradicting the 3rd Quarter salary data” depends on annotative acts. We give fuller attention to such queries in §5.

## 3.2. Work Processes

Meaningful work involves many individual information acts, each of which contributes to the same end. We call such sequences, or such compositions, of information acts work processes. Work processes are “chunks” of work that, in many situations, make more sense or, certainly, provide a more complete view of work than do isolated information acts. Work processes have two related roles in a readying system, 1) as a “program,” which describes how to do work, and 2) as a record of what work has been done.

We use statecharts (Harel 1987) as the external representation of work processes that is visible to users of a readying system. (Internally, we represent the same information by a set of equivalent Prolog statements.) Statecharts are comprehensible to people and allow them to construct or to examine work processes. In the following examples, we show how statecharts serve both roles.

Figure 1 is an example of a statechart that can be used as a program. This work process is called travel arrangements and helps a worker get the paperwork done for a business trip. This program is invoked when a person expresses a desire to travel (say, by making the appropriate selection from a menu), thus causing the desire to travel condition to become true. Every program has a similar entry condition on the outside that determines when the program should be executed. The travel arrangements work process consists of two separate processes that are executed concurrently: the travel request process and the cash advance request process. A statechart indicates concurrency with a dotted line dividing a rectangle.

As its name suggests, a statechart depicts a sequence of states (indicated by rounded rectangles). The arrows entering a state indicate when a transition should be made into that state from another. An arrow that begins with a black circle shows the default starting point for a process. In this case, since there are two concurrent processes, there are two starting states, both called write the msg, that are entered at the same time.

Consider the arrow at the beginning of the travel request process—it has /create-email-doc below it which indicates that the system should execute the action called createemail-doc. Notice that create-email-doc, like other actions labeling transition arcs, is a specific instance of an information act from Table 1—in this case, the act (one of the use acts).

Figure 1 A Statechart Representation of a Work Process  
![](/api/attachments/QV34YAYS/fulltext/images/61e4e3c64a01c98909e520444179616e2686dbcbc84943caafc82a1946715344.jpg)

The complete format of a transition label from state A to state Z is if c / b, which is interpreted as follows: “The process will go from state A to state Z when occurs and if $\gamma$ is true. If this transition takes place, then, simultaneously, the program will execute $\beta . { ^ \prime \prime }$ Each part of this label is optional. (As a notational convention, the $i f$ is used only when there is a c part of a label and the $^ { \prime \prime } / ^ { \prime \prime }$ is used only when there is a b-part of a label.) In the case of the label /create-email-doc, the system automatically takes the transition since there is no condition on it and executes the create-email-doc act.

Information acts make up the and b parts of the transition label while predicates that reflect a condition like the number of documents in an individual’s electronic in-box or some state of the environment make up the c-part. A transition with an information act in its b-part (e.g., /create-email-doc) represents an information act that a readying system automatically performs as a side effect when the if c condition on that transition is satisfied. The if c part of the transition acts as a sentinel, keeping the system from changing state. Once the act is performed by either the worker (because she has the information, time, and wherewithal to perform the act) or the readying system (because it was triggered by some other event), the process will move to a new state if $\gamma$ is true.

Returning to our example in Figure 1, in the write the msg state the worker is inserting text into the document. As the transition label from this state indicates, the system will leave this state when the user performs the send-email documentary act.

An important point about statecharts is revealed by the write the msg state (details shown in Figure 2); namely, writing the message may be done in one or more editing sessions, and it may be performed by typing, copying text from another document, or in other ways—we cannot tell from the statechart in this figure. Accordingly, there may be many individual information acts associated with the write the msg state that are not portrayed in the travel arrangements statechart. In fact, this virtue of statecharts—their ability to show details at various level of abstraction, even within a single diagram—motivated us to use them to represent work processes.

To complete our example, at the same time the system begins the travel request process, it also begins the cash advance request process. This process has the same structure as the travel request process but involves a different document that performs a different function.

Remember that there is a second role of work processes—as a record of work that has been performed. As work is completed, with or without some level of automated support from a readying system, the appropriate information acts are recorded. For example, Figure 3 shows a partially completed work process. As depicted, this figure looks very similar to a statechart that is used as a program. In actuality, it differs in two important ways: First, it is incrementally composed, on-the-fly, as work is performed; in contrast, statecharts used as programs are composed in advance. For instance, in Figure 3 where travel arrangements are being made for a trip to Chicago, the travel request has been sent (since the current state in travel request is travel req with boss) but the cash advance message is still being composed (since the current state in cash advance request is write the msg). Second, a statechart used as a record contains much detail about the actions that were performed: who performed them, when they were performed, etc. These important details will be presented in §4.

Figure 2 The “Write the Msg” Work Process  
![](/api/attachments/QV34YAYS/fulltext/images/fd75d57f64e3fe8a7aea93ad5da90d39e35de8f399e97b353a0151393e83db4e.jpg)

Figure 3 A Statechart Representation of a Partially Completed Work Process  
![](/api/attachments/QV34YAYS/fulltext/images/91be393912a063c06f2ca307218e7169bd26baa81bbd0812e423a60813b21d43.jpg)

Not all work with documents fits into a predefined work process. But all information acts associated with all documents are still recorded by a readying system. Every time a worker creates, adds text to, edits, opens, closes, or sends a document, those information acts are recorded, even when they take place outside a programmed work process. In such situations a state chart representation links together information acts chronologically.

Figure 4 summarizes the interrelationship between people and work processes. While doing work that involves documents, a worker will perform information acts. These actions might either 1) activate some work process program which can, in turn, perform some other information act or 2) remind a worker to perform another information act. The readying system will create a record whenever an information act is performed. A worker may document (via annotative acts) any documents she has worked with. Subsequently, what is recorded and documented can improve a worker’s ability to locate needed information.

Figure 4 Relations Among Uses of Information Acts  
![](/api/attachments/QV34YAYS/fulltext/images/c5ea689b0173f582a27072ae3937d999dec890779a93c6c73b7e7b915fa3ba6e.jpg)

## 3.3. Information Objects

Implicitly, we have been referring to documents that contain text throughout this paper. But there is nothing special about text in what we are describing. To make this point clear, what we have said so far—as well as all that follows—pertains to any information object. By this term we usually mean ordinary documents such as memos, meeting minutes, reports, and letters; but we can also mean drawings, scanned images, or anything else stored on a computer. That is, information objects generalize the concept of text-only documents, and are “documents” in the broadest sense of the term.

An information object has content and a context. The content of a document is the subject material it specifically expresses. For drawings, images, and other nontext information objects, the content is analogously defined. Context includes information describing the document that is not part of its content proper. For instance, the content of meeting minutes is what was written in that document. Its contextual description includes the document’s author, the meeting time, the meeting location, the attendees, the leader of the meeting, the financial position of the company at that time, the news of the day, etc. The context also includes information about work: what project is the meeting part of, who called the meeting, what event precipitated the meeting, what resulted from the meeting, etc.

Content descriptions (exemplified by keywords) are based on human perceptions (which can vary widely among users) and are subject to linguistic problems surrounding synonyms, homonyms, polysemy, etc. On the other hand, contextual descriptions are based on facts, and so can be advantageous for identifying and retrieving documents or other information objects. As we will discuss in the following section, we have defined a detailed description of how information acts should be recorded so that some of this contextual information is automatically captured whenever information work is done. It is straightforward to modify or extend what can be recorded to include other contextual information, if that new contextual information’s usefulness for retrieval is deemed greater than its difficulty to capture.

## 4. Recording Work with Information Acts

A simile we used before to describe a readying system was that it records office work as would a camera with a special lens that only perceives information acts. We have mentioned that much detailed information is recorded that we did not portray in our statechart representation. Here we explain these details.

As a point of emphasis, remember that the transitions in any statechart are of the same structure: each contains an information act or other observable conditions. The states within a statechart will vary dramatically, of course, from work process to work process. So, a technical, legal work process, for example, will not have a travel req with boss state as would as would a travel work process, but will have states appropriate to some aspect of technical, legal work. Still, all work processes are built from the same information act building blocks. In this way, we have a descriptive language capable of describing any kind of document used in any kind of information work. It is precisely this fact that we exploit for retrieval.

## 4.1. A Grammar for Work

A readying system records much information about an information act by adhering to a context-free grammar expressed in BNF. By recording information acts with this grammar, it is possible for a retrieval system to parse them (and their compositions as statecharts) and so use them to locate documents more effectively. The grammar for information acts is shown in Figure 5.

In the first rule of the BNF, an information act (infoAct) is defined as an actor performing a certain information act (theAct) within a context (iaContext). The last symbol in the definition (iaID) is the identifier for the information act. As shown in the second rule, theAct is allowed to take on one of three possible values: use acts, annotative acts, and documentary acts. These are the three types of information acts previously shown in Table 1. The next three rules define the specifics for each type of information act.

As explained in §3.1, documentary acts include a speech act (rules 5, 8, 9). Recall that a speech act’s structure is F(P), where P is the argument of the illocutionary force F (see rule 10). The list of forces associated with a speech act (see rule 12) are those listed in §3.1.

## Figure 5 Partial BNF Representation for Recorded Information Acts

```txt
1. infoAct ::= "infoAct(" actor "," theAct "," iaContext "," iaID ")
2. theAct ::= useAct | annotativeAct | documentaryAct
3. useAct ::= createAct | ("open(" docID "," application_name ")") | beginChange | ("commit_change(" docID ")") | ("close(" docID ")") | ("destroy(" docID ")") | ("retrieve(" docID ")")
4. annotativeAct ::= ("link(" docID "," docID ")") | ("make_note(" docID "," plain Text ")")
5. documentaryAct ::= send | receive
6. createAct ::= ("create_e_mail_doc(" docID ")") | ("create_wordprocessor_doc(" docID ")")
7. beginChange ::= ("begin_typing(" docID ")") | ("copy_change(" from "," to ")")
8. send ::= ("send_e_mail(" recipient "," speechAct "," docID ")") | ("send_fax(" recipient "," speechAct "," docID ")")
9. receive ::= ("receive_fax(" sender "," speechAct "," docID ")") | ("receive_e_mail(" sender "," speechAct "," docID ")")
10. speechAct ::= ("speech_act([" 1#("sa(" force "," content ")") ])") | ("speech_act([" 1#("sa(" force "," contentDesc ")") ";b," docID ")") | ("speech_act([" 1#(force "(null)") " ], "docID ")")
11. iaContext ::= "[" #( ("process_id(" processID ")") | ("time_of_act(" timePred ")") | ("respond_to(" iaID ")") | ("step(" stepID ")") | ("project(" projectID ")")) ]"
12. force ::= "inform" | "retract" | "predict" | "confirm" | "question" | "require" | "permit" | "promise" | "offer"
13. recipient ::= actor
14. sender ::= actor
15. actor ::= personID | ("actor(" (personID | "system") "," personID ")")
```

Missing terms (e.g., timePred) are defined in a straight-forward manner. We have limited our presentation to those terms necessary to understand the basic structure of the language.

The augmented BNF used in this definition is in common use on the Web and is defined in RFC 822 (which can be found at http://ds2.internic.net/rfc/ rfc822.txt). Literals are surrounded by quotes while terms are not. The bar (| ) means “or” while the square brackets indicate optionality. Elements enclosed in parentheses should be treated as a single element. A pound sign (#) is used to indicate a list of terms; thus, 1#(person) indicates a list of 1 or more persons.

The illocutionary force, P, used with a speech act (rule 10) defines speech acts of two main types. First, the speech act can be a fully computer-processable message that does not refer to any external document; a simple example is

```erlang
(1) infoAct(molly,
    send_e_mail(lindsey,
    speech_act([sa(inform,
    snow(city(ann_arbor, mi, usa),
    time("03:30:00p on May-12-1966"))]), 
    none),
    [time_of_act("03:33:13p on May-12-1966"), 
    i21)
```

This is an e-mail message from molly to lindsey in which molly is informing lindsey that it is snowing in Ann Arbor at 3:30pm on May 12. The corresponding receive act would be

(2) infoAct(lindsey,

```txt
(4) infoAct(molly,
    send_e_mail(lindsey,
    speech_act([inform(null)]),
    d32),
    [time_of_act("03:33:15p on May-12-1966"), i23)
```

receive\_e\_mail(molly, speech\_act(. . . , none), [time\_of\_act(“03:33:27p on May-12-1966”)], i96)

The system constructs this act directly from the send\_email act. Such formal messages, which use predefined predicates, are especially useful for allowing work process programs to parse and automatically respond to incoming messages.

The other type of speech act refers to accompanying documents. Examples of the three forms of this type follow. If a person were to send a document about the weather in Ann Arbor to another person, this speech act would look something like

(3) infoAct(molly, send(lindsey, speech\_act([sa(inform, weather)]), d32), [time\_of\_act(“03:33:14p on May-12-1966”)], i22)

This is a simpler message than in (1), using free-text for the argument of inform, but it is less informative. It tells the recipient that the purpose of document d32 is to inform about the weather. The message sender could also substitute sa(inform, “It is snowing”) for sa(inform, weather). Finally, the third form of this type of speech act is even less informative; it merely tells the recipient what illocutionary force(s) the document carries. An example of this type of message is

Though these types of speech acts vary in their specificity, each can be useful for retrieval as we will see in §5.4.

Different readying systems might be based on a slightly different grammar. For instance, in Figure 5 the iaContext term only includes the work process associated with the information act, the timing of the act, the information act that this information act is a response to, the particular step of a work process the act is associated with, and the project associated with the information act. We have chosen these items on the assumption that they will often facilitate retrieval. Similarly, the speech act typology we have used in Table 1 (which makes up the force term in Figure 5) could be replaced by another typology; and other information acts could be produced by different production rules. For different types of work environments, these changes might make a readying system more useful and retrieval more effective.

## 5. Improving Information Retrieval

In this section, we show how recording information acts can improve information retrieval. In doing so, we will also illustrate some of the details about recorded information acts, as well as how work processes used as programs provide some level of work automation. We have an evolving prototype that implements some of these features.

## 5.1. Retrieval Based on Facts

As we just saw, for any information act some contextual information is recorded, including the actor (the person performing the act) and the time of the act. Recording these contextual facts in a formal way in a database allows certain elementary, fact-based questions to be answered by a query against the database.

The examples we use in this section show off the capabilities of a readying system using questions that are reasonable to ask with it. Further research must be carried out to determine if these are, in fact, the kinds of questions that users would actually pose.

For instance, to answer the question “Which documents did Phil create?”, a searcher would issue the formal query

(5) Find DocID where

infoAct(actor 4 phil,

theAct 4 create(DocID))

(The clauses within the infoAct term restrict the information acts that might ultimately match the query.) The retrieval system would then consult its database of information acts to find matching information acts, such as

(6) infoAct(phil,

create(d72),

[time\_of\_act(“11:42:16a on Oct-10-1966”)],

This information act can be interpreted as “Phil created document d72 at 11:42:16a on October 10, 1966. The identifier for this act is i35.” The complete answer to the query would be a set of document identifiers (DocID) gathered from information acts in which Phil creates a document; this set would include document d72. Questions like “Which documents did Phil create in August, 1996?” and “Which documents were created in August, 1996?” could be just as easily answered.<sup>1</sup>

Ordinary file systems can answer some of these questions, also, though not necessarily easily. However, since we record with information acts all actions on documents, we can directly answer questions that few other systems could. For instance, “Which documents have been written or revised on the system by two or more people?” is answered by finding any documents that have at least two commit\_change information acts performed by different people:

```erlang
(7) Find Doc where
    infoAct(theAct = commit_change(Doc),
    actor = P1),
    infoAct(theAct = commit_change(Doc),
    actor = P2),
    P1 ≠ P2
```

Even more difficult (and likely impossible) for most other systems to respond to would be a question like “Who has seen the document that Dennis wrote on January 1, 1981?” From the database of recorded information acts, we simply find the actors in the open information acts (as specified below) that satisfy the following compound query:

```python
(8) Find P where
    infoAct(actor = dennis,
    theAct = create_wordprocessor_doc(Doc),
    date_of_act = "Jan-01-1981"),
    infoAct(actor = P,
    theAct = open(document = Doc))
```

This query finds the people P who have performed the information act open on any document Doc that was created by Dennis on January 1, 1981. Of course, if Dennis created more than one document on that date, we would need to restrict the create information act further if we wished to find out about a specific document. Questions similar to these can be especially useful in identifying a document known to have been seen by certain individuals.

Information acts may also directly record that one document is related to another. For instance, suppose that Mackenzie reads document d25 from Hannah and thinks that it is related to the Oracle document d6. Mackenzie can manually link these two documents, thus producing the information act:

```txt
(9) infoAct(mackenzie link(d6, d25), ..., i41)
```

To find documents that have been manually linked to document d6 we submit the following query:

```txt
(10) Find Doc where infoAct(theAct = link(d6, Doc))
```

“Chains” of linked documents can be useful for uncovering associated information that is not contained within a single document. Such chains can be found by retrieving a given document plus all others that are transitively linked to or from it by either link or make notes information acts. Similar capability is generally unavailable in traditional file systems.

The system is also capable of inferring links when they are implicit, such as when a message is composed in response to another message. For example, suppose that Mackenzie’s system records the following information act signifying that it received a question via email from Hannah:

```erlang
(11) infoAct(mackenzie,
    receive_e_mail(hannah,
    speech_act([question(null)]),
    d25),
    [project(kennedy),
    process(define_project),
    step(set_requirements),
    time_of_act("03:06:58 on Oct-26-1966")]), i36)
```

Mackenzie’s system could automatically create a document that would be completed by Mackenzie. The system could ensure that any contextual information associated with the act in (11)—and, hence, with document d25 referred to within that act—is automatically associated with the document created in response to that act. At a basic level, this means that the act that automatically creates the document contains a respond\_to predicate:

```erlang
(12) infoAct(actor(system, mackenzie), create_e_mail(d73), [respond_to(d25), ...], i37)
```

This effectively establishes a link between d25 and d73. But, more interestingly, any information about the original e-mail (such as its project) can be incorporated into the automatically composed response. Thus, the previous information act might actually look like:

```txt
(13) infoAct(actor(system, mackenzie), create_e_mail(d73), [respond_to(d25), time_of_act("03:07:15p on Oct-26-1966"), project(kennedy), process(define_project), step(set_requirements)], i37)
```

The advantage here, of course, is that we can easily create ad hoc conceptual categories, like the “Kennedy project” or the “define\_project process,” and then find “linked” documents that are elements of such categories.

Another form of retrieval based on facts comes from having knowledge about software packages. For example, the question, “Where is the word processing document that contains information copied from a graphics package?,” might be asked as follows:

```txt
(14) Find Doc where
    infoAct(theAct = create_wordprocessor_doc(Doc)),
    infoAct(theAct = create_graphics_doc(Doc2)),
    infoAct(theAct = copy_change(Doc2, Doc))
```

```python
(15) infoAct(hank,
    make_note(d22, "Need Don's input before continuing."), 
    [time_of_act("03:01:22 on Oct-26-1966"), 
    i35)
```

we can answer questions like “Where is the document Joe wrote but that Hank annotated?”:

```erlang
(16) Find Doc where
    infoAct(actor = joe,
    theAct = create_wordprocessor_doc(document = Doc)),
    infoAct(actor = hank,
    theAct = make_note(document = Doc))
```

Similarly, whenever one is working with a document and hopes to remember some of its broad, underlying context, one can ask to see all the annotations that have been associated with it.

## 5.2. Retrieval Based on Timing Relationships

Dates and times are sprinkled throughout our examples. Sometimes, by means of deductive inference, timing relationships can be the key to describing the information one wants to retrieve. For instance, consider the need for information expressed by

Find the document Maria wrote about the Kennedy project. Kathryn received it just before the ‘Right sizing’ document was broadcast by Joe to all employees.

A query that would find this would be:

```erlang
(17) Find Doc where
    infoAct(actor = maria,
    theAct = create_wordprocessor_doc(Doc)),
    infoAct(actor = kathryn,
    theAct = receive(Doc),
    date_of_act = Date1,
    project(kennedy) in iaContext),
    infoAct(actor = joe,
    theAct = send_e_mail(recipient = all_employees,
    document = Doc2),
    date_of_act = Date2),
    Date2 - Date1 ≤ i-day,
    "right sizing" in subject(Doc2)
```

The success of our method hinges on the fact that our system records the dates and actors of the relevant information acts and can link these with the facts about documents (as exemplified by the last two lines in (17)).

Another form of question one might raise—and one which also relies on deductive inference other systems are unable to support—is “I (Leigh) am looking for the document I was writing about the Nooton project that I revised again and again until I liked it.” A suitable query would examine each document that was part of the Nooton project. It would count the number of times each document was revised, and present them to the inquirer sorted on that basis:

```erlang
(18) Find Doc, Count where
    infoAct(actor = leigh,
    theAct = create_wordprocessor_doc(Doc),
    project(nooton) in iaContext),
    Count = count(infoAct(actor = leigh,
    theAct = commit_change(Doc)))
    sorted by Count
```

## 5.3. Retrieval Based on a Hierarchy of Information Acts

In §3.1 we mentioned that information acts are organized hierarchically. This provides an opportunity for flexible retrieval, because we can ask for documents in a specific way and still retrieve them even if certain details are inaccurate. For instance, “Find the faxes that David received from Anne” would be specified by the query:

(19) Find Doc where

```txt
infoAct(actor = david,
theAct = receive_fax(actor = anne, document = Doc))
```

(This assumes that faxes are retrieved over computer fax-modems and therefore recorded by information acts.) If the system determines that David received no faxes from Anne, it can reason that receiving by fax and receiving by e-mail are both specializations of the receive information act, and so look for documents David received from Anne by e-mail instead of fax. The details about how a particular querying system performs partial matching by generalizing or specializing information acts are not important here.

## 5.4. Retrieval Based on Speech Acts

Recall that illocutionary forces are associated with any documentary act (an information act in which one tries to do something with a document by sending it). By recording these “purposes” for transmitting documents, new kinds of retrieval are possible. For instance, the question “Where is the request that Hannah sent to Mackenzie in October?” specifically relies on the fact that the document being sought was making a request (rather than having another illocutionary force). Documents with the right sender, recipient, and illocutionary force will be retrieved.

Multi-document exchanges of information can also be identified, based on illocutionary forces. For instance, consider

Where is the document Hannah faxed Mackenzie? It was a confirmation of a question Mackenzie e-mailed her about being able to hire a new contractor. Find the original question, too.

The document sought (a fax) will have a force of confirm and a respond\_to condition that associates it with a question Mackenzie raised by e-mail. The relevant query would be the following:

```python
(20) Find Doc1, Doc2 where
    infoAct(actor = mackenzie,
    theAct = send_e_mail(actor = hannah,
    question in speechAct,
    document = Doc1)),
    infoAct(actor = hannah,
    theAct = send_fax(actor = mackenzie,
    confirm in speechAct,
    document = Doc2),
    respond_to(Doc1) in iaContext)
```

Illocutionary forces are arranged hierarchically. We suggest a base set of forces (listed in §3.1) that have proven effective thus far (Moore 1995). But, each of these forces can be extended in many different ways so that they become the “parents” of more specialized forces. For instance, an illocutionary force of permit may have these specializations: approve, regulate, or authorize. To offer may be specialized by to quote (as in to quote a price) or by to suggest. An illocutionary force attached to a documentary act may be either a base force or a more specialized force. In general, users of a readying system must provide the appropriate force (since only they understand a document’s purpose). The only exception is when the readying system is engaged in a completely formal conversation, like responding formulaically with an offer to a formal request for a price quotation.

As with information acts, the hierarchical organization of illocutionary forces provides benefits for retrieval. For instance, in the database of recorded information acts might be

(21) . . .send\_e\_mail( . . .sa(inform, “new vacation schedule” . . .) . . .

Inform is a base illocutionary force (by our categorization), and remind is a specialization of informing in the sense that one is informed about something again. So, a question “Find the reminder that was sent about the new vacation schedule” could uncover documents (like the one sent in (21)) informing (not reminding) about the vacation schedule. Again, the details about how a particular querying system performs partial matching by generalizing or specializing are not important here.

Finally, each of the various types of propositions we associate with illocutionary forces may provide some advantage for retrieval. Recalling an example we used earlier, each of the following is an acceptable example of a force applied to a proposition: inform(rain(city(ann\_arbor, mi, usa), time(“03:30:02p on May-12-66”))), inform(“It is raining”), inform(weather), and inform(null). Whereas full propositions (like “it is raining”) are most descriptive about the purpose of a document, a content fragment (weather), or a null proposition may be useful for retrieval, too. The query “Find documents informing Joe that it is raining” would find a document associated with the second speech act:

(22) Find Doc where

infoAct(actor 4 joe,

theAct 4 receive\_e\_mail(document 4 Doc,

The query “Find documents informing Joe about the weather” would find the a document associated with the third speech act:

(23) Find Doc where

Neither query, however, would find both such documents, since we don’t employ any semantic devices that relate rain to weather, for instance. (This could be done at the expense of further complicating the system—but it is not our focus.) The usefulness of a speech act characterization of document usage is that we can distinguish documents making, say, requests, about the weather from those that inform us about the weather. An inquirer (Diane) may even wish to view all the e-mail messages that make a request of her, which she would do as follows:

(24) Find Doc where infoAct(actor 4 diane, theAct 4 receive\_e\_mail(document 4 Doc, request in speechAct)).

5.5. Retrieval Involving Work Processes and Work Documents can also be located according to their association with work process programs. For instance, to find out what documents are involved in making travel arrangements, one would inspect the travel arrangements statechart (shown in Figure 1). From this, it is immediately seen that the appropriate documents are two types of e-mail messages: the travel request per se, and the request for a cash advance. A readying system’s knowledge about work process programs permits another type of query that compares expected and actual behavior. For example, the question “What work process is incomplete because Joe hasn’t finished the paperwork?” would, implicitly, compare the record in Figure 3 (assumed to be describing Joe’s work) with the work process program in Figure 1. The record (Figure 3) would indicate that the cash advance was created but never sent to the boss (as Figure 3 would require for the entire travel arrangements process to be completed).

## 6. Other Research

There are many articles on office automation systems which take a variety of approaches to supporting information work: a problem oriented approach Woo and Lochovsky (1987), a procedure oriented approach Croft and Lefkowitz (1988), or even a knowledge based approach Tueni, Li, and Fares (1988). Similarly, there is a huge information retrieval literature. However, the intersection of these two bodies of literature, which are the bases for our work, is small.

Celentano et al. (1991, 1993) proposed a system for retrieving documents based on their uses and roles. A chief characteristic of this work is the need to specify in advance a document’s use (who will prepare it, review it, etc.) and any special circumstances that pertain to it (for instance that a special letter of authorization is required only when a loan is at least \$100,000). Retrieval of documents whose use or roles cannot be specified in advance lie outside the scope of this system.

Work done by Lamming and Newman (1992) and Lamming and Flynn (1994) also attempts to retrieve documents based on the activities they are involved in. These efforts attempt to provide complete, detailed activity logs for people, documents, office equipment, etc. For instance, the whereabouts of people wearing active badges that emit infrared signals are continually tracked throughout the day. Similarly, individual stylus-strokes on Personal Digital Assistants are recorded and time stamped. Later, these details are analyzed in an attempt to portray larger, more meaningful episodes of activity.

Our work thus falls somewhere between Lamming’s and Celentano’s: We use information acts as primitive actions on documents that, nonetheless, provide more meaningful descriptions of work than stylus-strokes or other very specific actions. On the other hand, information acts can be recorded and examined outside of predefined patterns of use (though they may also be examined as part of work process programs when required).

Finally, speech act theory and other theories of communications have been proposed as ways to describe office transactions (Au¨ ramaki et al. (1988), Winograd and Flores (1986). Primarily, these works try to describe the commitments and obligations inherent in office work, rather than providing any application to information retrieval. However, a recent series of articles in Computer Supported Cooperative Work contain a debate on the appropriateness of using speech act theory as a foundation for system design (see Suchman (1994) and Winograd (1994) for the original articles, Agre (1995) et al. for responses to these two articles, and Suchman (1995) for a rebuttal). Suchman’s position is that speech act theory does not capture all the nuances of human communication and, further, that its categorization of messages is a form of organizational control over system users. Our position is a moderate, though optimistic, one: We agree that speech act theory does not capture all the nuances of human communication; however, we believe that it does capture some dimensions that can be useful (for information retrieval in our case). We also support Winograd’s point that if a user feels that his or her message cannot be conveyed effectively by a system, other communication avenues are always available (e.g., phone, faceto-face meetings)—though, of course, this would mean that these communications would not be available for later retrieval using the system as we have described it. We are betting that the benefit of having a system that can help solve the information retrieval problem would outweigh in many cases the costs of subjecting a communication to the categories imposed by speech act theory.

## 7. Summary and Discussion

We have defined a new type of information system in this paper: a readying system, which makes an information worker ready to do work. We claim that information workers from all professions work with documents in similar ways, and that a readying system can help them automate certain behaviors and also find the information they need to do their work. Certain types of work should find immediate benefit from a readying system. For instance, in a technical publishing environment, where there is strong need to document certain formal features and where most documents are already online, benefits should be immediate. In addition, it is becoming increasingly commonplace to digitize important paper documents, and some organizations are beginning to operate in a nearly paperfree environment. Work in such environments will also benefit from a readying system.

Our focus has been on the way a readying system provides a greatly enriched description of the way documents are used, thus providing an opportunity for new types of information retrieval queries. In essence, these descriptions of documents’ use greatly expand the ordinary contextual descriptions of documents.

Barfield (1996) has complained that contextual information in the digital world is lacking and that this makes finding information more difficult than it should be. Our paper addresses this shortcoming.

To support querying in this enriched context, a readying system must record and document what has been done. We have devoted considerable attention in this paper to the bases for recording, including information acts, speech acts, and work processes. We have defined a formal language that should be considered a working prototype—it is complete and provides needed functionality but also can be modified given new demands by its users. For example, the open use act records which application opens a document. This information could be expanded: other acts could capture this information or applications could be grouped by functionality. Information about applications could also be removed if document-centric computing (suggested by technologies such as OpenDoc or OLE) becomes a reality. Other examples of potential changes to the language include providing document version control and allowing the user to declare that documents are complete and cannot or should not be revised. Thus, while the recording capability has many useful features, it can be extended as need be.

Documenting work involves extending the description of the use of documents even further. When one writes a document, there are countless unwritten associations she has to it: who is likely to approve of what it says, what sources of data still need to be investigated, what arguments might be raised in objecting to its conclusions (and what counter-arguments might be raised to defeat them), and so forth. When a document’s author returns to a document (after a lengthy delay) to continue working on it, these associations may be very hard to recapture, making it difficult to continue work. For the reader of the document, some of the author’s implicit associations will not be evident, and the reader may misapprehend its relevance altogether.

A readying system is supposed to reduce the difficulties an information worker has in dealing with completely different information as she switches among many projects. Ideally, when one resumes a task, a readying system would effectively capture the mental “state” she was in when the task was suspended. An information act description of work, comprised of use acts and documentary acts, may help one “recapture state” in a limited way. Annotative acts help a bit more. But a truly effective readying system should support better an information worker’s need to document her mental associations to a project (the arguments, counter-arguments, etc. we mentioned). Much research needs to be done to improve upon the customary devices people use today when attempting this, like attaching notes to documents or grouping documents together in a folder. Providing effective ways to document these underlying thoughts about a document’s history and use may be extremely effective in helping information workers be ready to work.<sup>2</sup>

## References

Agre, P. E. 1995. Accountability and discipline: a comment on Suchman and Winograd. Computer Supported Cooperative Work 3 31–35.

Aura¨maki, E., E. Lehtinen, K. Lyytinen. 1988. A speech-act-based office modeling approach. ACM Trans. Office Inform. Systems 6(2) 126–152.

Austin, J. L. 1975. How to Do Things with Words. 2nd edition. Harvard University Press, Cambridge, MA.

Kent, B., M. Harnish. 1979. Linguistic Communication and Speech Acts. MIT Press, Cambridge, MA.

Ballmer, T., W. Brennenstuhl. 1981. Speech Act Classification. Springer-Verlag.

Barfield, L. 1996. Sticky labels. SIGCHI Bull. 28(2)95.

Celentano, A., M. Fugini, S. Pozzi. 1991. Querying office systems about document roles. A. Bookstein, Y. Chiaramella, G. Salton, V. Raghavan, eds. Proc. Fourteenth Annual International ACM/ SIGIR Conf. on Research and Development in Information Retrieval. Assoc. for Computing Machinery 183–189.

——, M. Grazia Fugini, S. Pozzi. 1995. Knowledge-based document retrieval in office environments: the Kabiria system. ACM Trans. Inform. Systems. 13(3) 237–268.

Croft, W. B., L. S. Lefkowitz. 1988. Using a planner to support office work. Robert B. Allen, ed., Proc. Conf. on Office Computing Systems. ACM SIGOIS & IEEECS TC-OA, ACM Press, Palo Alto, CA 55–62.

Gordon, M. D. 1997. It’s 10 a.m. Do you know where your documents are? The nature and scope of information retrieval problems in business. Informations Processing and Management 33(1) 107–121.

Hammer, M., J. Champy. 1993. Reengineering the Corporation. Harper-Business, New York.

<sup>2</sup>File: getting-ready.tex. The authors contributed equally to this paper. Send correspondance to either author.

Harel, David. 1987. Statecharts: A visual formalism for complex systems. Sci. of Computer Programming 8 231–274.

Harrington, H. J. 1991. Business Process Improvement. McGraw-Hill, New York.

Lamming, M. G., W. Newman. 1992. Activity based information retrieval—Technology in support of human memory. Information Processing 92: Personal Computers and Intelligent Systems, Vol. 3, Elsevier, New York, 68–81.

——, M. Flynn. 1994. “Forget-me-not”: intimate computing support of human memory. Proc. FRIEND21: 1994 International Symposium on Next Generation Human Interface.

Malone, T. W., K.-Y. Lai, C. Fry. 1995. Experiments with Oval: a radically tailorable tool for cooperative work. ACM Trans. Inform. Systems 13(2) 177–205.

Medina-Mora, R., T. Winograd, R. Flores, F. Flores. 1992. The action workflow approach to workflow management technology. Jon Turner, Robert Kraut, Eds., Proc. Conf. on Computer-Supported Cooperative Work, ACM SIGCHI & SIGOIS, ACM Press, Toronto, Canada 281–288.

Moore, S. A. 1995. A communication framework for applications. J. F. Nunamaker, Jr., R. H. Sprague, Jr., Eds., Proc. Hawaii International Conf. on System Sciences, III, Wailea, HI, IEEE Computer Society Press, 330–341.

——. 1996. Testing speech act theory and its applicability to EDI & other computer processable messages. Proc. Hawaii International Conf. on System Sciences. IEEE Computer Society Press.

Radosevich, L. 1995. Going with the flow. Computer World. April 87– 97.

Searle, J. R., D. Vanderveken. 1985. Foundations of Illocutionary Logic. Cambridge University Press, Cambridge, MA.

Sohlenkamp, M., G. Chwelos. 1994. Integrating communication, cooperation, and awareness: The DIVA virtual office environment. R. Furuta, C. Neuwirth, Eds., Proc. Conf. on Computer Supported Cooperative Work, Chapel Hill, NC. ACM SIGCHI & SIGOIS, ACM Press, 331–343.

Suchman, L. 1994. Do categories have politics? Computer Supported Cooperative Work 2 177–190.

——. 1995. Speech acts and voices: Response to Winograd et al. Computer Supported Cooperative Work 3 85–95.

Trammell, K. 1996. Work flow without fear. Byte April 21(4) 55–60.

Tueni, M., J. Li, P. Fares. 1988. AMS: A knowledge-based approach to task representation, organization and coordination. Robert B. Allen. Ed., Proc. Conf. on Office Information Systems, ACM SI-GOIS & IEEECS TC-OA, ACM Press, March 78–87.

Wilson, L. 1994. All together now. Inform. Week November 57–64.

Winograd, T. 1994. Categories, disciplines, and social coordination. Computer Supported Cooperative Work 2 191–197.

——, F. Flores. 1986. Understanding Computers and Cognition. Ablex Publishing Corp., Norwood, NJ.

Woo, C. C., F. H. Lochovsky. 1987. Integrating procedureautomation and problem-solving approaches to supporting office work. G. Bracchi, D. Tsichritzis, Eds., Office Systems: Methods and Tools, IFIP TC8/WG 8.4, North-Holland, Amsterdam 17–32.

Nancy Van House, Associate Editor. This paper was received on July 16, 1996, and has been with the authors 10 months for 1 revision.
