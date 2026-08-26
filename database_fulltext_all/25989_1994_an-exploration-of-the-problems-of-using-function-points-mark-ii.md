---
otero_id: 25989
otero_key: "3QUCZARW"
title: "An exploration of the problems of using function points mark II"
authors: "R. Hughes"
year: "1994"
journal: "Information Systems Journal"
doi: "10.1111/j.1365-2575.1994.tb00050.x"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# An exploration of the problems of using function points mark II

R. Hughes

Department of Computing, University of Brighton, Brighton, UK

Abstract. This paper examines critically the function point analysis mark II (FPA mark II) method of measuring the functionality of information systems. Although the focus of the paper is on FPA mark II as devised by Symons, both this and the Albrecht method, from which the FPA mark II was developed, are briefly discussed. The published attempts to validate FPA mark II are reviewed and then the problems encountered by the author in applying the approach are described. The final part of the paper is concerned with the fit between SSADM and FPA mark II.

Keywords: function points, software cost estimation, software productivity measurement, SSADM.

## INTRODUCTION

Interest has been growing in what might appear to be the easily comprehended and commonsense ideas of function point analysis (FPA) as a method of measuring software development productivity and sizing proposed computer-based information systems. However, one survey (Heemstra & Kusters, 1991) at least has found that the application of this technique does not guarantee accurate estimates. This paper attempts to explore some reasons for this.

A contention of this paper is that there is a conflict between the concept of function points (FPs) as an indicator of value to the user and that of FPs as an indicator of system size and hence effort. To take an analogy, say the driver of a motor car breaks down in a remote area and has to be towed to the only garage for many miles around. The car is of no use to the owner at that moment and potentially the cost of restoring the owner's mobility is that of buying another vehicle at the cost of, say, around £8000. It turns out that the repair is a very simple one for a skilled mechanic, and all in all the cost to the garage proprietor is only £10, taking into account the spare part needed and the mechanic's time. If the proprietor were to charge £1000 for the repair, the vehicle owner might feel understandably aggrieved, even though the garage has 'saved' the owner £7000 on the purchase of a new vehicle. Some idea of a fair price comes into play. The same notion can arise when measuring software functionality: there is a tendency to assign less value to that which appears to be easy to produce.

The origins of this paper lie in the need to evaluate FPA as a suitable technique to be taught on undergraduate and postgraduate information systems courses. Among the criteria to be considered were: the validity of the method and its acceptability in industry, its ease of use, the degree to which it was 'structured' (i.e. did not rely heavily on intuition) and its fit with the use of other techniques, in particular to SSADM v4, to which the University of Brighton has a strong commitment. One desirable feature of any technique in an educational environment is its applicability to the kind of tasks a student may be required to undertake (e.g. student projects).

Although both the Albrecht method and the later Symons version are briefly reviewed, the focus of the remainder of the paper is on the latter. Some of the published attempts to evaluate this method are discussed, and then some of the problems experienced by the author in applying the approach are described. The final part of the paper is concerned with the fit between SSADM and FPA mark II.

## FUNCTION POINT ANALYSIS

## Albrecht Function Points

The technique of function point analysis was originally described by Albrecht (1979) and Albrecht & Gaffney (1983), and was the result of work done at IBM with the measurement of system development productivity. It was apparent that there was a need for some measure of the actual work accomplished in a computer-based information system, but that source lines of code (SLOC) had many drawbacks, such as its susceptibility to differences in programming language and coding style and its remoteness from the users' actual needs. What was required was some way of assessing the actual functionality delivered to the user. An approach was suggested which counts the number of input transactions, enquiries, reports, master files and interfaces to other systems.

Some of these can be more complicated and do more work for the user than others and FPA takes this into account by using weights for the degree of complexity of each element. As the Albrecht method has been refined, this complexity has been defined in terms of rules relating, for example, to the number of data items used.

The weighted counts are then summed to give an overall function point (FP) count for the system under consideration. This represents the information processing size, but it is recognized that additional value can be delivered to the user through other, technical, attributes of the system, such as the use of distributed processing and sophisticated end-user interfaces. It is important to note that these relate solely to the actual system delivered to the users and not to the technical environment in which the system is developed so that, for example, the use of a 4GL is not directly relevant. The technical attributes are catered for by the 'technical complexity adjustment' (TCA), in which each of 14 factors is scored in the range 0–5.

