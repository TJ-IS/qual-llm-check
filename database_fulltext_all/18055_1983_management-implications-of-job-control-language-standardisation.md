---
otero_id: 18055
otero_key: "DCAYN3GX"
title: "Management implications of job control language standardisation"
authors: "K. Hopper; P.R. Newsted"
year: "1983"
journal: "Information & Management"
doi: "10.1016/0378-7206(83)90031-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Management Implications of Job Control Language Standardisation

K. Hopper

Department of Computer Science, University of Waikato, Hamilton, New Zealand

and

P.R. Newsted

Faculty of Management, University of Calgary, Calgary, Alberta
T2N 1N4, Canada

The brief history of command language standardisation efforts is reviewed: time and cost savings are detailed as reasons for requiring a standard operating system command and response language (OSCRL). A model of an abstract computing machine environment is introduced as a desirable kind of environment and as a way for management to understand the standardisation process. Management involvement is seen as all important, not only to support standardisation but to guide the increased flexibility which standardisation brings. Finally, it is stressed that technical experts must get involved to ensure a competent and comprehensive result – even though an actual standard may be five or more years distant.

Keywords: Job control languages, command languages, response languages, standardisation, standards management, user interfaces, user environments, abstract machines.

![](/api/attachments/DCAYN3GX/fulltext/images/0891a524813ca416b38cba3cbd8e08c3f0a472a6413bc814bdcac828a6b8f992.jpg)

After graduating with First Class honours in electronic engineering from Cambridge University, Mr. Hopper spent 16 years as an engineering officer in the Royal Air Force where his involvement with computers ranged from hardware design and maintenance to information system architectures. Since leaving the RAF he has held university appointments in England and New Zealand where his research interests have centred on operating system interfaces – both to the user and to the underlying hardware. He is a member of IFIP WG2.7.

## 1. Introduction

"A user's access to a computer system and its various facilities is, in almost all cases, via a system command language. Probably no other feature is more important in determining an individual's effectiveness in using a computer than this aspect. The user is often placed in the position of an absolute master over an awesomely powerful slave, who speaks a strange and painfully awkward tongue, whose obedience is immediate and complete but woefully thoughtless, without regard to the potential destruction of its master's things, rigid to the point of being psychotic, lacking sense, memory, compassion and - worst of all - obvious consistency".

[1. p. 512]

## 1.1. Management Requirements

A common command and response language system is now a necessity. Even if some users can be ‘masters’ over their ‘slaves’ there is growing support for a standard or universal command language. A brief survey [2] that was recently presented at an American National Standards Institute meeting illustrates this. The purpose of this

![](/api/attachments/DCAYN3GX/fulltext/images/d179c6eab4154ffaf3909508bd872f74b45f14923972b8b01451308b46eea3a8.jpg)

Trained as a psychologist at Carnegie-Mellon University, Peter Newsted has concentrated his problem solving interests in business data processing. His recent work has investigated the characteristics of computer programs which make them easier to design and understand – thus leading to greater productivity in application programming. The logical extension of this work to command languages has resulted in his present interest in levels of abstraction as a way to meet user needs.

survey was to determine potential support for a universal timesharing command language. The survey questionnaire was returned by 21% of the 542 people solicited on the mailing list of MIS Interrupt (a quarterly newsletter sent to academics and practitioners in management information systems). Two-thirds of those responding felt that such a language should be developed as soon as possible. As these respondents were businessmen and management professors rather than merely computer experts, it is clear that this is not just a computer scientist's dream.

The survey, which also suggested potential command names for respondent comment, further discovered that people are as adamant about their own command names as they are about a standard. Though they may want to do similar things, they are quick to suggest alternate names for these functions. Fortunately, those functions which were required were not as numerous as names. The total number of functions considered in the questionnaire was 19. Only five functionally different ones were added to the list by two or more respondents.

Only 15% of the respondents expressed some allegiance to existing systems. This low percentage, more than anything, seems to suggest that users are not happy with existing systems. Clearly 85% do not feel strongly enough about their current systems to express any loyalty to them!

