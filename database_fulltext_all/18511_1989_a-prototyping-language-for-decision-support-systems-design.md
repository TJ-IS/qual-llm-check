---
otero_id: 18511
otero_key: "CXUBJZJP"
title: "A prototyping language for decision support systems design"
authors: "W.E. Cundiff"
year: "1989"
journal: "Information & Management"
doi: "10.1016/0378-7206(89)90023-2"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
# A Prototyping Language for Decision Support Systems Design

W.E. Cundiff

Division of Administration, Griffith University, Nathan, Brisbane, Queensland 4111, Australia

APL has long been associated with decision support system development, where the emphasis has been on full system implementation. However, the inherent features of APL that have made it popular with DSS designers, have been largely overlooked within the more traditional domain of information systems design. A functioning prototype DSS designed for marine park planning is presented from the perspective of user/system dialogue. The executable notation embodying the design, based on the single flow control construct of sequence, is portrayed, along with the associated system array structures.

Keywords: Decision support systems, Prototyping, Systems design, APL, Marine Park planning, Microcomputer applications, Hierarchical database management, Programmer productivity, Command language, Interactive dialogue.

![](/api/attachments/CXUBJZJP/fulltext/images/9dc9cf6d0a7eec6a0beff27e1aee0e93a042ede1242253966818e1915cf78678.jpg)

W.E. Cundiff is a lecturer in Organisational Modelling and Information Systems in the Division of Administration at Griffith University, Brisbane, Australia. He obtained his Masters degree, concentrating in systems modelling and simulation, from Toronto's York University in 1976. He has written and consulted widely on systems and computing where his work has appeared in publications such as Applied Mathematical Modelling, Simulation, and Technological Forecasting and

Social Change. He is past Technical Director of an APL software house in Sydney, Australia and prior to that, Senior Research Associate with the Institute for Research on Public Policy in Montreal. Mr Cundiff has been on the Editorial Board of Transnational Data and Communications Report since 1978.

## 1. Introduction

The linkage between APL (A Programming Language) and the origins of the DSS movement have been well documented from the mid-1970s [3]. Over the years, a great deal of debate has addressed the issue of the appropriate technological and organisational locus of DSS. While the literature includes much discussion of the integrative role of DSS within information systems, generally the outcome has been to isolate DSS, at least conceptually. The spin-offs from the advent of application generators and fourth-generation development tools has been bi-directional between primary use in highly-structured transaction-based systems and DSS applications. However, well-regarded industry observers see the main imperative for production gains to be within the production level, scheduled applications; the area forever burdened by large backlogs and high fixed costs for software development. [14]

DSS applications have often been characterised as ad hoc rather than routinely used; strategic rather than tactical or operational and, inherently more mathematical than arithmetic; i.e. not designed primarily for moving, sorting, and isolating special cases of information. The mathematical correlation has accompanied the use of APL in DSS, given the language's rather large built-in repertoire of primitive functions and special symbols. However, APL has been shown to be a high productivity development environment when the key criteria of fixed versus marginal costs, absolute machine/programmer hours, machine/programmer hourly costs, and user time/costs are evaluated, vis-a-vis a traditional system development life cycle and embodiment in an HOL such as COBOL [10]. As a development tool for realising systems, APL has been portrayed as an effective solution to many of the software related performance problems. [13]

## 2. A Prototyping Language

Many frameworks for system design have emerged over the past decade, including that of prototyping $[1,2,4,15]$ . Within the prototype paradigm, various roles and objectives have emerged to characterise the approach. A traditional systems approach views prototyping as an exercise in confirmation. It is utilised as a tool in carrying out a more effective feasibility study or alternatively in the more advanced stages of the development life cycle as a device for finalising the target design. $[16]$ It, therefore, serves to strengthen conventional analysis and design techniques rather than provide an alternative per se. Prototyping can then even hasten or strengthen the quest to freeze the specification. The overall result is that development and implementation abide separately and they do so with increased impetus.

