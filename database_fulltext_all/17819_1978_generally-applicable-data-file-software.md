---
otero_id: 17819
otero_key: "4H37625F"
title: "Generally applicable data-file software"
authors: "R.D. Boschloo"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90026-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Generally Applicable Data-File Software

R.D. Boschloo

Royal Naval College (A.M). Het Niewe Diep S, 1781 AC
Den Helder. The Netherlands

In just the same way as it is inefficient to use only Jumbo-jets for air transport, it is also inefficient to use data base software for all data processing applications. However, it is remarkable that it is simple data processing project one often has to manage with application dependent software. This article shows how it is possible to develop generally applicable software files for the various operations upon files such as creating, updating and sorting, changing the storage structure, selecting soft files, plotting numeric values, etc. The technique involves including the complete file description in the file itself, but the composition of this file description plays an important role. The described method has been used at the author's institute for more than two years and meets the needs of many users both in administrative and scientific applications. It seems that non-prottammers quickly find it useful for building their own data collections.

Keywords. General file systems, application independent software data structure levels, logical file structure, file definition.

![](/api/attachments/4H37625F/fulltext/images/f41b016570f414cf1eaab262313b5ea519169f57c7bab4c529d7b5b0cf4983f1.jpg)

R.D. Boschloo joined the Statistical Department of the Mathematical Centre in Amsterdam in 1964 where his main activity consisted of Developing programs for statistics and operations research. In 1967 he received a Master's degree in mathematics at the University of Amsterdam and transferred from the Mathematical Centre to the Centre for Automation of Weapon and Command Systems of the Royal Nether lands Navy, As Head of the Section Support Software of this Centre he has been involved in the development of an operating system for a military computer and in the development of a compiler for real-time system programs. Since 1972 he has been a teacher at the Heval Naval College (KIM) and Head of the Computer centre of this Institute.

1. Introduction

Data base software can be an appropriate tool for information systems building if several people have access to the same data and especially if they are allowed to change the data. This statement holds even more if the data has a complex structure and the reports tend to be different each time. However, this is not the situation for most computer applications, and even the designers of data base software are aware of this; e.g., see to the CODASYL report [1]. The growing number of small computer systems and the fact that even large systems often service users with their own data-files make it unlikely that this picture will change rapidly. For smaller data processing applications, generally applicable file software will often prove valuable.

## 2. Concepts and definitions

A data-file is identified by a name and consists of a collection of records. In general, a distinction is made between a "logical" record and a "physical" record. Physical records are the building blocks of a file (seen from the hardware point of view). Logical records are the building blocks of a file as seen by the user.

A (logical) record consists of a number of related data-items (or field) (e.g. [2]), or attribute, or property, or data element). The items of a record describe the same entity, object or situation, for example, the salary parameters of a certain employee or the experimental values at a certain time. One or more of the data-items of a record (key-items) are used to identify individual records in a file. See Fig. 1.

One of the attributes of a record is its length. The length of a record can be interpreted either as the number of data items in the record (the "logical" record length) or the number of words or characters © North-Holland Publishing Company
Information & Management 1 (1978) 199-206 used to store the record on a certain medium (the "physical" record length). In this paper, the length of a record is always used to mean logical length i.e. the number of items in the record. The length of the records in a file is said to be variable if the number of items in a record is not the same for each of the records in the file.

![](/api/attachments/4H37625F/fulltext/images/b3836d7e62d34ee5f17a55e6b22cae239231f880959d69e00f823faa6a22a7c0.jpg)  
Fig. 1. General file structure.

A file has fixed length records if all records in the file have the same number of items (see Fig. 2). In this paper, all files will be defined to have fixed length records (though the physical record length may differ). Because a file with variable record length can unambiguously be converted into a file with fixed record length (see Fig. 3), the restriction to fixed length records may hardly limit the application.

One or more data items of a record called the key-items are used for identification. Keys consisting of more than one data item are called concatenated keys. If a unique selection capability for each individual record is required, it is necessary that all key-item values in a file are unique. Some operations—such as the updating of a single record—are undefined for a file with duplicate values of key-items, however many other operations (such as sort) do not give any problem for duplicates. See Fig. 4.

![](/api/attachments/4H37625F/fulltext/images/5685507ddc708ac0596a874c4a78d5fd77dd8b74b51e9f247b13654e6d363c42.jpg)  
Fig. 2. Examples of variable and fixed (logical) record length.

