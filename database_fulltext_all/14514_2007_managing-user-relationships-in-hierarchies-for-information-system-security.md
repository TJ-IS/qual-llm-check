---
otero_id: 14514
otero_key: "BKYW2DCX"
title: "Managing user relationships in hierarchies for information system security"
authors: "Mark Vroblefski; Andrew Chen; Benjamin Shao; Matthew Swinarski"
year: "2007"
journal: "Decision Support Systems"
doi: "10.1016/j.dss.2006.11.010"
query: "construct"
source: "https://ais.kexu.win"
images_downloaded: false
---
www.elsevier.com/locate/dss

# Managing user relationships in hierarchies for information system security

Mark Vroblefski <sup>a</sup>, Andrew Chen <sup>b</sup>, Benjamin Shao <sup>c,⁎</sup>, Matthew Swinarski <sup>d</sup>

<sup>a</sup> Department of Management Information Systems, Eller College of Management, University of Arizona, Tucson, AZ 85721, United States <sup>b</sup> Accounting and Information Systems, School of Business, University of Kansas, Lawrence, KS 66045, United States <sup>c</sup> Department of Information Systems, W. P. Carey School of Business, Arizona State University, Tempe, AZ 85287, United States <sup>d</sup> Department of Management Information Systems, School of Business, Penn State University, Erie, PA 16563, United States

Received 30 June 2005; received in revised form 6 June 2006; accepted 1 November 2006 Available online 22 December 2006

## Abstract

Hierarchies are an important concept in information protection systems. The uses of hierarchies in the security domain of computer information systems include access hierarchies, levels of abstraction in security kernels, multi-level security, and user hierarchies, among others. Using user hierarchies as an example, this paper proposes a new protection mechanism to achieve the key-to-key (KTK) security policy wherein each user in the hierarchy is assigned a key pair and the relationship between any two users can be revealed through an operation on their corresponding keys. In addition to the security provided by the policy, the new mechanism manifests several advantages over the previous methods in the literature. Among its merits are (1) simple and quick operations performed to determine user relationships, (2) less storage requirements, and (3) a high degree of dynamism that allows easy addition and deletion of user keys without affecting most of the existing keys in the user hierarchy. The relevance of the new KTK scheme to organizations and its implications for potential business applications are also discussed. © 2006 Elsevier B.V. All rights reserved.

Keywords: Security; Protection; Hierarchies; User relationships; Key-to-key scheme; Number theory; Decision support

## 1. Introduction

Hierarchies are figurative representations of subjects arranged in a top-down network order. Such a concept has been utilized in a variety of aspects in the security domain of computer information systems for quite some time. The first instance is access hierarchies that automatically give privileged subjects a superset of the rights over less privileged subjects [9]. For example, a protection ring for implementing a linear hierarchy of access privileges and a hierarchical tree of directories were proposed for the MULTICS operating system [19,21]. A subject tree hierarchy was presented by Graham and Denning [12], and the access-controller hierarchy of the accessor-list system was introduced in [20].

Hierarchies have also been used in verifiable systems to decompose a security kernel into a linear hierarchy of abstract processes [10]. The system is verified one level at a time, assuming that all lower levels are correctly verified. Oftentimes security levels are organized into a linearly hierarchical order in the multi-level security that prevents downward information flow from a high security level to a low security level [11]. In addition,

Shao et al. [22], Tsai and Chang [23], and Yeh et al. [25] have incorporated cryptographic techniques into user hierarchies to achieve access control among users without the intervention of operating systems. Chang et al. [5] defined a mechanism for the partial ordered user hierarchy that creates an interpolating polynomial for each user based on the user's ID and the ID of his immediate predecessor.

In the above hierarchies, nodes may represent different identities such as access privileges, directories, processes, security levels, and users. Practical examples of such hierarchies in the context of information systems for managing IT resources are numerous. One example is hierarchical key control where a hierarchy of key distribution centers (KDCs) can be established so that each local KDC is responsible for a specific domain, such as a single LAN or a single building, of a large network. For communication among users within the same local domain, the local KDC is responsible for key distribution. If a user in a supervisor domain needs to access information belonging to another user in a subordinate domain, then a global KDC first has to confirm the relationship between the two users and then provide a key that allows the supervisor access to the subordinate's information. Another example is the hierarchy of ranks, such as the one that categorizes information sensitivity into unclassified, confidential, secret, and top secret and the one used in the computer information systems that separates the activities into hardware, security kernel, operating system tasks, and user tasks.

Aside from the many interpretations associated with the nodes, one prerequisite for the hierarchies is to confirm whether a particular arc exists between two nodes before the protection system can proceed to carry out other critical tasks, such as the change of access rights, retrieval of files under a directory, the decryption of encrypted files belonging to subordinates, etc. Several mechanisms have been proposed in the literature to represent the structure of a hierarchy [3,6,24]. Using user hierarchies as an example, this paper presents a new and effective mechanism based on number theory to achieve the security policy that assigns a key pair to each user so as to easily determine the relationship between two users through a predefined operation. Compared with the previous schemes, the new mechanism possesses several virtues. Among those merits are (1) simple and quick operations performed to determine user relationships, (2) less storage requirements, and (3) a high degree of dynamism that allows easy addition and deletion of user keys without affecting most of the existing keys in the user hierarchy.

An example of a highly dynamic, flexible structure is a virtual organization. A virtual organization is a union of companies that gather to share their expertise for a variety of projects [16]. Employees of the various companies may temporarily work on multiple projects at various times needing access to different information. A flexible access control system is required to provide the proper information to the employees involved at the right time. Cheng [8] discusses the importance of dynamic access control in the context of e-commerce.

The remainder of the paper is organized as follows. Section 2 introduces two concepts related to user hierarchies, i.e., the H matrix and the key-to-key (KTK) security policy. It also briefly reviews the major KTK methods in the literature. Based on the Fundamental Theorem of Arithmetic in number theory, Section 3 proposes a new KTK mechanism and demonstrates its effectiveness with examples. Section 4 discusses practical issues associated with the application of the KTK mechanism and presents a solution called key vectorization. Section 5 discusses performance issues and compares the key vectorization approach with other KTK methods. Section 6 explicates the practical relevance of the new KTK scheme to organizations; its practical implications to possible business applications are also presented. Finally, Section 7 concludes the paper by suggesting some topics for future research.

## 2. Foundations and literature review

## 2.1. Basic concepts

A user hierarchy is defined as a network structure of users arranged in the order of their authority positions in the organization. Fig. 1 shows a simple example of a user hierarchy with five users. An arc between two users indicates that one is the supervisor (or father, in the graph terminology) of the other. An information protection system should be able to store, verify, and guard such a user hierarchy with rigorous discipline. For instance, the protection system should grant the request of user 4 to read a file of user 3, since user 4 is superior to user 3. On the other hand, the system should deny a similar request from user 1 because user 1 is a sibling of user 3 and does not possess such access rights. In effect, the confirmation of the arcs (and hence the relationships) between users in the hierarchy will help determine the appropriateness of any further tasks performed by the protection system.

To represent such a user hierarchy in the protection system, a matrix like Fig. 2 can be used. The relationship matrix R has both rows and columns representing each user, and an entry $r _ { i j }$ represents the relationship between user i and user j. For instance, the protection system can easily determine that user 2 is “father of” user 5 because $r _ { 2 5 } = 3$ (the relationship code for “father of”). A formal definition of the relationship matrix R can be given as follows.

![](/api/attachments/BKYW2DCX/fulltext/images/5566d3d4238b07ba82e1e4a8d9b10c750c8ecab1349cec4d73e6898cc04b293b.jpg)  
Fig. 1. An example of user hierarchy.

