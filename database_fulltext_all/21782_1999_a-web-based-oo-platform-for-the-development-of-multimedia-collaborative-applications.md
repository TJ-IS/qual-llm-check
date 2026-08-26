---
otero_id: 21782
otero_key: "GK39EV7Z"
title: "A Web-based OO platform for the development of multimedia collaborative applications"
authors: "Luis A Guerrero; David A Fuller"
year: "1999"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(99)00050-0"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Web-based OO platform for the development of multimedia collaborative applications

Luis A. Guerrero <sup>)</sup>, David A. Fuller

Computer Science Department, Pontificia UniÕersidad Catolica de Chile, Vicuna Mackenna 4860, Santiago 6904411, Chile´ ˜

## Abstract

Building CSCW applications is still a complex task. This paper presents a software framework based on objects for building collaborative applications mainly on top of the Web. The 10 objects of the framework are box, boxObject, enÕironment, user, role, session, broadcast, Õiew, boxObjectType and floorControl. We argue that these objects can be combined to produce a great number of collaborative applications. The main aspects in the framework and objects design are discussed. Examples of applications that were developed using the framework are also shown. q 1999 Elsevier Science B.V. All rights reserved.

Keywords: Collaborative applications construction; Object-oriented framework; CSCW; Web applications

## 1. Introduction

These days, it is very common to find Web sites with information about university courses, where the students not only can find administrative information on the course, but also the whole text, exercises, previous semester assignments, and any other type of information related to the course. It is clear that these are helpful for students, course assistants and even for the lecturer. However, this focus has some deficiencies. First of all, the concept of roles <sup>w</sup> <sup>x</sup> 8 is not included. In fact, each user has the same access to all the information and due to the fact that the lecturer, the assistants and the students have different needs for the content, they will require different views when they access the same information.

Second, the system does not have the flexibility of producing different information when a user is in a different state of the teaching–learning process. For example, when a student begins to study, he can require a lesson with all the details. Later, he may perhaps need only the headers and the examples, and maybe at the end only the exercises and the most important definitions. The current Web documents that support university courses do not provide this flexibility. Ingham states that Web sites should provide high service quality levels for their users 14 . <sup>w</sup> <sup>x</sup>

Third, the current systems do not support collaboration among users. For example, they do not provide facilities for writing a collaborative report, although it is very common that the students work in groups and submit reports. When using a collaborative approach, asynchronous, structured and persistent discussions could be implemented on different topics of the subject. Tools that allow the lecturer, assistants and students to discuss a lesson in a synchronous and distributed way can be provided by means of a virtual meeting at a specific hour. And many other tools can be provided if we consider that the Web is already a very successful collaborative environment 5 . <sup>w</sup> <sup>x</sup>

While trying to solve these deficiencies, the CLASS project ‘‘Collaborative Learning Applica-Ž tions for Students’ Support’’ 12 was created. This. <sup>w</sup> <sup>x</sup> project had two main objectives: the creation of collaborative environments that supported interaction among students, assistants and professors, and the creation of flexible Web documents, that allowed information queries and different views according to the role of the users.

From the start of the project, we observed the need for a simple but powerful tool for the quick construction and modification of collaborative applications. It was the beginning of the TOP ‘‘TenŽ Objects Platform’’ platform that is made up of . objects for the construction of collaborative applications. This framework is the one that we present in this paper.

At present, there are a few projects that have similar goals. The Habanero project at NCSA 20 is<sup>w</sup> <sup>x</sup> a framework for sharing Java objects with colleagues distributed around the Internet. However, it does not provide tools for managing data or facilities for the development of Web applications. Habanero is a good platform for the development of Java applications, but it does not have facilities for building applications in other languages.

BSCW ‘‘Basic Support for Cooperative Work’’Ž . <sup>w</sup> <sup>x</sup> 15,21 enables collaboration over the Web. BSCW is a ‘‘shared workspace’’ system which supports document uploading, event notification, group management, a little data awareness and version control. However, it does not provide tools to manage data nor facilities for the development of collaborative applications.

