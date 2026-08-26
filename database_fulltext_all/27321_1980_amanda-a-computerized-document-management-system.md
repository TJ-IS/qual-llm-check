---
otero_id: 27321
otero_key: "226Q9N2X"
title: "AMANDA: A Computerized Document Management System"
authors: "Ronald Schwartz; Joan Fortune; Julian Horwich"
year: "1980"
journal: "MIS Quarterly"
doi: "10.2307/249319"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
AMANDA: A Computerized Document Management System  
Author(s): Ronald Schwartz, Joan Fortune and Julian Horwich  
Source: MIS Quarterly, Vol. 4, No. 3 (Sep., 1980), pp. 41-49  
Published by: Management Information Systems Research Center, University of Minnesota  
Stable URL: http://www.jstor.org/stable/249319  
Accessed: 20-10-2015 14:54 UTC

Your use of the JSTOR archive indicates your acceptance of the Terms & Conditions of Use, available at http://www.jstor.org/page/info/about/policies/terms.jsp

JSTOR is a not-for-profit service that helps scholars, researchers, and students discover, use, and build upon a wide range of content in a trusted digital archive. We use information technology and tools to increase productivity and facilitate new forms of scholarship. For more information about JSTOR, please contact support@jstor.org.

# AMANDA: A Computerized Document Management System

By: Ronald Schwartz
Joan Fortune
Julian Horwich

## Abstract

AMANDA, an acronym for Automated Management of Document Access, is a completely online intraorganizational document based retrieval system. It is both a reference system, in that an indexed summary or surrogate of a document is created and stored for retrieval by computer, and a full text system, and in that the complete document can be entered, searched, and retrieved if needed.

AMANDA is capable of handling a wide variety of document types (e.g., letter, memo, report, contract, reprint, book) by tailoring an organizational communication. A system which widens the channels of communication and helps to integrate disjoint functions provides large and complex organizations the means of over coming a basic operational deficiency.

AMANDA is currently in active use within several departments at American Critical Care, a division of American Hospital Supply Corporation. Departments at other divisions access the system from remote sites.

Keywords: User orientation, applications development, decision support system, interactive software, online system, database systems, management information system, information systems design, information systems, document management, records management, filing

ACM Categories: 3.70, 3.74, 3.75

Mankind has devoted a good deal of time and effort in the last thirty years to generating information without giving adequate attention to how it should be processed and stored for convenient retrieval. Finagle's Law succinctly captures the essence of the problem:

The information we have is not what we want; the information we want is not what we need; and the information we need is not available [1].

We are all vaguely aware of the reality of the “knowledge explosion,” and suffer under its impact without fully appreciating the magnitude of the problem. A few statistics should illustrate the point. One half the present body of knowledge has come into existence in the last twenty years, and five to ten times more information is available on a given subject area than thirty years ago. About five million scientific and technical articles are published annually in about 100,000 journals. The world’s output of new books is about 1000 titles per day. The world generates new scientific and technical information at the rate of about six million published pages a year [3]. These data refer to published materials alone, and for some of this we do have serviceable means of access though libraries and online bibliographic retrieval systems. But published pages comprise only a small fraction of the world’s output of information that merits storage for potential retrieval, and accessibility to this material is totally inadequate. The quantities of information are so vast that just storing and retrieving the information generated within small organizations taxes the capacities of the most resourceful keeper of the files. Yet retrieval of this internal documentation is often more important to the effective operation of an organization than is retrieval of the published literature.

Our article is getting the best of us because manual filing systems simply do not work for this purpose. Manual systems are inadequate for handling the expanding volume of paper and the variety of ways it has to be retrieved, no matter how ingeniously one applies color coding schemes, edged-notched cards, index card cross reference systems, or thoughtful subject headings to the problem.

This inadequacy is documented in a literature survey reported in the MIS Quarterly by Swanson and Culnan [4]. These authors presented a classification scheme with examples from the literature for what they refer to as document based information systems. These are distinguished from the more familiar database management system (DBMS) in which the stored elements are individual data items. In contrast, the document based system uses the document itself as the basic unit of retrieval.\*

