---
otero_id: 25954
otero_key: "3J9XVFCE"
title: "To model objects in information systems and user interfaces: implications for object‐oriented methods"
authors: "J. Kaasboll"
year: "1993"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1993.tb00118.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# To model objects in information systems and user interfaces: implications for object-oriented methods

J. Kaasbøll

Department of Informatics, University of Oslo, PO Box 1080 Blindern, N-0316 Oslo 3, Norway; E-mail: jens.kaasbøll@ifi.nio.no

Abstract. A general way of contrasting the object-oriented to the function-oriented approach, called 'object-order' and 'function-order', is proposed in this paper. In addition, when modelling information systems, there is a third principle of ordering, 'subject-order'. Object and function-order are used to define the two approaches to modelling information systems and in human-computer interaction, in ways that are compatible to the corresponding distinction in programming. The conditions for selecting either of the two approaches are, however, not discussed here.

By means of an object-ordered method, e.g. Jackson System Development (JSD), an object-ordered model is produced, and the user interface that can be derived from the model is object-ordered too. However, other guidelines in JSD support subject-order. A function-ordered interface can be derived from the subject-ordered model. A computer system designed by means of an object-organized method may therefore obtain an interface that is partially object-ordered and partially function-ordered. Other object-oriented methods give guidelines for designing function-oriented interfaces without relating these guidelines to the model.

The system designer may benefit from having three principles of ordering when modelling a system. However, a user may be confused by an interface that sometimes gives preference to objects, sometimes to functions.

Keywords: information systems, systems analysis and design, user interfaces, user/machine systems.

## 1 INTRODUCTION

A dispute between function-oriented and object-oriented programming exists, and currently object-orientation seems to be in fashion. Object-oriented programming has been defined using the mechanisms of programming languages, e.g. encapsulation of data and functions, categorization of objects into classes and generalization of categories with inheritance and polymorphism, and dynamic instantiation and deletion of objects (Korson & McGregor, 1990; Wirfs-Brock & Johnson, 1990). Some claim that objects should contain their own sequence of actions as well (Nygaard, 1986).

In the field of information systems, there are two areas in which similar controversies have occurred:

(1) Modelling: A model of an information system can include data, computers, user interfaces, users, human use of information, tasks, etc. How can an object-oriented and a function-oriented model be defined? And which is to be preferred?

(2) Human-Computer Interaction: How to define an object-oriented and a function-oriented interface, and how to select either of them during design?

In the field of modelling, object-oriented models have been constructed in a manner similar to that of programming. However, when considering object-orientation in human-computer interaction, properties such as generalization and encapsulation have not been discussed in the literature. Although this could be of interest, the discussion in this paper is restricted to the distinction between the ordering principle of functions, objects and subjects. Function-order and object-order are defined below, while subject-order will be introduced in section 3.

In order to define a distinction that is applicable in modelling as well as in interaction, the concepts 'object' and 'function' are related to persons and acts in the following manner: a person acts upon or about or towards an object or several objects, and a computer processes objects. A category of acts or processes is called a function. For example, when a person enters a record in a database, the record and the database constitute objects, while, in general, the act of entering constitutes a function.

When performing several acts or processes, the acts and processes may be upon, towards or about several objects. If there exists a sequence of acts or processes upon an object, and the acts or the processes are categorized by different functions, the sequence is object-ordered. If there exist sequences of acts or processes upon several objects, and the acts or processes are categorized by the same function, the sequence is function-ordered. For example, when entering one record after another, the function 'to enter' is stable, while the objects shift, therefore this is function-ordering. However, when entering, controlling, correcting and transferring a record, there is a fixed object upon which several functions are applied, hence the sequence is object-ordered.

There may be no order at all. A receptionist at a hotel may use a computer to book two rooms for three nights, check out a guest, add up today's income, search for a credit card number, see if there is room for a party in the dining hall, etc. There is no recurring pattern in the work. The receptionist works with rooms, guests, time periods, money, etc. in any combination. No kind of object seems to dominate. No kind of function seems to dominate either. Booking, checking in, checking out, etc. are done at requests that occur at random.

The order will often be dependent on the level of detail. At the aggregated level, one may search for customer records, which is function-ordered. At the next level of detail, one may perform several operations on each customer record, working in an object-ordered sequence. For each operation, several parameters or data items may be entered, such that the ordering is according to functions at this level of detail.

