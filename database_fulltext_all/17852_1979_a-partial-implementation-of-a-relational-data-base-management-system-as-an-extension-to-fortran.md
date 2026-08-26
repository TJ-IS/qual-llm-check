---
otero_id: 17852
otero_key: "4G2CJ2QB"
title: "A partial implementation of a relational data-base management system as an extension to FORTRAN"
authors: "R.K. Bagga; V. Rajaraman"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90023-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Partial Implementation of a Relational Data-Base Management System as an Extension to FORTRAN

Lt. Col. R.K. Bagga

Computer Centre, DRDL, Hyderabad, India

and

Prof. V. Rajaraman

Computer Centre, Indian Institute of Technology, Kanpur, India

In general applications of a Data Base Management System (DBMS) for centralised monitoring of a medium sized data base, a Relational approach is often said to be preferred to a Hierarchical or a Network approach, because of its simplicity and ease of usage. An experimental Relational DBMS has been implemented at the Computer Centre of the Indian Institute of Technology, Kanpur, India. This system provides most of the facilities required for a Data Model Definition, Data Sub-language, and Data Manipulation Language. The FORTRAN language was selected as the host, because of its popularity and the available system software. The resulting DBMS has been tested on live data and the results have been encouraging.

Keywords: Data Base, DBMS, Relational Approach, Date Model Definition, Data Sub-Language, Data Manipulation Language, FORTRAN.

## 1. Introduction

At the Indian Institute of Technology, Kanpur, India, we have made a partial implementation of a relational DBMS as an extension to FORTRAN. This paper deals with the implementation details and its use with a medium sized data base.

There are three major data models that are encountered in modern DBMS:

\* The Hierarchical Model

\* The Network of "CODASYL DBTG" Model

\* The Relational Model

A special issue of ACM's Computing Surveys discussed in details all three models [1]. Comparisons of these three approaches show that there is no overall best choice: each approach will meet the needs of a portion of the diverse users community.

The Relational approach was introduced by Codd [2] in 1970, and when we decided to implement a relational DBMS, the concept was still in an experimental stage at universities and research laboratories. However some relational system like Tymshare's

![](/api/attachments/4G2CJ2QB/fulltext/images/c4a0d5a1aea9e634475f9c6247fc58ffedaa31c7892de7ce42cc2a93fce06429.jpg)

MAGNUM [3] and IBM's ADL [4] have since become commercially available.

## 2. The Relational Approach

The Relational Approach for data model is based on the realization that files that obey certain constraints may be considered as mathematical relations, and hence elementary relation theory may be brought to bear on various practical problems of dealing with data in such files. It is customary, (though not essential) when discussing relations to represent a relation as a 'table'. One such relation named PROJ is shown in Table 1. In the tabular representation of a relation, the following properties (which derive from the definition of a relation) should be observed:

(1) No two rows (tuples) are identical;

(2) The ordering of rows is not significant;

(3) The ordering of columns is significant. However, if any individual column is referenced by the appropriate domain name and not by its relative position, then the ordering of the columns is not significant.

(4) Every value within a relation is an atomic data item (i.e., it is not decomposable into other items).

## 2.1. Normalisation

The last property of the above relations brings the most important concept of normalisation in the relational approach. Normalisation theory begins with the observation that certain collection of relations have better properties in an updating environment than do other collection of relations containing the same data. This is a formal way of expressing a very simple idea; that each relation should describe a single 'concept'. If more than one concept is found in a relation, the relation should be split into smaller relations. Some of the basic concepts of Normalisation have been discussed in [5]. The notion of functional dependence (within a relation) is of paramount importance in understanding normalisation. This may be looked on as a mathematical formulation of the concept of a unique key and relationships between keys.

Given a relation R, we say that attribute Y of R is functionally dependent on attribute X of R if and only if each X-value in R has associated with it precisely one Y-value in R (at any one time). Note that the same X-value may appear in many different tuples of R; if Y is functionally dependant on X, the definition tells us that every one of these tuples must contain the same Y-value. In our relation PROJ for example, attributes QRNO, TYPE, NAME, LAB and PRNO are each functionally dependent on attribute CODE. Given a particular CODE value, there exists precisely one corresponding value for each of QRNO, TYPE, NAME, LAB and PRNO. The functional dependencies of relation PROJ are diagrammatically shown in Fig. 1.

