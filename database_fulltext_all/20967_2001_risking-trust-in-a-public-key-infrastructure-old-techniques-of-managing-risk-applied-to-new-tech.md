---
otero_id: 20967
otero_key: "5SFJWWW9"
title: "Risking “trust” in a public key infrastructure: old techniques of managing risk applied to new technology"
authors: "Andrew D Fernandes"
year: "2001"
journal: "Decision Support Systems"
doi: "10.1016/s0167-9236(00)00139-1"
query: ""
source: "https://ais.kexu.win"
images_downloaded: false
---
# Risking AtrustB in a public key infrastructure: old techniques of managing risk applied to new technology

Andrew D. Fernandes )

Securify, Inc. http:( ) <sup>rr</sup>www.securify.com<sup>r</sup> , 2535 Sterling Green DriÕe, MorrisÕille, NC 27560 USA

## Abstract

Installing a public key infrastructure PKI can change in the security model of an IT operation in several ways. ThisŽ . article gives a layman’s overview of what exactly a PKI is, and how one can be built and operated safely and securely. First, the PKI must be designed using the familiar principles of risk management, rather than Atrust managementB. Next, although it is not widely appreciated, digital signatures are not equivalent to traditional signatures, and understanding this difference is crucial to understanding how a PKI needs to be audited. Lastly, I will show that for a PKI to provide ongoing security, the principles of compromise–containment and regular auditing must be adhered to. q 2001 Elsevier Science B.V. All rights reserved.

Keywords: Digital signature; Public key; PKI; Risk management; Digital certificate; Certification authority; Trusted third party; Cryptography; Certification practice statement

## 1. Introduction to digital signatures

With companies worldwide rapidly embracing electronic commerce, digital security systems have become commonplace rather than just specialty items for high-end use. Words such as AencryptionB, Adigital signatureB, and Apublic key infrastructureB Ž . PKI are used so often in the media that it’s easy to forget how novel these terms really are.

For instance, one misunderstood concept is the difference between analyzing an audit trail that uses digital signatures as opposed to handwritten ones. Most people assume the analysis is the same in both scenaris. Is this a safe assumption? Are digital signatures truly impossible to forge? What does it mean to AtrustB a third party in an electronic transaction? The answers to these questions may surprise you . . .

## 1.1. What are digital signatures?

To understand what digital signatures are and how they are used, let us first analyze a traditional banking scenario to see how handwritten signatures are used in daily transactions. Suppose that you were a teller at a bank, and a stranger came up to your wicket with a slip to withdraw money on what they claimed to be their account. The only form of identification that you have for them is their handwritten signature on the withdrawal slip. Being a cautious

(Questioned Signature),

(Original Sample Signature)

teller, you would then take the deposit slip into the back room of the bank where all of your customers original sample signatures are stored to compare the two signatures.

No two handwritten signatures ever look exactly alike, so you would have to use your judgement to determine whether or not the signature was a forgery. For example, when comparing handwritten signatures as shown in Fig. 1, you may decide to accept the signature as genuine although there are small differences between the two samples. Of course, if the withdrawal is sufficiently large, you may require additional identification before giving Alice her money. On the other hand, if the two signatures differed substantially, such as those in Fig. 2, then it is unlikely that you are facing the ArealB Alice. Although it is possible for signatures to change over time, such a change is relatively rare. If her signature does change, Alice may still be able to re-prove her identity by displaying additional identification, and then update her AoriginalB sample signature at the bank.

If we work through the same scenario using digital signatures, there are remarkable similarities between using handwritten and digital signatures. Just like a paper withdrawal slip, Alice will submit an electronic withdrawal slip, perhaps by email. The slip even has a space for her signature. This time, however, her AsignatureB is a series of numbers. Putting you back in your guise as a bank teller, suppose you received an email request to transfer money from Alice’s account to Bob’s account. All that you and the computer would see is a request that looked like Fig. 3, where the number A234234728349B in the figure is Alice’s digital signature. In practice, using systems such as the United States’ Digital Signature Standard 6 , keys and the <sup>w</sup> <sup>x</sup> digital signatures are between 150 and 600 decimal digits long. The signature is calculated using the whole digital message, so any change in the message, no matter how slight, will invalidate the signature. The signature will only be valid if the entire message is copied exactly—including the serial number. So, if Alice sent a copy of her email to Bob, what stops Bob from making a second identical withdrawal? The bank would not process the second request since it would have the same serial number —and serial numbers are never reused. Therefore, although handwritten signatures must be almost identical from transaction to transaction, a digital signature must look different for every transaction.

![](/api/attachments/5SFJWWW9/fulltext/images/62f3790636bae3a97bf64dfac5ca67284eccf3735d050ea777fa1841bb0d9542.jpg)

![](/api/attachments/5SFJWWW9/fulltext/images/edb884bad596cb93ef698537cafcec19a48a5afa1678473a170c66eacee2892e.jpg)  
Fig. 1. Similar, but non-identical signatures.

![](/api/attachments/5SFJWWW9/fulltext/images/6c70bd088a3acad9896834e6301d914e2b9262ec6cafaa82744dbe63b8e6ae2d.jpg)  
Fig. 2. Two non-similar signatures.

With the handwritten signatures, it was easy for the teller to verify Alice’s signature on the withdrawal slip because of the visual similarity between the slip and the bank’s records. In contrast, digital signatures are just long strings of numbers, and can only be compared by detailed mathematical calculation, not by eye. So, how can a teller know that a string of numbers is a valid signature, especially since the numbers must be different for every transaction? In the electronic world, there is a digital version of the bank’s paper sample signature. A computer can validate a digitally signed document by mathematically combining the digital signature numbers with the Aoriginal sampleB numbers. Whereas handwritten validation of signatures can be done by eye, digital verification is more difficult than just comparing two numbers. Instead, the digital Aoriginal sampleB is mathematically combined with the signed document and the digital signature, and the result of the calculation determines the document’s validity. For example, the process of determining the validity of a series of email requests for account transfers would look something like Fig. 4. Note in the figure that although the digital signature of every email is a different number, the Aoriginal sampleB never changes. To the teller, there would be no reason to suspect that the last example has an invalid signature without using a computer to solve the relevant mathematics. The teller themselves would never know.

![](/api/attachments/5SFJWWW9/fulltext/images/f5661982b967708222a04cf95a5d3a11e59d252b9e7c22db386bf4aa293a6cd6.jpg)  
Fig. 3. A schematic Adigitally signedB request.

In cryptographic terms, the digital Aoriginal sampleB is called Alice’s public key. Alice wants every teller in every bank to have a copy of it, so each teller can verify her digital messages as genuine. For Alice to digitally sign a document, she must provide her computer with a the message she wants signed,Ž . and b a secret number called herŽ . priÕate key. The term AprivateB comes from the fact that Alice must keep this number private—anyone who has it could produce a perfectly valid forged signature. The computer would take these two pieces of information, use them in a complicated mathematical formula, and produce Alice’s digital signature as a result.

![](/api/attachments/5SFJWWW9/fulltext/images/b1b005c4f1fe74cb5d3b4ccc8105707d3dd7305561825b08c772a047c650afc6.jpg)  
Fig. 4. Validating a digital signature.

So, how does the bank obtain Alice’s public key in the first place? Anybody wanting to use digital signatures needs a way to produce, distribute, and destroy public keys—the bank wants yours, and you want the bank’s. The computer programs and protocols needed for everyone to exchange public keys is called a public key infrastructure. There is a lot of PKI information on the web—a good place to start for information is a Alink farmB such as Ref. 12 .<sup>w</sup> <sup>x</sup>

## 1.2. Digital signatures need PKIs

To build a PKI, you need more than software that can produce and validate digital signatures. Consider how banks currently obtain their original paper sample signatures. When opening a bank account, Alice must provide a sample of her signature plus additional identification to show that she really is Alice. The banks must carefully guard her paper signature to prevent fraud.

The digital case is a little different. Each person could physically go to the bank and hand over a copy of their public key, just as they would a handwriting sample. However, requiring a physical appearance eliminates the main advantage of electronic commerce—everything can be done online. So, if Alice can submit her public key to the bank only by email, the bank has no way of knowing that the emailed public key really came from Alice. After all, they do not yet have any public key for her. If the bank allows Alice to submit her public key via email, what would stop Alice from opening a credit card account, and claiming that her name was Carol? The bank needs to somehow attach Alice’s physical identity with her digital identity. In a nutshell, associating a AnameB with a public key is the central business of companies like VeriSign 23 , Thawte<sup>w</sup> <sup>x</sup> <sup>w x</sup> <sup>w x</sup> 21 , and GTE CyberTrust 17 .

