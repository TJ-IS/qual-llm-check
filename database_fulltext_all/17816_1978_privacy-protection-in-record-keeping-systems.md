---
otero_id: 17816
otero_key: "C9GDKV58"
title: "Privacy protection in record-keeping systems"
authors: "Rein Turn"
year: "1978"
journal: "Information & Management"
doi: "10.1016/0378-7206(78)90025-3"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Privacy Protection in Record-Keeping Systems

Rein Turn

California State University at Northridge, Northridge, California, U.S.A.

Laws now in effect in several countries grant individualities certain privacy rights visissiv record-keeping organizations in government an in the private sector that maintain personal data records about them. These laws require record-keeping organizations to implement procedures and technical measures that allow individuals to exercise their privacy rights and assure that data quality, confidentiality, and security are maintained. This paper presents an overview of the basic issues in privacy protection, discusses the implementation of privacy protection requirements, and examines certain special problems that arise in extending privacy protection to international data processing systems.

Keywords Privacy, security, data protection, record keeping, personal data, data quality, transnational data flow.

![](/api/attachments/C9GDKV58/fulltext/images/8a4611224a328a3a36f3e8021948ccf5fb932110869bdbc3ec97c50725179784.jpg)

Rein Turn is Professor of Computer Science in the Computer Science Department of the California State University, Northridge, California, and a consultant with the TRW Defense and Space Systems Group in Redondo Beach, California. He received the N.H.D. in Engineering from the University of California, Los Angeles, in 1963. Previously he was an Information Scientist with The Rand Corporation, Santa

Monica, California. He has been concerned with the privacy protection and data security areas over ten years and has published numerous papers on these topics. He is also the author of a book. Computers in the 1980s, and is concerned over societal implications as of advances in computer technology. He served as a technology consultant to the U.S. Privacy Protection Study Commission. At present he is Chairman of the AIIPS Panel on Transborder Data Flow, and Vice-Chairman of the Technical Committee on Privacy and Security of the IEEE Computer Society.

## 1. Introduction

Protection of individual privacy concerns managers of information systems and the information processing field in general mainly because of the increasingly widespread use of automated record-keeping systems for maintaining personal data about individuals. In this context, "privacy" is a term that refers to certain rights of individuals vis-à-vis the collection, processing, storage, dissemination, and use in decision making of personal data about them. A synonymous term frequently used in Europe is "data protection". Protection is achieved when adequate rights are granted, effective requirements are placed on record-keeping organizations, and compliance is achieved.

Emphasis in providing privacy protection is on automated record-keeping systems because they permit record-keeping, establishing linkages between record-keeping systems, and correlating records from disparate sources at a larger scale, faster, and with more flexibility and economy than possible in manual systems. Thus, any threats to individual rights, or unfairness in decision making that may occur accidentally or deliberately in manual record-keeping systems are amplified in automated systems.

In recent years the privacy issue in automated record-keeping systems has changed from a topic of concern, study, and debate to an item for legislative action. To date, national privacy protection laws have been enacted in Sweden, United States. Federal Republic of Germany, Canada, and Norway [1–9]. Similar legislation is pending in nearly a dozen countries. The forms of regulatory mechanisms established by these laws vary from country to country, but the privacy rights granted to individuals tend to be remarkably similar. However, the details of their operational implementation can vary widely, especially as they relate to the differences in privacy protection requirements placed on the public and the private sectors, procedures to be implemented by record-keeping organization, enforcement of compliance, and the associated costs.

Privacy protection issues become international in scope when transnational flows of personal data are taken into account. Such data flows are on the increase due to rapid growth of international computer-communication networks and services they provide. Several international bodies have expressed their concerns with the privacy protection problem and are exploring ways to assure that the privacy rights of individuals available in their home countries can be extended to other countries where personal data about them may be maintained. The Council of Europe has adopted two formal resolutions on privacy protection [10,11] and is now developing an international Convention [12]. Studies have been sponsored by the United Nations [13], and the Organization of Economic Cooperation and Development (OECD) has sponsored symposia on the topic [14]. OECD is now developing guidelines for privacy protection in transnational data flow situations.

The process of providing privacy protection in automated record-keeping systems is only in its initial stages. Many new privacy protection laws will be proposed, studied, and debated from many points of view. The purpose of this paper is to examine the policy, procedural, and technical questions in implementing privacy protection requirements in a manner which, hopefully, will provide guidance to managers of information systems who will have to implement privacy protection requirements in their organizations. Emphasis will be or operational experience in countries that have already enacted privacy legislation.

