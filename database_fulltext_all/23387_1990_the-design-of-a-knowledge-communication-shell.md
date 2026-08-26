---
otero_id: 23387
otero_key: "VEBKSVX3"
title: "The design of a knowledge communication shell"
authors: "E B James; R P Lister; C Edeleanu"
year: "1990"
journal: "Journal of Information Technology"
doi: "10.1057/jit.1990.18"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# The design of a knowledge communication shell

E.B. JAMES, R.P. LISTER and C. EDELEANU

Imperial College and Juniper Systems Partnership Ltd., UK

Abstract: The Juniper 1 program offers a simple, low cost 'shell' for the construction of interactive knowledge bases. This paper describes some of the features of Juniper 1 and the reasons for using it in preference to conventional expert systems.

## Introduction

Our aim is to show how a structured collection of knowledge, a knowledge base, of the type often associated with a so-called expert system can be built up and the information contained mediated to the user in a simple way. We describe the knowledge communication shell or support system which makes it as easy as possible for someone inexperienced in computing to build a knowledge base which can then be made available to users on the majority of small computers.

## The definition of a knowledge base

Let us define a knowledge base through an example.

A firm has a catalogue of thousands of different specialized products. Each day, there are many telephone enquiries for advice on which product to order, and these requests are referred to an ‘expert’ advisor. Provision of expert advice tends to be time-consuming and therefore expensive. However, it is found that the majority of such requests for advice conform to a number of standard patterns, and the expert spends most of his time in relatively routine work.

Over a period of time, an experienced advisor will have developed a collection of questions to ask the intending purchaser, so that the item they need can be quickly established. Each question from the expert depends on the enquirer's previous answer, so that the expert's question collection can be arranged as a decision tree.

What if this decision tree were stored in a computer? Then whoever answers an enquirer can read a question off the computer screen and relay the enquirer's answer to the computer by selecting among a number of expected answers already displayed. This will bring up another question on the screen together with another series of expected answers, and so on until a final screen tells the enquirer that they need a particular product.

This is the essence of the ‘knowledge base’ concept. The expert sets up in advance in the computer a model of how he or she deals with an enquirer, and given that the expert has competently anticipated the range of possible answers to each probing question, then the enquirer should soon be directed to helpful information. Notice that the expert provides two things: the knowledge about the subject and also the plan for interrogating the enquirer.

Having delegated the role of the expert (at least in part) to a computer, enquiries can be made by relatively inexperienced users, and it may be profitable for our example company to distribute the knowledge base to its clients for them to operate on site.

Up to now, it has been assumed that the user will follow directions which are built into the pages designed by the expert. But for many purposes, the user would prefer to browse, that is to move around in the knowledge base in an exploratory fashion, rather than to search for the answer to a specific query. Our shell enables the knowledge base to be explored like a cross-referenced book. A search can be made to satisfy ad hoc or imaginary requirements, or the effect of following any of the options provided can be investigated. Alternatively, the user can access an index of key words which are used on the enquiry screen, and hopefully explained directly to the customer where necessary. In short, the knowledge base can be used as the 'bible' which incorporates both the definition of an organization's products and a description of its activities as encapsulated in the activities of its various experts.

Naturally, problems will always arise which could not have been anticipated when a knowledge base was first prepared. By providing a computerized system to 'filter out' routine enquiries, the expert consultant now has more time to deal with problems which require personal attention. In due course, these new patterns of enquiry can be incorporated in the knowledge base.

## The design of the knowledge base constructor

Development of our system began in 1983, with a program called CAMS (for Computer Assisted Metals Selector). The process of refinement has continued since then in response to our users' needs. In 1989, for copyright reasons, we changed the name to Juniper 1.

In marked contrast to the usual expert systems or conventional programming approach, we have created a knowledge base construction shell which enormously simplifies the construction of a structured knowledge base. We have studiously avoided incorporating unnecessary facilities for their own sake; every aspect of Juniper 1 has been specifically requested by knowledge base authors. Our system comprises two main parts: a constructor program, used by the expert to build knowledge bases; and a 'run-time' program which will be distributed to users together with knowledge bases.

We noted earlier that a knowledge base embodies both information and a plan for interrogating the enquirer. Traditionally these two elements have been dealt with by separate people. The wisdom of the expert has had to be mediated through a knowledge engineer, who actually carried out the business of building the knowledge base. In our system, the expert can perform both roles.

The expert, who is the sole knowledge base constructor, types what the customer or student is required to see directly on the screen, and can at any time go into ‘run mode’ to check how the system behaves from the point of view of the enquirer or end user.

Technically, the knowledge base can be described as a frame hierarchy; or each screen can be seen as a node in a decision tree. Alternatively, the screen can be interpreted as an object with a large number of attributes or qualities; or each screen can represent a system state, with transitions between screens described in a transition table. Our aim is to provide a rich variety of construction tools, with no dogmatism about which is the best to employ. The tools already provided can simulate the activities of a conventional expert system if required.