These 14 scores are summed to create a ‘degree of influence’ (DI), which is used to modify the information processing size FP count.

As indicated earlier, the original purpose of FPA was to assist in the measurement of productivity. Behrens (1983), for example, used FPs to compare the productivity of on-line and batch program development environments. It was only a short step to use FPs as a driver in system size estimation. For example, Albrecht (1983) noted that with the systems he examined it took, on average, 100 lines of COBOL to deliver an FP.

Albrecht FPs have subsequently been incorporated into a number of cost estimation software packages, including SPQR, SIZER/FP, ASSET-R and the original version of BYL (Before you Leap) (Tate & Verner 1990). In addition, many CASE tools can produce FP counts from their meta data repositories. In the USA, a very active international function point user group (IFPUG) was formed in 1986, and detailed counting rules have been formulated (e.g. IFPUG, 1990).

## Function point analysis mark II

Symons (1988) presented a critique of Albrecht FPA. One criticism was the narrow range of weights allowed. For example, the multipliers for input transactions range between 3 and 6, which allows the most complex transaction to be only twice as difficult as the simplest.

Another criticism was the choice of values for these weights. Albrecht maintained that they reflected the relative value of the function to the user and that they had been established by debate and trial, but no details were given about how these particular numbers had been picked.

An alternative method of calculating function points was outlined by Symons, which was later fleshed out in a book (1991). Symons' original work was for the UK government, and his method, commonly referred to as FPA mark II, is now a government standard. A European function point user group has been formed which attempts to cater for users of both the Albrecht and Symons flavours of FPs, but as it has been constituted as the standards authority for FPA mark II it is inevitably focused more on the latter.

An attraction of FPA mark II is that it is based on an intuitively simple model of the transactions in an information system as comprising inputs that are received, data stores that are referenced and updated and outputs that are generated (Fig. 1).

In keeping with the user orientation of the approach, the input is always obtained from the user and the output is always that which is delivered to the user. Each transaction is individually sized, and the resulting counts are summed to obtain the overall information processing size for the whole system. This exploits the probability of there being a rough mapping between what the user perceives as a 'transaction' and what is likely to be implemented physically as a 'module'.

A potential problem with this model of a process is that of 'granularity'. Any process can be decomposed into subprocesses with inputs, outputs and stored data, which can be further broken down again and again. At what level do we consider the processes as transactions for FP counting purposes? DeMarco (1982) suggests, in a slightly different context, that decomposition should stop when the next level down does not input or output fewer data items than the current one. Symons deals with this problem by specifying that each transaction must have an input from the system user and must return data to the user. This is fine for information systems for which FPA has been designed, but leads to problems when attempts are made to extend the method to real-time environments (Rule, 1993a).

Figure 1. Elements of a transaction.  
![](/api/attachments/3QUCZARW/fulltext/images/0346c3ab6a2d47298240d3d5bd2921a5d50bb0fcd75fec1c2cb61a0a20efd6d0.jpg)

For each transaction in the system, counts are made of:

(a) the individual data item types read,

(b) the entity types that are accessed and/or updated,

(c) the individual data item types that are output.

It is the types of data and entity that are counted. Further rules have been laid down about counting and are discussed later.

Having obtained the raw counts, these are multiplied by weightings, which should reflect the amount of effort required to implement each of the three types of element. These weightings can be calculated for a specific environment, or 'industry averages', which are currently 0.58, 1.66 and 0.26, may be used. In either case the weightings used for these three elements should, by convention, be proportions of 2.5.

Symons stresses that the FP count for an individual transaction must be a very crude indicator of transaction size. Practitioners are warned not to use it as a predictor of the size of a corresponding software module that might execute that transaction, but to use the total FP count to indicate the overall system size.

The Symons method follows Albrecht in attempting to take into account technical complexity. Five new factors have been added. Many of the technical factors that presented problems in the late 1970s are now run of the mill so that the 'industry average coefficient' by which the 'degree of influence' (DI) is multiplied has been reduced from 0.01 to 0.005.

## EMPIRICAL VALIDATION OF FUNCTION POINTS MARK II

## Information processing size