Alternatively, the so-called subset evolution interpretation of prototyping tends toward a blurring between the roles and objectives of design and implementation. The focus is not on the provision of a test-bed for an overall design, but instead the specification in sufficient detail to construct an abbreviation of the targeted system, one that works and is robust enough to permit adaptation in the managerial decision-making setting. Extensibility is paramount, accommodating the evolving knowledge and cognitive style of the user. APL has proven to be a very effective development environment for achieving the objectives of subset evolution in prototyping system design by negotiation. [17] APL has been used widely as a shorthand for DSS design and implementation. It has a powerful primitive set, an interactive user focus, and greatly reduced dependence on serially determined control constructs (such as conditional branching, and leading/trailing test iteration). Numerous full-functionality interpreters of APL are available for mainframe, mini and microcomputer configurations, supporting advanced formatting capability, virtual memory paging and advanced array operators.

## 3. The Problem

The complexities of natural resource management are monumental from even a simple unique disciplinary perspective. The inter-connected relationships in a coral reef community, from the standpoint of an ecologist, are so complicated that "they would make the largest computer in the world blanch". [19] Introduce economic factors, such as fisheries [8] and competing interests fraught with human values, and the problem of understanding and effective management is magnified exponentially. [11] However, the need for thoughtful coordination of activities affecting the Great Barrier Reef Province is necessary for its conservation, while permitting the widest but judicious use of this vast part of mankind's heritage. The Great Barrier Reef Marine Park Authority is one such body with a mandate to formulate and administer a planned approach. The complexity and scope of the data required as input to the planning process in the management of coral reef resources has been well documented elsewhere. [7]

The vested interests can be divided, in the broadest sense, into three groups: fishing, tourism, and conservation. [12] Obviously, overlap exists across the three interests; e.g. commercial versus recreational fishing; conservation based research stations versus temporary island habitation by tourists and so on. However, the broad classification has been seen to be workable and forms the basis for the decision support framework presented here.

## 4. A Prototype DSS

It should be noted that systems thinking [18] and modern information technology from state-of-the-art computing hardware/software[20] to satellite and remote sensing [9] have been brought to bear on the problem of understanding the dynamic processes and supporting the task of planning and management of the Great Barrier Reef Province and marine park. The framework described here is founded on an hierarchical model of data. [6] The focus is on establishing a design that will incorporate properties of adaptability and functionality. The database management component should, in particular, accommodate a highly interactive user/system dialogue and permit the ready use of the stored data with application-specific models and data analysis routines. [5]

The prototype is fully operational, having been developed and run on an IBM PS/2 Model 30 with 640 K of RAM. The hardware configuration supports an 8087-2 mathematics coprocessor at 8 Mhz and a Multi-Colour Graphics Array for conversion from ASCII characters to the APL symbol set. The software is written using the APL interpreter (version 1.0) developed by the IBM Madrid Scientific Centre. The actual software (10 modules) for all data management functions shown occupies 23 lines of executable code. An additional function for displaying and printing results of queries and computations is written in 19 lines of APL. A separate user-defined routine (Capricorn1) that packages the entire dialogue for repeated command file use is written in 16 lines.

Six data structures, principally for search and indexing operations, are included (PERSPECTIVE through TIMEFRAME). Intermediate global arrays for storage and search are maintained in the library workspace (REF = numeric and LEVIL = literal). All other variables, local and global, are generated during execution. Therefore the prototype can be set up and run given these algorithms and data structures. Finally all data are stored in a single multi-dimensional numeric array of rank 6. The dimensions have a one-to-one correspondence to the row size of the global arrays containing the attributes for each of the six levels composing the numeric array (DATA). The following section portrays the step-by-step dialogue fo using the prototype. The APL functions are listed in order of presentation in Appendix 1. The associated data structures are also included. Given the brevity of the code embodying the prototype, the suitably equipped reader is encouraged to key in and experiment with the software. A utility function (BUILD) is included for constructing the associated level arrays, and another (PUTDATA) for entering data values.