Normalisation theory involves a series of Normal Forms -- four in number -- which provide successive improvements in update properties of the data base. These are:

1. First Normal Form (1NF) - A relation in first Normal Form is a relation in which each component of each tube is non decomposable, i.e., the component is not a set sequence, or a relation. The relations in first normal form are sometime called 'flat files'.

2. Second Normal Form (2 NF) - A relation $R$ is said to be in second normal form if and only if, the non-key domains of $R$ , if any, are functionally dependant on the primary key of $R$ ; i.e., there is one designated primary key on which all other elements depend.

TABLE 1  
Example of a Relation named PROJ

<table><tr><td>CODE</td><td>QR No</td><td>TYPE</td><td>NAME</td><td>LAB</td><td>PR No</td></tr><tr><td>1</td><td>571</td><td>1</td><td>IONO SCATTER</td><td>PRL AHMEDABAD</td><td>RD-P1-69/RRL-5</td></tr><tr><td>2</td><td>823</td><td>3</td><td>BALLOON FACILITY</td><td>PRL AHMEDABAD</td><td>SL-P2-71/RRL-9</td></tr><tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr><tr><td>1001</td><td>23</td><td>2</td><td>GPA FOR SET 25</td><td>RRL HYDERABAD</td><td>SL-PX-60/RRL/18</td></tr><tr><td>1002</td><td>938</td><td>5</td><td>TROPO EQUIPMENT</td><td>RRL DYDERABAD</td><td>RD-P1-67/RRL-24</td></tr></table>

![](/api/attachments/4G2CJ2QB/fulltext/images/ad2576f02128dc750d4e643165d0426519c5d103121b95ad6d62d736afdc32b9.jpg)  
Fig. 1. Functional Dependencies of Relation RROJ in 4NF.

3. Third Normal Form (3 NF) - A related $R$ is said to be in 3 NF if it is in 2NF and, every non-key attribute is nontransitively dependent on the primary key.

4. Fourth Normal Form (4 NF) - A relation $R$ is said to be in 4NF if and only if, for all time each tuple of $R$ consists of a primary key value that identified some entity, together with a set of mutually independent attribute values that describe the entity in some way.

For example, the relation PROJ is in 4 NF. Each tuple consists of a CODE value, identifying some particular project together with five pieces of descriptive information concerning that project-type, qualitative requirement, name, laboratory, and number. Moreover each of these five descriptive items is independent of the other four. The design of a data base in 4 NF depends on a knowledge of the functional dependencies among the attributes of the data. The knowledge cannot be discovered automatically, but must be furnished by the Data Base designer who understands the semantics of the information.

## 2.2. Language for the Relational System

There are a large variety of languages for accessing or otherwise using a relational DBMS; four classes of these are relational calculus, relational algebra, mapping oriented languages, and graphic oriented languages. For a general discussion on features of these languages, the reader is referred to [6].

Codd presented the details of a data sub-language (DSL ALPHA) based on relational calculus [7]. A typical query in ALPHA has two parts: a target that specifies the particular attributes that are to be returned, and a qualification that selects particular tuples from the target relation. In the present implementation, an attempt has been made to provide most of features of DSL ALPHA.

## 3. System Design

Fig. 2 shows the block schematic of the overall system view of the Relational DBMS as implemented at the Indian Institute of Technology, Kanpur. A brief description of the important modules and their functions are given in the following paragraphs.

![](/api/attachments/4G2CJ2QB/fulltext/images/a26457edc8d79fc32bf06b6d3eb76e340d8c32ed26738c4e0b78fbb08aad6608.jpg)  
Fig. 2. Overall Block Schematic of System Design.

## 3.1. Data Model Definition (DMD)

The DMD includes the definitions of all the relations and their domains. For simplicity, the first domain in each of the relations has been reserved for the Key. The following commands are to be used for initial creation of the data base:

## 1. RELN NAME AC

This command defines a relation, its name and access code.

## 2. FLDS NAME IN FORMATS FIXED IN-INTEGER 15 AN-ALPHA 10A2 AD-ALPHA 30A2

