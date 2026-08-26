---
otero_id: 18195
otero_key: "ADYDHJK9"
title: "Structured systems analysis using SPSL/SPSA"
authors: "Eric W. Channen; Paul G. Sorenson; Jean-Paul Tremblay"
year: "1985"
journal: "Information & Management"
doi: "10.1016/0378-7206(85)90067-9"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# Structured Systems Analysis Using SPSL/SPSA

Eric W. Channen

University of Windsor, Windsor, Ontario, Canada

Paul G. Sorenson and Jean-Paul Tremblay
Department of Computational Science, University of Saskatchewan, Saskatoon, Saskatchewan, Canada S7N OWO

This paper describes how a structured systems analysis methodology can be supported using SPSL/SPSA, a computer-aided analysis and documentation tool. The integration of the methodology and the tool is illustrated using a case study approach. The use of various SPSA reports to assist in analyzing a system description in accordance with the methodology is also outlined.

Keywords: Structured Systems Analysis and Design, Computer-Aided Analysis and Design.

![](/api/attachments/ADYDHJK9/fulltext/images/2cd612d3267b293ca8bc011bf1fe35eb1c93bfc43793b1ca5b130ebc4275d0ec.jpg)

Paul G. Sorenson received his B.Sc. and M.Sc. in Computing Science at the University of Alberta and Ph.D. in Computer Science at the University of Toronto. He is currently a Professor and Head of the Department of Computational Science at the University of Saskatchewan. He has co-authored books in Data Structures and Compiler Construction with J.P. Tremblay. He spent a year as a Visiting Research Scientist at IBM San Jose Research Laboratory.

![](/api/attachments/ADYDHJK9/fulltext/images/6bc031cd81d5c72305f67fab8939a4ed43be9384511380bdfa3fe25a616b044a.jpg)

J. Paul Tremblay received his B.Sc. and M.Sc. in Electrical Engineering from the University of New Brunswick and a Ph.D. in Computer Science from the Case Institute of Technology. He is currently a Professor of Computational Science at the University of Saskatchewan. He has co-authored books in Discrete Structures, Data Structures and Compiler Construction. In the past year he was on leave at the University of Arizona MIS Department.

## 1. Introduction

It has been conjectured that, in recent years, productivity in the systems development life cycle has been greatly improved through the use of techniques such as structured programming $[1]$ and later, structured design $[15]$ and structured analysis $[3]$ . At the same time tremendous advances have taken place in systems development aids, such as database management systems, data dictionaries and very recently computer-aided analysis and design tools $[11]$ . Unfortunately, very little effort has gone into the integration of these methods and the tools that support system development by the information system analyst/designer.

This paper describes how a computer-aided analysis and documentation tool, SPSL/SPSA (Simple Problem Statement Language/Simple Problem Statement Analyzer) as described in [2] and [8], can be used to support a structured analysis methodology proposed by [3]. SPSL/SPSA is a component of the DEVIEW (DEvelopment of an Information system Environment Workbench) project at the University of Saskatchewan. It has several benefits, but probably the most important is the assurance that the system analysts will conform to a standard in system documentation. This can be checked, in part, through completeness and consistency analysis when using the tool; but this will only be briefly introduced here.

![](/api/attachments/ADYDHJK9/fulltext/images/a811dfa5a7f914854e9c1c9e134eb5f57e7f8e673280599d4d6443c3344359bd.jpg)  
Eric W. Channen received his B.A. and Ph.D. in Physical Chemistry from the University of Toronto. He served as Director of the School of Computer Science at the University of Windsor for over ten years, developing its undergraduate Computer Science program, and is presently a Professor there. His interests are in language processing and problem oriented languages. He spent a recent summer in Saskatchewan working on the SPSL/SPSA project.

## 2. Summary of a Structured System Analysis Methodology

“Structured Analysis” consists of several steps; it is described in the following informal algorithm:

1. Conduct a series of initial interviews with users and produce a "Request for Proposal" (RFP).