Probably many organizations have carried out their own validation exercises but have not thought to publish the results. Where accounts of the experience of developers are published these very often do not contain quantitative evaluations of the techniques, e.g. Tompkins & Stanway (1991) were able to say that it was found to be a more objective approach to estimating but supplied no quantitative data.

One way of evaluating FPs as a measure of application size is to count the FPs for an existing application and then to compare this value with some other measure e.g. SLOC. A good correlation here would not necessarily mean that FPs would be a useful predictor of size. It might be, for instance, that not all the information needed to calculate FPs is present at the beginning of a project. In fact there is anecdotal evidence from user group meetings that estimations of the FPs of a system before it is built are inevitably much less accurate than retrospective analyses of existing systems because of factors such as 'scope creep', the tendency for functionality to be expanded as development progresses. Further evaluation comparing the estimates derived using FP methods and alternative approaches with the actual system size is therefore needed.

One example of mark II results that have been published comes from the Inland Revenue (Betteridge et al., 1990). Mark II FPs and source lines of code (SLOC) were collected from eight projects, of which three were new developments and five were enhancements. For the new developments they found an 89% correlation between function points and effort, which compared with a 94% correlation for SLOC and effort. This correlation is remarkably high. Kemerer (1987), for example, found a 75% correlation between Albrecht FPs and effort. For enhancement projects there was a 70% correlation between FPs and effort with the Inland Revenue projects.

Other findings at the Inland Revenue were that FPs, unlike SLOC, could be found at an early stage of the project. The Inland Revenue study also found that they could use suitably trained non-IS staff to count the FPs. This has not been confirmed by other FPA mark II practitioners with whom the author has spoken: often considerable systems analysis skills are needed to 'reverse engineer' an existing well-established system to obtain the information required by FPA mark II.

Ratcliff & Rollo (1990) attempted to analyse a Jackson system development (JSD) project at Abbey National in terms of both Albrecht and Symons FPs. There are difficulties in using the findings of this study as the main point was to attempt to map FPs onto the JSD model of systems. The effectiveness of this mapping does not appear to be tested by comparing the count derived from the JSD model and FP count of the system derived by conventional means after the system had been implemented. An estimate of COBOL SLOC and effort was derived using Albrecht & Gaffney's conversion factors of 1983, which one would assume were derived from 3GL environments, but the Abbey National environment was clearly heavily 4GL based. The COBOL code was generated automatically and turned out to be 50% of that estimated. A reason suggested for this was that the code generator produced code that was more compact than that produced by an experienced COBOL programmer, but empirical evidence for this was not given.

Tate & Verner (1990) report on a study in which FPs and SLOC were counted for one increment of an application that had already been delivered and were then used to predict the SLOC for a second increment. Mark II FPs predicted a size that was 73% of the actual, while a model tailored for the particular environment was 93% of the actual. This again was a 4GL environment, and the finding that a model tailored for a particular environment does better than a generalized model is not surprising. The approach here involved generating SLOC figures for non-procedural 4GL parameter tables. For example, a line in a table describing a screen format, if it referred to a single object on the screen, would count as one SLOC (Verner & Tate, 1988). This is clearly rather different from a SLOC as it is more commonly perceived in a 3GL environment.

It needs to be stressed that Symons as the originator of the mark II method has consistently warned against the use of FPs as a predictor of SLOC.

Thomas (1993) describes an SSADM-based project in which FPs were counted at the end of the systems requirement phase and were then used to calculate what the effort to produce the systems requirement should have been. The FP count indicated that the work hours should have been 3168 when it actually was 2520. Thomas felt that the discrepancy might be explained by the fact that some SSADM stages were omitted and thus reduced the effort expended and that a 20% risk factor for the first use of a CASE tool was too pessimistic. Overall, he found the approach promising. Information in this report about the effort needed to implement the complete project would have been even more valuable.

One study relates to the Albrecht method but still has a bearing on the mark II method. Heemstra & Kusters (1991), in a survey of Dutch users of FPs, found that overall the users of FPA tended to have larger overruns of project budgets than those who did not use FPs. This has to be put into the context that at least the FP users knew that they were over budget. The survey found that 35% of the organizations did not do any estimating, 50% recorded no data on project progress and 57% had no cost accounting mechanisms for projects. It was suggested by the writers of this report that many FP users did not implement the method with sufficient care.

## Empirical validation of technical complexity adjustment