It has been argued that user interfaces should be consistent (Nielsen, 1989). Transfer of learning from one situation to another is hampered by inconsistencies (Rosenberg, 1989, p.25). Consistency creates expectations of program behaviour, and if a new program fulfils these expectations, it will increase the possibility of being accepted (Nielsen, 1989, p.5). Company standards concerning the user interface can also reduce specification work (Nielsen, 1989). However, 'ease of use' may conflict with principles of consistency, so the purpose of using the computer programs has to be taken into account before insisting on consistency in a special dimension (Grudin, 1989).

Concerning objects and functions, a user interface may support one or the other style of working, e.g. by allowing for first selecting object and then functions, or vice versa. It will be inconsistent if a computer system mixes up the two principles of ordering at one level of detail. The general principle is that the interface should, at each level of detail, consistently allow for either 'select object, apply functions', or 'select function, apply to objects'.

When modelling an information system, a designer may decompose the system in an order that is supported by a modelling technique, e.g. processes or classes of objects. Some techniques focus on processes, while others give preference to objects.

What is considered here is the implication from

(1) the way of ordering when modelling an information system

to (2) the ordering principle of the user interface.

Current methods in system development do not seem to acknowledge that there may be any implications. This paper aims to explain how modelling according to methods that have been characterized as 'object-oriented' or 'object organized' affects the ordering of the interface.

The argument is presented by means of the Jackson System Development method (JSD) (Jackson, 1983), because this method makes a clear distinction between user interface components and other contents of the software. The main principle of modelling in JSD corresponds to object-ordering. In this article, it does not matter that JSD lacks some of the acknowledged properties of object-orientation.

Object vs function-ordering in human-computer interaction and user interface is discussed in section 2. The popular opinion that object-ordering is equivalent to windows or icons is rejected. Section 3 presents the relevant aspects of an information system. The principle of object-ordered modelling that corresponds to object-ordered interaction is presented. JSD is presented in section 3, and in section 4 JSD illustrates the implications of the modelling approach on the principle of the ordering of the user interface. Implications for designers of CASE tools and of information systems are outlined in section 5.

## 2 OBJECT AND FUNCTION-ORDER IN HUMAN-COMPUTER INTERACTION

The difference between object and function-ordering has been defined according to their mutual sequence. In order to make a corresponding distinction in the area of user interface, the sequence of events taking place at the interface needs to be considered. This sequence is the process of human-computer interaction. The interaction could be ordered according to functions or objects, or it could have no order at all. The ordering of the interaction can be supported by the user interface.

To be able to define what an 'object' is in the context of human-computer interaction, one has to be aware that what an object is from a user's point of view does not have to correspond to how a programmer regards objects. Since the aim here is to discuss how to avoid a user experiencing the interface as inconsistent, the user perspective on objects is adopted. To put it simply, objects then constitute the items of the work of the user. Objects correspond to the grammatical objects of sentences uttered by the user about what he or she is doing. In 'I write letters', the 'letters' constitute the objects of work. In the case of a librarian, for example, the objects may consist of books, records of books in the computer system, borrowers, records of borrowers, letters, catalogues, etc. Object-ordered interaction would in this case, imply that he or she performed various functions on each book, record, letter, etc. before shifting to another object.

A user interface that supports object-ordered interaction is called an object-ordered interface. For example, a mail program that allows for working with a letter, doing any kind of transformation on it in any order, e.g. deciding its receivers, writing, drawing, or calculating its contents, and sending it, is object-ordered.

Function ordered interaction requires the opposite order: first select a function, then write a sequence of input data, all of which is processed accordingly. For example, it may be a mail program operating in the following fashion: you select the send-command, then the program goes into a loop asking for receiver and file-name repeatedly.

Shneiderman suggests a correspondence between the way of ordering and the style of the interface. He claims that function-ordering is preferable when using a command language style of interface with arbitrary signs, while the iconic or physical signals used in graphical interfaces better support object-ordering (Shneiderman, 1987, pp. 151–52). Consequently, in a command language, the command should precede the object, e.g. Display File and not File Display. In a graphical interface that might support direct manipulation, the object-order should be of preference. In order words, one should first select the object, e.g. by point and click followed by highlighting, and then perform the functions on the object selected. Shneiderman does not relate these principles to any concept of object or function-ordering, however.