Again, examining current non-digital practices in the banking community will show how the bank can safely digitally register Alice. Suppose that when opening your first account at the bank, you presented your driver’s license as identification. Most drivers’ licenses a have a photo and printed name, bŽ . Ž . contain a signature sample, and c are difficult toŽ . forge. The license is a certificate that confirms the identity of the bearer. So suppose that the bank kept records of its client’s digital Aoriginal samplesB as a series of certificates signed by Trent, a very trusted bank manager, as shown in Fig. 5. Now instead of having to keep every public key secure, the bank would need only one securely authentic copy of Trent’s public key, since every certificate would be considered valid if Trent signed it. How Trent comesŽ to trust Alice, Bob, or any other of the bank’s clientele is a completely separate story. That key . would be used to authenticate Alice’s public key, which would then be used to authenticate her withdrawal request. If Trent is very trustworthy to the bank, then Alice could even introduce herself to the bank using any certificate Trent had given her. Her digital certificate could be used in place of her

Serial Number 9144

"Alice" is 5930864930293

Serial Number 9145

Signed, 24364515645 (Trent)

"Bob" is 94034095989834

![](/api/attachments/5SFJWWW9/fulltext/images/2d8d6abf3c0dd8c8b88d36c78aa37132bc8c78fd107f3df26003aa10916f1f8a.jpg)

Serial Number 9146

Signed, 3984835989 (Trent)

"Carol" is 21309983458984

Signed, 88489547434 (Trent)

Fig. 5. A set of certificates issued by trusted authority Trent.

(etc.)

driver’s license as identification. Her certificate is AproofB of her ArightB to associate her name with the public key A593086930293B Ž . as per Fig. 5 .

Of course, many details need to be addressed before a bank could actually use digital signatures in everyday transactions. Handwritten signatures may change over time, and digital signatures are no different. After all, passwords may be stolen or forgot ten, and a change in a password may imply a change in digital signature. Alice’s name may change, or she may have opened her account using a fraudulent name. Therefore, the bank needs methods to collect, verify, archive, distribute, update, or revoke any public key it may deal with. Not only must the bank manage the list of its customers’ public keys, but the bank’s customers have to manage the bank’s public keys. Otherwise, how would Alice receive emailed confirmation that her request was completed? Communication is, after all, a two-way street.

For people to communicate by telephone, you need more than just telephones. For a useful phone system, you need phone books, telephone poles, operators, directory assistance, wiring technicians, billing systems, laws, protocols, policies, and so on. Only when these items are connected together to form a communication infrastructure, can you can make a call. Similarly, the software, hardware, policies, protocols, and laws that Alice needs to use to be able to reliably verify Bob’s digital signature also form a communications infrastructure. That infrastructure is called a Public Key Infrastructure, or APKIB for short.

## 1.3. Electronic identity in a public key infrastructure

To recap: certificates tie a person’s name with their public key. Their public key is used to verify their electronic identity. But is Alice’s Aelectronic identityB really the same as her name? For instance, what happens if the bank has two clients who are both named Alice? This exact calamity is depicted in Fig. 6. Assuming that Trent is trustworthy, which AAliceB does each public key refer to? What if each AAliceB has more than one public key, or more than one bank account? Alice’s name alone does not uniquely identify her to the bank. Our two Alices could physically show their driver’s licenses to distinguish themselves, if they could tolerate the inconvenience. But in a purely digital world, a digital signature is the only possible way that an electronic identity can be verified.

![](/api/attachments/5SFJWWW9/fulltext/images/8bf566516ead244cc36b5b1953f8a66aa772529803c4fb428e35a3121c10d14a.jpg)  
Fig. 6. Which AAliceB corresponds to which certificate.

What if Alice’s certificate contained more information about her, such as her address, and physical description? Her certificate would look like Fig. 7. Never mind that Alice may not want the bank to know her weight, this certificate will probably be sufficient to distinguish her from any other Alice, other than her twin sister. Now, however, Trent must be responsible for verifying all the information in that certificate. He will have to verify Alice’s address, check her eye color, and possibly confirm her weight. Revealing personal or confidential information in a certificate is a real problem in PKIs. For details, see European Union Directive 95<sup>r</sup>46<sup>r</sup>EC <sup>w</sup> <sup>x</sup> 20 .

With all the work it takes to certify Alice’s identity, Trent will have to assure the bank that he will carry out his certification work properly, accurately, and diligently. After all, the bank may rely on his certificate to loan Alice a lot of money. If Alice defaults on the loan, the bank will want to find her! In PKI terms, Trent is acting as a Certification Authority Ž . CA —an authority responsible for issuing digital certificates, and certifying them as accurate and correct. The Certification Authority is an important part of the PKI. Trent had better be very trustworthy, because both Alice and the bank rely on him to perform his job with care. If Trent makes mistakes in certifying people, the bank may be defrauded, or Alice could have money stolen. In fact, everyone using the PKI risks loss from using the PKI, Trent included. Understanding these risks, and how these risks can be managed, is the topic of the rest of this paper.

## 1.4. Other digital signature references

There are many references that explain digital signatures, cryptography, and PKI. For basic web and electronic commerce security, see Refs. 4 and<sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 5 . Two excellent books on the mathematics of cryptography are Ref. 29 for the beginner, and Ref. <sup>w</sup> <sup>x</sup> <sup>w</sup> <sup>x</sup> 28 for the more advanced student. Lastly, one of the most influential books in the field of PKI is Ref. <sup>w</sup> <sup>x</sup> 2 , although it should be mentioned that the authors assume that a PKI must operate along the lines dictated by the ITU recommendation X.509.

```txt
Serial Number 9148
"Alice" of Toronto, Ontario, Canada, has blue eyes, is 1.8 meters tall, weighs 80 kilograms, and has digital signature public key 5930864930293.
Signed,
02398327432
(Trent)
```  
Fig. 7. How not to identify Ž . AAliceB from the information in her certificate.

## 2. The risks of using a public key infrastructure

The purpose of a PKI is to associate a person’s electronic identity with their physical identity. More succinctly, a PKI identifies people. But what happens if the PKI somehow gets it wrong? Like any other type of infrastructure, it’s impossible to build a completely flawless PKI. Cases of mistaken identity will occur. So, what happens if Bob relies on Alice’s digital signature, but the signed message did not really come from Alice? Bob would be relying on a digital forgery. A Certification Authority cannot necessarily stop digital forgeries because the CA only validates Alice’s identity when issuing her a certificate for the first time. If Alice’s private key is subsequently stolen, the CA usually has no liability for any losses anyone incurs. For example, in Sections 7.3 and 7.4 of VeriSign’s Certification Practice Statement <sup>w</sup> <sup>x</sup> 26 , Bob would be responsible for always using a AtrustworthyB computer, and agree not to hold anyone except himself responsible for the appearance of any digital forgeries. Unfortunately, there is currently no accepted or even widely used definition of the term AtrustworthyB.

Cases of mistaken identity happen relatively frequently with traditional signatures. Credit card theft and fraudulent check writing are two of the bestknown examples, and are the consequence of signature forging. Although handwritten signature forging is fairly commonplace, the handwritten signature remains the most accepted type of identification used today. Handwritten signatures are considered reliable enough for the vast majority of day-to-day business. In theory, digital signatures are literally billions of times harder to forge than handwritten signatures. Therefore, you may expect that relying the validity of a digital signature is more risk-free than relying on the validity of a handwritten signature.

Unfortunately, the analogy we have used so far between handwritten and digital signatures starts to break down when you analyze the risks of using a PKI. The consequences of a digital forgery appearing in the PKI are surprisingly far-reaching, and may affect more people than you think.

## 2.1. EÕeryone is exposed to risk

If your handwritten signature is forged at the bank and money is withdrawn from your account, you will suffer the loss unless you can prove the signature was a forgery. If the signature was forged, the bank will suffer the loss. In any case, the only two parties at risk here are you and the bank, and both of you are only at risk for that one disputed transaction. In contrast to this scenario, the appearance of one digital forgery puts eÕery PKI participant at risk, for eÕery transaction that uses the PKI. To understand how and why one digital forgery has such long reaching consequences, we have to examine the risks of each individual PKI participant.