The responses made to the survey questions were also tempered with a healthy scepticism as to whether a single language is possible at all. Can all vendors provide the same system? Can all users be satisfied with this system? As will be suggested, the answers to these questions are in the affirmative, but with the major qualification that what must be developed and standardised is not a particular language, but a portable method based on a single language system which can provide as many different environments as users want.

## Costs of Delay

It appears, therefore, that the present status of command languages is something which should be the concern of every manager whose organisation makes use of a computer. The costs of training and retraining are only the immediately obvious expenses which could be reduced if a suitable standard command language were available. Even a seven year old analysis [10] of the changeover costs and benefits of a standard OSCRL estimates the savings (in equivalent 1970 U.S. dollars) to be \$67 million annually – \$62 million due to re-education alone. Hidden costs are probably several orders of magnitude higher. Among these would be:

a. Reprocessing costs due to errors made because of inadvertent unfamiliarity.

b. Indirect costs of processing delays.

c. Costs of changing machine operating systems.

d. The almost incalculable costs of staff frustration, low staff morale, etc.

These costs are recurrent and a forceful reason to embark upon a standardisation programme, but no savings can be made unless users are in a position to insist that equipment and software which they buy conform to a standard.

## 1.3. Standardisation as the Answer

The recognition of the unsatisfactory state of command languages by computing authorities has been sporadic throughout the world over the last decade. The earliest organised attempt was the Working Conference on Command Languages called by the International Federation of Information Processing Technical Committee 2 (IFIP TC 2) in Lund, Sweden in 1974 [3]. A more limited seminar was sponsored in the same year by the United Kingdom's National Computing Centre [4]. As an immediate result of these two meetings, IFIP set up a working group (WG 2.7) with the subject area of Operating System Interfaces and the British Computer Society formed a Command Language Working Party with the specific aim of investigating and proposing a command language standard.

Since 1974 subcommittees of other national standards and computing organisations have initiated attempts to develop a command language standard. In the United States, these include the National Bureau of Standards, the American national Standards Institute (Committee ANSI/X3H1), and the Committee on Data System Languages (CODASYL). CODASYL's Journal of Development [5] which has been written by its Common Operating Systems Command Language Committee (COSCL) has been published by the Canadian Government. The Deutsche Institut für Normalisierung (DIN) in Germany and Association Francaise de Normalisation (AFNOR) in France are fully involved, as well as preliminary meetings in Poland, Bulgaria and Ireland. Much of this work is summarised by papers in the Proceedings of the Second IFIP TC Command Language Conference in Berchtesgaden, West Germany in September, 1979 [6].

The International Standards Organisation (ISO) has also recently instigated a work item to develop a command and response language standard within its Technical Committee 97. This group has the potential to coordinate all national standardisation efforts and produce a world-wide standard.

The incentive for all this global effort is not only dissatisfaction with the technical performance of existing OSCRL's and their diversity, but also a very positive reaction to the very high annual costs of retraining when staff move or when an organisation buys a new machine. Extrapolating the earlier \$62 million re-education estimate to 1983 (assuming worldwide inflation of 10% per year) would indicate annual savings of \$214 million. In addition, the increasing use of computers in networks has now made the failure to standardise even more costly.

## 1.4. Developing a Standard

At present, efforts aimed at obtaining consensus on a standard by different groups are individual approaches to the problem. While it is essential that specific technical orientations be considered, it is even more important that end users become involved. In this respect a command and response language system is quite different from a programming language system; the skills and needs of actual users vary over a much wider range. Any standard which is to gain acceptance must be seen to meet the needs of everyone from a ticket clerk to a system programmer.

The start of work in this field by ISO is a major opportunity for users and managers to become involved, not just in reading proposals in an interested way, but in actually contributing to national working papers all over the world.

## 2. A Command System Model

## 2.1. The UNCLE System