Web-CT ‘‘World Wide Web Course Tool’’ 10Ž . <sup>w</sup> <sup>x</sup> is an easy-to-use environment for creating WWWbased courses that are otherwise beyond the ability of the non-computer programmer. However, it does not provide collaboration facilities or data administration.

NSTP ‘‘Notification Service Transfer Protocol’’Ž . <sup>w</sup> <sup>x</sup> 4 is a good infrastructure system for building synchronous groupware. However, it lacks facilities for the construction of asynchronous collaborative applications.

GroupKit 16,22 is a very good tool for building<sup>w</sup> <sup>x</sup> real-time applications such as drawing tools, editors and meeting tools that are shared simultaneously among several users. However, it does not provide facilities for the construction of asynchronous collaborative applications nor facilities for Web applications.

The TOP platform contains the facilities of the above-mentioned systems, sharing objects through a Web interface, with data administration tools and facilities for the construction of synchronous collaborative applications.

## 2. The group memory and the box object

One of the main design characteristics of the platform is the group memory 3,8 . This memory is <sup>w</sup> <sup>x</sup> where all of the information that has been generating during group working sessions is stored. The final product of the workgroup will also be stored here, as well as all other information for user and data awareness 6 . For the administration of the group memory<sup>w</sup> <sup>x</sup> we use the box object.

A box object is a repository of information in which other objects can be kept. For each object that is kept in a box, the platform stores specific information. This information is stored in another object called boxObject. Therefore the boxObject maintains administrative information on all the objects that are contained in a box. Fig. 1 graphically displays a box and some of the objects that can be kept inside it.

Each box object contains the following information: name, owner or creator, description, state open, Ž closed, erased, system , versions yes or no , types of . Ž . objects that it accepts, list of users and access rights. According to its state, a box can be open, which means in this case that the users can put in and take out objects; closed, when it does not allow objects to be put in or taken out; logically erased, in a state in which only an administrator of the platform can recover it; and system, which is a special state of boxes that belong to the same framework.

![](/api/attachments/GK39EV7Z/fulltext/images/278d71b948eea324667e6f70a794ce1e1b61500ea4d694cf917cf708d01e3639.jpg)  
Fig. 1. Box object for the administration of the group memory.

Awareness mechanisms play a very important role in collaborative applications because they give users the feeling that they are working in groups. In order to provide awareness mechanisms, we should give users information about what the other users are doing or what they have done recently. All this information is stored, in some way, in the group memory. In order to help the applications show awareness information to the users, the boxes have the option of keeping versions of their objects. When this option is activated in a box, the objects are not physically erased or updated. Each object maintains a list with its previous versions.

It can also be indicated what type of objects a box can accept. The types of objects are defined inside the same platform. When a user tries to put an object inside a box, it first checks if this object type is accepted. It also checks to see whether the box is open, and if the user has enough rights access on that box. Each box has a list of roles with the following types of user rights: to put Ž . Ž . P , to erase E , to modify Ž . Ž . M and a special right called owner O grants all of the rights over an object only if the user is the owner of that object.

The box object also has methods of managing its information. For example, just to name a few there are methods for putting objects, for taking them out, for asking if an object exists inside the box in question, for giving a list of all the objects or a list of a specific object type, for recovering a number of previous versions of an object, for closing a box, for opening it and for erasing it.

There is an instance of boxObject for each object inside a box. This object contains, among other information, the owner of the object, the date and hour of its creation and last modification; the list of previous versions for this object if the box accepts Ž versions , and the keywords of this object that will. allow us to make queries later about the information of the box.

## 3. The TOP objects

Using the objects box and boxObject, some other objects that provide facilities for the construction of collaborative applications have been built. All these objects have services, and over these services we can finally build collaborative applications. Fig. 2 shows this diagram.

Using the objects box and boxObject, the following TOPobjects have been built: enÕironment, user, role, broadcast, session, boxObjectType, view and floorControl.

## 3.1. The enÕironment object

The enÕironment object contains information about the whole environment of the application: its name which should correspond with the physicalŽ name of the application , description, owner or ad-. ministrator, list of users with their respective roles and the lists of boxes. Through the enÕironment object, an application has access to its work area. All the other objects of the platform must be associated to an environment.