It can be seen from the descriptions of the Albrecht and mark II methods that the mark II method essentially extends the Albrecht TCA approach to some new technological factors and reduces the overall effect of the factors. The TCA has been seen as a weak aspect of both the Albrecht and Symons flavours of FPA. Kemerer (1987) found that taking into account technical complexity could in fact make the Albrecht method a poorer predictor of system size. Heemstra & Kusters (1991) noted in their survey of Dutch Albrecht FP users that many did not use a TCA or used a factor of 1.01, which as they comment is very close to 1.00, i.e. no adjustment at all.

The modifications to the TCA calculation suggested by Symons reduce the multiplier used for each factor from 0.01 to 0.005, which would seem to imply that, with FPA mark II, the TCA for 'normal' projects would have a strong tendency to reduce the overall information processing size. Thomas (1993), for instance, reported a TCA of 0.85 being used on his project.

Betteridge (1992), on the other hand, reported that with Inland Revenue projects the mark II TCA made very little difference and did not take into account the actual abnormal costs experienced.

Symons (1988) pointed out that some of the technical complexity factors did seem to overlap: for example, the separate factors of performance requirements, heavy configuration use and a high transaction rate all relate to physical performance. Kitchenham (1992) applied principal component analysis to a set of FP data, and this confirmed that six of the factors accounted for 85.5% of the variability of the data and that none of the remaining components contributed more than 5% of the variability. This implies that the 14 original Albrecht factors can be reduced to six.

In general, these adjustments are only useful when the same developers are involved with producing systems which have radically different characteristics. As Kitchenham points out, in most development environments these characteristics are likely to remain stable from one application to another. However, not everybody lacks faith in the TCA factors. Dreger (1989) writes: ‘... it would be a serious mistake for your shop not to use them as stated and weighted.’ (p. 66).

It may be that although the present TCA approach is unhelpful, there is still a need for account to be taken of those user requirements that would not be apparent from a purely logical model of a proposed system. This would seem to be the view of Verner et al. (1989), who identified that 20% of the final system size came from such requirements. Rule (1993b) has suggested a modified method of TCA based on the identification and quantification of ‘non-functional requirements’ such as usability and adaptability.

## AN EVALUATION OF FUNCTION POINT ANALYSIS MARK II AS A TEACHABLE TECHNIQUE

## Background

A technique, to be teachable, should be as 'structured' as possible, i.e. it should not be based primarily on 'intuition'. Many of the methods described in standard texts on software engineering are heavily reliant on intuition. The Constructive Cost Model (COCOMO) formulated by Boehm (1981), for example, requires an initial estimate of SLOC which has to be estimated in this way. Betteridge et al. (1990) seemed to show that FPA mark II could be applied in a consistent and objective way.

The version of the FPA technique that was examined in some detail was the Symons mark II version because it appeared that the Central Computing and Telecommunications Agency (CCTA) as guardians of government IT standards had adopted it as the method to complement SSADM version 4. Because of this a good degree of compatibility might have been expected. (It seems that the latest guidelines on estimating and SSADM have backtracked on this.)

To obtain experience of the mark II technique, it was applied retrospectively to a number of student projects. Figures for FPs and SLOC were collected on a module-by-module basis. This goes rather further than Symons might wish as he warns against trying to correlate FPs and SLOC. Also, Symons does not recommend the use of FPs for the relatively low-level calculation of module sizes. Although quite a good correlation was found, this will not be discussed further as the applicability of data derived from the examination of student projects to 'real' application environments is problematical. Although the statistical validity of such an exercise is doubtful, the experience of trying to use the technique was illuminating. In retrospect, it seems sensible to precede empirical validation using statistical techniques by more informal, experiential, evaluations which can identify potential strengths and weaknesses in the technique. Such informal evaluations may be of more benefit to a potential user of a technique because it can be related to the user's own environment.

One area in which FPA mark II has received some criticism from the proponents of the Albrecht version has been with the application of the weightings to the input, output and processing elements of a transaction. These should correspond to the average effort required to implement an instance of each of the types of element. An attempt was made to identify those parts of the code in the projects that related to the input, output and processing elements identified by FPA mark II.

## Some difficulties encountered with counting FPs