This command defines a field or item name, and its type whether INTEGER, ALPHA-NUMERIC (SINGLE OR DOUBLE). For simplicity, fixed formats are used.

## 3. DATA 99

This command indicates that all domain definition for the relation have been completed and data tuples follow. The number of tuples to be included in the relation are given.

## 4. IEND

This command indicates the end of the DMD and completion of the Data Definition phase for all relations.

Let us take an example of a data base of a number of research laboratories, where a number of projects are undertaken. Table 2 shows a DMD which creates three relations concerning the project, its progress, and funds positions named PROJ, PORG, and FUND. Relation PROG gives the progress of each of the projects, whereas FUND indicates details of sanctioned funding (Foreign Exchange, Rupee Element, and Totals), and expenses.

## 3.2. DMD Analyser

The DMD analyser is the main software which checks the validity of each of the commands of the DMD and builds up various tables as part of the data structure module. It also prepares the INDEX for the various storage devices, and places the relation on physical devices in conjunction with the Data Base Operating System. It consists of the following modules:

1. MAIN Scanner

2. IRELN Routine

3. IFLDS Routine

4. IOPT Routine

5. ICON Routine

TABLE 2  
Example of Data Model Definition for three relations: PROJ, PROG and FUND

<table><tr><td>RELN</td><td>PROJ</td><td>AB</td></tr><tr><td>FLDS</td><td>CODE</td><td>IN</td></tr><tr><td>FLDS</td><td>QRNO</td><td>IN</td></tr><tr><td>FLDS</td><td>TYPE</td><td>IN</td></tr><tr><td>FLDS</td><td>NAME</td><td>AN</td></tr><tr><td>FLDS</td><td>LAB</td><td>AN</td></tr><tr><td>FLDS</td><td>PRNO</td><td>AN</td></tr><tr><td>DATA</td><td>95</td><td></td></tr><tr><td>RELN</td><td>PROG</td><td>AB</td></tr><tr><td>FLDS</td><td>CODE</td><td>IN</td></tr><tr><td>DATA</td><td>POSN</td><td>AD</td></tr><tr><td>RELN</td><td>95</td><td></td></tr><tr><td>FLDS</td><td>FUND</td><td>AB</td></tr><tr><td>FLDS</td><td>CODE</td><td>IN</td></tr><tr><td>FLDS</td><td>SARE</td><td>IN</td></tr><tr><td>FLDS</td><td>SAFE</td><td>IN</td></tr><tr><td>FLDS</td><td>SATL</td><td>IN</td></tr><tr><td>FLDS</td><td>SPRE</td><td>IN</td></tr><tr><td>FLDS</td><td>SPFE</td><td>IN</td></tr><tr><td>FLDS</td><td>SPTL</td><td>IN</td></tr><tr><td>DATA</td><td>BALN</td><td>IN</td></tr><tr><td>IEND</td><td>95</td><td></td></tr></table>

## 3.2.1. Main Scanner

The functions performed by the MAIN Scanner are:

1. Initialisation of all tables, pointers, and variable codes.

2. Validating the RELN Command, storing the relation name and its access code.

3. Validating the FLDS commands and storing the field name and type in FTAB for all items.

4. Testing for the DATA command and ascertaining the number of tuples in the initial relation. Working out the extra space for adding tuples during run time. The ICON routine is used for converting from Alpha to Integer format.

5. Building the Data structure RTAB after disk storage details have been worked out.

6. Using subroutine IOPT for input/output from any device to system buffers and from system buffer to the appropriate device. All the relation tuples are placed on the secondary storage and an index is maintained in RTAB.

7. Testing for IEND command after each relation; if not, it checks for a fresh RELN card and repeats [2] to [6] until an IEND command is encountered.

8. Storing all system tables RTAB, FTAB and RFDIR in system area. The contents of system tables, after definition of three relations is shown in Tables 3, 4 and 5.

## 3.2.2. IRELN Routine

The following functions are performed for IRELN:

1. Initialisation of parameters when the new relation is encountered.

2. Testing relation name. If a relation with the same name has earlier been defined, give an error message.

3. Incrementing the pointers.

4. Allocating a suitable device number, depending on how many relations have been defined so far.