![](/api/attachments/GK39EV7Z/fulltext/images/933ad6e8aedad6b3cf27e4e6a92c5dc66a5b49840e8c9f3b12ecde0e87f3b99c.jpg)  
Fig. 2. The TOP framework and objects scheme.

This object has methods to create, erase and modify environments; to ask if a specific environment exists; to supply a list of existing environments; to ask if a user is a member of this environment; to ask access rights the user has on that environment; to ask which boxes are associated with this environment; and to ask which sessions are associated with that environment.

## 3.2. The user object

The user object contains information about the users of the platform: their login names, passwords, complete names, e-mail addresses, photographs, addresses, phone numbers and the last date and time each user worked on the platform.

This object has methods to create, erase and modify users, to ask if a user exists, to supply a list of users and to return information of a specific user.

## 3.3. The role object

A role is a set of privileges and responsibilities attributed to a person 8 . The<sup>w</sup> <sup>x</sup> role object contains the rights access of a group of users over the objects of a box or a view. These rights can be to put objects, erase objects, modify objects and<sup>r</sup>or see objects. It has methods to create, erase and modify roles.

## 3.4. The broadcast object

The broadcast object is an extension of the box object. Broadcast is a special type of box that maintains a list of connected users to a session and their host and port numbers. Any object sends to a broadcast is automatically send to all the users on the broadcast list. The broadcast object has the option of storing the objects sent to him but may not choose to do so. It also has information on the type of objects on which the broadcast should be performed, and the port number to which the objects should be sent this depends on the application . Ž .

This object has methods to create, erase and modify broadcast boxes, to send an object to the broadcast box, to include new users connected to the session and to remove users from the session.

## 3.5. The session object

A session is a period of synchronous or asynchronous interaction supported by a groupware system 8 . The<sup>w</sup> <sup>x</sup> session object allows different work sessions to be defined inside the same environment. This object matches the boxes defined in the environment according to the user’s name and the session in which he is working. This object is of great importance because it allows different work groups to use the same application, without making any change in that application. In this way, we can create collaborative applications for a work group and to allow that many groups use it simultaneously. The session object extends single-group applications to multi-group applications.

This object contains an ID, description, name of the environment to which it belongs, list of users, list of connected users including their host names andŽ port numbers , list of boxes, date and time of the . start and termination of the session, and a coordinator.

It has methods to create, erase and modify sessions, to ask if a user is a member or coordinate a session, to ask if a user is connected to the session, to check if the session is open according to the Ž beginning and ending time and to ask the host name. and the port number of a connected user.

## 3.6. The boxObjectType object

The boxObjectType object allows defining new types of objects that will be stored by the boxes. For each type, this object defines a name, an extension, an icon and the respective visualization information for the particular object type. For example, if there are defined graphic objects for a Web application, the object type should contain in its visualization tag something like IMG SRC² ² : <sup>s</sup> PATH BORDER<sup>s</sup> 0 . Using this tag, the system knows the way in: which it should present the objects when being visualized. In these tags the constants PATH and ² : ² : OBJ can be used. The first one will be automatically substituted by the complete path of the object Ž . when displaying graphics, for example and the second one will be substituted by the complete object for example when visualizing text . Icons can Ž .

also be assigned to the object types. This allows a graphic visualization of the types in many situations such as when showing lists of objects.

This object has methods to create, erase and modify types, to ask if a type exists, and to return the icon, tags or extension of a specific type.

## 3.7. The Õiew object

A Õiew is a visual, or multimedia representation of some portion of a shared context 8 . The<sup>w</sup> <sup>x</sup> Õiew object allows different views to be defined on the same objects of a box. A Õiew can be of three types: html HŽ . Ž . Ž . , list L and query Q . ‘‘Html’’ when the view is a simple html document, for Web applica tions; ‘‘list’’ when it is an orderly list of objects that define the structure of the view. For example, if we have a box to store a document, the first object in the list will probably be the title, the second object the authors, then the abstract, the introduction, etc. For a great number of applications, it is enough to have an orderly list of the objects for the views. The view type ‘‘query’’ is the most complex, and based on a very simple SQL language, it allows us to make queries on the objects of a box. For example, queries like: ‘‘select all the exercises from chapter 2 that deal with pointers’’. This would entail placing a select on the box named ‘‘chapter 2’’ of the ‘‘exercise’’ objects that contains the word ‘‘pointer’’ among their keywords.

