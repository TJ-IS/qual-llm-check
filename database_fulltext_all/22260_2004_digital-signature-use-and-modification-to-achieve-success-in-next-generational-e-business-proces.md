---
otero_id: 22260
otero_key: "3WSC3E5D"
title: "Digital signature: use and modification to achieve success in next generational e-business processes"
authors: "Alok Gupta; Y.Alex Tung; James R. Marsden"
year: "2004"
journal: "Information & Management"
doi: "10.1016/s0378-7206(03)00090-9"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Digital signature: use and modification to achieve success in next generational e-business processes

Alok Gupta<sup>a,\*</sup>, Y. Alex Tung<sup>b,1</sup>, James R. Marsden<sup>b,1</sup>

<sup>a</sup>Department of Information and Decision Sciences, Carlson School of Management, University of Minnesota, Minneapolis, MN 55455, USA <sup>b</sup>Department of Operations and Information Management, School of Business Administration, University of Connecticut, Storrs, CT 06269, USA

Received 1 February 2002; received in revised form 1 February 2003; accepted 1 June 2003

## Abstract

A US law, the electronic signatures (E-Sign) in Global and National Commerce Act (signed by then President Clinton on 30 June 2000 with an effective date of 1 October 2000), grants electronic signatures legal validity equivalent to traditional handwritten counterparts. The intention of this law is to cut costs while providing more stringent security. In the emerging ecommerce arena, electronic signatures hold great potential for facilitating secure electronic transactions. But signatures are used in many critical business processes that occur prior to or independent of final transactions. Contract development and numerous other processes entail a series of draft modifications and sign-offs. Can electronic signatures provide cost savings and security in these activities? In this paper, we

(i) detail fundamentals and the current status of electronic signatures;

(ii) describe the integration of electronic signatures with electronic verification and authentication technologies;

(iii) explore e-commerce applications, especially document management processes, that could benefit from adopting electronic signatures; and

(iv) propose modifications to the electronic signature process to enable innovative document management processes. We propose modifications using partial document ownership, soft signatures, and hard signatures.

<sup>#</sup> 2003 Elsevier B.V. All rights reserved.

Keywords: Electronic signature; Digital signature; E-commerce; Computer verification and authentication; Biometrics technologies; Computer security; Negotiation support

## 1. Introduction

In the e-commerce arena, security is a great concern to many organizations when a considerable volume of documents and transactions are computerized/digitized and exchanged online [8,11,13]. This paper’s primary focus is on the techniques commonly referred to as ‘‘digital signatures,’’ which are attachments to documents used to verify or authenticate a ‘‘signer’’ and the document signed. Combined with certificates issued by trusted third parties and enhanced by biometric authentication tools, digital signatures are gaining a presence in the transaction or final document arena. Our argument, however, is that their really significant benefits for companies and organizations lie in potential improvement of stepwise sign-off processes including negotiation and contract/document generation.

Following the American Bar Association (ABA) guidelines [1], we differentiate digital signatures from the more mundane digitized images of hand-written signatures, such as typed notations like ‘/s/John Smith’, or even addressing notations, such as electronic mail headers. In addition to improved security, digital signatures provide the following advantages:

(i) no need to print out documents for signing;

(ii) reduced storage of paper copies;

(iii) improved management and access (anytime/anywhere) of electronic versus paper documents;

(iv) elimination of need for faxing or overnight mailing—reduction of cycle time;

(v) improved security of document transmission; and

(vi) enhanced management processes outside the ‘‘final signature’’ step.

The concepts and ideas in this paper have been developed in an attempt to adopt leading edge digital signature technologies for everyday business processes. Operational managers helped in shaping and refining the vision of an ideal system and helped identify the shortcomings/limitations of current digital signature technology. Such interaction is critically important in understanding existing practices as well as in shaping technological solutions that enabled process enhancements.

## 2. Concept and current status of digital signature

Digital signatures process is based on the idea of asymmetric encryption. Each user of this paradigm has two ‘‘keys’’ assigned to them. One of the keys is known only to the user and is called ‘‘private’’ key while the other key is public knowledge and is known as ‘‘public’’ key. Both public and private keys can be used to encrypt or decrypt data, however, whatever is encrypted by public key can only be decrypted by private key and vice versa. Typical encryption, for example the encryption of credit card information for online transactions, requires that the data be encrypted using recipients public key so that only intended receiver (such as Amazon.com) can decrypt the data. However, digital signature involves reverse of the encryption process. The data is encrypted with the private key of an entity and anyone can decrypt it using the public key; since a public key can only decrypt the data from a corresponding private key, the identity of the sender is verified. Since digital signatures are often used with large documents and encryption is a computationally intensive technique, instead of encrypting the document, a hash of the document is typically computed and encrypted. A hash is a unique representation of a text but typically would be much smaller in size as compared to the original document. There are a variety of asymmetric cryptosystems that create and verify digital signatures. While these use different algorithms, they share the operational pattern described above. Fig. 1 depicts the digital signature creation and verification processes.We use the term authentication to refer to any process through which one verifies information. One may want to verify the origin of a document, the identity of the sender, the time and date a document was sent and/or signed, the identity of a computer or user, etc. The process of verification involves the following elements:

Digital signature: Created and verified using a cryptosystem.

Private key: One part of the key used to create the digital signature; known only to the signer.

Public key: The second part of the key used to decrypt or verify the digital signature; available to all those needing to communicate with the signer or validate the document, etc.

Hash function: Algorithm used in creating a digital representation, unique to a message or document, in the form of a hash value or hash result.

The ABA guidelines provide the following summary of the digital signature process:

To sign a document or any other item of information, the signer first delimits precisely the borders of what is to be signed. The delimited information to be signed is termed the ‘‘message’’ . . . a hash function in the signer’s software computes a hash result unique (for all practical purposes) to the message. The signer’s software then transforms the hash result into a digital signature using the signer’s private key. The resulting signature is thus unique to both the message and the private key used to create it.

![](/api/attachments/3WSC3E5D/fulltext/images/562c1635d97a21eaae1a8665f664a7a50e7e1bf440cefe8aadd4464944764c40.jpg)  
Digital Signature Creation Process Digital Signature Verification Process  
Fig. 1. Digital signature creation and verification processes.

Typically, a digital signature (a digitally signed hash result of the message) is attached to its message and stored or transmitted with the message. However, it may also be sent or stored as a separate data element, so long as it maintains a reliable association with its message. Since a digital signature is unique to its message, it is useless if wholly disassociated from its message.

Verification of a digital signature is accomplished by computing a new hash result of the original message by means of the same hash function used to create the digital signature. Then, using the public key and the new hash result, the verifier checks: (1) whether the digital signature was created using the corresponding private key; and (2) whether the newly computed hash result matches the original hash result which was transformed into the digital signature during the signing process. The verification software will confirm the digital signature as ‘‘verified’’ if: (1) the signer’s private key was used to digitally sign the message, which is known to be the case if the signer’s public key was used to verify the signature because the signer’s public key will verify only a digital signature created with the signer’s private key; and (2) the message was unaltered, which is known to be the case if the hash result computed by the verifier is identical to the hash result extracted from the digital signature during the verification process. (N.B.: ABA Guidelines refer to Schneier [15].)

In addition to the signer and the recipient, a third party has come to play a significant role in the process. It is commonly referred to as the trusted third party, this individual or entity typically issues an electronic certificate verifying that a particular public key is associated with a specific individual who holds the corresponding private key. Often referred to as the certification authority, the trusted third party in effect provides a service certifying authenticity of signer and document. In fact, the trusted third party often digitally signs the certificate, a digital signature that can be ‘‘certified’’ by yet another trusted third party. It is important to understand that the process itself may be repeated ad infinitum with certification/ verification occurring at higher and higher levels of a hierarchy. What stops the process is trust (the willingness of the recipient, the one relying upon the validity of the original signature, to accept the original signature as genuine). Clearly, efficiency in e-business applications is directly tied to such acceptance occurring very early in this cycle.

In fact, both the technology of digital signatures and the necessary legal authority are in place to attain such efficiency. Like other once ‘‘new’’ transaction processes, such as holding Federal Reserve notes rather than silver or gold, gains from convenience and efficiency and the emergence of trusted third parties will drive its acceptance and use.

## 2.1. Digital signatures within an organization

Digital signatures can also be used in processes or transactions in the organization. A network security director, MIS help desk, or other verifiable controlling authority can act as the certification authority and mitigate acceptance and use issues. Fig. 2 presents a pictorial description of such a process, which we term an Organization Digital ID (ODigID).

Here, each time someone sends a message, they attach their ODigID. The recipient first uses the ODigID to verify that the author’s public key is authentic, then uses that public key to verify the message itself. This way, only one public key, that of the certifying authority, has to be centrally stored or widely publicized, since everyone else can simply transmit their public key and valid ODigID with the messages.

Using ODigIDs, an authentication chain can be established that corresponds to an organizational hierarchy, allowing for convenient public key registration and certification in a distributed environment. One common way this can be achieved is via directory services, where the directory makes an information source available to a user community, for example, information on names, telephone numbers, and e-mail addresses or about network resources, such as printers and routers.