Review of the literature for references to various document based systems resulted in examples of both intraorganizational systems, i.e., internal to the organization, and extraorganizational systems, i.e., external to the organization. While several extraorganizational systems were identified which provide broad coverage and convenient access to documents in the public domain (e.g., SDC Search Service, DIALOG, New York Times Information Bank, and LEXIS), intra-organizational systems with comparable scope and utility were not found. Rather, the intra-organizational document based systems described in the literature were limited to either those tailored to meet specific management control needs (e.g., control of project documentation), or simpler operational control objectives (e.g., processing of registration forms for a convention).

It is curious, indeed, that so little effort has been directed to creating general purpose storage and retrieval capability for intraorganizational documentation, given the magnitude of the need and the broad recognition of the inadequacy of conventional, manual approaches. Finagle's Law holds true because professionals and managers do not have available a system which enables convenient access to the massive amounts of diverse kinds of material with which they are confronted. The paper in filing cabinets stands as a largely untapped resource.

Recognition of this serious deficiency in intraorganizational document retrieval capability led American Critical Care to design such a system. This article describes the results of these efforts in detail, up to the current stage of evolution of the system, as well as some plans for future enhancements, and an evaluation of the impact of the system on the organization. The description is preceded by a brief excursion into the logic of document filing itself, which is intended to show why all manual filing systems are fundamentally self-limiting and inadequate, and only computer systems can meet the demands for comprehensive document management.

## Manual Document Filing

The study of how people go about filing documents led us to consider strategies of filing as levels, with increasing complexity as one moves to higher levels. We have defined four such levels. The first, Level One, may be described as follows: arrange documents in sequence, without reference to chronology or subject. This is the simplest possible approach—namely, just make a stack or drawer of documents arranged in order of arrival, or in any other random order. (Actually, there is a lower level, pre-level one, which is to keep papers strewn about without placing them in a pile. While this is a popular storage strategy and has the advantage of using physical location to facilitate retrieval, it cannot be dignified by being elevated to a level of file organization.)

Level One characterizes most “in-baskets” as documents waiting to be reviewed, and more significantly, in terms of retrieval, it characterizes information that awaits processing. Level One is further characterized by sequential searching—one scans the stacks, document by document, until the desired information is found.

The principal advantages to Level One filing are simplicity, timeliness, and general reliability. Filing is simply adding to the stack. The most timely information is close by and retrievable without intermediate processing. Reliability resides in the notion that if one looks long enough one will surely run into the information eventually. However, depending on the height of the stack, retrieval degrades rapidly.

Level Two filing may be described as follows: arrange documents in sequence by chronology. This is the familiar chronological file or daybook approach. At this level a limited random access approach to searching can be employed. Documents can be retrieved by knowing either the exact or approximate creation date. The obvious advantage is that the whole file need not be searched if there is some known point of entry by date.

The disadvantages to a strictly chronological file are:

Limited search access. Searching is limited to knowing the date, approximate date, or searching sequentially through all documents, as in Level One.

Limited scope. Chronological files are most amenable to correspondence where dates are especially noteworthy. Documents for which topic, not date, is likely to be recalled, are not suited to this approach.

Level Three filing is “dictionary” filing, which puts like or related things together. “Like” may refer to the form of the document (e.g., laboratory notebooks, computer printouts, or reports), or to its content. Level Three files are almost always alphabetical. They require a decision (“what else is this like” in form or content), and they require either accurate recall for retrieval, or a sequential scan if recall does not work. That is, one must either remember how the desired information is stored to access it directly, or else scan the file sequentially as in Level One. Generally there is only a single subject descriptor, which makes the filing decision simple, but makes retrieval tedious and time consuming.

Attempts to expand Level Three filing to provide additional access points include making multiple copies of a document, and filing each copy according to a different descriptor. However, this solution degrades rapidly, in the case of documents covering a wide range of subjects. In short, Level Three offers limited random access searching capabilities, but is inadequate for large files of complex information.

Level Three filing could be markedly improved if separate files were made for select combinations of descriptors along with a file for each descriptor. This would enable narrower or more defined searching (e.g., all advertising material related to bonds), along with the broader searching capability of the single descriptors. This filing approach requires anticipation of the retrieval strategy in choosing probable combinations of descriptors for separate files. Beyond this, one could set up files for all combinations of descriptors so that no anticipation is necessary, and every possible search is maximally available. If the average document is assigned ten descriptors, then each document would require 1,023 filings. Clearly this becomes tedious in short order, and unduly burdens the storage side of records management.