## 5. The DSS Dialogue

The six levels of the hierarchy can be accessed individually or in any combination across the DATA array. It is necessary to specify the selection in a dyadic form; i.e. by supplying, as arguments, the name of the level and the specific identifier within the level. For instance if the variable of concern is labour force, the following will retrieve only that data:

## 'VARIABLE' SELECT 1

Referring to the global array VARIABLE in Appendix 1, it can be seen that it is associated with a descriptor as well as a numeric code (1) and a mnemonic (work). The literal data for search and indexing will ultimately map to the fifth dimension of the rank 6 structure DATA. Thus the six dimensions of the DATA array represent paths through the hierarchy beginning with PERSPECTIVE followed by SECTION, INTEREST, ACTIVITY, VARIABLE, and TIMEFRAME.

Having designated the data of interest, normally a particular zoning section is of importance, though aggregates can also be stored as totals. Therefore, if it is the Capricornia Section, it is designated by again using the SELECT function:

## 'SECTION' SELECT 1

These two commands have flagged the data for retrieval of labour force for the Capricornia section. It can be viewed from any or all of seven perspectives. If, ultimately, an analysis requires a comparison between the actual and forecast conditions, it is now necessary to specify the subset of data that corresponds to these two perspectives:

## 'PERSPECTIVE' SELECT 27

The operation further decomposes the hierarchy into a three-dimensional array. However, numerous variables can be stored not only by multiple perspectives but also by vested-interest; i.e. labour force data could be retained for the population making up the tourism industry as well as the fishing industry. Therefore, further specificity is necessary:

## 'INT' SELECT 4

Here, the fishing labour force data is sought. The level identifier may be abbreviated to any unique combination of leading characters.

Again totals could be sought or specified activities designated by interest. Fishing takes many forms, and here three types are targeted:

## 'ACTIVITY' SELECT 345

As the refinement proceeds, the data will now be retrieved for gill netting, beam trawling, and beach

Fig. 1

seining. However, having made all of the selections through the hierarchy, the time period of importance has not been stipulated. Therefore it is necessary to specify the timeframe. The data structure can easily accommodate any combination of periodicity and time horizons for forecasts and estimates, as well as for archiving historical time series. Here we are interested in forecasted and observed data for the three years – 1985 through 1987:

## 'T' SELECT 1 2 3

Once all data are selected, they may be ordered according to the computational or display requirements or left in the original hierarchical structure. A restructuring is needed for subsequent mathematical operations and output. The timeframe dimension is within perspective and, at the two lowest levels, can be visualised as a row and column structure. Next, perspective is within activity, introducing the third dimension and effectively designating a cube; a perspective x time x activity combination. These structures can be large, depending on the scope of the database. Further restructuring of the hierarchy is obtained by situating the three-dimensional array in the required interest level, in section and, finally, in the variable of concern:

## STRUCTURE 'V, S, I, A, P, T'

Computation or operations across the resulting hierarchy can be initiated by stating the level to be accessed:

## LEVEL 'ACTIVITY'

After this any of the built-in functions may be applied. Here a summation is carried out to consolidate the values of the three fishing activities. The user may specify the code under which the result will be stored; 999 is supplied:

## 999 INSERT SUM NO 3 4 5

Two arguments are user-supplied: a three element vector indicating the specific items within the earlier designated activity level and a scalar for the intermediate storage.

The storage location for intermediate retention of the results of the computation may also be identified:

## 999 ID 'NET/TRAWL/SEINE'

The activity level occupies the planar dimension of the restructured cube, the ID effectively supplies a description title for report generation, noting that the output will always be tabular.

Having made the summations across the activity level, the results are used to compute the difference between the two perspectives beginning by again addressing a particular level across which the subtraction will be performed.

## LEVEL 'P'