In order to be consistent in the way that systems are evaluated, there need to be uniform rules. Where a ruling has been formulated in response to a query about the application of principles to a particular case, it may well be that the precise outcome of the ruling does not matter as long as similar cases are treated consistently. A rule, once formulated, should only be modified with great reluctance as this may invalidate data that have already been collected and classified.

This accepted, some of the rules laid down for FPA mark II seem rather arbitrary. Many problems seem to arise from the conflict between seeing FPs as a measure of user functionality and seeing FPs as a predictor of development effort.

In the examples (some trivial, some less so) discussed below the FP count for certain system features would be quite low compared with the effort needed to implement them, and this reduces the effectiveness of FPs as a predictor of effort.

## Data element counting

## Control data elements

Control data elements such as menu options are ignored as are menu screens. In the systems that we looked at these items added considerably to the processing required as they often had an impact on the overall system structure. As significant effort may be required in their design and implementation, ignoring them would appear to have a detrimental effect on the estimating of system size. Menus are not ignored in the Albrecht method (Dreger, 1989), and it is noticeable that the method developed by Verner et al. (1989) also recognizes menus.

## Trigger items

It is suggested that, even if a transaction has no input data items, a token trigger ought to be counted. The justification for this seemed weak with our sample programs as no program code was needed to deal with the trigger. Even with larger systems, the counting of triggers would make only a marginal difference and, while this might help to compensate for the fact that control items and menus are not counted, this seems to be a rather indirect way of letting some justice be done. However, the identification of triggers is still important as it establishes the process under examination as a true user-initiated transaction.

## Dates

Dates are generally to be treated as one item rather than as three separate items, e.g. day, month and year. In fact, dates were found to be generally tricky to process. They are pivotal to some processing, often triggering many actions, and treating them as three separate items is often a better reflection of the role that they actually play.

## Counting entity references

FPA mark II distinguishes between primary and non-primary entities. Each primary entity type referenced is counted once, but references to non-primary entities are lumped together as an access to a notional 'system' entity.

The main difficulty here was with the distinction between primary and non-primary entities. Primary entities are those which are subject to frequent access and update, for example an employee in a payroll system. On the other hand, non-primary entities are basically look-up tables. From a 3GL programming point of view the distinction is well defined. FPA mark II attempts to get away from such a physical basis, and when it does things become less distinct. An entity could in one transaction behave like a primary entity and in another behave more like a non-primary entity. For example, in a project control system, a transaction could look up the employee reference on an employee record simply in order to obtain a name and nothing more.

A second point is that each primary entity type referenced is counted only once regardless of the number of times it is referenced. An example of this might be where a money amount is to be transferred from one account to another. Although the two account records would have different roles, the entity type would only be counted once.

## Separating outputs

This was a major problem area. The difficulty arises when, for example, what appears to be the same on-line enquiry can be made with different types of selection criteria or the same report can be generated but sorted to different orders. Low & Ross Jeffery (1990) identified this as a major reason for differences between FP counters using the Albrecht method.

The ‘official’ guidance given is that if each of the different types of output is for different users then they can be counted once for each user group. The way to consider these problems is to attempt to see the computer transaction in the context of the wider business transaction in which it is embedded. If different forms of an enquiry are used when doing different tasks, then it would appear to be appropriate to count each type of use separately.

Another ruling which is in a similar area is that two outputs that represent the same data, one in tabular format and the other using graphics such as bar charts, should be treated as the same. The principle that the same information represented in different ways should be treated as one output seems to be rather harsh. Users must get some benefit from the graphical output, otherwise they would not require it: it might at least save them the effort of reproducing the data in the graphical format themselves.

Once again, the issue here seems to be the difference between the value to the user and the cost of development. FPs are designed to reflect both these aspects, which may in fact be very different. Any product has the cost it took to produce it, the value it might have to a consumer and a price which the producer and consumer can agree on. FPA in a sense attempts to arrive at a single figure that encompasses all three aspects, and in consequence an element of bargaining may be present.

## Identifying input, output and processing effort

As well as the counting of input and output data types and the entity types accessed, FPA mark II requires the calibration of the weightings by which the counts are to be multiplied. This requires the calculation of the proportion of effort normally expended on the development of each type of functionality and its normalization to fractions of 2.5. This has attracted the criticism that the proportions of effort are bound to be influenced by the technology involved. The use of effort as the common measure appears to be Symons' attempt to overcome the problem, identified by DeMarco (1982), of the relative scaling of different types of system component.