Let us use the decision tree model to describe the system. Each screen of information which appears to the user is related to a particular node in a decision tree. The user gets to a particular screen by choosing between a path through the tree from a beginning root node. Each node stores local variables which help to define what appears on the screen and how the node is related to other nodes. In addition, global variables can be used to transfer information from one node to any other. The values are transferred through an individual control program which underlies each node. We can look on the display of a particular screen as an in-built function of that control program. As we shall describe later, the control program may be examined and modified by an author if required, but it is not visible to a user.

Now let us describe how the screen appears to the user. The top line of each screen is an index line. Any group of contiguous characters on this line can be used as a key to access that particular screen in search model later. The rest of the screen can display text. The creator of the screen simply types it in with the inbuilt word processor. Each screen can also act as spreadsheet, so that the eventual user can insert numerical values or pieces of text into a spreadsheet model which has been set up by the page creator. However, data and text is not tied to columns as in a conventional spreadsheet. To the screen builder, the screen appears simultaneously as a word processor and spreadsheet; spreadsheet cells can start at any character position and can be of arbitrary length. This facility can be used for example to produce a page with printed equations which work, or where the user can add certain words and obtain information of personal relevance.

Each screen can also display a graph. Any function of the global variables and those associated with the current screen can be displayed as a graph, or a collection of X and Y values can be typed in directly by the user, and displayed in a variety of ways.

In many cases it may be necessary to make use of information already existent in other forms. Product lists will most probably be held in a database, and lengthy technical specifications will exist as word processor text files. We have therefore included a number of functions to provide support for database and text files. These external files may be displayed and edited as an integral part of the spreadsheet. Text files and database memo fields can be edited inside scrolling windows.

Pictures can also be displayed, in colour, together with the text.

The program underlying a particular screen could be controlling in real time a piece of equipment such as a laser video disc, speech synthesizer, or some equipment in a laboratory. It is equally possible to receive data from peripheral devices.

Any screen, through its own associated control program, can call into action an external program, with starting parameters available from user input into the current page. Results returned from the external program can be presented on the current screen in any desired arrangement. A screen can therefore act as the user interface to some underlying program or group of programs. Since these programs can be in a variety of languages, our system can provide a stand-ardized interface for interaction between programs, and is an attractive vehicle for those concerned with reusable programs. This ‘bridge’ to external software is important because it allows us to keep our system as simple as possible without restricting the range of possible uses. We have deliberately refrained from duplicating sophisticated mathematical or graphic functions that are adequately catered for by proprietary sources.

We have described so far the facilities which can be associated with any given screen. We next consider how individual screens can be controlled and sequenced.

## Moving from one screen to another

The transfer from one screen display or node to another during a session with a user can be realized through a wide variety of processes:

\- The user can press a numerical key (0..9), which represents a decision to view one of ten alternative successor screens. Or they can press B to go back to the node at which they were previously. Continuously pressing B retraces the path they have traversed since the beginning of the session

\- The user can initiate a search of the index line of all other screens for a particular keyword. Screens which have this keyword in the index line will be shown in succession, so that the user can select or reject them. Alternatively, the user can search the text of every page in the data base for a word or phrase and have the relevant screens displayed

\- Transfer to a new screen can occur directly as the result of a calculation which uses a combination of inputs from the user and local or global variables previously stored

\- The user can quote the reference number or name of the screen node which was assigned when the node was first created.

With this wide range of constructional facilities the knowledge base builder can set up a teaching sequence varying in complexity from a simple PRESTEL-type hierarchy of fixed screens accessible by quoting a number which is the 'address' of the desired screen, to a complex sequence of interlinked decision models which can be explored by the user in an unlimited number of ways. Usually the user traces a path from node to node which depends on responses to prompts specified on the screen. Alternatively the user can 'browse' in the knowledge base by accessing any node/screen via key words on its index line. Certain screens can be set up to contain lists of these key words for this purpose, like a book index.

The overall structure of each knowledge base would appear to be hierarchical, but access to any screen via keyword or phrase search products. In this case, essentially each node can access every other node, although there would normally be a planned sequence of node visits as determined by the constructor. In practice the builder probably starts with a hierarchy and later adds cross references which turn it into a lattice. This would seem to copy a natural process of model building, which starts with a simple hierarchical design and later adds cross references between nodes.

A good design should cater for both novice and experienced users. The experienced user will probably wish to bypass many explanatory screens, or those concerned with elementary diagnoses, and move directly to more specific areas. Providing short cuts is a simple process, using the inbuilt node link editor.