As with the summation, subtraction is invoked by the MINUS function, differing from SUM in that it is dyadic, requiring an argument to the left and right. By designating the second and seventh perspective, performing the subtraction and inserting the result into an intermediate array position, all computation and storage operations are completed:

## 99 INSERT (NO 2) MINUS NO 7

The result is identified as before for later report generation. The software will associate the result with a row or column user-supplied identifier as follows:

## 99 ID 'VARIANCE'

By this time, the original selected data are no longer needed. The only concern is with the summed data across the activity level and the difference between these six values by perspective. Again, by indicating the desired level, superfluous data may be eliminated from the workspace by each coded reference:

## 'ACT' EXCLUDE 345

Finally the desired output may be shown on the screen or printed by simply keying:

## DISPLAY RESULTS

The output is arranged automatically by descending level, identifying all levels and associated component names within levels, along with those that are user-supplied (Fig. 1).

DISCREPANCY-ACTUAL VS FORECAST DATA

<table><tr><td>VARIABLE</td><td colspan="3">LABOUR FORCE</td></tr><tr><td>SECTION</td><td colspan="3">CAPRICORNIA</td></tr><tr><td>INTEREST</td><td colspan="3">FISHING</td></tr><tr><td>ACTIVITY</td><td></td><td>NET/TRAWL/SEINE</td><td></td></tr><tr><td>TIMEFRAME</td><td>1985</td><td>1986</td><td>1987</td></tr><tr><td>*PERSPECTIVE*</td><td></td><td></td><td></td></tr><tr><td>OBSERVED PERFORMANCE</td><td>436</td><td>496</td><td>726</td></tr><tr><td>EXPLORATORY FORECAST</td><td>754</td><td>661</td><td>698</td></tr><tr><td>VARIANCE</td><td>-318</td><td>-165</td><td>28</td></tr></table>

## 6. Findings

The prototype simulation of the proposed planning system was undertaken with baseline data and associated parameters of sufficient size to make decisions regarding the feasibility of undertaking larger scale development. In particular, the primary data structure – the numeric array DATA – was expanded from an original test benchmark based on three time periods to twelve and later to thirty-six periods. The expansion of the dataset led to an exponential decrease in processing speeds of roughly one order of magnitude for each increase in the three ranges.

Simulation of the system under the various conditions of retrieval, update, and simple analysis were carried out. Those were seen to characterise the typical end use of the system given the projected expansion of the database. The goal sought was essentially twofold. Firstly, the user/system dialogue was to be assessed regarding the ease of adaptation to a command language. It was noted that a command language dialogue is typically high on the scale in terms of user/task sophistication. It requires more knowledge on the part of the user prior to being able to use the system effectively in contrast to say, a menu-driven interface.

The prototype was also instrumental in gauging underlying system performance independent of the language implementation. This second goal ties in with aim of negotiating an appropriate user/system interface but with more attention to the constraints imposed on the construction of the underlying data structures and algorithms given the realisation of the dialogue best suited to the simulated task and user. The earlier mentioned notion of subset evolution is also very much dependent on a range of tools for effecting systemic change dynamically over time as user needs and understanding grow, as well as when the problem focus itself changes.

Issues regarding compilation time, establishment and maintenance of separate data files, and the scope of editing features are all important. However, at this stage in the evaluation of the prototype, attention was centred on such factors as key selection, the higher level syntax of the dialogue and the degree to which commands could be layered into macro commands such as CAPRICORN1.

The prototype was very useful in seeking and obtaining answers to these questions which could lead to an idealised design to work with as development progressed. This iterative process of using the prototype to simulate the exploration of previously ill-defined needs and expectations on the part of the end-user proved important in determining the volumes and different kinds of planning variables. This was one determinant of complexity while the extent and types of interactions among the planning variables formed a second. Though overlapping, the two determinants would affect design decisions regarding appropriate data structures and algorithm construction respectively.