While much guidance is given to the counting of FPs, the advice concerning the identification of the types of processing is rather sparse. It is laid down that the effort relates to all stages of the development of a system including analysis, design, programming, testing and documentation. This assumes that the proportion of effort given to each of the three major components will be the same at each stage. The evaluation under discussion related primarily to the programming stage but illustrates some of the problems that can emerge.

Difficult cases were mainly caused by general housekeeping procedures, program control structures and hybrid input/output/processing procedures.

## General housekeeping

Symons (1991) quotes Boehm's early 1980s estimate that up to $85\%$ of program code could be accounted for in this way. A more recent and reasonable estimate in Verner et al. (1989) is of $20\%$ in an information systems development environment. In the student programs that were examined, housekeeping accounted for very little, but then students are not going to be overly concerned with such matters as audit trails, security, back-up and recovery.

## Program control

This was often as high as 40% of program code. The amount of such code appeared to be very much tied to the level of program complexity. One cause of discrepancies between FPs and final system size might be that FPA mark II does not have enough data available to it to gauge the level of complexity with which a transaction may have to cope.

## Hybrid processing

The distinction between input and output code is often not clear cut when one is dealing with a system that interacts with on-line operators. The division between input and processing can also be vague on occasion. For example, validation of data is to be counted as part of the input process. This in general would seem to be obvious, but what happens if an error message is to be produced when, for example, details of the author requested cannot be found on a bibliographic database? Is this an error in the input, or is it a legitimate answer to a query of the nature 'Are there any books by Barbara Kitchenham in the library?'. The commonsense approach would be to treat that code as 'processing', as its magnitude will be mainly governed by the nature of the database being used. The division between 'processing' and 'output' can also be problematical. All calculations should be treated as 'processing', but this does not seem right when the calculation is simply that of a total that appears on a report. Once again the guidelines could be refined: this time so that only calculations the results of which are stored on the database are included under 'processing'.

## FPA MARK II AND SSADM V4

Looking at Fig. 1, there would appear to be a good fit between the SSADM view of a function and the FPA mark II view of a transaction: after all, what is shown is an SSADM data flow diagram process box. Some caution must be shown, however, as FPA mark II recognizes as transactions only those processes which are triggered by an event in the external world.

The essential purpose of a feasibility study is to gauge and weigh the costs and benefits of implementing a proposed system. It would therefore be at this stage that one would like to be able to apply the FPA mark II estimating. In order to do this we need to identify for each transaction (or function in SSADM terms):

(a) number of data item types input,

(b) number of data item types output,

(c) number of entity types accessed.

With SSADM, at feasibility stage what would actually be produced are:

(a) a top-level data flow diagram (which may be supported by elementary process descriptions)

(b) a preliminary logical data structure (LDS),

(c) entity descriptions to support the LDS

The information as it stands would not identify all transactions, and even if it did would provide no detailed documentation of the data flows. These problems are not insurmountable. Experienced estimators are used to having to make assumptions about the future shape of a proposed system. This is acceptable as long as those who use the estimates are aware of their speculative nature, even though they are drawn up in an ‘objective’ FP form.

Symons suggests a 'guesstimate' version of FPA mark II, in which the estimator identifies the likely transactions in the proposed system and then classifies them by type (update, enquiry or delete) and complexity (simple, average, complex). A simple table is then used to derive the appropriate FP count. This really constitutes a different method of calculating FPs to that which is usually recognized as the FPA mark II method.

An examination of the SSADM products shows that enough information is provided to make preliminary FP counts at the end of investigation of current system stage for each of the business options being considered. Thomas (1993) prefers the later requirements specification stage, when more detail is available. Some FPA rules rely on the way the system is implemented physically and so further refinements of the count would be needed even later. Compare Fig. 1 with Fig. 2, which shows how the definition of functions are derived in SSADM (this is reproduced from Downs et al., 1992).

This illustrates how some components of functions are not clearly defined until late in the SSADM process. SSADM encourages a progression through its stages from the general outline of what will be required to more and more precise analyses of the details of the system. To this extent it reflects the 'spiral' model of Boehm (1988). This means that the FP counts can be improved as time goes on, but it may also mean that at the later stages there are data available which the technique does not use but which can provide a more accurate idea of information processing size, e.g. the complexity of the input and output structures as well as simply by the numbers of data items involved.