In the following, this article concentrates on object-ordered interface and object-ordered interaction. This does not imply that object-order in interaction is a better design choice than function-order. The actual choice should be made according to the task of the users, the purpose of the program, and specifications concerning consistency.

The phrase 'object-oriented user interface' is sometimes used for every interface containing icons or supporting direct use. Verplank says in a handbook of human-computer interaction:

'Shneiderman has defined the term "direct manipulation" quite broadly to include video games, display editors, spread-sheets, and "desktop metaphors". What can be called "object-oriented" direct manipulation interfaces more narrowly defines a class of interfaces which rely on concrete and visible objects, simplified sets of user actions and rapid feedback where the key activity is visibly moving screen images by pointing at them.

![](/api/attachments/3J9XVFCE/fulltext/images/9fa96c74c7d2519e1760674ab24147a6b9024dc70d4ed1dd4fc61c0fca929a9f.jpg)  
Figure 1. An interface icon that represents a function. Objects can enter at the top and be collected at the right hand side.

Computer-aided design interfaces, video games, the "desktop metaphor" and graphical programming languages are examples.' (Verplank, 1988, p. 365)

Verplank further says that 'objects' should be appropriate to the intended application. He uses the term 'object' quite consistently in the same sense as done here, although he does not express the difference between functions and objects. At least one of the 'objects' in his illustrations, a converter, is an icon representing a function. Using icons does not guarantee that a user will or should interpret the icon as an object. An icon that looks like a mincer may represent a function (see Fig. 1).

An icon that represents a function does not necessarily create a function-ordered interaction, however. Consider an interface for direct manipulation that has several icons representing functions and several representing objects. If the user can select an object and drag it through several functions, e.g. enter it at the top of the mincers and collect it at the right hand side, the sequential order of acts is according to the objects.

However, if the user has to select a function icon and drag it from one object to another to perform the operations on the objects, the interaction would be function-ordered.

The Macintosh user interface is renowned for its object-oriented user interface. However, it is not consistently object-ordered in the sense defined here. Both programs and data are presented in the same manner to the user: files are identified by an icon and a name. For example, if you are at the operating system level (the 'Finder') and want to edit a new document, you will have to select the edit operation first, by means of starting up an editor program. Then you start to write and experience that there seems to be a text object on the screen. However, the text will not be an object selectable at the operating system level before you give a save-command.

A user may subjectively experience working in an object-ordered fashion, even if the user interface only partially supports the principle. In the Macintosh case, the user may be thinking of the file to be edited while starting up the editor, such that he or she preserves his or her experience of object-ordering while handling the functions of the user interface. A corresponding remark could be given considering the functional order.

If generating new objects supported the object-ordered experience, there could e.g. have been a pile of blank documents from which to start. This principle was built into the interface of Lisa, the predecessor of Macintosh. The principle was abandoned, and a study of user experiences gives one reason:

'To get a piece of memo paper or a folder in Lisa they had to select a template icon (called a stationary pad), "tear off" a copy using the File/Print menu, and only then open the new icon for work (assigning a name to the new icon was optional). A user complained, "I write my memos before tearing them off. If they're going to use analogies they ought to do them right!" (Carroll & Mazur, 1986, p. 42).

The primary object-ordering was accepted, while the ordering of the functions to be fulfilled should be reversed.

A reason for the appearance of programs as objects can be found at the level of programming. When programming an editor and a file system in an object-oriented manner, the programs become objects in the programming environment, and they may be described as objects in a programming language. For interfaces intended for programmers, it may therefore be useful to represent programs as objects. An example is found in a programming environment intended for object-oriented programming by Hedin & Magnusson (1988). They make a distinction between activity-oriented and object-oriented use of windows. They define activity-oriented as a window that enables a programmer to perform a certain activity, e.g. browsing through a list. An object-oriented window is, in their terms, 'a window that has a one-to-one correspondence to an object'. (Hedin & Magnusson, 1988, p. 42). An 'object' in this sense refers to an object in an object-oriented programming language. They state that the interface they have designed is 'object-oriented' in this sense. However, it turns out that a window may contain a description of classes as well as procedures. This illustrates that in interfaces of programming environments, one has to distinguish between program text and program execution, and one has to be careful when transferring principles from programming environments to designing interfaces for applications.