Specifically the prototype assists in confirming the relative mix of numeric versus mnemonic identifiers. This is very much a volume sensitive factor contingent on the foreseen number and types of variables. It was observed that some planning variables would expand cross-sectionally, i.e., ACTIVITY while others such as SECTION would likely require structures to accommodate only longitudinal growth.

The higher level syntax must permit a complete restructuring of the database for extraction and analysis. This is due to complexities between levels necessary for even a simple analysis and because of the requirements for data display. The tradeoff met here is between a relatively complicated syntax that could achieve such a rearrangement by a single string or by way of simple level-specific commands that can be issued successively. A standard command for selective extraction is most useful given the proposed inclusion of analytical routines for say, curve fitting or input to econometric models.

Where necessary, complex retrievals based on reordering across the entire database are formed into separate routines. Here, language considerations become inescapable and the issue of user/task sophistication becomes central in the ongoing evolution of the system. If the relative number of routines is small and static, the creation and maintenance of extensible functions could be performed by support personnel. However, the prototype has suggested a considerable number of avenues for enhancement, in particular, by way of layered commands for repetitive use. In this case the end-user must have facility with the mechanism for combining the level-specific commands.

It was in simulation of direct user involvement in operating the prototype system that the power of APL became most apparent. In particular, with the requirement that commands be successively layered and stored in user-defined routines, participants in the design process were able to package commands with minimal tutoring. A high degree of user autonomy was soon established and the very basic skills of APL in calculator mode were being developed.

## 7. Conclusion

The notation of APL provides a very powerful and concise tool for quickly designing and implementing prototype DSS. It lends itself particularly well to designing higher level user dialogues and thus embraces the prototype design philosophy of subset evolution.

The co-existence of one conceptual data type along with primitive and user-defined functions in a single workspace provides a cohesive approach to DSS design. APL is an interactive development environment that facilitates very quick testing with concise, direct error diagnostics. The interactive character of APL promotes direct user involvement in the design process, not just from the perspective of walkthroughs and demonstrations, but from the actual user/system dialogue at the keyboard. While APL supports a large-scale file handling subsystem, prototype development need not resort to separate data files given the co-existence of workspace-objects. For a significant class of DSS applications, the construction of workspace only systems is well sufficient to accommodate very large data structures. As shown, the actual algorithms are quite concise and therefore have minimal memory and storage requirements.

Of special consequence is the capacity for system specification and design based on an algorithmic treatment using sequence only; looping and branching are totally unnecessary in specifying database organisation concepts for data capture, management and analysis. The notion that prototype design and functional system implementation should be viewed in concert must ultimately result in productivity gains for both the analyst and the end-user.

## Acknowledgements

The author wishes to acknowledge the impact on this paper of seeing and using APL in practice. The experience of Christopher Sanderson of I.P. Sharp Australia, in the area of computer-assisted planning, has been especially influential in shaping the technical assumptions and content.

## Appendix

SELECT[□]

R\* W SELECT X;WW;Y;X1

[1] Y←A,LEVIL[WW\* LEVIL[;1]←W←1↑W;]

[2] X1\*(A,Y[;20+4],((1↑FY),1)F',')←X

[3] W,'←',5 O×X1

[4] REF[''WW;←P,X]\*X

STRUCTURE[□]

STRUCTURE X;ZZ

[1] X←(X←',')/X

[2] LEV\*LEVIL[ZZ\*LEVIL[;1]←X;]

[3] REF\*REF[ZZ;]

[4] DAT\*2 1 3&DATA[P;S;I;A;V;T]

LEVEL[□]

LEVEL X

DIM\*LEV[;1]←X

NO[□]

R\*NO XX

[1] PRC\*DIM-3

R\*DAT

SUM[□]

R\*SUM X

R\*+/[PRC]X

INSERT[□]

W INSERT X

[1] DAT\*DAT,[PRC]X

REF[DIM;REF[DIM;]+O]\*W

ID[□]