## 2. Privacy protection requirements

In daily interactions with public and private organizations, individuals provide personal data to obtain services, benefits, or privileges, or as requested by law. Some organizations also collect, store, and use personal data on their own initiative. There is a general expectation by individuals concerned that the personal data they must provide or are collected about them are relevant for stated purposes, will not be used or disseminated for other purposes, and will be maintained accurate and up to date. However, as documented in the literature [15-18] and in the course of studies in several countries [19-22], these expectations are not likely to be met without granting them a set of legally enforceable privacy rights vis-a-vis the record-keeping organizations.

## 2.1. Principles of fair information practices

The individual privacy rights specified in enacted or pending legislation have evolved concurrently in several countries. Collectively they form a Code of Fair Information Practices first conceived by a governmental study commission in the United States [23] and subsequently expanded in the report of the U.S. Privacy Protection Study Commission [24]. The code rests on the following eight basic principles which are equally applicable to record-keeping systems in the public and private sectors:

1. Openness - there must be no personal data record-keeping systems whose very existence is secret, and there must be a policy of openness about any organization's record-keeping policies, practices, and systems.

2. Individual access - there must be a way for individuals to find out what personal data about them is on record and how they are used, and to see and copy those data.

A. individual participation -- there must be a way for individuals to correct or amend records of personal data above themselves.

4. Collection limitation - there must be limits on the types of personal data an organization may collect about individuals, and restrictions on the manner in which it collects these data.

5. Use limitation – there must be way for individuals to prevent personal data about themselves collected for one purpose from being used for other purposes without their knowledge or consent.

6. Disclosure limitation – there must be limits on external disclosures of information about an individual a record-keeping organization may make, and there must be legally enforceable confidentiality obligations of record-keeping organizations with respect to the use and disclosure of personal data.

7. Information management - any record-keeping organization creating, maintaining, using or disseminating records of identifiable personal data shall be responsible to implement data management policies and practices which assure that the collection, maintenance, use, and dissemination of data about individuals is necessary and lawful, that the data themselves are current and accurate, and that precautions are taken to prevent their misuse.

8. Accountability - a record-keeping organization shall be held accountable for its personal data record-keeping policies, practices, and systems.

An important principle that must be added in the still evolving Code is stated in the recently enacted Data Processing and Freedom Act in France [4]: "No judicial, governmental or private decision involving a finding or judgement on human conduct may be based solely on automatic processing of data which give a description of the individual's profile or personality." This principle makes explicit the main concern in privacy protection; it is not the collection and storage of personal data in automated record-keeping systems that has the greatest potential for unfairness to individuals, but their use in decision making is.

## 2.2. Privacy rights of individuals

Based on the Code of Fair Information Practices, the Council of Europe's resolutions [10,11], and the rational studies [19-22], the basic privacy rights can be defined, and requirements, procedures, and mechanisms proposed for their implementation and enforcement. The French privacy protection act [4] eloquently summarizes these rights as follows: "Information processing is to be in the service of every citizen. It is to develop in a framework of international cooperation. It is to infringe neither human identity, nor human rights, nor privacy, nor individual or public freedoms...Everyone is entitled to know and challenge the data and logic used in automatic processing, the results of which are against him."

More specifically, the following rights of individuals are specific in most of the enacted or pending privacy protection laws:

1. The right to know of the existence and purpose of any automated record-keeping system, the types of personal data maintained, uses made of those data, and the legal basis for requiring that personal data be provided to such a system.

2. The right to know about the existence of personal data about themselves in any such system.

3. The right to access and inspect personal data about themselves, and to challenge their quality (e.g., relevance, accuracy, completeness and currency).

4. The right to request correction, erasure, addition of supplemental data or, if this is denied, submit rebuttals to be included in disputed records.

5. The right to control, or at least to contest, dissemination or use of personal data beyond purposes that were stated when the data were collected.

6. The right for further remedies under the law, and to restitution for harms suffered as a consequence of a violation of privacy rights.

To assure that individuals can exercise these or similar rights, privacy protection laws specify certain criteria and requirements that record-keeping organizations must satisfy, administrative procedures that they must follow, regulatory mechanisms to enforce compliance, and penalties for violations. Important considerations are the scope of a privacy protection law - which types of organizations are covered by the law, and how is enforcement achieved.

