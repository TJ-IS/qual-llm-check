---
otero_id: 19179
otero_key: "J47JYETJ"
title: "An investigation of a cost-effective solution for multimedia medical information management"
authors: "Ken Chee Keung Law; Horace Ho Shing Ip; Siu Lok Chan"
year: "1995"
journal: "Information & Management"
doi: "10.1016/0378-7206(95)00002-e"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Applications

# An investigation of a cost-effective solution for multimedia medical information management

Ken Chee Keung Law, Horace Ho Shing Ip, Siu Lok Chan

Image Computing Group, Department of Computer Science, City University of Hong Kong $^{1}$ , 83 Tat Chee Avenue, Kowloon, Hong Kong

## Abstract

The unstructured paper-based medical document contains heterogeneous data formats, such as text-based medical reports, graphics data, such as electrocardiograms, radiographic snapshots, such as Chest X-rays and MRI, possibly motion image sequences, such as angiograms, and verbal comments of physicians in surgeries. These multimedia information are currently stored in paper folders as print-outs, films, or tapes. The information has a high risk of being misfiled or wearing out. Advances in multimedia technology have made possible the authoring, storage and presentation of medical information in a systematic and easily-accessible way. This paper discusses the background and rationale that led to the design and prototyping of a computerized cost-effective multimedia medical document system.

Keywords: Multimedia information systems; Medical document systems; Hypermedia; User interface

## 1. Background

Hospitals in Hong Kong have a higher patient volume and more daily procedures than with other countries [2,15]. As a result, a large quantity of medical documents exist; they are distributed among many hospitals. Most of these documents are valuable to physicians, because they form not only the patient's medical history but also provide case studies for physician training. A typical manual medical document contains a hand-written report with medical symbols to describe the background, observation, and diagnosis. It is supplemented by information of different types and formats, such as laboratory result sheets, electrocardiograms (ECG) graphs, video tape or snapshots on echocardiogram, chest X-ray images, CT, MRI, etc. These pieces of information are stored in a large paper folder. To limit the storage, each medical document is generally kept chronologically for no longer than ten years. The information inside such paper-based documents is frequently unavailable, because it may be misfiled or lost [11]. Currently, access to the information from different places simultaneously is impossible, as there is only a single (master) copy of the document. Even when the medical document is available, poor organization and illegible handwriting may make retrieval of the desired information laborious and time consuming.

## 1.1. HIS vs imaging workstations

In the past decade, there has been a shift from manual to computerized approaches to the recording of medical information. The need for efficient access to the increased amount of medical information together with advances in information technology (IT) paved the way to innovative computerized medical information system (IS) in the last decade $[3,5,11,19]$ . These computerized IS are basically divided into two types: centralized medical IS, such as a Hospital IS (HIS), which store the medical information for global access, and a standalone workstation, which offers more flexible capabilities.

Most HIS allow only text and numerical data entries. Obviously these cannot always represent the precise details of a medical document, especially such items as X-rays. The medical imaging system on workstations, on the other hand, provides both normal patient medical information handling services and system platforms enabling the access and storage of medical images. These can be directly transmitted through a gateway to the host system. However, the cost for one workstation per physician is prohibitive; unlike text-based applications that can use a dumb terminal, there is need for color and high resolution graphics terminals for medical image diagnosis purpose, etc. Moreover, in order to enhance the workstations for sounds and video presentations, multimedia peripherals, such as sound and video capture board for these workstations, further add to the cost.

## 1.2. The advances of multimedia technology

The multimedia industry is becoming mature and is predicted to be a major growth area in future [7]. Generally speaking, multimedia refers to computer-controlled systems that combine a rich mix of text, graphics, still and moving pictures, music, and sounds. By combining a variety of formats, multimedia technology enables the conversion of information to a better format for immediate understanding.

In recent years, cost-efficient multimedia peripherals and tools have been introduced for a wide range of computers, especially in the PC range. With the decrease in the price, multimedia computers became “affordable”. Modern improvements include high speed, high quality display to provide good Graphical User Interfaces (GUI), large memory, and large storage capacity, cost-effective multimedia authoring tools, and peripherals, and also a high speed data communication network.

However, the lack of multimedia standards is a barrier for developers $[9,14,16]$ . General multimedia standards should include: still and moving images, audio, animation, programming interfaces to hardware, and the file format for exchange multimedia documents.

## 1.3. Goals and objectives of the investigation

