---
otero_id: 17859
otero_key: "Q7Q48UJA"
title: "Cryptographic transformation of data relationships"
authors: "Thomas J. Murray"
year: "1979"
journal: "Information & Management"
doi: "10.1016/0378-7206(79)90040-5"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Cryptographic Transformation of Data Relationships

Thomas J. Murray

School of Business Administration, University of Missouri-St. Louis, St. Louis, Missouri 63121, USA

The use of cryptographic transformations for the protection of sensitive data stored in a computer based file can be an effective data security technique. The overhead incurred in such use is primarily associated with the enciphering and deciphering routines. Two cases are described in which such overhead may be significantly reduced.

Keywords: Cryptography, data security, pointers, data relationships.

![](/api/attachments/Q7Q48UJA/fulltext/images/05447d702423b3252ae01a30df04a3c5734e8510fe480f36e8fc88d966e46f7c.jpg)

Thomas J. Murray is an Assistant Professor of Information Systems at the University of Missouri-St. Louis. His area of interest is computer based information systems and his academic background is in both engineering and business administration. He has held a number of both technical and managerial positions in industry. Professor Murray received his Ph.D. from the University of Massachusetts at Amherst.

## 1. Introduction

The protection of sensitive data from unauthorized access is of serious concern in many operating environments. The need to protect arises from concerns for privacy considerations, (e.g. with medical or credit files) and from considerations of competitive market position, (e.g. of market research or product testing data). The access to such data must be strictly controlled. Although such considerations exist in an organization supported by manual information systems, it becomes more complex and difficult to achieve data security in an organization supported by automated information systems.

Physical security, access authorization schemes, and administrative controls form an essential barrier to compromise. If, however, these are circumvented, either accidentally or deliberately, then the contents of a data file may be compromised. As a final line of protection, sensitive files may be enciphered, i.e. they may undergo a cryptographic transformation and be rendered unintelligible to anyone without the necessary key to decipher them.

The cryptographic transformation of sensitive data files adds a level of security to the protection of the contents of those files, and thus contributes towards a more secure operating environment. The most tangible cost associated with providing this additional security is that involved in the actual enciphering and deciphering of data whenever it is read from or written to these files.

In some applications, much of the data contained in a given file may not be sensitive yet, the costs of enciphering and deciphering are incurred as if all the data were sensitive. This paper describes an approach where costs may be significantly reduced for some applications; the enciphering and deciphering operations are assumed to be performed by software.

## 2. Cryptographic transformations

Cryptography (or privacy transformation as it is sometimes called) is concerned not with hiding or masking the existence of sensitive data but with transforming the data in such a way that it is unintelligible to anyone without knowledge of the reverse transformation.

![](/api/attachments/Q7Q48UJA/fulltext/images/c67c2fed833af92972d38e07c799ea9381730e371622091c8fc81761af4af1d2.jpg)  
Fig. 1. Basic cryptographic relations.

The following two definitions are used here:

Plaintext is undisguised data that is intelligible to all knowing the language.

Ciphertext is plaintext after it has undergone a cryptographic transformation.

Both the transformation and its reverse must be one-to-one, i.e. there must be no ambiguity in the results. Figure 1 illustrates this.

Cryptananalysis is the process of transforming a ciphertext back into plaintext without advance knowledge of the original transformation. The effectiveness or the usefulness of any cryptographic transformation must be judged in terms of its resistance to cryptanalysis.

Computer based approaches generally provide a pseudorandom string of digits which can be combined with the plaintext to produce the ciphertext.

The Vernam [1] system was first used on telegraph systems. Two data streams are used: one stream contains the plaintext, the other contains a string of pseudo-random digits. An exclusive logical OR operation is performed and the result is the enciphered text. To reverse the transformation an exact copy of the pseudo-random stream is combined with the ciphertext again using an exclusive logical OR operation.

The advantage of this system is that the same pseudo-random stream is used to both encipher and decipher. The disadvantage is that the pseudo-random stream must be as long as the plaintext. For heavy use this is a serious problem, which may be eased by using multiple pseudo-random streams containing numbers of entries that are relatively prime to each other. For example using a two stream system: the first stream contains 1000 pseudo-random numbers and the second stream contains 1001 pseudo-random numbers. The two streams form loops which repeat and both streams are applied to the plaintext. The number of combinations possible with the two streams is the product, i.e. 1,001,000.

The pseudo-random sequence required for the streams can be generated either by hardware or by software. The most common hardware device is the shift register and the sequence generated repeats after $2^{n} - 1$ bits where n is the number of stages.