2. Construct a set of initial high-level data flow diagrams (DFD's) for a system that will satisfy the needs in the RFP. A data flow diagram contains symbols representing four types of information for a system description:

i External entities – usually classes of people who receive or produce information. An external entity is symbolized by a solid square.

ii Data flows - represent data structures in motion; symbolized by directed arcs.

iii Processes are symbolized by upright rectangles with corners rounded.

iv Data stores - locations where data structures are internally stored. Data stores are symbolized by a rectangle with one side missing.

3. Refine the data flow diagrams in an iterative top-down fashion and incorporate details, such as exception handling.

4. Construct the dictionary database. This primarily provides details about the contents, size and volatility of data stores.

5. Specify performance and size (e.g., how often certain processes are performed).

6. Provide a high-level description of process logic. Conventional process description techniques (decision trees, decision tables and pseudo code) are often used for this.

7. Define immediate access requirements of each data store, based on user query requirements.

Note that these analysis steps (except the first) are performed iteratively. Initially, the analyst describes only a segment of the system. On each iteration, various reports are generated to perform any required analysis. Based on this analysis, some aspect of the system description may be found inadequate and an earlier stage of analysis repeated.

The current version of SPSL/SPSA supports the first six of these steps quite effectively.

## 3. Overview of the SPSL/SPSA System

SPSL/SPSA [2] is a systems analysis and documentation package designed and implemented on PDP-11s and VAXs under UNIX. It is a subset of the PSL/PSA package [9] that was developed for information systems analysis and documentation at the University of Michigan. SPSL is a nonprocedural language used to define the logical structure and requirements of an information processing system. It describes an information processing system through objects and relationships between objects. SPSA is a software package which accepts SPSL statements and generates various documentation and analysis reports from the database.

SPSL permits the description of both system related information and data related information as follows:

## 3.1. System

a. System flow deals with the flow of data into, out of, and within the system.

b. System structure is concerned with the hierarchies in an informatimon processing system, i.e. it deals with the breakdown of high-level processing activities into logical components.

c. System size is concerned with the volume of processing and the amount of data stored.

d. System dynamics refer to the manner in which a system behaves over time.

## 3.2.Data

a. Data structure represents the relationships which exist among data that are manipulated and used by the system, as seen by the users.

b. Data derivation specifies how new data are derived within the system.

A description of an information processing system in SPSL centers around its system components, called objects, and the relationships between these components. The analyst creates an object and relates it, via relationship specifications, to the rest of the system in a unit of description called a section. In general, the ordering of sections is not significant, and therefore SPSL is nonprocedural. These types of system and data related information will be exhibited by an example later in the paper.

SPSA is a software system with three functions: 1. It provides a facility to compile SPSL statements and store an equivalent representation in a database.

2. It allows modification of a problem statement stored in a database. These facilities provide various features including the ability to change the name and type of an object, combine the information stored in two system components and delete the undesired object, input and delete selected SPSL statements, and input and delete SPSL objects.

3. It produces documentation from a problem statement stored in an SPSA database and determines if the problem statement is complete. These functions are provided by various SPSA reports. Five of these are primary reporting functions [13]. They include the ability to print object names from the SPSA database, to analyze the completeness and consistency of the interactions among process and data descriptions, to display any/all hierarchies contained in the system and/or data, to print a dictionary of the data elements, and to provide a formatted listing of the contents of a database.

The SPSL/SPSA system has been used for the last three years in a teaching environment $[10]$ and is currently being tested commercially. It has proved beneficial in structured analysis and documentation, yet inexpensive to operate. The system is being expanded to include additional features to aid the analyst: a prototype output generator $[14]$ , a prototype form-oriented data entry and transaction handler $[12]$ , and a data flow diagram production facility $[4,7]$ . Further plans include features to aid structured design an logical database design.

## 4. Applying Structured Systems Analysis to an Example System

A radiologist and his staff of X-ray technicians treat up to 100 patients a day, though a typical daily load is 50 to 60 cases. For most patients (about $95\%$ ) the service is paid for by the Provincial Health Insurance Plan (PHIP). The remaining $5\%$ are about equally divided between those charged to the Workman's Compensation Board (WCB) and those billed privately to the patient.

At present, claim forms for PHIP are prepared by a data processing service, but the quality of the work is unsatisfactory: up to 15% of the forms are in error. Significant delays occur in correcting these errors. The radiologist believes that a small in-house computer would both improve the quality of the work and permit the production of several reports analyzing his practice that are not now available.

Following the methodology of Gane and Sarson the first step in a structured, top-down analysis is to identify the primary sources and destinations of data flows, the major flows themselves, the major processes that handle the data, and the major data stores. We will begin by describing the existing system in this manner. Normally the high-level DFD would be developed in an incremental fashion starting from the primary sources of data and concluding with the primary destinations. To reduce the length of the paper, we have included only the final high-level data flow diagram (DFD) as given in Figure 1.

A primary source of data is the patient, from whom the “treatment voucher” is obtained. It is prepared in the process create-voucher by a receptionist using the information obtained from the patient, from the prescription, and from PHIP schedules of treatment and doctor codes. These vouchers are sent to the process prepare-claims which prepares bills or claims for payment. The claims are sent to PHIP, WCB or to the patient, depending on the type of account. The voucher, or data from it, must also be filed for later reference when the payment is received. Although we are describing an existing system, we do not wish to tie our analysis to the specifics of existing operations. Thus we will consider all filing to be done in one undifferentiated file. Next we recognize that claims and bills will normally be paid by the agency or person receiving them. Also, at the top level of analysis we must represent the regular reports received or person receiving them. For example, we must represent the regular reports received by the doctor. These are the daily treatment report and the monthly accounts receivable report.

The PHIP schedules in the manual system are printed lists, but logically they are data stores and are shown as such in the PHIP doctor schedule and PHIP treatment schedule data stores. In this instance PHIP publishes revised doctor and treatment schedules once a year, and issues occasional corrections.

As discussed earlier, the treatment vouchers and

![](/api/attachments/ADYDHJK9/fulltext/images/3442c7f8db31be9e2a869f23814b06f5be874382d68a2e5c23acd594384e775c.jpg)  
Fig. 1.

the PHIP treatment schedules are used by the service bureau to print the PHIP claims forms; they are then returned to the doctor's office. Here the treatment vouchers are stapled to the doctor's copy of the claims form and placed in a file of outstanding accounts. When payment is received, as shown in the process payment, the vouchers are removed from the active patient account file, marked "paid", and placed in a file of paid patient accounts (old patient file). Once a month, a statement of accounts receivable is prepared manually and sent to the doctor and his account as an income synopsis for the clinic.

If we wish we can “explode” the process box “prepare claims” to show the breakdown of operations between the service bureau and the doctor’s office. This is shown in Figure 2.

A similar explosion can be made of the “process payment” box; see Figure 3. Note that this introduces, as a data store, the journal in which records of receipts are maintained, and from which the monthly accounts receivable report is produced. This is an example of how detailed information not required at a high-level can be hidden at a lower level of system description (i.e., information hiding).

![](/api/attachments/ADYDHJK9/fulltext/images/515a65e9c536117c7e62570c7edcbe08daea9ed4ba06a186d7eba88de49fa2cb.jpg)

Fig. 2.  
![](/api/attachments/ADYDHJK9/fulltext/images/5ec605e308b58e5dccfedb2f22e3a598e2fe5169528c90c8e5c25059e3c48406.jpg)  
Fig. 3.

## 5. Representing Data Flow Diagrams in SPSL

As already mentioned, DFDs consist of symbols representing external entities, processes, and data stores, linked by directed arcs (usually labelled) representing data flows. The first three of these can be represented by the SPSL objects INTERFACE, PROCESS, and SET respectively. Data flows, however, cannot be represented quite so directly. The data themselves are represented by INPUT, OUTPUT and ENTITY objects named to correspond to the labels on the arcs. The type of object used in a particular case depends upon the type of objects that serve as a source and as the destination of the arc. The several cases appear in Table 1. In order to indicate that a data arc links two particular nodes in the DFD, the SPSL definitions of the source and destination objects must include statements that respectively reflect the transmission and receipt of the data.

As an example of this method, consider the arc labelled “treatment voucher” in Figure 1. It represents the flow of data from the external entity (INTERFACE) “patient” to the process “prepare claims”. This portion of the DFD could be represented in SPSL as follows:

DEFINE INPUT treatment-voucher;
DEFINE INTERFACE patient;

GENERATES treatment-voucher; DEFINE PROCESS prepare-claims;

RECEIVES treatment-voucher;

## 6. Representing System Structure in SPSL

The DFDs shown earlier represent part of the structured approach to systems analysis. The analyst starts by viewing the system in broad terms. This overview is then successively refined by adding details and “exploding” major parts of the system to show internal detail.

Such system structure can be described in SPSL in one of two ways. For example, the “explosion” of the process “prepare-claims” shown in Figure 2 can be represented by the SUBPARTS statement. DEFINE PROCESS prepare-claims;

SUBPARTS ARE print-forms-report,

collate-forms,

prepare-non-PHIP-claims;

The subparts statement can also be used to show structure in INTERFACE, INPUT, and OUTPUT objects. Structure in SET objects, however, is shown by the SUBSETS statement. Thus, for example, if the old patient and new patient files of Figure 1 are viewed initially as a single set, “patient-file”, their difference in function can be identified by subdividing the “patient-file” as follows in SPSL:

DEFINE SET patient-file;

SUBSETS ARE active-patient-file,

old-patient-file.

There are certain drawbacks to this method of representing structure in SPSL. First, the subparts (subsets) must be the same type of object as their parents. Thus, the explosion of “process payment” from Figure 1 to Figure 3 cannot be represented this way, since Figure 3 contains a SET. Also of some concern is the problem of representing data flows. For example, if we wish to show the flow of data into and out of the process “prepare claims”

Table 1

<table><tr><td>Source object</td><td>destination object</td><td>object used to represent the data that flows</td><td>statement used to indicate the source or the of destination of the data flow</td><td>statement used to indicate the data flow</td></tr><tr><td>INTERFACE</td><td>PROCESS</td><td>INPUT</td><td>GENERATES</td><td>RECEIVES</td></tr><tr><td>PROCESS</td><td>INTERFACE</td><td>OUTPUT</td><td>GENERATES</td><td>RECEIVES</td></tr><tr><td>PROCESS</td><td>PROCESS</td><td>ENTITY</td><td>CREATES</td><td>USES</td></tr><tr><td>PROCESS</td><td>SET</td><td>ENTITY</td><td>ADDS/UPDATES *</td><td>CONSISTS OF</td></tr><tr><td>SET</td><td>PROCESS</td><td>ENTITY</td><td>CONSISTS OF</td><td>REFERENCES/REMOVES</td></tr></table>

\* When a PROCESS updates a record in a set (this is shown in a DFD by a bi-directional arc, or by two identically labelled arcs flowing in opposite directions) the data record is represented by an ENTITY, the PROCESS contains a UPDATES statement, and the SET a CONSISTS OF statement.

in Figure 1, we would write the following:
DEFINE PROCESS prepare-claims;
SUBPARTS ARE print-forms-report,
select-PHIP,
collate-forms,
prepare-non-PHIP-claims;
USES treatment-voucher;
GENERATES PHP-claim;
GENERATES WCB-claim;
GENERATES bill;
GENERATES daily-treatment-report;
REFERENCES treatment-code;
ADDS active-treatment-record TO active-patient-file;

This is quite satisfactory but when we define sub-processes, we encounter a situation which is at least, confusing.

GENERATES PHIP-claim;

The OUTPUT “PHIP-claim”, appearing in both definitions, refers in fact to exactly the same data object. Whether the user chooses to duplicate this definition or not is probably dependent on his/her experience and taste. It should be noted that if the same OUTPUT is used twice in this fashion, the completeness checks that form part of SPSA will be in part defeated.

A different approach for indicating structure in SPSL is possible: the KEYWORD statement can be used with any object. All objects that form a logical unit of structure have the same KEYWORD. This can be used as a selection criterion for generating reports or displays later produced by SPSA. Thus the user can effectively examine in isolation any substructure he wishes. Because an object can have many different KEYWORDS, it can be assigned to more than one substructure.

## 7. Graphical Support for Data Flow Diagrams

MONDRIAN [4,7] is a special subsystem of SPSL/SPSA that can automatically generate DFDs from a system description.

Benefits of computer generated DFDs include:

1. time saved (in the order of hours).

2. less errors and omissions; and

3. guidelines for drawing DFDs are incorporated in the automated package.

An interactive spatial-oriented interface DE-PICT [5,6] is also being developed. It present a dynamic window that contains segments of a DFD. Interactive updates to a MONDRIAN generated diagram or a diagram created from “scratch” are possible. The analyst may add, delete or update icons or arcs on a high resolution graphics display via a mouse using a menu selection capability. In addition, details relating to system size, structure and dynamics, and data structure and derivation of an identified system component can be retrieved from the SPSA database and altered using the existing on-line update facility.

## 8. Constructing a Data Dictionary

SPSL is not a language for writing programs, but for writing descriptions or specifications. Many of its statements would be called comments in a programming language. The DESCRIPTION statement is of this type. As a result the user can, with care, build a system description that will relate closely to any programming language to be used later in the system development.

## 8.1. Data Elements

Individual data items are defined in SPSL in ELEMENT sections. This allows the following properties to be defined (as shown in Table 2).

1. Aliases for the data element

2. Related data elements

3. Range of values and meaning of values

4. Length

5. Encoding

6. Other editing information

Names, such as DATE and DATE-IN-FULL, represent the same data expressed in different formats.

This is achieved by defining separate ELEMENT objects with appropriately related names and suitable ATTRIBUTES, as illustrated in lines 6 through 17 in Table 2. In this example, the date a patient is treated appears as a 6-digit number (day/month/year). This same date on a claim to WCB or a private patient might be in full, since these are prepared manually.

Ranges and meanings of values are specified in the VALUES and CODE statements; e.g., scheduled fees for individual X-ray treatments are always less than \$100.00 (line 19 of Table 2). An example of the meaning of data values can be found in our system as well (see lines 22 through 24 of Table 2). The code specifying the type of patient is one of the following – “PHIP”, “WCB”, or “PRIV” – indicating the method of payment.

```txt
1 DEFINE ELEMENT patient-number;
2 SYNONYM IS pat-no;
3 ATTRIBUTES ARE character,
4 pic "A99999".
5 length 6;
6 DEFINE ELEMENT treatment-date;
7 DESCRIPTION;
8 (1)This is the date on which the patient is treated.
9 (2)See also "treatment-date-full" where the same value
10 is expressed with month and year in full
11 (3)Example of general form is "11/12/83";
12 DEFINE ELEMENT treatment-date-full;
13 DESCRIPTION;
14 (1)This is the date on which the patient is treated.
15 (2)See also "treatment-date" where the same value is expressed in numeric form
16 (3)Example of general form is "Dec. 11, 1983";
18 DEFINE ELEMENT scheduled-fee;
19 VALUES ARE 0 THRU 99.99;
20 DEFINE ELEMENT patient-type;
21 VALUES ARE "PHIP", "WCB", "PRIV";
22 CODE "PHIP" MEANS "prov health ins plan";
23 CODE "WCB" MEANS "workmans comp board";
24 CODE "PRIV" MEANS "private-patient";
```

SPSA places a limit on the length of the string that gives the “meaning” in the CODE statement; a literal constant is limited to 24 characters. If abbreviations cannot be used, supplementary text would be included in the DESCRIPTION.

Length and encoding information is specified in an ATTRIBUTES statement. For example, the patient-number code consists of a letter followed by five digits as defined in lines 3 and 4. This is a COBOL-like picture clause, but SPSL is in no way limited to such forms because any meaningful formatting notation can be specified. All of the attributes listed become names in the SPSA database which must conform to the naming rules, and must not be used inconsistently in other parts of the SPSL problem statement.

## 8.2. Describing Data Structures

The basic structural unit is the group, defined in a GROUP section and made up of ELEMENT and other GROUP objects. There are three other components that are closely related: ENTITY, INPUT, and OUTPUT objects, defined in separate sections. They are also made up of GROUP and ELEMENT objects; however, they also represent the concept of data in motion between PROCESS and SET or INTERFACE objects. They are not interchangeable with GROUP objects, although INPUT and OUTPUT objects can have SUBPARTS which are also INPUT and OUTPUT objects respectively.

The data flow marked “patient data” from the INTERFACE “patient” to the PROCESS “create-voucher” is shown in Figure 1. Since this data flow goes from an INTERFACE to a PROCESS it must be represented as an INPUT. From the problem description presented in Section 3 we see that it contains the following patient data: name (last name, initials) address (street, city, province, postal code) phone number method of payment (PHIP, WCB, private) PHIP number referring doctor’s name list of X-rays to be provided

This can be described in SPSL by using an INPUT section that names the data flow and shows its contents in a CONSISTS statement; see lines 1–8 of Table 3.

The third through sixth items on the list of

## Table 3

```txt
1 DEFINE INPUT patient-data;
2 CONSISTS OF patient-name,
3 patient-phone-number,
4 patient-type,
5 patient-PHIP-number,
6 referring-doctor-name,
7 patient-address,
8 X-ray-list;
9
10 DEFINE GROUP patient-name;
11 CONSISTS OF patient-last-name,
12 patient-initials;
13
14 DEFINE GROUP patient-address;
15 CONSISTS OF patient-street,
16 patient-city,
17 patient-province,
18 patient-postal-code;
19
20 DEFINE GROUP X-ray-list;
21 CONSISTS OF 3 X-ray-description;
```

contents are elementary items that would be defined elsewhere in ELEMENT sections. The other three are composite and must be defined in GROUP sections, such as those appearing in lines 10 through 21 of Table 3. In each of these GROUP objects the components are ELEMENT objects. Other GROUP objects could be included, however, if additional levels of structure were needed. For example, “patient-street” could be defined as a group made up of “house-number” and “street-name”.

The last component of “patient-data” is a list of X-ray treatments to be provided. This is an instance of the repeated appearance of a data item in a larger structure; see lines 20 and 21 of Table 3.

The collection of elementary data items into GROUP objects is a convenience provided for the user, but not required by the SPSL language. It is possible, for example, to replace the GROUP objects specified in the INPUT section above with their elementary items.

Sometimes certain components are optional; e.g., the patient's PHIP number is not always included, since it is not needed for WCB or private patients. SPSL does not have a satisfactory way for recording either the optional presence of a component, or the presence of one of set of alternatives. One way of showing that a component is optional is to include it in the CONSISTS statement and insert a note that it is optional in the DESCRIPTION statement. Another is to include a SYSTEM-PARAMETER whose value is 0 or 1 before the ELEMENT.

## 8.3. Describing Data Stores

Data stores are described in SET sections: specifying the contents of the store, its size, any ordering of information within it, whatever subdivisions it has, and how frequently its contents change. The “active patient file” in Figure 1 consists of the records of all patients from the time they are treated until their accounts are paid. In our DFD the patient records are identified by the name “active patient record”. This is defined in lines 1 and 2 of Table 4.

The size of a SET is specified by the CARDINALITY statement which states how many records it is expected to contain. For our example system (see Section 4) this is 3000 entries. An appropriate CARDINALITY statement appears in line 3 of Table 4.

In this example the number 3000 is intended to give a rough measure of the size of the SET, not an exact value. It is possible, of course, to have a SET that does not always have a fixed number of records. If an estimate is intended, this can be shown as follows by using a SYSTEM-PARAMETER for the CARDINALITY: SYSTEM-PARAMETER no-of-records;

VALUE IS "approximately 3000";

SYSTEM-PARAMETER no-of-records;

VALUE IS 2500 THRU 3500;

In the active patient file the records are arranged in sequence by patient number as shown in the ORDERED BY statement of line 4 in Table 4.

A concept that is somewhat related to the ordering of records within a SET is that of identifying individual records. SPSL regards this as a characteristic of the record itself, and requires that it be specified in the ENTITY section as follows: DEFINE ENTITY active-PHIP-pat-rec;

IDENTIFIED BY patient-number;

Subdivision into subparts can be described in SPSL through the use of the SUBSETS and SUB-SETTING-CRITERIA statements; see lines 5 through 7 of Table 4. The names in the SUBSETS statement are SET names, and, unless otherwise specified, have the same properties as their parent. Alternatively, the SET can be defined simply as having SUBSETS.

## Table 4

```txt
1 DEFINE SET active-patient-file;
2 CONSISTS OF active-pat-rec,
3 CARDINALITY IS 3000;
4 ORDERED BY patient-number;
5 SUBSETS ARE PHIP-patient,
6 WCB-patient,
7 private-patient;
8 SUBSETTING-CRITERIA IS patient-type;
9 VOLATILITY-SET;
10 New patient records are added daily.
11 Records of patients whose accounts
12 have been paid are removed monthly;
13 VOLATILITY-MEMBER;
14 The average lifetime of a record
15 in the file is 8 through 12 weeks;
16 DERIVATION;
17 Customer records are created and added
18 to the file by the processes “collate-forms”
19 and “prepare-non-PHIP-claims”;
```

VOLATILITY-SET and VOLATILITY-MEMBER statements, like DESCRIPTION, are comment-type statements. The user can include them to describe how rapidly the SET and its members change.

Finally, SPSL provides a DERIVATION statement (lines 16 through 19 in Table 4), a comment-type statement, that allows a description of the source of information.

Several other statements can occur in an ENTITY section when it is a member of a SET. A CARDINALITY statement specifies how often instances of the ENTITY occur in the system. VOLATILITY of an ENTITY may also be stated. Finally one can include a statement that specifies how an individual instance of an ENTITY can be identified. Table 5 shows these additional definitional capabilities for describing an ENTITY.

## 9. Describing Processes

SPSL is not a programming language in the ordinary sense. It is a computer processable language designed to describe a target system during its formative stage, or to describe and existing system at a comparable level of detail. Neverthe-

## Table 5

```sql
DEFINE ENTITY active-pat-rec;
DESCRIPTION;
This consists of the treatment
voucher for an active patient.
The “patient-PHIP-number” appearing
in the CONSISTS statement is optional;
CARDINALITY IS 300;
CONSISTS OF patient-number,
patient-name,
patient-address,
patient-phone-number,
patient-type,
patient-PHIP-number,
treatment-code-list,
treatment-code-list,
doctor-code,
X-ray-list;
IDENTIFIED BY patient-number;
VOLTATILITY;
These entities are created daily. They
remain in the active patient file until
the account is paid
– usually 8 through 12 weeks;
```

less, the analyst cannot choose to ignore processes entirely.

Specifying the inputs and outputs to a process provides a process description at a level appropriate to this stage of analysis. However, it is often desirable to indicate more about its internal functions. For example, UPDATES implies a particular kind of process-reading a record, making some change in it and replacing it in its data store; CREATES and GENERATES statements imply its creation and generation. This is illustrated in the following examples that correspond to the process “print-forms-reports” of Figure 2. This process created the ENTITY “PHIP-claim” (see Table 6) and GENERATES the OUTPUT “daily-treatment-report” (see Table 7).

The ELEMENT total-patient-claim has not appeared before in our discussion, and warrants further attention. As its name suggests, it represents the total claim for all the treatments given to the patient. This is computed by the process and can be shown by including a DERIVES statement.

Internal processing can also be shown by use of the MODIFIES statement which indicates that changes are made to ENTITY objects (such as records in a file). This statement is particularly appropriate in conjunction with the UPDATES statement. Again, a USING clause may be inserted to indicate the data used for the modifica-

CREATES PHIP-claim USING patient-number,
patient-name,
patient-address,
patient-PHIP-number,
treatment-date,
referring-doctor-name,
radiologist-name,
radiologist-address,
radiologist-PHIP-code,
X-ray list,
total-patient-claim;

GENERATES daily-treatment-report USING treatment-date,
patient-number,
patient-name,
X-ray-list,
total-patient-claim,
past-claims-summary;

tion. It does not, however, permit us to specify which components in the ENTITY are being changed.

The UTILIZES statement shows that a process makes use of some standard procedure; this might be a library subroutine, such as SORT.

The PROCEDURE statement can also be useful. It is a comment-type statement that in principle one could use to list the code for a computer program, although as indicated earlier this level of detail is rarely appropriate at the analysis stage. Consideration could be given to inserting high-level algorithms expressed, for example, in “Structured English” [3] at this detailed analysis stage.

## 9.1. Process Initiation and Synchronization

Process initiation and synchronization can be specified using the CONDITION and EVENT sections, and the TRIGGERS and CAUSES statements.

If the PROCESS “make-acc-rec-report” of Figure 3 is to occur at the end of each month, this can be shown by defining an EVENT as follows.
DEFINE EVENT end-of-month;

HAPPENS 1 TIME-PER month;

TRIGGERS make-acc-rec-report;

Often processes are to be performed in sequence. For example, in Figure 2 the PROCESS "select-PHIP" is to take place after the PROCESS "print-forms-reports"; this can be specified by: DEFINE PROCESS print-forms-reports;

TERMINATION-TRIGGERS select-PHIP;

The CONDITION section can be used to indicate that a PROCESS will be performed only under certain conditions. For example, in Figure 2 the PROCESS “collate-forms” is performed only for patients whose bills are to be submitted to PHIP. For all other patients the PROCESS “prepare-non-PHIP-claims” is to be carried out. This can be shown by the following: DEFINE CONDITION PHIP-case;

TRUE-WHILE;

patient-type = "PHIP" and

PROCESS "select-PHIP" is complete;

FALSE-WHILE;

PROCESS "select-PHIP" is complete;

BECOMING TRUE TRIGGERS collate-forms;

BECOMING FALSE TRIGGERS prepare-non-PHIP-claim;

It should be noted that the TRUE-WHILE and FALSE-WHILE statements are comment-type, and so can be used to specify the true and false conditions in a very flexible manner. Yet another type of synchronization arises when a system output produces a response from an interface. A case in point in our example system arises when the submission of a claim to PHP produces (we expect) a payment from PHP. This can be shown by including a CAUSE-RESPONSE statement in the appropriate OUTPUT section as follows:

DEFINE OUTPUT PHIP-claim;

CAUSES-RESPONSE PHIP-payment;

System dynamics can be indicated in many other ways. EVENT, INPUT, OUTPUT and PROCESS objects can all be described as occurring at stated time intervals through use of the HAPPENS statement. CONDITION, EVENT, INPUT and PROCESS objects can trigger PROCESS objects. INPUT, OUTPUT and PROCESS objects can all CAUSE EVENTS. These types of process initiations are all described in the SPSL/SPSA Primer [2].

## 10. Producing System Dictionaries

The SPSA analyzer accepts a system description and stores it; it performs a syntactic check on the SPSL statements and produces appropriate error messages. It can also be used to prepare a variety of reports.

The Dictionary Report, produced by first obtaining a list of all object names of interest to the analyst using the Name Selection Report, contains only the names of the system components together with their types, keywords, synonyms and any DESCRIPTION statements that are included in the SPSL sections that define them.

A listing of the SPSL problem description is, in a sense, a form of dictionary. Such a listing is, of course, produced when SPSA compiles the SPSL code into a database. It is not, however, likely to be in a usable form since it is merely a copy of the source statements. Unless the user has taken particular care in writing the problem description, the entries (the SPSL sections) will not be in alphabetic order. Nor need they be neatly formatted.

As the analysis progresses it is likely that changes will have to be made in the original listing. If these changes are incorporated into the original source statements and the modified version re-compiled, a new and up-to-date source listing would be produced. However, it is more likely that changes would be made directly and interactively to the SPSA database through use of the on-line UPDATE facility. In this case a source listing need not be produced and, therefore, any dictionary based solely on the source description would soon become out of date.

Fortunately SPSA does provide the means to prepare a dictionary based upon the SPSL section definitions. This is the Formatted Problem Statement Report. It produces for each system component requested, an SPSL listing that is reconstructed from the database. This has a number of advantages. First, if the list of names for which entries are to appear is in alphabetic order, then so will the entries in the Formatted Problem Statement Report. This will automatically be the case if the list of names is produced by the Name Selection Report. Second, the output is in a standard format. It is not the original source but a reconstruction. Thus the user need not write his original source statements in a fixed form to obtain a standard dictionary appearance.

In the foregoing we have been discussing the dictionary in terms of printed (hard copy) output. SPSA, through its UPDATE command, allows dictionary entries (SPSL sections) to be displayed interactively on a computer terminal.

## 11. Conclusion

Over the past two years the SPSL/SPSA system has been used and tested in the analysis of several significant projects involving local firms in a full year course in Information Analysis and Design given at the University of Saskatchewan [10]. Serious attempts have been made to use structured systems analysis techniques in conjunction with documenting the system, however, the methodology has not been rigorously applied. This paper provides a guide to the successful integration of the tool and the technique.

Because SPSL/SPSA was designed without the support of a specific methodology in mind, some problems exist in using it in a structured systems analysis context. Specifically, there are difficulties in representing data flow. The automatic generation of data flow diagrams, which is made possible by using the system MONDRIAN [4,7], is in prototype stage of development. Facilities needed in SPSL/SPSA to support system prototyping are now being addressed. The addition of a spatial-oriented DFD interface should enhance the system usability.

The long-term goal of the DEVIEW project is to produce a system environment that would assist the analyst/designer in the formative stages of system development. This tool must support the application of generally accepted methodologies such as structured systems analysis [3] and design [15], yet also allow the user immediate feedback and direct involvement in the evolution of the system. Ultimately, it is hoped that relatively unsophisticated users would be able to express their requirements directly to a system that could assist in producing the desired information system. While undoubtedly the inception of a fully automated development system is some time off for large, complex information systems, it may be close at hand for small, special purpose application systems.

## Acknowledgements

The authors would like to thank Beth Protsko for assisting in the preparation of the paper and the editor for his valuable comments. The work was supported by NSERC Grants A9290 and A9294.

## References

[1] O.J. Dahl, E.W. Dijkstra, and C.A.R. Hoare, Structured Programming, Academic Press, London, 1972.

[2] A. Friesen, E. Wig, J.P. Tremblay, and P.G. Sorenson, "SPSL/SPSA Primer (Version 1.1)", Department of computational Science, Technical Report 82-5 (1982), University of Saskatchewan.

[3] C. Gane, and T. Sarson, Structured Systems Analysis: Tools and Techniques, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1979.

[4] L.B. Protsko, Placement and Routing Algorithms for the Automatic Generation of Data Flow Diagrams M.Sc. Thesis, Department of Computational Science, University of Saskatchewan, Saskatoon, Saskatchewan, November, 1983.

[5] L.B. Protsko, G.P.A. Kurtenbach, P.G. Sorenson and J.P. tremblay, “DEPICT: A Graphical Interface for System Analysis and Design”, HICSS-18 Conference, 1985.

[6] L.B. Protsko, G.P.A. Kurtenbach, P.G. Sorenson, and J.P. Tremblay, 'Design of a Graphics Database in Support of Computer-Aided Information Systems Development', HICSS-18 Conference, 1985.

[7] L.B. Protsko, P.G. Sorenson, and J.P. Tremblay, "MONDRIAN: A System to Produce Automatically Data Flow Diagrams from an SPSA Data Base", in preparation.

[8] P.G. Sorenson, J.P. Tremblay, and A.W. Friesen, "SPSL/SPSA: a Minicomputer Database System for Structured Systems Analysis and Design", Proc. Joint SIGSMALL and SIGMOD Workshop on Database Systems, Orlando, October 13–15, 1981, pp. 109–116.

[9] D. Teichroew, and E. Hershey, "PSL/PSA: A Computer Aided Technique for Structured Documentation and Analysis of Information Systems", IEEE Transactions on Software Engineering, Vol. SE-3, No. 1, 1977 pp. 48–58.

[10] J.P. Tremblay and P.G. Sorenson, “The Use of Automated Analysis and Design Aids in the Teaching of Information Systems”, Computers in Education North-Holland Publishing Company, IFIP, 1981, pp. 409–416.

[11] J.P. Tremblay, P.G. Sorenson, E.D. Wig, and D.R. Perkins, "A Survey of Some Automated Aids for Systems Analysis and Documentation", INFOR, vol 19, no. 3, August, 1981, pp. 205–229.

[12] J.A. Wald, and P.G. Sorenson, “Productivity Tools for a Database Management System”, Proceedings of COMPSAC 83, Chicago, Nov. 1983, pp. 1879–187.

[13] E.D. Wig, "Computer Aided Systems Analysis Reporting", Technical Report 79–6, Department of Computational Science, University of Saskatchewan, Saskatoon, Saskatchewan, 1979.

[14] E.D. Wig, PSL/PSA Reporting and Prototype Output Generation Facilities in a Minicomputer Environment, M.Sc. Thesis, Department of Computational Science, University of Saskatchewan, Saskatoon, Saskatchewan, June, 1979.

[15] E. Yourdon and L. Constantine, Structured Design, Prentice-Hall, Inc., Englewood Cliffs, New Jersey, 1979.