An HIS with multimedia workstations would no doubt cost billions of dollars and many years of development. Indeed, most multimedia applications should be developed in an open, flexible, user-oriented, and cost-effective multimedia platform, such as a PC with a windows user interface. After seeking advice and suggestions from local physicians, we formulate a set of system requirements:

(a) It would be valuable to design a general purpose multimedia medical system architecture. A prototype system could then be implemented and extended to cover other medical records, such as those for oncology and dermatology.

(b) The system should support open systems interfaces to allow for a variety of available multimedia peripherals and software tools so that the users can benefit from advance in technology and upgrading.

(c) Each physician should possess one multimedia terminal to handle the local patient records. Medical records, on the other hand, could be exchanged easily between physicians.

![](/api/attachments/J47JYETJ/fulltext/images/451461faa21243b1a665328c9732a82d8ed64c684dd4b68d08a285ed9556f83a.jpg)  
Fig. 1. (a) Generic logical structure of a cardiac catheterization record; (b) Specific logical structure of a cardiac catheterization record.

(d) The system should provide a consistent GUI (Graphic User Interface) for multimedia information.

(e) The system should provide a standard method for interfacing different types of medical information in a consistent environment. Multimedia data can easily be captured/authored by a non-technical user. In addition, the multimedia data should be easy to change and delete.

(f) Since the details of the medical images are important for diagnosis, the quality of the gray scale should be at least 256 levels. Graphics terminals with high resolution 1024 × 1024 pixels with 24-bit colors would be ideal for the system.

(g) The system should provide query functions so that physicians can select patient's records using several keywords or according to the semantics of the multimedia data.

(h) The medical record should be portable to allow other physicians to retrieve the data from different computer systems.

## 2. Conceptual structure of a cardiac catheterization record

Here, we used the cardiac catheterization record (CCR) as a case study; it has diverse contents needing various media types and formats. Individual leaf nodes in the hierarchy represent information units containing various media type(s) of data that may include textual data (T), image (I), graphics (G), sound (S) and/or video (V). The data can be broadly divided into three categories: patient clinical, cardiac investigation, and management plan. The constituent elements are not always explicitly indicated in some existing (manually generated) CCR. However, we shall assume that all the CCR are composed of these components so that all CCRs pertain to the same document class. We describe the elements in a CCR in terms of the Office Document Architecture (ODA) standard [2]. The objective is to define an application profile in an ODA standard subset that is applicable to the medical domain and adds features that are required but not supported by the current version of ODA; e.g. including the handling of voice, annotations, forms, simultaneous treatment of objects, and video sequences.

The Content Node: This will either be Simple or Composite. It may be self-contained in the environment of document interchange. Each simple node represents an unbreakable unit of information in either one of the multimedia formats. Each composite node is composed of several instances of simple nodes. Each node is identified with a node ID. It can be a text-node, graphics-node, image-node, sound-node or video-node. The ODA that organizes the content (nodes) of CCR can be represented by 4 kinds of structures namely, Generic and Specific logical structure, Generic and Specific layout structure.

Logical Structure: The logical structure provides a way of organizing the content of the document; it is intended to correspond closely to those aspects of the document structure related to the functional semantics of the document. The relationships of the information nodes can be defined as REQ (Required), SEQ (Sequence), REP (Repeat), CHO (Choice) and OPT (Optional); they may be used in combinations. Fig. 1a shows the generic logical structure of a CCR as a hierarchy. A specific logical structure of a CCR for Patient A is derived from the generic logical structure of the CCR. It represents an instance of this CCR report class that describes the details of a specific CCR in the real world. An example in Fig. 1b shows that the CCR contains exactly two sets of Chest X-ray data.

Layout Structure: The layout structure of the CCR provides a method of organizing the content of the document into a layout appearance that can be displayed on the screen. As the media type, sound, and video are still not supported by the latest ODA version, a modification and subset of the standard would be required. This is termed the Document Application Profile. In this, we adopted the processable document model of the standard so that the document originator has to specify only the logical structure but allow future modification of the document content and layout. Furthermore, there may be possible enhancements to the layout structure by using hypermedia nodes and links, as well as temporal concepts.

## 3. Modelling a hypermedia document

Hypermedia is a way of representing and accessing information. It views the information space as a graph whose nodes store information and whose arcs represent semantic relationships. In a hypermedia document, a hyperlink corresponding to embedded pointers would be marked by a dependent marker such as highlighting linked area in the document (see Fig. 2). When a hyperlink is activated, the system extracts its destination node from the hyperbase and presents it to the user with associated method.

## 3.1. Definition of media-nodes

