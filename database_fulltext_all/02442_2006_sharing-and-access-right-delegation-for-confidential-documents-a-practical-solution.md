---
otero_id: 2442
otero_key: "2FAM83MW"
title: "Sharing and access right delegation for confidential documents: A practical solution"
authors: "S.M. Yiu; S.W. Yiu; L.K. Lee; Eric K.Y. Li; Michael C.L. Yip"
year: "2006"
journal: "Information & Management"
doi: "10.1016/j.im.2006.03.003"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Sharing and access right delegation for confidential documents: A practical solution

S.M. Yiu <sup>a,\*</sup>, S.W. Yiu <sup>b</sup>, L.K. Lee <sup>a</sup>, Eric K.Y. Li <sup>a</sup>, Michael C.L. Yip <sup>a</sup>

<sup>a</sup> Department of Computer Science, The University of Hong Kong, Pokfulam Road, Hong Kong <sup>b</sup> Hydra Limited, Wanchai, Hong Kong

Received 25 September 2003; received in revised form 29 August 2005; accepted 13 March 2006 Available online 9 May 2006

## Abstract

This paper addresses a practical problem in document management systems for which no existing solution is currently available in the market. To store confidential documents, a common approach is to keep only the encrypted version of the documents to ensure confidentiality of the contents. In real cases, documents may need to be shared by more than one person or group in a company and it is common for a manager to delegate the access rights of a documents to a delegatee. How is it possible to share encrypted documents and delegate the access rights of encrypted documents? Here, we discuss the issues related to this problem and provide a practical and easy-to-implement solution for solving the problem. It has been shown to be feasible by a prototype implementation. We also show how to extend our solution to be more scalable by taking advantage of the company’s hierarchical structure. <sup>#</sup> 2006 Elsevier B.V. All rights reserved

Keywords: Document management systems; Access right delegation; Encrypted documents; Shared documents; Public-key infrastructure

## 1. Introduction

Document management systems (e.g. [3]) are IS specially designed for handling and managing documents. In such systems, documents are usually stored in a database for ease and efficient retrieval. This kind of system helps save storage space for paper records and enhances the communication and dissemination of information. In real applications, the management of these documents is complicated. Not all documents are accessible to everyone in the company. Some are strictly confidential and security measures must be taken to protect their contents. On the other hand, sharing them is unavoidable and it is also common for a manager to delegate his or her access rights of the documents to a delegatee to help in handling them.

Consider the following scenario. In a company, let D be a confidential document that should only be accessible by some senior staff, say Bob, Mary, and John. However, John is going on a business trip and would like to delegate his access right to his delegatee Alice for handling the document. Later, when John returns, he needs to revoke Alice’s access right to D.

This problem seems to be related to access control, where one technique for handling access control is to use an access control list (ACL), which states clearly which user is allowed to access which resources (documents) together with the allowable operations (e.g. read, write, delete) in the form of a data structure (e.g. a table) [1,12,17,20]. When a user attempts to access a document, the system checks the ACL to see whether the user may be granted the access. In fact, using an ACL, the sharing, delegation, and revocation can be performed easily by adding and removing the user on the ACL. In our example, the ACL contains four entries for document D (Bob, Mary, John, and Alice). When John returns from his trip, the entry of Alice for D will be deleted. However, from the security point of view, an ACL alone does not provide a satisfactory solution. If only the plain version of a document is stored, an attacker may be able to obtain the document if they can break into the system. In fact, if the document is transmitted through any network (inside or outside the company), the attacker (possibly an insider) can easily obtain a copy of the document without accessing the database. For highly confidential documents, we therefore, need another level of security. Also, the ACL is usually maintained by the database administrator who thus has the full control and access right to all documents in the database. So, the security of the system depends on a single person, which violates the security; indeed, the principle of separation of duties should be implemented to avoid collusion.