## 2.1.1. Risks of the signature owner

Alice uses her signature to authorize many transactions in her life, from bank withdrawals and credit card purchases, to entering real estate contracts and signing school notes for her children. Therefore, if someone forges Alice’s signature, they could potentially steal from her, damage her credit rating, or allow her children to skip school. In the physical world, a number of safeguards limit the damage that a forgery could inflict on Alice. By law, Alice’s credit card company cannot hold her liable for purchases she did not make. Her bank must let her disavow any withdrawal request shown in her banking statement. There are strict limits on consumer liability for Automated Teller Machine ATM , debitŽ . card, credit card, and checking account fraud in the US; these limits have been summarized by the Federal Deposit Insurance Corporation 16 . For a single<sup>w</sup> <sup>x</sup> transaction of large value, such as a real estate contract, a court would probably rule that more than just a signature would be needed to positively identify Alice in the deal. Lastly, Alice’s children would be foolish to skip school more than once using her forged signature. Since the children directly benefit from the forgery, it would be clear to their teacher who the forger is, and that knowledge would result in the forger being caught.

In summary then, Alice does not have to worry about someone forging her signature because she has many options. She aŽ . transfers her loss to someone else, such as the credit card company or the bank, bŽ . needs more than just her signature to complete a transaction, or c accepts small losses, since theŽ . forgers will surely get caught if they become too greedy. These techniques Alice uses to manage her risks can also be used in the digital world. Therefore, with proper risk management techniques, the total risk that Alice is exposed to is relatively small. Without proper risk management, her potential losses are enormous.

## 2.1.2. Risks of the relying party

Anyone that relies on Alice’s signature for identification is called a relying party. The bank relies on Alice’s signature to validate withdrawal requests. Her credit card company relies on her signature to authorize credit purchases. They run the risk of losing money if they accept a forged copy of Alice’s signature as valid. Currently banks and credit card companies manage their risks using numerous techniques. They charge high interest rates to make up for fraudulent losses. They implement widespread auditing and checking programs to detect potential frauds. They require multiple types of identification before they will create and allow access to your account. Combining these and other techniques allow them to remain profitable while accepting certain levels of unavoidable loss. Despite all of the credit card fraud that exists, the credit card portion of the banking industry remains extremely profitable 7 .<sup>w</sup> <sup>x</sup>

If the digital world follows similar techniques, anybody who needs to rely on a digital signature could manage their risks in a similar way. Unfortunately, a detailed look at the structure of a PKI reveals that these goals are not simple to accomplish. For example, imagine the situation depicted in Fig. 8. There, Alice 1 requests a certificate from her CA Ž . much they way she could request a credit card with her credit card company. Trent the CA would then validate her identity and 2 issue her a certificate. Ž . Alice could then take her certificate, sign a digital contract with Bob, and 3 convince Bob of herŽ . identity using her certificate. What happens if somehow Mallet, a malicious evildoer, manages to fake Alice’s identity and defraud Bob? What recourse does Bob have? To answer that question, let us look at similar situations that occur with handwritten signatures.

![](/api/attachments/5SFJWWW9/fulltext/images/87547110e0df569aa0420195e8826b4b95bc29db2924454f024306d3b650ffdc.jpg)  
Fig. 8. The relationship between a Certification Authority, a signature owner, and a relying party.

Suppose that Alice had 1 applied to Trent for aŽ . credit card, 2 been issued the card, and 3 boughtŽ . Ž . a stereo from merchant Bob. Unfortunately, somewhere along the way, Mallet stole Alice’s credit card number and is was really him who bought the stereo from Bob. As an authorized credit card-accepting merchant, Bob does not need to worry about fraud because his legal arrangement with Trent protects him from fraud. In other words, before either Alice or Bob can use or accept a credit card, they must enter a legal agreement with Trent. That legal agreement specifies how both of them manage their risks.

Suppose that Bob does not have a legal arrangement with Trent. This would be the case if Alice Ž . actually Mallet wrote Bob a digital check to be drawn on Trent’s bank. Here, Bob would have to either accept his loss from the bad check, or buy insurance against that type of fraud. Another possibility is for Bob to require additional identification from Alice. However, do not forget that in the digital domain, Alice’s digital signature is the only way she can identify herself. It is not surprising that merchant acceptance of personal checks has fallen in the past few years—the personal check does not allow Bob many ways to manage his risks.

Getting back to the digital domain, remember that Alice’s digital signature is meant to act as a replacement for her handwritten one. Therefore, if Alice

Ž . again, really Mallet were sending Bob a digital contract, Bob would have no recourse if Mallet defrauded him. Therefore, a PKI will generally not allow Bob very many risk management options unless he has some sort of legal relationship with the CA, much like a credit card company and a merchant.

## 2.1.3. Risks of the certification authority

When acting as a CA, Trent is responsible for certifying that the information in Alice’s certificate accurately describes her. Therefore, if Bob relies on Alice’s certificate to verify her identity, he is not relying on Alice’s signature to prevent fraud; Bob is relying on Trent’s signature. If Bob is defrauded by Mallet masquerading as Alice, he will expect Trent to cover his losses. Therefore, Trent is acting like an insurance agent, protecting Bob from the risks of using Trent’s PKI. Currently, some CAs offer insurance to their clients protecting them from damages resulting from forged signatures; an example is VeriSign’s NetSure plan 24 . However, CA Trent<sup>w</sup> <sup>x</sup> may not be able to insure Alice in any economically feasible way because the value of Alice’s signature changes with each transaction.

The amount that Alice’s signature is worth really depends on what her signature is doing. Alice may be signing a note for her child’s schoolteacher, authorizing a US\$100,000 sale with her stockbroker, or signing an important company memo. In some cases, the transaction she signs has a definite monetary value, while in others it does not. Therefore, calculating the absolute value of her signature is not easy, or maybe even possible.

An insurance agent will indemnify only specific types of damage covered by the insurance contract, and only up to a specified monetary amount. For instance, car insurance coverage amounts are calculated based on the value of the vehicle and an estimate of how much damage that single car can cause. The cost of that insurance is based on the type of vehicle, how it will be used, and the age and sex of the drivers. Since the value of Alice’s signature can change, it is impossible for Trent or even AliceŽ . to put a dollar value on the integrity of her signature. If Alice and Trent cannot agree on the value of Alice’s signature, then Trent cannot underwrite an insurance policy for her.

The amount which Alice’s Asignature insuranceB will cost is the other question she and Trent must answer. Alice obviously will want to pay as little as possible for as much coverage as possible. Trent will have to look at Alice’s past claim history, her history of being defrauded via the PKI, how she uses her digital signature, how any past digital forgeries were made, and the minimum<sup>r</sup>average<sup>r</sup>maximum monetary worth of each signature. Therefore, calculating Alice’s insurance rate is a much bigger problem than AsimplyB determining the worth of her signature.

In fact, Trent’s chief difficulty costing out Alice’s insurance rate is that he has no information on Alice’s signature’s fraud history. The standard accounting and auditing tools available to the auto insurance industry are missing from the PKI industry. Worse yet, the accounting and auditing needed to set her insurance rates would be equivalent to Alice reporting each and every signature she makes to Trent. People like Alice are usually concerned with how credit-reporting agencies such as Equifax <sup>w x</sup> <sup>w x</sup> 15 or TransUnion 22 handle their credit histories. It is unlikely she would agree to give Trent her credit history and detailed records of all her signed transactions. In summary, even assuming that Trent could evaluate Alice’s signature, he probably could not figure out a reasonable rate to charge for his AinsuranceB.

Therefore, Trent may have a difficult time offering his CA services as a profitable business. He cannot manage Alice’s risk of using his PKI because he cannot reasonably evaluate her potential losses, nor can he the pattern of her losses. Current commercial CAs offering insurance set an arbitrary value on each digital certificate they sell, and users cannot customize their coverage. For instance, a VeriSign Class 1 certificate is good for somehow verifying the authenticity of a person’s email address, and includes US\$1000 of insurance coverage. Forgetting the ramifications of offering insurance across multiple legal jurisdictions, such a policy implies that US\$1000 must be sufficient to cover Alice’s loss if email fraud costs her something as tangible as her job, or as intangible as her good name within her company. Therefore, it is doubtful that VeriSign’s insurance is really providing Alice value for her money. In fact, having the CA vouch for the authenticity of an email address is a little strange at best, considering that an independent Internet Service Provider ISP or mailŽ . host provider always provides the email address, and would be in a much better position to vouch for an email AidentityB.