In the HyperCardiac system, the content of a node can be a passage of text, a sound clip, a picture, an image, animation sequences, or a motion video clip as atomic information in the CCR document. These are referred to as simple media-nodes, or as a combination of simple media-nodes: a composite media-node. Each simple media-node is a complex object having its own internal data structure and procedures that define the methods for operations and means of presentation of its content.

A composite node is self-defined according to the categories of information in the CCR document. These are like the collections in a hypermedia system that classifies information into related sets of nodes. Thus, a composite node serves as a gathering of related simple nodes that limit the user's view of the information to the most relevant part, while hiding the rest. For example, Chest X-ray (C201) is a composite node which might contain three simple image-nodes (C201-I001, C201I002 and C201I003) and a text-node (C201T001). The attributes of the simple medianode can be Node-ID Node-Name, Node-Type, Node-File-ID, Node-Format, Node-Author, Node-Keyword (for keyword search), Node-Semantic (for content search), Node-Status, Node-Access (PUBLIC/PRIVATE or READ ONLY/WRITE), etc.

## 3.2. Definition of hyperlinks

Hyperlinks are pointers connecting medianodes that have some semantic relationship in

![](/api/attachments/J47JYETJ/fulltext/images/8983f616fed6cc58a3bec45ddd860eac401ac03cb20b6b6d6f5636ab428b8c99.jpg)  
Fig. 2. A hypermedia CCR document is formed by defining hyperlinks between media-nodes.

HyperCardiac. They provide association to other media-nodes and data items, such as annotations or node-semantics. Since the media-nodes in a CCR document are on the same levels, a one-directional referential link is adopted in the HyperCardiac system. Referential links generally have two ends, and are usually directed [6,18]. This link is termed a “hyperlink source”. It may be a geometrical region in a digitized picture, a set of continuous characters in a text passage, or a time duration in a clip of sound or video sequence. The other end of the hyperlink is called the “hyperlink destination”, which is either a “hot region” or an entire media-node. Like medianodes, hyperlinks are defined by a set of attributes, such as Link-Type (in the form of MN: TT (Text-to-Text), TG, TI, GG, GI, TV, etc.), Link-Source, Link-Destination, Link-ID, Link-

Name, Link-Author, Link-Display (LINK-TO-ANNOTATION, REPLACE, GO-TO, SPATIAL-TEMPORAL, etc.), Link-Status (SHOWN or HIDDEN), Link-Access (PUBLIC/ PRIVATE or READ ONLY/WRITE), etc.

There are 4 types of hyperlink: (a) Link-to-Annotation, which allows a transient display of an annotation node and then return to the source node; (b) Replace, which allows a source node to be detected and replaced by a destination node; (c) Go-to, which allows a source node to be retained while activating a destination node and (d) Spatial-Temporal Hyperlink, which handles active media, such as digitized sound, animation, and motion video sequences that involve spatial and temporal relations; for this, necessary synchronization between any two pieces of multimedia information are introduced.

![](/api/attachments/J47JYETJ/fulltext/images/39f9cc2b702efd173875771ec7c097bad24d7f8e50793bd25c881a12dbe14b80.jpg)  
Fig. 3. Presentation scenarios of a CCR document.

## 3.3. Presentation scenario

The media-nodes are stored as separate media files or as unformatted data. The description of the hyperlinks connecting media-nodes is separated from that of the media-nodes themselves and it is stored in the hyperbase. This stores the presentation scenario of each CCR document, which is a collection of hyperlinks to show the possible paths of media-nodes presentation [10]. Several users can define their own presentation scenarios to allow them generation of customized documents from multiple functions. Furthermore, information segments can be referenced from different places and so ideas can be expressed with less overlap and duplication. Fig. 3 illustrated the media-nodes and the hyperlinks that form the presentation scenarios for a CCR document.

## 4. Overview of software architecture

The design of HyperCardiac is independent of any computer platforms but it takes into account cost-effectiveness and computer resources aspects of hardware available to local medical officers. There are three subsystems: the Database Subsystem / Server, the Authoring Subsystem, and the Presentation Subsystem. A HyperDocument Interface (HDI) is introduced; this lies between the subsystems in order to achieve module independence. (see Fig. 4). Other system components are the Hyperbase, which stores the hyperlinks information to form presentation scenarios, and the Database, which is the physical repository for the media content in the CCR document. In addition, a Windows Layer is incorporated to provide a multimedia user interface. Media-node to Window Object Mapping is used to provide an effective hypermedia browsing and authoring mechanism.

## 4.1. HyperDocument Interface (HDI)