In many applications, the functions can be modified, implying that users can program their applications. For example, in a drawing program, the user may select a drawing tool and reshape it. If so, a situation similar to that of programming environments appears. The functions of the applications become objects of the programming activity. For example, the drawing tool becomes the object of the reshaping function.

Summarizing the topic of human-computer interaction, two principles concerning object-ordering have been outlined:

(1) Select as objects the items that users perceive as objects of their work, and do not simply include everything that can be expressed as objects in an object-oriented programming language.

(2) Object-ordering of human-computer interaction occurs when the sequence of the operations performed by the user is 'Stick to one object at a time, and perform various operations on it'. This can be achieved if allowed by the user interface, regardless of its iconic or textual form.

## 3 OBJECT-ORDERED MODELS OF INFORMATION SYSTEMS

The concept ‘information system’ is used here to include computers, users, information, paper documents, communication equipment, etc., and the processes that take place in and between these components. In order to create an information system, it is recommended that parts of it be modelled. As in the areas of programming and human-computer interaction, different principles of ordering can be identified in the methods for modelling. Assume that object or function-order is wanted in the interaction. Then it would assist the design task if there were correspondence between the ordering of the model and that of the interface or the human-computer interaction. In this section, object-ordering in modelling is defined, and some methods that have been characterized as object-oriented are discussed.

## 3.1 Principles of order in information systems

Object-order in modelling is defined as a modelling process in which the main principle for decomposition is to decompose according to the objects of work. The outcome of object-ordered modelling is an object-ordered model. For example, in the case of a library information system, the objects of work to be modelled as objects have been identified as books, records of books in the computer system, borrowers, records of borrowers, letters, catalogues, etc. Even if the objects of work constitute the main criteria for decomposition, functions or other aspects may constitute criteria at lower levels of details in the models.

Compared to the issue of human-computer interaction, however, more aspects than the objects of work can be considered when modelling an information system. The following is a conceptual classification of aspects that will be relevant in the discussion of ordering. The objects of work are found in the categories 0 and 1. The library information system is used as an example:

(0) Reality: The reality to be represented in the computer. For example, books, borrowers, loans, acts of loaning, constraints on loans.

(1) Representation: The representation of the reality in the computer. For example, records of books, borrowers, loans, transitions between states of books, library catalogues and changes in them.

(2) Users: The users and their work, their professional roles, their needs and opportunities, the goals and rules of the organizations. For example, the librarians, their work, their knowledge and organization.

(3) User interface: The user interface of the computer. For example, keys, pointers, windows, menus, commands, etc. (Derived from Mathiassen et al., 1991).

Reality and Users constitute the world outside the computer system, and these are often mixed up when modelling information systems. A basic distinction is that what happens in category no. 2 (Users) is about no. 0 (Reality). The information system and the work of the users are about Category 0, Reality. The work of librarians is e.g. about books. The data in category 1 are also about Reality. The user interface in category 3 is the form given to the representation, and it is this category that the user experiences directly.

Since object-order is defined to take its point of departure in Reality and Representation, the remaining categories call for an analysis. First, however, we will consider the issues covered by common modelling methods.

When making a data model, the entities of Reality will usually constitute the point of departure. If records and relations already exist, the modelling process could start with Representation. The entities of a data model are therefore candidates for being objects, although they lack the operations and their sequence, which is necessary to model the object-order.

The logical dataflow diagrams of structured analysis model Representations (Yourdon, 1989). The main principle of decomposition in dataflow diagrams is according to processes, which implies that it is impossible to achieve object-ordering.

In the physical dataflow diagrams sometimes used in analysis and design, decomposition is performed according to the individual users or departments, and the computer hardware. These constitute the persons and equipment in categories 2 and 3, performing the acts or processes taking place. This may correspond to the subject of sentences uttered by the user about what he or she is doing, e.g. in 'I write letters', or about what the computer is doing, e.g. 'It prints the letters'. Modelling according to this principle corresponds neither to object nor function-order. Because the main principle of decomposition is according to the persons or the equipment who perform the processes, this way of ordering is called subject-order.