Software may incorporate a random number generator. Security lies in the constants of the algorithm itself and in the seed. Since all random number generators repeat, the length of the unrepeated sequence is a critical factor.

An alternative method lies in storing the random sequence on a demountable storage medium such as a magnetic tape or disk cartridge. The device can be safeguarded and mounted only under proper supervision.

The protection of a data file may involve encipherment ranging from the entire contents of the file to pointers in the file. Between these two extremes, part of the data may be transformed into ciphertext and part left in plaintext. We now discuss two cases: one in which pointers are transformed and one in which the data is segmented into cipher and plaintext.

## 3. Case I - pointer-only transformation

The usual approach is to encipher the entire file, and all applications must first decipher, at least, those logical records retrieved.

The following discussion centers on a file with two characteristics:

(1) the file contains multiple records - none of which taken in isolation are sensitive, and

(2) sensitivity of the file contents lies in the relationships that exist between the records and not in the records themselves.

Pointers (or symbolic record addresses) are frequently used to create a data structure which expresses the relationship between the elements of the structure. Figure 2 illustrates such a linking between logical records in a file. The pointers represent logical record numbers. In the figure logical record 1 is linked to logical record 7, logical record 7 is linked to logical record 3, and logical record 3 ends this linkage.

![](/api/attachments/Q7Q48UJA/fulltext/images/75666322e423c2d54e94ef8bf3a062f221027486f2383cd830e70b619473a2e0.jpg)  
Fig. 2. Use of pointers in a file.

It should be observed that the pointers may link the records in one file with records in another file.

If the pointers alone are enciphered then only the relationships are cryptographically secure; then the file may be processed without deciphering whenever applications do not require knowledge of relationships. When relationship knowledge is needed, only one or more pointer fields need be deciphered since all non-sensitive data in the record is in plaintext.

Such a system might occur in a hospital or credit environment. Identification of patients or persons with credit ratings is seldom sensitive. Similarly specific medical diagnoses and their associated treatments or specific credit ratings or credit backgrounds may not be sensitive. Only in relating a particular patient with a specific diagnosis or a particular person with a specific credit rating is confidentiality needed. Applications requiring reports involving patient or customer lists, statistical analyses, historical experience, etc. are not sensitive and can be processed normally.

## 4. Case II - data subsets

In some applications, only a limited amount of data in the file is sensitive. In this case, the file can be subdivided into two subsets. Linkages between individual records in these subsets may be made by means of pointers, as illustrated in figure 3, where pointers in the nonsensitive subset link to enciphered entries in the sensitive subset. As a result applications involving only the nonsensitive portion of the data may still by run without deciphering overhead.

![](/api/attachments/Q7Q48UJA/fulltext/images/68343ea61ff6919890a12b9d65b9e9fb4049e31a250288c8091ab94d2af02096.jpg)  
Fig. 3. Linkages between subsets.

If, in a particular application, sensitivity exists in knowledge of the existence of related sensitive data, then pointers may be enciphered. These pointers may then be used to link data in the non-sensitive subset back to the sensitive subset. Access to plaintext equivalents of these pointers can be obtained only through the sensitive subset.

This principle of dividing the data into sensitive and non-sensitive subsets also lends itself to improved security since a smaller number of users may now be authorized knowledge of (or access to) the deciphering key.

## 5. Conclusions

One of the drawbacks of using a cryptographic transformation is the increased time required to decipher the file for every application using that file. This overhead can be reduced.

Overhead represents the additional time required to process ciphertext above and beyond the time required to process its plaintext equivalent. This overhead is

primarily a function of:

(a) enciphering and deciphering technique, and

(b) the quantity of ciphertext required to be deciphered on any given run.

The greatest savings can be achieved in those cases where only the relationships between the logical records are sensitive; only the pointers need be enciphered, and, correspondingly, deciphered when, and if, any of these relationships must be known. Users who are not authorized may still access and make use of the data content: they are only barred from pointer decipherment.

if only a small segment of the data must be treated confidentially, it may be placed in a separate area of the file. Applications requiring only non-sensitive data need not incur the cryptographic overhead, yet the sensitive records may be easily linked to the non-sensitive area of the file, if the pointers are deciphered.

With fewer applications requiring deciphering, security is increased.

## Reference

[1] G.S. Vernam, "Cipher Printing Telegraph Systems for Secret Wire and Radio Telegraphic Communications". Journal of the American Institute of Electrical Engineers, Vol. XLV, Feb. 1926, pp. 109-115.