The introduction of the HyperDocument Interface (HDI) serves to achieve the design objectives of 'Modularity' and 'Extendibility'. It is necessary to define a standardized, accurate, and reliable communication interface among the subsystems so that they can be operated independently without interfering with each other. In the HDI design, the internal structure of physical database and hyperbase would be hidden to the application subsystems. They would access the CCR document data items by sending messages that invoke the DB functions provided by Database Subsystem/Server and retrieve the required information through HDI. In other words, only the DB Server can interact with the physical hyperbase and the database. There are two advantages in such a design. (1) As long as the CCR document structure remains the same, the change of physical database or DBS will not affect the other application subsystems and (2) New application subsystems can be added to HyperCardiac easily, without knowing about other subsystems.

## 4.2. Database Subsystem / Server (DBS)

The Database Server/Subsystem (DBS) provides the retrieval and storage services for the subsystems. It forms the basis of the HyperCardiac system. The choice of a data model for the multimedia data depends on the behaviour of the media-node itself. It is found that media-nodes are dynamic, having temporal-spatial relationships to other nodes. The pure relational data model and the simple node and link model in a hypermedia system is not rich enough to support the storage and information management as well as the presentation tasks required by multimedia applications $[1,4,7,8,13]$ . On the other hand, an object-oriented data model has the problem of poor performance and divergent SQL standards $[12]$ . Moreover, the fundamental difficulty in handling multimedia data lies in the problem of handling the rich semantics that is contained in multimedia data $[17]$ . In the design of the HyperCardiac system, a pseudo-object-oriented approach of mapping the media node data to the Media-Window objects was adopted. This allows the media data to have structural and behaviour properties and yet still be controlled and presented by the Windows GUI. On the other hand, the design of the HDI in the HyperCardiac sys-

![](/api/attachments/J47JYETJ/fulltext/images/6556d9dbcc682995cf364866b4af8d5ea97f5f0bea29c99905c37cd2fa60d76c.jpg)  
Fig. 4. Overview of architecture for HyperCardiac system.

tem is open to any physical database storage so that subsystems can be freely built on the architecture now being designed. Since new generation of multimedia data models and DBMS are not yet available, an optimal design of a database for the multimedia medical documents must be selected based on one of the existing DBMS, within the crucial factors of stability and availability. Thus, a hybrid approach was taken to integrate the idea of relations, hypermedia, and objects in a traditional RDBMS to demonstrate the feasibility of the idea.

![](/api/attachments/J47JYETJ/fulltext/images/b5babe14d67cdd4a06d6f3efac7114299675af11ed690573472efaec5a96bbbf.jpg)  
Fig. 5. Architecture of the DBS in the HyperCardiac system.

## 4.2.1. Hybrid DBMS approach

With these considerations, a hybrid database is designed for the DBS of the HyperCardiac system which handles:

(1) only the structural properties of the media-node object; i.e., the attributes of the objects. The behaviour properties of the objects on each subsystem, i.e., the methods, could be maintained through a Window Object Mapping Mechanism. The mechanism would inherit the properties of the window object class and its associated methods for the subsystem operation.

(2) the relationship of pieces of media-nodes inside or outside the documents, in the forms of relational table(s). Query on the relationship of the text media data would be executed by standard SQL statements. The query of the multimedia data would be made possible by using a keyword match or a semantic-description retrieval of the media nodes.

(3) the hypermedia data of the CCR document by means of the links and nodes in the relational tables that form the hyperbase. The hypermedia also makes possible the spatial-temporal relationship between media-nodes.

## 4.2.2. Overview of the DBS

Fig. 5 shows the architecture of the prototype DBS in the HyperCardiac system. It was built on top of an RDBMS. The DBS provides DB functions that handle the CCR documents through the HDI of the HyperCardiac system. Each CCR document is called a “patient folder”. Subsystems can request the DB services to manipulate this through communication messages to the DBS. It would read or write the patient folder from or to the physical database to the HDI according to the request. The architecture of the DBS could be divided into two parts: the Document Manager and Physical Storage.

The Document Manager: This provides services for query and storage of the hyperlinked patient folder. These functions are handled by the Query Manager (DBS/QM) and the Storage Manager (DBS/SM). The first provides a set of DB functions that can be used for queries, retrieval, and updating the patient folders. The second provides services for disk management and multimedia data storage. Whenever a patient folder is selected upon query, a HDI for a patient folder will be initialized. Whenever there is a request for updating, information from the user via the HDI is placed in physical storage. The user invokes the query through the DB functions interface, as shown in Fig. 5 There are several DB functions provided to the subsystems: (a) Check Patient Folder Existence, (b) Make Query and Browse on the Patient Folders, (c) Retrieve Patient Folder (d) Maintain Patient Folders.