Definition 1. Let $U { = \{ i | \mathrm { i } { = } 1 , 2 , . . . , n \} }$ be the set of users and $\mathfrak { R } { = } \{ r _ { t } | t { = } 1 , 2 , { . . . , } \nu \}$ be the set of user relationships, where n is the total number of users and v is the total number of user relationships in the protection system. Let the determination function F be a function from U × U to Ω(ℜ), where Ω(ℜ) denotes all possible subsets of ℜ. Then the matrix $R = ( U , ~ U , ~ F )$ is called the relationship matrix.

A close inspection of Fig. 2, however, reveals that the relationship matrix R is symmetric in nature thanks to the complementary relationships in pairs (i.e., father vs. son, brother vs. brother, and grandfather vs. grandson). By saying user 1 is “son of” user 4, we know immediately that user 4 is “father of” user 1. The implication of this observation is that the diagonal and upper triangular elements of the R matrix are unnecessary; the lower triangular elements alone are sufficient to represent the user hierarchy. The abridged matrix is called the H matrix, as shown in Fig. 3. In the H matrix, if the relationship $h _ { i j }$ of user i to user j is “grandfather of”, then it is equivalent to saying that user j is “grandson of” user i.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td>-</td><td>4</td><td>1</td><td>2</td><td>0</td></tr><tr><td>2</td><td>5</td><td>-</td><td>5</td><td>3</td><td>3</td></tr><tr><td>3</td><td>1</td><td>4</td><td>-</td><td>2</td><td>0</td></tr><tr><td>4</td><td>3</td><td>2</td><td>3</td><td>-</td><td>1</td></tr><tr><td>5</td><td>0</td><td>2</td><td>0</td><td>1</td><td>-</td></tr></table>

Fig. 2. The relationship matrix R.

<table><tr><td></td><td>1</td><td>2</td><td>3</td><td>4</td><td>5</td></tr><tr><td>1</td><td></td><td></td><td></td><td></td><td></td></tr><tr><td>2</td><td>5</td><td></td><td></td><td></td><td></td></tr><tr><td>3</td><td>1</td><td>4</td><td></td><td></td><td></td></tr><tr><td>4</td><td>3</td><td>2</td><td>3</td><td></td><td></td></tr><tr><td>5</td><td>0</td><td>2</td><td>0</td><td>1</td><td></td></tr></table>

Fig. 3. The abridged H matrix.

While easy to comprehend, the H matrix has several shortcomings for implementation. First, because the size of the matrix goes up as the square of the number of users, the H matrix becomes inefficient when there are many users to be represented in the hierarchy; this issue is even more significant when the H matrix is sparse (i.e., when no relation exists among most of the users). Second, storing the H matrix in the memory without any kind of protection is in conflict with the security requirement. Third, the H matrix needs to be transformed into a modified matrix before it can be stored and retrieved in the memory; such a transformation incurs extra overhead costs for storing and maintaining the H matrix.

To cope with the above shortcomings associated with the H matrix, Wu and Hwang [24] proposed the key-tokey (KTK) security policy: each user in the hierarchy is assigned a vector key and the relationship between any two users is obtained through a pre-defined operation on their corresponding vector keys. This KTK security policy overcomes the first shortcoming of the H matrix because the number of user vector keys is in linear proportion to the number of users. Further, because user keys are constructed, stored, and protected by the system, it enhances the security by preventing the direct storage of the H matrix in the memory. Finally, if designed carefully, the KTK schemes can have faster operations to reveal the user relationships, in comparison with the transformation of the H matrix.

## 2.2. Previous KTK schemes

Several schemes have been proposed in the literature to implement the KTK security policy. The major ones are briefly reviewed and their potential drawbacks are also discussed. The first KTK scheme was proposed by

Wu and Hwang [24]. Their KTK scheme first assigns arbitrary values to the upper triangular and diagonal elements of the H matrix, so that any upper-left square submatrix is non-singular. Then the vector keys of users are constructed by solving sets of linear equations in Galois field $G F ( t )$ where t is the smallest prime greater than any element of the H matrix. Finally, the relationship between user i and user j is calculated through their corresponding vector keys $K _ { i }$ and $K _ { j }$ as $F ( K _ { i } , \ K _ { j } ) =$ $K _ { i } ^ { * } K _ { j } { = } h _ { i j } ,$ where $i { > } j$ and \* denotes the inner product in $G F ( t )$ . In addition to the additional efforts required to determine the non-singular submatrices, one significant drawback of their KTK scheme is that the number of elements in each vector key is equal to the number of users in the hierarchy. As a result, the addition and deletion of a user in the hierarchy require the recomputation of all the vector keys. In other words, their KTK scheme lacks any dynamism. Also, their KTK scheme requires more space than the original H matrix.

Chang and Jiang [6] proposed a binary coding method, called direct key assignment, which incorporates a breadth-first search to generate binary numbers as keys corresponding to the location of the user in the hierarchic tree. Though the binary operations to reveal user relationships are faster, two issues surface in their KTK scheme. First, the binary KTK scheme can only accommodate the special case of tree-like hierarchies; it cannot handle the general case of partially ordered sets. Second, the number of bits in a user key is equal to the number of users in the hierarchy, so the addition and deletion of a user will affect other existing keys (except when the added/deleted user is at the lowest level of the tree hierarchy).

Chang et al. [3] then tried to improve Wu and Hwang's KTK scheme [24] by first transforming the H matrix into a $T _ { r k }$ matrix, where the number of rows r is a fixed number equal to the maximum entry $h _ { \mathrm { m a x } }$ in the H matrix and the number of columns k is dependent on the size of the H matrix and increases by one when the original H matrix grows by r. For every column of the $T _ { r k }$ matrix, a column key is computed as $K _ { j } ^ { \prime } = \alpha \stackrel { ( j - 1 ) } { , } , j = 1 , . . . , k$ with $\alpha { = } h _ { \mathrm { m a x } } { + } 1$ . For every row of the $T _ { r k }$ matrix, a row key is computed as $\begin{array} { r } { K _ { i } = \sum _ { s = 1 } ^ { k } t _ { i s } K _ { s } ^ { \prime } , i = 1 , . . . , r . } \end{array}$ To determine the relationship between two users, the original locations of the relationship in the H matrix are first transformed into the corresponding locations in the $T _ { r k }$ matrix. Let the transformed locations be i and j. Then the relationship $\begin{array} { r } { T _ { i j } = \left[ \frac { K _ { i } \mathrm { ~ m o d ~ } K _ { j + 1 } ^ { \prime } } { K _ { j } ^ { \prime } } \right] \mathrm { ~ i f ~ } j < k \mathrm { ~ o r ~ } \left[ \frac { K _ { i } } { K _ { j } ^ { \prime } } \right] \mathrm { ~ i f ~ } j = k } \end{array}$ . The merit of this improved KTK scheme is that the number of keys $( = r + k )$ is smaller than the number of entries in the original H matrix, so it requires less space than Wu and

Hwang's method [24]. However, the addition of a new user will affect the existing row keys $K _ { i }$ if the new $t _ { i k }$ in $k _ { i } = \sum _ { s = 1 } ^ { k } t _ { i s } K _ { s } ^ { \prime }$ is greater than zero, or if one or more new column keys $K _ { k } ^ { \prime }$ must be added. Besides, the transformation of the indices from the H matrix to the $T _ { r k }$ matrix requires extra computation efforts.