## 2.1.4. Risks of a A signing authorityB

In many corporate situations, an employee is never in direct contact with the CA. Instead, the employer often gives Asigning authorityB to the CA so that the CA can act on the employer’s behalf. Therefore, what is being risked is the employer’s reputation as a Asigning authorityB, not Trent’s reputation. Even though Trent does the signing in this situation, and the employer is not actively involved in the PKI, the employer’s reputation can be ruined! Understanding this type of risk is important because as long as the PKI is only used for internal business, small amounts of internal fraud usually do not affect the employer’s or the employee’s reputations outside of the company.

The dream of PKI designers, however, is that a PKI be used for both internal and external business of the company. In this situation, keeping a pristine reputation may not be so easy in case of fraud. Suppose that Alice works for Carol, Bob works for Dave, and Trent an independent contractor acts as a Ž . CA for everyone. Such a situation is depicted in Fig. 9. Carol would hire Trent to certify Alice, and Dave would hire Trent to certify Bob. Since 1 CarolŽ . trusts Trent, and 2 Dave trusts Trent, they instructŽ .

![](/api/attachments/5SFJWWW9/fulltext/images/7f50578274dfba166009dac90139883ed9910a8f1aa2577282f3a06a04ba95de.jpg)  
Fig. 9. Does the CA or does the employer guarantee an employee’s employment with the employer?

their respective employees 3 Alice and 4 Bob toŽ . Ž . trust Trent as well. Therefore, 5 Alice and BobŽ . would be free to trust each other in a transaction. If Bob is defrauded by a forgery of Alice’s digital signature, we have already examined how Alice or Trent may suffer. But what, if any, is the danger for Carol Alice’s employer ?Ž .

Carol’s risks in this arrangement are not clear because it is not clear who AownsB Alice’s Adigital identityB. With a handwritten signature, there is never any doubt that Alice owns her own signature. If Alice’s handwritten signature is forged, it is primarily Alice’s identity that is compromised. Even though Alice works for Carol and does work on Carol’s behalf, a forgery usually only affects Alice and almost never harms Carol’s reputation. Here, however, Carol has bought Alice’s digital identity from Trent and presumably owns the digital certificate of Alice’s identity. For her personal life, Alice may have bought certification services from a completely different source. Her work identity would belong to Carol, her personal identity would belong to her, and the two identities would have nothing in common. If Alice’s work identity is forged and Bob suffers as a result, Carol’s reputation could be tarnished because she controls Alice’s work identity. This sort of situation has no analogy with current handwritten signatures and notions of identity.

Again, suppose Alice and Bob are communicating, and Alice begins to suspect that her digital signature has somehow become compromised. Can she herself request Trent to revoke her digital identity, or must she make the request through Carol? What if Carol is away on a business trip and cannot respond immediately? What if Alice and Carol believe Alice’s signature to be secure, but Bob accumulates evidence that Alice’s signature has been forged, and sends that evidence to Trent? Can Trent revoke Alice’s identity without consulting, or getting a request from Alice or Carol? No matter what, since Carol is supplying the computer infrastructure needed by Alice to produce digital signatures, if Alice’s signature is forged, Carol’s reputation will suffer.

## 2.2. Trust management Õs. risk management

When we described the risks of using a PKI in the last section, a word we used repeatedly was AtrustB: Alice trusts Carol; Bob trusts Trent; Alice trusts

Trent; Carol trusts Dave; and so on. Although we were discussing risks, we described the PKI creating links of AtrustB among the users. So clearly, the concepts of AriskB and AtrustB are somehow related. We will assume that everyone using the PKI wants to manage his or her risk of using the PKI. Therefore, they will also want to manage their AtrustB as well. But what exactly is Atrust managementB, and how is it related to Arisk managementB? Most PKIs built today, and most laws about PKI, are based on the idea of Atrust management.B However, risk management is an alternative basis for constructing a PKI. In Sections 2.2.1, 2.2.2 and 2.2.3, we will compare trust- and risk-management, and suggest why dealing with AriskB is better than AtrustB.

## 2.2.1. A Trust managementB defined

To define ATrust managementB, we need to understand exactly what we mean by the word AtrustB. According to the original purveyors of PKI, the International Telecommunication Union, AtrustB can be defined in the following manner:

Generally, an entity can be said to AtrustB a second entity when it the first entity makes theŽ . assumption that the second entity will behave exactly as the first entity expects. 27<sup>w</sup> <sup>x</sup>

In terms of using the PKI, the situation seems straightforward, and the relationships among Alice, Bob, and Trent are shown in Fig. 10. Alice 1 asksŽ . her trusted CA for Bob’s public key. Her CA, Trent,

![](/api/attachments/5SFJWWW9/fulltext/images/5dbfeb81ccdf749637dab570b666e6271d5ea3a5ce1ffc21bc9450d12ee8bc90.jpg)  
Fig. 10. Can Bob trust Alice if he does’nt know her, but already trusts Trent?

Ž . 2 gives her a digitally signed certificate telling her what Bob’s public key is. Lastly, 3 she uses thatŽ . public key to communicate with someone who is supposed to be Bob. Alice does not really have to trust Bob in this scenario. Instead, she has to trust Trent to give her the correct public key for Bob. If Trent was less trustworthy, he could give Alice the key of a Mallet, a malicious evildoer, and fool her into believing that Mallet was really Bob. Alice would be totally deceived.

Saying that Alice trusts Trent means that Alice believes that Trent will behave the way Alice expects him to every time she needs his service. So, how can Alice know how Trent will run his CA business? What are his obligations and responsibilities in running the PKI, and how will he carry them out? Unraveling trust models can be a complex undertaking; see Ref. 14 for examples. <sup>w</sup> <sup>x</sup>

To answer these questions of AWho trusts whom, and for what, and why?B, Trent should supply Alice with a thick sheaf of documentation describing exactly what he does to run his PKI, where he runs his PKI, when he operates his PKI, how he operates his PKI, and who helps him operate his PKI. Furthermore, he needs to tell Alice the policies he has toward the use of the certificates he issues. He may not mind Alice relying on his certificate for casual email, but may not want her to rely on them when she discusses nuclear bomb secrets. All this information is bundled together into Trent’s Certificate Practice Statement Ž . CPS and Certificate Policies Ž . CP documentation. In real life, they can amount to quite a mountain of paper. VeriSign’s CPS comes in at 116 pages 25 . Worse yet, the Internet Engineer-<sup>w</sup> <sup>x</sup> ing Task Force IETF has a working group striving Ž . to bring a Public Key Infrastructure using X.509 Ž . PKIX 18 into existence. Their<sup>w</sup> <sup>x</sup> outline of the information a CA should disclose to its clients, RFC-2459, weighs in at 129 pages 3 and even then<sup>w</sup> <sup>x</sup> needs additional documentation to round it out.

To find out what these piles of paperwork mean in real life, try pointing your favorite web browser to VeriSign’s AsecureB web site: https:<sup>rr</sup>www.verisign.com. There is no special significance to Ž VeriSign in this example; any AhttpsB enabled web server would suffice. VeriSign was singled out only to provide a concrete example. After a few mo-. ments, a secure communication channel will be set up between your browser and VeriSign’s server, and the main web page will appear. Public keys, digital certificates, and digital signatures were exchanged— all without you knowing—in order to set up the secure communication link. You made the decision to trust VeriSign as a CA when you decided to use your browser, and VeriSign’s CA dictated that you could trust that Awww.verisign.comB belonged to the VeriSign Inc. Company of California. The extent that you can trust VeriSign is only the extent that you can be assured that they have lived up to the terms and conditions of their CPS. Whether or not you can trust the security of your communication with Awww.verisign.comB is a completely separate matter. Almost every commercial https-enabled browser is distributed with VeriSign enabled as a trusted CA. This includes Netscape Navigator, Microsoft Internet Explorer, Sun’s HotJava, Lotus Notes, and Opera’s browser. You can see the contents of the digital signatures under Netscape or Explorer by clicking on the golden padlock icon, located on the top menu bar or the bottom of the browser window, respectively.