Level Four, “encyclopedic” filing, represents an effort to approximate this kind of retrievability more efficiently than Level Three. Level Four filing also puts similar items together, but adds indentation. Broad descriptors are successively subclassified into narrower descriptors, producing a hierarchy, or tree, of subject descriptors.

The branch of the tree given in Figure 1 illustrates a part of a filing hierarchy for documents on drug products in a pharmaceutical company. A wholly different tree structure would have resulted if different descriptors were chosen at branch points. This suggests that indentation—the filing decision that creates the tree—reflects the anticipated route of access. For example, if one is interested in obtaining all of the reports issued by Dr. Jones on the efficacy of dopamine in the treatment of children in shock, retrieval is straightforward. However, if one wanted to locate all correspondence by Dr. Jones, it may be necessary to search many other branches of the tree, not just those documents related to a single drug. This extended searching is necessary because a “physician file” with a correspondence subheading was not an anticipated route of access built into the organizational structure of the file.

The main limitation of Level Four filing is that inevitably there are far fewer branches in the tree structure than actual search strategies required. That is, as with Level Three, all possible searches cannot be anticipated—the hierarchical tree structure required would be far too complex. Even if one were willing to try, the structural complexity necessary to provide rapid retrieval of all searches would not be justified by their frequency—again, far too much emphasis would be placed on the storage side of storage and retrieval. Eventually the continual sprouting of new trees and branches would force the structure to fall by its own weight. This is the ultimate limiting factor in Level Four filing systems.

![](/api/attachments/226Q9N2X/fulltext/images/df0ce39f135f968e36350e0615b0531504ff3a0d9af155b7ffa60d93a3987bba.jpg)  
Figure 1. Level 4

While Level Four filing and all lower levels are inadequate in principle, they are still worse in practice. To illustrate, consider how filing is accomplished in a typical company. Each secretary organizes her own Level Four files with a structure that is entirely personal and idiosyncratic. The system works as long as the routes of access have been correctly anticipated and built into the structure of the file. Difficulties arise whenever retrieval goes outside these structural constraints, which is often. In addition, the file structure is incompletely learned by the secretary's successor, who in turn superimposes her own peculiar filing preferences. After just a few changes of personnel, the files all but defy retrieval. This approach provides no comparability across files so each cabinet poses its own unique retrieval challenge. If there is a need to do a comprehensive search of all the documents in the organization relating to some topic, it requires riffling through many files spread throughout the company, each with a unique, often impenetrable file organization.

While comprehensive retrieval capability is extremely difficult with any manual system, given a sizeable document collection, there is a solution at the next level of filing, computerized filing. The computer can provide the total hierarchy that manual Level Four cannot attain. It serves as the next and perhaps final step in a logical progression of filing schemes. The computer enables every descriptor to be indented, "anded" in Boolean terms, under every other descriptor in all possible tree like arrangements. Retrieval can be as broad or narrow as the combinations of descriptors allow. This is the enormous advantage that the computer brings to document retrieval.

## Computerized Document Filing

With the clear recognition that nothing short of a computer system would suffice for our needs, we proceeded with its design, development, and implementation. Our system is called AMANDA, an acronym for Automated Management of Document Access. AMANDA is a completely online interactive timeshared system, written for a Digital Equipment Corporation PDP 11/70 minicomputer under the RSTS operating system. It was created entirely at American Critical Care, a division of American Hospital Supply Corporation, and has been under development for about three years.

As with extraorganizational computerized document retrieval systems, AMANDA is bibliographic. That is, for each document filed in a physical file, a surrogate or citation is created and stored in the computer. The citation contains basic descriptive information such as one finds in a bibliography—title, author, date, reference, type of document, etc. The citation also contains descriptors or keywords (the file headers in manual files), and other information to facilitate searching. Full text may also be stored.

<table><tr><td>MANUAL</td><td></td><td>AUTOMATED</td></tr><tr><td>Indention</td><td></td><td>Boolean “Anding”</td></tr><tr><td>Dopamine</td><td></td><td></td></tr><tr><td>Shock</td><td>—</td><td rowspan="5">Dopamine and Shock, and Jones, M.D., and Reports and Children and Efficacy</td></tr><tr><td>Jones, M.D.</td><td>—</td></tr><tr><td>Reports</td><td></td></tr><tr><td>Children</td><td></td></tr><tr><td>Efficacy</td><td></td></tr></table>

Figure 2. Level 4 Idention Equals Boolean “Anding”