Physical Storage: The Media File Mapping Mechanism allows the storing of the media-nodes on separate files that are mapped to the corresponding values of an attribute in the media tables. The handling of media-nodes on separate files has its pros and cons. The main drawback is that data integrity is more difficult to maintain. The positive side is that it allows the physical storage implementation to be performed easily and with flexibility. The media-files can be stored as the standard formats, and this allows media editing by the commercially available editors and media data interchange between systems becomes easy. In addition, the implementation of different media data stored in different mediabases is rather simple. Since the multimedia data are large, a standard magnetic disk would be insufficient to handle its volume. Therefore, optical disk can be used to store the dynamic media data such as sound and video files, while the traditional magnetic disk can be used to store the static data.

## 4.3. The authoring subsystem (AUS)

The AUS provides a tool for the user to capture raw media through various editors and to allow the definition of hyperlinks to form presentation scenarios for the CCR document through the hyperlink editor. The design of a customized

![](/api/attachments/J47JYETJ/fulltext/images/aade7bb6d500f919d1abe775d6d2bafbefdbeac93b015c78bc62f72582afe408.jpg)  
Fig. 6. Architecture of the AUS in the HyperCardiac system.

AUS provides the following characteristics: easy of use for non-technical users, providing a consistent platform for multimedia data entry, hardware portability, allowing customised presentation scenario, and hypermedia features.

The AUS consists of two parts: the Media-Node

![](/api/attachments/J47JYETJ/fulltext/images/aa2f0ab5f610b15ca11ca03a4787501e64eb51bfac8477ad089188b58c4283c2.jpg)  
Fig. 7. DOT dialog (UI design) of AUS in the HyperCardiac system.

Manager, which captures and registers the media-nodes, and the Hyperlink Manager, which creates and registers the hyperlink relations (see Fig. 6).

The Media-Node Manager: this governs the capturing of media-nodes to form a CCR document. Once a CCR document is selected through the DB functions interface and placed in the HDI, the authoring process is undertaken through a DOT dialog (Fig. 7)

Once a media-type is selected in a composite media-node, say "Image" of "Chest X-ray", the media-node assigns a new Node\_ID; this is assigned sequentially for each media type. Subsequently, the corresponding media-editors associated with the media-nodes would be activated. When a media object (node) is activated in the AUS (client), the media editors (server applications) would be linked for the manipulation of the object. After capturing the media-nodes through the media editors, the media-node would be saved as a media file in the HDI using the same naming convention (Node\_ID). The attributes of the media-nodes such as Node-Name, Node-Type, Node-Keyword, Node-Semantic, Node-Status and Node-Access would be registered. The Media-Node Manager also provides operations for modifying, deleting, and browsing the media-nodes from the HDI.

The Hyperlink Manager: This constructs the hyperlink tuples in the hyperindex files in the HDI. These link the source and destination media-nodes. A set of hyperlink-editors are designed for the display of the media node; they allow the marking of linked-areas in the media-nodes. The linked-area of the media-nodes can be varied according to the nature of the media types. For Character-based media, i.e., text and form nodes, they are denoted by highlighted words. For Picture-based media, i.e., image and graphics nodes, they are denoted by rectangular regions on the picture. For Active-media, the data is denoted by a period of time. The marking of linked-area for passive media would be simply provided by dragging the hot area of the media-node on screen using a mouse. For dynamic media, the linked area is registered through the hyperlink attribute input dialog. For instance, to define a hyperlink in a chest X-ray image node to an echocardiogram text node, hot regions can be defined by dragging a rectangle box with using a mouse onto the desired position, say the tumour issues. User can then specify the destination node as an echocardiogram text. Upon the creation of each hyperlink, attributes such as the LINK-NAME, LINK-STATUS, LINK-DISPLAY and LINK-ACCESS would be input by the user to define the properties of the hyperlink.

![](/api/attachments/J47JYETJ/fulltext/images/e25da6e4c145a8181aab267cece974a4ad4f9fbaa562fe65224afffecf59e6cd.jpg)  
Fig. 8. Architecture of the PSS in the HyperCardiac system.

## 4.4. Presentation subsystem (PSS)

The Presentation Subsystem (PSS) of the HyperCardiac system presents the hypermedia CCR document according to the user customized presentation scenarios defined in the authoring process.