![](/api/attachments/4H37625F/fulltext/images/f8f85de5a1d1dc03539cb68f8adf0a61a0db97ce7cd4047997bcf9bdff34ce44.jpg)  
Fig. 3. Conversion into fixed length b gical records.

<table><tr><td colspan="2">partnumber - quantity sold</td></tr><tr><td colspan="2">key item</td></tr><tr><td>2&#x27;9</td><td>50</td></tr><tr><td>139</td><td>15</td></tr><tr><td>382</td><td>710</td></tr><tr><td>2&#x27;4</td><td>73</td></tr><tr><td>2&#x27;9</td><td>82</td></tr><tr><td>139</td><td>76</td></tr></table>

Fig. 4. Example of a non-sorted data-file with duplicated values of key-items.

Since all file-operations in this paper are applicable to files with unique keys, all files discussed here are supposed to have unique keys. However, the reader can easily find out when duplicate keys are allowed.

## 3. The file description

Many files consist of records which are a grouped number of values or text; if one examines these files in themselves, it is even difficult to locate the starting point of each data-item; i.e., the description of these files is to be found outside them. Fig. 5 illustrates this.

In a conventional file system (Fig. 5a), the data description is in the application program. Data management routines of the operating system are used for operations on records. In a data base approach (Fig. 5b), a file description is part of the data model description.

The method described in this paper is illustrated in Fig. 5c. As indicated, the (complete) data description (for example: number of (key) items, item types, item names, maximum value of each item, etc.) is given outside the application programs as part of the file.

![](/api/attachments/4H37625F/fulltext/images/0c11d5bb8e0b95b9145aabec425155042ff1e1d42a19b60d8dab2ebe4cdd754d.jpg)  
Fig. 5. Various description methods for stored data A Conventional files; B. Delta base approach; C. Method described here.

This technique is therefore quite similar to the data base method, except that the files are completely separated from one another. Compared to the conventional method, this method has the advantage that one can write file independent programs. The system has been used for both administrative and scientific work; the former use update programs while the latter tend to use plot, least square fit, and statistical programs.

The system is also effective in the field of education; in the past, students had to spend time writing programs for creation and maintenance of data-files. This can be very useful in a course for system programmers, but technical aspects of data-files are less important in a training course for computer users.

## 4. The contents of a file description

The more complex the operations on a file, the more detailed the required specifications of the file structure. If all the files on a tape must be copied to another tape, then even the names of the files need not be known by the program that makes the copy. But if a program has to match on a given key to select a record, then a thorough specification of the file must be available.

The system described in this paper allows standard operations on generalized files, so a detailed file description is required. This description, stored at the beginning of the file, has two levels of detail:

A. General information about the file structure.

B. Detailed information about each data item in a record.

The general information about the file structure covers the following:

\- file types (sequential, sorted on keyvalue, duplicate keys, etc.)

version number/creation date

\- number of key items

\- number of non key items.

The parameter $\langle file type \rangle$ is needed by such software as SORT-programs that change the sequence of the records. Such a SORT-program would then change the parameter $\langle file type \rangle$ . If (later) a program tries to access this file via the old key, say in a sequential way, it first checks the $\langle file type \rangle$ parameter and prints an error message.

Other general information that could be useful is information about privacy or protection level of user groups allowed to read and/or write the file. In some computer systems, these facilities may be part of the operating system.

The (version number/creation data or time) is automatically updated with each alteration.

The second description level of the file-structure contains detailed information about each data item. A data item is, in some respects, similar to a variable in a programming language, having a name, type, and value.

Since the name and type of a data item do not change in the successive records of a file, these two aspects can be stated once: at the beginning of the file, in our system, for each data item, key or not, the following information is stored:

item type (integer, real, text, etc.)
maximum length (especially for text items)

\- minimum value

-- maximum value

The maximum and minimum value can be used by general file programs to screen record content. A conversational input program could print an error message if an input item value is out of range

## 5. The logical, storage, and physical structure

Up to now we have discussed the logical structure of a data-file. Any user who is not interested in software details but only in the sorts of available data is, in fact, thinking of the logical structure. However a user is often also interested in the time to access the data; in some situations, a response may be in hours, in others a few seconds. The response time depends on the manner in which the data is stored. The accessibility depends on the storage structure, as illustrated in three simple examples:

\- A row of objects has a serial structure if the objects are arranged randomly so that one must search through the objects consecutively until the object is found.

\- In a sequential structure the objects are sorted according to the key value. A sequential structure allows faster search since not all successive objects must be examined; skip or binary search allows long strides through the row to the approximate location of the object.