5. Maintaining an index of the relation on a particular device and its relative location.

## 3.2.3. IFLDS Routine

The IFLDS routine performs the following functions:

1. Increments pointer both for FTAB and RFDIR.

TABLE 3  
RTAB Parameter after three relations have been defined

<table><tr><td colspan="6"></td><td colspan="3">FORMATS</td></tr><tr><td>RELATIONID(RELID)</td><td>NAME OF RELATION(NAME)</td><td>DEVICE NO(DNO)</td><td>STARTING POSITION(SP)</td><td>ACCESS CODE(AC)</td><td>NO OF TUPLES(N)</td><td>INTEGER(IN)</td><td>ALPHA(NA)</td><td>ALPHA DOUBLE(AD)</td></tr><tr><td>1.</td><td>PROJ</td><td>4</td><td>1</td><td>AB</td><td>95</td><td>3</td><td>3</td><td>0</td></tr><tr><td>2.</td><td>PROG</td><td>4</td><td>106</td><td>AB</td><td>95</td><td>1</td><td>0</td><td>1</td></tr><tr><td>3.</td><td>FUND</td><td>4</td><td>211</td><td>AB</td><td>95</td><td>8</td><td>0</td><td>0</td></tr></table>

TABLE 4  
FTAB contents after DMD analyser has created three relations

<table><tr><td>FIELD IN (FLDID)</td><td>FIELD NAME (FNAME)</td><td>FORMAT (FOT)</td></tr><tr><td>1</td><td>CODE</td><td>1</td></tr><tr><td>2</td><td>ORNO</td><td>1</td></tr><tr><td>3</td><td>TYPE</td><td>1</td></tr><tr><td>4</td><td>NAME</td><td>2</td></tr><tr><td>5</td><td>LAB</td><td>2</td></tr><tr><td>6</td><td>PRNO</td><td>2</td></tr><tr><td>7</td><td>POSN</td><td>3</td></tr><tr><td>8</td><td>SARE</td><td>1</td></tr><tr><td>9</td><td>SAFE</td><td>1</td></tr><tr><td>10</td><td>SATL</td><td>1</td></tr><tr><td>11</td><td>SPRE</td><td>1</td></tr><tr><td>12</td><td>SPFE</td><td>1</td></tr><tr><td>13</td><td>SPTL</td><td>1</td></tr><tr><td>14</td><td>BALN</td><td>1</td></tr></table>

TABLE 5  
RFDIR Contents after the definition

<table><tr><td>RELID</td><td>FLDID</td><td>FOT</td></tr><tr><td>1</td><td>1</td><td>1</td></tr><tr><td>1</td><td>2</td><td>1</td></tr><tr><td>1</td><td>3</td><td>1</td></tr><tr><td>1</td><td>4</td><td>2</td></tr><tr><td>1</td><td>5</td><td>2</td></tr><tr><td>1</td><td>6</td><td>2</td></tr><tr><td>2</td><td>1</td><td>1</td></tr><tr><td>2</td><td>7</td><td>3</td></tr><tr><td>3</td><td>1</td><td>1</td></tr><tr><td>3</td><td>8</td><td>1</td></tr><tr><td>3</td><td>9</td><td>1</td></tr><tr><td>3</td><td>10</td><td>1</td></tr><tr><td>3</td><td>11</td><td>1</td></tr><tr><td>3</td><td>12</td><td>1</td></tr><tr><td>3</td><td>13</td><td>1</td></tr><tr><td>3</td><td>14</td><td>1</td></tr></table>

2. Tests whether the item or field name has earlier been defined to enter the proper FLDID.

3. Tests whether it is a new field name, in which case a fresh FLDID is allotted and a record kept in FTAB (which functions as a Data Dictionary).

4. Checks for an appropriate type and makes a corresponding entry in RFDIR. The type of formats corresponding entry in RFDIR. The type of formats used are given in Table 6. Considering the type of application, it was felt that any data could be converted into the above three formats without any loss of information.

## 3.2.4. IOPT Routine