Each document and its citation are assigned one unique number. The document is physically filed in the filing cabinet according to the number, and all components of the citation are related and stored in the computer according to this same number.

Physical filing of documents by number is much like Level One filing—the next document receives the next number and place in the drawer. However, by identifying the document date, assigning descriptors, and storing these in the computer, the document is effectively “filed” as in Level Two, Three, and Four, insofar as retrieval is concerned. That is, a search can be made knowing the document date, exact or approximate, as in a chron file or by descriptor, as in a Level Three, or Four file. Searches are done by specifying particular elements of a citation to the computer. The computer matches these queried elements against what is stored to produce a listing of specific documents with those elements. A Level Two chron file is now nothing more than a date of entry. A Level Three descriptor file is now a keyword. This type of searching is completely random access. The end result, in contrast to the manual filing systems described earlier, is a specific document or specific group of documents rather than a file folder of related information. Sequential scanning of documents is often obviated and replaced by scanning citation listings.

The physical file location is completely independent of anticipated routes of access, i.e., there is no need for Level Four type “trees” to be transplanted into the computer. Retrieval is based on the bibliographic information and other descriptors assigned and stored. The need for multiple copies is eliminated. A citation is stored once, and is retrievable on as many access points as were entered.

AMANDA can manage both a central file and also many individual, personal files. Use of AMANDA at American Critical Care centers around a central, or company, file of vital company records, and other product related information of broad or general interest. These documents are stored in, and disseminated from, a central and secured location. They are assigned document numbers and citation components by information professionals including keywords taken from a standardized dictionary. Computer searches of the central file can be done either by information specialists on request, or by anyone in the company authorized and knowledgeable in AMANDA's operation.

At the same time, AMANDA is also used by individuals who choose to have their own structurally independent personal computerized document file. These documents are housed in each individual's work area. The individuals and/or their secretaries create and store citations for their own documents which may then be searched by AMANDA. An individual can search the central file, and/or his personal file, or all files within specified security limits described below. Users generally find it unnecessary to keep personal copies of many central file documents since they can be readily searched by the individual, and a copy obtained from the central file, if needed. This helps check the costly, and often unnecessary, proliferation of paper.

AMANDA is oriented toward the end user, most likely a manager, scientist, or secretary. AMANDA speaks in human terms, comprehensive and friendly. Extensive help messages and internal checks on user responses lead users through the three basic functions: entry of new documents, changes to previously entered documents, and retrieval. The dialogue itself is not built into the computer programs, enabling it to be easily tailored to the needs of the user community without reprogramming.

AMANDA can accommodate a wide range of document types. One of the first steps in designing AMANDA was to survey all the filing cabinets, vaults, personal files, and in-baskets of two of the company's departments. The documents were classified by type into twenty-two categories (e.g., memos, reports, reprints, and unlikely "documents" such as lab specimens and lab notebooks). AMANDA was designed to accommodate all of these types without exception. The software also allows convenient definition of new document types for environments which process different categories of documents. This is a significant advantage over other document management systems which handle only a single document type because they are customized to a single project objective.

For each type of document, the bibliographic information characteristic of that type is identified. AMANDA prompts for entry of only those information types appropriate for a document (e.g., for reprints some of the information types are title, author, journal name, source and abstract; for memos the information types include "from," "to," subject, date, keywords). The user need only specify the document type on entry and AMANDA will prompt for the appropriate information. As with the dialogue and document types, these information types can also be conveniently changed without reprogramming.

AMANDA requests that the user assign a security level and a retention period to each document entered. Central file documents are assigned retention dates by information specialists to comply with legal and regulatory requirements. Owners of personal files select retention dates according to their own needs. AMANDA periodically generates reports to identify those documents for which the retention period has expired. The user can delete the document or extend the retention period at his option.

Searching all personal files is a very powerful and effective means for sharing information amongst managers and professionals in a cooperative enterprise. However, there is a legitimate concern for security. AMANDA allows the user to assign one of three levels of security to each document ranging from general availability to completely restricted access. They are:

Level 1—Company personnel can see the complete citation and the document.

Level 2—Company personnel can see the citation except for abstract and number. Access to the document is at the discretion of the holder.

Level 3—No one except the holder of a document can see the citation or the document.