<table><tr><td>John Doe&#x27;s Information: Name, Organization, Address, etc.</td></tr><tr><td>John Doe&#x27;s Public Key</td></tr><tr><td>Digital ID Certificate Number</td></tr><tr><td>Digital ID Expiration Date</td></tr><tr><td>XYZ Corp.&#x27;s Digital Signature and ID Information</td></tr></table>

Fig. 2. A sample subscribed digital ID for John Doe from XYZ Corp.

Many enterprises today operate multiple independent directory services based on separate proprietary protocols, requiring separate administration and maintenance of each service. As the number of applications and utilities relying on directories has increased, the task of maintaining these separate directories has become increasingly difficult. However, a single directory service could be structured to support the enterprise as a whole, accessed by an industry standard access protocol (Fig. 3).

The goal of establishing the directory as the unified information source for the enterprise can only be met if all the applications relying on the directory support a common means of accessing and interpreting the information stored therein. Open standards are clearly necessary.

Unlike more general-purpose databases, the data in a directory is usually read much more often than it is changed. Updates to a directory are typically simple changes to a single entry rather than read-then-modify transactions affecting many entries. As a result, a directory does not, in general, require the complex transaction management or roll back schemes supported by database products. A directory is tuned to give quick response to high volumes of queries.

![](/api/attachments/3WSC3E5D/fulltext/images/ceff29eab367633156fa2d83d54e28360c6ad119967d054432c39c2a107873b7.jpg)  
Fig. 3. The directory service as the hub of a large distributed system.

A fully featured directory allows information to be replicated amongst multiple servers to increase availability and reliability. A directory application is typically tolerant of transient inconsistencies. This leads to a significant decrease in the complexity of the replication protocols.

Directories can therefore be used with Public Key Infrastructure (PKI), a system of digital certificates, Certificate Authorities, and other registration authorities that verify and authenticate the validity of each party involved in an Internet transaction. PKIs are currently evolving and there is no single PKI or even a single agreed-upon standard for setting up a PKI. However, nearly everyone agrees that reliable PKIs are necessary before electronic commerce can be widespread.

## 3. Enhanced security

While digital signatures are already being used by companies such as Federal Express in the physical world and BuyAndHold.com in the electronic world, their scope is limited, since the only requirement is to obtain the verification from a customer that he/she agrees to the statements in a given document. The party that requires the customer’s signature produces the document. The customer does not have the opportunity or the means to edit the document. Thus, the signed documents’ integrity can never be questioned. The signer’s authenticity is not under question.

For electronic contracts and negotiations, where all the parties involved may have opportunity and means to alter the document, a signature must meet the following two properties:

\- Signer authentication: A signature should indicate who signed a document, message, or record.

\- Document authentication: A signature should verify the document, i.e. ‘‘what is signed,’’ making it impracticable to falsify or alter the signed matter.

While the digital signatures based on encryption mechanisms provide significant protection from document related inconsistencies, signer authentication is reliable only to the extent that the key used was that of the appropriate person. Insecure computers, revelation of password, etc. can compromise the key.

Signer authentication can be enhanced by attaching unique identification traits of individuals to a document as an electronic signature. There are numerous electronic authentication techniques [4–6,14], which can serve this role. We briefly compare: traditional password, key cards, face recognition, fingerprints, hand geometry, retina pattern, iris scan, voice, DNA, and hand-written signature scan.

Five fundamental performance factors are used to compare these: failure to authenticate, false acceptance rate, false rejection rate, ease of use, and highly secure (difficult to forge or replicate). An ideal electronic authentication system should satisfy these five performance criteria as depicted in Fig. 4.

![](/api/attachments/3WSC3E5D/fulltext/images/b198345a08169cb1168468da3f45b500f6ccebcd75fa50119adecb91851cd27f.jpg)  
Fig. 4. An ideal electronic authentication system.

## 3.1. Traditional password

This is the simplest and oldest way of authenticating a computer system user and is the most widely used authentication technology today. It is easy to use on any system. However, it is generally viewed as a relatively low-security option, due to the frequency of forgotten or co-opted passwords. In addition, there are well-structured and effective hacking techniques for password log-ons.

## 3.2. Key cards

Traditional key cards are magnetic strip cards that store the PIN or password in the magnetic strip. The user obtains the authentication upon exposing the card under a magnetic reader and passing the verification process. In addition to very limited storage capabilities, key cards are vulnerable to damage and theft. Thus, they provide little, if any, functionality. In fact, key cards can be viewed as the equivalentofcarrying a PINor a password.

## 3.3. Smart cards

The evolution of key cards has resulted in ‘‘the smart card’’. Identical in size and feel to credit cards, smart cards store information on an integrated microprocessor chip located within the body of the card. These chips hold information, from stored (monetary) value (used for retail and vending machines), to secure information and applications (for higher-end operations such as medical/healthcare records). New information and/or applications can be added, depending on the chip capabilities. Smart cards allow thousands of times the information storable on magnetic stripe cards. In addition, smart cards are more reliable, perform multiple functions and are more secure.