## 3.2 Object-ordered modelling methods

The object-ordered methods divide their area of application into objects with associated functions. Objects are sometimes referred to as components, entities or classes, while functions are called services, methods, events, actions, procedures, etc.

Two early approaches that did not consider user interface are first described briefly (Holbæk-Hanssen et al., 1975; Rosenquist, 1982). Then two recent methods that do not consider implications from models to interface are discussed (Wirfs-Brock et al., 1990; Coad & Yourdon, 1991a,b). JSD is finally described.

DELTA is a language specially suited for modelling real time system (Holbæk-Hanssen et al., 1975; Håndlykken & Nygaard, 1981). An object in DELTA may consist of data, procedures, and an action sequence. There are no explicit guidelines for selecting what to model as an object. The mechanisms in the language make it easy to model components with analogue action sequences, and exemplars are presented in which users, computers and components from process control systems are modelled as DELTA objects. In addition, objects of work are modelled. This includes all four categories of an information system. DELTA is therefore considered both subject-ordered and object-ordered.

Entity life-cycle models consist of entities with associated discrete event sequences, and the entities to be chosen seem to correspond to entities in ER data models (Rosenquist, 1982). No evidence of other ways of applying the technique is found. Therefore, the entity life-cycle model is classified as object-ordered.

Object-oriented analysis and design (OOAD) first sets out to analyse the 'problem domain component', corresponding to the Category 0, Reality (Coad & Yourdon, 1991a and b). In the design phase, a human interaction component is to be constructed. They propose to make a model of the users, but these models are not related to the object-oriented model of the computer system. Therefore, OOAD is not subject-ordered. Concerning interface design, Coad & Yourdon advise to design a command hierarchy (Coad & Yourdon, 1991b, pp. 57, 60–61). No reason for this function-ordered approach is given.

Designing object-oriented software (DOOS) is a method for program design, assuming that one should immediately make an object-oriented model of category 1, Representation (Wirfs-Brock et al., 1990). Concerning user interface, DOOS supports structuring of the interface program. The form and contents of the interface seem to be taken for granted, however. Their examples start off from given interfaces of a drawing program and an automatic teller machine. Thus DOOS does not use the model to derive properties of the interface.

Jackson System Development (JSD): In a survey of object-oriented system development approaches, the JSD method was characterized by 'object-based concepts' and 'functional decomposition', without the mechanisms of inheritance, dynamic types of references and procedures, etc. that are usually required for the 'object-oriented approach' (Henderson-Sellers & Edwards, 1990, p. 146). The lack of mechanisms for inheritance and procedures in JSD is acknowledged. However, that does not concern the sequential properties discussed here.

Its principles of ordering will have to be considered at several stages of JSD modelling, three of which can be summarized:

Entity structure step: The Reality (category 0) is considered. The actions and events are organized according to the entities that undergo or perform the actions. For example, the entity 'book' is returned, and the entity 'borrower' is returning it. For each entity, the actions and events are ordered in a time sequence. These entities are called 'entities-0'. Because the sequence of events and actions are associated with each entity, and because the entities constitute the objects of work, the entity structure step produces an object-ordered model.

Initial model step: The representations, called 'entities-1' (category 1, Representation above), of the entities-0 are modelled, and the communicative relations between them are outlined in a network. A book record with its possible transformations is an example of an entity-1. The internal structure of the entities-1 are similar to the structure of the entities-0. Since the area considered belongs to what the work is about, the model is still object-ordered.

Function step: Functions are added to the model, e.g. statistical reports about the book entities or request/response. These represent the books and borrowers as well, and they also belong to category 1. They are mainly modelled as functions that are decomposed in more detailed functions, and their principle of ordering is therefore closer to functions than to objects.

An extension of JSD with the common properties of object-orientation is found in (Mathiassen et al., 1992).

In summary, there are two areas that can be modelled in object-order:

(1) the reality which the information system and the work of the users is about, and

(2) the representation of this area in computers or on paper.

Subject-order is achieved if the main principle of decomposition is according to the users or equipment performing the processes in the information system.

## 4 IMPLICATIONS FROM MODELS TO INTERFACE