This does not mean that FPs should not still be counted at all stages of the project life cycle. At each stage of a project FPA measures not the final size of the system but the current perception of that system by the developers. FPA can thus detect changes to the scope of the envisaged system, which may mean that there is a need for renegotiation of the development contract.

![](/api/attachments/3QUCZARW/fulltext/images/871dfc78149096a62dcf616d43405ad8c70aa179b3570f8271354ebd0f25fa6d.jpg)  
Figure 2. The typical components of a function (after Downs et al. (1992). The numbers refer to the stages of SSADM, namely: 0, feasibility study; 1, investigation of the current environment; 2, business system options; 3, requirements specification; 4, technical system options; 5, logical design; 6, physical design.

There is nothing in these observations that contradicts Symons' own very forcibly expressed sentiments: 'No one method of estimating should be used. Like the advice on voting in Chicago, "do it early, and do it often"!'

## CONCLUSIONS

1 Nothing in this work detracts from the value of FPA mark II as an early predictor of effort, especially when compared with the other methods available.

2 There is an imperfect match between the data needs of FPA mark II and the products of the SSADM version 4 feasibility study module.

3 The distinction between the 'input', 'output' and 'processing' components of an information system are not clear cut and make the calculation of the corresponding weightings problematical.

4 The accuracy of FPA mark II as a predictor of final system size will be affected by the lack of information about the complexity of the input and output data structures, which may only be made known at a later stage of the project life cycle.

5 Confusion is caused by the conflict between the role of FPs as a measure of functionality and FPs as a predictor of development effort. This conflict is a critical one as the concept of 'functionality' is associated with the idea of 'value to the user'. FP counts are likely to become weapons in political battles about 'value for money' and the need or otherwise for the outsourcing of IS software development and maintenance. In these circumstances, the assumption that FPA mark II is a purely objective measure is a dangerous one.

## FURTHER RESEARCH DIRECTIONS

A call for the publication of more results of the findings of IS practitioners would seem to be appropriate at this point. Some words of caution need to be sounded, however. Empirical investigation has to have a sound intuitive foundation, so that, for instance, the assumptions upon which the investigation are based are clearly thought out and stated. A danger with methods such as SSADM, when CASE tool support is available, is that researchers may be overwhelmed by too many data: selectivity is needed, particularly if an industry-wide metrics data repository is to be contemplated.

Two specific research areas appear to be promising. The first is examining the products of methods such as SSADM to determine which ones can help predict the likely structural complexity of the final system. For example, it would appear that entity correspondence diagrams (ECDs) and enquiry access path (EAP) diagrams, which show how the accesses to the various entity types needed by a function are related, would give a good approximation of the database manipulation that needs to be carried out by the final system.

A second line of research could take into account the volume of use that transactions have: this could enhance the idea of value to the users. To take a simplistic example:

<table><tr><td>Transaction</td><td>Function points</td><td>Transactions/month</td><td>Function-use/month</td></tr><tr><td>A</td><td>30</td><td>20</td><td>600</td></tr><tr><td>B</td><td>15</td><td>200</td><td>3000</td></tr></table>

Transaction B is clearly the most used. Because it is used the most, one might expect that it would require the most maintenance effort. Adams' (1984) analysis of the operational failures showed that the probability of failure was clearly linked to the volume of use. From this has been developed the idea (Cobb & Mills, 1990) that, by creating usage profiles of systems which identify the frequency of use of each feature and by then designing tests to mirror that usage, the risk of failure can be drastically reduced.

If the volume of use could have been correctly forecast at development time then the developers might well have decided to invest more in the development of transaction B to ensure the highest standards of ease of use and maintainability.

It is possible to speculate further and suggest that volume of use may be an indicator of complexity. The larger any population is, the more diversity it may have. When there is a large number of transaction executions, even if they look superficially homogeneous, there is more possibility of exceptions. It would follow from this that 'scope creep' may well be more prevalent with high-volume transactions than low-volume ones. This is something it is clearly possible to test empirically.

## REFERENCES

Adams, E.N. (1984) Optimizing Preventive Service of Software Products. IBM Journal of Research and Development, 28, 2–13.

Albrecht, A.J. (1979) Measuring application development productivity. In: Proceedings of the joint Share/Guide/IBM Applications Development Symposium Monterey CA, October 14–17, 83–92. Reprinted in: Programming Productivity: Issues for the Eighties, Capers & Jones (eds). Computer Society Press.

Albrecht, A.J. & Gaffney, J.E. (1983) Software function, source lines of code and development effort prediction: a software science validation. IEEE Transactions in Software Engineering, 9, 639–648.

Behrens, C.A. (1983) Measuring the productivity of computer systems development activities with function points. IEEE Transactions in Software Engineering, 9, 648–652.

Betteridge, R. (1992) Uses and abuses of function point

analysis. Presented at European Function Point Users Conference, London, June 24–25.

Betteridge, R., Fisher, D. & Goodman, P. (1990) Function points v. lines of code. Systems Development, August, 4–6.

Boehm, B.A. (1981) Software Engineering Economics. Prentice Hall, New York.

Boehm, B.W. (1988) A spiral model of software development and enhancement. IEEE Computer, May, 61–72.

Cobb, R.H. & Mills, D.M. (1990) Engineering software under statistical quality control. IEEE Software. November, 44–54.

DeMarco, T. (1982) Controlling Software Projects. Yourdon Press, Englewood Cliffs, NJ.

Downs, E., Clare, P. & Coe, I. (1992) Structured Systems Analysis and Design Method: Application and Context, 2nd edn. Prentice Hall, Hemel Hempstead.

Dreger, J.B. (1989) Function Point Analysis Prentice Hall, Englewood Cliffs.

Heemstra, F.J. & Kusters, R.J. (1991) Function point analysis: evaluation of a software cost estimation model. European Journal of Information Systems, 1, 229–237.

IFPUG (1990) Function Point Counting Practices Manual. Release 3.0, Sprouls, J. (ed.). AT&T, Piscataway, NJ.

Kemerer, C.F. (1987) An empirical validation of software cost estimation models. Communications of the ACM, 30, 416–429.

Kitchenham, B.A. (1992) Empirical studies of assumptions that underlie software cost-estimation models. Information and Software Technology, 34, 211–218.

Low, G.C. & Ross Jeffery, D. (1990) Function points in the estimation and evaluation of the software process. IEEE Transactions in Software Engineering, 16, 64–71.

Ratcliff, B. & Rollo, L.R. (1990) Adapting function point analysis to Jackson systems development. Software Engineering Journal, 5, 79–84.

Rule, P.G. (1993a) Function point counting practices for highly constrained systems. Presented at European Function Point Users Conference, Bristol, 24–26 March.

Rule, P.G. (1993b) Technical complexity as a size driver. Presented at European Software Cost Modelling Meeting, Bristol, 22–24 March.

Symons, C.R. (1988) Function point analysis: difficulties and improvements. IEEE Transactions in Software Engineering, 14, 2–11.

Symons, C.R. (1991) Software Sizing and Estimating. Mk II FPA. Wiley, Chichester.

Tate, G. & Verner, J.M. (1990) Software sizing and costing

models: a survey of empirical validation and comparison studies. Journal of Information Technology, 5, 12–26.

Thomas, I. (1993) SSADM version 4 estimating: a project view. SSADM Newsletter, 17, 8–9, 14.

Tompkins, C. & Stanway, J. (1991) Function point analysis and SSADM. SSADM Newsletter, 12, 27–30.

Verner, J. & Tate, G. (1988) Estimating size and effort in fourth-generation development. IEEE Software, July, 15–22.

Verner, J.M., Tate, G., Jackson, B. & Hayward, R.G. (1989) Technology dependence in function point analysis: a case study and critical review. In: Proceedings of the 11th International Conference on Software Engineering, Pittsburgh, May, pp. 375–382.

## Biography

Bob Hughes started work as a computer programmer in 1970 after having obtained a humanities degree. He worked in the telecommunications and energy industries and in local government, progressing through the roles of programmer, senior programmer, programming team leader, systems analyst and database analyst. In 1981 he headed the information systems group at what is now the University of Middlesex, and in 1984 moved to the University of Brighton as a senior lecturer. At Brighton, he has specialized in software project management, particularly in a European context. He is currently researching into the application of software measurement to information systems analysis and design.