## 3.4. Face recognition

Facial images are probably the most common biometric characteristic used by humans for personal identification. Facial recognition identifies an individual by analyzing the shape, pattern and positioning of facial features [18]. There are two methods used for processing the data: video and thermal imaging. Standard video techniques are based on the image captured by a video camera. Thermal imaging techniques analyze the heat-generated pattern of blood vessels under the skin. Currently, this technology suffers from lack of reliability. For example, systems have difficulty in distinguishing twins, in recognizing users after minor changes, such as a haircut, or identifying an individual when not wearing glasses, etc. [3].

## 3.5. Fingerprints

All fingerprints contain a unique physical characteristic: the discontinuities that interrupt the otherwise smooth flow of ridges. The quality of a fingerprint image is relative to the number of minutiae points captured. In a recent class study at the University of Connecticut’s edgelab (see http://www.sba.uconn.edu/ users/atung/d-sign/), student researchers found that between 24 and 70 minutia points are sampled in a current typical optical fingerprint reader. The analysis also indicated that the technology generates false acceptances at a rate between 1:1000 and 1:100,000. Also, due to its traditional association with police investigation of crimes, this technology is low in user acceptability. Together, these factors considerably impede the use of fingerprint id technology.

## 3.6. Hand geometry

Virtually every person’s hand is shaped differently and the shape (which include measurements such as lengths and width of the fingers and knuckles, etc.) does not change (after a certain age) significantly over time. One major advantage of using hand geometry is that neither the environment (e.g. humid weather) nor individual anomalies (e.g. dry skin) has significant effects on the identification accuracy. Current disadvantages, unfortunately, include both a lack of discriminative capabilities and the cumbersome size of the hand geometry-based system.

## 3.7. Retina pattern

The retina is the layer of blood vessels at the back of the eyes. Digital images of retina patterns can be acquired by directing a low-intensity beam of visual or infrared light into the eyes to capture the characteristics. An area is scanned and the unique pattern is captured. Retina biometrics is considered to be the best biometric performer. However, despite its accuracy, this technique is often considered inconvenient and intrusive and may be difficult to gain general acceptance. Eye and retinal scanner are ineffectual with the blind and those who have cataracts.

## 3.8. Iris scan

The iris is the annular region of eye. Each iris is unique and even irises of identical twins are different. An iris recognition system uses a video camera to capture the sample while the software compares the resulting data against stored templates. One advantage is that this is extremely difficult to tamper with and it is easy to detect artificial irises [17]. In fact, the falseaccept rate is purportedly (or theoretically) 1:10<sup>78</sup>. In the class study project at UCONN’s edgelab there were no false-accept. When advanced auto-calibration cameras were used, false rejects rarely occurred. Three key summary points relating to iris scan are as follows:

\- Iris scan is strategically a compelling biometric for both identification and authentication, due to rich, static nature of the patterns.

\- Iris scan is functionally viable today for physical security and may be cost-effective.

\- Desktop iris scan is still relatively immature, but has strong future potential, as next-generation cameras will have capability to provide high-compression desktop video-conferencing and facial recognition for persistence.

## 3.9. Voice

Voice-based verification (voice recognition) can be either text-dependent or independent [2]. A text-based verification authenticates the identity based on utterance of a fixed predetermined phrase. A text-independent verification verifies the identity by analyzing unique speech characteristics, such as the frequency between phonetics. While voice recognition is convenient, it is not completely reliable due to impersonation, remote access, and inaccuracy. A person with a cold or laryngitis may have problems using a system due to false rejection.

## 3.10. DNA

Structurally, DNA is a double helix. The only difference between two people is the order of their base pairs. There are so many millions of base pairs in each person’s DNA that every person has a different sequence. Using these sequences, every person could be identified solely by the sequence of their base pairs. However, each person has about three thousand million ‘‘base pairs’’ and thus the identifying task is very time-consuming. The technology is still in its infancy stage.

## 3.11. Hand-written signature scan

A hand-written signature may be authenticated automatically by analyzing the shape, speed, stroke, pen pressure, and timing information during the act of

Table 1  
A comparison of authentication technologies based on five performance factors

<table><tr><td>Performance factors technologies</td><td>Failure to authenticate</td><td>False rejection rate</td><td>False acceptance rate</td><td>Ease of use</td><td>Highly secure</td></tr><tr><td>E-signature</td><td>●●●●●</td><td>●●●●●</td><td>●●●●●</td><td>●●●●○</td><td>●●●●●</td></tr><tr><td>Key cards</td><td>●●●●○</td><td>●●●●○</td><td>●●●●○</td><td>●●●●●</td><td>●○○○</td></tr><tr><td>Traditional password</td><td>●●●●●</td><td>●●●●●</td><td>●●●●●</td><td>●●●●●</td><td>○○○○</td></tr><tr><td>Hand-written signature</td><td>●●●○○</td><td>●●●○○</td><td>●●●○○</td><td>●●●●●</td><td>●●●○○</td></tr><tr><td>Voice</td><td>○○○○</td><td>●●●○○</td><td>●●●○○</td><td>●●●○</td><td>●○○○</td></tr><tr><td>Fingerprints</td><td>●●●●○</td><td>●●●●○</td><td>●●●●○</td><td>●●●○</td><td>●●●○</td></tr><tr><td>Hand geometry</td><td>●○○○</td><td>●○○○</td><td>●○○○</td><td>●●●○</td><td>●●○○</td></tr><tr><td>Face recognition</td><td>●○○○</td><td>●○○○</td><td>●○○○</td><td>●●●○</td><td>●○○○</td></tr><tr><td>Retina pattern</td><td>●●●○</td><td>●●●○</td><td>●●●○</td><td>●●○○</td><td>●●●○</td></tr><tr><td>Iris scan</td><td>●●●○</td><td>●●●○</td><td>●●●○</td><td>●●○○</td><td>●●●○</td></tr><tr><td>DNA</td><td>●●●●</td><td>●●●●</td><td>●●●●</td><td>●●○○</td><td>●●●●</td></tr></table>

Filled circle indicates higher performance.

![](/api/attachments/3WSC3E5D/fulltext/images/f7bd17fe137f9bb8b058d42e7e5eef3942d525b130d1a318716c20b7557b77f3.jpg)  
Fig. 5. A two-dimensional comparison of authentication technologies.

signing. The primary advantage it has over other types of biometric technologies is that signatures are already accepted as a common method of identity verification.

Table 1 compares these technologies using the five performance factors. We can also compare authentication technologies using two dimensions: biometrics/ objects and behavioral/physical. Fig. 5 provides an illustration.

We view the alternative authentication technologies as add-ons to the digital signature used to enhance the authenticating power of the process. As valuable as this combination may prove to be, it is still limited to final document and signer authentication.

## 4. E-signature for document management processes: a framework (digital signature for signing documents for archival)

As one would expect, initial applications of new information technologies focus on the most straightforward and easiest. In many cases, this has been transaction processing and digital signature technology has been no exception. In a typical application, an individual either uses the public key of the receiver or his own private key to sign a document. When the document reaches the designated receiver, it can be opened and verified by using the appropriate key. Such applications are straightforward and do offer poten tially significant efficiency and cost savings.

Consider the B2B process of working on a contract. Here, multiple individuals may need to review a document, modify it, and, once a final document is achieved, sign it for archival purposes. Similarly, consider internal documents that are mandated to follow a stipulated routing with a signature required at each step. A signer at step n is approving or verifying the document before it moves forward to step n þ 1. If any changes are made at step n, all signatures at steps 1 to n  1 must be invalidated.

While digital signature technology can easily be applied to our first example, this is not the case for situations exemplified by our second example. Current digital signature technology does not adequately deal with such environments, despite the potential efficiency gains and improvements in accuracy over the current process.

Consider a generic contract management process [7,9,10,12] as used, with minor variations, in most large corporations. Fig. 6 presents an overview of this process, which depicts the internal structure of a negotiating team for only one of the two or more groups or ‘‘companies’’ involved in the negotiation.

A contract is usually built in several steps. In each step, the negotiating parties come to a tentative agreement on one or more parts or a subset of the contract. Most tentative agreements need to be ‘‘initialed’’ by the principals from both organizations. However, before the principals sign any agreement, they typically need to get approval from several members of the project team, both internal and external to the organization. Examples of external team members include lawyers and consultants, while examples of internal team members include subject matter experts, CIO, CEO, etc. Typically, each of the individuals involved in the progressive sign-offs are able to make modifications to the tentative documents or add conditions. Thus, the final document may have several changes and/or addenda. In addition, the original document is hardly ever the copy on which all modifications are made. Modifications are made on hard copies, quite often a faxed version of the original.

Several inefficiencies in this process are readily apparent. First, each copy of the tentative agreement needs to be archived as a proof of approval. Second, the additions and conditions need to be compiled and sent to all of the team members before final approval can be made. Third, the archival system for paper is inefficient and prone to errors/mishandling. Fourth, while most organizations accept faxed signatures, it is not a secure process. Finally, the time consumed by the process is needlessly extended because of the many iterations.

![](/api/attachments/3WSC3E5D/fulltext/images/5a06ddf45cd5216d23533626b7f17f2ada3453c2dffb51adff26c6380efe1fc7.jpg)  
Fig. 6. Typical contract negotiation process.

![](/api/attachments/3WSC3E5D/fulltext/images/eee419e81df29ee060ba73757fa673f3c02a9f528847277e88d539b56472e8eb.jpg)  
Fig. 7. An ideal internal contract negotiation system.

It is not difficult to see the efficiencies that an electronic process can bring. First, it can enhance the accessibility of the document. Second, the most recent copies of can be presented when a document is requested. Third, document access and modifications can be tracked. Fourth, the archival process is less prone to errors. Finally, digital signatures can be used to conduct the process in a more secure manner. Fig. 7 presents the process of an internal contract negotiation mechanism from the perspective of a member of the project team. An ODigID can facilitate efficiency in such internal processes.

When a new document needs signatures from team members, a call goes out. The document management system has to determine whether or not the document was signed before or after any modification to the document content. If an individual did not alter the document, then the signature is stored. However, if the content is changed, then the document management system has to note the changed parts, identify the owner(s)—the original author, and invalidate the signatures of those individuals (if present). The calculation of the diff, i.e. the difference between the original and modified document is critical since it identifies exactly what changes were made. All members of the team are always sent all the modifications. However, the signatures are automatically invalidated only if the content originally authored by that team member is altered. The team member can always choose to withdraw (invalidate) his or her own signatures if he or she does not agree with the modifications.

The characteristics of this system were influenced by an investigation involving the authors and a public/private partnership with General Electric. This investigation included work overseen by faculty mentors and GE managers. The investigation included repeated interaction with managers across business units, structured report outs, and formal post-mortems for detailed lessons learned.

![](/api/attachments/3WSC3E5D/fulltext/images/d717b429f9038a9afc3d2d84f067b2679b11d31c9121fc37739c28fccb323ae8.jpg)  
Fig. 8. A digital signature prototype.

## 4.1. Current status of digital signatures with respect to document management

Fig. 8 presents the conceptual diagram of a prototype document signing system we developed. The system involves an integration of digital signature technology with organizational single sign-on initiatives and a document management system.

This prototype enables the document workflow architecture depicted in Fig. 9.

The process has the following steps: (N.B.: We have combined the one-time process of registration with the certificate server from the description with the retrieval of certificate that needs to be made repeatedly only if a user needs mobile access to his/her digital signature.)

Retrieve certificate: Before starting to sign documents with a digital signature, users need to download a personal certificate from a certificate server to their PC. This can be done by submitting on-line authentication to the certificate server or by using plug-in certificate tools (e.g. RSA’s web passport). Certificate can be stored in user’s PC for future use or deleted after signing.

Obtain the document: Users can download document from any file server in use. When a user is checking out a document, other users can be prevented from obtaining that document with write access. However, many file servers write file version information to the documents, which, in turn, invalidates digital signatures.

Signing the document: User can use digital signature plug-in tools that are compatible with document creation software to sign or validate signatures on a document. For the prototype, we used E-Lock, software that acts as a Microsoft Office plug-in and is compatible with RSA products.

Submit the signed document: After signing a document, users can check document back into file server, which then lets other authorized users have complete access to it.

Locking down the document: When all individuals of the contract process have signed a document, the document can be locked down and moved to an access-controlled directory in the file server.

![](/api/attachments/3WSC3E5D/fulltext/images/a53679928022a985779b5bb53f7264bddc845db2a460cc2c2565105d1ae12b1f.jpg)  
Fig. 9. The process flow for document signing.

The server side processes are responsible for:

Identity authentication: The certificate server checks a user’s identification when the user submits login information or uses other authentication technologies (e.g. biometrics) with the help of secure ID server.

Certificate issuance and revocation: Based on successful authentication, the certificate, together with a user’s private/public key pair, is sent to the user by the certificate server automatically or by a certificate administrator manually.

Document control—check in/out, version and lock down: The file server keeps control of document access and status.

Signing process management—setting up the name list and broadcasting signature status: The signing process manager sets up the signature control list to decide who can sign what documents and broadcasts signature status to relevant people.

## 4.2. Status quo versus the requirements of digital document signing

Clearly, current technology is capable of providing signing capabilities for a finalized document. However, it is woefully inadequate in dealing with transient stages. The most serious shortcoming of the current technology is the binding of the signature to the entire document. Currently, a digital signature is invalidated if the document is altered. In fact, if a different version of software (such as Microsoft Word) is used to open a document, the document may have all its previous signatures invalidated. We propose adding partial document ownership, soft signatures, and hard signatures.

Partial document ownership involves assigning ownership of the content to an individual when that individual changes part of a document. Clearly, partial document ownership requires that a document be recognized as a collection of objects (for example, paragraphs). Soft signatures are analogous to initials: when an individual chooses to sign a document with a soft signature, the signature is not invalidated with a modification to the document. Hard signatures are the traditional digital signatures that are invalidated when the document is changed.

If all three capabilities were to be built into signing tools, an individual could sign a document in such a way that all parts were signed with a soft signature unless the individual had partial ownership of some parts and they would be given a hard signature. This process has the advantage that changes made by an individual do not invalidate his/her signature. In addition, automatic generation of differences between old and modified documents need to be completed and collated. This is not simply generating differences between the words (as in UNIX). The differences have to be generated at the contextual level (e.g. at the level of sentences or paragraphs). While document authoring software, such as Microsoft Word, provide tracking capabilities, signing tools need to implement extraction capabilities to highlight and pinpoint changes for quick review of a changed document.

Finally, the signing tools should include automatic email capabilities so that all the individuals who have signed the documents are notified either to review or re-sign (see Fig. 7) as soon as the document is changed. Alternatively, this capability can be integrated with the document management system.

The document management system (or repository) should keep track of versions and differences between the current document and all previous versions. Based on version information, the document management system must be able to deliver the differences between the current document and the one previously viewed and signed by a given person. Current off-the-shelf technologies do not support this signature process.

## 5. Managerial implications and summary

The digital signature process is being or will soon be adopted by organizations to replace traditional ways of signing documents, especially when they are transmitted over the Internet. As Sprague [16] pointed out, most organizations have a substantial set of paperwork systems that have not been fully computerized because they are based on documents rather than data records. We contend that, while digital signature technological tools exist, these tools were developed with limited business applications—final transactions—as their focus. Today large corporations are driving their employees towards paperless operations. Still, rather than redefining underlying workflow, the focus is too often on adopting technology that fluidly fits into existing workflow rather than considering how technological advances enable innovative workflow processes to enhance efficiency and effectiveness.

Digital signatures have natural applications in many business processes. This technology can move beyond playing the role of supporting organizational processes to actually enabling business processes. However, a different paradigm needs to be established. In particular, documents have to be explicitly managed as a collection of entities that can have multiple ownerships.

Our framework identifies the current capabilities and shortcomings of the digital signature process. In addition, we identify and illustrate an electronic document management process that will significantly enhance the application of digital signature technology in a wide array of business processes. Managers can play an active role in adoption and design of technology. In doing so, they can actively help to reshape and increase the effectiveness of their business processes. In this paper, we begin to demonstrate such efforts with respect to future roles for digital signatures in organizational processes by focusing on technological requirements to deliver the desired product—a secure and authentication-based automated document management and contract negotiation system.

## Acknowledgements

The concepts and ideas in this paper have been developed over the past 2 years in an attempt to adopt the leading edge technologies for everyday business processes. The authors have interacted with several high level and operational managers and digital signature software providers. The operational managers helped in shaping and refining the vision of an ideal system and helped identify the shortcomings/limitations of current technology. We are also grateful to the students at UCONN’s edgelab who went in uncharted waters studying and using cutting edge technology (RSA’s web passport) as it was being released for beta testing. We are also thankful to the GE Capital managers at edgelab for their feedback and for helping and arranging the necessary contacts and tools for this project. This work was partially supported by funding from the Treibick Electronic Commerce Initiative, Department of Operations and Information Management, School of Business, University of Connecticut.

[16] R.H. Sprague, Electronic document management: challenges and opportunities for information systems managers, MIS Quarterly 19 (1), 1995, pp. 29–49.

[18] J. Zhang, Y. Yan, M. Lades, Face recognition: eigenface, elastic matching, and neural nets, Proceedings of the IEEE 85 (9) (1997) 1423–1436.

[17] R.P. Wildes, Iris recognition: an emerging biometric technology, Proceedings of the IEEE 85 (9) (1997) 1348– 1364.

## References

[4] D. Harrison, Security issues for systems used for collecting, storing and interpreting human biological data, Journal of Commercial Biotechnology 8 (4), 2002, pp. 304– 314.

[1] American Bar Association, Digital Signature Guidelines Tutorial, Posted at ABA site: http://www.abanet.org/scitech/ ec/isc/dsg-tutorial.html, 2001.

[3] J.G. Daugman, High confidence visual recognition of persons by a test of statistical independence, IEEE Transactions on Pattern Analysis and Machine Intelligence 15 (11), 1993, pp. 1148–1161.

[5] A.K. Jain, L. Hong, S. Pankanti, Biometric identification, Communications of the ACM 43 (2), 2000, pp. 90–98.

[14] G.D. Sausser, Use of electronic signatures: past and present, Healthcare Financial Management 56 (6), 2002, pp. 72–73.

[2] J.P. Campbell Jr., Speaker recognition: a tutorial, Proceedings of the IEEE 85 (9) (1997) 1437–1463.

[12] A. Rangaswamy, G.R. Shell, Using computers to realize joint gains in negotiations: toward an electronic bargaining table, Management Science 43 (8), 1997, pp. 1147–1163.

[15] B. Schneier, Applied Cryptography: Protocols, Algorithms, and Source Code in C, second ed., Wiley, New York, 1996.

[13] S.D. Ryan, B. Bordoloi, Evaluating security threats in mainframe and client/server environments, Information and Management 32 (3), 1997, pp. 137–146.

[6] A.K. Jain, L. Hong, S. Pankanti, R. Bolle, An identityauthentication system using fingerprints, Proceedings of the IEEE 85 (9) (1997) 1365–1388.

[7] M. Jarke, M.T. Jelassi, M.F. Shakun, MEDIATOR: towards a negotiation support system, European Journal of Operational Research 31 (3), 1987, pp. 314–334.

[8] B. Jung, I. Han, S. Lee, Security threats to Internet: a Korean multi-industry investigation, Information and Management 38 (8), 2001, pp. 487–498.

[10] J.F. Nunamaker Jr., A.R. Dennis, J.S. Valacich, D.R. Vogel, Information technology for negotiating groups: generating options for mutual gain, Management Science 37 (10), 1991, pp. 1325–1346.

[11] R. Oppliger, Internet security: firewalls and beyond, Communications of the ACM 40 (5), 1997, pp. 92–102.

[9] L.H. Lim, I. Benbasat, A theoretical perspective of negotiation support systems, Journal of Management Information Systems 9 (3), 1992, pp. 27–44.

![](/api/attachments/3WSC3E5D/fulltext/images/1012ef75f940f4433a9d1ffef0b1072813bf1a26ebff9e7d941809a772db286f.jpg)

Alok Gupta is an associate professor at the Department of Information and Decision Sciences at Carlson School of Management, University of Minnesota. He received his PhD in management science and information systems from The University of Texas at Austin in 1996. His research has been published in various information systems, economics, and computer science journals such as Management Science, ISR, CACM, JMIS,

Decision Sciences, Journal of Economic Dynamics and Control, Computational Economics, Decision Support Systems, IEEE Internet Computing, International Journal of Flexible Manufacturing Systems, Information Technology Management, and Journal of Organizational Computing and Electronic Commerce. In addition, his articles have been published in several leading books in the area of economics of electronic commerce. He has received prestigious NSF CAREER award for his research in Online Auctions. He serves on the editorial boards of ISR, DSS and Brazilian Electronic Journal of Economics.

![](/api/attachments/3WSC3E5D/fulltext/images/42257faa6c579369e508ffa2fe8d8785bf0e4584380f4da170c3ee5db5f22da0.jpg)

Y. Alex Tung is an associate professor in the Department of Operations and Information Management at the University of Connecticut. He received his PhD in decision science and information systems from the University of Kentucky. His research interests are applied artificial intelligence, expert systems, and electronic commerce. His research has appeared in Management Science, Journal of Management Information Systems, Decision

Support Systems, European Journal of Operational Research, Journal of Multi-Criteria Decision Analysis, and numerous other leading journals.

![](/api/attachments/3WSC3E5D/fulltext/images/34e8a87a6d72e721cad3274c68cae02fb5fc18d4fba9db87f50f35bbec1040f4.jpg)

James R. Marsden came to UCONN in 1993 as professor and head, Department of Operations and Information Management, School of Business Administration, University of Connecticut. Dr. Marsden was part of a three-person concept development team that initiated and oversaw the development of the Connecticut Information Technology Institute and is currently serving as its executive director. He developed and implemented the Treibick Electronic

Commerce Initiative that is funded through a generous gift provided by Richard Treibick and the Treibick Family Foundation. He was a member of the edgelab development team and currently serves on the edgelab Steering Committee which selects and resources projects and oversees operations. Dr. Marsden is a two-time winner of the Chancellor’s Award for IT Excellence and a co-winner of the Team Connecticut Program Award from the Office of Economic Development. He has a lengthy research publication record in market innovation and analyses, economics of information, artificial intelligence, and production theory. His research work has appeared in Management Science, IEEE Transactions on Systems, Man and Cybernetics, American Economic Review, Journal of Economic Theory, Journal of Political Economy, Computer Integrated Manufacturing Systems, Decision Support Systems, Journal of Management Information Systems, and numerous other academic journals. Professor Marsden received his AB from the University of Illinois and his MS and PhD from Purdue University. Having completed his JD while at the University of Kentucky, Jim has been admitted to both the Kentucky and Connecticut Bar.