This is a general purpose subroutine to provide all types of input and output facilities for different devices. The TDC-FORTRAN provides a very flexible N-Format, which has been used to provide any combination of IN, AN, or AD formats [8]. BUFF (10,40) is the system buffer used by this subroutine. The IOPT Subroutine is used in the Data Sub-Language routines as an input/output facility: thus the routine also tests whether the user level corresponds to "read only" or both "read and write" access. If a "read only" user tries to write in the data base, an appropriate error is indicated and access terminated.

TABLE 6

<table><tr><td>Format</td><td>Alpha-numeric Code</td><td>Integer Code</td></tr><tr><td>I5</td><td>IN</td><td>1</td></tr><tr><td>10A2</td><td>AN</td><td>2</td></tr><tr><td>30A2</td><td>AD</td><td>3</td></tr></table>

## 3.2.5. ICON Routine

Like IOPT, ICON is a general purpose utility routine which converts the integer values read in Alphanumeric format to integer format for computational usage. ICON unpacks the digits and, depending upon their codes, works out the corresponding integer value.

## 3.3. Data Sub-Language Routines (DSL)

There are six different routines used to perform various retrieval functions for the user, any of these can be called from the user program. Brief description of each of these is now given.

## 3.3.1. GETO

This subroutine provides a particular record occurrence or tuple once the relation ID, tuple number, and rewind option is specified. The functions of the subroutine are:

1. Locate the Relation ID in RTAB.

2. Find (from the index) on which particular device this relation is stored.

3. On that device, find the first relation and its parameters.

4. Traverse all relations in sequence until the desired relation beginning is achieved.

5. Knowing the displacement of the tuple, traverse until the desired tuple is found.

6. Output the tuple to the user work area.

7. Depending on the position of the rewind flag, rewind the device before returning.

## 3.3.2. GETF

This subroutine is an extension of subroutine GETO, which obtains a particular tuple in a relation. The present subroutine finds out the position and format of the desired item/field whose ID has been specified. It brings the value into the user work area. An Example of the use of GETF is shown in Fig. 3.

## 3.3.3. GETR

This is a basic subroutine which outputs a complete relation once a relation ID has been specified. The same function could be achieved by using GETO until all the tuples of a relations are obtained. Here the relation ID is located in RTAB and the index is searched to locate the relation. Once located, the relation is transferred to the user work area.

## 3.3.4. GETV

This is a very useful routine for inverted file type of queries. The sub routine scans a particular given field/item of a relation for the given value. Once the match is obtained in the given field, the corresponding value of the required field is transferred to the buffer according to the format. Extensive use of other routines like GETF, GETO, BSERCH is made in this routine. A condition can be set in the subroutine to ensure that the first value is output or that all values satisfying the requirement are output. In case of no match of the given value, a flag is set and an error message is returned. A simple example of finding the first five projects assigned to a particular research laboratory is shown in outline in Fig. 4.

## 3.4.5. GETU

GETU is one of the important routines which retrieves a number of different fields in different relations based on the primary key of the first relation. This is an unqualified GET routine, where no conditions are to be matched. It extensively uses other routines (Like GETF, GETV). The relation ID's

PROGRAM EXTRACT
C DECLARATIVE STATEMENTS AND INITIALISATION
CALL OPEN
C RELID TO BE MODIFIED-MRID FLDID TO BE MODIFIED-MFID
C RECORD OCCURANCE ... MIOR USER WORK AREA - IUSR
C TEMPORARY ARRAY TO TEST GETF - IV
READ (5, 140) MRID, MFID, MIOR, (IUSR (1, K), K = 1, 10)
140 FORMAT (315, 30A2)
C TESTING FOR EXISTING VALUE
CALL GETF (MRID MFID, MIOR, IV)
WRITE (6, 240) (IV(K), K = 1, 10)
240 FORMAT ('EXISTING VALUE IN FIELD', 5X, 10A2)
CALL MDYREC (MRID, MFID, MIOR, IUSR)
WRITE (6, 250) MRID, MFID, MIOR, (IUSR (1, K), K = 1, 10)
250 FORMAT (5X, 'MODIFY RELID', 15, 2X, 'FLDID', 15, 2X, 'IOR',
15, 2X, 'AS FOLLOWS'/25X, 10A2)
C TESTING FOR MODIFIED VALUE
CALL GETF (MRID, FMID, MIOR, IV)
WRITE (6, 240) (IV(K), K = 1, 10)
STOP
END
OUTPUT EXTRACT
EXISTING VALUE IN FIELD ... RRL HYDERABAD
MODIFY RELID 1 FLDID 5 IOR 6 AS FOLLOWS
PRL AHMEDABAD
EXISTING VALUE IN FIELD ... PRL AHMEDABAD