Several auxiliary programs are provided to assist the knowledge base constructor. Pages may be resequenced, isolated or removed from the knowledge base. A given knowledge base can be cannibalised, and fragments may be joined together to form a new knowledge base.

There are two user interfaces to our system, the first with the knowledge base builder, who is usually an expert in the field, and the second with the final user who expects to obtain information. We aim to make the structure of the knowledge base explicit to the builder, and we provide a range of help facilities to remind the builder of what can be done at any point in the construction. It is possible to obtain a print-out of the knowledge base structure at any time.

Whether the knowledge base is being built or being used, it is always possible to press a HELP key and obtain context-sensitive information about how to proceed.

Our aim is to make the construction of a knowledge base as simple as possible by removing much of the technical paraphernalia traditionally surrounding knowledge base systems. This does not imply that a complex enquiry or training sequence system will be simple to build. Both the quality of the information provided to the user, and the performance of the system as perceived by them, will depend on the skill of the constructor. However, the organization of the material will be much more effectively under the control of the subject expert than in previous support systems and will depend much more on presentational skills than on any particular computer experience or expertise.

## The relation to conventional expert systems

Since our shell claims to support the mediation of a knowledge base to a user, it is natural that there will be interest in its relation to conventional expert systems.

It does not seem profitable to consider whether our shell does or does not have each of the features characteristic of an expert system shell. We would prefer to focus attention on the practical application of the shell, and indicate our willingness to mimic any application which is currently believed to require the support of an expert system shell.

Juniper 1 can simulate the operation of a conventional expert system as it appears to the user. But it does not require knowledge to be represented as a sequence of logical rules. The system does not make logical deductions unless they are explicitly built in by the expert. Leith (1986) shows that the conventional expert system operation is simply not relevant in modelling, for example, a legal system; on the other hand, our system can model the ad hoc judiciary processes of the real world, which he describes, because the transfer of attention from one screen to another is determined by the 'expert' who builds the knowledge base, and this need not be related to any 'logical' process of inference or induction.

It should be recognized that a system which draws inferences from a set of logical rules is essentially statistical in nature, and is not well suited to areas where such factors as rule-of-thumb, 'discretion', or safety margins are important factors. Of course, we do not question that rule-based systems have been used successfully in many applications. We do argue that there are many cases for which rule-based systems are unsuitable, or for which an alternative approach is equally valid and offers a lower cost solution.

Most current work associates conventional expert systems with logic programming. Martins (1984) explains why this is misguided. Certainly, if the construction of each knowledge base involves the specialised expertise of a large number of computer specialists as it seems to at present, there will not be sufficient specialists to create a base in each company. It seems that our attempt to avoid all need for expertise other than that of the subject expert has got to succeed.

One practical demonstration of the benefits of our approach is described in Baker, James and Lister (1988). With financial support from the Department of Trade and Industry, we were able to show how a knowledge base giving advice on design against brittle fracture in the welding industry could be produced directly by a single subject specialist. The time scale for this was measured in weeks rather than months.

In the future, we would expect that the term expert systems would be replaced by one that is less contentious and more user-oriented, and that such systems would take their place among a wide range of alternative computer-mediated training tools.

## Relation to hypertext

A recent valuable summary of developments in hypertext by Conklin (1987) provides a checklist of features to be found in them. It would seem that most of these are available in our shell also. We now see Juniper 1 as an important vehicle for extending the ideas behind hypertext, that is, the development of text in hierarchical rather than linear form. However, since each node in our system provides access to databases, pictures, external programs and peripheral devices as well as text, it would be more accurate to describe Juniper 1 as a hypermedia system.

## The relation to conventional programming

Naturally, all that can be done in Juniper 1 can be done in a conventional programming language. However, the deficiencies of conventional languages are well known: as programs get bigger, there is no way of presenting a hierarchical structure in the program language itself, other than presenting it as a series of subroutines or procedures. All instructions in a programming language are essentially at the same level of detail.

Recent developments in object-oriented programming are moving towards a more flexible approach to program structure. In a similar way, our system permits each node in the hierarchy to be an 'object', with many possible attributes. However the vast bulk of most program source code is to do with the tedious and repetitious business of input-output; that is, presenting information on the screen in a digestible form and eliciting responses from the user. In Juniper 1, this is taken care of. We do not consider that expert advisors should have to be bothered with the minutiae of low-level program code.

Using Juniper 1, the designer can set up a hierarchical arrangement of screens which structure and explain the program, while at a lower level conventional program segments can be attached to and controlled from any of the pages. Juniper 1 can be its own documentation in hypertextual form.

It is an embarrassing fact that some users appear to be trying to use Juniper 1 as if it were a conventional language. Although our system provides a full set of mathematical and text functions, we would not claim such a total generality and convenience for every application. For specialized tasks, Juniper 1 is particularly suitable to act as a self-explaining 'front end' to any existing program. This leads to the concept of reusable program segments, where the transfer of values in and out of a specific program segment is under the control of the Juniper 1 page which 'front-ends' it. A new program is then created by reassembling a suitable selection of these Juniper 1 program control pages. This is related to the concept of an IPSE (Integrated Programming Support Environment).