For instance, in the US, Mallet could easily obtain a VeriSign certificate, set up a web site, and defraud every visitor. In this case, VeriSign would have no liability toward those who were defrauded because VeriSign’s CPS says that VeriSign only promises to check the names of the people to whom it issues certificates. VeriSign does not check that it is safe for Alice and Bob to do business with them. In practice, Internet CAs usually need only rudimentary forms of identification, and their digital certificates usually cost only US\$10 to US\$200.

In summary, Atrust managementB is like dealing with what an engineer would call a Awhite-boxB: a mechanical box that we can open up and inspect the inner workings. Such a white-box is shown in Fig. 11. Every time you request a public key in from theŽ . CA theŽ . Ž . Awhite boxB you get a public key out as an answer. The CPS and CP documents allow us to peer into the inner workings of the PKI machinery inside the white-box and let us verify that the box is properly doing its documented job. It may be producing flawed, unreliable, or useless output, but the white-box approach only verifies that the box—and hence trust—is producing results in accord with documented procedures.

![](/api/attachments/5SFJWWW9/fulltext/images/f2d46b50ebb0abeb61a4c5e3d328cb862dd87783d4ae0d8b770f36305aebe86a.jpg)  
Fig. 11. A Awhite-boxB process with well-defined inputs and outputs.

## 2.2.2. A Risk managementB defined

In theory, a well-designed white-box should never fail. Contentious design and rigorous peer review should ensure that the white-box correctly handles any input. The operating specifications of the whitebox process are available for review, so as a whitebox user you can theoretically verify for yourself that the white-box is robust, reliable, and well designed. In practice, however, the situation is not that simple.

There are two issues that make trusting a whitebox process complicated. The first issue can be posed as a question: does knowing the operational parameters of a process or machine make using that process or machine any safer? Consider a modern passenger jet such as the Boeing 777. To the average passenger, the airplane’s wings may look far too small to lift such a large fuselage. Boeing has thousands of pages of documentation detailing the 777’s flight characteristics and operational parameters, but if Alice doubted the air-worthiness of the plane, it’s doubtful that any of that documentation would reassure her. After all, it would take months for her to read Boeing’s evidence, never mind the years of specialized training she would need to understand what it all meant.

What if Alice was trying to decide on the trustworthiness between two CA services, one operated by Bob and another operated by Carol? In theory, Alice could decide by obtaining each of Bob’s and Carol’s Certification Practice Statements, reading them, and comparing their PKI operations. In practice, that’s quite unlikely to occur. A CPS is typically over a hundred pages long, and filled with a lot of technical arcana. Bob does nightly off-site backups . . . but Carol has a mirrored data-center. Which is better? Bob uses FIPS-140-1 certified software . . . but Carol is getting certified under ISO-IS-15408. Does it make a difference? If so, how much? Bob offers a Afraud insuranceB program, and has processed several claims for forged digital identities . . . Carol has no such program, but has never had any of her certified identities forged. Which scenario is preferable?

The second issue that complicates AtrustingB a white-box process has to do with the messy nature of real life. Just like any other machine, a PKI can fail for many unforeseen reasons. Like a modern passenger aircraft, a PKI should be designed from the ground up to be safe and reliable. For the most part, the aircraft and the PKI will function efficiently and well. But no amount of design can stop the occasional airplane from going down in flames, and we should not expect any different behavior from a PKI. After all, neither an airplane nor a PKI can be totally safe from an intelligent, patient, and well-funded terrorist. Trent may operate exactly the way his CPS specifies, and Alice may always trust him to always do so. But what if Alice sustains a loss due to Trent anyway? She could lose something as tangible as money, or as intangible as her reputation. What if she sustains her loss even though Trent never violates the terms in his CPS?

Clearly, Alice takes a risk when she decides to use the PKI, even though she trusts the PKI’s operator. For Alice to feel safe, she needs to know that she will not suffer too badly no matter how Trent’s PKI fails. By limiting the potential damage she may suffer, Alice manages her risk of using Trent’s PKI. In other words, risk management looks at the operations of the PKI like an impenetrable Ablack-boxB Ž . to use engineering terms again as shown in Fig. 12. As input, the black-box processes a question such as AWhat is Alice’s public key?B On output, it should provide her current public key. If the black-box provides the wrong key, or no key at all, Alice may not care why the black-box did not work, but she will definitely want assurances that the black-box failure will not send her to jail, or ruin her life! Alice will only use the PKI if it is constructed in a manner that allows her to manage her risks. It is doubtful that she would ever let Trent manage her risks for her. Doing so would be like asking the banks AWhich bank is the safest bank?B or asking the airlines AWhich airline will look after me the best?B Alice is the only person who is guaranteed to put her own self-interest first.

![](/api/attachments/5SFJWWW9/fulltext/images/855b2a042bbecbdcc2e3ac0216df32325aa1b538e00b71da5a672b3d09370f88.jpg)  
Fig. 12. A Ablack-boxB process with well-defined inputs and outputs.

There are may ways to formally define the phrase Arisk managementB, but the simplest definition comes from Ron Dembo 1 , a mathematician and founder <sup>w</sup> <sup>x</sup> of Algorithmics <sup>w</sup> <sup>x</sup> 11 a Toronto-based company that specializes in financial risk management. Paraphrasing from Dembo, we define

the risk an asset is exposed to can be measured as the potential difference between the asset’s value now and at some point in the future, due to differences in the environment 1 .<sup>w</sup> <sup>x</sup>

The asset in question could be as tangible as the money in your wallet, or as intangible as your reputation. With our definition, it does not matter how the asset interacts with the environment. After all, you can keep your money in a well-hidden safe, but rampant inflation will diminish its buying power just as surely as if it had been stolen. Further, our definition acknowledges that some assets are intrinsically difficult to peg with a dollar value. A faulty credit report can do untold damage to your financial standing, yet it can be impossible to guess a priori the dollar value of your reputation.

Lastly, our definition shows that risk changes over time. That is why merchants check the validity of your credit card with eÕery transaction, if possible. Someone could begin fraudulently using your credit card number at any moment. Therefore, risk management has to be an ongoing process, with the risk being re-evaluated at every transaction.

Our point is that risk can be measured, and therefore managed. In fact, many of our laws, customs, and ways of doing business have evolved from triedand-true risk management techniques. When faced with a risk, you can

accept residual risk, if the loss will not be too great,

hedge your bets, planning contingencies to handle any outcome,

insure against any possible future loss,

enter into contracts that legally assign liability and remedies, or

rely on legislation and current laws to provide you with protection.

To understand how risk management relates to a PKI, we need to restate the main purpose of a PKI. A PKI allows other people to rely on the validity of your public key. The fact that someone can rely on your public key is a valuable fact—it is valuable to you and it is valuable to the relying party. Since the reliance is valuable, you can consider it an asset. And the value of any asset, financial or otherwise, is always subject to risk.

2.2.3. A Trust B and A risk B define A structural stabil-$i t y ^ { , 9 }$

So far, we have discussed the theoretical differences between AtrustB in a PKI, and Arisk managementB in a PKI. What we have not discussed is whether or not these theoretical differences result in any practical differences, as far as the average PKI user is concerned. Does it really make a difference to Alice if her bank creates a PKI featuring Atrust managementB vs. Arisk managementB? Absolutely!

For instance, we have already seen how the credit card industry has structured it service such that the card issuer, the merchant, and the card holder are all subject to reasonable amounts of risk for the reward of being able to use the convenience of plastic. But does the concept of AtrustB appear in any other aspects of the banking industry? Certified check services, for instance, are often widely described as Aa bank acting as a trusted intermediary between two individuals, one of whom needs to transfer money to the otherB.

In reality, nobody really AtrustsB anybody in such a situation. Suppose Alice wants to give Bob a certified check. Alice can go to Carol at her bank, obtain the check, and give it to Bob. Bob can take the check, and give it to Dave at his bank for deposit to his account. So at first glance, it looks like Dave is trusting Carol to honor the certified check that she issued. In reality, Carol and Dave can issue and cash certified checks because they both belong to the same Acertified check clearinghouse networkB. The clearinghouse has strict rules for membership, because certified checks have to be reliable. Carol and Dave will probably honor the terms of clearinghouse membership because being able to offer certified check services is a valuable service for them to offer. If there is a problem in clearing the check, the clearinghouse handles the matter internally, among Carol, Dave, and other clearinghouse members. In fact, Bob does not even have to trust Dave to properly clear the check. The clearinghouse would ensure that Bob gets his cash, again, because it is in their self-interest to maintain certified checks as high-quality financial instruments. So in reality, everyone involved in the certified check system takes a risk in handling certified checks. But the clearinghouse system acts to manage the risk, distributing the risk in such a way that everyone’s self-interest and financial benefit is served when the system runs smoothly.