To ensure the confidentiality of the contents of documents, one can use encryption; by only storing the encrypted version of the documents an attacker will find it difficult to read the content without knowing the decryption key. To perform encryption, one can make use of the public key infrastructure (PKI) [9,10], where each entity has a public and private key pair. The private key is to be kept secret by the user and the public key will be authenticated by a trusted certificate authority (CA). To encrypt a document for a user, say Bob, we can use his public key to encrypt the document, which can only be decrypted by Bob using his private key.

However, using encryption alone also has problems. For example, in the example, we would have to encrypt document D four times, with the public keys of Bob, Mary, John, and Alice, respectively. We have to store four different encrypted versions of the document. It is obvious that the solution is not scalable and will waste storage space. Also, when compared to symmetric key encryption and decryption in which the same key is used for encryption and decryption (e.g. data encryption standard (DES) and advanced encryption standard (AES) [15,16], public-key encryption and decryption are relatively slow and may not be appropriate for daily operations. Note also that a pure symmetric encryption approach is not appropriate, as the key distribution and management process will be complicated. Thus, a straight-forward application of encryption may not allow the sharing of documents and the delegation of access rights to be done effectively.

Here we provide a solution to the problem of storing confidential documents in a system so that sharing of the documents and delegation of access rights can be performed effectively. Existing database and software packages only provide encryption functions and allow users to store an encrypted version of the document in the database. However, ways of sharing the documents and delegating access rights are not provided. Though there are other works on delegation (e.g. [6,13,14,18,23]), they are difficult to apply as most of them focus only on the delegation of the signing right. So, it is desirable to have a practical and easy to implement solution. Of course, the study of security in an information retrieval system is not new (e.g. [8,21,22]), but previous studies did not consider the sharing of the encrypted documents and the operation of delegation.

## 2. The methodology

We investigated the problem in the following way:

1. We defined the problem by identifying the requirements. They are summarized from a number of specifications based on several real cases obtained from a computer software development company. The real cases covered a number of industries, including government and software house.

2. We investigated and reviewed existing solutions, including those in several existing document management systems. We found that none of these can satisfy all the requirements, especially the delegation of access rights for encrypted documents.

3. We designed a solution to support the sharing and delegation of authority and the ensuing workflow.

4. We implemented a prototype using servers and development tools commonly available in order to show that the prototype fit most existing IS.

5. We tested the prototype by creating 50 users (about the number of staff in a medium-sized company) and evaluated the results to show that the solution was efficient; normally, the use of encryption affects the performance of the system adversely. We compared the operations of retrieving files with and without using our encryption solution to show that our method, though slower is reasonably fast.

## 3. The requirements

We first distinguish two concepts: delegation and access right granting. If the documents are not encrypted, delegation can simply be achieved by granting access right, but for encrypted documents, the delegate (alternate) needs to have both proper access right and the decryption key.

## 3.1. Assumption

Each user has generated a public key and a private key based on PKI. The public key is stored in a certificate signed by the CA and is accessible by everyone. The private key is to be stored securely by the user (e.g. it could be stored in a smart card). Note that the CA can be an agent within the company if the system is only used within the company.

## 3.2. Requirements

The followings are the requirements, summarized from a number of requirement specifications in several development projects that cover industrial sectors (such as government and software house), for handling confidential documents.

 Security level: Each user and each document in the system is assigned a security level. In general, if the security level of a user is lower than that of the document, the user is not allowed to access the document unless the user was delegated to do so.

For simplicity, here we only assume that there are two levels of security: confidential and unclassified, for which the documents can be accessed by every user.

 Types of access rights: There are three types of access rights: read, update, and delete. The owner (creator) of the document is automatically assigned all three.

 Confidentiality: Confidential documents must be stored and transmitted in encrypted form.

 Multiple access: The same (confidential) document can be accessible by multiple users without creating multiple copies of it.<sup>1</sup>

 Types of delegation: The system should support delegation of access rights at the Global and Document level. To make sure that delegation is made in a restricted manner, for each user (the delegator), a list of pre-defined delegatees is set. Delegation can only be performed for pre-defined delegatees. Any changes in the list of pre-defined delegatees must go through a dedicated procedure. In fact, this requirement can be used to support the ‘‘acting’’ operation, which is common today.

o Global level delegation: The delegator can delegate all or selected access rights to his or her delegatees. The delegation will be applied to all documents accessible by the delegator including those to be created. However, the delegatee can only access the documents with a security level not greater than that of the delegatee. This requirement is to fit a real case scenario in which a manager usually delegates his or her secretary to handle most of the documents.

o Document level delegation: The delegatee can be granted access rights to a document even if it has a higher security level than that of the delegatee.

 Properties of delegation—transferability and revocability:

o Delegation can be transferable. For example, if Bob delegates his access rights to John, then John can further delegates his access rights to Mary.

o Delegation is revocable. The revocation will be done through the whole delegation tree. In other words, if Bob has delegated his right to John and John has further delegated his right to Mary, then when Bob revokes the delegation to John, the delegation to Mary will also be revoked.

 Access right granting: A user is allowed to assign access rights of a document to multiple users provided that the user has the access rights (not by delegation) and the other users have a higher or equal security level to that of the document.

## 4. A review of existing solutions

We considered various existing solutions that may have satisfied the requirements. We studied three document management systems [4,5,24] in detail but found that they either did not provide a strong solution or that the solutions were not flexible enough for delegation. Table 1 shows the comparison of our solution with those three (WORLDOX enterprise document manager, Edge2004 of Edge Web Link, and DigiSAFE). We compare them from the following aspects:

Document management: Whether the system provided basic document management functions.

Document security and integrity: Whether the system provided functions to ensure security and integrity of the documents stored in the system (if only access control is provided, it is not secure enough).

Reader and author authentication: Whether the system can authenticate the reader and author of the documents before they are allowed to access and work with them.

Table 1  
Comparison of our needs and three existing solutions

<table><tr><td></td><td>Our needs</td><td>WORLDOX Enterprise Document Manager (http://www.worldox.com/)</td><td>Edge2004 of Edge Web Link (http://www.edgedepot.com)</td><td>DigiSAFE (http://www.digisafe.com)</td></tr><tr><td>Document management</td><td>Y</td><td>Y</td><td>Y</td><td>Y</td></tr><tr><td>Document security and integrity</td><td>Y</td><td>Y (Only access control without encryption)</td><td>Y (Only access control without encryption)</td><td>Y</td></tr><tr><td>Reader and author authentication</td><td>Y</td><td>N</td><td>N</td><td>Y</td></tr><tr><td>Provide delegation operations</td><td>Y</td><td>N</td><td>N</td><td>N</td></tr></table>

Delegation: Delegation is a common practice, we check whether this function was provided.

## 5. Our proposed solution

Our solution combines the techniques of ACL and encryption to provide a feasible solution for solving the problem of sharing and access right delegation for confidential documents. It provides two levels of security and divides the responsibility to two parties, the database administrator (DBA) and the security officer (SO). To speed up the process, we make use of the concept of ‘‘session keys’’ such that the same document is only encrypted once, using symmetric key encryption with the session key. For those users who can access the document, we encrypt the session key using their public key. In other words, a user must have the appropriate private key to decrypt the session key and must be granted access to the document in the ACL before he or she can access the document.

Session key encryption for documents: To avoid encrypting the same document more than once, we use session keys. For each document, we generate a session key and encrypt the document using it. For each user allowed to access the document, we encrypt the session key using the public key of the user. In this case, only the user who has the corresponding private key can extract the session key in order to decrypt and read the document.

Access control table and delegation table: We make use of two tables in the database to store the ACL and delegation information. These tables control access to the documents.

Separation of duties: There are two independent entities, the DBA and the SO. The DBA has the full control and access to the access control table and delegation table but is not given the session key to any of the documents. The SO keeps the encrypted session keys for all documents but does not have an access entry in the access control and delegation tables. So, unless the two collude, neither can break the system and gain access to the unencrypted documents.

## 5.1. Details

Fig. 1 shows the system architecture. Users access the system via a web browser. Since we have to ensure that only the encrypted version of a document is transmitted over the network, the encryption and decryption are performed on the client side, which has a Java Crypto Engine. The application servers work with the database server which holds the ACT and the delegation table for authentication, authorization, and document handling. Note that there is an administrator console for the SO to perform necessary functions.

The structures of the ACT and delegation tables are shown in Fig. 2. For the ACT, if Bob has access rights to document D, then there is a record for Bob and D. For the delegation table, if Peter is a pre-defined delegatee of Bob, then there will be a record for Peter and Bob. For global level delegation, we set the Doc\_ID to a predefined value, -1, and the delegated access rights will be stored in the same record. When the system starts, records for pre-defined delegatees are created in the delegation table with all access rights set to ‘‘No’’. For document level delegation, a separate record with the related ID of the document will be created in the table after the delegation has been performed.

On the client side, when a document is created, a session key is generated by the creator through a clientside program. The document is encrypted by that session key using a symmetric key encryption algorithm. Access rights are granted to the appropriate users. The corresponding entries will be created in the ACT. For these users (including SO and all the pre-defined delegatees of these users), the session key is encrypted using their public keys. These encrypted session keys will also be stored in the database. The SO will have the encrypted versions of all session keys and no session keys will exist as plain text.

![](/api/attachments/2FAM83MW/fulltext/images/f2fba9b03a9a7995c315648073700f65f62f31b969cff4ac0d95fdfab14b60a5.jpg)  
Fig. 1. System architecture.

If a user has the corresponding access right to a document and the delegatee has a security level greater than or equal to that of the document, then the user can grant the right to the delegatee and an entry with the appropriate access right will be created in the ACT. The session key for the document is decrypted using the delegatee’s private key and the session key is encrypted by the public keys of the user and all the user’s perdefined delegatees.

The user delegates an access right of a document to a delegatee (document level delegation) by making a new entry for the delegatee and the document with the appropriate access right is created in the delegation table. The session key for the document will be encrypted using the delegatee’s public key and the public keys of all his or her pre-defined delegatees.

<table><tr><td>Field Name</td><td>Data Type</td><td>Description</td></tr><tr><td>A_ID</td><td>Number</td><td>Primary key</td></tr><tr><td>Doc_ID</td><td>Number</td><td>Document unique ID</td></tr><tr><td>User_ID</td><td>Number</td><td>User unique ID</td></tr><tr><td>read</td><td>Yes or No</td><td>Grant read access?</td></tr><tr><td>upd</td><td>Yes or No</td><td>Grant update access?</td></tr><tr><td>del</td><td>Yes or No</td><td>Grant delete access?</td></tr></table>

If a user has a pre-defined delegatee, he or she may delegate an access right globally to the delegatee (global level delegation). The entry for the user and delegatee in the delegation table will be updated. The session keys for all documents that are accessible by the user will be encrypted using the delegatee’s public key. Note that there is a trade off between the security and the efficiency of the system: the encrypted session keys of all documents accessible by the user for the delegatee may be created when the system starts.

<table><tr><td>Field Name</td><td>Data Type</td><td>Description</td></tr><tr><td>D_ID</td><td>Number</td><td>Primary key</td></tr><tr><td>Valid_from</td><td>Date</td><td>Starting date of delegation</td></tr><tr><td>Valid_to</td><td>Date</td><td>Ending date of delegation</td></tr><tr><td>Delegator_id</td><td>Number</td><td>Delegator ID</td></tr><tr><td>Delegatee_id</td><td>Number</td><td>Delegatee ID</td></tr><tr><td>read</td><td>Yes or No</td><td>Grant read access?</td></tr><tr><td>upd</td><td>Yes or No</td><td>Grant update access?</td></tr><tr><td>del</td><td>Yes or No</td><td>Grant delete access?</td></tr><tr><td>Doc_ID</td><td>Number</td><td>Document ID (for document level delegation)</td></tr></table>

Fig. 2. The access control table and the delegation table.

![](/api/attachments/2FAM83MW/fulltext/images/ed2a5c9b6afaa592290d2f2c642eb6f02e714a87c5e2fea30f97660d2abb549c.jpg)  
Fig. 3. Overview of software architecture.

To check whether the user can access a document, the system must first consult the ACT and see if there is an entry for the user and the document with the appropriate access right. Otherwise, the system can check the delegation table to see if the user has been delegated an appropriate access right to the document. If it has, the encrypted version of the document can be sent to the user. The decryption is performed on the client side so that the transmitted document is in encrypted form.

The user revokes delegated access right from the delegatee by updating the corresponding record in the delegation table. Then, for security purpose, all relevant encrypted session keys are deleted. However, for efficiency purpose, they may be retained.

Not all functions are listed and discussed here. For example, there should be functions designed for the DBA, such as updating the list of pre-defined delegatees of a user.

## 5.2. Implementation

Fig. 3 shows the software architecture of our implementation. The architecture is a standard threetier one. The Web server was Apache Group HTTP Server with SSL support by OpenSSL. The Application Server was Jakarta Tomcat Server while the Database Server is Oracle 8i Enterprise Database. Java 2 Platform, Enterprise Edition (J2EE) was used for programming the system. For communication between the clients and the servers, Java Applets were used on the client side and JavaServer Pages (JSP) were used to present the Applets to clients. Java Servlets and JavaBeans were used in the server side for business logic and interaction with the Oracle database. The Java Cryptography Extension (JCE) was used for cryptographic operations. In order to utilize the cryptographic services, Bouncy Castle, one of the service providers suggested by Sun, was used as a service provider with the standard JCE.

Our reasons for choosing these components for our prototype implementation were: these servers are used in many existing IS. Also, since we needed to work in a TCP/IP network with standard protocols and use as many non-proprietary components as possible, we used Java technologies on both the server and client side. Figs. 4 and 5 show screen shots of the prototype.

## 6. Evaluation

Although our solution can provide confidentiality to the documents while allowing delegation and sharing operations, there is a question to address about the efficiency of our solution.

In a medium-sized company, there will be a few dozen users, so we created about 50 users for testing. We then studied the speed of two common operations (uploading and downloading). Our study showed that the performance of the system was good (each operation took about 10 s). Obviously, if the delegation chain t is long, the performance degrades because the system needs to follow the chain and perform updates for each user on t. Fortunately, long delegation chains are not likely to occur, so the performance of the system is reasonable.

![](/api/attachments/2FAM83MW/fulltext/images/3c50367f79fd1ef2f82e8c7e6cf8c184e6539d818b884b65098b2250d2eb009a.jpg)  
Fig. 4. Delegation (global-level).

![](/api/attachments/2FAM83MW/fulltext/images/e1c03f970324748e55564c19f5d0e14f42153f4e5e8d1797898c38f78df9a3a8.jpg)  
Fig. 5. Delegation (document-level).

Table 2 shows the uploading time of different sized documents and different numbers of accessible users for systems both with and without our solution. Users were scheduled to upload the file randomly, so there may be cases when the uploading time is smaller even though the number of accessible users increased. But in general, the uploading time increased with the number of accessible users. Table 3 shows the downloading time of documents.

From Tables 2 and 3, the time for uploading or downloading a document is basically longer than that without encryption and digital signature. Obviously, this is due to the extra time needed for encrypting or decrypting the documents and uploading or downloading user certificates. In Figs. 6–9, one can see that the document uploading time is proportional to the number of accessible users, due to the uploading of user certificates; this time dominates that for document encryption when the number of accessible users is large. But even when it involves 50 users and a 1000 K file, the upload can be done reasonably quickly (within 10 s).

Uploading performance of our prototype compared with that without encryption and digital signature

<table><tr><td rowspan="3">No. of users</td><td colspan="8">Uploading time in milliseconds</td></tr><tr><td colspan="4">Without encryption and digital signature</td><td colspan="4">With encryption and digital signature</td></tr><tr><td>1 K file</td><td>10 K file</td><td>100 K file</td><td>1000 K file</td><td>1 K file</td><td>10 K file</td><td>100 K file</td><td>1000 K file</td></tr><tr><td>1</td><td>263</td><td>170</td><td>173</td><td>1299</td><td>357</td><td>2053</td><td>704</td><td>3605</td></tr><tr><td>2</td><td>127</td><td>94</td><td>137</td><td>1245</td><td>724</td><td>544</td><td>721</td><td>4036</td></tr><tr><td>5</td><td>160</td><td>114</td><td>157</td><td>1970</td><td>891</td><td>1683</td><td>838</td><td>4296</td></tr><tr><td>10</td><td>874</td><td>497</td><td>367</td><td>1386</td><td>1165</td><td>1018</td><td>1408</td><td>4974</td></tr><tr><td>15</td><td>588</td><td>541</td><td>234</td><td>1342</td><td>1509</td><td>1205</td><td>2160</td><td>5075</td></tr><tr><td>20</td><td>293</td><td>374</td><td>1031</td><td>2827</td><td>1586</td><td>1372</td><td>2016</td><td>6012</td></tr><tr><td>30</td><td>1005</td><td>330</td><td>344</td><td>1482</td><td>2210</td><td>3258</td><td>3078</td><td>5995</td></tr><tr><td>40</td><td>1132</td><td>1422</td><td>788</td><td>2220</td><td>2534</td><td>3021</td><td>3648</td><td>6906</td></tr><tr><td>50</td><td>881</td><td>1162</td><td>514</td><td>2170</td><td>4029</td><td>5381</td><td>3969</td><td>8909</td></tr></table>

Table 3  
Download performance of our prototype compared with that without encryption and digital signature  
Downloading time in milliseconds (excluding downloading the data from the server)

<table><tr><td colspan="4">Without encryption and digital signature</td><td colspan="4">With encryption and digital signature</td></tr><tr><td>1 K file</td><td>10 K file</td><td>100 K file</td><td>1000 K file</td><td>1 K file</td><td>10 K file</td><td>100 K file</td><td>1000 K file</td></tr><tr><td>7</td><td>7</td><td>10</td><td>90</td><td>164</td><td>120</td><td>220</td><td>1328</td></tr></table>

## 7. A more scalable solution

Fig. 10 shows an example of a company hierarchy, where each edge between two entities represents a parent–child (belong-to) relationship. A child is a member of its parent in the company. For example, staff S and staff R are both members of Team 1. An entity z is called a descendant of another entity y if, by following the belong-to relationships, one can reach z from y. In a company, a descendant of a node y is also a member of y. For instance, staff R and staff S are descendants of department A and therefore, they are members of department A. A logical unit is called a ‘‘group’’.

There is a possible scalability issue in our basic scheme. Consider an organization with two documents accessible by a department that has 1000 members. In the basic scheme, the session key of each of the documents must be encrypted 1000 times, i.e. there are 2000 encryptions in total, and the number of encrypted session keys is 2000.

![](/api/attachments/2FAM83MW/fulltext/images/cbc342bc79dbb284c47c26eac0c3c1ff0ee3b23c8e71fac3a11429fe46dcb0aa.jpg)  
Fig. 6. Uploading time for a 1K File vs. number of users.

![](/api/attachments/2FAM83MW/fulltext/images/be9e2b74d7efeae917b9765b0c936b1ec7d232b4574fda27711a5d5aa3913bd9.jpg)  
Fig. 7. Uploading time for a 10K file vs. number of users.

![](/api/attachments/2FAM83MW/fulltext/images/6e34321c2dca6ac13c648c8044a808159b98101fbfd4b1555cc0fba00de5d60f.jpg)  
Fig. 8. Uploading time for a 100K file vs. number of users.

![](/api/attachments/2FAM83MW/fulltext/images/aa0761427e2f86476c1b040547d775da2f77a54b20a402fd78219bae435abed9.jpg)  
Fig. 9. Uploading time for a 1G file vs. number of users.

![](/api/attachments/2FAM83MW/fulltext/images/bf595a7aac07e3ec2a4a34576b208f68809b06dc20d701518b44352bde18a250.jpg)  
Fig. 10. Modelling company hierarchy using virtual user concept.

We extended our basic scheme by taking advantage of the company hierarchical structure. Each group (logical unit) is regarded as a user and will be assigned a public and private key pair. Documents then can be made accessible by a group. As it is essentially a virtual user, there is no difference in document handling. However, all user members of a group should be able to access the documents at the security level of the members.

Since virtual users are not real users, they cannot store the private key, so there must be a different approach for managing the public and private key pair. Public key management may be the same as that for real users but the private key will be stored in encrypted form in the database. The private key of a group is encrypted by the public key of the Security Officer and public keys of the children; with the private key of one of the children, a user can obtain the private key of the group to decrypt documents accessible by it or obtain the private key of its parents for decrypting documents accessible by the groups in a higher layer, provided that the user has the right security level.

By default, the system will always have a virtual user representing the whole company. When the SO adds a group, it is being added as a child to one or more of the other groups in the system. Initially, the Company is the only virtual user. When a new group is added as a child, the public key certificate of the new group will be stored in the database, whilst its private key will be encrypted by the SO’s public key and stored. Thus, all groups have their private keys encrypted by the SO’s public key. At the same time, the private key of the parent is retrieved by the SO (using the SO’s private key). Then, the private key of the parent can be encrypted by the public key of the new group and stored. The addition of a new user to the system is similar to the addition of group to the system, except that the private key of the real user will not be encrypted by the SO’s public key or stored in the system.

## 8. Conclusions

We have developed and discussed a practical security related problem in document management systems. In particular, we consider how the sharing and access right delegation of encrypted documents can be performed in such systems. We showed a feasible and practical solution to solving the problem. Our solution combined the technique of access control list and session key symmetric encryption. We implemented this solution as a prototype and preliminary testing showed that the performance is quite good for a medium-sized company with about 50 users. We also showed how to take advantage of the hierarchical structure of a company and introduced the concept of virtual users to make the solution more effective. The solution provided represents a first step towards solving this security problem.

## Acknowledgements

The authors would like to sincerely thank the reviewers and the editor for very useful comments that help to greatly improve the readability and clarity of the whole paper.

## References

[1] J.F. Barkley, Comparing simple role based access control models and access control lists, in: Proceedings of the Second ACM Workshop on Role-Based Access Control, VA, USA, November 1997, pp. 127–132.

[3] E. Bertino, D. Montesi, Design and development of a document management system for banking applications: an example of office automation, in: Proceedings of the International Conference on Database and Expert Systems Applications, Vienna, Austria, 1990, pp. 500–507.

[4] DigiSAFE, http://www.digisafe.com. Accessed 18 June 2005.

[5] Edge Web Link & Edge, http://www.edgedepot.com. Accessed 18 June 2005.

[6] M. Gasser, E. McDermott, An architecture for practical delegation in a distributed system, in: Proceedings of the 1990 IEEE Symposium on Security and Privacy, CA, USA, May 1990, pp. 20–30.

[8] C.E. Koh, H.J. Watson, Data management in executive information systems, Information & Management 33(6), 1998, pp. 301– 312.

[9] S. Kelm, The PKI Page, http://www.pki-page.org/.Accessed 06 July 2004.

[10] S. Kent, T. Polk, IETF Public-Key Infrastructure Working Group Charter, URL http://www.ietf.org/html.charters/pkixcharter.html. Accessed 06 July 2004.

[12] S.-p. Li, S.-z. Wu, T. Guo, The consistency of an access control list, in: Proceedings of the 4th International Conference on Information and Communications Security, Singapore, December 2002, pp. 367–373.

[13] M. Mambo, K. Usuda, E. Okamoto, Proxy signatures: delegation of the power to sign messages, IEICE Transactions on Funda mentals of Electronics, Communications and Computer Sciences E79-A(9), 1996, pp. 1338–1354.

[14] M. Mambo, K. Usuda, E. Okamoto, Proxy signatures for delegating signing operation, in: Proceedings of the Third ACM Conference on Computer and Communications Security, New Delhi, India, March 1996, pp. 48–57.

[15] NIST, The Data Encryption Standard, http://csrc.nist.gov/pub lications/fips/fips46-3/fips46-3.pdf. Accessed 06 July 2004.

[16] NIST, The Advanced Encryption Standard, http://csrc.nist.gov publications/fips/fips197/fips-197.pdf. Accessed 06 July 2004.

[17] J. Qian, ACLA: a framework for access control list (ACL) analysis and optimization, in: Proceedings of the IFIP TC6/ TC11 International Conference on Communications and Multimedia Security Issues, Darmstadt, Germany, May 2001.

[18] C. Ruan, V. Varadharajan, A weighted graph approach to authorization delegation and conflict resolution, in: Proceedings of 9th Australasian Conference on Information Security and Privacy, Sydney, Australia, July 2004, pp. 402–413.

[20] H.G. Stiegler, A structure for access control lists, Software Practice and Experience 9(10), 1979, pp. 813–819.

[21] B. Thuraisingham, Multilevel security for information retrievel systems, Information & Management 24(2), 1993, pp. 93– 103.

[22] B. Thuraisingham, Multilevel security for information retrieval systems—II, Information & Management 28(1), 1995, pp. 49– 61.

[23] V. Varadharajan, P. Allen, S. Black, An analysis of the proxy problem in distributed systems, in: Proceedings of the IEEE

Symposium on Security and Privacy, CA, USA, May 1991, pp. 255–275.

[24] WORLDOX Enterprise Document Manager, http://www.worldox.com. Accessed 19 June 2005.

![](/api/attachments/2FAM83MW/fulltext/images/63133fd841265ba4a5781fbbaa952a9dcc5b7cca8a97938f0e332278b5bfc730.jpg)  
Dr S.M. Yiu obtained his Ph.D. in Computer Science from the University of Hong Kong and is currently a Research Assistant Professor in the Department of Computer Science of the same university. His research interests include information security, cryptography, and bioinformatics.

![](/api/attachments/2FAM83MW/fulltext/images/dc6db974b1d444de34f48de40eea2ee74c7b45392e181372cbbd5792ba0c0193.jpg)

Dr S.W. Yiu obtained his Ph.D. from the University of California at Berkeley. Dr. Yiu is currently the Principal Consultant of Hydra Limited who has extensive experi ence in designing and implementing cryp tographic applications, performing IT security review and risk assessment. His research interests include cryptography and information security.

![](/api/attachments/2FAM83MW/fulltext/images/74cc15e29bfb52af06177ea9bc2513ba3fbf53f72e3181b24184d1a82507ca11.jpg)

Lee, Lap Kei is currently a Ph.D. research student in the Department of Computer Science at the University of Hong Kong. His research interest is design and analysis of algorithms.

![](/api/attachments/2FAM83MW/fulltext/images/5be1720c8a1b1191c14c00d2da2381754380b6ad6b4bf1b5199211d2d4e73e82.jpg)

Li, Kwun Yan Eric got his Bachelor of Computer Engineering degree from the University of Hong Kong in 2004. He is currently an IT Officer in Hang Seng Bank (member of HSBC Group), specializing in Treasury Trading systems and applications development.

![](/api/attachments/2FAM83MW/fulltext/images/61c71bc74a09d063d7d1a2be466a1114efe8c7f8704a4118bf8d112f0d87fac9.jpg)

Yip, Chi Lap obtained his Bachelor of Computer Engineering degree from the University of Hong Kong and is currently a Marketing Service Executive in a local trading company, utilizing his technical knowledge and experience in providing consultancy and service in product devel opment.