Fig. 8 shows the PSS architecture in the HyperCardiac system. The PSS consists of two parts: the Scenario Manager that controls the path of the media-nodes and the Annotation Manager that allows the creation of multimedia personal annotation to the nodes.

Scenario Manager: This is used the purpose of controlling the path of presenting the data in a CCR document. Once the user has chosen a media-node from the DOT dialogue, the presentation scenario would be invoked. The user accesses the media-nodes in two different ways: free retrieval through the DOT dialogue or by activating the hyperlinks of the media-nodes. If the hyperlink is activated, the Scenario Manager would seek the destination media-node from the hyperindex lists. This node is then displayed on a window (except for the Link-Display = REPLACE command) according to the attributes of the node and its hyperlinks.

Annotation Manager: This allows the media-node to be associated with multimedia comments or annotations. This Node-Semantic can then be used as for public text annotation in order to increase understanding of the media-node. In addition, in the PSS, a physician viewing the document can introduce his or her own set of private annotations. Whenever a physician registers in the system and selects the right record, a personal set of private annotations about the medical record would also be returned whenever he or she is browsing through the document. The physicians can freely choose the appropriate media types for the annotation. Such a design broadens the value of the medical records and allows them to be dynamic instead of static in nature.

## 5. Implementation issues

The HyperCardiac was built for cost-efficiency, open standards and modular application platform. Taking theoretical and practical thoughtfulness, the PC was selected as its development and operating platform. It is important that the it is suitable in both the HyperCardiac prototype and for the full system implementation.

## 5.1. Hardware requirements

The HyperCardiac system uses an IBM compatible PC486 with 8 megabytes of memory. It requires 3 megabytes of hard disk storage for the document system setup. Each cardiac catheterization record requires 1 to 2 megabytes of hard disk for storage. The storage size per record is determined by the number of image files and video files in the record. The monitor has a super VGA graphic board which supports $1024 \times 768$ resolution with 64 thousand colors display. This resolution and the number of gray levels for the image are adequate for cardiologists. The multimedia peripherals are also based on the MPC specifications and those that provide the Media Control Interface $^{©}$ (MCI) device drivers following the Application Programming Interface (API) standards in the Multimedia Extensions of MS-Windows $^{©}$ [9]. An add-in sound board is attached to the computer system for sophisticated presentations. There is also a video board and a VCR that allow the capturing of video sequences.

## 5.2. Software requirements

Again, a base operating system (OS) was chosen for the HyperCardiac system in the PC environment. Microsoft Windows $^{©}$ 3.1 (MS-Windows $^{©}$ ), is placed on top of MS-DOS $^{©}$ which offers considerable advantages to both users and software developers over the conventional PC environment. Thus the design places the advanced features, such as GUI, multitasking and the hardware independence, in a single PC operating environment.

A set of media-editors is in addition required for capturing and editing raw multimedia data

![](/api/attachments/J47JYETJ/fulltext/images/5fd55ef9c4e83e0aefcc433daa28ae70c3bfbef194766d05156153bb609d5c6a.jpg)  
Fig. 9. System architecture for the development of HyperCardiac.

during the authoring process. CCR Document originators can produce pieces of media-nodes (text, graphics, digitized images, sound, animation, video) through various media editors and link them in terms of higher-level document concepts. The HyperCardiac system utilizes the media-editors, either commercially purchased or self-defined, under the Object Linking and Embedding $^{©}$ (OLE) mechanism provided by MS-Windows $^{©}$ . Under the OLE mechanism, control of the flow and naming and formatting of medianodes in the editor (server application) can be easily controlled by the HyperCardiac system (client application). Thus, users can choose the appropriate media editors to capture the data. Fig. 9 shows the operating system architecture for the HyperCardiac system.

![](/api/attachments/J47JYETJ/fulltext/images/7504e05947ee7093eab65802b7b3ddfc824951981ec74e6849f21e06800b8f80.jpg)  
Fig. 10. Multiple document interface of the PSS.

## 5.3. System features

The HyperCardiac system is operated in MS-Windows $^{©}$ with the following features:

(a) Multiple Document Interface (MDI): The multitasking feature of MS-Windows allows the HyperCardiac system to be operated on the Multiple Document Interface (MDI). This allows the users to work simultaneous with many open Media-Windows. Each CCR document would be mapped to a frame window. Within the frame window's client area is an invisible window, the MDI client window, that holds the MDI child windows; these would be the Media-Windows in the HyperCardiac system. The MDI provides good management of the multiple media-nodes on the screen. Fig. 10 shows such a presentation scenario of a CCR document in the MDI environment.