In fact, an in-depth analysis of almost any currently used transaction system, such as consumer credit rating agencies or modern contract laws, shows that widely used or widely deployed systems must always manage the risk of using the system. Why is that? The answer has to do with the concept from dynamical systems theory called structural stability. Focusing again on PKI, we can call a PKI Astructurally stableB if the PKI remains generally reliable even if the PKI does not work properly on rare occasion. On the other hand, if one bad digital signature or forged identity undermines everyone’s confidence in the PKI, we call it Astructurally unstableB because one small mishap causes the whole infrastructure to totter over and collapse.

We contend that trust-based systems are inherently unstable, because the value of the system is based solely on the reliability of the trusted party— and nobody is universally reliable. If Alice trusts her

CA, it only means that she believes her CA will live up to the level of service promised in the CPS. Alice may trust her CA to follow their CPS, but can she afford to repeatedly risk everything she owns on that assumption? Probably not . . . not unless she is assured that the CA always has her best interests at the forefront.

There is one further point to mention. We have asserted that a PKI has to be structurally stable because it must remain reliable if the occasional digital forgery appears. But do we really have to worry about digital forgeries? After all, a PKI is built using cryptography, and most vendors will assure us a cryptographic signature could not be forged with billions of years, billions of dollars, and billions of computers. Is all this hoopla about structural stability much ado about nothing?

As we will show in the next few sections, structural stability is very important in a PKI, and we prove this by making two points. First, the integrity of a PKI that is secured only through cryptography can be totally destroyed by the presence of a single digital forgery, implying that a crypto-only PKI is structurally unstable. Then we show that not only are digital forgeries possible, they are fairly easy to produce even with the best cryptography available. Therefore, structural stability is a fundamental requirement in a PKI, not a luxury. We end by noting that although the next few sections focus mainly on managing public keys for digital signatures, similar arguments and examples apply to managing encryption public keys as well.

## 3. Consequences of digital forgery

Paradoxically, handwritten signatures are seen as a AsecureB method of endorsing a document because they are relatively cheap and easy to forge. Current legal and administrative practices dealing with handwritten signatures or easily forged things, such as PINs codes or credit card numbers do not pretend that transactions involving these codes are even tricky to fake.

In contrast, most people believe, and many laws codify the idea, that digital signatures are unforgeable because they use cryptography. Therefore, if a digital signature cannot be forged, then we always expect that Alice to have signed a document bearing her digital signature. We AtrustB that the crypto and the PKI work to together to create a secure signature, and that implies that we can AtrustB the PKI and the CA that operates it.

As an academic exercise, let us play ADevil’s AdvocateB and suppose that despite having a remarkably detailed and stringent operating practice, Alice finds a message bearing her digital signature that she is sure that she did not sign. It could be that she signed it accidentally, or it could be that she had honestly forgotten to sign it. Actually, perhaps Alice remembers signing the document, but does not want to own up to the action. Worse yet, perhaps her archenemy Mallet has maliciously stolen her key, and is now masquerading as Alice in cyberspace!

Theoretically, such a Akey compromiseB event creates no problems for Alice. Most likely, the Certificate Policies CPs and CPS to which she isŽ . bound obligate her to notify her CA of the forgery so she can have the CA certify a new public key. Her situation is similar to calling a credit card company, asking them to issue you a new card number. Since Trent, Alice’s CA, is a trustworthy fellow, he immediately does what his CPS says he will do: he revokes Alice’s old key, and certifies her new one. Alice takes her new key and gets back to work. End of story. Or is it?

Over the next few weeks, Alice’s co-worker Bob notices that Alice seems to be disavowing quite a number of her old messages that were signed with her old public key. It seems to him that every time a message turns up that was embarrassing or detrimental to Alice, she claims that she did not really sign the message. Her old key was compromised, after all . . . she would never have signed such a thing . . . it must have been Mallet trying to malign her good name . . . So, is Alice being honest as the unwitting victim of character assassination, or has she discovered an easy way to disavow past mistakes? What is poor Bob to believe? Alice had used her old public key for over a year, and had signed many hundreds of messages with it. No one bothered keeping them in secure storage because, by definition, they were secured with cryptography.

The presence of that one digital forgery destroyed Bob’s faith in the integrity of the PKI. Even though Alice, Bob, and Trent all performed their duties as expected, and could be trusted to do so again, the security of the PKI was structurally unstable, rendering it non-existent. Conventional PKI technology, built with the ideas of Atrust management,B will only be reliable and secure if nobody ever writes a description of how to forge a digital signature.

## 3.1. How to forge a digital signature

Forging a digital signature is actually quite easy as long as you forget trying to break the mathematics. It is a good thing for criminals that there’s more to the world than abstract algebra. For instance, one of the old tried-and-true methods of obtaining a key works whether the keys are strings of digital bits or cut pieces of metal. The malicious Mallet need only kidnap Alice’s pet cat and threaten it with grievous bodily harm if Alice does not give him her public key. Cryptographers call this technique Arubber hose cryptographyB.

If Mallet wants to be slightly more refined, he can peek over Alice’s shoulder and surreptitiously record her password. If Mallet and Alice work in the same office, he could probably just install a virus, Trojan horse, or other piece of AmalwareB that would record Alice’s password as she typed it in. In fact, there are many books, such as Refs. 5,30 , that detail a<sup>w</sup> <sup>x</sup> plethora of the surprisingly many and varied ways that Mallet can infiltrate a computing infrastructure. All of these attacks would be successful against poor Alice because she is dependent on her computer to perform the cryptographic operations that result in her digital signature. If that computer is no longer secure, then neither is Alice’s public key.

The obvious solution to this sort of problem is to never allow Alice’s public key to be placed on untrusted hardware. Instead of Alice’s desktop computer performing the digital signature, Trent can specify that Alice’s public key must always reside on a tamper-resistant smartcard, with the smartcard itself being the only computer ever to see the public key. Trent can even specify that Alice use advanced biometric techniques, such as fingerprint and retinal scans, to enable her smartcard’s operation. In fact, many active PKIs today operate with exactly these constraints, believing that it makes them much more secure and trustworthy. Like many obvious solutions, however, none of these security measures necessarily work. It is more than the fact that tamper-resistant is not the same thing as tamper-proof, implying that with enough effort any smartcard can be broken. Alice’s key remains susceptible to theft since her office has budgetary cost constraints. The budget ensures that Alice will undoubtedly work with her email, spreadsheets, and databases using commodity hardware and software. She only uses her trusted computing hardware her smartcard to digitally signŽ . documents, not work with them.

To a AhackerB the security flaw is obvious. To digitally sign a document, Alice’s computer must transmit it to the smartcard device. Alice, not having voltage probes in her fingers and being unable to decode RS-232 or USB impulses unassisted even if she did, must trust that her unsecured computer is transmitting the right document, and the right document alone, to her smartcard for signing. A smart malware hacker could easily trick her computer into transmitting any document they wanted to her smartcard. Alice would never know. Alice’s only defense is to obtain a much better computer, one that is tamper-resistant, and runs only secure software. Such a machine would be very expensive to build, even more expensive to program, even more again expensive to maintain, and probably quite inconvenient to use. In fact, Bob, Carol, Dave, and all of Alice’s co-workers in the PKI would have to use similar machines to prevent compromise of their keys as well. Some organizations, such as the military, have such stringent security standards that they are willing to bear the time and expense to install such a system, but few others can afford it.

Even if such a tamper-proof computing system were to become widespread, it would, by definition, be a commodity, and every hacker in the world would be searching for, and finding, previously unsuspected vulnerabilities. We have to conclude that cryptography only makes it a little more difficult to forge a digital signature, not impossible. For instance, the digital satellite broadcast community has continually needed to relearn the point that cryptography is not equal to security. Over the years, hundreds of encryption techniques have been used to protect pay-per-view satellite data, with almost all of them requiring the viewer to install tamper-resistant smartcards into their satellite receivers. Despite the use of tamper-resistant hardware though, it often takes the hacker communities only a few hours to crack new protection schemes 8 .<sup>w</sup> <sup>x</sup>

## 3.2. When is a digital signature forged?