W ID X

(DIM≠4)/LO

TOPLINE\* ',20×X,20'
'O

LO:BOTTOMLINE\*20×X,20'
'MINUS[□]

R\*W MINUS X

R\*-/[PRC]X

HEADING[□]

HEADING X

RESULTS←',X

EXCLUDE[□]

W EXCLUDE X;L;MASK

MASK(1+PDAT)P1

MASK[REF[L\*LEV[;1]←W;]+X]←O

DAT\*MASK/[L-3]DAT

SKIP[□]

SKIP X

(X,1)P'

DISPLAY[□]

DISPLAY X;W;LEVX;REFX;LABL;Z;O

[1] SKIP 25
[2] 45 CENTRE RESULTS
[3] W\*1
[4] O\*PZ\*PDAT
[5] '
[6] LEVX\*LEV[1 2 3 4 6 5;]
[7] REFX\*REF[1 2 3 4 6 5;]
[8] LO:REFF\*(REFX[W;] $\neq$ O)/REFX[W;]
[9] \*L1\*X=W=6
[10] LABL\* ',,(★LEVX[W;])[REFF;\*12]
[11] ((2\*X=5)\* P',),LEVX[W;],LABL
[12] \*(6=W),O\*W\*W+1)/LO,LO
[13] 50\* '-
[14] ',LEVX[4;],TOPLINE
[15] \*LO\*X-5=W\*W+1
[16] L1:\*\*,LEVX[W;],'\*'
[17] LABL\*(★LEVX[W;])[-1\*REFF;\*20]
[18] LABL\*(LABL,[1]BOTTOMLINE)[;\*20]
[19] LABL,(12 O\*(-2\*Z)PDAT)[;6\*12\*X[O]]
▼ CAPRICORN1[0]▼
▼ CAPRICORN1 PERIODS
[1] 'VARIABLE' SELECT 1
[2] 'SECTION' SELECT 1
[3] 'PERSPECTIVE' SELECT 2 7
[4] 'INT' SELECT 4
[5] 'A' SELECT 3 4 5
[6] 'TIME' SELECT PERIODS
[7] STRUCTURE 'V,S,I,A,P,T'
[8] LEVEL 'A'
[9] 999 INSERT SUM NO 3 4 5
[10] 999 ID 'NET/TRAWL/SEINE'
[11] LEVEL 'P'
[12] 99 INSERT(NO 2)MINUS NO 7
[13] 99 ID 'VARIANCE'
[14] HEADING 'DISCREPANCY-ACTUAL VS FORECAST DATA'
[15] 'A' EXCLUDE 3 4 5
[16] DISPLAY RESULTS

INTEREST

<table><tr><td>LABOUR FORCE</td><td>1</td><td>WORK</td></tr><tr><td>BIOMASS</td><td>2</td><td>BIO</td></tr></table>

<table><tr><td colspan="3">SECTION</td></tr><tr><td>CAPRICORNIA</td><td>1</td><td>CAP</td></tr><tr><td>FAR NORTHERN</td><td>2</td><td>FN</td></tr><tr><td>CORMORANT PASS</td><td>3</td><td>CP</td></tr></table>

<table><tr><td>BASELINE RESEARCH</td><td>1</td><td>BASE</td></tr><tr><td colspan="2">OBSERVED PERFORMANCE2</td><td>OBS</td></tr><tr><td>DRAFT PLAN</td><td>3</td><td>DRAFT</td></tr><tr><td>ZONED PLAN</td><td>4</td><td>ZONE</td></tr><tr><td>NORMATIVE ESTIMATE</td><td>5</td><td>NORM</td></tr><tr><td>HISTORICAL RECORD</td><td>6</td><td>HIST</td></tr><tr><td colspan="2">EXPLORATORY FORECAST7</td><td>FORE</td></tr></table>