Chang et al. [4] proposed another binary coding method. Each relationship is assigned a binary value $h _ { i j }$ of b bits. Each binary digit of $h _ { i j }$ is represented by $h _ { i j } ^ { ( x ) } ,$ $x = 1 , 2 , \hdots b$ . The number of possible relationships is less than $2 ^ { b }$ . Each user is assigned a distinct prime $K _ { i }$ as the key. Each user also has a lock vector $L _ { i }$ with b values, $( L _ { i ( b ) } , L _ { i ( b - 1 ) } , . . . , L _ { i ( 1 ) } )$ , where $L _ { i ( x ) } = \Pi _ { i = 1 } ^ { \ ' m } ~ ( K _ { j } ) ^ { h _ { i j } ^ { ( x ) } }$ , for $x = 1 , 2 , . . . , b$ and $i = 1 , 2 , . . . , m$ . In order to decide the relationship between users i and j, b divisions are required to find $h _ { i j } ^ { ( x ) } , x { = } 1 , 2 , \ldots b .$ . In adding or removing a user, this method only requires a recalculation of the lock vectors of the users who are involved (or users that have relationships with the user added or deleted). The drawbacks of their method, however, include (1) the extensive computation efforts involved in recalculating the lock vector when changing a relationship or when a user is added or removed and (2) the overflow problem that is more problematic. If a relationship is changed, many and perhaps all of the values in a lock vector need to be updated.

Chang et al. [7] employed a combination of Morton number theory and prime factorization in their proposed KTK method. The security manager chooses four prime numbers $q _ { t } , \ t = 1 , \ 2 , \ 3 , \ 4 .$ . The relationship matrix is mapped to the Morton sequence in a square matrix, and h<sub>z</sub> represents the relationship $h _ { i j }$ at Morton sequence z. For each $2 \times 2$ Morton matrix, an encrypted compound privilege (ECP) is calculated as $\mathrm { E C P } _ { s } = \Pi _ { z = 4 ( s - 1 ) } ^ { z + 3 } q _ { t } ^ { h _ { z } }$ where t=1, 2, 3, 4 and $s = 1 , 2 , . . . , m .$ . A user relationship can be found by a finite number of divisions. The drawback of this method is that when a user x + 1 is added or removed, the ECP values for s=1 to $x / 2$ must be recomputed.

## 3. The new KTK scheme

The Fundamental Theorem of Arithmetic in number theory states that every positive integer greater than one can be factored uniquely into a product of primes. The uniqueness of the factorization was first noticed by Euclid, but Gauss was the first to prove the theorem [17]. Based on the Fundamental Theorem of Arithmetic, we propose our KTK scheme as follows.

Theorem 1. Given any H matrix where there are n users and the element $h _ { i j }$ represents the relationship of user i to user j $( i > j ) ,$ , a distinct prime key $P _ { i }$ is assigned to each user $i ( i \geq 2 ) ,$ , and a user key for user j $( I \leq j \leq n ^ { - }$ 1) is computed as $\begin{array} { r } { K _ { j } = \prod _ { i = j + 1 } ^ { n } P _ { i } ^ { \bar { h } _ { i j } } } \end{array}$ . The prime key–user key pair $( P _ { i } , K _ { j } )$ uniquely determines the relationship $h _ { i j }$ of user i to user j.

Proof. Assume the prime key–user key pair $( P _ { i } , K _ { j } )$ cannot uniquely determine the relationship $h _ { i j }$ of user i to user j. That is, the user key $K _ { j }$ can be represented as a product of prime keys in two ways, say $K _ { j } { = } W _ { 1 } W _ { 2 }$ $W _ { r } { = } Q _ { 1 } Q _ { 2 } \cdots Q _ { s }$ where $W _ { i }$ and $\mathcal { Q } _ { j }$ are all primes, written in increasing order so that $\dot { W } _ { 1 } \leq W _ { 2 } \leq . . . \leq W _ { r }$ and $\mathcal { Q } _ { 1 } \leq Q _ { 2 } \leq . . . \leq Q _ { s }$ . Since $W _ { 1 } | Q _ { 1 } Q _ { 2 } \cdots Q _ { s } ,$ we know $W _ { 1 } = Q _ { k }$ for some k, implying $W _ { 1 } \geq Q _ { 1 }$ . Similar reasoning gives $Q _ { 1 } \geq W _ { 1 }$ , hence $W _ { 1 } = Q _ { 1 }$ . We may cancel this common factor and obtain ${ \it W } _ { 2 } { \it W } _ { 3 } \cdots { \it W } _ { r } = Q _ { 2 } Q _ { 3 } \cdots Q _ { s }$ Repeat the process to get $W _ { 2 } { = } Q _ { 2 }$ and cancel this common factor. If the inequality $r { < } s$ held, we would eventually come to $1 = { \cal Q } _ { r + 1 } { \cal Q } _ { r + 2 } \cdots { \cal Q } _ { s } ,$ which is contradictory because each $Q _ { j } { > } 1$ . Hence $r { = } s ,$ , and $W _ { 1 } = Q _ { 1 } , W _ { 2 } = Q _ { 2 } , . . . , W _ { r } = Q ,$ , making the two factorizations of $K _ { j }$ identical. Consequently, the key pair $( P _ { i } , K _ { j } )$ can uniquely determine the relationship $h _ { i j } ,$ which is equal to the number of occurrence of $P _ { i }$ in factoring $K _ { j } .$ □

Next, we propose the determination function $F$ to compute the relationship $h _ { i j }$ of user i to user j. For $i { > } j ,$

$$
\begin{array}{l} h _ {i j} = F (P _ {i}, K _ {j}) \\ = \left\{ \begin{array}{l l} F (P _ {i}, K _ {j} / P _ {i}) + 1, & \text { if } K _ {j} \bmod P _ {i} = 0 \\ 0, & \text { if } K _ {j} \bmod P _ {i} \neq 0 \end{array} \right. \end{array}\tag{1}
$$

For $i { < } j ,$ we first compute the relationship of $h _ { j i }$ and then reverse it to obtain $h _ { i j } .$ For $i { = } j , h _ { i i } { = } ^ {  } \mathrm { s e l f . } ^ { \cdot \cdot }$ It is noted that the KTK scheme performs a certain number of divisions to obtain $h _ { i j } ,$ , and that number is bounded by a constant equal to the maximum of $h _ { i j } .$ . The effectiveness of the KTK scheme is now demonstrated using an example.

Example 1. The application of the new KTK scheme to the user hierarchy in Fig. 1 (and the H matrix of Fig. 3) proceeds as follows. First, it assigns distinct prime keys to user i (i ≥ 2): $P _ { 2 } { = } 2 , P _ { 3 } { = } 3 , P _ { 4 } { = } 5 , P _ { 5 } { = } 7$ . Then, a user key is calculated for each user j $( 1 \leq j \leq 4 )$ $K _ { 1 } = 2 ^ { 5 } \dot { 3 } ^ { 1 } 5 ^ { 3 } 7 ^ { 0 } = 1 2 , 0 0 0$ $K _ { 2 } = 3 ^ { 4 } 5 ^ { 2 } 7 ^ { 2 } = \bar { 9 } 9 , 2 2 5$ $K _ { 3 } =$ $5 ^ { 3 } 7 ^ { 0 } = 1 2 5 , K _ { 4 } = 7 ^ { 1 } = 7$ . Now suppose the protection system wants to verify the relationship $h _ { 4 2 }$ of user 4 to user 2. Because 4 N 2, $h _ { 4 2 } = F ( P _ { 4 } , K _ { 2 } ) = F ( 5 , 9 9 2 2 5 ) =$ $F ( 5 , ~ 1 9 8 4 5 ) + 1 = F ( 5 , ~ 3 9 6 9 ) + 2 = 0 + 2 = 2$ , which equals the code for “son $\mathrm { o f . } ^ { \mathrm { , s } }$ User 4 is therefore found to be “son of” user 2. If the system needs to check the relationship $h _ { 1 2 }$ of user 1 to user 2, then since $1 < 2 .$ , it first computes $h _ { 2 1 } = F ( P _ { 2 } , K _ { 1 } ) = F ( 2 , 1 2 , 0 0 0 ) = F ( 2$ $6 0 0 0 ) + 1 = F ( 2$ , 3000)+2= F(2, 1500)+3=F(2, 750)+ $4 { = } F ( 2 , 3 7 5 ) + 5 { = } 0 + 5 { = } 5$ , a value equal to the code for “grandfather of.” The system can infer user 1 as “grandson $\mathrm { o f ^ { \circ } }$ user 2 because user 2 is found to be “grandfather $\mathrm { o f } ^ { \mathfrak { s } }$ user 1. Finally, $h _ { 5 1 } = F ( P _ { 5 } , K _ { 1 } ) = F ( 7$ 12000) = 0, which is the code for “no relation.” The KTK scheme reveals that user 5 is “unrelated $\mathrm { t o } ^ { \dag }$ user 1. □

To add a new user $n + 1$ into the hierarchy, the KTK scheme will do two things to accomplish this task. First, it assigns a distinct prime key $P _ { n + 1 }$ to the new user $n + 1$ Second, for the new entries $h _ { ( n + 1 ) j } { > } 0 \ ( j { = } 1 , . . . , n ) .$ , it recomputes the user keys through $\tilde { K } _ { j } ^ { \prime } { = } K _ { j } \left( P _ { n + 1 } \right) ^ { h ( n + 1 ) j }$ . It is noted if $h _ { ( n + 1 ) j } { = } 0 , K _ { j } ^ { \prime } { = } K _ { j } ( P _ { n + 1 } ) ^ { h ( { \bar { n } } + 1 ) j } { = } K _ { j } \left( P _ { n + 1 } \right) ^ { 0 } { = } K _ { j } .$ As such, only the keys for those users who are related to the new user need to be recomputed. The keys for the unrelated users would remain the same and need not be recomputed. This characteristic of the new KTK scheme is noteworthy because most of the time the added user is related to only a few existing users in the hierarchy and only their user keys need to be recomputed.

By the same token, to delete an existing user t from the hierarchy, the KTK scheme will recompute only the keys of the related users through $K _ { j } ^ { \prime } { = } K _ { j } \dot { ( } P _ { t } ) ^ { - } { } ^ { F ( } P \dot { t , } ~ K j { ) }$ where $F ( P _ { t } , K _ { j } ) { > } 0$ . Then the prime key $P _ { t }$ is reserved for future users. All the other keys for unrelated users are unaffected by the deleted user.

Example 2. Suppose a new user 6 is added to the hierarchy of Fig. 1 as a son of user 2, as shown in Fig. 4. A distinct prime key 11 is assigned as $P _ { 6 } .$ . Since $h _ { 6 1 } = 0$ $h _ { 6 2 } { = } 2 , h _ { 6 3 } { = } 0 , h _ { 6 4 } { = } 1 , h _ { 6 5 } { = } 1$ , the keys for users 1 and 3 are not affected. Only the keys for users 2, 4 and 5 need to be recomputed as $K _ { 2 } ^ { \prime } = K _ { 2 } ( 1 1 ) ^ { 2 } = ( 9 9 2 2 5 ) ( 1 2 1 ) =$ 12006225, $K _ { 4 } ^ { \prime } { = } K _ { 4 } ( 1 1 ) ^ { 1 } { = } ( 7 ) ( 1 1 ) { = } 7 7 , K _ { 5 } ^ { \prime } { = } ( 1 1 ) ^ { 1 } { = } 1 1$ Next, suppose an existing user 5 is deleted from the hierarchy of Fig. 1, as shown in Fig. 5. Since F $( P _ { 5 } , K _ { 1 } ) = 0 , F ( P _ { 5 } , K _ { 2 } ) = 2 , F ( P _ { 5 } , K _ { 3 } ) = 0 , F ( P _ { 5 } , K _ { 4 } ) = 1$ again the keys for users 1 and 3 are not affected. Only the keys for users 2 and 4 need to be recomputed as $K _ { 2 } ^ { \prime } { = } K _ { 2 } ( 7 ) ^ { - 2 } { = } 9 9 , 2 2 5 / 4 9 { = } 2 0 2 5$ and as $K _ { 4 } ^ { \prime } { = } K _ { 4 } ( 7 ) ^ { - 1 } { = } 7 / 7 { = } 1$ □

![](/api/attachments/BKYW2DCX/fulltext/images/a38357a962cb7cac6d9b1e649fdda592600e2f8b2f43a91a5d0f9f9abccd7c1a.jpg)  
Fig. 4. Addition of user 6 into the hierarchy.

![](/api/attachments/BKYW2DCX/fulltext/images/8a93558b2be8b52718cecc367b614aa870ce0cea11785a0e1dee1d3e440c1740.jpg)  
Fig. 5. Deletion of user 5 from the hierarchy.

## 4. Practical issues

Each user j in the hierarchy is assigned a key pair $( P _ { j } ,$ $K _ { j } )$ , where $P _ { j }$ is a prime number and $K _ { j }$ is calculated as a product of prime powers. In a programming language like Java, a long integer uses 64 bits (or 8 bytes) to store its value. Based on the Prime Number Theorem [17], the number of primes allowed in this case is equal to $\begin{array} { r } { \pi \big ( 2 ^ { 6 4 } \big ) = \frac { \dot { 2 } ^ { 6 4 } } { \ln { ( 2 ^ { 6 4 } ) } } \approx 4 . 1 6 \times 1 0 ^ { 1 7 } } \end{array}$ . This number is more than enough for practical use and, therefore, there is no issue regarding the availability of distinct prime keys $P _ { j }$ for users.

On the other hand, the user key $K _ { j }$ is calculated as a product of prime powers. Although a signed long integer with a 64-bit word can hold a number as large as 9,223,372,036,854,775,807, $K _ { j }$ is still likely to surpass this maximum and hence causes an overflow error. The major concern here is associated with the power of a prime that increases the user key $K _ { j }$ exponentially. Fortunately, this potential overflow issue is not as significant as it used to be. Many object-oriented programming languages now provide arbitrary precision arithmetic classes (called BigInteger in Java's case)

which can handle integers with an arbitrarily long sequence of digits. Another solution to cope with this potential overflow issue is to decompose user keys $K _ { j }$ into their X-based representations [14]. In this paper, a different solution called key vectorization is proposed to alleviate this potential overflow issue by reducing the powers of primes to one when constructing the user keys $K _ { j }$

For an H matrix with n users, suppose the greatest element of $h _ { i j }$ is equal to r. Then for user j, define the set $S _ { t } = \{ i | h _ { i j } = t$ and $i = j + 1 , . . . , n \} , 1 \leq t \leq r .$ Key vectorization will construct the user key $K _ { j }$ as a vector of r-tuple $( K _ { j 1 } , K _ { j 2 } , . . . , K _ { j r } )$ , where

$$
K _ {j t} = \left\{ \begin{array}{l l} \prod_ {i \in S _ {t}} P _ {i}, & \text { if } S _ {t} \neq \varnothing \\ 0, & \text { if } S _ {t} = \varnothing \end{array} \right. 1 \leq t \leq r.\tag{2}
$$

Next, the determination function F to compute the relationship $h _ { i j }$ of user i to user j with key vectorization is revised as follows. For $i { > } j ,$

$$
\begin{array}{l} h _ {i j} = F (P _ {i}, K _ {j t}) \\ \qquad = \left\{ \begin{array}{l l} t, & \text { if } K _ {j t} \bmod P _ {i} = 0 \\ 0, & \text { if } K _ {j t} \bmod P _ {i} \neq 0 \end{array} \right. 1 \leq t \leq r. \end{array}\tag{3}
$$

For $i { < } j ,$ we first compute the relationship of $h _ { j i }$ and then reverse it to obtain $h _ { i j } .$ . For $i { = } j , h _ { i i } { = } ^ { \ast } \mathrm { s e l f . } ^ { \ast }$ Again, the effectiveness of the revised KTK scheme with key vectorization is demonstrated using an example.

Example 3. For user 2 in Fig. 3, $S _ { 1 } = \emptyset , S _ { 2 } = \{ 4 , 5 \}$ $S _ { 3 } = \bigcirc , S _ { 4 } = \{ 3 \} , S _ { 5 } = \emptyset$ . According to Eq. (2), the user key $K _ { 2 }$ is constructed as a 5-tuple vector: $K _ { 2 1 } = 0 ,$ $K _ { 2 2 } = P _ { 4 } P _ { 5 } = ( 5 ) ( 7 ) = 3 5 , K _ { 2 3 } = 0 , K _ { 2 4 } = P _ { 3 } = 3 , K _ { 2 5 } = 0$ Note that the original key $K _ { 2 }$ of 99,925 in Example 1 is now represented as (0, 35, 0, 3, 0) with a greatest element equal to 35 only. The user key vectors for all of the five users are shown in Fig. 6. Suppose the protection system needs to check whether user 5 is “son of” user 2, i.e., $h _ { 5 2 } { = } 2$ . The determination function $F ( P _ { 5 } , \ K _ { 2 2 } ) = F ( 7 , \ 3 5 ) = 2$ (because 35 mod 7 = 0), confirming user 5 is indeed “son of” user 2. □

<table><tr><td>j</td><td> ${K}_{j1}$ </td><td> ${K}_{j2}$ </td><td> ${K}_{j3}$ </td><td> ${K}_{j4}$ </td><td> ${K}_{j5}$ </td></tr><tr><td>1</td><td>3</td><td>0</td><td>5</td><td>0</td><td>2</td></tr><tr><td>2</td><td>0</td><td>35</td><td>0</td><td>3</td><td>0</td></tr><tr><td>3</td><td>0</td><td>0</td><td>5</td><td>0</td><td>0</td></tr><tr><td>4</td><td>7</td><td>0</td><td>0</td><td>0</td><td>0</td></tr><tr><td>5</td><td>0</td><td>0</td><td>0</td><td>0</td><td>0</td></tr></table>

Fig. 6. The key vectors for the five users in Fig. 1 with $r { = } 5 .$

It is noted that compared with the original user keys in Theorem 1, the revised user keys in Eq. (2) have each distinct prime number appear once at most. By constructing the user key as a vector of a fixed-length tuple, the KTK scheme reduces the likelihood of overflowing key values.

A simulation experiment was also conducted to illustrate the impact of overflow errors on the capacity of the proposed KTK system with key vectorization and the number of users that can be accommodated. The simulation was coded in Visual Basic and the user key vectors were defined as variant data type. The variant data type in Visual Basic is 22 bytes in length. Two variables were considered: the matrix density (defined as the proportion of nonzero entries in the relationship matrix H) and $P _ { \mathrm { m a x } } .$ . If we define $P ( t )$ as the proportion of nonzero entities in the relationship matrix that equal $t ,$ $1 \leq t \leq r ,$ then we can define $P _ { \mathrm { m a x } }$ as the maximum of $P ( t ) , 1 \leq t \leq r .$ The $P _ { \mathrm { m a x } }$ is studied because, in general, the element of the key vector that experiences overflow first will be the element that corresponds to the dominant relationship. The values studied for the matrix density and $P _ { \mathrm { m a x } }$ are $0 . 1 , 0 . 2 , . . . , 0 . 9$ and $0 . 1 , 0 . 2 , . . . , 0 . 5 ,$ respectively. Entries in the relationship matrix H follow a uniform distribution. For each test, users are added one at a time until an overflow occurs. When a user is added, an available prime number is assigned as the new user's prime key, the relationships between the new user and all existing users are generated, and the user key vectors are updated. For every combination of values for the matrix density and $P _ { \mathrm { m a x } } ,$ five runs were conducted and the averages plotted in Fig. 7.

In the worst case studied where the matrix density equals 0.9 and $P _ { \mathrm { m a x } }$ equals 0.5, roughly 300 users are possible. However, because relationship matrices are typically sparse, larger capacities can be realized. For instance, the KTK system can accommodate more than 5000 users when both the matrix density and $P _ { \mathrm { m a x } }$ are equal to 0.1. Capacities can also be increased by manipulating the relationships. For example, if the relationship “son of” is represented in the relationship matrix by $t = 1$ and $P _ { \mathrm { m a x } } { = } P ( 1 )$ , we can define a new relationship $t = h _ { \mathrm { m a x } } + 1$ also for “son $\mathrm { o f ^ { \circ } }$ and set half of the “son of” entries equal to 1 and half equal to $h _ { \mathrm { m a x } } + 1$ Depending on the distribution of the other relationships, large increases in capacity can be achieved from this manipulation. For instance, if initially $P ( 1 ) { = } 0 . 5$ and all of the other relationships have $P ( t ) \leq 0 . 2 5$ for a matrix density of 0.5, the manipulation can increase the capacity from 350 to approximately 650. The only expense is in the storage of n additional user key elements attributed to the “new” relationship.

## 5. Performance analysis and comparison

In this section, the performance of the proposed KTK scheme with key vectorization will be discussed and compared with other KTK methods from the literature [1–4,6,7,14,15,18,24]. In the literature, some KTK schemes are also called single-key-lock (SKL) mechanisms. The keys and locks in the SKL methods correspond to the prime keys and user keys in our method, respectively. When comparing different KTK and SKL methods, literature considers the access control matrix application [4,7,14,15] as opposed to the user relationship application discussed in this paper because of the importance of access control in information assurance [13]. Each row of the access control matrix corresponds to a user or process and each column corresponds to a file or resource. An entry $a _ { i j }$ in the access control matrix $A _ { m \times n }$ is the access right of user i to file j. Therefore, to put the access control matrix $A _ { m \times n }$ in the context of our KTK schemes, $a _ { i j } = h _ { i j } , \ a _ { m a x } = h _ { m a x } ,$ and $m = n .$

![](/api/attachments/BKYW2DCX/fulltext/images/89ae4cda175692e8b4e43e21781d205f12f569c9e1567998a80360f6b3a9a451.jpg)  
Fig. 7. Simulation results of maximum number of users with a key size of 22 bytes.

The performance of the proposed key vectorization method will be discussed and compared with the other KTK schemes based on the following six criteria put forth by Hwang et al. [14]:

1. the effort involved in initializing keys and locks;

2. the effort involved in determining an access right given a key and lock;

3. the effort involved when an access right is modified;

4. the effort involved when a new user is added;

5. the effort involved when a current user is deleted; and

6. the storage requirement for the keys and locks.

Tables 1–6 summarize the effectiveness and efficiency of several KTK schemes including our method.

## 5.1. Effort to initialize

Table 1 summarizes the effort to initialize keys and locks. Wu and Hwang's [24] and Chang and Jiang's [6] methods both require solving linear equations that can be computationally intense. Chang et al. [3] requires the transformation of the H matrix before the locks can be calculated, which increases the computational effort needed. The methods proposed by Chang [1,2] and Hwang et al. [14] may both encounter an overflow problem. The calculations required by Laih et al. [18] are complex. The computational efforts of the remaining methods [4,7,15] and our method are much more straightforward.

Table 1  
Initialization of the keys and locks

<table><tr><td>KTK schemes</td><td>Effort involved in initializing keys and locks</td></tr><tr><td>Wu and Hwang [24]</td><td>Given  $m$  keys, solve  $n$  sets of  $m$ linear equations for  $n$  lock vectors</td></tr><tr><td>Chang (1986) [1]</td><td>Given  $n$  locks, compute  $K_i = \sum_{j=1}^{n} (L/L_j) \times x_j \times a_{ij} \mod L$  for  $m$  keys</td></tr><tr><td>Chang (1987) [2]</td><td>Given  $n$  locks, compute  $K_i = \sum_{j=1}^{n} [a_{ij} \times L_j/n] \times n \times M_j$  for  $m$  keys</td></tr><tr><td>Laih et al. [18]</td><td>Given  $m$  keys, compute  $L_j(x) = \sum_{i=1}^{m} G_i^z \Pi_{s=1}^{i-1} (x-K_s)$  for  $n$  lock vectors</td></tr><tr><td>Chang and Jiang [6]</td><td>Given  $m$  keys, solve  $n$  sets of  $bm \ 0-1$ linear equations for  $n$  lock matrices</td></tr><tr><td>Hwang et al. [14]</td><td>Given  $m$  keys, compute  $L_j = \prod_{i=1}^{m} K_i^{a_{ij}}$  for  $n$  locks in the X-based form</td></tr><tr><td>Hwang and Yang [15]</td><td>Given  $m+n$  keys, compute  $L_{i1} = \sum_{h=1}^{t_i} S_h L_s^{h-1}$ ,  $L_{i2} = \sum_{h=1}^{t_i} O_h L_o^{h-1}$  for  $2a_{\max}$  locks</td></tr><tr><td>Chang et al. (1994) [3]</td><td>Transform the H matrix. Given  $k=a_{\max}$  keys, compute  $K_i = \sum_{s=1}^{k} t_is K_s'$  for  $i=1,2,...,r$ </td></tr><tr><td>Chang et al. (1997) [4]</td><td>Given  $m$  keys, compute  $L_{j(x)} = \prod_{i=1}^{m} K_i^{a_{ij}^{(x)}}$  for  $x=1,2,...,b$  and  $j=1,2,...,n$ </td></tr><tr><td>Chang et al. (2000) [7]</td><td>Given 4 keys, compute ECP values =  $\Pi_{z=4(s-1)}^{z+3} q_t^{a_z}$ , where  $t=1,2,3,4$ </td></tr><tr><td>Our method</td><td>Given  $m$  keys, compute  $K_{jt} = \prod_{ieS_i} P_i$  if  $S_i \neq \emptyset$  and 0 otherwise, for  $1 \leq t \leq r$ , where  $r=a_{\max}$  and  $S_t=\{i|a_{ij}=t \text{ and } i=j+1,...,n\}$ </td></tr></table>

Table 2

<table><tr><td colspan="2">Computation of access right</td></tr><tr><td>KTK schemes</td><td>Operations needed to compute the access right,  $a_{ij}$ </td></tr><tr><td>Wu and Hwang [24]</td><td> $m$  multiplications,  $(m-1)$  additions and one division</td></tr><tr><td>Chang (1986) [1]</td><td>One division</td></tr><tr><td>Chang (1987) [2]</td><td>Two divisions and one subtraction</td></tr><tr><td>Laih et al. [18]</td><td> $(i-1)$  multiplications,  $(i-1)$  additions and one division</td></tr><tr><td>Chang and Jiang [6]</td><td> $bm$  ANDs and  $b(m-1)$  XORs</td></tr><tr><td>Hwang et al. [14]</td><td> $\leq a_{\max}$  ( $X$ -based) divisions ( $a_{\max}$ : maximal value of access right)</td></tr><tr><td>Hwang and Yang [15]</td><td> $O(mn)$  divisions</td></tr><tr><td>Chang et al. (1994) [3]</td><td>Two or three divisions,  $2i$  additions and subtractions</td></tr><tr><td>Chang et al. (1997) [4]</td><td> $b$  divisions</td></tr><tr><td>Chang et al. (2000) [7]</td><td> $X$  divisions ( $X$ : maximal value of compound access right)</td></tr><tr><td>Our method</td><td> $\leq a_{\max}$  divisions ( $a_{\max}$ : maximal value of access right)</td></tr></table>

## 5.2. Effort to compute access right

As for the computation efforts to reveal an access right, our original proposed KTK scheme performs a certain number of divisions. The number of divisions is bounded by a constant equal to $a _ { \mathrm { m a x } } .$ The revised KTK scheme with key vectorization needs at most $a _ { \mathrm { m a x } }$ division operations. Table 2 summarizes the operations needed to compute an access right. The only other methods that require a constant number of operations are Chang's [1,2], Hwang et al.'s [14], and Chang et al.'s [4]. The other KTK methods require a number of operations proportional to the number of users.

<div class="mineru-algorithm" style="white-space: pre-wrap; font-family:monospace;">
Table 3
Modification of access right

KTK schemes Effort involved in changing access right $a_{ij}$ to $a'_{ij}$

Wu and Hwang [24] Solve a new set of $m$ linear equations for new locks $L_j$

Chang (1986) [1] Recompute $K_i = K_i + (L/L) \times x_j \times (a_{ij} - f(K_i, L_j)) \mod L$

Chang (1987) [2] Recompute $K_i = K_i + (|a_{ij} \times L_j/n| - |f(K_i, L_j) \times L_j/n|) \times n \times M_j$

Laih et al. [18] Recompute the $(m-i+1)$ coefficients $G_i^j$ for $L_j$

Chang and Jiang [6] Solve a new set of $bm$ 0–1 linear equations for $L_j$

Hwang et al. [14] Recompute $L_j = L_j \times (K_i)^{(a_{ij}' - a_{ij})}$

Hwang and Yang [15] Recompute $K_{a_{ij}1}, K_{a_{ij}2}, K_{a_{ij}'1}$, and $K_{a_{ij}'2}$

Chang et al. (1994) [3] Find $t_{kl}$ given $i$ and $j$. Recompute $K_k = K_k + (a_{ij}' - a_{ij}) \times K_l'$

Chang et al. (1997) [4] Recompute $L_{j(x)} = L_{j(x)} \times (K_i)^{(a_{ij}'(x) - a_{ij}(x)}$ for $x=1, 2, ..., b$

Chang et al. (2000) [7] Recompute ECP's = ECP_s × q_t^{(a'_l' - a_ij)} for $t = (z \mod 4) + 1$, s = (z/4) + 1

Our method Recompute $K_{jt} = K_{jt}/P_t$ and $K_{jt'} = K_{jt'} * P_i$, where $t = a_{ij}$ and $t' = a'_{ij}$
</div>

Table 4

<table><tr><td colspan="2">Table 4Appendability</td></tr><tr><td>KTK schemes</td><td>Appendability</td></tr><tr><td>Wu and Hwang [24]</td><td>Recompute all lock vectors</td></tr><tr><td>Chang (1986) [1]</td><td>Recompute all keys</td></tr><tr><td>Chang (1987) [2]</td><td>Recompute all keys</td></tr><tr><td>Laih et al. [18]</td><td>Yes (add a coefficient to each lock vector)</td></tr><tr><td>Chang and Jiang [6]</td><td>Recompute all lock matrices</td></tr><tr><td>Hwang et al. [14]</td><td>Recompute the locks of accessible files only</td></tr><tr><td>Hwang and Yang [15]</td><td>Recompute the locks of access rights affected</td></tr><tr><td>Chang et al. (1994) [3]</td><td>Row keys effected must be updated and a new column key may need to be added</td></tr><tr><td>Chang et al. (1997) [4]</td><td>To add user  $U_{m+1}$ , recomputed the elements of lock vector for  $a_{(m+1)j}^{(x)}=1$  only</td></tr><tr><td>Chang et al. (2000) [7]</td><td>To add subject  $S_{(m+1)}$ , recomputed the elements of ECP values for  $s=1$  to  $n/2$ </td></tr><tr><td>Our method</td><td>Recompute the locks of accessible files only</td></tr></table>

## 5.3. Effort to change access right

The computational efforts to modify an access right are summarized in Table 3. Wu and Hwang's [24] and Chang and Jiang's [6] methods require sets of linear equations to be solved. Our proposed method only requires one division and one multiplication to change an access right.

<table><tr><td colspan="2">Removability</td></tr><tr><td>KTK schemes</td><td>Removability</td></tr><tr><td>Wu and Hwang [24]</td><td>Recompute all lock vectors</td></tr><tr><td>Chang (1986) [1]</td><td>Recompute all keys</td></tr><tr><td>Chang (1987) [2]</td><td>Recompute all keys</td></tr><tr><td>Laih et al. [18]</td><td>To delete  $U_i$ , recomputed  $(m-i)$  coefficients of all for deleting</td></tr><tr><td>Chang and Jiang [6]</td><td>Recompute all lock matrices</td></tr><tr><td>Hwang et al. [14]</td><td>Recompute the locks of accessible files only</td></tr><tr><td>Hwang and Yang [15]</td><td>Recompute the locks of access rights affected</td></tr><tr><td>Chang et al. (1994) [3]</td><td>Reconstruct  $T$  matrix, recompute all row keys</td></tr><tr><td>Chang et al. (1997) [4]</td><td>To delete user  $U_{m+1}$ , recomputed the elements of lock vector for  $a_{(m+1)j}^{(x)}=1$  only</td></tr><tr><td>Chang et al. (2000) [7]</td><td>To delete subject  $S_{(m+1)}$ , recomputed the elements of ECP values for  $s=1$  to  $n/2$ </td></tr><tr><td>Our method</td><td>Recompute the locks of accessible files only</td></tr></table>

Table 6

<table><tr><td colspan="2">Storage requirement</td></tr><tr><td>KTK schemes</td><td>The complexity of the required storage</td></tr><tr><td>Wu and Hwang [24]</td><td> $O(m^{2}+mn)$ </td></tr><tr><td>Chang (1986) [1]</td><td> $O(m+n)$ </td></tr><tr><td>Chang (1987) [2]</td><td> $O(m+n)$ </td></tr><tr><td>Laih et al. [18]</td><td> $O(mn)$ </td></tr><tr><td>Chang and Jiang [6]</td><td> $O(m^{2}+bmn)$ </td></tr><tr><td>Hwang et al. [14]</td><td> $O(mn)$ </td></tr><tr><td>Hwang and Yang [15]</td><td> $O(m+n)$ </td></tr><tr><td>Chang et al. (1994) [3]</td><td> $O(mn)$ </td></tr><tr><td>Chang et al. (1997) [4]</td><td> $O(mn)$ </td></tr><tr><td>Chang et al. (2000) [7]</td><td> $\max(O(m), O(n))$ </td></tr><tr><td>Our method</td><td> $O(m)$ </td></tr></table>

## 5.4. Effort to update keys when adding new user

Table 4 summarizes the efforts needed to update keys and locks when adding a new user. Laih et al.'s [18] performs the best on this criterion because full appendability is achieved. In our proposed method, when a user is added, only the user keys of related users need to be recomputed. Therefore, considering the H matrix is typically sparse, the proposed method can still be efficient.

## 5.5. Effort to update keys when deleting user

The computational efforts required to update keys and locks when removing a user are summarized in Table 5. To remove a user, as when adding a user, our method only requires the user keys of the related users to be recomputed. Tables 4 and 5 thus illustrate our method's ability to manage the dynamics of the system.

## 5.6. Storage requirements

The space requirements are summarized in Table 6. An access control matrix $A _ { m \times n }$ has mn elements to store. The new KTK scheme in Theorem 1 requires only $( m + n )$ integers (m for prime keys and n for user keys). The revised KTK scheme with key vectorization needs only $( \boldsymbol { a } _ { \mathrm { m a x } } + 1$ )m integers (m for prime keys and $a _ { \mathrm { m a x } } m$ for user keys). The key vectorization method is still in linear proportion to the number of users, compared with the square order in the original relationship matrix. The method proposed by Chang et al. [7] is the only scheme that is comparable to ours with respect to storage requirements. The storage requirement of Chang et al.'s [7] method is on the order of max (O(m), O(n)).

## 6. Discussions and implications

In this section, we discuss the practical relevance of our new KTK scheme to modern businesses and organizations. In addition, the specific advantages that our prime key based system implies for potential business applications are presented. Evidenced by recent mandates and compliance regulations on security and privacy (e.g., Sarbanes–Oxley, Gramm–Leach–Bliley, Health Insurance Portability and Accountability Act–HIPAA, and Federal Information Security Management Act), companies are in need of increased security and reporting capabilities to prove to the federal government as well as many state governments that their IT security, administration and operations are in line with new regulations and mandates. However, in order to provide better IT security more effectively and efficiently, companies must balance the level of security attained with potential reductions in operational capability attributable to such security endeavors [13]. In this study, we propose a new solution to strive for better security without sacrificing too much of operational efficiency. The proposed “key vectorization” for our KTK mechanism provides better performance compared with other KTK schemes, as demonstrated in Tables 1–6. The new scheme along with key vectorization can result in improved operational capability for an organization that has to rely on business applications requiring tighter IT security control.

To highlight the major advantages of our proposed solution and its relevance to business applications, we can see that the prime key based system offers the following desirable characteristics.

(1) Simple and quick operation: Our solution provides simple and fast computation efforts to determine users' relationships in hierarchies while implementing IT security. This characteristic is necessary for today's business environment that requires fast responses and efficient resource usage. For example, it is vital for business applications or agents to securely access necessary data without waiting for responses or over-consuming company's computing/IS resources. We conjecture that incorporating our solution to a large information system such as an ERP system can benefit both operational and security needs.

(2) Less storage: Our solution requires less storage needs for security keys. On one hand, this results in fast access to keys with less search time. On the other hand, limited storage needs can facilitate mobile and ubiquitous computing while the storage of these keys can be easily detached-then-attached or copied to distributed/remote access locations. For today's component-based, modular agile business applications, our solution provides better fit with this characteristic.

(3) High degree of dynamism: Our solution requires minimal maneuvering for adding or deleting keys. This feature is crucial for business with dynamic operation needs. For example, companies (a) with dynamically changing applications which need to alter security access hierarchies frequently, (b) with frequent intra- or inter-organizational project team formation/dissolution, (c) with high employee turnovers, (d) with frequent business partner changes due to temporary business needs, and (e) with virtual organization structure will benefit greatly from our solution.

## 7. Conclusions

In this paper, we have proposed a key-to-key (KTK) scheme to implement the security policy wherein a user in the hierarchy is assigned a key pair and the relationship between any two users can be revealed through a pre-defined operation on the two keys associated with the two users. Based on the Fundamental Theorem of Arithmetic in number theory, this new KTK scheme manifests several advantages:

(1) Only a certain number of division operations are required to compute the relationship between any two users. The simplicity and limited number of divisions imply that the KTK scheme is relatively quick to determine user relationships.

(2) The spaces required for storing the prime keys and user keys are much less than the original H matrix.

(3) The KTK scheme facilitates the easy addition and deletion of users in the hierarchy. It only recomputes the user keys for the related users in the hierarchy, unlike such other KTK schemes as Wu and Hwang [24] and Chang and Jiang [6] where all the existing user keys need to be recomputed. In other words, a high degree of dynamism is achieved in the new KTK scheme as the addition and deletion of users do not affect most of the existing keys in the user hierarchy.

Some practical issues have also been discussed, including the number of prime keys allowed in the KTK system. Also discussed is the possibility of overflowing user keys. This potential overflow issue is not as significant as it used to be, considering modern objectoriented programming languages like Java have built-in arithmetic classes to handle arbitrary precision integers. In addition, a solution called key vectorization has also been presented to palliate this issue.

In terms of future research, researchers are prompted to devise new KTK mechanisms that will determine the relationships in a user hierarchy more quickly and efficiently and that will require less storage capacity. Even though the KTK scheme proposed in this paper has achieved a high degree of dynamism when it adds or deletes a user, the ultimate goal is to come up with a KTK scheme that will fulfill the perfect dynamism without affecting any of the existing user keys, including those of both related and unrelated users.

## Acknowledgments

The authors are thankful to the reviewers for their positive comments and insightful suggestions. The usual disclaimer applies.

## References

[1] C.C. Chang, On the design of a key-lock-pair mechanism in information protection systems, BIT 26 (4) (1986) 410–417.

[2] C.C. Chang, An information protection scheme based upon number theory, The Computer Journal 30 (3) (1987) 249–253.

[3] C.C. Chang, J.K. Jan, D.J. Buehrer, A scheme to determine the relationship between two users in a hierarchy, Computers & Security 13 (3) (1994) 255–261.

[4] C.C. Chang, D.C. Lou, T.C. Wu, A binary access control method using prime factorization, Information Sciences 96 (1997) 15–26.

[5] C.C. Chang, I.C. Lin, H.M. Tsai, A dynamic mechanism for determining relationships in a partially ordered user hierarchy, Proc. of the 18th International Conference on Advanced Information Networking and Applications, Fukuoka, Japan (March 2004), 2004, pp. 133–138.

[6] C.K. Chang, T.M. Jiang, A binary single-key-lock system for access control, IEEE Transactions on Computers 38 (10) (1989) 1462–1466.

[7] H.K.-C. Chang, J.J. Hwang, H.H. Liu, A novel access control method using Morton number and prime factorization, Informa tion Sciences 130 (2000) 23–40.

[8] E.C. Cheng, An object-oriented organizational model to support dynamic role-based access control in electronic commerce, Decision Support Systems 29 (2000) 357–369.

[9] D.E.R. Denning, Cryptography and Data Security, Addison-Wesley, Reading, MA, 1982.

[10] E.W. Dijkstra, The structure of the ‘THE’-multiprogramming system, Communications of the ACM 11 (5) (1968) 341–346.

[11] D. Gollmann, Computer Security, John Wiley & Sons, Chichester, England, 1999.

[12] G.S. Graham, P.J. Denning, Protection-principles and practice, Proc Spring Joint Computer Conference, vol. 40, AFIPS Press, Montvalc, NJ, 1972, pp. 417–429.

[13] J.T. Hamill, R.F. Deckro, J.M. Kloeber, Evaluating information assurance strategies, Decision Support Systems 39 (2005) 463–484.

[14] J.J. Hwang, B.M. Shao, P.C. Wang, A new access control method using prime factorization, The Computer Journal 35 (1) (1992) 16–20.

[15] M.-S. Hwang, W.-P. Yang, A new dynamic access control scheme based on subject-object list, Data & Knowledge Engineering 14 (1994) 45–56.

[16] J. Kim, Hierarchical structure of Intranet functions and their relative importance: using the analytic hierarchy process for virtual organizations, Decision Support Systems 23 (1998) 59–74.

[17] R. Kumanduri, C. Romero, Number Theory with Computer Applications, Prentice Hall, Upper Saddle River, NJ, 1998.

[18] C.S. Laih, L. Harn, J.Y. Lee, On the design of a single-key-lock mechanism based on Newton's interpolating polynomial, IEEE Transactions on Software Engineering 15 (9) (1989) 1135–1137.

[19] J.H. Saltzer, Protection and the control of information sharing in Multics, Communications of the ACM 17 (7) (1974) 388–402.

[20] J.H. Saltzer, M.D. Schroeder, The protection of information in computer systems, Proceedings of the IEEE 63 (Sept. 1975) 1278–1308.

[21] M.D. Schroeder, J.H. Saltzer, A hardware architecture for implementing protection ring, Communications of the ACM 15 (3) (1972) 157–170.

[22] B.M. Shao, J.J. Hwang, P.C. Wang, Distributed assignment of cryptographic keys for access control in a hierarchy, Computers & Security 13 (1) (1994) 79–84.

[23] H.M. Tsai, C.C. Chang, A cryptographic implementation for dynamic access control in a user hierarchy, Computers & Security 14 (2) (1995) 159–166.

[24] M.L. Wu, T.Y. Hwang, Access control with single-key-lock, IEEE Transactions on Software Engineering 10 (2) (1984) 185–191.

[25] J.H. Yeh, R. Chow, R. Newman, Key assignment for enforcing access control policy exceptions in distributed systems, Information Sciences 152 (2003) 63–88.

Mark Vroblefski received a Ph.D. in Management Science and Systems, an M.S. in Industrial Engineering and a B.S. in Mechanical Engineering from the State University of New York at Buffalo, and an M.B.A. from the State University of New York at Binghamton. He teaches courses in Production and Operations Management, Database Management, Telecommunications and Network Security. His primary research interests are in the areas of telecommunication networks, wireless communication networks and computer/network security. He has published in INFORMS Journal on Computing, European Journal of Operational Research, Omega, and Engineering Applications of Artificial Intelligence. Dr. Vroblefski is a member of the Institute for Operations Research and the Management Sciences (INFORMS) and the Decision Sciences Institute (DSI).

![](/api/attachments/BKYW2DCX/fulltext/images/8285a6b285ad267611fb08da7c20f93ac4c1dfa15cc8365d5883675f8a5f0ee5.jpg)

Andrew N. K. Chen received his Bachelor of Business Administration from Soochow University at Taiwan, M.S. in Accountancy from George Washington University, and Ph.D. in Operations and Information Management from University of Connecticut. His current teaching and research interests include knowledge management, IT business value, electronic commerce, database management, and business and Web programming applications.

His research work appears in Decision Support Systems, European Journal of Operational Research, Journal of Electronic Commerce Research, Journal of Management Information Systems, Management Information Systems Quarterly, and international conferences such as Americas Conference on Information Systems (AMCIS), Decision Sciences Institute (DSI) Conference, International Conference on Information Systems (ICIS), and Workshop on Information Technologies and Systems (WITS).

![](/api/attachments/BKYW2DCX/fulltext/images/5eb9e73f8cd0f34ac060c9234638275e974b0ae940adb2be6b0762a65884a3fc.jpg)

Benjamin B. M. Shao received his B.S. and M.S. from National Chiao Tung University, Taiwan, and his Ph.D. from the State University of New York at Buffalo. His research interests include IT impacts, IS security, e-commerce adoption, distributed processing, and software project management. His research has appeared in Communications of the ACM, The Computer Journal, Computers and Security, Decision Support Systems, European Journal of Operational Research, IEEE Transactions on Dependable and Secure Computing, IEEE Transactions on Systems, Man, and Cybernetics, Information and Management, International Journal of Human-Computer Studies, International Journal of Production Research, Journal of the Association for Information Systems, and Journal of the Operational Research Society, among others.

![](/api/attachments/BKYW2DCX/fulltext/images/9425c4dccb424634d34840d84b7808b11bfedd8429616a75c639cf08db24162c.jpg)  
Matthew Swinarski is an assistant professor in the Sam and Irene Black School of Business at Penn State University, The Behrend College. He received his Ph.D. from the State University of New York at Buffalo in MIS. His research, part of a larger project in the area of ITS outsourcing that was funded by the National Science Foundation (NSF), has been presented at HICSS and AMCIS. He has served as Issue Managing Editor for the Journal of Information Technology Theory

and Application (JITTA) and as Editor-in-Chief of INFORMS OR/MS Tomorrow Newsletter. His industry experience includes installation, configuration, operation and service contact management of enterprise applications for manufacturing companies in the Western New York area.