## Relation to CAL authoring systems

Juniper 1 is a natural vehicle for the preparation of conventional computer-based training material. The teacher determines what to present on screen and can type it in immediately: he or she decides how to ask for a reaction from the students, and specify that directly with the aid of the calculator page facility. Quite complex interactions can be set up through a sequence of Juniper 1 text and calculation pages. Often there will be no need for actual programming as in conventional authoring systems. The students can use a spreadsheet to explore a model inserted by the teacher, simply by typing in parameters as requested, or input values from experiments and plot graphs in a form determined either by the teacher or by themselves.

Reports on student activity and progress can be maintained through any number of interactive sessions by storing these in Juniper 1 with the aid of the database facility. Information stored in this way could also enable students to return to a situation reached at the end of a previous session, with the recovery of all previous responses.

Simulation programs and other complex pieces of program which are already in existence can be incorporated by calling from a Juniper 1 screen. However, we expect that a whole new range of built-in facilities will be asked for when trainers, experienced in a wide variety of authoring systems, begin to construct their knowledge bases with Juniper 1.

## Current developments

Juniper 1 can appear in very different guises to different types of user. At the simplest level, it can appear as a moderately convenient if limited word processor, though the user will soon discover its hypertextual implications. At the same level, it can be used solely as a means of setting up a hierarchy of simple spreadsheets. Used solely as a database attachment facility Juniper 1 could provide the most convenient way of access to database for a majority of users.

As package developers, we are under constant pressure to add an endless list of new features to Juniper 1. Since Juniper 1 is so general, these features include just about every feature existing in every other package, in word processors, in spreadsheets, in database development, in desktop publishers. There is clearly a limit to such implied increases in size and complexity, and so pleas for inclusion will often be met by suggesting that some other package is set up so that it can be called from Juniper 1. In other words, we do not see Juniper 1 as a general package suitable for creating all applications, but as a friendly interfacing tool to a myriad of other facilities.

## How developers can become involved

Our system has been under development since 1983, although the work stems from much earlier research on adaptive tree-structures (Partridge and James, 1974). Earlier versions are in use as conventional knowledge base builders in six countries. A project to demonstrate how the technique might be applied to a range of different types of information was sponsored by the Department of Trade and Industry, and a demonstration of the use of an expert system in welding technology has been completed (Baker, James and Lister, 1988).

Another project funded by the Department of Trade and Industry has successfully employed Juniper 1 and related facilities in the support of those who have lost their memory through accident or disease. In this project, consultants have been able to combine the use of speech synthesis and recognition devices with diagnostic and training knowledge bases.

In addition, the Home Office has funded a project to demonstrate the application of expert systems and intelligent databases to the work of the Metropolitan Police Fraud Squad, based on Juniper 1.

A project currently in progress in West Germany involves Juniper 1 acting as a front end to a large relational database held on an IBM mainframe computer.

It is now time for users with a variety of specialized applications to develop their own systems based on Juniper 1. Potential users are cordially invited to contact the authors for a demonstration with a view to collaborative development. The success of our construction shell will depend on the creative abilities of the subject experts who build the knowledge bases. We aim to place as few computing obstacles as possible in their way.

## References

Baker, R.G., James, E.B. and Lister, R.P. (1988) The application of knowledge based systems in welding. Conference on Computers in Welding, The Welding Institute, Cambridge, June

Conklin, E.J. (1987) Hypertext: an introduction and survey. IEEE Computer, September.

James, E.B. (1986) Computer based teaching for undergraduates: old problems and new possi- bilites. Computer Education, 10, 2, 267–72.

James, E.B. and Lister, R.P. (1987) The use of an expert knowledge base in training. International Conferences on Training for Change, IEE, London

James, E.B. and Lister, R.P. (1988) Expert knowledge bases in office automation. Colloquium on Emerging Office Technologies, IEE, April

Leith, P. (1986) Fundamental errors in legal logic programming. Computer Journal, 29, 6, 545–52.

Martins, G.R. (1984) The overselling of expert systems. Datamation, 30, 18

Partridge, D.P. and James, E.B. (1974) Natural information processing. Int.J.Man-Machine Studies, 6, 205–35.

## Biographical note

Edward James is Lecturer and Consultant in Educational Computing at Imperial College. Costi Edeleanu is a Consultant Engineer. Paul Lister is a Systems Consultant. The authors are Directors of

Juniper Systems Partnership Limited.

Address for correspondence: Edward James, The Computer Centre, Imperial College, Exhibition Road, London SW7 2AZ.