When we discussed the consequences of Alice discovering a digital forgery in her name, the reader may have noticed the critical role of time. Alice notified Trent of the compromise since her CP and CPS obligate her to do so as soon as she became aware of it. But what would be the consequences if it took a long time for Alice to discover the compromise? What if Alice forgets to notify Trent, or Trent loses her notification message? What if Alice never learns of the compromise at all? Any of these scenarios could be disastrous for Alice or the people relying on her public key. If Mallet were careful, he would have free reign with a criminal’s Holy Grail: an untraceable counterfeiting tool! Alice, Bob, and all of their friends could never really trust the security of their PKI again.

Therefore, for a PKI to remain secure, knowing when a key compromise occurred is just as important as knowing about the compromise in the first place. In an attempt to reliably document when digital signatures are created, cryptographers have invented entities called Acyber-notariesB to deal with new creations such as digital time-stamping protocols and other novel crypto-techniques 9 . The cryptogra-<sup>w</sup> <sup>x</sup> pher’s reasoning is that since we cannot trust the PKI to tell us when a potential fraud occurs, we have to trust an outside stranger to vouch for when and how every digital signature was made. If we really examine the issue, however, we see that a cyber-notary really does not help us discover when a key compromise truly occurred. If every document is timestamped, it may prevent Mallet from backdating a forged document, but it certainly does not prevent him from wreaking havoc in any other way. In fact, giving special legal powers to cyber-notaries may be a dangerous thing to do, and doing so may risk the integrity of our social fabric. After all, if cryptography does not imply AperfectB security, we should not enact laws that give digital signatures special status.

As an interesting aside, despite how important computers are in everyday business, no one really has much experience with relying on digital signatures to provide a secure basis for e-commerce.

Giving CAs special legal powers may be the equivalent of creating an e-commerce Apolice state,B for all we know. The issue is too important for regulators to simply guess what the results of new regulations will be.

## 3.3. Digital signatures are not A legal signaturesB

Arguably, digital contract formation is perceived as one of the most important applications of digital signatures. PKI creators argue that since digital signatures are supposedly unforgeable, it should be much harder to repudiate disavow a digitally signed Ž . contract than a handwritten one. Such an argument is flawed because it presumes that the act of signing a contract plays a legal role in binding the parties to the terms of the contract. In reality, a contract is formed by what is termed Aan exchange of consent.B In legal-speak, it is called the Asubstantive rule of formation of contract.B Translated for non-lawyers, this means that the law binds parties to the terms of a contract when those parties consent to the terms of the contract between them. The signature and even the piece of paper the contract may be written on are strictly incidental! We note that different legal juris-Ž dictions have different interpretations of the law. For simplicity, we describe the law as it applies to the most of the US states and Canadian provinces..

So, if signatures are not required to create a contract, why are they so important in contemporary commerce? Suppose that Alice and Bob have a contract between them, and Alice decides to renege on her contractual obligations. Bob would then seek redress in the courts, and the first thing the court would require is proof that Alice consented to the contract in the first place. How consent is proven is the domain of evidentiary law, and it is here where signatures become important. A signature can be defined as any act that unambiguously signifies that consent has been achieved. There is nothing magic about a written name; a signature can even be an AXB marked on a piece of paper, as was frequently the case when illiteracy was more prevalent. In Japan and other Asian countries, special stamps known as AchopsB are used to signify consent, not a handwritten name. In fact, Japan has two different types of chops: those used for everyday transactions, and those used for important, high value transactions.

The AimportantB chops must be registered with the government to be before they may be used or relied on.

How much evidence is necessary to prove consent? After all, most types of conventional signatures can be easily forged. So why is fraud not completely rampant in society? In keeping with the principles of good risk management, current laws dictate that the weight of the evidence must be proportional to the value of the contract. For instance, if you buy an apple from the local grocery store, you have actually completed a contract with the grocer to exchange your money for their apple. The value of the transaction is so low that nothing needs to be written down, and no record of the transaction will probably ever be kept. In contrast, the exchange of real estate can be so important that the courts have deemed that no AverbalB contract can deemed trustworthy enough by evidentiary law to prove consent.

Therefore, for a digital signature to be legally binding, it must satisfy the laws and current conventions of evidence. We have shown, however, that due to the structural instability of a PKI based on cryptography alone, digital signatures by themselÕes are not secure, and therefore should not be completely trusted. In legal-speak, the digital signature should not have a heavy eÕidentiary weight. However, since digital contract signing is such a valuable thing to be able to do, many groups have advocated or even enacted laws that dictate a priori that digital signatures are always trustworthy. In some cases, such as with the American Bar Association ABA ,Ž . there are even proposals to invent a type of AsignatureB that by legislative fiat, can never be forged! ŽSome lawyers may disagree with such an interpretation. For the texts and interpretations of the actual laws in question, see Ref. 10 , especially the section on the Utah legislation..

Fortunately, in recent months there have been a number of state<sup>r</sup>provincial, federal, and international proposals to allow PKIs to be used in e-commerce as long as the PKI follows the principles of good risk management. These new technology-neutral laws dictate that consent must always be proven by context, and cannot be proven just by technology. Guidelines on how to deal with digital signatures have been issued by policy groups such as the American Bar Association ABA , the United Na-Ž .

tions Commission on International Trade Law UN-Ž CITRAL , the US National Conference of Commis-. sioners on Uniform State Laws NCCUSL , the Uni-Ž . form Law Conference of Canada ULCC , and theŽ . Organization for Economic Co-operation and Devel opment OECD . Legislation, such as Canada’s pro- Ž . posed Uniform Electronic Commerce Act UECAŽ . or America’s National Conference of Commissioners on Uniform State Laws NCCUSL , have only re-Ž . cently been signed into law, but very little is known how the courts will interpret these new laws, and even less is known about the laws’ long-term implications. Therefore, it is crucial that the role and consequences of nonrepudiation in a public key infrastructure be clearly understood.

For an example of how these laws can modify the interpretation of a digital signature, consider the digital signature capabilities of the two most popular email clients in the world, Netscape Messenger and Microsoft Outlook. Each of these programs has a configuration checkbox buried in its configuration settings that allows the user to Asign every message by default.B The very fact that these checkboxes exist could be used to argue that the digital signature of a message was Asomehow added by the computer,B and did not imply that the user consented to the content of the message. Therefore, a signature is not a signature, if something is always signed! There are infinite variations on the theme of default signatures: there could be two types of signatures, one used to signal consent, and another just to authenticate the message. We could have users specifically designate messages where they felt that the signature designated consent . . . and so on. The failing that most of these arguments have is that they all imply that the signature in some way implies consent, whereas we argue that consent must always be contextual.

Some pundits argue that new laws are not necessary at all in PKI regulation since the use of digital signatures in commerce can be regulated by contractual agreements between users and their CA, and between different CAs. Inter-CA agreements, called Across certificationB agreements, although they look straightforward, are really a legal minefield containing explosive unresolved issues such as Athird party liabilityB problems, Anon-contracted obligationB difficulties, and other risks that we have already noted in passing. More detail on these subjects can be found in Refs. 13,19 . We conclude that legislation<sup>w</sup> <sup>x</sup> alone is not enough to manage the risks of using or operating a PKI. So if legislation is not enough, how do we do Adamage controlB if there is fraud within a PKI?

## 3.4. Damage control: when and how

We have established that a trust based PKI is structurally unstable, that it is relatively simple to forge a cryptographic signature, and that contracts and legislation are not sufficient to mitigate the risks inherent in using the PKI. So, can we use a PKI to bring authenticity, integrity, and confidentiality to digital commerce, and if so, how? Another way of stating the same question is Aif context provides intent, then how do you show context?B If we examine these two questions and the relationship between them, we have to conclude that digital signatures alone are not secure because the digital signature cannot provide context. Therefore, the signature, and hence the PKI will be secure and reliable if and only if we can record the context in which a document was signed. So our questions about the security of the PKI can be boiled down to one core question: how can we reliably record the context of a signature?

## 3.4.1. Showing compromise by audit trails