The Õiew object contains a refresh method thatŽ. builds and stores a static view. For example, for Web application refresh create the html document corre- Ž. sponding to that view or query. This document is stored and displayed every time a user wants to see this view. The SQL queries are executed only a few times, when the information of the box is changed. Each Õiew maintains a list of roles.

It also has methods to create, erase and modify views, to update the order of the object list, to supply the list of views of a box, to see the view as a HTML page and to see the object list of the view using the Ž corresponding icons of each type ..

Through the view objects we can create HTML documents that uses hypertext, graphics, audio and video. However, the boxes can also stored HTML pages with all these elements.

## 3.8. The floorControl object

The floorControl object allows as the assignment of a floor control policy to an object type in a box. When an object has floor control, only a user can have that object at a certain moment. If another user requests the same object, he is added to a waiting list according to the floor control policy requested when creating the floor control FIFO, priorities, etc. .Ž . When the user that has the object releases it, the object is assigned to the following user in the list. For example, if we want to create an application with only one telepointer object 11 , we need to assign a<sup>w</sup> <sup>x</sup> floor control to it. Using an object broadcast, we can have an application where one at a time users request the telepointer to make indications to the other users, or to write on a whiteboard.

This object contains an ID number, the name of the associated box, the name of the user that has the floor control and a queue of users that request the floor control. It has methods for requesting and releasing floor control, for assigning floor control and for placing users in queues.

## 4. The TOP platform

All the objects have been built like classes of the Java language 9 . Each object has its own instance<sup>w</sup> <sup>x</sup> variables and its own methods. From a main server of the platform the classes are imported and a set of more powerful methods or services are created. These methods are used by the applications built over the platform. The server checks the syntaxis of the requested services and creates a thread to attend each query.

The 10 objects of the platform can be combined to build collaborative applications. Each application that wants to make use of the services should create its own environment first. Then, it can define its users, the roles of these users and all the other objects that it needs.

Fig. 3 shows an OMT 17 diagram with the<sup>w</sup> <sup>x</sup> structure of the TOP platform objects. This figure shows the relationships between objects when the applications are built.

In the design part of application construction, the user should first of all decide what type of objects he will need and what information he will keep in them.

![](/api/attachments/GK39EV7Z/fulltext/images/fbf8768238b5326e8e615a524adab7956cef7de0358fa060e395063171d9b72f.jpg)  
Fig. 3. Structure of the TOP framework objects for a collaborative application.

Then he should create the objects with their respective names and build the application. The application will always communicate with the same server, and it will request services over the objects that were previously created.

Fig. 4 shows a scheme of the platform server and the kind of applications that can be built.

The TOP server was built using the 10 objects and a database for the storage of the object instances.

At present this database is composed by simple text files managed from Java, using that language’s methods of concurrency control. However, at this time we are working on an improved version using an OODBMS.

We can build applications in any language that allows us to define sockets. Also we can built Web applications that communicate with the platform through our own Web server built in Java 13 . Using this Web server, we can download applets that allow us to communicate directly with the server, using a ‘‘fourth-generation Web site’’ scheme 7 . It is also<sup>w</sup> <sup>x</sup> possible to built modules or programs in Java that are executed on the Web server side, similar to the serÕlets of the Java Web Server 23 . The applica-<sup>w</sup> <sup>x</sup> tions build over the platform take advantage of incorporating actiÕe objects <sup>w</sup> <sup>x</sup> 2 , meaning those modules that are downloaded through a Web server, executed and then have their results shown through a Web page.

![](/api/attachments/GK39EV7Z/fulltext/images/3cea046bd80f5215a7d9377b6be9e7e626d82260865764b1898b8c95ffb68e7d.jpg)  
Fig. 4. Scheme of the TOP server and the application interfaces.

Let us take a look at some examples of the application’s construction using the platform.

## 5. An asynchronous and persistent Hello World