In all but one enacted laws, privacy protection is provided to individuals - physical persons. However, in the Norwegian privacy protection law "personal information" is defined as data traceable to individuals, associations, and foundations. Extending privacy protection to data on legal persons is a new consideration with a potential for significant new requirements on record-keeping organizations. From the point of view of organizations covered under privacy protection laws, there are three general approaches:

1. Omnibus privacy protection legislation which applies (usually with some exceptions) to all public and private record-keeping organizations, such as provided in the Swedish, German, French and Norwegian laws.

2. Area-by-area legislations where separate laws are enacted to provide privacy protection in specific parts of public or private sectors. Examples are the Privacy Act of 1974 in the United States, and the Canadian privacy protection law, that apply to the federal governments only, regional privacy protection laws in several countries, the consumer credit reporting laws in the United States, Canada and Great Britain, and the criminal justice area.

3. International conventions that serve as binding guidelines for harmonization of privacy protection laws within communities of nations such as the Council of Europe or the CECD.

Each approach has merits and drawbacks. Omnibus legislation establishes uniform requirements for all record-keeping organizations, but cannot easily handle problems that are unique to various specific segments of the public or private sectors covered by the law. Area-by-area legislation is easier to enact and permits flexibility in handling exceptions without unduly burdening other segments, but it is likely to result in scattering of privacy protection requirements throughout the legal code of the country. Nevertheless, this approach was recommended by the Privacy Protection Study Commission in the United States for extending privacy protection to the private sector [24].

Different approaches are also being pursued in establishing enforcement mechanisms for privacy protection requirements. Typically, they tend to reflect the traditional approaches to implementing legislation in the different countries:

1. Establishment of administrative commissions with authority to issue privacy protection regulations binding to government agencies, to grant or deny operating licences to record-keeping organizations in the private sector, and to serve as focal points for handling citizens' complaints. This approach is taken in the European privacy protection legislation and proposed on an international scale by the Council of Europe's draft convention.

2. Dependence on self-compliance with the law by the record-keeping organization with enforcement through judicial actions as necessary. The Privacy Act of 1974 in the United States is an example.

3. Development of privacy protection codes of ethics and conduct enforced by government or industry associations, subject to public scrutiny. This approach was identified as a viable option in an earlier British study on record-keeping in the private sector [20].