Object-order in human-computer interaction and in modelling information systems has been discussed. Bringing the two together, it would have been comfortable for the designer if an object-ordered model brought about a particular principle of ordering in the user interface of the system designed. It could be argued that if the principle of object-order in modelling outlined above is followed, the model would constitute a basis for an object-ordered interface as well. However, if an 'object-oriented' modelling technique is used in a subject-ordered way, the interface becomes function-ordered.

JSD will be used as an exemplar in this argument, because it is the broadest method when the areas of modelling and the corresponding principles of order are at stake. The librarians' computer system is used for illustration.

In the entity structure step, models of, for example, books and borrowers are produced. In a simplified, textual form, the book and borrower entities may be described as in Fig. 2.

<table><tr><td>Book-0</td><td>Borrower-0</td></tr><tr><td>Acquire</td><td>Register</td></tr><tr><td>Classify</td><td>REPEAT</td></tr><tr><td>REPEAT</td><td>Lend</td></tr><tr><td>Borrowed</td><td>Return</td></tr><tr><td>Returned</td><td>EITHER</td></tr><tr><td>Book end</td><td>Move OR Die</td></tr></table>

Figure 2. Entity structure step. Derived from (Sutcliffe, 1988, p. 70).

In the initial model step, the representation of these entities in the computer is produced. These entities, called Book-1 and Borrower-1, have internal processes corresponding to the -0 entities. Book-1 is shown in Fig. 3.

```htaccess
Book-1
Receive registration
Receive classification
REPEAT
Receive borrower-id
Receive borrower-id
Book end
```  
Figure 3. Book-1 entity from the initial model step.

The classes of entities are depicted in a network diagram, including the flow of data between entity-0 classes and entity-1 classes (see Fig. 4).

In the function step, additional functions can be designed. The librarian may, for example, want a statistical report on the frequency of loans for a range of books. This is modelled by an entity which retrieves data from the Book-1 entities in the network, as indicated in the upper right corner of Fig. 4 (in italics). The functions constitute additional functionality (category 3) to the system.

In the network, the border between the world outside the computer (Reality) and the data inside it (Representations) is depicted by a dotted line. The dataflows that cross this line become the input/output of the computer system. The structure of the input/output flows could be used as a basis for designing the ordering principle of the user interface. If so, there would be two classes of entities: books and statistics. In a more realistic setting, there would be many more classes, e.g. borrowers. The top level interaction offered by an interface with these components would be to make a selection from the classes or the individual entities.

![](/api/attachments/3J9XVFCE/fulltext/images/62c698042fd684fda28833542da99b72187ea542a0b37061084f71e93c047ec0.jpg)  
Figure 4. Initial model step and function step (in italics). The rectangles illustrate classes of entities. Some relations are omitted.

Books constitute objects. However, statistical reports can be expressed at the interface as a function, e.g. Calculate Statistics, or as an object, e.g. Statistical Report. If chosen as a function, the appearance of the statistics would be inconsistent with that of the books.

In order to obtain an object-ordered interface after applying the function step in JSD, these principles should be followed.

(1) Make each entity or class of entities obtained in the initial model step appear as an object or a class of objects.

(2) For each entity modelled in the function step, make each output product of these appear as an object.

The issue of designing a user interface is not discussed at any detail in the literature on JSD. However, one way of modelling in order to design user interfaces is recommended in a textbook by Alistair Sutcliffe (Sutcliffe, 1988, pp. 71–73):

'The starting point is to model the time ordering of the user's actions when operating the computer system. The dialogue can be modelled as a series of steps in which the computer asks a question and the user replies . . .'

This approach implies that the time ordering of the operations enabled at the user interface should mimic the time ordering of the work of the librarian. The representation of the user interface can therefore be similar to the representation of the user. Consequently, one should model the user in the library, namely the librarian. The librarian entity is presented in Fig. 5.

![](/api/attachments/3J9XVFCE/fulltext/images/30d916828cef632d54a6cb756f904210900a903c301cb094f7c24251d004ac0b.jpg)  
Figure 5. Librarian entities according to Sutcliffe's recommendations. Librarian-2 represents the librarian, while Librarian-3 represents the user interface of the computer.