Suppose that we want to build an asynchronous and persistent ‘‘Hello World’’ application, that is, an application where the users can enter at any moment, post their messages or greetings, and see the list of all the messages that other users have posted until that moment.

First we create a box called helloWorldBox, where all the messages are stored. We will define a ‘‘guest’’ user with rights to put a ‘‘greeting’’ object type. Once these objects are created in the platform laterŽ in the paper we will show how to create them , we. can create the application that communicates with the server and put the messages in the box. Fig. 5 shows this application.

This ‘‘HelloWorld’’ application was developed as an applet that is loaded through an HTML page. Once the applet is loaded, it communicates directly with the TOP platform server.

Let take a look at the way to manage TOP framework objects.

## 6. Administrator of the TOPobjects

The administrator module of the platform is itself an application built on the platform. It was implemented in Java, like a stand-alone application. This application allows us to create the TOPobjects TOPŽ Platform objects . Fig. 6 shows the administrator’s. main screen.

![](/api/attachments/GK39EV7Z/fulltext/images/fcfb4e82d117a58aa8cd75b9e860e1b436276ed7a6b87f5cb841b6756ab6fd3e.jpg)  
Fig. 5. ‘‘HelloWorld’’ asynchronous application over the TOP framework.

![](/api/attachments/GK39EV7Z/fulltext/images/50bafd0a6d75d753d10e31e65a315dfef0a42271020d17526275a1c4b0bdbff8.jpg)  
Fig. 6. Administrator module for the TOP framework objects.

The administrator allows us to create and to modify environments and users. When entering the option of modifying environments, the screen of Fig. 7 is shown.

From this option we can modify the environment of the ‘‘HelloWorld’’ application. Also there are buttons to modify the other objects related with this environment: boxes, views and types of objects. These other options present similar screens. When clicking a button, the application sends a message to the server with the corresponding parameters, and a message is returned with the result of the operation.

All the operations over the objects of the platform can be carried out from this administrator. However, the applications can send these same messages in case they need to create or to modify boxes or another object dynamically.

![](/api/attachments/GK39EV7Z/fulltext/images/d64410e9677027531f1518cb6fb78d777506141a8927b5e3dd31c5026decac27.jpg)  
Fig. 7. Modification of the enÕironment objects.

## 7. Discussion groups

This application was also implemented as an applet. The objective of this application was to provide discussion areas for an undergraduate course. In this case, the Groupware course was chosen. Different discussion topics were presented, each one corresponding to a different box, and two types of user roles were defined: lecturer and students. The students can see the messages on all of the topics, but they cannot put messages in all of them. There are certain topics where only the lecturer can post messages. For example, the topic of news is ‘‘official’’. Here the lecturer can put things like ‘‘the next class will begin 15 min late.’’ We can also obtain the users’ information. This application is very similar to the previous ‘‘HelloWorld’’ application, but it uses more boxes, and it has different users and roles. Fig. 8 shows the application.

When entering the application, the user’s login name and password is requested, and access is denied if the user does not belong to the group. New topics can be added easily by defining new boxes.

The following application, also created on the platform, shows a simple asynchronous collaborative editor.

## 8. Asynchronous collaborative editor

This is another application developed on TOP. For this editor, each new document corresponds to a new box, where we can put two types of objects: text and graphics. As a strategy of collaborative edition, we have decided that each user can only erase or modify objects that were created by him. A user can see the objects of other users and can make comments, but he cannot erase them nor modify them.

![](/api/attachments/GK39EV7Z/fulltext/images/2fb4b4309fa5a63a16181a9ed66d7a94a786251aeef95da7babc2d5926a29d2a.jpg)  
Fig. 8. Application for discussion groups over TOP framework.

![](/api/attachments/GK39EV7Z/fulltext/images/cf75c5bf64b18f2407f4aacbe98d2e43f73d37d5f65cf017dd4b5288c4bb7bec.jpg)  
Fig. 9. Entrance to the asynchronous collaborative editor.

As a general strategy, the users should have a previous meeting, generally a synchronous face-to-face meeting, to define the structure of the document and to decide what topics each member should deal with. Once the structure of the document has been defined, they continue using the editor in an asynchronous and distributed way.