As any forensic accountant can tell you, the only reliable way to prove fraud is to have an audit trail of your transactions. An accountant’s ledger tracks where money went and what it was used for. Similarly, a PKI should track what documents were signed, and how the signatures were relied on. In other words, accounting for and auditing the use of the PKI create structural stability. Of course, nothing is quite as simple as it may seem. For instance, the danger of auditing every transaction in a PKI is that there would be no privacy or confidentiality for the PKI users. Unfortunately, a detailed treatment of privacy and confidentiality issues in a PKI would take us too far afield, so we do not pursue them. Similarly, a properly detailed discussion of the techniques of auditing transactions, such as the use of routine checks, internal controls, and so on, would also take us far afield of the current discussion. Instead, we will briefly summarize why auditing and accounting are so important in risk management, and briefly touch on how a PKI can be audited.

## 3.4.2. Auditing yields compromise containment

The conclusion we have been leading to is that if transactions involving the PKI can be audited, then the appearance of one, two, or even several forged messages does not imply that the PKI is no longer trustworthy. In fact, in a rigorously audited PKI it may be possible to even pinpoint when, where, and how a key compromise occurred.

However, auditing a PKI is not a trivial procedure. It is more than just keeping a record of signed messages. For instance, most businesses would like to add digital signature and encryption features to their routine email. A busy employee may easily send tens of messages per day, and receive upwards of a hundred. Multiplying these figures by 10–50,000 employees and it soon becomes clear that rigorous accounting for digital signatures is impossible for every little piece of communication! In other words, even though a short routine message may bear a digital signature, it still must be believed with caution, despite the use of cryptography!

In the end, the method of communication that we have just discussed is exactly how business communication occurs today. Imagine a business that routinely audits eÕery phone call, eÕery piece of mail, and eÕery handwritten note that its employees were involved in. Such a business would spend a lot of money never getting anything accomplished. This example should be kept in mind when creating an audit structure for a PKI.

## 3.4.3. AÕailable auditing tools and technologies

Cryptography not only lets people create digital signatures and keep their messages private, but can help create audit logs that are very difficult to tamper with. Currently, no PKI software exists that audits the transactions in the PKI in any useful manner. The closest systems come from Entrust Technologies, although they only keep an audit log of actions taken by the CA. The PKI users are left to their own devices.

It is a good thing that cryptographers are a resourceful bunch. Creating a PKI with rigorous accounting and auditing that preserves the confidentiality and anonymity of its users is perhaps the next great challenge of the e-commerce revolution. Only the tried-and-true techniques of risk management, where AtrustB is not an issue, will allow business to proceed on fast-tracked Internet time.

## Acknowledgements

The author would like to acknowledge and thank Bonnie Deroo and David Masse for their thoughtful contributions to this article, as well as the PKI team at Securify for every facet of their support.

## References

<sup>w</sup> <sup>x</sup> 1 R.S. Dembo, A. Freeman, Seeing Tomorrow: Weighing Financial Risk in Everyday Life, McClelland & Stewart, Toronto, Canada, 1998, April, ISBN 0-7710-2612-9.

<sup>w</sup> <sup>x</sup> 2 W. Ford, M. Baum, Secure Electronic Commerce: Building the Infrastructure for Digital Signatures and Encryption, Prentice-Hall, Saddle River, NJ, 1997, April, ISBN 0134763424.

<sup>w</sup> <sup>x</sup> 3 ftp:<sup>rr</sup>ftp.isi.edu<sup>r</sup>in-notes<sup>r</sup>rfc2459.txt.

<sup>w</sup> <sup>x</sup> 4 S. Garfinkel, G. Spafford, Web Security and Commerce, O’Reilly & Associates, Cambridge, MA, 1997, June, ISBN 1565922697.

<sup>w</sup> <sup>x</sup> 5 A.K. Ghosh, E-Commerce Security: Weak Links, Best Defenses, Wiley, New York, 1998, ISBN 0471192236.

<sup>w</sup> <sup>x</sup> 6 http:<sup>rr</sup>csrc.nist.gov<sup>r</sup>fips<sup>r</sup>fips1861.pdf.

<sup>w</sup> <sup>x</sup> 7 http:<sup>rr</sup>federalreserve.gov<sup>r</sup>boarddocs<sup>r</sup>rptcongress<sup>r</sup> creditcard<sup>r</sup>1999<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 8 http:<sup>rr</sup>www.2600.com<sup>r</sup> and http:<sup>rr</sup>www.hackernews. com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 9 http:<sup>rr</sup>www.abanet.org<sup>r</sup>scitech<sup>r</sup>ec<sup>r</sup>cn<sup>r</sup>home.html.

<sup>w</sup> <sup>x</sup> 10 http:<sup>rr</sup>www.abanet.org<sup>r</sup>scitech<sup>r</sup>ec<sup>r</sup>isc<sup>r</sup>digital.html.

<sup>w</sup> <sup>x</sup> 11 http:<sup>rr</sup>www.algorithmics.com<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 12 http:<sup>rr</sup>www.cert.dfn.de<sup>r</sup>eng<sup>r</sup>team<sup>r</sup>ske<sup>r</sup>pem-dok.html.

<sup>w</sup> <sup>x</sup> 13 http:<sup>rr</sup>www.cryptonym.com<sup>r</sup>research<sup>r</sup>rsa97<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 14 http:<sup>rr</sup>www.entrust.com<sup>r</sup>downloads<sup>r</sup>pdf<sup>r</sup>trustmodels.pdf.

<sup>w</sup> <sup>x</sup> 15 http:<sup>rr</sup>www.equifax.com.

<sup>w</sup> <sup>x</sup> 16 http:<sup>rr</sup>www.fdic.gov<sup>r</sup>consumer<sup>r</sup>consnews<sup>r</sup>spr98<sup>r</sup>crook. html.

<sup>w</sup> <sup>x</sup> 17 http:<sup>rr</sup>www.gte.com<sup>r</sup>cybertrust<sup>r</sup>index.html.

<sup>w</sup> <sup>x</sup> 18 http:<sup>rr</sup>www.ietf.org<sup>r</sup>html.charters<sup>r</sup>pkix-charter.html.

<sup>w</sup> <sup>x</sup> 19 http:<sup>rr</sup>www.law.tm<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 20 http:<sup>rr</sup>www.privacy.org<sup>r</sup>pi<sup>r</sup>intl orgs <sub>–</sub> <sup>r</sup>ec<sup>r</sup>eudp.html.

<sup>w</sup> <sup>x</sup> 21 http:<sup>rr</sup>www.thawte.com.

<sup>w</sup> <sup>x</sup> 22 http:<sup>rr</sup>www.transunion.com.

<sup>w</sup> <sup>x</sup> 23 http:<sup>rr</sup>www.verisign.com.

<sup>w</sup> <sup>x</sup> 24 http:<sup>rr</sup>www.verisign.com<sup>r</sup>netsure<sup>r</sup>plan.html.

25 https:<sup>rr</sup>www.verisign.com<sup>r</sup>repository<sup>r</sup>CPS1.2<sup>r</sup>.

<sup>w</sup> <sup>x</sup> 26 https:<sup>rr</sup>www.verisign.com<sup>r</sup>repository<sup>r</sup>CPS1.2<sup>r</sup>CPSCH7. HTM.

<sup>w</sup> <sup>x</sup> 27 ITU-T Recommendation X.509 1997 Ed. : InformationŽ . Technology, Open Systems Interconnection - The Directory: Authentication Framework http: Ž . <sup>rr</sup>www.itu.int<sup>r</sup> .

<sup>w</sup> <sup>x</sup> 28 A. Menezes, P.C. Van Oorschot, S. Vanstone, Handbook of Applied Cryptography, CRC Press, Boca Raton, FL, 1996, October, ISBN 0849385237.

29 B. Schneier, Applied Cryptography: Protocols, Algorithms, and Source Code in C, 2nd edn., Wiley, New York, 1995, October, ISBN 0471128457.

<sup>w</sup> <sup>x</sup> 30 B. Schneier, Secrets and Lies: Digital Security in a Networked World, Wiley, New York, 2000, September, ISBN 0-471-25311-1.

![](/api/attachments/5SFJWWW9/fulltext/images/ecec575ba177b0a933fd02b3aeab59766bf4f7e28e8c6283ce064767324f2609.jpg)

Andrew Fernandes is a mathematician and a programmer specializing in cryptography, public key infrastructures, and risk management. Over the past few years, he has worked at helping companies analyze the risks inherent in their secure communications infrastructures, designing new and modifying old ecommerce protocols, and evaluating security software, hardware, firmware, and wetware. Recently, he has worked jointly with legal and financial professionals to

analyze the impact of digital signature and e-commerce legislation on modern business practices.