The user interface mirrors the tasks of the user, and therefore the structure of the interface becomes function-ordered. The user and the user interface entities are added to the network diagram in Fig. 6. A likely implementation of this structure is a two-level menu hierarchy in which Back office and Front desk constitute the upper level. Figure 7 illustrates this function-ordered interface compared to an object-oriented one.

According to the categories for modelling outlined in section 3, Sutcliffe proposes a subject-ordered model as a basis for user interface design. The resulting interface supports function-ordered human-computer interaction.

## To summarize in a principle for interface design:

When an 'object-oriented' modelling technique is used, and function-ordered human-computer interaction is preferable, make a subject-ordered model of the users' tasks.

Textbooks on JSD do not make the implications for interface ordering explicit. Therefore, one would expect that the order of the interface corresponded to the object-order of the modelling method. This does not seem to be the case.

JSD has been used to demonstrate the relation between the principles of ordering in modelling and in user interface. The relations are summarized in Fig. 8.

The property of JSD that has been applied in this argument is that the entities have a sequence of events. If the entity describes the user as a subject, the choices at the interface become the events in this entity. Similar results would have appeared if using OOAD or DOOS in a subject-ordered way. Figure 9 shows the Librarian as it could have been described in each method. From each of these OOAD- and DOOS-objects that describe subjects, one would have derived a function-ordered interface. The OOAD would have resulted in a flat menu. DOOS would have produced a two-level menu similar to JSD, because of its separation of methods into contracts.

![](/api/attachments/3J9XVFCE/fulltext/images/76cdf7517da365892dba8ae810bc92b01cc7408941ae6d8719e31ac66b3141cf.jpg)  
Figure 6. JSD network with user (category 2) and user interface (category 3) added.

There are no clues in the methods that lead to constructing the objects presented here. However, there are no rules that prevent a system designer from making these subject-ordered models either.

The properties of the methods utilized in this argument are only dependent on the basic principle of decomposing a system into objects with associated functions. Therefore, the relations between the principles of ordering in the information system model and at the user interface will be valid in any object-oriented method. The only difference to be noted between the methods is whether they lead to a flat menu or a layered one.

## 5 IMPLICATIONS

Three principles of ordering have been introduced: object-order (section 1), function-order (section 1), and subject-order (section 3). Designers of user interfaces should be aware that the objects of work of a user neither correspond directly to objects in programming languages nor to arbitrarily chosen icons.

Function Order  
![](/api/attachments/3J9XVFCE/fulltext/images/6df3641c3ab342e1266785fb26c95c22f76b71252303bdd6d22691237f8a5842.jpg)

Object Order  
![](/api/attachments/3J9XVFCE/fulltext/images/907bc494e496a9febde692d40f5895689aa7d1a034b2fb37c7f55e1378e1ac07.jpg)  
Figure 7. Menu-driven user interfaces according to function order (top) and object order (bottom).

Principle of ordering

Information systems model

User Interface

![](/api/attachments/3J9XVFCE/fulltext/images/a4aa723c52e994a5c4db1943cac431d8cd03d5130301913d4451980642e1374a.jpg)  
Figure 8. The consequence of the ordering principle in the information system model upon the user interface.  
DOOS

OOAD  
![](/api/attachments/3J9XVFCE/fulltext/images/098f3179ee89b27ac4a5d80e08a0b9b644b2f1f9eb316af62802438ad312cc71.jpg)

Class: Librarian's User Interface

Contracts

1 Keeping the catalogue of books up to date

Acquire books

This method retrieves the book id from the user and returns the id.

Classify books

This method retrieves the classification code from the user and returns it.

2 Keeping the register of loans up to date Book loan

This method returns the book id and

the borrower.

Book return

This method returns the book id and

the borrower.

Figure 9. Subject order. The models of the user interface of the librarian according to Coad & Yourdon's OOAD and Wirfs-Brock et al.'s DOOS, respectively.

It has been demonstrated that when selecting object-order in the information system model, the corresponding user interface will also become object-ordered. However, when selecting subject-order in the model, the user interface will become function-ordered.

In practice, the order of the interface does not have to be directly derived from the model of the information system. An experienced system designer would let the users test prototypes. However, students and unskilled designers could design the interface based on the information system model directly.