When entering the editor, the user’s login name, password and the name of the document the nameŽ of the box he wants to edit is requested, as shown in. Fig. 9.

Once he enters the document, the screen with the main menu is shown, where three options appear: edit, files and document. This menu is shown in Fig. 10.

In the edit option the text object types are created and sent to the box. In the file option, text and graphic objects can be sent to the box, such as a graph or text that was made at home or in some place without a connection to Internet. This option also allows owners of objects to erase them. Finally, the document option shows the complete document, evoking a Õiew object of type ‘‘list’’. In this option a screen is also shown with the order of the Õiew objects, and allows for the possibility of moving the objects to another place inside the orderly list. We also created a type of object called ‘‘post-it notes’’ that are yellow notes that can be added to any other object of the document. A special icon was created for this object, and a script JavaScript was definedŽ . to visualize the message like a small yellow screen. An example is shown in Fig. 11.

![](/api/attachments/GK39EV7Z/fulltext/images/c9070ef0e7b9250358069da0750f355743154a89be57be2ae692da6aa0963548.jpg)  
Fig. 10. Main menu of the collaborative editor.

![](/api/attachments/GK39EV7Z/fulltext/images/f7dbeccc07815dea1359a988b23ac47da1260f53cddb8a812cd2a0a2cee0ed66.jpg)  
Fig. 11. A view of the document Ž . box with object type ‘‘post-it note’’.

The editor has two means of visualization twoŽ views . The one shown in the previous figure that. displays information on the name of the objects, the owner of the objects and the post-it notes; and the other view where the document is shown in its final version, without any other information.

In spite of being a simple asynchronous collaborative editor, it proved to be extremely useful for paper writing. At this moment we are working on an improved editor’s version. It is important to highlight the fact that the complete editor was developed in three days using all of the tools that the TOP platform provides. In the editor, applets were not used. All programming was written using JavaScript 19 <sup>w</sup> <sup>x</sup> and HTML 1 .<sup>w</sup> <sup>x</sup>

## 9. An electronic meeting system

This application uses the TOP platform to coordinate the shifts through a floor control object ofŽ . video and audio transmission among the participants of the meeting. For the capture, transmission and visualization of audio and video, we used commercial software. The system allows a group of people to participate in a distributed synchronous meeting, with two possible options: audio and video transmission or text-only. The application presents a screen with options to request the floor control for audio and video. It also presents a chat window where a user can send a message to the whole group or some specific user, selecting from a list of users participating in the session. It is important to emphasize that the chat is a key tool to support the collaboration between the users through the Web 18 . <sup>w</sup> <sup>x</sup>

![](/api/attachments/GK39EV7Z/fulltext/images/a20923de6bf8dfdf3172bce50c6b727ff8a9070211c3288965131e9883718bf8.jpg)  
Fig. 12. A simple Electronic Meeting System over TOP framework.

The application defines two types of roles: meeting coordinator and participants. The coordinator can participate in the meeting just like any other user. Fig. 12 shows the interface of this application.

The chat window was implemented with a broadcast type box. All the messages sent by users to that box are automatically distributed to all the other users of the session. This broadcast box also has persistence, so all the topics commented on during the meeting are stored for a later revision.

A box with broadcast is used for the chat, but we also have two other similar boxes: one for brainstorming and another for holding votes. The meeting coordinator can change the window of the chat box for the brainstorming box or for the voting box. In this way, all the users can see if the coordinatorŽ permits it the ideas that the other users have sent. anonymously, or the results of votes, also anonymously.

At any moment, any user can write an idea and send it anonymously to the brainstorming box. The coordinator can request a vote at any moment, for which he activates the voting option. The system allows each user to cast only one vote. The coordinator can also change the floor control policy, for example in order to give priorities to some users.

The content of the three boxes is shown through a Õiew of type ‘‘orderly list’’. There were three types of objects defined for the three boxes: comments, ideas and votes. The three boxes are of a broadcast type. This is a good example of an application that uses the 10 objects of the platform.

## 10. Other collaborative applications

A combination of the platform’s TOPobjects can be used for the creation of numerous more complex applications. Three examples of applications that we are working on at this moment are a mail system Ž . mailbox , a brainstorming system and a voting system.