Before discussing the management implications of using an implementation of a command language standard, it is relevant to consider the sort of model which could provide desirable command and response facilities for all users. The model considered here was developed as part of the KIWINET/NICOLA project. The complete system, known as UNCLE (Users' Nice Command Language Environment) [7-9] developed from two originally independent projects: KIWINET started in 1976 at Massey University, New Zealand, and NICOLA (NIce standard COntrl LLanguage) started in Spring, 1977, at Dortmund University in Germany. This system is characterised by high security object storage, concurrent processing, and network usage included within a comprehensive command and response language mechanism.

## 2.2. Abstract Machines

In the ideal world envisaged by UNCLE, users would be able to use job-specific constructs in making commands and receive responses similarly couched. They should only need to understand the abstract machine these commands imply.

Although the idea of providing a machine for each user is offered by the virtual machine facility of a number of modern operating systems (e.g. IBM's VM/370), the associated concept of providing an abstraction of the tailored machine is new. The abstraction process which provides this conceptual machine has three stages:

a. Using the NICOLA language, a given kind of abstract machine (AM) is defined. This specifies and names the types of objects and operations with which the user may react. It also specifies those elements of command language which may be used in manipulating objects, together with the semantically related responses.

b. A particular user who is to be given an AM is provided with an environment: a set of useful objects such as files, packages, and programs to be used in starting work. These might include an editor, a compiler and a debugging package for a student, while a financial analyst would get various accounting and forecasting tools.

c. Once defined the machine and environment would be associated with each other and 'declared' to the computer system. In many conventional systems this is called creating a new user; but a conventional user has not been relieved of the task of puzzling out the mysteries of setting up a friendly environment - UNCLE would provide this.

## 2.3. The Basic Abstract Machine

In order to form the basis of a possible standard, it is essential that the abstraction is made from a fundamental definition of all the object types and operations which any possible operating system could provide. In UNCLE terminology this definition is from an underlying facility known as the Basic Abstract Machine (BAM). Portability of the whole system at this low level requires little reliance on the underlying operating system. This relieves the user of the traditional problem of switching languages when hardware is changed. The problem is now one of BAM implementers ensuring transparency. The logical primitives of the BAM are in an intermediate 'code' which is machine independent. The BAM takes no account on the physical details of the machine. The abstraction process for user machines builds conceptual layers upon this intermediate code (which itself is ultimately mapped at the machine-dependent level).

## 2.4. The Spherical Model

Fig. 1 illustrates a model of all potential users' 'machines' using the UNCLE concept. At the centre of this abstraction sphere lies the BAM 'containing' the real operating system and hardware. No user can directly access the inside of this sphere except in ways which are controlled by the BAM. From the BAM surface outwards, various kinds of abstract machines of decreasing complexity may exist. There may be a large number of these. At any given radius in the sphere, a surface of many identical abstract machines may exist. The “latitude” and “longitude” of this surface can be considered to represent different ranges of activity and functions at the particular level of complexity. Figure 1 lists some representative possibilities.

To the extent it is possible to fully implement the BAM using existing OS (operating system) features, the OS/hardware sphere would be fully contained within the BAM sphere. If not it would 'bulge out', and it would be a management decision whether to change the OS, discard the OS, or write part of the BAM primitives in machines language.

## 2.5. Ramifications of Many Kinds of Abstract Machines

The flexibility afforded by abstraction of this kind may appear to lead to a Tower of Babel - even though there may be a large number of individually satisfied users. But this is not inevitable if management (using the spherical model) is successful in introducing an appropriate number of two-dimensional surfaces (of activity and function) at a limited number of 'distances' or complexity levels. Clearly the development of a very large number of these is undesirable. A very small number (fewer than ten) is probably too restrictive. Seven or eight might be adequate at a single commercial site, or 20–30 at an academic research site; but different sites will want different kinds of machines even for similar users.

Over time, fewer kinds would exist as more people learned and became aware of the common ones which had similar complexity and were involved in serving similar functions. For example, why have two kinds of machines for two companies which each have programmer trainees writing basic accounts receivable software in COBOL? There will probably be fewer simple kinds of AM's than complex ones. The simpler kinds will have many more users, however.

Though users would normally expand their knowledge of these various machines in training sessions over their careers, management itself would decide when a new kin' of AM was called for. It would be either more comprehensive or more limited depending on changing usage. It is of major importance that management accept the burden of controlling and administering special environments which can be derived from a standard OSCRL or else AM kinds will proliferate in the same way as programming languages. UNCLE illustrates some kinds of machines which would likely be needed initially [9, pp. 7–120].

![](/api/attachments/DCAYN3GX/fulltext/images/9f6e9f2431e4f29d850fa38f8cf367048d2043d922491006bd5fc7fae695022c.jpg)  
Fig. 1. The UNCLE Sphere.

## 3. Introducing Abstract Machines

It might seem that making existing OS's into levels of AM's would be the best way to implement an UNCLE concept; at best this is a political ploy. What is really needed is a single basic command and response mechanism from which other languages and dialects can be logically derived. The main advantage of the BAM concept over existing command language facilities or any of the proposed standards (e.g. COSCL) is the ability to give particular users particular 'machines' and still maintain portability.

Hence the best approach would be to implement the BAM on each OS command language (and directly on the hardware underneath as the need for an OS faded). This way any abstract machine could be run on any hardware. Obviously there would be resource limitations on small mainframes and microcomputers as well as with simulations on machines with 'barely acceptable' OS's. Only so much can be simulated without the simulation overhead degrading performance.

Where BAM primitives are not codable from existing OS commands, either machine code or modification of the OS would be needed. This potential portability does not imply that all physical computers would run all the same kinds of machines. This limitation is not dictated by the BAM concept but by the kinds of things in which different kinds of mainframes excel (e.g. payroll vs. weather forecasting).

Researchers would probably be motivated to implement the BAM on most OS's. ISO acceptance of the UNCLE type of model for standardisation purposes would be an essential prerequisite; few vendors would implement a new environment which had the support of only a handful of researchers. The final disappearance of underlying OS command languages would be completely transparent to a user and would only impact those users still making direct use of an old command language. But even these users' needs could be met

if management wished -- by making the OS an AM kind.

The general approach of using UNCLE concepts in a popular environment is another method which could be tried. For example, the environment required for ADA [11] is a ready-made place for such an experiment. If the UNCLE model were accepted as the support environment for this language, it would become as much a default standard as Ada is likely to become. Certainly practical approaches such as this are as essential as formal standards from ISO.

## 4. The Spherical Model in an Organisation

As shown in Fig. 2, a 'cone' of AM kinds (extracted from the BAM sphere of Fig. 1) can represent an organisation's range of computing operations. A spherical rectangle (within this cone) at some distance between the centre (outside the BAM sphere) and the surface represents one kind of abstract machine. Within this rectangle there may be many users of this kind of machine, though each user would have his own instance of this particular AM.

Without standardisation, users of a non-UN-CLE computing system would not be grouped at all; they would be free to change and build their own environments. Though environments could be just as nice as a particular AM, they would be at the mercy of the underlying OS (without a portable BAM and an AM kind to support them).

Using the spherical model, therefore, standardisation is essentially a matter of controlling the proliferation of individual attempts at tailoring. Whether the proliferation is controlled along one, two, or all three dimensions of the sphere at the same time, the introduction of the AM kinds and their potential subsets is a matter of negotiation within standards authorities. For instance, it would be practical to specify standards separately for AM kinds and for the environments which are combined with them in particular machines. Thus both the operations possible with a given machine and the objects it could use (such as compilers, editors, or electronic mail) could be appropriately standardised. It would certainly behoove a firm to develop a 'good' machine with a useful environment because such a system would be a likely candidate for standardisation. Such standardisation would ensure a marketing success and a monetary return to recoup a firm's development costs.

## 4.1. Accepting an Abstraction Model

What does acceptance of an UNCLE-like model as the basis for a standard mean to a typical organisation? Organisations seldom make use of their current practical standards, and this situation is exacerbated by the rapid turnover of DP personnel. The only real reference to standards is usually in the form of an outcry when some external standard changes. The problems of COBOL 81 replacing COBOL 74 are still not solved. The same is true as the U.S. Postal service plans to switch from its five digit ZIP code to one of nine digits.

The result is that DP shops are so underfunded for standards and training activities (only 1% of their budget in a recent survey [12]) that little more than lip service is paid to these activities. This must change for command language standards. Because a standard OSCRL will lead to less change when new hardware and/or software is installed, such a system would be easy to justify on cost-benefit grounds. Less change will mean less retraining leading to higher and more consistent productivity. While management may discover that employees are made more mobile as they find themselves freed from worrying about retraining if they change jobs, higher morale in standardised environments should improve loyalty and reduce turnover.

![](/api/attachments/DCAYN3GX/fulltext/images/fb3ed34fd866c166e1c2a83c05c0f68f7bce9b3eff930078effc83154ce2eac5.jpg)  
Fig. 2. Organisational Cones of Corporate Abstract Machines.

Organisations would be motivated to improve their training programmes as an incentive to keep employees. Improving such programmes would also become easier and more worthwhile as training goals become clearer because of standardised environments and a well-defined set of abstract machines. Certainly organisations would benefit by knowing if new employees are adequately prepared. "Do you know Inventory Machine 2.2?", would be as common a question as "Do you know

COBOL?". Even if the current rate of job switching does not decline, retraining costs would still not be as high because of the standardisation of training possible with an abstract machine model.

Certification of programmers, data processors, word processors, and even order-entry clerks would also occur as it became evident that specific skills were not only required but could be easily identified (i.e. as proficiency on a given kind of AM). There could easily be levels of certification as programmers and users became proficient at using an increasing number of machines.

## 5. Control by Users and Vendors

Existing organisational groupings imply controls outside of single organisations. User groups such as SHARE (for IBM users) or DECUS (for

Digital Equipment users) would be natural forces to demand that vendors make particular abstract machines available on all their hardware models.

There could well be different kinds provided (as abstractions from the BAM) by different manufacturers. This would not be desirable from a user point of view. It would be very discouraging if different kinds of machines were copyrighted, though some form of licensing may be essential. A proprietary return for developing a new kind of AM is probably a necessary motivation.

## 5.1. Hierarchies of Machines

The most important kinds of machines to be requested would be those derived from specific applications. A common payroll machine, a common inventory machine or a common union-dues-and-benefit-reporting machine might all be created. The hierarchical nature of abstract machines and the ability of machines ‘closer’ to the BAM to assume the functions of ‘farther away’ machines easily allows the UNCLE concepts to be integrated within a modern distributed processing environment. The potential grouping of such machines is illustrated in Figure 2. Basic data would all be shared in this scheme, though users of one kind of machine might think of the data in a different way to users of another kind of machine.

The rough triangle which this hierarchical chart forms can be thought of as a cone in the UNCLE sphere with the bottom of the chart being the simpler machines which would be on the surface of the sphere while the point of the cone represents the BAM near the centre of the sphere. Companies may even have multiple cones representing their various major processing activities: one for managing and accounting functions and another for those things specifically related to their business, such as seismic data processing or computer-aided manufacturing. These cones could well intersect and overlap as the pointed ends approached the BAM. Particular kinds of AM's may thus become a very important in-house standard. Instead of saying that everything must be in ANSI COBOL 74, one would say that everything must be developed in "Commercial Machine 2" with subsets (2.1, 2.2,

2.2.1, etc.) for more restricted or specialised functions.

## 6. Designing the Right Kinds of Abstract Machines

While management is capable of realising and enforcing standardisation, the problem of ensuring that an appropriate standard is developed - be it an UNCLE-like model or not - must fall to the technical experts in command languages, networks and user interfaces. These experts would have to define the exact subset of the OSCRL available for users of various AM's.

## 6.1. Command and Response Syntax

For commands they would also have to consider if any syntax changes were to be made from a basic language such as NICOLA. Any changes of this kind should be as few as possible so that progression to other machines is not impeded by a syntax fundamentally different from the basic format. Also any fundamental changes of syntax would increase the translation overhead and should only be adopted as the result of a conscious management decision.

For responses they would have to make decisions regarding verbosity and the need for a multi-level help system. One problem to be addressed would be how to handle messages which the user might or might not be expected to understand. One possibility would be an extended help dialogue, while at the other extreme would be the 'coffee break message' where a user would be told, "Go away and we will try to fix it".

Users of a given kind of machine should be sampled to see which forms of commands and responses they prefer or which most improve their productivity. However, it must be stressed that management should ensure that short-range preferences are not mistakenly followed to the detriment of accepting the basic syntax of a standard language within a standard model.

## 6.2. Using Software Packages

A further issue which requires technical expertise is the selection of a package versus an implementation through an OSCRL. This is the choice between using a package – such as one for a reservation system – or writing such a system in an OSCRL. Initially management which had selected a standardised environment would probably wish to continue to use their existing packages. Building a new machine or even retraining to use a standard machine would probably be prohibitively expensive in time and money just after an UNCLE-type model had been implemented. Thus most 'packages' would be invoked from a general package-user AM. This would act as 'shell' for existing applications.

As time and funds permitted, this shell could be developed into specific function machines in the standard OSCRL. At this stage expert help would be required to ensure that user needs were met and that a specific machine was truly worthy of being a standard kind of AM. Certainly professional associations would have to be consulted (e.g., the International Association of Travel Agents for a reservation machine). It is also likely that the whole standardisation process itself – fortunately on a much small scale – would be reinitiated to ensure an acceptable product.

## 7. Conclusion

If management is to reap the full benefits of a standard command and response language, it must embrace the concept of abstraction and follow through with its support of this concept in standardisation activities and organisations. It must also provide support to technical experts to ensure that the right kinds of sub-environments are created to truly satisfy all users in its corporate domain.

## References

[1] J.A. Miller and J.C. Thomas, Jr., Behavioral issues in the use of interactive systems, International Journal of Man-Machine Studies 9 (1977) 509–536.

[2] P.R. Newsted, A survey of potential time sharing commands, Invited Report, American National Standards Institute's Technical Committee (X3H1) Meeting, Berkeley, California (Jan., 1979).

[3] C. Unger, ed., Proceedings of the IFIP Working Conference on Command Language, Lund, Sweden, 1974 (North-Holland Publ. Comp., Amsterdam, 1975).

[4] D. Simpson, ed., Job Control Languages Past, Present and Future (NCC Publications, London, 1974).

[5] CODASYL Common Operating Systems Command Language Committee, COSCL Journal of Development, Version 1.6 (Canadian Department of Supply and Services, Ottawa, 1980).

[6] D. Beech, ed., Command Language Directions, Proceedings of the IFIP TC 2.7 Working Conference on Command Languages, Berchtesgaden, West Germany, September, 1979 (North-Holland Publ. Comp., Amsterdam, 1980).

[7] H.J. Kugler, ed., N. Lehmann, P. Putfarken and C. Unger. The construction of user interfaces: a guide for defining abstract machines (Universität Dortmund November, 1980).

[8] H.J. Kugler, N. Lehmann, P. Putfarken and C. Unger. The basic abstract machine: Language reference manual (Universitat Dortmund, October, 1980).

[9] K. Hopper, H.J. Kugler, and C. Unger, Users' Nice Control Language Environment: Specimen user manual (University of Leeds, Department of Computer Studies, Report No. 150, May, 1981).

[10] E.H. Sibley, Economic justification of an OSCL/OSRL, Operating System Review (October, 1976) 7–15.

[11] DOD, Requirements for an ADA programming support environment (U.S. Department of Defense, November, 1980).

[12] W. Schatz, The feds discover IRM, Datamation 27, No. 6 (1981) 75–77.