Fig. 3. Extracts of Program to Output and to Modify a particular field using subroutine MDYREC. GETF Routine is used for testing existing and corrected value.

and the corresponding fields are required to be stored in two arrays prior to using the subroutine. This type of retrieval may be required when a particular report is to be generated.

## 3.4.6. GETQ

This is the most complex of all the search routines. It retrieves a number of fields/items subject to qualification fields satisfying a particular condition. Six relational condition operators are used for matching values. Extensive use of earlier routines GETO, GETV is made. A common field matrix is used for moving from one relation to the other. The output is ordered according to the primary key of the qualification field. As another example, fig. 5 shows an extract program that obtains the project number, research laboratory, and progress of all projects, where sanctioned funds exceed a specified level, say 5 lakh rupees.

## 3.4. Data Manipulation Routines

There are four different routines providing the manipulation facilities for various record occurrences and the relations. Their description is now given.

## 3.4.1. ADDREL Routine

ADDREL is one of the data manipulation routines which adds a new relation during run time. It is a privileged routine which can be called by the DBA or a systems analyst with a security level less than 10. The entire data required has to be available in the user work area, including the name of the relation and the names of the various data items/fields. The subroutine searches for any space left after deletion of a previous relation with a similar or less space requirement. If space is found the added relation will be stored with the same DNO, otherwise a fresh area is located at the end of all DNO's and the full relation is stored. The Relation name is entered into RTAB and all new fields/item names are put in FTAB. RFDIR is updated. Once the relation details are amended permanently, the system area tables must be rewritten; this is done by subroutine CLOSE.

```csv
PROGRAM EXTRACT
C DECLARATIVE STATEMENTS AND INITIALIZATION
CALL OPEN
C TARGET RELATION - TRT TARGET FIELD - TRF
C OUTPUT TO BE STORED IN - IUSR (USER WORK AREA)
C QUALIFICATION FIELD - IQF QUALIFICATION VALUE - 1G
C NO OF TUPLES REQUIRED IF CONDITION IS SATISFIED - ION
READ (5, 110) TRT, TRF, IQF, ION, (1G(I), I = 1, 30)
110 FORMAT (4I5, 30A2)
CALL GETV (TRT, IQF, IG, TRF, IUSR, ION)
WRITE (6, 210) ION, TRT, TRF, IQF, (IG(I), I = 1, 30)
210 FORMAT ('GET FIRST' 15, 'TUPLES FROM RELID', 15, 2X,
'FLDID', 15, 2X, 'WHERE VALUE FLDID', 15, 2X, 'IS AS
FOLLOWS'/30X, 30A2)
WRITE (6, 220) (IUSR (J.K), J = 1, ION), K = 1, 30)
220 FORMAT (10X, 30A2)
STOP
END
OUTPUT EXTRACT
GET FIRST 5 TUPLES FROM RELID 1 FLDID 6 WHERE -
VALUE OF FLDID 5 IS AS FOLLOWS
RRL HYDERABAD
SL-PX-66/RRL-18
RD-P1-67/RRL-24
SA-PX-67/RRL-26
SN-P1-68/RRL-28
SN-P1-68/RRL-39
```  
Fig. 4. Extract of Program and Output for finding any field, with qualification, from a single Relation using GETV.

## 3.4.2. ADDREC Routine

When DMD is originally building the data base, ten percent extra storage is allocated for any additions at the end of each relation. The overflow is computed as:

$$
\mathrm{IOFL} = \mathrm{NDC} / 1 0 + 1,
$$

where

NDC = Number of tuples in the relation

IOFL = Extra storage or overflow area.

The area is initialised with zeroes for integer fields and blanks for alphanumeric fields. Whenever a tuple is to be added to the relation, the availability of the overflow area is tested; if the area is full, the error message is given; otherwise the tuple is placed at the end of the relation. If the overflow area is full, the DBA is required to regenerate the system (by using the DMD Module). Once a record is added, the RTAB must be rewritten on the system area. This is also done by subroutine CLOSE.