The mailbox is an asynchronous application that allows the users to send and to receive different types of objects, in addition to text. For their construction we defined a box with the types of objects that are accepted, the users and their roles, and the views. Using the advantages provided by the view object, we can give a greater degree of ‘‘intelligence’’ to this application, such as defining filters for messages received, either for users, or for words contained in the messages.

The brainstorming application is a box where the assigned users can post ideas during a certain period. A user with a facilitator role opens the box to begins the brainstorming period and closes it at the end, preventing users from posting more ideas. We can put text objects in the box, but also any previously defined object type. For example we could make a brainstorming of art logos graphics , or songs for aŽ . festival, or forms for a purchase bid. There is not restriction placed upon the type of objects or ideas.

A voting system can be built in a similar way. A box and a small module that counts the votes are the only extra components that we need.

## 11. Conclusions and further work

In this paper we have presented an object-oriented platform for the construction of collaborative multimedia applications. We also presented the design of some collaborative applications built on this platform.

The box object is the main object of the platform, and it is used to manage the group memory of the collaborative applications. It also provides versions mechanisms for the objects, by which it is possible to provide mechanisms of data awareness. Through the user object, it is possible also to provide user awareness. Users’ roles and different Õiews can also be defined on the content of the boxes.

Another important TOPobject is the session object that allows us to extend single-group applications to multi-group applications. The session object also allows us to reuse the applications like components of another collaborative environment. For instance, if a new collaborative environment needs a chat in order to provide communication among the users, we can create a new session of a chat application already made. Then we can include this session inside the collaborative environment like a new component. In this way, we can reuse all the collaborative applications built on the TOP platform.

As future line of work, we are designing and building more collaborative applications on the platform, to improve and to extend their services. We are also working on improving the outlines of security and concurrency control. In order to do so, we are studying the use of an OODBMS to manage the objects stored in the boxes.

Although the platform was built mainly for Web applications, any application that can define sockets can use its services. The platform has been built completely in Java, and is therefore portable. At this moment we have TOP versions working on Windows NT and Sun Solaris. Recently, we finished developing a Web server in Java with communication facilities with the platform.

## Acknowledgements

This work was partially supported by the Chilean Science and Technology Fund FONDECYT , grant Ž . 198-0960.

## References

<sup>w</sup> <sup>x</sup> 1 T. Berners-Lee, D. Connolly, Hypertext Markup Language Specification-2.0, IETF HTML Working Group, RFC1866, 1994.

<sup>w</sup> <sup>x</sup> 2 M. Brown, M. Najork, Distributed Active Objects, Proceedings of the 5th International World Wide Web Conference, 1996.

<sup>w</sup> <sup>x</sup> 3 J. Conklin, Capturing Organizational Memory, Readings in Groupware and Computer-Supported Cooperative Work, Morgan Kaufmann Publishers, 1993, 561–565.

<sup>w</sup> <sup>x</sup> 4 M. Day, J. Patterson, D. Mitchel, The Notification Service Transfer Protocol NSTP : Infrastructure for SynchronousŽ . Groupware, Hyper Proceedings of the Sixth Internationa World Wide Web Conference, 1997.

<sup>w</sup> <sup>x</sup> 5 A. Dix, Challenges and Perspectives for Cooperative Work on the Web, Proceedings of the ERCIM Workshop on CSCW and the Web, 1996.

<sup>w</sup> <sup>x</sup> 6 P. Dourish, V. Belloti, Awareness and Coordination in Shared Workspaces, Proceedings of CSCW’92, 1992, 107–114.

<sup>w</sup> <sup>x</sup> 7 W. Eckerson, Web-Based Query Tools and Architectures, available at: http:<sup>rr</sup>www.infospace-inc.com<sup>r</sup>docs<sup>r</sup>general<sup>r</sup>wqtinfo2.html.

<sup>w</sup> <sup>x</sup> 8 C.A. Ellis, S.J. Gibbs, G.L. Rein, Groupware some issues and experiences, Commun. ACM 34 1 1991 38–58.Ž . Ž .

<sup>w</sup> <sup>x</sup> 9 D. Flanagan, Java in a Nutshell, O’Reilly, 1997.