So far, AMANDA's utility as a purely document based system has been emphasized. However, since AMANDA is highly flexible in terms of definition of documents, other applications readily suggested themselves before the ink was dry. For example, our library, a previously unorganized collection of books and journals, was automated by AMANDA. Rather than maintain a conventional card catalog our book holdings were put online, making our entire library collection maintainable and searchable from any terminal in our network.

In two cases, AMANDA was made available to two other divisions of the corporation. Using the same software, but through redefining of document types, information types, and dialogue, the database administrator established two functionally distinct, remotely accessed databases in a matter of days.

Yet another database has been created through document redefinition to accommodate a chemical compound registration system. In this case, the same AMANDA software which uses the document database, also runs a system which identifies the chemical name, company number, synthesizing chemist, research program, and other relevant information about potential drug products in research. Similarly, address and phone directories, logging functions, and other unorthodox "documents" are being managed by the system.

## Future Enhancements

While the features described clearly demonstrate the serviceability of the software, the synergy to be derived from the interface of AMANDA with other systems holds potentially even greater benefit. The linking of word processing to AMANDA to enable the simultaneous creation and filing of documents is a logical extension. An idealized future example is shown in Figure 3, which lists the stepwise activities involved in the creation, distribution, and filing of a letter. In this case, information in word processing becomes filing information in AMANDA.

The secretary creating the letter is first asked to identify the type of document that is to be created. In this case, “letter” is selected from a menu. The sender’s and recipient’s names are then typed in response to another prompt. These are “looked up” in an electronic names and address file. The appropriate return address and mailing address are then auto-entered.

Next, the text or body of the letter is created. An ending is selected from another menu. Carbon copy recipients are named and the secretary is asked whether this is a final draft. If so, distribution and filing are next considered.

At this point, the secretary can direct copies to be sent via electronic mail, to other terminals in the network, or by conventional mail. For hardcopy to be mailed, the address information previously referenced is again used to address the envelope.

The next question concerns filing. Is the document to be filed? If so, in which file? The choices may include one's own personal file, or the company central file. If the document will indeed be filed, the secretary is then asked to provide additional information. From the text itself the addressee, sender, date, number of pages, etc., can be extracted electronically, but security, retention, a title, and keywords are still to be assigned. An intriguing possibility is to allow the secretary to tag certain words in the text as keywords, as the text is created. Finally, when the surrogate is complete, a document number is assigned by AMANDA, and copies are distributed electronically or manually.

![](/api/attachments/226Q9N2X/fulltext/images/13d2da371a08dd30d0554a16ca0cffc0d79edad23364ff49f202d5bbf8e0346d.jpg)  
Figure 3. Creation, Distribution, and Filing of a Letter

The other direction of flow across the interface, AMANDA to word processing, is also useful. Bibliographic information retrieved from an AMANDA search can be included in text created on a word processor. An example will illustrate the process.

Until recently American Critical Care lacked an effective means for coordinating and following up on book orders in the Information Center. Early efforts at communicating information included distribution of a standard monthly memo and a list of books ordered during the period. The list was prepared by referring to purchase order records.

With AMANDA, online cataloging and order tracking starts by entering whatever is known about the book being ordered—title, author, requestor—along with the keyword “ordered.” Periodically, the order clerk conducts an AMANDA search using the terminal of a word processor. She conducts a search for citations with the “ordered” keyword and the month(s). Results are displayed on the CRT and then stored on a floppy disk of the word processor, appended to a form letter. The form letter is then list processed to produce individually addressed copies of the letter and book list.

Another benefit from the AMANDA word processing interface is the ability to electronically lift boiler plate sections out of AMANDA for inclusion in a document being typed on a word processor. Abstracts, study numbers, and directory names and addresses are examples of material that might be extracted in this manner.

Other likely extensions include a data processing/AMANDA interface. This presents the opportunity to conveniently file away the output from computer data processing. It could include the whole spectrum of computer output from data listings to tabular displays to graphics.

Finally, the linkage between word processing, AMANDA, and various terminals in the network, paves the way for the electronic creation and transmission of documents, that is, electronic mail with the option to keep the electronic message on file.

## Impact on the Company

In the short time since AMANDA has been introduced to the company for selected use, its effects are already apparent and far reaching. AMANDA has notably improved company communication by opening personal files and facilitating companywide information flow. Easy online access to personal files and the central file, within security limits, benefits the whole company in its day-to-day operation. Perhaps most importantly, where once our files served as a dead storage area for paper that would otherwise clutter the office, they are gradually coming to be viewed as an active information resource. Filed documents are increasingly being used as an integral part of the decision process.