An index sequential structure occurs if a sequential structure has an index which points in a key to groups of objects. With this structure rapid access to relevant objects can be realized after brief reference to the index.

Besides an index for the key item of the record, it is sometimes desirable to create other fast access paths (via other “secondary” keys in the record). In this “multikey” access, there are primary key and index, and one or more secondary keys and indices.

It will be obvious that the more access keys, the more complex the storage structure, and it will be more difficult and time consuming to add a new object.

For the sake of completeness, a third level of file structure is mentioned; besides the logical structure and the storage structure, a physical structure is distinguished. This structure (celimits the way in which the file (including possible indices) is represented on a storage medium

![](/api/attachments/4H37625F/fulltext/images/22b96df5676ad57c86b8de7909c24f0d028d06e948e02cc8554526f8539b542b.jpg)  
Fig. 6. A standa J file can be automatically converted from one storage structure to another

The more technical aspects of the various storage and physical structures are not important in understanding this article; this subject is covered in the existing literature (e.g., part two of [3]).

In our technique, a file can be accessed in many different ways by selecting one of the available storage structures; the storage structure is independent of the logical structure of the file. In consequence, any data-file can be automatically converted from one storage structure to another as long as the logical structure of the file is indicated to the program that carries out the conversion. If the description of the logical structure is embodied in the file itself, as a motivated here, one can write a generally applicable program for the storage structure conversion of any standard file. In our institute, this method was implemented in software which converts from sequential to index sequential storage structures and vice versa (Fig. 6). A general program was also written to add one or more secondary indices.

The fact that a file with a given logical structure can be converted into several different storage structures shows a major difference from a conventional file system, and provides a great deal of independence of data from program.

## 6. Design of the generally applicable file programs

Now we will indicate the practical utility of our method. For this purpose, simple examples seem appropriate. Therefore, a sequential file structure is chosen, and data files will consist of records with only a few items. The method is applicable either in a conversational time sharing system, but it is also applicable in a batch environment. True enough these non-conversational fine programs can not support the user input by way of questions and answers, but a list of plainly stated errors messages will meet these disadvantages which are inherent to batch processing. The illustration assumes (as at the author's first rule) a conversational system.

In the sequential version of a standard file, the complete file description is placed ahead of the file itself. Every generally applicable file program first requests the name of the file, opens this file and reads the description. The complete file structure -- the number of items, the number of key-items, the item names, the item tyres, the allowed value ranges -- is now known in the program. Four typical general programs are now discussed.

Example 1: A SCRT program. After having read the file description, the program lists the names of the record items on the terminal and asks the user for the name(s) of the item(s) on which the new file should be sorted, and for a name of this new file. After the user has answered these questions, the new file is created in the records in a new order. If the "SORT-item" was of the type string, an ascending alphabetic SORT is carried out, otherwise the records are sorted in ascending numeric value of the named SORT key.

Example 2: A LIST program. This program lists the actual contents of any standard file. Since the data item names are known, item names can be printed as heading at the top of the columns of each new page. The required width of each column can be derived from the item description; e.g., if the maximum value of an integer item is 999 and the minimum value is 0, a width of 3 positions plus one (or two) spaces is sufficient. The number of columns that can be placed on one line depends on the width of the columns and the maximum width of the print device. If a record has to be split over more than one line, an extra line fixed is output between records.

If required, the page number, file name, creation data and file version can be printed at the top of each page.

Example 3: A conversational UPDATE program. This program for a sequential file reads the descripttion from the beginning and asks the user for update data by printing the item names of the records. As an item name is printed, the program waits for input of a corresponding item value. If this value does not meet the type and range description of that item (as defined at the beginning of the file) an error message is printed, and the item name is printed again. (See, for example, the second record of figure 7).

![](/api/attachments/4H37625F/fulltext/images/5c4589f946aa74bb87d503e53e382b6dc334b3bdf57dba0185225e299d72cd8f.jpg)  
Fig. 7. Example of a file update (Terminal input from the user is undefined; comments are in lower case characters).

In fig. 7, the file CITIES must already exist before the updata-run starts. A very first version of a file (containing a file description and an end-record) can be defined by means of a general file definition program. A single minus sign (-) instead of a value for the first non-key-item indicates that the record has to be deleted (e.g., in the last record). All updates, which may be input in any order, are stored in an array. As soon as the updata command “(”) has been given, a new updated file is created. The user can decide to keep the old file for back-up. It is not clear in figure 7 whether the records with the key value AMSTERDAM and ROTTERDAM are new records or updates for existing ones. This will be kept unsettled until at the end of the run, the array with insertions, updates and deletions is processed into a new master file. A so called journal of audit trail could give certainty about the existence of the key values in the old master file (in this audit trail all actions upon records are mentioned). Earlier updates that are already placed in the array but not yet implemented in the old master file can still be corrected by using the same key value again followed by a new record contents or by the symbols “--” in case cancellation of the earlier update is desired. A single plus sign (+) instead of a value for a non-key-item indicates that, the value of this item in the corresponding record of the old master file is not to be changed. Provisions are made to buffer, if required, the updates in a separate file or to add the updates to an already existing buffer file and update the master file only occasionally.

In this system there is no difference between the structure of an updata file and the structure of a master file.

Example 4: Selection of a subfile. In many situations, printing, copying, etc. are only to be carried out on a part of the records in the file. Therefore facilities are required to select subfiles which consist of records with a certain item value (or a certain range). The records of the selected subfile need not contain all the items of the original file; so the subfile will not only have less records but the records can be smaller too.

The easiest way to implement a facility for the selection of subfiles is to write a program that first asks for the name of the original file, the selection criteria to be applied on the records, the name of the subfile to be created, and the record structure of this file. After the specification of all these parameters the original file is processed, and the new file is created. This new file has a standard format, thus, other generally applicable programs (such as sort) can be applied.

It takes more effort to implement a combined selection and sort facility, but an intermediate subfile can sometimes be omitted if programs (such as print) are equipped with two subroutines; the first reads in the selection parameters at the beginning of the program run and the second carries out the selection tests for each successive record of the original file.

Duplicate keys can occur if one or more of the original key-items are omitted in the new record structure, so in that case, the file type indicator in the file description should be set to "duplicate keys".

Example 5: Other Useful Subsystems. Several other software features are worth considering:
- A program that plots the points (or a line though the points) defined by the value of any given pair of numeric items in the records. This is particularly useful when the items consist of the values of experiment parameters at a certain point of time. Because of this, experimental data are often stored in a standard file format as they enter the system.

\- Statistical programs, e.g., that calculate and plot least square fit curves through the points defined by any given pair of numeric items in the records.

\- A lay out program through which the number and position of record items can be chosen for printing.
- Programs for the conversion of the storage structure of a file.

## 7. Application dependent programs

Fig. 8 reflects the general principles of normal data processing, where the raw data is complete but somewhat inaccessible to the user. Data needs to be processed, for instance by a computer, in order to produce information that reflects the needs of the user.

Although the products are different for each project and even for various users within the same project, there are often many similarities as far as the processing of data is concerned. One can therefore try to develop a general applicable program. This leads to the situation where a substantial part of the data processing is performed by generally applicable software but some work still has to be performed by special purpose programs.

![](/api/attachments/4H37625F/fulltext/images/89d2bbbdc2eb16260eb6ca7f56ee9306ad26ed2c603a6592cea1f9b5d05780da.jpg)

A. $M_{1}$ , $M_{2}$ , $M_{3}$ , $M_{4}$ , $M_{5}$ , $M_{6}$ , $M_{7}$ , $M_{8}$ , $M_{9}$ , $M_{10}$ , $M_{11}$ , $M_{12}$ , $M_{13}$ , $M_{14}$ , $M_{15}$ , $M_{16}$ , $M_{17}$ , $M_{18}$ , $M_{19}$ , $M_{20}$ , $M_{21}$ , $M_{22}$ , $M_{23}$ , $M_{24}$ , $M_{25}$ , $M_{26}$ , $M_{27}$ , $M_{28}$ , $M_{29}$ , $M_{30}$ , $M_{31}$ , $M_{32}$ , $M_{33}$ , $M_{34}$ , $M_{35}$ , $M_{36}$ , $M_{37}$ , $M_{38}$ , $M_{39}$ , $M_{40}$ , $M_{41}$ , $M_{42}$ , $M_{43}$ , $M_{44}$ , $M_{45}$ , $M_{46}$ , $M_{47}$ , $M_{48}$ , $M_{49}$ , $M_{50}$ , $M_{51}$ , $M_{52}$ , $M_{53}$ , $M_{54}$ , $M_{55}$ , $M_{56}$ , $M_{57}$ , $M_{58}$ , $M_{59}$ , $M_{60}$ , $M_{61}$ , $M_{62}$ , $M_{63}$ , $M_{64}$ , $M_{65}$ , $M_{66}$ , $M_{67}$ , $M_{68}$ , $M_{69}$ , $M_{70}$ , $M_{71}$ , $M_{72}$ , $M_{73}$ , $M_{74}$ , $M_{75}$ , $M_{76}$ , $M_{77}$ , $M_{78}$ , $M_{79}$ , $M_{80}$ , $M_{81}$ , $M_{82}$ , $M_{83}$ , $M_{84}$ , $M_{85}$ , $M_{86}$ , $M_{87}$ , $M_{88}$ , $M_{89}$ , $M_{90}$ , $M_{91}$ , $M_{92}$ , $M_{93}$ , $M_{94}$ , $M_{95}$ , $M_{96}$ , $M_{97}$ , $M_{98}$ , $M_{99}$ , $M_{100}$  
![](/api/attachments/4H37625F/fulltext/images/9bab7f1377cfd38f472fe391dc38fee7de1b0e13e1611d8f662a011b59584f1c.jpg)  
9 TEACINO TOWARDS GENERAL APPLICABLE PROGRAMS  
Fig. 8. Universal and special data processing software.

It was our intention to reduce the volume of special purpose software in favour of general purpose software (but without making this general purpose part too complicated). However, it is still necessary to develop special purpose file programs for some projects.

The production of special purpose programs for handling files with a sequential structure is only slightly more difficult when using our standard files. If special purpose programs use a more complex file structure, then it is even an advantage to use our standard files, since the standard structure allows the development of standard subroutines for their access. Because of the availability of a complete file description, these routines can be more problems oriented than the usual operating system oriented data management routines. Here we are similar to data base software, the application programmer is freed from much of the cares about the access of data via indices, pointer, tables, etc.

As long as special purpose programs have to deal with only one standard file at a time, the file handling aspect of that program will not be very difficult. Unfortunately, however, in many applications more than one data file has to be processed simultaneously.

Data files which are to be processed simultaneously are often related through an item that is common in both files. As an example: In file A, one of the record items is a Code Number, while in file B complete data is given. The simultaneous processing of these two files consists of combining records of file A with records of file B so that they have the same value for this common item. The result of this process can be produced in the form of a standard file, which allows further processing with generally applicable file programs.

Even generally applicable programs for simultaneous file processing can be written (e.g. see Figure 9). File B has to be accessed via the common item that is used as primary or secondary key. The sequence of the records in the output file is determined by the sequence of the records in File A, if necessary the records of this file can first be resorted.

The single result file is a much easier object for further processing than the two (or more) original files. However the decisions about the input files and the processing of them are difficult techniques to apply by the average user. This is perhaps an indication that the simultaneous processing of files does exceed the boundaries of generally applicable programs, but other methods or special purpose programs using subroutines for easier file access are probably more adequate after all!

![](/api/attachments/4H37625F/fulltext/images/4f2f8582aeb3bf08e3d8b1be37c0caf3b10cd730a8d6b34574c0bfe4fc1083ba.jpg)  
Fig. 9. Simultaneous processing of related files while combining records with common item values.

## 8. Conclusions

A standardized file in which a complete definition of the file structure is included in the file itself, permits the production of generally applicable file programs for operations such as sorting, updating, subfile selection, conversion to another storage structure, etc. Experience of the author shows that many of the users of generally applicable file programs do not need any further application dependent software. Many other users, however, still need to write additional special software, but also here the use of a standard file structure has advantages since the development of this software is not complicated by the standard file structure.

The mutual communication between users, between computer people and between users and computer people is simplified because of the use of standard files and programs and the use of corresponding terminology, concepts and working procedures. The documentation activity is also reduced since a part of it can consist of a reference to the user manua and possible other documents of the standard file system. Moreover, it will be obvious that the use of generally applicable programs reduces the program production and maintenance activities.

The use of more complex storage structures in application programs is also simplified since the complex file access actions can be left to standard subroutines with access to a complete file description. Indeed, our tailored routines are more problem oriented than the usual data management subroutines.

## Acknowledgement

The author developed this system in conjunction with C.W.R. Nijenlaris who is also at the Royal Naval College (KIM) Den Helder, The Netherlands.

## References

[1] CODASYL Data Base Task (Group, April 7) Report (available from: IAG Headquarters, American).

[2] L.H. Gould, IF2P Guide to Concepts and Terms in Data Processing (North-Holland Publishing Company, Amsterdam-London, 1971).

[3] J. Martin, Computer Data-Base Organization (Prentice-Hall, Inc., Unkwood Cliffs, N.J., 1975, 19–7)