10 M. Goldberg, S. Salari, P. Swoboda, World Wide Web-Course tool: An environment for building WWW-based courses, Computer Networks and ISDN Systems, Proceedings of the 5th International World Wide Web Conference, 1996, 1219–1231.

<sup>w</sup> <sup>x</sup>11 S. Greenberg, C. Gutwin, M. Roseman, Semantic Telepointers for Groupware, Proceedings of the OzCHI ’96, Sixth Australian Conference on Computer-Human Interaction, 1996, 24–27.

<sup>w</sup> <sup>x</sup> 12 L.A. Guerrero, D. Fuller, CLASS: A Computer Platform for the Development of Education’s Collaborative Applications, Proceedings of CRIWG’97, 1997, 51–60.

<sup>w</sup> <sup>x</sup> 13 E.R. Harold, Java Network Programming, O’Reilly, 1997.

<sup>w</sup> <sup>x</sup> 14 D. Ingham, S. Caughey, M. Little, Supporting Highly Manageable Web Services, Hyper Proceedings of the Sixth International World Wide Web Conference, 1997.

<sup>w</sup> <sup>x</sup> 15 M. Pieper, D. Hermsdorf, BSCW for Disabled Teleworkers: Usability Evaluation and Interface Adaptation of an internetbased Cooperation Environment, Hyper Proceedings of the Sixth International World Wide Web Conference, 1997.

<sup>w</sup> <sup>x</sup> 16 M. Roseman, S. Greenberg, Building real time groupware with groupkit, a groupware toolkit, ACM Transactions on Computer Human Interaction 3 1 1996 66–106.Ž . Ž .

<sup>w</sup> <sup>x</sup> 17 J. Rumbaugh et al., Object-Oriented Modeling and Design, Prentice-Hall, Englewood Cliffs, NJ, 1991.

<sup>w</sup> <sup>x</sup> 18 M. vanWelie, A. Eliens, Chatting on the Web, Proceedings ¨ of the ERCIM Workshop on CSCW and the Web, 1996.

<sup>w</sup> <sup>x</sup> 19 A. Wooldridge, M. Morgan, M.C. Reynolds, J. Honeycutt, Using JavaSript, 2nd edn., QUE, 1997.

<sup>w</sup> <sup>x w</sup> <sup>x</sup> 20 Habanero Habanero. http:<sup>rr</sup>www.ncsa.uiuc.edu<sup>r</sup> SDG<sup>r</sup>Software<sup>r</sup>Habanero.

<sup>w</sup> <sup>x w</sup> <sup>x</sup> 21 BSCW Basic Support for Cooperative Work. http:<sup>rr</sup> bscw.gmd.de.

<sup>w</sup> <sup>x w</sup> <sup>x</sup> 22 Groupkit Groupkit. http:<sup>rr</sup>www.cpsc.ucalgary.ca<sup>r</sup>projects<sup>r</sup>grouplab<sup>r</sup>projects<sup>r</sup>groupkit.

<sup>w</sup> <sup>x w</sup> <sup>x</sup> 23 JWS Java Web Server. http:<sup>rr</sup>jeeves.javasoft.com.

![](/api/attachments/GK39EV7Z/fulltext/images/20e9581c550c7fac34b5267b769742ababcc283c2e4cea4eee0fb64d25a3bc51.jpg)  
Luis A. Guerrero is a Doctor of Engineering degree student of Computer Science at the Pontificia Universidad Catolica de Chile. He received a Bache-´ lor degree in Computer Science from the Universidad de Costa Rica, and a MSc degree in Computer Science from Instituto Tecnologico de Costa Rica. His´ research interests include the modeling, design and building processes of collaborative applications and object-oriented technologies.

David A. Fuller is an Associate Professor of Computer Science at the Pontificia Universidad Catolica de Chile. He received his PhD´ in Computer Science from Imperial College of Science, Technology and Medicine at the London University, England, a MSc in Computer Science from the University of California, Los Angeles, and a BS in Electrical Engineering from Pontificia Universidad Catolica de Chile. His research interests include collaborative´ systems, systems development, object-oriented frameworks and visual programming.