(b) Device Independence: The HyperCardiac system makes use of the Media Control Interface $^{©}$ (MCI) API standard of MS-Windows $^{©}$ . The MCI is a software layer that sits between Windows and the hardware devices [9]. Through this interface, modules in the HyperCardiac system can interact with any multimedia hardware, such as sound cards, video cards and CD ROMs; this provides a MCI-aware driver through a set of MCI software routines. Hardware modifications would not affect the flow of the program. The only adjustment needed would be for new device drivers installed to replace old ones.

(c) Document Organization Tree (DOT) Dialog: Because of the high volume of information in a CCR document, the user may find it difficult to access the information using a pull-down menu or list box. This situation is especially serious in the authoring process, where users must keep alert and remember which information has been processed. The logical organization tree of the CCR document is helpful in giving both an overview of the CCR documents in the HyperCardiac system and showing the presence of the media-nodes. On the basis of this, a Document Organization Tree (DOT) Dialog is designed for the medianodes of all subsystems. This serves three purposes:

(a) it specifies the information content, media types, and associated methods required of the CCR.

(b) it defines the logical relationship and cross-referencing between the different parts of the CCR;

(c) it provides a “map” that facilitates the retrieval of specific pieces of information and allows “navigation” through different medianodes by a physician.

The DOT dialog will show the logical organization of the CCR document, and thus the relationship between composite nodes. Each leaf node of the tree would associate with a push button. Users can select the desired media-node by clicking the push button with the mouse. The DOT dialog design provides a direct user interface and reduces cognitive overheads on the media-node selection.

(d) Hypermedia Concept: The concept of hypermedia is implemented in the system. Windows on the screen are associated with nodes in the database, and links are provided between these nodes, both graphically (as labelled tokens) and in the database (as pointers). A node is a unit of information that might be a text paragraph, an image, a graphics picture or even a video sequence. Links are usually denoted by words highlighted in a text paragraph or hot regions in an picture. When a link is activated, a jump is made to the referenced link. Hypermedia allows users to retrieve the information non-linearly with a predefined logical sequence. Three kinds of links are implemented in this system: text-to-text, text-to-image, and image-to-text. Consequently, a chest X-ray image can link to an extra text paragraph for its diagnostic report, etc., and also be associated with an ECG or the patient's background information. Each node can be defined with multiple links to other nodes. The hyperlink information is stored in an index table and it can be updated.

## 6. Conclusions

Many physicians are impressed with the prototype of this new approach for manipulation and presentation of medical records. The CCR documents are particularly well-suited for manipulation. The design of the HyperCardiac system is both requirement-driven and technology-driven. On the physicians point of view, the system is tailor-made because it can fulfill most of the requirements and bring the manipulation of the CCR document into a new era. Cost effectiveness is another important issue. To fulfill local requirements, the low cost PC platform under MS-Windows $^{®}$ environment was deemed necessary, with manipulation of multimedia medical information quickly and accurate.

The capability of this system can be extended by connecting systems through public switched networks so that medical document can be shared between physicians at different hospitals easily through modems and telephone lines. This is important because current manual-handled CCR document require a great deal of time to access at remote sites. On the other hand, each CCR document could be stored in a floppy diskette or even an optical disk so that the document can be carried by the patients. This could speed up the diagnosis process in an emergency. The system is also used for demonstrations, training, etc.

This research demonstrates that the multimedia technology is well-suitable to be applied on the field of complex documents. A prototype had been implemented to demonstrate the research idea and it allows the capturing, formatting, and storing of medical documents in a PC windows platform. The design is generic and so the emphasis had been made on subsystems and multimedia hardware independence.

## 7. Acknowledgement

The authors would like to thank our medical collaborators Dr. Chau Wan Yeung of Kwong

Wah Hospital and Dr. Wong Chun Por of Ruttenjee Hospital who have given us valuable professional advice and clinical data.

## References

[1] Agosti, M. et al., “A Hypertext Environment For Interfacting With Large Texual Databases”, Information Processing & Management, 371–381, Vol. 28, No. 3, 1992.

[2] Appelt, W. et al., “The Formal Specification of the ISO Open Document Architecture (ODA) Standard”, The Computer Journal, 268–279, Vol. 36, No. 3, 1993.

[3] Barnett, G.O., “The Application of Computer-Based Medical-Record Systems in Ambulatory Practice”, Computers And Medicine – Implementing Health Care Information Systems, 85, 99, Springer-Verlag, 1989.

