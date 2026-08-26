---
otero_id: 23782
otero_key: "SABRGVNK"
title: "Some systems implications of EU Data Protection Directive"
authors: "F-A Allaert; B Barber"
year: "1998"
journal: "European Journal of Information Systems"
doi: "10.1057/palgrave.ejis.3000278"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Some systems implications of EU Data Protection Directive

F-A Allaert<sup>1</sup> and B Barber<sup>2</sup>

<sup>1</sup>Agence pour la Protection des Syste<sup>\`</sup>mes d’Information de la Sante<sup>´</sup>, APSIS, Dijon, France; <sup>2</sup>NHS Executive, Birmingham, UK

## Introduction

At the present time we do not know exactly how the various provisions of the European Union Directive 95/46/FC ‘On the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of such Data’ (1995) will be interpreted bu it can be expected to usher in a new data protection regime for most of the European Union. It aims to “protect the fundamental rights and freedoms of natural persons, and in particular their right to privacy with respect to the processing of personal data” [Art 1.1] and to facilitate “the free flow of personal data between Member States” of the European Union [Art 1.2]. In effect the Directive defines ‘data privacy’ for the EU for the next few decades. The text is an agreed compromise text which provides a variety of options for Member States which they may choose to exercise when framing their national legislation. It extends the scope of the data protection arrangements demanded by the Council of Europe Convention 108 (1981) by requiring, amongst other things, that sound, image and manual data [Art 2(c) ‘personal data filing systems’] are all brought within the scope of this new legislation. At this stage in the development of new legislation it is far too early to be sure of how the law will be developed and interpreted, but informaticians and systems engineers must begin to address the likely systems implications of the Directive as any necessary facilities must be in place in respect of ‘new processing’ by 24 October 1998 at the latest. The presentation represents a prudent and conservative systems engineer’s approach to the likely systems requirements. When the full legal force of the new legislation becomes apparent, it may be that some of the requirements will prove to be unnecessary because the law is not interpreted as stringently as the strict reading of the words might suggest. However, the history of data protection is that initial requirements tend to be interpreted in a strengthened fashion as the data protection commissioners and the courts review practice in the light of the specified legal texts. In this context it may be expected that the processing of special categories of data, including personal health data which is prohibited under Article 8 unless special safeguards are in place, will tend to attract the more stringent safety measures as time goes by. Furthermore, as faster and more capable technology becomes available, practices which would have been prohibitively resource consuming or expansive become standard practice for organizations that do not wish to be seen as negligent. Correspondingly, such technologies reduce the protection provided by previously adequate measures of data privacy and, hence, establish the need for further safeguards.

## Implementation timescales

Article 32 of the Directive indicates that national legislation is required by 24 October 1998 and that there is an exemption for “processing that is already under way on the date the national provisions enter into force” which allows three years from that date for such processing to be brought into compliance. In order to test whether any processing of personal data is in progress it would appear that one only needs to issue a subject access request. If the result is positive then ‘some processing is already under way’, otherwise no processing is under way. The simplicity of this test is that it is logical and quite unambiguous. The exemption does not refer to ‘processing systems’ but to ‘processing’ and it does not allow as much time for compliance as appears at first reading of the text. The implication is that all ‘new processing’ will have to comply by 24 October 1998 at the latest and in systems terms this leaves little time for the systems development and testing that may be required, the issues relating to manual files or ‘personal data filing systems’ are more complex and do not immediately impinge upon the systems required for automated processing. However, the allowance of an extended period of six years until 24 October 2007 for bringing these files into compliance with the Directive is limited by the need to give subject access throughout this extended period, and by the implications of the second half of Recital 69 which appears to require that as personal data held in personal data filing systems is utilised during this period it is required to bring the whole system up to the standards required by the Directive rather than just the file in question. Where a large system of manual medical records is concerned, it would appear impossible to bring the whole “system into conformity with these provisions [of the Directive] at the time of such processing”.

## Health care requirements

The sensitivity of personal health data is recognised in Article 8 of the Directive which is concerned with the processing of special categories of data. The key issues in health care arise from the well established need for confidentiality, together with the even more serious requirements for the integrity and availability of the patient data required where the information systems are concerned with the active treatment of patients, and where patients may suffer damage or death if the information on which their treatment is based is either wrong or missing. Work on the use of the CCTA Risk Analysis and Management Methodology, CRAMM (CRAMM User Guide, 1996) illustrated the health care issues arising from situations where information systems are used as an integral part of the treatment process (Barber & Davey, 1992; Barber et al, 1992). The effect is that where personal health data are simply recorded for research or other purposes but not utilised directly in the processes of delivering health care, the key issue is that of confidentiality and the various issues of confidentiality have been well recognised by health care professionals from the time of Hippocrates and continue to be regarded as vital to patient confidence in the caring processes (Griesser et al, 1980, 1983; Gaunt & Roger-France, 1990; EU Commission, 1991a,b; Allaert & Dusserre, 1992; Barber et al, 1994; Allaert & Dusserre, 1994). The AIM SEISMED project (Secure Environment for Information Systems in MEDicine) developed this work on a European basis and issued a set of guidelines for routine use in health information systems (Barber et al, 1990; The SEISMED Consortium, 1996). These guidelines have been developed as a self-consistent set to be used by managers, users and technical staff. They were developed in a fashion consistent with the EU data protection directive and the work of the Council of Europe on the Protection of Medical Data (1996). The health telematics ISHTAR project (1996) is carrying out further elaboration and validation of these guidelines at 100 centres.

## Developing standards for health information systems

It had always been envisaged that computer controlled systems of clinical care would be developed in which the delivery of care was handled autonomously by a computer system but that such ‘safety-related systems’ would require very special design and testing. The beginnings of such safety standards are outlined in the recent standardisation work of the International Electro technical Commission (Shaw, 1990; Draft International Standard IEC, 1995; Bennett, 1994) and in the requirements for handling medical devices (EU Council Directive, 1993). However, the advent of health information systems that are at the heart of the processes of delivering care has led to the potential for causing damage to patients despite the fact that the systems are not directly connected to patients in the sense of acting as a conventional medical device. A clinician is located in the ‘air gap’ between the patient and the information system but where that clinician does not examine the information provided by the system in a critical fashion, or where he is unable to obtain information from the system, it is possible for him to provide inappropriate care or fail to provide appropriate care as a result of which the patient may be damaged or even die. The reasons for such a failure may vary, the clinician may be tired after a long period on duty, he may be worried about family or other matters, he may not have been trained properly, but for whatever reason, a cross-check is not carried out that could have revealed the problem. Such problems arise at inquests but until recently they have not involved computerised information systems. As a result of these considerations, the European standards body for Medical Informatics (CEN Technical Committee 251 Working Group 6) has developed a standard (CEN, 1996) that should be out for ballot shortly which seeks to classify health information systems according to their security features in terms of their requirements for confidentiality, integrity, and availability and to provide a set of appropriate protection measures for the various categories of the system.

## System requirements

## Security

Article 17 of the EU Directive requires “appropriate technical and organizational measures to protect personal data in particular where the processing involves the transmission of data over a network” which have “regard to the state of the art and the cost of their implementation” and are “appropriate to the risks represented by the processing and the nature of the data to be protected”. These requirements need to be in place as soon as the national legislation becomes effective. In addition, the approach taken by the Directive effectively mandates the use of risk analysis. Inadequate security will certainly breach the requirements of the Directive and can render the ‘controller’ liable for negligence under Articles 22–24 which are concerned with Judicial Remedies, Liability and Sanctions. The issue of the interpretation of the text in Article 23.2 which allows that: “The Controller may be exempted from this liability, in whole or in part, if he proves that he is not responsible for the event giving rise to the damage” could be significant, as usually the controller will not be directly responsible for a security breach. It is more likely that his negligence may arise from the failure to implement some security measure, and hence left open some system vulnerability, which a reasonable person would have implemented if he was knowledgeable about the current practice and costs in information systems security and if he had understood that likely impact on his patients or his organization of a security breach. It is likely that prudent hospitals will ensure that they have appropriate security audits commissioned so that they can, at least, prove that they have taken these issues seriously and ensured that all reasonable measures have been installed.

Where personal health data, or other Article 8 special category data are involved, and where these data are networked, higher levels of security will clearly be appropriate. In the networking context it is diffuclt to envisage any current alternatives to the use of cryptographic security services. Digital signatures are likely to be required to ensure that information has not been tampered with and that its origin has been securely authenticated, and personal health data are likely to need to be encrypted appropriately when they are sent over open networks. These facilities will be greatly assisted with the widespread availability of a networking infrastructure that provides such services together with trusted third parties and smart cards that can hold the private keys and the associated certificates. Work is in progress on these issues both nationally across Europe and within EU TrustHealth (1996) and SIREN projects (1996).

## Rectification, erasure and blocking

Article 12(b) allows data subjects to secure the rectification, erasure or blocking of their personal data where these data do not comply with the requirements of the Directive “in particular because they are inaccurate or incomplete”. Facilities are required to allow this to happen. In general, in health care it will be appropriate to block the personal data in question so that the clinicians have access to the information but yet it is clearly marked as ‘inaccurate or incomplete’ and is not made available to third parties.

## Third party disclosures

Where personal data have been rectified, erased or blocked, data subjects can require that the controller notifies third parties of this rectification, erasure or blocking ‘unless this proves impossible or involves a disproportionate effort’. This clearly requires a third party disclosure register of some sort to be built into the systems audit trial and it is difficult to see that this would be an unreasonable requirement bearing in mind that special category personal data are being passed to third parties. It might be that the existing audit trails of some systems would be adequate for this task but it is likely that a special register will be required unless this requirement turns out to be very infrequently required. Furthermore, it might be desirable for the register to be kept as part of the patient record and to include all recipients of personal health data rather than simply third parties.

## User authentication

In order to enable these matters to be resolved, it is important that all users of the information system should be properly authorised and authenticated. This is a basic security requirement of all information systems, but the arrangements in many health care settings allow systems to be logged-in all days and utilised by whom so ever requires to use the system, or else users freely share their passwords with colleagues. These practices must be prohibited as systems become an integral part of the delivery of health care. If no-one knows who is using the system or entering information into the system, then it can only mean that the system is of no particular importance. Such an approach would not be accepted in the context of the written medical record. This requirement for authentication of system users is particularly important where third parties are given access to health information systems as they are subject to quite different rules in the Directive. This practice is becoming much more common where the delivery of care involves multiprofessional teams, shared care between hospitals, community care providers and general practitioners.

## Data origin and consents

The Directive has a number of articles concerned with the origin of personal data (Articles 10 & 11] and the consents for data usage [Articles 7 & 8] and transmission across borders where there is no “adequate level of protection” [Art 261]. It may be that, eventually, it will be necessary for information systems to record the basis for processing and these various consents in a clear and unambiguous fashion and as a fundamental part of the patients’ record.

## Conclusion

The EU Directive establishes a number of requirements for health information systems which need to be considered and addressed now if the next generation of health information systems are to be compliant with its requirements as well as being responsive to health care needs in the next century.

Digital signatures are currently thought to be the most appropriate means of secure authentication and verification of the integrity of the information contained in

either messages or files. Article 17 is especially concerned with the issues of processing involving transmission over a network. This appears to mandate the use of encryption for confidentiality where such services are required, for instance in the transmission of personal health data over networks and the use of digital signatures for the authentication of the origin of messages and the Draft Convention “For the Protection of Human Rights and Dignity of the Human Being with Regard to the Application of Biology and Medicine, Bioethics Convention”, Directorate of Legal Affairs, Council of Europe, Strasbourg, July 1994.

## References

Allaert FA and Dusserre L (1994) Security of Health Information Systems in France: What we do will no longer be different from what we tell. pp 201–204 in Barber et al (1994).

Allaert FA and Dusserre L (1992) Transborder Flows of Personal Data in Europe- Legal and Ethical Approach. In MEDINFO 92 (Lun KC et al, Eds) pp 1572–1575, IMIA, by North Holland, Amsterdam, ISBN 0 444 89668 6.

Barber B and Davey J (1992) The Use of the CCTA Risk Analysis and Management Methodology [CRAMM] in Health Information System’s. In MEDINFO 92 (Lun KC et al, Eds) pp 1589–1593. IMIA by North Holland, Amsterdam, 1992, ISBN 0 444 89668 6.

Barber B et al (1990) Towards Security in Medical Telematics. vol 27, In Studies in Health Technology and Informatics. IOS Press, Amsterdam, ISBN 90 5199 246 7.

Barber B, Vincent R and Scholes M (1992) Worst Case Scenarios: the Legal Consequences. In Current Perspectives in Healthcare Computing (Richards B et al, Eds), pp 282–288, British Computer Society by BJHC Weybridge, ISBN 0 9481-98 12 5.

Barber et al (1994) Caring for Health Information: Safety; Security and Secrecy. IMIA WG4 Elsevier, Amsterdam, ISSN 0020-7101. Also in International Journal of Bio-Medical Computing, 35, Sup plement, February 1994.

Bennett PA (1994) Standards in Medical Software. pp 197–213 in Barber et al (1994).

CEN (1996) Security Categorisation and Protection for Healthcare Information Systems, draft CEN prENV, ref CEN TC25 1 fWG6 N96-060, 1996-10-26.

Council of Europe Convention 108 (1981) For the Protection of Individualise with regard to Automatic Processing of Personal Data. January 1981, ISBN (1982) 92-871-0022-5.

CRAMM User Guide (1996) Issue 1.0, April 1996, CRAMM software version 3.0. The CRAMM Manager, PO Box 1028, London N1 1UX, UK.

Draft International Standard IEC (1995) 1508 Functional Safety Related Systems June 1995. Part 1: General Requirements (65AJI79/CDV). Part 2: Requirements for Electrical/Electronic Programmable Electronic Systems (65A/180/CD). Part 3: Software Requirements (65A/Igl/CDV). Part 4: Definitions and Abbreviations of Terms (65A/1 82/CDV). Part 5: Guidelines on the Application of Part 1 (65A/183/CDV). Part 6: Guidelines on the Application of Parts 2 and 3 (65A/184/CD). Part 7: Bibliography of Techniques and Measures (65A/185/CD).

EU Commission (1991a) Data Protection and Confidentiality in Health

Informatics: Handling Health Data in Europe in the Future. DG XIII/F AIM, vol 1. In Studies in Health Technology and Informatics, IOS Press, Amsterdam, ISBN 90 5199 052 9.

EU Commission (1991b) The Six Safety First Principles Of Health Information Systems- A Programme of Implementation. Part 1 Safety and Security, Barber B et al, pp 297–301. Part 2 The Environment, Convenience and Legal Issues, de Schouwer P et al pp 302–307. Progress Report, Barber B and O’Moore R, pp 308–314.

EU Council Directive (1993) Concerning Medical Devices. OJ L169/1-43, 14 June 1993 Directive.

FA Allaert is a medical doctor and lawyer specialising in computer law in medicine. He is chairman of the Healthcare Data Security and Software Quality working group of the European Centre for Standardisation CENTC 251/WG III which depends on the European Union. He manages the French Agency for Healthcare Data Security (APSIS) and an Evaluation Centre of Biotechnologies (CENBIOTECH).

European Union Directive 95/46/EC (1995) On the Protection of Individuals with Regard to the Processing of Personal Data and on the Free Movement of such Data. OJ L291/31-50, 24 October 1995.

## About the authors

Gaunt N and Roger-France F (1990) The Security of the Electronic Health Care Record – Professional and, Ethical Implications. In Towards Security in Medical Telematics, (Barber B et al, Eds), pp 10–22, vol 27 in Studies in Health Technology and Informatics, IOS Press, Amsterdam, ISBN’90 5199 246 7.

Griesser G et al. (1980) Data Protection in Health Information Systems: Considerations and Guidelines. IMIA WG4 by North Holland, Amsterdam, 1980, ISBN 0 444 86052 5.

Griesser C et al (1983) Data Protection in Health Information Systems: Where Do We Stand? IMIA WG4 by North Holland, Amsterdam, ISBN 0 444 8671 3 9.

ISHTAR Project (1996) Implementing Secure Healthcare Telematics Applications in Europe, EU Fourth Framework, HT 1028, 1996– 1999.

Shaw R (1990) Safety and Security Of Information Systems. In Towards Security in Medical Telematics. (Barber B et al, Eds) pp 190–199. vol 27 in Studies in Health Technology and Informatics, IOS Press, Amsterdam. ISBN 90 5199 246 7.

SIREN Project (1996) Security in Regional Networks, HT 4110, 1996–1998.

The SEISMED Consortium (1996), Data Security for Health Care. Volumes in Studies in Health Technology and Informatics, IOS Press, Amsterdam, 1996. Vol I Management Guidelines ISBN 90 5199 264 5 (series vol 31). Vol II Technical Guidelines, ISBN 90 5199 265 3 (series vol 32). Vol III User Guidelines, ISBN 90 5199 266 1 (series vol 33).

The Protection of Medical Data (1996) (and Genetic-Data) draft Recommendation for the Council of Europe, June 1996.

TrustHealth Project (1996) EU Fourth Framework Trustworthy Health Telematics 1, HT 1051, 1996–1997.

B Barber was educated at Cambridge as a theoretical physicist and then joined the London Hospital where he set up the operational research unit. He then moved to the North-East Thames Regional Health Authority to assist with NHS planning. Subsequently he spent time implementing the Data Protection Act 1984 and then moved to the NHS executive as manager of the security and data protection programme.