<table><tr><td>AGGREGATE</td><td>1</td><td>ALL</td></tr><tr><td>TOURISM</td><td>2</td><td>TOUR</td></tr><tr><td>CONSERVATION</td><td>3</td><td>CONS</td></tr><tr><td>FISHING</td><td>4</td><td>FISH</td></tr></table>

7 3 4 5 2 3

<table><tr><td colspan="10">REF</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>4</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>3</td><td>4</td><td>5</td><td>999</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>2</td><td>7</td><td>99</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>1</td><td>2</td><td>3</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

LEVIL
PERSPECTIVE
SECTION
INTEREST
ACTIVITY
VARIABLE
TIMEFRAME

## References

[1] M. Alavi, "An Assessment of the Prototyping Approach to Information Systems Development", Communication of the ACM, 27, No. 6 (1987), 556–563.

[2] L. Bally, J. Brittan, and K.H. Wagner, "A Prototype Approach to Information Systems Design and Development", Information and Management (1977), 21–26.

[3] R.G. Canning, "APL and Decision-Support Systems", EDP Analyzer, 14, No. 5 (1976).

[4] R.G. Canning, "Developing Systems by Prototyping", EDP Analyzer, 19, No. 10 (1981).

[5] W.F. Cundiff, “On the Specification of Diverse Models in APL”, Simulation, 45, No. 3 (1985), 138–143.

[6] C.J. Date, An Introduction to Database Systems, 2nd edition, Addison-Wesley, Reading, Mass. (1977).

[7] M. Gawel, “Involvement of the Users of Coral Reef Resources in Management Plans”, in: Kenchington, R.A. and Hudson, B.E.T., Coral Reef Management Handbook, UNESCO, Jakarta (1984), 99–109.

[8] T. Hundloe, Fisheries of the Great Barrier Reef, Great Barrier Reef Marine Park Authority, Townsville (1985).

[9] D.L. Jupp, K.A. Kuchler, D. van R. Classen and W. Bour, "Coral Reef Remote Sensing Applications", Geocarto International, 4 (1986), 3–15.

[10] P.G.W. Keen, and T.J. Gambino, “Building a Decision Support System: The Mythical Man-Month Revisited”, in: Bennet, J.L. (ed), Building Decision Support Systems, Addison-Wesley, Menlo Park (1983), 133–172.

[11] G. Kelleher, and R.A. Kenchington, “Australia’s Great Barrier Reef Marine Park: Making Development Compatible with Conservation”, Ambio, 11, No. 5 (1982), 262–267.

[12] R.A. Kenchington, "The Concept of Marine Parks and Its Implementation", Proceedings of the Symposium of the Capricornia Section of the Great Barrier Reef, Royal Society of Queensland (March 1984), 153–158.

[13] J. Martin, Application Development Without Programmers, Prentice-Hall, Englewood Cliffs (1982).

[14] J. Martin, An Information Systems Manifesto, Prentice-Hall, Englewood Cliffs (1984).

[15] R.E.A. Mason, and T.T. Cary, "Prototyping Interactive Information Systems", Communications of the ACM, 26, No. 5 (1983), 347-354.

[16] J.H. Moore, and M.G. Chang, "Meta-design Considerations in Building DSS", Proceedings of the 13th Hawaii International Conference on Systems' Sciences, Western Periodicals, North Hollywood (1980).

[17] A. Smith, APL: A Design Handbook for Commercial Systems, John Wiley and Sons, Chichester (1982).

[18] K.P. Stark, and A.B. Pomeroy, "A Systems Approach to the Management of a Reef Ecosystem", Proceedings of the Workshop on the Northern Sector of the Great Barrier Reef, GBRMPA, Townsville (1978), 403–421.

[19] F.H. Talbot, Director of the Australian Museum quoted in: McGregor, C., The Great Barrier Reef, Time-Life International (Nederland) B.V., Amsterdam (1974), 26.

[20] W. Wallace, "Data-modelling the Great Barrier Reef", Working Paper, GBRMPA (1982).