[4] Blattner, M. et al., “Messages, Models, and Media”, Multimedia Review, 15–21, Vol. 3, No. 3, Fall 1992.

[5] Cheung, A.W.N., “Princess Margaret Hospital-Hospital Information System: Computer System Selection”, Hong Kong Medical Informatics Conference Proceeding, 120–124, 1990.

[6] Conklin, J., “Hypertext: An Introduction and Survey”, Journal of IEEE Computer, 17–41, September 1987.

[7] Coyne, J.P., “Relational Databases And Multimedia Repositories”, Multimedia Review, 24–29, Fall 1991.

[8] Coyne, J.P., “The Need for a Multimedia Data Model”, Multimedia Review, 64–67, Vol. 3, No. 3, Fall 1992.

[9] Elliott, S.D., “A Primer on Multimedia Standards”, Multimedia Review, 30–43, Vol. 3, No. 2, Summer 1992.

[10] Fujikawa, K. et al., “Multimedia Presentation System ‘Harmony’ With Temporal and Active Media”, USENIX, 75–93, Summer 1991.

[11] Karmouch, A. et al., “A Multimedia Medical Communications System”, IEEE Journal on Selected Areas in Communications, Vol. 8, No. 3, 325–339, April 1990.

[12] Kim, W., “Object-oriented Database Systems: Strengths And Weaknesses”, Journal of Object-oriented Programming, 21–25, July/August 1991.

[13] Klas, W. et al., “Visual Database Need Data Models for Multimedia Data”, Visual Database System, 433–461, IFIP, 1989.

[14] Kretz, F., “Coded Representation of Multimedia and Hypermedia Information Objects: Towards the MHEG standard”, Signal Processing: Image Communication, 113–128, 1992.

[15] Mak, C., Smith N., “Implementation Issues of Hospital Information Systems: A Hong Kong Perspective”, Hong Kong Medical Informatics Conference, 113–119, 1990.

[16] McInerny, M., “Multimedia Data Formats: Issues and Instances”, Technical Report from Information Technology Center, CMU-ITC-098, Carnegie Mellon University Press, June 1991.

[17] Meyrowitz, N., “Intermedia: The Architecture and Construction of an Object-oriented Hypermedia System and Applications Framework”, OOPSLA'86 Proceedings, 186–201, September 1986.

[18] Tomek, I. et al., "Hypermedia-Introduction and survey", Journal of Microcomputer Applications, 63–103, 1991.

[19] Watson, D.S. et al., “Working With MUFFIN: A Clinical User’s View”, Hong Kong Medical Informatics Conference Proceeding, 8–11, 1990.

![](/api/attachments/J47JYETJ/fulltext/images/5ad467f53d22ea776a05a038df8a6c07fc68ffd2bc41c4a2d5f29fce82dd0e3d.jpg)

Ken Chee Keung Law received his BSc in Chemical Engineering from the National Cheng Kung University, Taiwan, the MSc in Process Analysis and Development from the University of Aston in Birmingham, and the PhD from the North East London Polytechnic in Computer Control in 1974, 1975 and 1979 respectively. He joined the Engineering Department, Cambridge University as a Computer Officer in 1981, specialized in computer

graphics, CAD systems and manufacturing numerical control systems. He joined the City University of Hong Kong as a university lecturer in 1991. His research interests include computer graphics, multimedia systems and medical systems.

![](/api/attachments/J47JYETJ/fulltext/images/a7d10bbb6727cf4d88dec4710b5cf57d3ffc8d15c13919a6ae5de3f0c8f19ad3.jpg)

Horace Ho Shing Ip received the BSc degree in Applied Physics and the PhD degree in Image Processing from University College London, UK, in 1980 and 1983 respectively. Since 1991, he has been a university senior lecturer at the City University of Hong Kong where he found and leads the Image Computing Research Group. He has published research papers in machine vision, computer graphics, image analysis processing and multi-

media information system. Dr. Ip is the founding Chairman of the Hong Kong Society for Multimedia and Image Computing, serves in the Council of the Hong Kong Computer Society and in the Governing Board of the International Association of Pattern Recognition.

![](/api/attachments/J47JYETJ/fulltext/images/d9260a3d61228f5a2c03dc28fa2db55c999502450e8fe975850547b16d08cefb.jpg)

Siu Lok Chan received the BSc in Computer Science and the MPhil degree in Multimedia Computing from the City University of Hong Kong, in 1990 and 1993 respectively. He is currently a PhD degree candidate in the Department of Computer Science at the City University of Hong Kong. His research interests include multimedia document systems, information retrieval and user interface.