As a member of the highly regulated pharmaceutical industry, American Critical Care has become distressingly aware that traditional approaches to information management are inadequate to meet the increasing demands imposed by legal and regulatory requirements. In the near future we anticipate that AMANDA will facilitate the process of assembling the multivolume and complexly interrelated government submissions which are required by the Food and Drug Administration for bringing new drugs to market. Many of the components of these submissions are already stored in AMANDA requiring only selective online review and retrieval for their incorporation.

AMANDA is currently being used by several departments at American Critical Care and from remote sites at other divisions in the corporation. It is being accessed from terminals, largely resident at secretaries' desks, which are also used for timeshared word processing and data processing on the PDP 11/70. Usage will increase as conventional typing equipment is phased out and replaced by terminals and printers, eventually extending the network throughout the company [2].

Finally, user acceptance by professional staff, managers, and secretaries has been almost universally positive. Secretaries report that it is easy to learn (a User's Manual has been created for this purpose), convenient to use, and far more pleasant to operate than manual filing. Managers and professionals indicate that their productivity has been enhanced. Whereas storage requires somewhat more effort (e.g., a retention period and security level is to be assigned to every document), fewer documents are stored and retrieval is facilitated. The more invested on the storage side in selecting a title, keywords, and other descriptors, the greater the return in retrieval capability. The tradeoff is largely left to the users' discretion, which makes AMANDA a useful and flexible tool capable of accommodating the needs of those who participate in the filing process, from the most fastidious to the least demanding.

## References

[1] Golde, R.A. "Muddling Through," AMACOM, New York, New York, 1976.

[2] Horwich, J.S., Fortune, J.S., Hoyt, H.J., and Schwartz, R.A. "An Integrated Computer Network in Pharmaceutical Technology," Pharmaceutical Technology, Volume 4, Number 1, January 1980, pp. 54-61.

[3] Jackson, E.B. "An Overview: The Information Explosion and its Implication for Management," Industrial Information Systems: A Manual for Higher Managements and Their Information Officer/Librarian Associates, Dowden, Hutchinson and Ross, Inc., Stroudsburg, Pennsylvania, 1978, p. 1.

[4] Swanson, E.B. and Culnan, M.J. "Document-Based Systems for Management Planning and Control: A Classification, Survey and Assessment," MIS Quarterly, Volume 2, Number 4, December, 1978, pp. 31-46.

## About the Authors

Ronald A. Schwartz, Ph.D., is the director of Scientific Affairs at American Critical Care, in McGaw Park, Illinois. After attending Brandeis

University, in Waltham, Massachusetts, and Northwestern University, in Evanston, Illinois, he received his Ph.D. in 1971 from the Illinois Institute of Technology, Chicago. He has since held various positions in the pharmaceutical industry, all related to providing support services to scientists and technicians engaged in drug research. In his present position, his department provides computer services, information services, and biostatistical support to the researchers and other professionals working on drug R&D. Dr. Schwartz has devoted a decade to the problem of simplifying the researcher and manager's job by replacing routine, time-consuming manual functions with user-oriented computer systems, and has written extensively on this subject. He is a member of the American Psychological Association, the American Statistical Association, and the Drug Information Association for which he served as the General Chairman of the 1979 annual meeting.

Joan Fortune established and manages the information center and the bibliographic retrieval and records management programs at American Critical Care, McGaw Park, Illinois. She has a B.S. in chemistry and an M.S. in organic chemistry from the University of Wisconsin, in Madison, and is pursuing an MBA at the University of Chicago Graduate School of Business. In recognition of her contribution to the design of AMANDA, she shared with Julian Horwich and Ronald A. Schwartz the 1979 American Critical Care President's Award for scientific and technical excellence.

Julian Horwich is systems manager at American Critical Care, in McGaw Park, Illinois. He received a B.S. in Electronical Engineering from Northwestern University, Evanston, Illinois, and did graduate work in computer science at the Illinois Institute of Technology, Chicago. In December 1976 he joined American Critical Care to found the Computer Services Department. As systems manager he is responsible for the development and operation of all research computer systems and for the installation of word processing systems. Prior to American Critical Care, he spent ten years at Abbott Laboratories implementing applications and doing systems programming. He also spent two years working in a support function for a computer vendor.

MIS Quarterly/September 1980 49