## 3.4.3. DELTRL Routine

This is also a privileged data manipulation subroutine for deleting an entire relation; it is allowed to DBA and users with security level less than 10. After checking authorisation for the subroutine, DNO (and other parameters of the relation to be deleted) are obtained from RTAB index entries. The entire disk space of the relation is blanked. The index is updated to include the deleted area on the AVAL list. RTAB is accordingly amended. FTAB is updated by deleting all items that are not referenced/required by any other relation in the data base. Similarly RFDIR is corrected to incorporate changes in the data base. After all the modifications are incorporated, the amended system tables must be rewritten in the system area, using CLOSE.

```csv
PROGRAM EXTRACT
C DECLARATIVE STATEMENTS AND INITIALISATION
CALL OPEN
C NO OF TARGET FIELDS - NRQ TARGET RELIDS - IRID
C TARGET FLDID - IFID QUALIFICATION RELID - IRQ
C QUALIFICATION FLDID - IFQ VALUE ARRAY - IV
C CONDITION OPERATOR - IOPR
C NUMBER OF OUTPUT TUPLES REQUIRER - ION
READ (5, 120) ION, NRQ, (IRID(I), IFID(I), I = 1, NRQ)
120 FORMAT (I5, NI2)
READ (5, 130) IRQ, IFQ, IV (1), IOPR
'30 FORMAT (3I5, A2)
WRITE (6, 230) NRQ, (IRID(I), IFID(I), I = 1, NRQ), IRQ, IFQ, IOPR, IV(1)
CALL GETQ, (IRQ, IFQ, IOPR, IV, ION, IRID, IFID)
230 FORMAT ('GET ALL RELID', I5, 2X, 'FLDID' I5/20X, 'RELID', I5,
2X, 'FLDID', I5/20X, 'RELID' I5, 2X, 'FLDID', I5/,
'GIVEN VALUE OF RELID', I5, 2X, 'FLDID', I5, 2X, A2, 2X, I5)
WRITE (6, 100) ((IUSR(I, J), I = 1, ION), J = 1, 30)
100 FORMAT (NI5, NA2)
STOP
END
OUTPUT EXTRACT
GET ALL RELID- 1 FLDID 6
RELID- 2 FLDID 5
RELID- 2 FLDID 7
GIVEN VALUE OF RELID- 3 FLDID- 10 GT 500
RD-P1-67/RRL-24 RRL HYDERABAD PROJECT COMPLETED REPORT AWAITED
SA-P2-73/RRL-87 PRL AHMEDABAD PROJECT IN PROGRES PDC DEC 79
RD-PX-76/DSL-93 DSL BANGALORE PROJECT HELP UP FOR FUNDS
```  
Fig. 5. Extract of Program and Output to get values from different relations given parameters of Qualification field using GETQ Routine.

## 3.4.4. MDYREC Routine

This subroutine can modify any tuple or field in the data base. If the record is to be deleted, it is replaced by zeroes and blanks in appropriate positions. The existing value is checked with the new value, and if both are identical, no further action is taken. The occurrence to be modified is brought into the buffer and modified, as desired, by the user. It is then rewritten by using IOPT. In all data manipulation routines, subroutine GETO with a non-rewind option is used to reach the desired occurrence for modification. Once the action is complete, the appropriate DNO is rewound. As an example Fig. 3 shows how to modify the name of the laboratory for a specific project. It uses GETF for testing whether the field is correctly modified.

## 3.5. UTILITY ROUTING

There are 6 utility routines to provide housekeeping and control of the Data Base. IOPT and ICON have already been described; the remaining four are now discussed.

## 3.5.1. OPEN Routine

This routine must be called before working with the data base. Its main functions are to:

1. Bring all the system tables from the system area to the main memory; this works independently of the DMD Analyser.

2. Ask the user for access code and security level.

3. Check level and flags when the user may only read the data.

4. Prepare the common field relation matrix (MCFR). Other search and utility routines need to find at least one common field between any two relations. If there is no common field, the particular relation cannot be used in combined queries involving two or more relations. To avoid time wastage in other routines, the MCFR is prepared after checking common items in all the relations requested by the user.