In general, administrative commissions are regarded as the only way to assure strong enforcement, but the wide powers of such commissions over information practices and operations of organizations raises other concerns, such as whether such commissions should be accountable to Parliaments, to the executive branch of the government, or be totally independent? For example, much of the debate over enactment of the French privacy protection law centered around the membership and powers of the National Commission for Data Processing and Freedom. It was established as an independent government agency whose seventeen membership positions were carefully apportioned to several governmental bodies (e.g., National Assembly, Supreme Court, Conceil d'Etat) and other groups. The Swedish Data Inspection Board was constituted in a similar manner. In Germany, the Federal Commissioner for Data Protection is appointed by the Federal President and, while independent in performing his duties, reports to the federal Minister of Interior.

## 3. Implementation of privacy protection requirements

Compliance with privacy protection requirements requires record-keeping organizations to establish new record-keeping and data processing policies and procedures, and to implement new technical capabilities. In general, the following types of requirements may be involved

1. Issue public notices on the existence and about the purposes of their automated personal data record-keeping systems.

2. Notify individuals about the existence of personal data records about them.

3. Establish procedures and facilities where individuals can inspect their own records, make these records available in a form comprehensible to the individual, establish procedures for reviewing challenges to data quality, provide means for including rebuttal statements, and establish mechanisms for notification or prior recipients of disputed records of corrections or amendments that were made.

4. Retrain from using data for purposes not previously announced unless explicitly permitted by law or unless prior permission has been obtained from individuals concerned. Establish procedures for requesting permissions.

5. Kee, an accounting of all disclosures to other organizations such that the data could be traced (e.g., for sending corrections).

6. Establish procedures and means for assuring that personal data are collected by lawful and fair means, and that they are appropriate and relevant for the purposes they are collected for, and that they are accurate, complete and up-to-date.

7. Maintain confidentiality of personal data by limiting access to only those personnel of the organization who need them in the course of their duties.

8. Conform with security standards that afford reasonable protection to the data processing facility, equipment, programs and data against accidental loss or deliberate destruction, and against unauthorized access, alteration, or transfer.

In addition, if a license must be obtained, an organization may have to prepare a detailed description of its record-keeping operations and submit to an on-site inspection by the licensing authority. For example, the licensing action by the Swedish Data Inspection Board involves, in addition to evaluating the purpose and function of the system, an examination of the technical aspects of data processing and storage, and the organization's plans to assure data quality, confidentiality and security. The Board may issue directives on rectifying inadequacies in record-keeping prior to granting a license [25].

## 3.1. Notifications

Notification procedures are designed to implement the prohibition against maintaining secret data systems, the right of individuals to know about personal data records about them, and their right to control non-routine dissemination and use of these data. Public notices on the existence of data systems may be issued in official government journals, in newspapers, printed on information collection forms, included in correspondence with data subjects, and/or provided upon request from public registers of record-keeping systems. For example, under privacy protection laws in force in the United States, Canada, and Germany, the federal government agencies of these countries must publish notices annually in government gazettes. In United States, the notices on the 6753 data systems of the federal government required over 4000 pages in the Federal Register, and preparation of these notices amounted to over 12% of the annual cost of implementing privacy protection requirements. In Sweden and in France, public notices are not required, but public registers are maintained by privacy protection commissions.

All existing privacy protection laws require that record-keeping organizations subject to law must, upon requests by individuals, notify them about any personal data records about them in data systems, and about the procedures to be followed to gain access for inspection of these records. An obvious short-coming of the notification upon request approach is the burden placed on the individuals—they may have to submit notification requests to a large number of organizations. Automatic notification of all data subjects of all data about them (i.e., the right for printout) is currently regarded as prohibitively costly. However, in certain systems where routine communications already exist between organizations and data subjects (e.g., billing, renewal of licenses or policies, taxation), notices and even printouts can be included with only a marginal increase in cost.

## 3.2. Inspection and reviews

Basic to privacy protection is the right of individuals to inspect their personal records, challenge their veracity or relevance, request corrections, and submit rebuttals when an organization refuses to make the requested changes. In order to facilitate exercising of privacy rights, an "easy access" approach is being implemented in the United States [26]:

1. An individual requesting access to personal records does not have to provide any justification for doing so.

2. Inspection can be done in person at a location convenient to the individual, or by mail.

3. Identification provided by the individual can be of the type people normally have (such as a driver's license) or, in absence of such identification, a signed statement of identiv is acceptable.

4. It is not necessary for the individual to know the precise Identifiers used by the organization in accessing personal records.

5. Individuals are permitted to take along another person and need not to justify this.

6. Records must be presented in comprehensible form - the various codes used in the data system must be translated into descriptive terms.

Special procedures may have to be implemented for permitting inspection in cases where the information is sensitive and knowledge may be harmful to the individual, as may be the case when certain medical and psychiatric data are involved. In such cases the individual will be permitted to designate someone competent to make the inspection in the individual's behalf. Another special situation arises in the case where information about an individual is contained in someone else's records and is not directly retrievable without brute-force search. Pending other solutions, this problem is handled in the United States by interpreting the intent of the Privacy Act as applying only to records that are directly retrievable using the individual's name or other identifiers.

Finally, to forestall possible harassment through frequent notification and inspection requests, organizations are permitted to make nominal charges for each instance, or to place a limit on the number of requests that may be made annually. For example, the Swedish Data Act permits one request per year from the same individual regarding the same data system. In general, experience to date indicates that there will not be a flood of inspection requests upon coming to force of a privacy protection law.

Implementation of the above provisions usually requires increasing the organization's staff, producing computer programs for translation of coded data into text form, and establishing of accounting systems. For more increases in the record storage requirements are likely to ensue as new data fields may have to be added for information about inspections and their results and for possible rebuttal statements. Experience in augmenting the Privacy Act in the United States has that 30% of the compliance costs are attributed to inspection requests.

## 3.3. Accounting requirements

To comply with privacy protection requirements, a record-keeping organization may have to maintain records of all non-routine disclustes of personal data to other organizations such that.

1. A list of disclosures can be furnished to individuals upon request;

2. Corrections and rebuttials can be sent to recipients;

and

3. Organization's compliance with privacy protection requirements can be audited

Accounting records must be sufficiently detailed in describing data items involved such that when a correction is made, only those who had received the data item in question will be sent the corrected version.

From technical point o view, accounting files must be designed so as to permit extraction all disclosures and transactions involving a particular individual. It is important that accounting requirements not be excessive (i.e., not involve high volume, routine transactions) since these files may easily be larger than the original record-keeping system itself, especially when long retaining periods are required. Costs to the organization include the additional storage media required, and processing time to generate the accounting records. Experience with the Privacy Act in the United States shows that 25% of the annual privacy protection cost stems from the accounting requirement.

An important aspect of the accounting requirement deals with compliance auditing. There are number of complex, unsolved problems here. For example, how can an oversight agency or the general public be assured that a government agency is not maintaining secret data systems? How can individuals be assured that they are shown all personal data about the ourselves? Finally, how can it be proven that illicit disclosures, or unlawful data exchanges or linkages are not taking place between organizations? Technical solutions to these problems are likely to be complex and costly, if they exist at all. For example, it may be necessary to design and install tamger-proof accounting systems operated by oversight agencies. In the absence of technical solutions, it may be necessary to depend on ethical employees to inform oversight agencies or news media of privacy law violations.

## 3.4. Data quality

Requirements that personal data maintained in automated record-keeping systems be relevant and appropriate for the decisions being made, complete, accurate, and up to date are basic in all privacy protection laws. Determination of relevance is a most important policy action – it establishes the representation of the individuals concerned for the purpose of decisions to be made. Including certain categories of personal data items and leaving out others can significantly affect the fairness of these decisions. Certain types of personal data are excluded in privacy protection laws. For example, in France, data which reflect an individual's racial origin or political, philosophical or religious opinions, or trade union membership cannot be collected without consent. In the newly enacted Norwegian privacy protection act, relevance decisions are made by the Data Surveillance Service by balancing the privacy interests of individuals against needs of the organization requesting permission for data collection and use. In general, to assure the due process rights of individuals regarding decisions made about them, their representatives should participate in policy decisions involving data relevance.

Accuracy of personal data can be improved by collecting them from original sources. This may even be required by law, is in the case of the Privacy Act of 1974 in the United States which specifies that personal data be collected " . . . to the greatest extent practicable from the subject individual when the information may result in adverse determinations ..." Data values close to some threshold which would make a significant difference in the decision should be reverified. In certain cases, thresholds should be specified as ranges of values rather than single values.

Certain data are "soft" in the sense that they represent judgements or options rather than facts. Thus, it would be misleading to attribute accuracy to such data. However, for increased confidence in evaluations, they should be obtained from several independent sources. The context in which evaluations are made is often crucial in their interpretation and should not be discarded in the interest of storage economy. For example, categorizing individuals as "high risk" for insurance purposes just because they fit the characteristics of some population group may be highly unfair.

Timeliness in personal data can be improved by periodic revalidation. The selection of data items to be revalidated and determination of the rates at which this should be done are policy actions which should involve consultations with the representatives of the subject individuals. Inspection by the individual is, of course, the best way to verify accuracy, timeliness and completeness of at least those data items that are in the individual's interest to keep accurate and current.

Technical means for maintaining data quality in an automated record-keeping system include the use of special coding or processing techniques (such as error detecting and correcting codes, and check-stems) for preventing modifications of the data due to human or machine errors, and appropriate techniques for increasing the system's reliability [27].

## 3.5. Data security

Data security must be maintained in order to prevent their accidental or intentional, but unauthorized disclosure, modification or erasure. It is a requirement independent of the nature of the data, but all privacy protection laws also require implementation of security safeguards. For example, the Privacy Act in the United States requires the establishment of administrative, technical and physical safeguards to insure the security and confidentiality of personal data records and protection "...against any anticipated threats to data security or integrity which could result in substantial harm, embarrassment, inconvenience, or unfairness to any individual on whom information is maintained." Several sets of guidelines for implementing data security are available [28-31].

The need for security safeguards depends on:

1. The sensitivity, volume, and frequency of use of stored data

2. The size and diversity of the user population.

3. The structure and operating environment of the data processing system.

For example, security threats are likely to be more serious in record-keeping systems which (a) are serviced by resource-sharing computer systems accessible from remote terminals, (b) where other, unrelated processing takes are processed concurrently with sensitive personal information, and (c) where some of the users of the systems are not associated with the record-keeping organization.

In any record-keeping system certain basic security safeguards must be implemented:

1. Access afforded only to those agency personnel whose official duties require use of personal information they need to know.

2. Physical protection provided to records on demountable storage media.

3. Protection provided to communication links between the computer and remote terminals.

In general, the nature of the safeguards implemented should be a function of the sensitivity of the data stored and processed, and the estimated risk to the system. Thus, it is desirable to establish sensitivity categories for personal data, specify minimum safeguards which should be implemented for each sensitivity category [32], and perform data security risk analyses. The goal is to plan and implement security systems that can adequately mask the identified vulnerabilities and, with acceptable confidence, counter the perceived threats [33-35]. A variety of techniques are available for implementing physical security, access controls and security software systems, and communications security [29,30,36-39].

## 4. Trans-national data flows

Concurrently with the development of computer-communication networks within national boundaries, similar systems spanning the national borders have come into existence, albeit at a lesser scale and rate. For example:

1. Multinational corporations have found it natural and economical to establish computer-communication links between their headquarters and their subsidiaries in foreign countries.

2. Data processing service bureaus are seeking to extend their markets into other countries.

3. Organizations in various countries dealing with international transactions or services have established common data communication systems,

4. International organizations provide information services to member countries.

5. National governments are responding to common problems by exchanging information over computer networks.

## 4.1. Privacy protection

A certain fraction of the data involved in these system are personal data on indertifiable individuals.

For these data the question of privacy protection arises, Most of the countries in the world have not yet enacted privacy protection laws, and those that have are concerned over their ability to tend privacy protection available at home to personal data about their citizens that are processed or stored abroad.

These and related concerns, and questions about balancing the benefits of free transnational data flows against potential harms that may result, have been subjects of a number of studies [40,41], and topics of international syposia [42,43]. The following approaches have been suggested and are being studied:

1. Harmonizing national data protection and privacy laws and/or establishing bi- or multilateral reciprocity agreements to extend the protection by national laws to cover personal information transferred between signatory countries.

2. Establishment of a binding international convention on privacy rights. A draft convention by Council of Europe incorporates and strengthens the data protection conventions this body previously adopted [10,11].

Regardless of the type of approach chosen to alleviate and balance the present privacy, dependency, and protectionism concerns of the countries involved in transnational data flows, there are a number of procedure and technical measures that must be provided to implement and enforce the agreement. Important among these are procedures and technological means for implementing privacy protection requirements similar to those discussed above in the context of national privacy protection laws. However, there are humorous new issues and problems:

1. Language differences between countries whose responsibility is it to perform the necessary translations?

2. Location of sites where inspection can be performed in person -- must the individual travel to the country where data on him are maintained?

3. Identification required from the individual when his inquiry is submitted by mail - how would ease of access be balanced against the threat of impersonation? How would impersonation be detected and penalties applied in trans-border inquiries?

4. Data quality - would a data processing organization abroad be responsible for obtaining additional information on residents of other countries in order to improve completeness and accuracy of personal data, and maintain them up-to-date?

5. Responsibility for preventing diversions, for unannounced distribution, for limiting access, and providing confidentiality and security if this responsibility belongs to the organization abroad, can compliance be enforced effectively from another country?

6. Penalties and restitution to individuals for privacy violations by record-keepers abroad - s the present international law adequate and easy to use without high-caliber legal assistance?

If the "easy access" philosophy were followed to resolve the above issues; certain approaches to some of the above questions are indicated. Let $X$ designate an organi, at on in the home country, $A$ , that transmits personal data abroad. Let $Y$ be an organi, at on in the host country, $B$ that receives personal data from $X$ for storage, processing and/or use. Then, the responsibility of serving as an interface between an individual in country $A$ and the record-keeper $Y$ on country $B$ could be placed as follows:

1. Organization X serves as the focal point for public and individual interactions with Y when X initiates data transfers to Y, be as a subsidiary, represents the parent multinational corporation Y. Furthermore, X would be responsible for data quality and for taking steps to assure Y's compliance with requirements in force in country 4.

2. In the case where Y collects personal information directly from residents of A, they can interact with Y directly when still in country B, or when in their own country through representatives of Y, or through a Supervisory Authority structure proposed in Council of Europe's draft Convention.

Implementing the above arrangements would allow individuals to exercise their privacy rights vis-s-vis Y in their own country and in their own language, with the focal point organizations X responsible for any translations and correspondence with Y. The details of implementing the different privacy protection requirements such as notification, inspection, etc. are discussed elsewhere [44]

## 4.2. Security considerations

Security aspects of implementing privacy protection requirements were summarized earlier in general terms. Added to these in transnational data processing and computer-communications systems are other considerations that may constrain management's control and complicate sensitivity and risk analyses:

1. While international standards for technical aspects of data communication are been developed (see, in general, [45]), no international standards are available for data sensitivity classification, physical environments in which data are processed and stored, clearance of system personnel, access controls, identification, auditing, and day-to-day operating procedures [46].

2. Existing international agreements, such as the International Telecommunications Convention of Malaga-Torremoliness, recognizes the "sovereign right of each country to regulate its telecommunications". While it is not addressing computer data communications directly, the Convention recognizes the rights of any signatory nation to: (a) monitor international communications and to stop transmission of any private communication which may appear dangerous to its security or contrary to its laws regarding public order or decency; (b) suspend indefinitely all international telecommunication services, including communications in transit; and (c) accept no responsibility towards users, particularly in regard to claims and damages.

3. Internationally, there is no uniformity of legal prohibition against interception or diversion by private parties of data in telecommunication systems.

4. There is a wide variation in the technical characteristics of telecommunication systems in various countries: and, correspondingly, in vulnerabilities of these systems to data security threats.

Thus, security systems implemented in transnational data processing systems must handle various national requirements while attempting to provide protection in an environment of (potentially) diverse equipments and operating procedures. For example, the ability to use encryption in transnational data communications depends on whether or not the governments involved insist on exercising their rights and prerogatives under the Malaga-Torremolino Convention.

## 5. Concluding remarks

Even though the existing privacy protection legislation tends to be quite specific on the privacy rights that are granted to individuals, and on the requirements that must be implemented by record-keeping organizations, there still is considerable latitude in interpretation of these requirements and choice of procedural and technical details in their implementation. Experience with existing and soon to be enacted privacy protection laws will eventually provide an empirical data base which can be used to rank implementation options on the basis of their suitability in various types of record-keeping and on the basis of their costs.

Implementation of privacy protection and data security requirements in transnational computer-communication systems involves numerous unanswered questions about policies, procedures, and technical means. However, it appears that transnational privacy protection requirements would be easiest to satisfy when organizations that transfer personal data to record-keepers abroad also serve as interfaces for individuals who want to exercise their privacy rights.

Techniques now exist for satisfying most of the data security requirements in computer-communication systems, but their effective use in trans-national systems may be constrained by a lack of standards. In particular, effective use of encryption as a communications security technique may be difficult if the countries involved want to exercise their right to monitor transborder communications traffic.

## References

[1] P.R. Vinge, Swedish Data Act, Federation of Swedish Industries (Steckholm, December 1973).

[2] Privacy Act of 1974, Title 5, United States Code, Section 552a (Public Law 93 579, December 31, 1974).

[3] Federal Data Prot. 19: 61 (20) - 61: tenschutzgesetz.
Bonn, 27 January 1, 27

[4] Lata Processing, Files and v. acm - t (Loi de l'Informatiques c' aux Liberte, Paris, 22 December 1977).

[5] Canadian : Human Rights Act, Part IV, Protection of Personal Information (Ottawa, October 1977).

[5] Personal Data Register Act (Oslo, 18 May 1978).

[7] F.W. Hondius, Emerging data protection in Europe (North-Holland/American Elsevier, Amsterdam, 1975).

[8] C.K. Wilk (Ed.), Selected foreign national data protection laws and bills, Office of Telecommunications, U.S. Department of Commerce (Washington, D.C., March 1978).

[9] Focus on France, Transnational Data Report 1 (March 1978) 1-4.

[10] Protection of the privacy of individuals vis-s-vis electronic data banks in the private sector, Revolution (73) 22, Committee of Ministers of the Council of Europe (Strasbourg, 30 September 1973).

[11] Protection of the privacy of individuals vis-vis, electronic data books in the public sector, Resolution (74) 29, Committee of Ministers of the Council of Europe (Strasbourg, 31 September 1974).

[12] J.W. Honduras, T.C. Council of Eur. ne's data protection, principles, Proc. Intern. Conf. C. Data Regulation (Online Conferences, Ltd., Uxbridge, England, February 1978).

[13] Human rights and the scientific and economical development, Commission on Human rights, United Nations Economic and Social Council (New York, January 9, 1974).

[14] Policy issues in data protection and privacy, OFCD (Paris, June 24-26, 1974).

[15] A. Westin, Privacy and Freedom (Athenetm, New York, 1968).

[16] A. Westin and M.A. Baker, Databanks in a free society; computers, record-keeping and privacy (Quadrangle Books, New York, 1972).

[17] A.R. Miller, Assault on privacy: computers, data banks and dossiers. (University of Michigan Press, Ann Arbor, Michigan, 1971).

[18] J.B. Rule, Private lives and public surveillance, (Allan Lane, London, 1973).

[19] Privacy and computer, Information Canada (Ottawa, 1972).

[20] Report of the Committee on Privacy, 5012, Her Majesty's Stationery Office (London, July 19-2).

[21] Rapport de la Commission Informatique et Liberte, decret no. 74, 938 du 3 avenirre 1974 (La documentation française, Paris, 1975, in French)

[22] Computers and privacy, Cm. 635, Her Majesty's Stationery Office, (London, December 1975).

[23] Records, computers and the rights of citizens. A report of the Secretary's Advisory Committee on Automated Personal Data Systems, U.S., Department of Health, Education and Welfare (Washington, D.C., July 1973).

[24] Personal privacy in an information society, Report of the Privacy Protection Study Commission (Washington, D.C., July 1977).

[25] J. Freese, The Swedish Data Act, Press Intern. Conf. on Trans-National Data Regulation (Online Conferences, Ltd., Uxbridge, England 1978).

[26] Privacy Act implementation: guideline and responsibilities, Federal Register 40. (July 9, 1973).

[27] J. Martin, Security, accuracy and privacy in computer systems (Pre- et al., Inc., Eaglewood Cliffs, N. 1973).

[28] Computer security guidelines for implementing the Privacy Act of 19'4, FIPS Pub 41, National Bureau of Standards, U.S. Department of Commerce (Washington, D.C., May 1975).

[29] Guidelines for physical security and risk management, FIPS Pub 31, National Bureau of Standards, U.S., Department of Commerce (Washington, D.C., June 1974).

[30] AI IPS System review manual on security (AI IPS Press, Montvale, N.J., 19 $^{4}$ ).

[31] Where next for computer security?, The National Computer Centre, C'd., (Sandbach, England, 1974).

[32] R. Turin, Classification of personal information for privacy protection purposes, AFIPS Conf. Proc. 46, 1976 Nat. Comp. Conf. (AFIPS Press, Montvale, NJ., 1976) 301-307.

[33] R.H. Courtney, Security risk analysis in electrochemical processing systems: AFIPS Conf. Proc. 46, 1977 Nat. Comp. Conf. (Alli S Press, Montvale, N.J., 1977) 97-104.

[34] K.K. Wong, A new approach to risk analysis and control The UK experience, Information Processing 77, Proc. II-IP Congress 77 (North Holland/American Elsevier, Amsterdam, 1977) 905-910.

[35] S. Glaseman, R. T. Liu, and R.S. Gaines, Problem areas in computer security risk assessment, AIIPS Conf. Proc. 46, 1977 Nat. Comp. Conf. (AIIPS Press, Montvale, N.J., 1977) 105-1

[36] J. II Salzer, and M C Schroeder, Protection of information in computer systems, Proc III 1-63 (September 1975) 1278-1308.

[37] T.A. Linden, Operating system structures to support security and reliable software, Computing Surveys 8 (December 1976) 409-445.

[38] H. Wood, The use of passwords for controlling access to remote computer systems and services, AFIPS Conf. Proc. 46, 1977 Nat. Comp. Conf. AFIPS Press, Monvale, N.J., 1977) 27-34.

[3c] R. Turn, Privacy transformations for databank systems, AFIPS Conf. 42, Proc. 1973 Nat. Comp. Conf. (AFIPS Press, Monvale, N.J., 19°3) 589-601.

[40] J.M. Carroll, The problem of transnational data flow, Policy Issues in Data Protection and Privacy. OFCD Informatics Studies 10 (OECD, Paris, 1976) 201-207.

[41] A. Gotieb, C. Dalfen, and K. Katz, The transborder transfer of information by communications and computer systems, Am. J. Intern. Law (April 1974).

[42] Symposium on transborder data flows and protection of privacy trends and impacts, OECD (Vienna, September 20-23, 1977).

[43] Intern. Conf. on Trans-National data regulation, Online Conferences, Ltd. (Brussels, February 7-9, 1978).

[44] R. Turn, Implementation of privacy and security requirements in trans-national data processing systems, Proc. Intern. Conf. on Trans-National Data Regulation (Online Conferences, Ltd., Uxbridge, England, February 1978).

[45] Conference on computer/telecommunications policy, OFCD Informatics Studies 11. (OFCD Paris, 1976).

[46] D. Firnberg, Security standards for transborder data flows, OECD Symp. on transborder data flows and protection of privacy - trends and impacts, (Vienna, 20–23 September 1977).