The interface order would also be automatically determined if a CASE tool were used to produce an interface format from a description of objects and subjects. Both the designers of CASE tools and the systems designers who apply CASE tools for generating drafts of user interfaces should be aware of the implications from the principles of ordering in the models to the layout of the user interface.

## REFERENCES

Carroll, J.M. & Mazur, S.A. (1986) Lisa learning. IEEE Transactions on Software Engineering, SE-12, 2.

Coad, P. & Yourdon, E. (1991a) Object Oriented Analysis, 2nd edn. Yourdon Press, Englewood Cliffs, NJ.

Coad, P. & Yourdon, E. (1991b) Object Oriented Design. Yourdon Press, Englewood Cliffs, NJ.

Grudin, J. (1989) The Case Against User Interface Consistency. Communications of the ACM, 33, 1164–1173.

Hedin, G. & Magnusson, B. (1988) The Mjølner Environment: Direct Interaction with Abstractions. In: ECOOP'88: European Conference on Object-Oriented Programming. Gjessing, S. & Nygaard, K. (eds), pp. 41–54, Springer Verlag, Berlin.

Henderson-Sellers, B. & Edwards, J.M. (1990) The object-oriented systems life cycle. Communications of the ACM, 33, 142–159.

Holbæk-Hanssen, E., Håndlykken, P. & Nygaard, K. (1975) System Description and the DELTA Language. Publ. no. 523, The Norwegian Computing Center, Oslo.

Händlykken, P. & Nygaard, K. (1981) The DELTA system description language: motivation, main concepts and experience from use. In: Software Engineering Environments. Hünke H. (ed.), pp. 173–190. North-Holland, Amsterdam.

Jackson, M. (1983) System Development. Prentice-Hall, Englewood Cliffs, NJ.

Korson, T. & McGregor, J.D. (1990) Understanding object-oriented: a unifying paradigm. Communications of the ACM, 33, 40–60.

Mathiassen, L., Munk-Madsen, A., Nielsen, P.A. & Stage, J.

(1991) Rapid Systems Modelling: The Soul of a New Technology. Institute for Electronic Systems, The University of Aalborg.

Mathiassen, L., Munk-Madsen, A., Nielsen, P.A. & Stage, J. (1992) Modelling events in object-oriented analysis. In: Proceedings of the 15th IRIS. Bjerknes, G., Bratteteig, T. & Kautz, K. (eds), pp. 742–757. Department of Informatics, University of Oslo.

Nielsen, J. (ed.) (1989) Coordinating User Interfaces for Consistency. Academic Press, Boston, MA.

Nygaard, K. (1986) Program Development as a Social Activity. In: Information Processing 86. Kugler, H.-J. (ed.), pp. 189–191. Elsevier, North Holland, Amsterdam.

Rosenberg, D. (1989) A cost benefit analysis for corporate user interface standards: what price to pay for a consistent 'look and feel'. In: Nielsen, 1989, pp. 21–34.

Rosenquist, C.J. (1982) Entity life cycle models and their applicability to information systems development life cycles. The Computer Journal 25.

Shneiderman, B. (1987) Designing the User Interface: Strategies for Effective Human-Computer Interaction. Addison Wesley, Reading, MA.

Sutcliffe, A. (1988) Jackson System Development. Prentice-Hall, New York, NY.

Verplank, W.L. (1988) Graphic challenges in designing object-oriented user interfaces. In: Handbook of Human-Computer Interaction. Helander, M. (ed.), pp. 365–376. Elsevier, North-Holland, Amsterdam.

Wirfs-Brock, R.J. & Johnson, R.E. (1990) Surveying current research in object-oriented design. Communications of the ACM, 33, 104–124.

## J. Kaasbøll

Wirfs-Brock, R., Wilkerson, B. & Wiener, L. (1990) Designing Object-Oriented Software. Prentice-Hall, Englewood Cliffs, NJ.

Yourdon, E. (1989) Modern Structural Analysis. Yourdon Press, Englewood Cliffs, New Jersey.

## Biography

Jens Kaasbøll is assistant professor at the Department of

Informatics, University of Oslo, where he has been employed for 12 years. He is currently a co-editor of Scandinavian Journal of Information Systems. His research interests are both in the theoretical basis for information systems, and in finding practical ways to redesign systems so that they appear more integrated seen from a user's point of view.