5. Store the system table and MCFR on disk for subsequent use.

Finally the user is given various RELID's and an access level and asked to continue usage of the system.

## 3.5.2. CLOSE Routine

This routine must be called on completion of data base usage. All temporary locations and the users work area are initialised, the necessary updates are made, and thus the system is ready for the next user.

## 3.5.3. BSEARCH Routine

This is a general purpose binary search routine used for matching the key values whenever there is a sorted table. The routine is based on an algorithm by Knuth [9]. The name of the table and its upper limit are specified, along with the search key value. The index value is transferred to the buffer by the routine.

## 3.5.4. DUMP Routine

To ensure data integrity, it may be necessary to take DUMPs at regular intervals, or whenever a fatal system error occurs. DUMP is a privileged subroutine. The system automatically outputs the current contents of all system tables and MCFR. By using subroutine GETR, all the relations opened by the user are given as output by DUMP. From these results, it should be possible for a system analyst/DBA to rectify any suspected error.

## 4. Results

An experimental Relational DBMS has been implemented on the TDC-316 (a 16 bit, third generation digital computer manufactured by ECIL, Hyderabad) at the Indian Institute of Technology Kanpur. The implementation consists of two independent modules; the DMD analyser and the routines for utilising the DSL (including DML and utility routines). The developed system meets most of the objectives of a DBMS. The use of Relations in 4NF helps in reducing redundancy and avoids certain insertion, deletion and update anomalies. The relational approach provides a very simple and effective view of the data base for the user. Since the system is FORTRAN based, it provides a high degree of flexibility. The system has been extensively tested for monitoring of projects with live data from a number of research laboratories in India. The results obtained have been very encouraging.

The working of the DBMS may be monitored by the DBA. In case of an error, DUMP routines may be invoked to aid in diagnosing the fault. The system provides data independence and a controlled level of redundancy. Security and privacy are ensured with the help of access codes allotted to each relation; different security levels may be assigned to various users. If any user who may not use the privileged routines of DML tries to access the data base, the DBA is informed and the user is prevented from proceeding further.

The response time is, to a large extent, dependent on the speed of the user terminal. With a slow terminal such as the ASR-33 the response time is of the order of 5 to 10 seconds.

The DMD analyser occupies only 10K words of memory, whereas all the routines of DSL and DML are accommodated in 12K words. The user has a work area of nearly 4K for other programs. The limitation on memory available can be overcome by using a machine with a larger memory.

The entire software of the DMD Analyser, DSL and DML routines were developed with an expenditure of 6 man months. The performance of the system could be further improved by making the entire system interactive and not leaving the choice of routines to user. Depending on the requirements of any terminal user, the appropriate routine can be called to meet the needs.

## References

[1] E.1. Sibley, Special Editor for Issue on Data Base Management Systems ACM Computing Surveys Vol 8 No. 1, March 1976. Available in reprint from IAG Headquarters, Amsterdam.

[2] E.F. Codd, “A relational Model of Data for large Shared Data Banks”, Communications of the ACM, Vol 13, No. 6, June 1970, pp. 377–397.

[3] Tymshare Inc. MAGNUM Reference Manual (November 1975).

[4] IBM Corporation. APL Data Language Program Description/Operations Manual. Form No. SB21-1805.

[5] C.J. Date, "An Introduction to Data Base Systems" Second Edition. Addison-Wesley Publishing Company Inc. Phillipines, 1977.

[6] Donald D. Chamberlin, 'Relational Data Base Management Systems' Computing Surveys Vol 8 No. 1, March 1976, pp. 43–66.

[7] Codd, "A Data Base Sub Language Founded on Relational Calculus", Proc. 1971 ACM-SIGFIDET Workshop on Data Description, Access and Control, Nov. 1971, ACM, New York, 1971, pp. 35–68.

[8] ECIL HYDERABAD 'TDC-316 FORTRAN', 1976. Available from Electronic Corporation of India LTD., Hyderabad, INDIA.

[9] D.E. Knuth, The Art of Computer Programming, Vol. 3 Sorting and searching, Addison-Wesley-1973, pp. 422–447.
